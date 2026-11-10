# PROMPT 12B-C1-R7 — FINAL STRUCTURAL VALIDATION, COMPLETE AI_CONTEXT ENTRY INTEGRITY, SEMANTIC ASSERTION PARSING AND CANONICAL DEFINITION DISCOVERY

## 1. TASK AUTHORIZATION

You are authorized to execute this corrective task directly inside the existing live Nation Supremacy project directory.

This is a targeted final corrective task for the Prompt 12B-C1 validator-hardening sequence.

You MUST implement the corrections, execute the required tests, preserve previous protections, synchronize documentation and provide a detailed implementation report.

Do not merely provide recommendations or a proposed implementation plan.

### Mandatory autonomous decision policy

Before substantial work, read the complete:

`AUTONOMOUS_DECISION_POLICY.md`

Policy identifier: D-014.

Follow D-014 throughout the task.

Resolve ordinary technical and documentation decisions autonomously.

Preserve approved decisions, owner-reserved decisions, historical records and all existing identifiers.

Do not invent approvals, test evidence or implementation results.

### Workspace restrictions

Work exclusively in the existing live project directory.

The latest independent audit snapshot is:

`Project X (76).zip`

This ZIP is an audit artifact, not a working project.

Never:

- Extract or use the audit ZIP as your working directory.
- Create duplicate project directories.
- Replace the live project with an archive.
- Overwrite unrelated work.
- Stage, commit or push Git changes.
- Begin Prompt 12C.

---

## 2. PREVIOUS AUDIT AND AUTHORITATIVE FINDINGS

The previous independent audit examined:

`Project X (76).zip`

The coding agent's bundled validator reported:

- 82/82 checks passed.
- 45/45 positive fixtures passed.
- 115/115 negative fixtures passed.
- Exit code 0.

All 30 numbered R6 fixtures passed.

However, independent mutation testing demonstrated eight additional bypasses.

These findings are the authoritative starting point for R7.

### Eight reproduced defects

| ID | Independent mutation | Expected |
|---|---|---|
| R7-01 | Duplicate FP-P01 in current `b12_fair_play` entry | REJECT |
| R7-02 | Missing parameter representation in current B-12 entry | REJECT |
| R7-03 | Incomplete current parameter assertion in AI_CONTEXT | REJECT |
| R7-04 | Additional continuation text containing a parameter assertion | REJECT |
| R7-05 | Additional B-12 parameter inventory row | REJECT |
| R7-06 | Incomplete current parameter collection in acceptance §2.1 | REJECT |
| R7-07 | Historical wording disguising a present-state assertion | REJECT |
| R7-08 | Duplicate canonical parameter definition in a heading | REJECT |

The complete 82-check production validator accepted these mutations.

Therefore, R6 did not achieve independent acceptance.

### Previous source locations

The independent auditor identified these locations in:

`docs/qa_backups/12B_validate_b12.py`

- `Model.rebuild()` — approximately lines 265–289.
- `canonical_params()` — approximately lines 969–992.
- `is_historical_exempt()` — approximately lines 1092–1101.
- `acceptance_stale_problems()` — approximately lines 1133–1174.
- `check_78()` — approximately lines 1404–1478.

Line numbers are from the previous snapshot. Inspect the actual live file rather than assuming they remain unchanged.

---

## 3. MANDATORY DEFECT 1 — COMPLETE AI_CONTEXT ENTRY PARSING

The current implementation does not reliably validate the complete current B-12 entry.

Selected lines are being inspected instead of the entire logical entry.

### Required correction

Identify the complete `b12_fair_play` entry in:

`docs/AI_CONTEXT.md`

Determine its exact structural boundaries using the actual document format.

Parse the complete entry, including:

- The main entry line.
- All continuation lines.
- Associated parameter inventory rows.
- Associated tables.
- Additional paragraphs.
- Additional sentences.
- Nested or indented content belonging to the entry.
- Any other authoritative current-state representation.

Do not assume the first parameter chain is the only relevant representation.

Do not assume that a line beginning with `b12_fair_play:` contains the entire entry.

### Required validation

The complete current entry must have:

1. Exactly one authoritative current B-12 entry.
2. Exactly one unambiguous canonical parameter collection.
3. A complete parameter representation.
4. No missing identifiers.
5. No unexpected identifiers.
6. No duplicate occurrences in authoritative representations.
7. No malformed parameter-like identifiers.
8. No conflicting current-state assertions.
9. No additional parameter inventory rows that contradict the canonical source.

The expected parameter sequence must be dynamically derived from the canonical formula register.

### Mandatory negative cases

Reject:

- Duplicate FP-P01 in the entry.
- Missing identifiers.
- An incomplete parameter chain.
- FP-P15 or another unexpected identifier.
- An additional current-state parameter sentence.
- A duplicate parameter inventory row.
- A second conflicting B-12 entry.
- A malformed parameter identifier in a continuation line.

### Preservation requirement

Legitimate explanatory references to individual formulas must remain valid.

Do not require every explanatory sentence to repeat the complete parameter collection.

---

## 4. MANDATORY DEFECT 2 — COMPLETE ACCEPTANCE DOCUMENT PARSING

The acceptance validator must not depend on a small collection of recognized phrases or first-match parsing.

Target:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

### Required correction

Parse complete logical paragraphs and records.

Include:

- Section headings.
- Section 2.1.
- All acceptance gates.
- Tables.
- Table continuations.
- Lists.
- Paragraphs.
- Multiple sentences.
- Additional clauses.
- Text containing parameter claims outside expected chains.

Recognize semantically equivalent current-state claims.

Examples include:

- The current formula parameters are ...
- The B-12 parameter set includes ...
- The formula register contains ...
- The authoritative parameter collection consists of ...
- The current formula-register identifiers are ...
- The B-12 inventory contains ...
- The current parameter list is ...

These examples are not an exhaustive keyword whitelist.

### Mandatory correction

A current-state assertion that claims to describe the complete canonical parameter collection must be compared with the full ordered canonical collection.

Reject:

- Incomplete collections.
- Missing IDs.
- Unexpected IDs.
- Duplicate IDs.
- Reordered IDs.
- Malformed IDs.
- Conflicting current-state collections.
- Additional current authoritative representations.

Do not simply scan for a fixed expected comma-separated chain.

Do not ignore statements outside the recognized representation.

### Important distinction

An explanatory mention of FP-P01 alone is not automatically a complete collection claim.

For example:

`FP-P01 is used by the market fairness calculation.`

This must remain valid when it is a legitimate explanatory statement.

The parser must distinguish complete collection assertions from ordinary references.

If an authoritative current-state statement is ambiguous, fail closed with a useful diagnostic.

---

## 5. MANDATORY DEFECT 3 — SEMANTIC HISTORICAL CLASSIFICATION

The R6 implementation still relies too heavily on historical keywords.

A sentence containing `historical` is not necessarily historical.

### Mandatory rejected example

`Historical record: the B-12 formula parameters remain FP-P01 and FP-P12.`

This asserts a current incomplete parameter collection and must be rejected.

### Legitimate historical examples

The following may be accepted:

- An explicitly dated former parameter range.
- A documented previous revision.
- An explicitly superseded parameter list.
- A historical comparison table.
- A description of how the canonical collection changed between versions.

### Required classification

Every relevant parameter-bearing statement must be classified as one of:

1. Current authoritative assertion.
2. Historical record.
3. Explicitly superseded record.
4. Explanatory reference.
5. Canonical definition.
6. Malformed candidate.
7. Ambiguous assertion.

### Classification requirements

Use the complete statement, surrounding document structure, record boundaries, tense and explicit historical context.

Do not classify a statement as historical solely because it contains:

- historical;
- previous;
- former;
- old;
- legacy;
- archived.

These terms must be evaluated in context.

A historical qualifier cannot override a present-tense current-state assertion.

Where an authoritative section contains an ambiguous parameter-bearing assertion, reject it rather than silently exempting it.

Document the classification rules and test both legitimate and adversarial examples.

---

## 6. MANDATORY DEFECT 4 — CANONICAL DEFINITION DISCOVERY

Canonical source:

`docs/stage-2/20_fair_play_and_player_protection_formula_register.md`

The current parser does not discover every definition candidate.

It skips certain Markdown heading lines, allowing duplicate definitions to escape.

### Required correction

Inspect the complete canonical definition region.

Discover parameter definitions in:

- Markdown tables.
- Ordinary paragraphs.
- Definition lists.
- Headings.
- Nested headings.
- Structured records.
- Explicit definition statements.
- Other formatting used by the actual canonical register.

### Mandatory negative cases

Reject:

- Duplicate FP-P14 definition in a heading.
- Duplicate definitions in prose.
- Duplicate definitions across a table and a paragraph.
- Conflicting definitions.
- Malformed definition identifiers.
- Missing definitions.
- Unexpected additional definitions.
- Definition records outside permitted canonical boundaries.
- Ambiguous definition regions.

### Important distinction

Not every parameter mention is a definition.

For example:

`FP-P01 is referenced in the acceptance section.`

This is an explanatory reference, not a second canonical definition.

The parser must recognize definition candidates and record boundaries without blindly counting every mention as a definition.

Do not restrict canonical extraction to Markdown table syntax.

Do not discard heading lines before inspecting their contents.

Do not silently ignore malformed definition candidates.

---

## 7. COMPLETE IDENTIFIER OCCURRENCE ACCOUNTING

Implement a reusable scanner for parameter-like identifiers.

It must retain every occurrence before any set conversion or deduplication.

For every occurrence, preserve:

- Source file.
- Section.
- Line number or source offset.
- Original token.
- Normalized identifier if valid.
- Surrounding logical statement.
- Structural context.
- Classification.
- Occurrence order.
- Validation outcome.

### Identifier cases

Recognize valid canonical identifiers and detect malformed variants, including:

- FP-P.
- FP-PX.
- FP-PXX.
- FP-P1.
- FP-P001.
- FP-P-01.
- FP-P01X.
- FP-P01_extra.
- FP-P01-extra when not an authorized identifier representation.
- Multiple malformed tokens.
- Malformed tokens next to punctuation.
- Malformed tokens in headings.
- Malformed tokens in tables.
- Malformed tokens in continuation lines.

Support ordinary hyphens, en dashes and em dashes in range representations.

Do not extract a valid prefix from a malformed larger token and discard the remaining characters.

Do not allow punctuation, Markdown formatting, whitespace or line breaks to make an occurrence disappear.

### Mandatory validation order

1. Discover the complete document block.
2. Extract all candidate occurrences.
3. Preserve occurrence order and source location.
4. Identify malformed tokens.
5. Classify each occurrence.
6. Validate duplicate counts.
7. Validate missing identifiers.
8. Validate unexpected identifiers.
9. Validate ordering.
10. Validate complete authoritative representations.
11. Construct lookup sets only after occurrence-level validation.

Do not use first-match selection where uniqueness is required.

Do not silently ignore unrecognized parameter-bearing statements.

---

## 8. CANONICAL SOURCE-OF-TRUTH

The formula register must remain the production source of truth.

Extract the authoritative ordered parameter definitions dynamically from:

`docs/stage-2/20_fair_play_and_player_protection_formula_register.md`

Requirements:

- No hard-coded production parameter list.
- No silent fallback.
- No duplicate hidden expected collection.
- No reliance on a hard-coded count of 14.
- No reliance on a second manually maintained identifier list.
- Reject unreadable or missing source files.
- Reject empty extraction.
- Reject duplicate definitions.
- Reject malformed definitions.
- Reject conflicting definitions.
- Reject ambiguous canonical regions.

Derive:

- Ordered parameter collection.
- Expected identifier sequence.
- Expected collection count.
- Expected unique identifier collection.

All downstream acceptance and AI_CONTEXT comparisons must use the same extracted source.

Preserve the separate Prompt 12B metric of 12 numerical parameters. Do not confuse it with the FP-P identifier collection.

Inspect `check_45()` and preserve its source-derived count behaviour.

If the canonical register legitimately changes, downstream expectations must follow the extracted records rather than a hidden fixed list.

---

## 9. MANDATORY ARCHITECTURAL REVIEW

Inspect the actual implementation before editing.

At minimum:

- `Model.rebuild()`
- `Model.param_raw`
- `canonical_params()`
- `param_representation()`
- `scan_param_occurrences()`
- `compare_param_occurrences()`
- `acceptance_stale_problems()`
- `is_historical_exempt()`
- `check_45()`
- `check_76()`
- `check_77()`
- `check_78()`
- AI_CONTEXT entry parsing.
- Canonical definition parsing.
- Gate parsing.
- All fixture execution paths.

Build on the existing architecture.

Do not create unnecessary parallel validator frameworks.

Prefer reusable structural parsers, lexical scanning and contextual classification over duplicated regular expressions.

The actual production validator must use the corrected parsing architecture.

A helper function that is tested but not called by the complete validator does not satisfy this task.

---

## 10. PERMANENT R7 ADVERSARIAL FIXTURES

Create permanent fixtures for all eight independently reproduced bypasses.

| Fixture | Mutation | Expected |
|---|---|---|
| R7-01 | Duplicate FP-P01 in current B-12 entry | REJECT |
| R7-02 | Missing parameter representation in current B-12 entry | REJECT |
| R7-03 | Incomplete current parameter assertion in AI_CONTEXT | REJECT |
| R7-04 | Additional continuation text with parameter assertion | REJECT |
| R7-05 | Additional B-12 parameter inventory row | REJECT |
| R7-06 | Incomplete collection in acceptance §2.1 | REJECT |
| R7-07 | Historical wording disguising present-state assertion | REJECT |
| R7-08 | Duplicate canonical definition in heading | REJECT |

### Additional negative fixtures

Add tests for:

- Multiple conflicting B-12 entries.
- Duplicate current authoritative assertions.
- Incomplete current parameter collections.
- Missing canonical identifiers.
- Unexpected identifiers.
- Reordered identifiers.
- Duplicate identifiers separated by punctuation.
- Malformed parameter tokens.
- Duplicate canonical definitions across formats.
- Malformed canonical definitions in headings.
- Additional current-state claims outside expected rows.
- Multiple continuation lines.
- Duplicate parameter inventory rows.
- Ambiguous document-block boundaries.
- Empty canonical extraction.
- Missing formula register.
- Changed canonical parameter count.
- Historical qualifiers combined with present-tense assertions.
- Unicode range separators.
- Multiple representations in one paragraph.
- Multiple sentences with conflicting representations.

### Additional positive fixtures

Preserve and test:

- A correct complete canonical representation.
- A genuinely dated historical range.
- An explicitly superseded historical collection.
- A legitimate historical comparison.
- A single explanatory FP-P01 reference.
- An explanation of an individual formula.
- A legitimate parameter mention in an AI_CONTEXT continuation.
- A valid explanatory paragraph inside the B-12 entry.
- A legitimate canonical formatting variation.

### Fixture quality

Negative fixtures pass only when the actual complete production validator rejects the mutation for the intended reason.

A crash, exception or unrelated failure does not count.

Positive fixtures must pass through the actual production validation path.

Use isolated copies or temporary inputs.

Never alter baseline specifications merely to make a fixture pass.

---

## 11. REGRESSION PROTECTION

The R6 baseline must be preserved.

Previous results:

- 82 validator checks.
- 45 positive fixtures.
- 115 negative fixtures.
- 30 numbered R6 fixtures.

These are minimum preservation requirements before R7 additions.

Run the unchanged R6 regression suite before and after modifications.

Preserve all R1–R6 protections, including:

- Duplicate-ID detection.
- Gate uniqueness.
- Duplicate acceptance-row detection.
- Malformed gate identifier detection.
- Stale formula-reference detection.
- Formula range validation.
- Canonical source extraction.
- Dynamic expected parameter collection.
- Source-derived count validation.
- Complete acceptance collection comparison.
- AI_CONTEXT synchronization.
- Historical-reference safeguards.
- Manifest validation.
- Prompt archive integrity.
- Prompt index validation.
- All previous positive fixtures.
- All previous negative fixtures.

Do not remove, skip, weaken or silently reclassify previous fixtures.

If an earlier check needs modification, provide an equivalent or stronger regression test and document the reason.

Report actual totals.

---

## 12. DOCUMENTATION AND ARCHIVE SYNCHRONIZATION

Preserve all four authoritative Prompt 12B specifications.

Do not rewrite their substantive content.

Preserve:

- 344 normative rules.
- 106 requirements.
- REQ-764 through REQ-869.
- 16 formulas.
- 12 numerical parameters.
- 14 canonical FP-P parameters, subject to the actual canonical register.
- D-178 through D-187.
- DD-226 through DD-235.
- All owner-reserved decisions.
- All legal-dependent unresolved decisions.

Preserve Prompt 12B acceptance:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL.
- 0 BLOCKED.

The three PARTIAL gates remain:

- P12B-14.
- P12B-16.
- P12B-23.

Do not artificially close them.

### Permanent R7 prompt archive

Create exactly one permanent archive:

`docs/prompts/prompt_12B-C1-R7_final_structural_validation_and_canonical_integrity.md`

Preserve the complete R7 instruction.

Update:

`docs/prompts/INDEX.md`

Ensure:

- Exact path.
- Unique index entry.
- No duplicate R7 archive.
- Complete archived instruction.
- Verified file size.
- Verified SHA-256.
- Reproducible checksum convention.

### Synchronization review

Review:

- `docs/PROJECT_PROGRESS.md`
- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/ROADMAP.md`
- `docs/stage-2/00_stage_2_handoff.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/prompts/INDEX.md`
- Relevant manifests.
- Relevant validator documentation.

Clearly distinguish:

- R6 implementation results.
- R6 independent audit failures.
- R7 implementation results.
- Pending independent R7 acceptance.
- Historical results from earlier revisions.

Do not present historical test totals as current results.

Update the handoff to state that:

- Project X (76) is the previous audited baseline.
- R7 is the next corrective task.
- The complete R7 instruction must accompany the next ZIP.
- Independent R7 acceptance is pending.
- Prompt 12C remains unauthorized.

---

## 13. VALIDATION REQUIREMENTS

After implementation, execute:

1. Complete Prompt 12B validator.
2. All existing positive fixtures.
3. All existing negative fixtures.
4. Original seven R4 adversarial fixtures.
5. All R5 fixtures.
6. All R6 fixtures.
7. All new R7 fixtures.
8. Prompt 12A validator.
9. Relevant Stage 2 validators.
10. Alliance validators.
11. Warfare validators.
12. Prompt 11B validator.
13. Prompt 11C validator.
14. Relevant unit tests.
15. Documentation link validation.
16. Prompt archive and index validation.
17. Change-manifest validation.
18. Final project validation.

### Independent-style mutation testing

Use isolated copies of:

- Complete AI_CONTEXT.
- Complete acceptance document.
- Complete canonical formula register.
- Complete acceptance gate register.

Execute the complete production validator against each mutation.

Do not report a helper-level test as proof that the production validator rejects the same mutation.

### Actual execution reporting

For each command, report:

- Exact command.
- Exit code.
- Actual output.
- Number of checks.
- Positive fixture count.
- Negative fixture count.
- Whether execution completed.
- Any error or timeout.

If a broad test suite times out, report it as incomplete.

Do not claim a suite passed without a completed result.

---

## 14. ACCEPTANCE CRITERIA

R7 is implementation-complete only if all criteria pass.

A. Entire B-12 AI_CONTEXT entry is structurally parsed.

B. All relevant continuation lines, paragraphs, inventory rows and additional representations are validated.

C. Acceptance §2.1 and all other relevant acceptance content are semantically inspected.

D. Historical classification cannot disguise present-state assertions.

E. Canonical definitions are discovered in tables, headings and prose.

F. Every relevant valid and malformed identifier occurrence is accounted for.

G. Duplicate, missing, unexpected and reordered identifiers cannot bypass validation.

H. The canonical formula register is the sole production source of truth.

I. All eight R7 reproductions are rejected for the correct reasons.

J. All R1–R6 protections and fixtures remain intact.

K. Legitimate historical and explanatory references remain valid.

L. The R7 prompt archive and documentation synchronization are complete.

M. An external auditor can reproduce the relevant results from the next ZIP.

N. No Prompt 12C work has started.

A passing aggregate validator total is not sufficient evidence of completion.

---

## 15. STRICT SCOPE LIMITATIONS

Do not:

- Begin Prompt 12C.
- Create Prompt 12C deliverables.
- Rewrite completed Prompt 12B specifications.
- Approve provisional requirements.
- Close owner-reserved decisions.
- Resolve legal-dependent questions without authorization.
- Implement production security controls.
- Create Supabase migration 0005.
- Claim production audit tamper-evidence is implemented.
- Claim production audit-digest operations are implemented.
- Change unrelated game architecture.
- Stage, commit or push Git changes.

Preserve all outstanding security obligations:

- Authenticated table-wide UPDATE access on `feasibility.profiles`.
- Missing corrective migration 0005.
- Missing SQL permission tests.
- Missing protective audit-log trigger.
- Unverified production tamper-evident audit implementation.
- Unverified production audit-digest job.

Preserve the three Prompt 12B PARTIAL acceptance gates.

---

## 16. FINAL IMPLEMENTATION REPORT

Provide:

1. Exact files created.
2. Exact files modified.
3. Exact R7 prompt archive path.
4. D-014 reading attestation, if actually completed.
5. All eight R6 bypass reproduction results before correction.
6. Corrections made for each defect.
7. AI_CONTEXT structural parsing implementation.
8. Acceptance semantic parsing implementation.
9. Historical classification implementation.
10. Canonical definition discovery implementation.
11. Identifier occurrence accounting implementation.
12. Dynamic canonical parameter extraction results.
13. Positive fixture results.
14. Negative fixture results.
15. R1–R6 regression results.
16. Project-wide validator results.
17. Unit-test results and incomplete executions.
18. Documentation synchronization results.
19. Prompt archive and checksum results.
20. Manifest validation results.
21. Remaining defects or limitations.
22. Git status without modifying Git.
23. Outstanding production security obligations.
24. Explicit confirmation that Prompt 12C has not started.

Use PASS, PARTIAL, FAIL and BLOCKED honestly.

Distinguish implementation completion, documentation completion, validator execution, fixture execution, runtime verification and independent audit acceptance.

Do not claim independent approval.

---

## 17. FINAL STOP CONDITION

After completing R7:

STOP.

Do not begin Prompt 12C.

Do not create Prompt 12C deliverables.

Do not interpret successful R7 implementation as permission to proceed.

The owner will create a fresh ZIP snapshot and submit it together with the complete R7 instruction to an independent auditor.

The independent auditor will independently inspect the archive, execute the validators, reproduce the R4–R7 adversarial mutations and verify every acceptance criterion.

Wait for separate owner authorization.

**FINAL DIRECTIVE**

Fix the underlying structural parsing and semantic classification weaknesses.

Do not merely patch the eight examples.

Preserve every previously approved specification and validation protection.

Make the canonical register the genuine source of truth.

Account for every relevant identifier occurrence.

Reject ambiguous authoritative records.

Preserve legitimate historical and explanatory information.

Produce reproducible evidence.

Stop after R7.

Prompt 12C remains unauthorized until the owner reviews the independent audit and explicitly approves it.
