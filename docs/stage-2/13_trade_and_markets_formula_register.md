# Trade and markets — formula and balance register

**Version:** 1.1 · **Created:** 2026-10-28 · **Stage 2, Prompt 07B** · **Revised:** 2026-10-29 (v1.1 is the Prompt 07C formula reconciliation: F-TM-005's validation now records the asymmetric `70 → 91` boundary and the reversed `130/100` case; F-TM-025 states that `space_reserved` is never added back; no constant or expression changed. Earlier: first issue, the directed-trade and Global Trade formulas, their constants, bounds, rounding, dependencies and validation methods)
**Status:** **Draft** — definitive formula definitions. **No formula has been implemented or runtime-tested.** The worked values in §5 are hand arithmetic, checked by `qa_backups/verify_market_numbers.py`.
**Authority:** This register is the **single authoritative source** for the expression, variables, units, bounds, rounding, timing and dependencies of every trade and market formula in Nation Supremacy. [B-07](13_trade_and_markets.md) summarises these formulas; if the two disagree, this register wins until it is corrected by a new revision.
**Companions:** [B-07](13_trade_and_markets.md) · [B-04 register](10_economic_formula_and_balance_register.md) · [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [requirements](03_requirements_traceability.md) · [07A research](research/07A_politics_and_war_market_research.md)

---

## 1. How to use this register

**F-TM-000 — Register rules.** *Provisional.*

1. Every market formula has exactly one `F-TM-###` row in §4. No other document may define a competing expression.
2. A formula is cited by ID, never by a nickname.
3. A number change is a new revision with a date and a reason; the old value stays in the revision history.
4. A formula that depends on a later prompt's input says so in its **Dependencies** field. The dependency is an interface, not an excuse to leave the formula undefined.
5. A formula is not "validated" because the algebra is consistent. Validation means a test was executed; **zero runtime tests have been executed**.
6. The register does not duplicate B-04's reference prices. It cites `P_ref(r)` from [B-04 register §3.5](10_economic_formula_and_balance_register.md); a change there changes this register's inputs without a second table.

**F-TM-000a — Status vocabulary.** **Confirmed (design)** means the rule is selected; **Provisional** means a number or coefficient may change at Prompt 14; **Deferred** means a later prompt owns the input. No formula is approved, implemented or tested.

**F-TM-000b — What "value" means here.** A **declared value** uses the prices the parties wrote. A **reference value** uses B-04's book values. The fair-value band uses the **reference value** (F-TM-005/006); the declared value is for display and for the fair-value-gap report (F-TM-004). A market price is neither: it is the executed price of one trade (F-TM-021).

---

## 2. Numerical conventions

**F-TM-000c — Integer arithmetic.** *Provisional (D-045; F-EC-000b).* All quantities, prices, crowns and totals are integers. Every division states `floor` or `ceil`; the default is `floor`. No formula uses binary floating point.

**F-TM-000d — Units.** *Provisional.* Units are stated per formula: `crowns`, `units`, `turns`, `bp`. A quantity without a unit is not a valid input.

**F-TM-000e — Boundary timing.** *Provisional (F-EC-000d).* All formulas run at the two-hour UTC boundary inside B-02's P3 or P4, except the submission checks in §4.20 (which run when the player submits) and the daily statistic job (which runs off the turn path).

**F-TM-000f — Ordering.** *Provisional.* Settlement uses B-02's P4 order: directed trades first, then Global Trade executions, each by `(submitted_at, action_id)`. A formula that reads a later sub-phase's output is invalid.

**F-TM-000g — No negative inputs.** *Provisional.* A quantity, price or crown amount is `≥ 0`; a resource line quantity is `≥ 1`; a global price is `≥ 1`; a total is `≥ 0`. A negative input is `MKT-E12`, not a formula result.

---

## 3. Constants

**F-TM-000h — Constants are versioned.** *Provisional.* The values below are the v1.0 provisional calibration. They are not measured, observed or balanced. Prompt 14 may change one only by a new revision of this register.

| Constant | Symbol | Value | Unit | Status | Rationale |
|---|---|---|---|---|---|
| Fair-value band | `B` | 3,000 | bp | Provisional | A ratio band; the reference's 30% is a shape, not a validated value |
| Fresh-nation window | `W_fresh` | 360 | turns | Provisional (inherited ONB-031) | 30 days at 12 turns/day |
| Directed expiry | `T_offer` | 72 | turns | Provisional | 6 days; enough for asynchronous negotiation, short enough to limit stale pledges |
| Listing expiry | `T_list` | 72 | turns | Provisional | Same |
| Failed acceptances to `STALE` | `N_stale` | 3 | count | Provisional | One is normal, two is suspicious, three is unbacked |
| Revision cap | `N_rev` | 10 | count | Provisional | Bounds negotiation |
| Directed active outgoing | `N_out` | 5 | chains | Provisional | Readability |
| Directed chains per pair | `N_pair` | 1 | chains | Provisional | One negotiation per relationship |
| Lines per side | `N_lines` | 5 | lines | Provisional | Legibility |
| Max units per line | `Q_max` | 100,000 | units | Provisional | Above any warehouse; arithmetic bound |
| Max crowns per side | `C_max` | 10,000,000 | crowns | Provisional | Arithmetic bound |
| Max unit price | `P_max` | 100,000 | crowns/unit | Provisional | Arithmetic bound |
| Active sell listings per resource | `N_sell` | 4 | listings | Provisional | Board readability |
| Active buy offers per resource | `N_buy` | 4 | offers | Provisional | Board readability |
| Active listings total | `N_list` | 12 | listings | Provisional | One nation's share of the board |
| Market actions per window | `N_act` | 20 | actions | Provisional | Spam ceiling |
| Action window | `T_act` | 12 | turns | Provisional | 24 hours |
| Executions per nation per turn | `N_exec` | 50 | executions | Provisional | P4 bound |
| World executions per turn | `N_world` | 5,000 | executions | Provisional placeholder | Stage 3 must replace it with a measured value |
| Statistic window | `T_stat` | 12 | turns | Provisional | A rolling day |
| Statistic minimum trades | `N_trades` | 5 | trades | Provisional (D-027) | k = 5 applied to trades |
| Statistic minimum nations | `N_nations` | 5 | nations | Provisional (D-027) | k = 5 applied to participants |
| Volume band | `V_band` | 10 | units | Provisional | Suppression coarseness |
| Fee rate | `fee_bp` | 0 | bp | Deferred to G-5 | No fee at launch |
| Flat fee | `fee_flat` | 0 | crowns | Deferred to G-5 | No fee at launch |
| Signed 64-bit maximum | `MAX_I64` | 9,223,372,036,854,775,807 | integer | Fixed | Platform bound |

**F-TM-000i — Reference prices are inputs, not constants of this register.** *Provisional.* `P_ref(r)` is read from [B-04 register §3.5](10_economic_formula_and_balance_register.md): Food 1, Coal 1, Oil 2, Iron 1, Bauxite 2, Lead 3, Uranium 30, Gasoline 6, Steel 7, Aluminum 8, Ammunition 6 crowns per unit. This register does not own those values.

---

## 4. Formulas

### 4.1 Side values

**F-TM-001 — Declared side value.** *Provisional (MKT-021).*

```
D(side) = crowns(side) + Σ over lines i of ( quantity_i × declared_price_i )
```
- **Inputs:** `crowns(side)` ≥ 0; `quantity_i` ≥ 1; `declared_price_i` ≥ 0.
- **Output:** crowns, integer ≥ 0.
- **Rounding:** none; each product is exact under F-TM-031.
- **Bounds:** `D ≤ C_max + N_lines × Q_max × P_max`.
- **Dependencies:** F-TM-031.
- **Validation:** recompute E1/E2's declared totals; a wrong unit price changes `D` but not `V`.

**F-TM-002 — Reference side value.** *Provisional (MKT-021).*

```
V(side) = crowns(side) + Σ over lines i of ( quantity_i × P_ref(resource_i) )
```
- **Inputs:** `crowns`; `quantity_i`; `P_ref(r_i)` from B-04.
- **Output:** crowns, integer ≥ 0.
- **Rounding:** none.
- **Bounds:** as F-TM-001.
- **Dependencies:** B-04 register §3.5.
- **Validation:** E1: `200 + 100 × 1 = 300`; E2: `100 + 40 × 2 + 20 × 1 = 200`.

**F-TM-003 — Pair ordering.** *Provisional.*

```
V_low  = min( V(A), V(B) )
V_high = max( V(A), V(B) )
D_low  = min( D(A), D(B) )
D_high = max( D(A), D(B) )
```
- **Output:** four crowns values.
- **Note:** the band uses `V`; the display uses both.
- **Validation:** E1 `V_low = 300`, `V_high = 350`.

**F-TM-004 — Side reference gap.** *Provisional (ECN-109).*

```
G(side) = V(side) − D(side)
```
- **Output:** crowns, may be negative.
- **Meaning:** how far the declared price is from book value for that side. It is **reporting**, not a fair-value test; the test is F-TM-006.
- **Validation:** E6: Kition `V = 300`, `D = 600`, `G = −300`; Larisa `V = 600`, `D = 600`, `G = 0`.

### 4.2 Fair value

**F-TM-005 — The band bound.** *Provisional (MKT-144).*

```
V_max = floor( V_low × ( 10,000 + B ) / 10,000 )
```
- **Inputs:** `V_low` ≥ 1; `B = 3,000`.
- **Output:** crowns, integer.
- **Rounding:** `floor` after the multiply, exactly once.
- **Bounds:** `V_max ≤ floor(1.3 × V_low)`.
- **Validation:** `V_low = 100 → 130`; `V_low = 175 → 227`; `V_low = 300 → 390`; `V_low = 70 → 91` (so `100` is out of band: a 30% discount is not the mirror of a 30% premium); the reversed pair `V_low = 100, V_high = 130` is in band.

**F-TM-006 — The fair-value verdict.** *Provisional (MKT-146).*

```
if V(A) = 0 and V(B) = 0        → INVALID          (MKT-E01)
if exactly one of V(A), V(B) = 0 → ONE_SIDED
if V_high ≤ V_max                → IN_BAND
otherwise                        → OUT_OF_BAND
```
- **Boundary:** equality with `V_max` is `IN_BAND` (MKT-144, E20).
- **Output:** one of four statuses.
- **Validation:** E1 `350 ≤ 390` → `IN_BAND`; E5 `200 > 130` → `OUT_OF_BAND`; E20 `130 ≤ 130` → `IN_BAND`, `131 > 130` → `OUT_OF_BAND`.

**F-TM-007 — The reported ratio.** *Provisional.*

```
ratio_bp = floor( V_high × 10,000 / V_low )        if V_low ≥ 1
```
- **Output:** basis points, integer ≥ 10,000 when `V_high > V_low`.
- **Use:** the interface's "the larger side is X% bigger" and the audit record. It is **not** the verdict; the verdict is F-TM-006.
- **Validation:** E2 `floor(200 × 10,000 / 175) = 11,428` (114.28%); E6 `floor(600 × 10,000 / 300) = 20,000` (200%).

**F-TM-008 — The fresh window.** *Provisional (MKT-147; ONB-031).*

```
elapsed = current_turn − nation_created_turn
fresh   = elapsed < W_fresh            (W_fresh = 360)
```
- **Inputs:** turn IDs; `nation_created_turn` is the turn the nation became `active`.
- **Output:** boolean.
- **Edge:** `elapsed = 360` is **not** fresh.
- **Validation:** E4 `elapsed = 9` → fresh; a nation created on turn 1 is not fresh on turn 361.

**F-TM-009 — The fresh verdict and signal.** *Provisional (MKT-146/148/149).*

```
fresh_party = fresh(A) or fresh(B)
if not fresh_party:
    verdict = F-TM-006 ; mature_signal = S01 if OUT_OF_BAND, S02 if ONE_SIDED, S03 if ONE_SIDED_RECEIVE
if fresh_party:
    if F-TM-006 = INVALID: reject E01
    if F-TM-006 = ONE_SIDED and fresh nation is the giver: reject E09
    if F-TM-006 = ONE_SIDED and fresh nation is the receiver: allow, signal S03
    if F-TM-006 = OUT_OF_BAND: reject E08
    if F-TM-006 = IN_BAND: allow
```
- **Output:** `ALLOW` or `REJECT(code)`, plus an optional signal.
- **Validation:** E4 allow; E5 reject `E08`; E19 posting reject `E08`; a one-sided fresh send reject `E09`.

### 4.3 Directed-trade formulas

**F-TM-010 — Directed line total.** *Provisional (MKT-019).*

```
line_total_i = quantity_i × declared_price_i
```
- **Output:** crowns.
- **Rounding:** none.
- **Validation:** E1 food `100 × 1 = 100`; E2 oil `40 × 2 = 80`.

**F-TM-011 — Directed side total.** *Provisional.* `D(A)` and `D(B)` by F-TM-001, with at most `N_lines = 5` lines per side.

**F-TM-012 — Directed offer declared total.** *Provisional.*

```
T_declared = D(A) + D(B)
```
- **Use:** display only. It is not the value of either side and must never be compared with one side's reference value.
- **Validation:** E1 `300 + 350 = 650`.

**F-TM-013 — Directed offer reference total.** *Provisional.*

```
T_reference = V(A) + V(B)
```
- **Use:** the audit and the "total book value exchanged" line.
- **Validation:** E1 `300 + 350 = 650` (coincides because declared = book).

**F-TM-014 — Expiry turn.** *Provisional (MKT-030).*

```
expires_turn = revised_turn + T_offer          (T_offer = 72)
```
- **Inputs:** the turn of the current revision; not the creation turn after a counteroffer.
- **Output:** turn ID.
- **Edge:** a revision on turn 10 expires at the start of turn 82; the offer is live through turn 81 and expires in turn 82's B0 pass.
- **Validation:** E12 `10 + 72 = 82`.

### 4.4 Listing quantities and reservations

**F-TM-015 — Listing remaining quantity.** *Provisional (MKT-128).*

```
quantity_remaining = quantity_posted − quantity_filled − quantity_locked
```
- **Invariant:** `0 ≤ quantity_remaining ≤ quantity_posted`.
- **Validation:** E7 `500 − 200 − 0 = 300`; E10 `500 − 300 − 0 = 200`; E12 `500 − 0 − 200 = 300`.

**F-TM-016 — Sell listing reserved units.** *Provisional.*

```
reserved_units = quantity_locked + quantity_remaining
```
- **Output:** units, `≤ quantity_posted`.
- **Validation:** E7 after the fill: `0 + 300 = 300`; before the fill: `0 + 500 = 500`.

**F-TM-017 — Buy offer commitment at posting.** *Provisional (MKT-091).*

```
crown_commitment = quantity_posted × unit_price
```
- **Output:** crowns.
- **Rounding:** none.
- **Validation:** E8 `400 × 2 = 800`.

**F-TM-018 — Buy offer reserved crowns.** *Provisional.*

```
reserved_crowns = ( quantity_locked + quantity_remaining ) × unit_price
```
- **Output:** crowns, `≤ crown_commitment`.
- **Validation:** E8 after the fill `(0 + 250) × 2 = 500`; `800 − 300 = 500`.

**F-TM-019 — Locked execution value.** *Provisional.*

```
locked_value = quantity_locked × unit_price
```
- **Use:** the part of a buy offer's reservation that belongs to accepted executions; for a sell listing it is the book-value basis of the locked units (F-TM-027).
- **Validation:** E8 `150 × 2 = 300`.

**F-TM-020 — Listing terminal test.** *Provisional.*

```
FILLED    if quantity_remaining = 0 and quantity_locked = 0
PARTIALLY_FILLED if quantity_filled > 0 and quantity_remaining > 0
OPEN      otherwise, while status is not CANCELLED/EXPIRED/SUSPENDED
```
- **Validation:** E7 after one fill: `remaining 300`, `filled 200` → `PARTIALLY_FILLED`; E10 after two fills: `remaining 200`, `filled 300` → `PARTIALLY_FILLED`; a 500/500 fill → `FILLED`.

### 4.5 Execution, availability and space

**F-TM-021 — Execution value.** *Provisional (MKT-131).*

```
T = x × unit_price            (1 ≤ x ≤ quantity_remaining)
```
- **Output:** crowns.
- **Validation:** E7 `200 × 8 = 1,600`; E8 `150 × 2 = 300`; E10 `100 × 8 = 800`.

**F-TM-022 — Buyer cost and seller proceeds.** *Provisional.*

```
buyer_cost      = T
seller_proceeds = T
```
For a sell listing the buyer pays `T` and the seller receives `T`; for a buy offer the seller receives `T` and the buyer pays `T`. The labels swap, the amount does not. A future fee would make `buyer_cost = T + fee_buyer` and `seller_proceeds = T − fee_seller`, with the fee written separately (F-TM-038); at launch both fees are zero.

**F-TM-023 — Available crowns.** *Provisional (TR-067/TR-069).*

```
available_crowns = total_crowns − reserved_crowns
```
- **Invariant:** `0 ≤ available_crowns ≤ total_crowns`.
- **Validation:** E13 `1,000 − 800 = 200`; a second `100 × 2 = 200` fits exactly; `101 × 2 = 202 > 200` fails.

**F-TM-024 — Available units.** *Provisional.*

```
available_units(r) = total_units(r) − reserved_units(r)
```
- **Validation:** E3 `120 − 20 = 100`; after selling 60: `60 − 20 = 40`.

**F-TM-025 — Free warehouse space.** *Provisional (ECN-124; MKT-054).* **The one canonical capacity predicate:** `space_reserved` is already subtracted, so it is never added back when testing an incoming quantity. `free_space + space_reserved` would ignore every existing reservation and overbook the warehouse.

```
free_space = W − total_inventory − space_reserved
```
- **Output:** units, may be negative only if a prior invariant failed (a defect).
- **Validation:** E15 `2,000 − 1,950 − 0 = 50`; a 100-unit purchase fails.

**F-TM-026 — Execution acceptance predicate.** *Provisional (MKT-129).*

```
accept  ⇔  turn_open
        ∧ owner(actor, nation)
        ∧ account_eligible ∧ nation_active
        ∧ listing.status ∈ {OPEN, PARTIALLY_FILLED}
        ∧ actor ≠ maker
        ∧ pair ∉ {RESTRICTED, MAINTAINED}
        ∧ political_state_allows(actor)
        ∧ 1 ≤ x ≤ quantity_remaining
        ∧ taker_can_cover(actor, x, side)
        ∧ x ≤ free_space(receiver)
        ∧ fresh_verdict = ALLOW
        ∧ limits_ok
        ∧ idempotency_key_new
```
- **Output:** accept or the first failing code.
- **Note:** the order of the conjuncts is the order in MKT-129; the first failure is reported. The predicate is not a formula with a numeric result.

**F-TM-027 — Realised fair-value gap.** *Provisional (ECN-109; MKT-140).*

```
gap_receiver = x × P_ref(r) − T
gap_giver    = T − x × P_ref(r)
```
- **Output:** crowns, one positive and one negative (or both zero).
- **Conservation:** `gap_receiver + gap_giver = 0`; no value is minted.
- **Validation:** E9 `100 × 8 − 900 = −100` for the buyer, `+100` for the seller; E6 `10 × 30 − 600 = −300` for the buyer, `+300` for the seller.

### 4.6 Statistics

**F-TM-028 — Volume-weighted average.** *Provisional (MKT-198).*

```
VWAP = floor( Σ over trades i of ( x_i × price_i ) / Σ over trades i of x_i )
```
- **Inputs:** completed trades in the window `[current_turn − 11, current_turn]`.
- **Output:** crowns per unit, integer ≥ 0.
- **Rounding:** one `floor` after the division; the numerator is summed first.
- **Bounds:** only published if F-TM-029 passes.
- **Validation:** three trades `(100 @ 8)`, `(200 @ 9)`, `(50 @ 7)`: numerator `800 + 1,800 + 350 = 2,950`; denominator `350`; `floor(2,950 / 350) = 8`.

**F-TM-029 — Sample gate.** *Provisional (MKT-197).*

```
publish ⇔ trades ≥ 5 ∧ distinct_participants ≥ 5
```
- `distinct_participants = |{buyer_nation_id} ∪ {seller_nation_id}|`.
- **Output:** boolean; when false the state is `INSUFFICIENT_SAMPLE` and no number or count is shown.
- **Validation:** four trades among five nations → suppress; five trades among five nations → publish; six trades among four nations → suppress.

**F-TM-030 — Volume band.** *Provisional (MKT-198).*

```
volume_band = floor( Σ x_i / V_band ) × V_band          (V_band = 10)
```
- **Output:** units, a multiple of 10, `≤ Σ x_i`.
- **Use:** the published volume; the exact total stays private.
- **Validation:** `Σ x = 347 → 340`; `Σ x = 9 → 0` (and a zero band is not published).

### 4.7 Arithmetic safety

**F-TM-031 — Checked multiply.** *Provisional (MKT-141).*

```
checked_mul(a, b):
    if a < 0 or b < 0: reject E12
    if b ≠ 0 and a > MAX_I64 / b: reject E11
    return a × b
```
- **Output:** the product or a rejection.
- **Note:** integer division here is the guard; it is not a game formula.
- **Validation:** `100,000 × 100,000 = 10,000,000,000` passes; a fabricated `10^19` product rejects.

**F-TM-032 — Safe directed bound.** *Provisional.*

```
max_directed_total = C_max + N_lines × Q_max × P_max
                   = 10,000,000 + 5 × 100,000 × 100,000
                   = 50,010,000,000
```
- **Output:** crowns; far below `MAX_I64`.
- **Validation:** recompute the expression; it must equal `50,010,000,000`.

**F-TM-033 — Valid quantity and price.** *Provisional (MKT-136).*

```
valid_line      ⇔ integer(q) ∧ 1 ≤ q ≤ Q_max ∧ integer(p) ∧ 0 ≤ p ≤ P_max
valid_global    ⇔ integer(q) ∧ 1 ≤ q ≤ Q_max ∧ integer(p) ∧ 1 ≤ p ≤ P_max
valid_crowns    ⇔ integer(c) ∧ 0 ≤ c ≤ C_max
```
- **Output:** boolean; false → `E12` (or `E04` for a bound).
- **Validation:** `q = 0` → `E12`; `q = 100,001` → `E04`; a global `p = 0` → `E12`.

### 4.8 Limits and windows

**F-TM-034 — The action window.** *Provisional (MKT-061).*

```
actions_in_window = count( market_action a :
                           a.nation = n ∧
                           a.turn ≥ current_turn − T_act + 1 ∧
                           a.turn ≤ current_turn )
allow ⇔ actions_in_window < N_act
```
- **Inputs:** turn IDs; `T_act = 12`; `N_act = 20`.
- **Output:** boolean.
- **Validation:** 20 actions from turns 90–101 with current 101 → the 21st fails; on turn 102 the turn-90 action leaves and one slot opens.

**F-TM-035 — The listing caps.** *Provisional (MKT-124).*

```
allow_post ⇔ active_sell(n, r) + (side = SELL ? 1 : 0) ≤ N_sell
           ∧ active_buy(n, r)  + (side = BUY  ? 1 : 0) ≤ N_buy
           ∧ active_total(n) + 1 ≤ N_list
```
- **Output:** boolean; false → `MKT-L09`/`MKT-L10`/`MKT-L11`.
- **Validation:** four sell listings on food and a fifth → `L09`; twelve total and a thirteenth → `L11`.

**F-TM-036 — The execution cap.** *Provisional (MKT-205).*

```
allow_execution ⇔ accepted_executions(n, current_turn) < N_exec
                ∧ accepted_executions(world, current_turn) < N_world
```
- **Output:** boolean; false → `MKT-L13`/`MKT-L14`.
- **Validation:** the 51st execution for one nation → `L13`; the 5,001st world-wide → `L14`.

### 4.9 Conservation and fees

**F-TM-037 — The conservation identity.** *Provisional (MKT-166).*

```
Σ over nations of crown_delta = 0
for each resource r: Σ over nations of unit_delta(r) = 0
```
With a fee enabled:

```
Σ crown_delta + fee_total = 0
```
- **Output:** boolean, checked at P7.
- **Validation:** E18's four events; a fabricated missing `−200` fails.

**F-TM-038 — The fee.** *Provisional (MKT-068; deferred).*

```
fee_buyer  = floor( T × fee_bp_buyer / 10,000 ) + fee_flat_buyer
fee_seller = floor( T × fee_bp_seller / 10,000 ) + fee_flat_seller
fee_total  = fee_buyer + fee_seller
```
- **At launch:** all four parameters are `0`, so `fee_total = 0` and no `FEE` event is written.
- **Output:** crowns, integer.
- **Rounding:** one `floor` per rate; the flat part is exact.
- **Dependencies:** G-5; D-109…D-121 do not enable a fee.
- **Validation:** with the launch parameters, every example's `fee_total = 0`; a fabricated `fee_bp = 500` on `T = 1,600` gives `80`.

**F-TM-039 — Settlement completeness.** *Provisional (MKT-171).*

```
settled ⇔ both ledger events exist
        ∧ same transfer_id
        ∧ both reservations are closed
        ∧ listing/offer quantity identity holds
        ∧ F-TM-037 holds
```
- **Output:** boolean; false at P7 is a defect (`MKT-S10`), not a partial publication.
- **Validation:** E1/E7/E18 pass; a fabricated trade with one event fails.

---

## 5. Worked check values

These are the values the documentation checker recomputes. They are examples, not balance claims.

| Check | Expression | Value |
|---|---|---|
| E1 reference values | `200 + 100 × 1`; `50 × 7` | `300`; `350` |
| E1 bound | `floor(300 × 13,000 / 10,000)` | `390`; `350 ≤ 390` |
| E2 values | `100 + 40 × 2 + 20 × 1`; `20 × 8 + 5 × 3` | `200`; `175` |
| E2 bound | `floor(175 × 13,000 / 10,000)` | `227`; `200 ≤ 227` |
| E2 ratio | `floor(200 × 10,000 / 175)` | `11,428` bp |
| E5 bound | `floor(100 × 13,000 / 10,000)` | `130`; `200 > 130` |
| E5 boundary | `130 ≤ 130` | in band |
| E6 ratio | `floor(600 × 10,000 / 300)` | `20,000` bp |
| E7 fill | `200 × 8` | `1,600` |
| E7 remaining | `500 − 200 − 0` | `300` |
| E8 commitment | `400 × 2` | `800` |
| E8 remaining commitment | `(0 + 250) × 2`; `800 − 300` | `500`; `500` |
| E9 gap | `100 × 8 − 900` | `−100` |
| E10 two fills | `200 × 8`; `100 × 8`; `1,600 + 800` | `1,600`; `800`; `2,400` |
| E10 identity | `500 − 300 − 0` | `200` |
| E11 cancel | `500 − 200` | `300` released |
| E12 expiry | `10 + 72` | `82` |
| E13 crowns | `1,000 − 800`; `101 × 2` | `200`; `202 > 200` |
| E15 space | `2,000 − 1,950 − 0` | `50` |
| E20 boundary | `floor(100 × 13,000 / 10,000)` | `130` |
| F-TM-028 VWAP | `floor((800 + 1,800 + 350) / 350)` | `8` |
| F-TM-030 band | `floor(347 / 10) × 10` | `340` |
| F-TM-032 max | `10,000,000 + 5 × 100,000 × 100,000` | `50,010,000,000` |
| F-TM-038 fee | launch parameters | `0` |

---

## 6. Revision history

**F-TM-000e — Revision history.** *Provisional.* v1.1 (2026-10-29): Prompt 07C reconciliation — the band's asymmetric boundary examples and the space-reservation warning; no expression or constant changed. v1.0 (2026-10-28): first issue. No earlier version exists. The constants are the v1.0 provisional calibration; no value has been tuned, simulated or measured. The formula set covers the directed trade, the public listing, the fair-value band, the fresh window, the statistics and the conservation identity. **No constant changed after the initial issue.** The B-07 correction that follows this issue, if any, will be recorded here with the exact rows it touched.

**F-TM-000f — What is not validated.** *Provisional.* (1) No formula has been executed against a database or a scheduler. (2) The examples are hand calculations, not a simulation. (3) The reference prices are book values, not market prices. (4) No player has traded. (5) The band, caps, expiry and statistic thresholds are unmeasured. (6) The world execution ceiling is a placeholder for Stage 3's measurement. (7) No claim of balance, liquidity or anti-fraud effectiveness is made.

**End of register.**
