# B-10 — Warfare, Campaigns, Military Operations and Postwar Settlements

**Version:** 1.3 · **Created:** 2026-11-03 · **Stage 2, Prompt 10B** · **Revised:** 2026-11-04 (v1.2 Prompt 10B-C2 corrects the final semantic defects in place and adds no numbered rule: `WAR-053l` protects civilian Food from `OP-09` and `WAR-053m` defines the single canonical P3.7 force snapshot, replacing the undefined P3.0; `WAR-009g` preserves validly accepted defensive commitments across `TRANSITION`/`CRISIS` while keeping every other check; `WAR-109f`–`WAR-109m` move impairment to an infrastructure-only carrying-value basis with exact P4.1/P5/next-turn boundaries, B-05 `URB-043`/`URB-044` repair cost with no materials, and B-06 `DMP-031` crowding instead of "paused growth"; `B10-C17`, `B10-C21`, `B10-C30` and `WAR-166` are corrected. The v1.1 text follows for history: v1.1 Prompt 10B-C adds military Food upkeep at P3.7 rank 6(a) (`WAR-053a`–`WAR-053k`, `WAR-064a`/`WAR-064b`, `F-WR-036`), city-targeted `OP-05 MISSILE_STRIKE` infrastructure damage and repair (`WAR-109a`–`WAR-109l`, `F-WR-037`/`F-WR-038`), the twelve-check fail-closed hostile validator (`WAR-009a`–`WAR-009f`), the political `TRANSITION`/`CRISIS` implementing rule (`WAR-053j`/`WAR-053k`), execution-time protection state (`WAR-116a`), one capped combined supply modifier (`WAR-071a`, `F-WR-039`) and honest espionage ownership (§13.3, `B10-AD-24`, `B10-C30`, `WQN-19`: no owner identified); the OP pool becomes a turn-scoped derived ledger refilled at the authorized P7 close with reservation at acceptance (`WAR-005a`, `WAR-043a`/`WAR-043b`). No numbered rule is renumbered, removed or reopened. · v1.3 Prompt 10B-C3 reconciles Operations Points with the authoritative B-02 lifecycle: the pool is persistent rather than turn-scoped, regenerates by one OP at the opening of P3.7 inside the existing recurring phase (not at P7 and not at P0), carries below the cap, and records one idempotent `REGENERATED` item per nation per turn. `WAR-039`–`WAR-043b`, `F-WR-001`/`F-WR-002`, `REQ-654`/`REQ-681`, `B10-C03`, `WQN-01`, `WQN-04` and `WCR-10` are corrected; no operation cost, cap value, battle rule or prior 10B/10B-C/10B-C2 correction changes.) · **Status:** **Specification complete at the documentation level.** No gameplay code, migration, deployment, runtime test, load test, security test, browser test or live-game integration test exists. Every number introduced by B-10 is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** unless it is an inherited approved value. B-10 is a rulebook, not a research report; the evidence base is [the 10A research report](research/10A_politics_and_war_warfare_research.md).

**Authority chain.** [DECISIONS.md](../DECISIONS.md) remains the only place an owner approval is recorded. This rulebook records the working AI's ordinary design decisions under [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (D-014) as `B10-AD-01`…`B10-AD-25`, mirrored as **DD-166…DD-190** in the [Stage 2 decision register](04_approved_and_provisional_decisions.md). None of them is an owner approval. No decision ID was added to, removed from or altered in `DECISIONS.md` by Prompt 10B.

**Companions.** [Formula register](17_warfare_formula_register.md) (authoritative for every calculation) · [requirements traceability](03_requirements_traceability.md) · [unresolved decisions](05_unresolved_design_decisions.md) · [progress log §58](06_stage_2_progress_log.md).

---

## 1. Executive summary

B-10 defines a **layered, mapless warfare system**: a sovereign nation declares war on another sovereign nation; the declaration creates exactly one **campaign**; the campaign carries a closed set of **objectives** and a closed catalogue of **operations**; operations consume the nation's single **Operations Points** pool (D-015) and existing B-04 resources; battles resolve deterministically with one bounded, seeded fortune roll; the campaign ends by objective completion, expiry, mutual peace, surrender or negotiated settlement; and the aftermath is recorded permanently without transferring cities or minting value.

The system has seven defining properties.

1. **Mapless.** No map, province, tile, front, coordinate, distance, adjacency, border, movement, territorial capture, occupation or geographic supply. A "blockade" is a symbolic national state with no sea zone. A "named city" may be an **asset target** for `OP-05`, but it is never a place: no map, coordinate, adjacency or movement is created.
2. **National sovereignty.** Only a nation's authenticated owner may declare, operate, surrender or settle. An Alliance has no military authority, no shared OP, no command channel and no automatic war entry. D-137, D-140 and D-141 boundaries are preserved exactly.
3. **One action economy.** All military actions draw on one national OP pool, which regenerates by one OP at the opening of P3.7 at each successful boundary, carries below its cap, is reserved while the turn is OPEN, and is consumed at resolution. There is no per-war pool, no per-campaign pool and no shared pool.
4. **Resource-backed and conservative.** Operations reserve and consume existing B-04 inventory. B-10 creates no resource and no loot; losses are military strength points and readiness, plus a **bounded, recoverable reduction of city infrastructure**, all B-10 state.
5. **Bounded.** A campaign has a hard deadline, an inactivity expiry and forced-loss caps. No war can run forever and no single battle can annihilate a nation.
6. **Readable.** The attacker sees an odds band before commitment, the defender sees a threat band, and both receive a complete battle report and a stated reason for every block or failure.
7. **Auditable and fail-closed.** Every hostile path calls one cumulative server-side validator at submission, at P2 and immediately before P5 execution. A blocked action moves nothing. B-09 blocks emit the mandatory `AUD-AL-017` event.

The system is **not implemented**. It is designed so that Prompt 10C can write workflows, edge cases and acceptance tests from it, and Prompt 14 can calibrate its provisional numbers, without inventing architecture.

---

## 2. Purpose, scope and non-goals

### 2.1 Purpose

B-10 exists so that two nations can fight a bounded, understandable and strategically meaningful conflict inside a mapless symbolic world, with meaningful readiness, force and supply decisions, real counterplay, enforceable endings and permanent records.

### 2.2 In scope

| Area | B-10 owns |
|---|---|
| Declaration | Eligibility, cumulative validation, cost, slots, rejection |
| Campaign | State machine, objectives, duration, expiry, inactivity, dormancy interaction, reroll interaction |
| Forces | Unit categories, strength points, caps, recruitment, upkeep, replacement |
| Readiness | National readiness value, gates, upkeep, recovery, penalties |
| Operations | Closed catalogue, prerequisites, costs, effects, counters, limits |
| Supply | Resource bundles, reservation, consumption, denial, shortage behaviour |
| Battle | Strength, counters, seeded fortune, tiers, losses, reports |
| Settlement | Ceasefire, surrender, negotiated terms, enforcement, reparations |
| Postwar | Exclusion cooldown, recovery, history, re-entry |
| Governance | Visibility, permissions, audit, failure codes, abuse taxonomy handoff |

### 2.3 Out of scope and non-goals

- No geography of any kind. 10A's mapless suitability analysis (§19) is binding. A city is a B-05 asset identifier, not a location; targeting one creates no map, coordinate, distance, border, front or movement.
- No city capture, city deletion or city ownership transfer; no facility damage or facility destruction. **City infrastructure damage is the single adopted exception**, bounded by `WAR-109a`–`WAR-109m` and `URB-157`.
- No direct population casualties, eviction or transfer from any operation.
- No nuclear weapons, no radiation mechanic, no uranium consumption.
- No espionage or covert-operation system.
- No Alliance military coordination, command, delegation, shared OP or military treasury.
- No loot, no forced wealth seizure, no debt, no negative balance, no future-income garnishment.
- No real-time combat, no tactical grid, no unit-by-unit positioning.
- No implementation, migration, deployment, release or production change.
- No calibrated numeric balance; Prompt 14 owns every calibration.

---

## 3. Authority and binding decisions

### 3.1 Inherited decisions preserved unchanged

| Decision | What B-10 must preserve |
|---|---|
| **D-014** | Ordinary design decisions are made and recorded by the working AI; owner-reserved matters are not |
| **D-015** | One national OP pool, military-only, non-transferable, reserved at acceptance, consumed at resolution; no per-war/campaign/shared pool; no MAP import. **Amended 2026-11-04 (Prompt 10B-C3):** one OP regenerated at each boundary, cap-enforced, with carry below the cap (the original "refill to cap / unused points do not bank" rate is superseded; every other property is unchanged) |
| **D-019** | Income before obligations; obligations before discretionary spending |
| **D-023** | Warfare is designed in Prompt 10 and excluded from the First Playable Build |
| **D-024** | No shared action budget; each subsystem declares its own visible limits; OP is not a general currency |
| **D-027** | Aggregates publish only at k ≥ 5 with complementary suppression |
| **D-028** | Dormancy at 14 days/168 turns; no offensive targeting or initiation |
| **D-031** | Separate account, nation and pair statuses; no fourth status |
| **D-032** | One account, one active nation |
| **D-122** | Global Trade remains mandatory product scope and release-gated; B-10 does not alter it |
| **D-124** | Only the B-08 national agreements exist; no new national treaty effect |
| **D-137** | Zero diplomatic delegation; no Alliance authority over a member's diplomacy |
| **D-140** | Narrow Alliance capabilities only: separate treaty object, tax, donations, same-Alliance ban; no collective command |
| **D-141** | The Alliance Receiving Ledger is a receipt/accounting record with one purpose-limited operational debit; it is not a military treasury |
| **D-142 / DD-165** | Phase 09B is accepted at specification level only; acceptance implies no implementation |

### 3.2 Inherited subsystem rules B-10 implements

| Source | Rule | B-10 use |
|---|---|---|
| B-02 | `TR-040`–`TR-046`, `TR-050`–`TR-053`, `TR-057`–`TR-060`, `TR-073`–`TR-074`, `TR-090` | Phases, frozen baseline, deterministic order, reservations, retries, audit spine |
| B-03 | `ONB-019`/`ONB-020` (7 days/84 turns protection), `NET-025`/`NET-026` (restricted pairs), `RRL-013`/`RRL-021` (reroll block) | Protection, pair checks, reroll |
| B-04 | `ECN-023`–`ECN-026`, `ECN-105`/`ECN-106`, `ECN-147`, `ECN-152`, `ECN-165`, `ECN-212`, `ECN-214` | Resources, obligation order, ledger, transfers |
| B-05 | `URB-008`, `URB-111`, `URB-157`, closed 17-facility catalogue, five research branches | City permanence, damage boundary, no military buildings |
| B-06 | `DMP-265` | `TRANSITION`/`CRISIS` restrictions; no combat modifier |
| B-07 | `MKT-009`, `MKT-218` | Inventory is untouched by war; only a B-08 embargo restricts trade |
| B-08 | `DP-T01`, `DIP-125`, `DIP-141` | National NAP war-declaration block |
| B-09 | `ALL-206`–`ALL-215`, `AX-18`, `AX-30`, `AUD-AL-017`, `AT-E00`/`AT-E01` | Cumulative attack validation, audit, military sovereignty |

### 3.3 B-10's own design decisions

The 25 architecture decisions are recorded in [§26](#26-decision-and-conflict-resolution-register) as `B10-AD-01`…`B10-AD-25` and mirrored as **DD-166…DD-190**. They are **Provisional design positions** under D-014: settled enough for 10C and 14 to work from, never owner approvals.

### 3.4 Owner-reserved matters preserved

`UD-040`–`UD-049` remain exactly as recorded, including `UD-047`. B-10 resolves only **`UD-032`**, which the register already assigned to Prompt 10. B-10 creates no collective diplomacy, no delegation, no Alliance military role and no Alliance treasury right, and it spends no Alliance funds.

---

## 4. Warfare entities and terminology

### 4.1 Entities

| Entity | Identifier | Definition | Owner of mutation |
|---|---|---|---|
| War | `war_id` | The legal hostile relationship between exactly two nations, created by one resolved declaration | B-10 at P5 |
| Campaign | `campaign_id` | The single scored episode of a war: objectives, progress, operations, deadline | B-10 at P5/P6 |
| Objective | `objective_id` | One of six closed objective types, with a per-side progress counter 0…1000 | B-10 at P5 |
| Operation | `operation_id` | One accepted military order from one nation | B-10 at P5 |
| Battle | `battle_id` | One resolution of one offensive operation against one defending nation | B-10 at P5 |
| Force | `(nation_id, unit_type)` | An integer strength-point pool per unit type | B-10 at P3/P4/P5 |
| Readiness | `nation_id` | One integer 0…1000 | B-10 at P3/P5 |
| Settlement | `settlement_id` | A closed-term peace proposal and its lifecycle | B-10 at P4/P5 |
| Exclusion | `(nation_a, nation_b, until_turn)` | A B-10 postwar re-declaration block created only by a settlement term | B-10 at P5 |

A `WAR` has exactly one `CAMPAIGN`. A campaign has exactly one primary and one secondary objective, both public and immutable. A campaign may contain many operations and battles. **One campaign never contains more than one war**, and a nation cannot join another nation's war; a third party may only declare its own separate war.

### 4.2 Mapless terminology contract

B-10 uses only symbolic, national-level language. The following table is binding on every rule, screen, event and failure message.

| Forbidden term | Required B-10 term | Reason |
|---|---|---|
| Front, front line | *Campaign* or *active campaign* | No line exists |
| Province, tile, territory, region | *Nation* | No subdivision exists |
| Map, coordinate, distance, adjacency, border | *(nothing — no equivalent)* | Geography is excluded |
| Unit movement, deployment, garrison | *Force pool*, *stationed strength* (national only) | No location exists |
| Capture, occupation, annexation | *Objective progress*, *campaign outcome* | No territory changes hands |
| Sea zone, shipping lane, convoy, depot, supply route | *Blockade state*, *supply bundle* | Supply is inventory-based only |
| Airspace, naval theatre | *Air operation*, *naval operation* (domain labels only) | Domain labels grant no geography |
| Bombardment of a city | *National strike* | Cities are never targets |

A "blockade" is an abstract national condition: while it is active, the blockaded nation's operation resource bundles cost 25% more (rounded up) and its readiness recovers 25 points less per turn. It does not stop production, delete trade or create geography. It is breakable by `OP-08 BREAK_BLOCKADE` and expires automatically after 12 turns.

### 4.3 Display quantities

| Quantity | Visibility |
|---|---|
| Own force by type, readiness, OP, inventory | Exact, private to the owner |
| Opponent force and readiness | Band only: `LOW` / `MODERATE` / `HIGH` / `SEVERE`, derived by the threat-band formula |
| Declaration, campaign existence, objectives, deadline, outcome, settlement terms | Public |
| Operation identity and target | Actor and defender at P5; public summary after resolution |
| Unit-level losses | Parties exact; public summary band |
| Audit records | Actor, defender where applicable, and authorised administration only |

---

## 5. Declaration and eligibility

### 5.1 Who may declare

`WAR-001` Only the authenticated owner of an active nation may submit a declaration. No office, Alliance role, treaty, ballot, majority, AI or administrator may declare for that nation.

`WAR-002` The declarer must be: active, not dormant, not in `TRANSITION` or `CRISIS`, not already holding an outgoing campaign, and not party to a pending declaration of its own.

`WAR-003` The target must be: an existing active nation, not the declarer, not dormant, not under B-03 newcomer protection, not the declarer's restricted pair, not covered by an active `DP-T01` national NAP with the declarer, not sharing an active Alliance with the declarer, and not covered by an active `AT-E01` Alliance NAP with the declarer.

`WAR-004` A declaration is unilateral. Consent is not required. Every prohibition in `WAR-003` applies before acceptance and again at P2 and P5.

### 5.2 Declaration cost and slots

| Item | Value | Status |
|---|---|---|
| Declaration OP cost | 2 OP | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Declaration crown fee | 500 crowns | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Outgoing campaign slot | 1 | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Incoming campaign slot | 1 | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Maximum active campaigns per nation | 2 (one outgoing, one incoming) | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Declaration response window | none — unilateral | Structural |

`WAR-005` A declaration reserves 2 OP and 500 unreserved crowns at acceptance. Both are consumed at P5 when the declaration resolves. If the declaration fails at P2 or P5, both reservations are released and nothing is charged.

`WAR-005a` **Acceptance is a B-02 state, not a phase.** Acceptance is the `ACCEPTED` state entered while the turn is OPEN, before P1 freeze (`TR-057`–`TR-060`). P4 is not a general acceptance point. P4 resolves orders that were already accepted — recruitment and B-05 construction and repair — and P5 resolves military execution. An order described as "accepted at P4" is a phase defect; an action accepted after P1 is impossible. The acceptance transaction writes the OP `HELD` item and the economic `RESERVATION_HELD` items together, or writes neither.

`WAR-006` The declarer chooses the campaign's **primary objective** and **secondary objective** at submission from the closed catalogue in §7.1. The two must differ. The choice is immutable after acceptance and is published with the declaration.

`WAR-007` A nation already fighting may be declared on if its incoming slot is free. A nation cannot join an existing campaign; it may only open its own campaign against one of the belligerents. There is no alliance drag, no co-belligerent status and no call to arms.

`WAR-008` A pending declaration blocks the declarer's reroll and counts as an active campaign for slot purposes from acceptance until it resolves or fails.

### 5.3 The canonical hostile-action validator

`WAR-009` Every hostile path — screen, API, retry, replay, administrative correction, conditional defensive trigger, city-targeted strike, future client and future operation — calls **one server-side validator**. The validator runs the applicable check set below **independently and cumulatively**, in this order, and stops at the first failure. It returns `PASS` or `FAIL(code, rule)`.

| # | Check | Declaration | Offensive operation | Hostile defensive (`BREAK_BLOCKADE`) | Self operation (`INTERCEPT`, `FORTIFY`, `RESUPPLY`) |
|---|---|---|---|---|---|
| 1 | Actor authority and nation state (`WAR-001`, `WAR-002`) | Yes | Yes | Yes | Yes |
| 2 | Target existence, distinctness, not dormant (`WAR-003`) | Yes | Yes | Yes | Self only |
| 3 | B-03 restricted pair (`NET-025`/`NET-026`) | Yes | Yes | Yes | No hostile target |
| 4 | B-03 newcomer protection and dormancy (`ONB-019`/`ONB-020`, `D-028`) | Yes | Yes | Yes | Yes for the actor; no target |
| 5 | B-08 national `DP-T01` — **declaration only** (`WAR-010`) | Yes | **No** | **No** | **No** |
| 6 | B-09 same-Alliance ban (`ALL-206`–`ALL-208`) | Yes | Yes | Yes | No |
| 7 | B-09 Alliance `AT-E01` NAP for covered pairs (`WAR-012`) | Yes | Yes | Yes | No |
| 8 | Political `TRANSITION`/`CRISIS` (`DMP-265`, §9.4) | New only | New only; accepted defensive commitments are exempt under `WAR-009g` | New only; accepted defensive commitments are exempt under `WAR-009g` | New only; accepted defensive commitments are exempt under `WAR-009g` |
| 9 | Active campaign and slot (`WAR-046`, `WAR-007`) | Slot | Campaign | Campaign and blockade | Campaign where required |
| 10 | OP and economic reservation (`F-WR-001`, `F-WR-002`) | Yes | Yes | Yes | Yes |
| 11 | Readiness gate (`F-WR-005`) | No | Yes | Yes | Yes |
| 12 | City target validity (`WAR-109a`) | No | Only for `OP-05` city target | No | No |

`WAR-009a` Checks 5, 6 and 7 are **separate and cumulative**. Passing one never substitutes for another. Leaving a shared Alliance does not bypass a still-active `AT-E01` NAP, and an expired Alliance NAP does not permit an attack between nations that still share an Alliance. The validator reads current records at each run; it never reads a cached roster, a copied treaty list or a client-side flag.

`WAR-009b` A **city target is not a separate attack path**. A city-targeted `OP-05` runs every national check in the offensive column first and the city check last. The city check can only reject; it can never waive, weaken or replace a national check. The attack is recorded against the target **nation** and names the city.

`WAR-009c` The validator runs at three points: **submission** (inside the acceptance transaction), **P2** against the frozen state, and **immediately before P5 execution**, after P3.7 has resolved the Food and readiness obligations. The three runs are independent. The **execution-time state governs**; a P2 pass is not a P5 guarantee and a P2 failure is not cured by a later state change. Protection, Alliance membership, treaties, political state, campaign state, readiness and the Food shortage state are all re-read at each point. At P2 and pre-P5, row 8 applies `WAR-009g`: a **validly accepted defensive commitment** is exempt from the political-state denial, while every other row still runs independently and cumulatively at the same point. Submission has no exception.

`WAR-009d` A blocked action is **not executed at all**: no OP is consumed, no resource leaves a reservation, no readiness changes, no strength or infrastructure is lost, no objective progress is added, and no state is applied. The reservation is released exactly once under `WAR-002`. The reason names the failing check and the blocking rule; it never reveals private treaty text.

`WAR-009e` `AUD-AL-017` is written **only** when checks 6 or 7 fail (`WRF-07`, `WRF-08`) and uses its exact B-09 field set. Every other denial writes `WRA-02` or `WRA-03` and never `AUD-AL-017`.

`WAR-009f` No Alliance role, office, ballot, majority, treaty, AI, administrator, UI state or client check may waive a row of the table. Hiding an attack button, filtering a list or checking on the client is **not** enforcement. A hostile path that does not call this validator is a release blocker, not a rule variant. `WAR-160` states the same invariant.

`WAR-009g` **Narrow political-state exception for an accepted defensive commitment.** *Provisional (REQ-666; `B10-C26`).* Row 8 denies **new** actions in `TRANSITION` or `CRISIS`. At P2 and pre-P5 it exempts a commitment that was validly accepted before the state began, because B-06 `DMP-265` requires an existing defensive commitment to resolve. The exemption is limited to a commitment that satisfies **all** of the following:

1. its operation type is one of the defensive or sustainment types in `WAR-053e` — `INTERCEPT`, `FORTIFY`, `BREAK_BLOCKADE` or `RESUPPLY`;
2. it was submitted and accepted while the turn was OPEN and before the political state began;
3. the commitment record stores its action ID, type, target, parameters, acceptance turn and the political state at acceptance;
4. its operation parameters are unchanged since acceptance;
5. its OP and every applicable resource were reserved correctly at acceptance and the reservation is still held in full;
6. it has not expired, been cancelled or become invalid for an unrelated reason;
7. its target and authorization still pass every non-political check.

The exemption changes **only** row 8. Checks 1–7 and 9–12 still run independently and cumulatively at the same point, including the B-03 restricted pair, newcomer and dormancy protection, the B-08 declaration rule, the B-09 same-Alliance ban, the covered `AT-E01` NAP, campaign and slot validity, OP/resource integrity, readiness, city-target validity and idempotency. A qualifying commitment keeps its existing reservation and spends nothing new. At submission there is **no** exception: every new action, defensive or offensive, is rejected with `WRF-09` and reserves nothing. The exemption never creates an action, a slot, an OP point, a resource or a discretionary order, and it never revives an action that already failed. If any non-political check fails, the action is blocked under that check's code, its reservation is released exactly once, and `AUD-AL-017` is written only for a B-09 check 6 or 7 failure (`WAR-009e`).

**Political-state scenarios.** Every row is deterministic; `WRF-09` is the only political code.

| # | Scenario | Submission | P2 | Pre-P5 | Result |
|---|---|---|---|---|---|
| 1 | `TRANSITION` before a new offensive submission | Active, new → `WRF-09` | — | — | Rejected; nothing reserved |
| 2 | `TRANSITION` after offensive acceptance but before P2 | Accepted while normal | Active, not defensive → `WRF-09` | — | Fails at P2; every reservation released; no effect |
| 3 | `TRANSITION` after P2 but before P5 | Accepted while normal | Passed while normal | Active, not defensive → `WRF-09` | Fails at pre-P5; every reservation released; no effect |
| 4 | `TRANSITION` after defensive acceptance but before P2 | Accepted while normal | Row 8 exempt; checks 1–7/9–12 run and pass | Resolves | Commitment resolves at P5 |
| 5 | `TRANSITION` after defensive acceptance but before P5 | Accepted while normal | Passed while normal | Row 8 exempt; checks 1–7/9–12 run and pass | Commitment resolves at P5 |
| 6 | `CRISIS` instead of `TRANSITION` | Same as row 1 for a new action | Same as rows 2/4 | Same as rows 3/5 | Identical outcomes; the state name changes nothing |
| 7 | State ends before P5 | A new action rejected while active stays rejected | An offensive that failed while active stays failed | An accepted offensive whose remaining run sees a normal state passes row 8; a defensive commitment resolves under the exemption | Execution-time state governs; no retroactive revival |
| 8 | Defensive commitment also blocked by an independent B-09 restriction | Accepted while normal | Row 8 exempt, but check 6 or 7 fails `WRF-07`/`WRF-08` | — | Blocked; reservation released once; `AUD-AL-017`; no bypass |

An accepted defensive commitment that fails solely because its own parameters changed is no longer the accepted commitment: it is a new action, has no exemption and, while the state is active, is rejected at submission. A released reservation is never restored by the exemption.

`WAR-010` An active `DP-T01` national NAP blocks a new war declaration. It does **not** terminate, suspend or restrict an already-active campaign, and it does **not** block operations inside one. B-08's authorized effect is a declaration block only; B-10 creates no further national treaty effect. This is the exact scope: `DP-T01` is **absent from checks 6–12** and appears only in the declaration column.

`WAR-011` Two nations sharing at least one active Alliance membership cannot declare on each other. The check is independent of the Alliance NAP check and of any constitution, office, vote or preference.

`WAR-012` An active `AT-E01` Alliance NAP blocks a declaration **and every hostile operation** by a covered member of one party against a covered member of the other. A non-consenting member remains a member but is **not covered**; the block applies only to recorded consenting pairs. `AT-E00` is a record-only treaty with **no attack effect** and is never treated as an active NAP.

`WAR-013` The applicable check set is re-run at P2 and again immediately before P5 execution against execution-time state. A declaration or operation that fails any recheck fails closed with no cost, no mutation and a stable failure code. A target that changed state is never retargeted (`TR-053`).

`WAR-014` A B-09 same-Alliance or Alliance NAP block writes the mandatory `AUD-AL-017` event with its defined fields. Other denial types use the B-10 audit events in §24, never `AUD-AL-017`.

### 5.4 Rejection codes

| Code | Meaning | Cost |
|---|---|---|
| `WRF-01` | Actor is not the authenticated owner | None |
| `WRF-02` | Actor nation dormant, retired or inactive | None |
| `WRF-03` | Target invalid, self, dormant or retired | None |
| `WRF-04` | Restricted pair | None |
| `WRF-05` | Target under newcomer protection | None |
| `WRF-06` | National `DP-T01` NAP active | None |
| `WRF-07` | Same-Alliance ban | None |
| `WRF-08` | Alliance `AT-E01` NAP covers the pair | None |
| `WRF-09` | `TRANSITION` or `CRISIS` | None |
| `WRF-10` | No outgoing campaign slot | None |
| `WRF-11` | Insufficient OP | None |
| `WRF-12` | Insufficient unreserved crowns | None |
| `WRF-13` | Duplicate submission (idempotent replay) | None; original receipt returned |
| `WRF-14` | Declaration expired before resolution | Reservations released |

---

## 6. Campaign architecture and state machine

### 6.1 States

| State | Entry | Permitted | Prohibited | Exit |
|---|---|---|---|---|
| `DECLARED_PENDING` | Declaration accepted | Nothing military; cancellation by the declarer before freeze | Everything else | P5 → `ACTIVE`, or failure → `VOID` |
| `ACTIVE` | Declaration resolved at P5 | Operations, objectives, settlement proposals, surrender | A second outgoing declaration | Victory, surrender, settlement, expiry → `ENDED` or `SETTLING` |
| `SETTLING` | A settlement is accepted and awaiting its P5 transfer | Settlement completion only | New operations | P5 → `ENDED` or back to `ACTIVE` on atomic failure |
| `SUSPENDED` | A participant became dormant | Nothing; deadline still runs | Operations, declarations, settlement acceptance | Dormancy end → `ACTIVE`; 48 suspended turns → `ENDED` by abandonment |
| `ENDED` | Terminal outcome recorded | Read-only history | Everything military | `ARCHIVED` after 84 turns |
| `ARCHIVED` | Permanent record | Read-only | Everything | None |
| `VOID` | Declaration failed before activation | Nothing | Everything | Permanent record |

`WAR-015` There is no `PAUSED` state. War does not pause for a political transition, a lost election, a holiday, a server delay or an Alliance decision.

`WAR-016` A campaign that is `ACTIVE` and has recorded no resolved offensive operation by either side for 24 consecutive turns enters a public `STALEMATE` condition. At 48 consecutive turns it expires at the next P6 under §7.4. A resolved offensive operation by either side resets the counter.

### 6.2 Transition diagram

```
                 declaration accepted
                          │
                          ▼
                 DECLARED_PENDING ──fail──► VOID
                          │ P5 resolve
                          ▼
        ┌──────────────► ACTIVE ◄──────────────┐
        │                 │  │                 │
        │   dormancy      │  │ settlement      │ dormancy ends
        │                 ▼  ▼ accepted         │
        │            SUSPENDED  SETTLING ───────┘
        │                 │          │
        │      48 turns   │          │ P5 transfer
        │                 ▼          ▼
        └──────────────► ENDED ◄─────┘
                          │ 84 turns
                          ▼
                       ARCHIVED
```

`WAR-017` Every state change writes a `WRA-05` campaign-state event with the prior state, new state, turn, reason and actor.

### 6.3 Deadline, extension and expiry

`WAR-018` A campaign's deadline is `declaration_resolved_turn + 84`. It may be extended **once** by 42 turns when both owners accept an `EXTEND` settlement proposal before the deadline. No further extension exists.

`WAR-019` The deadline is evaluated at P5.4 before operations resolve. An expired campaign does not resolve further offensive operations; pending operations fail with `WRF-20` and release their reservations. The expiry outcome is computed at P6 under §7.4.

`WAR-020` Expiry is not a defeat and creates no reparations, no exclusion and no protection. It is the designed off-ramp from a war neither side can win.

### 6.4 Dormancy

`WAR-021` When a participant becomes dormant (`D-028`), the campaign enters `SUSPENDED` at the next P0. No operation by either side may target the dormant nation, and the dormant nation submits nothing.

`WAR-022` An operation accepted before dormancy that has not resolved fails at P2 or P5 with `WRF-21`, releases every reservation and applies no effect. A defensive operation accepted by the dormant nation also fails and releases; protection is not a shield that spends OP.

`WAR-023` The deadline continues to run while suspended. After 48 suspended turns the campaign ends at P6 with outcome **`ABANDONED`**: the non-dormant side receives a **limited victory by abandonment**, with no reparations, no loot, no exclusion and no protection. If both sides are dormant, the outcome is a **draw**.

`WAR-024` A returning nation finds the campaign concluded or, if it returns before the 48-turn limit, `ACTIVE` again with its force, readiness and progress exactly as suspended. No progress decays during suspension.

### 6.5 Reroll — UD-032 resolution

`WAR-025` **UD-032 is resolved as Option A: the reroll block is retained.** A nation that is party to any campaign in `DECLARED_PENDING`, `ACTIVE`, `SUSPENDED` or `SETTLING` cannot reroll. The block is the existing B-03 `RRL-021` behaviour, now defined precisely.

`WAR-026` "Active campaign" for the reroll block includes a pending declaration made by or against the nation, an active campaign, a suspended campaign and a campaign awaiting settlement transfer. It ends when the campaign reaches `ENDED` or `VOID`.

`WAR-027` The block is escapable without waiting for expiry: the nation may **surrender** (§20.3), which ends the campaign at the next P5 and releases the block. The block therefore cannot trap a player indefinitely.

`WAR-028` A blocked reroll attempt is recorded as a review signal with the campaign identifier. It consumes nothing, changes no state and is not a sanction. Attempting to reroll through a second account is a distinct B-03/Prompt 12 matter and is not created or adjudicated by B-10.

**Why Option A.** B-03 already fails closed; permitting a reroll would let a losing player erase an active war and the record attached to it (identity laundering), would require a forfeit-and-attribution model with no owner-approved basis, and would hand the opponent an unresolved outcome. Option B's forfeit adds settlement and attribution rules without improving fairness; Option C preserves the war but splits account and nation identity in a way B-03's one-account model does not support. Option A is simplest, preserves every existing rule and, with surrender as the off-ramp, does not deny player freedom beyond the campaign's bounded life. The trade-off is disclosed: a player who wants to reroll must first end the war.

### 6.6 Historical attribution and cleanup

`WAR-029` A retired nation's campaigns remain attributed to that nation and remain readable permanently. Its opponent's record shows the outcome and the retirement, not a disappearance. A reroll never transfers a campaign, a victory, a loss, a settlement obligation or an exclusion to the replacement nation.

`WAR-030` `ARCHIVED` campaigns keep the campaign header, objectives, outcomes, settlement record and audit references. Per-turn operation rows may be compacted under `D-026` after 12 months into a permanent summary; totals and outcomes are never deleted.

`WAR-031` No cleanup path may delete a campaign that is `ACTIVE`, `SUSPENDED`, `SETTLING` or has an outstanding settlement. Archival is a read-model change only.

---

## 7. Objectives and victory

### 7.1 The closed objective catalogue

`WAR-032` There are exactly six objective types. No hidden score, secondary meter, resistance pool or war-point currency exists. Both sides score progress on the same primary and secondary objectives; progress is per side, 0…1000.

| ID | Name | Progress earned by | Completion |
|---|---|---|---|
| `OBJ-ATTRITION` | Attrition | Destroying enemy strength points in resolved offensive operations | 1,000 |
| `OBJ-INTERDICTION` | Interdiction | Successful raids and air strikes that impose supply denial | 1,000 |
| `OBJ-BLOCKADE` | Blockade | Holding an active blockade at the end of each P5 | 1,000 |
| `OBJ-AIR` | Air control | Successful air strikes and interceptions | 1,000 |
| `OBJ-DEFENCE` | Defensive success | Successful interceptions, fortifications that absorb an attack, and broken blockades | 1,000 |
| `OBJ-STRIKE` | Strategic strike | Successful missile and air strikes | 1,000 |

`WAR-033` The declarer selects one primary and one secondary objective at submission. They must differ. Both are public. Neither can be changed, added or removed after acceptance.

`WAR-034` Progress is capped at 1,000 per side per objective. Progress cannot be bought, transferred, gifted or produced by an Alliance. Only a resolved B-10 operation adds progress.

`WAR-035` Each operation type may contribute progress at most **8 times per campaign per side**. Further resolutions of that type still resolve and still cause losses, but add no objective progress. This is the anti-farming control.

### 7.2 Progress values

| Operation | ATTRITION | INTERDICTION | BLOCKADE | AIR | DEFENCE | STRIKE |
|---|---|---|---|---|---|---|
| `OP-01 RAID` | 40 | 70 | 0 | 0 | 0 | 0 |
| `OP-02 ASSAULT` | 80 | 30 | 0 | 0 | 0 | 0 |
| `OP-03 AIR_STRIKE` | 50 | 40 | 0 | 80 | 0 | 60 |
| `OP-04 BLOCKADE` | 0 | 40 | 100 | 0 | 0 | 0 |
| `OP-05 MISSILE_STRIKE` | 70 | 0 | 0 | 0 | 0 | 100 |
| `OP-06 INTERCEPT` | 0 | 0 | 0 | 40 | 60 | 0 |
| `OP-07 FORTIFY` | 0 | 0 | 0 | 0 | 50 | 0 |
| `OP-08 BREAK_BLOCKADE` | 0 | 0 | 0 | 0 | 60 | 0 |

All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. `OP-09 RESUPPLY` earns no progress. A failed offensive operation earns **no** progress; a successful one earns the value exactly once.

`WAR-036` Counter-progress: when a defensive operation succeeds against an offensive operation, the defender subtracts `floor(progress_value × 2500 / 10000)` from the attacker's matching objective total, floored at zero. The attacker still earns nothing for a failed operation.

### 7.3 Victory determination

`WAR-037` Victory is evaluated at P6 after all P5 battles and progress updates, in this order:

1. **Primary completion.** If exactly one side's primary progress is 1,000, that side wins.
2. **Decisive or limited.** If the winner's opponent has less than 250 primary progress, the outcome is **`DECISIVE_VICTORY`**; otherwise **`LIMITED_VICTORY`**.
3. **Simultaneous completion.** If both sides reach 1,000 on the primary in the same turn, compare `primary + floor(secondary / 2)`; the higher total wins a **`LIMITED_VICTORY`**; an exact tie is a **`DRAW`**.
4. **No completion.** The campaign continues until expiry, surrender or settlement.

`WAR-038` A defensive objective completion (`OBJ-DEFENCE` primary) wins for the side that completed it; the labels above are side-relative and do not imply that only the declarer can win.

### 7.4 Outcome set

| Outcome | Condition | Reparations | Exclusion | Record |
|---|---|---|---|---|
| `DECISIVE_VICTORY` | §7.3 step 2 | Only by settlement | Only by settlement | Permanent |
| `LIMITED_VICTORY` | §7.3 steps 2–3 | Only by settlement | Only by settlement | Permanent |
| `DRAW` | §7.3 step 3 tie, or a mutual ceasefire | None | None | Permanent |
| `MUTUAL_PEACE` | Both owners accept a ceasefire | None | None | Permanent |
| `SURRENDER` | One owner surrenders | None | None | Permanent |
| `EXPIRY` | Deadline reached | None | None | Permanent |
| `ABANDONED` | §6.4 dormancy expiry | None | None | Permanent |

No victory automatically transfers value, destroys development or grants protection. Automatic conquest rewards are rejected; every transfer requires a settlement (§21).

---

## 8. Operations Points

### 8.1 The single national pool

`WAR-039` Each nation has exactly one Operations Points pool. It is military-only, non-transferable, non-purchasable and never shared. There is no per-war pool, no per-campaign pool and no Alliance pool. This is D-015 as amended on 2026-11-04: the amendment changes only the regeneration rate and the carry below the cap; every other property is unchanged.

| Property | Rule | Status |
|---|---|---|
| Cap | 10 OP | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Regeneration | At the opening of P3.7, once per successful boundary: `op_balance = min(op_cap, op_balance + 1)`; one `REGENERATED` item per nation per turn, including a recorded `0` at the cap; never above `op_cap` | Structural rate (D-015 as amended 2026-11-04); rate and cap calibrated together by Prompt 14 |
| Carry | `op_balance` persists across turns below the cap; no point above the cap exists; nothing is converted, gifted or transferred | Structural (D-015 as amended) |
| Availability | `available = max(0, op_balance − reserved)`; spendable from the next OPEN window, which begins only when P7 publishes the turn as `COMPLETED` | Structural |
| Starting value | Cap | Structural |
| Reservation | At acceptance, while the turn is OPEN, before P1 freeze | Structural (D-015) |
| Consumption | At P5 resolution | Structural (D-015) |
| Transfer | None, ever | Structural (D-015) |
| Purchase | None, ever | Structural |

`WAR-040` The OP pool is a **persistent national ledger**, not a turn-scoped counter. `op_balance` is the unspent balance carried between turns; `reserved` is the sum of live `HELD` items; `available = max(0, op_balance − reserved)`. The only balance increase is the P3.7 regeneration. P0 only confirms the turn identity and writes the run record; it performs **no** OP mutation. P3 performs **no** OP mutation except the single regeneration at the opening of P3.7. P7 performs **no** regeneration: it verifies `reserved = 0`, releases any unresolved action under `WAR-043`, and publishes the turn, after which the next OPEN window may spend the balance. The regeneration is keyed on `(nation_id, turn_id)`; a second attempt for the same boundary returns the original receipt and writes nothing. A stored balance above `op_cap`, a negative balance, a reservation above the balance, or a second regeneration for one turn is an integrity failure (`WRF-34`), not a rule.

`WAR-041` A player sees four numbers: **cap**, **available**, **reserved** and **consumed this turn**. Internally `op_balance = available + reserved`; `available = max(0, op_balance − reserved)`; `consumed` is a per-turn counter for display and audit, not a deduction from `op_balance` a second time. The arithmetic is exact integer arithmetic; `0 ≤ available ≤ op_balance ≤ op_cap` and `0 ≤ reserved ≤ op_balance`. A player who wants the full pool reads `available + reserved`; a player who wants spendable OP reads `available` without subtracting anything mentally.

`WAR-042` Every OP movement is an item in the national OP ledger: `REGENERATED`, `HELD`, `RELEASED`, `CONSUMED`. The ledger is append-only. An action writes exactly one `HELD` and at most one terminal item (`CONSUMED` or `RELEASED`), all keyed by `action_id`. A boundary writes exactly one `REGENERATED` item keyed by `(nation_id, turn_id)`. A retry of the same idempotency key returns the original receipt and writes nothing; it never reserves, consumes or regenerates a second time. A `RELEASED` item leaves `op_balance` unchanged because the amount was only reserved, never debited; a `CONSUMED` item decreases both `reserved` and `op_balance` by the amount exactly once.

`WAR-043` At the P7 close, **before** the turn is published, every accepted action without a terminal resolution is void: its OP and resource reservations are released, `WRF-22` is written, and it cannot be replayed into the next turn without a new submission. The close then verifies `reserved = 0`; if any reservation remains, `WRF-34` holds the checkpoint and the turn is not published. A released reservation does not refund OP because the balance was never debited; it only restores `available`. P7 writes no `REGENERATED` item.

`WAR-043a` The lifecycle is fixed and is not interchangeable with any other phase: **submission → `ACCEPTED` while the turn is OPEN → OP `HELD` and economic-resource reservation → P1 freeze → P2 revalidation → P3.7 single `REGENERATED` (+1, capped) → P4 order resolution where applicable (recruitment, B-05 construction) → P5 military execution and `CONSUMED` → rejection, expiry, cancellation or failure → `RELEASED` and audit → P7 verification and publication.** Acceptance never occurs at P4; consumption never occurs at acceptance; the only OP regeneration is at P3.7, and P0 and the P7 close never regenerate.

`WAR-043b` Unused OP is carried below the cap, never above it. There is no way for `op_balance` or `available` to exceed `op_cap`, and no reservation or point can be transferred to another nation, campaign, Alliance or action. Banking below the cap is deliberate: it lets a player save toward a heavy operation while keeping the recovery rhythm linear.

**Worked accounting.** Turn `t` opens with `op_balance = 8` (carried from `t−1`), `reserved = 0`, cap 10. During the OPEN window the player accepts A (2 OP) and B (3 OP): A writes `HELD 2`, then B writes `HELD 3`; `reserved = 5`, `available = 8 − 5 = 3`. P2 fails B: B writes `RELEASED 3`; `reserved = 2`, `available = 6`. P3.7 writes `REGENERATED 1`: `op_balance = min(10, 8 + 1) = 9`, `reserved = 2`, `available = 7`. P5 resolves A: A writes `CONSUMED 2`; `reserved = 0`, `op_balance = 7`, `consumed = 2`. P7 verifies `reserved = 0` and publishes; the next OPEN window sees `op_balance = 7`, `available = 7`. P3.7 of `t+1` regenerates to 8. If A had not resolved by the P7 close, A would write `RELEASED 2` and `WRF-22`; `op_balance` would remain 9 and `available` would return to 9. A second `CONSUMED` for A is `WRF-34` and debits nothing.

**Worked examples — OP regeneration, reservation and release.** Notation: `R(T)` is the single `REGENERATED` item for turn T; `H(A)`, `C(A)` and `X(A)` are `HELD`, `CONSUMED` and `RELEASED` for action A. Cap 10 unless stated; all values are OP.

1. **Zero OP at a boundary.** `op_balance 0`, `reserved 0`, `available 0`; `R(T) +1`; final balance 1, reserved 0, available 1. Events: `R(T)`.
2. **One below cap.** `op_balance 9`, `reserved 0`, `available 9`; `R(T) +1`; final balance 10, available 10. Events: `R(T)`.
3. **Already at cap.** `op_balance 10`, `reserved 0`, `available 10`; `R(T) 0` is recorded; final balance 10, available 10. No point is created or lost; the zero event proves the boundary ran once.
4. **Below cap with an outstanding reservation.** `op_balance 6`, `reserved 4`, `available 2`; `R(T) +1`; final balance 7, reserved 4, available 3. The reservation survives the regeneration and is neither refunded nor double-counted.
5. **Multiple accepted operations.** `op_balance 10`; A holds 3, B holds 4, C holds 2 → `reserved 9`, `available 1`; `R(T) 0` (already at cap). At P5 A and C succeed (`C(A) 3`, `C(C) 2`) and B fails (`X(B) 4`); final balance 5, reserved 0, available 5, consumed 5. Events: `H(A)`, `H(B)`, `H(C)`, `R(T) 0`, `C(A)`, `C(C)`, `X(B)`.
6. **One accepted operation resolving after the P3.7 boundary.** `op_balance 7`; A holds 3 → `reserved 3`, `available 4`. `R(T) +1` → balance 8, reserved 3, available 5. P5 resolves A → `C(A) 3`, balance 5, reserved 0, available 5. The reservation is outstanding across the regeneration point and is consumed once.
7. **One operation cancelled before resolution.** `op_balance 6`; A holds 3 → available 3; A is cancelled while OPEN → `X(A) 3`, balance 6, reserved 0, available 6. `R(T) +1` → balance 7, available 7. A release restores availability, never the balance.
8. **Failed P5 processing followed by retry.** `op_balance 5`; A holds 2; `R(T) +1` → balance 6, reserved 2, available 4. P5 writes `C(A) 2` and debits to balance 4; the turn fails after that write. The retry reads the terminal `CONSUMED` item, writes nothing and leaves balance 4. If the failure occurred before `C(A)`, the retry consumes exactly once and still ends at 4. No second regeneration occurs because `R(T)` already exists.
9. **Repeated turn-boundary processing.** `op_balance 3`; the first run writes `R(T) +1` → 4; a duplicate run for the same `(nation_id, turn_id)` returns the original receipt and writes no item; final balance 4. P0 also refuses a duplicate run, so the boundary is processed once.
10. **A nation entering a restricted political state.** `op_balance 5`; an accepted defensive commitment D holds 2 before `TRANSITION` begins → `reserved 2`, available 3. `R(T) +1` → balance 6, reserved 2, available 4. New orders are rejected with `WRF-09` and reserve nothing; D resolves at P5 (`C(D) 2`) → balance 4, reserved 0, available 4. Regeneration does not bypass the state, and the accepted commitment is preserved under `WAR-009g`.
11. **A dormant nation.** `op_balance 4`, no reservations; `R(T) +1` → balance 5, available 5. Dormancy blocks the submissions it already blocks; the increased balance grants no action and bypasses no protection. The OP remains for the first legal window after the restriction ends.
12. **Reaching the cap while an old reservation remains outstanding.** `op_balance 9`; A holds 4 → `reserved 4`, available 5; `R(T) +1` → balance 10, reserved 4, available 6. P5 resolves A (`C(A) 4`) → balance 6, reserved 0, available 6. If A instead remains unresolved at P7, `X(A) 4` → balance 10, reserved 0, available 10, with `WRF-22`.

`WAR-044` A campaign ending while an operation is pending does not refund the operation as a special case; the ordinary P2/P5 failure path releases it. If the operation already resolved in that turn, it stands even if the campaign ends later in the same P5.

### 8.2 Action limits

`WAR-045` Per nation per turn: at most **3 accepted offensive operations** and **3 accepted conditional defensive operations**, in addition to one declaration and one settlement action. These are B-10's declared limits under D-024; they are not a general action budget. All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

`WAR-046` An operation may target only a nation with which the actor has an `ACTIVE` campaign. There is no attack outside a campaign.

---

## 9. Military readiness

### 9.1 The readiness model

`WAR-047` Readiness is one national integer from 0 to 1,000. It is a **combat and gate** value only. It never multiplies tax, production, research, construction or market prices, and it is not purchasable with real money or Crowns.

| Property | Value | Status |
|---|---|---|
| Starting readiness | 700 | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Cap | 1,000 | Structural |
| Paid-upkeep recovery | +50 per turn | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Unpaid-upkeep penalty | −100 per turn | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Interdiction penalty | −50 per successful interdiction | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Blockade recovery penalty | −25 per turn while blockaded | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Combat readiness loss | −25 per battle, win or lose | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Operation gate — light | 300 (RAID, FORTIFY, INTERCEPT, RESUPPLY) | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Operation gate — heavy | 500 (ASSAULT, AIR_STRIKE, BLOCKADE, BREAK_BLOCKADE, MISSILE_STRIKE) | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |

`WAR-048` Readiness is checked at acceptance, at P2 and immediately before P5. An operation whose readiness gate fails at P5 fails closed with `WRF-23` and releases its reservations.

`WAR-049` Readiness is never a function of account activity, login frequency, attendance, time zone or real time. It changes only through the listed game events.

### 9.2 Upkeep

`WAR-050` Readiness upkeep is a P3.7 obligation, paid in `ECN-105` rank 6. It has two components: crowns and ammunition/gasoline. The obligation is computed from `total_strength` in the **canonical P3.7 force snapshot** (`WAR-053m`), the same snapshot the military Food ration reads. The exact coefficients are stated once in `F-WR-003` of the [formula register](17_warfare_formula_register.md) and are provisional.

`WAR-051` If the obligation is paid, readiness recovers by 50 (capped at 1,000) at P3.7 and an `OBLIGATION_PAID` event is written. If it is unpaid, `ECN-106` applies: the obligation is **cancelled**, no debt exists, readiness falls by 100 (floored at 0) and the digest states the shortfall.

`WAR-052` Unpaid readiness upkeep never blocks an operation by itself; it lowers readiness, which may then fail a gate. The player is warned before the boundary when projected readiness would fall below a gate.

`WAR-053` Political `TRANSITION` or `CRISIS` does not change readiness upkeep, does not pause it and grants no combat, readiness or OP modifier (`DMP-265`).

### 9.3 Military food upkeep

`WAR-053a` A nation's force eats every turn. Strength points are **abstract combat weight**, not soldiers: one strength point is never one soldier. The conversion is a published, per-type **soldier-equivalent** table. Every value is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

| Unit type | Soldier-equivalents per strength point (`e_t`) |
|---|---:|
| `UNIT-INF` | 10 |
| `UNIT-ARM` | 4 |
| `UNIT-AIR` | 2 |
| `UNIT-NAV` | 20 |

`ration_equivalents = Σ_t (strength_points_t × e_t)`. A strength point of armour or air therefore consumes fewer rations than an infantry point, and a naval point consumes more; the model is a national crew-and-support abstraction, not a unit roster.

`WAR-053b` **Ration demand.** `military_food_demand = ceil(ration_equivalents / 1000)`. One Food unit feeds 1,000 soldier-equivalents for one turn — the same physical unit and the same 1,000-person scale as civilian Food (`ECN-080`), so the two demands are directly comparable and never use different units. Demand is computed at P3.7 from the **canonical P3.7 force snapshot** (`WAR-053m`), which is the same force readiness upkeep reads and the same force the frozen P5 baseline uses. A force of 1,000 infantry points and 100 naval points has 10,000 + 2,000 = 12,000 equivalents and demands **12 Food**.

`WAR-053c` **Timing and civilian priority.** The ration is a P3.7 obligation. P3.6 civilian Food resolves first and is never reduced to feed the military. The `OP-09` Food reservation is a **conditional claim on surplus above the protected civilian requirement** (`WAR-053l`): P3.6 verifies that condition before it consumes anything, and a reservation that would leave the protected requirement unmet is released to civilian use, with the `OP-09` action failing in whole under `WRF-25`. P3.7 may consume only Food that remains unreserved after P3.6 and after every other reservation held for another action. If the remaining Food is below the demand, the **military** obligation is short. The civilian `food_demand`, `unmet_food`, `shortfall_ratio` and `hunger_penalty_bp` (`ECN-080`–`ECN-083`) are computed before and without the military ration and are never changed by it.

`WAR-053d` **Payment and shortage.** If unreserved Food is at least the demand, the engine consumes exactly the demand, writes `OBLIGATION_PAID` with component `MILITARY_RATION`, and changes no readiness by the ration itself. If it is below the demand, the whole obligation is **cancelled**: no partial consumption, no debt, no negative inventory, no future-income seizure and **no unit deletion**. The engine writes `OBLIGATION_CANCELLED`, applies `readiness = max(0, readiness − 100)`, and sets `RATION_SHORT` for the turn. The unreserved quantity is read after P3.6 and after the `WAR-053l` conditional check; a released `OP-09` reservation is not available to the garrison as if it were ordinary surplus, because the releasing action has failed. The whole-obligation rule is `ECN-106`; the consequence belongs to B-10.

`WAR-053e` **Shortage consequence and recovery.** While `RATION_SHORT` is active, the canonical validator fails every **offensive** operation at the pre-P5 run with the new code `WRF-35` and releases it; defensive and sustainment operations (`INTERCEPT`, `FORTIFY`, `BREAK_BLOCKADE`, `RESUPPLY`) still resolve. The state clears at the next P3.7 in which the ration is paid in full. Readiness recovers only through paid readiness upkeep (+50, `WAR-051`) and a resolved `OP-09` (+100, `WAR-110`); there is no catch-up, no automatic recovery and no multiplier while short. A nation may pay readiness upkeep while short; the two obligations are separate and the net readiness change is the sum.

`WAR-053f` **Distinct from `OP-09` operational rations.** `OP-09 RESUPPLY` carries an additional **4 Food field ration**, reserved with the action at acceptance and consumed at P5 through `RESERVATION_CONSUMED`. It is an operational ration, not the garrison ration: it never counts toward `military_food_demand`, never substitutes for it and never reduces it. At acceptance it may be reserved only from the eligible Food surplus defined by `WAR-053l`; if that surplus is below 4, the whole action is rejected with `WRF-25` and nothing is reserved. It is never partially funded and never takes Food that the protected civilian requirement needs. The P3.7 ration cannot consume Food reserved for `OP-09`, because obligations never consume a reservation (`TR-070`).

`WAR-053g` **No double counting.** The recurring ration is charged once per turn from the whole force. The `OP-09` field ration is charged once per accepted operation. They are two separate events with two separate purposes; a nation that pays both pays their sum, a nation that pays only one receives only that effect, and no path derives one from the other or charges the same Food twice. A released `OP-09` reservation returns to unreserved stock once and cannot be reserved, consumed or released a second time; idempotency is keyed on the action ID.

`WAR-053h` **Visibility and audit.** The owner sees the demand, the paid or short outcome, the shortfall and `RATION_SHORT`; an opponent sees only the existing readiness band and never the exact Food stock. The events are `OBLIGATION_PAID`/`OBLIGATION_CANCELLED` with component `MILITARY_RATION`, plus `WRA-14` for the inventory leg. A protected-civilian release writes `RESERVATION_RELEASED` for the `OP-09` action and `WRF-25` on the action record; no new ledger type is created. The digest states the protected requirement, the eligible surplus and the release, if any.

`WAR-053i` **Political states do not change the ration.** `TRANSITION` and `CRISIS` neither pause nor reduce military Food upkeep and grant no shortage exception (`DMP-265`). The ration is a recurring obligation, not a military order.

`WAR-053l` **Protected civilian Food requirement and the conditional `OP-09` reservation.** *Provisional (REQ-695/REQ-697).* Civilian demand is canonical and is computed before any `OP-09` claim is considered:

```
protected_civilian_food = ceil(population / 1000)                  (ECN-080; F-EC-002)
other_food_reservations = Σ Food held for other accepted actions, excluding OP-09
eligible_op09_surplus   = opening_food + projected_food_production
                          − other_food_reservations
                          − protected_civilian_food
```

**At acceptance (while the turn is OPEN).** An `OP-09` action may reserve its 4 Food only while `eligible_op09_surplus − (OP-09 Food already held this turn) ≥ 4`. Otherwise the whole action is rejected with `WRF-25`, nothing is reserved and no partial operation exists. `projected_food_production` is the turn's planned net Food output at P3.3 and is a labelled forecast, not a guarantee. The reservation is held once, in the existing Food inventory; no second inventory and no second reservation is created.

**At P2.** The acceptance condition is re-checked against the frozen opening stock and the frozen production plan. A failure fails the action in whole and releases its reservation exactly once.

**At P3.6, before any civilian consumption.** The actual quantities are read and the protected requirement is tested first:

```
food_after_other   = opening_food_actual + food_produced_actual
                     − other_food_reservations
op09_held_total    = 4 × (accepted OP-09 actions still holding Food)
available_if_held  = food_after_other − op09_held_total
```

If `available_if_held ≥ protected_civilian_food`, every `OP-09` reservation stands and `food_for_civilians = available_if_held`. Otherwise the protected requirement is short by `release_required = protected_civilian_food − available_if_held`; reservations are released in **reverse acceptance order** (latest accepted first, action ID descending as the tie-break) until the released total is at least `release_required`. Each released action fails in whole with `WRF-25`, consumes nothing at P5 and releases all 4 of its Food; no reservation is partially released. Then `food_for_civilians = food_after_other − (op09_held_total − released_total)`, and civilian consumption and `unmet_food` are computed from that value under `ECN-082`/`ECN-083`. If even the released total cannot cover demand, civilians receive all available Food, the remaining shortfall is recorded and the `OP-09` actions have already failed.

The requirement uses the **current frozen population** for the boundary. Population is updated only at P3.8 and is effective next turn (B-06 `DMP-034`), so the same requirement is used at acceptance, P2 and P3.6; an audited population correction before P3.6 changes the requirement and is handled by the same P3.6 test, never by spending protected Food. A released reservation never becomes ordinary surplus for the garrison: the action that held it has failed, and the released Food is consumed by civilians first.

**Worked examples — civilian Food protection.** All values are in Food units.

1. **Fully funded civilian demand.** Opening 50, production 0, demand 50, `OP-09` requests 4. `eligible_op09_surplus = 50 + 0 − 0 − 50 = 0 < 4`. The action is rejected with `WRF-25`; nothing is reserved; P3.6 consumes 50 and `unmet_food = 0`. The operation cannot displace civilian demand.
2. **Sufficient surplus.** Opening 60, production 0, demand 50, `OP-09` requests 4. `eligible_op09_surplus = 60 − 50 = 10 ≥ 4`; 4 are reserved. At P3.6, `available_if_held = 60 − 4 = 56 ≥ 50`; civilians consume 50, the field ration stands, and P5 consumes 4. End stock 6 (2 unreserved + 4 consumed at P5); no shortfall.
3. **Production and other reservations.** Opening 20, planned and actual production 40, another accepted action holds 6, demand 50, `OP-09` requests 4. `eligible_op09_surplus = 20 + 40 − 6 − 50 = 4 ≥ 4`; 4 are reserved. At P3.6, `food_after_other = 20 + 40 − 6 = 54`; `available_if_held = 54 − 4 = 50 ≥ 50`; civilians consume 50 and the field ration stands. If actual production is only 35 instead of 40, `food_after_other = 49` and `available_if_held = 45 < 50`; the 4 are released, the action fails with `WRF-25`, `food_for_civilians = 49`, `unmet_food = 1` and the hunger ratio uses 49. No protected Food is spent and no debt is created.
4. **Civilian demand changes or an estimate is stale.** Opening 55, production 0, demand 50 at acceptance, `OP-09` reserves 4 (`eligible surplus 5 ≥ 4`). Before P3.6 an audited correction raises the frozen population so demand becomes 54. At P3.6, `available_if_held = 55 − 4 = 51 < 54`; the 4 are released, the action fails, `food_for_civilians = 55`, `unmet_food = 0`. If the correction instead lowers demand to 48, `available_if_held = 51 ≥ 48` and the reservation stands. The stale estimate is corrected by the P3.6 test, not by spending protected Food.
5. **P5 interruption and retry.** An accepted `OP-09` holds 4. At P5 the action consumes them through one `RESERVATION_CONSUMED` keyed on the action ID. If P5 is interrupted after consumption but before commit, recovery resumes from the P5 checkpoint and does not consume again; if it is interrupted before consumption, the retry consumes exactly once. A P3.6 release already failed the action, so no P5 consumption can follow. The same 4 units are never both consumed and released, and no second reservation is created on retry.
6. **Military recurring rations and `OP-09`.** Opening 70, production 0, demand 50, `OP-09` reserves 4. At P3.6 `available_if_held = 66 ≥ 50`; civilians consume 50, leaving 20. At P3.7 the garrison demand is 3 Food (3,000 soldier-equivalents). Unreserved Food is 16 (`20 − 4 held`), so the 3 are paid, readiness is unchanged and 13 remain unreserved. At P5 the 4 field rations are consumed. The total debited is 50 civilian + 3 garrison + 4 operational = 57, each with its own event and purpose; the garrison demand never included the field ration.

`WAR-053m` **The canonical P3.7 force snapshot.** *Provisional (REQ-694/REQ-696).* There is no P3.0 and no second force baseline. B-10 declares one processing step at the **opening of P3.7**, before `ECN-105` rank 6(a), inside the authorized P3.7 subphase; it creates no global phase and changes no B-02 phase. That step materializes any strength whose recruitment completion turn has arrived and stores one immutable snapshot:

```
force_snapshot(t) = { strength_INF, strength_ARM, strength_AIR, strength_NAV }
total_strength    = Σ_t force_snapshot(t).strength_t
ration_equivalents = Σ_t (force_snapshot(t).strength_t × e_t)
```

The snapshot contains:

1. the force at the opening boundary, which is the prior turn's post-P5 force;
2. plus every recruitment order whose completion turn is this turn and which was paid and completed at the prior turn's P4 — its strength is added before the snapshot is stored;
3. minus nothing else: no current-turn recruitment has run, no pending order is included, and no cancelled, failed or unaffordable order ever entered.

It excludes current-turn P4 recruitment (not yet resolved), pending recruitment (not yet complete), cancelled or failed recruitment (never entered) and strength lost at any P5 (already removed from the opening force). The same stored values are read by the military Food ration (`F-WR-036`) and readiness upkeep (`F-WR-003`); neither may recompute a different force. The P5 operational force is the snapshot adjusted only by voluntary P4 disbanding (`WAR-060`), which is an explicitly justified difference: disbanded strength was still fed and maintained at P3.7 earlier in the same turn but is absent from the frozen P5 baseline by rule. P5 losses apply after the battle and reduce the next turn's opening force.

### 9.4 Political `TRANSITION` and `CRISIS`

`WAR-053j` `DMP-265` is implemented by B-10 with the following exact rule. The rule is mechanical and creates no combat, readiness, OP or economic modifier.

1. **New declaration.** Rejected at submission with `WRF-09`; nothing reserves.
2. **New offensive operation.** Rejected at submission with `WRF-09`; nothing reserves.
3. **New defensive or sustainment operation.** Also rejected at submission with `WRF-09`; DMP-265 blocks **new military orders**, not only offensive ones.
4. **Accepted defensive commitment.** An operation accepted while the political state was normal resolves at P5 even if the state begins before the boundary: `INTERCEPT` may trigger, `FORTIFY` may apply, `BREAK_BLOCKADE` and `RESUPPLY` resolve. It is not a new order. `WAR-009g` supplies the narrow row-8 exemption and lists the seven conditions; every other check still runs, so a commitment also blocked by a B-03/B-08/B-09 restriction does not resolve.
5. **Accepted offensive operation.** Fails at the first validation run after the state begins (P2 or pre-P5) with `WRF-09`, releases every reservation and applies no effect. It is not converted into a defensive action.
6. **War does not pause.** Campaign deadlines, the stalemate counter, blockade duration, readiness upkeep, military Food upkeep, the `BLOCKADED` recovery penalty, objective progress and settlement windows all continue.
7. **Blockade state.** A blockade imposed before the state continues; `BREAK_BLOCKADE` is an accepted defensive commitment and resolves under item 4.
8. **Diplomacy.** A ceasefire, surrender or settlement proposal or acceptance is not a military order and remains available to the authenticated owner; it is not blocked by this rule.
9. **No retroactive validation.** An action that failed under item 5 is not revived when the political state ends; a new submission is required.
10. **Return to normal.** From the first boundary at which neither `TRANSITION` nor `CRISIS` is active, new orders are accepted normally. The state never retroactively validates, voids, boosts or penalizes an action resolved while it was active.

`WAR-053k` The political check is `WAR-009` row 8 and runs at submission, P2 and immediately before P5. Submission has no exception. At P2 and pre-P5, `WAR-009g` exempts a qualifying accepted defensive commitment from row 8 only; checks 1–7 and 9–12 remain independent and cumulative. The execution-time state governs. `WRF-09` is the only political code; no separate offensive or defensive code exists.

---

## 10. Military units, recruitment and development

### 10.1 Force pools

`WAR-054` A nation's military is four integer **strength-point pools**, one per unit type. There are no individual units, no damaged state, no location and no movement. Losses subtract strength points; recruitment adds them.

| ID | Unit type | Strength per point | Attack factor | Defence factor | Unlock tier |
|---|---|---|---|---|---|
| `UNIT-INF` | Infantry | 10 | 8,000 bp | 11,000 bp | T1 |
| `UNIT-ARM` | Armour | 25 | 12,000 bp | 9,000 bp | T2 |
| `UNIT-AIR` | Aircraft | 20 | 14,000 bp | 6,000 bp | T3 |
| `UNIT-NAV` | Naval | 30 | 11,000 bp | 10,000 bp | T3 |

All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. "Strength per point" is the abstract weight of one point of that type in the force-cap calculation; attack and defence factors are basis points applied to strength in the battle formula.

### 10.2 Development tiers and buildings

`WAR-055` Military capability is gated by **national development tier**, not by a new building:

| Tier | Requirement | Unlocks |
|---|---|---|
| `MIL-T1` | Always available | Infantry |
| `MIL-T2` | 2 cities **or** total infrastructure ≥ 100 | Armour |
| `MIL-T3` | 4 cities **or** total infrastructure ≥ 250 | Aircraft, naval |
| `MIL-T4` | 6 cities **or** total infrastructure ≥ 500 | Missile strikes |

All thresholds are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

`WAR-056` **No military building exists and no Military research branch exists.** The B-05 17-facility catalogue and its five research branches remain closed and unchanged. This is a deliberate deferral: adding a military building would revise B-05's catalogue, costs, capacity and construction rules without evidence that the simpler national tier is insufficient. A future expansion may propose one through the normal decision process; B-10 creates none.

`WAR-057` A tier loss caused by demolition, a city-count change or infrastructure damage does **not** destroy existing strength, but it blocks further recruitment of the affected type until the tier is restored. No unit is disbanded automatically.

### 10.3 Caps and recruitment

| Property | Value | Status |
|---|---|---|
| Force cap (strength points) | `1,000 + 100 × city_count + 2 × total_infrastructure` | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Training capacity per turn | `20 + 5 × city_count`, capped at 80 | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Maximum single-type share | 60% of total strength after recruitment | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Recruitment time | 1 turn (INF), 2 turns (ARM, AIR), 3 turns (NAV) | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |

`WAR-058` Recruitment is a P4 order. It reserves crowns and resources at acceptance, consumes them at P4, and adds the strength points at the **opening of the completion turn's P3.7**, immediately before the canonical force snapshot (`WAR-053m`). The completion turn is `order_turn + training_turns`, where training is 1 turn for infantry, 2 for armour and aircraft and 3 for naval (§10.3, `F-WR-015`): an infantry order placed at P4 of turn T enters T+1's snapshot, and an armour order placed at P4 of T enters T+2's. The added strength is then eligible for that turn's military Food ration, readiness upkeep and P5 operations; it is not eligible for any earlier P3.7 or P5. It consumes no OP. A recruitment order that would exceed the force cap or the single-type share is rejected at acceptance with `WRF-24`.

`WAR-059` Recruitment costs:

| Unit | Crowns per strength point | Resources per strength point |
|---|---|---|
| `UNIT-INF` | 20 | 0.2 steel, 0.1 ammunition |
| `UNIT-ARM` | 24 | 0.2 steel, 0.08 ammunition |
| `UNIT-AIR` | 45 | 0.1 aluminium, 0.1 gasoline, 0.1 ammunition |
| `UNIT-NAV` | 40 | 0.27 steel, 0.13 gasoline, 0.07 ammunition |

All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. Resource quantities are computed with ceiling rounding per order; the formula register is authoritative.

`WAR-060` Disbanding is voluntary at P4, instant, and returns no resources and no crowns. It reduces strength immediately. It cannot be used to avoid a pending battle in the same turn: disbanding is applied at P4 and the frozen P5 baseline already reflects it, which is permitted; it cannot be applied between P5 battles.

`WAR-061` A nation at zero total strength is not eliminated, is not protected, and keeps its cities, resources and account. It may rebuild. A campaign against a zero-strength nation continues until it ends by objective, surrender, settlement or expiry.

**Worked examples — recruitment arrival and the force snapshot.** All values are strength points; Food is in units.

1. **Normal existing forces.** At the opening of P3.7 the force is 200 `UNIT-INF` and 300 `UNIT-ARM`; no recruitment completes this turn. `force_snapshot = (200, 300, 0, 0)`; `ration_equivalents = 200×10 + 300×4 = 3,200`; Food demand `ceil(3,200/1,000) = 4`. Readiness `total_strength = 500` → `ceil(500×5,000/10,000) = 250` crowns, `ceil(500×200/10,000) = 10` ammunition, `ceil(500×100/10,000) = 5` gasoline. Food and readiness read the same 500/3,200 values.
2. **Recruitment completed in the previous turn.** 100 `UNIT-INF` were ordered at P4 of T−1, paid then, and complete at the opening of T's P3.7. They are added before the snapshot: `force_snapshot = (100, 0, 0, 0)`; equivalents 1,000; Food 1; readiness `total_strength = 100` → 50 crowns, 2 ammunition, 1 gasoline. The P5 baseline of T includes them.
3. **Recruitment submitted in the current turn.** 100 `UNIT-INF` are ordered at P4 of T. P3.7 of T has already run, so they are not in T's snapshot; T's Food and readiness exclude them. They enter T+1's snapshot after completion. They are not eligible for T's P5.
4. **Recruitment that fails or is cancelled.** 100 `UNIT-ARM` are ordered at P4 of T but cancelled before completion, or fail their P4 validation. They never enter any snapshot, never consume Food or readiness upkeep and are never eligible for operations. The reserved crowns and resources are released under the ordinary cancellation rule; no strength appears.
5. **A force loss at P5.** At T's P3.7 the snapshot is 200 `UNIT-INF` (`2,000` equivalents, 2 Food) and T pays for it. A P5 battle destroys 120 points, leaving 80. T's snapshot is not rewritten. T+1 opens at 80 `UNIT-INF` (`800` equivalents, `ceil(800/1,000) = 1` Food); readiness is computed from `total_strength = 80` (40 crowns, `ceil(1.6) = 2` ammunition, `ceil(0.8) = 1` gasoline). The loss reduces the next turn, not the turn that paid.
6. **The following turn's Food and readiness.** After the loss in example 5, 30 `UNIT-ARM` complete at T+1's P3.7. `force_snapshot = (80, 30, 0, 0)`; equivalents `800 + 120 = 920`; Food `ceil(920/1,000) = 1`. `total_strength = 110` → `ceil(110×5,000/10,000) = 55` crowns, `ceil(110×200/10,000) = 3` ammunition, `ceil(110×100/10,000) = 2` gasoline. Both obligations read one snapshot; no P3.0 value exists.

---

## 11. Resources and upkeep

### 11.1 Resource roles

`WAR-062` B-10 draws on exactly **five** existing B-04 resources. Four — **gasoline, ammunition, steel and aluminium** — form the operation supply bundle. The fifth, **Food**, is consumed only by the recurring military Food ration (`WAR-053a`–`WAR-053i`) and by the additional `OP-09` field ration (`WAR-053f`). Food is **not** a general bundle resource: no other operation has a Food line. B-10 creates no twelfth resource.

`WAR-063` Every military resource movement uses the B-04 ledger. B-10 registers **no new event type**: reservations write `RESERVATION_HELD`, releases write `RESERVATION_RELEASED`, P5 consumption writes `RESERVATION_CONSUMED`, P3.7 military Food and readiness upkeep write `OBLIGATION_PAID` or `OBLIGATION_CANCELLED` with a component field (`MILITARY_RATION` or `READINESS`), recruitment writes `CAPEX`, and settlement transfers write `TRANSFER_OUT`/`TRANSFER_IN`. Infrastructure damage and repair use the B-05 events `INFRASTRUCTURE_DAMAGED` and `INFRASTRUCTURE_REPAIRED` (`URB-122`); they move no inventory.

> **Reconciliation note.** `ECN-214` names a `CONSUME` event, but `ECN-165` does not register that type. B-10 does not invent it. `RESERVATION_CONSUMED` is the registered event for a reserved military cost consumed at resolution. This is recorded as `B10-C28`; B-04's register of event types is unchanged.

### 11.2 Upkeep and priority

`WAR-064` Military Food ration and readiness upkeep share `ECN-105` rank 6 with any other Prompt 10 obligation. Within rank 6 the deterministic sub-order is: **(a) military Food ration**, **(b) readiness upkeep**, (c) settlement reparations due that turn (none exist, because reparations are immediate), (d) any other B-10 obligation. Feeding the force precedes paying readiness; both precede every discretionary claim. This preserves B-04's published order and creates no new rank.

`WAR-064a` The military Food ration is charged from **unreserved** Food after P3.6. It is not reserved at acceptance, because a P3 obligation may not consume another action's reservation (`TR-070`). If the unreserved Food is below the whole demand, the whole obligation is cancelled under `ECN-106`; there is no partial payment, no negative inventory and no debt.

`WAR-064b` Readiness upkeep is charged from **unreserved** crowns, ammunition and gasoline after the ration sub-step. A ration shortfall does not consume or cancel the readiness obligation; the nation may pay both or either, and the readiness deltas are summed. Political states do not alter this order (`WAR-053i`).

`WAR-065` A cancelled readiness obligation never becomes debt, never seizes future income and never consumes another action's reservation. Only unreserved crowns and inventory can be charged.

### 11.3 Conservation

`WAR-066` B-10 never mints, destroys or hides value. Specifically:

- Operations reserve and consume existing inventory; the amounts are recorded per action.
- Units and readiness are B-10 state, not B-04 inventory; unit losses are not ledger events.
- No loot exists. No stockpile is destroyed by a raid.
- Reparations move existing value through a transfer with matched events.
- A blockade changes costs and recovery, never production, inventory or trade.
- Recruitment is a `CAPEX` outflow with no value creation.
- Every failure releases every reservation exactly once.

`WAR-067` P7 checks: total reserved OP equals the sum of live OP reservations; every consumed reservation has exactly one consumption item; total military resource outflow equals the sum of consumed and upkeep amounts; no nation has negative inventory or negative OP; a settlement transfer's two legs are equal and matched.

---

## 12. Supply and logistics

### 12.1 The mapless supply model

`WAR-068` Supply is an **inventory bundle** attached to an operation. It depends only on national inventory and the operation's requirements. It never depends on distance, route, depot, convoy, border, adjacency, port, sea lane or territory.

`WAR-069` The supply bundle is reserved at acceptance and consumed at P5. Because the reservation is protected from P3 obligations and other actions, a resolved operation cannot discover a shortage at P5. If the bundle is unavailable at acceptance, the operation is rejected with `WRF-25` and nothing is reserved.

`WAR-070` Partial execution does not exist. An operation either resolves with its full bundle or fails with no effect. A failed operation releases the full bundle.

`WAR-071` Supply denial is a B-10 state imposed by a successful `OP-01 RAID` or `OP-03 AIR_STRIKE` when the campaign objective is `OBJ-INTERDICTION`: the target pays a supply-bundle surcharge on its next turn's operations and loses 50 readiness once, when the denial is applied. Denial lasts one turn, does not stack with itself and does not destroy inventory. The surcharge is a component of the single combined modifier in `WAR-071a`, not a separate multiplication.

`WAR-071a` **One ordered, bounded modifier rule.** Supply denial and blockade are combined **once, additively, before any rounding**:

```
denial_bp    = 2,500 if SUPPLY_DENIED is active, else 0
blockade_bp  = 2,500 if BLOCKADED is active, else 0
surcharge_bp = min(5,000, denial_bp + blockade_bp)
bundle'_r    = ceil(bundle_r × (10,000 + surcharge_bp) / 10,000)   for each resource r
```

The order is fixed: read the base bundle, sum the applicable modifiers, apply the cap, apply the combined multiplier **once**, then round up once per resource. The modifiers are never multiplied together and never rounded separately. When both are active the surcharge is **+50%**, not +56.25%. The 2,500, 2,500 and 5,000 values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

| Scenario | Denial | Blockade | `surcharge_bp` | RAID 5 gasoline / 5 ammunition |
|---|---|---|---|---|
| Neither | No | No | 0 | 5 / 5 |
| Denial only | Yes | No | 2,500 | 7 / 7 |
| Blockade only | No | Yes | 2,500 | 7 / 7 |
| Both | Yes | Yes | 5,000 | 8 / 8 |
| Denial expires, blockade remains | No | Yes | 2,500 | 7 / 7 |
| Blockade applied after denial in the same turn | Yes | Yes | 5,000 | 8 / 8 |

The last two rows show that the result depends only on the states at evaluation, not on the order in which they were applied. The readiness effects are **not** part of this cap: denial applies −50 once when it is imposed, and blockade applies −25 recovery per turn at P3.7. They are different quantities and both may apply; neither is counted twice.

`WAR-072` A blockade does not stop production, delete trade or freeze inventory. It applies the combined surcharge in `WAR-071a` and the −25 readiness-recovery penalty in §9.1, and it is breakable. A blockaded nation with no denial therefore pays +25%; a blockaded nation that is also denied pays +50%, never more.

### 12.2 Supply bundles

| Operation | Gasoline | Ammunition | Steel | Aluminium |
|---|---|---|---|---|
| `OP-01 RAID` | 5 | 5 | 0 | 0 |
| `OP-02 ASSAULT` | 10 | 10 | 2 | 0 |
| `OP-03 AIR_STRIKE` | 10 | 6 | 0 | 1 |
| `OP-04 BLOCKADE` | 8 | 4 | 2 | 0 |
| `OP-05 MISSILE_STRIKE` | 6 | 12 | 0 | 2 |
| `OP-06 INTERCEPT` | 4 | 6 | 0 | 0 |
| `OP-07 FORTIFY` | 0 | 2 | 4 | 0 |
| `OP-08 BREAK_BLOCKADE` | 6 | 4 | 2 | 0 |
| `OP-09 RESUPPLY` | 4 | 2 | 0 | 0 |

All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. `OP-09 RESUPPLY` additionally consumes **4 Food** as an operational field ration and restores 100 readiness when it resolves. That 4 Food is reserved at acceptance and consumed at P5; it is distinct from, additional to and never a payment toward the recurring military Food ration in §9.3 (`WAR-053f`).

---

## 13. Complete operation catalogue

### 13.1 Master table

`WAR-073` The operation catalogue is **closed**. No hidden, event-only, administrative or future operation exists in B-10. Every operation is listed here with its full contract.

| ID | Name | Category | Target | Preconditions | OP | Unit requirement | Resolves |
|---|---|---|---|---|---|---|---|
| `OP-01` | `RAID` | Ground | Enemy nation in an active campaign | Readiness ≥ 300; INF ≥ 1 | 2 | INF 100%, ARM 50% | P5.6 |
| `OP-02` | `ASSAULT` | Ground | Enemy nation in an active campaign | Readiness ≥ 500; INF ≥ 100 strength | 3 | INF 100%, ARM 100% | P5.6 |
| `OP-03` | `AIR_STRIKE` | Air | Enemy nation in an active campaign | Readiness ≥ 500; AIR ≥ 20 strength; MIL-T3 | 3 | AIR 100% | P5.6 |
| `OP-04` | `BLOCKADE` | Naval | Enemy nation in an active campaign | Readiness ≥ 500; NAV ≥ 30 strength; MIL-T3; no active blockade by either side | 3 | NAV 100% | P5.6 |
| `OP-05` | `MISSILE_STRIKE` | Strategic | Enemy nation in an active campaign; optionally one of its B-05 cities | Readiness ≥ 500; MIL-T4 | 4 | None (national capability) | P5.6 |
| `OP-06` | `INTERCEPT` | Defensive | Conditional: next incoming air or missile attack | Readiness ≥ 300 | 1 | AIR 100% | P5.5 |
| `OP-07` | `FORTIFY` | Defensive | Self; next incoming ground attack | Readiness ≥ 300 | 2 | INF 100% | P5.5 |
| `OP-08` | `BREAK_BLOCKADE` | Defensive | Active enemy blockade on self | Readiness ≥ 500; NAV ≥ 30 strength | 2 | NAV 100% | P5.5 |
| `OP-09` | `RESUPPLY` | Sustainment | Self | Readiness < 1,000 | 1 | None | P5.5 |

All OP costs and resource bundles are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

### 13.2 Per-operation contracts

#### `OP-01 RAID`

- **Purpose:** A cheap, repeatable ground action that erodes strength and enables interdiction.
- **Effect:** Resolves one battle against the target's ground defence. On a successful result, deals losses, earns progress and applies supply denial if `OBJ-INTERDICTION` is the actor's primary or secondary objective.
- **Counter:** `OP-07 FORTIFY` raises the target's defence power by 25%; a successful defence earns `OBJ-DEFENCE` progress and counter-progress.
- **Losses:** By tier (§16). Cap 20% of engaged strength per side per battle.
- **Limits:** 3 offensive operations per side per turn; 8 progress-bearing resolutions per campaign per side.
- **Visibility:** Actor and defender see the battle report at P6; public summary after.
- **Audit:** `WRA-04` battle, `WRA-06` progress.
- **Failure:** `WRF-23` readiness, `WRF-25` supply, `WRF-26` no campaign, `WRF-21` dormancy.

#### `OP-02 ASSAULT`

- **Purpose:** The heaviest conventional ground action; the main attrition tool.
- **Effect:** Resolves one battle using full infantry and armour. A decisive result adds a one-turn `SHAKEN` state to the defender (−100 readiness).
- **Counter:** `OP-07 FORTIFY`; a successful defence adds counter-progress.
- **Losses:** By tier; attacker losses are higher on a failed assault.
- **Limits:** Requires 100 strength; 3 offensive operations per side per turn.
- **Visibility / Audit / Failure:** As `OP-01`.

#### `OP-03 AIR_STRIKE`

- **Purpose:** Air-domain action that contests air control, supports attrition and can impose interdiction.
- **Effect:** Resolves one battle against air defence. On success, damages strength, earns AIR/ATTRITION/STRIKE progress and may apply supply denial.
- **Counter:** `OP-06 INTERCEPT` raises defence power by 40% and reduces attacker power by 15%.
- **Losses:** Air losses are applied to the actor's AIR pool; defender losses to AIR first, then INF at 25% weight.
- **Limits:** 3 offensive operations; MIL-T3; 8 progress-bearing resolutions.
- **Visibility / Audit / Failure:** As `OP-01`. No city, facility or geographic target exists.

#### `OP-04 BLOCKADE`

- **Purpose:** A symbolic national condition that raises the target's operating costs and slows recovery.
- **Effect:** Resolves one naval contest. On success, the target enters `BLOCKADED` for 12 turns: +25% operation bundle cost, −25 readiness recovery. On failure, no state is applied.
- **Counter:** `OP-08 BREAK_BLOCKADE` removes the state on success.
- **Losses:** Naval strength by tier. No economic loss, no production loss and no trade deletion.
- **Limits:** One active blockade per pair; re-imposition after a break has a 12-turn cooldown.
- **Visibility:** Public state; exact naval strength private.
- **Audit:** `WRA-04`, `WRA-07` state change.
- **Failure:** `WRF-27` blockade already active or cooldown.

#### `OP-05 MISSILE_STRIKE`

- **Purpose:** A conventional strategic strike that is expensive, high-impact and can damage a named city's infrastructure without destroying the city, a facility or a population.
- **Target class:** `target_type = NATION` (default) or `CITY(city_id)`. The city must exist, belong to the target nation and be identified by B-05 `city_id`. A city is a **B-05 asset identifier, not a location**: no coordinate, distance, adjacency, border, movement or map is created. A city target is still an attack on the nation and runs the full `WAR-009` check set first (`WAR-009b`).
- **Effect:** Resolves one battle with a fixed national strike power of 2,000 plus 25% of AIR attack power. On success, damages strength, earns STRIKE/ATTRITION progress and applies −100 readiness. If the target is a city and the tier is `ATTACKER_VICTORY` or `DECISIVE_VICTORY`, §16.4 applies bounded infrastructure damage, capacity and housing recalculation, a book-value impairment and a recoverable repair path.
- **Counter:** `OP-06 INTERCEPT` — the only counter — raises defence power by 40% and reduces strike power by 15%.
- **Losses:** Defender strength; attacker loses ammunition and may lose AIR strength at 10% of the defender's loss.
- **Limits:** MIL-T4; 2 missile strikes per campaign per side; no nuclear variant. City damage is additionally capped per strike and per city per campaign (§16.4).
- **Visibility:** The strike is public at P6; exact strength and book value stay private; city infrastructure and damage are public at P6.
- **Audit:** `WRA-04`, `WRA-08` strategic strike; `INFRASTRUCTURE_DAMAGED` when a city is damaged.
- **Failure:** `WRF-28` tier or campaign limit; `WRF-36` invalid city target; `WRF-35` unfed force. No city destruction, city transfer, facility damage or direct population casualty.

#### `OP-06 INTERCEPT`

- **Purpose:** The universal air and missile counter; also a defensive objective tool.
- **Effect:** A conditional order accepted at P4. It triggers once against the first incoming air strike or missile strike in the same P5. If no such attack occurs, it expires at P7 and releases its reservations.
- **Counterplay:** Cannot itself be countered; it is the counter. It does not lock the game because it is single-use, conditional and limited to 3 per turn.
- **Losses:** Air strength by tier; a successful interception limits attacker losses to the defender's tier result.
- **Limits:** 3 conditional defensive operations per turn; one trigger per accepted order.
- **Visibility:** The defender sees the attack type and the outcome, never the attacker's exact composition.
- **Audit:** `WRA-04`, `WRA-09` interception.
- **Failure:** `WRF-23` readiness, `WRF-25` supply.

#### `OP-07 FORTIFY`

- **Purpose:** The ground counter and a bounded defensive posture.
- **Effect:** Applies one `FORTIFIED` state to the nation until the end of the current P5. The first incoming ground attack against it has the defender's power raised by 25%; the state is then consumed. It does not stack and does not carry across a boundary.
- **Counterplay:** It cannot be stacked, has no duration beyond one P5 and costs 2 OP, so it cannot create an indefinite defensive lock.
- **Losses:** None directly; the battle it modifies resolves normally.
- **Limits:** One active `FORTIFIED` state per nation; 3 defensive operations per turn.
- **Visibility:** The state is visible to the opponent as `DEFENSIVE POSTURE` without exact strength.
- **Audit:** `WRA-07`, `WRA-10` fortification.
- **Failure:** `WRF-23`, `WRF-25`.

#### `OP-08 BREAK_BLOCKADE`

- **Purpose:** The naval counter that restores normal cost and recovery.
- **Effect:** Resolves one naval contest against the blockading nation. On success, removes `BLOCKADED`, earns `OBJ-DEFENCE` progress and applies counter-progress to the blockader's `OBJ-BLOCKADE`.
- **Counterplay:** It is the counter to `OP-04`; it cannot be blocked except by the ordinary eligibility rules.
- **Losses:** Naval strength by tier.
- **Limits:** 3 defensive operations per turn; 12-turn re-imposition cooldown on the blockader.
- **Visibility / Audit / Failure:** Public state change; `WRA-04`, `WRA-07`; `WRF-23`, `WRF-25`, `WRF-29` no active blockade.

#### `OP-09 RESUPPLY`

- **Purpose:** Converts resources into readiness; the recovery operation.
- **Effect:** Restores 100 readiness (cap 1,000) and consumes **4 Food** as an operational field ration in addition to the bundle. The field ration is reserved at acceptance and consumed at P5; it is not the recurring garrison ration and never reduces or pays the P3.7 military Food obligation (`WAR-053f`–`WAR-053g`). It never exceeds the readiness cap and never creates readiness for free.
- **Counterplay:** It is not an attack and has no counter; it is limited by OP, resources and the readiness cap.
- **Losses:** None.
- **Limits:** Once per turn per nation.
- **Visibility:** Private.
- **Audit:** `WRA-11` resupply; `RESERVATION_CONSUMED` includes the 4 Food.
- **Failure:** `WRF-25`, `WRF-30` readiness already at cap, `WRF-35` only if the operation is hostile (it is not, so `WRF-35` never applies to `OP-09`).

### 13.3 Excluded and adopted categories

| Category | Disposition | Reason / owner |
|---|---|---|
| Nuclear weapons | **Rejected** | Disproportionate, no radiation model compatible with the mapless scale, would require uranium consumption and a B-04 amendment; `WFC-14` |
| Espionage / covert operations | **Excluded — no owner identified** | Not a B-10 operation and **no current or future prompt is named as its owner**. It is not transferred to Prompt 12 or to any other prompt; a future expansion needs its own owner decision, limits and validator hook. No covert action exists in B-10 |
| City destruction, deletion or ownership transfer | **Rejected** | `URB-035`: a city is permanent for the life of the nation; no capture, sale, merger or transfer |
| City infrastructure damage | **Adopted — `OP-05` only** | `WAR-109a`–`WAR-109m`; bounded, capped, recoverable and book-valued; capacity and housing recalculated; no city loss |
| Facility damage or destruction | **Not adopted — separate future design** | No current rule damages, deletes, disables or transfers a facility; adding one needs its own B-05 decision for capacity, book value and pending orders. Infrastructure damage is **not** facility damage |
| Direct population casualties, eviction or transfer | **Rejected** | No strike kills, moves or evicts people; reduced housing is applied at the next P3.8 through B-06 `DMP-031` crowding, never through a warfare casualty rule (`URB-157`, `WAR-109f`) |
| Territorial capture / occupation | **Rejected** | Mapless constraint |
| Unit movement / deployment | **Rejected** | No location exists |
| Economic looting | **Rejected** | Conservation and anti-snowball; reparations are consensual only |
| Alliance joint operations | **Rejected** | B-09 military sovereignty; no delegation, no shared OP |
| Bio, chemical or terror operations | **Rejected** | No design basis, no evidence, disproportionate |

---

## 14. Battle-resolution model

### 14.1 Architecture

`WAR-074` Battle resolution is **deterministic strength comparison with one bounded, seeded fortune roll**. It is not a hidden probability model. Every input is published in the battle report; the only unknown before resolution is the fortune roll, and its bound is disclosed.

`WAR-075` All arithmetic is integer or fixed-point basis points. There is no floating point. Each formula's rounding is defined in the formula register.

### 14.2 Power calculation

`WAR-076` **Raw force** is `Σ(strength_points × strength_per_point)` over the engaging unit types.

`WAR-077` **Attack power** is:

```
attack_force = Σ_t floor(strength_points_t × strength_per_point_t × attack_factor_bp_t / 10000)
attack_power = floor(attack_force × readiness_factor_bp / 10000)
attack_power = floor(attack_power × counter_attack_bp / 10000)
```

Per-type aggregation and every rounding step are defined in `F-WR-021` of the [formula register](17_warfare_formula_register.md).

`WAR-078` **Defence power** is the same sequence using `defence_factor_bp`, the defender's readiness factor and `counter_defence_bp`.

`WAR-079` `readiness_factor_bp = 5000 + 5 × readiness`, giving 5,000 at readiness 0 and 10,000 at 1,000. Readiness therefore scales combat power between 50% and 100%; it can never exceed 100% and is not an economic multiplier.

`WAR-080` `OP-05 MISSILE_STRIKE` uses `national_strike_power = 2000 + floor(air_attack_power × 2500 / 10000)` and has no raw-force term. The 2,000 and 25% are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

### 14.3 Ratio, fortune and tiers

`WAR-081` `base_ratio_bp = floor(attack_power × 10000 / (attack_power + defence_power))`. If both powers are zero, `base_ratio_bp = 5000`.

`WAR-082` `fortune_bp = seeded_integer(seed, battle_id, −500, +500)`. The seed is the frozen turn digest seed already used by B-02's seeded lottery (`TR-046`); the range is closed and integer. The seed, battle identifier and resulting roll are recorded in the battle report after resolution. No client, player or administrator chooses or sees the roll before P5.

`WAR-083` `effective_ratio_bp = clamp(base_ratio_bp + fortune_bp, 0, 10000)`.

| Effective ratio | Tier | Meaning |
|---|---|---|
| 0–3,999 | `ATTACKER_DEFEAT` | Defender holds; attacker loses more |
| 4,000–4,999 | `REPULSED` | Defender advantage; attacker loses more |
| 5,000–5,999 | `CONTESTED` | No objective progress; both lose |
| 6,000–7,499 | `ATTACKER_VICTORY` | Attacker gains progress |
| 7,500–10,000 | `DECISIVE_VICTORY` | Attacker gains progress and a state effect |

All boundaries are inclusive at the lower bound. The tier thresholds are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

`WAR-084` A `CONTESTED` result never grants objective progress and never removes `BLOCKADED` or `FORTIFIED`; it only applies losses. A `DECISIVE_VICTORY` on `OP-02 ASSAULT` applies `SHAKEN` (−100 readiness to the defender); on `OP-05 MISSILE_STRIKE` it applies −100 readiness; on `OP-04 BLOCKADE` it applies the blockade state.

### 14.4 Counters

| Counter | Condition | Effect |
|---|---|---|
| `OP-07 FORTIFY` | Active against an incoming ground attack | `counter_defence_bp = 12500` for the first ground attack; then consumed |
| `OP-06 INTERCEPT` | Triggered against an incoming air or missile strike | `counter_defence_bp = 14000`, `counter_attack_bp = 8500` |
| `OP-08 BREAK_BLOCKADE` | Against an active blockade | `counter_attack_bp = 7000` for the blockader's defence contest |
| No counter | Otherwise | `10000` on both sides |

All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. Counters never stack; the strongest applicable counter applies, and a second `FORTIFY` in the same P5 is rejected with `WRF-31`.

### 14.5 Pre-battle disclosure

`WAR-085` Before confirming an offensive operation, the attacker sees:

- its own exact attack power;
- the opponent's **threat band** (`LOW`/`MODERATE`/`HIGH`/`SEVERE`) and the defence-power range implied by that band;
- the possible tier range for the disclosed fortune bound;
- the exact OP, resource and readiness costs;
- the declared counter or counters the defender may use;
- every block reason, if any.

`WAR-086` The attacker never sees the opponent's exact strength, readiness or inventory. The threat band is computed from exact server state but exposed only as one of four bands:

| Band | Opponent force ratio to the viewer's force |
|---|---|
| `LOW` | below 0.75 |
| `MODERATE` | 0.75 to below 1.25 |
| `HIGH` | 1.25 to below 2.00 |
| `SEVERE` | 2.00 and above |

`WAR-087` The defender sees, when a campaign is active, its own threat band relative to the opponent and, at P6, the battle report. The defender does not see the incoming operation before P5, which is why conditional defensive orders exist.

`WAR-088` After resolution both parties receive a **battle report**: battle identifier, turn, operation type, exact engaged strength by type, readiness, counters, powers, base ratio, fortune roll, effective ratio, tier, losses, progress gained, counter-progress and the reason. The public summary omits exact strength and inventory and shows only the tier, the operation type and a loss band.

---

## 15. Simultaneous combat and deterministic ordering

### 15.1 B-10's internal P5 order

`WAR-089` B-10 fixes the following order inside B-02's P5 phase. Every step is checkpointed.

| Step | Action |
|---|---|
| `P5.0` | Load the frozen campaign and operation set; verify the P5 idempotency manifest |
| `P5.1` | Validate and resolve pending declarations in `(submitted_at, action_id)` order; create campaigns |
| `P5.2` | Apply campaign deadline, inactivity expiry and dormancy suspension |
| `P5.3` | Complete accepted settlements atomically; end their campaigns |
| `P5.4` | Validate every remaining accepted operation against execution-time state; fail closed and release |
| `P5.5` | Snapshot readiness and force; resolve `OP-09 RESUPPLY`, `OP-07 FORTIFY` and arm `OP-06 INTERCEPT` |
| `P5.6` | Resolve offensive operations in the order below; each battle applies losses immediately |
| `P5.7` | Resolve `OP-08 BREAK_BLOCKADE` as a defensive offensive contest |
| `P5.8` | Apply objective progress and counter-progress |
| `P5.9` | Write battle, state and settlement audit records; compute the P6 victory input |

`WAR-090` Offensive order key: `(campaign_priority, attacker_nation_id, operation_priority, submitted_at, action_id)` where `campaign_priority` is the campaign identifier in ascending order (deterministic and stable) and `operation_priority` is `BLOCKADE` 1, `MISSILE_STRIKE` 2, `AIR_STRIKE` 3, `ASSAULT` 4, `RAID` 5. The key is total; no two operations share it.

### 15.2 Frozen baseline and damage carry

`WAR-091` All operations in a turn read the same **frozen P5 baseline** (`TR-050`). Earlier battles' losses are applied as a `damage_carry` subtraction in the order above, so a strength point cannot fight twice after being destroyed. This is "same baseline, applied in order", not a re-read of mutated state.

`WAR-092` The second and later attacks by the same attacker on the same target use `available_strength = max(0, baseline_strength − cumulative_losses_this_turn)` and `available_defence = max(0, baseline_defence − cumulative_losses_this_turn)`. Readiness is read from the baseline and is not reduced by earlier battles in the same turn.

`WAR-093` A target that reaches zero available strength in a turn can still be attacked; the attack resolves against a defence power of zero and normally achieves a decisive tier. This cannot destroy more strength than exists. The campaign still does not end until victory, surrender, settlement or expiry.

### 15.3 Dependencies and simultaneous actions

`WAR-094` B-10 has **one** declared dependency edge: `OP-06 INTERCEPT` depends on an incoming air or missile operation. It is a conditional order, not a chained action; if no qualifying attack exists it expires with no effect and no cost beyond its released reservation.

`WAR-095` No other operation supports, boosts, chains to or depends on another. Two offensive operations are independent even when they share a target. There is no combined-arms bonus and no declared-order edge that can silently retarget.

`WAR-096` An operation whose target changed state so that it is no longer valid fails with `WRF-26`; it never retargets (`TR-053`). A stale target is a failure, not a substitution.

### 15.4 Idempotency and recovery

`WAR-097` Every submission carries a client idempotency key scoped to the actor. A duplicate key returns the original receipt and performs no second reservation.

`WAR-098` Resolution is keyed by `(turn_id, operation_id)` and `(turn_id, battle_id)`. Each battle writes exactly one `APPLIED` marker and one set of ledger items. A retry after a crash reads the marker and skips the battle.

`WAR-099` Interrupted P5 recovery (`TR-043`) resumes at the last completed checkpoint. Before resuming a battle the resolver verifies that its `APPLIED` marker and all of its ledger items are either all present or all absent. A partially written battle is not possible because each battle is one transaction; if the transaction is absent the battle is re-run against the same frozen baseline and the same seed, producing the same result.

`WAR-100` P7 checks that the number of applied battles equals the number of resolved operations, that no `operation_id` has two battle records, and that the sum of applied losses equals the recorded cumulative loss per nation.

---

## 16. Losses and damage

### 16.1 What can be lost

`WAR-101` B-10 losses are exactly: **military strength points**, **readiness**, **temporary states** (`BLOCKADED`, `FORTIFIED`, `SHAKEN`, `SUPPLY_DENIED`, `RATION_SHORT`), and — only through a successful city-targeted `OP-05 MISSILE_STRIKE` — **city infrastructure levels** with their capacity, housing and book-value consequences. Nothing else can be lost.

`WAR-102` No **city** can be destroyed, deleted, captured, renamed out of existence, merged or transferred. No **facility** can be damaged, destroyed, deleted, disabled or transferred. No research, technology, resource stock, crown, population, approval, stability, legitimacy or account can be damaged, destroyed, captured or transferred by a battle. City infrastructure is the **only** B-05 attribute a strike may reduce, and only under §16.4. Direct population casualties, eviction, starvation caused by a strike and population transfer are prohibited. `URB-157` is amended for infrastructure damage only; every other protection in it is preserved.

`WAR-103` A nation at zero strength keeps everything else and is not eliminated. There is no "defeat deletes the nation" rule.

### 16.2 Loss rates

| Tier | Attacker loss (bp of engaged) | Defender loss (bp of engaged) |
|---|---|---|
| `ATTACKER_DEFEAT` | 1,500 | 500 |
| `REPULSED` | 1,000 | 700 |
| `CONTESTED` | 800 | 800 |
| `ATTACKER_VICTORY` | 700 | 1,000 |
| `DECISIVE_VICTORY` | 500 | 1,500 |

All values are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

`WAR-104` Losses are computed per engaged unit type, applied proportionally with the largest-remainder method, and floored to whole strength points. Tie-break for the remainder is unit-type identifier order (`UNIT-AIR`, `UNIT-ARM`, `UNIT-INF`, `UNIT-NAV`).

`WAR-105` Per-battle cap: a side cannot lose more than **20%** of its engaged strength in one battle. Campaign cap: a side cannot lose more than **60%** of its strength at campaign start across the campaign. Once the campaign cap is reached, further battles apply zero strength loss to that side (readiness loss still applies) and the battle report states `LOSS_CAP_REACHED`. This is the anti-snowball bound.

`WAR-106` Readiness loss is 25 per resolved battle for each participating side, applied after the battle, floored at zero. It is not capped by the strength-loss cap.

### 16.3 Destruction and recovery

`WAR-107` Strength points removed by losses are destroyed. They are not prisoners, not recoverable, not salvage and not returned by a settlement. They may be rebuilt only through recruitment.

`WAR-108` There is no separate "wounded", "damaged" or "repairing" unit state. A strength pool is a single integer; a battle reduces it.

`WAR-109` A campaign's cumulative loss counter resets only when a new campaign begins. It is never reset by a boundary, a blockade or a settlement proposal.

### 16.4 City targeting and infrastructure damage

`WAR-109a` **Only `OP-05 MISSILE_STRIKE` may carry a city target.** The operation carries `target_type = NATION` or `target_type = CITY(city_id)`. The city must exist, belong to the target nation and be one of that nation's B-05 cities. No other operation, counter, settlement term, raid, assault, air strike or blockade may target a city. A city is a B-05 asset identifier, never a location: the rule creates no coordinate, distance, adjacency, border, movement, front or map.

`WAR-109b` **A city target is not a shortcut.** The strike is an attack on the target **nation**. It runs the complete `WAR-009` offensive check set — authority, target, restricted pair, protection, same-Alliance, covered `AT-E01` NAP, political state, campaign, OP, resources, readiness and the Food-shortage state — before the city check. The city check can only add a rejection (`WRF-36`); it can never waive a national block. The canonical validator records the target nation as the defender and the city as the affected asset.

`WAR-109c` **When damage applies.** Infrastructure damage applies only when the strike resolves at tier `ATTACKER_VICTORY` or `DECISIVE_VICTORY`. `CONTESTED`, `REPULSED` and `ATTACKER_DEFEAT` apply no infrastructure damage; a strike blocked at submission, P2 or pre-P5 applies none; a successful `INTERCEPT` applies none. The battle itself still resolves normally with strength losses, readiness loss and objective progress.

`WAR-109d` **Damage formula.** Let `I` be the city's infrastructure immediately before the strike, after every P4.1 completion of the same turn.

```
removed_raw   = ceil(I × 500 / 10,000)                  (5% of the current level, rounded up)
removed       = min(removed_raw, 20, campaign_headroom) (never more than 20 per strike)
I_after       = max(10, I − removed)
removed       = I − I_after                              (the actual decrease, after the floor)
```

The 5%, 20 and floor 10 are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. `campaign_headroom` is the remaining per-city campaign allowance in `WAR-109e`. A strike against a city already at infrastructure 10 removes 0 and writes no damage event, but the battle still resolves.

`WAR-109e` **Caps.** Per city per campaign, cumulative infrastructure damage cannot exceed `floor(I_campaign_start × 3,000 / 10,000)` — 30% of the city's infrastructure at the campaign's start, rounded down. Once the cap is reached, further city strikes deal 0 infrastructure damage and still resolve the battle. The cap is per city and is never pooled across cities. The 30% value is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. A new campaign against the same nation starts a new cap from the city's then-current level; it does not inherit the old campaign's remaining allowance.

`WAR-109f` **Capacity and housing recalculated; no population change at P5.** Immediately after the damage, B-05 recomputes the city's development capacity and housing from the new level (`URB-041`, `URB-042`):

```
capacity = 10 + floor(I_after / 10)
housing  = 45,000 + 100 × I_after + 25,000 × civic_centres
```

No facility is deleted, moved, disabled or transferred. If `Σ facility DC > capacity`, the city enters **capacity overdraw**: every existing facility is preserved and remains owned and operable, but new construction or upgrade orders that would increase the facility count or DC are blocked until capacity is at least the used DC. The deficit is displayed. The reduced capacity is the **stored state**; construction eligibility uses the effective-capacity boundary in `WAR-109m`, so a level repaired at P4.1 of turn T supports the new capacity from T+1, not for an order accepted in T.

A housing shortfall creates **no** population change at P5: infrastructure damage does not kill, evict, delete or transfer a person, and it creates no warfare population-loss formula. `housing_after` becomes the housing input for the **next P3.8**, where B-06 `DMP-034` computes population once. If national population exceeds national housing at that boundary, the existing `DMP-031` crowding rule applies, not a paused-growth stand-in:

```
natural   = population + floor(population × growth_bp / 10,000)      (DMP-028, floored)
excess    = max(0, population − housing)
decline   = max(ceil(excess / 10), max(0, population − natural))
population_next = max(1,000, population − decline)                   (F-PD-002 floor)
```

The 10%-of-excess rounded-up decline, the natural-decline comparison and the 1,000 floor are B-06's; B-10 adds no second demographic rule. A later repair raises housing and changes the next applicable P3.8 calculation; it does not retroactively undo a decline already settled. A lower `total_infrastructure` may also lower the national force cap and development tier (§10.3, `WAR-055`); existing strength is never destroyed and no unit is disbanded, but recruitment is blocked until strength is within the cap and the tier is restored.

`WAR-109g` **Book-value impairment is infrastructure-only.** B-10 does not use total city book value. B-05 maintains a city infrastructure subledger (`URB-118a`):

```
infrastructure_gross_capital(city)        = Σ completed UPGRADE_INFRASTRUCTURE lots' capitalized cost
infrastructure_accumulated_impairment(city)
infrastructure_carrying_value(city)       = gross − accumulated
fixed_asset_book_value                    = Σ_city infrastructure_carrying_value
                                          + Σ other recognized fixed assets (facilities and other assets)
```

The initial capital at 50 and a new city at 10 form a **zero-cost opening lot**: their infrastructure was granted, not purchased, so their capitalized basis is 0 and their impairment is 0. This is an accounting convention, not a claim that the levels are worthless. Facilities and other city assets are **not** part of `infrastructure_carrying_value` and are never impaired by infrastructure damage; a city with no purchased infrastructure levels records a level loss and a 0 impairment.

The damage impairment is:

```
impaired = min(infrastructure_carrying_value_before,
               floor(infrastructure_carrying_value_before × removed / I_before))
infrastructure_accumulated_impairment += impaired
infrastructure_carrying_value_after = before − impaired
fixed_asset_book_value              −= impaired
```

`I_before` is `I_combat` from `WAR-109m` — the post-P4.1 level the P5 battle actually reads, never a stale opening value. Impairment creates no expense, no sale, no refund and no new ledger type, and nothing is transferred to the attacker. Repeated damage reads the **post-impairment carrying value**, so it cannot impair more than remains; `accumulated ≤ gross` is an invariant. A unique `damage_event_id = (turn_id, strike_action_id, city_id)` makes application idempotent: re-running the same strike after an interruption writes no second level loss and no second impairment. `INFRASTRUCTURE_DAMAGED` records the city, `I_before`, `removed`, `I_after`, the impairment, the campaign cumulative and the action.

`WAR-109h` **Repair cost and capitalization are B-05's.** Repair is not a B-10 operation, costs no OP and is not blocked by an active campaign. A repair order names one city and restores `n` levels, where `1 ≤ n ≤ min(10, 500 − I, unrepaired_levels)`; `unrepaired_levels` is the city's recorded cumulative damage not yet restored. The cost is exactly B-05's infrastructure cost, with **no material charge and no second discount**:

```
base_repair_cost = Σ_{j=I}^{I+n−1} (8 + floor(j / 10))                 (URB-043)
repair_cost      = ceil(base_repair_cost × 9,000 / 10,000)             (URB-044, only if Civil Survey is owned)
repair_cost      = base_repair_cost                                    (otherwise)
```

`repair_cost` is reserved from crowns at acceptance and charged as **capex** at P4.1. On completion, B-05 adds a new infrastructure lot with `levels_added = n` and `capitalized_cost = repair_cost` (`URB-118a`): `infrastructure_gross_capital += repair_cost`; `infrastructure_accumulated_impairment` is **unchanged**; `infrastructure_carrying_value += repair_cost`; `fixed_asset_book_value += repair_cost`. Repair therefore capitalizes the new spend and does **not** reverse the impairment of the levels that were destroyed; it never restores more value than the cost actually paid. The new capacity reduces `CAPACITY_OVERDRAWN` by the increase in `capacity(I_after_repair)`, and the overdraw flag clears at the P4.1 check in which `overdrawn_dc = 0` (`URB-051a`). `INFRASTRUCTURE_REPAIRED` records the city, levels, cost, `I_before` and `I_after_repair`, keyed on `order_id`; a retry of the same order is idempotent. A repair that is accepted but fails at P4.1 heals nothing, charges nothing and releases its reservation; a new order may be submitted later. Repair cannot create a city, add infrastructure above 500, or repair damage that has not occurred.

`WAR-109i` **P4.1 before P5; the named snapshots.** P4.1 construction and repair complete before the P5 baseline is frozen. A completed repair is physically present for that turn's P5 battle and is measured by the strike, but its capacity and housing become effective on B-05's next-turn boundary (`WAR-109m`). P5 damage never retroactively undoes a P4.1 completion, and a P4.1 repair never heals damage inflicted later in the same P5. If a construction or repair order and a strike affect the same city in one turn, the order applies first and the strike is computed on the post-order level. The authoritative values are named once in `WAR-109m`; no rule may use an unnamed "current level".

`WAR-109m` **Authoritative infrastructure, capacity, housing and book-value snapshots.** *Provisional (REQ-700–REQ-703).* The following values are distinct and deterministic. They preserve B-02's P0–P7 sequence and B-05's P4.1 boundary; no global phase is added.

| Value | Definition | Written at | Read by |
|---|---|---|---|
| `I_open(T)` | Infrastructure at the start of turn T = `I_post_P5(T−1)` | Prior P5 / turn opening | Acceptance and P2 of construction/repair; `housing_population(T)` |
| `I_pre(T)` | `= I_open(T)` at the start of P4.1, before any P4.1 order applies | P4.1 start | P4.1 validation |
| `I_post_P4_1(T)` | After every P4.1 upgrade or repair that completes in T | P4.1 | P5 combat |
| `I_combat(T)` | `= I_post_P4_1(T)`; the pre-strike level used by `F-WR-037` | P5 battle start | Damage formula and impairment denominator |
| `I_post_P5(T)` | `= I_combat(T) − removed`, never below 10 | P5 damage | `I_open(T+1)`; P6 disclosure |
| `capacity_construction(T)` | `= 10 + floor(I_open(T) / 10)` | Acceptance/P2 of T | Construction DC validation in T |
| `capacity_effective(T+1)` | `= 10 + floor(I_post_P5(T) / 10)` | T+1 opening | Construction DC validation in T+1 |
| `housing_population(T)` | `= 45,000 + 100 × I_open(T) + 25,000 × civic_centres` | P3.8 of T | B-06 population and `DMP-031` crowding at P3.8 of T |
| `housing_effective(T+1)` | `= 45,000 + 100 × I_post_P5(T) + 25,000 × civic_centres` | T+1 opening | B-06 at P3.8 of T+1 |
| `BV_post_P4_1(T)` | Infrastructure carrying after repair capitalization | P4.1 of T | Next applicable P3.8 wealth |
| `BV_post_P5(T)` | `BV_post_P4_1(T)` after impairment | P5 of T | P3.8 of T+1 wealth; `I_open(T+1)` related records |

The reconciliation of "available next turn" with the same-turn P5 rule is exact: **P5 combat reads the physical post-P4.1 level (`I_combat`); construction capacity and population housing read the derived values at their own effective boundaries.** A repair at P4.1 of T is therefore in the city when T's strike resolves, yet its added capacity and housing support T+1's construction and P3.8 population, not T's. A P5 strike in T is reflected in T+1's `I_open`, `capacity_effective`, `housing_effective` and `BV_post_P5`; it cannot change T's already-completed P3.8 population. National wealth at a P3.8 uses the book value written by the prior turn's P5 and P4.1, because P4.1 and P5 of the current turn occur after P3.8.

**Worked examples — infrastructure accounting and timing.** All crown values are exact; no discount is applied unless stated.

*Accounting example.* City A starts at `I = 50` with a zero-cost opening lot. At P4.1 of turn 100 it buys 50 → 60: `base = 10 × 13 = 130` crowns, no materials; new lot 10 levels, gross 130, accumulated 0, carrying 130. A separately purchased facility has book value 5,000. National fixed assets = 130 + 5,000 = **5,130**. At P5 of turn 100 a victorious strike removes `ceil(60 × 500/10,000) = 3` levels (`campaign_headroom 18`, `I − 10 = 50`): `impaired = min(130, floor(130 × 3/60)) = 6`; accumulated 6, carrying **124**, `I = 57`; national fixed assets = 124 + 5,000 = **5,124**. The facility remains **5,000** in both steps; it is not in the infrastructure subledger and cannot be impaired by this event. At P4.1 of turn 101 the nation repairs 3 levels at `I = 57`: `base = 3 × (8 + floor(57/10)) = 3 × 13 = 39`; no Civil Survey, so 39 crowns; new lot 3 levels at 39, gross 169, accumulated still 6, carrying **163**, `I = 60`; national fixed assets = 163 + 5,000 = **5,163**. Repair capitalized its cost and did not reverse the 6 impairment. A second strike in turn 101 removing 3 at `I = 60` impairs `floor(163 × 3/60) = 8`, leaving accumulated 14 and carrying **155** — never above gross 169. A city with only its zero-cost initial 50 levels records impairment 0 on any damage and still records the level loss.

*Timing examples.*

1. **Repair at P4.1, no P5 attack.** `I_open = 57`; repair 3 → `I_post_P4_1 = I_combat = 60`; no damage → `I_post_P5 = 60`. `capacity_construction(T) = 10 + floor(57/10) = 15`; `housing_population(T) = 45,000 + 5,700 = 50,700`; T+1: capacity 16, housing 51,000. `BV_post_P4_1 = BV_post_P5 = 163`.
2. **Repair followed by a successful strike.** `I_open = 57`; repair → 60; strike removes 3 → `I_post_P5 = 57`; `capacity_construction(T) = 15`; `housing_population(T) = 50,700`; T+1 capacity 15, housing 50,700. Book value 163 → impairment `floor(163 × 3/60) = 8` → 155.
3. **Repair followed by an intercepted strike.** Repair → 60; a successful `INTERCEPT` applies no damage (`WAR-109c`), so `I_post_P5 = 60`; T+1 capacity 16, housing 51,000; book value stays 163.
4. **Construction before repair.** In T, `I_open = 57` gives capacity 15; used DC is 14 and a facility order needs 2, so `14 + 2 > 15` and the order is rejected at submission/P2 even though a 3-level repair is also ordered. The repaired capacity (16) is effective at T+1, not for an order accepted in T (`URB-046`).
5. **Construction submitted after damage.** A P5 strike in T leaves `I_post_P5 = 57`, effective at T+1. In T+1, `capacity_construction = 15`; the same 14 + 2 order still fails. Repairing 3 levels at P4.1 of T+1 does not validate the order in T+1; it can be submitted in T+2, when `capacity_effective = 16`.
6. **Two damage events in the same turn.** If the operation rules permit two victorious strikes on one city in one P5, they resolve sequentially: the first uses `I_combat` and writes `I_1 = I_combat − removed_1`; the second uses `I_1` as its `I_before`, with `campaign_headroom` reduced by `removed_1`, and impairs the carrying value after the first event. The campaign cap is shared and the floor still binds. If the rules do not permit a second strike, it is rejected before execution and no second damage exists.
7. **Interrupted P5 and retry.** If P5 is interrupted after the damage event is written but before commit, recovery resumes from the P5 checkpoint and the `damage_event_id` makes the retry idempotent: no second level removal and no second impairment. If it is interrupted before the event is written, the retry applies it exactly once. The stored `I_post_P5` and `BV_post_P5` are authoritative for T+1.

*Housing example.* A single-city nation has population 50,000, `I = 50`, no civic centre, so housing is 50,000. A P5 strike in T removes 10 levels → `I_post_P5 = 40`, housing **49,000**; no person is harmed at P5. At P3.8 of T+1, with the nation fed and `growth_bp = 50` (provisional illustration), `natural = 50,000 + floor(50,000 × 50/10,000) = 50,250`; `excess = 1,000`; `decline = max(ceil(1,000/10), max(0, 50,000 − 50,250)) = max(100, 0) = 100`; `population_next = max(1,000, 49,900) = 49,900`. If nothing changes, the next turn's excess is 900 and the decline 90 → 49,810. If the nation repairs to `I = 50` at P4.1 of the next turn, housing returns to 50,000; at the following P3.8 population 49,810 is below housing, so `excess = 0`, no crowding decline applies, and growth resumes under `DMP-028`. If hunger makes `natural` 49,500, the decline is `max(100, 500) = 500` — the natural decline dominates, exactly as `DMP-031` states. The 1,000 floor applies to every path.

`WAR-109j` **Prohibitions.** City destruction, deletion, capture, transfer, sale, merger, renaming out of existence or ownership change is prohibited. Facility destruction, deletion, disablement or transfer is prohibited and is **not** created by infrastructure damage. Direct population casualties, eviction, strike-caused starvation and population transfer are prohibited. Infrastructure cannot fall below 10. A city not owned by the target nation cannot be targeted. A city cannot be targeted outside an active campaign.

`WAR-109k` **Visibility and audit.** City identity, infrastructure before and after, removed levels and the campaign cumulative are public at P6. Exact book value, exact force and inventory remain private. The battle report names the city and the removed levels. `WRA-08` is written for the strike and `INFRASTRUCTURE_DAMAGED` for the damage. Repair writes `INFRASTRUCTURE_REPAIRED` and a `CAPEX` ledger entry.

`WAR-109l` **Failure codes.** `WRF-36` rejects an invalid city target: the city does not exist, does not belong to the target nation, or the operation is not `OP-05`. A city at the infrastructure floor or at its campaign cap is **not** a rejection; the strike resolves and deals 0 infrastructure damage. An invalid repair order is `WRF-37` and releases its reservation.

---

## 17. Recovery and repair

### 17.1 Readiness recovery

`WAR-110` Readiness recovers by +50 at P3.7 when readiness upkeep is paid, by +100 through a resolved `OP-09 RESUPPLY`, and by nothing else. It is capped at 1,000 and never recovers automatically while blockaded beyond the −25 penalty.

`WAR-111` Readiness is not repaired by Crowns alone. `RESUPPLY` requires OP and resources, so readiness has an action cost as well as an economic one.

### 17.2 Force recovery

`WAR-112` Destroyed strength is replaced only by recruitment under §10.3. Recruitment is capped by training capacity, force cap and single-type share. There is no instant rebuild, no paid instant-finish and no catch-up multiplier.

`WAR-113` A defeated nation rebuilds at the same rates as a victor. It receives no hidden recovery bonus and no extra protection. Its advantage is that its opponent also bears losses, has spent OP and resources, and may face its own campaign limits.

`WAR-114` A nation may begin a new campaign while below its force cap. There is no minimum strength to declare, but the readiness and unit gates still apply.

---

## 18. Protection and counterplay

### 18.1 Protection layers

`WAR-115` B-10 creates **no new protection state and no new protection duration**. The only protections are B-03's:

| Layer | Source | B-10 treatment |
|---|---|---|
| Newcomer protection | `ONB-019`/`ONB-020`, 7 days/84 turns, account-scoped, once | Blocks declaration and every offensive operation; rechecked at P2 and P5 |
| Dormancy | `D-028`, 14 days/168 turns | Suspends campaigns; blocks all targeting |
| Restricted pair | `NET-025`/`NET-026` | Blocks declaration and every hostile operation |
| National NAP | `DP-T01`, 360 turns | Blocks declaration only |
| Same-Alliance ban | `ALL-206`–`ALL-208` | Blocks declaration and every hostile operation |
| Alliance NAP | `AT-T01`/`AT-E01` | Blocks declaration and every hostile operation for covered pairs |

`WAR-116` Protection expiry between acceptance and execution is handled by the P2 and P5 rechecks: if protection is still active at either point, the operation fails closed with `WRF-05` and releases everything. If it expires before P5, the operation may proceed. The execution-time state is authoritative.

`WAR-116a` **No stale protection snapshot.** The P2 result is evidence, not a verdict. At the immediate pre-P5 check the validator reads the current protection state:

- Protection **becomes active** after P2 (for example a newcomer protection begins or an `AT-E01` NAP is registered): the previously accepted operation fails at pre-P5 with `WRF-05`, and every OP, crown and resource reservation is released. It does not resolve because P2 passed.
- Protection **expires** after P2: an operation that passed P2 may proceed. An operation already failed at P2 stays failed and released; expiry does not revive it, and the actor must submit a new action.
- Dormancy follows the same rule: it blocks at the moment of execution even if the target was awake at P2.

`WAR-117` A protected or dormant nation's own accepted defensive operations fail and release; protection is not a way to spend OP while immune.

### 18.2 Counterplay guarantees

`WAR-118` Every offensive operation has at least one declared counter, and every counter is usable under a stated condition:

| Offensive | Counter | Condition | Bound |
|---|---|---|---|
| `RAID` | `FORTIFY` | Own nation, readiness ≥ 300 | One state, one P5, consumed on first use |
| `ASSAULT` | `FORTIFY` | Same | Same |
| `AIR_STRIKE` | `INTERCEPT` | Conditional on an incoming air attack | One trigger per order, 3 per turn |
| `MISSILE_STRIKE` | `INTERCEPT` | Conditional on an incoming missile attack | Same |
| `BLOCKADE` | `BREAK_BLOCKADE` | Own nation is blockaded, NAV ≥ 30 | 12-turn re-imposition cooldown |

`WAR-119` No counter creates an infinite defensive lock: `FORTIFY` lasts one P5 and cannot stack; `INTERCEPT` triggers once and expires; `BREAK_BLOCKADE` is an ordinary contest with losses and a cooldown on re-imposition. A defender cannot become permanently unattackable through counters.

`WAR-120` Counterplay never bypasses a protection, pair or treaty check. A counter is itself an operation and passes the cumulative validator where it is hostile (`BREAK_BLOCKADE`).

---

## 19. Ceasefires and peace

### 19.1 Mutual ceasefire

`WAR-121` Either owner may propose a **mutual ceasefire** at any time while the campaign is `ACTIVE`. The other owner may accept or reject. Acceptance ends the campaign at the next P5 as `MUTUAL_PEACE` with outcome `DRAW`, no reparations, no exclusion and no protection.

`WAR-122` A ceasefire proposal expires after 12 turns if unanswered. A rejected or expired proposal creates no cooldown and no record beyond the proposal event.

`WAR-123` A ceasefire cannot be proposed by an Alliance, an office, a treaty or an administrator. Only a party's authenticated owner may propose or accept.

### 19.2 Mutual peace with terms

`WAR-124` "Peace with terms" is the **settlement** object in §20. A ceasefire is the term-free version. There is no third peace mechanism.

---

## 20. Surrender and negotiated settlement

### 20.1 The settlement object

`WAR-125` A settlement belongs to one campaign and has these states: `PROPOSED`, `COUNTERED`, `ACCEPTED`, `REJECTED`, `WITHDRAWN`, `EXPIRED`, `COMPLETED`, `FAILED`.

| State | Entry | Exit |
|---|---|---|
| `PROPOSED` | One owner submits terms | Accept, reject, counter, withdraw, expire |
| `COUNTERED` | The other owner submits different terms | Accept, reject, withdraw, expire |
| `ACCEPTED` | Both owners accept the exact version | P5 `COMPLETED` or `FAILED` |
| `REJECTED` / `WITHDRAWN` / `EXPIRED` | Terminal without effect | — |
| `COMPLETED` | Transfer applied atomically | — |
| `FAILED` | Balance or state changed at P5 | Campaign returns to `ACTIVE` |

`WAR-126` Terms are immutable after submission. A change requires a new proposal. There is at most one live settlement per campaign.

`WAR-127` A proposal expires after 12 turns. A counter has the same window. There is no automatic acceptance and silence never accepts.

### 20.2 Permitted terms

`WAR-128` Only these terms exist. No other term may be proposed or enforced.

| Term | Meaning | Enforceable |
|---|---|---|
| `TERM_CEASEFIRE` | End the war, no transfers | Yes |
| `TERM_REPARATION_CROWNS` | Payer transfers a fixed crown amount at P5 | Yes, atomic |
| `TERM_REPARATION_RESOURCE` | Payer transfers a fixed quantity of one resource at P5 | Yes, atomic |
| `TERM_DISARMAMENT` | Payer disbands a fixed number of strength points at P5 | Yes, atomic |
| `TERM_EXCLUSION` | The pair cannot declare on each other for 84 turns | Yes |
| `TERM_WHITE_PEACE` | End the war with no fault or transfer | Yes |

All durations and caps are **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

`WAR-129` **Prohibited terms** (rejected, never enforceable): city or facility transfer or deletion; population transfer; account deletion; real-world payment; Alliance treasury contribution; Alliance obligation without the affected nation owner's separate consent; forced treaty signature; future-income garnishment; debt; resource creation; transfer of a restricted-pair right; anything that would violate B-03, B-04, B-05 or B-09.

`WAR-130` A term that requires a nation to join, leave or act through an Alliance is invalid. B-10 cannot create an Alliance obligation.

### 20.3 Surrender

`WAR-131` An owner may **surrender** unilaterally. Surrender is a settlement with `TERM_CEASEFIRE` only: the campaign ends at the next P5 as `SURRENDER`, the opponent receives a `LIMITED_VICTORY`, and there are no transfers, no disarmament and no exclusion unless the victor separately offers and the loser separately accepts a negotiated settlement.

`WAR-132` Surrender cannot be refused. It is the guaranteed off-ramp that makes the UD-032 reroll block escapable.

`WAR-133` A surrendered nation is not protected, not deleted and not penalised beyond the loss record. It may declare again when its slots and the settlement terms allow.

### 20.4 Enforcement

`WAR-134` A settlement is enforced only by its own terms at P5. There is no ongoing enforcement body, no automatic penalty for a future breach and no administrator discretion.

`WAR-135` `TERM_EXCLUSION` is enforced by the declaration validator: while `current_turn < until_turn`, a declaration between the pair fails with `WRF-32` at submission, P2 and P5. It is a B-10 war rule, not a B-08 treaty and not an Alliance treaty.

`WAR-136` `TERM_DISARMAMENT` disbands strength at P5 in the order infantry, armour, aircraft, naval until the stated amount is removed. If the payer has less strength than stated, the remaining amount is cancelled, the term is recorded as partially satisfied and the settlement still completes. No debt is created.

---

## 21. Settlement enforcement and reparations

### 21.1 Caps and source

`WAR-137` Reparations are a **one-time transfer from existing unreserved value at P5**. They are never a debt, never an instalment plan, never a claim on future income and never a negative balance.

| Cap | Value | Status |
|---|---|---|
| Crown reparations | ≤ 25% of the payer's unreserved crowns at acceptance, and ≤ 100,000 crowns | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Resource reparations | ≤ 10% of the payer's unreserved stock of that resource at acceptance, per resource | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| Combined terms | One crown term and one resource term per settlement | Structural |
| Payment schedule | Single immediate P5 transfer | Structural |
| Failure to pay | Settlement fails atomically; no partial transfer; campaign continues | Structural |

`WAR-138` At acceptance the payer's available value is checked and **reserved**. The reservation is held until P5, so P3 obligations and other actions cannot consume it. If the reservation is lost for any reason before P5, the settlement fails with `WRF-33` and the campaign returns to `ACTIVE`.

`WAR-139` Reparations move value through `TRANSFER_OUT`/`TRANSFER_IN` with one transfer identifier and matched amounts. They create nothing, destroy nothing and bypass no restriction. A restricted-pair or embargo rule is not bypassed by a settlement; if a transfer is prohibited, the term is invalid at proposal time.

`WAR-140` There is **no loot**. A victor gains no automatic share of the loser's treasury, inventory, production or cities. Every transfer is written into a settlement and accepted by both owners.

`WAR-141` An Alliance may not pay, receive, guarantee or broker a reparation. The Alliance Receiving Ledger is not a military treasury and has no role in B-10.

---

## 22. Postwar consequences

`WAR-142` At `ENDED`, both nations keep their account, nation, cities, facilities, research, inventory, treasury and population. The only consequences are the recorded outcome, the losses already applied, any settlement transfer and any `TERM_EXCLUSION`.

`WAR-143` B-10 grants **no post-defeat protection**. A defeated nation relies on B-03's existing protections only. This avoids a second protection system and a conflicting duration; `WQN-16` is therefore answered as "none beyond B-03".

`WAR-144` A `TERM_EXCLUSION` lasts 84 turns from the settlement's completion. It blocks declaration between the pair only; it does not block operations in a different campaign, trade, diplomacy or Alliance membership.

`WAR-145` Recovery after defeat is ordinary: readiness recovers through paid upkeep and `RESUPPLY`; strength is rebuilt through recruitment; resources are produced. There is no special recovery rate.

`WAR-146` Re-entry is ordinary: a nation may declare again when it has an outgoing slot, passes every validator and is not excluded. No cooldown exists apart from `TERM_EXCLUSION` and the campaign's own end state.

`WAR-147` The campaign record is permanent. Rankings and world events receive the outcome under B-11's rules; no aggregate is published below k = 5 (D-027).

---

## 23. Visibility and permissions

### 23.1 Visibility matrix

| Object | Public | Alliance | Private | Restricted |
|---|---|---|---|---|
| Declaration | Yes, at P6 | — | — | — |
| Campaign existence, objectives, deadline, outcome | Yes | — | — | — |
| Operation identity and target | After P6 summary | — | Actor and defender at P5 | — |
| Battle report (exact) | — | — | Actor and defender | — |
| Battle summary (tier, loss band) | Yes | — | — | — |
| Own force, readiness, OP, inventory | — | — | Owner | — |
| Opponent force and readiness | Band only | — | — | — |
| Settlement proposal and terms | Yes once accepted | — | While pending, parties only | — |
| Audit records | — | — | Actor/defender where applicable | Authorised administration |
| Blocked-attack reason | Actor sees the rule and the counterparty | — | — | No private treaty text |

`WAR-148` Alliance membership grants **no** military visibility. An Alliance does not see a member's operations, readiness, force, inventory, battle reports or settlement drafts. `AX-18`'s narrow roster surface is unchanged and is not a war room.

`WAR-149` A failure message explains the actor's own rejection without leaking another nation's private information. It may state "blocked by an active non-aggression agreement" but not the agreement's private terms, the other party's inventory or its exact strength.

`WAR-150` Public aggregates follow D-027. A per-war public statistic that could identify a small group is withheld or coarsened; no per-nation private value is published as an aggregate.

### 23.2 Permissions

| Action | Who may perform it |
|---|---|
| Declare war | The nation's authenticated owner |
| Submit, cancel or amend an operation | The nation's authenticated owner, before the freeze |
| Propose, counter, accept, reject or withdraw a settlement | The nation's authenticated owner |
| Surrender | The nation's authenticated owner |
| Declare a ceasefire | The nation's authenticated owner |
| Read own military data | The owner |
| Read another nation's exact military data | Nobody through a player interface |
| Administrative correction | Authorised administration through a recorded reversal, never an in-place edit |

`WAR-151` No Alliance role, office, ballot, majority, treaty, AI or administrator may exercise any row above for a member. This is D-137 and B-09's military sovereignty.

### 23.3 Confirmation requirements

`WAR-152` A declaration, a missile strike, a surrender and a settlement acceptance each require an explicit confirmation that names the counterparty, the OP and resource cost, the objective set (for a declaration), the expected effect and the irreversible consequence. Confirmation cannot be defaulted, pre-checked or remembered.

---

## 24. Audit events and failure codes

### 24.1 Military audit events

`WAR-153` Every event below is immutable, append-only and written inside the transaction that causes it.

| ID | Event | Required fields |
|---|---|---|
| `WRA-01` | `WAR_DECLARED` | war, campaign, declarer, target, objectives, turn, cost, action key |
| `WRA-02` | `WAR_BLOCKED` | actor, target, failing check, code, turn, action key; `AUD-AL-017` additionally for B-09 blocks |
| `WRA-03` | `OP_ACCEPTED` / `OP_REJECTED` | operation, actor, target, type, cost, reservation ids, code |
| `WRA-04` | `BATTLE_RESOLVED` | battle, operation, powers, ratio, fortune, tier, losses, progress |
| `WRA-05` | `CAMPAIGN_STATE` | campaign, prior state, new state, turn, reason |
| `WRA-06` | `OBJECTIVE_PROGRESS` | campaign, side, objective, delta, new total, source operation |
| `WRA-07` | `STATE_APPLIED` / `STATE_REMOVED` | nation, state, source, expiry |
| `WRA-08` | `STRATEGIC_STRIKE` | operation, actor, target, tier, losses, limits used |
| `WRA-09` | `INTERCEPTION` | operation, defender, triggering attack, result |
| `WRA-10` | `FORTIFICATION` | nation, state, consumed-by battle or expiry |
| `WRA-11` | `RESUPPLY` | nation, OP, resources, readiness before/after |
| `WRA-12` | `SETTLEMENT` | settlement, campaign, parties, terms, state, transfer id |
| `WRA-13` | `CAMPAIGN_ENDED` | campaign, outcome, victor, progress, turn, reason |
| `WRA-14` | `RESERVATION_AUDIT` | action key, OP, resources, state, turn |

`WAR-154` `AUD-AL-017` is used only for a B-09 same-Alliance or Alliance NAP block and keeps its exact B-09 field set. It is never used for protection, pair, national NAP, political-state, slot, resource or readiness denials.

`WAR-155` Audit access is role-based. The actor sees its own records; the defender sees the battle and settlement records that concern it; an Alliance sees none of a member's military records; authorised administration sees the record for fair-play work. Prompt 12 owns the broader enforcement and penalty policy; B-10 supplies the taxonomy, evidence fields and block records.

### 24.2 Failure codes

| Code | Stage | Meaning | Mutation |
|---|---|---|---|
| `WRF-01` | Submission | Actor not authenticated owner | None |
| `WRF-02` | Submission/P2/P5 | Actor nation dormant, retired or inactive | None |
| `WRF-03` | Submission/P2/P5 | Target invalid, self, dormant or retired | None |
| `WRF-04` | Submission/P2/P5 | Restricted pair | None |
| `WRF-05` | Submission/P2/P5 | Newcomer protection | None |
| `WRF-06` | Submission/P2/P5 | National NAP | None |
| `WRF-07` | Submission/P2/P5 | Same-Alliance ban | None; `AUD-AL-017` |
| `WRF-08` | Submission/P2/P5 | Alliance NAP | None; `AUD-AL-017` |
| `WRF-09` | Submission/P2/Pre-P5 | `TRANSITION`/`CRISIS` for a new offensive order, or the execution-time political state blocks it | None at submission; reservations released at P2/pre-P5 |
| `WRF-10` | Submission | No campaign slot | None |
| `WRF-11` | Submission | Insufficient OP | None |
| `WRF-12` | Submission | Insufficient crowns/resources | None |
| `WRF-13` | Submission | Duplicate idempotency key | None; original receipt |
| `WRF-14` | P5 | Declaration expired before resolution | Reservations released |
| `WRF-20` | P5 | Campaign expired | Reservations released |
| `WRF-21` | P2/P5 | Campaign suspended by dormancy | Reservations released |
| `WRF-22` | P7 | Operation unresolved by P7 | Reservations released; void |
| `WRF-23` | P2/P5 | Readiness gate failed | Reservations released |
| `WRF-24` | Submission | Force cap or type-share exceeded | None |
| `WRF-25` | Submission/P2/P5 | Supply bundle unavailable | Reservations released |
| `WRF-26` | P2/P5 | No active campaign or stale target | Reservations released |
| `WRF-27` | Submission | Blockade active or cooldown | None |
| `WRF-28` | Submission | Tier or campaign limit for missile strike | None |
| `WRF-29` | Submission | No active blockade to break | None |
| `WRF-30` | Submission | Readiness already at cap | None |
| `WRF-31` | Submission | Duplicate `FORTIFY` in the same P5 | None |
| `WRF-32` | Submission/P2/P5 | Postwar exclusion active | None |
| `WRF-33` | P5 | Settlement reservation lost; atomic failure | Campaign returns to `ACTIVE` |
| `WRF-34` | P5 | Internal invariant violation; turn checkpoint held | Operator path; no partial publication |
| `WRF-35` | Pre-P5 | `RATION_SHORT`: the force is unfed; a new offensive operation is blocked | Reservations released; defensive and sustainment operations still resolve |
| `WRF-36` | Submission/P2/P5 | Invalid city target: not `OP-05`, city missing, or not owned by the target nation | Reservations released; the strike does not resolve |
| `WRF-37` | P4.1 | Invalid infrastructure repair: above 10 levels, above the damage, or above the 500 cap | Reservations released; no charge |

---

## 25. Cross-system integration contracts

### 25.1 Contract matrix

`WAR-156` The following contracts are binding. Each row names the shared state, the phase, the validation point, the mutation owner, the failure behaviour, the economic and visibility effect, and the B-10 requirement that implements it.

| Source | B-10 dependency | B-10 implementation | Phase / trigger | Validation point | Mutation owner | Failure | Economic impact | Visibility / audit | Requirement |
|---|---|---|---|---|---|---|---|---|---|
| B-02 `TR-040` | P0–P7 phases | B-10 mutates only at acceptance while OPEN, P3.7, P4.1 (recruitment and construction/repair) and P5 | Acceptance/P3.7/P4.1/P5 | Phase contract | B-02 scheduler | `WRF-34` | Reservations at acceptance; charges at resolution | `WRA-01`…`WRA-14` | REQ-654 |
| B-02 `TR-050` | Frozen baseline | All battles read the P5 baseline and apply damage carry | P5.5–P5.7 | Baseline checksum | B-10 | `WRF-34` | Deterministic | Battle report | REQ-655 |
| B-02 `TR-045`/`TR-046` | Deterministic order and seed | B-10 order key and battle seed | P5 | Replay check | B-10 | `WRF-34` | None | `WRA-04` | REQ-655 |
| B-02 `TR-059`/`TR-060` | Reservation validation at acceptance, P2 revalidation | All operations and settlements reserve at acceptance; P2 rechecks | Submission/P2 | Canonical validator | B-02 | `WRF-05`…`WRF-12` | Released reservation | `WRA-02`, `WRA-14` | REQ-656 |
| B-02 `TR-057` | Idempotency | Action key and `(turn, operation)` resolution key | Submission/P5 | Duplicate check | B-02 | `WRF-13` | None | `WRA-03` | REQ-657 |
| B-03 `ONB-019`/`ONB-020` | Newcomer protection | Blocks declaration and every offensive operation | Submission/P2/P5 | Cumulative validator step 4 | B-10 | `WRF-05` | None | `WRA-02` | REQ-658 |
| B-03 `NET-025`/`NET-026` | Restricted pairs | Blocks every hostile path | Submission/P2/P5 | Step 3 | B-10 | `WRF-04` | None | `WRA-02` | REQ-658 |
| B-03 `D-028` | Dormancy | Suspends campaign, fails operations, expiry by abandonment | P0/P2/P5 | Dormancy check | B-10 | `WRF-21` | Released | `WRA-05` | REQ-659 |
| B-03 `RRL-013`/`RRL-021` | Reroll | Blocked while `DECLARED_PENDING`, `ACTIVE`, `SUSPENDED`, `SETTLING` | Reroll request | Campaign-state check | B-03 | Reroll blocked | None | Review signal | REQ-660 |
| B-04 `ECN-023` | Closed 11-resource roster | Uses gasoline, ammunition, steel, aluminium only | All | Register check | B-04 | `WRF-12` | Reservation/consumption | `WRA-14` | REQ-661 |
| B-04 `ECN-105`/`ECN-106` | Obligation order | Military Food ration at rank 6(a), readiness upkeep at 6(b); an unpaid obligation cancels, never debts | P3.7 | Obligation check | B-10 | `OBLIGATION_CANCELLED`, `RATION_SHORT` | Readiness −100 | `WRA-11` | REQ-662, REQ-696 |
| B-04 `ECN-165` | Ledger types | No new type; uses `RESERVATION_*`, `OBLIGATION_*`, `CAPEX`, `TRANSFER_*` | P4/P5 | P7 reconciliation | B-04 | `WRF-34` | Conserved | Ledger | REQ-661 |
| B-04 `ECN-212` | Immediate reparations | One-time P5 transfer, cap, no debt | P5.3 | Transfer check | B-04 | `WRF-33` | Conserved | `WRA-12` | REQ-663 |
| B-05 `URB-157` | City identity and infrastructure | No city capture, deletion or transfer; `OP-05` may reduce infrastructure under the §16.4 caps; no facility is affected | P5 | `WAR-009` matrix then `WAR-109a` city check | B-10 + B-05 | `WRF-36` | Book-value impairment; repair capex | Battle report, `INFRASTRUCTURE_DAMAGED` | REQ-664, REQ-699–REQ-703 |
| B-05 catalogue | No military building | Development tier gates units; catalogue unchanged | Submission | Tier check | B-10 | `WRF-28` | Recruitment `CAPEX` | `WRA-03` | REQ-665 |
| B-05 research | No Military branch | No military research; five branches unchanged | — | — | — | — | None | — | REQ-665 |
| B-06 `DMP-265` | Political restrictions | New orders blocked; accepted defensive resolve; accepted offensive fail; war continues | Submission/P2 | Political-state check | B-10 | `WRF-09` | Released | `WRA-02` | REQ-666 |
| B-07 `MKT-009`/`MKT-218` | Trade independence | War does not block trade; only a B-08 embargo does | P4 | Embargo check | B-08 | Existing market code | None | Market rules | REQ-667 |
| B-08 `DP-T01`/`DIP-141` | National NAP | Blocks declaration only; inert effect now active in exact scope | Submission/P2/P5 | Step 5 | B-10 | `WRF-06` | None | `WRA-02` | REQ-668 |
| B-09 `ALL-206`–`ALL-215` | Same-Alliance and NAP | Cumulative checks 6–7 on every hostile path | Submission/P2/P5 | Canonical validator | B-09 engine | `WRF-07`/`WRF-08` | None | Mandatory `AUD-AL-017` | REQ-669 |
| B-09 `AX-18` | Roster surface | No military data through membership | All | Access check | B-09 | Denied | None | Access log | REQ-670 |
| B-09 `D-141` | ARL not a treasury | No Alliance payment, receipt, guarantee or brokerage | Proposal/P5 | Term validation | B-10 | Invalid term | None | `WRA-12` | REQ-671 |
| D-027 | Privacy | k ≥ 5 aggregates; no private military value | Publication | Aggregate check | B-02 | Withhold | None | Public summary | REQ-672 |
| Prompt 11 | War events, objectives, ranking input | Emits `WRA-13`, outcome and objective totals | P6 | Event schema | B-11 | Missing record | None | Public | REQ-673 |
| Prompt 12 | Abuse taxonomy and evidence | Supplies block records, evidence fields, prohibited behaviours | Continuous | Fair-play review | B-12 | Review | None | Restricted | REQ-674 |
| Prompt 13 | Interface | Supplies odds band, threat band, confirmation content, failure copy | UI | Copy audit | B-13 | — | None | Player-facing | REQ-675 |
| Prompt 14 | Calibration | Supplies every provisional value and formula | — | Calibration suite | B-14 | — | Balance | — | REQ-676 |
| Prompt 15 | Assembly | Supplies canonical references and consistency evidence | — | Bible audit | B-15 | — | — | — | REQ-677 |

All requirement IDs `REQ-654`…`REQ-677` are new B-10 rows and are registered in the [traceability register](03_requirements_traceability.md). The remaining B-10 requirements `REQ-678`…`REQ-693` map to the adopted 10A candidates in §27, and `REQ-694`…`REQ-703` implement the §25.3 Food and §25.4 infrastructure-damage matrices.

### 25.2 Integration invariants

`WAR-157` **Phase invariant.** No B-10 state mutates outside acceptance while the turn is OPEN, P3.7, P4.1 recruitment/construction, or P5. A UI or API call that appears to change readiness, force, progress, OP or campaign state outside those points is a defect, not a rule. P0 and the P7 close never regenerate OP; the only regeneration is the single P3.7 item within the existing recurring phase.

`WAR-158` **Transaction invariant.** One battle is one transaction. Its losses, progress, state changes, ledger items and audit events commit together or not at all.

`WAR-159` **Conservation invariant.** The sum of every B-04 inventory movement caused by B-10 equals the sum of reservations consumed plus obligations paid; no B-10 path creates or destroys Crowns or resources.

`WAR-160` **Validator invariant.** Every present and future hostile entry point — declaration, raid, assault, air strike, missile strike, blockade, blockade break, any counter, any administrative replay and any future operation — calls the canonical cumulative validator. A new path that does not call it is a release blocker.

`WAR-161` **Authority invariant.** No Alliance role can read a member's private military state, spend a member's OP or resources, submit a member's operation or declare for a member. `AX-30` is preserved.

`WAR-162` **Privacy invariant.** A public war statistic that would identify fewer than five nations is withheld or coarsened under D-027. No exact readiness, force or inventory is ever public.

`WAR-163` **Provisional invariant.** Every value labelled provisional is owned by Prompt 14. No later document may present one as calibrated or approved.

### 25.3 Food integration matrix

`WAR-163a` The military Food integration is complete at the following ten points. No point may be changed by a later prompt without a B-10 revision.

| # | Element | Owner | Trigger | Phase | Validation | Mutation | Economic consequence | Failure | Visibility | Audit | Requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Soldier-equivalent factor `e_t` | B-10 | Any strength-point total | Any read | Table lookup, 4 types | None | None | Unknown type → `WRF-34` | Owner | None | REQ-694 |
| 2 | `ration_equivalents` | B-10 | P3.7 | P3.7 | `Σ(strength_points × e_t)` | None | None | Negative strength → `WRF-34` | Owner | `WRA-14` | REQ-694 |
| 3 | `military_food_demand` | B-10 | P3.7 | P3.7 | `ceil(equivalents / 1000)` | None | Sets the Food debit | Division by zero cannot occur (denominator 1,000) | Owner | `WRA-14` | REQ-695 |
| 4 | Civilian priority | B-04 | P3.6 before P3.7 | P3.6→P3.7 | `ECN-080`…`ECN-085`; protected requirement `WAR-053l` | Food consumed by civilians first | Garrison sees only the remainder | Shortfall never diverts civilian Food; an OP-09 reservation that would break the protected requirement is released | Owner | `FOOD_CONSUMED` | REQ-695 |
| 5 | Ration payment | B-04 obligation engine | P3.7 rank 6(a) | P3.7 | Whole obligation vs unreserved Food | Debit Food | `OBLIGATION_PAID` | `OBLIGATION_CANCELLED`, no debt | Owner | `OBLIGATION_PAID`/`CANCELLED` `MILITARY_RATION` | REQ-696 |
| 6 | Ration shortfall | B-10 | Unpaid ration | P3.7→pre-P5 | `RATION_SHORT` flag | Readiness −100 | Food saved, readiness lost | Offensive blocked `WRF-35`; defensive still resolves | Owner + readiness band | `WRA-14` | REQ-696 |
| 7 | Recovery | B-10 | Next paid P3.7 | P3.7 | Flag cleared | `RATION_SHORT` cleared | No catch-up payment | — | Owner | `WRA-14` | REQ-697 |
| 8 | `OP-09` field ration | B-10 | Operation acceptance | Acceptance→P5 | 4 Food reserved **only from `eligible_op09_surplus` above the protected civilian requirement** (`WAR-053l`) | Reserved, then consumed | Separate from garrison | `WRF-25` if the eligible surplus is short or P3.6 must release it; never `WRF-35` | Owner | `WRA-03`, `WRA-14` | REQ-697 |
| 9 | No double counting | B-10 | Every turn | P3.7/P5 | Two distinct event keys | Each Food unit debited once | Conservation holds | Duplicate key → `WRF-34` | Owner | `WRA-14` | REQ-698 |
| 10 | Political states | B-10 | `TRANSITION`/`CRISIS` | P3.7 | `WAR-053i` | None | Ration still due | No exception | Owner | `OBLIGATION_*` | REQ-698 |

### 25.4 Infrastructure-damage integration matrix

`WAR-163b` The city-infrastructure integration is complete at the following ten points.

| # | Element | Owner | Trigger | Phase | Validation | Mutation | Economic consequence | Failure | Visibility | Audit | Requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | City target | B-10 + B-05 | `OP-05` submitted | Submission/P2/P5 | Exists, owned by target, `OP-05` only | None | None | `WRF-36` | City identity public | `WRA-02` | REQ-699 |
| 2 | Nation checks first | B-10 | Same submission | Submission/P2/P5 | Full `WAR-009` matrix | None | None | `WRF-01`…`WRF-13` | Actor | `WRA-02` | REQ-699 |
| 3 | Damage roll | B-10 | Attacker victory | P5 | `F-WR-037` caps and floor | `removed` levels | None until applied | Draw/defeat → 0 damage | Battle report | `WRA-08` | REQ-700 |
| 4 | Infrastructure write | B-05 | Damage applied | P5 | Integer 10…500 | `infrastructure −= removed` | Asset lower | Floor prevents <10 | Public at P6 | `INFRASTRUCTURE_DAMAGED` | REQ-700 |
| 5 | Capacity recalc | B-05 | Same instant | P5 | `URB-041` | New capacity | May create overdraw | Overdraw blocks new orders, not production | City view | `INFRASTRUCTURE_DAMAGED` | REQ-701 |
| 6 | Housing recalc | B-05 + Prompt 06 | Same instant | P5 | `URB-042` | New housing | Growth pauses; no eviction | No casualty | City view | `INFRASTRUCTURE_DAMAGED` | REQ-701 |
| 7 | Facilities preserved | B-05 | Any damage | P5 | No facility row changes | None | No recipe/DC/limit change | Facility deletion is a defect | Public | None | REQ-702 |
| 8 | Book-value impairment | B-04 + B-05 | Same instant | P5 | `F-WR-038` | Book value reduced | National wealth falls | Impairment > value → `WRF-34` | Owner book value | `INFRASTRUCTURE_DAMAGED` | REQ-702 |
| 9 | Repair | B-05 | Player order | P4.1 | `1…10`, `≤500`, `≤unrepaired` | Level restored, capex charged | Crowns spent, asset restored | `WRF-37` | Owner cost | `INFRASTRUCTURE_REPAIRED` + `CAPEX` | REQ-703 |
| 10 | Ordering | B-02 + B-05 | Same turn | P4.1→P5 | P4.1 commits before P5 | Repair then damage | No retroactive undo | Late repair cannot heal a past strike | Public timeline | `WRA-08` | REQ-703 |

---

## 26. Decision and conflict-resolution register

### 26.1 Architecture decision register

`WAR-164` The following 25 decisions are B-10's complete architecture. Each is a **Provisional design position** under D-014, mirrored as DD-166…DD-190. No architecture decision is deferred to Prompt 14.

| ID | Decision | Alternatives considered | Rationale | Source constraints | Downstream effect |
|---|---|---|---|---|---|
| `B10-AD-01` | Layered object: `WAR` → exactly one `CAMPAIGN` → objectives/operations/battles | Nation-war only; campaign above many wars; single flat object | One war one campaign avoids two competing score structures while keeping a legal relationship and a scored episode distinct | 10A WFH-B1; B-02 | 10C state machines; 11 event schema |
| `B10-AD-02` | Max 1 outgoing + 1 incoming campaign, 2 total; no joining another war | P&W 5/3; unlimited; 1 total | Bounded exposure, no coalition drag, no slot-filling | `WFC-05`; B-09 sovereignty | 10C declaration tests; 14 calibration |
| `B10-AD-03` | One war per campaign; one primary + one secondary objective | Many wars per campaign; many objectives; single meter | Readable terms, finite scoring, no hidden second front | `WCR-05`; `WFC-01` | 10C objective tests |
| `B10-AD-04` | Per-campaign objective progress per side; OP strictly national | National war score; per-war pool; single resistance pool | Keeps OP national (D-015) and makes progress legible without a second currency | D-015; `WFC-06` reject | 14 calibration; 13 meter |
| `B10-AD-05` | 84-turn deadline + one 42-turn extension; 24/48 inactivity rule | 60 turns; 168; unlimited | Bounded, aligns with B-03's 84-turn unit, forces an off-ramp | `WFC-07`; WFS-022 | 10C expiry tests |
| `B10-AD-06` | Owner-only unilateral declaration; 2 OP + 500 crowns; slot check | Consent; zero cost; strength-range gate | Declarations must be meaningful but not prohibitive; a strength gate would add a second balance surface | D-015; `WFC-02`; `WCR-02` | 10C eligibility |
| `B10-AD-07` | One immutable `STANDARD` war profile; no posture switch; objective set immutable | Three P&W war types; four postures; selectable looting | Avoids asymmetric hidden modifiers; declaration terms are the strategy | `WFC-03`; `WFC-22` | 10C declaration; 13 copy |
| `B10-AD-08` | Six closed objectives: ATTRITION, INTERDICTION, BLOCKADE, AIR, DEFENCE, STRIKE | Resistance meter; capture; economy-only | Every objective is mapless and measurable | `WCR-05`/`WCR-06`; mapless | 10C objectives; 11 events |
| `B10-AD-09` | Victory by primary completion; decisive/limited/draw; expiry/abandonment outcomes | Hidden score; total destruction | Deterministic, public, no hidden meter | `WCR-27`; `WFQ-06` | 10C outcome matrix |
| `B10-AD-10` | Nine operations: RAID, ASSAULT, AIR_STRIKE, BLOCKADE, MISSILE_STRIKE, INTERCEPT, FORTIFY, BREAK_BLOCKADE, RESUPPLY | P&W nine actions copied; larger catalogue | Closed, mapless, every offensive has a counter; espionage/nuclear excluded | `WCR-15`/`WCR-16`; `WFC-11`/`WFC-12` | 10C operation tests |
| `B10-AD-11` | National readiness 0…1,000, combat/gate only, never economic | Per-unit readiness; economic multiplier | One readable value; B-06 has no combat modifier and B-04 income is untouched | `WCR-11`/`WCR-12`; `WFC-20` | 14 calibration |
| `B10-AD-12` | Four strength-point pools, no individual units, no damage state | Explicit units; P&W unit list; per-unit readiness | Simpler, deterministic, still supports counters and losses | `WFR-006`; `WFC-20` | 10C force tests; 13 display |
| `B10-AD-13` | Recruitment at P4, arrival at next P3, no OP cost, force cap and type-share | Instant buy; OP cost; unlimited | Separates the action economy from the production economy; prevents monotype | D-015; `WCR-13`/`WCR-14` | 14 calibration |
| `B10-AD-14` | Four-resource supply bundles, reserved at acceptance, consumed at P5; no geography | Supply stat; depots; routes | Uses existing resources and conservation; mapless | `WCR-19`; B-04 | 10C supply tests; 14 bundles |
| `B10-AD-15` | Deterministic power + one seeded ±500 bp fortune roll; five tiers | Pure deterministic; three rolls 40–100%; hidden RNG | Reproducible, explainable, bounded; no hidden bonuses | `WCR-17`; `WFC-08`; `WFE-07` | 10C battle tests; 14 tuning |
| `B10-AD-16` | Losses are strength, readiness and bounded city infrastructure; 20% battle cap, 60% campaign cap | Unbounded infrastructure damage; loot; annihilation | Anti-snowball, conservation, `URB-157`; infrastructure damage is capped at 20 levels per strike, 30% per city per campaign and a floor of 10 | `WCR-25`; `URB-157`; `WFC-13`; WFH-D3 partially adopted | 10C loss tests; 14 tuning |
| `B10-AD-17` | 3 offensive + 3 conditional defensive ops per turn; defensive prep before offensives | Unlimited; P&W MAP per war; simultaneous | Bounded, deterministic, preserves counterplay | D-024; `WCR-23` | 10C ordering tests |
| `B10-AD-18` | Closed-term settlement; immediate atomic transfer; white-peace surrender; no instalments | Peace offer only; debt; forced terms | Avoids coercion and debt; keeps B-04 conservation | `WFC-17`; `WQN-17`/`WQN-18` | 10C settlement tests |
| `B10-AD-19` | No new postwar protection; optional 84-turn exclusion term; ordinary recovery | Beige analogue; automatic protection | Avoids a second protection system; aligns with B-03 | `WCR-28`; `WFC-23`; `WQN-16` | 10C postwar tests |
| `B10-AD-20` | UD-032 Option A: retain reroll block; surrender is the off-ramp | B forfeit; C old identity | Simplest, no laundering, no new attribution model, preserves B-03 | `UD-032`; `WCR-15` risk; §28 of 10A | 10C reroll tests; B-03 cross-reference |
| `B10-AD-21` | City infrastructure damage is adopted for `OP-05` only; no facility or city destruction, no transfer, no population casualty | Facility damage; city destruction; no damage at all | `URB-157` is amended narrowly: recoverable levels, derived capacity/housing, proportional book-value impairment, no building deletion | `URB-157`; `WFC-13`; `WFC-19`; `WQN-12`; WFH-D3 partially adopted | 10C negative tests; 14 infrastructure formulas |
| `B10-AD-22` | No military building and no Military research branch; development tiers gate units | One military building; full branch | Keeps B-05's closed catalogue untouched; simpler initial model | B-05; `WFC-21`; `WCR-40` | Future expansion; 14 tiers |
| `B10-AD-23` | Conventional missile strike only; no nuclear, no radiation, no uranium | Nuclear with nation-level fallout; world-level effect | Disproportionate, conservation-breaking, needs a B-04 amendment | `WFC-14`; WFS-028 | 10C exclusion tests |
| `B10-AD-24` | Espionage excluded and unassigned | Covert ops with separate budget; B-12 ownership | No Bible part owns it and no evidence justifies a second covert economy | `WFC-16`; `WQN-19`; D-024 | Future expansion needs a decision |
| `B10-AD-25` | Pre-battle odds band for attacker, threat band for defender, full report after | No odds; exact odds; exact enemy data | Transparency without private-data leakage | `WCR-17`/`WCR-18`; `WQN-20`; `GAP-11` | 10C disclosure tests; 13 UI |

### 26.2 Conflict register

`WAR-165` Every known cross-system conflict or missing decision is recorded below with its disposition. The dispositions use the required vocabulary: `RESOLVED BY B-10`, `INHERITED — EXISTING RULE PRESERVED`, `RECONCILED — CROSS-SYSTEM BEHAVIOUR DEFINED`, `TRANSFERRED — NAMED DOWNSTREAM OWNER`, `OWNER-RESERVED — AUTHORIZATION NOT AVAILABLE`, `EXTERNAL EVIDENCE LIMITATION`.

| ID | Source IDs | Conflict or missing decision | Owner / player effect | Economic & security effect | Disposition | Resolution | Implementing rule | Registers / validation | Downstream |
|---|---|---|---|---|---|---|---|---|---|
| `B10-C01` | `TR-042` | Are campaign costs drawn pre- or post-P3? | Timing clarity | Double-spend risk | RESOLVED BY B-10 | Costs are reserved at acceptance against the then-current unreserved balance and consumed from the reservation at P5; P3 income does not enlarge it and P3 obligations cannot consume it | `WAR-005`, `WAR-040` | Requirement row; arithmetic check | 10C |
| `B10-C02` | `TR-041`, `ECN-152` | P3 readiness upkeep vs P5 combat | Predictable readiness | No double charge | RECONCILED | Upkeep at P3.7 sets readiness; P5 reads the post-P3 value | `WAR-050`, `WAR-089` | Formula F-WR-003/005 | 10C |
| `B10-C03` | D-015, `TR-059` | OP refill vs carried reservations | Simple OP display | No lost or duplicated OP | RESOLVED BY B-10 (revised 10B-C3) | The OP pool is a persistent national ledger. It regenerates by one OP at the **P3.7 opening of each boundary**, never at P0 or P7, carries below the cap, and records one idempotent `REGENERATED` item per turn. A reservation stays outstanding across P3.7, reduces `available` rather than `op_balance`, and is consumed once at P5 or released once at cancellation/P7 void | `WAR-040`–`WAR-043b` | `WRA-14` | 10C |
| `B10-C04` | `TR-060` | P2 vs final P5 validation | Clear failure reason | Fail-closed | RESOLVED BY B-10 | Both run the same canonical validator; P5 is authoritative; either failure releases everything | `WAR-009`, `WAR-013` | `WRF-05`…`WRF-12` | 10C |
| `B10-C05` | `TR-050` | Simultaneous offensive and defensive operations | Fair counterplay | No double count | RESOLVED BY B-10 | Defensive prep at P5.5; offensives at P5.6; frozen baseline + damage carry | `WAR-089`…`WAR-093` | F-WR-022 | 10C |
| `B10-C06` | `TR-052` | Contested targets and dependent actions | No hidden chains | No unintended retarget | RESOLVED BY B-10 | One dependency edge (`INTERCEPT`); no support ops; each action independent | `WAR-094`, `WAR-095` | 10C dependency test | 10C |
| `B10-C07` | `TR-044`, `TR-050` | Attack ordering | Reproducibility | No priority exploit | RESOLVED BY B-10 | Total order key in `WAR-090` | `WAR-090` | Determinism test | 10C |
| `B10-C08` | `TR-053` | Stale target | Honest failure | No laundering | RESOLVED BY B-10 | Fail with `WRF-26`, never retarget | `WAR-096` | `WRF-26` | 10C |
| `B10-C09` | `TR-057` | Duplicate actions and retries | No double battle | No repeated loss | RESOLVED BY B-10 | Idempotency key + resolution key + one `APPLIED` marker | `WAR-097`…`WAR-099` | `WRF-13` | 10C |
| `B10-C10` | `TR-043` | Interrupted P5 | One outcome | No partial settlement | RESOLVED BY B-10 | Checkpointed P5, per-battle transaction, replay against same baseline and seed | `WAR-099`, `WAR-158` | Recovery test | 10C |
| `B10-C11` | `D-028`, B-02 | Participant becomes dormant | War does not hang | No targeting of dormant | RECONCILED | `SUSPENDED`; 48-turn abandonment outcome | `WAR-021`…`WAR-024` | `WRA-05` | 10C |
| `B10-C12` | B-03 `ONB-019` | Target becomes dormant | Protection stays authoritative | No OP spent on immune target | INHERITED | Operation fails and releases | `WAR-022` | `WRF-21` | 10C |
| `B10-C13` | B-03 protection | Protection expires between acceptance and execution | Predictable timing | No bypass | RESOLVED BY B-10 | Execution-time state decides; P2/P5 recheck | `WAR-116` | `WRF-05` | 10C |
| `B10-C14` | `DMP-265` | Existing defensive commitments when dormant/protected | No free defence | Consistent fail-closed | RESOLVED BY B-10 | Defensive orders fail and release when the nation is protected or dormant | `WAR-117` | `WRF-21` | 10C |
| `B10-C15` | `UD-032`, `RRL-021` | Reroll with an active campaign | Player must end the war first | No identity laundering | RESOLVED BY B-10 (owner authority not required — register assigns Prompt 10) | Option A: retain block; surrender is the off-ramp | `WAR-025`…`WAR-028` | UD register updated | 10C; B-03 |
| `B10-C16` | B-03 attribution | Historical attribution and cleanup | Record survives | No transfer to replacement | RECONCILED | Permanent attribution, archival, no cleanup of live campaigns | `WAR-029`…`WAR-031` | Audit retention test | 10C/11 |
| `B10-C17` | `ECN-105` | Where readiness upkeep sits | Readable priority | No rank change | RECONCILED | Rank 6, sub-order **(a) military Food**, (b) readiness, (c) settlement, (d) other military obligation | `WAR-064` | F-WR-003, F-WR-036 | 10C |
| `B10-C18` | `ECN-106` | Unpaid upkeep consequence | No debt | Readiness penalty only | RECONCILED | Cancelled obligation, −100 readiness, no debt | `WAR-051` | `WRA-11` | 10C |
| `B10-C19` | B-04 reservations | Resource reservation, consumption, release, shortage | Clear costs | Conservation | RESOLVED BY B-10 | Reserve at acceptance, consume at P5, release on every failure; no partial execution | `WAR-069`, `WAR-070` | `WRA-14` | 10C |
| `B10-C20` | D-015, B-04 | OP and resource costs together | Predictable price | No double charge | RECONCILED | Separate ledgers, one action key; both reserved at acceptance | `WAR-005`, `WAR-042` | Arithmetic check | 10C |
| `B10-C21` | B-04, B-05 | Repair and recovery costs | No free rebuild | Uses existing production | RESOLVED BY B-10 | **Two distinct paths, never one pool.** Military recovery: readiness via upkeep/`RESUPPLY`, strength via recruitment; no separate military repair cost. City infrastructure repair: a separate B-05 `UPGRADE_INFRASTRUCTURE` capex order at P4.1 (`WAR-109h`, B-05 `URB-043`/`URB-044`, no materials), capitalised as a new infrastructure lot; it never restores strength or readiness | `WAR-109h`, `WAR-110`…`WAR-113` | Repair/cost test | 10C/14 |
| `B10-C22` | `WQN-17`/`WQN-18`, B-04 | Loot and reparation caps | No automatic seizure | Conservation | RESOLVED BY B-10 | No loot; consensual reparations; 25%/100,000 crown cap; immediate transfer | `WAR-137`…`WAR-140` | F-WR-029 | 10C |
| `B10-C23` | `URB-157`, WFH-D3 | Facility damage | Facilities always remain | No B-05 catalogue rewrite | RESOLVED BY B-10 | No facility damage, deletion, disablement or transfer. City **infrastructure** damage is a separate, adopted, recoverable effect (`WAR-109a`–`WAR-109m`) and never touches a facility or its book value | `WAR-101`, `WAR-102`, `WAR-109a`–`WAR-109m` | Negative test | 10C |
| `B10-C24` | B-05 catalogue | Military buildings and research | No new facility | No B-05 change | RESOLVED BY B-10 | Deferred; development tiers | `WAR-055`, `WAR-056` | Catalogue check | Future expansion |
| `B10-C25` | B-05, `WFC-13` | City targeting | A city may be named as an asset target | No geographic reading | RESOLVED BY B-10 | `OP-05` may target a B-05 `city_id`; the strike still runs the full national validator first; no other operation targets a city; no map or location is created | `WAR-009b`, `WAR-102`, `WAR-109a` | Copy audit | 10C/13 |
| `B10-C26` | `DMP-265` | Political states and war | War does not pause | No combat modifier | RECONCILED | New offensive orders blocked (`WRF-09`); **validly accepted defensive commitments are exempt from the political-state row only** (`WAR-009g`), with every other check still running; accepted offensive operations fail at P2/pre-P5 and release; deadlines continue; the execution-time state governs | `WAR-053j`, `WAR-053k`, `WAR-009c`, `WAR-009g` | Eight-scenario table; `WRF-09` | 10C |
| `B10-C27` | B-08 `DP-T01`; B-09 `AT-E01` | National vs Alliance NAP; membership changes | Two distinct blocks | No merged treaty | RECONCILED | National NAP blocks declarations only; Alliance NAP blocks all hostile paths for covered pairs; execution-time state decides; checks are separate and cumulative | `WAR-009a`, `WAR-010`…`WAR-012` | `AUD-AL-017` test | 10C |
| `B10-C28` | `ECN-214` vs `ECN-165` | `CONSUME` event named but not registered | No visible divergence | Ledger integrity | RECONCILED | Use `RESERVATION_CONSUMED`; no new type; the military Food debit uses `OBLIGATION_PAID` with component `MILITARY_RATION` | `WAR-063`, `WAR-064a` | Event-set check | B-04 note |
| `B10-C29` | `AUD-AL-017` | Audit scope | Correct records | No over-broad logging | INHERITED | Only B-09 blocks emit it | `WAR-154` | Audit test | 10C/12 |
| `B10-C30` | `WFC-16`, `WQN-19` | Espionage ownership | No covert ops | No second currency | **EXCLUDED FROM CURRENT B-10 SCOPE — UNASSIGNED FUTURE-SCOPE CANDIDATE** | Excluded from B-10. **No owner is identified and nothing is transferred**: not Prompt 12, not Prompt 10C, not any later prompt. A future expansion requires its own owner decision and does not exist today | §13.3; `B10-AD-24` | Scope check | Roadmap |
| `B10-C31` | B-09 `ALL-089`, `AX-30` | Alliance military authority | No command creep | Sovereignty | INHERITED | No command, delegation, shared OP or treasury use | `WAR-161`, §23.2 | Authority test | 10C |
| `B10-C32` | `GAP-11`, `WQN-20` | Pre-battle odds | Transparency | No private leak | RESOLVED BY B-10 | Odds band, threat band, full report | `WAR-085`…`WAR-088` | F-WR-032/033 | 10C/13 |
| `B10-C33` | `WQN-17`, `WFC-17` | Settlement duration and enforcement | No indefinite obligation | No debt | RESOLVED BY B-10 | Closed terms, immediate transfer, 84-turn exclusion, no continuing body | §20–§21 | 10C | 10C |
| `B10-C34` | `WFC-14`, WFS-028 | Nuclear and radiation scope | No escalation | No uranium demand | RESOLVED BY B-10 | Nuclear rejected; conventional missile only | `B10-AD-23`, §13.3 | Scope check | 14/15 |

`WAR-166` No B-10-owned decision remains open. Items `B10-C30` (espionage) and the future military-building expansion are **excluded from the current B-10 scope by decision** and are recorded as **unassigned future-scope candidates**, not as transferred ownership and not as unresolved B-10 rules, so the roadmap can see them honestly.

**Conflict count:** 34 recorded, 30 resolved or reconciled by B-10, 3 inherited unchanged (`B10-C12`, `B10-C29`, `B10-C31`), 1 excluded from the current B-10 scope as an unassigned future-scope candidate (`B10-C30`). No conflict is owner-reserved: none of them touches `UD-040`–`UD-049`.

---

## 27. 10A research disposition matrix

`WAR-167` This section dispositions **every** research identifier in the [10A report](research/10A_politics_and_war_warfare_research.md). A 10A candidate is not a rule because 10A proposed it: each row below states what B-10 did, where the rule lives, and which project requirement carries it. Nothing in this section approves a number; every value remains **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**.

### 27.1 Disposition summary

| Family | Count | Disposition | Result |
|---|---|---|---|
| `WCR-01`–`WCR-44` candidate requirements | 44 | 33 adopted, 10 amended, 1 transferred | 43 carried into `REQ-678`–`REQ-693`; `WCR-33` to Prompt 12 |
| `WQN-01`–`WQN-20` numerical questions | 20 | 17 architecture decisions + provisional values; 1 rejected (no such effect); 2 closed by exclusion or B-03 alignment | §27.3; F-WR register |
| `WFQ-01`–`WFQ-22` research questions | 22 | 15 resolved by a B-10 rule (14 resolved, 1 resolved by design); 7 not applicable because the P&W behaviour has no NS analogue | §27.4 |
| `WRK-01`–`WRK-15` risks | 15 | All mitigated or carried with a named owner | §27.5 |
| `WFX-01`–`WFX-12` evidence conflicts | 12 | 0 manufactured; 4 carried as P&W evidence status, 1 adopted as context, 2 closed as irrelevant, 3 closed by design, 1 evidence-method conflict applied, 1 open external evidence gap | §27.6 |
| `WFC-01`–`WFC-26` classifications | 26 | 3 adopted in substance, 14 adapted, 5 rejected, 2 not applicable, 1 replaced by a first-principles design, 1 transferred to Prompt 12 | §27.7 |
| `GAP-01`–`GAP-16` local evidence gaps | 16 | 8 closed by design decision, 3 closed as irrelevant, 1 transferred to a named owner, 4 remain open evidence gaps with no NS rule dependency | §27.8 |
| `WFH-A1`–`WFH-F6` handoff | 36 | A preserved, B resolved, C followed, D reconciled, E met, F resolved | §27.9 |

### 27.2 Candidate requirements (`WCR-01`–`WCR-44`)

| ID | Candidate | Disposition | B-10 rule | REQ | Rationale and evidence |
|---|---|---|---|---|---|
| `WCR-01` | Cumulative declaration validation on every entry point | **Adopt** | `WAR-009`–`WAR-014` | REQ-678 | Twelve-check fail-closed validator run at submission, P2 and pre-P5; B-03/B-08/B-09 blocks bind every path (`WFH-D4`, `WFH-D5`) |
| `WCR-02` | Strength range and campaign-slot gate | **Amend** — reject the range, adopt the slot gate | `WAR-005`, `WAR-007` | REQ-678 | B-10 has no power score to read; a range would invent a B-11 metric (`B10-AD-06`). Protection, slots and eligibility are the gates |
| `WCR-03` | Immutable posture with disclosed trade-offs | **Amend** — one `STANDARD` profile, no posture set | `WAR-006`; `B10-AD-07` | REQ-678 | Immutability retained; P&W's three asymmetric war types rejected (`WFC-03`, `B10-C07`) |
| `WCR-04` | No posture may bypass a protection or block | **Adopt** | `WAR-003`, `WAR-004`, `WAR-013` | REQ-678 | Structural: there is no posture, and every block is re-run at P2 and P5 |
| `WCR-05` | At least one readable objective beyond a meter | **Adopt** | §7.1; `B10-AD-08` | REQ-679 | Six objectives with stated completion thresholds |
| `WCR-06` | Objectives achievable without geography | **Adopt** | §7.1, §4.2 | REQ-679 | Every objective is a national-inventory or battle-count condition |
| `WCR-07` | Explicit states and one terminal outcome | **Adopt** | §6.1–§6.2; `B10-AD-01` | REQ-680 | Seven states; `ENDED`/`ARCHIVED`/`VOID` are terminal |
| `WCR-08` | No indefinite campaign; expiry has a settlement step | **Adopt** | `WAR-020`–`WAR-024`; `B10-AD-05` | REQ-680 | 84-turn deadline, one 42-turn extension, inactivity and dormancy paths |
| `WCR-09` | All military orders draw on one national OP pool | **Adopt** | §8.1; `WAR-029`–`WAR-032` | REQ-681 | D-015 as amended: one pool, military-only, +1 at P3.7; no per-war, per-campaign or shared pool |
| `WCR-10` | OP cap and costs published, never purchasable or transferable | **Adopt** | `WAR-033`, `WAR-034`, `WAR-040` | REQ-681 | Cap 10; +1 OP at the P3.7 opening of each boundary, capped; no purchase, no transfer, no gifting |
| `WCR-11` | Readiness visible and derivable from declared inputs | **Adopt** | §9.1, §23.1 | REQ-682 | Owner sees the value and the declared deltas; opponent sees a band only |
| `WCR-12` | Readiness is not an economic multiplier and not purchasable | **Adopt** | `WAR-045`, `WAR-046`; `B10-AD-11` | REQ-682 | Readiness affects combat and gates only; B-04 income is untouched |
| `WCR-13` | Finite enumerated unit roster with caps, upkeep and burn | **Adopt** | §10.1–§10.3; `B10-AD-12` | REQ-683 | Four strength-point pools; no individual units, no unit damage state |
| `WCR-14` | Losses bounded per operation and recoverable through production | **Adopt** | §16, §17; `B10-AD-16` | REQ-683 | 20% per-battle and 60% per-campaign caps; recovery by recruitment only |
| `WCR-15` | Closed, enumerated operation set | **Adopt** | §13.1; `B10-AD-10` | REQ-684 | Nine operations, no hidden operation, excluded categories published |
| `WCR-16` | Every operation declares cost, prerequisites, target class, effect, counter and burn | **Adopt** | §13.2 per-operation contracts | REQ-684 | Each contract carries all seven fields plus limits, visibility and failure |
| `WCR-17` | Deterministic, or bounded random with published odds | **Adopt** | §14.2–§14.5; `B10-AD-15` | REQ-685 | Deterministic power + one seeded ±500 bp fortune, bounded and reproducible |
| `WCR-18` | Both sides can read the outcome and its reason | **Adopt** | §14.5, `WAR-088` | REQ-685 | Tier, losses, readiness, objective delta and block reason |
| `WCR-19` | Logistics is inventory/resource based; no distance, route, depot or convoy | **Adopt** | §12.1; `B10-AD-14` | REQ-686 | Supply bundles reserved at acceptance, consumed at P5 |
| `WCR-20` | Blockade must not stop production or mint value, and must be breakable | **Amend** — blockade affects military supply only | §12.1, `WAR-072`; `OP-08` | REQ-686 | Production and trade are untouched; `+25%` supply cost and `−25` recovery are provisional; `OP-08` breaks it |
| `WCR-21` | Protection explicit, time-boxed, enforced at every attack path | **Adopt** | §18.1; `WAR-115`–`WAR-117` | REQ-687 | Reuses B-03 only; no new protection state or duration |
| `WCR-22` | Protection is not an economic multiplier | **Adopt** | `WAR-115`, `WAR-143` | REQ-687 | No income, production or upkeep change |
| `WCR-23` | Every offensive operation has a declared counter | **Adopt** | §13.2, §18.2; `B10-AD-17` | REQ-688 | Counter matrix covers all six offensive operations |
| `WCR-24` | Control states contestable and expiring | **Amend** — no standing control states | §13.2, §14.4 | REQ-688 | Effects are per-battle or per-turn and expire automatically; nothing persists to contest |
| `WCR-25` | Losses bounded, attributed and recorded; no city or population loss | **Adopt** | §16; `B10-AD-16`, `B10-AD-21` | REQ-689 | Strength points, readiness and bounded city **infrastructure** levels only; no city, facility or population loss; infrastructure damage is capped and recoverable (`URB-157`) |
| `WCR-26` | Loot and reparations move existing value and never mint | **Amend** — no loot; consensual reparations only | §21; `WAR-137`–`WAR-140` | REQ-689 | One-time transfer from unreserved stockpiles, capped and ledgered |
| `WCR-27` | Victory, mutual peace and expiry defined; no unilateral bypass of protection | **Adopt** | §7.3, §19, §20; `B10-AD-09` | REQ-680 | Primary completion or expiry determines the outcome; surrender is always available |
| `WCR-28` | Termination produces a record and a post-conflict protection state | **Amend** — record yes, no new protection state | §22; `B10-AD-19` | REQ-680 | Permanent record; B-03 protection is the only protection |
| `WCR-29` | Settlement object records parties, terms, duration, enforcement and audit | **Adopt** | §20.1, §20.4; `B10-AD-18` | REQ-690 | Eight states, six closed terms, immediate enforcement, `WRA-12` |
| `WCR-30` | Settlement cannot compel city deletion, real payment or an Alliance obligation | **Adopt** | §20.3 prohibited terms | REQ-690 | Closed term set; Alliance obligations and real-world payment are invalid |
| `WCR-31` | Every attack path calls same-Alliance and Alliance-NAP validators independently | **Adopt** | `WAR-009`, `WAR-011`, `WAR-012`; §25.1 | REQ-691 | Cumulative checks 6–7; mandatory `AUD-AL-017` on a B-09 block |
| `WCR-32` | No Alliance may order, move, attack with or spend for a member | **Adopt** | `WAR-161`; §23.2 | REQ-691 | No command, delegation, shared OP, treasury use or war declaration |
| `WCR-33` | War-slot filling, collusion and botting defined as prohibited with evidence and consequence | **Transfer — Prompt 12** | §24.1 evidence fields only | — | B-10 records evidence and block reasons; the prohibited-behaviour taxonomy and sanctions belong to B-12 fair play (`WFC-25`) |
| `WCR-34` | Record sufficient evidence without surveillance overreach | **Adopt** | §24.1 `WRA-01`–`WRA-14` | REQ-692 | Fourteen events with defined fields; no private inventory or treaty text |
| `WCR-35` | Attack confirmation states cost, effect, counterplay and block reason | **Amend** — content minimum adopted; screen design to Prompt 13 | `WAR-152` | REQ-692 | B-10 fixes what must be shown; B-13 owns layout and copy |
| `WCR-36` | Timeline legible to both sides without leaking private treaty data | **Amend** — visibility rule adopted; rendering to Prompt 13 | §23.1, `WAR-148`–`WAR-150` | REQ-692 | Block reason only; no private terms, inventory or exact strength |
| `WCR-37` | No coordinates, distance, adjacency, borders, movement, territory or geographic control | **Adopt** | §4.2; `WAR-168` | REQ-684 | Terminology contract is binding on every operation, state and screen |
| `WCR-38` | Rename geographic labels or define them symbolically | **Adopt** | §4.2 | REQ-684 | BLOCKADE and AIR are symbolic conditions, explicitly defined, not zones |
| `WCR-39` | Military progression plural and not dominant | **Adopt** | §10.2; `B10-AD-22` | REQ-693 | Four development tiers gate units; no separate military ladder |
| `WCR-40` | Military upgrades bounded, visible and resettable under declared rules | **Amend** — no military research branch | §10.2; `B10-AD-22` | REQ-693 | B-05's five branches are unchanged; no respec rule is created because no military upgrade exists |
| `WCR-41` | Every resource and OP movement ledgered; no minting, negative balance or hidden transfer | **Adopt** | §11.3; `WAR-063` | REQ-681 | Existing B-04 ledger types only; P7 conservation check |
| `WCR-42` | Reservation and consumption atomic; failure releases the reservation | **Adopt** | `WAR-005`, `WRF-34`; `B10-AD-01` | REQ-681 | Acceptance reserves, P5 consumes, any failure releases with no charge |
| `WCR-43` | Every declaration, operation, block, settlement and termination writes an audit record | **Adopt** | §24.1 | REQ-692 | `WRA-01`–`WRA-14` cover every mutation and every block |
| `WCR-44` | Audit readable only to authorised roles, without leaking private military or treaty data | **Amend** — matrix adopted; administrative access implementation to Prompt 12 | §23.1; `WAR-148` | REQ-692 | B-10 fixes the access matrix; B-12 owns the administration surface |

**`WAR-168`** The terminology contract in §4.2 is the operative definition of mapless conformance. A future operation that needs a distance, a route, a coordinate, a border, a front or a territorial state is **out of scope** and requires a new owner decision; it is not an extension of §13.

### 27.3 Numerical and formula questions (`WQN-01`–`WQN-20`)

| ID | Question | B-10 architecture decision | Value | Status |
|---|---|---|---|---|
| `WQN-01` | National OP cap | One national pool, `op_balance` persistent and regenerated by one OP at the P3.7 opening of each boundary, capped | Cap 10 | Provisional — F-WR-001 |
| `WQN-02` | Declaration OP cost | Declaration reserves and consumes OP | 2 OP | Provisional — F-WR-019 |
| `WQN-03` | Per-operation OP cost | Closed nine-operation cost table | 1–4 OP by operation | Provisional — F-WR-019 |
| `WQN-04` | Regeneration scaling | Flat +1 per boundary; no readiness, size or activity scaling | Flat | Structural (rate provisional as calibrated with cap) — F-WR-001 |
| `WQN-05` | Progress pool | Per-side objective progress, one primary and one secondary | 0…1,000 | Provisional — F-WR-009 |
| `WQN-06` | Progress per outcome | Table by operation and battle tier | 20–250 per resolution | Provisional — F-WR-009 |
| `WQN-07` | Campaign length | 84 turns, one 42-turn extension | 84 + 42 | Provisional — F-WR-007 |
| `WQN-08` | Simultaneous campaigns | One outgoing, one incoming, two total | 1 / 1 / 2 | Provisional — F-WR-006 |
| `WQN-09` | Build caps and recruitment rate | Force cap and training-capacity formulas | Formula | Provisional — F-WR-012/013 |
| `WQN-10` | Unit cost and upkeep | Recruitment cost table and P3.7 readiness upkeep | Table | Provisional — F-WR-015/003 |
| `WQN-11` | Per-operation resource burn | Four-resource supply bundles | Table | Provisional — F-WR-016 |
| `WQN-12` | Infrastructure damage formula and cap | **Adopted for `OP-05` only** — `removed = min(ceil(I × 500/10,000), 20, campaign_headroom, I − 10)`; floor 10; 30% per city per campaign | Formula | Provisional — F-WR-037; `WAR-109a`–`WAR-109m` |
| `WQN-13` | Casualty formula | Strength-point loss by battle tier | Table | Provisional — F-WR-027 |
| `WQN-14` | Loot percentage | **No loot**; consensual reparations only | 25% / 100,000 crowns / 10% resource | Provisional — F-WR-029 |
| `WQN-15` | Improvement-destruction chance | **No improvement or facility destruction exists**; infrastructure levels are not improvements and their damage is the separate WQN-12 rule | Zero | Rejected — `URB-157`, `B10-AD-21`, `WQN-12` |
| `WQN-16` | Post-defeat protection | No new state; B-03 protection only | B-03 values | Resolved by alignment — `B10-AD-19` |
| `WQN-17` | Settlement duration and enforcement | Closed terms, immediate atomic execution, no continuing body; optional 84-turn exclusion | 84 turns for exclusion | Provisional — F-WR-029/031 |
| `WQN-18` | Reparations cap | Caps on unreserved crowns and per-resource share | 25% / 100,000 / 10% | Provisional — F-WR-029 |
| `WQN-19` | Espionage budget and frequency | **Espionage excluded and unassigned**; no owner is identified | None | Closed by exclusion — `B10-AD-24` |
| `WQN-20` | Pre-battle odds disclosure | Odds band for attacker, threat band for defender, full report after | Bands | Provisional — F-WR-032/033 |

`WAR-169` No `WQN` answer is a Nation Supremacy value inherited from Politics & War. Where a P&W figure and an NS figure happen to coincide, the NS figure is justified by the NS economy and marked provisional, not by the coincidence.

### 27.4 Research questions (`WFQ-01`–`WFQ-22`)

| ID | Question | Disposition | B-10 rule |
|---|---|---|---|
| `WFQ-01` | Airstrike cost and resistance values | **Resolved by design** — first-principles `OP-03 AIR_STRIKE` at 3 OP; no P&W values imported | §13.2; `GAP-01` |
| `WFQ-02` | Is the 250% war range live? | **Not applicable** — B-10 has no strength range | `B10-AD-06`; `WCR-02` |
| `WFQ-03` | What happens at expiry? | **Resolved** — deadline, extension, `SETTLING`, expiry outcome | `WAR-020`–`WAR-024` |
| `WFQ-04` | Fixed simultaneous-attack order? | **Resolved** — published order key and frozen baseline | §15.1–§15.2; F-WR-022 |
| `WFQ-05` | Are pre-battle odds shown? | **Resolved** — odds and threat bands | §14.5; F-WR-032/033 |
| `WFQ-06` | Hidden war score beyond the meter? | **Resolved** — no hidden score; progress and outcome are public | §7.3; `B10-AD-09` |
| `WFQ-07` | Does blockade affect production? | **Resolved** — no; blockade affects military supply cost and recovery only | §12.1, `WAR-072` |
| `WFQ-08` | Does radiation affect combat? | **Not applicable** — nuclear weapons and radiation rejected | `B10-AD-23` |
| `WFQ-09` | Do defensive wars follow the same slot rules? | **Resolved** — incoming slot only; defensive operations consume no campaign slot | `WAR-005`, `WAR-007` |
| `WFQ-10` | Can a nation declare on a target whose protection expires mid-war? | **Resolved** — protection is evaluated at declaration and at P2/P5; later expiry does not retroactively validate or void a declaration | `WAR-003`, `WAR-013` |
| `WFQ-11` | Do existing wars continue after defeat? | **Resolved** — a campaign ends at settlement or expiry; no war continues past its terminal state | §6.1, §20 |
| `WFQ-12` | Is there a peace-treaty record? | **Resolved** — the settlement object is the record | §20.1; `WRA-12` |
| `WFQ-13` | Can a blockaded nation receive Alliance-bank transfers? | **Not applicable** — no Alliance treasury or military bank exists | `WAR-161`; ARL is credit-only |
| `WFQ-14` | Are inactive wars auto-peaced? | **Resolved** — dormancy suspends; 48 suspended turns produce `ABANDONED` | `WAR-021`–`WAR-023` |
| `WFQ-15` | Declaration cooldown after peace? | **Resolved** — no automatic cooldown; only an agreed 84-turn exclusion term restricts a new campaign | §20.2; `B10-AD-19` |
| `WFQ-16` | Does war type change resistance reduction? | **Not applicable** — one `STANDARD` profile | `B10-AD-07` |
| `WFQ-17` | Does Fortify stack? | **Resolved** — `OP-07` applies once per battle, does not stack, and expires with the battle | §13.2; §14.4 |
| `WFQ-18` | Does Ground Control transfer between wars? | **Not applicable** — no control state and no cross-campaign effect | `WCR-24` amend |
| `WFQ-19` | Does Air Superiority affect naval battles? | **Not applicable** — no Air Superiority state; `OP-03` affects readiness and supply only | §13.2 |
| `WFQ-20` | How are multiple MAP pools displayed? | **Not applicable** — one national pool | §8.1 |
| `WFQ-21` | Is there a war-exhaustion mechanic? | **Resolved** — none; readiness, deadline and abandonment are the only pressures | §9, §6.3–§6.4 |
| `WFQ-22` | What happens when a participant is deleted mid-war? | **Resolved** — dormant/deleted → suspension → `ABANDONED`; reroll is blocked (`UD-032` Option A) | `WAR-023`, `WAR-025`–`WAR-028` |

`WAR-170` Seven questions are marked **not applicable** because the P&W mechanic they describe does not exist in Nation Supremacy. That is a design answer, not an evidence gap: no further research can change a rule that B-10 deliberately does not have.

### 27.5 Risk register (`WRK-01`–`WRK-15`)

| ID | Risk | Likelihood / impact | Mitigation in B-10 | Rule | Validation | Owner |
|---|---|---|---|---|---|---|
| `WRK-01` | Per-war MAP pools imported, contradicting D-015 | Medium / High | One national pool; per-war, per-campaign and shared pools are expressly prohibited | `WAR-029`–`WAR-032` | §8 tests; `B10-C06` | Closed by B-10 |
| `WRK-02` | P&W numbers copied without NS calibration | High / High | Every value labelled provisional; no P&W value used as justification | §27.3; `WAR-169` | F-WR-035 calibration envelope | Prompt 14 |
| `WRK-03` | Airstrike cost and effect guessed | High / Medium | Designed from first principles as `OP-03`, not imported | §13.2 | Operation contract test | Closed by B-10 |
| `WRK-04` | Fortify enables indefinite stalling | Medium / High | `OP-07` is once per battle, one OP cost, no stacking; attack still resolves | §13.2, §14.4 | `F-WR-026` | Prompt 14 |
| `WRK-05` | One-sided loss model produces a runaway snowball | Medium / High | Loss caps, no loot, **bounded** infrastructure damage (20 levels per strike, 30% per campaign, floor 10, recoverable), recovery by production, 84-turn bound | §16; `B10-AD-16`; `WAR-109d`–`WAR-109e` | F-WR-027/028/037/038 | Prompt 14 |
| `WRK-06` | Slot filling and shield wars | High / High | One outgoing and one incoming slot; no joining; no empty-war reward; blocked/empty wars audited | `WAR-005`, `WAR-007`; §24 | Slot tests; `WRA-06` | Prompt 12 |
| `WRK-07` | Multi-accounting or same-network collusion multiplies slots | Medium / High | One-owner rule at declaration; B-03 identity; evidence fields; no IP-only judgement | `WAR-001`; §24 | Review signal | Prompt 12 |
| `WRK-08` | Coercive settlement terms | Medium / High | Closed term set; prohibited terms; surrender cannot be refused | §20.2–§20.3; `B10-AD-18` | Term-validation tests; `WRF-32` | Prompt 12 |
| `WRK-09` | Loot or reparations mint value | Medium / High | No loot; transfer from unreserved stockpiles only; atomic failure | §11.3, §21 | P7 conservation; `WRF-33` | Prompt 14 |
| `WRK-10` | Alliance command creep | Medium / High | No command, delegation, shared OP, treasury use or declaration for a member | `WAR-161`, §23.2 | Authority tests; `B10-C31` | Closed by B-10 |
| `WRK-11` | Geographic language reintroduces map thinking | High / Medium | Terminology contract; symbolic definitions; naming audit | §4.2; `WAR-168` | Language sweep | Prompt 13 |
| `WRK-12` | Opaque resolution destroys trust | Medium / High | Deterministic baseline, bounded fortune, published bands, full report | §14.5, `WAR-088` | Disclosure tests | Prompt 13 |
| `WRK-13` | Audit or visibility leak | Low / High | Role-based access, no Alliance visibility, redacted block reasons | §23.1; `WAR-148`–`WAR-150` | Negative access tests | Prompt 12 |
| `WRK-14` | Protection durations conflict with B-03 | High / Medium | No new durations; B-03 is authoritative | §18.1 | Duration check | Closed by B-10 |
| `WRK-15` | Reroll escapes a losing campaign | Medium / High | `UD-032` Option A: reroll remains blocked; surrender is the off-ramp | `WAR-025`–`WAR-028`; `B10-AD-20` | Reroll tests | Closed by B-10 |

`WAR-171` Every risk is either closed by a B-10 rule or carries a named downstream owner. No risk is assigned to Prompt 10B itself.

### 27.6 External evidence conflicts (`WFX-01`–`WFX-12`)

| ID | Conflict | Kind | Disposition | Why |
|---|---|---|---|---|
| `WFX-01` | Plane cost/upkeep, two published versions | P&W fact conflict | **Carried** as P&W evidence status | NS has no planes as individual units; no NS value depends on the winner |
| `WFX-02` | Missile/nuke cost | P&W fact conflict | **Carried** | NS missile cost is designed, not imported |
| `WFX-03` | Ship operating resources | P&W fact conflict | **Carried** | NS supply bundles are designed |
| `WFX-04` | Missile infrastructure cap | P&W fact conflict | **Carried** as P&W evidence status | NS now has its own cap (`WAR-109e`, `F-WR-037`); no P&W value is imported |
| `WFX-05` | Aggressor/defender effect | P&W finding | **Adopted as context** | NS has no role bonus; only operations and readiness matter |
| `WFX-06` | 250% war range unverified | External evidence gap | **Closed as irrelevant** | No strength range exists |
| `WFX-07` | War expiry routine unknown | External evidence gap | **Closed by design** | `WAR-020`–`WAR-024` define expiry completely |
| `WFX-08` | No settlement object in P&W | P&W absence finding | **Closed by design** | §20 creates the object |
| `WFX-09` | Airstrike values missing | External evidence gap | **Closed by design** | `OP-03` designed from first principles |
| `WFX-10` | P&W NAP enforcement unverified | External evidence gap | **Closed as irrelevant** | B-08 `DP-T01` is the authoritative NAP rule |
| `WFX-11` | PWPedia vs Fandom authority | Evidence-method conflict | **Applied** | Official source wins; recorded in 10A, not re-decided here |
| `WFX-12` | No live declaration screen observed | Observation gap | **Open — no NS dependency** | B-10 defines its own validator and copy requirements |

`WAR-172` No conflict in this table was closed by inventing evidence. The distinction is preserved: a P&W fact conflict stays a P&W fact conflict; an NS design choice is labelled as an NS design choice; an unresolved external gap stays open when nothing in B-10 depends on it.

### 27.7 P&W-to-Nation-Supremacy classification (`WFC-01`–`WFC-26`)

| ID | P&W mechanic | In B-10 | Rule |
|---|---|---|---|
| `WFC-01` | Resistance race | **Adapted** — per-side objective progress | §7.2 |
| `WFC-02` | Unilateral declaration | **Adopted** with cumulative validation | §5.3 |
| `WFC-03` | Three war types | **Rejected** — one `STANDARD` profile | `B10-AD-07` |
| `WFC-04` | Score window 75–250% | **Not applicable** — no strength gate | `B10-AD-06` |
| `WFC-05` | 5/3 war slots | **Adapted** — 1 outgoing / 1 incoming | `B10-AD-02` |
| `WFC-06` | Per-war MAP pools | **Rejected** — one national OP pool | §8.1 |
| `WFC-07` | 60-turn bound | **Adapted** — 84 turns + one extension | `B10-AD-05` |
| `WFC-08` | Three-roll 40–100% with tiers | **Adapted** — one seeded ±500 bp roll, five tiers | §14.3 |
| `WFC-09` | Control states | **Adapted** — BLOCKADE and AIR as symbolic conditions, not zones | §4.2, §13.2 |
| `WFC-10` | Ground battle | **Adapted** — `OP-02 ASSAULT` and `OP-01 RAID` | §13.2 |
| `WFC-11` | Airstrike | **Replaced by first-principles design** — `OP-03` | §13.2 |
| `WFC-12` | Naval battle | **Adapted** — `UNIT-NAV` pool and `OP-04 BLOCKADE`; no sea zone | §10.1, §13.2 |
| `WFC-13` | Missiles | **Adapted** — `OP-05 MISSILE_STRIKE` against a city-as-asset, no facility damage | §13.2; `B10-AD-21` |
| `WFC-14` | Nuclear weapons and radiation | **Rejected** | `B10-AD-23` |
| `WFC-15` | Fortify | **Adapted** — `OP-07`, once per battle, no stacking | §13.2 |
| `WFC-16` | Espionage | **Not applicable** — excluded and unassigned | `B10-AD-24` |
| `WFC-17` | Offer peace | **Adapted** — ceasefire plus closed-term settlement | §19, §20 |
| `WFC-18` | Victory loot | **Adapted** — no loot; consensual reparations | §21 |
| `WFC-19` | Infrastructure and improvement damage | **Adapted** — city infrastructure levels only; no improvement or facility destruction | `B10-AD-21`; `WAR-109a`–`WAR-109m`; `URB-157` |
| `WFC-20` | Units, caps, recruitment, upkeep | **Adapted** — four pools, training capacity, readiness upkeep | §10, §9.2 |
| `WFC-21` | Military research | **Rejected** — development tiers only | `B10-AD-22` |
| `WFC-22` | Ten war policies | **Rejected** — no policy set | `B10-AD-07` |
| `WFC-23` | Beige and new-nation protection | **Adapted** — B-03 only | §18.1 |
| `WFC-24` | No alliance war or delegated command | **Adopted** | `WAR-161` |
| `WFC-25` | Moderation of war abuses | **Transferred** — taxonomy to Prompt 12, evidence retained | §24 |
| `WFC-26` | Mapless conflict as a precedent | **Adopted** | §4.2 |

`WAR-173` Classification counts for B-10: **3 adopted in substance** (`WFC-02`, `WFC-24`, `WFC-26`), **14 adapted** (`WFC-01`, `WFC-05`, `WFC-07`–`WFC-10`, `WFC-12`, `WFC-13`, `WFC-15`, `WFC-17`–`WFC-20`, `WFC-23`), **5 rejected** (`WFC-03`, `WFC-06`, `WFC-14`, `WFC-21`, `WFC-22`), **2 not applicable** (`WFC-04`, `WFC-16`), **1 replaced by design** (`WFC-11`), **1 transferred** (`WFC-25`). Total 26. The rule reference is authoritative in every row.

### 27.8 Local evidence gaps (`GAP-01`–`GAP-16`)

| ID | Gap | Disposition | Rule or owner |
|---|---|---|---|
| `GAP-01` | Airstrike cost and effect | **Closed by design** | `OP-03` at 3 OP, provisional (§13.2) |
| `GAP-02` | Live declaration screen fields | **Open — no NS dependency** | B-10 defines its own validator and confirmation minimum (`WAR-152`) |
| `GAP-03` | War expiry routine | **Closed by design** | `WAR-020`–`WAR-024` |
| `GAP-04` | Settlement enforcement and duration | **Closed by design** | §20–§21 |
| `GAP-05` | Whether the 250% range is live | **Closed as irrelevant** | No strength range (`B10-AD-06`) |
| `GAP-06` | Complete July 2025 changelog | **Open — P&W evidence only** | No NS rule depends on it |
| `GAP-07` | Unit-page revision dates | **Open — P&W evidence only** | No NS rule depends on it |
| `GAP-08` | Missile 300/350 wording | **Closed by design** | NS designs its own damage cap (`WAR-109d`–`WAR-109e`); no P&W value imported |
| `GAP-09` | Parentheses in published damage formulas | **Closed as irrelevant** | No P&W damage formula is used |
| `GAP-10` | Simultaneous action ordering | **Closed by design** | §15; F-WR-022 |
| `GAP-11` | Pre-battle odds disclosure | **Closed by design** | §14.5; `B10-AD-25` |
| `GAP-12` | Alliance coordination practice | **Open — social evidence only** | B-10 permits no military coordination (`WAR-161`) |
| `GAP-13` | Moderation evidence standard and appeals | **Transferred — Prompt 12** | B-12 owns fair-play process |
| `GAP-14` | DEFCON mechanics | **Closed as irrelevant** | No DEFCON state |
| `GAP-15` | Repair and rebuild rates | **Closed by design** | Strength recovery by recruitment only (§17.2); city infrastructure repair is a separate B-05 capex order (`URB-046`, `WAR-109h`) |
| `GAP-16` | Any war-exhaustion equivalent | **Closed by design** | No exhaustion mechanic (`WFQ-21`) |

`WAR-174` The five gaps the 10A handoff named — `GAP-01`, `GAP-03`, `GAP-04`, `GAP-10`, `GAP-11` — are all closed by an explicit B-10 rule, not by waiting for evidence. `GAP-13` is the only gap transferred to a named owner.

### 27.9 10A handoff completion (`WFH-A1`–`WFH-F6`)

**A. Preserved constraints**

| ID | Requirement | Evidence of preservation |
|---|---|---|
| `WFH-A1` | Rulebook, not research | This document states rules; every evidence citation points to 10A rather than restating its catalogue |
| `WFH-A2` | Strict mapless design | §4.2, `WAR-168`; no distance, route, coordinate, front, border, movement or capture anywhere in §5–§24 |
| `WFH-A3` | D-015 national OP model | §8.1; one pool, military-only, +1 regenerated at P3.7 and carried below the cap (amended 2026-11-04), non-transferable, reserve at acceptance, consume at resolution |
| `WFH-A4` | Explicit UD-032 resolution | §6.5; `B10-AD-20`; Option A with full rationale |
| `WFH-A5` | No Alliance military authority | `WAR-161`; §23.2; no command, delegation, shared pool, treasury use or declaration |
| `WFH-A6` | Values provisional until Prompt 14 | Every table tagged; F-WR-035 calibration envelope |

**B. Architecture decisions**

| ID | Decision needed | Resolution | Location |
|---|---|---|---|
| `WFH-B1` | Campaign model | Layered `WAR` → one `CAMPAIGN` → objectives and operations | `B10-AD-01` |
| `WFH-B2` | Progress model | Per-side objective progress inside one campaign; OP stays national | `B10-AD-03`/`B10-AD-04` |
| `WFH-B3` | Posture model | One immutable `STANDARD` profile, no war types | `B10-AD-07` |
| `WFH-B4` | Operation catalogue and OP costs | Nine operations, 1–4 OP | `B10-AD-10`; §13 |
| `WFH-B5` | Resolution and odds disclosure | Deterministic power + seeded fortune; odds and threat bands | `B10-AD-15`/`B10-AD-25` |
| `WFH-B6` | Termination and settlement | Victory, expiry, ceasefire, closed-term settlement, surrender; `UD-032` Option A | `B10-AD-18`/`B10-AD-20`; §19–§21 |

**C. Structure**

| ID | Requested section | Delivered as |
|---|---|---|
| `WFH-C1` | Purpose, scope, constraints, mapless conformance | §1–§4 |
| `WFH-C2` | Declaration, eligibility, protection, validation | §5, §18 |
| `WFH-C3` | Campaign states, objectives, duration, expiry | §6–§7 |
| `WFH-C4` | Operations, OP, readiness, units, resources | §8–§13 |
| `WFH-C5` | Resolution, control, counterplay, losses | §14–§17 |
| `WFH-C6` | Termination, settlement, postwar, audit, open questions | §19–§24, §26–§27 |

**D. Constraints and invariants**

| ID | Invariant | Status |
|---|---|---|
| `WFH-D1` | Reserve at acceptance; consume at resolution; no mutation outside a declared phase | **Preserved** — §8.1, §15; `WAR-005a`, `WAR-040`–`WAR-043b`, `WAR-063` |
| `WFH-D2` | No minting; all value moves through the B-04 ledger | **Preserved** — §11.3, §21 |
| `WFH-D3` | No city loss; infrastructure and improvements may be damaged | **Amended — infrastructure adopted, improvements rejected.** `OP-05` may damage **city infrastructure levels** only, capped and recoverable; no improvement or facility is damaged; no city is lost (`WAR-109a`–`WAR-109m`, `B10-AD-21`, `B10-C23`) |
| `WFH-D4` | Cumulative validation: restricted pair, protection, national NAP, Alliance NAP, same-alliance | **Preserved** — `WAR-009` steps 3–7 |
| `WFH-D5` | Fail closed; blocked attack moves nothing; mandatory `AUD-AL-017` on B-09 blocks | **Preserved** — `WAR-013`, `WAR-014` |
| `WFH-D6` | No delegation, no collective power, no Alliance spending of member resources | **Preserved** — `WAR-161` |

`WAR-175` `WFH-D3` is the only handoff invariant amended rather than preserved. The amendment is **narrower than the handoff text** in one direction and **wider in another**: it adopts infrastructure damage (which 10A suggested) under strict caps and a floor, and it rejects improvement/facility damage (which 10A also suggested). City loss remains prohibited. No new currency, score or location is created, and the no-city-loss baseline is unchanged.

**E. Acceptance criteria**

| ID | Criterion | Evidence |
|---|---|---|
| `WFH-E1` | Two nations can fight a bounded war with a readable outcome | §5–§7, §14; outcome set is public |
| `WFH-E2` | There is a way to stop | Ceasefire, mutual peace, expiry, surrender, abandonment (§19–§20) |
| `WFH-E3` | No infinite one-sided attrition | 20%/60% loss caps, 84-turn bound, readiness gate, surrender off-ramp |
| `WFH-E4` | Every offensive operation has a declared counter | §13.2, §18.2 counter matrix |
| `WFH-E5` | Every attack path is covered by the cumulative validator | `WAR-009`; the validator is the only entry point |
| `WFH-E6` | Every number is provisional and traceable | §27.3; F-WR-035 |

**F. Open questions carried into 10B**

| ID | Question | Resolution |
|---|---|---|
| `WFH-F1` | Airstrike cost/effect | `OP-03` at 3 OP; provisional |
| `WFH-F2` | War expiry routine | 84 + 42 turns, `SETTLING`, expiry outcome |
| `WFH-F3` | Simultaneous ordering | Published key, frozen baseline, damage carry |
| `WFH-F4` | Pre-battle odds disclosure | Odds and threat bands, full report after |
| `WFH-F5` | Settlement enforcement and duration | Immediate atomic execution; optional 84-turn exclusion |
| `WFH-F6` | UD-032 option | Option A — retain the reroll block; surrender is the off-ramp |

`WAR-176` All 36 handoff items are dispositioned. Nothing in the 10A handoff is left as an unstated assumption: the six constraints are quoted and met, the six decisions are named, the six structure items are delivered, the six invariants are checked (one amended), the six acceptance criteria are evidenced, and the six open questions are answered.

---

## 28. Formula register references

`WAR-177` The authoritative statement of every B-10 formula is the [warfare formula register](17_warfare_formula_register.md). This section is an index only. Where this rulebook describes a calculation in prose, the register's expression is the operative definition; if the two ever diverge, the register wins and this rulebook is corrected.

`WAR-178` Every formula below is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** except where the type column says **Structural**. A structural formula is a definition, not a balance value: changing its constants is calibration, changing its shape is an architecture change.

| ID | Formula | Rulebook anchor | Type |
|---|---|---|---|
| `F-WR-001` | OP availability, regeneration and cap | §8.1, `WAR-039`–`WAR-043b` | Structural (cap and rate provisional) |
| `F-WR-002` | OP reservation lifecycle (`HELD` → `CONSUMED` / `RELEASED`) | §8.1, `WAR-005a`, `WAR-042` | Structural |
| `F-WR-003` | Readiness upkeep debit and obligation settlement at P3.7 | §9.2, §11.2, `ECN-152` | Provisional |
| `F-WR-004` | Cumulative declaration eligibility | §5.3, `WAR-009` | Structural |
| `F-WR-005` | Readiness value and gate evaluation | §9.1, `WAR-047`–`WAR-053` | Provisional |
| `F-WR-006` | Campaign slot occupancy | §5.2, `WAR-005`/`WAR-007` | Provisional |
| `F-WR-007` | Campaign deadline and extension | §6.3, `WAR-018`–`WAR-020` | Provisional |
| `F-WR-008` | Inactivity warning and abandonment threshold | §6.3–§6.4, `WAR-016`, `WAR-021`–`WAR-024` | Provisional |
| `F-WR-009` | Objective progress accumulation and clamp | §7.2 | Provisional |
| `F-WR-010` | Victory determination order | §7.3, `WAR-037`–`WAR-038` | Structural |
| `F-WR-011` | Progress-bearing resolution cap | §7.2, `WAR-035` | Provisional |
| `F-WR-012` | Force cap | §10.3 | Provisional |
| `F-WR-013` | Training capacity | §10.3 | Provisional |
| `F-WR-014` | Single-type force-share cap | §10.3 | Provisional |
| `F-WR-015` | Recruitment cost and arrival | §10.3, `WAR-058`–`WAR-060` | Provisional |
| `F-WR-016` | Operation supply-bundle requirement | §12.2, `WAR-066`–`WAR-070`, `WAR-053f` | Provisional |
| `F-WR-017` | Denial surcharge and readiness penalty | §12.1, `WAR-071` | Provisional |
| `F-WR-018` | Blockade supply and recovery modifier | §12.1, `WAR-072` | Provisional |
| `F-WR-019` | Total action cost (declaration and operation) | §5.2, §13.1, §8.2 | Provisional |
| `F-WR-020` | Readiness factor in combat | §14.2 | Provisional |
| `F-WR-021` | Base combat ratio | §14.2 | Structural (constants provisional) |
| `F-WR-022` | Deterministic order key, frozen baseline and battle seed | §15.1–§15.2 | Structural |
| `F-WR-023` | Seeded fortune draw | §14.3 | Provisional |
| `F-WR-024` | Effective combat score | §14.3 | Structural |
| `F-WR-025` | Battle-tier classification | §14.3 | Provisional |
| `F-WR-026` | Counter modifier application | §14.4 | Provisional |
| `F-WR-027` | Strength-point loss calculation | §16.2 | Provisional |
| `F-WR-028` | Per-battle and per-campaign loss caps | §16.2 | Provisional |
| `F-WR-029` | Reparation caps and atomic settlement | §21.1, `WAR-137`–`WAR-140` | Provisional |
| `F-WR-030` | Ceasefire and settlement proposal window | §19.1, §20.1 | Provisional |
| `F-WR-031` | Exclusion duration and disarmament partial cancellation | §20.2, §20.4 | Provisional |
| `F-WR-032` | Odds band disclosure | §14.5, `WAR-085`–`WAR-088` | Provisional |
| `F-WR-033` | Threat band disclosure | §14.5, `WAR-086` | Provisional |
| `F-WR-034` | P5 execution validity, idempotency and failure | §15.4, §24.2 | Structural |
| `F-WR-035` | Calibration envelope and parameter ownership | §27.3, Prompt 14 handoff | Structural (contains every provisional value) |
| `F-WR-036` | Military food ration | §9.3, `WAR-053a`–`WAR-053i` | Structural (rates provisional) |
| `F-WR-037` | City infrastructure damage | §16.4, `WAR-109a`–`WAR-109f` | Structural (constants provisional) |
| `F-WR-038` | Infrastructure asset impairment and repair | §16.4, `WAR-109f`–`WAR-109m`, `URB-043`/`URB-044`/`URB-118a`/`URB-118b` | Structural (constants provisional) |
| `F-WR-039` | Combined supply modifier | §12.1, `WAR-071`–`WAR-072` | Structural (rates provisional) |

`WAR-179` Each register entry carries the 20 mandatory fields: identifier, name, purpose, exact expression, input variables with types and ranges, output type and range, rounding and integer rules, clamping, worked example, boundary example, failure behaviour, determinism and seed rule, phase and trigger, mutation owner, visibility, audit event, provisional status, calibration owner, source rule, and downstream consumer.

`WAR-180` No formula in this list introduces a new resource, currency, score or ledger type. Inputs come from §4.1 entities, the B-04 resource roster, readiness and objective progress. An output that would need a new type is a design error, not a missing formula.

---

## 29. Prompt 10C handoff

`WAR-181` Prompt 10C owns workflows, acceptance cases and traceability. It receives the following from B-10 and **must not invent** campaign architecture, OP economics, battle formulas, operation costs, settlement logic or permissions.

### 29.1 What 10C receives

| # | Input | Source | 10C use |
|---|---|---|---|
| 1 | Complete campaign state machine | §6.1–§6.2, `WAR-015`–`WAR-019` | State-transition cases and terminal-state coverage |
| 2 | Complete operation state machine | §13.2, §15.1 | Per-operation order, resolution, cancellation and failure paths |
| 3 | Declaration and eligibility rules | §5, `WAR-001`–`WAR-014` | Twelve-check validator cases, one per check and one per block |
| 4 | Every operation's prerequisites, costs, effects and counter | §13.1–§13.2 | One positive and one negative case per operation, including a city-targeted `OP-05` |
| 5 | Exact OP reservation and consumption | §8, `WAR-029`–`WAR-034` | Ledger-state cases, including release on failure |
| 6 | Readiness and resource requirements | §9, §11, §12 | Gate cases, upkeep cases, bundle cases, military Food ration cases |
| 7 | Battle-resolution formulas | §14; F-WR-020–F-WR-028 | Worked-example cases at tier boundaries |
| 8 | Victory and expiry conditions | §7.3–§7.4, §6.3 | Outcome matrix, including expiry and abandonment |
| 9 | Losses and recovery | §16–§17; F-WR-037–F-WR-038 | Cap cases, recovery cases and infrastructure-damage/repair cases |
| 10 | Peace, surrender and settlement rules | §19–§20 | Proposal, counter, acceptance, rejection, expiry, white peace |
| 11 | Protection and reroll outcomes | §18, §6.5 | Every attack path against every protection state, including a protection change between P2 and P5; `UD-032` Option A |
| 12 | All block and failure codes | §5.4, §24.2, `WRF-01`–`WRF-37` | One case per code, with the state proving nothing moved |
| 13 | Visibility and audit rules | §23–§24, `WAR-148`–`WAR-156` | Positive and negative access cases |
| 14 | Simultaneous-action ordering | §15, F-WR-022 | Two-attacker, two-defender, cross-campaign ordering cases |
| 15 | Interrupted-P5 recovery | §15.4, `WRF-34` | Replay, partial-failure and idempotency cases |
| 16 | Cross-system integration contracts | §25.1–§25.4 | Bidirectional traceability, B-02 through Prompt 15, plus the Food and infrastructure matrices |
| 17 | Formula and example references | §28; F-WR register | Exact inputs and expected outputs for every formula |
| 18 | Unresolved downstream and owner-reserved boundaries | §3.4, §27.9 | Cases must assert that no owner-reserved policy is decided by a workflow |

### 29.2 Required workflow coverage

**States.** Campaign (`DECLARED_PENDING`, `ACTIVE`, `SETTLING`, `SUSPENDED`, `ENDED`, `ARCHIVED`, `VOID`); operation (submitted, reserved, validated, resolved, cancelled, failed, released); block (each `WRF` code); settlement (`PROPOSED`, `COUNTERED`, `ACCEPTED`, `REJECTED`, `WITHDRAWN`, `EXPIRED`, `COMPLETED`, `FAILED`); termination (victory, draw, expiry, abandonment, surrender); recovery (readiness, strength, interrupted P5).

**Happy paths.** Declaration → reservation → P2 revalidation → P5 resolution → operation → battle → progress → victory/expiry → settlement → postwar record. A second path covers declaration → suspension → abandonment. A third covers declaration → ceasefire → white peace.

**Permission failures.** Restricted pair, newcomer protection, dormancy, national `DP-T01` NAP, same-Alliance, Alliance `AT-E01` NAP, political `TRANSITION`/`CRISIS`, no outgoing slot, insufficient OP, insufficient unreserved crowns, invalid target, invalid city target, insufficient supply bundle, readiness gate, military Food shortfall (`RATION_SHORT`), duplicate submission.

**Edge cases.** Membership change at a boundary; NAP expiry during a campaign; protection becoming active between P2 and P5; reroll during a campaign (`UD-032` Option A); target protection expiring mid-campaign; simultaneous attacks from two campaigns; expiry on the same turn as a victory threshold; settlement accepted on the deadline turn; dormancy of the declarer at P0; deletion of a belligerent; blockade and break in the same turn; a nation both denied and blockaded paying the capped 50% surcharge; `INTERCEPT` against a `MISSILE_STRIKE`; `OP-05` against a city with capacity overdraw and with a repair order at the same P4.1; loss cap reached mid-campaign.

**Recovery.** Failed P5 phase, interrupted turn, uncommitted reservation release, committed resolution replay, duplicate-run refusal, checkpoint resume at the last committed sub-phase, and the rule that no partial battle state is visible before `WRA-04`.

**Matrix.** Bidirectional and exhaustive: every rule has at least one case, every case cites a rule, and no `WAR-`, `WRF-`, `WRA-` or `F-WR-` identifier is orphaned. 10C reports coverage counts and lists any unclosed identifier rather than silently omitting it.

**Boundary.** Workflows are specifications, not code. Tests are defined, not executed. 10C must not claim a runtime result.

**Must not add.** No new Alliance rule, no NAP coverage or consent rule, no treasury-spending authority, no appeal right, no change to D-015, no resolution of `UD-040`–`UD-049`, and no renaming of a B-10 state or code.

### 29.3 Downstream prompt handoffs

| Prompt | Receives from B-10 | Must not assume |
|---|---|---|
| **Prompt 11** — world events, objectives, rankings | `WRA-13` war events, objective totals, outcome records, settlement records, ranking inputs | That a P&W war score or resistance meter exists |
| **Prompt 12** — fair play, protection, privacy, administration | Abuse evidence fields, block records, `AUD-AL-017` duties, prohibited-behaviour candidates (`WCR-33`), audit access implementation (`WCR-44`), `GAP-13` | That P&W's moderation model or penalties apply |
| **Prompt 13** — interface and journeys | Operations board content, confirmation minimum (`WAR-152`), odds and threat bands, timeline visibility, settlement screens, failure copy | That the interface may hide a block instead of explaining it |
| **Prompt 14** — formulas and balance | F-WR-001–F-WR-039, every provisional value, boundary examples, simulation needs (`WRK-02`, `WRK-05`, `WRK-08`) | That a P&W number is an NS value |
| **Prompt 15** — Bible assembly | §25 integration matrix, `WAR-157`–`WAR-163`, §26 decisions and conflicts, canonical references | That P5 may mutate another subsystem outside its phase |

`WAR-182` No core warfare design decision is transferred to a downstream prompt. The transfers in §29.3 are *presentation*, *process* and *assembly* work that depends on B-10 but cannot change it.

---

## 30. Completion and limitation statement

### 30.1 What is complete

`WAR-183` B-10 is **complete at the specification level**. It defines, to the level of an implementable rule:

1. A closed object model (`WAR` → one `CAMPAIGN` → objectives, operations, battles, settlement) with no mapless violation.
2. A twelve-step cumulative declaration and hostile-action validator that preserves every B-03, B-08 and B-09 block, runs at submission, P2 and pre-P5, and fails closed.
3. A seven-state campaign machine with a deadline, one extension, inactivity handling, dormancy suspension and full attribution on cleanup.
4. Six objectives, a per-side progress model, a deterministic victory order and a complete outcome set.
5. One national OP pool under D-015 as amended on 2026-11-04, held as a persistent national ledger that regenerates one OP at the P3.7 opening of each boundary, carries below the cap, and has reservation, consumption, release and void rules with an explicit prohibition on per-war, per-campaign and shared pools.
6. One readiness value with declared inputs, gates and a combat role that is not an economic multiplier.
7. Four strength-point force pools, a force cap, a training capacity, a type-share cap, recruitment timing and a recurring military Food ration with soldier-equivalent conversion.
8. A four-resource supply model with no geography, one combined denial-and-blockade surcharge and a separately bounded readiness-recovery penalty.
9. A closed nine-operation catalogue in which every offensive operation has a declared counter.
10. A deterministic-plus-bounded-fortune battle model with published odds and threat bands and a complete battle report.
11. A total ordering contract at P5, a frozen baseline, one dependency and complete idempotency.
12. Bounded losses — strength, readiness and city infrastructure — recovery paths and a settlement framework with closed terms, prohibited terms, surrender, immediate enforcement and reparations caps.
13. No new protection state, no Alliance military authority and no Alliance treasury role.
14. A complete audit event set, failure code set and visibility matrix.
15. A 28-row cross-system contract matrix with seven invariants, plus dedicated Food-upkeep and infrastructure-damage integration matrices.
16. A disposition for every 10A identifier in eight families, and a complete decision and conflict register.
17. A 39-formula index cross-referenced to a dedicated register.

### 30.2 What is not complete and is not claimed

`WAR-184` B-10 does **not** claim any of the following:

- **No implementation.** No code, schema, migration, endpoint, interface or configuration was produced.
- **No gameplay or integration test.** No battle, declaration, settlement, reroll, block, P5 recovery, database, browser, load or multiplayer behaviour was executed.
- **No numeric approval.** Every non-structural value is provisional. B-10 defines the shape of the calculation and the owner of the number, not the final number.
- **No balance evidence.** No simulation was run. The loss caps, OP costs, progress values, reparations caps and readiness gates are untested design choices.
- **No owner decision.** The only unresolved decision B-10 resolves is `UD-032`, under the authority recorded in `05_unresolved_design_decisions.md`. `UD-040`–`UD-049` remain Open and owner-reserved. No treasury spending, membership policy, appeal right, delegation or other owner-reserved policy is approved here.
- **No 10C acceptance suite.** B-10 does not create the 10C workflow companion; §29 hands the material to Prompt 10C, which owns the workflows and the acceptance matrix.
- **No P&W value imported as an NS value.** Where an NS number resembles a P&W number, the NS justification is economic and provisional, never evidentiary.

### 30.3 Known limitations

| # | Limitation | Consequence | Owner |
|---|---|---|---|
| 1 | All balance values are untested | A coherent rulebook can still produce a poor game; Prompt 14 must calibrate and simulate | Prompt 14 |
| 2 | 10A's numeric evidence is partially outdated and its air and odds evidence was incomplete | B-10 designs those areas from first principles; the design carries no evidentiary authority from P&W | Prompt 14 / 15 |
| 3 | No live interface observation exists | Confirmation, timeline and failure copy are specified as content, not as an observed screen | Prompt 13 |
| 4 | Strength is a four-pool abstraction, not individual units | The model cannot express unit composition or per-unit readiness; that is a deliberate scope cut. Military Food demand is therefore expressed in soldier-equivalents, not headcount | Future expansion decision |
| 5 | No military building or research branch | Military growth is capped by development tier, recruitment capacity and resources; a future expansion needs a new owner decision | Future expansion |
| 6 | Infrastructure damage is bounded; facility damage is not designed | `OP-05` can reduce city infrastructure and impair book value, but no facility is damaged or destroyed and no city is captured or deleted; facility damage and direct population casualties remain prohibited without a separate B-05 owner decision | B-05 / Future expansion |
| 7 | Espionage is excluded and unassigned | Covert play has no owner and no economy; its absence is recorded, not hidden | Roadmap |
| 8 | `UD-032` Option A keeps rerolls blocked during a campaign | A player in a losing campaign must surrender or wait; this is a deliberate integrity choice, not an oversight | B-03 / Prompt 10C tests |
| 9 | Documentation validation only | The validators in §30.5 check structure, identifiers and cross-references, not runtime behaviour | Stage 3+ |

### 30.4 Owner-reserved boundaries preserved

`WAR-185` B-10 touches none of the following, and no workflow, example or formula in this document may be read as deciding them: `UD-040` (multiple membership), `UD-041` (office template), `UD-042` (membership policy), `UD-043` (succession and removal), `UD-044` (appeal policy), `UD-045` (the rest of the Alliance capability catalogue beyond the narrow tax-management authorization), `UD-046` (Alliance Treasury ownership, custody, capacity and spending), `UD-047` (collective diplomacy), `UD-048` and `UD-049`.

`WAR-186` The Alliance Receiving Ledger remains a credit-only receipt boundary. It is not a military treasury, it cannot fund an operation, it cannot pay a reparation and it cannot guarantee a settlement. No B-10 rule reads or writes it.

### 30.5 Validation status

`WAR-187` B-10 was checked with the project's documentation validators, including the dedicated `qa_backups/10B_validate_warfare.py`, for section completeness, identifier uniqueness, disposition arithmetic, cross-reference resolution, formula-field completeness, register counts and boundary language. The exact commands and their actual results are recorded in the completion report and in the Stage 2 progress log. Only documentation checks were run. No runtime, gameplay, database, browser, security, load or live-integration test was performed, and none is claimed.

### 30.6 Completion statement

`WAR-188` **Prompt 10B is complete at the specification and documentation level.** The B-10 rulebook and its formula register exist, cover all 30 required topics, disposition every 10A research identifier, preserve every binding constraint, resolve `UD-032` explicitly, and hand a complete rule set to Prompt 10C for workflow construction and to Prompt 14 for calibration. B-10 is not implemented, not balanced, not playtested and not released. The next task is **Prompt 10C — warfare workflows, acceptance cases and traceability**.
