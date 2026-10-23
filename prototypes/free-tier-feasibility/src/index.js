/**
 * Project X free-tier feasibility spike — Worker entrypoint.
 *
 * Public routes are read-only. Mutating routes require the spike token and are
 * disabled unless ALLOW_SPIKE=1. The data is synthetic; no player data exists.
 */

import {
  PRODUCT_CRON,
  authorizeSpike,
  computeSlot,
  isSlotClosed,
  slotIso,
} from "./slots.js";
import { DEFAULT_BATCH_NATIONS, recordRun, reportSlot, resolveTurn } from "./engine.js";

const SERVICE = "px-feasibility-spike";

function json(body, status = 200) {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

function html() {
  return new Response(
    `<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Project X — free-tier feasibility spike</title>
<style>
 body{font:16px/1.5 system-ui,sans-serif;max-width:44rem;margin:3rem auto;padding:0 1rem;color:#1b1b1b}
 code{background:#f2f2f2;padding:.1rem .3rem;border-radius:3px}
 .ok{color:#0a6b2f;font-weight:600}
</style></head>
<body>
<h1>Project X — free-tier feasibility spike</h1>
<p class="ok">The Worker is running.</p>
<p>This page exists only to prove that a browser-accessible application can be
served from the free configuration. It is not the game.</p>
<ul>
  <li><a href="/health">/health</a> — runtime and current turn slot</li>
  <li><a href="/api/status">/api/status</a> — last completed slot and recent runs</li>
</ul>
<p>Mutating test routes require a token and are disabled unless the deployment
opts in. Synthetic data only.</p>
</body></html>`,
    { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } },
  );
}

async function seedNations(env, n) {
  const statements = [];
  for (let start = 1; start <= n; start += 20) {
    const values = [];
    const params = [];
    for (let id = start; id < Math.min(start + 20, n + 1); id += 1) {
      values.push("(?, ?, 0, 0)");
      params.push(id, `Synthetic Nation ${id}`);
    }
    statements.push(
      env.DB.prepare(`INSERT OR REPLACE INTO nations (id, name, treasury, last_slot) VALUES ${values.join(", ")}`).bind(...params),
    );
  }
  await env.DB.batch(statements);
  return n;
}

async function handleSpike(request, env, url) {
  const action = url.pathname.replace("/api/spike/", "");

  if (action === "init") {
    const schema = [
      `CREATE TABLE IF NOT EXISTS world (key TEXT PRIMARY KEY, value TEXT NOT NULL)`,
      `CREATE TABLE IF NOT EXISTS nations (id INTEGER PRIMARY KEY, name TEXT NOT NULL, treasury INTEGER NOT NULL DEFAULT 0, last_slot INTEGER NOT NULL DEFAULT 0)`,
      `CREATE TABLE IF NOT EXISTS turn_runs (slot INTEGER PRIMARY KEY, status TEXT NOT NULL, cursor INTEGER NOT NULL DEFAULT 0, processed INTEGER NOT NULL DEFAULT 0, started_at TEXT NOT NULL, completed_at TEXT)`,
      `CREATE TABLE IF NOT EXISTS turn_processing (slot INTEGER NOT NULL, nation_id INTEGER NOT NULL, applied_at TEXT NOT NULL, delta INTEGER NOT NULL, run_id TEXT NOT NULL, PRIMARY KEY (slot, nation_id))`,
      `CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY AUTOINCREMENT, slot INTEGER NOT NULL, nation_id INTEGER NOT NULL, delta INTEGER NOT NULL, cause TEXT NOT NULL, created_at TEXT NOT NULL)`,
      `CREATE INDEX IF NOT EXISTS idx_audit_slot_nation ON audit (slot, nation_id)`,
      `CREATE TABLE IF NOT EXISTS spike_runs (id INTEGER PRIMARY KEY AUTOINCREMENT, slot INTEGER NOT NULL, trigger TEXT NOT NULL, outcome TEXT NOT NULL, nations_processed INTEGER NOT NULL, remaining INTEGER NOT NULL, duration_ms REAL NOT NULL, rows_read INTEGER NOT NULL, rows_written INTEGER NOT NULL, db_size_after INTEGER, error TEXT, created_at TEXT NOT NULL)`,
      `CREATE INDEX IF NOT EXISTS idx_spike_runs_slot ON spike_runs (slot)`,
    ];
    await env.DB.batch(schema.map((sql) => env.DB.prepare(sql)));
    return json({ ok: true, action: "init", statements: schema.length });
  }

  if (action === "seed") {
    const n = Number(url.searchParams.get("n") || "50");
    if (!Number.isInteger(n) || n < 1 || n > 5000) return json({ error: "n must be 1..5000" }, 400);
    const reset = url.searchParams.get("reset") === "1";
    if (reset) {
      await env.DB.batch([
        env.DB.prepare("DELETE FROM audit"),
        env.DB.prepare("DELETE FROM turn_processing"),
        env.DB.prepare("DELETE FROM turn_runs"),
        env.DB.prepare("DELETE FROM spike_runs"),
        env.DB.prepare("DELETE FROM world"),
        env.DB.prepare("DELETE FROM nations"),
      ]);
    }
    const seeded = await seedNations(env, n);
    return json({ ok: true, action: "seed", nations: seeded, reset });
  }

  if (action === "resolve") {
    const slotParam = url.searchParams.get("slot");
    const now = Date.now();
    const slot = slotParam === null ? computeSlot(now) : Number(slotParam);
    if (!Number.isInteger(slot) || slot < 0) return json({ error: "slot must be a non-negative integer" }, 400);
    if (!isSlotClosed(slot, now)) return json({ error: "slot boundary has not passed yet", slot, now }, 400);

    const batch = Number(url.searchParams.get("batch") || String(DEFAULT_BATCH_NATIONS));
    const maxBatchesParam = url.searchParams.get("maxBatches");
    const maxBatches = maxBatchesParam === null ? null : Number(maxBatchesParam);
    const faultParam = url.searchParams.get("faultAfter");
    const faultAfter = faultParam === null ? null : Number(faultParam);
    const storageFull = url.searchParams.get("storageFull") === "1";
    if (!Number.isInteger(batch) || batch < 1 || batch > 1000) return json({ error: "batch must be 1..1000" }, 400);
    if (maxBatches !== null && (!Number.isInteger(maxBatches) || maxBatches < 1)) {
      return json({ error: "maxBatches must be a positive integer" }, 400);
    }
    if (faultAfter !== null && (!Number.isInteger(faultAfter) || faultAfter < 0)) {
      return json({ error: "faultAfter must be a non-negative integer" }, 400);
    }

    try {
      const result = await resolveTurn(env, { slot, trigger: "http", batchSize: batch, maxBatches, faultAfter, storageFull, now });
      await recordRun(env, result);
      return json({ ok: true, ...result });
    } catch (error) {
      await recordRun(env, {
        slot,
        trigger: "http",
        outcome: "error",
        processed: 0,
        remaining: -1,
        duration_ms: 0,
        metrics: { rows_read: 0, rows_written: 0, db_size_after: null },
        error: String(error && error.message ? error.message : error),
      });
      return json(
        {
          ok: false,
          slot,
          error: String(error && error.message ? error.message : error),
          code: (error && error.code) || null,
        },
        409,
      );
    }
  }

  if (action === "report") {
    const slot = Number(url.searchParams.get("slot") || String(computeSlot(Date.now())));
    if (!Number.isInteger(slot) || slot < 0) return json({ error: "slot must be a non-negative integer" }, 400);
    return json({ ok: true, report: await reportSlot(env, slot) });
  }

  return json({ error: "unknown spike action" }, 404);
}

async function handleStatus(env) {
  const db = env.DB;
  const world = await db.prepare("SELECT value FROM world WHERE key = 'last_completed_slot'").all();
  const counts = await db.prepare("SELECT (SELECT COUNT(*) FROM nations) AS nations, (SELECT COUNT(*) FROM audit) AS audit, (SELECT COUNT(*) FROM turn_runs) AS turns").all();
  const runs = await db.prepare("SELECT slot, trigger, outcome, nations_processed, remaining, duration_ms, rows_written, created_at FROM spike_runs ORDER BY id DESC LIMIT 10").all();
  return json({
    ok: true,
    service: SERVICE,
    now: new Date().toISOString(),
    current_slot: computeSlot(Date.now()),
    product_cron: PRODUCT_CRON,
    last_completed_slot: world.results[0] ? Number(world.results[0].value) : null,
    counts: counts.results[0],
    recent_runs: runs.results,
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "GET" && url.pathname === "/") return html();
    if (request.method === "GET" && url.pathname === "/health") {
      return json({
        ok: true,
        service: SERVICE,
        now: new Date().toISOString(),
        current_slot: computeSlot(Date.now()),
        slot_iso: slotIso(computeSlot(Date.now())),
        runtime: "workerd",
        product_cron: PRODUCT_CRON,
      });
    }
    if (request.method === "GET" && url.pathname === "/api/status") {
      try {
        return await handleStatus(env);
      } catch (error) {
        return json({ ok: false, error: String(error.message || error) }, 500);
      }
    }

    if (url.pathname.startsWith("/api/spike/")) {
      if (!authorizeSpike(request, env)) {
        return json({ error: "spike routes are disabled or the token does not match" }, 403);
      }
      try {
        return await handleSpike(request, env, url);
      } catch (error) {
        return json({ ok: false, error: String(error.message || error) }, 500);
      }
    }

    return json({ error: "not found" }, 404);
  },

  async scheduled(controller, env) {
    const slot = computeSlot(controller.scheduledTime);
    try {
      const result = await resolveTurn(env, {
        slot,
        trigger: "cron",
        now: controller.scheduledTime,
      });
      await recordRun(env, result);
    } catch (error) {
      await recordRun(env, {
        slot,
        trigger: "cron",
        outcome: "error",
        processed: 0,
        remaining: -1,
        duration_ms: 0,
        metrics: { rows_read: 0, rows_written: 0, db_size_after: null },
        error: String(error && error.message ? error.message : error),
      });
    }
  },
};
