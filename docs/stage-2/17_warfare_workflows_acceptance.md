# B-10 warfare — workflows, cross-system integration and acceptance

**Version:** 1.0 · **Created:** 2026-11-04 · **Stage 2, Prompt 10C**
**Status:** **Acceptance specification — design only.** It specifies what a future implementation must do and how that behaviour is to be tested. No warfare code, database schema, endpoint, screen, scheduler, migration or deployment exists. **No test below has been executed as a runtime test.** Nothing here is release-approved, balanced or playtested.
**Authority:** [B-10](17_warfare_and_settlements.md) **v1.3** owns the warfare rules; [the warfare formula register](17_warfare_formula_register.md) **v1.3** owns every calculation; [the 10A research report](research/10A_politics_and_war_warfare_research.md) is evidence, never a rule source. **This document** owns the workflows (`WFW-`), the player journeys (`J1`–`J17`), the edge-case catalogue (`WFE-`), the failure-to-workflow map, the concurrency and security acceptance criteria, the acceptance matrix (`WFA-`) and the evidence register. It adds **no** mechanic of its own; where a workflow and a rule disagree, B-10 wins and this document is corrected.
**Sovereignty rule (WAR-001, WAR-151):** the human player has authority over the military decisions of their own nation. The game validates, informs, records and enforces authorized decisions; it never declares, operates, surrenders or settles for a player, never infers consent from silence, and never lets an Alliance, an office, a treaty, a ballot, an AI or an administrator act for a nation.
**Companions:** [B-10](17_warfare_and_settlements.md) · [formula register](17_warfare_formula_register.md) · [10A research](research/10A_politics_and_war_warfare_research.md) · [requirements](03_requirements_traceability.md) · [decisions](04_approved_and_provisional_decisions.md) · [unresolved](05_unresolved_design_decisions.md) · [Stage 2 handoff](00_stage_2_handoff.md) · [progress log](06_stage_2_progress_log.md)

---

## 1. Scope, authority and reading order

**1.1 What this document is for.** Prompt 10B decided the warfare model: seven campaign states, six objectives, nine operations, one national Operations Points pool, a twelve-check cumulative hostile-action validator, readiness and a recurring military Food ration, a closed four-resource supply model, a deterministic-plus-bounded-fortune battle model, bounded losses including capped city-infrastructure damage, eight settlement states and six settlement terms, fourteen audit events and a `WRF-01`–`WRF-37` failure-code span with thirty-two defined codes. Prompt 10C must show that the model can be **operated**: who acts, in which order, what the player sees before confirming, what the server validates and persists, which boundary step resolves it, which record is written, which failure is returned, and which acceptance test would prove it.

**1.2 What it is not.** It is not a second rulebook and does not redefine a state, a value, a permission or a limit. It does not implement a screen: a view description is a specification input, not an application. It does not turn a specification-level scenario into a passed test. It does not resolve an owner decision, and it does not design Prompt 11's world events, Prompt 12's enforcement policy, Prompt 13's screens or Prompt 14's calibration.

**1.3 Reading order for a new session.** Read [B-10](17_warfare_and_settlements.md) §1–§9 first, then the [formula register](17_warfare_formula_register.md) §3–§4, then this document §2–§4 for the canonical semantics, then the workflow for the task at hand, then the matrix row for every rule being implemented. Use the [10A report](research/10A_politics_and_war_warfare_research.md) to understand an evidence gap or a player-experience risk, never to import a mechanic.

**1.4 Status vocabulary.** **Specified** means the behaviour is written down and traceable; **test-designed** means a scenario exists but has not run; **document-checked** means a consistency or identifier check in `qa_backups/` ran and passed; **runtime-tested** and **playtested** mean what they say and are **not claimed anywhere in this document**.

**1.5 Identifier spaces introduced here.** Workflows **`WFW-001`…`WFW-040`**; player journeys **`J1`…`J17`**; edge cases **`WFE-001`…`WFE-060`**; acceptance tests **`WFA-001`…`WFA-124`**. None of these is a game rule: a `WFW`/`J`/`WFE`/`WFA` row is a specification artefact, and every rule it exercises carries its own `WAR-`/`WRF-`/`WRA-`/`F-WR-` identifier from B-10 and its register.

**1.6 Counts in this document (verified by `qa_backups/verify_warfare_workflows.py`).** 25 lifecycle steps, 40 workflows, 17 player journeys, 60 edge cases, 124 acceptance tests in 16 classes (A–O with eight each, plus P with four supplementary coverage tests), 9 operations, 32 defined failure codes in the `WRF-01`–`WRF-37` span (`WRF-15`–`WRF-19` unallocated, §10.2), 14 audit events, 39 formulas, 25 architecture decisions, 34 conflict entries, 230 `WAR-` identifiers (188 numbered plus 42 lettered sub-rules), 50 warfare requirements (`REQ-654`–`REQ-703`) and 13 subsystem/prompt integration rows. §14.2 records **50 requirement relationships**: **44 DIRECT VERIFICATION**, **1 SUPPORTING VERIFICATION** (`REQ-672`) and **5 DEFERRED** (`REQ-673`–`REQ-677`, owned by Prompts 11–15). No requirement is **NOT COVERED** at this level.

**1.7 Fixed constraints this document may not vary.**

1. **Documentation only.** No code, schema, endpoint, interface, scheduler, deployment or configuration is authorized by 10C.
2. **Mapless.** No map, province, tile, front, coordinate, distance, adjacency, border, movement, territorial capture, occupation or geographic supply. A city is a B-05 asset identifier used only as an `OP-05` target, never a location.
3. **`OP-08` is `BREAK_BLOCKADE`.** The nine-operation catalogue is exactly `OP-01 RAID`, `OP-02 ASSAULT`, `OP-03 AIR_STRIKE`, `OP-04 BLOCKADE`, `OP-05 MISSILE_STRIKE`, `OP-06 INTERCEPT`, `OP-07 FORTIFY`, `OP-08 BREAK_BLOCKADE`, `OP-09 RESUPPLY`. **Espionage is not authorized** by this document or by B-10: no covert operation, no owner, no budget, no validator hook (`B10-AD-24`, `B10-C30`).
4. **No city or facility destruction.** No workflow deletes, captures, sells, merges or transfers a city; damages, disables or transfers a facility; or kills, evicts or transfers a person. The only B-05 attribute a strike may reduce is city infrastructure, under `WAR-109a`–`WAR-109m`.
5. **Operations Points unchanged.** One persistent national military-only pool; `available = max(0, op_balance − reserved)`; one `REGENERATED` item of +1 at the opening of P3.7 per `(nation_id, turn_id)`, including a recorded 0 at the cap; cap 10; carry below the cap; `HELD` at acceptance, `CONSUMED` at P5, `RELEASED` once on failure, cancellation or P7 void; no P0 or P7 regeneration; no per-war, per-campaign, shared, purchasable or transferable pool.
6. **No provisional promotion.** Every B-10 number remains **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. A workflow may not present one as calibrated, approved or final, and may not change one to simplify a test.
7. **Owner-reserved decisions untouched.** `UD-040`–`UD-049` remain **Open**; `UD-032` remains **Resolved Option A**. No workflow, matrix row or edge case decides one.
8. **Protected decisions preserved.** D-014, D-015, D-027, D-122, DD-136, `REQ-513` and the Global Trade gates G-1–G-6 are unchanged.

**1.8 Relationship to the B-10 handoff.** §29 of B-10 lists eighteen inputs a workflow owner receives and an eighteen-item required coverage list. §14.8 records that disposition item by item. This document adds no architecture decision and records no new `B10-AD-` entry.

---

## 2. Canonical semantics used by every workflow

### 2.1 Actors and authority

| Actor | Identifier | May do | May never do |
|---|---|---|---|
| Nation owner | `owner(nation_id)` | Declare, submit, amend, cancel, surrender, propose, counter, accept, reject, withdraw, repair, recruit, disband | Act for another nation; delegate a military decision |
| System scheduler | `B-02` phase runner | Advance P0–P7, run the boundary, write audit | Choose an operation, a term, an objective or a target |
| Canonical validator | `WAR-009` | Return `PASS` or `FAIL(code, rule)` | Waive a check, infer consent, retarget |
| Authorised administration | Prompt 12 | Read fair-play evidence, record a reversal | Edit a committed result in place; declare or operate for a nation |
| Alliance role | B-09 | Alliance-internal matters within `AX-01`–`AX-30` | Command, delegate, spend a member's OP or resources, read a member's private military state |

**2.1.1** The actor is always resolved from the authenticated session to an active nation (`WAR-001`). A request body that names a different `nation_id` fails `WRF-01` and mutates nothing (`WAR-009d`).

### 2.2 Object model

```
WAR (war_id) ── exactly one ──► CAMPAIGN (campaign_id)
                                   ├── objective: primary, secondary (immutable, public)
                                   ├── progress[side][objective] 0…1000
                                   ├── OPERATION (operation_id) ──► BATTLE (battle_id)
                                   └── SETTLEMENT (settlement_id) ──► terms
```

**2.2.1** A `WAR` is the legal hostile relationship; a `CAMPAIGN` is its single scored episode. One campaign never contains more than one war, and a third nation may only open its own separate war (`WAR-007`, `B10-AD-01`).

**2.2.2** The entity and mutation owners are exactly B-10 §4.1. Operations, battles, campaign state, objective progress and exclusions mutate at P5; force and readiness mutate at P3, P4 and P5; a settlement mutates at P4 (proposal) and P5 (transfer).

### 2.3 Mapless contract applied to every workflow

**2.3.1** Every label, notification, failure message and confirmation uses the B-10 §4.2 required vocabulary. A workflow that would need a place, a route, a distance or a location has no implementation and is a defect, not a missing feature.

**2.3.2** A blockade is a national state with a 25% bundle surcharge and a −25 per-turn readiness-recovery penalty, a 12-turn duration and one counter (`OP-08`). It stops no production, deletes no trade and creates no sea zone.

**2.3.3** A city target is an asset reference. The strike is against the **nation**; the city identifier names the affected asset and can only add a rejection (`WRF-36`), never waive a national check (`WAR-009b`).

### 2.4 The complete 25-step campaign lifecycle

Every step below is a **lifecycle step**, not a new phase. The phase names in brackets are B-02's. A step marked **gate** can fail the whole action; a step marked **write** mutates state.

| # | Step | Phase | Gate or write | Authoritative rule |
|---|---|---|---|---|
| 1 | Owner opens the war panel and chooses a target nation | OPEN | — | `WAR-001` |
| 2 | Server loads current eligibility facts for actor and target | OPEN | — | `WAR-003`, `WAR-009` |
| 3 | Owner selects one primary and one distinct secondary objective | OPEN | — | `WAR-006`, `WAR-033` |
| 4 | Pre-commitment disclosure is rendered: cost, effect, counters, every block reason | OPEN | — | `WAR-085`, `WAR-152` |
| 5 | Owner gives explicit, non-defaulted confirmation naming the counterparty and cost | OPEN | — | `WAR-152` |
| 6 | Submission transaction runs validator run #1 (twelve rows, cumulative, fail at first) | OPEN | gate | `WAR-009`, `WAR-009a`–`WAR-009f` |
| 7 | Idempotency key is checked; a replay returns the original receipt | OPEN | gate | `WAR-097`, `WRF-13` |
| 8 | OP `HELD` and every resource `RESERVATION_HELD` are written atomically with the accepted record | OPEN, before P1 | write | `WAR-005`, `WAR-005a`, `WAR-042` |
| 9 | Declaration audit and public terms are written; campaign enters `DECLARED_PENDING` | OPEN→P1 | write | `WRA-01`, `WAR-017` |
| 10 | P1 freezes the turn baseline | P1 | write | `TR-050`, `WAR-091` |
| 11 | Validator run #2 against the frozen state; failure voids the declaration and releases everything | P2 | gate | `WAR-013`, `WAR-009c` |
| 12 | P3.6 resolves civilian Food and tests the protected civilian requirement before any military claim | P3.6 | write | `WAR-053c`, `WAR-053l`, `ECN-080` |
| 13 | P3.7 opening writes one `REGENERATED` OP item and stores the canonical force snapshot | P3.7 | write | `WAR-040`, `WAR-053m`, `F-WR-001` |
| 14 | P3.7 rank 6(a) pays or cancels the military Food ration | P3.7 | write | `WAR-053d`, `WAR-064` |
| 15 | P3.7 rank 6(b) pays or cancels readiness upkeep and applies recovery or the −100 penalty | P3.7 | write | `WAR-050`, `WAR-051` |
| 16 | P4 resolves recruitment, disbanding and B-05 construction/repair orders already accepted | P4 | write | `WAR-058`–`WAR-060`, `WAR-109h` |
| 17 | Validator run #3 immediately before P5 against execution-time state | Pre-P5 | gate | `WAR-009c`, `WAR-116a` |
| 18 | P5.1 resolves declarations in `(submitted_at, action_id)` order and activates campaigns | P5.1 | write | `WAR-089`, `WAR-018` |
| 19 | P5.2 applies deadline, inactivity expiry and dormancy suspension | P5.2 | write | `WAR-019`, `WAR-021` |
| 20 | P5.3 completes accepted settlements atomically and ends their campaigns | P5.3 | write | `WAR-138`, `WAR-158` |
| 21 | P5.4 validates and releases every remaining accepted operation that fails | P5.4 | gate | `WAR-089`, `WRF-20`–`WRF-23` |
| 22 | P5.5 snapshots readiness and force; resolves `OP-09`, `OP-07`, arms `OP-06` | P5.5 | write | `WAR-089`, `WAR-110` |
| 23 | P5.6–P5.8 resolve offensives in the total order, then `OP-08`, then progress | P5.6–P5.8 | write | `WAR-090`–`WAR-093`, `WAR-036` |
| 24 | P6 evaluates victory, records the outcome and publishes the permitted summary | P6 | write | `WAR-037`, `WAR-147` |
| 25 | P7 verifies reservations, voids unresolved actions, publishes the turn; `ARCHIVED` after 84 turns | P7 | write | `WAR-043`, `WAR-030` |

**2.4.1** Steps 12–25 repeat every turn a campaign is live. Steps 1–11 run once per declaration. Steps 18–25 also carry settlement completion, dormancy and termination for every live campaign, not only the one being declared.

**2.4.2** A step may not be reordered. `WAR-043a` states the same order and forbids substituting acceptance for P4, acceptance for consumption, or P7 for regeneration.

### 2.5 The three validation points

| Point | Runs | Reads | A failure means |
|---|---|---|---|
| Submission | Inside the acceptance transaction | Live state at submission | Nothing is reserved; nothing exists (`WAR-009d`) |
| P2 | After P1 freeze | Frozen state | Reservation released once; campaign `VOID` or operation failed (`WRF-05`–`WRF-12`) |
| Pre-P5 | After P3.7 | Execution-time state | Reservation released once; no partial effect |

**2.5.1** The three runs are independent. A P2 pass is not a P5 guarantee, and a P2 failure is not cured by a later state change (`WAR-009c`, `WAR-116a`). Submission has no political-state exception; only validly accepted defensive commitments are exempt at P2 and pre-P5, and only from row 8 (`WAR-009g`).

### 2.6 Reservation lifecycle

```
submit ──► HELD ──► CONSUMED            (P5 resolution)
              ├──► RELEASED           (validation failure, cancellation, P7 void)
              └──► RELEASED           (P3.6 protected-civilian release for OP-09)
```

**2.6.1** A `HELD` item reduces `available`, never `op_balance`. A `CONSUMED` item reduces both `reserved` and `op_balance` exactly once. A `RELEASED` item leaves `op_balance` unchanged because the balance was never debited (`WAR-042`).

**2.6.2** Every action writes exactly one `HELD` and at most one terminal item keyed by `action_id`. Every failure path releases exactly once (`WAR-066`, `WAR-067`).

**2.6.3** An obligation never consumes a reservation (`TR-070`). The P3.7 ration and readiness upkeep read **unreserved** stock only.

### 2.7 Determinism, ordering and idempotency

**2.7.1** P5 order is fixed by `WAR-089`. Offensive order is `(campaign_priority, attacker_nation_id, operation_priority, submitted_at, action_id)`; operation priority is `BLOCKADE` 1, `MISSILE_STRIKE` 2, `AIR_STRIKE` 3, `ASSAULT` 4, `RAID` 5 (`WAR-090`).

**2.7.2** Every battle reads one frozen baseline and applies earlier losses as `damage_carry` (`WAR-091`, `WAR-092`). Readiness is read from the baseline and is not reduced by earlier battles in the same turn.

**2.7.3** The battle seed is the frozen turn digest seed (`TR-046`); `fortune_bp` is a closed integer in −500…+500 (`WAR-082`). A replay against the same baseline, order and seed produces the same tier and the same losses (`WAR-099`).

**2.7.4** Submission idempotency is scoped to the actor (`WAR-097`). Resolution idempotency is keyed by `(turn_id, operation_id)` and `(turn_id, battle_id)` (`WAR-098`). A duplicate never reserves, consumes or regenerates a second time.

### 2.8 Failure semantics (binding on every workflow)

**2.8.1** A blocked action is **not executed at all**: no OP is consumed, no reservation is spent, no readiness changes, no strength or infrastructure is lost, no progress is added and no state is applied (`WAR-009d`).

**2.8.2** The failure names the failing check and the blocking rule. It states "blocked by an active non-aggression agreement" but never discloses private treaty text, the counterparty's inventory or its exact strength (`WAR-149`).

**2.8.3** `AUD-AL-017` is written **only** for a same-Alliance or Alliance-NAP failure (`WRF-07`, `WRF-08`) and keeps its exact B-09 field set (`WAR-154`).

**2.8.4** A failed operation never retargets (`WAR-096`). A failed declaration never becomes a different campaign. A failed settlement returns the campaign to `ACTIVE` (`WRF-33`).

### 2.9 Forbidden vocabulary in workflows and test copy

| Forbidden | Required |
|---|---|
| Front, front line, battle line | *Campaign*, *active campaign* |
| Province, tile, territory, region | *Nation* |
| Map, coordinate, distance, adjacency, border, hex | *(no equivalent)* |
| Move, deploy, march, station at, garrison in | *Force pool*, *stationed strength* (national) |
| Capture, occupy, annex, conquer | *Objective progress*, *campaign outcome* |
| Sea zone, lane, convoy, depot, route | *Blockade state*, *supply bundle* |
| Bombard, siege | *National strike* |
| Covert, spy, sabotage, infiltrate | *(nothing — espionage is not authorized)* |

---

## 3. Actors, permissions and sovereign limits

### 3.1 Permission matrix

| Action | Owner | Alliance role | Office | Treaty | AI | Administrator |
|---|---|---|---|---|---|---|
| Declare war | Yes | No | No | No | No | No |
| Submit operation | Yes | No | No | No | No | No |
| Amend or cancel before freeze | Yes | No | No | No | No | No |
| Surrender | Yes | No | No | No | No | No |
| Propose / counter / accept / reject / withdraw settlement | Yes | No | No | No | No | No |
| Ceasefire | Yes | No | No | No | No | No |
| Read own force, readiness, OP, inventory | Yes | No | No | No | No | Fair-play evidence only |
| Read another nation's exact military state | No | No | No | No | No | Recorded reversal context only |
| Recruit, disband | Yes | No | No | No | No | No |
| Order city repair | Yes | No | No | No | No | No |
| Record a correction | No | No | No | No | No | Yes, as a reversal |

**3.1.1** An Alliance may not pay, receive, guarantee or broker a reparation and may not fund an operation (`WAR-141`, `B10-AD-24`). The Alliance Receiving Ledger has no B-10 role.

**3.1.2** Membership grants no military visibility: no operations, readiness, force, inventory, battle report or settlement draft (`WAR-148`, `AX-18`).

### 3.2 Execution-time revalidation

**3.2.1** Every hostile path — declaration, nine operations, any counter, any administrative replay and any future operation — calls the one canonical validator (`WAR-009`, `WAR-160`). A path that does not is a release blocker.

**3.2.2** Client-side hiding or filtering is not enforcement (`WAR-009f`).

**3.2.3** The validator never reads a cached roster, a copied treaty list or a client flag (`WAR-009a`).

### 3.3 Confirmation requirements

| Action | Must name | Cannot be |
|---|---|---|
| Declaration | Counterparty, 2 OP, 500 crowns, primary and secondary objective, expected effect, irreversibility | Defaulted, pre-checked or remembered |
| `OP-05` missile strike | Counterparty, city (if any), 4 OP, bundle, expected effect, permissible damage bound | Defaulted |
| Surrender | Counterparty, `TERM_CEASEFIRE`, no transfers, permanent record | Defaulted |
| Settlement acceptance | Counterparty, every term, the transfer amount, the irreversibility | Defaulted |

**3.3.1** A confirmation is a fresh act by the authenticated owner (`WAR-152`). A remembered or auto-accepted preference is a defect.

### 3.4 Sovereign limit on silence and delegation

**3.4.1** Silence never accepts a declaration, a ceasefire, a settlement, a counter or an extension (`WAR-127`, `WAR-121`). A window expiry is a rejection.

**3.4.2** No workflow converts an accepted defensive commitment into an offensive one, and none creates a new action after a political state begins (`WAR-009g`, `WAR-053j`).

**3.4.3** No workflow lets an Alliance, an office, a ballot or a majority exercise any row of §3.1 (`WAR-151`, D-137).

---

## 4. Lifecycle and state models

### 4.1 Campaign state machine

| State | Entry | Permitted | Prohibited | Exit |
|---|---|---|---|---|
| `DECLARED_PENDING` | Declaration accepted while OPEN | Cancellation by declarer before freeze; nothing military | Everything else | P5.1 → `ACTIVE`; failure → `VOID` |
| `ACTIVE` | Declaration resolved at P5.1 | Operations, objectives, settlement proposals, surrender | A second outgoing declaration | Victory, surrender, settlement → `ENDED` or `SETTLING` |
| `SETTLING` | A settlement accepted and awaiting its P5 transfer | Settlement completion only | New operations | P5.3 → `ENDED`, or atomic failure → `ACTIVE` |
| `SUSPENDED` | A participant became dormant at P0 | Nothing; the deadline still runs | Operations, declarations, settlement acceptance | Dormancy end → `ACTIVE`; 48 suspended turns → `ENDED` `ABANDONED` |
| `ENDED` | Terminal outcome recorded | Read-only history | Everything military | `ARCHIVED` after 84 turns |
| `ARCHIVED` | Permanent record | Read-only | Everything | None |
| `VOID` | Declaration failed before activation | Nothing | Everything | Permanent record |

**4.1.1** There is no `PAUSED` state (`WAR-015`). War does not pause for a political transition, a lost election, a holiday, a server delay or an Alliance decision.

### 4.2 Operation state model

| State | Meaning | Terminal |
|---|---|---|
| `SUBMITTED` | Accepted into the OPEN window | No |
| `RESERVED` | OP `HELD` and resources `RESERVATION_HELD` written | No |
| `VALIDATED_P2` | Passed validator run #2 | No |
| `SCHEDULED_P5` | Passed pre-P5 and is in the P5 order key | No |
| `RESOLVED` | Battle/effect applied, OP `CONSUMED` | Yes |
| `CANCELLED` | Owner cancelled before freeze, reservation released | Yes |
| `FAILED` | A validator run or P5 step failed, reservation released, code written | Yes |
| `VOID_P7` | Never resolved by P7, released under `WRF-22` | Yes |

### 4.3 Settlement state model

| State | Entry | Exit |
|---|---|---|
| `PROPOSED` | One owner submits terms | Accept, counter, reject, withdraw, expire |
| `COUNTERED` | Other owner submits different terms | Accept, counter, reject, withdraw, expire |
| `ACCEPTED` | Both owners accept the exact version; value reserved | P5.3 `COMPLETED` or `FAILED` |
| `REJECTED` / `WITHDRAWN` / `EXPIRED` | Terminal without effect | — |
| `COMPLETED` | Transfer applied atomically | — |
| `FAILED` | Reservation or balance lost at P5 | Campaign returns to `ACTIVE` |

**4.3.1** There is at most one live settlement per campaign and terms are immutable after submission (`WAR-126`). A proposal or counter expires after 12 turns (`WAR-127`).

### 4.4 OP ledger model

| Event | Key | Effect on `available` | Effect on `op_balance` |
|---|---|---|---|
| `REGENERATED` | `(nation_id, turn_id)` | +1, capped by `op_cap − reserved` | +1, capped at `op_cap` |
| `HELD` | `action_id` | −amount | None |
| `RELEASED` | `action_id` | +amount | None |
| `CONSUMED` | `action_id` | None | −amount; `reserved` −amount |

**4.4.1** `op_balance = available + reserved`; `0 ≤ available ≤ op_balance ≤ op_cap`; `0 ≤ reserved ≤ op_balance` (`WAR-041`). A breach is `WRF-34`, not a rule.

**4.4.2** The player sees four numbers: cap, available, reserved and consumed this turn. `consumed` is a display counter, not a second deduction.

### 4.5 Readiness model

**4.5.1** Readiness is one integer 0…1,000, combat and gate only (`WAR-047`). Gates are light 300 (`RAID`, `FORTIFY`, `INTERCEPT`, `RESUPPLY`) and heavy 500 (`ASSAULT`, `AIR_STRIKE`, `BLOCKADE`, `BREAK_BLOCKADE`, `MISSILE_STRIKE`).

**4.5.2** Recovery is +50 at a paid P3.7, +100 from a resolved `OP-09`, and nothing else (`WAR-110`). Losses are −25 per resolved battle, −50 per successful interdiction once, −25 recovery while blockaded, −100 for an unpaid readiness obligation and −100 for an unpaid ration (`WAR-047`, `WAR-053e`).

**4.5.3** Readiness is not a function of login, attendance, time zone or real time (`WAR-049`).

### 4.6 Blockade and fortification states

| State | Applied by | Duration | Effect | Removed by | Re-application |
|---|---|---|---|---|---|
| `BLOCKADED` | Successful `OP-04` | 12 turns | +25% bundle, −25 readiness recovery per turn | Successful `OP-08`; expiry | 12-turn cooldown after a break |
| `FORTIFIED` | Accepted `OP-07` at P5.5 | One P5 | +25% defence power on the first ground attack, then consumed | Consumption; end of P5 | Once per P5 |
| `SHAKEN` | Decisive `OP-02` | One turn | −100 readiness | Expiry | — |
| `SUPPLY_DENIED` | Successful `OP-01`/`OP-03` under `OBJ-INTERDICTION` | One turn | +25% bundle, −50 readiness once | Expiry | Resets on a new denial |
| `RATION_SHORT` | Unpaid P3.7 ration | Until a fully paid P3.7 | Blocks new offensive operations (`WRF-35`) | Paid ration | — |
| `CAPACITY_OVERDRAWN` | City damage | Until repair | Blocks construction/upgrade orders that increase DC | Repair at P4.1 | — |

**4.6.1** Denial and blockade combine once, additively, capped at +50%, before one per-resource ceiling (`WAR-071a`, `F-WR-039`). The readiness penalties are separate and are never part of that cap.

### 4.7 Protection and eligibility decision

| Layer | Blocks | Rechecked |
|---|---|---|
| Newcomer protection (7 days/84 turns, account-scoped, once) | Declaration and every offensive operation | Submission, P2, pre-P5 |
| Dormancy (14 days/168 turns) | All targeting and initiation; suspends campaigns | P0, P2, pre-P5 |
| Restricted pair | Declaration and every hostile operation | Submission, P2, pre-P5 |
| National `DP-T01` NAP | Declaration only | Submission, P2, pre-P5 |
| Same-Alliance ban | Declaration and every hostile operation | Submission, P2, pre-P5 |
| Alliance `AT-E01` NAP for covered pairs | Declaration and every hostile operation | Submission, P2, pre-P5 |
| `TERM_EXCLUSION` | Declaration between the pair only | Submission, P2, pre-P5 |

**4.7.1** `AT-E00` is record-only and is never treated as an active NAP (`WAR-012`). The server evaluates the stored treaty type, never a client label.

### 4.8 P5 internal order

| Step | Action | Workflow |
|---|---|---|
| P5.0 | Load frozen campaigns and operations; verify the idempotency manifest | WFW-040 |
| P5.1 | Resolve pending declarations; activate campaigns | WFW-004 |
| P5.2 | Deadline, inactivity, dormancy suspension | WFW-005, WFW-006 |
| P5.3 | Complete settlements atomically | WFW-038, WFW-039 |
| P5.4 | Validate and release remaining operations | WFW-018 |
| P5.5 | Snapshot readiness and force; `OP-09`, `OP-07`, arm `OP-06` | WFW-016, WFW-014, WFW-013 |
| P5.6 | Resolve offensives in the order key | WFW-020–WFW-024 |
| P5.7 | Resolve `OP-08` as a defensive offensive contest | WFW-015 |
| P5.8 | Apply objective progress and counter-progress | WFW-024 |
| P5.9 | Write audit records and compute the P6 input | WFW-040 |

---

## 5. Workflow catalogue

Every workflow below carries the same **23 fields**. `Tests` names the acceptance rows that prove it; §14.2 proves the converse. A workflow is a specification of server behaviour, not a screen.

### 5.1 Group A — declaration and campaign start

#### WFW-001 — Declare war

| Field | Content |
|---|---|
| ID and name | `WFW-001` — Declare war against one nation |
| Purpose | Create one pending declaration that becomes exactly one campaign |
| Initiating actor | `owner(nation_id)` of the declarer |
| Permissions | Owner only; no Alliance, office, ballot, treaty, AI or administrator (`WAR-001`, `WAR-151`) |
| Preconditions | Declarer active, not dormant, not `TRANSITION`/`CRISIS`, no outgoing campaign, no pending own declaration; target exists, is active, not self, not dormant, not restricted pair, not protected, no `DP-T01`, no shared Alliance, no covered `AT-E01`; outgoing slot free; ≥ 2 available OP; ≥ 500 unreserved crowns |
| Inputs | `target_nation_id`, `primary_objective`, `secondary_objective` (distinct, from the six), `idempotency_key`, `confirmation_token` |
| Validation | Validator run #1, rows 1–10 in order; objective pair distinct and in the closed catalogue; `WRF-01`…`WRF-13` |
| Player-visible information | Target threat band; exact 2 OP and 500 crowns; the objective pair; expected campaign effect; every current block reason |
| Decision points | Choose target, choose primary, choose secondary, confirm |
| Consent | Unilateral — target consent is not required (`WAR-004`); declarer confirmation is explicit and fresh (`WAR-152`) |
| System processing | One transaction writes the accepted record, OP `HELD` 2, crowns `RESERVATION_HELD` 500, `WRA-01` and `WRA-14` |
| State transitions | none → `DECLARED_PENDING` at acceptance; → `ACTIVE` at P5.1; → `VOID` on P2/pre-P5 failure |
| Resource consequences | 2 OP and 500 crowns held, not debited; consumed only when the declaration resolves at P5.1 |
| Notifications | Actor receipt with campaign identifier; target is not notified before the public declaration at P6 |
| Audit and history | `WRA-01` (war, campaign, declarer, target, objectives, turn, cost, action key); `WRA-14` reservation audit |
| Failure | `WRF-01`–`WRF-13`; nothing is reserved and no campaign exists (`WAR-009d`) |
| Cancellation and withdrawal | Before P1 freeze the declarer may withdraw under `WFW-003`; the reservation is released once |
| Recovery | A duplicate key returns the original receipt (`WRF-13`); an interrupted acceptance commits all items or none |
| Acceptance criteria | Exactly one campaign per accepted declaration; no objective change after acceptance; a blocked declaration moves nothing; the four numbers (cap, available, reserved, consumed) reconcile |
| B-10 rules | `WAR-001`–`WAR-008`, `WAR-005a`, `WAR-009`, `WAR-033`, `WAR-152` |
| Requirements | REQ-654, REQ-656, REQ-658, REQ-668, REQ-669, REQ-678 |
| Formulas | F-WR-004, F-WR-006, F-WR-019 |
| Tests | WFA-009, WFA-010, WFA-011, WFA-012, WFA-013, WFA-014 |

#### WFW-002 — Declaration rejected

| Field | Content |
|---|---|
| ID and name | `WFW-002` — Declaration rejected by the canonical validator |
| Purpose | Return one exact reason and guarantee no mutation |
| Initiating actor | `owner(nation_id)` of the declarer |
| Permissions | Same as `WFW-001`; rejection grants no authority |
| Preconditions | A submission that fails at least one of rows 1–10 |
| Inputs | The rejected submission and its action key |
| Validation | Stops at the first failing check; records the failing check, code and rule (`WAR-009`, `WAR-009d`) |
| Player-visible information | The blocking rule and the counterparty; no private treaty text, inventory or exact strength (`WAR-149`) |
| Decision points | None — the action is refused |
| Consent | None; a rejection is not consent and creates no obligation |
| System processing | Writes `WRA-02`; writes `AUD-AL-017` only for `WRF-07`/`WRF-08` |
| State transitions | None |
| Resource consequences | None; no OP or resource is reserved |
| Notifications | Actor only; the target is not told an attempt occurred |
| Audit and history | `WRA-02` (actor, target, failing check, code, turn, action key) |
| Failure | The rejection itself; the code is stable and the reason is not disclosed to the target |
| Cancellation and withdrawal | Not applicable |
| Recovery | The actor may resubmit after the cause is resolved; a resubmission is a new action |
| Acceptance criteria | Inventory, OP, readiness, progress and campaign state are byte-identical before and after; the code matches the failing row |
| B-10 rules | `WAR-009`–`WAR-014`, `WAR-009d`–`WAR-009f`, `WAR-154` |
| Requirements | REQ-658, REQ-668, REQ-669, REQ-678, REQ-692 |
| Formulas | F-WR-004 |
| Tests | WFA-009, WFA-010, WFA-011, WFA-012 |

#### WFW-003 — Withdraw a pending declaration

| Field | Content |
|---|---|
| ID and name | `WFW-003` — Withdraw a declaration before the freeze |
| Purpose | Let the declarer cancel a `DECLARED_PENDING` campaign before P1 |
| Initiating actor | `owner(nation_id)` of the declarer |
| Permissions | Owner only; the target cannot cancel another nation's declaration |
| Preconditions | Campaign is `DECLARED_PENDING` and the turn has not frozen (P1 not committed) |
| Inputs | `campaign_id`, `idempotency_key`, reason (optional, private) |
| Validation | Campaign exists, is owned by the actor, is `DECLARED_PENDING`, and the freeze has not occurred |
| Player-visible information | The campaign, its objectives, the held 2 OP and 500 crowns |
| Decision points | Confirm withdrawal |
| Consent | Owner only; no counterparty consent exists in this state |
| System processing | Releases OP and crowns once; writes `WRA-05`, `WRA-14`; sets `VOID` |
| State transitions | `DECLARED_PENDING` → `VOID` |
| Resource consequences | Held amounts released; nothing charged |
| Notifications | Actor receipt; no target notification |
| Audit and history | `WRA-05` with reason `WITHDRAWN`, `WRA-14` |
| Failure | After freeze, withdrawal is impossible; the action must be allowed to resolve or fail |
| Cancellation and withdrawal | This workflow is the cancellation |
| Recovery | A duplicate withdrawal returns the original receipt and releases nothing twice |
| Acceptance criteria | `reserved` returns to its pre-declaration value; `op_balance` unchanged; no second release |
| B-10 rules | `WAR-005`, `WAR-042`, `WAR-043a` |
| Requirements | REQ-656, REQ-657, REQ-681 |
| Formulas | F-WR-002 |
| Tests | WFA-010, WFA-017, WFA-081 |

#### WFW-004 — Campaign activation at P5.1

| Field | Content |
|---|---|
| ID and name | `WFW-004` — Resolve a pending declaration into an active campaign |
| Purpose | Activate the campaign, consume the declaration cost and publish the terms |
| Initiating actor | B-02 P5.1 scheduler (no player action) |
| Permissions | System only; the actor cannot force activation |
| Preconditions | Campaign is `DECLARED_PENDING` and passed P2 and pre-P5 |
| Inputs | Frozen declaration set ordered by `(submitted_at, action_id)` |
| Validation | Validator is not re-run here; P5.4 handles remaining operations and pre-P5 handled the declaration |
| Player-visible information | Both owners learn the campaign is active, its objectives, deadline and identifier |
| Decision points | None |
| Consent | Already recorded at acceptance; activation adds no consent |
| System processing | Consumes 2 OP and 500 crowns once; writes `WRA-05`, `WRA-14`; sets `ACTIVE`; deadline `resolved_turn + 84` |
| State transitions | `DECLARED_PENDING` → `ACTIVE` |
| Resource consequences | Reservation consumed; no new charge |
| Notifications | Both owners; declaration public at P6 (`WAR-147`) |
| Audit and history | `WRA-05`, `WRA-01` completion, `WRA-14` |
| Failure | A declaration that fails before P5.1 never reaches this workflow and becomes `VOID` |
| Cancellation and withdrawal | None after activation except surrender or settlement |
| Recovery | Replay of P5.1 skips an already activated campaign by its action key |
| Acceptance criteria | Exactly one activation per declaration; deadline exact; cost consumed exactly once |
| B-10 rules | `WAR-005`, `WAR-018`, `WAR-019`, `WAR-089` |
| Requirements | REQ-654, REQ-657, REQ-680, REQ-681 |
| Formulas | F-WR-002, F-WR-007, F-WR-019 |
| Tests | WFA-013, WFA-017, WFA-018, WFA-081 |

#### WFW-005 — Campaign suspended by dormancy

| Field | Content |
|---|---|
| ID and name | `WFW-005` — Suspend a campaign when a participant becomes dormant |
| Purpose | Freeze military activity without pausing the deadline |
| Initiating actor | B-02 P0/P5.2 dormancy detection |
| Permissions | System only (`D-028`, `WAR-021`) |
| Preconditions | A participant is dormant at P0 or at P5.2 |
| Inputs | Dormancy state, campaign set |
| Validation | Dormancy is read from the current state, never cached |
| Player-visible information | The non-dormant owner sees `SUSPENDED` and the remaining deadline; the dormant owner sees it on return |
| Decision points | None; dormancy is an external state |
| Consent | None |
| System processing | Sets `SUSPENDED`; fails unresolved operations with `WRF-21` and releases them; writes `WRA-05`, `WRA-14` |
| State transitions | `ACTIVE` → `SUSPENDED` |
| Resource consequences | All outstanding reservations released once |
| Notifications | Both owners where reachable |
| Audit and history | `WRA-05` with reason `DORMANCY` |
| Failure | A protected or dormant nation's own defensive operation also fails and releases (`WAR-117`) |
| Cancellation and withdrawal | Operations may not be submitted while suspended |
| Recovery | Return before 48 suspended turns restores `ACTIVE` with force, readiness and progress unchanged |
| Acceptance criteria | No progress decay; deadline continues; no operation resolves while suspended |
| B-10 rules | `WAR-021`–`WAR-024`, `WAR-117` |
| Requirements | REQ-659, REQ-687 |
| Formulas | F-WR-008 |
| Tests | WFA-073, WFA-074, WFA-075 |

#### WFW-006 — Expiry, abandonment and stalemate termination

| Field | Content |
|---|---|
| ID and name | `WFW-006` — Terminate a campaign by expiry, abandonment or stalemate |
| Purpose | End a campaign that cannot or should not continue |
| Initiating actor | B-02 P5.2/P6 scheduler |
| Permissions | System only (`WAR-019`, `WAR-023`) |
| Preconditions | Deadline reached; or 24/48 stale turns; or 48 suspended turns |
| Inputs | Deadline, resolved-operation history, dormancy history, current turn |
| Validation | Deadline is `declaration_resolved_turn + 84` plus at most one 42-turn extension; the stale counter resets on a resolved offensive |
| Player-visible information | `STALEMATE` is public at 24 turns; the deadline and outcome are public |
| Decision points | An owner may propose a ceasefire or settlement before expiry; no automatic choice exists |
| Consent | Expiry needs no consent and creates no obligation; abandonment needs none |
| System processing | Fails pending operations (`WRF-20`), releases them, computes the outcome at P6, writes `WRA-05`, `WRA-13` |
| State transitions | `ACTIVE`/`SUSPENDED` → `ENDED` |
| Resource consequences | All reservations released; no reparations, no exclusion, no protection |
| Notifications | Both owners; public outcome at P6 |
| Audit and history | `WRA-05`, `WRA-13` (campaign, outcome, victor, progress, turn, reason) |
| Failure | Expiry is never a defeat and never a failure of the action; it is an outcome |
| Cancellation and withdrawal | A settlement or surrender before the deadline takes precedence at P5.3 |
| Recovery | `ENDED` is terminal; only `ARCHIVED` follows after 84 turns |
| Acceptance criteria | Outcome is one of `EXPIRY`, `ABANDONED`; no transfer; no protection; record permanent |
| B-10 rules | `WAR-016`, `WAR-018`–`WAR-024`, `WAR-037`, `WAR-038` |
| Requirements | REQ-659, REQ-680 |
| Formulas | F-WR-007, F-WR-008, F-WR-010 |
| Tests | WFA-019, WFA-020, WFA-077, WFA-078 |

### 5.2 Group B — operations

All nine operations share the submission mechanics of `WFW-001` steps 6–9 (validator run #1, idempotency, atomic `HELD`/`RESERVATION_HELD`, `WRA-03`/`WRA-14`). The tables below state only what differs and the fields the shared mechanics do not supply. Every operation also requires an `ACTIVE` campaign against the target (`WAR-046`), a free action limit (`WAR-045`) and a passing readiness gate (`WAR-048`).

#### WFW-007 — `OP-01 RAID`

| Field | Content |
|---|---|
| ID and name | `WFW-007` — Submit `OP-01 RAID` |
| Purpose | Cheap repeatable ground action that erodes strength and enables interdiction |
| Initiating actor | `owner(nation_id)` of the attacker |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 300; INF ≥ 1 strength; offensive slot < 3; `RATION_SHORT` inactive |
| Inputs | `campaign_id`, `target_nation_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11 of the validator; no row 12 because there is no city target |
| Player-visible information | Own exact attack power; target threat band; tier range; 2 OP and the 5 gasoline / 5 ammunition bundle; `FORTIFY` as the declared counter |
| Decision points | Submit or not; no target change after acceptance |
| Consent | Owner only; no target consent |
| System processing | Resolves one battle at P5.6; on success deals losses, adds progress and may apply supply denial when `OBJ-INTERDICTION` is the actor's primary or secondary |
| State transitions | `SUBMITTED` → `RESERVED` → `VALIDATED_P2` → `SCHEDULED_P5` → `RESOLVED`/`FAILED` |
| Resource consequences | 2 OP and the bundle held at acceptance, consumed at P5; readiness −25 after battle |
| Notifications | Battle report to both at P6; public summary after |
| Audit and history | `WRA-04`, `WRA-06`, `WRA-14`, and `WRA-07` when denial is applied |
| Failure | `WRF-23` readiness, `WRF-25` supply, `WRF-26` no campaign/stale target, `WRF-21` dormancy, `WRF-35` unfed |
| Cancellation and withdrawal | Before freeze via `WFW-017`, releasing everything once |
| Recovery | Same action key returns the receipt; an interrupted P5 replays the same baseline and seed |
| Acceptance criteria | Bundle exact; progress applied once and only on success; denial applied once; cap respected |
| B-10 rules | `WAR-045`, `WAR-046`, `WAR-069`, `WAR-071`, `WAR-073`, §13.2 |
| Requirements | REQ-684, REQ-686, REQ-688 |
| Formulas | F-WR-016, F-WR-017, F-WR-019, F-WR-027 |
| Tests | WFA-025, WFA-026, WFA-033, WFA-034, WFA-041 |

#### WFW-008 — `OP-02 ASSAULT`

| Field | Content |
|---|---|
| ID and name | `WFW-008` — Submit `OP-02 ASSAULT` |
| Purpose | The heaviest conventional ground action and main attrition tool |
| Initiating actor | `owner(nation_id)` of the attacker |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 500; INF ≥ 100 strength; offensive slot < 3; `RATION_SHORT` inactive |
| Inputs | `campaign_id`, `target_nation_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11; unit gate INF ≥ 100; no city row |
| Player-visible information | Attack power, threat band, tier range, 3 OP and the 10/10/2/0 bundle, `FORTIFY` counter |
| Decision points | Submit or not |
| Consent | Owner only |
| System processing | One battle with full infantry and armour; a decisive result adds `SHAKEN` (−100 readiness) to the defender |
| State transitions | As `WFW-007` |
| Resource consequences | 3 OP and bundle consumed at P5; readiness −25 both sides |
| Notifications | Battle report; `SHAKEN` visible as a readiness band change |
| Audit and history | `WRA-04`, `WRA-06`, `WRA-07`, `WRA-14` |
| Failure | `WRF-23`, `WRF-24` unit gate, `WRF-25`, `WRF-26`, `WRF-35` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | Idempotent replay; `SHAKEN` applied once |
| Acceptance criteria | 100-strength gate enforced; `SHAKEN` only on a decisive tier; losses within the per-battle cap |
| B-10 rules | `WAR-045`, `WAR-073`, `WAR-084`, §13.2 |
| Requirements | REQ-683, REQ-684, REQ-688 |
| Formulas | F-WR-016, F-WR-019, F-WR-025, F-WR-027 |
| Tests | WFA-121, WFA-120 |

#### WFW-009 — `OP-03 AIR_STRIKE`

| Field | Content |
|---|---|
| ID and name | `WFW-009` — Submit `OP-03 AIR_STRIKE` |
| Purpose | Contest air control, support attrition and impose interdiction |
| Initiating actor | `owner(nation_id)` of the attacker |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 500; AIR ≥ 20; `MIL-T3`; offensive slot < 3; not `RATION_SHORT` |
| Inputs | `campaign_id`, `target_nation_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11; tier check `MIL-T3`; no city target exists for this operation |
| Player-visible information | Attack power, threat band, tier range, 3 OP and the 10/6/0/1 bundle, `INTERCEPT` counter (+40% defence, −15% attack) |
| Decision points | Submit or not |
| Consent | Owner only |
| System processing | One battle against air defence; success adds AIR/ATTRITION/STRIKE progress and may apply denial |
| State transitions | As `WFW-007` |
| Resource consequences | 3 OP and bundle; readiness −25 |
| Notifications | Battle report; public summary |
| Audit and history | `WRA-04`, `WRA-06`, `WRA-07`, `WRA-14` |
| Failure | `WRF-23`, `WRF-24` tier, `WRF-25`, `WRF-26`, `WRF-35` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | Idempotent replay |
| Acceptance criteria | No city, facility or geographic target accepted; air losses hit the AIR pool; counter applied once |
| B-10 rules | `WAR-055`, `WAR-073`, §13.2 |
| Requirements | REQ-684, REQ-688, REQ-693 |
| Formulas | F-WR-016, F-WR-026, F-WR-027 |
| Tests | WFA-122, WFA-120 |

#### WFW-010 — `OP-04 BLOCKADE`

| Field | Content |
|---|---|
| ID and name | `WFW-010` — Submit `OP-04 BLOCKADE` |
| Purpose | Apply the symbolic national blockade state that raises cost and slows recovery |
| Initiating actor | `owner(nation_id)` of the attacker |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 500; NAV ≥ 30; `MIL-T3`; no active blockade by either side; no 12-turn cooldown |
| Inputs | `campaign_id`, `target_nation_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11; blockade state and cooldown check (`WRF-27`) |
| Player-visible information | Naval contest disclosure, 3 OP, the 8/4/2/0 bundle, `BREAK_BLOCKADE` counter |
| Decision points | Submit or not |
| Consent | Owner only |
| System processing | One naval contest; success applies `BLOCKADED` for 12 turns (+25% bundle, −25 recovery); failure applies nothing |
| State transitions | `BLOCKADED` on the target; `WRA-07` |
| Resource consequences | 3 OP and bundle; readiness −25 |
| Notifications | Public state; exact naval strength private |
| Audit and history | `WRA-04`, `WRA-07`, `WRA-14` |
| Failure | `WRF-27` active blockade or cooldown; `WRF-23`, `WRF-25`, `WRF-35` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | A replay cannot apply a second blockade state |
| Acceptance criteria | One blockade per pair; no production or trade loss; 12-turn duration exact |
| B-10 rules | `WAR-071a`, `WAR-072`, `WAR-073`, `WAR-119` |
| Requirements | REQ-686, REQ-688 |
| Formulas | F-WR-018, F-WR-039 |
| Tests | WFA-025, WFA-029, WFA-065, WFA-113 |

#### WFW-011 — `OP-05 MISSILE_STRIKE` (nation target)

| Field | Content |
|---|---|
| ID and name | `WFW-011` — Submit `OP-05 MISSILE_STRIKE` with `target_type = NATION` |
| Purpose | Expensive strategic strike with national effect and no city implication |
| Initiating actor | `owner(nation_id)` of the attacker |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 500; `MIL-T4`; fewer than 2 missile strikes by that side in the campaign; not `RATION_SHORT` |
| Inputs | `campaign_id`, `target_nation_id`, `target_type = NATION`, `idempotency_key`, confirmation |
| Validation | Rows 1–11; tier and campaign-limit check (`WRF-28`) |
| Player-visible information | Strike power 2,000 + 25% of air attack; threat band; 4 OP and the 6/12/0/2 bundle; `INTERCEPT` is the only counter; −100 readiness on success |
| Decision points | Submit or not |
| Consent | Owner only |
| System processing | One battle with the fixed national strike power; success adds STRIKE/ATTRITION progress and −100 readiness; no infrastructure change |
| State transitions | As `WFW-007` |
| Resource consequences | 4 OP and bundle; attacker may lose AIR at 10% of the defender's loss |
| Notifications | Strike public at P6; exact strength private |
| Audit and history | `WRA-04`, `WRA-08`, `WRA-14` |
| Failure | `WRF-28`, `WRF-35`, `WRF-23`, `WRF-25` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | Campaign counter increments once per resolved strike |
| Acceptance criteria | At most two per campaign per side; no city row runs; readiness effect applied once |
| B-10 rules | `WAR-080`, `WAR-109a`, `WAR-109b`, §13.2 |
| Requirements | REQ-684, REQ-688, REQ-699 |
| Formulas | F-WR-021, F-WR-026, F-WR-027 |
| Tests | WFA-025, WFA-030, WFA-041, WFA-113 |

#### WFW-012 — `OP-05 MISSILE_STRIKE` (city target)

| Field | Content |
|---|---|
| ID and name | `WFW-012` — Submit `OP-05 MISSILE_STRIKE` with `target_type = CITY(city_id)` |
| Purpose | Permit the single adopted infrastructure-damage effect, bounded and recoverable |
| Initiating actor | `owner(nation_id)` of the attacker |
| Permissions | Owner only |
| Preconditions | All `WFW-011` preconditions; the city exists, belongs to the target nation and is a B-05 `city_id` |
| Inputs | `campaign_id`, `target_nation_id`, `target_type = CITY`, `city_id`, `idempotency_key`, confirmation that names the city |
| Validation | **Every national row 1–11 first**, then row 12 city validity; the city check can only reject (`WRF-36`) |
| Player-visible information | The same strike disclosure plus the city, its public infrastructure and the possible damage bound; never the defender's exact book value |
| Decision points | Submit or not; the city cannot be changed after acceptance |
| Consent | Owner only |
| System processing | One battle against the target nation; on `ATTACKER_VICTORY`/`DECISIVE_VICTORY` applies `removed = min(ceil(I × 500/10,000), 20, campaign_headroom, I − 10)`, then capacity, housing and impairment |
| State transitions | As `WFW-007`; `INFRASTRUCTURE_DAMAGED`; possibly `CAPACITY_OVERDRAWN` |
| Resource consequences | 4 OP and bundle; no city deletion, no facility loss, no population casualty |
| Notifications | City, `I_before`, `removed`, `I_after` and campaign cumulative public at P6 |
| Audit and history | `WRA-04`, `WRA-08`, `INFRASTRUCTURE_DAMAGED`, `WRA-14` |
| Failure | `WRF-36` invalid city; `WRF-28`, `WRF-35`, `WRF-23`, `WRF-25` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | `damage_event_id = (turn_id, strike_action_id, city_id)` makes the write idempotent |
| Acceptance criteria | A victory at the floor or the campaign cap deals 0 and still resolves; impairment ≤ carrying value; no facility row changes |
| B-10 rules | `WAR-009b`, `WAR-109a`–`WAR-109m` |
| Requirements | REQ-664, REQ-689, REQ-699, REQ-700, REQ-701, REQ-702 |
| Formulas | F-WR-037, F-WR-038 |
| Tests | WFA-030, WFA-031, WFA-049, WFA-050, WFA-051, WFA-052, WFA-105, WFA-106 |

#### WFW-013 — `OP-06 INTERCEPT`

| Field | Content |
|---|---|
| ID and name | `WFW-013` — Submit `OP-06 INTERCEPT` |
| Purpose | Universal air and missile counter, also a defensive objective tool |
| Initiating actor | `owner(nation_id)` of the defender |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 300; AIR strength ≥ 1; conditional-defensive slot < 3 |
| Inputs | `campaign_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11 with self as actor; no hostile target row |
| Player-visible information | Own air power; 1 OP and the 4/6/0/0 bundle; single trigger; +40% defence and −15% attacker power |
| Decision points | Arm or not; the trigger cannot be aimed after submission |
| Consent | Owner only |
| System processing | Armed at P5.5; triggers once against the first incoming air or missile strike in the same P5; expires at P7 if unused |
| State transitions | `SCHEDULED_P5` → `RESOLVED` or `VOID_P7` |
| Resource consequences | 1 OP and bundle held; released if unused |
| Notifications | Defender sees attack type and outcome, never the attacker's exact composition |
| Audit and history | `WRA-04`, `WRA-09`, `WRA-14` |
| Failure | `WRF-23`, `WRF-25`; an unused order expires with `WRF-22` at P7 |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | One trigger per accepted order; a replay does not trigger twice |
| Acceptance criteria | First qualifying attack only; cannot be countered; limit three per turn |
| B-10 rules | `WAR-073`, `WAR-094`, `WAR-119`, §13.2 |
| Requirements | REQ-684, REQ-688 |
| Formulas | F-WR-026 |
| Tests | WFA-025, WFA-032, WFA-066, WFA-067 |

#### WFW-014 — `OP-07 FORTIFY`

| Field | Content |
|---|---|
| ID and name | `WFW-014` — Submit `OP-07 FORTIFY` |
| Purpose | Ground counter and bounded defensive posture |
| Initiating actor | `owner(nation_id)` of the defender |
| Permissions | Owner only |
| Preconditions | `ACTIVE` campaign; readiness ≥ 300; INF ≥ 1; no active `FORTIFIED`; defensive slot < 3 |
| Inputs | `campaign_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11 with self as actor; duplicate check (`WRF-31`) |
| Player-visible information | 2 OP and the 0/2/4/0 bundle; +25% defence on the first ground attack; one P5 only |
| Decision points | Arm or not |
| Consent | Owner only |
| System processing | Applies `FORTIFIED` at P5.5; the first ground attack gains `counter_defence_bp = 12500`; then consumed |
| State transitions | `FORTIFIED` applied and removed in the same P5 |
| Resource consequences | 2 OP and bundle consumed at P5 |
| Notifications | Opponent sees `DEFENSIVE POSTURE`, never exact strength |
| Audit and history | `WRA-07`, `WRA-10`, `WRA-14` |
| Failure | `WRF-23`, `WRF-25`, `WRF-31` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | A second submission in the same P5 is `WRF-31`; the state never carries across a boundary |
| Acceptance criteria | Does not stack; one P5; no indefinite lock |
| B-10 rules | `WAR-073`, `WAR-119`, §13.2 |
| Requirements | REQ-684, REQ-688 |
| Formulas | F-WR-026 |
| Tests | WFA-025, WFA-032, WFA-066, WFA-068 |

#### WFW-015 — `OP-08 BREAK_BLOCKADE`

| Field | Content |
|---|---|
| ID and name | `WFW-015` — Submit `OP-08 BREAK_BLOCKADE` |
| Purpose | Naval counter that restores normal cost and recovery |
| Initiating actor | `owner(nation_id)` of the blockaded nation |
| Permissions | Owner only |
| Preconditions | An active enemy blockade on the actor; readiness ≥ 500; NAV ≥ 30; defensive slot < 3 |
| Inputs | `campaign_id`, `blockading_nation_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11 in the hostile-defensive column; `WRF-29` when no active blockade exists |
| Player-visible information | Naval contest disclosure; 2 OP and the 6/4/2/0 bundle; `counter_attack_bp = 7000` |
| Decision points | Submit or not |
| Consent | Owner only |
| System processing | Resolves at P5.7 as a defensive offensive contest; success removes `BLOCKADED`, adds `OBJ-DEFENCE` progress and counter-progress, and starts the 12-turn re-imposition cooldown |
| State transitions | `BLOCKADED` removed; `WRA-07` |
| Resource consequences | 2 OP and bundle; naval losses by tier |
| Notifications | Public state change |
| Audit and history | `WRA-04`, `WRA-07`, `WRA-14` |
| Failure | `WRF-29`, `WRF-23`, `WRF-25`, `WRF-35` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | A replay cannot remove a state twice |
| Acceptance criteria | Only the blockaded nation may break; success is the only removal besides expiry |
| B-10 rules | `WAR-073`, `WAR-118`, `WAR-119` |
| Requirements | REQ-684, REQ-686, REQ-688 |
| Formulas | F-WR-026 |
| Tests | WFA-025, WFA-029, WFA-065, WFA-069 |

#### WFW-016 — `OP-09 RESUPPLY`

| Field | Content |
|---|---|
| ID and name | `WFW-016` — Submit `OP-09 RESUPPLY` |
| Purpose | Convert resources into readiness; the only recovery operation |
| Initiating actor | `owner(nation_id)` |
| Permissions | Owner only |
| Preconditions | Readiness < 1,000; not already resupplied this turn; eligible Food surplus ≥ 4 above the protected civilian requirement |
| Inputs | `campaign_id`, `idempotency_key`, confirmation |
| Validation | Rows 1–11 with self as actor; `WRF-30` at cap; `WRF-25` when the eligible surplus is short |
| Player-visible information | +100 readiness, 1 OP, the 4/2/0/0 bundle and 4 Food; the eligible-surplus test; `RATION_SHORT` is never a block for this operation |
| Decision points | Submit or not |
| Consent | Owner only |
| System processing | Reserves 4 Food at acceptance; P3.6 may release it in reverse acceptance order; resolves at P5.5 restoring 100 readiness |
| State transitions | `RESOLVED`; readiness +100 capped |
| Resource consequences | 1 OP, bundle and 4 Food consumed; never pays the garrison ration |
| Notifications | Private to the owner |
| Audit and history | `WRA-11`, `WRA-14` |
| Failure | `WRF-25`, `WRF-30`; `WRF-35` never applies to `OP-09` |
| Cancellation and withdrawal | `WFW-017` before freeze |
| Recovery | One `RESERVATION_CONSUMED` per action key; a P3.6 release prevents any P5 consumption |
| Acceptance criteria | Readiness never exceeds 1,000; four Food debited once; no double counting with the garrison ration |
| B-10 rules | `WAR-053f`, `WAR-053g`, `WAR-053l`, `WAR-110` |
| Requirements | REQ-662, REQ-694, REQ-695, REQ-696, REQ-697, REQ-698 |
| Formulas | F-WR-016, F-WR-036 |
| Tests | WFA-033, WFA-036, WFA-037, WFA-038, WFA-039, WFA-040, WFA-105 |

#### WFW-017 — Amend or cancel an accepted operation

| Field | Content |
|---|---|
| ID and name | `WFW-017` — Amend or cancel an accepted operation before the freeze |
| Purpose | Let the owner correct a mistake before P1 without a second reservation |
| Initiating actor | `owner(nation_id)` |
| Permissions | Owner only |
| Preconditions | Operation is `RESERVED` and the turn has not frozen |
| Inputs | `operation_id`, the amended parameters or a cancellation flag, `idempotency_key` |
| Validation | Re-runs the canonical validator on the amended form; an amendment is a new action with a new key |
| Player-visible information | The amended cost, effect and block reasons |
| Decision points | Amend, cancel or keep |
| Consent | Owner only |
| System processing | Cancellation releases once and writes `WRA-14`; an amendment releases the old reservation and reserves the new one in one transaction |
| State transitions | `RESERVED` → `CANCELLED` or a new `RESERVED` |
| Resource consequences | Released amounts restored; amended amounts held |
| Notifications | Actor only |
| Audit and history | `WRA-03`, `WRA-14` |
| Failure | After the freeze nothing can change; the operation resolves or fails |
| Cancellation and withdrawal | This workflow is the cancellation |
| Recovery | A replay of the cancellation returns the receipt and does not double-release |
| Acceptance criteria | Exactly one terminal item per action key; no amendment after freeze |
| B-10 rules | `WAR-005a`, `WAR-042`, `WAR-096` |
| Requirements | REQ-656, REQ-657 |
| Formulas | F-WR-002 |
| Tests | WFA-123, WFA-120 |

#### WFW-018 — Operation rejection and reservation release

| Field | Content |
|---|---|
| ID and name | `WFW-018` — Reject an operation and release its reservations exactly once |
| Purpose | One deterministic failure path for every operation and every validation point |
| Initiating actor | Canonical validator at submission, P2 or pre-P5 |
| Permissions | System only |
| Preconditions | Any failing check |
| Inputs | The action and its reservation items |
| Validation | Stops at the first failing check; the code is stable |
| Player-visible information | The failing rule and the counterparty; never private treaty text |
| Decision points | None |
| Consent | None |
| System processing | Releases every held item once, writes `WRA-02`/`WRA-03`, and writes `WRA-14`; `AUD-AL-017` only for `WRF-07`/`WRF-08` |
| State transitions | `RESERVED` → `FAILED` |
| Resource consequences | All OP and resources restored to availability; `op_balance` unchanged |
| Notifications | Actor |
| Audit and history | `WRA-02`, `WRA-03`, `WRA-14` |
| Failure | This workflow is the failure path |
| Cancellation and withdrawal | Not applicable |
| Recovery | A retry of the same key cannot re-release; it returns the terminal receipt |
| Acceptance criteria | No partial release; no mutation beyond the release; the code matches the failing row |
| B-10 rules | `WAR-009d`, `WAR-013`, `WAR-066`, `WAR-067` |
| Requirements | REQ-656, REQ-657, REQ-658, REQ-666, REQ-692 |
| Formulas | F-WR-002, F-WR-004 |
| Tests | WFA-009, WFA-010, WFA-011, WFA-012, WFA-014, WFA-081 |

#### WFW-019 — Duplicate submission and idempotent replay

| Field | Content |
|---|---|
| ID and name | `WFW-019` — Duplicate submission and idempotent replay |
| Purpose | Prevent a double-click or retry from reserving or resolving twice |
| Initiating actor | Any submission path |
| Permissions | Same as the original action |
| Preconditions | A key already used by that actor |
| Inputs | The repeated request and its key |
| Validation | Key scope is the actor; a duplicate returns the original receipt (`WRF-13`) |
| Player-visible information | The original receipt, unchanged |
| Decision points | None |
| Consent | Not re-collected; a duplicate is not a new consent |
| System processing | Reads the stored receipt; writes nothing |
| State transitions | None |
| Resource consequences | None |
| Notifications | None |
| Audit and history | `WRA-03` original only; no second event |
| Failure | `WRF-13` is the returned code for a duplicate |
| Cancellation and withdrawal | Not applicable |
| Recovery | This workflow is the recovery |
| Acceptance criteria | One `HELD`, at most one terminal item and one battle per action key |
| B-10 rules | `WAR-097`–`WAR-100` |
| Requirements | REQ-657 |
| Formulas | F-WR-022, F-WR-034 |
| Tests | WFA-013, WFA-081, WFA-082, WFA-083 |

### 5.3 Group C — battle resolution, losses and damage

#### WFW-020 — Resolve one battle

| Field | Content |
|---|---|
| ID and name | `WFW-020` — Resolve one offensive operation into one battle |
| Purpose | Produce one deterministic tier, one loss set and one report |
| Initiating actor | B-02 P5.6/P5.7 resolver |
| Permissions | System only; no player input at resolution |
| Preconditions | Operation passed pre-P5 and is in the P5 order key |
| Inputs | Frozen baseline, strength by type, readiness, counters, seed, battle identifier |
| Validation | Battle reads `available_strength = max(0, baseline − cumulative_losses)` and the baseline readiness (`WAR-092`) |
| Player-visible information | Nothing until `WRA-04` is written; no partial battle state is visible before the event |
| Decision points | None at resolution |
| Consent | Already given at acceptance |
| System processing | `attack_power`, `defence_power`, `base_ratio_bp`, `fortune_bp`, `effective_ratio_bp`, tier, losses, progress — all integer or bp |
| State transitions | `SCHEDULED_P5` → `RESOLVED` |
| Resource consequences | OP and bundle consumed once; losses applied |
| Notifications | Battle report to both parties at P6; summary public |
| Audit and history | `WRA-04` (powers, ratio, fortune, tier, losses, progress) |
| Failure | `WRF-34` on an invariant violation; the checkpoint holds and nothing is published |
| Cancellation and withdrawal | None at this stage |
| Recovery | One `APPLIED` marker per `(turn_id, battle_id)`; a replay skips the battle |
| Acceptance criteria | Same baseline, order and seed reproduce the same tier and losses; both-zero powers give ratio 5,000 |
| B-10 rules | `WAR-074`–`WAR-084`, `WAR-091`–`WAR-093` |
| Requirements | REQ-655, REQ-684, REQ-685 |
| Formulas | F-WR-020–F-WR-026 |
| Tests | WFA-041, WFA-042, WFA-043, WFA-044, WFA-045, WFA-081 |

#### WFW-021 — Apply losses and caps

| Field | Content |
|---|---|
| ID and name | `WFW-021` — Apply strength losses under the per-battle and per-campaign caps |
| Purpose | Bound and attribute every strength loss |
| Initiating actor | Battle resolver |
| Permissions | System only |
| Preconditions | A resolved tier with a loss rate |
| Inputs | Engaged strength by type, loss rate in bp, cumulative campaign loss, campaign-start strength |
| Validation | Per-type proportional loss with largest remainder; tie-break `UNIT-AIR`, `UNIT-ARM`, `UNIT-INF`, `UNIT-NAV`; floor to whole points |
| Player-visible information | Parties see exact losses; public sees a band |
| Decision points | None |
| Consent | None |
| System processing | Applies 20% per-battle and 60% per-campaign caps; a capped side takes zero strength loss and the report states `LOSS_CAP_REACHED` |
| State transitions | Strength pools reduced; no unit state |
| Resource consequences | No ledger item; strength is B-10 state, not inventory |
| Notifications | Battle report |
| Audit and history | `WRA-04` |
| Failure | More loss than exists is impossible; the remainder is not carried as debt |
| Cancellation and withdrawal | Not applicable |
| Recovery | Losses are written inside the battle transaction; a replay applies none |
| Acceptance criteria | No side loses more than 20% in one battle or 60% across the campaign; readiness loss still applies at the cap |
| B-10 rules | `WAR-104`–`WAR-109` |
| Requirements | REQ-683, REQ-689 |
| Formulas | F-WR-027, F-WR-028 |
| Tests | WFA-049, WFA-050, WFA-052, WFA-053 |

#### WFW-022 — Readiness loss and temporary states

| Field | Content |
|---|---|
| ID and name | `WFW-022` — Apply readiness loss and temporary battle states |
| Purpose | Attribute readiness cost and apply the permitted state effects |
| Initiating actor | Battle resolver |
| Permissions | System only |
| Preconditions | A resolved battle; a decisive tier for `SHAKEN`; a successful denial for `SUPPLY_DENIED` |
| Inputs | Tier, battle participation, denial eligibility |
| Validation | −25 readiness per resolved battle per side; −50 once when denial is imposed; floored at 0 |
| Player-visible information | Readiness band; `DEFENSIVE POSTURE` for `FORTIFIED` |
| Decision points | None |
| Consent | None |
| System processing | Applies readiness deltas and state rows; writes `WRA-07` |
| State transitions | `SHAKEN`, `SUPPLY_DENIED`, `FORTIFIED` consumed |
| Resource consequences | None |
| Notifications | Owner sees exact readiness; opponent sees the band |
| Audit and history | `WRA-07`, `WRA-10` |
| Failure | No readiness below 0; no permanent state |
| Cancellation and withdrawal | Not applicable |
| Recovery | Each state row written once per battle or per denial |
| Acceptance criteria | Readiness loss is not capped by the strength cap; no state stacks |
| B-10 rules | `WAR-047`, `WAR-071`, `WAR-106`, `WAR-119` |
| Requirements | REQ-682, REQ-686, REQ-688 |
| Formulas | F-WR-005, F-WR-017 |
| Tests | WFA-033, WFA-041, WFA-066, WFA-069 |

#### WFW-023 — Apply city infrastructure damage and impairment

| Field | Content |
|---|---|
| ID and name | `WFW-023` — Apply city infrastructure damage, capacity, housing and impairment |
| Purpose | Implement the single adopted B-05 damage effect exactly and atomically |
| Initiating actor | Battle resolver for a victorious city-targeted `OP-05` |
| Permissions | System only |
| Preconditions | `ATTACKER_VICTORY` or `DECISIVE_VICTORY`; a valid city target; `I_combat` from the P4.1 snapshot |
| Inputs | `I_combat`, campaign-start level, remaining campaign headroom, infrastructure carrying value |
| Validation | `removed = min(ceil(I × 500/10,000), 20, headroom, I − 10)`; `I_after ≥ 10`; 30% per city per campaign |
| Player-visible information | City, `I_before`, `removed`, `I_after` and cumulative public at P6; book value private |
| Decision points | None |
| Consent | None |
| System processing | Recomputes `capacity`, `housing`; sets or clears `CAPACITY_OVERDRAWN`; impairs carrying value; no facility or population row changes |
| State transitions | Infrastructure reduced; `CAPACITY_OVERDRAWN` possibly set |
| Resource consequences | Book value falls by the impairment; no expense, sale or refund |
| Notifications | `INFRASTRUCTURE_DAMAGED`; city view |
| Audit and history | `INFRASTRUCTURE_DAMAGED` keyed `(turn_id, strike_action_id, city_id)` |
| Failure | `WRF-34` if impairment would exceed carrying value; no partial write |
| Cancellation and withdrawal | Not applicable |
| Recovery | The damage key makes a replay write no second level loss and no second impairment |
| Acceptance criteria | `accumulated ≤ gross`; floor 10; cap 30%; no city, facility or person lost |
| B-10 rules | `WAR-109c`–`WAR-109m` |
| Requirements | REQ-664, REQ-700, REQ-701, REQ-702 |
| Formulas | F-WR-037, F-WR-038 |
| Tests | WFA-030, WFA-031, WFA-049, WFA-051, WFA-052, WFA-053 |

#### WFW-024 — Objective progress and counter-progress

| Field | Content |
|---|---|
| ID and name | `WFW-024` — Apply objective progress and counter-progress |
| Purpose | Score a campaign without a hidden meter |
| Initiating actor | P5.8 resolver |
| Permissions | System only |
| Preconditions | A resolved offensive or defensive result |
| Inputs | Operation type, tier, success, objective pair, per-type resolution count |
| Validation | Progress only on success; `CONTESTED` earns nothing; each type contributes at most 8 times per campaign per side |
| Player-visible information | Both sides see both progress totals; the objective pair is public |
| Decision points | None |
| Consent | None |
| System processing | Adds the published value once; a successful defence subtracts `floor(value × 2500/10,000)` from the attacker's matching total, floored at zero |
| State transitions | Progress 0…1,000 per side per objective |
| Resource consequences | None |
| Notifications | Progress event; public totals |
| Audit and history | `WRA-06` (campaign, side, objective, delta, new total, source operation) |
| Failure | No negative progress; no progress from an alliance, a gift or a purchase |
| Cancellation and withdrawal | Not applicable |
| Recovery | One progress event per resolved operation |
| Acceptance criteria | Cap 1,000; eight-resolution cap; no progress on failure or `CONTESTED` |
| B-10 rules | `WAR-032`–`WAR-036` |
| Requirements | REQ-679, REQ-680 |
| Formulas | F-WR-009, F-WR-011 |
| Tests | WFA-041, WFA-043, WFA-045, WFA-049, WFA-054 |

### 5.4 Group D — economy, force, recovery and restrictions

#### WFW-025 — P3.7 military Food ration

| Field | Content |
|---|---|
| ID and name | `WFW-025` — Pay or cancel the garrison Food ration at P3.7 |
| Purpose | Feed the force after civilians and without debt |
| Initiating actor | B-04 obligation engine at P3.7 rank 6(a) |
| Permissions | System only |
| Preconditions | The canonical P3.7 force snapshot exists; P3.6 civilian Food completed |
| Inputs | `force_snapshot`, soldier-equivalent factors, unreserved Food after P3.6 |
| Validation | `demand = ceil(Σ(strength × e_t) / 1,000)`; whole obligation against unreserved Food |
| Player-visible information | Owner sees demand, paid or short, shortfall and `RATION_SHORT`; opponent sees only a readiness band |
| Decision points | None at the boundary; the player could have recruited or traded earlier |
| Consent | None |
| System processing | Pays in full with `OBLIGATION_PAID` component `MILITARY_RATION`, or cancels in full with `OBLIGATION_CANCELLED`, readiness −100 and `RATION_SHORT` |
| State transitions | `RATION_SHORT` set or cleared |
| Resource consequences | Food debited once; no partial payment, no debt, no unit deletion |
| Notifications | Digest states demand, shortfall and `RATION_SHORT` |
| Audit and history | `OBLIGATION_PAID`/`OBLIGATION_CANCELLED`, `WRA-14` |
| Failure | A short ration is not an action failure; it is a recorded shortage |
| Cancellation and withdrawal | Not applicable |
| Recovery | A fully paid next P3.7 clears the flag with no catch-up |
| Acceptance criteria | Never consumes reserved Food; never changes civilian demand; never double-charges `OP-09` |
| B-10 rules | `WAR-053a`–`WAR-053i`, `WAR-053m`, `WAR-064a` |
| Requirements | REQ-662, REQ-694, REQ-695, REQ-696, REQ-698 |
| Formulas | F-WR-036 |
| Tests | WFA-033, WFA-034, WFA-035, WFA-036, WFA-037 |

#### WFW-026 — P3.7 readiness upkeep

| Field | Content |
|---|---|
| ID and name | `WFW-026` — Pay or cancel readiness upkeep at P3.7 rank 6(b) |
| Purpose | Price readiness recovery without creating debt |
| Initiating actor | B-04 obligation engine at P3.7 |
| Permissions | System only |
| Preconditions | `total_strength` from the canonical snapshot; the ration sub-step completed |
| Inputs | `total_strength`, crown, ammunition and gasoline coefficients |
| Validation | Whole obligation from unreserved crowns, ammunition and gasoline; no reservation is consumed |
| Player-visible information | Owner sees the obligation and the outcome; a warning is shown when projected readiness would fall below a gate |
| Decision points | None at the boundary |
| Consent | None |
| System processing | Paid: readiness +50 capped, `OBLIGATION_PAID`. Unpaid: obligation cancelled, readiness −100 floored, no debt |
| State transitions | Readiness changes |
| Resource consequences | Crowns, ammunition and gasoline debited once |
| Notifications | Digest |
| Audit and history | `OBLIGATION_PAID`/`OBLIGATION_CANCELLED` component `READINESS`, `WRA-14` |
| Failure | Unpaid upkeep never blocks an operation by itself; it lowers readiness, which may fail a gate |
| Cancellation and withdrawal | Not applicable |
| Recovery | Recovery only by a later paid upkeep or `OP-09` |
| Acceptance criteria | Ration and readiness are separate obligations; their deltas sum; no rank change |
| B-10 rules | `WAR-050`–`WAR-053`, `WAR-064`–`WAR-065` |
| Requirements | REQ-662, REQ-682 |
| Formulas | F-WR-003, F-WR-005 |
| Tests | WFA-033, WFA-034, WFA-038, WFA-039, WFA-040 |

#### WFW-027 — P3.7 OP regeneration and force snapshot

| Field | Content |
|---|---|
| ID and name | `WFW-027` — Regenerate one OP and store the canonical force snapshot |
| Purpose | The only OP increase and the single force baseline |
| Initiating actor | B-02 P3.7 opening |
| Permissions | System only |
| Preconditions | The turn reached P3.7; the snapshot has not been stored |
| Inputs | `op_balance`, `op_cap`, previous post-P5 force, recruitment orders completing this turn |
| Validation | `op_balance = min(op_cap, op_balance + 1)`; key `(nation_id, turn_id)`; no second run |
| Player-visible information | Cap, available, reserved, consumed; own force by type |
| Decision points | None |
| Consent | None |
| System processing | Writes one `REGENERATED` item (including 0 at the cap) and one immutable snapshot before rank 6(a) |
| State transitions | `op_balance` and `available` increase by at most one |
| Resource consequences | None |
| Notifications | Digest |
| Audit and history | `WRA-14` |
| Failure | A stored balance above the cap, a negative balance or a second regeneration is `WRF-34` |
| Cancellation and withdrawal | Not applicable |
| Recovery | A duplicate boundary returns the original receipt and writes nothing |
| Acceptance criteria | P0 and P7 never regenerate; reservations survive the regeneration; the snapshot is the only force source |
| B-10 rules | `WAR-040`–`WAR-043b`, `WAR-053m` |
| Requirements | REQ-654, REQ-681, REQ-694, REQ-696 |
| Formulas | F-WR-001, F-WR-036 |
| Tests | WFA-033, WFA-035, WFA-081, WFA-084 |

#### WFW-028 — P4 recruitment

| Field | Content |
|---|---|
| ID and name | `WFW-028` — Order recruitment at P4 |
| Purpose | Rebuild strength through the ordinary economy |
| Initiating actor | `owner(nation_id)` |
| Permissions | Owner only |
| Preconditions | Unit type unlocked by `MIL-T1`–`MIL-T4`; force cap and single-type share would not be exceeded; crowns and resources available |
| Inputs | Unit type, strength points, `idempotency_key`, confirmation |
| Validation | Force cap `1,000 + 100 × city_count + 2 × total_infrastructure`; training capacity `min(80, 20 + 5 × city_count)`; 60% single-type share (`WRF-24`) |
| Player-visible information | Cost, training turns, arrival turn, resulting cap and share |
| Decision points | Type, quantity, confirm |
| Consent | Owner only |
| System processing | Reserves at acceptance, charges `CAPEX` at P4, adds strength at the opening of the completion turn's P3.7 |
| State transitions | Strength added before the snapshot |
| Resource consequences | Crowns and resources consumed; no OP cost |
| Notifications | Owner |
| Audit and history | `CAPEX`, `WRA-03` |
| Failure | `WRF-24` cap or share; `WRF-12` funds; no partial recruitment |
| Cancellation and withdrawal | Before P4 the order may be cancelled and its reservation released |
| Recovery | The completion turn is `order_turn + training_turns`; a cancelled order never enters a snapshot |
| Acceptance criteria | Arrival before the snapshot; not eligible for an earlier P5; no instant finish |
| B-10 rules | `WAR-054`–`WAR-061` |
| Requirements | REQ-683, REQ-693 |
| Formulas | F-WR-012–F-WR-015 |
| Tests | WFA-049, WFA-055, WFA-056, WFA-105 |

#### WFW-029 — P4 disbanding

| Field | Content |
|---|---|
| ID and name | `WFW-029` — Disband strength at P4 |
| Purpose | Let the owner reduce strength voluntarily, including to satisfy disarmament |
| Initiating actor | `owner(nation_id)` or an accepted `TERM_DISARMAMENT` at P5 |
| Permissions | Owner only for a voluntary disband |
| Preconditions | Strength of the chosen type exists; P4 has not completed |
| Inputs | Unit type, quantity, `idempotency_key` |
| Validation | Quantity ≤ available strength; disbanding is applied at P4 and reflected in the frozen P5 baseline |
| Player-visible information | Resulting strength and cap |
| Decision points | Type and quantity |
| Consent | Owner only |
| System processing | Reduces strength immediately; returns no resources and no crowns; no OP |
| State transitions | Strength reduced before the snapshot |
| Resource consequences | None returned; no refund |
| Notifications | Owner |
| Audit and history | `CAPEX` context only; no destruction event |
| Failure | Cannot be applied between P5 battles |
| Cancellation and withdrawal | Not reversible once P4 completes |
| Recovery | Not applicable |
| Acceptance criteria | No refund; no avoidance of an already frozen battle |
| B-10 rules | `WAR-060`, `WAR-136` |
| Requirements | REQ-683, REQ-690 |
| Formulas | F-WR-031 |
| Tests | WFA-124, WFA-120 |

#### WFW-030 — P4.1 city infrastructure repair

| Field | Content |
|---|---|
| ID and name | `WFW-030` — Order city infrastructure repair at P4.1 |
| Purpose | Give the only recovery path for strike damage |
| Initiating actor | `owner(nation_id)` |
| Permissions | Owner only |
| Preconditions | The city has recorded unrepaired damage; `1 ≤ n ≤ min(10, 500 − I, unrepaired_levels)`; crowns available |
| Inputs | `city_id`, `n`, `idempotency_key`, confirmation |
| Validation | `WRF-37` for above 10 levels, above the damage or above the 500 cap |
| Player-visible information | Levels, exact `URB-043` cost, no materials, Civil Survey `9,000/10,000` only if owned; `I_before` and `I_after_repair` |
| Decision points | City, levels, confirm |
| Consent | Owner only |
| System processing | Reserves crowns at acceptance, charges `CAPEX` at P4.1, restores levels, capitalises a new lot without reversing impairment |
| State transitions | `I` restored; `CAPACITY_OVERDRAWN` clears when `overdrawn_dc = 0` |
| Resource consequences | Crowns spent; no materials; no refund of past impairment |
| Notifications | `INFRASTRUCTURE_REPAIRED`, owner cost |
| Audit and history | `INFRASTRUCTURE_REPAIRED` keyed `order_id`; `CAPEX` |
| Failure | `WRF-37`; nothing is charged and the reservation is released |
| Cancellation and withdrawal | Before P4.1 the order may be cancelled and released |
| Recovery | A retry of the same `order_id` is idempotent; a failed order heals nothing |
| Acceptance criteria | P4.1 commits before P5; the repair cannot retroactively heal a later strike; no city created |
| B-10 rules | `WAR-109h`, `WAR-109i`, `WAR-109m` |
| Requirements | REQ-701, REQ-703 |
| Formulas | F-WR-038 |
| Tests | WFA-051, WFA-052, WFA-059, WFA-060, WFA-105 |

#### WFW-031 — Protection becomes active between P2 and P5

| Field | Content |
|---|---|
| ID and name | `WFW-031` — Fail an accepted operation when protection activates before P5 |
| Purpose | Enforce execution-time protection without a stale snapshot |
| Initiating actor | Pre-P5 validator |
| Permissions | System only |
| Preconditions | An accepted operation; protection or dormancy became active after P2 |
| Inputs | Current protection, pair, NAP, Alliance and dormancy state |
| Validation | Row 4 (and rows 6–7) re-read; `WRF-05` for protection, `WRF-21` for dormancy |
| Player-visible information | Actor sees the block and the counterparty; no private treaty text |
| Decision points | None at pre-P5 |
| Consent | None; protection is not consent |
| System processing | Releases every reservation once and writes `WRA-02`, `WRA-14` |
| State transitions | `SCHEDULED_P5` → `FAILED` |
| Resource consequences | Full release; no consumption |
| Notifications | Actor |
| Audit and history | `WRA-02`, `WRA-14` |
| Failure | This workflow is the failure path |
| Cancellation and withdrawal | Not applicable |
| Recovery | Expiry of protection after the failure does not revive the action; a new submission is required |
| Acceptance criteria | A P2 pass does not survive a later protection change |
| B-10 rules | `WAR-116`, `WAR-116a`, `WAR-117` |
| Requirements | REQ-658, REQ-687 |
| Formulas | F-WR-004 |
| Tests | WFA-065, WFA-070, WFA-071, WFA-072 |

#### WFW-032 — Political `TRANSITION` or `CRISIS` interaction

| Field | Content |
|---|---|
| ID and name | `WFW-032` — Apply the political-state restriction to military orders |
| Purpose | Block new orders without pausing the war or granting a modifier |
| Initiating actor | Validator row 8 at submission, P2 and pre-P5 |
| Permissions | System only |
| Preconditions | `TRANSITION` or `CRISIS` is active |
| Inputs | Political state, the action's acceptance turn and parameters, the operation type |
| Validation | New action → `WRF-09`; accepted defensive commitment meeting all seven `WAR-009g` conditions → row 8 exempt, every other row still runs |
| Player-visible information | The state and the rule; no hidden modifier |
| Decision points | The owner may still propose a ceasefire, surrender or settlement |
| Consent | None |
| System processing | Rejects and reserves nothing, or exempts a qualifying commitment and resolves it |
| State transitions | None for a rejected action; a qualifying commitment resolves |
| Resource consequences | A new action reserves nothing; a qualifying commitment spends only what it already held |
| Notifications | Actor |
| Audit and history | `WRA-02` |
| Failure | `WRF-09` is the only political code |
| Cancellation and withdrawal | An accepted offensive that fails is not converted into a defensive action |
| Recovery | No retroactive revival when the state ends |
| Acceptance criteria | Eight `WAR-009g` scenarios reproduce exactly; war never pauses |
| B-10 rules | `WAR-009g`, `WAR-053j`, `WAR-053k` |
| Requirements | REQ-666 |
| Formulas | F-WR-004 |
| Tests | WFA-011, WFA-065, WFA-072, WFA-100, WFA-110 |

#### WFW-033 — Reroll request during a campaign

| Field | Content |
|---|---|
| ID and name | `WFW-033` — Block a reroll while the nation is party to a campaign |
| Purpose | Preserve identity and record integrity (`UD-032` Option A) |
| Initiating actor | `owner(nation_id)` requesting a B-03 reroll |
| Permissions | B-03 owns the reroll; B-10 supplies the campaign-state check |
| Preconditions | The nation is party to `DECLARED_PENDING`, `ACTIVE`, `SUSPENDED` or `SETTLING` |
| Inputs | Reroll request |
| Validation | Campaign-state check across both outgoing and incoming campaigns |
| Player-visible information | The block reason and the two exits: surrender or wait for the campaign to end |
| Decision points | Surrender, continue, or defer the reroll |
| Consent | Owner only; the block is not a sanction |
| System processing | Records a review signal with the campaign identifier; consumes nothing |
| State transitions | None |
| Resource consequences | None |
| Notifications | Owner |
| Audit and history | Review signal; no `WRA` military event |
| Failure | The reroll is refused, not failed |
| Cancellation and withdrawal | A surrender ends the campaign and releases the block at the next P5 |
| Recovery | Once `ENDED` or `VOID`, the reroll may proceed under B-03 |
| Acceptance criteria | No identity laundering; no campaign transfer to a replacement nation |
| B-10 rules | `WAR-025`–`WAR-030` |
| Requirements | REQ-660 |
| Formulas | F-WR-007 |
| Tests | WFA-073, WFA-076, WFA-079, WFA-080 |

### 5.5 Group E — ceasefire, surrender and settlement

#### WFW-034 — Propose a mutual ceasefire

| Field | Content |
|---|---|
| ID and name | `WFW-034` — Propose a term-free mutual ceasefire |
| Purpose | End a campaign by agreement without transfers |
| Initiating actor | `owner(nation_id)` of either party |
| Permissions | Owner only |
| Preconditions | Campaign is `ACTIVE` |
| Inputs | `campaign_id`, `idempotency_key`, confirmation |
| Validation | One live settlement per campaign; the other owner is the only counterparty |
| Player-visible information | Terms: end the war, no transfers, no exclusion, no protection; outcome `MUTUAL_PEACE` with `DRAW` |
| Decision points | Propose or not; the counterparty accepts or rejects |
| Consent | Both owners; silence never accepts (`WAR-127`) |
| System processing | Creates a settlement in `PROPOSED` with `TERM_CEASEFIRE`; on acceptance the campaign enters `SETTLING` |
| State transitions | `ACTIVE` → `SETTLING` on acceptance → `ENDED` at P5.3 |
| Resource consequences | None |
| Notifications | Both owners |
| Audit and history | `WRA-12` |
| Failure | Silent expiry after 12 turns; no cooldown |
| Cancellation and withdrawal | Either proposer may withdraw before acceptance |
| Recovery | A rejected or expired proposal creates no obligation |
| Acceptance criteria | No transfer, no exclusion, no protection; only the owners act |
| B-10 rules | `WAR-121`–`WAR-124`, `WAR-127` |
| Requirements | REQ-690 |
| Formulas | F-WR-030 |
| Tests | WFA-057, WFA-061, WFA-062, WFA-111 |

#### WFW-035 — Propose a settlement with terms

| Field | Content |
|---|---|
| ID and name | `WFW-035` — Propose a closed-term settlement |
| Purpose | Let the parties end a war with enforceable, immediate terms |
| Initiating actor | `owner(nation_id)` of either party |
| Permissions | Owner only |
| Preconditions | Campaign is `ACTIVE`; no live settlement; every term is in the closed catalogue |
| Inputs | `campaign_id`, the term set, payer and amounts, `idempotency_key`, confirmation naming every term |
| Validation | Term ∈ `TERM_CEASEFIRE`, `TERM_REPARATION_CROWNS`, `TERM_REPARATION_RESOURCE`, `TERM_DISARMAMENT`, `TERM_EXCLUSION`, `TERM_WHITE_PEACE`; reparation caps 25% / 100,000 crowns / 10% per resource; prohibited terms rejected at proposal |
| Player-visible information | Every term, the exact transfer, the irreversibility and the 12-turn window |
| Decision points | Term set, payer, amounts, confirm |
| Consent | Proposer now; counterparty must accept the exact version |
| System processing | Creates `PROPOSED`; terms immutable after submission; a counter replaces the live version |
| State transitions | `PROPOSED` → `COUNTERED`/`ACCEPTED`/`REJECTED`/`WITHDRAWN`/`EXPIRED` |
| Resource consequences | None until acceptance; the payer's value is reserved at acceptance |
| Notifications | Counterparty only while pending; public once accepted |
| Audit and history | `WRA-12` |
| Failure | Invalid term, prohibited term or over-cap amount is rejected at proposal |
| Cancellation and withdrawal | Proposer may withdraw before acceptance |
| Recovery | Expiry after 12 turns; silence is rejection |
| Acceptance criteria | No debt, no instalment, no loot, no Alliance obligation; no term outside the six |
| B-10 rules | `WAR-125`–`WAR-130` |
| Requirements | REQ-690 |
| Formulas | F-WR-029, F-WR-030, F-WR-031 |
| Tests | WFA-057, WFA-058, WFA-059, WFA-061, WFA-064 |

#### WFW-036 — Respond to a settlement

| Field | Content |
|---|---|
| ID and name | `WFW-036` — Counter, accept, reject or withdraw a settlement |
| Purpose | Provide the only four responses and no fifth |
| Initiating actor | `owner(nation_id)` of either party, by role |
| Permissions | Owner only; the proposer may withdraw, either owner may counter or reject, only the counterparty may accept the exact live version |
| Preconditions | A live settlement in `PROPOSED` or `COUNTERED` |
| Inputs | `settlement_id`, response, counter terms if any, `idempotency_key` |
| Validation | The accepting owner must not be the proposer of the live version; counter terms must differ; the window must be open |
| Player-visible information | The exact live terms and the 12-turn expiry |
| Decision points | Counter, accept, reject or withdraw |
| Consent | Explicit per owner; an acceptance is never inferred |
| System processing | Writes `WRA-12`; an acceptance reserves the payer's value and moves the campaign to `SETTLING` |
| State transitions | `PROPOSED` → `COUNTERED`/`ACCEPTED`/`REJECTED`/`WITHDRAWN` |
| Resource consequences | On acceptance only: payer's OP-free value reserved |
| Notifications | Both owners |
| Audit and history | `WRA-12` (settlement, campaign, parties, terms, state, transfer id) |
| Failure | A forged acceptance by the proposer fails `WRF-01` and changes nothing |
| Cancellation and withdrawal | Withdrawal is the proposer's terminal exit |
| Recovery | A duplicate response returns the original receipt |
| Acceptance criteria | No automatic acceptance; one live version; no response after expiry |
| B-10 rules | `WAR-125`–`WAR-128` |
| Requirements | REQ-690, REQ-692 |
| Formulas | F-WR-030 |
| Tests | WFA-057, WFA-058, WFA-060, WFA-061, WFA-062 |

#### WFW-037 — Surrender

| Field | Content |
|---|---|
| ID and name | `WFW-037` — Surrender unilaterally |
| Purpose | Guarantee an off-ramp and make the reroll block escapable |
| Initiating actor | `owner(nation_id)` of one party |
| Permissions | Owner only; the opponent cannot refuse |
| Preconditions | Campaign is `ACTIVE` or `SUSPENDED` |
| Inputs | `campaign_id`, `idempotency_key`, confirmation naming `TERM_CEASEFIRE`, no transfers and the permanent record |
| Validation | Owner identity; campaign state |
| Player-visible information | Outcome `SURRENDER`, opponent `LIMITED_VICTORY`, no transfers, no disarmament, no exclusion, no protection |
| Decision points | Confirm or not |
| Consent | Surrendering owner only; the opponent's consent is not required (`WAR-132`) |
| System processing | Creates a settlement with `TERM_CEASEFIRE` only; the campaign moves to `SETTLING` and ends at P5.3 |
| State transitions | `ACTIVE` → `SETTLING` → `ENDED` |
| Resource consequences | None |
| Notifications | Both owners |
| Audit and history | `WRA-12`, `WRA-13` |
| Failure | Surrender cannot be refused and cannot be withdrawn after P5.3 |
| Cancellation and withdrawal | A settlement offered before P5.3 takes precedence if accepted |
| Recovery | The reroll block lifts at `ENDED` |
| Acceptance criteria | No transfer, no exclusion unless separately negotiated, no protection |
| B-10 rules | `WAR-131`–`WAR-133` |
| Requirements | REQ-660, REQ-690, REQ-692 |
| Formulas | F-WR-010, F-WR-030 |
| Tests | WFA-057, WFA-061, WFA-063, WFA-076, WFA-079 |

#### WFW-038 — Settlement completion at P5.3

| Field | Content |
|---|---|
| ID and name | `WFW-038` — Complete an accepted settlement atomically |
| Purpose | Apply every term once and end the campaign |
| Initiating actor | B-02 P5.3 resolver |
| Permissions | System only |
| Preconditions | Settlement is `ACCEPTED`; the payer's reservation is intact |
| Inputs | Terms, reserved amounts, campaign, parties |
| Validation | Re-checks the reserved value; a lost reservation is `WRF-33` |
| Player-visible information | Transfer identifier, amounts and the campaign outcome |
| Decision points | None |
| Consent | Both owners already accepted the exact version |
| System processing | One transaction writes `TRANSFER_OUT`/`TRANSFER_IN`, the disarmament disband, the exclusion row, `WRA-12`, `WRA-13` and `COMPLETED` |
| State transitions | `SETTLING` → `ENDED`; settlement `ACCEPTED` → `COMPLETED` |
| Resource consequences | Matched transfer; conservation holds; no value created |
| Notifications | Both owners; terms public |
| Audit and history | `WRA-12`, `WRA-13` |
| Failure | Any missing leg fails the whole settlement; nothing partial |
| Cancellation and withdrawal | Not applicable after acceptance |
| Recovery | One completion per settlement identifier |
| Acceptance criteria | Two transfer legs equal and matched; exclusion duration 84 turns; no ongoing body |
| B-10 rules | `WAR-134`–`WAR-141` |
| Requirements | REQ-663, REQ-689, REQ-690 |
| Formulas | F-WR-029, F-WR-031 |
| Tests | WFA-057, WFA-059, WFA-060, WFA-064, WFA-111 |

#### WFW-039 — Settlement atomic failure

| Field | Content |
|---|---|
| ID and name | `WFW-039` — Fail a settlement whose reservation or balance was lost |
| Purpose | Prevent a partial transfer and restore the campaign honestly |
| Initiating actor | B-02 P5.3 resolver |
| Permissions | System only |
| Preconditions | Settlement is `ACCEPTED` and a reserved amount is no longer available |
| Inputs | Reservation state, settlement identifier |
| Validation | Any mismatch is `WRF-33`; no partial transfer is attempted |
| Player-visible information | Both owners see the failure and the returned `ACTIVE` campaign |
| Decision points | The parties may propose again |
| Consent | The failure creates no new obligation |
| System processing | Writes `WRA-12` with `FAILED`; campaign returns to `ACTIVE`; no ledger leg is written |
| State transitions | `SETTLING` → `ACTIVE`; settlement → `FAILED` |
| Resource consequences | None moved |
| Notifications | Both owners |
| Audit and history | `WRA-12` |
| Failure | This workflow is the failure path |
| Cancellation and withdrawal | Not applicable |
| Recovery | A new proposal is required; terms are not revived |
| Acceptance criteria | Zero transfer legs on failure; campaign state restored exactly |
| B-10 rules | `WAR-137`, `WAR-138` |
| Requirements | REQ-663, REQ-690 |
| Formulas | F-WR-029 |
| Tests | WFA-060, WFA-062, WFA-084 |

### 5.6 Group F — recovery and turn close

#### WFW-040 — Interrupted P5 recovery and P7 close

| Field | Content |
|---|---|
| ID and name | `WFW-040` — Recover an interrupted P5 and close the turn at P7 |
| Purpose | Guarantee one outcome per battle and one published turn |
| Initiating actor | B-02 recovery path and P7 close |
| Permissions | System only |
| Preconditions | A checkpoint exists after an interruption, or the turn reached P7 |
| Inputs | Checkpoint, `APPLIED` markers, ledger items, `reserved` per nation |
| Validation | Before resuming a battle, its marker and ledger items are all present or all absent; P7 verifies `reserved = 0` |
| Player-visible information | Nothing partial; a battle is visible only after `WRA-04`; the turn is visible only when published |
| Decision points | None |
| Consent | None |
| System processing | Resumes at the last completed checkpoint; voids unresolved actions with `WRF-22`; releases them; publishes only when every check passes |
| State transitions | Resumed battle → `RESOLVED`; unresolved → `VOID_P7` |
| Resource consequences | Each release once; no refund of a consumed OP |
| Notifications | Publication event for the turn |
| Audit and history | `WRA-04` per battle, `WRA-14` per release, `WRA-05` for a state change |
| Failure | A remaining reservation at P7 is `WRF-34`; the checkpoint holds and the turn is not published |
| Cancellation and withdrawal | Not applicable |
| Recovery | This workflow is the recovery; replaying against the same baseline and seed is deterministic |
| Acceptance criteria | Applied battles = resolved operations; one battle per operation; losses reconcile; no partial publication |
| B-10 rules | `WAR-043`, `WAR-097`–`WAR-100`, `WAR-158`, `WAR-159` |
| Requirements | REQ-654, REQ-655, REQ-657, REQ-661 |
| Formulas | F-WR-022, F-WR-034 |
| Tests | WFA-081, WFA-082, WFA-083, WFA-084, WFA-085, WFA-086 |

---

## 6. Workflow-to-state transition ledger

| Workflow | From | To | Trigger | Event |
|---|---|---|---|---|
| WFW-001 | none | `DECLARED_PENDING` | Validator pass and atomic acceptance | `WRA-01`, `WRA-14` |
| WFW-002 | none | none | Any failing check | `WRA-02` |
| WFW-003 | `DECLARED_PENDING` | `VOID` | Owner withdrawal before freeze | `WRA-05`, `WRA-14` |
| WFW-004 | `DECLARED_PENDING` | `ACTIVE` | P5.1 resolution | `WRA-05`, `WRA-14` |
| WFW-005 | `ACTIVE` | `SUSPENDED` | Dormancy at P0/P5.2 | `WRA-05`, `WRA-14` |
| WFW-006 | `ACTIVE`/`SUSPENDED` | `ENDED` | Expiry, abandonment or stalemate | `WRA-05`, `WRA-13` |
| WFW-007–WFW-016 | none | `RESERVED` | Accepted operation | `WRA-03`, `WRA-14` |
| WFW-017 | `RESERVED` | `CANCELLED` or new `RESERVED` | Owner amend/cancel before freeze | `WRA-03`, `WRA-14` |
| WFW-018 | `RESERVED` | `FAILED` | Validation failure | `WRA-02`/`WRA-03`, `WRA-14` |
| WFW-019 | any | unchanged | Duplicate key | `WRA-03` original |
| WFW-020 | `SCHEDULED_P5` | `RESOLVED` | Battle commit | `WRA-04` |
| WFW-021–WFW-024 | `RESOLVED` | `RESOLVED` | Loss, state, damage and progress application | `WRA-04`, `WRA-06`, `WRA-07`, `INFRASTRUCTURE_DAMAGED` |
| WFW-025 | none | `RATION_SHORT` set/cleared | P3.7 ration | `OBLIGATION_*`, `WRA-14` |
| WFW-026 | none | readiness change | P3.7 upkeep | `OBLIGATION_*`, `WRA-14` |
| WFW-027 | none | `op_balance` +1, snapshot stored | P3.7 opening | `WRA-14` |
| WFW-028 | none | strength added | P3.7 of the completion turn | `CAPEX` |
| WFW-029 | none | strength reduced | P4 or P5 disarmament | `CAPEX` context |
| WFW-030 | none | `I` restored, overdraw cleared | P4.1 | `INFRASTRUCTURE_REPAIRED`, `CAPEX` |
| WFW-031 | `SCHEDULED_P5` | `FAILED` | Protection at pre-P5 | `WRA-02`, `WRA-14` |
| WFW-032 | none | none or `RESOLVED` | Political state | `WRA-02` |
| WFW-033 | none | none | Reroll request | review signal |
| WFW-034–WFW-037 | `ACTIVE` | `SETTLING` | Accepted ceasefire, settlement or surrender | `WRA-12` |
| WFW-038 | `SETTLING` | `ENDED` | P5.3 completion | `WRA-12`, `WRA-13` |
| WFW-039 | `SETTLING` | `ACTIVE` | P5.3 atomic failure | `WRA-12` |
| WFW-040 | any | `VOID_P7` where unresolved | P7 close | `WRA-14`, `WRA-05` |

**6.1** Every transition above writes exactly one state event; no workflow writes a state without an event and no event exists without a transition (`WAR-017`, `WAR-153`).

**6.2** No workflow moves a campaign from `ENDED` back to a live state. No workflow moves `VOID` anywhere. `ARCHIVED` is a read-model change only (`WAR-030`, `WAR-031`).

---

## 7. Cross-lifecycle matrices

### 7.1 Operation, target, counter and phase

| Operation | Target class | Counter | Resolves | Offensive slot | Progress families | City effect |
|---|---|---|---|---|---|---|
| `OP-01 RAID` | Enemy nation in campaign | `FORTIFY` | P5.6 | Yes | ATTRITION, INTERDICTION | None |
| `OP-02 ASSAULT` | Enemy nation in campaign | `FORTIFY` | P5.6 | Yes | ATTRITION, INTERDICTION | None |
| `OP-03 AIR_STRIKE` | Enemy nation in campaign | `INTERCEPT` | P5.6 | Yes | ATTRITION, INTERDICTION, AIR, STRIKE | None |
| `OP-04 BLOCKADE` | Enemy nation in campaign | `BREAK_BLOCKADE` | P5.6 | Yes | INTERDICTION, BLOCKADE | None |
| `OP-05 MISSILE_STRIKE` | Enemy nation, optionally one city | `INTERCEPT` | P5.6 | Yes | ATTRITION, STRIKE | Infrastructure only |
| `OP-06 INTERCEPT` | Conditional incoming air/missile | none | P5.5 | No | AIR, DEFENCE | None |
| `OP-07 FORTIFY` | Self | none | P5.5 | No | DEFENCE | None |
| `OP-08 BREAK_BLOCKADE` | Active enemy blockade on self | none | P5.7 | No | DEFENCE | None |
| `OP-09 RESUPPLY` | Self | none | P5.5 | No | none | None |

### 7.2 Protection and eligibility by validation point

| Condition | Submission | P2 | Pre-P5 | Code |
|---|---|---|---|---|
| Newcomer protection active | Reject | Reject | Reject | `WRF-05` |
| Protection expired before P2 | Allow | Allow | Allow | — |
| Protection activated after P2 | Allow (then fail) | Allow | Reject | `WRF-05` |
| Protection expired after a P2 failure | — | Failed | Stays failed; no revival | `WRF-05` |
| National `DP-T01` active, declaration | Reject | Reject | Reject | `WRF-06` |
| National `DP-T01` active, operation in a live campaign | Allow | Allow | Allow | — |
| Same-Alliance pair | Reject | Reject | Reject | `WRF-07` + `AUD-AL-017` |
| Covered `AT-E01` pair | Reject | Reject | Reject | `WRF-08` + `AUD-AL-017` |
| `AT-E00` record-only | Allow | Allow | Allow | — |
| Restricted pair | Reject | Reject | Reject | `WRF-04` |
| Dormant actor or target | Reject | Reject | Reject | `WRF-02`/`WRF-03`/`WRF-21` |
| `TERM_EXCLUSION` active | Reject | Reject | Reject | `WRF-32` |
| `TRANSITION`/`CRISIS`, new action | Reject | Reject | Reject | `WRF-09` |
| `TRANSITION`/`CRISIS`, accepted defensive commitment | Allow | Exempt row 8 only | Exempt row 8 only | — |
| `RATION_SHORT`, new offensive | Allow | Allow | Reject | `WRF-35` |
| `RATION_SHORT`, defensive or sustainment | Allow | Allow | Allow | — |

### 7.3 Military Food accounting

| Component | Phase | Source | Reserved | Effect | Failure |
|---|---|---|---|---|---|
| Civilian Food | P3.6 | Opening + production − other reservations | No | Priority consumption | `unmet_food` under `ECN-082` |
| Protected civilian requirement | P3.6 | `ceil(population/1,000)` | No | Never reduced for the military | — |
| `OP-09` field ration (4 Food) | Acceptance / P3.6 / P5 | Eligible surplus above the protected requirement | Yes | +100 readiness at P5 | `WRF-25` |
| Garrison ration | P3.7 6(a) | Unreserved Food after P3.6 | No | None if paid; `RATION_SHORT` if not | `WRF-35` pre-P5 |
| Readiness upkeep | P3.7 6(b) | Unreserved crowns, ammunition, gasoline | No | +50 readiness if paid; −100 if not | none by itself |

### 7.4 Infrastructure timing

| Value | Written | Read by |
|---|---|---|
| `I_open(T)` | Prior P5 | Acceptance/P2 of construction and repair |
| `I_pre(T)` | P4.1 start | P4.1 validation |
| `I_post_P4_1(T)` | P4.1 | P5 combat |
| `I_combat(T)` | P5 battle start | `F-WR-037`, impairment denominator |
| `I_post_P5(T)` | P5 damage | `I_open(T+1)`, P6 disclosure |
| `capacity_construction(T)` | Opening | Construction in T |
| `capacity_effective(T+1)` | T+1 opening | Construction in T+1 |
| `housing_population(T)` | P3.8 of T | Population and crowding at P3.8 of T |
| `housing_effective(T+1)` | T+1 opening | Population and crowding at P3.8 of T+1 |
| `BV_post_P4_1(T)` | P4.1 of T | Next applicable P3.8 wealth |
| `BV_post_P5(T)` | P5 of T | P3.8 of T+1 |

### 7.5 Settlement terms

| Term | Changes | Enforced at | Cap or duration | Partial possibility |
|---|---|---|---|---|
| `TERM_CEASEFIRE` | Ends the war | P5.3 | — | No |
| `TERM_REPARATION_CROWNS` | Crown transfer | P5.3 | 25% and 100,000 crowns | No; atomic |
| `TERM_REPARATION_RESOURCE` | One resource transfer | P5.3 | 10% per resource | No; atomic |
| `TERM_DISARMAMENT` | Strength disband | P5.3 | Stated amount | Yes; remainder cancelled, no debt |
| `TERM_EXCLUSION` | Declaration block | Submission/P2/pre-P5 | 84 turns | No |
| `TERM_WHITE_PEACE` | Ends the war, no fault | P5.3 | — | No |

### 7.6 OP accounting scenarios

| Scenario | Start | Action | End | Required event |
|---|---|---|---|---|
| Regenerate below cap | balance 8, reserved 0 | P3.7 | balance 9 | `REGENERATED 1` |
| Regenerate at cap | balance 10, reserved 0 | P3.7 | balance 10 | `REGENERATED 0` |
| Reserve two actions | balance 8 | hold 2 and 3 | available 3 | Two `HELD` |
| P2 failure | reserved 5 | release 3 | available 6 | `RELEASED 3` |
| Consume at P5 | reserved 2 | resolve | balance −2, reserved 0 | `CONSUMED 2` |
| P7 void | reserved 2 | unresolved | balance unchanged, available +2 | `RELEASED 2`, `WRF-22` |
| Duplicate boundary | any | second run | unchanged | none; original receipt |

### 7.7 Campaign outcome matrix

| Condition | Outcome | Reparations | Exclusion | Protection |
|---|---|---|---|---|
| One primary reaches 1,000, opponent < 250 | `DECISIVE_VICTORY` | Only by settlement | Only by settlement | None |
| One primary reaches 1,000, opponent ≥ 250 | `LIMITED_VICTORY` | Only by settlement | Only by settlement | None |
| Both reach 1,000; `primary + floor(secondary/2)` differ | `LIMITED_VICTORY` | Only by settlement | Only by settlement | None |
| Both reach 1,000; exact tie | `DRAW` | None | None | None |
| Mutual ceasefire accepted | `MUTUAL_PEACE` (`DRAW`) | None | None | None |
| Surrender | `SURRENDER` | None | None | None |
| Deadline | `EXPIRY` | None | None | None |
| 48 suspended turns | `ABANDONED` | None | None | None |

---

## 8. Player journeys

**J1 — Declare and raid (happy path).** Owner A opens the panel, selects B, chooses `OBJ-ATTRITION` primary and `OBJ-INTERDICTION` secondary, reads the cost (2 OP, 500 crowns) and confirms. `WFW-001` accepts; A holds 2 OP and 500 crowns. At P5.1 the campaign activates. At the next boundary A submits `OP-01 RAID` (2 OP, 5 gasoline, 5 ammunition); it passes all three validation runs; at P5.6 the battle resolves at `ATTACKER_VICTORY`; A gains 40 ATTRITION; both lose strength; readiness −25 each. Tests: WFA-009, WFA-013, WFA-025, WFA-041.

**J2 — Defend and counter.** B, attacked by `OP-01`, had armed `OP-07 FORTIFY` at P5.5. The first ground attack reads `counter_defence_bp = 12500`, the tier falls to `REPULSED`, B gains `OBJ-DEFENCE` progress and A loses 1,000 bp against B's 700 bp. B sees the battle report at P6; the public summary shows only tier and loss band. Tests: WFA-032, WFA-066, WFA-068.

**J3 — Blockade and break.** A submits `OP-04 BLOCKADE` and wins; B enters `BLOCKADED` for 12 turns (+25% bundle, −25 recovery). B submits `OP-08 BREAK_BLOCKADE`; it resolves at P5.7, wins, removes the state and starts A's 12-turn cooldown. B gains `OBJ-DEFENCE`; A's `OBJ-BLOCKADE` takes counter-progress. Tests: WFA-029, WFA-065, WFA-069.

**J4 — Missile strike a city and repair.** A at `MIL-T4` submits `OP-05` with `CITY(city_id)`; all national rows pass and the city row passes. The strike is decisive; `removed = 3` at `I = 60`; capacity and housing fall; book value is impaired by 6; no facility or person is affected. At the next P4.1 B repairs 3 levels at the `URB-043` cost, capitalising a new lot without reversing the impairment. Tests: WFA-030, WFA-031, WFA-051, WFA-052, WFA-059, WFA-105, WFA-106.

**J5 — Food shortage turn.** A's garrison needs 4 Food; unreserved Food after P3.6 is 3. The whole obligation is cancelled, readiness falls 100, `RATION_SHORT` is set. At pre-P5 A's new `OP-02 ASSAULT` fails `WRF-35` and releases; A's armed `OP-07 FORTIFY` still resolves. Next turn a paid ration clears the flag with no catch-up. Tests: WFA-034, WFA-035, WFA-036, WFA-037, WFA-040.

**J6 — Political transition mid-campaign.** `TRANSITION` begins after A accepted a `FORTIFY`. At pre-P5 row 8 exempts the accepted defensive commitment; `FORTIFY` resolves. A's new `RAID` in the same window is refused `WRF-09` and reserves nothing. The deadline continues to run. Tests: WFA-072, WFA-100, WFA-110.

**J7 — Newcomer protection expiry.** B is protected when A declares; the declaration fails `WRF-05` at submission and again at P2 while the protection lasts. After 84 turns the protection expires; A declares again and passes. The earlier failure is not revived. Tests: WFA-009, WFA-070, WFA-071.

**J8 — NAP and same-Alliance block.** A and B share an Alliance; A's declaration fails `WRF-07` with `AUD-AL-017`. Later A leaves; a still-active `AT-E01` NAP between A's new Alliance and B fails the operation with `WRF-08` and a second `AUD-AL-017`. A record-only `AT-E00` never blocks. Tests: WFA-097, WFA-098, WFA-099, WFA-100, WFA-101.

**J9 — Dormant opponent and abandonment.** B becomes dormant; the campaign becomes `SUSPENDED` and the deadline keeps running. A's pending raid fails `WRF-21` and releases. After 48 suspended turns the campaign ends `ABANDONED` with a limited victory for A, no reparations and no protection. Tests: WFA-073, WFA-074, WFA-075, WFA-077.

**J10 — Negotiated settlement.** B, losing, proposes `TERM_REPARATION_CROWNS` of 20,000 and `TERM_EXCLUSION` of 84 turns. A counters with 10,000 and no exclusion. B accepts. At P5.3 the crown transfer is reserved, matched and applied atomically; the campaign ends `ENDED` and the exclusion blocks declarations only. Tests: WFA-057, WFA-058, WFA-059, WFA-064.

**J11 — Surrender and reroll.** A is losing and wants to reroll. The reroll is blocked while the campaign is `ACTIVE`. A surrenders under `WFW-037`; the campaign ends `SURRENDER` with a limited victory for B and no transfers. The reroll block lifts at `ENDED`. Tests: WFA-063, WFA-076, WFA-079.

**J12 — Expiry and stalemate.** Neither side resolves an offensive for 24 turns; `STALEMATE` is public. At 48 turns the campaign expires at P6 with `EXPIRY`, no reparations and no protection. A later raid resets the counter only if it resolves before expiry. Tests: WFA-019, WFA-020, WFA-077, WFA-078.

**J13 — Double-click and replay.** A double-submits a raid; the second request carries the same key and returns the original receipt with `WRF-13`; only one `HELD` and one battle exist. A captured request replayed with a new key is a new submission and must pass every check. Tests: WFA-081, WFA-082, WFA-083, WFA-113.

**J14 — Interrupted P5.** The resolver crashes after battle one commits and before battle two. Recovery reads battle one's `APPLIED` marker and skips it; battle two re-runs against the same baseline and seed and produces the same result. No partial battle is visible before `WRA-04`. Tests: WFA-083, WFA-084, WFA-085, WFA-086.

**J15 — Alliance coordination refused.** An Alliance officer attempts to submit a raid for a member and to read the member's readiness. Both are refused; no OP moves and no data is returned. The member may act for itself only. Tests: WFA-001, WFA-002, WFA-089, WFA-097.

**J16 — Protection activates between P2 and P5.** B was unprotected at P2. Before pre-P5 B becomes a protected newcomer. A's accepted raid fails `WRF-05` at pre-P5 and every reservation is released; the P2 pass is not a guarantee. Tests: WFA-070, WFA-071, WFA-072.

**J17 — Loss cap reached mid-campaign.** A's cumulative loss reaches 60% of its campaign-start strength. A further battle applies zero strength loss to A, still applies −25 readiness, and the report states `LOSS_CAP_REACHED`. A can still be attacked and still earns no progress on failure. Tests: WFA-050, WFA-052, WFA-053, WFA-056.

---

## 9. Edge-case register

| ID | Class | Scenario | Expected outcome | Workflow | Test |
|---|---|---|---|---|---|
| `WFE-001` | A | A request names another nation's `nation_id` in the body | `WRF-01`; nothing mutates | WFW-001, WFW-002 | WFA-001 |
| `WFE-002` | A | An Alliance officer submits an operation for a member | Refused; no OP moves; no record in the member's name | WFW-007, WFW-018 | WFA-002 |
| `WFE-003` | A | An administrator attempts an in-place edit of a committed battle | Rejected; only a recorded reversal is permitted | WFW-020, WFW-040 | WFA-003 |
| `WFE-004` | A | Two sessions submit the same intended declaration with different keys | Slot check admits one; the second fails `WRF-10` | WFW-001, WFW-019 | WFA-004 |
| `WFE-005` | B | Target enters newcomer protection between submission and P2 | `WRF-05` at P2; everything released; campaign `VOID` | WFW-002, WFW-031 | WFA-009 |
| `WFE-006` | B | Target signs a `DP-T01` NAP after submission, before P2 | `WRF-06` at P2; the war never activates | WFW-002, WFW-031 | WFA-010 |
| `WFE-007` | B | Declarer has an incoming campaign but no outgoing slot | `WRF-10`; nothing reserved | WFW-001 | WFA-011 |
| `WFE-008` | B | Primary and secondary objectives are identical | Submission rejected as invalid input before the validator | WFW-001 | WFA-012 |
| `WFE-009` | C | Deadline falls on the same turn as a primary completion | P6 evaluates completion first; `LIMITED_VICTORY` or `DECISIVE_VICTORY`, not `EXPIRY` | WFW-006 | WFA-017 |
| `WFE-010` | C | A settlement is accepted on the deadline turn | P5.3 completes it before P5.4 expiry | WFW-038, WFW-006 | WFA-018 |
| `WFE-011` | C | 24 stale turns, then a resolved raid | `STALEMATE` clears; no expiry at 48 | WFW-006 | WFA-019 |
| `WFE-012` | J | A reroll is requested in the same boundary as a `VOID` record | The block lifts only after `VOID` is recorded | WFW-033 | WFA-076 |
| `WFE-013` | D | `OP-05` city target belongs to a third nation | `WRF-36`; no national check is waived | WFW-012 | WFA-030 |
| `WFE-014` | D | `OP-04` while a blockade by either side is active | `WRF-27`; no reservation | WFW-010 | WFA-029 |
| `WFE-015` | D | A second `OP-07` in the same P5 | `WRF-31`; no stacking | WFW-014 | WFA-032 |
| `WFE-016` | E | `OP-09` at readiness 1,000 | `WRF-30`; nothing reserved | WFW-016 | WFA-038 |
| `WFE-017` | E | Nation is both denied and blockaded | `surcharge_bp = 5000` once; RAID bundle 8/8, never 8.25 or a second rounding | WFW-007, WFW-010 | WFA-033 |
| `WFE-018` | E | Ration demand 4, unreserved Food 3 | Whole obligation cancelled; readiness −100; `RATION_SHORT`; no debt | WFW-025 | WFA-034 |
| `WFE-019` | E | `OP-09` requests 4 Food with eligible surplus 3 | `WRF-25` at acceptance; nothing reserved | WFW-016 | WFA-036 |
| `WFE-020` | E | P3.6 must release two `OP-09` reservations | Reverse acceptance order; both fail `WRF-25`; civilians keep the Food | WFW-016, WFW-025 | WFA-037 |
| `WFE-021` | F | Both attack and defence power are zero | `base_ratio_bp = 5000`; fortune decides; `CONTESTED` at fortune 0 | WFW-020 | WFA-041 |
| `WFE-022` | F | Two attacks by one attacker in one P5 | Second uses baseline minus cumulative losses; readiness is not reduced twice as a baseline input | WFW-020, WFW-021 | WFA-042 |
| `WFE-023` | F | Fortune +500 with base ratio 7,400 | Effective 7,900; `DECISIVE_VICTORY`; no rounding of the roll | WFW-020 | WFA-043 |
| `WFE-024` | F | Attacker requests exact enemy strength before P5 | Only the threat band is returned; exact values appear in the report after `WRA-04` | WFW-020 | WFA-044 |
| `WFE-025` | G | A loss would exceed 20% of engaged strength | Capped; the report states the cap | WFW-021 | WFA-049 |
| `WFE-026` | G | Campaign cumulative loss reaches 60% | Zero further strength loss; readiness loss continues; `LOSS_CAP_REACHED` | WFW-021 | WFA-050 |
| `WFE-027` | G | City at `I = 10` is struck victoriously | `removed = 0`; no damage event; the battle still resolves | WFW-023 | WFA-051 |
| `WFE-028` | G | Repair `n = 5` with 3 unrepaired levels | `WRF-37` at P4.1; nothing charged; reservation released | WFW-030 | WFA-052 |
| `WFE-029` | H | The settlement reservation is lost before P5.3 | `WRF-33`; campaign returns `ACTIVE`; zero transfer legs | WFW-039 | WFA-060 |
| `WFE-030` | H | A proposal is unanswered for 12 turns | `EXPIRED`; silence never accepts | WFW-035, WFW-036 | WFA-061 |
| `WFE-031` | H | Disarmament requests more strength than exists | Remainder cancelled; partial satisfaction; settlement still completes; no debt | WFW-038 | WFA-064 |
| `WFE-032` | H | Surrender while a settlement is `PROPOSED` | The surrender ends the campaign with `TERM_CEASEFIRE`; the open proposal terminates; one outcome | WFW-037 | WFA-063 |
| `WFE-033` | I | Protection activates between P2 and pre-P5 | `WRF-05` at pre-P5; every reservation released | WFW-031 | WFA-070 |
| `WFE-034` | I | Protection expires after a P2 failure | The failure stands; a new submission is required | WFW-031 | WFA-071 |
| `WFE-035` | I | `OP-04` and `OP-08` in the same turn | `OP-08` resolves at P5.7; a success removes the state and starts the cooldown | WFW-015 | WFA-069 |
| `WFE-036` | J | Reroll requested while `SETTLING` | Blocked; only surrender or expiry ends the wait | WFW-033 | WFA-076 |
| `WFE-037` | J | Declarer is dormant at P0 with a pending declaration | `SUSPENDED`; the declaration fails `WRF-21`; everything released | WFW-005 | WFA-073 |
| `WFE-038` | J | Target dormant at P2 but awake at pre-P5 | The operation proceeds; execution-time state governs | WFW-031 | WFA-074 |
| `WFE-039` | J | Both sides dormant for 48 suspended turns | `ABANDONED` with `DRAW`; no reparations | WFW-006 | WFA-077 |
| `WFE-040` | J | A belligerent retires; the account rerolls | Campaign stays attributed; record readable; nothing transfers | WFW-006, WFW-033 | WFA-078 |
| `WFE-041` | K | Duplicate submission with the same key | `WRF-13`; original receipt; one `HELD` | WFW-019 | WFA-081 |
| `WFE-042` | K | P5 interrupted after a battle committed | Resume skips the `APPLIED` battle; no double losses | WFW-040 | WFA-083 |
| `WFE-043` | K | P5 interrupted before a battle committed | Replay against the same baseline and seed produces the same tier and losses | WFW-040 | WFA-084 |
| `WFE-044` | K | P7 finds a remaining reservation | `WRF-34`; checkpoint held; the turn is not published | WFW-040 | WFA-086 |
| `WFE-045` | L | A third party queries exact readiness through the API | Denied; only a band may be returned | WFW-020 | WFA-089 |
| `WFE-046` | L | An Alliance requests a member's battle report | Denied; `AX-18` surface unchanged | WFW-020 | WFA-090 |
| `WFE-047` | L | A public statistic would identify four nations | Withheld or coarsened under D-027 | WFW-020 | WFA-091 |
| `WFE-048` | L | A blocked attack names an `AT-E01` counterparty | The actor sees the rule and counterparty but no private text; `AUD-AL-017` uses B-09 fields only | WFW-002 | WFA-092 |
| `WFE-049` | M | Same-Alliance pair attempts a declaration | `WRF-07` + `AUD-AL-017`; no OP moved | WFW-002 | WFA-097 |
| `WFE-050` | M | Covered `AT-E01` pair attempts an operation | `WRF-08` + `AUD-AL-017` | WFW-002 | WFA-098 |
| `WFE-051` | M | A client labels an `AT-E00` as a NAP | The server ignores the label and admits on the canonical validator only | WFW-002 | WFA-099 |
| `WFE-052` | M | A member leaves the Alliance between P2 and pre-P5 | Membership re-read; the same-Alliance block lifts but an active `AT-E01` still blocks (checks separate and cumulative) | WFW-031 | WFA-101 |
| `WFE-053` | N | City strike reduces infrastructure, capacity and housing | The next P3.8 applies `DMP-031` crowding; no casualties at P5 | WFW-023 | WFA-105 |
| `WFE-054` | N | City strike impairs book value | National wealth at the next P3.8 reflects `BV_post_P5`; a 5,000 facility is unchanged | WFW-023 | WFA-106 |
| `WFE-055` | N | A war is active and trade continues | B-07 trade is unaffected; only a B-08 embargo blocks it | WFW-007 | WFA-107 |
| `WFE-056` | N | `TRANSITION` begins after `FORTIFY` acceptance | `FORTIFY` resolves under `WAR-009g`; a new raid is refused `WRF-09` | WFW-032 | WFA-110 |
| `WFE-057` | O | A client hides the attack button but the API submits | The server validator decides; hiding is not enforcement | WFW-002 | WFA-113 |
| `WFE-058` | O | A captured request is replayed with a new key after a P2 failure | Treated as a new submission; it must pass every check; the old action is not revived | WFW-019, WFW-031 | WFA-114 |
| `WFE-059` | O | A forged acceptance is submitted on behalf of the counterparty | `WRF-01`; nothing changes | WFW-036 | WFA-115 |
| `WFE-060` | O | A request attempts to move OP to another nation or an Alliance pool | No such operation exists; rejected with no ledger item | WFW-019 | WFA-116 |

---

## 10. Failure catalogue

**10.1 Why this section exists.** B-10 §24.2 defines the closed set of failure codes. This section binds each code to the workflow that can emit it, the mutation it may and may not perform, and the acceptance test that proves it. **A workflow may not invent a code, reuse a code for a different meaning, or return a generic error where a code exists.**

**10.2 Identifier span and defined codes.** The closed span is `WRF-01`–`WRF-37`. **Thirty-two codes are defined**; `WRF-15`, `WRF-16`, `WRF-17`, `WRF-18` and `WRF-19` are **unallocated gaps** in the numbering and may not be used by any workflow, test or implementation. B-10 §29 line 12 refers to the span `WRF-01`–`WRF-37`; it does not assert that all thirty-seven numbers carry a definition. This document follows the definitions, not the span.

| Code | Stage | Meaning (B-10 §24.2) | Permitted mutation | Workflows | Tests |
|---|---|---|---|---|---|
| `WRF-01` | Submission | Actor is not the authenticated owner of the acting nation | None | WFW-002, WFW-018, WFW-036 | WFA-001, WFA-115 |
| `WRF-02` | Submission / P2 / P5 | Acting nation dormant, retired or inactive | None | WFW-002, WFW-005 | WFA-013, WFA-073 |
| `WRF-03` | Submission / P2 / P5 | Target invalid, self, dormant or retired | None | WFW-002 | WFA-014 |
| `WRF-04` | Submission / P2 / P5 | B-03 restricted pair | None | WFW-002 | WFA-015 |
| `WRF-05` | Submission / P2 / P5 | Newcomer protection active | Release every reservation at P2/P5; none at submission | WFW-002, WFW-031 | WFA-009, WFA-070 |
| `WRF-06` | Submission / P2 / P5 | National `DP-T01` NAP active | None | WFW-002 | WFA-010, WFA-100 |
| `WRF-07` | Submission / P2 / P5 | Same-Alliance ban | None; writes `AUD-AL-017` | WFW-002 | WFA-097 |
| `WRF-08` | Submission / P2 / P5 | Alliance `AT-E01` NAP covers the pair | None; writes `AUD-AL-017` | WFW-002 | WFA-098 |
| `WRF-09` | Submission / P2 / pre-P5 | `TRANSITION` or `CRISIS` blocks a new order, or the execution-time political state blocks an accepted offensive order | None at submission; release at P2/pre-P5; a qualifying accepted defensive commitment is exempt from row 8 only (`WAR-009g`) | WFW-002, WFW-032 | WFA-110 |
| `WRF-10` | Submission | No outgoing campaign slot | None | WFW-001 | WFA-011 |
| `WRF-11` | Submission | Insufficient OP (`available < cost`) | None | WFW-018 | WFA-035 |
| `WRF-12` | Submission | Insufficient unreserved crowns or resources | None | WFW-018, WFW-028 | WFA-035, WFA-109 |
| `WRF-13` | Submission | Duplicate idempotency key | None; original receipt returned | WFW-019 | WFA-081 |
| `WRF-14` | P5 | Declaration expired before resolution | Release reservations | WFW-006 | WFA-021 |
| `WRF-20` | P5 | Campaign expired | Release reservations | WFW-006 | WFA-022 |
| `WRF-21` | P2 / P5 | Campaign suspended by dormancy | Release reservations | WFW-005, WFW-031 | WFA-023, WFA-074 |
| `WRF-22` | P7 | Operation unresolved by P7 close | Release reservations; void; cannot replay | WFW-040 | WFA-085 |
| `WRF-23` | P2 / P5 | Readiness gate failed | Release reservations | WFW-018, WFW-031 | WFA-031 |
| `WRF-24` | Submission | Force cap or single-type share exceeded | None | WFW-028 | WFA-109 |
| `WRF-25` | Submission / P2 / P5 | Supply bundle or Food unavailable, including a released `OP-09` field ration | Release reservations | WFW-016, WFW-018, WFW-025 | WFA-036, WFA-037 |
| `WRF-26` | P2 / P5 | No `ACTIVE` campaign or stale target | Release reservations; never retarget | WFW-018, WFW-031 | WFA-025 |
| `WRF-27` | Submission | Blockade already active or in cooldown | None | WFW-010 | WFA-028, WFA-029 |
| `WRF-28` | Submission | Missile-strike tier or campaign limit exceeded | None | WFW-011, WFW-012 | WFA-026 |
| `WRF-29` | Submission | No active blockade to break | None | WFW-015 | WFA-069 |
| `WRF-30` | Submission | Readiness already at cap for a sustainment operation | None | WFW-016 | WFA-038 |
| `WRF-31` | Submission | Duplicate `FORTIFY` in the same P5 | None | WFW-014 | WFA-032 |
| `WRF-32` | Submission / P2 / P5 | Postwar exclusion active | None | WFW-001 | WFA-059 |
| `WRF-33` | P5 | Settlement reservation lost; atomic failure | Campaign returns to `ACTIVE`; zero transfer legs | WFW-039 | WFA-060, WFA-087 |
| `WRF-34` | P5 / P7 | Internal invariant violation; checkpoint held | No partial publication; operator path | WFW-027, WFW-040 | WFA-040, WFA-086 |
| `WRF-35` | pre-P5 | `RATION_SHORT`: a new offensive operation is blocked | Release reservations; defensive and sustainment operations still resolve | WFW-002, WFW-031 | WFA-034 |
| `WRF-36` | Submission / P2 / P5 | Invalid city target: not `OP-05`, city missing, or not owned by the target nation | Release reservations; the strike does not resolve | WFW-012 | WFA-027, WFA-030 |
| `WRF-37` | P4.1 | Invalid infrastructure repair: above 10 levels, above the damage, or above the 500 cap | Release reservations; no charge | WFW-030 | WFA-052 |

**10.3 Failure semantics binding on every row.** A failure is atomic: either the whole action is rejected with nothing reserved, or the action fails at P2/P5 with every reservation released exactly once. There is no partial acceptance, no partial reservation, no partial resolution and no debt. A failure never mutates `op_balance`; it only removes the `HELD` item and restores `available`. Every failure writes `WRA-02` (block), `WRA-03` (`OP_REJECTED`) or the specific event named in the row, and `WRF-07`/`WRF-08` additionally write `AUD-AL-017` with the exact B-09 field set. A retry after a failure is a new submission with a new action key; it must pass every check and is never a revival.

**10.4 Codes that are deliberately absent.** No code exists for espionage, sabotage, assassination, city capture, facility destruction, population casualty, territory, alliance command, OP transfer or debt. Their absence is a design decision (`B10-AD-24`, `B10-C30`, §1.7 item 3), not an omission; a workflow that appears to need one is mis-specified.

---

## 11. Concurrency, atomicity, idempotency, exploit prevention and security acceptance

**11.1 Concurrency and serialization.** Two requests may arrive for the same nation, the same target, the same campaign or the same turn boundary.

1. **Single-writer rule.** Within one `(nation_id, turn_id)`, actions are applied in a deterministic order. The submission order used for acceptance is the server receipt order; the P5 resolution order is the `WAR-115` order key `(campaign_priority, attacker_nation_id, operation_priority, submitted_at, action_id)`, never client-supplied order.
2. **Slot arbitrage.** Two simultaneous declarations for the same outgoing slot: exactly one is admitted; the other fails `WRF-10`. The decision is made under a lock on `(nation_id, slot, turn_id)` and is not reversible by retry.
3. **OP double-spend.** `HELD` items are written before the acceptance response. Two concurrent operations check `available = max(0, op_balance − reserved)` against the balance including all committed `HELD` items; the sum of live `HELD` items plus `consumed` may never exceed `op_balance` plus regenerations. Violation is `WRF-34`.
4. **Blockade and fortification state.** `OP-04` and `OP-07` mutate a per-nation or per-pair state that is read at acceptance and again at P5. A concurrent second `OP-04` on the same pair fails `WRF-27`; a second `OP-07` in the same P5 fails `WRF-31`.
5. **Settlement acceptance.** A settlement is completed once at P5.3. Two counterparty acceptances for the same proposal produce one completion; the second returns the original receipt and writes no second `WRA-12`.
6. **Turn boundary.** P3.7 and P5 are single-flight per turn. A concurrent duplicate boundary run returns the original receipt and performs no second mutation (`WAR-040`, `WAR-043`).

**11.2 Atomicity boundaries.** The following units are all-or-nothing and are the only permitted commit points:

| Unit | Commit point | On failure |
|---|---|---|
| Declaration acceptance | Submission while OPEN | Nothing reserved; `WRA-02` |
| Operation acceptance | Submission while OPEN | Nothing reserved; `WRA-03` `OP_REJECTED` |
| P2 revalidation | P2 | Every reservation released once; action failed |
| P3.6 civilian Food | P3.6 | `OP-09` actions released in reverse acceptance order with `WRF-25`; no partial release |
| P3.7 ration and upkeep | P3.7 | Whole obligation paid or cancelled; no debt |
| P3.7 OP regeneration | Opening of P3.7 | One `REGENERATED` item per `(nation_id, turn_id)`; zero is recorded at cap |
| P4.1 repair and construction | P4.1 | `WRF-37`; nothing charged |
| P5 resolution | P5 | Battle, losses, damage and progress commit together under `WRA-04` |
| P5.3 settlement | P5.3 | `WRF-33`; campaign returns `ACTIVE`; no transfer leg |
| P7 close | P7 | Void of unresolved actions, `reserved = 0` verified, then publication; `WRF-34` holds the checkpoint |

**11.3 Idempotency.** Every mutating request carries a client action key; every server resolution carries a key derived from `(turn_id, operation_id)` or `(turn_id, settlement_id)`.

1. A replayed submission with the same key returns the original receipt and writes nothing (`WRF-13` is the explicit duplicate signal where a new submission duplicates an existing intent; a true same-key replay is transparent and does not create a second item).
2. A replayed P5 battle reads the committed `APPLIED` battle and skips it; losses are not applied twice.
3. A replayed P3.7 boundary returns the original `REGENERATED` receipt.
4. A replayed P7 close re-verifies `reserved = 0` and does not republish.
5. Idempotency is server-side. A client that omits or forges a key cannot cause a second mutation; the server derives its own key and rejects a conflicting body under the same key with `WRF-34`.

**11.4 Exploit-prevention acceptance.** The following are explicit acceptance criteria, each with a test.

| # | Exploit | Required behaviour | Test |
|---|---|---|---|
| 1 | Slot filling or a shield war to deny a third nation | One outgoing and one incoming slot; no joining; no empty-war reward; blocked and empty wars audited | WFA-118 |
| 2 | Farming OP by declaring and voiding repeatedly | Declaration costs 2 OP and 500 crowns; a voided declaration does not refund the declaration cost unless the failure is server-caused; no `REGENERATED` on void; reroll block applies | WFA-119 |
| 3 | Double-click submit | One `HELD`, one action, one receipt | WFA-082 |
| 4 | Client-side hiding of a forbidden action | Server validator decides; UI state is not enforcement | WFA-113 |
| 5 | Replay after a P2 failure with a new key | New submission; every check reruns; the old action is dead | WFA-114 |
| 6 | Forged acceptance, forged surrender or forged settlement response | `WRF-01`; nothing changes | WFA-115 |
| 7 | Request tampering with cost, target or tier | Server recomputes cost, revalidates target and re-derives tier; client values are display only | WFA-117 |
| 8 | Alliance peer pressure or delegated authority | No command, no delegated order, no shared OP, no inference from silence | WFA-102, WFA-104 |
| 9 | Reading a rival's exact strength before P5 | Only a band may be returned; exact values appear after `WRA-04` | WFA-044, WFA-089 |
| 10 | Empty-war or no-op resolution to farm objective progress | Progress only from a resolved battle or a resolved sustainment operation under the objective's stated source | WFA-119 |
| 11 | Negative or fractional OP, strength or resource | Integer domain enforced; negative strength is `WRF-34`; no fractional OP or resource exists | WFA-040 |

**11.5 Security acceptance (design level).**

1. **Authenticated ownership.** Every request is authorized against the session's active nation. A body-supplied `nation_id` is advisory at most; mismatch is `WRF-01`.
2. **Server authority.** Target validity, cost, readiness, supply, protection, NAP, Alliance and political checks are re-evaluated server-side at submission, P2 and immediately before P5. No client flag, hidden field or cached value can waive a check.
3. **Fail-closed.** An unavailable dependency (B-03, B-04, B-08, B-09 state, seed service) fails the action closed rather than admitting it.
4. **Least disclosure.** Responses and events disclose only the fields in §12.2. Exact readiness, exact force, exact inventory, private treaty text and another nation's reservations are never returned.
5. **Audit integrity.** Audit events are append-only. An administrator may record a reversal; an administrator may not edit a committed battle, loss, damage or transfer in place.
6. **No secret learning.** A failure response states the code and the rule but never reveals a hidden value (exact enemy strength, another nation's OP balance, another nation's Food stock).
7. **Replay resistance.** Action keys are scoped to nation and turn; a captured key from one nation cannot be used by another.

---

## 12. Notifications, visibility and confirmation content

**12.1 Notification catalogue.** Notifications are derived from the fourteen `WRA-` events plus the boundary outcomes. Each notification names the nation, the campaign, the turn, the event and the next legal action; it never contains a hidden value.

| Notification | Trigger | Recipients | Content floor | Must not contain |
|---|---|---|---|---|
| Declaration received | `WRA-01` | Target owner | Declarer, objectives, turn, that a response window is open | Declarer's OP balance or force |
| Declaration blocked | `WRA-02` | Actor | Failing check and code; for B-09 blocks, the counterparty and rule | Private treaty text |
| Operation accepted | `WRA-03` | Actor | Operation, target, cost, reservation reference | Enemy strength |
| Operation failed | `WRA-03` `OP_REJECTED` or action failure | Actor | Code, rule, that every reservation was released | Hidden state that caused a check to fail where disclosure is restricted |
| Battle report | `WRA-04` | Both belligerents | Powers, ratio, fortune, tier, losses, progress | Third-party identity in a privacy-coarsened statistic |
| Campaign state change | `WRA-05` | Both belligerents | Prior and new state, turn, reason | — |
| Objective progress | `WRA-06` | Both belligerents | Side, objective, delta, total, source | — |
| State applied or removed | `WRA-07` | Owner and affected pair | State, source, expiry | — |
| Strategic strike | `WRA-08` | Both belligerents | City identity, infrastructure before/after, removed levels | Exact book value, exact force |
| Interception | `WRA-09` | Defender and attacker | Result and the triggering attack | — |
| Fortification | `WRA-10` | Owner | State and expiry | — |
| Resupply | `WRA-11` | Owner | OP and resources consumed, readiness before/after | — |
| Settlement | `WRA-12` | Parties | Terms, state, transfer reference | Private text of an `AT-E00` |
| Campaign ended | `WRA-13` | Both belligerents and the public record | Outcome, victor, progress, turn, reason | — |
| Reservation audit | `WRA-14` | Owner; administration on request | Action key, OP, resources, state, turn | — |

**12.2 Visibility matrix.** The rows are the audiences; the columns are the data classes. `P` = public, `O` = owner only, `B` = both belligerents, `A` = administration only, `—` = never disclosed.

| Data | Public | Owner | Opponent | Alliance | Admin |
|---|---|---|---|---|---|
| Campaign existence, states, outcome | P | O | B | — | A |
| Objectives and progress totals | P | O | B | — | A |
| Battle report (powers, tier, losses) | after `WRA-04` | O | B | — | A |
| Exact readiness | band only | O | band only | — | A |
| Exact force and inventory | — | O | — | — | A (fair play) |
| OP balance and reservations | — | O | — | — | A (fair play) |
| Food stock and military demand | — | O | band only | — | A |
| City infrastructure | P | O | P | — | A |
| Exact book value and facility detail | — | O | — | — | A |
| Settlement terms | P when completed | O | B | — | A |
| `AT-E00` private text | — | parties | parties | — | A |
| `AUD-AL-017` block record | — | actor sees rule and counterparty | — | — | A |

**12.3 Confirmation requirements.** A destructive or irreversible military action requires an explicit confirmation that names the action, the target, the cost and the consequence. Confirmation is required for: a declaration (2 OP, 500 crowns, one outgoing slot, a public record); every offensive operation (OP cost, supply bundle, readiness effect); `OP-05` city target (city identity and that only infrastructure may be reduced); `OP-07` and `OP-09` (OP and resource cost); a settlement acceptance (each term and its duration); a surrender (campaign ends, terms apply); a disbanding order (strength removed). Confirmation is never pre-checked, never remembered across turns and never inferred from a previous acceptance. A confirmation dialog is a client presentation of a server-validated intent; the server revalidates on receipt.

**12.4 Prohibited communication.** No notification, confirmation, battle report or public statistic may: disclose another nation's exact military state; identify fewer than five nations in a published aggregate (D-027); reveal an `AT-E00`'s private text to an Alliance; suggest that an Alliance, office, AI or administrator has authority over a nation's military decision; or present a provisional value as calibrated.

---

## 13. Acceptance matrix

**13.1 How to read a test.** Every `WFA-` record is a **test design**, not a passed test. Each of the 124 records is written as two linked tables that share the same `WFA-` identifier:

1. **Identification table** — `ID`, `Test name`, `Class`, `Requirement`, `Workflow`, `Edge case`, `Rules`, `Formula`, `Definition`, `Execution`.
2. **Behaviour table** — `ID`, `Initial state`, `Input`, `Phase`, `Expected validation (ordered)`, `Expected output`, `Expected mutation`, `Expected no-mutation`, `Ledger`, `Audit`, `Failure code`, `Privacy`, `Evidence`.

Together the two tables carry the complete 22-field record schema: test ID, test name, test class, requirement, workflow, edge case, rules (including lettered sub-rules), formula, initial state, input, execution phase, expected validation (ordered), expected output, expected mutation, expected no-mutation, ledger, audit, privacy, evidence, definition status and execution status. The identifier joins the tables; a record is incomplete unless both rows exist and every cell is populated.

**13.1.1 Definition status versus execution status.** `Definition` states whether the design is complete — every mandatory field written, every reference resolvable, every expected result observable. `Execution` states whether the test has actually run against an implementation. In this version **every record is `Definition: COMPLETE` and `Execution: NOT RUN`**. No warfare implementation exists, so no `WFA-` record is `PASS` or `FAIL`; `BLOCKED` and `NOT RUN` are the only honest execution values and `NOT RUN` is used throughout. A `COMPLETE` definition is a specification achievement, not a test result.

**13.1.2 Value conventions.**

- **Formula** names the register formula the test exercises, or states `N/A — reason` where the behaviour is a check set, a state rule or an integrity constraint rather than arithmetic.
- **Ledger** records the OP lifecycle state the test observes: `none`, `HELD`, `CONSUMED`, `RELEASED`, or an arrowed transition such as `HELD → CONSUMED`.
- **Audit** names the `WRA-` event the test expects, or states `none — reason` where the action is rejected before an event is written.
- **Failure code** names the `WRF-` code the test expects, or states `N/A — reason` where no failure code exists for a lawful outcome or a structural refusal.
- **Privacy** names the audience that may observe the result: `actor`, `defender`, `actor + defender`, `Alliance`, `public`, `moderators`, or a combination.
- **Evidence** names the artefacts that make the record checkable: the edge case, the workflow and the governing section.

**13.1.3 Phase vocabulary.** `Phase` is one of `OPEN`, `P2`, `P3.7`, `P4.1`, `P5`, `P7`. Where a test observes a whole turn, the phase named is the commit point under test and the ordered validation names the other phases visited.

**13.2 The sixteen classes.** Classes A–O hold eight tests each, `WFA-001`–`WFA-120`; class P holds four supplementary coverage tests, `WFA-121`–`WFA-124` (§13.18).

| Class | Name | Tests | Covers |
|---|---|---|---|
| A | Authority, identity and sovereignty | WFA-001–008 | `WAR-001`–`WAR-008`, `WAR-151` |
| B | Declaration eligibility and protection | WFA-009–016 | `WAR-002`–`WAR-014`, B-03/B-08/B-09 blocks |
| C | Campaign states, deadlines and termination | WFA-017–024 | §6 states, deadlines, dormancy, outcomes |
| D | Operation eligibility, targeting and slots | WFA-025–032 | `WAR-045`–`WAR-046`, operation catalogue, city target |
| E | Economy, OP ledger, Food and supply | WFA-033–040 | `WAR-040`–`WAR-043b`, `WAR-053a`–`m`, `WAR-069` |
| F | Battle resolution and determinism | WFA-041–048 | §14, `F-WR-019`–`F-WR-030` |
| G | Losses, damage, repair and caps | WFA-049–056 | §16, `WAR-109a`–`WAR-109m`, `WAR-111`–`WAR-114` |
| H | Peace, settlement and surrender | WFA-057–064 | §19–§22, `WAR-125`–`WAR-141` |
| I | Protection, counters and persistent states | WFA-065–072 | §12, §18, `WAR-094`–`WAR-100` |
| J | Dormancy, reroll and account lifecycle | WFA-073–080 | `WAR-021`–`WAR-024`, `WAR-028`–`WAR-031`, `UD-032` |
| K | Idempotency, atomicity, recovery and concurrency | WFA-081–088 | §11, `WAR-040`, `WAR-043`, `WAR-143`–`WAR-147` |
| L | Visibility, privacy and audit access | WFA-089–096 | §23–§24, D-027, `WAR-148`–`WAR-155` |
| M | Alliance, NAP and diplomacy boundaries | WFA-097–104 | `WAR-010`–`WAR-012`, B-08, B-09 |
| N | Cross-system integration B-02–B-09 | WFA-105–112 | §25 contract matrix |
| O | Security, abuse resistance and final acceptance | WFA-113–120 | §11.4–§11.5, §17 |
| P | Supplementary operation and lifecycle coverage | WFA-121–124 | WFW-008, WFW-009, WFW-017, WFW-029 |

### 13.3 Class A — authority, identity and sovereignty

**13.3.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-001` | Body-supplied nation identity is rejected | A | REQ-654, REQ-678 | WFW-001, WFW-002 | WFE-001 | `WAR-001`, `WAR-009d`, `WRF-01` | N/A — the twelve-check validator is a cumulative check set, not arithmetic | COMPLETE | NOT RUN |
| `WFA-002` | Alliance officer cannot operate for a member | A | REQ-691 | WFW-007, WFW-018 | WFE-002 | `WAR-001`, `WAR-151` | N/A — authority resolution is not a formula | COMPLETE | NOT RUN |
| `WFA-003` | Committed battle cannot be edited in place | A | REQ-692 | WFW-020, WFW-040 | WFE-003 | `WAR-151`, `WAR-155` | N/A — append-only integrity rule, no calculation | COMPLETE | NOT RUN |
| `WFA-004` | Concurrent declarations claim one outgoing slot | A | REQ-678 | WFW-001, WFW-019 | WFE-004 | `WAR-005`, `WAR-007`, `WRF-10` | `F-WR-006` | COMPLETE | NOT RUN |
| `WFA-005` | Silence never accepts a settlement | A | REQ-690 | WFW-036 | WFE-030 | `WAR-151`, `WAR-138` | `F-WR-030` | COMPLETE | NOT RUN |
| `WFA-006` | Office, treaty, ballot and administrator confer no military authority | A | REQ-691 | WFW-001 | — (authority matrix §2.1) | `WAR-001`, `WAR-151` | N/A — authority resolution is not a formula | COMPLETE | NOT RUN |
| `WFA-007` | Declaration confirmation is complete and non-defaulted | A | REQ-678 | WFW-001 | — (confirmation floor §12.3) | `WAR-005`, `WAR-006` | `F-WR-004`, `F-WR-019` | COMPLETE | NOT RUN |
| `WFA-008` | Withdrawal before P1 releases every reservation once | A | REQ-678 | WFW-003 | — (withdrawal window WFW-003) | `WAR-003`, `WAR-005` | `F-WR-002` | COMPLETE | NOT RUN |

**13.3.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-001` | Session owned by N1; both nations active; body names N2 | Submit a declaration with `nation_id = N2` | OPEN | 1 resolve the authenticated nation N1; 2 compare it with the body field; 3 fail closed at the ownership row; 4 execute nothing | `WRF-01` naming the ownership rule; no declaration record; the attempt is visible to moderators under N1 | None | No declaration, no OP movement, no record in N2's name, no crown reservation | none — rejected before reservation | none — rejection precedes `WRA-01`; moderators see the attempt | `WRF-01` | actor; moderators | WFE-001; WFW-001/002; §2.1.1, §10.2 |
| `WFA-002` | N1 and N2 in one active Alliance; session owned by N1; N2 idle | N1 submits an operation whose actor field names N2 | OPEN | 1 authenticate N1; 2 ownership resolves to N1 only; 3 reject the foreign actor; 4 no Alliance channel is consulted | Refused; `WRF-01`; no OP or resource moves | None | No delegated order, no Alliance command, no implicit consent, no record under N2 | none — rejected at submission | none — no `WRA-03` is written for a rejected actor | `WRF-01` | actor; the Alliance learns nothing of N2's military state | WFE-002; WFW-007/018; §2.1, §12.2 |
| `WFA-003` | A `WRA-04` battle record is committed; administrator session | Attempt an in-place edit of losses, tier or damage | P5 | 1 resolve the actor as administration; 2 find no in-place mutation path; 3 require a recorded reversal instead; 4 re-read the original digest | Rejected; only a recorded reversal is permitted; the original record is intact | None | No silent rewrite of losses, tier or damage; no deletion | none — an administrative edit is refused before any ledger entry | `WRA-04` remains unchanged; any reversal would be a new event | N/A — no `WRF-` code exists for an administrative edit; the refusal is structural (`WAR-155`) | moderators; both belligerents keep the unchanged report | WFE-003; WFW-020/040; §11.5 item 5, §12.2 |
| `WFA-004` | N1 has one free outgoing slot; two sessions; enough OP and crowns for one declaration | Submit the same intent with different action keys concurrently | OPEN | 1 both requests pass the twelve checks on live state; 2 lock `(nation_id, slot, turn_id)`; 3 the first writes `ACCEPTED` and `HELD`; 4 the second re-reads occupancy and fails the slot row | Exactly one declaration admitted; the second fails `WRF-10`; one `WRA-01` | One declaration `ACCEPTED`; 2 OP `HELD`; 500 crowns reserved; one slot occupied | No two declarations, no slot duplication, no second reservation | `HELD` ×1 (2 OP) | `WRA-01` ×1 | `WRF-10` | actor; the target is notified of the admitted declaration only | WFE-004; WFW-001/019; §11.1 item 2, §11.2 |
| `WFA-005` | Settlement `PROPOSED`; counterparty silent | Advance 12 turns without a response | P5 | 1 increment the window once per turn; 2 find no response event; 3 expire the proposal at the twelfth turn; 4 apply no term | `EXPIRED`; no terms applied; no transfer | Proposal state `PROPOSED → EXPIRED` | No acceptance by silence, no inferred consent, no transfer | none — no reservation is consumed by an expired proposal | `WRA-12` (state change to `EXPIRED`) | N/A — expiry is a lawful outcome, not a failure | actor + defender | WFE-030; WFW-036; §7.5, §12.1 |
| `WFA-006` | Any non-owner actor: office, AI, treaty counterparty, ballot majority or administrator | Attempt to declare for N1 through every surface | OPEN | 1 resolve the principal; 2 confirm no enumerated role maps to `owner(N1)`; 3 reject each variant; 4 execute nothing | Refused; nothing mutates | None | No authority derived from office, treaty, majority or administration | none — no authority exists, so no value movement | none — rejection at submission; moderators see the attempt | `WRF-01` | actor; moderators | §2.1, §11.5 item 1; WFW-001 |
| `WFA-007` | N1 active, free outgoing slot, sufficient OP and crowns | Open the declaration confirmation | OPEN | 1 run the twelve checks; 2 render target, primary and secondary objective, 2 OP, 500 crowns, slot and public-record notice; 3 leave every control unset; 4 accept only an explicit confirmation | Confirmation naming every required item before commit | None until confirmation | No submission before explicit confirmation; no pre-checked box; no remembered consent | none at confirmation | none at confirmation | N/A — a confirmation view has no failure code | actor | §12.3; WFW-001; REQ-675 content floor |
| `WFA-008` | Declaration `DECLARED_PENDING` before P1 freeze | Owner withdraws | OPEN | 1 authenticate the owner; 2 confirm the state precedes P1; 3 release each `HELD` item exactly once; 4 never activate | Withdrawn; reservations released; no campaign activates | State `DECLARED_PENDING → WITHDRAWN`; 2 OP `RELEASED`; crowns released | No withdrawal after P1 freeze, no double release, no `WRA-05` activation | `HELD → RELEASED` once | `WRA-05` (state change) | N/A — a lawful owner withdrawal has no failure code | actor; the target is notified of the withdrawal | WFW-003; §4.1, §6 |

### 13.4 Class B — declaration eligibility and protection

**13.4.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-009` | Newcomer protection activating before P2 voids the declaration | B | REQ-658, REQ-687 | WFW-002, WFW-031 | WFE-005 | `WAR-003`, `WAR-009`, `WAR-116`, `WRF-05` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-010` | National NAP signed before P2 blocks activation | B | REQ-668 | WFW-002, WFW-031 | WFE-006 | `WAR-010`, `WRF-06` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-011` | Incoming campaign consumes no outgoing slot | B | REQ-678 | WFW-001 | WFE-007 | `WAR-002`, `WAR-007`, `WRF-10` | `F-WR-006` | COMPLETE | NOT RUN |
| `WFA-012` | Identical primary and secondary objectives are rejected as input | B | REQ-679 | WFW-001 | WFE-008 | `WAR-006` | N/A — the objective set is a closed enumeration | COMPLETE | NOT RUN |
| `WFA-013` | Dormant declarer cannot declare | B | REQ-659 | WFW-002 | — (dormancy boundary §4.7) | `WAR-002`, `WRF-02` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-014` | Invalid, self, missing or dormant target is rejected | B | REQ-678 | WFW-002 | — (target variants §2.1.1) | `WAR-003`, `WRF-03` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-015` | Restricted pair cannot be bypassed through a third party | B | REQ-658 | WFW-002 | — (B-03 restricted pairs) | `WAR-003`, B-03 `NET-025`/`NET-026`, `WRF-04` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-016` | Twelve checks in order admit and charge a declaration | B | REQ-678 | WFW-001 | — (happy path §2.4) | `WAR-009` checks 1–12, `WAR-005`, `WRA-01` | `F-WR-004`, `F-WR-019` | COMPLETE | NOT RUN |

**13.4.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-009` | A valid declaration is accepted; the target gains newcomer protection before P2 | Run P2 | P2 | 1 load the frozen baseline; 2 run the twelve checks; 3 the protection row fails; 4 release every reservation; 5 void the campaign | `WRF-05`; every reservation released; campaign `VOID`; `WRA-02` | Declaration `ACCEPTED → VOID`; 2 OP `RELEASED`; crowns released | No battle, no OP consumption, no activation | `HELD → RELEASED` once | `WRA-02`; `WRA-05` (state `VOID`) | `WRF-05` | actor + defender | WFE-005; WFW-002/031; §2.5, §10.2 |
| `WFA-010` | Declaration accepted; the target signs `DP-T01` before P2 | Run P2 | P2 | 1 load the frozen baseline; 2 run the twelve checks; 3 the national-NAP row fails; 4 release; 5 never activate | `WRF-06`; the war never activates; reservations released | Declaration `ACCEPTED → VOID`; `HELD → RELEASED` | No activation, no campaign record as fought | `HELD → RELEASED` once | `WRA-02`; `WRA-05` | `WRF-06` | actor + defender | WFE-006; WFW-002/031; §10.2, §12.1 |
| `WFA-011` | N1 has an incoming campaign and no outgoing slot | Submit a declaration | OPEN | 1 run the twelve checks; 2 confirm the slots are separate; 3 read outgoing occupancy; 4 fail the slot row | `WRF-10`; nothing reserved | None | No queueing, no joining the incoming campaign | none — rejected before reservation | none — rejection at submission | `WRF-10` | actor | WFE-007; WFW-001; §4.1, §10.2 |
| `WFA-012` | Primary and secondary objectives name the same identifier | Submit | OPEN | 1 parse the objective pair; 2 require two distinct closed identifiers; 3 reject before the validator; 4 write no record | Rejected as invalid input before the validator; no record | None | No silent substitution of a secondary objective | none — rejected before any OP or crown is reserved | none — malformed input never reaches `WRA-01` | N/A — malformed input is rejected before a `WRF-` code exists | actor | WFE-008; WFW-001; §2.2, §10.4 |
| `WFA-013` | The declarer is dormant at submission | Submit | OPEN | 1 resolve the actor; 2 read dormancy; 3 fail closed; 4 execute nothing | `WRF-02`; nothing reserved | None | No dormant declaration, no reservation | none — rejected before any OP or crown is reserved | none — rejection at submission | `WRF-02` | actor | WFW-002; §4.7, §10.2 |
| `WFA-014` | The target is self, missing, retired or dormant, tested as four variants | Submit each variant | OPEN | 1 resolve the target; 2 reject the self, missing, retired and dormant variants; 3 execute nothing | `WRF-03` for each variant; nothing reserved | None | No self-declaration, no declaration on a dormant nation | none — rejected before any OP or crown is reserved | none — rejection at submission | `WRF-03` | actor | WFW-002; §2.1.1, §10.2 |
| `WFA-015` | The declarer and target form a B-03 restricted pair | Submit directly and through an intermediary variant | OPEN | 1 resolve the real actor and target; 2 run the B-03 pair check; 3 reject; 4 refuse any third-party substitution | `WRF-04`; nothing reserved | None | No restricted-pair bypass through a third party | none — rejected before any OP or crown is reserved | none — rejection at submission | `WRF-04` | actor | WFW-002; §10.2; B-03 `NET-025`/`NET-026` |
| `WFA-016` | All twelve declaration checks pass | Submit and resolve at P5 | P5 | 1 submission run passes rows 1–12 in order; 2 check the idempotency key; 3 recompute the cost server-side; 4 freeze at P1; 5 revalidate at P2; 6 activate at P5.1 | `DECLARED_PENDING → ACTIVE`; 2 OP and 500 crowns consumed; `WRA-01`; target notified | Declaration `ACCEPTED → ACTIVE`; `HELD → CONSUMED` at P5.1; crowns consumed | No check skipped, no cost waived, no second charge | `HELD → CONSUMED` | `WRA-01`; `WRA-05` | N/A — the positive path has no failure code | actor + defender; the declaration is a public record | WFW-001; §2.4 steps 6–18; §10.2 |

### 13.5 Class C — campaign states, deadlines and termination

**13.5.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-017` | Primary completion outranks deadline expiry | C | REQ-680 | WFW-006 | WFE-009 | `WAR-019`, `WAR-025` | `F-WR-007`, `F-WR-010` | COMPLETE | NOT RUN |
| `WFA-018` | Settlement accepted on the deadline turn completes before expiry | C | REQ-690 | WFW-038, WFW-006 | WFE-010 | `WAR-019`, `WAR-125` | `F-WR-030` | COMPLETE | NOT RUN |
| `WFA-019` | A resolved raid clears stalemate | C | REQ-680 | WFW-006 | WFE-011 | `WAR-026` | `F-WR-008` | COMPLETE | NOT RUN |
| `WFA-020` | P5.1 activates a declaration and records the state change | C | REQ-680 | WFW-004 | — (activation ordering §2.4) | `WAR-016`, `WAR-017`, `WRA-05` | `F-WR-007` | COMPLETE | NOT RUN |
| `WFA-021` | An expired declaration charges no cost | C | REQ-680 | WFW-006 | — (declaration expiry) | `WAR-018`, `WRF-14` | `F-WR-007` | COMPLETE | NOT RUN |
| `WFA-022` | Deadline releases every pending operation | C | REQ-680 | WFW-006 | — (deadline with pending operations) | `WAR-019`, `WRF-20` | `F-WR-007` | COMPLETE | NOT RUN |
| `WFA-023` | Dormancy suspends and fails a pending declaration | C | REQ-659 | WFW-005 | WFE-037 | `WAR-021`, `WAR-022`, `WRF-21` | `F-WR-008` | COMPLETE | NOT RUN |
| `WFA-024` | Forty-eight suspended turns abandon the campaign | C | REQ-680 | WFW-006 | WFE-039 | `WAR-023`, `WAR-024` | `F-WR-008` | COMPLETE | NOT RUN |

**13.5.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-017` | Primary completion and the campaign deadline fall on the same turn | Run P6 | P5 | 1 P5.4 resolves every accepted action; 2 P6 evaluates primary completion before expiry; 3 record the victory and no expiry | `LIMITED_VICTORY` or `DECISIVE_VICTORY`, never `EXPIRY` | Campaign `ACTIVE → ENDED` with a victory outcome | No expiry beating a completed primary objective | none — no reservation is live at P6 | `WRA-05`; `WRA-13` | N/A — a lawful victory is not a failure | public outcome; actor + defender | WFE-009; WFW-006; §4.1, §7.7 |
| `WFA-018` | A settlement is accepted on the deadline turn | Run P5.3 then P5.4 | P5 | 1 P5.3 completes the settlement atomically; 2 P5.4 finds no live campaign to expire; 3 end the campaign once | Settlement completes; no expiry | Settlement `ACCEPTED → COMPLETED`; terms applied; campaign ended | No expiry of a completed settlement, no second outcome | none — settlement state changes without a value transfer | `WRA-12`; `WRA-13` | N/A — a lawful completion is not a failure | actor + defender; terms public when completed | WFE-010; WFW-038/006; §2.4 steps 20–21, §7.5 |
| `WFA-019` | Twenty-four stale turns are recorded, then a raid resolves | Resolve the raid and run P6 | P5 | 1 read the inactivity counter at 24; 2 a resolved operation resets the stale count; 3 no expiry is evaluated at 48 | `STALEMATE` clears; no expiry at 48 | Inactivity counter reset; campaign remains `ACTIVE` | No stale counter that ignores a resolved operation | none — inactivity reset changes no ledger balance | none — no state change occurs; the counter reset is a turn-ledger entry | N/A — a lawful reset is not a failure | actor + defender | WFE-011; WFW-006; §4.1, §7.7 |
| `WFA-020` | A declaration survives P2 | Run P5.1 | P5 | 1 order declarations by `(submitted_at, action_id)`; 2 activate; 3 write prior and new state; 4 consume the declaration cost | `DECLARED_PENDING → ACTIVE`; `WRA-05` with prior and new state | Campaign state changed; 2 OP and 500 crowns consumed | No activation without the P5.1 step, no second charge | `HELD → CONSUMED` | `WRA-05` | N/A — the positive activation path has no failure code | actor + defender; state is public | WFW-004; §2.4 step 18, §6 |
| `WFA-021` | A declaration expires before resolution | Run P5 | P5 | 1 compare the deadline with the current turn; 2 the declaration is not activated; 3 fail `WRF-14`; 4 release | `WRF-14`; reservations released; no campaign | Declaration `EXPIRED`; `HELD → RELEASED` | No cost charged for an expired declaration | `HELD → RELEASED` once | `WRA-02`; `WRA-05` | `WRF-14` | actor | WFW-006; §10.2 |
| `WFA-022` | An `ACTIVE` campaign reaches its deadline with pending operations | Run P5.4 | P5 | 1 detect the deadline; 2 fail each pending operation; 3 release each exactly once; 4 compute the expiry outcome at P6 | `WRF-20` for each pending operation; reservations released; expiry outcome at P6 | Each operation `FAILED`; `HELD → RELEASED`; campaign ended with expiry | No late offensive resolution, no charge | `HELD → RELEASED` once per operation | `WRA-02`; `WRA-13` | `WRF-20` | actor + defender | WFW-006; §2.4 steps 19 and 21 |
| `WFA-023` | The declarer is dormant at P0 with a pending declaration | Run P0–P2 | P2 | 1 detect dormancy; 2 suspend the campaign; 3 fail the pending declaration; 4 release every reservation | `SUSPENDED`; declaration fails `WRF-21`; everything released | Campaign `ACTIVE → SUSPENDED`; declaration `FAILED`; `HELD → RELEASED` | No campaign progress while dormant | `HELD → RELEASED` once | `WRA-05`; `WRA-02` | `WRF-21` | actor + defender | WFE-037; WFW-005; §4.1, §4.7 |
| `WFA-024` | Both sides are dormant for 48 suspended turns | Advance the suspension counter | P5 | 1 confirm both sides dormant; 2 the counter reaches 48; 3 abandon with `DRAW`; 4 apply no reparations | `ABANDONED` with `DRAW`; no reparations; `WRA-13` | Campaign `SUSPENDED → ABANDONED`; outcome `DRAW` | No reparations, no victor, no silent reset | none — abandonment records no reparation or transfer | `WRA-13`; `WRA-05` | N/A — abandonment is a terminal outcome, not a failure | public outcome; actor + defender | WFE-039; WFW-006; §4.1, §7.7 |

### 13.6 Class D — operation eligibility, targeting and slots

**13.6.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-025` | Offensive outside an active campaign is refused | D | REQ-684 | WFW-011 | — (campaign prerequisite §5.2) | `WAR-045`, `WAR-046`, `WRF-26` | N/A — eligibility is a state check | COMPLETE | NOT RUN |
| `WFA-026` | Missile strike resolves within tier and campaign limit | D | REQ-699 | WFW-011, WFW-012 | — (valid national strike §7.1) | `WAR-109a`–`WAR-109c`, `WRF-28` | `F-WR-021`, `F-WR-037` | COMPLETE | NOT RUN |
| `WFA-027` | Only `OP-05` may name a city | D | REQ-699 | WFW-012 | — (non-`OP-05` city target) | `WAR-109l`, `WRF-36` | N/A — target validity check | COMPLETE | NOT RUN |
| `WFA-028` | Missing or foreign city is rejected after national checks | D | REQ-699 | WFW-012 | — (city missing or foreign) | `WAR-109l`, `WRF-36` | N/A — target validity check | COMPLETE | NOT RUN |
| `WFA-029` | A second blockade on the same pair is refused | D | REQ-686 | WFW-010 | WFE-014 | `WAR-083`, `WRF-27` | `F-WR-018` | COMPLETE | NOT RUN |
| `WFA-030` | Third-party city cannot proxy a national target | D | REQ-699 | WFW-012 | WFE-013 | `WAR-109b`, `WRF-36` | N/A — target validity check | COMPLETE | NOT RUN |
| `WFA-031` | Readiness gate blocks an operation | D | REQ-682 | WFW-018, WFW-031 | — (readiness gate §4.5) | `WAR-048`, `WRF-23` | `F-WR-005` | COMPLETE | NOT RUN |
| `WFA-032` | A second fortification in one P5 is refused | D | REQ-688 | WFW-014 | WFE-015 | `WAR-100`, `WRF-31` | `F-WR-026` | COMPLETE | NOT RUN |

**13.6.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-025` | No `ACTIVE` campaign exists with the target | Submit `OP-05` nation target | P2 | 1 resolve the campaign from the operation; 2 find no `ACTIVE` campaign; 3 fail the campaign row; 4 never retarget | `WRF-26`; nothing reserved | None | No attack outside a campaign, no retarget | none — rejected before any OP or resource is reserved | `WRA-02` | `WRF-26` | actor | WFW-011; §10.2 |
| `WFA-026` | An active campaign exists; tier and campaign strike limit are measured | Submit a valid `OP-05` against a nation | P5 | 1 run the national checks; 2 verify the missile tier; 3 verify the per-campaign strike limit; 4 accept; 5 resolve at P5 with the strike-power formula | Accepted; strike power computed; the city target is optional | Operation `ACCEPTED → RESOLVED`; `HELD → CONSUMED`; supply consumed; infrastructure damage applied | No tier bypass, no strike beyond the campaign limit | `HELD → CONSUMED` | `WRA-03`; `WRA-08` | N/A — the in-limit positive path has no failure code | actor + defender; city infrastructure is public | WFW-011/012; §7.1, §7.4 |
| `WFA-027` | A non-`OP-05` operation names a city | Submit | OPEN | 1 identify the operation; 2 only `OP-05` may carry a city; 3 fail the city-target row; 4 write no damage | `WRF-36`; nothing reserved; no city damage | None | No city targeting by raid, assault or air strike | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-36` | actor | WFW-012; §10.2, §12.2 |
| `WFA-028` | The city does not exist or belongs to another nation | Submit `OP-05` | OPEN | 1 run every national check first; 2 resolve city ownership; 3 fail the city row; 4 refuse substitution | `WRF-36`; the national checks are not waived | None | No target substitution, no damage to a third nation's city | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-36` | actor | WFW-012; §2.3.3, §10.2 |
| `WFA-029` | A blockade by either side is active on the pair | Submit `OP-04` | OPEN | 1 read the pair state; 2 find an active blockade; 3 fail the state row; 4 apply no second modifier | `WRF-27`; nothing reserved | None | No stacked blockade, no second surcharge | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-27` | actor | WFE-014; WFW-010; §10.2, §11.1 item 4 |
| `WFA-030` | An `OP-05` city target belongs to a third nation | Submit | OPEN | 1 run the full national check set; 2 resolve city ownership last; 3 fail the city row; 4 refuse the proxy | `WRF-36`; the full national check set still runs first | None | No third-party city as a proxy target | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-36` | actor | WFE-013; WFW-012; §2.3.3, §10.2 |
| `WFA-031` | Readiness is below the operation's gate | Submit | P2 | 1 read readiness at the validation point; 2 compare it with the operation gate; 3 fail; 4 release | `WRF-23`; nothing reserved | None | No operation at a failed readiness gate | none — rejected before any OP or resource is reserved | `WRA-02` | `WRF-23` | actor | WFW-018/031; §4.5, §10.2 |
| `WFA-032` | One `OP-07` is already accepted for the same P5 | Submit a second `OP-07` | OPEN | 1 read the per-nation P5 state; 2 find the fortification; 3 fail the duplicate row; 4 apply no second bonus | `WRF-31`; no stacking | None | No double fortification bonus | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-31` | actor | WFE-015; WFW-014; §10.2, §11.1 item 4 |

### 13.7 Class E — economy, OP ledger, Food and supply

**13.7.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-033` | Combined denial and blockade surcharge is capped and applied once | E | REQ-686 | WFW-007, WFW-010 | WFE-017 | `WAR-068`, `F-WR-039` | `F-WR-016`, `F-WR-017`, `F-WR-018`, `F-WR-039` | COMPLETE | NOT RUN |
| `WFA-034` | Whole ration obligation cancels and readiness drops 100 | E | REQ-696 | WFW-025 | WFE-018 | `WAR-053d`, `WAR-053e`, `WRF-35` | `F-WR-036` | COMPLETE | NOT RUN |
| `WFA-035` | Insufficient OP or crowns is refused at submission | E | REQ-681 | WFW-018 | — (cost insufficiency §11.1) | `WAR-041`, `WAR-042`, `WRF-11`, `WRF-12` | `F-WR-001`, `F-WR-019` | COMPLETE | NOT RUN |
| `WFA-036` | `OP-09` surplus shortfall is refused atomically | E | REQ-697 | WFW-016 | WFE-019 | `WAR-053l`, `WRF-25` | `F-WR-036` | COMPLETE | NOT RUN |
| `WFA-037` | P3.6 releases two `OP-09` reservations in reverse order | E | REQ-697 | WFW-016, WFW-025 | WFE-020 | `WAR-053l`, `WRF-25` | `F-WR-036` | COMPLETE | NOT RUN |
| `WFA-038` | Resupply at readiness cap is refused | E | REQ-688 | WFW-016 | WFE-016 | `WAR-051`, `WRF-30` | `F-WR-005` | COMPLETE | NOT RUN |
| `WFA-039` | OP regeneration is one item per nation-turn | E | REQ-681 | WFW-027 | — (regeneration §4.4) | `WAR-040`, `WAR-043a` | `F-WR-001` | COMPLETE | NOT RUN |
| `WFA-040` | OP conservation across consumption and release | E | REQ-681 | WFW-027, WFW-040 | — (worked accounting §8) | `WAR-040`, `WAR-043`, `WRF-34` | `F-WR-001`, `F-WR-002` | COMPLETE | NOT RUN |

**13.7.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-033` | The nation is both denied and blockaded | Compute the supply bundle | OPEN | 1 apply the denial surcharge of 2,500 bp; 2 apply the blockade surcharge of 2,500 bp; 3 cap the combined value at 5,000 bp; 4 round each bundle line once | `surcharge_bp = min(5000, 2500 + 2500) = 5000`; RAID bundle `ceil(5 × 1.5) / ceil(5 × 1.5)` = 8 / 8 applied once | The 8 / 8 bundle is reserved at acceptance | No double rounding, no 8.25, no second surcharge | `HELD` (supply bundle) | `WRA-03` (accepted cost) | N/A — a lawful capped computation | actor | WFE-017; WFW-007/010; §7.1, §14.4 |
| `WFA-034` | Ration demand is 4 and unreserved Food is 3 | Run P3.7 | P3.7 | 1 compute the demand from the canonical force snapshot; 2 compare it with unreserved Food; 3 the whole obligation cannot be paid; 4 cancel it entirely; 5 apply the readiness penalty | Whole obligation cancelled; readiness −100; `RATION_SHORT`; no debt; offensive blocked `WRF-35` | Readiness reduced by 100; no Food consumed; `RATION_SHORT` recorded for the turn | No partial payment, no debt, no civilian Food taken | none — the ration is not an OP ledger item | none — no `WRA-` event is defined for a cancelled ration; the turn ledger records the shortfall | `WRF-35` (offensive blocked at pre-P5) | actor; the opponent sees only a band | WFE-018; WFW-025; §7.3 |
| `WFA-035` | `available` is below the OP cost, or crowns are below the cost, tested as two variants | Submit | OPEN | 1 compute the total cost; 2 compare `available` and unreserved crowns; 3 fail the OP or crown row; 4 reserve nothing | `WRF-11` or `WRF-12`; nothing reserved | None | No negative balance, no overdraft, no partial reservation | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-11` / `WRF-12` | actor | WFW-018; §11.1 item 3 |
| `WFA-036` | Eligible `OP-09` surplus is 3 against a 4 Food requirement | Submit `OP-09` | OPEN | 1 compute the protected civilian requirement; 2 compute the eligible surplus; 3 compare 3 with 4; 4 fail the whole action | `WRF-25`; nothing reserved | None | No partial field ration, no civilian displacement | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-25` | actor | WFE-019; WFW-016; §7.3 |
| `WFA-037` | Two `OP-09` reservations exist and P3.6 must release both | Run P3.6 | P3.7 | 1 satisfy the protected civilian requirement first; 2 process reservations in reverse acceptance order; 3 fail both; 4 release each exactly once | Both fail `WRF-25`; civilians keep the Food | Both operations `FAILED`; `HELD → RELEASED` in reverse order | No forward-order release, no partial release | `HELD → RELEASED` ×2 | `WRA-02` ×2 | `WRF-25` | actor; the opponent sees only a band | WFE-020; WFW-016/025; §7.3 |
| `WFA-038` | Readiness is already at the cap | Submit `OP-09` | OPEN | 1 read readiness; 2 compare it with the cap; 3 fail the sustainment row; 4 reserve nothing | `WRF-30`; nothing reserved | None | No wasted resupply, no silent readiness gain | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-30` | actor | WFE-016; WFW-016; §10.2 |
| `WFA-039` | Balance is 9 below the cap; two turns are run | Run P3.7 twice | P3.7 | 1 open P3.7; 2 write one item per `(nation_id, turn_id)`; 3 add 1 below the cap; 4 record 0 at the cap; 5 never regenerate at P0 or P7 | +1 each turn; one `REGENERATED` item per turn; a zero item at the cap | `op_balance` +1 per turn; one `REGENERATED` line per turn | No P0 or P7 regeneration, no second item for one turn | `REGENERATED` ×1 per turn | `WRA-14` | N/A — a lawful regeneration | actor | WFW-027; §4.4, §11.2 |
| `WFA-040` | Balance 8, A holds 2, B fails, A resolves | Replay the worked accounting of §8 | P5 | 1 A writes `HELD` 2; 2 B fails and releases; 3 A consumes 2; 4 recompute `available = max(0, op_balance − reserved)`; 5 run the conservation check | `op_balance` 7 after A consumes; `available` 7; `reserved` 0; conservation holds | `op_balance` 8 → 7; A `HELD → CONSUMED`; B `HELD → RELEASED` | No lost or duplicated OP, no negative balance | `HELD → CONSUMED` (A); `HELD → RELEASED` (B) | `WRA-03`; `WRA-14` | N/A — the positive conservation path has no failure code | actor; moderators on request | §8 worked accounting; WFW-027/040 |

### 13.8 Class F — battle resolution and determinism

**13.8.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-041` | Zero power yields a contested result | F | REQ-685 | WFW-020 | WFE-021 | `WAR-081`, `WAR-083`, `F-WR-021` | `F-WR-021`, `F-WR-024`, `F-WR-025` | COMPLETE | NOT RUN |
| `WFA-042` | Second attack uses the post-loss baseline once | F | REQ-685 | WFW-020, WFW-021 | WFE-022 | `WAR-091`, `WAR-092` | `F-WR-022`, `F-WR-027` | COMPLETE | NOT RUN |
| `WFA-043` | Fortune is added once and never rounded | F | REQ-685 | WFW-020 | WFE-023 | `WAR-082`, `WAR-083`, `WAR-085` | `F-WR-023`, `F-WR-024`, `F-WR-025` | COMPLETE | NOT RUN |
| `WFA-044` | Pre-battle query returns a threat band only | F | REQ-672 | WFW-020 | WFE-024 | `WAR-086`, `F-WR-033` | `F-WR-033` | COMPLETE | NOT RUN |
| `WFA-045` | Readiness factor is bounded 5,000–10,000 | F | REQ-685 | WFW-020 | — (readiness factor §7.7) | `WAR-079`, `F-WR-020` | `F-WR-020` | COMPLETE | NOT RUN |
| `WFA-046` | Identical baseline and seed replay identically | F | REQ-655 | WFW-020 | — (determinism §11.3) | `WAR-082`, `F-WR-022`, `F-WR-023` | `F-WR-022`, `F-WR-023` | COMPLETE | NOT RUN |
| `WFA-047` | Strike power uses air attack only | F | REQ-693 | WFW-011 | — (`OP-05` strike power) | `WAR-080`, `F-WR-021` | `F-WR-021` | COMPLETE | NOT RUN |
| `WFA-048` | Tier boundaries are exact | F | REQ-685 | WFW-020 | — (tier boundaries §14.4) | `WAR-083`, `WAR-084`, `F-WR-025` | `F-WR-025` | COMPLETE | NOT RUN |

**13.8.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-041` | Attack power and defence power are both zero | Resolve the battle with fortune 0 | P5 | 1 compute both powers; 2 both are zero so `base_ratio_bp = 5000`; 3 add fortune 0; 4 map to the tier; 5 apply losses | `base_ratio_bp = 5000`; effective 5,000; `CONTESTED`; losses applied | Battle `APPLIED`; strength losses; readiness −25 | No division by zero, no attacker default win | `CONSUMED` (the operation) | `WRA-04` | N/A — a lawful contested battle | actor + defender | WFE-021; WFW-020; §7.7 |
| `WFA-042` | One attacker resolves two attacks in the same P5 | Resolve both | P5 | 1 order by the §4.8 key; 2 snapshot the first baseline; 3 apply the first losses; 4 the second baseline is the first minus cumulative losses; 5 readiness is not subtracted again as a baseline input | The second attack uses the reduced baseline; both tiers and loss sets are computed once | Two battles `APPLIED`; cumulative losses; readiness −25 per battle | No double readiness subtraction, no stale baseline | `CONSUMED` ×2 | `WRA-04` ×2 | N/A — a lawful two-battle sequence | actor + defender | WFE-022; WFW-020/021; §4.8, §11.1 item 1 |
| `WFA-043` | Base ratio is 7,400 and the seeded fortune is +500 | Resolve | P5 | 1 draw the seeded fortune; 2 confirm it lies within −500…+500; 3 add it once; 4 map the effective value | Effective 7,900; `DECISIVE_VICTORY`; no rounding of the roll | Battle `APPLIED`; losses | No clamped or rounded fortune beyond the stated bounds | `CONSUMED` | `WRA-04` | N/A — a lawful battle | actor + defender | WFE-023; WFW-020; §7.7 |
| `WFA-044` | The attacker queries the defender's strength before P5 | Request the value | P5 | 1 authenticate the caller; 2 classify the requested datum; 3 return only the permitted band; 4 withhold exact values until `WRA-04` | Only the threat band is returned; exact values appear in the report after `WRA-04` | None | No exact enemy strength, readiness or inventory | none — a pure computation writes no ledger item | none — a read-only query writes no event | N/A — the request is answered with a band, not refused | actor; the defender's exact values withheld | WFE-024; WFW-020; §12.2 |
| `WFA-045` | Readiness is 0, 500 and 1,000 in three fixtures | Compute `readiness_factor_bp` | P5 | 1 apply `5000 + 5 × readiness`; 2 evaluate all three fixtures; 3 clamp inside 5,000–10,000 | 5,000 / 7,500 / 10,000 respectively | None — a pure computation | No factor above 10,000 or below 5,000 | none — a pure computation writes no ledger item | none — a computation writes no event | N/A — a lawful computation | actor | WFW-020; register `F-WR-020` |
| `WFA-046` | The frozen baseline and seed are identical across two runs | Resolve twice | P5 | 1 freeze the baseline; 2 derive the seed; 3 resolve once; 4 replay from the same inputs | Identical tier and losses; the same fortune draw | The first resolution mutates; the replay returns the committed battle | No wall-clock or client randomness, no second mutation | none beyond the first resolution | `WRA-04` ×1; the replay writes nothing | N/A — determinism is a positive property | actor + defender | WFW-020; §11.3 |
| `WFA-047` | Air attack power is 6,000 | Compute strike power | P5 | 1 apply `2000 + floor(air_attack_power × 2500 / 10000)`; 2 include no raw-force term; 3 round once | `2000 + floor(6000 × 2500 / 10000) = 3500` | None — a pure computation | No extra force term, no rounding drift | none — a pure computation writes no ledger item | none — a computation writes no event | N/A — a lawful computation | actor | WFW-011; register `F-WR-021` |
| `WFA-048` | Eight fixtures place the effective ratio at 3,999, 4,000, 4,999, 5,000, 5,999, 6,000, 7,499 and 7,500 | Resolve each boundary | P5 | 1 compute each effective value; 2 map it to exactly one tier; 3 assert the adjacent boundaries do not overlap | `ATTACKER_DEFEAT`, `REPULSED`, `REPULSED`, `CONTESTED`, `CONTESTED`, `ATTACKER_VICTORY`, `ATTACKER_VICTORY`, `DECISIVE_VICTORY` | Eight fixture battles `APPLIED` | No off-by-one tier boundary | `CONSUMED` ×8 (fixture) | `WRA-04` ×8 | N/A — lawful boundary resolutions | actor + defender | WFW-020; register `F-WR-025`, §14.4 |

### 13.9 Class G — losses, damage, repair and caps

**13.9.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-049` | Battle loss is capped at 20 percent | G | REQ-689 | WFW-021 | WFE-025 | `WAR-105`, `F-WR-028` | `F-WR-027`, `F-WR-028` | COMPLETE | NOT RUN |
| `WFA-050` | Campaign loss cap stops strength loss but not readiness loss | G | REQ-689 | WFW-021 | WFE-026 | `WAR-105`, `WAR-109` | `F-WR-028` | COMPLETE | NOT RUN |
| `WFA-051` | A floor-level city takes zero damage but the battle resolves | G | REQ-700 | WFW-023 | WFE-027 | `WAR-109h`, `WRF-36` | `F-WR-037` | COMPLETE | NOT RUN |
| `WFA-052` | Over-repair is refused at P4.1 without charge | G | REQ-703 | WFW-030 | WFE-028 | `WAR-109l`, `WAR-114`, `WRF-37` | `F-WR-038` | COMPLETE | NOT RUN |
| `WFA-053` | Largest-remainder loss allocation is exact | G | REQ-689 | WFW-021 | — (fractional loss §5.3) | `WAR-104`, `F-WR-027` | `F-WR-027` | COMPLETE | NOT RUN |
| `WFA-054` | Readiness loss is 25 per battle, floored at zero | G | REQ-682 | WFW-022 | — (readiness loss §5.4) | `WAR-106`, `WAR-110` | `F-WR-005` | COMPLETE | NOT RUN |
| `WFA-055` | Per-city campaign damage cap is enforced | G | REQ-700 | WFW-023 | — (30 percent cap §7.4) | `WAR-109g`, `WAR-109i` | `F-WR-037` | COMPLETE | NOT RUN |
| `WFA-056` | Repair cost is stepped and discounted once | G | REQ-703 | WFW-030 | — (repair cost §7.4) | `WAR-114`, B-05 `URB-043`/`URB-044` | `F-WR-038` | COMPLETE | NOT RUN |

**13.9.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-049` | A computed loss exceeds 20 percent of engaged strength | Apply losses | P5 | 1 compute the proportional loss; 2 compare it with the 20 percent battle cap; 3 cap the removal; 4 state the cap in the report | Capped at 20 percent; the report states the cap | Capped strength removal; readiness −25 | No loss above the battle cap | `CONSUMED` | `WRA-04` | N/A — the cap is a lawful bound | actor + defender | WFE-025; WFW-021; §5.3, register `F-WR-028` |
| `WFA-050` | Campaign cumulative loss reaches 60 percent | Resolve another battle | P5 | 1 read the cumulative campaign loss; 2 the 60 percent cap is reached; 3 remove zero further strength; 4 still apply the readiness loss | Zero further strength loss; readiness loss continues; `LOSS_CAP_REACHED` | Battle `APPLIED`; no strength removal; readiness −25 | No strength loss past the campaign cap, no suppression of readiness loss | `CONSUMED` | `WRA-04` | N/A — the cap is a lawful bound; `LOSS_CAP_REACHED` is a state label | actor + defender | WFE-026; WFW-021; §5.3 |
| `WFA-051` | City infrastructure is at the floor of 10 and the attacker wins | Strike the city | P5 | 1 compute the damage formula; 2 find zero headroom above the floor; 3 record `removed = 0`; 4 still resolve the battle | `removed = 0`; no damage event; the battle still resolves | Battle `APPLIED`; no infrastructure change | No negative infrastructure, no rejection for a floor-level city | `CONSUMED` | `WRA-04`; `WRA-08` with `removed = 0` | N/A — zero damage is lawful | actor + defender; infrastructure is public | WFE-027; WFW-023; §7.4 |
| `WFA-052` | A repair of 5 levels is requested with 3 unrepaired levels | Submit the repair | P4.1 | 1 read the damage; 2 compare the requested levels with the unrepaired levels; 3 fail the repair row; 4 release the reservation | `WRF-37` at P4.1; nothing charged; reservation released | None; `HELD → RELEASED` | No over-repair, no charge, no negative damage balance | `HELD → RELEASED` | `WRA-02` | `WRF-37` | actor | WFE-028; WFW-030; §7.4 |
| `WFA-053` | A mixed force produces a fractional proportional loss | Apply losses | P5 | 1 compute each type's proportional loss; 2 allocate by largest remainder in `UNIT-AIR`, `UNIT-ARM`, `UNIT-INF`, `UNIT-NAV` order; 3 verify the sum equals the computed integer | Total removed equals the computed integer | Strength removed per type | No rounding that loses or creates strength points | `CONSUMED` | `WRA-04` | N/A — a lawful allocation | actor + defender | WFW-021; register `F-WR-027` |
| `WFA-054` | Three battles resolve in one turn | Apply readiness | P5 | 1 subtract 25 per battle; 2 floor at zero; 3 apply no catch-up | Readiness reduced and floored at zero | Readiness reduced | No readiness below zero, no automatic recovery | none — readiness changes without an OP or resource item | `WRA-04` ×3 | N/A — a lawful readiness loss | actor | WFW-022; §5.4 |
| `WFA-055` | A city has already taken 30 percent of its infrastructure this campaign | Strike again on a victory | P5 | 1 read cumulative city damage; 2 the per-city campaign cap is reached; 3 remove zero further levels; 4 refuse a substitute city | Zero further damage; the cap is enforced | Battle `APPLIED`; no damage | No second 30 percent tranche, no damage to another city as a substitute | `CONSUMED` | `WRA-04`; `WRA-08` with `removed = 0` | N/A — the cap is a lawful bound | actor + defender; infrastructure is public | WFW-023; §7.4 |
| `WFA-056` | City damage is 7 and a repair of 3 levels is ordered | Compute the cost | P4.1 | 1 apply `Σ(8 + floor(j/10))` to the repaired levels; 2 apply the 10 percent Civil Survey discount once; 3 respect the 500-level cap | Stepped cost with one discount; the cap is respected | Crowns charged; infrastructure restored | No discount stacking, no charge above the cap | none — crowns, not OP | none — repair is a B-05 city-ledger event; no `WRA-` event is defined | N/A — a lawful positive cost | actor; infrastructure is public | WFW-030; register `F-WR-038`; B-05 |

### 13.10 Class H — peace, settlement and surrender

**13.10.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-057` | Mutual ceasefire applies and ends the campaign | H | REQ-690 | WFW-034 | — (ceasefire §7.5) | `WAR-121`–`WAR-124` | N/A — a term application, not arithmetic | COMPLETE | NOT RUN |
| `WFA-058` | Six terms are valid and an invented term is refused | H | REQ-690 | WFW-035 | — (closed term set §7.5) | `WAR-126`–`WAR-130` | `F-WR-031` | COMPLETE | NOT RUN |
| `WFA-059` | Postwar exclusion blocks a new declaration at all three points | H | REQ-690 | WFW-001 | — (exclusion §7.5) | `WAR-135`, `WRF-32` | `F-WR-031` | COMPLETE | NOT RUN |
| `WFA-060` | Lost settlement reservation fails atomically | H | REQ-690 | WFW-039 | WFE-029 | `WAR-138`, `WRF-33` | `F-WR-029` | COMPLETE | NOT RUN |
| `WFA-061` | An unanswered proposal expires without cooldown | H | REQ-690 | WFW-035, WFW-036 | WFE-030 | `WAR-122`, `F-WR-030` | `F-WR-030` | COMPLETE | NOT RUN |
| `WFA-062` | Inactivity never implies consent | H | REQ-690 | WFW-036 | — (silence rule §12.3) | `WAR-151`, `WAR-138` | N/A — consent is a rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-063` | Surrender terminates a proposed settlement with one outcome | H | REQ-690 | WFW-037 | WFE-032 | `WAR-139`, `WAR-140` | N/A — one-outcome rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-064` | Disarmament beyond available strength is partly satisfied without debt | H | REQ-690 | WFW-038 | WFE-031 | `WAR-137`, `WAR-136` | `F-WR-031` | COMPLETE | NOT RUN |

**13.10.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-057` | An `ACTIVE` campaign exists | Propose and accept a mutual ceasefire | P5 | 1 one owner proposes; 2 the counterparty accepts explicitly; 3 apply `TERM_CEASEFIRE`; 4 move to `SETTLING` then the end state; 5 write the event | `TERM_CEASEFIRE` applied; campaign `SETTLING` then ended; `WRA-12` | Settlement `COMPLETED`; campaign ended; no transfer | No third-party proposal, no automatic acceptance | none — ceasefire applies no value transfer | `WRA-12`; `WRA-13` | N/A — a lawful agreement | actor + defender; terms public when completed | WFW-034; §7.5 |
| `WFA-058` | A valid settlement window is open | Submit each of the six terms, then an invalid term | P4.1 | 1 confirm the closed term enumeration; 2 admit each of the six valid terms; 3 reject the invalid term; 4 reserve nothing for it | Six terms valid; the invalid term is rejected and reserves nothing | Six proposal terms recorded; the invalid term writes nothing | No open-ended or new term type | none — an invalid term reserves nothing | `WRA-12` (proposal) | N/A — the term set is closed and an unknown term is rejected before the validator | actor + defender | WFW-035; §7.5 |
| `WFA-059` | `TERM_EXCLUSION` is active until turn T | Declare between the pair before T | OPEN | 1 submission check; 2 P2 recheck; 3 pre-P5 recheck; 4 fail at each point | `WRF-32` at submission, P2 and P5; nothing reserved | None | No declaration before the exclusion ends | none — rejected before any OP or resource is reserved | `WRA-02` | `WRF-32` | actor + defender; the exclusion is public | WFW-001; §10.2 |
| `WFA-060` | A settlement is accepted and its reservation is lost before P5.3 | Run P5.3 | P5 | 1 read the settlement reservation; 2 it is missing; 3 fail the whole unit; 4 return the campaign to `ACTIVE`; 5 commit zero transfer legs | `WRF-33`; campaign returns `ACTIVE`; zero transfer legs | Settlement `FAILED`; campaign `ACTIVE`; no transfer | No partial transfer, no campaign end | none — the reservation is already lost and no leg commits | `WRA-12` (failure); `WRA-05` | `WRF-33` | actor + defender | WFE-029; WFW-039; §11.2 |
| `WFA-061` | A proposal is unanswered for 12 turns | Advance the window | P5 | 1 the window is 12 turns; 2 no response is recorded; 3 expire the proposal; 4 apply no cooldown | `EXPIRED`; no cooldown; no term applied | Proposal `EXPIRED` | No acceptance by silence | none — expiry applies no term and moves no value | `WRA-12` | N/A — expiry is a lawful outcome | actor + defender | WFE-030; WFW-035/036; §7.5 |
| `WFA-062` | The counterparty does not respond | Advance to the window end | P5 | 1 find no response event; 2 infer no acceptance; 3 expire the proposal | Proposal expires; nothing transfers | Proposal `EXPIRED` | No inferred consent from inactivity | none — expiry applies no term and moves no value | `WRA-12` | N/A — expiry is a lawful outcome | actor + defender | WFW-036; §12.3 |
| `WFA-063` | The owner surrenders while a settlement is `PROPOSED` | Surrender | P5 | 1 confirm the owner acts personally; 2 surrender is unilateral; 3 apply `TERM_CEASEFIRE`; 4 terminate the open proposal; 5 record exactly one outcome | Campaign ends with `TERM_CEASEFIRE`; the open proposal terminates; exactly one outcome | Campaign ended; proposal terminated; terms applied | No double outcome, no competing settlement | none — ceasefire termination applies no value transfer | `WRA-12`; `WRA-13` | N/A — a lawful surrender | actor + defender; outcome is public | WFE-032; WFW-037; §4.3, §7.5 |
| `WFA-064` | Disarmament requests more strength than exists | Complete the settlement | P5 | 1 compare each demand with available strength; 2 cancel the remainder; 3 record partial satisfaction; 4 complete the settlement; 5 create no debt | Remainder cancelled; partial satisfaction; settlement completes; no debt | Strength removed to zero where demanded; settlement `COMPLETED` | No strength below zero, no debt for the unmet remainder | none — the cancelled remainder moves no value | `WRA-12`; `WRA-13` | N/A — partial satisfaction is lawful | actor + defender | WFE-031; WFW-038; §7.5 |

### 13.11 Class I — protection, counters and persistent states

**13.11.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-065` | Fortification raises defence to 12,500 once | I | REQ-688 | WFW-014 | — (fortification §4.6) | `WAR-098`, `F-WR-026` | `F-WR-026` | COMPLETE | NOT RUN |
| `WFA-066` | Interception triggers once with 14,000 defence and 8,500 attack | I | REQ-688 | WFW-013 | — (interception §4.6) | `WAR-095`, `WAR-118`, `F-WR-026` | `F-WR-026` | COMPLETE | NOT RUN |
| `WFA-067` | Break-blockade removes the blockade and starts cooldown | I | REQ-688 | WFW-015 | — (break blockade §4.6) | `WAR-118`, `F-WR-026` | `F-WR-026` | COMPLETE | NOT RUN |
| `WFA-068` | Only the strongest applicable counter applies | I | REQ-688 | WFW-020 | — (no stacking §4.6) | `WAR-119`, `WAR-120` | `F-WR-026` | COMPLETE | NOT RUN |
| `WFA-069` | Break-blockade resolves at P5.7 after the blockade | I | REQ-686 | WFW-015 | WFE-035 | `WAR-089`, `WAR-118`, `WRF-29` | `F-WR-018` | COMPLETE | NOT RUN |
| `WFA-070` | Protection activating after P2 fails at pre-P5 | I | REQ-687 | WFW-031 | WFE-033 | `WAR-116`, `WRF-05` | N/A — a timing check, not arithmetic | COMPLETE | NOT RUN |
| `WFA-071` | Protection expiry does not revive a failed action | I | REQ-687 | WFW-031 | WFE-034 | `WAR-116` | N/A — a timing check, not arithmetic | COMPLETE | NOT RUN |
| `WFA-072` | No re-blockade during cooldown | I | REQ-686 | WFW-010, WFW-015 | — (cooldown §4.6) | `WAR-083`, `WAR-118` | `F-WR-018` | COMPLETE | NOT RUN |

**13.11.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-065` | An incoming attack exists and `OP-07` is accepted | Resolve both | P5 | 1 resolve `OP-07` at P5.5; 2 set defence power to 12,500; 3 apply it once to the incoming battle; 4 discard the state after the turn | Defence power 12,500 applied once | Fortification state applied; battle uses 12,500 | No stacking, no carry to another P5 | `HELD → CONSUMED` | `WRA-10`; `WRA-04` | N/A — a lawful defensive resolution | actor + defender | WFW-014; §4.6, register `F-WR-026` |
| `WFA-066` | An incoming air or missile operation is declared | Resolve `OP-06` | P5 | 1 arm the interception at P5.5; 2 trigger only on a qualifying attack; 3 use defence 14,000 and attack 8,500; 4 expire after one trigger | Defence 14,000 and attack 8,500; triggers once and expires | Interception state consumed; battle resolved | No interception without a triggering attack, no second trigger | `HELD → CONSUMED` | `WRA-09`; `WRA-04` | N/A — a lawful interception | actor + defender | WFW-013; §4.6 |
| `WFA-067` | A blockade is active on the pair | Resolve `OP-08` | P5 | 1 resolve `OP-08` at P5.7; 2 use attack power 7,000; 3 on success remove the blockade; 4 start the cooldown | Attack power 7,000; success removes the blockade and starts the cooldown | Blockade removed; cooldown state set | No break without a blockade, no cooldown skip | `HELD → CONSUMED` | `WRA-07`; `WRA-04` | N/A — a lawful counter | actor + defender; the state is public | WFW-015; §4.6 |
| `WFA-068` | `FORTIFY` and `INTERCEPT` are both active | Resolve an attack | P5 | 1 enumerate active counters; 2 select the strongest applicable one; 3 add no second value | The strongest applicable counter applies; no addition | The battle uses exactly one counter value | No stacked counter values | `CONSUMED` | `WRA-04` | N/A — a lawful counter selection | actor + defender | WFW-020; §4.6 |
| `WFA-069` | `OP-04` and `OP-08` are submitted in the same turn | Run P5 | P5 | 1 the blockade resolves at its own step; 2 `OP-08` resolves at P5.7; 3 success removes the state and starts the cooldown; 4 `WRF-29` only if no blockade exists | `OP-08` at P5.7; success removes the state and starts the cooldown; `WRF-29` only if no blockade exists | Blockade applied then removed; cooldown set | No break at P5.6, no break before the blockade resolves | `HELD → CONSUMED` ×2 | `WRA-07`; `WRA-04` | `WRF-29` (conditional) | actor + defender | WFE-035; WFW-015; §4.8 |
| `WFA-070` | Protection activates between P2 and pre-P5 | Run pre-P5 | P5 | 1 P2 has passed; 2 protection becomes active; 3 the pre-P5 recheck runs; 4 fail; 5 release | `WRF-05`; every reservation released | Operation `FAILED`; `HELD → RELEASED` | No execution because P2 passed | `HELD → RELEASED` | `WRA-02` | `WRF-05` | actor + defender | WFE-033; WFW-031; §2.5.1 |
| `WFA-071` | Protection expires after a P2 failure | Re-submit after expiry | P2 | 1 the earlier failure stands; 2 no revival path exists; 3 a new submission is required; 4 the new submission passes the checks | The earlier failure stands; a new submission is required and passes | Old action remains `FAILED`; new action `ACCEPTED` | No automatic revival of the failed action | old `RELEASED`; new `HELD` | `WRA-02` (old); `WRA-03` (new) | N/A — the test asserts non-revival; the original failure was `WRF-05` | actor | WFE-034; WFW-031; §2.5.1 |
| `WFA-072` | A blockade was broken and the cooldown is running | Re-submit `OP-04` during the cooldown | OPEN | 1 read the cooldown; 2 it is active; 3 fail the state row; 4 create no new blockade | `WRF-27`; no new blockade until the cooldown ends | None | No immediate re-blockade | none — rejected before any OP or resource is reserved | none — rejected at submission | `WRF-27` | actor | WFW-010/015; §4.6 |

### 13.12 Class J — dormancy, reroll and account lifecycle

**13.12.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-073` | Dormant declarer suspends and releases | J | REQ-659 | WFW-005 | WFE-037 | `WAR-021`, `WAR-022`, `WRF-21` | `F-WR-008` | COMPLETE | NOT RUN |
| `WFA-074` | Execution-time dormancy governs over a stale P2 result | J | REQ-659 | WFW-031 | WFE-038 | `WAR-013`, `WAR-116` | N/A — a timing check, not arithmetic | COMPLETE | NOT RUN |
| `WFA-075` | An active campaign blocks reroll | J | REQ-660 | WFW-033 | — (reroll block `UD-032` Option A) | `WAR-028`, `WAR-030` | N/A — an account-lifecycle rule | COMPLETE | NOT RUN |
| `WFA-076` | Reroll unblocks only after `VOID` and never during settlement | J | REQ-660 | WFW-033 | WFE-012, WFE-036 | `WAR-028`, `WAR-029`, `UD-032` Option A | N/A — an account-lifecycle rule | COMPLETE | NOT RUN |
| `WFA-077` | Forty-eight suspended turns abandon the campaign | J | REQ-659 | WFW-006 | WFE-039 | `WAR-023`, `WAR-024` | `F-WR-008` | COMPLETE | NOT RUN |
| `WFA-078` | Retirement and reroll preserve campaign attribution | J | REQ-660 | WFW-006, WFW-033 | WFE-040 | `WAR-028`, `WAR-029` | N/A — a record-retention rule | COMPLETE | NOT RUN |
| `WFA-079` | Newcomer protection cannot be extended by declaration | J | REQ-658 | WFW-002 | — (newcomer protection B-03) | B-03 `ONB-019`/`ONB-020`, `WAR-115` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-080` | Surrender is the off-ramp from a reroll block | J | REQ-660 | WFW-037 | — (surrender off-ramp `UD-032` Option A) | `UD-032` Option A, `WAR-028` | N/A — an account-lifecycle rule | COMPLETE | NOT RUN |

**13.12.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-073` | The declarer is dormant at P0 with a pending declaration | Run P0–P2 | P2 | 1 detect dormancy; 2 suspend the campaign; 3 fail the pending declaration; 4 release | `SUSPENDED`; declaration fails `WRF-21`; everything released | Campaign `SUSPENDED`; declaration `FAILED`; `HELD → RELEASED` | No activation while dormant | `HELD → RELEASED` | `WRA-05`; `WRA-02` | `WRF-21` | actor + defender | WFE-037; WFW-005; §4.7 |
| `WFA-074` | The target is dormant at P2 and awake at pre-P5 | Run both rechecks | P5 | 1 P2 fails the dormancy row; 2 a fresh submission is made after waking; 3 pre-P5 reads the awake state; 4 the operation proceeds | P2 fails `WRF-21`; on a fresh submission after waking the operation proceeds; execution-time state governs | Old action `FAILED`; new action `ACCEPTED` | No stale P2 result overriding execution-time state | old `RELEASED`; new `HELD` | `WRA-02` (old); `WRA-03` (new) | `WRF-21` (P2) | actor | WFE-038; WFW-031; §2.5.1 |
| `WFA-075` | An `ACTIVE` campaign is attributed to the account | Request a reroll | OPEN | 1 read the attributed campaign; 2 it is `ACTIVE`; 3 block the reroll; 4 require settlement, surrender or expiry | Blocked; the campaign must end by settlement, surrender or expiry | None | No reroll that erases an active campaign | none — rejected before any OP or resource is reserved | none — a refused request writes no event | N/A — the block is an `UD-032` Option A rule outcome, not a `WRF-` code | actor | WFW-033; `UD-032` Option A |
| `WFA-076` | Either `VOID` is recorded, or the campaign is `SETTLING`, tested as two states | Request a reroll in each state | P7 | 1 read the campaign state; 2 with `VOID` recorded the block lifts; 3 while `SETTLING` the request stays blocked; 4 preserve the ordering | The block lifts only after `VOID` is recorded; blocked while `SETTLING` | Reroll permitted in the `VOID` case; none in the `SETTLING` case | No reroll before `VOID`, no reroll during settlement | none — the reroll block changes no ledger balance | `WRA-05` (the `VOID` record) | N/A — a lawful state-dependent outcome | actor | WFE-012/036; WFW-033 |
| `WFA-077` | Both sides are dormant for 48 suspended turns | Advance the counter | P5 | 1 confirm both sides dormant; 2 the counter reaches 48; 3 abandon with `DRAW`; 4 apply no reparations | `ABANDONED` with `DRAW`; no reparations | Campaign `SUSPENDED → ABANDONED` | No victor, no transfer, no hidden reset | none — abandonment records no reparation or transfer | `WRA-13` | N/A — a terminal outcome | public; actor + defender | WFE-039; WFW-006; §4.1 |
| `WFA-078` | A belligerent retires and the account rerolls | Inspect the campaign record | P7 | 1 reroll the account; 2 read the campaign; 3 attribution is unchanged; 4 the record remains readable and nothing transfers | Campaign stays attributed; the record is readable; nothing transfers | Account rerolled; campaign record unchanged | No record deletion, no asset transfer | none — the campaign record survives without a transfer | none — no battle or state event is written; the record is retained | N/A — a retention rule | actor; the opponent keeps the record | WFE-040; WFW-006/033 |
| `WFA-079` | A newcomer is inside the 7-day and 84-turn protection window | Submit a declaration | OPEN | 1 run the newcomer-protection row; 2 the target is protected; 3 fail; 4 reserve nothing | `WRF-05`; nothing reserved | None | No protection extension beyond the stated scope | none — rejected before any OP or resource is reserved | `WRA-02` | `WRF-05` | actor | WFW-002; B-03 `ONB-019`/`ONB-020`; §10.2 |
| `WFA-080` | Reroll is blocked by an active campaign | Surrender | P5 | 1 the reroll remains blocked; 2 surrender is permitted; 3 the campaign ends; 4 a later reroll follows the normal rules | Surrender ends the campaign; a later reroll is governed normally | Campaign ended; account eligibility is evaluated normally afterwards | No reroll used to avoid terms, no surrender bypassing terms | none — surrender ends the campaign without a value transfer | `WRA-13`; `WRA-12` | N/A — a lawful surrender | actor + defender | WFW-037; `UD-032` Option A |

### 13.13 Class K — idempotency, atomicity, recovery and concurrency

**13.13.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-081` | Duplicate idempotency key returns the original receipt | K | REQ-657 | WFW-019 | WFE-041 | `WAR-097`, `WRF-13` | N/A — idempotency is a key rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-082` | Concurrent double-click yields one action | K | REQ-657 | WFW-019 | — (double click §11.4) | `WAR-097`, `WAR-042` | N/A — idempotency is a key rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-083` | Interrupted P5 skips an applied battle | K | REQ-655 | WFW-040 | WFE-042 | `WAR-099`, `F-WR-034` | `F-WR-034` | COMPLETE | NOT RUN |
| `WFA-084` | Interrupted-before-commit replay is deterministic | K | REQ-655 | WFW-040 | WFE-043 | `WAR-099`, `F-WR-022` | `F-WR-022`, `F-WR-023` | COMPLETE | NOT RUN |
| `WFA-085` | P7 voids an unresolved operation and releases it | K | REQ-681 | WFW-040 | — (P7 void §11.2) | `WAR-043`, `WRF-22` | `F-WR-002` | COMPLETE | NOT RUN |
| `WFA-086` | P7 holds the checkpoint when a reservation remains | K | REQ-681 | WFW-040 | WFE-044 | `WAR-043`, `WAR-100`, `WRF-34` | N/A — an invariant check, not arithmetic | COMPLETE | NOT RUN |
| `WFA-087` | Settlement transfer is all-or-nothing | K | REQ-663 | WFW-039 | — (atomic transfer §11.2) | `WAR-138`, `F-WR-029`, `WRF-33` | `F-WR-029` | COMPLETE | NOT RUN |
| `WFA-088` | A duplicate P3.7 boundary writes one item | K | REQ-681 | WFW-027 | — (duplicate boundary §11.3) | `WAR-040`, `WAR-043a` | `F-WR-001` | COMPLETE | NOT RUN |

**13.13.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-081` | The same action key is submitted twice | Replay the request | OPEN | 1 find the key; 2 return the original receipt; 3 write no second reservation; 4 write no second audit event | `WRF-13`; original receipt; one `HELD` item | None on the replay | No second reservation, no second audit event | one `HELD` | `WRA-03` ×1 | `WRF-13` | actor | WFE-041; WFW-019; §11.3 |
| `WFA-082` | Two concurrent double-click submissions arrive | Submit both before either commits | OPEN | 1 take the idempotency lock; 2 the first commits; 3 the second returns the original receipt; 4 verify one `HELD` | One action and one `HELD`; the other returns the original receipt | One action committed | No two distinct actions, no double spend | `HELD` ×1 | `WRA-03` ×1 | N/A — the second request is a replay, not a failure | actor | §11.4 item 3; WFW-019 |
| `WFA-083` | P5 is interrupted after a battle commits | Resume P5 | P5 | 1 read the committed battle; 2 it is `APPLIED`; 3 skip it; 4 apply no second loss; 5 write no second event | Resume skips the `APPLIED` battle; no double losses; no second `WRA-04` | Resume state only | No re-applied losses, no duplicate battle | `CONSUMED` once | `WRA-04` ×1 | N/A — a lawful recovery | actor + defender | WFE-042; WFW-040; §11.3 |
| `WFA-084` | P5 is interrupted before a battle commits | Resume and replay | P5 | 1 reuse the frozen baseline; 2 reuse the seed; 3 recompute; 4 assert the same tier and losses | The same frozen baseline and seed produce the same tier and losses | One battle committed | No new fortune draw, no changed baseline | `CONSUMED` once | `WRA-04` ×1 | N/A — a lawful recovery | actor + defender | WFE-043; WFW-040; §11.3 |
| `WFA-085` | An accepted operation has no terminal resolution at P7 | Run the P7 close | P7 | 1 find the unresolved operation; 2 release it; 3 record `WRF-22`; 4 void it so it cannot replay | `RELEASED`; `WRF-22`; the action is void and cannot replay into the next turn | Operation `VOID`; `HELD → RELEASED` | No silent carry-over, no balance debit | `HELD → RELEASED` | `WRA-02`; `WRA-14` | `WRF-22` | actor | WFW-040; §11.2 |
| `WFA-086` | A reservation remains at the P7 close | Run the P7 close | P7 | 1 verify `reserved = 0`; 2 the check fails; 3 record `WRF-34`; 4 hold the checkpoint and publish nothing | `WRF-34`; the checkpoint is held; the turn is not published | Nothing is published | No publication with a live reservation | `HELD` remains | `WRA-14`; `WRA-02` | `WRF-34` | actor; moderators | WFE-044; WFW-040; §11.2 |
| `WFA-087` | A settlement transfer would partly commit | Force a failure between legs | P5 | 1 stage the first leg; 2 inject a failure; 3 roll back every leg; 4 return the campaign to `ACTIVE`; 5 record the failure | Zero transfer legs; campaign returns `ACTIVE`; `WRA-12` records the failure | Settlement `FAILED`; campaign `ACTIVE`; no value moved | No partial crown or resource transfer | none — the failed settlement moves no value | `WRA-12`; `WRA-05` | `WRF-33` | actor + defender | WFW-039; §11.2 |
| `WFA-088` | A duplicate P3.7 boundary run is requested for one turn | Run the boundary twice | P3.7 | 1 derive the boundary key; 2 the first run writes the item; 3 the second returns the original receipt; 4 write no second item | The second run returns the original receipt and writes no item | One `REGENERATED` item | No second `REGENERATED` item, no second OP | `REGENERATED` ×1 | `WRA-14` ×1 | N/A — a lawful replay | actor | WFW-027; §11.3 |

### 13.14 Class L — visibility, privacy and audit access

**13.14.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-089` | A third party cannot query exact readiness | L | REQ-672 | WFW-020 | WFE-045 | `WAR-086`, `WAR-148`, `F-WR-033` | `F-WR-033` | COMPLETE | NOT RUN |
| `WFA-090` | An Alliance cannot read a member's battle report | L | REQ-670 | WFW-020 | WFE-046 | `WAR-148` | N/A — an access rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-091` | A public aggregate below five nations is withheld | L | REQ-672 | WFW-020 | WFE-047 | `WAR-147`, `WAR-150`, D-027 | N/A — a k-anonymity threshold | COMPLETE | NOT RUN |
| `WFA-092` | A blocked attack discloses the rule and counterparty only | L | REQ-669 | WFW-002 | WFE-048 | `WAR-014`, `WAR-154`, `AUD-AL-017` | N/A — a disclosure rule | COMPLETE | NOT RUN |
| `WFA-093` | Ration view separates owner detail from opponent band | L | REQ-672 | WFW-025 | — (ration visibility `WAR-053h`) | `WAR-053h`, `WAR-149` | `F-WR-036` | COMPLETE | NOT RUN |
| `WFA-094` | Only the fourteen audit events are emitted | L | REQ-692 | WFW-020, WFW-025 | — (audit catalogue §14.5) | `WAR-153`–`WAR-155` | N/A — an event catalogue | COMPLETE | NOT RUN |
| `WFA-095` | Nothing partial is visible before battle commit | L | REQ-692 | WFW-020 | — (pre-commit leakage) | `WAR-088`, `WAR-153` | N/A — a visibility-timing rule | COMPLETE | NOT RUN |
| `WFA-096` | Only authorised administration reads fair-play data | L | REQ-692 | WFW-040 | — (administrative access) | `WAR-155` | N/A — an access rule, not arithmetic | COMPLETE | NOT RUN |

**13.14.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-089` | A third party queries exact readiness | Query | P5 | 1 authenticate; 2 classify the audience; 3 return only the permitted band; 4 withhold the exact value | Denied the exact value; only a band may be returned | None | No exact readiness to a non-owner | none — a read or visibility check writes no ledger item | none — a read-only query | N/A — the request is answered with a band | actor and defender see their own; the third party receives a band only | WFE-045; §12.2 |
| `WFA-090` | An Alliance requests a member's battle report | Request | P5 | 1 authenticate; 2 classify the Alliance audience; 3 deny the military record; 4 leave the `AX-18` surface unchanged | Denied; the `AX-18` surface is unchanged | None | No Alliance access to military records | none — a read or visibility check writes no ledger item | none — a denied read writes no event | N/A — the request is refused by the visibility matrix, not a `WRF-` code | Alliance denied; the two belligerents retain their reports | WFE-046; §12.2; B-09 `AX-18` |
| `WFA-091` | A public statistic would identify four nations | Publish | P5 | 1 count the distinct nations; 2 apply the k = 5 threshold; 3 four is below it; 4 withhold or coarsen | Withheld or coarsened below k = 5 | None | No small-group re-identification | none — a read or visibility check writes no ledger item | none — a suppressed publication writes no event | N/A — suppression is a D-027 policy outcome | public; the statistic is withheld | WFE-047; D-027; §12.4 |
| `WFA-092` | A blocked attack names an `AT-E01` counterparty | Inspect the response and audit record | OPEN | 1 fail the operation; 2 show the rule and the counterparty; 3 withhold private treaty text; 4 write `AUD-AL-017` with B-09 fields only | The actor sees the rule and counterparty; no private treaty text; `AUD-AL-017` uses B-09 fields only | One `AUD-AL-017` record | No `AT-E00` text, no extra personal data | none — an audit record is not an OP or resource movement | `AUD-AL-017`; `WRA-02` | `WRF-08` | actor sees the rule; moderators see `AUD-AL-017` | WFE-048; §10.2, §12.2 |
| `WFA-093` | The owner and the opponent view a ration-short turn | Inspect both views | P3.7 | 1 render the owner view; 2 render the opponent view; 3 compare the disclosed fields | The owner sees demand, outcome and shortfall; the opponent sees only a band | None | No exact Food stock to the opponent | none — an audit record is not an OP or resource movement | none — visibility is a read | N/A — a lawful disclosure split | actor detail; defender band | WFW-025; §12.2 |
| `WFA-094` | A full turn contains a battle, a settlement and a ration | Enumerate the events | P5 | 1 enumerate the emitted events; 2 each is one of the fourteen; 3 verify append-only order | Exactly the fourteen `WRA-` events named in §14.5 where applicable; append-only | Events appended | No event outside the closed fourteen, no in-place edit | `WRA-14` included | `WRA-01`–`WRA-14` as applicable | N/A — the positive catalogue path | varies per event; the public record carries only the permitted fields | §14.5, §12.2 |
| `WFA-095` | A battle is being resolved | Inspect visibility before and after `WRA-04` | P5 | 1 read the pre-commit view; 2 confirm nothing partial is present; 3 read the post-commit view; 4 confirm the report appears exactly at `WRA-04` | Nothing partial is visible before commit; the report appears at `WRA-04` | The event commits the report | No pre-commit battle leakage | none — the report is not a ledger movement | `WRA-04` | N/A — a lawful visibility boundary | actor + defender | WFW-020; §12.2 |
| `WFA-096` | An administrator opens a fair-play record | Query | P7 | 1 authenticate the administrator; 2 check the authorised purpose; 3 return the record; 4 deny every other audience | Authorised administration sees the record; other audiences do not | None | No broad administrative browsing of private military state | none — a read or visibility check writes no ledger item | none — access logging is a Prompt 12 duty | N/A — a lawful access decision | moderators only | §12.2; Prompt 12 handoff |

### 13.15 Class M — Alliance, NAP and diplomacy boundaries

**13.15.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-097` | A same-Alliance declaration is refused and audited | M | REQ-669 | WFW-002 | WFE-049 | `WAR-011`, `WRF-07`, `AUD-AL-017` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-098` | A covered `AT-E01` pair blocks an operation | M | REQ-669 | WFW-002 | WFE-050 | `WAR-012`, `WRF-08`, `AUD-AL-017` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-099` | A client-declared NAP label has no effect | M | REQ-669 | WFW-002 | WFE-051 | `WAR-012`, `WAR-154` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-100` | A national NAP blocks only the declaration | M | REQ-668 | WFW-002 | — (national NAP §14.9) | `WAR-010`, `WRF-06` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-101` | A membership change is re-read at pre-P5 | M | REQ-669 | WFW-031 | WFE-052 | `WAR-011`, `WAR-012`, `WAR-013` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-102` | An Alliance cannot order, spend or declare | M | REQ-691 | WFW-007, WFW-018 | — (Alliance authority §2.1) | `WAR-001`, `WAR-151` | N/A — an authority rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-103` | ARL is not a military treasury | M | REQ-671, REQ-672 | WFW-020 | — (ARL boundary §12.2) | `WAR-148`, `WAR-151` | N/A — an authority rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-104` | An Alliance NAP cannot bind a withholding member | M | REQ-669 | WFW-036 | — (consent rule §12.3) | `WAR-012`, `WAR-151` | N/A — a consent rule, not arithmetic | COMPLETE | NOT RUN |

**13.15.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-097` | The declarer and the target share an active Alliance | Declare | OPEN | 1 read B-09 membership; 2 apply the same-Alliance block; 3 fail; 4 write the Alliance block record | `WRF-07`; `AUD-AL-017`; no OP moved | One `AUD-AL-017` record | No same-Alliance war, no Alliance override | none — the block writes an audit record, not a ledger item | `WRA-02`; `AUD-AL-017` | `WRF-07` | actor sees the rule and counterparty; moderators see the record | WFE-049; §10.2; B-09 |
| `WFA-098` | A covered `AT-E01` pair is selected | Submit an operation | OPEN | 1 run the canonical `AT-E01` check; 2 the pair is covered; 3 fail; 4 write the Alliance block record | `WRF-08`; `AUD-AL-017` | One `AUD-AL-017` record | No hostile operation across a covered NAP | none — the block writes an audit record, not a ledger item | `WRA-02`; `AUD-AL-017` | `WRF-08` | actor sees the rule; moderators see the record | WFE-050; §10.2 |
| `WFA-099` | A client labels an `AT-E00` as a NAP | Submit | OPEN | 1 ignore the client label; 2 consult only the canonical `AT-E01`; 3 admit or block on that result | The server ignores the label; only the canonical `AT-E01` check admits or blocks | Follows the canonical result | No client-declared treaty effect, no `AUD-AL-017` for `AT-E00` | none — the label is ignored before reservation | follows the canonical result; no `AUD-AL-017` | N/A — the label is ignored rather than failed | actor | WFE-051; §2.1, §11.5 item 2 |
| `WFA-100` | An active national `DP-T01` NAP exists | Declare | OPEN | 1 run the national NAP check; 2 the pair is covered; 3 fail; 4 leave existing campaigns and trade untouched | `WRF-06`; nothing reserved; existing campaigns and trade unaffected | None | No block on operations inside an existing campaign, no trade block | none — the NAP block rejects before any reservation | `WRA-02` | `WRF-06` | actor | WFW-002; §14.9 row 7 |
| `WFA-101` | A member leaves the Alliance between P2 and pre-P5 | Run pre-P5 | P5 | 1 re-read membership; 2 the same-Alliance block lifts; 3 an active `AT-E01` still blocks; 4 keep the checks separate and cumulative | Membership re-read; the same-Alliance block lifts; an active `AT-E01` still blocks | The operation follows the cumulative result | No cached membership result, no merged check | `HELD → RELEASED` if blocked | `WRA-02`; `AUD-AL-017` if `AT-E01` | `WRF-08` (when `AT-E01` applies) | actor | WFE-052; WFW-031; §2.5.1 |
| `WFA-102` | An Alliance attempts to issue an order or share OP | Submit through every surface | OPEN | 1 find no delegation surface; 2 find no shared pool; 3 find no automatic war entry; 4 reject | Refused; no delegated order, no shared OP, no automatic war entry | None | No Alliance command channel, no pooled OP | none — no delegated military value moves | none — no event is written for a refused alliance action | `WRF-01` | Alliance denied; actor and moderators see the attempt | §2.1, §15.4; WFW-007/018 |
| `WFA-103` | An Alliance requests a military treasury or member data | Request | P5 | 1 apply the ARL function boundary; 2 refuse payment, receipt, guarantee and brokerage; 3 refuse member data | Refused; ARL is not a military treasury; member data is not available | None | No Alliance payment, receipt, guarantee or brokerage | none — the Alliance ledger is not a military treasury | none — a refused read writes no event | N/A — the request is refused by scope | Alliance denied | §12.2; B-09 ARL |
| `WFA-104` | An Alliance NAP is proposed for a member | Withhold that member's consent | OPEN | 1 require per-member consent; 2 silence is not consent; 3 withhold the member; 4 allow the rest to opt in individually | The member is not covered; no inference from silence; the rest may opt in individually | Only consenting members are covered | No implied consent, no Alliance-wide binding without each nation's consent | none — consent coverage changes without a value transfer | none — consent records belong to B-09, not to a `WRA-` event | N/A — a consent outcome, not a failure | actor; the Alliance sees who opted in | §12.3, §15.4 |

### 13.16 Class N — cross-system integration B-02–B-09

**13.16.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-105` | Housing damage feeds next-turn crowding without casualties | N | REQ-701 | WFW-023 | WFE-053 | `WAR-109e`, B-05 `URB-157`, B-06 `DMP-031` | N/A — a cross-system recomputation, not a B-10 formula | COMPLETE | NOT RUN |
| `WFA-106` | Only infrastructure book value is impaired | N | REQ-702 | WFW-023 | WFE-054 | `WAR-109j`, B-05 `URB-118` | `F-WR-038` | COMPLETE | NOT RUN |
| `WFA-107` | War does not block trade | N | REQ-667 | WFW-007 | WFE-055 | B-07 `MKT-009`, `MKT-218` | N/A — an ownership rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-108` | Civilian Food is satisfied before military Food | N | REQ-662, REQ-695 | WFW-025, WFW-026 | — (Food priority §7.3) | B-04 `ECN-105`/`ECN-106`, `WAR-053c` | `F-WR-003`, `F-WR-036` | COMPLETE | NOT RUN |
| `WFA-109` | Force cap and type share are enforced | N | REQ-683, REQ-693 | WFW-028 | — (force cap §5.2) | `WAR-058`, `WAR-112`, `F-WR-012`, `WRF-24` | `F-WR-012`, `F-WR-013`, `F-WR-014` | COMPLETE | NOT RUN |
| `WFA-110` | Accepted fortification survives `TRANSITION` but a new raid does not | N | REQ-666 | WFW-032 | WFE-056 | B-06 `DMP-265`, `WAR-009g`, `WRF-09` | N/A — a political-state gate, not arithmetic | COMPLETE | NOT RUN |
| `WFA-111` | P4.1 repair commits before P5 damage | N | REQ-703 | WFW-030 | — (ordering §7.4) | B-05 `URB-157`, `WAR-109m` | `F-WR-038` | COMPLETE | NOT RUN |
| `WFA-112` | A full turn mutates only at the four commit points | N | REQ-654, REQ-655, REQ-656 | WFW-001, WFW-020, WFW-027 | — (phase ownership §2.4) | B-02 `TR-040`, `TR-050`, `TR-059` | N/A — a phase-ownership rule, not arithmetic | COMPLETE | NOT RUN |

**13.16.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-105` | A strike reduces infrastructure, capacity and housing | Run the next P3.8 | P3.7 | 1 P5 commits the damage; 2 the next P3.8 recomputes capacity and housing; 3 `DMP-031` crowding applies; 4 no casualty is generated | `DMP-031` crowding applies to the reduced capacity and housing; no casualties at P5 | Crowding state recomputed; no population removed | No population casualty, no instant crowding at P5 | none — crowding is recomputed without a ledger item | `WRA-08`; crowding is a B-06 event | N/A — a lawful integration | actor; infrastructure is public | WFE-053; WFW-023; B-05/B-06 |
| `WFA-106` | A strike impairs city book value | Run the next P3.8 | P3.7 | 1 apply damage only to the infrastructure subledger; 2 national wealth reflects `BV_post_P5`; 3 a 5,000-crown facility is unchanged | National wealth reflects `BV_post_P5`; a 5,000-crown facility is unchanged | Infrastructure subledger only | No facility damage, no double impairment | none — impairment changes book value without a resource movement | `WRA-08` | N/A — a lawful integration | actor | WFE-054; B-05 `URB-118` |
| `WFA-107` | A war is active | Run trade | P5 | 1 confirm war has no trade-ban effect; 2 only a B-08 embargo blocks; 3 one rule one owner | Trade continues; only a B-08 embargo blocks it | None by warfare | No automatic war trade ban, no duplicate owner | none — trade continues without a warfare ledger item | none — trade is a B-07 flow | N/A — a lawful integration | public market | WFE-055; B-07 |
| `WFA-108` | Civilian and military Food demand occur in one turn | Run P3.6 then P3.7 | P3.7 | 1 satisfy civilian Food at P3.6; 2 pay the military ration at rank 6(a); 3 pay upkeep at 6(b); 4 verify no double count | Civilian Food first and never reduced; military ration at 6(a), upkeep at 6(b); no double counting | Food debits and readiness upkeep | No military priority over civilians, no debt | none — the OP ledger is untouched; B-04 debits the ration and upkeep | `WRA-11` | N/A — a lawful priority | actor; the opponent sees a band | WFW-025/026; B-04 `ECN-105`/`ECN-106` |
| `WFA-109` | Recruitment would exceed the force cap or the type share | Submit | OPEN | 1 compute the force cap; 2 compute the type share; 3 read training turns; 4 fail the cap or share row | `WRF-24`; nothing reserved; arrival is timed by training turns | None on failure | No above-cap force, no early arrival | none — recruitment fails before any resource is committed | `WRA-02` | `WRF-24` | actor | WFW-028; §5.2 |
| `WFA-110` | `TRANSITION` begins after `FORTIFY` acceptance | Run pre-P5, then submit a raid | P5 | 1 the accepted defensive commitment is exempt from row 8; 2 `FORTIFY` resolves; 3 the new raid fails the political row | `FORTIFY` resolves under `WAR-009g`; the raid is refused `WRF-09` | Fortification resolves; the raid writes nothing | No new order, no cancellation of the accepted defensive commitment | fortification `HELD → CONSUMED`; raid none | `WRA-10`; `WRA-02` | `WRF-09` | actor | WFE-056; WFW-032; §2.5.1 |
| `WFA-111` | A repair is ordered at P4.1 and a strike resolves at P5 in the same turn | Run P4.1 then P5 | P4.1 | 1 commit the repair at P4.1; 2 apply the P5 damage; 3 confirm no retroactive heal | Repair commits before damage; no retroactive heal; ordering is visible in the timeline | Infrastructure repaired and then damaged | No P5 damage undone by a later repair | none — repair and damage settle through B-04, not the OP ledger | none for repair (B-05 ledger); `WRA-08` for the strike | N/A — a lawful ordering | actor; infrastructure is public | WFW-030; §7.4 |
| `WFA-112` | A full P0–P7 turn is audited at every mutation point | Audit every mutation point | OPEN | 1 mutations occur at acceptance while OPEN; 2 at P3.7; 3 at P4.1; 4 at P5; 5 no mutation at P0, P1, P2, P3 other than P3.7, P4 or P6; 6 the frozen baseline is honoured | Mutations only at acceptance while OPEN, P3.7, P4.1 and P5; the frozen baseline is honoured | At the four permitted commit points only | No mutation in P0, P1, P2, P3 other than P3.7, P4 or P6 | recorded at each commit point | `WRA-` events at the commit points | N/A — the invariant path | moderators; actors see their own | §2.4; B-02 `TR-040`, `TR-050`, `TR-059` |

### 13.17 Class O — security, abuse resistance and final acceptance

**13.17.1 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-113` | Hiding a control is not enforcement | O | REQ-678 | WFW-002 | WFE-057 | `WAR-009`, `WAR-152` | `F-WR-004` | COMPLETE | NOT RUN |
| `WFA-114` | A replay after a P2 failure is a new submission | O | REQ-657 | WFW-019, WFW-031 | WFE-058 | `WAR-097`, `WAR-013` | N/A — an idempotency rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-115` | A forged counterparty acceptance is refused | O | REQ-690 | WFW-036 | WFE-059 | `WAR-001`, `WRF-01` | N/A — an authority rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-116` | OP cannot be moved, pooled or purchased | O | REQ-681 | WFW-019 | WFE-060 | `WAR-040`, `WAR-001` | N/A — no such operation exists | COMPLETE | NOT RUN |
| `WFA-117` | Tampered cost, target or tier is recomputed | O | REQ-681, REQ-678 | WFW-007, WFW-018 | — (request tampering §11.4) | `WAR-041`, `WAR-009d` | `F-WR-019` | COMPLETE | NOT RUN |
| `WFA-118` | Shield-war slot filling is blocked | O | REQ-678 | WFW-001 | — (slot filling §11.4) | `WAR-007`, `WAR-008` | `F-WR-006` | COMPLETE | NOT RUN |
| `WFA-119` | Declare-and-void farming is unprofitable | O | REQ-679, REQ-681 | WFW-001, WFW-024 | — (declaration farming §11.4) | `WAR-005`, `WAR-008`, `WAR-028` | N/A — an economic rule, not arithmetic | COMPLETE | NOT RUN |
| `WFA-120` | Full scenario keeps every record consistent | O | all REQ-654–703 | WFW-001–040 | — (end-to-end scenario) | all B-10 rules | all 39 `F-WR-` formulas, shape only; calibration DEFERRED to Prompt 14 | COMPLETE | NOT RUN |

**13.17.2 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-113` | A client hides the attack control but the API is called directly | Submit directly | OPEN | 1 ignore the UI state; 2 run the server validator; 3 decide on server facts only | The server validator decides; the UI omission is not enforcement | Follows the server result | No client-only enforcement | `HELD` if accepted, `none` if rejected | `WRA-02` or `WRA-01` per result | `WRF-` code from the failing row; none waived | actor | WFE-057; §11.4 item 4 |
| `WFA-114` | A captured request is replayed with a new key after a P2 failure | Replay | P2 | 1 treat the new key as a new submission; 2 rerun every check; 3 keep the old action dead | Treated as a new submission; every check reruns; the old action is not revived | A new action if it passes; the old remains `FAILED` | No revival, no skipped revalidation | old `RELEASED`; new `HELD` | `WRA-02` (old); `WRA-03` (new) | `WRF-` code from the new submission; none waived | actor | WFE-058; §11.4 item 5 |
| `WFA-115` | A forged acceptance is submitted on behalf of the counterparty | Submit | OPEN | 1 resolve the session to its actor; 2 the actor is not the counterparty; 3 reject | `WRF-01`; nothing changes | None | No settlement accepted without the counterparty's own session | none — a forged acceptance is rejected before any record | none — rejected at submission; moderators see the attempt | `WRF-01` | actor; moderators | WFE-059; §11.4 item 6 |
| `WFA-116` | A request attempts to move OP to another nation or an Alliance pool | Submit every plausible shape | OPEN | 1 find no such operation in the catalogue; 2 reject each shape; 3 write no ledger item | No such operation exists; rejected with no ledger item | None | No transfer, no pool, no purchase | none — no such operation exists, so no ledger item | none — there is no operation to audit | N/A — the operation does not exist, so no `WRF-` code applies | actor | WFE-060; §11.4 item 11, §1.7 item 5 |
| `WFA-117` | A request tampers with cost, target or tier | Submit a forged body | OPEN | 1 recompute the cost server-side; 2 revalidate the target; 3 re-derive the tier; 4 treat client values as display only | The server values win | Follows the recomputed result | No trusted client cost, target or tier | `HELD` at the recomputed cost; `none` if rejected | `WRA-02` on rejection, otherwise the accepted action's event | `WRF-` code from the recomputed result | actor | §11.4 item 7 |
| `WFA-118` | A slot-filling or shield-war pattern is attempted | Attempt to fill both slots without a genuine campaign | OPEN | 1 enforce one outgoing and one incoming slot; 2 forbid joining; 3 refuse an empty-war reward; 4 audit the block | One outgoing and one incoming slot; no joining; no empty-war reward; the block is audited | Slot occupancy; block record | No empty-war reward, no third-party lockout | `none` when blocked; `HELD` for one admitted declaration | `WRA-02` | `WRF-10` | actor; moderators | §11.4 item 1 |
| `WFA-119` | A declare-and-void or no-op resolution loop is attempted | Loop the pattern | P7 | 1 the declaration cost is not refunded except for a server-caused failure; 2 no `REGENERATED` on void; 3 progress only from a resolved source | Declaration costs are not refunded except for a server-caused failure; no `REGENERATED` on void; progress only from a resolved source | The paid declaration cost is consumed; no regeneration | No OP or progress farming | declaration cost `CONSUMED`; no regeneration | `WRA-01`; `WRA-05` per declaration | N/A — the loop is lawful but unprofitable | actor; moderators | §11.4 items 2 and 10 |
| `WFA-120` | A complete scenario runs: declaration, raid, blockade, strike, settlement, P7 | Run end to end | P5 | 1 declaration; 2 raid; 3 blockade; 4 strike; 5 settlement; 6 P7 close; 7 every §6 record present; 8 `reserved = 0`; 9 one outcome; 10 audit immutable | Every record from §6 present and consistent; `reserved = 0`; the campaign ended with one outcome; audit immutable | All permitted commit points | No missing record, no orphan state, no double outcome | `HELD` → `CONSUMED`/`RELEASED`; final `reserved = 0` | all fourteen `WRA-` events where applicable | N/A — the positive end-to-end path | all audiences per §12.2 | §6, §8, §14 |

### 13.18 Class P — supplementary operation and lifecycle coverage

**13.18.1 Why this class exists.** Classes A–O were fixed at eight tests each when the matrix was first designed. A reverse-coverage pass found four workflows whose only inbound reference was the end-to-end scenario `WFA-120`: `WFW-008` (`OP-02 ASSAULT`), `WFW-009` (`OP-03 AIR_STRIKE`), `WFW-017` (amend or cancel an accepted operation) and `WFW-029` (P4 disbanding). An end-to-end scenario proves that a path can run; it does not prove an operation's own gates, counters or timing. Class P adds one dedicated record per gap. It does not replace, renumber or weaken any of `WFA-001`–`WFA-120`; it appends `WFA-121`–`WFA-124`.

**13.18.2 Identification.**

| ID | Test name | Class | Requirement | Workflow | Edge case | Rules | Formula | Definition | Execution |
|---|---|---|---|---|---|---|---|---|---|
| `WFA-121` | Assault enforces the 100-strength gate and applies `SHAKEN` only on a decisive result | P | REQ-684, REQ-688 | WFW-008 | — (operation path WFW-008; no §9 entry) | `WAR-045`, `WAR-073`, `WAR-084`, `WRF-23`, `WRF-24`, `WRF-25`, `WRF-26`, `WRF-35` | `F-WR-016`, `F-WR-019`, `F-WR-025`, `F-WR-027` | COMPLETE | NOT RUN |
| `WFA-122` | Air strike applies the `MIL-T3` and 20-air gates, never targets a city, and counts `INTERCEPT` once | P | REQ-684, REQ-688, REQ-693 | WFW-009 | — (operation path WFW-009; no §9 entry) | `WAR-055`, `WAR-073`, `WRF-23`, `WRF-24`, `WRF-25`, `WRF-26`, `WRF-35` | `F-WR-016`, `F-WR-026`, `F-WR-027` | COMPLETE | NOT RUN |
| `WFA-123` | Cancellation releases once; an amendment re-reserves atomically and only before the freeze | P | REQ-656, REQ-657 | WFW-017 | — (amendment window WFW-017; no §9 entry) | `WAR-005a`, `WAR-042`, `WAR-096`, `WRF-34` | `F-WR-002` | COMPLETE | NOT RUN |
| `WFA-124` | P4 disbanding reduces strength with no refund and cannot dodge a frozen battle | P | REQ-683, REQ-690 | WFW-029 | — (P4 window WFW-029; no §9 entry) | `WAR-060`, `WAR-136` | `F-WR-031` | COMPLETE | NOT RUN |

**13.18.3 Behaviour.**

| ID | Initial state | Input | Phase | Expected validation (ordered) | Expected output | Expected mutation | Expected no-mutation | Ledger | Audit | Failure code | Privacy | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WFA-121` | `ACTIVE` campaign; attacker readiness 500, INF strength exactly 100, two offensive slots used; defender active; 6 Food and the 10/10/2/0 bundle available | Submit `OP-02 ASSAULT` with campaign, target, key and confirmation; repeat with INF 99 | P5 | 1 run rows 1–11; 2 apply the INF ≥ 100 unit gate; 3 confirm no city row exists; 4 reserve 3 OP and the bundle; 5 revalidate at P2; 6 resolve one battle on full INF and ARM; 7 compute the tier and cap losses; 8 apply `SHAKEN` only on a decisive tier; 9 apply readiness −25 to both sides | 100 accepted with a battle report; 99 refused `WRF-24`; `SHAKEN` appears only on a decisive result | 3 OP `CONSUMED`; bundle consumed; losses applied; readiness −25 both sides; defender −100 more only on a decisive tier | No city or facility damage; no `SHAKEN` on a non-decisive tier; no third-party loss | `HELD` (3 OP) → `CONSUMED` | `WRA-04`, `WRA-06`, `WRA-07`, `WRA-14` | `WRF-23`, `WRF-24`, `WRF-25`, `WRF-26`, `WRF-35` | actor; defender; public summary; moderators | WFW-008; §4.5, §5.2; REQ-684 |
| `WFA-122` | `ACTIVE` campaign; attacker readiness 500, AIR 20, `MIL-T3`; one offensive slot free; defender has an armed `INTERCEPT`; no `RATION_SHORT` | Submit `OP-03 AIR_STRIKE`; repeat at AIR 19 and with a city in the body | P5 | 1 run rows 1–11; 2 apply the `MIL-T3` tier gate; 3 apply AIR ≥ 20; 4 reject any city target; 5 apply the single `INTERCEPT` counter (+40% defence, −15% attack); 6 resolve one battle; 7 charge air losses to the AIR pool | AIR 20 accepted; AIR 19 refused `WRF-24`; a city names `WRF-36`; `INTERCEPT` counted once | 3 OP `CONSUMED`; 10/6/0/1 bundle consumed; readiness −25; AIR losses applied | No city, facility or geographic damage; no stacked counter; no army or navy loss | `HELD` (3 OP) → `CONSUMED` | `WRA-04`, `WRA-06`, `WRA-07`, `WRA-14` | `WRF-23`, `WRF-24`, `WRF-25`, `WRF-26`, `WRF-35`, `WRF-36` | actor; defender; public summary; moderators | WFW-009; §4.6, §5.2; REQ-693 |
| `WFA-123` | A `RESERVED` `OP-01` with 2 OP and 500 crowns `HELD`; P1 has not frozen | Cancel it; then submit an amendment that changes the target with a new action key; then attempt an amendment after the freeze | OPEN | 1 authenticate the owner; 2 confirm `RESERVED` and pre-freeze; 3 cancellation releases once and writes `WRA-14`; 4 re-run the canonical validator on the amended form; 5 release the old reservation and reserve the new in one transaction; 6 allow exactly one terminal item per key; 7 refuse any change after the freeze | Cancellation leaves zero live reservations; the amendment holds the new amount; a post-freeze attempt changes nothing | `HELD` → `RELEASED` exactly once; a new `HELD` for the amended amount | No double release, no double reservation, no amendment after the freeze | `HELD` → `RELEASED`; new `HELD` | `WRA-03`, `WRA-14` | `WRF-34` only for a conflicting body under one key; a lawful amendment has no failure code | actor; moderators | WFW-017; §11.2, §11.3; REQ-656 |
| `WFA-124` | Strength exists; P4.1 has not completed; a battle has already committed in this P5 | Disband 10 INF at P4.1; then attempt a disband between two P5 battles; then attempt a disband that exceeds available strength | P4.1 | 1 authenticate the owner; 2 confirm the type and quantity ≤ available strength; 3 confirm P4.1 has not completed; 4 reduce strength before the P5 snapshot; 5 return no resources, crowns or OP; 6 refuse any disband between P5 battles | Strength reduced by 10; the frozen P5 baseline reflects it; the between-battles attempt is refused; the excess attempt changes nothing | Strength −10 before the snapshot | No refund of resources, crowns or OP; no avoidance of an already frozen battle | none — disbanding writes no OP item | none — `CAPEX` context only, no warfare event | N/A — timing and quantity are structural rules, not `WRF-` codes | actor; the counterparty sees only the resulting strength band | WFW-029; §2.4, §19; REQ-683 |

---

## 14. Bidirectional traceability

**14.1 Method.** Traceability is recorded in both directions, and both directions are machine-checked by `qa_backups/verify_warfare_workflows.py`.

- **Forward.** Every one of the 50 requirements (`REQ-654`–`REQ-703`), 230 `WAR-` identifiers (188 numbered plus 42 lettered), 39 formulas, 32 defined failure codes, 14 audit events, 25 architecture decisions, 34 conflict entries and 13 integration rows names at least one workflow and at least one test — except a row explicitly classified **DEFERRED**, which names its owner, future task and dependency instead.
- **Reverse.** Every one of the 40 workflows names at least one requirement and at least one rule and is exercised by at least one dedicated test (§14.3.3); every one of the 60 edge cases names a workflow and a test (§14.3.4); every one of the 124 tests names at least one workflow and at least one requirement (§14.3.5). A dash in a test's edge-case cell is an explicit statement that no §9 entry applies, never a silent omission.

The four dispositions are:

- **DIRECT VERIFICATION** — a test exercises the requirement's own wording and would fail if the behaviour changed.
- **SUPPORTING VERIFICATION** — the requirement is exercised indirectly through a contract owned elsewhere; the test proves the B-10 side of the seam, not the owner's policy.
- **DEFERRED** — the requirement is owned by a later prompt; 10C records the handoff and claims no verification.
- **NOT COVERED** — no relationship exists. **There are zero NOT COVERED rows** at the specification level; any future gap must be listed here, not silently omitted.

**14.1.1 Forward classification totals.** Of the 50 requirements, **44 are DIRECT VERIFICATION**, **1 is SUPPORTING VERIFICATION** (`REQ-672`, the threat-band query whose contract is owned by B-09 but whose B-10 side is tested by `WFA-044`), **5 are DEFERRED** (`REQ-673`–`REQ-677`, owned by Prompts 11–15 with the handoff recorded in §14.8.3) and **0 are NOT COVERED**.

**14.1.2 Reverse coverage totals.** 40 workflows, 60 edge cases, 124 tests. Four workflows (`WFW-008`, `WFW-009`, `WFW-017`, `WFW-029`) were exercised only by the end-to-end scenario before class P was added; `WFA-121`–`WFA-124` now give each a dedicated record. The reverse indices in §14.3.3–§14.3.5 are generated from the same records the validator parses, so a reference added to one side and not the other fails the build.


### 14.2 Requirements REQ-654–REQ-703

| REQ | Focus | Classification | Workflows | Tests |
|---|---|---|---|---|
| REQ-654 | Mutations only at acceptance, P3.7, P4.1, P5; no P0/P7 regeneration | DIRECT VERIFICATION | WFW-001, 004, 027, 040 | WFA-112, WFA-039 |
| REQ-655 | Frozen baseline, total order key, one seed, replay identical | DIRECT VERIFICATION | WFW-020, 040 | WFA-046, WFA-083, WFA-084 |
| REQ-656 | Reserve at acceptance; revalidate P2 and pre-P5; release once | DIRECT VERIFICATION | WFW-018, 031 | WFA-031, WFA-070 |
| REQ-657 | Client idempotency key; resolution keys; no second item | DIRECT VERIFICATION | WFW-019, 040 | WFA-081, WFA-082 |
| REQ-658 | B-03 protection and restricted pairs on every path | DIRECT VERIFICATION | WFW-002, 031 | WFA-009, WFA-015, WFA-079 |
| REQ-659 | Dormancy suspends, fails pending, 48 suspended turns `ABANDONED` | DIRECT VERIFICATION | WFW-005, 006 | WFA-023, WFA-073, WFA-077 |
| REQ-660 | Reroll block; surrender off-ramp; recorded signal | DIRECT VERIFICATION | WFW-033, 037 | WFA-075, WFA-076, WFA-080 |
| REQ-661 | Closed 11-resource roster and registered ledger types | DIRECT VERIFICATION | WFW-016, 027 | WFA-040 |
| REQ-662 | Upkeep at `ECN-105` rank 6; cancel never debt; −100 readiness | DIRECT VERIFICATION | WFW-026 | WFA-108 |
| REQ-663 | Immediate P5 reparations within caps; atomic failure | DIRECT VERIFICATION | WFW-038, 039 | WFA-060, WFA-087 |
| REQ-664 | No city/facility destruction, no population casualty; exception bounded | DIRECT VERIFICATION | WFW-023 | WFA-051 |
| REQ-665 | No military building or Military research branch | DIRECT VERIFICATION | WFW-028 | WFA-109 |
| REQ-666 | Political block; narrow defensive exemption; offensive fails | DIRECT VERIFICATION | WFW-032 | WFA-110 |
| REQ-667 | War does not block trade | DIRECT VERIFICATION | WFW-007, 010 | WFA-107 |
| REQ-668 | National `DP-T01` blocks declaration only | DIRECT VERIFICATION | WFW-002 | WFA-100 |
| REQ-669 | Same-Alliance and `AT-E01` blocks, independent, `AUD-AL-017` | DIRECT VERIFICATION | WFW-002, 031 | WFA-097, WFA-098, WFA-101 |
| REQ-670 | Alliance has no military visibility or roster surface | DIRECT VERIFICATION | WFW-020 | WFA-090 |
| REQ-671 | ARL is not a military treasury | DIRECT VERIFICATION | WFW-020 | WFA-103 |
| REQ-672 | D-027 aggregates: k = 5, no private per-nation value | **SUPPORTING VERIFICATION** — B-10 supplies the rule; Prompt 12/13 own publication policy | WFW-020 | WFA-089, WFA-091 |
| REQ-673 | Prompt 11 handoff: war events, objective totals, outcomes, settlements, ranking inputs | **DEFERRED** — Prompt 11 owns world events and rankings | WFW-024 | WFA-120 (event set only) |
| REQ-674 | Prompt 12 handoff: evidence fields, block records, audit duties, abuse taxonomy | **DEFERRED** — Prompt 12 owns fair-play policy | WFW-002, 040 | WFA-092 (record shape only) |
| REQ-675 | Prompt 13 handoff: board content, confirmation minimum, bands, failure copy | **DEFERRED** — Prompt 13 owns the interface | WFW-001, 007, 020 | WFA-007 (content floor only) |
| REQ-676 | Prompt 14 handoff: all 39 formulas and provisional values | **DEFERRED** — Prompt 14 owns calibration | WFW-020, 021, 025 | WFA-048 (shape only) |
| REQ-677 | Prompt 15 handoff: integration matrix, registers, conflicts | **DEFERRED** — Prompt 15 owns Bible assembly | all | WFA-120 (reference integrity only) |
| REQ-678 | Owner-only unilateral declaration; 12 checks; immutable objectives | DIRECT VERIFICATION | WFW-001, 002 | WFA-016, WFA-001 |
| REQ-679 | Exactly six mapless objectives; 0…1,000; public and capped | DIRECT VERIFICATION | WFW-024 | WFA-012, WFA-024 |
| REQ-680 | Seven states, one outcome; 84+42; 24/48; dormancy 48 | DIRECT VERIFICATION | WFW-006 | WFA-017, WFA-020, WFA-024 |
| REQ-681 | One national OP pool; formula; cap; carry; idempotent regeneration | DIRECT VERIFICATION | WFW-027, 040 | WFA-035, WFA-039, WFA-040 |
| REQ-682 | Readiness 0…1,000, gates 300/500, not purchasable | DIRECT VERIFICATION | WFW-022 | WFA-031, WFA-054 |
| REQ-683 | Four strength pools; force cap; training; share; bounded losses | DIRECT VERIFICATION | WFW-021, 028 | WFA-049, WFA-109 |
| REQ-684 | Closed nine-operation catalogue with declared fields | DIRECT VERIFICATION | WFW-007–016 | WFA-025 |
| REQ-685 | Deterministic power + ±500 bp; five tiers; bands; report | DIRECT VERIFICATION | WFW-020 | WFA-041, WFA-048 |
| REQ-686 | Supply reserved/consumed; no geography; capped combined surcharge | DIRECT VERIFICATION | WFW-007, 010, 015 | WFA-033, WFA-069 |
| REQ-687 | No new protection; B-03 enforced and rechecked | DIRECT VERIFICATION | WFW-031 | WFA-070, WFA-071 |
| REQ-688 | Every offensive has a counter; no stacking; no infinite lock | DIRECT VERIFICATION | WFW-013, 014, 015 | WFA-065, WFA-068 |
| REQ-689 | Bounded losses; no loot; reparations move existing value | DIRECT VERIFICATION | WFW-021, 023 | WFA-049, WFA-053 |
| REQ-690 | Eight-state settlement, six terms, no debt, atomic enforcement | DIRECT VERIFICATION | WFW-034–039 | WFA-057, WFA-058, WFA-064 |
| REQ-691 | No Alliance order, movement, attack, spend or declaration | DIRECT VERIFICATION | WFW-007, 018 | WFA-002, WFA-102 |
| REQ-692 | Explicit confirmation; no default; no private leak | DIRECT VERIFICATION | WFW-001, 020 | WFA-094, WFA-007 |
| REQ-693 | Four development tiers gate capability; no separate branch | DIRECT VERIFICATION | WFW-028 | WFA-109 |
| REQ-694 | Soldier-equivalents and canonical force snapshot | DIRECT VERIFICATION | WFW-025, 027 | WFA-034 |
| REQ-695 | Military demand separate; civilian priority; protected requirement | DIRECT VERIFICATION | WFW-025 | WFA-108 |
| REQ-696 | Whole ration obligation at rank 6(a); no debt; no reservation seizure | DIRECT VERIFICATION | WFW-025 | WFA-034 |
| REQ-697 | `OP-09` 4 Food only from eligible surplus; released under `WRF-25` | DIRECT VERIFICATION | WFW-016 | WFA-036, WFA-037 |
| REQ-698 | Each Food unit debited once; distinct event keys | DIRECT VERIFICATION | WFW-025, 026 | WFA-037, WFA-108 |
| REQ-699 | City-targeted `OP-05`; national checks first; city check last | DIRECT VERIFICATION | WFW-012 | WFA-027, WFA-030 |
| REQ-700 | Damage formula, floor 10, 30% campaign cap, atomic write | DIRECT VERIFICATION | WFW-023 | WFA-051, WFA-055 |
| REQ-701 | Capacity and housing recomputed next turn; no casualties | DIRECT VERIFICATION | WFW-023 | WFA-105 |
| REQ-702 | Only the infrastructure subledger is impaired | DIRECT VERIFICATION | WFW-023 | WFA-106 |
| REQ-703 | Repair 1–10 levels, stepped cost, 500 cap, P4.1 before P5 | DIRECT VERIFICATION | WFW-030 | WFA-052, WFA-056, WFA-111 |

**Totals:** 50 rows = 44 DIRECT VERIFICATION + 1 SUPPORTING VERIFICATION (`REQ-672`) + 5 DEFERRED (`REQ-673`–`REQ-677`) + 0 NOT COVERED.

### 14.3 Every numbered WAR rule

The 188 numbered rules are covered by contiguous section ranges. Each range names the workflows and tests that exercise it; a rule inside a range is covered when the range's workflow executes the behaviour the rule constrains. No range is an orphan.

| Rule range | Subject | Workflows | Representative tests |
|---|---|---|---|
| `WAR-001`–`WAR-014` | Authority, declaration eligibility, canonical validator, NAP and Alliance blocks | WFW-001, 002, 018 | WFA-001, 016, 097, 098 |
| `WAR-015`–`WAR-031` | Campaign states, deadlines, dormancy, reroll, termination | WFW-004, 005, 006, 033 | WFA-017–024, 073–078 |
| `WAR-032`–`WAR-038` | Six objectives, progress, victory and outcome | WFW-024, 006 | WFA-012, 017, 024 |
| `WAR-039`–`WAR-046` | OP pool, availability, regeneration, acceptance, limits | WFW-018, 027 | WFA-035, 039, 040 |
| `WAR-047`–`WAR-053` | Readiness, gates, recovery, upkeep | WFW-022, 026 | WFA-031, 054, 108 |
| `WAR-054`–`WAR-061` | Force pools, caps, training, unit types | WFW-028, 021 | WFA-049, 109 |
| `WAR-062`–`WAR-067` | Recruitment, arrival, disbanding | WFW-028, 029 | WFA-109 |
| `WAR-068`–`WAR-072` | Supply bundles and the combined modifier | WFW-007–016 | WFA-033, 036 |
| `WAR-073` | Reservation versus obligation precedence | WFW-025, 026 | WFA-034, 108 |
| `WAR-074`–`WAR-088` | Operation catalogue, prerequisites, effects, counters, battle inputs | WFW-007–016 | WFA-025–032, 041–048 |
| `WAR-089`–`WAR-100` | P5 internal order, baseline, idempotency, recovery | WFW-020, 040 | WFA-042, 046, 083, 084 |
| `WAR-101`–`WAR-109` | Losses, readiness loss, caps, city damage | WFW-021, 022, 023 | WFA-049–055 |
| `WAR-110`–`WAR-114` | Readiness and force recovery, repair | WFW-026, 030 | WFA-054, 056 |
| `WAR-115`–`WAR-120` | Protection, counters and counter stacking | WFW-031, 013, 014, 015 | WFA-065–071 |
| `WAR-121`–`WAR-124` | Ceasefire | WFW-034 | WFA-057 |
| `WAR-125`–`WAR-136` | Settlement object, terms, windows | WFW-035, 036, 038 | WFA-058, 061 |
| `WAR-137`–`WAR-141` | Reparations, surrender, enforcement | WFW-037, 038, 039 | WFA-060, WFA-063, WFA-064 |
| `WAR-142`–`WAR-147` | Postwar recovery, re-entry, permanent record | WFW-006, 033 | WFA-077, WFA-078 |
| `WAR-148`–`WAR-152` | Visibility, privacy, sovereignty, confirmation | WFW-001, 020, 025 | WFA-089–096, WFA-007 |
| `WAR-153`–`WAR-155` | Audit events, `AUD-AL-017` scope, audit access | WFW-020, 040 | WFA-092, WFA-094, WFA-096 |
| `WAR-156`–`WAR-163` | Integration contracts and invariants | `WFW-001`–`WFW-040` | WFA-105–112 |
| `WAR-164`–`WAR-166` | Food integration | WFW-025, 026 | WFA-108 |
| `WAR-167`–`WAR-176` | City infrastructure integration | WFW-023, 030 | WFA-105–107, 111 |
| `WAR-177`–`WAR-180` | Settlement and postwar integration | WFW-038 | WFA-060 |
| `WAR-181`–`WAR-182` | 10C handoff and downstream boundary | `WFW-001`–`WFW-040` | WFA-120 |
| `WAR-183`–`WAR-188` | Completion, limitations, open items | WFW-040 | WFA-120 |

**14.3.1 The 42 lettered sub-rules.** Every lettered rule is listed individually because each carries distinct semantics that a range cannot absorb.

| Sub-rule | Subject | Workflow | Test |
|---|---|---|---|
| `WAR-005a` | Acceptance state is `ACCEPTED` while OPEN before P1 freeze | WFW-001 | WFA-008 |
| `WAR-009a` | One canonical validator, twelve checks, cumulative | WFW-002 | WFA-016 |
| `WAR-009b` | Check order and short-circuit reporting | WFW-002 | WFA-014 |
| `WAR-009c` | Revalidation points at P2 and pre-P5 | WFW-031 | WFA-070 |
| `WAR-009d` | Blocked action executes nothing | WFW-018 | WFA-001 |
| `WAR-009e` | `AUD-AL-017` only for checks 6 and 7 | WFW-002 | WFA-092 |
| `WAR-009f` | No waiver by retry, client or administration | WFW-002 | WFA-113 |
| `WAR-009g` | Defensive-commitment exemption from row 8 only | WFW-032 | WFA-110 |
| `WAR-043a` | P7 void and release of unresolved actions | WFW-040 | WFA-085 |
| `WAR-043b` | P7 verifies `reserved = 0` before publication | WFW-040 | WFA-086 |
| `WAR-053a` | Soldier-equivalent weights | WFW-025 | WFA-034 |
| `WAR-053b` | Demand rounding and canonical snapshot | WFW-025, 027 | WFA-034 |
| `WAR-053c` | Civilian priority and timing | WFW-025 | WFA-108 |
| `WAR-053d` | Whole-obligation payment or cancellation | WFW-025 | WFA-034 |
| `WAR-053e` | `RATION_SHORT` consequences and recovery | WFW-025 | WFA-034 |
| `WAR-053f` | `OP-09` is distinct from garrison ration | WFW-016 | WFA-036 |
| `WAR-053g` | No double counting of Food | WFW-025, 026 | WFA-037 |
| `WAR-053h` | Visibility and audit of the ration | WFW-025 | WFA-093 |
| `WAR-053i` | No debt and no seizure of another reservation | WFW-025 | WFA-034 |
| `WAR-053j` | Ration ordering against other obligations | WFW-026 | WFA-108 |
| `WAR-053k` | Political check is `WAR-009` row 8 | WFW-032 | WFA-110 |
| `WAR-053l` | Protected civilian requirement and eligible `OP-09` surplus | WFW-016, 025 | WFA-036, 037 |
| `WAR-053m` | Canonical P3.7 force snapshot | WFW-027 | WFA-039 |
| `WAR-064a` | Training turns by unit type | WFW-028 | WFA-109 |
| `WAR-064b` | Arrival at the opening of P3.7 | WFW-028 | WFA-109 |
| `WAR-071a` | Supply reserved at acceptance, consumed at P5 | WFW-007 | WFA-033 |
| `WAR-109a` | `OP-05` may name a city asset target | WFW-012 | WFA-026 |
| `WAR-109b` | National checks first, city check last | WFW-012 | WFA-030 |
| `WAR-109c` | City target validity conditions | WFW-012 | WFA-027 |
| `WAR-109d` | Damage is infrastructure only | WFW-023 | WFA-051 |
| `WAR-109e` | Capacity and housing boundaries | WFW-023 | WFA-105 |
| `WAR-109f` | Facilities preserved | WFW-023 | WFA-106 |
| `WAR-109g` | Per-city per-campaign cap | WFW-023 | WFA-055 |
| `WAR-109h` | Floor of 10 and zero-damage resolution | WFW-023 | WFA-051 |
| `WAR-109i` | Damage formula and headroom | WFW-023 | WFA-051 |
| `WAR-109j` | Book-value impairment only on the infrastructure subledger | WFW-023 | WFA-106 |
| `WAR-109k` | Visibility and audit of a strike | WFW-023 | WFA-095 |
| `WAR-109l` | `WRF-36` for invalid city, `WRF-37` for invalid repair | WFW-012, 030 | WFA-027, 052 |
| `WAR-109m` | P4.1 before P5; no retroactive repair | WFW-030 | WFA-111 |
| `WAR-116a` | Protection becoming active after P2 fails at pre-P5 | WFW-031 | WFA-070 |
| `WAR-163a` | Integration invariant: one mutation owner per phase | WFW-040 | WFA-112 |
| `WAR-163b` | Integration invariant: reservation conservation across systems | WFW-027 | WFA-040 |

**14.3.2 Numbered-rule completeness.** 188 numbered + 42 lettered = **230 WAR identifiers**, all inside the ranges or named individually above. The validator recomputes both counts from B-10 and fails if either drifts.

**14.3.3 Reverse workflow index.** Every one of the forty workflows is exercised by at least one test. The table names the tests, the requirements those tests disposition, and the WAR rules they cite. `WFA-120` exercises every workflow end to end (§13.17) and is recorded once there rather than repeated in every row.

| Workflow | Name | Tests | Requirements via those tests | WAR rules cited |
|---|---|---|---|---|
| `WFW-001` | Declare war | `WFA-001`, `WFA-004`, `WFA-006`, `WFA-007`, `WFA-011`, `WFA-012`, `WFA-016`, `WFA-059`, `WFA-112`, `WFA-118`, `WFA-119` | `REQ-654`–`REQ-656`, `REQ-678`–`REQ-679`, `REQ-681`, `REQ-690`–`REQ-691` | `WAR-001`–`WAR-002`, `WAR-005`–`WAR-009`, `WAR-028`, `WAR-135`, `WAR-151` |
| `WFW-002` | Declaration rejected | `WFA-001`, `WFA-009`, `WFA-010`, `WFA-013`, `WFA-014`, `WFA-015`, `WFA-079`, `WFA-092`, `WFA-097`, `WFA-098`, `WFA-099`, `WFA-100`, `WFA-113` | `REQ-654`, `REQ-658`–`REQ-659`, `REQ-668`–`REQ-669`, `REQ-678`, `REQ-687` | `WAR-001`–`WAR-003`, `WAR-009`–`WAR-012`, `WAR-014`, `WAR-115`–`WAR-116`, `WAR-152`, `WAR-154` |
| `WFW-003` | Withdraw a pending declaration | `WFA-008` | `REQ-678` | `WAR-003`, `WAR-005` |
| `WFW-004` | Campaign activation at P5.1 | `WFA-020` | `REQ-680` | `WAR-016`–`WAR-017` |
| `WFW-005` | Campaign suspended by dormancy | `WFA-023`, `WFA-073` | `REQ-659` | `WAR-021`–`WAR-022` |
| `WFW-006` | Expiry, abandonment and stalemate termination | `WFA-017`, `WFA-018`, `WFA-019`, `WFA-021`, `WFA-022`, `WFA-024`, `WFA-077`, `WFA-078` | `REQ-659`–`REQ-660`, `REQ-680`, `REQ-690` | `WAR-018`–`WAR-019`, `WAR-023`–`WAR-026`, `WAR-028`–`WAR-029`, `WAR-125` |
| `WFW-007` | `OP-01 RAID` | `WFA-002`, `WFA-033`, `WFA-102`, `WFA-107`, `WFA-117` | `REQ-667`, `REQ-678`, `REQ-681`, `REQ-686`, `REQ-691` | `WAR-001`, `WAR-009`, `WAR-041`, `WAR-068`, `WAR-151` |
| `WFW-008` | `OP-02 ASSAULT` | `WFA-121` | `REQ-684`, `REQ-688` | `WAR-045`, `WAR-073`, `WAR-084` |
| `WFW-009` | `OP-03 AIR_STRIKE` | `WFA-122` | `REQ-684`, `REQ-688`, `REQ-693` | `WAR-055`, `WAR-073` |
| `WFW-010` | `OP-04 BLOCKADE` | `WFA-029`, `WFA-033`, `WFA-072` | `REQ-686` | `WAR-068`, `WAR-083`, `WAR-118` |
| `WFW-011` | `OP-05 MISSILE_STRIKE` (nation target) | `WFA-025`, `WFA-026`, `WFA-047` | `REQ-684`, `REQ-693`, `REQ-699` | `WAR-045`–`WAR-046`, `WAR-080`, `WAR-109` |
| `WFW-012` | `OP-05 MISSILE_STRIKE` (city target) | `WFA-026`, `WFA-027`, `WFA-028`, `WFA-030` | `REQ-699` | `WAR-109` |
| `WFW-013` | `OP-06 INTERCEPT` | `WFA-066` | `REQ-688` | `WAR-095`, `WAR-118` |
| `WFW-014` | `OP-07 FORTIFY` | `WFA-032`, `WFA-065` | `REQ-688` | `WAR-098`, `WAR-100` |
| `WFW-015` | `OP-08 BREAK_BLOCKADE` | `WFA-067`, `WFA-069`, `WFA-072` | `REQ-686`, `REQ-688` | `WAR-083`, `WAR-089`, `WAR-118` |
| `WFW-016` | `OP-09 RESUPPLY` | `WFA-036`, `WFA-037`, `WFA-038` | `REQ-688`, `REQ-697` | `WAR-051`, `WAR-053` |
| `WFW-017` | Amend or cancel an accepted operation | `WFA-123` | `REQ-656`–`REQ-657` | `WAR-005`, `WAR-042`, `WAR-096` |
| `WFW-018` | Operation rejection and reservation release | `WFA-002`, `WFA-031`, `WFA-035`, `WFA-102`, `WFA-117` | `REQ-678`, `REQ-681`–`REQ-682`, `REQ-691` | `WAR-001`, `WAR-009`, `WAR-041`–`WAR-042`, `WAR-048`, `WAR-151` |
| `WFW-019` | Duplicate submission and idempotent replay | `WFA-004`, `WFA-081`, `WFA-082`, `WFA-114`, `WFA-116` | `REQ-657`, `REQ-678`, `REQ-681` | `WAR-001`, `WAR-005`, `WAR-007`, `WAR-013`, `WAR-040`, `WAR-042`, `WAR-097` |
| `WFW-020` | Resolve one battle | `WFA-003`, `WFA-041`, `WFA-042`, `WFA-043`, `WFA-044`, `WFA-045`, `WFA-046`, `WFA-048`, `WFA-068`, `WFA-089`, `WFA-090`, `WFA-091`, `WFA-094`, `WFA-095`, `WFA-103`, `WFA-112` | `REQ-654`–`REQ-656`, `REQ-670`–`REQ-672`, `REQ-685`, `REQ-688`, `REQ-692` | `WAR-079`, `WAR-081`–`WAR-086`, `WAR-088`, `WAR-091`–`WAR-092`, `WAR-119`–`WAR-120`, `WAR-147`–`WAR-148`, `WAR-150`–`WAR-151`, `WAR-153`–`WAR-155` |
| `WFW-021` | Apply losses and caps | `WFA-042`, `WFA-049`, `WFA-050`, `WFA-053` | `REQ-685`, `REQ-689` | `WAR-091`–`WAR-092`, `WAR-104`–`WAR-105`, `WAR-109` |
| `WFW-022` | Readiness loss and temporary states | `WFA-054` | `REQ-682` | `WAR-106`, `WAR-110` |
| `WFW-023` | Apply city infrastructure damage and impairment | `WFA-051`, `WFA-055`, `WFA-105`, `WFA-106` | `REQ-700`–`REQ-702` | `WAR-109` |
| `WFW-024` | Objective progress and counter-progress | `WFA-119` | `REQ-679`, `REQ-681` | `WAR-005`, `WAR-008`, `WAR-028` |
| `WFW-025` | P3.7 military Food ration | `WFA-034`, `WFA-037`, `WFA-093`, `WFA-094`, `WFA-108` | `REQ-662`, `REQ-672`, `REQ-692`, `REQ-695`–`REQ-697` | `WAR-053`, `WAR-149`, `WAR-153`–`WAR-155` |
| `WFW-026` | P3.7 readiness upkeep | `WFA-108` | `REQ-662`, `REQ-695` | `WAR-053` |
| `WFW-027` | P3.7 OP regeneration and force snapshot | `WFA-039`, `WFA-040`, `WFA-088`, `WFA-112` | `REQ-654`–`REQ-656`, `REQ-681` | `WAR-040`, `WAR-043` |
| `WFW-028` | P4 recruitment | `WFA-109` | `REQ-683`, `REQ-693` | `WAR-058`, `WAR-112` |
| `WFW-029` | P4 disbanding | `WFA-124` | `REQ-683`, `REQ-690` | `WAR-060`, `WAR-136` |
| `WFW-030` | P4.1 city infrastructure repair | `WFA-052`, `WFA-056`, `WFA-111` | `REQ-703` | `WAR-109`, `WAR-114` |
| `WFW-031` | Protection becomes active between P2 and P5 | `WFA-009`, `WFA-010`, `WFA-031`, `WFA-070`, `WFA-071`, `WFA-074`, `WFA-101`, `WFA-114` | `REQ-657`–`REQ-659`, `REQ-668`–`REQ-669`, `REQ-682`, `REQ-687` | `WAR-003`, `WAR-009`–`WAR-013`, `WAR-048`, `WAR-097`, `WAR-116` |
| `WFW-032` | Political `TRANSITION` or `CRISIS` interaction | `WFA-110` | `REQ-666` | `WAR-009` |
| `WFW-033` | Reroll request during a campaign | `WFA-075`, `WFA-076`, `WFA-078` | `REQ-660` | `WAR-028`–`WAR-030` |
| `WFW-034` | Propose a mutual ceasefire | `WFA-057` | `REQ-690` | `WAR-121`–`WAR-124` |
| `WFW-035` | Propose a settlement with terms | `WFA-058`, `WFA-061` | `REQ-690` | `WAR-122`, `WAR-126`–`WAR-130` |
| `WFW-036` | Respond to a settlement | `WFA-005`, `WFA-061`, `WFA-062`, `WFA-104`, `WFA-115` | `REQ-669`, `REQ-690` | `WAR-001`, `WAR-012`, `WAR-122`, `WAR-138`, `WAR-151` |
| `WFW-037` | Surrender | `WFA-063`, `WFA-080` | `REQ-660`, `REQ-690` | `WAR-028`, `WAR-139`–`WAR-140` |
| `WFW-038` | Settlement completion at P5.3 | `WFA-018`, `WFA-064` | `REQ-690` | `WAR-019`, `WAR-125`, `WAR-136`–`WAR-137` |
| `WFW-039` | Settlement atomic failure | `WFA-060`, `WFA-087` | `REQ-663`, `REQ-690` | `WAR-138` |
| `WFW-040` | Interrupted P5 recovery and P7 close | `WFA-003`, `WFA-040`, `WFA-083`, `WFA-084`, `WFA-085`, `WFA-086`, `WFA-096` | `REQ-655`, `REQ-681`, `REQ-692` | `WAR-040`, `WAR-043`, `WAR-099`–`WAR-100`, `WAR-151`, `WAR-155` |

**14.3.4 Reverse edge-case index.** Each of the sixty edge cases names the workflow it constrains and the test that proves it. Three edge cases (`WFE-030`, `WFE-037`, `WFE-039`) are additionally cited by a second test that exercises the same boundary from another class; the primary test is the one named in §9.

| Edge case | Class | Primary test | Also cited by | Workflows |
|---|---|---|---|---|
| `WFE-001` | A | `WFA-001` | — | WFW-001, WFW-002 |
| `WFE-002` | A | `WFA-002` | — | WFW-007, WFW-018 |
| `WFE-003` | A | `WFA-003` | — | WFW-020, WFW-040 |
| `WFE-004` | A | `WFA-004` | — | WFW-001, WFW-019 |
| `WFE-005` | B | `WFA-009` | — | WFW-002, WFW-031 |
| `WFE-006` | B | `WFA-010` | — | WFW-002, WFW-031 |
| `WFE-007` | B | `WFA-011` | — | WFW-001 |
| `WFE-008` | B | `WFA-012` | — | WFW-001 |
| `WFE-009` | C | `WFA-017` | — | WFW-006 |
| `WFE-010` | C | `WFA-018` | — | WFW-038, WFW-006 |
| `WFE-011` | C | `WFA-019` | — | WFW-006 |
| `WFE-012` | J | `WFA-076` | — | WFW-033 |
| `WFE-013` | D | `WFA-030` | — | WFW-012 |
| `WFE-014` | D | `WFA-029` | — | WFW-010 |
| `WFE-015` | D | `WFA-032` | — | WFW-014 |
| `WFE-016` | E | `WFA-038` | — | WFW-016 |
| `WFE-017` | E | `WFA-033` | — | WFW-007, WFW-010 |
| `WFE-018` | E | `WFA-034` | — | WFW-025 |
| `WFE-019` | E | `WFA-036` | — | WFW-016 |
| `WFE-020` | E | `WFA-037` | — | WFW-016, WFW-025 |
| `WFE-021` | F | `WFA-041` | — | WFW-020 |
| `WFE-022` | F | `WFA-042` | — | WFW-020, WFW-021 |
| `WFE-023` | F | `WFA-043` | — | WFW-020 |
| `WFE-024` | F | `WFA-044` | — | WFW-020 |
| `WFE-025` | G | `WFA-049` | — | WFW-021 |
| `WFE-026` | G | `WFA-050` | — | WFW-021 |
| `WFE-027` | G | `WFA-051` | — | WFW-023 |
| `WFE-028` | G | `WFA-052` | — | WFW-030 |
| `WFE-029` | H | `WFA-060` | — | WFW-039 |
| `WFE-030` | H | `WFA-061` | `WFA-005` | WFW-035, WFW-036 |
| `WFE-031` | H | `WFA-064` | — | WFW-038 |
| `WFE-032` | H | `WFA-063` | — | WFW-037 |
| `WFE-033` | I | `WFA-070` | — | WFW-031 |
| `WFE-034` | I | `WFA-071` | — | WFW-031 |
| `WFE-035` | I | `WFA-069` | — | WFW-015 |
| `WFE-036` | J | `WFA-076` | — | WFW-033 |
| `WFE-037` | J | `WFA-073` | `WFA-023` | WFW-005 |
| `WFE-038` | J | `WFA-074` | — | WFW-031 |
| `WFE-039` | J | `WFA-077` | `WFA-024` | WFW-006 |
| `WFE-040` | J | `WFA-078` | — | WFW-006, WFW-033 |
| `WFE-041` | K | `WFA-081` | — | WFW-019 |
| `WFE-042` | K | `WFA-083` | — | WFW-040 |
| `WFE-043` | K | `WFA-084` | — | WFW-040 |
| `WFE-044` | K | `WFA-086` | — | WFW-040 |
| `WFE-045` | L | `WFA-089` | — | WFW-020 |
| `WFE-046` | L | `WFA-090` | — | WFW-020 |
| `WFE-047` | L | `WFA-091` | — | WFW-020 |
| `WFE-048` | L | `WFA-092` | — | WFW-002 |
| `WFE-049` | M | `WFA-097` | — | WFW-002 |
| `WFE-050` | M | `WFA-098` | — | WFW-002 |
| `WFE-051` | M | `WFA-099` | — | WFW-002 |
| `WFE-052` | M | `WFA-101` | — | WFW-031 |
| `WFE-053` | N | `WFA-105` | — | WFW-023 |
| `WFE-054` | N | `WFA-106` | — | WFW-023 |
| `WFE-055` | N | `WFA-107` | — | WFW-007 |
| `WFE-056` | N | `WFA-110` | — | WFW-032 |
| `WFE-057` | O | `WFA-113` | — | WFW-002 |
| `WFE-058` | O | `WFA-114` | — | WFW-019, WFW-031 |
| `WFE-059` | O | `WFA-115` | — | WFW-036 |
| `WFE-060` | O | `WFA-116` | — | WFW-019 |

**14.3.5 Reverse test index.** Each of the 124 tests names its class, the workflow(s) it verifies, the edge case it discharges where one applies, and the requirements it dispositions. A dash in the edge-case column is an explicit statement that the test verifies a positive, boundary or contract path rather than an entry in the §9 register.

| Test | Class | Workflows | Edge case | Requirements |
|---|---|---|---|---|
| `WFA-001` | A | `WFW-001`–`WFW-002` | `WFE-001` | `REQ-654`, `REQ-678` |
| `WFA-002` | A | `WFW-007`, `WFW-018` | `WFE-002` | `REQ-691` |
| `WFA-003` | A | `WFW-020`, `WFW-040` | `WFE-003` | `REQ-692` |
| `WFA-004` | A | `WFW-001`, `WFW-019` | `WFE-004` | `REQ-678` |
| `WFA-005` | A | `WFW-036` | `WFE-030` | `REQ-690` |
| `WFA-006` | A | `WFW-001` | — | `REQ-691` |
| `WFA-007` | A | `WFW-001` | — | `REQ-678` |
| `WFA-008` | A | `WFW-003` | — | `REQ-678` |
| `WFA-009` | B | `WFW-002`, `WFW-031` | `WFE-005` | `REQ-658`, `REQ-687` |
| `WFA-010` | B | `WFW-002`, `WFW-031` | `WFE-006` | `REQ-668` |
| `WFA-011` | B | `WFW-001` | `WFE-007` | `REQ-678` |
| `WFA-012` | B | `WFW-001` | `WFE-008` | `REQ-679` |
| `WFA-013` | B | `WFW-002` | — | `REQ-659` |
| `WFA-014` | B | `WFW-002` | — | `REQ-678` |
| `WFA-015` | B | `WFW-002` | — | `REQ-658` |
| `WFA-016` | B | `WFW-001` | — | `REQ-678` |
| `WFA-017` | C | `WFW-006` | `WFE-009` | `REQ-680` |
| `WFA-018` | C | `WFW-006`, `WFW-038` | `WFE-010` | `REQ-690` |
| `WFA-019` | C | `WFW-006` | `WFE-011` | `REQ-680` |
| `WFA-020` | C | `WFW-004` | — | `REQ-680` |
| `WFA-021` | C | `WFW-006` | — | `REQ-680` |
| `WFA-022` | C | `WFW-006` | — | `REQ-680` |
| `WFA-023` | C | `WFW-005` | `WFE-037` | `REQ-659` |
| `WFA-024` | C | `WFW-006` | `WFE-039` | `REQ-680` |
| `WFA-025` | D | `WFW-011` | — | `REQ-684` |
| `WFA-026` | D | `WFW-011`–`WFW-012` | — | `REQ-699` |
| `WFA-027` | D | `WFW-012` | — | `REQ-699` |
| `WFA-028` | D | `WFW-012` | — | `REQ-699` |
| `WFA-029` | D | `WFW-010` | `WFE-014` | `REQ-686` |
| `WFA-030` | D | `WFW-012` | `WFE-013` | `REQ-699` |
| `WFA-031` | D | `WFW-018`, `WFW-031` | — | `REQ-682` |
| `WFA-032` | D | `WFW-014` | `WFE-015` | `REQ-688` |
| `WFA-033` | E | `WFW-007`, `WFW-010` | `WFE-017` | `REQ-686` |
| `WFA-034` | E | `WFW-025` | `WFE-018` | `REQ-696` |
| `WFA-035` | E | `WFW-018` | — | `REQ-681` |
| `WFA-036` | E | `WFW-016` | `WFE-019` | `REQ-697` |
| `WFA-037` | E | `WFW-016`, `WFW-025` | `WFE-020` | `REQ-697` |
| `WFA-038` | E | `WFW-016` | `WFE-016` | `REQ-688` |
| `WFA-039` | E | `WFW-027` | — | `REQ-681` |
| `WFA-040` | E | `WFW-027`, `WFW-040` | — | `REQ-681` |
| `WFA-041` | F | `WFW-020` | `WFE-021` | `REQ-685` |
| `WFA-042` | F | `WFW-020`–`WFW-021` | `WFE-022` | `REQ-685` |
| `WFA-043` | F | `WFW-020` | `WFE-023` | `REQ-685` |
| `WFA-044` | F | `WFW-020` | `WFE-024` | `REQ-672` |
| `WFA-045` | F | `WFW-020` | — | `REQ-685` |
| `WFA-046` | F | `WFW-020` | — | `REQ-655` |
| `WFA-047` | F | `WFW-011` | — | `REQ-693` |
| `WFA-048` | F | `WFW-020` | — | `REQ-685` |
| `WFA-049` | G | `WFW-021` | `WFE-025` | `REQ-689` |
| `WFA-050` | G | `WFW-021` | `WFE-026` | `REQ-689` |
| `WFA-051` | G | `WFW-023` | `WFE-027` | `REQ-700` |
| `WFA-052` | G | `WFW-030` | `WFE-028` | `REQ-703` |
| `WFA-053` | G | `WFW-021` | — | `REQ-689` |
| `WFA-054` | G | `WFW-022` | — | `REQ-682` |
| `WFA-055` | G | `WFW-023` | — | `REQ-700` |
| `WFA-056` | G | `WFW-030` | — | `REQ-703` |
| `WFA-057` | H | `WFW-034` | — | `REQ-690` |
| `WFA-058` | H | `WFW-035` | — | `REQ-690` |
| `WFA-059` | H | `WFW-001` | — | `REQ-690` |
| `WFA-060` | H | `WFW-039` | `WFE-029` | `REQ-690` |
| `WFA-061` | H | `WFW-035`–`WFW-036` | `WFE-030` | `REQ-690` |
| `WFA-062` | H | `WFW-036` | — | `REQ-690` |
| `WFA-063` | H | `WFW-037` | `WFE-032` | `REQ-690` |
| `WFA-064` | H | `WFW-038` | `WFE-031` | `REQ-690` |
| `WFA-065` | I | `WFW-014` | — | `REQ-688` |
| `WFA-066` | I | `WFW-013` | — | `REQ-688` |
| `WFA-067` | I | `WFW-015` | — | `REQ-688` |
| `WFA-068` | I | `WFW-020` | — | `REQ-688` |
| `WFA-069` | I | `WFW-015` | `WFE-035` | `REQ-686` |
| `WFA-070` | I | `WFW-031` | `WFE-033` | `REQ-687` |
| `WFA-071` | I | `WFW-031` | `WFE-034` | `REQ-687` |
| `WFA-072` | I | `WFW-010`, `WFW-015` | — | `REQ-686` |
| `WFA-073` | J | `WFW-005` | `WFE-037` | `REQ-659` |
| `WFA-074` | J | `WFW-031` | `WFE-038` | `REQ-659` |
| `WFA-075` | J | `WFW-033` | — | `REQ-660` |
| `WFA-076` | J | `WFW-033` | `WFE-012`, `WFE-036` | `REQ-660` |
| `WFA-077` | J | `WFW-006` | `WFE-039` | `REQ-659` |
| `WFA-078` | J | `WFW-006`, `WFW-033` | `WFE-040` | `REQ-660` |
| `WFA-079` | J | `WFW-002` | — | `REQ-658` |
| `WFA-080` | J | `WFW-037` | — | `REQ-660` |
| `WFA-081` | K | `WFW-019` | `WFE-041` | `REQ-657` |
| `WFA-082` | K | `WFW-019` | — | `REQ-657` |
| `WFA-083` | K | `WFW-040` | `WFE-042` | `REQ-655` |
| `WFA-084` | K | `WFW-040` | `WFE-043` | `REQ-655` |
| `WFA-085` | K | `WFW-040` | — | `REQ-681` |
| `WFA-086` | K | `WFW-040` | `WFE-044` | `REQ-681` |
| `WFA-087` | K | `WFW-039` | — | `REQ-663` |
| `WFA-088` | K | `WFW-027` | — | `REQ-681` |
| `WFA-089` | L | `WFW-020` | `WFE-045` | `REQ-672` |
| `WFA-090` | L | `WFW-020` | `WFE-046` | `REQ-670` |
| `WFA-091` | L | `WFW-020` | `WFE-047` | `REQ-672` |
| `WFA-092` | L | `WFW-002` | `WFE-048` | `REQ-669` |
| `WFA-093` | L | `WFW-025` | — | `REQ-672` |
| `WFA-094` | L | `WFW-020`, `WFW-025` | — | `REQ-692` |
| `WFA-095` | L | `WFW-020` | — | `REQ-692` |
| `WFA-096` | L | `WFW-040` | — | `REQ-692` |
| `WFA-097` | M | `WFW-002` | `WFE-049` | `REQ-669` |
| `WFA-098` | M | `WFW-002` | `WFE-050` | `REQ-669` |
| `WFA-099` | M | `WFW-002` | `WFE-051` | `REQ-669` |
| `WFA-100` | M | `WFW-002` | — | `REQ-668` |
| `WFA-101` | M | `WFW-031` | `WFE-052` | `REQ-669` |
| `WFA-102` | M | `WFW-007`, `WFW-018` | — | `REQ-691` |
| `WFA-103` | M | `WFW-020` | — | `REQ-671`–`REQ-672` |
| `WFA-104` | M | `WFW-036` | — | `REQ-669` |
| `WFA-105` | N | `WFW-023` | `WFE-053` | `REQ-701` |
| `WFA-106` | N | `WFW-023` | `WFE-054` | `REQ-702` |
| `WFA-107` | N | `WFW-007` | `WFE-055` | `REQ-667` |
| `WFA-108` | N | `WFW-025`–`WFW-026` | — | `REQ-662`, `REQ-695` |
| `WFA-109` | N | `WFW-028` | — | `REQ-683`, `REQ-693` |
| `WFA-110` | N | `WFW-032` | `WFE-056` | `REQ-666` |
| `WFA-111` | N | `WFW-030` | — | `REQ-703` |
| `WFA-112` | N | `WFW-001`, `WFW-020`, `WFW-027` | — | `REQ-654`–`REQ-656` |
| `WFA-113` | O | `WFW-002` | `WFE-057` | `REQ-678` |
| `WFA-114` | O | `WFW-019`, `WFW-031` | `WFE-058` | `REQ-657` |
| `WFA-115` | O | `WFW-036` | `WFE-059` | `REQ-690` |
| `WFA-116` | O | `WFW-019` | `WFE-060` | `REQ-681` |
| `WFA-117` | O | `WFW-007`, `WFW-018` | — | `REQ-678`, `REQ-681` |
| `WFA-118` | O | `WFW-001` | — | `REQ-678` |
| `WFA-119` | O | `WFW-001`, `WFW-024` | — | `REQ-679`, `REQ-681` |
| `WFA-120` | O | `WFW-001`–`WFW-040` | — | `REQ-654`–`REQ-703` |
| `WFA-121` | P | `WFW-008` | — | `REQ-684`, `REQ-688` |
| `WFA-122` | P | `WFW-009` | — | `REQ-684`, `REQ-688`, `REQ-693` |
| `WFA-123` | P | `WFW-017` | — | `REQ-656`–`REQ-657` |
| `WFA-124` | P | `WFW-029` | — | `REQ-683`, `REQ-690` |

**14.3.6 Per-rule disposition.** The validator derives one disposition for every numbered and lettered rule from two authoritative inputs: the exact `Rules` cell of each acceptance record, and the range or sub-rule row that names the workflow and test. A rule is **DIRECT VERIFICATION** when at least one record cites that exact identifier, **SUPPORTING VERIFICATION** when the range or sub-rule row names a live workflow and a live test that exercise the rule's subject without an exact citation, **DEFERRED** only when a row names an owner and future task, and **NOT COVERED** only with an explicit scope justification. Every disposition also carries the workflow, test, formula where the citing record names one, cross-system source for the integration ranges (`WAR-156`–`WAR-180`), and evidence (`§14.3.3` for workflows, `§14.3.5` for tests). A blank, an unknown identifier, a `WFA-999`/`WFW-999`/`WAR-999` placeholder, or a DIRECT classification without a record that cites the exact rule is rejected.

| Population | Total | DIRECT VERIFICATION | SUPPORTING VERIFICATION | DEFERRED | NOT COVERED |
|---|---|---|---|---|---|
| Numbered `WAR-001`–`WAR-188` | 188 | 95 | 93 | 0 | 0 |
| Lettered sub-rules (`WAR-005a`–`WAR-163b`) | 42 | 19 | 23 | 0 | 0 |
| **All WAR identifiers** | **230** | **114** | **116** | **0** | **0** |

### 14.4 All 39 formulas

Each formula is exercised by the named test with the register's exact inputs and expected outputs; **every value remains provisional** and no test asserts a calibrated number.

| Formula | Subject | Workflows | Tests |
|---|---|---|---|
| `F-WR-001` | OP availability, regeneration and cap | WFW-027 | WFA-039, WFA-040 |
| `F-WR-002` | OP reservation lifecycle | WFW-017, 018, 040 | WFA-040, WFA-085 |
| `F-WR-003` | Readiness upkeep and P3.7 obligation | WFW-026 | WFA-108 |
| `F-WR-004` | Cumulative declaration eligibility | WFW-001, 002 | WFA-016 |
| `F-WR-005` | Readiness value and gate | WFW-022 | WFA-031, WFA-045 |
| `F-WR-006` | Campaign slot occupancy | WFW-001 | WFA-011 |
| `F-WR-007` | Campaign deadline and extension | WFW-006 | WFA-017 |
| `F-WR-008` | Inactivity, stalemate and abandonment | WFW-006 | WFA-019, WFA-077 |
| `F-WR-009` | Objective progress | WFW-024 | WFA-024 |
| `F-WR-010` | Victory determination | WFW-006 | WFA-017 |
| `F-WR-011` | Progress-contribution cap | WFW-024 | WFA-024 |
| `F-WR-012` | Force cap | WFW-028 | WFA-109 |
| `F-WR-013` | Training capacity | WFW-028 | WFA-109 |
| `F-WR-014` | Single-type share | WFW-028 | WFA-109 |
| `F-WR-015` | Recruitment cost and arrival | WFW-028 | WFA-109 |
| `F-WR-016` | Operation supply bundle | WFW-007–016 | WFA-033 |
| `F-WR-017` | Supply-denial surcharge | WFW-007 | WFA-033 |
| `F-WR-018` | Blockade modifier | WFW-010, 015 | WFA-033, WFA-069 |
| `F-WR-019` | Total action cost | WFW-018 | WFA-035 |
| `F-WR-020` | Readiness factor in combat | WFW-020 | WFA-045 |
| `F-WR-021` | Combat power and base ratio | WFW-020 | WFA-041, WFA-047 |
| `F-WR-022` | Order key, frozen baseline and seed | WFW-020, 040 | WFA-046, WFA-084 |
| `F-WR-023` | Fortune draw | WFW-020 | WFA-043, WFA-046 |
| `F-WR-024` | Effective ratio | WFW-020 | WFA-043, WFA-048 |
| `F-WR-025` | Battle tier | WFW-020 | WFA-048 |
| `F-WR-026` | Counter modifier | WFW-013, 014, 015 | WFA-065, WFA-066, WFA-067 |
| `F-WR-027` | Strength-point losses | WFW-021 | WFA-053 |
| `F-WR-028` | Loss caps | WFW-021 | WFA-049, WFA-050 |
| `F-WR-029` | Reparation caps and atomic transfer | WFW-038, 039 | WFA-060, WFA-087 |
| `F-WR-030` | Settlement proposal window | WFW-035 | WFA-061 |
| `F-WR-031` | Exclusion and disarmament | WFW-037, 038 | WFA-059, WFA-064 |
| `F-WR-032` | Odds band | WFW-007 | WFA-044 |
| `F-WR-033` | Threat band | WFW-020 | WFA-044, WFA-089 |
| `F-WR-034` | P5 validity, idempotency and recovery | WFW-040 | WFA-083, WFA-084 |
| `F-WR-035` | Calibration envelope (**PROVISIONAL — PROMPT 14**) | all | WFA-048 (shape only; calibration DEFERRED to Prompt 14) |
| `F-WR-036` | Military Food ration | WFW-025 | WFA-034 |
| `F-WR-037` | City infrastructure damage | WFW-023 | WFA-051, WFA-055 |
| `F-WR-038` | Fixed-asset impairment and repair | WFW-023, 030 | WFA-056, WFA-106 |
| `F-WR-039` | Combined supply modifier | WFW-007, 010 | WFA-033 |

### 14.5 The fourteen audit events

Every event is written once per committed change, is visible only to the audiences named in §12.2, and is not duplicated by an idempotent replay.

| Event | Trigger | Timing | Actor / visibility | Workflows | Tests | Replay |
|---|---|---|---|---|---|---|
| `WRA-01` `WAR_DECLARED` | Declaration accepted | OPEN | actor; target; public record; moderators | WFW-001 | WFA-016 | Same-key replay returns the original receipt; no second event |
| `WRA-02` `WAR_BLOCKED` | Any block or failed revalidation | Submission, P2, pre-P5 | actor; moderators | WFW-002, 018, 031 | WFA-001, WFA-092 | A new submission is a new block; a same-key replay writes nothing |
| `WRA-03` `OP_ACCEPTED` / `OP_REJECTED` | Operation submission outcome | Submission; P5 | actor; moderators | WFW-007–018 | WFA-035 | Exactly one terminal item per action key |
| `WRA-04` `BATTLE_RESOLVED` | Battle commit | P5 | both belligerents; public summary; moderators | WFW-020 | WFA-041, WFA-095 | A committed battle is skipped on replay; no double losses |
| `WRA-05` `CAMPAIGN_STATE` | Any campaign state change | P0; P5; P7 | both belligerents; public state; moderators | WFW-004, 005, 006 | WFA-020 | One event per transition; a replayed boundary republishes nothing |
| `WRA-06` `OBJECTIVE_PROGRESS` | Objective delta | P5 | both belligerents; moderators | WFW-024 | WFA-024 | One event per committed delta |
| `WRA-07` `STATE_APPLIED` / `STATE_REMOVED` | Blockade, fortification, other temporary state | P5 | both belligerents; moderators | WFW-010, 014, 015 | WFA-069 | One event per state change; no stacking |
| `WRA-08` `STRATEGIC_STRIKE` | `OP-05` resolution and city damage | P5 | attacker; defender; public infrastructure; moderators | WFW-011, 012, 023 | WFA-095 | One event per resolved strike |
| `WRA-09` `INTERCEPTION` | `OP-06` resolution | P5 | both belligerents; moderators | WFW-013 | WFA-066 | One event per intercept |
| `WRA-10` `FORTIFICATION` | `OP-07` resolution | P5 | both belligerents; moderators | WFW-014 | WFA-065 | One event per fortification |
| `WRA-11` `RESUPPLY` | `OP-09` resolution and upkeep | P3.7; P5 | actor; moderators | WFW-016, 026 | WFA-036 | One event per resolution |
| `WRA-12` `SETTLEMENT` | Settlement state change or completion | P4 proposal; P5.3 completion | both parties; moderators | WFW-034–039 | WFA-057, WFA-060 | One completion per proposal; a second acceptance returns the receipt |
| `WRA-13` `CAMPAIGN_ENDED` | Terminal outcome | P5, P6, P7 | both belligerents; public outcome; moderators | WFW-006, 037, 038 | WFA-024 | One terminal event per campaign |
| `WRA-14` `RESERVATION_AUDIT` | Reservation and Food audit leg | Acceptance; P5; P7 | actor; moderators | WFW-025, 027 | WFA-040 | One leg per reservation change; release is recorded once |

### 14.6 Failure codes

The **32 defined codes** are each mapped in §10.2 to at least one workflow and one test. `WRF-15`–`WRF-19` are unallocated gaps and are **not** claimed as covered. No code is orphaned and no test depends on an undefined code.

### 14.7 Architecture decisions and conflict entries

**14.7.1 `B10-AD-01`–`B10-AD-25`.** Every architecture decision is dispositioned by the workflows and tests below. 10C records no new `B10-AD-` entry.

| AD | Subject | Workflows | Tests |
|---|---|---|---|
| `B10-AD-01` | Layered war → one campaign → objectives/operations/battles | WFW-001, 020 | WFA-120 |
| `B10-AD-02` | One outgoing + one incoming campaign; no joining | WFW-001 | WFA-011, WFA-118 |
| `B10-AD-03` | One war per campaign; one primary + one secondary objective | WFW-001, 024 | WFA-012 |
| `B10-AD-04` | Per-campaign progress per side; OP strictly national | WFW-024, 027 | WFA-040 |
| `B10-AD-05` | 84+42 deadline; 24/48 inactivity | WFW-006 | WFA-017, WFA-019 |
| `B10-AD-06` | Owner-only unilateral declaration; 2 OP + 500 crowns | WFW-001 | WFA-007, WFA-016 |
| `B10-AD-07` | One immutable `STANDARD` profile; no posture switch | WFW-001 | WFA-007 |
| `B10-AD-08` | Six closed mapless objectives | WFW-001, 024 | WFA-012 |
| `B10-AD-09` | Victory by primary completion; five outcome classes | WFW-006 | WFA-017, WFA-024 |
| `B10-AD-10` | Nine-operation catalogue | WFW-007–016 | WFA-025 |
| `B10-AD-11` | National readiness 0…1,000, combat-only | WFW-022 | WFA-045, WFA-054 |
| `B10-AD-12` | Four strength-point pools; no individual units | WFW-021, 028 | WFA-053 |
| `B10-AD-13` | Recruitment at P4, arrival at P3.7, no OP cost | WFW-028 | WFA-109 |
| `B10-AD-14` | Four-resource supply bundle, no geography | WFW-007–016 | WFA-033 |
| `B10-AD-15` | Deterministic power + one seeded ±500 bp fortune | WFW-020 | WFA-041, WFA-043, WFA-046 |
| `B10-AD-16` | Bounded losses; 20% battle, 60% campaign | WFW-021 | WFA-049, WFA-050 |
| `B10-AD-17` | 3 offensive + 3 conditional defensive per turn; prep first | WFW-014, 020 | WFA-032, WFA-042 |
| `B10-AD-18` | Closed-term settlement; immediate atomic transfer | WFW-035–039 | WFA-058, WFA-087 |
| `B10-AD-19` | No new postwar protection; optional exclusion | WFW-006, 031 | WFA-059, WFA-071 |
| `B10-AD-20` | `UD-032` Option A: reroll block, surrender off-ramp | WFW-033, 037 | WFA-075, WFA-080 |
| `B10-AD-21` | City infrastructure damage for `OP-05` only | WFW-023 | WFA-051, WFA-055 |
| `B10-AD-22` | No military building or Military research branch | WFW-028 | WFA-109 |
| `B10-AD-23` | Conventional missile only; no nuclear | WFW-011, 012 | WFA-026 |
| `B10-AD-24` | Espionage excluded and unassigned | §1.7 item 3 | WFA-116 |
| `B10-AD-25` | Odds band, threat band, full report after | WFW-020 | WFA-044, WFA-089 |

**14.7.2 `B10-C01`–`B10-C34`.** Every conflict entry has a disposition in B-10 and a verification path here. `B10-C30` (espionage) remains **excluded and unassigned**; 10C does not create it.

| Conflict | Subject | Workflows | Tests |
|---|---|---|---|
| `B10-C01` | Campaign cost timing | WFW-001, 018 | WFA-016, WFA-035 |
| `B10-C02` | P3 upkeep vs P5 combat readiness | WFW-026, 020 | WFA-108 |
| `B10-C03` | OP refill vs carried reservations | WFW-027, 040 | WFA-039, WFA-040 |
| `B10-C04` | P2 vs final P5 validation | WFW-031 | WFA-070 |
| `B10-C05` | Simultaneous offensive and defensive operations | WFW-020 | WFA-042 |
| `B10-C06` | Contested targets and dependent actions | WFW-013 | WFA-066 |
| `B10-C07` | Attack ordering | WFW-020 | WFA-046 |
| `B10-C08` | Stale target | WFW-018 | WFA-025 |
| `B10-C09` | Duplicate actions and retries | WFW-019 | WFA-081 |
| `B10-C10` | Interrupted P5 | WFW-040 | WFA-083, WFA-084 |
| `B10-C11` | Participant becomes dormant | WFW-005 | WFA-023 |
| `B10-C12` | Target becomes dormant | WFW-005 | WFA-073 |
| `B10-C13` | Protection expires between acceptance and execution | WFW-031 | WFA-071 |
| `B10-C14` | Existing defensive commitments when dormant | WFW-032 | WFA-110 |
| `B10-C15` | Reroll with an active campaign | WFW-033 | WFA-075 |
| `B10-C16` | Historical attribution and cleanup | WFW-006 | WFA-078 |
| `B10-C17` | Where readiness upkeep sits | WFW-026 | WFA-108 |
| `B10-C18` | Unpaid upkeep consequence | WFW-026 | WFA-034 |
| `B10-C19` | Resource reservation, consumption, release | WFW-018 | WFA-040 |
| `B10-C20` | OP and resource costs together | WFW-018 | WFA-035 |
| `B10-C21` | Repair and recovery costs | WFW-028, 030 | WFA-056, WFA-109 |
| `B10-C22` | Loot and reparation caps | WFW-038 | WFA-060 |
| `B10-C23` | Facility damage | WFW-023 | WFA-106 |
| `B10-C24` | Military buildings and research | WFW-028 | WFA-109 |
| `B10-C25` | City targeting | WFW-012 | WFA-027 |
| `B10-C26` | Political states and war | WFW-032 | WFA-110 |
| `B10-C27` | National vs Alliance NAP; membership changes | WFW-002, 031 | WFA-100, WFA-101 |
| `B10-C28` | `CONSUME` event naming | WFW-027 | WFA-040 |
| `B10-C29` | `AUD-AL-017` scope | WFW-002 | WFA-092 |
| `B10-C30` | Espionage ownership — **excluded, unassigned** | §1.7 item 3 | WFA-116 |
| `B10-C31` | Alliance military authority | WFW-007 | WFA-102 |
| `B10-C32` | Pre-battle odds | WFW-020 | WFA-044 |
| `B10-C33` | Settlement duration and enforcement | WFW-035–039 | WFA-057, WFA-059 |
| `B10-C34` | Nuclear and radiation scope | WFW-011 | WFA-026 |

### 14.8 B-10 §29 handoff disposition

**14.8.1 The eighteen received inputs.** Each input is present and used, or its absence is stated.

| # | Input | Where used | Status |
|---|---|---|---|
| 1 | Campaign state machine | §4.1, §6, WFW-004–006 | **Used** |
| 2 | Operation state machine | §4.2, WFW-007–019 | **Used** |
| 3 | Declaration and eligibility | §2.5, WFW-001, 002, §13.4 | **Used** |
| 4 | Operation prerequisites, costs, effects, counters | §5.2, §7.1, WFW-007–016 | **Used** |
| 5 | OP reservation and consumption | §4.4, WFW-027, §7.6 | **Used** |
| 6 | Readiness and resource requirements | §4.5, §7.3, WFW-025, 026 | **Used** |
| 7 | Battle formulas | §7.7, WFW-020, §13.8 | **Used** |
| 8 | Victory and expiry | §4.1, §7.7, WFW-006 | **Used** |
| 9 | Losses and recovery | WFW-021–023, 030, §13.9 | **Used** |
| 10 | Peace, surrender, settlement | WFW-034–039, §13.10 | **Used** |
| 11 | Protection and reroll | WFW-031, 033, §13.11–13.12 | **Used** |
| 12 | Block and failure codes | §10 | **Used**, with the `WRF-15`–`WRF-19` gap disclosed |
| 13 | Visibility and audit | §12, WFW-020, §13.14 | **Used** |
| 14 | Simultaneous-action ordering | §2.7, §4.8, WFW-020 | **Used** |
| 15 | Interrupted-P5 recovery | WFW-040, §13.13 | **Used** |
| 16 | Cross-system integration | §14.9, §7.3–7.4 | **Used** |
| 17 | Formula and example references | §7, §14.4 | **Used** |
| 18 | Unresolved and owner-reserved boundaries | §15, §16, §1.7 | **Used**; `UD-040`–`UD-049` remain Open |

**14.8.2 Required coverage.** States — all seven campaign states (WFW-004–006, 038, 039), all operation states (WFW-007–019), all thirty-two defined block codes (§10), all eight settlement states (WFW-034–039). Happy paths — declaration → battle → settlement (WFA-120); declaration → suspension → abandonment (WFA-023, 077); declaration → ceasefire → white peace (WFA-057). Permission failures — every code in §10.2 has a test. Edge cases — membership change (WFA-101), NAP expiry within a campaign (WFA-100), protection activating between P2 and P5 (WFA-070), reroll (WFA-075–076), protection expiry (WFA-071), simultaneous attacks (WFA-042), expiry on a victory turn (WFA-017), settlement on the deadline (WFA-018). Recovery — WFA-083–088. Matrix — §14. Boundary — this document defines tests and executes none. Must-not-add — §1.7 and §15 record compliance.

**14.8.3 Downstream handoff boundary.** Prompt 11 receives events, objective totals, outcomes and settlement records (REQ-673, WFA-120); Prompt 12 receives evidence fields and block records (REQ-674, WFA-092); Prompt 13 receives board content, confirmation minimum and failure copy (REQ-675, WFA-007); Prompt 14 receives all formulas and provisional values (REQ-676, WFA-048); Prompt 15 receives the integration matrix and registers (REQ-677, WFA-120). **No downstream prompt receives authority to change a B-10 state, code, cost, formula shape or permission.**

### 14.9 Subsystem and prompt integration rows

Every integration row carries eleven contract fields. **A row with an empty field, a reference to a nonexistent workflow, edge case or test, or an unnamed validation or mutation owner is rejected by the validator.** For rows 1–8 the mutation owner is the subsystem that owns the object; warfare reads it and writes only its own records. For rows 9–13 the mutation owner is `none` where the receiving prompt presents, calibrates or documents rather than mutates.

| # | Subsystem / prompt | Source rule | Workflows | Edge cases | Tests | Validation owner | Mutation owner | Trigger / phase | Ordering | Transaction / accounting | Failure / recovery | Audit | Privacy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | B-02 phases | B-02 `TR-040`, `TR-050`, `TR-059` | WFW-001, 027, 040 | WFE-042–044 | WFA-112 | B-10 P3.7/P5 scheduler | B-02 phase engine | OPEN acceptance, P3.7, P4.1, P5, P7 | `WAR-040` single-flight; P3.7 precedes P5 | One commit per phase; OP ledger per §4 | `WRF-34`; resume from the last committed checkpoint | `WRA-04`, `WRA-05` | moderators; actors see their own records |
| 2 | B-03 protection, network pairs, dormancy | `ACC-016`, `NET-015`; `ONB-019`, `ONB-023`, `ONB-037`, `ONB-039` | WFW-002, 005, 031 | WFE-005, 006, 033, 034, 037, 038 | WFA-009, WFA-015, WFA-073 | B-10 hostile-state gate | B-03 state (read-only to warfare) | OPEN, P2, pre-P5 | Re-read at every boundary | No reservation on block; release once on P2/pre-P5 failure | `WRF-02`, `WRF-03`, `WRF-04`, `WRF-05`, `WRF-21`; release | `WRA-02`, `WRA-03` | actor; target sees the block category; moderators |
| 3 | B-04 economy | `ECN-105`, `ECN-119`, `ECN-152`, `ECN-163`, `ECN-214` | WFW-018, 026, 038 | WFE-017–020, 031 | WFA-035, WFA-060, WFA-108 | B-10 ledger | B-04 economy | OPEN, P3.7, P5 | Ration before upkeep; reparation last | All-or-nothing; no debt | `WRF-11`, `WRF-12`, `WRF-33`, `WRF-35`; release | `WRA-03`, `WRA-12` | actor; moderators |
| 4 | B-05 cities and infrastructure | `URB-042`, `URB-046`, `URB-051a`, `URB-118a`, `URB-118b` | WFW-023, 030 | WFE-013, 027, 028, 053, 054 | WFA-051, WFA-105, WFA-106 | B-10 city-target gate | B-05 city registry | P5 damage; P4.1 repair | Damage before the next P3.8; repair at P4.1 | Damage event commits with the battle | `WRF-36`, `WRF-37`; release | `WRA-08` | city infrastructure public; actor; moderators |
| 5 | B-06 population and politics | `DMP-030`, `DMP-031`, `DMP-031a`, `DMP-045`, `DMP-052` | WFW-032 | WFE-053, 056 | WFA-105, WFA-110 | B-10 political gate | B-06 population/politics | Next P3.8; P2; pre-P5 | Political re-read before P5 | No transfer; an accepted defensive commitment is exempt | `WRF-09`; release | `WRA-02` | public political state; actor; moderators |
| 6 | B-07 market | B-07 `MKT-009`, `MKT-218` | WFW-007 | WFE-055 | WFA-107 | B-07 market | B-07 market only | Continuous | Not ordered by warfare | No warfare accounting | N/A — no war trade ban exists | none — trade is a B-07 flow | public market |
| 7 | B-08 diplomacy | `DIP-037`, `DIP-070`, `DIP-141` | WFW-002 | WFE-006, 051 | WFA-100 | B-10 declaration gate | B-08 diplomacy | OPEN, P2, pre-P5 | NAP check before slot occupancy | No reservation on block | `WRF-06`, `WRF-08`; release | `WRA-02`; `AUD-AL-017` | the pair; moderators |
| 8 | B-09 Alliance | `ALL-199`, `ALL-204`, `ALL-206`, `ALL-208`, `AUD-AL-017`, `AT-E01` | WFW-002, 031 | WFE-046, 049, 050, 052 | WFA-097, WFA-098, WFA-102 | B-10 Alliance gate | B-09 Alliance records | OPEN, P2, pre-P5 | Membership re-read at each boundary | No reservation on block | `WRF-07`, `WRF-08`; release | `AUD-AL-017`; `WRA-02` | Alliance sees its own; moderators |
| 9 | Prompt 11 | `WAR-032`–`WAR-038` (B-10 objectives and outcome) | WFW-024 | WFE-009, 011, 039 | WFA-120 | B-10 outcome evaluator | B-10 campaign and objective records | P5/P6; P7 close | Completion before expiry | One outcome per campaign | `WRF-20`; checkpoint recovery | `WRA-05`, `WRA-06` | public outcome; moderators |
| 10 | Prompt 12 | `WAR-148`–`WAR-155` (B-10 evidence and audit) | WFW-002, 040 | WFE-047, 048, 059 | WFA-092, WFA-096 | B-10 evidence writer | B-10 evidence store | Every block and commit | Evidence precedes publication | Append-only | `WRF-34`; checkpoint held | `WRA-02`, `WRA-04` | moderators; redacted actor view |
| 11 | Prompt 13 | This document §12.3; `WAR-149`–`WAR-152` (B-10 visibility and sovereignty) | WFW-001, 020 | WFE-024, 057 | WFA-007, WFA-044 | B-10 surface contract | none — presentation only | OPEN confirmation; pre-P5 query | Server value before display | No transaction | `WRF-01`; the server validator decides | `WRA-02` for blocked attempts | actor bands only |
| 12 | Prompt 14 | Formula register v1.3, `F-WR-001`–`F-WR-039` | WFW-020, 021, 025 | WFE-017, 023 | WFA-048 | Calibration owner (Prompt 14) | none — parameters only | Calibration run | Shape fixed before calibration | Atomic parameter set | N/A — no calibrated value is asserted | calibration record (future) | internal |
| 13 | Prompt 15 | This document §14 (cross-document registers) | WFW-001–040 | WFE-001–060 | WFA-120 | Documentation owner | none — documentation | Handoff | Registers before implementation | No transaction | N/A — documentation only | none — a documentation row writes no audit event | internal |

### 14.10 10A research disposition

The 10A report supplies **44 candidates in 22 areas**; none is a rule. B-10 adopted or consolidated **43** into `REQ-654`–`REQ-703`; `WCR-33`/`WCR-34` (abuse and fair play) and `WCR-44` (audit) are carried as handoffs to Prompt 12; `WCR-40` (progression) is constrained by `B10-AD-22`; the espionage candidate area is excluded (`B10-AD-24`, `B10-C30`). The 22 areas map to the workflows as follows:

| Area | Candidates | Workflow | Test |
|---|---|---|---|
| 1 Declaration eligibility | WCR-01, 02 | WFW-001, 002 | WFA-016 |
| 2 War types | WCR-03, 04 | WFW-001 | WFA-007 |
| 3 Campaign objectives | WCR-05, 06 | WFW-024 | WFA-012 |
| 4 Campaign lifecycle | WCR-07, 08 | WFW-004–006 | WFA-017 |
| 5 Operations economy | WCR-09, 10 | WFW-027 | WFA-040 |
| 6 Readiness | WCR-11, 12 | WFW-022 | WFA-045 |
| 7 Unit roster | WCR-13, 14 | WFW-028 | WFA-109 |
| 8 Operation catalogue | WCR-15, 16 | WFW-007–016 | WFA-025 |
| 9 Battle resolution | WCR-17, 18 | WFW-020 | WFA-041 |
| 10 Supply and logistics | WCR-19, 20 | WFW-007–016 | WFA-033 |
| 11 Protection states | WCR-21, 22 | WFW-031 | WFA-070 |
| 12 Counterplay | WCR-23, 24 | WFW-013–015 | WFA-065 |
| 13 Losses | WCR-25, 26 | WFW-021 | WFA-049 |
| 14 War termination | WCR-27, 28 | WFW-006 | WFA-024 |
| 15 Settlement | WCR-29, 30 | WFW-035–039 | WFA-058 |
| 16 Alliance integration | WCR-31, 32 | WFW-002, 007 | WFA-097, WFA-102 |
| 17 Abuse and fair play | WCR-33, 34 | WFW-002, 040 | WFA-092 (DEFERRED policy) |
| 18 Transparency | WCR-35, 36 | WFW-001, 020 | WFA-007, WFA-089 |
| 19 Mapless conformance | WCR-37, 38 | all | WFA-116 |
| 20 Progression | WCR-39, 40 | WFW-028 | WFA-109 |
| 21 Conservation | WCR-41, 42 | WFW-018, 027 | WFA-040 |
| 22 Audit and records | WCR-43, 44 | WFW-020, 040 | WFA-094, WFA-096 |

### 14.11 Orphan audit — ten separate totals

Each total is computed independently by the validator. **Unexplained orphans must be zero in every row.** A disclosed gap, a DEFERRED row with a named owner, or an explicit `—` is not an orphan; an unexplained zero-reference row is.

| # | Population | Total | Disposition | Unexplained orphans |
|---|---|---|---|---|
| 1 | WAR rules — 188 numbered plus 42 lettered sub-rules | 230 | Every numbered rule lies in one of the 26 contiguous ranges of §14.3; every lettered sub-rule is listed individually in §14.3.1; each row names a workflow and a test | **0** |
| 2 | Requirements `REQ-654`–`REQ-703` | 50 | 44 DIRECT, 1 SUPPORTING (`REQ-672`), 5 DEFERRED (`REQ-673`–`REQ-677`, owners named in §14.8.3), 0 NOT COVERED | **0** |
| 3 | Formulas `F-WR-001`–`F-WR-039` | 39 | Every formula names its workflow and test in §14.4; `F-WR-035` tests shape only and defers calibration to Prompt 14 | **0** |
| 4 | Decisions — 25 `B10-AD`, 25 `DD-166`–`DD-190` mirrors, 34 `B10-C`, `UD-032` and `UD-040`–`UD-049` | 25 + 25 + 34 + 1 + 10 | Each `B10-AD` row is dispositioned in §14.7.1; each conflict in §14.7.2; `B10-C30` is excluded by design; `UD-032` is applied; `UD-040`–`UD-049` remain OPEN and owner-reserved, and are listed rather than decided | **0** |
| 5 | Failure codes `WRF-01`–`WRF-37` | 32 defined (+5 disclosed gaps) | Every defined code names a workflow and a test in §10.2; `WRF-15`–`WRF-19` are disclosed as unallocated and cited by no test | **0** |
| 6 | Audit events `WRA-01`–`WRA-14` | 14 | Every event names its emitting workflow, its tests, its actor and visibility, and its replay treatment in §14.5 | **0** |
| 7 | Integration contracts (subsystem and prompt rows) | 13 | Every row names source subsystem, source rule, WFW/WFE/WFA references, validation and mutation owner, trigger, ordering, transaction, failure, audit and privacy in §14.9 | **0** |
| 8 | Workflow reverse references | 40 | Every `WFW-001`–`WFW-040` is cited by at least one dedicated test in §14.3.3; `WFA-121`–`WFA-124` close the four former single-reference gaps | **0** |
| 9 | Edge-case reverse references | 60 | Every `WFE-001`–`WFE-060` names a primary test in §14.3.4; `WFE-030`, `WFE-037` and `WFE-039` are additionally cited by a second test | **0** |
| 10 | Test source references | 124 | Every `WFA-001`–`WFA-124` names at least one workflow and one requirement in §14.3.5; tests with no §9 entry declare `—` explicitly | **0** |

**14.11.1 Reading the totals.** Row 4 is the only place where a population is counted in parts: the 25 architecture decisions, their 25 register mirrors, the 34 conflict entries, one applied unresolved decision and ten owner-reserved decisions are distinct populations that the earlier single-line audit conflated. They are reported together here because all five are decision records, and separately by disposition because only the first four are dispositioned by 10C. The ten `UD-040`–`UD-049` entries are neither orphans nor approvals: they are explicitly **OPEN**, and the validator fails if any is presented as resolved.

**14.11.2 What would count as an orphan.** A numbered rule cited by no workflow; a requirement with no test and no named deferral; a formula with no test; an architecture decision with no disposition; a defined failure code no test can emit; an audit event no workflow writes; an integration row with a missing contract field; a workflow with no test; an edge case with no test; a test with no rule or no requirement. The self-test mutates the document into each of these states and requires rejection (§14.12).

### 14.12 Fixture catalogue and named representative subset

The authoritative fixture catalogue is [warfare_fixture_catalogue.md](../qa_backups/warfare_fixture_catalogue.md). It is a **projection** of the canonical machine-readable registry [warfare_fixture_registry.json](../qa_backups/warfare_fixture_registry.json), and both are generated by `verify_warfare_workflows.py --emit-catalogue`. Documentation and execution therefore cannot drift silently. The registry is the single source for **13 positive fixtures** (`PF-01`–`PF-13`), **67 negative fixtures** (`NF-01`–`NF-67`) and **10 N/A unit fixtures** (`NA-01`–`NA-10`), **90 fixtures in total**. Every entry carries the fixture ID, exact name, exact mutation description, target source/row/field, old and expected value, expected rejecting check, expected failure reason, executor name, executor source hash, documentation reference and declared result.

Check 47 verifies the registry and the executable suite against each other: unique IDs; complete definitions; every executable fixture documented and every documented fixture executable; the declared executor is callable and its `inspect.getsource` SHA-1 matches; the executor actually applies the declared mutation to the declared target (one change block for a row edit or deletion, the declared append text for an append, and the declared old→new value for a replacement); the expected check rejects the mutated copy; the observed failure contains the declared reason; the clean context is unmodified; and the temporary mutated copy is discarded. A different valid executor, an unrelated invalid output, a replaced description, a wrong target or a wrong expected check fails check 47. §17.6 records the C3 corruption proof.

The table below is a **named representative subset**, not a replacement for the catalogue. Every ID, mutation and expected check is copied from the catalogue and executed by `--self-test`; the full set, including the twelve traceability corruptions `NF-41`–`NF-52` and the fifteen integration corruptions `NF-53`–`NF-67`, remains in the catalogue.

| ID | Mutation applied | Expected rejecting check | Catalogue result |
|---|---|---|---|
| `NF-09` | Delete one test's identification row | 09 — identification and behaviour sets differ | Rejected |
| `NF-13` | Assign a class-P test to class A | 13 — edge-case class disagrees with test | Rejected |
| `NF-14` | Point a test at `WFE-999` | 14 — unknown edge-case identifier | Rejected |
| `NF-15` | Point a test at `WFW-999` | 15 — unknown workflow identifier | Rejected |
| `NF-16` | Point a test at `REQ-704` | 16 — requirement outside `REQ-654`–`REQ-703` | Rejected |
| `NF-17` | Cite the unallocated `WRF-19` | 17 — unallocated failure code | Rejected |
| `NF-18` | Cite `WAR-189` | 18 — rule outside the B-10 inventory | Rejected |
| `NF-19` | Cite `WRA-15` | 19 — audit event outside `WRA-01`–`WRA-14` | Rejected |
| `NF-20` | Cite `F-WR-040` | 20 — formula outside `F-WR-001`–`F-WR-039` | Rejected |
| `NF-21` | Point an edge case at `WFA-999` | 21 — edge-case test does not exist | Rejected |
| `NF-45` | Insert the fabricated rule `WAR-999` into a numbered range | 44 — fabricated numbered rule | Rejected |
| `NF-46` | Insert the fabricated lettered rule `WAR-005z` | 44 — fabricated lettered rule | Rejected |
| `NF-49` | Remove the workflow source mapping from a WFA record | 15 — test names no workflow | Rejected |
| `NF-50` | Orphan `WFW-040` | 18 — workflow has no dedicated test | Rejected |
| `NF-51` | Orphan `WFE-060` | 19 — edge case is not cited back | Rejected |
| `NF-52` | Orphan `WFA-124` | 09 — test row is missing | Rejected |
| `NF-53` | Point the B-02 integration source at `B-99` / `FAKE-999` | 45 — source subsystem and rule do not exist | Rejected |
| `NF-63` | Remove an integration validation owner | 45 — validation owner empty | Rejected |
| `NF-64` | Remove an integration mutation owner | 45 — mutation owner empty | Rejected |

---

## 15. D-014 autonomy audit

**15.1 Scope.** This section audits every decision 10C made under [D-014](../AUTONOMOUS_DECISION_POLICY.md). The test is not whether the document is long; it is whether 10C stayed inside **authoring autonomy** and left **player sovereignty** and **owner-reserved decisions** untouched.

**15.2 Category check.**

- **Category A — fixed constraints.** 10C changed none. The eleven-resource roster, mapless world, 2-hour cadence, account policy, Cloudflare Pages + Supabase, free-first target and Stage sequencing are unchanged. The eight 10C fixed constraints are restated in §1.7 and enforced by the validator.
- **Category B — ordinary design and documentation decisions.** One consequential decision was required; it is recorded as `D-143` in [DECISIONS.md](../DECISIONS.md) and summarized in §15.3. Workflow decomposition, identifier spaces and class taxonomy are documentation conventions recorded here, not game decisions. **No ordinary matter was deferred to the owner**: every routine authoring choice was made under D-014, and work stopped only at the prompt's own boundaries — no implementation and no Prompt 11.
- **Category C — provisional decisions.** **None created by 10C.** Every B-10 value remains Provisional under its existing entry; 10C neither promotes nor recalibrates one. `UD-040`–`UD-049` remain **Open** and are not decided by any workflow.
- **Category D — external, costly or irreversible actions.** **None taken.** No implementation, deployment, publication, purchase, credential use or external write occurred. No commit was made.

**15.3 The one recorded decision (`D-143`).**

| Field | Record |
|---|---|
| Question | How should 10C treat the five unallocated numbers `WRF-15`–`WRF-19`? |
| Alternatives | (a) Invent five codes to fill the span — rejected: it would add failure semantics not in B-10 and change a closed set; (b) renumber to a contiguous 32 — rejected: it would rename B-10 identifiers and break every existing reference; (c) keep the span uncontiguous and **disclose the gap** — chosen. |
| Evidence | B-10 §24.2 defines 32 rows; no Stage 2 document defines `WRF-15`–`WRF-19`; B-10 §29 line 12 refers to the span, not to 37 definitions. |
| Consequence | §10.2 lists 32 defined codes and names the five gaps; no workflow, test or implementation may use a gap; the validator asserts both facts. |
| Priority test | Data integrity and honest records outrank cosmetic contiguity (§4 items 2 and 10). |
| Reopen condition | The owner or a later B-10 revision assigns a meaning to a gap; then the new definition is recorded in B-10 first and this document follows. |

**15.4 Authoring autonomy versus player sovereignty.** A workflow may describe a decision; it may not make one for a player. The audit below confirms that every workflow preserves the rule that only the authenticated owner acts, consent is explicit, and silence is never acceptance.

| Workflow group | Initiating actor | Explicit confirmation required | Silence or delegation accepted? | Sovereignty finding |
|---|---|---|---|---|
| WFW-001–006 declaration and campaign | Owner only | Yes, for declaration | No; a declaration is unilateral but the declarer acts personally, and a settlement or ceasefire needs the counterparty's own acceptance | Preserved |
| WFW-007–019 operations | Owner only | Yes, for every offensive operation | No; no Alliance, office or AI may submit | Preserved |
| WFW-020–024 battle, losses, progress | Scheduler and canonical validator | Not applicable (no player choice) | The system never chooses an operation, target or term | Preserved |
| WFW-025–030 ration, upkeep, regeneration, recruitment, disbanding, repair | Owner orders recruitment, disbanding and repair; the ration and regeneration are automatic obligations | Yes for recruitment, disbanding and repair | No delegated recruitment; no inferred disbanding | Preserved |
| WFW-031–033 protection, political state, reroll | Scheduler and owner | Reroll is an owner request and is blocked, not granted | No protection waiver by an Alliance or administrator | Preserved |
| WFW-034–039 ceasefire, settlement, surrender | Owner only, each party separately | Yes, for acceptance and surrender | **No**; silence expires, never accepts | Preserved |
| WFW-040 recovery and close | Scheduler | Not applicable | No player action is inferred during recovery | Preserved |

**15.5 What 10C did not do.** It did not: declare or operate for a player; treat an Alliance, office, ballot, treaty, AI or administrator as a military authority — **an Alliance office confers no military command**; infer consent from silence; resolve `UD-040`–`UD-049`; promote a provisional value; add, remove or rename a B-10 state, code, operation or formula; change an OP, Food, readiness, loss or settlement number; or claim a runtime result.

**15.6 Policy review.** [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) was read and applied without weakening it. No exception, waiver or new category was introduced. 10C did not stop to ask an ordinary design question; it stopped only at the boundary the prompt itself sets — do not implement and do not begin the next prompt.

---

## 16. Implementation handoff

**16.1 Status.** **Implementation is not authorized by 10C.** This section tells a future implementer what exists, what must be decided elsewhere first, and what must not be built. It is a handoff, not a work order.

**16.2 What an implementer receives.** A complete rule source (B-10 v1.3), a complete formula source (register v1.3), a workflow for every player and system action (WFW-001–040), a state-transition ledger (§6), edge cases (WFE-001–060) and 124 test designs (WFA-001–WFA-124). The implementer does **not** receive calibrated numbers, UI layouts, database schemas or deployment choices.

**16.3 Prerequisites before any code.**

1. **Prompt 14 calibration.** Every B-10 value is Provisional. A runtime implementation before calibration would hard-code numbers that the owner has not accepted.
2. **Prompt 12 policy.** Evidence retention, penalty policy and audit-access implementation are owned by Prompt 12; 10C supplies record shape only.
3. **Prompt 13 interface.** The confirmation minimum, board content, bands and failure copy are specified as content floors here; the interface itself is Prompt 13's.
4. **An explicit owner implementation instruction.** No prompt after 10C is assumed; none is begun here.

**16.4 Recommended implementation order (when authorized).** Phase contract and ledger first; declaration and validator second; operations and reservations third; P3.6/P3.7 obligations fourth; P5 battle, losses and damage fifth; settlement and postwar sixth; audit, visibility and recovery seventh; acceptance execution last. Each layer must pass its WFA rows before the next depends on it.

**16.5 Non-negotiables carried forward.**

1. One server-side canonical validator at submission, P2 and pre-P5; fail closed.
2. One persistent national OP ledger; no P0/P7 regeneration; no shared or transferable pool.
3. Reserve at acceptance, consume at P5, release exactly once on failure, cancellation or P7 void.
4. Civilian Food before military Food; whole obligations; no debt.
5. Mapless objects only; no city, facility or population destruction; `OP-05` infrastructure damage only.
6. No Alliance military authority, shared OP, treasury use or private member data.
7. Explicit consent only; no inference from silence; no delegated military decision.
8. Append-only audit; no in-place edit of a committed result.
9. Every provisional value labelled; no promotion without Prompt 14 evidence.
10. Runtime claims require runtime evidence; a green document validator is not a playtest.

**16.6 What must not be built.** Espionage or any covert operation; a per-war, per-Alliance or purchasable OP pool; city capture, transfer or deletion; facility damage; population casualty; nuclear or radiation effects; military buildings or a Military research branch; Alliance command, delegated orders or a military treasury; a second protection system; debt, instalments or loot; a hidden war score or resistance meter.

**16.7 Definition of implementation-ready.** A layer is implementation-ready only when: its rules are stable, its formulas are calibrated or explicitly parameterised, its workflows and WFA rows are reviewed, its cross-system contracts name one mutation owner, and its failure codes are closed. At the end of 10C, **no layer meets the calibration condition**, which is why implementation status is **not started**, not "blocked by a defect".

---

## 17. Acceptance record — Prompt 10C

**17.1 How to read this record.** This section records the final status of every mandatory gate P10C-01–P10C-44. A gate is **PASS** only where the evidence named in the row was inspected or executed during this pass; a document asserting its own completeness is not evidence. `PASS` is therefore always paired with a section, an identifier or a command. Four statuses are possible: **PASS**, **FAIL**, **BLOCKED** (waiting on an external owner or dependency) and **NOT RUN** (no evidence was produced). No gate in this pass is BLOCKED or NOT RUN; one supplementary unit suite is explicitly NOT RUN and is disclosed in §17.3 item 3.

**17.2 Gate table.**

| Gate | Required PASS condition | Status | Evidence |
|---|---|---|---|
| P10C-01 | Canonical workflow document exists at the exact required path | **PASS** | `docs/stage-2/17_warfare_workflows_acceptance.md` exists, **v1.0**, 2026-11-04, §§1–17; `[01]` asserts the header and design-only status; the 10B validator's `[9-boundary]` check asserts its presence |
| P10C-02 | All applicable B-10 rules are respected | **PASS** | §2 fixes the canonical semantics; `[02]` asserts the eight fixed constraints verbatim; `[31]` proves the WAR ranges cover `WAR-001`–`WAR-188` exactly; `[32]` proves all 42 lettered sub-rules match B-10; `[37]` rejects prohibited constructs; `[38]` rejects promoted provisional values; `[39]` matches cross-document counts; no B-10 rule, state, code, cost or formula was changed by 10C |
| P10C-03 | Complete campaign lifecycle is covered | **PASS** | §2.4 lists the 25 steps from `P0` to `P7`; `[04]` asserts all 25; WFW-001–006 and WFW-040 bind the opening, activation, suspension, termination and close; §6 is the workflow-to-state ledger |
| P10C-04 | Declaration, acceptance and participation workflows are complete | **PASS** | §5.1 Group A: WFW-001 (declare), WFW-002 (rejected), WFW-003 (withdraw), WFW-004 (activation), WFW-005 (suspension), WFW-006 (expiry, abandonment, stalemate); §4.1 state machine; WFA-009–016 |
| P10C-05 | Readiness and force preparation workflows are complete | **PASS** | §4.5 readiness model; WFW-025 (P3.7 Food ration), WFW-026 (readiness upkeep), WFW-027 (OP regeneration and force snapshot), WFW-028/029 (recruitment, disbanding); §7.3 military Food accounting; WFA-033–040 |
| P10C-06 | Every authorized operation has a complete workflow | **PASS** | WFW-007–016 cover OP-01 RAID, OP-02 ASSAULT, OP-03 AIR_STRIKE, OP-04 BLOCKADE, OP-05 MISSILE_STRIKE (nation and city targets), OP-06 INTERCEPT, OP-07 FORTIFY, OP-08 BREAK_BLOCKADE and OP-09 RESUPPLY; `[03]` proves nine operations with no espionage; WFW-017–019 close amend/cancel, rejection and idempotent replay |
| P10C-07 | Targeting and support workflows are complete | **PASS** | §7.1 operation/target/counter/phase matrix; WFW-011 and WFW-012 (nation and city targets for OP-05); WFW-016 (support through OP-09); the §2 counter-strength table; WFA-025–032 |
| P10C-08 | Battle-resolution sequence is complete | **PASS** | WFW-020 resolves one battle; §4.8 fixes the P5 internal order key `(campaign_priority, attacker_nation_id, operation_priority, submitted_at, action_id)`; §2.7 fixes determinism and idempotency; WFA-041–048 (Class F) |
| P10C-09 | Loss reporting and recovery are complete | **PASS** | WFW-021 (losses and caps), WFW-022 (readiness loss and temporary states), WFW-028/029 (force recovery), WFW-030 (city repair); §5.3 and §5.4; WFA-049–056 (Class G) |
| P10C-10 | Counterplay and defensive responses are complete | **PASS** | WFW-013 INTERCEPT, WFW-014 FORTIFY, WFW-015 BREAK_BLOCKADE, WFW-016 RESUPPLY, WFW-031 protection activation, WFW-032 political-state interaction, WFW-033 reroll; §4.6 blockade and fortification states; §4.7 protection and eligibility; WFA-065–072 (Class I) |
| P10C-11 | Ceasefire, surrender and settlement workflows are complete | **PASS** | §5.5 Group E: WFW-034 (ceasefire offer), WFW-035 (settlement terms), WFW-036 (response), WFW-037 (surrender), WFW-038 (P5.3 completion), WFW-039 (atomic failure); §4.3 settlement states; §7.5 term matrix; WFA-057–064 |
| P10C-12 | Failure, cancellation and interruption handling is complete | **PASS** | §10 binds every defined `WRF-` code to its emitting workflow, mutation limits and test; WFW-002, 017, 018, 019, 039 and 040 cover rejection, cancellation, replay, atomic failure and interrupted-P5 recovery; §11.2 names every atomic unit; WFA-081–088 |
| P10C-13 | Player journeys cover successful and failed paths | **PASS** | §8 contains 17 journeys `J1`–`J17`; `[07]` asserts all 17 in order; the set includes a rejected declaration, a failed operation, abandonment, defence and interception, a settlement breakdown and the loss cap |
| P10C-14 | Edge-case register is comprehensive and cross-referenced | **PASS** | §9 carries `WFE-001`–`WFE-060`; `[08]` counts 60; `[09]` proves the same IDs appear in both WFA tables; `[13]` proves each edge-case class matches its primary test; `[14]` proves every test edge-case reference resolves and `[19]` proves every edge case is cited back |
| P10C-15 | Concurrency, idempotency and atomicity are addressed | **PASS** | §11.1 six serialization rules (single writer, slot arbitrage, OP double-spend, blockade and fortification state, settlement completion, turn boundary); §11.2 atomic-unit table with commit points; §11.3 idempotency keys; WFA-081–088 (Class K) |
| P10C-16 | Security and exploit-prevention checks are complete | **PASS** | §11.4 eleven exploit-prevention criteria each with a test; §11.5 seven design-level security criteria; §13.17 Class O `WFA-113`–`WFA-120`; `[36]` proves no runtime claim was smuggled into the acceptance text |
| P10C-17 | Privacy and information-visibility rules are complete | **PASS** | §12.2 visibility matrix (audience × data class, `P`/`O`/`B`/`A`/`—`); §12.4 five publication prohibitions including the D-027 five-nation aggregate rule; §11.5 items 4 and 6 (least disclosure, no secret learning); WFA-089–096 (Class L) |
| P10C-18 | B-02 integration is verified | **PASS** | §14.9 row 1: mutations only at acceptance, P3.7, P4.1 and P5, with no P0/P7 OP mutation; WFW-001, 027 and 040; WFA-112 (Class N); §4.4 OP ledger model |
| P10C-19 | B-03 integration is verified | **PASS** | §14.9 row 2: protection, restricted pairs and dormancy block on every path; WFW-002, 005 and 031; WFA-009, WFA-015 and WFA-073 |
| P10C-20 | B-04 integration is verified | **PASS** | §14.9 row 3: reservations, ledger types, upkeep rank and reparations; WFW-018, 026 and 038; WFA-035, WFA-060 and WFA-108; §7.3 records the whole-obligation cancellation and no-debt rule |
| P10C-21 | B-05 integration is verified | **PASS** | §14.9 row 4: city identity, infrastructure-only damage, capacity and housing recalculation, impairment and P4.1 repair; WFW-023 and 030; WFA-051, WFA-105 and WFA-106; §7.4 infrastructure timing |
| P10C-22 | B-06 integration is verified | **PASS** | §14.9 row 5: housing damage feeds B-06 crowding, and political `TRANSITION`/`CRISIS` restricts new offensives with the narrow accepted-defensive exception; WFW-032; WFA-105 and WFA-110 |
| P10C-23 | B-07 integration is verified | **PASS** | §14.9 row 6: war does not block trade, one rule one owner, no warfare mutation of a market object; WFW-007; WFA-107 |
| P10C-24 | B-08 integration is verified | **PASS** | §14.9 row 7: a national NAP blocks only the declaration, `AT-E00` and `AT-E01` remain distinct, and no diplomatic delegation exists; WFW-002; WFA-100 |
| P10C-25 | B-09 integration is verified | **PASS** | §14.9 row 8: same-Alliance ban, `AT-E01` in the Alliance checks, `AUD-AL-017` on the two alliance block codes, and no Alliance command, delegated order, shared OP, military treasury or private member data; WFW-002 and 031; WFA-097, WFA-098 and WFA-102 |
| P10C-26 | Prompt 11–15 handoffs are documented | **PASS** | §14.9 rows 9–13 bind Prompt 11 (events, objectives, rankings input), Prompt 12 (evidence and moderation duties), Prompt 13 (board, confirmation minimum, bands, failure copy), Prompt 14 (formulas and calibration) and Prompt 15 (integration matrix and registers); §14.8.3 states each downstream boundary; §16 repeats them for the implementer |
| P10C-27 | All 50 requirements are dispositioned | **PASS** | §14.2 lists `REQ-654`–`REQ-703` once each; `[21]` asserts the set; `[16]` resolves every requirement cited by a test against the authoritative register; `[22]` proves the classification totals **44 DIRECT / 1 SUPPORTING / 5 DEFERRED / 0 NOT COVERED** |
| P10C-28 | All numbered and lettered B-10 rules are dispositioned | **PASS** | §14.3 gives 26 contiguous ranges covering 188 numbered rules; §14.3.1 lists all 42 lettered sub-rules individually; §14.3.2 states the 230 WAR identifiers; `[31]` and `[32]` recompute both from B-10 |
| P10C-29 | All 39 formulas are dispositioned | **PASS** | §14.4 lists `F-WR-001`–`F-WR-039` with their workflows and tests; `[24]` asserts 39 rows and matches the authoritative register; `[25]` proves every formula row names live workflows and tests |
| P10C-30 | All B-10 architecture decisions are dispositioned | **PASS** | §14.7.1 dispositions `B10-AD-01`–`B10-AD-25`; §14.7.2 dispositions `B10-C01`–`B10-C34`; `[28]` asserts 25 decisions and `[29]` asserts 34 conflict entries against B-10 |
| P10C-31 | Bidirectional traceability has zero unexplained orphans | **PASS** | §14.1 defines the four dispositions; §14.3.3–§14.3.5 are the reverse indexes; §14.11 records ten orphan totals; `[15]` proves every test workflow reference resolves, `[33]` recomputes all ten totals, `[41]` asserts the ten-row audit and that §14.12's named representative subset is drawn from the executable catalogue; `[47]` aligns all **90 fixtures** (13 positive / 67 negative / 10 N/A) in the canonical registry with their executable executors, exact mutations, targets, expected checks and reasons; **0 unexplained orphans** |
| P10C-32 | Acceptance matrix has positive, negative and boundary coverage | **PASS** | §13.2 defines 16 classes (A–O × 8 + P × 4 = 124); §13.18 records the four supplementary tests; `[09]`–`[12]` assert 124 paired rows, 16 classes with the correct sizes, the 22-field record and `Definition: COMPLETE` / `Execution: NOT RUN`; §13.16 and §13.17 bind integration and security; §14.8.2 names negative and boundary cases |
| P10C-33 | Every relevant failure code has test coverage | **PASS** | §10.2 records 32 defined codes and the five unallocated gaps `WRF-15`–`WRF-19` (D-143 / DD-191); §10 binds each code to a workflow and a test; §14.6 is the code-to-test register; `[27]` asserts the 32-code set, the gap disclosure and that every defined code is cited by a test while no gap is |
| P10C-34 | D-014 autonomous decision compliance is demonstrated | **PASS** | §15.1–15.6 audits every 10C decision against [D-014](../AUTONOMOUS_DECISION_POLICY.md); §15.2 records Category A–D, no routine deferral and no Category C/D action; §15.4 separates authoring autonomy from explicit player consent; §15.6 records the policy review with no waiver; `[34]` asserts the policy, register and document statements |
| P10C-35 | Owner-reserved decisions remain untouched | **PASS** | §15.5 states that 10C resolved none of `UD-040`–`UD-049`; `[34]` proves all ten remain **Open** in the 05 register and that `UD-032` is **Resolved**; the register was inspected at **27 Resolved / 4 Deferred / 18 Open = 49**; no `D-` decision approves an owner-reserved policy |
| P10C-36 | Global Trade and other fixed release gates remain unchanged | **PASS** | §1 item 8 records D-014, D-015, D-027, D-122, DD-136, `REQ-513` and G-1–G-6 unchanged; no 10C edit touched a Global Trade document, gate or statistic |
| P10C-37 | Workflow validator has been created and executed | **PASS** | `docs/qa_backups/verify_warfare_workflows.py` executed on the unmodified repository (2026-11-04): **CHECKS: 49, EXECUTED: 49, FAILED: 0, exit 0**; every check reported its assertion count; check 47 now verifies the 90-fixture canonical registry, executor identity/hash, exact binding and expected rejection (see [log §66](06_stage_2_progress_log.md) and §17.6) |
| P10C-38 | Positive and negative fixtures behave as expected | **PASS** | `--self-test` (2026-11-04, **58.38s** (earlier accepted runs 60.58s, 70.76s, 74.27s, 76.12s, 78.58s and 80.69s), limit 120s, **WITHIN BOUND**, exit 0) returned: registry 49/49 sequential; clean **49/49** with assertions; **13/13** positive accepted; **49/49** per-check mutations detected; **67/67** negative fixtures bound, executed and rejected at the expected check; **10/10** N/A fixtures matched; **C3-NF 5/5**; **C3-NA 15/15**; 0 skipped. The four NF-53 corruptions (different executor, replaced description, wrong target, wrong expected check) are rejected, while the original NF-53 is accepted and still rejected by check 45 |
| P10C-39 | Relevant subsystem regression validators pass | **PASS** | Executed in C3 (2026-11-04), all exit 0 unless stated: `10B_validate_warfare.py` (1036 checks, 73/73 negative, CF-01/CF-02 clean); `validate_final.py` (ALL CHECKS PASSED); `09_validate.py` (359/359); `09A_validate_alliance.py` (943); `09B_validate_alliance_semantic.py` (34/34); `verify_economy_numbers.py` (164/164); `verify_city_numbers.py` (267/267); `verify_politics_numbers.py` (879/879); `verify_alliance_numbers.py` (375 passed, 0 failed); `verify_alliance_workflows.py` (49 workflows / 65 edge cases / 132 tests); `verify_alliance_workflows.py --self-test` (24/24); `verify_diplomacy_numbers.py` (9 groups, 0 failed); `verify_diplomacy_workflows.py` (17 groups, 0 failed); `verify_market_numbers.py` (ALL CHECKS PASSED); `verify_market_workflows.py` (ALL CHECKS PASSED); `test_decision_registers.py` (12 tests OK); `test_next_action.py` (25 tests OK); `test_09A_alliance_validator.py` (43 tests OK); `09_register_counts.py` (exit 0). B-02 lifecycle is exercised by `10B_validate_warfare.py` (TR-040/TR-050/TR-059) and by `[30]`/`[45]` integration row 1. The workflow validator is reported in P10C-37/38. The 267-test historical `test_09B_alliance_semantic_validator.py` was retried under a 180s bound and **did not complete** (exit 124) — it is **NOT RUN** and is not counted as a pass (§17.3 item 3) |
| P10C-40 | Markdown link validator passes | **PASS** | `validate_links.py` final C3 scan (2026-11-04, after §66 and §17.6 were written): **66 files, 3078 links, 2696 checked locally, 382 external skipped, 29 anchors checked, 0 unresolved**, exit 0; `--self-test` **11/11**, exit 0 |
| P10C-41 | All required current-status documents are synchronized | **PASS** | 00 handoff, 01 roadmap, 02 outline, 03 requirements, 04 and 05 registers, 06 progress log (**§66**, with §63–§65 preserved), `DECISIONS.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md` and `ROADMAP.md` state 10A/10B/10C and C3 complete, D-001…D-143, DD-001…DD-191 and Prompt 11 next; the 124-test/16-class/49-check/90-fixture counts are synchronized; `[48]` enforces 124/16 agreement and `validate_final.py` passes |
| P10C-42 | Specification-versus-implementation status is accurate | **PASS** | Every `WFA-` row declares `Definition: COMPLETE` and `Execution: NOT RUN`; §16.1 states implementation is not authorized; §16.7 records that no layer is implementation-ready; `[10]`, `[36]` and `[38]` reject any runtime, implementation or promotion claim; the header states that no code, schema, endpoint, screen or deployment exists |
| P10C-43 | Final implementation handoff is complete | **PASS** | §16.2–16.7 cover the received artefacts, prerequisites, recommended order, ten non-negotiables, the must-not-build list and the definition of implementation-ready; §16.7 names calibration as the missing condition |
| P10C-44 | Actual evidence supports the reported PASS | **PASS** | Every row above names an inspected section, identifier or executed command; the C3 corruption proof, N/A enforcement results and bounded self-test are separately recorded in §17.6; the limits are stated in §17.3 and §16.1; no gate rests on the document's own assertion, and no gate was promoted merely because C3 was written |

**17.2.1 C3 re-evaluation.** All 44 gates were re-read against the C3 evidence; the rows whose evidence text changed are P10C-31, P10C-37, P10C-38, P10C-39, P10C-40, P10C-41 and P10C-44. Gates P10C-27–P10C-36 were re-checked against the final clean run rather than promoted: the 50 requirements, 188 numbered and 42 lettered rules, 39 formulas, 25 architecture decisions, 34 conflicts, 32 failure codes, 124 tests in 16 classes, ten orphan totals, D-014 audit and the ten Open `UD-040`–`UD-049` entries are unchanged and still asserted. No gate changed from FAIL/BLOCKED/NOT RUN to PASS because the C3 text was written, and no gate is marked PASS on the strength of a document statement alone.

**17.3 Gate notes and limits.** Three disclosures belong with this record because they change what "all validators pass" means.

1. **Status-expectation maintenance in four validators.** Advancing the live prompt from 10C to 11 required updating literal expectations in `09_validate.py` (prompt `11`, `DD-001…DD-191`, row-10 wording), `09A_validate_alliance.py` (accepted next-prompt values), `09B_validate_alliance_semantic.py` (D-001…D-143, DD-001…DD-191, Confirmed 4, total 191, 143 project decisions, next prompt 11) and `verify_politics_numbers.py` (row 10 now requires 10C complete and Prompt 11 next). No rule, arithmetic, fixture or negative check was removed or weakened; each edit makes the gate assert the current, correct state. `validate_final.py` also now accepts a header dated on or after 2026-11-03 instead of the literal 2026-11-03.
2. **10B validator boundary inversion.** `10B_validate_warfare.py` §9 previously asserted that this document did **not** exist, because 10C had not started. Before the change it failed with exactly three problems (`[9-boundary]` twice and `[10-continuity]` once) on account of 10C's completion. The dated maintenance pass inverts those two checks to assert the companion exists and is non-empty, and moves the expected live prompt to 11 while requiring 10C in the completed set. The B-10 boundary the check protects — 10C may not invent B-10 content — is unchanged and still enforced.
3. **What no gate proves.** No gate proves runtime behaviour. The 124 acceptance tests, 60 edge cases and every formula are **designs**; none has been executed against code, because no code exists. No database, migration, endpoint, scheduler, screen or deployment was created, and no load, security, browser or live-integration test was run. All warfare numbers remain provisional pending Prompt 14. A separate limitation is external to 10C and disclosed rather than hidden: the Phase 09B unit suite `test_09B_alliance_semantic_validator.py` (267 tests) does not complete in a bounded run and is **not reported as passing**; the 34-check `09B_validate_alliance_semantic.py` validator, which covers the same acceptance surface at document level, does pass.

**17.4 Result.** All 44 mandatory gates are **PASS**, no critical contradiction is unresolved, no mandatory workflow is missing, the traceability ledger has zero unexplained orphans and every mandatory validator that was run passed. Prompt 10C is therefore **PASS — COMPLETE AT THE SPECIFICATION/DOCUMENTATION LEVEL**. This is an acceptance of a specification, not of a game: implementation status is **not started**, and Prompt 14 still owns numerical calibration.

**17.5 If a later reader finds a defect.** A defect found after this record does not silently demote or promote 10C. It is recorded as a dated correction entry in the [progress log](06_stage_2_progress_log.md), the affected section here is amended in place, and the gate table above is re-issued with the corrected evidence. Historical entries are preserved, never rewritten.

**17.6 C3 correction evidence (2026-11-04).** Prompt 10C-C3 corrected two validator defects found after C2: check 47 did not bind a negative fixture's executor, target, expected check or documented description to its executed mutation, and `justified_value()` accepted `N/A — WAR-999` because any identifier-shaped token bypassed the reason rule. The table records what was actually executed in C3; it does not reuse a C1/C2 result as C3 evidence.

| Check / fixture | Test actually executed | Actual result | Supporting file / command | Limitation |
|---|---|---|---|---|
| check 47, all 90 fixtures | registry completeness, executor hash, exact binding, expected rejection and reason, catalogue projection | **PASS** — 13 positive, 67 negative, 10 N/A aligned; no undocumented or unexecutable fixture | `verify_warfare_workflows.py`; `warfare_fixture_registry.json`; `warfare_fixture_catalogue.md`; clean run `[47]` 4 assertions | Executes in memory against copies; it is not a runtime test of warfare |
| `NF-53` original | C3-NF-05: original definition accepted by check 47, then rejected by check 45 with the declared reason | **PASS** — accepted as the genuine fixture and still rejected | `--self-test`, C3-NF 5/5 | In-memory copy; no project file altered |
| C3-NF-01 | replace the `NF-53` executor with the different valid executor `c54` | **PASS (tamper rejected)** — check 47 reports an executor/source-hash mismatch | `--self-test`, C3-NF 5/5 | Meta-tests intentionally tamper with the registry in memory |
| C3-NF-02 | replace the documented `NF-53` description | **PASS (tamper rejected)** — documented description no longer matches | `--self-test`, C3-NF 5/5 | As above |
| C3-NF-03 | change the `NF-53` mutation target and declared values | **PASS (tamper rejected)** — the executor does not produce the declared change | `--self-test`, C3-NF 5/5 | As above |
| C3-NF-04 | change the expected rejecting check to 46 | **PASS (tamper rejected)** — check 46 does not reject, and the declared check differs from the executable fixture | `--self-test`, C3-NF 5/5 | As above |
| `justified_value`, C3-NA-01…15 | bare `N/A`, `NONE`, empty, whitespace, bare punctuation-only values (`...`, `—`, `---`), `N/A — WAR-999`, `N/A — WFW-999`, `N/A — WFA-999`, generic reasons, invalid identifiers inside a reason, and valid field-specific explanations | **PASS** — 15/15 matched the required verdict | `--self-test`, C3-NA 15/15; `[46]` 849 assertions | N/A fixtures call the production function directly; no runtime corpus |
| WFA `N/A` audit | all 124 tests × six mandatory fields, plus integration columns 6–13 | **PASS** — no bare, meaningless or unresolved-identifier N/A value | clean run `[46]` 849 assertions; `[45]` 451 assertions | Documentation-level consistency only |
| bounded self-test | complete suite, including NF-53, C3-NF, C3-NA, positives and all negative fixtures | **PASS** — 58.38s elapsed (earlier accepted runs 60.58s, 70.76s, 74.27s, 76.12s, 78.58s and 80.69s), limit 120s, status WITHIN BOUND, exit 0 | `--self-test` START 2026-11-04T20:31:36, FINISH 20:32:35 | Timing is machine-specific; the timeout is enforced only at the end of the run |
| main validator | all 49 checks on the unmodified repository | **PASS** — `CHECKS: 49  EXECUTED: 49  FAILED: 0`, exit 0 | `python docs/qa_backups/verify_warfare_workflows.py` | Documentation validator, not a game test |
| `--report`, 27 totals | every separate total computed on the unmodified repository | **PASS** — 0 invalid WAR, WFW, WFE, WFA and formula references; 188/188 numbered and 42/42 lettered WAR mappings verified; 124 WFA records, 0 missing/invalid N/A reasons; 67/67 negative fixtures aligned | `python docs/qa_backups/verify_warfare_workflows.py --report` | Informational totals only; the reference scan excludes deliberate negative-example prose in §14.12 and §17.6, and that exclusion affects no check or gate |
| `test_09B_alliance_semantic_validator.py` | bounded retry of the 267-test historical suite | **NOT RUN** — stopped by a 180s bound with exit 124; not counted as a pass | `timeout 180 python docs/qa_backups/test_09B_alliance_semantic_validator.py` | Suite does not complete in a bounded run; the 34-check document validator passes |

No project document was used as a corruption target. The fixtures mutate in-memory copies; the authoritative files were read, never rewritten, by the fixture harness.
