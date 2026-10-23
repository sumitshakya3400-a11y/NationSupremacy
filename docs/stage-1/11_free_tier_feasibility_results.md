# Report 11 — Free-tier technical feasibility results

**Version:** 1.0
**Date:** 2026-10-23
**Status:** Measurement record. Supersedes the planned statuses in [Report 10](10_stage_1_gate_evidence_and_feasibility_plan.md) where they differ.
**Scope:** GATE-13, GATE-16, GATE-18. No architecture decision is approved here, and Stage 1 is not declared complete.

---

## 0. Summary — read this first

A bounded prototype was written, tested locally in the real Workers runtime (`workerd`), and then **deployed to the owner's connected free Cloudflare account** with a real D1 database, a real public HTTPS endpoint and real cron schedules. Synthetic data only.

What the evidence shows:

| Question | Result |
|---|---|
| Does a free Worker serve the page and API? | **Yes** — deployed, HTTPS, `200`, measured |
| Does D1 persist synthetic state? | **Yes** — 1,000 nations, schema, reads, writes, reports |
| Is a turn exactly-once under duplicate triggers? | **Yes** — ledger + per-nation marker; duplicate = 1 read, 0 writes |
| Does bounded batching resume forward-only? | **Yes** — partial → resume → exactly 250/250 and 1,000/1,000 applied |
| Does an interrupted invocation corrupt state? | **No** — failed runs left `running`, resumed to exactly N applications |
| Does a simulated storage limit fail safely? | **Yes** — 409, no completed ledger, clean recovery |
| Do 12 turns/day fit the free scheduler CPU budget? | **Only below a measured size.** A 250-nation batch used ~1.4–5.1 ms CPU; resolving 1,000 nations in one invocation used **36.6 ms and 61.6 ms** — over the 10 ms free limit |
| Did a live Cron Trigger fire? | **Yes — observed.** It fired at 08:46:41Z, resolved the 08:00 UTC slot for 1,000 nations in 14.9 s, and fired again at 08:51:00Z for the same slot as a 0-write no-op. Propagation took ~24 minutes |
| Are the 100k/day write limits a real constraint? | **Yes, and now quantified** — 6.01 rows written per nation-turn, so ~1,388 nations at 12 turns/day |
| Is ₹0 still credible? | **Conditional** — at small sizes, yes; at ~1,000 nations in one invocation, the CPU limit is exceeded |
| Did this pass verify the account's plan/billing? | **No** — the connector lacks Billing Read scope (403) |

**GATE-13, GATE-16 and GATE-18 all remain CONDITIONAL.** The evidence is materially stronger than before, and one genuinely new failure mode was found, but none of the three gates' recorded acceptance criteria is fully met. Details in §9.

---

## 1. Environment and what was actually executed

| Item | Value |
|---|---|
| Project root | `C:\Users\suren\Downloads\Project X` |
| Starting state | Byte-identical to `Project X step 9 correction.zip` (38/38 SHA-256 matches) |
| Version control | Local git repository created in this pass; baseline commit `a1174d8` on `main`; work on branch `prototype/free-tier-feasibility` |
| Local runtime | `workerd` via `wrangler 4.152.0`, local D1 (Miniflare) |
| Deployed runtime | Cloudflare Workers, compatibility date `2026-10-23`, script `px-feasibility-spike` |
| Deployed database | D1 `px-feasibility-spike`, id `850d9eb4-7a44-4365-81f5-cca954b3738b`, region APAC |
| Public endpoint | `https://px-feasibility-spike.nationsphere.workers.dev` |
| Schedules configured | `0 */2 * * *` (product) and `*/5 * * * *` (test-only, to observe cron without a 2-hour wait) |
| Data | Synthetic nations `Synthetic Nation 1…N`; no player, account or personal data |

**A note on the Supabase integration.** The connected account contains one Supabase project, `NATIONSPHERE`, in region `ap-southeast-2`, status **`INACTIVE`** (paused). It was read for status only. It was not resumed, queried, migrated or otherwise modified, and no new Supabase project was created. §4 explains why.

### 1.1 What "deployed" does and does not mean here

- The Worker is **really deployed** and publicly reachable over HTTPS. `/health` and `/api/status` are read-only; mutating routes require a token that is stored as a Worker secret, not in the repository.
- The D1 database is **really Cloudflare D1**, not a SQLite stand-in.
- The **Cron Trigger is configured and was observed firing**: once to complete a 1,000-nation turn (08:46:41Z) and once to no-op as a duplicate (08:51:00Z). What is still not observed is a **full 24-hour, 12-boundary run**.
- The measurements are **not** a load test against a production world. They are single synthetic turns at 50, 250 and 1,000 nations, run once or a few times each.

---

## 2. Official limits and prices verified on 2026-10-23

All figures below were read from the official documentation on the date shown; no figure is reused from an earlier report without re-checking.

| Source | Verified facts relevant here |
|---|---|
| [Workers limits](https://developers.cloudflare.com/workers/platform/limits/) | Free: 100,000 requests/day; **10 ms CPU per HTTP request and per Cron Trigger**; 128 MB memory; 50 subrequests/invocation; 5 cron triggers per account; 64 MiB worker; 1 s startup; Cron duration limit 15 min; error 1102 on CPU exceed; error 1027 on daily request limit; "each isolate has some built-in flexibility" for infrequent overages |
| [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) | Free plan is the default; static-asset requests are free and unlimited; paid plan is a **$5/month minimum** |
| [D1 limits](https://developers.cloudflare.com/d1/platform/limits/) | Free: **10 databases**, **500 MB per database**, 5 GB per account, **7-day Time Travel**, **50 queries per Worker invocation**, 100 bound params per query, 30 s max query duration, single-threaded per database |
| [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/) | Free: **5,000,000 rows read/day**, **100,000 rows written/day**, 5 GB storage; **no egress charge**; on limit exceed queries fail (no charge); "indexes will add an additional written row" |
| [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/) | UTC only; five-field expressions; changes propagate in "several minutes (up to 15 minutes)" |
| [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) | Free plan requires a **public** repository; 1 GB site; 100 GB/month soft bandwidth; **not allowed as a free host for a commercial SaaS** |
| [Supabase pricing](https://supabase.com/pricing) | Free: $0, unlimited API requests, **500 MB database**, 5 GB egress, 50k MAU, 2 active projects, **no automatic backups, no PITR**, **paused after 1 week of inactivity** |
| [Supabase billing docs](https://supabase.com/docs/guides/platform/billing-on-supabase) | Free plan quotas and project caps confirmed; paid plans are not paused |
| [Workers Logs pricing](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) | Included in Free: 200,000 events/day, 3-day retention; moves to 0.5 GB/day free allowance on 2026-12-01 |

### 2.1 Conflicts and changes worth recording

1. **D1's free database size is 500 MB, but account storage is 5 GB.** The 500 MB figure is per database; the account can hold 10 databases. P9's storage arithmetic assumed a 500 MB *database*, which is the binding limit for a single shared world. Unchanged conclusion, clarified basis.
2. **`50 queries per Worker invocation` is a harder constraint than it first appears.** It is listed as a D1 limit, and it is not the same as the 50-subrequest limit. The prototype deliberately stays at 8–20 queries per invocation; a naive per-nation statement loop would exceed it at ~50 nations.
3. **The 10 ms CPU limit is not a precise kill switch.** Two invocations in this spike used 36.6 ms and 61.6 ms of CPU and still returned `200`; Cloudflare documents "built-in flexibility" for infrequent overages. Treat 10 ms as a budget, not a guarantee — and not as a licence to exceed it.
4. **GitHub Pages cannot host this project's frontend as-is** on a free plan while the repository is private, and its terms exclude using Pages as the free host for a commercial service. That does not block ₹0 (Cloudflare static assets are free and unlimited), but REQ-032's "Pages" wording should not be read as "GitHub Pages is the plan".
5. **Supabase's free plan has no backups at all.** The pricing page lists "Automatic backups: Not included"; SEC-030 requires a restorable backup and SEC-032 a disclosed RPO. This is a functional gap, not a pricing preference.

---

## 3. What was built

Location: `prototypes/free-tier-feasibility/` (3 source modules, 1 schema, 2 test scripts, 1 README). No gameplay, no accounts, no production schema.

| File | Purpose |
|---|---|
| `src/slots.js` | Pure UTC slot arithmetic (2h boundaries), product-cron validation, constant-time spike token check |
| `src/engine.js` | `resolveTurn()`: slot ledger, per-nation idempotency marker, bounded batch loop, per-batch atomic D1 writes, resumption, metrics |
| `src/index.js` | Worker entrypoint: HTML page, `/health`, read-only `/api/status`, token-guarded `/api/spike/*`, `scheduled()` handler |
| `schema/0001_init.sql` | Six tables + two indexes; `CREATE … IF NOT EXISTS` so re-applying is safe |
| `test/slots.test.js` | 11 unit tests (no dependencies) |
| `scripts/integration.mjs` | 23 integration checks against local workerd |
| `scripts/measure.mjs` | Capacity table at 50 / 250 / 1,000 nations |

### 3.1 The integrity design, in one paragraph

A turn is claimed in `turn_runs` by primary key, so two triggers cannot both "own" the same slot. Each nation is processed by a single D1 `batch()` of three statements: `INSERT OR IGNORE` into `turn_processing (slot, nation_id)`, a guarded `UPDATE nations … WHERE last_slot < slot`, and an `INSERT … SELECT … WHERE EXISTS` audit row keyed to this invocation's `run_id`. D1 batches are transactions, so either the marker, the value change and the audit row all exist, or none of them do. Re-running the same slot finds the marker, changes zero rows, writes no audit row, and returns `noop`. Resumption reads `turn_runs.cursor`, so it only moves forward.

### 3.2 What is deliberately absent

No authentication, no session, no rate limiting, no per-user authorization, no retention job, no export, no backup drill, no 18-system schema, no real game values. Each is a separate Stage 2+ concern and none is claimed as tested.

---

## 4. Candidate architectures

| Criterion | A: Workers + D1 | B: Workers + Supabase | Outcome |
|---|---|---|---|
| Mandatory monthly cost | ₹0 | ₹0 | Tie |
| Database capacity | 500 MB **per database**, 5 GB/account, 10 DBs | 500 MB/project, 2 active projects | D1 |
| Read/write metering | 5M reads + 100k writes/day, measured | Unlimited API requests, compute-bound | Supabase on paper; D1 measured |
| Free backups | **7-day Time Travel** | **None** on Free | D1, decisively (SEC-030) |
| Idle behaviour | Always available | **Paused after 1 week of inactivity** (the existing `NATIONSPHERE` project is currently INACTIVE) | D1, decisively for a 12-turn/day world |
| Connection model from a Worker | Native binding, no pooler | Pooler/Hyperdrive; extra hop and connection budget | D1 |
| Scheduling | Native UTC cron (5 free); one boundary observed firing live | `pg_cron` inside Postgres; not exercised | D1 on evidence, not only on principle (see §7) |
| Recovery/restore | Time Travel + `d1 export` | None on Free | D1 |
| Relational maturity, auth, storage, realtime | Weaker (no native auth; SQLite) | Much stronger | Supabase |
| Lock-in | SQLite dialect; export available | Postgres; portable | Supabase |

**Decision (not an approval): keep Cloudflare Workers + D1 as the tested candidate and treat Supabase as the exit/fallback target.** The two decisive facts are the missing free backups and the idle pause on Supabase, both of which collide with SEC-030 and with a world that only advances when something runs. Supabase's advantages are real but are not needed by the first playable, and its free tier would be a worse fit for the recovery requirement.

Creating a Supabase test project was rejected on purpose: the free plan allows two active projects, project creation is slow, the free plan has no backups to test, and none of the decisive facts above would change. That is a **documented non-test**, not an oversight.

**Other configurations considered and rejected:** GitHub Pages + Supabase (adds a service and still has no backups); a VPS or container host (not ₹0); Durable Objects as the primary store (free tier exists but is not needed and adds a second state model); Workers + KV (no relational integrity or transactions, unusable for settlement).

---

## 5. Tests actually executed

### 5.1 Local unit tests

```
cd prototypes/free-tier-feasibility
node --test test/slots.test.js
```

**Result: 11/11 passed, 0 failed**, exit 0. Covers exact boundary alignment, one-millisecond-before-boundary behaviour, 12 distinct slots in 24h, 2h spacing, ISO formatting, rejection of invalid input, closed-slot guard, cron-string validation, and all token/opt-in combinations (including "no token configured ⇒ never authorise").

### 5.2 Local integration tests (real workerd + local D1)

```
node scripts/integration.mjs
```

**Result: 23/23 passed, 0 failed**, exit 0. It starts `wrangler dev --test-scheduled`, seeds 250 synthetic nations and asserts:

| # | Check | Observed |
|---|---|---|
| 1–2 | Boots; advertises the 12/day cadence | `200`, `0 */2 * * *` |
| 3 | Serves the HTML page | `200`, text present |
| 4 | Rejects a spike call with no token | `403` |
| 5–6 | Schema init is repeatable | `200` twice |
| 7 | Seeds synthetic data | `250` nations |
| 8–9 | One invocation resolves the world; metrics recorded | completed, 250 applied, 3 batches, 1,507 rows written, 1,506 rows read, 16 requests |
| 10 | Repeated trigger for the same slot | `noop`, "slot already completed" |
| 11 | One batch stops early | 50 applied, 200 remaining |
| 12–13 | Resumed invocations finish exactly once; value conserved | 250 markers, 250 audit rows, delta sum 3,250 = expected |
| 14–16 | Injected interruption fails safely and is recorded; resume completes exactly once | `409`, `error` run row, then 250/250 |
| 17–19 | Simulated storage limit fails safely; turn not marked complete; recovery completes | `409`, ledger `running`, then completed |
| 20 | An older slot is refused | `noop`, "older than the last completed slot" |
| 21–22 | Last completed slot persists; scheduled handler runs | slot remembered; `/__scheduled` resolved the current slot |
| 23 | Scheduled run recorded as `cron` | slot 248992 completed |

### 5.3 Deployed tests

Executed against `https://px-feasibility-spike.nationsphere.workers.dev` with a real D1 binding. Results in §6.

### 5.4 Project documentation validators

```
cd docs
python qa_backups/validate_final.py
python qa_backups/09_validate.py
```

**Before this pass:** `ALL CHECKS PASSED` and `68/68`.
**After this pass:** both pass again (`ALL CHECKS PASSED`; `68/68`), but only after **scoping one assertion in each script** — the "no production code" check now exempts the authorised `prototypes/` directory (plus `node_modules`/`dist`). The check is not weaker where it matters: code in `docs/`, at the project root, or in any future game directory still fails. This change is disclosed here because a validator that is edited to pass must be visible, not silent. No other assertion was touched, and none was deleted.

---

## 6. Deployed results

All runs below are real requests to the deployed Worker against real D1. `duration_ms` is measured inside the Worker around `resolveTurn`; it therefore includes D1 round trips and is **not** CPU time. `rows_read` / `rows_written` are the sums of D1's own `meta` values.

### 6.1 Persistence and integrity

| ID | Scenario | Outcome | Applied | Duration | Rows read | Rows written | Requests | DB bytes after |
|---|---|---|---|---|---|---|---|---|
| D1 | 250 nations, whole slot, batch 250 | completed | 250 | 2,635 ms | 1,505 | 1,505 | 11 | 102,400 |
| D2 | Same slot again (duplicate trigger) | **noop** | 0 | 51 ms | 1 | **0** | 1 | 102,400 |
| D3 | 1,000 nations, whole slot, batch 250 | completed | 1,000 | 5,632 ms | 6,008 | 6,008 | 20 | 249,856 |
| D4 | 1,000 nations, one batch of 50 | partial | 50 | 1,481 ms | 1,253 | 302 | 8 | 94,208 |
| D5 | 1,000 nations, one batch of 100 | partial | 100 | 1,672 ms | 1,503 | 602 | 8 | 114,688 |
| D6 | 1,000 nations, one batch of 250 | partial | 250 | 2,354 ms | 2,253 | 1,502 | 8 | 159,744 |
| D7 | 1,000 nations again, whole slot | completed | 1,000 | 6,358 ms | 6,008 | 6,008 | 20 | 249,856 |
| D8 | **Live Cron Trigger**, 1,000 nations, no batch cap | completed | 1,000 | **14,883 ms** | n/r | 6,013 | n/r | 249,856 |
| D9 | **Live Cron Trigger**, same slot 5 min later | **noop** | 0 | 201 ms | n/r | **0** | n/r | 249,856 |

The cron rows were not instrumented with request counts (`n/r`): the Worker records duration and rows, not D1 request counts, for scheduled runs. D8's 6,013 writes vs D7's 6,008 is fixed overhead from the ledger/measurement rows on a fresh slot.

Reading the table:

- **Exactly-once holds in production D1, not just locally.** A duplicate invocation performed one read, wrote nothing, and returned in 51 ms (250-nation world) / 173 ms (1,000-nation world).
- **A partial slot stays partial.** With `maxBatches=1`, the ledger remains `running` and reports `remaining`; nothing marks the turn complete early.
- **Write amplification is 6.01 rows per nation-turn** (1,505/250, 6,008/1,000). That is the number DEF-006 needed, and it is higher than a three-statement design suggests because the primary keys and the audit index each add a written row — exactly the mechanism the D1 pricing page documents.
- **Reads cost about the same as writes here** (~6 rows read per nation-turn), because the batch's guarded `UPDATE` and `EXISTS` sub-queries touch the marker row.
- **A 1,000-nation turn took 5.6–6.4 s of wall clock** in one invocation. Wall clock is not the binding limit (cron allows 15 minutes; HTTP has no duration limit), but it is long enough that a client-triggered design would need care.

### 6.2 Failure and recovery

| Scenario | Result |
|---|---|
| Injected interruption after 100 nations (local workerd) | `409`; `spike_runs` records `error`; ledger `running`; resume completes to exactly 250 applications and 250 audit rows |
| Simulated storage limit (`storageFull=1`) | `409` before any partial nation; ledger stays `running`; a normal retry completes |
| Duplicate trigger | `noop`, no writes |
| Older slot after a newer completion | `noop`, "older than the last completed slot" |
| Repeated schema initialisation | `200`, idempotent DDL |

**What was not tested:** a real D1 quota exhaustion (the daily cap was not hit and must not be hit deliberately), a real Cloudflare incident, a mid-batch worker kill (the fault is injected between batches), and a real network partition. Those remain PV-07/PV-03 open items.

### 6.3 CPU time, sampled from the provider

Cloudflare exposes per-invocation CPU time through `workersInvocationsAdaptive`. The figures below are **sampled analytics**, not counters recorded by the Worker. They are noisy: identical work produced different numbers across buckets.

| Scenario | Observed CPU | Free limit | Reading |
|---|---|---|---|
| One batch of 100, 20 consecutive invocations | **1.27 – 5.11 ms** (median ≈ 3.5 ms) | 10 ms | Fits |
| One batch of 250, 10 consecutive invocations | **1.40 – 4.68 ms** (median ≈ 3.4 ms) | 10 ms | Fits |
| 1,000 nations in one invocation (attempt 1) | **36.57 ms** | 10 ms | **Over** |
| 1,000 nations in one invocation (attempt 2) | **61.63 ms** | 10 ms | **Over** |
| Single batch samples (early, cold) | 6.71 ms / 11.16 ms / 20.10 ms | 10 ms | Inconsistent; treat as noise around the batch size |

**Interpretation.** The per-batch numbers are stable enough to act on: a 100–250-nation batch stays inside the 10 ms budget. The whole-slot numbers at 1,000 nations are 4–6× over it, consistently across two attempts. Both exceeded runs still returned `200`, which matches Cloudflare's documented "built-in flexibility for infrequent overages" — but a 12-turn/day game would repeat that overage 12 times a day, and the documentation says consistent overruns are terminated.

**Consequence:** the scheduled handler must cap the work it does per invocation. The prototype's `scheduled()` calls `resolveTurn` without a `maxBatches` cap, so at 1,000 nations it would do exactly the run that measured 36–62 ms. That is a **design defect in the spike**, found by measurement, and it is recorded rather than patched after the fact. A production resolver needs either (a) a world-size cap, (b) a per-invocation batch cap plus a continuation mechanism (Queue, Durable Object alarm, or self-fetch) that can finish a turn inside its 2-hour window, or (c) a paid plan. Each is an owner decision; none is taken here.

---

## 7. Scheduling and UTC boundaries

### 7.1 What is proven

- Slot arithmetic is correct at the boundary, one millisecond before it, and across a full UTC day (12 slots, 2h apart). Unit-tested.
- The Worker exposes a `scheduled()` handler; `wrangler dev --test-scheduled` invoked it and it resolved the current shared slot (recorded with `trigger = 'cron'`).
- The deployed Worker's schedule list contains exactly `0 */2 * * *` and `*/5 * * * *`, confirmed by `GET /accounts/{id}/workers/scripts/px-feasibility-spike/schedules` after the `PUT`.
- **A live Cron Trigger fired.** Two cron invocations were recorded in production D1:

| At (UTC) | Slot | Outcome | Nations | Duration | Rows written |
|---|---|---|---|---|---|
| 08:46:41 | 248992 (08:00) | **completed** | 1,000 | **14,883 ms** | 6,013 |
| 08:51:00 | 248992 (08:00) | **noop** | 0 | 201 ms | **0** |

The pair is the strongest single piece of evidence in this report: the first invocation resolved the current shared slot on a real trigger, and the second — five minutes later, from the same schedule — found the completed ledger, applied nothing, and wrote nothing. That is exactly-once turn resolution under a real duplicate trigger, not a simulation.

- There is no per-nation schedule anywhere in the design: one slot number is derived from one timestamp and applied to the whole world.

### 7.2 What is still not proven

- **A 24-hour run.** Only two triggers were observed, both inside the same 2-hour slot. Twelve completed boundaries in a row, with no miss, is still PV-01's open criterion.
- **Cron CPU attribution.** The analytics bucket closest to the 08:46 run reports **45.69 ms** CPU (with a 1.9 s worker duration), and the bucket near 08:51 reports 4.97 ms. Adaptive sampling does not expose an invocation ID, so the 45.69 ms figure is *consistent with* the 1,000-nation cron run exceeding the 10 ms limit, not proof that it was that invocation. The run nevertheless returned successfully, which again shows the limit is enforced with tolerance for infrequent overages.
- **Propagation timing.** Schedules were accepted at `08:22:37Z`; the first firing was `08:46:41Z` — about 24 minutes later. Cloudflare documents "up to 15 minutes". The earlier "not observed" conclusion in this report was written at 08:43:56Z, three minutes before the trigger fired; it was wrong, and this section replaces it.

**Therefore: the two-hour UTC schedule has now been exercised by the real scheduler at one boundary, including duplicate-trigger protection. The twelve-boundaries-per-day claim remains untested.**

---

## 8. Capacity, quota and cost

### 8.1 Measured per-nation cost

| Metric | Measured | Basis |
|---|---|---|
| Rows written per nation-turn | **6.01** | 6,008 / 1,000, deployed |
| Rows read per nation-turn | **~6.01** | 6,008 / 1,000, deployed |
| Statements per nation-turn | **3.0** | 3,016 / 1,000 |
| D1 queries (requests) per 250-nation batch | **8** | D6, including fixed overhead |
| Wall clock per 1,000-nation turn | **5.6–6.4 s** | D3/D7 |
| CPU per 100–250-nation batch | **1.3–5.1 ms** | sampled analytics |
| CPU per 1,000-nation invocation | **36.6–61.6 ms** | sampled analytics |
| Database growth per nation-turn | **≈ 250 bytes** | 249,856 bytes after 1,000 nation-turns |

### 8.2 What that implies against the free limits

| Limit | Arithmetic | Ceiling |
|---|---|---|
| 100,000 rows written/day | 100,000 ÷ (6.01 × 12 turns) | **≈ 1,386 nations** |
| 5,000,000 rows read/day | 5,000,000 ÷ (6.01 × 12) | ≈ 69,000 nations (not binding) |
| 500 MB database | 500 MB ÷ (250 B × 12 × 365) | ≈ **456 nation-years** of hot audit; at 1,000 nations ≈ 167 days, at 250 nations ≈ 667 days |
| 10 ms CPU per invocation | measured: 250 nations/batch fits; 1,000 in one invocation does not | **~250–500 nations per invocation** (unmeasured between the two) |
| 100,000 requests/day | 12 cron + N user requests | not binding at S1/S2 |

**The write ceiling (~1,386) lands inside Prompt 9's revised planning range of 1,100–2,000.** That is a genuine confirmation of DEF-006's correction: the earlier "~3,000" figure was optimistic, and 6 rows/nation-turn rather than 3 is why.

**The CPU ceiling is the surprise, and it is lower than the write ceiling.** Under the tested shape, ~250 nations fit one invocation comfortably; 1,000 do not. With 12 turns/day, a design that can only do 250 nations per invocation needs four invocations per boundary — which the free cron alone does not provide.

### 8.3 Cost and quota consumption of this spike

- Services used: Workers (free), D1 (free), cron schedules (free), `workers.dev` subdomain (free). No R2, no paid add-on, no custom domain, no payment method, no Supabase project.
- Rows written by the measurement runs: roughly **40,000–45,000**, i.e. **under half of one day's 100,000 free writes** (seeding plus all turn runs). That is a useful warning: capacity testing is itself a non-trivial consumer of the quota it is testing.
- Database size: **≈ 250 KB** at 1,000 nations after one turn.
- Requests: a few hundred, far below 100,000/day.
- The account's **plan tier and payment method could not be verified**: `GET /accounts/{id}/subscriptions` returned `403` because the OAuth connection has no Billing Read scope. This is a real limitation of PV-09, not a pass.
- No charge was incurred or enabled by this pass to the best of the available evidence; the absence of a billing scope means "no charge" is **asserted from the resources used**, not from a billing record.

### 8.4 Scenario verdicts after measurement

| Scenario | Before | After measurement |
|---|---|---|
| S0 prototype (1–10) | Fits | **Fits** — measured |
| S1 private playtest (25–100) | Fits | **Fits** — 100-nation batch: 1.3–5.1 ms CPU, 602 writes/turn |
| S2 modest launch (300) | Fits requests/writes; storage is a retention problem | **Borderline** — writes 21,636/day (22%); CPU needs two 150-nation batches per turn, which the cron does not obviously provide |
| S2b upper launch (1,000) | "The edge" | **CPU fails in one invocation** (36–62 ms), writes 72,000/day (72%), storage ~167 days. Needs a continuation mechanism |
| S3 growth (2,000–5,000) | Not supported | **Not supported** — writes exceed 100k/day at ~1,386 |

---

## 9. Gate verdicts

| Gate | Recorded requirement | Final status | Why |
|---|---|---|---|
| **GATE-13** | The next workstream can proceed without undocumented assumptions | **CONDITIONAL** | The assumptions are now documented in Report 10 §3.2 and this report, and one previously undocumented assumption (that a single invocation can resolve any world size) has been replaced with a measurement. But OD-02 is still undecided, the DEF-003 condition has not been accepted by the owner, and V-2/CV-002 have not run. Documentary work cannot close an owner decision or a human test. |
| **GATE-16** | Every essential component has a plausible free-tier path or an explicit blocker | **CONDITIONAL** | D1 persistence, execution, HTTPS delivery and the 12/day slot model are now **measured**, not inferred. The live scheduler is now **observed working** (a real trigger completed a 1,000-nation turn and no-opped a duplicate). But a 24-hour/12-boundary run does not exist; e-mail, backups and auth remain undecided (OD-06/07) or unmeasured (PV-15); and at ~1,000 nations the CPU budget is exceeded in one invocation. Auth is the one remaining component with neither a measured fit nor a confirmed blocker. |
| **GATE-18** | The ₹0 claim is not based on unverified capacity or a hidden paid dependency | **CONDITIONAL** | Capacity is now measured at 50/250/1,000 and the write ceiling is ~1,386 nations — better evidence than any prior version. But the measurement identifies a CPU failure at 1,000, the capacity target is not owner-approved, PV-09's billing check is blocked, and no 24-hour/12-turn or quota-exhaustion run exists (the cron evidence is two triggers inside one slot). The ₹0 claim is **supported at S0/S1, borderline at S2, and not supported at S2b/S3** under the tested shape. |

**No gate moved to PASS. No gate moved to FAIL**, because the failures observed are at an exploratory size (1,000) that the owner has not adopted as a requirement.

### 9.1 Stage 1 verdict

The deliverables are complete through Reports 10–11, but **Stage 1 readiness is not complete**. Of the 20 gates: **17 pass, 3 conditional, 0 fail** — unchanged in count from Prompt 9, changed in evidence. The correct status remains **Stage 1 incomplete — conditionally ready for bounded Stage 2 work**, and the next step is the owner decisions below, not the Game Design Bible.

---

## 10. Failures, skips and limitations

| Item | Type | Detail |
|---|---|---|
| Live Cron Trigger | **Observed** | Completed a 1,000-nation turn at `08:46:41Z` (14.9 s, 6,013 writes) and no-opped a duplicate at `08:51:00Z` (0 writes) |
| 12 consecutive boundaries | **Not observed** | Two triggers inside one slot is not a 24-hour run |
| 24-hour / 12-turn run | **Not run** | Would require a day of observation; PV-01 remains open |
| Real quota exhaustion | **Not run** | Deliberately not forced; simulated only |
| Billing/plan verification | **Blocked** | Connector lacks Billing Read scope (HTTP 403) |
| Argon2id CPU (PV-15) | **Not measured** | Would need an added dependency; PBKDF2 benchmark not run either, so the KDF question is untouched |
| E-mail throughput (PV-10) | **Blocked** | Requires a provider and an owner decision (OD-07) |
| Backup/restore drill (PV-08, OD-06) | **Not run** | Time Travel window exists; restore was not exercised |
| Mid-batch kill | **Not tested** | Fault injected between batches; no OS-level kill |
| GitHub push / CI | **Not possible** | Integration is read-only (search/commits/PRs); no repository exists for this project |
| Supabase empirical test | **Deliberately not run** | Free plan has no backups; decision is documentary (§4) |
| CPU figures | **Sampled** | Analytics, not exact per-invocation counters; noisy |
| 1,000-nation CPU gap | **Unmeasured** | The exact crossover between 250 and 1,000 nations is not known |

---

## 11. Security and maintenance notes for the spike

- The mutating routes require `x-spike-token`; the token is a Cloudflare Worker secret, not in git. A missing token makes the routes refuse everything, including a correctly formed request.
- The token used for this pass is a throwaway value for a synthetic spike. It should be rotated (`wrangler secret put SPIKE_TOKEN`) or the Worker deleted; it must never be reused for a real deployment.
- Read-only routes expose aggregate counts only: no tokens, no account data, no personal data.
- `/api/status` is public and unauthenticated. That is acceptable for synthetic data; it would not be acceptable for a world with real players.
- The spike has no rate limiting, no input-size limits beyond the seed cap, no CSRF defence (it is a token API, not a browser session), and no audit of who called it. None of that is needed for the evidence, all of it is needed before real use.
- Cleanup: `wrangler delete px-feasibility-spike` and `wrangler d1 delete px-feasibility-spike` remove the deployment and the data; deleting the Worker removes its schedules.

---

## 12. Recommended next step

1. **Owner:** decide OD-02 (scope), accept or reject the DEF-003 assumptions, and set a capacity target (or approve the exploratory sizes). Those are the only ways GATE-13 moves.
2. **Owner/next session:** leave the Worker deployed for 24 hours and read `spike_runs`, or accept that PV-01's 12-boundary criterion stays open; the trigger itself is now proven.
3. **Engineering (next Stage 2 spike):** fix the scheduled handler's missing per-invocation cap, then measure the 250→1,000 CPU crossover and a continuation mechanism if 1,000 is a real target.
4. **Do not** start the Game Design Bible or a production schema on the strength of this report. The architecture decision (D-005) stays **Provisional**.

---

## 13. Final audit — the fifteen required questions

| # | Question | Answer |
|---|---|---|
| 1 | Which project files and connected resources were inspected? | All nine Stage-1 reports, the four continuity files, both validators and `DECISIONS.md`, plus the extracted archive manifest. Cloudflare: account, Worker list, D1 list, one existing unrelated Worker (`nationsphere-api`, read only), schedules, analytics. Supabase: one project's status (`NATIONSPHERE`, `INACTIVE`). GitHub: connector inspected, no project repository exists. |
| 2 | Was the Prompt 9 correction state verified? | Yes. The working tree matched `Project X step 9 correction.zip` on **38/38** SHA-256 comparisons before any edit, and `DECISIONS.md` was not modified by this pass. |
| 3 | Were the exact gate definitions retrieved? | Yes, verbatim from P9 §20.2 (criteria) and §20.4 (blocking conditions), restated in Report 10 §3. |
| 4 | Which integrations and actions were actually available? | **Cloudflare:** read plus write — Worker upload, D1 create/query, schedule read/write. Billing read is **not** available (403). **GitHub:** read-only actions (search/commits/PRs); no repository for this project, so nothing could be pushed. **Supabase:** read of project metadata only; the project was paused and was deliberately left paused. |
| 5 | Was a real deployment completed? | **Yes** — Worker `px-feasibility-spike` on `workers.dev`, real D1 database, two cron schedules. Local workerd tests also ran; they are reported separately from the deployment. |
| 6 | What evidence supports or contradicts D1's suitability? | **Supports:** exactly-once resolution across 250 nations, resumable batches, safe failure on injected limits, 7-day Time Travel, always-on availability, 6.01 rows written per nation-turn ⇒ ~1,386-nation write ceiling, a live cron firing. **Contradicts:** 36.6–61.6 ms CPU for 1,000 nations in one invocation (10 ms budget), the 50-query-per-invocation cap, single-threaded per database, and no per-invocation record cap in the current handler. |
| 7 | What evidence supports or contradicts Supabase's suitability? | **Supports (documentary):** unlimited API requests, Postgres maturity, auth/storage/realtime, portability. **Contradicts:** free plan has **no backups or PITR** (collides with SEC-030/SEC-032) and **pauses after a week of inactivity**, which is fatal for a world that must advance 12 times a day. Not tested empirically — a documented decision, not an oversight (§4). |
| 8 | Which configuration best fits requirements and ₹0? | **Workers + D1 remains the tested candidate; Supabase is the documented fallback/exit path.** D-005 stays **Provisional**; no architecture is approved. |
| 9 | Was a real two-hour UTC scheduled trigger tested? | **Yes, at one boundary.** `08:46:41Z` completed slot 248992 (1,000 nations, 14.9 s); `08:51:00Z` correctly no-opped it (0 writes). Twelve consecutive boundaries were **not** observed (PV-01 open). |
| 10 | Results for persistence, idempotency, recovery, resumability? | Ledger persists the last completed slot across invocations; repeated and out-of-order slots are refused; 250 nations applied exactly once (250 markers, 250 audit rows, value conserved); injected interruption returns 409, records an `error` run, and a resume completes exactly once; a simulated storage limit fails safely without marking the turn complete and recovers afterwards. |
| 11 | Which measurements are reproducible, which are estimates? | **Reproducible:** rows written/read (6.01 per nation-turn), statements per nation-turn (3.0), requests per batch, wall clock, batch counts — all from D1 rows the scripts recreate. **Sampled/estimated:** CPU (analytics buckets, no per-invocation ID), the 250→1,000 crossover, and all monthly extrapolations. |
| 12 | Which tests passed, failed, skipped or were blocked? | **Passed:** 11/11 unit, 23/23 local integration, all deployed checks, `validate_final.py`, `09_validate.py` (68/68). **Blocked:** billing/plan read (403), GitHub push/CI (no repo, read-only), e-mail (no provider), Argon2id CPU (no benchmark), 24-hour run and real quota exhaustion (not attempted). **Skipped by design:** Supabase empirical test, mid-batch OS kill. |
| 13 | Final status of each readiness gate? | **GATE-13 CONDITIONAL**, **GATE-16 CONDITIONAL**, **GATE-18 CONDITIONAL** — reasons and evidence in §9.1. No gate moved to PASS; none moved to FAIL. |
| 14 | Does Stage 1 meet its documented completion criteria? | **No.** 17 pass / 3 conditional / 0 fail. Documentation is complete and consistent; readiness is not. |
| 15 | Exact next task? | Owner decisions **OD-02** (scope), a capacity target, and OD-06/07 (backups, e-mail); then leave the spike deployed 24 hours to close PV-01's 12-boundary criterion, and cap per-invocation work in the scheduled handler before any 1,000-nation claim. |
