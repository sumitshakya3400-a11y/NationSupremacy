# PROMPT 12C — FAIR-PLAY OPERATIONAL WORKFLOWS, CROSS-SYSTEM INTEGRATION, EDGE-CASE SPECIFICATIONS AND ACCEPTANCE TESTS

> **Archival provenance (recorded by Prompt 12C-FINAL-C1, 2026-11-10).** This is the owner's original Prompt 12C instruction. Its source is the instruction **supplied in the working session** and retained in that session's transcript; it is **not** a copy recovered from a file, an uploaded audit snapshot or an exported artifact, because no such copy exists in the repository or in `.cloud-attachments/` (the only attachment there is an imported conversation record dated 2026-10-31, which predates Prompt 12C and does not contain it). The text below was transcribed from the session-supplied instruction and stored byte-wise as written; the recorded SHA-256 in [`INDEX.md`](INDEX.md) identifies **these stored bytes**, and byte-for-byte comparison against an independent external original was **not** possible. Where a future copy of the owner's original becomes available, it must be diffed against this file and any difference recorded here rather than silently corrected. This file is a historical record: it is not live design authority, and a later decision or corrective pass may supersede its execution status without editing the archived text. It must never be confused with the later **Prompt 12C-FINAL-C1** corrective instruction, which is a different, bounded repository-integrity task.

## 1. ROLE AND RESPONSIBILITY

Act as the senior game-systems architect, requirements engineer, security architect, workflow designer, integration architect, documentation engineer and independent quality-assurance specialist for **Nation Supremacy**.

Your responsibility is to translate the authoritative Prompt 12A and Prompt 12B research, requirements and fair-play specifications into a coherent operational specification that integrates correctly with the entire previously designed game.

You are not working on an isolated fair-play document.

You are extending an existing interconnected strategy-game design whose previous systems, decisions, requirements, formulas, identifiers, workflows and acceptance specifications must remain consistent.

The quality of this work will be judged by:

1. Completeness of operational workflow specifications.
2. Accuracy of fair-play requirement implementation at the specification level.
3. Cross-system consistency with all previously completed prompts.
4. Correct integration contracts and system responsibilities.
5. Completeness of edge-case coverage.
6. Traceability from authoritative requirements to workflows and acceptance tests.
7. Preservation of governance, security restrictions and owner-reserved decisions.
8. Absence of contradictory, duplicated or invented rules.

Do not optimize for the number of documents or tests produced.

Optimize for a coherent, implementable and internally consistent game specification.

---

## 2. MANDATORY GOVERNANCE — READ BEFORE WORK

Before substantial work, locate and read the entire file:

`AUTONOMOUS_DECISION_POLICY.md`

Read it completely, including all decision classifications, restrictions, decision-making boundaries and escalation requirements.

Pay particular attention to D-014.

This policy is authoritative.

You must follow it throughout this task.

### Mandatory decision-making restrictions

- Never make an owner-reserved decision without explicit owner authorization.
- Never convert an open or provisional decision into an approved decision.
- Never resolve a legal-dependent question through unsupported assumptions.
- Never silently change approved design decisions.
- Never invent numerical parameters, formulas, thresholds, retention periods, sanctions or security guarantees.
- Never treat an external recommendation as an approved project requirement.
- Never use autonomous decision-making as permission to expand the authorized project scope.
- Preserve decision provenance and the distinction between existing decisions, recommendations and unresolved questions.

Where a decision is necessary but not authorized, document the dependency, its impact and the required owner decision.

Continue all work that can legitimately proceed without resolving that decision.

Do not block unrelated workflows unnecessarily.

---

## 3. PROJECT BASELINE — INSPECT THE ENTIRE EXISTING PROJECT

Do not start writing immediately.

First inspect the existing live project and establish the authoritative documentation baseline.

The latest independent audit snapshot, Project X (78), is reference evidence only.

The live project directory remains the working project.

Never use an uploaded ZIP as the working directory.

Never create duplicate project directories or overwrite unrelated work.

### 3.1 Review the previously completed prompts

Review the completed specifications and their authoritative outputs for:

- Prompt 07 — Market.
- Prompt 08 — Diplomacy.
- Prompt 09 — Alliances.
- Prompt 10 — Warfare and World Events, including their separate specifications.
- Prompt 11 — Objectives, Rankings and Progression.
- Prompt 11C — Player journeys, workflows, edge cases, integration contracts and acceptance specifications.
- Prompt 12A — Research, evidence, requirements, integrations and risk foundations.
- Prompt 12B — Fair-play and player-protection authoritative specifications.

Inspect the relevant files rather than relying solely on summaries, AI_CONTEXT entries or handoff descriptions.

Use existing canonical indexes, prompt archives, the Stage 2 roadmap and authoritative specification documents to establish exact file locations and document authority.

### 3.2 Review the existing 12B baseline

The authoritative Prompt 12B files are:

1. `docs/stage-2/20_fair_play_and_player_protection.md`
2. `docs/stage-2/20_fair_play_and_player_protection_requirements.md`
3. `docs/stage-2/20_fair_play_and_player_protection_formula_register.md`
4. `docs/stage-2/20_fair_play_and_player_protection_acceptance.md`

Use these as authoritative sources for the 12C work.

Preserve the established baseline:

- 344 normative rules.
- 13 categories.
- 106 requirements: REQ-764–REQ-869.
- 16 formulas.
- 12 numerical parameters.
- 14 canonical FP-P identifiers.
- 26 acceptance gates.
- Decisions D-178–D-187.
- DD-226–DD-235.

The requirements currently comprise:

- 86 Provisional.
- 20 Open.
- 0 Approved.
- 0 Deferred.

Do not silently change these statuses.

Use the existing canonical formula and parameter definitions. Do not invent replacements.

### 3.3 Review the 12A research baseline

Preserve and use the following research foundation:

- 106 candidate requirements.
- 30 integration dependencies.
- 32 threats.
- 15 failure postures.
- 15 open research questions.
- 32 recommendations.
- 11 information categories.
- 40 benchmark mechanisms.
- 18 comparator profiles.

Preserve decisions D-163–D-177 and DD-211–DD-225.

Preserve unresolved questions UD-052–UD-060.

The seven PARTIAL acceptance gates from 12A must not be artificially closed.

Research recommendations must not silently become approved game rules.

### 3.4 Review the Prompt 11C baseline

Prompt 11C already established documentation specifications for:

- 25 player journeys.
- 50 workflows.
- 84 edge cases.
- 17 integration contracts.
- 272 acceptance-test specifications.
- 30 threats.
- 20 acceptance gates.

These are existing documentation specifications, not evidence of runtime implementation.

The new 12C documents must integrate with this material rather than creating competing or contradictory versions.

Do not silently change existing counts, identifiers, specifications or acceptance statuses.

Reuse and reference existing specifications where appropriate.

Create additions only when there is a demonstrable fair-play requirement that is not already adequately addressed.

---

## 4. OWNER'S EXPLICIT SCOPE AND PROJECT RESTRICTIONS

This task authorizes documentation-level design specification work for Prompt 12C only.

The authorized scope is:

1. Translate the B-12 rules into operational workflows.
2. Integrate fair-play requirements with previously designed game systems.
3. Define fair-play edge cases and failure scenarios.
4. Define integration contracts and system responsibilities.
5. Produce traceable acceptance-test specifications.
6. Preserve governance and security restrictions.
7. Maintain consistency across all previously completed prompts.

### Explicitly prohibited work

Do not:

- Implement gameplay.
- Write production gameplay code.
- Implement database migrations.
- Change production application architecture.
- Implement account, moderation, sanction or enforcement functionality.
- Implement security controls or claim they are operational.
- Perform R8 validator correction.
- Fix the five R7 residual bypasses.
- Modify `docs/qa_backups/12B_validate_b12.py`.
- Create another R8 correction prompt.
- Expand the R7 validator-hardening effort.
- Begin Prompt 13, 14 or 15.
- Treat Prompt 12C as authorization to close 12B-C1.
- Treat Prompt 12C as authorization to close existing PARTIAL gates.

Do not use this task to pursue unrelated technical cleanup.

---

## 5. CRITICAL CURRENT STATUS — PRESERVE EXACTLY

The owner has explicitly deferred R8.

Preserve:

| Item | Required status |
|---|---|
| R7 implementation | RETAINED |
| R7 registered tests | PASS |
| R7 independent acceptance | NOT ACCEPTED |
| Five R7 residual weaknesses | KNOWN AND UNFIXED |
| R8 | DEFERRED BY OWNER |
| 12B-C1 | NOT CLOSED |
| Prompt 12C | Authorized within this prompt's scope |

The five known R7 residual weaknesses concern:

1. Incomplete current-state parameter assertion recognition.
2. AI_CONTEXT block-boundary parsing.
3. Canonical register table parsing.
4. Unicode malformed identifier suffix detection.
5. Multiline malformed identifier suffix detection.

Do not fix, conceal or reclassify these findings.

### Preserve the three 12B PARTIAL gates

The following must remain PARTIAL:

1. P12B-14 — Audit-spine and tamper-evidence verification.
2. P12B-16 — Supabase privilege and audit-protection defects.
3. P12B-23 — Project-wide synchronization and legacy validator debt.

Prompt 12C must not automatically close, downgrade, upgrade or reinterpret these gates.

Any new 12C acceptance gates must be separately identified and must not replace existing 12B gates.

---

## 6. WORKSTREAM A — AUTHORITATIVE RULE-TO-WORKFLOW TRANSLATION

Translate the normative B-12 rules into operational workflows.

The purpose is to describe exactly how fair-play requirements interact with the game's operational systems and player journeys.

Do not merely paraphrase normative rules.

For each relevant rule or requirement, establish:

1. What event or condition activates the requirement?
2. Which player action or game event is involved?
3. Which system is responsible?
4. Which other systems participate?
5. What information is required?
6. Which information may be accessed?
7. What validations or decisions occur?
8. What state transitions are permitted?
9. What happens when a check succeeds?
10. What happens when a check fails?
11. What does the player experience?
12. What administrative or moderation action is permitted?
13. What audit evidence is required?
14. What happens when a dependency is unavailable?
15. What happens when the result is ambiguous?
16. What happens when the workflow must be appealed, reviewed or corrected?
17. Which acceptance tests verify the workflow?

### Workflow specification requirements

Each workflow must have:

- A unique canonical identifier.
- A descriptive name.
- A clear purpose.
- Trigger and preconditions.
- Participating actors.
- Participating systems.
- Required inputs.
- Validation and decision sequence.
- Normal execution path.
- Alternative execution paths.
- Failure handling.
- Resulting state.
- Player communication requirements.
- Audit and traceability requirements.
- Security and privacy considerations.
- Related requirements.
- Related normative rules.
- Related integration contracts.
- Related edge cases.
- Related acceptance tests.

Use established project terminology and workflow conventions.

Do not invent identifiers where existing identifier conventions must first be inspected.

Do not create duplicate workflows merely to increase the document count.

---

## 7. WORKSTREAM B — CROSS-SYSTEM CONSISTENCY AND INTEGRATION

This is one of the highest-priority requirements of Prompt 12C.

Nation Supremacy must operate as one coherent strategy game.

Fair-play rules must not contradict, unexpectedly override or create parallel versions of existing gameplay rules.

Review each relevant existing system and identify all genuine fair-play integration points.

At minimum, assess the following:

### 7.1 Market

Examine:

- Market manipulation.
- Artificial pricing behaviour.
- Repeated or coordinated transaction patterns.
- Abuse of trade mechanisms.
- Transaction verification.
- Economic fairness.
- Relevant player-protection interventions.

Preserve existing market mechanics, terminology, resource definitions and economic ownership rules.

### 7.2 Diplomacy

Examine:

- Harassment and coercion.
- Manipulative diplomatic conduct.
- Abusive communications.
- Diplomatic restrictions.
- Player protection.
- Reporting and review interactions.

Do not change existing diplomatic mechanics without authorization.

### 7.3 Alliances

Examine:

- Coordinated abuse.
- Alliance-level exploitation.
- Shared-account or collusion concerns.
- Leadership abuse.
- Alliance sanctions and consequences.
- Fairness between members and non-members.

Preserve existing alliance permissions and leadership responsibilities.

### 7.4 Warfare

Examine:

- Exploitation of combat systems.
- Artificial coordination.
- Unfair targeting behaviour.
- Abuse of warfare restrictions.
- Fair-play interventions.
- Sanctions and recovery interactions.

Do not change combat formulas or military balance.

### 7.5 World Events

Examine:

- Event manipulation.
- Unequal or unintended event effects.
- Abuse of event triggers.
- Event-related player protection.
- Recovery and failure conditions.

Preserve existing event mechanics and event-authority boundaries.

### 7.6 Objectives

Examine:

- Artificial objective completion.
- Exploitation of progress conditions.
- Coordinated reward abuse.
- Unfair progress advantages.
- Objective integrity.

Preserve existing objective requirements and reward ownership.

### 7.7 Rankings

Examine:

- Ranking manipulation.
- Artificial score inflation.
- Unfair progression advantages.
- Invalid result handling.
- Corrections to ranking outcomes.
- Historical ranking integrity.

Do not silently rewrite ranking formulas or scoring rules.

### 7.8 Progression

Examine:

- Abusive progression.
- Unfair advancement.
- Reward manipulation.
- Exploitation of progression dependencies.
- Player-protection consequences.

Preserve existing progression definitions and dependencies.

### 7.9 Shared infrastructure and supporting systems

Also assess relevant interactions with:

- Accounts and authentication.
- Nation registration.
- Shared turn processing.
- Administration.
- Moderation.
- Reporting.
- Notifications.
- Audit and logging.
- Data retention and privacy.
- Security and permissions.
- Recovery and appeals.

Only specify integrations supported by the established project requirements.

Do not assume an unbuilt system already exists.

### Mandatory integration matrix

Create a cross-system integration matrix identifying:

| Field | Required contents |
|---|---|
| Integration ID | Canonical identifier |
| Source system | Originating system |
| Destination system | Receiving system |
| Trigger | Event or condition |
| Required data | Minimum necessary information |
| Data authority | System responsible for authoritative state |
| Processing responsibility | Which system performs each action |
| Permissions | Authorized actors and access boundaries |
| State effects | Permitted resulting changes |
| Failure behaviour | Defined failure posture |
| Audit requirements | Required evidence |
| Related B-12 requirements | Canonical requirement identifiers |
| Related existing specifications | Previous prompt references |
| Related workflows | Workflow identifiers |
| Related tests | Acceptance-test identifiers |
| Unresolved decisions | Owner or legal dependencies |

### Cross-system consistency rules

For every integration, explicitly verify:

1. No contradictory rule exists in another system.
2. No system receives authority it does not possess.
3. No duplicate source of truth is created.
4. Existing resource and currency definitions are preserved.
5. Existing turn timing and processing order are preserved unless an approved decision authorizes otherwise.
6. Existing permissions and ownership rules are preserved.
7. Fair-play restrictions do not unintentionally break normal gameplay.
8. Administrative privileges are not expanded implicitly.
9. Privacy boundaries are maintained.
10. Failure handling remains consistent across systems.
11. Appeals and corrections do not bypass existing authority boundaries.
12. Historical records and rankings are not silently rewritten.

Where two specifications conflict, do not independently choose a winner.

Identify the conflicting statements, their authority, their impact and the owner decision required.

---

## 8. WORKSTREAM C — EDGE CASES AND FAILURE SCENARIOS

Develop the fair-play-specific edge-case specifications.

Do not duplicate the 84 previously established Prompt 11C edge cases unnecessarily.

First search the existing edge-case register and determine which cases already cover the relevant situation.

For each additional or materially extended case, provide:

- Unique identifier.
- Scenario description.
- Triggering condition.
- Affected systems.
- Related workflow.
- Related requirement.
- Expected system behaviour.
- Expected player experience.
- Security and privacy implications.
- Recovery or escalation behaviour.
- Audit requirements.
- Related acceptance tests.
- Whether the scenario requires owner or legal resolution.

### Required scenario categories

Assess all relevant scenarios, including:

**Player behaviour**
- False reports.
- Malicious reports.
- Repeated reports.
- Coordinated reporting.
- Harassment.
- Impersonation.
- Abusive communications.
- Retaliation.

**Economic and gameplay manipulation**
- Coordinated market manipulation.
- Artificial resource generation.
- Exploit chains.
- Abusive trade patterns.
- Unfair reward claims.
- Ranking manipulation.
- Objective exploitation.

**Account and identity**
- Account compromise.
- Shared-account indicators.
- Account recovery.
- Identity ambiguity.
- Unauthorized access.
- Conflicting account states.

**Moderation and enforcement**
- Incorrect sanctions.
- Inconsistent enforcement.
- Delayed review.
- Evidence insufficiency.
- Appeals.
- Repeated violations.
- Administrative abuse.
- Conflicting moderation outcomes.

**Technical and operational failures**
- Partial workflow execution.
- Duplicate event delivery.
- Retry behaviour.
- Timeout.
- Service unavailability.
- Inconsistent database state.
- Failure during a shared turn.
- Concurrent actions.
- Stale data.
- Audit-write failure.
- Recovery after interruption.

**Privacy and information handling**
- Unauthorized disclosure.
- Excessive data collection.
- Unauthorized administrative access.
- Retention conflicts.
- Deletion requests.
- Legal holds.
- Evidence access restrictions.

Do not turn hypothetical threats into confirmed project incidents.

Use existing threat identifiers where applicable.

---

## 9. WORKSTREAM D — INTEGRATION CONTRACTS

Specify the operational contracts between fair-play functionality and the existing game systems.

The contracts must define:

1. Contract identifier.
2. Contract purpose.
3. Producing system.
4. Consuming system.
5. Trigger and execution conditions.
6. Required input schema or data description.
7. Output or expected response.
8. Data ownership.
9. Authorization requirements.
10. Validation responsibilities.
11. Idempotency and duplicate handling.
12. Transaction boundaries where applicable.
13. Retry behaviour.
14. Timeout behaviour.
15. Failure handling.
16. Audit requirements.
17. Privacy restrictions.
18. Related workflows.
19. Related edge cases.
20. Acceptance-test references.

Do not invent APIs, production endpoints, schemas, database columns or implementation details that have not been authorized or established.

Where technical details are undecided, specify the required contract behaviour and clearly mark the unresolved implementation decision.

### Integration dependency preservation

Cross-reference the 30 Prompt 12A integration dependencies.

Reuse existing dependency identifiers.

If new dependencies are genuinely necessary, allocate identifiers only after verifying the current canonical register and applicable identifier policy.

---

## 10. WORKSTREAM E — ACCEPTANCE-TEST SPECIFICATIONS

Create comprehensive, traceable acceptance-test specifications for the fair-play operational workflows and cross-system integrations.

These are documentation-level acceptance specifications.

They are not evidence of completed production implementation or runtime testing.

Every acceptance test must have:

- Unique acceptance-test identifier.
- Test objective.
- Related requirement IDs.
- Related normative rule references.
- Related workflow.
- Related integration contract.
- Related edge cases.
- Preconditions.
- Required test data.
- Action sequence.
- Expected results.
- Expected state transitions.
- Expected player-visible outcome.
- Expected permission outcome.
- Expected audit evidence.
- Failure criteria.
- Applicable test classification.
- Execution requirements.
- Current verification status.

### Mandatory coverage

Cover:

1. Normal successful workflows.
2. Invalid or unauthorized actions.
3. Boundary conditions.
4. Duplicate and repeated actions.
5. Concurrent actions.
6. Failure and recovery.
7. Cross-system consistency.
8. Privacy restrictions.
9. Administrative permissions.
10. Moderation and appeal handling.
11. Audit integrity requirements.
12. Shared-turn interactions.
13. Idempotency and retry behaviour.
14. Unresolved or legally dependent scenarios.

### Test classifications

Clearly distinguish:

- Positive acceptance specifications.
- Negative acceptance specifications.
- Boundary acceptance specifications.
- Security acceptance specifications.
- Integration acceptance specifications.
- Recovery acceptance specifications.
- Privacy acceptance specifications.
- Owner-decision-dependent acceptance specifications.

Do not label a specification as a passing test unless it was actually executed against an available implementation.

Use explicit statuses such as:

- SPECIFIED.
- IMPLEMENTED.
- EXECUTED.
- PASS.
- FAIL.
- BLOCKED.
- NOT APPLICABLE.

These statuses must retain their distinct meanings.

---

## 11. WORKSTREAM F — COMPLETE TRACEABILITY

Produce a traceability matrix linking:

12A research and recommendations
→ 12A requirements and risks
→ 12B normative rules
→ 12B requirements
→ 12C workflows
→ 12C integration contracts
→ 12C edge cases
→ 12C acceptance-test specifications.

The matrix must also identify links to previously completed systems and Prompt 11C specifications.

Requirements must not disappear between documents.

Every relevant 12B requirement must be:

1. Mapped to an operational workflow or explicitly classified as not applicable to a 12C workflow, with justification.
2. Mapped to relevant integration contracts where applicable.
3. Covered by appropriate acceptance specifications.
4. Linked to any unresolved dependency or owner decision.
5. Traceable back to its authoritative rule.

Identify orphan requirements, workflows, contracts, edge cases and tests.

Identify circular dependencies and missing integration links.

Do not force artificial links merely to produce complete-looking coverage.

Every excluded or not-applicable item requires a reason.

---

## 12. WORKSTREAM G — SECURITY, PRIVACY AND ADMINISTRATIVE BOUNDARIES

Preserve all security limitations and outstanding obligations.

The following issues remain unresolved and must not be reported as implemented or verified:

- Authenticated table-wide UPDATE access on `feasibility.profiles`, including `treasury`.
- Missing corrective migration 0005.
- Missing SQL permission tests.
- Missing protective audit-log trigger.
- No verified production tamper-evident audit implementation.
- No verified operating audit-digest job.

These are not minor documentation issues.

They must be reflected appropriately in relevant workflows, contracts, failure scenarios and acceptance-test specifications.

### Mandatory restrictions

Do not:

- Authorize unrestricted treasury changes.
- Expand authenticated permissions.
- Assume row-level security provides column-level protection.
- Claim tamper-evident logging exists.
- Claim production audit protection is verified.
- Claim audit digest operations are active.
- Invent admin privileges.
- Allow moderators to make financial or gameplay changes without an established authority.
- Expose confidential evidence unnecessarily.
- Assume all moderation information is publicly visible.
- Invent retention periods or legal authority.

Where the workflow depends on outstanding security controls, explicitly mark the dependency and required verification.

Preserve the three existing 12B PARTIAL gates.

New 12C acceptance specifications must not artificially close any existing gate.

---

## 13. WORKSTREAM H — DECISIONS AND UNRESOLVED QUESTIONS

Review the existing decision registers before introducing any new decisions.

Preserve:

- D-163–D-177.
- DD-211–DD-225.
- D-178–D-187.
- DD-226–DD-235.
- UD-052–UD-060.

Use the existing decision-management conventions.

New decisions may only be assigned when genuinely necessary and permitted by the autonomous decision policy.

For each unresolved issue, specify:

- Issue identifier.
- Description.
- Relevant systems.
- Related requirements.
- Why resolution is needed.
- Available options, where supported.
- Consequences of each option.
- Dependencies.
- Owner decision required.
- Legal or research dependency, if applicable.
- Whether work can continue without resolution.

Do not manufacture approvals.

Do not silently convert recommendations into decisions.

Do not resolve owner-reserved questions.

---

## 14. DOCUMENTATION STRUCTURE AND CHANGE CONTROL

Before creating files, inspect the current project structure and Prompt 12 roadmap.

Use the existing naming, numbering, cross-reference and documentation conventions.

Do not invent a competing document structure.

Determine the appropriate canonical locations for:

1. Fair-play operational workflows.
2. Cross-system integration specifications.
3. Fair-play edge cases.
4. Integration contracts.
5. Acceptance-test specifications.
6. Traceability and acceptance records.

If the project conventions support combining some of these materials, avoid unnecessary fragmentation.

Update relevant indexes and handoff records consistently.

Do not rewrite the existing 12A or 12B canonical documents merely to make 12C easier.

Do not overwrite completed specifications.

Preserve historical records.

If an existing document contains a material contradiction, document it and follow the authority and decision-escalation rules.

### Status synchronization

Where project-maintenance updates are needed, synchronize:

- Stage 2 roadmap.
- Stage 2 progress log.
- AI_CONTEXT.
- AI_HANDOFF.
- PROJECT_PROGRESS.
- ROADMAP.
- Other canonical project indexes as appropriate.

Keep current status clauses consistent.

Do not mechanically edit unrelated historical statements.

Do not change R7, R8 or 12B-C1 status while synchronizing Prompt 12C.

---

## 15. QUALITY ASSURANCE AND VALIDATION

Before completion, independently review the resulting documentation.

### Required validation areas

**Structural integrity**
- Required files exist.
- Correct headings and document structure.
- No duplicate canonical identifiers.
- No broken local links.
- Correct references.
- No malformed tables or registers.

**Requirement integrity**
- No missing 12B requirements.
- No invented or altered normative rules.
- No unauthorized requirement-status changes.
- No duplicated requirements presented as new requirements.

**Cross-system integrity**
- Market consistency.
- Diplomacy consistency.
- Alliance consistency.
- Warfare consistency.
- World Event consistency.
- Objectives consistency.
- Rankings consistency.
- Progression consistency.
- Shared infrastructure consistency.

**Workflow integrity**
- Clear triggers.
- Complete normal and alternative paths.
- Explicit failure behaviour.
- Defined responsibilities.
- Valid state transitions.
- Adequate player communication and audit requirements.

**Integration integrity**
- Clear ownership.
- Correct permissions.
- Defined inputs and outputs.
- Appropriate failure behaviour.
- No invented implementation guarantees.

**Acceptance integrity**
- Requirements covered.
- Edge cases covered.
- Negative cases included.
- Security and privacy cases included.
- Tests have observable expected results.
- Specification and execution statuses distinguished.

**Governance integrity**
- Autonomous Decision Policy followed.
- Owner decisions preserved.
- Outstanding security obligations preserved.
- Three PARTIAL gates unchanged.
- R8 remains deferred.
- 12B-C1 remains not closed.
- No unauthorized Prompt 13–15 work.

### Existing validators

Run relevant existing documentation and project validators where appropriate.

Do not modify validators to achieve a PASS.

Do not expand R7 validator-hardening work.

If an existing validator fails because of a known baseline issue, record the exact failure and distinguish it from new Prompt 12C defects.

Do not report tests as passing when they were not executed.

A documentation validator PASS does not establish runtime implementation.

---

## 16. REQUIRED FINAL AUDIT

Before declaring Prompt 12C documentation complete, provide a structured independent completion report.

The report must contain:

### A. Files created and modified

List each file and its purpose.

Distinguish newly created documents from updates to indexes or handoffs.

### B. Workflow inventory

Report:

- Existing workflows reused.
- New workflows specified.
- Workflow coverage.
- Unresolved workflow dependencies.

### C. Integration inventory

Report:

- Existing contracts reused.
- New contracts specified.
- Integration coverage.
- Missing or unresolved integrations.

### D. Edge-case inventory

Report:

- Existing cases reused.
- New cases added.
- Duplicates avoided.
- Unresolved scenarios.

### E. Acceptance-test inventory

Report:

- Positive specifications.
- Negative specifications.
- Boundary specifications.
- Security specifications.
- Integration specifications.
- Recovery specifications.
- Privacy specifications.
- Owner-decision-dependent specifications.

Clearly distinguish specified, implemented, executed and passed statuses.

### F. Traceability assessment

Report:

- Total relevant 12B requirements.
- Requirements mapped.
- Requirements not applicable, with justifications.
- Orphan requirements.
- Orphan workflows.
- Orphan contracts.
- Orphan edge cases.
- Orphan tests.
- Unresolved traceability gaps.

### G. Cross-system consistency assessment

Provide a system-by-system result for:

- Market.
- Diplomacy.
- Alliances.
- Warfare.
- World Events.
- Objectives.
- Rankings.
- Progression.
- Accounts and shared infrastructure.
- Administration and moderation.

Identify contradictions and their resolution or escalation status.

### H. Governance and security assessment

Explicitly confirm:

- AUTONOMOUS_DECISION_POLICY.md was read completely.
- D-014 was preserved.
- Owner-reserved decisions were not overridden.
- Legal-dependent questions remain unresolved where necessary.
- Three 12B PARTIAL gates remain unchanged.
- Seven 12A PARTIAL gates remain preserved.
- Outstanding security obligations remain outstanding.
- Five R7 residual weaknesses remain recorded and unfixed.
- R8 remains DEFERRED.
- 12B-C1 remains NOT CLOSED.
- No Prompt 13, 14 or 15 work was initiated.

### I. Validation evidence

List actual validation commands, results, failures, skipped checks and limitations.

Do not invent test results.

### J. Final verdict

Use these categories:

- COMPLETE — all authorized documentation requirements satisfied.
- COMPLETE WITH DOCUMENTED LIMITATIONS — deliverables are complete, but explicitly identified unresolved external or owner-controlled dependencies remain.
- PARTIAL — material authorized deliverables remain incomplete.
- BLOCKED — an essential authorization or dependency prevents meaningful completion.

Do not declare COMPLETE when material requirements are missing.

---

## 17. FINAL GOVERNANCE AND STOPPING RULES

This prompt does not authorize production gameplay implementation.

This prompt does not authorize production database changes.

This prompt does not authorize R8 correction.

This prompt does not authorize 12B-C1 closure.

This prompt does not authorize new balance decisions.

This prompt does not authorize legal-dependent decisions.

This prompt does not authorize future stages.

Do not stage, commit, reset, merge or push Git changes without explicit authorization.

Do not resolve pre-existing unmerged Git entries.

Work in the existing live project directory and preserve unrelated work.

If an issue lies outside the authorized scope, document it without silently expanding the task.

When Prompt 12C is complete, stop.

Do not automatically begin Prompt 13.

---

## 18. FINAL OBJECTIVE

Deliver a coherent, traceable and operationally detailed fair-play specification that fits the existing Nation Supremacy design.

The final work must demonstrate that fair-play and player-protection requirements are integrated with the already designed game systems rather than existing as an isolated document.

The resulting specifications must be suitable as authoritative inputs for subsequent UI, balance, architecture and implementation stages.

**Most important principles:**

1. Follow `AUTONOMOUS_DECISION_POLICY.md` completely.
2. Maintain cross-system consistency with all previously completed prompts.
3. Preserve approved decisions and canonical identifiers.
4. Never invent implementation evidence.
5. Preserve all three 12B PARTIAL gates.
6. Preserve all outstanding security limitations.
7. Do not correct R8 residual weaknesses.
8. Do not close 12B-C1.
9. Do not perform gameplay implementation.
10. Stop after the authorized Prompt 12C scope is completed.

**Nation Supremacy must develop as one consistent game, not as a collection of disconnected specifications.**
