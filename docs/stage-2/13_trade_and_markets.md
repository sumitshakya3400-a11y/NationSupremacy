# Trade and markets

**Version:** 1.1 · **Created:** 2026-10-28 · **Stage 2, Prompt 07B** · **Revised:** 2026-10-29 (v1.1 is the Prompt 07C reconciliation: **E1** now records the single 200-crown payment on the correct legs instead of a self-cancelling `+200`/`−200` pair on both sides; **MKT-039**, **MKT-058**, **MKT-095**, **MKT-129** and **MKT-135** state one canonical space predicate, `u ≤ W − total_inventory − space_reserved`, and no longer add reservations back; **MKT-144/MKT-145** and **E5/E20** describe the ratio band as the asymmetric rule it is and add reversed and discount boundaries. Earlier: first issue, the directed-trade foundation, the required long-term Global Trade Market and its reservation, pricing, fair-value, privacy, accounting and release-gate rules)
**Status:** **Draft** — the authoritative document for Bible part **B-07**. It contains design rules, not implementation. No rule here is implemented, runtime-tested, balanced by play or released. **Global Trade is designed but not available**, and its six release conditions have not been met.
**Rule status vocabulary:** **Approved** (established by an owner constraint or a confirmed project decision) · **Provisional** (a design that binds later prompts but is not owner-approved) · **Proposed** (a candidate a later prompt may adopt or discard) · **Deferred** (belongs to a later stage). A rule ID is stable; rules are superseded, never deleted.

**Authority.** This document is the single authoritative specification for Nation Supremacy's trade and market systems. Where it disagrees with a summary elsewhere, this document wins until both are corrected by a revision. It does **not** own the turn system ([B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md)), the account and network policy ([B-03](09_account_onboarding_nation_creation_and_progression.md)), the economy and ledger ([B-04](10_economy_resources_treasury_and_finances.md) and its [register](10_economic_formula_and_balance_register.md)), production and storage ([B-05](11_cities_infrastructure_production_and_research.md)) or domestic politics ([B-06](12_population_and_domestic_politics.md)); it depends on them and cites them by ID.

**Companions:** [Bible outline](02_master_game_design_bible_outline.md) · [requirements register](03_requirements_traceability.md) · [decision registers](04_approved_and_provisional_decisions.md) · [unresolved questions](05_unresolved_design_decisions.md) · [formula register](13_trade_and_markets_formula_register.md) · [07A research report](research/07A_politics_and_war_market_research.md) · [progress log](06_stage_2_progress_log.md)

---

## 1. Document control and scope

**MKT-001 — What this document owns.** *Provisional (REQ-174).* This document owns: the two market systems and the boundary between them; the directed-offer object, its lines, its lifecycle and its accounting; the Global Trade Market's sell listings and buy offers; the tradable-asset list and the prohibited-asset list; execution, reservation and settlement rules for both systems; pricing, rounding and reference-price presentation; the fair-value band and the fresh-nation transfer window; market-action limits; market privacy, history and retention; published market statistics; the six-part Global Trade release gate; and the market's cross-system contracts.

**MKT-002 — What this document does not own.** *Provisional.* It does not own the turn phases or reservation machinery (B-02); the account, nation, reroll or shared-network policy (B-03); the treasury, resource, ledger or warehouse model (B-04); capacity, power or warehouse expansion (B-05); leadership states (B-06); diplomacy, alliances, warfare, rankings or administration (Prompts 08–12); screens and journeys (Prompt 13); or balance values (Prompt 14). It cites them; it may not silently override them.

**MKT-003 — The two systems and the product requirement.** *Approved scope; design provisional.* Nation Supremacy has **two** trading systems in its long-term design:

| System | Status | Availability |
|---|---|---|
| **A — Directed trades** | The first-playable trading system | Available at first playable, fee-free |
| **B — Global Trade Market** | A **required long-term product feature** | **Deferred** — unavailable until all six release conditions G-1…G-6 are demonstrably satisfied (§9) |

**MKT-004 — Three statements that must all remain true.** *Provisional.* (1) Global Trade is a required part of the long-term product; it is not an optional idea and may not be quietly dropped from the roadmap. (2) Directed trades remain the initial and first-playable trading model. (3) A design document is not an implementation; Global Trade may not be described as available, released or implemented until the gate passes and the code exists and is tested.

**MKT-005 — No second clock, no second ledger.** *Provisional.* Both systems resolve inside B-02's existing two-hour boundary. Neither system may invent a scheduler, a continuous matching daemon, a browser-timed settlement, a second currency or a second ledger. Every market value movement is a B-04 ledger event.

**MKT-006 — No retroactive economic change.** *Provisional (ECN-211).* A trade settles at **P4** and may not change a P3 production result, a P3 obligation or an earlier phase's outcome. A trade accepted after P3 has run waits for the next boundary.

---

## 2. Evidence-to-decision summary from Prompt 07A

**MKT-007 — How the research was used.** *Provisional.* Every material choice below is traceable to a 07A finding (`PWR-###`), an existing project rule (a `D-`, `ECN-`, `ONB-`, `NET-` or `TR-` ID) or an explicitly labelled design rationale. The research is evidence about **Politics & War**, not a rulebook for Nation Supremacy. Where the evidence is weak, the choice below is labelled provisional and given a validation method. Research statements are labelled as facts, reported experiences, inferences, proposed rules or open questions, per 07A §2.4.

| 07A finding | Evidence and limitation | Relevant Nation Supremacy constraint | Design implication | Decision taken here | Status |
|---|---|---|---|---|---|
| `PWR-002`, `PWR-006` — a posted-offer board with manual acceptance; no documented matching engine or priority rule | Moderate; historical player claim + official tutorial + interface shape | B-02 class **Q**; D-034 row 4 requires a pair check before reserving; free-first write budget | Prefer a taker-selected model over an automatic matcher: no priority rule has to be invented, no self-match or restricted-pair leak at match time | **MKT-101…MKT-118**: taker chooses a specific offer/listing; ordering is deterministic for **display** only | Proposed rule |
| `PWR-003` — quantity, total and unit price shown together; `return = quantity × unit price` | Strong interface observation | D-045 integers; ECN-027 book values | Show quantity, unit price, total and book value as four distinct numbers | **MKT-071…MKT-077**, **MKT-133** | Proposed rule |
| `PWR-004`, `PWR-009` — offers persist and can be deleted; no expiry rule found | Moderate; 4-day sample | D-016 offers do not reserve; B-02 `EXPIRED` state exists | Offers must expire; a stale pledge is a liability, and unbounded persistence inflates storage | **MKT-046**: 72-turn expiry (6 days), provisional | Proposed rule |
| `PWR-005`, `PWR-022` — a clicked offer can fail for insufficient resources or cash; consistent with no reservation at posting | Weak-to-moderate, historical | **D-016 is binding** for directed offers | Keep D-016 for directed offers; make the failure explicit, counted and terminal after repeated failure | **MKT-041**, **MKT-047**: no reservation at creation; re-validate at acceptance; three failed acceptances expire the offer (`STALE`) | Approved constraint (D-016) + proposed rule |
| `PWR-007` — Politics & War appears to settle at acceptance | Moderate inference, not a rule | B-02 class Q; ECN-211 requires P4 settlement; TR-070 | Do not copy immediate settlement: reserve at acceptance, settle at P4 | **MKT-052…MKT-058** | Approved constraint (ECN-211) |
| `PWR-011`…`PWR-013` — public index, daily averages, public per-nation trade history | Strong for display; moderate for computation | **D-017**: high confidentiality at first playable; D-027 k = 5 | Publish nothing public at first playable; keep a per-party history; gate any aggregate | **MKT-131…MKT-138**, **MKT-150…MKT-156** | Approved constraint (D-017) |
| `PWR-016`, `PWR-019` — ±30% band for new/flagged nations; new nations may not send all or most of their value | Moderate for the band; strong for the transfer rule | **ONB-031/ONB-032** require a window and a band assigned to Prompt 07; ECN-208 | Base the band on the **book value** (the only anchor that exists at first playable), make it symmetric as a ratio, and make it a **block** for fresh nations and a **signal** for everyone else | **MKT-080…MKT-090**: ratio band 3,000 bp; window 360 turns; ADR-6 | Proposed rule |
| `PWR-017`, `PWR-024` — per-resource active-offer caps; same-network interaction bans | Moderate for the announced cap; strong for the official rules | D-024 requires a declared visible limit for every action; D-034 row 4 | Declare caps and rate limits rather than copying a number; justify each bound | **MKT-059…MKT-067**, **MKT-091…MKT-100** | Proposed rule |
| `PWR-001` — three surfaces: global, alliance, private | Moderate | D-017 first-playable directed trades; Prompt 09 owns alliances | Design the directed and global layers; declare an alliance market out of scope and name its owner | **MKT-008** | Scope decision |
| `PWR-010` — no fee found, and the absence is not proof | Unknown | ECON-016 defers the fee to G-5; directed trade is fee-free at first playable | Do not import a rate; keep the first-playable fee at zero and leave the market fee to G-5 | **MKT-096**, **MKT-122** | Approved constraint + deferred decision |
| `PWR-018`, `PWR-029` — automated trading prohibited; a price API exists behind a key | Strong | Prompt 12 owns enforcement; D-017 hides terms at first playable | State the posture; do not design an execution API; leave enforcement to Prompt 12 | **MKT-139**, **MKT-140** | Proposed rule |
| `PWR-023`, `PWR-025`, `PWR-026` — crossed offers; confirmation fatigue; display ambiguity | Weak, single-source | B-04 requires visible causes; B-02 §23 digests | Show the opposite best price and the spread; require a confirmation only when the price differs from the reference or the pair is unrestricted; state which side gives what | **MKT-075**, **MKT-118**, **MKT-133** | Proposed rule |

**MKT-008 — Deliberately out of scope.** *Provisional.* An alliance market, an auction, a futures or option market, a loan or credit market, an automated trading API and an order-execution bot are **not** designed here. If an alliance market is wanted, Prompt 09 owns it and must declare its permissions, its pair checks and its accounting; it may not reuse this document's listing object without a new decision. Operations Points, research points, development capacity, grid units, housing and political influence are never tradable.

---

## 3. Market philosophy and the shared economic contract

**MKT-009 — Production first, trade second.** *Approved constraint (D-043).* Trade exists to move value between nations, not to create it. No market mechanism mints crowns or resources. A trade is a transfer at a price; the price determines who gains, never whether new value exists.

**MKT-010 — What a price is, and what it is not.** *Provisional.* Four different numbers must never share a label:

| Number | Owner | Meaning |
|---|---|---|
| **Reference price** (`P_ref`) | B-04 register §3.5 | An accounting **book value** for national wealth, cost comparison and the fair-value check. Not a quote, not a floor, not a ceiling |
| **Asking price** | This document | What a seller will accept for one unit if a taker chooses the listing |
| **Buy price** | This document | What a buyer will pay for one unit if a seller chooses the buy offer |
| **Completed trade price** | This document | What one specific exchange actually happened at |

A completed trade price is evidence about one exchange. It is **not** a market-wide valuation, and the game must not present it as one. A published average is a statistic with a stated window, sample and suppression rule, or it is not published at all (§23).

**MKT-011 — Integer crowns and units.** *Approved constraint (D-045).* Every price, quantity and total is a whole number. Every division states `floor` or `ceil`. No trade, statistic or split may use binary floating point. Basis points express every percentage.

**MKT-012 — No debt, no credit, no overdraft.** *Approved constraint (D-050).* A trade may not create a negative balance, an IOU, a deferred payment, a loan or an interest charge. If the crowns are not available, the trade fails.

**MKT-013 — Warehouse space is real.** *Provisional (ECN-124; URB-154).* Units received by trade occupy warehouse space. A purchase that would not fit fails; the sender is never allowed to overfill a receiver's warehouse, and space is reserved at acceptance so a later production phase cannot consume the space a trade promised (§13).

**MKT-014 — Atomicity and idempotency.** *Approved constraint (REQ-009; ECN-211).* Every value-moving trade is all-or-nothing: both legs or neither, with a shared `transfer_id`. A duplicate request produces one trade and returns the original receipt; it never executes twice.

**MKT-015 — Reservation before spending.** *Approved constraint (B-02 TR-067/TR-068).* An accepted market action reserves its cost against the **available** balance. Two accepted actions can never commit the same unit or the same crown.

**MKT-016 — Every displayed lever changes an outcome.** *Approved constraint (D-043).* No market control may be decorative. A price a player cannot choose, a slider that does not change settlement, or a filter that does not change what can be executed is a specification defect.

**MKT-017 — The market is server-authoritative.** *Approved constraint (SEC-012; TR-072).* The browser shows state; it never decides a balance, a price, a match, an eligibility or a settlement. The server re-checks every market action.

---

## 4. Directed trades — the first-playable system

**MKT-018 — Directed-trade definition.** *Provisional (ECON-013; REQ-174).* A **directed trade** is a private, bilateral proposal from one nation to one named counterparty, negotiated as a sequence of revisions and concluded by acceptance. Its terms are visible only to the two parties and to restricted administrative audit (D-017).

**MKT-019 — One leg of a trade is a side.** *Provisional.* A trade has exactly two sides: the **proposer's side** and the **recipient's side**. Each side is an object:

| Field | Type | Rule |
|---|---|---|
| `crowns` | integer ≥ 0 | Crowns that this side gives to the other side |
| `lines[]` | 0…5 entries | Resource lines this side gives |
| `line.resource` | roster ID (D-044) | One of the eleven resources |
| `line.quantity` | integer ≥ 1 | Whole units |
| `line.unit_price` | integer ≥ 0 | Crowns per unit, evaluated in the fair-value check; 0 means "no value claimed" |

A side with `crowns = 0` and no lines gives nothing. A side with `crowns = 0` but lines present still gives value.

**MKT-020 — A trade with an empty side is a gift.** *Provisional.* If exactly one side gives nothing, the trade is **one-sided** and is subject to the fresh-nation rule and the fair-value signal (§17). A trade with **both** sides empty is invalid (`MKT-E01`). There is no separate "gift" object: a gift is a directed trade whose other side is empty, so it inherits the same accounting, audit and pair checks. This is why no market rule may treat a gift as a trade-free path.

**MKT-021 — Two values, two jobs.** *Provisional (F-TM-001…F-TM-004).* One side has two values. Its **declared value** is `D = crowns + Σ(quantity × unit_price)` using the prices the parties submitted; it is what the offer says the goods are worth and what the screen displays. Its **reference value** is `V = crowns + Σ(quantity × P_ref)` using B-04's reference prices; crowns count at face value on both sides. The pair's reference values are `V_low = min(V_A, V_B)` and `V_high = max(V_A, V_B)`; the declared values are `D_low` and `D_high`.

**The fair-value band is evaluated on the reference value, never on the declared price.** A seller can write any unit price; only the book value of what actually moves is independent of the parties' labels. A trade of 1,000 uranium (book 30,000) for 1,000 crowns is out of band even if the offer prints "1 crown per uranium", because the resource side's reference value is 30,000 and the crown side's is 1,000. The declared value is still shown, because the difference between it and the book value is information a player needs (§16).

**MKT-022 — At least one side must give something, and the quantities must be plausible.** *Provisional.* `V_high ≥ 1`. No line may have `quantity > MAX_TRADE_UNITS_PER_LINE` (100,000, provisional), no side may hold more than **5** lines, `crowns ≤ MAX_TRADE_CROWNS` (10,000,000, provisional) and every product in `V` is computed with a checked multiply (F-TM-031). A quantity of zero is not a line; remove the line instead.

**MKT-023 — The offer object.** *Provisional.* A directed offer is the persistent object that carries the negotiation. Its logical fields:

| Field | Meaning |
|---|---|
| `offer_id` | Stable identity, unique per world |
| `chain_id` | Identity of the negotiation; identical across revisions |
| `revision` | Integer ≥ 1, incremented by every counteroffer |
| `author_account_id` | The account that wrote the current revision |
| `proposer_nation_id` | The nation whose side is `side_proposer` |
| `recipient_nation_id` | The named counterparty |
| `side_proposer`, `side_recipient` | The two sides as in MKT-019 |
| `status` | One of the lifecycle states in MKT-026 |
| `created_turn`, `revised_turn`, `expires_turn` | Turn IDs, never wall-clock times |
| `failed_accept_count` | Incremented on each failed acceptance; see MKT-047 |
| `acceptance_action_id` | The accepted action that reserved the trade, if any |
| `reservation_refs` | The crown, resource and space reservations created at acceptance |
| `transfer_id` | Shared id written by the two settlement ledger events |
| `superseded_by` | The revision that replaced this one, if any |
| `termination_reason` | A stable code for `DECLINED`, `CANCELLED`, `EXPIRED` or `FAILED` |

**MKT-024 — One live revision at a time.** *Provisional.* A counteroffer creates a **new revision** in the same chain, authored by the other party, and marks the previous revision `SUPERSEDED`. A superseded revision can never be accepted, settled or reserved, and an acceptance that names it fails with `MKT-E06`. Only the latest revision of an `ACTIVE` or `COUNTERED` chain can be accepted. This is the rule that prevents a stale version from executing.

**MKT-025 — A counteroffer is a new proposal, not an amendment.** *Provisional.* A counteroffer **replaces the terms**; it may change quantities, prices, crowns, the resource lines or even which side gives what. It may not change the counterparty (`recipient_nation_id` is fixed at creation) or the `chain_id`. Each counteroffer resets `expires_turn` to `now_turn + 72` and increments `revision`; a chain is limited to **10 revisions**, after which the parties must create a new chain (`MKT-E07`). The limit is visible before the tenth counteroffer is submitted.

**MKT-026 — The lifecycle states.** *Provisional.* A chain is in exactly one state:

| State | Meaning | Terminal? | Reservations |
|---|---|---|---|
| `ACTIVE` | The current revision awaits the recipient's decision | No | None (D-016) |
| `COUNTERED` | The recipient answered with a new revision; the ball is back with the other party | No | None |
| `ACCEPTED` | The recipient accepted the current revision; the trade is reserved and queued for P4 | No | Both sides and the buyer's space |
| `RESOLVED` | Settled at P4; both legs applied and ledgered | **Yes** | Consumed |
| `DECLINED` | The recipient declined; recorded with a reason | **Yes** | None |
| `CANCELLED` | The current author withdrew the offer before acceptance | **Yes** | Released if any |
| `EXPIRED` | The expiry turn passed, or the offer went `STALE` | **Yes** | Released if any |
| `FAILED` | Accepted, but could not apply at P2 or P4 | **Yes** | Released |

**MKT-027 — Permitted transitions.** *Provisional.*

```
ACTIVE     → COUNTERED | ACCEPTED | DECLINED | CANCELLED | EXPIRED
COUNTERED  → COUNTERED | ACCEPTED | DECLINED | CANCELLED | EXPIRED
ACCEPTED   → RESOLVED | FAILED
RESOLVED, DECLINED, CANCELLED, EXPIRED, FAILED are terminal
```

No state returns to an earlier one. A `FAILED` or `EXPIRED` chain is history; a party that still wants the trade creates a new chain. `ACCEPTED` is the only state that holds reservations.

**MKT-028 — A decline is free and neutral.** *Provisional (D-016's spirit; 07A `PWR-025`).* Declining records the chain as `DECLINED` with a stable reason (`MKT-D01` no longer wanted, `MKT-D02` terms unacceptable, `MKT-D03` counterparty unavailable, `MKT-D04` other). It charges nothing, changes no balance, creates no diplomatic penalty, no reputation effect and no notification to third parties. The proposer sees the decline and its reason code, never a private note.

**MKT-029 — Cancellation.** *Provisional.* The **current author** of the live revision may cancel while the state is `ACTIVE` or `COUNTERED`. Cancellation is immediate (`I` class), terminal, and releases nothing because nothing is reserved. The counterparty sees "the offer was withdrawn" without a reason field. A party may not cancel an `ACCEPTED` chain: acceptance has reserved the trade, and withdrawal is no longer possible. To stop an accepted trade before P4, a party must rely on the P2 failure path, which is not a player action and cannot be triggered at will.

**MKT-030 — Expiry.** *Provisional (F-TM-014).* A chain expires at `expires_turn = revised_turn + 72` (provisional: 72 turns / 6 days). Expiry is evaluated in B-02's **B0** band at the boundary, not on a wall clock, and writes `EXPIRED` with `MKT-D05`. Expiry releases nothing because nothing is reserved. A counteroffer resets the clock; the tenth revision is the last, so the maximum chain life is bounded by ten windows.

**MKT-031 — Why 72 turns.** *Provisional; rationale recorded.* Twelve turns per day makes 72 turns six days: long enough that two players in different time zones can negotiate without simultaneous presence, short enough that a pledge made from stock that has since been spent does not linger for weeks. 07A found Politics & War offers persisting four days with no documented expiry (`PWR-004`); Nation Supremacy cannot copy "no expiry" because a stale pledge plus D-016's no-reservation rule produces exactly the failed-acceptance frustration the research documents (`PWR-022`). Prompt 14 may retune the number through a register revision.

**MKT-032 — An accepted trade is queued, not finished.** *Provisional (B-02 class Q; TR-004).* Acceptance assigns the trade to the current open turn and prints the assigned turn and the closing time. Between acceptance and P4 the interface shows **"pending settlement at Turn N close"**, the reserved figures, and the fact that neither side has moved yet. Nothing may be shown as completed before P7 publishes.

**MKT-033 — Settlement position.** *Provisional (TR-042; §20).* Trade settlement is at **P4**, in the market's declared internal order: **directed trades first (B1 order), then Global Trade executions (B1 order)**. Both sub-phases sit inside P4 and after P3. A trade may not be settled inside P3, and a trade accepted after the turn's P4 has begun joins the next turn.

**MKT-034 — Both legs or neither.** *Provisional (ECN-211; TR-055 row "a trade's counterparty cannot deliver").* At P4 the engine applies the seller's resource removal and the buyer's crown removal, then the buyer's resource addition and the seller's crown addition, inside **one transaction**. If any leg fails, the whole trade fails with the specific code, both reservations are released in the same step, and the digest says why. A partially applied trade is prohibited.

**MKT-035 — A trade does not consume P3 output.** *Provisional (ECN-211).* If P3 produced the steel the seller is trading, it exists before P4 and may be sold. If the trade delivers fertilizer-equivalent inputs, it cannot affect this turn's production; the buyer's production sees it from the next boundary. The interface states this.

---

## 5. Directed-trade creation, negotiation and acceptance

**MKT-036 — Creation.** *Provisional.* Any nation in one of the states permitting economic action (B-03 account state `ACTIVE`/`ELIGIBLE`, nation `active`, not `unavailable`) may create a directed offer to a **visible** nation with which its pair is **not** `RESTRICTED` or `MAINTAINED`. Creation validates, in this order: actor owns the nation; the turn is open; the account and nation are eligible; the pair check; the counterparty exists and is visible; the terms pass MKT-022; the side limits pass MKT-059…MKT-062; the resource IDs are in the roster; the fair-value rule where it applies (§17); and the idempotency key is new. Failure produces `REJECTED` with a stable code and no reservation.

**MKT-037 — Creation reserves nothing.** *Approved constraint (D-016).* Creating or revising a directed offer **does not** reserve crowns, resources or warehouse space. The offered goods may be spent, sold or destroyed before acceptance. This is deliberate: an offer is a published pledge, not a commitment of stock, and Nation Supremacy prefers a possible failed acceptance to dead stock and double-spend complexity. The cost is the failure path in MKT-041.

**MKT-038 — The pledge is disclosed as a pledge.** *Provisional (07A `PWR-022`).* The offer screen states: "Accepting checks both sides again. If the other nation no longer has the offered goods or crowns, the acceptance fails and nothing moves." The interface never shows a directed offer as "guaranteed".

**MKT-039 — Acceptance is the reservation point.** *Provisional (D-016; TR-067).* When the recipient accepts the live revision, the server, inside one transaction: re-validates both sides against the **current** available balances; checks the pair again; checks the recipient's political state; checks each receiving nation's `free_space` (F-TM-025: `W − total_inventory − space_reserved`, already net of every reservation) covers the units it will receive; creates the crown, resource and space reservations for both sides; writes the accepted action; and marks the chain `ACCEPTED`. If any check fails, nothing is reserved and the chain stays in its previous state except for `failed_accept_count`.

**MKT-040 — Acceptance re-validates the whole trade, not just the clicked side.** *Provisional (TR-051).* Both sides' resources, both sides' crowns, both warehouse capacities, the pair state, both nations' eligibility and the recipient's leadership state are read at acceptance. A trade whose proposer has since spent the goods fails even though the recipient did everything correctly.

**MKT-041 — The acceptance failure reasons.** *Provisional.* A failed acceptance produces a specific, player-visible code on the rejecting side:

| Code | Meaning | What the taker sees |
|---|---|---|
| `MKT-A01` | The proposer no longer has the offered resources | "That nation no longer has the offered goods." |
| `MKT-A02` | The proposer no longer has the offered crowns | "That nation no longer has the offered crowns." |
| `MKT-A03` | The **acting nation** cannot cover its own side (at acceptance or at posting) | "You do not have enough available to complete this trade." |
| `MKT-A04` | Warehouse space is insufficient for the incoming units | "Your warehouse cannot hold the incoming goods." |
| `MKT-A05` | The pair is restricted or maintained | "Interactions with this account are restricted." |
| `MKT-A06` | The recipient's leadership state forbids market actions | "Market actions are unavailable while authority is suspended." |
| `MKT-A07` | The terms fail the fresh-nation fair-value rule | "New-nation protection applies to this trade." |
| `MKT-A08` | The offer expired, was superseded or was cancelled | "This offer is no longer live." |
| `MKT-A09` | Duplicate idempotency key | Returns the original receipt |

**MKT-042 — A failed acceptance moves nothing.** *Provisional (TR-056; NET-029).* No crown, resource or space is reserved or moved; the chain is not marked `FAILED` (that state belongs to an accepted trade that could not settle). The failure is recorded as an event with the code and the acting nation, and both parties' history shows the attempt.

**MKT-043 — Who may accept.** *Provisional.* Only the **named recipient** of the live revision may accept it. A counteroffer transfers the right to accept to the other party. A third party can never accept, and a third party cannot see that the chain exists (D-017). If a nation rerolls, its open chains are withdrawn by B-03's reroll rule (RRL; D-039) and cannot be accepted afterwards (`MKT-A08`).

**MKT-044 — The acceptance window.** *Provisional (TR-063).* Acceptance is submitted while a turn is **OPEN**; it is assigned to that turn and settles at its boundary. An acceptance submitted after `LOCKED` belongs to the next turn. The confirmation names the assigned turn.

**MKT-045 — A counteroffer does not require acceptance of the previous terms.** *Provisional.* Accepting the live revision closes the negotiation; countering replaces it. There is no double-acceptance hazard because only one revision is live (MKT-024) and acceptance marks the chain `ACCEPTED` in the same transaction, so a second acceptance of the same revision fails with `MKT-A08`.

**MKT-046 — Reservation contents at acceptance.** *Provisional.* Acceptance reserves, for each side: its `crowns` against the treasury's available balance, each line's `quantity` against that resource's available balance, and the **incoming units' warehouse space** against the receiving nation's free space. Space is reserved on the **buyer** of each unit (the nation that will receive it), which may be either side in a barter or a bundled trade, and separately for each direction where both sides receive resources. The sender's units remain in its warehouse but become unavailable.

**MKT-047 — The stale-offer rule.** *Provisional.* Each failed acceptance increments `failed_accept_count`. When it reaches **3**, the chain moves to `EXPIRED` with `MKT-D06 (STALE)` in the same boundary. This prevents an unfunded offer from attracting unlimited failed attempts, bounds wasted player effort (07A `PWR-022`) and gives the proposer a visible reason to restock or cancel. A successful counteroffer resets the count to zero, because the terms changed.

**MKT-048 — Why 3.** *Provisional; rationale recorded.* One failure is normal (both sides may legitimately have changed plans). Two is suspicious. Three consecutive failures on unchanged terms mean the offer is not backed in practice; expiring it is cheaper than letting it accumulate. The number is a provisional tuning value owned by Prompt 14.

**MKT-049 — A directed trade may not target an unavailable nation.** *Provisional (TR-053).* A dormant, retired, removed or `unavailable` nation cannot be addressed; an existing chain to a nation that becomes dormant before acceptance fails at acceptance with `MKT-A08` and is marked `EXPIRED` (`MKT-D07`). Dormancy does not fail an already-**accepted** trade: it settles normally, because the reservation already exists.

**MKT-050 — Reroll interaction.** *Provisional (D-039; RRL).* A nation with any `ACCEPTED` and unsettled chain cannot reroll (B-03's pre-reroll check reads the market for exactly this). A nation may reroll with `ACTIVE` or `COUNTERED` chains: those are withdrawn as part of the reroll, the counterparties see `MKT-A08`, and the account's pair records and sanctions survive. The pre-reroll check is exposed in the confirmation screen as a named blocker, never as a hidden timer.

**MKT-051 — Political-state interaction.** *Approved constraint (DMP-262).* While a nation's `leadership_state` is `TRANSITION` or `CRISIS`, its player may **read** the market — offers addressed to it, its own offers, balances, listings — and may **not create, counter, accept, decline or cancel** a directed offer or create a reservation. An **already accepted** trade settles normally at P4; the state change does not fail it. The interface explains the state, says which actions are unavailable, and never presents the restriction as a sanction, a penalty or a fee. 06B imposes no trade tax, tariff or embargo, and this document adds none.

---
## 6. Directed reservations, settlement and failure

**MKT-052 — The reservation set.** *Provisional (TR-067; ECN-125).* An accepted directed trade holds five kinds of reservation, each with its own identity and release path:

| Reservation | Held against | Quantity |
|---|---|---|
| Proposer crowns | Proposer treasury | `side_proposer.crowns` |
| Proposer resources | Each proposer line | `line.quantity` per resource |
| Recipient crowns | Recipient treasury | `side_recipient.crowns` |
| Recipient resources | Each recipient line | `line.quantity` per resource |
| Incoming space | Each receiving nation's warehouse | The units that nation will receive, per resource direction |

A side that gives nothing has no crown or resource reservation. A side that receives nothing has no space reservation. The set is created once, in one transaction, and closed exactly once.

**MKT-053 — Reservations are exclusive and visible.** *Provisional (TR-068; TR-069).* Total, reserved and available are three separate figures everywhere a balance is shown. The sum of a nation's reservations may never exceed its total. A market screen that shows only a total is a specification defect.

**MKT-054 — Space is reserved, not merely checked.** *Provisional; rationale recorded.* B-04 ECN-124 says a purchase fails at acceptance if the goods do not fit, and P3 runs before P4. If acceptance only checked free space, P3 production could fill the warehouse between acceptance and settlement and turn a valid trade into a P4 failure. Reserving the incoming space (ECN-125 already permits a reservation on "output space") makes P3's `free_space` calculation subtract it, so the goods fit at P4. This is a new application of the existing reservation model, not a new balance concept.

**MKT-055 — P2 re-validation.** *Provisional (TR-060).* At P2 the engine re-checks, against the frozen snapshot: both nations still exist and are not `removed`; both sides' reservations are still intact and still cover the terms; the pair is still not restricted for a **new** interaction; the buyer's space reservation still covers the incoming units; and the trade's terms are unchanged since acceptance. It does **not** re-apply the political-state test (MKT-051) and does **not** re-apply the fresh-nation band to a trade that was in band at acceptance and whose parties' ages changed only by the passage of the same turn. Age is evaluated at acceptance; the P2 check uses the acceptance-time verdict for the band, but a **newly restricted pair** is a valid P2 failure (`F3`).

**MKT-056 — P4 settlement.** *Provisional (ECN-211).* At P4 the engine, in one transaction: consumes the proposer's reserved crowns and resources and the recipient's reserved crowns and resources; adds the received crowns and resources to each side; consumes the space reservations; writes `TRADE_SELL` on each side's ledger for what it gave and `TRADE_BUY` for what it received, with one shared `transfer_id`; and closes every reservation. The two crown deltas sum to zero and each resource's two deltas sum to zero.

**MKT-057 — Failure at P2 or P4.** *Provisional (TR-062; TR-055).* A P2 failure marks the chain `FAILED`, releases every reservation in the same step, moves nothing and writes the failure code. A P4 failure does the same for the whole trade: there is no partial settlement. The digest names the code and the side that could not perform, and both parties see the same outcome. The offer is not resurrected; a new chain is required.

**MKT-058 — The settlement order inside P4.** *Provisional (TR-042; TR-044 band B1).* Directed trades settle before Global Trade executions. Within each group, accepted actions are ordered by `submitted_at` then `action_id` (TR-045). Because reservations are exclusive, the order cannot change whether a trade is affordable or whether it fits: the receiving nation's space was reserved at acceptance, and P3's `free_space` already subtracts that reservation. The order changes only the sequence of record writes. A P4 space failure therefore does **not** mean that an earlier trade legitimately filled the warehouse — it means the space reservation was missing or the no-overcommit invariant (MKT-135) was already broken. It is reported as `F4`, and the cause is investigated as a defect, not accepted as ordinary competition.

---

## 7. Directed-trade limits, expiry and anti-spam

**MKT-059 — D-024 requires declared limits, not a hidden hand-wave.** *Approved constraint (D-024).* Every directed-trade action has a visible, server-enforced limit. The limits below are **provisional values**; each states its unit, scope, period, rejection reason, rationale and validation plan. No client may submit past a limit, and no limit may depend on a player being online at a boundary.

| Limit | Value | Unit and scope | Period | Rejection | Rationale |
|---|---|---|---|---|---|
| Active outgoing chains | **5** per nation | Chains in `ACTIVE` or `COUNTERED` authored by the nation | Rolling | `MKT-L01` | A player can negotiate with five counterparts without turning the offer list into spam |
| Chains per counterparty | **1** per nation pair | Live chains between the same two nations | Rolling | `MKT-L02` | Forces one negotiation per relationship; prevents a ladder of near-identical offers |
| Revisions per chain | **10** | Counteroffers in one `chain_id` | Chain lifetime | `MKT-L03` | Bounds negotiation and the row count; ten exchanges is generous for a two-hour game |
| Resource lines per side | **5** | Lines in one side | Per offer | `MKT-L04` | A bundle stays legible; the eleventh resource would need a second screen |
| Quantity per line | **100,000** units | Units in one line | Per line | `MKT-L05` | Above any achievable warehouse; bounds arithmetic and display |
| Crowns per side | **10,000,000** | Crowns in one side | Per side | `MKT-L06` | Far above any plausible treasury; keeps multiplication inside 64-bit range |
| Directed market actions | **20** per nation | Create, counter, accept, decline, cancel | 12 consecutive turns (24 h) | `MKT-L07` | Bounds the write rate and the notification volume without blocking ordinary play |

**MKT-060 — Why five active offers.** *Provisional; rationale recorded.* 07A found staff reducing a spam problem with a cap of three active buy and three active sell offers **per resource** (`PWR-024`), a per-resource model that suits a public board. A directed trade is a relationship, not a price rung, so the natural bound is **per counterparty** (one) plus a **total** that covers a player's regular partners and a few new ones (five). The number is not copied from Politics & War and is not claimed to be balanced.

**MKT-061 — The rate limit is a ceiling, not a budget.** *Provisional (D-024).* The 20-action limit is a denial-of-spam ceiling, not an action currency. It does not refill in a way that rewards waiting for a particular minute, it is visible on the trade screen, and it is evaluated on **turn IDs** (`current_turn − 11 … current_turn`), never on wall-clock time. A player who reaches it is told how many actions remain and when the oldest leaves the window.

**MKT-062 — Limits are enforced before reservation.** *Provisional (NET-029).* A limit rejection happens before any reservation, before any write to the offer's terms and before any notification. It is recorded as an event with the limit code, not as a completed action.

**MKT-063 — Expiry is a boundary job, not a player action.** *Provisional (B-02 band B0).* Expiry runs in P0/P1-adjacent maintenance for the turn, deterministically ordered by `(expires_turn, chain_id)`, and is idempotent. A chain whose `expires_turn` is less than the current turn and which is still `ACTIVE` or `COUNTERED` becomes `EXPIRED`. Expiry of an `ACCEPTED` chain is impossible: acceptance clears the expiry and the trade is governed by P2/P4.

**MKT-064 — Expiry notification.** *Provisional.* Both parties receive one digest line on the first boundary after expiry: "Offer to <nation> expired; nothing was reserved or moved." The line is deduplicated so a retry of the boundary job cannot produce two lines.

**MKT-065 — The offer list is bounded.** *Provisional.* The incoming and outgoing lists show at most **50** chains per page, newest first, with a stable secondary sort by `chain_id`. A player with more than 50 is at the cap in practice (5 outgoing; incoming is bounded by other players' caps but could be larger). Pagination uses a cursor, not an unbounded query, and the count shown is exact.

**MKT-066 — No bulk acceptance.** *Provisional.* There is no "accept all" control. Each acceptance is a separate idempotent action with its own re-validation, because a bulk acceptance would create an unbounded transaction and would make the failure report ambiguous. This is a deliberate friction: the research's confirmation-fatigue finding (`PWR-025`) is answered by **informative** confirmation, not by removing the check.

**MKT-067 — Anti-automation.** *Provisional (Prompt 12 owns enforcement).* Automated offer creation, acceptance, cancellation or price polling that performs an action is prohibited. A read-only notification that tells a player an offer exists, leaving the action manual, is permitted in principle; Prompt 12 writes the enforcement rule and the evidence standard. This document does not add an API, a webhook or a bot surface, and no market rule may assume one exists.

---

## 8. Directed-trade fees

**MKT-068 — The first-playable directed trade is fee-free.** *Approved constraint (ECON-013; D-116; G-5).* There is **no** listing fee, **no** percentage transaction fee, **no** flat transaction fee, **no** hidden tax and **no** political-stability-based charge on a directed trade. The four components are all exactly zero at first playable, and the settlement writes no `FEE` event.

**MKT-069 — Why zero, and what would change it.** *Provisional; rationale recorded.* 07A found no documented Politics & War fee and explicitly refused to treat that absence as proof (`PWR-010`). Nation Supremacy's Stage 1 comparison adopted fee-free directed trade as the point of the private layer (ECON-013), and the fee question for a public market is deferred to G-5. A fee is not needed to solve spam (limits do that), to prevent double-spend (reservations do that) or to fund the ledger (it is a transfer). Adding one now would be an unapproved tax on ordinary play.

**MKT-070 — A future fee is a gate-stage decision, not a silent change.** *Provisional.* Any future directed or global fee requires: a new decision entry; a `fee_bp` or flat value with a stated payer; a `FEE` ledger event; a conservation identity that includes the fee; a player-facing label; and a G-5 record. Until then `fee_bp = 0` and `fee_flat = 0` are the only legal values, and the formula register's fee formula (F-TM-038) returns zero.

---
## 9. Global Trade — status and release gate

**MKT-071 — What Global Trade is.** *Approved scope; design provisional.* The **Global Trade Market** is a world-readable board on which eligible nations publish a resource for sale, or a request to buy one, at a stated unit price in crowns. Any eligible nation may take an open listing, subject to the pair, eligibility, fair-value and capacity rules. It is resource-for-crowns only (MKT-090).

**MKT-072 — Product requirement and release condition are different facts.** *Approved constraint (REQ-010).* Global Trade is **required in the long-term product** and is **not available for release** until all six conditions G-1…G-6 are met. The release gate is not a design question and may not be waived by this document, by a later design prompt, by a schedule or by an owner preference expressed without evidence. A gate that fails leaves the feature in the roadmap and blocks release; it does not delete the feature.

**MKT-073 — Current gate status.** *Provisional; must be updated only with evidence.*

| Gate | Requirement | Current status | Why |
|---|---|---|---|
| **G-1** | Identity and anti-multi integrity controls implemented and functioning, with a declared tolerance band and review process | **NOT MET** | The D-034/D-036 mechanisms are designed, not implemented; no live incident rate exists |
| **G-2** | Actual write counts and a passed budget test demonstrate the market fits the operational budget | **NOT MET** | No market write count has been measured; Stage 3 does not exist yet |
| **G-3** | Measured directed-trade activity demonstrates a reasonable basis for expecting meaningful global-market participation | **NOT MET** | No live play; the qualifying threshold must be read from observed data, not invented |
| **G-4** | A documented reference-price design and manipulation-pattern review exists, with a clear explanation of what the statistic means | **PARTIAL** | This document supplies the design (§16, §23) and the manipulation review (§18); the **review and the implementation** do not exist |
| **G-5** | The fee policy is decided using the gate's required evidence | **NOT MET** | No fee policy is decided; §8 keeps the directed trade at zero and leaves the market fee open |
| **G-6** | Projected settlement disputes fit a declared operational capacity | **NOT MET** | No dispute-rate projection or ops capacity exists |

**MKT-074 — What counts as passing a gate.** *Provisional.* A gate passes only when its **evidence** exists, is recorded, and is reviewed by the role named in MKT-075. A design document, a proposed test, a planned feature, a date, a roadmap entry or a developer's assurance is not evidence. "G-4 partial" means the design half exists; it is not a pass.

**MKT-075 — Gate evidence ownership.** *Provisional.*

| Gate | Evidence owner | Validation method | Passing condition | Corrective action if it fails |
|---|---|---|---|---|
| G-1 | Integrity design + operations | Implemented control suite plus an audit-trail review of live incidents | The declared tolerance band is met over a stated observation window, with every incident reviewed | Keep the market off; fix the control; re-measure |
| G-2 | Architecture | Measured writes per market action × projected actions, against the chosen platform's budget | The projection fits with a declared safety margin, and a load test at the target scale passes | Reduce rows per action, add compaction, or defer the release |
| G-3 | Product/analytics | Completed directed trades per active nation per day over a stated window | The measured rate clears a threshold **set from the data** before the market launches | Keep directed-only; revisit after a population increase |
| G-4 | Economy integrity | Reference-price computation review plus an enumerated manipulation-pattern review | Every pattern is countered, visibly exposed, or accepted with a stated rationale | Fix the statistic or publish it with a caveat flag |
| G-5 | Owner + economy | The Stage 1 fee comparison re-run with live data | A fee posture (including zero) is recorded with its payer, rate and ledger event | Keep zero; do not invent a rate |
| G-6 | Operations | Projected settlement-dispute rate against declared capacity | Projected disputes are within capacity with a stated margin | Add a dispute path or defer the release |

**MKT-076 — The market is dark until the gate passes.** *Provisional.* At first playable the Global Trade routes return a neutral "not available" state. There is no hidden listing table, no feature flag exposed to clients, no read-only preview of other nations' listings and no "beta" board. A dark feature that can be reached by a crafted request is a release, not a deferral.

**MKT-077 — No claim of readiness.** *Provisional.* No continuity document, roadmap, handoff or UI may describe Global Trade as "ready", "live", "in beta", "implemented" or "released" while any gate is not met. The correct description is: **"designed; release-gated; G-1…G-6 not met."**

---

## 10. Global Trade — sell listings

**MKT-078 — The sell-listing object.** *Provisional.* A sell listing is one resource offered for crowns. Its logical fields:

| Field | Rule |
|---|---|
| `listing_id` | Stable identity |
| `side` | `SELL` |
| `seller_nation_id` | The owner of the offered units |
| `resource` | One roster ID (MKT-090) |
| `quantity_posted` | Integer ≥ 1, ≤ 100,000 |
| `quantity_filled` | Settled units; starts 0 |
| `quantity_locked` | Accepted but unsettled units; starts 0 |
| `quantity_remaining` | `posted − filled − locked` (F-TM-015) |
| `unit_price` | Integer ≥ 1 crown per unit |
| `total_displayed` | `remaining × unit_price`, shown to the taker (F-TM-021) |
| `created_turn`, `expires_turn` | Turn IDs; `expires_turn = created_turn + 72` |
| `status` | `OPEN`, `PARTIALLY_FILLED`, `FILLED`, `CANCELLED`, `EXPIRED`, `SUSPENDED` |
| `reservation_ref` | The inventory reservation created at posting |
| `execution_refs` | The accepted executions and their reservations |
| `public_nation_label` | The seller's public nation name and number, shown on the listing |

**MKT-079 — Posting a sell listing reserves the units.** *Provisional; new decision, scoped.* Posting a sell listing moves `quantity_posted` units from **available** to **reserved** in the seller's inventory. The units stay in the warehouse, still count toward `W`, and still appear in the total; they cannot be sold, consumed, traded or listed again. This is deliberately **not** D-016: D-016 governs a private proposal that a named counterparty may or may not accept; a public listing is an open offer to the world that any eligible taker may execute without further negotiation, so an unbacked listing would be a promise the seller cannot keep and would reproduce the failed-acceptance problem at world scale. The new decision is D-109; D-016 is unchanged and still governs directed offers.

**MKT-080 — Posting does not reserve crowns.** *Provisional.* A sell listing reserves only the offered units. The seller's crowns are untouched. The seller may spend crowns freely; the listing does not depend on them.

**MKT-081 — The seller's warehouse must already hold the units.** *Provisional.* Posting checks `available_units(resource) ≥ quantity_posted`. If not, the listing is rejected with `MKT-L08` and nothing is reserved. The units must already exist; a listing may not be backed by future production.

**MKT-082 — The asking price is the execution price.** *Provisional.* A taker who executes a sell listing pays exactly the listing's `unit_price` per unit. There is no auction, no price improvement, no automatic undercut and no negotiation on a public listing. A seller who wants a different price cancels the remainder and posts again; a taker who wants a different price chooses another listing or makes a directed offer.

**MKT-083 — Partial fills are supported.** *Provisional.* A taker may execute `1 ≤ x ≤ quantity_remaining`. The execution moves `x` units from `quantity_remaining` to `quantity_locked`, reserves `x × unit_price` crowns on the taker, and leaves the listing `OPEN` or `PARTIALLY_FILLED` with the remainder available. Each fill is an independent execution with its own `execution_id`, `transfer_id`, reservations and ledger pair; the listing is the parent, not a single transaction.

**MKT-084 — Why partial fills.** *Provisional; rationale recorded.* The research could not establish whether Politics & War allows partial acceptance (`PWR-006`), so this is not copied. Partial fills are adopted because a small nation may not be able to afford a large lot, and forcing whole-lot purchases would make large listings unusable by exactly the players who need them. The cost is more rows and more complex remaining-quantity accounting; §14 and §19 make that cost explicit, and Prompt 14 may test a whole-lot variant.

**MKT-085 — Cancelling a sell listing.** *Provisional.* The seller may cancel while `status` is `OPEN` or `PARTIALLY_FILLED`. Cancellation releases `quantity_remaining` immediately and leaves `quantity_locked` untouched; the locked units settle at P4. If `quantity_locked` is non-zero, the listing becomes `CANCELLED` with `locked_remainder = true` and closes when the last locked execution resolves. A cancelled listing cannot be executed again, even if an execution later fails and releases its units: those units return to the seller's available inventory, not to the cancelled listing.

**MKT-086 — Expiry of a sell listing.** *Provisional.* At `expires_turn`, the listing expires in the B0 band. `quantity_remaining` is released to the seller; `quantity_locked` is untouched and its executions settle normally. The digest line names the released quantity and any executions still pending.

**MKT-087 — The listing is public while it is open.** *Provisional.* An open sell listing shows: the resource, the remaining quantity, the unit price, the total for the remaining quantity, the created and expiry turns, the seller's public nation name and public number, and its status. It does **not** show the seller's treasury, warehouse, other listings, account identity, network state, sanction state or the reason for any restriction. A listing that is `SUSPENDED` by an administrative action shows "temporarily unavailable", never the reason.

**MKT-088 — A listing is not a contract with a named buyer.** *Provisional.* Posting a sell listing creates no obligation to any particular nation. The seller's only obligation is the reservation: the reserved units are available to the first eligible execution that the server accepts, and the seller may cancel the remainder at any time. This is why the seller cannot be forced to sell to a specific counterparty and why a restricted pair can be excluded without telling the seller who tried.

**MKT-089 — Suspension is administrative and narrow.** *Provisional (Prompt 12 owns the procedure).* A listing may be `SUSPENDED` by a privileged action while a review is open. Suspension blocks new executions, keeps existing locks, records the reason in the restricted audit, and shows only "temporarily unavailable" publicly. It is not a confiscation: the units remain the seller's, and the listing is cancelled or restored when the review closes. No administrator may transfer the units to another nation.

---

## 11. Global Trade — buy offers

**MKT-090 — The buy-offer object.** *Provisional.* A buy offer is one resource requested for crowns. Its logical fields mirror MKT-078 with these differences:

| Field | Rule |
|---|---|
| `side` | `BUY` |
| `buyer_nation_id` | The owner of the crown commitment |
| `quantity_posted` | Integer ≥ 1, ≤ 100,000 |
| `unit_price` | Integer ≥ 1 crown per unit; the **maximum** the buyer will pay |
| `crown_commitment` | `quantity_posted × unit_price` at posting (F-TM-017) |
| `quantity_remaining`, `quantity_locked`, `quantity_filled` | As in MKT-078 |
| `reserved_crowns` | `(remaining + locked) × unit_price`, decreasing only as executions settle |
| `status` | `OPEN`, `PARTIALLY_FILLED`, `FILLED`, `CANCELLED`, `EXPIRED`, `SUSPENDED` |

**MKT-091 — Posting a buy offer reserves the crowns.** *Provisional (F-TM-017).* Posting reserves `quantity_posted × unit_price` crowns on the buyer. The crowns remain in the treasury, count in the total, and are unavailable to any other action. They are released exactly once: consumed by settlement, or released on cancellation, expiry or failure of the remainder. A buy offer may never advertise purchasing power that is not reserved.

**MKT-092 — The buy price is the execution price.** *Provisional.* A seller who executes a buy offer receives exactly the offer's `unit_price` per unit. The buyer does not pay more than the reserved maximum, and the seller does not receive less. There is no price improvement, no bid-ask crossing and no negotiation on a public buy offer.

**MKT-093 — Partial fills on a buy offer.** *Provisional.* A seller may execute `1 ≤ x ≤ quantity_remaining`. The execution locks `x` units of the buyer's crown reservation, reserves `x` units on the seller, and moves `x` from `quantity_remaining` to `quantity_locked`. At settlement the buyer pays `x × unit_price` and receives `x` units; the seller receives the crowns and gives the units. The remaining crown reservation falls by exactly `x × unit_price`.

**MKT-094 — Cancelling and expiring a buy offer.** *Provisional.* Cancellation releases `quantity_remaining × unit_price` crowns immediately; locked crowns stay reserved until their executions settle or fail. Expiry does the same at `expires_turn`. A cancelled or expired buy offer cannot be executed again; a failed execution's crowns return to the buyer's available balance, not to the closed offer.

**MKT-095 — The buyer's warehouse must have room at execution, not at posting.** *Provisional (ECN-124).* A buy offer does not know who will sell to it, and the buyer's warehouse may fill before an execution. Each execution therefore checks the buyer's **`free_space`** at acceptance — the figure that already subtracts every existing space reservation (F-TM-025) — and then reserves the incoming units. Adding the reservations back would ignore them and overbook the warehouse. If the buyer cannot hold them, the execution fails with `MKT-A04` and the buy offer's remaining quantity is unaffected. This is the correct place for the check because the seller cannot be expected to know the buyer's storage.

**MKT-096 — The listing board is symmetric.** *Provisional.* Sell listings and buy offers share one board, one set of filters, one expiry constant and one execution rule. The only differences are which side reserves what and which side receives the resource at settlement. A player who understands one understands the other.

**MKT-097 — No self-trade.** *Provisional.* A nation may not execute its own listing or buy offer. The server rejects it with `MKT-E10`. A nation also may not use a second account to execute its listing; that is the pair rule (D-034 row 4) and, where the accounts are not yet linked, the transfer-graph review (Prompt 12). Self-trade is prohibited because it would let a player manufacture a price, a history or a ranking signal without moving value between independent parties.

**MKT-098 — No wash or circular trading.** *Provisional (D-035; NET-026).* Two accounts may not execute reciprocal listings at a price that returns the same value to each side, and a chain of three or more accounts may not be used to route value around a pair restriction. Where both legs are visible, the server blocks the pair; where they are not, the pattern is a rule violation supported by the audit record. Detection is not claimed to be complete.

---

## 12. Tradable and prohibited assets

**MKT-099 — The eleven resources are the only tradable goods.** *Approved constraint (D-044; ECN-023).* Both systems trade only the roster: **Food, Coal, Oil, Iron, Bauxite, Lead, Uranium, Gasoline, Steel, Aluminum, Ammunition.** The roster is closed; a twelfth resource requires a new decision, a lifecycle, a storage rule and a register entry.

**MKT-100 — Crowns are the only money.** *Approved constraint (D-049).* A trade prices in crowns and settles in crowns. There is no second currency, no gold, no premium currency and no alliance scrip. A trade may not exchange crowns for a promise, a favour, a vote, a treaty, a rank or an entitlement.

**MKT-101 — Prohibited assets.** *Provisional.* None of the following is ever tradable, in either system: Operations Points; research points; development capacity; grid units; housing; population; political influence, approval, stability or legitimacy; technology; buildings or facilities; territory or city slots; account entitlements, cosmetics or badges; moderation outcomes; and any future asset not explicitly added by a decision. A UI that offers any of these for sale is a defect.

**MKT-102 — Military goods are ordinary resources here.** *Provisional.* Ammunition, steel, aluminum, gasoline and the raw inputs are tradable like any other resource. Prompt 10 may add a **war-time** restriction (a blockade, an embargo or a captured-stock rule), but it may not make them non-tradable in peacetime without a decision. A blockade or embargo is a diplomacy/war rule, not a market fee.

**MKT-103 — A resource has one identity everywhere.** *Provisional (D-044).* The same roster ID is used in production, storage, the ledger, the listing, the offer line and the report. A localised display name may differ; the internal ID may not. A trade may not use a "food-like" alias or a bundle named after a resource.

**MKT-104 — No resource substitution.** *Provisional (ECN-006/011).* A trade delivers exactly the resource on the line. A seller may not deliver coal when the line says iron, and a buyer may not accept a substitute. If the wrong resource is the only one available, the trade fails; it does not auto-swap.

---

## 13. Market discovery and presentation

**MKT-105 — Directed discovery.** *Provisional.* The directed screen shows: offers addressed to the player; the player's outgoing chains; each chain's live terms, revision, author, created turn, expiry turn and status; the player's total/reserved/available crowns and resources; and the number of actions left in the 12-turn window. It does **not** show other nations' directed offers (D-017). A player finds a counterparty through diplomacy, alliances, the world view or a direct nation link, not through a public list.

**MKT-106 — Global discovery.** *Provisional.* The global board shows, per resource: the best sell price and quantity, the best buy price and quantity, the **spread** (best buy minus best sell) with a clear "crossed" indicator when the best buy is above the best sell, the number of open listings, and the last published statistic if one exists (§23). The board can be filtered by resource and side, sorted by unit price ascending (sells) or descending (buys), then by `created_turn`, then `listing_id`. The sort is a **display** order, not an execution priority; the taker names the listing.

**MKT-107 — Crossed books are shown, not silently exploited.** *Provisional (07A `PWR-023`).* If the best buy price is at or above the best sell price, the board shows a "crossed" badge and both listings remain separately executable at their own prices. The game does not auto-cross them, and it does not hide the better price. A taker who executes the worse of two compatible listings sees a confirmation naming the better price. This is the deliberate answer to the research's crossed-offer frustration: keep manual choice, remove the information disadvantage.

**MKT-108 — What a listing row promises.** *Provisional.* Each row states, in plain words: the resource, the quantity a taker can buy or sell right now (`quantity_remaining`), the unit price, the total for that quantity, the seller/buyer's public nation label, the expiry turn, and the fact that execution reserves now and settles at the next boundary. It must not imply that the resource has already moved.

**MKT-109 — Four numbers, four labels.** *Provisional.* A listing or offer shows **unit price**, **total**, **reference value** and, where one exists, the **last completed price** for that resource. The reference value is labelled "book value" and carries a tooltip: "An accounting value, not an offer." The last completed price is labelled with its window and sample ("last completed trade", "24-hour average, 7 trades"). No two of these may share a label or a colour.

**MKT-110 — Insufficient data is a state, not a zero.** *Provisional.* When a resource has no listing, the board shows "no sell listings" / "no buy offers", not "0". When a statistic has too few trades, it shows "not enough trades to publish", not "0" and not the last value silently carried forward. The three states — no supply, no demand, insufficient sample — are visually and textually distinct.

**MKT-111 — The confirmation is informative, not routine.** *Provisional (07A `PWR-025`).* A confirmation is required when: the execution price differs from the reference value by more than the fair-value band; the trade is with a nation the player has not traded with before; or the trade is one-sided. It shows the exact unit price, total, book value, the difference and the settlement turn. A routine trade at an in-band price with a known counterparty needs one confirmation, not two. The rule is "confirm the surprising", not "confirm everything".

**MKT-112 — The failure message names the cause.** *Provisional (B-02 §23; ECN-055).* Every rejected or failed market action returns one of the stable codes in MKT-041 or MKT-150, a one-sentence explanation and the next possible action ("restock and ask them to accept again", "choose a smaller quantity", "wait for the next turn"). It never says only "failed".

**MKT-113 — No dark patterns.** *Provisional.* The interface may not pre-select the most expensive listing, hide the total behind a hover, auto-fill a quantity above the player's available balance, or use a countdown that implies the listing will vanish sooner than `expires_turn`. A "buy" button shows the total before it is pressed.

**MKT-114 — Accessibility and the two-hour rhythm.** *Provisional (Prompt 13 owns the final screen design).* The board must be usable without simultaneous presence: a player can read it, choose a listing, accept, and leave; the trade settles at the boundary whether or not the browser is open. No market action requires a notification to arrive in time, and no listing is first-come in a way that rewards refresh speed (MKT-118).

---

## 14. Execution model and determinism

**MKT-115 — The execution model is taker-selected posted price.** *Provisional; the central market decision.* A taker chooses **one specific listing** and a quantity, and executes at that listing's posted unit price. There is no automatic matching engine, no price-time priority, no pro-rata allocation across listings and no crossing of a buy offer with a sell offer. The market is a board of firm posted prices, not a continuous exchange.

**MKT-116 — Why this model.** *Provisional; rationale recorded.* (1) It requires no invented priority rule, and 07A could not find one in Politics & War (`PWR-006`). (2) It is deterministic without a seeded lottery: the taker names the lot. (3) It makes the restricted-pair check local to one listing and one taker, so a blocked pair never needs a "next best" fallback that could leak the restriction. (4) It fits the free-first budget: no per-turn scan of the whole book to find crossings. (5) It preserves the research's strongest positive — the player chooses, and offers can wait (`PWR-002`, `PWR-004`).

**MKT-117 — What the model costs.** *Provisional; trade-off recorded.* A buyer and a seller can both be on the board at compatible prices and not trade (`PWR-023`). The design mitigates this with the crossed badge, the best-price line and a confirmation that names a better listing (MKT-107), but it does not eliminate it. The alternative — an automatic matcher — would solve the crossing and create priority, self-match, restricted-pair and determinism problems that the project has not chosen to take on. Prompt 14 may model both; a change to automatic matching requires a new decision, not a quiet implementation.

**MKT-118 — Determinism rules.** *Provisional (TR-044/TR-045).* Execution is deterministic because the taker names `listing_id` and `x`. Display order is deterministic by `(price, created_turn, listing_id)`. Expiry is deterministic by `(expires_turn, listing_id)`. Settlement order inside P4 is deterministic by `(submitted_at, action_id)`. No rule may use database row order, hash order, client order or wall-clock arrival beyond the frozen keys. A tie in a display sort is broken by `listing_id`.

**MKT-119 — No partial acceptance of a directed offer.** *Provisional.* A directed offer is accepted whole or not at all. A recipient who wants only part of it must counter with the smaller quantity. This is the deliberate difference from a public listing: a private proposal is a single bargain, and splitting it would create a second implied offer that the proposer never made.

**MKT-120 — A taker may execute more than one listing in a turn.** *Provisional.* There is no one-execution-per-turn rule, but the per-nation execution rate limit (MKT-124) and the P4 work bound apply. Each execution is a separate action with its own reservation and settlement.

**MKT-121 — An execution is accepted now and settles at P4.** *Provisional (B-02 class Q).* The taker sees "reserved; settles at Turn N close". The listing's `quantity_locked` rises immediately, the taker's crowns or units are reserved immediately, and nothing moves until P4. The seller may cancel the unlocked remainder in the meantime; the locked quantity is unaffected.

**MKT-122 — Execution races are resolved by reservation, not by arrival order.** *Provisional.* Two takers may attempt the same remaining quantity in the same turn. The first acceptance to **reserve** the units wins, because the reservation is exclusive (TR-068); the second is rejected with `MKT-A10` ("the remaining quantity is already committed"). If both are submitted in the same request batch, the server serialises them by `submitted_at` then `action_id`; the loser is rejected, never partially filled. The listing's `quantity_locked` can never exceed `quantity_posted − quantity_filled`.

**MKT-123 — Failure releases exactly once.** *Provisional (ECN-125).* Every reservation has one release path. A P2 failure, a P4 failure, a cancellation or an expiry calls the same idempotent release, keyed by the reservation ID, so a retry cannot release twice. A release that would make a balance negative is a defect, not a rule.

**MKT-124 — Market-action rate limits.** *Provisional (D-024).* In addition to MKT-059's directed limits, a nation may hold at most **4 active sell listings and 4 active buy offers per resource** and at most **12 active listings in total**; it may submit at most **20 market actions** (post, execute, cancel) in any 12 consecutive turns; and at most **50 executions may be accepted for it in one turn**, which bounds its P4 work. There is no per-listing execution cap: a listing may be partially filled several times in one turn, and each fill is a separate execution. Each limit is visible on the board and returns a stable code (`MKT-L09`…`MKT-L12`).

**MKT-125 — Why the listing caps.** *Provisional; rationale recorded.* A public board is a shared reading surface. Four price steps per resource and twelve total let a player ladder a few prices without turning the board into one nation's shop; the number is set for readability and write cost, not copied from Politics & War's three-per-resource announcement (`PWR-024`). Prompt 14 may tune it.

**MKT-126 — Listing revisions are not supported.** *Provisional.* A listing cannot be edited. A seller who wants a different price or quantity cancels the remainder and posts a new listing. This keeps every execution priced against terms the taker actually saw, avoids a version race, and makes the history unambiguous. The cost is an extra listing row; the benefit is that a listing's terms never change under a taker.

---
## 15. Global listing reservations and settlement

**MKT-127 — Three reservations at an execution.** *Provisional.* When a taker executes a listing, the server creates or converts, in one transaction: (1) the **taker's side** — crowns for a sell listing, units for a buy offer; (2) the **maker's side** — the listing's existing reservation is split so that `x` units (sell) or `x × unit_price` crowns (buy) become *execution-locked* and the remainder stays *listing-reserved*; and (3) the **incoming space** on the nation that will receive the units. If any of the three cannot be created, the whole execution is rejected and the listing is unchanged.

**MKT-128 — Listing quantity and reservation identities.** *Provisional (F-TM-015…F-TM-018).* For every listing, at every boundary:

```
quantity_posted = quantity_filled + quantity_locked + quantity_remaining
```

and the maker's reservation is exactly:

```
sell listing:  reserved_units   = quantity_locked + quantity_remaining
buy offer:     reserved_crowns  = (quantity_locked + quantity_remaining) × unit_price
```

`quantity_locked` is the part under accepted, unsettled executions. `quantity_remaining` is what a new taker can still execute. `quantity_filled` is settled history. No rule may use `quantity_posted − quantity_filled` as "available": that figure includes the locked part and would over-advertise.

**MKT-129 — The execution acceptance order.** *Provisional.* The server checks, in this order: turn open; actor owns the nation; account/nation eligible; the listing is `OPEN` or `PARTIALLY_FILLED`; the actor is not the maker; the pair is not `RESTRICTED` or `MAINTAINED`; the actor's political state permits the action; `1 ≤ x ≤ quantity_remaining`; the taker can cover its side from **available** crowns/units; the receiver's `free_space` — already net of existing space reservations — covers `x`; the fresh-nation band, if it applies; the rate limits; the idempotency key. The first failure returns its code; nothing is reserved.

**MKT-130 — P2 re-validation of an execution.** *Provisional.* At P2 the engine re-checks the listing's existence and status, the maker's and taker's existence, both reservations, the space reservation, and the pair. It does not re-apply the political-state test (the execution was accepted while the state permitted it) and does not re-open the price. A listing that expired with a locked execution does **not** fail that execution: the locked part is already committed and settles. A listing that was administratively suspended after the execution was accepted also does not fail it, unless the suspension explicitly names accepted executions; the default is that suspension blocks new executions only.

**MKT-131 — P4 settlement of an execution.** *Provisional (ECN-211).* In one transaction: the taker pays `T = x × unit_price` crowns (sell) or delivers `x` units (buy); the maker delivers `x` units (sell) or pays `T` crowns (buy); the receiving nation's space reservation is consumed and the units are added; the giving nation's reservation is consumed and the units removed; `quantity_locked` falls by `x`, `quantity_filled` rises by `x`; the maker's remaining reservation is reduced by exactly the settled amount; and two ledger events with one `transfer_id` are written. The listing becomes `FILLED` when `remaining = 0` and `locked = 0`; otherwise it stays `OPEN` or `PARTIALLY_FILLED`.

**MKT-132 — Execution failure.** *Provisional.* A P2 or P4 failure of an execution releases **all three** reservations, moves nothing, returns `x` from `quantity_locked` to `quantity_remaining` if the listing is still `OPEN` or `PARTIALLY_FILLED`, and marks the execution `FAILED`. If the listing was cancelled or expired in the meantime, the units/crowns return to the maker's **available** balance, not to the closed listing. The taker sees the code; the maker sees "an execution failed and the remainder was released" without the taker's identity beyond what the maker already saw on the accepted execution.

**MKT-133 — Cancellation and execution race.** *Provisional.* Cancellation wins only over the **unlocked remainder**. An execution accepted before the cancellation holds its locked quantity and settles. A cancellation accepted before an execution causes the execution's `MKT-A10` rejection because `quantity_remaining` is zero. If both are submitted in the same batch, `submitted_at` then `action_id` decides; the loser fails cleanly. No race may produce a negative remaining quantity or a double release.

**MKT-134 — Expiry with locked executions.** *Provisional.* At `expires_turn`, the listing's `quantity_remaining` is released to the maker and the listing becomes `EXPIRED`. `quantity_locked` is untouched: its executions settle, and each settlement reduces the locked quantity. When the last locked execution resolves, the listing is closed. The board shows an expired listing as closed, not as available. A listing may not be extended; a maker who wants to continue posts a new listing.

**MKT-135 — The no-overcommit invariant.** *Provisional.* For every nation and every resource: `reserved_units ≤ total_units`; for crowns: `reserved_crowns ≤ total_crowns`; for warehouse space: `sum(space_reserved) ≤ W − total_inventory` at the moment of reservation, equivalently `free_space = W − total_inventory − space_reserved ≥ 0` (F-TM-025). These are checked at every reservation and again at P7. **No rule may add `space_reserved` back** when testing whether an incoming quantity fits: that would count the same capacity twice. A violation is a defect that fails the turn's invariant check, not a rule a player can trigger.

---

## 16. Pricing, rounding and reference prices

**MKT-136 — Unit-price representation.** *Provisional.* A price is an integer number of crowns per whole unit. A directed line may use `0` to express "no value claimed" (a gift component); a global listing or buy offer must use **at least 1**. There is no fractional price, no sub-crown unit and no floating-point display.

**MKT-137 — Total order value.** *Provisional (F-TM-010/F-TM-021).* A total is `quantity × unit_price`, computed with a checked multiply. There is no division and therefore no rounding in a total. A display may group thousands with separators; it may not round the number.

**MKT-138 — Where rounding exists.** *Provisional (F-EC-000b).* Rounding appears only in a derived **rate**: a published average, a percentage or a fair-value bound. Every such formula states `floor` or `ceil`. The default is `floor`. A published average is `floor(Σ value / Σ quantity)`; a fair-value bound is `floor(V_low × (10,000 + B) / 10,000)`.

**MKT-139 — Reference prices are B-04's, unchanged.** *Approved constraint (ECN-027; D-058).*

| Resource | Book value (crowns/unit) | Resource | Book value (crowns/unit) |
|---|---|---|---|
| Food | 1 | Uranium | 30 |
| Coal | 1 | Gasoline | 6 |
| Oil | 2 | Steel | 7 |
| Iron | 1 | Aluminum | 8 |
| Bauxite | 2 | Ammunition | 6 |
| Lead | 3 | | |

This table is a copy for readability. If it ever disagrees with [the B-04 register §3.5](10_economic_formula_and_balance_register.md), the register wins and this table is corrected. The prices are **book values**, not market prices, floors or ceilings.

**MKT-140 — The three price labels.** *Provisional.* A listing shows its asking or buy price; a completed trade shows its executed price; a report shows the reference price. The words are fixed: **"asking price"**, **"offer price"**, **"completed price"**, **"book value"**. "Market price" is not used for any of them, because none is a market-wide price. A statistic is labelled with its window and sample or it is not shown.

**MKT-141 — Safe arithmetic bounds.** *Provisional (F-TM-031/F-TM-032).* `MAX_TRADE_UNITS_PER_LINE = 100,000`; `MAX_TRADE_CROWNS = 10,000,000`; `MAX_UNIT_PRICE = 100,000`; the signed 64-bit maximum is the hard ceiling. Every multiply checks `a ≤ MAX_I64 / b` before computing `a × b`; a failed check rejects the action with `MKT-E11` and is never wrapped, clamped or silently truncated. The largest legal directed total is `10,000,000 + 5 × 100,000 × 100,000 = 50,010,000,000`, which is far below `9.22 × 10^18`; the bound exists to keep the rule explicit, not because the product is near the ceiling.

**MKT-142 — No price floor or ceiling on the trade itself.** *Provisional.* The market does not fix a minimum or maximum price for a resource. A player may ask 1 crown or 100,000 crowns for uranium; the board shows the price and the book value, and the fair-value rule governs who may execute it (§17). A price control would contradict the "production first, trade second" philosophy (D-043) and the research's finding that the reference game describes itself as laissez-faire (`PWR-028`) without Nation Supremacy having to copy that label.

**MKT-143 — No price history at first playable.** *Approved constraint (D-017).* At first playable there is no public price history, no index, no average and no per-trade public record. A party sees its own completed trades. Any published statistic is a gate-stage feature (§23) and requires the gate, the sample rule and the suppression rule.

---

## 17. Fair value and fresh-nation protection

**MKT-144 — The band is a ratio on reference value.** *Provisional; Prompt 07 owns it (ECN-208; ONB-032).* The fair-value band is `B = 3,000` basis points (30%), applied as a **ratio** between the two sides' reference values:

```
in_band  ⇔  V_high ≤ floor(V_low × (10,000 + B) / 10,000)
```

with `V_low = min(V_A, V_B)` and `V_high = max(V_A, V_B)`. The pair is normalized **by value**, not by which nation proposed, so reversing the parties cannot change the verdict; `V_low = 0` on exactly one side is `ONE_SIDED`, and both sides at zero is invalid (MKT-146). The comparison is inclusive at the boundary: a pair at exactly 1.30 passes.

**MKT-145 — Why a ratio, and why 30%.** *Provisional; rationale recorded.* The ratio is scale-free: it asks "is the larger side at most 30% bigger than the smaller?" and gives the same answer for a 10-unit trade and a 10,000-unit trade. It is **not symmetric in percentage terms** and must never be described as a `±30%` band. At a ratio of 1.30 the larger side is 130% of the smaller, so the smaller is 76.92% of the larger, not 70%. Equivalently, a 30% premium passes while a 30% discount from the larger side fails: `100 vs 70` has a bound of `floor(70 × 1.30) = 91`, so 100 is out of band, whereas `100 vs 130` is in band. The interface reports `ratio_bp` and says "the larger side is X% bigger" (F-TM-007); it does not print a plus-or-minus range. At first playable the only stable anchor is the book value, and the rule is stated once, as this ratio. 07A found a ±30% band in Politics & War applied to new and flagged nations (`PWR-016`); the structure is borrowed as a **shape**, not as a validated value. `B = 3,000` is provisional and Prompt 14 must test it (§30, UD-037).

**MKT-146 — Four fair-value statuses.** *Provisional (F-TM-006).*

| Status | Condition | Fresh-nation effect | Mature-nation effect |
|---|---|---|---|
| `IN_BAND` | Both sides have `V ≥ 1` and the bound holds | Allowed | Allowed, no signal |
| `OUT_OF_BAND` | Both sides have `V ≥ 1` and the bound fails | **Rejected** (`MKT-E08`) | Allowed; signal `MKT-S01` recorded |
| `ONE_SIDED_SEND` | `V_low = 0` and the fresh nation is the **giving** side | **Rejected** (`MKT-E09`) | Allowed; signal `MKT-S02` recorded |
| `ONE_SIDED_RECEIVE` | `V_low = 0` and the fresh nation is the **receiving** side | Allowed; signal `MKT-S03` recorded | Allowed; signal `MKT-S03` recorded |

A trade with both sides at zero is invalid (`MKT-E01`), not one-sided.

**MKT-147 — The fresh window.** *Provisional (ONB-031/ONB-032).* A nation is **fresh** while

```
current_turn − nation_created_turn < 360
```

i.e. for its first **360 turns (30 days at 12 turns/day)**. `nation_created_turn` is the turn in which the nation became `active`, not the account's registration turn. A replacement nation from a reroll receives a new `nation_created_turn` and therefore a new 360-turn window (ONB-033); this is not a repeatable bonus, because every new nation receives it and it grants nothing except the protection rule.

**MKT-148 — What the fresh rule blocks.** *Provisional.* A fresh nation may not:

1. send a one-sided transfer to another account (`ONE_SIDED_SEND`);
2. execute or accept a directed trade outside the band, in **either** direction;
3. execute a global listing whose price is outside the band against the resource's book value, in **either** direction;
4. post a global listing whose price is outside the band, because the only reason to post it is to execute it with someone.

It **may**: trade reciprocally in band; buy or sell at an in-band price; receive a one-sided gift (recorded as `MKT-S03`); negotiate, decline and cancel; and read the whole market.

**MKT-149 — Why receiving is allowed but recorded.** *Provisional; residual risk disclosed.* The harm the window targets is converting the standard starting bundle into a transfer to another account (ONB-032). A fresh nation **sending** value is the direct route; a fresh nation **receiving** value is not a route out of its own bundle, and banning receipt would punish a legitimate gift to a new player. The residual route — a mature account funds a fresh account, which later funnels value back after the window — is **not mechanically prevented** by this rule; it is a transfer-graph review signal (D-035) and a Prompt 12 concern. This document does not claim the route is closed.

**MKT-150 — Where the check runs.** *Provisional.* The fair-value check runs at: directed offer **creation**; directed **acceptance**; global listing **posting** (the poster's own side against book value); global **execution acceptance** (both parties); and P2, using the verdict recorded at acceptance. A trade that was in band when accepted is not retroactively failed because a reference price changed later in the same turn; reference prices are constants, so this is a completeness rule, not an expected event.

**MKT-151 — Age can change between creation and acceptance.** *Provisional.* If the proposer was fresh at creation but is no longer fresh at acceptance, the acceptance is evaluated on the **acceptance-time** age. If the recipient was fresh at creation and is still fresh at acceptance, the acceptance-time rule applies. A trade created while both were mature can become restricted if one party's nation is replaced by a reroll before acceptance; the replacement is a different nation with a new creation turn, and the acceptance re-check sees it.

**MKT-152 — Rerolls and replacement nations.** *Provisional (D-039).* A reroll destroys open offers and any accepted-but-unsettled trade blocks the reroll (MKT-050). A replacement nation is fresh from its own creation turn. A pair restriction survives the reroll, so a replacement cannot trade with the same restricted counterparty. The band applies to the replacement exactly as to any new nation; it is not waived because the account is old.

**MKT-153 — Counterparties at different ages.** *Provisional.* If **either** party is fresh, the whole trade must be in band. A mature nation cannot use a fresh nation's inexperience to extract value, and a fresh nation cannot use its window to extract value from a mature one. The rule is symmetric because the band compares the two sides, not the two ages.

**MKT-154 — Listings and the window.** *Provisional.* A listing posted while the maker was fresh remains visible if the maker later becomes mature; the execution check uses the **execution-time** ages. A listing posted by a mature nation can be executed by a fresh taker only if the price is in band. A listing that was in band at posting can become out of band only if the book value changes, which it does not within a turn; the practical case is a listing posted out of band by a mature nation and executed by a fresh nation, which is blocked at execution.

**MKT-155 — A legitimate unusual trade is not cheating.** *Provisional.* For a mature nation, an out-of-band trade is **allowed** and produces a review signal, a neutral confirmation and an audit record. It does not produce a public accusation, a score penalty, a trade ban, a confiscation or an automatic suspension. Price alone never proves manipulation; a player may genuinely value a resource differently, may be helping an ally, or may be completing a deal negotiated elsewhere. The signal exists so that a pattern can be reviewed, not so that a single trade can be punished.

**MKT-156 — The band is not a tax and not a fee.** *Provisional.* No value is transferred, charged or withheld because a trade is in or out of band. The band decides **whether a protected nation may trade** and **whether a mature trade is reviewed**; it never moves a crown. A future fee is a separate G-5 decision (MKT-070).

---

## 18. Manipulation signals and review

**MKT-157 — What the market records as a signal.** *Provisional.* The following are recorded as `MKT-S` signals with the trade or listing ID, the parties, the turn and the measured values. A signal is **evidence for review**, not a finding:

| Signal | What is measured | Why it is recorded |
|---|---|---|
| `MKT-S01` | A mature trade outside the fair-value band | A large value asymmetry may be legitimate; a pattern is not |
| `MKT-S02` | A mature one-sided send | A gift is allowed; a repeated funnel is not |
| `MKT-S03` | A one-sided receive by a fresh nation | The residual route in MKT-149 |
| `MKT-S04` | Two accounts trading repeatedly at the same price and quantity | Possible wash or reciprocal transfer |
| `MKT-S05` | A listing cancelled and reposted at the same price within 3 turns | Possible board spam or price signalling |
| `MKT-S06` | A trade between accounts with a shared-network observation | The pair matrix should already block it; a signal means a detection gap |
| `MKT-S07` | A price more than 10× the book value, or less than one tenth | Extreme outlier; not automatically wrong |
| `MKT-S08` | One nation accounting for more than 50% of a resource's completed volume in a 12-turn window | Concentration worth watching, not a violation |
| `MKT-S09` | A fresh nation's first completed trade is out of band | Should be impossible; a signal here indicates a rule gap |
| `MKT-S10` | A completed trade whose ledger pair fails the conservation identity | A defect, not a player act; pages the operator |

**MKT-158 — The thresholds are diagnostic, not legal.** *Provisional.* `MKT-S07`'s 10× and `MKT-S08`'s 50% are **triage** values, not rules a player can breach. They are provisional and Prompt 14 may tune them. No signal alone triggers a sanction.

**MKT-159 — Cartels are allowed; price-fixing is expensive, not impossible.** *Provisional (ECN-191).* A group may buy up a resource, post high asks, or coordinate its listings. That is a legitimate market strategy. It cannot force a sale, every other nation can build the same capacity, and the board shows the book value next to the ask so a buyer can see the premium. The design does not attempt to make cartels impossible; it makes them expensive and contestable. A cartel that uses multiple accounts or a restricted pair to coordinate is caught by the account and pair rules, not by a price rule.

**MKT-160 — Review, not punishment, at the market layer.** *Provisional.* A signal opens a **review item** for Prompt 12's process. The market layer may suspend a listing (MKT-089) while a review is open, but it may not ban an account, delete history, confiscate units, reverse a settled trade or publish the reason. Those are administrative acts with their own decision, evidence standard and appeal (D-042); the market supplies evidence and a narrow suspension, nothing more.

**MKT-161 — No automatic permanent ban, no silent confiscation.** *Provisional.* A market rule may reject an action, record a signal and suspend a listing. It may not permanently ban an account, remove a nation, or transfer value to the operator or another player. A settled trade is final unless a privileged reversal is recorded with a reason and an appeal path (B-04's `REVERSAL` event); a market signal alone is not sufficient reason for a reversal.

**MKT-162 — Evidence retention.** *Provisional (D-026; D-042).* A signal record keeps the identifiers, the values, the turn and the rule version for **12 months** (class O), unless an open case requires longer. It does not keep raw IP addresses, session tokens or private messages. A closed case's evidence follows Prompt 12's retention rule. The permanent audit spine keeps the value mutations and the privileged acts, not the analyser's notes.

---
## 19. Treasury, inventory, atomicity and accounting

**MKT-163 — A directed trade's value flow.** *Provisional.* For a trade where A gives `crowns_A` and lines `L_A`, and B gives `crowns_B` and lines `L_B`:

| Nation | crowns delta | resource delta | space delta |
|---|---|---|---|
| A | `−crowns_A + crowns_B` | `−L_A + L_B` | `−units(L_A) + units(L_B)` |
| B | `−crowns_B + crowns_A` | `−L_B + L_A` | `−units(L_B) + units(L_A)` |

The crown deltas sum to zero; each resource's deltas sum to zero; each nation's net space change is the difference between what it gives and receives, and the **receiving** direction must fit under its space reservation. If both sides give the same resource, the deltas are netted for the ledger but the reservation is on the gross incoming quantity, because the units physically enter and leave.

**MKT-164 — A global execution's value flow.** *Provisional.* For a sell listing at `p` with `x` units:

| Nation | crowns delta | resource delta |
|---|---|---|
| Seller | `+x × p` | `−x` |
| Buyer | `−x × p` | `+x` |

For a buy offer the signs reverse. The fee is zero (MKT-068); if a future fee exists, it is a third row `FEE` with the declared payer and the conservation identity becomes `Σ crown deltas + fee = 0`, never `Σ crown deltas = 0` silently broken.

**MKT-165 — Ledger events.** *Provisional (ECN-165; ECN-211).* Each side writes one event with the shared `transfer_id`:

For a **simple one-resource sale**, each side writes one event:

| Side | Event | Amount |
|---|---|---|
| Buyer of resources | `TRADE_BUY` | `−total_crowns`, `+units` |
| Seller of resources | `TRADE_SELL` | `+total_crowns`, `−units` |

For a **bundle or a barter**, a side that both gives and receives writes **two** events — a `TRADE_SELL` for what it gave and a `TRADE_BUY` for what it received — and all events in the trade share one `transfer_id`. The crown amounts across the whole set must sum to zero; each resource's amounts must sum to zero. A side that gives and receives the same resource writes the net quantity on its two events, but the **reservations** are on the gross incoming and outgoing quantities, because the units physically enter and leave.

A crown payment is recorded once: on the payer's `TRADE_BUY` event for the goods it acquires and on the payee's `TRADE_SELL` event for those goods; the opposite leg of a bundle carries `0` crowns. A single payment must never appear with both signs on the same side's two events (E1). Each event carries the resource lines, the unit prices, the listing or offer ID, the counterparty nation ID and the turn. The set is written in the same transaction; a missing half is a defect (`MKT-S10`), not a state to repair by guessing.

**MKT-166 — Conservation identities.** *Provisional.* At P7, for every market transaction:

1. `Σ crowns_delta = 0` (or `+ fee = 0` when a fee is enabled);
2. for each resource, `Σ units_delta = 0`;
3. `total_crowns` never negative for either nation;
4. `total_units(resource)` never negative;
5. `0 ≤ total_inventory ≤ W` for both nations;
6. `reserved ≤ total` for every reserved quantity;
7. the two ledger rows share exactly one `transfer_id` and one turn.

A failure of any identity makes the transaction fail atomically; it does not publish a partial result.

**MKT-167 — No minting, no burning.** *Provisional (ECN-099; ECN-211).* A trade creates no crown and no resource. It moves them. The only exception is an explicitly approved future fee, which destroys or redirects the fee amount by a declared rule and writes `FEE`. At launch there is no fee, so the strict identity holds.

**MKT-168 — Reservation release is idempotent.** *Provisional.* Every release is keyed by the reservation ID and records the release event once. A retry of the same P2/P4 failure, a duplicate cancellation, or a boundary replay cannot release twice. The three releases — resolution, failure, cancellation/expiry — all call the same operation and all write the same event type.

**MKT-169 — Duplicate execution requests.** *Provisional (TR-057; `F9`).* Every market action carries an idempotency key. A duplicate key returns the original receipt and the original state; it does not create a second execution, a second reservation or a second ledger row. A different key with the same terms is a **new** action and is subject to the available quantity; if the listing is exhausted, it fails with `MKT-A10`.

**MKT-170 — A failed trade leaves both sides unchanged.** *Provisional (TR-056).* At P2 or P4 failure: crowns, resources, space and listing quantities return to their pre-acceptance values; the reservations are released; the only lasting records are the failure event and the action record. A failed trade never leaves a half-moved balance, a stuck lock or a "pending forever" row.

**MKT-171 — Reconciliation query.** *Provisional (Stage 5 implements).* The operator can reconstruct, for any turn: the accepted market actions, their reservations, their settlements, their release events, the ledger pairs and the listing quantity identity. The reconstruction uses only the permanent audit spine and the class-P records; it does not depend on a mutable cache. A market transaction that cannot be reconstructed from these records is a defect.

**MKT-172 — No retroactive repricing.** *Provisional.* A settled trade's price, quantity and ledger rows are permanent. A later reference-price change, a balance patch or a market redesign does not rewrite them. A correction, if ever needed, is a new `REVERSAL`/`ADJUSTMENT` event with a reason, an author and an appeal path — never a silent update.

---

## 20. Turn timing and settlement reconciliation

**MKT-173 — The ten steps of a market action.** *Provisional.* Every value-moving market action follows this sequence; the numbering is the contract.

| # | Step | What happens | What is visible |
|---|---|---|---|
| 1 | **Submission** | The client sends the action with an idempotency key | "Submitting" |
| 2 | **Acceptance or matching** | The server validates, reserves and marks the action accepted | "Accepted for Turn N; settles at close" |
| 3 | **Eligibility checks** | Account, nation, pair, political state, limits | A rejection code if any fails |
| 4 | **Reservation or commitment** | Crowns, units and space are held | Total / reserved / available |
| 5 | **P2 validation** | The frozen snapshot is re-checked; failures release | "Failed at validation: <code>" |
| 6 | **P4 settlement** | Both legs apply atomically; ledger pair written | "Settled at Turn N" |
| 7 | **Success publication** | P7 digest line and the parties' history | The receipt and the new balances |
| 8 | **Failure handling** | Release, state `FAILED`, code, digest | "Failed: <code>; nothing moved" |
| 9 | **Reservation release** | Idempotent, exactly once | The reserved figure falls |
| 10 | **Recovery after interruption** | The same frozen input is replayed; `F8` retries the action with the turn | "Recovering Turn N" |

**MKT-174 — Trade settlement is inside P4, after P3.** *Provisional (TR-040; ECN-211).* A trade accepted in the open window is evaluated against the frozen state at `LOCKED`, after P3's production and obligations. It cannot rescue a P3 production shortage (the inputs arrive at P4) and cannot change a P3 tax or food result. The interface says: "Arrives after this turn's production; available from the next turn."

**MKT-175 — The boundary assignment.** *Provisional (TR-035/TR-036).* A market action submitted before `LOCKED` belongs to the current turn; at or after `LOCKED` it belongs to the next. The client shows the assigned turn before confirmation. A late click is a next-turn action, never a lost action and never a silent re-price.

**MKT-176 — Counterparty ineligibility after acceptance.** *Provisional.* If a counterparty becomes ineligible (suspended, removed, nation retired, pair restricted) between acceptance and P2, the trade fails at P2 with `F3` and both sides are released. If the ineligibility is a **leadership state** (`TRANSITION`/`CRISIS`), the trade does **not** fail (MKT-051): the state restricts new actions, not an already-accepted settlement. If the counterparty rerolls, D-039 blocks the reroll while an accepted trade is unsettled, so this case should not arise; if it does through an operational error, the trade fails cleanly with `F3` and nothing moves.

**MKT-177 — Cancellation, expiry and execution races.** *Provisional.* The general rule is: a reservation is exclusive, so the first action to reserve wins; every later action fails cleanly with a specific code. A cancellation of an unaccepted directed offer is immediate. A cancellation of a listing affects only the unlocked remainder. An expiry affects only the unlocked remainder. An execution that has already reserved cannot be cancelled by the maker. No race may produce a negative balance, a double release or a listing whose parts exceed its whole.

**MKT-178 — Interrupted resolution.** *Provisional (TR-043; TR-038).* If P4 is interrupted after some trades settled, recovery resumes from the P4 checkpoint with the same frozen snapshot and the same ordering. A trade that settled writes its ledger pair once; a trade that did not settle is retried. The turn is never published with half a trade. A duplicate settlement is prevented by the action state and the idempotency key, not by hoping the retry is not reached.

---

## 21. Eligibility, account integrity and political restrictions

**MKT-179 — The checks at each point.** *Provisional (D-034; NET-029).*

| Check | Directed creation | Directed acceptance | Listing posting | Execution acceptance | P2 | P4 |
|---|---|---|---|---|---|---|
| Account is eligible | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Nation is active and not unavailable | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Pair is not `RESTRICTED`/`MAINTAINED` | ✔ | ✔ | — (no named counterparty) | ✔ | ✔ | ✔ |
| Political state permits new actions | ✔ | ✔ | ✔ | ✔ | — (acceptance verdict) | — |
| Fresh-nation band | ✔ | ✔ | ✔ (own price) | ✔ | Verdict from acceptance | — |
| Limits and rate | ✔ | ✔ | ✔ | ✔ | — | — |
| Balance/space available | — | ✔ | ✔ | ✔ | ✔ | ✔ |

A check that is not applicable is shown as `—`, not skipped silently. A **new** pair restriction discovered at P2 fails the trade; a political state that begins after acceptance does not.

**MKT-180 — The pair check is before reservation.** *Provisional (D-034 row 4; NET-029).* A restricted pair cannot create, accept, execute, settle or match a market action. The blocked action moves nothing, receives `MKT-A05`, and is recorded as an event. The counterparty is not told which account is restricted; the blocked player is told only "interactions with this account are restricted", with the review route.

**MKT-181 — Public participation stays open.** *Provisional (NET-028).* A restricted account may still post a **public** listing and may trade with unrelated accounts (D-034 row 19). It may not use the public board to reach its paired account, and it may not use a third account to route value to it (D-035). The market does not hide the whole board from a restricted player; it blocks the specific pair.

**MKT-182 — No parallel identity system.** *Provisional (D-031; D-032).* The market reads the account, nation and pair states that B-03 owns. It does not create a market-specific "trust score", a "verified trader" badge, a separate ban list or a hidden reputation. A player-facing market status is a view of the existing states, never a fourth state.

**MKT-183 — Shared network is not proof.** *Provisional (D-034; D-037).* Two accounts on one network are not cheaters. The pair state is a restriction on interaction, with a review route (D-033); the market applies the restriction and never publishes the reason or treats the pair as guilty. A `LARGE` network (more than 25 accounts in 24 hours) is not blanket-restricted, and the market must not infer abuse from the network alone.

**MKT-184 — Sanctions survive a reroll.** *Provisional (D-039).* A suspended or banned account cannot trade, including through a replacement nation. A pair restriction survives the reroll. A market ban is not a thing the market can impose; it is an account measure owned by Prompt 12. A reroll never clears a sanction, a review or an evidence record.

**MKT-185 — Political states and the market.** *Approved constraint (DMP-262).* `TRANSITION` and `CRISIS` are read-only for new market actions. The market remains readable. Already-accepted trades settle. `NORMAL`, `ELECTORAL`, `SUCCESSION` and `RECOVERY` do not restrict market actions; the election campaign has its own action rules (B-06) and this document does not add a political fee, tariff, embargo or stability penalty. A diplomacy or war restriction (Prompt 08/10) is a separate rule and may not be implemented as a market fee.

---

## 22. Privacy, history and retention

**MKT-186 — Directed terms are parties-only.** *Approved constraint (D-017).* A directed offer, its lines, its revisions, its decline reason and its failure code are visible to the two parties and to restricted administrative audit. A third party cannot see that the chain exists, cannot see its terms and cannot infer it from a public list. A settlement's ledger rows are visible to the owning nation and to audit; they are not public.

**MKT-187 — Global listings are public by design.** *Provisional; gate-stage.* An **open** global listing is public: resource, remaining quantity, unit price, total, created/expiry turns and the maker's public nation name and number. This is the listing's purpose. It does not expose the maker's treasury, warehouse, other listings, account, network, sanction or review state.

**MKT-188 — Completed global trades are not a public per-trade feed.** *Provisional.* A completed global trade's **existence and price** are visible to its two parties and to audit. The board may show an **aggregate** statistic (§23) after the gate; it does not publish "Nation A sold 200 steel to Nation B at 8" to the world. This deliberately differs from the reference game's public per-nation trade history (`PWR-013`) and honours D-017's confidentiality posture. The listing's remaining quantity changing is an unavoidable public signal that *someone* executed; the counterparty's identity is not published.

**MKT-189 — Personal history.** *Provisional.* Each nation has a permanent, paginated **trade history** of its own: directed offers sent/received (with status), global listings posted, executions made and received, settlements, failures and releases. It shows the counterparty for a completed trade (the party already knows it), the price, the quantity, the turn and the `transfer_id`. It is visible only to the owning account and to audit. It is class P (permanent) for completed trades and class S for operational noise.

**MKT-190 — Retention classes.** *Provisional (D-026).*

| Record | Class | Retention |
|---|---|---|
| Completed trade (both ledger rows, price, quantity, parties) | **P** | Permanent — the audit spine |
| Listing / offer object after terminal state | **S** | Hot 30 days, then summarised into the nation's monthly summary; the completed trade remains P |
| Reservation and release rows | **S** | Hot 30 days; the settlement row references them; summaries keep totals |
| Failure and rejection events | **S** | Hot 30 days, then summarised; a repeated-failure counter is kept with the offer |
| Manipulation signal | **O** | 12 months, or longer if a case is open |
| Enforcement note and evidence | **O** | 12 months floor; open case longer (D-042) |
| Published statistic | **P** (aggregate) | The statistic and its method; the underlying trades are not republished |
| Idempotency key | **S** | Hot 30 days; the settled action's key is retained with the action |

**MKT-191 — Compaction never breaks a settlement.** *Provisional (D-026).* The daily compaction job may replace an old offer/listing row with a summary, but it may not delete a completed trade's ledger pair, its `transfer_id`, its price or its quantity. A compacted offer keeps its terminal status and its link to the settlement. A replay after compaction must still find the settlement evidence.

**MKT-192 — No personal data in the market.** *Provisional (D-042).* The market stores no raw IP, no e-mail, no real name, no payment data and no session token. The network key is a digest held by B-03's restricted table; the market reads the pair state, not the key. A listing shows a public nation label, never an account identifier.

**MKT-193 — Administrative read is logged.** *Provisional (D-042).* A privileged read of directed terms, a listing's suspension reason or an enforcement signal is logged with the actor, the reason and the time. An administrator may not silently edit a public listing, a price or a history row.

**MKT-194 — Deletion and account closure.** *Provisional.* On account closure, the account's private market records are deleted or anonymised per D-042, while the permanent audit spine keeps the value-mutation records required for conservation. A completed trade with another nation is not deleted from the **other** nation's history; the closed nation's identity is replaced by a neutral "closed account" label where the other party's record needs it.

---

## 23. Published market statistics

**MKT-195 — No statistic at first playable.** *Approved constraint (D-017).* Until Global Trade passes G-1…G-6, no market statistic is public. A player sees their own history and the book values; nothing else. This is not a temporary oversight and may not be relaxed by a UI convenience.

**MKT-196 — What a post-gate statistic may be.** *Provisional.* After the gate, the market may publish, per resource, a **24-hour completed-trade average** and a **24-hour volume band**, plus the **best current ask/bid** from live listings. The best ask/bid is not an aggregate over people; it is a live listing, and it is labelled as such. The average is an aggregate and must pass MKT-197.

**MKT-197 — The sample rule.** *Provisional (D-027; k = 5).* A statistic is published only when the window contains:

- at least **5 completed trades**; **and**
- at least **5 distinct participating nations** (the union of buyers and sellers);
- otherwise the state is `INSUFFICIENT_SAMPLE` and no number is shown.

The 5-nation condition is the k = 5 aggregate rule applied to the market: a "market average" computed from two accounts is not a market, and publishing it would reveal their trades. When either condition fails, the state is `INSUFFICIENT_SAMPLE`: the market shows "not enough trades to publish" and suppresses the count as well, because a count of two trades plus the two nations' public listings would identify them.

**MKT-198 — Computation.** *Provisional (F-TM-028).* For a qualifying window:

```
VWAP = floor( Σ (quantity_i × price_i) / Σ quantity_i )
```

over completed trades in the window, with every trade weighted by its quantity. The volume band is `floor(Σ quantity / 10) × 10` (nearest lower 10 units) so that a small change cannot be differenced out of the published total. The window is the **last 12 turns** ending at the current turn, inclusive; it is a rolling window, not a calendar day, because the game has no calendar day boundary.

**MKT-199 — Complementary suppression.** *Provisional (D-027).* If publishing the total volume and all but one resource's volume would reveal the suppressed resource, at least one further resource is suppressed. If a total plus a subset would reveal a single trade or a single nation's activity, the subset is coarsened or withheld. The rule is applied by the statistic job, not left to the UI.

**MKT-200 — What the statistic is not.** *Provisional.* It is not a price floor, a ceiling, a settlement price, a guarantee or a valuation. It is a **backward-looking** average of completed trades over a stated window and sample. The label says "24-hour average of completed trades; N trades; M nations; book value X". A player who reads it as a quote has been misled by the interface, which is a defect.

**MKT-201 — Manipulation resistance is partial.** *Provisional.* Self-trade is blocked (MKT-097) and a restricted pair cannot wash (MKT-098), but a group can still trade among unrelated accounts at a chosen price to move the average. The statistic resists this only by requiring five distinct nations, by using a quantity-weighted mean, by publishing the sample and by flagging `MKT-S08`. The design does not claim the average is manipulation-proof; G-4 exists because it is not.

**MKT-202 — Statistics are computed off the turn path.** *Provisional (free-first).* The statistic job runs as an idempotent daily maintenance job, not inside P4. It reads the completed trades for the window, computes, applies suppression and writes one row per resource per day. A failure of the job leaves yesterday's statistic in place with its date; it never publishes a partial or zero value.

**MKT-203 — No per-nation public volume ranking.** *Provisional.* The market does not publish "top traders" or a per-nation volume leaderboard. That is a ranking feature owned by Prompt 11, and if it exists it must pass D-027 and must not be derived from private directed trades. A player's own volume is in their history.

---
## 24. The declared limits (D-024 contract)

**MKT-204 — Every limit in one place.** *Provisional.* This is the B-02 §24 declaration for the market. Each row is server-enforced, visible before submission, and returns its code. The values are provisional; Prompt 14 tunes them by register revision.

| Code | Limit | Value | Unit, scope and period | Why it exists |
|---|---|---|---|---|
| `MKT-L01` | Active outgoing directed chains | 5 | Chains in `ACTIVE`/`COUNTERED` per nation, rolling | Prevents offer spam without limiting relationships to one |
| `MKT-L02` | Chains per counterparty | 1 | Live chains per nation pair, rolling | Forces one negotiation per relationship |
| `MKT-L03` | Revisions per chain | 10 | Counteroffers per `chain_id` | Bounds negotiation and rows |
| `MKT-L04` | Resource lines per side | 5 | Lines per side | A bundle stays legible |
| `MKT-L05` | Quantity per line | 100,000 | Units per line | Above any warehouse; bounds arithmetic |
| `MKT-L06` | Crowns per side | 10,000,000 | Crowns per side | Keeps arithmetic far inside 64-bit |
| `MKT-L07` | Directed market actions | 20 | Per nation per 12 consecutive turns | Bounds writes and notifications |
| `MKT-L08` | Available inventory for a listing | The offered quantity | Per resource, at posting | A listing must be backed |
| `MKT-L09` | Active sell listings per resource | 4 | Per nation per resource | Readability and board fairness |
| `MKT-L10` | Active buy offers per resource | 4 | Per nation per resource | Same |
| `MKT-L11` | Active listings in total | 12 | Per nation | Bounds a single nation's share of the board |
| `MKT-L12` | Market actions | 20 | Per nation per 12 consecutive turns (post, execute, cancel) | Bounds the write rate |
| `MKT-L13` | Accepted executions per nation per turn | 50 | Per nation per turn | Bounds P4 work |
| `MKT-L14` | Accepted executions world-wide per turn | 5,000 (provisional operational guard) | Per turn | Keeps a boundary inside its two-hour window on the free tier |
| `MKT-L15` | Directed offer expiry | 72 turns | From the last revision | Prevents stale pledges |
| `MKT-L16` | Listing expiry | 72 turns | From posting | Same, for the public board |
| `MKT-L17` | Failed acceptances before `STALE` expiry | 3 | Per chain, reset by a counteroffer | Removes an unbacked offer |

**MKT-205 — `MKT-L14` is an operational guard, not a game rule.** *Provisional.* If a turn's accepted-execution count reaches 5,000, further execution acceptances are refused with `MKT-L14` ("settlement capacity for this turn is full; try the next turn") until the next window. The number is a placeholder for the capacity Stage 3 measures; it must be set from the measured boundary time, not guessed. A refusal happens **before** reservation, so no player is left with a locked trade that cannot settle. This is the only market limit that exists for infrastructure rather than design reasons, and it is disclosed as such.

**MKT-206 — Limits never depend on presence.** *Provisional.* No limit rewards being online at the boundary, no limit is a per-click budget and no limit resets on a local clock. All windows are turn-based. A player who checks once a day sees the same limits as one who checks every hour.

**MKT-207 — A limit rejection is free.** *Provisional (NET-029).* A rejected market action reserves nothing, moves nothing and counts against the rate limit only when the limit itself is the reason (a rejected action does not consume the 20-action window; otherwise a player could be locked out by failed attempts). The interface shows the remaining allowance before submission.

---

## 25. Free-first feasibility

**MKT-208 — What this section is and is not.** *Provisional.* It estimates the **logical** work a market action creates, so Stage 3 can measure it. It is not a measurement, not a benchmark and not a claim that the free tier is sufficient. The approved provider direction is Cloudflare Pages plus Supabase PostgreSQL/Auth/RLS with `pg_cron` as the single scheduler (D-008); this document does not change it and does not extend the Stage 1 prototype.

**MKT-209 — Write estimate per action.** *Provisional; a design estimate, not a measurement.*

| Action | Rows written (estimate) | Notes |
|---|---|---|
| Create a directed offer | 3–4 | Offer, revision, action, audit |
| Counter a directed offer | 3 | New revision, previous-revision status, action |
| Accept a directed offer | 8–14 | Action, offer status, up to 5 crown/resource reservations per side, up to 2 space reservations |
| Settle a directed trade | 7–10 | 2–4 ledger events, reservation closures, trade row, `transfer_id`, offer status |
| Fail a directed trade | 3–5 | Release per reservation, action status, event |
| Post a listing | 3 | Listing, reservation, action |
| Execute a listing | 4–6 | Execution, taker reservation, listing locked/remaining update, action |
| Settle an execution | 6–8 | 2 ledger rows, 2–3 reservation closures, execution status, listing update |
| Cancel a listing | 2–3 | Listing status, release, action |
| Expire a listing or offer | 1–2 | Status plus release; batched at the boundary |

**MKT-210 — Per-turn bound.** *Provisional.* The market's P4 work is bounded by `MKT-L13` per nation and `MKT-L14` world-wide. Expiry is a B0 maintenance pass over listings whose `expires_turn` equals the current turn, not a scan of all history. The statistic job is daily and off the turn path. There is no per-request market poller, no continuous matcher and no subscription.

**MKT-211 — Read pattern.** *Provisional.* A board page reads one page of listings (≤ 50), the best ask and bid per resource from an indexed view, and the player's own balances. It does not read the whole book, another nation's history or the audit spine. The directed screen reads the player's chains (≤ 50 per page). A per-nation read counter is included in the Stage 3 measurement.

**MKT-212 — Duplicated-history risks.** *Provisional.* Three are identified and prohibited: (1) a per-turn copy of every open listing into a history table; (2) a settlement row that repeats the full ledger payload; (3) a "market events" feed that duplicates the digest. The listing's own state is the history of its remaining quantity; the ledger pair is the history of the value movement; the digest line is the player-facing summary. One fact, one row.

**MKT-213 — What Stage 3 must measure.** *Provisional.* (a) writes per action at the real schema, (b) the P4 time with 5,000 executions, (c) the board read time with 1,000 open listings, (d) the expiry pass time with a full year of listings, (e) the statistic job time, (f) the storage after 12 months under D-026, and (g) whether `MKT-L14` can be raised or must be lowered. Until then, no claim of free-tier feasibility is made.

---

## 26. Failure scenarios

**MKT-214 — The failure contract.** *Provisional.* For every scenario below: the **state** column gives the final chain/listing state; **value** says whether anything moved; **release** says what was released; **player** is the visible outcome; **audit** is what is retained. "Nothing" means no crown, resource or space moved and no ledger row was written. All codes are stable.

### 26.1 Directed trades

| # | Scenario | State | Value | Release | Player sees | Audit |
|---|---|---|---|---|---|---|
| 1 | Proposer spends the offered goods before acceptance | Stays `ACTIVE`; `failed_accept_count` +1 | Nothing | None | `MKT-A01` on the taker; the proposer sees "an acceptance failed; restock or cancel" | Failure event, chain ID, code |
| 2 | Counterparty lacks the crowns for its side | Stays `ACTIVE` | Nothing | None | `MKT-A03` on the taker | Failure event |
| 3 | A resource is already reserved by another accepted action | Stays `ACTIVE` | Nothing | None | `MKT-A01`/`MKT-A03` naming the shortfall, never the other action | Failure event; the other action is not identified |
| 4 | Buyer cannot accommodate the incoming units | Stays `ACTIVE` | Nothing | None | `MKT-A04` with the free-space figure | Failure event |
| 5 | Two accepted actions compete for the same inventory | Later acceptance rejected | Nothing for the loser | None | `MKT-A01` on the later taker | Two acceptance attempts, one accepted |
| 6 | Acceptance races with cancellation | Cancellation wins if it committed first; otherwise acceptance wins | Nothing on the loser | None | `MKT-A08` or `MKT-A01` | Both actions with their order key |
| 7 | Acceptance races with a counteroffer | The live revision is the one accepted; the stale one fails | Nothing on the loser | None | `MKT-A08` | Revision IDs and statuses |
| 8 | The trade expires | `EXPIRED` | Nothing | None (nothing was reserved) | "Offer expired" on both sides | Expiry event, `MKT-D05` |
| 9 | Eligibility changes before P4 | `FAILED` | Nothing | Both sides and space | `F3` | P2 failure, reason, turn |
| 10 | A prohibited pair attempts a transfer | No chain created, or `ACTIVE` chain becomes unacceptable | Nothing | None | `MKT-A05` | Blocked-attempt event, pair state, no public reason |
| 11 | A fresh nation attempts a prohibited one-sided send | Rejected at creation or acceptance | Nothing | None | `MKT-E09` | Fair-value verdict, reference values, turn |
| 12 | A market action during `TRANSITION`/`CRISIS` | Action rejected before reservation | Nothing | None | `MKT-A06` with the state and the read-only rule | Rejection event |
| 13 | A nation rerolls with an accepted trade outstanding | Reroll **blocked** (D-039) | Nothing | None | The pre-reroll check names the unsettled trade | Reroll block event |

### 26.2 Global Trade

| # | Scenario | State | Value | Release | Player sees | Audit |
|---|---|---|---|---|---|---|
| 14 | A seller posts without enough available inventory | No listing | Nothing | None | `MKT-L08` with available vs requested | Rejection event |
| 15 | A buyer posts without enough available crowns | No listing | Nothing | None | `MKT-L06` or the available-crowns message | Rejection event |
| 16 | Two buyers attempt the same remaining sell quantity | First reservation wins; second rejected | Nothing for the loser | None | `MKT-A10` on the loser | Both executions, one accepted |
| 17 | Two sellers compete to fill a buy offer | First reservation wins; second rejected | Nothing for the loser | None | `MKT-A10` | Both executions |
| 18 | A partial fill succeeds | Listing `PARTIALLY_FILLED`; execution `RESOLVED` | `x` units and `x × p` crowns move | The settled portion | "Filled x of y" | Execution, ledger pair, quantity identity |
| 19 | A listing is cancelled while an execution is pending | `CANCELLED`; execution still settles | The locked portion moves; the remainder is released | `quantity_remaining` | "Remainder cancelled; one execution pending" | Cancellation and settlement rows |
| 20 | A listing expires | `EXPIRED` | Nothing for the remaining quantity | `quantity_remaining` | "Listing expired; x units released" | Expiry event |
| 21 | A seller withdraws already-committed inventory | Rejected or only the available part is listed | Nothing | None | `MKT-L08` | Rejection |
| 22 | A buyer spends already-committed crowns | Rejected by the available balance | Nothing | None | `MKT-A03` or an affordability message | Rejection; the reserved listing is unaffected |
| 23 | A public listing bypasses a prohibited pair | Execution rejected before reservation | Nothing | None | `MKT-A05` | Blocked attempt; the maker is not told who |
| 24 | A public execution violates the fresh-nation band | Execution rejected | Nothing | None | `MKT-E08` | Verdict with reference values |
| 25 | An unusual-price transaction triggers a signal | Settles normally | The trade moves | Consumed | A neutral confirmation; no accusation | `MKT-S01`, values, turn |
| 26 | A duplicate execution request | One execution only | Once | — | The original receipt | Both requests, one execution |
| 27 | P2 rejects a transaction | `FAILED` | Nothing | All three reservations | `F3`/`F4` | P2 record |
| 28 | P4 is interrupted and resumes | Execution retried; `F8` until resolved | Once | Once | "Recovering Turn N" | Recovery record, same `transfer_id` |
| 29 | A listing is submitted before the gate passes | No listing | Nothing | None | "Global Trade is not available" | Gate refusal |
| 30 | A statistic fails the sample or suppression rule | Not published | Nothing | None | `INSUFFICIENT_SAMPLE` or a coarsened band | Statistic job record |

### 26.3 Shared accounting

| # | Scenario | State | Value | Release | Player sees | Audit |
|---|---|---|---|---|---|---|
| 31 | The value risks overflow | Action rejected | Nothing | None | `MKT-E11` | Bounds check record |
| 32 | An invalid or zero quantity is submitted | Action rejected | Nothing | None | `MKT-E12` | Rejection |
| 33 | A failed transaction must leave both sides unchanged | `FAILED`/rejected | Nothing | Exactly once | The code and "nothing moved" | Failure plus release events |
| 34 | A completed transaction must reconcile | `RESOLVED` | Exactly the declared amounts | Consumed | The receipt and balances | Ledger pair, `transfer_id`, P7 identity check |
| 35 | A private directed trade must not be disclosed | Parties-only | — | — | A third party sees nothing | Restricted access log on any privileged read |

**MKT-215 — "Nothing" is checkable.** *Provisional.* For every failure row, the P7 invariant check confirms that both nations' totals, reservations and inventory are identical to their pre-acceptance values (except for the failure record). A difference is a defect, not a variant.

---
### 26.4 The code register

**MKT-215a — Every market code in one place.** *Provisional.* A code is stable, player-visible where MKT-A/D apply, and never reused for a different meaning. The market uses B-02's `F1`…`F10` for resolution failures; it does not invent a parallel `F` family.

| Code | Meaning | Where it appears |
|---|---|---|
| `MKT-A01` | The proposer no longer has the offered resources | Acceptance |
| `MKT-A02` | The proposer no longer has the offered crowns | Acceptance |
| `MKT-A03` | The acting nation cannot cover its own side | Acceptance, posting |
| `MKT-A04` | The receiver's warehouse cannot hold the incoming units | Acceptance, execution |
| `MKT-A05` | The pair is `RESTRICTED` or `MAINTAINED` | Creation, acceptance, execution |
| `MKT-A06` | The political state forbids new market actions | Creation, acceptance, posting, execution |
| `MKT-A07` | The fresh-nation rule refuses the acceptance; the message carries `E08`/`E09` as the sub-reason | Acceptance |
| `MKT-A08` | The offer or listing is no longer live (expired, superseded, cancelled, closed) | Acceptance, execution |
| `MKT-A09` | Duplicate idempotency key; the original receipt is returned | Every action |
| `MKT-A10` | The remaining quantity is already committed or the listing is exhausted | Execution |
| `MKT-D01` | Declined: no longer wanted | Decline |
| `MKT-D02` | Declined: terms unacceptable | Decline |
| `MKT-D03` | Declined: counterparty unavailable | Decline |
| `MKT-D04` | Declined: other | Decline |
| `MKT-D05` | Expired: the expiry turn passed | Expiry |
| `MKT-D06` | Expired: `STALE` after three failed acceptances | Expiry |
| `MKT-D07` | Expired: the counterparty became unavailable before acceptance | Acceptance/expiry |
| `MKT-E01` | Both sides are empty or the trade's value is zero | Creation |
| `MKT-E02` | A resource ID is not in the eleven-resource roster | Creation, posting |
| `MKT-E03` | The same resource appears twice on one side | Creation |
| `MKT-E04` | A quantity or crown amount is outside its declared bound | Creation, posting |
| `MKT-E05` | The counterparty does not exist or is not visible | Creation |
| `MKT-E06` | The named revision is not the live revision | Acceptance |
| `MKT-E07` | The chain has reached its ten-revision cap | Counteroffer |
| `MKT-E08` | The trade is outside the fair-value band while a fresh nation is a party | Creation, posting, execution |
| `MKT-E09` | A fresh nation is sending a one-sided transfer | Creation, acceptance |
| `MKT-E10` | A nation tried to execute its own listing or buy offer | Execution |
| `MKT-E11` | The arithmetic would exceed the safe bound | Creation, execution |
| `MKT-E12` | A quantity or price is negative, non-integer, or zero where the rule requires at least one | Creation, posting, execution |
| `MKT-G01` | Global Trade is not available because the release gate has not passed | Every global route |
| `MKT-L01`…`MKT-L17` | The declared limits in MKT-204 | The action that hit the limit |
| `MKT-S01`…`MKT-S10` | The review signals in MKT-157 | Recorded only; not player-visible as an accusation |

**MKT-215b — A sub-reason is not a second code.** *Provisional.* `MKT-A07` carries `E08` or `E09` in its message so the player knows whether the price or the one-sidedness is the problem. The audit records both, but the code table keeps `A07` as the acceptance-stage code and `E08`/`E09` as the creation/posting codes. A test that sees two top-level codes for one failure is wrong.

---

## 27. Worked examples

**MKT-216 — How to read the examples.** *Provisional.* Every number below uses the constants in this document and [the formula register](13_trade_and_markets_formula_register.md): the eleven reference prices (MKT-139), `B = 3,000` bp, `MAX_TRADE_UNITS_PER_LINE = 100,000` and the 72-turn expiry. Starting balances are illustrative, not a standard start. The examples demonstrate **internal arithmetic consistency**; they do not prove balance, liquidity, abuse resistance or production readiness. Every division is `floor`.

### E1 — A successful directed reciprocal trade

**Opening.** Aurelia has 1,000 crowns, 300 food and 0 steel. Borealis has 500 crowns, 0 food and 120 steel. Both are mature and unrelated.

**Terms.** Aurelia offers **200 crowns + 100 food**; Borealis offers **50 steel**. Aurelia prices food at 1; Borealis prices steel at 7.

| Side | Reference value | Declared value |
|---|---|---|
| Aurelia | `200 + 100 × 1 = 300` | `300` |
| Borealis | `50 × 7 = 350` | `350` |

`V_low = 300`, `V_high = 350`. Bound: `floor(300 × 13,000 / 10,000) = floor(390) = 390`. `350 ≤ 390`, so `IN_BAND`.

**Acceptance.** Aurelia reserves 200 crowns, 100 food and 50 units of space. Borealis reserves 50 steel and 100 units of space. No value moves.

**P4.** Aurelia: crowns `1,000 − 200 = 800`; food `300 − 100 = 200`; steel `0 + 50 = 50`. Borealis: crowns `500 + 200 = 700`; steel `120 − 50 = 70`; food `0 + 100 = 100`.

**Ledger.** One `transfer_id`, four events:

| Nation | Event | Crowns | Resource |
|---|---|---|---|
| Aurelia | `TRADE_SELL` | `0` | `−100 food` |
| Aurelia | `TRADE_BUY` | `−200` | `+50 steel` |
| Borealis | `TRADE_SELL` | `+200` | `−50 steel` |
| Borealis | `TRADE_BUY` | `0` | `+100 food` |

Crown sum `0 − 200 + 200 + 0 = 0`; food `−100 + 100 = 0`; steel `+50 − 50 = 0`. **Reconciled.** The 200 crowns are the consideration for the steel leg, so the payment appears **once**: as a debit on Aurelia's `TRADE_BUY` and a credit on Borealis's `TRADE_SELL`. The food leg has no crown consideration and carries `0`. An earlier draft put `+200` on Aurelia's `TRADE_SELL` and `−200` on its `TRADE_BUY` (and the mirror on Borealis), which nets each treasury to zero while the closing balances move by ±200 — the same payment counted twice. A single payment must never be entered with both signs on one side's two events.

### E2 — A bundled directed trade

**Opening.** Cyrene: 400 crowns, 100 oil, 60 coal. Delos: 300 crowns, 40 aluminum, 20 lead.

**Terms.** Cyrene gives **100 crowns + 40 oil + 20 coal**; Delos gives **20 aluminum + 5 lead**.

| Side | Reference value |
|---|---|
| Cyrene | `100 + 40 × 2 + 20 × 1 = 100 + 80 + 20 = 200` |
| Delos | `20 × 8 + 5 × 3 = 160 + 15 = 175` |

Bound: `floor(175 × 13,000 / 10,000) = floor(227.5) = 227`. `200 ≤ 227` → `IN_BAND`.

**Reservations.** Cyrene reserves 100 crowns, 40 oil, 20 coal and **25 units of space** (20 aluminum + 5 lead). Delos reserves 20 aluminum, 5 lead and **60 units of space** (40 oil + 20 coal).

**P4.** Cyrene: crowns 300; oil 60; coal 40; aluminum 20; lead 5. Delos: crowns 400; aluminum 20; lead 15; oil 40; coal 20. Five lines, two directions, one `transfer_id`; every resource delta nets to zero.

### E3 — A stale directed offer

**Opening.** Ephyra has 120 food, of which **20 is reserved** for an accepted construction order, so **available = 100**. It offers **100 food** to Gela for **100 crowns**.

**What changes.** Ephyra sells 60 food to a third nation. Its total food becomes 60, the 20 reservation remains, so **available = 40**. The offer is still `ACTIVE`; nothing was reserved when it was created (D-016).

**Gela accepts.** The acceptance re-validates Ephyra's side: `40 < 100` → `MKT-A01`. `failed_accept_count = 1`. No crown, food or space is reserved; Gela's 100 crowns remain available. The chain stays `ACTIVE`.

**If it happens twice more.** On the third failed acceptance the chain moves to `EXPIRED` with `MKT-D06 (STALE)`. Ephyra can restock and create a new chain; Gela sees "this offer is no longer live".

### E4 — A fresh-nation fair reciprocal trade

**Opening.** Halos was created on turn 1; the current turn is 10, so `elapsed = 9 < 360` and Halos is **fresh**. It has 310 units and 1,500 crowns.

**Terms.** Halos gives **100 food**; Ionia gives **100 crowns**. `V_Halos = 100`, `V_Ionia = 100`. Bound `130`; `100 ≤ 130` → `IN_BAND`.

**Result.** Allowed. Halos reserves 100 food and 100 space; Ionia reserves 100 crowns. At P4 Halos has 100 more crowns and 100 less food; Ionia the reverse. The trade is reciprocal and in band, so it is exactly the legitimate newcomer trade ONB-031 permits.

### E5 — A fresh-nation out-of-band trade

**Terms.** Halos gives **100 food** and asks for **200 crowns**. `V_low = 100`, `V_high = 200`; bound `130`; `200 > 130` → `OUT_OF_BAND`.

**Result.** Rejected at creation with `MKT-E08`; nothing is reserved and no chain exists. The message says: "New-nation protection: the larger side of a trade may be at most 30% bigger than the smaller. 100 food is worth 100 crowns and 200 crowns is 100% bigger, so this trade is outside the band."

**Boundary.** At **130 crowns** the bound is `floor(100 × 13,000 / 10,000) = 130` and `130 ≤ 130`, so it **passes**. One crown more fails.

### E6 — A mature-nation unusual-price trade

**Opening.** Kition (mature) has 20 uranium; Larisa (mature) has 1,000 crowns.

**Terms.** Kition sells **10 uranium** for **600 crowns**. `V_Kition = 300`, `V_Larisa = 600`; bound `390`; `600 > 390` → `OUT_OF_BAND`.

**Result.** **Allowed.** The confirmation shows "60 crowns per unit; book value 30; +100% over book". The settlement moves 600 crowns and 10 uranium; the market records `MKT-S01`. No sanction, no block, no public flag. Kition's realised gain over book is `600 − 300 = +300`; Larisa's realised gap is `−300`. National wealth is not minted: one side's gain is the other's cost.

### E7 — A successful public sell listing

**Opening.** Massalia has 800 steel, 0 reserved. Nicaea has 5,000 crowns, a 2,000-unit warehouse and 1,000 units in stock (free space 1,000).

**Posting.** Massalia lists **500 steel at 8 crowns**. It reserves 500 steel: total 800, reserved 500, available 300. No crowns are reserved. The board shows 500 × 8 = 4,000.

**Execution.** Nicaea executes **200 units**. It reserves `200 × 8 = 1,600` crowns and 200 units of space. Massalia's listing moves 200 to `quantity_locked`: remaining 300, locked 200, reserved units 500.

**P4.** Nicaea: crowns `5,000 − 1,600 = 3,400`; steel `0 + 200 = 200`. Massalia: crowns `0 + 1,600 = 1,600`; steel `800 − 200 = 600`. Listing: filled 200, locked 0, remaining 300, reserved 300.

**Book-value report.** Nicaea received steel with a book value of `200 × 7 = 1,400` and paid 1,600, a realised gap of **−200**. Massalia sold book value 1,400 for 1,600, a realised gain of **+200**. No crown was created.

### E8 — A successful public buy offer

**Opening.** Olbia has 1,000 crowns and 0 food. Patara has 400 food.

**Posting.** Olbia posts **400 food at 2 crowns**, committing `400 × 2 = 800` crowns: total 1,000, reserved 800, available 200.

**Execution.** Patara executes **150 units**. Olbia's locked crown commitment is `150 × 2 = 300`; Patara reserves 150 food and Olbia reserves 150 units of space.

**P4.** Olbia: crowns `1,000 − 300 = 700`; food `0 + 150 = 150`. Patara: crowns `0 + 300 = 300`; food `400 − 150 = 250`. Olbia's buy offer: filled 150, locked 0, remaining 250, reserved crowns `250 × 2 = 500`.

**Check.** `800 − 300 = 500`, exactly the remaining commitment. The buyer never advertised more than it had reserved.

### E9 — A completed global purchase and the fair-value gap

**Opening.** Rhegium buys **100 aluminum at 9 crowns** from a listing.

**Values.** Total paid `100 × 9 = 900`. Book value `100 × 8 = 800`. The buyer's realised fair-value gap is `800 − 900 = −100`. The seller's is `+100`. The ledger moves 900 crowns and 100 aluminum; national wealth changes by `−900 + 800 = −100` for the buyer and `+900 − 800 = +100` for the seller. The sum is zero. The 1-crown difference per unit is a **transfer**, not a mint.

### E10 — Two partial fills of one listing

**Opening.** same seller as E7: 900 steel, 0 reserved. Posts **500 at 8**: reserved 500, available 400.

**Fill 1.** A buyer executes 200 at 8 = 1,600. After settlement: filled 200, locked 0, remaining 300; reserved units 300; seller steel 700.

**Fill 2.** Another buyer executes 100 at 8 = 800. After settlement: filled 300, locked 0, remaining 200; reserved units 200; seller steel 600; proceeds `1,600 + 800 = 2,400`.

**Identity.** `500 = 300 filled + 0 locked + 200 remaining`. Each fill had its own `execution_id`, its own `transfer_id` and its own ledger pair. The listing was the parent, not a single transaction.

### E11 — Reservation and cancellation

**Opening.** Sinope has 900 steel, 0 reserved, 0 available elsewhere.

1. Post **500 at 8** → total 900, reserved 500, available 400.
2. A buyer executes **200** → locked 200, remaining 300; reserved 500.
3. Sinope cancels the listing → releases **300**, keeps 200 locked; total 900, reserved 200, available 700.
4. P4 settles the 200 → total 700, reserved 0, available 700.

The cancelled listing cannot be executed again; a later failed execution of the 200 would return those units to Sinope's available balance, not to the closed listing.

### E12 — Expiry with a locked execution

**Opening.** Smyrna posts **500 steel at 8** on turn 10; `expires_turn = 82`. By turn 82 it has filled 0 and a buyer has an accepted 200-unit execution, so `locked = 200`, `remaining = 300`.

**At turn 82.** The B0 maintenance pass sees `expires_turn = 82`: it releases the **300 remaining**, marks the listing `EXPIRED`, and leaves the 200 locked. P4 settles the 200: filled 200, locked 0, listing closed. Smyrna's inventory falls by 200, not 500.

### E13 — Double-spend prevention

**Inventory.** Tyre has 600 steel. It posts 500 → available 100. A second post of 500 is rejected with `MKT-L08` (`100 < 500`); a second post of 100 is allowed (two active listings, both within the per-resource cap).

**Crowns.** Tyre has 1,000 crowns. It posts a buy offer of 400 food at 2 → reserved 800, available 200. A second buy offer of 100 at 2 = 200 is allowed exactly. A third of 101 at 2 = 202 is rejected: `202 > 200`. The reservation is the mechanism; the client's displayed balance is never the authority (TR-068, TR-072).

### E14 — A restricted pair attempts a public execution

**Opening.** Assur and Byblos are `RESTRICTED` (same network, unresolved). Byblos has a sell listing of 100 food at 1. Assur tries to execute it.

**Result.** Rejected at acceptance with `MKT-A05`, before any reservation. Byblos's listing remains 100; Byblos is not told who tried, only that no execution occurred. The audit records the pair state, the listing ID and the turn. D-034 row 4 is satisfied: the market match was blocked at the match point.

### E15 — Warehouse-capacity failure

**Opening.** Ctesiphon has `W = 2,000`, total inventory 1,950, no space reserved → free 50. It tries to execute **100 steel** from a listing.

**Result.** `MKT-A04`: "Your warehouse cannot hold the incoming goods (need 100, free 50)." No crowns are reserved, the listing is unchanged, and Ctesiphon can buy at most 50 units this turn. This is ECN-124 applied to a purchase.

### E16 — A duplicate execution request

**Opening.** A buyer executes 200 steel at 8 with key `K1`.

**First request.** Accepted; 1,600 crowns reserved; listing locked 200.

**Second request with `K1`.** Returns the original receipt (`MKT-A09`), no new reservation, no second lock. Reserved stays 1,600; locked stays 200.

**A different key `K2` for 100 more.** The listing has 300 remaining, so it is accepted: locked 300, reserved `1,600 + 800 = 2,400`. Two executions, not three.

### E17 — An atomic failure with no value transfer

**Opening.** A trade of 100 food for 100 crowns was accepted. At P2, the crown-paying nation is found suspended.

**Result.** `F3`. The 100 food reservation and the 100 crowns reservation are released; no ledger row is written; both totals are exactly what they were before acceptance. The chain is `FAILED`. The digest says "Failed at validation: the counterparty is no longer eligible; nothing moved." The seller's food is available again.

### E18 — Ledger reconciliation

Using E1's four events, the reconciliation is:

| Check | Computation | Result |
|---|---|---|
| Crown conservation | `+200 − 200 + 200 − 200` | `0` |
| Food conservation | `−100 + 100` | `0` |
| Steel conservation | `+50 − 50` | `0` |
| One `transfer_id` | all four events | pass |
| Buyer's cost = seller's proceeds | `200` each way | pass |
| Negative balance | none | pass |

A reconciliation that fails any row is a defect (`MKT-S10`), not a rounding difference.

### E19 — A fresh nation's listing and a fresh buyer's execution

**Posting by a fresh seller.** Halos lists **10 uranium at 60**. Book value is `10 × 30 = 300`; the ask is 600; `600 > floor(300 × 1.3) = 390` → `OUT_OF_BAND`. Because Halos is fresh, the **posting** is rejected with `MKT-E08` (MKT-148 item 4). At **30 crowns** the ask is 300 and the listing is allowed.

**Execution by a fresh buyer.** A mature seller lists 10 uranium at 60. Halos (fresh) tries to execute. The two sides are 600 crowns and 300 book; `600 > 390` → rejected at execution with `MKT-E08`. A mature buyer may execute it and receives `MKT-S01`.

### E20 — The inclusive band boundary

`V_low = 100`. `B = 3,000`.

| `V_low` | `V_high` | `floor(V_low × 13,000 / 10,000)` | Verdict | Why |
|---|---|---|---|---|
| 100 | 129 | 130 | `IN_BAND` | 29% premium |
| 100 | **130** | 130 | **`IN_BAND`** | **inclusive boundary: exactly 1.30** |
| 100 | 131 | 130 | `OUT_OF_BAND` | 31% premium |
| 130 | 100 | 130 | `IN_BAND` | reversed parties; the pair is normalized by value |
| 70 | 100 | 91 | `OUT_OF_BAND` | a 30% discount is **not** the mirror of a 30% premium: 100 is 42.86% bigger than 70 |
| 0 | 100 | — | `ONE_SIDED` | one side gives nothing (MKT-146); it is not a band failure |
| 0 | 0 | — | `INVALID` | both sides empty (`MKT-E01`) |

The boundary is inclusive by design: a trade at exactly 1.30 is inside the band, and a test that rejects it is wrong. The rule is asymmetric: `100 vs 130` passes, `70 vs 100` does not. The interface therefore says "the larger side is X% bigger", never "within ±30%"; a 30% discount would require a ratio of 1.4286, not 1.30.

### E21 — A counteroffer replaces the terms

**Opening.** A offers 100 food for 100 crowns. B counters with 100 food for **120 crowns**. A accepts.

**Revision.** The chain moves to revision 2, authored by B; revision 1 becomes `SUPERSEDED` and can never be accepted. The fair-value check on revision 2: `V_low = 100`, `V_high = 120`, bound 130 → `IN_BAND`.

**Reservations.** A reserves 100 food; B reserves 120 crowns; B reserves 100 space. P4: A gives 100 food and receives 120 crowns; B gives 120 crowns and receives 100 food. Revision 1 moved nothing and reserved nothing. The expiry is `acceptance-or-revision turn + 72`; the counteroffer reset it.

---
## 28. Cross-system contracts

**MKT-217 — The contract table.** *Provisional.* "Owner" is the document that holds the authoritative rule. The market depends on it and may not contradict it. A contradiction is resolved by correcting the market document, not by quietly creating a second rule.

| System | Owner | What the market depends on | What the market returns | A contradictory implementation would be |
|---|---|---|---|---|
| **B-02 — turn system** | [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) | P0–P7; class Q; `ACCEPTED → RESOLVED/FAILED`; TR-067…TR-072 reservations; B1 ordering; `F1`…`F10`; idempotency; recovery | Market action types mapped to Q; P4 sub-order; market failure codes wrapping the `F` codes; row/work estimates | Settling at acceptance, a second scheduler, a second ordering key, or a market action that bypasses P2 |
| **B-03 — account and nation** | [B-03](09_account_onboarding_nation_creation_and_progression.md) | One account per person (D-018/D-032); account/nation states; NET-014…NET-043 pair matrix; ONB-031/032 window; RRL reroll; restrictions survive | The pair check at every value-moving step; the fresh window applied to trade; a pre-reroll check for unsettled trades | A market-specific identity, a "trusted trader" flag, a reroll that clears a restriction, or a trade that ignores the pair |
| **B-04 — economy and treasury** | [B-04](10_economy_resources_treasury_and_finances.md) + [register](10_economic_formula_and_balance_register.md) | Crowns; eleven resources; integer units; no debt; total/reserved/available; warehouse; reference prices; `TRADE_BUY`/`TRADE_SELL`; `transfer_id`; conservation | The trade's value flow, its ledger pair, the realised gap report and the fee event (when enabled) | A second currency, a negative balance, a mint, a burn without a fee, or a trade that changes a P3 result |
| **B-05 — production and storage** | [B-05](11_cities_infrastructure_production_and_research.md) | `W`; `free_space = W − total_inventory`; `SPACE_BLOCKED`; one national warehouse; RM is not tradable | A space reservation at acceptance; a hard failure when the goods do not fit | An overfill, a per-city stockpile, a purchased building, or a traded research point |
| **B-06 — domestic politics** | [B-06](12_population_and_domestic_politics.md) | `leadership_state`; DMP-262's read-only rule for `TRANSITION`/`CRISIS`; no political trade tax | A state check at acceptance only; a readable market; normal settlement for accepted trades | A political fee, a tariff, a stability penalty, or a failure of an already-accepted trade because the state changed |
| **Prompt 08 — diplomacy** | Future B-08 | Embargoes, blockades, treaties, diplomatic standing | A hook for a diplomatic restriction; the market does not define one | A market-level embargo invented before B-08, or a treaty that silently moves value outside the ledger |
| **Prompt 09 — alliances** | Future B-09 | Alliance membership; bank permissions; role checks | Nothing at launch; an alliance market is out of scope (MKT-008) | Routing a trade through an alliance bank, or an alliance-only board that bypasses the pair rule |
| **Prompt 10 — warfare** | Future B-10 | Operations Points (non-tradable); campaigns; blockades if adopted | A war-time trade restriction hook; no OP in a trade | Trading OP, buying a campaign result, or a blockade implemented as a market fee |
| **Prompt 11 — world events** | Future B-11 | Rankings; chronicle; objectives; k = 5 | Market statistics and the trade history that a ranking must not expose | A "top trader" ranking derived from private directed trades |
| **Prompt 12 — fair play** | Future B-12 | Moderation; evidence; appeals; retention; automation | `MKT-S` signals; a narrow listing suspension; the audit trail | An automatic ban from a price signal, a public accusation, or a confiscation |
| **Prompt 13 — interface** | Future B-13 | Screens, journeys, accessibility, notifications | The labels, states and confirmation rules in §13 and §22 | A "market price" label on a book value; a listing shown as settled before P4 |
| **Prompt 14 — formulas** | Future B-14 | Simulation, tuning, rounding, caps | The constants and the test list in §30 | A silent constant change without a register revision |
| **Prompt 15 — Bible** | Future B-15 | The assembled cross-system matrix | This document's edges | A Bible that presents a provisional value as approved |

**MKT-218 — One rule, one owner.** *Provisional.* If B-08 later adds an embargo, the market reads it; it does not grow its own. If B-09 adds an alliance market, it must declare its own permissions and pair checks; it may not reuse this document's listing object by implication. If B-12 wants a market ban, it must use the account measures it owns; the market will not grow a fourth state (MKT-182).

**MKT-219 — The accounting interface is stable.** *Provisional.* B-04 may change a reference price only by a register revision. The market's value formula reads the register's constant; it does not copy a second table into code. The `TRADE_BUY`/`TRADE_SELL` names and the shared `transfer_id` are fixed by ECN-211; a rename requires a B-04 decision and a market revision.

**MKT-220 — The political interface is one-way.** *Provisional.* B-06 tells the market whether new actions are permitted; the market tells B-06 only that a trade settled or failed, for the digest. The market does not feed approval, stability or legitimacy, and it does not read a political score to price a trade. A future "war economy" or "blockade" effect belongs to B-08/B-10 and must state its own ledger row and its own player-facing cause.

---

## 29. Formula and requirement references

**MKT-221 — The market's formulas.** *Provisional.* All expressions live in [the market formula register](13_trade_and_markets_formula_register.md) under `F-TM-###`. This document summarises; the register is authoritative for the expression, variables, units, bounds, rounding and dependencies. The register does not duplicate B-04's reference prices; it cites them.

| Area | Formula IDs |
|---|---|
| Side values, declared vs reference | F-TM-001…F-TM-004 |
| Fair-value bound, verdict, ratio and fresh window | F-TM-005…F-TM-009 |
| Directed line, side and offer totals, expiry | F-TM-010…F-TM-014 |
| Listing quantity and reservation identities | F-TM-015…F-TM-020 |
| Execution value, available balance and space | F-TM-021…F-TM-026 |
| Realised fair-value gap | F-TM-027 |
| Market average and sample gate | F-TM-028…F-TM-030 |
| Checked arithmetic and bounds | F-TM-031…F-TM-033 |
| Limits and rate windows | F-TM-034…F-TM-036 |
| Conservation and fee | F-TM-037…F-TM-039 |

**MKT-222 — The requirements.** *Provisional.* The traceable rows are **REQ-427…REQ-512** in [the requirements register](03_requirements_traceability.md). They cover the two-system scope, the directed object and lifecycle, reservations and settlement, limits, fees, the Global Trade object and execution, assets, discovery, pricing, fair value, fresh protection, manipulation, accounting, timing, eligibility, privacy, statistics, the six gates, free-first feasibility and the examples. Their statuses are provisional unless the row cites an owner constraint.

**MKT-223 — The decisions.** *Provisional.* The project-level decisions are **D-109…D-121** in [DECISIONS.md](../DECISIONS.md); the Stage 2 position rows are **DD-123…DD-135** in [the Stage 2 register](04_approved_and_provisional_decisions.md). D-016 and D-017 are unchanged; **D-110 is a scoped new rule for public listings**, not an amendment of D-016.

**MKT-224 — The unresolved rows.** *Provisional.* **UD-037** (band and limit calibration) and **UD-038** (post-gate liquidity and crossed-book behaviour) are opened as simulation/operational questions. No design question in this document is left open: every rule above is decided, provisionally where a number is involved.

---

## 30. Provisional decisions and open validation obligations

**MKT-225 — What is provisional and why.** *Provisional.*

| Constant or rule | Value | Why it is provisional | Who validates |
|---|---|---|---|
| Fair-value band `B` | 3,000 bp | A judgement, not a measurement; the reference's 30% is a shape, not a validated number | Prompt 14 simulation (UD-037) |
| Fresh window | 360 turns / 30 days | Inherited from ONB-031/032; not measured | Prompt 14; a later player-experience review |
| Directed expiry | 72 turns | Chosen for asynchronous negotiation and storage; not measured | Prompt 14 |
| Listing expiry | 72 turns | Same | Prompt 14 |
| Failed acceptances to `STALE` | 3 | A heuristic | Prompt 14 |
| Active outgoing offers | 5 | A readability judgement | Prompt 14 |
| Active listings per resource / total | 4 / 12 | A readability and write-cost judgement | Prompt 14 |
| Market actions per 12 turns | 20 | A spam ceiling | Prompt 14 |
| Executions per nation per turn | 50 | A P4 bound | Prompt 14 + Stage 3 |
| World executions per turn | 5,000 | A placeholder for measured capacity | Stage 3 must replace it |
| `MKT-S07` extreme price | 10× / one tenth | Triage, not a rule | Prompt 14 |
| `MKT-S08` concentration | 50% of a resource's volume | Triage | Prompt 14 |
| Statistic window | 12 turns | A rolling day; the game has no calendar day | Prompt 14 |
| Volume band | lower 10 units | A suppression coarseness | Prompt 14 |

**MKT-226 — What is decided, not provisional.** *Provisional (design).* The **structure** is decided: two systems; directed fee-free; no reservation at directed creation; reservation at acceptance; P4 settlement; public listings reserve; taker-selected price; partial fills; fair value on book value; fresh block and mature signal; parties-only directed terms; public listings, private completed-trade identity; no statistics at first playable; the six-gate release. A later prompt may change a structure only by a superseding decision with a documented reason, not by a local exception (TR-095).

**MKT-227 — The validation obligations this document creates.** *Provisional.* The following are planned, not executed:

1. A simulation of the band at 1,000–3,000 bp over a representative trade mix, testing how many legitimate fresh trades are blocked and how many out-of-band mature trades are flagged.
2. A simulation of the listing caps and the 72-turn expiry over a 30-day, 1,000-nation world, measuring empty-board time and stale-listing share.
3. A write-count measurement per action on the real schema, and a P4 load test at 5,000 executions.
4. A pair-check test that a restricted pair cannot execute either side of a public listing and cannot infer the restriction from the error.
5. A conservation/fuzz test that every failure path leaves both sides identical, and every success sums to zero.
6. A duplicate-request test for every action type, including a retry after a P4 interruption.
7. A gating test that no Global Trade route is reachable before G-1…G-6 pass.
8. A suppression test that a 4-nation statistic is withheld and a 5-nation statistic is published without a complementary leak.

**MKT-228 — What has *not* been validated.** *Provisional.* No line of market code exists. No database, scheduler, RLS policy, endpoint or screen has been built or tested. No player has traded. The arithmetic in §27 is hand-checked by the documentation checker, not by a runtime. The fair-value band, the caps and the expiry are **not** balanced, and no claim is made that they are.

---

## 31. Validation results

**MKT-229 — What was actually run.** *Provisional.* The documentation-level checks are recorded here after the final edit. The market's arithmetic checker is `qa_backups/verify_market_numbers.py`; it recomputes sections 17, 23 and 27 from the register's constants and guards the document's own claims. It is a **documentation check**, not a runtime test.

| Command | Expected | Actual |
|---|---|---|
| `python qa_backups/verify_market_numbers.py` | All checks pass | See §31.1 |
| `python qa_backups/verify_market_numbers.py --self-test` | Every guard rejects its defect | See §31.1 |
| `python qa_backups/validate_final.py` | All document checks pass | See §31.1 |
| `python qa_backups/09_validate.py` | All register checks pass | See §31.1 |
| `python qa_backups/test_next_action.py` | All tests pass | See §31.1 |
| `python qa_backups/test_decision_registers.py` | All tests pass | See §31.1 |
| `python qa_backups/verify_economy_numbers.py` | 164/164 | See §31.1 |
| `python qa_backups/verify_city_numbers.py` | 267/267 | See §31.1 |
| `python qa_backups/verify_politics_numbers.py` | 879/879 | See §31.1 |

### 31.1 Recorded result (final run, 2026-10-28)

| Command | Actual result | Exit |
|---|---|---|
| `python3 qa_backups/verify_market_numbers.py` | **76/76** checks passed; 0 failed | 0 |
| `python3 qa_backups/verify_market_numbers.py --self-test` | **12/12** guards detected their defect | 0 |
| `python3 qa_backups/verify_economy_numbers.py` | **164/164** passed | 0 |
| `python3 qa_backups/verify_city_numbers.py` | **267/267** passed | 0 |
| `python3 qa_backups/verify_politics_numbers.py` | **879/879** passed | 0 |
| `python3 qa_backups/validate_final.py` | **ALL CHECKS PASSED** | 0 |
| `python3 qa_backups/validate_final.py --self-test` | **3/3** guards detected their defect | 0 |
| `python3 qa_backups/09_validate.py` | **345/345** checks passed | 0 |
| `python3 qa_backups/test_decision_registers.py` | **12** tests OK | 0 |
| `python3 qa_backups/test_next_action.py` | **15** tests OK | 0 |

**2026-10-29 follow-up — status reconciliation, no design change.** A later review found contradictory 07B/07C status sentences in the continuity files, and no guard able to see them: the validator compared **prompt numbers**, and 07B and 07C are both "Prompt 07". `status_rules.py` now carries a sub-prompt rule wired into `validate_final.py`, and `test_next_action.py` grew from 15 to **20** tests (the `--self-test` count is now **4/4**). That pass corrected status text only — **no rule, formula, example, requirement, decision or gate in this document changed** — and its record is [progress log §22](06_stage_2_progress_log.md).

**What the market checker proves.** It recomputes the examples in §17, §23 and §27 from the register's constants, checks that each of the 35 rows in §26 names a final state, verifies that every `MKT-` and `F-TM-` identifier cited here exists in the register, confirms the eleven-resource roster and the reference prices against B-04, and asserts the fresh-window boundary (turn 359 fresh, 360 not), the inclusive band edge, the reservation identities, crown conservation and the zero launch fee. The 12 self-tests each corrupt one input and require rejection, so a disabled guard fails the run.

**Validator repairs made in this pass.** Three inherited checkers encoded the register totals that existed **before** 07B, so they reported failures that were about the checker, not the design. Each was updated to the real, recounted total: the requirement range (**REQ-001…REQ-512**, and a check whose code still compared against 426 while its own message said 512), the unresolved range (**UD-001…UD-038**), the status reconciliation (**22 Resolved / 8 Deferred / 8 Open**) and the requirement status totals (**18 approved / 487 provisional / 5 open / 2 deferred**). The prompt-column pattern now accepts `07B`/`07C`. A fourth guard required the stage roadmap row to end with the literal **"Prompt 07 next"**; it now requires **"07B market foundations complete"** *and* **"Prompt 07C next"**, which is stricter than the old sentence because both facts must be present. **No assertion was deleted, skipped or loosened to pass unconditionally**; every updated check still fails on a wrong count or a wrong stage, and all self-tests were rerun afterwards.

**Not run — there is nothing to run.** No game server, database, turn scheduler, queue or browser was started; no market code exists. No concurrency, load, security or penetration test was performed. No balance simulation, liquidity measurement or incident-rate measurement exists. The 3,000 bp band, the limits, the 72-turn expiry, the statistics thresholds and the 5,000-execution world guard remain unvalidated numbers.

**MKT-230 — Limitations.** *Provisional.* A passing documentation check proves that the formulas in this document agree with the register and that the examples' arithmetic is internally consistent. It does **not** prove market balance, liquidity, anti-fraud effectiveness, free-tier capacity or production readiness. Those are MKT-227's obligations and Stage 3's measurements.

---

## 32. Handoff to Prompt 07C

**MKT-231 — What 07C inherits.** *Provisional.* 07C owns the **workflows, edge cases, integration checks and final market-design acceptance**. It inherits a decided foundation, not a blank page. It must not re-open the structure in MKT-226 without a superseding decision.

**MKT-232 — What 07C must produce.** *Provisional.*

1. **Screen-by-screen workflows**: the directed inbox, the compose/counter screen, the offer detail, the global board, the listing detail, the execution confirmation, the trade history, the failure state, the empty/insufficient-sample state, and the read-only political state.
2. **Edge-case walkthroughs** beyond §26: a counteroffer arriving after acceptance, a listing suspended mid-execution, a reroll in the same turn as an accepted trade, a warehouse expansion in the same turn as an incoming execution, a P2 failure after a cancellation, a duplicate across a recovery, and a statistic that crosses the 5-nation threshold between two turns.
3. **Integration checks** against B-02, B-03, B-04, B-05, B-06 and the future B-08…B-14, with a signed-off interface table and the exact field each side reads.
4. **Acceptance tests** for the eight obligations in MKT-227, with a test ID, a precondition, a step, an expected result and a failure code.
5. **Final acceptance** of the market design only when the specification, the registers, the continuity documents and the available checks agree.

**MKT-233 — What 07C may not do.** *Provisional.* It may not implement code, create migrations, deploy, start Prompt 08, release Global Trade, change a decision without a superseding entry, or turn a provisional value into an approved one by describing it as such. It may not add a fee, a tax, a price floor or a new asset.

**MKT-234 — The 07C checklist.** *Provisional.*

- [ ] Every §26 failure has a player-visible message and a stable code.
- [ ] Every screen names the settlement turn and never shows a pending trade as complete.
- [ ] Every balance display has total, reserved and available.
- [ ] Every price display distinguishes book value, asking/offer price and completed price.
- [ ] The crossed-book badge and the better-price confirmation are specified.
- [ ] The fresh-nation block and the mature signal are distinguishable in the UI.
- [ ] A restricted pair sees a neutral message and the review route, never the other account's state.
- [ ] The read-only `TRANSITION`/`CRISIS` state is specified with its exact disabled controls.
- [ ] The six gates are visible as **not met**, with their evidence owners.
- [ ] The 5-nation statistic rule and the `INSUFFICIENT_SAMPLE` state are specified.
- [ ] The ledger pair and `transfer_id` are visible in the player's own history, not to third parties.
- [ ] No production code, migration, deployment or live-world change is claimed.

**MKT-235 — Document control.** *Provisional.*

| Item | Value |
|---|---|
| Prompt | Stage 2, Prompt 07B — market foundations; reconciled by Prompt 07C — workflows and acceptance |
| Version | 1.1 |
| Created | 2026-10-28 (v1.1 2026-10-29) |
| Primary deliverable | `docs/stage-2/13_trade_and_markets.md` |
| Companion | `docs/stage-2/14_market_workflows_and_acceptance.md` (workflows, matrix, gate evidence) |
| Formula register | `docs/stage-2/13_trade_and_markets_formula_register.md` |
| Requirements | REQ-427…REQ-513 |
| Project decisions | D-109…D-122 |
| Stage 2 positions | DD-123…DD-136 |
| Open unresolved rows | UD-037, UD-038 |
| Implementation status | **None** — design only |
| Global Trade status | **Designed; release-gated** — G-1, G-2, G-3, G-5 and G-6 **not met**; G-4 **partial** |
| Next task | **Prompt 08 — diplomacy between nations**, once Prompt 07C is accepted; 07C's acceptance record is the companion §15 |

**End of document.**
