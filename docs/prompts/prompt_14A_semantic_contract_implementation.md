# NATION SUPREMACY — PROMPT 14A SEMANTIC CONTRACT IMPLEMENTATION AND CONTROLLED VALIDATOR CUTOVER

**Project:** Nation Supremacy  
**Parent phase:** Prompt 14A — Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Starting audit baseline:** Project X (105)  
**Architecture proposal:** `docs/qa_backups/14A_SEMANTIC_CONTRACT_ARCHITECTURE_PROPOSAL.md`  
**Execution type:** Controlled architecture implementation, semantic validator replacement and final QA reconciliation  
**Authority:** D-014 — Autonomous Decision Policy

**Current authoritative status:**

- Prompt 14A: OPEN — NOT COMPLETE.
- Numerical foundation: SUBSTANTIALLY COMPLETE.
- Semantic validation architecture review: COMPLETE.
- Semantic contract implementation: NOT STARTED.
- Prompt 14B: NOT AUTHORIZED / NOT STARTED.

---

# 1. MISSION

Implement the canonical machine-readable numerical-contract architecture recommended by the independent review of Project X (105).

The existing semantic validator has repeatedly accepted semantically contradictory amendments expressed using alternative numerical terminology.

The independent review reproduced three complete false acceptances:

- D-991 — Radix-two exponent/significand encoding.
- D-992 — Sign, exponent and mantissa fields.
- D-993 — Residual sub-unit amounts between turns.

Each passed all 55 existing numerical foundation checks.

Adding more keywords or regex patterns is not an acceptable solution.

**Replace the underlying validation architecture.**

The objective is to establish one authoritative, structured representation for the controlled numerical rules, with:

1. Strictly typed numerical propositions.
2. Explicit numerical representation rules.
3. Explicit scope, units and timing.
4. Structured exceptions, conditions and negation.
5. Complete material-clause coverage.
6. Deterministic amendment comparison.
7. Independently reviewed evidence provenance.
8. Separate D-014 authority validation.
9. Generated or strictly validated human-readable specifications.
10. Comprehensive positive and adversarial regression testing.

This assignment must preserve the completed numerical foundation.

Do not restart Prompt 14A or perform another diagnostic-only investigation.

---

# 2. MANDATORY GOVERNANCE

Before implementation, read the complete:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Also inspect:

- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/DECISIONS.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/22_formulas_and_balance.md`
- The complete B-04 formula register.
- The B-09 F-AL-006 definition.
- The numerical baseline QA report.
- The complete 14A architecture proposal.
- The previous Prompt 14A correction archives.
- The existing numerical validator and mutation fixtures.

Follow D-014, particularly its distinction between Categories A, B, C and D.

Do not modify `AUTONOMOUS_DECISION_POLICY.md`.

## 2.1 Working-environment restrictions

Work directly in the existing live project repository.

Uploaded ZIP files are independent audit snapshots. They are not working project directories.

Do not:

- Create another project directory.
- Duplicate the repository.
- Overwrite completed work unnecessarily.
- Stage, commit, push, reset, revert or discard Git changes.
- Modify production frontend, backend, SQL, database, migrations, APIs or gameplay.
- Change numerical formula definitions or parameter values.
- Modify production amendment manifests to fabricate an authorized amendment.
- Create owner authorization.
- Authorize Prompt 14B.

The work concerns documentation contracts, validators, regression tests and associated QA records only.

---

# 3. PRESERVATION REQUIREMENTS

The following are mandatory regression invariants.

| Existing component | Required state |
|---|---|
| Active formula identifiers | 295 unchanged |
| Retired formula | F-WEP-048 remains retired |
| Formula registers | All nine preserved |
| Numerical parameter records | 393 unchanged |
| B-03 carry-in parameters | All 20 preserved |
| B-14 canonical file | `22_formulas_and_balance.md` |
| Existing validator checks | 55 preserved |
| Existing numerical self-tests | 138 preserved |
| B-04 source contracts | Baseline rules unchanged |
| B-04 source hashes | Both original hashes preserved |
| Production amendment manifest | `amendments: []` |
| Decision records | Historical identifiers preserved |
| Evidence provenance | Existing source history preserved |
| D-014 | Unmodified |

The two existing B-04 baseline hashes are:

- F-EC-000b: `bb1090ccae5cd15e0d883a57ab63216a106ff7c4e503e85cf2146e19e02271c6`
- F-EC-000f: `3025cc447ebb91be8d226ff5035da0e403947d2be603e81e535bbd5600bca5ca`

Do not modify either baseline clause during initial contract extraction.

If renderer output differs from the existing source after the agreed normalization, correct the contract extraction or renderer. Do not silently rewrite the source rule.

---

# 4. RESOLVED ARCHITECTURAL AND GOVERNANCE QUESTIONS

The following findings from the independent review must be incorporated.

## 4.1 Arithmetic authority — Category B

The repository already contains:

- D-045 — Resource units and precision.
- D-064 — Deterministic integer arithmetic.

Both are Confirmed design decisions.

Under D-014, the numerical arithmetic convention is a Category B design rule.

Do not classify P-003, the binary-floating-point prohibition, as an owner-reserved Category A decision merely because B-14 §2.1 associates integer arithmetic with fixed hosting constraints.

D-008, D-009 and D-010 establish platform and hosting direction.

D-045 and D-064 establish the relevant arithmetic design rules.

The validator must derive proposition authority from the actual policy and governing decision records, not from an unsupported assumption.

Correct the B-14 §2.1 authority references where necessary:

- Hosting and backend constraints must retain their actual D-008/D-009/D-010 authority.
- Integer arithmetic and whole-unit precision must cite D-045/D-064.

Do not alter historical decision entries.

A new Category B architecture decision may be recorded under D-014 when the contract architecture is adopted. The working AI must make and document ordinary Category B decisions rather than requesting unnecessary owner approval.

## 4.2 F-EC-000b numerical scope

Do not model the arithmetic convention as one undifferentiated global permission or prohibition.

Separate:

**B-04 register-specific rules:**

- Whole integer quantities.
- Explicit division rounding.
- Basis-point percentages.
- B-04 formula arithmetic.

**Cross-cutting arithmetic authority:**

Preserve the broader integer economic-arithmetic rule established by D-064, within its actual documented scope.

Do not silently extend it to every unrelated numerical system merely because the project contains nine formula registers.

Every proposition must have an explicit, source-supported scope.

## 4.3 B-09 F-AL-006 must remain valid

Preserve the canonical B-09 rule:

`F-AL-006 — Automatic Per-Turn Production Tax Arithmetic`

It specifies legitimate cumulative fractional accrual within a turn using:

- Integer gross production.
- Integer basis-point rates.
- Cumulative production-event totals.
- Integer arithmetic and floor rounding.
- Separate asset-specific accumulation.
- Per-turn settlement and reconciliation.

This is not permission to retain residual fractional balances between turns.

Represent these as distinct concepts:

- `CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN`
- `CROSS_TURN_REMAINDER_PERSISTENCE`

Do not collapse them into an ambiguous generic fractional-carry proposition.

A B-04 prohibition or unresolved status must not accidentally reject the legitimate B-09 F-AL-006 model.

D-993, concerning residual sub-unit amounts between turns, must remain unsupported unless a future properly evidenced and authorized change establishes otherwise.

No B-09 formula or rate may be changed in this assignment.

## 4.4 Evidence reviewer accountability

Establish an explicit **Independent Human Evidence Reviewer** role and review procedure.

The reviewer must be a human and must not be the amendment author or implementation actor.

Every active SUPPORTS mapping must record:

- Actual reviewer identity.
- Reviewer role.
- Review date.
- Source document and SHA-256.
- Exact section and excerpt.
- Proposition identifier.
- Covered scope and conditions.
- Evidence classification.
- Review rationale.
- Review status.

The working AI may prepare evidence mappings for review.

It must not claim human review or independently promote its own proposed classification to SUPPORTS.

Do not invent the identity of a reviewer.

When no actual human reviewer has approved a mapping, retain its `NOT_REVIEWED` or equivalent draft state. No semantic amendment requiring that evidence may pass.

This restriction must not prevent construction and testing of the validator itself.

---

# 5. CANONICAL NUMERICAL CONTRACTS

Create the proposed controlled architecture under:

`docs/stage-2/22_numerical_contracts/`

Use a minimal, maintainable artifact structure:

- `index.json`
- `schema.json`
- `lexicon.json`
- `F-EC-000b.contract.json`
- `F-EC-000f.contract.json`
- `evidence_mappings.json`
- `projections/`

The contract files must be authoritative for the controlled clauses once adopted.

The Markdown paragraphs in the B-04 formula register must be generated from the contracts or validated against their deterministic rendered projections.

Do not create a competing formula register or duplicate the 295 existing formula definitions.

Do not duplicate D-014 decisions in the contract files.

Every proposition must reference the applicable existing `F-` and `D-` identifiers.

New proposition identifiers must be namespaced, stable and never reused.

## 5.1 Strict schema

Implement a complete machine-verifiable schema.

At minimum, validate:

**Contract identity**

- Schema version.
- Contract ID.
- Clause ID.
- Source document.
- Baseline source hash.
- Contract version.
- Lifecycle status.
- Effective decision reference.

**Scope**

- Formula register or system.
- Economic domain where applicable.
- Turn phase.
- Within-turn versus across-turn persistence.
- Explicit inheritance rules.

**Propositions**

- Stable proposition ID.
- Closed proposition-kind enumeration.
- Typed subject.
- Typed predicate.
- Typed object.
- Modality.
- Polarity.
- Conditions.
- Exceptions.
- Units and dimensions.
- Timing.
- Numerical representation.
- Rounding and precision.
- Authority.
- Source anchor.
- Proposition status.

**Exception modelling**

Each exception must identify:

- Target proposition.
- Permitted effect.
- Scope.
- Conditions.
- Applicable authority.

Unknown exception effects and invalid targets must be rejected.

**Schema safeguards**

- Reject unknown fields.
- Reject duplicate identifiers.
- Reject dangling references.
- Reject invalid enumerations.
- Reject missing mandatory metadata.
- Reject incompatible subject/predicate/object combinations.
- Reject unit and dimension incompatibility.
- Reject incomplete timing and rounding specifications.
- Reject ambiguous inheritance.

Do not use generic `OTHER` or unrestricted text fields to bypass semantic validation.

Contract lifecycle states must be separate from D-237's numerical-value status vocabulary.

Preserve the four numerical statuses and the existing absence marker.

## 5.2 Correct negative arithmetic representation

The existing proposal's P-003 example incorrectly combines:

`MAY_USE_REPRESENTATION`

with:

`MUST_NOT`.

Correct this.

Use one formally defined, unambiguous representation proposition.

For example, the normalized meaning must be:

- Predicate: `USES_REPRESENTATION`.
- Object: `BINARY_FLOATING_POINT`.
- Modality: `MUST_NOT`.

Define the semantics of polarity and modality so double negation and conflicting permissions cannot bypass validation.

Provide explicit truth-table or equivalent normalization tests.

## 5.3 Unestablished propositions

Represent the cross-turn fractional-remainder question as an unresolved knowledge state, not as an established positive rule.

A `NOT_ESTABLISHED` mapping cannot count as a `SUPPORTS` mapping.

An unresolved proposition must not be required to possess positive supporting evidence merely to preserve the baseline.

However, any proposed change that turns an unresolved proposition into an affirmative permission must require new reviewed supporting evidence and appropriate D-014 authority.

---

# 6. CONTROLLED LANGUAGE AND MATERIAL COMPLETENESS

Prefer typed contract patches as the authoritative amendment mechanism.

The controlled-language parser may be retained as an ingestion or migration mechanism.

If a prose parser is implemented:

1. Define its complete grammar.
2. Version the grammar.
3. Parse every material clause segment.
4. Produce a typed proposition representation.
5. Require 100% material coverage.
6. Reject ambiguous or multiply interpretable clauses.
7. Reject all unknown material terms and constructs.
8. Reject unconsumed trailing qualifications.
9. Never use AI inference, network services or unrestricted NLP at validation time.

After adoption, raw prose must not become an alternative route around the typed contract.

A new synonym may either map to a reviewed canonical concept or be rejected as unmapped.

It must never be silently accepted.

## Mandatory fail-closed errors

Implement stable, machine-readable errors, including:

- `CONTRACT_SCHEMA_INVALID`
- `CONTRACT_UNMAPPED_TERM`
- `CONTRACT_UNPARSED_MATERIAL_SEGMENT`
- `CONTRACT_PROJECTION_MISMATCH`
- `CONTRACT_PROPOSITION_CONFLICT`
- `CONTRACT_EXCEPTION_UNSUPPORTED`
- `CONTRACT_SCOPE_MISMATCH`
- `CONTRACT_EVIDENCE_MAPPING_MISSING`
- `CONTRACT_EVIDENCE_NOT_REVIEWED`
- `CONTRACT_EVIDENCE_PROPOSITION_MISMATCH`
- `CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS`
- `CONTRACT_AUTHORITY_MISMATCH`
- `CONTRACT_OWNER_AUTHORIZATION_MISSING`

Use precise diagnostics containing the proposition ID and relevant JSON path.

---

# 7. INDEPENDENT EVIDENCE VALIDATION

Evidence and authority must be separate gates.

## Evidence gate

The gate must determine whether an independently reviewed source establishes the exact changed proposition, including its scope and conditions.

Permitted classifications:

- `SUPPORTS`
- `CONTRADICTS`
- `QUALIFIES`
- `CONTEXT_ONLY`
- `NOT_ESTABLISHED`
- `INVALID_SOURCE`
- `PARSE_FAILURE`
- `NOT_REVIEWED`

Only an actual reviewed SUPPORTS mapping may satisfy the positive evidence requirement.

The validator must:

- Recompute the full source hash.
- Resolve the exact section.
- Verify the exact excerpt.
- Confirm proposition identity.
- Confirm scope and conditions.
- Reject partial coverage.
- Reject stale evidence mappings.
- Reject contradictory evidence.
- Reject an amendment that supplies its own evidence mapping.

An existing clause may establish the current baseline during extraction. It must not be treated as independent evidence that a changed proposition is correct.

Do not include `authorizing_decision` in an evidence mapping as a substitute for independent evidence.

The D-014 authority gate is separate.

The validator may confirm the integrity and coverage of human-reviewed evidence. It must not claim that it independently proves human semantic judgment.

---

# 8. D-014 AUTHORITY VALIDATION

`DECISIONS.md` remains the sole decision-authority register.

The contract must reference existing decision IDs and must not create a parallel decision system.

For each changed proposition, validate:

- Decision exists exactly once.
- Correct clause and proposition scope.
- Correct D-014 category.
- Correct decision status.
- Previous and replacement contract versions.
- Alternatives and rationale.
- Evidence references.
- Consequences.
- Reopening conditions.
- Owner authorization where genuinely required.
- No pending, rejected, deferred or superseded authority.

Category rules:

**Category B:** Ordinary design and implementation decisions. The working AI decides and records them under D-014.

**Category C:** Provisional decisions with a named missing evidence item or test. They remain Provisional.

**Category A/D:** Owner-reserved matters. Require authentic, traceable owner-originated authorization.

For Category A/D, a decision-register status or manifest string alone must not be treated as proof of owner authorization. Verify the original owner instruction or authorization source and its provenance. If that source cannot be established, reject the amendment.

The contract's authority metadata must never authorize itself.

A Category B amendment must not be able to downgrade an owner-reserved proposition by simply changing `owner_reserved` or its authority classification in JSON.

Any authority-classification change must itself be checked against D-014 and the governing decision history.

---

# 9. DETERMINISTIC AMENDMENT AND FINGERPRINT VALIDATION

Implement distinct fingerprints for:

1. Canonical contract.
2. Rendered human-readable projection.
3. Source Markdown.
4. Evidence documents.

Use deterministic serialization, canonical ordering and UTF-8.

The amendment process must compare typed propositions, not merely hashes or matching sentences.

Compute:

- Added propositions.
- Removed propositions.
- Changed propositions.
- Unchanged propositions.
- Scope changes.
- Exception changes.
- Unit and timing changes.
- Authority changes.

Every changed proposition must independently satisfy both evidence and authority gates.

No hash, filename, decision ID or manifest entry can override a semantic failure.

The baseline production amendment manifest must remain empty while the initial architecture is implemented.

---

# 10. IMPLEMENTATION AND MIGRATION

Complete this as one coordinated implementation assignment.

## Phase 0 — Freeze and record baseline

Record actual results from the existing live repository:

- 55/55 numerical foundation checks.
- 138/138 numerical self-tests.
- Both B-04 source hashes.
- Empty production amendment manifest.
- 295 active formulas.
- 393 parameter records.
- 20 B-03 carry-ins.
- Nine formula registers.
- D-014 unchanged.

## Phase 1 — Build shadow contracts

Create the strict schema, contract index, lexicon and two B-04 contracts.

Build deterministic renderers.

Prove normalized projection equivalence with the existing B-04 clauses.

Do not modify the existing rules.

Create the evidence-review workflow and prepare draft mappings.

Do not fabricate SUPPORTS classifications.

## Phase 2 — Build the new validator

Create:

`docs/qa_backups/14A_contract_validator.py`

Create:

`docs/qa_backups/test_14A_contract_validator.py`

Integrate new checks into the existing numerical foundation validator using new IDs beginning at `14A-56`.

Do not weaken any existing check during the shadow-validation phase.

New validator checks must independently verify:

- Schema integrity.
- Full material coverage.
- Contract hashes.
- Projection equivalence.
- Evidence mapping integrity.
- D-014 authority.
- Amendment proposition diffs.
- Exception and condition semantics.
- Determinism.

## Phase 3 — Controlled validator adoption

Once the baseline and adversarial tests pass, adopt the canonical contracts through an appropriate Category B D-014 decision.

Record the decision with all required alternatives, rationale, evidence, trade-offs, confidence and reopening conditions.

Do not request owner approval for an ordinary Category B implementation decision.

The old regex/blocklist logic may be retained for historical diagnostics, but it must not remain a competing acceptance gate after the new architecture becomes authoritative.

A legitimate amendment accepted by the new contract architecture must not be rejected by the retired lexical gate.

Preserve legacy test history and explain any superseded semantic checks.

## Phase 4 — Final documentation and closeout

Reconcile:

- B-04 source projections.
- B-14 canonical documentation.
- Numerical QA report.
- DECISIONS.md.
- AI_CONTEXT.md.
- AI_HANDOFF.md.
- Stage 2 roadmap.
- Progress log.
- Prompt archive and its index.

Preserve all historical correction archives.

Do not rewrite historical records into false statements.

---

# 11. MANDATORY REGRESSION TESTS

## 11.1 Negative cases

All six attacks must be permanently tested:

| Case | Required result |
|---|---|
| D-998 | Reject unrelated fair-play evidence |
| D-999 | Reject prohibition-to-permission reversal |
| D-990 | Reject unauthorized alternative-representation exception |
| D-991 | Reject radix-two exponent/significand encoding permission |
| D-992 | Reject sign/exponent/mantissa representation permission |
| D-993 | Reject unsupported cross-turn residual carry |

Each class must contain at least three materially different wording variations.

Do not reject the variants merely because of an unrelated missing hash, malformed manifest or other structural problem.

Test the actual semantic reason.

For D-991 and D-992, either canonical mapping to the prohibited representation or fail-closed unknown-term rejection is acceptable.

For D-993, specifically verify that no evidence supports cross-turn persistence.

## 11.2 Positive cases

The implementation must prove that legitimate changes remain possible.

Required fixtures:

1. Unchanged original baseline.
2. Valid Category B wording clarification.
3. Valid Category B semantic change with genuinely supporting evidence.
4. Valid Category C provisional change.
5. Valid owner-authorized Category A change against a genuinely owner-reserved test proposition.
6. Legitimate B-09 F-AL-006 cumulative within-turn accrual.

Do not classify P-003 as Category A merely to create an owner-authorized positive fixture.

Do not simply reject every amendment to obtain passing negative tests.

## 11.3 Adversarial dimensions

Test:

- Positive and negative propositions.
- Double negation.
- Negation scope.
- Permission and prohibition reversals.
- Conditional exceptions.
- Multiple exceptions.
- Global versus subsystem scope.
- Cross-register scope leakage.
- Units and dimensions.
- Basis-point conversions.
- Rounding directions.
- Negative-number floor behaviour.
- Timing and persistence.
- Within-turn versus across-turn accumulation.
- Alternative arithmetic representations.
- Unknown terms and predicates.
- Unknown exception effects.
- Partial evidence coverage.
- Stale evidence hashes.
- Fabricated evidence quotations.
- Contradictory evidence.
- Unauthorized authority changes.
- Category C promotion.
- Self-authorizing contract metadata.
- Owner-authorization placeholders.
- Contract and projection fingerprint manipulation.

Use deterministic, reproducible mutation tests.

Report proposition coverage and test results.

---

# 12. CURRENT DOCUMENTATION STATUS RECONCILIATION

An important defect exists in Project X (105).

The current repository still claims that Prompt 14A is complete because the earlier 55/55 checks and 138/138 tests passed.

Those historical counts are real, but their interpretation as proof of semantic completeness is incorrect.

In particular:

- B-14 §15.11 claims 20/20 semantic gates PASS.
- SEM-07 claims unknown material wording fails closed.
- The independent D-991, D-992 and D-993 reproductions disprove that claim.

Preserve the original §15.11 and the original progress-log §107 as historical records.

Append a superseding B-14 status section and a new dated progress-log entry explaining the independent findings and implementation outcome.

Correct the current-position entries in:

- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/stage-2/22_numerical_baseline_qa_report.md`

The current status must accurately distinguish:

- Earlier numerical foundation work.
- Previous semantic validator implementation.
- Failed semantic acceptance attempts.
- Completed diagnostic architecture review.
- New contract implementation.
- Documentation-level completion.
- Owner acceptance.

The current status must not claim Prompt 14A is complete if any mandatory implementation gate remains open.

The next action must be stated precisely.

**Prompt 14B must remain NOT AUTHORIZED / NOT STARTED.**

Do not reopen Prompt 13 or modify unrelated historical acceptance records.

---

# 13. REQUIRED PROMPT ARCHIVING AND DELIVERABLES

Archive this exact implementation prompt at:

`docs/prompts/prompt_14A_semantic_contract_implementation.md`

Update:

`docs/prompts/INDEX.md`

Do not summarize the original prompt in its permanent archive.

Required deliverables:

1. Canonical machine-readable contracts.
2. Strict schema.
3. Canonical lexicon.
4. Evidence mapping system.
5. Deterministic renderer.
6. New contract validator.
7. Complete regression suite.
8. Validator integration.
9. Independent QA implementation report.
10. Updated B-14 status and revision history.
11. Updated numerical QA report.
12. Updated progress log.
13. Updated current project handoff and context.
14. Archived implementation prompt.
15. Accurate next-action statement.

Suggested QA report:

`docs/qa_backups/14A_SEMANTIC_CONTRACT_IMPLEMENTATION_REPORT.md`

---

# 14. FINAL ACCEPTANCE CRITERIA

The assignment may be reported complete only when:

| ID | Acceptance criterion |
|---|---|
| AC-01 | 295 formulas unchanged |
| AC-02 | 393 parameter records unchanged |
| AC-03 | 20 B-03 carry-ins unchanged |
| AC-04 | Nine formula registers preserved |
| AC-05 | Existing 55 numerical checks preserved |
| AC-06 | Existing 138 self-tests preserved |
| AC-07 | Both original B-04 hashes preserved |
| AC-08 | Production amendment manifest remains empty |
| AC-09 | Both controlled contracts pass strict schema validation |
| AC-10 | B-04 source projections match the existing clauses |
| AC-11 | All material propositions have complete coverage |
| AC-12 | P-003 negative representation rule is unambiguous |
| AC-13 | D-045/D-064 authority is correctly represented |
| AC-14 | F-AL-006 remains valid |
| AC-15 | D-991, D-992 and D-993 are rejected |
| AC-16 | D-998, D-999 and D-990 are rejected |
| AC-17 | All required positive fixtures pass |
| AC-18 | Evidence and authority gates operate independently |
| AC-19 | Human evidence-review status is genuine and traceable |
| AC-20 | Owner authorization cannot be fabricated or self-authorized |
| AC-21 | Unknown material propositions fail closed |
| AC-22 | No unrestricted NLP or external service is required |
| AC-23 | Validation is deterministic and offline |
| AC-24 | Legacy semantic rejection logic cannot block valid adopted amendments |
| AC-25 | Current project documentation and status are reconciled |
| AC-26 | Historical records remain preserved |
| AC-27 | No production, gameplay or numerical values are changed |
| AC-28 | D-014 remains unchanged |
| AC-29 | Prompt 14B remains unauthorized |
| AC-30 | Actual execution evidence is recorded |

If any criterion fails, identify it precisely and leave Prompt 14A OPEN.

Do not declare success because the new validator passes its own incomplete fixtures.

Do not claim human evidence approval without actual human review.

Do not claim owner acceptance.

---

# 15. FINAL REPORT

Provide:

1. Exact list of files created.
2. Exact list of files modified.
3. Architecture implemented.
4. Contract schema and proposition model.
5. How evidence review works.
6. How D-014 authority is enforced.
7. How unknown and contradictory material is rejected.
8. Results for all six mandatory negative cases and their paraphrases.
9. Results for every positive fixture.
10. Full legacy and new validator totals.
11. Formula, parameter and carry-in preservation counts.
12. Source-hash and manifest verification.
13. Actual Git status, without performing Git operations.
14. Remaining blockers or provisional decisions.
15. Final Prompt 14A status.
16. Exact next action.

Distinguish:

- Implementation complete.
- Documentation complete.
- Validation passed.
- Owner acceptance pending.
- Owner acceptance granted.

Never combine these into a single completion claim.

---

# FINAL INSTRUCTION

The purpose of this assignment is to finish the semantic-validation problem properly.

Do not return to the previous keyword-and-regex correction cycle.

Do not produce another large diagnostic proposal.

Do not redesign the 295 formulas or the 393 numerical records.

Implement the canonical contract approach, resolve the documented schema and governance defects, run the complete adversarial and positive regression suite, and reconcile the project's current status.

**Prompt 14A must remain open until the actual semantic-validation architecture is demonstrated to work.**

**Prompt 14B remains exclusively subject to separate explicit owner authorization.**
