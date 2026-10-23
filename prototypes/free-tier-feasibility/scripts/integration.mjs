#!/usr/bin/env node
/**
 * Integration harness for the free-tier feasibility spike.
 *
 * It starts `wrangler dev` (local workerd + local D1), drives the HTTP and
 * scheduled paths, and asserts the properties the gates care about.
 *
 * It uses the LOCAL runtime. Nothing here is evidence of a deployed run; the
 * deployed measurements are recorded separately in the feasibility report.
 */

import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "..");
const PORT = Number(process.env.SPIKE_PORT || 8787);
const TOKEN = process.env.SPIKE_TOKEN || "local-test-token";
const BASE = `http://127.0.0.1:${PORT}`;
const TURN_MS = 7200 * 1000;

const results = [];
function check(name, ok, detail) {
  results.push({ name, ok, detail });
  console.log(`${ok ? "PASS" : "FAIL"}  ${name}${detail ? `  — ${detail}` : ""}`);
}

async function call(method, route, { token = TOKEN, body } = {}) {
  const res = await fetch(BASE + route, {
    method,
    headers: token ? { "x-spike-token": token } : {},
    body,
  });
  const text = await res.text();
  let data;
  try {
    data = JSON.parse(text);
  } catch {
    data = { raw: text };
  }
  return { status: res.status, data };
}

async function waitForHealth(timeoutMs = 90000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    try {
      const res = await fetch(BASE + "/health");
      if (res.ok) return res.json();
    } catch {
      // not up yet
    }
    await new Promise((r) => setTimeout(r, 500));
  }
  throw new Error("wrangler dev did not become healthy within " + timeoutMs + "ms");
}

function startDev() {
  const wrangler = path.join(root, "node_modules", "wrangler", "bin", "wrangler.js");
  if (!existsSync(wrangler)) throw new Error("wrangler is not installed; run npm install first");
  const args = [wrangler, "dev", "--port", String(PORT), "--test-scheduled", "--var", `SPIKE_TOKEN:${TOKEN}`];
  const child = spawn(process.execPath, args, {
    cwd: root,
    env: { ...process.env, WRANGLER_SEND_METRICS: "false" },
    stdio: ["ignore", "pipe", "pipe"],
  });
  child.stdout.on("data", (d) => process.stdout.write("[dev] " + d));
  child.stderr.on("data", (d) => process.stderr.write("[dev] " + d));
  return child;
}

function stopDev(child) {
  if (!child || child.killed) return;
  if (process.platform === "win32") {
    spawn("taskkill", ["/pid", String(child.pid), "/T", "/F"], { stdio: "ignore" });
  } else {
    child.kill("SIGTERM");
  }
}

const expectedDelta = (id) => 10 + (id % 7);
const expectedSum = (n) => {
  let sum = 0;
  for (let id = 1; id <= n; id += 1) sum += expectedDelta(id);
  return sum;
};

async function main() {
  const dev = startDev();
  let exitCode = 0;
  try {
    const health = await waitForHealth();
    check("worker boots and serves /health", health.ok === true, `slot ${health.current_slot}`);
    check("health advertises the 12/day product cadence", health.product_cron === "0 */2 * * *", health.product_cron);

    const page = await fetch(BASE + "/");
    const pageText = await page.text();
    check("browser page is served as HTML", page.ok && pageText.includes("feasibility spike"), `HTTP ${page.status}`);

    const unauth = await call("POST", "/api/spike/init", { token: null });
    check("spike routes reject a request with no token", unauth.status === 403, `HTTP ${unauth.status}`);

    const init = await call("POST", "/api/spike/init", { token: TOKEN });
    check("schema initialises (idempotent DDL)", init.status === 200 && init.data.ok === true, `HTTP ${init.status}`);
    const init2 = await call("POST", "/api/spike/init", { token: TOKEN });
    check("schema initialisation is repeatable", init2.status === 200 && init2.data.ok === true);

    const N = 250;
    const seed = await call("POST", `/api/spike/seed?n=${N}&reset=1`);
    check("synthetic dataset seeds", seed.status === 200 && seed.data.nations === N, `N=${N}`);

    const base = Math.floor(Date.now() / TURN_MS) - 20;

    // --- exactly-once -------------------------------------------------------
    const first = await call("POST", `/api/spike/resolve?slot=${base}&batch=100`);
    check(
      "one invocation resolves the whole world",
      first.data.outcome === "completed" && first.data.applied === N,
      `outcome=${first.data.outcome} applied=${first.data.applied} batches=${first.data.batches}`,
    );
    const firstMetrics = first.data.metrics || {};
    check(
      "completed run reports rows written and db size",
      firstMetrics.rows_written > 0 && firstMetrics.db_size_after > 0,
      `rows_written=${firstMetrics.rows_written} rows_read=${firstMetrics.rows_read} requests=${firstMetrics.requests} statements=${firstMetrics.statements}`,
    );

    const repeat = await call("POST", `/api/spike/resolve?slot=${base}&batch=100`);
    check(
      "a repeated trigger for the same slot is a no-op",
      repeat.data.outcome === "noop",
      `reason=${repeat.data.reason}`,
    );

    // --- bounded batches and resumption ------------------------------------
    const slotB = base + 1;
    const partial = await call("POST", `/api/spike/resolve?slot=${slotB}&batch=50&maxBatches=1`);
    check(
      "a small batch stops early and reports remaining work",
      partial.data.outcome === "partial" && partial.data.applied === 50 && partial.data.remaining === N - 50,
      `applied=${partial.data.applied} remaining=${partial.data.remaining}`,
    );

    let applied = partial.data.applied;
    let guard = 0;
    while (applied < N && guard < 20) {
      const next = await call("POST", `/api/spike/resolve?slot=${slotB}&batch=50&maxBatches=1`);
      applied = next.data.applied;
      guard += 1;
    }
    const reportB = await call("GET", `/api/spike/report?slot=${slotB}`);
    check(
      "resumed invocations finish the slot exactly once",
      applied === N && reportB.data.report.applied.n === N && reportB.data.report.audit.n === N,
      `applied=${applied} markers=${reportB.data.report.applied.n} audit_rows=${reportB.data.report.audit.n}`,
    );
    check(
      "value is conserved and matches the deterministic rule",
      Number(reportB.data.report.applied.delta_sum) === expectedSum(N),
      `delta_sum=${reportB.data.report.applied.delta_sum} expected=${expectedSum(N)}`,
    );

    // --- interruption -------------------------------------------------------
    const slotC = base + 2;
    const fault = await call("POST", `/api/spike/resolve?slot=${slotC}&batch=50&faultAfter=100`);
    check("an injected interruption fails the invocation", fault.status === 409, `HTTP ${fault.status}`);
    const afterFault = await call("GET", `/api/status`);
    const ledgerC = afterFault.data.recent_runs.find((r) => r.slot === slotC && r.outcome === "error");
    check("the failure is recorded, not hidden", Boolean(ledgerC), ledgerC ? ledgerC.outcome : "missing run row");

    const resumeC = await call("POST", `/api/spike/resolve?slot=${slotC}&batch=50`);
    const reportC = await call("GET", `/api/spike/report?slot=${slotC}`);
    check(
      "the interrupted slot resumes forward-only to exactly " + N + " applications",
      resumeC.data.outcome === "completed" &&
        reportC.data.report.applied.n === N &&
        reportC.data.report.audit.n === N,
      `applied=${reportC.data.report.applied.n} audit=${reportC.data.report.audit.n}`,
    );

    // --- simulated quota exhaustion ----------------------------------------
    const slotD = base + 3;
    const full = await call("POST", `/api/spike/resolve?slot=${slotD}&batch=50&storageFull=1`);
    check("a simulated storage limit fails safely", full.status === 409, `HTTP ${full.status}`);
    const reportD = await call("GET", `/api/spike/report?slot=${slotD}`);
    check(
      "a failed run does not mark the turn completed",
      !reportD.data.report.ledger || reportD.data.report.ledger.status !== "completed",
      `ledger=${reportD.data.report.ledger ? reportD.data.report.ledger.status : "none"}`,
    );
    const recoverD = await call("POST", `/api/spike/resolve?slot=${slotD}&batch=100`);
    check("the world recovers after the limit clears", recoverD.data.outcome === "completed", recoverD.data.outcome);

    // --- forward-only -------------------------------------------------------
    const old = await call("POST", `/api/spike/resolve?slot=${base}&batch=100`);
    check("an older slot is refused as forward-only", old.data.outcome === "noop", `reason=${old.data.reason}`);

    const finalStatus = await call("GET", "/api/status");
    check(
      "the world remembers the last completed slot",
      finalStatus.data.last_completed_slot === slotD,
      `last=${finalStatus.data.last_completed_slot} expected=${slotD}`,
    );

    // --- scheduled handler --------------------------------------------------
    await call("POST", `/api/spike/seed?n=50&reset=1`);
    const sched = await fetch(BASE + "/__scheduled?cron=" + encodeURIComponent("0 */2 * * *"));
    check("the scheduled handler is reachable through the runtime", sched.ok, `HTTP ${sched.status}`);
    await new Promise((r) => setTimeout(r, 1000));
    const schedStatus = await call("GET", "/api/status");
    const cronRun = schedStatus.data.recent_runs.find((r) => r.trigger === "cron");
    check(
      "a scheduled invocation resolves the current shared slot",
      Boolean(cronRun) &&
        cronRun.outcome === "completed" &&
        schedStatus.data.last_completed_slot === Math.floor(Date.now() / TURN_MS),
      cronRun ? `slot ${cronRun.slot} ${cronRun.outcome}` : "no cron run recorded",
    );

    const failed = results.filter((r) => !r.ok);
    exitCode = failed.length === 0 ? 0 : 1;
    console.log(`\n${results.length - failed.length}/${results.length} integration checks passed`);
  } catch (error) {
    console.error("HARNESS ERROR:", error);
    exitCode = 2;
  } finally {
    stopDev(dev);
  }
  process.exit(exitCode);
}

main();
