# Report 10 — Stage 1 gate evidence and free-tier feasibility plan

**Version:** 1.0
**Date:** 2026-10-23
**Status:** Plan, with the executed measurements recorded separately in [11_free_tier_feasibility_results.md](11_free_tier_feasibility_results.md).
**Scope:** GATE-13, GATE-16 and GATE-18 only. This report does not approve an architecture, a schema, a game mechanic, or Stage 1 completion.

---

## 0. Why this report exists

Prompt 9 closed with **17 gates passing, 3 conditional, 0 failing** and an explicit refusal to call Stage 1 complete. The three conditional gates were not documentation defects; each was waiting on a different kind of evidence:

- GATE-13 waits on an **owner decision** and on **human validation sessions**.
- GATE-16 waits on **runtime/component measurements**.
- GATE-18 waits on **capacity measurements** and a **provider-account review**.

This report does three things: it records the exact gate text from the saved report, separates what evidence already exists from what is missing, and defines the smallest test that could produce each missing item. Report 11 records what was actually executed and what remained blocked. Where the two disagree, Report 11 wins — it is the measurement record.

---

## 1. Starting state inspected

### 1.1 Project root and version

| Item | Actual value |
|---|---|
| Project root | `C:\Users\suren\Downloads\Project X` |
| Version marker | Byte-identical to `Project X step 9 correction.zip` (38 zip entries compared by SHA-256, **0 mismatches**) |
| Stage 1 reports present | 9 (`01`…`09`), 2,087 lines of audit in Report 9 alone |
| Continuity files | `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `DECISIONS.md` |
| Validators present | `qa_backups/09_validate.py`, `qa_backups/validate_final.py`, `qa_backups/09_register_counts.py` (counter only) |
| Existing code | **None.** The project was documentation-only before this pass |
| Version control at start | **None** — `git rev-parse` returned "not a git repository" |

The archive check matters: the brief said to use `Project X step 9 correction.zip` if available and not to pretend otherwise. It was available, and the working tree matched it exactly before any edit in this pass. Everything after this point is therefore a delta from the verified Prompt 9 correction state.

### 1.2 Files read for this report

Read in full or in the windows where the gate definitions live:

- `09_integrated_design_synthesis_and_readiness_audit.md` — §1.3–1.6 (findings, zero-cost conclusion, next steps), §2.1–2.4 (reading depth, inventory, defect policy), §13.2–13.4 (validation register, PV-01…PV-15, what needs players), §15.1–15.6 (owner decisions and blocking questions), §16 (requirements traceability), §17.3–17.11 (limits, workload scenarios, component matrix, scenario verdicts), §20.1–20.4 (gate criteria, results, tally, what would flip).
- `07_economy_design_and_market_structure.md` — §16.3–16.4 and §22 (write model used by DEF-006), §24–27 (gates, sources, QA record).
- `08_security_privacy_fair_play_and_trust.md` — SEC-018…021/031 (turn integrity, audit spine), §13/§14 (audit and backup requirements), ST-007…009, OSQ-003/007.
- `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `DECISIONS.md` — current status and the decision register.
- Both validators, to know what they assert before changing anything.

### 1.3 Gate provenance — read this before quoting a gate

Prompt 9 §20.1 states plainly: **no standalone Stage 1 acceptance-criteria document exists**, and the 20 gates are *proposed* criteria written to be falsifiable, not owner-approved policy. That still governs. This report therefore treats a gate as authoritative *as the project's current working criterion* while keeping its provenance visible. Changing a gate's wording to make it pass is forbidden; so is silently replacing it with an easier criterion.

### 1.4 Baseline checks run before any edit

| Check | Command | Result |
|---|---|---|
| Documentation validator (legacy role) | `python qa_backups/validate_final.py` (from `docs/`) | **ALL CHECKS PASSED**, exit 0 |
| Documentation validator (current) | `python qa_backups/09_validate.py` | **68/68 checks passed**, exit 0 |

Both are document-consistency checks. They say nothing about runtime behaviour, capacity, security or cost, and this report does not treat them as such.

### 1.5 Connected services — what was actually available

| Service | Available actions (verified) | Not available | Consequence |
|---|---|---|---|
| **Cloudflare** | Account read; Worker list; D1 list/create/query; Worker upload; schedule read/write; docs search | **Billing/subscription read** — `GET /accounts/{id}/subscriptions` → HTTP 403, "no OAuth scope covers this endpoint" | Components can be tested for real; the *plan tier* cannot be confirmed from inside this environment |
| **GitHub** | Repository search, commit/issue/PR reads (read-only, public search) | Create repository, push, read private repo, write files, CI control | No Project X repository was found; remote version control is an **owner action** |
| **Supabase** | Project list, SQL, migrations, Edge Function deploy, logs | — (project creation needs cost confirmation) | One existing project was found, **INACTIVE** (paused); no new project was created |

**Existing Cloudflare resources were left untouched.** The account contains one Worker from an earlier unrelated effort, `nationsphere-api` (created 2026-09-17, fetch handler, no cron schedules). It was read to confirm it exists and was not modified, redeployed or deleted. The account had **zero D1 databases** before this pass.

**Existing Supabase resource:** one project, `NATIONSPHERE` (region `ap-southeast-2`), status **`INACTIVE`**, created 2026-09-17. It is paused. It was read only for status and was not resumed, queried, migrated or otherwise changed. Its paused state is itself evidence for the architecture comparison in §6.

---

## 2. The three gates, exactly as recorded

Quoted from `09_integrated_design_synthesis_and_readiness_audit.md` §20.2 (columns: requirement, evidence, result, severity, remaining action, blocks Stage 1 / implementation / ₹0):

| ID | Gate requirement | Recorded evidence | Result | Severity | Remaining action | Blocks Stage 1 | Blocks impl. | Blocks ₹0 |
|---|---|---|---|---|---|---|---|---|
| **GATE-13** | *The next workstream can proceed without undocumented assumptions* | DEF-003 (validation gates bypassed); DEF-001/002 (scope); numbers absent | **Conditional** | High | Record accepted assumptions; decide OD-02; run V-2/CV before design freeze | Yes | Yes | No |
| **GATE-16** | *Every essential component has a plausible free-tier path or an explicit blocker* | §17.10: 5 verified, 3 likely, 5 conditional, 1 not required; 0 incompatible for the FPB | **Conditional** | High | Measure cron/D1/auth (PV-01…07, PV-15); decide OD-01/06 | Yes | Yes | Yes |
| **GATE-18** | *The ₹0 claim is not based on unverified capacity or a hidden paid dependency* | Capacity unmeasured; no hidden paid dependency found; R2 optional | **Conditional** | High | Execute PV-01…07; PV-09 | Yes | Yes | Yes |

Prompt 9 §20.4 defines what would flip each one:

| Gate | To pass | Evidence needed |
|---|---|---|
| GATE-13 | Record the bypassed validation as accepted assumptions and fix scope | OD-02 recorded; V-2/CV-002 scheduled |
| GATE-16 | Show each component fits or has a blocker | PV-01…07, PV-15; R2/domain decision |
| GATE-18 | Replace capacity assumptions with measurements | PV-02/04/05/06 actuals |

### 2.1 What the gate names in the brief do and do not mean

The brief calls them "validation evidence", "free-tier component fit" and "capacity evidence". Those are fair paraphrases, but the recorded text is narrower and more specific, and it is the recorded text that governs:

- GATE-13 is **not** "run every validation test". It is "the next workstream can proceed without *undocumented* assumptions" — an assumption can be recorded and accepted instead of resolved, which is why the remaining action says "record accepted assumptions".
- GATE-16 is **not** "everything is measured". It accepts "a plausible free-tier path **or an explicit blocker**". A component with an honest blocker can still satisfy the gate; a component with an optimistic guess cannot.
- GATE-18 **is** measurement-bound: it asks whether the ₹0 claim rests on unverified capacity, so prose cannot close it.

---

## 3. Gate evidence matrix

Legend for the "missing evidence" type: **D** documentary, **T** automated-test evidence, **R** deployed-runtime evidence, **M** measured capacity, **O** owner decision, **H** human testers.

| # | Gate | Why conditional today | Evidence that already exists | Missing evidence (type) | Smallest reliable procedure | Access needed | Status |
|---|---|---|---|---|---|---|---|
| 1 | GATE-13 | Three separate gaps: DEF-003's bypassed gates are accepted by the auditor but not by the owner; DEF-001/002 leave two incompatible "first playable" definitions; economy numerics are deliberately absent | P9 §2.3 records the audit-level acceptance; V-1…V-10 and CV-001…006 are designed; CP/FPB taxonomy exists in P5 §11; OD-02 options costed | Owner's acceptance of the DEF-003 assumptions (**O**, **D**); OD-02 chosen (**O**); V-2 session test and CV-002 comprehension test executed (**H**, **T**) | (a) publish a consolidated assumptions register with IDs and consequences; (b) owner answers OD-02; (c) run V-2 on a paper/mock session and CV-002 on a clickable mock | Owner; 4–6 testers; no paid service | **CONDITIONAL** |
| 2 | GATE-16 | 5 of 14 components were judged only "likely" or "conditional"; 0 were incompatible, but none of the likely/conditional ones had runtime evidence | §17.10 component matrix; §17.3 limits with access dates; D1 and Workers limits re-read 2026-10-23; page/TLS and source-control verdicts | Measured cron CPU/subrequests (ZD-04, **M**, **R**); measured D1 write/storage behaviour (ZD-03, **M**, **R**); auth KDF CPU (ZD-05, **M**); decisions OD-01/06 for e-mail and backups (**O**) | A deployed Worker with a cron trigger, a real D1 database and a synthetic batch job; a local KDF benchmark in the same runtime | Free Cloudflare account (available); no e-mail provider without owner choice | **CONDITIONAL** |
| 3 | GATE-18 | The ₹0 claim was built on the S0–S3 workload model, and every number in it was an assumption; no turn had ever been resolved | §17.4 scenarios and assumptions; §17.5 storage arithmetic; DEF-006's corrected write range; no hidden paid dependency found | Rows read/written per nation-turn (PV-04, **M**); bytes appended per nation-day (PV-05, **M**); invocation duration/CPU at N=50/250/1000 (PV-02, **M**, **R**); quota-exhaustion behaviour (PV-07, **T**); free-plan audit including payment method (PV-09, **O**, **D**) | Deploy the spike with its real D1 binding, seed synthetic nations, run turns, read `meta.rows_written`/`rows_read`/`size_after` and recorded durations | Free Cloudflare account; billing endpoint needs a scope the connector lacks | **CONDITIONAL** |

### 3.1 Existing acceptance criteria, quoted from where they already exist

These are not invented for this report; each is already a requirement with an ID in Report 9 §12–13 or Report 8:

| Criterion | ID | Text (abridged) | Applies to |
|---|---|---|---|
| 12 turns/day at fixed UTC boundaries, no live resolution | REQ-015 | "The world must resolve 12 turns/day at fixed UTC boundaries" — test: 24h run → 12 completed turn records | GATE-16/18 |
| Exactly-once, forward-only resolution | REQ-016 | Duplicate and abort injection → no double-apply, resume completes | GATE-16/18 |
| Free scheduler CPU/subrequest fit | REQ-035 | "Twelve scheduled turns/day must run within the free scheduler's CPU/subrequest limits" | GATE-16/18 |
| Free database size and write fit, or redesigned retention | REQ-034 | "Load model → size and writes measured" | GATE-16/18 |
| No automatic charges or paid plan | REQ-036 | "Provider config review → no payment method, no overage" | GATE-18 |
| Free static host with public URL and TLS | REQ-032 | "Deploy → HTTPS page loads without a paid plan" | GATE-16 |
| Free execution tier with server authority | REQ-033 | "Deploy → API responds within free limits" | GATE-16 |
| E-mail within free caps or explicitly waived | REQ-039 | "Signup → verification or documented waiver; recovery works" | GATE-16 |
| Machine-checkable proof for PV tests | PV-01…PV-15 | Each has a "PASS looks like" column in P9 §13.3 | GATE-18 |

### 3.2 Acceptance criteria that do **not** exist yet

This is a finding, not a gap to paper over:

1. **No approved population target.** The S0–S3 table is explicitly "all assumptions, none measured". There is no owner statement that "Project X must support N active nations on the free tier". Without it, a measurement can show *what a load costs* but cannot show *whether the load is the required one*. Proposed for owner review: use the already-written test sizes (50 / 250 / 1,000 nations) as exploratory measurement points and treat S1 (25–100) and S2 (300) as the scenario the ₹0 claim must survive. **Not approved here.**
2. **No gate-level threshold for "plausible".** GATE-16 allows "plausible free-tier path"; plausibility is unquantified. Working interpretation used in Report 11: a component is *verified* when its documented limit is compared with a measured usage for the claimed scenario; *likely* when the limit is documented and the usage is estimated; *conditional* when neither is measured.
3. **No definition of the retention window's storage budget.** §17.5 recommends 90 days hot + export, but SDQ-003 is still open, so PV-05 can measure growth but cannot pass "retention is designed".
4. **No quota-exhaustion product behaviour.** OD-01 is open, so PV-07 can observe that writes fail safely but cannot pass "players see the approved degraded state".

### 3.3 Dependencies, cost and security implications

| Item | Cost | Security / integrity implication |
|---|---|---|
| Deployed spike Worker + D1 database | ₹0 under Workers Free and D1 Free (100k req/day, 10 ms CPU, 500 MB/db, 100k writes/day) | Public endpoint; must not hold real data or credentials; delete after measurement |
| Cron trigger | Included; 5 per account on Free | The schedule *is* the game clock; a silent miss is a fairness incident, so the test must prove miss-detection, not just success |
| Synthetic dataset | Negligible (1,000 rows ≈ 1 MB) | Synthetic only — no player data exists, and none may be invented |
| Billing verification | Free | Blocked by connector scope; cannot be asserted from inside |
| Supabase comparison | ₹0 to evaluate; a new project would be a persistent resource | Free plan has **no automatic backups** and pauses after 1 week idle — both are integrity risks, not just conveniences |

No paid plan, add-on, R2 bucket, custom domain or payment method was enabled, and none is required by the plan in this report.

---

## 4. Plan, mapped to the project's own test IDs

The project already named the tests; this plan does not invent new identifiers for the same work. Only the execution path is new.

| Test | Existing "PASS looks like" | What this pass will actually do | What it will not claim |
|---|---|---|---|
| PV-01 (12 turns/day) | 12 turn records in 24h, no missed boundary | Local slot-math unit tests for a full 24h and a live cron firing observed at one UTC boundary | A 24-hour observation |
| PV-02 (boundary scaling) | Completes within CPU/subrequest limits; record actuals | Record wall clock, statement count, rows read/written at N = 50 / 250 / 1,000 on the deployed Worker | That N=1,000 proves production scale |
| PV-03 (duplicate/abort/delay) | Duplicate no-ops; forward-only resume | Inject duplicate invocation, mid-batch failure and a late slot | A real network partition or a real Cloudflare incident |
| PV-04 (write budget) | Within 100k/day or documented overflow | Sum `meta.rows_written` per nation-turn including index and audit rows | That the audit-heavy production schema has the same row count |
| PV-05 (storage growth) | Under 500 MB with retention; export restores | Measure bytes/nation/day from `size_after`; report days-to-cap | That export/retention is designed (SDQ-003 open) |
| PV-06 (request ceiling) | Within 100k requests/day | Arithmetic on the S0–S3 model against the measured requests/invocation | A traffic test |
| PV-07 (quota exhaustion) | Writes fail safely; no corruption; honest error | Inject a storage-full-style failure and assert no partial apply | That the real daily cap was hit |
| PV-09 (free-only audit) | No paid plan, no charge trigger, HTTPS works | Inspect available account resources; verify no paid feature is used; record the billing-scope blocker | That the account's plan tier was verified |
| PV-15 (auth KDF) | Chosen KDF fits free limits without weakening policy | Benchmark PBKDF2 in the same runtime; leave Argon2id unmeasured unless a dependency is justified | That Argon2id fits |

### 4.1 Architecture comparison, decided on documentation first

The brief asks for Cloudflare + D1, Cloudflare + Supabase, and "another configuration only if materially better". A three-way empirical bake-off would be larger than the evidence needs, so the comparison is documentary where the facts are decisive and empirical only where they are not.

Decisive documentary facts (all verified 2026-10-23):

| Question | Cloudflare Workers + D1 | Cloudflare Workers + Supabase |
|---|---|---|
| Monthly cost at the claimed scenario | ₹0 (Free plan) | ₹0 (Free plan) |
| Database included | 500 MB/database, 5 GB/account, 10 databases | 500 MB/project, 2 active projects |
| Read/write quota | 5M rows read/day, 100k rows written/day | Unlimited API requests (compute-bound) |
| Backups on free | **7-day Time Travel** | **None** (no automatic backups, no PITR) |
| Idle behaviour | Always available | **Paused after 1 week of inactivity** |
| Connection model from a Worker | Binding; no pooler, no connection limit | Pooler/Hyperdrive needed; latency hop |
| Scheduled turns | Native cron on UTC, 5 schedules | `pg_cron` (works, but jobs run inside Postgres) |
| Operational surface | One platform, one deploy | Two platforms, two dashboards, two failure domains |

The two facts that decide the *first* candidate are the backup and pause behaviours: **SEC-030 requires a restorable backup**, and a world that pauses after a quiet week is a 12-turns-per-day game that has stopped. D1's free plan provides 7-day point-in-time recovery; Supabase's free plan provides none. Supabase's strengths — real Postgres, mature SQL, auth/storage/realtime, better relational modelling — do not offset a missing recovery path for a game whose audit trail is the product.

**Plan:** test Cloudflare + D1 only. Keep Supabase as the documented exit/fallback target (REQ-037) and revisit if the project ever needs Postgres-specific capability. No Supabase project is created: the two-project free cap, the 500 MB limit, the pause behaviour and the missing backups mean a test project would add a persistent resource without changing the recommendation.

---

## 5. What would change a gate's status

| Gate | Would PASS if | Would FAIL if | Would stay CONDITIONAL if |
|---|---|---|---|
| GATE-13 | OD-02 is recorded in `DECISIONS.md`; the DEF-003 assumptions are accepted by the owner in writing; V-2 and CV-002 are scheduled with named testers | The owner rejects the CP/FPB taxonomy and no replacement scope exists | Any of the three is missing — including "scheduled" with no date |
| GATE-16 | Each of ZD-02…ZD-08 is either measured against its documented limit at the claimed scenario or has an explicit blocker recorded | A component cannot serve the claimed scenario at ₹0 and no blocker is acceptable | Measurements improve some components but e-mail/backups/auth remain undecided or unmeasured |
| GATE-18 | PV-02/04/05/06 produce actuals that fit the free limits at the claimed scenario, and PV-09 confirms no paid trigger | Measured writes/storage/CPU exceed the free caps at the claimed scenario | Measurements exist for a small N only, or the plan tier cannot be verified |

A documentation change alone can only move GATE-13, and only in its "record the assumptions" part. GATE-16 and GATE-18 are measurement gates; no amount of writing closes them.

---

## 6. Next action

1. Execute the prototype plan in §4 and record actuals in Report 11 (the gate statuses in Report 11 supersede the ones here).
2. Ask the owner for OD-02 (scope) and for acceptance or rejection of the DEF-003 assumptions; those are the only two items that can move GATE-13.
3. Ask the owner whether to run V-2/CV-002 with 4–6 testers, and whether to approve the exploratory measurement sizes in §3.2 as the capacity target.
4. Do not select an architecture, design a production schema, or start Stage 2 on the strength of this plan.

---

## 7. Execution outcome (added 2026-10-23 after the measurements)

The plan above was executed in the same pass. The measurement record is [Report 11](11_free_tier_feasibility_results.md); where the two differ, Report 11 wins.

| Gate | Status after execution | What changed | What did not |
|---|---|---|---|
| GATE-13 | **CONDITIONAL** | The undocumented assumptions are now written down, and one of them (that a single invocation can resolve any world size) was replaced by a measurement. The architecture question is answered on evidence. | OD-02 is still undecided, the DEF-003 condition is not owner-accepted, and V-2/CV-002 have not run. |
| GATE-16 | **CONDITIONAL** | Workers execution, D1 persistence, HTTPS delivery, the 12/day slot model and the spike's own cron handler are now measured rather than inferred; a real free-tier deployment exists. | No live Cron Trigger was observed; e-mail/backups/auth remain owner-blocked or unmeasured; at ~1,000 nations one invocation exceeds the 10 ms CPU budget. |
| GATE-18 | **CONDITIONAL** | Rows written/read per nation-turn are measured (6.01), giving a ~1,386-nation write ceiling, and per-invocation CPU is measured at 50/100/250/1,000 nations. | No 24-hour/12-turn run, no real quota exhaustion, no billing-scope verification, and no owner-approved capacity target. |

**No gate was promoted.** The evidence moved several components from "likely" to "measured", and it produced one new negative finding (CPU at 1,000 nations), but each gate still has at least one unmet recorded criterion. Stage 1 remains **incomplete — conditionally ready**.
