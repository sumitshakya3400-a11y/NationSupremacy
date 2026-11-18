# Prompt 14B-C1-R1-R1 — closeout report

**Stage:** Stage 2 · **Parent:** Prompt 14B — B-04 economy, resources, income and treasury · **Correction:** 14B-C1-R1-R1
**Executed:** 2026-11-17 · **Status:** **`COMPLETE` at the documentation/QA level**
**Scope:** eliminate the two reproduced false-pass conditions in the 14B-C1 source-reference validator, add real end-to-end mutation coverage, record semantic-review limitations, and reconcile the raw and normalized Git state. No economic value, formula, numerical status, classification, matrix row or owner-reserved decision changed.
**Parent reports:** [14B report](25_prompt_14B_b04_economy_completion_report.md) · [C1 report](26_prompt_14B-C1_closeout_report.md) · [R1 report](27_prompt_14B-C1-R1_closeout_report.md) · **Archive:** [R1-R1 archive](../prompts/prompt_14B-C1-R1-R1_end_to_end_source_reference_validation_and_adversarial_mutation_testing.md) · **Progress log:** [§116](06_stage_2_progress_log.md)

---

## A. Original defect reproduction

The two Project X (112) false-pass attacks were reproduced **before** the validator was corrected, using a temporary copy of the live `docs` repository and the production entry point:

**Command (fixture):** `python <fixture>/qa_backups/14B_C1_validate_closeout.py`, cwd `<fixture>` (a complete temporary copy of `docs`).

| Step | Mutation | Production exit | Actual result | Verdict |
|---|---|---:|---|---|
| Baseline | none | **0** | `PASS: 1330/1330` | valid baseline |
| Attack A | crosswalk `ECN-214` → `ECN-999` | **0** | `PASS: 1330/1330` | **false pass reproduced** |
| Restore A | none | **0** | pass | restored |
| Attack B | crosswalk `14B_verify_b04_economy.py` → `14B_nonexistent_economy.py` | **0** | `PASS: 1330/1330` | **false pass reproduced** |
| Restore B | none | **0** | pass | restored |

**After the correction**, the same production entry point on the same fixture:

| Step | Production exit | Diagnostic |
|---|---:|---|
| Baseline | **0** | `PASS: 1620/1620` |
| Attack A | **1** | `X5 row 6 ECN ECN-999 exists: ECN-999` |
| Restore A | **0** | pass |
| Attack B | **1** | `X21 QA report validator 14B_nonexistent_economy.py exists: 14B_nonexistent_economy.py` |
| Restore B | **0** | pass |

Both attacks are now rejected by the full production validator with a targeted diagnostic, not by a helper predicate or an unrelated crash. The **1,620/1,620** figure in the table above was the production count at that intermediate stage, before the R1-R1 closeout-report checks were added. The final production validator count after all R1-R1 checks is **1,790/1,790** (see §E).

---

## B. Reference-resolver coverage

The validator now resolves the actual identifier and document forms in the 17-category crosswalk and the 49 parameter records.

| Namespace / reference | Authoritative source | Checked | Unresolved |
|---|---|---:|---:|
| Decision IDs (parameter rows) | `DECISIONS.md` rows `| D-### |` | **50 references across 49 rows**; 6 distinct IDs (D-045, D-046, D-048, D-052, D-058, D-063) | **0** |
| Decision IDs (crosswalk) | `DECISIONS.md` | **3 distinct** (D-046, D-058, D-063) | **0** |
| Decision IDs (R1/R1-R1 reports) | `DECISIONS.md` | **8 distinct** (D-014, D-044, D-045, D-046, D-048, D-052, D-058, D-063) | **0** |
| `ECN-*` | B-04 rulebook headings `**ECN-###` | **25 distinct** after range expansion | **0** |
| `F-EC-*` | B-04 formula register headings `**F-EC-###` | **31 distinct** after range expansion | **0** |
| `F-WR-*` | B-10 formula register headings `### F-WR-###` and its index table | **1 distinct** (`F-WR-036`) | **0** |
| Source sections (`§`) | B-04 rulebook, register, inventory, 14B report, this QA report | **44 section references** | **0** |
| Validator/test filenames | `qa_backups/*.py` | **5 distinct** crosswalk names plus global report names | **0** |
| Local report links | repository-relative paths within the repo root | all R1 and R1-R1 links | **0** |
| Human semantic reviews still required | — | **17 CW records** plus **5 SR records** | all **NOT PERFORMED** |

**Resolver behavior.** The validator distinguishes: a valid reference; an existing but wrong/irrelevant source (expected structural parent per group: D-045 extraction, D-046 recipes, D-048 generators, D-058 prices, D-063 bundle, D-052 warehouse); a superseded decision (rejected unless explicitly labelled `SUPERSEDED`/`HISTORICAL`); a missing or malformed identifier; a nonexistent file; a valid file with a nonexistent heading; a path outside the repository root; and a reference requiring human semantic review (recorded, not claimed as reviewed).

**Source-ID conventions.** The 49 records keep the source ID `None`; the record key is a source locator (`B-04 §section · name`), not a canonical parameter ID. No global parameter-ID namespace was created. The crosswalk's former local reading-key phrase (`R-01…R-24`) was replaced with “the 24 §3.1 records”; the 14B report's R-keys remain explicitly local.

### B.2 Crosswalk semantic review record

The automated checks prove existence, expected-parent relevance and status consistency. They do **not** prove that a human reviewer agrees with the relevance. The following CW record is reviewable structured evidence; every row's human-review status is `NOT PERFORMED`.

| CW | QA row | Source | Cited record | Claim | Relevance | Authority | Review status | Uncertainty |
|---|---|---|---|---|---|---|---|---|
| CW-01 | 1 | B-04 rulebook; B-04 register | `ECN-094`, `ECN-146`; `F-EC-001`, `F-EC-003` | P3.1 tax and hunger arithmetic | The cited records define the tax formula, hunger penalty and P3.1 timing that the row summarises. | Authoritative B-04 sources; Category B design with provisional numbers | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-02 | 2 | B-04 rulebook §13; register §4.3 | `ECN-119`–`ECN-130`; `F-EC-021`–`F-EC-023`, `F-EC-028`–`F-EC-030` | 11-resource inventory and conservation | The cited records define inventory, reservation, production, transfer and conservation accounting. | Authoritative B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-03 | 3 | B-04 register §3.1; D-063; inventory §6 | `ECN-121`; register §3.1; the 24 §3.1 records | Starting bundle and opening balances | The register's §3.1 table and D-063 record the bundle values; the inventory rows carry their metadata. | Authoritative B-04/D-063 sources; numbers provisional | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-04 | 4 | B-04; register §3.2 | `ECN-042`/`ECN-046`/`ECN-049`/`ECN-148`; `F-EC-004`/`F-EC-005` | Seven extraction chains | The cited records define batch capacity, extraction limits, variable cost and P3.3 timing. | Authoritative B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-05 | 5 | B-04 §10; D-046; register §3.3 | `ECN-066`–`ECN-079`; `F-EC-006`–`F-EC-012` | Four processing recipes | The cited records define the recipe table, power derating, input/money/space limits and P3.5 processing. | Authoritative B-04/D-046 sources; numbers provisional | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-06 | 6 | B-04 §11; B-10 `F-WR-036` | `ECN-080`–`ECN-091`, `ECN-214`; `F-EC-002`, `F-EC-002a`, `F-EC-003` | Civilian and military Food boundary | The cited records define civilian demand, hunger, the P3.7 military ration and the B-10 ownership boundary. | Authoritative B-04/B-10 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-07 | 7 | B-04 §9; register §3.4 | `ECN-056`–`ECN-065`; `F-EC-006`, `F-EC-007`, `F-EC-008`, `F-EC-013` | Generation, fuel and derating | The cited records define grid units, generator fuel/output, fail-closed operation and pro-rata derating. | Authoritative B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-08 | 8 | B-04 `ECN-051`, `ECN-105`, `ECN-147`, `ECN-147a` | `F-EC-014`; register §3.3/§3.4 | Maintenance and operating costs | The cited records define whole-obligation maintenance, its order and the operating-cost boundary. | Authoritative B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-09 | 9 | B-04 §12; register §4.3 | `ECN-092`–`ECN-118`, `ECN-125`–`ECN-128`; `F-EC-018`, `F-EC-019`, `F-EC-020` | Treasury, reservations and closing identity | The cited records define the treasury vocabulary, reservation model, closing identity and non-negative balance. | Authoritative B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-10 | 10 | Register §3.5/§5; D-058 | `F-EC-031`, `F-EC-032`, `F-EC-036`, `F-EC-037` | Reference prices and margins | The cited records define book values, base/loaded margins and payback. | Authoritative B-04/D-058 sources; prices provisional | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-11 | 11 | Register §4.3/§4.4 | `F-EC-024`, `F-EC-025`, `F-EC-026`, `F-EC-029`, `F-EC-030`, `F-EC-035` | Wealth and transfer conservation | The cited records define inventory/fixed-asset book value, transfer conservation and wealth reconciliation. | Authoritative B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-12 | 12 | 14B report §6; B-04 §20 | Examples 1–20; Examples A–H | Worked examples | The 14B report reproduces the 20 published examples and adds A–H from the same constants. | Authoritative 14B/B-04 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-13 | 13 | 14B report §5; B-02/B-03/B-05–B-10 sources | X-01…X-35; C-01…C-18 register | 35 dependency rows | The matrix records each dependency with source and receiving evidence; the register is separate. | Authoritative cross-system sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-14 | 14 | Inventory §6/§6.1 | 49 records; source IDs remain `None`; categories A/B/C/D | D-014 category metadata | The inventory rows record the category, authority, structural parent, rationale and evidence path. | Authoritative inventory/D-014 sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-15 | 15 | Register §5; 14B report §4.9/§4.10 | `F-EC-038`, `F-EC-039`; F14B-01…F14B-20 | Dominance and money-creation findings | The register defines the tests; the 14B report records the 30-turn reference model and findings. | Authoritative B-04/14B sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-16 | 16 | 14B report §8; this report §7 | 35 command rows | Validator execution results | The 14B report records the executed commands and actual output; the QA report records the 14B execution summary. | Authoritative execution records | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |
| CW-17 | 17 | 14B report §9; B-04 `ECN-228`; register `F-EC-046` | §9.1–§9.4 | Runtime, migration, balance and playtesting limitations | The cited records explicitly state what is not validated and where the runtime/playtest boundary lies. | Authoritative B-04/14B sources | NOT PERFORMED — automated existence/status check only | Human semantic review not performed. |

**Authority note.** The cited structural decisions are Category B decisions confirmed under delegated D-014 authority; they are **not owner approvals**, and their numerical parameters remain provisional where indicated. No owner approval is invented.

---

## C. Adversarial testing

### C.1 Method

[`14B_R1_R1_mutation_tests.py`](../qa_backups/14B_R1_R1_mutation_tests.py) creates **one temporary copy** of the live `docs` repository, runs the production validator on the clean fixture (exit 0), applies each mutation to a real document in that copy, runs the **same production validator** (`python <fixture>/qa_backups/14B_C1_validate_closeout.py`, cwd `<fixture>`), requires a nonzero exit with the intended diagnostic, restores the original file, and requires exit 0 again. The live repository is never modified. The 20 resolver positive controls are executed separately; they are **not** counted in the 15 production mutation totals.

### C.2 Mutation results

| ID | File | Original → Mutated | Expected | Exit | Diagnostic | Result |
|---|---|---|---|---|---:|---|---|
| M01 | `22_numerical_baseline_qa_report.md` | `ECN-214` → `ECN-999` | reject | 1 | `X5 row 6 ECN ECN-999 exists: ECN-999` | **PASS** |
| M02 | `22_numerical_baseline_qa_report.md` | `F-EC-001` → `F-EC-999` | reject | 1 | `X5 row 1 F-EC F-EC-999 exists: F-EC-999` | **PASS** |
| M03 | `22_numerical_baseline_qa_report.md` | `F-WR-036` → `F-WR-999` | reject | 1 | `X5 row 6 F-WR F-WR-999 exists: F-WR-999` | **PASS** |
| M04 | `22_numerical_parameter_inventory.md` | parent `D-063` → `D-999` (Treasury row) | reject | 1 | `A19 every cited decision exists: … ['D-999']` | **PASS** |
| M05 | `27_prompt_14B-C1-R1_closeout_report.md` | QA link → `22_nonexistent_qa.md` | reject | 1 | `R12 local link resolves: 22_nonexistent_qa.md` | **PASS** |
| M06 | `22_numerical_baseline_qa_report.md` | completion `14B §4.1` → `14B §99.9` | reject | 1 | `X4 row 1 completion section 14B §99.9 exists: 14B §99.9` | **PASS** |
| M07 | `22_numerical_baseline_qa_report.md` | `14B_verify_b04_economy.py` → `14B_nonexistent_economy.py` | reject | 1 | `X21 QA report validator 14B_nonexistent_economy.py exists: 14B_nonexistent_economy.py` | **PASS** |
| M08 | `22_numerical_parameter_inventory.md` | parent `D-063` → `D-004` (superseded) | reject | 1 | `A20 no cited decision is a superseded record presented as current: … ['D-004']` | **PASS** |
| M09 | `22_numerical_parameter_inventory.md` | recipe parent `D-046` → empty | reject | 1 | `A14 structural parent/source present: 'B-04 §3.3 · Refining'` | **PASS** |
| M10 | `22_numerical_parameter_inventory.md` | authority → `owner-approved constraint` | reject | 1 | `A21 decision authority wording is not an owner-approval claim: … owner-approved constraint` | **PASS** |
| M11 | `22_numerical_baseline_qa_report.md` | result → `playtest completed` | reject | 1 | `X11 row 1 result does not claim unsupported success: playtest completed` | **PASS** |
| M12 | `22_numerical_parameter_inventory.md` | category `C` → `E` | reject | 1 | `A11 D-014 category is valid: … E` | **PASS** |
| M13 | `22_numerical_parameter_inventory.md` | category `C` → `PROVISIONAL VALUE` | reject | 1 | `A11/A12 category/status violation: … PROVISIONAL VALUE` | **PASS** |
| M14 | `22_numerical_parameter_inventory.md` | key `B-04 §3.1 · Treasury` → `B-04 §3.1 · NP-EC-001 Treasury` | reject | 1 | `A5 record key name matches parameter: … NP-EC-001 Treasury` | **PASS** |
| M15 | `22_numerical_baseline_qa_report.md` | duplicate crosswalk row 1 | reject | 1 | `C2 source/result table has 17 rows: 18` | **PASS** |

**Total: 15/15 real end-to-end mutations rejected; 15/15 restored baselines passed.** The production entry point was used for every case; no helper predicate was counted as a mutation pass.

### C.3 Positive controls

**20/20 resolver positive controls passed:** valid D-063 resolves; a nonexistent decision ID is rejected; D-004 is superseded; D-063 is not; valid B-04 §13 resolves; §99 rejected; valid register §3.2 resolves; §99.9 rejected; valid report §4.1 resolves; §99.9 rejected; ECN range expands; delegated Category B wording accepted; owner-approved wording rejected; planned-playtest wording accepted; completed-playtest wording rejected; category C distinct from a status; status-as-category rejected; valid local link resolves; missing local link rejected; a superseded decision explicitly labelled `SUPERSEDED` is acceptable. The last is a resolver-logic control; no live row currently cites a superseded decision.

**Helper-vs-production distinction.** The 20 controls are resolver-level tests and are reported separately. The 15 production mutations above are the only cases counted in the mutation total.

---

## D. Baseline integrity

| Item | Verified value |
|---|---:|
| B-04 parameter records | **49** |
| D-014 Category A / B / C / D | **0 / 0 / 49 / 0** |
| Unresolved classifications | **0** |
| Numerical statuses | **49 `PROVISIONAL VALUE`** |
| Source IDs | **all `None`**; no fabricated IDs |
| Cross-system dependency rows | **35** |
| Matrix totals | **27 `VERIFIED CONSISTENT` / 4 `VERIFIED WITH DOCUMENTED LIMITATION` / 4 `CONTRADICTION IDENTIFIED` / 0 `NOT YET VERIFIED`** |
| Contradiction register | **18 entries**, separate from the matrix |
| B-06 outside-authority items | **2** (C-06/C-07), separate |
| QA categories | **17** |
| Evidence dimensions | **7** (documentation, numerical validation, integration, runtime, migration, balance, playtesting) |
| B-04 active formulas | **47** |
| Worked examples | **20 published + A–H**, unchanged |

No economic value, formula identity, numerical status, classification, matrix row or owner-reserved decision changed in this assignment.


---

## E. Regression testing

| # | Command | Actual result | Exit |
|---:|---|---|---|
| 1 | `python qa_backups/14B_C1_validate_closeout.py` | **PASS 1,790/1,790** (49 categories, 50 decision references, 35 matrix rows, 17 crosswalk rows, 7 dimensions, 5 SR records, 17 CW records, 15 mutation rows) | 0 |
| 2 | `python qa_backups/14B_R1_R1_mutation_tests.py` | **15/15 mutations rejected and restored; 15/15 restores passed; 20/20 resolver controls** | 0 |
| 3 | `python qa_backups/14B_verify_b04_economy.py` | **PASS 321/321** | 0 |
| 4 | `python qa_backups/verify_economy_numbers.py` | **PASS 170/170** | 0 |
| 5 | `python qa_backups/14A_validate_numerical_foundation.py` | **64 checks, 0 failed** | 0 |
| 6 | `python qa_backups/14A_contract_validator.py` | **9/9 checks; 11 mappings, 11 NOT_REVIEWED** | 0 |
| 7 | `python qa_backups/test_14A_contract_validator.py` | **83 tests OK** | 0 |
| 8 | `python qa_backups/test_14A_trusted_amendment_security.py` | **46 tests OK** | 0 |
| 9 | `python qa_backups/test_14A_metadata_diff.py` | **8 tests OK** | 0 |
| 10 | `python qa_backups/validate_final.py` | **ALL CHECKS PASSED** | 0 |
| 11 | `python qa_backups/validate_links.py` | **final count recorded in §E.1 below** | 0 |
| 12 | `python qa_backups/09_validate.py` | **371/371** | 0 |
| 13 | `python qa_backups/test_decision_registers.py` | **12 tests OK** | 0 |
| 14 | `python qa_backups/test_next_action.py` | **27 tests OK** | 0 |
| 15 | `python qa_backups/10B_validate_warfare.py` | **1036 checks; 73/73 negative fixtures** | 0 |
| 16 | `python qa_backups/12A_validate_foundations.py` | **PASS** | 0 |
| 17 | `python qa_backups/13A_validate_ui_foundations.py` | **34/34** | 0 |
| 18 | `python qa_backups/13B_validate_ui_specifications.py` | **28/28** | 0 |
| 19 | `python qa_backups/13C_validate_interaction_specs.py` | **27/27** | 0 |
| 20 | `python qa_backups/13D_validate_integration.py` | **75/75** | 0 |
| 21 | `python qa_backups/11B_validate_b11.py` | **61/61; 52/52 gates; 0 unresolved links** | 0 |

**Inherited failures preserved (executed in this session):**

| Command | Result | Exit |
|---|---|---|
| `verify_politics_numbers.py` | **878/879** — stale progress-log guard | 1 (inherited) |
| `11A_validate_research.py` | **29/30** — frozen `REQ-703` maximum | 1 (inherited) |
| `09A_validate_alliance.py` | **941/943** — stale continuity guards | 1 (inherited) |
| `09B_validate_alliance_semantic.py` | **8 frozen D/DD-range problems** | 1 (inherited) |

**New regressions:** none found. **Tests not run:** no runtime, database, scheduler, market, UI, migration or playtest exists, so no runtime, migration, balance or playtesting test can be executed; the QA crosswalk records this explicitly. The 30-turn model remains deterministic reference arithmetic, not a simulation.

### E.1 Final documentation-link validation

Command: `python qa_backups/validate_links.py` (from `docs/`).

| Measure | Final value |
|---|---:|
| Exit code | **0** |
| Markdown files scanned | **150** |
| Links found | **4,618** |
| Links checked locally | **4,236** |
| External links skipped | **382** |
| Anchors checked | **34** |
| **Unresolved** | **0** |

The final execution above is the single source for the R1-R1 link count. The R1 report's 4,601 is a prior execution against a smaller set; it is not retained as the current total. The C1 report similarly points to the R1/R1-R1 records as historical counts.

---

## F. Git-state reconciliation

**Raw status command:** `git status --porcelain=v1 --untracked-files=all`.

| Measure | Final live value |
|---|---:|
| Branch | **`main`** |
| HEAD | **`bff91193f946ce77f60da9a838d5d76364552ed5`** |
| HEAD subject | `docs: add Stage 2 numerical contracts, semantic validation suite, and QA reports` |
| HEAD date | 2026-11-17 11:01:43 +0530 |
| Raw modified tracked paths | **25** |
| Untracked paths | **12** |
| Staged paths | **0** |
| Substantive modified tracked paths after CRLF/LF normalization | **25** |
| Line-ending-only modified tracked paths | **0** |

**Normalization method.** For every modified tracked path, the worktree bytes were compared with the corresponding `HEAD` blob after replacing `CRLF` (`\r\n`) with `LF` (`\n`) in both. If the normalized byte sequences were equal, the path was counted as line-ending-only; otherwise it was counted as substantive. No other whitespace normalization was applied. The comparison script is read-only and did not stage, commit, reset or modify any file.

**Complete substantive changed-path list (25):** `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/DECISIONS.md`, `docs/PROJECT_PROGRESS.md`, `docs/prompts/INDEX.md`, `docs/qa_backups/09_validate.py`, `docs/qa_backups/12A_validate_foundations.py`, `docs/qa_backups/13A_validate_ui_foundations.py`, `docs/qa_backups/13B_validate_ui_specifications.py`, `docs/qa_backups/14A_validate_numerical_foundation.py`, `docs/qa_backups/test_next_action.py`, `docs/qa_backups/validate_final.py`, `docs/qa_backups/verify_economy_numbers.py`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/04_approved_and_provisional_decisions.md`, `docs/stage-2/06_stage_2_progress_log.md`, `docs/stage-2/10_economic_formula_and_balance_register.md`, `docs/stage-2/10_economy_resources_treasury_and_finances.md`, `docs/stage-2/22_formula_master_inventory.md`, `docs/stage-2/22_formulas_and_balance.md`, `docs/stage-2/22_numerical_baseline_qa_report.md`, `docs/stage-2/22_numerical_contracts/evidence_mappings.json`, `docs/stage-2/22_numerical_contracts/index.json`, `docs/stage-2/22_numerical_parameter_inventory.md`.

**Comparison with the Project X (112) ZIP metadata.** The ZIP reported **157 raw modified tracked paths / 25 substantive / 132 line-ending-only**, with **9 untracked** and **0 staged**. The live checkout reports **25 raw modified / 25 substantive / 0 line-ending-only**, with **12 untracked** (the extra three are the R1-R1 mutation suite, report and archive) and **0 staged**. The difference is not concealed: the live raw count is 25, and the reproducible normalization finds zero EOL-only paths. The 157/132 observation is consistent with a different Git index/filter environment (or a snapshot whose line endings were normalized on checkout) and is recorded as an audit-environment observation, not as the live state. No file was converted, reverted or restaged to force a match.

**Owner commit.** The owner-reported Prompt 14B commit is **not verifiable** in this checkout: no commit after `bff9119` exists, and the 14B/C1/R1/R1 work is uncommitted. Recent history remains `bff9119` → `f1698d5` (2026-11-13) → `dd00ed8` → `07027fb` → `b186a0f`. No commit hash is fabricated, and no history was rewritten.

**No Git action.** No `git add`, `git commit`, `git push`, `git checkout`, `git reset`, `git clean`, `git stash`, `git rebase`, `git merge`, branch switch or history rewrite was performed. Everything remains unstaged for the owner.

---

## G. Final assessment

**`COMPLETE`**

Both original Project X (112) false-pass attacks were reproduced before correction (both returned exit 0) and are now rejected by the full production entry point (exit 1) with targeted diagnostics. The validator resolves 49 parameter records, 50 decision references, 25 ECN identifiers, 31 F-EC identifiers, 1 F-WR identifier, 44 section references, 5 validator filenames and the R1/R1-R1 local links; 0 references remain unresolved. Fifteen real end-to-end mutations execute against temporary copies of the real documents, all 15 are rejected for the intended reason, all 15 clean restores pass, and 20/20 resolver positive controls pass. The 49 parameter records, their Category C classifications and their `PROVISIONAL VALUE` statuses are unchanged; the 35-row matrix remains 27/4/4/0; the 18-entry contradiction register and the 2 B-06 items remain separate; the 17 QA categories and seven evidence dimensions remain accurate. The final link check shows **0 unresolved**. The Git state is reported raw and normalized, and the owner commit is recorded as unverified rather than fabricated. Prompt 14C–14K remain **NOT AUTHORIZED**.
