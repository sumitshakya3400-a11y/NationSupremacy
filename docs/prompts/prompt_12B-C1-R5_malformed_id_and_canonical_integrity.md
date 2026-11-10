# PROMPT 12B-C1-R5 — MALFORMED IDENTIFIER DETECTION, COMPLETE CURRENT-STATE SCANNING, CANONICAL DEFINITION INTEGRITY AND GATE REGISTER HARDENING

## 1. TASK AUTHORIZATION

You are authorized to execute this corrective task directly inside the existing live Nation Supremacy project directory.

This is a targeted validator-hardening, adversarial-testing and documentation-synchronization task.

You MUST first read the complete:

`AUTONOMOUS_DECISION_POLICY.md`

Follow D-014 throughout the task.

Resolve ordinary technical and documentation questions autonomously. Preserve approved decisions, identifiers, historical specifications and established project architecture.

### Critical workspace instruction

Work exclusively in the existing live Nation Supremacy project folder.

The latest independent audit snapshot is:

`Project X (74).zip`

This ZIP is an audit artifact, not your working project.

Do not:

- Extract or use an audit ZIP as your working project.
- Create duplicate project directories.
- Replace the live project with an archive.
- Overwrite unrelated work.
- Perform Git staging, committing or pushing.
- Begin Prompt 12C.

---

## 2. BACKGROUND AND PREVIOUS CORRECTIVE WORK

The completed corrective sequence is:

- PROMPT 12B-C1.
- PROMPT 12B-C1-R1.
- PROMPT 12B-C1-R2.
- PROMPT 12B-C1-R3.
- PROMPT 12B-C1-R4.

R4 attempted to resolve seven validator bypasses discovered during the Project X (73) audit.

The Project X (74) archive reports:

- 82/82 validator checks.
- 33/33 positive fixtures.
- 73/73 negative fixtures.

Independent verification confirmed that the seven exact R4 fixtures reject their specified mutations.

However, further adversarial testing exposed additional bypasses.

**R4 is not independently accepted.**

Your task is to resolve every finding in this prompt without weakening any R1–R4 protection.

---

## 3. INDEPENDENTLY REPRODUCED DEFECTS

The following defects were reproduced against Project X (74).

You MUST independently reproduce each finding against the corresponding live-project validator before implementing the correction.

Do not assume the audit description alone establishes the exact code path.

### DEFECT 1 — MALFORMED PARAMETER IDENTIFIERS IN THE ACCEPTANCE GATE

The P12B-19 row accepts malformed parameter-like tokens outside the correctly formatted expected chain.

Reproduced mutation:

Append:

`FP-PXX`

after an otherwise correct FP-P01–FP-P14 chain.

Observed result:

The complete validator still passes.

Required correction:

- Detect malformed parameter-like identifiers.
- Detect tokens that begin with the FP-P identifier namespace but do not satisfy its canonical identifier format.
- Reject FP-PXX.
- Reject FP-P1, FP-P001 and FP-P01X where these do not correspond to valid canonical identifiers.
- Reject unexpected valid-looking identifiers such as FP-P15.
- Reject malformed parameter tokens regardless of punctuation or formatting.
- Scan the complete current-state P12B-19 representation.
- Do not allow malformed identifiers to disappear during parsing.
- Produce a specific validation diagnostic.

Do not hard-code the number of permitted parameter identifiers.

The canonical formula register remains authoritative.

### DEFECT 2 — STALE INDIVIDUAL PARAMETER CLAIMS IN ACCEPTANCE

The acceptance validator fails to detect some stale current-state claims containing individual parameter identifiers.

Reproduced mutation:

`Current formula-register identifiers: FP-P01, FP-P12.`

The validator accepts this stale claim.

The following variations must also be detected:

- Comma-separated stale identifiers.
- Backtick-formatted individual identifiers.
- Individual identifiers appearing in additional sentences.
- Partial parameter lists.
- Multiple parameter representations in one section.
- Stale identifiers represented outside the expected parameter-chain format.

Required correction:

- Scan the complete relevant acceptance document.
- Extract individual parameter occurrences.
- Identify their contextual meaning.
- Compare current authoritative parameter claims against the canonical parameter collection.
- Reject stale, incomplete or conflicting current-state representations.
- Do not restrict validation to ranges or one structured parameter chain.

### DEFECT 3 — CANONICAL REGISTER DUPLICATE-DEFINITION FORMATTING BYPASS

The canonical parser does not reliably detect duplicate definitions when formatting conventions are violated.

Reproduced mutation:

Add a duplicate FP-P14 definition without the expected backtick formatting.

Observed result:

The additional definition is ignored and the validator passes.

Required correction:

- Detect canonical parameter-definition candidates independently of optional Markdown formatting.
- Detect definitions in tables and ordinary text.
- Detect duplicate definition identifiers regardless of formatting.
- Reject duplicate canonical definitions.
- Reject malformed canonical identifiers.
- Reject conflicting definitions of the same identifier.
- Detect unexpected additional definitions.
- Reject missing definitions.
- Preserve legitimate explanatory references that are not definitions.

Do not solve this by blindly treating every mention of an identifier as a definition.

Implement a reliable distinction between a canonical definition, an explanatory mention and a historical reference.

The canonical formula register must not contain ambiguous authoritative definitions.

### DEFECT 4 — HISTORICAL LABEL BYPASS

The current historical-reference handling is too permissive.

Reproduced mutation:

`Historical note: the formula register now contains only FP-P01–FP-P12.`

The validator accepts this statement even though it describes a current-state assertion using historical wording.

Required correction:

- Do not classify an entire sentence as legitimate historical content merely because it contains the word `historical`.
- Evaluate the actual assertion.
- Distinguish genuinely past facts from statements describing the present state.
- Detect current-state language inside sentences containing historical terminology.
- Reject stale current-state claims even when a historical qualifier appears elsewhere in the sentence.
- Preserve explicitly dated and genuinely historical records.
- Preserve legitimate explanations of former parameter arrangements when they are clearly identified as superseded.

Historical classification must be based on the meaning and structure of the assertion, not a single keyword.

### DEFECT 5 — AI_CONTEXT INVENTORY SCANNING IS TOO NARROW

The validator currently concentrates on the row containing the formula-register filename.

Reproduced mutation:

Add an additional unexpected parameter assertion elsewhere in the current B-12 Fair Play inventory entry.

Observed result:

The validator accepts the unexpected parameter.

Required correction:

- Locate the complete current B-12 AI_CONTEXT entry.
- Scan its complete relevant content, including paragraphs, table rows, additional sentences and continuation text.
- Extract every parameter-like identifier occurrence.
- Detect malformed, duplicated, unexpected, missing and conflicting representations.
- Validate the complete current-state representation against the canonical formula register.
- Preserve explicitly justified historical references.
- Do not validate only the filename-bearing row.
- Do not ignore text outside the first recognized parameter chain.

There must be one unambiguous authoritative current B-12 formula-register representation.

### DEFECT 6 — MALFORMED DUPLICATE GATE IDENTIFIER

The gate-register parser fails to detect malformed identifiers that duplicate an existing gate identifier with an appended suffix.

Reproduced mutation:

Add:

`P12B-19X`

as an additional gate-like row while retaining the existing P12B-19 row.

Observed result:

The validator ignores the malformed duplicate.

Required correction:

- Detect gate identifier candidates independently of whether their suffix matches the expected exact format.
- Validate the format of every gate-like identifier in the authoritative acceptance gate register.
- Reject malformed identifiers that resemble existing authoritative gate identifiers.
- Reject duplicate exact identifiers.
- Reject conflicting duplicates.
- Scan the complete authoritative gate register.
- Do not silently ignore malformed gate identifiers.
- Retain existing legitimate references to gate identifiers in explanatory and historical prose.

All authoritative gate identifiers must be unique and correctly formatted.

### DEFECT 7 — HARD-CODED PARAMETER COUNT IN CHECK 45

The validator still contains a hard-coded parameter-count assertion of 14 in `check_45()`.

This is inconsistent with the R4 requirement that the canonical formula register provide the ultimate parameter source of truth.

Required correction:

- Inspect the actual purpose of `check_45()`.
- Determine whether it verifies the formula-register parameter collection or a separate Prompt 12B specification metric.
- Where it validates the canonical FP-P collection, derive the expected count dynamically from the extracted canonical parameter records.
- Where a declared count exists in the canonical register, validate that declaration against the actual extracted definition records.
- Do not retain an independent hard-coded production expectation of 14.
- Do not introduce another hard-coded list or count in a different function.
- Do not silently change the separate documented Prompt 12B metric of 12 numerical parameters.
- Preserve the distinction between the canonical FP-P identifier collection and other numerical-parameter metrics unless the actual source documentation establishes that they refer to the same collection.

A changed canonical parameter count must be detected and handled through source-derived validation.

---

## 4. CANONICAL PARAMETER REGISTER — SOURCE-OF-TRUTH ENFORCEMENT

Canonical file:

`docs/stage-2/20_fair_play_and_player_protection_formula_register.md`

The canonical register must remain the single authoritative production source for the FP-P parameter identifier collection.

Review and strengthen:

- `Model.rebuild()`
- `Model.param_raw`
- `canonical_params()`
- `param_representation()`
- `scan_param_occurrences()`
- `compare_param_occurrences()`
- `acceptance_stale_problems()`
- `check_45()`
- `check_76()`
- `check_77()`
- `check_78()`
- All related parsing and historical-reference helpers.

Mandatory requirements:

1. Extract every actual canonical parameter definition.
2. Detect definitions regardless of optional Markdown backticks.
3. Validate exact identifier syntax.
4. Validate uniqueness before constructing lookup sets.
5. Validate that definitions are unambiguous.
6. Validate the actual extracted collection against any declared canonical count.
7. Reject an unreadable or missing register.
8. Reject an empty extracted collection.
9. Reject malformed definitions.
10. Reject duplicate definitions.
11. Reject unexpected definitions where their addition conflicts with the authoritative register's declared structure.
12. Build one ordered canonical collection dynamically.
13. Derive downstream expected identifiers from this collection.
14. Use the same canonical collection in acceptance and AI_CONTEXT comparisons.
15. Do not use a hard-coded identifier count as an alternative source of truth.
16. Do not silently fall back to the old hard-coded list.

Hard-coded expectations may remain inside isolated test fixtures where appropriate.

They must not replace the canonical source during production validation.

### Important parsing principle

Preserve occurrence information until duplicate validation is complete.

Do not convert extracted identifiers into a set before checking:

- Duplicate counts.
- Occurrence order.
- Missing identifiers.
- Unexpected identifiers.
- Malformed tokens.

---

## 5. COMPLETE CURRENT-STATE SCANNING

The validator must distinguish between:

1. Current authoritative claims.
2. Historical claims.
3. Explicitly superseded claims.
4. Explanatory references.
5. Canonical register definitions.
6. Malformed or ambiguous claims.

Implement reusable scanning and classification helpers.

Do not duplicate fragile regular expressions across individual checks.

### Current-state scanning obligations

For the acceptance document:

- Scan the complete relevant current-state content.
- Include §2.1.
- Include P12B-19.
- Include other current acceptance representations where applicable.
- Detect individual IDs, ranges and comma-separated lists.
- Detect unformatted representations.
- Detect additional parameter assertions in adjacent clauses and sentences.

For AI_CONTEXT:

- Scan the complete current B-12 entry.
- Include its associated text and inventory content.
- Detect additional parameter assertions outside structured chains.
- Detect conflicting current representations.

For the canonical register:

- Inspect every actual definition.
- Detect duplicate and malformed definitions.
- Preserve legitimate explanatory mentions.

For the gate register:

- Inspect every authoritative gate identifier.
- Detect duplicate, malformed and ambiguous identifiers.

### Historical-reference protection

Create fixtures proving that all of the following behave correctly:

- A clearly dated historical parameter range is accepted when it is genuinely historical.
- An explicitly superseded historical representation is accepted where properly contextualized.
- A historical explanation containing an old identifier remains accepted.
- A stale range asserted as current is rejected.
- A stale range cannot bypass validation merely by adding the word `historical`.
- A sentence containing both a historical reference and a current-state assertion is evaluated correctly.
- Explanatory mentions are not incorrectly treated as authoritative definitions or current-state claims.

Do not remove historical safeguards merely to increase negative-fixture results.

---

## 6. PERMANENT R5 ADVERSARIAL FIXTURES

Add permanent, independently meaningful fixtures for every reproduced defect.

At minimum:

| Fixture | Mutation | Expected |
|---|---|---|
| R5-01 | Append FP-PXX to the gate representation | REJECT |
| R5-02 | Insert stale individual IDs in acceptance | REJECT |
| R5-03 | Insert stale comma-separated IDs with backticks | REJECT |
| R5-04 | Duplicate canonical FP-P14 definition without backticks | REJECT |
| R5-05 | Use historical wording around a stale current-state assertion | REJECT |
| R5-06 | Add an unexpected parameter assertion elsewhere in AI_CONTEXT | REJECT |
| R5-07 | Add malformed P12B-19X gate-like row | REJECT |
| R5-08 | Validate check_45 against a source-derived parameter count | PASS |
| R5-09 | Insert a malformed canonical parameter definition | REJECT |
| R5-10 | Insert a duplicate canonical parameter definition in another format | REJECT |
| R5-11 | Insert a missing parameter from a current acceptance representation | REJECT |
| R5-12 | Insert a partial current parameter representation | REJECT |
| R5-13 | Insert an unexpected valid-looking parameter identifier | REJECT |
| R5-14 | Add a current-state parameter assertion elsewhere in acceptance | REJECT |
| R5-15 | Duplicate a gate identifier using a malformed suffix | REJECT |
| R5-16 | Insert a conflicting current B-12 representation | REJECT |
| R5-17 | Insert a correctly identified historical range | PASS |
| R5-18 | Insert a legitimate explanatory identifier reference | PASS |
| R5-19 | Insert a genuinely superseded historical definition | PASS |
| R5-20 | Add a sentence containing historical context and a stale current-state assertion | REJECT |

Add further fixtures for:

- FP-P1 and FP-P001.
- FP-P01X and similar malformed identifiers.
- Multiple malformed parameter tokens.
- Duplicate IDs separated by punctuation.
- Duplicate IDs in adjacent sentences.
- Unicode hyphen, en dash and em dash variants.
- Multiple representations in one section.
- Reordered identifiers.
- Missing canonical definitions.
- Changed canonical parameter count.
- Extra canonical parameter definitions.
- Missing or unreadable canonical register.
- Empty canonical collection.
- Duplicate exact gate identifiers.
- Conflicting gate identifiers.
- Multiple current-state AI_CONTEXT entries.
- Mixed historical and current assertions.
- Legitimate historical records containing backticks.
- Legitimate explanatory text containing parameter IDs.

### Fixture quality requirements

Every negative fixture must:

1. Execute the actual validator.
2. Receive a rejection for the intended validation reason.
3. Produce a meaningful diagnostic identifying the defect.
4. Avoid treating crashes, exceptions or unrelated failures as successful rejection.

Every positive fixture must prove that legitimate content remains accepted.

Never modify canonical baseline documents merely to make a fixture pass.

Mutation testing must operate on isolated copies or temporary fixture inputs.

---

## 7. REGRESSION PROTECTION — R1 THROUGH R4

Preserve every existing R1–R4 protection.

Do not remove or weaken:

- Duplicate-ID checks.
- Duplicate gate-row detection.
- Stale-reference checks.
- Formula range checks.
- Canonical parameter extraction.
- Parameter-chain validation.
- Historical-reference safeguards.
- Manifest validation.
- Prompt archival validation.
- AI_CONTEXT synchronization.
- Positive fixtures.
- Negative fixtures.
- Existing validator checks.

Run the unchanged R4 fixture suite before and after implementing R5.

The R4 baseline is:

- 82 validator checks.
- 33 positive fixtures.
- 73 negative fixtures.

These are minimum preservation requirements, not targets that authorize reducing existing coverage.

Add R5 checks and fixtures without deleting or replacing previous ones.

If the architecture requires legitimate changes to an existing check, document the reason, preserve its original protection, and add an equivalent or stronger regression fixture.

Report all actual totals.

---

## 8. DOCUMENTATION SYNCHRONIZATION

Preserve the four authoritative Prompt 12B specifications.

Do not rewrite their substantive content.

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

Preserve the existing Prompt 12B acceptance results:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL.
- 0 BLOCKED.

The three PARTIAL gates must remain:

- P12B-14.
- P12B-16.
- P12B-23.

Do not close them artificially.

### Mandatory outdated-status corrections

The R4 independent audit found outdated validator totals in:

1. `docs/PROJECT_PROGRESS.md`
2. `docs/ROADMAP.md`
3. `docs/stage-2/00_stage_2_handoff.md`

These files contain older validator totals despite also containing newer R4 status information.

Review and synchronize all current status summaries.

Remove contradictory current-state claims.

Do not erase legitimate historical audit results.

Clearly distinguish:

- Historical R3 results.
- Historical R4 results.
- Current R5 execution results.
- Independent audit findings.
- Pending independent acceptance.

Review:

- `docs/PROJECT_PROGRESS.md`
- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/ROADMAP.md`
- `docs/stage-2/00_stage_2_handoff.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/prompts/INDEX.md`
- Change manifests.
- Relevant validator documentation.

### Permanent prompt archive

Create:

`docs/prompts/prompt_12B-C1-R5_...md`

Follow the established naming convention.

Archive the complete R5 instruction.

Update `docs/prompts/INDEX.md` with the exact path.

Do not create duplicate prompt files.

Update the project handoff so the next independent auditor knows that:

- Project X (74) is the previous audit baseline.
- R5 is the current corrective task.
- The complete R5 prompt must accompany the fresh ZIP snapshot.
- Independent adversarial auditing is still required.
- Prompt 12C remains unauthorized.

---

## 9. VALIDATION REQUIREMENTS

Run the following after the modifications.

1. Complete Prompt 12B validator.
2. All existing positive fixtures.
3. All existing negative fixtures.
4. All seven original R4 adversarial fixtures.
5. All new R5 fixtures.
6. All R1–R4 regression fixtures.
7. Prompt 12A validator.
8. Relevant Stage 2 validators.
9. Alliance validators.
10. Warfare validators.
11. Prompt 11B and 11C validators.
12. Relevant unit tests.
13. Documentation link validation.
14. Final project validation.

Also conduct independent-style mutation tests against:

- The gate register.
- The complete acceptance document.
- The canonical formula register.
- The complete current B-12 AI_CONTEXT entry.

For every execution report:

- Exact command.
- Exit code.
- Actual check count.
- Positive fixture count.
- Negative fixture count.
- Failure output, if any.
- Whether execution completed.
- Whether the result is relevant to R5 acceptance.

Do not report a timed-out test suite as passing.

Do not report an incomplete test run as a completed suite.

Do not fabricate execution evidence.

### Important pytest instruction

If broad pytest execution exceeds the execution limit:

- Record that it did not complete.
- Identify any observed failures.
- Run relevant targeted tests separately where practical.
- Do not claim the entire suite passed.

---

## 10. ACCEPTANCE CRITERIA

R5 is complete only when every criterion below is satisfied.

### A. Malformed identifiers

Malformed FP-P identifiers cannot bypass acceptance, AI_CONTEXT or canonical-register validation.

### B. Stale individual claims

Individual stale parameter IDs, comma-separated representations and partial lists are rejected when asserted as current.

### C. Canonical definition integrity

Unformatted, formatted, duplicated or malformed canonical definitions cannot disappear during extraction.

### D. Historical-reference safety

Genuinely historical information remains valid, but historical wording cannot conceal a stale current-state assertion.

### E. Full AI_CONTEXT scanning

The complete current B-12 entry is validated, not just one table row.

### F. Gate identifier integrity

All authoritative gate identifiers are correctly formatted, unique and unambiguous.

### G. Canonical count architecture

The canonical formula register determines the expected FP-P identifier collection and its derived count.

No duplicate hard-coded production expectation remains.

### H. Regression

Every existing R1–R4 capability and fixture remains operational.

### I. Documentation

All outdated status summaries are synchronized.

The complete R5 instruction is permanently archived and indexed.

### J. Independent audit readiness

The project contains reproducible evidence for every correction and enough documentation for an external auditor to independently verify the results.

A passing validator total alone is insufficient.

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
- Claim production audit-digest operations are implemented.
- Change unrelated game architecture.
- Stage, commit or push Git changes.

Preserve the known outstanding security obligations:

- Authenticated table-wide UPDATE access on `feasibility.profiles`.
- Missing corrective migration 0005.
- Missing SQL permission tests.
- Missing protective audit-log trigger.
- Unverified production tamper-evident audit implementation.
- Unverified production audit-digest job.

Preserve Prompt 12B PARTIAL gates P12B-14, P12B-16 and P12B-23.

---

## 12. FINAL IMPLEMENTATION REPORT

At completion, provide:

1. Exact files created.
2. Exact files modified.
3. Exact permanent R5 prompt archive path.
4. D-014 reading attestation, only if actually completed.
5. Independent reproduction results for all seven R4-audit findings.
6. All malformed-identifier detection results.
7. Acceptance stale-reference scanning results.
8. Canonical definition integrity results.
9. Historical-reference classification results.
10. AI_CONTEXT complete-entry scanning results.
11. Gate uniqueness results.
12. `check_45()` architectural correction details.
13. Positive fixture results.
14. Negative fixture results.
15. R1–R4 regression results.
16. Project-wide validator results.
17. Unit-test results.
18. Incomplete or timed-out test executions.
19. Documentation synchronization results.
20. Manifest and prompt archive verification.
21. Remaining unresolved issues.
22. Git status without making Git changes.
23. Explicit confirmation that production security work was not falsely claimed.
24. Explicit confirmation that Prompt 12C has not started.

Use honest PASS, PARTIAL, FAIL and BLOCKED statuses.

Distinguish:

- Documentation completion.
- Validator execution.
- Fixture execution.
- Runtime verification.
- Independent audit acceptance.

Do not claim independent approval.

---

## 13. STOP CONDITION

After completing R5:

STOP.

Do not begin Prompt 12C.

Do not create Prompt 12C workflows, integrations, acceptance specifications or implementation tasks.

The owner will create a fresh ZIP snapshot and submit it together with the complete R5 prompt to an independent auditor.

The independent auditor must:

- Extract and inspect the exact new ZIP.
- Compare it against the complete R5 prompt.
- Independently reproduce all previous R4 defects.
- Independently reproduce all R5 defects.
- Inspect canonical parameter extraction.
- Test historical-reference safeguards.
- Test complete occurrence scanning.
- Verify gate uniqueness.
- Execute relevant project validators and fixtures.
- Verify documentation synchronization.
- Report any remaining bypasses.

Wait for separate owner authorization.

**Guiding principle: Every identifier occurrence must be accounted for, every authoritative definition must be unambiguous, every historical exception must be justified, and the canonical formula register—not validator assumptions—must remain the source of truth.**