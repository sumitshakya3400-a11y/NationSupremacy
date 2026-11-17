# PROMPT 14A-C1 — PARAMETER INVENTORY VALIDATOR COMPLETENESS AND FINAL QA RECONCILIATION

> **Archive provenance:** Transcribed from the authorized Prompt 14A-C1 instruction supplied in the working session of 2026-11-13. This paragraph is the only addition; the instruction text below is preserved in full and is not summarized. No independent external copy exists in the repository, so byte-for-byte comparison against an outside original was not possible. The SHA-256 recorded in [INDEX.md](INDEX.md) identifies the stored bytes of this file.

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Master Game Design Bible  
**Parent phase:** Prompt 14 — Numbers, Formulas, Balance and Worked Examples  
**Original phase:** Prompt 14A — Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Correction:** 14A-C1  
**Execution type:** Targeted documentation and QA-validator correction only  
**Implementation authorization:** NONE  
**Next phase:** Prompt 14B — NOT STARTED / NOT AUTHORIZED  
**Authority:** D-014 — Autonomous Decision Policy

---

# 1. MISSION

Execute a narrowly scoped corrective pass against the actual current project repository.

The purpose is to correct the defects identified during the independent audit of:

`Project X (95).zip`

The independent audit confirmed that Prompt 14A's principal deliverables are present and that its initial formula inventory is complete.

However, four outstanding issues prevent full acceptance:

1. The Prompt 14A numerical parameter validator does not adequately validate all 393 parameter records against their authoritative sources.
2. The current numerical QA and progress records contain stale documentation-link totals.
3. Acceptance gate P14A-06 reports approximately 380 parameter records instead of the verified 393 records.
4. The numerical QA report contains an inaccurate statement about the politics validator's process exit code and an unsupported generic statement about validator exit-code behaviour.

Correct these four issues without restarting Prompt 14A.

**The objective is to make the parameter inventory independently verifiable and reconcile the final QA evidence.**

Do not redesign the numerical architecture.

Do not recalibrate any game values.

Do not change any of the 295 original formula definitions.

Do not start Prompt 14B.

---

# 2. MANDATORY GOVERNANCE

Before starting:

1. Read the complete `docs/AUTONOMOUS_DECISION_POLICY.md`.
2. Follow D-014 and all applicable owner-reserved boundaries.
3. Read the complete Prompt 14A archived instruction.
4. Read the actual Prompt 14A implementation and current validator.
5. Read the independent audit findings from the owner.
6. Inspect the current Git working-tree status without modifying it.

The original Prompt 14A instructions remain binding except where this correction explicitly narrows the task.

## 2.1 Protected restrictions

You MUST NOT:

- Modify `docs/AUTONOMOUS_DECISION_POLICY.md`.
- Change any owner-approved decision.
- Resolve an owner-reserved UD.
- Change the 295 original formula definitions.
- Change any initial resource, treasury, production, research, trade, diplomacy, Alliance, warfare or progression value.
- Change the approved D-015 Operations Points model.
- Change D-019 ordering.
- Change the two-hour UTC turn cadence.
- Change P0–P7.
- Modify frontend or backend implementation.
- Modify gameplay prototypes.
- Modify databases, SQL, API, migrations or security implementation.
- Perform Git operations.
- Stage, commit, push, reset, revert or discard files.
- Claim the Git working tree is clean without evidence.

The original B-04 through B-12 formula registers must remain unchanged.

The existing B-14 architecture and inventory structure must be preserved.

Do not reopen accepted Prompt 13A, 13B, 13C or 13D.

Prompt 14B–14K remain unauthorized.

---

# 3. BASELINE TO PRESERVE

Project X (95) established the following baseline.

## 3.1 Formula inventory

| System | Active formulas |
|---|---:|
| B-04 | 47 |
| B-05 | 41 |
| B-06 | 44 |
| B-07 | 39 |
| B-08 | 12 |
| B-09 | 8 |
| B-10 | 39 |
| B-11 | 49 |
| B-12 | 16 |
| **Total** | **295** |

These 295 active formula identifiers were independently verified.

One retired formula, `F-WEP-048`, is separately recorded.

Do not change these counts without new source evidence.

## 3.2 Parameter inventory

The current canonical inventory contains 393 parameter records.

| Inventory section | Records |
|---|---:|
| B-02 | 7 |
| B-03 | 20 |
| B-04 | 49 |
| B-05 | 73 |
| B-06 | 96 |
| B-07 | 26 |
| B-08 | 12 |
| B-09 | 8 |
| B-10 | 39 |
| B-11 | 49 |
| B-12 | 14 |
| **Total** | **393** |

The 393 figure is the number of parameter inventory records, not necessarily the number of individual scalar values. Some records represent vectors or grouped numerical values.

Preserve this distinction.

## 3.3 Canonical B-14 files

The following files already exist:

- `docs/stage-2/22_formulas_and_balance.md`
- `docs/stage-2/22_formula_master_inventory.md`
- `docs/stage-2/22_numerical_parameter_inventory.md`
- `docs/stage-2/22_numerical_baseline_qa_report.md`

Do not replace or recreate them unnecessarily.

The canonical B-14 filename remains:

`22_formulas_and_balance.md`

D-198 remains authoritative.

## 3.4 Existing Prompt 14A validator

Existing validator:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Existing self-test result:

- Validator: 28/28.
- Self-tests: 20/20.

These passing totals are not sufficient by themselves because independent mutation testing identified parameter-inventory coverage gaps.

Do not remove or weaken any of the existing 28 checks or 20 regression tests.

---

# 4. CORRECTION 1 — COMPLETE PARAMETER INVENTORY VALIDATOR

**Highest-priority task.**

The existing Prompt 14A validator currently passes even when important changes are made to parameter records.

The independent audit reproduced these failures:

| Mutation tested | Required behaviour | Existing result |
|---|---|---|
| Remove B-10 `F-WR-001` parameter record | FAIL | Incorrectly PASS |
| Change B-10 `F-WR-003` decision owner | FAIL | Incorrectly PASS |
| Change B-10 `F-WR-003` from PROVISIONAL VALUE to OWNER-APPROVED VALUE | FAIL | Incorrectly PASS |
| Change B-04 starting treasury from 1,500 to 1,501 in the parameter map | FAIL | Incorrectly PASS |

These defects must be corrected.

## 4.1 Required validator enhancement

Extend:

`docs/qa_backups/14A_validate_numerical_foundation.py`

The validator must independently inspect the actual parameter inventory and reconcile it against its authoritative source documents.

It must not validate the inventory merely by checking that:

- A section exists.
- A parameter identifier is present in a text file.
- A total row count matches.
- A few representative records exist.
- The same copied values appear in two documents.

The validator must check each parameter record individually.

## 4.2 Complete source coverage

Verify parameter records across every applicable system:

- B-02.
- B-03.
- B-04.
- B-05.
- B-06.
- B-07.
- B-08.
- B-09.
- B-10.
- B-11.
- B-12.

No system may receive weaker validation simply because its inventory format differs.

Where source structures differ, implement appropriate source-specific extraction or validation adapters.

Do not silently skip difficult registers.

## 4.3 Validate each parameter record

For every one of the 393 records, validate all applicable fields:

| Field | Validation requirement |
|---|---|
| Parameter identifier/name | Must resolve to the canonical source |
| Owning system | Must match the source |
| Source document | Must exist |
| Source section | Must resolve |
| Current numerical value | Must agree with the authoritative source |
| Units | Must agree with source |
| Precision | Must agree with source or have an explicit missing-data marker |
| Rounding | Must agree with source or have an explicit missing-data marker |
| Timing | Must agree with source or have an explicit missing-data marker |
| Formula dependencies | Must reference valid formula identifiers |
| Decision authority | Must match the applicable source decision |
| Numerical status | Must be supported by the appropriate evidence |
| Owner-reserved status | Must preserve the actual decision-register position |
| Evidence requirement | Must not be falsely reported as satisfied |
| Playtesting requirement | Must remain visible where applicable |

Do not invent missing source metadata.

A genuine source omission must be explicitly recorded as a gap.

A missing source field must never silently become a passing value.

## 4.4 Source-to-inventory reconciliation

The validator must independently establish:

1. Which parameter records are expected from the authoritative sources.
2. Which records appear in the B-14 inventory.
3. Which records are missing.
4. Which records are duplicated.
5. Which values differ.
6. Which units differ.
7. Which rounding rules differ.
8. Which parameter authorities differ.
9. Which numerical classifications differ.
10. Which records contain unresolved dependencies.

Use stable source references and existing parameter identifiers.

Where no stable identifier exists, use a deterministic source key based on the canonical source, parameter name and scope. Do not invent a competing global parameter-ID namespace.

## 4.5 Source authority must be independently checked

For numerical values, use the appropriate canonical formula register or specification.

For owner authority, inspect:

- B-03 §21.2 and §21.3 where relevant.
- `docs/DECISIONS.md`.
- Applicable DD and UD registers.
- Applicable canonical system specifications.
- Existing owner authorization evidence.

Do not assume that a parameter's presence in B-14 grants Prompt 14 ownership of its decision.

Do not assume that the same team owns the specification, numerical approval, implementation and validator.

## 4.6 Four-status validation

The validator must enforce the four established numerical labels:

- `OWNER-APPROVED VALUE`
- `PROVISIONAL VALUE`
- `DESIGN PROPOSAL`
- `NEEDS PLAYTESTING`

Check the status against its actual supporting evidence.

Examples:

- A value without an owner-approval decision cannot be classified as owner-approved.
- A provisional value cannot be silently promoted because an arithmetic validator passes.
- A design proposal cannot be represented as an adopted formula.
- A playtesting-dependent value cannot be confirmed solely by documentation checks.

Keep `UNSPECIFIED` as an absence marker, not a fifth numerical status.

Do not weaken the four-status rules.

## 4.7 Special validation for B-03

Retain complete validation of all 20 B-03 §21.2 carry-in parameters.

For every parameter, verify:

- Source value.
- Source identity.
- Numerical owner.
- Validator owner.
- Current status.
- Evidence requirement.
- Relevant UD disposition.
- Playtesting or external measurement dependency.

Any change to a B-03 source value or owner in the inventory must be rejected unless the actual canonical source has a corresponding authorized change.

Do not modify B-03 during this correction.

## 4.8 Validator behaviour

The enhanced validator must return a non-zero process exit code when it identifies a material integrity failure.

Its output must identify:

- Exact parameter.
- Expected value or state.
- Actual value or state.
- Source document.
- Affected inventory location.
- Failure category.

Do not use a generic FAIL message without identifying the affected record.

---

# 5. CORRECTION 2 — PARAMETER REGRESSION AND MUTATION TESTS

Expand the Prompt 14A regression tests.

Preserve every existing positive and negative test.

Add explicit regression tests for the four independently reproduced failures.

## 5.1 Mandatory regression matrix

| Test | Expected result |
|---|---|
| Remove B-10 `F-WR-001` parameter record | REJECT |
| Change B-10 `F-WR-003` owner | REJECT |
| Promote B-10 `F-WR-003` without approval evidence | REJECT |
| Change B-04 starting treasury 1,500 to 1,501 | REJECT |
| Change a parameter unit | REJECT |
| Change a parameter rounding rule | REJECT |
| Remove a parameter source reference | REJECT |
| Duplicate a parameter record | REJECT |
| Remove a B-08 parameter record | REJECT |
| Remove a B-09 parameter record | REJECT |
| Remove a B-11 parameter record | REJECT |
| Change an owner-reserved UD classification | REJECT |
| Mark a playtesting-dependent parameter owner-approved | REJECT |
| Preserve a correctly documented provisional parameter | ACCEPT |
| Preserve a properly sourced owner-approved parameter | ACCEPT |
| Preserve an explicit missing-data marker | ACCEPT only where the canonical source genuinely omits that field |

All mutation tests must operate on temporary test fixtures.

Never deliberately corrupt the actual canonical formula registers or authoritative parameter inventory to run a negative test.

## 5.2 Independent testing requirement

Tests must demonstrate that the validator actually detects the mutated conditions.

Do not write tests that merely call helper functions using hardcoded expected PASS or FAIL outcomes.

Use temporary copies or structured fixtures representing the actual inventory.

Test both successful and unsuccessful paths.

## 5.3 Avoid self-validating logic

The expected data must originate from authoritative source files or independently controlled source fixtures.

Do not generate the expected values by reading the B-14 inventory itself and then compare that inventory to itself.

Avoid sharing the same faulty parsing logic between inventory generation and expected-value extraction.

Where source-specific parsing is necessary, document its assumptions and test them.

## 5.4 Preserve test history

Report:

- Previous validator checks.
- New validator checks.
- Previous self-tests.
- New self-tests.
- Total actual tests executed.
- New mutation cases.
- All pass/fail results.

Do not claim that a larger test count automatically means greater coverage.

Explain what the new tests protect against.

---

# 6. CORRECTION 3 — RECONCILE THE PARAMETER COUNT

The canonical B-14 §5 identifies:

**393 parameter inventory records.**

However, acceptance gate P14A-06 still uses approximately 380.

Correct the current gate wording.

The authoritative figure should be:

**393 parameter inventory records, comprising 7 B-02 records, 20 B-03 records, and the remaining 366 records across B-04 through B-12.**

Retain the qualification:

Some inventory records represent vectors or grouped numerical values; 393 is the number of inventory records, not necessarily the number of individual scalar values.

Update every current Prompt 14A statement that incorrectly says:

- Approximately 380.
- Approximately 390, if used as an exact acceptance measure.
- Any other inconsistent current parameter count.

Inspect:

- `docs/stage-2/22_formulas_and_balance.md`
- `docs/stage-2/22_numerical_parameter_inventory.md`
- `docs/stage-2/22_numerical_baseline_qa_report.md`
- Prompt 14A acceptance-gate records.
- Prompt 14A progress records.
- Relevant handoff and continuity summaries.

Update only current authoritative claims.

Preserve historical counts when they are correctly labelled as historical estimates or earlier states.

Do not change the underlying 393 parameter records during this count reconciliation.

---

# 7. CORRECTION 4 — DOCUMENTATION-LINK QA RECONCILIATION

The independent Project X (95) audit reproduced the following current documentation-link baseline:

| Measure | Previous actual result |
|---|---:|
| Markdown files scanned | 122 |
| Total links checked | 4,321 |
| Local links | 3,939 |
| External links skipped | 382 |
| Anchors checked | 34 |
| Unresolved links | 0 |

However, the current Prompt 14A progress record still contains the older Prompt 13D figures:

- 4,225 total links.
- 3,843 local links.

The numerical QA report also states 117 Markdown files scanned instead of 122.

## 7.1 Required correction

Locate the current inaccurate Prompt 14A claims in:

- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/stage-2/22_numerical_baseline_qa_report.md`
- Any corresponding current B-14 handoff or QA summary.

Correct them using the actual final command output.

The previous reproduced baseline is:

- 122 Markdown files.
- 4,321 links checked.
- 3,939 local links.
- 382 external links skipped.
- 34 anchors.
- 0 unresolved.

**Important:** Re-run the documentation-link validator after completing C1.

Because Prompt 14A-C1 itself and its archive may introduce additional Markdown files or links, the final current totals may legitimately differ from the previous baseline.

Therefore:

1. Record the previous baseline.
2. Execute the current documentation-link validator.
3. Record its exact final output.
4. Update all current claims with those final actual values.
5. Preserve the older 4,225/3,843 figures in historical Prompt 13D records.
6. Do not alter historical evidence to make all project snapshots display the same link totals.

Zero unresolved links must remain independently verified.

---

# 8. CORRECTION 5 — POLITICS VALIDATOR EXIT-CODE EVIDENCE

The Prompt 14A numerical QA report states that:

`verify_politics_numbers.py`

prints one failed check but exits with code 0.

The independent audit executed the script and found:

- 878/879 checks passed.
- One failed check.
- Actual process exit code: 1.

Correct the numerical QA report.

## 8.1 Required investigation

Inspect the actual:

`verify_politics_numbers.py`

and any relevant wrapper scripts.

Verify:

- The explicit process-exit behaviour.
- The actual command used.
- The actual process return code.
- The exact failure.
- Whether the failure is inherited or introduced.

Record the evidence accurately.

Do not modify the politics validator merely to make Prompt 14A's report appear clean.

The one inherited failed check remains visible unless separately corrected through its authorized process.

## 8.2 Generic exit-code claim

The existing QA report also makes a generic statement suggesting that several validators print FAIL while returning exit code 0.

Do not preserve a generic statement without specific evidence.

Either:

- Provide the exact validator, command, output and exit code for each verified exception; or
- Remove the unsupported generalization.

Do not claim that a validator has failed solely because an old log contains an earlier failure message.

Use current execution evidence.

---

# 9. REQUIRED DOCUMENTATION UPDATES

Only update the files genuinely affected.

At minimum inspect:

1. `docs/qa_backups/14A_validate_numerical_foundation.py`
2. Its existing Prompt 14A self-test or regression test file.
3. `docs/stage-2/22_numerical_baseline_qa_report.md`
4. `docs/stage-2/22_numerical_parameter_inventory.md`
5. `docs/stage-2/22_formulas_and_balance.md`
6. `docs/stage-2/06_stage_2_progress_log.md`
7. Relevant Prompt 14A acceptance-gate records.
8. Relevant `AI_CONTEXT.md` and `AI_HANDOFF.md` entries, only where current claims need synchronization.

Do not rewrite the entire canonical documents.

Use narrowly scoped edits.

Preserve all formula identifiers, parameter records, decisions and historical sections.

## 9.1 Permanent correction prompt archive

Save this entire Prompt 14A-C1 instruction verbatim as:

`docs/prompts/prompt_14A-C1_parameter_inventory_validator_completeness_and_final_qa_reconciliation.md`

Requirements:

- Preserve all sections.
- Do not summarize.
- Do not remove acceptance requirements.
- Retain the original correction scope.
- Calculate byte count and SHA-256.
- Verify the archived file against the supplied instruction.
- Update `docs/prompts/INDEX.md` using the existing convention.
- Never overwrite the original Prompt 14A archive.

---

# 10. ACCEPTANCE GATES

Create or update a focused Prompt 14A-C1 acceptance-gate record.

| Gate | Acceptance objective |
|---|---|
| C1-01 | Complete governance and policy review |
| C1-02 | All 393 parameter inventory records are reconciled |
| C1-03 | B-02 through B-12 parameter coverage is validated |
| C1-04 | Source values are verified |
| C1-05 | Units, precision, rounding and timing metadata are validated |
| C1-06 | Parameter ownership and decision authority are verified |
| C1-07 | Four numerical status safeguards are enforced |
| C1-08 | All 20 B-03 carry-in safeguards remain intact |
| C1-09 | Four original negative mutation cases are rejected |
| C1-10 | Additional cross-system negative fixtures pass |
| C1-11 | Existing Prompt 14A tests remain intact and pass |
| C1-12 | P14A-06 accurately records 393 parameter records |
| C1-13 | Documentation-link totals are rerun and reconciled |
| C1-14 | Politics-validator process exit evidence is corrected |
| C1-15 | Other QA assertions are supported by actual execution |
| C1-16 | Prompt archive and index are verified |
| C1-17 | Historical records and owner-reserved decisions are preserved |
| C1-18 | No formula or game-balance changes occur |
| C1-19 | Final project and documentation QA complete |
| C1-20 | Final correction report and handoff produced |

Use the statuses:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

A gate may pass only when its required evidence actually supports the claim.

Do not turn an incomplete test into PASS by relabelling it.

---

# 11. FINAL VALIDATION

After making the corrections:

1. Run the strengthened numerical foundation validator.
2. Run all previous Prompt 14A self-tests.
3. Run all new parameter mutation tests.
4. Verify all 393 parameter inventory records.
5. Verify all 295 formula identifiers remain unchanged.
6. Recheck all 20 B-03 carry-in parameters.
7. Rerun the relevant economy, city, politics, market, diplomacy, Alliance, warfare, progression and fair-play validators.
8. Reproduce the politics-validator exit code.
9. Rerun the documentation-link validator.
10. Rerun the final project validator.
11. Rerun decision-register tests.
12. Rerun next-action tests.
13. Verify the archived Prompt 14A-C1 text.
14. Verify all new internal document links.
15. Compare the original formula registers against the starting snapshot.
16. Inspect actual modified files and Git status.
17. Verify the Autonomous Decision Policy remains unchanged.
18. Verify no prototype or implementation files were modified.
19. Confirm no subsequent Prompt 14 phase was started.

Report inherited validator failures separately.

Do not reopen accepted Prompt 13 work for unrelated historical validator problems.

Do not claim that actual gameplay balance has been established.

---

# 12. OUT-OF-SCOPE RESTRICTIONS

This correction does not authorize:

- Rewriting the 295 formulas.
- Modifying the 393 existing parameter records to make validation easier.
- Adjusting starting treasury or initial resources.
- Changing costs, prices, production, research, tax or maintenance.
- Changing warfare or Operations Points values.
- Changing diplomacy or Alliance permissions.
- Changing progression rewards.
- Changing fair-play parameters.
- Resolving owner-reserved UDs.
- Changing D-015 or D-019.
- Altering the two-hour UTC cadence.
- Creating game mechanics.
- Building a gameplay simulation.
- Modifying frontend/backend/database/API/SQL/security/deployment code.
- Modifying the Autonomous Decision Policy.
- Performing Git operations.
- Starting Prompt 14B.

Only the parameter-validator completeness and final QA reconciliation defects identified in this correction are authorized.

---

# 13. FINAL HANDOFF

Produce a correction report containing:

1. Initial Project X (95) baseline.
2. Every identified defect.
3. Exact files changed.
4. All 393 parameter records' validation outcome.
5. Source validation coverage for B-02 through B-12.
6. Original mutation tests and their corrected results.
7. New regression-test totals.
8. Updated documentation-link totals.
9. Correct politics-validator exit-code evidence.
10. Final P14A-C1 acceptance-gate table.
11. Inherited QA failures.
12. Confirmation that the 295 formula definitions were unchanged.
13. Confirmation that owner-reserved decisions were preserved.
14. Confirmation that no implementation work occurred.
15. Confirmation that no Git operations occurred.
16. SHA-256 and byte count of the archived correction prompt.
17. Remaining limitations.
18. The single next action.

The completion recommendation must be one of:

- COMPLETE.
- PARTIAL.
- NOT COMPLETE.

Do not claim COMPLETE if any required parameter validation remains unverified.

---

# 14. FINAL SUCCESS CONDITION

Prompt 14A-C1 is complete only when:

- All 393 parameter inventory records are individually reconciled against appropriate authoritative sources.
- Parameter values, authorities and numerical statuses cannot be silently changed without the validator detecting the discrepancy.
- All four original mutation failures are correctly rejected.
- New positive and negative regression tests pass.
- The parameter count is accurately recorded as 393 inventory records.
- Current documentation-link totals match the actual final execution output.
- Historical Prompt 13D link totals remain intact.
- The politics-validator exit-code statement is accurate.
- Unsupported QA claims have been removed or supported with evidence.
- The original 295 formula definitions remain unchanged.
- All owner-reserved decisions remain intact.
- Existing Prompt 14A work is preserved.
- All correction acceptance gates are supported by actual evidence.
- The correction prompt is archived and verified.
- No implementation or Git operations occurred.
- No further Prompt 14 subphase was executed.

**FINAL NEXT ACTION:**

If all C1 requirements pass:

**PROMPT 14A COMPLETE — AWAIT OWNER REVIEW AND EXPLICIT AUTHORIZATION OF PROMPT 14B.**

Otherwise:

**PROMPT 14A-C1 REMAINS OPEN — REPORT THE EXACT UNRESOLVED GATES.**

**END OF PROMPT 14A-C1**
