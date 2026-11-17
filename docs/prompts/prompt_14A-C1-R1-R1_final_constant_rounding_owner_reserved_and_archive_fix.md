# PROMPT 14A-C1-R1-R1 — FINAL CONSTANT PRECISION/ROUNDING VALIDATION, OWNER-RESERVED FIELD ENFORCEMENT AND VERBATIM ARCHIVE RECONCILIATION

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Master Game Design Bible  
**Parent phase:** Prompt 14 — Numbers, Formulas, Balance and Worked Examples  
**Original phase:** Prompt 14A — Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Correction chain:** Prompt 14A → Prompt 14A-C1 → Prompt 14A-C1-R1 → Prompt 14A-C1-R1-R1  
**Execution type:** Final targeted documentation-validator, regression-test and prompt-archive correction  
**Implementation authorization:** NONE  
**Baseline:** Project X (97)  
**Next phase:** Prompt 14B — NOT STARTED / NOT AUTHORIZED  
**Authority:** D-014 — Autonomous Decision Policy

---

# 1. MISSION

Execute the final narrowly scoped correction to the Prompt 14A numerical foundation validator.

Project X (97) has successfully corrected the nine previously identified mutation weaknesses.

The independent audit nevertheless identified two additional defects:

1. B-04 Treasury precision/rounding metadata can be changed to an invalid value without the validator detecting the modification.
2. The B-04 Treasury owner-reserved field can be changed without the validator detecting the modification.

There is also one remaining prompt-archive reconciliation issue:

3. The archived Prompt 14A-C1-R1 document contains additional provenance text despite the original instruction requiring verbatim archival.

This correction must resolve all three findings.

**The objective is to finish Prompt 14A's numerical metadata validation and close its remaining archival integrity issue.**

Do not restart Prompt 14A.

Do not repeat the entire C1 or C1-R1 implementation.

Do not rewrite the 393 parameter records.

Do not recalibrate any game values.

Do not start Prompt 14B.

This is intended to be the final corrective pass before independent Prompt 14A acceptance.

---

# 2. MANDATORY GOVERNANCE

Before any modifications:

1. Read the complete `docs/AUTONOMOUS_DECISION_POLICY.md`.
2. Follow D-014 and all owner-reserved decision boundaries.
3. Read the complete Prompt 14A archive.
4. Read the complete Prompt 14A-C1 archive.
5. Read the complete Prompt 14A-C1-R1 archive.
6. Read the current B-14 canonical document.
7. Read the complete numerical parameter inventory.
8. Inspect the existing Prompt 14A validator and all its self-tests.
9. Inspect the source documents governing B-04 numerical precision, rounding and parameter ownership.
10. Inspect the actual decision registers and relevant owner-reserved UDs.

Use the actual repository, not the coding agent's previous report.

## 2.1 Protected restrictions

You MUST NOT:

- Modify the Autonomous Decision Policy.
- Change D-015 or D-019.
- Change the two-hour UTC cadence.
- Change P0–P7.
- Change any of the 295 original formula definitions.
- Change any of the 393 parameter values to make validation pass.
- Change the B-04 starting treasury value.
- Change costs, prices, production rates, research costs, taxation, market fees or military values.
- Change owner-approved decisions.
- Resolve owner-reserved UDs.
- Invent owner approval.
- Modify frontend or backend implementation.
- Modify gameplay prototypes.
- Modify databases, SQL, API, migrations or security implementation.
- Perform Git operations.
- Stage, commit, push, reset, revert or discard changes.
- Start Prompt 14B or any subsequent Prompt 14 subphase.

The existing Project X (97) work must be preserved.

---

# 3. VERIFIED BASELINE

The following figures must remain consistent unless a genuine source discrepancy is independently demonstrated.

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

The retired formula `F-WEP-048` remains excluded.

## 3.2 Parameter inventory

| System | Records |
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

These are inventory records, not necessarily individual scalar values.

Preserve all 393 records and their existing organization.

## 3.3 Current validator baseline

File:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Project X (97) baseline:

- Validator: 41/41 PASS.
- Self-tests: 48/48 PASS.
- Nine original R1 mutation cases: REJECTED.

Preserve these existing checks and tests.

Add the final missing safeguards.

---

# 4. CORRECTION A — B-04 PRECISION AND ROUNDING SOURCE VALIDATION

**Priority: CRITICAL**

The independent audit reproduced this defect:

| Test | Expected | Project X (97) result |
|---|---|---|
| Change B-04 Treasury precision/rounding metadata to `round to nearest banana` | REJECT | Incorrectly PASS |

The validator checks the presence of metadata but does not adequately establish that the precision/rounding content agrees with the authoritative source.

## 4.1 Inspect authoritative sources

Inspect the complete relevant B-04 sections, particularly:

`docs/stage-2/10_economic_formula_and_balance_register.md`

Also inspect:

- The B-04 parameter table in the canonical B-14 inventory.
- The relevant formula definitions.
- Existing B-04 numerical conventions.
- Any register-level precision and rounding rules.
- Any applicable decision records.

Determine exactly which precision and rounding rules are applicable to the starting Treasury parameter.

Do not guess.

Do not copy an invented convention into the source document.

## 4.2 Required validator behaviour

Extend the existing validator so that B-04 through B-07 constant-table parameter records have source-backed precision and rounding validation.

The validation must distinguish:

1. A precision rule explicitly specified for an individual parameter.
2. A rounding rule explicitly specified for an individual parameter.
3. A register-level convention applicable to the parameter.
4. A documented statement that the field is not specified.
5. An unresolved or ambiguous source definition.
6. An extraction or parsing failure.

Do not treat these situations as equivalent.

Where the source defines a register-level convention, the validator may apply it to the relevant parameter only when the source actually establishes that applicability.

Where the source does not specify a rule, retain an explicit missing-data marker.

An extraction failure must never be converted into an accepted missing-data marker.

## 4.3 Parameter-specific and register-level rules

The validation must not require every parameter to have an invented individual rounding rule.

Instead:

- Identify the exact governing source rule.
- Record whether the rule is individual or register-level.
- Verify its applicability.
- Compare the inventory against that rule.
- Reject unsupported modifications.

Do not create conflicting conventions between B-04, B-05, B-06 and B-07.

Do not force identical rounding across systems if the authoritative sources specify different treatment.

## 4.4 Exact mutation regression

Add this mandatory test:

**Test:** Change the B-04 Treasury parameter's documented precision/rounding metadata to `round to nearest banana`.

Expected:

- The validator detects the modification.
- It identifies the exact parameter.
- It identifies the incorrect field.
- It reports the expected source convention.
- It reports the altered inventory value.
- It returns a non-zero process exit code.

The test must use a temporary inventory fixture.

Do not modify the actual canonical Treasury record.

## 4.5 Additional precision and rounding tests

Add positive and negative tests.

| Test | Expected |
|---|---|
| Correct B-04 Treasury precision/rounding | PASS |
| Invalid B-04 Treasury rounding | REJECT |
| Change a source-defined B-04 rounding rule | REJECT |
| Change a source-defined B-05 precision rule | REJECT |
| Change a source-defined B-06 rounding rule | REJECT |
| Change a source-defined B-07 precision rule | REJECT |
| Preserve a legitimate missing-data marker | PASS |
| Remove a required precision/rounding marker | REJECT |
| Introduce an unparseable source rule | BLOCKED/FAIL, never PASS |

Do not add tests based on fabricated source conventions.

---

# 5. CORRECTION B — OWNER-RESERVED FIELD SOURCE ENFORCEMENT

**Priority: CRITICAL**

The independent audit reproduced this defect:

| Test | Expected | Project X (97) result |
|---|---|---|
| Change B-04 Treasury owner-reserved field to YES | REJECT | Incorrectly PASS |

The validator does not adequately protect this field for constant-table records.

## 5.1 Complete source-of-authority investigation

Inspect:

- B-02 and B-03 specifications.
- All nine formula registers.
- B-14 numerical parameter inventory.
- Global decision register.
- DD register.
- UD register.
- Applicable owner-authorization evidence.

Determine the correct owner-reserved classification for every relevant parameter record.

Do not presume that a parameter is owner-reserved solely because it is provisional.

Do not presume that a parameter is not owner-reserved solely because it belongs to a normal gameplay system.

An unresolved value and an owner-reserved decision are different classifications.

## 5.2 Complete inventory coverage

Validate the existing owner-reserved field across all applicable 393 records.

The validator must detect:

- A false YES classification.
- A false NO classification.
- Removal of an actual owner-reserved restriction.
- Addition of an unsupported owner-reserved restriction.
- A mismatch with an applicable UD.
- A mismatch with an explicit owner decision.
- An unverified owner-reserved classification.

For each record, identify:

1. Parameter identity.
2. Current inventory flag.
3. Expected source-backed flag.
4. Applicable decision or UD.
5. Source path and section.
6. Whether the field is explicitly specified.
7. Whether its classification is independently verified.

Use an explicit marker when the source does not establish the classification.

Do not silently assume NO when the source is ambiguous.

An inability to determine authority must remain visible.

## 5.3 Protect all owner-reserved boundaries

Preserve all applicable owner-reserved decisions, including the existing Alliance and fair-play restrictions.

In particular, retain the existing actual statuses and restrictions for:

- UD-017.
- UD-040 through UD-060, where applicable.
- All other owner-reserved decisions discovered in the real registers.

This list is a minimum inspection checklist, not permission to ignore other owner-reserved decisions.

Do not resolve any UD.

Do not change any Category A decision.

## 5.4 Exact mutation regression

Add the independently reproduced test:

**Test:** Change the B-04 Treasury parameter's owner-reserved field to `Yes — owner-reserved` when its authoritative source classification is not owner-reserved.

Expected:

- Validator rejects the mutation.
- Exact parameter and field are reported.
- Expected source classification is reported.
- Applicable source reference is reported.
- Validator exits non-zero.

Run the test against a temporary fixture.

Do not modify the canonical Treasury record.

## 5.5 Additional owner-reserved tests

| Test | Expected |
|---|---|
| Correct B-04 Treasury classification | PASS |
| Change B-04 Treasury to owner-reserved without authority | REJECT |
| Change a genuinely owner-reserved parameter to NO | REJECT |
| Change a non-owner-reserved parameter to YES | REJECT |
| Remove an applicable UD reference | REJECT |
| Replace an applicable UD with an unrelated D reference | REJECT |
| Preserve a genuinely unresolved but non-owner-reserved parameter | PASS |
| Preserve a genuinely owner-reserved parameter | PASS |
| Source authority cannot be established | BLOCKED, never silently PASS |

The positive tests must demonstrate that legitimate owner-reserved records continue to work.

Do not solve false positives by marking every record owner-reserved.

---

# 6. VALIDATOR ARCHITECTURE

Strengthen the existing:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Do not replace it with an unrelated validator.

Preserve:

- All 41 existing validator checks.
- All 48 existing self-tests.
- All nine R1 mutations.
- All source adapters.
- Existing coverage reporting.
- Existing diagnostic structure.

## 6.1 Source-first validation

Expected values must come from authoritative source files or independent, source-controlled fixtures.

Do not compare the parameter inventory against values copied from the same inventory.

Do not make a B-14 record validate itself.

Do not create a hardcoded expected value that is unsupported by the governing specification.

Where a source-specific convention is required, document its provenance and applicability.

## 6.2 No circular validation

The validator must not treat:

- A D-number as automatic approval evidence.
- A formula ID as owner authority.
- A provisional parameter as an owner-reserved decision.
- A missing field as an affirmative NO.
- A validator passing as evidence of owner approval.

Every classification must be justified independently.

## 6.3 Fail-closed behaviour

When source metadata is unavailable, ambiguous or unparseable:

1. Identify the record.
2. Identify the field.
3. Identify the source.
4. Explain why the metadata cannot be confirmed.
5. Mark the applicable validation result PARTIAL, BLOCKED or FAIL.
6. Return a non-zero process exit code where the unverified field is a required acceptance condition.

Never silently skip the record.

Never convert an extraction failure into a passing missing-data marker.

---

# 7. FINAL REGRESSION TEST SUITE

Preserve all existing tests.

Add the exact two newly discovered mutations.

Add sufficient positive and negative controls for both protections.

The final test suite must demonstrate:

### Precision/rounding

- Valid conventions pass.
- Invalid conventions fail.
- Source changes are detected.
- Missing-data cases remain distinguishable.
- Parser failures do not pass.

### Owner-reserved metadata

- Legitimate owner-reserved records pass.
- Legitimate non-owner-reserved records pass.
- Unsupported YES mutations fail.
- Unsupported NO mutations fail.
- Unrelated decision references do not establish ownership.
- Ambiguous authority does not pass silently.

All tests must use temporary fixtures.

Do not corrupt actual project files.

Do not simply assert that an error occurred; verify that the intended field and parameter triggered it.

## 7.1 Test report

Report:

- Existing checks retained.
- New validator checks.
- Existing self-tests retained.
- New self-tests.
- Number of precision/rounding tests.
- Number of owner-reserved tests.
- Positive test count.
- Negative test count.
- Total test count.
- Exact commands.
- Actual process exit codes.

The test report must explain the protection established by each test group.

---

# 8. PROMPT ARCHIVE RECONCILIATION

The Project X (97) audit identified an archival discrepancy.

The C1-R1 archive was required to preserve the exact supplied instruction but contains additional provenance text.

Inspect:

`docs/prompts/prompt_14A-C1-R1_complete_parameter_metadata_source_validation_and_false_approval_regression_hardening.md`

Compare the archived content with the exact original Prompt 14A-C1-R1 instruction supplied to the coding agent.

## 8.1 Required outcome

The archive must contain the exact original instruction and no additional unrequested narrative.

Preserve:

- All original headings.
- All acceptance requirements.
- All tables.
- All restrictions.
- All regression instructions.
- All final completion conditions.

Remove only material demonstrably outside the original supplied prompt.

Do not rewrite or shorten the original instructions.

Do not fabricate an original source copy if it is unavailable.

If the exact original cannot be recovered or verified, report that limitation rather than claiming byte-for-byte identity.

## 8.2 Hash reconciliation

After the archival correction:

1. Calculate the final byte count.
2. Calculate SHA-256.
3. Update `docs/prompts/INDEX.md`.
4. Verify the index matches the exact archived file.
5. Preserve the original Prompt 14A and C1 archives.
6. Do not overwrite unrelated archived prompts.

## 8.3 Archive this final correction prompt

Save this complete instruction verbatim at:

`docs/prompts/prompt_14A-C1-R1-R1_final_constant_rounding_owner_reserved_and_archive_fix.md`

Update:

`docs/prompts/INDEX.md`

Record:

- Prompt ID.
- Full title.
- Archive path.
- Archive date.
- Exact byte count.
- SHA-256.

Verify that the archived file matches this complete instruction.

Do not append unrequested provenance paragraphs.

---

# 9. DOCUMENTATION UPDATES

Update only the genuinely affected files.

At minimum inspect:

1. `docs/qa_backups/14A_validate_numerical_foundation.py`
2. Existing Prompt 14A regression/self-test file.
3. `docs/stage-2/22_numerical_parameter_inventory.md`
4. `docs/stage-2/22_numerical_baseline_qa_report.md`
5. `docs/stage-2/22_formulas_and_balance.md`
6. Relevant Prompt 14A acceptance-gate record.
7. `docs/stage-2/06_stage_2_progress_log.md`
8. `docs/prompts/INDEX.md`

Do not rewrite the complete B-14 numerical architecture.

Do not rewrite the 393-record parameter inventory without a real source discrepancy.

If actual corrections to existing metadata become necessary, document the exact source evidence and affected records.

Preserve historical records and previously verified test results.

## 9.1 QA coverage disclosure

The final report must explicitly distinguish:

- Source-backed precision/rounding rules.
- Register-level conventions.
- Legitimate missing-data markers.
- Owner-reserved classifications.
- Unverified authority.
- Parser limitations.

Do not present partial source coverage as complete.

---

# 10. ACCEPTANCE GATES

Create or update a focused final correction acceptance-gate assessment.

| Gate | Acceptance objective |
|---|---|
| R1-R1-01 | Complete policy and governance review |
| R1-R1-02 | Existing 41 validator checks preserved |
| R1-R1-03 | Existing 48 self-tests preserved |
| R1-R1-04 | B-04 Treasury precision/rounding source verified |
| R1-R1-05 | Invalid Treasury precision/rounding mutation rejected |
| R1-R1-06 | B-04–B-07 precision/rounding metadata coverage verified |
| R1-R1-07 | All 393 owner-reserved flags reconciled |
| R1-R1-08 | False B-04 Treasury owner-reserved flag rejected |
| R1-R1-09 | Genuine owner-reserved parameter remains accepted |
| R1-R1-10 | False NO/YES owner-reserved mutations rejected |
| R1-R1-11 | Unrelated decision references cannot establish authority |
| R1-R1-12 | Ambiguous ownership fails closed |
| R1-R1-13 | New positive and negative regressions pass |
| R1-R1-14 | Previous C1/R1 regressions remain intact |
| R1-R1-15 | All 393 parameter records remain reconciled |
| R1-R1-16 | All 295 formula identifiers remain unchanged |
| R1-R1-17 | Historical QA evidence is preserved |
| R1-R1-18 | C1-R1 verbatim archive reconciled or limitation documented |
| R1-R1-19 | This final correction prompt archived and hashed |
| R1-R1-20 | Final project validator passes |
| R1-R1-21 | Documentation links and prompt index pass |
| R1-R1-22 | Owner-reserved decisions and policy remain protected |
| R1-R1-23 | No implementation or Git operations occurred |
| R1-R1-24 | Final independent handoff is prepared |

Use:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

Do not mark a gate PASS if the source evidence is missing.

Do not report all 393 owner-reserved flags as verified merely because the rows contain YES/NO text.

---

# 11. FINAL VALIDATION

Before declaring this final correction complete:

1. Run the complete Prompt 14A validator.
2. Run all 48 previous self-tests.
3. Run the new precision/rounding tests.
4. Run the new owner-reserved tests.
5. Re-run all nine original R1 mutation tests.
6. Confirm all previously corrected C1/R1 cases remain rejected.
7. Verify the B-04 Treasury correct baseline passes.
8. Verify the invalid Treasury precision/rounding mutation fails.
9. Verify the invalid Treasury owner-reserved mutation fails.
10. Verify at least one genuinely owner-reserved record remains correctly protected.
11. Verify all applicable owner-reserved classifications across the 393-record inventory.
12. Reconcile the current parameter inventory.
13. Reconcile the 295 active formula identifiers.
14. Verify all 20 B-03 carry-ins.
15. Run the relevant existing numerical validators.
16. Rerun documentation-link validation.
17. Run the final project validator.
18. Run decision-register tests.
19. Run next-action tests.
20. Verify prompt archives and SHA-256 values.
21. Inspect exact modified files.
22. Compare protected files and formula-register changes against the starting snapshot.
23. Inspect Git status without modifying it.
24. Verify no implementation work or unauthorized decision occurred.
25. Verify Prompt 14B was not started.

Inherited validator failures must remain separate from newly introduced failures.

Do not claim gameplay balance has been proven.

---

# 12. STRICT SCOPE CONTROL

This is the final targeted correction.

Do not start another broad audit or redesign.

Do not fix unrelated legacy validators.

Do not reopen Prompt 13.

Do not change any existing numerical balance value.

Do not add new game mechanics.

Do not create new system specifications.

Do not modify security or prototype implementation.

If another unrelated issue is noticed, record it as an observation without expanding this assignment.

If a genuine owner-reserved or source ambiguity prevents completion, report the exact blocker rather than making an unauthorized decision.

---

# 13. FINAL HANDOFF

Produce a final correction report containing:

1. Starting Project X (97) baseline.
2. B-04 Treasury precision/rounding source analysis.
3. The exact invalid precision/rounding mutation and its rejection evidence.
4. Owner-reserved classification source analysis.
5. The exact Treasury owner-reserved mutation and its rejection evidence.
6. All 393 owner-reserved field reconciliation results.
7. Positive and negative regression results.
8. Preservation of all previous 41 validator checks and 48 self-tests.
9. Total final validator and self-test counts.
10. C1-R1 archive reconciliation outcome.
11. Final C1-R1-R1 archive byte count and SHA-256.
12. Exact files modified.
13. Confirmation that the 295 original formulas are unchanged.
14. Confirmation that the 393-record inventory is preserved.
15. Confirmation that no owner-reserved decisions were changed.
16. Confirmation that the Autonomous Decision Policy remains unchanged.
17. Confirmation that no implementation or prototype modifications occurred.
18. Confirmation that no Git operations occurred.
19. Inherited QA limitations.
20. Final acceptance-gate table.
21. The single next action.

The completion recommendation must be exactly one of:

- COMPLETE.
- PARTIAL.
- NOT COMPLETE.

---

# 14. FINAL SUCCESS CONDITION — CLOSE PROMPT 14A

This correction is complete only when:

- Invalid B-04 Treasury precision/rounding metadata is rejected.
- Source-backed precision/rounding conventions are validated across B-04 through B-07.
- Invalid B-04 Treasury owner-reserved classification is rejected.
- All 393 owner-reserved field classifications are reconciled against their appropriate authorities.
- Genuine owner-reserved records remain protected.
- Unrelated D/DD/UD references cannot create false numerical approval.
- Positive and negative regression tests pass.
- All earlier 41 validator checks and 48 self-tests remain preserved and passing.
- The previous nine C1-R1 mutation weaknesses remain fixed.
- All 295 original formula definitions remain unchanged.
- All 393 parameter records remain accounted for.
- C1-R1 archive integrity is reconciled.
- The final correction prompt is archived verbatim and verified.
- All applicable project QA passes.
- Owner-reserved decisions remain intact.
- No implementation work or Git operation occurs.
- No subsequent Prompt 14 phase is executed.

When all conditions are satisfied, the final status must state:

**PROMPT 14A — DOCUMENTATION AND NUMERICAL FOUNDATION COMPLETE.**

**PROMPT 14A-C1 — COMPLETE.**

**PROMPT 14A-C1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1 — COMPLETE.**

**PROMPT 14A — READY FOR FINAL INDEPENDENT OWNER ACCEPTANCE.**

**NEXT ACTION: AWAIT THE OWNER'S EXPLICIT AUTHORIZATION OF PROMPT 14B.**

If any condition remains unverified, report the precise unresolved gate. Do not create another broad correction prompt for unrelated matters.

**END OF PROMPT 14A-C1-R1-R1**
