# Report 11 — Free-tier technical feasibility results

**Version:** 1.1 (corrected 2026-10-23 by Prompt 10.1; the Supabase + Cloudflare architecture was then tested and recorded in §§14–19)
**Date:** 2026-10-23
**Status:** Measurement record. Supersedes the planned statuses in [Report 10](10_stage_1_gate_evidence_and_feasibility_plan.md) where they differ. §14 lists the claims in v1.0 that were wrong and what replaced them; read it before quoting anything above it.
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
| Did a live Cron Trigger fire? | **Yes — but not the product schedule.** Nine invocations were recorded between 08:46:41Z and 09:26:00Z, all on the temporary `*/5 * * * *` test schedule. The `0 */2 * * *` schedule never fired in the observation window (its first opportunity was 10:00Z). See §7 and §14.1 |
| Are the 100k/day write limits a real constraint? | **Yes, and now quantified** — 6.01 rows written per nation-turn, so ~1,388 nations at 12 turns/day |
| Is ₹0 still credible? | **Conditional** — at small sizes, yes; at ~1,000 nations in one invocation, the CPU limit is exceeded |
| Did this pass verify the account's plan/billing? | **No** — the connector lacks Billing Read scope (403) |

**GATE-13, GATE-16 and GATE-18 all remain CONDITIONAL.** The evidence is materially stronger than before, and one genuinely new failure mode was found, but none of the three gates' recorded acceptance criteria is fully met. Details in §9.

---

## 1. Environment and what was actually executed

| Item | Value |
|---|---|
| Project root | `C:\Users\suren\Downloads\Project X` |
| Starting state | 38 files matched `Project X step 9 correction.zip` byte-for-byte before any edit; re-verified in Prompt 10.1 against baseline commit `a1174d8` (20 exact, 16 line-ending-only, 2 gitignored). See §14.2 |
| Version control | Local git repository created in this pass; baseline commit `a1174d8` on `main`; work on branch `prototype/free-tier-feasibility` |
| Local runtime | `workerd` via `wrangler 4.152.0`, local D1 (Miniflare) |
| Deployed runtime | Cloudflare Workers, compatibility date `2026-10-23`, script `px-feasibility-spike` |
| Deployed database | D1 `px-feasibility-spike`, id `850d9eb4-7a44-4365-81f5-cca954b3738b`, region APAC |
| Public endpoint | `https://px-feasibility-spike.nationsphere.workers.dev` |
| Schedules configured | `0 */2 * * *` (product) and `*/5 * * * *` (test-only, to observe cron without a 2-hour wait) |
| Data | Synthetic nations `Synthetic Nation 1…N`; no player, account or personal data |

**A note on the Supabase integration (v1.0).** At the start of Prompt 10 the connected account contained one Supabase project, `NATIONSPHERE`, in region `ap-southeast-2`, status **`INACTIVE`** (paused). In v1.0 it was read for status only and deliberately left paused. **Prompt 10.1 reversed that decision** once the owner selected Supabase: the project was resumed, and a fully isolated `feasibility` schema was created and tested inside it. Nothing in the project's pre-existing `public` schema was read, altered or depended on. The v1.0 reasoning is preserved in §4 with a correction; the new results are in §§14–19.

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
5. **Supabase's free plan has no *provider-managed* backups.** The pricing page lists "Automatic backups: Not included" and PITR is paid-only. The official backups page recommends that free-tier projects "regularly export their data using the Supabase CLI `db dump` command and maintain off-site backups", so a restorable backup is achievable — by the owner, on a schedule, stored separately. SEC-030/SEC-032 are therefore satisfiable in principle but not by default. Corrected in §14.4: v1.0 described this as "no backups at all", which understated the documented export path.

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
| Free backups | **7-day Time Travel** | **No provider-managed backups**; documented path is an owner-run `supabase db dump` stored off-site, plus a tested restore | D1 on convenience, not on feasibility (corrected — see §14.4) |
| Idle behaviour | Always available | **Paused after a week of low activity**; "a few user requests to the database each day" is documented as enough to prevent it | D1 on principle; a live game with daily traffic should not pause (corrected — see §14.3) |
| Connection model from a Worker | Native binding, no pooler | Pooler/Hyperdrive; extra hop and connection budget | D1 |
| Scheduling | Native UTC cron (5 free); one boundary observed firing live | `pg_cron` inside Postgres; not exercised | D1 on evidence, not only on principle (see §7) |
| Recovery/restore | Time Travel + `d1 export` | None on Free | D1 |
| Relational maturity, auth, storage, realtime | Weaker (no native auth; SQLite) | Much stronger | Supabase |
| Lock-in | SQLite dialect; export available | Postgres; portable | Supabase |

**v1.0 recommendation (superseded 2026-10-23 by the owner's decision, D-008): keep Workers + D1 as the tested candidate and treat Supabase as the exit/fallback target.** Two facts drove it: the absence of provider-managed free backups and the idle pause. Both were overstated (§14.3–14.4), and in any case the owner has since selected Supabase (D-008). The recommendation is preserved here as history, not as the current position.

**Creating a Supabase test project was rejected in v1.0** on the grounds that the free plan allows two active projects, creation is slow, and there are no backups to test. Prompt 10.1 did not create a project either — it used the existing `NATIONSPHERE` project, resumed it, and isolated all work in a new `feasibility` schema. The v1.0 non-test is therefore superseded by an actual test (§15).

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
- **A live Cron Trigger fired — from the five-minute test schedule, not the product schedule.** The deployed D1 database records nine cron invocations, all read on 2026-10-23:

| At (UTC) | Slot | Outcome | Nations | Duration | Rows written |
|---|---|---|---|---|---|
| 08:46:41 | 248992 (08:00) | **completed** | 1,000 | **14,883 ms** | 6,013 |
| 08:51:00 | 248992 (08:00) | noop | 0 | 201 ms | 0 |
| 08:56:00, 09:01:53, 09:06:00, 09:11:01, 09:16:00, 09:21:00, 09:26:00 | 248992 (08:00) | noop (seven more) | 0 | 197–517 ms | **0** |

The nine timestamps sit on a five-minute cadence (the 08:45 tick, delayed to 08:46:41, then every five minutes). That is the signature of `*/5 * * * *`, the temporary schedule added to observe cron without waiting two hours — **not** of `0 */2 * * *`. The 08:00 boundary had passed at 08:22 when the schedules were created, and the product schedule's next opportunity was 10:00Z, outside the observation window. **The product two-hour schedule has never been observed firing.** The `*/5` schedule was removed at 09:31Z; only `0 */2 * * *` remains.

What the nine invocations *do* prove is still the strongest single piece of evidence in this report, and it is about duplicate protection rather than cadence: the first invocation resolved the shared slot for 1,000 nations, and the eight that followed found the completed ledger and wrote nothing at all. That is exactly-once turn resolution under repeated real triggers, not a simulation.

- There is no per-nation schedule anywhere in the design: one slot number is derived from one timestamp and applied to the whole world.

### 7.2 What is still not proven

- **A 24-hour run.** Only two triggers were observed, both inside the same 2-hour slot. Twelve completed boundaries in a row, with no miss, is still PV-01's open criterion.
- **Cron CPU attribution.** The analytics bucket closest to the 08:46 run reports **45.69 ms** CPU (with a 1.9 s worker duration), and the bucket near 08:51 reports 4.97 ms. Adaptive sampling does not expose an invocation ID, so the 45.69 ms figure is *consistent with* the 1,000-nation cron run exceeding the 10 ms limit, not proof that it was that invocation. The run nevertheless returned successfully, which again shows the limit is enforced with tolerance for infrequent overages.
- **Propagation timing.** Schedules were accepted at `08:22:37Z`; the first firing was `08:46:41Z` — about 24 minutes later. Cloudflare documents "up to 15 minutes". The earlier "not observed" conclusion in this report was written at 08:43:56Z, three minutes before the trigger fired; it was wrong, and this section replaces it.

**Therefore: the real scheduler was exercised, and duplicate-trigger protection held across nine invocations — but all of them were driven by the temporary five-minute schedule. Neither the two-hour product schedule nor twelve consecutive boundaries have been observed.** This is corrected in §14.1; v1.0 wrongly described the firings as proof that the product cadence had run.

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
| **GATE-16** | Every essential component has a plausible free-tier path or an explicit blocker | **CONDITIONAL** | D1 persistence, execution, HTTPS delivery and the 12/day slot model are now **measured**, not inferred, and duplicate triggers held across nine real invocations. But every one of those invocations came from the temporary five-minute schedule; the product two-hour schedule was never observed firing. A 24-hour/12-boundary run does not exist; e-mail and backups remain undecided (OD-06/07); auth is unmeasured at 1,000 users (PV-15); and at ~1,000 nations one invocation exceeds the free CPU budget. §16 re-assesses this gate under the owner-selected Supabase architecture. |
| **GATE-18** | The ₹0 claim is not based on unverified capacity or a hidden paid dependency | **CONDITIONAL** | Capacity is now measured at 50/250/1,000 and the write ceiling is ~1,386 nations — better evidence than any prior version. But the measurement identifies a CPU failure at 1,000, the capacity target is not owner-approved, PV-09's billing check is blocked, and no 24-hour/12-turn or quota-exhaustion run exists (the cron evidence is two triggers inside one slot). The ₹0 claim is **supported at S0/S1, borderline at S2, and not supported at S2b/S3** under the tested shape. |

**No gate moved to PASS. No gate moved to FAIL**, because the failures observed are at an exploratory size (1,000) that the owner has not adopted as a requirement.

### 9.1 Stage 1 verdict

The deliverables are complete through Reports 10–11, but **Stage 1 readiness is not complete**. Of the 20 gates: **17 pass, 3 conditional, 0 fail** — unchanged in count from Prompt 9, changed in evidence. The correct status remains **Stage 1 incomplete — conditionally ready for bounded Stage 2 work**, and the next step is the owner decisions below, not the Game Design Bible.

---

## 10. Failures, skips and limitations

| Item | Type | Detail |
|---|---|---|
| Live Cron Trigger | **Observed, test schedule only** | Nine invocations at a five-minute cadence between `08:46:41Z` and `09:26:00Z`; the first completed a 1,000-nation turn (14.9 s, 6,013 writes), the other eight wrote nothing. The `0 */2 * * *` schedule never fired in the window |
| 12 consecutive boundaries | **Not observed** | Nine triggers inside one slot is not a 24-hour run, and none came from the product schedule |
| 24-hour / 12-turn run | **Not run** | Would require a day of observation; PV-01 remains open |
| Real quota exhaustion | **Not run** | Deliberately not forced; simulated only |
| Billing/plan verification | **Blocked** | Connector lacks Billing Read scope (HTTP 403) |
| Argon2id CPU (PV-15) | **Not measured** | Would need an added dependency; PBKDF2 benchmark not run either, so the KDF question is untouched |
| E-mail throughput (PV-10) | **Blocked** | Requires a provider and an owner decision (OD-07) |
| Backup/restore drill (PV-08, OD-06) | **Not run** | Time Travel window exists; restore was not exercised |
| Mid-batch kill | **Not tested** | Fault injected between batches; no OS-level kill |
| GitHub push / CI | **Not possible** | Integration is read-only (search/commits/PRs); no repository exists for this project |
| Supabase empirical test (v1.0) | **Superseded** | v1.0 deliberately skipped it; Prompt 10.1 ran it in isolation and recorded the results in §15 |
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

## 13. Final audit — the fifteen required questions (v1.0; corrected where marked)

> Prompt 10.1 required its own twenty-question audit; that is §19, and where the two differ, §19 wins. The answers below were corrected on 2026-10-23 where the original evidence did not support them (Q2, Q7, Q8, Q9, Q15).

| # | Question | Answer |
|---|---|---|
| 1 | Which project files and connected resources were inspected? | All nine Stage-1 reports, the four continuity files, both validators and `DECISIONS.md`, plus the extracted archive manifest. Cloudflare: account, Worker list, D1 list, one existing unrelated Worker (`nationsphere-api`, read only), schedules, analytics. Supabase: one project's status (`NATIONSPHERE`, `INACTIVE`). GitHub: connector inspected, no project repository exists. |
| 2 | Was the Prompt 9 correction state verified? | **Yes, and re-verified in Prompt 10.1.** All 38 archive files were compared to baseline commit `a1174d8`: 20 identical byte-for-byte, 16 identical after line-ending normalisation, 2 (`.freebuff/`) absent because they are gitignored. `DECISIONS.md` was not modified by the v1.0 pass; Prompt 10.1 modified it only to record the owner's two approved decisions (D-007, D-008). |
| 3 | Were the exact gate definitions retrieved? | Yes, verbatim from P9 §20.2 (criteria) and §20.4 (blocking conditions), restated in Report 10 §3. |
| 4 | Which integrations and actions were actually available? | **Cloudflare:** read plus write — Worker upload, D1 create/query, schedule read/write. Billing read is **not** available (403). **GitHub:** read-only actions (search/commits/PRs); no repository for this project, so nothing could be pushed. **Supabase:** read of project metadata only; the project was paused and was deliberately left paused. |
| 5 | Was a real deployment completed? | **Yes** — Worker `px-feasibility-spike` on `workers.dev`, real D1 database, two cron schedules. Local workerd tests also ran; they are reported separately from the deployment. |
| 6 | What evidence supports or contradicts D1's suitability? | **Supports:** exactly-once resolution across 250 nations, resumable batches, safe failure on injected limits, 7-day Time Travel, always-on availability, 6.01 rows written per nation-turn ⇒ ~1,386-nation write ceiling, a live cron firing. **Contradicts:** 36.6–61.6 ms CPU for 1,000 nations in one invocation (10 ms budget), the 50-query-per-invocation cap, single-threaded per database, and no per-invocation record cap in the current handler. |
| 7 | What evidence supports or contradicts Supabase's suitability? | **Corrected — now tested (§15).** Supports: exactly-once resolution held, a failed transaction rolled back completely, a 1,000-nation slot resolved in 47–59 ms of database time, RLS and grants denied every prohibited action, and pg_cron fired on schedule. Contradicts: the free plan has **no provider-managed backups** (a documented export exists but an owner-run, tested restore is required), storage grows ~291 bytes per nation-turn (≈4 MB/day at 1,000 nations ⇒ the 500 MB free database is a ~125-day budget without retention), and the project is shared with an unrelated pre-existing schema. The v1.0 claim that pausing is "fatal" was wrong (§14.3). |
| 8 | Which configuration best fits requirements and ₹0? | **Superseded by D-008.** The owner selected Cloudflare hosting + Supabase backend/database on 2026-10-23. The engineering details remain provisional; D-005 is marked superseded, not deleted. |
| 9 | Was a real two-hour UTC scheduled trigger tested? | **No — corrected.** Nine real cron invocations were recorded, all on the temporary `*/5 * * * *` schedule; the first completed slot 248992 (1,000 nations, 14.9 s) and the other eight wrote nothing. The `0 */2 * * *` schedule had no opportunity to fire inside the window. The two-hour cadence was tested for arithmetic and for duplicate protection, not for scheduling. |
| 10 | Results for persistence, idempotency, recovery, resumability? | Ledger persists the last completed slot across invocations; repeated and out-of-order slots are refused; 250 nations applied exactly once (250 markers, 250 audit rows, value conserved); injected interruption returns 409, records an `error` run, and a resume completes exactly once; a simulated storage limit fails safely without marking the turn complete and recovers afterwards. |
| 11 | Which measurements are reproducible, which are estimates? | **Reproducible:** rows written/read (6.01 per nation-turn), statements per nation-turn (3.0), requests per batch, wall clock, batch counts — all from D1 rows the scripts recreate. **Sampled/estimated:** CPU (analytics buckets, no per-invocation ID), the 250→1,000 crossover, and all monthly extrapolations. |
| 12 | Which tests passed, failed, skipped or were blocked? | **Passed:** 11/11 unit, 23/23 local integration, all deployed checks, `validate_final.py`, `09_validate.py` (68/68). **Blocked:** billing/plan read (403), GitHub push/CI (no repo, read-only), e-mail (no provider), Argon2id CPU (no benchmark), 24-hour run and real quota exhaustion (not attempted). **Skipped by design:** Supabase empirical test, mid-batch OS kill. |
| 13 | Final status of each readiness gate? | **GATE-13 CONDITIONAL**, **GATE-16 CONDITIONAL**, **GATE-18 CONDITIONAL** — reasons and evidence in §9.1. No gate moved to PASS; none moved to FAIL. |
| 14 | Does Stage 1 meet its documented completion criteria? | **No.** 17 pass / 3 conditional / 0 fail. Documentation is complete and consistent; readiness is not. |
| 15 | Exact next task? | **Superseded — see §19.** Prompt 10.1's next task is to observe the product two-hour schedule at a real boundary, then design the owner-run backup and restore drill that the free plan does not provide. |

---

## 14. Corrections to v1.0 (Prompt 10.1)

The owner's Prompt 10.1 asked for the earlier conclusions to be re-checked rather than repeated. Six things were wrong, overstated, or unsupported. Each is corrected here, in place above, and in the continuity files.

| # | v1.0 claim | Correction | Evidence |
|---|---|---|---|
| 14.1 | "A live Cron Trigger fired … the two-hour schedule has now been exercised by the real scheduler at one boundary" | **Wrong.** Nine invocations were recorded, all on the temporary `*/5 * * * *` schedule. The product `0 */2 * * *` schedule never fired in the window; the 08:00 boundary had already passed when the schedules were created at 08:22Z, and the next opportunity was 10:00Z. Duplicate protection is proven; product cadence is not | D1 `spike_runs`: nine rows, 08:46:41 → 09:26:00, five-minute cadence; schedule list read at 09:31Z |
| 14.2 | "Byte-identical to `Project X step 9 correction.zip` (38/38 SHA-256 matches)" | **Undated and no longer repeatable as stated**, because six documents have been edited since. Re-verified against baseline commit `a1174d8` instead: 20 of 38 archive files identical byte-for-byte, 16 identical after line-ending normalisation (the archive stores CRLF, git stores LF), 2 absent because `.freebuff/` is gitignored | `zipfile` + `git show a1174d8:<path>` comparison, 2026-10-23 |
| 14.3 | Supabase "pauses after a week of inactivity … fatal for a world that must advance 12 times a day" | **Overstated.** The documented trigger is *low activity over seven days*; Supabase states that "a few user requests to the database each day over the previous week is enough" to prevent pausing. A live game with players and a two-hourly job is exactly the traffic that prevents it. The real risk is a **pre-launch or dormant** project pausing — recoverable for up to a year — not a running world | [free-project-pausing](https://supabase.com/docs/guides/platform/free-project-pausing), read 2026-10-23 |
| 14.4 | Supabase free plan has "no backups at all" / "None on Free" | **Imprecise.** There are no *provider-managed* backups and no PITR, but Supabase's own backups page directs free-tier projects to "regularly export their data using the Supabase CLI `db dump` command and maintain off-site backups". The requirement is satisfiable by the owner; it is simply not automatic | [backups](https://supabase.com/docs/guides/platform/backups), read 2026-10-23 |
| 14.5 | "This pass verified …" for the D1 numbers | **Partly reproducible only.** The local unit and integration suites can be re-run in this workspace; the deployed D1 runs cannot be re-created without re-running the spike against production D1 (and spending the quota it measures). They are retained as *previously reported* measurements, not independently re-verified in 10.1 | §5.1–5.2 re-run in 10.1; deployed rows read from D1 directly |
| 14.6 | Architecture recommendation: "keep D1 as the tested candidate, Supabase as fallback" | **Overtaken by the owner's decision** (D-008). Preserved as history in §4; the current direction is Cloudflare hosting + Supabase backend/database | [DECISIONS.md](../DECISIONS.md) D-008 |

### 14.7 What was re-run, and what was not

| Check | Rerun in 10.1? | Result |
|---|---|---|
| `node --test test/slots.test.js` (D1 prototype) | **Yes** | 11/11 passed |
| `node scripts/integration.mjs` (local workerd + local D1) | **Yes** | 23/23 passed |
| Deployed D1 measurements | Re-read, not re-run | Nine cron rows and the earlier HTTP runs are still in `spike_runs` |
| `validate_final.py`, `09_validate.py` | **Yes** | Updated and passing (see §18) |
| Supabase turn engine | **Yes — new** | §15 |
| Cloudflare page deployment | **Yes — new** | §15.7 |

---

## 15. Supabase + Cloudflare feasibility results (Prompt 10.1)

The owner selected Cloudflare hosting + Supabase backend/database (D-008). The smallest test that could produce evidence for the gates under that direction was built and run. Everything below is a real execution against the owner's connected accounts, not a simulation.

### 15.1 Where it ran, and what was isolated

| Item | Value |
|---|---|
| Supabase project | `NATIONSPHERE`, ref `suotjamclwdithcitspe`, region `ap-southeast-2`, PostgreSQL 17.6.1.166 |
| Status at start | `INACTIVE` (paused). Resumed with the connected integration; reached `ACTIVE_HEALTHY` |
| Isolation | New schema `feasibility`. **Nothing in the pre-existing `public` schema was read, altered or depended on** |
| Extensions added | `pg_cron` (for the scheduler test) |
| Rows | 1,000 synthetic nations; 3,000 nation-turn markers; 3,000 audit rows. No accounts, no personal data |
| Cloudflare | Worker `nation-supremacy` on `nationsphere.workers.dev`; the D1 spike `px-feasibility-spike` left in place |

**Two things the next session must know.**

1. The project was **not empty**. It already contained a `public` schema with `app_meta`, `ns_rate_limit_config`, `ns_signup_attempts`, `ns_signup_reservations`, `ns_signup_bypass` and `player_profiles`, all with zero rows and comments referring to ADR-037/ADR-040. Those are not part of this project's saved documentation and were left untouched. They may be an earlier attempt at the same game; that is an owner question, not something this report can resolve.
2. The Supabase tooling flagged **`public.app_meta` as having Row Level Security disabled**, which would expose it through the Data API to anyone holding the publishable key. No change was made: enabling RLS without policies would break whatever uses it. The owner must decide. The remediation statement is `ALTER TABLE "public"."app_meta" ENABLE ROW LEVEL SECURITY;` — but only after deciding which policies it needs.

### 15.2 The engine, in one paragraph

`feasibility.current_slot(ts)` is `floor(epoch(ts)/7200)`, so every boundary is an even UTC hour and a 24-hour window contains exactly 12 slots. A slot is claimed by inserting into `turn_runs`, whose primary key is the slot; a completed slot returns `noop` before any work. Each batch is a single SQL statement: candidate nations are selected `for update`, `turn_applied` is inserted with `on conflict (slot, nation_id) do nothing`, the treasury and `last_slot` are updated from the rows actually inserted, and an audit row is written for each — so the value change and its audit row cannot disagree. A `pg_try_advisory_xact_lock` serialises resolvers. `turn_runs.cursor` advances forward-only, which is what makes a partial slot resumable.

### 15.3 Persistence, idempotency, resumability, failure

| Test | Result |
|---|---|
| Slot arithmetic | `08:00:00Z → 248992`, `07:59:59.999999Z → 248991`, `10:00:00Z → 248993`; step 1; **12 distinct slots in 24 h**. Matches the D1 spike's slot number for 08:00Z exactly |
| Batch 1 (250) | `partial`, 250 applied, cursor 250, 750 remaining, **25.2 ms** |
| Batch 2 (250, resumed) | `partial`, cumulative 500, cursor 500, **15.5 ms** |
| Final batch (1,000) | `completed`, cumulative 1,000, **24.3 ms** |
| Duplicate trigger on the completed slot | `noop`, reason `slot already completed`, 0 applied |
| Older slot | `noop`, reason `older than the last completed slot` |
| Conservation | **1,000 markers, 1,000 audit rows, treasury sum 10,000, 0 wrong rows, 0 stale slots** |
| Injected failure mid-batch | Exception raised; **the whole transaction rolled back**: 0 run rows, 0 markers, 0 audit rows, treasury unchanged |
| Retry after that failure | `completed`, 1,000 applied, 1,000 markers, 1,000 audit rows, treasury 20,000 — **no duplication, no gap** |
| Whole slot, batch 250 | `completed`, 1,000 applied, 4 batches, **47.2 ms** |
| Two overlapping calls | The harness serialised them: the second saw the completed slot and returned `noop` in 3.3 ms. **True concurrency was not exercised** |

The rollback result is the important difference from D1. D1's per-nation batches commit independently, so an interruption leaves the ledger `running` and a resume continues. PostgreSQL's single-transaction batch means an interruption leaves **nothing**; the retry redoes the batch from the same cursor. Both are safe, and the Postgres behaviour is simpler to reason about; the cost is that a very large batch is also a very large transaction.

### 15.4 Access control — tested, not asserted

All tests ran as the real roles (`set local role authenticated` / `anon`) with a synthetic JWT claim, in rolled-back transactions.

| Test | Result |
|---|---|
| `authenticated` (sub `user-a`) reads its own profile | 1 row, own only |
| `authenticated` reads `user-b`'s profile | **0 rows** (RLS) |
| `authenticated` updates `user-b`'s profile | **0 rows affected** (RLS) |
| `authenticated` updates `nations.treasury` | **permission denied for table nations** |
| `authenticated` executes the resolver | **permission denied for function resolve_slot** |
| `anon` reads `profiles` | **permission denied for table profiles** |
| `authenticated` reads the world | 1,000 rows — the intended read-only world view |

A signed-in player therefore cannot move a treasury, mark a turn complete, write an audit row, or read another player's record. That is the client-trust boundary SEC-010/012 asks for, tested at the database layer. It is **not** a test of the HTTP/PostgREST path, of Supabase Auth, or of a real browser session.

### 15.5 Scheduling

| Test | Result |
|---|---|
| `pg_cron` available | Installed; `cron.job` and `cron.job_run_details` present |
| Temporary every-minute job | Fired at **09:39:00.04Z** and **09:40:00.03Z**; `job_run_details.status = succeeded`. Removed after the test |
| Product job `0 */2 * * *` | Created 09:40:52Z. **Fired at 10:00:00Z**, resolved slot 248993, `job_run_details.status = succeeded`, heartbeat row written |
| Duplicate protection under the real scheduler | Slot 248993 had already been completed by the test sequence, so the scheduled run **no-opped** and wrote nothing but the heartbeat |

The product schedule fired **exactly on the boundary**, in the chosen platform, with no propagation delay observed. That is materially better evidence than the Cloudflare test, where the observed firings came from a five-minute schedule. It is still **one boundary**, not twelve.

### 15.6 Capacity and storage

| Metric | Measured |
|---|---|
| Database time, 1,000-nation slot | **47.2 ms** (batch 250) and **59.1 ms** (batch 100) |
| Database time, 250-nation batch | 15.5–25.2 ms |
| Table growth | 1,000 → 3,000 nation-turns added 582 KB across the three tables |
| **Marginal storage** | **≈ 291 bytes per nation-turn** (markers + audit + nation row) |
| Extrapolation at 1,000 nations, 12 turns/day | ≈ 3.5 MB/day ⇒ **the 500 MB free database is a ~140-day budget** without retention |
| Whole database | 13.0 MB, of which the spike is ~1.2 MB; the rest is the pre-existing schema and platform catalogs |

Unlike the Workers free plan, Supabase's free plan does not meter CPU per query; the binding constraints are **500 MB of database, 5 GB of egress, and 2 active projects**. The 500 MB limit is per project, and this project is already shared with another schema, so retention policy is not optional at 1,000 nations.

### 15.7 Cloudflare website

| Check | Result |
|---|---|
| URL | **https://nation-supremacy.nationsphere.workers.dev** — live, HTTPS |
| Document title | `<title>Nation Supremacy</title>` |
| Visible heading | `<h1>Nation Supremacy</h1>` |
| `/` | `200`, `text/html; charset=utf-8`, 1,972 bytes |
| `/health` | `200`, JSON: service, build, `role: feasibility preview, not the game` |
| Unknown path | `404` |
| `POST /` | `405` with `Allow: GET, HEAD` |
| Headers | CSP (`default-src 'none'`, inline style/script only), `nosniff`, `no-referrer`, `X-Frame-Options: DENY` |

The page is **served by a Worker script**, not by the static-assets pipeline. That is a limitation of the connector, not a design choice: the static-assets upload requires an `Authorization` header on the asset-upload request, and the connected tool can only send the account token. Static assets are free and unmetered on Workers, so production should use them (or Pages); doing so needs `wrangler` with an API token, which this environment did not have.

Two deployment faults occurred and are recorded because they are the kind of thing that silently produces a "deployed" site that does not work: the first upload stored the multipart envelope as the script body (the API accepted it, and the Worker returned `error code: 1042`), and the second upload succeeded but left **`workers.dev` disabled for the script**, which also returned 404. The fix was to upload the module as raw JavaScript and enable the script subdomain explicitly.

### 15.8 What this does not prove

- **No true concurrency.** The two-invocation test was serialised by the tool; the advisory lock has not been exercised against a real second session. The unique constraints are what was tested.
- **No backup or restore.** No export was taken, no restore was drilled. The free plan has no provider-managed backups (§14.4).
- **No auth flow.** RLS was tested by switching Postgres roles, not through a browser session and not through Supabase Auth.
- **No 24-hour run.** One product boundary, at 10:00:00Z.
- **No load test.** 1,000 synthetic nations, one operation at a time.
- **No PostgREST/edge-function path.** The resolver is a database function; exposing it through the Data API was not attempted, and should not be (SEC-010).

---

## 16. Gate re-assessment under D-008

The gates themselves did not change. Their evidence did, and the architecture they are assessed against is now Supabase + Cloudflare rather than Workers + D1.

| Gate | Recorded requirement | Status | Evidence now | What is still missing |
|---|---|---|---|---|
| **GATE-13** | The next workstream can proceed without undocumented assumptions | **CONDITIONAL** | The assumptions are documented; the architecture direction is now an owner decision (D-008), not an unresolved question | **OD-02** (scope) is still undecided, the DEF-003 condition has not been accepted, and V-2/CV-002 have still not run |
| **GATE-16** | Every essential component has a plausible free-tier path or an explicit blocker | **CONDITIONAL** | Website hosting (Cloudflare, live), database (Supabase, tested), scheduler (pg_cron, fired on the boundary), exactly-once resolution, resumable batches, least privilege and RLS all have evidence in the chosen architecture. Auth has a plausible free path (50,000 MAU) | **No 24-hour/12-boundary run**; no backup/restore drill; e-mail (OD-07) still undecided; auth is documented, not exercised; the free database's 500 MB needs a retention policy before 1,000 nations |
| **GATE-18** | The ₹0 claim is not based on unverified capacity or a hidden paid dependency | **CONDITIONAL** | No paid dependency found in the chosen configuration. Storage and time are measured (291 B/nation-turn, 47–59 ms per 1,000-nation slot). The website is free | **Capacity target still unapproved**; billing tier still unverifiable through the connector; no quota-exhaustion run; retention cost not yet modelled as a decision |

**No gate moves to PASS, and none moves to FAIL.** GATE-16 is now much closer: the only missing component with no measurement at all is e-mail (OD-07), and the only missing *process* is backup/restore.

### 16.1 Stage 1 verdict

**Stage 1 is not complete.** 17 gates pass, 3 are conditional, 0 fail — the same counts as Prompt 9, with stronger evidence and a settled architecture direction. The verdict remains **conditionally ready for bounded Stage 2 work**.

---

## 17. ₹0 cost analysis for the selected architecture

| Component | Free allowance (verified 2026-10-23) | What it means here | Risk |
|---|---|---|---|
| Cloudflare Worker requests | 100,000/day | A page + health check per visit; not binding for a small game | Low |
| Cloudflare static assets | Free and unlimited (production path) | The prototype uses a Worker instead; production should not | None |
| Supabase database | 500 MB/project | ≈140 days at 1,000 nations × 12 turns without retention | **Medium** — needs a retention decision |
| Supabase egress | 5 GB/month | A 2 KB page is ~5 GB at 2.5 M page views; a JSON API costs more | Low for a small world |
| Supabase API requests | Unlimited | The turn engine is a database function, so it does not consume API quota | None |
| Supabase MAU | 50,000 | Far above a small launch | None |
| Supabase projects | 2 active | This project already exists; a second would be a test/staging project | Low |
| Supabase backups | **Not included** | Owner-run `db dump` + off-site storage required. Storage of a 500 MB dump is not free everywhere | **Medium** — an operational obligation, not a fee |
| Supabase pause | After a week of low activity | A live game will not pause; a dormant pre-launch project will | Low, recoverable for 1 year |
| Supabase log retention | 1 day | Enough for debugging, not for incident review | Medium for operations |
| Supabase Edge Functions | 500,000 invocations | Not needed: the resolver is a database function | None |

**Verdict: ₹0 in mandatory monthly cost is supported for the selected architecture at prototype/small-playtest scale**, provided (a) audit retention is designed before ~1,000 nations, (b) backups are exported by the owner, and (c) no Edge Function or paid add-on becomes necessary. It is **not** a guarantee, and it is **not yet evidenced beyond one boundary and one synthetic world**.

---

## 18. Tests, validators and documentation changes

| Check | Result |
|---|---|
| `node --test test/slots.test.js` (D1 prototype, re-run) | **11/11 passed** |
| `node scripts/integration.mjs` (local workerd + D1, re-run) | **23/23 passed** |
| Supabase migration `0001`, `0002`, `0003`, `pg_cron` | **Applied successfully** |
| Supabase engine tests (§15.3) | **10 of 11 passed**; true concurrency **not exercised** (the harness serialised the two calls) |
| Supabase access-control tests (§15.4) | **7/7 passed** |
| Cloudflare site checks (§15.7) | **6/6 passed** |
| `python qa_backups/validate_final.py` | **ALL CHECKS PASSED** after the update below |
| `python qa_backups/09_validate.py` | **74/74 passed** after the update below |

**Validator changes, disclosed.** `09_validate.py` asserted `D-001…D-006` and that no `D-007` exists — a guard written when nothing was owner-approved. Two decisions now are (D-007, D-008), so the assertion had to change or it would fail on a correct document. It now asserts that D-004 is still `Provisional`, that D-005 is marked `Superseded by D-008`, that D-007 and D-008 exist with the right subject matter, and that the decision count is 8. `validate_final.py` carried the same stale pair of expectations (D-005 `Provisional`, "unexpected D-007") and was updated the same way. No assertion was deleted, and none was weakened to hide a defect.

---

## 19. Final audit — the twenty required questions

| # | Question | Answer |
|---|---|---|
| 1 | Which files and connected resources were inspected? | The four continuity files, Reports 9–11, both validators, `DECISIONS.md`, and the whole `prototypes/` tree. Cloudflare: account, Worker list, subdomain, schedules, D1 rows, deployments. Supabase: project metadata, tables, extensions, `pg_cron`, roles and privileges. GitHub: repository search and file reads |
| 2 | Was the Prompt 9 correction state verified? | **Yes.** All 38 archive files compared to baseline commit `a1174d8`: 20 exact, 16 line-ending-only, 2 gitignored. Zero content differences |
| 3 | Was the owner's architecture decision recorded consistently? | **Yes.** D-008 in `DECISIONS.md`; D-005 marked superseded; Reports 10–11 and all three continuity files state the same direction |
| 4 | Is Nation Supremacy recorded as the official name? | **Yes.** D-007, `AI_CONTEXT` §2, the handoff, the progress table, Report 11, and the deployed page title/heading |
| 5 | Does the prototype display Nation Supremacy? | **Yes** — `<title>Nation Supremacy</title>` and `<h1>Nation Supremacy</h1>`, verified by fetching the live URL |
| 6 | Was the website actually deployed to Cloudflare? | **Yes** — a real Worker deployment, publicly reachable over HTTPS |
| 7 | Exact verified public URL? | **https://nation-supremacy.nationsphere.workers.dev** |
| 8 | Was Supabase actually tested? | **Yes** — real project, real migrations, 1,000 synthetic nations, real `pg_cron` |
| 9 | Did the authentication and protected-state tests pass? | **Yes at the database layer**: RLS isolates rows, and grants deny treasury updates, resolver execution and audit reads. **Auth itself (sign-up, session, JWT issuance) was not exercised** |
| 10 | Was the shared two-hour turn tested against a real scheduled trigger? | **Yes, once.** `pg_cron` fired the product job at **10:00:00Z** on the boundary and resolved the current slot |
| 11 | Was a complete 24-hour, 12-turn observation completed? | **No.** One product boundary plus a one-minute test job |
| 12 | Were interruption recovery, idempotency and resumability tested? | **Yes.** Injected failure rolled back completely and the retry applied exactly 1,000 with no duplication; duplicate and older slots no-opped; batches resumed from a forward-only cursor |
| 13 | Was a backup restored successfully? | **No.** No export was taken and no restore was drilled. The free plan provides no automatic backup |
| 14 | What capacity measurements were obtained? | 1,000-nation slot in 47.2–59.1 ms of database time; 250-nation batch in 15.5–25.2 ms; **291 bytes per nation-turn**; ≈3.5 MB/day at 1,000 nations |
| 15 | Is ₹0 supported? | **Supported at prototype/small-playtest scale, conditional beyond it** — see §17 |
| 16 | Which tests passed, failed, skipped or were blocked? | Passed: 11/11 unit, 23/23 local D1 integration, 4 migrations, 9 engine tests, 7 access-control tests, 6 site checks, both validators. **Not exercised:** true concurrency, backup/restore, Supabase Auth, 24-hour run, quota exhaustion. **Blocked:** Cloudflare billing read (403), GitHub write (no repository for this project), static-assets upload (connector cannot send the upload header) |
| 17 | Updated gate statuses? | **GATE-13 CONDITIONAL, GATE-16 CONDITIONAL, GATE-18 CONDITIONAL** |
| 18 | Does Stage 1 meet its documented criteria? | **No.** 17 pass / 3 conditional / 0 fail |
| 19 | What remains for the owner? | OD-02 (scope), a capacity target, OD-06 (backup tier/process), OD-07 (e-mail), and a decision about the pre-existing `public` schema and the RLS-disabled `app_meta` |
| 20 | Exact next task? | See §20 |

---

## 20. Next task

**Observe twelve consecutive product boundaries** on the Supabase job now running, and record the results. It is the single cheapest item that moves GATE-16 and GATE-18: the scheduler is deployed, the heartbeat table records every firing, and the only missing input is a day of elapsed time. Read it with:

```sql
select slot, fired_at from feasibility.cron_heartbeat
 where job = 'resolve_current_turn' order by id desc limit 20;
select * from cron.job_run_details order by start_time desc limit 20;
```

Do **not** start the Game Design Bible or a production schema on the strength of this report. The turn engine is proven at one boundary, the backup path is unbuilt, and the capacity target is still the owner's to set.
