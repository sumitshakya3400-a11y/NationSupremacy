# Prompt 14C-C1 — B-05 city-founding gate correction and fully loaded research investment reconciliation

**Stage:** Stage 2 · **Parent:** Prompt 14C · **Subphase:** 14C-C1 · **Primary system:** B-05
**Executed:** 2026-11-18 · **Baseline:** Project X (114) independent audit; live repository at `3b9cadc` + Prompt 14C working-tree changes
**Status:** **PROMPT 14C-C1 COMPLETE — corrective evidence. PROMPT 14C IS READY FOR FINAL OWNER REVIEW — NOT YET OWNER ACCEPTED.** No runtime implementation, no balance acceptance and no playtesting exist.
**Authority:** narrow owner-authorized correction following the Project X (114) audit; Prompt 14A and Prompt 14B remain accepted and are not reopened; [D-014](../AUTONOMOUS_DECISION_POLICY.md).
**Read with:** [Prompt 14C completion report](29_prompt_14C_b05_cities_completion_report.md) (historical body preserved) · [B-05 rulebook](11_cities_infrastructure_production_and_research.md) · [B-05 formula register](11_city_infrastructure_production_and_research_formula_register.md) · [`14C_verify_b05_cities.py`](../qa_backups/14C_verify_b05_cities.py) · [D-247](../DECISIONS.md)

---

## 1. Scope, preservation and what changed

### 1.1 The two audited findings

The Project X (114) independent audit identified two material numerical-analysis gaps in the Prompt 14C package:

- **Finding A** — the 12th-city founding-gate infrastructure cost was reported as **12,340 crowns**; the correct minimum no-discount investment is **12,450 crowns**.
- **Finding B** — the research-rate comparison measured institutes, upkeep and technology crowns, but did not include the infrastructure and city-founding investment required to accommodate larger institute configurations; the comparison was not a fully loaded national investment.

Both are calculation and analytical-reconciliation corrections. **No B-05 or B-04 formula, recipe, price, maintenance rate or tax value was redesigned or changed.**

### 1.2 Preservation

- Prompt 14A remains **OWNER ACCEPTED**; Prompt 14B remains **OWNER ACCEPTED and CLOSED (2026-11-18)**. Neither is reopened.
- The original [Prompt 14C completion report](29_prompt_14C_b05_cities_completion_report.md) is **preserved with its historical body unchanged**, including the superseded 12,340 figure; a dated correction notice at its top points to this addendum.
- **D-246 is preserved as a historical decision.** The new **D-247 / DD-293** supersedes only its incorrect 12-city gate calculation and clarifies the scope of its research-cost figures; the unrelated 14C findings in D-246 stand.
- The 41 `F-CI` identifiers, 73 B-05 parameter records, 17 buildings, 12 technologies, four programmes, matrix (33/4/2/0), 12 examples and the simulation model are preserved. The global counts remain **295 formulas / 393 parameter records / 73 B-05 records**.
- No B-04 document was edited. No owner-reserved parameter was changed. No staging or commit was performed.

### 1.3 The corrections at a glance

| Item | Prompt 14C (historical) | Prompt 14C-C1 (current) |
|---|---|---|
| 12th-city gate investment | 12,340 crowns (12-city calculation) | **12,450 crowns** (11 existing cities; 950 additional levels) |
| Research cost presentation | Research-only figures labelled "total research cost" | **Research-only** and **fully loaded B-05 establishment** distinguished |
| Two-institute configuration | Infrastructure omitted | **+270 crowns** (capital 50 → 70) |
| Four/six/twelve/twenty-four institutes | No city or infrastructure cost | City founding and infrastructure included; fully loaded table below |
| Validator | Gate value printed, not asserted | **15 explicit checks; 9 self-tests**, including a regression that rejects 12,340 |

---

## 2. Finding A — the 12th-city founding gate

### 2.1 The authoritative rule

URB-032 requires, for the `k`-th city, `k ≤ 12` and national infrastructure `ΣI ≥ 100 × (k − 1)`; **the city being founded does not exist at submission and cannot contribute its own starting infrastructure**. At the 12th city the requirement is `100 × 11 = 1,100` national infrastructure across the **eleven existing cities**. F-CI-003 defines the sum, F-CI-004 the unit cost, F-CI-005 the order cost and F-CI-007 the gate.

### 2.2 The correct pre-founding state

Immediately before founding the 12th city the standard development path holds eleven cities:

| City | Starting infrastructure |
|---|---:|
| Capital | 50 |
| Cities 2–11 (ten cities) | 10 each |
| **Total** | **150** |

The nation must acquire `1,100 − 150 = **950**` additional infrastructure levels across those eleven cities.

### 2.3 The minimum-cost allocation and cost

The minimum no-discount allocation is:

- Capital: 50 → 100 = **750 crowns** (`130 + 140 + 150 + 160 + 170`).
- Each of the ten other cities: 10 → 100 = **1,170 crowns** (`10 × (9 + 10 + … + 17)`).
- Total: `750 + 10 × 1,170 = **12,450 crowns**`.
- Final national infrastructure: `11 × 100 = 1,100`, which exactly satisfies the gate.

### 2.4 Independent optimality verification (not hardcoded)

The verifier builds every available marginal level `(unit_cost = 8 + floor(j/10), city, j)` for the eleven cities, sorts them and takes the 950 cheapest. The result:

- **950 cheapest levels cost 12,450 crowns**;
- the **highest marginal cost taken is 17**, and the **next available marginal cost is 18** — so no substitution can reduce the cost (the chosen set is the prefix of the global marginal-cost order, and the cut is at a strict price boundary);
- the chosen levels are exactly 50 in the capital and 90 in each of the ten other cities, i.e. **eleven cities at 100**;
- the allocation respects the 500 maximum and the integer rule.

This is an independent marginal-cost merge, not a reuse of the report's display arithmetic. It proves the 12,450 figure is the minimum, not merely a feasible total.

### 2.5 Why 12,340 is invalid

The 14C calculation started from **twelve** cities at 10 (`12 × 10 = 120`), took `1,100 − 120 = 980` additional levels and minimised that distribution. That is invalid for the 12th-city gate because the 12th city **does not exist before the gate it must pass**. The founding condition is evaluated against eleven cities, 950 levels and 12,450 crowns. The 12,340 figure is superseded, not an alternative. The verifier now includes a regression that fails if the 12-city method is accepted.

### 2.6 Discount treatment (separate scenario, never the baseline)

The baseline of **12,450 crowns** is **no-discount**. Civil Survey (`tech_civ_survey`) has no prerequisite, costs **20 RP + 140 crowns**, takes effect at the turn after completion, and removes **1,000 bp (10%)** from an infrastructure order after the marginal sum (F-CI-005, `ceil(base × 9,000 / 10,000)`).

- If Civil Survey is active **before** the 950 gate levels are ordered, the gate costs `ceil(12,450 × 0.9) = **11,205 crowns**`, a saving of **1,245 crowns** before the technology's own cost.
- The technology costs 140 crowns + 20 RP and requires a standing research institute and an active project; those are not free. The net crown saving before RP/lab costs is **1,105**.
- Orders placed **before** the technology completes pay full price; no discount is retroactive and no future unlock is assumed. The baseline table in §3 remains no-discount for comparability.
- The same 10% treatment, if legally active, would reduce the research-infrastructure components: 270→243, 750→675, 1,920→1,728, 5,430→4,887 and 12,450→11,205. This is presented as a scenario, not merged into the baseline.

### 2.7 Founding costs remain a separate expense

The independently verified city-founding total for cities 2–12 is unchanged: **101,750 crowns + 220 steel** (book value 103,290 including 1,540 of steel at 7). The gate is a separate infrastructure expense of **12,450 crowns**. The combined baseline is:

**114,200 crowns + 220 steel**, before any facility construction or operating costs.

There is no double counting: the 101,750 is the F-CI-006 sum, and the 12,450 is infrastructure capex; neither term contains the other.

### 2.8 Every superseded reference

The following references used **12,340** and are superseded by this addendum:

| Location | Original text | Status |
|---|---|---|
| [Prompt 14C report §4.1](29_prompt_14C_b05_cities_completion_report.md) (current line 245) | "the cheapest distribution … costs **12,340 crowns**" and "980 additional levels" | **Superseded**: eleven cities, 950 levels, 12,450 crowns |
| [Prompt 14C report §4.3](29_prompt_14C_b05_cities_completion_report.md) (current line 281), strategy F | "101,750 + 220 steel + **12,340** gate infrastructure" | **Superseded**: 101,750 + 220 steel + **12,450** = 114,200 crowns + 220 steel |
| [Prompt 14C report §15.3](29_prompt_14C_b05_cities_completion_report.md) (current line 981), playtest item 3 | "gate cost (**12,340**)" | **Superseded**: gate cost **12,450** |
| [D-246](../DECISIONS.md) | "the 12-city gate requiring **12,340 crowns** of additional infrastructure" | **Superseded only for this figure** by D-247; all other D-246 findings stand |
| [Progress log §117](06_stage_2_progress_log.md) | "the 12-city gate (**12,340 crowns**)" | Historical record preserved; this addendum and §118 correct it |
| Old `14C_verify_b05_cities.py` INFO line | printed the computed 12,340 without asserting correctness | **Corrected**: the verifier now asserts 12,450 and the eleven-city basis |

The original Prompt 14C report body is not rewritten; the correction notice at its top and this table identify the superseded text.

---

## 3. Finding B — fully loaded research investment

### 3.1 What the original comparison measured

The original §8.2 table measured **research-only** expenditure: laboratory crown construction at 500 each (shown at book value 640 with 20 steel valued at 7), laboratory upkeep `2 × N × T(N)` and the 3,180-crown technology tree. It did **not** include:

- the infrastructure needed to fit two laboratories in the capital (50 → 70);
- the infrastructure and city founding needed when the two-per-city limit forces additional cities;
- the city-founding steel;
- the steel procurement or opportunity value beyond the opening 20 units.

Those figures remain valid **as research-only metrics**. They are not the full national investment, and the addendum now labels them accordingly.

### 3.2 Standard starting conditions and capacity

| Parameter | Value |
|---|---:|
| Cities / capital infrastructure | 1 / 50 |
| Development capacity | 15 DC |
| Used / free capacity | 11 DC / **4 DC** |
| Research institute DC | **3 DC** |
| Maximum institutes per city | **2** |
| Laboratory crowns / steel / book | 500 / 20 / **640** |
| Laboratory upkeep | 2 crowns/turn |
| Research output | 1 RP per standing institute per turn |
| Tree | 448 RP, 12 technologies, **3,180 crowns** |

**Two institutes in one city.** One institute consumes 3 of the 4 free DC and fits. Two consume 6 DC, so the capital must gain 2 DC; infrastructure 50 → 70 adds 2 DC and costs `130 + 140 = **270 crowns**`. This investment was missing from the original comparison.

**City requirements from URB-032 and the two-per-city limit:**

| Institutes | Cities | Why |
|---:|---:|---|
| 1 | 1 | 3 DC ≤ 4 free |
| 2 | 1 | 6 DC requires 50 → 70 infrastructure (270 crowns) |
| 4 | 2 | 2 per city; city 2 requires national infrastructure ≥ 100 |
| 6 | 3 | city 3 requires national infrastructure ≥ 200 |
| 12 | 6 | city 6 requires national infrastructure ≥ 500 |
| 24 | 12 | city 12 requires national infrastructure ≥ 1,100 |

The minimum infrastructure to support each city count (no discount):

| Cities | Allocation | Infrastructure crowns |
|---:|---|---:|
| 1 (2 labs) | capital 50 → 70 | **270** |
| 2 | capital 50 → 100; city 2 at 10 | **750** |
| 3 | capital 100; city 2 10 → 100; city 3 at 10 | **1,920** |
| 6 | capital 100; cities 2–5 10 → 100; city 6 at 10 | **5,430** |
| 12 | capital 100; cities 2–11 10 → 100; city 12 at 10 | **12,450** |

The 12-city line is the corrected Finding A result. The 24-institute configuration therefore includes the 12,450-crown gate.

### 3.3 The fully loaded investment table

`T(N) = ceil(448 / N)` for N > 0. **Total crown expenditure excludes the steel value**, which is shown separately; **Reference-value total = total crowns + 7 × total steel**. The table is no-discount.

| Institutes | Cities | Duration | Infra crowns | Founding crowns | Founding steel | Lab crowns | Lab steel | Total steel | Lab upkeep | Tree crowns | Steel value at 7 | Total crown expenditure | Total steel required | Reference-value total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 448 | 0 | 0 | 0 | 500 | 20 | 20 | 896 | 3,180 | 140 | 4,576 | 20 | 4,716 |
| 2 | 1 | 224 | 270 | 0 | 0 | 1,000 | 40 | 40 | 896 | 3,180 | 280 | 5,346 | 40 | 5,626 |
| 4 | 2 | 112 | 750 | 1,000 | 20 | 2,000 | 80 | 100 | 896 | 3,180 | 700 | 7,826 | 100 | 8,526 |
| 6 | 3 | 75 | 1,920 | 2,750 | 40 | 3,000 | 120 | 160 | 900 | 3,180 | 1,120 | 11,750 | 160 | 12,870 |
| 12 | 6 | 38 | 5,430 | 15,500 | 100 | 6,000 | 240 | 340 | 912 | 3,180 | 2,380 | 31,022 | 340 | 33,402 |
| 24 | 12 | 19 | 12,450 | 101,750 | 220 | 12,000 | 480 | 700 | 912 | 3,180 | 4,900 | 130,292 | 700 | 135,192 |

**Zero institutes.** No research project can progress; the duration is not finite; no laboratory, infrastructure, founding or technology expenditure is incurred. A nation with no standing institute cannot start a project (URB-059).

**The 24-institute upkeep is 912 crowns** (`2 × 24 × 19`), not 456. The 12-institute upkeep is also 912 (`2 × 12 × 38`); the 6-institute upkeep is 900 (`2 × 6 × 75`); the 4-institute upkeep is 896 (`2 × 4 × 112`).

### 3.4 Additional investment versus the preceding configuration

| Institutes | Crown delta | Steel delta | Reference-value delta |
|---:|---:|---:|---:|
| 1 (vs 0) | +4,576 | +20 | +4,716 |
| 2 (vs 1) | +770 | +20 | +910 |
| 4 (vs 2) | +2,480 | +60 | +2,900 |
| 6 (vs 4) | +3,924 | +60 | +4,344 |
| 12 (vs 6) | +19,272 | +180 | +20,532 |
| 24 (vs 12) | +99,270 | +360 | +101,790 |

The two-institute increment is **+770 crowns** (500 laboratory + 270 infrastructure) and **+20 steel**; the four-institute increment adds the second city (1,000 crowns + 20 steel) and 750 infrastructure; the late increments are dominated by city founding.

### 3.5 Steel procurement and opportunity cost

| Institutes | Gross steel | Opening stock | Steel beyond opening | Opportunity value at 7 |
|---:|---:|---:|---:|---:|
| 1 | 20 | 20 | **0** | 140 |
| 2 | 40 | 20 | **20** | 280 |
| 4 | 100 | 20 | **80** | 700 |
| 6 | 160 | 20 | **140** | 1,120 |
| 12 | 340 | 20 | **320** | 2,380 |
| 24 | 700 | 20 | **680** | 4,900 |

The 24-institute path requires **680 steel beyond the opening stock**. That steel is not free: it must be produced under B-04's steel recipe (10 iron + 6 coal → 8 steel), bought through B-07 trade, or acquired by transfer/reward under the owning rules. The table's 4,900 is the **opportunity value at the reference price**, not a crown payment. No B-04 recipe, price or accounting rule was changed. The standard start holds exactly 20 steel, so even the **two-institute** configuration requires 20 more steel; the 14C simulation S09 confirms the second laboratory was steel-gated in practice.

### 3.6 Research-only versus fully loaded — the bridge

| Institutes | Original §8.2 "total research cost" (lab book + upkeep + tree) | + Infrastructure | + Founding crowns | + Founding steel value | = Fully loaded reference |
|---:|---:|---:|---:|---:|---:|
| 1 | 4,716 | 0 | 0 | 0 | **4,716** |
| 2 | 5,356 | 270 | 0 | 0 | **5,626** |
| 4 | 6,636 | 750 | 1,000 | 140 | **8,526** |
| 6 | 7,920 | 1,920 | 2,750 | 280 | **12,870** |
| 12 | 11,772 | 5,430 | 15,500 | 700 | **33,402** |
| 24 | 19,452 | 12,450 | 101,750 | 1,540 | **135,192** |

The original figures used the laboratory **book value 640** (500 crowns + 20 steel at 7). The new table separates **lab crowns 500** from **lab steel 20**; its reference total equals the bridge. The original 24-institute "total research cost" of 19,452 is therefore **research-only**; the fully loaded reference is **135,192**, a **6.95×** difference driven by the twelve-city network. The original comparison must not be presented as the full national investment requirement.

### 3.7 Feasibility and construction sequence

The actual sequence is bounded by one construction action per city per turn, one founding per nation per turn, the gate at submission, next-turn activation of a new facility and the two-institute limit:

| Institutes | Cities | Labs per city | Minimum infrastructure distribution | Capacity used | Founding | All labs standing at start of turn | Research activation (network-first sequence) |
|---:|---:|---|---|---|---|---:|---:|
| 1 | 1 | 1 | capital 50 | 14/15 | — | **T2** | **T2** |
| 2 | 1 | 2 | capital 70 | 17/20 | — | **T4** | **T2** |
| 4 | 2 | 2 + 2 | capital 100; city 2 at 10 | capital 17/20; city 2 6/11 | city 2 | **T5** | **T4** |
| 6 | 3 | 2 each | capital 100; city 2 100; city 3 10 | capital 17/20; city 2 6/20; city 3 6/11 | cities 2–3 | **T7** | **T4** |
| 12 | 6 | 2 each | capital 100; cities 2–5 100; city 6 10 | capital 17/20; cities 2–5 6/20; city 6 6/11 | cities 2–6 | **T13** | **T4** |
| 24 | 12 | 2 each | capital 100; cities 2–11 100; city 12 10 | capital 17/20; cities 2–11 6/20; city 12 6/11 | cities 2–12 | **T25** | **T4** |

The earliest sequence is:

- **1 institute:** T1 build the laboratory; standing T2.
- **2 institutes:** T1 lab 1; T2 capital 50 → 70 (270); T3 lab 2; both standing T4. A research project can start at T2 with one lab.
- **4 institutes:** T1 capital 50 → 100; T2 found city 2; T3 capital lab 1 and city 2 lab 1; T4 both second labs; all four standing T5.
- **6 institutes:** T1 capital 50 → 100; T2 found city 2; T3 city 2 10 → 100 and capital lab 1; T4 found city 3 and capital lab 2; T5 city 2 lab 1 and city 3 lab 1; T6 city 2 lab 2 and city 3 lab 2; all six standing T7.
- **12 institutes:** the same pattern extends to six cities; city k is founded on even turns 2, 4, 6, 8, 10 and its 10 → 100 upgrade follows on the next odd turn; the last city's second lab stands at T13.
- **24 institutes:** the pattern extends to twelve cities; the last city is founded at T22 and its second lab stands at T25.

**Research duration versus network time.** `T(N) = ceil(448/N)` measures RP generation with N standing institutes; it is **not** the time to establish the network. The network times are T2/T4/T5/T7/T13/T25 for the six non-zero configurations. A player may start research earlier with fewer labs (the activation boundary above is T2 for every N ≥ 1 if a first lab is built first), but that delays the full network and the aggregate rate. The actual sequential technology timeline also depends on prerequisites, one project at a time, RP banking and crown availability; the aggregate duration is a comparative metric, not the exact unlock schedule.

**Funding feasibility.** The fully loaded table is the investment requirement, not a claim that the standard start can fund it from opening cash. The standard start holds 1,500 crowns and 20 steel; one lab (500 + 20 steel) is affordable, but the two-lab configuration needs 1,270 crowns and 40 steel, and the larger configurations require 7,826–130,292 crowns. The standard start's operating cash is approximately neutral (14B: −1/turn), so the larger networks require economic growth, trade or the steel industry. The 14C simulation S09 reached only one lab in 120 turns because the second was steel-gated; S10/S11 use prepared mid-game states and are not standard-start funding evidence.

### 3.8 Corrected research-payback implications

The fully loaded investment changes the payback conclusion, not merely the setup cost. Allocating the reference-value total across the 448 RP gives a **fully loaded reference cost per RP** and a payback for a representative 24-RP technology (e.g. `tech_agri_rotation`, +4 food/turn at four farms):

| Institutes | Reference total | Reference per RP | 24-RP tech share | Payback at +4 food/turn |
|---:|---:|---:|---:|---:|
| 1 | 4,716 | 10.53 | **252.6** | **63.2 turns** |
| 2 | 5,626 | 12.56 | **301.4** | **75.3 turns** |
| 4 | 8,526 | 19.03 | **456.8** | **114.2 turns** |
| 6 | 12,870 | 28.73 | **689.5** | **172.4 turns** |
| 12 | 33,402 | 74.56 | **1,789.4** | **447.3 turns** |
| 24 | 135,192 | 301.77 | **7,242.4** | **1,810.6 turns** |

The per-RP allocation is an analytical share of the network, not a rule; the point is the **scale penalty**: a 24-institute network costs about **28.7×** the one-institute network per RP (301.77 vs 10.53) once infrastructure, city founding and steel are loaded. A single 24-RP food technology can never justify a 24-lab network on its own; the network must be justified by the **whole tree** (all 448 RP), the strategic value of calendar time, or other branches' effects. The research-only figure understated this by up to 6.95× in absolute investment and much more in the marginal per-RP comparison.

**Capacity implications.** Every laboratory consumes **3 DC** and the two-per-city limit forces new cities for larger networks; the capital at 50 fits one lab, two need a 50→70 upgrade, and beyond two the network consumes **city founding slots and 3–12 cities** without adding any production facility. The research network is therefore a **city-development decision**, not a laboratory-only purchase: its opportunity cost includes the farms, power and industry those cities could otherwise have hosted.

---

## 4. Validator and numerical-test corrections

The audit correctly found that the original `14C_verify_b05_cities.py` printed the computed gate cost as an INFO line without asserting its correctness. The verifier now:

1. Computes the gate from **eleven existing cities**, `150` starting infrastructure and `950` additional levels.
2. Asserts the **12,450** minimum and the **750 + 10 × 1,170** decomposition.
3. Proves optimality with an **independent marginal-cost merge**: the 950 cheapest levels, highest taken 17, next 18, final distribution eleven cities at 100.
4. Asserts that the **12-city/980-level method is invalid** and that 12,340 is rejected (a self-test reproduces the old method and requires failure).
5. Asserts all seven research configurations: cities, duration, infrastructure, founding, lab crowns, lab steel, total steel, upkeep, tree, total crowns and reference value.
6. Asserts **two institutes require 270 infrastructure crowns**, **four/six/twelve/twenty-four institutes require 2/3/6/12 cities**, and **24-institute upkeep is 912, not 456**.
7. Runs an **independent network scheduler**: one action per city per turn, one founding per nation per turn, gates at submission, next-turn activation and DC checks; it must return T2/T4/T5/T7/T13/T25.
8. Checks the addendum's fully loaded table, the presence of D-247 and the explicit supersession of 12,340.

**New check count:** 15 checks and 9 self-tests (the Prompt 14C-time 10 checks / 5 self-tests are preserved as the historical result and extended, not replaced). The self-tests mutate the gate method, the gate total, the 24-lab upkeep and the 4-lab city count and require the checks to fail.

---

## 5. Decision record

**D-247 / DD-293** is recorded in [DECISIONS.md](../DECISIONS.md) and the [design register](04_approved_and_provisional_decisions.md). It:

- records why 12,340 was wrong (the 12th city was counted before founding) and why **12,450** is the correct no-discount baseline;
- records the research-only versus fully loaded distinction and the corrected institute comparisons;
- records the evidence and validators;
- supersedes **only** the incorrect 12-city gate calculation and the scope of D-246's research-cost figures;
- preserves D-246 and every unrelated 14C finding;
- confirms that **no B-05 or B-04 formula was redesigned**.

---

## 6. What Prompt 14C-C1 did not do

- No Prompt 14A or 14B work was reopened; no B-04 document was edited.
- No B-05 formula, identifier, constant or numerical status was changed; the 41/73/17/12/4 counts are preserved.
- No runtime implementation, balance acceptance or playtesting is claimed; the 64 T05 specifications remain **0 executed**.
- No simulation scenario was changed; the existing results stand. The corrected research table is a new analytical reconciliation, not a simulation result.
- No new documentation-validator security framework was built; the existing verifier was extended with targeted assertions.

---

## 7. Validation and remaining limitations

**Executed for this correction (actual commands and results, run from `docs/` on 2026-11-18):**

| # | Command | Actual result | Exit |
|---:|---|---|---:|
| 1 | `python qa_backups/verify_city_numbers.py` | **267/267 passed** | 0 |
| 2 | `python qa_backups/verify_economy_numbers.py` | **170/170 passed** | 0 |
| 3 | `python qa_backups/14B_verify_b04_economy.py` | **321/321 passed — ALL CHECKS PASSED** | 0 |
| 4 | `python qa_backups/14A_validate_numerical_foundation.py` | **64 checks, 0 failed — PASS** | 0 |
| 5 | `python qa_backups/14C_verify_b05_cities.py` | **15/15 checks passed; 9/9 self-tests** | 0 |
| 6 | `python qa_backups/14C_simulate_b05.py` | 24 scenarios × 10/30/60/120; **0 invariant problems** | 0 |
| 7 | `python qa_backups/09_validate.py` | **371/371 passed** | 0 |
| 8 | `python qa_backups/12A_validate_foundations.py` | **45/45 passed** | 0 |
| 9 | `python qa_backups/13A_validate_ui_foundations.py` | **34/34 passed** | 0 |
| 10 | `python qa_backups/13B_validate_ui_specifications.py` | **28/28 passed** | 0 |
| 11 | `python qa_backups/validate_links.py` | **0 unresolved** (382 external skipped; 34 anchors) | 0 |
| 12 | `python qa_backups/validate_final.py` | **ALL CHECKS PASSED** | 0 |
| 13 | `python qa_backups/test_decision_registers.py` | **12/12 — OK** | 0 |
| 14 | `python qa_backups/test_next_action.py` | **27/27 — OK** | 0 |
| 15 | Inherited: `verify_politics_numbers.py` | **878/879 — 1 inherited failure** | 1 |
| 16 | Inherited: `11A_validate_research.py` | **29/30 — 1 inherited failure** | 1 |
| 17 | Inherited: `09A_validate_alliance.py` | **941/943 — 2 inherited failures** | 1 |
| 18 | Inherited: `09B_validate_alliance_semantic.py` | **8 frozen-scope defects** | 1 |

The four inherited failures are unchanged, pre-existing, and outside this correction's scope. `0 of 64` T05 specifications are executed; no runtime, balance or playtest is claimed. The 14C-time verifier result (10 checks / 5 self-tests) is preserved as the historical result; the corrected verifier extends it to 15 / 9 without deleting or relaxing any check.

**Remaining limitations.** The standard start cannot fund the larger research networks from opening cash; steel beyond 20 units must be produced or bought; the network-time schedule is a rules-feasibility sequence, not a claim that a player can afford it by that turn; the B-04 contradictions C-14C-01 and C-14C-02 remain B-04-owned handoffs; the 14B validator technical debt and the four inherited historical failures remain; no balance or playtest is claimed.

**Readiness.** **PROMPT 14C IS READY FOR FINAL OWNER REVIEW — NOT YET OWNER ACCEPTED.** The two audited findings are corrected, independently verified, tested and documented; the historical records are preserved. Prompt 14D remains **NOT AUTHORIZED**.

---

## 8. Git closeout

**Branch:** `main`. **HEAD at start:** `3b9cadc`. **Staged:** 0. No staging, commit, checkout, reset, clean, stash, branch or push was performed.

**Working-tree state at the end of Prompt 14C-C1 (read-only `git status --porcelain`): 20 modified tracked paths, 7 untracked files, 27 individual paths, 0 staged changes.** The detail is the Prompt 14C closeout list plus:

| Added/modified by C1 | Nature |
|---|---|
| `docs/stage-2/30_prompt_14C-C1_city_gate_and_research_investment_correction.md` | **new** — this corrective evidence |
| `docs/DECISIONS.md` | D-247 appended; D-246 preserved |
| `docs/stage-2/04_approved_and_provisional_decisions.md` | DD-293 appended |
| `docs/qa_backups/14C_verify_b05_cities.py` | gate and fully loaded research checks and self-tests |
| `docs/stage-2/29_prompt_14C_b05_cities_completion_report.md` | dated correction notice at the top only; historical body preserved |
| Continuity files | Prompt 14C-C1 status, decision range and next action |
| Contract evidence registry | hash refresh after the legitimate continuity amendments; review status unchanged |

**Generated cache artifacts.** `docs/qa_backups/__pycache__/` may contain refreshed `.pyc` files; they are generated, ignored by `.gitignore` and not substantive changes.

**B-04 preservation.** No B-04 formula, recipe, price, maintenance rate, tax value or rulebook text was edited.

---

**End of Prompt 14C-C1 correction addendum.**
