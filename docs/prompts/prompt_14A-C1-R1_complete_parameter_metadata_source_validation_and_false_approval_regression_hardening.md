# PROMPT 14A-C1-R1 — COMPLETE PARAMETER METADATA SOURCE VALIDATION AND FALSE-APPROVAL REGRESSION HARDENING

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Master Game Design Bible  
**Parent phase:** Prompt 14 — Numbers, Formulas, Balance and Worked Examples  
**Original phase:** Prompt 14A — Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Correction chain:** Prompt 14A-C1 → Prompt 14A-C1-R1  
**Execution type:** Targeted documentation-validator and regression-test correction  
**Implementation authorization:** NONE  
**Next phase:** Prompt 14B — NOT STARTED / NOT AUTHORIZED  
**Authority:** D-014 — Autonomous Decision Policy  
**Baseline:** Project X (96)

---

# 1. MISSION

Execute a narrowly scoped correction to the Prompt 14A numerical parameter validator.

The independent audit of Project X (96) confirmed that Prompt 14A and most of C1 are substantially complete.

However, additional independent mutation tests identified nine validator weaknesses.

The validator currently passes certain parameter modifications that it must reject.

The affected information includes:

- Parameter units.
- Decision authority.
- Numerical approval status.
- Timing.
- Evidence requirements.
- Evidence classifications.
- Owner-reserved status.
- Source-to-inventory consistency.

The purpose of C1-R1 is to make the numerical parameter inventory independently verifiable across all 393 existing parameter records.

**The validator must detect unauthorized or unsupported changes to source-backed parameter metadata, not merely verify that records and headings exist.**

This correction must preserve all previously completed Prompt 14A and C1 work.

Do not restart either phase.

Do not change the game's numerical formulas or balance parameters.

Do not begin Prompt 14B.

---

# 2. MANDATORY GOVERNANCE

Before starting, read the complete:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Also read:

- The complete archived Prompt 14A.
- The complete archived Prompt 14A-C1.
- The current Prompt 14A canonical B-14 document.
- The complete numerical parameter inventory.
- The complete formula master inventory.
- The current numerical baseline QA report.
- The current Prompt 14A validator.
- Its complete regression-test suite.
- The applicable decision and DD/UD registers.

Follow D-014 and all owner-reserved boundaries.

## 2.1 Strict restrictions

You MUST NOT:

1. Modify `AUTONOMOUS_DECISION_POLICY.md`.
2. Change any owner-approved numerical value.
3. Resolve or reinterpret any owner-reserved UD.
4. Change any original formula definition.
5. Change the existing 393 parameter records merely to make the validator pass.
6. Change any initial treasury, resource, cost, production, research, market, diplomacy, Alliance, warfare or progression value.
7. Change D-015 or its approved Operations Points model.
8. Change D-019.
9. Change the two-hour UTC turn cadence.
10. Change the P0–P7 turn sequence.
11. Modify frontend, backend, database, SQL, API, migration, security or deployment implementation.
12. Modify gameplay prototypes.
13. Perform Git operations.
14. Stage, commit, push, reset, revert or discard files.
15. Reopen unrelated accepted project phases.
16. Start Prompt 14B or any subsequent Prompt 14 subphase.

The original nine formula registers must remain unchanged.

The existing B-14 canonical filename must remain:

`docs/stage-2/22_formulas_and_balance.md`

The previously authorized Prompt 14A-C1 corrections must be preserved.

---

# 3. VERIFIED PROJECT X (96) BASELINE

Use the actual repository as the source of truth.

The previous independent audit established the following baseline.

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

Preserve all 295 active formula identifiers.

The retired formula `F-WEP-048` must remain excluded from the active total.

## 3.2 Numerical parameter inventory

| System | Parameter records |
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

These are parameter inventory records, not necessarily individual scalar values. Vector and grouped records must retain their existing structure.

Do not change the inventory count without evidence from the authoritative source documents.

## 3.3 Existing validators

Current Prompt 14A validator:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Project X (96) baseline:

- Validator: 35/35.
- Self-tests: 35/35.

These existing checks must be preserved.

Add stronger source-to-inventory validation and regression coverage.

Do not remove, weaken or bypass any previous check.

---

# 4. NINE INDEPENDENTLY REPRODUCED MUTATION FAILURES

The following nine mutations were independently tested against temporary copies of the Project X (96) parameter inventory.

The validator incorrectly passed them.

C1-R1 MUST make every one of these mutations fail.

| # | System | Parameter | Mutation | Expected result |
|---:|---|---|---|---|
| 1 | B-10 | F-WR-003 | Change unit to `bananas` | REJECT |
| 2 | B-04 | Treasury parameter | Change numerical decision authority | REJECT |
| 3 | B-04 | Treasury parameter | Promote PROVISIONAL to OWNER-APPROVED without evidence | REJECT |
| 4 | B-04 | Treasury parameter | Change timing metadata | REJECT |
| 5 | B-03 | Observation window | Change unit from hours to bananas | REJECT |
| 6 | B-03 | Observation window | Replace its evidence requirement with `evidence already satisfied` | REJECT |
| 7 | B-03 | Observation window | Change evidence classification from Playtest data to Confirmed | REJECT |
| 8 | B-02 | Turn length | Change OWNER-APPROVED status to PROVISIONAL without source evidence | REJECT |
| 9 | B-12 | FP-P07 | Change unit to bananas | REJECT |

Use the exact canonical parameter names and source records.

If a parameter name differs from this description in the actual inventory, resolve it against the canonical source rather than inventing a replacement identifier.

These nine cases must become permanent regression fixtures.

---

# 5. RECONCILE ALL 393 PARAMETER RECORDS AGAINST AUTHORITATIVE SOURCES

This is the central requirement.

The validator must verify parameter metadata across every applicable system:

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

All 393 records must have source reconciliation.

A system-specific parser may be necessary because the existing source registers use different Markdown structures.

That is acceptable.

Incomplete coverage or silent skipping is not acceptable.

## 5.1 Required validation fields

For each applicable parameter, independently compare:

| Field | Required verification |
|---|---|
| Parameter ID/name | Exact authoritative identity |
| Owning system | Correct B-section |
| Source document | Correct canonical path |
| Source section | Actual source location |
| Current value | Source-to-inventory equality |
| Unit | Exact source-supported unit |
| Precision | Exact source rule or explicit missing-data marker |
| Rounding | Exact source rule or explicit missing-data marker |
| Timing | Exact source rule or explicit missing-data marker |
| Formula dependencies | Valid source formula identifiers |
| Decision authority | Actual documented authority |
| Implementation owner | Correct ownership where specified |
| Validator owner | Correct ownership where specified |
| Numerical status | Evidence-supported classification |
| Owner-reserved status | Actual decision-register status |
| Evidence requirement | Exact source-supported requirement |
| Evidence classification | Exact source-supported classification |
| Reopening conditions | Correctly preserved |
| Outstanding dependencies | Correctly represented |

Not every source defines every field.

In such cases:

- Use an explicit `NOT SPECIFIED IN SOURCE` marker.
- Verify that the canonical source genuinely omits the field.
- Distinguish absence of a source requirement from a validator's inability to parse it.
- Do not manufacture metadata.

A missing-data marker is acceptable only when the source has actually been examined and no such field is specified.

An extraction failure is not equivalent to a legitimate missing-data marker.

## 5.2 Mandatory field coverage report

Produce an explicit coverage matrix.

| System | Records | Values | Units | Precision | Rounding | Timing | Authority | Status | Evidence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B-02 | 7 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-03 | 20 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-04 | 49 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-05 | 73 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-06 | 96 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-07 | 26 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-08 | 12 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-09 | 8 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-10 | 39 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-11 | 49 | Report | Report | Report | Report | Report | Report | Report | Report |
| B-12 | 14 | Report | Report | Report | Report | Report | Report | Report | Report |
| **Total** | **393** | | | | | | | | |

For every field, report:

- Source-defined and successfully matched.
- Source-defined but mismatched.
- Not specified in the source and explicitly marked.
- Unable to parse or verify.

The last category must never silently count as PASS.

The report must distinguish actual source completeness from validator coverage.

---

# 6. VALIDATE UNITS PROPERLY

The validator must compare units against authoritative sources.

Do not merely check that the unit field is non-empty or syntactically valid.

Examples:

- A duration expressed in hours must not silently become a resource unit.
- A percentage must not silently become a basis-point value.
- A per-turn production rate must not become a per-day rate.
- A population value must not become a treasury value.
- A military point must not become a resource quantity.

Preserve legitimate compound and vector units.

Do not force all systems into one unit convention.

For every record:

1. Identify the actual source unit.
2. Identify the inventory unit.
3. Compare them.
4. Report any difference.
5. Reject unsupported modifications.

Missing units must be explicitly identified as source omissions or unresolved specification gaps.

---

# 7. VALIDATE PARAMETER OWNERSHIP AND DECISION AUTHORITY

This is a critical governance safeguard.

The validator must compare the ownership information against its proper authoritative source.

Inspect:

- The canonical B-section.
- `docs/DECISIONS.md`.
- Applicable DD records.
- Applicable UD records.
- B-03 §21.2 and §21.3.
- Existing owner authorization evidence.

Do not equate these separate responsibilities:

1. System specification owner.
2. Numerical decision authority.
3. Formula owner.
4. Implementation owner.
5. Validator/test owner.
6. Owner-reserved decision authority.

## 7.1 Owner-approved values

A parameter must not be classified as OWNER-APPROVED merely because:

- A D-number is present.
- A decision reference appears nearby.
- The parameter exists in a specification.
- A formula validator passes.
- A coding agent labels it approved.
- The parameter was proposed in an earlier prompt.

The referenced decision must explicitly support approval of that numerical value or its precise governing rule.

The evidence must be traceable to the actual decision record.

If the decision only establishes the formula structure, it cannot automatically approve the formula's provisional numerical constants.

If approval cannot be proved:

- Preserve the appropriate existing status.
- Identify the missing approval evidence.
- Report the issue.
- Do not invent owner approval.

## 7.2 Owner-reserved parameters

Verify that owner-reserved values cannot be changed into ordinary Category B decisions or OWNER-APPROVED values without actual owner authorization.

Preserve the existing Alliance and fair-play decision boundaries.

---

# 8. VALIDATE ALL FOUR NUMERICAL STATUSES

Use the four existing labels exactly:

1. `OWNER-APPROVED VALUE`
2. `PROVISIONAL VALUE`
3. `DESIGN PROPOSAL`
4. `NEEDS PLAYTESTING`

The validator must verify the classification against source evidence.

## 8.1 Required safeguards

- OWNER-APPROVED VALUE requires explicit approval evidence for the actual value or governing numerical rule.
- PROVISIONAL VALUE must preserve its unresolved evidence and ownership.
- DESIGN PROPOSAL must remain separate from the current authoritative formula/value.
- NEEDS PLAYTESTING must preserve the measurement and playtesting requirements.

The presence of a decision ID is not sufficient proof of numerical approval.

A successful arithmetic test is not sufficient proof of numerical approval.

A documentation validator passing is not sufficient proof of numerical approval.

A Category B design decision does not automatically become an owner-approved numerical value.

A Category C decision must retain its provisional status until its required evidence has been obtained.

Do not invent a fifth status.

---

# 9. B-03 EVIDENCE METADATA VALIDATION

B-03 requires particular attention because its §21.2 table contains 20 provisional parameters with numerical owner and validator responsibility.

All 20 records must be checked against the actual canonical source.

For each record, verify:

- Parameter name.
- Value.
- Unit.
- Status.
- Numerical owner.
- Validator owner.
- Evidence requirement.
- Evidence classification.
- Review conditions.
- External dependencies.
- Applicable UD disposition.

The validator must reject:

- A changed evidence requirement.
- An incorrect evidence classification.
- A fabricated claim that evidence has already been satisfied.
- A changed parameter owner.
- An unsupported status promotion.
- A changed source value.
- A changed unit.

Do not rewrite B-03 to make B-14 validation easier.

Do not promote any of its provisional values.

Keep the actual B-03 owner and validator assignments.

---

# 10. SOURCE-SPECIFIC VALIDATION ADAPTERS

Inspect the actual structures of the source documents and implement appropriate adapters.

At minimum, cover these systems.

## B-02

Validate:

- Turn length.
- Two-hour UTC cadence.
- P0–P7 references.
- Timing values.
- Approval status.
- Relevant decision authority.

The established turn schedule must remain unchanged.

## B-03

Validate all 20 §21.2 carry-ins, including evidence, units, owners and statuses.

## B-04 through B-07

Validate:

- Current numerical values.
- Units.
- Parameter authorities.
- Precision.
- Rounding.
- Timing.
- Formula dependencies.
- Numerical statuses.

## B-08 and B-09

Validate:

- Diplomatic and Alliance parameter identities.
- Numerical ownership.
- Units.
- Timing.
- Rounding.
- Owner-reserved restrictions.
- Numerical status.

Do not invent Alliance storage, withdrawal, taxation or operational-funding permissions.

## B-10

Validate:

- Warfare parameter identities.
- Units.
- Costs and point types.
- Turn timing.
- Decision authority.
- Provisional status.
- Approved D-015 model references.

Do not redesign the Operations Points model.

## B-11

Validate:

- Event and reward parameters.
- Objective and ranking parameters.
- Units.
- Timing.
- Caps and thresholds.
- Evidence and status.

Preserve retired formula classifications.

## B-12

Validate:

- Fair-play parameter identities.
- Units.
- Thresholds.
- Measurement windows.
- Retention periods.
- Ownership.
- Status.
- External dependencies.

Preserve owner-reserved, legal-review and implementation-measurement requirements.

---

# 11. VALIDATOR IMPLEMENTATION REQUIREMENTS

Primary validator:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Strengthen this existing validator.

Do not create a disconnected replacement that leaves the old validator weak.

## 11.1 Independent source extraction

Expected values must originate from authoritative source documents or independently controlled source fixtures.

Do not generate expected values from the B-14 inventory and then compare that inventory against itself.

Avoid using exactly the same faulty extraction logic for:

- Inventory generation.
- Authoritative expected values.
- Regression-test expectations.

Use source-specific extraction where needed.

Document assumptions and test the parsers.

## 11.2 Fail-closed validation

If a source-defined field cannot be parsed or verified, the validator must:

- Report the exact record.
- Report the unverified field.
- Identify the source.
- Return a non-zero exit code for a material validation gap.

It must not silently skip the record.

An explicit source omission is different from an extraction failure.

## 11.3 Useful error output

For each failure report:

- System.
- Parameter ID/name.
- Field.
- Expected source value.
- Actual inventory value.
- Canonical source path.
- Source section.
- Inventory location.
- Failure category.

Do not return generic failure messages without record-level evidence.

## 11.4 Deterministic execution

The validator must produce deterministic results.

Use the repository's established Python conventions.

Prefer standard-library functionality.

Do not add unnecessary external packages.

Do not introduce filesystem-dependent or network-dependent assumptions.

---

# 12. REQUIRED REGRESSION TESTS

Preserve all existing Prompt 14A and C1 tests.

Add all nine independently reproduced mutations from §4.

In addition, add the following regression cases.

| # | Regression case | Expected |
|---:|---|---|
| 1 | Change a source-defined parameter unit | REJECT |
| 2 | Change a source-defined decision authority | REJECT |
| 3 | Promote an unapproved provisional value | REJECT |
| 4 | Change a source-defined timing field | REJECT |
| 5 | Change source-backed precision | REJECT |
| 6 | Change source-backed rounding | REJECT |
| 7 | Fabricate evidence completion | REJECT |
| 8 | Change evidence classification | REJECT |
| 9 | Change owner-reserved status | REJECT |
| 10 | Remove a source-backed parameter record | REJECT |
| 11 | Duplicate a parameter record | REJECT |
| 12 | Modify a B-03 carry-in value | REJECT |
| 13 | Modify a B-03 unit | REJECT |
| 14 | Modify a B-03 owner | REJECT |
| 15 | Modify a B-03 evidence requirement | REJECT |
| 16 | Modify a B-03 evidence classification | REJECT |
| 17 | Modify B-02 turn-length status | REJECT |
| 18 | Modify B-12 unit | REJECT |
| 19 | Preserve a correctly sourced provisional value | ACCEPT |
| 20 | Preserve an explicitly approved and evidenced numerical value | ACCEPT |
| 21 | Preserve an explicitly documented missing-data field | ACCEPT |
| 22 | Report an unparseable source field | BLOCKED/FAIL, never PASS |

Avoid duplicate tests that do not add a distinct protection.

## 12.1 Testing method

All mutation tests must use temporary fixtures or temporary copies.

Do not corrupt authoritative source files or actual project inventory files during testing.

Demonstrate that each test genuinely changes the relevant data.

Run the actual validator against the modified fixture.

Capture its process exit code and diagnostic output.

A test passes only when the expected rejection or acceptance actually occurs.

## 12.2 Coverage reporting

Report:

- Number of parameter records discovered.
- Number of records reconciled.
- Number of fields source-validated.
- Number of source omissions.
- Number of unparseable fields.
- Number of mismatches.
- Number of owner/status checks.
- Number of positive regression tests.
- Number of negative regression tests.
- Total self-tests.

Do not use the total number of passing checks as a substitute for coverage information.

---

# 13. REQUIRED FILES AND DOCUMENTATION

Update only the files genuinely required.

At minimum inspect:

- `docs/qa_backups/14A_validate_numerical_foundation.py`
- Existing Prompt 14A self-test/regression file.
- `docs/stage-2/22_numerical_parameter_inventory.md`
- `docs/stage-2/22_formulas_and_balance.md`
- `docs/stage-2/22_numerical_baseline_qa_report.md`
- Relevant Prompt 14A acceptance-gate record.
- `docs/stage-2/06_stage_2_progress_log.md`
- Relevant current continuity records.

Do not rewrite the original formula registers.

Do not replace the entire parameter inventory unnecessarily.

Only correct actual source inconsistencies discovered through this work.

If a real source inconsistency is found:

1. Report it.
2. Identify the affected record.
3. Preserve the original source authority.
4. Do not invent a correction.
5. Do not make an owner-reserved decision.
6. Record its status and next action.

## 13.1 Permanent prompt archive

Archive this complete instruction verbatim at:

`docs/prompts/prompt_14A-C1-R1_complete_parameter_metadata_source_validation_and_false_approval_regression_hardening.md`

Update:

`docs/prompts/INDEX.md`

Record:

- Prompt ID.
- Full title.
- Archive path.
- Archive date.
- Byte count.
- SHA-256.

Verify the archived instruction against the complete supplied prompt.

Do not overwrite the original Prompt 14A or C1 archives.

---

# 14. ACCEPTANCE GATES

Create a focused C1-R1 acceptance assessment.

| Gate | Acceptance objective |
|---|---|
| R1-01 | Complete policy and governance review |
| R1-02 | Nine original mutation cases rejected |
| R1-03 | All 393 parameter records source-reconciled |
| R1-04 | B-02 metadata validated |
| R1-05 | All 20 B-03 carry-ins validated |
| R1-06 | B-04 metadata validated |
| R1-07 | B-05 metadata validated |
| R1-08 | B-06 metadata validated |
| R1-09 | B-07 metadata validated |
| R1-10 | B-08 metadata validated |
| R1-11 | B-09 metadata validated |
| R1-12 | B-10 metadata validated |
| R1-13 | B-11 metadata validated |
| R1-14 | B-12 metadata validated |
| R1-15 | Units source-validated |
| R1-16 | Precision and rounding source-validated |
| R1-17 | Timing source-validated |
| R1-18 | Decision authorities source-validated |
| R1-19 | Four numerical status safeguards enforced |
| R1-20 | Evidence requirements and classifications validated |
| R1-21 | Owner-reserved decisions protected |
| R1-22 | Positive and negative regression suite passes |
| R1-23 | All earlier Prompt 14A/C1 checks preserved |
| R1-24 | QA and parameter coverage reports reconciled |
| R1-25 | Prompt archive and index verified |
| R1-26 | No original formula definitions changed |
| R1-27 | No implementation or Git changes |
| R1-28 | Final project validation completed |
| R1-29 | Handoff and completion assessment prepared |

Allowed statuses:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

Do not report a PASS when source evidence is absent.

A validator that skips an entire parameter category cannot pass its corresponding source-coverage gate.

An unparseable source field must remain a visible limitation.

---

# 15. FINAL VALIDATION

Before concluding:

1. Rerun the complete Prompt 14A validator.
2. Run all previous 35 Prompt 14A self-tests.
3. Run all previous 35 C1 self-tests.
4. Run all nine newly mandatory mutation cases.
5. Run every additional regression case.
6. Verify all 393 parameter records.
7. Verify source coverage for B-02 through B-12.
8. Reconcile the 295 active formula identifiers.
9. Verify the original formula registers are unchanged.
10. Verify all 20 B-03 carry-in records.
11. Verify the B-04 Treasury authority/status/timing safeguards.
12. Verify B-10 F-WR-003 unit protection.
13. Verify B-12 FP-P07 unit protection.
14. Verify B-02 turn-length approval status.
15. Verify D-015 and D-019 references.
16. Run relevant existing numerical validators.
17. Rerun documentation-link validation.
18. Run the final project validator.
19. Run decision-register tests.
20. Run next-action tests.
21. Verify the archived Prompt 14A-C1-R1 instruction.
22. Inspect all modified files.
23. Inspect Git status without changing it.
24. Verify the Autonomous Decision Policy is unchanged.
25. Verify no gameplay implementation or prototype files were modified.
26. Verify no subsequent Prompt 14 phase was started.

Keep inherited validator failures separate from newly introduced failures.

Do not describe documentation or offline arithmetic verification as runtime gameplay testing.

Do not claim balance has been established.

---

# 16. OUT-OF-SCOPE WORK

This correction does not authorize:

- Formula redesign.
- Parameter recalibration.
- Changing the 295 original formula definitions.
- Changing the 393 existing numerical parameter values.
- Changing starting treasury or initial resources.
- Changing production ratios.
- Changing research costs.
- Changing trade fees or price rules.
- Changing Alliance permissions.
- Changing warfare or Operations Points.
- Changing progression rewards.
- Changing fair-play thresholds.
- Resolving owner-reserved decisions.
- Creating new game mechanics.
- Creating a playable simulation.
- Modifying frontend/backend/database/API/SQL/security/deployment systems.
- Modifying the Autonomous Decision Policy.
- Performing Git operations.
- Starting Prompt 14B.

If the validator exposes a genuine source-document conflict, report it separately instead of silently deciding which owner-controlled value is correct.

---

# 17. FINAL HANDOFF

Produce a detailed C1-R1 completion report containing:

1. Starting Project X (96) baseline.
2. The nine original mutation failures.
3. How each mutation is now detected.
4. Source-specific adapter coverage.
5. All 393 parameter records' reconciliation status.
6. Units, precision, rounding and timing coverage.
7. Authority and approval-evidence coverage.
8. B-03 evidence-metadata coverage.
9. Four-status safeguard results.
10. All positive and negative regression results.
11. Total tests executed.
12. All outstanding source omissions or ambiguities.
13. Any genuine source inconsistencies.
14. Exact files modified.
15. Confirmation that the 295 original formulas remain unchanged.
16. Confirmation that owner-reserved decisions remain intact.
17. Confirmation that no implementation work occurred.
18. Confirmation that no Git operations occurred.
19. Prompt archive SHA-256 and byte count.
20. Final acceptance-gate table.
21. Remaining limitations.
22. The single next action.

The final recommendation must be one of:

- COMPLETE.
- PARTIAL.
- NOT COMPLETE.

Do not claim COMPLETE while any required source-backed parameter field remains unverified or can be silently altered without detection.

---

# 18. FINAL SUCCESS CONDITION

Prompt 14A-C1-R1 is complete only when:

- All nine previously reproduced mutation weaknesses are rejected.
- All 393 parameter records are reconciled against authoritative sources.
- Source-backed units cannot be silently modified.
- Source-backed timing cannot be silently modified.
- Precision and rounding metadata are validated.
- Numerical decision authority cannot be silently modified.
- Numerical approval cannot be fabricated using an unrelated decision reference.
- All four numerical statuses are evidence-controlled.
- B-03 values, units, owners, evidence requirements and classifications are source-validated.
- B-02 turn-length authority and status are verified.
- B-10 and B-12 unit validation is complete.
- All B-02 through B-12 systems have explicit validation coverage.
- Positive and negative regressions pass.
- Earlier Prompt 14A/C1 tests remain intact.
- The original 295 formula definitions are unchanged.
- The original 393 parameter records are preserved except for separately documented, source-authorized corrections.
- Owner-reserved decisions remain untouched.
- The correction archive is verified.
- The final project QA is complete.
- No implementation work or Git operations occurred.
- Prompt 14B has not been started.

**If all requirements pass:**

PROMPT 14A AND PROMPT 14A-C1 ARE READY FOR FINAL INDEPENDENT ACCEPTANCE.

**NEXT ACTION: AWAIT OWNER REVIEW AND EXPLICIT AUTHORIZATION OF PROMPT 14B.**

**If any gate remains unresolved:**

PROMPT 14A-C1-R1 REMAINS OPEN. REPORT THE EXACT UNRESOLVED RECORDS, FIELDS AND ACCEPTANCE GATES.

**END OF PROMPT 14A-C1-R1**
