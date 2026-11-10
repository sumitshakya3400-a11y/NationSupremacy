# PROMPT 12B-C1-R3 — DUPLICATE-ID DETECTION, STALE-REFERENCE VALIDATION AND FINAL VALIDATOR CLOSURE

## 1. Mission

Complete the remaining Prompt 12B-C1 validator weaknesses identified during the independent audit of Project X (72).

The R2 validator successfully fixed the three earlier bypasses. However, independent mutation testing identified four additional bypasses:

1. Duplicate parameter IDs in the acceptance gate are accepted.
2. Duplicate parameter IDs in AI_CONTEXT are accepted.
3. Stale parameter ranges elsewhere in the acceptance document are not detected.
4. Duplicate or conflicting current-state B-12 formula-register entries in AI_CONTEXT are not detected.

This task must fix all four defects, add explicit adversarial fixtures, and establish reliable cross-document parameter-integrity validation.

This is a targeted validator and documentation-closeout task. Do not rewrite Prompt 12B, C1, R1, or R2.

## 2. Live project working-directory requirement

You are working directly in the existing live Nation Supremacy project directory.

Make all changes directly in that existing project directory.

The owner's ZIP archives are independent audit snapshots only.

Do not:
- Extract or use an owner-uploaded audit ZIP as your working project.
- Create a duplicate project directory.
- Replace the live project with an archive.
- Overwrite live project work with snapshot contents.
- Ask the owner to move files into another working directory.

Inspect the current live files before editing. Preserve all unrelated changes.

## 3. Mandatory governance

Before starting:

1. Read the complete `AUTONOMOUS_DECISION_POLICY.md` in the live project.
2. Follow D-014 and all applicable project governance.
3. Inspect the canonical formula register.
4. Inspect the current Prompt 12B validator and its complete fixture/test structure.
5. Inspect the acceptance document, `docs/AI_CONTEXT.md`, and the R1/R2 progress-log entries.
6. Inspect the project prompt archive, prompt index, and roadmap conventions.
7. Review the R2 validator implementation to understand exactly why the four bypasses passed.

Do not rely on summaries or selected policy sections.

Resolve ordinary technical details autonomously using established project conventions. Do not reopen approved architecture, invent decisions, or close owner-reserved matters.

## 4. Canonical parameter authority

The canonical source of truth is:

`docs/stage-2/20_fair_play_and_player_protection_formula_register.md`

Verify the actual contents of this file before changing validator assumptions.

The expected current parameter set is:

- FP-P01
- FP-P02
- FP-P03
- FP-P04
- FP-P05
- FP-P06
- FP-P07
- FP-P08
- FP-P09
- FP-P10
- FP-P11
- FP-P12
- FP-P13
- FP-P14

There must be exactly 14 unique registered parameter identifiers.

Do not independently maintain inconsistent hard-coded parameter lists in separate validator functions.

Implement or reuse one authoritative extraction and validation routine. Other document checks must compare their references against the canonical extracted parameter set.

The canonical extraction must preserve occurrence information. Do not convert identifiers to a set before checking duplicates.

A set may be used for membership comparison after duplicate detection, but it must not erase evidence of repeated identifiers.

## 5. Required correction A — Duplicate-ID detection in P12B-19

Target:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

Relevant gate:

`P12B-19`

Existing validator check:

`12B-77`

### Required behaviour

Strengthen check `12B-77` so it verifies:

1. All 14 canonical parameter IDs are represented.
2. Each required parameter is represented exactly as intended by the document's conventions.
3. No parameter ID is repeated unintentionally.
4. No unexpected parameter ID is present.
5. No intermediate identifier is missing.
6. The displayed range is complete and consecutive where compact range notation is used.
7. The stated count agrees with the canonical register.

The validator must preserve the original extracted identifier sequence and frequency counts long enough to detect duplicates.

Do not silently deduplicate the extracted identifiers before validation.

### Mandatory adversarial mutation

The previous independent audit added another `FP-P01` to the otherwise correct complete P12B-19 parameter range.

The previous validator incorrectly returned PASS.

Create an explicit negative fixture reproducing this exact mutation.

Expected result: FAIL, with a diagnostic identifying the duplicated `FP-P01` in `P12B-19`.

Also test duplication of an intermediate identifier and an unexpected parameter ID.

## 6. Required correction B — Duplicate-ID detection in AI_CONTEXT

Target:

`docs/AI_CONTEXT.md`

Relevant content:

The current B-12 formula-register entry.

Existing validator check:

`12B-78`

### Required behaviour

Strengthen check `12B-78` so it verifies:

1. All 14 canonical parameter IDs appear in the current B-12 entry.
2. No required ID is missing.
3. No parameter ID is duplicated.
4. No unexpected parameter ID appears.
5. The parameter count agrees with the canonical register.
6. The displayed range is complete and consecutive.
7. The extracted current-state identifier list matches the canonical register.

Preserve occurrence counts during extraction.

Do not use set conversion as the first extraction operation.

### Mandatory adversarial mutation

The previous independent audit repeated `FP-P01` in the otherwise correct AI_CONTEXT parameter range.

The previous validator incorrectly returned PASS.

Create an explicit negative fixture reproducing the exact defect.

Expected result: FAIL, with a diagnostic identifying the duplicate parameter ID in the B-12 entry.

Also test a duplicate intermediate identifier and an unexpected ID.

## 7. Required correction C — Detect stale current-state parameter references throughout acceptance

Target:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

The previous independent audit retained a correct P12B-19 gate and correct §9 parameter count, but inserted this stale current-state statement elsewhere:

`Current formula-register range: FP-P01–FP-P12`

The previous validator incorrectly returned PASS.

### Required behaviour

Extend the current-state consistency validation so that a correct P12B-19 gate cannot conceal a stale current-state parameter claim elsewhere in the acceptance document.

Inspect all relevant current-state descriptions, not only P12B-19 and §9.1.

At minimum, validate:

- Current formula-register summaries.
- Current formula-to-parameter coverage descriptions.
- Acceptance gate descriptions that refer to the current parameter register.
- Validator specifications.
- Current-state matrices and summaries.
- Other explicit claims describing the present parameter count or range.

Reject current-state statements that:

- Claim 12 parameters.
- End the parameter range at FP-P12.
- Omit FP-P13 or FP-P14.
- Contain an incomplete or discontinuous range.
- Present a count inconsistent with the canonical register.
- Contradict another current-state description in the same document.

### Historical-record protection

Do not blindly reject every occurrence of `FP-P12` or the number 12.

Historical records may legitimately state that the earlier version had 12 parameters.

Distinguish:

- Current-state claims, which must match the current canonical register.
- Historical-state records, which must preserve the accurate earlier count.
- Unrelated references to 12.
- References to other identifiers or quantities.

Use section boundaries, labels, document conventions, and contextual markers to identify historical records.

A historical reference to the earlier 12-parameter state must not cause a false failure.

However, adding the word "historical" to an otherwise current-state stale claim must not be allowed to bypass validation when the claim is still presented as a current-state summary.

### Mandatory adversarial mutation

Create an explicit negative fixture that:

1. Retains the correct complete P12B-19 gate.
2. Retains the correct 14-parameter count in §9.
3. Adds the stale current-state statement `Current formula-register range: FP-P01–FP-P12` elsewhere in the acceptance document.

Expected result: FAIL.

Also create a positive fixture showing that an accurate historical reference to the earlier 12-parameter state remains valid.

## 8. Required correction D — Detect duplicate and conflicting current-state entries in AI_CONTEXT

Target:

`docs/AI_CONTEXT.md`

The previous independent audit retained the correct B-12 formula-register entry and added a second current-state entry for the same formula register that reported 12 parameters.

The previous validator selected the first matching entry and incorrectly returned PASS.

### Required behaviour

Strengthen the AI_CONTEXT validation so it identifies all current-state B-12 formula-register entries.

It must:

1. Locate every authoritative/current-state B-12 formula-register entry using the existing document structure.
2. Confirm there is exactly one authoritative current-state entry unless the established project convention explicitly permits multiple entries with clearly distinct purposes.
3. Validate every permitted current-state entry against the canonical 14-parameter set.
4. Reject conflicting parameter counts or ranges.
5. Reject duplicate or contradictory current-state B-12 summaries.
6. Reject a second current-state entry that reports 12 parameters or FP-P01 through FP-P12.
7. Provide a clear diagnostic identifying the conflicting section or entry.

Do not simply select the first match.

Do not search the entire file indiscriminately and treat historical or unrelated mentions as current-state entries.

If there are legitimate multiple B-12 references, classify them according to their actual document roles. Ensure all current-state claims are synchronized.

### Mandatory adversarial mutation

Create an explicit negative fixture that:

1. Retains the correct existing B-12 formula-register entry.
2. Adds a second current-state B-12 formula-register entry reporting 12 parameters.
3. Leaves the first correct entry unchanged.

Expected result: FAIL, identifying the duplicate or conflicting current-state entry.

Also test an additional current-state entry containing 14 parameters but an incomplete range. It must fail.

## 9. Required correction E — Robust shared extraction and comparison

Review the R2 extraction implementation, including any function equivalent to `extract_param_ids()`.

The previous implementation lost duplicate evidence by converting identifiers into a set.

Replace or refactor it so the validation pipeline preserves:

- Ordered identifier occurrences.
- Duplicate frequency.
- Missing identifiers.
- Unexpected identifiers.
- Discontinuous ranges.
- Source section and entry identity.
- Whether the source is current-state or historical.

The shared validation routine should return enough structured information for the individual document checks to produce accurate diagnostics.

At a minimum, the comparison should identify:

- Expected parameter set.
- Actual ordered parameter occurrences.
- Missing IDs.
- Duplicate IDs and their counts.
- Unexpected IDs.
- Range gaps.
- Conflicting current-state entries.
- Source document and section.

Use the project's existing programming and test conventions.

Avoid introducing unnecessary dependencies.

Do not use one broad whole-file regular expression as a substitute for contextual section extraction.

## 10. Required correction F — Adversarial fixtures

Create explicit fixtures for every identified bypass.

### F1. Acceptance gate

1. Complete FP-P01 through FP-P14 range: PASS.
2. Duplicate FP-P01: FAIL.
3. Duplicate an intermediate parameter: FAIL.
4. Unexpected parameter identifier: FAIL.
5. Missing FP-P13: FAIL.
6. Missing FP-P14: FAIL.
7. Missing intermediate parameter: FAIL.
8. Historical 12-parameter record: PASS.

### F2. AI_CONTEXT

9. Complete FP-P01 through FP-P14 range: PASS.
10. Duplicate FP-P01: FAIL.
11. Duplicate an intermediate parameter: FAIL.
12. Unexpected parameter ID: FAIL.
13. Missing FP-P13: FAIL.
14. Incomplete range ending at FP-P12: FAIL.
15. Second conflicting current-state B-12 entry with 12 parameters: FAIL.
16. Second current-state B-12 entry with an incomplete 14-parameter claim: FAIL.
17. Historical reference to the earlier 12-parameter state: PASS.

### F3. Acceptance stale-current-state references

18. Correct P12B-19 and §9 with no contradictory current-state references: PASS.
19. Add the stale current-state range FP-P01 through FP-P12 elsewhere: FAIL.
20. Add a stale current-state statement claiming 12 parameters elsewhere: FAIL.
21. Accurate historical statement describing the old 12-parameter state: PASS.
22. Unrelated use of the number 12: PASS.

### F4. Manifest regression

Preserve the R2 protection for the actual R1 §77.1 manifest.

23. Correct AI_CONTEXT entry in §77.1: PASS.
24. AI_CONTEXT removed from §77.1 but retained in §76.1: FAIL.
25. AI_CONTEXT mentioned elsewhere but absent from §77.1: FAIL.

The existing manifest tests must continue to pass.

### Fixture integrity

For every negative fixture:

- Confirm that it fails because of the intended validation check.
- Do not count a syntax error, missing test setup, or unrelated exception as proof of correct rejection.
- Include an assertion for the expected diagnostic/check identity where supported.
- Run the complete positive and negative fixture suites.

For every positive fixture:

- Demonstrate that valid current-state and historical records are accepted.
- Ensure the validator does not over-reject legitimate historical references.

Use temporary copies or in-memory mutation inputs. Do not corrupt the actual live files during tests.

Do not delete, weaken, skip, relabel, or bypass previous fixtures.

## 11. Required correction G — Validator diagnostics

Each relevant validator failure must identify:

- The affected document.
- The affected section or entry.
- The missing, duplicated, or unexpected parameter.
- The nature of the mismatch.
- The relevant validator check.

Examples of expected diagnostic meaning:

- `P12B-19 contains duplicate parameter FP-P01`.
- `AI_CONTEXT B-12 entry contains duplicate parameter FP-P01`.
- `Acceptance document contains stale current-state range FP-P01–FP-P12 in section ...`.
- `AI_CONTEXT contains a conflicting second current-state B-12 formula-register entry`.
- `Expected 14 parameter IDs but found an incomplete or discontinuous range`.

Do not produce generic error messages that hide the source of the defect.

## 12. Required correction H — Preserve existing R2 protections

All previous R1/R2 protections must remain effective:

1. Acceptance P12B-19 checks the complete parameter range.
2. AI_CONTEXT checks the complete parameter range.
3. R1 §77.1 manifest is checked independently of §76.1.
4. Historical C1 manifest accuracy is preserved.
5. The three original R2 adversarial bypasses remain rejected.
6. No simplistic project-wide ban on the number 12 is introduced.
7. The canonical parameter register remains the source of truth.

Do not resolve the new defects by removing earlier checks or changing expected fixture outcomes.

## 13. Progress status and truthful completion records

Inspect current R1 and R2 status statements in:

- `docs/AI_CONTEXT.md`
- Project progress log, especially §§76–77 and the existing R2 entry.
- Relevant roadmap and project-status documents.

Do not erase historical results.

Until R3 genuinely passes all mandatory requirements, do not claim final validator closure.

After successful completion:

1. Add a new R3 progress-log entry using the next appropriate section number.
2. Record all files actually changed.
3. Record the four independently reproduced bypasses.
4. Record the new checks and explicit mutation fixtures.
5. Record actual test outcomes.
6. Distinguish R1 documentation synchronization, R2 original bypass corrections, and R3 additional validator corrections.
7. Update current-state project summaries to reflect the actual result.
8. Preserve historical progress entries exactly where they remain accurate.

If any required bypass remains undetected, report PARTIAL and explain the unresolved gap.

Do not inflate check counts or mark work complete solely because the main validator passes.

## 14. Prompt archival

Archive this complete R3 prompt using the existing prompt-file conventions.

Suggested filename:

`docs/prompts/prompt_12B-C1-R3_duplicate_id_and_stale_reference_validation.md`

Inspect the prompt index before adopting the name.

Requirements:

- Save the complete prompt text.
- Update `docs/prompts/INDEX.md`.
- Update any required prompt inventory or roadmap reference.
- Verify archive/index consistency.
- Preserve original Prompt 12B, C1, R1, and R2 archives.
- Do not invent an approval or authorization status.
- Record R3 as a targeted validator correction.

## 15. Regression validation

After implementation, execute:

1. Prompt 12B validator.
2. All Prompt 12B positive fixtures.
3. All Prompt 12B negative fixtures.
4. All new R3 adversarial fixtures.
5. Prompt 12A validator and fixtures.
6. Documentation link validator.
7. Final project validator.
8. Formula-register consistency checks.
9. Integration-traceability checks.
10. Relevant project regression tests.
11. Any validators affected by the prompt archive, index, roadmap, AI_CONTEXT, or progress-log changes.

Report exact commands, actual outputs, test totals, failures, and skipped tests.

### Known legacy issue

Preserve and accurately report the existing Prompt 11A issue:

`11A_validate_research.py` check 29 expects REQ-703, while the legitimate global requirement frontier is REQ-869.

Do not weaken the validator or claim this issue was fixed by R3 unless it was separately and legitimately corrected with appropriate authorization.

## 16. Acceptance and governance preservation

Preserve the current Prompt 12B acceptance result:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL/BLOCKED.

Preserve these three PARTIAL gates:

- `P12B-14`: audit-spine and tamper-evidence implementation is not verified.
- `P12B-16`: prototype database privilege and audit-protection defects remain.
- `P12B-23`: project-wide synchronization and legacy validator debt.

Preserve all existing:

- Requirements REQ-764 through REQ-869.
- Decisions D-178 through D-187.
- Mirrored decisions DD-226 through DD-235.
- Unresolved UD-017 and UD-052 through UD-060.
- Formula identifiers and parameter identifiers.
- Integration contract IDs and B-system mappings.
- Owner-reserved and legal-dependent matters.

Do not approve, close, defer, or reinterpret owner-reserved decisions without authorization.

A passing documentation validator does not prove production implementation or runtime security.

## 17. Strict scope restrictions

This task is limited to documentation consistency, validator maintenance, tests, archival and governance records.

Do not:

- Start Prompt 12C.
- Create Prompt 12C workflows, journeys, or acceptance specifications.
- Change gameplay behaviour.
- Implement production security controls.
- Add or modify production migrations.
- Change database permissions, grants, RLS policies, or triggers.
- Implement runtime audit-digest or tamper-evidence mechanisms.
- Change approved architecture.
- Rewrite the four main B-12 specification documents unnecessarily.
- Create a duplicate project directory or use an audit ZIP as the working project.
- Stage, commit, or push Git without explicit owner authorization.

Document unrelated discoveries separately instead of expanding scope.

## 18. Final delivery report

Return a factual report containing:

### A. Four reproduced R2 bypasses

For each:
- Exact mutation.
- Previous check behaviour.
- Why the bypass occurred.
- Code correction.
- New negative fixture.
- Evidence that it now fails for the intended reason.

### B. Duplicate-ID protection

Show:
- Canonical expected IDs.
- Duplicate detection method.
- Acceptance gate result.
- AI_CONTEXT result.
- Duplicate and unexpected-ID fixture outcomes.

### C. Stale-reference and conflicting-entry protection

Show:
- Current-state range scan behaviour in the acceptance document.
- Historical-record treatment.
- AI_CONTEXT current-state entry extraction.
- Duplicate/conflicting entry handling.
- Fixture outcomes.

### D. Preserved R2 coverage

Confirm that all three original R2 bypasses still fail as expected.

### E. Files and archival

List:
- All files changed.
- R3 permanent prompt path.
- Prompt index and roadmap changes.
- New progress-log entry.
- Validator and fixture files.

### F. Test evidence

Provide:
- Exact commands.
- Total checks.
- Passed and failed checks.
- Positive fixture totals.
- Negative fixture totals.
- Each of the four new bypass outcomes.
- Regression results.
- Skipped or unavailable tests.
- Known legacy issue.

### G. Acceptance and governance

Confirm preservation of:
- 23 PASS / 3 PARTIAL / 0 FAIL-BLOCKED.
- Three existing PARTIAL gates.
- All unresolved owner decisions.
- Existing requirements, formula, decision, and integration identifiers.

### H. Scope confirmation

Explicitly confirm:
- Prompt 12C was not started.
- No production implementation or database security changes were made.
- No Git stage, commit, or push was performed.
- All changes were made in the existing live project directory.

### I. Final verdict

Select exactly one:

**COMPLETE** — every R3 requirement is satisfied and the explicit adversarial fixtures demonstrate that all four newly identified bypasses and all earlier R2 bypasses are rejected.

**PARTIAL** — any required check, fixture, documentation correction, or validation remains incomplete or unverified.

Do not declare COMPLETE based solely on a passing validator total.

## 19. Stop condition

After R3, stop and provide the factual delivery report.

Do not start Prompt 12C or any subsequent project phase without the owner's explicit authorization.

Leave the existing live project ready for the owner's next independent audit.