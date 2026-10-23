/**
 * Turn-resolution engine for the feasibility spike.
 *
 * Properties under test:
 *  - one shared slot for the whole world (no per-nation schedules);
 *  - exactly-once per (slot, nation) even if the invocation is repeated;
 *  - resumable in bounded batches, forward-only;
 *  - no partial nation apply when an invocation dies mid-way.
 *
 * It is intentionally small and synthetic. It is not game logic.
 */

import { slotIso } from "./slots.js";

export const DEFAULT_BATCH_NATIONS = 100;
const MINT_BASE = 10;

/** Deterministic synthetic "production" so conservation can be recomputed. */
export function nationDelta(nationId) {
  return MINT_BASE + (nationId % 7);
}

class Metrics {
  constructor() {
    this.rowsRead = 0;
    this.rowsWritten = 0;
    this.dbSizeAfter = null;
    this.statements = 0;
    this.requests = 0;
  }

  absorb(meta) {
    meta = meta || {};
    this.rowsRead += meta.rows_read || 0;
    this.rowsWritten += meta.rows_written || 0;
    if (typeof meta.size_after === "number" && meta.size_after > 0) {
      this.dbSizeAfter = meta.size_after;
    }
  }

  addOne(result) {
    this.requests += 1;
    this.statements += 1;
    this.absorb(result && result.meta);
    return this;
  }

  /** A D1 batch is one request carrying several statements. */
  addBatch(results) {
    this.requests += 1;
    for (const item of results) {
      this.statements += 1;
      this.absorb(item && item.meta);
    }
    return this;
  }

  snapshot() {
    return {
      rows_read: this.rowsRead,
      rows_written: this.rowsWritten,
      db_size_after: this.dbSizeAfter,
      statements: this.statements,
      requests: this.requests,
    };
  }
}

function firstRow(result) {
  return (result && result.results && result.results[0]) || null;
}

async function readLastCompleted(db, metrics) {
  const res = await db.prepare("SELECT value FROM world WHERE key = 'last_completed_slot'").all();
  metrics.addOne(res);
  const row = firstRow(res);
  return row ? Number(row.value) : null;
}

async function readRun(db, slot, metrics) {
  const res = await db
    .prepare("SELECT status, cursor, processed FROM turn_runs WHERE slot = ?")
    .bind(slot)
    .all();
  metrics.addOne(res);
  return firstRow(res);
}

async function countNations(db, metrics) {
  const res = await db.prepare("SELECT COUNT(*) AS n FROM nations").all();
  metrics.addOne(res);
  return Number(firstRow(res).n);
}

async function countApplied(db, slot, metrics) {
  const res = await db
    .prepare("SELECT COUNT(*) AS n FROM turn_processing WHERE slot = ?")
    .bind(slot)
    .all();
  metrics.addOne(res);
  return Number(firstRow(res).n);
}

export async function recordRun(env, record) {
  await env.DB.prepare(
    `INSERT INTO spike_runs
       (slot, trigger, outcome, nations_processed, remaining, duration_ms,
        rows_read, rows_written, db_size_after, error, created_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
  )
    .bind(
      record.slot,
      record.trigger,
      record.outcome,
      record.processed,
      record.remaining,
      record.duration_ms,
      record.metrics.rows_read,
      record.metrics.rows_written,
      record.metrics.db_size_after,
      record.error || null,
      new Date().toISOString(),
    )
    .run();
}

/**
 * Resolve one slot.
 *
 * @param {object} env Worker env with the DB binding.
 * @param {object} options slot, trigger, batchSize, faultAfter, storageFull, now.
 */
export async function resolveTurn(env, options) {
  const {
    slot,
    trigger = "http",
    batchSize = DEFAULT_BATCH_NATIONS,
    maxBatches = null,
    faultAfter = null,
    storageFull = false,
    now = Date.now(),
  } = options;

  if (!Number.isInteger(slot) || slot < 0) {
    throw new TypeError("slot must be a non-negative integer");
  }
  if (!Number.isInteger(batchSize) || batchSize < 1) {
    throw new TypeError("batchSize must be a positive integer");
  }
  if (maxBatches !== null && (!Number.isInteger(maxBatches) || maxBatches < 1)) {
    throw new TypeError("maxBatches must be null or a positive integer");
  }

  const db = env.DB;
  const metrics = new Metrics();
  const startedAt = Date.now();
  const appliedAt = new Date(now).toISOString();

  const last = await readLastCompleted(db, metrics);
  if (last !== null && slot <= last) {
    return {
      outcome: "noop",
      slot,
      slot_iso: slotIso(slot),
      trigger,
      reason: slot === last ? "slot already completed" : "slot is older than the last completed slot",
      processed: 0,
      remaining: 0,
      duration_ms: Date.now() - startedAt,
      metrics: metrics.snapshot(),
    };
  }

  let run = await readRun(db, slot, metrics);
  if (run && run.status === "completed") {
    return {
      outcome: "noop",
      slot,
      slot_iso: slotIso(slot),
      trigger,
      reason: "turn ledger already marked completed",
      processed: 0,
      remaining: 0,
      duration_ms: Date.now() - startedAt,
      metrics: metrics.snapshot(),
    };
  }

  if (!run) {
    const claimed = await db
      .prepare("INSERT OR IGNORE INTO turn_runs (slot, status, cursor, processed, started_at) VALUES (?, 'running', 0, 0, ?)")
      .bind(slot, appliedAt)
      .run();
    metrics.addOne(claimed);
    run = claimed.meta && claimed.meta.changes > 0 ? { status: "running", cursor: 0, processed: 0 } : await readRun(db, slot, metrics);
    if (!run) throw new Error("turn ledger row could not be claimed");
  }

  let cursor = Number(run.cursor);
  let processed = Number(run.processed);
  const total = await countNations(db, metrics);
  let batchIndex = 0;

  for (;;) {
    if (storageFull && processed > 0) {
      throw Object.assign(new Error("simulated D1 storage limit reached"), { code: "SPIKE_STORAGE_FULL" });
    }
    if (faultAfter !== null && processed >= faultAfter) {
      throw Object.assign(new Error("simulated interruption after " + processed + " nations"), {
        code: "SPIKE_INTERRUPTED",
      });
    }

    const out = await db
      .prepare("SELECT id FROM nations WHERE id > ? ORDER BY id LIMIT ?")
      .bind(cursor, batchSize)
      .all();
    metrics.addOne(out);
    const nations = out.results || [];
    if (nations.length === 0) break;

    const statements = [];
    for (const nation of nations) {
      const delta = nationDelta(nation.id);
      statements.push(
        db
          .prepare(
            `INSERT OR IGNORE INTO turn_processing (slot, nation_id, applied_at, delta, run_id)
             VALUES (?, ?, ?, ?, ?)`,
          )
          .bind(slot, nation.id, appliedAt, delta, String(now)),
      );
      statements.push(
        db
          .prepare("UPDATE nations SET treasury = treasury + ?, last_slot = ? WHERE id = ? AND last_slot < ?")
          .bind(delta, slot, nation.id, slot),
      );
      statements.push(
        db
          .prepare(
            `INSERT INTO audit (slot, nation_id, delta, cause, created_at)
             SELECT ?, ?, ?, 'turn-production', ?
             WHERE EXISTS (
               SELECT 1 FROM turn_processing
               WHERE slot = ? AND nation_id = ? AND run_id = ?
             )`,
          )
          .bind(slot, nation.id, delta, appliedAt, slot, nation.id, String(now)),
      );
    }

    const results = await db.batch(statements);
    metrics.addBatch(results);

    let applied = 0;
    for (let i = 0; i < results.length; i += 3) {
      const changes = results[i] && results[i].meta ? results[i].meta.changes : 0;
      if (changes > 0) applied += 1;
    }

    cursor = nations[nations.length - 1].id;
    processed += applied;
    batchIndex += 1;

    const progress = await db
      .prepare("UPDATE turn_runs SET cursor = ?, processed = ? WHERE slot = ?")
      .bind(cursor, processed, slot)
      .run();
    metrics.addOne(progress);

    if (maxBatches !== null && batchIndex >= maxBatches) break;
    if (nations.length < batchSize) break;
  }

  const appliedCount = await countApplied(db, slot, metrics);
  if (appliedCount < total) {
    return {
      outcome: "partial",
      slot,
      slot_iso: slotIso(slot),
      trigger,
      processed,
      applied: appliedCount,
      total,
      remaining: total - appliedCount,
      batches: batchIndex,
      duration_ms: Date.now() - startedAt,
      metrics: metrics.snapshot(),
    };
  }

  metrics.addOne(
    await db
      .prepare("UPDATE turn_runs SET status = 'completed', completed_at = ? WHERE slot = ?")
      .bind(appliedAt, slot)
      .run(),
  );
  metrics.addOne(
    await db
      .prepare(
        `INSERT INTO world (key, value) VALUES ('last_completed_slot', ?)
         ON CONFLICT(key) DO UPDATE SET value = excluded.value`,
      )
      .bind(String(slot))
      .run(),
  );

  return {
    outcome: "completed",
    slot,
    slot_iso: slotIso(slot),
    trigger,
    processed,
    applied: appliedCount,
    total,
    remaining: 0,
    batches: batchIndex,
    duration_ms: Date.now() - startedAt,
    metrics: metrics.snapshot(),
  };
}

/** Aggregate verification used by the spike's own report endpoint. */
export async function reportSlot(env, slot) {
  const db = env.DB;
  const nations = await db
    .prepare("SELECT COUNT(*) AS n, COALESCE(SUM(treasury),0) AS treasury_sum, COALESCE(SUM(last_slot),0) AS last_slot_sum FROM nations")
    .all();
  const applied = await db
    .prepare("SELECT COUNT(*) AS n, COALESCE(SUM(delta),0) AS delta_sum FROM turn_processing WHERE slot = ?")
    .bind(slot)
    .all();
  const audit = await db
    .prepare("SELECT COUNT(*) AS n, COALESCE(SUM(delta),0) AS delta_sum FROM audit WHERE slot = ?")
    .bind(slot)
    .all();
  const run = await db.prepare("SELECT * FROM turn_runs WHERE slot = ?").bind(slot).all();
  const runs = await db.prepare("SELECT * FROM spike_runs WHERE slot = ? ORDER BY id").bind(slot).all();
  const world = await db.prepare("SELECT value FROM world WHERE key = 'last_completed_slot'").all();
  const auditTotal = await db.prepare("SELECT COUNT(*) AS n FROM audit").all();

  return {
    slot,
    slot_iso: slotIso(slot),
    world_last_completed_slot: world.results[0] ? Number(world.results[0].value) : null,
    nations: nations.results[0],
    applied: applied.results[0],
    audit: audit.results[0],
    ledger: run.results[0] || null,
    runs: runs.results,
    audit_rows_total: auditTotal.results[0].n,
  };
}
