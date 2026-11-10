# PROMPT 12B-C1-R2 — VALIDATOR COMPLETENESS, ADVERSARIAL MUTATION TESTS AND FINAL CLOSEOUT

## 1. Mission

Complete the remaining Prompt 12B-C1-R1 validator-closure work.

The independent audit of Project X (71) found that the R1 documentation corrections are present, but three validator checks can still pass when required information is missing.

This task must correct those three weaknesses, add adversarial negative fixtures that reproduce the failures, and establish that the validator genuinely enforces the requirements rather than merely detecting selected keywords.

This is a targeted validator-maintenance and documentation-closeout task. Do not rewrite Prompt 12B, C1, or R1.

## 2. Live project working-directory requirement

You are working directly in the existing live Nation Supremacy project directory.

All project changes must be made directly in that existing working directory.

The owner may create ZIP snapshots and upload them to an independent reviewer. Those ZIP files are audit snapshots only.

Do not:
- Extract an owner's audit ZIP and use it as your working project.
- Treat an uploaded ZIP as the authoritative working directory.
- Create another project directory or duplicate project.
- Replace or overwrite the live project using an archive.
- Ask the owner to move project files into a different working directory.

Inspect the existing live files before making changes.

## 3. Mandatory governance

Before starting:

1. Read the complete `AUTONOMOUS_DECISION_POLICY.md` in the live project.
2. Follow D-014 and applicable project governance.
3. Inspect the existing Prompt 12B validator, its fixtures, test harness, and mutation-testing conventions.
4. Inspect the current formula register, acceptance document, AI_CONTEXT, prompt archive/index, and project progress log.
5. Preserve all approved identifiers, architecture, historical records, owner-reserved decisions, and legal-dependent matters.

Resolve ordinary implementation details autonomously using established project conventions.

Do not invent evidence, claim unexecuted tests, backdate attestations, or mark work complete before it has actually passed.

## 4. Required correction A — Full parameter-range validation in acceptance gate

Target file:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

Relevant gate: `P12B-19`.

The canonical formula register currently contains exactly 14 registered parameters:

`FP-P01` through `FP-P14`.

The acceptance gate must cover the complete parameter range.

### Required validator behaviour

Strengthen the existing check, currently identified as `12B-77`, so it validates the complete set of parameter identifiers rather than merely checking that the count is 14 and that `FP-P14` appears.

The validator must:

1. Extract the relevant `P12B-19` gate section using the existing document structure.
2. Identify all registered parameter IDs referenced by that gate.
3. Compare the extracted identifiers against the canonical expected set.
4. Require all 14 IDs:
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
5. Detect missing identifiers, unexpected identifiers, and duplicates where the document's representation makes duplicates meaningful.
6. Reject incomplete, discontinuous, or misleading ranges.
7. Avoid accepting a document merely because it contains the text `14 parameters` and `FP-P14`.

### Mandatory adversarial test

The previous independent audit replaced the gate's complete range with this incomplete range:

`FP-P01, FP-P02, FP-P14`

The old validator incorrectly passed it.

Create a negative fixture reproducing this exact defect. The strengthened validator must reject it.

Also test a range that omits FP-P13 while retaining FP-P14 and the claim of 14 parameters. It must fail.

## 5. Required correction B — Full parameter-range validation in AI_CONTEXT

Target file:

`docs/AI_CONTEXT.md`

Relevant content: the current B-12 formula-register entry.

The current-state summary must represent all 14 registered parameter IDs.

### Required validator behaviour

Strengthen the existing check, currently identified as `12B-78`.

It must:

1. Extract the current B-12 formula-register entry, not search the entire file indiscriminately.
2. Validate the full set FP-P01 through FP-P14.
3. Compare the extracted identifiers with the canonical formula-register identifiers.
4. Detect missing, unexpected, discontinuous, and duplicate identifiers where appropriate.
5. Confirm that the current-state parameter count is consistent with the canonical register.
6. Reject a statement that claims 14 parameters but lists an incomplete range.
7. Reject a range ending at FP-P12.
8. Preserve unrelated historical statements and unrelated occurrences of the number 12.

Do not merely test for the presence of the strings `14 parameters` and `FP-P14`.

### Mandatory adversarial test

The previous independent audit removed FP-P13 while retaining the 14-parameter claim and FP-P14.

The old validator incorrectly passed it.

Create a negative fixture reproducing this exact defect. The strengthened validator must reject it.

## 6. Required correction C — Validate the actual R1 manifest section

Target file:

The current Prompt 12B-C1/R1 progress log.

Relevant sections:
- §76.1: C1 change-manifest information.
- §77.1: R1-specific changed-file manifest.

The R1 changed-file manifest must independently account for the files changed by R1.

### Required validator behaviour

Strengthen the existing check, currently identified as `12B-80`.

It must:

1. Locate the actual R1-specific §77.1 manifest section using the project's structural conventions.
2. Extract entries from that section only.
3. Verify that `docs/AI_CONTEXT.md` is listed when R1 changes that file.
4. Verify the other files actually modified by R1 according to the manifest's stated scope and conventions.
5. Avoid treating an entry in §76.1 as proof that §77.1 is complete.
6. Detect a missing, malformed, or misplaced R1 manifest entry.
7. Preserve the historical accuracy of the C1 manifest.

The validator must not satisfy the R1 manifest requirement by finding `docs/AI_CONTEXT.md` somewhere else in the progress log.

### Mandatory adversarial test

The previous independent audit removed `docs/AI_CONTEXT.md` from §77.1 but retained it in §76.1.

The old validator incorrectly passed.

Create a negative fixture reproducing this exact defect. The strengthened validator must reject it.

## 7. Required correction D — Canonical identifier extraction

Use the canonical formula register as the authoritative source for the parameter-ID set.

Do not independently hard-code a partial list in different validator functions.

Implement or reuse one reliable extraction and comparison approach that:

- Reads the canonical registered parameter IDs.
- Establishes the expected set of 14 unique identifiers.
- Verifies the exact required identifier range.
- Compares acceptance and AI_CONTEXT references with that canonical set.
- Produces actionable error messages showing which IDs are missing, unexpected, or duplicated.

Avoid fragile substring checks that can pass on incomplete text.

If the documents use compact range notation rather than listing every ID individually, parse and validate that notation explicitly. A displayed range must represent the complete consecutive sequence, not merely mention its endpoints.

Do not silently normalize malformed source documents into passing results.

## 8. Required correction E — Adversarial mutation fixtures

Add fixtures using the project's established test conventions.

At minimum, include:

### Acceptance-document fixtures

1. Correct complete FP-P01–FP-P14 representation: PASS.
2. Range containing only FP-P01, FP-P02, and FP-P14: FAIL.
3. Missing FP-P13 while retaining FP-P14 and the 14-parameter claim: FAIL.
4. Missing FP-P14: FAIL.
5. Missing an intermediate parameter: FAIL.
6. Historical 12-parameter record in a historical section: must not cause a false failure.

### AI_CONTEXT fixtures

7. Correct complete 14-parameter representation: PASS.
8. FP-P13 removed while FP-P14 and the count of 14 remain: FAIL.
9. Parameter range ending at FP-P12: FAIL.
10. A missing intermediate parameter: FAIL.
11. Historical references to the earlier 12-parameter state remain valid.

### Manifest fixtures

12. AI_CONTEXT listed in §77.1: PASS.
13. AI_CONTEXT removed from §77.1 but retained in §76.1: FAIL.
14. AI_CONTEXT mentioned elsewhere but absent from §77.1: FAIL.
15. Malformed or empty R1 changed-file manifest: FAIL.
16. Correct historical C1 manifest remains valid.

The three previously reproduced bypasses must be explicit negative fixtures. Do not rely on an unrelated generic malformed-input test as a substitute.

### Mutation-test integrity

Where supported by the project's conventions:

- Perform mutations against temporary fixture copies or in-memory content.
- Do not corrupt the actual live project files as part of a test.
- Confirm that each negative fixture fails for the intended check, not because of an unrelated parser or setup error.
- Confirm that positive fixtures still pass.
- Preserve existing fixture coverage and test names where possible.
- Do not delete, weaken, skip, or relabel old tests to improve the totals.

## 9. Required correction F — Validator quality and diagnostics

For each strengthened check, provide useful diagnostic output.

Examples of the expected diagnostic meaning:

- Acceptance gate missing parameter FP-P13.
- AI_CONTEXT B-12 entry missing parameter FP-P13.
- R1 §77.1 manifest missing `docs/AI_CONTEXT.md`.
- R1 manifest check incorrectly satisfied only by a §76.1 entry.

The validator should make the failing document and relevant section clear.

Avoid:

- Whole-file searches that accidentally accept references from unrelated sections.
- Hard-coded assumptions that ignore the canonical register.
- Endpoint-only validation.
- Tests that only confirm a keyword exists.
- Catch-all exception handling that converts errors into successful checks.
- Pass results when files or sections are absent.

## 10. Required correction G — Status and progress documentation

Inspect the existing R1 completion statements in:

- `docs/AI_CONTEXT.md`
- The project progress log, especially §77.
- Any current Prompt 12B/C1/R1 status summary or roadmap reference.

Do not erase historical facts.

Before R2 actually passes its required checks, the project must not claim that validator closure is complete.

Once R2 passes all completion requirements:

1. Add a new R2 progress-log entry using the next appropriate section number.
2. Record the actual files changed.
3. Record the actual validator and fixture results.
4. Record the three adversarial cases and their demonstrated outcomes.
5. Update current project status references so they distinguish:
   - R1 documentation synchronization completed.
   - R2 validator completeness and adversarial tests completed.
6. Mark C1/R1/R2 closeout complete only to the extent demonstrated by evidence.
7. Preserve all previous historical progress entries.

If any mandatory check remains failing, keep the closeout status PARTIAL and explicitly record why.

Do not mark the work complete merely because the main validator has a passing total.

## 11. Prompt archival

Save the complete R2 instruction as a permanent project prompt using the existing prompt archive convention.

Suggested descriptive filename:

`docs/prompts/prompt_12B-C1-R2_validator_completeness.md`

Before using that exact filename, inspect the existing prompt index and naming rules.

Requirements:

- Archive the complete instruction.
- Update `docs/prompts/INDEX.md`.
- Update any required prompt inventory or roadmap entry.
- Verify the archived prompt and index are consistent.
- Do not overwrite the original Prompt 12B, C1, or R1 prompt files.
- Include the prompt's correct scope and authorization status.

## 12. Regression validation

Run all relevant validation after implementation.

At minimum:

1. Prompt 12B validator.
2. All Prompt 12B positive fixtures.
3. All Prompt 12B negative fixtures.
4. All new adversarial mutation fixtures.
5. Prompt 12A validator and fixtures.
6. Documentation link validator.
7. Final project validator.
8. Relevant formula-register checks.
9. Relevant integration-traceability checks.
10. Relevant project regression tests.
11. Validators affected by updates to the prompt archive/index, progress log, AI_CONTEXT, or roadmap.

Record the exact commands and actual results.

For each validator, report:
- Checks executed.
- Checks passed.
- Checks failed.
- Positive fixture count and result.
- Negative fixture count and result.
- Tests skipped or unavailable.

Do not claim execution of a test that was not run.

### Known legacy issue

Preserve the previously disclosed Prompt 11A validator issue:

`11A_validate_research.py` check 29 expects REQ-703, while the legitimate current global requirement frontier is REQ-869.

Do not weaken its validator or falsely claim the legacy issue is fixed as part of R2.

Record it accurately if the affected validator is rerun.

## 13. Preserve acceptance and governance

The current Prompt 12B acceptance tally is:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL/BLOCKED.

Preserve the three PARTIAL gates:

- `P12B-14`: audit-spine and tamper-evidence implementation is not verified.
- `P12B-16`: prototype database privilege and audit-protection defects remain.
- `P12B-23`: project-wide synchronization and legacy validator debt.

Do not convert PARTIAL gates into PASS because a documentation validator succeeds.

Preserve:

- Requirements REQ-764 through REQ-869.
- Decisions D-178 through D-187.
- Mirrored decisions DD-226 through DD-235.
- Unresolved UD-017 and UD-052 through UD-060.
- All existing owner-reserved and legal-dependent matters.
- The 16 formula identifiers and 14 parameter identifiers.
- All established B-system and INT contract identifiers.

Do not approve, defer, close, or reinterpret owner-reserved decisions without authorization.

## 14. Strict scope restrictions

This is a documentation, validator, testing, governance, and archival task only.

Do not:

- Begin Prompt 12C.
- Create Prompt 12C workflows, journeys, or acceptance specifications.
- Change gameplay behaviour.
- Implement production security controls.
- Create or modify production database migrations.
- Modify grants, RLS policies, triggers, or database permissions.
- Implement runtime audit-digest jobs or tamper-evidence mechanisms.
- Change approved architecture.
- Rewrite the B-12 specifications unnecessarily.
- Create a duplicate project or use an audit ZIP as a working project.
- Stage, commit, or push Git without explicit owner authorization.

Document unrelated findings separately rather than expanding scope.

## 15. Final delivery report

Provide a factual report with the following sections:

### A. Three reproduced defects

For each defect, identify:
- The original validator check.
- The mutation that reproduced the bypass.
- Why the old validator passed it.
- The corrective implementation.
- The new negative fixture.
- Evidence that the strengthened validator now rejects it.

### B. Parameter-range validation

Confirm that:
- The canonical register contains exactly 14 expected identifiers.
- P12B-19 is validated against the complete set.
- AI_CONTEXT is validated against the complete set.
- Missing, unexpected, duplicate, or discontinuous identifiers are detected.

### C. Manifest validation

Confirm that:
- The validator checks the actual R1 §77.1 section.
- An entry in §76.1 cannot satisfy the R1 requirement.
- The correct R1 manifest passes.
- The three manifest bypass fixtures behave as expected.

### D. Fixtures and mutation testing

List all new and existing fixture results, clearly distinguishing positive and negative tests.

### E. Files changed and archival

List all changed project files, the permanent R2 prompt path, index updates, and progress-log entry.

### F. Regression validation

Report exact commands, check totals, fixture results, failures, skipped tests, and the known 11A legacy issue.

### G. Governance and acceptance

Confirm preservation of all existing acceptance statuses and unresolved decisions.

### H. Scope confirmation

Explicitly confirm:
- Prompt 12C was not started.
- No production implementation or database security changes were made.
- No Git stage, commit, or push was performed.

### I. Final verdict

Select exactly one:

- **COMPLETE** — every R2 requirement is satisfied and independently reproducible by the project's tests.
- **PARTIAL** — one or more requirements remain incomplete, unsupported, or unverified.

Do not declare COMPLETE based solely on a passing validator total. The three adversarial bypasses must be demonstrably rejected.

## 16. Stop condition

After completing R2, stop and return the factual delivery report.

Do not begin Prompt 12C or any subsequent project phase without the owner's explicit authorization.

Leave the existing live project ready for the owner's next independent review.