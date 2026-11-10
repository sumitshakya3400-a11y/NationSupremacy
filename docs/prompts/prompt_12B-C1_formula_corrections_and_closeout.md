# PROMPT 12B-C1 — FORMULA CORRECTIONS, INTEGRATION TRACEABILITY, PROMPT ARCHIVAL AND FINAL DOCUMENTATION CLOSEOUT

**Stage:** Stage 2 — System Design  
**Phase:** Prompt 12B-C1  
**Parent Phase:** Prompt 12B — Complete System Specifications  
**Objective:** Correct identified defects and complete the remaining documentary and governance closeout.  
**Authorization:** Owner-authorized corrective documentation task.  
**Working Environment:** Existing live Nation Supremacy project directory.  
**Implementation Authority:** Documentation, specifications, registers and validators only.

---

# 1. MANDATORY STARTING INSTRUCTIONS

Before beginning:

1. Work directly inside the existing live Nation Supremacy project directory.
2. Read `AUTONOMOUS_DECISION_POLICY.md` completely.
3. Follow D-014 throughout this task.
4. Inspect the existing Prompt 12B deliverables and relevant canonical project documents.
5. Inspect existing prompt-file naming and directory conventions.
6. Preserve the existing architecture, naming conventions, identifiers and historical records.

**Important working-environment distinction:**

The coding agent works directly in the existing live project directory.

ZIP archives created by the owner are independent audit snapshots for external review. They are not working projects.

Do not:
- Extract or use an owner-provided audit ZIP as the working project.
- Create another project directory.
- Create a duplicate working copy.
- Replace the live project with an archive.
- Overwrite existing project work.

All corrections must be made in the existing live project directory.

Do not perform Git staging, committing or pushing without explicit owner authorization.

---

# 2. TASK OBJECTIVE

Prompt 12B has already produced its major specification package.

The purpose of Prompt 12B-C1 is to correct specific defects identified during independent review and complete the two remaining documentary/governance obligations.

This is a targeted corrective pass.

**Do not rewrite Prompt 12B or unnecessarily restructure its completed specifications.**

Preserve the existing four principal deliverables:

1. `docs/stage-2/20_fair_play_and_player_protection.md`
2. `docs/stage-2/20_fair_play_and_player_protection_requirements.md`
3. `docs/stage-2/20_fair_play_and_player_protection_formula_register.md`
4. `docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

Make focused corrections only where evidence demonstrates a defect.

---

# 3. CORRECTION 1 — FORMULA F-FP-002

**Priority: High**

Inspect F-FP-002 in:

`docs/stage-2/20_fair_play_and_player_protection_formula_register.md`

The previously audited expression was:

`C = min(max(V_law - V_obs, 0), B_i)`

Its example used:

- V_law = 100
- V_obs = 140
- B_i = 40
- Claimed result: C = 40

However, the actual mathematical result is:

`min(max(100 - 140, 0), 40) = 0`

This is inconsistent.

Required work:

1. Inspect the complete definition of F-FP-002.
2. Inspect the associated correction rules in the authoritative rulebook.
3. Inspect all dependent formulas and references.
4. Determine the intended economic meaning of every variable.
5. Correct the expression, example or both, as justified by the actual specification.
6. Ensure the corrected formula produces the intended result.
7. Add boundary examples, including:
   - No discrepancy.
   - Positive discrepancy.
   - Negative discrepancy.
   - Zero correction.
   - Correction exceeding the applicable cap.
   - Missing or invalid input.

Do not blindly reverse the subtraction merely to make the previous example pass.

Verify the intended semantics first.

Update all dependent references and examples.

---

# 4. CORRECTION 2 — FORMULA F-FP-014 AND ACCOUNTING SIGN CONVENTIONS

**Priority: High**

Inspect F-FP-014 and the related accounting correction rules.

The previously audited expression was:

`O + L - C - R + P - X = Z`

The specification does not adequately establish whether correction and reversal amounts are unsigned magnitudes or signed ledger effects.

This creates ambiguity.

Required work:

1. Inspect the complete accounting and correction model.
2. Inspect COR-003 and all dependent rules.
3. Establish an explicit ledger sign convention.
4. Define the treatment of:
   - Original transactions.
   - Corrective transactions.
   - Reversals.
   - Compensation.
   - Illicit benefit removal.
   - Administrative adjustments.
5. Establish whether the formula uses signed entries or unsigned amounts with explicit directional operators.
6. Verify that reversing an earlier correction produces the correct opposite effect.
7. Verify that corrections do not duplicate original transactions.
8. Preserve historical transactions where compensating entries are required.
9. Add worked examples covering ordinary corrections and reversals.

Ensure the formula and the authoritative rulebook use the same accounting convention.

Do not introduce a new economic policy or unsupported numerical parameter.

---

# 5. CORRECTION 3 — REPEAT-VIOLATION FORMULA CONSISTENCY

**Priority: High**

Inspect:

- F-FP-001.
- F-FP-011.
- All related severity and penalty rules.

The earlier audit identified a potential double-counting problem.

F-FP-001 includes confirmed prior violations in severity.

F-FP-011 additionally uses the prior-violation count.

This may be intentional, but the specification must demonstrate that the effects are distinct and justified.

Required work:

1. Identify exactly how prior violations influence severity.
2. Identify exactly how they influence penalty calculations.
3. Determine whether the same aggravating factor is counted twice.
4. Distinguish:
   - Violation severity.
   - Repeat-offender classification.
   - Conduct-sanction adjustment.
   - Economic correction.
5. Ensure economic correction is not improperly increased merely because a player has previous violations.
6. Preserve the requirement that economic corrections and conduct sanctions have independent justifications.
7. Add examples demonstrating the resulting behavior.
8. Update related requirements and rulebook references where necessary.

Do not invent new penalty coefficients or approve provisional values.

---

# 6. CORRECTION 4 — FORMULA AND NUMERICAL PARAMETER REGISTER COMPLETENESS

**Priority: High**

Inspect all 16 formulas and all 12 numerical parameters.

Specifically investigate the previously identified parameter references:

- Variable `f` in F-FP-009.
- Parameter `A₀`, identified as FP-P07.
- Variable `w` in F-FP-008.

Required work:

1. Inventory every independently configurable numerical input used by every formula.
2. Check whether each input has a corresponding parameter-register entry.
3. Check for parameters referenced in formulas but missing from the register.
4. Check for unused or incorrectly referenced parameters.
5. Verify units and dimensional consistency.
6. Verify lower and upper bounds.
7. Verify null and missing-value behavior.
8. Verify default behavior.
9. Verify rounding rules.
10. Verify approval authority and status.
11. Verify dependencies between parameters.
12. Distinguish structural constants from configurable numerical parameters.

Every independently configurable parameter must have an identifiable register entry.

Do not create artificial parameters for variables that are not independently configurable.

Preserve provisional, unresolved, owner-required and legal-required classifications.

Do not promote any parameter to Approved without actual authority.

---

# 7. CORRECTION 5 — CROSS-SYSTEM INTEGRATION MAPPING

**Priority: Critical**

Inspect:

`docs/stage-2/20_fair_play_and_player_protection.md`

And:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

The previous independent audit found inconsistencies in the cross-system integration mapping.

In particular, the acceptance document's §5 mapping appears to associate several B-system identifiers with incorrect INT integration contract identifiers.

The earlier audit identified these expected associations for verification against the canonical architecture:

| System | Integration reference |
|---|---|
| B-03 Accounts | INT-001 |
| B-04 Economy | INT-003 |
| B-05 Cities and research | INT-004 |
| B-06 Politics | INT-005 |
| B-07 Markets | INT-006 |
| B-08 Diplomacy | INT-007 |
| B-09 Alliances | INT-008 |
| B-10 Warfare | INT-009 |
| B-11 World events and objectives | INT-010 |
| B-11 Rankings and progression | INT-011 |
| B-02 Turn engine | INT-013 |
| B-02 Audit spine | INT-014 |

These are audit findings to verify, not permission to override canonical architecture.

Required work:

1. Inspect the authoritative system registry.
2. Inspect the canonical B-system identifiers and names.
3. Inspect INT-001 through INT-020.
4. Inspect every corresponding rulebook integration reference.
5. Inspect the acceptance document's cross-system mapping.
6. Verify every system-to-contract association against canonical project documentation.
7. Correct incorrect associations.
8. Identify missing systems or integration contracts.
9. Identify duplicate or ambiguous mappings.
10. Preserve existing identifiers.

Do not renumber existing systems or integration contracts to make the table appear consistent.

The acceptance document must accurately identify the systems affected by each integration contract.

---

# 8. CORRECTION 6 — COMPLETE INTEGRATION CONTRACT TRACEABILITY

**Priority: High**

Prompt 12B §13 requires each actual integration dependency to identify seven fields:

1. System boundary.
2. Data or authority dependency.
3. Invariant.
4. Security requirement.
5. Ownership.
6. Prompt 12C integration work.
7. Implementation dependency.

Inspect INT-001 through INT-020.

For every actual dependency, verify these seven fields.

Where fields are missing or insufficiently defined:

- Complete them.
- Use existing architecture and terminology.
- Preserve the correct ownership boundaries.
- Identify genuine dependencies only.
- Avoid inventing unnecessary integrations.

Ensure the acceptance matrix and rulebook reference the same integration definitions.

Also check cross-references involving:

- Authentication.
- Accounts.
- Profiles.
- Economy.
- Markets.
- Diplomacy.
- Alliances.
- Warfare.
- World events.
- Objectives.
- Rankings.
- Notifications.
- Moderation.
- Administration.
- Evidence storage.
- Audit systems.

Do not create detailed player journeys or end-to-end operational workflows. Those remain reserved for Prompt 12C.

---

# 9. CORRECTION 7 — PERMANENT PROMPT 12B ARCHIVAL

**Priority: High**

The owner explicitly requires prompts to be preserved as separate permanent project files.

The complete original Prompt 12B instruction was supplied to the coding agent.

The previous audit did not find a separate permanent file containing that complete instruction.

Required work:

1. Inspect the existing prompt archive and naming convention.
2. Identify the correct established prompt directory.
3. Identify the correct filename convention.
4. Save the complete original Prompt 12B instruction as a permanent project prompt file.
5. Preserve the entire instruction, including its original sections and restrictions.
6. Do not create an abbreviated summary as a substitute.
7. Do not silently rewrite the original instruction.
8. Update the established prompt index or roadmap with the exact file path.
9. Update relevant progress and handoff references.

Before creating the file, check whether an identical permanent copy already exists.

Avoid duplicate prompt files.

If the complete original instruction is not accessible, report this honestly rather than reconstructing missing text and presenting it as the original.

---

# 10. CORRECTION 8 — AUTONOMOUS DECISION POLICY READING ATTESTATION

**Priority: High**

Canonical policy:

`AUTONOMOUS_DECISION_POLICY.md`

The previous audit established that the policy exists and that the specification work is generally consistent with D-014.

However, an explicit attestation confirming complete reading was not found.

Required work:

1. Read the entire canonical policy now.
2. Confirm that the full document was read.
3. Record the actual reading date.
4. Record the exact canonical file path.
5. Record the attestation in the Prompt 12B progress entry or appropriate handoff document.
6. Distinguish a reading performed now from any historical reading before Prompt 12B began.

If the agent cannot establish that it read the policy before Prompt 12B, it must not claim that it did.

Do not backdate the attestation.

Do not alter, weaken or replace the policy.

---

# 11. ACCEPTANCE GATE REASSESSMENT

Inspect:

`docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

The existing Prompt 12B acceptance framework contains 26 gates:

- 23 PASS.
- 3 PARTIAL.
- 0 FAIL.
- 0 BLOCKED.

The previous independent audit recommended reviewing three additional areas:

1. Formula correctness and accounting consistency.
2. Cross-system integration mapping.
3. Formula and parameter-register completeness.

Required work:

1. Reassess all 26 gates against actual documentary evidence.
2. Correct acceptance criteria where necessary.
3. Verify that each gate has adequate evidence.
4. Identify unresolved dependencies.
5. Update statuses only where evidence justifies a change.
6. Preserve all three existing PARTIAL gates unless new independently verifiable evidence justifies changing them.
7. Do not artificially convert PARTIAL to PASS.
8. Do not manufacture acceptance evidence.

The existing 26-gate structure must be preserved.

The audit's proposed reassessment of 20 PASS / 6 PARTIAL is a recommendation, not a predetermined outcome.

Determine the actual result independently.

Also preserve Prompt 12A's seven PARTIAL gates.

---

# 12. REQUIREMENT AND DECISION TRACEABILITY

Preserve:

- REQ-764 through REQ-869.
- D-178 through D-187.
- DD-226 through DD-235.
- UD-017.
- UD-052 through UD-060.

Do not renumber identifiers.

Do not duplicate requirements or decisions.

Do not silently approve provisional requirements.

If formula or integration corrections affect existing requirements:

1. Update the appropriate references.
2. Preserve requirement identity.
3. Record the revision rationale.
4. Update traceability matrices.
5. Update relevant acceptance references.

Check all affected references across the project.

---

# 13. PROJECT-WIDE DOCUMENTATION SYNCHRONIZATION

Inspect and update relevant documents where necessary:

- `AI_CONTEXT.md`
- `AI_HANDOFF.md`
- `PROJECT_PROGRESS.md`
- `ROADMAP.md`
- Stage 2 handoff.
- Stage 2 roadmap.
- Stage 2 progress log.
- Prompt index.
- Global requirements ledger.
- Requirements traceability matrix.
- Global decision register.
- Mirrored decision register.
- Unresolved-decision register.
- Formula register.
- Numerical parameter register.
- Security and risk registers.
- Acceptance-gate records.
- Change manifest.
- Relevant QA documentation.

Preserve historical entries.

Do not modify unrelated documents unnecessarily.

Record files inspected but not modified where relevant.

Update all affected status references consistently.

---

# 14. VALIDATION REQUIREMENTS

Run appropriate validators after the corrections.

At minimum verify:

### Formula validation
- All formulas have complete definitions.
- Worked examples produce mathematically correct results.
- Sign conventions are consistent.
- Parameter references resolve.
- Dimensional consistency is maintained.
- Repeat-violation calculations are internally consistent.

### Integration validation
- All B-system references resolve.
- All INT identifiers resolve.
- System-to-contract associations match canonical architecture.
- Required seven integration fields are present.
- Acceptance and rulebook mappings agree.

### Prompt archival validation
- Complete Prompt 12B instruction exists.
- Correct prompt index entry exists.
- No duplicate prompt file exists.

### Governance validation
- Policy reading attestation exists.
- Reading date is truthful.
- Policy remains unchanged.

### Cross-document validation
- Requirement IDs remain consistent.
- Decision IDs remain consistent.
- Unresolved decisions remain open.
- Acceptance totals reconcile.
- Internal links resolve.
- Implementation claims remain accurate.

### Regression validation

Run relevant existing project validators without weakening them.

Preserve the known legacy 11A REQ-703 versus REQ-764 expectation issue. Do not silently alter legacy validator expectations to manufacture passing results.

For each validator record:

- Exact command.
- Exit code.
- Checks executed.
- Passed checks.
- Failed checks.
- Fixture results.
- Known limitations.

Do not claim a validator ran if it was not actually executed.

---

# 15. SECURITY AND IMPLEMENTATION RESTRICTIONS

This is still a documentation and specification corrective task.

Do not:

- Implement Supabase migrations.
- Modify database grants.
- Modify RLS policies.
- Create corrective migration 0005.
- Create audit-log triggers.
- Modify authentication or authorization runtime behavior.
- Implement production audit-digest jobs.
- Modify economic transaction logic.
- Change gameplay implementation.
- Create production security controls.

The following obligations must remain visible:

- `feasibility.profiles` sensitive-field UPDATE protection.
- Treasury protection.
- Corrective database migration.
- SQL permission tests.
- Protective audit-log trigger.
- Tamper-evident audit implementation.
- Audit-digest operation and verification.

Documentation is not implementation.

Preserve the existing implementation-readiness distinctions.

---

# 16. STRICT PROMPT 12C BOUNDARY

Prompt 12C remains a separate phase requiring separate owner authorization.

Do not:

- Begin Prompt 12C.
- Create player journey catalogues.
- Create complete workflow libraries.
- Create detailed operational sequence diagrams.
- Create Prompt 12C acceptance deliverables.
- Begin implementation planning beyond the existing documented dependencies.

Complete this corrective pass and stop.

---

# 17. REQUIRED FINAL DELIVERY REPORT

Provide a detailed final report containing:

## A. Corrective work completed
List every correction and exact file path.

## B. Formula corrections
For each affected formula provide:

- Original problem.
- Corrected definition.
- Mathematical examples.
- Parameter references.
- Dependencies.
- Verification results.

## C. Integration corrections
Report:

- Corrected B-system mapping.
- INT-001 through INT-020 review.
- Seven-field completeness.
- Remaining integration dependencies.

## D. Permanent prompt archival
Provide the exact saved Prompt 12B instruction path and prompt-index reference.

## E. Autonomous policy attestation
Provide:

- Canonical policy path.
- Confirmation of complete reading.
- Actual reading date.
- Honest distinction between historical and current attestation.

## F. Requirements and decisions
Confirm preservation of:

- REQ-764–REQ-869.
- D-178–D-187.
- DD-226–DD-235.
- All unresolved decisions.

## G. Acceptance gates
Report all 26 gates with actual statuses and evidence.

## H. Validators
Provide actual commands, exit codes, results and limitations.

## I. Documentation synchronization
List every modified file and reason.

## J. Outstanding matters
Identify remaining owner decisions, legal dependencies, implementation obligations and technical uncertainties.

## K. Final status
Assign an evidence-based result:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

Do not claim full completion if material defects remain.

---

# 18. FINAL INSTRUCTION

Work autonomously under D-014.

Use the existing live Nation Supremacy project directory.

Treat all owner-created ZIP archives exclusively as independent audit snapshots, never as working projects.

Correct the identified defects with minimal, evidence-based changes.

Preserve completed Prompt 12B work, historical decisions, requirements, unresolved matters and owner authority.

Do not manufacture evidence, approvals, validator results or implementation claims.

Do not begin Prompt 12C.

Do not perform Git staging, committing or pushing.

**Complete Prompt 12B-C1 and stop for the owner's next independent review and authorization.**