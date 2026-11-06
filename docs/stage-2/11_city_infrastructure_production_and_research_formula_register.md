# City, infrastructure, production and research — formula and balance register

**Version:** 1.3 · **Created:** 2026-10-25 · **Revised:** 2026-11-04 (v1.3 Prompt 10B-C2 updates **F-CI-019** to the infrastructure-only carrying-value basis: `fixed_assets = Σ_city infrastructure_carrying_value + Σ_other book_value`, with the zero-cost opening lot and no facility impairment. No construction cost, capacity, housing or research coefficient changed. The v1.2 text follows for history: v1.2 corrects F-CI-021's worked example to Example 15B's actual **22/24 → 24, +1 banked** state, keeps the 23/24 case only in its correct Example 20 context, and aligns the demand cross-reference with B-04's `planned_batches = M + A ≤ capacity`. No coefficient changed. v1.1 reconciles the register with the rulebook after independent review: F-CI-005's bound is corrected to **16,170**, F-CI-004 no longer claims a starting-level unit price, F-CI-011 is scoped to facilities and warehouse expansions with **no** infrastructure discount, and F-CI-021 becomes the single research-allocation formula with `rp_pool`, `rp_reserved` and `rp_available`. No other constant changed.) · **Stage 2, Prompt 05**
**Status:** **Draft** — definitive formula definitions; **no formula has been implemented or runtime-tested.**
**Authority:** This register is the **single authoritative source** for the expression, variables, units, bounds, rounding, timing and dependencies of every city, infrastructure, building, research and programme formula in Nation Supremacy. [B-05](11_cities_infrastructure_production_and_research.md) explains these formulas; if the two disagree, this register wins until it is corrected by a new revision.
**Companions:** [B-05](11_cities_infrastructure_production_and_research.md) · [research report](research/05_politics_and_war_city_infrastructure_production_research.md) · [B-04 register](10_economic_formula_and_balance_register.md) · [B-04 rulebook](10_economy_resources_treasury_and_finances.md)

---

## 1. How to use this register

**F-CI-000 — Register rules.** *Provisional.* Every formula has one entry, one ID and one owner. An entry that lacks a field is incomplete. A number that appears in prose but not here is a defect. If a later prompt needs a new formula, it adds an entry with a new ID; it never redefines an existing one. **F-CI-000a — No formula may be duplicated.** If a B-04 formula already computes a quantity (a batch's variable cost, a recipe's output, a reference price), B-05 cites it and does not restate it.

**F-CI-000b — B-04 wins on economic values.** *Provisional.* Where a B-05 formula consumes a B-04 quantity — output per batch, variable cost, maintenance, reference price, power draw — the B-04 value is authoritative and the B-05 formula must be written so that changing the B-04 value changes the result without editing B-05.

**F-CI-000c — All values integer.** *Provisional.* Capacity, housing, crowns, materials, RP, batches and levels are integers. Percentages and discounts are basis points (`10,000 bp = 100%`). Every division states `floor` or `ceil`. No formula uses floating point.

**F-CI-000d — Time is the turn, not the clock.** *Provisional.* `turn_id` identifies a two-hour boundary. A formula's "timing" names a phase (`P3.7`, `P4.1a`…`P4.1d`, `P4.2`) from B-02/B-04. No formula reads wall-clock time.

**F-CI-000e — Constants are provisional.** *Provisional.* Every number in §3 is the v1.0 provisional calibration. Prompt 14 may change a value by a new revision; it may not change a formula's structure without a B-05 revision.

## 2. Numerical conventions

| Convention | Rule |
|---|---|
| Integers | All quantities are whole numbers. A fractional intermediate is floored or ceiled by the stated rule, never rounded to nearest unless stated |
| Basis points | `10,000 bp = 100%`; `1,000 bp = 10%`; a discount of 10% is `1,000 bp` |
| Rounding of discounts | `ceil(base × (10,000 − discount_bp) / 10,000)` — the player never gets a fraction of a crown |
| Capacity | Integer points; a facility's DC is a property of its class, not a stored per-instance value |
| Batches | Integer; a batch is atomic (B-04 ECN-054) |
| Housing | Integer people; a city's housing is derived, never stored |
| RP | Integer points; no fractions, no interest, no conversion |
| Negative values | No formula may produce a negative capacity, housing, cost, refund or balance. A negative input is clamped to 0 before use |
| Zero | A zero capacity, zero institute or zero batch is valid and yields zero, never an error |
| Time | A value becomes effective at the **next** boundary unless the entry says "immediate" |

---

## 3. Constants and calibrated tables

### 3.1 City and infrastructure constants

| Item | Value | Unit | Notes |
|---|---:|---|---|
| Maximum cities per nation | 12 | cities | Hard bound (D-067) |
| Capital starting infrastructure | 50 | levels | Standard start (D-063) |
| New city starting infrastructure | 10 | levels | URB-034 |
| Minimum infrastructure | 10 | levels | A city cannot exist below this |
| Maximum infrastructure | 500 | levels | Per city |
| Infrastructure step | 10 | levels | The natural purchase unit; smaller steps are legal |
| Base capacity | 10 | DC | `capacity = 10 + floor(I/10)` |
| Capacity per 10 infrastructure | 1 | DC | |
| Housing base | 45,000 | people | |
| Housing per infrastructure | 100 | people/level | `45,000 + 100×I` = 50,000 at I=50 |
| Housing per civic centre | 25,000 | people | |
| City cost base | 400 | crowns | `400 + 150×k²` |
| City cost coefficient | 150 | crowns | |
| City steel cost | 20 | steel | Every founding |
| National infrastructure per prior city | 100 | levels | `Σ I ≥ 100 × (k−1)` |
| Construction discount cap | 2,000 | bp | 20% |
| Demolition refund | 2,500 | bp | 25% of crowns paid |

### 3.2 Building capacity costs and limits

| Class | DC per unit | Per-city limit |
|---|---:|---:|
| Extraction facility | 1 | 8 per resource |
| Processing facility | 2 | 4 per chain |
| Generator level | 2 | 6 levels, all classes |
| Warehouse expansion | 1 | 6 |
| Research institute | 3 | 2 |
| Civic centre | 2 | 3 |

### 3.3 Building catalogue

| ID | Name | Class | DC | Crowns | Materials | Prerequisite |
|---|---|---|---:|---:|---|---|
| `bld_farm` | Farm | Extraction (food) | 1 | 120 | 5 steel | — |
| `bld_coal_mine` | Coal mine | Extraction (coal) | 1 | 160 | 5 steel | — |
| `bld_oil_well` | Oil well | Extraction (oil) | 1 | 220 | 5 steel | — |
| `bld_iron_mine` | Iron mine | Extraction (iron) | 1 | 180 | 5 steel | — |
| `bld_bauxite_mine` | Bauxite mine | Extraction (bauxite) | 1 | 220 | 5 steel | — |
| `bld_lead_mine` | Lead mine | Extraction (lead) | 1 | 260 | 5 steel | — |
| `bld_uranium_mine` | Uranium mine | Extraction (uranium) | 1 | 600 | 10 steel, 5 aluminum | `tech_nuclear_engineering` |
| `bld_refinery` | Refinery | Processing (refining) | 2 | 320 | 15 steel | — |
| `bld_steel_mill` | Steel mill | Processing (steel) | 2 | 380 | 15 steel | — |
| `bld_smelter` | Aluminum smelter | Processing (aluminum) | 2 | 420 | 20 steel | `tech_ind_chem` |
| `bld_ammo_plant` | Ammunition plant | Processing (ammunition) | 2 | 360 | 15 steel | `tech_ind_heat` |
| `bld_coal_plant` | Coal plant | Generation | 2 | 280 | 10 steel | — |
| `bld_oil_plant` | Oil plant | Generation | 2 | 340 | 10 steel, 5 aluminum | — |
| `bld_nuclear_plant` | Nuclear plant | Generation | 2 | 1,200 | 30 steel, 20 aluminum | `tech_nuclear_engineering` |
| `bld_warehouse` | Warehouse expansion | Support | 1 | `180 + 40n` | 5 steel | — |
| `bld_lab` | Research institute | Support | 3 | 500 | 20 steel | — |
| `bld_civic` | Civic centre | Support | 2 | 300 | 10 steel | — |

`n` in the warehouse cost is the number of expansions already built nationally, starting at 0. A `bld_warehouse` adds 250 units of national warehouse capacity.

### 3.4 Standard capital grant (D-063)

| Item | Value |
|---|---:|
| Cities | 1 (capital) |
| Infrastructure | 50 |
| Capacity | 15 DC |
| Housing | 50,000 |
| Facilities | 3 farms, 2 coal mines, 1 oil well, 1 iron mine, 1 refinery, 1 coal plant |
| DC used | `3 + 2 + 1 + 1 + 2 + 2 = 11` |
| DC free | 4 |
| Fixed-asset book value | **0** (granted, not purchased) |
| Capacity vector | food 3, coal 2, oil 1, iron 1, refining 1, coal generator 1 |

### 3.5 Research tree

| ID | Branch | RP | Crowns | Prerequisite | Effect |
|---|---|---:|---:|---|---|
| `tech_agri_rotation` | Agriculture | 24 | 160 | — | +1 food per batch |
| `tech_agri_mechanisation` | Agriculture | 44 | 300 | rotation | +1 food per batch |
| `tech_ext_coal` | Extraction | 20 | 140 | — | +1 coal per batch |
| `tech_ext_oil` | Extraction | 32 | 220 | ext_coal | +1 oil per batch |
| `tech_ext_metals` | Extraction | 40 | 280 | ext_coal | +1 iron, +1 bauxite per batch |
| `tech_ext_deep` | Extraction | 56 | 360 | ext_metals | +1 lead, +1 uranium per batch |
| `tech_ind_heat` | Industry | 28 | 200 | — | +1 steel per batch; unlocks ammo plant |
| `tech_ind_chem` | Industry | 48 | 340 | ind_heat | +1 gasoline, +1 aluminum per batch; unlocks smelter |
| `tech_ind_ordnance` | Industry | 36 | 260 | ind_heat | +1 ammunition per batch |
| `tech_civ_survey` | Civil works | 20 | 140 | — | infrastructure cost −10% |
| `tech_civ_methods` | Civil works | 40 | 280 | civ_survey | construction crown cost −10% |
| `tech_nuclear_engineering` | Energy | 60 | 500 | civ_methods, ind_chem | unlocks uranium mine and nuclear plant |
| **Total** | | **448** | **3,180** | | |

### 3.6 National programmes

| ID | Branch | RP | Crowns | Materials | Effect |
|---|---|---:|---:|---|---|
| `prg_granary` | Agriculture | 100 | 900 | 100 steel, 50 aluminum | +500 warehouse; +1 food per batch |
| `prg_survey` | Extraction | 100 | 1,000 | 100 steel, 50 gasoline | extraction variable cost −2 (min 2) |
| `prg_standards` | Industry | 100 | 1,200 | 150 steel, 50 aluminum | processing maintenance −1 (min 1) |
| `prg_civil_works` | Civil works | 100 | 1,100 | 120 steel, 60 aluminum | +2 DC per city |

### 3.7 Upkeep and research

| Item | Value | Unit |
|---|---:|---|
| Research institute upkeep | 2 | crowns/turn |
| Civic centre upkeep | 1 | crown/turn |
| RP per institute per turn | 1 | RP |
| Active research projects per nation | 1 | project |
| Warehouses: national base | 2,000 | units |
| Warehouse per expansion | 250 | units |
| Granary programme warehouse bonus | 500 | units |

---

## 4. The formula register

Each entry states expression, variables, units, range, rounding, timing, dependencies, example, rationale, edge cases, validation and requirements.

### 4.1 City and infrastructure

**F-CI-001 — Development capacity.**

| Field | Definition |
|---|---|
| Expression | `capacity(city) = 10 + floor(infrastructure / 10)` |
| Variables | `infrastructure` (levels, integer 10…500) |
| Units | Output: capacity points (DC) |
| Range | 11 … 60 |
| Rounding | Floor to whole DC |
| Timing | Derived, read at submission and at P4.1 |
| Dependencies | URB-041; D-070 |
| Example | `I=50 → 10 + 5 = 15`; `I=500 → 60` |
| Rationale | One lever, one visible number; each 10 levels adds exactly one DC |
| Edge cases | `I<10` is invalid (a city cannot exist below 10); `I=10 → 11`; a non-multiple of 10 floors |
| Validation | T05-B03 |
| Requirements | REQ-199 |

**F-CI-002 — City housing.**

| Field | Definition |
|---|---|
| Expression | `housing(city) = 45,000 + 100 × infrastructure + 25,000 × civic_centres` |
| Variables | `infrastructure` (10…500); `civic_centres` (0…3) |
| Units | Output: people |
| Range | 46,000 … 170,000 |
| Rounding | None (integer multiplication and addition) |
| Timing | Derived; read by Prompt 06 at the boundary |
| Dependencies | URB-042, URB-060; D-079 |
| Example | Capital at 50 with 0 civic: `45,000 + 5,000 = 50,000` |
| Rationale | Housing is the city's contribution to population, not a second population model |
| Edge cases | A city at 10 houses 46,000; three civic centres at 500 house 170,000; an unfunded civic centre's housing is excluded from **growth** only (URB-120) |
| Validation | T05-B04 |
| Requirements | REQ-200, REQ-256 |

**F-CI-003 — National infrastructure.**

| Field | Definition |
|---|---|
| Expression | `national_infrastructure = Σ_cities infrastructure(city)` |
| Variables | Per-city infrastructure (10…500) |
| Units | Levels |
| Range | 50 … 6,000 (12 × 500) |
| Rounding | None |
| Timing | Read at submission for a founding |
| Dependencies | F-CI-001/002 |
| Example | One capital at 100 → 100 |
| Rationale | The expansion gate is development, not elapsed time |
| Edge cases | A nation with no city is invalid; a city under construction does not count until it exists |
| Validation | T05-A02 |
| Requirements | REQ-192 |

**F-CI-004 — Infrastructure unit cost.**

| Field | Definition |
|---|---|
| Expression | `unit_cost(I) = 8 + floor(I / 10)` |
| Variables | `I` (current infrastructure, 10…500) |
| Units | Crowns per level |
| Range | 9 … 58 |
| Rounding | Floor |
| Timing | Computed at submission from the current level |
| Dependencies | URB-043 |
| Example | `I=50 → 13`; `I=100 → 18`; `I=400 → 48` |
| Rationale | Linear growth keeps the curve legible and avoids the reference game's exponential cliff |
| Edge cases | The unit price is **marginal**: it rises as the level rises, and F-CI-005 sums each level at its own price. A large order therefore costs exactly the same as the same levels bought in several orders; it is never cheaper per level |
| Validation | T05-B01 |
| Requirements | REQ-201 |

**F-CI-005 — Infrastructure order cost.**

| Field | Definition |
|---|---|
| Expression | `infrastructure_cost(I, n) = ceil( ( Σ_{k=0}^{n−1} (8 + floor((I + k) / 10)) ) × (10,000 − discount_bp) / 10,000 )` |
| Variables | `I` (current level, 10…500); `n` (levels bought, 1…490); `discount_bp` (0…2,000) |
| Units | Crowns |
| Range | 9 (one level at 10) … **16,170** (the largest legal order, 10 → 500: 490 levels) before discount; **12,936** after the 2,000 bp cap. 50 → 500 is **15,750** |
| Rounding | Each unit price is floored; the sum is exact; the discount is applied once to the sum and ceiled. With `discount_bp = 0` the result is the exact integer sum |
| Timing | P4.1c; charged as capex |
| Dependencies | F-CI-004; `tech_civ_survey`; URB-044 |
| Example | 50→100: `130 + 140 + 150 + 160 + 170 = 750`; at 1,000 bp: `ceil(750 × 9,000/10,000) = 675`; 50→500: **15,750**; 10→500: **16,170**; 10→500 at the 2,000 bp cap: `ceil(16,170 × 8,000/10,000) = 12,936` |
| Rationale | Summing the unit price as the level rises is D-069's model and the only definition under which splitting an order changes nothing. A single multiplication at the starting price would undercharge a large order and contradict the decision |
| Edge cases | `n = 0` is invalid; an order that would pass 500 is rejected, not clamped; `n` need not be a multiple of 10; the last level bought is `I + n − 1`; ten 10-level orders and one 100-level order cost the same; only Civil Survey discounts this formula at launch, so `discount_bp` is 0 or 1,000 in practice |
| Validation | T05-B01/B02 |
| Requirements | REQ-201, REQ-203 |

**F-CI-006 — City cost.**

| Field | Definition |
|---|---|
| Expression | `city_cost(k) = 400 + 150 × k²`, plus 20 steel |
| Variables | `k` (the number of the city being founded, 2…12) |
| Units | Crowns; steel units |
| Range | 1,000 … 22,000 crowns |
| Rounding | None |
| Timing | P4.1a; charged as capex |
| Dependencies | URB-032/033 |
| Example | `k=2 → 1,000`; `k=3 → 1,750`; `k=12 → 22,000` |
| Rationale | Quadratic growth is a real cost without the reference game's cubic explosion |
| Edge cases | `k=1` is the capital and is never charged; a founding that fails charges nothing; no discount applies |
| Validation | T05-A02/A03 |
| Requirements | REQ-193 |

**F-CI-007 — Founding threshold.**

| Field | Definition |
|---|---|
| Expression | `can_found(k) = (k ≤ 12) ∧ (national_infrastructure ≥ 100 × (k − 1))` |
| Variables | `k` (2…12); `national_infrastructure` (F-CI-003) |
| Units | Boolean |
| Range | True/false |
| Rounding | None |
| Timing | Submission |
| Dependencies | F-CI-003 |
| Example | `k=2` needs 100; a capital at 50 cannot found |
| Rationale | Expansion follows development |
| Edge cases | Exactly 100 passes; 99 fails; the 12th city needs 1,100 |
| Validation | T05-A02 |
| Requirements | REQ-192 |

**F-CI-008 — Used capacity.**

| Field | Definition |
|---|---|
| Expression | `used(city) = Σ_facilities dc(class(facility))` |
| Variables | Facility list; `dc` = 1/2/3 by class (F-CI-009) |
| Units | DC |
| Range | 0 … 60 |
| Rounding | None |
| Timing | Derived; checked at submission and P4.1 |
| Dependencies | URB-048 |
| Example | Standard capital: `7×1 + 1×2 + 1×2 = 11` |
| Rationale | Derived, so it cannot drift from the facility list |
| Edge cases | An empty city uses 0; a demolished facility is removed at the next turn, not immediately |
| Validation | T05-C01 |
| Requirements | REQ-205, REQ-216 |

**F-CI-009 — Capacity cost of a class.**

| Field | Definition |
|---|---|
| Expression | `dc(extraction)=1; dc(processing)=2; dc(generator level)=2; dc(warehouse)=1; dc(lab)=3; dc(civic)=2` |
| Variables | Class |
| Units | DC |
| Timing | At construction |
| Dependencies | URB-048 |
| Example | A refinery costs 2; a farm costs 1 |
| Rationale | Weighted footprints let heavy industry cost more of a city than a mine |
| Edge cases | A generator **level** costs 2; three levels cost 6 |
| Validation | T05-C01 |
| Requirements | REQ-205 |

**F-CI-010 — Free capacity.**

| Field | Definition |
|---|---|
| Expression | `free(city) = capacity(city) − used(city)` |
| Variables | F-CI-001, F-CI-008 |
| Units | DC |
| Range | 0 … 60 |
| Rounding | None |
| Timing | Submission and P4.1 |
| Dependencies | URB-050/051 |
| Example | Standard capital: `15 − 11 = 4` |
| Rationale | The number the player actually spends |
| Edge cases | Negative is impossible by the invariant; if observed it is a defect, not a state |
| Validation | T05-C03 |
| Requirements | REQ-207, REQ-216 |

### 4.2 Construction, capacity and accounting

**F-CI-011 — Construction crown cost.**

| Field | Definition |
|---|---|
| Expression | `cost(b) = ceil(crown_base(b) × (10,000 − discount_bp) / 10,000)` |
| Variables | `crown_base(b)` from §3.3; `discount_bp = 1,000` if `tech_civ_methods` is complete, else 0. **Scope:** `BUILD_FACILITY` and `EXPAND_WAREHOUSE` only. It is **not** applied to `UPGRADE_INFRASTRUCTURE` (F-CI-005 owns that, with Civil Survey), to materials, to `FOUND_CITY` or to programmes |
| Units | Crowns |
| Range | 108 … 1,200 |
| Rounding | Ceil |
| Timing | P4.1c, charged as capex |
| Dependencies | URB-072; §3.3 |
| Example | Refinery `320 → ceil(320×9,000/10,000) = 288` with Civil Methods; `320` without |
| Rationale | One discount, applied once, rounded against the player |
| Edge cases | Materials are never discounted; city founding, programmes and infrastructure are not discounted by this formula; at launch each cost has exactly **one** discount source, so no order can receive both Civil Survey and Civil Methods; a future second construction discount is additive to this one, applied once to the base, and capped at a combined 2,000 bp |
| Validation | T05-D01 |
| Requirements | REQ-217, REQ-224 |

**F-CI-012 — Construction book value.**

| Field | Definition |
|---|---|
| Expression | `book_value(b) = cost(b) + Σ_m (qty_m × reference_price(m))` |
| Variables | `cost(b)` (F-CI-011); material quantities from §3.3; `reference_price` from the B-04 register §3.5 |
| Units | Crowns |
| Range | 143 … 1,570 |
| Rounding | None |
| Timing | P4.1, when the asset resolves |
| Dependencies | B-04 ECN-098/108; D-058 |
| Example | Farm `120 + 5×7 = 155`; with Civil Methods `108 + 35 = 143` |
| Rationale | Materials are capitalised, not expensed, so construction does not destroy wealth |
| Edge cases | A granted starting facility has book value 0; a demolition removes the whole value; there is no depreciation |
| Validation | T05-G01 |
| Requirements | REQ-251 |

**F-CI-013 — Warehouse expansion cost.**

| Field | Definition |
|---|---|
| Expression | `warehouse_cost(n) = 180 + 40 × n` |
| Variables | `n` (expansions already built nationally, 0…71) |
| Units | Crowns, plus 5 steel |
| Range | 180 … 3,020 |
| Rounding | None |
| Timing | P4.1c |
| Dependencies | URB-058; B-04 ECN-122 |
| Example | First expansion `180`; second `220`; sixth `380` |
| Rationale | Rising marginal cost, as B-04 requires; each expansion is worth the same 250 units |
| Edge cases | `n` counts all cities; a demolished warehouse does not reduce `n`, so rebuilding is dearer — deliberate |
| Validation | T05-C05 |
| Requirements | REQ-213 |

**F-CI-014 — National warehouse capacity.**

| Field | Definition |
|---|---|
| Expression | `W = 2,000 + 250 × expansions + 500 × granary` |
| Variables | `expansions` (count, ≥0); `granary` (0/1) |
| Units | Units of storage |
| Range | 2,000 … 20,500 |
| Rounding | None |
| Timing | Next turn after construction |
| Dependencies | B-04 ECN-120/121; URB-058; F-CI-024 |
| Example | One expansion: `2,250`; with Granary: `2,750` |
| Rationale | One shared warehouse, as B-04 fixed; B-05 only adds capacity |
| Edge cases | A demolished warehouse removes its 250 at the next turn; the Granary bonus is once |
| Validation | T05-E06 |
| Requirements | REQ-213 |

**F-CI-015 — Extraction output.**

| Field | Definition |
|---|---|
| Expression | `output(r) = batches_run(r) × (Y_r + yield_bonus(r))` |
| Variables | `batches_run` from B-04 F-EC-004; `Y_r` from B-04 register §3.2; `yield_bonus(r)` = sum of completed technology/programme bonuses |
| Units | Units of resource `r` |
| Range | 0 … `capacity × (Y + 3)` |
| Rounding | None (integer addition and multiplication) |
| Timing | P3.3 |
| Dependencies | B-04 F-EC-004/005; F-CI-023 |
| Example | 4 farms, +2 bonus: `4 × (20 + 2) = 88` |
| Rationale | Research raises the output of a batch that runs; it never makes a blocked batch run |
| Edge cases | A blocked batch yields 0 regardless of bonus; the bonus never applies to purchased or transferred units |
| Validation | T05-E02 |
| Requirements | REQ-228 |

**F-CI-016 — Processing output.**

| Field | Definition |
|---|---|
| Expression | `output(c) = batches_run(c) × (Y_c + yield_bonus(c))` |
| Variables | `batches_run` from B-04 F-EC-008 with derating; `Y_c` from B-04 register §3.3; bonus per chain |
| Units | Units of the manufactured good |
| Range | 0 … `capacity × (Y + 1)` |
| Rounding | None |
| Timing | P3.5 |
| Dependencies | B-04 F-EC-006…012; F-CI-023 |
| Example | 1 refinery, +1: `1 × (8 + 1) = 9` gasoline |
| Rationale | Same rule as extraction; the recipe's input list is unchanged |
| Edge cases | The bonus never changes inputs; a derated-to-zero chain yields 0; one bonus per chain unless the register adds another |
| Validation | T05-E01 |
| Requirements | REQ-228, REQ-234 |

**F-CI-017 — Processing maintenance with the Standards Bureau.**

| Field | Definition |
|---|---|
| Expression | `maintenance(c) = batches × max(1, 2 − standards_bonus)` |
| Variables | `batches` (capacity); `standards_bonus = 1` if `prg_standards`, else 0 |
| Units | Crowns per turn |
| Range | 1 … 2 per batch |
| Rounding | None |
| Timing | P3.2 |
| Dependencies | B-04 ECN-051; URB-107 |
| Example | 4 batches with the Bureau: `4 × 1 = 4` instead of 8 |
| Rationale | A maintenance floor of 1 keeps the programme from making capacity free |
| Edge cases | Extraction maintenance stays 1 and is unaffected; generator maintenance stays 2 |
| Validation | T05-F08 |
| Requirements | REQ-253 |

**F-CI-018 — Demolition refund.**

| Field | Definition |
|---|---|
| Expression | `refund = floor(crown_cost_paid × 2,500 / 10,000)` |
| Variables | `crown_cost_paid` (what the asset actually cost when built; 0 for a granted facility) |
| Units | Crowns |
| Range | 0 … 300 |
| Rounding | Floor |
| Timing | P4.1b |
| Dependencies | URB-071; URB-121 |
| Example | Farm 120 → 30; refinery 320 → 80; granted farm 0 → 0 |
| Rationale | A real but unattractive recovery; cycling is always a loss |
| Edge cases | Materials are never returned; the book value removed is the full value, so the unrecovered part is an impairment; a discounted build refunds 25% of the discounted price |
| Validation | T05-G04 |
| Requirements | REQ-223 |

**F-CI-019 — Fixed-asset book value.**

| Field | Definition |
|---|---|
| Expression | `fixed_assets = Σ_city infrastructure_carrying_value(city) + Σ_other book_value(asset)`, where `infrastructure_carrying_value = infrastructure_gross_capital − infrastructure_accumulated_impairment` (URB-118a) |
| Variables | Per-city infrastructure gross capital and accumulated impairment; every standing facility and warehouse expansion |
| Units | Crowns |
| Range | 0 … unbounded in principle; about 300,000 in a maxed nation |
| Rounding | None |
| Timing | Recomputed after P4.1 capitalisation and after P5 impairment; reported in national wealth at P3.8 from the prior turn's closing value |
| Dependencies | F-CI-012; B-04 ECN-108; URB-118a/118b; B-10 F-WR-038 |
| Example | One refinery 425; plus a farm 155 → 580. Infrastructure: a 50 → 60 upgrade adds one 130-crown lot (carrying 130); a 3-level strike at `I = 60` impairs 6 → carrying 124; a 39-crown repair adds a new lot → carrying 163 |
| Rationale | A derived total, never an editable field |
| Edge cases | Infrastructure counts at **carrying value**, not at level × a unit price; the initial 50 or 10 levels are a zero-cost opening lot and add 0; facility book value is excluded from infrastructure impairment; research and programmes do not count; demolition removes the asset's value |
| Validation | T05-G01 |
| Requirements | REQ-251 |

**F-CI-020 — Research rate.**

| Field | Definition |
|---|---|
| Expression | `rp_per_turn = research_institutes(nation)` |
| Variables | Standing institutes, 0…24 |
| Units | Research points per turn |
| Range | 0 … 24 |
| Rounding | None |
| Timing | P4.2 |
| Dependencies | URB-059, URB-095 |
| Example | 3 institutes → 3 RP |
| Rationale | One point per institute is the simplest legible rate |
| Edge cases | An institute built at P4.1 of turn T does not produce in T; an unpaid institute produces 0 (`LAB_IDLE`) |
| Validation | T05-F01 |
| Requirements | REQ-235, REQ-238 |

**F-CI-021 — Research progress.**

| Field | Definition |
|---|---|
| Expression | `need = max(0, cost_rp − progress)`; `rp_applied = min(rp_per_turn, need)`; `progress += rp_applied`; `rp_pool += rp_per_turn − rp_applied`; `rp_available = rp_pool − rp_reserved`. With no active project `need = 0` and the whole generation banks |
| Variables | `cost_rp` (total project cost); `progress` (0…cost_rp); `rp_per_turn` (F-CI-020); `rp_pool` (banked points); `rp_reserved` (points reserved by accepted `COMMISSION_PROGRAMME` actions, 0…`rp_pool`); `rp_available` |
| Units | Research points |
| Range | 0 … `cost_rp` |
| Rounding | None |
| Timing | P4.2 |
| Dependencies | F-CI-020 |
| Example | **22/24, 3 RP** → applied 2, progress 24, pool +1 (Example 15B); 23/24 with 1 RP → applied 1, pool 0 (Example 20); 100 banked reserved for a programme → pool 0, then 5 RP on a 10/44 project → progress 15 (Example 15C) |
| Rationale | One assignment per point: the project and the pool are **disjoint accounts**, and a programme reads only the pool, so progress is never a currency that another system can spend |
| Edge cases | No project → need 0, all banks; completion → the surplus banks and progress is **not** converted back into points; a programme reservation lowers `rp_available` but not `rp_pool` until P4.1d; cancellation or failure releases it; a programme never subtracts from `progress`; a point may never appear in both `progress` and `rp_pool`; P4.1d precedes P4.2, so a programme cannot be funded by the same settlement's generation |
| Validation | T05-F03 |
| Requirements | REQ-238 |

**F-CI-022 — Research completion.**

| Field | Definition |
|---|---|
| Expression | `complete = progress ≥ cost_rp` |
| Variables | F-CI-021 |
| Units | Boolean |
| Timing | P4.2; effect next turn |
| Dependencies | URB-096, URB-099 |
| Example | 24 ≥ 24 → complete at turn 41, active turn 42 |
| Rationale | One condition, no hidden roll |
| Edge cases | A project exactly at cost completes; a completed project cannot be restarted; a retained duplicate completion is a defect |
| Validation | T05-F04 |
| Requirements | REQ-239, REQ-241 |

### 4.3 Modifiers, programmes and totals

**F-CI-023 — Modifier total and cap.**

| Field | Definition |
|---|---|
| Expression | `yield_bonus(r) = min(cap(r), Σ_sources bonus(source, r))` |
| Variables | Sources = completed technologies and programmes; `cap(r)` = 3 for food, 1 for every other raw, 1 per manufactured good |
| Units | Units per batch |
| Range | 0 … cap |
| Rounding | None |
| Timing | Read at production; the sum is computed from completed sources |
| Dependencies | URB-100; §3.5/§3.6 |
| Example | Food `1 + 1 + 1 = 3`; a fourth source would be rejected at design time |
| Rationale | Integer additions avoid rounding and compounding; the cap is checked in the design, not silently at runtime |
| Edge cases | A source that is not completed does not count; a programme counts once; no percentage multiplier exists |
| Validation | T05-F05, T05-F07 |
| Requirements | REQ-242 |

**F-CI-024 — Programme availability.**

| Field | Definition |
|---|---|
| Expression | `available(p) = branch_complete(branch(p)) ∧ ¬held(p) ∧ rp_available ≥ rp_required(p)` |
| Variables | Programme `p`; branch completion from URB-103; `rp_available = rp_pool − rp_reserved` (F-CI-021); `rp_required(p)` from §3.6 |
| Units | Boolean |
| Timing | Submission |
| Dependencies | URB-107/108 |
| Example | Granary available after both Agriculture technologies |
| Rationale | The branch is the gate; there is no project-slot currency |
| Edge cases | A programme held once cannot be held again; a reroll removes it; insufficient **banked** RP rejects at submission (`F5`) and creates no reservation, even if the active project has points in progress; the reservation is taken at acceptance and consumed at P4.1d |
| Validation | T05-F08 |
| Requirements | REQ-246, REQ-247 |

**F-CI-025 — Upkeep.**

| Field | Definition |
|---|---|
| Expression | `upkeep = 2 × labs + 1 × civic_centres` |
| Variables | Standing labs and civic centres |
| Units | Crowns per turn |
| Range | 0 … 84 |
| Rounding | None |
| Timing | P3.7 |
| Dependencies | URB-120 |
| Example | 2 labs + 3 civic → `4 + 3 = 7` |
| Rationale | Only the two support buildings whose output is a flow have upkeep |
| Edge cases | Unpaid → `LAB_IDLE` / `CIVIC_UNFUNDED`; never negative; never debt |
| Validation | T05-G03 |
| Requirements | REQ-253 |

**F-CI-026 — National wealth with fixed assets.**

| Field | Definition |
|---|---|
| Expression | `national_wealth = treasury + Σ(inventory_units × reference_price) + fixed_assets` |
| Variables | B-04 ECN-108; F-CI-019 |
| Units | Crowns |
| Range | ≥ 0 |
| Rounding | None |
| Timing | P3.8 / report |
| Dependencies | B-04 ECN-108 |
| Example | `1,209 + 35 + 425 = 1,669` after a refinery |
| Rationale | Construction converts liquid to fixed value; research and programmes reduce wealth |
| Edge cases | A demolition's impairment lowers wealth; research spending lowers wealth; no double count |
| Validation | T05-G05 |
| Requirements | REQ-255 |

### 4.4 Limits and availability

**F-CI-027 — Per-city limit check.**

| Field | Definition |
|---|---|
| Expression | `allowed = count(class, city) + 1 ≤ limit(class)` |
| Variables | `count` of the facility class in that city; `limit` from §3.2 |
| Units | Boolean |
| Timing | Submission and P4.1 |
| Dependencies | URB-049 |
| Example | A 9th farm in one city is rejected (limit 8) |
| Rationale | Limits create specialisation without a percentage bonus |
| Edge cases | Generator levels share one limit of 6; a demolished facility frees its slot next turn |
| Validation | T05-C04 |
| Requirements | REQ-206 |

**F-CI-028 — Construction slot availability.**

| Field | Definition |
|---|---|
| Expression | `slot_free(city, turn) = ¬∃ accepted construction action for (city, turn)` |
| Variables | Accepted actions of the construction class |
| Units | Boolean |
| Timing | Submission |
| Dependencies | URB-064 |
| Example | Second refinery order in the same city/turn is rejected |
| Rationale | One build per city per boundary is the pacing device |
| Edge cases | A cancelled action frees the slot; a failed resolution does not free it for that turn (the turn is over) |
| Validation | T05-D02 |
| Requirements | REQ-218 |

**F-CI-029 — Capacity check at resolution.**

| Field | Definition |
|---|---|
| Expression | `valid = used(city) + dc(order) ≤ capacity(city)` |
| Variables | F-CI-001/008/009 |
| Units | Boolean |
| Timing | P4.1c, against the frozen state |
| Dependencies | URB-050 |
| Example | 19 used + 2 DC > 20 → fails `F5` |
| Rationale | Defence in depth; normally unreachable because of the slot and the no-reduction rule |
| Edge cases | Equality passes; a negative DC is invalid input, not a free build |
| Validation | T05-D05 |
| Requirements | REQ-207, REQ-216 |

**F-CI-030 — City-count check.**

| Field | Definition |
|---|---|
| Expression | `allowed = cities < 12` |
| Variables | Current city count |
| Units | Boolean |
| Timing | Submission |
| Dependencies | URB-031 |
| Example | A 12-city nation cannot found a 13th |
| Rationale | A hard operational and design bound |
| Edge cases | A founding in flight counts only when it resolves; two foundings in one turn are prevented by the slot |
| Validation | T05-A04 |
| Requirements | REQ-191 |

---

## 5. Reference cost and margin table

**F-CI-031 — Cost per DC and base margin.** *Provisional.* At the reference prices (B-04 register §3.5) and without research, each facility has the following standing economics. `Margin` is the batch's contribution at the reference price **before** power; `per DC` divides the margin by the facility's capacity cost. The table is a design check, not a promise: a player sells at market prices, not reference prices.

| Facility | DC | Crowns | Crowns/DC | Base margin/batch | Margin/DC |
|---|---:|---:|---:|---:|---:|
| Farm | 1 | 120 | 120 | **+7** | +7.0 |
| Coal mine | 1 | 160 | 160 | **−1** | −1.0 |
| Oil well | 1 | 220 | 220 | **+1** | +1.0 |
| Iron mine | 1 | 180 | 180 | **−1** | −1.0 |
| Bauxite mine | 1 | 220 | 220 | **+1** | +1.0 |
| Lead mine | 1 | 260 | 260 | **+1** | +1.0 |
| Uranium mine | 1 | 600 | 600 | **+1** | +1.0 |
| Refinery | 2 | 320 | 160 | **+6** | +3.0 |
| Steel mill | 2 | 380 | 190 | **+14** | +7.0 |
| Aluminum smelter | 2 | 420 | 210 | **+14** | +7.0 |
| Ammunition plant | 2 | 360 | 180 | **+10** | +5.0 |
| Coal plant | 2 | 280 | 140 | — (6 GU) | — |
| Oil plant | 2 | 340 | 170 | — (6 GU) | — |
| Nuclear plant | 2 | 1,200 | 600 | — (20 GU) | — |
| Research institute | 3 | 500 | 167 | — (1 RP) | — |
| Civic centre | 2 | 300 | 150 | — (25,000 housing) | — |
| Warehouse (+250) | 1 | 180 | 180 | — (250 units) | — |

**F-CI-032 — What the table says, and what it does not.** *Provisional.* Three observations are deliberate. (1) **Coal and iron lose one crown per batch at the reference price.** They are inputs, not cash crops; a nation mines them because steel needs them, not to sell them. (2) **Steel and aluminum have the best margin per DC (7.0),** tied with food, because they are the industrial payoff for the power and input chains they require. (3) **The refinery is the weakest processing margin per DC (3.0)** because its value is the gasoline it unlocks and the construction demand for it, not the spread. The table does **not** say which strategy wins: it ignores power, maintenance, capital, trade prices and the demand ceiling. Prompt 14 must run the simulation (URB-133).

**F-CI-033 — The known provisional skew.** *Provisional.* Steel's 7.0 margin/DC with a 190-crown capital cost is the strongest simple build in the table, and a nation that only builds steel mills would be rich in the model and poor in practice: it needs iron and coal mines (negative margin), power, and a buyer. The balance depends on the demand for steel (construction, war) and on the market price. This is recorded now so that Prompt 14 tests it rather than discovering it: **if steel dominates after simulation, the answer is a demand-side change (construction or warfare consumption), not a silent nerf to the recipe**, because the recipe is B-04's (D-046).

**F-CI-034 — Research payback.** *Provisional.* A technology's payback is `crowns / (bonus per batch × batches affected × margin per unit)`, ignoring RP. For `tech_agri_rotation` (160 crowns, +1 food/batch) with four farms at a reference food price of 1: `160 / (1 × 4 × 1) = 40` turns of production — but the bonus also persists and applies to every future farm. With eight farms it is 20 turns. For `tech_ind_heat` (200 crowns, +1 steel/batch) with two steel mills at a margin of 7 per extra unit: `200 / (1 × 2 × 7) ≈ 14` turns. Research is deliberately **slower to pay back than a building** on a small scale and **faster on a large one**; that is the intended trade (URB-131).

---

## 6. Worked example index

| Example | Formula(s) | Expected result |
|---|---|---|
| 1 Standard capital | F-CI-001/002/008 | 15 DC, 11 used, 4 free; housing 50,000; book 0 |
| 2 Second city | F-CI-003/006/007 | 1,000 crowns + 20 steel; 11 DC; housing 46,000 |
| 3 Infrastructure 50→100 | F-CI-004/005 | 750 crowns (675 with Civil Survey); 20 DC; housing 55,000 |
| 4 Capacity before/after | F-CI-001/010 | free 4 → 9 |
| 5 Build a farm | F-CI-011/012 | 120 + 5 steel; book 155; food capacity 4 |
| 6 Food output | F-CI-015 | 80 food; cost 52; closing 150 |
| 7 Coal output | F-CI-015/017 | 30 coal; margin −3; closing 84 |
| 8 Facility does not fit | F-CI-008/009/010/011; B-04 ECN-137 | 19+2 rejected; 19+1 accepted; total 1,000 crowns/20 steel, available 880/15, then 880/15 after resolution |
| 9 Refining | F-CI-016, B-04 F-EC-008 | 8 gasoline; base margin 6; loaded 0 |
| 10 Steel | F-CI-016, B-04 F-EC-007 | 8 steel; margin 14; loaded 5 |
| 11 Aluminum + power cliff | F-CI-016, B-04 F-EC-007 | 66% → 0 batches; then 12 GU → 8 aluminum |
| 12 Ammunition | F-CI-016 | 10 (11 with tech); margin 10 (loaded 4); treasury 1,000 → 978 |
| 13 Insufficient input/money | F-CI-011, B-04 ECN-068 | rejected / no consumption |
| 14 Cancel, retry, duplicate | F-CI-028/029, B-04 ECN-141 | released; same result; one build |
| 15 Research | F-CI-020/021/022 | 24 turns with 1 lab; 12 with 2; B: 3 RP at 22/24 → 2 progress + 1 pool; C: 100 banked funds a programme while progress 10→15 |
| 16 Modifier once | F-CI-023 | 4 × 23 = 92, not 26.6 × 4 |
| 17 Demolition | F-CI-018 | refund 30; impairment 125; grant refunds 0 |
| 18 Power shortfall | B-04 F-EC-007; F-CI-016 | 75%; 3 of 4 batches |
| 19 Construction reconciliation | F-CI-012/026 | 1,529 → 1,209; wealth 1,669 unchanged |
| 20 Research duplicate | F-CI-022, B-04 ECN-155 | one completion; effect next turn |

---

## 7. Change control

**F-CI-035 — Changing a constant.** *Provisional.* A constant in §3 may be changed only by a new revision of this register, with the reason, the affected examples, the affected requirements and the validation re-run. Prompt 14 may propose a change; this register records it.

**F-CI-036 — Changing a formula.** *Provisional.* A formula's structure — its variables, its rounding, its class costs, its caps — may be changed only by a new B-05 revision with a recorded decision. A change that makes an existing worked example wrong must update the example, the index and the checker in the same revision.

**F-CI-037 — Adding a formula.** *Provisional.* A new formula gets the next free `F-CI-` ID. Existing IDs are never reused, renumbered or deleted; a withdrawn formula is marked `Withdrawn` with the revision that withdrew it.

**F-CI-038 — B-04 precedence.** *Provisional.* If a B-05 formula and a B-04 formula compute the same quantity, the B-04 formula is authoritative and the B-05 entry is corrected. The two registers must agree on every shared quantity; `verify_city_numbers.py` checks the shared constants it can read.

---

## 8. Revision history and validation record

**F-CI-039 — Revision history.** *Provisional.* v1.0 (2026-10-25): first issue. No earlier version exists. Every constant is the v1.0 provisional calibration; nothing has been tuned or measured. v1.1 (2026-10-25): reconciliation with the rulebook after independent review — F-CI-004's edge case no longer claims a fixed starting-level price, F-CI-005's upper bound is 16,170 (the earlier figure was a flat maximum that no legal order could reach) with the 12,936 capped case, F-CI-011 is scoped to facilities and warehouse expansions only, and F-CI-021 becomes the single assignment formula with `rp_pool`, `rp_reserved` and `rp_available`. No coefficient changed. v1.2 (2026-10-25): F-CI-021's example corrected to Example 15B's **22/24, 3 RP → applied 2, pool +1**; the 23/24 case remains only as Example 20. No coefficient changed.

**F-CI-040 — Validation record.** *Provisional.*

Run from `docs/` on 2026-10-25, after the last edit to this register:

| Command | Actual result |
|---|---|
| `python qa_backups/verify_city_numbers.py` | **267/267 arithmetic checks passed** — every constant and all 20 examples, plus the v1.2 guards for the stepped bound, basis-point vocabulary, reservation balances, F-CI-021's Example 15B state, the `M + A ≤ C` capacity cases and cross-document agreement |
| `python qa_backups/verify_economy_numbers.py` | **146/146 checks passed** — the shared B-04 constants are unchanged |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`** |
| `python qa_backups/09_validate.py` | **338/338 checks passed** |

The count is read from the run, not asserted here: a later revision that adds checks prints a larger number and is not a failure.

**F-CI-041 — What is not validated.** *Provisional.* (1) No formula has been executed against a database, a scheduler or a game. (2) The examples are hand calculations, not a simulation. (3) The cost and margin tables are accounting estimates at reference prices, not observed market outcomes. (4) No player has built a city. (5) The balance questions in URB-133 are unanswered. (6) The 64 test specifications are unexecuted.

---

## 9. Cross-references

- [B-05 — Cities, infrastructure, production and research](11_cities_infrastructure_production_and_research.md)
- [Research report](research/05_politics_and_war_city_infrastructure_production_research.md)
- [B-04 rulebook](10_economy_resources_treasury_and_finances.md) · [B-04 register](10_economic_formula_and_balance_register.md)
- [Requirements traceability](03_requirements_traceability.md)
- [Stage 2 decision register](04_approved_and_provisional_decisions.md)
- [B-02 turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md)

<!-- END -->

