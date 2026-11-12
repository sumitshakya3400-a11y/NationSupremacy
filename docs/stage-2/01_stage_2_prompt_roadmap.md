# Stage 2 prompt roadmap — Master Game Design Bible

> **09B acceptance status (2026-11-03):** **Phase 09B Alliance specification and documentation: ACCEPTED.** Recorded by **D-142** (specification/documentation level) and **DD-165**; the independent review findings were applied by 09B-N, 09B-O and 09B-P. Acceptance is **not** production implementation, live-game integration testing or release, and it is **not** a new owner authorization: `UD-040`–`UD-049` remain Open or Deferred exactly as recorded in the [05 register](05_unresolved_design_decisions.md). No Alliance rule changed in this acceptance pass: automatic per-turn taxation, the four-category ARL, the narrow `UD-045` authorization with `UD-046` Open, the separate `D-140`-authorized Alliance-to-Alliance treaty/NAP framework (`AT-E00`/`AT-E01`) without general delegation, with `UD-047` remaining Open for collective positions and any delegation model, and `AX-01`–`AX-30` are unchanged, and Global Trade (D-122) remains approved mandatory scope and release-gated. **Prompt 09C** — Alliance workflows, edge cases, acceptance matrix and release-gate evidence — is **complete at the specification/documentation level (2026-11-03; correction passes recorded in [§54](06_stage_2_progress_log.md) and [§55](06_stage_2_progress_log.md); original close in §53); Prompt 10A research is complete (research/documentation only; [§56](06_stage_2_progress_log.md)); Prompt 10B is complete at the specification/documentation level (§58; final corrections 10B-C §59, 10B-C2 §60 and 10B-C3 §61); Prompt 10C is complete at the specification/documentation level (2026-11-04; §63–§66, including the 10C-C3 validator-integrity correction)**; no new 09B redesign or research is authorized. Prompts 11–15 remain pending, with their B-09 and B-10 dependencies now recorded.

**Created:** 2026-10-23
**Status:** Registered by **D-012**. Prompts 01–06 executed (2026-10-23/25) and accepted; **Prompt 07 is complete (2026-10-29)** — 07A research and 07B market foundations (2026-10-28), then 07C workflows and acceptance; **Prompt 08 is complete (2026-10-30): 08A research and requirements, 08B diplomacy foundations and 08C workflows and acceptance, corrected by 08C-C, 08C-D and 08C-E on 2026-10-30**; Prompt 09A — alliance research and candidate requirements baseline — is accepted after the final 09A-F closure pass (2026-10-31; with 09A-D and 09A-E substantive corrections); **Phase 09B Alliance specification and documentation: ACCEPTED (2026-11-03; D-142 / DD-165)** — accepted at the specification/documentation level only, with production implementation, integration testing in the live game and release still pending; **Prompt 09C is complete at the specification/documentation level (2026-11-03; correction passes [§54](06_stage_2_progress_log.md), [§55](06_stage_2_progress_log.md)); Prompt 10A research complete (research/documentation only; §56); Prompt 10B is complete at the specification/documentation level (§58; final corrections 10B-C §59, 10B-C2 §60 and 10B-C3 §61); Prompt 10C is complete at the specification/documentation level (2026-11-04; §63–§66)**; **Prompt 11A — research, benchmarking and design foundations — is complete at the research/design-foundations level (2026-11-05; §67)** and **Prompt 11B is complete at the specification level (2026-11-05; §68), Prompt 11C is complete at the specification/documentation level (log §72), and Prompt 12A is complete at the research/design-foundations level (log §73), **Prompt 12B is complete at the specification/documentation level (log §75), and Prompt 12C is complete at the specification/documentation level (2026-11-10; log §85), with 10 journeys, 52 workflows, 100 edge cases, 378 acceptance specifications and 20 gates at 16 PASS / 2 PARTIAL / 2 BLOCKED, and with no rule, requirement, contract identifier, formula, parameter or number added — 12B acceptance remains 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23` unchanged), R8 remains DEFERRED BY OWNER and 12B-C1 remains NOT CLOSED**; Prompt 11's 11C companion still awaits owner acceptance of its PARTIAL verdict, and Prompts 13–15 are pending. `UD-040`–`UD-049` remain Open or Deferred; no owner decision was resolved by the acceptance record. No gameplay implementation has yet been performed. Global Trade is approved mandatory product scope (D-122) but remains release-gated.
**Official stage:** Stage 2 — Create the Master Game Design Bible ([ROADMAP.md](../ROADMAP.md)).
**Objective:** produce the authoritative game-design specification for Nation Supremacy — how the game works, what players can do, which rules and formulas resolve outcomes, how systems interact, and how the player experience behaves.

This file is the **only** Stage 2 prompt register. Do not create a competing roadmap. If a prompt's scope proves wrong, amend this file and record the change; do not start a second sequence.

---

## 0. Progress

| # | Prompt | Deliverable (target path under `docs/stage-2/`) | Status |
|---|---|---|---|
| 01 | Bible structure and requirements traceability | `02_…outline.md`, `03_requirements_traceability.md`, `04_approved_and_provisional_decisions.md`, `05_unresolved_design_decisions.md` | **Complete** (2026-10-23; [log](06_stage_2_progress_log.md)) |
| 02 | Core gameplay loop, symbolic world and turn system | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](07_core_gameplay_loop_symbolic_world_and_turn_system.md) | **Complete** (2026-10-23; [log](06_stage_2_progress_log.md)) |
| 03 | Account onboarding, nation creation and progression | [`09_account_onboarding_nation_creation_and_progression.md`](09_account_onboarding_nation_creation_and_progression.md) — the planned `08_…` slot is the decision-closure audit | **Complete** (2026-10-24; [log §7](06_stage_2_progress_log.md)) |
| 04 | Economy, resources, treasury and national finances | [`10_economy_resources_treasury_and_finances.md`](10_economy_resources_treasury_and_finances.md), [`10_economic_formula_and_balance_register.md`](10_economic_formula_and_balance_register.md), [`research/04_politics_and_war_economy_research.md`](research/04_politics_and_war_economy_research.md) — two `10_` documents, because the formula register is authoritative separately from the rulebook | **Complete** (2026-10-24; [log §8](06_stage_2_progress_log.md)) |
| 05 | Cities, infrastructure, production and research | [`11_cities_infrastructure_production_and_research.md`](11_cities_infrastructure_production_and_research.md), [`11_city_infrastructure_production_and_research_formula_register.md`](11_city_infrastructure_production_and_research_formula_register.md), [`research/05_politics_and_war_city_infrastructure_production_research.md`](research/05_politics_and_war_city_infrastructure_production_research.md) — two `11_` documents, for the same reason as Prompt 04 | **Complete** (2026-10-25; [log §9](06_stage_2_progress_log.md)) |
| 06 | Population and domestic politics — two parts: **06A** foundation, **06B** elections, campaigns, leadership retention, crises and unrest | 06A: [`12_population_and_domestic_politics.md`](12_population_and_domestic_politics.md) + [`12_population_and_domestic_politics_formula_register.md`](12_population_and_domestic_politics_formula_register.md) + [`research/06_…`](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md); 06B: appended to the same two documents (the planned `12_domestic_politics.md` slot was taken by the split) | **Complete** (2026-10-25; **micro-corrected 2026-10-28, five passes, the cross-document reconciliation, the publication/catch-up correction and the handoff-timing clarification** — B-06 **v2.5** in two parts, register **v2.4** F-PD-001…F-PD-044, 31 examples E19–E49, **879/879** arithmetic checks with an 18/18 failure-demonstration; [log §10](06_stage_2_progress_log.md)–[§19](06_stage_2_progress_log.md)) |
| 07 | Trade and market systems — **07A** research, **07B** foundations, **07C** workflows and acceptance | **07A:** [`research/07A_politics_and_war_market_research.md`](research/07A_politics_and_war_market_research.md) · **07B:** [`13_trade_and_markets.md`](13_trade_and_markets.md) + [`13_trade_and_markets_formula_register.md`](13_trade_and_markets_formula_register.md) · **07C:** workflows and acceptance | **07A complete**; **07B complete** (2026-10-28); **07C complete and accepted** (2026-10-29; [`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md); [log §23](06_stage_2_progress_log.md)) |
| 08 | Diplomacy between nations — **08A** research and requirements, **08B** foundations, **08C** workflows and acceptance | **08A:** [`research/08A_diplomacy_research.md`](research/08A_diplomacy_research.md) · **08B:** [`15_diplomacy.md`](15_diplomacy.md) v1.2 + [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md) v1.2 (`14`_ is the 07C companion; Prompt 09 becomes `16_alliances.md`, D-132; corrected by 08B-C and 08B-D) · **08C:** [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md) v1.3 (30 workflows, 54 edge cases, 88 tests; exhaustive §15.5 ledger, 101 DIRECT / 16 SUPPORTING / 1 DEFERRED; corrected by 08C-C, 08C-D and 08C-E) | **08A complete** (2026-10-29; research only — no diplomacy rule is approved; [log §24](06_stage_2_progress_log.md)); **08B complete** (2026-10-30; designed, not implemented; [log §25](06_stage_2_progress_log.md)); **08B-C correction complete** — seven audit defects repaired in v1.1 ([log §26](06_stage_2_progress_log.md)); **08B-D correction complete** — F-DP-005/007/008 freeze intervals, limits rows and the stale handoff header repaired in v1.2 ([log §27](06_stage_2_progress_log.md)); **08C complete** (2026-10-30; [log §28](06_stage_2_progress_log.md)); **08C-C correction complete** — all 54 DPE mappings audited, 14 missing tests added (`DPA-073`…`DPA-086`), §14 headings and DPW-001/002 references corrected ([log §29](06_stage_2_progress_log.md)); **08C-D correction complete** — `DPA-087`/`DPA-088` added, five REQ rows reconciled, `DPE-054` separated into three scenarios and retained PARTIAL for Prompt 12, validator ranges and fixtures hardened ([log §30](06_stage_2_progress_log.md)); **08C-E correction complete** — exhaustive bidirectional §15.5 ledger (117 pairs + 1 deferred), direct/supporting classification enforced in both directions, DPA-041/087/088 reconciled, validator at 31/31 self-tests ([log §31](06_stage_2_progress_log.md)); **Prompt 08 complete** |
| 09 | Alliance system and alliance management | [`16_alliances.md`](16_alliances.md) (`15_` is B-08; D-132); **09C companion (complete at specification/documentation level):** `16_alliances_workflows_acceptance.md` | **ACCEPTED — specification/documentation level (D-142 / DD-165).** 09A accepted after 09A-F; 09B corrected by 09B-C through 09B-P. ([§32](06_stage_2_progress_log.md)–[§36](06_stage_2_progress_log.md), [§37](06_stage_2_progress_log.md)–[§52](06_stage_2_progress_log.md); [09B-F audit](16_alliances_project_wide_consistency_audit.md) amended by 09B-G, hardened under 09B-H, extended by 09B-I with the ALL-093 withdrawal, a separate Alliance treaty object, NAP enforcement and the same-Alliance attack ban, corrected by 09B-J with automatic per-turn production taxation, player-authored 0–100% asset-specific rates, role-governed policy freeze, a credit-only receiving ledger under an Open UD-046, non-covered NAP membership and C25 plain-modal completion, re-verified by 09B-K with positive appeal-grant semantics, ALF-21/23/24 cleanup, credit-only ARL wording, an ambiguous-membership 0% safeguard under Open UD-040 and post-tax production-chain accounting, and consolidated by 09B-L with the ALL-006–ALL-008 taxation reconciliation, the four-category ARL receipt/accounting record and purpose-limited operational funding, the narrow UD-045 authorization with UD-046 Open, the AT-E00/AT-E01 effect catalogue and the widened C25 detector), closed out by 09B-M with the fail/review/safe C25 gate, the restored D-140 plus dated D-141, the ARL availability boundary and cumulative tax accrual, corrected by 09B-N with recourse wording, former-people labels and redress review routing, and completed by 09B-O with a bounded procedural-domain gate covering petition, review, reconsideration, challenge, hearing, remedy and fixed denial, then corrected by 09B-P with ambiguous dismissal and grievance review routing and an explicit redress failure; **Phase 09B accepted at specification/documentation level by D-142 / DD-165; production implementation, integration testing and release pending; `UD-040`–`UD-049` remain Open/Deferred; **Prompt 09C complete at the specification/documentation level (2026-11-03; §53 original close, §54 and §55 correction passes); Prompt 10A research complete (research/documentation only; §56); Prompt 10B complete at the specification/documentation level (§58; final corrections 10B-C §59, 10B-C2 §60 and 10B-C3 §61); Prompt 10C complete at the specification/documentation level (2026-11-04; §63–§66); Prompt 11 is complete at the specification level with its 11C PARTIAL verdict awaiting owner acceptance; Prompt 12A is complete at the research/design-foundations level; Prompt 12B next and not started**)** |
| 10 | Warfare, campaigns and postwar settlements | `17_warfare_and_settlements.md` (`16_` is B-09's); **10A research companion:** [`research/10A_politics_and_war_warfare_research.md`](research/10A_politics_and_war_warfare_research.md); **10C companion:** [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md) | **COMPLETE at the specification/documentation level — Prompt 10B (specification) complete (2026-11-03; [§58](06_stage_2_progress_log.md)), correction 10B-C complete (2026-11-04; [§59](06_stage_2_progress_log.md)), final semantic closure 10B-C2 complete (2026-11-04; [§60](06_stage_2_progress_log.md)) and final consistency pass 10B-C3 complete and verified PASS (2026-11-04; [§61](06_stage_2_progress_log.md), verification [§62](06_stage_2_progress_log.md); [B-10](17_warfare_and_settlements.md) **v1.3**, 30 sections, 188 numbered rules plus 42 lettered sub-rules + [formula register](17_warfare_formula_register.md) **v1.3**, 39 formulas; 25 architecture decisions; every 10A identifier dispositioned; `UD-032` resolved as Option A; Operations Points are one persistent national military-only pool with +1 OP at the P3.7 opening, cap 10 provisional and carry below the cap; 89 links repaired and a project link validator added; documentation only — no code or runtime test); Prompt 10A research complete ([§56](06_stage_2_progress_log.md), corrected by [§57](06_stage_2_progress_log.md)); Prompt 10C complete at the specification/documentation level (2026-11-04; [§63–§66](06_stage_2_progress_log.md): 40 workflows, 60 edge cases, 124 acceptance tests (120 core plus four class-P supplements), 50-requirement bidirectional ledger, D-143 failure-code-gap disclosure, designed not executed); Prompt 11 is complete at the specification level; Prompt 12A is complete at the research/design-foundations level; Prompt 12B next and not started. No code, runtime test or release.** |
| 11 | World events, objectives, rankings, long-term progression — **11A** research and design foundations, **11B** specification (B-11 rulebook), **11C** workflows and acceptance — **all three complete at the specification/documentation level (log §67, §68, §72)**; the parent prompt stays open pending owner acceptance of 11C's PARTIAL verdict | `18_world_events_objectives_rankings_progression.md` (**B-11 v1.0, drafted by 11B**) with its [formula register](18_world_events_objectives_rankings_progression_formula_register.md) and [52-gate acceptance crosswalk](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md) with its [acceptance source artifact](18_world_events_objectives_rankings_progression_acceptance_source.md); **11A deliverables:** [`research/11A_world_events_objectives_rankings_progression_research.md`](research/11A_world_events_objectives_rankings_progression_research.md), [`research/11A_comparator_sources_and_benchmarks.md`](research/11A_comparator_sources_and_benchmarks.md), [`research/11A_integration_and_risk_registers.md`](research/11A_integration_and_risk_registers.md) | **11A COMPLETE at the research/design-foundations level** (2026-11-05; [§67](06_stage_2_progress_log.md)) — 114 source rows, 73 benchmark entries, 7 games, 40 integration rows, 28 risks, 30 candidate requirements, 16 open questions, 34 recommendations, D-144…D-151 / DD-192…DD-199; **no B-11 rule, number or implementation approved**. **11B COMPLETE at the system-specification level** (2026-11-05; [§68](06_stage_2_progress_log.md)) — 723 `WEP-` rules, 50 formula IDs (49 active + 1 retired), 17 contracts, 60 requirements, D-152…D-161 / DD-200…DD-209; **11B-C2 integrity correction applied and independently accepted by C3** (2026-11-05; §§70–§71) — original 52 criteria preserved in a hashed [source artifact](18_world_events_objectives_rankings_progression_acceptance_source.md) and matched by the crosswalk, 52/52 gate rows PASS with 61 separate validator checks; independent acceptance recorded by C3; **11C complete at the specification/documentation level (log §72); its PARTIAL verdict awaits owner acceptance.** Prompt 11's parent remains open |
| 12 | Fair play, player protection, privacy, administration — **12A** research and design foundations, **12B** specification, **12C** workflows and acceptance | [20_fair_play_and_player_protection.md](20_fair_play_and_player_protection.md) plus its [formula register](20_fair_play_and_player_protection_formula_register.md), [requirement register](20_fair_play_and_player_protection_requirements.md) and [acceptance framework](20_fair_play_and_player_protection_acceptance.md) | **12A complete** (2026-11-06; [log §73](06_stage_2_progress_log.md), reconciled 2026-11-07 [§74](06_stage_2_progress_log.md)); **12B specification complete at the documentation level** (2026-11-07; [§75](06_stage_2_progress_log.md)), corrected by **12B-C1** ([§76](06_stage_2_progress_log.md)), **12B-C1-R1** ([§77](06_stage_2_progress_log.md)), **12B-C1-R2** ([§78](06_stage_2_progress_log.md)), **12B-C1-R3** ([§79](06_stage_2_progress_log.md)) and **12B-C1-R4** ([§80](06_stage_2_progress_log.md)) and **12B-C1-R5** ([§81](06_stage_2_progress_log.md)) and **12B-C1-R6** ([§82](06_stage_2_progress_log.md)) and **12B-C1-R7** ([§83](06_stage_2_progress_log.md)) — 344 rules, 16 violation classes, 16 formulas, 14 parameters, 106 requirements (`REQ-764`–`REQ-869`), 26 acceptance gates (23 PASS / 3 PARTIAL); validator 87 checks with 59/59 positive and 153/153 negative fixtures, each run through the complete check registry, plus a 23/23 subprocess mutation audit; R6 failed independent acceptance on eight reproduced bypasses, R7 closes them but its own independent acceptance is **not accepted**; the independent audit of Project X (77) reported five further bypass classes, which are kept on the record as known residual weaknesses, and **R8 is DEFERRED BY OWNER (2026-11-10; [§84](06_stage_2_progress_log.md)) with reopening only on explicit owner authorization and no unsolicited R8 correction work authorized**; **12C complete at the specification/documentation level (2026-11-10; [§85](06_stage_2_progress_log.md))** — canonical companions [`20_fair_play_and_player_protection_workflows.md`](20_fair_play_and_player_protection_workflows.md) (10 `FPJ-`, 52 `FPW-`), [`20_fair_play_and_player_protection_integration.md`](20_fair_play_and_player_protection_integration.md) (the twenty `INT-` contracts reused with none added; 2 conflicts, 10 gaps) and [`20_fair_play_and_player_protection_edge_cases_acceptance.md`](20_fair_play_and_player_protection_edge_cases_acceptance.md) (100 `FPE-`, 378 `FPA-` all `SPECIFIED`/`BLOCKED` and none executed, the 106-row `REQ-764`…`REQ-869` ledger with 0 orphans, 20 `P12C-` gates at 16 PASS / 2 PARTIAL / 2 BLOCKED); validator [`12C_validate_fair_play_workflows.py`](../qa_backups/12C_validate_fair_play_workflows.py) at 24 checks; decisions **D-188…D-197 / DD-236…DD-245**; documentation only — no implementation, no gate closed, `P12B-14`/`P12B-16`/`P12B-23` and the seven 12A PARTIAL gates unchanged, R8 still **DEFERRED BY OWNER** and 12B-C1 still **NOT CLOSED**; the pre-existing conflict-marker defect in 25 files (117 hunks) is **remediated and evidenced** (2026-11-10; [§86](06_stage_2_progress_log.md)); the 12C gate tally recomputes to 16 PASS / 2 PARTIAL / 2 BLOCKED on that evidence |
| 13 | Interface, screens and player journeys — **13A** research/architecture/design foundations and **13B** screen & component specifications | 13A deliverables: [`research/13A_politics_and_war_ui_research.md`](research/13A_politics_and_war_ui_research.md), [`research/13A_ui_design_principles_and_architecture.md`](research/13A_ui_design_principles_and_architecture.md), [`research/13A_master_screen_inventory.md`](research/13A_master_screen_inventory.md), [`research/13A_responsive_and_design_system_foundations.md`](research/13A_responsive_and_design_system_foundations.md), [`research/13A_ui_requirements_open_questions_and_acceptance.md`](research/13A_ui_requirements_open_questions_and_acceptance.md); B-13 rulebook reserved at `21_interface_and_player_journeys.md` (D-198) | **13A COMPLETE at the research/design-foundations level (2026-11-11; [§87](06_stage_2_progress_log.md); D-198…D-205 / DD-246…DD-253; 24 P13A gates at 23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED).** **13B — screen and component specifications — is next, unauthorized and unstarted.** |
| 14 | Numbers, formulas, balance and worked examples | `21_formulas_and_balance.md` | Pending |
| 15 | Assemble and verify the Bible | `22_master_game_design_bible.md`, `23_stage_2_completion_report.md` | Pending |

> **Split note (2026-10-25):** Stage 2 Prompt 06 is executed as two parts — **06A** (population, government identity, approval, constituencies, policy; complete) and **06B** (elections, campaigns, leadership retention, crises and unrest; complete). They are one roadmap stage, not two; the 15-prompt sequence is unchanged, and the earlier "06 — Population and domestic politics … next task" row is **historical** only.

Target filenames are guidance, not a quota. Create a document when it has real content; reuse an existing document rather than duplicating rules. One document is authoritative for each rule, and the Bible links to it.

> **Filename note (2026-10-29):** the `14_diplomacy.md` guidance name is unavailable — `14_market_workflows_and_acceptance.md` is the 07C companion. 08A confirms the collision and proposes `15_diplomacy.md`; **08B confirms the next free prefix at its start** and then updates this table and the outline together, as the rule above requires. Rows 09–15 keep their guidance numbers until that confirmation; no file is renumbered after it has been cited.

> **Filename note (2026-10-25):** Prompt 05 created two documents under the `11_` prefix (the rulebook and the formula register), so its planned `11_domestic_politics.md` slot moved to `12_`, and rows 06–15 shifted by one with it (`12_domestic_politics.md` … `22_stage_2_completion_report.md`). The outline's filename-numbering note records the rule: the prefix is a serial number in this folder, not the Bible part number.

> **Filename note (2026-10-24):** Prompt 04 created two documents under the `10_` prefix (the rulebook and the formula register), so Prompt 05 takes the next free prefix and confirms it at start. Rows 06–15 keep their guidance numbers until their own prompt writes the file; no file is renumbered after it has been cited.

> **Filename note (2026-10-23):** the original table used `06_…` for Prompt 02, which collided with the progress log. Prompt 02's brief fixed its document at `07_…`; the not-yet-written rows therefore moved one place (`07`–`19` for Prompts 02–14, `20` for the Bible, `21` for the completion report). The **15-prompt sequence, purposes and guardrails are unchanged**. Each future prompt may confirm its own path; if it does, update this table and the outline together.

---

## 1. Mandatory start-of-prompt procedure

Every Stage 2 prompt begins with this, before any writing:

1. Read [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md), [DECISIONS.md](../DECISIONS.md) and [ROADMAP.md](../ROADMAP.md).
2. Read the Stage 1 reports that the prompt's topic depends on — in full, not from memory of a summary.
3. Read the Bible material already written, plus `03_requirements_traceability.md` and `05_unresolved_design_decisions.md`.
4. Check whether the answer already exists in a document. Update the authoritative document; do not fork a second source of truth.
5. Only then write.

A new chat or a different model has no memory of earlier sessions. Assume nothing carries over except the files.

### End-of-prompt procedure

Record in the updated documents and in [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md):

- which prompt was completed and which file is authoritative for its content;
- requirements newly covered (by ID) and decisions still open;
- anything newly **proposed** versus **approved**;
- tests or validations actually executed, with results;
- the exact next prompt.

Update [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md) and [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) whenever the current state or the next task changes. Add a [DECISIONS.md](../DECISIONS.md) entry **only** for a genuine owner approval or a recorded project decision.

---

## 2. Fixed inputs every prompt must respect

These are constraints, not topics for re-debate:

- **Name:** Nation Supremacy (D-007). `Project X` is internal only.
- **World:** fictional and **mapless** — a symbolic network of nations and relationships. Never introduce a geographic world map, territorial fronts or real-world borders.
- **Time:** one global turn every **2 hours on fixed UTC boundaries**, 12 per day, resolved server-side. Changing this requires an owner decision.
- **Backend direction:** Cloudflare Pages frontend + Supabase PostgreSQL/Auth/RLS with `pg_cron` as the single authoritative scheduler (D-008). Stage 2 does not re-litigate this and does not implement it.
- **Free-first:** ₹0 required monthly cost is the target; it is not a guarantee at every scale.
- **Accounts:** one account per person is a requirement; the technical enforcement mechanism is a later-stage design problem. Do not claim perfect identity verification exists.
- **Provisional status:** **D-015** approves the Operations Points *model*; its cap, per-order costs and readiness scaling stay provisional. Every other unapproved proposal stays provisional. Stage 2 may **specify** them, never silently promote a value or a proposal.
- **Decision authority:** ordinary design questions are decided and recorded by the working AI under [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (D-014); fixed constraints, money/legal commitments, missing credentials and destructive external actions remain owner decisions.
- **Labelling:** every rule is marked as an owner-approved requirement, a provisional design choice, a playtest-dependent value, or an implementation detail.

---

## 3. The 15 prompts

### Prompt 01 — Master Game Design Bible structure and requirements traceability

**Purpose.** Build the frame, not the Bible: decide its structure, map what Stage 1 already established, collect what is approved, name what is provisional, and list what is missing.

**Inputs.** Reports 01–13 (especially 05 concept/pillars, 06 systems, 07 economy, 08 security, 09 synthesis with REQ-001…039); DECISIONS.md; ROADMAP.md.

**Outputs.**
- Bible outline: parts, chapters, and which document is authoritative for each rule family.
- Requirements traceability tracker: REQ-001…039 against design coverage (covered / partially covered / not yet designed), with the owning Stage 2 prompt.
- Approved-decisions register and provisional-decisions register, separated.
- Unresolved design decisions register: DEF-001/002/018, OD-01…OD-12, SDQ-001…018 (P0 subset first), ECOQ families, OSQ-001…012 — each with the prompt that should resolve it.
- Stage 2 progress log.
- Prioritised work list for Prompts 02–14, derived from that gap analysis.

**Guardrail.** Do not write the whole Bible in this prompt. Do not resolve a design question because it is convenient; classify it instead.

**Done when.** The outline, the three registers and the traceability table exist, the gaps are named, and Prompt 02 can start without further preparation.

---

### Prompt 02 — Core gameplay loop, symbolic world and turn system

**Purpose.** Define what a player actually does in a session, how the mapless world is legible, and how the shared turn resolves.

**Outputs.** Core session loop (first minute → first turn → steady state); turn timing and boundary rules; action limits and sequencing; deterministic turn-resolution order; inactive-player behaviour; player-facing explanation and worked examples.

**Must preserve.** Two-hour UTC cadence; no map; absence must not be punished and presence must not be rewarded (DP-002); no attendance streaks.

**Done when.** A reader can state, without ambiguity, what happens between 10:00 and 12:00 UTC and in what order.

---

### Prompt 03 — Account onboarding, nation creation and progression

**Purpose.** Define the journey from first visit to a functioning nation, and how a nation grows across weeks.

**Outputs.** Account holder policy and ownership model; shared-network interaction restrictions and their review/appeal route; account-to-nation workflow; identity and creation rules (name, short name, emblem, starting posture); the standard starting state with numbers delegated; instant reroll and its reset boundary; account lifecycle and recovery; onboarding, newcomer protection, progression milestones; inactivity, abandonment and re-entry. Delivered in [B-03](09_account_onboarding_nation_creation_and_progression.md).

**Must preserve.** One account per person (policy now, enforcement later); the first session must be completable in a short sitting.

**Done when.** The first-hour experience and the first-month arc are both specified, and nothing depends on a purchased domain or paid service.

---

### Prompt 04 — Economy, resources, treasury and national finances

**Purpose.** Define money, materials, production, consumption, taxation, income, expenses and upkeep.

**B-03 carry-in.** The replacement nation receives only the standard starting bundle, once; a reroll destroys every asset, reservation and progress item. Fix the starting-grant size and the deficit rule; B-03's provisional parameters are not approved values (B-03 §8, §9.4, §18; REQ-067/068/072).

**Outputs.** Resource catalogue (each with purpose and at least two uses / two sourcing routes per ECON-006's floor); economic rules; treasury and accounting rules; transaction and cost definitions; initial formula shapes; economic safeguards; worked examples.

**Must preserve.** One treasury pool, no debt, no interest, no activity rewards (ECON-001/019/020); the conservation accounting identity C1–C4; `ECOQ-002` and `ECOQ-004` are the top open numeric families.

**Done when.** Every resource has a stated purpose and every money flow in and out of the treasury is enumerated.

---

### Prompt 05 — Cities, infrastructure, production and research

**Purpose.** Define how a nation expands productive capacity.

**B-03 carry-in.** A new nation starts at baseline; a reroll removes all levels, queues and research programmes, and nothing is transferred (B-03 §9.4, §18).

**Outputs.** Construction rules; building/facility catalogue structure; upgrade costs and prerequisites; production modifiers; research and programme progression; dependencies between cities/infrastructure/production/research.

**Must preserve.** No geographic city placement — the symbolic-world model requires that cities be capacity/identity entities, not map tiles. Science stays a research programme class, not a sixth development line.

**Done when.** A player's investment choices are describable as a small set of legible decisions with stated effects.

---

### Prompt 06A — Population and domestic politics: the foundation (complete 2026-10-25)

**Purpose.** Define population, public sentiment, government forms, policy, legitimacy and stability, and publish the interfaces the interactive political system will use.

**Delivered.** A national population with a hard housing cap and a gradual crowding decline; six fixed constituencies with published weights and support terms; approval, stability and derived legitimacy; six permanent governments with five numeric channels each; two policy axes with a 12-turn cooldown; the political state and the P3.8 settlement; the complete 06B interface bundle; 18 worked examples and a formula register.

**Guardrail honoured.** The proposed permanent-government choice was evaluated, not assumed (adopted as Model A with reasons), and no election interval, penalty or crisis threshold was finalised.

**Done when.** Political decisions produce foreseeable, explainable effects on the economy and the nation's standing — **satisfied for the foundation**; the interactive consequences remain 06B's.

---

### Prompt 06B — Elections, campaigns, leadership retention, political crises and unrest (complete 2026-10-25)

**Purpose.** Build the interactive political game loop on the 06A foundation: elections, campaigns, leadership retention, crises, unrest and recovery.

**B-03 carry-in.** A new nation uses the default political preset; a reroll ends its political state with no stability, policy or legitimacy benefit carried over (B-03 §18).

**Outputs.** Domestic politics rules; policy effects; stability/legitimacy model; government options and limits; player decision framework; worked examples of political consequences.

**Guardrail.** If a mechanic (elections, coups, parties) is genuinely optional, document the options and trade-offs as unresolved rather than approving one. 06B must consume — never redefine — `approval`, `stability_bp`, `legitimacy`, the six supports, the weights and the political state.

**Done when.** Every adopted leadership process is reachable and exitable, every crisis has a published trigger, severity curve and recovery path, and the whole design is verified against B-04's ledger and B-05's capacity. — **satisfied**: the 12-turn transition, the five retention tests, the 18-turn crisis and the 12-turn recovery are published with their exit conditions; every proposed penalty was modelled against B-04 and B-05 and three were rejected on that evidence.

---

### Prompt 07 — Trade and market systems

**Stage split (2026-10-28).** Prompt 07 is executed in three parts: **07A** — Politics & War market research and handoff (complete; report under `research/`); **07B** — Nation Supremacy market foundations and economic integration (complete 2026-10-28; B-07 and its register); **07C** — market workflows, safeguards, edge cases, integration checks and final acceptance. **07C is complete (2026-10-29)** and its companion is [`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md); implementation has not started. The 07A report supplies evidence only and approves no Nation Supremacy market rule.

**07C result (2026-10-29).** [The companion](14_market_workflows_and_acceptance.md) records the directed and Global Trade workflows (W-D01…W-D20, W-G01…W-G30), the cross-system interface table, fourteen edge-case walkthroughs, an 83-test catalogue and a **237/237-rule** acceptance matrix with no unmapped rule. **D-122 / DD-136 / REQ-513** approve Global Trade as mandatory product scope; the six gates remain **not met / partial**. B-07 **v1.1** corrects three confirmed defects (E1 ledger double-count, space reservations added back, symmetric-band wording). The acceptance verdict is **PASS at the specification level**; Prompt 08 — diplomacy — followed, and its **08A research is complete (2026-10-29)**.

**Purpose.** Define how nations exchange resources and enter trade agreements.

**B-03 carry-in.** Block directed and market trades between a restricted pair; resolve pending offers on reroll; apply the fresh-nation one-sided transfer restriction and own the fair-value band and window (B-03 §5.5, §9.5, §18; REQ-063).

**Outputs.** Market mechanics; trade workflows; pricing and fee rules; transaction limits; settlement behaviour; integrity requirements (manipulation, wash trading, one-sided trades) with examples.

**Must preserve.** Directed trades at first playable, atomic offer/accept with **no partial fill of a directed offer** (ECON-013, R-19; MKT-119); a listing market only behind gate G-1…G-6; alliance and diplomacy interactions stated. B-07 keeps the directed rule and adds partial fills only to a **public listing**, where each fill is a separate execution (MKT-083).

**Done when.** The trade loop and its abuse cases are both specified, and DEF-018's offer-reservation ambiguity is either resolved (with an owner decision) or carried as an explicit open question. **Satisfied by 07B:** D-016 settles directed offers, D-110 settles public listings, and the failure paths are enumerated in B-07 §26.

**07A result (2026-10-28).** [Research report](research/07A_politics_and_war_market_research.md) v1.0: 14 sections, 22 sources (`PWS-001`…`PWS-022`), 30 findings (`PWR-001`…`PWR-030`), evidence classes and confidence per finding. It records the evidenced posted-offer/manual-acceptance structure, the public price and trade-history layer, the account/network restrictions, the undocumented matching/partial-fill/fee/expiry questions, and the player-experience evidence with its limits. **No fee, limit, price band, order type, reservation rule or settlement rule was approved.** The report's §14 is the 07B handoff; its §12 lists the gaps, including the unavailability of the owner's authenticated Chrome session.

**07B inputs.** The report's §14.6 reading list, §14.7 reconciliation list and §14.8 open-decision list; D-016, D-017, REQ-010, ECN-211, B-03 ONB-031/ONB-032, B-04 ECN-208 and the D-034 pair matrix. The gate G-1…G-6 remains **unpassed**, so a listing market remains **Deferred**.

**07B result (2026-10-28).** [B-07](13_trade_and_markets.md) v1.0 (32 sections, 237 `MKT-` rules (`MKT-001`…`235` plus `215a`/`215b`), 21 worked examples, 35 failure scenarios) and its [formula register](13_trade_and_markets_formula_register.md) v1.0 (`F-TM-001…F-TM-039`). Directed trades stay first-playable and fee-free; a directed offer reserves nothing and settles atomically at P4; a **public listing reserves at posting** (D-110, a new scoped rule; D-016 is unchanged); execution is **taker-selected posted price** with partial fills and no matcher (D-111); the fair-value band is **3,000 bp on book value** with a fresh block and a mature signal (D-114); no market statistic is public at first playable (D-117); Global Trade is **designed, required and release-gated**, with G-1, G-2, G-3, G-5 and G-6 **not met** and G-4 **partial**. Decisions **D-109…D-121** / **DD-123…DD-135**; requirements **REQ-427…REQ-512**; **UD-037/UD-038** opened for calibration and post-gate liquidity. No market code, migration or deployment exists.

---

### Prompt 08 — Diplomacy between nations

**Stage split (2026-10-29; updated 2026-10-30).** Prompt 08 is executed in three parts: **08A** — diplomacy research, evidence, requirements and cross-system integration (**complete**, report under `research/`); **08B** — Nation Supremacy diplomacy foundations (**complete 2026-10-30**: states, permissions, treaty mechanics, effects, formula register and cross-system contracts); **08C** — workflows, edge cases, safeguards, worked examples and acceptance (**complete 2026-10-30, corrected by 08C-C, 08C-D and 08C-E**: 30 `DPW-` workflows, 54 `DPE-` cases and 88 `DPA-` tests; 52 edge cases covered, 2 partial, both Prompt 12 dependencies; exhaustive §15.5 ledger with 101 direct, 16 supporting and 1 deferred requirement relationship). They are **one roadmap stage, not three**; the 15-prompt sequence, purposes and guardrails are unchanged. **08A approved nothing**; **08B decided the rules and approved no implementation.**

**08A result (2026-10-29).** [The research report](research/08A_diplomacy_research.md) v1.0: 19 sections, **19 sources** (`DPS-001`…`DPS-019`), **54 findings** (`DPR-001`…`DPR-054`), 6 conflicts (`DPX-01`…`DPX-06`), 12 candidate recommendations (`DCR-01`…`DCR-12`) and 16 questions for 08B/08C/09 (`DQ-01`…`DQ-16`). It records the comparator evidence (Politics & War, eRepublik, Call of War, Stellaris, EVE Online), the **Prompts 01–07C integration matrix**, the **Prompt 09 interface and ownership matrix** (`A-01`…`A-12`), the UD-033 analysis, and the two handoffs. **UD-013 and UD-033 were left open by 08A** and were later resolved by 08B (D-124, D-128); the report decides neither. It records two gaps: no B-08 rulebook exists, and `14_diplomacy.md` cannot be created because `14_` is the 07C companion.

**08B result (2026-10-30; corrected 2026-10-30 by 08B-C and 08B-D).** [B-08](15_diplomacy.md) v1.2 — 22 sections, **157 `DIP-` rules**, **15 `DPF` codes**, **12 worked examples** — and its [formula register](15_diplomacy_formula_register.md) (`F-DP-001`…`F-DP-012`). The model is three-layered: a directional posture (`FRIENDLY`/`NEUTRAL`/`TENSE`/`HOSTILE`), a mutual agreement with versions, and a separate effect. The catalogue is **three agreements** — `DP-T01` NAP (war-declaration block, inert until Prompt 10), `DP-T02` consultation (notice gate), `DP-T03` aid (crown-only transfer) — plus **one act**, `DP-A01` embargo (24 turns, `HOSTILE` posture required, new transfers blocked, grandfathering, no fee). There is **no diplomatic reputation score**: a nation-scoped public breach count over 4,380 turns with no mechanical effect, and a replacement starts at zero (**UD-033 resolved as option (a)**). **UD-013 resolved** by the three-effect map. Player sovereignty is explicit: the sole authority is the active nation’s owner; no delegation; no autonomous accept/reject/declare/break; automatic acts are limited to activation, expiry and cleanup; `TRANSITION`/`CRISIS` freezes deadlines. Decisions **D-123…D-132** / **DD-137…DD-146**; requirements **REQ-514…REQ-533**; **UD-039** opened for Prompt 09. `DPX-01`…`DPX-05` resolved; `DPX-06` split between B-08 (nation-level) and Prompt 09 (alliance-level). Canonical path is **`15_diplomacy.md`**; Prompt 09’s planned file is **`16_alliances.md`**. **No implementation, migration or deployment exists.**

**Purpose.** Define relationships, treaties, negotiation, sanctions, diplomatic actions and the cost of breaking commitments.

**B-03 carry-in.** A restricted pair cannot conclude a treaty with each other; a reroll terminates the old nation's treaties with a recorded event and the replacement starts neutral. **UD-033 is resolved by D-128** (no score; nation-scoped breach count; replacement starts at zero), so B-08 implements the neutral restart rather than re-deciding the scope.

**Outputs.** Diplomacy rules; treaty lifecycle (offer → accept → active → breach/expiry → record); permissions; costs and restrictions; breach and termination rules; 3–5 worked interactions.

**Must preserve.** No border-based mechanics; reputation effects route to one primary register (SYS-013 discipline); the treaty register remains minimal at first playable.

**Done when.** Every diplomatic state is reachable, exitable, and visible to both parties, and no rule requires a map.

---

### Prompt 09 — Alliance system and alliance management

**Purpose.** Define founding, governing, joining, leaving and operating alliances.

**B-03 carry-in.** A restricted pair may share an alliance but may not use its bank or hold simultaneous bank-authorising roles; a reroll ends membership and vacates roles without transferring assets (B-03 §18).

**Outputs.** Creation and membership rules; leadership roles, ranks and permissions; governance and voting; shared resources or benefits (if permitted); alliance diplomacy; Alliance coordination and a **restricted Alliance management interface** — not a war room, with no military command, no member OP spending and no shared pool. **(Clarified 2026-11-04 by Prompt 10B-C3: an "Alliance war room" is not a deliverable; the nation-owner war interface is B-10's nation-level, owner-only War Operations Board, and the Alliance surface is management only.)**

**B-08 interface.** Prompt 09 reads [B-08 §18](15_diplomacy.md), which publishes the nation-level treaty object, the authority contract, the membership-change rule (a nation treaty **persists** through join/leave/removal), the pair-restriction contract, the embargo contract, the visibility and notification rules, and **UD-039**. UD-039 is **Resolved by `D-137`**: B-08 has no alliance-level treaty object, and there is zero diplomatic delegation. **`D-140` (Prompt 09B-I) narrowly amends that scope**: Prompt 09 creates a **separate** B-09 Alliance-to-Alliance treaty object (`AT-T01`…`AT-T05`) that does not reuse or extend the B-08 nation object, and zero diplomatic delegation remains. B-08 grants **no** delegation. The Alliance document is **`16_alliances.md`**, not `15_alliances.md`, because `15_` is B-08. This paragraph is updated to the recorded resolution; the pre-D-137 planning instruction is preserved in the progress log as history.

**09A result (2026-10-31; accepted after 09A-F).** [The research report](research/09A_alliance_research.md), [source/finding registers](research/09A_alliance_sources_findings.md), [AX integration matrix](research/09A_alliance_integration_matrix.md) and [semantic review record](research/09A_alliance_reference_review.md) establish the evidence base. 09A-D performed the final traceability correction pass on AX-08 (distinguishing national warehouse storage under REQ-141/142 from alliance treasury capacity under REQ-176 and open UD-046), classifying **77** requirement relationships (39 direct, 19 related, 6 supporting, 13 no-existing across 13 AX records), completed the **15-permission** Politics & War inventory and verified the Black Knights three-stage recruitment process. **After 09B-L the Alliance block is 120 requirements (`REQ-534`–`REQ-653`): 36 Approved, 71 Provisional, 12 Open and 1 Deferred** — the 36 Approved rows are the 30 owner-authorized additions for taxation, donations, Alliance treaties, NAP consent and the same-Alliance attack ban plus the six purpose-limited operational-funding requirements; `UD-039` was deferred at 09A and is now resolved by D-137 for B-08 and amended in part by D-140 for the separate B-09 object, while `UD-040`–`UD-049` remain open; `UD-040` remains Open (09B-K adds only a reversible ambiguous-attribution 0% fallback), **UD-046 remains Open** (09B-J authorizes only automatic collection and credit to a receiving ledger, not ownership, custody, capacity, withdrawal, spending, distribution or dual approval) and **UD-047 remains Open**. 09A approves no rule and implements nothing.

**09B correction record (2026-11-02/03; acceptance recorded 2026-11-03).** Prompts 09B-C through 09B-P corrected the Alliance rulebook, its formula register, its 30 integration contracts and the semantic validator. 09B-L established the current `ALL-006`–`ALL-008` taxation reconciliation, the four-category ARL receipt/accounting record with purpose-limited operational funding, the narrow `UD-045` authorization with `UD-046` Open, and the `AT-E00`/`AT-E01` effect catalogue; 09B-M added the fail/review/safe C25 gate, restored D-140 with the dated D-141 successor, and fixed the ARL availability boundary and cumulative tax accrual. **Prompt 09B-N** closed the two appeal-detection defects identified by the independent audit — recourse wording and former-people labels — and routed uncertain redress wording to manual review. **Prompt 09B-O** closes the eight remaining procedural false negatives (petition for reconsideration, permitted review, mandatory hearing, subject-to-reconsideration, right to challenge removal, request for review, fixed denial of review and petition for redress) through a bounded person/action/normative-force gate, with ten positive, negative, ambiguous, historical and unrelated controls. C25 still returns exactly three outcomes — **FAIL**, **MANUAL REVIEW** and **SAFE** — and `UD-044` remains owner-reserved; no Alliance rule, owner decision or historical record changed. **Prompt 09B-P** closes the three remaining audited false negatives — an ambiguous challenge to dismissal and an unspecified grievance process now require manual review, while an express right to seek redress for an expulsion fails — and adds fixtures 262–265 with six compact controls. The isolated suite now contains 266 tests; 09B-P executed only Python compilation, its four new tests, the affected C25 group and the relevant C24 controls, not the complete suite. The historical record remains that 09B-P left the phase **ready for independent acceptance, not then independently accepted**; acceptance was recorded afterwards by the owner-directed alignment pass below.

**09B acceptance record (2026-11-03; specification/documentation level).** **Phase 09B Alliance specification and documentation: ACCEPTED** — **D-142** in [DECISIONS.md](../DECISIONS.md) and **DD-165** in the [04 register](04_approved_and_provisional_decisions.md), with the [05 register](05_unresolved_design_decisions.md) unchanged in decision state. This acceptance covers the Alliance rulebook [`16_alliances.md`](16_alliances.md), its [formula register](16_alliances_formula_register.md), its [integration contracts](16_alliances_integration_contracts.md) and the independent review findings already applied by 09B-N, 09B-O and 09B-P. It does **not** mean production implementation, integration testing in the live game or release; it is **not** a new owner authorization; and it resolves or closes **no** unresolved decision — `UD-040`, `UD-044`, `UD-045` (narrow tax permission only), `UD-046` (narrow ARL/operational boundary only), `UD-047`, `UD-048` and `UD-049` remain exactly as recorded. No Alliance rule was regenerated or redesigned. Global Trade (D-122) is preserved. **Prompt 09C is complete at the specification/documentation level (2026-11-03; §53 original close, §54 and §55 correction passes); Prompt 10A research is complete (research/documentation only; [§56](06_stage_2_progress_log.md)); Prompt 10B is complete at the specification/documentation level (§58; final corrections 10B-C §59, 10B-C2 §60 and 10B-C3 §61); Prompt 10C is complete at the specification/documentation level (2026-11-04; §63–§66).**

**Guardrail.** Alliance membership is never mandatory (AP-004). Shared treasuries are high-risk: specify caps and audit records or exclude them explicitly. Do not copy `Promote Self to Leader`, do not make `roles.manage` a default officer power, and keep treaty consent and embargo imposition national.

**Done when.** A new alliance can be founded, run and dissolved entirely within the rules, and every permission is stated.

---

### Prompt 09C — Alliance workflows, edge cases, acceptance matrix and release-gate evidence

**Status.** **COMPLETE at the specification/documentation level (2026-11-03; original close [log §53](06_stage_2_progress_log.md), correction passes [§54](06_stage_2_progress_log.md) and [§55](06_stage_2_progress_log.md)).** The canonical deliverable is [`16_alliances_workflows_acceptance.md`](16_alliances_workflows_acceptance.md): 49 workflows (`ALW-001`–`ALW-049`), 65 edge cases (`ALE-001`–`ALE-065`), 132 acceptance tests (`AAT-001`–`AAT-132`; 124 behavioural plus 8 document-level traceability checks), exhaustive `ALL`/`REQ`/`AX`/`F-AL`/`AUD-AL`/`D`/`DD`/`UD` traceability, release-gate evidence and implementation handoff. Completion is documentation-only: no gameplay code, runtime test or deployment exists, and `UD-040`–`UD-049` remain Open. **Prompt 10A is complete and Prompt 10B is complete at the specification/documentation level (§58; final corrections 10B-C §59, 10B-C2 §60 and 10B-C3 §61); Prompt 10C is complete at the specification/documentation level (2026-11-04; §63–§66).** The registration scope below is preserved as history.

**Purpose.** Produce the workflow-and-acceptance companion to [B-09](16_alliances.md), in the established **B-07 and B-08 companion convention** ([`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md), [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md)): player-visible workflows, edge cases, a bidirectional traceability ledger and an explicit acceptance standard. It **does not regenerate Alliance rules** — B-09, its [formula register](16_alliances_formula_register.md) and its [integration contracts](16_alliances_integration_contracts.md) stay authoritative — and it **does not repeat 09A research**. Where the companion needs a rule, it cites the authoritative section; where it needs a value, it cites the formula register; where an owner decision is open, it records the dependency rather than deciding it.

**Canonical deliverable.** `docs/stage-2/16_alliances_workflows_acceptance.md` — the single companion path. The `16_alliances.md` rulebook remains the rule source of truth; the companion is the workflow and acceptance source of truth. No other filename is registered for 09C.

**Required workflow groups (A–J).** Each group states the player-visible happy path, permission failures, boundary and edge cases, the notifications and audit records produced, and the rule/requirement references that govern it:
- **A — Founding and membership:** founding requirements and cost path; application, invitation, acceptance and rejection; joining, leaving, removal and dissolution; membership caps, cooldown and re-entry; restricted-pair carry-in under B-03.
- **B — Constitution and governance:** constitution adoption and amendment; offices, ranks and permission grants; voting and quorum; policy freeze; leadership succession and vacancy; permission-denied paths.
- **C — Taxation:** player-authored brackets and 0–100% asset-specific rates; separate Crowns and resource percentages; member assignment; effective turn and policy version; automatic per-turn collection; receipts and tax history; 100% Crowns tax and maintenance interaction.
- **D — Donations:** voluntary Crown and resource donations to the Alliance; permitted and blocked sources; receipt and accounting record; no expansion of spending authority.
- **E — ARL and operational funding:** the four-category ARL; receipt, credit-only accounting and availability boundary; purpose-limited operational funding under the narrow `UD-045` authorization with `UD-046` Open; unavailable operational purposes and their failure paths.
- **F — Treaties:** the separate B-09 Alliance-to-Alliance object (`AT-T01`–`AT-T05`); offer, consent, activation, expiry, breach and termination; zero diplomatic delegation (`D-137`/`D-140`).
- **G — NAP:** Alliance-level non-aggression for the explicitly consenting covered nations under the separate Alliance-to-Alliance treaty framework authorized by **`D-140`** (`AT-T01` / `AT-E01`); membership and coverage visibility; the non-covered-membership case; activation, expiry and breach effects. `UD-047` remains Open for collective positions and delegation and authorizes no part of this framework.
- **H — Same-Alliance attack prevention:** the ban at every attack entry point and path; cumulative server-side enforcement with B-03 pair restrictions and B-08 national treaty/NAP; membership, treaty and campaign changes; explanation surfaces; mandatory audit; no bypass and no new coverage or consent rules.
- **I — Audit, notification and security:** what each workflow records; who may read tax reports, contribution history, treaty-consent records and audit entries; role/permission authorization; privacy limits for Alliance tax reports and member contribution history; the boundary between platform moderation and the owner-reserved `UD-044` expulsion/appeal question.
- **J — Failure and recovery:** insufficient funds or resources; ambiguous or missing membership attribution (the reversible 0% fallback under Open `UD-040`); interrupted turns and retry safety; partial or rejected operations; dissolution and exit with outstanding obligations; recovery paths that never create hidden entitlements.

**Required bidirectional traceability matrix.** The companion must publish one exhaustive, machine-checkable ledger that maps **both directions** between:
- Alliance rule identifiers (`ALL-*`) and their workflow sections;
- the Alliance requirement block `REQ-534`–`REQ-647`, together with the six purpose-limited operational-funding rows `REQ-648`–`REQ-653`;
- the integration rows `AX-01`–`AX-30`;
- the formula-register entries (`F-AL-*` and related) and B-08/B-10/B-12/B-13/B-14 cross-references;
- `D-*` decisions and `DD-*` records that authorize each rule;
- every unresolved decision the workflow touches (`UD-040`–`UD-049`), recorded as an open dependency with its exact state — never resolved by the companion;
- workflow identifiers, acceptance criteria and executable test identifiers.

Every rule, requirement, AX row and formula must appear in at least one workflow; every workflow must cite the rules that govern it; no orphan rows in either direction. Direct, supporting and deferred relationships are classified as in the B-08 ledger, and deferrals name their downstream owner prompt. Compatibility with B-10 (warfare), B-12 (fair play/privacy), B-13 (interface) and B-14 (formulas) is traced by reference, not duplicated.

**Acceptance standard.** The companion is acceptable only when: all ten workflow groups are complete for happy paths, permission failures, edge cases and recovery; the matrix is bidirectional, exhaustive and free of orphan identifiers; every unresolved decision remains Open/Deferred with its owner and is not silently resolved; the specification/implementation boundary is explicit (workflows are specifications, not code, and tests are defined but not executed against a build); and the companion adds no Alliance rule, no NAP coverage or consent rule, no treasury-spending authority and no appeal right. On acceptance it records the deliverable as specified and **not implemented**, leaving production implementation, live-game integration testing and release pending.

**Guardrail.** Register only. Do not execute 09C, do not create `16_alliances_workflows_acceptance.md` in this pass, do not regenerate B-09, and do not repeat 09A research.

---

### Prompt 10 — Warfare, campaigns and postwar settlements

**Purpose.** Design conflict that is strategically meaningful without geographic fronts.

**B-03 carry-in.** A restricted pair cannot attack each other, join the same side or support each other; a reroll is blocked during an active campaign until this prompt defines the forfeit (UD-032); battle history stays attributed to the old nation (B-03 §18).

**Outputs.** War lifecycle; readiness and military costs; campaign objectives and operation types; supply and strategic choice; battle-resolution model; losses and counterplay; victory conditions; ceasefire and settlement framework.

**Must preserve.** Mapless abstract conflict; transparent resolution both sides can read; protection and off-ramps (F-017 prevention); the **D-015** Operations Points model (military-only, one OP regenerated at the P3.7 opening, carried below the cap, non-transferable, reserved at acceptance, consumed at resolution) with its cap, costs and scaling still provisional.

**Sub-prompt register (2026-11-03; 10C completion 2026-11-04).** Prompt 10 is executed as three sub-prompts against one roadmap item: **10A — Politics and War warfare research, evidence, requirements and cross-system integration — COMPLETE (2026-11-03; research/documentation only)**; its canonical deliverable is [`research/10A_politics_and_war_warfare_research.md`](research/10A_politics_and_war_warfare_research.md), which supplies the source register (`WFS-001`…`WFS-040`), findings (`WFR-001`…`WFR-052`), formula evidence (`WFE-01`…`WFE-16`), the P&W-to-Nation-Supremacy classification (`WFC-01`…`WFC-26`), candidate requirements (`WCR-01`…`WCR-44`), open questions (`WFQ-01`…`WFQ-22`) and the 10B/10C handoffs, and **approves no B-10 rule**. **10B — Warfare Foundations and Complete Rules — is COMPLETE at the specification/documentation level (2026-11-03; [§58](06_stage_2_progress_log.md)), corrected by 10B-C ([§59](06_stage_2_progress_log.md)), 10B-C2 ([§60](06_stage_2_progress_log.md)) and 10B-C3 ([§61](06_stage_2_progress_log.md), verified [§62](06_stage_2_progress_log.md))**; its canonical deliverables are [`17_warfare_and_settlements.md`](17_warfare_and_settlements.md) (v1.3, 30 sections, 188 numbered rules plus 42 lettered sub-rules, 25 architecture decisions) and [`17_warfare_formula_register.md`](17_warfare_formula_register.md) (v1.3, 39 formulas, 20 mandatory fields each). **10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence — is COMPLETE at the specification/documentation level (2026-11-04; [§63–§66](06_stage_2_progress_log.md))**; its canonical deliverable is [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md) — 40 workflows (`WFW-001`–`WFW-040`), 60 edge cases (`WFE-001`–`WFE-060`), 124 acceptance tests (120 core plus four class-P supplements) (`WFA-001`–`WFA-124`) in 16 classes, a 50-requirement bidirectional ledger (44 DIRECT / 1 SUPPORTING / 5 DEFERRED / 0 NOT COVERED), all 230 WAR identifiers, 39 formulas, 25 architecture decisions, 34 conflict entries and the D-143 failure-code-gap disclosure; designed, **not executed**. The parent item is **COMPLETE at the specification/documentation level**, and Prompt 11 was next; its **11A** research pass closed ([§67](06_stage_2_progress_log.md)) and its **11B** specification has since closed ([§68](06_stage_2_progress_log.md)); **11C** is complete at the specification/documentation level (log §72). No 10A/10B/10C output is a rule approval, implementation, runtime test or release.

**B-09 Alliance dependency (registered 2026-11-03).** Prompt 10 inherits four attack-prevention layers and must design around them, not restate them: the B-03 restricted-pair ban, the B-08 national treaty/NAP block, the B-09 Alliance NAP for the explicitly consenting covered nations under the separate Alliance-to-Alliance treaty framework authorized by **`D-140`** (`AT-T01` / `AT-E01`), and the B-09 same-Alliance attack ban. Enforcement is **cumulative and server-side at every attack entry point and path** — the War Operations Board, campaign declaration, operation targeting, support actions and any future path — so no entry point can bypass an inherited block. Prompt 10 must define how a membership change, treaty/NAP acceptance or expiry, or an active campaign changes that enforcement, including the turn boundary at which it takes effect; must specify the player-facing explanation for each blocked action; and must make audit records mandatory for every blocked attempt and every override-capable administrative action. It introduces **no new Alliance coverage rule, no new consent rule and no delegation**; the Alliance NAP and ban rules remain B-09's, and `UD-044`/`UD-047` remain owner-reserved.

**Done when.** Two nations can fight a bounded war with a readable outcome, a way to stop, and no infinite one-sided attrition.

---

### Prompt 11 — World events, objectives, rankings and long-term progression

**Sub-prompt register (2026-11-05).** Prompt 11 executes as three sub-prompts against this one roadmap item, mirroring the 07/08/09/10 shape (**D-144** / **DD-192**): **11A — research, benchmarking and design foundations — COMPLETE (2026-11-05) at the research/design-foundations level**, delivering the 35-section report, the comparator source and benchmark register (`11A-RS` 114 rows, `11A-BM` 73 entries) and the integration/risk registers (`11A-INT` 40, `V-01`…`V-18`, `11A-RK` 28, `11A-CR` 30, `11A-OPEN` 16) with `11A-DR` 34 recommendations; **11B — B-11 complete system specifications — COMPLETE at the system-specification level (2026-11-05; §68)**, with canonical `18_world_events_objectives_rankings_progression.md` and its formula register; **11C — B-11 workflows, edge cases and acceptance — COMPLETE at the specification/documentation level (log §72)**. No file was renamed; D-152 confirms the path. **11A approves no rule, formula, number, screen or implementation, allocates no global `REQ-` or `UD-` ID, and closes no owner-reserved decision — `UD-024` stays Deferred.**

**Purpose.** Keep the shared world interesting over months.

**B-03 carry-in.** A new nation is unranked until its first boundary; a reroll removes its current ranking and writes a retirement event; old events stay attributed to the old nation; no first-time reward is transferable (B-03 §18).

**Outputs.** Strategic objectives; world-event framework and timing relative to the turn boundary; achievements; ranking criteria (plural standings, no single dominant ladder); world chronicle; long-term progression; endgame/seasonal concepts if any.

**Guardrail.** No manual content team exists (AP-003): events are systemic, not authored live-ops.

**Done when.** A player returning after a month can see what changed in the world and why.

---

### Prompt 12 — Fair play, player protection, privacy and administration rules

**Purpose.** Turn the security research into explicit game policy.

**Executed split (2026-11-06; D-163 / DD-211; 12A reconciled 2026-11-07; 12B completed 2026-11-07).** Prompt 12 runs in three parts like Prompts 07–11: **12A** — research, evidence, requirements and design foundations (**complete 2026-11-06 and reconciled 2026-11-07**, [log §73](06_stage_2_progress_log.md), log §74; three deliverables under [`research/`](research/12A_fair_play_privacy_moderation_administration_research.md)); **12B** — the B-12 rulebook, formula register, requirement register and acceptance framework at `stage-2/20_fair_play_and_player_protection*.md` (**specification complete at the documentation level 2026-11-07**, log §75; 344 rules, 16 formulas, `REQ-764`–`REQ-869`, D-178…D-187 / DD-226…DD-235); **12C** — workflows, cross-system integration and acceptance (**complete at the specification/documentation level 2026-11-10**, log §85; 10 `FPJ-` journeys, 52 `FPW-` workflows, 100 `FPE-` edge cases, 378 `FPA-` acceptance specifications, the twenty `INT-` contracts reused without a new identifier, 20 `P12C-` gates at 16 PASS / 2 PARTIAL / 2 BLOCKED and **D-188…D-197** / **DD-236…DD-245**). **12B approved no numeric duration, penalty, retention period or owner-reserved decision and implemented no migration, grant, RLS policy, audit trigger or gameplay change; `UD-017` and `UD-040`–`UD-060` are untouched. 12C closed no PARTIAL gate and started no Prompt 13, 14 or 15 work; Prompt 13 remains next, is not started, and needs its own owner authorization (D-002).** The complete original Prompt 12B instruction is permanently archived at [`docs/prompts/prompt_12B_complete_system_specifications.md`](../prompts/prompt_12B_complete_system_specifications.md), indexed in [`docs/prompts/INDEX.md`](../prompts/INDEX.md).

**B-03 carry-in.** Implement the inherited policy: pair restrictions reviewed with least privilege, IP never sufficient for a permanent ban, preservation orders, retention and appeals as specified in B-03 §5.6–§5.10 and §14; the tooling is this prompt's.

**Outputs.** Fair-play policy; new-player protection rules; abuse reporting and moderation workflow; administrative authority boundaries; audit-trail requirements; botting/collusion/multi-account policy; one-account-per-person policy; privacy-conscious enforcement.

**Must preserve.** This is policy, not implementation. No promise of perfect detection; no surveillance posture; the ST-001…020 tests remain unexecuted until a build exists.

**B-09 Alliance dependency (registered 2026-11-03).** Prompt 12 must specify the privacy, authorization and audit rules that the accepted Alliance workflows depend on: operator correction under **DPE-049**; privileged-read auditing under **DPE-054**; confidentiality of Alliance tax reports and tax receipts; who may read a member's contribution history and under which role/permission; retention and access rules for treaty-consent records; and the authorization model for Alliance roles and permissions when an administrative or support action is involved. Audit records must be readable only to authorized roles and must not leak tax or contribution data through moderation tooling. Prompt 12 must also keep the boundary explicit: **platform moderation** (fair play, abuse, account enforcement) is distinct from an **Alliance expulsion and its appeal**, which remains the owner-reserved `UD-044` question. Prompt 12 must not create an Alliance appeal right, must not decide who may expel a member, and must not resolve `UD-044`; it may specify how an existing platform appeal is requested and evidenced without implying an Alliance-specific remedy.

**Done when.** Each prohibited behaviour has a stated rule, a stated consequence, and a stated evidence source — without requiring technical controls that do not exist yet.

---

### Prompt 13 — Interface, screens and player journeys

**Executed split (2026-11-11; D-198).** Prompt 13 runs in two parts like the 07–12 families: **13A — UI research, architecture and design foundations** — COMPLETE at the research/design-foundations level (2026-11-11; [§87](06_stage_2_progress_log.md)), delivering the five canonical documents in row 13 above: the Politics & War primary UI research and benchmark register, the design-principles and architecture document, the 100-screen `SCR-` master inventory and hierarchy, the responsive and design-system foundations, and the UI requirements / open questions / acceptance register; and **13B — screen and component specifications** — next, unauthorized and unstarted, which authors the B-13 rulebook at the path reserved by D-198 and allocates the B-13 requirement block from `REQ-870`. 13A approved no screen as a product commitment, allocated no global `REQ-`/`UD-` row, and changed no rule; its `13A-OQ` register keeps every owner-reserved question open.

**Purpose.** Translate rules into a legible browser experience.

**B-03 carry-in.** The onboarding, reroll-confirmation, shared-network explanation and review surfaces are specified in B-03 §11, §16 and §17; this prompt supplies screens, not new rules.

**Outputs.** Screen inventory; navigation; National Command Center; economy and production screens; politics screens; trade and diplomacy panels; a **restricted Alliance management interface** (not a war room — no military command, no member OP spending, no private war visibility, no shared pool or delegation); the **Nation-owner War Operations Board** (nation-level, owner-only, B-10 visibility); event feed and notifications; critical journeys and UI behaviour specifications.

**War/Alliance boundary (clarified 2026-11-04 by Prompt 10B-C3).** Prompt 13 designs two distinct surfaces and must not merge them: the War Operations Board is the nation owner's B-10 operations surface, showing only that nation's OP balance, reservations, operations and battles; the Alliance interface is management and coordination only. It preserves `AX-18`, `UD-047`, `UD-049`, `REQ-589`–`REQ-591`, `WAR-148` and `WAR-161` — no Alliance military command, no member OP spending or delegation, and no private war visibility between allies. This is a boundary statement, not UI design; Prompt 10C's workflow layer is complete and the Prompt 13 screen work remains unstarted.

**Must preserve.** No map screen; the mapless network view is the world surface; absence-respecting session design.

**Guardrail.** Specifications only — no frontend code in Stage 2.

**B-09 Alliance dependency (registered 2026-11-03).** Prompt 13 must provide screens and journeys for the accepted Alliance rules without adding rules: tax bracket creation and management with separate **Crowns and resource percentages**, member assignment, the effective turn and policy version shown before confirmation, tax history and receipts, and aggregate contribution reports; donations and their receipt record; the four **ARL** categories and the **unavailable operational purposes** with their explanatory failure states; treaty offer, consent and coverage visibility; and clear explanations when an action is blocked by a **NAP** or by the **same-Alliance attack ban**, plus permission-denied states for Alliance roles. Each screen must state which B-09 section governs it. Prompt 13 must **not** design native real-time Alliance chat, voice, or a Discord or other third-party messaging integration; in-game notifications and audit visibility are the supported surface. Privacy limits from Prompt 12 apply to tax reports and member contribution history.

**Done when.** Every Stage 2 rule has a place a player can see and act on it.

---

### Prompt 14 — Numbers, formulas, balance and worked examples

**Purpose.** Bring the systems together numerically and hunt for runaway advantages, exploits and dead ends.

**B-03 carry-in.** Every number B-03 leaves open is listed in its §21.2 parameter table; label and test each one, and treat none as approved (B-03 §18).

**Outputs.** Formula register (unit, rounding, timing assumption per formula); initial parameter set; representative turn calculations; economic and military worked examples; exploit and edge-case scenarios; cross-system balance analysis; explicit list of values needing simulation or playtesting.

**Must preserve.** Four labels, never blurred: owner-approved value, provisional value, design proposal, needs-playtesting. The Operations Points *model* is approved (D-015); every OP number and every other provisional mechanic stays provisional.

**B-09 Alliance dependency (registered 2026-11-03).** Prompt 14 must carry the accepted Alliance formulas into one consistent numerical model: automatic per-turn production tax at player-authored **0–100%** rates; separate **Crowns and resource** rate schedules; cumulative fractional rounding stated per asset and per turn; per-Alliance assignment for a nation in multiple Alliances, including the reversible **protective fallback** when attribution is ambiguous (Open `UD-040`); the interaction of a **100% Crowns tax** with maintenance; **resource production-chain accounting** after tax; **ARL** receipt and credit-only accounting; and the cost dependencies of purpose-limited **operational funding** under the narrow `UD-045` authorization while `UD-046` remains Open. Every formula cites the [B-09 formula register](16_alliances_formula_register.md) and labels its value. Prompt 14 introduces **no unsupported capacity, storage or fee assumption**, does **not reduce the tax ceiling**, and does **not resolve `UD-040` or `UD-046`**; a formula that would require either decision records the dependency and the provisional branch.

**Done when.** A reader can compute one turn by hand for a sample nation, and every number is labelled with its status.

---

### Prompt 15 — Assemble and verify the Master Game Design Bible

**Purpose.** Compile the approved designs into one rulebook and perform **one** bounded review.

**B-03 carry-in.** Verify that B-03 §18's contracts are reflected by their owner prompts and that the account, pair and reroll rules are not duplicated inconsistently.

**B-09 Alliance dependency (registered 2026-11-03).** Prompt 15 must assemble the accepted B-09 rulebook, its **09C workflow-and-acceptance companion** (`16_alliances_workflows_acceptance.md`), and the Alliance interactions owned by B-10 (warfare attack prevention), B-12 (privacy, security and audit), B-13 (Alliance journeys) and B-14 (Alliance formulas), inside the existing **B-01–B-19** scope. It keeps **one authoritative source per rule family**: B-09 for Alliance rules, its formula register for numbers, its integration contracts for cross-system obligations and the 09C companion for workflows and acceptance. It cross-references rather than restates, verifies that the same-Alliance ban and NAP are enforced cumulatively from B-10, that Alliance tax/contribution privacy is consistent from B-12 and that interface journeys match B-13, and it preserves the specification/implementation distinction: the assembled Bible states rules, not code; acceptance remains at the specification level; production implementation, integration testing and release remain later-stage work; and `UD-040`–`UD-049` stay open exactly as recorded.

**Outputs.** Completed Bible with a single authoritative entry point; requirements traceability report; cross-system consistency findings; unresolved decisions and accepted risks; balance assumptions deferred to testing; a Stage 2 completion decision; updated continuity files; a recommendation for the next official stage.

**Bounded completion rule.** Stage 2 may close when the core loop and major systems are coherently specified, cross-system interactions are documented, requirements trace to design sections, formulas/units/timing are internally consistent, provisional decisions and open questions are explicitly recorded, remaining balance work is assigned to simulation/playtesting, and one entry point exists. It may **not** be extended because playtesting or implementation has not happened.

**May not claim.** Implementation, production security, live balance, or launch readiness. Those are later stages.

---

## 4. What Stage 2 must not do

- Implement the game, write frontend or backend game code, or apply production database migrations.
- Change hosting resources or deploy anything.
- Repeat Stage 1 research without a documented material gap.
- Repeat the Stage 3 hosting experiments; their evidence stands.
- Introduce a geographic map, alter the turn cadence, or change the one-account-per-person requirement.
- Present a provisional value as approved, or re-open a recorded decision (D-015 above all) without new evidence.
- Call a documented formula "balanced".
- Stay open only because future simulation remains.

## 5. When something is missing

Classify it, then continue:

1. **Blocking design decision** — no coherent rule can be written without it. Ask the owner, with concrete options.
2. **Provisional design choice** — write the proposal, label it, continue.
3. **Playtesting or simulation item** — specify the rule, register the value as needing evidence.
4. **Implementation-stage detail** — define behaviour now, defer the mechanism.
5. **Accepted carry-forward risk** — record it, defer it, do not block.

Ask the owner only for case 1. Everything else is documentation work.
