# PROMPT 12B-C1-R1 — FINAL DOCUMENTATION SYNCHRONIZATION AND VALIDATOR CLOSURE

## 1. Mission

Complete the remaining documentation and validator corrections identified during the independent audit of Prompt 12B-C1.

This is a **targeted closeout correction**, not a rewrite of Prompt 12B or Prompt 12B-C1.

You are working directly in the existing, live Nation Supremacy project directory. Make all changes in that existing project. Do not create a duplicate project directory, extract or use an audit ZIP as a working project, replace the live project with an archive, or overwrite unrelated work.

Your objective is to eliminate the remaining inconsistencies concerning the 14 registered formula parameters, correct the autonomous-policy reading attestation's line-count discrepancy, synchronize the change manifest, and strengthen the validator so these defects cannot pass unnoticed again.

## 2. Mandatory governance

Before making changes:

1. Read the complete `AUTONOMOUS_DECISION_POLICY.md` from the existing live project. Do not rely on a summary or selected sections.
2. Follow D-014 and all applicable approved project governance.
3. Inspect the current versions of every affected file before editing. Do not assume the previously audited line numbers are unchanged.
4. Inspect the existing prompt archive, prompt index, validator conventions, fixture conventions, progress log, and project-wide context files.
5. Record only work actually performed during this task. Do not backdate attestations, claim historical actions that cannot be verified, or invent test results.

Resolve ordinary documentation and validator details autonomously, using existing project conventions. Do not reopen settled architecture or owner-reserved decisions.

## 3. Required correction A — Acceptance document parameter counts

File:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

Inspect the complete document and correct the remaining stale references identified in the audit.

At minimum:

- Gate `P12B-19` must refer to the complete registered parameter range `FP-P01` through `FP-P14`, not merely `FP-P12`.
- The validator specification in §9.1 must state that the formula register contains **14 parameters**, not 12.
- Check the document's other current-state descriptions, matrices, summaries, and acceptance evidence for the same inconsistency.
- Ensure all current-state descriptions agree with the canonical formula register.

Do not change the approved meaning or scope of any acceptance gate merely to update the parameter count.

The current registered parameters are `FP-P01` through `FP-P14`. Verify this against the actual canonical formula register before editing.

## 4. Required correction B — AI_CONTEXT synchronization

File:

`docs/AI_CONTEXT.md`

Find the current B-12 formula-register summary. It currently reports 12 parameters and must be synchronized.

Update it to accurately report:

- 14 registered parameters.
- The complete range `FP-P01` through `FP-P14`.
- The existence of the two additional registered parameters FP-P13 and FP-P14.
- The current formula-register location and status, consistent with the canonical register.

Inspect the surrounding B-12 context for any other stale current-state references caused by the C1 additions.

Do not broadly rewrite `AI_CONTEXT.md`. Preserve unrelated project context and all established terminology.

## 5. Required correction C — Autonomous-policy reading attestation

Inspect:

- `AUTONOMOUS_DECISION_POLICY.md`
- The Prompt 12B-C1 entry in the project's progress log, particularly §76.
- The existing reading attestation and its stated line count.

The previous audit found that the attestation reports 122 lines, while the policy file in the audited snapshot contains 121 lines.

Resolve this discrepancy using the actual policy file in the live project.

Requirements:

1. Calculate the current file's line count using a clearly stated, reproducible method.
2. Correct the inaccurate line-count reference in the attestation.
3. Ensure the attestation identifies the correct policy path and actual reading date.
4. Do not backdate, invent, or alter the historical date of reading.
5. Do not claim the policy was read again unless you actually read it completely during this task.
6. If the policy has changed since the earlier attestation, distinguish the earlier reading from the current full reading and identify the applicable version or date.

The attestation must remain truthful and auditable.

## 6. Required correction D — C1 change manifest

Inspect the Prompt 12B-C1 closeout entry, particularly §76.1 of the progress log.

After updating `docs/AI_CONTEXT.md`, add it to the C1 changed-file manifest.

Verify that the manifest accurately identifies all files actually changed by Prompt 12B-C1 and this corrective task, following the project's existing manifest conventions.

Do not claim files were changed if they were not. Do not silently omit a changed file.

If the project distinguishes the original C1 changes from R1 follow-up corrections, preserve that distinction rather than rewriting historical records.

## 7. Required correction E — Strengthen the Prompt 12B validator

Find and inspect the existing Prompt 12B validator and its positive/negative fixture structure.

Extend the existing validator using established project conventions. Do not create a competing validator or weaken existing checks.

The validator must detect the following cross-document inconsistencies:

### E1. Canonical parameter-register verification

- Confirm that the canonical formula register contains exactly the expected 14 registered parameters.
- Confirm that the identifiers are `FP-P01` through `FP-P14`.
- Confirm that FP-P13 and FP-P14 are present and correctly represented.
- Detect missing, duplicate, or unexpected parameter identifiers.

### E2. Acceptance-document synchronization

- Confirm that gate `P12B-19` covers all 14 registered parameters.
- Confirm that acceptance §9.1 reports 14 registered parameters.
- Detect a stale current-state reference that reports only 12 parameters or ends the parameter range at FP-P12.

### E3. AI_CONTEXT synchronization

- Confirm that the current B-12 formula-register entry in `docs/AI_CONTEXT.md` reports 14 parameters.
- Confirm that its parameter range includes FP-P01 through FP-P14.
- Detect a stale current-state count of 12 or a range ending at FP-P12.

### E4. Attestation and manifest verification

- Check that the current C1 reading attestation identifies the correct policy path and a reproducible line count.
- Check that the C1/R1 change manifest includes `docs/AI_CONTEXT.md` if this task changes it.
- Do not hard-code a historical line count that will become invalid after legitimate future policy edits. Prefer a reproducible comparison or a clearly identified version-specific attestation.

### E5. Historical-record protection

Important: historical progress entries may legitimately mention that the register previously contained 12 parameters.

Do not implement a simplistic project-wide ban on the number 12 or on `FP-P01`–`FP-P12`.

The validator must distinguish:
- Current-state claims, which must reflect 14 parameters.
- Historical records, which must retain accurate historical counts.
- Other unrelated uses of the number 12.

A valid historical statement must not fail merely because it records the earlier state.

### E6. Fixtures

Add or update fixtures to demonstrate that:

- The correct 14-parameter current state passes.
- A current-state acceptance claim of 12 parameters fails.
- A current-state parameter range ending at FP-P12 fails.
- An AI_CONTEXT entry that still reports 12 parameters fails.
- A missing FP-P13 or FP-P14 fails.
- A duplicate parameter identifier fails.
- A historically accurate record of the earlier 12-parameter state is not incorrectly rejected.
- Incorrect attestation metadata is detected where covered by the validator.

Run all positive and negative fixtures. Report actual results.

Do not weaken, delete, bypass, or relabel existing checks or fixtures to achieve a pass.

## 8. Cross-document consistency review

After making the corrections, compare the following documents directly:

1. `docs/stage-2/20_fair_play_and_player_protection.md`
2. `docs/stage-2/20_fair_play_and_player_protection_requirements.md`
3. `docs/stage-2/20_fair_play_and_player_protection_formula_register.md`
4. `docs/stage-2/20_fair_play_and_player_protection_acceptance.md`
5. `docs/AI_CONTEXT.md`
6. The Prompt 12B-C1/R1 progress-log entries.
7. The Prompt 12B validator and its fixtures.
8. The prompt archive and its index.

Confirm that the same current-state facts are reported consistently, especially:

- 16 registered formulas.
- 14 registered parameters, FP-P01 through FP-P14.
- Correct F-FP-002 and F-FP-014 specifications.
- Correct prior-violation treatment across F-FP-001 and F-FP-011.
- Correct integration mapping and the 20 dependency contracts.
- Existing requirements allocation and decision references.
- The three existing Prompt 12B PARTIAL acceptance gates.
- Prompt 12C remains unstarted and unauthorized.

Do not change previously approved formulas, integration IDs, requirement IDs, decisions, or acceptance meanings as part of this synchronization task.

## 9. Preserve acceptance and unresolved matters

Preserve the existing Prompt 12B acceptance result unless new, direct evidence justifies a change.

The current documented result is:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL/BLOCKED.

The three PARTIAL gates must remain appropriately disclosed:

- `P12B-14`: audit-spine and tamper-evidence implementation is not verified.
- `P12B-16`: prototype database privilege and audit-protection defects remain.
- `P12B-23`: project-wide synchronization and legacy validator debt.

Do not convert a PARTIAL gate to PASS merely because its specification or validator passes.

Preserve the unresolved owner/legal decisions, including UD-017 and UD-052 through UD-060. Do not silently approve or close them.

Preserve the existing requirements allocation, including REQ-764 through REQ-869, and the established decision identifiers D-178 through D-187 and DD-226 through DD-235.

Preserve the known Prompt 11A legacy validator issue: check 29 still expects REQ-703 even though the legitimate current requirement frontier is REQ-869. Do not weaken the validator or misreport this known issue as resolved.

## 10. Prompt archival

Treat this corrective prompt as a separate permanent project prompt, following the existing prompt-file naming and archival conventions.

- Save its complete text in the appropriate existing `docs/prompts/` location.
- Use the next appropriate unique prompt identifier and a descriptive filename.
- Update `docs/prompts/INDEX.md` and any required prompt inventory or roadmap references.
- Record its scope accurately as a targeted Prompt 12B-C1 closeout correction.
- Do not overwrite the original Prompt 12B or Prompt 12B-C1 prompt archives.

## 11. Regression validation

After all changes, run the relevant validators and tests available in the live project.

At minimum:

1. Prompt 12B validator and all its positive/negative fixtures.
2. Prompt 12A validator and fixtures.
3. Documentation link validator.
4. Final project validator.
5. Relevant formula-register and integration-traceability checks.
6. Relevant project regression tests.
7. Any validator specifically affected by the changed prompt archive, prompt index, AI_CONTEXT, or progress log.

Report exact command names, actual check totals, positive-fixture counts, negative-fixture counts, failures, and skipped tests.

Do not report a validator as passing if it was not executed.

Do not claim runtime, database, security, production, or deployed-system verification from documentation-only tests.

## 12. Strict scope restrictions

This task is documentation, governance, archival, and validator maintenance only.

Do not:

- Implement Prompt 12C.
- Create Prompt 12C journeys, workflows, or acceptance specifications.
- Make production game changes.
- Add or modify production database migrations.
- Modify RLS policies, grants, triggers, or database permissions.
- Implement audit-digest jobs or runtime tamper-evidence mechanisms.
- Change gameplay behaviour.
- Change approved architecture or owner-reserved decisions.
- Rewrite the four B-12 specification documents unnecessarily.
- Create duplicate project directories or use an audit ZIP as a working project.
- Stage, commit, or push Git changes without explicit owner authorization.

If you discover an unrelated defect, document it separately. Do not silently expand this task.

## 13. Final delivery report

When finished, provide a factual report containing:

### A. Corrections completed
List each corrected file and the exact inconsistency resolved.

### B. Parameter synchronization
Confirm that the formula register, acceptance document, validator, and AI_CONTEXT consistently reflect the 14 registered parameters.

### C. Attestation
State the policy path, actual line-count method, verified line count, reading date, and any version distinction.

### D. Change manifest and archival
Provide the corrective prompt's permanent path, prompt-index update, and synchronized changed-file manifest.

### E. Validator improvements
List new checks, positive fixtures, negative fixtures, and historical-record protection.

### F. Validation results
Provide actual commands and results, including any failure, skipped check, or known legacy issue.

### G. Acceptance and governance
Report the final gate tally and confirm that unresolved owner decisions and the three PARTIAL gates remain preserved.

### H. Remaining issues
List any unresolved issue honestly, with file path and evidence.

### I. Scope confirmation
Explicitly confirm that no Prompt 12C work, production implementation, database security changes, or Git stage/commit/push actions were performed.

## 14. Completion standard

Do not declare Prompt 12B-C1-R1 complete merely because files were edited.

It is complete only when:

- All identified current-state parameter references are synchronized.
- The reading attestation is accurate and reproducible.
- The change manifest reflects the actual changed files.
- The validator detects the identified stale-reference defects.
- Positive and negative fixtures demonstrate the expected behaviour.
- Relevant regression validation has been executed and reported.
- Governance, unresolved decisions, and acceptance statuses remain intact.

After completing this targeted correction, stop. Do not begin Prompt 12C. Return the factual delivery report and leave the existing live project ready for the owner's next independent review.