# PROMPT 14B-C1-R1-R1 — END-TO-END SOURCE-REFERENCE VALIDATION, ADVERSARIAL MUTATION TESTING AND FINAL GIT-STATUS RECONCILIATION

**Archive status:** Archived on 2026-11-17 from the owner-supplied correction assignment in the authorized working session. The archived text preserves the complete requirements, boundaries, acceptance criteria and closeout-report specification. The archive header records provenance; no provenance paragraph is added to the body.
**Supplied by:** project owner, 17 November 2026.
**Parent:** PROMPT 14B — B-04 Economy, Resources, Income and Treasury.
**Previous assignment:** PROMPT 14B-C1-R1.
**Outcome:** [Prompt 14B-C1-R1-R1 closeout report](../stage-2/28_prompt_14B-C1-R1-R1_closeout_report.md); [progress log §116](../stage-2/06_stage_2_progress_log.md).

---

# NATION SUPREMACY — PROMPT 14B-C1-R1-R1
## END-TO-END SOURCE-REFERENCE VALIDATION, ADVERSARIAL MUTATION TESTING AND FINAL GIT-STATUS RECONCILIATION

**Project:** Nation Supremacy
**Parent assignment:** PROMPT 14B — B-04 ECONOMY, RESOURCES, INCOME AND TREASURY
**Previous assignment:** PROMPT 14B-C1-R1 — FINAL SOURCE-REFERENCE INTEGRITY, DECISION-AUTHORITY WORDING, EVIDENCE-STATUS AND GIT-STATE RECONCILIATION
**Baseline snapshot:** Project X (112)
**Authorization:** Narrowly authorized final validator and QA correction
**Objective:** Eliminate the reproduced false-pass conditions in the Prompt 14B-C1 source-reference validator and establish independently reproducible end-to-end mutation coverage.

---

# PART 1 — MANDATORY GOVERNANCE

## 1.1 Read the complete governance policy

Before starting, read the entire:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Follow D-014 and all owner-reserved decision boundaries.

Also inspect:

- `docs/AI_HANDOFF.md`
- `docs/PROJECT_PROGRESS.md`
- `docs/DECISIONS.md`
- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/prompts/INDEX.md`

Do not modify the Autonomous Decision Policy.

## 1.2 Existing project authority

Preserve:

- Prompt 14A owner acceptance.
- Prompt 14B owner authorization.
- Prompt 14B economic analysis.
- All 49 B-04 parameter records.
- All 49 existing D-014 classifications.
- All existing numerical values and statuses.
- The 35-row cross-system consistency matrix.
- The separate contradiction register.
- The completed Prompt 14B-C1 and C1-R1 documentation corrections.

Do not reopen completed economic work.

## 1.3 Scope restrictions

This assignment authorizes only:

1. Correction of the source-reference validator.
2. Real end-to-end adversarial mutation tests.
3. Reference-resolution and semantic-evidence traceability improvements.
4. Accurate validator and test reporting.
5. Raw-versus-normalized Git-status reconciliation.
6. Necessary prompt archival and continuity updates.

It does not authorize:

- Economic formula changes.
- Numerical parameter changes.
- Starting-bundle changes.
- Production-chain changes.
- Tax or maintenance changes.
- B-04 redesign.
- B-05/B-06/B-07/B-09/B-10 redesign.
- Database migrations.
- Runtime implementation.
- New gameplay mechanics.
- Modification of D-014.
- Prompt 14C or any subsequent Prompt 14 assignment.

The owner retains Git commit authority.

Do not stage, commit, amend, reset, rebase, push or rewrite Git history.

Work in the existing live repository, not an uploaded ZIP.

---

# PART 2 — REPRODUCE THE PROJECT X (112) FALSE-PASS DEFECTS FIRST

The previous independent audit reproduced two false-pass conditions using isolated copies of the Project X (112) documentation.

These are established regression cases and must be reproduced before changing the validator.

## 2.1 Attack A — Nonexistent economic source identifier

Original valid crosswalk reference:

`ECN-214`

Mutation:

`ECN-999`

The mutated identifier does not exist in the applicable authoritative B-04 source.

Previous actual result:

`PASS: 1330/1330`

This was a false acceptance.

Required result:

The production closeout validator must reject the mutated crosswalk with a clear source-reference error.

## 2.2 Attack B — Nonexistent validator filename

Original valid reference:

`14B_verify_b04_economy.py`

Mutation:

`14B_nonexistent_economy.py`

The mutated filename does not exist in the authoritative validator location.

Previous actual result:

`PASS: 1330/1330`

This was another false acceptance.

Required result:

The production closeout validator must reject the mutated filename and identify the invalid path.

## 2.3 Reproduce through the real production entry point

Do not reproduce these attacks by calling helper predicates directly.

Use:

`python qa_backups/14B_C1_validate_closeout.py`

Run it using the appropriate `docs` working directory and the exact documented production invocation.

The mutation must occur in the actual crosswalk source document in a temporary copy of the repository.

Then invoke the complete production validator against that mutated copy.

The validator must return a nonzero exit code and a meaningful diagnostic.

Restore the valid baseline and confirm that the same production entry point passes.

These two cases are mandatory permanent regression tests.

---

# PART 3 — REBUILD SOURCE-REFERENCE VALIDATION PROPERLY

## 3.1 Audit the current validator

Inspect:

`docs/qa_backups/14B_C1_validate_closeout.py`

Audit:

- `check_crosswalk()`
- `ecn_ids()`
- `fec_ids()`
- `fwr_ids()`
- `check_local_link()`
- `local_link_targets()`
- Existing D-014 validation.
- Existing parameter-record validation.
- Existing cross-system matrix validation.
- Existing evidence-dimension checks.
- Current self-test implementation.

Identify every reference field that is currently checked only for non-empty text rather than actual target resolution.

Do not replace the whole validator without evidence that replacement is necessary.

Preserve useful existing validation architecture and checks.

## 3.2 Establish authoritative source registries

Build or use a deterministic reference resolver for each identifier namespace found in the actual Prompt 14B QA crosswalk.

The reference resolver must use authoritative source documents, not arbitrary text matches anywhere in the repository.

At minimum inspect and resolve:

**A. Decision identifiers**

Source:

`docs/DECISIONS.md`

Validate that every cited D-014 decision identifier:

- Exists as an actual decision record.
- Has a valid authoritative record location.
- Is not confused with a similar number or unrelated text.
- Has the correct current or superseded status.
- Has the authority claimed by the crosswalk.

**B. B-04 economic identifiers**

Authoritative sources include:

- `docs/stage-2/10_economy_resources_treasury_and_finances.md`
- `docs/stage-2/10_economic_formula_and_balance_register.md`

Resolve all applicable `ECN-*` identifiers against their actual authoritative records.

Resolve all applicable `F-EC-*` formulas against the correct formula register.

Reject nonexistent identifiers.

**C. Warfare identifiers**

Resolve applicable `F-WR-*` identifiers against the actual authoritative B-10 source documents.

Do not assume an identifier belongs to a file merely because a similarly named file exists.

Inspect the real formula register and identify the correct source location.

For example, the existing `F-WR-036` military Food boundary must point to its actual authoritative specification.

**D. Other formula and requirement identifiers**

For any additional identifier namespace in the crosswalk:

1. Identify its authoritative register.
2. Establish the actual record structure.
3. Build an appropriate deterministic resolver.
4. Validate every reference against that source.

Do not invent namespaces.

## 3.3 Reference-validation architecture

The validator must distinguish the following conditions:

1. Reference exists and resolves correctly.
2. Reference exists but points to an incorrect or irrelevant source.
3. Reference exists but is superseded.
4. Reference is missing.
5. Reference is malformed.
6. Reference is fabricated.
7. Source exists but its relevant section does not.
8. Source is outside the authorized scope.
9. Reference requires human semantic review.

Do not classify every existing string as valid evidence.

## 3.4 Crosswalk-specific validation

Inspect every row of:

`docs/stage-2/22_numerical_baseline_qa_report.md`

In particular:

`Prompt 14B — Detailed Evidence Crosswalk`

For every crosswalk row, validate:

- QA category.
- Source document.
- Source section.
- Formula identifiers.
- Parameter identifiers or source record references.
- Decision identifiers.
- Validator filenames.
- Test filenames.
- Completion-report references.
- Execution evidence references.
- Status claims.

Every reference must resolve to a real source.

Where a reference is a file path, check that the file exists under the correct repository location.

Where a reference is a heading, check that the actual heading exists.

Where a reference is a formula or decision identifier, check that the identifier exists in its authoritative register.

Where a reference identifies a test or validator, check that the actual test or validator file exists.

Where a reference identifies an executed test result, verify that the claimed execution evidence exists and is associated with that test.

Do not accept a crosswalk reference because its field merely contains non-empty text.

## 3.5 File path safety

Validate that repository-relative paths:

- Resolve within the intended repository.
- Exist.
- Do not escape the repository through path traversal.
- Are not silently redirected to similarly named files.
- Use the correct case where the project expects case-sensitive paths.

Do not invent replacement locations for missing references.

Record unresolved source references accurately.

---

# PART 4 — SEMANTIC RELEVANCE AND EVIDENCE AUTHORITY

Reference existence is not the same as semantic correctness.

For example, a real D-046 decision record may exist, but it does not automatically support an unrelated tax parameter.

The validator and supporting documentation must distinguish:

**Reference existence:** Does the source exist?

**Reference integrity:** Does the cited identifier or heading resolve to the correct source?

**Authority:** Is the referenced source authorized to establish the claimed decision or rule?

**Relevance:** Does the cited source actually support this particular parameter, formula or QA claim?

**Execution evidence:** Has the referenced test or review actually been performed?

## 4.1 Human semantic review

Do not pretend unrestricted natural-language relevance can be proven by a basic regex.

Where automated semantic verification is not reliable, establish an explicit review record containing:

- Crosswalk row identifier.
- Source document.
- Cited section or record.
- Claim being supported.
- Reason the source is relevant.
- Authority of the source.
- Reviewer identity, when actual review has occurred.
- Review date.
- Review outcome.
- Outstanding uncertainty.

Do not invent human reviewer identities or approval.

A planned review must remain planned.

A missing reviewer must not be represented as a completed review.

## 4.2 D-014 authority integrity

Preserve all 49 existing B-04 parameter classifications.

The current classifications are:

| Category | Existing records |
|---|---:|
| A | 0 |
| B | 0 |
| C | 49 |
| D | 0 |

These classifications must not be changed merely to make the validator pass.

Keep numerical statuses separate from D-014 categories.

In particular:

- Category B is not equivalent to owner approval.
- Category C remains evidence-dependent and provisional.
- Category A remains owner-reserved.
- Category D remains owner-only for applicable external, costly or irreversible actions.

Do not misrepresent confirmed Category B structural decisions as owner-approved constraints.

Preserve the existing distinction between provisional parameter values and confirmed design structures.

## 4.3 Evidence-status integrity

Preserve the seven independent evidence dimensions:

1. Documentation.
2. Numerical validation.
3. Integration consistency.
4. Runtime implementation.
5. Migration.
6. Gameplay balance.
7. Playtesting.

Do not permit a reference to a planned test to satisfy a claim of executed validation.

Do not permit a document reference to establish runtime implementation.

Do not permit arithmetic tests to establish gameplay balance.

Preserve the actual evidence statuses recorded in the current numerical baseline QA report.

---

# PART 5 — REAL END-TO-END ADVERSARIAL MUTATION TESTING

This is the central deliverable of the assignment.

## 5.1 Required test methodology

Every adversarial test must:

1. Start from a known valid copy of the actual relevant project documents.
2. Confirm that the unmodified production validator passes.
3. Create a separate temporary copy of the required source documents.
4. Apply one deliberate mutation to a real source record, crosswalk row, reference or evidence claim.
5. Run the exact production validator against the mutated copy.
6. Capture the exit code and diagnostic.
7. Confirm that the validator rejects the mutation for the intended reason.
8. Restore the clean fixture.
9. Re-run the validator and confirm that it passes.

The tests must execute the same validator used for normal project closeout.

A test that merely calls `check_local_link("missing.md")` is not sufficient.

A test that directly calls `ecn_ids()` or `fwr_ids()` with a hard-coded value is not sufficient.

A test that checks only whether a helper returns `False` is not sufficient.

A mutation test is complete only when it demonstrates that the actual production entry point rejects the mutated repository content.

## 5.2 Mandatory mutation cases

Implement at least the following real end-to-end mutation tests.

### Case 1 — Fabricated ECN identifier

Replace a genuine crosswalk ECN identifier with `ECN-999`.

Expected: production validator rejects it.

### Case 2 — Fabricated F-EC identifier

Replace a valid B-04 formula reference with a nonexistent F-EC identifier.

Expected: production validator rejects it.

### Case 3 — Fabricated F-WR identifier

Replace a valid B-10 formula reference with a nonexistent F-WR identifier.

Expected: production validator rejects it.

### Case 4 — Nonexistent decision identifier

Replace a valid D-014 decision reference with an identifier that does not exist in the authoritative decision register.

Expected: production validator rejects it.

### Case 5 — Nonexistent source file

Replace an existing source-document path with a nonexistent repository-relative path.

Expected: production validator rejects it.

### Case 6 — Nonexistent heading

Retain a valid document path but replace its section heading reference with a nonexistent heading.

Expected: production validator rejects it.

### Case 7 — Nonexistent validator filename

Replace a real validator filename with:

`14B_nonexistent_economy.py`

Expected: production validator rejects it.

### Case 8 — Stale or superseded reference

Mutate a current reference so that it points to a superseded or obsolete record while still appearing syntactically valid.

Expected: production validator identifies the incorrect status or requires explicit historical-status classification.

### Case 9 — Missing evidence reference

Remove a required decision or evidence reference from a parameter or crosswalk row.

Expected: production validator rejects it or marks the record explicitly unresolved according to its defined status rules.

### Case 10 — False owner approval

Change a confirmed Category B structural decision into an unsupported owner-approved claim.

Expected: production validator rejects the unsupported authority claim or requires a genuine owner-approval evidence record.

### Case 11 — Fabricated execution evidence

Change a planned playtest or unexecuted validator result into a completed execution claim without an execution record.

Expected: production validator rejects the claim.

### Case 12 — Incorrect D-014 category

Change a parameter's D-014 category to an invalid or unsupported category.

Expected: production validator rejects it.

### Case 13 — Numerical-status/category substitution

Replace a D-014 category with a numerical status such as `PROVISIONAL VALUE`.

Expected: production validator rejects it.

### Case 14 — Invented source parameter identifier

Introduce a fabricated source parameter ID into a record whose established source-ID convention is `None`.

Expected: production validator rejects it unless a genuine authoritative source identifier exists.

### Case 15 — Duplicate or ambiguous reference

Create a duplicate or ambiguous reference so the validator cannot establish which authoritative source record is intended.

Expected: production validator rejects the ambiguity or requires explicit resolution.

## 5.3 Positive controls

For every relevant mutation family, include at least one valid counterpart.

Examples:

- Valid ECN identifier passes.
- Valid F-EC identifier passes.
- Valid F-WR identifier passes.
- Existing decision identifier passes.
- Existing source path and heading pass.
- Properly classified historical/superseded reference passes when explicitly labelled historical.
- Properly documented provisional parameter passes.
- Properly documented planned playtest passes when represented as planned rather than completed.
- Existing no-source-ID convention passes.

The validator must reject invalid material without rejecting valid existing project content.

## 5.4 Mutation test reporting

Report each case separately:

| Field | Required |
|---|---|
| Mutation ID | Unique |
| Source file | Exact path |
| Original content | Actual valid value |
| Mutated content | Actual invalid value |
| Expected result | REJECT |
| Actual exit code | Recorded |
| Actual diagnostic | Recorded |
| Production entry point used | Exact command |
| Result | PASS/FAIL |

A mutation test must be marked PASS only when the production validator rejects the deliberately invalid repository state for the correct reason.

Do not count an exception or unrelated parser crash as a successful semantic rejection.

Do not aggregate helper-function unit tests into the production mutation total.

---

# PART 6 — TEST IMPLEMENTATION AND ISOLATION

## 6.1 Temporary test environment

Run mutation tests against temporary repository fixtures.

Do not modify the live authoritative documents during adversarial tests.

Do not modify the owner's working files.

Use a deterministic fixture or temporary copy of the smallest complete set of necessary repository documents.

Every test must begin with a fresh or restored valid fixture.

## 6.2 Production entry-point compatibility

The validator must support a clear way to validate a temporary fixture.

Use a documented repository-root or fixture-root argument if necessary.

Preserve the normal existing invocation for ordinary project validation.

For example, an explicit fixture-root option may be used, but only implement it in a manner consistent with the existing validator architecture.

Do not hard-code `/tmp`, a particular developer username, or the current audit environment.

Do not create a separate weakened testing validator.

The production validation logic and mutation tests must share the same reference-resolution implementation.

## 6.3 Failure diagnostics

Every rejected mutation should identify:

- The affected crosswalk row or parameter.
- The invalid reference.
- The expected source namespace.
- The authoritative register or source.
- The reason the reference failed.

Do not return only a generic PASS/FAIL count.

---

# PART 7 — REFERENCE-RESOLVER REGRESSION PROTECTION

Add focused tests for the actual resolver architecture.

At minimum verify:

1. Valid decision IDs resolve to their actual records.
2. Invalid decision IDs are rejected.
3. Valid ECN IDs resolve to their authoritative economic specification entries.
4. Invalid ECN IDs are rejected.
5. Valid F-EC IDs resolve to the B-04 formula register.
6. Invalid F-EC IDs are rejected.
7. Valid F-WR IDs resolve to the correct B-10 authoritative register.
8. Invalid F-WR IDs are rejected.
9. Valid source paths resolve correctly.
10. Nonexistent paths are rejected.
11. Valid headings resolve.
12. Nonexistent headings are rejected.
13. Duplicate identifiers are handled safely.
14. Superseded references are distinguishable from current references.
15. References from unrelated source systems are not incorrectly accepted.
16. Required references cannot be omitted silently.
17. Repository-relative path restrictions work.
18. No-source-ID parameter conventions remain intact.
19. Correct numerical statuses remain unchanged.
20. Valid existing cross-system rows continue to pass.

Do not create a second competing source registry if the project already has an authoritative structured mapping that can be safely extended.

Keep all source mappings auditable.

---

# PART 8 — PRESERVE AND REVALIDATE THE EXISTING 49 PARAMETER RECORDS

The 49 B-04 parameter records remain the existing authoritative scope.

Do not rebuild them.

Verify:

- All 49 records remain present.
- All 49 D-014 classifications remain valid.
- All current numerical statuses remain unchanged.
- Existing source ownership is preserved.
- Existing source identifiers are preserved.
- Missing source identifiers remain missing rather than fabricated.
- Decision references resolve.
- Source paths resolve.
- Evidence references resolve or remain explicitly unresolved.
- No owner approval is invented.

Required D-014 category distribution in the current baseline:

- Category A: 0.
- Category B: 0.
- Category C: 49.
- Category D: 0.

If actual source evidence reveals a genuine classification problem, document it precisely rather than silently changing it.

No category change is authorized merely to satisfy a validator.

---

# PART 9 — PRESERVE THE CROSS-SYSTEM MATRIX AND QA CROSSWALK

## 9.1 Cross-system matrix

Preserve all 35 existing dependency rows.

The previously verified matrix totals remain:

| Status | Records |
|---|---:|
| VERIFIED CONSISTENT | 27 |
| VERIFIED WITH DOCUMENTED LIMITATION | 4 |
| CONTRADICTION IDENTIFIED | 4 |
| NOT YET VERIFIED | 0 |
| TOTAL | 35 |

Do not change these classifications without independent evidence.

Do not mix the separate contradiction register into the matrix totals.

Preserve the out-of-scope B-06 findings.

## 9.2 QA evidence crosswalk

Preserve the 17 existing QA categories and seven evidence dimensions.

Make only changes necessary to connect existing crosswalk references to the authoritative resolver.

Do not duplicate the entire completion report.

Do not rewrite economic calculations.

Do not inflate the 17 categories or create unnecessary documentation.

The crosswalk must remain an accurate navigation and evidence map.

---

# PART 10 — RAW AND NORMALIZED GIT-STATUS RECONCILIATION

The Project X (112) audit found an important distinction.

The ZIP metadata reported:

- Branch: `main`.
- HEAD: `bff91193f946ce77f60da9a838d5d76364552ed5`.
- Raw modified tracked paths: 157.
- Untracked paths: 9.
- Staged paths: 0.
- Substantive changes after LF normalization: 25.
- Line-ending-only differences: 132.

The 132 line-ending differences must not be concealed inside the 25 substantive changes.

## 10.1 Required reporting

On the final live repository state, report separately:

1. Raw `git status --porcelain=v1 --untracked-files=all`.
2. Raw modified tracked path count.
3. Untracked path count.
4. Staged path count.
5. Substantive modified tracked path count after line-ending normalization.
6. Line-ending-only modified tracked path count.
7. Actual branch and HEAD.
8. Latest relevant commit history.

Use a reproducible normalization method.

Compare worktree files with the corresponding HEAD blobs after normalizing CRLF/LF line endings only.

Do not ignore other whitespace changes or substantive content changes.

Provide a complete list of the normalized substantive changed paths.

## 10.2 Owner commit reconciliation

The owner has reported that earlier Prompt 14B work was committed.

Verify the actual live repository.

If the claimed commit exists:

- Record the actual hash.
- Record the commit subject.
- Identify which Prompt 14B files are included.
- Explain why Project X (112) showed an older HEAD if relevant.

If the claimed commit cannot be verified:

- State that it cannot be verified from the actual repository.
- Do not fabricate a commit hash.
- Do not stage, commit, reset or modify history.

The coding AI must not commit any R1-R1 changes.

The owner will decide when to commit them.

---

# PART 11 — EXISTING VALIDATION SUITES

After implementation, run all relevant existing validation suites.

At minimum:

1. New end-to-end source-reference mutation suite.
2. Updated Prompt 14B-C1 closeout validator.
3. Prompt 14B economy validator.
4. B-04 arithmetic validator.
5. Prompt 14A numerical foundation validator.
6. Prompt 14A contract validator.
7. Original contract regression tests.
8. Trusted amendment security tests.
9. Metadata regression tests.
10. Decision-register tests.
11. Next-action tests.
12. Project-wide documentation validator.
13. Project-wide documentation-link checker.
14. Relevant B-09, B-10, B-11 and B-12 cross-system validators where affected by changed source references.

Use actual project commands and working directories.

Do not assume that an earlier passing result remains valid after source-reference changes.

Record actual output, exit code and test totals.

Keep the four inherited historical validator failures documented:

- Politics arithmetic: 878/879.
- 11A research: 29/30.
- 09A alliance: 941/943.
- 09B alliance semantic: eight historical frozen-reference failures.

Do not weaken their historical controls merely to make this assignment pass.

---

# PART 12 — FINAL DOCUMENTATION AND REPORTING

Update only the records affected by the R1-R1 correction.

Relevant documents may include:

- `docs/qa_backups/14B_C1_validate_closeout.py`
- The new end-to-end mutation test module.
- The Prompt 14B-C1/R1 closeout report.
- `docs/stage-2/22_numerical_parameter_inventory.md`, only if necessary.
- `docs/stage-2/22_numerical_baseline_qa_report.md`, only if necessary.
- `docs/stage-2/25_prompt_14B_b04_economy_completion_report.md`, only if necessary.
- `docs/PROJECT_PROGRESS.md`
- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/AI_HANDOFF.md`
- `docs/prompts/INDEX.md`

Create the permanent prompt archive:

`docs/prompts/prompt_14B-C1-R1-R1_end_to_end_source_reference_validation_and_adversarial_mutation_testing.md`

Preserve the original Prompt 14B, C1 and R1 archives.

Do not create unnecessary duplicate registers or reports.

## 12.1 Final closeout report

Create a dedicated R1-R1 completion report following existing conventions.

It must include:

### A. Original defect reproduction

- ECN-999 attack.
- Nonexistent validator filename attack.
- Production validator commands.
- Actual rejection results.

### B. Reference-resolver coverage

- Decision identifiers checked.
- ECN identifiers checked.
- F-EC identifiers checked.
- F-WR identifiers checked.
- Other namespaces checked.
- Source paths checked.
- Headings checked.
- Test filenames checked.
- Unresolved references, if any.
- Human semantic reviews still required.

### C. Adversarial testing

- Number of real end-to-end mutation tests.
- Number passed.
- Number failed.
- Positive control results.
- Full production-validator invocation evidence.
- Exact expected and actual diagnostics.

### D. Baseline integrity

- 49 parameter records.
- 49 existing D-014 classifications.
- Existing numerical statuses.
- 35 cross-system dependency rows.
- Correct matrix totals.
- 17 QA categories.
- Seven evidence dimensions.

### E. Regression testing

- All actual commands.
- Exit codes.
- Pass/fail totals.
- Inherited failures.
- New regressions.
- Tests not run and reasons.

### F. Git-state reconciliation

- Raw modified path count.
- Untracked count.
- Staged count.
- Substantive normalized modified path count.
- EOL-only modified path count.
- Complete substantive changed-file list.
- Branch.
- HEAD.
- Owner commit evidence.
- Confirmation no Git modifications were staged or committed.

### G. Final assessment

Use one exact status:

- `COMPLETE`
- `PARTIALLY COMPLETE — OWNER REVIEW REQUIRED`
- `NOT COMPLETE`

Do not claim completion simply because the baseline validator passes.

The actual adversarial mutation cases must fail through the production entry point.

---

# PART 13 — ACCEPTANCE CRITERIA

Prompt 14B-C1-R1-R1 is complete only when:

1. Both original Project X (112) false-pass attacks are independently reproduced before correction.
2. ECN, F-EC, F-WR, decision, document, heading, test and evidence references are actually resolved against authoritative repository sources.
3. Nonexistent references are rejected by the full production validator.
4. At least 15 real end-to-end mutation cases execute against temporary source-document copies.
5. Each mutation produces the correct nonzero exit result and diagnostic.
6. Valid positive controls continue to pass.
7. Helper-function tests are not misrepresented as production mutation tests.
8. Semantic relevance and authority limitations are honestly recorded.
9. All 49 B-04 parameter records and their existing numerical statuses are preserved.
10. All 35 cross-system dependency rows and their correct status totals are preserved.
11. The 17 QA categories and seven evidence dimensions remain accurate.
12. Existing Prompt 14B economic analysis remains unchanged.
13. All applicable existing validators and regressions are executed.
14. Raw Git counts and line-ending-normalized substantive counts are independently reported.
15. The claimed owner commit is verified against actual repository evidence or explicitly recorded as unverified.
16. Prompt archive and handoff are updated.
17. No Git changes are staged or committed.
18. Prompt 14C and subsequent phases remain unauthorized.

**A PASS from the main validator is not sufficient without the end-to-end mutation evidence.**

**A PASS from helper-function unit tests is not sufficient without production-entry-point mutation tests.**

**A nonzero exit caused by an unrelated crash is not a successful security rejection.**

---

# PART 14 — FINAL EXECUTION ORDER

Execute in this order:

1. Read complete D-014 governance.
2. Verify live repository state and previous commit history.
3. Reproduce both Project X (112) false-pass attacks.
4. Audit reference namespaces and authoritative sources.
5. Correct the production reference resolver.
6. Add real end-to-end mutation tests in isolated temporary fixtures.
7. Add positive controls.
8. Verify all 49 parameter records and all cross-system references.
9. Preserve the 35-row matrix and seven QA evidence dimensions.
10. Execute all relevant regression and project-wide validators.
11. Rerun documentation-link validation.
12. Reconcile raw and normalized Git counts.
13. Update the dedicated completion report.
14. Archive this complete R1-R1 assignment.
15. Update project handoff and continuity records.
16. Leave every change unstaged and uncommitted.

**FINAL OBJECTIVE: ENSURE THAT THE NATION SUPREMACY PROMPT 14B SOURCE-REFERENCE VALIDATOR CANNOT ACCEPT FABRICATED, NONEXISTENT, STALE OR MISREPRESENTED CROSS-SYSTEM EVIDENCE MERELY BECAUSE A REFERENCE FIELD CONTAINS TEXT.**

The owner will independently inspect the next ZIP snapshot before deciding whether Prompt 14B-C1-R1-R1 is formally accepted.

**Prompt 14C is not authorized by this assignment.**
