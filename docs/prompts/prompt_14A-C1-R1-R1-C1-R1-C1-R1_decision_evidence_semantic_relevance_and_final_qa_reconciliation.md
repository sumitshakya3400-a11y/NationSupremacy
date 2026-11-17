# PROMPT 14A-C1-R1-R1-C1-R1-C1-R1 — DECISION EVIDENCE SEMANTIC RELEVANCE VALIDATION AND FINAL QA RECONCILIATION

## 1. OBJECTIVE

Complete the remaining defects identified during the independent audit of Project X (101).

This is a narrow corrective assignment within Prompt 14A.

The two objectives are:

1. Ensure that D-014 decision evidence substantively supports the exact amendment being authorized, rather than merely checking whether a referenced file exists.
2. Reconcile all current documentation-link validation totals across B-14, the numerical QA report, the progress log and applicable current continuity records.

The previous independent audit reproduced a false acceptance involving a fabricated B-04 amendment supported by an unrelated fair-play document.

This defect must be fixed and permanently covered by regression tests.

Do not restart Prompt 14A or unnecessarily rewrite completed work.

## 2. MANDATORY GOVERNANCE AND POLICY

Before beginning, read the entire:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Follow its actual D-014 requirements, including all Category A, B, C and D authority boundaries.

Do not modify the Autonomous Decision Policy.

Preserve the distinction between:

- Owner-approved values.
- Provisional values.
- Design proposals.
- Values requiring playtesting.

A decision-register entry, validator result, arithmetic calculation or successful test does not constitute owner approval.

Do not fabricate owner authorization, evidence, decisions, test results or acceptance records.

### Workflow restrictions

- Work in the existing live project repository.
- Uploaded ZIP archives are audit snapshots, not working repositories.
- Do not create duplicate project folders.
- Do not overwrite existing work unnecessarily.
- Do not stage, commit, push, reset, revert or discard Git changes.
- Do not modify protected Git history.
- Do not implement gameplay, formulas, frontend, backend, database, SQL, API, migration, security or deployment changes.
- Do not modify the existing production B-04 formula source clauses.
- Do not alter the two current B-04 source hashes.
- Do not populate the production amendment manifest.
- Do not authorize Prompt 14B.

Inspect actual files before making changes. Do not assume filenames, validator structures or decision classifications without checking the repository.

## 3. CORRECTION A — SUBSTANTIVE EVIDENCE RELEVANCE VALIDATION

### 3.1 Existing defect

The previous validator's `_evidence_supports()` function primarily checks:

- Evidence text length.
- Evidence or rationale wording.
- Presence of a recognized repository path.
- Existence of the referenced file.

These checks are insufficient.

A referenced file can exist without supporting the proposed amendment.

The validator must not accept an amendment merely because the decision contains convincing language and a valid repository path.

### 3.2 Required validation principle

Implement actual evidence-content verification.

The validation chain must be:

**Affected source clause → decision rationale → specific evidence claim → relevant evidence document → actual supporting document content → consequences → authorization → amendment manifest → matching source fingerprint.**

Every part of this chain must be verifiable.

The validator must establish:

1. Which exact controlled clause is changing.
2. What specific proposition the amendment is asserting.
3. Which evidence claim supports that proposition.
4. Which actual source document and section contain the supporting information.
5. Whether the referenced content genuinely supports the claimed proposition.
6. Whether the decision's rationale accurately reflects that content.
7. Whether the decision has the authority required by D-014.
8. Whether the amendment manifest and source fingerprint correspond to the authorized change.

A file path, filename, existing document, generic evidence description, matching keyword or matching hash is not independently sufficient proof of substantive relevance.

### 3.3 Evidence-source validation design

Inspect the current B-04 source contracts, validator architecture, existing decision records and authoritative documentation before choosing the implementation.

Implement a deterministic, auditable evidence-validation mechanism compatible with the repository's existing architecture.

The mechanism must:

- Inspect actual evidence document contents.
- Identify the relevant source section or content location.
- Connect the evidence to the precise affected clause and asserted proposition.
- Verify evidence excerpts or structured references against the actual source content.
- Distinguish supporting evidence from unrelated, contradictory or merely contextual material.
- Reject fabricated, generic, misleading and unrelated evidence descriptions.
- Detect nonexistent, stale, incorrectly located or materially changed evidence references.
- Require appropriate evidence coverage for every material claim needed to justify an amendment.
- Preserve source provenance and traceability.
- Fail closed when relevance cannot be established.

Where structured evidence mappings, source contracts or evidence identifiers are appropriate, use them.

Do not depend exclusively on free-text similarity or generic keyword matching.

Do not accept an exact quotation merely because it appears somewhere in a document: its actual context and relationship to the proposed amendment must also be checked.

Do not make all amendments fail simply to obtain a fail-closed result. Genuine supporting evidence must continue to permit legitimate amendments.

### 3.4 Exact Project X (101) false-acceptance regression

Create a permanent negative regression test reproducing the independent audit attack.

The test must:

1. Start with the existing B-04 source fixture.
2. Modify `F-EC-000b` to permit binary floating-point calculations.
3. Update the source hash.
4. Create a complete-looking Category B decision record using D-998.
5. Include the previous rule.
6. Include the replacement rule.
7. Include alternatives.
8. Include rationale.
9. Include consequences.
10. Include reopening conditions.
11. Cite `docs/stage-2/20_fair_play_and_player_protection.md` as supporting evidence.
12. Include generic or misleading evidence wording.
13. Supply a matching amendment manifest.
14. Ensure that the non-evidence structural and authorization requirements are otherwise satisfied according to the actual D-014 classification of the affected clause.

**Expected result: REJECT.**

Most importantly, rejection must be attributable to the failure of substantive evidence relevance.

Do not allow the test to pass merely because of an unrelated authorization, syntax, missing-field or hash error.

The test must demonstrate that an unrelated existing document cannot authorize a B-04 numerical amendment.

### 3.5 Additional negative regression tests

Add focused tests for:

- An unrelated document containing superficially similar terminology.
- A document whose relevant section does not support the proposed change.
- Generic evidence language without substantive supporting material.
- A fabricated supporting excerpt that does not match the actual source.
- A genuine quotation presented with misleading context.
- A stale or invalid evidence location.
- An evidence source that has materially changed since the recorded reference.
- A decision whose rationale makes claims that its cited source does not support.
- A decision with partial evidence coverage where a material claim remains unsupported.

Each negative test must demonstrate rejection for the appropriate evidence-related reason.

### 3.6 Positive regression tests

Preserve and verify legitimate amendment paths.

Create or retain temporary, isolated positive fixtures for:

**Category A**
- A valid owner-authorized test fixture.
- Correct owner authority and supporting evidence.
- No fabricated production owner approval.

**Category B**
- A complete legitimate ordinary design-decision fixture.
- Relevant supporting evidence.
- Correct decision classification, rationale and authority.

**Category C**
- A valid provisional decision fixture.
- Safe working default.
- Named evidence or test requirement.
- Correct provisional classification and reopening conditions.

Also test the unchanged Project X (101) baseline.

All test-only owner authorization and decisions must remain clearly identified as temporary test fixtures. Do not insert synthetic approvals into production decision registers.

A positive fixture must be accepted when it satisfies the actual D-014 requirements and the evidence genuinely supports the proposed change.

## 4. CORRECTION B — PRESERVE EXISTING VALIDATOR COVERAGE

Preserve all 51 existing numerical foundation validator checks.

Preserve all 118 existing self-tests and all other previously established regression coverage.

The new tests must be additive.

Do not:

- Delete an existing test.
- Weaken an existing assertion.
- Skip a failing test.
- Convert a failing test to an expected failure.
- Suppress a validator error.
- Change an expected result merely to make the suite pass.
- Reuse existing test identifiers in a conflicting way.

Maintain stable test identifiers and append new coverage using the repository's existing naming conventions.

Execute:

1. Numerical foundation validator.
2. Complete existing self-test suite.
3. New evidence-relevance regression tests.
4. Decision-register tests.
5. Next-action tests.
6. Final project validator.

Where a complete test suite cannot run, report the actual limitation and the tests independently executed. Never report a timeout as a pass.

## 5. CORRECTION C — FINAL DOCUMENTATION-LINK QA RECONCILIATION

### 5.1 Project X (101) baseline

The independently measured Project X (101) figures were:

| Measure | Baseline |
|---|---:|
| Markdown files | 128 |
| Total links | 4,359 |
| Local links | 3,977 |
| External links skipped | 382 |
| Anchors | 34 |
| Unresolved links | 0 |

The progress log reported these figures correctly.

However, B-14 CLOSURE-26 and numerical QA report §5.14 retained older totals of:

- 4,355 total links.
- 3,973 local links.

These are stale records.

### 5.2 Required reconciliation procedure

Complete the correction archive and all associated documentation changes first.

Then execute the actual documentation-link validator against the final working repository.

Use the resulting execution output as the authoritative current count.

Do not assume the new totals will remain identical to Project X (101), because this correction may introduce additional Markdown documents and links.

Reconcile all current operational records, including:

- `docs/stage-2/22_formulas_and_balance.md`
- Numerical QA report §5.14.
- Progress log current status.
- B-14 CLOSURE-26.
- B-14 CLOSURE-27, if it contains affected current totals.
- Applicable current continuity summaries and indexes.

Use the actual existing file locations and naming conventions.

Ensure that every current record reports the same execution's:

- Markdown file count.
- Total links.
- Local links.
- External links skipped.
- Anchor count.
- Unresolved links.

Retain the actual execution date and validation context.

### 5.3 Historical record preservation

Do not rewrite historical validation results.

Do not retrospectively replace earlier counts in historical progress entries, previous audit reports or archived correction records.

Correct current operational records only.

Distinguish historical results from the latest authoritative validation result.

## 6. PRESERVATION REQUIREMENTS

The following work must remain intact:

| Protected item | Required preservation |
|---|---|
| Active formula identifiers | 295 |
| Parameter inventory records | 393 |
| B-03 carry-in parameters | 20 |
| Existing numerical validator checks | All 51 |
| Existing self-tests | All 118 |
| Existing source-validation safeguards | Preserve |
| Treasury precision/rounding safeguards | Preserve |
| Owner-reserved field safeguards | Preserve |
| B-04 semantic source safeguards | Preserve |
| D-014 authorization safeguards | Preserve |
| Two current B-04 source hashes | Unchanged |
| Production amendment manifest | Empty |
| AUTONOMOUS_DECISION_POLICY.md | Unmodified |
| Existing owner-reserved decisions | Preserved |
| Historical correction archives | Preserved |
| Historical QA results | Preserved |

Preserve:

- All nine original formula registers.
- The canonical B-14 filename `22_formulas_and_balance.md`.
- All 20 B-03 carry-in parameter ownership and provisional classifications.
- Original numerical ownership.
- All existing formula and parameter identifiers.
- Existing source contracts, except narrowly necessary validator-specific metadata changes that do not alter protected production source content or hashes.

Do not introduce any new approved game-balance value.

Do not turn provisional values into approved values.

Do not create actual project decisions just to satisfy regression tests.

## 7. PROMPT ARCHIVAL REQUIREMENTS

Create a separate permanent prompt archive using this exact unique identifier:

`14A-C1-R1-R1-C1-R1-C1-R1`

Archive path:

`docs/prompts/prompt_14A-C1-R1-R1-C1-R1-C1-R1_decision_evidence_semantic_relevance_and_final_qa_reconciliation.md`

Requirements:

1. Store the complete correction instruction.
2. Update the applicable prompt index.
3. Preserve all earlier correction archives.
4. Do not overwrite the parent correction archive.
5. Do not reuse the parent correction ID.
6. Verify the archived file exists.
7. Record its actual byte size and SHA-256 hash.
8. Verify that its index reference resolves correctly.

Do not claim archival completion without verifying the actual file.

## 8. FINAL VALIDATION AND QA

After all changes and archival operations are complete, independently execute the applicable checks.

At minimum:

1. Verify all 295 formula identifiers.
2. Verify all 393 parameter records.
3. Verify all 20 B-03 carry-ins.
4. Verify the two B-04 source hashes are unchanged.
5. Verify the production amendment manifest remains empty.
6. Execute all original numerical validator checks.
7. Execute all existing self-tests.
8. Execute the exact D-998 false-acceptance regression.
9. Execute all additional negative evidence tests.
10. Execute positive Category A, B and C fixtures.
11. Verify that rejection of the D-998 attack is specifically attributable to unsupported evidence.
12. Execute decision-register tests.
13. Execute next-action tests.
14. Execute the final project validator.
15. Execute documentation-link validation after all archive and QA changes.
16. Reconcile every current QA count.
17. Verify the complete correction archive and its SHA-256.
18. Read Git status without modifying it.
19. Verify the Autonomous Decision Policy remains unmodified.
20. Verify no protected production formula or historical decision was changed.

Run independent mutation tests rather than trusting only the included self-tests.

Report any test limitation honestly.

## 9. REQUIRED FINAL REPORT

Provide a factual completion report containing:

### A. Evidence-relevance correction
- Actual validator files modified.
- Exact implementation approach.
- How supporting content is verified.
- How evidence is connected to the affected clause.
- Why the original D-998 attack is now rejected.

### B. Regression results

| Test | Expected result | Actual result |
|---|---|---|
| Exact Project X (101) D-998 attack | REJECT | |
| Unrelated evidence | REJECT | |
| Misleading evidence | REJECT | |
| Fabricated excerpt | REJECT | |
| Stale evidence location | REJECT | |
| Valid Category A fixture | ACCEPT | |
| Valid Category B fixture | ACCEPT | |
| Valid Category C fixture | ACCEPT | |
| Unchanged baseline | PASS | |

Provide the actual test identifiers and results.

### C. Validator results

Report actual counts for:

- Numerical foundation validator.
- Existing self-tests.
- New evidence tests.
- Decision-register tests.
- Next-action tests.
- Final project validator.

### D. Final documentation QA

Report the actual post-correction link-validation totals and demonstrate that all current operational records agree.

### E. Preservation audit

Explicitly confirm:

- Formula inventory preserved.
- Parameter inventory preserved.
- B-03 carry-ins preserved.
- B-04 production hashes unchanged.
- Production amendment manifest still empty.
- D-014 policy unchanged.
- Historical decisions preserved.
- Previous correction archives preserved.

### F. Git and repository status

Report actual Git status and any modified or untracked files relevant to the correction.

Do not claim a clean repository unless verified.

Do not perform Git operations.

### G. Final completion assessment

Choose one:

- COMPLETE — ALL REQUIREMENTS VERIFIED.
- PARTIALLY COMPLETE — SPECIFIC DEFECTS REMAIN.
- NOT COMPLETE — CRITICAL REQUIREMENTS FAILED.

Do not equate documentation completion with owner acceptance.

Do not declare Prompt 14A owner-accepted. That remains the owner's decision.

## 10. STRICT SCOPE BOUNDARY

This is the final targeted Prompt 14A correction.

Do not restart the original Prompt 14A work.

Do not redesign the numerical architecture.

Do not rewrite the nine formula registers.

Do not change formulas or numerical values.

Do not expand the assignment into unrelated security, gameplay, database or implementation work.

Do not create another broad correction prompt unless the completed work reveals a genuinely independent critical defect that cannot be resolved within this assignment.

Do not manufacture defects or unnecessary correction cycles.

If all requirements pass, report completion and recommend final Prompt 14A owner acceptance.

**PROMPT 14B REMAINS NOT AUTHORIZED / NOT STARTED.**

Only the owner may authorize Prompt 14B.

---

# FINAL EXPECTATION

The purpose of this correction is to close Prompt 14A properly.

An unrelated existing document must never be sufficient to authorize a fabricated numerical amendment.

Legitimate, adequately evidenced and properly authorized amendments must continue to work.

All current QA counts must agree with the final actual validation execution.

Preserve the completed numerical foundation and all historical project decisions.

**Fix only what is demonstrably defective. Verify it independently. Then stop.**
