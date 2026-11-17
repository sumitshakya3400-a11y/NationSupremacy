# PROMPT 14A-C1-R1-R1-C1-R1-C1-R1-R1 — EVIDENCE CONTRADICTION DETECTION, SUBSTANTIVE SUPPORT VALIDATION AND FINAL QA RECONCILIATION

## 1. OBJECTIVE

Complete the remaining defects discovered during the independent audit of Project X (102).

This is a narrowly scoped corrective assignment within Prompt 14A.

The objectives are:

1. Correct the evidence validator's ability to distinguish genuinely supporting evidence from contradictory, misleading, irrelevant and insufficient evidence.
2. Prevent a genuine quotation from an authorized document from being used to support a proposition that the quotation actually contradicts.
3. Add permanent regression tests reproducing the exact Project X (102) D-999 false acceptance.
4. Preserve all legitimate Category A, B and C amendment workflows.
5. Reconcile the outstanding documentation-link totals across the final B-14, QA report and applicable current project records.

Do not restart Prompt 14A.

Do not redesign the numerical architecture.

Do not modify formulas or game-balance values.

The purpose is to close the remaining evidence-validation and documentation-reconciliation defects.

## 2. MANDATORY GOVERNANCE

Before starting, read the entire:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Follow the actual D-014 requirements and Category A, B, C and D authority boundaries.

Do not modify the Autonomous Decision Policy.

Preserve the distinction between:

- OWNER-APPROVED VALUE.
- PROVISIONAL VALUE.
- DESIGN PROPOSAL.
- NEEDS PLAYTESTING.

Do not invent owner approval.

A validator pass, evidence quotation, source fingerprint, decision-register record or regression fixture does not constitute owner authorization.

Category A decisions remain subject to owner authority.

Category B decisions must follow the actual working-AI decision authority and recording requirements.

Category C decisions must remain provisional, with safe working defaults and named evidence or test requirements.

Do not turn provisional decisions into approved decisions.

### Workflow restrictions

- Work in the existing live project repository.
- Do not use an uploaded ZIP as the working project.
- Do not create duplicate project folders.
- Do not overwrite unrelated existing work.
- Do not stage, commit, push, reset, revert or discard Git changes.
- Do not modify protected Git history.
- Do not implement gameplay, frontend, backend, database, SQL, API, migration, security or deployment changes.
- Do not modify the production B-04 formula clauses.
- Do not change the two current B-04 source hashes.
- Do not populate the production amendment manifest.
- Do not reopen Prompt 13.
- Do not authorize Prompt 14B.

Inspect existing files and architecture before deciding which files require modification.

## 3. PROJECT X (102) — EXACT REMAINING DEFECT

### 3.1 Previous correction that works

Project X (102) successfully rejects the original Project X (101) D-998 attack.

The original unrelated-document evidence attack is therefore covered.

Do not remove or weaken that protection.

### 3.2 Newly reproduced critical defect

The independent audit discovered that the current `_evidence_supports()` implementation still relies on insufficient semantic checks.

The validation mechanism checks:

- Authorized evidence location.
- Resolution of the cited section.
- Whether a quotation appears in the cited section.
- Token overlap between the evidence quotation and the recorded support claim.
- Whether the rationale contains sufficient-looking text.

These checks do not reliably establish that evidence supports the proposed amendment.

### 3.3 Exact Project X (102) attack

The independent audit performed the following temporary mutation:

1. Modified `F-EC-000b` to permit binary floating-point calculations.
2. Updated the formula's source fingerprint.
3. Created a complete-looking Category B decision, D-999.
4. Included the previous rule.
5. Included the replacement rule.
6. Included alternatives.
7. Included rationale.
8. Included consequences.
9. Included reopening conditions.
10. Cited the authorized B-14 §8.2 evidence location.
11. Supplied an exact quotation from that location:

   "No binary floating point; no fractional carry stated"

12. Claimed that the quotation supported permitting binary floating-point calculations.
13. Supplied a matching amendment manifest.

The quotation was genuine.

The evidence location was authorized.

The quotation's meaning nevertheless contradicted the proposed amendment.

**Actual Project X (102) result:**

- Validator 14A-45: falsely passed.
- Validator 14A-46: falsely passed.
- Validator 14A-48: falsely passed.

The validator accepted a proposed change that its own cited source contradicted.

This is the principal defect to fix.

## 4. CORRECTION A — ACTUAL EVIDENCE SUPPORT AND CONTRADICTION VALIDATION

### 4.1 Required principle

The validator must distinguish:

- SUPPORTS: The evidence positively supports the precise proposition being asserted.
- CONTRADICTS: The evidence conflicts with the proposed proposition.
- QUALIFIES: The evidence supports the proposition only under specific conditions or limitations.
- CONTEXT_ONLY: The evidence provides background but does not establish the proposition.
- NOT_ESTABLISHED: The cited evidence does not establish the proposition.

Only genuinely sufficient SUPPORTS evidence may satisfy the supporting-evidence requirement.

A quotation containing similar words must not automatically be classified as supporting evidence.

### 4.2 Validate the actual proposition

The evidence validator must evaluate the relationship between:

1. The affected source clause.
2. The previous rule.
3. The replacement rule.
4. The proposition that the amendment seeks to establish.
5. The exact evidence passage.
6. The evidence passage's meaning and context.
7. The decision rationale.
8. The asserted consequences.
9. The decision's authority under D-014.
10. The amendment manifest and source fingerprint.

The validator must detect relevant differences involving:

- Negation.
- Permission versus prohibition.
- Required versus optional behaviour.
- Positive versus negative claims.
- Scope.
- Conditions.
- Exceptions.
- Numerical constraints.
- Units.
- Timing.
- Quantifiers.
- Modality.
- Preconditions and limitations.

The mechanism must not mistake a prohibition for permission, a restriction for an authorization, or an absence of information for affirmative supporting evidence.

### 4.3 Exact contradiction that must be recognized

The Project X (102) source quotation:

"No binary floating point"

expresses a prohibition.

The proposed replacement:

"Binary floating point calculations are permitted"

expresses permission.

The cited statement cannot support the proposed replacement.

It directly contradicts it.

The validator must reject this relationship even when:

- The evidence document is authorized.
- The source section exists.
- The quotation is exact.
- The source hash is correct.
- The decision record is structurally complete.
- The amendment manifest matches.
- The quotation contains substantial keyword overlap.

The second clause, "no fractional carry stated", must not be treated as affirmative evidence that fractional or floating-point arithmetic is permitted.

Absence of a restriction in a source document is not automatically proof of permission.

### 4.4 Implement an auditable evidence-validation mechanism

Inspect the existing source contracts, evidence records, validator architecture and B-04 controlled clauses.

Implement the strongest deterministic, auditable mechanism compatible with the existing architecture.

Where appropriate, use structured evidence claims and source-content contracts that explicitly identify:

- Source document.
- Exact source locator.
- Relevant source content.
- Source provenance.
- Source fingerprint.
- Proposition being established.
- Relevant subject and scope.
- Positive or negative polarity.
- Conditions and qualifications.
- Whether the source supports, contradicts or merely contextualizes the proposition.
- Applicable affected clause.
- The basis for the evidence relationship.

The relationship between evidence and proposition must be independently established through the project's authorized evidence-source mechanism.

Do not allow the amendment's own decision record to declare its cited evidence supportive without independent validation.

Do not allow an unverified source annotation to authorize its own amendment.

Any authoritative evidence mapping or source-contract changes must follow D-014 authority and documentation requirements.

Do not manufacture owner-approved evidence mappings.

If evidence relevance cannot be established using authorized source information, fail closed.

### 4.5 Source-context verification

The validator must inspect more than isolated quotations.

It must establish that:

- The quotation is genuinely present.
- Its surrounding context has been considered.
- Negation and qualifications have not been omitted.
- The claimed proposition is compatible with the actual source content.
- The document does not contain a contrary statement that invalidates the claimed inference.
- The cited passage concerns the relevant subject and scope.
- The evidence has not been selectively quoted to reverse its meaning.

Exact quotation verification is necessary but not sufficient.

### 4.6 Deterministic validation requirement

Do not rely exclusively on:

- Token overlap.
- Keyword matching.
- Evidence-description length.
- Generic rationale wording.
- Path existence.
- Hash matching.
- Quotation presence.
- Unverified free-text declarations that evidence supports an amendment.

The validator must use verifiable source-backed relationships.

Do not rely on an external AI model or an unrepeatable subjective judgement at runtime.

The validation result must be deterministic, reproducible, explainable and auditable.

If a proposition cannot be reliably evaluated, do not silently accept it. Return an explicit evidence-validation failure.

## 5. CORRECTION B — PERMANENT NEGATIVE REGRESSION TESTS

All negative regression tests must run in isolated temporary fixtures.

Do not modify the real production formula clauses or production amendment manifest.

### 5.1 Exact D-998 regression

Preserve the original Project X (101) negative test.

Expected result:

REJECT — UNRELATED EVIDENCE.

Rejection must be attributable to the evidence relevance failure, not unrelated structural errors.

### 5.2 Exact D-999 regression

Permanently reproduce the complete Project X (102) attack.

Test:

- `F-EC-000b` modified to permit binary floating-point calculations.
- Updated source fingerprint.
- Complete Category B D-999 decision.
- Previous rule.
- Replacement rule.
- Alternatives.
- Rationale.
- Consequences.
- Reopening conditions.
- Authorized B-14 §8.2 evidence locator.
- Genuine quotation: "No binary floating point; no fractional carry stated".
- Misleading claim that the quotation supports floating-point permission.
- Matching amendment manifest.

Expected result:

**REJECT — EVIDENCE CONTRADICTS THE PROPOSED AMENDMENT.**

The rejection must specifically identify the contradiction or unsupported evidence relationship.

Do not let an unrelated authorization or syntax failure make this test pass.

### 5.3 Additional negative tests

Create permanent regression coverage for:

1. Genuine quotation with reversed meaning.
2. Explicit prohibition presented as permission.
3. Explicit permission presented as prohibition.
4. Evidence that supports only part of the proposed amendment.
5. Evidence whose conditions are omitted from the decision.
6. Evidence with misleading surrounding context.
7. Contradictory statements in the same relevant source.
8. Evidence that establishes background but not the proposed proposition.
9. Absence of a statement falsely presented as affirmative authorization.
10. Incorrect numerical scope.
11. Incorrect units or timing.
12. A quotation that matches but concerns a different subject.
13. A fabricated supporting excerpt.
14. An altered source document with a stale fingerprint.
15. An unauthorized attempt to change the evidence-support mapping.
16. A decision rationale that contradicts its actual cited source.

Every negative test must demonstrate rejection for the appropriate reason.

### 5.4 No special-case-only fix

Do not solve this by hardcoding only:

- D-999.
- F-EC-000b.
- The exact quotation.
- B-14 §8.2.
- One specific proposed replacement.

The validator must enforce the underlying general evidence-support principle.

The D-999 fixture is a permanent regression case, not the entire implementation.

## 6. CORRECTION C — POSITIVE REGRESSION PROTECTION

Do not make all amendments fail in order to achieve fail-closed validation.

Preserve and execute positive fixtures.

### Category A

Test a legitimate owner-authorized amendment fixture.

Requirements:

- Correct Category A classification.
- Required owner authorization evidence.
- Genuine supporting evidence.
- Complete decision information.
- Matching amendment manifest.

Use temporary test-only approval data.

Do not create real owner approvals in production registers.

### Category B

Test a legitimate ordinary design amendment.

Requirements:

- Correct Category B classification.
- Appropriate working-AI authority.
- Genuine evidence supporting the exact proposed change.
- Complete rationale.
- Alternatives and consequences.
- Reopening conditions.
- Matching amendment manifest.

### Category C

Test a legitimate provisional amendment.

Requirements:

- Correct Category C classification.
- Safe working default.
- Named evidence or test requirement.
- Provisional status.
- Appropriate reopening conditions.

It must not be promoted automatically to OWNER-APPROVED VALUE.

### Baseline

Verify that the unchanged Project X (102) production baseline passes.

Positive test fixtures must be isolated and must not introduce actual production decisions, changes to formula source clauses or nonempty production amendment manifests.

## 7. CORRECTION D — PRESERVE ALL EXISTING VALIDATOR COVERAGE

Project X (102) independently produced:

| Existing test suite | Baseline |
|---|---:|
| Numerical foundation validator | 52/52 |
| Self-tests | 124/124 |
| Decision-register tests | 12/12 |
| Next-action tests | 27/27 |
| Final project validator | PASS |

Preserve all existing checks.

New regression tests must be additive.

Do not:

- Delete existing test cases.
- Weaken old assertions.
- Suppress errors.
- Convert failures into expected failures.
- Skip negative cases.
- Change expected values merely to make tests pass.
- Reuse test identifiers improperly.

Run the complete existing self-test suite.

If a suite times out, report that honestly and provide its actual execution results. Never report incomplete execution as a pass.

## 8. CORRECTION E — FINAL DOCUMENTATION-LINK RECONCILIATION

### 8.1 Project X (102) actual baseline

The independent documentation-link validator returned:

| Measure | Project X (102) |
|---|---:|
| Markdown files | 129 |
| Total links | 4,363 |
| Local links | 3,981 |
| External links skipped | 382 |
| Anchors | 34 |
| Unresolved links | 0 |

However, B-14 CLOSURE-26/27 and numerical QA report §5.16 still reported:

- 4,360 total links.
- 3,978 local links.

The progress log correctly contained the actual X102 totals.

### 8.2 Required correction

After all evidence-validator changes, tests, documentation changes and prompt archival are complete:

1. Execute the actual documentation-link validator.
2. Capture its full execution result.
3. Record the actual Markdown file count.
4. Record the actual total-link count.
5. Record the actual local-link count.
6. Record the actual external-links-skipped count.
7. Record the actual anchor count.
8. Record the actual unresolved-link count.

Update all applicable current operational records, including:

- `docs/stage-2/22_formulas_and_balance.md`
- Numerical QA report §5.16.
- B-14 CLOSURE-26.
- B-14 CLOSURE-27.
- Current progress-log status.
- Applicable current continuity and index documents.

Inspect the repository for the actual report paths and use its existing naming conventions.

Every current operational report must refer to the same final validation execution.

Do not hardcode the Project X (102) baseline if the latest final execution produces different totals.

If documentation modifications alter link counts, rerun validation and reconcile again until the records are synchronized.

### 8.3 Historical preservation

Do not rewrite historical validation counts.

Do not change Project X (101) or Project X (102) audit records to make them appear to have contained the latest counts.

Update current operational records only.

Clearly distinguish historical snapshots from the latest authoritative execution.

## 9. PRESERVATION REQUIREMENTS

The following must remain protected:

| Item | Requirement |
|---|---|
| Active formula identifiers | 295 |
| Parameter inventory records | 393 |
| B-03 carry-in parameters | 20 |
| Numerical validator coverage | Preserve all 52 existing checks |
| Self-test coverage | Preserve all 124 existing tests |
| Decision-register tests | Preserve all 12 |
| Next-action tests | Preserve all 27 |
| Formula registers | Preserve all nine |
| B-04 source hashes | Unchanged |
| Production amendment manifest | Empty |
| D-014 policy | Unmodified |
| Historical decisions | Preserved |
| Earlier correction archives | Preserved |
| Canonical B-14 filename | 22_formulas_and_balance.md |

Do not alter:

- The 295 formula identifiers.
- The 393 parameter records.
- The 20 B-03 carry-in parameters.
- Original numerical ownership.
- Owner-reserved decisions.
- Existing approved or provisional classifications.
- Production formula clauses.
- The two current B-04 source hashes.
- The production amendment manifest.
- Historical progress entries.
- Earlier prompt archives.

Do not introduce new approved balance parameters.

Do not perform unrelated gameplay or implementation work.

## 10. PROMPT ARCHIVAL REQUIREMENTS

Create a new permanent correction prompt archive using this exact unique ID:

`14A-C1-R1-R1-C1-R1-C1-R1-R1`

Permanent archive path:

`docs/prompts/prompt_14A-C1-R1-R1-C1-R1-C1-R1-R1_evidence_contradiction_detection_and_final_qa_reconciliation.md`

Requirements:

1. Archive the complete correction prompt.
2. Update the prompt index.
3. Preserve all previous correction archives.
4. Never overwrite the Project X (101) or Project X (102) correction archives.
5. Do not duplicate the parent correction ID.
6. Verify the archived file exists.
7. Record its actual byte size.
8. Calculate and record its actual SHA-256.
9. Verify the prompt index points to the correct file.

Do not claim archival completion without checking the actual file and index.

## 11. FINAL INDEPENDENT VALIDATION

After all modifications and archival operations, run the following:

### Numerical foundation

- Verify all 295 active formula identifiers.
- Verify all 393 parameter records.
- Verify all 20 B-03 carry-in parameters.
- Verify both B-04 source hashes remain unchanged.
- Verify the production amendment manifest remains empty.

### Evidence validation

- Run the original D-998 negative regression.
- Run the exact D-999 negative regression.
- Run all additional negative evidence tests.
- Run legitimate Category A positive fixture.
- Run legitimate Category B positive fixture.
- Run legitimate Category C positive fixture.
- Run unchanged production baseline.
- Verify that the D-999 attack fails specifically because evidence contradicts the amendment.

### Existing test suites

- Numerical foundation validator.
- Complete self-test suite.
- Decision-register tests.
- Next-action tests.
- Final project validator.

### Documentation

- Execute the documentation-link validator after all final document changes.
- Reconcile all current QA reports.
- Verify the prompt archive and index.
- Verify historical counts have not been rewritten.

### Governance and repository

- Read the complete Autonomous Decision Policy.
- Verify no substantive policy changes.
- Read the actual Git status.
- Report all relevant modified and untracked files.
- Do not perform Git operations.
- Do not claim repository cleanliness unless independently established.

## 12. REQUIRED FINAL REPORT

Deliver a complete factual report.

### A. Evidence validator changes

Identify:

- Exact validator files changed.
- The mechanism used to establish evidence relevance.
- How contradictions are detected.
- How source context and qualifications are handled.
- How source provenance and fingerprints are verified.
- Why D-998 and D-999 are now rejected.

### B. Regression results

Provide actual results:

| Test | Expected |
|---|---|
| Project X (101) D-998 attack | REJECT |
| Project X (102) D-999 attack | REJECT |
| Genuine quotation with opposite meaning | REJECT |
| Prohibition presented as permission | REJECT |
| Partial evidence coverage | REJECT |
| Misleading context | REJECT |
| Fabricated quotation | REJECT |
| Stale evidence fingerprint | REJECT |
| Unauthorized evidence mapping change | REJECT |
| Valid Category A fixture | ACCEPT |
| Valid Category B fixture | ACCEPT |
| Valid Category C fixture | ACCEPT |
| Unchanged production baseline | PASS |

For every negative test, provide the actual rejection reason.

For every positive test, show that acceptance was achieved without weakening the evidence requirements.

### C. Validator coverage

Report actual results for:

- Numerical foundation validator.
- Existing self-tests.
- New evidence tests.
- Decision-register tests.
- Next-action tests.
- Final project validator.

Distinguish tests executed from tests merely present in the repository.

### D. Final QA counts

Provide the actual final documentation-link execution totals.

Identify the exact documents updated.

Demonstrate that every current operational report agrees.

### E. Preservation audit

Explicitly confirm:

- 295 formulas preserved.
- 393 parameter records preserved.
- 20 B-03 carry-ins preserved.
- Nine formula registers preserved.
- Both B-04 source hashes unchanged.
- Production amendment manifest empty.
- D-014 unchanged.
- Historical decisions preserved.
- Previous correction archives preserved.

### F. Git and archive status

Report:

- Actual modified tracked files.
- Actual untracked files.
- Correction archive path.
- Actual archive byte size.
- Actual SHA-256.
- Prompt index verification.

Do not modify Git history or stage files.

### G. Final completion assessment

Choose exactly one:

- COMPLETE — ALL REQUIREMENTS VERIFIED.
- PARTIALLY COMPLETE — SPECIFIC DEFECTS REMAIN.
- NOT COMPLETE — CRITICAL REQUIREMENTS FAILED.

Do not declare owner acceptance.

Only the owner can accept Prompt 14A.

## 13. STRICT SCOPE BOUNDARY

This is a narrowly scoped final evidence-validation and documentation-reconciliation correction.

Do not restart Prompt 14A.

Do not repeat already completed formula or parameter inventory work.

Do not rewrite the numerical architecture.

Do not alter formulas, numerical values or source hashes.

Do not modify D-014.

Do not create real project decisions to satisfy tests.

Do not introduce an unrelated security, gameplay, database or implementation assignment.

Do not create another broad correction cycle.

If an independent critical issue remains, explain its exact evidence and scope instead of expanding this assignment unnecessarily.

If all requirements pass, recommend final Prompt 14A owner acceptance.

**PROMPT 14B REMAINS NOT AUTHORIZED / NOT STARTED.**

Only the owner may authorize Prompt 14B.

---

# FINAL EXPECTATION

The central requirement is straightforward:

A genuine quotation from an authorized document must not be accepted as supporting evidence when its actual meaning contradicts the proposed amendment.

The validator must establish the substantive relationship between the cited evidence and the exact proposed change.

Legitimate, properly authorized and genuinely supported Category A, B and C amendments must continue to work.

All current documentation-link totals must agree with the actual final validator execution.

Preserve the completed numerical foundation and all historical decisions.

**Fix the demonstrated defects. Test them independently. Reconcile the documentation. Then stop.**
