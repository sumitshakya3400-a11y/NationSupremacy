> **CORRECTION NOTICE — 2026-11-18 (Prompt 14C-C1; the body below is preserved as the historical 14C record):** The **12,340-crown** 12th-city gate figure in §4.1, the §4.3 strategy-F row and the §15.3 playtest item is **SUPERSEDED**. The correct minimum no-discount gate is **12,450 crowns**, calculated from **eleven existing cities** (capital 50 + ten cities at 10 = 150 infrastructure; 950 additional levels; `750 + 10 × 1,170`). The §8.2 research figures are **research-only** metrics, not the fully loaded national investment; the fully loaded standard-start networks include infrastructure and city founding (24 institutes: **130,292 crowns + 700 steel**, reference 135,192, not 19,452). See [30_prompt_14C-C1_city_gate_and_research_investment_correction.md](30_prompt_14C-C1_city_gate_and_research_investment_correction.md) and **D-247 / DD-293**. No other 14C finding was changed; the corrected verifier reports **15/15 checks and 9/9 self-tests**.

# Prompt 14C — B-05 cities, infrastructure, production and research — completion report

**Stage:** Stage 2 · **Parent:** Prompt 14 · **Subphase:** 14C · **System:** B-05
**Supporting systems:** B-02, B-03, B-04, B-06, B-07, B-08, B-09, B-10 (plus the B-11/B-12 contracts)
**Executed:** 2026-11-18 · **Baseline:** Project X (113) / live repository at `3b9cadc`
**Status:** **PROMPT 14C COMPLETE AT THE DOCUMENTATION, NUMERICAL-ANALYSIS, SIMULATION AND DOCUMENT-VALIDATION LEVEL.** No B-05 formula has been implemented, run against a database or scheduler, or played. No numerical value was retuned. The B-05 balance is not accepted.
**Authority:** explicit owner authorization dated 18 November 2026; Prompt 14A owner acceptance (17 November 2026); Prompt 14B owner acceptance and closure (18 November 2026); [D-014](../AUTONOMOUS_DECISION_POLICY.md).
**Read with:** [B-05 rulebook](11_cities_infrastructure_production_and_research.md) · [B-05 formula register](11_city_infrastructure_production_and_research_formula_register.md) · [B-04 rulebook](10_economy_resources_treasury_and_finances.md) · [B-04 register](10_economic_formula_and_balance_register.md) · [B-14 canonical](22_formulas_and_balance.md) · [numerical baseline QA report](22_numerical_baseline_qa_report.md) · [`14C_verify_b05_cities.py`](../qa_backups/14C_verify_b05_cities.py) · [`14C_simulate_b05.py`](../qa_backups/14C_simulate_b05.py)

---

## 1. Assignment scope and source reconciliation

### 1.1 What was executed

1. Read the governance set in full: `AUTONOMOUS_DECISION_POLICY.md` (D-014), `AI_CONTEXT.md`, `AI_HANDOFF.md`, `DECISIONS.md`, the Stage 2 roadmap and progress log, B-05 and its formula register, the four B-14 documents, the B-04 rulebook/register and the Prompt 14B completion report.
2. Reconciled the live repository against the Project X (113) baseline in the assignment.
3. Independently recounted the B-05 parameter inventory, verified the 41 F-CI identifiers and classified them by actual purpose (30 executable, 4 analytical, 7 governance).
4. Audited every B-05 numerical parameter's identity, value, unit, source, formula dependency, precision, rounding, timing, decision authority, numerical status, validator, evidence requirement, dependencies and owner-reserved flag.
5. Calculated the city-development lifecycle: founding costs 2–12, the national-infrastructure gate, the stepped infrastructure curve, capacity/housing efficiency and six investment strategies.
6. Examined all 17 building types and the seven extraction, four processing and three generator classes, including construction, materials, capacity, upkeep, book value, demolition, utilisation and payback.
7. Analysed eight industrial strategies, the 0/25/50/75/100% utilisation sweep, the mandatory steel-margin investigation and the demand-side conditions under which each chain fails.
8. Evaluated all 12 technologies, five branches, four national programmes, seven research-rate scenarios and the research-payback framework.
9. Built and executed a deterministic B-05/B-04 reference model over 24 scenarios at 10, 30, 60 and 120 turns, including eight failure or low-return scenarios and two two-strategy comparisons.
10. Produced 12 new integrated worked examples (E1–E12), the 39-row cross-system consistency matrix, the separate contradiction and limitation register, the B-14 reconciliation and the validation record.
11. Made only documentation and metadata corrections inside B-05/B-14 authority; **no B-04-owned recipe, price, maintenance rate or tax value was changed**. Two B-04 cross-document contradictions were found and handed off, not edited.
12. Ran the existing and new validators and recorded the actual results in §14.

### 1.2 Repository baseline reconciliation

| Check | Project X (113) baseline | Live repository | Result |
|---|---|---|---|
| Branch / HEAD at start | not stated | `main` / `3b9cadc` | reconciled |
| Working tree at start | — | clean, 0 modified, 0 untracked, 0 staged | preserved |
| B-05 formula identifiers | 41 active | 41 active (`F-CI-001`…`F-CI-041`) | matches |
| B-05 parameter records | 73 in §7 | 73 rows, 1:1 to the register §3 tables | matches |
| Building catalogue | 17 types | 17 (7 extraction, 4 processing, 3 generators, 3 support) | matches |
| Technology tree | 12 technologies / 5 branches | 12 / 5; 448 RP and 3,180 crowns | matches |
| National programmes | 4 | 4 | matches |
| Existing B-05 examples | 20 | 20 | matches |
| Existing T05 specifications | 64 | 64 (A6, B6, C8, D8, E8, F8, G6, H6, I4, J4) | matches |
| B-04 formula/parameter records | 47 / 49 | 47 / 49 | matches |
| B-14 active formula total | 295 | 295 | matches |
| B-14 parameter total | 393 | 393 | matches |
| City / economy validators | 267/267 and 170/170 | 267/267 and 170/170 (actual run, §14) | reproduced |

No legitimate newer B-05 change was found. The working tree was clean before this phase.

### 1.3 Source inventory

| Item | Count | Evidence |
|---|---:|---|
| Active B-05 formulas | **41** | Register §4.1–§4.4 (001–030), §5 (031–034), §7–§8 (035–041) |
| Executable B-05 formulas | **30** | `F-CI-001`…`F-CI-030` |
| Analytical B-05 definitions | **4** | `F-CI-031`…`F-CI-034` |
| Governance B-05 records | **7** | `F-CI-035`…`F-CI-041` |
| B-05 parameter records | **73** | [parameter inventory §7](22_numerical_parameter_inventory.md) |
| Formula/rule-embedded parameter groups | **6** | Annex A, §3.4 (not inventory records; see §3.4) |
| Building catalogue | **17** | Register §3.3 |
| Technologies / branches / programmes | **12 / 5 / 4** | Register §3.5–§3.6 |
| Worked examples (existing + new) | **20 + 12** | B-05 §20; this report §9 |
| T05 test specifications | **64** | B-05 §24; executed: **0** |
| Cross-system matrix rows | **39** | This report §11 |
| Contradiction-register entries | **2** | This report §12 (separate from the matrix) |

### 1.4 Governance and decisions

[D-014](../AUTONOMOUS_DECISION_POLICY.md) was read in full and not modified. Three Category-B decision pairs are recorded: **D-244 / DD-290** (B-05 formula classification and numerical status), **D-245 / DD-291** (parameter recount and the embedded-parameter convention) and **D-246 / DD-292** (14C economic findings and the reference model, without retuning). No owner-reserved decision was resolved. No Category A constraint changed. The Prompt 14A and Prompt 14B accepted decisions were not reopened; the B-04 formula register and rulebook were not edited.

### 1.5 Required deliverables map

| Deliverable | Where |
|---|---|
| A. Complete B-05 numerical master analysis | §2 |
| B. Complete B-05 parameter reconciliation | §3 |
| C. City development balance report | §4 |
| D. Infrastructure and building economics report | §4, §5 |
| E. Industrial profitability report | §6 |
| F. Population and housing dependency report | §7 |
| G. Research progression report | §8 |
| H. Integrated worked examples | §9 (E1–E12) |
| I. Economic simulation report | §10 |
| J. Cross-system consistency matrix | §11 |
| K. Contradiction and limitation register | §12 |
| L. B-14 inventory and baseline reconciliation | §13 |
| M. Prompt 14C completion report | This document; archived instruction in `docs/prompts/` |

---

## 2. B-05 formula reconciliation — all 41 identifiers

### 2.1 Counting and classification

The register defines exactly **41 active identifiers**. The assignment's warning is correct: they are not 41 executable runtime calculations.

| Class | IDs | Count | Purpose |
|---|---|---:|---|
| Executable calculation | `F-CI-001`…`F-CI-030` | **30** | City, capacity, housing, construction, production, accounting, research, upkeep and availability formulas with inputs, output, units, rounding and timing |
| Analytical assessment | `F-CI-031`…`F-CI-034` | **4** | The reference cost/margin table, its interpretation, the known provisional skew and the simplified research-payback framework |
| Change-control and validation | `F-CI-035`…`F-CI-041` | **7** | Constant change, formula change, new formula, B-04 precedence, revision history, validation record and non-validation statement |

No identifier was added, retired, renumbered or redefined. The global B-14 formula total stays **295**.

### 2.2 The 41-identifier assessment

Legend: **E** = executable, **A** = analytical, **G** = governance. Every entry's canonical source is [the B-05 register](11_city_infrastructure_production_and_research_formula_register.md); its identifier, name and source section were verified against [the master inventory §4.2](22_formula_master_inventory.md). All values remain `PROVISIONAL VALUE`; analytical/governance records keep `UNSPECIFIED` where they carry no value.

| ID | Name | Type | Expression / rule (verified) | Inputs → output (units) | Rounding · timing | Dependencies | Assessment |
|---|---|:-:|---|---|---|---|---|
| F-CI-001 | Development capacity | E | `10 + floor(I/10)` | Infrastructure (levels 10–500) → DC | floor · derived; submission and P4.1 | B-04 capacity vector; URB-041; D-070 | Correct; reproduces 15/11/60. Retained |
| F-CI-002 | City housing | E | `45,000 + 100×I + 25,000×civic` | I, civic (0–3) → people | none · derived; P3.8 | URB-042; D-079; B-06 DMP-037 | Correct; 46k–170k. Retained |
| F-CI-003 | National infrastructure | E | `Σ cities I` | Per-city I → levels | none · founding submission | F-CI-001; URB-032 | Correct. Retained |
| F-CI-004 | Infrastructure unit cost | E | `8 + floor(I/10)` | I → crowns/level | floor · submission | URB-043; D-069 | Correct; 9–58. Retained |
| F-CI-005 | Infrastructure order cost | E | `ceil(Σ (8+floor(j/10)) × (10,000−bp)/10,000)` | I, n, discount_bp → crowns | unit prices floored; sum exact; discount once, ceiled · P4.1c capex | F-CI-004; Civil Survey; URB-044 | Correct; 10→500 = 16,170; 50→500 = 15,750; capped 12,936. Retained |
| F-CI-006 | City cost | E | `400 + 150k²` + 20 steel | k (2–12) → crowns + steel | none · P4.1a capex | URB-032/033 | Correct; 1,000–22,000. Retained |
| F-CI-007 | Founding threshold | E | `k ≤ 12 ∧ ΣI ≥ 100(k−1)` | k, F-CI-003 → boolean | none · submission | F-CI-003 | Correct; 12th at 1,100. Retained |
| F-CI-008 | Used capacity | E | `Σ dc(class)` | Facility list → DC | none · derived | URB-048 | Correct; standard 11. Retained |
| F-CI-009 | Capacity cost of a class | E | 1/2/2/1/3/2 | Class → DC | none · construction | URB-048 | Correct. Retained |
| F-CI-010 | Free capacity | E | `capacity − used` | F-CI-001/008 → DC | none · submission and P4.1 | URB-050/051 | Correct; 4 at start. Retained |
| F-CI-011 | Construction crown cost | E | `ceil(crown_base × (10,000−bp)/10,000)` | Building, discount → crowns | ceil · P4.1c capex | Civil Methods; URB-072 | Correct; facilities/warehouse only. Retained |
| F-CI-012 | Construction book value | E | `cost + Σ qty×reference_price` | Cost, materials → crowns | none · P4.1 | B-04 D-058; ECN-098/108 | Correct; farm 155. Retained |
| F-CI-013 | Warehouse expansion cost | E | `180 + 40n` + 5 steel | n (0–71) → crowns | none · P4.1c | URB-058; ECN-122 | Correct; 180–3,020. Retained |
| F-CI-014 | National warehouse capacity | E | `2,000 + 250×exp + 500×granary` | Counts → units | none · next turn | ECN-120/121; URB-058/107 | Correct; 2,000–20,500. Retained |
| F-CI-015 | Extraction output | E | `batches_run × (Y + bonus)` | Batches, B-04 Y, bonus → units | none · P3.3 | B-04 F-EC-004/005; F-CI-023 | Correct; B-04 owns Y/V/M. Retained |
| F-CI-016 | Processing output | E | `batches_run × (Y + bonus)` | Batches, B-04 Y, bonus → units | none · P3.5 | B-04 F-EC-006…012 | Correct; recipes unchanged. Retained |
| F-CI-017 | Processing maintenance | E | `batches × max(1, 2−standards)` | Capacity, bonus → crowns/turn | none · P3.2 | B-04 ECN-051/147a; D-241 | Correct; floor 1. Retained |
| F-CI-018 | Demolition refund | E | `floor(crown_cost_paid × 2,500/10,000)` | Paid crowns → crowns | floor · P4.1b | URB-071/121 | Correct; 0–300. Retained |
| F-CI-019 | Fixed-asset book value | E | `Σ infrastructure_carrying + Σ other book_value` | Lots, facilities → crowns | none · after P4.1/P5 | URB-118a/b; B-04 ECN-108; B-10 F-WR-038 | Correct in B-05; **B-04 register F-EC-026 conflicts — C-14C-02** |
| F-CI-020 | Research rate | E | `research_institutes` | Standing labs (0–24) → RP/turn | none · P4.2 | URB-059/095 | Correct; idle lab 0. Retained |
| F-CI-021 | Research progress | E | `need=max(0,cost−progress); applied=min(rate,need); pool+=rate−applied; available=pool−reserved` | Project, rate, pool → RP | none · P4.2 | F-CI-020 | Correct; points assigned once; pooled separately. Retained |
| F-CI-022 | Research completion | E | `progress ≥ cost` | F-CI-021 → boolean | none · P4.2; effect next turn | URB-096/099 | Correct. Retained |
| F-CI-023 | Modifier total and cap | E | `min(cap, Σ bonuses)` | Completed sources → units/batch | none · read at production | URB-100 | Correct; food 3, others 1. Retained |
| F-CI-024 | Programme availability | E | `branch complete ∧ ¬held ∧ rp_available ≥ cost` | Programme, pool → boolean | none · submission | URB-107/108; F-CI-021 | Correct; banked RP only. Retained |
| F-CI-025 | Upkeep | E | `2×labs + 1×civics` | Standing support → crowns/turn | none · P3.7 | URB-120 | Correct; 0–84. Retained |
| F-CI-026 | National wealth | E | `treasury + Σ inventory×price + fixed assets` | B-04 stocks, F-CI-019 → crowns | none · P3.8/report | B-04 ECN-108 | Correct. Retained |
| F-CI-027 | Per-city limit check | E | `count+1 ≤ limit` | Facility count → boolean | none · submission/P4.1 | URB-049 | Correct; 8/4/6/6/2/3. Retained |
| F-CI-028 | Construction slot availability | E | `no accepted construction action for (city,turn)` | Actions → boolean | none · submission | URB-064 | Correct. Retained |
| F-CI-029 | Capacity check at resolution | E | `used + dc ≤ capacity` | F-CI-001/008/009 → boolean | none · P4.1c | URB-050 | Correct; defence in depth. Retained |
| F-CI-030 | City-count check | E | `cities < 12` | Count → boolean | none · submission | URB-031 | Correct. Retained |
| F-CI-031 | Cost per DC and base margin | A | Table of DC, crowns/DC, base margin, margin/DC | Facility → analysis | n/a | B-04 F-EC-036; F-CI-032/033 | Correct at reference prices; **omits capex payback and upkeep by design** (F-CI-032 says so). No value change |
| F-CI-032 | What the table says | A | Interpretation of F-CI-031 | n/a → analysis | n/a | F-CI-031 | Correct; steel/aluminum 7.0 margin/DC, refinery 3.0. Retained |
| F-CI-033 | The known provisional skew | A | Steel-dominance caveat and demand-side remedy | n/a → analysis | n/a | F-CI-031; D-046 | Correct; 14C confirms the caveat and adds the demand evidence (§6.7). Retained |
| F-CI-034 | Research payback | A | `crowns / (bonus × batches × margin per unit)`, RP ignored | Tech, batches → turns | n/a | URB-131 | **Arithmetically correct but incomplete**: omits RP, lab capex/upkeep and alternative-capex basis. 14C publishes an extended framework (§8.7) **without changing the formula** |
| F-CI-035 | Changing a constant | G | Register revision with reason, affected examples/requirements, re-run | n/a | n/a | F-CI-000e | Correct; 14C changed no constant |
| F-CI-036 | Changing a formula | G | B-05 revision + decision; examples/index/checker updated | n/a | n/a | D-014 | Correct; no structure change made |
| F-CI-037 | Adding a formula | G | Next free ID; never reuse/renumber/delete | n/a | n/a | — | Correct; no formula added |
| F-CI-038 | B-04 precedence | G | B-04 wins on shared quantities | n/a | n/a | B-04 | Correct; 14C honoured it |
| F-CI-039 | Revision history | G | Dated revision log | n/a | n/a | — | Preserved |
| F-CI-040 | Validation record | G | Dated command results | n/a | n/a | — | Preserved; 14C results appended to the QA report, not rewritten here |
| F-CI-041 | What is not validated | G | Honest non-validation statement | n/a | n/a | — | Preserved and extended by this report §15 |

### 2.3 Findings of the formula assessment

1. **The executable set is complete and internally consistent.** Every formula has an expression, inputs, output, units, rounding, timing, dependencies, rationale, edge cases, validation reference and requirement. The arithmetic is recomputed by `verify_city_numbers.py` (267/267) and by this phase's verifier.
2. **The analytical entries are correctly classified.** `F-CI-031`…`F-CI-034` are definitions and interpretations, not runtime calculations; their recorded metadata gaps in the B-14 master inventory are expected, not omissions.
3. **The governance entries are change-control records.** `F-CI-035`…`F-CI-041` carry no numerical values; treating them as executable would be wrong.
4. **One genuine completeness gap was identified in `F-CI-034`.** The simplified payback ignores the RP cost, institute capex and upkeep, and it uses a "margin per unit" that can be read as price rather than contribution. 14C does **not** change the formula (a structure change would require a B-05 revision under F-CI-036); it publishes the extended analytical framework in §8.7 and records the limitation (L-14C-03). The formula remains valid for the narrow question it asks.
5. **No formula value was changed.** Every number remains `PROVISIONAL VALUE`. Passing arithmetic is not calibration, simulation is not balance and no player has played the build.

---

## 3. B-05 parameter reconciliation

### 3.1 Independent recount and source verification

The live inventory's B-05 section (§7) contains **exactly 73 records**. They were recounted line by line and mapped to the B-05 register's constant tables §3.1–§3.7:

| Register source | Rows | Inventory records | Match |
|---|---:|---:|---|
| §3.1 City and infrastructure constants | 17 | 17 | 1:1 |
| §3.2 Building capacity costs and limits | 6 | 6 | 1:1 |
| §3.3 Building catalogue | 17 | 17 | 1:1 |
| §3.4 Standard capital grant | 9 | 9 | 1:1 |
| §3.5 Research tree (12 technologies + total) | 13 | 13 | 1:1 |
| §3.6 National programmes | 4 | 4 | 1:1 |
| §3.7 Upkeep and research | 7 | 7 | 1:1 |
| **Total** | **73** | **73** | **73/73** |

The count is reproducible from the files, not asserted: 73 inventory rows starting `| None |`, 73 source rows across the seven constant tables, and no orphan on either side. No duplicate parameter name, no missing record and no extra record was found (the verifier's `14C-02` check compares the name sets both ways).

### 3.2 Metadata validation

Every record was inspected against the required fields. The inventory supplies, for all 73 B-05 records: parameter identity (source name; `None` ID under the established convention), current value, unit (or the explicit `Not specified`/grouped-vector form), exact source (`B-05 §3.x`), formula dependency (`Used by`), precision (integer/basis-point convention), timing (per source table), decision authority (`Prompt 14 calibration; B-05 structure owner`), numerical status (`PROVISIONAL VALUE`), validator (`verify_city_numbers.py`), evidence requirement, dependencies and owner-reserved (`No`). No field is missing for a B-05 record; the vector rows state each value with its own unit inside the cell (e.g. `Y=20; V=12; M=1; P=1`).

**Decision authority.** The 73 values are **Category C** in D-014 terms: safe provisional defaults with a named evidence path. The *structure* is Category B and was confirmed by D-066…D-080 (and, for the standard bundle, D-063). None is owner-reserved. **No record was promoted to `OWNER-APPROVED VALUE`.** Passing arithmetic does not approve a value.

### 3.3 Reconciliation result

| Measure | Result |
|---|---:|
| Records discovered | **73** |
| Records verified against their source | **73** |
| Records missing from the inventory (within its stated constant-table coverage) | **0** |
| Duplicate records | **0** |
| Incorrect ownership | **0** |
| Incorrect numerical status | **0** |
| Missing required metadata | **0** |
| Records changed | **0** |
| Records retained unchanged | **73** |
| Formula/rule-embedded parameter groups outside constant-table coverage | **6** (Annex A; not records) |
| Global B-14 parameter record total | **393 (unchanged)** |

**Why the six embedded groups are not new records.** The B-14 inventory's stated B-05 coverage is "every constant-table row in B-05 §3". The six groups in Annex A are values chosen inside formula entries or rule paragraphs, not rows of §3. The same convention applies to B-04…B-07 (formula-embedded values are covered only for B-08…B-11). Promoting the six groups to records would change the cross-system counting convention for one system only; the coherent choice is to record them completely in the annex, keep the inventory method stable and leave promotion to a future cross-system convention decision. **Nothing is omitted from the analysis**: every value, source and formula is stated in Annex A.

### 3.4 Annex A — formula/rule-embedded B-05 parameters (6 groups)

| Parameter | Value | Unit | Source | Used by | Status | Why not a §7 record |
|---|---|---|---|---|---|---|
| Infrastructure unit-cost base | **8** | crowns/level | F-CI-004 expression; URB-043 | F-CI-004, F-CI-005 | PROVISIONAL VALUE | Formula intercept, not a §3 table row |
| Yield-bonus cap | **3 food; 1 other raw; 1 manufactured** | units/batch | URB-100; F-CI-023 | F-CI-015/016/023 | PROVISIONAL VALUE | Rule-table cap inside the formula entry |
| Variable-cost floor | **2** | crowns/batch | URB-100; prg_survey effect | F-EC-005; F-CI-023; prg_survey | PROVISIONAL VALUE | Floor rule inside the modifier class |
| Maintenance floor | **1** | crown/batch | URB-100; F-CI-017; prg_standards | F-CI-017; F-EC-014 | PROVISIONAL VALUE | Floor rule inside the modifier class |
| Per-turn action slots | **1 founding + 1 programme per nation; 1 construction per city** | actions/turn | URB-064; F-CI-028 | F-CI-028; URB-067 | PROVISIONAL VALUE | Rule constants, not §3 table rows |
| City-name bounds and rename cooldown | **3–24 characters; 24 hours** | characters; hours | URB-030 | City naming; audit; UI | PROVISIONAL VALUE | Cosmetic/security bound, not an economic §3 row |

**Ownership observations.** (1) The national warehouse base (**2,000**) appears in both B-04 §3.1 and B-05 §3.7; B-04 is authoritative for the warehouse (ECN-120/121) and B-05 restates it to keep F-CI-014 self-contained. (2) The B-05 §3.4 "Facilities" and "Capacity vector" rows restate the D-063 starting bundle that B-04 also records; B-04 owns the economic identity of the bundle, B-05 owns the city-side derivation (capacity 15, used 11, free 4, housing 50,000, book 0). (3) B-04 owns every recipe, output per batch, variable cost, maintenance rate and reference price; B-05 consumes them through F-CI-015/016/017 and never restates them as its own. (4) B-06 owns population growth, tax policy, stability and the service-cost share; B-05 supplies only housing and the civic count. (5) B-10 owns military consumption and the `OP-05` damage quantities; B-05 owns the city state and the recalculation.

---

## 4. City development economics

### 4.1 City founding, cities 2–12

Using F-CI-006 (`400 + 150k²` + 20 steel) and F-CI-007 (`ΣI ≥ 100(k−1)`):

| k | Crown cost | Steel | Book value | Gate ΣI | Marginal DC added* | Crowns per added DC |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1,000 | 20 | 1,140 | 100 | 16 | 109 |
| 3 | 1,750 | 20 | 1,890 | 200 | 11 | 159 + gate |
| 4 | 2,800 | 20 | 2,940 | 300 | 11 | 255 + gate |
| 5 | 4,150 | 20 | 4,290 | 400 | 11 | 377 + gate |
| 6 | 5,800 | 20 | 5,940 | 500 | 11 | 527 + gate |
| 7 | 7,750 | 20 | 7,890 | 600 | 11 | 705 + gate |
| 8 | 10,000 | 20 | 10,140 | 700 | 11 | 909 + gate |
| 9 | 12,550 | 20 | 12,690 | 800 | 11 | 1,141 + gate |
| 10 | 15,400 | 20 | 15,540 | 900 | 11 | 1,400 + gate |
| 11 | 18,550 | 20 | 18,690 | 1,000 | 11 | 1,686 + gate |
| 12 | 22,000 | 20 | 22,140 | 1,100 | 11 | 2,000 + gate |
| **Total 2–12** | **101,750** | **220** | **103,290** | — | **121** | — |

\*The k=2 row counts the capital's 5 new DC from the 100-level gate plus the new city's 11 DC. Later rows count only the new city's 11 DC because the gate is shared with earlier development.

**The gate binds long before the crown cost.** At 12 cities the nation needs 1,100 national infrastructure. Twelve cities at their 10-level minimum supply only 120, so **980 additional levels** are required across the cities. The cheapest distribution (equalising the rising marginal price) costs **12,340 crowns** — more than the 101,750 crowns of founding fees are for all cities? No: it is a separate **12,340-crown** infrastructure investment on top of the 101,750, and it is what actually limits expansion. A capital alone cannot reach the 12th-city gate (500 maximum < 1,000 needed with eleven 10-level cities); the player must develop every city, not just the capital. This is the intended "expansion follows development" rule, and it means the 12-city limit is reached by broad development, not by hoarding crowns.

**A new city is an empty shell.** It enters at infrastructure 10, 11 DC, 46,000 housing and no facilities, with book value 1,140 (1,000 crowns + 20 steel at 7). It adds a **second construction slot** (one build per city per turn) and a **second set of per-city limits** — its main strategic value. The 20-steel material cost is a real gate: the standard start holds exactly 20 steel, so founding the second city consumes the entire construction-material stock. Without a steel source, no farm, lab or mine can follow. A city founded on turn 15 with no steel left is a housing and construction-slot purchase, not a production purchase.

### 4.2 Infrastructure investment

`infrastructure_cost(I,n) = Σ_{j=I}^{I+n−1} (8 + floor(j/10))`, discount applied once (F-CI-005). The stepped marginal price is the design: each level pays its own decade price, so splitting an order changes nothing.

| Range | Levels | Crowns (no discount) | Crowns per DC (1 DC / 10 levels) | Crowns per 1,000 housing |
|---|---:|---:|---:|---:|
| 10 → 20 | 10 | **90** | 90 | 90 |
| 20 → 50 | 30 | **330** | 110 | 110 |
| 50 → 100 | 50 | **750** | 150 | 150 |
| 100 → 200 | 100 | **2,250** | 225 | 225 |
| 200 → 500 | 300 | **12,750** | 425 | 425 |
| 10 → 500 (max legal) | 490 | **16,170** | 330 (60 DC) | 330 |
| 50 → 500 (capital max) | 450 | **15,750** | 350 (45 DC) | 350 |
| 50 → 500 with Civil Survey | 450 | **14,175** | 315 | 315 |
| 10 → 500 at the 2,000 bp cap | 490 | **12,936** | 264 | 264 |

**Efficiency findings.**
1. **Cost per DC rises 4.75×** from 90 (10→20) to 425 (200→500, per decade average), but the absolute step is linear in the level, not exponential. Late infrastructure is expensive, not impossible.
2. **Infrastructure's housing is a side-effect, not its purpose.** At 50→100 the player pays 150 crowns per 1,000 housing; a civic centre provides 25,000 housing for 300 crowns + 10 steel — **12 crowns per 1,000** (plus 2 DC and 1 upkeep). Infrastructure is the **only scalable DC source**; civic centres are the **housing tool**. The two do not compete for the same purpose.
3. **The first 5 DC are cheap.** 50→100 costs 750 for 5 DC + 5,000 housing; founding a second city adds 11 DC for 1,000 crowns + the 100-national-infrastructure gate (750). Founding is cheaper per DC at k=2 (109 vs 150), but after k=3 the gate investment dominates and city count is justified by **construction slots and limits**, not by DC price.
4. **Infrastructure cannot be sold** (URB-045): a mistake is permanent opportunity cost. The only reduction is bounded `OP-05` damage and repair, which is expensive and does not refund.
5. **The 500 cap and 12-city bound interact**: a maxed nation has 720 DC (12×60) but a single city's facility limits demand 70 DC, so 60 is never enough for a fully maxed catalogue in one city; the limit is reached only by spreading chains across cities — the intended specialisation tension.

### 4.3 Strategy comparison A–F

| Strategy | Capital and time | What it buys | Advantage | Disadvantage | Verdict |
|---|---|---|---|---|---|
| **A. Upgrade the capital** | 750 for 50→100; 15,750 to 500 | 5–45 DC, 5,000–45,000 housing | Cheapest early DC; no steel; one city's limits | Diminishing DC per crown; no new construction slot; housing expensive vs civic | Best **early** (first 5–10 DC); poor after ~200 |
| **B. Found a second city and develop it** | 1,000 + 20 steel + 420 to 50 infra; gate 100 national infra | 11→15 DC, 46,000–51,000 housing, a second construction slot and limit set | Cheapest DC at k=2; parallel builds; more labs/civics | Consumes the 20-steel stock; the gate requires 100 national infrastructure; no facilities by itself | **Best tempo** purchase if steel is secured |
| **C. Develop existing cities for production** | Facility capex (120–1,200) + DC | Output, not capacity | Direct return; farms +7/turn; steel +14 base | DC must exist first; power/inputs/maintenance | The **only** strategy that earns cash |
| **D. Build facilities without infrastructure** | Facility capex only | Uses free 4 DC at start | Fast | Stops at 4 DC; a 2-DC refinery plus a 1-DC farm fits, the rest does not | A **trap** after the first 2–3 facilities |
| **E. Housing and civic centres** | 300 + 10 steel per civic | 25,000 housing, 2 DC, 1 upkeep | 12 crowns per 1,000 housing; converts tax base into growth | Slow growth (0.5–0.65%/turn); needs food; uses DC | **Strongest long-run** investment once food is secure |
| **F. Expand towards the city limit** | 101,750 + 220 steel + 12,340 gate infrastructure | 12 construction slots, 12 limit sets, 720 DC at cap | Maximum specialisation and tempo | Enormous cost; each marginal city is worth less; the gate forces broad development | A **late-game** choice, not an early goal |

**Conclusion.** Maximum infrastructure and maximum city count are not automatically optimal. The cheap early wins are (1) secure food, (2) add 5–10 DC to the capital for the first facilities, (3) build civic housing once food allows, and (4) found the second city when 20 steel can be spared. The expensive late wins are the 200→500 infrastructure curve and cities 7–12; they buy tempo and limits, not cash efficiency.

---

## 5. Buildings, construction and maintenance economics

### 5.1 The 17-type economics table

Book value = crown cost + materials at reference prices (F-CI-012). Margin is the B-04 base margin at reference prices before power (F-EC-036/F-CI-031); the loaded figure subtracts power at 3.00 crowns/GU (marginal coal). Payback is book value ÷ base margin at full utilisation, before power. "Utilisation risk" names the condition that destroys the return.

| Building | DC | Crowns | Materials | Book | Contribution/batch | Base margin/turn* | Payback (base) | Recurring cost | Utilisation risk |
|---|---:|---:|---|---:|---|---:|---:|---|---|
| Farm | 1 | 120 | 5 steel | 155 | 20 food | +7 | 22.1 | 1 maintenance | Food demand cap; warehouse full |
| Coal mine | 1 | 160 | 5 steel | 195 | 10 coal | −1 | never | 1 | Only valuable as fuel/steel input |
| Oil well | 1 | 220 | 5 steel | 255 | 8 oil | +1 | 255 | 1 | Feeds refining; 8 < 10 per refinery batch |
| Iron mine | 1 | 180 | 5 steel | 215 | 10 iron | −1 | never | 1 | Only valuable inside steel |
| Bauxite mine | 1 | 220 | 5 steel | 255 | 8 bauxite | +1 | 255 | 1 | Feeds smelters only |
| Lead mine | 1 | 260 | 5 steel | 295 | 6 lead | +1 | 295 | 1 | Feeds ammunition only |
| Uranium mine | 1 | 600 | 10 steel, 5 aluminum | 710 | 1 uranium | +1 | 710 | 1 | Nuclear fuel only; tech-gated |
| Refinery | 2 | 320 | 15 steel | 425 | 8 gasoline | +6 | 70.8 (0 loaded) | 2 | Oil input; power; zero loaded margin |
| Steel mill | 2 | 380 | 15 steel | 485 | 8 steel | +14 | 34.6 (+5 loaded → 97) | 2 | Iron + coal + 3 GU + a buyer |
| Aluminum smelter | 2 | 420 | 20 steel | 560 | 8 aluminum | +14 | 40 (+2 loaded → 280) | 2 | 12 bauxite + 4 GU + tech |
| Ammunition plant | 2 | 360 | 15 steel | 465 | 10 ammunition | +10 | 46.5 (+4 loaded → 116) | 2 | Military demand; tech-gated |
| Coal plant | 2 | 280 | 10 steel | 350 | 6 GU | — | via enabled batches | 2 | Fuel; surplus GU discarded |
| Oil plant | 2 | 340 | 10 steel, 5 aluminum | 450 | 6 GU | — | via enabled batches | 2 | 4.33/GU book; oil opportunity cost |
| Nuclear plant | 2 | 1,200 | 30 steel, 20 aluminum | 1,570 | 20 GU | — | via enabled batches | 2 | Uranium + lead; tech-gated |
| Warehouse (+250) | 1 | 180+40n | 5 steel | 215 (first) | 250 units | — | strategic | 0 | Fills; expansion cost rises |
| Research institute | 3 | 500 | 20 steel | 640 | 1 RP | — | via research | 2 upkeep | No project; unpaid → idle |
| Civic centre | 2 | 300 | 10 steel | 370 | 25,000 housing | — | via tax base | 1 upkeep | Unpaid → housing excluded |

\*One batch for extraction/processing; a generator's "margin" is not revenue — it enables processing output.

**Classification.** (1) **Cash-positive at reference:** farm, oil/bauxite/lead/uranium mines (thin), the four processing chains (loaded margins 0 to +5), and food. (2) **Strategic losses:** coal and iron mines lose 1 crown per batch at reference; their value is realised inside steel. (3) **Enablers with no direct margin:** generators, warehouse, lab, civic. (4) **Payback is long everywhere**: the best base payback is 22 turns (farm); the best processing payback is 35 turns (steel mill); most are 40–300. A processing plant is a long-horizon asset, not an early cash machine.

### 5.2 Construction, demolition and accounting separation

- **Initial construction expenditure** = crown cost (F-CI-011) at P4.1; **material expenditure** = inventory units at reference book value, never cash unless bought.
- **Recurring upkeep** = the B-04 capacity maintenance (1/2/2 per batch/level) plus the lab/civic P3.7 upkeep (2/1). These are separate from capex and are never capitalised.
- **Variable production expenditure** = per-batch cost paid only if the batch runs; it is neither capex nor maintenance.
- **Power expenditure** = generator fuel (book value) + generator variable + generator maintenance; it is incurred whether or not the delivered GU is used, and the marginal cost per GU (3.00 for coal) differs from the actual cost at low utilisation (9.00 at 2/6 at the standard start).
- **Asset book value** = crown + materials at reference (F-CI-012); infrastructure separately at carrying value (F-CI-019/URB-118a).
- **Demolition refund** = 25% of crowns paid, materials never returned, full book value removed, the difference impaired (F-CI-018/URB-121). Granted facilities refund 0. Cycling is always a loss: build 120 + demolish 30 + rebuild 120 = 210 for the same farm.
- **Realised market revenue** is a B-07 event, not book value; an unsold manufactured good is inventory book value, not cash.

**Underutilisation.** Because maintenance is paid on **capacity** whether or not a batch runs, an idle facility bleeds its maintenance every turn; a partially derated chain wastes the unrun batches' maintenance but not their variable cost. The 0% case is the worst: full maintenance, zero output. This is the economic reason not to hold idle capacity forever and the reason the "excessive facilities" and "underused refining" scenarios fail (§10).

---

## 6. Industrial profitability

### 6.1 Seven extraction chains

| Chain | Y | V | M | Price | Output value | Full cost | Base margin | Payback on book | Role |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Food | 20 | 12 | 1 | 1 | 20 | 13 | **+7** | 22.1 | Survival; food demand caps it |
| Coal | 10 | 10 | 1 | 1 | 10 | 11 | **−1** | never | Fuel and steel input |
| Oil | 8 | 14 | 1 | 2 | 16 | 15 | **+1** | 255 | Refinery input; 8 < 10 per batch |
| Iron | 10 | 10 | 1 | 1 | 10 | 11 | **−1** | never | Steel input |
| Bauxite | 8 | 14 | 1 | 2 | 16 | 15 | **+1** | 255 | Aluminum input |
| Lead | 6 | 16 | 1 | 3 | 18 | 17 | **+1** | 295 | Ammunition/nuclear input |
| Uranium | 1 | 28 | 1 | 30 | 30 | 29 | **+1** | 710 | Nuclear fuel only |

Extraction is not a cash business except food. Coal and iron are deliberately negative: a player who sells raw coal or iron at reference destroys value relative to converting it into steel. Food is the strongest extraction chain because it is the survival good, but its demand is population-capped and its storage finite.

### 6.2 Four processing chains

| Chain | Inputs | Output | Input book | Output book | V | M | GU | **Base margin** | **Loaded at 3/GU** | Capital (book) | Loaded payback |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Refining | 10 oil | 8 gasoline | 20 | 48 | 20 | 2 | 2 | **+6** | **0** | 425 | never |
| Steel | 10 iron + 6 coal | 8 steel | 16 | 56 | 24 | 2 | 3 | **+14** | **+5** | 485 | 97 |
| Aluminum | 12 bauxite | 8 aluminum | 24 | 64 | 24 | 2 | 4 | **+14** | **+2** | 560 | 280 |
| Ammunition | 8 lead + 4 coal | 10 ammunition | 28 | 60 | 20 | 2 | 2 | **+10** | **+4** | 465 | 116 |

The margins match B-04 F-EC-036 exactly; no recipe or price was changed. Refining's zero loaded margin is the single most important industrial fact: its value is the gasoline market and military demand, not a reference-price spread. Steel and aluminum tie on base margin; steel has the lower capital, lower power draw and a two-input chain, while aluminum has a single input and a higher-value output.

### 6.3 Three generator classes

| Class | GU/level | Fuel/level | Variable | Maintenance | Full cost/level | Cost/GU | Actual cost at the standard start* |
|---|---:|---|---:|---:|---:|---:|---:|
| Coal | 6 | 6 coal (book 6) | 10 | 2 | 18 | **3.00** | 9.00 (2 of 6 GU used) |
| Oil | 6 | 5 oil (book 10) | 14 | 2 | 26 | **4.33** | 13.00 (2 of 6 used; plus refining opportunity) |
| Nuclear | 20 | 1 uranium + 1 lead (book 33) | 40 | 2 | 75 | **3.75** | 18.75 (4 of 20 used) |

\*Actual cost is the whole running level's cost divided by the GU actually consumed; surplus GU is discarded. The same generator costs 3.00/GU marginal but 9.00/GU actual at the standard start's 2/6 utilisation. Nuclear is the costliest per GU but delivers 3.33× the GU per DC (20 GU per 2 DC vs 6 per 2 DC), so its value is **power DC compression**, not cheap energy. Uranium's only sink is nuclear fuel; `tech_ext_deep` (+1 uranium per batch) halves the mining needed for a given nuclear fleet, which is why URB-133's question 4 is real but conditional on a nuclear build.

### 6.4 Eight development strategies

Cash figures are per turn at reference prices, fully loaded with self-supplied inputs and dedicated power; capex is crowns plus material book value. "Demand" names the buyer assumption that must hold.

| Strategy | Package | Capex (book) | DC | Output | Cash margin | Payback (book) | Demand | Verdict |
|---|---|---:|---:|---|---:|---:|---|---|
| 1. Food and essentials | 4 farms | 620 | 4 | 80 food | **+28** | 22 | Population growth; food sales | **Best early return**; capped by growth/storage |
| 2. Raw extraction | coal/iron mines | 195/215 each | 1 each | 10 units | −1 each | never | Internal only | **Strategic loss leader**; never a cash strategy |
| 3. Steel | 4 mills + 4 iron + 4 coal + 2 plants | 4,280 | 20 | 32 steel + 4 coal | **+12** (+40 with ind_heat) | 357 (107 tech) | Construction, warfare, market ≥7 | **Strongest first manufacturing build** |
| 4. Aluminum | 4 smelters + 6 bauxite + 4 coal + 3 plants | 5,530 | 28 | 32 aluminum + 22 coal | **+4** (+36 with ind_chem) | 1,383 (154 tech) | Market ≥8, warfare, advanced construction | **Viable second industrial chain; capital-hungry** |
| 5. Refining and gasoline | 4 refineries + 5 wells + 2 coal + 2 plants | 4,065 | 20 | 32 gasoline + 8 coal | **−9** | never | Gasoline ≥6 with a buyer; military fuel | **Weakest chain; volume/market play only** |
| 6. Ammunition | 4 plants + 6 lead + 3 coal + 2 plants | 4,915 | 21 | 40 ammunition + 4 lead + 2 coal | **+7** (+31 with ind_ordnance) | 702 (159 tech) | Warfare; military demand | Profitable only when war demand exists |
| 7. Mixed industry | steel + food + civic + lab | varies | 25–35 | mixed | +30 to +60 | 60–150 | Multiple | **Most robust**; avoids single-demand risk |
| 8. Research-oriented | 2 labs + research tree | 640/lab + 3,180 tree | 6 (2 labs) | RP | no direct cash | via yield/capex savings | Tech effects | **Capacity-free output; slow payback** (§8) |

### 6.5 Utilisation sweep

For a 4-batch processing chain (whole batches; power derating `floor(4 × pct/10,000)`):

| Utilisation | Batches run | Output | Variable cost | Maintenance | Base margin at reference | Loaded margin (3/GU) |
|---:|---:|---:|---:|---:|---:|---:|
| 0% | 0 | 0 | 0 | **full (capacity)** | 0 − maintenance | negative by maintenance |
| 25% | 1 | 8 (steel) | 24 | 8 | +14 − **6** = +8 | +5 − 6 = −1 |
| 50% | 2 | 16 | 48 | 8 | +28 − 6 = +22 | +10 − 6 = +4 |
| 75% | 3 | 24 | 72 | 8 | +42 − 6 = +36 | +15 − 6 = +9 |
| 100% | 4 | 32 | 96 | 8 | +56 − 6 = +50 | +20 − 6 = +14 |

The maintenance column is 4 batches × 2 crowns = 8 at every utilisation (paid on capacity). The **idle-capacity cost** is the full maintenance plus any dedicated power; at 0% the chain loses 8 crowns/turn (plus generator cost) and produces nothing. The whole-batch rule creates a cliff: at 25% a 4-batch chain still runs one whole batch; at 66% a 1-batch chain runs zero (B-05 Example 11). The player must see this before building.

### 6.6 Mandatory steel-margin investigation

**The 14B observation is confirmed, with conditions.**

| Question | Finding |
|---|---|
| Is steel's +14 base margin real? | **Yes.** 8×7 − (10×1 + 6×1) − 24 − 2 = +14; loaded at 3 GU × 3.00 = +5. It matches B-04 exactly |
| Does steel tie aluminum? | **At base, yes** (+14 each). Steel wins on capital (485 vs 560), power (3 vs 4 GU) and input cost; aluminum wins on output price and single-input simplicity |
| Is steel the practical strongest first build? | **Yes, at launch.** The 4-batch steel package earns +12/turn on 4,280 book; the aluminum package earns +4 on 5,530 and needs a 48-RP tech and a smelter unlock. Steel also starts producing earlier (no tech gate) |
| Does research change the ranking? | **It narrows it.** `tech_ind_heat` turns steel into +40/turn (capex payback 107); `tech_ind_chem` turns aluminum into +36/turn (154) — steel still leads on capital efficiency, aluminum earns more gross revenue. The simulation's prepared comparison (S19/S20) ends at steel 27,534 wealth vs aluminum 27,067 at 120 turns — steel ahead, but only by 1.7% |
| Does steel become unprofitable without demand? | **Yes.** With no buyer (S07), the steel package's cash margin is **−216/turn** (variable + maintenance + power) while inventory accumulates 32 steel/turn; the warehouse fills and batches become `SPACE_BLOCKED`. Treasury ends at **164** vs **4,377** with reference sales; wealth is almost entirely unsold book value (12,590, fixed assets 6,480). Unsold steel is not money |
| What makes steel fail? | (1) No construction/military/market demand; (2) coal starvation — the 4-mill package needs 24 coal for reduction plus 12–18 for power, so 4 coal mines (40) are marginal and the starting refinery's 6-coal draw can tip it; (3) power underbuild; (4) the 20-steel bootstrap — a standard-start nation cannot build the mill plus mines without selling/buying steel |
| Is steel dominant in the formal F-EC-038 sense? | **No.** It does not have the highest margin **and** lowest capital **and** lowest risk, and no output is universally required with no substitute. It is the best *first* manufacturing build, not an unbeatable one |
| Should the recipe or price change? | **No.** The recipe is B-04's (D-046) and was not touched. If playtesting confirms dominance, the correct lever is **demand**: construction steel consumption already exists in B-05; warfare (B-10) and player demand (B-07) are the other levers. A silent nerf to steel would violate B-04 ownership and F-CI-038 |

**Recommendation.** Keep the steel recipe and reference price unchanged. In the balance phase, test steel demand against actual construction and warfare volumes; if steel still dominates, price the demand side (more steel in advanced construction, military consumption, or a B-07 market condition), not the production side. Record the 20-steel bootstrap as a deliberate early constraint, not a defect: it forces the first steel mill decision.

### 6.7 Dominance, dead ends and capital traps

1. **No processing chain is a dead end** because every facility can be demolished for 25% of its crowns, but the refund is small (steel mill 95 crowns on 380) and materials are lost. A wrong industrial build is expensive, not fatal.
2. **Refining is the weakest chain** at reference (zero loaded margin, −9/turn as a self-supplied package). Its real value is the gasoline market and military fuel; a nation that builds refineries without a buyer is in a capital trap.
3. **Ammunition without war demand** is a slow asset: +7/turn on 4,915 book (702 turns). With `tech_ind_ordnance` it doubles to +31 (159 turns), but still needs a war or a buyer.
4. **The 20-steel start is the first capital trap.** The player can spend it on four farms (good), a lab (research), a second city (housing/tempo), or a steel mill (industry) — not all. A steel mill plus mines needs ~35 steel, so the first steel build must use the starting iron/coal facilities or buy steel.
5. **Overbuilding power** (S14) burns 36 coal + 60 crowns + 12 maintenance per turn for unused GU; treasury ends at 1,800 vs 6,214 in the baseline at 120 turns.
6. **Underused refining** (S13) pays 10 crowns/turn of maintenance for four refineries that cannot run (no oil), producing nothing.
7. **Overbuilt facilities** (S12) pay 120 power-short turns and 4,560 maintenance; the nation survives on tax, not industry.
8. **No exploit loop was found**: demolition loses value, granted facilities refund zero, production is exactly-once, reservations release once, and research points are assigned once (§8.4).

---

## 7. Population and housing dependency

### 7.1 The formulas and the ownership split

- **B-05 owns** `housing(city) = 45,000 + 100×I + 25,000×civic` (F-CI-002) and the `CIVIC_UNFUNDED` state.
- **B-06 owns** growth (`F-PD-001/002`): `growth_bp = clamp(50 + floor((approval−55)/2) + min(15, floor(headroom×100/population)) − floor(hunger/30) − floor(crowding/100), −100, 100)`; population is capped at `housing_growth` and floored at 1,000; crowding declines gradually. B-05 supplies the housing number and nothing else.
- **B-04 owns** civilian food demand (`ceil(population/1,000)`), tax (`floor(population×300×stability/1e9)` with the hunger penalty), and the public-service cost (B-06's 20% share).
- **B-10 owns** military rations. B-05 adds no population model.

### 7.2 Civic centre versus infrastructure

| Housing source | Crowns | Materials | Book | DC | Upkeep | Housing | Crowns per 1,000 | Tax value at full occupancy* |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| Civic centre | 300 | 10 steel | 370 | 2 | 1 | 25,000 | **12** | 75 − 15 service − 16.25 food − 1 upkeep = **42.75/turn** |
| Infrastructure 50→300 | 6,250 | — | 6,250 | 25 | 0 | 25,000 | 250 | Same tax, plus 25 DC |
| Infrastructure 100→600 (not legal; cap 500) | — | — | — | — | — | — | — | — |

\*At 300 bp tax, 20% service share, food at 13 crowns per 20 units, 25,000 people = 25 food/turn.

**The civic centre is the housing tool.** It costs 12 crowns per 1,000 housing versus 90–425 for infrastructure. Its payback at full occupancy is 370 / 42.75 ≈ **8.7 turns**; the binding constraint is growth speed, not money. A 25,000-housing city fills at 0.5–0.65%/turn: with 75,000 total housing from 50,000 population, the population reaches 53,343 by turn 10, 60,713 by turn 30, 68,903 by turn 50 and 75,000 by turn 70 (F-PD-001/002, approval 55, no hunger). Average occupancy over the ramp is roughly half, so the realistic civic payback is ~15–20 turns — still the strongest long-run investment in the game, provided food capacity grows with it.

**Food is the prerequisite.** Each 1,000 people consumes 1 food/turn and produces 3 crowns of gross tax (2.4 after the service cost). Feeding 25,000 more people needs 25 food, i.e. 1.25 farm batches (16.25 crowns/turn) — a net cash contribution of roughly 43 crowns/turn per civic at full occupancy. A civic built without food capacity starves the added people (hunger penalty up to 3,000 bp, tax −30%) and the investment turns negative. This is the intended coupling: housing → population → food → tax.

### 7.3 What the model encourages and what it does not

1. **It encourages meaningful city development**: housing is the only way to grow the tax base; civic centres make housing cheap; infrastructure makes DC; population growth is slow enough that the player must plan food and housing together.
2. **It does not create a second population model**: cities hold housing, not people; there is no migration, no per-city population and no local workforce.
3. **It punishes excessive housing investment**: housing above what food and services can support produces hungry, crowded people and a tax penalty; a civic whose upkeep is unpaid loses its housing from growth (CIVIC_UNFUNDED) and creates crowding.
4. **Consequences of a housing shortage** (S15): when the civic upkeep stops at turn 4, `housing_growth` falls from 150,000 to 75,000; the population declines by `ceil(excess/10)` per turn (10% of the excess) to 75,000 and stays there; no one is evicted, no building is lost. This is B-06's `DMP-031` crowding, and B-05's only role is the number.
5. **Ownership boundary**: B-05 does not grow, move or kill population; B-06 does not add housing; B-04 does not change the food formula; B-10 does not add a casualty rule to a strike.

---

## 8. Research progression and technology economics

### 8.1 The 12 technologies

Durations are `ceil(RP / institutes)`; the direct payback is F-CI-034's formula at representative batch counts; the full-cost payback adds the RP cost at the 1-lab whole-tree rate of 3.43 crowns/RP (lab capex 640 + 896 upkeep over 448 RP) and values each extra unit at its reference price. Representative batches: 4 farms, 4 coal mines, 3 oil wells, 4 iron + 4 bauxite mines, 3 lead + 1 uranium mine, 2 refineries, 4 steel mills, 3 smelters, 2 ammunition plants.

| Tech | Branch | RP | Crowns | Prereq | Turns @1/@2/@4 labs | Effect | Representative benefit/turn | Direct payback | Full-cost payback |
|---|---|---:|---:|---|---:|---|---:|---:|---:|
| `tech_agri_rotation` | Agriculture | 24 | 160 | — | 24/12/6 | +1 food/farm | 4 | 40.0 | 60.6 |
| `tech_agri_mechanisation` | Agriculture | 44 | 300 | rotation | 44/22/11 | +1 food/farm | 4 | 75.0 | 112.7 |
| `tech_ext_coal` | Extraction | 20 | 140 | — | 20/10/5 | +1 coal/batch | 4 | 35.0 | 52.1 |
| `tech_ext_oil` | Extraction | 32 | 220 | ext_coal | 32/16/8 | +1 oil/batch | 6 | 36.7 | 55.0 |
| `tech_ext_metals` | Extraction | 40 | 280 | ext_coal | 40/20/10 | +1 iron, +1 bauxite | 12 | 23.3 | 34.8 |
| `tech_ext_deep` | Extraction | 56 | 360 | ext_metals | 56/28/14 | +1 lead, +1 uranium | 39* | 9.2 | 14.2 |
| `tech_ind_heat` | Industry | 28 | 200 | — | 28/14/7 | +1 steel; unlocks ammo | 28 | 7.1 | 10.6 |
| `tech_ind_chem` | Industry | 48 | 340 | ind_heat | 48/24/12 | +1 gasoline, +1 aluminum; unlocks smelter | 36 | 9.4 | 14.0 |
| `tech_ind_ordnance` | Industry | 36 | 260 | ind_heat | 36/18/9 | +1 ammunition | 12 | 21.7 | 32.0 |
| `tech_civ_survey` | Civil works | 20 | 140 | — | 20/10/5 | Infrastructure −10% | saves 10% of infra spend | break-even spend 2,086 | full cost 208.6 |
| `tech_civ_methods` | Civil works | 40 | 280 | civ_survey | 40/20/10 | Construction −10% | saves 10% of facility spend | break-even spend 4,171 | full cost 417.1 |
| `tech_nuclear_engineering` | Energy | 60 | 500 | civ_methods, ind_chem | 60/30/15 | Unlocks uranium mine + nuclear plant | structural | no direct | structural |

\*The reference value of +1 uranium (30/unit) is an upper bound; uranium's only sink is nuclear fuel. The real benefit is that one uranium mine can fuel two nuclear levels instead of one, saving a 710-crown mine per extra level; it is strong only inside a nuclear build.

**Total tree:** 448 RP, 3,180 crowns. The tree is deliberately short: every technology changes a number a player can see.

### 8.2 Research-rate scenarios

| Institutes | Cities needed (2 labs/city) | Tree turns `ceil(448/N)` | Lab capex | Lab upkeep over the run | Lab total | Plus tree crowns | Total research cost | Time saved vs 1 lab |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | never | 0 | 0 | 0 | 3,180 (never spent) | — | — |
| 1 | 1 | **448** | 640 | 896 | 1,536 | 3,180 | **4,716** | — |
| 2 | 1 | **224** | 1,280 | 896 | 2,176 | 3,180 | **5,356** | 224 turns for +640 |
| 4 | 2 | **112** | 2,560 | 896 | 3,456 | 3,180 | **6,636** | 336 for +1,920 |
| 6 | 3 | **75** | 3,840 | 900 | 4,740 | 3,180 | **7,920** | 373 for +3,204 |
| 12 | 6 | **38** | 7,680 | 912 | 8,592 | 3,180 | **11,772** | 410 for +7,056 |
| 24 | 12 | **19** | 15,360 | 912 | 16,272 | 3,180 | **19,452** | 429 for +14,736 |

**Interpretation.** More institutes do not reduce total upkeep per RP (2 crowns per RP is fixed by 2 crowns per lab per turn and 1 RP per lab per turn); they add capex to compress calendar time. The 24-institute path costs **4.1×** the one-institute path to finish 429 turns sooner. That may be worth it in a competitive world, but it is never a cash-saving choice. A nation with no institute accumulates no RP and cannot start a project (URB-059). The standard start holds exactly 20 steel — one lab — so the **second lab is gated by steel**, not by crowns; a research-first nation without a steel source is stuck at one lab (S09 shows exactly this: 3 technologies in 120 turns).

### 8.3 Allocation, banking and programme funding — verified

- **P4.2 assignment:** `need = max(0, cost−progress)`, `applied = min(rate, need)`, pool += rate − applied; a point is assigned to the project **or** the pool, never both (F-CI-021; B-05 Example 15B: 3 RP at 22/24 → 2 progress + 1 pool).
- **Programmes spend banked RP only:** `rp_pool` is reserved at acceptance and consumed at P4.1d, **before** P4.2 generation; a programme cannot be funded by the same settlement's RP, and it never reduces an active project's progress (B-05 Example 15C; F-CI-024).
- **One active project per nation** (URB-093); a completed project cannot restart; effects apply next turn (URB-096/099).
- **No double counting:** the per-settlement identity `Δprogress + Δrp_pool + rp_consumed_by_programmes = rp_generated` holds in every simulation scenario (the model asserts it by construction; the pool and progress are separate fields).
- **Upkeep:** labs 2 crowns/turn, civic 1, charged at P3.7 rank 7(a) labs then civic; an unpaid lab produces no RP (`LAB_IDLE`), an unpaid civic's housing is excluded from growth (`CIVIC_UNFUNDED`). The aggregate-vs-per-facility allocation when only part of the upkeep is affordable is a documented limitation (L-14C-02); the conservative model idles the whole class.

### 8.4 National programmes

| Programme | Branch | RP | Crowns | Materials (book) | Cash + RP cost | Full book cost | Effect | Payback / value |
|---|---|---:|---:|---:|---:|---:|---|---|
| `prg_granary` | Agriculture | 100 | 900 | 100 steel + 50 aluminum (1,100) | 1,243 | 2,343 | +500 warehouse; +1 food/farm | 8 food/turn → 155 turns cash; storage strategic |
| `prg_survey` | Extraction | 100 | 1,000 | 100 steel + 50 gasoline (1,000) | 1,343 | 2,343 | Extraction variable −2 (min 2) | 40/turn at 20 batches → 33.6 turns |
| `prg_standards` | Industry | 100 | 1,200 | 150 steel + 50 aluminum (1,450) | 1,543 | 2,993 | Processing maintenance −1 (min 1) | 16/turn at 16 batches → 96 turns; 48 batches → 32 turns |
| `prg_civil_works` | Civil works | 100 | 1,100 | 120 steel + 60 aluminum (1,320) | 1,443 | 2,763 | +2 DC per city | 24 DC at 12 cities ≈ avoids 8,400 infra → net ~5,643; at 2 cities 4 DC loses |

**Scale dependence.** `prg_civil_works` is the strongest at scale (it displaces the expensive 200→500 infrastructure curve), weak at one or two cities. `prg_survey` pays back fastest with many extraction batches; `prg_standards` needs many processing batches; `prg_granary` is a storage/strategic programme whose cash payback is long. None is a prerequisite for another; each is the payoff for completing a branch.

### 8.5 Research-path comparison A–F

| Path | Technologies (order) | Cost | Effect | Best for |
|---|---|---|---|---|
| A. Agriculture first | rotation → mechanisation | 68 RP, 460 crowns | +2 food/farm (cap 3 with Granary) | A nation whose food margin is thin; the safest first branch |
| B. Extraction first | ext_coal → ext_metals → ext_deep (→ oil) | 116–148 RP, 640–860 crowns | +1 coal/iron/bauxite/lead/uranium | A nation with many mines or a nuclear plan; weak on its own because coal/iron margins are negative |
| C. Industry first | ind_heat → ind_chem → ind_ordnance | 112 RP, 800 crowns | +1 steel/gasoline/aluminum/ammo; unlocks ammo + smelter | A nation with power and inputs; the **highest cash payback** (ind_heat 10.6 turns at four mills) |
| D. Civil works first | civ_survey → civ_methods | 60 RP, 420 crowns | 10% off infrastructure and facilities | A nation about to spend >2,086 on infrastructure and >4,171 on facilities; the cheapest enabler of expansion |
| E. Energy progression | civ_methods + ind_chem → nuclear | 168 RP, 1,120 crowns | uranium + nuclear unlock | A DC-constrained mid-game nation; nuclear gives 20 GU per 2 DC; expensive per GU |
| F. Mixed | food → industry → civil → extraction | 448 RP total | all | The intended long-run path; no branch is a trap, but early order matters |

**Verdict.** Industry-first is the fastest cash payback *if the plants exist*; agriculture-first is the safest; civil-works-first is the best enabler if the player is about to spend on construction; extraction-first is only strong with many mines; nuclear is a DC-compression play, not an energy-cost play.

### 8.6 The extended research-payback framework (F-CI-034 unchanged)

F-CI-034 asks a narrow question: `crowns / (bonus × batches × margin per unit)`. It is a valid first-order estimate but it omits (1) the RP cost, (2) the institute capex and upkeep, (3) the difference between price and contribution margin, (4) utilisation, (5) power and input constraints, (6) demand, and (7) the remaining investment horizon. The fuller framework is:

```
full_cost(tech) = crowns + RP × per_RP_lab_cost + apportioned_lab_capex
per_RP_lab_cost = (lab_capex + 2 × lab_turns) / RP_completed
net_benefit(turn) = Σ_affected_facilities [bonus × batches_run(turn) × realised_margin_per_unit(turn)]
payback_turns   = min t such that Σ_{s=1..t} net_benefit(s) ≥ full_cost(tech)
```

with `batches_run` from B-04's derating and limits, `realised_margin_per_unit` from the actual sale (B-07) or the internal replacement value, and the time remaining in the player's horizon. This framework reproduces F-CI-034 when RP, lab costs, power, demand and utilisation are ignored; it shows, for example, that `tech_agri_rotation` at four farms costs **242.3 crowns** fully loaded and pays back in **60.6 turns**, not the 40 turns of the simplified formula. **The formula itself is not changed**; the framework is published as analytical guidance and the limitation is recorded (L-14C-03). A future decision may promote it to a formula under F-CI-036 if the owner wants a formal runtime calculation.

---
## 9. Integrated worked examples E1–E12

All examples use the published integers, the standard start (D-063) unless stated, and the P3/P4 order. Every number is recomputed by `14C_verify_b05_cities.py` and, where a scenario is referenced, by `14C_simulate_b05.py`.

### Example E1 — Developing the existing capital

**Opening.** Standard start; treasury **1,529** (B-04 Example 2's closing balance); steel **20**; capital infrastructure **50**; capacity **15 DC**, used **11**, free **4**; housing **50,000**; fixed assets **0**.

**Order 1 — infrastructure 50 → 100 (F-CI-005).** `130 + 140 + 150 + 160 + 170 = 750` crowns; no materials. Treasury **779**; capacity `10 + 10 = 20`; housing `45,000 + 10,000 = 55,000`; book value **+750**; DC used 11, free **9**.

**Order 2 — a fourth farm (F-CI-011/012).** 120 crowns + 5 steel; book `120 + 35 = 155`; treasury **659**; steel **15**; DC used **12**, free **8**; food capacity 4.

**Production (B-04 F-EC-004/005).** 4 farms × 20 = **80 food**; variable 4 × 12 = 48; maintenance 4 × 1 = 4; contribution at reference `80 − 52 = +28`. Population 50,000 → demand 50; food `120 + 80 − 50 = 150`.

**Final state.** Treasury 659; steel 15; capacity 20/12; housing 55,000; fixed assets `750 + 155 = 905`; national wealth is unchanged by the capex (liquid crowns and steel become fixed assets); the farm adds +28/turn and its book payback is `155 / 7 = 22.1` turns.

**Interpretation.** Infrastructure bought **room**, not output; the farm is the first cash-positive asset. The 750-crown upgrade also adds 5,000 housing, whose full-occupancy tax value is 15 crowns/turn — a 50-turn housing payback, far slower than the farm. The purchase is justified by the 5 DC, not by the housing.

### Example E2 — Founding and developing a second city

**Opening.** Capital at 100 (E1's state); treasury **1,529**; steel **20**; national infrastructure **100** (the k=2 gate); one city.

**Founding (F-CI-006/007).** `city_cost(2) = 400 + 150×4 = 1,000` crowns + 20 steel; book `1,000 + 140 = 1,140`. Treasury **529**; steel **0**; cities 2; national housing `55,000 + 46,000 = 101,000`. The new city has infrastructure 10, capacity 11, housing 46,000 and no facilities. It adds a **second construction slot** and a second set of per-city limits.

**Development.** 10 → 50 costs `90 + 100 + 110 + 120 = 420`; treasury **109**; capacity 15; housing 51,000; national housing 106,000; book +420 (total 1,560).

**The steel wall.** With steel 0, the nation cannot build a farm (5 steel), a mine (5) or a lab (20). The second city is a shell until steel is produced or bought. The full path — gate 750 + founding 1,000 + development 420 = **2,170 crowns** — buys **+20 DC** (the capital's 5 from the gate plus the new city's 15) and **51,000 housing**, at **108.5 crowns/DC**, plus a construction slot. That is cheaper per DC than continuing the capital from 100 (225/DC for 100→200) and much cheaper than the 200→500 curve (425/DC).

**Interpretation.** Founding the second city is the best **tempo** purchase in the game, but it consumes the entire 20-steel stock. A player who founds before securing a steel source trades all facility construction for housing and a slot.

### Example E3 — Infrastructure versus facility construction at one DC

At the capital's 50-level state, three ways to spend roughly one DC:

| Choice | Cost | DC | Output | Recurring | Payback |
|---|---:|---:|---|---|---:|
| Infrastructure 50 → 60 (F-CI-004/005) | **130** crowns | +1 | +1,000 housing | none | housing tax 3/turn → ~43 turns; no output |
| Farm (F-CI-011/012) | **120** + 5 steel (book 155) | +1 | 20 food | 12 variable + 1 maintenance | **22.1** turns at reference |
| Warehouse expansion (F-CI-013/014) | **180** + 5 steel (book 215) | +1 | +250 storage | none | strategic; prevents `SPACE_BLOCKED` |

**Interpretation.** The infrastructure step is *not* a building: it raises the DC ceiling and the housing floor, but produces nothing. The farm is the only one of the three that earns. The warehouse earns nothing directly but protects every chain from space blocking. A player with 4 free DC should buy one farm (1), one lab (3) or a refinery (2) plus a farm (1) — not four infrastructure steps.

### Example E4 — Housing expansion: civic centre versus infrastructure

**Civic route.** 300 crowns + 10 steel (book 370), 2 DC, 1 upkeep, +25,000 housing. At 300 bp tax, 25,000 people generate **75 crowns** of gross tax; service 20% = 15; food 25 units at 13 crowns per 20 units = 16.25; civic upkeep 1 → net **42.75/turn** at full occupancy. Payback `370 / 42.75 = 8.7` turns. Growth from 50,000 toward 75,000 at 0.5–0.65%/turn reaches **53,343** at turn 10, **60,713** at turn 30, **68,903** at turn 50 and **75,000** at turn 70; the average occupancy over the ramp is about half, so the realistic payback is **15–20 turns**.

**Infrastructure route.** 25,000 housing needs 250 levels; 50 → 300 costs `750 + 2,250 + 3,250 = 6,250`, gives **25 DC** and the same housing, with no upkeep. The housing payback is `6,250 / 42.75 ≈ 146` turns; the DC is the real purchase.

**Interpretation.** The civic centre is the **housing** tool (12 crowns per 1,000 housing); infrastructure is the **DC** tool (90–425 crowns per DC, 150 crowns per 1,000 housing at 50→100). Building civic centres before food capacity is a trap: the added people starve, hunger suppresses tax and the payback disappears. Building them after food is secured is the strongest long-run investment in the game.

### Example E5 — Constructing and operating an extraction facility (lead into ammunition)

**Lead mine (F-CI-011/012).** 260 crowns + 5 steel; book **295**; 1 DC; output 6 lead; variable 16; maintenance 1; base margin `6×3 − 16 − 1 = +1`; book payback **295** turns at reference. Lead is a thin extraction chain on its own.

**Ammunition plant (tech_ind_heat).** 360 crowns + 15 steel; book **465**; 2 DC; recipe 8 lead + 4 coal → 10 ammunition; variable 20; maintenance 2; 2 GU; base margin `10×6 − (8×3 + 4×1) − 20 − 2 = +10`; loaded at 2 GU × 3 = **+4**.

**Integrated (1 plant + 2 lead mines).** Capex `465 + 2×295 = 1,055`; 2 lead mines produce 12 lead (1 batch consumes 8, surplus 4); margins: ammo +10, two lead mines +2, power −6 → **+6/turn**; payback `1,055 / 6 = 176` turns. With `tech_ind_ordnance` (+1 ammunition = +6/turn), **+12/turn** → 88 turns.

**Interpretation.** Ammunition is a war-demand asset. Without a military buyer it is a 176-turn payback; with the tech and a war it halves. The extraction mine is not the investment — the plant and the demand are.

### Example E6 — Constructing and operating a steel mill package

**Package.** 4 steel mills + 4 iron mines + 4 coal mines + 2 coal plants (independent of the starting facilities; assumed at a city with 200 infrastructure, 20 DC for the package). Capex `4×380 + 4×180 + 4×160 + 2×280 = 3,440` crowns; materials `4×15 + 4×5 + 4×5 + 2×10 = 120` steel (book 840); **book 4,280**; **20 DC**.

**Steady state at reference prices.** Output 32 steel (224 crowns) + coal `40 − 24 − 12 = 4` surplus (4) = **228**; cash costs: iron 4×11 = 44, coal 4×11 = 44, steel variable+maintenance 4×26 = 104, generators 2×12 = 24 → **216**; **+12/turn**. Book payback `4,280 / 12 = 357` turns.

**With `tech_ind_heat`.** Output 36 steel (252) + 4 coal = 256; same costs 216 → **+40/turn**; book payback **107** turns.

**With steel at 8/unit.** 32×8 + 4 = 260 − 216 = **+44/turn**; payback 97 turns.

**No demand (the failure case).** Output accumulates 32 steel/turn; the cash costs continue **−216/turn**; the shared 2,000-unit warehouse fills in about 60 turns of steel alone and `SPACE_BLOCKED` stops the mills. In the 120-turn simulation (S07) treasury ends at **164** versus **4,377** with reference sales; wealth is **12,590**, almost all unsold book value and fixed assets, not spendable money.

**Interpretation.** Steel is the strongest first manufacturing build at reference prices and the clearest example of the difference between wealth and cash: unsold steel is wealth, but the variable and maintenance costs are cash. Demand — construction, warfare or a player market — is the missing half of the investment case.

### Example E7 — Comparing steel and aluminum investment

| Item | Steel package | Aluminum package |
|---|---:|---:|
| Facilities | 4 mills + 4 iron + 4 coal + 2 plants | 4 smelters + 6 bauxite + 4 coal + 3 plants |
| DC | 20 | 28 |
| Capex (crowns) | **3,440** | **4,480** |
| Materials (book) | 120 steel (840) | 150 steel (1,050) |
| Book value | **4,280** | **5,530** |
| Output/turn | 32 steel + 4 coal | 32 aluminum + 22 coal |
| Cash margin (no research) | **+12/turn** | **+4/turn** |
| Cash margin (industry tech) | **+40** (`ind_heat`) | **+36** (`ind_chem`) |
| Book payback (no research) | **357** | **1,383** |
| Book payback (tech) | **107** | **154** |
| Gate | none | `tech_ind_chem` (48 RP + `ind_heat` 28 RP) + smelter unlock |
| Inputs | iron + coal (two chains) | bauxite (one chain) |
| Power | 3 GU/batch | 4 GU/batch |

**Simulation comparison (prepared, both techs, reference sales).** At 120 turns: steel treasury **22,484**, wealth **27,534**; aluminum treasury **20,141**, wealth **27,067**. Steel leads by **1.7%** in wealth and **2,343** in treasury; aluminum sells more gross value (36,342 vs 31,350) but spends more on inputs and power.

**Interpretation.** Steel is the better **first** build: cheaper capital, earlier production, lower power, no tech gate. Aluminum is a viable **second** chain once `tech_ind_chem` exists and aluminum demand (military, advanced construction, market) is present. The margin difference narrows after research; neither chain is a runaway.

### Example E8 — Establishing research institutes and calculating their payback

**One institute.** 500 crowns + 20 steel; book **640**; 3 DC; upkeep **2/turn**; 1 RP/turn.

**`tech_agri_rotation`.** 24 RP + 160 crowns. With one lab: **24 turns**; lab upkeep 24×2 = 48; **cash 208** plus the lab. With the lab shared over the whole 448-RP tree, the per-RP lab cost is `(640 + 896) / 448 = 3.43`, so the tech's full cost is `160 + 24×3.43 = 242.3`. At 4 farms the benefit is 4 food/turn (reference value 4), giving a **direct** payback of `160/4 = 40` turns (F-CI-034) and a **full-cost** payback of `242.3/4 = 60.6` turns.

**Two institutes.** 12 turns; lab capex 1,280 + upkeep 48 + tech 160 = **1,488** if the labs are dedicated to this one technology → payback **372** turns. Shared over the tree: per-RP lab cost `(1,280 + 896)/448 = 4.86`; tech full cost `160 + 24×4.86 = 276.6` → **69** turns. The second lab buys **calendar time**, not a cheaper technology.

**Interpretation.** Research is a **capacity-free** way to raise output: it uses no DC beyond the labs and no inputs, and its yield bonus is permanent. Its direct cash payback is slower than a farm's (60.6 vs 22.1 turns at four farms) but it does not consume a farm's DC or its maintenance. The second lab is a tempo decision, not a cost-saving one.

### Example E9 — Funding and completing a technology (`tech_ind_heat`)

**Setup.** Two institutes (book 1,280, 4 upkeep/turn); `tech_ind_heat` = 28 RP + 200 crowns; **14 turns** at 2 RP/turn; upkeep 56; total cash 256; full cost with the shared-tree rate `200 + 28×3.43 = 296.0`.

**Benefit.** +1 steel per mill batch. With four mills: +4 steel/turn = **+28/turn** at reference (or +32 at 8/unit); **full-cost payback 10.6 turns**. It also unlocks the ammunition plant.

**Interpretation.** Industry technologies pay back fastest **when the plants already exist**. A technology that adds +1 per batch is worth nothing without batches; the correct order is facilities first, then the yield technology (or a small pilot facility to justify the tech).

### Example E10 — Comparing research, industrial and city-development investment (1,000 crowns)

**Snapshot.** Capital already at infrastructure 100 (gate met), treasury 1,500, standard facilities and 20 steel. Each path spends about 1,000 crowns; the simulation runs 120 turns with surplus food/coal/gasoline sold at reference.

| Path | Spend | T30 treasury / wealth | T120 treasury / wealth | Outcome |
|---|---|---:|---:|---|
| Second city | 1,000 + 20 steel | **2,561 / 4,578** | **12,315 / 14,975** | 2 cities; population 92,048 by T120; **58 food-short turns** (no food investment) |
| Research institute + agri tech | 660 + 20 steel | **2,738 / 4,320** | **9,266 / 11,826** | 1 technology; capacity-free +1 food/farm; slowest cash |
| Four farms | 480 + 20 steel | **3,653 / 5,293** | **12,689 / 15,229** | Best cash and wealth; food surplus sold; no new DC |
| Infrastructure 100 → 150 | 1,000 | **2,540 / 4,566** | **9,685 / 12,611** | +5 DC +5,000 housing; population 60,000; enables future facilities |

**Interpretation.** All four paths are viable and none dominates on every axis. Farms win cash and wealth over 120 turns; the second city wins tempo and housing but starves without food; the lab is the weakest cash path but buys permanent, capacity-free output; infrastructure buys the DC that every facility strategy needs. The "best" choice depends on the next decision, which is exactly the intended strategic texture.

### Example E11 — Overinvesting in power generation (the failure)

**State.** Capital at 150 infrastructure with 6 coal plant levels (12 DC; 36 GU), the standard production facilities (2 GU demand), 60 coal, 2 coal mines (20 coal/turn).

**Per turn.** 6 levels burn **36 coal** and pay **60 crowns** variable + **12** maintenance. Supply 36 GU; demand 2 GU; **34 GU are discarded** (`ECN-059`). Coal production 20/turn cannot sustain 36/turn; after the 60-coal stock is spent the levels fail closed in sequence. Treasury at turn 10 is **1,092** versus **1,490** in the baseline; at turn 120 it is **1,800** versus **6,214**.

**Interpretation.** A generator level runs whenever fuelled and funded; there is no idle control. Overbuilding power is a continuous cash leak and a fuel drain. The player's remedies are to fill the grid with processing or to demolish the plant (25% refund). The correct pattern is to build generation just ahead of demand, not 18× ahead.

### Example E12 — Excessive research institutes (the low-return path)

**State.** 12 institutes (6 cities × 2) and the full 12-technology tree.

**Cost.** Lab capex `12 × 640 = 7,680`; tree crowns 3,180; upkeep over the 38-turn tree `24 × 38 = 912`; **total 11,772** crowns. The one-lab path costs `640 + 3,180 + 896 = 4,716` and takes 448 turns. The extra **7,056** crowns buy **410 turns** of calendar time.

**After completion.** If the labs are not demolished, they keep charging 24/turn for zero RP use: `(120 − 38) × 24 = 1,968` crowns over the rest of a 120-turn horizon. The simulation (S11) shows a large treasury because the prepared state has a 150,000 population, but the research spend is **4.1×** the one-lab path and 25% of the lab capex is recoverable only by demolition.

**Interpretation.** Research speed is a **competitive** purchase, not a cash-saving one. Rush the tree when early technologies unlock a strategy that an opponent cannot match; otherwise one or two labs and a patient queue dominate on cost. Demolish idle labs; do not let them bleed 24 crowns/turn.

---

## 10. Economic simulation report

### 10.1 The reference model

`qa_backups/14C_simulate_b05.py` implements one nation's published B-05 rules on top of the published B-04 settlement and B-06 growth:

- **P3.1** tax (`floor(population × 300 × 10,000 / 1e9)` with the previous hunger penalty), **P3.2** whole-obligation maintenance (extraction → generation → processing), **P3.3** extraction (food first; money and space limits), **P3.4** power (per-level fail-closed fuel and variable cost; `floor(10,000×supply/demand)`; whole-batch derating), **P3.5** processing (input, money, space and power limits), **P3.6** civilian food and hunger, **P3.7** facility upkeep 7(a) then the public-service cost 7(b), **P3.8** population growth (F-PD-001/002 with approval held at the neutral 55; hunger and crowding applied; housing cap; 1,000 floor).
- **P4.1** construction (one action per city; founding and programmes), **P4.2** research generation, assignment, banking and completion, **P4.3** a **labelled demand scenario**: `reference` sells chosen goods to an assumed buyer at the B-04 reference price; `none` sells nothing.
- Integer arithmetic only; no floating point in any decision. The model asserts treasury ≥ 0, warehouse ≤ capacity, DC within capacity, infrastructure 10–500 and population ≥ 1,000 after every scenario; no violation occurred in any of the 24 runs.

**Assumptions, explicitly labelled.** Approval is held at 55 (B-06 politics is out of scope); no warfare, diplomacy, alliances or trade counterparties exist; prepared mid-game states are snapshots with zero-cost opening infrastructure lots; reference-price sales are an optimistic B-07 assumption and are never presented as NPC demand; population growth is B-06's formula, not a B-05 invention.

**Cross-check.** The model reproduces Prompt 14B's 30-turn standard-start reference exactly: **treasury 1,530, inventory 1,516 units, wealth 4,386** (S01). This is independent evidence that the B-05 capacity layer did not perturb the B-04 accounting.

### 10.2 Scenario results (10 / 30 / 60 / 120 turns)

| Scenario | T10 treasury | T30 treasury | T60 treasury | T120 treasury | T10 wealth | T30 wealth | T60 wealth | T120 wealth | T120 cities | T120 techs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| S01 baseline (no sales) | 1,490 | 1,530 | 2,706 | 6,214 | 2,870 | 4,386 | 6,424 | 10,290 | 1 | 0 |
| S02 baseline + food sales | 1,590 | 1,830 | 2,564 | 6,320 | 2,870 | 4,386 | 6,596 | 10,710 | 1 | 0 |
| S03 baseline + manufactured sales | 2,230 | 3,086 | 4,532 | 8,400 | 2,870 | 4,386 | 6,530 | 10,398 | 1 | 0 |
| S04 infrastructure-first | 193 | 70 | 301 | 164 | 2,879 | 4,541 | 7,181 | 13,240 | 1 | 0 |
| S05 rapid city expansion | 1,242 | 1,233 | 1,229 | 2,103 | 2,879 | 4,454 | 6,793 | 12,761 | 2 | 0 |
| S06 steel focus (reference sales) | 363 | 121 | 71 | 4,377 | 2,879 | 4,565 | 7,626 | 13,139 | 1 | 0 |
| S07 steel focus (no demand) | 193 | 70 | 300 | **164** | 2,879 | 4,541 | 7,191 | 12,590 | 1 | 0 |
| S08 aluminum-first attempt (tech-gated) | 363 | 253 | 744 | 6,008 | 2,879 | 4,551 | 7,523 | 13,613 | 1 | 0 |
| S09 research-first (2 labs) | 559 | 459 | 1,545 | 4,857 | 2,698 | 4,049 | 6,056 | 9,728 | 1 | 3 |
| S10 research-first (4 labs, prepared) | 4,463 | 6,595 | 10,311 | 17,899 | 6,856 | 9,563 | 13,271 | 20,865 | 2 | 12 |
| S11 excessive institutes (12 labs) | 5,059 | 8,021 | 15,839 | 41,006 | 8,750 | 11,729 | 19,505 | 44,559 | 6 | 12 |
| S12 excessive facilities (overbuilt) | 2,082 | 3,067 | 5,057 | 11,308 | 4,400 | 5,379 | 7,350 | 13,587 | 1 | 0 |
| S13 underused refining capacity | 2,421 | 3,420 | 4,950 | 8,880 | 3,353 | 4,737 | 6,837 | 11,037 | 1 | 0 |
| S14 power overinvestment | 1,092 | 765 | 574 | **1,800** | 2,256 | 2,986 | 4,247 | 7,155 | 1 | 0 |
| S15 housing shortage (civic unfunded) | 5,509 | 8,187 | 11,493 | 18,181 | 8,250 | 10,971 | 14,280 | 20,970 | 1 | 0 |
| S16 food shortage | 1,514 | 1,309 | 889 | **2,388** | 2,674 | 3,745 | 5,143 | 7,000 | 1 | 0 |
| S17 insufficient treasury | **0** | **2** | **9** | **2** | 1,552 | 1,302 | 1,339 | 1,432 | 6 | 0 |
| S18 balanced mixed development | 1,505 | 2,601 | 4,203 | 7,809 | 2,863 | 4,299 | 6,441 | 10,495 | 1 | 0 |
| S19 steel vs aluminum — steel | 4,784 | 7,723 | 12,524 | 22,484 | 9,834 | 12,773 | 17,574 | 27,534 | 1 | 2 |
| S20 steel vs aluminum — aluminum | 3,997 | 5,740 | 10,421 | 20,141 | 9,891 | 12,666 | 17,347 | 27,067 | 1 | 2 |
| S21 menu — second city | 1,102 | 2,561 | 5,431 | 12,315 | 2,884 | 4,578 | 7,530 | 14,975 | 2 | 0 |
| S22 menu — research institute | 1,423 | 2,738 | 4,862 | 9,266 | 2,705 | 4,320 | 6,822 | 11,826 | 1 | 1 |
| S23 menu — four farms | 1,633 | 3,653 | 6,665 | 12,689 | 3,093 | 5,293 | 8,605 | 15,229 | 1 | 0 |
| S24 menu — infrastructure 100–150 | 1,102 | 2,540 | 4,921 | 9,685 | 2,884 | 4,566 | 7,247 | 12,611 | 1 | 0 |

### 10.3 What the scenarios show

**Baseline and sales (S01–S03).** The no-sales baseline is cash-stable but warehouse-bound: stock peaks at 1,944 of 2,000 and production stops; treasury grows on tax alone because there is nothing left to spend on. Selling food adds little (S02); selling the starting manufactured stock and ongoing gasoline adds ~2,200 at T120 (S03) but is a labelled market assumption, not free income. The S01 T30 values reproduce 14B exactly.

**Infrastructure without food (S04).** The infrastructure-first state buys 310 levels (8,680 crowns), grows its population to **79,212** and suffers **33 food-short turns**: housing grew, food did not. Treasury ends at 164, wealth 13,240 (almost all fixed assets). This is the clearest demonstration that infrastructure is not a food strategy.

**Rapid city expansion (S05).** The growth planner reaches the 100 gate, founds **one** city (the second), and by T120 has 2 cities, 300 infrastructure levels bought, population 84,792 and **9 food-short turns**. The 20-steel stock is consumed by the founding, so no farm can follow; the nation cannot reach the 200 gate without more steel. City 3 never happens. **The binding constraint on expansion is steel and the gate, not crowns.**

**Steel with and without demand (S06–S07).** Same build, opposite outcomes: **4,377 versus 164** treasury at T120. The no-demand state's wealth (12,590) is unsold book value and fixed assets; its food shortage appears because the refinery and steel chain compete for coal and the steel plan spends its steel on the package. This is the mandatory steel-demand finding in simulation form.

**Aluminum-first from a cold start (S08).** The smelter requires `tech_ind_chem`, which the scenario does not research; the plan stalls at bauxite mines, produces **zero aluminum**, and lives on coal/gasoline sales. The path is not "bad economy"; it is **tech-gated** and the gate must be planned first. The prepared comparison (S20) shows the chain's true economics.

**Research (S09–S11).** From the standard start, the second lab is steel-gated, so S09 has one lab and completes **3 technologies in 120 turns**. Prepared four-lab research (S10) completes the tree near T112; twelve labs (S11) complete it by **T38**, then keep charging 24/turn. Speed costs capex, not upkeep per RP.

**Overbuilding and underuse (S12–S14).** S12 pays **120 power-short turns** and 4,560 maintenance; S13 pays 10 crowns/turn for four refineries with no oil and produces nothing; S14 burns 36 coal and 72 crowns per turn for 34 discarded GU and ends at **1,800** versus 6,214. Each is a real, visible mistake, not a hidden trap.

**Housing and food failure (S15–S17).** S15 shows crowding working exactly as B-06 specifies: with civic upkeep stopped at turn 4, population falls from 150,000 to **75,000** and stays there. S16 shows hunger suppressing tax: treasury 2,388 versus 6,214, with 119 food-short turns. S17 is the overextended state: 6 cities, 60 extraction and 30 processing batches, population 50,000; treasury collapses to **0–9**, maintenance consumes 12,348 of 12,618 tax, food is short for 105 turns and the population falls to 38,422. **Broad industry without population and food is insolvency.**

**Balanced development (S18).** The greedy production planner never reaches a lab (its free DC is always spent on production), so it completes **zero technologies** in 120 turns despite a healthy treasury. Research is not automatic; a production-only strategy leaves the tree untouched. This is an opportunity-cost result, not a defect.

**Steel versus aluminum (S19–S20).** Steel leads at every horizon and ends **1.7% ahead in wealth** (27,534 vs 27,067) with **2,343 more treasury**. Aluminum sells more gross value but spends more. Steel is the first industrial chain; aluminum is the second, conditional one.

**The 1,000-crown menu (S21–S24).** Farms win wealth at T120 (15,229), the second city wins tempo but starves (14,975 with 58 food-short turns), the lab is the weakest cash path (11,826) but buys a technology, and infrastructure buys DC and housing (12,611). Every path is defensible; none dominates.

### 10.4 Dominance, dead ends and capital traps (F14C findings)

| ID | Finding | Evidence | Severity | Owner | Disposition |
|---|---|---|---|---|---|
| F14C-01 | The B-05 model reproduces 14B's standard-start 30-turn result exactly | S01: 1,530 / 1,516 / 4,386 | Informational | B-05/B-04 | Validation anchor |
| F14C-02 | The 20-steel start is a hard bootstrap gate for labs, cities and steel | E2, E6, S05, S09 | Medium | B-05 | Deliberate constraint; document, no change |
| F14C-03 | Steel is the practical strongest first manufacturing build; not formal dominance; demand-gated | E6, E7, S06/S07, S19/S20 | Medium | B-05/B-04 | No recipe change; demand-side playtest named |
| F14C-04 | Aluminum is the second industrial chain; tech-gated and capital-hungry | E7, S08, S20 | Medium | B-05 | Keep; playtest with aluminum demand |
| F14C-05 | Refining is the weakest chain at reference (0 loaded margin; −9/turn self-supplied) | §6.2, §6.6 | Medium | B-04 | Preserve as a market/military play |
| F14C-06 | Ammunition is war-demand dependent | E5 | Medium | B-05/B-10 | Playtest with military demand |
| F14C-07 | Civic housing is the strongest long-run investment once food is secured | E4, S21–S24 | Medium | B-05 | Keep; food coupling is intended |
| F14C-08 | Infrastructure-first without food starves the population | S04 | Medium | B-05/B-06 | Keep; warning surfaces in UI |
| F14C-09 | City expansion is gated by national infrastructure and steel, not crowns | S05, E2 | Medium | B-05 | Keep; the gate is the design |
| F14C-10 | More labs buy time, not cheaper research; the second lab is steel-gated | §8.2, S09–S11 | Medium | B-05 | Keep; demolition is priced |
| F14C-11 | Power, facility and lab overbuilding are cash leaks with visible flags | S11–S14 | Low | B-05 | Keep; no hidden penalty needed |
| F14C-12 | No money-creating or value-cycling exploit was found | E17-type checks; S01–S24 invariants | None | B-05/B-04 | No change |

**Capital traps.** The first one is the 20-steel allocation (farm vs lab vs city vs mill). The second is a processing package with no buyer (S07). The third is a refinery fleet without oil (S13). The fourth is broad industry without population (S17). Each is priced and visible; none is an unstoppable snowball. **No dominant strategy** was found: the strongest industrial chain (steel) requires demand, the strongest housing tool (civic) requires food, and the strongest capacity tool (infrastructure) requires population and facilities to use it.

### 10.5 Simulation limitations

The model is deterministic arithmetic, not a game. It has one nation, no market counterparty, no politics, no war, no diplomacy, no alliances and no random world events. Approval is held at 55. Prepared states use zero-cost opening lots. Reference-price sales are an assumption, not B-07 behaviour. **Simulation is numerical evidence, not proof of player balance.**

---

## 11. Cross-system consistency matrix

**Method.** Every row was read in both authoritative documents. The vocabulary is exactly the four required statuses. The **contradiction register in §12 is separate** and is not counted as matrix rows.

| ID | Source → Target | Source documents | Formula / parameter IDs | Dependency and expected interaction | Owner | Timing | Evidence and validation | Result | Status | Limitation |
|---|---|---|---|---|---|---|---|---|---|---|
| X-01 | B-02 → B-05 | B-02 §13 TR-040; B-05 URB-067 | P3.7/P4.1/P4.2 | Construction at P4.1, research at P4.2, upkeep at P3.7 | B-02 | Boundary | Phase order verified in the simulator | Holds | **VERIFIED CONSISTENT** | — |
| X-02 | B-02 → B-05 | B-02 §18; B-04 ECN-132/141; B-05 URB-070 | F-CI-028 | Action states, idempotency and event keys | B-02 | Submission and P4.1 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-03 | B-05 → B-02 | B-05 URB-064/113; B-02 §18 | F-CI-028 | One construction per city, one founding and one programme per nation per turn | B-05 | Submission | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-04 | B-02 → B-05 | B-02 §10 TR-024; B-05 URB-009/030/116 | — | 2-hour UTC cadence; no economic rule reads wall-clock time | B-02 | Turn | Rule comparison | Holds | **VERIFIED WITH DOCUMENTED LIMITATION** | The 24-hour city-rename cooldown is cosmetic real-time, not an economic rule (L-14C-06) |
| X-05 | B-03 → B-05 | B-03 §8; D-063; B-05 URB-028/047 | §3.4 | Standard capital 50 I, 15 DC, nine granted facilities, book 0 | B-03 | Nation creation | Rule comparison and E1 | Holds | **VERIFIED CONSISTENT** | — |
| X-06 | B-03 → B-05 | B-03 §9.4; B-05 URB-038/142 | — | Reroll destroys cities, facilities, RP, techs, programmes; standard bundle once | B-03 | Reroll | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-07 | B-03 → B-05 | D-067; B-05 URB-031/035 | F-CI-030 | 12-city bound; no deletion or transfer | B-03/B-05 | Submission | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-08 | B-04 → B-05 | B-04 §10; register §3.2/§3.3; B-05 F-CI-015/016 | F-EC-004/005/008/012 | Output per batch, recipes and yields consumed unchanged | B-04 | P3.3/P3.5 | Cross-document value comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-09 | B-04 → B-05 | B-04 ECN-051/147a; D-241; B-05 F-CI-017 | F-EC-014 | Maintenance rates, whole obligations, standards floor | B-04 | P3.2 | Rule comparison and simulation | Holds | **VERIFIED CONSISTENT** | — |
| X-10 | B-04 → B-05 | B-04 D-058; register §3.5; B-05 F-CI-012 | Reference prices | Book value uses reference prices; not a market promise | B-04 | P4.1 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-11 | B-04 → B-05 | B-04 ECN-120/121/124; B-05 F-CI-014 | Warehouse | National warehouse, space blocking, expansion 250 | B-04 | P3.3/P3.5 | Rule comparison and simulation | Holds | **VERIFIED CONSISTENT** | — |
| X-12 | B-04 ↔ B-05 | B-04 register F-EC-026; B-04 ECN-108; B-05 F-CI-019/URB-118a/b | F-EC-026, F-CI-019 | Fixed assets = infrastructure carrying value + other assets, with impairment | B-04 | P4/P5/P3.8 | Expression comparison | **F-EC-026's expression omits infrastructure carrying value and impairment** | **CONTRADICTION IDENTIFIED** | C-14C-02; B-04-owned handoff |
| X-13 | B-04 → B-05 | B-04 ECN-105/152 rank 7; B-05 URB-120 | F-CI-025 | P3.7 order: 7(a) facility upkeep, 7(b) service, 7(c) construction maintenance | B-04/B-05 | P3.7 | Rule comparison | Holds; B-05 supplies the lab-then-civic order inside 7(a) | **VERIFIED WITH DOCUMENTED LIMITATION** | The lab/civic aggregate allocation when part of the upkeep is affordable is unspecified (L-14C-02) |
| X-14 | B-05 → B-04 | D-241; B-04 F-EC-004/012/014; B-05 F-CI-015/016/017/023 | Yield and maintenance bonuses | B-04 consumes the published B-05 modifiers | B-04 | P3.3/P3.5 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-15 | B-04 ↔ B-05 | B-04 ECN-028; B-05 URB-107/F-CI-024 | `prg_survey` | Gasoline sink roster vs the 50-gasoline programme material | B-04 | Programme | Rule comparison | **ECN-028 lists military fuel and trade only; B-05 consumes 50 gasoline** | **CONTRADICTION IDENTIFIED** | C-14C-01; B-04-owned handoff |
| X-16 | B-04 → B-05 | B-04 ECN-080–091; B-05 URB-081 | F-EC-002/003 | Food priority, demand, hunger; B-05 adds no food rule | B-04 | P3.6 | Rule comparison and simulation | Holds | **VERIFIED CONSISTENT** | — |
| X-17 | B-05 → B-06 | B-05 F-CI-002; B-06 DMP-037 | Housing | `45,000 + 100I + 25,000 civic` | B-05 | P3.8 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-18 | B-06 → B-05 | B-06 F-PD-001/002, DMP-030; B-05 URB-124 | Growth | Housing is a hard growth cap; crowding is gradual | B-06 | P3.8 | Formula comparison and S15 | Holds | **VERIFIED CONSISTENT** | — |
| X-19 | B-05 → B-06 | B-05 URB-120; B-06 DMP-038 | CIVIC_UNFUNDED | Unpaid civic housing excluded from growth; people not evicted | B-05 | P3.7/P3.8 | Rule comparison and S15 | Holds | **VERIFIED CONSISTENT** | — |
| X-20 | B-06 → B-04/B-05 | B-06 F-PD-020; B-04 F-EC-001; D-240 | Service cost | Population → tax → 20% service obligation | B-06/B-04 | P3.1/P3.7 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-21 | B-06 → B-05 | B-06 DMP-028/034; B-05 URB-124/125 | Approval/stability | B-05 supplies only housing and civic count; approval and stability are B-06's | B-06 | P3.8 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-22 | B-07 → B-05 | B-07 MKT-053; B-05 URB-154 | — | Trade moves crowns/resources, never capacity, RP or buildings | B-07 | P4.3 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-23 | B-07 → B-05 | B-04 ECN-124; B-05 URB-058/154 | F-CI-014 | Warehouse checked on the buyer before settlement | B-07/B-04 | P4.3 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-24 | B-07 → B-05 | B-07 §2; B-04 D-058; B-05 F-CI-012 | Reference price | Reference price is book value; there is no NPC buyer | B-07/B-04 | P4.3 | Rule comparison and simulation labels | Holds as a book-value rule | **VERIFIED WITH DOCUMENTED LIMITATION** | Industrial cash flow depends on a real buyer; the simulation labels every sale assumption (L-14C-05) |
| X-25 | B-07 → B-05 | B-07 D-114 | 3,000 bp band | Fair-value band applies to trades, not to B-05 costs | B-07 | P4.3 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-26 | B-08 → B-05 | B-05 URB-155 | — | A sanction may freeze an action, never delete an asset | B-08 | Submission | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-27 | B-08 → B-05 | B-05 URB-155 | — | Aid/reparations move crowns/resources only | B-08 | P4 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-28 | B-09 → B-05 | B-09 ALL-006/087; ECN-213a; B-05 URB-156 | — | Production tax on current-turn crowns/resources; RP, housing and capacity are not taxable | B-09 | P3 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-29 | B-09 → B-05 | B-09 ALL-087; B-05 URB-156 | — | No alliance ownership of cities, facilities, technologies or programmes | B-09 | Any | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-30 | B-09 → B-04 | ECN-213a; B-04 P3 order | — | Post-tax same-turn consumption; B-05 capacity reads the national vector | B-04/B-09 | P3 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-31 | B-10 → B-05 | B-10 WAR-109a–m; F-WR-037; B-05 URB-157 | Damage | `removed = min(ceil(I×500/10,000), 20, campaign headroom, I−10)` | B-10 | P5 | Formula comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-32 | B-10 → B-05 | B-10 WAR-109m; B-05 URB-046/118b | Repair/impairment | Repair at P4.1 before P5; impairment after the strike; new lot, no reversal | B-10/B-05 | P4.1/P5 | Worked check (URB-118b) | Holds | **VERIFIED CONSISTENT** | — |
| X-33 | B-10 → B-05 | B-10 WAR-109f; B-05 URB-157(4) | — | Facilities are preserved; no deletion or transfer | B-10 | P5 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-34 | B-10 → B-05 | B-10 WAR-053a–l, F-WR-036; B-05 URB-157 | Military demand | Ammunition, gasoline, steel, aluminum and food demand | B-10 | P3.7/P5 | Rule comparison | Holds as a contract | **VERIFIED WITH DOCUMENTED LIMITATION** | The demand quantities are B-10-owned and provisional; no playtest exists |
| X-35 | B-10 → B-04 | B-10 WAR-053l; B-04 ECN-081 | Military food | Ration at P3.7 6(a), never added to civilian demand | B-10/B-04 | P3.7 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-36 | B-11 → B-05 | B-05 URB-158 | — | Rewards may grant crowns, resources, RP or a one-time programme only via a keyed event | B-11 | P4 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-37 | B-11 → B-05 | B-05 URB-158; B-04 ECN-108 | National wealth | Rankings may use national wealth; capacity/housing/RP are statistics, not buyable scores | B-11/B-04 | P3.8 | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-38 | B-12 → B-05 | B-05 URB-159 | — | A correction is a reversal; removing a facility also reverses the value it created | B-12 | Any | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |
| X-39 | B-12 → B-05 | B-05 URB-143/159 | F-CI-001/002/019 | No operator edits capacity, housing or fixed-asset book value in place | B-12 | Any | Rule comparison | Holds | **VERIFIED CONSISTENT** | — |

**Status totals:** 33 / 4 / 2 / 0 — 33 `VERIFIED CONSISTENT`, 4 `VERIFIED WITH DOCUMENTED LIMITATION`, 2 `CONTRADICTION IDENTIFIED`, 0 `NOT YET VERIFIED`; **sum = 39**, equal to the 39 matrix rows above. The two contradictions are `X-12` (C-14C-02) and `X-15` (C-14C-01); they are also recorded in the separate §12 register and are **not** counted again as matrix rows. The 14B historical 35-row matrix and its 18-entry register are not reused here.

---

## 12. Contradiction and limitation register

### 12.1 Contradictions (separately counted; 2)

| ID | Exact conflicting rules and locations | Affected systems | Severity | Actual owner | Economic/gameplay consequence | Proposed correction or ownership handoff | Within Prompt 14C authority? |
|---|---|---|---|---|---|---|---|
| C-14C-01 | B-04 ECN-028 says gasoline's sinks are "military fuel (B-10 supply bundles) and trade", and that the construction-fuel role was not adopted; B-05 URB-107 requires **50 gasoline** as a material for `prg_survey` (and `F-CI-024`) | B-04 roster; B-05 programmes | Low | **B-04** (roster statement) | The roster understates gasoline demand by one programme sink; a player reading only ECN-028 may under-invest in refining. No value is created or destroyed | B-04 revision adds "national-programme materials" to the gasoline sink list; B-05's 50-gasoline cost is unchanged. Handoff only; no edit by 14C | **No** — B-04 owns the roster and Prompt 14B is closed |
| C-14C-02 | B-04 register **F-EC-026** expresses `fixed_asset_book_value = Σ_completed_construction(crown + materials)`; B-04 **ECN-108** defines it as the sum of **city infrastructure carrying values** plus other recognised fixed assets, with impairment; B-05 **F-CI-019**/URB-118a/b implement the carrying-value and impairment model | B-04 register; B-04 rulebook; B-05; B-10 | **High** (coherence) | **B-04 register** (stale expression) | If implemented from F-EC-026, every infrastructure upgrade (up to 15,750 crowns) would be omitted from fixed assets and every `OP-05` strike would fail to impair book value; national wealth and the warfare accounting would be wrong | Restate F-EC-026 as `Σ_city infrastructure_carrying_value + Σ_other book_value(asset)` with impairment and the zero-cost opening lot, matching ECN-108/F-CI-019; no numeric change. Handoff only; no edit by 14C (B-04-owned, 14B closed) | **No** |

### 12.2 Documented limitations (not contradictions; not counted as matrix rows)

| ID | Limitation | Severity | Owner | Disposition |
|---|---|---|---|---|
| L-14C-01 | The founding book value (1,000 crowns + 140 steel) is recorded in "other recognised fixed assets" but no subledger category is named for it; a city is never demolished, so it never retires | Low | B-05 | Recorded; a future B-05 revision may name a city-founding lot. No value changed |
| L-14C-02 | When the lab or civic upkeep is only partly affordable, the B-05 rule says the institute/civic "produces no RP"/"housing is not counted"; whether the obligation is per facility or per class is not explicit. The simulation uses the conservative class-level obligation | Medium | B-05/B-04 | Recorded; a future clarification should choose per-facility or per-class and state it in URB-120. No value changed |
| L-14C-03 | F-CI-034's simplified payback omits RP, lab capex/upkeep, utilisation and demand; 14C publishes the extended framework (§8.6) without changing the formula | Medium | B-05 | Recorded; formula intact; the extended framework is analytical guidance |
| L-14C-04 | URB-129's "can afford exactly one of" is illustrative; other combinations (e.g. coal plant + farm + warehouse, or steel mill + farm) are affordable with 1,500 crowns and 20 steel | Low | B-05 | Recorded; no rule depends on the sentence. No edit |
| L-14C-05 | No NPC demand exists; reference-price sales are a labelled scenario assumption. A real world's industrial cash flow depends on B-07 players and B-10 warfare | High (interpretation) | B-07/B-10 | Recorded in every simulation result; no NPC demand is invented |
| L-14C-06 | The 24-hour city-rename cooldown is real elapsed time in an otherwise turn-based document; it has no economic effect | Informational | B-05 | Recorded; cosmetic only |
| L-14C-07 | Six formula/rule-embedded parameter groups are not separate inventory records; they are fully specified in Annex A under the established constant-table convention | Low | B-14/B-05 | Recorded; no count change; promotion would require a cross-system convention decision |

**Prompt 14B technical debt preserved.** The two internal documentation-validator limitations disclosed and accepted during Prompt 14B closeout remain technical debt; this phase did not create another correction cycle for them.

---

## 13. B-14 reconciliation and change crosswalk

### 13.1 Formula master inventory

The B-05 section of [`22_formula_master_inventory.md`](22_formula_master_inventory.md) was re-verified: **41 index rows + 41 field-level rows**, all identifiers unique, all names and source sections matching the B-05 register, no missing or duplicated active record. The 11 analytical/governance entries (`F-CI-031`…`F-CI-041`) keep their recorded metadata gaps, which 14C classifies as **expected non-executable metadata** rather than omissions: an analytical or governance entry has no inputs, output, rounding or timing to state. No formula record was added, retired or renamed; the global count remains **295**.

### 13.2 Numerical parameter inventory

[`22_numerical_parameter_inventory.md`](22_numerical_parameter_inventory.md) §7 was recounted at **73 records**, verified 1:1 against register §3, with metadata complete and no value changed. A 14C reconciliation note is added to §7 pointing to this report's Annex A for the six embedded groups. The global record count remains **393**.

### 13.3 Numerical baseline QA report and canonical B-14 document

[`22_numerical_baseline_qa_report.md`](22_numerical_baseline_qa_report.md) gains a Prompt 14C execution record with the actual results, the 39-row matrix tally and the separate contradiction register. [`22_formulas_and_balance.md`](22_formulas_and_balance.md) gains a §20 "Prompt 14C — B-05 reconciliation status" section that records what was reconciled, what was not established and the next subphase; its existing architecture and §19 are preserved.

### 13.4 Complete change crosswalk

**No numerical value changed in Prompt 14C.** The crosswalk records the documentation and metadata changes only:

| Change ID | Formula ID | Parameter | Old value | New value | Owning source | Formula master | Parameter inventory | Baseline QA | Worked examples | Decisions | Validator | Status | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CH-14C-01 | F-CI-031…041 | Classification | Not classified by type in the register | Analytical (031–034) / governance (035–041) recorded in this report and the master inventory note | B-05 register | B-05 §4.2 note | n/a | 14C record | E8, §8.6 | D-244/DD-290 | 14C-01, 14A-29 | Confirmed | None; no executable field claimed |
| CH-14C-02 | — | 73 B-05 records | 73 | 73 (verified; 0 changed) | B-05 §3 | n/a | §7 note | 14C record | §3.4 Annex A | D-245/DD-291 | 14C-02, 14C-03 | Confirmed | Six embedded groups remain outside the record count |
| CH-14C-03 | F-CI-034 | Research payback (analytical) | Unchanged | Unchanged; extended framework published in §8.6 | B-05 register | B-05 §5 | n/a | 14C record | E8, E9 | D-246/DD-292 | 14C-06 | Confirmed | Framework is analytical, not a formula |
| CH-14C-04 | — | 14C findings | — | F14C-01…12 recorded | This report | n/a | n/a | 14C record | §6, §10 | D-246/DD-292 | 14C-08 | Confirmed (analysis) | Balance and playtesting remain open |
| CH-14C-05 | F-EC-026 (B-04) | Fixed-asset expression | Construction-only expression | **Not changed by 14C**; contradiction C-14C-02 handed to B-04 | B-04 | B-04 §4 | n/a | 14C matrix | — | — | 14C-09 matrix | Handoff | B-04 must correct its own register |
| CH-14C-06 | — | Gasoline sink roster | — | **Not changed by 14C**; contradiction C-14C-01 handed to B-04 | B-04 | B-04 §3 | n/a | 14C matrix | — | — | 14C-09 matrix | Handoff | B-04 must correct its own roster |

**Traceability statement.** Every proposed change is a documentation/metadata change and is traced to the authoritative source, the master inventory, the parameter inventory, the QA report, the examples, the decision record and a validator. **No numerical value or formula structure changed; no untraceable change exists.**

---

## 14. Validation and actual results

### 14.1 Executed commands

Run from `docs/` on 2026-11-18 after the report and the B-14/continuity edits. Each row is an actual execution, not a recollection; no output is fabricated.

| # | Command | Actual result | Exit |
|---:|---|---|---:|
| 1 | `python qa_backups/verify_city_numbers.py` | **PASS: 267/267** city arithmetic checks | 0 |
| 2 | `python qa_backups/verify_economy_numbers.py` | **PASS: 170/170** economy arithmetic checks | 0 |
| 3 | `python qa_backups/14B_verify_b04_economy.py` | **ALL CHECKS PASSED** (321/321 internal checks; 30-turn produce 1,530/4,386, idle 3,713/4,133) | 0 |
| 4 | `python qa_backups/14A_validate_numerical_foundation.py` | **CHECKS: 64, FAILED: 0 — RESULT: PASS** (documentary consistency only) | 0 |
| 5 | `python qa_backups/14C_verify_b05_cities.py` | **10/10 checks passed; 5/5 self-tests passed** | 0 |
| 6 | `python qa_backups/14C_simulate_b05.py` | 24 scenarios × 10/30/60/120 turns; **0 invariant problems** | 0 |
| 7 | `python qa_backups/test_decision_registers.py` | **Ran 12 tests — OK** | 0 |
| 8 | `python qa_backups/test_next_action.py` | **Ran 27 tests — OK** | 0 |
| 9 | `python qa_backups/validate_links.py` | **0 unresolved**; 382 external skipped; 34 anchors checked | 0 |
| 10 | `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** | 0 |
| 11 | `python qa_backups/09_validate.py` | **371/371 checks passed — ALL CHECKS PASSED** | 0 |
| 12 | `python qa_backups/12A_validate_foundations.py` | **45/45 checks passed — RESULT: PASS** (documentation quality only) | 0 |
| 13 | `python qa_backups/13A_validate_ui_foundations.py` | **34/34 checks passed — RESULT: PASS** (documentation level) | 0 |
| 14 | `python qa_backups/13B_validate_ui_specifications.py` | **28/28 checks passed — RESULT: PASS** (documentation level) | 0 |
| 15 | `python qa_backups/verify_politics_numbers.py` | **878/879 — 1 inherited failure** (progress-log row 10 wording) | 1 |
| 16 | `python qa_backups/11A_validate_research.py` | **29/30 — 1 inherited failure** | 1 |
| 17 | `python qa_backups/09A_validate_alliance.py` | **941/943 — 2 inherited failures** (handoff/status) | 1 |
| 18 | `python qa_backups/09B_validate_alliance_semantic.py` | **8 inherited frozen-range defects** (D-219/DD-267/tally/status expectations) | 1 |

### 14.2 Focused numerical tests added by 14C

`14C_verify_b05_cities.py` recomputes (with fail-capable assertions): city founding costs 2–12 and the 103,290 total; the infrastructure milestone curve (90/330/750/2,250/12,750/16,170/15,750/1,000/6,250) and the Civil Survey and 2,000-bp cap cases; capacity and housing; the 70 > 60 limit tension; warehouse and upkeep ranges; all 17 building book values; the base and loaded margin tables; the food/steel/aluminum/ammunition/refining package margins and capex; the 448 RP / 3,180 crown tree; durations at 1/2/4/6/12/24 labs; lab cost totals; programme costs; the 12 worked examples; the simulation anchors (S01 = 14B exactly; steel-with-demand vs no-demand; power overbuild; overextended treasury; 12-lab tree; civic-unfunded crowding at 75,000; steel ahead of aluminum; menu ordering); and the report matrix totals.

### 14.3 What the arithmetic does not prove

No formula has been implemented, migrated, scheduled or runtime-tested. The T05 specifications remain **0 of 64 executed**. The simulation is deterministic arithmetic, not gameplay. The standard start is not balance-accepted. Passing validators is documentation and numerical evidence, not implementation or player acceptance.

### 14.4 Inherited historical failures

The four inherited historical validator failures recorded by Prompt 14B remain relevant and are not B-05 regressions: `verify_politics_numbers.py` (**878/879** — progress-log row 10 wording), `11A_validate_research.py` (**29/30**), `09A_validate_alliance.py` (**941/943** — handoff and status-block prompt expectations) and `09B_validate_alliance_semantic.py` (**8 semantic defects**, all frozen scope expectations: DECISIONS D-001..D-219/246 rows, DD-001..DD-267/292 rows, DD status tallies 52/79/267, and an old `stage_2_next_prompt` list). They are recorded as history, not repaired in this phase. The 14B documentation-validator technical debt is untouched. All other executed validators pass; the expectation advances in `09_validate.py`, `12A`, `13A`, `13B` and `validate_final.py` deleted or relaxed no check.

---

## 15. Completion assessment and remaining work

### 15.1 Completion categories

| Category | Status |
|---|---|
| Documentation (all 41 formulas, 73 records, 17 buildings, 12 technologies, 4 programmes, 39 matrix rows, 2 contradictions, 7 limitations) | **COMPLETE** |
| Numerical analysis (city, infrastructure, buildings, industry, housing, research, payback) | **COMPLETE** |
| Simulation (24 scenarios × 4 horizons, invariants, failure cases) | **EXECUTED** |
| Document validation (city, economy, 14B, 14A, 14C, decisions, next action, links, final) | **EXECUTED (§14)** |
| Runtime implementation | **NOT STARTED / NOT VERIFIED** |
| Balance acceptance | **NOT CLAIMED** |
| Player playtesting | **NOT EXECUTED** |

### 15.2 Acceptance criteria (27)

| # | Requirement | Status | Evidence |
|---:|---|---|---|
| 1 | All 41 F-CI identifiers assessed and classified | **MET** | §2 |
| 2 | All B-05 parameter records recounted and reconciled | **MET** | §3 |
| 3 | Parameter authority and numerical status verified | **MET** | §3.2 |
| 4 | City founding economics calculated | **MET** | §4.1, E2 |
| 5 | Infrastructure costs and capacity efficiency evaluated | **MET** | §4.2, E3 |
| 6 | All 17 building types examined | **MET** | §5.1 |
| 7 | Maintenance and operating costs assessed | **MET** | §5.2, §6 |
| 8 | Production capacity and industrial profitability analyzed | **MET** | §6 |
| 9 | Steel and aluminum margins tested | **MET** | §6.6, E7, S19/S20 |
| 10 | Population and housing dependencies reconciled | **MET** | §7, S15 |
| 11 | All 12 technologies assessed | **MET** | §8.1 |
| 12 | All four national programmes evaluated | **MET** | §8.4 |
| 13 | Research duration, costs and payback calculated | **MET** | §8.1–8.3, E8/E9 |
| 14 | Investment opportunity costs compared | **MET** | §4.3, §6.4, E10 |
| 15 | At least ten new integrated worked examples | **MET** | §9 (E1–E12) |
| 16 | 10/30/60/120-turn simulations executed | **MET** | §10 |
| 17 | Economic exploit and failure analysis completed | **MET** | §6.7, §10.4 |
| 18 | Formal cross-system dependency matrix completed | **MET** | §11 |
| 19 | Status totals independently reconciled | **MET** | 33/4/2/0 = 39 (14C-09) |
| 20 | Separate contradiction register maintained | **MET** | §12 |
| 21 | Every change cross-referenced to B-14 | **MET** | §13.4 |
| 22 | Formula master inventory reconciled | **MET** | §13.1 |
| 23 | Numerical parameter inventory reconciled | **MET** | §13.2 |
| 24 | Numerical baseline QA report updated | **MET** | §13.3 |
| 25 | Relevant validators and tests actually executed | **MET** | §14 |
| 26 | Historical limitations and playtesting requirements recorded | **MET** | §14.4, §15.3 |
| 27 | Completion report and continuity files updated | **MET** | This report; §16; continuity files |

### 15.3 Remaining playtesting requirements

1. A **30-turn standard-start playtest** of each early path (food, lab, second city, four farms), measuring cash, wealth, food security and the first shortage.
2. A **100-turn two-nation trade pair** testing whether steel's construction demand and refining's gasoline market produce the intended specialisation.
3. A **100-turn 12-city development test** of the gate cost (12,340), construction slots, per-city limits and the 500 cap.
4. A **steel-demand test**: construction-heavy, war-heavy and market-heavy worlds, measuring steel price, inventory accumulation and the steel package's cash payback.
5. An **aluminum-demand test** after `tech_ind_chem`, measuring whether the second chain earns its 5,530 book.
6. A **housing-and-food growth test** (civic centres + farms) over 70 turns, confirming the occupancy ramp and the hunger penalty.
7. A **research-speed test** comparing 1, 2 and 12 labs, with real opportunity cost and a demolition decision.
8. A **power utilisation test** at 25/50/75/100% and the 66% one-batch cliff.
9. A **warfare-damage test** of `OP-05`, repair and the carrying-value impairment once B-04's F-EC-026 is corrected.
10. A **market-price test** (steel 6/7/8, aluminum 7/8/9, gasoline 5/6/7) to confirm the break-evens and the refining role.

### 15.4 Remaining limitations

No runtime; no balance acceptance; no playtest; B-05 register remains Draft; the 64 T05 tests are unexecuted; the two B-04 contradictions and seven limitations above; the 14B technical debt; the four inherited validator failures; the six embedded parameter groups outside the record count; and the owner's acceptance is not claimed.

### 15.5 Recommended next action (not authorized here)

The owner should review this report and the resulting snapshot. If accepted, the next authorized subphase is **Prompt 14D** — not started and not authorized by this document. Implementation must wait for the owner's acceptance of the full Prompt 14 numerical foundation; the two B-04 contradictions (C-14C-01, C-14C-02) should be corrected by B-04's owner before any implementation of fixed-asset accounting or the programme material roster.

---

## 16. Git closeout

**Branch:** `main`. **HEAD at start:** `3b9cadc`. **Staged:** 0. **No staging, commit, checkout, reset, clean, stash, branch or push was performed.** The owner retains commit authority.

**Working-tree state at the end of Prompt 14C (read-only `git status --porcelain`): 20 modified tracked paths, 6 untracked files, 26 individual paths, 0 staged changes.**

| # | Modified tracked path | Nature |
|---:|---|---|
| 1 | `docs/AI_CONTEXT.md` | 14C current banner and status block |
| 2 | `docs/AI_HANDOFF.md` | current position, decision count and next action |
| 3 | `docs/DECISIONS.md` | D-244…D-246 |
| 4 | `docs/PROJECT_PROGRESS.md` | status block and Prompt 14 row |
| 5 | `docs/prompts/INDEX.md` | 14C archive row |
| 6 | `docs/qa_backups/09_validate.py` | decision/DD expectation advance |
| 7 | `docs/qa_backups/12A_validate_foundations.py` | decision-range expectation advance |
| 8 | `docs/qa_backups/13A_validate_ui_foundations.py` | date, DD and decisions-range expectation advance |
| 9 | `docs/qa_backups/13B_validate_ui_specifications.py` | date, D/DD counts and range expectation advance |
| 10 | `docs/qa_backups/validate_final.py` | DD count and word-map expectation advance |
| 11 | `docs/stage-2/00_stage_2_handoff.md` | next action and Prompt 14 table |
| 12 | `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 14 row |
| 13 | `docs/stage-2/04_approved_and_provisional_decisions.md` | DD-290…DD-292 |
| 14 | `docs/stage-2/06_stage_2_progress_log.md` | §117 |
| 15 | `docs/stage-2/22_formula_master_inventory.md` | B-05 reconciliation note |
| 16 | `docs/stage-2/22_formulas_and_balance.md` | §20 B-05 status |
| 17 | `docs/stage-2/22_numerical_baseline_qa_report.md` | 14C execution record |
| 18 | `docs/stage-2/22_numerical_contracts/evidence_mappings.json` | controlled-evidence hash refresh for the amended B-14 document; all mappings remain `NOT_REVIEWED` |
| 19 | `docs/stage-2/22_numerical_contracts/index.json` | source-document and evidence-mapping hash refresh; preserved 295/393 baseline unchanged |
| 20 | `docs/stage-2/22_numerical_parameter_inventory.md` | §7 14C recount note |

| # | Untracked file | Purpose |
|---:|---|---|
| 1 | `docs/prompts/prompt_14C_b05_cities_infrastructure_production_research.md` | archived assignment (42,766 bytes; 1,533 LF; SHA-256 `47aa595c…`) |
| 2 | `docs/qa_backups/14C_verify_b05_cities.py` | 14C numerical/document verifier (10 checks; 5 self-tests) |
| 3 | `docs/qa_backups/14C_simulate_b05.py` | B-05 deterministic reference model (24 scenarios) |
| 4 | `docs/qa_backups/14C_simulation_results.json` | model output for the 24 scenarios × 4 horizons |
| 5 | `docs/qa_backups/14C_simulation_console.txt` | model console record |
| 6 | `docs/stage-2/29_prompt_14C_b05_cities_completion_report.md` | this report |

**Controlled-evidence note.** The contract registry's whole-document hashes were refreshed because the legitimate 14C amendments changed `22_formulas_and_balance.md` and `DECISIONS.md`; the evidence excerpt, classification and `NOT_REVIEWED` review status are unchanged, and no human review or owner authorization is claimed.

**Generated cache artifacts.** `docs/qa_backups/__pycache__/` may contain refreshed `.pyc` files from the executed validators/imported model; they are generated, ignored by `.gitignore` (`__pycache__/`, `*.pyc`) and not substantive changes.

**B-04 preservation.** No B-04 formula, recipe, price, maintenance rate, tax value or rulebook text was edited. The two B-04 contradictions are handoffs (C-14C-01, C-14C-02). The B-04 and B-05 accepted decisions of Prompts 14A and 14B were not reopened.

**Validation at close.** City 267/267; economy 170/170; 14B 321/321; 14A 64/64; 14C 10/10 + 5/5 self-tests; simulation 24 scenarios and 0 invariant violations; `validate_final.py` ALL CHECKS PASSED; links 0 unresolved; decision registers 12/12; next action 27/27; `09_validate.py` 371/371; 12A 45/45; 13A 34/34; 13B 28/28. The four inherited failures remain (§14.4).

---

**End of Prompt 14C completion report.**
