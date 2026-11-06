# Final decision-closure audit — Stage 2

**Version:** 1.2 · **Date:** 2026-10-23 (v1.1 adds D-030 and reconciles the registers; v1.2 micro-correction — 8 prompt-owned rows marked Deferred, 5 remain Open, and the Supabase export commands corrected against the official CLI workflow) · **Stage:** 2 (Master Game Design Bible) · **Status:** Audit record — **not** Bible part B-03.
**Purpose:** inventory every decision and unresolved question in the project, resolve what the available evidence supports, separate genuine uncertainty from scheduled work, and establish whether Prompt 03 may proceed.
**This file does not occupy the Bible document slot.** Prompt 03's deliverable was planned as `08_nation_creation_and_progression.md` (B-03); this audit took the `08` filename, so the deliverable was written on 2026-10-24 as [09_account_onboarding_nation_creation_and_progression.md](09_account_onboarding_nation_creation_and_progression.md). This audit cleared the ground for it.

**Report map (audit brief A–H):** A = §1 · B = §2 · C = §3 · D = §4–§5 · E = §6 · F = §7 · G = §8 · H = §11. The final-report items 1–10 requested by the brief are covered by §1–§12 and are summarised in the session reply.

---

## 1. Audit scope and method

### 1.1 Documents read in full

| Group | Files |
|---|---|
| Continuity | [AI_CONTEXT](../AI_CONTEXT.md), [AI_HANDOFF](../AI_HANDOFF.md), [PROJECT_PROGRESS](../PROJECT_PROGRESS.md), [DECISIONS](../DECISIONS.md), [ROADMAP](../ROADMAP.md), [AUTONOMOUS_DECISION_POLICY](../AUTONOMOUS_DECISION_POLICY.md) |
| Stage 2 frame | [00 handoff](00_stage_2_handoff.md), [01 prompt register](01_stage_2_prompt_roadmap.md), [02 Bible outline](02_master_game_design_bible_outline.md), [03 requirements](03_requirements_traceability.md), [04 design decisions](04_approved_and_provisional_decisions.md), [05 unresolved register](05_unresolved_design_decisions.md), [06 progress log](06_stage_2_progress_log.md), [07 B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) |
| Stage 1 evidence | Reports 01–13, in particular 03 (FO register), 04 (F-012/FO-018), 06 (§15G action models), 07 (§10.2/§12.5/§14.1), 08 (OSQ/SEC/ST), 09 (§11.1, §12), 11 (measured bytes), 13 (closure and CF-01…CF-09) |
| Tooling | `docs/qa_backups/09_validate.py`, `validate_final.py`, `test_next_action.py`, `test_decision_registers.py`, `status_rules.py` |
| Repository | `git status`, the `prototypes/` tree, and every file path referenced by the changed documents |

### 1.2 Method

1. Read the actual files, not the prompt's summary of them.
2. Build the inventory from the files themselves (`grep`/`awk` counts, not prose claims).
3. Classify each open item by what it actually needs: design decision, technical-design decision, empirical validation, future-stage deliverable, external permission, accepted risk, or duplicate.
4. Resolve every Category A/B item that the current evidence supports; record a `D-` entry and propagate it.
5. Leave an item open only with a precise question, a reason, and a named next test or owner.
6. Add validator coverage for each failure class the audit found; do not weaken existing checks.
7. Re-run every available check and record the actual output.

### 1.3 What this audit is not

- It is **not** Prompt 03 and does not write B-03.
- It is **not** an implementation, migration, deployment or hosting change.
- It does **not** claim any backup, restore, scheduler, concurrency, capacity or authentication test was executed.
- It does **not** reopen a settled decision without a conflict, a safety issue or new evidence.

---

## 2. Complete inventory (verified from the files)

| Register | Range | Total | Status breakdown |
|---|---|---|---|
| Project decisions — `DECISIONS.md` | D-001…D-030 | **30** | 27 **Confirmed**, 1 **Provisional** (D-006), 2 **Superseded** (D-004→D-015, D-005→D-008) |
| Design positions — `04` | DD-001…DD-048 | **48** | 22 **Approved**, 24 **Provisional**, 1 **Superseded** (DD-019→DD-033), 1 **Deferred** (DD-007) |
| Unresolved questions — `05` | UD-001…UD-030 | **30** | 17 **Resolved**, 8 **Deferred to a named future prompt**, 5 **Open**; class over the 13 non-resolved rows: **A = 0**, **B = 5**, **C = 3**, **D = 3**, **E = 2** |
| Requirements — `03` | REQ-001…REQ-060 | **60** | 12 **Approved**, 41 **Provisional**, 5 **Open**, 2 **Deferred**; **0 executed validations** |
| Carry-forward backlog | CF-01…CF-09 | **9** | 0 closed by this audit; each has a named official stage and acceptance criterion |
| Stage 2 prompts | 01…15 | **15** | 2 complete (01–02), 1 next (03), 12 pending (04–15) |

**Checked for duplication and renumbering:** every D, DD, UD and REQ ID is unique and contiguous in its own family; no ID was deleted, reused or renumbered in this audit. The two superseded decisions keep their original text and point to their successors.

**Historical counts are not current counts.** §5.1 of the progress log records the Prompt 01 state (47 requirements, 32 DD positions, 3 class-A UDs) and §5.1c the post-Prompt-02 state. Those snapshots are correct for their dates; §5.1d records the current state.

---

## 3. Decisions resolved in this audit

Seven decisions were made. Each is a normal Category A/B choice under [the policy](../AUTONOMOUS_DECISION_POLICY.md) — no owner approval was required or invented.

### 3.1 Summary

| ID | Question | Previous status | Final status | Deciding entry |
|---|---|---|---|---|
| D-024 | Is there a shared action budget beyond Operations Points? | D-004 superseded, but the non-military half was only a provisional B-02 rule | **Confirmed** | D-024 |
| D-025 | Recovery tier, RPO/RTO, and the player-facing treatment of a FAILED turn | UD-016 mixed "Open"/"partly resolved"; UD-028 Open | **Confirmed** (policy); drill **Awaiting validation** (CF-02) | D-025; resolves UD-016, UD-028 |
| D-026 | How long history is retained, and what the storage budget is | UD-004 "partially resolved" | **Confirmed** (policy); sizes **Provisional** | D-026; resolves UD-004 |
| D-027 | Minimum group size for a published aggregate | UD-027 Open | **Confirmed** | D-027; resolves UD-027 |
| D-028 | Inactivity threshold, protection, removal and reactivation | UD-025 Open; assigned to Prompt 03 | **Confirmed** (policy); threshold **Provisional** | D-028; resolves UD-025 |
| D-029 | Is e-mail verified at launch, and how? | UD-015 Open | **Confirmed** (policy); provider **Deferred** to Stage 6 | D-029; resolves UD-015 |
| D-030 | Are pending diplomatic acts visible to the counterparty before resolution? | UD-029 Open | **Confirmed** (design) | D-030; resolves UD-029 |

### 3.2 D-024 — no shared action budget

**Decision.** Military orders use Operations Points (D-015). Every other subsystem limits its actions with its own declared, player-visible constraints: resource cost plus reservation, a per-turn action cap, offer/treaty slots, cooldowns or prerequisite gates. Each subsystem must state those limits in the B-02 §24 contract; an action with no declared limit is a specification defect. No general-purpose action currency may be added without superseding D-024.

**Why.** D-004 asked whether the game should use a shared budget, separate subsystem budgets, or action-specific costs. D-015 settled the military case only. A shared pool would couple unrelated systems (a trade offer competing with a construction order) and reward hoarding; per-domain limits keep each subsystem legible and are already B-02 TR-005's posture. No numeric cap is invented here — Prompt 04/10/14 own the numbers.

**Affected:** [DECISIONS D-024](../DECISIONS.md), [04 DD-042](04_approved_and_provisional_decisions.md), [B-02 §4/§19/§24](07_core_gameplay_loop_symbolic_world_and_turn_system.md), [03 §3.4](03_requirements_traceability.md). Requirements: REQ-001, REQ-014.

### 3.3 D-025 — recovery, backup and failed-turn policy

**Decision, in three layers.**

1. **Turn recovery.** Forward-only resume from phase checkpoints for the same slot, idempotent per `(slot, nation)`. Retries never publish twice or re-apply an effect.
2. **Failed turn.** After a bounded retry budget the turn becomes `FAILED` and the world waits — it does not skip the slot. Players see a **delay**; accepted actions stay pending and are never silently dropped, and no cost is charged unless the turn completes. If it later completes, the normal digest appears with its completion time. If the operator cannot recover it, the incident is disclosed, and only an operator decision recorded in the incident log may **void** the turn: reservations are released, no cost is charged, and the digest states that the turn did not resolve. A **disaster restore** that loses turns is a declared outage: unreconstructable slots are not replayed, the gap is disclosed, and the world resumes at the next boundary — the only exception to the no-skip rule, and never silent.
3. **Data recovery.** Supabase Free has **no provider-managed backups and no PITR**. The owner runs **three separate logical exports at least daily**: custom roles (`supabase db dump --role-only -f roles.sql`), schema (the default dump, `-f schema.sql`) and data (`--data-only --use-copy -f data.sql`). The CLI reference states the **default dump contains no data and no custom roles**, so one default invocation is not a full backup. Exports are encrypted and stored off-platform. Migrations remain the schema source; migration history (`supabase_migrations`) is exported separately if it is to be preserved; Storage objects and custom `auth`/`storage` changes are exported separately; custom LOGIN role passwords are not in the dump and must be handled out of band. Keep **7 daily exports plus 3 monthly archives**. Targets: **RPO ≤24 h, RTO ≤24 h best-effort**, disclosed as project targets, not provider guarantees. A **quarterly restore drill** into a scratch free project (Free allows 2 active projects) must reproduce row counts and the audit ledger. It is **CF-02**, owner-assisted.

**Why.** Supabase's official documentation states that automatic backups and PITR are not included on Free, recommends self-managed `db dump` exports, and makes daily backups (7 days) and PITR paid features on Pro and above. Its official CLI restore workflow runs **three commands** — `--role-only`, the default schema dump, and `--data-only` — and the CLI reference says the default dump excludes data and custom roles. A single `db dump` must therefore not be described as capturing all three. No provider RPO/RTO is documented. B-02 TR-077…083 already fixed forward recovery; the missing pieces were the player-facing `FAILED` treatment and the data-loss tier. The synthetic prototype demonstrated rollback once, at one boundary; that is feasibility evidence, not a drill.

**What is not claimed.** No backup has been taken under this policy, no restore has been performed, and no RPO/RTO has been measured. CF-02 remains unexecuted. **A public launch with real accounts is gated on CF-02 passing.**

**Affected:** [DECISIONS D-025](../DECISIONS.md), [04 DD-043](04_approved_and_provisional_decisions.md), [B-02 TR-080](07_core_gameplay_loop_symbolic_world_and_turn_system.md), [05 UD-016/UD-028](05_unresolved_design_decisions.md), [03 REQ-028/REQ-059](03_requirements_traceability.md), [00 §8 CF-02](00_stage_2_handoff.md).

### 3.4 D-026 — history retention

**Decision.** Class-S digests are hot for **30 days**, then compact to **one monthly summary per nation** kept **12 months**, then deleted. Class-P records are **permanent**. Class-O moderation/abuse records keep a **12-month floor** unless an open case requires longer; Prompt 12 sets the operational value. The **permanent audit spine** required by REQ-027 (value mutations, pipeline phases, privileged acts) is **not** subject to that floor. Compaction is an idempotent daily maintenance job, not a turn phase, never deletes class P, and is itself recorded. Retention is a maximum, disclosed to players. If Stage 3 measures more than **350 MB at 1,000 nations**, the hot window drops to 14 days and summaries to 6 months before launch.

**Arithmetic.** At the measured 264–291 B/nation-turn, 12 turns/day for 30 days is **95–105 MB per 1,000 nations**. A 10% monthly-compaction assumption adds roughly 11–21 MB per month of summaries — about 130–250 MB over 12 months. That fits the 500 MB free database at 1,000 nations but not comfortably at 2,000, where D-022's cap/pause posture applies. **The 10% ratio is an assumption, not a measurement.**

**Affected:** [DECISIONS D-026](../DECISIONS.md), [04 DD-044](04_approved_and_provisional_decisions.md), [B-02 TR-092](07_core_gameplay_loop_symbolic_world_and_turn_system.md), [05 UD-004](05_unresolved_design_decisions.md), [03 REQ-024/034/058](03_requirements_traceability.md).

### 3.5 D-027 — aggregate disclosure threshold

**Decision.** A published aggregate over a group requires **at least 5 contributing members (k = 5)**. A smaller group is merged into a stable "other" group only when the merged group is still ≥5; otherwise the value is withheld or coarsened. **Complementary suppression** applies: if a total plus all but one component would reveal that component, at least one further component is suppressed too. No differencing across turns or related tables may recover a suppressed component. The rule applies to alliance, market, ranking-group and world statistics; an individual nation's public ranking is not an aggregate. k = 5 is a design constant, not a legal-compliance claim.

**Why.** B-02 TR-022 required non-leakage but named no number. k = 5 is the smallest common small-cell threshold, simple to apply and audit. A threshold alone leaks by subtraction, hence complementary suppression. UD-017 (jurisdiction) remains a separate legal question.

**Affected:** [DECISIONS D-027](../DECISIONS.md), [04 DD-045](04_approved_and_provisional_decisions.md), [B-02 TR-022](07_core_gameplay_loop_symbolic_world_and_turn_system.md), [05 UD-027](05_unresolved_design_decisions.md), [03 REQ-057](03_requirements_traceability.md).

### 3.6 D-028 — dormancy, protection and abandonment

**Decision.** A nation becomes **dormant after 14 consecutive days (168 turns) without an authenticated session**. While dormant it cannot be targeted by new offensive actions and cannot initiate them; it stays in the world and keeps alliance membership; it is excluded from public rankings and published aggregates; it suffers no resource decay or additional absence penalty, and its queued/recurring effects continue under the normal economy rules. The first authenticated session ends dormancy; protection from attack lasts until the **first boundary after that session** (at most 2 hours) and is not extended by further logins without play. No nation is deleted at 14 days. After **12 consecutive months dormant** it is **archived** — removed from the world graph and rankings, data retained, with a notice to its verified e-mail 30 days beforehand; a login within 12 months of archival restores it. Deletion occurs only on the owner's request or under a separately disclosed policy in Prompt 12.

**Why.** This follows DP-002 (no presence requirement, no absence punishment) while stopping ghost nations from absorbing wars indefinitely. 14 days spans a two-week holiday; 168 turns makes the boundary explicit. The one-boundary return grace is short enough that it cannot be farmed as permanent protection (F-017). Archival is reversible and avoids automatic data loss. **The 14-day threshold is Provisional**; the effects are Confirmed.

**Affected:** [DECISIONS D-028](../DECISIONS.md), [04 DD-046](04_approved_and_provisional_decisions.md), [B-02 TR-096](07_core_gameplay_loop_symbolic_world_and_turn_system.md), [05 UD-025](05_unresolved_design_decisions.md), [00 §10](00_stage_2_handoff.md), [03 REQ-022](03_requirements_traceability.md).

### 3.7 D-029 — e-mail verification at launch

**Decision.** Public launch requires a **verified e-mail before nation creation**. An unverified account cannot create or control a nation, trade, post or hold office; it may only complete the confirmation link or a password-reset flow. Supabase's default is that an unconfirmed user cannot sign in at all. Supabase Auth confirmation stays enabled. The **built-in Supabase e-mail service is development-only** — 2 messages/hour and recipients restricted to project team members — so public registration requires **custom SMTP**, which Supabase includes on the Free plan. Stage 6 selects a free-tier transactional provider and records it. If SMTP is not configured and tested, the project runs only as a **CP with pre-provisioned accounts** (D-020), not open registration. Recovery uses the verified e-mail plus a review path; no SMS or paid identity check. Verification does **not** prove one person = one account; D-018 enforcement stays behavioural.

**Why.** Supabase's docs state the built-in mail limit is 2/hour and not for production, custom SMTP is included on Free with a default 30/hour adjustable limit, and hosted projects require confirmation by default with unconfirmed users unable to sign in. Waiving verification would weaken recovery and anti-abuse with no saving. The policy is decidable now; the vendor is not.

**What is not claimed.** No SMTP provider has been selected, no sign-up/confirm/recovery flow has been tested, and no email has been sent. **CF-04 remains unexecuted.**

**Affected:** [DECISIONS D-029](../DECISIONS.md), [04 DD-047](04_approved_and_provisional_decisions.md), [05 UD-015](05_unresolved_design_decisions.md), [03 REQ-039](03_requirements_traceability.md), [00 §10](00_stage_2_handoff.md).

### 3.8 D-030 — pending diplomatic-act visibility

**Decision.** A pending diplomatic proposal (treaty offer, pact, or formal message requiring acceptance) is visible to its **named counterparty** as a **pending act** while it is open — acceptance requires seeing it. It is **not** visible to third parties until both parties declare it, it takes effect at a boundary, or a party publishes it. A rejection or withdrawal is private to the two parties unless the withdrawing/rejecting party publishes it. Declared acts (signature, war declaration, public posture) are public when declared. The terms of a pending act never enter a published aggregate (D-027).

**Why.** B-02 TR-020 already makes relations transparent and intent opaque. An offer cannot be accepted unseen, but publishing it to third parties would leak intent and bargaining position. D-017 sets the same parties-only posture for trade terms. The detailed exceptions — alliance-only offers, war declarations, public ultimatums — belong to Prompt 08.

**Affected:** [DECISIONS D-030](../DECISIONS.md), [04 DD-048](04_approved_and_provisional_decisions.md), [B-02 TR-020/TR-096](07_core_gameplay_loop_symbolic_world_and_turn_system.md), [05 UD-029](05_unresolved_design_decisions.md), [03 REQ-012/057](03_requirements_traceability.md). Requirements: REQ-012, REQ-057.

---

## 4. Every unresolved ID and its final status

### 4.1 Resolved (17)

| ID | Final status | Deciding entry | What was decided |
|---|---|---|---|
| UD-001 | Resolved | D-020 | CP and FPB are distinct scope terms; Stage 2 completion is neither |
| UD-002 | Resolved | D-016 | Trade offers do not reserve; reserve and settle atomically at acceptance |
| UD-003 | Resolved | B-02 §14 | Fixed P0–P7 phases, B0–B4 bands, published ordering key, seeded lottery |
| UD-004 | Resolved | D-026 | 30-day hot digests → 12 monthly summaries → delete; class-P permanent |
| UD-008 | Resolved | D-017 | Trade terms visible only to the parties; no public offer book |
| UD-014 | Resolved (policy) | D-018 | Multi-accounting prohibited; proportionate review-first enforcement |
| UD-015 | Resolved (policy) | D-029 | Verified e-mail before nation creation; custom SMTP mandatory at launch |
| UD-016 | Resolved (policy); drill open | D-025 | Forward recovery; daily three-part roles/schema/data `db dump`; RPO/RTO ≤24 h best-effort; quarterly CF-02 |
| UD-018 | Resolved (model) | D-015 | Single military-only Operations Points pool; values provisional |
| UD-019 | Resolved | D-023 | Warfare in scope for Prompt 10, excluded from the FPB |
| UD-020 | Resolved | D-021 | No newcomer catch-up acceleration at launch |
| UD-021 | Resolved (policy) | D-022 | Cap, degrade and pause signups at free-tier limits; no auto-upgrade |
| UD-025 | Resolved | D-028 | Dormancy at 14 days; protection; no decay; reversible archival |
| UD-027 | Resolved | D-027 | k = 5 aggregates with complementary suppression |
| UD-028 | Resolved | D-025 | FAILED turn delays the world; pending actions preserved; operator void only |
| UD-029 | Resolved | D-030 | Pending proposals visible to the counterparty only; third parties on declaration/effect/publication |
| UD-030 | Resolved | D-019 | Income before upkeep inside P3 |

### 4.2 Deferred to a future prompt (8)

These rows are **not resolved** and are **not generic open indecision**. Each has an owning subsystem prompt, and the remaining work is that prompt's rulebook.

| ID | Prompt | What remains |
|---|---|---|
| UD-009 | 06 | Domestic-policy axes and stability effects; the ≤2-axis bound is provisional |
| UD-010 | 05 | Sourcing competition inside the production/scarcity frame |
| UD-011 | 05 | Emphasis-change mechanics; immediate record + next-boundary effect is fixed |
| UD-012 | 09 | Alliance roles, pool draws and succession |
| UD-013 | 08 | Treaty effects beyond a NAP analogue |
| UD-022 | 13 | Notification/event-feed taxonomy |
| UD-023 | 13 | Network, market and war-board UI taxonomy |
| UD-024 | 11 | World-chronicle quality bar |

### 4.3 Genuinely open (5)

| ID | Class | Question | Why evidence is insufficient today | Next action |
|---|---|---|---|---|
| UD-005 | C | Treasury drain curves and austerity thresholds | Numeric; needs simulation | Prompt 04 formula; Prompt 14 simulation |
| UD-006 | C | Scarcity, respecialization and velocity-band numbers | Numeric; needs simulation | Prompt 04 formula; Prompt 14 simulation |
| UD-007 | C | Development-line thresholds | Numeric; needs simulation | Prompt 04 formula; Prompt 14 simulation |
| UD-017 | E | Which data-protection jurisdiction applies | **Category D — legal position the project cannot self-assign** | Owner before public launch; Prompt 12 states the posture |
| UD-026 | E | May the world be split into shards/multiple worlds? | Needs capacity evidence that does not exist | Prompt 15 scope; Stage 3 CF-01/CF-03 |

**No class-A item remains.** **17 Resolved + 8 Deferred + 5 Open = 30.** Deferred is not resolved: the owning prompt must still write the rule and record a `D-` entry.

---

## 5. Remaining provisional and open items

### 5.1 Design positions that remain Provisional (not blockers)

24 DD rows remain Provisional because they are Stage 1 design proposals that a later prompt must turn into an authoritative rule. They are not "undecided" in the sense of blocking work: each has a named owning prompt and a test. They become Approved only when their subsystem document is written and, where required, a `D-` entry records the position.

| DD | Position (short) | Why it is still Provisional | What settles it |
|---|---|---|---|
| DD-001 | CX-5 concept | Stage 1 recommendation; no approval entry | Prompt 15 consolidation, or a `D-` entry |
| DD-002 | Six pillars / eight anti-pillars | Same | Prompt 15; every prompt tests against them |
| DD-003 | SYS-001…018 catalog | Same | Prompts 02–13 as each system is written |
| DD-004 | One treasury, reservations, zero debt | Economy rule not yet written | Prompt 04 |
| DD-005 | Four material classes, two-use/two-route floor | Economy rule not yet written | Prompt 04/05 |
| DD-006 | Directed trades only at FPB | Trade rule not yet written | Prompt 07 |
| DD-008 | Paid, one-per-turn respecialization | Production rule not yet written | Prompt 05 |
| DD-009 | Stability as a floor, ≤2 policy axes | Politics rule not yet written | Prompt 06 (UD-009) |
| DD-010 | Three-class timing contract | Used by B-02; no approval entry | Prompt 15 |
| DD-011 | Server-authoritative security baseline | Design only; no implementation | Prompt 12; Stage 5/8 |
| DD-017 | Absence respected, re-entry summary | Used by B-02; presentation not written | Prompt 03/13 |
| DD-018 | Optional alliances, capped pool | Alliance rule not yet written | Prompt 09 (UD-012) |
| DD-021 | One shared world | Capacity evidence absent (UD-026) | Prompt 15; Stage 3 |
| DD-022 | Slot identity and epoch | B-02 rule; no approval entry | Prompt 15 |
| DD-023 | Boundary assignment, no grace | B-02 rule; no approval entry | Prompt 15 |
| DD-024 | Turn lifecycle and recovery states | B-02 rule; technical parts Deferred | Prompt 15; Stage 5/8 |
| DD-025 | P0–P7 phases | B-02 rule; subsystems must declare internal order | Prompts 04–11 |
| DD-026 | Deterministic ordering catalogue | B-02 rule; not simulated | Prompt 15; PV-02 |
| DD-027 | Reservation at acceptance | B-02 rule; numbers belong to Prompt 04 | Prompt 04 |
| DD-028 | Amend/cancel only while OPEN | B-02 rule; subsystems may add penalties | Prompts 04–10 |
| DD-029 | One outcome; forward recovery | B-02 rule; CF-02/CF-06 unexecuted | Prompt 12; Stage 8 |
| DD-030 | Digest-first history | B-02 rule; retention now D-026 | Prompt 11/12 |
| DD-031 | Visibility classes; transparent relations | B-02 rule; thresholds now D-027 | Prompts 07–13 |
| DD-032 | No presence requirement | B-02 rule; dormancy now D-028 | Prompts 03/12/13 |

These are **positions awaiting their own rulebook**, not unanswered questions. None blocks Prompt 03. **DD-007** (a listings market) is the only **Deferred** position: gates G-1…G-6 can activate it, and no prompt may assume it exists at first playable. **DD-019** is Superseded by DD-033 and kept as history.

### 5.2 Project decision that remains Provisional

**D-006** (the FO register is inputs-only) is Provisional by design: it governs how Stage 1 findings are treated, not a game rule. It does not block any prompt. It becomes moot only when every FO is either adopted or rejected in a later decision.

### 5.3 Empirical validation tasks — not design decisions

| ID | What must be proven | Current status | Where it closes |
|---|---|---|---|
| CF-01 | Capacity target and quota validation | **Not executed.** No owner-approved nation cap; measured only at 1,000 synthetic nations | Stage 3, before launch |
| CF-02 | Backup and restore drill | **Not executed.** D-025 fixes the policy; **no backup exists yet** | Stage 3 design, Stage 8+ execution |
| CF-03 | Twelve consecutive boundaries | **Not executed.** One product `pg_cron` firing at 10:00:00Z observed; no 12-boundary run | Stage 3 (elapsed time) |
| CF-04 | Supabase Auth end-to-end | **Not executed.** D-029 fixes the policy; no SMTP provider selected | Stage 6 |
| CF-05 | CP/FPB scope decision | **Not executed.** D-020 supplies the vocabulary; Stage 5 must set the FPB boundary | Stage 5, first task |
| CF-06 | True concurrency test | **Not executed.** Exactly-once demonstrated once, not under two simultaneous resolvers | Stage 8+ |
| CF-07 | Billing-scope read and quota alarms | **Not executed.** No authorised billing read | Stage 3 |
| CF-08 | Recovery, e-mail and moderation runbooks | **Not written.** D-025/D-029 define the policies the runbooks must implement | Stage 8+ |
| CF-09 | V-2/CV-002 validation sessions | **Not executed.** No players have been observed | Stage 8+ |

**None of these is marked passed.** A policy decision never proves the mechanism.

### 5.4 Genuinely unavailable evidence

- **Free-tier capacity at 2,000+ players** — the measured write/storage budget does not support a claim; D-022's cap/pause posture is the honest response (UD-026, CF-01).
- **The 10% compaction ratio** — assumed for the retention arithmetic; Stage 3 must measure it. If actual compaction is worse, the 350 MB trigger forces the shorter window.
- **Playtest evidence for the 14-day dormancy threshold** — none exists; the threshold is Provisional and revisitable.
- **Legal jurisdiction** — UD-017 is a Category D question; the project can state a privacy posture but cannot choose the applicable law.

---

## 6. Future-stage work, separated from decisions

| Prompt | Work that remains | Is it an unresolved decision? |
|---|---|---|
| **03** Account onboarding, nation creation, progression | Creation flow, starting state, progression milestones, re-entry presentation; applies D-028 and D-029 | **No.** Dormancy and verification are decided; the prompt writes the rulebook |
| 04 Economy | Deficit/austerity rule, all numeric values, visible action limits under D-024 | Formula shapes yes; exact numbers are class-C simulation |
| 05 Cities/production/research | Slots, prerequisites, modifiers, emphasis mechanics (UD-010/011) | Its own design content |
| 06 Politics | Policy axes, stability effects, cooldowns (UD-009) | Its own design content |
| 07 Trade | Offer expiry, atomic settlement, visibility implementation | D-016/D-017 already settle the policy |
| 08 Diplomacy | Treaty effects, breach, declaration timing (UD-013); pending-act visibility is settled by D-030 | Its own design content, except the visibility rule it implements |
| 09 Alliances | Governance, pool, succession, restricted Alliance management interface (not a war room; clarified 2026-11-04 by Prompt 10B-C3) (UD-012) | Its own design content |
| 10 Warfare | Order costs, protection states, settlement rules; OP numbers | D-015/D-023 settle scope and model; numbers are class-C |
| 11 World events | Event generation, objectives, rankings, chronicle quality (UD-024); applies D-027 | Its own design content |
| 12 Fair play | Detection, sanctions, appeals, deletion, recovery disclosure; implements D-018/D-025/D-026 | Mechanics, not policy |
| 13 Interface | Screen inventory, navigation, journeys, notification/UI taxonomies (UD-022/023) | Its own design content |
| 14 Numbers/balance | Every value, rounding, caps, simulations | Class-C evidence work |
| 15 Assembly | Consistency review, completion decision, scope statement (UD-026) | Its own review work |

**Not a failure to decide:** a subsystem prompt writing its own rulebook is the plan, not indecision. The register's §6 classifies each active UD accordingly.

---

## 7. Contradictions corrected

| # | Where | Contradiction | Correction |
|---|---|---|---|
| 1 | AI_CONTEXT §7 | "FO-018 (catch-up) stays owner-held" while D-021 had decided no acceleration | Replaced with the D-021 launch posture; FO-018 remains an input, not a live owner question |
| 2 | AI_HANDOFF §G item 18 | "the FO-018 catch-up decision itself remains owner-held" | Replaced with D-021; historical Prompt 3 status annotated |
| 3 | AI_HANDOFF §G item 21 | OSQ-003 e-mail and OSQ-007 recovery tier still listed as open | Updated: D-029 and D-025 decide the policy; the mechanisms remain Stage 6/CF-02 |
| 4 | `05` UD-016 row vs §6 | Row said "Open", §6 said "policy yes, proof no" | Row and §6 now both say **Resolved (policy); drill Awaiting validation (CF-02)** |
| 5 | `05` UD-015 evidence | Claimed a "free-tier send cap 100–300/day unmeasured" | Corrected to the documented 2/hour built-in limit, team-only recipients, and custom SMTP on Free |
| 6 | `06` §5.1 | "Register consistency (D-004 provisional)" read as current | Labelled as the Prompt 01 snapshot; D-015 superseded it later that day |
| 7 | `06` §5.1c | "Current register counts" frozen at 23/41/30 before this audit | Relabelled "at that point"; new §5.1d carries the current counts |
| 8 | `05` §4/§6 | Prompt 03 was told to decide UD-025; §6 still counted 20 active rows | D-028 decides it; §6 now separates 8 deferred rows from 5 open rows |
| 9 | `03` §3 | Counts 12/39/7/2 and "seven Open rows" | 12/41/5/2; §3.1 explains the moves and warns that Provisional ≠ verified |
| 10 | `04`/AI_CONTEXT/AI_HANDOFF/PROJECT_PROGRESS | Decision count 23 and DD 41 | Raised to the current 30 decisions and 48 design positions everywhere |
| 11 | `00` §10 | Prompt 03 "must decide UD-025" | Prompt 03 applies D-028; UD-025 is resolved |
| 12 | `07` TR-022/TR-080/TR-092/TR-096 | Aggregate threshold, retention and dormancy still described as open; Prompt 03 still asked to decide dormancy | Updated to D-027/D-025/D-026/D-028; no rule renumbered |
| 13 | `09_validate.py` docstring | Still said "DECISIONS D-001..D-023" and "D-004 still provisional" | Updated to D-029 and the supersession |
| 14 | `03` §3.2 | Implied REQ-024/028/039 all merely needed decisions | REQ-028/039 are policy-decided but unverified; REQ-024 stays Open for deletion design |
| 15 | `07` §29 / `05` UD-029 | Pending diplomatic visibility was still listed as open for Prompt 08 | D-030 decides it; TR-020 and TR-096 record the rule |
| 16 | `00`, `05` §6, `06` §5, PROJECT_PROGRESS, B-02 reference block | The D-030 pass left six/29/47/16/14 and D-024…D-029 wording in current text | Reconciled to seven decisions D-024…D-030, 30 D, 48 DD, 17 resolved / 8 deferred / 5 open everywhere |
| 17 | `AI_CONTEXT` row 07 / validator assertions | B-02 still described as v1.4 and the register guards still expected 29/47 and D-001..029 | Updated to v1.5, D-001…D-030, DD-001…DD-048 and 315 validator checks |

---

## 8. Accepted risks

| Risk | Why it is accepted now | Condition that would force a change |
|---|---|---|
| **R-1 — No backup or restore drill yet** | Free plan has no managed backup; the project is still pre-launch and synthetic | CF-02 must pass before any public launch with real accounts; a failed drill blocks launch |
| **R-2 — RPO up to 24 h** | Daily exports are the only ₹0 option; more frequent exports would increase owner burden without a provider guarantee | If real players join, revisit export frequency or accept the disclosed loss window explicitly |
| **R-3 — Free projects pause after 7 days of low database activity** | Production traffic should prevent it; a total outage could trigger it | A pause during an outage is an incident; resume within the documented one-year window, never treat pause as a backup |
| **R-4 — Free plan allows 2 active projects** | The drill needs a scratch project; deletion is owner-performed | If both slots are occupied, the drill cannot run until one is freed; that blocks CF-02 |
| **R-5 — 10% compaction ratio is assumed** | No measured summary size exists | Stage 3 measurement; if >350 MB at 1,000 nations, apply the 14-day/6-month fallback |
| **R-6 — k = 5 is a design floor, not legal compliance** | UD-017 jurisdiction is unknown | A legal review may raise k or add suppression rules; that supersedes D-027, not silently changes it |
| **R-7 — 14-day dormancy is untested** | It balances holiday absence against ghost nations; playtest evidence is absent | Playtest showing either ghost-farming or holiday punishment; D-028 is revised with evidence |
| **R-8 — SMTP provider not selected** | Provider choice needs an external account (owner-assisted) and belongs to Stage 6 | No provider means CP-only launch, not open registration; a free-tier change may force a different provider |
| **R-9 — No provider RPO/RTO** | Supabase publishes no guarantee; the project's targets are its own | Any paid tier or provider change would require a new decision; do not import a provider SLA claim into the docs |
| **R-10 — Capacity above 1,000 nations unsupported** | Measured evidence stops there; D-022 caps/pauses rather than promising | CF-01/CF-03 measurement; a capacity target is an owner decision |

---

## 9. Research record

Two external questions were researched; no other claim in this audit depends on an unverified external fact.

### 9.1 Supabase backup and disaster recovery

| Item | Finding |
|---|---|
| Free plan backups | **Not included.** Pricing marks automatic backups and PITR "Not included in free" |
| Pro / Team / Enterprise | Daily backups: Pro 7 days, Team 14 days, Enterprise up to 30 days (pricing says "Custom" for Enterprise) |
| PITR | Paid add-on on Pro+; pricing lists ~$100/month per 7 days; requires at least a Small compute add-on; enabling it stops daily backups |
| Self-managed path | Supabase recommends `supabase db dump` for Free projects. The official CLI workflow exports **roles (`--role-only`), schema (default) and data (`--data-only`) separately**, then restores with `psql`. The CLI reference states the **default dump has no data and no custom roles**. Migration history needs its own `--schema supabase_migrations` export; Storage objects and custom `auth`/`storage` schema changes are separate; custom LOGIN role passwords are not included. |
| Caveats | Dumps exclude Storage objects; custom `auth`/`storage` changes need separate handling; custom LOGIN role passwords are not stored; raw `pg_dump` can include Supabase internals |
| Free project limits | 2 active projects per organization (paused projects do not count); low database activity for 7 days can pause a Free project; paused projects can be restored for up to one year |
| RPO/RTO | **No official numeric RPO/RTO guarantee.** Docs warn daily backups can lose a day; PITR granularity is not a guaranteed RPO |

Sources: [Database Backups](https://supabase.com/docs/guides/platform/backups) · [Backup and Restore using the CLI](https://supabase.com/docs/guides/platform/migrating-within-supabase/backup-restore) · [CLI Reference](https://supabase.com/docs/reference/cli/introduction) · [Pricing](https://supabase.com/pricing) · [Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq) · [Project Pausing](https://supabase.com/docs/guides/platform/free-project-pausing) · [PITR usage](https://supabase.com/docs/guides/platform/manage-your-usage/point-in-time-recovery).

### 9.2 Supabase Auth e-mail verification

| Item | Finding |
|---|---|
| Built-in e-mail limit | **2 messages/hour per project**; recipients restricted to project team members; not for production, no delivery SLA, limits can change |
| Custom SMTP | Included on Free; default **30 messages/hour**, adjustable; Supabase recommends it for production |
| Confirmation default | Hosted projects require e-mail confirmation by default; unconfirmed users cannot sign in; it can be disabled but the production checklist recommends keeping it |
| Exceeded limit | Auth returns 429; the docs do not state whether an unconfirmed signup row is rolled back |
| Auth MAU | Free includes 50,000 MAU; total users unlimited |

Sources: [Auth Rate Limits](https://supabase.com/docs/guides/auth/rate-limits) · [Custom SMTP](https://supabase.com/docs/guides/auth/auth-smtp) · [Password-based Auth](https://supabase.com/docs/guides/auth/passwords) · [Production Checklist](https://supabase.com/docs/guides/deployment/going-into-prod) · [Pricing](https://supabase.com/pricing).

### 9.3 Research limitations

- The provider pages are live and undated; the figures are those displayed on 2026-10-23. Supabase states the built-in mail limit can change without notice.
- No vendor was selected for SMTP, so no provider-specific free-tier limit is asserted.
- FO-018/D-021 was **not** re-researched: the Stage 1 reports already contain the genre evidence, and the decision is a launch posture, not a factual claim.
- No load, backup, scheduler, concurrency or auth test was run in this audit.

---

## 10. Validation record

The exact commands and results are recorded after the final run. This section must never claim a check that was not executed.

| Check | Actual result |
|---|---|
| `python docs/qa_backups/09_validate.py` | **335/335 checks passed — ALL CHECKS PASSED**, exit 0 |
| `python docs/qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED**, exit 0 |
| `python docs/qa_backups/test_next_action.py` | **Ran 10 tests — OK** |
| `python docs/qa_backups/test_decision_registers.py` | **Ran 12 tests — OK** (ranges, deferred/open taxonomy, section-6 match, backup wording, next prompt) |
| Register counts and ID uniqueness | **PASS** — D-001…D-030 (30), DD-001…DD-048 (48), UD-001…UD-030 (30: 17 resolved, 8 deferred, 5 open), REQ-001…REQ-060 (60: 12/41/5/2); no gap or duplicate |
| Local link resolution | **556 relative links checked across `docs/*.md`, `stage-1/*.md` and `stage-2/*.md` — 0 broken** |
| Cross-document next action | **PASS** — the STATUS blocks, AI_CONTEXT index, AI_HANDOFF §H, Stage 2 handoff §10 and progress-log header all name Prompt 03; the stale-next-action scan finds no current sentence pointing at Prompt 01/02 |
| Negative tests of the new checks | **11 of 11 detected, every file hash restored, validators re-passed:** D-004 reverted to Provisional; UD-016 and UD-009 set Open; FO-018 described as owner-held; CF-02 claimed executed; AI_CONTEXT totals reverted to DD-047; D-030 set Provisional; duplicate D-030 row; Stage 2 handoff range ended at D-029; DD-043 reverted to a single dump; D-025's default-dump omission removed |
| Validator robustness fix | The 09 validator crashed on a failure message containing `₹` under the Windows legacy console encoding; `sys.stdout.reconfigure(encoding="utf-8")` was added to both validators so a failure prints instead of aborting |
| Not run | No game test (none exists), **no backup or restore drill**, no SMTP/auth test, no scheduler, concurrency or load test, no deployment |

### 10.1 Regression coverage for the failure classes in the audit brief

| # | Failure class | Check that now catches it |
|---|---|---|
| 1 | A decision resolved in one place but Open elsewhere | Each resolved UD must be absent from §6's non-resolved inventory; deferred rows must name their prompt; UD-016 must contain both `Resolved` and `CF-02` |
| 2 | A launch decision contradicted by current context/handoff text | The exact "FO-018 owner-held" sentences are forbidden in the three continuity files; D-021 must exist |
| 3 | UD-016 conflicting statuses | Row must say `Resolved (policy)` and name CF-02; §6 must not list it |
| 4 | D-004 inconsistent across registers | DECISIONS and the design register must both say `Superseded by D-015`; no current file may say D-004 is provisional |
| 5 | A handoff naming an older prompt as next | `test_next_action.py` plus the next-action scan over AI_CONTEXT, AI_HANDOFF, PROJECT_PROGRESS, `00` §10 and `06`'s header |
| 6 | Stale totals or a completed spec described as unwritten | AI_CONTEXT's index rows must carry `DD-001…DD-048`, `D-001…D-030`, the 12/41/5/2 counts and `97 rules`/`v1.5` |
| 7 | Historical snapshots mistaken for current instructions | Report 9 keeps its pre-closure verdict and "Historical snapshot" label; `06` labels the Prompt 01/02 counts as historical |
| 8 | Duplicated or renumbered IDs | Contiguity checks over D-001…030, DD-001…048, UD-001…030 and REQ-001…060; the duplicate-D-030 negative test |
| 9 | A fixed-architecture document naming another provider | AI_CONTEXT, AI_HANDOFF, `00` and B-02 must name Cloudflare and Supabase and must not name Vercel, Netlify or Firebase |
| 10 | A future test reported complete because its design was decided | CF-02 and CF-04 may not be described as successfully executed; the audit must state that no backup was taken and no SMTP provider was selected |
| 11 | A default database dump described as a complete backup | D-025, DD-043 and this audit must name `--role-only` and `--data-only`, record the default dump's missing data/custom roles, and contain no single-command claim; both validators and `test_decision_registers.py` enforce it |

---

## 11. Readiness

**Internal consistency.** After the corrections in §7, the decision log, both Stage 2 registers, the requirements tracker, B-02, the continuity files and the Stage 2 handoff agree on every count and status this audit touched. The remaining Provisional and Open items are classified and owned.

**Can Prompt 03 proceed without routine design approvals?** **Yes** — the final validation run passes (335/335, cross-file pass, 12+10 tests, 11/11 mutations). Prompt 03 inherits:

- one account ↔ one nation (REQ-002/043; D-018 policy);
- identity persistence through absence (B-02 §22);
- the decided dormancy policy (D-028) — it **applies**, and no longer decides, UD-025;
- the verified-e-mail gate (D-029) — it writes the flow; Stage 6 configures SMTP;
- the pending-diplomacy visibility rule (D-030) — Prompt 08 implements it;
- the no-presence rule and the digest/re-entry hooks;
- the starting-resource reservation model (B-02 §19).

**What Prompt 03 must not do:** re-decide UD-025 or UD-015, invent economy numbers, change the cadence or the mapless world, write code, migrate, deploy, or claim a backup/auth test passed.

**No Prompt 03 deliverable exists yet.** `08_nation_creation_and_progression.md` was not created by this audit.

> **Dated note (2026-10-24, after this audit).** Prompt 03 has since been written as [09_account_onboarding_nation_creation_and_progression.md](09_account_onboarding_nation_creation_and_progression.md) — the original `08_…` slot is this audit record. The sentence above is this audit's own 2026-10-23 snapshot and is kept unchanged; it is **not** a current-state statement. The audit's 30-decision / 48-position / 30-UD / 60-REQ counts are likewise its snapshot; the current registers are 42 / 60 / 33 / 97.

---

## 12. Scope confirmation

- **Application code:** none added or changed.
- **Database:** no migration, schema, data, RLS policy or credential change.
- **Deployment/hosting:** none. Cloudflare Pages and Supabase remain the fixed architecture; no provider was replaced.
- **Cost:** no paid dependency, plan or purchase. The only new external facts are free-tier limits.
- **Implementation claims:** none. CF-01…CF-09 remain unexecuted; D-025/D-029 are policy decisions, not proof.
- **Files changed:** documentation under `docs/` only, plus the document-QA validators.
