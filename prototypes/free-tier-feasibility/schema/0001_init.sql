-- Project X free-tier feasibility spike schema.
-- Synthetic data only. This is NOT the production schema and must not be
-- extended into one without the architecture decision (D-005) being settled.

CREATE TABLE IF NOT EXISTS world (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS nations (
  id        INTEGER PRIMARY KEY,
  name      TEXT    NOT NULL,
  treasury  INTEGER NOT NULL DEFAULT 0,
  last_slot INTEGER NOT NULL DEFAULT 0
);

-- One row per turn slot: the exactly-once ledger (REQ-016).
CREATE TABLE IF NOT EXISTS turn_runs (
  slot         INTEGER PRIMARY KEY,
  status       TEXT    NOT NULL CHECK (status IN ('running', 'completed')),
  cursor       INTEGER NOT NULL DEFAULT 0,
  processed    INTEGER NOT NULL DEFAULT 0,
  started_at   TEXT    NOT NULL,
  completed_at TEXT
);

-- Per-nation idempotency marker; (slot, nation_id) is the duplicate guard.
CREATE TABLE IF NOT EXISTS turn_processing (
  slot       INTEGER NOT NULL,
  nation_id  INTEGER NOT NULL,
  applied_at TEXT    NOT NULL,
  delta      INTEGER NOT NULL,
  run_id     TEXT    NOT NULL,
  PRIMARY KEY (slot, nation_id)
);

-- Deliberately indexed: this is how the spike measures index write amplification.
CREATE TABLE IF NOT EXISTS audit (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  slot       INTEGER NOT NULL,
  nation_id  INTEGER NOT NULL,
  delta      INTEGER NOT NULL,
  cause      TEXT    NOT NULL,
  created_at TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_audit_slot_nation ON audit (slot, nation_id);

-- Measurements, one row per invocation. Indexed on purpose (one extra write).
CREATE TABLE IF NOT EXISTS spike_runs (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  slot              INTEGER NOT NULL,
  trigger           TEXT    NOT NULL,
  outcome           TEXT    NOT NULL,
  nations_processed INTEGER NOT NULL,
  remaining         INTEGER NOT NULL,
  duration_ms       REAL    NOT NULL,
  rows_read         INTEGER NOT NULL,
  rows_written      INTEGER NOT NULL,
  db_size_after     INTEGER,
  error             TEXT,
  created_at        TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_spike_runs_slot ON spike_runs (slot);
