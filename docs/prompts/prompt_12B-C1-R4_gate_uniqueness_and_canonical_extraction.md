# PROMPT 12B-C1-R4 — GATE UNIQUENESS, COMPLETE OCCURRENCE SCANNING, HISTORICAL-SECTION VALIDATION AND CANONICAL PARAMETER EXTRACTION

## 1. TASK AUTHORIZATION

You are authorized to execute this corrective task directly inside the existing live Nation Supremacy project directory.

This is a targeted validator-hardening and documentation-closeout task.

You MUST first read the complete:

`AUTONOMOUS_DECISION_POLICY.md`

Follow D-014 throughout this task.

Resolve ordinary technical matters autonomously. Do not repeatedly interrupt the owner for routine implementation decisions.

### Critical workspace instruction

Work exclusively in the existing live project folder.

The owner may independently create ZIP snapshots for external auditing. Such archives are not your working environment.

Do not:

- Extract or use an audit ZIP as your working project.
- Create duplicate project directories.
- Replace the live project with an archive.
- Overwrite unrelated work.
- Perform Git staging, committing or pushing.
- Begin Prompt 12C.

---

## 2. BACKGROUND

The previous corrective passes were:

- PROMPT 12B-C1.
- PROMPT 12B-C1-R1.
- PROMPT 12B-C1-R2.
- PROMPT 12B-C1-R3.

The latest independently audited snapshot was:

`Project X (73).zip`

R3 reported:

- 82/82 validator checks.
- 33/33 positive fixtures.
- 59/59 negative fixtures.

However, independent mutation testing revealed seven additional validator bypasses.

Your task is to eliminate these bypasses without weakening any previous protections.

---

## 3. MANDATORY SEVEN DEFECTS TO FIX

### DEFECT 1 — Duplicate complete P12B-19 rows

Current problem:

The validator uses first-match selection when locating the P12B-19 acceptance row.

A second complete P12B-19 row can therefore be inserted without triggering failure.

Required correction:

- Parse every P12B-19 row.
- Require exactly one current authoritative P12B-19 row.
- Reject duplicate rows even when they are byte-for-byte identical.
- Reject conflicting duplicate rows.
- Reject malformed duplicate identifiers.
- Do not silently choose the first or last row.

### DEFECT 2 — Unexpected parameter IDs outside the expected comma chain

Current problem:

The acceptance gate can contain an unexpected parameter identifier after a semicolon without detection.

Example:

A valid FP-P01–FP-P14 representation followed by `FP-P15`.

Required correction:

- Scan the entire relevant current-state gate content.
- Extract every parameter identifier occurrence.
- Compare the complete extracted occurrence sequence with the canonical expected representation.
- Reject unexpected identifiers.
- Reject duplicate identifiers.
- Reject missing identifiers.
- Reject out-of-order identifiers.
- Reject malformed representations.

Do not restrict validation to a single expected formatting pattern.

### DEFECT 3 — Duplicate parameter IDs outside the expected chain

Current problem:

An additional FP-P01 can be inserted after a semicolon and escape duplicate detection.

Required correction:

- Count all parameter identifier occurrences across the relevant representation.
- Detect duplicate occurrences regardless of punctuation or separators.
- Detect duplicates in the same row, adjacent clauses and additional sentences.
- Do not use set conversion before checking occurrence counts.

### DEFECT 4 — Stale formula claims inside acceptance §2.1

Current problem:

The current implementation excludes the entire §2.1 reassessment section from stale-reference scanning.

This creates a blind spot.

Required correction:

- Review the exact purpose of the exclusion.
- Preserve legitimate historical commentary.
- Do not exempt an entire section from validation.
- Distinguish historical references from current-state assertions.
- Reject stale formula-register ranges when represented as current claims inside §2.1.
- Preserve legitimate historical references with explicit historical context.

Historical information must not be mistaken for current authoritative information.

### DEFECT 5 — Unformatted stale parameter ranges

Current problem:

The scanner misses ranges without backticks.

Example:

`Current formula-register range: FP-P01-FP-P12`

Required correction:

- Detect parameter identifiers in both formatted and unformatted text.
- Detect common range representations.
- Detect hyphenated, en-dash and em-dash forms.
- Detect individual IDs and comma-separated representations.
- Detect stale current-state claims even if formatting conventions are violated.
- Avoid false positives on clearly identified historical records.

### DEFECT 6 — Unexpected parameter IDs in AI_CONTEXT outside the structured chain

Current problem:

An unexpected FP-P15 can be appended outside the expected structured parameter chain in AI_CONTEXT.

Required correction:

- Scan the entire relevant current B-12 AI_CONTEXT entry.
- Extract every FP-P identifier occurrence.
- Compare the extracted identifiers with the canonical formula-register identifiers.
- Reject unexpected identifiers.
- Reject missing identifiers.
- Reject duplicates.
- Reject inconsistent current-state representations.

Do not validate only the first recognized structured chain.

### DEFECT 7 — Duplicate parameter IDs in AI_CONTEXT outside the structured chain

Current problem:

An additional FP-P01 can be added outside the expected chain without detection.

Required correction:

- Count every occurrence across the entire relevant current-state representation.
- Reject duplicate occurrences.
- Ensure that structured and unstructured representations cannot bypass duplicate checks.
- Preserve legitimate historical references where explicitly marked and justified.

---

## 4. CANONICAL PARAMETER EXTRACTION — CRITICAL ARCHITECTURAL CORRECTION

The existing validator contains a hard-coded parameter expectation similar to:

`EXPECTED_PARAMS = [f"FP-P{n:02d}" for n in range(1, 15)]`

This is not acceptable as the ultimate source of truth.

The canonical formula register must supply the authoritative parameter identifiers.

File:

`docs/stage-2/20_fair_play_and_player_protection_formula_register.md`

Required implementation:

1. Extract parameter definitions from the actual canonical formula register.
2. Validate the extracted identifiers for uniqueness.
3. Validate identifier format.
4. Validate the expected count against the actual extracted records.
5. Build the authoritative ordered parameter collection dynamically.
6. Derive the expected identifier set from that collection.
7. Use this canonical collection for all downstream comparisons.
8. Compare acceptance and AI_CONTEXT representations against the same extracted source.
9. Reject malformed or duplicated canonical parameter definitions.
10. Ensure a missing or unreadable canonical register causes a validation failure rather than silently falling back to hard-coded IDs.

Hard-coded fixture expectations may remain inside explicitly isolated test fixtures when useful, but they must not replace the canonical source during normal validation.

Do not merely introduce another hard-coded list in a different function.

The source-of-truth relationship must be genuine.

---

## 5. COMPLETE OCCURRENCE SCANNING

Review the existing parsing and validation architecture.

In particular, inspect:

- `Model.rebuild()`
- `param_representation()`
- `acceptance_stale_problems()`
- `check_77()`
- `check_78()`
- Related parsing helpers.
- Existing historical-reference handling.

Implement reusable parsing helpers rather than duplicating fragile regular expressions.

The scanner must distinguish:

- Current authoritative claims.
- Historical claims.
- Explicitly superseded claims.
- Explanatory references.
- Canonical register definitions.

Do not ignore malformed text simply because it does not follow the expected formatting convention.

Do not allow extra identifiers to disappear during extraction.

Do not use first-match selection where the requirement is uniqueness.

Do not convert occurrence lists to sets before duplicate validation.

---

## 6. ADVERSARIAL MUTATION FIXTURES

Add permanent adversarial fixtures covering every reproduced defect.

At minimum, implement these seven fixtures:

| Fixture | Mutation | Expected |
|---|---|---|
| R4-01 | Duplicate complete P12B-19 row | REJECT |
| R4-02 | Unexpected FP-P15 after semicolon in gate row | REJECT |
| R4-03 | Duplicate FP-P01 after semicolon in gate row | REJECT |
| R4-04 | Stale current-state range inside §2.1 | REJECT |
| R4-05 | Unformatted stale FP-P01-FP-P12 range | REJECT |
| R4-06 | Unexpected FP-P15 outside AI_CONTEXT structured chain | REJECT |
| R4-07 | Duplicate FP-P01 outside AI_CONTEXT structured chain | REJECT |

Add further tests for:

- Missing parameter identifiers.
- Reordered identifiers.
- Duplicate canonical parameter definitions.
- Malformed parameter IDs.
- Duplicate gate identifiers.
- Multiple conflicting current-state entries.
- Historical references that should remain valid.
- Legitimate explanatory mentions.
- Missing formula register.
- Empty extracted parameter collection.
- Extra parameters in the canonical register.
- Changed canonical parameter count.
- Unicode dash variations.
- Multiple representations in one document.

### Fixture quality requirements

A negative fixture passes only when the validator rejects the mutated input for the intended reason.

A crash or unrelated exception does not count as a successful rejection.

Positive fixtures must prove that legitimate historical and explanatory references continue to work.

Never modify the baseline source documents merely to make a fixture pass.

---

## 7. REGRESSION PROTECTION

Preserve every existing R1, R2 and R3 validation capability.

Do not remove:

- Duplicate-ID checks.
- Stale-reference checks.
- Formula range checks.
- Manifest validation.
- Prompt archival validation.
- AI_CONTEXT synchronization.
- Historical parameter safeguards.
- Existing positive fixtures.
- Existing negative fixtures.

Run the previous R3 fixture suite unchanged before and after the R4 modifications.

Any regression must be investigated and corrected.

Do not reduce the number of existing checks or fixtures merely to achieve a passing result.

---

## 8. DOCUMENTATION AND PROJECT SYNCHRONIZATION

Preserve the four authoritative Prompt 12B specifications.

Do not rewrite their completed substantive content.

Preserve:

- 344 normative rules.
- 106 requirements.
- REQ-764 through REQ-869.
- 16 formulas.
- 12 numerical parameters.
- D-178 through D-187.
- DD-226 through DD-235.
- All owner-reserved decisions.
- All legal-dependent unresolved decisions.

Preserve Prompt 12B acceptance:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL.
- 0 BLOCKED.

The three PARTIAL gates must remain:

- P12B-14.
- P12B-16.
- P12B-23.

Update only documentation genuinely affected by R4.

Review relevant:

- `docs/PROJECT_PROGRESS.md`
- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/ROADMAP.md`
- `docs/stage-2/00_stage_2_handoff.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/prompts/INDEX.md`
- Change manifests and relevant validator documentation.

Create a permanent prompt archive following the established naming convention:

`docs/prompts/prompt_12B-C1-R4_...md`

Preserve the complete R4 instruction.

Update the prompt index with the exact path.

Do not create duplicate prompt files.

Update the project handoff so the next independent auditor knows to audit the resulting ZIP against the complete R4 instruction supplied separately.

---

## 9. VALIDATION REQUIREMENTS

Run:

1. The complete Prompt 12B validator.
2. All positive fixtures.
3. All negative fixtures.
4. All seven new R4 fixtures.
5. All R1–R3 regression fixtures.
6. Prompt 12A validation.
7. Relevant project-wide validators.
8. Relevant unit tests.
9. Documentation link validation.
10. Final project validation.

Report actual commands, exit codes and outputs.

Do not claim tests were executed when they were not.

Do not report a test suite as passing if it timed out or did not complete.

Do not weaken any existing validator to achieve success.

---

## 10. ACCEPTANCE CRITERIA

R4 is complete only when all of the following are satisfied.

### A. Seven reproduced defects

All seven mutations are rejected for the correct reason.

### B. Canonical extraction

The expected parameter identifiers are derived from the canonical formula register, not a hard-coded production expectation.

### C. Occurrence completeness

No duplicate, missing, unexpected or reordered identifier can bypass scanning through alternate punctuation or additional text.

### D. Historical-reference safety

Legitimate historical references remain valid, but stale current-state claims are rejected even inside previously excluded sections.

### E. Regression

All existing R1–R3 protections continue to pass.

### F. Documentation

The complete R4 prompt is permanently archived and indexed.

Relevant project-status documentation is synchronized.

### G. Independent audit readiness

The project contains enough evidence for an external auditor to reproduce all relevant results.

Do not mark R4 complete merely because the validator reports a passing total.

---

## 11. STRICT SCOPE LIMITATIONS

This task is exclusively validator hardening, adversarial testing and documentation synchronization.

DO NOT:

- Begin Prompt 12C.
- Create Prompt 12C deliverables.
- Rewrite completed Prompt 12B specifications.
- Approve provisional requirements.
- Close owner-reserved decisions.
- Resolve legal-dependent questions without authorization.
- Implement production security controls.
- Create Supabase migration 0005.
- Claim audit tamper-evidence is implemented.
- Change unrelated game architecture.
- Stage, commit or push Git changes.

The outstanding Supabase and audit-log security obligations must remain documented.

---

## 12. FINAL REPORT

At completion, provide:

1. Exact files created or modified.
2. Exact permanent R4 prompt archive path.
3. Autonomous policy reading attestation, if actually read.
4. Seven defect-by-defect correction results.
5. Canonical parameter extraction implementation details.
6. Positive fixture results.
7. Negative fixture results.
8. R1–R3 regression results.
9. Project-wide validator results.
10. Test results and incomplete tests.
11. Documentation synchronization results.
12. Remaining unresolved issues.
13. Git status without making Git changes.
14. Explicit statement that Prompt 12C has not started.

Use honest PASS, PARTIAL, FAIL and BLOCKED statuses.

Do not fabricate results or claim independent approval.

---

## 13. STOP CONDITION

After completing R4:

STOP.

Do not begin Prompt 12C.

The owner will create a fresh ZIP snapshot and submit it with the complete R4 prompt to an independent auditor.

The independent auditor will inspect the ZIP and verify compliance against that exact R4 instruction.

Wait for further owner authorization.

**Guiding principle: Fix the actual validator weaknesses, preserve all previous protections, and make the canonical register—not hard-coded assumptions—the source of truth.**