#!/usr/bin/env node
/**
 * Local capacity measurement for the free-tier feasibility spike.
 *
 * Starts local workerd + local D1 and records, per dataset size:
 *   - one invocation that resolves the whole slot (bounded batches internally)
 *   - one invocation that processes exactly one batch (the per-trigger shape)
 *
 * These are LOCAL wall-clock and D1-emulation numbers. The Worker CPU limit is
 * a deployed metric and is NOT measured here.
 */

import { spawn } from "node:child_process";
import { existsSync, writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "..");
const PORT = Number(process.env.SPIKE_PORT || 8788);
const TOKEN = process.env.SPIKE_TOKEN || "local-test-token";
const BASE = `http://127.0.0.1:${PORT}`;
const TURN_MS = 7200 * 1000;

async function call(method, route) {
  const res = await fetch(BASE + route, { method, headers: { "x-spike-token": TOKEN } });
  const text = await res.text();
  try {
    return { status: res.status, data: JSON.parse(text) };
  } catch {
    return { status: res.status, data: { raw: text } };
  }
}

async function waitForHealth(timeoutMs = 90000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    try {
      const res = await fetch(BASE + "/health");
      if (res.ok) return res.json();
    } catch {
      /* not up yet */
    }
    await new Promise((r) => setTimeout(r, 500));
  }
  throw new Error("worker did not become healthy");
}

function startDev() {
  const wrangler = path.join(root, "node_modules", "wrangler", "bin", "wrangler.js");
  if (!existsSync(wrangler)) throw new Error("wrangler is not installed");
  const child = spawn(
    process.execPath,
    [wrangler, "dev", "--port", String(PORT), "--var", `SPIKE_TOKEN:${TOKEN}`],
    { cwd: root, env: { ...process.env, WRANGLER_SEND_METRICS: "false" }, stdio: ["ignore", "pipe", "pipe"] },
  );
  child.stdout.on("data", () => {});
  child.stderr.on("data", () => {});
  return child;
}

function stopDev(child) {
  if (!child || child.killed) return;
  if (process.platform === "win32") spawn("taskkill", ["/pid", String(child.pid), "/T", "/F"], { stdio: "ignore" });
  else child.kill("SIGTERM");
}

async function main() {
  const sizes = [50, 250, 1000];
  const rows = [];
  const dev = startDev();
  try {
    await waitForHealth();
    await call("POST", "/api/spike/init");
    const base = Math.floor(Date.now() / TURN_MS) - 100;
    let slot = base;

    for (const n of sizes) {
      await call("POST", `/api/spike/seed?n=${n}&reset=1`);

      // Whole-slot invocation: batch size chosen to stay inside 50 queries.
      slot += 1;
      const whole = await call("POST", `/api/spike/resolve?slot=${slot}&batch=250`);
      if (whole.data.outcome !== "completed") throw new Error(`N=${n} whole-slot run did not complete: ${JSON.stringify(whole.data)}`);
      rows.push({
        scenario: "whole-slot",
        nations: n,
        outcome: whole.data.outcome,
        batches: whole.data.batches,
        duration_ms: whole.data.duration_ms,
        rows_read: whole.data.metrics.rows_read,
        rows_written: whole.data.metrics.rows_written,
        requests: whole.data.metrics.requests,
        statements: whole.data.metrics.statements,
        db_size_after: whole.data.metrics.db_size_after,
        rows_written_per_nation: Number((whole.data.metrics.rows_written / n).toFixed(3)),
        rows_read_per_nation: Number((whole.data.metrics.rows_read / n).toFixed(3)),
        ms_per_nation: Number((whole.data.duration_ms / n).toFixed(3)),
      });

      // One-batch invocation: the per-trigger shape under a bounded budget.
      slot += 1;
      const one = await call("POST", `/api/spike/resolve?slot=${slot}&batch=50&maxBatches=1`);
      if (!["partial", "completed"].includes(one.data.outcome)) {
        throw new Error(`N=${n} one-batch run failed: ${JSON.stringify(one.data)}`);
      }
      rows.push({
        scenario: "one-batch",
        nations: n,
        outcome: one.data.outcome,
        processed: one.data.applied,
        remaining: one.data.remaining ?? 0,
        duration_ms: one.data.duration_ms,
        rows_read: one.data.metrics.rows_read,
        rows_written: one.data.metrics.rows_written,
        requests: one.data.metrics.requests,
        statements: one.data.metrics.statements,
        db_size_after: one.data.metrics.db_size_after,
        buffer_batches_to_finish: Math.ceil(one.data.remaining / 50),
      });
    }

    console.log(JSON.stringify({ runtime: "local workerd + local D1", measured_at: new Date().toISOString(), rows }, null, 2));

    const outDir = path.join(root, "results");
    mkdirSync(outDir, { recursive: true });
    writeFileSync(path.join(outDir, "local-capacity.json"), JSON.stringify({ runtime: "local workerd + local D1", measured_at: new Date().toISOString(), rows }, null, 2));
  } finally {
    stopDev(dev);
  }
}

main().catch((error) => {
  console.error("MEASURE ERROR:", error);
  process.exit(1);
});
