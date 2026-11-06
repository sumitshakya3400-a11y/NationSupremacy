# Economic formula and balance register

**Version:** 1.4 · **Created:** 2026-10-24 · **Stage 2, Prompt 04** · **Revised:** 2026-11-04 (v1.4 Prompt 10B-C2 updates **F-EC-003** to the protected-civilian-Food model: `available_if_held` and `available_after_release` are distinct, `unmet_food` is computed after any `OP-09` release in reverse acceptance order, and the dependency on B-10 `WAR-053l` is explicit. No constant or tax coefficient changed. The v1.3 text follows for history: v1.3 records **ECN-147a** in F-EC-014: maintenance is one whole obligation per chain, attempted in the extraction → generation → processing order, paid or cancelled whole, with a published standard-start allocation (1 crown → oil paid, five chains `UNMAINTAINED`, treasury 0). No constant or formula value changed. Earlier: 2026-10-25 — v1.2 corrects F-EC-006: `planned_batches = M + A ≤ C`, where manual batches occupy capacity instead of being added to it, with the worked-example index and the F-EC-006 example updated. No coefficient changed. Earlier: v1.1 numerical correction pass — bundle total, F-EC-021/023 examples, the worked-example index and the validation record; see F-EC-044)
**Status:** **Draft** — definitive formula definitions; **no formula has been implemented or runtime-tested.**
**Authority:** This register is the **single authoritative source** for the expression, variables, units, bounds, rounding, timing and dependencies of every economic formula in Nation Supremacy. [B-04](10_economy_resources_treasury_and_finances.md) summarises these formulas; if the two disagree, this register wins until it is corrected by a new revision.
**Companions:** [B-04](10_economy_resources_treasury_and_finances.md) · [research report](research/04_politics_and_war_economy_research.md) · [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [requirements](03_requirements_traceability.md)

---

## 1. How to use this register

**F-EC-000 — Register rules.** *Provisional.*

1. Every economic formula has exactly one `F-EC-###` row in §4. No other document may define a competing expression.
2. A formula is cited by ID, never by a nickname.
3. A number change is a new revision with a date and a reason; the old value is kept in the revision history.
4. A formula that depends on a later prompt's input says so in its **Dependencies** field. The dependency is an interface, not an excuse to leave the formula undefined.
5. A formula is not "validated" because the algebra is consistent. Validation means a test was executed; **zero tests have been executed**.

**F-EC-000a — Status vocabulary.** *Provisional.* **Confirmed (design)** means the rule is selected; **Provisional** means a number or coefficient may change at Prompt 14; **Deferred** means a later prompt owns the input. No formula is approved, implemented or tested.

---

## 2. Numerical conventions

**F-EC-000b — Integer arithmetic.** *Provisional (REQ-162).* All quantities are integers. Every division states its rounding: `floor` (toward negative infinity for negative values; toward zero for the positive values used here), `ceil` or `round_half_up`. No formula uses binary floating point. A percentage is an integer in **basis points** (bp), where 10,000 bp = 100%.

**F-EC-000c — Units.** *Provisional.* Units are stated per formula: `crowns`, `units`, `batches`, `GU`, `people`, `bp`, `turns`. A quantity without a unit is not a valid formula input.

**F-EC-000d — Boundary timing.** *Provisional.* All economic formulas run at the two-hour UTC boundary, inside B-02's P3 or P4. No formula runs continuously, on a browser timer or on a per-request basis except the submission checks in §4.19.

**F-EC-000e — Ordering.** *Provisional.* The P3 order is F-EC-001 (tax), F-EC-014 (maintenance), F-EC-004 (extraction), F-EC-013 (power), F-EC-006/007/008 (processing), F-EC-002/003 (food), obligations, close. A formula that reads a later sub-phase's output is invalid.

---

## 3. Constants and calibrated tables

**F-EC-000f — Constants are versioned.** *Provisional.* The constants below are the **v1.0 provisional calibration**, carried unchanged into v1.1 (see F-EC-044). They are not observed prices and not balance claims. Prompt 14 may change a value only by a new revision of this register.

### 3.1 Standard starting bundle (D-063)

| Item | Value | Unit |
|---|---|---|
| Treasury | 1,500 | crowns |
| Population | 50,000 | people |
| Warehouse capacity | 2,000 | units |
| Tax rate | 300 | bp |
| Stability factor | 10,000 | bp |
| Food | 120 | units |
| Coal | 60 | units |
| Oil | 30 | units |
| Iron | 30 | units |
| Bauxite | 20 | units |
| Lead | 10 | units |
| Uranium | 0 | units |
| Gasoline | 20 | units |
| Ammunition | 0 | units |
| Steel | 20 | units |
| Aluminum | 0 | units |
| Food capacity | 3 | batches |
| Coal capacity | 2 | batches |
| Oil capacity | 1 | batch |
| Iron capacity | 1 | batch |
| Bauxite / lead / uranium capacity | 0 | batches |
| Refining capacity | 1 | batch |
| Steel / aluminum / ammunition capacity | 0 | batches |
| Coal generator | 1 | level |

The bundle occupies **310 units** of warehouse space (`120 + 60 + 30 + 30 + 20 + 10 + 0 + 20 + 0 + 20 + 0 = 310`), leaving 1,690 of the 2,000 units free.

### 3.2 Extraction coefficients

| Resource | Output per batch `Y` | Variable cost per batch `V` | Maintenance per batch | Reference price |
|---|---|---|---|---|
| Food | 20 | 12 | 1 | 1 |
| Coal | 10 | 10 | 1 | 1 |
| Oil | 8 | 14 | 1 | 2 |
| Iron | 10 | 10 | 1 | 1 |
| Bauxite | 8 | 14 | 1 | 2 |
| Lead | 6 | 16 | 1 | 3 |
| Uranium | 1 | 28 | 1 | 30 |

### 3.3 Processing recipes

| Chain | Inputs per batch | Output per batch | Variable cost | Power draw | Maintenance |
|---|---|---|---|---|---|
| Refining | 10 oil | 8 gasoline | 20 | 2 GU | 2 |
| Steel | 10 iron + 6 coal | 8 steel | 24 | 3 GU | 2 |
| Aluminum | 12 bauxite | 8 aluminum | 24 | 4 GU | 2 |
| Ammunition | 8 lead + 4 coal | 10 ammunition | 20 | 2 GU | 2 |

### 3.4 Generators

| Generator | Capacity per level | Fuel per level per turn | Variable cost per level | Maintenance per level |
|---|---|---|---|---|
| Coal | 6 GU | 6 coal | 10 | 2 |
| Oil | 6 GU | 5 oil | 14 | 2 |
| Nuclear | 20 GU | 1 uranium + 1 lead | 40 | 2 |

### 3.5 Reference prices (book values, not market prices)

| Resource | Price (crowns/unit) |
|---|---|
| Food | 1 |
| Coal | 1 |
| Oil | 2 |
| Iron | 1 |
| Bauxite | 2 |
| Lead | 3 |
| Uranium | 30 |
| Gasoline | 6 |
| Steel | 7 |
| Aluminum | 8 |
| Ammunition | 6 |

**F-EC-000g — Why these reference prices.** *Provisional.* Each is set near the **full cost** of producing one unit at a representative scale: extraction variable cost divided by output, plus a processing margin. The prices are deliberately round numbers so a player can do the arithmetic mentally. They are not promises that a unit can be sold for that amount. The register's §6 margin table shows the resulting per-batch margins.

---

---

## 4. The formula register

Each entry states: expression, variables, units, range, rounding, timing, dependencies, worked example, rationale, edge cases, validation and requirements. A formula with a missing field is incomplete.

### 4.1 Income and food

**F-EC-001 — Tax income.**

| Field | Definition |
|---|---|
| Expression | `tax_income = floor(population × tax_rate_bp × stability_factor_bp / 1,000,000,000)` |
| Variables | `population` (people, integer ≥ 0); `tax_rate_bp` (bp, 0…10,000); `stability_factor_bp` (bp, 5,000…11,000) |
| Units | Output: crowns (integer) |
| Range | 0 … `population × 11,000 / 100,000` crowns; no negative |
| Rounding | Floor to whole crowns |
| Timing | P3.1, after applying the stored hunger penalty |
| Dependencies | Prompt 06 supplies population, tax rate and stability; the hunger penalty is F-EC-003 |
| Example | `floor(50,000 × 300 × 10,000 / 1,000,000,000) = 150` crowns |
| Rationale | One visible lever: more people or a higher rate raises income; stability is the political brake |
| Edge cases | Population 0 → 0; stability 0 is outside the range and must be clamped to 5,000; a rate above 10,000 is invalid, not a money printer |
| Validation | T04-B01 |
| Requirements | REQ-132 |

**F-EC-002 — Food demand.**

| Field | Definition |
|---|---|
| Expression | `food_demand = ceil(population / 1,000)` |
| Variables | `population` (people, integer ≥ 0) |
| Units | Output: food units per turn |
| Range | 0 … `ceil(max_population / 1,000)` |
| Rounding | Ceiling; one unit feeds up to 1,000 people |
| Timing | P3.6 |
| Dependencies | Prompt 06 supplies population |
| Example | `ceil(50,000 / 1,000) = 50` units |
| Rationale | A legible, linear staple: population growth raises demand predictably |
| Edge cases | 1 person → 1 unit (ceil); 0 people → 0; a population change at P4 does not change this turn's demand |
| Validation | T04-C01 |
| Requirements | REQ-127 |

**F-EC-002a — Military Food demand is a separate formula.** *Provisional.* The garrison ration is **not** part of `food_demand` and never changes the hunger ratio. It is computed by `F-WR-036` in the B-10 warfare formula register and paid at P3.7 rank 6(a) from the Food left after P3.6. A formula or screen that adds it to `food_demand` is incorrect.

**F-EC-003 — Hunger penalty.**

| Field | Definition |
|---|---|
| Expression | `hunger_penalty_bp = min(3,000, floor(3,000 × unmet_food / food_demand))`, with `unmet_food = max(0, food_demand − available_after_release)` and `hunger_penalty_bp = 0` when `food_demand = 0` |
| Variables | `unmet_food` (units); `food_demand = protected_civilian_food` (units); `food_after_other = opening + produced − other_food_reservations`; `available_if_held = food_after_other − op09_held_total`; `available_after_release = food_after_other − op09_held_after_release` (units) |
| Units | Output: basis points (0…3,000) |
| Range | 0…3,000 bp (0–30%) |
| Rounding | Floor; cap at 3,000 |
| Timing | Computed at P3.6, stored, applied at the next P3.1 |
| Dependencies | B-10 `WAR-053l` supplies `op09_held_total` and the release order; Prompt 06 may add a stability effect but may not change this formula |
| Example | `unmet 20, demand 50 → floor(3,000×20/50) = 1,200 bp`; next tax `floor(150×8,800/10,000) = 132`. With opening 20, production 40, demand 50 and one OP-09 holding 4: `food_after_other = 54`, `available_if_held = 50 ≥ 50`, so the reservation stands and `unmet = 0`. With production 35: `food_after_other = 49`, `available_if_held = 45 < 50`, so the OP-09 reservation is released, `available_after_release = 49`, `unmet = 1` |
| Rationale | Graduated, forecastable, recoverable; no one-third cliff; civilian demand is protected before any OP-09 field ration |
| Edge cases | Demand 0 → 0; unmet 0 → 0; unmet = demand → 3,000; a 1-unit unmet in a 100,000-person nation rounds to 30 bp, not 0; an OP-09 reservation is never allowed to create unmet civilian demand while it can be released |
| Validation | T04-C02/C03 |
| Requirements | REQ-128 |

**F-EC-004 — Extraction batches.**

| Field | Definition |
|---|---|
| Expression | `batches_run = min(C, floor(available_crowns / V), floor(free_space / Y))` |
| Variables | `C` (capacity, batches ≥ 0); `available_crowns` (crowns, integer ≥ 0); `V` (variable cost per batch, crowns > 0); `free_space` (units ≥ 0); `Y` (output per batch, units > 0) |
| Units | Output: batches (integer) |
| Range | 0 … `C` |
| Rounding | Floor each limit, then take the minimum |
| Timing | P3.3, per resource in the published order |
| Dependencies | F-EC-014 (maintenance already charged); F-EC-023 (free space) |
| Example | `C=5, V=10, available=100, Y=10, free=25 → min(5, 10, 2) = 2` batches |
| Rationale | A batch is atomic; the strictest constraint wins |
| Edge cases | `V=0` is invalid (undefined); `free_space < Y` → 0; negative crowns → 0 |
| Validation | T04-D01/C04 |
| Requirements | REQ-112/141 |

**F-EC-005 — Extraction variable cost.**

| Field | Definition |
|---|---|
| Expression | `variable_cost = batches_run × V` |
| Variables | `batches_run` (integer ≥ 0); `V` (crowns per batch) |
| Units | Output: crowns |
| Range | 0 … `C × V` |
| Rounding | None (integer multiplication) |
| Timing | P3.3, charged as each batch runs |
| Dependencies | F-EC-004 |
| Example | `2 × 10 = 20` crowns |
| Rationale | Cost follows the batch, not the capacity; an idle batch costs only maintenance |
| Edge cases | 0 batches → 0 cost; a blocked batch never incurs `V` |
| Validation | T04-B02 |
| Requirements | REQ-112 |

### 4.2 Power and processing

**F-EC-006 — Power demand.**

| Field | Definition |
|---|---|
| Expression | `power_demand = Σ_chains (planned_batches × draw_per_batch)`, where `planned_batches = M + A` and `M + A ≤ C` |
| Variables | `C` = chain capacity (batches); `M` = accepted manual batches reserved this turn; `A` = automatic batches the standing policy schedules in the unreserved slots (`0 ≤ A ≤ C − M`), computed before derating; `draw_per_batch` = 2/3/4/2 GU for refining/steel/aluminum/ammunition |
| Units | Output: grid units (GU) |
| Range | 0 … `Σ(capacity × draw)` |
| Rounding | None (integer sum) |
| Timing | P3.5, before any processing |
| Dependencies | Prompt 05 capacity; F-EC-012 |
| Example | Refining `C=2, M=0, A=2` → 4 GU, plus steel `C=2, M=1, A=1` → 6 GU, total 10 GU; refining `C=2, M=2` → `P=2`, **4 GU, never 8** |
| Rationale | Demand is computed once so the derating is fair and order-independent |
| Edge cases | No processing → 0; `M = 0` and `A = 0` → 0; an accepted manual order that later fails still counts in the plan used for `power_pct`, because the grid is sized before the failure; a manual batch **occupies** a slot and is never added on top of `C`; `planned_batches = C + M` is invalid because it would exceed the chain's capacity |
| Validation | T04-D05 |
| Requirements | REQ-119 |

**F-EC-007 — Power percentage.**

| Field | Definition |
|---|---|
| Expression | `power_pct = 10,000` if `supply ≥ demand`, otherwise `floor(10,000 × supply / demand)` |
| Variables | `supply` (GU); `demand` (GU) |
| Units | Output: basis points (0…10,000) |
| Range | 0…10,000 bp |
| Rounding | Floor |
| Timing | P3.5 |
| Dependencies | F-EC-006; F-EC-013 |
| Example | `supply 6, demand 10 → floor(10,000×6/10) = 6,000 bp (60%)` |
| Rationale | One published percentage for every chain; no hidden priority |
| Edge cases | Demand 0 → 10,000; supply 0 → 0; supply > demand → 10,000 |
| Validation | T04-D05 |
| Requirements | REQ-120 |

**F-EC-008 — Processing batches available.**

| Field | Definition |
|---|---|
| Expression | `batches_available = floor(C × power_pct / 10,000)` |
| Variables | `C` (capacity, batches ≥ 0); `power_pct` (bp) |
| Units | Output: batches |
| Range | 0 … `C` |
| Rounding | Floor |
| Timing | P3.5, before manual orders |
| Dependencies | F-EC-007 |
| Example | `C=2, pct=6,000 → floor(2×0.6) = 1` batch |
| Rationale | Conservative and deterministic; a level-1 chain at 60% idles, which is the visible cost of underbuilding power |
| Edge cases | `C=1, pct=9,999 → 0`; `C=0 → 0`; a manual order needing more than `batches_available` fails atomically |
| Validation | T04-D05 |
| Requirements | REQ-120 |

**F-EC-009 — Processing input limit.**

| Field | Definition |
|---|---|
| Expression | `input_limit = min_over_inputs(floor(available_input / required_per_batch))` |
| Variables | `available_input` (units, unreserved); `required_per_batch` (units > 0) |
| Units | Output: batches |
| Range | 0 … `C` |
| Rounding | Floor per input, then minimum |
| Timing | P3.5 |
| Dependencies | F-EC-022 (available inventory) |
| Example | Iron 100, coal 100, steel recipe 10+6 → `min(10, 16) = 10`, capped at capacity |
| Rationale | The scarcest input decides; no substitution |
| Edge cases | A reserved input is excluded; an input of 9 for a 10-required batch → 0 batches, and the 9 is not consumed |
| Validation | T04-D07 |
| Requirements | REQ-121/123 |

**F-EC-010 — Processing money limit.**

| Field | Definition |
|---|---|
| Expression | `money_limit = floor(available_crowns / V)` |
| Variables | `available_crowns` (crowns); `V` (crowns per batch > 0) |
| Units | Output: batches |
| Range | 0 … `C` |
| Rounding | Floor |
| Timing | P3.5 |
| Dependencies | F-EC-019 (available balance) |
| Example | 100 crowns, 24/batch → 4 batches, capped at capacity |
| Rationale | No credit; a batch is funded in full |
| Edge cases | 23 crowns, 24/batch → 0; reserved crowns are excluded |
| Validation | T04-B06 |
| Requirements | REQ-133 |

**F-EC-011 — Processing space limit.**

| Field | Definition |
|---|---|
| Expression | `space_limit = floor(free_space / output_per_batch)` |
| Variables | `free_space` (units ≥ 0); `output_per_batch` (units > 0) |
| Units | Output: batches |
| Range | 0 … `C` |
| Rounding | Floor |
| Timing | P3.5 |
| Dependencies | F-EC-023 |
| Example | Free space 5, steel output 8 → 0 batches |
| Rationale | No overflow and no destruction |
| Edge cases | A manual order reserves output space at acceptance, so standing policy sees the reduced free space |
| Validation | T04-C04 |
| Requirements | REQ-142 |

**F-EC-012 — Processing output.**

| Field | Definition |
|---|---|
| Expression | `output = batches_run × output_per_batch`; `inputs_consumed = batches_run × input_per_batch` |
| Variables | `batches_run` (integer ≥ 0); `output_per_batch`, `input_per_batch` (units) |
| Units | Output and inputs: units |
| Range | 0 … `C × output_per_batch` |
| Rounding | None (integer multiplication) |
| Timing | P3.5, atomically with the cost |
| Dependencies | F-EC-008/009/010/011 |
| Example | 2 steel batches → 16 steel; 20 iron + 12 coal consumed |
| Rationale | Fixed recipe, no yield randomness |
| Edge cases | A blocked batch consumes no input; a manual order that fails consumes nothing |
| Validation | T04-D07 |
| Requirements | REQ-121 |

**F-EC-013 — Generator output and fuel.**

| Field | Definition |
|---|---|
| Expression | If full fuel and variable cost are available: `GU = level × capacity_per_level`, `fuel_consumed = level × fuel_per_level`, `cost = level × V`; otherwise `GU = 0`, `fuel_consumed = 0`, `cost = 0` |
| Variables | `level` (integer ≥ 0); `capacity_per_level` (6 or 20 GU); `fuel_per_level` (6 coal / 5 oil / 1 uranium + 1 lead); `V` (10/14/40 crowns) |
| Units | GU, units, crowns |
| Range | 0 … `level × 20` GU |
| Rounding | None |
| Timing | P3.4, coal → oil → nuclear |
| Dependencies | F-EC-021/022 (fuel inventory); F-EC-019 (crowns) |
| Example | One coal level: 6 GU, 6 coal, 10 crowns; one nuclear level: 20 GU, 1 uranium + 1 lead, 40 crowns |
| Rationale | Fail-closed, no partial burn; surplus is discarded |
| Edge cases | 5 coal for a 6-coal generator → 0 GU and 0 coal consumed; a nuclear level with uranium but no lead → 0 GU |
| Validation | T04-D06 |
| Requirements | REQ-119 |

### 4.3 Treasury, maintenance and inventory

**F-EC-014 — Maintenance.**

| Field | Definition |
|---|---|
| Expression | `maintenance = Σ_extraction(C_extraction × 1) + Σ_processing(C_processing × 2) + Σ_generators(levels × 2)` |
| Variables | Capacity in batches; generator levels |
| Units | Output: crowns |
| Range | 0 … a nation's total capacity × 2 |
| Rounding | None (integer sum) |
| Timing | P3.2, after tax and before extraction |
| Dependencies | Prompt 05 capacity |
| Example | Standard start: 3+2+1+1 + 2 + 2 = 11 crowns |
| Rationale | Idle capacity is not free; this is the anti-hoarding cost |
| Edge cases | One **whole** obligation per chain, attempted in **ECN-147a**'s order (extraction → generation → processing); paid in full or cancelled in full, and the engine continues past an unaffordable chain; a cancelled chain is `UNMAINTAINED` and cannot run this turn; the mark clears at the next P3.2 in which its obligation is paid; a capacity of 0 costs 0 |
| Allocation | Standard start, 1 crown: food 3 and coal 2 cancelled, **oil 1 paid**, iron 1, generator 2 and refining 2 cancelled — five `UNMAINTAINED`, treasury 0 (D-050) |
| Validation | T04-B02 |
| Requirements | REQ-116 |

**F-EC-015 — Gross income.**

| Field | Definition |
|---|---|
| Expression | `gross_income = tax_income + one_time_rewards` |
| Variables | `tax_income` (crowns); `one_time_rewards` (crowns, ledgered) |
| Units | Crowns |
| Range | 0 … |
| Rounding | None |
| Timing | P3.1 and P4 (rewards) |
| Dependencies | F-EC-001; Prompt 11 rewards |
| Example | 150 + 0 = 150 |
| Rationale | Gross is before expenses; it is not profit |
| Edge cases | A reward at P4 is not available to pay P3 costs; it is next turn's liquidity |
| Validation | T04-B02 |
| Requirements | REQ-131 |

**F-EC-016 — Net operating income.**

| Field | Definition |
|---|---|
| Expression | `net_operating_income = gross_income − operating_expenses`, where `operating_expenses = maintenance + extraction_variable + generator_variable + processing_variable` |
| Variables | Crowns |
| Units | Crowns |
| Range | Can be negative; no floor (it is a statistic, not a balance) |
| Rounding | None |
| Timing | P3.8 |
| Dependencies | F-EC-005/012/013/014/015 |
| Example | 150 − 121 = 29 |
| Rationale | Separates running the nation from investing in it |
| Edge cases | Capex is excluded; a trade is excluded; a reward is included |
| Validation | T04-B02/B03 |
| Requirements | REQ-131 |

**F-EC-017 — Net cash flow.**

| Field | Definition |
|---|---|
| Expression | `net_cash_flow = closing_treasury − opening_treasury` |
| Variables | Crowns |
| Units | Crowns |
| Range | Any integer |
| Rounding | None |
| Timing | P3.8/P4 close |
| Dependencies | F-EC-018 |
| Example | 1,529 − 1,500 = +29 |
| Rationale | The single number that tells a player whether the turn added or removed liquidity |
| Edge cases | A construction turn can have positive operating income and negative cash flow |
| Validation | T04-B05 |
| Requirements | REQ-131 |

**F-EC-018 — Closing treasury.**

| Field | Definition |
|---|---|
| Expression | `closing = opening + tax + rewards + sale_proceeds + transfers_in + refunds − operating − capex − purchase_costs − transfers_out − fees` |
| Variables | All terms are integer crowns |
| Units | Crowns |
| Range | ≥ 0 (non-negative invariant) |
| Rounding | None; the identity must hold to the crown |
| Timing | P3.8 for the economic part; P4 adds capex/trade; P7 publishes |
| Dependencies | F-EC-001/016; Prompt 05/07/08 |
| Example | `1,500 + 150 − 121 = 1,529` |
| Rationale | One reconciling identity for every flow |
| Edge cases | If any term would make the balance negative, the underlying action must fail or be cancelled first |
| Validation | T04-B05/B06 |
| Requirements | REQ-132/139 |

**F-EC-019 — Available balance.**

| Field | Definition |
|---|---|
| Expression | `available = total_treasury − reserved_total` |
| Variables | Crowns |
| Units | Crowns |
| Range | 0 … total; never negative |
| Rounding | None |
| Timing | Any read; authoritative at submission and P3 |
| Dependencies | F-EC-020 |
| Example | `1,529 − 40 = 1,489` |
| Rationale | A player sees what they can actually spend |
| Edge cases | A reservation larger than the balance is an invariant violation; the accepting action is rejected |
| Validation | T04-D03 |
| Requirements | REQ-137 |

**F-EC-020 — Reserved total.**

| Field | Definition |
|---|---|
| Expression | `reserved_total = Σ(active money reservations)` |
| Variables | One row per accepted action |
| Units | Crowns |
| Range | 0 … total_treasury |
| Rounding | None |
| Timing | Every acceptance/release |
| Dependencies | B-02 reservation model; ECN-126 |
| Example | Two orders reserving 40 and 20 → 60 |
| Rationale | Exclusive claims prevent double spend |
| Edge cases | A released reservation is removed exactly once; a consumed reservation is removed and charged |
| Validation | T04-D03/D04 |
| Requirements | REQ-137 |

**F-EC-021 — Inventory total.**

| Field | Definition |
|---|---|
| Expression | `total_inventory = Σ_resource total_units(r)` |
| Variables | Per-resource integer totals |
| Units | Units (shared warehouse) |
| Range | 0 … `W` |
| Rounding | None |
| Timing | After every inventory change |
| Dependencies | F-EC-012/013/022 |
| Example | Standard start: 310 units |
| Rationale | One number for the shared warehouse |
| Edge cases | A reserved unit is included in total; a consumed unit is not |
| Validation | T04-C05 |
| Requirements | REQ-141 |

**F-EC-022 — Inventory available.**

| Field | Definition |
|---|---|
| Expression | `available_units(r) = total_units(r) − reserved_units(r)` |
| Variables | Per-resource integers |
| Units | Units |
| Range | 0 … total |
| Rounding | None |
| Timing | At every read and reservation check |
| Dependencies | ECN-125/126 |
| Example | 28 oil total, 10 reserved → 18 available |
| Rationale | The same split as money; no mental subtraction |
| Edge cases | Reserved > total is an invariant violation and blocks the action |
| Validation | T04-D03 |
| Requirements | REQ-143 |

**F-EC-023 — Free warehouse space.**

| Field | Definition |
|---|---|
| Expression | `free_space = W − total_inventory` |
| Variables | `W` (capacity, units); `total_inventory` (units) |
| Units | Units |
| Range | 0 … `W` |
| Rounding | None |
| Timing | Before every production or purchase |
| Dependencies | F-EC-021; Prompt 05 expansion |
| Example | `2,000 − 310 = 1,690` |
| Rationale | The overflow gate |
| Edge cases | A reserved output space reduces the free space available to another order |
| Validation | T04-C04 |
| Requirements | REQ-142 |

**F-EC-024 — National wealth.**

| Field | Definition |
|---|---|
| Expression | `wealth = treasury + inventory_book_value + fixed_asset_book_value` |
| Variables | Crowns; book values in crowns |
| Units | Crowns (an estimate) |
| Range | ≥ 0 |
| Rounding | None; each component is an integer |
| Timing | P3.8 report |
| Dependencies | F-EC-025/026 |
| Example | `1,529 + 678 + 0 = 2,207` |
| Rationale | Distinguishes liquid from total value |
| Edge cases | A market crash does not change book value; a sale does |
| Validation | T04-B08 |
| Requirements | REQ-136 |

**F-EC-025 — Inventory book value.**

| Field | Definition |
|---|---|
| Expression | `inventory_book_value = Σ_resource total_units(r) × reference_price(r)` |
| Variables | Units; crowns per unit |
| Units | Crowns |
| Range | 0 … `W × max_price` |
| Rounding | None |
| Timing | P3.8 report |
| Dependencies | §3.5 prices |
| Example | `130×1 + 74×1 + 28×2 + 40×1 + 20×2 + 10×3 + 28×6 + 20×7 = 678` |
| Rationale | A stable accounting value, not a market claim |
| Edge cases | A price of 0 would make a resource free; no reference price is 0 |
| Validation | T04-B08 |
| Requirements | REQ-136 |

**F-EC-026 — Fixed-asset book value.**

| Field | Definition |
|---|---|
| Expression | `fixed_asset_book_value = Σ_completed_construction(crown_cost + Σ_material_cost(reference_price × quantity))` |
| Variables | Completed construction records |
| Units | Crowns |
| Range | ≥ 0 |
| Rounding | None |
| Timing | Updated at P4 when a construction completes |
| Dependencies | Prompt 05 construction record; F-EC-027 |
| Example | 150 + 10×7 = 220 |
| Rationale | Construction converts liquid assets into a durable asset; it does not destroy wealth |
| Edge cases | No depreciation in v1; an abandoned project does not add value |
| Validation | T04-B04 |
| Requirements | REQ-136 |

**F-EC-027 — Construction book value.**

| Field | Definition |
|---|---|
| Expression | `construction_book_value = crown_cost + Σ(material_quantity × reference_price)` |
| Variables | Crowns; units; prices |
| Units | Crowns |
| Range | ≥ 0 |
| Rounding | None |
| Timing | At completion (P4) |
| Dependencies | Prompt 05 cost table; §3.5 |
| Example | 150 + 10×7 + 5×6 = 250 |
| Rationale | Avoids a phantom wealth loss when materials are consumed |
| Edge cases | A construction with no material cost has book value = crown cost |
| Validation | T04-B04 |
| Requirements | REQ-136 |

### 4.4 Trade, conservation and audit

**F-EC-028 — Trade fee.**

| Field | Definition |
|---|---|
| Expression | `fee = floor(gross_value × fee_bp / 10,000)`; `seller_net = gross_value − fee` |
| Variables | `gross_value` (crowns); `fee_bp` (bp, 0…1,000) |
| Units | Crowns |
| Range | 0 … 10% of gross |
| Rounding | Floor; the fee is destroyed, not transferred |
| Timing | At trade settlement (P4) |
| Dependencies | Prompt 07 (fee policy); D-016/D-017 |
| Example | `160 × 200 / 10,000 = 3`; seller nets 157 |
| Rationale | A disclosed sink; no hidden spread |
| Edge cases | `fee_bp=0` → 0; a 1-crown trade with 2% → 0, not 1 |
| Validation | T04-F04 |
| Requirements | REQ-174 |

**F-EC-029 — Transfer conservation.**

| Field | Definition |
|---|---|
| Expression | For every transfer: `Δseller(resource) + Δbuyer(resource) = 0`; `Δseller(crowns) + Δbuyer(crowns) = 0` |
| Variables | Signed integer deltas |
| Units | Units or crowns |
| Range | Exact zero |
| Rounding | None |
| Timing | P4, atomically |
| Dependencies | Prompt 07/08 |
| Example | Seller −20 steel, buyer +20 steel; seller +160 crowns, buyer −160 |
| Rationale | Trade moves value; it does not create it |
| Edge cases | A fee breaks the crown identity by the fee amount, which is recorded separately |
| Validation | T04-F04 |
| Requirements | REQ-174 |

**F-EC-030 — Money conservation.**

| Field | Definition |
|---|---|
| Expression | `Σ closing = Σ opening + Σ tax + Σ rewards + Σ administrative_credits − Σ operating − Σ capex − Σ fees` |
| Variables | World totals, integer crowns |
| Units | Crowns |
| Range | Exact identity |
| Rounding | None |
| Timing | P7 world check |
| Dependencies | F-EC-018/028 |
| Example | A two-nation trade cancels; only the fee changes the total |
| Rationale | Detects a mint or a leak |
| Edge cases | A disaster restore may break the identity for the lost turns; the gap is disclosed (D-025) |
| Validation | T04-I03 |
| Requirements | REQ-138 |

**F-EC-031 — Reference margin per batch.**

| Field | Definition |
|---|---|
| Expression | `margin = Σ(output_qty × reference_price) − Σ(input_qty × reference_price) − variable_cost − allocated_maintenance` |
| Variables | Quantities; prices; crowns |
| Units | Crowns per batch |
| Range | Any integer |
| Rounding | None |
| Timing | Report only; not a settlement rule |
| Dependencies | §3.2–3.5 |
| Example | Steel: `8×7 − (10×1 + 6×1) − 24 − 2 = 56 − 16 − 26 = 14` |
| Rationale | Makes a chain's economics visible without a market price |
| Edge cases | A negative margin is a warning, not an automatic stop |
| Validation | T04-H04/I02 |
| Requirements | REQ-160 |

**F-EC-032 — Payback turns.**

| Field | Definition |
|---|---|
| Expression | `payback_turns = ceil(construction_book_value / max(1, margin_per_turn))` |
| Variables | Crowns; crowns/turn |
| Units | Turns |
| Range | ≥ 1; undefined if margin ≤ 0 (report "never at this price") |
| Rounding | Ceiling |
| Timing | Report only |
| Dependencies | F-EC-027/031 |
| Example | `ceil(250 / 7) = 36` turns |
| Rationale | A legible investment estimate |
| Edge cases | Margin 0 → "never"; a price change changes the estimate, so it is labelled a forecast |
| Validation | T04-B04 |
| Requirements | REQ-160 |

**F-EC-033 — Settlement event key.**

| Field | Definition |
|---|---|
| Expression | `event_key = H(turn_id, nation_id, phase, entity, sequence)` |
| Variables | Integers/strings; `H` is a stable hash agreed at Stage 5 |
| Units | Opaque string |
| Range | Unique per logical event |
| Rounding | None |
| Timing | At event write |
| Dependencies | B-02 idempotency; Stage 5 hash choice |
| Example | `H(812,42,'P3.1','tax',1)` |
| Rationale | Exactly-once at the event level |
| Edge cases | A hash collision is treated as a defect and aborts the turn |
| Validation | T04-F02 |
| Requirements | REQ-151 |

**F-EC-034 — Settlement idempotency key.**

| Field | Definition |
|---|---|
| Expression | `settlement_key = (turn_id, nation_id)` |
| Variables | Integers |
| Units | Composite key |
| Range | One row per nation-turn |
| Rounding | None |
| Timing | At settlement start |
| Dependencies | B-02 |
| Example | `(812, 42)` |
| Rationale | A duplicate run reads the existing row |
| Edge cases | A different configuration version is a conflict, not a re-run |
| Validation | T04-E02 |
| Requirements | REQ-150 |

**F-EC-035 — Wealth reconciliation.**

| Field | Definition |
|---|---|
| Expression | `Δwealth = Δtreasury + Δinventory_book_value + Δfixed_asset_book_value` |
| Variables | Crowns |
| Units | Crowns |
| Range | Exact identity |
| Rounding | None |
| Timing | P3.8 report |
| Dependencies | F-EC-024/025/026 |
| Example | `2,207 − 2,100 = 29 + 78` |
| Rationale | Explains a wealth change even when cash and inventory move in opposite directions |
| Edge cases | A market-price change does not affect book wealth; a fee reduces it |
| Validation | T04-B08 |
| Requirements | REQ-136 |

---

---

## 5. Reference margin and balance table

**F-EC-036 — Base margin table.** *Provisional.* The margin is the value of the output at reference prices minus the value of the inputs, the variable cost and the allocated maintenance. It **excludes** the generator's power cost, which is reported separately (see the note below). A negative margin is not an error; it is a statement that the raw good is worth more inside a chain than sold on its own.

| Chain | Output value | Input value | Variable | Maint. | **Base margin** |
|---|---|---|---|---|---|
| Food extraction | 20 | 0 | 12 | 1 | **+7** |
| Coal extraction | 10 | 0 | 10 | 1 | **−1** |
| Oil extraction | 16 | 0 | 14 | 1 | **+1** |
| Iron extraction | 10 | 0 | 10 | 1 | **−1** |
| Bauxite extraction | 16 | 0 | 14 | 1 | **+1** |
| Lead extraction | 18 | 0 | 16 | 1 | **+1** |
| Uranium extraction | 30 | 0 | 28 | 1 | **+1** |
| Refining | 48 | 20 | 20 | 2 | **+6** |
| Steel | 56 | 16 | 24 | 2 | **+14** |
| Aluminum | 64 | 24 | 24 | 2 | **+14** |
| Ammunition | 60 | 28 | 20 | 2 | **+10** |

**F-EC-037 — Power cost is separate.** *Provisional.* At the reference fuel prices, one GU costs approximately **3.0 crowns** from coal, **4.3** from oil and **3.8** from nuclear (fuel book value + variable + maintenance, divided by GU). A fully loaded chain margin subtracts `draw × 3.0` for a coal-powered nation:

| Chain | Base margin | Power (coal, 3.0/GU) | **Fully loaded** |
|---|---|---|---|
| Refining | +6 | −6 | **0** |
| Steel | +14 | −9 | **+5** |
| Aluminum | +14 | −12 | **+2** |
| Ammunition | +10 | −6 | **+4** |

Refining is break-even at the reference gasoline price when powered by coal. That is deliberate: refining's value is the **gasoline price** and the construction/military demand, not a guaranteed arbitrage. If the market price of gasoline is 7 instead of 6, the fully loaded margin is **+8** per batch (one extra crown on each of eight units); at 5 it is −8. A player who wants a refining business must find a buyer, not rely on the reference price.

**F-EC-038 — Dominance test.** *Provisional.* A chain is **dominant** if it has (a) the highest base margin **and** the lowest capital cost per batch **and** the lowest operating risk, or (b) an output that every other chain requires with no substitute. At v1.0, food has the highest extraction margin but its demand is capped by population and storage; steel and aluminum have the highest processing margins but require power and construction capital; refining is break-even under coal power. No chain meets both (a) and (b). Prompt 14 must re-run this test after any number change.

**F-EC-039 — Money-creation test.** *Provisional.* Over a 30-turn simulation, `Σ new crowns` (tax + rewards) must not exceed `Σ economic output at reference prices` (production + processing). If it does, operating costs or maintenance are too small, or tax income is too high. This is a design target; it has not been measured.

---

## 6. Worked example index

| Example | Formula(s) | Expected result |
|---|---|---|
| 1 New nation | F-EC-024/025/026 | Wealth 2,100; 310 units |
| 2 Positive income | F-EC-001/014/015/016/018 | Closing 1,529; net 29 |
| 3 Operating loss | F-EC-014/015/016/024 | Closing 1,247; net −282; wealth +146 |
| 4 Capex vs opex | F-EC-027/031/032 | Book value 250; margin 7; payback 36 |
| 5 Reconciliation | F-EC-017/018/028 | Closing 1,428; identity holds |
| 6 Warehouse limit | F-EC-004/023 | 2 batches; 20 coal; 25 cost |
| 7 Refining | F-EC-008/012 | 16 gasoline; 40 cost |
| 8 Aluminum | F-EC-008/012 | 8 aluminum; 24 cost |
| 9 Steel | F-EC-009/012 | 16 steel; 48 cost; 20 iron + 12 coal |
| 10 Ammunition | F-EC-009/012 | 20 ammunition; 40 cost; 16 lead + 8 coal |
| 11 Food shortage | F-EC-002/003 | 1,200 bp; tax 132; recovery 150 |
| 12 Insufficient inputs | F-EC-006/009/010/011 | Reject F1; accepted order fails F5; releases all; `C=2, M=2 → P=2`, 4 GU, not 8 |
| 13 Overflow | F-EC-011/023 | Batch blocked; nothing destroyed |
| 14 Duplicate settlement | F-EC-033/034 | Second run no-op |
| 15 Insolvency | F-EC-014/018 | Closing 11; obligation cancelled; no debt |
| 16 Market | F-EC-028/029 | 160 transfer; 3 fee; conservation |
| 17 Reroll | F-EC-024/026 | Old assets destroyed; replacement 2,100 |
| 18 Power shortfall | F-EC-006/007/008 | 60%; one batch per chain |
| 19 Hunger recovery | F-EC-003 | 1,200 → 132 → 150 |
| 20 Book vs market | F-EC-024/031 | Wealth −20 on a sale at 5 |

**F-EC-040 — Examples are not a simulation.** *Provisional.* Each example is a hand calculation. It proves that the formulas can be applied consistently; it does **not** prove that the economy is balanced, that a market clears, or that a database implementation matches. Those are Prompt 14/Stage 3 tests.

---

## 7. Change control

**F-EC-041 — Changing a number.** *Provisional.* A number change requires: the old value, the new value, the reason, the affected formulas/examples, a date and a decision ID. The old value is kept in §8. A change that would alter a recipe's input list is not a number change; it is a new B-04 revision.

**F-EC-042 — Changing a formula.** *Provisional.* A formula change requires a new `F-EC-###` ID if the meaning changes; an editorial clarification keeps the ID. The old expression is preserved in §8. No prompt may silently redefine a formula in its own document.

**F-EC-043 — Adding a formula.** *Provisional.* The next free ID is used. The formula must state all fields in §4 and appear in the index. A formula that is only a report label is not added; it is a report definition.

---

## 8. Revision history and validation record

**F-EC-044 — Revision history.** *Provisional.* v1.0 (2026-10-24): first issue. No earlier version exists. The constants are the v1.0 provisional calibration; no value has been tuned or measured. **v1.1 (2026-10-24):** numerical correction pass. The bundle total (310), the F-EC-021/023 examples, the worked-example index and the register's validation record were corrected; two examples in the rulebook were rebuilt. **No constant, formula, recipe or reference price changed.** A same-day micro-correction completed v1.1: the index's Example 5 row was synchronised with the rulebook (**1,426 → 1,428**), this register's header now reads v1.1, and the arithmetic checker compares the two documents. **v1.2 (2026-10-25):** F-EC-006 publishes `planned_batches = M + A ≤ C`; no value changed. **v1.3 (2026-10-28):** F-EC-014 records ECN-147a's whole-obligation allocation and its standard-start worked case; no constant, formula or reference price changed.

**F-EC-045 — Validation record.** *Provisional.*

The register and the rulebook it serves were checked on 2026-10-24 with the repository's document and arithmetic tools, run from `docs/`:

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`**, including the B-04 block and a check that every `F-EC-` cited by the rulebook exists here |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** |
| `python qa_backups/test_next_action.py` | **15 tests — OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 — `ALL CHECKS PASSED`**: recomputes the starting bundle, every base margin in §5, all 20 worked examples and this register's index from §3's constants; compares Example 5 with this register's index row and both headers with their stated revision; and fails on any stale figure |

Every constant in §3 is exercised by the arithmetic script; a disagreement between this register and the rulebook is a defect. **Not run:** no formula has been executed against a database or a scheduler, and no simulation exists.

**F-EC-046 — What is not validated.** *Provisional.* (1) No formula has been executed against a database or a scheduler. (2) The examples are hand calculations, not a simulation. (3) The reference prices are accounting estimates, not observed market prices. (4) No player has played the economy. (5) The balance targets in F-EC-038/039 are unmeasured. (6) The hash function in F-EC-033 is a Stage 5 choice, not a fixed algorithm.

---

## 9. Cross-references

- [B-04 — Economy, resources, treasury and finances](10_economy_resources_treasury_and_finances.md)
- [Research report](research/04_politics_and_war_economy_research.md)
- [Requirements traceability](03_requirements_traceability.md)
- [Stage 2 decision register](04_approved_and_provisional_decisions.md)
- [B-02 turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md)

<!-- END -->
