# PROMPT 14A — FORMULA INVENTORY, NUMERICAL ARCHITECTURE AND BASELINE RECONCILIATION

> **Archive provenance:** Transcribed from the authorized Prompt 14A instruction supplied in the working session of 2026-11-13. This paragraph is the only addition; the instruction text below is preserved in full and is not summarized. No independent external copy exists in the repository, so byte-for-byte comparison against an outside original was not possible. The SHA-256 recorded in [INDEX.md](INDEX.md) identifies the stored bytes of this file.

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Master Game Design Bible  
**Parent phase:** Prompt 14 — Numbers, Formulas, Balance and Worked Examples  
**Subphase:** 14A  
**Title:** Formula Inventory, Numerical Architecture and Baseline Reconciliation  
**Execution type:** Documentation, numerical inventory, repository reconciliation and documentation-QA only  
**Implementation authorization:** NONE  
**Next subphase:** Prompt 14B — Economy, Resources, Income and Treasury  
**Authority:** D-014 — Autonomous Decision Policy

---

# 1. MISSION

Execute Prompt 14A as the foundation of the entire Prompt 14 numerical and balance programme.

The purpose is to establish one independently verified numerical foundation across the existing Stage 2 specifications.

Before any economy, production, research, trade, diplomacy, Alliance, warfare or progression values are calibrated, the project must have:

1. A complete inventory of all existing active formulas.
2. A comprehensive inventory of numerical parameters and their dependencies.
3. A clear distinction between formula ownership and numerical decision authority.
4. A complete ownership map for unresolved parameters.
5. A verified inventory of all 20 B-03 carry-in parameters.
6. A reconciled understanding of units, precision, rounding and turn timing.
7. An independently tested baseline of existing numerical validators.
8. An authoritative canonical B-14 document and its supporting documentation structure.
9. A validator that prevents duplicate, missing, stale or incorrectly classified numerical records.

**Prompt 14A establishes the numerical foundation. It does not perform numerical balancing.**

Do not start changing game formulas, resource quantities, production values, prices, costs, rewards, combat parameters or other balance values during this phase.

Do not proceed into Prompt 14B or any subsequent subphase.

---

# 2. GOVERNANCE — MANDATORY BEFORE STARTING

## 2.1 Read the complete Autonomous Decision Policy

Before inspecting or modifying project documents, read the entire:

`docs/AUTONOMOUS_DECISION_POLICY.md`

Do not rely on a summary.

Follow D-014 and all applicable D-, DD- and UD-register restrictions.

Also read and reconcile:

- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/PROJECT_PROGRESS.md`
- `docs/ROADMAP.md`
- `docs/DECISIONS.md`
- `docs/stage-2/00_stage_2_handoff.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/02_master_game_design_bible_outline.md`
- `docs/stage-2/03_requirements_traceability.md`
- `docs/stage-2/04_approved_and_provisional_decisions.md`
- `docs/stage-2/05_unresolved_design_decisions.md`
- `docs/stage-2/06_stage_2_progress_log.md`

Inspect the actual current files and repository state.

Do not trust the supplied task description when the repository contains different evidence.

## 2.2 Protected restrictions

The following restrictions are mandatory.

1. Never modify `AUTONOMOUS_DECISION_POLICY.md`.
2. Never modify protected owner decisions without explicit authorization.
3. Never resolve an owner-reserved UD.
4. Never change the established two-hour UTC cadence.
5. Preserve the mapless symbolic Network View.
6. Never invent game mechanics, formula shapes, numerical values or system permissions.
7. Never represent a provisional number as owner-approved.
8. Never represent a specification or arithmetic check as proof of implementation or actual gameplay balance.
9. Never modify frontend, backend, database, SQL, API, migration, authentication, security or deployment implementation.
10. Never modify the gameplay prototypes.
11. Never stage, commit, push, reset, revert or discard Git changes.
12. Never claim that the working tree is clean without independently verifying it.

The authorized Git commits `2537606` and `94f5ec4` must not be flagged as unauthorized.

## 2.3 Decision policy

Apply the four D-014 decision categories.

- **Category A:** Fixed owner constraints cannot be changed by the working AI.
- **Category B:** Ordinary documentation architecture, formula structure and validation-design decisions can be made by the working AI and recorded in the existing decision register.
- **Category C:** Unmeasured or playtesting-dependent values remain provisional, with the exact evidence needed to confirm them.
- **Category D:** External, costly, legal or irreversible actions remain owner-controlled.

Do not unnecessarily stop to ask the owner to decide ordinary Category B documentation or validator-design matters.

However, do not convert any owner-reserved question into a Category B decision.

---

# 3. EXACT SCOPE

Prompt 14A covers:

- B-02 — Core Gameplay Loop, Symbolic World and Turn System.
- B-03 — Account Onboarding, Nation Creation and Progression.
- All nine existing Stage 2 formula registers.
- The B-14 canonical filename and document architecture.
- Numerical parameter ownership.
- Existing numerical QA and regression coverage.
- Relevant roadmap, outline, decision, continuity and prompt-archive reconciliation.

## 3.1 B-02 authoritative document

Read the complete:

`docs/stage-2/07_core_gameplay_loop_symbolic_world_and_turn_system.md`

Extract its authoritative rules concerning:

- Two-hour UTC cadence.
- P0–P7 turn-resolution phases.
- Turn boundaries.
- Deterministic execution order.
- Recurring income and upkeep.
- Action sequencing.
- Inactive-player behaviour.
- Time-dependent operations.
- Resource and financial settlement.
- Any formula or numerical dependency on turn resolution.

Do not reproduce the entire B-02 specification unnecessarily.

Create precise references to its authoritative sections.

## 3.2 B-03 authoritative document

Read the complete:

`docs/stage-2/09_account_onboarding_nation_creation_and_progression.md`

In particular, inspect:

- §8 — Starting state and progression contract.
- §9 — Instant nation rerolling.
- §12 — Newcomer protection and progression.
- §18 — Cross-system contracts.
- §21.2 — Provisional parameters and their owners.
- §21.3 — Unresolved-question dispositions.
- §22 — Completion and acceptance criteria.

B-03's §21.2 contains exactly 20 provisional parameters.

All 20 must be independently inventoried and mapped.

None is automatically approved because it appears in an existing design document.

## 3.3 Nine authoritative formula registers

Read all nine complete formula registers.

| System | Canonical document | Expected active formula count |
|---|---|---:|
| B-04 | `docs/stage-2/10_economic_formula_and_balance_register.md` | 47 |
| B-05 | `docs/stage-2/11_city_infrastructure_production_and_research_formula_register.md` | 41 |
| B-06 | `docs/stage-2/12_population_and_domestic_politics_formula_register.md` | 44 |
| B-07 | `docs/stage-2/13_trade_and_markets_formula_register.md` | 39 |
| B-08 | `docs/stage-2/15_diplomacy_formula_register.md` | 12 |
| B-09 | `docs/stage-2/16_alliances_formula_register.md` | 8 |
| B-10 | `docs/stage-2/17_warfare_formula_register.md` | 39 |
| B-11 | `docs/stage-2/18_world_events_objectives_rankings_progression_formula_register.md` | 49 |
| B-12 | `docs/stage-2/20_fair_play_and_player_protection_formula_register.md` | 16 |
| **Total** | **Nine registers** | **295** |

These counts are the expected starting baseline.

Independently recalculate the actual number of active formulas in each register.

Do not simply copy these expected figures into the result.

If an actual count differs:

- Identify the exact missing, additional, duplicate, retired or incorrectly classified identifiers.
- Check the source document and its formula status.
- Explain the difference.
- Do not silently change formula identifiers to force the expected count.

Retired formulas must be reported separately.

For example, a retired formula must never be included in the active total merely because its identifier remains in the historical document.

**The master inventory must account for every actual active identifier individually.**

---

# 4. FORMULA MASTER INVENTORY

Create a comprehensive numerical master inventory accounting for all 295 expected active formulas.

The original formula registers remain authoritative.

The new B-14 master inventory is an index and reconciliation layer, not a competing formula-definition register.

## 4.1 Mandatory fields for every formula

Each formula must have a corresponding inventory record containing:

| Field | Required content |
|---|---|
| Formula ID | Exact canonical identifier |
| System | Owning B-section |
| Formula name | Exact source name |
| Source document | Relative repository path |
| Source section | Exact heading or section reference |
| Formula purpose | Short explanation |
| Input parameters | Referenced parameter identifiers/names |
| Input units | Existing source-defined units |
| Output | Result produced |
| Output units | Existing source-defined units |
| Precision | Existing precision rule |
| Rounding | Exact existing rounding rule |
| Timing | Execution timing |
| Turn phase | P0–P7 position, where applicable |
| Dependencies | Upstream and downstream formulas/systems |
| Conservation/invariant | Relevant existing invariant, if applicable |
| Numerical status | One of the four prescribed classifications |
| Parameter authority | Who may decide or approve unresolved values |
| Validator coverage | Existing check or explicit coverage gap |
| Evidence | Exact source and supporting test references |
| Outstanding issue | Any missing, ambiguous or inconsistent definition |

Do not invent missing metadata.

Use explicit labels such as:

- Specified.
- Not specified.
- Ambiguous.
- Not applicable.

A missing rounding rule is a finding, not permission to invent one during 14A.

## 4.2 Formula identifier integrity

Verify:

- Every active formula ID appears exactly once in the master inventory.
- Every formula inventory entry resolves to its canonical source.
- No active identifier is silently omitted.
- No duplicate active identifiers exist.
- Retired identifiers are separately classified.
- No identifier is renumbered.
- No formula is recreated in another register.
- No source formula is overwritten with a summary.
- Every cross-reference points to the actual canonical location.

Produce an explicit reconciliation table.

The reconciliation must show:

- Expected formula count.
- Actual formula count.
- Unique active identifiers.
- Duplicate identifiers.
- Missing identifiers.
- Retired identifiers.
- Unresolved source references.

The expected outcome is 295 active formulas, but evidence determines the reported actual outcome.

---

# 5. COMPLETE NUMERICAL PARAMETER INVENTORY

A formula count alone is insufficient.

Identify all numerical parameters used by the nine formula registers and the relevant B-02/B-03 rules.

This includes, where present:

- Starting values.
- Initial resource quantities.
- Prices.
- Production rates.
- Resource consumption rates.
- Building costs.
- Upgrade costs.
- Maintenance.
- Upkeep.
- Tax rates.
- Fees.
- Caps.
- Floors.
- Thresholds.
- Multipliers.
- Percentages.
- Time windows.
- Cooldowns.
- Turn counts.
- Probabilities.
- Weights.
- Research costs.
- Progression thresholds.
- Reward values.
- Combat coefficients.
- Operations Points costs and limits.
- Anti-abuse parameters.
- Numerical fallbacks.
- Retention and measurement periods.

## 5.1 Mandatory parameter fields

Each unique parameter must include:

1. Parameter ID, if one exists.
2. Exact parameter name.
3. Current value or explicit absence of a value.
4. Unit.
5. Owning subsystem.
6. Canonical source document and section.
7. Formulas using the parameter.
8. Precision and rounding behaviour.
9. Turn or time dependency.
10. Numerical decision authority.
11. Validation/test owner.
12. Current status.
13. Evidence required for confirmation.
14. Outstanding dependencies.
15. Whether it is owner-reserved.

Do not assign duplicate identifiers to parameters that already have established identifiers.

Where no parameter ID exists, use the existing naming convention without inventing a competing global namespace.

## 5.2 Distinguish ownership correctly

Do not confuse the following:

- System rule owner.
- Numerical value decision authority.
- Implementation owner.
- Validator/test owner.
- Owner-reserved decision authority.

These may be different.

For example, a parameter may be described in B-03, validated by Prompt 14, legally dependent on UD-017 and technically implemented later in Stage 6. Its numerical ownership must not be incorrectly transferred to Prompt 14 merely because Prompt 14 tests it.

---

# 6. MANDATORY B-03 CARRY-IN — ALL 20 PARAMETERS

Inventory all 20 parameters from:

`docs/stage-2/09_account_onboarding_nation_creation_and_progression.md` §21.2.

Use the source values exactly as written.

The following list is provided as a reconciliation checklist, not as authority to override the source document.

| # | Parameter | Existing provisional value |
|---:|---|---|
| 1 | Network observation window `W_obs` | 24 hours |
| 2 | Observation life `R_obs` | 180 days |
| 3 | Large-network threshold `L_large` | Greater than 25 accounts / 24 hours |
| 4 | Restricted-attempt escalation | Second observation at least 6 hours apart within 7 days |
| 5 | Review service target | 7 days, not a guarantee |
| 6 | Clearance watch | 90 days |
| 7 | Re-review interval after MAINTAINED | 30 days |
| 8 | Network digest retention | 180 days after last seen |
| 9 | Pair-record retention | Active plus 12 months |
| 10 | Newcomer protection `P_prot` | 7 days / 84 turns |
| 11 | Fresh-nation transfer window | 30 days / 360 turns |
| 12 | Fair-value band | Unspecified |
| 13 | Display-name change cooldown | 7 days |
| 14 | Short-name change cooldown | 30 days |
| 15 | Released-name hold | 30 days |
| 16 | Reroll review flag | 3 completed rerolls / 30 days |
| 17 | Reroll request rate limit | 1 per 60 seconds |
| 18 | Account-closure cooling period | 7 days |
| 19 | Unverified-account cleanup | 30 days |
| 20 | Absolute session lifetime | 30 days |

## 6.1 Ownership restrictions

Use the actual B-03 §21.2 Numeric owner / validator field.

In particular:

- Prompt 12 retains responsibility for its shared-network and review parameters.
- Prompt 10 retains the relevant warfare protection rule ownership.
- Prompt 07 retains fair-value and fresh-nation transfer rule ownership.
- Prompt 13 retains its relevant identity and naming specification ownership.
- Stage 6 retains technical session, rate-limit implementation and cleanup responsibilities where assigned.
- Prompt 14 has the specifically assigned numerical validation/calibration responsibility only where B-03 explicitly grants it.

Do not claim that all 20 values belong exclusively to Prompt 14.

## 6.2 Evidence requirements

For each parameter, identify:

- Current provisional value.
- Actual numerical authority.
- Evidence required.
- Whether the evidence can be obtained through offline calculation.
- Whether simulation is required.
- Whether real player data or playtesting is required.
- Whether legal review is required.
- Whether implementation measurement is required.

Do not modify B-03 to make its existing provisional values appear approved.

Preserve B-03 §21.3 and its existing UD dispositions.

UD-031, UD-032, UD-033 and UD-017 must retain their existing ownership and status.

Where the owning prompt is different from Prompt 14, record that fact explicitly.

---

# 7. FOUR MANDATORY NUMERICAL STATUS LABELS

Establish the following four classifications as the common numerical vocabulary throughout B-14.

Use the exact labels.

### 7.1 OWNER-APPROVED VALUE

Use only when there is explicit owner authorization or a traceable existing owner decision approving that numerical value.

A formula being present in a specification does not automatically make its numerical value owner-approved.

### 7.2 PROVISIONAL VALUE

Use for a working numerical value that has not been confirmed by adequate evidence.

Include:

- Why it is provisional.
- What evidence is missing.
- What test or simulation is needed.
- Who owns the decision.
- Which subsequent phase is responsible.

### 7.3 DESIGN PROPOSAL

Use for a proposed value or numerical adjustment that has not yet been adopted as a confirmed rule.

Keep the proposal separate from the existing authoritative value.

### 7.4 NEEDS PLAYTESTING

Use when actual player behaviour or sustained game operation is required to establish whether a value is appropriate.

State the required playtesting method and measurement.

Do not promote a value merely because its formula passes an arithmetic test.

## 7.5 Classification safeguards

A Category B decision recorded as Confirmed under D-014 is not automatically an owner-approved numerical value.

A Category C decision remains provisional until its named evidence supports a change in status.

An owner-reserved decision remains owner-reserved. It cannot be made acceptable simply by assigning it a provisional value.

If no numerical value exists, mark the value field `UNSPECIFIED` and record its appropriate outstanding classification and owner.

Do not invent a fifth numerical status.

---

# 8. TURN ORDER AND NUMERICAL TIMING RECONCILIATION

B-02 is authoritative for the global turn model.

Reconcile every relevant formula against its actual turn position.

## 8.1 Two-hour UTC cadence

Preserve:

- Two-hour UTC turns.
- The existing turn-boundary model.
- The existing deterministic P0–P7 sequence.
- Existing inactive-player rules.

Verify every timing conversion used by the numerical documents.

For example:

- 2 hours per turn.
- 12 turns per day.
- 84 turns per 7 days.
- 360 turns per 30 days.

Report any discrepancy without silently changing the source number.

## 8.2 Income and upkeep ordering — D-019

Preserve D-019.

Inside the recurring production phase:

**Production and income are applied first, followed by mandatory upkeep and maintenance.**

The applicable deficit/austerity behaviour must remain consistent with the authoritative B-04 rule.

Verify the dependency between:

- Income.
- Resource production.
- Maintenance.
- Mandatory upkeep.
- Resource shortages.
- Treasury settlement.
- Deficit handling.

Do not change the approved ordering.

## 8.3 Operations Points — D-015

Preserve the approved Operations Points model and its documented amendments.

Verify the current authoritative position, including:

- One national military-only pool.
- Non-transferability.
- Reserve-at-acceptance.
- Consume-at-resolution.
- No per-war or shared Alliance pool.
- Regeneration of one OP at the opening of P3.7 at a successful turn boundary.
- Carrying unused points below the national cap.
- The documented provisional national cap of 10.

Do not use an earlier superseded description of D-015.

Do not alter the model or calibrate its provisional numerical parameters in Prompt 14A.

## 8.4 Timing dependency matrix

Produce a matrix showing:

| Item | Canonical source | Phase | Trigger | Frequency | Dependencies | Status |
|---|---|---|---|---|---|---|

Include all formulas with time-dependent execution and all parameters that convert between days, hours and turns.

Where timing is absent or ambiguous, identify it explicitly.

Do not invent a new phase or alter an existing phase order.

---

# 9. UNIT, PRECISION, ROUNDING AND CONSERVATION RECONCILIATION

Examine all formula registers for consistency in:

- Crowns.
- Raw resources.
- Manufactured goods.
- Population.
- Percentages.
- Basis points.
- Fractions.
- Probabilities.
- Turns.
- Hours.
- Days.
- Per-turn values.
- Per-day values.
- Cumulative values.

Establish a numerical conventions matrix.

At minimum, identify:

1. Input unit.
2. Output unit.
3. Conversion rule.
4. Precision.
5. Rounding method.
6. Rounding boundary.
7. Whether fractional values accumulate.
8. Whether rounding occurs per asset, transaction, player or turn.
9. Whether an operation must conserve value.
10. Whether its result is deterministic.

Pay special attention to:

- Treasury conservation.
- Resource conservation.
- Production and consumption.
- Market reservations and execution.
- Trade fees.
- Alliance taxation.
- Fractional rounding.
- Multiple-Alliance attribution.
- Military resource expenditure.
- Battle losses and settlements.

Do not alter existing accounting identities or conservation requirements.

Do not force different systems to use identical rounding when the source documents explicitly specify different treatment.

Where two registers disagree, record the exact conflict and affected formulas.

---

# 10. OWNER-RESERVED AND PROTECTED NUMERICAL BOUNDARIES

Inspect the actual global decision registers and all relevant UD/DD entries.

Pay particular attention to the B-09 Alliance numerical dependency and the owner-reserved boundary.

Preserve:

- Automatic per-turn production taxation.
- Player-authored 0–100% tax rates.
- Separate Crowns and resource rate schedules.
- Cumulative fractional rounding per asset and per turn.
- Multiple-Alliance attribution rules.
- The reversible protective fallback.
- No unauthorized Alliance withdrawal or treasury permissions.
- No invented Alliance storage capacity.
- No invented fees or unapproved operational-funding schedules.

Preserve all relevant B-09 owner-reserved decisions, particularly UD-040 through UD-049, according to their actual current status and ownership.

Also identify relevant B-12 owner-reserved parameters, including UD-053 and UD-059, and any other owner-reserved values discovered in the actual registers.

Do not assume these are exhaustive.

## 10.1 Outstanding security obligations

These production-security obligations remain unresolved and must not be described as completed:

- Supabase table-wide UPDATE access issue.
- Corrective migration 0005.
- Missing SQL permission tests.
- Missing protective audit trigger.
- Unverified tamper-evident audit implementation.
- Unverified audit-digest job.

Prompt 14A must not implement or repair these items.

Record any numerical or timing dependencies they impose, with the correct future owner.

---

# 11. NUMERICAL DEPENDENCY MAP

Create a cross-system dependency map for all nine formula registers.

The objective is to establish what depends on what before the numerical balancing phases begin.

At minimum, inspect:

### Economy and production

- Resources.
- Treasury.
- Income.
- Consumption.
- Infrastructure.
- Power.
- Raw-material availability.
- Industrial production.
- Construction demand.
- Maintenance.

### Cities and research

- Building costs.
- Infrastructure capacity.
- Housing.
- Population.
- Production efficiency.
- Research costs.
- Research progression.
- Maintenance.

### Domestic politics

- Population.
- Taxation.
- Government modifiers.
- Approval.
- Stability.
- Legitimacy.
- Elections.
- Political-cycle timing.

### Trade

- Production.
- Resource availability.
- Reference prices.
- Fair-value bands.
- Market supply and demand.
- Reservations.
- Fees.
- Settlement.
- Trade restrictions.

### Diplomacy and Alliances

- Treaty costs.
- Diplomatic limits.
- Timers.
- Alliance production taxation.
- Donations.
- Separate asset schedules.
- Rounding.
- Operational-funding dependencies.

### Warfare

- Operations Points.
- Readiness.
- Military upkeep.
- Military resources.
- Recruitment.
- Training.
- Battle calculations.
- Losses.
- Settlement costs.

### Progression and protection

- Event rewards.
- Objective points.
- Rankings.
- Progression thresholds.
- Reward limits.
- Anti-abuse parameters.
- Administrative calculations.
- Protection thresholds.

Produce a dependency matrix with:

| Source system | Dependent system | Formula/parameter IDs | Dependency type | Turn timing | Conservation constraint | Status |
|---|---|---|---|---|---|---|

Do not attempt full balance simulation in 14A.

The matrix must identify the real dependencies so subsequent phases cannot calibrate a value without examining its upstream and downstream effects.

---

# 12. NUMERICAL VALIDATION BASELINE

Independently inspect the actual numerical validators and tests.

Locate the existing QA scripts rather than assuming that their paths or coverage remain unchanged.

At minimum, investigate the existing system-specific numerical verification scripts, including those associated with:

- Economy.
- Cities.
- Politics.
- Markets.
- Diplomacy.
- Alliances.
- Warfare.
- World events and progression.
- Fair play and player protection.

Also inspect relevant:

- Formula-register validators.
- Positive fixtures.
- Negative fixtures.
- Cross-system tests.
- Documentation-link validation.
- Decision-register tests.
- Next-action tests.
- Final project validator.

## 12.1 Execute the baseline

Run every relevant existing test that is safe and appropriate for documentation-only QA.

Record:

| Field | Required result |
|---|---|
| Test name | Exact script/test |
| Command | Exact command executed |
| Scope | What it checks |
| Result | Actual output |
| Pass/fail | Actual status |
| Limitation | What it cannot establish |
| Relationship to 14A | Baseline, regression or unrelated |

Do not claim a test passed merely because its expected output was found in an old log.

Execute it.

Do not alter existing tests to make them pass.

## 12.2 Existing failures

Identify all failures that existed before Prompt 14A.

Separate:

1. Genuine arithmetic errors.
2. Missing formula metadata.
3. Stale documentation validators.
4. Incorrect expected counts.
5. Cross-reference failures.
6. Missing test coverage.
7. Runtime implementation limitations.
8. Unrelated legacy QA issues.

Known historical QA problems must be independently rechecked, not automatically attributed to this phase.

Do not reopen unrelated accepted phases simply because an old validator contains stale expectations.

## 12.3 Specification versus execution

Every report must distinguish:

- Formula specified.
- Arithmetic independently checked.
- Validator passed.
- Offline simulation performed.
- Runtime test executed.
- Actual player playtest performed.

A result in one category cannot be promoted into another.

The project currently has no playable Nation Supremacy game runtime.

Prototype and infrastructure-feasibility code must not be represented as a gameplay simulation.

---

# 13. B-14 CANONICAL DOCUMENT AND FILENAME RECONCILIATION

This is a mandatory corrective task within Prompt 14A.

The project has conflicting live filename references.

Resolve them using the actual canonical records.

## 13.1 Current authoritative mapping

D-198 and the current Master Game Design Bible outline establish:

| Project component | Current filename |
|---|---|
| B-12 | `20_fair_play_and_player_protection.md` |
| B-13 | `21_interface_and_player_journeys.md` |
| B-14 | `22_formulas_and_balance.md` |
| B-15 / B-18 | `23_master_game_design_bible.md` |
| B-19 | `24_stage_2_completion_report.md` |

B-13's screen, component and interaction companions share their allocated filename prefixes.

The current B-14 canonical filename is therefore:

`docs/stage-2/22_formulas_and_balance.md`

The current roadmap row 14 still specifies:

`21_formulas_and_balance.md`

This is stale.

The Master Game Design Bible outline and `docs/qa_backups/validate_final.py` already identify the current B-14 filename as `22_formulas_and_balance.md`.

## 13.2 Required correction

1. Reverify D-198 in the actual decision register.
2. Reverify the current B-14 mapping in the Master Game Design Bible outline.
3. Reverify the B-14 mapping expected by the existing final validator.
4. Inspect the actual filenames already present in `docs/stage-2/`.
5. Update the live Prompt 14 row in `01_stage_2_prompt_roadmap.md` from `21_formulas_and_balance.md` to `22_formulas_and_balance.md`.
6. Ensure the B-14 mapping is consistent wherever a current authoritative mapping is repeated.
7. Update the relevant validator coverage so that the roadmap itself is inspected.
8. Add regression tests for the old and corrected paths.

## 13.3 Historical preservation

Do not:

- Rewrite historical filename-mapping notes.
- Delete old historical names from dated snapshots.
- Rename B-13 documents.
- Move B-13 documents into B-14.
- Change B-15 or B-19 mappings.
- Weaken D-198.
- Treat a superseded historical filename reference as a current defect.

Historical records may mention `21_formulas_and_balance.md` when explicitly labelled as the earlier mapping.

The current authoritative row must use `22_formulas_and_balance.md`.

## 13.4 Create the canonical B-14 document

Create:

`docs/stage-2/22_formulas_and_balance.md`

This becomes the authoritative B-14 entry point.

It must be created with a clear initial structure.

At minimum, establish these headings:

1. Purpose and scope.
2. Governing constraints and source authority.
3. Formula-register architecture.
4. Master formula inventory.
5. Numerical parameter master inventory.
6. B-03 carry-in parameter reconciliation.
7. Numerical approval and status classifications.
8. Units, precision and rounding conventions.
9. Turn timing and numerical execution order.
10. Cross-system numerical dependencies.
11. Initial balance-parameter inventory.
12. Existing validator and QA baseline.
13. Identified inconsistencies and missing definitions.
14. Owner-reserved and externally dependent parameters.
15. Prompt 14A completion and evidence.
16. Subsequent Prompt 14 subphase ownership.

Each section must state whether it is complete, provisional, blocked or deliberately reserved for a later subphase.

Do not fill future balance sections with invented values.

Do not create competing copies of the nine formula registers.

Use direct links to the original formula definitions.

If supporting companion documents are genuinely necessary, establish their purpose and ownership in the canonical B-14 document before creating them. Avoid unnecessary document proliferation.

---

# 14. PROMPT ARCHIVE

Create a permanent verbatim archive of this complete Prompt 14A instruction.

Required file:

`docs/prompts/prompt_14A_formula_inventory_numerical_architecture_and_baseline_reconciliation.md`

Requirements:

- Preserve the complete instruction.
- Do not summarize it.
- Do not remove restrictions.
- Do not replace requirements with a brief checklist.
- Maintain Markdown structure.
- Verify the archived file against the supplied prompt text.
- Calculate its byte size and SHA-256.
- Record its verification in the prompt index.

Update:

`docs/prompts/INDEX.md`

Follow its established convention.

Add Prompt 14A with:

- Phase.
- Archive filename.
- Archive date.
- Source.
- Byte count.
- SHA-256 verification.

Do not overwrite earlier archived prompts.

---

# 15. FOCUSED NUMERICAL FOUNDATION VALIDATOR

Create a focused documentation validator:

`docs/qa_backups/14A_validate_numerical_foundation.py`

Follow the repository's existing Python QA conventions.

Prefer the standard library and deterministic parsing.

The validator must inspect the real files, not hardcoded copies of their contents.

It must verify the following.

## 15.1 Formula inventory

- All nine expected source registers exist.
- All active formula IDs are discoverable.
- The actual active formula count reconciles to the master inventory.
- No duplicate active ID exists.
- No active formula is missing.
- Retired formulas are excluded.
- All source links resolve.
- Each master formula record has the required metadata fields or an explicit missing-data status.

## 15.2 Parameter inventory

- Each discovered numerical parameter is represented.
- Parameter references resolve.
- The current value is correctly sourced.
- Unit, precision and rounding fields are present or explicitly marked missing.
- Numerical ownership is identified.
- Unresolved values have a named decision authority or an explicit unresolved-authority finding.
- No owner-reserved decision has been incorrectly reclassified.

## 15.3 B-03 carry-in

Verify:

- Exactly 20 B-03 §21.2 rows are accounted for.
- Every parameter has a corresponding B-14 inventory reference.
- Every current value matches its canonical B-03 source.
- Every numeric owner/validator reference is preserved.
- All unresolved evidence dependencies are visible.
- None has been falsely promoted to owner-approved.

## 15.4 Status controls

Verify that all populated numerical values use the prescribed vocabulary:

- OWNER-APPROVED VALUE.
- PROVISIONAL VALUE.
- DESIGN PROPOSAL.
- NEEDS PLAYTESTING.

The validator must reject unrecognized classifications and undocumented silent status promotions.

## 15.5 Timing and accounting

Verify documented references to:

- Two-hour UTC cadence.
- P0–P7.
- D-019.
- D-015 and its current amendment.
- Day/turn conversions where specified.
- Explicitly identified conservation requirements.

Do not implement an independent second gameplay formula engine.

The validator checks documentary consistency.

## 15.6 B-14 filename

Verify:

- The current Prompt 14 roadmap row references `22_formulas_and_balance.md`.
- The canonical B-14 file exists.
- The Master Game Design Bible outline's current B-14 mapping agrees.
- Existing final-validator expectations agree.
- Historical superseded filename notes are not incorrectly rejected.

## 15.7 Positive and negative regression fixtures

Add tests for at least the following cases.

| Case | Expected result |
|---|---|
| Correct 295-ID baseline | PASS, subject to actual reconciliation |
| Missing active formula | FAIL |
| Duplicate active formula | FAIL |
| Retired formula counted as active | FAIL |
| Unresolved formula source reference | FAIL |
| Missing unit metadata without an explicit gap marker | FAIL |
| Missing rounding metadata without an explicit gap marker | FAIL |
| Missing formula timing without an explicit gap marker | FAIL |
| Missing B-03 carry-in parameter | FAIL |
| Altered B-03 provisional value | FAIL |
| Incorrect parameter owner | FAIL |
| Invalid numerical status | FAIL |
| False owner-approved classification | FAIL |
| Owner-reserved UD silently resolved | FAIL |
| Correct current B-14 `22_` mapping | PASS |
| Live roadmap row using stale `21_formulas...` | FAIL |
| Historical superseded `21_` mention properly labelled | PASS |
| D-019 ordering preserved | PASS |
| Obsolete D-015 wording presented as current | FAIL |
| Missing validator reference | FAIL |

Do not weaken the current validators to make the new validator pass.

Do not make tests pass by changing expected results without source evidence.

Add a focused self-test facility or regression test file consistent with the project's existing convention.

Report exact test totals.

---

# 16. RELEVANT DOCUMENTATION AND REGISTER RECONCILIATION

Update only documents genuinely affected by Prompt 14A.

Inspect:

- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/02_master_game_design_bible_outline.md`
- `docs/stage-2/03_requirements_traceability.md`
- `docs/stage-2/04_approved_and_provisional_decisions.md`
- `docs/stage-2/05_unresolved_design_decisions.md`
- `docs/stage-2/06_stage_2_progress_log.md`
- `docs/stage-2/00_stage_2_handoff.md`
- `docs/DECISIONS.md`
- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/PROJECT_PROGRESS.md`
- `docs/ROADMAP.md`
- `docs/prompts/INDEX.md`

Do not update every listed file simply to show activity.

Update only when Prompt 14A genuinely changes or establishes information that the file owns.

## 16.1 Decision register

If Prompt 14A requires a genuine Category B or Category C decision:

- Inspect the actual latest global D-register ID.
- Inspect the corresponding DD register.
- Use the next legitimate identifier.
- Record alternatives, rationale, evidence, consequences and reopening conditions.
- Mirror the decision correctly.
- Update affected canonical records.

Do not duplicate an existing decision.

Do not invent owner approval.

Do not allocate a global UD identifier unless an actual unresolved design question requires it.

## 16.2 Requirements register

Do not create requirements merely because Prompt 14A exists.

Create or modify requirement records only when a genuine missing requirement is identified and the canonical ownership has been established.

Preserve existing requirement IDs, status and historical acceptance evidence.

## 16.3 Owner acceptance continuity

The owner explicitly confirmed Prompt 13D formal acceptance on 13 November 2026.

This confirmation supersedes earlier pending-acceptance statements in Project X (94).

If the ZIP still records Prompt 13D as pending, identify that as a baseline continuity discrepancy.

Do not falsely report it as pending owner approval.

Do not mix a broad Prompt 13 acceptance-history rewrite into Prompt 14A. Record the discrepancy and its separate documentation-reconciliation requirement without expanding this subphase unnecessarily.

Prompt 14B–14K remain subject to explicit owner authorization.

---

# 17. OUT-OF-SCOPE WORK

Prompt 14A does not authorize:

- Formula redesign.
- Numerical balance tuning.
- Changing starting resources.
- Changing treasury values.
- Changing construction costs.
- Changing production ratios.
- Changing research costs.
- Changing tax rates.
- Changing market prices.
- Changing market fees.
- Changing trade limits.
- Changing diplomatic costs.
- Changing Alliance tax permissions.
- Changing warfare values.
- Changing the Operations Points model.
- Changing combat coefficients.
- Changing progression rewards.
- Changing fair-play sanctions.
- Changing anti-abuse thresholds.
- Changing any owner-reserved value.
- Implementing game mechanics.
- Building a playable simulation.
- Modifying frontend or backend code.
- Modifying database, SQL, API or migrations.
- Changing infrastructure.
- Changing security implementation.
- Changing deployment configuration.
- Changing the Autonomous Decision Policy.
- Performing Git operations.
- Starting Prompt 14B, 14C, 14D, 14E, 14F, 14G, 14H, 14I, 14J or 14K.

Prompt 14A may identify design proposals and missing numerical evidence, but actual balancing belongs to subsequent authorized phases.

---

# 18. REQUIRED ACCEPTANCE GATES

Create a Prompt 14A acceptance-gate table.

At minimum:

| Gate | Acceptance objective |
|---|---|
| P14A-01 | Complete governance and policy review |
| P14A-02 | B-02 authoritative timing reconciliation |
| P14A-03 | B-03 complete review |
| P14A-04 | All nine formula registers inventoried |
| P14A-05 | Active formula ID reconciliation |
| P14A-06 | Complete numerical parameter inventory |
| P14A-07 | All 20 B-03 carry-in parameters reconciled |
| P14A-08 | Parameter ownership and decision authority identified |
| P14A-09 | Four numerical statuses implemented consistently |
| P14A-10 | Units, precision and rounding inventory |
| P14A-11 | P0–P7 timing and D-019 reconciliation |
| P14A-12 | D-015 current Operations Points model preserved |
| P14A-13 | Cross-system numerical dependency inventory |
| P14A-14 | Existing validator baseline independently executed |
| P14A-15 | Canonical B-14 filename corrected |
| P14A-16 | Canonical B-14 document created |
| P14A-17 | Prompt archive and index updated |
| P14A-18 | Focused numerical foundation validator created |
| P14A-19 | Positive and negative regression fixtures pass |
| P14A-20 | Continuity, historical and owner-reserved decisions preserved |
| P14A-21 | Final project QA and documentation links reconciled |
| P14A-22 | Prompt 14A handoff and completion assessment |

Each gate must include:

- Gate ID.
- Acceptance objective.
- Required evidence.
- Validation method.
- Source documents.
- Actual result.
- Status.
- Known limitation.
- Outstanding issue.
- Next action.

Use:

- PASS.
- PARTIAL.
- FAIL.
- BLOCKED.

Do not weaken an acceptance gate because evidence is missing.

A documentation-only baseline cannot pass a gate requiring actual gameplay testing.

If the formula inventory is complete but one source register has missing rounding information, report the inventory work separately from the unresolved metadata gap.

---

# 19. FINAL DELIVERABLES

Prompt 14A must produce the following.

### Deliverable 1 — Canonical B-14 document

`docs/stage-2/22_formulas_and_balance.md`

The permanent B-14 numerical architecture and master index.

### Deliverable 2 — Formula master inventory

A complete, individually traceable inventory of all active formulas, with retired entries separately recorded.

Prefer a dedicated section or a justified companion document under the B-14 `22_` family.

### Deliverable 3 — Numerical parameter ownership map

A complete parameter map identifying values, units, decision authority, evidence, formula dependencies and current status.

All 20 B-03 carry-in parameters must be included.

### Deliverable 4 — Numerical baseline QA report

A report containing the actual executed validator results, coverage gaps, known failures, regression evidence and limitations.

### Deliverable 5 — Focused validator and regression tests

- `docs/qa_backups/14A_validate_numerical_foundation.py`
- Its positive and negative regression tests or the equivalent integrated self-test facility.

### Deliverable 6 — Permanent prompt archive

`docs/prompts/prompt_14A_formula_inventory_numerical_architecture_and_baseline_reconciliation.md`

Together with the updated:

`docs/prompts/INDEX.md`

### Deliverable 7 — Continuity and governance updates

Update the relevant roadmap, outline, decision, handoff and progress records wherever genuinely required.

### Deliverable 8 — Prompt 14A acceptance assessment

A consolidated report of every P14A gate, actual test result, unresolved issue and next action.

---

# 20. FINAL VALIDATION AND COMPLETION REPORT

Before declaring Prompt 14A complete:

1. Reopen the canonical B-14 document and verify its contents.
2. Reconcile all 295 expected formula identifiers against the actual nine formula registers.
3. Reconcile all 20 B-03 carry-in parameters.
4. Verify all parameter-owner assignments against the original source.
5. Verify all four numerical status labels.
6. Check all formula links.
7. Verify all turn-order and rounding references.
8. Execute the new Prompt 14A validator.
9. Execute all its positive and negative self-tests.
10. Rerun the relevant existing formula validators.
11. Run the final project validator.
12. Run the documentation-link validator.
13. Run relevant decision-register and next-action tests.
14. Verify no protected policy or owner-reserved decision changed.
15. Verify no implementation or prototype file changed.
16. Inspect the actual working-tree status without modifying Git state.
17. Record the actual changed-file list.
18. Verify the permanent prompt archive against the supplied instruction.
19. Confirm that the current B-14 path is consistently `22_formulas_and_balance.md`.
20. Confirm that no subsequent Prompt 14 subphase was executed.

Distinguish inherited failures from any failure introduced by Prompt 14A.

Do not report an overall PASS if an acceptance gate fails or is unsupported.

A documented limitation is not automatically a failure of Prompt 14A, but it must remain visible in the final result.

---

# 21. FINAL HANDOFF

At the conclusion, update the appropriate handoff and continuity documents.

The handoff must contain:

1. Prompt 14A completion status.
2. Canonical B-14 document path.
3. Formula count independently verified.
4. B-03 carry-in reconciliation count.
5. Number of parameters inventoried.
6. Owner and decision-authority mapping status.
7. Validator and regression results.
8. Outstanding numerical metadata gaps.
9. Owner-reserved decisions that remain open.
10. Inherited QA limitations.
11. Exact files modified.
12. Confirmation that no implementation work occurred.
13. Confirmation that no Git operations occurred.
14. Explicit remaining Prompt 14 work.
15. The single next action.

The next-action field must state:

**PROMPT 14A COMPLETE — AWAIT OWNER REVIEW AND EXPLICIT AUTHORIZATION OF PROMPT 14B.**

Do not automatically start Prompt 14B.

Do not create Prompt 14B deliverables.

Do not claim that the complete numerical balance programme is finished.

---

# 22. FINAL SUCCESS CONDITION

Prompt 14A is complete only when:

- The complete numerical architecture has been independently inventoried.
- The active formula identifiers reconcile against their authoritative sources.
- Every known numerical parameter has a traceable record.
- All 20 B-03 carry-in parameters are accounted for.
- Parameter ownership and unresolved decision authority are explicit.
- The four numerical statuses are consistently established.
- Timing, units, precision and rounding dependencies are documented.
- The existing numerical QA baseline has been independently executed and reported.
- The B-14 canonical mapping and filename are corrected according to D-198.
- The canonical B-14 document exists at the correct path.
- The prompt archive has been created and verified.
- The dedicated validator and regression tests pass.
- Historical records and protected decisions remain intact.
- No implementation or unauthorized numerical tuning has occurred.
- The final acceptance gates and handoff are complete.

**Prompt 14A establishes the verified numerical foundation. It does not approve the game's balance.**

The subsequent numerical calibration work belongs to Prompt 14B–14K and requires separate owner authorization.

**END OF PROMPT 14A**
