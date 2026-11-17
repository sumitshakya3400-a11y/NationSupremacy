# PROMPT 14A-C1-R1-R1-C1 — B-04 SOURCE SEMANTIC VALIDATION AND FINAL DOCUMENTATION-LINK RECONCILIATION

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Master Game Design Bible  
**Parent phase:** Prompt 14 — Numbers, Formulas, Balance and Worked Examples  
**Original phase:** Prompt 14A — Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Correction chain:** Prompt 14A → C1 → C1-R1 → C1-R1-R1 → C1-R1-R1-C1  
**Execution type:** Final targeted documentation-validator and QA reconciliation  
**Implementation authorization:** NONE  
**Starting snapshot:** Project X (98)  
**Next phase:** Prompt 14B — NOT STARTED / NOT AUTHORIZED  
**Authority:** D-014 — Autonomous Decision Policy

---

# 1. MISSION

Execute the final targeted correction identified during the independent audit of Project X (98).

The audit confirmed that:

- The original 295 formula inventory is complete.
- All 393 numerical parameter records are present.
- The two previous Treasury precision/rounding and owner-reserved defects have been corrected.
- The Prompt 14A validator reports 44/44 checks passing.
- The regression suite reports 64/64 passing.
- The final project validator passes.

However, two additional defects remain.

**Finding A — B-04 source semantic validation**

The validator does not detect certain changes to the actual authoritative B-04 integer-arithmetic and calibration-authority statements.

**Finding B — Final documentation-link reconciliation**

B-14 §15.5 reports 124 Markdown files, while the actual Project X (98) documentation-link execution reports 125 Markdown files.

Correct both issues.

This must be a narrow final correction, not another redesign or broad audit.

Preserve all completed Prompt 14A, C1, R1 and R1-R1 work.

Do not change numerical values, formulas, system mechanics or owner decisions.

Do not start Prompt 14B.

---

# 2. MANDATORY GOVERNANCE

Before modifying anything:

1. Read the complete `docs/AUTONOMOUS_DECISION_POLICY.md`.
2. Follow D-014 and applicable owner-reserved restrictions.
3. Inspect the actual Project X (98) repository.
4. Read the complete B-04 economic formula register.
5. Read the existing Prompt 14A validator.
6. Read all previous Prompt 14A correction archives.
7. Read the B-14 numerical architecture.
8. Inspect the latest decision and UD registers.
9. Inspect the actual final documentation-link validator output.

## 2.1 Strict restrictions

You MUST NOT:

- Modify the Autonomous Decision Policy.
- Change any of the 295 formula definitions.
- Change any of the 393 numerical parameter values.
- Change the B-04 starting treasury.
- Change production, prices, research, upkeep, taxation or other balance values.
- Rewrite the B-04 authoritative register merely to make its validator pass.
- Invent a new numerical authority.
- Invent an owner approval.
- Resolve any owner-reserved UD.
- Change D-015 or D-019.
- Change the two-hour UTC cadence or P0–P7.
- Modify gameplay implementation or prototypes.
- Modify frontend, backend, database, SQL, API, security or deployment systems.
- Perform Git operations.
- Stage, commit, push, reset, revert or discard files.
- Start Prompt 14B or any later subphase.

All modifications must remain within this correction's scope.

---

# 3. PROJECT X (98) VERIFIED BASELINE

Preserve the existing verified results.

## 3.1 Formula inventory

| System | Active formulas |
|---|---:|
| B-04 | 47 |
| B-05 | 41 |
| B-06 | 44 |
| B-07 | 39 |
| B-08 | 12 |
| B-09 | 8 |
| B-10 | 39 |
| B-11 | 49 |
| B-12 | 16 |
| **Total** | **295** |

Retired `F-WEP-048` remains excluded.

## 3.2 Numerical parameter inventory

Total: **393 parameter records**.

Preserve all records and their existing source mappings.

## 3.3 Existing validation baseline

| Test | Project X (98) result |
|---|---:|
| Numerical foundation validator | 44/44 |
| Numerical foundation self-tests | 64/64 |
| Final project validator | PASS |
| Decision-register tests | 12/12 |
| Next-action tests | 27/27 |

All these existing tests must remain intact and pass after this correction.

---

# 4. CORRECTION A — B-04 SOURCE SEMANTIC VALIDATION

**Highest priority.**

Authoritative source:

`docs/stage-2/10_economic_formula_and_balance_register.md`

The following two B-04 rules are particularly important.

## 4.1 F-EC-000b — Integer arithmetic

The current authoritative statement in Project X (98) is:

**F-EC-000b — Integer arithmetic.**

"All quantities are integers. Every division states its rounding: `floor` (toward negative infinity for negative values; toward zero for the positive values used here), `ceil` or `round_half_up`. No formula uses binary floating point. A percentage is an integer in basis points (bp), where 10,000 bp = 100%."

The validator must protect the actual operative rule.

It must detect a modification such as:

"All quantities may be decimal fractions."

It must also detect removal or reversal of the statement prohibiting binary floating-point formula calculations.

The following must remain independently verifiable:

- Integer quantities.
- Explicit division rounding.
- Supported rounding methods.
- No binary floating-point formula calculations.
- Integer basis-point percentages.
- 10,000 bp = 100%.

Do not simply check whether `F-EC-000b` exists.

Verify its substantive normative content.

## 4.2 F-EC-000f — Versioned constants and calibration authority

The current authoritative statement in Project X (98) is:

**F-EC-000f — Constants are versioned.**

"The constants below are the v1.0 provisional calibration, carried unchanged into v1.1 (see F-EC-044). They are not observed prices and not balance claims. Prompt 14 may change a value only by a new revision of this register."

The validator must verify:

- The v1.0 provisional calibration classification.
- Its documented relationship to v1.1.
- The F-EC-044 reference.
- The distinction between provisional calibration and observed prices.
- The distinction between provisional calibration and a balance claim.
- The rule that Prompt 14 changes a value only through a new revision of the register.

Do not replace the existing authority statement with an invented requirement that only the project owner may revise the register.

Preserve the actual D-014 decision boundaries.

## 4.3 The two independently reproduced mutations

The Project X (98) audit tested these modifications against temporary source copies.

Both were incorrectly accepted.

They must become permanent regression tests.

### Mutation 1 — Integer arithmetic rule

Original:

"All quantities are integers."

Mutation:

"All quantities may be decimal fractions."

Expected result: **REJECT**

### Mutation 2 — Calibration authority

Original:

"Prompt 14 may change a value only by a new revision of this register."

Mutation:

"Only the project owner may change a value by a new revision of this register."

Expected result: **REJECT**, because it changes the actual established source rule without an authorized amendment.

## 4.4 Additional negative tests

Also test:

| Mutation | Expected |
|---|---|
| Remove the binary floating-point prohibition | REJECT |
| Permit floating-point formula calculations | REJECT |
| Remove explicit division-rounding requirements | REJECT |
| Change basis-point relationship | REJECT |
| Change 10,000 bp = 100% | REJECT |
| Remove the provisional-calibration classification | REJECT |
| Change v1.0/v1.1 relationship | REJECT |
| Remove F-EC-044 reference | REJECT |
| Change provisional calibration into observed-price claims | REJECT |
| Change the register-revision restriction | REJECT |
| Preserve exact current source rules | PASS |

All negative tests must operate on temporary fixtures.

Do not mutate the real B-04 source register.

---

# 5. IMPLEMENTATION OF SOURCE SEMANTIC PROTECTION

Strengthen:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Do not create a disconnected validator.

## 5.1 Validate operative source content

The validator must check the actual content of F-EC-000b and F-EC-000f.

Checking only:

- Formula IDs.
- Section headings.
- Hash existence.
- Required keyword presence.

is insufficient.

It must detect changes that reverse or weaken the rule.

Use a deterministic method capable of distinguishing the approved current source language from unsupported modifications.

A suitable approach may combine:

1. Source-section extraction.
2. Normalized normative-clause comparison.
3. Required semantic element checks.
4. Approved source-contract fingerprints.
5. Explicit regression fixtures.

Select the most maintainable approach consistent with the existing validator architecture.

## 5.2 Controlled source-contract baseline

Establish an independently traceable baseline for the two authoritative clauses.

Record:

- Source document path.
- Formula ID.
- Source section.
- Applicable source version.
- Expected normative content.
- Normalized source fingerprint where used.
- Why the clause is protected.
- What evidence would permit a legitimate future change.

The baseline must not be generated from the potentially mutated text during the same validation operation.

Otherwise, the validator would validate a changed source against itself.

## 5.3 Legitimate future amendments

Do not permanently prohibit legitimate authorized amendments.

The validator must allow a future change only when:

- The appropriate authority has approved the amendment under D-014.
- The applicable decision evidence is present.
- The canonical B-04 register is revised consistently.
- The controlled expected source contract is deliberately updated.
- The update is documented and regression-tested.

Do not invent additional owner approval requirements where the existing policy does not require them.

Do not allow an unsupported amendment merely because the source text changed.

## 5.4 Fail-closed behaviour

If the clause is:

- Missing.
- Unparseable.
- Ambiguous.
- Inconsistent with the expected normative contract.
- Changed without the applicable authority evidence.

the validator must report the exact problem and return a non-zero exit code.

Do not silently skip a source contract.

Do not convert parser failure into PASS.

Do not claim semantic verification based solely on the existence of an identifier.

---

# 6. REQUIRED SOURCE-SEMANTIC REGRESSION SUITE

Add regression tests covering both clauses.

At minimum:

**F-EC-000b:**

- Correct integer rule passes.
- Decimal-fraction mutation fails.
- Floating-point permission mutation fails.
- Missing rounding requirement fails.
- Missing basis-point rule fails.
- Incorrect basis-point relationship fails.

**F-EC-000f:**

- Correct provisional versioning rule passes.
- Changed provisional classification fails.
- Removed F-EC-044 reference fails.
- Unsupported observed-price claim fails.
- Unsupported balance-claim promotion fails.
- Altered register-revision authority fails.
- An appropriately evidenced legitimate amendment follows the documented amendment path.

Tests must verify actual validator output and exit code.

Do not test only individual helper functions.

Run the full validator against temporary mutated source files.

---

# 7. CORRECTION B — B-14 DOCUMENTATION-LINK COUNT

The Project X (98) independent audit established:

| Measure | Actual result |
|---|---:|
| Markdown files scanned | 125 |
| Total links checked | 4,341 |
| Local links | 3,959 |
| External links skipped | 382 |
| Anchors | 34 |
| Unresolved links | 0 |

The corresponding B-14 acceptance entry is:

`docs/stage-2/22_formulas_and_balance.md`

Section:

`§15.5 Prompt 14A-C1-R1-R1 final correction gates`

Gate:

`R1-R1-21`

It currently reports:

**124 files; 0 unresolved; index rows match**

This is stale.

## 7.1 Required correction

Correct the documentation-link evidence in R1-R1-21.

However, do not blindly replace 124 with 125.

This correction will create one new permanent Markdown prompt archive. That archive may change the total number of scanned Markdown files.

Therefore:

1. Record the Project X (98) baseline of 125 Markdown files.
2. Create and verify the new correction prompt archive.
3. Execute the actual documentation-link validator after all modifications.
4. Record the exact final Markdown-file count.
5. Record the exact final link count.
6. Record local links.
7. Record external links skipped.
8. Record anchors.
9. Record unresolved links.
10. Update R1-R1-21 using the actual final output.

If the final count remains 125, report 125.

If the new archive increases it to 126, report 126.

Never invent or assume the final count.

## 7.2 Historical preservation

Preserve the existing historical link counts for earlier Project X snapshots.

Do not rewrite:

- Project X (94) historical records.
- Project X (95) historical records.
- Project X (96) historical records.
- Project X (97) historical records.
- Project X (98) baseline evidence.

Update only the current final acceptance evidence where necessary.

## 7.3 Final QA report reconciliation

Ensure the following records agree:

- B-14 §15.5.
- `docs/stage-2/22_numerical_baseline_qa_report.md`.
- `docs/stage-2/06_stage_2_progress_log.md`.
- Any relevant current Prompt 14A handoff.

All current final link totals must come from the same final execution.

Do not create competing current totals.

---

# 8. REQUIRED FILE CHANGES

Keep changes restricted to the actual affected files.

At minimum inspect:

1. `docs/qa_backups/14A_validate_numerical_foundation.py`
2. Existing Prompt 14A self-test/regression mechanism.
3. `docs/stage-2/22_formulas_and_balance.md`
4. `docs/stage-2/22_numerical_baseline_qa_report.md`
5. `docs/stage-2/06_stage_2_progress_log.md`
6. `docs/prompts/INDEX.md`

Only modify additional files if actual evidence requires it.

Do not rewrite the formula inventory or parameter inventory.

Do not modify any original formula register.

---

# 9. FINAL PROMPT ARCHIVE

Archive this complete correction instruction verbatim at:

`docs/prompts/prompt_14A-C1-R1-R1-C1_B04_source_semantic_validation_and_final_link_reconciliation.md`

Update:

`docs/prompts/INDEX.md`

Record:

- Prompt ID.
- Full title.
- Canonical archive path.
- Archive date.
- Exact byte count.
- SHA-256.

Verify that the archive matches this supplied instruction.

Do not append unrequested provenance paragraphs.

Preserve the prior Prompt 14A archive files.

---

# 10. ACCEPTANCE GATES

Create or update a focused correction acceptance record.

| Gate | Acceptance objective |
|---|---|
| FINAL-C1-01 | Complete governance and policy review |
| FINAL-C1-02 | F-EC-000b integer rule semantically validated |
| FINAL-C1-03 | F-EC-000b rounding requirements validated |
| FINAL-C1-04 | F-EC-000b floating-point prohibition protected |
| FINAL-C1-05 | F-EC-000b basis-point relationship protected |
| FINAL-C1-06 | F-EC-000f calibration-version rule validated |
| FINAL-C1-07 | F-EC-000f provisional classification preserved |
| FINAL-C1-08 | F-EC-000f F-EC-044 reference preserved |
| FINAL-C1-09 | F-EC-000f calibration claims remain correct |
| FINAL-C1-10 | F-EC-000f register-revision rule protected |
| FINAL-C1-11 | Both original semantic mutations rejected |
| FINAL-C1-12 | Additional semantic regression tests pass |
| FINAL-C1-13 | Legitimate baseline source passes |
| FINAL-C1-14 | Authorized amendment handling documented |
| FINAL-C1-15 | No original formula definitions changed |
| FINAL-C1-16 | No numerical parameter values changed |
| FINAL-C1-17 | B-14 §15.5 final link count reconciled |
| FINAL-C1-18 | All current QA records show identical final link totals |
| FINAL-C1-19 | Documentation-link validator passes |
| FINAL-C1-20 | Final project validator passes |
| FINAL-C1-21 | Existing 44 validator checks preserved |
| FINAL-C1-22 | Existing 64 self-tests preserved |
| FINAL-C1-23 | Previous C1/R1/R1-R1 regressions remain passing |
| FINAL-C1-24 | New correction prompt archived verbatim |
| FINAL-C1-25 | Prompt index hash and byte count verified |
| FINAL-C1-26 | Owner-reserved decisions preserved |
| FINAL-C1-27 | No implementation or Git operations occur |
| FINAL-C1-28 | Final handoff prepared |

Use:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

Do not mark a gate PASS without actual evidence.

---

# 11. FINAL VALIDATION

Before completion:

1. Run the full numerical foundation validator.
2. Run all existing 64 self-tests.
3. Run all new F-EC-000b and F-EC-000f semantic tests.
4. Verify both original semantic mutations are rejected.
5. Verify all previous Treasury precision/rounding protections remain intact.
6. Verify all previous owner-reserved protections remain intact.
7. Verify all nine original C1-R1 mutation protections.
8. Verify the 295 formula inventory.
9. Verify all 393 parameter records.
10. Verify no original formula register changed.
11. Execute the final documentation-link validator.
12. Update B-14 §15.5 with the final actual scan totals.
13. Reconcile the QA report and progress log.
14. Run the final project validator.
15. Run decision-register tests.
16. Run next-action tests.
17. Verify all prompt archive hashes.
18. Verify the newly archived instruction is verbatim.
19. Inspect all modified files.
20. Inspect Git status without modifying it.
21. Confirm the Autonomous Decision Policy is unchanged.
22. Confirm no gameplay or prototype implementation changed.
23. Confirm Prompt 14B was not started.

Report inherited validator limitations separately.

Do not claim that numerical balance or gameplay behaviour has been proven.

---

# 12. STRICT SCOPE CONTROL

This is a final targeted reconciliation.

Do not:

- Restart Prompt 14A.
- Rebuild the 393-record inventory.
- Rebuild the 295-formula inventory.
- Rewrite B-04.
- Recalibrate any value.
- Redesign any formula.
- Create additional game mechanics.
- Fix unrelated legacy validators.
- Reopen accepted Prompt 13 phases.
- Change unrelated historical records.
- Introduce another broad documentation restructuring.

Any unrelated observation must be recorded without expanding this assignment.

If the actual source reveals a genuine authority ambiguity, report it rather than inventing a decision.

---

# 13. FINAL HANDOFF

Produce a completion report containing:

1. Project X (98) baseline.
2. Exact F-EC-000b source validation results.
3. Exact F-EC-000f source validation results.
4. Result of both previously missed semantic mutations.
5. Additional positive and negative regression results.
6. Full preservation of previous 44 validator checks and 64 self-tests.
7. Final Markdown-file count.
8. Final total-link count.
9. Final local-link count.
10. Final external-link count.
11. Final anchor count.
12. Final unresolved-link count.
13. B-14 §15.5 reconciliation result.
14. Exact files modified.
15. Confirmation that the 295 formulas and 393 parameters remain unchanged.
16. Confirmation that owner-reserved decisions remain intact.
17. Prompt archive byte count and SHA-256.
18. Final acceptance-gate table.
19. Any inherited limitations.
20. The single next action.

The final recommendation must be:

- COMPLETE.
- PARTIAL.
- NOT COMPLETE.

Do not claim COMPLETE if either semantic mutation is still accepted or the final link-count evidence remains inconsistent.

---

# 14. FINAL SUCCESS CONDITION

This correction is complete only when:

- The integer-arithmetic rule is semantically protected.
- The division-rounding rules are semantically protected.
- The floating-point prohibition is semantically protected.
- The basis-point relationship is semantically protected.
- The versioned provisional-calibration rule is protected.
- The calibration-authority statement is protected.
- Both previously missed source-semantic mutations are rejected.
- All additional semantic tests pass.
- Legitimate baseline source text passes.
- All previous 44 validator checks and 64 self-tests remain intact and passing.
- The earlier Treasury and owner-reserved protections remain intact.
- The final documentation-link count is based on an actual execution.
- B-14 §15.5 agrees with the QA report and progress log.
- The 295 formulas remain unchanged.
- The 393 parameter records remain unchanged.
- Owner-reserved decisions and D-014 remain untouched.
- The new prompt archive is verified.
- All final acceptance gates have actual evidence.
- No implementation or Git operations occurred.
- No subsequent Prompt 14 subphase was started.

When every condition passes, report:

**PROMPT 14A — NUMERICAL FOUNDATION COMPLETE.**

**PROMPT 14A-C1 — COMPLETE.**

**PROMPT 14A-C1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1-C1 — COMPLETE.**

**PROMPT 14A — READY FOR FINAL OWNER ACCEPTANCE.**

**NEXT ACTION: AWAIT EXPLICIT OWNER AUTHORIZATION OF PROMPT 14B.**

If any condition remains unresolved, report its exact gate and evidence. Do not create another broad correction cycle for unrelated issues.

**END OF PROMPT 14A-C1-R1-R1-C1**
