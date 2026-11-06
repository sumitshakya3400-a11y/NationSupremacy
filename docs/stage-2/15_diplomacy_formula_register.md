# B-08 diplomacy — formula and limit register

**Version:** 1.2 · **Created:** 2026-10-30 · **Stage 2, Prompt 08B** · **Corrected 2026-10-30 (Prompt 08B-C):** F-DP-002 now keys proposals as ordered and agreements as unordered, F-DP-004/006/008/009 apply the freeze rule of DIP-105 explicitly, and F-DP-010's boundary example is recalculated. **Corrected 2026-10-30 (Prompt 08B-D):** F-DP-005 and F-DP-007 now apply the actor freeze over the same explicit interval as F-DP-004/006/008/009, the three cooldowns' §3 limits rows and descriptions state their extension, and F-DP-002's heading matches its per-direction rule. No value changed.
**Status:** **Design only. Every value is Provisional and belongs to Prompt 14.** No formula here is balanced, simulated, implemented or tested. The register defines the arithmetic of [`15_diplomacy.md`](15_diplomacy.md); the rulebook remains authoritative for the rule.
**Scope:** the twelve calculations B-08 actually needs. There is no reputation score, trust curve, prestige value or relation modifier, because B-08 adopts none (DIP-084, DIP-137).
**Units:** turns are integer boundaries; crowns are integer units; counts are non-negative integers; booleans are `true`/`false`. All arithmetic is integer. No rounding is required except where a rule says so; no formula here uses a fraction, a percentage or a random term.

---

## 1. How to read a formula

Each entry states: purpose; definition; variables and units; range and bounds; rounding; timing; edge cases; source; dependencies; a worked example; and the validation expected in Prompt 08C/14.

**A value marked "Provisional" is a structural default, not a balance claim.** Prompt 14 may change it by editing the register and the rule's value together. A change that alters the *shape* of a formula is a design change and needs a `D-` entry.

**Freeze.** Two functions, because DIP-105 gives two scopes and a timer belongs to exactly one:

- `frozen_turns(n, a, b)` — boundaries nation `n` spent in `TRANSITION` or `CRISIS` in the interval `(a, b]`. Non-negative integer. Used by **actor-scoped** timers: posture cooldown, notice cooldown, breach cooldown, embargo re-imposition.
- `frozen_pair(a, b)` — boundaries in `(a, b]` on which **either** party to the pair was frozen, **each boundary counted once**. When both are frozen the value is +1 for that boundary, not +2. Used by **pair-scoped** timers: proposal expiry, agreement expiry, notice-window end.

No other timer uses either function. The embargo's 24-turn term, the 12-turn minimum before a notice is usable, the renewal's “strictly before expiry” test and dormancy are **not** freeze-aware (DIP-105). Freeze is not a penalty; it restores time the rules took away.

**Actor-scoped timers are counted in unfrozen boundaries.** `t ≥ start + N + frozen_turns(n, start, t)` is arithmetically the same statement as “`N` boundaries in `(start, t]` on which `n` was not frozen have elapsed”, so every actor-scoped cooldown is a count of **unfrozen** boundaries (DIP-105(b)). Each such formula therefore names its start event and writes the interval `(start, t]` in full; a bare `frozen_turns(actor)` is not a definition and must never appear. The interval always begins at the event that starts the base duration — the posture change, the notice, the breach, or the embargo's end (or early lift).

---

## 2. The formulas

### F-DP-001 — Open outgoing proposal count

| Field | Definition |
|---|---|
| **Purpose** | Enforce the declared proposal cap (DIP-045/DIP-106). |
| **Definition** | `open_out(n) = count(proposals p where p.from = n and p.status = PENDING)` |
| **Variables** | `n` = nation ID; `p` = proposal. Unit: proposals (integer). |
| **Range** | `0 ≤ open_out(n) ≤ 3`. |
| **Bounds** | A new proposal is permitted only if `open_out(n) < 3`. At 3, `DPF-06`. |
| **Rounding** | None. |
| **Timing** | Checked at submission and again at P2. A withdrawal, rejection or expiry releases a slot immediately in the acting boundary's state, but the next submission is validated at the next boundary. |
| **Edge cases** | An accepted proposal no longer counts as open. A proposal that expires at the same boundary as a new submission is counted as open at P2 if the expiry is ordered after the submission validation; DIP-103's order makes expiry run first, so the slot is free. |
| **Source** | DIP-045, DIP-106; D-024. |
| **Dependencies** | F-DP-002, F-DP-004. |
| **Example** | At turn 1000, A has proposals P1 (to B), P2 (to C) and P3 (to D), all `PENDING`. A fourth submission to E fails `DPF-06`. If P2 is rejected at 1004, A may submit a new proposal at 1005. |
| **Validation** | 08C: submit at 0/1/2/3; withdraw at 3 then submit; reject at 3 then submit; expiry at 3 then submit in the same boundary. |
| **Value** | **3 — Provisional.** |

### F-DP-002 — One live proposal per direction and type

| Field | Definition |
|---|---|
| **Purpose** | Prevent duplicate and reciprocal-proposal ambiguity (DIP-044, DIP-050). |
| **Definition** | `live(from, to, type) = count(proposals p where p.from = from and p.to = to and p.type = type and p.status = PENDING)`. Valid state: `live ≤ 1` per **direction**. |
| **Variables** | `from`, `to` = nation IDs, **ordered** (`from → to`); `type` ∈ `{DP-T01, DP-T02, DP-T03, AMEND, RENEW, TERMINATE}`. Unit: proposals. |
| **Range** | `0` or `1` per ordered pair. |
| **Bounds** | A second `PENDING` in the **same direction** and type fails `DPF-04`. A reciprocal proposal is the opposite direction, so it is **not** a duplicate and both may be `PENDING` (DIP-044). |
| **Rounding** | None. |
| **Timing** | Checked at submission and P2. |
| **Edge cases** | A reciprocal proposal (B→A of the same type while A→B is pending) is a **different ordered key**, so both may be `PENDING`. Once **either** activates, the pair holds an `ACCEPTED`/`ACTIVE` agreement whose key is **unordered** (F-DP-003, DIP-052), so the other proposal fails at P2 with `DPF-04` and is recorded `EXPIRED` with the reciprocal reason. Proposal identity is ordered; agreement identity is not — the two keys must never be conflated (DIP-124). |
| **Source** | DIP-044, DIP-050, DIP-052, DIP-124. |
| **Dependencies** | F-DP-001, F-DP-003. |
| **Example** | A→B `DP-T01` pending at 1000. B→A `DP-T01` submitted at 1002 is allowed, because it is a different ordered key. B accepts A's proposal at 1003, so the agreement is `ACCEPTED` at 1004 with the unordered key `{A,B}+DP-T01`. A's acceptance of B's reciprocal is re-validated at 1004 and fails `DPF-04` because the unordered pair now has an `ACCEPTED` `DP-T01`; B's reciprocal is recorded `EXPIRED` with reason “a reciprocal agreement activated”. |
| **Validation** | 08C: duplicate same-direction; reciprocal both directions; reciprocal accept race; the same type in the reverse direction after activation (must fail); a different type on the same pair (allowed). |
| **Value** | **1 — structural, not a tunable number.** |

### F-DP-003 — Active agreement count

| Field | Definition |
|---|---|
| **Purpose** | Enforce the declared agreement cap (DIP-054/DIP-106). |
| **Definition** | `active(n) = count(agreements a where (a.party1 = n or a.party2 = n) and a.status ∈ {ACCEPTED, ACTIVE})` |
| **Variables** | `n` = nation ID; `a` = agreement. Unit: agreements. |
| **Range** | `0 ≤ active(n) ≤ 8`. |
| **Bounds** | Acceptance of a ninth fails `DPF-11`. A proposal may be submitted when `active(n) = 8` only if it warns that acceptance will fail; the submission itself is allowed (the cap is on active agreements, not proposals). |
| **Rounding** | None. |
| **Timing** | Checked at submission (warning), acceptance (fail closed), P2 and P7. |
| **Edge cases** | An agreement counts once even if both parties are the same nation (impossible; DIP-123). A terminated/expired/breached/completed agreement does not count. An `ACCEPTED` aid counts until delivery or termination. |
| **Source** | DIP-054, DIP-106. |
| **Dependencies** | F-DP-002, F-DP-009. |
| **Example** | A holds 8 active agreements (3 NAPs, 3 consultations, 2 aids). A ninth acceptance fails `DPF-11`. If one NAP expires at the boundary, the acceptance may succeed at the next boundary. |
| **Validation** | 08C: 7/8/9; expiry then accept; terminate then accept; aid delivery then count. |
| **Value** | **8 — Provisional.** |

### F-DP-004 — Proposal expiry

| Field | Definition |
|---|---|
| **Purpose** | Define when an unanswered proposal lapses (DIP-046). |
| **Definition** | `expiry_turn(t) = submitted_turn + 36 + frozen_pair(submitted_turn, t)`. Evaluated at each P2; the deadline can only move **later**, never earlier. |
| **Variables** | `submitted_turn` = the boundary at which the proposal was recorded; `frozen_pair(a, b)` = boundaries in `(a, b]` on which **either** party was frozen, each counted once (DIP-105(a)). Unit: turn number. |
| **Range** | `expiry_turn ≥ submitted_turn + 36`. |
| **Bounds** | The expiry is a boundary; a proposal submitted between boundaries is dated to the next boundary. |
| **Rounding** | None. |
| **Timing** | Evaluated at P2 of each boundary; at `current_turn = expiry_turn` the proposal becomes `EXPIRED` before activation checks (DIP-103). |
| **Edge cases** | A freeze that begins after submission extends the deadline by its full duration. A freeze that ends exactly at the expiry boundary still extends by the frozen boundaries; the proposal does not expire on the boundary the state ends. If **both** parties are frozen on the same boundary the pair gains **one** boundary, not two — the same lost boundary is restored once. A withdrawal or acceptance before expiry ends the clock, and a deadline already extended does not shrink when the freeze ends. |
| **Source** | DIP-046, DIP-105; DIP-022. |
| **Dependencies** | DIP-103; B-06 state flag. |
| **Example** | Proposal submitted at 1000; no freeze. Expiry 1036. Notified at 1024 (12 turns before). At P2 of 1036 it is `EXPIRED`. If the proposer was in `CRISIS` on 12 boundaries, expiry becomes 1048. If the proposer was frozen on 1010–1015 and the counterparty on 1013–1018, the union is 1010–1018 = **9** boundaries, so expiry is 1045 — not 1048, because 1013–1015 are counted once. |
| **Validation** | 08C: no freeze; proposer freeze; counterparty freeze; **both frozen on the same boundary (+1 only)**; disjoint freezes (sum); freeze ending at expiry; freeze beginning after expiry; withdrawal at 1035; acceptance at 1036 (must fail as expired). |
| **Value** | **36 turns — Provisional.** |

### F-DP-005 — Posture cooldown

| Field | Definition |
|---|---|
| **Purpose** | Prevent posture churn and notification spam (DIP-027). |
| **Definition** | `eligible_turn(t) = last_posture_change_turn(pair, direction) + 12 + frozen_turns(actor, last_posture_change_turn, t)` — **12-turn base cooldown + the actor's own freeze extension** (DIP-105(b)). Evaluated at the boundary being validated, so the extension only ever grows and the cooldown is 12 **unfrozen** boundaries. |
| **Variables** | `actor` = the nation that changed its posture and must wait — the **only** nation whose freeze counts; `pair` = unordered; `direction` = actor→target; `last_posture_change_turn` = the turn of the last successful change, or `-∞` if none; `frozen_turns(actor, a, b)` = boundaries the actor spent in `TRANSITION`/`CRISIS` in `(a, b]`; `t` = the boundary being validated. Unit: turn number. |
| **Range** | `eligible_turn(t) ≥ last_posture_change_turn + 12`. |
| **Bounds** | The freeze interval is `(last_posture_change_turn, t]` — it starts **at the change itself**, exclusive at the start and inclusive at `t`, the same start the base 12 turns use. A change at `current_turn < eligible_turn(current_turn)` fails `DPF-08`; at `current_turn ≥ eligible_turn(current_turn)` it is allowed. |
| **Rounding** | None. |
| **Timing** | Checked at submission. |
| **Edge cases** | A failed change (wrong state, unavailable target) does **not** set `last_posture_change_turn` (DIP-032). A no-op change to the same posture does not set it. A reroll resets the replacement's posture to `NEUTRAL` and clears its cooldowns. Only the actor's freeze counts: the counterparty's freeze never lengthens the actor's wait, and a boundary on which **both** nations are frozen is still one boundary for the actor. Freeze inside the 12 turns and freeze after them are the same operation — the eligible turn moves by the frozen boundaries in `(last, t]` — but a change cannot resolve on a boundary where the actor is frozen, because diplomacy is read-only then (DIP-022). |
| **Source** | DIP-027, DIP-032, DIP-105, DIP-127. |
| **Dependencies** | B-06 freeze; DIP-105. |
| **Example** | A sets `HOSTILE` toward B at 1500. No freeze: `eligible_turn = 1512`, so A may set `TENSE` at 1512 and may not set `FRIENDLY` at 1506. If A is in `CRISIS` on 1504, 1505 and 1506 (3 boundaries), `eligible_turn(1506) = 1515`: 1514 fails, 1515 passes. If only **B** was frozen over those boundaries, the eligible turn stays 1512. If A is frozen for a long block, the rule is the same one applied repeatedly: at 1600 with 100 frozen boundaries since 1500 the eligible turn is 1612 — 12 unfrozen boundaries still have to elapse. |
| **Validation** | 08C: change at +11 (fail), +12 (pass); failed change does not consume; no-op does not consume; actor freeze +3 (1514 fails, 1515 passes); **counterparty freeze +0**; both frozen on one boundary (+1 only); long freeze block (12 unfrozen boundaries); interval boundary at `last_posture_change_turn` itself. |
| **Value** | **12 turns + actor freeze — Provisional.** |

### F-DP-006 — Consultation notice: validity (6a) and cooldown (6b)

Two different timers share this rule. **Validity** is the window in which a notice may authorise a hostile act; **cooldown** is how soon the same nation may send another notice. They are calculated separately and must never be reported as one number.

**6a — Validity.**

| Field | Definition |
|---|---|
| **Purpose** | Define when a `DP-T02` notice authorises a hostile act (DIP-039a, DIP-031). |
| **Definition** | `valid(notice, action_turn, t) = (action_turn ≥ notice.turn + 12) and (action_turn ≤ notice.turn + 36 + frozen_pair(notice.turn, t))`. |
| **Variables** | `notice.turn` = the boundary the notice was recorded; `action_turn` = the boundary the posture change or embargo would resolve; `frozen_pair` = boundaries in the interval on which **either** party was frozen, each counted once (DIP-105(a)). Unit: turns. |
| **Range** | `true` or `false`. |
| **Bounds** | Outside the window, `DPF-09`. A missing notice is also `false`. |
| **Rounding** | None. |
| **Timing** | Checked at submission and P2 of the hostile act. |
| **Edge cases** | Only the **end** moves with freeze; the 12-turn minimum does not, because it is a minimum wait, not a deadline (DIP-105). The notice does not expire early if the pact is amended; it uses the window in force when sent. A notice sent before the pact activates is invalid. A notice sent after the pact expires is invalid. If both parties are frozen on the same boundary the window gains one boundary, not two. |
| **Source** | DIP-039a, DIP-105; `DP-T02`. |
| **Dependencies** | F-DP-005 (posture), F-DP-006b (cooldown), F-DP-008 (embargo). |
| **Example** | Notice at 2000, no freeze. A `HOSTILE` change at 2010 fails (`< 12`). At 2012 it passes. At 2036 it passes. At 2037 it fails. With the notice's recipients frozen on 12 boundaries inside the window, the end becomes 2048: 2048 passes, 2049 fails. |
| **Validation** | 08C: 11/12/36/37; no freeze / pair freeze / both frozen on one boundary; no notice; notice before activation; notice after expiry; the minimum wait unaffected by freeze. |
| **Value** | **12–36 turns (end + freeze) — Provisional.** |

**6b — Cooldown.**

| Field | Definition |
|---|---|
| **Purpose** | Stop notice spam (DIP-039a). |
| **Definition** | `notice_eligible(t) = last_notice_turn + 12 + frozen_turns(actor, last_notice_turn, t)`. |
| **Variables** | `last_notice_turn` = the boundary of the actor's last notice to that counterparty; `frozen_turns` = boundaries **the actor** spent frozen in the interval (DIP-105(b)). Unit: turn number. |
| **Range** | `notice_eligible ≥ last_notice_turn + 12`. |
| **Bounds** | A notice at `current_turn < notice_eligible` fails `DPF-10`. At or after it, the notice is allowed. |
| **Rounding** | None. |
| **Timing** | Checked at submission. |
| **Edge cases** | The counterparty's freeze never extends the actor's cooldown. A failed notice attempt does not set `last_notice_turn`. A reroll clears the cooldown for the replacement. |
| **Source** | DIP-039a, DIP-105. |
| **Dependencies** | F-DP-006a. |
| **Example** | Notice at 2000 → second notice eligible 2012. At 2011 it fails `DPF-10`; at 2012 it passes. If the sender was frozen on 2 boundaries, the eligible turn becomes 2014. |
| **Validation** | 08C: +11 (fail), +12 (pass); actor freeze (+2); counterparty freeze (no change); failed attempt does not consume. |
| **Value** | **12 turns (+ actor freeze) — Provisional.** |

### F-DP-007 — Breach cooldown

| Field | Definition |
|---|---|
| **Purpose** | Ensure a break has a visible, bounded consequence (DIP-073/DIP-106). |
| **Definition** | `eligible_turn(t) = breach_turn + 36 + frozen_turns(actor, breach_turn, t)` for the **same pair and type** — **36-turn base cooldown + the breaker's own freeze extension** (DIP-105(b)). Evaluated at the boundary being validated, so the cooldown is 36 **unfrozen** boundaries. |
| **Variables** | `actor` = the nation that broke the agreement and must wait — the **only** nation whose freeze counts; `breach_turn` = the boundary the agreement became `BREACHED`; `frozen_turns(actor, a, b)` = boundaries the actor spent in `TRANSITION`/`CRISIS` in `(a, b]`; `t` = the boundary being validated; `pair`/`type` identify the blocked proposal. Unit: turn number. |
| **Range** | `eligible_turn(t) ≥ breach_turn + 36`. |
| **Bounds** | The freeze interval is `(breach_turn, t]` — it starts **at the break**, the same start the base 36 turns use. A proposal of the same type to the same counterparty at `current_turn < eligible_turn(current_turn)` fails `DPF-14`; at or after it, the proposal is allowed. A different type or a different counterparty is unaffected. |
| **Rounding** | None. |
| **Timing** | Checked at submission. |
| **Edge cases** | A break of an aid and a break of a NAP on the same turn create two cooldowns, one per type. A mutual termination creates none. A reroll clears the cooldown for the replacement (new nation, no history), which is part of DIP-087's disclosed limitation. Only the breaker's freeze counts: the counterparty's freeze never lengthens the breaker's wait, and a boundary on which both are frozen is one boundary. Freeze extends the wait in the same way it extends a posture cooldown (F-DP-005); a break cannot resolve on a frozen boundary in any case (DIP-022). |
| **Source** | DIP-073, DIP-087, DIP-105, DIP-106. |
| **Dependencies** | F-DP-001, F-DP-002. |
| **Example** | A breaks a NAP at 1500. No freeze: A cannot propose `DP-T01` to B until 1536, and may propose `DP-T02` at 1501. If A is in `TRANSITION` on 1502–1504 (3 boundaries), `eligible_turn(1504) = 1539`: 1538 fails with `DPF-14`, 1539 passes. If only **B** was frozen over those boundaries, the eligible turn stays 1536. A long freeze behaves the same way: the cooldown is 36 unfrozen boundaries from the break. |
| **Validation** | 08C: same type at +35 (fail), +36 (pass); **actor freeze +3 (1538 fails, 1539 passes)**; **counterparty freeze +0**; both frozen on one boundary (+1 only); long freeze block; boundary at `breach_turn` itself; different type (pass); different counterparty (pass); reroll (new nation, pass). |
| **Value** | **36 turns + actor freeze — Provisional.** |

### F-DP-008 — Embargo term and re-imposition

| Field | Definition |
|---|---|
| **Purpose** | Bound the sanction and prevent a permanent or spammed embargo (DIP-094/DIP-106). |
| **Definition** | `end_turn = declared_turn + 24` — **not** freeze-aware; `reimpose_eligible(t) = end_turn + 12 + frozen_turns(imposer, end_turn, t)` — **12-turn base cooldown + the imposer's freeze extension** (DIP-105(b)), so the wait is 12 **unfrozen** boundaries of the imposer. A lift sets `end_turn = lift_turn` and measures the cooldown from that lift. |
| **Variables** | `declared_turn`, `lift_turn` = boundaries; `end_turn` = expiry boundary (or the lift boundary); `imposer` = the declaring nation, the **only** nation whose freeze counts for the cooldown; `frozen_turns(imposer, a, b)` = boundaries the imposer spent in `TRANSITION`/`CRISIS` in `(a, b]`; `t` = the boundary being validated. Unit: turns. |
| **Range** | `end_turn = declared + 24`; `reimpose_eligible(t) ≥ end_turn + 12`. |
| **Bounds** | The freeze interval is `(end_turn, t]` — it starts at the term's end, or at the early lift that replaced it. A new embargo by the same imposer on the same target at `current_turn < reimpose_eligible(current_turn)` fails `DPF-08`; at or after it, the declaration is allowed. A different target is unaffected. |
| **Rounding** | None. |
| **Timing** | Declared at P4 step 5; expired or lifted at P4 step 5; re-imposition checked at submission and P2. |
| **Edge cases** | **The 24-turn term is not extended by either party's freeze** (DIP-105, exception 1): a coercive act must not grow because the target was politically paralysed. The re-imposition cooldown **is** extended by the imposer's freeze only; the target's freeze never lengthens the imposer's wait. A lift at 10 turns still requires the 12-turn cooldown from the lift, not from the original declaration. A same-boundary expiry and re-declaration fails, because the new `reimpose_eligible` is at least `end_turn + 12`. The target's own embargo is independent (DIP-099). A reroll lifts the old nation's embargo and clears its cooldowns. |
| **Source** | DIP-094, DIP-098, DIP-099, DIP-105, DIP-127. |
| **Dependencies** | B-07 embargo hook; B-03 pair check. |
| **Example** | Declared at 1600; end 1624; re-impose eligible 1636. Lifted at 1610; re-impose eligible 1622. If the imposer was frozen on 1626–1627 (2 boundaries), the expiry path's eligible turn becomes 1638 — the term still ended at 1624. If only the **target** was frozen, the eligible turn stays 1636. |
| **Validation** | 08C: expiry at 24; term not extended by either freeze; lift at 10; re-impose at 34 (fail) and 36 (pass); imposer freeze +2; target freeze +0; lift then re-impose at +11/+12; same-boundary re-declare (fail); target's own embargo. |
| **Value** | **24-turn term (not freeze-extended); 12-turn base re-imposition cooldown + imposer freeze — Provisional.** |

### F-DP-009 — Agreement expiry and renewal

| Field | Definition |
|---|---|
| **Purpose** | Define the term and the prospective renewal (DIP-067). |
| **Definition** | `expiry_turn(t) = activation_turn + 360 + frozen_pair(activation_turn, t)`; a valid renewal sets `expiry_turn' = expiry_turn + 360`. An aid has no expiry; it completes on delivery. |
| **Variables** | `activation_turn` = the boundary the agreement became `ACTIVE`; `frozen_pair` = boundaries in `(activation_turn, t]` on which **either** party was frozen, each counted once (DIP-105(a)). Unit: turn number. |
| **Range** | `expiry_turn ≥ activation_turn + 360`. |
| **Bounds** | A renewal is valid only if it activates at a boundary **strictly before** `expiry_turn`. At or after expiry, `DPF-12`. |
| **Rounding** | None. |
| **Timing** | Evaluated at P2; expiry runs before activation (DIP-103). |
| **Edge cases** | A freeze extends the term for both parties; if only one party is frozen, the term still extends by that party's frozen boundaries (the other party is not penalised by the freeze). If **both** are frozen on the same boundary the term gains **one** boundary, not two. The extension is calculated once and is **not** re-applied to a renewal (the “strictly before expiry” test uses the already-extended expiry, DIP-105 exception 3). A renewal accepted before expiry but activating at the expiry boundary fails `DPF-12`. |
| **Source** | `DP-T01`/`DP-T02`; DIP-067, DIP-105, DIP-058. |
| **Dependencies** | F-DP-004; B-06 freeze. |
| **Example** | Activation 1011; expiry 1371. Renewal accepted at 1370 activates at 1371 — but 1371 is not strictly before 1371, so it fails `DPF-12`; the parties should have renewed earlier. A renewal accepted at 1350 activates at 1351 and sets expiry 1731. |
| **Validation** | 08C: expiry at 360; renewal at 359 (pass), 360 (fail); freeze; aid completion; version unchanged by renewal. |
| **Value** | **360 turns — Provisional.** |

### F-DP-010 — Derived breach count

| Field | Definition |
|---|---|
| **Purpose** | Define the only derived diplomatic number (DIP-085). |
| **Definition** | `breach_count(n, t) = count(events e where e.type = AGREEMENT_BREACHED and e.actor = n and t − 4380 < e.turn ≤ t)` |
| **Variables** | `n` = nation; `t` = current turn; `e.turn` = breach boundary. Unit: count (integer). |
| **Range** | `0 ≤ breach_count ≤ number of breaches in the window`; unbounded in principle, finite in practice. |
| **Bounds** | No negative value; no partial credit; a breach at exactly `t − 4380` is **outside** the window (strict lower bound); a breach at `t` is inside. |
| **Rounding** | None. |
| **Timing** | Evaluated for display at P6; not an input to any other rule. |
| **Edge cases** | A retired nation keeps its historical count on its page; the replacement starts at 0. A breach by a nation that later changes its name remains attributed to the nation ID, not the name. A correction event does not decrement the count unless a `D-` entry authorises a reversal (none does). |
| **Source** | DIP-085, DIP-086, DIP-090, DIP-120; UD-033/D-128. |
| **Dependencies** | DIP-117 (class-P events); DIP-127 (retirement). |
| **Example** | Breaches at turns 100, 200 and 5000. **At current turn 4480** the lower bound is `4480 − 4380 = 100`, so the window is `100 < e.turn ≤ 4480`: the breach at 100 is **excluded** (it sits exactly on the strict bound), the breach at 200 is **included**, and the breach at 5000 is **excluded** as it is in the future. Count = **1**. At current turn 4580 the window is `200 < e.turn ≤ 4580`: the 200 breach is now excluded and the count is **0**. At current turn 5000 the window is `620 < e.turn ≤ 5000`: only the 5000 breach counts. At current turn 4380 the window is `0 < e.turn ≤ 4380`: the 100 and 200 breaches are inside, the 5000 one is not — count = **2**. |
| **Validation** | 08C: 0/1/2/3 breaches; **turn 4480 with a breach at exactly 100 (excluded)**; turn 4380 (two inside); breach at exactly `t` (included); breach at `t + 1` (future, excluded); retired nation; replacement; rename; no effect on any other rule. |
| **Value** | **4,380 turns (365 days) — Provisional.** |

### F-DP-011 — Aid conservation

| Field | Definition |
|---|---|
| **Purpose** | Guarantee that aid moves value and creates none (DIP-040; ECN-212). |
| **Definition** | For amount `A`: `payer_after = payer_before − A`; `recipient_after = recipient_before + A`; `A ≥ 1`; `A ≤ available_crowns(payer)`; `reserved(payer, A)` at acceptance. Sum of all balances is unchanged. |
| **Variables** | `A` = integer crowns; `payer_before`/`recipient_before` = available crowns at P4; `available_crowns` excludes reservations. Unit: crowns. |
| **Range** | `A ≥ 1`; `payer_after ≥ 0` (no debt, D-050); `recipient_after ≥ 0`. |
| **Bounds** | If `A > available_crowns(payer)`, submission fails `DPF-05`; if the reservation fails at acceptance, `DPF-05`; if the reservation is lost before P4, the transfer is re-queued or terminated (DIP-129), never overdrawn. |
| **Rounding** | None. |
| **Timing** | Submission check; acceptance reservation; P4 transfer with matched ledger events. |
| **Edge cases** | A zero or negative amount is `DPF-13`. A recipient at its treasury cap? B-04 has no treasury cap; the transfer still credits. A frozen party: the delivery waits (DIP-105). A voided boundary: re-queue, no breach. |
| **Source** | DIP-040, DIP-071, DIP-129; ECN-212; D-050/D-055. |
| **Dependencies** | B-04 reservation/ledger; B-02 P4. |
| **Example** | Payer 12,000 available, recipient 3,000, A = 5,000. Reservation leaves payer available 7,000. At P4: payer 7,000, recipient 8,000; world total unchanged (15,000). A = 0 fails `DPF-13`; A = 12,001 fails `DPF-05`. |
| **Validation** | 08C: normal; exact balance; one over; zero; negative; voided turn; freeze; pair restriction; conservation. |
| **Value** | **Integer crowns; no fee — structural.** |

### F-DP-012 — Agreement version increment

| Field | Definition |
|---|---|
| **Purpose** | Make every amendment a distinct, consent-bearing version (DIP-064). |
| **Definition** | `version' = version + 1` on a valid `AMEND` activation; the prior version is recorded `SUPERSEDED` with its activation and supersession turns. A renewal does **not** increment the version; a termination/expiry/breach does not change it. |
| **Variables** | `version` = positive integer, starting at 1 at first activation. Unit: version number. |
| **Range** | `1 ≤ version ≤ 2^31 − 1` (implementation bound; no design limit). |
| **Bounds** | An amendment that would set `version' ≠ version + 1` is invalid (`DPF-13`). |
| **Rounding** | None. |
| **Timing** | At P4 of the amendment's activation. |
| **Edge cases** | Two amendments accepted for the same version: the first by ordering wins; the second fails at P2 with `DPF-04` (one live `AMEND` per pair+agreement). A version history is immutable; a correction is a new version, not an edit. |
| **Source** | DIP-053, DIP-064, DIP-065. |
| **Dependencies** | F-DP-009. |
| **Example** | Version 1 activated 1011. Amendment accepted 1204, activated 1205 → version 2; version 1 marked `SUPERSEDED` at 1205. Renewal at 1350 keeps version 2. |
| **Validation** | 08C: v1→v2; two amendments race; renewal does not increment; invalid type change; version history retained. |
| **Value** | **+1 per amendment — structural.** |

---

## 3. Consolidated limits

| Limit | Formula | Value | Failure |
|---|---|---|---|
| Outgoing proposals | F-DP-001 | 3 | `DPF-06` |
| Live proposal per direction+type | F-DP-002 | 1 | `DPF-04` |
| Active agreements | F-DP-003 | 8 | `DPF-11` |
| Proposal expiry | F-DP-004 | 36 turns **+ pair freeze** | `EXPIRED` |
| Posture cooldown | F-DP-005 | 12 turns **+ actor freeze** | `DPF-08` |
| Notice window (validity) | F-DP-006a | 12–36 turns **+ pair freeze** | `DPF-09` |
| Notice cooldown | F-DP-006b | 12 turns **+ actor freeze** | `DPF-10` |
| Breach cooldown | F-DP-007 | 36 turns **+ actor freeze** | `DPF-14` |
| Embargo term | F-DP-008 | 24 turns, **never freeze-extended** | `EXPIRED` |
| Embargo re-imposition | F-DP-008 | 12 turns **+ imposer freeze** | `DPF-08` |
| Agreement term | F-DP-009 | 360 turns **+ pair freeze** | `EXPIRED` |
| Aid amount | F-DP-011 | integer ≥ 1 | `DPF-05`/`DPF-13` |
| Breach window | F-DP-010 | 4,380 turns | — |
| Version | F-DP-012 | +1 | `DPF-13` |

**Freeze column, not a second value.** A value marked “+ freeze” is the base duration with DIP-105's extension applied; the base itself never changes with freeze. `+ pair freeze` uses `frozen_pair(a, t)` (each boundary once, either party); `+ actor freeze` uses `frozen_turns(actor, start, t)` from **that timer's own start event**; `+ imposer freeze` uses `frozen_turns(imposer, end_turn, t)`. Each row's wording must match the formula it cites, and no row is extended by a freeze it does not name. A cooldown is therefore a count of **unfrozen** boundaries, not a longer wall-clock wait.

**DIP-152 — No other number exists.** If a later prompt needs a diplomatic number not in this table, it must add a formula to this register and a rule to B-08 together. A number introduced in a screen, a test or an implementation note is not a rule.

---

## 4. Validation expectations

**DIP-153 — Arithmetic checks are document checks.** Prompt 08C and the B-08 validator should recompute every example in this register and in B-08 §20. A mismatch is a documentation defect. No runtime, load, concurrency or security test is possible, because no implementation exists.

**DIP-154 — Boundary cases are mandatory.** Each formula's validation must include the value exactly at its bound, one below and one above, plus the freeze case and the retired-nation case. A test that only checks the happy path does not validate the limit.

**DIP-155 — Values are labelled everywhere.** Every surface that shows a limit or a term must show the word "provisional" or a link to this register until Prompt 14 validates it. A player-facing claim that a value is balanced is prohibited.

**DIP-156 — One authority.** If this register and B-08 disagree, B-08's rule wins for *what* happens and this register is corrected for *how it is calculated*. A second formula for the same value is a defect.

**DIP-157 — No numeric reputation.** The register deliberately has no formula for trust, honour, standing, prestige or diplomatic score. F-DP-010 is a count of events, not a score; it feeds no other calculation. Adding a score formula requires a new decision and the reversal of DIP-084.
