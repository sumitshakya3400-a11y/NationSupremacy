# B-10 warfare formula register

**Version:** 1.3 · **Created:** 2026-11-03 · **Stage 2, Prompt 10B** · **Revised:** 2026-11-04 (v1.2 Prompt 10B-C2 keeps every identifier and fixes the correction defects in place: `F-WR-016`/`F-WR-019` gain the protected civilian Food condition, `F-WR-036` reads the canonical P3.7 force snapshot `WAR-053m`, and `F-WR-037`/`F-WR-038` move to the infrastructure-only carrying-value basis with the B-05 repair curve. No formula is renumbered, removed or added. · v1.3 Prompt 10B-C3 rewrites `F-WR-001` to the persistent OP ledger with +1 regeneration at the P3.7 opening and updates `F-WR-002` so a release restores availability without refunding the balance; no other formula changes.) · **Status:** **Specification complete at the documentation level. Unimplemented, uncalibrated and untested.**

**Authority.** This register is the authoritative statement of every B-10 calculation. The [B-10 rulebook](17_warfare_and_settlements.md) defines the rules; where it describes arithmetic in prose, this register's expression governs. If the two ever diverge, this register wins and the rulebook is corrected.

**Companions.** [B-10 rulebook](17_warfare_and_settlements.md) · [10A research](research/10A_politics_and_war_warfare_research.md) · [requirements traceability](03_requirements_traceability.md) · [decisions](04_approved_and_provisional_decisions.md).

**Status of values.** Every numeric constant in this register is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** unless the entry's field 17 says **Structural**. A structural formula may still contain a provisional constant; the structure is fixed, the constant is not.

---

## 1. Purpose

`WF-001` This register exists so that Prompt 14 can calibrate and Prompt 10C can write acceptance cases without re-deriving any B-10 arithmetic. Every formula below has the same 20 fields, the same rounding convention and the same determinism rule. No formula is defined only in prose in the rulebook.

`WF-002` This register creates no new resource, currency, score, ledger type or event type. Its inputs are the B-10 entities in rulebook §4.1 and the B-04 resource roster. A formula needing a new type is a design defect, not a missing entry.

---

## 2. The 20 mandatory fields

| # | Field | Meaning |
|---|---|---|
| 1 | **Identifier** | Stable `F-WR-###` code, never reused |
| 2 | **Name** | Short human name |
| 3 | **Purpose** | What decision the calculation supports |
| 4 | **Expression** | The exact arithmetic, in integer or basis-point form |
| 5 | **Inputs** | Every variable with type and valid range |
| 6 | **Output** | Type, unit and range |
| 7 | **Rounding** | Floor, ceiling or largest-remainder rule; no floating point |
| 8 | **Clamping** | Every bound applied and the order of application |
| 9 | **Worked example** | One concrete, arithmetic-checked case |
| 10 | **Boundary example** | The smallest, largest or degenerate case |
| 11 | **Failure behaviour** | What happens on invalid or missing input; fail-closed rule |
| 12 | **Determinism and seed** | Whether the result is reproducible and what seed is used |
| 13 | **Phase and trigger** | The B-02 phase and event that evaluates it |
| 14 | **Mutation owner** | The single component that writes the result |
| 15 | **Visibility** | Who may see the input and the output |
| 16 | **Audit event** | The `WRA-` record written when the result is applied |
| 17 | **Provisional status** | Structural, or provisional with the calibration owner |
| 18 | **Calibration owner** | The prompt that may change the constants |
| 19 | **Source rule** | The exact `WAR-` rule or section |
| 20 | **Downstream consumer** | The system or prompt that reads the result |

---

## 3. Global conventions

`WF-003` **Integer arithmetic.** All money, resources, strength points, OP and progress are integers. All combat and loss proportions are basis points (`bp`, where 10,000 bp = 100%). There is no floating-point step, and no intermediate value is rounded except where an expression says so.

`WF-004` **Division.** Integer division always floors toward zero unless the expression says `ceil`. A division by zero is never allowed: every formula defines its zero-denominator branch.

`WF-005` **Clamping order.** Clamp after the final arithmetic step unless the expression states an intermediate clamp. A clamped value is never fed back into the same formula in the same evaluation.

`WF-006` **Determinism.** Every formula is a pure function of its declared inputs plus, where stated, the frozen turn seed. No formula reads wall-clock time, player activity, login state, latency or random device entropy.

`WF-007` **Seed.** The only seed is the frozen turn digest seed already used by B-02's seeded lottery (`TR-046`). A battle-specific draw is `seeded_integer(seed, battle_id, low, high)`, inclusive at both ends and stable for the same `(seed, battle_id)`.

`WF-008` **Fail closed.** If an input is missing, out of range or inconsistent with the frozen baseline, the formula does not guess. The action fails with the rulebook's failure code, every reservation is released and no partial value is written.

`WF-009` **One writer.** Each formula has exactly one mutation owner. No second component recomputes and overwrites a value that another component owns.

`WF-010` **No hidden state.** Every input is either an entity field, a B-04 ledger value, a published constant or the frozen seed. No formula depends on a value a player cannot, in principle, derive from published rules and their own records.

---

## 4. Formula index

| ID | Formula | Rulebook anchor | Structural? |
|---|---|---|---|
| `F-WR-001` | OP availability, regeneration and cap | §8.1, `WAR-039`–`WAR-043b` | Structure yes, cap and rate no |
| `F-WR-002` | OP reservation lifecycle | §8.1, `WAR-005a`, `WAR-042` | Yes |
| `F-WR-003` | Readiness upkeep and P3.7 obligation | §9.2, §11.2, `WAR-050`–`WAR-052` | No |
| `F-WR-004` | Cumulative declaration eligibility | §5.3, `WAR-009`–`WAR-014` | Yes |
| `F-WR-005` | Readiness value and gate | §9.1, `WAR-047`–`WAR-049` | No |
| `F-WR-006` | Campaign slot occupancy | §5.2, `WAR-005`, `WAR-007` | No |
| `F-WR-007` | Campaign deadline and extension | §6.3, `WAR-018`–`WAR-020` | No |
| `F-WR-008` | Inactivity, stalemate and abandonment | §6.3–§6.4, `WAR-016`, `WAR-021`–`WAR-024` | No |
| `F-WR-009` | Objective progress | §7.2, `WAR-036` | No |
| `F-WR-010` | Victory determination | §7.3, `WAR-037`–`WAR-038` | Yes |
| `F-WR-011` | Progress-contribution cap | §7.2, `WAR-035` | No |
| `F-WR-012` | Force cap | §10.3 | No |
| `F-WR-013` | Training capacity | §10.3 | No |
| `F-WR-014` | Single-type share | §10.3, `WAR-058` | No |
| `F-WR-015` | Recruitment cost and arrival | §10.3, `WAR-058`–`WAR-059` | No |
| `F-WR-016` | Operation supply bundle | §12.2 | No |
| `F-WR-017` | Supply-denial surcharge | §12.1, `WAR-071` | No |
| `F-WR-018` | Blockade modifier | §12.1, `WAR-072` | No |
| `F-WR-019` | Total action cost | §5.2, §13.1, §8.2 | No |
| `F-WR-020` | Readiness factor in combat | §14.2, `WAR-079` | No |
| `F-WR-021` | Combat power and base ratio | §14.2, `WAR-076`–`WAR-081` | Structure yes, constants no |
| `F-WR-022` | Order key, frozen baseline and seed | §15.1–§15.2, `WAR-089`–`WAR-093` | Yes |
| `F-WR-023` | Fortune draw | §14.3, `WAR-082` | No |
| `F-WR-024` | Effective ratio | §14.3, `WAR-083` | Yes |
| `F-WR-025` | Battle tier | §14.3, `WAR-083` table | No |
| `F-WR-026` | Counter modifier | §14.4 | No |
| `F-WR-027` | Strength-point losses | §16.2, `WAR-104` | No |
| `F-WR-028` | Loss caps | §16.2, `WAR-105` | No |
| `F-WR-029` | Reparation caps and atomic transfer | §21.1, `WAR-137`–`WAR-139` | No |
| `F-WR-030` | Settlement proposal window | §19.1, §20.1, `WAR-122`, `WAR-127` | No |
| `F-WR-031` | Exclusion and disarmament | §20.4, `WAR-135`–`WAR-136` | No |
| `F-WR-032` | Odds band | §14.5, `WAR-085` | No |
| `F-WR-033` | Threat band | §14.5, `WAR-086` | No |
| `F-WR-034` | P5 validity, idempotency and recovery | §15.4, `WAR-097`–`WAR-100` | Yes |
| `F-WR-035` | Calibration envelope | §27.3, Prompt 14 handoff | Yes |
| `F-WR-036` | Military food ration | §9.3, `WAR-053a`–`WAR-053m` | Structure yes, rates no |
| `F-WR-037` | City infrastructure damage | §16.4, `WAR-109a`–`WAR-109f`, `WAR-109m` | Structure yes, constants no |
| `F-WR-038` | Infrastructure asset impairment and repair | §16.4, `WAR-109f`–`WAR-109m`; URB-043/044/118/118a/118b/157 | Structure yes, constants no |
| `F-WR-039` | Combined supply modifier | §12.1, `WAR-071`–`WAR-072` | Structure yes, rates no |

---

## 5. Formula entries

### F-WR-001 — OP availability, regeneration and cap

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-001` |
| 2 | Name | OP availability, regeneration and cap |
| 3 | Purpose | Tell a player, and the validator, how many Operations Points are in the pool, how many are spendable and when the pool grows |
| 4 | Expression | The pool is a persistent national ledger. `op_balance` carries between turns; `reserved` is the sum of live `HELD` items; `available = max(0, op_balance − reserved)`. At the opening of P3.7, once per successful boundary: `op_balance = min(op_cap, op_balance + 1)`, writing one `REGENERATED` item keyed on `(nation_id, turn_id)` even when the amount is 0. P0 and P7 write no OP mutation. The regenerated OP is spendable only from the next OPEN window, which begins when P7 publishes the turn as `COMPLETED` |
| 5 | Inputs | `op_cap` int 1…10 (published constant, currently 10); `op_balance` int 0…op_cap; `reserved` int 0…op_balance, sum of live `HELD` items; `turn_id`, `nation_id` |
| 6 | Output | `available` int 0…op_cap; new `op_balance` after P3.7 |
| 7 | Rounding | None; exact integer addition and subtraction |
| 8 | Clamping | `op_balance` clamped above by `op_cap` and below by 0; `available` floored at 0; a reservation above `op_balance` is invalid, not clamped |
| 9 | Worked example | Turn `t` opens with `op_balance 8`; A reserves 2 and B reserves 3 → `reserved 5`, `available 3`; P2 fails B → `reserved 2`, `available 6`; P3.7 writes `REGENERATED 1` → `op_balance 9`, `available 7`; P5 consumes A → `op_balance 7`, `reserved 0`, `available 7`; the next OPEN window sees 7 |
| 10 | Boundary example | `op_balance 0` → P3.7 regenerates to 1. `op_balance 9` → 10. `op_balance 10` → the event records 0 and the balance stays 10. A duplicate `(nation_id, turn_id)` regeneration returns the original receipt and writes nothing. A live reservation at the P7 close is released and does not refund the balance |
| 11 | Failure behaviour | If `op_balance > op_cap`, `op_balance < 0`, `reserved > op_balance`, or a second `REGENERATED` item exists for one boundary, the state is inconsistent: no new action is accepted, `WRF-34` is raised and the turn checkpoint is held |
| 12 | Determinism and seed | Deterministic; no seed |
| 13 | Phase and trigger | Regeneration written once at the opening of P3.7; availability read at submission, P2, pre-P5 and the P7 close; spendable from the next OPEN window after P7 publication. No P0 or P7 regeneration |
| 14 | Mutation owner | The B-10 OP service writes the `REGENERATED` item and the reservation service writes `reserved` changes; B-02 owns the P3.7 and OPEN-window boundaries. P0 writes only the run record |
| 15 | Visibility | Owner sees cap, available, reserved and consumed this turn (`WAR-041`); no other player sees any of them |
| 16 | Audit event | `WRA-14` on every reservation-state and regeneration change; `WRA-14` reconciliation at P7 |
| 17 | Provisional status | Structure structural; cap and regeneration rate **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** as a pair |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §8.1, `WAR-039`–`WAR-043b` |
| 20 | Downstream consumer | Declaration validator, operation validator, Prompt 13 OP display |

### F-WR-002 — OP reservation lifecycle

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-002` |
| 2 | Name | OP reservation lifecycle |
| 3 | Purpose | Guarantee that an accepted action holds its OP exactly once and that a failure returns it exactly once without changing the pool balance |
| 4 | Expression | On acceptance while OPEN: `reserved = reserved + cost`, ledger item `HELD`. On resolution: `reserved = reserved − cost`, `op_balance = op_balance − cost`, `consumed = consumed + cost`, item `CONSUMED`. On P2 failure, pre-P5 failure, cancellation while OPEN or P7 void: `reserved = reserved − cost`, item `RELEASED`; `op_balance` is unchanged because the amount was never debited. `REGENERATED` belongs to F-WR-001. No state permits two terminal items for one `action_id` |
| 5 | Inputs | `cost` int 1…4; `action_id` unique client key; current `reserved`, `op_balance`, per-turn `consumed` |
| 6 | Output | New `reserved`, new `op_balance`, new `consumed`, one ledger item |
| 7 | Rounding | None |
| 8 | Clamping | `reserved` never negative and never above `op_balance`; `op_balance` never negative; `consumed` never decreases within a turn |
| 9 | Worked example | Declaration cost 2: acceptance while OPEN sets `reserved 2`; P5 resolution sets `reserved 0`, debits `op_balance` by 2 and records `consumed 2` |
| 10 | Boundary example | A second terminal attempt for the same `action_id` returns the original receipt and writes no item (0 additional OP). A cancellation after consumption is invalid; a release after release is invalid; both are `WRF-34` |
| 11 | Failure behaviour | A missing ledger item or a duplicate consumption is `WRF-34`; the action is not re-run and no value is guessed |
| 12 | Determinism and seed | Deterministic; keyed by `action_id` |
| 13 | Phase and trigger | Acceptance while the turn is OPEN and before P1 freeze (`HELD`); P2 or pre-P5 failure (`RELEASED`); P5 resolution (`CONSUMED`); cancellation while OPEN (`RELEASED`); unresolved at the P7 close (`RELEASED` + `WRF-22`). P4 resolves already-accepted orders and never accepts a new one |
| 14 | Mutation owner | B-10 requirement service; the B-04 ledger is append-only |
| 15 | Visibility | Owner sees the net OP numbers; the ledger line is owner-visible and partially administration-visible |
| 16 | Audit event | `WRA-14`; `WRA-03` for operation acceptance/rejection |
| 17 | Provisional status | Structural |
| 18 | Calibration owner | None for the lifecycle; Prompt 14 for `cost` |
| 19 | Source rule | §8.1, `WAR-005`, `WAR-040`–`WAR-043b` |
| 20 | Downstream consumer | P5 executor, P7 reconciliation, Prompt 13 |

### F-WR-003 — Readiness upkeep and P3.7 obligation

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-003` |
| 2 | Name | Readiness upkeep and P3.7 obligation |
| 3 | Purpose | Charge a force-proportional upkeep before combat and translate payment into a readiness change without creating debt |
| 4 | Expression | `upkeep_crowns = ceil(total_strength × 5000 / 10000)`. `upkeep_ammunition = ceil(total_strength × 200 / 10000)`. `upkeep_gasoline = ceil(total_strength × 100 / 10000)`. If all three are payable from the value left unreserved **after the military Food ration at P3.7 (a)**: debit them, write `OBLIGATION_PAID`, `readiness = min(1000, readiness + 50)`. Otherwise cancel the whole obligation, write `OBLIGATION_CANCELLED`, `readiness = max(0, readiness − 100)` |
| 5 | Inputs | `total_strength` = Σ of the canonical P3.7 force snapshot (`WAR-053m`), int 0…force cap; unreserved crowns int ≥0; unreserved ammunition int ≥0; unreserved gasoline int ≥0; current readiness int 0…1,000 |
| 6 | Output | Debit amounts, one obligation state, new readiness |
| 7 | Rounding | Ceiling per resource, per turn, after the proportional multiplication |
| 8 | Clamping | Readiness clamped to 0…1,000 after the delta; no negative inventory; no partial payment |
| 9 | Worked example | total_strength 1,000 → 500 crowns, 20 ammunition, 10 gasoline; if paid, readiness 700 → 750 |
| 10 | Boundary example | total_strength 0 → 0 crowns, 0 ammunition, 0 gasoline; the obligation is vacuously paid and readiness still recovers by 50, capped at 1,000. Readiness 990 paid → 1,000. Readiness 40 unpaid → 0 |
| 11 | Failure behaviour | A shortfall in any component cancels the entire obligation: no partial debit, no debt, `readiness −100`. The player is warned before the boundary (`WAR-052`) |
| 12 | Determinism and seed | Deterministic; no seed |
| 13 | Phase and trigger | P3.7, inside `ECN-105` rank 6, sub-order (b), after the military Food ration at (a) |
| 14 | Mutation owner | B-04 obligation engine reads B-10 strength and writes the debit; B-10 writes the readiness delta |
| 15 | Visibility | Owner sees the obligation and the shortfall; no opponent visibility |
| 16 | Audit event | `OBLIGATION_PAID` / `OBLIGATION_CANCELLED`; `WRA-14` for the inventory legs |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all four coefficients) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §9.2, §11.2, `WAR-050`–`WAR-052` |
| 20 | Downstream consumer | P5 combat (reads the post-P3 readiness), Prompt 13 upkeep warning |

### F-WR-004 — Cumulative declaration eligibility

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-004` |
| 2 | Name | Cumulative declaration eligibility |
| 3 | Purpose | Produce one fail-closed answer for every declaration entry point |
| 4 | Expression | `eligible = authority ∧ target_valid ∧ not_restricted ∧ not_protected ∧ no_national_nap ∧ not_same_alliance ∧ no_alliance_nap ∧ not_political_block ∧ slot_free ∧ op_available ∧ crowns_available`. Evaluated left to right, stopping at the first false; the output is `PASS` or `FAIL(code)`. `DP-T01` is tested **only in the `no_national_nap` term**: it is declaration-only and is never applied to an operation against a nation that is already at war |
| 5 | Inputs | Actor identity and state; target identity and state; B-03 pair and protection results; B-08 `DP-T01` declaration-only result; B-09 `ALL-206`–`ALL-208` and `AT-E01` results; political state; slot count; OP availability; unreserved crowns |
| 6 | Output | `PASS`, or `FAIL` with exactly one `WRF-01`…`WRF-13` |
| 7 | Rounding | None |
| 8 | Clamping | Not applicable; boolean |
| 9 | Worked example | Valid actor and target, no blocks, slot free, 10 OP, 2,000 crowns → `PASS`; reservation then takes 2 OP and 500 crowns |
| 10 | Boundary example | Same state but an active `DP-T01` → `FAIL(WRF-06)`; no reservation, no mutation |
| 11 | Failure behaviour | Fail closed; nothing moves; one stable code; `AUD-AL-017` only for `WRF-07`/`WRF-08` |
| 12 | Determinism and seed | Deterministic given execution-time state; checks 3–7 are re-run at P2 and P5 |
| 13 | Phase and trigger | Submission, P2 revalidation, pre-P5 revalidation |
| 14 | Mutation owner | B-10 declaration service calls B-03, B-08 and B-09 validators; no validator writes |
| 15 | Visibility | Actor sees its own code and the blocking rule; never private treaty text (`WAR-149`) |
| 16 | Audit event | `WRA-02`; `AUD-AL-017` additionally for B-09 blocks |
| 17 | Provisional status | Structural |
| 18 | Calibration owner | None |
| 19 | Source rule | §5.3, `WAR-009`–`WAR-014` |
| 20 | Downstream consumer | Declaration receipt, Prompt 13 failure copy, Prompt 12 review |

### F-WR-005 — Readiness value and gate

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-005` |
| 2 | Name | Readiness value and gate |
| 3 | Purpose | Maintain one national readiness integer and decide whether an operation passes its gate |
| 4 | Expression | `readiness' = clamp(readiness + 50·paid − 100·unpaid − 50·interdictions − 25·blockaded − 25·battles, 0, 1000)`. Gate: `pass = readiness ≥ gate(op)`, where `gate = 300` for RAID, FORTIFY, INTERCEPT, RESUPPLY and `gate = 500` for ASSAULT, AIR_STRIKE, BLOCKADE, BREAK_BLOCKADE, MISSILE_STRIKE |
| 5 | Inputs | `readiness` int 0…1,000; booleans `paid`, `unpaid`, `blockaded`; `interdictions` int ≥0 this turn; `battles` int ≥0 this turn; operation type |
| 6 | Output | New readiness int 0…1,000; gate boolean |
| 7 | Rounding | None; integer deltas |
| 8 | Clamping | Final clamp 0…1,000; gate evaluated on the clamped value |
| 9 | Worked example | readiness 700, paid upkeep, no battles → 750; `OP-02 ASSAULT` gate 500 → pass |
| 10 | Boundary example | readiness 300 → RAID passes, ASSAULT fails (`WRF-23`); readiness 0 → every operation fails its gate |
| 11 | Failure behaviour | A gate failure at P5 is `WRF-23`, all reservations released, no effect |
| 12 | Determinism and seed | Deterministic; no seed; never a function of activity or real time (`WAR-049`) |
| 13 | Phase and trigger | P3.7 for upkeep; P5 for battle loss; submission, P2 and pre-P5 for the gate |
| 14 | Mutation owner | B-10 readiness service |
| 15 | Visibility | Owner exact; opponent band only (§23.1) |
| 16 | Audit event | `WRA-11` for resupply; `WRA-04` records readiness loss in a battle; gate failure in `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all deltas and gates; start 700) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §9.1, `WAR-047`–`WAR-049` |
| 20 | Downstream consumer | F-WR-020, Prompt 13 readiness display, Prompt 14 balance |

### F-WR-006 — Campaign slot occupancy

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-006` |
| 2 | Name | Campaign slot occupancy |
| 3 | Purpose | Bound simultaneous exposure without a per-war action economy |
| 4 | Expression | `outgoing = count(campaigns where declarer = n and state ∈ {DECLARED_PENDING, ACTIVE, SUSPENDED, SETTLING})`; `incoming = count(campaigns where target = n and state ∈ same set)`; `slot_free = outgoing < 1 ∧ incoming < 1 ∧ (outgoing + incoming) < 2` |
| 5 | Inputs | Nation identifier; campaign list with declarer, target and state |
| 6 | Output | Three integers and one boolean |
| 7 | Rounding | None |
| 8 | Clamping | Counts cannot exceed the number of live campaigns |
| 9 | Worked example | One active campaign as declarer, none as target → outgoing 1, incoming 0, slot_free false |
| 10 | Boundary example | One outgoing and one incoming → total 2, no further declaration; a terminated campaign is excluded immediately |
| 11 | Failure behaviour | No slot → `WRF-10`; no reservation |
| 12 | Determinism and seed | Deterministic on state at evaluation time |
| 13 | Phase and trigger | Submission, P2, P5 |
| 14 | Mutation owner | B-10 campaign service |
| 15 | Visibility | Owner sees own counts; the public sees campaign existence |
| 16 | Audit event | `WRA-02` on refusal; `WRA-01` on acceptance |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (slot counts) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §5.2, `WAR-005`, `WAR-007` |
| 20 | Downstream consumer | F-WR-004, Prompt 13 slot display |

### F-WR-007 — Campaign deadline and extension

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-007` |
| 2 | Name | Campaign deadline and extension |
| 3 | Purpose | Guarantee every campaign has a finite end |
| 4 | Expression | `deadline = declaration_resolved_turn + 84 + (42 if extended_once else 0)`; `expired = current_turn ≥ deadline` |
| 5 | Inputs | `declaration_resolved_turn` int ≥1; `extended_once` boolean; `current_turn` int ≥1 |
| 6 | Output | Deadline turn int; expiry boolean |
| 7 | Rounding | None |
| 8 | Clamping | `extended_once` is at most one; a second extension is invalid |
| 9 | Worked example | Resolved turn 120 → deadline 204; extended → 246 |
| 10 | Boundary example | Resolved turn 1 → deadline 85; expiry is evaluated at P5.4 before operations, so an operation on turn 85 does not resolve |
| 11 | Failure behaviour | A missing resolved turn is `WRF-34`; no campaign is created without one |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Creation; P5.2 and P5.4 |
| 14 | Mutation owner | B-10 campaign service |
| 15 | Visibility | Public: existence, objectives, deadline |
| 16 | Audit event | `WRA-05` on extension; `WRA-13` on expiry |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (84 and 42) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §6.3, `WAR-018`–`WAR-020` |
| 20 | Downstream consumer | Prompt 11 timeline, Prompt 13 countdown |

### F-WR-008 — Inactivity, stalemate and abandonment

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-008` |
| 2 | Name | Inactivity, stalemate and abandonment |
| 3 | Purpose | End wars nobody is fighting, and bound dormancy |
| 4 | Expression | `stale = current_turn − last_resolved_offensive_turn`; `STALEMATE` at `stale ≥ 24`; expiry at `stale ≥ 48`. Separately, `suspended_turns` counts consecutive suspended turns: `ABANDONED` at `suspended_turns ≥ 48` |
| 5 | Inputs | Current turn; last resolved offensive turn; suspended-turn counter; campaign state |
| 6 | Output | Condition flag: none, `STALEMATE`, `EXPIRY`, or `ABANDONED` |
| 7 | Rounding | None |
| 8 | Clamping | Counters reset only on a resolved offensive operation or on return from suspension |
| 9 | Worked example | Last offensive at turn 100, current 124 → `STALEMATE`; at 148 → `EXPIRY` |
| 10 | Boundary example | Last offensive at turn 100, current 147 → still active; at 148 → expiry. A defensive operation alone does not reset `stale` |
| 11 | Failure behaviour | A missing last-offensive value is initialised to the campaign start turn, never guessed |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.2 |
| 14 | Mutation owner | B-10 campaign service |
| 15 | Visibility | Public stalemate flag; outcome public at P6 |
| 16 | Audit event | `WRA-05`, `WRA-13` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (24, 48, 48) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §6.3–§6.4, `WAR-016`, `WAR-021`–`WAR-024` |
| 20 | Downstream consumer | Prompt 11 world events, Prompt 13 status |

### F-WR-009 — Objective progress

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-009` |
| 2 | Name | Objective progress |
| 3 | Purpose | Convert a resolved operation into bounded, readable progress and counter-progress |
| 4 | Expression | On success: `p' = min(1000, p + value(op, objective))`. On a successful defensive counter: `p' = max(0, p − floor(value(op, objective) × 2500 / 10000))`. A failed offensive adds nothing |
| 5 | Inputs | Current progress int 0…1,000; operation type; objective type; success boolean; counter boolean |
| 6 | Output | New progress int 0…1,000; delta int |
| 7 | Rounding | Counter-progress floored once, after the multiplication |
| 8 | Clamping | 0…1,000 on the final value; counter cannot push below 0 |
| 9 | Worked example | ATTRITION 900 + successful ASSAULT 80 → 980. Counter: 980 − floor(80×2500/10000)=980−20=960 |
| 10 | Boundary example | 960 + 80 → 1,000 (clamped, 40 lost). Progress 10 with a 20 counter → 0 |
| 11 | Failure behaviour | An unknown `(operation, objective)` pair is `WRF-34`; no progress is written |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.8 |
| 14 | Mutation owner | B-10 progress service |
| 15 | Visibility | Both sides see both progress totals; the public sees the objective set and completion |
| 16 | Audit event | `WRA-06` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all 48 table values and 2500 bp) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §7.2, `WAR-036` |
| 20 | Downstream consumer | F-WR-010, Prompt 11 events, Prompt 13 meter |

### F-WR-010 — Victory determination

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-010` |
| 2 | Name | Victory determination |
| 3 | Purpose | Produce one public outcome from two progress states |
| 4 | Expression | 1. If exactly one side has `primary = 1000`, that side wins. 2. If the opponent's primary `< 250` → `DECISIVE_VICTORY`, else `LIMITED_VICTORY`. 3. If both reach 1000 in the same turn, compare `primary + floor(secondary / 2)`; higher wins `LIMITED_VICTORY`; exact tie → `DRAW`. 4. Otherwise no completion |
| 5 | Inputs | Primary and secondary progress for both sides, each 0…1,000; turn |
| 6 | Output | One outcome label or `NONE` |
| 7 | Rounding | `floor(secondary / 2)` |
| 8 | Clamping | Progress inputs are already 0…1,000 |
| 9 | Worked example | A primary 1,000 / secondary 600 → 1,300; B primary 1,000 / secondary 500 → 1,250; A wins `LIMITED_VICTORY` |
| 10 | Boundary example | A 1,000/0 vs B 1,000/0 → exact tie → `DRAW`. A 1,000 vs B primary 249 → `DECISIVE_VICTORY`; B 250 → `LIMITED_VICTORY` |
| 11 | Failure behaviour | Missing progress is `WRF-34`; no outcome is published |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P6, after P5.9 |
| 14 | Mutation owner | B-10 campaign service |
| 15 | Visibility | Public outcome and victory input; exact secondary totals public |
| 16 | Audit event | `WRA-13` |
| 17 | Provisional status | Structure structural; 250 threshold **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §7.3, `WAR-037`–`WAR-038` |
| 20 | Downstream consumer | Prompt 11 rankings, Prompt 13 outcome screen, Prompt 12 records |

### F-WR-011 — Progress-contribution cap

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-011` |
| 2 | Name | Progress-contribution cap |
| 3 | Purpose | Stop a single cheap operation from farming an objective |
| 4 | Expression | For each `(campaign, side, operation_type)`, `count' = min(8, count + 1)` on a successful resolution. Progress is added only if `count < 8`; otherwise the resolution applies losses but adds 0 progress |
| 5 | Inputs | `count` int 0…8; success boolean |
| 6 | Output | New count int 0…8; `adds_progress` boolean |
| 7 | Rounding | None |
| 8 | Clamping | Upper bound 8 |
| 9 | Worked example | count 7, successful RAID → count 8, progress added once. count 8, successful RAID → count 8, progress 0 |
| 10 | Boundary example | count 7 on the last turn of the campaign → still adds; count 8 → never adds again |
| 11 | Failure behaviour | A missing counter treats the resolution as non-progress-bearing and writes no progress; the loss still applies |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.8, before F-WR-009 |
| 14 | Mutation owner | B-10 progress service |
| 15 | Visibility | Both sides see the count per operation type; the cap is published |
| 16 | Audit event | `WRA-06` with `delta = 0` when capped |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (8) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §7.2, `WAR-035` |
| 20 | Downstream consumer | F-WR-009, Prompt 14 |

### F-WR-012 — Force cap

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-012` |
| 2 | Name | Force cap |
| 3 | Purpose | Bound total strength relative to national development without a military building |
| 4 | Expression | `force_cap = 1000 + 100 × city_count + 2 × total_infrastructure` |
| 5 | Inputs | `city_count` int ≥1; `total_infrastructure` int ≥0 |
| 6 | Output | `force_cap` int ≥1,000 |
| 7 | Rounding | None |
| 8 | Clamping | No upper clamp; negative inputs are invalid |
| 9 | Worked example | 3 cities, 150 infrastructure → 1,000 + 300 + 300 = **1,600** |
| 10 | Boundary example | 1 city, 0 infrastructure → **1,100**; a demolition that lowers infrastructure lowers the cap but never destroys existing strength (`WAR-057`) |
| 11 | Failure behaviour | Invalid city or infrastructure input is `WRF-34`; recruitment is refused |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P4 recruitment validation |
| 14 | Mutation owner | B-10 recruitment service reads B-05 city data |
| 15 | Visibility | Owner exact; no opponent visibility |
| 16 | Audit event | `WRA-03` on rejection with `WRF-24` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (1,000, 100, 2) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §10.3 |
| 20 | Downstream consumer | F-WR-014, Prompt 13 capacity display |

### F-WR-013 — Training capacity

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-013` |
| 2 | Name | Training capacity |
| 3 | Purpose | Bound recruitment per turn so strength grows with development, not with treasury alone |
| 4 | Expression | `training_capacity = min(20 + 5 × city_count, 80)` |
| 5 | Inputs | `city_count` int ≥1 |
| 6 | Output | `training_capacity` int 25…80 |
| 7 | Rounding | None |
| 8 | Clamping | Upper bound 80 |
| 9 | Worked example | 3 cities → 20 + 15 = **35** strength points per turn |
| 10 | Boundary example | 1 city → 25; 20 cities → 120 clamped to **80** |
| 11 | Failure behaviour | Zero or negative city count is invalid; recruitment refused with `WRF-34` |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P4 recruitment |
| 14 | Mutation owner | B-10 recruitment service |
| 15 | Visibility | Owner exact; public may see a coarse capacity band |
| 16 | Audit event | `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (20, 5, 80) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §10.3 |
| 20 | Downstream consumer | Prompt 13 recruitment screen, Prompt 14 |

### F-WR-014 — Single-type share

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-014` |
| 2 | Name | Single-type share |
| 3 | Purpose | Prevent a monotype force that defeats the counter design |
| 4 | Expression | After a proposed recruitment: `total = Σ strength_points`; for each type `t`, require `strength_t ≤ floor(total × 6000 / 10000)` |
| 5 | Inputs | Per-type strength points after the order; total int ≥0 |
| 6 | Output | Pass boolean; the offending type if any |
| 7 | Rounding | Share cap floored |
| 8 | Clamping | Applied after the order is added, not before |
| 9 | Worked example | Total 1,000, AIR 650 → cap 600 → rejected (`WRF-24`) |
| 10 | Boundary example | Total 1,000, AIR exactly 600 → pass. Total 0 → vacuous pass |
| 11 | Failure behaviour | Rejection writes `WRF-24`, reserves nothing |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P4 recruitment validation |
| 14 | Mutation owner | B-10 recruitment service |
| 15 | Visibility | Owner sees the share; no opponent visibility |
| 16 | Audit event | `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (60%) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §10.3, `WAR-058` |
| 20 | Downstream consumer | Prompt 13 force composition, Prompt 14 |

### F-WR-015 — Recruitment cost and arrival

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-015` |
| 2 | Name | Recruitment cost and arrival |
| 3 | Purpose | Price strength in crowns and resources, with a stable arrival rule |
| 4 | Expression | `crowns = crowns_per_sp(t) × added`; `resource_qty = ceil(resource_per_sp(t,r) × added)` per resource; arrival at the next P3 after the P4 order; INF 1 turn, ARM and AIR 2, NAV 3 |
| 5 | Inputs | Unit type; `added` int 1…training capacity; per-type rate table |
| 6 | Output | Crown cost int; per-resource cost int; arrival turn |
| 7 | Rounding | Ceiling per resource, per order; crowns exact |
| 8 | Clamping | `added` cannot exceed training capacity or force cap headroom; no partial order |
| 9 | Worked example | 100 INF → 100 × 20 = **2,000 crowns**, ceil(0.2×100)=**20 steel**, ceil(0.1×100)=**10 ammunition**, arrives at the next P3 |
| 10 | Boundary example | 1 INF → 20 crowns, 1 steel, 1 ammunition (ceiling applies); 0 → rejected |
| 11 | Failure behaviour | Insufficient crowns or resources is `WRF-12`; nothing is reserved |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P4 order; consumption at P4; arrival at the next P3 |
| 14 | Mutation owner | B-10 recruitment service; B-04 ledger writes `CAPEX` and reservations |
| 15 | Visibility | Owner exact; opponent sees only a strength band |
| 16 | Audit event | `WRA-03`; `WRA-14` for reservations; `CAPEX` ledger entry |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all rates and delays) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §10.3, `WAR-058`–`WAR-059` |
| 20 | Downstream consumer | Prompt 13 recruitment screen, Prompt 14 |

### F-WR-016 — Operation supply bundle

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-016` |
| 2 | Name | Operation supply bundle |
| 3 | Purpose | Attach a fixed, mapless inventory requirement to every operation |
| 4 | Expression | `bundle = table[op]`; on acceptance while OPEN `reserved_r = reserved_r + bundle_r` for each of gasoline, ammunition, steel, aluminium. `OP-09 RESUPPLY` additionally reserves 4 Food as a field ration (F-WR-036), **but only from eligible surplus above the protected civilian requirement** (`WAR-053l`): `eligible_op09_surplus = opening_food + projected_food_production − other_food_reservations − protected_civilian_food`, and the reservation requires `eligible_op09_surplus − OP-09 Food already held ≥ 4`. At P3.6 the actual values are re-tested; a reservation that would leave the protected requirement unmet is released in whole and the action fails `WRF-25`. No other operation reserves Food |
| 5 | Inputs | Operation type; unreserved inventory per resource; `opening_food`; `projected_food_production` (labelled forecast); `other_food_reservations`; `protected_civilian_food = ceil(population/1,000)` (F-EC-002); OP-09 Food already held this turn |
| 6 | Output | Four integer quantities plus the `OP-09` Food quantity; pass boolean |
| 7 | Rounding | None in the base table; surcharges use ceiling (F-WR-039); the protected requirement uses the F-EC-002 ceiling |
| 8 | Clamping | Inventory cannot go negative; reservation is atomic across all resources; a Food reservation never consumes protected civilian Food; no partial operation |
| 9 | Worked example | `OP-02 ASSAULT` → 10 gasoline, 10 ammunition, 2 steel, 0 aluminium, 0 Food. `OP-09` with opening Food 60, no production, other reservations 0, demand 50 → eligible surplus `60 − 50 = 10 ≥ 4`; 4 Food reserved |
| 10 | Boundary example | `OP-07 FORTIFY` → 0 gasoline, 2 ammunition, 4 steel, 0 aluminium; exact inventory equal to the bundle passes. `OP-09` with opening Food 50, demand 50 → eligible surplus 0 < 4 → `WRF-25`, nothing reserved |
| 11 | Failure behaviour | Any shortfall is `WRF-25`; nothing is reserved; full release on a later failure. An `OP-09` reservation that would leave protected civilian demand unmet is released at P3.6 and the action fails in whole; it is never partially funded or substituted with civilian Food |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Acceptance while OPEN; the P3.6 protected-civilian test; consumption at P5 |
| 14 | Mutation owner | B-10 supply service; B-04 ledger; the P3.6 test is owned by B-04's Food sub-phase and reads the B-10 reservation |
| 15 | Visibility | Owner exact; opponent never sees inventory; the digest shows the protected requirement and any release |
| 16 | Audit event | `WRA-03`, `WRA-14`; a release writes `RESERVATION_RELEASED` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all 36 quantities and the 4-Food field ration) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §12.2, §9.3, §13.2; `WAR-053f`, `WAR-053l`; B-04 ECN-082 |
| 20 | Downstream consumer | F-WR-019, F-WR-039, Prompt 13 cost display |

### F-WR-017 — Supply-denial surcharge

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-017` |
| 2 | Name | Supply-denial surcharge |
| 3 | Purpose | Supply the denial component of the single ordered stacking rule in F-WR-039 |
| 4 | Expression | `denial_bp = 2,500` while `SUPPLY_DENIED` is active, otherwise `0`. The component is **not applied on its own**; F-WR-039 sums it with `blockade_bp` (F-WR-018), caps the total at 5,000 bp and applies one ceiling per resource. `readiness −50` once when denial is applied; denial lasts one turn and does not stack |
| 5 | Inputs | `denied` boolean; current readiness |
| 6 | Output | `denial_bp` int 0 or 2,500; readiness delta |
| 7 | Rounding | None on the component; the combined ceiling is in F-WR-039 |
| 8 | Clamping | Readiness 0…1,000; denial is one turn, no stacking |
| 9 | Worked example | Denial alone: `denial_bp = 2,500` → RAID 5 / 5 becomes 7 / 7 via F-WR-039; readiness 700 → 650 |
| 10 | Boundary example | No denial: `denial_bp = 0`; denial on a zero bundle stays zero |
| 11 | Failure behaviour | If the surcharged bundle is unaffordable, the operation fails with `WRF-25`; no partial denial cost |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Next turn's acceptance after a successful interdiction; combined in F-WR-039 |
| 14 | Mutation owner | B-10 supply service |
| 15 | Visibility | Affected owner sees the denial state and the surcharge; attacker sees success |
| 16 | Audit event | `WRA-07` for the state; `WRA-03` for the cost |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (25%, 50) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §12.1, `WAR-071` |
| 20 | Downstream consumer | F-WR-039, Prompt 13 warning |

### F-WR-018 — Blockade modifier

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-018` |
| 2 | Name | Blockade modifier |
| 3 | Purpose | Supply the blockade component of the single ordered stacking rule in F-WR-039 |
| 4 | Expression | `blockade_bp = 2,500` while `BLOCKADED` is active, otherwise `0`. The component is **not applied on its own**; F-WR-039 sums it with `denial_bp` (F-WR-017) and caps the total. Separately, readiness recovery is `−25` per turn. No effect on tax, production, inventory or trade |
| 5 | Inputs | `blockaded` boolean; planned readiness recovery |
| 6 | Output | `blockade_bp` int 0 or 2,500; modified recovery |
| 7 | Rounding | None on the component; the combined ceiling is in F-WR-039 |
| 8 | Clamping | Recovery cannot go below 0; a blockade does not stack with itself |
| 9 | Worked example | Blockade alone: `blockade_bp = 2,500` → ASSAULT 10 / 10 becomes 13 / 13 via F-WR-039; paid recovery 50 → 25 |
| 10 | Boundary example | Blockade with no paid upkeep: recovery is already 0; the bundle surcharge still applies |
| 11 | Failure behaviour | An unaffordable surcharged bundle is `WRF-25`; the blockade state is not consumed |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Acceptance and P5 for the bundle; P3.7 for recovery; combined in F-WR-039 |
| 14 | Mutation owner | B-10 blockade service |
| 15 | Visibility | Blockade existence is public; exact cost is owner-only |
| 16 | Audit event | `WRA-07`, `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (25%, 25) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §12.1, `WAR-072` |
| 20 | Downstream consumer | F-WR-039, F-WR-005, Prompt 13 |

### F-WR-019 — Total action cost

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-019` |
| 2 | Name | Total action cost |
| 3 | Purpose | Present one complete price for a declaration or an operation before confirmation |
| 4 | Expression | Declaration: `2 OP + 500 crowns, no resources`. Operation: `OP[op]` plus the supply bundle after the single combined surcharge in F-WR-039, plus 4 Food for `OP-09` only when the `F-WR-016`/`WAR-053l` eligibility condition holds. Readiness gate is a prerequisite, not a cost; `RATION_SHORT` blocks offensive operations but is not a price |
| 5 | Inputs | Action type; operation type if any; denial and blockade states; city target flag; for `OP-09`, the protected civilian requirement and eligible Food surplus |
| 6 | Output | OP int; crowns int; four resource ints; Food int |
| 7 | Rounding | Inherited from F-WR-016/F-WR-039 |
| 8 | Clamping | No negative cost; no cost is ever refunded after a successful resolution; the displayed `OP-09` Food cost is 4 only when it can be reserved above the protected requirement, otherwise the action is unavailable |
| 9 | Worked example | `OP-05 MISSILE_STRIKE` under no suppression → 4 OP, 6 gasoline, 12 ammunition, 0 steel, 2 aluminium, 0 Food; under denial and blockade → 4 OP, 8 gasoline, 16 ammunition, 0 steel, 3 aluminium |
| 10 | Boundary example | Declaration → 2 OP and 500 crowns; a failure before P5 releases both. `OP-09` → 2 OP, bundle and 4 Food when eligible; with no eligible surplus the action is rejected `WRF-25`, never shown as partially affordable |
| 11 | Failure behaviour | Insufficient OP is `WRF-11`; insufficient crowns or resources is `WRF-12` or `WRF-25`; `RATION_SHORT` is `WRF-35`; an `OP-09` protected-Food failure is `WRF-25` |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Submission and confirmation while OPEN |
| 14 | Mutation owner | B-10 cost service; reservations by F-WR-002, F-WR-016 and F-WR-036 |
| 15 | Visibility | Actor sees the full cost before confirmation (`WAR-152`); opponent never sees it |
| 16 | Audit event | `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all costs) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §5.2, §8.1, §9.3, §12.1, §13.1 |
| 20 | Downstream consumer | Prompt 13 confirmation screen, Prompt 14 |

### F-WR-020 — Readiness factor in combat

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-020` |
| 2 | Name | Readiness factor in combat |
| 3 | Purpose | Convert readiness into a bounded combat multiplier without making it an economic multiplier |
| 4 | Expression | `readiness_factor_bp = 5000 + 5 × readiness` |
| 5 | Inputs | `readiness` int 0…1,000 |
| 6 | Output | `readiness_factor_bp` int 5,000…10,000 |
| 7 | Rounding | None |
| 8 | Clamping | Input and output bounds are structural |
| 9 | Worked example | readiness 700 → 5,000 + 3,500 = **8,500** |
| 10 | Boundary example | readiness 0 → 5,000 (50%); readiness 1,000 → 10,000 (100%, never above) |
| 11 | Failure behaviour | Out-of-range readiness is `WRF-34`; the battle does not resolve |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.6 per battle |
| 14 | Mutation owner | B-10 battle resolver |
| 15 | Visibility | Owner exact; opponent band only |
| 16 | Audit event | `WRA-04` records readiness and the factor |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (5,000 and 5) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.2, `WAR-079` |
| 20 | Downstream consumer | F-WR-021 |

### F-WR-021 — Combat power and base ratio

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-021` |
| 2 | Name | Combat power and base ratio |
| 3 | Purpose | Produce the deterministic strength comparison before fortune |
| 4 | Expression | `raw_force = Σ_t (strength_points_t × strength_per_point_t)`; `force_bp = Σ_t floor(strength_points_t × strength_per_point_t × factor_bp_t / 10000)`; `power = floor(force_bp × readiness_factor_bp / 10000)`; then `power = floor(power × counter_bp / 10000)`. `base_ratio_bp = floor(attack_power × 10000 / (attack_power + defence_power))`; if both are 0 → `5000`. For `OP-05`: `strike_power = 2000 + floor(air_attack_power × 2500 / 10000)` and no raw-force term |
| 5 | Inputs | Per-type strength points; per-type strength-per-point; per-type attack or defence factor bp; readiness factor bp; counter bp |
| 6 | Output | `attack_power` int ≥0; `defence_power` int ≥0; `base_ratio_bp` int 0…10,000 |
| 7 | Rounding | Floor after each stated multiplication |
| 8 | Clamping | Ratio 0…10,000; powers ≥0; zero-denominator branch defined |
| 9 | Worked example | Attack power 8,500, defence power 6,000 → floor(8,500×10,000/14,500) = **5,862** |
| 10 | Boundary example | Both powers 0 → **5,000**. Defence 0 with attack >0 → **10,000**. Attack 0 with defence >0 → **0** |
| 11 | Failure behaviour | A missing factor or an unknown unit type is `WRF-34`; the battle is not resolved |
| 12 | Determinism and seed | Deterministic; no seed in this step |
| 13 | Phase and trigger | P5.6 per battle, against the frozen baseline |
| 14 | Mutation owner | B-10 battle resolver |
| 15 | Visibility | Exact powers only in the private battle report (`WAR-088`); public sees tier and loss band |
| 16 | Audit event | `WRA-04` |
| 17 | Provisional status | Structure structural; all factors and the 2,000/25% strike constants **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.2, `WAR-076`–`WAR-081` |
| 20 | Downstream consumer | F-WR-023, F-WR-024, F-WR-032 |

### F-WR-022 — Order key, frozen baseline and seed

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-022` |
| 2 | Name | Order key, frozen baseline and seed |
| 3 | Purpose | Make simultaneous combat reproducible and independent of arrival order |
| 4 | Expression | Offensive order key: `(campaign_priority, attacker_nation_id, operation_priority, submitted_at, action_id)`, ascending lexicographic, where `operation_priority` is BLOCKADE 1, MISSILE_STRIKE 2, AIR_STRIKE 3, ASSAULT 4, RAID 5. All battles read the frozen P5 baseline; earlier losses are subtracted as `damage_carry`. Seed = frozen turn digest seed (`TR-046`) |
| 5 | Inputs | Campaign identifier; attacker identifier; operation priority; submission timestamp; action identifier; frozen baseline |
| 6 | Output | Total order; per-battle seed input |
| 7 | Rounding | None |
| 8 | Clamping | No tie remains: `action_id` is unique |
| 9 | Worked example | Two ASSAULTs: campaign 7, attacker 41, priority 4, submitted 10:00:03, action `a91` sorts before campaign 7, attacker 41, priority 4, 10:00:09, `a92` |
| 10 | Boundary example | Identical campaign, attacker and priority with the same `submitted_at` → `action_id` decides; no dependence on processing order |
| 11 | Failure behaviour | A missing component is `WRF-34`; the turn checkpoint is held rather than resolving in an arbitrary order |
| 12 | Determinism and seed | Fully deterministic; one seed per turn |
| 13 | Phase and trigger | P5.0–P5.7 |
| 14 | Mutation owner | B-02 scheduler supplies the seed; B-10 resolver orders |
| 15 | Visibility | Order key is not player-visible; the battle report identifies the battle and turn |
| 16 | Audit event | `WRA-04` records battle identifier, seed and roll |
| 17 | Provisional status | Structural; operation priorities **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** |
| 18 | Calibration owner | Prompt 14 for priorities only |
| 19 | Source rule | §15.1–§15.2, `WAR-089`–`WAR-093` |
| 20 | Downstream consumer | F-WR-023, F-WR-034, Prompt 14 replay tests |

### F-WR-023 — Fortune draw

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-023` |
| 2 | Name | Fortune draw |
| 3 | Purpose | Add bounded uncertainty without hidden probability |
| 4 | Expression | `fortune_bp = seeded_integer(seed, battle_id, −500, +500)`, inclusive at both ends |
| 5 | Inputs | Frozen turn seed; `battle_id`; fixed bounds −500…+500 |
| 6 | Output | Integer −500…+500 |
| 7 | Rounding | None; integer draw |
| 8 | Clamping | Bounds are structural |
| 9 | Worked example | seed and battle produce **+137** |
| 10 | Boundary example | A draw of −500 or +500 is legal; the distribution is uniform over the closed range |
| 11 | Failure behaviour | A missing seed or battle identifier is `WRF-34`; no draw is fabricated |
| 12 | Determinism and seed | Reproducible for the same `(seed, battle_id)`; seed and result published after resolution |
| 13 | Phase and trigger | P5.6, once per battle |
| 14 | Mutation owner | B-10 battle resolver |
| 15 | Visibility | Published in the battle report after resolution; never before |
| 16 | Audit event | `WRA-04` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (±500) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.3, `WAR-082` |
| 20 | Downstream consumer | F-WR-024, F-WR-032 |

### F-WR-024 — Effective ratio

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-024` |
| 2 | Name | Effective ratio |
| 3 | Purpose | Combine the deterministic ratio and the bounded fortune |
| 4 | Expression | `effective_ratio_bp = clamp(base_ratio_bp + fortune_bp, 0, 10000)` |
| 5 | Inputs | `base_ratio_bp` 0…10,000; `fortune_bp` −500…+500 |
| 6 | Output | `effective_ratio_bp` 0…10,000 |
| 7 | Rounding | None |
| 8 | Clamping | 0…10,000 after addition |
| 9 | Worked example | 5,862 + 137 = **5,999** → `CONTESTED` |
| 10 | Boundary example | 9,800 + 500 → **10,000**; 200 − 500 → **0** |
| 11 | Failure behaviour | Out-of-range inputs are `WRF-34` |
| 12 | Determinism and seed | Deterministic given F-WR-022 and F-WR-023 |
| 13 | Phase and trigger | P5.6 |
| 14 | Mutation owner | B-10 battle resolver |
| 15 | Visibility | Private exact value in the battle report; public tier only |
| 16 | Audit event | `WRA-04` |
| 17 | Provisional status | Structural |
| 18 | Calibration owner | None for the clamp |
| 19 | Source rule | §14.3, `WAR-083` |
| 20 | Downstream consumer | F-WR-025, F-WR-027 |

### F-WR-025 — Battle tier

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-025` |
| 2 | Name | Battle tier |
| 3 | Purpose | Convert the effective ratio into a readable outcome and a loss rate |
| 4 | Expression | `0–3,999 → ATTACKER_DEFEAT`; `4,000–4,999 → REPULSED`; `5,000–5,999 → CONTESTED`; `6,000–7,499 → ATTACKER_VICTORY`; `7,500–10,000 → DECISIVE_VICTORY`. Lower bound inclusive |
| 5 | Inputs | `effective_ratio_bp` 0…10,000 |
| 6 | Output | One tier label |
| 7 | Rounding | None |
| 8 | Clamping | Every integer 0…10,000 maps to exactly one tier |
| 9 | Worked example | 5,999 → `CONTESTED`; 6,000 → `ATTACKER_VICTORY` |
| 10 | Boundary example | 3,999 → `ATTACKER_DEFEAT`; 4,000 → `REPULSED`; 7,499 → `ATTACKER_VICTORY`; 7,500 → `DECISIVE_VICTORY` |
| 11 | Failure behaviour | An out-of-range value is `WRF-34` |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.6 |
| 14 | Mutation owner | B-10 battle resolver |
| 15 | Visibility | Tier public; exact ratio private |
| 16 | Audit event | `WRA-04` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all five thresholds) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.3, `WAR-083` |
| 20 | Downstream consumer | F-WR-027, F-WR-009, Prompt 13 |

### F-WR-026 — Counter modifier

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-026` |
| 2 | Name | Counter modifier |
| 3 | Purpose | Give every offensive operation a declared, bounded counter |
| 4 | Expression | `FORTIFY` against the first ground attack → `counter_defence_bp = 12500`; `INTERCEPT` against air or missile → `counter_defence_bp = 14000`, `counter_attack_bp = 8500`; `BREAK_BLOCKADE` → `counter_attack_bp = 7000`; otherwise `10000`. The strongest applicable counter applies; counters never stack |
| 5 | Inputs | Incoming operation type; active defensive operation; target state |
| 6 | Output | Attack bp and defence bp, each 7,000…14,000 |
| 7 | Rounding | None |
| 8 | Clamping | One counter per battle; a duplicate `FORTIFY` is `WRF-31` |
| 9 | Worked example | ASSAULT against a fortified defender → defence bp **12,500**; no attack bp change |
| 10 | Boundary example | Two applicable counters cannot both apply; the higher defence bp wins. No counter → 10,000/10,000 |
| 11 | Failure behaviour | A counter whose condition is not met is not applied; it is not an error |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.5 arms defensive operations; P5.6/P5.7 uses the bp |
| 14 | Mutation owner | B-10 battle resolver |
| 15 | Visibility | Defender knows its own counter; attacker sees the declared counter in the odds preview |
| 16 | Audit event | `WRA-10` for fortification, `WRA-09` for interception, `WRA-04` for the battle |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (12,500, 14,000, 8,500, 7,000) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.4 |
| 20 | Downstream consumer | F-WR-021, F-WR-032 |

### F-WR-027 — Strength-point losses

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-027` |
| 2 | Name | Strength-point losses |
| 3 | Purpose | Apply losses proportionally and reproducibly without destroying infrastructure |
| 4 | Expression | Per side and tier: `rate_bp` from the loss table; `loss_t = floor(engaged_t × rate_bp / 10000)` per unit type, then distribute any remaining points by the largest-remainder method, tie-broken by unit-type identifier order (`UNIT-AIR`, `UNIT-ARM`, `UNIT-INF`, `UNIT-NAV`) |
| 5 | Inputs | `engaged_t` per type int ≥0; tier; loss table |
| 6 | Output | Loss per type int ≥0; total int ≥0 |
| 7 | Rounding | Floor per type, then largest remainder |
| 8 | Clamping | Total loss cannot exceed engaged strength; readiness loss is separate (`−25`) |
| 9 | Worked example | Engaged 1,000 attacker at `ATTACKER_VICTORY` (700 bp) → floor(1,000×700/10,000) = **70** |
| 10 | Boundary example | Engaged 0 → 0 loss. `DECISIVE_VICTORY` defender at 1,500 bp on 1,000 → **150**; the 20% cap does not bind here |
| 11 | Failure behaviour | An unknown tier or unit type is `WRF-34`; no loss is applied |
| 12 | Determinism and seed | Deterministic; largest remainder is deterministic |
| 13 | Phase and trigger | P5.6 immediately after F-WR-025 |
| 14 | Mutation owner | B-10 loss service |
| 15 | Visibility | Exact losses in the private report; public loss band |
| 16 | Audit event | `WRA-04`, `WRA-08` for a strategic strike |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all 10 rates) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §16.2, `WAR-104` |
| 20 | Downstream consumer | F-WR-028, F-WR-005, Prompt 14 |

### F-WR-028 — Loss caps

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-028` |
| 2 | Name | Loss caps |
| 3 | Purpose | Prevent a single battle or a single campaign from annihilating a force |
| 4 | Expression | `battle_cap = floor(engaged × 2000 / 10000)`; `loss = min(loss, battle_cap)`. `campaign_cap = floor(campaign_start_strength × 6000 / 10000)`; cumulative losses for the side cannot exceed it; once reached, further battles apply 0 strength loss but still apply readiness loss |
| 5 | Inputs | Computed loss; engaged strength at battle start; campaign-start strength; cumulative campaign losses |
| 6 | Output | Capped loss per type; remaining campaign allowance |
| 7 | Rounding | Floor on both caps |
| 8 | Clamping | Per-battle cap first, then campaign cap; readiness is not capped |
| 9 | Worked example | Engaged 1,000, computed loss 250 → battle cap 200 → **200** applied |
| 10 | Boundary example | Campaign start 1,000, cumulative 600 → cap reached; the next battle applies **0** strength loss but still −25 readiness |
| 11 | Failure behaviour | A missing campaign-start value is initialised at campaign creation; it is never inferred later |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.6 after F-WR-027 |
| 14 | Mutation owner | B-10 loss service |
| 15 | Visibility | Exact loss private; cap state may be shown to the owner as "loss limit reached" |
| 16 | Audit event | `WRA-04` records the applied, not the uncapped, loss |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (20%, 60%) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §16.2, `WAR-105` |
| 20 | Downstream consumer | F-WR-005, Prompt 14 snowball tests |

### F-WR-029 — Reparation caps and atomic transfer

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-029` |
| 2 | Name | Reparation caps and atomic transfer |
| 3 | Purpose | Bound consensual transfers without creating debt or loot |
| 4 | Expression | Crowns: `pay ≤ min(floor(unreserved_crowns × 2500 / 10000), 100000)`. Resource: `qty_r ≤ floor(unreserved_r × 1000 / 10000)` per resource. At acceptance, reserve exactly the capped amount; at P5 transfer `TRANSFER_OUT`/`TRANSFER_IN` with matched legs; if either leg fails, the whole settlement fails with `WRF-33` |
| 5 | Inputs | Unreserved crowns int ≥0; unreserved stock per resource int ≥0; proposed amounts |
| 6 | Output | Accepted amount; reservation; two matched ledger legs |
| 7 | Rounding | Floor on both caps; proposed amounts are integers |
| 8 | Clamping | Per-settlement caps; one crown term and one resource term per settlement |
| 9 | Worked example | Unreserved 200,000 crowns, proposed 60,000 → cap min(50,000, 100,000) = 50,000; proposal of 60,000 is invalid |
| 10 | Boundary example | Unreserved 600,000, proposed 150,000 → cap **100,000**; resource stock 1,000 steel, proposed 100 → cap 100 exactly |
| 11 | Failure behaviour | A lost reservation or a blocked transfer → `WRF-33`, no partial transfer, campaign returns to `ACTIVE` |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Proposal validation; P5.3 |
| 14 | Mutation owner | B-10 settlement service; B-04 transfer ledger |
| 15 | Visibility | Terms public once accepted; pending terms parties only |
| 16 | Audit event | `WRA-12` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (25%, 100,000, 10%) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §21.1, `WAR-137`–`WAR-139` |
| 20 | Downstream consumer | Prompt 11 record, Prompt 13 settlement screen, Prompt 14 |

### F-WR-030 — Settlement proposal window

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-030` |
| 2 | Name | Settlement proposal window |
| 3 | Purpose | Bound negotiation and prevent silent acceptance |
| 4 | Expression | `expires = proposed_turn + 12`. A counter resets the window to `counter_turn + 12`. Acceptance requires both owners and executes at P5.3 of the accepting turn. Silence never accepts |
| 5 | Inputs | Proposal or counter turn; current turn; acceptance flags for both owners |
| 6 | Output | State: `PROPOSED`/`COUNTERED`, `EXPIRED`, `ACCEPTED`, `REJECTED`, `WITHDRAWN` |
| 7 | Rounding | None |
| 8 | Clamping | One live settlement per campaign; terms immutable after submission |
| 9 | Worked example | Proposed turn 100 → expires 112; accepted turn 108 → executes at P5.3 of turn 108 |
| 10 | Boundary example | Proposed turn 100, current 112 → `EXPIRED` before P5.3; a counter on turn 111 resets expiry to 123 |
| 11 | Failure behaviour | An acceptance missing one owner is not accepted; no partial execution |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Submission; P5.2 for expiry; P5.3 for execution |
| 14 | Mutation owner | B-10 settlement service |
| 15 | Visibility | Pending terms parties only; accepted terms public |
| 16 | Audit event | `WRA-12` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (12) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §19.1, §20.1, `WAR-122`, `WAR-127` |
| 20 | Downstream consumer | Prompt 13 negotiation UI, Prompt 11 record |

### F-WR-031 — Exclusion and disarmament

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-031` |
| 2 | Name | Exclusion and disarmament |
| 3 | Purpose | Make the two durable settlement terms deterministic and debt-free |
| 4 | Expression | Exclusion: `until_turn = completion_turn + 84`; a declaration fails with `WRF-32` while `current_turn < until_turn`. Disarmament: remove points in order INF, ARM, AIR, NAV until `removed = min(stated, available)`; any shortfall is cancelled and the term is recorded as partially satisfied |
| 5 | Inputs | Completion turn; stated exclusion or disarmament amount; payer strength by type |
| 6 | Output | `until_turn`; removed points by type; partial-satisfaction flag |
| 7 | Rounding | None |
| 8 | Clamping | Removal cannot exceed available strength; no debt for the shortfall |
| 9 | Worked example | Completion turn 200 → exclusion until 284. Stated disarmament 500, payer has 300 → 300 removed, 200 cancelled, settlement completes |
| 10 | Boundary example | Stated 0 → term is vacuously satisfied; exclusion of 84 turns applies from the completion turn, not the proposal turn |
| 11 | Failure behaviour | A malformed term is invalid at proposal; it never reaches P5 |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | P5.3 on settlement completion; exclusion checked at submission, P2 and P5 |
| 14 | Mutation owner | B-10 settlement service; B-10 force service for removal |
| 15 | Visibility | Exclusion pair and duration public; disarmament amount public once accepted |
| 16 | Audit event | `WRA-12`, `WRA-13` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (84) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §20.4, `WAR-135`–`WAR-136` |
| 20 | Downstream consumer | F-WR-004, Prompt 13, Prompt 14 |

### F-WR-032 — Odds band

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-032` |
| 2 | Name | Odds band |
| 3 | Purpose | Disclose a truthful, bounded outcome range before commitment without revealing exact enemy power |
| 4 | Expression | With `base_ratio_bp` and fortune bounds ±500: `low = clamp(base − 500, 0, 10000)`, `high = clamp(base + 500, 0, 10000)`. Map `low` and `high` through F-WR-025 and present the inclusive tier range, plus the exact own attack power and exact own costs |
| 5 | Inputs | `base_ratio_bp`; fortune bound; counter set; F-WR-025 |
| 6 | Output | Tier range label (for example `CONTESTED–ATTACKER_VICTORY`) |
| 7 | Rounding | None |
| 8 | Clamping | 0…10,000 before tier mapping |
| 9 | Worked example | base 5,862 → low 5,362 (`CONTESTED`), high 6,362 (`ATTACKER_VICTORY`) → band **CONTESTED–ATTACKER_VICTORY** |
| 10 | Boundary example | base 9,800 → low 9,300, high 10,000 → **DECISIVE_VICTORY only**; base 200 → **ATTACKER_DEFEAT only** |
| 11 | Failure behaviour | If enemy power is unavailable to the validator, no odds band is shown and the operation cannot be confirmed |
| 12 | Determinism and seed | Deterministic on the disclosed inputs; the actual fortune is drawn only at P5 |
| 13 | Phase and trigger | Confirmation, before submission |
| 14 | Mutation owner | B-10 disclosure service |
| 15 | Visibility | Attacker only; never shows exact enemy strength, readiness or inventory |
| 16 | Audit event | No event for a preview; the confirmed operation writes `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (±500, tier thresholds) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.5, `WAR-085` |
| 20 | Downstream consumer | Prompt 13 confirmation screen, Prompt 14 |

### F-WR-033 — Threat band

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-033` |
| 2 | Name | Threat band |
| 3 | Purpose | Give the defender a readable warning without leaking the attacker's exact state |
| 4 | Expression | `ratio = opponent_force / viewer_force`; `LOW < 0.75`; `MODERATE 0.75 ≤ ratio < 1.25`; `HIGH 1.25 ≤ ratio < 2.00`; `SEVERE ≥ 2.00`. If `viewer_force = 0` and `opponent_force > 0` → `SEVERE`; if both 0 → `MODERATE` |
| 5 | Inputs | Viewer force int ≥0; opponent force int ≥0 |
| 6 | Output | One of four labels |
| 7 | Rounding | Comparison in exact integer cross-multiplication; no floating point |
| 8 | Clamping | Zero-denominator branches defined |
| 9 | Worked example | opponent 1,500, viewer 1,000 → ratio 1.50 → **HIGH** |
| 10 | Boundary example | ratio exactly 0.75 → MODERATE; exactly 1.25 → HIGH; exactly 2.00 → SEVERE |
| 11 | Failure behaviour | A missing force value produces no band; the defender sees "unavailable", not a guess |
| 12 | Determinism and seed | Deterministic |
| 13 | Phase and trigger | Campaign active; refreshed at P6 |
| 14 | Mutation owner | B-10 disclosure service |
| 15 | Visibility | Defender only; the attacker never sees it |
| 16 | Audit event | None; the P6 battle report carries the resolved data |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all four boundaries) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §14.5, `WAR-086` |
| 20 | Downstream consumer | Prompt 13 campaign screen |

### F-WR-034 — P5 validity, idempotency and recovery

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-034` |
| 2 | Name | P5 validity, idempotency and recovery |
| 3 | Purpose | Guarantee one outcome per action per turn, even after a crash or replay |
| 4 | Expression | `execute = valid_at_p5 ∧ ¬applied[turn_id, operation_id]`. On success write one `APPLIED` marker and one set of ledger items in one transaction. On restart, resume at the last checkpoint and skip every operation with a committed `APPLIED` marker. A retry with the same idempotency key returns the original receipt |
| 5 | Inputs | Execution-time validity; `(turn_id, operation_id)`; `(turn_id, battle_id)`; checkpoint position; idempotency key |
| 6 | Output | One applied outcome or one failure; no partial state |
| 7 | Rounding | None |
| 8 | Clamping | At most one application per key; at most one consumption per reservation |
| 9 | Worked example | A crash after battle 3 of 5 resumes at checkpoint 3; battles 1–3 are not re-applied, battles 4–5 resolve against the same frozen baseline |
| 10 | Boundary example | A duplicate submission after a successful resolution returns the original receipt and writes no second loss |
| 11 | Failure behaviour | An invariant violation is `WRF-34`; the turn checkpoint is held, nothing is published, and the operator path is invoked |
| 12 | Determinism and seed | Deterministic; the same seed and baseline reproduce the same outcome |
| 13 | Phase and trigger | P5.0 manifest, every P5 sub-phase, P7 reconciliation |
| 14 | Mutation owner | B-10 resolver inside the B-02 checkpoint transaction |
| 15 | Visibility | Nothing partial is visible before `WRA-04`; the final report is visible to both parties |
| 16 | Audit event | `WRA-03`, `WRA-04`, `WRA-14` |
| 17 | Provisional status | Structural |
| 18 | Calibration owner | None |
| 19 | Source rule | §15.4, `WAR-097`–`WAR-100` |
| 20 | Downstream consumer | Prompt 10C recovery cases, Stage 3 implementation |

### F-WR-035 — Calibration envelope

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-035` |
| 2 | Name | Calibration envelope |
| 3 | Purpose | Give Prompt 14 one complete manifest of every provisional B-10 constant and its owner |
| 4 | Expression | A manifest, not a calculation: for each constant, `(formula_id, constant_name, current_value, range_to_test, unit, affected_rule)`. The manifest is the union of fields 17 in F-WR-001…F-WR-038 plus the rulebook tables marked provisional |
| 5 | Inputs | F-WR-001…F-WR-038 field 17 entries; rulebook §27.3 |
| 6 | Output | A versioned parameter list |
| 7 | Rounding | None |
| 8 | Clamping | Every constant has an explicit range; a value outside the range requires an architecture review, not a calibration run |
| 9 | Worked example | `(F-WR-005, start_readiness, 700, 500–900, points, WAR-047)`; `(F-WR-001, op_cap, 10, 6–20, OP, WAR-039)` |
| 10 | Boundary example | A constant with no range is a manifest defect and blocks the calibration run |
| 11 | Failure behaviour | A missing constant stops the run; Prompt 14 may not silently choose a default |
| 12 | Determinism and seed | Manifest is deterministic; simulation seeds belong to Prompt 14 |
| 13 | Phase and trigger | Prompt 14 calibration and every later rebalance |
| 14 | Mutation owner | Prompt 14 owns values; B-10 owns the formula shape |
| 15 | Visibility | Internal design and calibration only |
| 16 | Audit event | None; changes are versioned in the register and the decision log |
| 17 | Provisional status | Structural container; contents provisional |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §27.3; `WAR-169`, `WAR-177`–`WAR-180` |
| 20 | Downstream consumer | Prompt 14, Prompt 15, Stage 3 tuning |

### F-WR-036 — Military food ration

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-036` |
| 2 | Name | Military food ration |
| 3 | Purpose | Convert a garrison's strength points into a recurring Food obligation using soldier-equivalents, distinct from civilian demand and from `OP-09` field rations |
| 4 | Expression | Let `force_snapshot` be the canonical P3.7 snapshot (`WAR-053m`), stored at the opening of P3.7 after any recruitment whose completion turn is this turn has been added. `ration_equivalents = Σ_t (force_snapshot.strength_t × e_t)` where `e_t` is the soldier-equivalent factor of unit type `t`. `military_food_demand = ceil(ration_equivalents / 1000)`. If payable from the Food left unreserved after P3.6 civilian consumption and after the `WAR-053l` conditional test: debit it, write `OBLIGATION_PAID` with component `MILITARY_RATION`, and leave readiness unchanged. Otherwise cancel the whole obligation, write `OBLIGATION_CANCELLED` with component `MILITARY_RATION`, and set `readiness = max(0, readiness − 100)` plus `RATION_SHORT`. `RATION_SHORT` blocks offensive operations at pre-P5 (`WRF-35`) and clears at the next paid P3.7 |
| 5 | Inputs | `force_snapshot.strength_t` per unit type, int ≥ 0, read from the single P3.7 snapshot (`WAR-053m`); `e_t` from the table (INF 10, ARM 4, AIR 2, NAV 20); unreserved Food int ≥ 0 after P3.6; current readiness int 0…1,000 |
| 6 | Output | `ration_equivalents` int ≥ 0; `military_food_demand` int ≥ 0; one obligation state; new readiness |
| 7 | Rounding | One ceiling only, after the whole sum; no per-type rounding |
| 8 | Clamping | Readiness 0…1,000; no negative Food; no partial payment; demand is never reduced by `OP-09` reservations; the snapshot is never recomputed from a second force baseline |
| 9 | Worked example | Snapshot 200 `UNIT-INF` + 300 `UNIT-ARM` → 2,000 + 1,200 = 3,200 equivalents → `ceil(3,200/1,000) = 4` Food. 300 `UNIT-ARM` alone → 1,200 equivalents → `ceil(1.2) = 2` Food |
| 10 | Boundary example | Zero strength → 0 equivalents → 0 Food; the obligation is vacuously paid and readiness does not fall. 1,001 equivalents → 2 Food. A 1-equivalent garrison → 1 Food. Current-turn recruitment excluded from the snapshot is not counted; prior-turn completed recruitment is |
| 11 | Failure behaviour | A shortfall cancels the whole obligation: no partial debit, no debt, `readiness −100`, `RATION_SHORT`. Food is never taken from civilian demand or from a protected `OP-09` reservation, and a unit is never deleted for lack of rations (`WAR-053f`, `WAR-053l`) |
| 12 | Determinism and seed | Deterministic; no seed |
| 13 | Phase and trigger | P3.7, inside `ECN-105` rank 6, sub-order (a), after P3.6 civilian Food; the snapshot is stored once at the opening of P3.7 (`WAR-053m`) |
| 14 | Mutation owner | B-04 obligation engine reads the stored B-10 force snapshot and writes the Food debit; B-10 writes the snapshot, the readiness delta and the `RATION_SHORT` flag |
| 15 | Visibility | Owner sees demand, payment and shortfall; opponent never sees exact stock |
| 16 | Audit event | `OBLIGATION_PAID` / `OBLIGATION_CANCELLED` with component `MILITARY_RATION`; `WRA-14` for the inventory leg |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (all four soldier-equivalent factors, the 1,000 feed rate and the 100 readiness penalty) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §9.3, `WAR-053a`–`WAR-053m` |
| 20 | Downstream consumer | P5 readiness gate, P3.7 obligation engine, Prompt 13 ration warning |

### F-WR-037 — City infrastructure damage

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-037` |
| 2 | Name | City infrastructure damage |
| 3 | Purpose | Bound the infrastructure levels `OP-05 MISSILE_STRIKE` removes from one B-05 city, and derive the new capacity and housing |
| 4 | Expression | Let `I = I_combat` from `WAR-109m` — the post-P4.1 level the P5 battle reads. `removed_raw = ceil(I × 500 / 10,000)`; `removed = min(removed_raw, 20, campaign_headroom, I − 10)`; `I_after = I − removed`; `capacity_after = 10 + floor(I_after / 10)`; `housing_after = 45,000 + 100 × I_after + 25,000 × civic_centres`. `campaign_headroom = floor(I_campaign_start × 3000 / 10,000) − already_removed_this_campaign`. Damage is applied only on `ATTACKER_VICTORY` or `DECISIVE_VICTORY` |
| 5 | Inputs | `I_combat` int 10…500 (never a stale opening value); `I_campaign_start` int 10…500; `already_removed_this_campaign` int ≥ 0; `civic_centres` int 0…3; victory tier |
| 6 | Output | `removed` int 0…20; `I_after` int 10…500; `capacity_after` int 11…60; `housing_after` int ≥ 0 |
| 7 | Rounding | Ceiling on `removed_raw`; floor in the capacity and campaign-headroom terms |
| 8 | Clamping | `removed` bounded by 0, by 20, by the remaining campaign headroom and by `I − 10`; `I_after` never below 10; no damage on a draw or defender victory |
| 9 | Worked example | `I = 50`, campaign start 50, no prior damage → `removed_raw = ceil(2.5) = 3`, headroom 15 → `removed = 3`, `I_after = 47`, capacity 14, housing 49,700 |
| 10 | Boundary example | `I = 10` → `removed_raw = 1` but `I − 10 = 0` → `removed = 0`, no mutation. `I = 500` → `removed_raw = 25` capped to 20. A third strike after the 30% headroom is exhausted → `removed = 0`; the battle still resolves |
| 11 | Failure behaviour | An invalid city id, a city not owned by the target nation, or an `OP-05` without an active campaign is `WRF-36`; nothing moves. A zero result at the floor or the campaign cap is **not** a rejection |
| 12 | Determinism and seed | Deterministic; no seed |
| 13 | Phase and trigger | P5, after the battle tier is known and before P6 disclosure; reads `I_combat`, writes `I_post_P5` |
| 14 | Mutation owner | B-10 damage service writes `removed`; B-05 writes `infrastructure`, `capacity` and `housing` from the new level |
| 15 | Visibility | City infrastructure and damage are public at P6; the battle report names the city |
| 16 | Audit event | `WRA-08`; B-05 `INFRASTRUCTURE_DAMAGED` with `damage_event_id = (turn_id, strike_action_id, city_id)`, applied once |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (500 bp base, 20-level cap, 30% campaign cap) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §16.4, `WAR-109a`–`WAR-109m` |
| 20 | Downstream consumer | F-WR-038, B-05 capacity/housing, Prompt 11 rankings, Prompt 13 battle report |

### F-WR-038 — Fixed-asset impairment and repair

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-038` |
| 2 | Name | Infrastructure asset impairment and repair |
| 3 | Purpose | Keep a city's **infrastructure** carrying value consistent with damage and price a bounded, costed repair, without touching facility book value or deleting facilities |
| 4 | Expression | **Asset basis.** `infrastructure_gross_capital(city)` = Σ capitalised crown cost of the city's completed `UPGRADE_INFRASTRUCTURE` lots. The initial city capital (50) and the new-city capital (10) are a **zero-cost opening lot**, so they add 0 to gross capital. `infrastructure_accumulated_impairment(city)` starts at 0. `infrastructure_carrying_value(city) = gross − accumulated`. **Impairment at P5.** `carrying_before = infrastructure_carrying_value(city)`; `impaired = min(carrying_before, floor(carrying_before × removed / I_combat))`; `accumulated += impaired`; `carrying_after = carrying_before − impaired`; `fixed_asset_book_value −= impaired` (B-04 ECN-108). **Repair at P4.1.** `base_repair_cost = Σ_{j=I}^{I+n−1} (8 + floor(j / 10))`; `repair_cost = ceil(base_repair_cost × 9,000 / 10,000)` only when Civil Survey is owned, otherwise `base_repair_cost`; `1 ≤ n ≤ min(10, 500 − I, unrepaired_levels)`. Capitalise the repair as a new lot: `gross += repair_cost`; `accumulated` unchanged; `carrying += repair_cost`; `fixed_asset_book_value += repair_cost`. No impairment reversal, no materials, no second discount |
| 5 | Inputs | `infrastructure_gross_capital` int ≥ 0; `infrastructure_accumulated_impairment` int ≥ 0; `I_combat` int 10…500 (`WAR-109m`); `removed` int 0…20; `n` int 1…10; `unrepaired_levels` int ≥ 0; Civil Survey owned boolean |
| 6 | Output | `impaired` int ≥ 0; `infrastructure_carrying_value` int ≥ 0; `repair_cost` int ≥ 0; `I_after_repair` int 10…500 |
| 7 | Rounding | Floor on impairment; exact integer lot sum and **one** ceiling on the discounted repair cost; no floating point |
| 8 | Clamping | `impaired ≤ carrying_before`; `accumulated ≤ gross` after every event; repair cannot exceed 10 levels/turn, the unrepaired damage, or level 500; facilities, their book value and their existence are never touched; repeated damage reads the post-impairment carrying value |
| 9 | Worked example | Opening `I = 50` at zero-cost basis: gross 0, accumulated 0, carrying 0. Upgrade 50→60 (10 lots): cost `Σ_{j=50}^{59}(8+floor(j/10)) = 10 × 13 = 130`; gross 130, accumulated 0, carrying 130; a 5,000-crown facility keeps its own value, so national fixed assets are 5,130. A strike removes `ceil(60 × 500 / 10,000) = 3`; `impaired = min(130, floor(130 × 3 / 60)) = 6`; carrying 124, accumulated 6, `I = 57`, national fixed assets 5,124, facility still 5,000. Repair 3 at `I = 57`: `3 × (8 + floor(57/10)) = 3 × 13 = 39`; gross 169, accumulated 6, carrying 163, national 5,163. A second strike of 3 levels then impairs `floor(163 × 3 / 60) = 8`; accumulated 14, carrying 155 |
| 10 | Boundary example | `removed = 0` → `impaired = 0`, no repair offered, carrying unchanged. City still at its initial level 50 with no upgrade lot → carrying 0, `impaired = 0` however much is removed, because there is no capitalised infrastructure cost to impair and the initial level is not a book asset. `removed = 20` at `I = 500` → `impaired = min(carrying, floor(carrying × 20 / 500))`. Repair 10 levels at `I = 400` → `10 × 48 = 480` crowns before the Civil Survey discount. Repair when `unrepaired_levels = 0` is `WRF-37` |
| 11 | Failure behaviour | A repair above the unrepaired damage, above 10 levels, above the 500 cap, or with no active `INFRASTRUCTURE_DAMAGED` record is `WRF-37`; nothing is charged and the capex reservation is released once. An unaffordable repair is `WRF-12`; no partial repair. A replayed damage event with the same `damage_event_id` applies once and never impairs twice |
| 12 | Determinism and seed | Deterministic; no seed; the order of two strikes in one turn is fixed by `WAR-109m` and shares the campaign cap |
| 13 | Phase and trigger | Impairment at P5 immediately after `F-WR-037` sets `removed`, reading `I_combat`; repair ordered in P4 and capitalised at P4.1; capacity and housing use the `WAR-109m` boundaries |
| 14 | Mutation owner | B-05 writes gross, accumulated, carrying and `fixed_asset_book_value`; B-10 writes the damage record and `removed` |
| 15 | Visibility | Carrying value and repair cost are owner-only; damage and the repaired level are public at P6 |
| 16 | Audit event | `INFRASTRUCTURE_DAMAGED` (carrying before/after, `impaired`, `damage_event_id`); `INFRASTRUCTURE_REPAIRED` (new lot, cost) + `CAPEX` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (10-level repair rate; repair cost inherits the URB-043 curve; the 9,000 bp Civil Survey discount is URB-044) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §16.4, `WAR-109f`–`WAR-109m`; B-05 `URB-043`, `URB-044`, `URB-118`, `URB-118a`, `URB-118b`, `URB-157`; B-04 `ECN-108` |
| 20 | Downstream consumer | B-04 national wealth reconciliation, B-05 capex, Prompt 13 repair screen and battle report |

### F-WR-039 — Combined supply modifier

| # | Field | Value |
|---|---|---|
| 1 | Identifier | `F-WR-039` |
| 2 | Name | Combined supply modifier |
| 3 | Purpose | Apply supply denial and blockade as one ordered, bounded surcharge so the two states are never counted twice |
| 4 | Expression | `denial_bp = 2,500` if `SUPPLY_DENIED` else 0; `blockade_bp = 2,500` if `BLOCKADED` else 0; `surcharge_bp = min(5,000, denial_bp + blockade_bp)`; `bundle'_r = ceil(bundle_r × (10,000 + surcharge_bp) / 10,000)` per resource. Applied once, to the base bundle, never multiplicatively. Readiness effects are separate: denial `−50` once, blockade recovery `−25` per turn |
| 5 | Inputs | Base `bundle_r` per resource; `denied` boolean; `blockaded` boolean |
| 6 | Output | `surcharge_bp` int 0…5,000; modified bundle per resource |
| 7 | Rounding | One ceiling per resource after the single addition |
| 8 | Clamping | Total surcharge capped at 5,000 bp; a state that is inactive contributes 0; the same state never stacks with itself |
| 9 | Worked example | RAID 5/5, both active → `surcharge_bp = 5,000`, `bundle' = ceil(5 × 15,000/10,000) = 8` for both resources |
| 10 | Boundary example | Neither active → 5/5. Denial only or blockade only → 7/7. Denial expired, blockade active → 7/7. Blockade applied after denial in the same turn → 8/8 |
| 11 | Failure behaviour | An unaffordable modified bundle is `WRF-25`; nothing is reserved; the states are not consumed |
| 12 | Determinism and seed | Deterministic; order of state evaluation does not change the sum |
| 13 | Phase and trigger | Acceptance while OPEN; re-read and applied at P5 |
| 14 | Mutation owner | B-10 supply service |
| 15 | Visibility | Owner sees the surcharge and the contributing states; opponent sees the states but not the exact cost |
| 16 | Audit event | `WRA-07`, `WRA-03` |
| 17 | Provisional status | **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** (25% per state, 50% cap) |
| 18 | Calibration owner | Prompt 14 |
| 19 | Source rule | §12.1, `WAR-071`–`WAR-072` |
| 20 | Downstream consumer | F-WR-016, F-WR-019, Prompt 13 |

---

## 6. Cross-register consistency

`WF-011` **Coverage.** Every calculation named in rulebook §5–§21 maps to exactly one entry above. The mapping is: declaration and slots → F-WR-004/F-WR-006/F-WR-019; campaign duration → F-WR-007/F-WR-008; objectives → F-WR-009/F-WR-010/F-WR-011; OP → F-WR-001/F-WR-002; readiness → F-WR-003/F-WR-005/F-WR-020; maintenance → F-WR-036; units → F-WR-012–F-WR-015; supply → F-WR-016/F-WR-017/F-WR-018/F-WR-039; battle → F-WR-021–F-WR-026; losses → F-WR-027/F-WR-028; city damage, impairment and repair → F-WR-037/F-WR-038; settlement → F-WR-029–F-WR-031; disclosure → F-WR-032/F-WR-033; execution → F-WR-034; calibration → F-WR-035.

`WF-012` **No duplicate definition.** The rulebook states the rule and the register states the arithmetic. Where the rulebook shows a formula (for example `readiness_factor_bp = 5000 + 5 × readiness`), the register repeats it only to make the entry self-contained; the register governs a divergence.

`WF-013` **Unspecified coefficients.** `WAR-050` names the upkeep components but not their coefficients. F-WR-003 supplies the coefficients and is authoritative for them. No other rule relies on an unstated number.

`WF-014` **Provisional inventory.** F-WR-035 is the complete list. A value is not provisional merely because it appears in a table; it is provisional when its F-WR-035 manifest row exists. Conversely, every rulebook value tagged **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** must have a manifest row.

`WF-015` **No new event or resource.** Every audit event used above is from `WRA-01`–`WRA-14`. Every resource is from the B-04 eleven-resource roster. Every ledger type is a registered B-04 type. A formula that would need a new one is rejected.

---

## 7. Validation and completion

`WF-016` The register was checked for: 39 sequential identifiers with no gap or duplicate; 20 populated fields in every entry; every `WAR-` anchor resolving to a rulebook rule; every rulebook calculation having a register entry; no floating-point step; no undefined division; and no new resource, currency or event type. The exact commands and results are recorded in the Stage 2 progress log and the completion report.

`WF-017` The register is **complete at the documentation level**. No formula has been implemented, executed, simulated or calibrated. No worked example is a gameplay result; each is arithmetic checked by hand. The calibration owner for every constant is Prompt 14.
