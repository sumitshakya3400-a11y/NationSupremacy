# Population and domestic politics — formula and balance register

**Version:** 2.5 · **Created:** 2026-10-25 · **Stage 2, Prompt 06A/06B** · **Revised:** 2026-11-04 (v2.5 Prompt 10B-C2 updates **F-PD-011** to read `housing_population(T)` from B-05 `URB-046` and B-10 `WAR-109m`, and adds the infrastructure-damage edge case: the reduced housing is read at the next P3.8 and repair is not retroactive into the settled turn. No growth, crowding, approval or legitimacy coefficient changed. The v2.4 text follows for history: v2.4 follows the fourth 06B micro-correction: **F-PD-028** and **F-PD-029** publish the submission window as `turn_id < resolution_turn`, `< T` only when the campaign opened on time, so a delayed campaign is not closed at its anchor before its own deadline; the campaign's four offsets, the restoration rule and every constant are unchanged. No formula value changed. v2.3 follows the third 06B micro-correction: **F-PD-028** anchors registration (`+12`), the final notice (`+22`) and the deadline (`+24`) on `campaign_open_turn`, and **F-PD-039** publishes the restoration to `ELECTORAL` before the deadline and the no-gap rule between consecutive blockers. v2.2 followed the second 06B micro-correction: **F-PD-028** now publishes `window_deadline = campaign_open_turn + 24` and `resolution_turn = the first eligible turn ≥ max(scheduled_contest_turn, window_deadline)`, so an interrupted campaign is never restarted (1000/976/1010 → 1010, not 1034); **F-PD-039** keeps `SUCCESSION` non-blocking for a scheduled contest. v2.1 was the 2026-10-28 reconciliation pass: F-PD-027, F-PD-028 and F-PD-039 now publish the anchored-and-caught-up schedule (`scheduled_contest_turn + 240 × k`), the once-only window opened at the first eligible turn, and the resolving-state eligibility (`NORMAL` **and** `ELECTORAL`, never `NORMAL`-only), matching B-06 v2.1's DMP-177/DMP-178/DMP-181/DMP-181a/DMP-181b. No other formula, constant, range or example changed. v2.0 adds Prompt 06B: 19 formulas F-PD-026…F-PD-044 for the political stability penalty, election schedule and window, campaign cost and bonus, election score and vote, challengers, result and tie-break, confidence, control margin, pressure, state durations, postponement, early exit, immunity, first contest, idempotency and audit; adds the §3.8 constants and §3.9 turnout weights; adds `political_stability_penalty_bp` to F-PD-017 and the P4.4 row to §10. No Part I formula changes meaning. v1.2 enforces the 1,000 population floor in F-PD-002 after every path and replaces the three tax terms whose `floor` rounding exceeded their published ranges with the signed `(300 − tax_bp) // divisor` form; no coefficient changed. v1.1 corrected the Range cells and the §3.7 constants)
**Status:** **Draft — the Prompt 06 design is documented and reconciled, and nothing in it is implemented.** The register defines **F-PD-001…F-PD-044**: the 25 Part I formulas and all 19 Part II formulas (F-PD-026…F-PD-044 — the stability penalty, election schedule and window, campaign cost and bonus, election score and vote, challengers, result and tie-break, confidence, control margin, pressure, state durations, postponement and eligibility, early exit, immunity, first contest, idempotency and the audit record). The main specification, this register and the worked examples were reconciled on **2026-10-28** (election-state and window policy, schedule anchoring and catch-up, the rejected-crisis arithmetic, and the removal of a duplicate decision-ID block in B-06); `qa_backups/verify_politics_numbers.py` recomputes every published number and now also models the schedule and guards the documents. **No formula has been implemented, migrated or runtime-tested**; passing documentation checks is not evidence that game code works. The constants remain provisional and **balance is not approved** — Prompt 14 must simulate the governments, the schedule and the crisis before launch.
**Authority:** This register is the **single authoritative source** for the expression, variables, units, bounds, rounding, timing and dependencies of every population, approval, stability, legitimacy, constituency, government-modifier and policy formula in Nation Supremacy. [B-06](12_population_and_domestic_politics.md) explains them; if the two disagree, this register wins until it is corrected by a new revision.
**Companions:** [B-06](12_population_and_domestic_politics.md) · [research report](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md) · [B-04 register](10_economic_formula_and_balance_register.md) · [B-05 register](11_city_infrastructure_production_and_research_formula_register.md)

---

## 1. How to use this register

**F-PD-000 — Register rules.** *Provisional.* Every formula has one entry, one ID and one owner. An entry that lacks a field is incomplete. A number that appears in prose but not here is a defect. A later prompt adds an entry with a new ID; it never redefines an existing one.

**F-PD-000a — Upstream values are cited, not restated.** Where a formula consumes a quantity another document owns — `hunger_penalty_bp`, `tax_income`, housing, capacity, `food_demand` — the owning document's value is authoritative and the formula is written so that changing it changes the result without editing this register.

**F-PD-000b — All values integer.** Population, support, approval, crowns and research points are whole numbers. Percentages and rates are basis points (`10,000 bp = 100%`). Every division states `floor` or `ceil`. No formula uses floating point.

**F-PD-000c — Time is the turn.** `turn_id` identifies a two-hour UTC boundary. A formula's timing names a settlement phase (P3.1…P3.8, P4.3) from B-04/B-06. No formula reads wall-clock time and no formula uses a random number.

**F-PD-000d — No formula twice.** Support, approval, stability and legitimacy each have exactly one computing formula. A policy, a government or an event changes an **input**, never a result. If two formulas would compute the same value, one of them is deleted, not reconciled.

**F-PD-000e — Constants are provisional.** Every number in §3 is the v1.0 provisional calibration. Prompt 14 may change a value by a new revision; it may not change a formula's structure without a B-06 revision.

## 2. Numerical conventions

| Convention | Rule |
|---|---|
| Integers | Every quantity is a whole number; a fractional intermediate is floored or ceiled by the stated rule |
| Basis points | `10,000 bp = 100%`; `1,000 bp = 10%`; `250 bp = 2.5%` |
| Rounding | `floor` unless the entry says `ceil`; service cost uses `ceil` on the government modifier only |
| Growth | Integer basis points, clamped −100…+100 before application |
| Population | Integer people, minimum **1,000**; never negative; never fractional |
| Approval | Integer 0…100 |
| Stability | Integer bp, 5,000…`stability_cap_bp` (never above 11,000) |
| Legitimacy | Integer 0…100, **derived** on read, never stored |
| Support | Integer 0…100 per group |
| Weights | Six fixed constants summing to **100** |
| Zero | A zero capacity, zero institute or zero service share yields zero, never an error |
| Ordering | Each formula states its phase; a formula may read only values stored before its phase |

---

## 3. Constants and calibrated tables

### 3.1 Population and housing constants

| Item | Value | Unit | Notes |
|---|---:|---|---|
| Starting population | 50,000 | people | D-063 / DMP-113 |
| Minimum population | 1,000 | people | DMP-120 invariant |
| Base growth rate | 50 | bp/turn | 0.5% |
| Growth clamp | −100…+100 | bp | At most 1% loss per turn from these terms |
| Approval reference | 55 | points | The neutral approval |
| Growth per approval | `floor((approval − 55)/2)` | bp | ±1 bp per 2 approval points |
| Headroom term cap | +15 | bp | Proportional term, capped |
| Hunger divisor | 30 | — | `−floor(hunger_bp/30)` |
| Crowding divisor | 100 | — | `−floor(crowding_bp/100)` |
| Crowding decline | `ceil(excess/10)` | people | 10% of the excess per turn |
| Housing base | 45,000 | people/city | B-05 URB-042 |
| Housing per infrastructure level | 100 | people | B-05 |
| Housing per funded civic centre | 25,000 | people | B-05 |
| Food demand divisor | 1,000 | — | B-04 ECN-080 |
| Hunger cap | 3,000 | bp | B-04 ECN-084 |

### 3.2 Political constants

| Item | Value | Unit | Notes |
|---|---:|---|---|
| Approval bounds | 0…100 | points | DMP-045 |
| Approval movement cap | 5 | points/turn | DMP-047 |
| Stability reference | 10,000 | bp | 100% at approval 55, BALANCED, no hunger, no crowding |
| Stability movement cap | 250 | bp/turn | DMP-054 |
| Stability floor | 5,000 | bp | DMP-053 |
| Stability hard ceiling | 11,000 | bp | B-04 ECN-094 |
| Support base | 48 | points | DMP-064 |
| Support bounds | 0…100 | points | DMP-064 |
| Policy cooldown | 12 | turns | DMP-102, per axis |
| Service share settings | 0 / 2,000 / 5,000 | bp | DMP-095 |
| Tax rate settings | 200 / 300 / 400 | bp | DMP-095 |

### 3.3 Fixed constituency weights

| ID | Group | Weight | Structural role |
|---|---|---:|---|
| `con_labour` | Labour | **30** | Wages, services, housing, food |
| `con_rural` | Rural producers | **15** | Food capacity share, services, stability |
| `con_industry` | Industry | **20** | Processing share, warehouse headroom, stability |
| `con_commerce` | Commerce | **15** | Warehouse headroom, tax, civil order |
| `con_scholars` | Scholars | **10** | Institutes, services, civil liberties |
| `con_security` | Security institutions | **10** | Public order, services, food, stability |

The weights are constants (DMP-063). They are used **once**, in F-PD-015, and once more by any 06B formula that 06B registers. They do not vary with population, employment, cities, production or policy.

### 3.4 Government channels

| `government_id` | `approval_weight_bp` | `stability_shift_bp` | `stability_cap_bp` | `service_cost_mod_bp` | `research_adjustment` |
|---|---:|---:|---:|---:|---:|
| `gov_democracy` | 32 | −100 | 11,000 | 0 | 0 |
| `gov_constitutional_monarchy` | 22 | +200 | 10,900 | 0 | 0 |
| `gov_absolute_monarchy` | 14 | +400 | 10,800 | 0 | 0 |
| `gov_dictatorship` | 16 | 0 | 10,600 | −1,000 | 0 |
| `gov_military_junta` | 10 | +250 | 10,600 | +500 | −1 |
| `gov_technocracy` | 24 | −150 | 10,900 | 0 | +1 |

Each row is applied once per channel (F-PD-025). No government has a tax multiplier, a production bonus or a construction discount.

### 3.5 Institutional weight vectors (legitimacy)

| Government | Labour | Rural | Industry | Commerce | Scholars | Security | Sum |
|---|---:|---:|---:|---:|---:|---:|---:|
| Democracy | 30 | 15 | 20 | 15 | 10 | 10 | 100 |
| Constitutional monarchy | 10 | 20 | 15 | 15 | 20 | 20 | 100 |
| Absolute monarchy | 20 | 20 | 10 | 5 | 5 | 40 | 100 |
| Dictatorship | 5 | 10 | 20 | 10 | 0 | 55 | 100 |
| Military junta | 0 | 0 | 0 | 0 | 0 | 100 | 100 |
| Technocracy | 5 | 0 | 15 | 5 | 65 | 10 | 100 |

### 3.6 Policy tables

**Order (`POL-ORDER`).**

| Setting | `order_stability_bp` | Labour | Rural | Industry | Commerce | Scholars | Security |
|---|---:|---:|---:|---:|---:|---:|---:|
| `OPEN` | −200 | +6 | −4 | +2 | +8 | +10 | −15 |
| `BALANCED` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `FIRM` | +300 | −6 | +4 | −2 | −8 | −10 | +15 |

**Fiscal (`POL-FISCAL`).**

| Setting | `tax_bp` | `service_share_bp` | Net at the standard start |
|---|---:|---:|---:|
| `LOW` | 200 | 0 | 100 |
| `STANDARD` | 300 | 2,000 | 120 |
| `HIGH` | 400 | 5,000 | 100 |

### 3.7 Support-term constants

| Input | Formula use | Divisor | Cap |
|---|---|---:|---|
| `service_share_bp` | labour, scholars | 400 | +12 each |
| `service_share_bp` | rural | 1,000 | +5 |
| `service_share_bp` | security | 2,000 | +2 |
| `300 − tax_bp` | labour / rural / industry / commerce / scholars | 40 / 20 / 15 / 12 / 50 | −3…+2 / ±5 / −7…+6 / −9…+8 / ±2 (at 200/300/400) |
| `hunger_bp` | labour / rural / security | 100 / 150 / 200 | −30 / −20 / −15 |
| `food_share_bp` | rural | 250 | 0…+40 |
| `processing_share_bp` | industry | 250 | 0…+40 |
| `warehouse_bp` | industry, commerce | 1,000, −5 | −5…+5 |
| `stability_bp − 10,000` | rural / industry / commerce / security | 500 / 400 / 400 / 400 | −10…+2 / −13…+2 / −13…+2 / −13…+2 |
| `institutes_active` | scholars | 3 per institute | +12 |
| `housing_bp` | labour | 500, −18 | −18…+2 |

### 3.8 Election, retention and crisis constants (Prompt 06B)

| Item | Value | Unit | Notes |
|---|---:|---|---|
| Election term | **240** | turns | DMP-177; 480 h = 20 days |
| Campaign window | **24** | turns | opens `campaign_open_turn` (`T − 24` when on time) |
| Registration close | **12** | turns before `T` | ballot fixed |
| Final notice | **2** | turns before `T` | digest projection |
| Incumbency allowance | **200** | bp | DMP-198 |
| Challenger floor | **4,000** | bp | below it, no challenger stands |
| Campaign points | **6** | points | platform allocation |
| Platform cap per group | **2** | points | DMP-190 |
| Campaign bonus cap | **6** | points per group | DMP-192 |
| Rally cost | **2 × unit** | crowns | `unit = ceil(population/1,000)` |
| Advertisement cost | **3 × unit** | crowns | up to two |
| Confidence threshold | **4,500** | bp | DMP-201 |
| Auto-confidence | **70** | legitimacy | motion not tabled |
| Warning band | **5** | legitimacy points | DMP-217 |
| Pressure window | **12** | turns | DMP-218 |
| Transition duration | **12** | turns | 24 h |
| Crisis duration | **18** | turns | 36 h |
| Recovery duration | **12** | turns | 24 h |
| Early crisis exit | **6** | turns | earliest |
| Challenge immunity | **24** | turns | after recovery |
| Stability penalty — transition | **800** | bp | F-PD-026 |
| Stability penalty — crisis | **1,500** | bp | F-PD-026 |
| Stability penalty — recovery | **400** | bp | F-PD-026 |

**Control thresholds and institutional response:**

| Government | Threshold | Response at 12 pressure turns |
|---|---:|---|
| `gov_constitutional_monarchy` | 45 | early confidence motion; failure → `TRANSITION` |
| `gov_absolute_monarchy` | 40 | `CRISIS` |
| `gov_dictatorship` | 35 | `CRISIS` |
| `gov_military_junta` | 40 | `CRISIS` |
| `gov_technocracy` | 42 | `TRANSITION` |

### 3.9 Election turnout weights

| Group | Population weight | Turnout factor | Election weight (bp) |
|---|---:|---:|---:|
| Labour | 30 | 9 | **2,443** |
| Rural | 15 | 13 | **1,765** |
| Industry | 20 | 11 | **1,991** |
| Commerce | 15 | 10 | **1,357** |
| Scholars | 10 | 15 | **1,358** |
| Security | 10 | 12 | **1,086** |
| **Total** | **100** | — | **10,000** |

The weights are constants and sum to exactly 10,000. They are **not** the approval weights and must not be substituted for them in F-PD-015.

---

## 4. Population formulas

**F-PD-001 — Population growth rate.**

| Field | Definition |
|---|---|
| Expression | `growth_bp = clamp(50 + floor((approval − 55)/2) + min(15, floor(headroom × 100 / population)) − floor(hunger_bp/30) − floor(crowding_bp/100), −100, 100)` |
| Variables | `approval` 0…100 (opening value); `headroom = max(0, housing_growth − population)`; `hunger_bp` 0…3,000 (B-04, this turn); `crowding_bp` 0…10,000 (F-PD-003) |
| Units | Output: basis points of the opening population per turn |
| Range | −100…+100 bp |
| Rounding | Each term floored separately; the sum is then clamped |
| Timing | P3.8, step 5 |
| Dependencies | F-PD-011 (housing), F-PD-003 (crowding), B-04 ECN-084 (hunger) |
| Stacks with | Nothing. No event, policy, government or technology adds a growth term (DMP-029) |
| Example | Standard start: `50 + 0 + 0 − 0 − 0 = 50`; with 5,000 headroom: `50 + 0 + 10 = 60` |
| Rationale | Four legible inputs, a hard clamp and no randomness |
| Edge cases | `population = 0` cannot occur (minimum 1,000); `hunger_bp` above 3,000 is clamped by B-04 before it arrives; a negative `headroom` is clamped to 0 so crowding is not counted twice |

**F-PD-002 — Population application (cap and decline).**

| Field | Definition |
|---|---|
| Expression | `natural = population + floor(population × growth_bp / 10,000)`; if `population > housing_growth`: `raw = population − max(ceil((population − housing_growth)/10), max(0, population − natural))`; else `raw = min(natural, housing_growth)`; **`new_population = max(1,000, raw)`** |
| Variables | `population` ≥ 1,000; `natural` ≥ 0; `raw` = the unclamped result; `housing_growth` from F-PD-011 |
| Units | People |
| Range | **1,000** … `max(population, housing_growth)`; when population is above housing the upper bound is the opening population, because a crowding decline never increases it |
| Rounding | Growth `floor`; the crowding decline `ceil` |
| Timing | P3.8, after F-PD-001 |
| Dependencies | F-PD-001, F-PD-011 |
| Stacks with | Nothing |
| Example | `population 50,000`, `growth_bp 60` → `natural 50,300`; housing 55,000 → **50,300**. Housing 50,200 → **50,200** (the 50 excess is discarded). **Floor:** population 1,000, approval 0, housing 45,000, hunger 3,000 → `growth_bp = 50 + floor(−55/2) + 15 − 100 = −63`; `natural = 1,000 + floor(1,000 × −63/10,000) = 993`; `raw = min(993, 45,000) = 993`; `new_population = max(1,000, 993) =` **1,000** (seven people would have been lost; the floor applies) |
| Rationale | Housing is a hard cap on growth (DMP-030) and crowding is a gradual decline (DMP-031) |
| Edge cases | `natural < population` → decline, never a cap; a crowding decline always wins over growth; the floor is applied **after** the growth rounding and the crowding decline, so no path can return below 1,000; at the floor a further negative rate keeps the population at 1,000 rather than creating a debt of people; the floor never creates food, income or a growth bonus |

**F-PD-003 — Crowding.**

| Field | Definition |
|---|---|
| Expression | `crowding_bp = 0` if `population ≤ housing_growth`, else `min(10,000, floor((population − housing_growth) × 10,000 / population))` |
| Variables | `population`; `housing_growth` (F-PD-011) |
| Units | Basis points |
| Range | 0…10,000 |
| Rounding | `floor` |
| Timing | P3.8; the value is used by F-PD-001, F-PD-017 and F-PD-006/007/008/009 |
| Dependencies | F-PD-011 |
| Stacks with | Nothing; crowding enters growth once and the stability target once |
| Example | Population 60,000, housing 50,000 → `floor(10,000 × 10,000/60,000) = 1,666` |
| Rationale | One derived integer instead of a second population model |
| Edge cases | No housing at all is impossible (base 45,000 per city); a population exactly at housing is not crowded |

**F-PD-010 — Food demand interface.**

| Field | Definition |
|---|---|
| Expression | `food_demand = ceil(population / 1,000)` — **owned by B-04 (ECN-080)**; this entry is the interface, not a second formula |
| Variables | `population` (this register) |
| Units | Food units per turn |
| Range | 1 … unbounded |
| Rounding | `ceil` |
| Timing | P3.6, using the population stored at the end of the previous turn |
| Dependencies | B-04 ECN-080; B-06 supplies `population` |
| Stacks with | Nothing |
| Example | 50,000 people → **50 units**; 60,000 → 60 |
| Rationale | One owner for consumption (DMP-035) |
| Edge cases | B-06 may not change the divisor, the rounding or the consumption order |

**F-PD-011 — Housing used for growth.**

| Field | Definition |
|---|---|
| Expression | `housing_growth = Σ_cities (45,000 + 100 × infrastructure + 25,000 × funded_civic_centres)` |
| Variables | `infrastructure` per city (B-05), read at `housing_population(T)` (B-05 `URB-046`, B-10 `WAR-109m`); `funded_civic_centres` counts only centres whose upkeep was paid at P3.7 |
| Units | People |
| Range | 45,000 per city … 95,000+ per city |
| Rounding | None (integer sum) |
| Timing | P3.8, after P3.7's obligation results |
| Dependencies | B-05 URB-042, URB-120, URB-046; B-10 WAR-109f/WAR-109m |
| Stacks with | B-05 only; B-06 adds no housing source |
| Example | Three cities at 50/50/50 infrastructure and one funded centre: `150,000 + 15,000 + 25,000 = 190,000`. A city at 50 struck down to 40 and read at the next P3.8: `45,000 + 4,000 = 49,000`, so a population of 50,000 has a 1,000 excess and DMP-031/F-PD-003 applies |
| Rationale | An unfunded civic centre does not house (DMP-038), without evicting anyone; warfare damage lowers housing the same way, with no casualty rule (DMP-031a) |
| Edge cases | A city cannot exist below 10 infrastructure (B-05); all centres unfunded → base housing only; a P4.1 repair of turn T is read at the next P3.8 and is not retroactive into T |

## 5. Constituency formulas

All six use the base 48 and are clamped to 0…100. They read the **opening** `stability_bp` (DMP-114 step 2), so the step is acyclic.

**F-PD-004 — Labour.**

| Field | Definition |
|---|---|
| Expression | `48 + floor(service_share_bp/400) + (300 − tax_bp) // 40 + (floor(housing_bp/500) − 18) − floor(hunger_bp/100) + order_labour` |
| Range | 0…100; terms 0…+12 / **−3…+2 at 200/300/400** / −18…+2 / −30 / ±6 |
| Timing | P3.8 step 2 |
| Example | Standard start: `48 + 5 − 0 + 2 − 0 + 0 = 55` |
| Edge cases | `SERVICES_UNFUNDED` sets `service_share_bp = 0` for the whole settlement (DMP-039) |

**F-PD-005 — Rural producers.**

| Field | Definition |
|---|---|
| Expression | `48 + floor(food_share_bp/250) + floor(service_share_bp/1,000) + (300 − tax_bp) // 20 − floor(hunger_bp/150) + floor((stability_bp − 10,000)/500) + order_rural` |
| Range | 0…100; terms 0…+40 / 0…+5 / −5…+5 / −20 / −10…+2 / ±4 |
| Timing | P3.8 step 2 |
| Example | Standard start: `48 + 15 + 2 − 0 − 0 + 0 + 0 = 65` |

**F-PD-006 — Industry.**

| Field | Definition |
|---|---|
| Expression | `48 + floor(processing_share_bp/250) + (300 − tax_bp) // 15 + (floor(warehouse_bp/1,000) − 5) + floor((stability_bp − 10,000)/400) + order_industry` |
| Range | 0…100; terms 0…+40 / **−7…+6 at 200/300/400** / −5…+5 / −13…+2 / ±2 |
| Timing | P3.8 step 2 |
| Example | Standard start: `48 + 5 − 0 + 3 + 0 + 0 = 56` |

**F-PD-007 — Commerce.**

| Field | Definition |
|---|---|
| Expression | `48 + (floor(warehouse_bp/1,000) − 5) + (300 − tax_bp) // 12 + floor((stability_bp − 10,000)/400) + order_commerce` |
| Range | 0…100; terms −5…+5 / **−9…+8 at 200/300/400** / −13…+2 / ±8 |
| Timing | P3.8 step 2 |
| Example | Standard start: `48 + 3 − 0 + 0 + 0 = 51` |

**F-PD-008 — Scholars.**

| Field | Definition |
|---|---|
| Expression | `48 + min(12, 3 × institutes_active) + floor(service_share_bp/400) + (300 − tax_bp) // 50 + order_scholars` |
| Range | 0…100; terms 0…+12 / 0…+12 / ±2 / ±10 |
| Timing | P3.8 step 2 |
| Example | Standard start: `48 + 0 + 5 − 0 + 0 = 53`; three institutes: `48 + 9 + 5 = 62` |

**F-PD-009 — Security institutions.**

| Field | Definition |
|---|---|
| Expression | `48 + floor(service_share_bp/2,000) − floor(hunger_bp/200) + floor((stability_bp − 10,000)/400) + order_security` |
| Range | 0…100; terms 0…+2 / −15 / −13…+2 / ±15 |
| Timing | P3.8 step 2 |
| Example | Standard start: `48 + 1 − 0 + 0 + 0 = 49` |
## 6. Derived political inputs

**F-PD-012 — Housing sufficiency.**

| Field | Definition |
|---|---|
| Expression | `housing_bp = min(10,000, floor(housing_growth × 10,000 / population))` |
| Units | Basis points |
| Range | 0…10,000 |
| Rounding | `floor` |
| Timing | P3.8; consumed once by F-PD-004 |
| Dependencies | F-PD-011 |
| Example | 50,000 people in 50,000 housing → `10,000` (labour term `20 − 18 = +2`); 50,000 in 25,000 housing → `5,000` (`+10 − 18 = −8`) |
| Rationale | Expresses sufficiency as one integer instead of a second housing meter |
| Edge cases | `population` cannot be 0; `housing_bp` is 0 only if housing is 0, which cannot happen | 

**F-PD-013 — Capacity composition shares.**

| Field | Definition |
|---|---|
| Expression | `food_share_bp = floor(food_capacity × 10,000 / production_capacity)`; `processing_share_bp = floor(processing_capacity × 10,000 / production_capacity)`; both **0** if `production_capacity = 0` |
| Variables | `production_capacity` = extraction + processing capacity only (B-05); generators, warehouses, institutes and civic centres are excluded |
| Units | Basis points |
| Range | 0…10,000 each |
| Rounding | `floor` |
| Timing | P3.8, from the capacities in force this turn |
| Dependencies | B-05 capacity |
| Example | 3 food + 5 other extraction + 1 processing = 9: `food_share = 3,333`, `processing = 1,111` |
| Rationale | Rural and industry support depend on **what the nation produces**, not on how much housing it has |
| Edge cases | A nation with generators but no extraction or processing has `production_capacity = 0` → both shares 0, so neither group is rewarded for power plants |

**F-PD-014 — Warehouse headroom.**

| Field | Definition |
|---|---|
| Expression | `warehouse_bp = floor(free_warehouse × 10,000 / warehouse_total)`, or **10,000** if `warehouse_total = 0` |
| Variables | `free_warehouse`, `warehouse_total` (B-04, from B-05 capacity) |
| Units | Basis points |
| Range | 0…10,000 |
| Rounding | `floor` |
| Timing | P3.8, after P3.5's production |
| Dependencies | B-04 storage |
| Example | 1,200 free of 4,000 → `3,000` (industry and commerce term `3 − 5 = −2`) |
| Rationale | A full warehouse is a real economic constraint and a visible political grievance |
| Edge cases | No warehouse at all → 10,000, which credits rather than punishes a nation that has not built one; B-04's 2,000-unit emergency store does not count as a warehouse |

## 7. Approval, stability and legitimacy

**F-PD-015 — Approval target.**

| Field | Definition |
|---|---|
| Expression | `approval_target = clamp(floor((support_labour×30 + support_rural×15 + support_industry×20 + support_commerce×15 + support_scholars×10 + support_security×10) / 100), 0, 100)` |
| Variables | The six supports from F-PD-004…F-PD-009; the weights from §3.3 |
| Units | Approval points 0…100 |
| Range | 0…100 |
| Rounding | `floor` of the weighted mean |
| Timing | P3.8 step 3, after the supports |
| Dependencies | F-PD-004…F-PD-009 |
| Stacks with | Nothing; there is no event, policy or government approval offset |
| Example | Standard start: `(55×30 + 65×15 + 56×20 + 51×15 + 53×10 + 49×10)/100 = 5,530/100 = 55` |
| Rationale | Approval is the population-weighted mean of the groups and nothing else (DMP-046) |
| Edge cases | Because the weights sum to 100, the result can never exceed the highest support or fall below the lowest; a support of 100 in every group gives exactly 100 |

**F-PD-016 — Approval movement.**

| Field | Definition |
|---|---|
| Expression | `approval_next = clamp(approval + clamp(approval_target − approval, −5, +5), 0, 100)` |
| Variables | `approval` (opening); `approval_target` (F-PD-015) |
| Units | Points |
| Range | 0…100; `|Δ| ≤ 5` |
| Rounding | None |
| Timing | P3.8 step 3 |
| Dependencies | F-PD-015 |
| Example | 55 → target 54 → **54**; 48 → target 55 → **53** (capped), then 55 |
| Rationale | The cap makes a shock legible and prevents a one-turn policy flip from harvesting a swing (DMP-047) |
| Edge cases | A target equal to the current value writes no `APPROVAL_CHANGED` event; the cap applies in both directions |

**F-PD-017 — Stability target.**

| Field | Definition |
|---|---|
| Expression | `stability_target_bp = clamp(10,000 + (approval − 55) × approval_weight_bp + stability_shift_bp + order_stability_bp − floor(hunger_bp/2) − floor(crowding_bp/10) − political_stability_penalty_bp, 5,000, stability_cap_bp)` |
| Variables | `approval` (the value computed in step 3, not the opening value); the government's three channels (§3.4); `order_stability_bp` (§3.6); `hunger_bp`; `crowding_bp`; `political_stability_penalty_bp` (F-PD-026, 0 in `NORMAL`/`ELECTORAL`/`SUCCESSION`) |
| Units | Basis points |
| Range | 5,000…`stability_cap_bp` ≤ 11,000 |
| Rounding | Each subtraction floored; the clamp applied last |
| Timing | P3.8 step 4 |
| Dependencies | F-PD-016, F-PD-003, government table, policy table |
| Stacks with | Nothing; each government channel appears exactly once, and the 06B penalty is a separate single term |
| Example | Constitutional monarchy at approval 55: `10,000 + 0 + 200 + 0 − 0 − 0 − 0 = 10,200`; in a crisis the same state with a 1,500 bp penalty targets 8,700 |
| Rationale | The only political variable that reaches the economy, and it reaches it through one identity |
| Edge cases | A target below 5,000 is clamped, so a hated government is inefficient rather than dead; a junta under `FIRM` gains 300 bp once, not per turn |

**F-PD-018 — Stability movement.**

| Field | Definition |
|---|---|
| Expression | `stability_next = stability_bp + clamp(stability_target_bp − stability_bp, −250, +250)` |
| Units | Basis points |
| Range | 5,000…`stability_cap_bp`; `|Δ| ≤ 250` |
| Rounding | None |
| Timing | P3.8 step 4 |
| Dependencies | F-PD-017 |
| Example | 10,000 → target 10,200 → **10,200**; 10,000 → target 8,500 → **9,750** |
| Rationale | Stability is a capacitor: a famine or a new government takes several turns to be felt (DMP-054) |
| Edge cases | The movement cap and the target clamp are different bounds; both apply |

**F-PD-019 — Legitimacy (derived).**

| Field | Definition |
|---|---|
| Expression | `legitimacy = clamp(floor((support_labour×v_labour + support_rural×v_rural + support_industry×v_industry + support_commerce×v_commerce + support_scholars×v_scholars + support_security×v_security) / 100), 0, 100)` |
| Variables | The six supports; the government's vector from §3.5 |
| Units | Points 0…100 |
| Range | 0…100 |
| Rounding | `floor` |
| Timing | Computed on read; never stored (DMP-058) |
| Dependencies | F-PD-004…F-PD-009, §3.5 |
| Example | Constitutional monarchy at the standard start: `(55×10 + 65×20 + 56×15 + 51×15 + 53×20 + 49×20)/100 = 54.95 → 54` |
| Rationale | The groups that can remove the government are not the same as the population (DMP-059) |
| Edge cases | A democracy's vector equals the approval weights, so its legitimacy equals its approval by construction; a junta's equals security support exactly |
| Consequence | **None in B-06.** Prompt 06B attaches the consequence (DMP-060) |

## 8. Policy formulas

**F-PD-020 — Public-service cost.**

| Field | Definition |
|---|---|
| Expression | `service_cost_base = floor(tax_income × service_share_bp / 10,000)`; `service_cost = ceil(service_cost_base × (10,000 + service_cost_mod_bp) / 10,000)` |
| Variables | `tax_income` (B-04 P3.1); `service_share_bp` from the fiscal setting in force; `service_cost_mod_bp` from §3.4 |
| Units | Crowns |
| Range | 0 … `ceil(tax_income × 5,250 / 10,000)` (the 5,000 bp maximum share with the +500 bp maximum modifier) |
| Rounding | `floor` on the base, `ceil` after the modifier |
| Timing | P3.7, as a discretionary obligation |
| Dependencies | B-04 P3.1, §3.4, §3.6 |
| Stacks with | Nothing; the modifier is applied once |
| Example | Tax 200, `HIGH`: base `100`, modifier 0 → **100**. Junta at tax 159: base 31, `ceil(31 × 1.05) = 33` |
| Rationale | A share of tax income ties the state's size to its revenue without a per-capita charge |
| Edge cases | If the unreserved treasury cannot pay it, the obligation is cancelled, nothing is charged, `SERVICES_UNFUNDED` is set and the effective share is 0 (DMP-039); the cost is at most 52.5% of tax income, so it cannot create a negative balance by itself |

**F-PD-021 — Research points per turn.**

| Field | Definition |
|---|---|
| Expression | `rp_per_turn = 0` if `institutes_active = 0`, else `max(0, institutes_active + research_adjustment)` |
| Variables | `institutes_active` (B-05: institutes that produced research this turn); `research_adjustment` (§3.4) |
| Units | Research points per turn |
| Range | 0 … `institutes_active + 1` |
| Rounding | None (integer) |
| Timing | P3.5/P4, whichever B-05 uses for research generation — the value is read there, not recomputed |
| Dependencies | B-05 F-CI-020 |
| Stacks with | Nothing; no technology or programme adds to this integer |
| Example | One institute: technocracy **2**, others **1**, junta **0**. Three institutes: **4 / 3 / 2** |
| Rationale | An integer adjustment is visible at one institute; a percentage would round to zero (DMP-089) |
| Edge cases | Zero institutes gives every government 0, including the technocracy |

**F-PD-022 — Order effects.**

| Field | Definition |
|---|---|
| Expression | Lookup of §3.6 by `policy_order`: one `order_stability_bp` and six `order_*` support terms |
| Units | bp (stability), points (support) |
| Range | −200…+300 bp; ±15 points |
| Rounding | None |
| Timing | Read at P3.8 by F-PD-004…F-PD-009 and F-PD-017 |
| Dependencies | DMP-094 |
| Stacks with | Additive with every other support term; applied once |
| Example | `OPEN`: `−200` bp, scholars `+10`, security `−15` |
| Rationale | One table, six support terms and one stability term; no hidden setting |
| Edge cases | A government that forbids a setting never has it in force (F-PD-024) |

**F-PD-023 — Fiscal settings.**

| Field | Definition |
|---|---|
| Expression | Lookup of §3.6 by `policy_fiscal`: `tax_bp` ∈ {200, 300, 400} and `service_share_bp` ∈ {0, 2,000, 5,000} |
| Units | bp |
| Range | As listed |
| Rounding | None |
| Timing | Read at P3.1 (tax), P3.7 (service) and P3.8 (support) |
| Dependencies | B-04 ECN-081 (`tax_rate_bp`), F-PD-020 |
| Stacks with | Nothing; one setting per axis |
| Example | `HIGH` = 400 bp tax with a 5,000 bp service share |
| Rationale | Tax and spending are coupled so the state has a size, not two independent dials |
| Edge cases | Intermediate rates (for example 250 bp) are rejected; the tax rate is never read from anywhere else |

**F-PD-024 — Policy legality, cooldown and timing.**

| Field | Definition |
|---|---|
| Expression | Legal if the setting exists for the axis **and** §3.4/§3.6 permits it for `government_id`; a change is allowed if `turn_id − policy_<axis>_changed_turn ≥ 12`; on resolution: `policy_<axis> = setting`, `policy_<axis>_changed_turn = turn_id` |
| Variables | `turn_id`; `policy_fiscal_changed_turn`; `policy_order_changed_turn`; `government_id` |
| Units | Turns |
| Range | Cooldown 0…12 remaining |
| Rounding | None |
| Timing | Validation while the turn is `OPEN`; resolution at **P4.3**; the new setting is used from turn **T+1** |
| Dependencies | DMP-090, DMP-101, DMP-102 |
| Stacks with | Nothing; one pending change per axis |
| Example | Change resolved on turn T blocks the same axis until T+12; the other axis is independent |
| Rationale | The cooldown is the entire limit — there is no crown cost (DMP-103) |
| Edge cases | An illegal or locked request is rejected **before** any cooldown is set; a rejected request does not start one; a junta may not leave `FIRM` because `FIRM` is its only legal setting |

**F-PD-025 — Government channels.**

| Field | Definition |
|---|---|
| Expression | Lookup of §3.4 by `government_id`: five values, each consumed by exactly one formula — `approval_weight_bp` and `stability_shift_bp` and `stability_cap_bp` by F-PD-017, `service_cost_mod_bp` by F-PD-020, `research_adjustment` by F-PD-021 |
| Units | bp per approval point; bp; bp; bp; whole RP |
| Range | 10…32; −150…+400; 10,600…11,000; −1,000…+500; −1…+1 |
| Rounding | None |
| Timing | Read at P3.7 (service) and P3.8 (stability) |
| Dependencies | DMP-086, DMP-087 |
| Stacks with | Each channel once; no channel is multiplicative with another |
| Example | Technocracy: `24`, `−150`, `10,900`, `0`, `+1` |
| Rationale | Five channels are the whole mechanical identity of a government |
| Edge cases | `government_id` is immutable, so the row never changes for a living nation (DMP-076) |

---

## 9. Stacking and anti-double-count rules

| Rule | Statement | Enforcement |
|---|---|---|
| **S-1** | Each government channel is applied exactly once, in the formula named in F-PD-025 | F-PD-017, F-PD-020, F-PD-021 |
| **S-2** | A policy changes inputs (`tax_bp`, `service_share_bp`, `order_*`) and never a result | F-PD-022, F-PD-023; approval has no policy term |
| **S-3** | A support term appears in exactly one group's formula | §5 table |
| **S-4** | `hunger_bp` enters growth once, labour once, rural once, security once, the stability target once | F-PD-001/004/005/009/017 |
| **S-5** | `crowding_bp` enters growth once and the stability target once | F-PD-001, F-PD-017 |
| **S-6** | `stability_bp` enters B-04's tax once, through `stability_factor_bp` | B-04 ECN-094 |
| **S-7** | Approval is not a direct modifier on anything but stability and growth | F-PD-001, F-PD-017 |
| **S-8** | Legitimacy has no consequence in B-06 | DMP-060 |
| **S-9** | No political event creates a crown, a resource or a person outside the formulas | DMP-121 invariant 10 |

## 10. Settlement order (P3.8)

| Step | Action | Formula | Reads |
|---:|---|---|---|
| 0 | (Part II) P4.4 of the **previous** turn set `political_stability_penalty_bp` | F-PD-026 | the state active at the start of P3.8 |
| 1 | Read the frozen opening state and P3 results | — | opening `approval`, `stability_bp`, `population`; this turn's `hunger_bp`, funded services, funded centres, capacities, warehouse |
| 2 | Six supports | F-PD-004…F-PD-009 | opening `stability_bp` |
| 3 | Approval target and movement | F-PD-015, F-PD-016 | the new supports |
| 4 | Stability target and movement | F-PD-017, F-PD-018 | the **new** approval |
| 5 | Growth rate and application | F-PD-001, F-PD-002, F-PD-003, F-PD-011 | the new approval |
| 6 | Write values, `politics_settled_turn`, events | — | — |

The order is acyclic: supports read the opening stability, the stability target reads the new approval, and growth reads the new approval but the opening food and housing results. A resumed settlement that finds `politics_settled_turn = turn_id` writes nothing (DMP-115).

## 11. Verification map

| Formula | Verified by | Check |
|---|---|---|
| F-PD-001/002 | B-06 Examples 2, 3, 4, 18 | `growth_bp`, cap, decline |
| F-PD-003/011/012 | Examples 1, 18 | crowding 1,666; decline 1,000 |
| F-PD-004…009 | Examples 1, 5, 8, 17 | supports per policy state |
| F-PD-015/016 | Examples 1, 6, 7, 9 | targets 55/41/54; capped movement |
| F-PD-017/018 | Examples 1, 10, 13 | targets 10,200 / 10,060 / 10,600 / 9,850 |
| F-PD-019 | Examples 1, 13 | 54 and 53 |
| F-PD-020 | Examples 5, 10, 12, 16 | 30 / 100 / 33 |
| F-PD-021 | Example 11 | 0/1/2 and 2/3/4 |
| F-PD-022/023 | Examples 5, 14, 17 | policy states |
| F-PD-024 | Examples 12, 14 | T+1 effect, T+12 cooldown |
| F-PD-025 | Examples 10, 13, 16 | five channels |
| Weights | Example 9 | sum 100; weighted mean 55 |
| F-PD-026 | E39–E40 | penalty 800 / 1,500 / 400; tax path |
| F-PD-027/028 | E19–E21, E47, E49 | anchor 377; window 976/988/998 |
| F-PD-029/030 | E22–E25 | 100 / 150; cap 6 |
| F-PD-031/032 | E26–E29 | 5,749 / 4,249 / 4,882 / 4,966 |
| F-PD-033/034 | E26–E30 | 4,600 / 4,300; tie rule |
| F-PD-035 | E31–E33 | 5,495 / 4,220 |
| F-PD-036/037 | E36–E38 | margin 4; pressure 12 |
| F-PD-038/040/041 | E34, E37, E45 | 12 / 18 / 6; immunity 24 |
| F-PD-042/043/044 | E46–E48 | first contest 340; one record |

`qa_backups/verify_politics_numbers.py` re-computes every row above from the formulas and fails on any drift. It is a document checker, not a runtime test.

## 12. Reserved for Prompt 06B

**Closed by Prompt 06B (2026-10-25).** Every item below is now answered by F-PD-026…F-PD-044 and B-06 §§24–38. The table is retained as history; it is no longer a list of open work.

| Reserved | What 06B must define |
|---|---|
| Election interval | The brief's proposed 240 turns is not adopted |
| Turnout, vote share, seat or executive selection | Inputs: approval, six supports, weights, population, `stability_bp` |
| Candidate registration and campaigns | Costs, actions, limits |
| Consequence of losing an election | The brief's 24-turn proposal is not adopted |
| Non-electoral retention test | Inputs: `legitimacy`, `stability_bp`, government vector, time in office |
| Crisis and unrest | Severity inputs: `hunger_bp`, `crowding_bp`, approval, legitimacy |
| Crisis penalties | The brief's 75% production cut and zero-tax period are not adopted |
| Recovery and leadership-state transitions | The vocabulary is fixed (DMP-128); the transitions are 06B's |
| Election and crisis worked examples | At least the same numerical discipline as §22 of B-06 |

A 06B formula that needs a new input must name its owner and amend B-06's DMP-065 table. It may not add a second approval, stability or legitimacy formula.

## 13. Prompt 06B formulas (F-PD-026…F-PD-044)

These formulas extend the register; they do not redefine F-PD-001…F-PD-025. Every one has a single owner (B-06 Part II), a published expression and a worked example in B-06 §35.

**F-PD-026 — Political stability penalty by state.**

| Field | Definition |
|---|---|
| Expression | `political_stability_penalty_bp = 0` if state ∈ {`NORMAL`, `ELECTORAL`, `SUCCESSION`}; `800` if `TRANSITION`; `1,500` if `CRISIS`; `400` if `RECOVERY` |
| Variables | `leadership_state` (DMP-128) |
| Units | Basis points |
| Range | 0…1,500 |
| Rounding | None |
| Timing | Read by F-PD-017 at P3.8; set at P4.4 |
| Dependencies | DMP-235, DMP-242 |
| Example | A crisis turn targets `10,000 − 1,500 = 8,500` (E39) |
| Rationale | The single route from politics to the economy; no second multiplier |
| Edge cases | The value is read from the state **at the start** of P3.8, so a state change at P4.4 applies from the next turn |

**F-PD-027 — Election schedule.**

| Field | Definition |
|---|---|
| Expression | `next_contest_turn = creation_turn + 240` at creation; after a contest, `next_contest_turn = scheduled_contest_turn + 240 × k`, where `k = ceil((resolved_contest_turn + 25 − scheduled_contest_turn) / 240)`, `k ≥ 1` |
| Variables | `creation_turn`, `scheduled_contest_turn`, `resolved_contest_turn` |
| Units | World-turn ID |
| Range | ≥ 240; every anchor is `creation_turn + 240 × n`, `n ≥ 1` |
| Rounding | `ceil` on `k`; no other rounding |
| Timing | Creation; P4.4 after resolution |
| Dependencies | DMP-177, DMP-181, DMP-181a |
| Example | Created turn 137 → 377; resolved 377 → next 617; resolved 700 → next 857 (E20; DMP-181a table) |
| Rationale | A per-nation anchor spreads load and never drifts; the multiplier skips cycles that were wholly missed instead of stacking overdue elections |
| Edge cases | A postponed contest keeps its original anchor; `resolved_contest_turn` never anchors the next contest; `k = 1` for every postponement an active nation can produce (B-02's 24-turn bound); the next anchor is always ≥ 25 turns after the resolution |

**F-PD-028 — Campaign window.**

| Field | Definition |
|---|---|
| Expression | `campaign_open_turn = the first eligible turn ≥ scheduled_contest_turn − 24`; `registration_close_turn = campaign_open_turn + 12`; `final_notice_turn = campaign_open_turn + 22`; `window_deadline = campaign_open_turn + 24`; `resolution_turn = the first eligible turn ≥ max(scheduled_contest_turn, window_deadline)`; campaign legal while `leadership_state = ELECTORAL` and `turn_id < resolution_turn`. For an on-time contest this is the published `T − 24 / T − 12 / T − 2` and resolution at `T`. **One window per contest**: it is never opened twice, never moved backwards, and never opened with deadlines already behind the nation (DMP-181b) |
| Variables | `scheduled_contest_turn`, `turn_id`, `leadership_state`, eligibility |
| Units | World-turn IDs |
| Range | 24 turns from open to deadline; resolution at the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)` |
| Rounding | None |
| Timing | P4.4 at open; validation on every campaign submission |
| Dependencies | F-PD-027, F-PD-039 |
| Example | `T = 1000`: 976 / 988 / 998 / close at 1000 (E21) |
| Rationale | 48 hours is one meaningful window, not a season; a postponed contest still gets its full window, just later |
| Edge cases | A request arriving as the resolution turn opens is rejected (`CAMPAIGN_CLOSED`); `ELECTORAL` is set only while the window is open; **the opening is computed once** — a blocking state that begins after the window opens never moves `campaign_open_turn`, never restarts the 24 turns and never resolves before `scheduled_contest_turn` (1000/976 blocked to 1010 resolves 1010, not 1034); a nation ineligible at `T − 24` is the other case and opens a new window at its first eligible turn |

**F-PD-029 — Campaign action cost.**

| Field | Definition |
|---|---|
| Expression | `unit = ceil(population / 1,000)`; rally cost `2 × unit`; advertisement cost `3 × unit`; platform cost `0` |
| Variables | `population` |
| Units | Crowns |
| Range | Rally ≥ 2; advertisement ≥ 3 |
| Rounding | `ceil` on the unit; exact multiplication after |
| Timing | Submission while the window is open (`ELECTORAL`) and `turn_id < resolution_turn`; for an on-time contest that is `< T` |
| Dependencies | B-04 `available_crowns`, ledger |
| Example | 50,000 → rally 100, advert 150 (E23–E24) |
| Rationale | Scales with the nation, so a mature treasury cannot buy a small nation's election |
| Edge cases | A rejected action charges nothing; a retry with the same key charges once |

**F-PD-030 — Campaign bonus.**

| Field | Definition |
|---|---|
| Expression | `campaign_bonus_i = min(6, platform_i + rally_i + advertise_i)`; platform: 6 points, max 2 per group, at least 3 groups; rally: +3 Labour, +2 Rural; each advert: +2 Commerce, +2 Industry, +1 Scholars |
| Variables | The submitted action rows |
| Units | Election points (added to a 0…100 support) |
| Range | 0…6 per group |
| Rounding | None |
| Timing | Read at P4.4 of the contest turn |
| Dependencies | F-PD-029, DMP-189…DMP-192 |
| Example | 2 Labour + rally = 5 (E25) |
| Rationale | Bounded, ephemeral and never a stored support |
| Edge cases | Excess points are clipped, not converted; a second contest starts from zero |

**F-PD-031 — Election score per group.**

| Field | Definition |
|---|---|
| Expression | `election_score_i = clamp(support_i + campaign_bonus_i, 0, 100)` |
| Variables | Six supports (P3.8), six bonuses |
| Units | Points |
| Range | 0…100 |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | F-PD-004…F-PD-009, F-PD-030 |
| Example | Support 40 + 2 = 42 (E22) |
| Rationale | A campaign moves the score, never the support |
| Edge cases | The clamp is after the addition; 97 + 6 = 100 |

**F-PD-032 — Incumbent vote.**

| Field | Definition |
|---|---|
| Expression | `vote_bp = min(10,000, floor(Σ (election_weight_i × election_score_i) / 100) + 200)` |
| Variables | §3.9 weights; six scores |
| Units | Basis points |
| Range | 0…10,000 |
| Rounding | `floor` of the weighted total, then +200 |
| Timing | P4.4 |
| Dependencies | F-PD-031, §3.9 |
| Example | Standard start 5,749 (E26) |
| Rationale | Turnout differs from population weight; the vote is not a second approval |
| Edge cases | The 10,000 cap binds only at every group 100; the +200 is added after the floor |

**F-PD-033 — Challenger scores.**

| Field | Definition |
|---|---|
| Expression | `popular_front_bp = clamp(4,400 + (60 − approval) × 40, 3,600, 6,400)`; `institutional_bp = clamp(4,300 + (55 − legitimacy) × 30, 3,600, 6,400)` |
| Variables | `approval`, `legitimacy` (computed from the six supports and the government vector) |
| Units | Basis points |
| Range | 3,600…6,400 |
| Rounding | None (all integers) |
| Timing | P4.4, using the P3.8 state |
| Dependencies | F-PD-015, F-PD-019 |
| Example | Approval 55 → 4,600; legitimacy 55 → 4,300 (E26) |
| Rationale | The contest is a referendum on the record, not a second random event |
| Edge cases | A challenger below 4,000 does not stand; a vacancy leaves the incumbent unopposed |

**F-PD-034 — Contest result and tie-break.**

| Field | Definition |
|---|---|
| Expression | The highest of `vote_bp`, `popular_front_bp`, `institutional_bp` wins; ties: incumbent → higher approval → lower candidate index (incumbent 0, popular front 1, institutional 2) |
| Variables | The three scores; `approval`; the fixed index |
| Units | — |
| Range | — |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | F-PD-032, F-PD-033 |
| Example | 5,000 / 5,000 / 4,700 → incumbent (E30) |
| Rationale | A total, published order; no coin flip |
| Edge cases | Every tie is recorded with the invoked rule; a missing candidate is skipped |

**F-PD-035 — Confidence score and motion.**

| Field | Definition |
|---|---|
| Expression | `confidence_bp = Σ (institutional_weight_i × election_score_i)`; motion carries if `confidence_bp ≥ 4,500`; not tabled if `legitimacy ≥ 70` at `T − 24` |
| Variables | §3.5 vector; six scores; `legitimacy` |
| Units | Basis points |
| Range | 0…10,000 |
| Rounding | None (integer weights and scores) |
| Timing | P4.4 |
| Dependencies | F-PD-019, F-PD-031 |
| Example | Standard start 5,495 → carries (E31); 4,220 → fails (E32) |
| Rationale | Parliament, not the population, is the electorate |
| Edge cases | No incumbency allowance; no challenger; an early motion has no campaign |

**F-PD-036 — Control margin and warning band.**

| Field | Definition |
|---|---|
| Expression | `control_margin = legitimacy − control_threshold`; warning while `control_margin < 5`; safe while `control_margin ≥ 5` |
| Variables | `legitimacy`; the government threshold (§3.8) |
| Units | Legitimacy points |
| Range | −100…+100 |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | F-PD-019, §3.8 |
| Example | Junta at 44 with threshold 40 → margin +4 → `SUCCESSION`, pressure 0 (E36) |
| Rationale | Five points is one ordinary support change, not a percentage |
| Edge cases | The band is not a penalty; it changes no economic value |

**F-PD-037 — Pressure counter.**

| Field | Definition |
|---|---|
| Expression | `pressure_turns = min(12, pressure_turns + 1)` if `legitimacy < control_threshold`; `0` if `legitimacy ≥ control_threshold` |
| Variables | `legitimacy`; threshold; the stored counter |
| Units | Turns |
| Range | 0…12 |
| Rounding | None |
| Timing | P4.4, once per turn |
| Dependencies | F-PD-036, F-PD-019 |
| Example | Security 39 (threshold 40) → 1; twelve consecutive → challenge (E37) |
| Rationale | Consecutive, not cumulative; a warning can be answered |
| Edge cases | Dormant/protected turns do not increment; a state in `TRANSITION`/`CRISIS`/`RECOVERY` does not evaluate |

**F-PD-038 — Leadership state and duration.**

| Field | Definition |
|---|---|
| Expression | State ∈ {`NORMAL`, `ELECTORAL`, `SUCCESSION`, `TRANSITION`, `CRISIS`, `RECOVERY`}; on entry to `TRANSITION` set `leadership_state_until_turn = entry_turn + 12`; `CRISIS` → `+18`; `RECOVERY` → `+12`; other states clear it to 0 |
| Variables | The resolved event, `entry_turn` |
| Units | World turns |
| Range | 12, 18 or 0 |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | DMP-235, DMP-236 |
| Example | Transition 12 turns (E34); crisis 18 (E37) |
| Rationale | The state's duration is part of the state, not a timer the scheduler owns |
| Edge cases | An active state is never re-entered; a state still active one turn late is `INTERRUPTED` |

**F-PD-039 — Contest postponement and eligibility.**

| Field | Definition |
|---|---|
| Expression | `eligible = nation_status = active AND dormant = false AND protection expired AND leadership_state ∉ {TRANSITION, CRISIS, RECOVERY}`. A due contest opens its window once, at the first eligible turn, and resolves at the first eligible turn ≥ `max(scheduled_contest_turn, window_deadline)`. When the last blocking state clears before `window_deadline`, `leadership_state` restores to `ELECTORAL` for the remaining turns; after the deadline it stays `NORMAL` until resolution. **`NORMAL` and `ELECTORAL` are both resolving states** — `ELECTORAL` is the open window and is never a postponement condition |
| Variables | `nation_status`, `dormant`, `protection`, `leadership_state`, `scheduled_contest_turn`, `turn_id` |
| Units | — |
| Range | A resolution is never earlier than `scheduled_contest_turn`. The window is always 24 turns; a blocking state inside it delays the resolution without extending the window, so the resolution may be later than 24 turns after eligibility began |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | B-03, DMP-181, DMP-181a, DMP-181b, DMP-234 |
| Example | A contest due in `RECOVERY` opens its window at the first eligible turn and resolves at the end of that 24-turn window; anchor unchanged (E20) |
| Rationale | Postpone, never accelerate, never cancel — and never postpone the election an open window is preparing |
| Edge cases | A dormant nation resolves no contest; a protected nation is not voted out; `SUCCESSION` does not block a contest; an early motion is not a scheduled contest and never opens a window; a blocker that clears before the deadline restores `ELECTORAL`, and consecutive blockers with no eligible turn between them restore nothing until the last clears |

**F-PD-040 — Early crisis exit.**

| Field | Definition |
|---|---|
| Expression | At crisis turn `t ≥ 6`, if `legitimacy ≥ control_threshold + 5`, end `CRISIS` and enter `RECOVERY`; otherwise end at `t = 18` |
| Variables | `t` (crisis turns elapsed), `legitimacy`, threshold |
| Units | Turns |
| Range | 6…18 |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | F-PD-036, F-PD-038 |
| Example | Turn 6, legitimacy 46 ≥ 45 → exit (E45) |
| Rationale | Recovery is earned by restoring legitimacy, not by waiting |
| Edge cases | Early exit does not skip `RECOVERY`; there is no early exit before turn 6 |

**F-PD-041 — Challenge immunity.**

| Field | Definition |
|---|---|
| Expression | After `CRISIS` or a technocracy `TRANSITION` ends: `challenge_immune_until_turn = end_turn + 24`, `pressure_turns = 0` |
| Variables | `end_turn` |
| Units | World turns |
| Range | 24 |
| Rounding | None |
| Timing | P4.4 on state exit |
| Dependencies | F-PD-038 |
| Example | Crisis ends turn 18 → immunity to 42 |
| Rationale | Prevents a death spiral without permanent immunity |
| Edge cases | Immunity does not suppress the warning band or the display; it suppresses a new challenge only |

**F-PD-042 — A new nation's first contest.**

| Field | Definition |
|---|---|
| Expression | `next_contest_turn = creation_turn + 240`; no contest, early motion or pressure evaluation before it |
| Variables | `creation_turn` |
| Units | World turns |
| Range | 240 |
| Rounding | None |
| Timing | Creation |
| Dependencies | F-PD-027, B-03 |
| Example | Created turn 100 → 340; campaign opens 316 (E47) |
| Rationale | A new player governs for 20 days before facing a vote |
| Edge cases | A reroll is a new creation; it copies no political state (E48) |

**F-PD-043 — Contest idempotency.**

| Field | Definition |
|---|---|
| Expression | A contest record is unique on `(nation_id, scheduled_contest_turn)`; a resolver that finds it returns the stored record; a campaign action is unique on `(nation_id, contest_turn, action_id, sequence)`; the turn marker is `politics_actions_settled_turn` |
| Variables | The keys; the stored record |
| Units | — |
| Range | — |
| Rounding | None |
| Timing | Every resolution and submission |
| Dependencies | B-04 ledger keys, DMP-182, DMP-243 |
| Example | Turn 377 resolved twice returns 5,749 once (E46) |
| Rationale | Applying a political event twice is the worst bug in the system |
| Edge cases | A late resolution stores both scheduled and resolved turns; a duplicate charge is reconstructed from the ledger |

**F-PD-044 — Contest audit record.**

| Field | Definition |
|---|---|
| Expression | One immutable record per resolved contest with `(nation_id, scheduled_turn, resolved_turn, kind, outcome, scores, campaign, state_in, formula_version, tie_break)` |
| Variables | The resolution inputs and outputs |
| Units | — |
| Range | — |
| Rounding | None |
| Timing | P4.4 |
| Dependencies | F-PD-032…F-PD-035, F-PD-043 |
| Example | E26 records 5,749, both challenger scores and the six contributions |
| Rationale | A player must be able to audit the result without trusting the server's word |
| Edge cases | A correction is a new record naming the original; the original is never edited |

**Verification map for Part II.** `qa_backups/verify_politics_numbers.py` recomputes E19–E49 from these formulas and fails on any drift. The values it checks are the register's constants, not a second copy: a changed constant that is not changed here fails the document check.

**§12 is now closed.** The reserved list above is retained as history; every item is answered by F-PD-026…F-PD-044 and B-06 §§24–38. A later prompt may add a formula here only with a new `F-PD-` ID, never by editing an existing one.

## 14. Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-25 | Initial register for Prompt 06A: population, housing, crowding, six supports, approval, stability, legitimacy, service cost, research adjustment, policy and government lookups, stacking rules and the settlement order. No election or crisis formula. |
| 1.1 | 2026-10-25 | Range cells for F-PD-004…F-PD-009 and the §3.7 support-term table corrected against the formulas at the documented input bounds: labour tax −3…+2; industry tax −7…+6; commerce tax −9…+8; rural/industry/commerce/security stability −10 or −13…+2; food and processing share 0…+40; rural service 0…+5; scholars service 0…+12. No expression changed |
| 1.2 | 2026-10-25 | F-PD-002 now computes `raw` on both the growth/cap and crowding paths and returns `max(1,000, raw)`, with the floor example (raw 993 → 1,000) and edge-case rules; F-PD-004, F-PD-005, F-PD-006, F-PD-007 and F-PD-008 use `(300 − tax_bp) // divisor`, the signed form that holds the published −3…+2, −7…+6 and −9…+8 endpoints; Range cells state the permitted 200/300/400 rates. No coefficient changed |
| 2.0 | 2026-10-25 | Prompt 06B: F-PD-026 political stability penalty (0/800/1,500/400); F-PD-027–028 schedule and campaign window; F-PD-029–030 campaign cost and capped bonus; F-PD-031–032 election score and turnout-weighted vote; F-PD-033–034 challenger scores, result and tie-break; F-PD-035 confidence; F-PD-036–037 control margin and pressure; F-PD-038 state durations; F-PD-039–042 postponement, early exit, immunity and first contest; F-PD-043–044 idempotency and audit. §3.8 constants, §3.9 turnout, F-PD-017 gains the penalty term, §10 gains the P4.4 row, §12 closed, §11 extended. Part I formulas keep their meaning |
| 2.4 | 2026-10-28 | Fourth 06B micro-correction, register side: **F-PD-028** and **F-PD-029** publish the submission window as `turn_id < resolution_turn` (`< T` only on an on-time opening), matching DMP-183/DMP-188/DMP-190's `registration_close_turn`. The delayed 980/992/1002/1004 example, the restoration rule and every constant are unchanged. No formula value changed. |
| 2.3 | 2026-10-28 | Third 06B micro-correction, register side: **F-PD-028** publishes the campaign's own deadline anchor with the delayed 980/992/1002/1004 example; **F-PD-039** publishes the `ELECTORAL` restoration and the no-gap rule. No formula value changed. |
| 2.2 | 2026-10-28 | Second 06B micro-correction, register side: **F-PD-028** publishes the once-only window — `campaign_open_turn` is computed once, `window_deadline = campaign_open_turn + 24`, and `resolution_turn` is the first eligible turn ≥ `max(scheduled_contest_turn, window_deadline)` — so an open campaign interrupted by a blocking state delays resolution without restarting the clock. **F-PD-039** keeps `SUCCESSION` non-blocking. No formula value changed. |
| 2.1 | 2026-10-28 | Final 06B micro-correction, register side: **F-PD-027** publishes the anchored schedule with the catch-up multiplier `k = ceil((resolved_contest_turn + 25 − scheduled_contest_turn) / 240)` so the next term is never anchored on a late resolution; **F-PD-028** publishes the once-only window — open at the first eligible turn from `T − 24`, resolution 24 turns later — and forbids a window whose deadlines are in the past; **F-PD-039** replaces the `NORMAL`-only condition with the true resolving-state rule (`NORMAL` **or** `ELECTORAL`, blocking states `TRANSITION`/`CRISIS`/`RECOVERY`). The status header now describes the register's real coverage (F-PD-001…F-PD-044) instead of the superseded "06B formulas are missing" text. No constant, range, formula meaning or published number changed; the arithmetic checker was extended and still passes |
