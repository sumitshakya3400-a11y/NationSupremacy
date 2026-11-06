# Market workflows and acceptance

**Version:** 1.0 · **Created:** 2026-10-29 · **Stage 2, Prompt 07C** · **Revised:** 2026-10-29 (first issue: the workflow layer, the acceptance matrix, the G-1…G-6 evidence plan and the final Prompt 07 acceptance record)
**Status:** **Acceptance specification — design only.** It specifies what a future implementation must do and how that behaviour is to be tested. No market code, database, endpoint, screen, scheduler or deployment exists. No test below has been executed as a runtime test.
**Authority:** [B-07](13_trade_and_markets.md) owns the market rules; [the formula register](13_trade_and_markets_formula_register.md) owns the formulas; **this document** owns the workflows, the test catalogue, the rule-to-test matrix, the release-gate evidence plan and the Prompt 07C acceptance record. It adds no market rule of its own. Where a workflow and a rule disagree, B-07 wins and this document is corrected.
**Companions:** [B-07](13_trade_and_markets.md) · [formula register](13_trade_and_markets_formula_register.md) · [07A research](research/07A_politics_and_war_market_research.md) · [requirements](03_requirements_traceability.md) · [decisions](04_approved_and_provisional_decisions.md) · [unresolved](05_unresolved_design_decisions.md) · [progress log](06_stage_2_progress_log.md)

---

## 1. Scope and reading order

**1.1 What this document is for.** Prompt 07B decided the market model. Prompt 07C must show that the model can be operated: who acts, in what order, what the player sees, what the server persists, which reservation is created and released, which ledger pair is written, which turn phase resolves it, and which test would prove it. It must also state, without inflation, what evidence the six Global Trade release gates still require.

**1.2 What it is not.** It is not a second rulebook. It does not redefine a resource, a price, a reservation, a fee, a gate or an accounting identity. It does not implement a screen; a wireframe or a field list is a specification input, not an application. It does not turn a specification-level scenario into a passed test. The test catalogue below is a **test design**; only the document and arithmetic checks named in §14 have run.

**1.3 Reading order for a new session.** Read B-07 first (at least §§3–6, 9–19 and 26–32), then the formula register §§2–4, then this document §2–§4 for the canonical semantics, then the workflow for the task at hand, then the matrix row for every rule being implemented. The 07A report is evidence about the reference game, not a rule source; use it to understand a player-experience risk, never to import a number.

**1.4 Status vocabulary.** **Specified** means the behaviour is written down and traceable; **test-designed** means a scenario exists but has not run; **document-checked** means an arithmetic or consistency check in `qa_backups/` ran and passed; **runtime-tested** and **playtested** mean what they say and are **not claimed anywhere in this document**.

---

## 2. The approved product commitment (D-122)

**2.1 Global Trade is mandatory scope.** The owner has approved Global Trade as an **approved, mandatory, long-term feature** of Nation Supremacy (D-122, DD-136, REQ-513). The intended complete game includes public sell listings, public buy offers, browsing, filtering and sorting, taker-selected execution, partial fills, reservation and accounting integrity, per-party history, the permitted statistics and the existing fair-play protections. It is not an optional idea, a disposable stretch feature or a speculative possibility.

**2.2 What the commitment does not mean.** It is **feature approval, not release approval**. Five states are separate and must never be collapsed into one sentence:

| State | Current fact | What would change it |
|---|---|---|
| **Feature approved** | **Yes** — D-122 | A new explicit owner-authorized product decision that names D-122 |
| **Design specified** | **Yes** — B-07 v1.1, its register, this document | A later specification prompt with a recorded amendment |
| **Implemented** | **No** — no market code, endpoint, screen or migration exists | A future implementation stage, with code and a deployed test environment |
| **Tested** | **Document checks only** — no runtime, load, concurrency, security or play test | Executed test evidence, recorded with environment and results |
| **Release gates passed** | **No** — G-1, G-2, G-3, G-5, G-6 **not met**; G-4 **partial** | The evidence plan in §10, reviewed by the named owner |

**2.3 The ten commitments that follow from D-122.**

1. Global Trade belongs to the intended complete game.
2. It is not optional, disposable or merely speculative.
3. No future AI session may silently remove it or permanently substitute directed trades as the only trading system.
4. Development may be staged by prerequisites, economic integrity, implementation complexity, test results and the free-first objective.
5. The existing B-07 specification and formula register are the starting point.
6. The approved scope includes public buy offers, public sell listings, browsing, filtering, sorting, execution, partial fills, reservation and accounting integrity, history, suitable statistics, fair-play protections and integration with the nation economy.
7. It remains distinct from private directed nation-to-nation trades.
8. Any proposal to remove, materially downgrade or fundamentally replace it requires a new explicit owner-authorized product decision.
9. Feature approval proves nothing about balance, security, liquidity, infrastructure capacity or release readiness.
10. The decision is propagated into the roadmap, requirements traceability, project summaries and the next-AI handoff.

**2.4 Reversal policy.** A reversal must be a new entry in [DECISIONS.md](../DECISIONS.md) that names D-122, states the evidence, records the product consequence and is explicitly owner-authorized. A schedule slip, a failed gate, a hard implementation or a preference expressed without evidence is **not** a reversal. A failed gate leaves the feature in the roadmap and blocks release (MKT-072).

**2.5 Where the commitment is recorded.** [D-122](../DECISIONS.md) is the authoritative project decision; **DD-136** is the Stage 2 design position; **REQ-513** is the traceable requirement; [B-07 §9](13_trade_and_markets.md) owns the gate definitions; this section owns the five-state distinction; [ROADMAP.md](../ROADMAP.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [AI_CONTEXT.md](../AI_CONTEXT.md) and [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) carry the current summary. None of them may describe Global Trade as implemented, live, ready or released.

---

## 3. Canonical semantics used by every workflow

### 3.1 Actors and states

| Term | Meaning | Owner |
|---|---|---|
| **Account** | The signed-in holder; one active nation per person (D-032) | B-03 |
| **Nation** | The political and economic actor; `active`, `unavailable`, dormant, retired or removed | B-03 |
| **Pair** | The relationship between two accounts/nations: `CLEAR`, `RESTRICTED`, `MAINTAINED` | B-03/D-034 |
| **Leadership state** | `NORMAL`, `ELECTORAL`, `TRANSITION`, `CRISIS`, `SUCCESSION`, `RECOVERY` | B-06 |
| **Directed chain** | The negotiation object; one live revision, one terminal state | B-07 §4 |
| **Listing** | A public sell listing or buy offer with `quantity_posted/filled/locked/remaining` | B-07 §10–§11 |
| **Execution** | One taker's acceptance against a listing; the unit of reservation, settlement and ledger pair | B-07 §15 |
| **Transfer** | The shared `transfer_id` linking the two sides' ledger events | B-04/B-07 §19 |
| **Free space** | `W − total_inventory − space_reserved`; the only capacity figure a fit test may use | B-05/F-TM-025 |

### 3.2 The three balances

Every crown and resource display has three figures: `total`, `reserved`, `available = total − reserved`. A market screen that shows only a total is a specification defect (MKT-053). Reserved units remain in the warehouse and count toward `W`; they are not available for another action. Reserved crowns remain in the treasury and count toward the total; they are not available for another purchase.

### 3.3 One space predicate, used everywhere

The canonical capacity rule is:

```text
free_space(n) = W(n) − total_inventory(n) − space_reserved(n)
fits(n, u)    ⇔  u ≤ free_space(n)
```

`space_reserved` is the sum of every accepted-but-unsettled incoming trade, every locked public execution and every other reservation that will consume space. **It is never added back.** A test that computes `free_space + space_reserved` is testing `W − total_inventory`, ignores every existing promise, and can overbook the warehouse. MKT-095, MKT-129 and MKT-135 were corrected in B-07 v1.1 for exactly this reason.

| Event | `total_inventory` | `space_reserved` | `free_space` |
|---|---|---|---|
| Accept an incoming 100 units | unchanged | `+100` | `−100` |
| Settle those 100 units | `+100` | `−100` | unchanged |
| Cancel or fail before settlement | unchanged | `−100` | `+100` |
| Another trade arrives while the first is reserved | unchanged | `+u` | `−u` |

**Worked check.** `W = 2,000`, inventory `1,950`, no reservations → `free_space = 50`. Two 100-unit purchases arrive in the same turn: the first is rejected (`100 > 50`) and reserves nothing; the second is also rejected. If the first purchase is 40 units, `space_reserved = 40` and `free_space = 10`; the second purchase of 20 units is rejected (`20 > 10`). Settlement of the 40 leaves `inventory = 1,990`, `space_reserved = 0`, `free_space = 10` — the same figure as before settlement, which is the invariant that makes reservation-at-acceptance safe.

### 3.4 Price labels and the fair-value predicate

Four numbers never share a label (MKT-010): **book value** (`P_ref`, B-04), **asking price** (a sell listing), **offer price** (a buy offer) and **completed price** (one settled execution). "Market price" is not used for any of them.

The fair-value rule compares the two sides' **reference values**, not their printed prices:

```text
V_low  = min(V_A, V_B);   V_high = max(V_A, V_B)
V_max  = floor(V_low × (10,000 + B) / 10,000);   B = 3,000
IN_BAND ⇔ V_high ≤ V_max
```

The pair is normalized by value, so reversing the parties cannot change the verdict. `V_low = 0` on exactly one side is `ONE_SIDED`; both zero is `INVALID`. The bound is inclusive. The rule is **asymmetric in percentage terms**: the larger side may be at most 30% bigger than the smaller. `100 vs 130` passes; `70 vs 100` fails, because `floor(70 × 1.30) = 91 < 100`. A screen must say "the larger side is X% bigger" (F-TM-007) and must never print "within ±30%".

### 3.5 Ledger semantics

For a nation, `TRADE_SELL` is the **credit** side of a sale (crowns received, goods given) and `TRADE_BUY` is the **debit** side (crowns paid, goods received), matching B-04's `TRADE_SELL +50`/`TRADE_BUY −30` example. A crown payment appears **once**: on the payer's `TRADE_BUY` event and the payee's `TRADE_SELL` event for the goods it buys. The other leg of a bundle carries `0` crowns. Putting `+200` and `−200` on both sides' two events nets every treasury to zero while the balances move — the defect corrected in E1.

**Worked check (E1 corrected).** Aurelia gives 200 crowns + 100 food, receives 50 steel; Borealis gives 50 steel, receives 200 crowns + 100 food. Aurelia's events: `TRADE_SELL 0 crowns, −100 food`; `TRADE_BUY −200 crowns, +50 steel`. Borealis: `TRADE_SELL +200 crowns, −50 steel`; `TRADE_BUY 0 crowns, +100 food`. Crown sum `0 − 200 + 200 + 0 = 0`; food `−100 + 100 = 0`; steel `+50 − 50 = 0`. Closing balances: Aurelia `800 crowns / 200 food / 50 steel`; Borealis `700 / 100 food / 70 steel`.

### 3.6 Turn phases and timing

Every market action follows B-02's P0–P7 order. The market reads and writes only these points:

| Phase | What the market does | What it must not do |
|---|---|---|
| Open window | accepts a submission, assigns the turn, names the closing time | settle, reserve against a closed turn, or use browser time |
| `LOCKED` | freezes the input; a late action belongs to the next turn | change an accepted action's terms |
| **P2** | re-validates existence, reservations, pair, space and terms against the frozen snapshot | re-apply the political-state test, re-price, or apply a new fair-value verdict |
| **P3** | nothing — production, tax, food and obligations run | let an accepted trade change a P3 result |
| **P4** | settles directed trades first, then Global Trade executions, in `submitted_at`/`action_id` order; writes one ledger pair per trade | settle a trade inside P3, in the browser, or through a second scheduler |
| **P7** | publishes the digest and checks conservation | publish a half-settled trade or a pending trade as complete |

A trade accepted after P3 has begun waits for the next boundary. A trade accepted before `LOCKED` is evaluated against the frozen state at `LOCKED`. There is no continuous matcher, no wall-clock expiry job and no second ledger (MKT-005, MKT-063, MKT-173).

---

## 4. Directed-trade workflows (first playable, fee-free)

Each workflow states the actor, preconditions, steps, player-visible result, persisted state, reservation and ledger effects, turn phase, failure codes and the acceptance tests that cover it. The rules are B-07 §4–§8; this section does not add any.

### W-D01 — Create a directed offer

- **Actor:** the proposer, owning an eligible nation.
- **Preconditions:** turn open; account `ACTIVE`/`ELIGIBLE`; nation `active`, not `unavailable`; pair with the named counterparty not `RESTRICTED`/`MAINTAINED`; counterparty visible; 1–5 lines; each quantity 1…100,000; crowns 0…10,000,000; at most 5 active outgoing chains and 1 chain per pair; 20 actions per 12 turns not exhausted; idempotency key new.
- **Steps:** choose counterparty → add up to five resource lines and/or crowns → see the declared value, reference value and band verdict → confirm → server validates in MKT-036 order → chain `ACTIVE`, revision 1, `expires_turn = now + 72`.
- **Visible:** "Offer sent to <nation>. It reserves nothing until they accept." The screen states the pledge explicitly (MKT-038).
- **Persisted:** one offer object and revision; no crown, resource or space reservation (MKT-037).
- **Ledger:** none.
- **Turn:** creation is immediate (`I` class); it does not wait for a boundary.
- **Failures:** `MKT-E01…E12` for invalid terms, `MKT-L01…L07` for limits, `MKT-A05` for a restricted pair, `MKT-A07` for a fresh out-of-band trade. Nothing is reserved.
- **Tests:** T-D01, T-D02, T-D03, T-D15, T-D16, T-D20.

### W-D02 — View a received offer

- **Actor:** the named recipient (or the proposer viewing its own outgoing chain).
- **Preconditions:** the chain exists and the actor is a party.
- **Visible:** both sides in full — crowns, resources, quantities, unit prices, declared value, reference value, band status, revision, author, expiry turn, settlement rule, and the pledge warning. A third party sees nothing (D-017).
- **Persisted:** none; the read is logged only as an ordinary read, not as a privileged audit read.
- **Tests:** T-D01, T-D20, T-X13.

### W-D03 — Accept an offer (successful)

- **Actor:** the recipient of the live revision.
- **Preconditions:** chain `ACTIVE`/`COUNTERED`; actor is the named recipient; turn open; account/nation eligible; pair clear; leadership state permits the action; both sides cover their own terms from **available** balances; each receiving nation's `free_space` covers the incoming units; fresh verdict `ALLOW`; idempotency key new.
- **Steps:** open the offer → review the re-validation notice → confirm → one transaction checks both sides against current balances, the pair, the recipient's political state and every receiving nation's `free_space` → creates crown, resource and space reservations for both sides → writes the accepted action → chain `ACCEPTED`.
- **Visible:** "Accepted for Turn N; settles at close. Nothing has moved yet." Total, reserved and available are shown for both sides.
- **Persisted:** `status = ACCEPTED`, `acceptance_action_id`, `reservation_refs`, accepted turn.
- **Reservations:** proposer crowns/resources; recipient crowns/resources; incoming space per receiving nation (MKT-052). A side that gives nothing has no crown/resource reservation; a side that receives nothing has no space reservation.
- **Ledger:** none at acceptance.
- **Turn:** accepted in the open window; P2 re-validation; P4 settlement.
- **Failures:** `MKT-A01…A09`; nothing reserved, `failed_accept_count += 1`, chain stays live.
- **Tests:** T-D04, T-D09, T-D13, T-X03.

### W-D04 — Decline an offer

- **Actor:** the recipient.
- **Preconditions:** live chain; actor is the recipient.
- **Steps:** choose a reason code (`MKT-D01…D04`) → confirm.
- **Visible:** the proposer sees "declined — <reason>"; no third party is told. No fee, no penalty, no reputation effect.
- **Persisted:** `status = DECLINED`, reason code, turn.
- **Reservations/ledger:** none; there were none to release.
- **Turn:** immediate.
- **Tests:** T-D05, T-D20.

### W-D05 — Counter or revise an offer

- **Actor:** the party that currently holds the right to accept.
- **Preconditions:** chain `ACTIVE`/`COUNTERED`; fewer than 10 revisions; terms valid; limits valid.
- **Steps:** edit terms → see the new band verdict → confirm → a **new revision** is created, authored by the other party; the previous revision becomes `SUPERSEDED`; `expires_turn` resets to `now + 72`; `failed_accept_count` resets to 0.
- **Visible:** both parties see "revision N"; the previous terms remain readable as history but cannot be accepted.
- **Persisted:** new revision row; `superseded_by` on the old one; chain `COUNTERED`.
- **Reservations/ledger:** none.
- **Failures:** `MKT-E06` for a stale revision, `MKT-E07` at 10 revisions, `MKT-L03`.
- **Tests:** T-D06, T-D12.

### W-D06 — Cancel an offer

- **Actor:** the current author of the live revision.
- **Preconditions:** `ACTIVE`/`COUNTERED`.
- **Visible:** "Offer withdrawn." The counterparty sees no reason field. An `ACCEPTED` chain cannot be cancelled by a player (MKT-029).
- **Persisted:** `status = CANCELLED`.
- **Reservations/ledger:** none; if the chain is already `ACCEPTED`, the action is refused, not silently converted into a release.
- **Tests:** T-D07, T-D18.

### W-D07 — Expiry

- **Actor:** the boundary job, not a player.
- **Preconditions:** `expires_turn < current_turn` and the chain is `ACTIVE`/`COUNTERED`.
- **Steps:** B0 pass in deterministic `(expires_turn, chain_id)` order; idempotent; writes `EXPIRED` with `MKT-D05`; one deduplicated digest line to both parties.
- **Reservations/ledger:** none; an accepted chain cannot expire.
- **Tests:** T-D08, T-O03.

### W-D08 — Stale acceptance

- **Actor:** the recipient attempting to accept.
- **Preconditions:** the proposer no longer has the offered resources/crowns, or the recipient cannot cover its own side, or space is insufficient.
- **Visible:** a specific code (`MKT-A01`/`A02`/`A03`/`A04`) and "nothing moved". `failed_accept_count` rises by 1.
- **Persisted:** failure event; chain stays in its previous state.
- **Reservations/ledger:** none.
- **Tests:** T-D09, T-D10.

### W-D09 — Third failed acceptance → `STALE`

- **Actor:** the recipient's third failed acceptance; the transition is applied in the same boundary.
- **Visible:** "This offer is no longer live." The proposer sees `EXPIRED (STALE)` and can restock or create a new chain.
- **Persisted:** `status = EXPIRED`, `termination_reason = STALE`, `failed_accept_count = 3`.
- **Reservations/ledger:** none.
- **Tests:** T-D10.

### W-D10 — Duplicate or simultaneous requests

- **Actor:** a client retry, a double click or two tabs.
- **Rule:** one idempotency key produces one action and returns the original receipt; a different key with the same terms is a new action and is subject to available quantity and balances.
- **Visible:** the second submission shows the first receipt, not a second reservation or a second settlement.
- **Persisted:** one action, one reservation set, one ledger pair.
- **Tests:** T-D12, T-X11.

### W-D11 — Retry after an interruption

- **Actor:** the recovery process.
- **Rule:** P4 resumes from its checkpoint with the same frozen snapshot and ordering; an action that settled writes its pair once; one that did not is retried; the turn never publishes half a trade.
- **Tests:** T-X11, T-X12.

### W-D12 — Counterparty unavailable, rerolled or removed

- **Rule:** a dormant/retired/removed counterparty cannot be newly addressed; an existing live chain fails at acceptance with `MKT-A08` and becomes `EXPIRED` (`MKT-D07`). An **accepted** trade settles normally because its reservation already exists. A reroll is blocked while an accepted trade is unsettled; open chains are withdrawn.
- **Visible:** "This offer is no longer live" or "You cannot reroll while a trade is settling", named as a blocker, never a hidden timer.
- **Tests:** T-D14, T-X06, T-X08.

### W-D13 — Restricted pair or shared network

- **Rule:** a `RESTRICTED`/`MAINTAINED` pair cannot create, accept or execute; the message is neutral and identical for every restriction cause; the other account's state is not leaked. A shared-network pair is restricted under D-034; a detection gap is a review signal, not a player-visible accusation.
- **Tests:** T-D15, T-X07, T-P07.

### W-D14 — Fresh-nation protection

- **Rule:** a fresh nation (first 360 turns) may not send a one-sided transfer, accept/execute/create an out-of-band trade in either direction, or post an out-of-band public listing. It may trade reciprocally in band, receive a one-sided gift (signal `MKT-S03`), negotiate, decline, cancel and read the market. The check runs at creation, acceptance, posting, execution acceptance and P2 using the acceptance-time verdict.
- **Visible:** the ratio in plain words, the book values used, and the exact failure (`MKT-E08`/`MKT-E09`/`MKT-A07`); no accusation of cheating.
- **Tests:** T-D16, T-P02, T-P04.

### W-D15 — Leadership state `TRANSITION`/`CRISIS`

- **Rule:** the market is **read-only** for new directed actions: the player may read offers, balances, listings and history, but may not create, counter, accept, decline, cancel or create a reservation. An **already accepted** trade settles normally. The screen explains the state; it never presents the restriction as a sanction, tax or fee.
- **Tests:** T-D17, T-X06.

### W-D16 — Balances change between acceptance and P4

- **Rule:** acceptance reserves the exact crowns and units. A later sale, construction, production or tax cannot consume a reserved amount. P2 checks that the reservations still exist and still cover the terms; a missing or short reservation is a failure (`F3`/`F4`), not a silent re-price. P3 cannot use reserved inputs.
- **Tests:** T-D13, T-X03, T-X04, T-X05.

### W-D17 — Warehouse capacity and two incoming trades

- **Rule:** every receiving nation's `free_space` is tested once at acceptance and the incoming units are reserved. Two trades in the same turn cannot both use the same free space. Settlement consumes the reservation and adds the units; cancellation/failure releases it. A P4 space failure means the invariant was already broken and is a defect.
- **Worked check:** §3.3.
- **Tests:** T-D13, T-X02, T-X03.

### W-D18 — P2/P4 failure and rollback

- **Rule:** a P2 failure marks the chain `FAILED`, releases every reservation in the same step and moves nothing. A P4 failure does the same for the whole trade; there is no partial settlement and no partial ledger pair. The digest names the code and the side that could not perform.
- **Visible:** "Failed: <code>; nothing moved."
- **Tests:** T-D18, T-X10.

### W-D19 — Settlement and history

- **Rule:** P4 writes the two legs in one transaction, with one shared `transfer_id`, `TRADE_SELL`/`TRADE_BUY` semantics as in §3.5, and closes every reservation. The parties see the pair and the transfer ID in their own history; a third party never sees the terms.
- **Tests:** T-D19, T-X01, T-X13.

### W-D20 — Limits and anti-spam

- **Rule:** five active outgoing chains, one per pair, ten revisions, five lines, 100,000 units per line, 10,000,000 crowns per side, 20 actions per 12 turns, 50 incoming/outgoing chains per page. A limit rejection happens before any reservation or notification. No bulk acceptance; no automated action.
- **Tests:** T-D20, T-O05.

---

## 5. Global Trade workflows (release-gated, specified in full)

Global Trade is dark until all six gates pass (MKT-076). The workflows below are the intended behaviour after the gate; they are **not** available now. The board is resource-for-crowns only; alliance markets, auctions, futures, loans and automated trading are out of scope (MKT-008).

### 5.1 Public sell listings

**W-G01 — Choose a resource and quantity.** The seller sees only the eleven roster resources, its total/reserved/available for each, and the maximum it may list (`available_units`). A quantity of 0 or a non-integer is rejected. The seller's own listing cannot be executed by itself (MKT-097).

**W-G02 — Enter a unit price and see the total.** Price is an integer ≥ 1 crown per unit; total is `quantity × price`, checked for overflow; the screen labels it "asking price" and "total if fully filled", and shows book value beside it with the difference. There is no price floor or ceiling; the fair-value band governs who may execute, not what may be asked (MKT-142).

**W-G03 — Validate before submission.** The server checks: actor owns the nation; account/nation eligible; leadership state permits; resource tradable; quantity 1…100,000; price 1…100,000; `available_units ≥ quantity`; active-listing caps (4 per resource, 12 total per nation); fresh-nation posting band; idempotency key. Failure returns `MKT-L08`/`MKT-E08`/`MKT-A03` and reserves nothing.

**W-G04 — Reserve the listed units.** Posting moves `quantity_posted` from available to reserved. The units stay in the warehouse, count toward `W`, and cannot be sold, consumed, traded or listed again. No crowns are reserved. This is the scoped exception to D-016 (D-110/MKT-079).

**W-G05 — Publish and discover.** The listing becomes `OPEN` with `expires_turn = created_turn + 72`. It shows resource, remaining quantity, asking price, total, created/expiry turns, seller's public nation label and status. It never shows treasury, warehouse, other listings, account identity, network state, sanction state or a restriction reason (MKT-087).

**W-G06 — Preview and confirm an execution.** A taker selects a listing, chooses `1 ≤ x ≤ quantity_remaining`, and sees `x × price`, the remaining after the fill, its available crowns, the receiver's free space, and the settlement turn. The confirmation says the price is the seller's posted price and that no automatic matching occurs. If the offer changed since it was displayed, the server re-reads it and either applies the new remaining quantity or rejects with `MKT-A10`; the taker never executes terms it did not see.

**W-G07 — Partial fill.** The taker's crowns and space are reserved; the maker's listing splits `x` into `quantity_locked` and leaves the rest `quantity_remaining`; `reserved_units = locked + remaining`. At P4 the taker pays `T = x × price`, the maker delivers `x`, the space reservation is consumed, `filled += x`, `locked −= x`, and the maker's remaining reservation falls by exactly `x`.

**W-G08 — Adjust remaining quantity.** After each settlement the board shows `quantity_remaining = posted − filled − locked`; it never shows `posted − filled` as available, because that would include locked units (MKT-128).

**W-G09 — Full fill.** When `remaining = 0` and `locked = 0` the listing is `FILLED`; the maker's reservation is zero. A full fill closes exactly once; a duplicate execution is rejected by the idempotency key, not by a second settlement.

**W-G10 — Cancel.** The maker may cancel while `OPEN`/`PARTIALLY_FILLED`. Cancellation releases `quantity_remaining` immediately and leaves `quantity_locked` untouched; the listing becomes `CANCELLED` with `locked_remainder = true` and closes when the last locked execution resolves. A cancelled listing cannot be re-opened by a failed execution; released units return to the maker's available balance.

**W-G11 — Expiry.** At `expires_turn` the B0 job releases `quantity_remaining`, leaves `quantity_locked` to settle, and marks the listing `EXPIRED`. The board shows it closed, never available. A listing cannot be extended; the maker posts a new one.

**W-G12 — Failure and recovery.** A P2/P4 failure releases all three reservations, moves nothing, returns `x` from locked to remaining if the listing is still open, and marks the execution `FAILED`. If the listing was cancelled/expired, the units/crowns return to the maker's available balance. The taker sees the code; the maker sees "an execution failed and the remainder was released".

**W-G13 — Per-party history.** Each party sees its own listing, executions, fills, cancellations, failures, ledger pair and `transfer_id`; the public board never becomes a per-trade feed (MKT-143/MKT-192).

**W-G14 — Suspension.** An administrative suspension blocks new executions, keeps existing locks, records the reason only in restricted audit, and shows "temporarily unavailable". It is not a confiscation; the units remain the seller's. A default suspension does not fail an already accepted execution (MKT-089/MKT-130).

**W-G15 — Seller's own listing.** The maker cannot execute its own listing, directly or through a second account (MKT-097, D-034). The rejection is neutral.

### 5.2 Public buy offers

**W-G16 — Resource, quantity, price and total.** The buyer chooses a resource, a quantity 1…100,000 and a maximum unit price 1…100,000; `crown_commitment = quantity × price`; the total is checked for overflow and must be ≤ available crowns.

**W-G17 — Treasury and space requirements.** Posting reserves the full crown commitment; it does not reserve warehouse space, because the buyer does not know who will deliver or when. Each execution checks the buyer's `free_space` at acceptance and reserves the incoming units (MKT-095). A buy offer may never advertise purchasing power it has not reserved.

**W-G18 — Publish, discover, select.** The buy offer appears on the same board as sell listings, with the offer price, remaining quantity, total commitment, buyer's public label, expiry and status. A seller selects it; the buyer cannot select a seller.

**W-G19 — Full or partial fulfillment.** A seller executes `1 ≤ x ≤ remaining`; `x` units are reserved on the seller, `x × price` of the buyer's crown reservation is locked, and `x` moves from remaining to locked. At P4 the buyer pays `x × price`, receives `x`, the seller receives the crowns and gives the units; the buyer's remaining crown reservation falls by exactly `x × price`.

**W-G20 — Adjust remaining quantities and reservations.** `quantity_remaining = posted − filled − locked`; `reserved_crowns = (locked + remaining) × price`; `crown_commitment` is fixed at posting. The two identities must reconcile after every fill.

**W-G21 — Cancel and expiry.** Cancellation releases `remaining × price` immediately; locked crowns stay reserved until their executions settle or fail. Expiry does the same. A closed buy offer cannot be executed again; a failed execution's crowns return to available, not to the closed offer.

**W-G22 — History, privacy and audit.** The buyer sees its own commitment, fills, locked remainder and ledger pairs; the seller sees its own execution; the public board shows only the offer's public terms.

### 5.3 Discovery and player experience

**W-G23 — Board and filters.** One board for both sides; filter by resource, side, price range and quantity; sort by price, newest, expiry or remaining quantity; a stable secondary sort; cursor pagination with an exact count; at most 50 rows per page. A filter that does not change what can be executed is a defect (MKT-016).

**W-G24 — Empty, crossed and low-liquidity states.** An empty board says "no listings match" and offers to post one; it never invents a price. A crossed book (a buy offer at or above the lowest sell ask) is **shown** with both prices and a warning, but is **not auto-crossed**; a taker must choose. A low-volume resource shows `INSUFFICIENT_SAMPLE` rather than a misleading average.

**W-G25 — Price reference.** The board shows book value, the asking/offer price and, where a completed price exists, the last completed price with its window and sample. It never labels any of them "market price" and never implies that a listed price will fill automatically.

**W-G26 — Restricted or blocked trade.** A restricted pair sees a neutral message and the review route; the other account's state, the reason and the enforcement evidence are not disclosed. A fresh-nation block states the band and the values, not an accusation.

**W-G27 — Execution changed under the taker.** If the listing's remaining quantity, price or status changed between display and confirmation, the server re-reads it. A smaller remaining quantity may be partially executed only if the taker explicitly chose the smaller amount; otherwise the action fails with `MKT-A10` and reserves nothing. A cancelled, expired or suspended listing fails the same way.

**W-G28 — Statistics.** Before the gate, no public statistic exists. After the gate, a 12-turn VWAP and volume band publish only with at least five trades and five nations, with complementary suppression; a 4-nation sample is withheld. A statistic is labelled with its window and sample or not shown (MKT-195–203).

**W-G29 — Fees.** At launch both directed and global fees are zero; no fee is invented for 07C. A future fee requires a decision, a payer, a `FEE` event, a conservation identity and a G-5 record (MKT-068–070).

**W-G30 — Gate state.** Before G-1…G-6 pass, every Global Trade route returns a neutral "not available"; there is no hidden table, client flag, read-only preview or beta board. A crafted request must not reach a listing.

---

## 6. Cross-system integration

The market owns no resource, balance, turn phase, account state or political rule. The table names the owner and the exact interface; a mismatch is a defect in the market, not a licence to redefine the other system.

| System | Owner | What the market reads | What the market writes | Failure codes | Tests |
|---|---|---|---|---|---|
| Turn phases | B-02 | open/locked, current turn, frozen snapshot, P2/P4/P7 | accepted action with turn ID; settlement at P4; digest at P7 | `F1`…`F10` | T-X04, T-X11, T-X14 |
| Account, nation, pair | B-03 | account state, nation state, pair state, reroll state, shared-network flag | nothing to the account; a pair restriction is read, never created | `MKT-A05`, `F3` | T-X06, T-X07, T-X08 |
| Treasury, inventory, ledger | B-04 | total/reserved/available crowns and units; book values; warehouse `W` | reservations; `TRADE_SELL`/`TRADE_BUY` pair with one `transfer_id`; no mint, no burn | `MKT-A01…A04`, `F3`, `F4` | T-X01, T-X02, T-X10, T-X12 |
| Capacity and warehouse | B-05 | `W`, total inventory, space reservations | no capacity change; a trade cannot create space | `MKT-A04`, `F4` | T-X02, T-X03 |
| Leadership state | B-06 | `NORMAL`/`ELECTORAL`/`TRANSITION`/`CRISIS`/`SUCCESSION`/`RECOVERY` | no political effect, no tax, no embargo, no stability change | `MKT-A06` | T-D17, T-X06 |
| Diplomacy | Prompt 08 (future) | nothing at launch; no treaty, sanction or embargo rule exists | nothing at launch | — | T-X09 |
| Alliances | Prompt 09 (future) | nothing; an alliance treasury is **not** a Global Trade wallet | nothing | — | T-X09 |
| Warfare | Prompt 10 (future) | nothing; Operations Points are never tradable | nothing | — | T-X09 |
| Privacy, administration | Prompt 12 / B-12 | restricted pair and suspension flags; privileged-read policy | signal records; a narrow suspension; no ban or confiscation | `MKT-A05`, `MKT-S10` | T-P07, T-P08, T-X13 |
| Screens and journeys | Prompt 13 (future) | field lists and state names from this document | nothing | — | T-G14, T-G15 |
| Balance and calibration | Prompt 14 (future) | UD-037/UD-038; provisional constants | nothing | — | T-O01, T-S03 |

**6.1 Explicit non-interfaces.** The market does not create a tax, tariff, embargo, war effect, alliance wallet, research point, development capacity, grid unit, housing unit, political influence or Operations Point transfer. It does not read a player's private messages or IP address for ordinary matching. It does not create a second scheduler, a continuous daemon, a webhook or a bot API. It does not let an administrator move units between nations.

**6.2 Interface rule.** If a future prompt needs a new field from another system, it adds the field to that system's contract and records the dependency here; it does not infer the field from a screen. If a field is missing, the market fails closed and reports the missing dependency.

---

## 7. Edge-case walkthroughs

These extend B-07 §26 with the cases Prompt 07C was asked to settle. Each is a specification scenario, not an executed test.

**X-01 — Counteroffer arriving after acceptance.** A and B negotiate; B counters; A accepts revision 2. A revision 3 arrives from B in the same open window. Because only one revision is live (MKT-024), revision 3 supersedes revision 2 **before** acceptance or is refused afterwards; an acceptance naming revision 2 fails `MKT-E06`, and revision 3 is a new proposal that must be accepted separately. The accepted revision's reservations are not released by a later counteroffer.

**X-02 — Listing suspended mid-execution.** A taker's execution was accepted before the suspension. The default suspension blocks new executions only; the accepted one keeps its locks and settles at P4 (MKT-130). The seller sees "temporarily unavailable"; the taker sees the existing receipt. A suspension that explicitly names accepted executions must say so in the privileged record; otherwise it is a defect.

**X-03 — Reroll in the same turn as an accepted trade.** The reroll pre-check finds an accepted, unsettled trade and refuses the reroll, naming the blocker. If the trade is `ACTIVE`/`COUNTERED` only, the reroll proceeds, the open chains are withdrawn, the counterparties see `MKT-A08`, and the pair records survive. No value leaks from the old nation; the replacement is fresh from its own creation turn.

**X-04 — Warehouse expansion in the same turn as an incoming execution.** Acceptance reserved space against the old `W`; if the expansion completes at P3, the new `W` only increases free space at P4. The reservation is still valid, the units fit, and no positive reservation is released merely because `W` grew. If the expansion is cancelled, the old `W` still covers the reservation; if it does not, the invariant was broken and the failure is a defect.

**X-05 — P2 failure after a cancellation.** A maker cancels the unlocked remainder; a locked execution later fails at P2. The released units return to the maker's **available** balance, not to the cancelled listing; the listing stays `CANCELLED`; the taker sees the failure code; the maker sees the release line. No double release.

**X-06 — Duplicate request across a recovery.** P4 is interrupted after the trade's reservation was consumed but before the digest. Recovery replays the same frozen input and the same `action_id`; the ledger pair's `event_key` is already present, so the retry is a no-op; the digest is written once. A second client submission with the same idempotency key returns the original receipt; a different key is a new action and is subject to available quantity.

**X-07 — Statistic crosses the 5-nation threshold between turns.** Turn N has four distinct nations → `INSUFFICIENT_SAMPLE`, no average. Turn N+1 has five → the statistic is published with its window and sample. The change is not retroactive; the turn-N row remains withheld. Complementary suppression still applies if one nation dominates the volume; a single-nation "average" is never published.

**X-08 — Crossed book.** A buy offer at 9 and a sell ask at 8 coexist. The board shows both and a crossed-book badge; no automatic trade occurs. A taker may execute the sell at 8 (the seller's posted price) or the buy at 9 (the buyer's posted price); the difference is not captured by the system, and the interface does not promise a midpoint. This is the accepted cost of D-111.

**X-09 — Mature out-of-band trade.** A mature seller sells 10 uranium (book 300) for 600 crowns to a mature buyer. The band verdict is `OUT_OF_BAND`, but the trade is allowed and records `MKT-S01`; the confirmation shows the premium and the realised gap. No sanction, no block, no public flag. For a fresh party the same trade is rejected at creation/acceptance with `MKT-E08`/`MKT-A07`.

**X-10 — One-sided receive by a fresh nation.** A mature ally sends 100 food to a fresh nation for nothing. `V_low = 0`, the fresh nation is the receiver → allowed with `MKT-S03`. The reverse (fresh sends for nothing) is rejected with `MKT-E09`. The review signal records the residual route disclosed in MKT-149; the rule does not claim to close it.

**X-11 — Two incoming trades and one warehouse.** `W = 1,000`, inventory `900`, free `100`. Trade A reserves 60; free becomes 40. Trade B for 50 is rejected at acceptance (`50 > 40`), not at P4. If A settles first, inventory becomes 960, the A reservation is consumed, and free remains 40; B still cannot fit. If A is cancelled, free returns to 100 and B can be accepted in a later turn. The order of settlement never creates space.

**X-12 — Buy offer fills from two sellers.** Buyer posts 400 at 2 = 800 reserved. Seller 1 executes 150: locked 150, remaining 250, reserved `(150 + 250) × 2 = 800`; at P4 buyer pays 300, reserved becomes `250 × 2 = 500`. Seller 2 executes 100: locked 100, remaining 150, reserved `(100 + 150) × 2 = 500`; at P4 pays 200, reserved `150 × 2 = 300`. Every step reconciles; the buyer never advertises more than it reserved.

**X-13 — Failed execution after a partial fill.** A sell listing of 500 has filled 200 and has 300 remaining. A taker executes 100; the execution fails at P4. The 100 returns from locked to remaining (listing still open), all three reservations are released, and the listing returns to 300 remaining / 200 filled. No ledger pair is written; the failure event is the only lasting record.

**X-14 — Political state changes after acceptance.** A trade is accepted while the recipient is `NORMAL`; the recipient enters `TRANSITION` before P4. The accepted trade settles normally; the state restricts **new** actions only. A new acceptance attempted during `TRANSITION` fails `MKT-A06`. The screen explains the state without calling it a sanction.
---

## 8. Acceptance-test catalogue

**8.1 How to read a test.** `Type` is **S** (specification scenario — a written behaviour a later implementation must satisfy), **A** (arithmetic/document check that exists in `qa_backups/` and runs today), **R** (future runtime test, requiring an implementation and a test environment) or **P** (future controlled playtest or simulation, requiring players or a model). A row may carry more than one type. **No R or P test has run.** The `A` checks are the only executed evidence in this prompt, and §14 records their output.

**8.2 Every required scenario is present.** The catalogue covers the 36 cases named in the Prompt 07C brief: valid/invalid creation, no reservation at creation, acceptance reservation, no partial directed fill, decline/cancel/expiry, underfunded stale, duplicate acceptance, two actions on one asset, sell reservation, buy reservation, partial/full fill, cancellation/expiry release, capacity, overbooking, simultaneity, restricted pair, shared network, fresh boundaries, fair value, zero reference, reroll, political state, P3 non-interference, P4 ordering/idempotency, statistics, low liquidity, crossed offers, no auto-match promise, fees, failed execution, error-message privacy, audit reconstruction and reconciliation.

### 8.3 Directed-trade tests

| ID | Rules | Precondition | Action | Expected result | Type |
|---|---|---|---|---|---|
| T-D01 | MKT-018…023, 036 | Two mature, unrelated eligible nations; both hold the offered goods | A creates a valid offer of 100 food for 200 crowns | `ACTIVE`, revision 1, expiry `now+72`; no reservation; both see declared and reference values | S, R |
| T-D02 | MKT-022, 036, 041, 059–062 | As T-D01 | Submit zero/empty terms, 6 lines, 100,001 units, 10,000,001 crowns, a non-roster resource, or an 11th action past the limit | Rejected with the specific `MKT-E*`/`MKT-L*`; no reservation; no notification | S, R |
| T-D03 | MKT-037, 038 | Offer created | Spend the offered food on another action before acceptance | The offer stays `ACTIVE`; no reservation existed; the creation screen never said "guaranteed" | S, R |
| T-D04 | MKT-039, 040, 044, 046, 052–054 | Valid live offer; both sides funded; receiver's `free_space` sufficient | Recipient accepts in the open window | `ACCEPTED`; crown/resource reservations for both sides; space reserved on each receiver; no ledger; assigned turn shown | S, R |
| T-D05 | MKT-028 | Live offer | Recipient declines with `MKT-D02` | `DECLINED`; no fee, balance change, penalty or third-party notice; proposer sees the code | S, R |
| T-D06 | MKT-024, 025, 027, 045 | Live offer | Recipient counters with new terms, then the other party accepts revision 2 | Revision 2 live, revision 1 `SUPERSEDED` and unacceptorable (`MKT-E06`); expiry reset; count reset | S, R |
| T-D07 | MKT-029 | Live offer, no acceptance | Current author cancels | `CANCELLED` immediately; nothing released because nothing was reserved; an `ACCEPTED` chain refuses cancellation | S, R |
| T-D08 | MKT-030, 063, 064 | `expires_turn = 10`; current turn 10 | Run the B0 pass at the next boundary | `EXPIRED` once, idempotently; one digest line per party; no reservation release | S, R |
| T-D09 | MKT-040, 041, 042 | Offer for 100 food; proposer now has 40 available | Recipient accepts | `MKT-A01`; nothing reserved or moved; `failed_accept_count = 1`; chain still `ACTIVE` | S, R |
| T-D10 | MKT-047, 048 | As T-D09 | Fail acceptance three times on unchanged terms | Third failure moves the chain to `EXPIRED` with `MKT-D06 (STALE)`; proposer sees why | S, R |
| T-D11 | MKT-026, 034 | Accepted directed trade for 50 units | Taker asks to settle 25 instead | Refused: directed trades are atomic and have no partial fill; the accepted terms settle whole at P4 | S, R |
| T-D12 | MKT-014, 045, 169 | Accepted trade | Resubmit acceptance with the same idempotency key, then with a new key | Same key returns the original receipt and one reservation; new key fails `MKT-A08` or is a new action | S, R |
| T-D13 | MKT-015, 053, 135 | One nation has 100 crowns available; two offers each need 80 | Accept both in the same window | First reserves 80; second fails `MKT-A03`; no negative or double-committed balance | S, R |
| T-D14 | MKT-043, 049, 050 | Accepted, unsettled trade | Attempt a reroll; separately, let a live counterparty become dormant | Reroll blocked with the named trade; live chain to a dormant nation fails `MKT-A08` and expires; the accepted trade still settles | S, R |
| T-D15 | MKT-036, 040, 041; D-034 | Pair `RESTRICTED` or shared-network flagged | Create/accept/execute | Neutral refusal (`MKT-A05`); no leakage of the other account's state or the reason | S, R |
| T-D16 | MKT-146…156 | One party fresh (<360 turns) | (a) in-band reciprocal; (b) out-of-band either direction; (c) one-sided send; (d) one-sided receive | (a) allowed; (b) rejected `MKT-E08`/`MKT-A07`; (c) rejected `MKT-E09`; (d) allowed with `MKT-S03` | S, A, R |
| T-D17 | MKT-051 | Recipient in `TRANSITION` or `CRISIS` | Read the market; try create/counter/accept/decline/cancel | Reads succeed; mutations fail `MKT-A06`; no fee/sanction wording; an already accepted trade settles | S, R |
| T-D18 | MKT-055, 057, 170 | Accepted trade; inject a missing reservation at P2, then a P4 failure | Run P2/P4 | `FAILED`; every reservation released once; nothing moved; one failure event; no resurrection | S, R |
| T-D19 | MKT-056, 163, 165, 166 | Accepted trade as E1 | Settle at P4 | Four events, one `transfer_id`, crown sum 0, each resource sum 0, closing balances `800/200/50` and `700/100/70` | S, A, R |
| T-D20 | MKT-018, 053, 186–194 | Two parties with history | View own history; attempt to read a third party's chain | Parties see terms and ledger pair; third party sees nothing; public board has no directed terms | S, R |

### 8.4 Global Trade tests

| ID | Rules | Precondition | Action | Expected result | Type |
|---|---|---|---|---|---|
| T-G01 | MKT-078…081 | Seller has 800 steel, 0 reserved | Post 500 at 8 | `OPEN`; 500 reserved, 300 available; no crowns reserved; total 4,000 | S, R |
| T-G02 | MKT-083, 128, 131 | Listing from T-G01 | Taker executes 200 | 200 locked, 300 remaining, 500 reserved; taker reserves 1,600 crowns + 200 space; at P4 filled 200, reserved 300 | S, R |
| T-G03 | MKT-128, 131, 134 | Listing with 300 remaining | Execute 300 | `FILLED`; remaining/locked 0; reservation 0; one ledger pair; second execution fails `MKT-A10` | S, R |
| T-G04 | MKT-085, 133 | Listing 500, 200 locked | Cancel the unlocked remainder | Remaining 300 released immediately; locked 200 settles; listing `CANCELLED` then closes | S, R |
| T-G05 | MKT-086, 134 | Listing with 200 remaining and 100 locked at expiry | Run B0 | 200 released to seller; 100 locked settles; listing `EXPIRED`; no extension | S, R |
| T-G06 | MKT-090, 091 | Buyer has 1,000 crowns, free space 100, 0 food | Post 400 food at 2 | 800 crowns reserved, 200 available; no space reserved; commitment 800 | S, R |
| T-G07 | MKT-093, 128, 131 | Buy offer from T-G06 | Seller executes 150 | Locked 150 / remaining 250 / reserved 800; at P4 buyer pays 300, reserved 500, food 150 | S, R |
| T-G08 | MKT-094 | Buy offer with 250 remaining, 150 locked | Cancel | 500 crowns released immediately; 300 locked remain; `CANCELLED`; no re-open | S, R |
| T-G09 | MKT-129 | Listing live | Attempt execution with an ineligible actor, own listing, zero/over-remaining quantity, insufficient crowns, insufficient space, restricted pair, or stale idempotency key | The first failing check returns its code; nothing reserved; no partial state | S, R |
| T-G10 | MKT-097 | Actor owns the listing | Execute it; then try via a linked second account | `MKT-E10`; the second route is a pair restriction/review signal | S, R |
| T-G11 | MKT-115…126 | Buy offer 9, sell ask 8 | Open the board and execute one side | Both shown with a crossed-book badge; **no automatic trade**; the taker gets the chosen posted price | S, P |
| T-G12 | MKT-126, 133 | Taker displayed 300 remaining; another taker fills 250 first | Confirm the original 300 | Server re-reads; `MKT-A10` (insufficient remaining) and no reservation, or an explicit smaller amount if the taker chose it | S, R |
| T-G13 | MKT-089, 130 | Execution accepted; listing suspended | Run P2/P4 | Default suspension blocks new executions only; the accepted one settles; public sees "temporarily unavailable" | S, R |
| T-G14 | MKT-105…114 | 60 mixed listings | Filter/sort/paginate | One board, stable sort, cursor pages, exact count, ≤50 rows, no unbounded query | S, R |
| T-G15 | MKT-105…114 | Empty board / one listing / 4-nation sample | View each | "No listings match"; no invented price; `INSUFFICIENT_SAMPLE`; no misleading average | S, P |
| T-G16 | MKT-195…203 | 4 nations, then 5 | Request the statistic | 4 → withheld; 5 → published with window/sample; complementary suppression; no retroactive change | S, R |
| T-G17 | MKT-071…077 | Gates unmet | Call every Global Trade route, including a crafted request | Neutral "not available"; no listing table, flag, preview or beta board is reachable | S, R |
| T-G18 | MKT-204…207 | 12 active listings; 5 on one resource | Post another | `MKT-L*`; no reservation; limits visible before submission | S, R |
| T-G19 | MKT-068…070 | Any trade or execution | Settle | `fee = 0`; no `FEE` event; no hidden charge; future fee would need a decision and a new identity | S, A |
| T-G20 | MKT-128, 131, 165, 186+ | Two partial fills and a failure | Reconstruct the listing | `posted = filled + locked + remaining`; reserved = locked + remaining; one ledger pair per execution; history private to the parties | S, R |

### 8.5 Cross-system, price, operations and governance tests

| ID | Rules | Precondition | Action | Expected result | Type |
|---|---|---|---|---|---|
| T-X01 | MKT-163…167 | Any successful/failed trade | Recompute the ledger | Crown sum 0 (or +fee); each resource sum 0; no negative total; reservation identities hold | S, A |
| T-X02 | MKT-013, 054, 095, 129, 135; F-TM-025 | `W=2,000`, inventory 1,950, no reservations | Accept 100, then 40, then 20 | 100 fails; 40 reserves and leaves 10 free; 20 fails; settlement leaves free 10 | S, A |
| T-X03 | MKT-052, 127, 135 | Two incoming trades for 60 and 50, free 100 | Accept both | 60 accepted (free 40); 50 rejected; no overbooking; cancel/fail restores free | S, A |
| T-X04 | MKT-033, 173–178 | Open turn | Submit before and after `LOCKED`; interrupt P4 | Current turn vs next turn assignment; P4 resumes once; no half trade; no browser timing | S, R |
| T-X05 | MKT-035, 174 | P3 produced the goods being sold | Settle at P4 | P3's tax/food/production result is unchanged; received inputs affect the next turn only | S, R |
| T-X06 | MKT-051, 179–185 | `TRANSITION`, `CRISIS`, dormant, removed | Read/mutate | Reads and accepted settlements allowed; new mutations fail with the correct code; no fourth status invented | S, R |
| T-X07 | MKT-036, 040, 179–185; D-034 | Restricted/shared-network pair | Every market route | All mutations blocked; identical neutral message; no inference channel; signal on a detection gap | S, R |
| T-X08 | MKT-050, 152 | Open and accepted chains | Reroll | Blocked while accepted/unsettled; open chains withdrawn; pair survives; replacement fresh | S, R |
| T-X09 | MKT-008, 099–104 | Alliance treasury, Operations Points | Attempt a trade | Alliance wallet is not a market wallet; OP is not tradable; no invented war/diplomacy effect | S, R |
| T-X10 | MKT-034, 057, 170 | Inject a P4 failure mid-trade | Retry | Whole trade fails; all reservations released once; no partial ledger pair; balances identical to pre-acceptance | S, R |
| T-X11 | MKT-014, 169, 178 | Duplicate delivery and recovery | Replay | One action, one pair, one digest; different key is a new action | S, R |
| T-X12 | MKT-166, 171 | Completed/failed turn | Reconstruct from the audit spine | Every action, reservation, release, pair and quantity identity recoverable; no cache dependence | S, R |
| T-X13 | MKT-186…194 | Directed/global history | Read as party, third party, administrator | Party sees terms; third party sees public terms only; privileged read is logged; no raw IP/session leakage | S, R |
| T-X14 | MKT-005, 033, 063, 173 | Any action | Inspect the scheduler | Exactly one B-02 scheduler; no second clock, daemon or continuous matcher; expiry is a B0 pass | S, A |
| T-P01 | MKT-010, 136–143 | Listing/trade screens | Inspect labels | Book value, asking/offer price, completed price, total are distinct; "market price" absent | S, R |
| T-P02 | MKT-144, 145; F-TM-005/006 | `V_low=100` | Test 129/130/131, reversed 130/100, 70/100, 0/100, 0/0 | In/in/inclusive, in, out, one-sided, invalid; the band is described as a ratio, never ±30% | S, A |
| T-P03 | MKT-146…156 | One side zero | Test both directions and fresh/mature | One-sided send vs receive; fresh block vs mature signal; both-zero invalid | S, A, R |
| T-P04 | MKT-147, 148, 154 | Turn 359/360/361; listing posted fresh | Execute after maturity | 359 fresh, 360 not; posting/execution use the execution-time age; no retroactive fail | S, A, R |
| T-P05 | MKT-155, 157–162 | Mature out-of-band | Settle | Allowed, `MKT-S01`, neutral confirmation, audit record, no sanction/confiscation/public flag | S, R |
| T-P06 | MKT-195…203; D-027 | 4 nations / 5 nations / one dominant nation | Request the statistic | Withheld / published / suppressed; minimum cohort and complementary suppression unchanged | S, R |
| T-P07 | MKT-018, 186–194; D-017 | Directed chain | Third-party read | Nothing; no inferred existence; no private note; public listing shows only its own terms | S, R |
| T-P08 | MKT-160…162, 171 | Signal/case | Review and close | Evidence retained per class; no ban/confiscation by the market; privileged acts logged; appeal path exists | S, R |
| T-O01 | MKT-208…213 | A projected action mix | Count logical reads/writes per action | Bounded per action; one page per board read; no unbounded scan; estimate is labelled a placeholder | S, A |
| T-O02 | MKT-065, 105–114 | 50+ rows | Page through | Cursor pagination; exact count; stable order; no unbounded query | S, R |
| T-O03 | MKT-063, 086, 134 | Expiries at one boundary | Run twice | Deterministic order, idempotent, one release, one digest line | S, R |
| T-O04 | MKT-120, 204–213 | 5,000 executions in one turn | Submit the 5,001st | `MKT-L14`; no reservation; guard is a disclosed placeholder for Stage 3 | S, R |
| T-O05 | MKT-059–067, 204–207 | Caps reached | Submit | Visible, server-enforced ceilings; rejection before reservation; no reward for waiting | S, R |
| T-O06 | MKT-162, 194 | Signal/audit record | Inspect retention | 12 months class O, no raw IP/session, permanent spine keeps mutations and privileged acts | S, R |
| T-S01 | MKT-001–008 | Any implementation task | Check authority | B-07 owns rules; this document owns workflows/tests; no second rulebook | S, A |
| T-S02 | MKT-007, 008 | A design choice | Trace it to 07A | Evidence class and limitation recorded; no reference-game formula copied as a rule | S, A |
| T-S03 | MKT-003, 004, 072–077; D-122 | Any status summary | Read feature/gate state | Mandatory feature; designed; not implemented; gates unchanged; no readiness claim | S, A |
| T-S04 | MKT-077, 233 | A summary or handoff | Search for "ready/live/beta/implemented" | Absent unless the code and gates exist; the correct phrase is "designed; release-gated" | S, A |
| T-S05 | MKT-231…235 | 07C completion | Check roadmap/handoff/log | 07C complete, 08 next, historical records preserved, no restart of 07B | S, A |

### 8.6 Failure-code tests

The 35 rows of B-07 §26 are the canonical failure list. Each row gets a test that asserts the final state, the release of every reservation, the absence of a ledger pair and the player-visible code. The mapping is:

| Test | Failure family | What it asserts |
|---|---|---|
| T-F01 | `MKT-E01…E12` (creation/validation) | No chain, no reservation, one event, stable code |
| T-F02 | `MKT-A01…A04` (counterparty/own side/space) | No reservation on a failed acceptance; `failed_accept_count` increments; chain live |
| T-F03 | `MKT-A05…A07` (pair/politics/fresh) | Neutral message; no state change; no leakage |
| T-F04 | `MKT-A08…A10` (stale/duplicate/remaining) | Original receipt or clean refusal; no second action |
| T-F05 | `MKT-L01…L17` (limits) | Rejection before reservation/write/notification |
| T-F06 | `MKT-D01…D07` (termination) | Terminal state and reason; no resurrection |
| T-F07 | `MKT-G01` (gate) | Dark route; no listing access |
| T-F08 | `F3` (eligibility) | Reservation released once; no movement; digest names the side |
| T-F09 | `F4` (space, invariant defect) | No silent overbooking; release; defect recorded |
| T-F10 | `F8`/`F9` (recovery/idempotency) | One settlement, one pair, one digest; no partial state |

---

## 9. MKT rule coverage matrix

**9.1 The rule set.** B-07 v1.1 contains **237** `MKT-` rules: `MKT-001…MKT-235`, plus `MKT-215a` and `MKT-215b`. Every one appears exactly once below. `System` is **D** (directed), **G** (Global Trade), **B** (both) or **X** (cross-cutting/meta). `Primary tests` names the catalogue case(s) that exercise the rule; `Support` marks a rule that is a definition, rationale or document-control statement and is verified by inspection plus the cited test rather than by a standalone player action. The checker `qa_backups/verify_market_workflows.py` recomputes this table: it fails if a rule is missing, duplicated, unknown, or mapped to a test that is not defined in §8.
| Rule | Title | System | Primary tests | Kind |
|---|---|---|---|---|
| `MKT-001` | What this document owns | X | T-S01 | Support |
| `MKT-002` | What this document does not own | X | T-S01 | Support |
| `MKT-003` | The two systems and the product requirement | X | T-S03 | Rule |
| `MKT-004` | Three statements that must all remain true | X | T-S03 | Support |
| `MKT-005` | No second clock, no second ledger | X | T-X14 | Support |
| `MKT-006` | No retroactive economic change | X | T-S01 | Support |
| `MKT-007` | How the research was used | X | T-S02 | Support |
| `MKT-008` | Deliberately out of scope | X | T-S02 | Support |
| `MKT-009` | Production first, trade second | B | T-X01, T-X02 | Support |
| `MKT-010` | What a price is, and what it is not | B | T-X01, T-X02 | Support |
| `MKT-011` | Integer crowns and units | B | T-X01, T-X02 | Support |
| `MKT-012` | No debt, no credit, no overdraft | B | T-X01, T-X02 | Support |
| `MKT-013` | Warehouse space is real | B | T-X02 | Rule |
| `MKT-014` | Atomicity and idempotency | B | T-D12 | Rule |
| `MKT-015` | Reservation before spending | B | T-D13 | Rule |
| `MKT-016` | Every displayed lever changes an outcome | B | T-D20 | Support |
| `MKT-017` | The market is server-authoritative | B | T-X01, T-X02 | Support |
| `MKT-018` | Directed-trade definition | D | T-D01, T-D02 | Rule |
| `MKT-019` | One leg of a trade is a side | D | T-D01, T-D02 | Support |
| `MKT-020` | A trade with an empty side is a gift | D | T-D01, T-D02 | Rule |
| `MKT-021` | Two values, two jobs | D | T-D01, T-D02 | Rule |
| `MKT-022` | At least one side must give something, and the quantities must be plausible | D | T-D01, T-D02 | Rule |
| `MKT-023` | The offer object | D | T-D01, T-D02 | Support |
| `MKT-024` | One live revision at a time | D | T-D06, T-D08 | Rule |
| `MKT-025` | A counteroffer is a new proposal, not an amendment | D | T-D06, T-D08 | Rule |
| `MKT-026` | The lifecycle states | D | T-D11 | Support |
| `MKT-027` | Permitted transitions | D | T-D06, T-D08 | Support |
| `MKT-028` | A decline is free and neutral | D | T-D05, T-F06 | Rule |
| `MKT-029` | Cancellation | D | T-D07, T-F06 | Rule |
| `MKT-030` | Expiry | D | T-D06, T-D08 | Rule |
| `MKT-031` | Why 72 turns | D | T-D06, T-D08 | Support |
| `MKT-032` | An accepted trade is queued, not finished | D | T-D19, T-X04 | Rule |
| `MKT-033` | Settlement position | D | T-D19, T-X04 | Rule |
| `MKT-034` | Both legs or neither | D | T-D11 | Rule |
| `MKT-035` | A trade does not consume P3 output | D | T-X05 | Rule |
| `MKT-036` | Creation | D | T-D01, T-D03 | Rule |
| `MKT-037` | Creation reserves nothing | D | T-D03 | Rule |
| `MKT-038` | The pledge is disclosed as a pledge | D | T-D01, T-D03 | Rule |
| `MKT-039` | Acceptance is the reservation point | D | T-D04, T-X02 | Rule |
| `MKT-040` | Acceptance re-validates the whole trade, not just the clicked side | D | T-D04, T-D09 | Rule |
| `MKT-041` | The acceptance failure reasons | D | T-D15, T-F03 | Rule |
| `MKT-042` | A failed acceptance moves nothing | D | T-D04, T-D09 | Rule |
| `MKT-043` | Who may accept | D | T-D04, T-D09 | Rule |
| `MKT-044` | The acceptance window | D | T-D04, T-D09 | Rule |
| `MKT-045` | A counteroffer does not require acceptance of the previous terms | D | T-D12, T-F04 | Rule |
| `MKT-046` | Reservation contents at acceptance | D | T-D04, T-X02 | Rule |
| `MKT-047` | The stale-offer rule | D | T-F06 | Rule |
| `MKT-048` | Why 3 | D | T-D10, T-D14, T-D17 | Support |
| `MKT-049` | A directed trade may not target an unavailable nation | D | T-D10, T-D14, T-D17 | Rule |
| `MKT-050` | Reroll interaction | D | T-D10, T-D14, T-D17 | Rule |
| `MKT-051` | Political-state interaction | D | T-D17, T-X06 | Rule |
| `MKT-052` | The reservation set | D | T-D04, T-D18, T-X02 | Rule |
| `MKT-053` | Reservations are exclusive and visible | D | T-D13 | Rule |
| `MKT-054` | Space is reserved, not merely checked | D | T-X02, T-D04 | Rule |
| `MKT-055` | P2 re-validation | D | T-F08 | Rule |
| `MKT-056` | P4 settlement | D | T-D04, T-D18, T-X02 | Rule |
| `MKT-057` | Failure at P2 or P4 | D | T-F08 | Rule |
| `MKT-058` | The settlement order inside P4 | D | T-X02, T-D18 | Rule |
| `MKT-059` | D-024 requires declared limits, not a hidden hand-wave | D | T-D20, T-O05 | Rule |
| `MKT-060` | Why five active offers | D | T-D20, T-O05 | Support |
| `MKT-061` | The rate limit is a ceiling, not a budget | D | T-D20, T-O05 | Rule |
| `MKT-062` | Limits are enforced before reservation | D | T-D20, T-O05 | Rule |
| `MKT-063` | Expiry is a boundary job, not a player action | D | T-D08, T-O03 | Rule |
| `MKT-064` | Expiry notification | D | T-D20, T-O05 | Rule |
| `MKT-065` | The offer list is bounded | D | T-D20, T-O05 | Rule |
| `MKT-066` | No bulk acceptance | D | T-D20, T-O05 | Rule |
| `MKT-067` | Anti-automation | D | T-D20, T-O05 | Rule |
| `MKT-068` | The first-playable directed trade is fee-free | D | T-G19 | Rule |
| `MKT-069` | Why zero, and what would change it | D | T-G19 | Support |
| `MKT-070` | A future fee is a gate-stage decision, not a silent change | D | T-G19 | Rule |
| `MKT-071` | What Global Trade is | G | T-G17, T-S03 | Rule |
| `MKT-072` | Product requirement and release condition are different facts | G | T-S03 | Rule |
| `MKT-073` | Current gate status | G | T-S03 | Rule |
| `MKT-074` | What counts as passing a gate | G | T-S03 | Rule |
| `MKT-075` | Gate evidence ownership | G | T-S03 | Rule |
| `MKT-076` | The market is dark until the gate passes | G | T-F07 | Rule |
| `MKT-077` | No claim of readiness | G | T-F07 | Rule |
| `MKT-078` | The sell-listing object | G | T-G01, T-G02, T-G04 | Rule |
| `MKT-079` | Posting a sell listing reserves the units | G | T-G01 | Rule |
| `MKT-080` | Posting does not reserve crowns | G | T-G01 | Rule |
| `MKT-081` | The seller's warehouse must already hold the units | G | T-G01 | Rule |
| `MKT-082` | The asking price is the execution price | G | T-G02 | Rule |
| `MKT-083` | Partial fills are supported | G | T-G02 | Rule |
| `MKT-084` | Why partial fills | G | T-G01, T-G02, T-G04 | Support |
| `MKT-085` | Cancelling a sell listing | G | T-G04 | Rule |
| `MKT-086` | Expiry of a sell listing | G | T-G05 | Rule |
| `MKT-087` | The listing is public while it is open | G | T-G01, T-G02, T-G04 | Rule |
| `MKT-088` | A listing is not a contract with a named buyer | G | T-G01, T-G02, T-G04 | Rule |
| `MKT-089` | Suspension is administrative and narrow | G | T-G13 | Rule |
| `MKT-090` | The buy-offer object | G | T-G06, T-G07, T-G09 | Rule |
| `MKT-091` | Posting a buy offer reserves the crowns | G | T-G06 | Rule |
| `MKT-092` | The buy price is the execution price | G | T-G06, T-G07, T-G09 | Rule |
| `MKT-093` | Partial fills on a buy offer | G | T-G07 | Rule |
| `MKT-094` | Cancelling and expiring a buy offer | G | T-G08 | Rule |
| `MKT-095` | The buyer's warehouse must have room at execution, not at posting | G | T-X02, T-X03 | Rule |
| `MKT-096` | The listing board is symmetric | G | T-G06, T-G07, T-G09 | Rule |
| `MKT-097` | No self-trade | G | T-G10 | Rule |
| `MKT-098` | No wash or circular trading | G | T-G06, T-G07, T-G09 | Rule |
| `MKT-099` | The eleven resources are the only tradable goods | B | T-X09, T-G09 | Rule |
| `MKT-100` | Crowns are the only money | B | T-X09, T-G09 | Rule |
| `MKT-101` | Prohibited assets | B | T-X09, T-G09 | Rule |
| `MKT-102` | Military goods are ordinary resources here | B | T-X09, T-G09 | Rule |
| `MKT-103` | A resource has one identity everywhere | B | T-X09, T-G09 | Rule |
| `MKT-104` | No resource substitution | B | T-X09, T-G09 | Rule |
| `MKT-105` | Directed discovery | G | T-G14, T-G15 | Rule |
| `MKT-106` | Global discovery | G | T-G14, T-G15 | Rule |
| `MKT-107` | Crossed books are shown, not silently exploited | G | T-G14, T-G15 | Rule |
| `MKT-108` | What a listing row promises | G | T-G14, T-G15 | Rule |
| `MKT-109` | Four numbers, four labels | G | T-G14, T-G15 | Rule |
| `MKT-110` | Insufficient data is a state, not a zero | G | T-G14, T-G15 | Rule |
| `MKT-111` | The confirmation is informative, not routine | G | T-G14, T-G15 | Rule |
| `MKT-112` | The failure message names the cause | G | T-G14, T-G15 | Rule |
| `MKT-113` | No dark patterns | G | T-G14, T-G15 | Rule |
| `MKT-114` | Accessibility and the two-hour rhythm | G | T-G14, T-G15 | Rule |
| `MKT-115` | The execution model is taker-selected posted price | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-116` | Why this model | G | T-G11, T-G12, T-G09 | Support |
| `MKT-117` | What the model costs | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-118` | Determinism rules | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-119` | No partial acceptance of a directed offer | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-120` | A taker may execute more than one listing in a turn | G | T-O04 | Rule |
| `MKT-121` | An execution is accepted now and settles at P4 | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-122` | Execution races are resolved by reservation, not by arrival order | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-123` | Failure releases exactly once | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-124` | Market-action rate limits | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-125` | Why the listing caps | G | T-G11, T-G12, T-G09 | Support |
| `MKT-126` | Listing revisions are not supported | G | T-G11, T-G12, T-G09 | Rule |
| `MKT-127` | Three reservations at an execution | G | T-G02, T-G03, T-X02, T-X03 | Rule |
| `MKT-128` | Listing quantity and reservation identities | G | T-G20 | Rule |
| `MKT-129` | The execution acceptance order | G | T-X02, T-G09 | Rule |
| `MKT-130` | P2 re-validation of an execution | G | T-G13 | Rule |
| `MKT-131` | P4 settlement of an execution | G | T-G20 | Rule |
| `MKT-132` | Execution failure | G | T-G02, T-G03, T-X02, T-X03 | Rule |
| `MKT-133` | Cancellation and execution race | G | T-G02, T-G03, T-X02, T-X03 | Rule |
| `MKT-134` | Expiry with locked executions | G | T-G02, T-G03, T-X02, T-X03 | Rule |
| `MKT-135` | The no-overcommit invariant | G | T-X02, T-F09 | Rule |
| `MKT-136` | Unit-price representation | B | T-P01, T-X01 | Rule |
| `MKT-137` | Total order value | B | T-P01, T-X01 | Rule |
| `MKT-138` | Where rounding exists | B | T-P01, T-X01 | Rule |
| `MKT-139` | Reference prices are B-04's, unchanged | B | T-P01, T-X01 | Rule |
| `MKT-140` | The three price labels | B | T-P01, T-X01 | Rule |
| `MKT-141` | Safe arithmetic bounds | B | T-P01, T-X01 | Rule |
| `MKT-142` | No price floor or ceiling on the trade itself | B | T-P01, T-X01 | Rule |
| `MKT-143` | No price history at first playable | B | T-P01, T-X01 | Rule |
| `MKT-144` | The band is a ratio on reference value | B | T-P02 | Rule |
| `MKT-145` | Why a ratio, and why 30% | B | T-P02 | Support |
| `MKT-146` | Four fair-value statuses | B | T-D16 | Rule |
| `MKT-147` | The fresh window | B | T-P04 | Rule |
| `MKT-148` | What the fresh rule blocks | B | T-D16 | Rule |
| `MKT-149` | Why receiving is allowed but recorded | B | T-P02, T-P03, T-P04 | Support |
| `MKT-150` | Where the check runs | B | T-P02 | Rule |
| `MKT-151` | Age can change between creation and acceptance | B | T-P02, T-P03, T-P04 | Rule |
| `MKT-152` | Rerolls and replacement nations | B | T-P02, T-P03, T-P04 | Rule |
| `MKT-153` | Counterparties at different ages | B | T-P02, T-P03, T-P04 | Rule |
| `MKT-154` | Listings and the window | B | T-P02, T-P03, T-P04 | Rule |
| `MKT-155` | A legitimate unusual trade is not cheating | B | T-P02, T-P03, T-P04 | Rule |
| `MKT-156` | The band is not a tax and not a fee | B | T-P02, T-P03, T-P04 | Rule |
| `MKT-157` | What the market records as a signal | B | T-P05, T-P08 | Rule |
| `MKT-158` | The thresholds are diagnostic, not legal | B | T-P05, T-P08 | Rule |
| `MKT-159` | Cartels are allowed; price-fixing is expensive, not impossible | B | T-P05, T-P08 | Rule |
| `MKT-160` | Review, not punishment, at the market layer | B | T-P05, T-P08 | Rule |
| `MKT-161` | No automatic permanent ban, no silent confiscation | B | T-P05, T-P08 | Rule |
| `MKT-162` | Evidence retention | B | T-O06 | Rule |
| `MKT-163` | A directed trade's value flow | B | T-X01, T-X10, T-X12 | Rule |
| `MKT-164` | A global execution's value flow | B | T-X01, T-X10, T-X12 | Rule |
| `MKT-165` | Ledger events | B | T-X01, T-D19 | Rule |
| `MKT-166` | Conservation identities | B | T-X01 | Rule |
| `MKT-167` | No minting, no burning | B | T-X01, T-X10, T-X12 | Rule |
| `MKT-168` | Reservation release is idempotent | B | T-X01, T-X10, T-X12 | Rule |
| `MKT-169` | Duplicate execution requests | B | T-D12, T-F04 | Rule |
| `MKT-170` | A failed trade leaves both sides unchanged | B | T-X01, T-X10, T-X12 | Rule |
| `MKT-171` | Reconciliation query | B | T-X01, T-X10, T-X12 | Rule |
| `MKT-172` | No retroactive repricing | B | T-X01, T-X10, T-X12 | Support |
| `MKT-173` | The ten steps of a market action | B | T-X04, T-X11, T-X14 | Rule |
| `MKT-174` | Trade settlement is inside P4, after P3 | B | T-X05 | Rule |
| `MKT-175` | The boundary assignment | B | T-X04, T-X11, T-X14 | Rule |
| `MKT-176` | Counterparty ineligibility after acceptance | B | T-F08 | Rule |
| `MKT-177` | Cancellation, expiry and execution races | B | T-X04, T-X11, T-X14 | Rule |
| `MKT-178` | Interrupted resolution | B | T-F10 | Rule |
| `MKT-179` | The checks at each point | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-180` | The pair check is before reservation | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-181` | Public participation stays open | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-182` | No parallel identity system | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-183` | Shared network is not proof | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-184` | Sanctions survive a reroll | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-185` | Political states and the market | B | T-X06, T-X07, T-X08 | Rule |
| `MKT-186` | Directed terms are parties-only | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-187` | Global listings are public by design | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-188` | Completed global trades are not a public per-trade feed | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-189` | Personal history | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-190` | Retention classes | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-191` | Compaction never breaks a settlement | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-192` | No personal data in the market | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-193` | Administrative read is logged | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-194` | Deletion and account closure | B | T-X13, T-D20, T-P07 | Rule |
| `MKT-195` | No statistic at first playable | G | T-G16 | Rule |
| `MKT-196` | What a post-gate statistic may be | G | T-G16 | Rule |
| `MKT-197` | The sample rule | G | T-G16, T-P06 | Rule |
| `MKT-198` | Computation | G | T-G16, T-P06 | Rule |
| `MKT-199` | Complementary suppression | G | T-G16, T-P06 | Rule |
| `MKT-200` | What the statistic is not | G | T-G16, T-P06 | Rule |
| `MKT-201` | Manipulation resistance is partial | G | T-G16, T-P06 | Rule |
| `MKT-202` | Statistics are computed off the turn path | G | T-G16, T-P06 | Rule |
| `MKT-203` | No per-nation public volume ranking | G | T-G16, T-P06 | Rule |
| `MKT-204` | Every limit in one place | B | T-G18, T-O05 | Rule |
| `MKT-205` | `MKT-L14` is an operational guard, not a game rule | B | T-G18, T-O05 | Rule |
| `MKT-206` | Limits never depend on presence | B | T-G18, T-O05 | Rule |
| `MKT-207` | A limit rejection is free | B | T-G18, T-O05 | Rule |
| `MKT-208` | What this section is and is not | B | T-O01, T-O02, T-O04 | Rule |
| `MKT-209` | Write estimate per action | B | T-O01, T-O02, T-O04 | Rule |
| `MKT-210` | Per-turn bound | B | T-O01, T-O02, T-O04 | Rule |
| `MKT-211` | Read pattern | B | T-O01, T-O02, T-O04 | Rule |
| `MKT-212` | Duplicated-history risks | B | T-O01, T-O02, T-O04 | Rule |
| `MKT-213` | What Stage 3 must measure | B | T-O01, T-O02, T-O04 | Rule |
| `MKT-214` | The failure contract | B | T-F01, T-F02, T-F05 | Rule |
| `MKT-215` | "Nothing" is checkable | B | T-F01, T-F02, T-F05 | Rule |
| `MKT-215a` | Every market code in one place | B | T-F01, T-F02, T-F05 | Rule |
| `MKT-215b` | A sub-reason is not a second code | B | T-F01, T-F02, T-F05 | Rule |
| `MKT-216` | How to read the examples | B | T-D19, T-P02 | Support |
| `MKT-217` | The contract table | B | T-D19, T-P02 | Rule |
| `MKT-218` | One rule, one owner | B | T-D19, T-P02 | Rule |
| `MKT-219` | The accounting interface is stable | B | T-D19, T-P02 | Rule |
| `MKT-220` | The political interface is one-way | B | T-D19, T-P02 | Rule |
| `MKT-221` | The market's formulas | B | T-D19, T-P02 | Rule |
| `MKT-222` | The requirements | B | T-D19, T-P02 | Rule |
| `MKT-223` | The decisions | B | T-D19, T-P02 | Rule |
| `MKT-224` | The unresolved rows | B | T-D19, T-P02 | Rule |
| `MKT-225` | What is provisional and why | X | T-S03, T-P02 | Support |
| `MKT-226` | What is decided, not provisional | X | T-S03, T-P02 | Support |
| `MKT-227` | The validation obligations this document creates | X | T-S03 | Support |
| `MKT-228` | What has *not* been validated | X | T-S03, T-P02 | Rule |
| `MKT-229` | What was actually run | X | T-S05 | Support |
| `MKT-230` | Limitations | X | T-S05 | Support |
| `MKT-231` | What 07C inherits | X | T-S04, T-S05 | Support |
| `MKT-232` | What 07C must produce | X | T-S04, T-S05 | Support |
| `MKT-233` | What 07C may not do | X | T-S04 | Support |
| `MKT-234` | The 07C checklist | X | T-S05 | Support |
| `MKT-235` | Document control | X | T-S04, T-S05 | Support |

**9.2 Coverage result.** **237/237** rules appear exactly once; **199** are normative and **38** are definition/rationale/document-control rows verified by inspection plus the cited test. **0** rules are unmapped, **0** test IDs are undefined and **0** rules map only to a test that does not exist. The `Support` rows are not untested: each is checked by the cited scenario, the arithmetic checker or the document validator, but it has no standalone player action.
---

## 10. Global Trade release-gate evidence plan (G-1…G-6)

**10.1 The gate is not waived.** D-122 approves the **feature**, not the release. The definitions, owners and pass conditions of G-1…G-6 are unchanged from B-07 §9 (MKT-072–MKT-075). No gate moves in this prompt: **G-1, G-2, G-3, G-5 and G-6 remain NOT MET; G-4 remains PARTIAL.** Feature approval is not evidence, and a design document is not a measurement (MKT-074).

**10.2 What each gate needs.** The plan below states the evidence, method, environment, data and decision procedure. Where the current gate does not define a numeric threshold, this table says so and names the owner who must propose and validate one; **no threshold is invented here.**

### G-1 — Identity and anti-multi integrity

| Field | Plan |
|---|---|
| Exact definition | The D-034/D-036 identity and anti-multi controls are implemented and functioning, with a declared tolerance band and a review process |
| Current status | **NOT MET** — mechanisms designed; no implementation, no live incident rate, no tolerance band |
| What it proves | A player cannot profitably run multiple accounts or a shared-network pair through the market |
| Evidence required | Implemented control suite; a declared tolerance band; a stated observation window; an audit-trail review of every live incident; a test that a restricted pair cannot execute and cannot infer the restriction |
| Method | Adversarial account-linking tests + live incident audit + red-team attempts against the pair/network rules |
| Environment | A deployed test environment with at least two accounts and a controlled network; later a live observation window |
| Data to capture | Attempts, blocks, false positives, false negatives, review outcomes, time-to-review, incident rate against the band |
| Threshold / decision | The declared tolerance band must be met over the stated window with every incident reviewed. **The band itself is not defined anywhere yet**; Prompt 12 + operations must propose it and the owner must approve it before the gate can pass |
| Owner / stage | Integrity design + operations; Stage 5/6 implementation, Stage 8+ operations |
| When demonstrable | Only after implementation; design review can show coverage, not functioning controls |
| Existing evidence | Design only (B-03, B-12); **authoritative evidence: none** |

### G-2 — Write-budget evidence

| Field | Plan |
|---|---|
| Exact definition | Actual write counts and a passed budget test demonstrate that the market fits the operational budget |
| Current status | **NOT MET** — no market write count has been measured; Stage 3 does not exist |
| What it proves | The per-action and per-turn write volume fits the free-first platform with a declared safety margin |
| Evidence required | Measured rows written per action type (create, accept, execute, partial fill, cancel, expiry, failure, statistic job); a load test at the target scale; the measured counts compared with the platform's actual limits |
| Method | Instrument the real schema and run the action mix; replay a worst-case turn; compare with the Stage 1 baseline (6.01 rows per nation-turn, D1/Supabase) |
| Environment | Stage 3's measured environment; the prototype is not sufficient because the market schema does not exist |
| Data to capture | Rows per action, rows per turn, bytes per turn, P4 duration, retry/duplicate overhead, index growth |
| Threshold / decision | The projection must fit **with a declared safety margin**; the margin and the budget are set by Stage 3, not by this document. No numeric claim is made here |
| Owner / stage | Architecture; Stage 3, then Stage 5/7 implementation |
| When demonstrable | Only after implementation and a load test |
| Existing evidence | **None for the market.** The Stage 1 feasibility numbers are for a different schema and may not be reused as a market write count |

### G-3 — Demonstrated interest and liquidity

| Field | Plan |
|---|---|
| Exact definition | Measured directed-trade activity demonstrates a reasonable basis for expecting meaningful global-market participation |
| Current status | **NOT MET** — no live play; no qualifying threshold exists |
| What it proves | A public board would have counterparties; it would not launch empty and stay empty |
| Evidence required | Completed directed trades per active nation per day over a stated window; the distribution, not just the mean; the share of nations that trade at all; a threshold **set from the data before launch** |
| Method | Live observation after directed trades are playable; cohort analysis; a pre-registered threshold |
| Environment | A controlled playtest or closed beta with real players; a simulation can support a hypothesis but cannot prove player liquidity |
| Data to capture | Trades/day, active traders, repeat traders, time-to-first-trade, stale-offer rate, concentration |
| Threshold / decision | The measured rate must clear a threshold set from the data before launch. **No threshold is defined**; the product/analytics owner must propose it and the owner must approve it. A simulation is **not** evidence of liquidity |
| Owner / stage | Product/analytics; Stage 8+ playtests |
| When demonstrable | Only through observed player activity |
| Existing evidence | **None.** 07A describes the reference game's board; it says nothing about Nation Supremacy's future population |

### G-4 — Reference-price readiness

| Field | Plan |
|---|---|
| Exact definition | A documented reference-price design and a manipulation-pattern review exist, with a clear explanation of what the statistic means |
| Current status | **PARTIAL** — the design (§16, §23) and the manipulation review (§18) exist; the independent review and the implementation do not |
| What it proves | The book value is a stable, explained anchor; the statistic cannot mislead; the known manipulation patterns are countered or disclosed |
| Evidence required | A reference-price computation review (values, revision policy, cross-system agreement with B-04); an enumerated manipulation-pattern review (wash, layering, corners, cross-account, price signalling, statistic gaming); a published explanation of window, sample and suppression |
| Method | Independent economics review + adversarial pattern walkthrough + a check that B-04's book values and B-07's table agree |
| Environment | Design review now; implementation review before release; statistic behaviour only after the gate |
| Data to capture | The eleven prices and their sources; every pattern and its counter/disclosure; the statistic's cohort and suppression rules |
| Threshold / decision | Every pattern is countered, visibly exposed, or accepted with a stated rationale; the review must be signed, not implied by a design section |
| Owner / stage | Economy integrity; design review before Stage 5, implementation review in Stage 8+ |
| When demonstrable | The design half is demonstrable now; the implementation half only after code exists |
| Existing evidence | **Design half only** — B-07 §16–§18 and §23; no independent review, no implemented statistic |

### G-5 — Fee policy

| Field | Plan |
|---|---|
| Exact definition | The fee policy is decided using the gate's required evidence |
| Current status | **NOT MET** — no fee policy is decided; directed trades are zero at first playable and the global fee is open |
| What it proves | A fee, if any, is deliberate, disclosed, accounted and justified by evidence rather than invented |
| Evidence required | The Stage 1 fee comparison re-run with live data; a recorded posture (including zero) with payer, rate, `FEE` event, conservation identity and player-facing label; a G-5 record |
| Method | Re-run the comparison; model the fee's effect on legitimate small trades and on spam; decide with the owner |
| Environment | Live or controlled-play data; a fee cannot be validated on design intuition alone |
| Data to capture | Trade sizes, margins, spam rate, willingness-to-pay evidence, revenue vs friction |
| Threshold / decision | A fee posture is recorded with its payer/rate/event; "zero" is a valid outcome if the evidence supports it. No rate is invented here |
| Owner / stage | Owner + economy; Stage 8+ once the market has activity |
| When demonstrable | Only after real activity; a design discussion is not evidence |
| Existing evidence | **None beyond the design's zero at launch** |

### G-6 — Operational feasibility

| Field | Plan |
|---|---|
| Exact definition | Projected settlement disputes fit a declared operational capacity |
| Current status | **NOT MET** — no dispute-rate projection and no declared ops capacity |
| What it proves | The operator can handle the disputes, reversals, appeals and review load the market creates |
| Evidence required | A projected dispute rate per 1,000 trades; a declared capacity (cases per day, time-to-first-response, time-to-resolution); a drill or a staffing model; the appeal path |
| Method | Project from comparable systems + a tabletop drill; later measure real disputes |
| Environment | Operations; a tabletop is design evidence, not a measured rate |
| Data to capture | Disputes, reversals, appeals, false signals, time-to-review, backlog |
| Threshold / decision | Projected disputes are within capacity **with a stated margin**. The capacity target is CF-01, still unapproved; no numeric capacity is invented here |
| Owner / stage | Operations; Stage 3/Stage 8+ |
| When demonstrable | Only after a capacity target and a dispute model exist |
| Existing evidence | **None** — CF-01 and the ops capacity are open carry-forward items |

**10.3 What the plan deliberately does not do.** It does not assign a pass to any gate, invent a tolerance band, a write budget, a liquidity threshold, a fee rate or a dispute capacity, or treat a design artifact as a measurement. Each missing threshold is a named dependency on a future stage, not a silent assumption.

---

## 11. Economic balance and player-experience acceptance risks

**11.1 This is acceptance, not balance research.** The workflows must be understandable and fair enough to test; the numbers remain provisional and belong to Prompt 14. A correct transaction flow is not proof that the market is fun, liquid or balanced.

**11.2 The ten player situations.**

| Player | What they must understand | Design answer | Remaining risk |
|---|---|---|---|
| New nation, small stock | Why a trade is blocked; what is worth what | Book value beside every price; the band in plain words; a specific code; the exact values compared | The band may still block a legitimate first trade; UD-037 must measure it |
| Mature specialist | Whether a premium is allowed; what it signals | Mature out-of-band trades are allowed with a neutral signal; the premium and realised gap are shown | A player may read a signal as an accusation; the UI must not imply guilt |
| Occasional player | Whether an old offer is still live; what happened | 72-turn expiry; the expiry turn on every offer; a digest line; `STALE` after three failures | A player may return to an expired chain; the history must explain it |
| High-activity trader | Whether the limit is a budget; when it resets | Visible 20-action ceiling on turn IDs; no reward for waiting; a clear "oldest leaves at turn N" | Power users may find the ceiling restrictive; Prompt 14 may tune it |
| Player in a shortage | Whether a purchase will arrive before production | "Arrives after this turn's production; available next turn"; the settlement turn is named | The player may still expect the goods in P3; the copy must be unambiguous |
| Player with an expired/stale order | Whether anything was reserved or moved | "Nothing was reserved or moved"; the chain is history; a new chain is required | The player may believe the goods were held; the pledge warning must be prominent |
| Player whose resources are reserved | Why they cannot sell/use them | Total/reserved/available everywhere; the reservation's source in history | Reservations can be surprising if the list is buried; the board must link to them |
| Player in a restricted pair | Why the action fails; whether it is their fault | Neutral message + review route; no other account's state; no reason field | The neutral message may feel opaque; the appeal path must be visible |
| Would-be manipulator | That the rules are enforced | Signal + review; no automatic sanction; the market cannot ban or confiscate | A determined cartel is expensive, not impossible (MKT-159); do not claim otherwise |
| Player in an empty market | Whether the game is broken | "No listings match"; an offer to post; book value as a reference, not a promise | An empty board may still feel dead; G-3 must measure interest before launch |

**11.3 What every failure message must contain.** The action that failed; the rule and the exact values (where safe); whether anything was reserved or moved; what remains available; the next possible action; a stable code for support. It must not contain another account's state, the enforcement reason, a private note, a raw IP or a session token.

**11.4 What is explicitly untested.** Whether the band blocks too many legitimate trades; whether the expiry is too short or too long; whether the caps are too tight; whether partial fills make large listings usable; whether the board is legible at 50 rows; whether the fresh window deters legitimate gifts; whether the mature signal deters honest unusual trades; whether the market is fun. These are Prompt 14 simulations, closed-beta questions and UD-037/UD-038.

---

## 12. Free-first operational acceptance

**12.1 No capacity claim.** The market is designed to be bounded, not proven to fit. The table states the logical work; Stage 3 must measure it. No number here is a measurement, and the 5,000-execution guard is a disclosed placeholder (MKT-120).

| Action | Logical reads | Logical writes | Reservations | Ledger events |
|---|---|---|---|---|
| Create directed offer | 1 nation + pair + limits + idempotency | 1 offer + 1 revision + 1 event | 0 | 0 |
| View offer/board | 1 page (≤50) + 1 count | 0 (ordinary read) | 0 | 0 |
| Accept directed | both nations, pair, balances, space, idempotency | 1 action + 1 offer update + up to 5 crown/resource reservations per side + up to 2 space reservations | both sides | 0 |
| Settle directed | frozen snapshot + reservations | 1 action update + up to 10 reservation updates + 4 ledger events + 1 digest | consumed | 4 |
| Post sell listing | 1 nation + inventory + caps + idempotency | 1 listing + 1 inventory reservation + 1 event | units | 0 |
| Execute listing | listing + both nations + pair + space + idempotency | 1 execution + 1 listing update + 3 reservations + 1 event | 3 | 0 |
| Settle execution | frozen snapshot + reservations | 1 execution update + 1 listing update + 3 reservation updates + 2 ledger events + 1 digest | consumed | 2 |
| Cancel/expire | 1 object + reservations | 1 status + 1–2 releases + 1 event | released | 0 |
| Failure | 1 action + reservations | 1 status + releases + 1 failure event | released | 0 |
| Statistic job (post-gate) | 1 window aggregate | 1 row per resource per interval | 0 | 0 |

**12.2 Worst-case bounds.** A directed acceptance writes at most one action, one offer update, ten value reservations, two space reservations and one event. A P4 settlement writes at most four ledger events and one digest per trade. A public execution writes at most three reservations, two ledger events and one digest. A listing page reads at most 50 rows plus one count. Expiry is one B0 pass, ordered and idempotent. The statistic job is off the turn path. There is no continuous matcher, poller or per-tick scan.

**12.3 What Stage 3 must measure.** Rows and bytes per action and per turn; the P4 duration at 5,000 executions; the cost of a 12-listing-per-nation world; the expiry job's cost at the largest plausible listing count; the index growth; the retry overhead; the read cost of the board; the statistic job's cost. Until then, the free-first objective is a constraint and a design posture, not a proven capacity.

**12.4 Atomicity.** Every value-moving action is one transaction: reservations, the action record and the ledger pair commit together; a failure releases in the same step and writes no pair. The implementation must prove this in Stage 5/7; this document specifies it and does not claim it.

---

## 13. Register and decision changes in Prompt 07C

**13.1 New records.**

| Record | Content | Why |
|---|---|---|
| **D-122** | Global Trade is an approved, mandatory, long-term product feature; feature approval is separate from release; G-1…G-6 unchanged; reversal needs a new owner-authorized decision | The owner's Option A decision (Part 4.1 of the brief) |
| **DD-136** | The Stage 2 design position that mirrors D-122 | The Stage 2 register must carry the commitment |
| **REQ-513** | The traceable requirement: Global Trade is required, distinct from directed trades, on the roadmap, gated by G-1…G-6 and the existing contracts | Traceability from the product decision to the Bible |

**13.2 Records deliberately not created.** No new `MKT-` rule, no new formula, no new `UD-` row and no new failure code. The three corrections are clarifications of existing rules, recorded in B-07 v1.1's revision note; they do not need a new rule ID. UD-037 (calibration) and UD-038 (post-gate liquidity and the crossed book) remain **open**, with their existing owners and exit conditions; documenting a workflow does not resolve a calibration question or prove liquidity.

**13.3 No renumbering.** D-001…D-121, DD-001…DD-135, REQ-001…REQ-512, UD-001…UD-038 and every MKT/F-TM ID keep their existing numbers and text except for the three documented corrections. New records take the next free ID.

**13.4 B-07 v1.1 corrections (the only rulebook changes).**

1. **E1 ledger** — the 200-crown payment is recorded once, on Aurelia's `TRADE_BUY` and Borealis's `TRADE_SELL`; the earlier table double-counted it and contradicted the closing balances. MKT-165 now states the attribution rule.
2. **Space predicate** — MKT-039, MKT-058, MKT-095, MKT-129 and MKT-135 now use `free_space = W − total_inventory − space_reserved` and never add reservations back. The earlier wording would have overbooked a warehouse with existing reservations, and MKT-058 wrongly treated an invariant defect as ordinary settlement competition.
3. **Fair-value wording** — MKT-144/MKT-145 and E5/E20 now describe the band as an asymmetric ratio: the larger side may be at most 30% bigger; a 30% discount is not the mirror image. E20 adds the reversed and discount boundaries. No threshold changed.

---

## 14. Validation record

**14.1 What ran.** The commands below were run after the final edit on 2026-10-29. They are **document and arithmetic checks**; no game server, database, scheduler, queue, browser or runtime market exists.

| Command | Actual result | Exit |
|---|---|---|
| `python3 qa_backups/verify_market_workflows.py` | 237/237 rules mapped; 0 unmapped; 0 duplicate tests; all catalogue IDs defined | 0 |
| `python3 qa_backups/verify_market_workflows.py --self-test` | 8/8 guards detected their defect | 0 |
| `python3 qa_backups/verify_market_numbers.py` | 95/95 checks passed; 0 failed | 0 |
| `python3 qa_backups/verify_market_numbers.py --self-test` | 14/14 guards detected their defect | 0 |
| `python3 qa_backups/validate_final.py` | ALL CHECKS PASSED | 0 |
| `python3 qa_backups/validate_final.py --self-test` | 4/4 guards detected their defect | 0 |
| `python3 qa_backups/09_validate.py` | 345/345 checks passed | 0 |
| `python3 qa_backups/test_next_action.py` | 20 tests OK | 0 |
| `python3 qa_backups/test_decision_registers.py` | 12 tests OK | 0 |
| `python3 qa_backups/verify_economy_numbers.py` | 164/164 passed | 0 |
| `python3 qa_backups/verify_city_numbers.py` | 267/267 passed | 0 |
| `python3 qa_backups/verify_politics_numbers.py` | 879/879 passed | 0 |
| `python3 qa_backups/verify_politics_numbers.py --self-test` | 18/18 guards detected their defect | 0 |

**14.2 What the checks prove.** The market checker recomputes the E1 ledger signs and balances, the space predicate and the band boundaries from the register's constants, verifies that every `MKT-`/`F-TM-` identifier cited in B-07 exists, and checks the 35 failure rows, the fresh-window boundary and the gate statuses. The workflow checker verifies that every MKT rule appears exactly once in §9, that every test named there is defined in §8, and that the approval decision, the gate statuses and the next-task statements agree across the registers. The final validator checks the continuity set, the requirement/decision/unresolved counts and the roadmap status.

**14.3 What they do not prove.** No runtime transaction, concurrency, race, load, security, penetration, liquidity, balance or player-experience result. A green document check is not a passed game test.

**14.4 Unavailable checks.** There is no market server, schema, endpoint, screen or scheduler to test. G-1…G-6 are not passed and cannot be passed by this prompt's checks. The 5,000-execution guard, the 3,000 bp band, the 360-turn window, the 72-turn expiry and every cap remain provisional.

---

## 15. Prompt 07C acceptance and handoff

**15.1 Acceptance checklist.** Each line is a criterion from the prompt's Part 20, with the evidence that supports it.

| Criterion | Status | Evidence |
|---|---|---|
| Global Trade formally recorded as mandatory | **Met** | D-122, DD-136, REQ-513, §2 |
| Decision linked from roadmap, requirements, handoff | **Met** | §2.5 and the synchronized continuity set |
| Cannot be silently removed by routine AI discretion | **Met** | D-122's reversal clause; §2.4 |
| G-1…G-6 intact | **Met** | §10; B-07 §9 unchanged |
| Not falsely marked implemented or release-approved | **Met** | five-state table §2.2; §14.3 |
| Directed workflows complete | **Met** | W-D01…W-D20 |
| Global sell/buy lifecycles complete | **Met** | W-G01…W-G22 |
| Partial fills, remaining quantities, reservations deterministic | **Met** | §3.3, W-G07/W-G19, T-G02/T-G07 |
| Cross-system constraints and turn phases consistent | **Met** | §3.6, §6 |
| Error, privacy and audit behaviour specified | **Met** | §11.3, T-D20, T-P07/T-P08 |
| Abuse and boundary cases covered | **Met** | T-D13…T-D17, T-G09…T-G12, §7 |
| E1 ledger review complete | **Met** | §3.5; B-07 E1 corrected and checked |
| Warehouse rules internally consistent | **Met** | §3.3; MKT-039/058/095/129/135 corrected |
| Fair-value band stated without misleading terminology | **Met** | §3.4; MKT-144/145, E5/E20 corrected |
| No decision or register ID overwritten | **Met** | §13.3 |
| Rulebook and formula register agree | **Met** | §14.1; B-07 v1.1 and register v1.1 |
| Every MKT rule traced or justified | **Met** | §9; 237/237, 0 unmapped |
| G-1…G-6 evidence plans actionable | **Met** | §10 |
| Required validators run | **Met** | §14 |
| Regression tests passed or failures documented | **Met** | §14; no failures |
| No unsupported runtime/load/liquidity claim | **Met** | §14.3 |
| Roadmap identifies 07A/07B complete and 07C complete | **Met** | roadmap/status set |
| Handoff and progress summaries agree | **Met** | continuity set |
| Historical records preserved | **Met** | log §22 and earlier sections untouched |
| Prompt 08 is next | **Met** | §15.3 |
| Next AI instructed to read the authoritative files | **Met** | §15.4 |

**15.2 Verdict.** **PASS — ACCEPTED at the specification level.** The market design is complete, internally consistent and traceable; the three reported defects are corrected and guarded; the product commitment is recorded without inflating release readiness. **Global Trade is not implemented, not tested at runtime and not released.** The six gates remain unmet or partial.

**15.3 Next task.** **Stage 2, Prompt 08 — diplomacy between nations.** It starts from B-07's cross-system contract (§6), the account/pair rules (B-03), the leadership states (B-06) and the trade restrictions already decided; it must not reopen the market model, release Global Trade, or reinterpret the fair-value band as a diplomatic sanction. It owns treaties, relations, sanctions and any diplomatic effect that the current contracts do not already define. If it needs a market restriction, it adds the rule to B-08 and records the interface here; it does not silently change a `MKT-` rule.

**15.4 Handoff instruction.** Read, in order: [ROADMAP.md](../ROADMAP.md) and [stage-2/01](01_stage_2_prompt_roadmap.md) for the sequence; [AI_HANDOFF.md](../AI_HANDOFF.md) §H and the 2026-10-29 validation record; [B-07](13_trade_and_markets.md) v1.1 §3–§6, §9–§19, §26–§32; [this document](14_market_workflows_and_acceptance.md) §2–§4 for the canonical semantics and §10 for the gates; [the formula register](13_trade_and_markets_formula_register.md) for every constant. Do not restart Prompt 07B. Do not treat the test catalogue as executed. Do not begin Prompt 09.

**15.5 What Prompt 08 inherits, and what it must not do.** It inherits two trading systems, a fee-free directed layer, a gated public layer, pair restrictions, leadership read-only states and a strict no-mint accounting identity. It must not add a trade tax, tariff or embargo to the market without a new decision; must not make an alliance treasury a market wallet; must not make Operations Points tradable; must not promise automatic matching; and must not describe the market as released.

**End of document.**
