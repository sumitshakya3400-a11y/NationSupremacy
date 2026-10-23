# Stage 2 handoff — Nation Supremacy

**Created:** 2026-10-23
**Status:** Stage 1 **closed** ([Report 13](../stage-1/13_stage_1_final_closure_and_stage_2_handoff.md)); Stage 2 authorized to begin.
**Audience:** the AI or engineer picking up the next task. Read this file, then the linked sources — not a new audit.

---

## 1. Objective

Turn the approved Stage 1 design into a production-grade data model and server-side authority design for the first playable scope, then implement it in bounded increments.

Stage 2 is **not** "build the game". It is the step that makes the game buildable without re-deciding fundamentals.

## 2. Where the project actually is

| Thing | State |
|---|---|
| Design | Complete for Stages 1's purpose: concept, pillars, 18 systems, economy, security registers (reports 01–09) |
| Architecture | Chosen and recorded: Cloudflare Pages (frontend) + Supabase (PostgreSQL, Auth, RLS, `pg_cron`) — D-008, D-009, D-010 |
| Public site | `https://nation-supremacy.pages.dev` — feasibility preview only, no gameplay |
| Backend | Supabase project **Nation Supremacy** `lqdzchtfxrbtwsrpkrzo`, `ap-south-1`, free tier |
| Prototype schema | `feasibility` schema: 6 tables, 5 functions, RLS proved, 1 `pg_cron` job (`0 */2 * * *`) |
| Old resources | Preview Worker and `NATIONSPHERE` project **deleted** (owner-confirmed) |
| Game code | **None.** Nothing in the repository is the game |

## 3. Roadmap context (do not invent a new one)

[Report 09 §19.2](../stage-1/09_integrated_design_synthesis_and_readiness_audit.md) defines the workstreams. Stage 2's own two workstreams are already delivered:

- **2A — decision closure and Stage 1 close-out:** delivered by Report 13 and D-011.
- **2B — free-tier measurement spike:** delivered by Reports 11 and 12 (1,000 nations, 35.5 ms/slot, 264 B/nation-turn, scheduler firings).

The next workstream is **roadmap Stage 3 — architecture and schema** (TQ-01…TQ-17, SDQ-003/018). That is what "Stage 2 development" means here.

## 4. Approved architecture (do not re-litigate)

- **Frontend:** static site on Cloudflare Pages. Preferred production path is static assets; today's deployment is a Pages Advanced Mode function because the connector cannot set the asset-upload `Authorization` header (Report 12 §2.1). No client-side game authority.
- **Backend:** Supabase PostgreSQL. All value changes are server-side; the browser may read what RLS allows and call server-side functions, never write authoritative balances.
- **Auth:** Supabase Auth. RLS policies key on the JWT `sub`. The prototype proves the mechanism with `request.jwt.claims`, not a real session (CF-04).
- **Scheduler:** Supabase Cron (`pg_cron`), one authoritative turn job per even UTC hour. **Cloudflare Cron must not run a competing turn scheduler** (D-008).
- **Turn model:** `floor(epoch/7200)` slot; `turn_runs.slot` primary key; `(slot, nation_id)` primary key on `turn_applied`; per-nation batch in one transaction; forward-only cursor. These four mechanisms are the tested exactly-once design — preserve them in the production schema.
- **Cost posture:** free-first. No mandatory paid service; no custom domain assumed; no provider upgrade without an owner decision.

## 5. Source files to preserve (do not rewrite or extend blindly)

| Path | Why it matters |
|---|---|
| `prototypes/supabase-feasibility/migrations/0001…0004` | The tested schema, functions, grants/RLS and schedule. The production schema should start from these, not from scratch |
| `prototypes/supabase-feasibility/site/index.html` | The live preview page; byte-identical to what is deployed |
| `prototypes/supabase-feasibility/scripts/build-pages-worker.mjs` | Build guard (brand, codename, credential checks) and the Pages deploy artifact |
| `prototypes/supabase-feasibility/results/nation-supremacy-project.json` | Measured evidence from the current project |
| `prototypes/free-tier-feasibility/` | Historical D1 comparison (11/11 unit, 23/23 integration recorded). **Do not extend it** |
| `docs/qa_backups/09_validate.py`, `validate_final.py` | Document/continuity validators. They assert the current closed state and the historical record |

## 6. Out of scope for Stage 2

- Full game implementation (economy, nation management, politics, markets, diplomacy, alliances, warfare).
- Any change to D-004 (Operations Points remain **Provisional**).
- A new Supabase organization (not required) or a paid plan.
- A custom domain, public launch, or marketing.
- Re-running Stage 1 audits, or reopening closed gates without new evidence.
- Production load testing at unapproved scale.

## 7. Carry-forward backlog (from Report 13 §7)

| ID | Item | Phase | Acceptance criterion |
|---|---|---|---|
| CF-01 | Capacity target and quota validation | Stage 3 → pre-launch | Owner-approved nation cap; measured rows/turn, storage/day, slot duration at that size with headroom; recorded as a decision |
| CF-02 | Backup and restore drill | Stage 3 design, Stage 8 execution | Export stored off-project; restore into scratch DB reproduces counts; RTO/RPO documented; no paid feature |
| CF-03 | Twelve consecutive boundaries | Stage 3 (elapsed time) | 12 consecutive even-hour successes in `cron.job_run_details` + one heartbeat per slot; no duplicate application |
| CF-04 | Supabase Auth end-to-end | Stage 3 | Real sign-up/in/out; two accounts isolated; no service key in client |
| CF-05 | OD-02 scope decision | **First task** | Decision entry selecting CP/FPB taxonomy and FPB scope; DEF-001/002 resolved |
| CF-06 | True concurrency test | Stage 8 | Two simultaneous resolvers; exactly one applies; no double application |
| CF-07 | Billing-scope read and quota alarms | Stage 3 | Free tier confirmed by an authorised read; alarms for DB size and function usage |
| CF-08 | Recovery, e-mail, moderation runbooks | Stage 8 | Written procedures with owner steps and no paid dependency |
| CF-09 | V-2/CV-002 validation sessions | Stage 6 | Sessions recorded; nothing fabricated before then |

## 8. Required tests for the first increment

The first increment must be verifiable without a playable game:

1. Every migration applies cleanly to an **empty scratch database** and re-applies without error (idempotence).
2. Slot arithmetic reproduces `248992` for `2026-10-23T08:00:00Z` and `248993` for `10:00:00Z`.
3. The exactly-once keys exist and are exercised: duplicate slot → `noop`; duplicate nation-turn → 0 rows.
4. An injected failure mid-batch leaves zero partial rows (rollback).
5. RLS matrix: for each protected table, a signed-in player can read only permitted rows and cannot write authoritative values; a second account sees zero foreign rows; `anon` is denied.
6. No secret in the client bundle or the repository.

## 9. Recommended first task

**Resolve OD-02, then design the production schema for that scope.**

Deliverable: a short design record under `docs/stage-2/` containing the scope decision, the production table list with keys and ownership columns, the RLS/authority matrix per table, the turn-phase ordering (SDQ-018) and the migration plan from `feasibility`. No production migration is applied to the live project in this increment.

Suggested prompt title: **"Stage 2, Increment 1 — scope decision and production schema design"**.

## 10. House rules for the next session

1. Read this file, [Report 13](../stage-1/13_stage_1_final_closure_and_stage_2_handoff.md), [AI_CONTEXT](../AI_CONTEXT.md), [AI_HANDOFF](../AI_HANDOFF.md), [DECISIONS](../DECISIONS.md). Do not re-run the Stage 1 audit.
2. Explicit owner authorization is still required per task (D-002). Do not widen a task's scope on your own.
3. Verify against the live services before claiming a deployment or a deletion.
4. Never commit credentials; never print them in reports.
5. Do not mark a test passed because it passed earlier — rerun what is cheap and relevant, and say what was not run.
6. Keep the public page honest: it is a feasibility preview until gameplay exists.
