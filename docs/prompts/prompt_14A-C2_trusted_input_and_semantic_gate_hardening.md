# NATION SUPREMACY — PROMPT 14A-C2
# TRUSTED AMENDMENT INPUTS, EVIDENCE REVALIDATION AND FINAL SEMANTIC GATE HARDENING

**Parent phase:** Prompt 14A — Numerical Foundation and Semantic Validation  
**Starting audit snapshot:** Project X (106)  
**Assignment type:** Targeted security hardening, adversarial regression and final QA reconciliation  
**Status:** Prompt 14A remains OPEN — NOT OWNER ACCEPTED  
**Prompt 14B:** NOT AUTHORIZED / NOT STARTED

---

# 1. MISSION

The independent audit of Project X (106) confirmed that the new canonical numerical-contract architecture represents substantial progress.

However, two additional false-acceptance vulnerabilities were independently reproduced against the actual production amendment-validation path.

### Finding 1 — Caller-controlled trusted inputs

The amendment-validation function accepts caller-supplied versions of authoritative validation inputs, including:

- Baseline contract.
- Evidence mappings.
- Schema.
- Lexicon.
- Decision-register contents.
- Owner authorizations.
- Projection template.

An amendment request must not be allowed to supply or replace its own trusted validation environment.

### Finding 2 — Incomplete material coverage

The existing `material_coverage()` implementation checks for expected fragments but does not account for everything between them.

An attacker can insert an additional contradictory material proposition into an otherwise valid candidate projection without the coverage validator detecting the insertion.

### Finding 3 — Evidence integrity is not consistently enforced

The canonical evidence registry is checked during production validation, but the amendment-validation path can subsequently accept caller-supplied evidence mappings without repeating the necessary integrity and provenance checks.

### Finding 4 — Authority sources can be substituted

The amendment request can supply decision-register content and owner-authorization data.

A fabricated test decision, D-940, was accepted during an independent production-mode reproduction.

### Finding 5 — Git-status reporting discrepancy

The implementation report describes 40 working-tree entries.

Independent inspection of Project X (106) reported:

- 152 modified tracked entries.
- 23 untracked entries.
- 175 total entries.
- No staged changes.

Correct the status reporting without staging, committing or reverting anything.

**This assignment must close these vulnerabilities without redesigning or rebuilding the numerical-contract architecture.**

Do not restart the previous regex and keyword correction cycle.

---

# 2. MANDATORY GOVERNANCE

Before implementation, read the complete:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Preserve D-014.

Do not modify the policy.

Maintain the established distinction:

- Category A: Owner authority.
- Category B: Working-AI design and implementation authority.
- Category C: Provisional evidence-dependent authority.
- Category D: Owner-reserved external, costly or irreversible actions.

Do not invent owner authorization.

Do not invent a human reviewer.

Do not modify unrelated project decisions.

Do not reopen accepted Prompt 13 work.

Do not authorize Prompt 14B.

## Working-environment restrictions

Work directly in the existing live Nation Supremacy repository.

Project X (106).zip is an audit snapshot, not a working project.

Do not create another project directory or duplicate repository.

Do not:

- Stage or commit Git changes.
- Push, reset, revert or discard changes.
- Modify production frontend, backend, SQL, database, migrations or APIs.
- Change gameplay.
- Change formulas or numerical parameter values.
- Modify D-014.
- Modify the production amendment manifest to simulate successful amendments.
- Remove historical correction archives.

Limit modifications to the existing contract validator, test suite and necessary associated QA/documentation files.

---

# 3. PRESERVE THE EXISTING IMPLEMENTATION

Do not restart the architecture.

Preserve:

- Canonical numerical contracts.
- `schema.json`.
- `lexicon.json`.
- Contract index.
- B-04 contracts.
- Evidence mapping architecture.
- Deterministic renderer.
- D-238 architecture decision.
- Existing 64 numerical foundation checks.
- Existing 83 contract regression tests.
- Existing 138 numerical self-tests.
- Historical 55-check baseline.
- All original regression fixtures.

Preserve the numerical foundation:

| Component | Required state |
|---|---:|
| Active formulas | 295 |
| Parameter records | 393 |
| B-03 carry-ins | 20 |
| Formula registers | 9 |
| Retired F-WEP-048 | Retired |
| B-04 F-EC-000b hash | Unchanged |
| B-04 F-EC-000f hash | Unchanged |
| Production amendment manifest | Empty |
| D-014 | Unmodified |

Do not resolve new security problems by changing existing numerical rules.

Preserve legitimate B-09 F-AL-006 within-turn cumulative accrual.

Preserve the D-045/D-064 Category B arithmetic authority classification.

---

# 4. FIX THE TRUSTED INPUT BOUNDARY

Target:

`docs/qa_backups/14A_contract_validator.py`

Inspect the complete implementation of:

`validate_amendment()`

Also inspect all functions it calls, including the production entry points.

## 4.1 Separate trusted context from amendment requests

Create a clearly defined trusted validation context.

It must be loaded by the validator from the actual canonical repository files using fixed, controlled paths.

Trusted inputs include:

1. Accepted baseline contracts.
2. Canonical schemas.
3. Canonical lexicon.
4. Evidence registry.
5. Evidence source documents.
6. DECISIONS.md.
7. AUTONOMOUS_DECISION_POLICY.md.
8. Owner-authorization records.
9. Canonical projection templates and renderer configuration.

The amendment request must not be allowed to replace these inputs.

The candidate request should contain only the information needed to describe a proposed amendment, such as:

- Amendment identifier.
- Target contract.
- Proposed typed proposition changes.
- References to existing evidence identifiers.
- References to applicable decision identifiers.
- Optional explanatory notes.

The request must not supply authoritative copies of repository files.

## 4.2 Reject caller-supplied trusted-source overrides

Reject attempts to supply or override:

- `baseline_contract`
- `evidence_mappings`
- `schema`
- `lexicon`
- `decision_register`
- `owner_authorizations`
- `projection_template`
- Any equivalent alias or alternative input capable of replacing trusted context.

Use strict request-schema validation.

Reject unknown fields.

Do not silently ignore attempted security overrides.

Return stable error codes with clear JSON paths.

## 4.3 Repository path protection

Trusted artifacts must be resolved from the actual repository root.

Reject:

- Path traversal.
- Paths outside the repository.
- Unexpected symbolic-link redirection.
- Alternate files supplied through an amendment request.
- Duplicate or ambiguous authoritative source locations.

Use the canonical repository path resolution rather than trusting user-provided path strings.

Do not introduce external services or network dependencies.

## 4.4 Trusted decision-register loading

Decision authority must come from the actual canonical DECISIONS.md.

An amendment request must never provide substitute decision-register text.

Verify:

- Decision ID uniqueness.
- Decision status.
- D-014 category.
- Decision scope.
- Proposition relationship.
- Applicable authority.
- Required owner authorization provenance.

Reproduce the fabricated D-940 attack and demonstrate that caller-supplied decision-register content cannot make it valid.

A request must not authorize itself by inventing its own decision record.

---

# 5. REPAIR EVIDENCE VALIDATION

Evidence verification must be performed against the trusted evidence registry and actual source documents whenever an amendment is evaluated.

Do not rely solely on validation performed earlier in a different execution path.

## 5.1 Revalidate every referenced mapping

For each evidence mapping referenced by the amendment:

1. Resolve the evidence identifier from the trusted registry.
2. Resolve its source using the canonical repository path.
3. Recompute the complete source SHA-256.
4. Compare against the registered hash.
5. Resolve the exact section.
6. Verify the recorded quotation against the actual source.
7. Verify the proposition identifier.
8. Verify scope and conditions.
9. Verify classification.
10. Verify reviewer metadata and review provenance.
11. Reject stale or inconsistent records.

## 5.2 Evidence classification

Preserve the existing classifications:

- SUPPORTS
- CONTRADICTS
- QUALIFIES
- CONTEXT_ONLY
- NOT_ESTABLISHED
- INVALID_SOURCE
- PARSE_FAILURE
- NOT_REVIEWED

Only independently reviewed SUPPORTS evidence can satisfy the positive evidence requirement.

Partial coverage is not complete support.

A contradictory or qualifying source must not automatically become SUPPORTS.

An amendment request cannot add its own evidence mapping and thereby authorize the amendment.

## 5.3 Human-review authenticity

A reviewer name, role string, date or checkbox is not sufficient proof that a human reviewed evidence.

Inspect the existing project workflow and use its actual approved review mechanism.

Do not invent reviewer identities or claim a human review happened.

Where an authentic and verifiable human attestation mechanism is not available:

- Preserve the mapping as NOT_REVIEWED.
- Reject amendments that depend on that mapping.
- Document the limitation.
- Do not fabricate an authenticity mechanism or owner authorization.

The reviewer must remain independent of the amendment author and implementation actor.

The validator can verify the integrity of an attestation, but must not claim that cryptographic integrity alone proves the quality of human semantic judgment.

## 5.4 Evidence attack regression

Permanently add the following adversarial test:

An amendment attempts to supply:

- An unrelated evidence document.
- A nonexistent evidence section.
- An invented quotation.
- A SHA-256 containing only zeros.
- An invented reviewer identity.
- An arbitrary SUPPORTS classification.

Expected result:

**REJECTED before amendment acceptance.**

Test the actual public production amendment-validation entry point.

Do not test only an internal helper function.

---

# 6. REPAIR COMPLETE MATERIAL COVERAGE

Target:

`material_coverage()`

Inspect its entire implementation and all callers.

The current implementation checks expected proposition fragments but fails to account for additional material between them.

Replace this fragment-presence logic with complete structural accounting.

## 6.1 Required behaviour

Every material segment must be accounted for by exactly one of:

1. A valid typed proposition.
2. A valid structured condition.
3. A valid structured exception.
4. An explicitly permitted, non-material grammatical element.

Everything else must fail closed.

Do not permit an unrecognized material proposition to exist merely because expected fragments appear elsewhere in the document.

## 6.2 Full coverage requirements

Validate:

- Complete source-span coverage.
- No unconsumed material text.
- No overlapping proposition spans.
- No silently ignored material.
- No unsupported trailing qualification.
- No inserted contradictory prose.
- No unrecognized exception.
- No missing scope qualification.
- No material text between otherwise valid proposition fragments.

If controlled-language parsing is used, require the complete parser output and its consumed source spans.

If generated projections are used, regenerate them exclusively from the canonical contracts and compare the entire normalized projection.

Do not accept arbitrary caller-supplied projection templates.

Do not rely on substring matching as proof of semantic coverage.

## 6.3 Exact coverage attack

Permanently reproduce the independent audit attack:

Insert:

"B-04 binary floating-point calculations are permitted."

into the candidate projection between otherwise valid expected proposition fragments.

The original contract prohibits binary-floating-point arithmetic.

Expected result:

- Projection mismatch or unparsed material error.
- Material coverage failure.
- Amendment rejected.
- No ACCEPTED result.

The validator must not report 100% coverage.

Test other insertion positions, including:

- Beginning of document.
- Middle of proposition.
- Between propositions.
- Inside an exception.
- End of document.
- After a valid trailing qualification.

Also test alternative wording of the same contradictory permission.

---

# 7. VALIDATE THE COMPLETE CONTRACT DIFF

Inspect the current amendment-comparison implementation.

It must not compare only proposition identifiers or proposition text.

The semantic comparison must account for every authoritative contract field, including:

- Subject.
- Predicate.
- Object.
- Modality.
- Polarity.
- Conditions.
- Exceptions.
- Scope.
- Inheritance.
- Units.
- Dimensions.
- Numerical representation.
- Rounding.
- Precision.
- Timing.
- Persistence.
- Evidence requirements.
- Authority references.
- Proposition lifecycle status.
- Contract-level constraints.
- Schema-relevant metadata.

Calculate deterministic diffs for all of these fields.

Every changed material field must pass the appropriate validation.

Unknown material changes must fail closed.

A valid proposition must not conceal an unauthorized change to its scope, evidence requirement or authority.

Preserve deterministic contract fingerprints and rendered-projection fingerprints.

A hash comparison alone is not semantic validation.

---

# 8. SEPARATE THE FOUR VALIDATION GATES

The production amendment path must execute the following gates against trusted context:

**Gate 1 — Contract integrity**

Validate schema, typed propositions, scope, conditions, exceptions, fingerprints and complete coverage.

**Gate 2 — Evidence integrity**

Validate real source content, exact excerpts, hashes, classification, scope and human-review provenance.

**Gate 3 — D-014 authority**

Validate actual decisions, applicable categories, decision status and authentic owner authorization where required.

**Gate 4 — Amendment comparison**

Validate every material change against the accepted baseline.

An amendment can pass only if all applicable gates pass.

No caller-supplied field, hash, reviewer identity, decision reference or contract metadata can override a failed gate.

Do not combine the gates into a permissive fallback path.

A failure in one gate must not be compensated for by passing another.

---

# 9. MANDATORY ADVERSARIAL REGRESSION TESTS

Use the actual production amendment entry point.

Tests must reproduce the real attack and verify the complete outcome.

## 9.1 Trusted-input attacks

| Attack | Required result |
|---|---|
| Request supplies a replacement baseline contract | REJECT |
| Request supplies replacement schema | REJECT |
| Request supplies replacement lexicon | REJECT |
| Request supplies fake evidence mappings | REJECT |
| Request supplies fake decision-register text | REJECT |
| Request supplies owner-authorization placeholders | REJECT |
| Request supplies an alternate projection template | REJECT |
| Request uses path traversal | REJECT |
| Request redirects a trusted path through a symlink | REJECT |

Add reasonable aliases and structurally different representations of these attacks.

## 9.2 Evidence attacks

| Attack | Required result |
|---|---|
| Fabricated source path | REJECT |
| Nonexistent section | REJECT |
| Invented quotation | REJECT |
| Incorrect source hash | REJECT |
| Stale source hash | REJECT |
| Invented reviewer identity | REJECT |
| Unsupported SUPPORTS classification | REJECT |
| Partial proposition coverage | REJECT |
| Contradictory evidence | REJECT |
| Request-created evidence mapping | REJECT |

## 9.3 Material-coverage attacks

| Attack | Required result |
|---|---|
| Contradictory text between expected fragments | REJECT |
| Unknown proposition | REJECT |
| Unparsed trailing qualification | REJECT |
| Additional permission hidden in exception | REJECT |
| Scope-changing material insertion | REJECT |
| Timing-changing material insertion | REJECT |
| Unit-changing material insertion | REJECT |
| Additional proposition in generated projection | REJECT |
| Duplicate or overlapping proposition spans | REJECT |

## 9.4 Authority attacks

Reproduce the fabricated D-940 scenario.

Also test:

- Decision-register injection.
- Incorrect decision category.
- Nonexistent decision.
- Duplicate decision.
- Deferred decision.
- Rejected decision.
- Superseded decision.
- Self-authorizing contract metadata.
- Category B downgrade of an owner-reserved proposition.
- Owner authorization supplied only through the amendment request.

All must be rejected for the correct semantic or authority reason.

## 9.5 Positive regression tests

The fixes must not reject every amendment.

Preserve and rerun:

1. Unchanged original baseline.
2. Valid Category B wording clarification.
3. Valid Category B semantic amendment with genuinely reviewed supporting evidence.
4. Valid Category C provisional amendment.
5. Valid owner-authorized Category A fixture with verifiable authorization provenance.
6. Legitimate B-09 F-AL-006 cumulative within-turn accrual.

Do not invent human review to make a positive fixture pass.

Use authentic test fixtures with explicitly documented provenance, or leave the human-review-dependent fixture blocked and explain the limitation.

Do not misclassify P-003 as Category A.

All existing D-998, D-999, D-990, D-991, D-992 and D-993 negative regression cases must remain intact.

---

# 10. TEST QUALITY AND EXECUTION

Do not weaken existing tests.

Do not make tests pass by adding unrelated structural failures.

Every test must identify the actual gate responsible for acceptance or rejection.

Use separate fixtures for:

- Valid baseline.
- Single-variable attacks.
- Combined attacks.
- Positive legitimate amendments.

The exact combined false-acceptance scenarios from Project X (106) must be permanent tests.

Tests must execute the same production validation path used for real amendments.

Avoid test-only security bypasses.

Record:

- Test name.
- Attack or positive scenario.
- Input fixture identifier.
- Expected result.
- Actual result.
- Failure code.
- Validation gate.
- Exit status.

Run the complete existing and new suites independently:

- Original 55 numerical checks.
- Current numerical validator checks.
- Original 138 numerical self-tests.
- Existing 83 contract tests.
- All new trusted-input and semantic-coverage tests.
- Documentation-link validator.

Do not state that a suite passed if it timed out, was skipped or was not executed completely.

If runtime is excessive, optimize test execution without reducing coverage.

All tests must be deterministic and offline.

---

# 11. GIT AND PROJECT-STATUS RECONCILIATION

The independent Project X (106) audit observed:

- 152 modified tracked entries.
- 23 untracked entries.
- 175 total working-tree entries.
- No staged changes.

The implementation report's 40-entry figure was inaccurate.

Reinspect the live repository and report its actual current status.

Compare Project X (106) with the current working tree using a safe, read-only method.

Distinguish:

- Pre-existing modifications.
- Files changed by this assignment.
- Newly created files.
- Existing untracked files.
- Staged changes, if any.

Do not stage, commit, revert or discard anything.

Do not claim that every modified file was created by this assignment.

Update the implementation and final QA report to present accurate counts and explain the difference from the previous audit snapshot.

---

# 12. DOCUMENTATION AND PROMPT ARCHIVING

Preserve the existing architecture proposal and implementation report.

Create a new assignment archive:

`docs/prompts/prompt_14A-C2_trusted_input_and_semantic_gate_hardening.md`

Archive the complete exact prompt.

Update:

`docs/prompts/INDEX.md`

Append a new progress-log entry explaining:

- Independent Project X (106) findings.
- Caller-controlled trusted-input vulnerability.
- Evidence revalidation failure.
- Material-coverage failure.
- Authority-source substitution.
- Exact corrections performed.
- Actual regression results.
- Remaining limitations.

Update the relevant current-position entries in:

- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/stage-2/22_formulas_and_balance.md`
- Numerical baseline QA report.
- Semantic-contract implementation report.

Preserve the previous implementation report and historical correction records.

Do not rewrite history or delete earlier failing test results.

Do not claim Prompt 14A is complete.

Prompt 14B must remain NOT AUTHORIZED / NOT STARTED.

---

# 13. REQUIRED DELIVERABLES

Provide the following:

1. Hardened trusted-context loader.
2. Strict amendment request schema.
3. Trusted evidence revalidation.
4. Authentic human-review provenance handling.
5. Trusted D-014 authority validation.
6. Complete material-coverage validation.
7. Complete contract-level semantic diff.
8. Fixed production amendment-validation entry point.
9. Expanded adversarial regression suite.
10. Preserved positive regression suite.
11. Updated numerical and semantic QA reports.
12. Corrected Git-status reconciliation.
13. Complete archived implementation prompt.
14. Updated project handoff and roadmap.

Suggested additional test file:

`docs/qa_backups/test_14A_trusted_amendment_security.py`

Use the existing project naming and test conventions if they differ.

Suggested report:

`docs/qa_backups/14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md`

---

# 14. FINAL ACCEPTANCE CRITERIA

| ID | Acceptance criterion |
|---|---|
| C2-01 | Trusted repository inputs cannot be replaced by amendment requests |
| C2-02 | Strict amendment request schema rejects unknown and privileged fields |
| C2-03 | Canonical repository paths cannot be substituted or redirected |
| C2-04 | Evidence is revalidated during amendment acceptance |
| C2-05 | Fabricated quotations and hashes are rejected |
| C2-06 | Human-review provenance is not fabricated |
| C2-07 | D-014 decision authority comes from trusted records |
| C2-08 | Fabricated D-940 scenario is rejected |
| C2-09 | Owner authorization cannot be caller-supplied |
| C2-10 | Complete material coverage is demonstrated |
| C2-11 | Contradictory inserted projection text is rejected |
| C2-12 | Every material contract-level field participates in semantic diff |
| C2-13 | All four validation gates operate independently |
| C2-14 | Original D-998/D-999/D-990 cases still reject |
| C2-15 | Original D-991/D-992/D-993 cases still reject |
| C2-16 | Positive legitimate amendments remain possible |
| C2-17 | B-09 F-AL-006 remains valid |
| C2-18 | All legacy tests are preserved and executed |
| C2-19 | All new security tests pass |
| C2-20 | Validation remains deterministic and offline |
| C2-21 | 295 active formulas remain unchanged |
| C2-22 | 393 numerical parameter records remain unchanged |
| C2-23 | All 20 B-03 carry-ins remain unchanged |
| C2-24 | Both original B-04 source hashes remain unchanged |
| C2-25 | Production amendment manifest remains empty |
| C2-26 | D-014 remains unchanged |
| C2-27 | No gameplay or production-system files are changed |
| C2-28 | Historical records and correction archives are preserved |
| C2-29 | Git status is reported accurately without Git operations |
| C2-30 | Prompt 14B remains unauthorized |

If any mandatory criterion fails, report it and leave the relevant workstream open.

Do not claim success merely because the tests written alongside the implementation pass.

The exact independently reproduced attacks must be demonstrated to fail through the actual production entry point.

---

# 15. FINAL REPORT FORMAT

Provide:

1. Executive completion assessment.
2. Root cause of each Project X (106) vulnerability.
3. Exact trusted-input boundary implemented.
4. Evidence integrity and reviewer-provenance implementation.
5. D-014 authority protection.
6. Complete material-coverage implementation.
7. Contract-level diff implementation.
8. Individual results for every mandatory attack.
9. Individual results for every positive fixture.
10. Legacy and new validator totals.
11. Formula and parameter preservation results.
12. Both B-04 hash verification results.
13. Production amendment manifest status.
14. Exact files created and modified.
15. Accurate Git status.
16. Remaining technical or governance limitations.
17. Final Prompt 14A status.
18. Exact next action.

Clearly distinguish:

- Implementation complete.
- Validation complete.
- Documentation complete.
- Human evidence review complete.
- Owner authorization obtained.
- Formal owner acceptance.

Never combine these into a single completion statement.

---

# FINAL INSTRUCTION

This is a targeted hardening assignment, not a new architecture project.

Keep the contract architecture from Project X (106).

Fix the actual vulnerabilities.

Make the production amendment-validation path fail closed against caller-controlled trusted inputs, fabricated evidence, substituted authority and unaccounted material propositions.

Preserve all legitimate existing formulas and numerical systems.

Do not return to regex-and-keyword patching.

Do not create another series of diagnostic-only prompts.

**The objective is to make the existing architecture trustworthy enough to pass independent adversarial verification.**

Prompt 14A remains OPEN until independent verification and owner acceptance.

Prompt 14B remains NOT AUTHORIZED / NOT STARTED.
