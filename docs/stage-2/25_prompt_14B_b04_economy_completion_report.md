# Prompt 14B — B-04 economy, resources, income and treasury — completion report

**Stage:** Stage 2 · **Parent:** Prompt 14 · **Subphase:** 14B · **System:** B-04
**Executed:** 2026-11-17 · **Baseline:** Project X (109) audit snapshot, reconciled against the live repository
**Status:** **PROMPT 14B COMPLETE AT THE DOCUMENTATION, NUMERICAL-ANALYSIS AND DOCUMENT-VALIDATION LEVEL.** No B-04 formula has been implemented, run against a database or scheduler, or played. No value was retuned. The standard start is not balance-accepted.
**Authority:** explicit owner authorization dated 17 November 2026; [Prompt 14A acceptance record](24_prompt_14A_owner_acceptance.md); [D-014](../AUTONOMOUS_DECISION_POLICY.md).
**Read with:** [B-04 rulebook](10_economy_resources_treasury_and_finances.md) · [B-04 formula register](10_economic_formula_and_balance_register.md) · [B-14 canonical](22_formulas_and_balance.md) · [numerical baseline QA report](22_numerical_baseline_qa_report.md) · [`14B_verify_b04_economy.py`](../qa_backups/14B_verify_b04_economy.py)

---

## 1. Assignment scope and source reconciliation

### 1.1 What was executed

Prompt 14B covered the work authorized by the 17 November 2026 instruction:

1. Recorded Prompt 14A owner acceptance (17 November 2026) and created the acceptance record that the continuity files already referenced ([24_prompt_14A_owner_acceptance.md](24_prompt_14A_owner_acceptance.md)); recorded Prompt 14B authorization; preserved every Prompt 14A limitation; authorized no later subphase.
2. Reconciled the live repository against the Project X (109) baseline.
3. Verified the 47 active B-04 formula identifiers and the 49 B-04 numerical parameter records.
4. Completed the parameter-ownership and numerical-status gate before changing a value.
5. Built the cross-system dependency inventory, consistency matrix and dependency graph for B-02, B-03, B-05, B-06, B-07, B-08, B-09 and B-10.
6. Recounted every existing worked example, produced the seven required integrated examples (A–G) plus the full standard-start example (H), and re-ran the 30-turn money-creation test as a deterministic reference model.
7. Investigated margins, deficits, dominance, sustainability and exploit classes; recorded findings with severity, owner and proposed resolution.
8. Made only the corrections needed for cross-system coherence; **no tax, production, maintenance, recipe or reference-price coefficient was changed**.
9. Synchronized the B-04 rulebook, the B-04 formula register, the B-14 canonical document, the formula master inventory, the numerical parameter inventory and the numerical baseline QA report.
10. Executed the existing and new validators and recorded the actual results in §8.

### 1.2 Repository baseline reconciliation

| Check | Project X (109) baseline | Live repository | Result |
|---|---|---|---|
| Branch / HEAD at start | not recorded in the prompt | `main` / `bff9119` | reconciled |
| Pre-existing working-tree changes | — | 6 modified tracked files (continuity only: `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `prompts/INDEX.md`, `01_stage_2_prompt_roadmap.md`, `06_stage_2_progress_log.md`); 0 untracked | preserved; they record the 14A acceptance/14B authorization decision from a prior partial session |
| Missing referenced record | — | `stage-2/24_prompt_14A_owner_acceptance.md` was referenced by four files but did not exist | **created** by 14B |
| B-04 formula register | 47 active formulas | 47 active formulas | matches |
| B-04 parameter records | 49 | 49 | matches |
| Worked examples | 20 | 20 | matches |
| Resources / recipes / generators | 11 / 4 / 3 | 11 / 4 / 3 | matches |
| Starting bundle | 310 units, 1,500 crowns | 310 units, 1,500 crowns | matches |
| Economy validator | `PASS: 164/164` | `PASS: 170/170` after the 14B corrections (6 new guard checks) | reproduced and extended |
| Two-hour UTC settlement | present | present (`ECN-144`) | matches |

No legitimate newer B-04 change was found to overwrite. The only pre-existing difference was the missing acceptance record and the six continuity edits, both preserved and completed.

### 1.3 Source inventory

| Item | Count | Evidence |
|---|---:|---|
| Active B-04 formulas | **47** | `F-EC-001`…`F-EC-046` plus `F-EC-002a`; the `F-EC-000` series is register convention and excluded |
| B-04 parameter records | **49** | [numerical parameter inventory §6](22_numerical_parameter_inventory.md): 24 starting-bundle values + 7 extraction vectors + 4 recipe vectors + 3 generator vectors + 11 reference prices |
| Worked examples | **20** | B-04 §20, `### Example 1`…`### Example 20` |
| Resources | **11** | 7 raw + 4 manufactured (`ECN-023`/`ECN-024`) |
| Manufacturing recipes | **4** | refining, steel, aluminum, ammunition (`ECN-066`, D-046) |
| Generator classes | **3** | coal, oil, nuclear (`ECN-057`, D-048) |
| Standard starting bundle | **310 units, 1,500 crowns** | `ECN-121`, D-063 |
| Settlement architecture | **2-hour UTC, P3.1–P3.8** | `ECN-144`; B-02 `TR-040` |
| B-03 carry-in parameters | **20** | [numerical parameter inventory §4](22_numerical_parameter_inventory.md); none is a B-04 value |

### 1.4 Formula identity

Identifiers were preserved. No formula was renumbered, retired or added. `F-EC-002a` remains the one lettered identifier with its own separable computation; `F-EC-036`…`F-EC-046` remain analytical/governance entries, so the executable-formula count is 36 and the recorded active count is 47. The global B-14 count stays **295/295 active** and the parameter count stays **393** records.

### 1.5 Governance and decisions

[D-014](../AUTONOMOUS_DECISION_POLICY.md) was read in full and not modified. Four Category-B decision pairs were recorded (D-240…D-243; DD-286…DD-289) and are summarized in §7. No owner-reserved matter was resolved. The Alliance treasury question (`UD-046`), multiple membership (`UD-040`) and the owner-reserved Prompt 09 decisions remain Open exactly as recorded.

---

## 2. B-04 formula reconciliation

### 2.1 Field completeness (all 47 active identifiers)

Legend: **E** = expression, **I/O** = inputs and output, **U** = units, **R** = rounding, **T** = timing, **D** = dependencies, **C** = conditions/exceptions, **P** = parameter ownership, **S** = numerical status, **V** = validation evidence. `✓` means the field is present and agrees with the canonical register; `c` means it was corrected/clarified by 14B; `n/a` means the identifier is a governance entry with no executable field.

| ID | Name | E | I/O | U | R | T | D | C | P | S | V | 14B note |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| F-EC-001 | Tax income | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-06 | PROVISIONAL VALUE | T04-B01 | B-06's policy set is {200,300,400}; see X-20 |
| F-EC-002 | Food demand | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-06 | PROVISIONAL VALUE | T04-C01 | — |
| F-EC-002a | Military Food demand | c | c | c | c | c | c | c | B-10 | UNSPECIFIED (no local value) | 10B validator + 14B Ex F | full field table added |
| F-EC-003 | Hunger penalty | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-C02/C03 | protected-civilian model verified |
| F-EC-004 | Extraction batches | c | c | ✓ | ✓ | ✓ | c | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-D01/C04 + 14B | consumes `yield_bonus` |
| F-EC-005 | Extraction variable cost | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B02 | — |
| F-EC-006 | Power demand | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-D05 | `M + A ≤ C` verified |
| F-EC-007 | Power percentage | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-D05 | — |
| F-EC-008 | Batches available | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-D05 | — |
| F-EC-009 | Input limit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-D07 | — |
| F-EC-010 | Money limit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B06 | — |
| F-EC-011 | Space limit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-C04 | — |
| F-EC-012 | Processing output | c | c | ✓ | ✓ | ✓ | c | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-D07 | consumes `yield_bonus` |
| F-EC-013 | Generator output and fuel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-D06 | fail-closed verified |
| F-EC-014 | Maintenance | c | c | ✓ | ✓ | c | c | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-B02 + 14B | consumes `standards_bonus`; facility upkeep excluded |
| F-EC-015 | Gross income | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-11 | PROVISIONAL VALUE | T04-B02 | — |
| F-EC-016 | Net operating income | c | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B02/B03 | `net economic result` published |
| F-EC-017 | Net cash flow | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B05 | — |
| F-EC-018 | Closing treasury | c | c | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 + all systems | PROVISIONAL VALUE | T04-B05/B06 + 14B | `operating` defined to include P3.7 obligations |
| F-EC-019 | Available balance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-02 | PROVISIONAL VALUE | T04-D03 | — |
| F-EC-020 | Reserved total | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-02 | PROVISIONAL VALUE | T04-D03/D04 | — |
| F-EC-021 | Inventory total | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-C05 | — |
| F-EC-022 | Inventory available | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-D03 | — |
| F-EC-023 | Free warehouse space | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-C04 | — |
| F-EC-024 | National wealth | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B08 | — |
| F-EC-025 | Inventory book value | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B08 | — |
| F-EC-026 | Fixed-asset book value | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-B04 | example uses farm 155 |
| F-EC-027 | Construction book value | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-B04 | example uses farm 155 |
| F-EC-028 | Trade fee | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-07 | PROVISIONAL VALUE | T04-F04 | fee is 0 at launch (B-07 MKT-068) |
| F-EC-029 | Transfer conservation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-07/B-08 | PROVISIONAL VALUE | T04-F04 + 14B Ex D | — |
| F-EC-030 | Money conservation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-I03 + 14B | — |
| F-EC-031 | Reference margin per batch | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-H04/I02 + 14B | actual-power note added at F-EC-037 |
| F-EC-032 | Payback turns | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04/B-05 | PROVISIONAL VALUE | T04-B04 | example 23 turns |
| F-EC-033 | Settlement event key | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-02 | PROVISIONAL VALUE | T04-F02 | hash choice remains Stage 5 |
| F-EC-034 | Settlement idempotency key | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-02 | PROVISIONAL VALUE | T04-E02 | — |
| F-EC-035 | Wealth reconciliation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B-04 | PROVISIONAL VALUE | T04-B08 | — |
| F-EC-036 | Base margin table | ✓ | ✓ | ✓ | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | 14B §4.5 | analytical entry |
| F-EC-037 | Power cost is separate | c | ✓ | ✓ | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | 14B §4.4 | utilisation distinction added |
| F-EC-038 | Dominance test | ✓ | ✓ | ✓ | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | 14B §4.5 | re-run; no formal dominance |
| F-EC-039 | Money-creation test | c | ✓ | ✓ | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | 14B §4.9 | 30-turn measurement added |
| F-EC-040 | Examples are not a simulation | ✓ | n/a | n/a | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | this report | preserved |
| F-EC-041 | Changing a number | ✓ | n/a | n/a | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | this report | preserved |
| F-EC-042 | Changing a formula | ✓ | n/a | n/a | n/a | n/a | ✓ | n/a | B-04 | UNSPECIFIED | this report | preserved |
| F-EC-043 | Adding a formula | ✓ | n/a | n/a | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | this report | no formula added |
| F-EC-044 | Revision history | c | n/a | n/a | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | this report | v1.5 entry added; old expressions preserved |
| F-EC-045 | Validation record | c | n/a | n/a | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | §8 | 14B results appended |
| F-EC-046 | What is not validated | ✓ | n/a | n/a | n/a | n/a | ✓ | ✓ | B-04 | UNSPECIFIED | this report | preserved and extended by ECN-228 |

**Result:** 36 executable identifiers and 11 analytical/governance identifiers are accounted for; no field is silently missing. The only substantive field corrections are the four marked `c` in the executable set (F-EC-004, F-EC-012, F-EC-014, F-EC-018) plus the F-EC-002a table completion; each is a cross-system contract completion, not a coefficient change.

### 2.2 Conditions, exceptions and change control

- **Whole-obligation maintenance** (`ECN-147a`) was verified against F-EC-014 and the standard-start allocation (`1 crown → oil`; five chains `UNMAINTAINED`).
- **Manual capacity** (`M + A ≤ C`) was verified against F-EC-006, `ECN-053`/`ECN-060` and B-05's `URB-050`.
- **Power derating** (`floor(C × pct / 10,000)`) was verified; a level-1 chain at 60% runs 0.
- **F-EC-041/042/043** change-control rules were preserved: no number changed without a decision; no formula meaning changed without preserving the previous expression; no new formula ID was added.
- **F-EC-044** now records v1.5 and the previous expressions for F-EC-004, F-EC-012 and F-EC-014.
- **F-EC-046** remains the non-validation statement; `ECN-228` extends it with the 14B limitations.

### 2.3 The 49 B-04 parameter records — ownership and status

Every record retains `PROVISIONAL VALUE`; none is promoted. The reading key **R-01…R-49** is local to this report and is not an identifier namespace (the source rows have no identifier; the inventory's rule is "no competing global namespace").

| Key | Parameter (source row) | Value | Unit | Source | Decision owner | Formula dependencies | Cross-system dependency | Timing | Evidence | Required future validation | Status |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| R-01 | Treasury | 1,500 | crowns | B-04 §3.1 | B-04 structure; Prompt 14 calibration | none directly | B-03 creation | creation | `verify_economy_numbers.py` | 30-turn playtest | PROVISIONAL VALUE |
| R-02 | Population | 50,000 | people | B-04 §3.1 | B-06 structural; Prompt 14 calibration | F-EC-001/002 | B-06 | creation; frozen at P3 | validator | B-06 growth model | PROVISIONAL VALUE |
| R-03 | Warehouse capacity | 2,000 | units | B-04 §3.1 | B-04 structure; B-05 expansion | F-EC-023 | B-05 `F-CI-014` | creation | validator | storage playtest | PROVISIONAL VALUE |
| R-04 | Tax rate | 300 | bp | B-04 §3.1 | B-06 policy ({200,300,400}) | F-EC-001 | B-06 DMP-095 | P3.1 | validator | B-06 balance | PROVISIONAL VALUE |
| R-05 | Stability factor | 10,000 | bp | B-04 §3.1 | B-06 | F-EC-001 | B-06 F-PD-017 | P3.1 | validator | B-06 balance | PROVISIONAL VALUE |
| R-06 | Food stock | 120 | units | B-04 §3.1 | B-04 | F-EC-003/021 | — | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-07 | Coal stock | 60 | units | B-04 §3.1 | B-04 | F-EC-013/021 | — | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-08 | Oil stock | 30 | units | B-04 §3.1 | B-04 | F-EC-012/021 | — | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-09 | Iron stock | 30 | units | B-04 §3.1 | B-04 | F-EC-012/021 | — | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-10 | Bauxite stock | 20 | units | B-04 §3.1 | B-04 | F-EC-012/021 | — | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-11 | Lead stock | 10 | units | B-04 §3.1 | B-04 | F-EC-012/021 | — | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-12 | Uranium stock | 0 | units | B-04 §3.1 | B-04 | F-EC-021 | — | creation | validator | nuclear playtest | PROVISIONAL VALUE |
| R-13 | Gasoline stock | 20 | units | B-04 §3.1 | B-04 | F-EC-021 | B-10 fuel demand | creation | validator | military playtest | PROVISIONAL VALUE |
| R-14 | Ammunition stock | 0 | units | B-04 §3.1 | B-04 | F-EC-021 | B-10 | creation | validator | military playtest | PROVISIONAL VALUE |
| R-15 | Steel stock | 20 | units | B-04 §3.1 | B-04 | F-EC-021/027 | B-05 construction | creation | validator | construction playtest | PROVISIONAL VALUE |
| R-16 | Aluminum stock | 0 | units | B-04 §3.1 | B-04 | F-EC-021 | B-05 advanced construction | creation | validator | construction playtest | PROVISIONAL VALUE |
| R-17 | Food capacity | 3 | batches | B-04 §3.1 | B-04/B-05 | F-EC-004/014 | B-05 farms | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-18 | Coal capacity | 2 | batches | B-04 §3.1 | B-04/B-05 | F-EC-004/014 | B-05 mines | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-19 | Oil capacity | 1 | batch | B-04 §3.1 | B-04/B-05 | F-EC-004/014 | B-05 wells | creation | validator | refinery sustainability | PROVISIONAL VALUE |
| R-20 | Iron capacity | 1 | batch | B-04 §3.1 | B-04/B-05 | F-EC-004/014 | B-05 mines | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-21 | Bauxite / lead / uranium capacity | 0 | batches | B-04 §3.1 | B-04/B-05 | F-EC-004/014 | B-05 mines | creation | validator | early-game playtest | PROVISIONAL VALUE |
| R-22 | Refining capacity | 1 | batch | B-04 §3.1 | B-04/B-05 | F-EC-008/014 | B-05 refinery | creation | validator | 30-turn model | PROVISIONAL VALUE |
| R-23 | Steel / aluminum / ammunition capacity | 0 | batches | B-04 §3.1 | B-04/B-05 | F-EC-008/014 | B-05 mills | creation | validator | early-game playtest | PROVISIONAL VALUE |
| R-24 | Coal generator | 1 | level | B-04 §3.1 | B-04/B-05 | F-EC-013/014 | B-05 plant | creation | validator | power playtest | PROVISIONAL VALUE |
| R-25 | Food extraction vector | Y20 / V12 / M1 / P1 | units; crowns; crowns; crowns/unit | B-04 §3.2 | B-04 structure; Prompt 14 calibration | F-EC-004/005/031 | B-05 F-CI-015 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-26 | Coal extraction vector | Y10 / V10 / M1 / P1 | same | B-04 §3.2 | B-04 | F-EC-004/005/031 | B-05 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-27 | Oil extraction vector | Y8 / V14 / M1 / P2 | same | B-04 §3.2 | B-04 | F-EC-004/005/031 | B-05 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-28 | Iron extraction vector | Y10 / V10 / M1 / P1 | same | B-04 §3.2 | B-04 | F-EC-004/005/031 | B-05 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-29 | Bauxite extraction vector | Y8 / V14 / M1 / P2 | same | B-04 §3.2 | B-04 | F-EC-004/005/031 | B-05 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-30 | Lead extraction vector | Y6 / V16 / M1 / P3 | same | B-04 §3.2 | B-04 | F-EC-004/005/031 | B-05 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-31 | Uranium extraction vector | Y1 / V28 / M1 / P30 | same | B-04 §3.2 | B-04 | F-EC-004/005/031 | B-05 | P3.3 | validator | playtest | PROVISIONAL VALUE |
| R-32 | Refining recipe | 10 oil → 8 gasoline; V20; 2 GU; M2 | units; crowns; GU; crowns | B-04 §3.3 | B-04/D-046; numbers provisional | F-EC-006–012/031 | B-05 F-CI-016 | P3.5 | validator | playtest | PROVISIONAL VALUE |
| R-33 | Steel recipe | 10 iron + 6 coal → 8 steel; V24; 3 GU; M2 | same | B-04 §3.3 | B-04/D-046 | F-EC-006–012/031 | B-05 | P3.5 | validator | playtest | PROVISIONAL VALUE |
| R-34 | Aluminum recipe | 12 bauxite → 8 aluminum; V24; 4 GU; M2 | same | B-04 §3.3 | B-04/D-046 | F-EC-006–012/031 | B-05 | P3.5 | validator | playtest | PROVISIONAL VALUE |
| R-35 | Ammunition recipe | 8 lead + 4 coal → 10 ammunition; V20; 2 GU; M2 | same | B-04 §3.3 | B-04/D-046 | F-EC-006–012/031 | B-05 | P3.5 | validator | playtest | PROVISIONAL VALUE |
| R-36 | Coal generator vector | 6 GU; 6 coal; V10; M2 | GU; units; crowns; crowns | B-04 §3.4 | B-04/D-048 | F-EC-013/014 | B-05 plant | P3.4 | validator | power playtest | PROVISIONAL VALUE |
| R-37 | Oil generator vector | 6 GU; 5 oil; V14; M2 | same | B-04 §3.4 | B-04/D-048 | F-EC-013/014 | B-05 | P3.4 | validator | power playtest | PROVISIONAL VALUE |
| R-38 | Nuclear generator vector | 20 GU; 1 uranium + 1 lead; V40; M2 | same | B-04 §3.4 | B-04/D-048 | F-EC-013/014 | B-05 | P3.4 | validator | power playtest | PROVISIONAL VALUE |
| R-39 | Food price | 1 | crowns/unit | B-04 §3.5 | B-04/D-058 | F-EC-025/031/036/037 | B-07 band; B-10 reparations | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-40 | Coal price | 1 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-41 | Oil price | 2 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-42 | Iron price | 1 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-43 | Bauxite price | 2 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-44 | Lead price | 3 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-45 | Uranium price | 30 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-46 | Gasoline price | 6 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-47 | Steel price | 7 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-48 | Aluminum price | 8 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |
| R-49 | Ammunition price | 6 | crowns/unit | B-04 §3.5 | B-04 | same | B-07/B-10 | read at close | validator | market playtest | PROVISIONAL VALUE |

**Ownership gate result:** every record has a named decision owner, a formula dependency set, a cross-system dependency set, a timing position and a validation path. **No record was promoted to `OWNER-APPROVED VALUE`.** The three external owners that B-04 consumes without owning are B-05 (capacity, construction cost, research modifiers, facility upkeep), B-06 (population, tax policy set, stability, public-service cost) and B-10 (military ration quantity and consequences).

---

## 3. Starting national economic position

### 3.1 Opening position

| Item | Value | Calculation |
|---|---:|---|
| Opening treasury | **1,500 crowns** | D-063 |
| Population | **50,000** | D-063; B-06 owns it |
| Opening food demand | **50 units** | `ceil(50,000/1,000)` |
| Warehouse capacity | **2,000 units** | `ECN-121` |
| Opening inventory | **310 units** | `120+60+30+30+20+10+0+20+0+20+0` |
| Inventory book value | **600 crowns** | `120×1 + 60×1 + 30×2 + 30×1 + 20×2 + 10×3 + 20×6 + 20×7` |
| Fixed-asset book value | **0 crowns** | the nine starting facilities are a zero-cost opening lot (`URB-047`) |
| Opening national wealth | **2,100 crowns** | `1,500 + 600 + 0` |
| Warehouse utilisation | **1,550 bp (15.5%)** | `310 / 2,000` |
| Available warehouse space | **1,690 units** | `2,000 − 310` |
| Tax rate / stability | **300 bp / 10,000 bp** | D-063; B-06 |
| Expected base tax | **150 crowns** | `floor(50,000 × 300 × 10,000 / 1e9)` |
| Expected maintenance | **11 crowns** | food 3, coal 2, oil 1, iron 1, generator 2, refining 2 |
| Expected variable production | **110 crowns** | extraction 80 + generator 10 + refining 20 |
| Expected public-service cost | **30 crowns** | B-06 `floor(150 × 2,000/10,000)` at `STANDARD` |
| Expected power supply | **6 GU** | one coal level |
| Expected industrial demand | **2 GU** | one refining batch |
| Expected civilian food demand | **50 units** | `ceil(50,000/1,000)` |

### 3.2 Full standard-start turn (Example H, B-04 + B-06)

| Phase | Flow | Treasury |
|---|---|---:|
| Opening | — | 1,500 |
| P3.1 | Tax `floor(50,000×300×10,000/1e9) = 150`; hunger 0; alliance 0 | 1,650 |
| P3.2 | Maintenance 11 (six whole obligations, all paid) | 1,639 |
| P3.3 | Food 3×12 = 36; coal 2×10 = 20; oil 14; iron 10 | 1,559 |
| P3.4 | Coal generator: 6 coal + 10 crowns → 6 GU | 1,549 |
| P3.5 | Refining: 10 oil + 20 crowns → 8 gasoline; `power_pct` 100% | 1,529 |
| P3.6 | Food: `120+60−50 = 130`; unmet 0; hunger 0 | 1,529 |
| P3.7 | Public-service cost 30; no military obligation | **1,499** |
| P3.8 | Close: treasury 1,499; inventory 350 units; book 678; wealth 2,177 | — |

**Measures:** capacity-operating income **+29** (F-EC-016); net operating income after obligations **−1**; net cash flow **−1**; inventory book-value change **+78**; **net economic result +77**; gross production value **154 crowns** at reference prices.

### 3.3 Economic solvency and constraints

| Dimension | Finding |
|---|---|
| Solvency | **Solvent.** A −1 crown/turn cash drift gives roughly 1,499 turns of runway at the standard start; no insolvency risk in the first 30 turns. |
| Liquidity | **Cash-neutral.** The 30-crown service cost converts the former +29 cash surplus into −1. Wealth still rises by 77/turn. |
| Resource sufficiency | **Food sufficient** (60 produced vs 50 consumed; 120 opening stock). **Oil is the binding input**: 8 produced vs 10 refined; the starting 30 oil is a 15-turn bridge (see F14B-03). |
| Production constraints | Capacity, not money or space, binds every extraction chain in the first turns. |
| Power constraints | No shortfall; 4 of 6 GU are surplus and discarded. |
| Storage constraints | 1,690 free units; +40 units/turn while refining runs; the wall is ~42 turns away if nothing is sold (extrapolated, not simulated beyond 30). |
| Shortage exposure | Food is secure; oil/refining is the first structural shortage; a 5-unit food shortfall would produce a 300 bp penalty. |
| Development constraints | The capital has 15 DC and the granted facilities use 11, leaving 4 DC; one refinery (2 DC) plus one farm (1 DC) fits; a second steel mill would not. |

### 3.4 Wealth versus cash

The opening 2,100 wealth is **not** 2,100 spendable crowns: 600 is inventory book value and 0 is fixed assets. The 1,500 crown treasury is the only liquid balance. A reserve reduces available cash without changing wealth. A sale converts inventory book value into cash at the negotiated price and can raise or lower wealth; it never mints value (`ECN-027`, `ECN-099`, Example 20).

---

## 4. Economic analysis

### 4.1 Taxation

`tax_income = floor(population × tax_rate_bp × stability_factor_bp / 1,000,000,000)`, with the stored hunger penalty applied as `base_tax × (10,000 − hunger_bp) / 10,000` before the floor (`F-EC-001`, `F-EC-003`, `ECN-146`).

| Case | Population | Rate | Stability | Hunger | Tax |
|---|---:|---:|---:|---:|---:|
| Standard start | 50,000 | 300 | 10,000 | 0 | **150** |
| 100,000 people, no hunger | 100,000 | 300 | 10,000 | 0 | **300** |
| 100,000, 600 bp hunger | 100,000 | 300 | 10,000 | 600 | **282** |
| Full starvation | 50,000 | 300 | 10,000 | 3,000 | **105** |
| `LOW` fiscal setting | 50,000 | 200 | 10,000 | 0 | **100** |
| `HIGH` fiscal setting | 50,000 | 400 | 10,000 | 0 | **200** |

The formula is linear in population and rate and floored once; the hunger factor is applied before the floor. B-06's policy set is `{200, 300, 400}` bp, so the formula's mathematical domain (0…10,000) is wider than the player-reachable set; that is a domain-versus-policy distinction, not a contradiction (X-20). The standard start's tax is 3 crowns per 1,000 people per turn.

### 4.2 Food

| Case | Opening | Produced | Demand | Consumed | Unmet | Hunger (next turn) |
|---|---:|---:|---:|---:|---:|---:|
| Standard start | 120 | 60 | 50 | 50 | 0 | 0 |
| Example C (100,000 people) | 20 | 60 | 100 | 80 | **20** | **600 bp** |
| OP-09 holding 4, stock 54 | 54 | 0 | 50 | 50 | 0 | 0 (reservation stands) |
| OP-09 holding 4, stock 49 | 49 | 0 | 50 | 49 | **1** | **60 bp** (reservation released) |
| Total shortage | 0 | 0 | 50 | 0 | **50** | **3,000 bp** |

Civilian Food is protected before any `OP-09` field ration (`ECN-081`/`ECN-082`). The military ration is separate (`F-WR-036`), paid at P3.7 rank 6(a) from the Food left after P3.6, never added to civilian demand. Food does not spoil. Recovery is one good turn (`ECN-085`). A food-secure standard start is stable indefinitely at 50,000 people because production (60) exceeds demand (50).

### 4.3 Extraction — seven chains

| Chain | Y/batch | V/batch | M/batch | Ref. price | Output value | Full cost | Base margin | Capacity at start | Money limit* | Space limit* | Binding constraint |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Food | 20 | 12 | 1 | 1 | 20 | 13 | **+7** | 3 | 136 | 84 | capacity |
| Coal | 10 | 10 | 1 | 1 | 10 | 11 | **−1** | 2 | 163 | 169 | capacity |
| Oil | 8 | 14 | 1 | 2 | 16 | 15 | **+1** | 1 | 111 | 211 | capacity |
| Iron | 10 | 10 | 1 | 1 | 10 | 11 | **−1** | 1 | 163 | 169 | capacity |
| Bauxite | 8 | 14 | 1 | 2 | 16 | 15 | **+1** | 0 | 111 | 211 | capacity 0 |
| Lead | 6 | 16 | 1 | 3 | 18 | 17 | **+1** | 0 | 102 | 281 | capacity 0 |
| Uranium | 1 | 28 | 1 | 30 | 30 | 29 | **+1** | 0 | 58 | 1,690 | capacity 0 |

\* Money and space limits are the integer batch limits after P3.2 at the standard start (treasury 1,639; free space 1,690), before the three-batch food chain consumes space.

The **negative coal and iron base margins are intentional**: raw coal and iron are worth more inside steel (steel +14) than sold at the reference price. A player who sells raw coal or iron at 1 destroys value relative to converting it; a player with no steel capacity may still sell it for liquidity. This is the published F-EC-036 reading, not an error. Food is the strongest extraction chain because it is the survival good, but its demand is capped by population and its storage by the warehouse.

### 4.4 Power — three generator classes

| Generator | GU/level | Fuel/level | Variable | Maintenance | Full cost/level | Cost per GU |
|---|---:|---|---:|---:|---:|---:|
| Coal | 6 | 6 coal (book 6) | 10 | 2 | **18** | **3.00** |
| Oil | 6 | 5 oil (book 10) | 14 | 2 | **26** | **4.33** |
| Nuclear | 20 | 1 uranium + 1 lead (book 33) | 40 | 2 | **75** | **3.75** |

At reference prices coal is the cheapest GU, oil the most expensive, nuclear in between. Two qualifications matter:

1. **Opportunity cost of oil.** Burning 5 oil as fuel forgoes refining it: one 10-oil batch yields 8 gasoline worth 48 for 20 variable, a value add of 28 per 10 oil (2.8/oil). At that opportunity cost, oil power is `(5×2.8 + 14 + 2)/6 = 5.00` crowns/GU, not 4.33. The register's 4.33 uses book value only and is labelled accordingly.
2. **Utilisation.** The 3.00/GU coal figure is **marginal at full output**. A generator runs if its full fuel and variable cost are available, and surplus GU is discarded (`ECN-058`/`ECN-059`). At the standard start only 2 of 6 GU are used, so the **actual** cost of the power consumed is `18/2 = 9.00` crowns/GU. The standard-start refining margin at actual utilisation is `6 − 18 = −12` crowns per batch, not the 0 in F-EC-037's full-utilisation table. Both figures are now published; the marginal figure answers "build more generation?", the actual figure answers "what did this batch cost?" (F14B-02/F14B-09).

There is **no generator idle control**. A generator level always runs when fuelled and funded, so a nation with surplus generation burns fuel every turn. At the standard start that is 16 crowns of fuel and variable cost for 6 GU of which 2 are used. The player's only remedies are to fill the grid (build processing capacity) or demolish the plant (`URB-023`). `ECN-059` calls this a real mistake; 14B records that the mistake cannot be paused, only avoided or filled (F14B-11).

### 4.5 Processing — four recipes, margins and dominance

| Chain | Inputs | Output | Input book | Output book | Variable | Maintenance | Power | **Base margin** | **Loaded at 3.0/GU** | Capital (B-05) | Capital per loaded crown |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Refining | 10 oil | 8 gasoline | 20 | 48 | 20 | 2 | 2 | **+6** | **0** | 425 | never (0 margin) |
| Steel | 10 iron + 6 coal | 8 steel | 16 | 56 | 24 | 2 | 3 | **+14** | **+5** | 485 | **97** |
| Aluminum | 12 bauxite | 8 aluminum | 24 | 64 | 24 | 2 | 4 | **+14** | **+2** | 560 | 280 |
| Ammunition | 8 lead + 4 coal | 10 ammunition | 28 | 60 | 20 | 2 | 2 | **+10** | **+4** | 465 | 117 |

**F-EC-038 dominance re-run.** No chain satisfies the formal test (highest base margin **and** lowest capital cost **and** lowest operating risk, or an output every other chain requires with no substitute):

- Steel and aluminum **tie** at +14 base margin. Steel has lower capital (485 vs 560), lower power (3 vs 4) and a cheaper input chain; aluminum has a single input and a higher-value output. Steel is the **practical** strongest first manufacturing build, but it is not formal dominance because refining and ammunition are cheaper to build per batch.
- Refining is the **weakest** chain economically: 0 loaded margin at full utilisation, negative at the standard start's actual utilisation, the highest input-volume requirement (10 oil vs 8 produced), and a 425-crown capital cost. Its value is the **gasoline price** and the military/trade demand, not a reference-price arbitrage (F14B-06).
- Ammunition has a positive loaded margin (+4) but its demand is military and cyclical; it is not dominant in peacetime.
- No processing output is required by every other chain with no substitute (steel is required by construction, but B-05's construction catalogue charges steel only and has no alternative-goods requirement that forces steel production).

**Recipe verification:** the four recipes match D-046 and the register exactly; inputs and outputs are integers; no recipe consumes its own output; input book value is below output book value in every chain; no per-nation variance exists (`ECN-075`/`ECN-076`). No recipe was changed.

### 4.6 Maintenance and upkeep

| Obligation | Standard start | Rate | Charged |
|---|---:|---|---|
| Food extraction | 3 | 1/batch | P3.2 |
| Coal extraction | 2 | 1/batch | P3.2 |
| Oil extraction | 1 | 1/batch | P3.2 |
| Iron extraction | 1 | 1/batch | P3.2 |
| Coal generator | 2 | 2/level | P3.2 |
| Refining | 2 | 2/batch | P3.2 |
| **Total** | **11** | | |
| Facility upkeep (lab/civic) | 0 at start | 2 / 1 per facility | **P3.7 rank 7(a)** |
| Public-service cost | **30** | 20% of gross tax | **P3.7 rank 7(b)** |

Maintenance is one whole obligation per chain, attempted extraction → generation → processing, paid in full or cancelled in full, and a cancelled chain is `UNMAINTAINED` for that turn (`ECN-147a`). The 1-crown case pays oil and cancels five; the 3-crown case pays food and cancels five; the 11-crown case pays all six. No partial maintenance and no proportional allocation exists. Facility upkeep and the public-service cost are **not** in F-EC-014; they are P3.7 obligations and are cancelled whole with their own flags. Maintenance is 7.3% of the standard-start outflow (11/151).

### 4.7 Treasury and inventory accounting

**Treasury identity (Example G):** `1,500 + 150 − 11 − 80 − 10 − 20 − 30 = 1,484`, where the 150 tax is reduced by the 15-crown alliance Crowns withholding before the nation's spendable balance: `1,500 + (150 − 15) − 11 − 80 − 10 − 20 − 30 = 1,484`. The identity holds to the crown.

**Resource identity (Example G):** `310 + 106 − 69 = 347` units. Per resource:

| Resource | Opening | Produced | Consumed / transferred | Closing |
|---|---:|---:|---:|---:|
| Food | 120 | 60 | 50 civilian + 1 military | 129 |
| Coal | 60 | 20 | 6 generator | 74 |
| Oil | 30 | 8 | 10 refining | 28 |
| Iron | 30 | 10 | 2 alliance tax | 38 |
| Bauxite | 20 | 0 | 0 | 20 |
| Lead | 10 | 0 | 0 | 10 |
| Gasoline | 20 | 8 | 0 | 28 |
| Steel | 20 | 0 | 0 | 20 |
| **Total** | **310** | **106** | **69** | **347** |

**Wealth identity:** `1,484 + 675 = 2,159`; opening `1,500 + 600 = 2,100`; change **+59** = net cash −16 + inventory +75. The components are not double-counted: treasury, inventory book value and fixed-asset book value are disjoint (`F-EC-024`). A reservation reduces **available** cash, never total treasury; it is not an expense. A reserved inventory unit still counts toward warehouse space and is excluded from `available_units` (`F-EC-022`).

### 4.8 Reference prices versus costs

| Term | Meaning | Standard-start example |
|---|---|---|
| Book value | Reference price × units | 20 steel = 140 crowns |
| Reference price | Accounting estimate, not a market promise | steel 7/unit |
| Actual market price | B-07's negotiated price | Example 16: 8/unit |
| Variable cost | Per batch, paid only if the batch runs | refining 20 |
| Maintenance | Per batch capacity, paid whether or not it runs | refining 2 |
| Power cost (marginal) | Fuel + variable + maintenance per used GU at full utilisation | coal 3.00/GU |
| Power cost (actual) | Whole generator cost ÷ used GU | 9.00/GU at 2/6 utilisation |
| Full economic cost | Inputs + variable + maintenance + power | refining 48/8 = 6.00 per gasoline at marginal power; 60/8 = 7.50 at actual standard-start power |
| Capital expenditure | One-time durable asset | farm 155 |
| Operating expenditure | Recurring cost of running capacity and obligations | 151/turn |

Full economic cost per manufactured unit at marginal power: gasoline **6.00** (price 6, margin 0), steel **6.375** (price 7, +0.625), aluminum **7.75** (price 8, +0.25), ammunition **5.60** (price 6, +0.40). Only gasoline is at break-even at the reference price. This is the deliberate design of F-EC-037: refining's profit comes from the gasoline market, not from the reference price. Apparent profitability that omits power, maintenance or the owner's own input book value is misleading; the table above includes all four.

### 4.9 Multi-turn sustainability and the money-creation test (F-EC-039)

The 30-turn deterministic reference model runs the standard start under two policies. It is **hand-equivalent arithmetic executed in `14B_verify_b04_economy.py`**, not a gameplay simulation.

| Measure | Produce (RUN_AT_CAPACITY) | Idle (no production) |
|---|---:|---:|
| Tax collected, 30 turns | **4,500** | **3,303** (hunger reduces it from turn 4) |
| Gross production value at reference prices | **4,476** | **0** |
| Net crowns added to the money supply | **+30** | **+2,213** |
| Closing treasury | **1,530** | **3,713** |
| Closing inventory units | **1,516** | **130** |
| Closing inventory book value | **2,856** | **420** |
| Closing national wealth | **4,386** | **4,133** |
| Food at close | **420** | **0** |
| Refinery idle turns | **3** (turns 16, 21, 26; one in five after the starting oil is spent) | 30 (by choice) |
| F-EC-039, gross reading | **FAIL by 24 crowns (0.5%)** | **FAIL** |
| F-EC-039, net reading | **PASS** (−24 vs 4,476) | **FAIL** |

Selected turns (produce): T1 treasury 1,499 / wealth 2,177 / 350 units; T10 1,490 / 2,870 / 710; T15 1,485 / 3,255 / 910; T16 1,504 / 3,324 / 952 (first refinery idle); T20 1,500 / 3,632 / 1,112; T25 1,515 / 4,009 / 1,314; T30 1,530 / 4,386 / 1,516.

**Interpretation.**

- The producing nation is **cash-neutral** (−1/turn while the refinery runs, +19 on the three idle turns) and **wealth-growing** (+77/turn early, slowing as oil binds). It is solvent for the whole 30 turns.
- The **gross** money-creation reading fails by 24 crowns: tax is 100.5% of gross production value over 30 turns. The **net** reading passes because the sinks (maintenance, variable costs, the service cost) return almost all the tax to the economy. The rule text does not define "new crowns", so both readings are recorded; the final reading is a Prompt 14 balance decision (C-11).
- **Idling fails both readings** and starves the population: food reaches 0 at turn 3, hunger caps at 3,000 bp, tax falls from 150 to 105, coal runs out at turn 10, and the nation ends with 2,213 extra crowns and 130 units. This is the behaviour the test is designed to catch, and it validates the test's purpose.
- The **warehouse does not block** in 30 turns (1,516 of 2,000 units). Extrapolating +40 units/turn, the wall is ~42 turns away; after that food continues (it is first in the priority order) while coal/iron block. The model does not claim a 42-turn result.
- **Oil is the binding input.** The refinery consumes 10 oil per batch but the starting oil well produces 8. The 30 starting oil is a 15-turn bridge; thereafter the refinery runs four turns in five, accumulating one batch's shortfall each cycle. A player must add oil capacity, buy oil or accept the idle turns (F14B-03).
- **Power is overbuilt at the start.** 6 GU are generated for 2 GU of demand; 4 GU are discarded every turn. The refinery's actual power cost is 9/GU, and its actual margin is −12/batch. The first processing build that uses the surplus is worth more than it appears (F14B-02).
- **No money is created by trade, transfer, reservation or duplicate settlement** in the model; every transfer is paired and every retry is a no-op (Examples D, 14, 16).

### 4.10 Exploit, failure and sustainability findings

Severity uses Critical / High / Medium / Low / Informational. "Reproducible" means the arithmetic in this report reproduces it; it does not mean a runtime exists.

| ID | Finding | Systems / formulas | Mechanism and calculation | Severity | Reproducible | Owner | Proposed resolution | Decision category | Regression test |
|---|---|---|---|---|---|---|---|---:|
| F14B-01 | Standard start is cash-neutral, not cash-positive | B-04 F-EC-001/014/016/018; B-06 F-PD-020 | 150 tax − 121 capacity opex − 30 service = **−1**; wealth +77 | Medium | Yes (Ex H) | B-04/B-06 balance | Accept as a design property or tune a coefficient in the Prompt 14 balance phase; no change made | C (needs playtesting) | `14B_verify_b04_economy.py` H checks |
| F14B-02 | Refining is loss-making at the standard start's actual utilisation | F-EC-031/037, ECN-059 | Generator costs 18 for 6 GU; 2 used → 9/GU; refining base +6 − 18 = **−12** | Medium | Yes | B-04 | Report both marginal and actual power cost; encourage filling the grid | B (reporting) | margin checks |
| F14B-03 | Oil production is below refinery input | R-19, R-32, F-EC-004/009 | 8 produced vs 10 required; 30 stock = 15 turns; then 4-on/1-off | Medium | Yes (30-turn) | B-04/B-05 balance | Build oil capacity or buy oil; no formula change | C (needs playtesting) | 30-turn model |
| F14B-04 | Gross money-creation test fails by 24 crowns | F-EC-039 | 4,500 tax vs 4,476 output | Medium | Yes | B-04/Prompt 14 | Clarify gross vs net reading in the balance phase; the net reading passes | C (provisional interpretation) | F-EC-039 checks |
| F14B-05 | Steel is the practical strongest manufacturing chain | F-EC-036/038; R-33 | +14 base, +5 loaded, capital/loaded 97 vs aluminum 280 | Low | Yes | B-04 | Not dominance; preserve the trade-off (steel needs two inputs) | B (observation) | margin checks |
| F14B-06 | Refining is the weakest chain | F-EC-036/037; R-32 | 0 loaded margin at full utilisation, negative at actual; 425 capital | Medium | Yes | B-04 | Preserve as the gasoline-market play; do not hide the cost | B (observation) | margin checks |
| F14B-07 | Raw coal/iron have negative base margins | F-EC-036 | Coal −1, iron −1; value is realized inside steel | Low | Yes | B-04 | Intentional; the report states it explicitly | B (clarification) | margin checks |
| F14B-08 | Warehouse fills in ~42 turns if nothing is sold | F-EC-023; R-07/R-17 | +40 units/turn; 1,690 free | Medium | Extrapolated | B-04/B-05 | Sell, process or expand (`URB-058`); no decay | B (observation) | projection only |
| F14B-09 | Power utilisation is not reported by F-EC-037 | F-EC-037 | Marginal 3.0 vs actual 9.0/GU | Medium | Yes | B-04 | Both figures now published | B (correction) | margin checks |
| F14B-10 | Alliance tax raises the effective service burden | ECN-213a; B-06 F-PD-020 | Service is 20% of gross 150 = 30; national net tax is 135; effective 22.2% | Low | Yes (Ex E/G) | B-06/B-09 | B-06 decides whether service reads gross or post-withholding; recorded | C (cross-system) | Ex E/G checks |
| F14B-11 | No generator idle control | ECN-058/059 | 16 crowns/turn for 2 used GU at the start | Low | Yes | B-04/B-05 | Fill the grid or demolish; no rule change | B (observation) | power checks |
| F14B-12 | A passive idle strategy starves the nation | F-EC-002/003 | Food 0 at turn 3; hunger 3,000; tax 105 | Informational | Yes (30-turn) | B-04 | The hunger penalty already punishes it; no new rule | B (validation) | 30-turn idle |
| F14B-13 | Duplicate settlement / event replay | F-EC-033/034 | Keyed no-op; no second row or event | None | Yes | B-02/B-04 | No change | — | Ex 14, negative tests |
| F14B-14 | Resource hoarding | F-EC-021/023 | Finite warehouse; no decay; opportunity cost only | None (design) | Yes | B-04 | Legitimate strategy; not an exploit | — | Ex 6/13 |
| F14B-15 | Long-term economic dead ends | F-EC-004/014; B-05 | No production chain is irreversible; recovery via B-05 build/demolish and B-07 sale | Low | Qualitative | B-04/B-05 | No dead end found; B-05 demolition costs 25% | — | — |
| F14B-16 | B-06 service cost was absent from B-04 | ECN-101/144/152/165 | Standard turn omitted 30 crowns | High (coherence) | Yes | B-04 corrected | D-240 | B | token + Ex H |
| F14B-17 | B-05 modifiers were absent from F-EC-004/012/014 | F-CI-015/016/017 | Research could break the space limit and maintenance | High (coherence) | Yes (source) | B-04 corrected | D-241 | B | token checks |
| F14B-18 | Example 4 used a superseded placeholder | F-EC-027/032 | 250/36 vs B-05's 155/23 | Medium | Yes | B-04 corrected | D-242 | B | validator Ex4 |
| F14B-19 | Gasoline's construction-fuel role is not implemented by B-05 | ECN-024/028; B-05 catalogue | B-05 charges crowns + steel only | Medium | Yes | B-05/B-04 | B-04 role corrected; B-05 may add a gasoline cost in a later balance pass | C (cross-system) | token check |
| F14B-20 | B-06 internal reference defects | DMP-135, DMP-097a | "P3.8 sub-step"; ECN-081 cited for the tax rate | Low | Yes | B-06 | Outside 14B authority; recorded | — | report only |

**No money-creating, resource-creating, duplicate-transfer or free-production exploit was found in the B-04 rules or in the reference model.** The material findings are balance/reporting issues, not exploitable loops. The two high-severity items (F14B-16/F14B-17) were coherence gaps in the documentation, and both are corrected in B-04.

---

## 5. Cross-system consistency audit

### 5.1 Method and vocabulary

Each confirmed dependency was read in **both** authoritative documents. The status vocabulary is exact:

- **VERIFIED CONSISTENT** — both documents state the same contract; arithmetic and timing agree.
- **VERIFIED WITH DOCUMENTED LIMITATION** — the contract holds, but a named limitation or unresolved external matter remains.
- **CONTRADICTION IDENTIFIED** — the documents disagree; the discrepancy is recorded with its owner.
- **NOT YET VERIFIED** — not inspected or not yet reproducible.
- **OUTSIDE PROMPT 14B AUTHORITY** — the correction belongs to another system; 14B records it and does not edit it.

No relationship is marked consistent because it looks plausible. A contradiction is not called resolved because it is documented; where the correction was within B-04's own authority it was applied and re-tested, and where it belongs to another system it retains the external owner.

### 5.2 Cross-system dependency inventory

| ID | Source → receiver | Source evidence | Receiving evidence | Formulas | Parameters | Input → output | Units / rounding |
|---|---|---|---|---|---|---|---|
| X-01 | B-02 → B-04 | `TR-024`, `TR-040` (2-hour P0–P7) | `F-EC-000d`, `ECN-144` | all | — | turn boundary → every P3 formula | hours; none |
| X-02 | B-02 → B-04 | `TR-040` P3/P4, `TR-044` B1 | `ECN-144`, `ECN-163` | all | — | phase position → internal P3.1–P3.8 | phase; none |
| X-03 | B-02 → B-04 | reservation model `TR-068`/`TR-069`/`TR-070` | `ECN-125`/`ECN-126`, `F-EC-019`/`020`/`022` | F-EC-019/020/022 | — | reservation → available balance | crowns/units; integer |
| X-04 | B-02 → B-04 | idempotency | `F-EC-033`/`F-EC-034`, `ECN-154`/`155` | F-EC-033/034 | — | turn+nation key → one settlement | composite key; exact |
| X-05 | B-02 → B-04 | `TR-005` OP regeneration at P3.7 | `ECN-007`, `ECN-144` | — | OP values (B-10) | one OP at P3.7 → military-only pool | OP; integer |
| X-06 | B-03 → B-04 | nation creation structure; §8 | `ECN-201`, D-063 | — | 20 carry-ins (not B-04) | starting state → bundle grant | mixed; exact |
| X-07 | B-03 → B-04 | reroll/reset `RRL-013`…`RRL-021` | `ECN-201`…`ECN-207` | F-EC-024/025 | — | retirement → assets destroyed | crowns/units; exact |
| X-08 | B-03 → B-04 | §21.2 carry-ins | inventory §4 | — | 20 carry-ins | none consumed by B-04 | mixed |
| X-09 | B-05 → B-04 | `URB-047`, `URB-055`…`URB-057` | `ECN-042`, `F-EC-004`/`F-EC-008` | F-EC-004/006/008 | capacity vector R-17…R-24 | facility → batches | batches; integer |
| X-10 | B-05 → B-04 | `URB-055`/`URB-056`, `F-CI-011`/`F-CI-012` | `F-EC-026`/`F-EC-027`/`F-EC-032` | F-EC-026/027/032 | building cost | construction → book value | crowns; integer |
| X-11 | B-05 → B-04 | `F-CI-015`/`F-CI-016` | `F-EC-004`/`F-EC-012` | F-EC-004/012 | `yield_bonus` | research → effective output | units; integer |
| X-12 | B-05 → B-04 | `F-CI-017` | `F-EC-014` | F-EC-014 | `standards_bonus` | programme → processing maintenance | crowns; integer |
| X-13 | B-05 → B-04 | `URB-059`/`URB-060` | `ECN-051`, `ECN-105` rank 7 | — | lab 2, civic 1 | facility → P3.7 upkeep | crowns; integer |
| X-14 | B-05 → B-04 | `URB-046`, `URB-067` (P4.1, next turn) | `ECN-098`, `ECN-162` | — | — | capex at P4.1 → capacity next turn | phase; none |
| X-15 | B-05 → B-04 | `URB-050`/`URB-051a` DC/overdraw | `ECN-042`, F-EC-004 | F-EC-004 | DC | capacity invariant → no extra batch | DC; integer |
| X-16 | B-05 → B-04 | `URB-058`, `F-CI-014` | `ECN-122`, `F-EC-023` | F-EC-023 | warehouse 2,000 + 250/expansion | expansion → free space | units; integer |
| X-17 | B-06 → B-04 | `F-PD-001`, `F-PD-017` | `F-EC-001` | F-EC-001 | population, tax rate, stability | frozen inputs → tax | people/bp → crowns; floor |
| X-18 | B-06 → B-04 | `F-PD-020`, `DMP-097`, `DMP-118`, `DMP-135` | `ECN-101`/`144`/`152`/`165` | F-EC-018 | service share 0/2,000/5,000; modifier | gross tax → P3.7 service cost | crowns; floor then ceil |
| X-19 | B-06 → B-04 | `F-PD-018` stability target | `F-EC-001`, `F-EC-003` | F-EC-001/003 | hunger feed | hunger → next tax | bp; floor |
| X-20 | B-06 → B-04 | `DMP-095` fiscal set | `F-EC-001` | F-EC-001 | tax 200/300/400 | policy → rate | bp; integer |
| X-21 | B-07 → B-04 | `MKT-033`/`MKT-034`/`MKT-056` | `ECN-162`, `F-EC-018`/`029` | F-EC-018/029 | — | P4 trade → treasury/inventory | crowns/units; exact |
| X-22 | B-07 → B-04 | `MKT-054`/`MKT-058` | `F-EC-023`, `ECN-124` | F-EC-023 | — | space reservation → free space | units; integer |
| X-23 | B-07 → B-04 | `MKT-068`/`MKT-070` | `F-EC-028`, `ECN-100` | F-EC-028 | `fee_bp = 0` | fee → zero at launch | crowns; floor |
| X-24 | B-07 → B-04 | `D-114`, band 3,000 bp; window 360 turns | `ECN-208` | — | band/window | review signal → no price change | bp/turns; integer |
| X-25 | B-08 → B-04 | aid/indemnity transfers; `F-DP-011` | `F-EC-029`/`F-EC-030`, `ECN-212` | F-EC-029/030 | — | transfer → paired ledger | crowns/units; exact |
| X-26 | B-09 → B-04 | `ALL-179`…`ALL-187`; `ECN-213a` | `ECN-144`/`146`/`148`/`150` | F-EC-001, F-EC-004/012 | rates 0…10,000 bp | production → source withholding | crowns/units; cumulative floor |
| X-27 | B-09 → B-04 | `ALL-187`, `ALL-220`…`ALL-226` | `ECN-213`/`ECN-213a` | — | no spendable purpose | ARL receipt → no general withdrawal | crowns/units; exact |
| X-28 | B-09 → B-04 | `ECN-213a` Crowns tax | `F-EC-001`, B-06 `F-PD-020` | F-EC-001 | rate | gross tax → net national + ARL | crowns; floor |
| X-29 | B-10 → B-04 | `F-WR-036`, `WAR-053l` | `ECN-080`/`081`/`214`, `F-EC-002a` | F-EC-002a/003 | soldier equivalents | force → P3.7 Food ration | Food units; one ceil |
| X-30 | B-10 → B-04 | supply bundles `F-WR-016` | `ECN-131`/`ECN-214` | — | bundle quantities | operation → reserved resources | units; integer |
| X-31 | B-10 → B-04 | `F-WR-001` OP | `ECN-007`, `ECN-144` | — | OP cap | OP → military actions only | OP; integer |
| X-32 | B-11 → B-04 | reward rules `F-WEP-046`/`F-WEP-049` | `F-EC-015`, `ECN-113` | F-EC-015 | reward amount | one-time reward → income | crowns; integer |
| X-33 | B-12 → B-04 | correction `F-FP-014` | `ECN-114`, `ECN-166` | F-EC-018 | — | adjustment/reversal → ledger | crowns; exact |
| X-34 | B-13 → B-04 | six number types; `ECN-177` | `ECN-183`/`ECN-217` | — | — | report → same definitions | — |
| X-35 | B-14 → B-04 | 47/49 count; D-237 | register/inventory | — | — | index → reconciled counts | — |

### 5.3 Consistency assessment

| ID | Timing | Resource / treasury consequence | Ownership | Numerical status | Existing coverage | Discrepancy | Required action | Status | Regression |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | every boundary | none | B-02 | fixed | validators | none | none | **VERIFIED CONSISTENT** | 14B model |
| X-02 | P3/P4 | none | B-02 | fixed | ECN-144 | none | none | **VERIFIED CONSISTENT** | Ex A/G |
| X-03 | acceptance/P3 | available ↓, total unchanged | B-02 | fixed | Ex 12/14 | none | none | **VERIFIED CONSISTENT** | negative tests |
| X-04 | settlement | none | B-02 | fixed | Ex 14 | none | none | **VERIFIED CONSISTENT** | Ex 14 |
| X-05 | P3.7 | OP only | B-02/B-10 | fixed | — | none | none | **VERIFIED CONSISTENT** | — |
| X-06 | creation | bundle once | B-03 | provisional | Ex 1/17 | none | none | **VERIFIED CONSISTENT** | Ex 1 |
| X-07 | retirement | assets destroyed | B-03 | fixed | Ex 17 | none | none | **VERIFIED CONSISTENT** | Ex 17 |
| X-08 | creation | none | B-03 | provisional | inventory §4 | none | none | **VERIFIED CONSISTENT** | inventory |
| X-09 | P3.3/P3.5 | capacity → batches | B-05 | provisional | Ex B | none | none | **VERIFIED CONSISTENT** | Ex B |
| X-10 | P4.1 | capex → book value | B-05 | provisional | Ex 4 | **placeholder cost** | corrected to farm 155 | **CONTRADICTION IDENTIFIED** (fixed in B-04) | Ex 4 |
| X-11 | P3.3/P3.5 | output ↑ | B-05 | provisional | F-CI-015/016 | **not consumed by B-04** | corrected | **CONTRADICTION IDENTIFIED** (fixed in B-04) | token + model |
| X-12 | P3.2 | maintenance ↓ | B-05 | provisional | F-CI-017 | **not consumed by B-04** | corrected | **CONTRADICTION IDENTIFIED** (fixed in B-04) | token + model |
| X-13 | P3.7 rank 7(a) | upkeep | B-05 | provisional | URB-059/060 | **not in F-EC-014** | clarified as P3.7 obligation | **VERIFIED WITH DOCUMENTED LIMITATION** | Ex A |
| X-14 | P4.1 → next turn | capacity next turn | B-05 | fixed | Ex 4 | none | none | **VERIFIED CONSISTENT** | Ex 4 |
| X-15 | P4.1 | no extra batch | B-05 | provisional | URB-051a | none | none | **VERIFIED CONSISTENT** | Ex B |
| X-16 | next turn | space ↑ | B-05 | provisional | URB-058 | none | none | **VERIFIED CONSISTENT** | Ex 6 |
| X-17 | P3.1 | tax ↑ | B-06 | provisional | Ex H/C | none | none | **VERIFIED CONSISTENT** | Ex H/C |
| X-18 | P3.7 rank 7(b) | treasury − | B-06 | provisional | Ex H | **absent from B-04** | B-04 adopts it (D-240) | **CONTRADICTION IDENTIFIED** (fixed in B-04; B-06 defects remain) | Ex H |
| X-19 | P3.6 → next P3.1 | tax ↓ | B-06 | provisional | Ex 11/19/C | none | none | **VERIFIED CONSISTENT** | Ex C |
| X-20 | P3.1 | rate | B-06 | provisional | DMP-095 | domain 0…10,000 vs set {200,300,400} | documented; B-04 does not own the set | **VERIFIED WITH DOCUMENTED LIMITATION** | Ex C |
| X-21 | P4 | paired transfer | B-07 | provisional | Ex 16/D | none | none | **VERIFIED CONSISTENT** | Ex D |
| X-22 | acceptance/P4 | space reserved | B-07 | provisional | MKT-054 | none | none | **VERIFIED CONSISTENT** | Ex D |
| X-23 | P4 | fee 0 | B-07 | fixed at launch | Ex 16 | none | none | **VERIFIED CONSISTENT** | Ex 16 |
| X-24 | acceptance | review only | B-07 | provisional | D-114 | none | none | **VERIFIED CONSISTENT** | Ex 16 |
| X-25 | P4 | paired transfer | B-08 | provisional | ECN-212 | none | none | **VERIFIED CONSISTENT** | Ex D |
| X-26 | P3.1/P3.3/P3.5 | source withholding | B-09 | design proposal | Ex E/G | none | none | **VERIFIED CONSISTENT** | Ex E |
| X-27 | P3/P4 | ARL receipt; no spend | B-09 | owner-reserved `UD-046` | Ex E | none | none | **VERIFIED WITH DOCUMENTED LIMITATION** | Ex E |
| X-28 | P3.1 | service base gross | B-06/B-09 | provisional | Ex G | service on gross vs post-tax net | recorded; B-06 decides | **VERIFIED WITH DOCUMENTED LIMITATION** | Ex G |
| X-29 | P3.7 6(a) | Food − | B-10 | provisional | Ex F | none | none | **VERIFIED CONSISTENT** | Ex F |
| X-30 | acceptance/P3.7 | resources reserved | B-10 | provisional | — | none | none | **VERIFIED CONSISTENT** | Ex F |
| X-31 | P3.7 | OP only | B-10 | provisional | — | none | none | **VERIFIED CONSISTENT** | — |
| X-32 | P3.1/P4 | crown inflow | B-11 | provisional | ECN-113 | none | none | **VERIFIED CONSISTENT** | — |
| X-33 | case | correction | B-12 | provisional | ECN-166 | none | none | **VERIFIED CONSISTENT** | — |
| X-34 | report | labels only | B-13 | fixed | ECN-177 | none | none | **VERIFIED CONSISTENT** | — |
| X-35 | index | counts | B-14 | fixed | 14A-02 | none | none | **VERIFIED CONSISTENT** | 14A-02 |

**Tally:** 35 dependency-matrix rows: 27 `VERIFIED CONSISTENT`, 4 `VERIFIED WITH DOCUMENTED LIMITATION`, 4 `CONTRADICTION IDENTIFIED`, 0 `NOT YET VERIFIED` (sum 35); separately, the 18-entry contradiction register and the 2 B-06 `OUTSIDE PROMPT 14B AUTHORITY` items are not part of the 35. The four matrix contradictions are X-10, X-11, X-12 and X-18; all four were corrected inside B-04's own authority. The parameter-inventory timing/units correction is contradiction-register entry C-08/C-09, **not** a matrix row. A fixed contradiction is reported as identified-and-corrected, not as if it had never existed.

**14B-C1 closeout correction (2026-11-17).** This tally was corrected by Prompt 14B-C1 from the earlier 27/6/5 summary; the six/ve split mixed matrix rows with contradiction-register entries. The matrix rows were recounted and no row classification changed. See [the C1 closeout report](26_prompt_14B-C1_closeout_report.md).

### 5.4 B-02 turn-order consistency

B-02's `TR-040` fixes P0 Prepare, P1 Freeze, P2 Re-validate, P3 Recurring, P4 Orders, P5 Conflict, P6 World, P7 Settle. B-04's `ECN-144` fixes the internal P3 order: **P3.1 tax → P3.2 maintenance → P3.3 extraction → P3.4 power → P3.5 processing → P3.6 food → P3.7 obligations → P3.8 close**. The two are consistent: B-04 does not create a second clock, a second phase or a second scheduler. D-019's income-before-upkeep rule is satisfied at P3.1 before P3.2. Extraction before power lets this turn's coal fuel this turn's generator; power before processing satisfies the physical prerequisite; processing before food lets a nation convert goods before the population eats; food before obligations protects civilians; obligations last; close last. **No formula reads a later sub-phase's output.** The alliance tax is a source withholding inside P3.1/P3.3/P3.5, not a new sub-phase. B-04's "P3.8 Close" is a local close; B-02's P7 remains the world settle and publication. **VERIFIED CONSISTENT.**

### 5.5 B-03 starting-state consistency

B-03 fixes the starting-state **structure** and defers every number to B-04/D-063. The live repository's standard start matches: 1,500 crowns, 50,000 people, 2,000 warehouse, 300 bp, the 310-unit bundle, the nine granted facilities and the eleven-batch capacity vector. The capital is 50 infrastructure / 15 DC; the nine granted facilities consume 11 DC, leaving 4. **No B-03 rule was modified.** The 20 §21.2 carry-ins are not B-04 values and none is consumed by a B-04 formula; their owners (Prompt 12, 10, 07, 13, Stage 6) are preserved exactly. **VERIFIED CONSISTENT.**

### 5.6 B-05 consistency

- **Capacity:** every facility adds one batch (extraction/processing) or one generator level; B-04's batch planning never exceeds the B-05 capacity vector. The 15-DC capital cannot hold the 17-DC plan in Example B; the legal 15-DC plan fits exactly.
- **Construction:** B-05 `F-CI-012` book value is `cost + Σ(materials × reference price)`; B-04 `F-EC-026`/`F-EC-027` receive it. Example 4 now uses the farm (120 + 5 steel = 155), not the superseded placeholder.
- **Research:** B-05 `F-CI-015`/`F-CI-016` publish a `yield_bonus`; B-04 `F-EC-004`/`F-EC-012` now consume it, including in the space limit so a bonus cannot overrun the warehouse. `F-CI-017` publishes a `standards_bonus` that reduces processing maintenance to a floor of 1; B-04 `F-EC-014` consumes it. At launch both bonuses are 0, so no published number changed.
- **Facility upkeep:** B-05's lab (2) and civic centre (1) are not capacity maintenance; B-04 now places them at P3.7 rank 7(a). This is a **VERIFIED WITH DOCUMENTED LIMITATION** because B-05 does not name the phase itself; B-04's placement is the deterministic receiving rule.
- **Timing:** construction resolves at P4.1 and capacity is available next turn; B-04's `ECN-098`/`ECN-162` agree.
- **Warehouse:** B-05 `F-CI-014` adds 250 units per expansion; B-04 `F-EC-023` reads `W`. Consistent.
- **Overdraw:** B-05 `URB-051a` keeps existing production running after damage; B-04's batch planning is unchanged. Consistent.

### 5.7 B-06 consistency

- Population, tax rate and stability are B-06's; B-04 consumes them as frozen P3.1 inputs and never redefines growth, approval or legitimacy.
- The public-service cost (`F-PD-020`) was **absent** from B-04 and is now adopted (D-240). The amount remains B-06's; B-04 executes the P3.7 debit and the cancellation flag.
- The service base is the **gross** P3.1 tax income. An alliance Crowns withholding reduces the national net but not the service base, so the effective service burden rises (20% of gross, 22.2% of the national net at a 10% alliance rate). This is a **documented limitation**; B-06 owns any change.
- The tax policy set is `{200, 300, 400}` bp; B-04's formula domain is wider. The set is B-06's and is not redefined.
- Hunger is computed by B-04 at P3.6 and consumed by B-06 in growth, support and stability; B-06 may not change the formula or the 3,000 bp cap.
- **Two B-06 internal defects are recorded and left alone:** `DMP-135` calls the service cost a "P3.7 obligation" and then a "P3.8 sub-step"; `F-PD-020` fixes P3.7. `DMP-097a` cites `ECN-081` for the tax-rate storage, but B-04's `ECN-081` is the Food-consumption timing; the correct B-04 references are `ECN-094`/`ECN-095`. Both are **OUTSIDE PROMPT 14B AUTHORITY**; owner B-06.

### 5.8 B-07 consistency

Trade settles at P4, both legs or neither, with one `transfer_id`; the buyer's space is reserved at acceptance and P3's `free_space` subtracts it. B-04's `F-EC-018`/`F-EC-029` reproduce the conserved transfer. The directed-trade fee is **0** at launch (`MKT-068`), and B-04's `F-EC-028` returns 0; the 2% fee in Example 16 is explicitly hypothetical and not adopted. The fair-value band is **3,000 bp** (D-114) and the fresh-nation window is **360 turns**; both are provisional review rules, not prices, and B-04 enforces neither. A trade at P4 cannot change a P3 production result. **VERIFIED CONSISTENT.**

### 5.9 B-09 consistency

- The alliance tax is a source withholding from **current-turn production** only; opening balances, stockpiles, processing inputs, donations and trade receipts are not taxed. The Crowns tax is withheld after P3.1's gross credit; resource tax is withheld at each P3.3/P3.5 production event.
- The cumulative-fractional-accrual rule reconciles: two 10-iron events at 2,500 bp collect 2 + 3 = **5**, equal to `floor(20 × 0.25)`; independent per-event floors collect 4 and under-collect. The event taxes reconcile to the per-turn floor.
- The Alliance Receiving Ledger is a receipt/accounting record, not a treasury pool. No purpose has an approved cost schedule, so no ARL value is spendable. `UD-046` remains Open. B-04 preserves the paired-event, no-minting, no-destruction and no-negative-balance constraints.
- **VERIFIED CONSISTENT** for the withholding mechanics; **VERIFIED WITH DOCUMENTED LIMITATION** for the ARL's unavailable debit path and the gross-vs-net service base.

### 5.10 B-10 consistency

- `F-WR-036` owns the military Food ration: `ceil(Σ(strength × soldier_equivalent) / 1,000)`, computed from the single P3.7 force snapshot; B-04 executes the debit at P3.7 rank 6(a) from the Food left after P3.6.
- Civilian Food is never diverted to the garrison; an unpayable ration is cancelled whole, sets `RATION_SHORT` and reduces readiness. The `OP-09` field ration is separate and is released before civilians are exposed.
- Military supply bundles reserve gasoline, ammunition, steel and aluminum at acceptance and consume at resolution; B-04 provides the ledger and reservation contract, not the quantities.
- Operations Points remain D-015's military-only pool; B-04 does not create a general action currency. **VERIFIED CONSISTENT.**

### 5.11 Shared accounting definitions

| Term | B-04 definition | Interacting systems | Status |
|---|---|---|---|
| Treasury | The single national crown balance; may never be negative | B-02, B-03, B-05…B-12 | consistent |
| Available balance | `total − reserved`; what a new action can spend | B-02, B-05, B-07, B-09 | consistent |
| Reserved balance | Exclusive claims; still owned and still counted in totals | B-02, B-05, B-07 | consistent |
| Obligations | P3.7 whole items; paid in full or cancelled in full | B-05, B-06, B-10 | consistent after D-240/D-241 |
| Resource availability | `total − reserved`; a reserved unit is not available | B-05, B-07, B-10 | consistent |
| Resource inventory | Per-resource integer totals in one shared warehouse | B-05, B-07 | consistent |
| Production | A batch's gross output before consumption | B-05, B-09 | consistent |
| Consumption | Civilian, military or industrial use; never double-counted | B-06, B-10 | consistent |
| Closing state | The P3.8/P7 reconciled balances | B-02, B-11, B-13 | consistent |
| Net operating income | Capacity operations only; produced goods are an asset swap | B-06, B-13 | clarified; B-06's DMP-097a table agrees |
| Net economic result | Net cash flow + inventory book-value change | B-13 | new report definition; B-06 has no competing term |

**No conflicting definition remains inside B-04.** The one externally visible divergence is B-06's DMP-097a narrative that calls the service cost "one named line" of operating expenses; B-04 now treats it as a P3.7 obligation outside `net_operating_income` but inside the closing identity's `operating` term. Both statements are reconcilable, and B-04's version is the authoritative accounting treatment.

### 5.12 Dependency graph

```
B-03 starting state ──────────────┐
B-06 population / tax set / stability ─→ F-EC-001 tax ─→ P3.1 treasury
B-09 frozen bracket ──────────────┘        │
                                           ├→ B-06 F-PD-020 service cost (from gross tax) ─→ P3.7
                                           └→ F-EC-018 closing
B-05 capacity vector ─→ F-EC-004 extraction ─→ resources ─→ F-EC-021/023 ─→ F-EC-025 book value
        │                    │                                             │
        │                    └→ F-EC-014 maintenance (P3.2)                 └→ F-EC-024 wealth
        ├→ F-EC-006/007/008 processing ─→ F-EC-012 output ─→ inventory
        └→ F-EC-013 generators ─→ GU supply ─→ F-EC-008 derating
B-05 research modifiers ─→ F-EC-004/012 (yield) and F-EC-014 (maintenance)
B-05 facility upkeep ─→ P3.7 rank 7(a)
B-06 hunger ← F-EC-003 ─→ next-turn F-EC-001 (one-turn feedback)
B-07 trade (P4) ─→ F-EC-018/029/030 (paired transfer)
B-08 aid/indemnity (P4) ─→ F-EC-029/030
B-09 production tax ─→ F-EC-004/012 net output (source withholding)
B-10 F-WR-036 ration ─→ P3.7 rank 6(a) Food debit
B-11 rewards ─→ F-EC-015
B-12 adjustments ─→ F-EC-018
B-13 reports ← F-EC-016/017/024/025/035
```

**Circular dependencies.** No **same-turn** cycle exists. The only feedback loops are time-delayed and intentional: (a) P3.6 hunger → next P3.1 tax (`F-EC-003` → `F-EC-001`); (b) the B-06 stability target reads approval and hunger, and stability feeds the next turn's tax. Both are one-turn delayed and are resolved before the next settlement. The model evaluates them in the published order and does not need a different phase order to make an example work.

### 5.13 Contradiction register

| ID | Contradiction | Evidence | Owner | Resolution state | Follow-up |
|---|---|---|---|---|---|
| C-01 | B-06's public-service cost was absent from B-04's P3.7, ledger event list and closing identity | B-06 `F-PD-020`, `DMP-097`, `DMP-118`, `DMP-135` vs B-04 `ECN-101`/`144`/`152`/`165` | B-04 (receiving system) | **corrected** by D-240 | B-06's internal P3.7/P3.8 wording remains (C-06) |
| C-02 | B-05's research modifiers were absent from B-04's output and maintenance formulas | B-05 `F-CI-015`/`016`/`017` vs F-EC-004/012/014 | B-04 | **corrected** by D-241 | none |
| C-03 | Example 4's construction cost contradicted B-05's catalogue | B-04 §20 Example 4 vs `URB-055` | B-04 | **corrected** by D-242 | validator updated |
| C-04 | B-04 claimed gasoline as a construction fuel; B-05 consumes no gasoline | B-04 `ECN-024`/`028` vs B-05 catalogue | B-05/B-04 | B-04 role claim **corrected**; B-05 unchanged | B-05 may add a gasoline material cost in a later balance pass |
| C-05 | B-05 facility upkeep was not in F-EC-014 | `URB-059`/`060` vs F-EC-014 | B-05/B-04 | **clarified** at P3.7 rank 7(a) | B-05 does not name the phase; B-04 supplies it |
| C-06 | B-06 calls the service cost a P3.7 obligation and a "P3.8 sub-step" | `DMP-135` | B-06 | **OUTSIDE PROMPT 14B AUTHORITY** | B-06 correction required |
| C-07 | B-06 cites `ECN-081` for the tax-rate storage; B-04's ECN-081 is Food timing | `DMP-097a` | B-06 | **OUTSIDE PROMPT 14B AUTHORITY** | B-06 should cite `ECN-094`/`ECN-095` |
| C-08 | Parameter inventory gave generator timing as P3.7 | inventory §6 vs B-04 `ECN-144` | B-04/B-14 | **corrected** to P3.4 | 14A validator expectation advanced |
| C-09 | Parameter inventory gave extraction/recipe/generator unit vectors as "Not specified"/"GU" | inventory §6 | B-04/B-14 | **corrected** to explicit vectors | none |
| C-10 | F-EC-001's domain is 0…10,000 bp; B-06's policy set is {200,300,400} | `F-EC-001` vs `DMP-095` | B-06 owns the set | **VERIFIED WITH DOCUMENTED LIMITATION** | none; B-04 may not widen B-06's set |
| C-11 | F-EC-039's "new crowns" is undefined gross or net | `F-EC-039` | B-04/Prompt 14 | **VERIFIED WITH DOCUMENTED LIMITATION**; both measured | final reading in the Prompt 14 balance phase |
| C-12 | ECN-185 target 1 used a metric that excludes production value | `ECN-185` vs `F-EC-016` | B-04 | **corrected** by D-242 | target now uses `net economic result` |
| C-13 | ECN-186 claimed a positive net operating income "if the player does nothing" | `ECN-186` vs Ex H | B-04 | **corrected** | text now states −1 |
| C-14 | Example 1 said 1,500 crowns covers "roughly twelve turns of 121/turn" | Example 1 vs service cost | B-04 | **corrected** to ten turns of 151 | none |
| C-15 | The service base is gross while the alliance tax reduces the national net | `ECN-213a` + B-06 `F-PD-020` | B-06/B-09 | **VERIFIED WITH DOCUMENTED LIMITATION** | B-06 decides |
| C-16 | F-EC-018's `operating` term was undefined | `F-EC-018` | B-04 | **corrected** by clarification | expression unchanged |
| C-17 | B-04's event list lacked the B-06 service events | `ECN-165` | B-04 | **corrected** by D-240 | none |
| C-18 | The standard start's residual power is not a player choice | `ECN-058`/`059` | B-04/B-05 | recorded as F14B-11 | no rule change |

**Register separation.** This 18-entry contradiction register is **not** the 35-row dependency matrix: its entries are not matrix rows and are not counted in the matrix tally. **No contradiction was marked resolved because it was merely documented.** C-01/C-02/C-03/C-08/C-09/C-12/C-13/C-14/C-16/C-17 were fixed in B-04 and re-tested; C-05 was clarified in B-04; C-04 was partly corrected in B-04 with B-05 unchanged; C-06/C-07 remain `OUTSIDE PROMPT 14B AUTHORITY`; C-10/C-11/C-15 are documented limitations; C-18 is recorded with no rule change.

---

## 6. Integrated worked examples A–H

Each example states the opening state, formula and parameter identifiers, units, phase, intermediate arithmetic, rounding, resource and treasury movements, closing state, conservation checks and cross-system references. All figures are reproduced by [`14B_verify_b04_economy.py`](../qa_backups/14B_verify_b04_economy.py).

### Example A — B-02 and B-04: a complete P3 settlement

**Opening.** Standard start (1,500 crowns, 310 units, 50,000 people, 3/2/1/1/1 extraction and refining capacity, one coal generator). **Accepted manual order:** one refining batch, reserved at P2 (10 oil, 20 crowns, 1 capacity, 8 output space). **Garrison:** 50 `UNIT-INF` = 500 soldier-equivalents. **Fiscal:** `STANDARD` (300 bp, 2,000 service share). **Formulas:** F-EC-001/002/003/004/006/008/011/012/013/014/018; F-WR-036; F-PD-020.

| Phase | Arithmetic | Treasury | Inventory movement |
|---|---|---:|---|
| P3.1 | `floor(50,000×300×10,000/1e9)=150`; hunger 0 | 1,650 | — |
| P3.2 | 3+2+1+1 extraction, 2 generator, 2 refining = 11; all paid | 1,639 | — |
| P3.3 | food `min(3,136,84)=3` → 60, −36; coal 2 → 20, −20; oil 1 → 8, −14; iron 1 → 10, −10 | 1,559 | +98 |
| P3.4 | coal level: 6 coal + 10 → 6 GU; fail-closed satisfied | 1,549 | −6 coal |
| P3.5 | `M=1, A=0, P=1, demand=2, supply=6 → pct=10,000`; manual batch runs: 10 oil + 20 → 8 gasoline | 1,529 | −10 oil, +8 gasoline |
| P3.6 | demand 50; available 180; consume 50; unmet 0 | 1,529 | −50 food |
| P3.7 | military ration `ceil(500/1,000)=1`; service `floor(150×2,000/10,000)=30` | **1,499** | −1 food |
| P3.8 | close; no negative balance; every ledger delta reconciles | **1,499** | — |

**Closing:** treasury 1,499; food 129, coal 74, oil 28, iron 40, bauxite 20, lead 10, gasoline 28, steel 20 = **349 units**; book value **677**; wealth **2,176**. **Conservation:** `1,500+150−11−80−10−20−30 = 1,499`; `310+106−67 = 349`. **Cross-system:** the manual order occupied a slot inside capacity (`M+A≤C`); the ration is separate from civilian demand; the service cost is a P3.7 obligation. **Result:** `VERIFIED CONSISTENT`.

### Example B — B-05 and B-04: development capacity and power limit production

**The invalid 17-DC plan.** Three farms (3), two coal mines (2), one oil well (1), one iron mine (1), two bauxite mines (2), one refinery (2), one steel mill (2), one smelter (2) and one coal plant (2) = **17 DC** against the capital's **15 DC**. The plan cannot be accepted (`URB-050`/`URB-051`); no order exists.

**A legal 15-DC plan.** Three farms, two coal mines, one oil well, one iron mine, two bauxite mines, one refinery, one steel mill and one coal plant = **15 DC**. Production before power: 60 food, 20 coal, 8 oil, 10 iron, 16 bauxite. The refinery needs 10 oil and has 8 produced; the steel mill needs 10 iron + 6 coal and runs; there is **no smelter**, so the 16 bauxite is stored, not converted.

**The power trap.** Suppose the same nation instead allocates one refinery (2 GU), one steel mill (3 GU) and one smelter (4 GU) on the single coal plant's **6 GU**. `power_demand = 9`, `supply = 6`, `pct = floor(10,000×6/9) = 6,666`; `batches_available = floor(1×6,666/10,000) = 0` for **each** level-1 chain. All three processing chains idle, consume no inputs and produce nothing; 6 GU are discarded. A second coal plant (2 more DC, 2 more maintenance and fuel) restores 12 GU and all three chains run at 100%. **Result:** `VERIFIED CONSISTENT`; B-04 never exceeds B-05 capacity, and B-05's DC bound forces a real choice.

### Example C — B-06 and B-04: population, food shortage and next-turn tax

**Opening.** Standard inventory except food 20; population **100,000** (housing is 50,000, so B-06's crowding rule applies; B-04 does not own it). Capacity 3 farms. **Formulas:** F-EC-001/002/003/014/018; F-PD-001/017/020.

| Phase | Arithmetic | Result |
|---|---|---|
| P3.1 | `floor(100,000×300×10,000/1e9)=300`; hunger 0 | tax 300 |
| P3.2 | maintenance 11 | — |
| P3.3 | food 60; coal 20; oil 8; iron 10 | — |
| P3.4 | 6 GU | — |
| P3.5 | refining 1 batch → 8 gasoline | — |
| P3.6 | `food_after_other = 20+60 = 80`; demand 100; consumed 80; **unmet 20**; `floor(3,000×20/100)=600 bp` | hunger 600 |
| P3.7 | service `floor(300×2,000/10,000)=60` | — |
| Close | treasury `1,500+300−11−80−10−20−60 = **1,619**` | wealth 2,167 |

**Next turn:** base tax 300; penalty 600 → `floor(300×9,400/10,000)=**282**`; service 56. **Conservation:** treasury identity holds; food `20+60−80 = 0`. **Result:** `VERIFIED CONSISTENT`; the hunger penalty is applied once, at the next P3.1, and clears after one good turn.

### Example D — B-07 and B-04: import/export settlement

**Opening.** Seller: 1,529 crowns, 40 steel. Buyer: 1,000 crowns, 0 steel, free space 1,690. **Trade:** 20 steel at 8 crowns = 160. **Formulas:** F-EC-018/023/029/030; MKT-033/034/054/056/068.

| Leg | Seller | Buyer |
|---|---|---|
| Before | 1,529 crowns, 40 steel | 1,000 crowns, 0 steel |
| P4 (atomic) | **1,689 crowns, 20 steel** | **840 crowns, 20 steel** |
| Book value effect | −140 book, +160 cash → wealth **+20** | −160 cash, +140 book → wealth **−20** |

**Conservation:** crowns `+160/−160` sum to zero; steel `−20/+20` sum to zero; no fee (`MKT-068`). **Space:** the buyer's 20 units are reserved at acceptance, so P3's free space already subtracts them; a free space below 20 would fail the trade atomically. **Timing:** the trade settles at P4 after P4.1 construction, so the buyer cannot use the purchased steel to pay for a same-turn P4.1 build; it must already own the steel at acceptance. **Result:** `VERIFIED CONSISTENT`.

### Example E — B-09 and B-04: alliance taxation and cumulative rounding

**Opening.** Standard start; alliance Crowns rate **1,000 bp** (10%); iron rate **2,500 bp** (25%); coal and gasoline unconfigured (0%). **Formulas:** F-EC-001/004/012/018; ECN-213a; F-AL-006.

| Asset | Gross | Tax | National net | ARL |
|---|---:|---:|---:|---:|
| Crowns (P3.1) | 150 | **15** | 135 | +15 |
| Iron (P3.3, one event) | 10 | **2** | 8 | +2 |
| Coal (existing stock, burned) | 6 | **0** | 6 | 0 |
| Gasoline (P3.5 output, 0%) | 8 | **0** | 8 | 0 |
| **Total** | | **17** | | 17 |

**Cumulative accrual:** two 10-iron events at 2,500 bp → event 1 `floor(10×0.25)=2`; cumulative 20 → `floor(20×0.25)=5`, event 2 = **3**; total **5** = `floor(20×0.25)`. Independent per-event floors give 2+2=4 and under-collect. **Treasury:** `1,500+135−11−80−10−20−30 = **1,484**`; service is 30 because B-06 reads the **gross** tax 150, not the 135 net. **ARL:** crowns 15, iron 2; no value is spendable because no AOP cost schedule is approved. **Conservation:** national −15/+15 crowns, −2/+2 iron; paired events; no minting or destruction. **Result:** `VERIFIED CONSISTENT` for the withholding; `VERIFIED WITH DOCUMENTED LIMITATION` for the gross service base and the unavailable ARL debit path.

### Example F — B-10 and B-04: military resource obligations

**Opening.** Standard start; garrison 200 `UNIT-INF` + 300 `UNIT-ARM` = 2,000 + 1,200 = **3,200 equivalents** → `ceil(3,200/1,000) = **4 Food**`. **Formulas:** F-WR-036; F-EC-002a/002/003/018; ECN-214.

| Phase | Arithmetic | Result |
|---|---|---|
| P3.6 | civilian demand 50; available 180; consumed 50 | food 130; unmet 0 |
| P3.7 6(a) | ration 4 ≤ 130 | food **126**; readiness unchanged |
| P3.7 7(b) | service 30 | treasury **1,499** |

**Short case.** Opening food 45, no food capacity, garrison 3,200 equivalents: P3.6 consumes 45 of 50 (unmet 5, hunger 300); P3.7 has 0 Food left, so the whole 4-Food ration is **cancelled**, `RATION_SHORT` is set and readiness falls by B-10's 100 points. No civilian Food is diverted and no unit is deleted. **OP-09:** a 4-Food field ration is reserved only from the surplus above the protected 50; with 54 available the reservation stands and civilians eat 50; with 49 the reservation is released, civilians eat 49 and the unmet ratio is 1/50. **Result:** `VERIFIED CONSISTENT`; B-04 does not redefine the military quantity.

### Example G — the full integrated economic turn

**Opening.** Standard start. **Accepted manual order:** one refining batch. **Alliance:** Crowns 1,000 bp, iron 2,500 bp. **Garrison:** 50 INF (1 Food). **Fiscal:** STANDARD. **Formulas:** F-EC-001…018; ECN-213a; F-WR-036; F-PD-020.

| Phase | Flow | Treasury |
|---|---|---:|
| Opening | — | 1,500 |
| P3.1 | tax 150; alliance Crowns −15 | 1,635 |
| P3.2 | maintenance 11 | 1,624 |
| P3.3 | food 60/−36; coal 20/−20; oil 8/−14; iron 10/−10; alliance iron −2 | 1,544 |
| P3.4 | 6 coal + 10 → 6 GU | 1,534 |
| P3.5 | manual refining 1: 10 oil + 20 → 8 gasoline | 1,514 |
| P3.6 | civilians eat 50 → food 130 | 1,514 |
| P3.7 | military ration 1 → food 129; service 30 | **1,484** |
| P3.8 | close | **1,484** |

**Closing:** food 129, coal 74, oil 28, iron 38, bauxite 20, lead 10, gasoline 28, steel 20 = **347 units**; book **675**; wealth **2,159**. **Conservation:** treasury `1,500+135−11−80−10−20−30 = 1,484`; resources `310+106−69 = 347`; wealth `2,159 = 2,100 + 59`; alliance `−15/+15` crowns and `−2/+2` iron. **Result:** `VERIFIED CONSISTENT`; every interacting system's definition is used once.

### Example H — the standard start with the B-06 service cost

**Opening.** Standard start; no manual orders; no military; STANDARD fiscal. **Formulas:** F-EC-001/014/016/018; F-PD-020.

| Phase | Flow | Treasury |
|---|---|---:|
| P3.1 | tax 150 | 1,650 |
| P3.2 | maintenance 11 | 1,639 |
| P3.3 | 80 | 1,559 |
| P3.4 | 10 | 1,549 |
| P3.5 | 20 | 1,529 |
| P3.6 | food 180 → 130; no shortage | 1,529 |
| P3.7 | service 30 | **1,499** |
| P3.8 | close | **1,499** |

**Measures:** capacity-operating income **+29**; net operating income after obligations **−1**; net cash flow **−1**; inventory book-value change **+78**; **net economic result +77**; gross output value **154**; wealth **2,177**. **Difference from Example 2:** Example 2 isolates B-04 capacity operations and closes at 1,529; Example H is the complete cross-system standard turn and closes at 1,499. Both are correct under their stated scope; presenting 1,529 as the standard start's closing balance without the service cost was the pre-14B omission (C-01/C-13).

---

## 7. Numerical decisions and change control

Four decisions were recorded under D-014. **No coefficient, recipe, tax rate or reference price changed.** The decisions are structural/completeness corrections plus one report-definition correction; the only example values that changed are the construction illustration in Example 4 (a placeholder replaced by B-05's authoritative cost) and the corrected scope/target statements.

### 7.1 D-240 — adopt the B-06 public-service cost as a P3.7 obligation

| Field | Record |
|---|---|
| 1 Existing state | B-04 had no public-service cost; P3.7 named military obligations and "other declared upkeep" only; `ECN-165` had no `POLICY_SERVICE_*` events; `F-EC-018`'s `operating` variable was undefined. |
| 2 Proposed state | Adopt B-06 `F-PD-020` at **P3.7 rank 7(b)** after facility upkeep; add `POLICY_SERVICE_COST` and `POLICY_SERVICE_CANCELLED`; define `operating` in F-EC-018 as every operating outflow actually paid, including P3.7 obligations; keep `net_operating_income` capacity-only and publish `net economic result`. |
| 3 Unit | Crowns. |
| 4 Numerical status | B-04 receiving rule: **DESIGN PROPOSAL**; B-06 amount: **PROVISIONAL VALUE**. No B-04 constant changed. |
| 5 Authorized owner | B-06 owns the formula, share and modifier; B-04 owns the receiving settlement and ledger treatment. |
| 6 Formula dependencies | F-EC-001 (gross tax), F-EC-016 (capacity income), F-EC-018 (closing identity). |
| 7 Cross-system dependencies | B-06 `F-PD-020`, `DMP-097`, `DMP-118`, `DMP-135`; B-09 `ECN-213a` (the service base is gross, before the alliance withholding). |
| 8 Old calculation | Standard start capacity income `150 − 121 = **+29**`; closing treasury **1,529** (Example 2's capacity-only scope). |
| 9 New calculation | Full standard turn `150 − 121 − 30 = **−1**`; closing **1,499**; net economic result **+77** (Example H). |
| 10 Economic consequences | The standard start is cash-neutral, not cash-positive; the service cost is 19.9% of gross tax at `STANDARD`; the first deliberate decision must turn the cash line positive. |
| 11 Treasury consequences | −30 crowns/turn at `STANDARD`; 0 at `LOW`; 100 at `HIGH` (before the government modifier). |
| 12 Resource consequences | None (crowns only). |
| 13 Affected worked examples | Example 2 gains a scope note; Example H is added as the integrated standard turn; Examples C, E, F, G include the service cost. `ECN-185` target 1 and `ECN-186` are restated. |
| 14 Alternatives considered | (a) Leave B-04 unchanged — rejected: the standard turn would be wrong by 30 crowns and the ledger would omit a real flow; (b) fold the service cost into `operating_expenses` — rejected: B-06 defines a cancellable P3.7 obligation, and capacity-operating income should stay comparable across turns with and without services; (c) adopt it at P3.7 rank 7(b) — **chosen**. |
| 15 Rationale | B-06 supplies the amount and the phase; B-04 is the receiving treasury and ledger. The adoption is one-way: B-04 does not redefine the service formula, share or modifier. |
| 16 Evidence | B-06 `F-PD-020` (P3.7, discretionary, cancelled whole), `DMP-097` (cost formula), `DMP-118` (two ledger events), `DMP-135` (B-04 adds the pointer); 14B Example H arithmetic. |
| 17 Confidence | High for the mechanism; medium for the balance consequence (no playtest). |
| 18 Required validation | 14B model (executed); Prompt 14 balance; a playtest of the first three turns. |
| 19 Reopening conditions | B-06 changes the formula, phase, share set or default government; a playtest shows the cash-neutral start is the wrong feel; a later prompt adds a second service cost. |
| 20 Decision ID | **D-240**; design-register pair **DD-286**. |

### 7.2 D-241 — consume the B-05 research modifiers and place facility upkeep

| Field | Record |
|---|---|
| 1 Existing state | F-EC-004/012 used the base output `Y`; F-EC-014 used a flat 2 per processing batch; B-05 facility upkeep had no B-04 placement. |
| 2 Proposed state | `Y_eff = Y + yield_bonus(r)` in F-EC-004/012 (including the space limit); `max(1, 2 − standards_bonus)` in F-EC-014 for processing only; facility upkeep at **P3.7 rank 7(a)**. |
| 3 Unit | Units (output), crowns (maintenance/upkeep). |
| 4 Numerical status | **DESIGN PROPOSAL** (contract completion). At launch both bonuses are 0 and there is no lab or civic centre, so every published number is unchanged. |
| 5 Authorized owner | B-05 owns the modifiers and upkeep amounts; B-04 consumes them. |
| 6 Formula dependencies | F-EC-004, F-EC-012, F-EC-014. |
| 7 Cross-system dependencies | B-05 `F-CI-015`, `F-CI-016`, `F-CI-017`, `URB-059`, `URB-060`. |
| 8 Old calculation | Space limit `floor(free_space / Y)`; processing maintenance `C × 2`. |
| 9 New calculation | `floor(free_space / Y_eff)`; `C × max(1, 2 − standards_bonus)`; identical at launch (bonus 0). |
| 10 Economic consequences | A research yield bonus cannot overrun the warehouse; the Standards Bureau can reduce processing maintenance to a floor of 1, not 0. |
| 11 Treasury consequences | 0 at launch; later up to −1 crown per processing batch with the programme. |
| 12 Resource consequences | 0 at launch; later +bonus units per batch. |
| 13 Affected worked examples | Examples 2, 7, 9, 10 and 18 are unchanged at launch; Example B illustrates capacity/power; the 14B formula table records the contract. |
| 14 Alternatives considered | (a) Leave B-04 silent — rejected: `ECN-076` already promises a published modifier, and the space limit would be wrong once a bonus exists; (b) add new formula IDs — rejected: the meaning is unchanged and the 47-count must be preserved; (c) consume the existing IDs — **chosen**. |
| 15 Rationale | Contract completion without renumbering: the recipe's inputs are unchanged, the output and maintenance are the only modified quantities, and the modifier is B-05's. |
| 16 Evidence | B-05 `F-CI-015`/`016`/`017` expressions, caps and edge cases; `ECN-076`; 14B §2. |
| 17 Confidence | High. |
| 18 Required validation | 14B model (executed); B-05 validator; a later research playtest. |
| 19 Reopening conditions | B-05 changes the modifier caps or adds a second source; a new maintenance modifier appears without a B-04 consumer. |
| 20 Decision ID | **D-241**; design-register pair **DD-287**. |

### 7.3 D-242 — reconcile Example 4, publish the net economic result and correct the gasoline role

| Field | Record |
|---|---|
| 1 Existing state | Example 4 used 150 crowns + 10 steel + 5 gasoline, book 250, payback 36; `ECN-185` target 1 used net operating income; `ECN-186` claimed a positive net operating income with no action; the roster called gasoline a construction fuel. |
| 2 Proposed state | Example 4 uses the B-05 `bld_farm` (120 crowns + 5 steel, book 155, payback 23); `ECN-185` target 1 uses `net economic result`; `ECN-186` states the measured −1; the roster and `ECN-028` stop claiming an implemented construction-fuel sink. |
| 3 Unit | Crowns, units. |
| 4 Numerical status | Examples: **PROVISIONAL VALUE**; report definition: **DESIGN PROPOSAL**; gasoline role: factual correction. |
| 5 Authorized owner | B-04; B-05 owns the construction cost; B-05 owns any future gasoline material cost. |
| 6 Formula dependencies | F-EC-016, F-EC-017, F-EC-025, F-EC-026, F-EC-027, F-EC-032. |
| 7 Cross-system dependencies | B-05 `URB-055`, `F-CI-012`; B-13 reporting; B-07/B-10 for gasoline's actual sinks. |
| 8 Old calculation | `150 + 10×7 + 5×6 = 250`; `ceil(250/7) = 36`; standard net +29. |
| 9 New calculation | `120 + 5×7 = 155`; `ceil(155/7) = 23`; standard net economic result +77. |
| 10 Economic consequences | The first farm pays back in 23 turns, not 36; the early-game target counts the value produced, not only cash. |
| 11 Treasury consequences | Capex at P4.1 is 120 crowns, not 150; the materials are 5 steel, not 10 steel + 5 gasoline. |
| 12 Resource consequences | A farm consumes no gasoline; gasoline's implemented sinks are military fuel and trade. |
| 13 Affected worked examples | Example 1 (ten turns of 151), Example 2 (scope note), Example 4 (rebuilt), Example 16 (band note), Example H (new), `ECN-117`, `ECN-185`, `ECN-186`, `ECN-208`, register F-EC-026/027/032 and index row 4. |
| 14 Alternatives considered | (a) Keep the placeholder — rejected: it contradicts B-05 and misstates the payback; (b) use a different building — rejected: one food batch is the farm; (c) adopt the farm — **chosen**. |
| 15 Rationale | B-04's own `ECN-228` already said construction costs were Prompt 05's; the placeholder had to be replaced once B-05 published the catalogue. |
| 16 Evidence | B-05 `URB-055` (farm 120 crowns, 5 steel, 1 DC), `F-CI-012` (book 155); 14B validator Example 4. |
| 17 Confidence | High. |
| 18 Required validation | `verify_economy_numbers.py` (170/170) and `14B_verify_b04_economy.py` (executed). |
| 19 Reopening conditions | B-05 changes the farm cost or adds a gasoline material cost; a later prompt redefines the early-game target. |
| 20 Decision ID | **D-242**; design-register pair **DD-288**. |

### 7.4 D-243 — record the 14B findings and the 30-turn measurement without retuning

| Field | Record |
|---|---|
| 1 Existing state | No 14B findings register; F-EC-039 unmeasured; the standard start's balance unexamined after the service-cost adoption. |
| 2 Proposed state | Record findings F14B-01…F14B-20, the 30-turn reference model and the cross-system matrix; **retain every value** and every `PROVISIONAL VALUE` status; defer any retune to the Prompt 14 balance phase and playtesting. |
| 3 Unit | n/a (analysis). |
| 4 Numerical status | All B-04 values remain **PROVISIONAL VALUE**. |
| 5 Authorized owner | B-04 for the analysis; Prompt 14 for the balance decision. |
| 6 Formula dependencies | F-EC-036, F-EC-037, F-EC-038, F-EC-039. |
| 7 Cross-system dependencies | B-05 (capacity/capital), B-06 (service/stability), B-09 (alliance), B-10 (military). |
| 8 Old calculation | No measurement. |
| 9 New calculation | Gross money-creation 4,500 vs 4,476 (fails by 24); net +30 (passes); idle fails both; the refinery idles 3 of 30 turns; power is overbuilt 4 GU. |
| 10 Economic consequences | Thin gross margin; cash-neutral start; oil is the binding input; steel is the practical first manufacturing build; refining is the weakest chain. |
| 11 Treasury consequences | Producing closes at 1,530; idle at 3,713. |
| 12 Resource consequences | Producing closes with 1,516 units; idle with 130 and no food. |
| 13 Affected worked examples | 14B §4.9 and §4.10; no B-04 example changed except Example 4 (D-242). |
| 14 Alternatives considered | (a) Retune a coefficient now — rejected: no playtest evidence and the values are provisional; (b) leave F-EC-039 unmeasured — rejected: the rule requires a measurement; (c) measure and record — **chosen**. |
| 15 Rationale | The assignment requires the consequences of the actual rules, not a retune to make a target pass. A recorded failure with a named cause is more useful than an unmeasured claim. |
| 16 Evidence | `14B_verify_b04_economy.py` output; §4.9/§4.10 tables. |
| 17 Confidence | Medium for the model; low for the balance. |
| 18 Required validation | Playtest; Prompt 14 balance; a 100-turn trade-pair and a 20-nation model. |
| 19 Reopening conditions | Any coefficient change; any playtest result; a decision on the gross/net reading of F-EC-039. |
| 20 Decision ID | **D-243**; design-register pair **DD-289**. |

### 7.5 Change-control compliance

- **F-EC-041 (changing a number):** no number changed. Example 4's illustration changed because it was a placeholder, not a constant; the old value is preserved in this report and in F-EC-044.
- **F-EC-042 (changing a formula):** the four formula edits are variable/definition completions, not meaning changes; the previous expressions are preserved in F-EC-044. No new formula ID was added.
- **F-EC-043 (adding a formula):** none added; `net economic result` is a report definition, which F-EC-043 explicitly excludes from the formula count.
- **F-EC-045 (validation record):** the 14B commands and results are appended in §8.
- **F-EC-046 / ECN-228:** the non-validation statements are extended, not weakened.

---

## 8. Validation and regression evidence

### 8.1 Executed commands and actual results

All commands were run from `docs/` with Python 3.12 on Windows on 2026-11-17. The results below are the actual terminal output, not a recollection.

| # | Command | Scope | Actual result | Exit |
|---:|---|---|---|---|
| 1 | `python qa_backups/verify_economy_numbers.py` | B-04 bundle, margins, Examples 1–20, cross-document Example 5, headers, stale tokens | **PASS: 170/170 economy arithmetic checks passed** | 0 |
| 2 | `python qa_backups/14B_verify_b04_economy.py` | 14B independent arithmetic: constants, 20 examples, margins, conservation, negative tests, A–H, 30-turn model, document tokens | **PASS: 321/321 Prompt 14B checks passed** | 0 |
| 3 | `python qa_backups/14B_verify_b04_economy.py --self-test` | Four deliberate mutations (price, recipe, negative treasury, duplicate settlement) | **SELF-TESTS: 4 cases**, all detected | 0 |
| 4 | `python qa_backups/verify_city_numbers.py` | B-05 city/construction/research arithmetic | **PASS: 267/267** | 0 |
| 5 | `python qa_backups/verify_market_numbers.py` | B-07 trade arithmetic | **MARKET VALIDATION: ALL CHECKS PASSED** | 0 |
| 6 | `python qa_backups/verify_diplomacy_numbers.py` | B-08 arithmetic and structure | **9 groups, 0 failed** | 0 |
| 7 | `python qa_backups/verify_alliance_numbers.py` | B-09 arithmetic and document checks | **375 passed, 0 failed** | 0 |
| 8 | `python qa_backups/verify_warfare_workflows.py` | B-10 workflows and fixtures | **49/49 executed, 0 failed** | 0 |
| 9 | `python qa_backups/verify_alliance_workflows.py` | B-09 workflows | **ALL CHECKS PASSED** | 0 |
| 10 | `python qa_backups/verify_diplomacy_workflows.py` | B-08 workflows | **17 groups, 0 failed** | 0 |
| 11 | `python qa_backups/verify_market_workflows.py` | B-07 workflows | **07C VALIDATION: ALL CHECKS PASSED** | 0 |
| 12 | `python qa_backups/09_validate.py` | B-03 structure and continuity | **371/371** | 0 |
| 13 | `python qa_backups/09A_validate_alliance.py` | B-09 structure | **943 checks, 2 inherited failures** (stale handoff/next-prompt guards) | **1 (inherited)** |
| 14 | `python qa_backups/09B_validate_alliance_semantic.py` | B-09 semantic | **8 inherited problems** (frozen D/DD ranges and next-prompt guard) | **1 (inherited)** |
| 15 | `python qa_backups/10B_validate_warfare.py` | B-10 structure, formulas, boundaries | **1036 checks; 73/73 negative fixtures rejected** | 0 |
| 16 | `python qa_backups/11A_validate_research.py` | 11A research quality | **30 checks, 1 inherited failure** (`REQ-703` frozen maximum) | **1 (inherited)** |
| 17 | `python qa_backups/11B_validate_b11.py` | B-11 specification, 52 gates, link subprocess | **61/61 checks; 52/52 gates PASS; links 0 unresolved** | 0 |
| 18 | `python qa_backups/11C_validate_b11_workflows.py` | B-11 workflows | **PASS** | 0 |
| 19 | `python qa_backups/12A_validate_foundations.py` | B-12 research foundations | **PASS**, 0 gaps | 0 |
| 20 | `python qa_backups/12B_validate_b12.py` | B-12 specification | **87/87** | 0 |
| 21 | `python qa_backups/12C_validate_fair_play_workflows.py` | B-12 workflows | **24/24** | 0 |
| 22 | `python qa_backups/13A_validate_ui_foundations.py` | 13A UI foundations | **34/34** | 0 |
| 23 | `python qa_backups/13B_validate_ui_specifications.py` | 13B screens/components | **28/28** | 0 |
| 24 | `python qa_backups/13C_validate_interaction_specs.py` | 13C interactions | **27/27** | 0 |
| 25 | `python qa_backups/13D_validate_integration.py` | 13D integration | **75/75** | 0 |
| 26 | `python qa_backups/14A_validate_numerical_foundation.py` | 14A documentary architecture | **64 checks, 0 failed** | 0 |
| 27 | `python qa_backups/14A_contract_validator.py` | Controlled contracts | **9/9 checks; 11 mappings, 0 reviewed, 11 NOT_REVIEWED** | 0 |
| 28 | `python qa_backups/test_14A_contract_validator.py` | Contract regression | **83 tests OK** | 0 |
| 29 | `python qa_backups/test_14A_trusted_amendment_security.py` | C2 security | **46 tests OK** | 0 |
| 30 | `python qa_backups/test_14A_metadata_diff.py` | C3 metadata | **8 tests OK** | 0 |
| 31 | `python qa_backups/validate_final.py` | Project-wide final validator | **VALIDATION: ALL CHECKS PASSED** | 0 |
| 32 | `python qa_backups/validate_links.py` | Documentation links | **144 files; 4,546 links; 4,164 local; 382 external; 34 anchors; 0 unresolved** | 0 |
| 33 | `python qa_backups/test_decision_registers.py` | UD register | **12 tests OK** | 0 |
| 34 | `python qa_backups/test_next_action.py` | Continuity / next action | **27 tests OK** | 0 |
| 35 | `python qa_backups/verify_politics_numbers.py` | B-06 arithmetic and guards | **878/879; 1 inherited stale guard** | **1 (inherited)** |

**Inherited failures preserved.** The four historical failures are unchanged in cause and are not edited to pass: `verify_politics_numbers.py` (a progress-log guard frozen at "Prompt 13C next"), `11A_validate_research.py` (a frozen `REQ-703` maximum), `09A_validate_alliance.py` (two stale continuity guards) and `09B_validate_alliance_semantic.py` (frozen D/DD ranges and a next-prompt guard). Prompt 14A recorded them; Prompt 14B neither introduces nor hides them.

**Expectation advances made by 14B.** Adding D-240…D-243 / DD-286…DD-289 moved the source-evidenced register maxima. The frozen expectations in `validate_final.py` (DD count), `09_validate.py` (DD contiguity), `12A_validate_foundations.py` and `13A`/`13B` (decisions range, DD maximum, status date), `test_next_action.py` (row 13/14 status), `14A_validate_numerical_foundation.py` (B-04 §3.3/§3.4 timing), `verify_economy_numbers.py` (Example 4 and header versions) and `test_next_action.py` were advanced to the new truth. No check was deleted, relaxed or converted into a warning.

**Trusted-evidence refresh.** The B-04 register, B-14 and `DECISIONS.md` were legitimately amended (D-240…D-243). The controlled contracts `NC-F-EC-000b` and `NC-F-EC-000f` and their projections were **not** changed: the protected clauses `F-EC-000b` and `F-EC-000f` are byte-identical, and the contract validator's clause fingerprints still pass. Only the whole-document hashes in `index.json` and `evidence_mappings.json` were refreshed, and the 11 evidence mappings remain `NOT_REVIEWED`; no human review or owner authorization is claimed. The `evidence_mappings.json` file hash in the registry index was recomputed after the refresh.

### 8.2 Positive regression coverage

The 14B validator and the existing suites cover: the standard bundle (310 units, 600 book, 2,100 wealth, 1,690 free); tax (150 at the standard start; 300 at 100,000 people); food sufficiency and shortage (0 / 20 / 50 unmet; 0 / 600 / 3,000 bp); seven extraction chains; three generators and fail-closed fuel; four recipes; maintenance and the whole-obligation allocation; trade accounting (paired, fee-free); alliance taxation (Crowns and iron; cumulative 2+3=5 vs independent 2+2=4); military ration (4 Food; whole cancellation); positive treasury movement; resource conservation (310+106−69=347); treasury conservation (1,500+135−11−80−10−20−30=1,484); and the full integrated settlement.

### 8.3 Negative and boundary coverage

The 14B model rejects: a negative crown balance; a negative resource quantity; an unknown resource; an alliance rate above 10,000 bp; a negative alliance rate; a manual order above capacity; a negative manual order; a negative military force; a negative population; a tax rate above 10,000 bp; a service share above 5,000 bp; an unaffordable batch; a space-blocked batch; a power-starved chain; a short-input batch; an unfunded service; and a cancelled ration. Duplicate settlement and duplicate event keys are no-ops. The document-token guards reject the superseded "250/36" Example 4, the stale "twelve turns of 121/turn" claim, the false "positive net operating income by doing nothing" claim, the "P3.7 generator" timing and the "gasoline → construction fuel" claim. The inherited four failures are documented rather than bypassed.

### 8.4 Independent arithmetic

The 14B validator is a separate calculation path from `verify_economy_numbers.py`: it re-derives the constants, the 20 examples, the margins, the integrated examples and the 30-turn model from the published values and does not import the economy validator. The two paths agree on every shared figure (bundle, Example 2, Example 3, margins, Example 4's corrected 155/23, wealth and the treasury identity).

**14B-C1 / R1 closeout evidence (2026-11-17).** The C1 closeout added the targeted validator [`14B_C1_validate_closeout.py`](../qa_backups/14B_C1_validate_closeout.py), which after the R1 extension passes **1,330/1,330** checks and **10/10** mutation tests (49 D-014 category rows with resolved decision references, 35 matrix rows at 27/4/4/0 with the 18-entry register separate, 17 crosswalk rows, and seven separate evidence dimensions). The corrected matrix tallies, the seven-dimension QA crosswalk and the final link count are recorded in the [C1 closeout report](26_prompt_14B-C1_closeout_report.md), [R1 closeout report](27_prompt_14B-C1-R1_closeout_report.md) and [QA report §8](22_numerical_baseline_qa_report.md). No value changed.

### 8.5 What the validation does not prove

Passing documentation validators does not prove runtime implementation. Passing arithmetic tests does not prove gameplay balance. The 30-turn model is deterministic hand-equivalent arithmetic, not a scheduler, database or player experience. No B-04 formula has been executed against a database or a scheduler; the semantic-contract evidence mappings remain `NOT_REVIEWED`; and the standard start has not been playtested.

---

## 9. Completion assessment and remaining limitations

### 9.1 Completion categories (reported separately)

| # | Category | Status | Basis |
|---:|---|---|---|
| 1 | Formula specification | **COMPLETE** | 47 identifiers reconciled; 4 contract completions; no formula added, renumbered or retired |
| 2 | Parameter inventory | **COMPLETE** | 49 records reconciled; every status retained; 2 metadata defects corrected |
| 3 | Numerical calculation | **COMPLETE for the documented model** | 20 examples + A–H + 30-turn model reproduced |
| 4 | Resource accounting | **COMPLETE** | 11-resource conservation in A/G and the 30-turn model |
| 5 | Treasury accounting | **COMPLETE** | closing identity, reservations, obligations and wealth reconciliation |
| 6 | Cross-system consistency | **COMPLETE for B-02/03/05/06/07/08/09/10** | 35 matrix rows: 27 consistent, 4 documented limitation, 4 contradiction identified, 0 not yet verified; 18-entry contradiction register and 2 B-06 items kept separate |
| 7 | Worked examples | **COMPLETE** | 20 recalculated; A–H added; all reproducible |
| 8 | Validator and regression tests | **COMPLETE** | actual results in §8; 4 inherited failures preserved |
| 9 | Economic balance assessment | **NOT ACCEPTED** | findings recorded; no retune; gross money-creation test fails by 24 |
| 10 | Playtesting requirements | **REQUIRED, NOT EXECUTED** | see §9.2 |
| 11 | Runtime implementation | **NOT STARTED** | no code, database, scheduler or deployment |

### 9.2 Playtesting requirements

The following must be tested before any claim of balance:

1. A 30-turn standard-start playtest on each of the three early paths (food, energy/refining, metals), measuring net economic result, cash, inventory and the first refinery idle.
2. A 100-turn two-nation trade pair, testing whether refining's gasoline margin and steel's construction demand produce the intended specialisation.
3. A 100-turn 20-nation world with random policies, measuring treasury p90/p10, wealth Gini, food- and power-shortage frequency, idle-capacity share and negative-cash-flow turns.
4. A price-shock scenario (gasoline 5 vs 7; bauxite 2.17; aluminium 7.75) to test the published break-evens.
5. A food-shortage scenario (20 unmet; 1,200 bp; recovery) and a war-consumption scenario (B-10 supply and ration).
6. A reroll scenario (asset destruction, no transfer).
7. A policy test of the three fiscal settings and six governments, including the public-service cost and the alliance withholding.
8. A 12-city development test of the 15-DC capital and the 17-DC overdraw (Example B).

### 9.3 Remaining limitations

1. **No runtime.** No formula, settlement, database, scheduler, market or UI exists. Nothing here is implemented.
2. **No simulation or player.** The 30-turn model is deterministic arithmetic; the standard start is not playtested.
3. **No balance acceptance.** The standard start is cash-neutral (−1/turn); the gross money-creation reading fails by 24 crowns; refining is loss-making at actual utilisation; oil binds; power is overbuilt. These are recorded, not retuned.
4. **B-06 owns two residual defects.** `DMP-135`'s P3.7/P3.8 wording and `DMP-097a`'s `ECN-081` citation are **OUTSIDE PROMPT 14B AUTHORITY**.
5. **B-05 does not implement gasoline's construction-fuel role.** B-04's claim is corrected; B-05 may add a material cost in a later balance pass.
6. **F-EC-039's gross/net reading is undecided.** Both are measured; the final reading is a Prompt 14 balance decision.
7. **`UD-040` and `UD-046` remain Open.** No general Alliance treasury right, ownership, custody or capacity is created.
8. **Contract evidence remains `NOT_REVIEWED`.** No human review or owner authorization is claimed; the hashes were refreshed as a controlled-evidence amendment, not as a review.
9. **The four inherited validator failures remain.** They are documented, not repaired.
10. **No owner acceptance of Prompt 14B.** The owner retains acceptance and commit authority.

### 9.4 Final completion assessment

**Prompt 14B is COMPLETE at the documentation, numerical-analysis and document-validation level.** The 47 formulas and 49 parameter records are reconciled; the starting economy, the four production chains, the seven extraction chains, the three generators, food, maintenance, treasury, inventory, reference prices and margins are calculated; the 11-resource and treasury conservation identities hold in the integrated examples; the cross-system matrix is complete for the in-scope systems; the 20 existing examples and the eight integrated examples are reproducible; the semantic-contract safeguards are preserved; and the validators and regressions have been executed with the actual results recorded above.

**It is not complete as an implementation, a balance result or a playtest.** No value was retuned; the standard start is cash-neutral; the gross money-creation test fails by 24 crowns; and the Prompt 14 balance phase and playtesting remain ahead. Prompt 14C–14K are **NOT AUTHORIZED**.

---

## 10. Git closeout

**Branch:** `main`. **HEAD:** `bff91193f946ce77f60da9a838d5d76364552ed5`. **Staged:** 0. No staging or commit was performed.

**Working-tree state at the end of Prompt 14B (read-only measurement):** **25 modified tracked paths, 4 untracked files, 29 individual paths, 0 staged.**

| # | Modified tracked path | Nature |
|---:|---|---|
| 1 | `docs/AI_CONTEXT.md` | continuity status |
| 2 | `docs/AI_HANDOFF.md` | continuity status and next action |
| 3 | `docs/DECISIONS.md` | D-240…D-243 and header |
| 4 | `docs/PROJECT_PROGRESS.md` | continuity status |
| 5 | `docs/prompts/INDEX.md` | 14B archive row |
| 6 | `docs/qa_backups/09_validate.py` | decision-range expectation |
| 7 | `docs/qa_backups/12A_validate_foundations.py` | decision-range expectation |
| 8 | `docs/qa_backups/13A_validate_ui_foundations.py` | range/date/DD expectation |
| 9 | `docs/qa_backups/13B_validate_ui_specifications.py` | range/date expectation |
| 10 | `docs/qa_backups/14A_validate_numerical_foundation.py` | B-04 timing expectation |
| 11 | `docs/qa_backups/test_next_action.py` | current-position assertions |
| 12 | `docs/qa_backups/validate_final.py` | DD count and word map |
| 13 | `docs/qa_backups/verify_economy_numbers.py` | Example 4, headers, guards |
| 14 | `docs/stage-2/00_stage_2_handoff.md` | current next action |
| 15 | `docs/stage-2/01_stage_2_prompt_roadmap.md` | row 13/14 status |
| 16 | `docs/stage-2/04_approved_and_provisional_decisions.md` | DD-286…DD-289 |
| 17 | `docs/stage-2/06_stage_2_progress_log.md` | header, current task, §113 |
| 18 | `docs/stage-2/10_economic_formula_and_balance_register.md` | v1.5 |
| 19 | `docs/stage-2/10_economy_resources_treasury_and_finances.md` | v2.1 |
| 20 | `docs/stage-2/22_formula_master_inventory.md` | B-04 line refs and F-EC-002a gap |
| 21 | `docs/stage-2/22_formulas_and_balance.md` | v1.5 and §19 |
| 22 | `docs/stage-2/22_numerical_contracts/evidence_mappings.json` | refreshed document hashes |
| 23 | `docs/stage-2/22_numerical_contracts/index.json` | refreshed source-document and evidence hashes |
| 24 | `docs/stage-2/22_numerical_parameter_inventory.md` | B-04 unit/timing metadata |
| 25 | `docs/stage-2/22_numerical_baseline_qa_report.md` | 14B execution record (§7) |

| # | Untracked file | Purpose |
|---:|---|---|
| 1 | `docs/prompts/prompt_14B_b04_economy_resources_income_treasury.md` | archived assignment (47,867 bytes; 1,826 LF; SHA-256 `85aa63e5…`) |
| 2 | `docs/qa_backups/14B_verify_b04_economy.py` | independent 14B arithmetic and regression suite |
| 3 | `docs/stage-2/24_prompt_14A_owner_acceptance.md` | acceptance record referenced by the continuity files |
| 4 | `docs/stage-2/25_prompt_14B_b04_economy_completion_report.md` | this report |

**Generated cache artifacts.** `docs/qa_backups/__pycache__/` may contain refreshed `.pyc` files from the executed validators (for example `14B_verify_b04_economy.cpython-312.pyc`, `14A_contract_validator.cpython-312.pyc`, `14A_validate_numerical_foundation.cpython-312.pyc`). They are generated, ignored by `.gitignore` (`__pycache__/`, `*.pyc`), not tracked and not substantive changes. No cache file was deleted or manipulated and the tracking policy was not changed.

**Validation commands and results.** The 35 commands and their actual results are recorded in §8.1. No result is a recollection; each was executed in this session. The four inherited historical failures remain and are not attributed to Prompt 14B.

**Git actions.** No `git add`, `git commit`, `git checkout`, `git reset`, `git clean`, `git stash`, branch creation or push was performed. The owner retains commit authority.

**14B-C1 note.** The working-tree counts above are the Prompt 14B-time measurement. The current 14B-C1 working-tree state, including the three new C1 files, is recorded in the [C1 closeout report §E](26_prompt_14B-C1_closeout_report.md). The owner-reported 14B commit was not present in this repository at the start of C1; `HEAD` remained `bff9119` and no commit was amended, rewritten or created.
