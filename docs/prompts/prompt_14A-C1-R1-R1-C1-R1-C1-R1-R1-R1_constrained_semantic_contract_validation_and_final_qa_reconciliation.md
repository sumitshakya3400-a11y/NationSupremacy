# PROMPT 14A-C1-R1-R1-C1-R1-C1-R1-R1-R1 — CONSTRAINED SEMANTIC CONTRACT VALIDATION AND FINAL QA RECONCILIATION

## 1. OBJECTIVE

Complete the remaining critical defect identified during the independent audit of Project X (103).

This is the final narrowly scoped correction within Prompt 14A.

Two deliverables are required:

1. Replace the inadequate clause-specific evidence stance detection with a deterministic, source-backed semantic contract validation mechanism.
2. Complete the final documentation-link, closure-register, prompt-archive and continuity reconciliation.

The latest independent audit reproduced a false acceptance that passes all 53 numerical foundation checks.

The current validator recognizes certain explicit phrases but fails to recognize a semantically equivalent numerical permission expressed through a differently worded exception.

This is not an invitation to implement unrestricted natural-language understanding.

Build a reliable, narrowly scoped validation mechanism for the existing controlled B-04 source contracts.

Do not restart Prompt 14A.

Do not redesign the numerical architecture.

Do not change production formulas, game-balance parameters or gameplay rules.

## 2. MANDATORY GOVERNANCE

Before beginning:

Read the complete:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Also read:

- `docs/DECISIONS.md`
- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/ROADMAP.md`
- The canonical B-04 register.
- Canonical B-14.
- The numerical QA report.
- The previous Prompt 14A correction archives.

Follow the actual D-014 rules.

### Authority boundaries

| Category | Required treatment |
|---|---|
| A | Owner authority only |
| B | Working AI decides and records the decision |
| C | Provisional decision with safe default and named evidence/test |
| D | Owner authority only |

Do not invent owner approval.

Do not treat test fixtures as genuine project decisions.

Do not promote provisional parameters to approved values.

Do not modify the Autonomous Decision Policy.

Preserve the distinction between documentation completion, implementation and owner acceptance.

### Workflow restrictions

- Work in the existing live repository.
- Never use an uploaded ZIP as the working project.
- Do not create duplicate project directories.
- Do not overwrite unrelated work.
- Do not stage, commit, push, reset, revert or discard Git changes.
- Do not change protected Git history.
- Do not implement frontend, backend, database, SQL, API, migration, gameplay, formula, security or deployment changes.
- Do not modify the production B-04 formula clauses.
- Do not change the two current B-04 source hashes.
- Do not populate the production amendment manifest.
- Do not reopen Prompt 13.
- Do not authorize Prompt 14B.

## 3. PROJECT X (103) — EXACT REPRODUCED DEFECT

### 3.1 Existing implementation

Inspect:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Relevant functions:

- `_classify_stance()`
- `_evidence_supports()`
- `_validate_decision_record()`
- `_validate_source_contract()`

The current implementation uses clause-specific regular expressions and a fallback that returns `supports` when none of its limited contradiction conditions match.

This is unsafe.

### 3.2 Exact D-990 mutation

The independent audit modified F-EC-000b using the following replacement wording:

"No formula uses binary floating point. An exception applies only when numeric calculations use an alternative representation within the treasury carry subsystem, subject to separate fractional ledger handling; the subsystem may use IEEE-754 binary representation and preserve fractional carry."

The mutation deliberately preserves the original literal prohibition anchor but adds a semantically conflicting exception.

The decision used:

- Category B.
- Decision ID D-990.
- Previous rule and replacement rule.
- Alternatives.
- Rationale.
- Consequences.
- Reopening conditions.
- Authorized B-14 §8.2 evidence location.
- The genuine quotation "No binary floating point; no fractional carry stated".
- A supports claim asserting permission for IEEE-754 binary representation and fractional carry.
- A matching amendment manifest.
- An updated source fingerprint.

### 3.3 Actual independent result

The complete numerical validator accepted this mutation.

All 53 checks returned no failures.

In particular:

- 14A-42 passed because the literal prohibition anchor remained present.
- 14A-45 passed despite the contradictory amendment evidence.
- 14A-48 passed because the amendment manifest was structurally valid.

The issue is not merely missing synonym coverage.

The issue is that the validator cannot reliably interpret the logical structure of the replacement clause, including its exceptions and scope.

This exact attack must become a permanent regression test.

## 4. CORRECTION A — REPLACE INADEQUATE STANCE DETECTION

### 4.1 Do not extend the current regex approach

Do not fix the defect by adding only:

- `IEEE-754`
- `binary32`
- `binary64`
- `fractional carry`
- `treasury subsystem`

as additional hardcoded strings.

Do not increase the number of arbitrary regular-expression windows and declare the semantic problem solved.

Do not return `supports` by default.

Unknown or incompletely understood propositions must not become supporting evidence automatically.

### 4.2 Required architecture: structured semantic contracts

Implement an explicit, deterministic semantic-contract mechanism for the controlled B-04 clauses.

The implementation should represent important statements as structured assertions rather than relying solely on free-text token overlap.

Use a consistent representation that can express:

- Clause identifier.
- Subject.
- Predicate.
- Object or numerical value.
- Modality.
- Positive or negative polarity.
- Scope.
- Conditions.
- Exceptions.
- Units.
- Timing.
- Source location.
- Provenance.

A suitable conceptual structure is:

`subject + predicate + object + modality + polarity + scope + conditions + exceptions`

The exact implementation format may follow the repository architecture.

The important requirement is that all material parts of the proposition are represented and validated.

### 4.3 F-EC-000b semantic coverage

The controlled contract must independently represent:

**A. Numeric domain**

- All quantities are integers.

**B. Arithmetic representation**

- Binary floating-point formula calculations are prohibited.
- Equivalent IEEE-754 binary floating-point representations must be recognized as belonging to the same controlled arithmetic concept.
- An exception allowing these representations must be detected even when the phrase "floating point" is absent from the exception itself.

**C. Division**

- Explicit rounding rules are required.
- Existing floor, ceil and round_half_up requirements must remain protected.
- Negative-value floor behaviour must not be confused with truncation toward zero.

**D. Percentage representation**

- Percentages are integer basis points.
- 10,000 bp = 100%.

**E. Fractional carry**

Represent fractional carry as a separate proposition.

Do not infer that a statement such as "no fractional carry stated" is an explicit prohibition of every possible fractional-carry operation.

It means the evidence does not establish permission or a rule for that operation unless the surrounding source establishes more.

Do not collapse independent propositions into one undifferentiated keyword test.

### 4.4 F-EC-000f preservation

Preserve the existing F-EC-000f semantic protections:

- v1.0 provisional calibration.
- Carried unchanged into v1.1.
- F-EC-044 relationship.
- Not observed prices.
- Not balance claims.
- Values change only through a new register revision.

The new architecture must not weaken these existing protections.

### 4.5 Synonym and terminology normalization

Use authoritative technical terminology where relevant.

The following are useful terminology references:

- IEEE Std 754-2019.
- ISO/IEC 60559:2020.
- NIST Digital Library of Mathematical Functions, §3.1.

Official sources:

https://standards.ieee.org/ieee/754/6210/

https://www.iso.org/standard/80985.html

https://dlmf.nist.gov/3.1

The standard terminology identifies binary floating-point arithmetic and formats such as binary32, binary64 and binary128.

Where technically justified, recognize equivalent terminology such as:

- IEEE-754 binary floating-point.
- Binary32.
- Binary64.
- Binary128.
- Single-precision binary floating point.
- Double-precision binary floating point.
- Float32/Float64 where the context establishes that they are floating-point representations.

Do not blindly treat every occurrence of "float", "double" or "binary representation" as equivalent.

Context, type and subject must be established.

Record the technical basis for terminology normalization.

External standards provide terminology and technical clarification only. They do not authorize changing Nation Supremacy's numerical rules.

### 4.6 Negation, exceptions and scope

The parser or structured validation mechanism must detect:

- Negation.
- Permission and prohibition.
- Must and may.
- Unless.
- Except.
- Only when.
- Where.
- Provided that.
- Notwithstanding.
- Conditional exceptions.
- Multiple sentences describing the same subject.
- Additional restrictions introduced after a semicolon.
- Scope changes.
- Exceptions applying to only one subsystem.
- An exception introduced much later in a sentence or paragraph.

An assertion may not be treated as fully compliant merely because one sentence contains the correct prohibition while another sentence adds an exception.

Every semantically relevant part of the controlled clause must be accounted for.

### 4.7 Complete clause coverage

This is mandatory.

The semantic parser must demonstrate that it has accounted for all material statements and qualifications in the complete controlled clause.

Unrecognized wording, unparsed exceptions, unknown conditions or unsupported modifiers must produce:

- NOT_ESTABLISHED, or
- SEMANTIC_PARSE_FAILURE.

They must not be silently ignored.

Do not allow a parser to recognize the first sentence and ignore a contradictory second sentence.

Do not accept a clause simply because the old prohibition phrase remains somewhere in its text.

### 4.8 Avoid unrestricted NLP

The implementation must remain:

- Deterministic.
- Reproducible.
- Explainable.
- Auditable.
- Compatible with the existing Python validation architecture.
- Free from paid runtime dependencies.
- Independent of external AI inference at validation time.

Use a finite, auditable grammar and typed proposition model appropriate to the two controlled B-04 contracts.

Do not attempt to claim that arbitrary English-language semantic understanding has been solved.

If wording cannot be parsed reliably, fail closed with an informative error.

## 5. CORRECTION B — SOURCE EVIDENCE AND PROVENANCE

### 5.1 Evidence must independently establish the proposition

The decision's own `supports` field must never be treated as proof.

The validator must independently determine whether the actual cited source content supports the exact proposition.

Each material assertion must be traced through:

1. Affected B-04 clause.
2. Parsed proposed change.
3. Specific evidence proposition.
4. Authorized source document.
5. Actual source section and content.
6. Source scope and conditions.
7. Computed evidence relationship.
8. D-014 decision authority.
9. Amendment manifest.
10. Source fingerprint.

### 5.2 Required evidence classifications

Use explicit classifications:

| Classification | Meaning |
|---|---|
| SUPPORTS | Source establishes the exact proposition |
| CONTRADICTS | Source conflicts with the proposition |
| QUALIFIES | Source supports only under specified conditions |
| CONTEXT_ONLY | Relevant background without proof |
| NOT_ESTABLISHED | Evidence does not establish the claim |
| INVALID_SOURCE | Source or provenance cannot be verified |
| PARSE_FAILURE | Material evidence content cannot be interpreted |

A contradiction must never be converted into support by keyword overlap.

Partial evidence coverage must not establish a complete amendment.

A qualifying condition must be included in the claim or the evidence must remain insufficient.

Absence of a statement must not automatically be interpreted as affirmative permission.

### 5.3 Controlled evidence mappings

Inspect the existing evidence allowlist and source contracts.

Where useful, establish a separately controlled evidence mapping containing:

- Evidence identifier.
- Document path.
- Section or exact source locator.
- Source version or fingerprint.
- Exact relevant excerpt.
- Proposition identifier.
- Semantic polarity.
- Scope.
- Conditions and qualifications.
- Evidence classification.
- Provenance and authorizing decision reference.

The mapping must be independent of the amendment manifest.

A decision or amendment manifest must not be able to authorize its own evidence mapping merely by supplying a new path or claim.

Any modification to a controlled evidence mapping must follow D-014 and be recorded with the appropriate authority, rationale, evidence and regression coverage.

The actual cited contents must still be validated.

A hash proves which bytes were referenced. It does not prove that those bytes support the proposition.

### 5.4 Provenance and traceability research basis

Use these standards as design references, not as substitutes for project authority:

W3C PROV-DM:

https://www.w3.org/TR/prov-dm/

NASA Systems Engineering Handbook:

https://www.nasa.gov/reference/system-engineering-handbook-appendix/

Relevant concepts include:

- Evidence source identity.
- Provenance.
- Quotation and derivation.
- Responsible agent.
- Unique assertion identifiers.
- Definitive source locations.
- Verification success criteria.
- Independent traceability assessment.

W3C PROV models provenance, but provenance alone does not prove semantic entailment. Implement the project's actual proposition validation separately.

## 6. CORRECTION C — PERMANENT D-990 REGRESSION

Create the exact Project X (103) D-990 attack as a permanent isolated negative regression.

Preserve:

- The original B-04 production source.
- Both source hashes.
- The empty production amendment manifest.

Use temporary in-memory overrides or isolated temporary files.

### Exact attack

Use this replacement clause wording:

"No formula uses binary floating point. An exception applies only when numeric calculations use an alternative representation within the treasury carry subsystem, subject to separate fractional ledger handling; the subsystem may use IEEE-754 binary representation and preserve fractional carry."

Use the genuine B-14 §8.2 quotation:

"No binary floating point; no fractional carry stated"

Use the misleading supports assertion:

"This passage establishes permission for IEEE-754 binary representation and fractional carry in numeric calculations."

Create a complete Category B D-990 fixture with:

- Previous rule.
- Replacement rule.
- Alternatives.
- Rationale.
- Consequences.
- Reopening conditions.
- Authorized source path and section.
- Matching source fingerprint.
- Matching amendment manifest.

Ensure all non-evidence structural and authorization requirements are valid.

### Expected result

**REJECT — CONTRADICTORY SEMANTIC CONTRACT / UNSUPPORTED EXCEPTION.**

The negative test must prove:

- 14A-45 rejects the amendment for evidence or semantic contradiction.
- 14A-48 remains structurally valid.
- The unrelated global B-04 anchor check does not produce the rejection.
- The failure is attributable to the actual semantic-contract violation.

The original D-990 fixture must not pass simply because of a missing decision, malformed manifest, hash mismatch or unrelated validator failure.

### Additional negative tests

Add permanent tests for:

1. IEEE-754 binary representation without the phrase "floating point".
2. Binary32 permission.
3. Binary64 permission.
4. Single/double precision exceptions.
5. A prohibition retained in the first sentence but contradicted by a later exception.
6. Exceptions introduced after long intervening text.
7. Treasury-specific exceptions.
8. Fractional carry permission.
9. Negation reversal.
10. Conditional permission.
11. Partial evidence coverage.
12. Unknown material clause wording.
13. Unparsed conditions.
14. Misleading evidence context.
15. Contradictory assertions from the same source.
16. Stale evidence fingerprints.
17. Unauthorized evidence mapping updates.

Every test must assert the correct semantic failure reason.

Do not create a fix that works only for the exact D-990 wording.

## 7. CORRECTION D — POSITIVE AMENDMENT REGRESSION

Preserve the legitimate positive amendment paths.

### Category A

A valid owner-authorized temporary test fixture must be accepted.

Do not create or insert a real owner approval into DECISIONS.md.

### Category B

A valid ordinary design amendment with genuinely supporting evidence must be accepted.

### Category C

A valid provisional decision must be accepted as Provisional.

Do not promote it to Confirmed or OWNER-APPROVED VALUE.

### Baseline

The unmodified Project X (103) production baseline must pass.

Do not make all amendments fail merely to prevent false acceptance.

## 8. CORRECTION E — PRESERVE ALL EXISTING VALIDATOR COVERAGE

Project X (103) baseline:

| Suite | Existing result |
|---|---:|
| Numerical validator | 53/53 |
| Self-tests | 128/128 |
| Decision-register tests | 12/12 |
| Next-action tests | 27/27 |
| Final validator | PASS |

All existing tests must remain intact.

Add the semantic-contract integrity check as the next available unique validator check, following the existing 14A-53 identifier.

Use the next available self-test identifiers.

Do not:

- Delete existing tests.
- Weaken existing assertions.
- Suppress existing failures.
- Skip failing tests.
- Convert actual failures into expected failures.
- Reuse test IDs improperly.
- Report a timeout as a pass.

Run the full existing self-test suite and all new negative and positive fixtures.

Report exact final counts.

## 9. CORRECTION F — DOCUMENTATION AND CLOSURE RECONCILIATION

### 9.1 Project X (103) actual link-validation baseline

The independent execution returned:

| Measure | Actual |
|---|---:|
| Markdown files | 130 |
| Total links | 4,367 |
| Local links | 3,985 |
| External links skipped | 382 |
| Anchors | 34 |
| Unresolved | 0 |

The progress log §106 and B-14 R1-R1-21 contain these values.

However, the following current records are stale:

- B-14 CLOSURE-26: 4,364 / 3,982.
- B-14 CLOSURE-27: 4,364 / 3,982.
- QA report §5.18: 4,364 / 3,982.

### 9.2 Reconciliation procedure

After every code, test, archive and documentation change is complete:

1. Execute the real documentation-link validator.
2. Capture its actual output.
3. Derive the final counts from execution.
4. Synchronize every current operational report.

Update:

- B-14 CLOSURE-26 and CLOSURE-27.
- QA report §5.18.
- Current B-14 link validation summary.
- Latest progress-log reconciliation.
- Current project progress summary.
- Current AI_HANDOFF.md.
- Current AI_CONTEXT.md.

Do not assume the final totals will remain 130/4,367/3,985. The new prompt archive and associated references may change the totals.

Use the actual final execution.

### 9.3 Preserve historical QA records

Do not rewrite historical snapshots.

In particular:

`QA report §5.16 — Evidence-relevance closure totals`

is explicitly historical and must remain unchanged.

Preserve earlier progress-log sections §103–§106 as historical records.

Do not retroactively replace the counts in earlier Project X audits.

### 9.4 Closure-register reconciliation

Inspect B-14's closure table.

The following existing records must be reviewed:

- CLOSURE-20: Previous 49 checks / 51 total.
- CLOSURE-21: Previous 94 tests / 118 total.
- CLOSURE-32: Prompt archive metadata.
- CLOSURE-35: Final handoff references Log §104.

The actual current validator baseline is 53 checks / 128 self-tests.

Do not silently rewrite a historical closure record if it describes an earlier snapshot.

Instead:

- Clearly label historical closure records with the prompt/snapshot they describe.
- Add new uniquely numbered closure records for the current correction.
- Ensure current closure summaries report the actual final test totals.
- Identify the exact prompt archive associated with every archive closure record.
- Update the latest handoff reference to the actual new progress-log section.

CLOSURE-32 currently contains metadata for an earlier correction archive. Preserve its actual historical association rather than replacing an older archive's identity.

### 9.5 Current status reconciliation

Project X (103) continuity documents currently state that Prompt 14A is ready for owner acceptance.

That statement must not remain the current status while the D-990 false acceptance is unresolved.

Update current summary sections to state:

**PROMPT 14A — OPEN / NOT READY FOR FINAL OWNER ACCEPTANCE UNTIL THE FINAL SEMANTIC-VALIDATION CORRECTION IS INDEPENDENTLY VERIFIED.**

Historical progress-log statements must remain historical.

Prompt 14B must continue to be recorded as NOT AUTHORIZED / NOT STARTED.

Preserve the owner's Prompt 13A–13D acceptance.

Do not reopen Prompt 13.

## 10. PRESERVATION REQUIREMENTS

| Protected item | Required preservation |
|---|---|
| Active formula identifiers | 295 |
| Parameter records | 393 |
| B-03 carry-ins | 20 |
| Formula registers | All nine |
| Previous numerical checks | All 53 |
| Previous self-tests | All 128 |
| Decision-register tests | All 12 |
| Next-action tests | All 27 |
| F-EC-000b baseline source hash | Unchanged |
| F-EC-000f baseline source hash | Unchanged |
| Production amendment manifest | Empty |
| D-014 policy | Unmodified |
| Historical decisions | Preserved |
| Previous correction archives | Preserved |
| Historical QA snapshots | Preserved |

Do not change any approved or provisional numerical values.

Do not make changes to the actual formula source text.

Do not modify existing owner-reserved decisions.

Preserve both current B-04 source hashes.

Do not create fabricated production amendment entries.

Do not touch unrelated existing modified files.

Do not clean the repository or perform Git operations.

## 11. UNIQUE PROMPT ARCHIVAL REQUIREMENTS

Archive this correction under the next unique identifier:

`14A-C1-R1-R1-C1-R1-C1-R1-R1-R1`

Exact archive path:

`docs/prompts/prompt_14A-C1-R1-R1-C1-R1-C1-R1-R1-R1_constrained_semantic_contract_validation_and_final_qa_reconciliation.md`

Requirements:

1. Store the complete correction prompt.
2. Update `docs/prompts/INDEX.md`.
3. Preserve the existing R1-R1 archive.
4. Preserve every previous correction archive.
5. Do not reuse the parent correction ID.
6. Verify the archive exists.
7. Record actual byte size.
8. Record actual SHA-256.
9. Verify the index entry.
10. Ensure all local links resolve.

Do not overwrite any previous correction archive.

## 12. FINAL VALIDATION

Execute all applicable checks after completing the correction.

### Numerical foundation

- Verify 295 active formulas.
- Verify 393 parameter records.
- Verify all 20 B-03 carry-ins.
- Verify all nine formula registers.
- Verify both source hashes.
- Verify the production amendment manifest remains empty.

### Semantic evidence validation

- Exact D-990 attack rejected.
- D-998 unrelated-evidence attack rejected.
- D-999 direct prohibition-as-permission attack rejected.
- IEEE-754 synonym attack rejected.
- Binary32/binary64 exception attacks rejected.
- Long-distance exception attack rejected.
- Scope and condition attacks rejected.
- Partial evidence coverage rejected.
- Unknown semantic content rejected safely.
- Positive A/B/C amendment fixtures accepted.
- Unchanged production baseline passes.

The D-990 attack must fail specifically for semantic contradiction.

A failure at an unrelated structural or anchor check is insufficient.

### Other validation

Execute:

1. Numerical foundation validator.
2. Complete existing and new self-tests.
3. Decision-register tests.
4. Next-action tests.
5. Final project validator.
6. Documentation-link validation.
7. Prompt archive integrity check.
8. Current QA consistency checks.
9. Git status inspection.

Run the mutation tests independently, not only through the included self-test suite.

Do not modify Git history.

Do not claim a clean repository unless actually verified.

## 13. REQUIRED FINAL REPORT

Provide an independently verifiable final report.

### A. Semantic-contract architecture

Explain:

- Actual implementation design.
- Typed proposition representation.
- Clause and exception parsing.
- Synonym normalization.
- Complete-clause coverage.
- Source evidence mapping.
- Provenance and fingerprints.
- Why the D-990 exception cannot bypass the validator.

### B. Negative regression results

| Mutation | Expected result |
|---|---|
| D-998 unrelated fair-play evidence | REJECT |
| D-999 prohibition-as-permission | REJECT |
| Exact D-990 attack | REJECT |
| IEEE-754 representation | REJECT |
| Binary32 permission | REJECT |
| Binary64 permission | REJECT |
| Long-distance exception | REJECT |
| Treasury-specific exception | REJECT |
| Fractional carry permission | REJECT unless independently established |
| Unsupported conditions | REJECT |
| Partial evidence | REJECT |
| Unknown material clause | REJECT |

Provide the actual rejection reason for every case.

### C. Positive regression results

| Test | Expected |
|---|---|
| Valid Category A | ACCEPT |
| Valid Category B | ACCEPT |
| Valid Category C | ACCEPT as Provisional |
| Unchanged production baseline | PASS |

### D. Validator results

Report actual final:

- Numerical foundation check count.
- Self-test count.
- New semantic test count.
- Decision-register test count.
- Next-action test count.
- Final project validator result.

Distinguish executed tests from tests merely present in the repository.

### E. Final documentation QA

Report all actual final link totals.

Identify every updated operational document.

Show that all current operational totals agree.

Confirm that historical reports were preserved.

### F. Preservation verification

Explicitly confirm all protected formula, parameter, source-hash, policy, manifest and historical-decision requirements.

### G. Repository and archive report

Report:

- Modified tracked files.
- Untracked files.
- Actual Git status.
- New archive path.
- Archive byte size.
- Archive SHA-256.
- Index verification.

Do not stage or commit anything.

### H. Final completion assessment

Choose exactly one:

- COMPLETE — ALL REQUIREMENTS VERIFIED.
- PARTIALLY COMPLETE — SPECIFIC DEFECTS REMAIN.
- NOT COMPLETE — CRITICAL REQUIREMENTS FAILED.

Do not claim owner acceptance.

Recommend final Prompt 14A owner acceptance only after every requirement is independently verified.

## 14. STRICT FINAL SCOPE BOUNDARY

This is the final narrowly scoped Prompt 14A semantic-validator correction.

Do not restart Prompt 14A.

Do not repeat the formula or parameter inventories.

Do not redesign the numerical architecture.

Do not implement the game.

Do not change numerical values.

Do not modify the D-014 policy.

Do not create unrelated security, gameplay, database or deployment tasks.

Do not manufacture tests or owner decisions.

Do not create another broad correction cycle.

If a genuinely independent critical defect is discovered, disclose its exact evidence and assess whether it can be resolved within this scope before proposing any new prompt.

If all requirements pass, recommend Prompt 14A final owner acceptance and stop.

**PROMPT 14B REMAINS NOT AUTHORIZED / NOT STARTED.**

Only the owner may authorize Prompt 14B.

---

# FINAL EXPECTATION

The objective is to prevent a numerical amendment from being authorized by an evidence quotation that contradicts the proposed change.

Preserve the actual meaning of source rules, including negation, exceptions, conditions, scope and technical terminology.

A phrase that retains the old prohibition while adding an exception must not be mistaken for a compliant rule.

Use structured, deterministic semantic contracts rather than another collection of special-case keywords.

Preserve all completed work.

Reconcile all current QA records using the actual final execution.

Verify everything independently.

**Fix the demonstrated defect. Prove the D-990 attack is rejected. Complete the QA reconciliation. Then stop.**
