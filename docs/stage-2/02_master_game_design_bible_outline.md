# Master Game Design Bible — outline and authority map

> **09B acceptance status (2026-11-03):** **Phase 09B Alliance specification and documentation: ACCEPTED.** Recorded at the specification/documentation level by **D-142 / DD-165**; production implementation, live-game integration testing and release remain pending, no `UD-040`–`UD-049` is resolved, and the record is not a new owner authorization. Automatic per-turn Alliance taxation is reconciled with `ALL-006`–`ALL-008` and §14; the Alliance Receiving Ledger is a four-category receipt/accounting record with one purpose-limited operational debit; `UD-045` holds only the narrow tax-management permission set and `UD-046` remains Open for ownership, custody, capacity, general withdrawal and general spending; `AT-E00`/`AT-E01` register record-only versus NAP effects; and `AX-01`–`AX-30` (30 contracts) are current. **Prompt 09C — Alliance workflows, edge cases, acceptance matrix and release-gate evidence — is COMPLETE at the specification/documentation level (2026-11-03; log §53); Prompt 10A — Politics and War warfare research — is complete (research/documentation only; log §56); Prompt 10B is complete at the specification/documentation level (log §58) and corrected by 10B-C/10B-C2/10B-C3/10B-C4 (log §§59–§62); Prompt 10C is complete at the specification/documentation level (2026-11-04; log §63–§66); Prompt 11 is next and has not started**; the 09C canonical deliverable is `16_alliances_workflows_acceptance.md`, which this pass does not create. No 09B redesign or research is authorized.

**Version:** 1.15 · **Created:** 2026-10-23 · **Stage 2, Prompt 01** · **Revised:** 2026-11-05 (v1.15 registers Prompt 11B as complete at the system-specification level, links the B-11 rulebook and formula register, records 723 `WEP-` rules, 50 `F-WEP-` formulas, 60 requirements REQ-704–REQ-763 and D-152…D-161 / DD-200–DD-209, and moves the live task to Prompt 11C. The v1.14 revision record follows: v1.14 registered Prompt 11A as complete at the research/design-foundations level, linked its three research deliverables from the B-11 entry, recorded the 11A/11B/11C split (**D-144** / **DD-192**) and moved the live task to Prompt 11B; at that point B-11 stayed Planned because 11A wrote no rule, number or document body. The v1.13 revision record follows: **Revised:** 2026-11-04 (Prompt 10C alignment — the warfare workflow and acceptance companion [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md) is complete at the specification/documentation level (40 `WFW-` workflows, 60 `WFE-` edge cases, 124 `WFA-` tests, a 50-requirement bidirectional ledger, the D-143 failure-code-gap disclosure; all Designed, not executed), B-10 stays at v1.3 with its formula register v1.3 (30 sections, 188 numbered rules plus 42 lettered sub-rules, 39 formulas, 25 architecture decisions), the earlier 10B-C/10B-C2/10B-C3/10B-C4 passes remain verified (log §§59–§62), 10C is complete (log §63–§66), Prompt 11 is next and not started, and every number remains provisional pending Prompt 14. Earlier v1.12: Prompt 10B-C3/C4 alignment — B-10 at v1.3, 42 lettered sub-rules, 39 formulas, 25 architecture decisions; 10B-C/C2/C3 verified; 10C next. Earlier v1.11: Prompt 10B-C alignment — B-10 v1.1 with 38 lettered sub-rules; 10C next. Earlier v1.10: Prompt 10B alignment — B-10 drafted with 30 sections, 188 rules, 39 formulas and 25 architecture decisions; 10B complete, 10C next. Earlier v1.9: Prompt 10A alignment — the B-10 row links the [10A warfare research report](research/10A_politics_and_war_warfare_research.md), which is research/documentation only and approves no B-10 rule; at that time 10A was complete, 10B was next and not started, 10C was pending, and the B-10 filename stays `17_warfare_and_settlements.md`). Earlier v1.8: 09B acceptance alignment — B-09 is **ACCEPTED at the specification/documentation level** by D-142/DD-165; the 09C companion `16_alliances_workflows_acceptance.md` is complete at the specification/documentation level; the B-10–B-19 filename mapping is corrected to the verified sequence `17_`–`23_` with no file renamed; B-16–B-18 scope preserved. Earlier v1.7: Prompt 08A — **B-08 is researched, not drafted**: the row links [the 08A report](research/08A_diplomacy_research.md), records that no diplomacy rule exists, and notes that the planned `14_diplomacy.md` name is unavailable because `14_` is the 07C companion, so 08B confirms the next free prefix. Earlier v1.6: Prompt 07B — **B-07 is drafted and linked** with its formula register; the two-system scope, the directed foundation and the release-gated Global Trade are recorded, and the B-07 row is updated. Earlier Prompt 06B — B-06 foundation drafted and linked; earlier: Prompt 05 — B-05 drafted and linked with its formula register and research report; B-06…B-15's planned filenames renumbered by one because B-05 now occupies `11_`; the serial-prefix rule recorded. Earlier: v1.3 Prompt 04 — B-04 drafted and linked with its formula register and research report; B-05's planned filename released because `10_` is now B-04's; §5 current state recomputed. Earlier: v1.2 Prompt 03 — B-03 linked; v1.1 Prompt 02 — B-02 drafted and linked; document numbering corrected)
**Status:** Structural foundation. **No gameplay rules are defined in this document** — B-02's rules live in the document it links.
**Planned authoritative entry point:** `22_master_game_design_bible.md` — created in Prompt 15, which will index and link the subsystem documents below. Until then, this outline is the map; the subsystem documents are authoritative for whatever they have actually specified.

**Numbering note (revised 2026-10-24).** `00`–`06` are Prompt 01's frame (handoff, roadmap, this outline, requirements, design decisions, unresolved register, progress log). Prompt 02's brief fixed its specification at `07_…`; Prompt 03's landed at `09_…` because `08_…` is the [decision-closure audit](08_final_decision_closure_audit.md), so the shift is no longer strictly one place per prompt. The rule that survives is the numbering rule in §1: **one authoritative document per Bible part, whatever its filename**, with this outline and the progress log recording the real path. Future prompts confirm their own path before writing; no document is renamed to force a sequence.

**File numbering.** The two-digit prefix on a Stage 2 file is a **serial number in `docs/stage-2/`**, not the Bible part number. Prompts 01–04 consumed `01`–`10`; Prompt 05's rulebook and register took `11_`, so Prompt 06 starts at `12_`; the 2026-10-25 shift moved every then-planned later name by one. The current verified mapping for the remaining parts is `17_`–`23_` (see the 2026-11-03 note below and the table). A planned name in this table is fixed when its prompt starts, not before.

**Filename mapping correction (2026-11-03).** Verified against the files that actually exist: B-09 is [`16_alliances.md`](16_alliances.md), with its [formula register](16_alliances_formula_register.md), [integration contracts](16_alliances_integration_contracts.md) and the completed 09C companion `16_alliances_workflows_acceptance.md` (specification/documentation only). The companion shares the `16_` prefix exactly as the B-07 and B-08 companions share theirs, so the remaining planned names are **B-10 `17_warfare_and_settlements.md`**, **B-11 `18_world_events_and_progression.md`**, **B-12 `19_fair_play_and_player_protection.md`**, **B-13 `20_interface_and_player_journeys.md`**, **B-14 `21_formulas_and_balance.md`**, **B-15 and B-18 `22_master_game_design_bible.md`**, and **B-19 `23_stage_2_completion_report.md`**. No existing file is renamed; earlier references to the old `16_warfare…`–`22_stage_2…` planning names are historical, not current paths. B-16 and B-17 keep their existing mappings.

---

## 1. What the Bible is, and what it is not

The Bible is the single authoritative description of **how Nation Supremacy works**: the player loop, every system's rules, the formulas that resolve outcomes, the interactions between systems, and the player-facing behaviour those rules produce.

It is **not**:

- an implementation plan, schema, API design or test suite (Stages 4–8);
- proof that any rule is balanced (Prompt 14 labels values; playtesting proves them);
- a second research report (Stage 1 stays the evidence base);
- a place to promote an unapproved proposal (D-003, D-012).

**Authority rule.** One document is authoritative for each rule family; everything else links to it and never restates the rule in a competing form. When a later prompt changes a rule, it edits the authoritative document and records the change — it does not add a contradicting paragraph elsewhere.

**Incremental build.** Prompt 01 establishes this frame. Prompts 02–14 write one subsystem each. Prompt 15 assembles the entry point and performs one bounded consistency review. The outline is therefore mostly **Planned**, and that is the correct state.

---

## 2. Required structure at completion

The finished Bible contains nineteen parts. Each part has a stable ID (`B-01`…`B-19`), a purpose, its authoritative document, the Stage 2 prompt that writes it, and a status.

Status vocabulary: **Planned** (not written) · **Draft** (written, unreviewed) · **Reviewed** (cross-checked against dependencies) · **Complete** (accepted for this stage). "Complete" never means implemented.

### B-01 — Game identity and design philosophy

| Field | Value |
|---|---|
| Purpose | State what the game is, for whom, and which design laws every later rule must obey |
| Content | Premise; intended player experience; strategic pillars DP-001…006; anti-pillars AP-001…008; intended audience and session shape; originality principles; symbolic-world concept; design boundaries; non-goals and prohibited assumptions |
| Authoritative document | `22_master_game_design_bible.md` Part I (created in Prompt 15), consolidating [Report 04](../stage-1/04_target_audience_and_player_experience.md) and [Report 05](../stage-1/05_core_game_concept_and_design_pillars.md) |
| Prompt | 15 (consolidation); source material already exists |
| Prerequisites | None |
| Validation | Every later section cites the pillars it serves; no rule contradicts an anti-pillar |
| Status | **Planned** — source material available |

### B-02 — Core gameplay loop and turn system

| Field | Value |
|---|---|
| Purpose | Define what a player does in a session and how the shared world advances |
| Content | Session shape; core loop (observe → decide → commit → boundary → digest → revise); symbolic-world model; 2-hour UTC schedule and slot arithmetic; boundary semantics; lifecycle and P0–P7 phases; action lifecycle and failure codes; deterministic ordering and tiebreaks; reservation; recovery; inactive-player behaviour; reports and history; subsystem contract |
| Authoritative document | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](07_core_gameplay_loop_symbolic_world_and_turn_system.md) |
| Prompt | 02 |
| Prerequisites | B-01 |
| Validation | Two readers compute the same state for one boundary; no rule requires presence; a reader can name the phase and ordering band of any action |
| Status | **Draft** — written 2026-10-23, not yet cross-reviewed by later subsystem prompts |

### B-03 — Accounts, nation creation and progression

| Field | Value |
|---|---|
| Purpose | Define the journey from first visit to a functioning, growing nation |
| Content | Account-to-nation relationship; one-account-per-person policy; shared-network interaction restrictions and their review/appeal route; registration and onboarding; nation identity and naming; standard starting conditions; progression milestones; instant reroll and its reset boundary; inactivity, abandonment and re-entry; account lifecycle, security and recovery; data classes and retention for the account boundary |
| Authoritative document | [`09_account_onboarding_nation_creation_and_progression.md`](09_account_onboarding_nation_creation_and_progression.md) — the Stage 2 register's original filename `08_nation_creation_and_progression.md` was unusable because `08` is the decision-closure audit |
| Prompt | 03 |
| Prerequisites | B-02 |
| Validation | A first-time player can found a nation and know what to do next without external help; a pair on one network is restricted without being accused; a reroll is permanent, immediate and does not reset account sanctions |
| Status | **Draft** — written 2026-10-24; no rule implemented or tested |

### B-04 — Economy, treasury and resources

| Field | Value |
|---|---|
| Purpose | Define money, materials, production, consumption, shortage and the accounting that constrains every value change |
| Content | The fixed 11-resource roster with a lifecycle profile per resource; extraction, power, recipes and standing production policy; food demand and the hunger penalty; the crown, income, operating expense, capital expenditure, cash flow, wealth and the no-debt austerity order; one shared warehouse and reservations; economic action states; the P3 two-hour settlement order and recovery; the append-only ledger and corrections; reporting and forecasts; balance targets; reroll economics; the cross-system contracts |
| Authoritative document | [`10_economy_resources_treasury_and_finances.md`](10_economy_resources_treasury_and_finances.md); every formula, constant and worked-example index in [`10_economic_formula_and_balance_register.md`](10_economic_formula_and_balance_register.md); evidence in [`research/04_politics_and_war_economy_research.md`](research/04_politics_and_war_economy_research.md) |
| Prompt | 04 |
| Prerequisites | B-02 (boundary timing, reservations, P3), B-03 (starting state, reroll) |
| Validation | Every resource has a source, a sink, a storage rule and a shortage rule; the balance and inventory identities hold in the 20 worked examples; a duplicate settlement writes nothing; a reroll destroys everything and grants only the standard bundle |
| Status | **Draft** — written 2026-10-24; 20 worked examples checked by recomputation; no rule implemented or runtime-tested |

### B-05 — Cities, infrastructure, production and research

| Field | Value |
|---|---|
| Purpose | Define what a city is in a mapless world and how nations convert crowns and materials into durable productive capacity |
| Content | The non-geographic city and its lifecycle; one capital, twelve cities and the no-deletion rule; founding prerequisites and cost; infrastructure, capacity and housing; the weighted development-capacity model and per-city limits; the closed 17-type building catalogue with costs, DC, limits, upkeep and demolition; construction, cancellation and the single construction slot; power plants on B-04's grid; the seven extraction and four processing facilities; the twelve-technology research tree, modifier classes and caps; the four branch-capstone programmes; P4 timing, reservation, capex and book value; the housing and research contracts with Prompts 06–15 |
| Authoritative document | [`11_cities_infrastructure_production_and_research.md`](11_cities_infrastructure_production_and_research.md); every formula, constant and worked-example index in [`11_city_infrastructure_production_and_research_formula_register.md`](11_city_infrastructure_production_and_research_formula_register.md); evidence in [`research/05_politics_and_war_city_infrastructure_production_research.md`](research/05_politics_and_war_city_infrastructure_production_research.md) |
| Prompt | 05 |
| Prerequisites | B-04 (capacity vector, batches, grid, recipes, capex, ledger), B-02 (phases, ordering, exactly-once), B-03 (starting state, reroll) |
| Validation | Every facility has a cost, a DC footprint, a limit, an input, an output and an upkeep; capacity never exceeds the formula; all 11 resources have a production path consistent with B-04; 20 worked examples recomputed by `qa_backups/verify_city_numbers.py`; a repeated settlement grants nothing twice; no map, land or coordinates anywhere |
| Status | **Draft** (v1.5) — written 2026-10-25; v1.2 corrected three internal references, two counts (17 building types, 12 technologies) and one dead requirement citation; v1.3 states the opening treasury in Example 3 and marks Example 1 as the founding balance; v1.4 is the independent-review reconciliation (stepped infrastructure cost with a 16,170 maximum, basis-point discounts with one source per cost, one research-assignment rule, total/reserved/available balances, Example 12 funded, URB-014 → D-015); v1.5 fixes F-CI-021's Example 15B citation and states `planned_batches = M + A ≤ capacity` with B-04; 20 worked examples checked by recomputation; no rule implemented or runtime-tested |

### B-06 — Population and domestic politics

| Field | Value |
|---|---|
| Purpose | Define the internal society that constrains economic and military choices |
| Content | Population model; public sentiment; government forms; policies (max two axes at first playable); stability and legitimacy; political progression; leadership changes if approved; consequences and risks |
| Authoritative document | [`12_population_and_domestic_politics.md`](12_population_and_domestic_politics.md) (rulebook, Part I + Part II); every formula is in [`12_population_and_domestic_politics_formula_register.md`](12_population_and_domestic_politics_formula_register.md) |
| Research | [`research/06_politics_and_war_domestic_politics_elections_and_policy_research.md`](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md) |
| Prompt | 06A (foundation) and 06B (elections, campaigns, retention, crises, unrest) |
| Prerequisites | B-04, B-05 |
| Delivered by 06A | National population with housing cap and crowding decay; six fixed constituencies; approval, stability and derived legitimacy; six permanent governments with five channels; two policy axes; the political state and P3.8 settlement; 06B interfaces; 18 worked examples |
| Delivered by 06B | The 240-turn per-nation election cycle and its five dates; the two simulated challengers; the three campaign actions; the turnout-weighted vote and the tie-break; the confidence motion; the 12-turn transition; the five continuous retention tests; the 18-turn crisis; the 12-turn recovery; the six-state machine; the P4.4 settlement; 31 worked examples E19–E49 |
| Validation | Every policy has a visible trade-off; stability is a floor, not a success ladder; no government is economically dominant; every support term is attributable |
| Status | **Draft** (2026-10-25, Part I + Part II) — accepted at the documentation level; no rule implemented or runtime-tested |

### B-07 — Trade and markets

| Field | Value |
|---|---|
| Purpose | Define how nations exchange resources without breaking conservation or fairness |
| Content | Two systems: directed trades (first playable, fee-free, no reservation at creation, atomic P4 settlement) and Global Trade (required long-term, release-gated public sell listings and buy offers, reservation at posting, taker-selected posted price, partial fills); offer/revision/accept/decline/cancel/expire lifecycle; integer pricing and reference values; fair-value band and fresh-nation protection; declared limits; privacy and personal history; post-gate statistics with k = 5; manipulation signals; the G-1…G-6 gate and its unmet status |
| Authoritative document | [`13_trade_and_markets.md`](13_trade_and_markets.md) and [`13_trade_and_markets_formula_register.md`](13_trade_and_markets_formula_register.md) |
| Prompt | 07A (research), 07B (foundations), 07C (workflows and acceptance) |
| Prerequisites | B-02 (turn, phases, reservations), B-03 (account, nation and pair states), B-04 (resources, treasury, ledger, warehouse), B-05 (storage capacity), B-06 (leadership state) |
| Validation | Both legs commit or neither; a directed offer cannot be partially filled; a public listing's partial fills are independent executions; decline is free; 35 failure cases and 21 examples reconcile; the gate is recorded as unmet |
| Status | **Designed** (07A/07B/07C complete; 07C companion accepted); **release-gated** for Global Trade; not implemented |

### B-08 — Diplomacy

| Field | Value |
|---|---|
| Purpose | Define relations between nations without geographic borders |
| Content | Relationship types; treaties and lifecycle; negotiation; sanctions; diplomatic actions; breach and termination; consequences and reputation routing; 3–5 worked interactions |
| Authoritative document | [`15_diplomacy.md`](15_diplomacy.md) — B-08, 22 sections, **v1.2**, **Draft** (designed; not implemented, not reviewed); every formula is in [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md) (`F-DP-001`…`F-DP-012`). Workflows and acceptance: [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md). Research: [`research/08A_diplomacy_research.md`](research/08A_diplomacy_research.md) |
| Prompt | 08A (research, complete), 08B (foundations, **complete 2026-10-30**), 08C (workflows and acceptance, **complete 2026-10-30, corrected by 08C-C, 08C-D and 08C-E**) |
| Prerequisites | B-02, B-03, B-04, B-06, B-07 |
| Validation | Every diplomatic state is reachable, exitable and visible to both parties; every action has one owner, one consent rule and one failure code |
| Status | **Draft** (08B and 08C complete 2026-10-30; 08C-C, 08C-D and 08C-E corrected the acceptance traceability, privacy, replay and bidirectional requirement evidence the same day; 88 tests, 52 covered / 2 partial edge cases, 101 direct + 16 supporting + 1 deferred relationship, both residual edge cases Prompt 12 dependencies); no implementation, no runtime test, no release approval. UD-013/UD-033 resolved; UD-039 resolved by D-137 for B-08 (no alliance-level treaty object in the national system; zero diplomatic delegation), amended in part by D-140 for the separate B-09 Alliance-to-Alliance object |

### B-09 — Alliances and alliance management

| Field | Value |
|---|---|
| Purpose | Define player-created collective organisations and their governance |
| Content | Formation and membership; player-defined leadership, permissions and governance; shared pool policy or explicit exclusion; alliance diplomacy; Alliance coordination and a restricted Alliance management interface — **not a war room**, with no military command, no member OP spending and no shared pool; succession — all inside an open-ended, player-authored constitutional model (D-135 / DD-151) |
| Authoritative document | [`16_alliances.md`](16_alliances.md) (the planned `15_alliances.md` moves one prefix because `15_` is B-08; no existing file is renamed), with [formula register](16_alliances_formula_register.md) and [integration contracts](16_alliances_integration_contracts.md); workflows and acceptance companion **completed by Prompt 09C**: `16_alliances_workflows_acceptance.md` (specification/documentation only) |
| Prompt | 09 (09A research, 09B specification/documentation, 09C workflow/acceptance companion); **09C complete at the specification/documentation level; Prompt 10A research complete; Prompt 10B complete at the specification/documentation level (§58; corrections 10B-C §59, 10B-C2 §60, 10B-C3 §61 and 10B-C4 §62); Prompt 10C complete at the specification/documentation level (2026-11-04; §63–§66, including the 10C-C3 validator-integrity correction); **Prompt 11A research is complete (2026-11-05; log §67), Prompt 11B is complete at the system-specification level (2026-11-05; log §68), and Prompt 11C is next** |
| Prerequisites | B-07, B-08; must read [B-08 §18](15_diplomacy.md) for the treaty object, authority, membership-change and visibility contracts, and respect **UD-039**, decided by D-137 and amended in part by D-140 (a separate B-09 Alliance-to-Alliance treaty object, zero delegation) |
| Validation | Every permission and every pool draw is authorised and audited; membership never mandatory |
| Status | **ACCEPTED — specification/documentation level (D-142 / DD-165, 2026-11-03).** 09A accepted after Prompt 09A-F; 09B corrected through 09B-P, including 09B-I (ALL-093 withdrawal, Alliance treaties, NAP enforcement and the same-Alliance attack ban), 09B-J (automatic per-turn production taxation, player-authored 0–100% asset-specific rates, role-governed policy freeze, a credit-only receiving ledger under an Open UD-046, non-covered NAP membership and C25 plain-modal completion), 09B-K (positive appeal-grant semantics, ALF-21/23/24 cleanup, credit-only ARL wording, an ambiguous-membership 0% safeguard under Open UD-040 and post-tax production-chain accounting), 09B-L (taxation/ARL/operational-funding consolidation and the narrow UD-045 authorization), 09B-M (fail/review/safe C25 gate), 09B-N (recourse wording and former-people labels), 09B-O (bounded procedural-domain gate) and 09B-P (ambiguous dismissal and grievance review routing). Acceptance does **not** mean production implementation, live-game integration testing or release, and resolves no `UD-040`–`UD-049`; Prompt 09C is complete at the specification/documentation level (2026-11-03; log §53); Prompt 10A research is complete (research/documentation only; log §56); Prompt 10B is complete at the specification/documentation level (log §58); Prompt 10C is complete at the specification/documentation level (2026-11-04; log §63–§66); Prompt 11 is next and has not started. ([§32](06_stage_2_progress_log.md)–[§36](06_stage_2_progress_log.md), [§37]–[§52], [§58](06_stage_2_progress_log.md)) |

### B-10 — Warfare, campaigns and postwar settlements

| Field | Value |
|---|---|
| Purpose | Make conflict strategically meaningful without a map |
| Content | War lifecycle; readiness and military costs; campaign objectives and operation types; supply; battle-resolution model; losses and counterplay; victory conditions; ceasefire and settlement; war-abuse prevention |
| Authoritative document | [`17_warfare_and_settlements.md`](17_warfare_and_settlements.md) with its [formula register](17_warfare_formula_register.md) and the [10C workflows and acceptance companion](17_warfare_workflows_acceptance.md) — B-10 is drafted; documentation only |
| Research evidence | [10A Politics and War warfare research](research/10A_politics_and_war_warfare_research.md) — research/documentation only; records the P&W source register, mechanics catalogue, mapless suitability analysis, cross-system integration matrix and candidate requirements, **approves no B-10 rule or number**, and leaves **UD-032 Open** |
| Prompt | 10 (10A research, 10B specification, 10C workflow/acceptance companion); **10A research complete (2026-11-03; research/documentation only); 10B specification complete (2026-11-03; §58) with corrections 10B-C/10B-C2/10B-C3/10B-C4 complete (2026-11-04; §§59–§62); 10C complete at the specification/documentation level (2026-11-04; §63–§66)** |
| Prerequisites | B-04, B-06, B-08, B-09; the OP model is approved by D-015 (cap, costs and scaling provisional) |
| Validation | Two nations can fight a bounded war with a readable result, an off-ramp and no infinite one-sided attrition |
| Status | **DRAFT — specification complete (v1.3, 2026-11-04), not implemented.** 188 numbered `WAR-` rules plus 42 lettered sub-rules, 39 formulas and 25 architecture decisions; 10B-C2 closes the Food, force-snapshot, political-defensive, infrastructure-accounting, repair-cost/timing and crowding defects; Prompt 10C adds the workflow and acceptance layer (40 `WFW-` workflows, 60 `WFE-` edge cases, 124 `WFA-` tests, a 50-requirement ledger; all **Designed, not executed**); every number is provisional pending Prompt 14; `UD-032` resolved as Option A; `UD-040`–`UD-049` remain Open |

### B-11 — World events, objectives, rankings and long-term progression

| Field | Value |
|---|---|
| Purpose | Keep the shared world interesting over months without a content team |
| Content | Strategic objectives; systemic world events and their timing relative to the boundary; achievements; plural rankings; world chronicle; long-term progression; endgame/seasonal concepts if any |
| Authoritative document | [B-11](18_world_events_objectives_rankings_progression.md) (**v1.0, drafted 2026-11-05**) with its [formula register](18_world_events_objectives_rankings_progression_formula_register.md) and [52-gate acceptance crosswalk](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md); D-152 confirms the canonical path |
| Research evidence | [11A world events, objectives, rankings and progression research](research/11A_world_events_objectives_rankings_progression_research.md) (35 sections) with [the comparator source and benchmark register](research/11A_comparator_sources_and_benchmarks.md) (114 `11A-RS` source rows, 73 `11A-BM` benchmark-mechanic entries, 7 games, Politics & War primary) and [the integration and risk registers](research/11A_integration_and_risk_registers.md) (40 `11A-INT` rows, `V-01`…`V-18` owning-rule violations, 28 `11A-RK` risks, 30 `11A-CR` candidate requirements, 16 `11A-OPEN` questions) plus 34 `11A-DR` recommendations — research/documentation only; **approves no B-11 rule, formula, number or implementation** and leaves **`UD-024` Deferred** with its bar on 11B |
<<<<<<< HEAD
| Prompt | 11 (11A research and design foundations, 11B specification, 11C workflow/acceptance companion); **11A complete (2026-11-05; §67); 11B COMPLETE at the system-specification level (2026-11-05; §68); 11B-C correction complete (2026-11-05; §69; 52/52 acceptance gates PASS); 11C complete (2026-11-06; §72); 12A complete at the research/design-foundations level (2026-11-06; §73) and reconciled by the 12A-C1 pass (2026-11-07; §74); 12B next and not started** |
=======
| Prompt | 11 (11A research and design foundations, 11B specification, 11C workflow/acceptance companion); **11A complete (2026-11-05; §67); 11B COMPLETE at the system-specification level (2026-11-05; §68); 11B-C correction complete (2026-11-05; §69; 52/52 acceptance gates PASS); 11C complete (2026-11-06; §72); 12A complete at the research/design-foundations level (2026-11-06; §73); 12B next and not started** |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
| Prerequisites | B-02, B-04, B-10 |
| Validation | Returning players can see what changed and why; no single dominant ladder |
| Status | **DRAFT — specification complete at the documentation level (v1.0, 2026-11-05), not implemented.** 723 `WEP-` rules in 29 sections, 50 `F-WEP-` formulas, 17 `WPC-` contracts, 40 `WPF-` codes, 50 `WPA-` events; 60 requirements REQ-704–763; D-152–D-161 / DD-200–DD-209; UD-024 resolved, UD-050/UD-051 open; unapproved calibration parameters remain provisional for Prompt 14, while structural formulas and inherited approved constants retain their documented status. The 11A foundation follows for history: **research complete (Prompt 11A, 2026-11-05)**. 11A supplies the benchmark evidence, the integration matrix, the anti-exploit register, four evaluated alternative sets with a recommended direction per area, and eight design directions **D-144…D-151 / DD-192…DD-199** — including the fixed intra-P6 order that answers the ordering question B-02 delegated to Prompt 11 (`TR-042`, band **B4**, `TR-055`). B-11 is specified in this document; no gameplay code, calibration, deployment or release exists. `AP-003`, `AP-005`, `AP-008`, `FO-024` (Rejected), `FO-020` (Deferred), `SYS-014`, `SYS-015`, `D-021`, `D-027`, `D-028` and the Global Trade gate state are preserved unchanged. |

### B-12 — Fair play, player protection, privacy and administration

| Field | Value |
|---|---|
| Purpose | Turn trust principles into explicit, enforceable-in-policy rules |
| Content | One-account-per-person policy; new-player protection; abuse reporting; moderation workflow; administrative authority and audit; botting/collusion policy; privacy-conscious enforcement; sanctions and appeals |
<<<<<<< HEAD
| Authoritative document | [20_fair_play_and_player_protection.md](20_fair_play_and_player_protection.md) (**v1.0, Prompt 12B, 2026-11-07**) with its [formula and parameter register](20_fair_play_and_player_protection_formula_register.md), [requirement register](20_fair_play_and_player_protection_requirements.md) and [acceptance framework](20_fair_play_and_player_protection_acceptance.md); `19_` remains occupied by the Prompt 11C companion |
| Prompt | 12 (12A research, 12B specification, 12C workflows/acceptance); **12A complete (2026-11-06; §§73–74); 12B specification complete at the documentation level (2026-11-07; §75); 12C next and not started, subject to separate owner authorization** |
| Prerequisites | B-03, B-07, B-09, B-10 |
| Validation | Each prohibited behaviour has a rule, a consequence and an evidence source; no claimed detection capability |
| Status | **DRAFT — specification complete at the documentation level (v1.0, 2026-11-07), not implemented.** 344 `FP/EVD/MA/CO/EX/PRV/MOD/ADM/COR/SEC/INT/FR/GOV` rules, 16 violation classes, 9 privacy classes, 8 actors, 8 roles, 15 failure postures, 16 formulas with 12 uncalibrated parameters, 106 requirements `REQ-764`–`REQ-869` (86 Provisional / 20 Open), D-178…D-187 / DD-226…DD-235 and UD-052…UD-060; validator 62 checks with 12/12 positive and 22/22 negative fixtures; acceptance 23 PASS / 3 PARTIAL. **No migration, grant, RLS policy, audit trigger, application enforcement or gameplay change exists; the prototype `profiles` grant and missing audit protection are disclosed, not fixed. Prompt 12C is not authorized.** |
=======
| Authoritative document | `20_fair_play_and_player_protection.md` — **reserved by D-163 / DD-211 for Prompt 12B and not yet created**; `19_` is occupied by the Prompt 11C companion |
| Prompt | 12 |
| Prerequisites | B-03, B-07, B-09, B-10 |
| Validation | Each prohibited behaviour has a rule, a consequence and an evidence source; no claimed detection capability |
| Status | **Design foundations complete (Prompt 12A, 2026-11-06; log §73)** — 152 source rows, 40 benchmark mechanics, 106 candidate requirements, 30 dependency rows, 32 threat rows, 15 failure postures, D-163…D-177 / DD-211…DD-225 and UD-052…UD-060. **No rule, penalty, permission, workflow or schema is written; the rulebook is Prompt 12B.** |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

### B-13 — Interface and player journeys

| Field | Value |
|---|---|
| Purpose | Specify how players see and act on the rules |
| Content | Screen inventory; navigation; National Command Center; economy/production; politics; trade; diplomacy; restricted Alliance management interface (**not a war room**); Nation-owner War Operations Board (nation-level, owner-only, B-10 visibility); notifications and event feed; onboarding and recovery journeys; accessibility and usability |
| Authoritative document | `20_interface_and_player_journeys.md` |
| Prompt | 13 |
| Prerequisites | B-02…B-12 (rules must exist to be displayed) |
| Validation | Every rule has a screen or surface; a new player completes the first session unassisted on paper |
| Status | **Planned** |

### B-14 — Formulas, numerical rules and balance

| Field | Value |
|---|---|
| Purpose | Make the rules computable and expose their failure modes |
| Content | Formula register with units/rounding/timing; starting values; costs and rewards; caps and minimums; representative turn calculations; cross-system interactions; edge cases; exploit scenarios; values awaiting testing |
| Authoritative document | `21_formulas_and_balance.md` |
| Prompt | 14 |
| Prerequisites | B-02…B-13 |
| Validation | A sample nation's turn is computable by hand; every value carries an approval label |
| Status | **Planned** |

### B-15 — Cross-system interactions

| Field | Value |
|---|---|
| Purpose | State how systems constrain and feed each other, so no rule is designed in isolation |
| Content | Interaction matrix; coupling rules; ordered resolution dependencies; known feedback loops; anti-cascade rules; the four load-bearing couplings (economy↔specialisation, acts/treaties↔reputation, conflict↔everything, transparency↔journal) |
| Authoritative document | `22_master_game_design_bible.md` Part XV (matrix assembled in Prompt 15 from INT-001…014 and each subsystem's dependency list) |
| Prompt | 15 (assembly); each prompt registers its own edges |
| Prerequisites | B-02…B-14 |
| Validation | Every edge is declared by both sides; no cycle without a stated resolution order |
| Status | **Planned** |

### B-16 — Requirements, decisions and traceability

| Field | Value |
|---|---|
| Purpose | Keep every requirement traceable and every decision honest |
| Content | Requirement IDs and sources; status; design coverage; dependencies; validation approach; unresolved questions; supersession history |
| Authoritative document | [`03_requirements_traceability.md`](03_requirements_traceability.md), with [`04_approved_and_provisional_decisions.md`](04_approved_and_provisional_decisions.md) and [`05_unresolved_design_decisions.md`](05_unresolved_design_decisions.md) |
| Prompt | 01, maintained through 15 |
| Prerequisites | None |
| Validation | IDs unique; every requirement has a source, a section and a prompt; no approval invented |
| Status | **Draft** — created this prompt |

### B-17 — Unresolved questions and carry-forward risks

| Field | Value |
|---|---|
| Purpose | Keep open questions visible and classified instead of silently resolved |
| Content | Blocking design decisions; provisional choices; playtest/simulation items; implementation details; accepted carry-forward risks |
| Authoritative document | [`05_unresolved_design_decisions.md`](05_unresolved_design_decisions.md) |
| Prompt | 01, maintained through 15 |
| Prerequisites | None |
| Validation | Every item has an ID, a blocking class, an owner and a responsible prompt |
| Status | **Draft** — created this prompt |

### B-18 — Revision and change control

| Field | Value |
|---|---|
| Purpose | Define how the Bible is edited so history is never silently rewritten |
| Content | Document ownership; update conventions; decision references; status transitions; cross-reference rules; revision history; conflict resolution between older notes and approved records |
| Authoritative document | `22_master_game_design_bible.md` Part XVIII, with this outline's §3 |
| Prompt | 15 |
| Prerequisites | B-16, B-17 |
| Validation | A change to any rule can be traced to a decision or a prompt record |
| Status | **Planned** |

### B-19 — Completion and acceptance criteria

| Field | Value |
|---|---|
| Purpose | State what "Stage 2 complete" means, and what it does not |
| Content | The bounded completion rule from the Stage 2 register; required coverage; consistency requirements; what may remain provisional; what must be deferred to testing or implementation |
| Authoritative document | `23_stage_2_completion_report.md` (decision) and [`01_stage_2_prompt_roadmap.md`](01_stage_2_prompt_roadmap.md) §3 Prompt 15 (rule) |
| Prompt | 15 |
| Prerequisites | B-01…B-18 |
| Validation | Every completion criterion is either met or explicitly carried forward with an owner |
| Status | **Draft** — the rule exists; the acceptance record does not |

---

## 3. Change control (applies from this prompt onward)

1. **One authority per rule family.** New material goes into the owning document; other documents link.
2. **No silent approval.** A rule may be *Provisional* or *Approved*; only [DECISIONS.md](../DECISIONS.md) can record the latter. Under [the autonomous policy](../AUTONOMOUS_DECISION_POLICY.md) (D-014) an AI may record a *design* approval there for an ordinary decision, citing its evidence; fixed constraints still require the owner, and no prompt may approve its own output by declaring it.
3. **Status transitions** are recorded in the document header and in [`06_stage_2_progress_log.md`](06_stage_2_progress_log.md): Planned → Draft → Reviewed → Complete. A later prompt may reopen a *Reviewed* document if it finds a contradiction; it must say which rule and why.
4. **Supersession, not deletion.** A replaced rule keeps its history, marked *Superseded by …*.
5. **Conflict resolution order:** approved owner decision → Stage 2 register entry → the owning subsystem document → Stage 1 report → proposal. If two documents at the same level disagree, the later prompt must resolve it explicitly and record the resolution; it may not pick silently.
6. **No fabricated evidence.** "Designed" ≠ "tested"; "formula present" ≠ "balanced"; "policy stated" ≠ "enforced".

---

## 4. Assembly plan for Prompt 15

1. Verify every B-section is at least **Reviewed**, or record why it is not.
2. Create `22_master_game_design_bible.md` as the single entry point: Part I–XIX summaries, each linking to its authoritative document; no rule duplicated.
3. Compile the cross-system interaction matrix (B-15) from the edges each prompt registered.
4. Re-run traceability: every REQ has coverage or a named gap; every UD has a disposition.
5. Run one bounded consistency review — not a new audit series.
6. Record the Stage 2 decision in `23_stage_2_completion_report.md` and update continuity.

---

## 5. Current state

| Item | State |
|---|---|
| Bible entry point | **Does not exist yet** — planned for Prompt 15; the Bible is not assembled |
| Sections planned | 19 |
| Sections drafted | 10 (B-02, B-03, B-04, B-05, B-06, B-08, B-09, B-16, B-17, and B-19's completion rule) — B-09 is **ACCEPTED at the specification/documentation level (D-142 / DD-165)**; the others remain Draft, not Reviewed |
| Sections with gameplay rules | **7** (B-02, B-03, B-04, B-05, B-06, B-08 and B-09; all rules provisional or design-confirmed, none implemented or tested) |
| Authoritative document | [12_population_and_domestic_politics.md](12_population_and_domestic_politics.md) — B-06, 38 sections in two parts, Draft (**v2.5**, five micro-correcting passes, the cross-document reconciliation and the publication/catch-up correction on 2026-10-28), with [formula register v2.4](12_population_and_domestic_politics_formula_register.md) (F-PD-001…F-PD-044) |
| Authoritative Prompt 03 specification | [09_account_onboarding_nation_creation_and_progression.md](09_account_onboarding_nation_creation_and_progression.md) — B-03, 22 sections, Draft |
| Authoritative Prompt 04 specification | [10_economy_resources_treasury_and_finances.md](10_economy_resources_treasury_and_finances.md) — B-04, 25 sections, Draft, with [formula register](10_economic_formula_and_balance_register.md) |
| Authoritative Prompt 05 specification | [11_cities_infrastructure_production_and_research.md](11_cities_infrastructure_production_and_research.md) — B-05, 26 sections, Draft (v1.5), with [formula register v1.2](11_city_infrastructure_production_and_research_formula_register.md) |
<<<<<<< HEAD
| Prompts executed | Stage 2, Prompts 01–07, 08A–08C, 09A–09B, 09C, 10A–10C, 11A–11C, 12A (07A/07B 2026-10-28; 07C and 08A 2026-10-29; 08B and 08C 2026-10-30; 09A accepted 2026-10-31; 09B corrected 2026-11-01 through 09B-P on 2026-11-03, **accepted at the specification/documentation level by D-142 / DD-165 on 2026-11-03**; 09C completed at the specification/documentation level on 2026-11-03, log §53; 10A warfare research completed 2026-11-03, research/documentation only, log §56; 10B warfare specification completed 2026-11-03, documentation only, log §58, with correction passes 10B-C, 10B-C2, 10B-C3 and 10B-C4 completed and verified 2026-11-04, log §§59–§62, B-10 v1.3; **10C warfare workflows and acceptance completed at the specification/documentation level on 2026-11-04, log §63–§66**); 11A–11C completed at the research/design-foundations and specification/documentation levels (log §§67–§72); 12A completed at the research/design-foundations level on 2026-11-06 (log §73) and reconciled by the 12A-C1 pass on 2026-11-07 (log §74); the [decision-closure audit](08_final_decision_closure_audit.md) is a separate audit record, not a prompt |
| Next prompt | **Prompt 12A — the B-12 research and design foundations — is **complete** (log §73) and reconciled by the 12A-C1 pass (2026-11-07; log §74); **Prompt 12B — B-12 rulebook, formula register, requirement register and acceptance framework — is complete at the specification/documentation level (2026-11-07; log §75); Prompt 12C is next in the roadmap, not started, and needs explicit owner authorization.**** **Prompt 11C is complete at the specification/documentation level (2026-11-06; log §72)** with [the B-11 workflows and acceptance companion](19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md). **Prompt 11B (the B-11 specification) is complete at the system-specification level (2026-11-05; log §68) and B-11 is drafted at v1.0; Prompt 11A (research, benchmarking and design foundations) was complete at the research/design-foundations level (2026-11-05; log §67).** Prompt 10C is complete at the specification/documentation level (2026-11-04; log §63–§66; canonical deliverable [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md)); Prompt 10B is complete at the specification/documentation level (2026-11-03; log §58), with its correction passes 10B-C, 10B-C2, 10B-C3 and 10B-C4 complete and verified (2026-11-04; log §§59–§62; [B-10](17_warfare_and_settlements.md) v1.3); Prompt 10A research is complete (research/documentation only; log §56); Prompt 09C is complete at the specification/documentation level (2026-11-03; log §53). The 09C canonical deliverable is `16_alliances_workflows_acceptance.md`. Production implementation, integration testing and release remain pending for all specified systems. |
| Bible status | **Incomplete by design** — 6 sections remain Planned (B-01, B-12, B-13, B-14, B-15 and B-18); B-09 is **ACCEPTED at the specification/documentation level**; B-11 is **drafted at v1.0 (specification complete, not implemented)**; B-10 is **drafted at the specification/documentation level (v1.3, not implemented)** with its Prompt 10C workflow/acceptance companion complete; Prompts 09C, 10A–10C and 11A–11C are complete at the specification/documentation level, Prompt 12A is complete at the research/design-foundations level (log §73) and reconciled by the 12A-C1 pass (log §74), and Prompts 12B–15 are pending; no section is reviewed or assembled |
=======
| Prompts executed | Stage 2, Prompts 01–07, 08A–08C, 09A–09B, 09C, 10A–10C, 11A–11C, 12A (07A/07B 2026-10-28; 07C and 08A 2026-10-29; 08B and 08C 2026-10-30; 09A accepted 2026-10-31; 09B corrected 2026-11-01 through 09B-P on 2026-11-03, **accepted at the specification/documentation level by D-142 / DD-165 on 2026-11-03**; 09C completed at the specification/documentation level on 2026-11-03, log §53; 10A warfare research completed 2026-11-03, research/documentation only, log §56; 10B warfare specification completed 2026-11-03, documentation only, log §58, with correction passes 10B-C, 10B-C2, 10B-C3 and 10B-C4 completed and verified 2026-11-04, log §§59–§62, B-10 v1.3; **10C warfare workflows and acceptance completed at the specification/documentation level on 2026-11-04, log §63–§66**); the [decision-closure audit](08_final_decision_closure_audit.md) is a separate audit record, not a prompt |
| Next prompt | **Prompt 12A — the B-12 research and design foundations — is **complete** (log §73) and **Prompt 12B — the B-12 rulebook and formula register — is next in the roadmap, not started, and needs explicit owner authorization.**** **Prompt 11C is complete at the specification/documentation level (2026-11-06; log §72)** with [the B-11 workflows and acceptance companion](19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md). **Prompt 11B (the B-11 specification) is complete at the system-specification level (2026-11-05; log §68) and B-11 is drafted at v1.0; Prompt 11A (research, benchmarking and design foundations) was complete at the research/design-foundations level (2026-11-05; log §67).** Prompt 10C is complete at the specification/documentation level (2026-11-04; log §63–§66; canonical deliverable [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md)); Prompt 10B is complete at the specification/documentation level (2026-11-03; log §58), with its correction passes 10B-C, 10B-C2, 10B-C3 and 10B-C4 complete and verified (2026-11-04; log §§59–§62; [B-10](17_warfare_and_settlements.md) v1.3); Prompt 10A research is complete (research/documentation only; log §56); Prompt 09C is complete at the specification/documentation level (2026-11-03; log §53). The 09C canonical deliverable is `16_alliances_workflows_acceptance.md`. Production implementation, integration testing and release remain pending for all specified systems. |
| Bible status | **Incomplete by design** — 6 sections remain Planned (B-01, B-12, B-13, B-14, B-15 and B-18); B-09 is **ACCEPTED at the specification/documentation level**; B-11 is **drafted at v1.0 (specification complete, not implemented)**; B-10 is **drafted at the specification/documentation level (v1.3, not implemented)** with its Prompt 10C workflow/acceptance companion complete; Prompts 09C, 10A–10C and 11A–11C are complete at the specification/documentation level, Prompt 12A is complete at the research/design-foundations level, and Prompts 12B–15 are pending; no section is reviewed or assembled |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

This outline defines no gameplay rule of its own. Approved inputs are the project constraints in [AI_CONTEXT.md](../AI_CONTEXT.md) §2 and the confirmed decisions D-001…D-142; where a decision records a design approval, its numeric parameters stay provisional as the decision states. B-02…B-06 and B-08 remain Draft until a later prompt reviews them; B-09 is accepted at the specification/documentation level only; none of their rules is implemented or tested.
