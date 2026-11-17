# PROMPT 14A-C1-R1-R1-C1-R1 — D-014 AMENDMENT AUTHORIZATION EVIDENCE VALIDATION AND FINAL PROMPT 14A CLOSURE

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Master Game Design Bible  
**Parent phase:** Prompt 14 — Numbers, Formulas, Balance and Worked Examples  
**Original phase:** Prompt 14A — Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Correction chain:** Prompt 14A → C1 → C1-R1 → C1-R1-R1 → C1-R1-R1-C1 → C1-R1-R1-C1-R1  
**Execution type:** Final targeted validator and authorization-evidence correction  
**Implementation authorization:** NONE  
**Baseline:** Project X (99)  
**Next phase:** Prompt 14B — NOT STARTED / NOT AUTHORIZED  
**Authority:** D-014 — Autonomous Decision Policy

---

# 1. MISSION

Execute the final targeted correction identified during the independent audit of Project X (99).

The audit confirmed:

- F-EC-000b integer-arithmetic protection passes.
- F-EC-000f calibration-rule protection passes.
- All previously identified source-semantic mutations are rejected.
- The numerical foundation validator passes 47/47.
- The regression suite passes 78/78.
- The documentation-link reconciliation is complete.

One remaining validator weakness was identified.

The validator protects F-EC-000b and F-EC-000f using controlled source hashes and normative-content checks.

However, it does not independently verify that a qualifying D-014 decision authorizes a changed source clause before an updated controlled hash is accepted.

**A changed hash must not become an authorization mechanism.**

This correction must make the source-amendment process evidence-controlled.

It must distinguish:

1. An authorized amendment.
2. An unsupported source modification.
3. An unrelated decision reference.
4. A pending or rejected decision.
5. An owner-reserved amendment lacking required owner authorization.

The objective is to close this final validator weakness and prepare Prompt 14A for final independent acceptance.

Do not restart Prompt 14A.

Do not repeat or rebuild the existing formula and parameter inventories.

Do not change any current numerical values.

Do not start Prompt 14B.

---

# 2. MANDATORY GOVERNANCE

Before modifying anything:

1. Read the complete `docs/AUTONOMOUS_DECISION_POLICY.md`.
2. Read the existing D-014 amendment and decision-recording requirements.
3. Inspect the current `docs/DECISIONS.md`.
4. Inspect applicable DD and UD records.
5. Read the complete B-04 formula register.
6. Read the existing F-EC-000b and F-EC-000f source-contract validation code.
7. Read the current Prompt 14A validator.
8. Read the complete 78-test regression suite.
9. Read the Project X (99) B-14 acceptance and QA records.

Do not rely on a decision-summary excerpt when the complete decision record is needed.

## 2.1 Protected restrictions

You MUST NOT:

- Modify the Autonomous Decision Policy.
- Invent an amendment authorization rule.
- Invent an owner approval.
- Create a decision merely to justify an already performed unauthorized change.
- Resolve owner-reserved UDs.
- Change D-015 or D-019.
- Change the established B-04 formula definitions.
- Change any of the 295 active formulas.
- Change any of the 393 parameter values.
- Modify the current F-EC-000b or F-EC-000f normative content.
- Change the two-hour UTC cadence.
- Change P0–P7.
- Modify frontend, backend, database, SQL, API, security or deployment implementation.
- Modify gameplay prototypes.
- Perform Git operations.
- Start Prompt 14B or any subsequent subphase.

The current B-04 source clauses and their verified hashes must remain unchanged during this assignment.

---

# 3. CURRENT PROJECT X (99) BASELINE

Preserve all existing verified work.

| Item | Baseline |
|---|---:|
| Active formula identifiers | 295 |
| Parameter records | 393 |
| B-03 carry-ins | 20 |
| Numerical validator | 47/47 |
| Regression tests | 78/78 |
| Final project validator | PASS |
| Decision tests | 12/12 |
| Next-action tests | 27/27 |
| Documentation links | 4,347 |
| Unresolved links | 0 |

The latest recorded link baseline is:

- 126 Markdown files.
- 4,347 links.
- 3,965 local links.
- 382 external links skipped.
- 34 anchors.
- Zero unresolved.

Rerun final link validation after the correction archive has been added, because the final totals may increase.

Preserve all historical counts.

---

# 4. CORRECTION A — EXPLICIT D-014 AMENDMENT EVIDENCE

Strengthen the existing validator:

`docs/qa_backups/14A_validate_numerical_foundation.py`

The validator must not accept a changed B-04 source contract merely because:

- Its hash was updated.
- Its expected phrase was changed.
- Its source-contract manifest was modified.
- A D-number appears somewhere in the source.
- An unrelated decision is cited.
- A coding agent claims the change was authorized.

A changed normative source clause must have traceable authorization consistent with D-014.

## 4.1 Determine the proper authority first

Do not assume every amendment requires identical approval.

Inspect D-014 and determine the applicable authority for the specific amendment.

Respect:

- Category A fixed owner constraints.
- Category B ordinary design decisions.
- Category C provisional evidence-dependent decisions.
- Category D external, costly, legal or irreversible actions.

Where a decision is owner-reserved, the required owner authorization must be present.

Where an ordinary Category B decision is legitimately permitted, use the existing D-014 decision-recording procedure.

Where a value remains provisional or evidence-dependent, preserve its actual status.

Do not upgrade a Category C parameter merely because a source clause has been revised.

**The purpose is to verify the correct authority, not to invent a universal owner-approval requirement.**

## 4.2 Required amendment evidence

For any changed protected source clause, require a traceable decision record that establishes:

1. Exact affected source document.
2. Exact affected formula/clause identifier.
3. The proposed change.
4. The previous rule.
5. The replacement rule.
6. The decision authority.
7. The D-014 category.
8. Decision status.
9. Rationale.
10. Alternatives considered, where required by the decision process.
11. Evidence supporting the change.
12. Consequences and dependencies.
13. Reopening conditions.
14. Required owner authorization, if owner-reserved.

The decision must explicitly cover the actual proposed amendment.

A decision concerning the B-04 formula architecture cannot automatically authorize a change to F-EC-000b integer arithmetic.

A decision concerning initial Treasury calibration cannot automatically authorize changing F-EC-000f revision authority.

Do not accept unrelated decision references as authorization.

## 4.3 Active decision status

Inspect the actual decision-register conventions.

A qualifying decision must be in the status required by D-014 for the applicable category.

Do not accept:

- Proposed but unaccepted decisions.
- Pending owner decisions.
- Rejected decisions.
- Deferred decisions.
- Superseded decisions.
- Closed decisions that do not cover the amendment.
- Decision references with no actual supporting record.

A legitimately authorized amendment must remain distinguishable from a proposal awaiting authorization.

---

# 5. CONTROLLED SOURCE-CONTRACT MANIFEST

Inspect the existing implementation and choose a maintainable approach.

The source-contract baseline must distinguish:

- The currently verified baseline.
- The approved normative content.
- The authority for any future amendment.
- The updated source fingerprint.

The validator must never allow an operator to establish a new trusted hash solely by editing a constant.

## 5.1 Required relationship

The validation chain must be:

**Authoritative source → qualifying decision → authorized amendment → revised source contract → revised controlled hash → regression evidence.**

Every element must be traceable.

If any required element is missing, the amendment must not be accepted.

## 5.2 Source-contract amendment record

For an authorized future amendment, maintain a controlled record containing:

| Field | Required content |
|---|---|
| Source document | Canonical path |
| Clause identifier | F-EC-000b or F-EC-000f |
| Previous fingerprint | Verified previous hash |
| New fingerprint | Actual revised source hash |
| Decision ID | Applicable D-register identifier |
| DD reference | Where required |
| D-014 category | Applicable category |
| Decision status | Actual recorded status |
| Authorization evidence | Exact source |
| Amendment rationale | Actual documented reason |
| Regression evidence | Relevant test results |

Do not populate this record with invented future decisions.

For Project X (99), retain the existing original source-contract baseline.

There is no current B-04 amendment to authorize.

---

# 6. CORRECTION B — REQUIRED AUTHORIZATION MUTATION TESTS

Create permanent regression tests covering the amendment authorization path.

Every test must use temporary fixtures.

Do not change the real B-04 source registers, decision registers or controlled baseline during negative testing.

## 6.1 Mandatory negative tests

| Test | Expected |
|---|---|
| Change F-EC-000b without a decision | REJECT |
| Change F-EC-000f without a decision | REJECT |
| Change source and update its hash without a decision | REJECT |
| Change source and cite an unrelated D-number | REJECT |
| Change source and cite a decision covering a different clause | REJECT |
| Cite a proposed/pending decision | REJECT |
| Cite a rejected decision | REJECT |
| Cite a deferred decision | REJECT |
| Cite a superseded decision | REJECT |
| Update the manifest without supporting decision evidence | REJECT |
| Change the decision's affected clause after hashing | REJECT |
| Change the previous fingerprint | REJECT |
| Change the new fingerprint so it does not match source content | REJECT |
| Make an owner-reserved change without required owner authorization | REJECT |
| Modify only the authority status while leaving source text unchanged | REJECT |

## 6.2 Mandatory positive tests

| Test | Expected |
|---|---|
| Preserve the current Project X (99) B-04 source clauses | PASS |
| Preserve the current hashes | PASS |
| Preserve the current decision register | PASS |
| Preserve a legitimately documented source omission | PASS |
| A properly authorized Category B amendment fixture follows D-014 | PASS |
| A properly owner-authorized Category A amendment fixture follows D-014 | PASS, only where the policy permits the change |

Positive fixtures must model the actual D-014 procedure.

Do not use fabricated or generic approval evidence.

Do not invent a real D-number.

Use clearly identified temporary test fixtures for illustrative amendments.

## 6.3 Test the entire validation chain

Do not simply test an authorization helper in isolation.

Run the actual validator against:

- The unchanged baseline.
- A modified source with no decision.
- A modified source with unrelated decision evidence.
- A modified source with pending decision evidence.
- A modified source with valid applicable decision evidence.
- A manifest whose hash does not match the source.
- A manifest with a decision ID that does not match the affected clause.

The tests must demonstrate both failure and legitimate authorized-amendment behaviour.

---

# 7. PRESERVE THE EXISTING B-04 SAFEGUARDS

Do not weaken any previous source-semantic validation.

The following F-EC-000b protections must continue to work:

- Integer quantities.
- Explicit division rounding.
- `floor`, `ceil` and `round_half_up` definitions.
- Prohibition of binary floating-point formula calculations.
- Integer basis-point percentages.
- 10,000 bp = 100%.

The following F-EC-000f protections must continue to work:

- v1.0 provisional calibration.
- Carried unchanged into v1.1.
- F-EC-044 reference.
- No observed-price claim.
- No balance claim.
- Prompt 14 revision restriction.

All previous Treasury precision/rounding and owner-reserved protections must remain intact.

All earlier mutation tests from C1, R1 and R1-R1 must continue to pass.

---

# 8. FINAL VALIDATION

Before completion:

1. Run the complete numerical foundation validator.
2. Preserve all 47 existing validator checks.
3. Run all 78 existing regression tests.
4. Run all new amendment authorization tests.
5. Verify both current F-EC source clauses.
6. Verify their current source fingerprints.
7. Verify the current B-04 decision and authority records.
8. Execute all previous source-semantic mutation tests.
9. Execute all previous Treasury precision/rounding tests.
10. Execute all previous owner-reserved tests.
11. Verify all 295 active formula identifiers.
12. Verify all 393 parameter records.
13. Verify all 20 B-03 carry-ins.
14. Run relevant existing system validators.
15. Rerun documentation-link validation.
16. Update B-14 and QA records with actual final link totals.
17. Run the final project validator.
18. Run decision-register tests.
19. Run next-action tests.
20. Verify all prompt archive hashes and byte counts.
21. Inspect actual modified files.
22. Inspect Git status without changing it.
23. Verify the Autonomous Decision Policy is unchanged.
24. Verify no original formula definitions or numerical values changed.
25. Verify Prompt 14B has not been started.

Do not claim that an authorized future amendment has been tested merely because a helper function passed.

Show the actual mutation and validation results.

---

# 9. DOCUMENTATION AND PROMPT ARCHIVE

Only update files genuinely required by this correction.

At minimum inspect:

- `docs/qa_backups/14A_validate_numerical_foundation.py`
- Existing numerical validator test file.
- Existing controlled source-contract records.
- `docs/DECISIONS.md`
- Applicable DD/UD records.
- `docs/stage-2/22_formulas_and_balance.md`
- `docs/stage-2/22_numerical_baseline_qa_report.md`
- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/prompts/INDEX.md`

Do not modify F-EC-000b or F-EC-000f source content.

Do not invent a new D-register decision just to make the current validator pass.

## 9.1 Archive this correction prompt

Create the permanent verbatim archive:

`docs/prompts/prompt_14A-C1-R1-R1-C1-R1_D014_amendment_evidence_validation_and_final_closure.md`

Update `docs/prompts/INDEX.md`.

Record:

- Prompt ID.
- Full title.
- Archive path.
- Archive date.
- Exact byte count.
- SHA-256.

Verify the archived content against the complete supplied instruction.

Do not append unrequested provenance text.

Preserve every previous Prompt 14A archive.

---

# 10. ACCEPTANCE GATES

| Gate | Acceptance objective |
|---|---|
| FINAL-R1-01 | Complete D-014 review |
| FINAL-R1-02 | Current F-EC-000b source verified |
| FINAL-R1-03 | Current F-EC-000f source verified |
| FINAL-R1-04 | Current controlled hashes verified |
| FINAL-R1-05 | Unauthorized source changes rejected |
| FINAL-R1-06 | Hash updates without decisions rejected |
| FINAL-R1-07 | Unrelated D-number references rejected |
| FINAL-R1-08 | Wrong-clause decision references rejected |
| FINAL-R1-09 | Pending/rejected/deferred decision references rejected |
| FINAL-R1-10 | Applicable D-014 decision authority verified |
| FINAL-R1-11 | Owner-reserved amendments require the applicable authorization |
| FINAL-R1-12 | Proper authorized amendment fixture accepted |
| FINAL-R1-13 | All previous source-semantic protections preserved |
| FINAL-R1-14 | All Treasury precision/rounding safeguards preserved |
| FINAL-R1-15 | All owner-reserved safeguards preserved |
| FINAL-R1-16 | All 47 previous validator checks preserved |
| FINAL-R1-17 | All 78 previous regression tests preserved |
| FINAL-R1-18 | New amendment mutation suite passes |
| FINAL-R1-19 | 295 formulas unchanged |
| FINAL-R1-20 | 393 parameter records unchanged |
| FINAL-R1-21 | Final link totals reconciled |
| FINAL-R1-22 | Final project validator passes |
| FINAL-R1-23 | Prompt archive and SHA-256 verified |
| FINAL-R1-24 | Policy and owner decisions preserved |
| FINAL-R1-25 | No implementation or Git operations |
| FINAL-R1-26 | Final Prompt 14A handoff prepared |

Use:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

Do not report a PASS without actual execution evidence.

---

# 11. STRICT SCOPE CONTROL

This is intended as the final Prompt 14A correction.

Do not restart the phase.

Do not rebuild the formula inventory.

Do not rebuild the parameter inventory.

Do not recalibrate values.

Do not redesign source formulas.

Do not fix unrelated inherited validators.

Do not rewrite historical progress records.

Do not reopen Prompt 13.

Do not create unnecessary correction cycles.

If an unrelated issue is discovered, report it separately without expanding this assignment.

If D-014 leaves a genuine authority question unresolved, report the precise ambiguity rather than deciding it.

---

# 12. FINAL HANDOFF

The final report must contain:

1. Project X (99) starting baseline.
2. Current F-EC-000b and F-EC-000f hashes.
3. D-014 amendment validation method.
4. Results of every negative mutation.
5. Results of every positive authorization fixture.
6. Confirmation that hash updates alone cannot authorize source changes.
7. Confirmation that unrelated D-numbers cannot authorize amendments.
8. Confirmation that owner-reserved amendments retain their proper authority.
9. Preservation of all 47 existing validator checks.
10. Preservation of all 78 existing regression tests.
11. New test totals.
12. Final documentation-link totals.
13. Exact files modified.
14. Confirmation that all 295 formulas remain unchanged.
15. Confirmation that all 393 parameter records remain unchanged.
16. Confirmation that D-014 and owner-reserved decisions remain intact.
17. Confirmation that no implementation or Git operations occurred.
18. Prompt archive SHA-256 and byte count.
19. Final acceptance-gate assessment.
20. Remaining limitations, if any.
21. The single next action.

---

# 13. FINAL SUCCESS CONDITION

This correction is complete only when:

- Both B-04 source clauses remain protected.
- Unsupported source modifications fail.
- Updating a source hash without qualifying decision evidence fails.
- Unrelated decision references fail.
- Pending, rejected, deferred and superseded decision references fail.
- Legitimately authorized amendment fixtures pass through the correct D-014 process.
- Owner-reserved amendments retain their proper authorization requirements.
- All previous 47 validator checks remain intact and passing.
- All previous 78 regression tests remain intact and passing.
- New amendment tests pass.
- The current B-04 source and hashes remain unchanged.
- All 295 formula definitions remain unchanged.
- All 393 parameter records remain unchanged.
- Final documentation-link counts match the actual final execution.
- Historical records remain preserved.
- The correction prompt is archived verbatim and verified.
- No implementation work or Git operations occurred.
- No subsequent Prompt 14 phase was started.

When all requirements pass, report:

**PROMPT 14A — NUMERICAL FOUNDATION COMPLETE.**

**PROMPT 14A-C1 — COMPLETE.**

**PROMPT 14A-C1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1-C1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1-C1-R1 — COMPLETE.**

**PROMPT 14A — READY FOR FINAL OWNER ACCEPTANCE.**

**NEXT ACTION: AWAIT EXPLICIT OWNER AUTHORIZATION OF PROMPT 14B.**

If any condition remains unresolved, identify the exact gate and evidence. Do not start another broad correction cycle.

**END OF PROMPT 14A-C1-R1-R1-C1-R1**
