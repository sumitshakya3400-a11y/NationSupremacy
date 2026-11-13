# Stage 2 progress log

**Official stage:** Stage 2 — Create the Master Game Design Bible ([ROADMAP](../ROADMAP.md))
**Last updated:** 2026-11-12 — **Prompt 13A-C1 (§88) — bounded semantic cross-reference, Politics & War research-evidence, validator, QA-reporting and acceptance reconciliation of Prompt 13A — is COMPLETE at the documentation-correction level:** semantic citations were reconciled across all five `research/13A_*.md` deliverables and `DECISIONS.md` (`D-201`–`D-203`), removing invalid `BP-035`; `13A-FND-026`, `13A-FND-031` (`Alliance` + `Color` text columns present; CSS swatch redundancy unverified) and `13A-FND-032` (bounded to unauthenticated GET shell fallback) plus dependent `BP`/`DR` entries were restricted to observed evidence; [`13A_validate_ui_foundations.py`](../qa_backups/13A_validate_ui_foundations.py) was upgraded to **34 checks** (`13A-33` semantic cross-reference rules, `13A-34` research-evidence alignment) with **29 regression self-tests**; `§87.5`'s inaccurate `test_09B` closing statement was corrected; CRLF status was verified clean (`5406c1f` vs `ec8662a`: 0 CRLF-only files in diff, clean working tree); **`P13A-10` remains PARTIAL** (**23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED**); and **Prompt 13A has NOT received owner acceptance.** Earlier 2026-11-11 baseline: **Prompt 12C-FINAL-C1 (§86) — controlled status reconciliation, conflict-marker remediation and final documentation acceptance — is COMPLETE: 117 committed merge-conflict hunks in 25 files were resolved to the owner-authorized main-line content, the single authoritative B-12 current-status entry was restored, the eleven previously unparseable QA scripts parse again and ten of them run (the eleventh, `12A_sync_docs.py`, is a bulk documentation-rewriting tool verified by syntax only and deliberately not executed as a repair step — see §86.4); all 32 scripts under `docs/qa_backups/` parse, `12B_validate_b12.py` reports 87/87 with its code unmodified, no decision identifier was minted and the canonical registers stay at **`D-001…D-197` / `DD-001…DD-245`**, with `D-197` and `DD-245` carrying dated follow-up annotations only. *(This clause previously misreported a `D-200 / DD-248` frontier with `D-198…D-200` and `DD-246…DD-248` recorded; that claim was unsupported by both registers and is removed by Prompt 12C-FINAL-C1-R1, which re-verified 197 contiguous `D-` rows ending at `D-197` and 245 contiguous `DD-` rows ending at `DD-245`.)* R8 remains DEFERRED BY OWNER, 12B-C1 remains NOT CLOSED, and no PARTIAL or BLOCKED gate was closed. The Prompt 12C (§85) — the B-12 operational workflows, cross-system integration, edge cases and acceptance specification — is COMPLETE at the documentation level:** 10 `FPJ-` journeys, 52 `FPW-` workflows, the twenty `INT-` contracts reused with none added, 100 `FPE-` edge cases, 378 `FPA-` acceptance specifications with none executed, the 106-row B-12 traceability ledger with 0 orphans, 20 `P12C-` gates at 16 PASS / 2 PARTIAL / 2 BLOCKED, decisions **D-188…D-197 / DD-236…DD-245** and a 24-check validator. **No rule, requirement, contract identifier, formula, parameter or number was added; `P12B-14`, `P12B-16` and `P12B-23` remain PARTIAL, the seven 12A PARTIAL gates remain PARTIAL, R8 remains DEFERRED BY OWNER and 12B-C1 remains NOT CLOSED. The pre-existing committed merge-conflict markers — 117 hunks in 25 files, 14 Markdown documents and 11 Python QA scripts, which Prompt 12C had recorded approximately as nine documents and twelve scripts — were carried there as a baseline limitation and have since been resolved by the §86 pass named at the head of this line.** **Prompt 12B-C1-R8-D (§84) records the owner's formal deferral of R8: R7's implementation is retained at 87/87 checks, 59/59 positive and 153/153 negative fixtures with the 23/23 subprocess mutation audit, its independent acceptance is NOT accepted, the eight R6 reproductions remain rejected, and the five bypass classes reported by the independent audit of Project X (77) are preserved as known residual weaknesses; no validator code was modified. 12B-C1 remains NOT CLOSED, the three PARTIAL gates are unchanged, and Prompt 12C was not authorized at that close — it has since been authorized, executed as §85 and reconciled as §86.** The 2026-11-07 record follows for history (its counts were superseded by R1–R7): **Prompt 12B — B-12 fair play, privacy, moderation and administration complete system specifications — is complete at the specification/documentation level (§75): four documents plus a validator, 344 rules, 16 formulas, `REQ-764`–`REQ-869`, D-178…D-187 / DD-226…DD-235, 26 gates at 23 PASS / 3 PARTIAL, validator 62/62 with 12/12 positive and 22/22 negative fixtures, and no migration, grant, audit control or gameplay change. Prompt 12C is next and not authorized.** The 2026-11-06 Prompt 11A record follows for history: (**Prompt 11A — World events, objectives, rankings and long-term national progression: research, benchmarking and design foundations — is complete at the research/design-foundations level (§67); its canonical deliverable is [`research/11A_world_events_objectives_rankings_progression_research.md`](research/11A_world_events_objectives_rankings_progression_research.md) with two companion registers; Prompt 11B is complete at the system-specification level (2026-11-05; log §68); the 11B-C2 integrity correction is applied and locally verified (2026-11-05; log §70; original 52 criteria preserved and matched, 52/52 gate rows PASS with 61 separate checks); independent acceptance was recorded by C3 on 2026-11-05, and Prompt 11C is complete at the specification/documentation level (log §72); Prompt 12A is complete at the research/design-foundations level (log §73); Prompt 12B was next at that time and is complete at the specification/documentation level (§75). The 2026-11-04 record follows: **Prompt 10C — Warfare workflows, cross-system integration, acceptance and final pass — is complete at the specification/documentation level (§63); its canonical deliverable is [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md); Prompt 11 was next; Prompt 10B (§58) and its correction passes 10B-C/10B-C2/10B-C3/10B-C4 (§59–§62) remain verified; Prompt 10A research (§56) and its correction (§57) remain complete; Stage 2 not complete.** Earlier on the same day: **Prompt 09C complete at the specification/documentation level — §53, with the §54 and §55 correction passes**. Earlier: **Prompt 06B complete**; the Prompt 06B micro-corrections in §12–§15, the consolidation audit in §16, the cross-document reconciliation in §17, the publication/catch-up correction in §18, the handoff-timing clarification in §19, the Prompt 07A research in §20, the Prompt 07B market foundations in §21, the **Prompt 07B status reconciliation and sub-prompt guard in §22**, the **Prompt 07C workflows, acceptance and product approval in §23**, the **Prompt 08A diplomacy research, evidence and requirements in §24**, the **Prompt 08B diplomacy foundations in §25**, the **Prompt 08B-C corrections in §26** the **Prompt 08B-D formula and handoff corrections in §27**, the **Prompt 08C workflows and acceptance in §28**, the **08C-C acceptance-matrix and reference corrections in §29**, the **08C-D semantic-coverage, traceability and replay corrections in §30** and the **08C-E bidirectional traceability and acceptance closure in §31** the **Prompt 09A alliance research and requirements baseline in §32**, the **Prompt 09A-C alliance corrections and semantic audit in §33** the **Prompt 09A-D final alliance treasury storage traceability correction in §34**, the **Prompt 09A-E AX-08 wording and treasury-policy correction in §35**, the **Prompt 09A-F final status reconciliation and acceptance closure in §36**, the **Prompt 09B alliance foundations in §37**, the **Prompt 09B-C foundations correction in §38**, the **Prompt 09B-D governance recovery, owner authority restoration, and semantic validation in §39**, the **Prompt 09B-E owner-reserved authority, diplomatic non-delegation, treasury neutrality, AX reconciliation and validator rebuild in §40**, the **Prompt 09B-F final authority audit, semantic validation and project-wide consistency audit in §41**, the **Prompt 09B-G validator hardening and adversarial regression in §42**, the **Prompt 09B-H negative-polarity entitlement correction in §43**, the **Prompt 09B-I correction in §44**, the **Prompt 09B-J correction in §45**, the **Prompt 09B-K final correction in §46**, the **Prompt 09B-L final consolidated correction in §47**, the **Prompt 09B-M final closeout in §48**, the **Prompt 09B-N recourse and former-member correction in §49**, the **Prompt 09B-O procedural false-negative correction in §50**, the **Prompt 09B-P dismissal, grievance and redress correction in §51**, and the **Phase 09B acceptance record in §52**) and the **Prompt 10A warfare research checkpoint in §56**

**Current task:** **Prompt 13B — complete screen and component specifications — is COMPLETE at the specification/documentation level (2026-11-13; §91): three canonical B-13 documents, 100 A–K screen specifications, 90 `UI-CMP` components, 8 overlays, `REQ-870`…`REQ-1089`, D-206…D-219 / DD-254…DD-267, Matrices A–C and the documentation impact register. No frontend, screen, component, migration or runtime test exists. The next action is the owner’s review of the Prompt 13B package; Prompt 13C is next but unauthorized and unstarted. R8 remains DEFERRED BY OWNER (§84): no further validator-hardening work is authorized.**

**Current status:** **Prompt 09C — Alliance workflows, edge cases, acceptance matrix and release-gate evidence — is COMPLETE at the specification/documentation level (2026-11-03; §53, corrected by §54 and §55).** The canonical deliverable is `docs/stage-2/16_alliances_workflows_acceptance.md` (49 workflows, 65 edge cases, 132 acceptance tests, exhaustive traceability). Completion is documentation-only: no gameplay code, runtime test or deployment exists. **Prompt 10A — Politics and War warfare research, evidence, requirements and cross-system integration — is complete (2026-11-03, §56), research/documentation only; Prompt 10B — Warfare Foundations and Complete Rules — is complete at the specification/documentation level (§58) with its correction passes 10B-C/10B-C2/10B-C3/10B-C4 verified (§59–§62); Prompt 10C — Warfare workflows, cross-system integration, acceptance and final pass — is complete at the specification/documentation level (§63); **Prompt 11A — world events, objectives, rankings and long-term national progression research and design foundations — is complete at the research/design-foundations level (2026-11-05; §67)**, Prompt 11B is complete at the system-specification level (2026-11-05; log §68), Prompt 11C is complete at the specification/documentation level (2026-11-06; §72), Prompt 12A is complete at the research/design-foundations level (2026-11-06; §73), and Prompt 12B is complete at the specification/documentation level (§75); Prompt 12C is complete at the specification/documentation level (§85) and its 12C-FINAL-C1 reconciliation pass is complete (§86); Prompt 11's parent awaits the owner's acceptance of its PARTIAL verdict; Stage 2 is not complete.** **Phase 09B Alliance specification and documentation: ACCEPTED.** Acceptance is at the specification/documentation level (D-142 / DD-165), not production implementation, live-game integration testing or release. Owner-reserved decisions remain open: `UD-040`–`UD-049` are **Open / Yes — owner**, with only the partial authorizations recorded by `D-140` and `D-141`; `UD-039` remains Resolved by `D-137` with its no-object component amended in part. Global Trade remains preserved under `D-122` with G-1–G-6 unchanged. Prompt 09A is accepted after Prompt 09A-F (§32–§36); Prompt 09B foundations were corrected and accepted under Prompts 09B-D through 09B-P (§37–§52; [09B-F audit](16_alliances_project_wide_consistency_audit.md)); Prompt 09B-L reconciled automatic Alliance taxation, the ARL receipt/accounting and operational-funding boundary, the `AT-E00`/`AT-E01` effect catalogue and the 30-contract set; Prompts 09B-M through 09B-P closed the remaining corrections. No new 09B redesign or research was authorized or performed.


---

## 1. Objective

Produce the authoritative game-design specification for Nation Supremacy: how the game works, what players can do, which rules and formulas resolve outcomes, how systems interact, and how the player experience behaves.

Stage 2 writes **specifications only**. No game code, no migrations, no deployments, no hosting changes. This log tracks the fifteen prompts and the work they produce; the project-wide tracker remains [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md).

---

## 2. Prompt status

| # | Prompt | Deliverable(s) | Status | Date |
|---|---|---|---|---|
| 01 | Bible structure, requirements traceability, decision registers, work plan | [`02_outline`](02_master_game_design_bible_outline.md), [`03_traceability`](03_requirements_traceability.md), [`04_decisions`](04_approved_and_provisional_decisions.md), [`05_unresolved`](05_unresolved_design_decisions.md), this log | **Complete** | 2026-10-23 |
| 02 | Core gameplay loop, symbolic world and turn system | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](07_core_gameplay_loop_symbolic_world_and_turn_system.md) | **Complete** | 2026-10-23 |
| 03 | Account onboarding, nation creation and progression | [`09_account_onboarding_nation_creation_and_progression.md`](09_account_onboarding_nation_creation_and_progression.md) — the `08_…` name in the original register belongs to the decision-closure audit | **Complete** (specification only) | 2026-10-24 |
| 04 | Economy, resources, treasury and national finances | [`10_economy_resources_treasury_and_finances.md`](10_economy_resources_treasury_and_finances.md), [`10_economic_formula_and_balance_register.md`](10_economic_formula_and_balance_register.md), [`research/04_politics_and_war_economy_research.md`](research/04_politics_and_war_economy_research.md) | **Complete** (specification only) | 2026-10-24 |
| 05 | Cities, infrastructure, production and research | [`11_cities_infrastructure_production_and_research.md`](11_cities_infrastructure_production_and_research.md), [`11_city_infrastructure_production_and_research_formula_register.md`](11_city_infrastructure_production_and_research_formula_register.md), [`research/05_politics_and_war_city_infrastructure_production_research.md`](research/05_politics_and_war_city_infrastructure_production_research.md) | **Complete** (specification only) | 2026-10-25 |
| 06A | Population and domestic-politics foundation | [`12_population_and_domestic_politics.md`](12_population_and_domestic_politics.md), [formula register](12_population_and_domestic_politics_formula_register.md), [P&W research](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md) | **Complete** (design only) | 2026-10-25 |
| 06B | Elections, campaigns, retention, crises and unrest | extends B-06 and its register | **Complete** (with the 06B micro-corrections, 2026-10-28) | 2026-10-25 |
| 07 | Trade and market systems — **07A** research, **07B** foundations, **07C** workflows and acceptance | **07A:** [`research/07A_politics_and_war_market_research.md`](research/07A_politics_and_war_market_research.md). **07B:** [`13_trade_and_markets.md`](13_trade_and_markets.md) **v1.1** + [`13_trade_and_markets_formula_register.md`](13_trade_and_markets_formula_register.md) **v1.1**. **07C:** [`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md) | **Complete** (2026-10-29) — 07A/07B 2026-10-28; 07C workflows, acceptance and product approval (D-122); [log §20–§23](06_stage_2_progress_log.md) |
| 08 | Diplomacy between nations — **08A** research and requirements, **08B** foundations, **08C** workflows and acceptance | **08A:** [`research/08A_diplomacy_research.md`](research/08A_diplomacy_research.md). **08B:** [`15_diplomacy.md`](15_diplomacy.md) v1.2 + [formula register](15_diplomacy_formula_register.md) v1.2 (08B-C corrections in §26; 08B-D in §27). **08C:** [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md) v1.3, corrected by 08C-C, 08C-D and 08C-E | **08A complete** (research only); **08B complete** (designed; no implementation); **08C complete** (2026-10-30; 30 workflows, 54 edge cases, **88 tests**, 52 covered / 2 partial; 118-row exhaustive ledger = 101 direct + 16 supporting + 1 deferred; designed, not executed); **08C-C correction complete** (§29); **08C-D correction complete** (§30); **08C-E correction complete** (§31); **Prompt 08 complete** | 2026-10-30 |
| 09 | Alliance system and alliance management | `16_alliances.md` | **ACCEPTED — specification/documentation level (D-142 / DD-165)** — Prompt 09A accepted after 09A-F; Prompts 09B through 09B-P completed the Alliance specification and its audited corrections; acceptance does not imply production implementation, live-game integration testing or release, and UD-040–UD-049 remain Open. Prompt 09C: complete at the specification/documentation level (2026-11-03; §53); Prompt 10A: complete (research/documentation only; §56); Prompt 10B: complete at the specification/documentation level (§58), corrected by §59–§62; Prompt 10C: complete at the specification/documentation level (2026-11-04; §63). | §32–§36, §37–§55 |
| 10 | Warfare, campaigns and postwar settlements | `17_warfare_and_settlements.md`; **10C companion:** [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md) | **COMPLETE at the specification/documentation level — Prompt 10C complete (2026-11-04; §63, corrections §64–§65)** ([B-10 rulebook](17_warfare_and_settlements.md) v1.3 + [formula register](17_warfare_formula_register.md) v1.3; 30 sections, 188 numbered rules plus 42 lettered sub-rules, 39 formulas, 25 architecture decisions; 10C adds 40 workflows, 60 edge cases, 124 acceptance tests in 16 classes, a 50-requirement bidirectional ledger, 26 contiguous WAR ranges, the D-143 failure-code-gap disclosure and 13 integration rows; all 10A candidates dispositioned; `UD-032` resolved as Option A; documentation only — no code, no runtime test, no release); 10A research complete (§56) and correction (§57); 10B specification complete at the specification/documentation level (§58) with the 10B-C/10B-C2/10B-C3/10B-C4 corrections (§59–§62); 10C §17 records the P10C-01…P10C-44 gates; Prompt 11 complete at the specification/documentation level (11C, §72); Prompt 12A complete at the research/design-foundations level (§73); Prompt 12B complete at the specification/documentation level (§75); Prompt 12C complete at the specification/documentation level (§85–§86) and owner-accepted on 2026-11-11; Prompt 13A complete at the research/design-foundations level (§87); Prompt 13C next, not started and pending owner authorization. | §56–§65 |
| 11 | World events, objectives, rankings and long-term progression — **11A** research and design foundations, **11B** specification, **11C** workflows and acceptance — **11C complete at the specification/documentation level (§72); the parent awaits owner acceptance of its PARTIAL verdict; Prompt 12B authorization is pending** | [`18_world_events_objectives_rankings_progression.md`](18_world_events_objectives_rankings_progression.md) (723 `WEP-` rules) + [`18_world_events_objectives_rankings_progression_formula_register.md`](18_world_events_objectives_rankings_progression_formula_register.md) (50 `F-WEP-` formulas, 17 contracts, 40 failure codes, 50 audit events); **11A deliverables:** [`research/11A_world_events_objectives_rankings_progression_research.md`](research/11A_world_events_objectives_rankings_progression_research.md), [`research/11A_comparator_sources_and_benchmarks.md`](research/11A_comparator_sources_and_benchmarks.md), [`research/11A_integration_and_risk_registers.md`](research/11A_integration_and_risk_registers.md) | **11B COMPLETE at the system-specification level** (2026-11-05; §68) — specification and documentation only; 60 requirements REQ-704…REQ-763, D-152…D-161 / DD-200–DD-209, UD-024 resolved, UD-050/UD-051 open; **11C COMPLETE at the specification/documentation level** (2026-11-06; §72); **12A complete at the research/design-foundations level (§73); Prompt 12B next and not started** | 2026-11-06 |
| 12 | Fair play, player protection, privacy and administration — **12A** research and design foundations, **12B** specification, **12C** workflows and acceptance | `20_fair_play_and_player_protection.md` plus its formula, requirement and acceptance companions | **12A complete at the research/design-foundations level**; **12B complete at the specification/documentation level**; **R7 retained at 87/87, 59/59, 153/153 and 23/23 but NOT independently accepted; the five Project X (77) bypass classes are known residual weaknesses; R8 is DEFERRED BY OWNER (§84)**; **12C complete at the specification/documentation level (§85) with its 12C-FINAL-C1 reconciliation pass (§86) and owner-accepted on 2026-11-11; 13A complete at the research/design-foundations level (§87); 13B next, unauthorized and not started** | 2026-11-10 |
| 13 | Interface, screens and player journeys — **13A** research, architecture and design foundations; **13B** screen and component specifications | `21_interface_and_player_journeys.md` (reserved by D-198; 13A's five deliverables are under [`research/`](research/13A_politics_and_war_ui_research.md)) | **13A complete at the research/design-foundations level (2026-11-11; §87), reconciled by Prompt 13A-C1 (2026-11-12; §88; NOT owner-accepted; `P13A-10` preserved PARTIAL at 23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED). 13B is next — not authorized and not started.** | — |
| 14 | Numbers, formulas, balance and worked examples | `22_formulas_and_balance.md` (moved by D-198) | Pending | — |
| 15 | Assemble and verify the Bible | `23_master_game_design_bible.md`, `24_stage_2_completion_report.md` (moved by D-198) | Pending | — |

Target filenames are guidance from the register; a prompt may create fewer or differently named documents if it says why. It may not skip a required output. **The numeric prefixes in rows 04–15 were planned before B-02 (`07_`) and B-03 (`09_`) were written; each later prompt confirms its own path before writing, and the actual path is what the outline and this log record.**

---

## 3. What Prompt 01 produced

| Deliverable | Content | Status |
|---|---|---|
| Bible outline | 19 parts (`B-01`…`B-19`), each with purpose, authoritative document, prompt, prerequisites, validation and status; authority map; change control; assembly plan | Draft — structure only, no gameplay rules |
| Requirements tracker | 47 requirements: 39 inherited unchanged from Report 09 §12 + 8 new (identity, mapless world, delivery, architecture, scheduler, account policy, two continuity rules); statuses, sections, prompts, dependencies, validation | Draft — 12 approved, 25 provisional, 8 open, 2 deferred |
| Decision register | D-001…D-013 summarised for design use; 20 design positions (`DD-001`…`DD-020`) with 6 approved, 13 provisional, 1 deferred | Draft |
| Unresolved register | 24 questions (`UD-001`…`UD-024`) with blocking classes, owners, prompts; 3 class A (each scoped to its own prompt) | Draft |
| This log | Prompt status, dependency plan, validation record | — |

**Decisions made by this prompt:** none that require owner approval. Two project rules were applied, not created: one authority per rule family, and no document may claim implementation, security or balance as proven (REQ-046/REQ-047).

### 3.2 What Prompt 02 produced

| Deliverable | Content | Status |
|---|---|---|
| B-02 specification | [07_core_gameplay_loop_symbolic_world_and_turn_system.md](07_core_gameplay_loop_symbolic_world_and_turn_system.md) — 31 sections, 97 numbered rules: core loop, three time scales, feedback contract, symbolic-world entities and edges, membership and identity, relationship/visibility model, slot clock and boundary semantics, lifecycle states, P0–P7 phases, published ordering catalogue, simultaneity and conflict rules, action lifecycle with failure codes, cancellation windows, reservation model, consistency guarantees, recovery, inactivity and fairness, reports and history, subsystem contract, ten worked examples | **Draft** — B-02's authoritative document |
| Requirements | 13 new (`REQ-048`…`REQ-060`); `REQ-017` moved Open → Provisional; totals **at Prompt 02**: 60 (12 approved / 39 provisional / 7 open / 2 deferred) | Updated |
| Decision register | 12 new design positions (`DD-021`…`DD-032`); `DD-010`/`011`/`012`/`013` marked as used by this prompt; totals now 32 (6 approved / 24 provisional / 1 explicit-provisional / 1 deferred) | Updated |
| Unresolved register | `UD-003` **resolved**; `UD-004` **partially resolved** (volume); 6 new entries (`UD-025`…`UD-030`); totals now 30 (29 active + 1 resolved) | Updated |
| Bible outline | B-02 marked **Draft** with its authoritative document; numbering corrected (`07`–`19` subsystem docs, `20` entry point, `21` completion report) | Updated |

**Resolved by this prompt:** UD-003 (deterministic ordering catalogue, §14) and UD-004's volume half (one bounded digest row per nation-turn, §23). **Raised:** UD-025 dormant nations, UD-026 sharding, UD-027 aggregate threshold, UD-028 failed-turn treatment, UD-029 pending diplomatic visibility, UD-030 income-vs-upkeep order. **Still provisional at Prompt 02:** D-004/DD-019 Operations Points — no action currency was introduced; *D-015 superseded D-004 later the same day and D-026/027/028 resolved UD-004/027/028, as §5.1d records.*

**Decisions made by this prompt:** no owner approval. The 12 new design positions are provisional; none is a game rule until the owner records a decision (D-003).

---

## 4. Prompt dependency and work plan

### 4.1 The chain

```
P02 core loop + turn system
 ├── P03 accounts, nation creation, progression
 ├── P04 economy, treasury, resources
 │    ├── P05 cities, infrastructure, production, research
 │    │    └── P06 population + domestic politics
 │    └── P07 trade + markets
 │         └── P08 diplomacy
 │              └── P09 alliances
 │                   └── P10 warfare + settlements
 ├── P11 world events, objectives, rankings, progression
 └── P12 fair play, protection, privacy, administration
      └── P13 interface, screens, player journeys
           └── P14 numbers, formulas, balance, worked examples
                └── P15 assemble and verify
```

### 4.2 Why the order is what it is

- **P02 came first** because every other system resolves at the boundary. Its ordering catalogue is the spine: it is now published ([07 §14](07_core_gameplay_loop_symbolic_world_and_turn_system.md)), so later prompts inherit an order instead of inventing one. UD-003 is resolved.
- **P03 before P04** because starting resources and nation identity are economy inputs; the economy cannot conserve what it cannot initialise.
- **P04 before P05–P07** because production, upgrades and trades all move treasury and material values under the conservation identity.
- **P05 before P06** because domestic policy modifies productive capacity; defining policy first would invent effects with no target.
- **P07 before P08/P09** because treaties and alliances act on tradeable value; alliance pools (if any) are value containers.
- **P08 before P09** because alliance diplomacy aggregates bilateral relations.
- **P10 after P04–P09** because war consumes readiness, materials and reputation, and its settlements touch diplomacy.
- **P11 after P02/P04/P10** because events and rankings must observe a world that already resolves, produces and fights.
- **P12 after the systems it governs** — you cannot write abuse policy for rules that do not exist.
- **P13 after the rules**, because the screens display them; a screen specified earlier would encode guesses.
- **P14 after all mechanics**, because formulas need targets; writing them earlier would fabricate them.
- **P15 last**, by definition.

### 4.3 Cross-system checkpoints

| Checkpoint | After | Must be true |
|---|---|---|
| Timing consistency | P02 | Every later subsystem uses the three-class timing contract and the ordering catalogue |
| Conservation | P04/P05/P07 | New value flows are added to the C1–C4 ledger, not outside it |
| Reputation routing | P08/P09/P10 | Acts route to one primary register (SYS-013 discipline) |
| Abuse coverage | P12 | Each P04–P11 mechanic names its abuse case |
| Legibility | P13 | Every rule has a surface; the digest explains every boundary effect |
| Numeric labelling | P14 | Every value carries one of: owner-approved, provisional, proposal, needs-testing |

A later prompt that finds a contradiction in an earlier document must fix the earlier document and record the change here — not paper over it locally.

### 4.4 Rules for every prompt

Read the four continuity files, the roadmap, the Bible material already written and both registers first. Update the authoritative document rather than creating a parallel one. Record what was actually validated. Do not begin the next prompt.

---

## 5. Validation record

### 5.1 Checks run for Prompt 01

| Check | Command | Result |
|---|---|---|
| Document/continuity validator | `py docs/qa_backups/09_validate.py` | **184/184 checks passed — ALL CHECKS PASSED** (175 before the 2026-10-23 micro-correction added the next-action checks) |
| Cross-file validator | `py docs/qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** (0 failures) |
| Requirement ID uniqueness and count | validator check over `03_requirements_traceability.md` | **PASS** — REQ-001…REQ-047, in order, no duplicate, every row assigned a prompt |
| Bible outline completeness (19 parts, entry point) | validator check over `02_master_game_design_bible_outline.md` | **PASS** — B-01…B-19 in order; entry point named |
| Register consistency (D-004 provisional **at Prompt 01**; D-013 present) | validator check over `04`/`DECISIONS.md` | **PASS at that snapshot** — DD-001…DD-020; Operations Points was still explicitly Provisional then; **D-004 was superseded later the same day by D-015**; D-013 reconciled |
| Unresolved-register classes and owners | validator check over `05_unresolved_design_decisions.md` | **PASS** — UD-001…UD-024, every row classed |
| Continuity agreement *(at Prompt 01 completion; superseded by the Prompt 02 row below)* | validator STATUS-block check across the three continuity files | **PASS then** — `stage_1: CLOSED`, `stage_2: IN PROGRESS`, `stage_2_next_prompt: 02` in all three |
| Stale next-action detector | `py docs/qa_backups/test_next_action.py` (stdlib `unittest`, 8 tests) | **OK** — a current field naming prompt 1 is rejected; labelled history, a plain mention and "Prompt 10" are accepted; the real continuity set reports no stale statement |
| Stage 2 handoff and progress-log next action | validator sections over `stage-2/00` §10 and `stage-2/06` header | **PASS** — both name Prompt 02; the current-action scan finds nothing stale |
| Negative tests of the new checks | mutation, then restore, then re-run | **PASS** — a duplicated REQ ID, a dropped DD row and a stale next-prompt value of 01 were each detected, then the clean state re-validated |

*The counts below are the Prompt 02-era state, kept for the record. The current counts are in §5.1c.*

**Counts asserted against the files, not copied from prose (after Prompt 02):** 60 requirements (12 approved / 39 provisional / 7 open / 2 deferred), 32 design decisions (6 approved / 24 provisional / 1 explicitly provisional / 1 deferred), 30 unresolved questions (29 active: A2 / B13 / C3 / D8 / E3, plus UD-003 resolved).

### 5.1b Checks run for Prompt 02

| Check | Command / method | Observed result |
|---|---|---|
| Document and continuity validator | `python docs/qa_backups/09_validate.py` | **196/196 checks passed — ALL CHECKS PASSED** |
| Cross-file validator | `python docs/qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| Stale next-action regression test | `python docs/qa_backups/test_next_action.py` | **10 tests, OK** — an earlier prompt named as current is rejected; history is accepted; the real continuity set is clean |
| B-02 structure | validator over `07_…` | **PASS** — §1–§31 in order; TR-001…TR-097 contiguous; P0–P7 and the published catalogue present |
| Register consistency | validators over `03`/`04`/`05` | **PASS** — 60 requirements, 32 design positions, 30 unresolved rows; UD-003 resolved; UD-004 partially resolved |
| Boundary rule coherence | manual comparison of TR-029 with Examples A/B and the report sample | **PASS** — one rule, no exception; the illustrative report's arithmetic was corrected during review (40 + 18 + 2 = 60) |
| Negative test | mutation → validators → restore → re-run | **PASS** — setting the index row's current action to Prompt 02 made both validators fail (exit 1); restore returned 196/196 and ALL CHECKS PASSED |
| What was **not** run | — | No turn was resolved, no simulation of the ordering catalogue, no load or scheduler test, no playtest. The design is unvalidated in operation |

### 5.1c Correction and autonomous-decision pass (2026-10-23, after Prompt 02)

A ZIP audit of the Prompt 01–02 output found four stale index descriptions, a historical handoff paragraph that read as current, and a class of pending items still phrased as owner questions. The pass fixed the continuity text, adopted the permanent decision policy (**D-014**, [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md)), and recorded nine design decisions (D-015…D-023) closing nine pending questions — a tenth unresolved row (UD-003) had already been resolved by Prompt 02 itself. No Prompt 03 deliverable was started.

| Decision | Resolved | What changed in the rules or registers |
|---|---|---|
| D-014 | — | Autonomous decision policy adopted: Category A/B/C/D, research record, when stopping is correct |
| D-015 | UD-018 (and D-004) | Operations Points approved as a model: military-only pool, refilled to cap, non-transferable, reserved at acceptance, consumed at resolution; numbers provisional |
| D-016 | UD-002 | Trade offers do not reserve; reservation begins at acceptance with atomic settlement |
| D-017 | UD-008 | Trade terms visible only to the two parties; aggregates behind gates and the UD-027 threshold |
| D-018 | UD-014 | One account per person; multi-accounting prohibited; proportionate review-first enforcement |
| D-019 | UD-030 | Within P3, income/production applies before mandatory upkeep |
| D-020 | UD-001 | CP/FPB scope taxonomy adopted; Stage 2 completion is neither |
| D-021 | UD-020 | No newcomer catch-up acceleration at launch |
| D-022 | UD-021 | Free-tier limit posture: cap, degrade, pause signups; no auto-paid upgrade, no data deletion |
| D-023 | UD-019 | Warfare in scope, designed in Prompt 10, excluded from the first playable |

**Register counts at the end of that pass (historical — superseded by §5.1d):** 23 project decisions (D-001…D-023; D-005 superseded by D-008, D-004 by D-015), 41 design positions (15 approved / 24 provisional / 1 superseded / 1 deferred), 60 requirements (12/39/7/2), 30 unresolved rows of which **10 resolved**, 1 partially resolved and 20 active with **no class-A item and no owner-gated design item** except the legal jurisdiction question (UD-017).

**Continuity corrections made in this pass:** `AI_CONTEXT` §5 index rows for `02`, `03`, `04` and `05` now describe the current files (B-02 drafted, REQ-001…060, D-001…D-023/DD-001…DD-041, UD-030 with its resolutions); the `STATUS` block's `decisions_range` and `operations_points` values now agree in all three continuity files; `AI_HANDOFF` labels the Prompt 6 "OP explicitly NOT resolved" paragraph as historical and no longer says D-004 remains provisional; the Stage 2 handoff, prompt register, outline prerequisites, B-02 reference block and D-004 references were repointed to D-015; the `05` register's owner-approval column was re-read under D-014 and a pending-item inventory (§6) added; `03` gained §3.4 mapping each new decision to the requirements it binds.

| Check | Command / method | Observed result |
|---|---|---|
| Document and continuity validator | `python docs/qa_backups/09_validate.py` | **200/200 checks passed at that point — ALL CHECKS PASSED** (exit 0); **202/202** after the two UD-030 regression checks below |
| Cross-file validator | `python docs/qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** (exit 0) |
| Stale next-action regression test | `python docs/qa_backups/test_next_action.py` | **Ran 10 tests — OK** |
| Register limits | both validators | **PASS** — D-001…D-023 contiguous with no gap or duplicate; DD-001…DD-041; UD-001…UD-030; REQ-001…REQ-060 |
| Link resolution | script over every `stage-2/*.md` plus `AUTONOMOUS_DECISION_POLICY.md` | **PASS** — 145 relative links checked, none dead (the validators cover the continuity files separately) |
| Negative test 1 — stale STATUS | set `decisions_range` back to `D-001..D-013` in `AI_CONTEXT` | **PASS (detected)** — validator exit 1, two failures naming the disagreement and the 23 IDs; file restored |
| Negative test 2 — supersession reverted | set D-004's status cell back to `Provisional` | **PASS (detected)** — validator exit 1, `D-004 status is 'Provisional', expected Superseded by D-015`; file restored |
| Restore check | re-run both validators after restoring | **PASS** — 200/200 and ALL CHECKS PASSED again |
| Continuity defect found afterwards | manual grep of `UD-*` across `stage-2/` | **FOUND** — B-02 §28/§29 still listed UD-030 as open for Prompt 04 even though D-019 had resolved it, and §29 listed it as newly raised |
| Fix and regression checks | B-02 v1.3 text + two new assertions in `09_validate.py` | **PASS** — the two checks fail if B-02 ever again asks Prompt 04 to decide the P3 order; re-run: **202/202**, `validate_final.py` ALL CHECKS PASSED, `test_next_action.py` 10/10 |
| What was **not** run | — | No game test (none exists), no scheduler or load test, no deployment, and **no new web research this pass**: the platform evidence cited by D-022 is the measured Stage 1 record (Reports 11–12), not a fresh reading of provider terms. Nothing here claims otherwise |

### 5.1d Decision-closure audit (2026-10-23, after Prompt 02)

A full audit of every decision and unresolved question closed seven more items and separated policy from proof. The full record is [08_final_decision_closure_audit.md](08_final_decision_closure_audit.md); this table is the log's summary. No Prompt 03 deliverable was written and no code, migration, deployment or hosting change was made.

| Decision | Resolved | What changed in the rules or registers |
|---|---|---|
| D-024 | — (completes D-004's question) | No shared action budget; every non-military subsystem declares a visible per-action limit in its B-02 §24 contract |
| D-025 | UD-016, UD-028 | Forward-only recovery; a `FAILED` turn delays the world and preserves pending actions; Free has no managed backup, so daily owner-run **three-part** `db dump` (roles/schema/data), RPO/RTO ≤24 h best-effort, quarterly CF-02; paid backup not adopted |
| D-026 | UD-004 | Class-S hot 30 days → 12 monthly summaries → deleted; class-P permanent; class-O ≥12 months; 14-day/6-month fallback above 350 MB at 1,000 nations |
| D-027 | UD-027 | k = 5 aggregates, stable merging, complementary suppression, no differencing |
| D-028 | UD-025 | Dormancy at 14 days/168 turns; no offensive targeting or initiation; no decay; excluded from rankings/aggregates; one-boundary return grace; reversible archival at 12 months |
| D-029 | UD-015 | Verified e-mail before nation creation; Supabase built-in mail is development-only; custom SMTP mandatory for public signup; no SMTP means CP only |
| D-030 | UD-029 | A pending diplomatic proposal is visible to its named counterparty while open; third parties see it only once declared, effective or published; rejection/withdrawal is private unless published |

**Current counts (verified against the files):** **30** project decisions (D-001…D-030; D-004 and D-005 superseded; D-006 provisional), **48** design positions (22 approved / 24 provisional / 1 superseded / 1 deferred), **60** requirements (12 approved / 41 provisional / 5 open / 2 deferred; **0 executed validations**), and **30** unresolved rows: **17 Resolved**, **8 Deferred to a named future prompt**, **5 Open** (class A 0 / B 5 / C 3 / D 3 / E 2 across the 13 non-resolved rows).

**What remains non-resolved:** 8 rows **Deferred to their named prompt** (UD-009→06, UD-010/011→05, UD-012→09, UD-013→08, UD-022/023→13, UD-024→11), and 5 **Open** rows: 3 class-C simulation (UD-005/006/007), 1 capacity measurement (UD-026), 1 legal (UD-017). **No class-A item and no owner-gated ordinary design item remains.**

**Policy vs proof.** D-025/D-029 are policy decisions, not executed tests. CF-02 (backup/restore), CF-04 (auth end-to-end) and the Stage 3 byte measurement remain **unexecuted** and are not counted as passed anywhere.

**Continuity corrections:** FO-018's "owner-held" wording in AI_CONTEXT/AI_HANDOFF replaced with D-021's launch posture; OSQ-003/007 annotated as decided by D-029/D-025; the UD-016 row and §6 reconciled; the historical D-004 line in §5.1 labelled as a Prompt 01 snapshot; the D-030 pass reconciled to 30 D / 48 DD / 17 resolved / 8 deferred / 5 open / seven decisions throughout Stage 2 and the continuity files; B-02 TR-022/TR-080/TR-092/TR-096 updated; Prompt 03 now applies D-028/D-029 rather than deciding UD-025/UD-015. The validators gained row-level status checks, exact active-inventory matching and an 8-mutation negative suite.

| Check | Command / method | Observed result |
|---|---|---|
| Document and continuity validator | `python docs/qa_backups/09_validate.py` | **335/335 checks passed — ALL CHECKS PASSED**, exit 0 |
| Cross-file validator | `python docs/qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED**, exit 0 |
| Stale next-action regression test | `python docs/qa_backups/test_next_action.py` | **Ran 10 tests — OK** |
| Decision-register regression tests | `python docs/qa_backups/test_decision_registers.py` | **Ran 12 tests — OK** |
| Link resolution | relative-link scan over `docs/*.md`, `stage-1/*.md` and `stage-2/*.md` | **556 links checked, 0 broken** |
| Register counts | both validators | **PASS** — 30 D, 48 DD, 30 UD (17 resolved / 8 deferred / 5 open), 60 REQ (12/41/5/2) |
| Negative tests | mutation → validator → restore → re-run | **11/11 detected:** D-004 reverted to Provisional, UD-016 and UD-009 set Open, FO-018 owner-held, CF-02 claimed executed, AI_CONTEXT totals reverted to DD-047, D-030 set Provisional, duplicate D-030 row, Stage 2 handoff range ended at D-029, DD-043 reverted to a single dump, D-025's omission sentence removed. Every file hash restored; final re-run 335/335 + ALL CHECKS PASSED |
| Validator robustness | failure message containing `₹` under Windows legacy stdout | **FIXED** — `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` added to both validators; a failing check now prints its reason instead of raising `UnicodeEncodeError` |
| What was **not** run | — | No game test (none exists), **no backup/restore drill**, no SMTP/auth test, no scheduler or load test, no deployment |

### 5.1e Final decision-closure micro-correction (2026-10-23)

A bounded ZIP-audit pass fixed four classes of defect without reopening the audit:

1. **Stale range summaries.** `PROJECT_PROGRESS.md` said “Twenty-nine entries, D-001…D-029”, and `stage-2/00_stage_2_handoff.md` §scope said `D-001…D-029`. Both now read **D-001…D-030** with **thirty** verified entries.
2. **Prompt-owned UD statuses.** UD-009/010/011/012/013/022/023/024 were generic `Open`; they are now **Deferred to Prompt 06/05/05/09/08/13/13/11** respectively. The five genuinely Open rows are UD-005/006/007 (simulation), UD-017 (legal) and UD-026 (capacity), so the register reconciles **17 Resolved + 8 Deferred + 5 Open = 30**. Deferred is explicitly not counted as resolved.
3. **Supabase export accuracy.** The official [Backup and Restore using the CLI](https://supabase.com/docs/guides/platform/migrating-within-supabase/backup-restore) workflow runs three commands — `--role-only` roles, default schema, `--data-only` data. The [CLI Reference](https://supabase.com/docs/reference/cli/introduction) states the default dump contains no data and no custom roles. D-025, DD-043, UD-016, AI_HANDOFF, the Stage 2 handoff and §3.3/§9.1 of the audit now say so; migration history, Storage objects, custom `auth`/`storage` schema changes and custom LOGIN passwords are separately handled. **No backup or restore was performed.**
4. **Regression coverage.** `09_validate.py` and `validate_final.py` now check current ranges, exclusive UD statuses, the §6 inventory and the three-part backup policy. A focused suite, `test_decision_registers.py`, adds 12 tests. The mutation suite detects 11/11 cases, including the previously missed UD status change and both stale-range/backup regressions.

### 5.2 Manual review

| Question | Finding |
|---|---|
| Is the outline navigable? | Yes — 19 parts, each with one authoritative document and a status; nothing claims to be written that is not |
| Does the tracker map real requirements? | Yes — every row has a source, a section, a prompt and a validation method; 5 rows are honestly Open after REQ-017 moved to Provisional and REQ-028/039 followed (policy decided, proof outstanding); REQ-024 stays Open for deletion design |
| Are approvals distinguished from proposals? | Yes — 12 Approved rows are all traceable to a confirmed decision or an owner-stated constraint; the rest are Provisional/Open/Deferred. The 13 Prompt 02 rows are **all Provisional** |
| Are blocking items separated from testing? | Yes — the two class-A items that stood at Prompt 02 (UD-002, UD-018) are **resolved** (D-016, D-015), and the audit added no new class-A row: **0 class-A rows**. The remainder are 9 prompt-owned design rows, 3 simulation, 1 measurement and 1 legal row; CF-01…CF-09 are explicitly excluded |
| Is there duplicate authority? | No — the outline names one authoritative document per rule family and links to Report 09 for inherited requirement text |
| Can another AI continue? | Yes — §4 gives the order and the dependencies; §5 states what ran; the next prompt is named |

**Prompt 02 manual review**

| Question | Finding |
|---|---|
| Is the cutoff ambiguous anywhere? | No — TR-029 states one rule (server receipt, half-open window, boundary instant to the later turn) and the table in Example B agrees with it. TR-030 explains why there is no grace period |
| Do acceptance and resolution contradict each other? | No — the separation is explicit (TR-051/TR-059/TR-061): acceptance is entry under the rules then in force, effect is decided at P2 against the frozen state |
| Is recurring-vs-order ordering contradictory? | No conflict found. The phase order is fixed; the internal P3 order (income before upkeep) was provisional at Prompt 02 and is **confirmed by D-019** the same day, so UD-030 is resolved and Prompt 04 owns only the deficit rule |
| Are duplicates handled? | Yes — server-assigned identity, idempotency key scoped to account/type/turn, replay returns the original, a changed payload is `F9`; “unknown” is an explicit client state |
| Is insufficient-resource behaviour clear? | Yes — exclusive reservations at acceptance; an order that cannot reserve its full cost is rejected, not queued; a later failure releases with `F1` |
| Is an interrupted turn safe? | Yes at the rule level — one published outcome, forward-only resume from phase checkpoints, nothing visible before COMPLETED; the technical mechanism is deferred |
| Is there an unjustified player-order advantage? | No — B1 order is published and deterministic; contested resources use order-independent allocation; time priority requires an explicit, published subsystem rule that does not exist yet |
| Do inactivity rules accidentally require presence? | No — TR-084/TR-085 and Example F; nothing in the framework waits for a player |
| Can private information leak? | Only through implementation error: visibility classes are assigned per field, aggregates require k = 5 with complementary suppression (D-027), and no public offer book exists (D-017) |
| Is any unapproved mechanic presented as final? | No — every rule is labelled; no general action currency was created; D-004/DD-019 are **superseded** by D-015/DD-033 (model approved, values provisional); no owner approval was invented |
| Does anything contradict the mapless constraint? | No — entities are a graph with edges; no coordinates, distances, fronts or provinces appear anywhere |
| Does anything contradict Stage 1 or Prompt 01? | No — Stage 1's proposals are cited as inputs, the registers are updated rather than forked, and D-001…D-013 are untouched. The document renumbering is administrative and recorded in the outline and roadmap |

### 5.3 Honest limits

- Prompt 02's rules are a design, not a running system: no turn has been resolved under them, and the exactly-once behaviour they require has only been demonstrated once in a synthetic prototype (CF-03/CF-06).
- No test in this project has been executed against an implementation, because none exists. The ordering catalogue's determinism has been reasoned and exemplified, not simulated.
- The requirement statuses reflect Stage 1 evidence plus the confirmed decisions; they are not re-verified product claims.
- The stale-next-action detector (`qa_backups/status_rules.py`) is a bounded heuristic: it inspects blocks and lines that assert a next action, so a stale instruction phrased without one of its markers could still escape. It guards against the regression that occurred; it is not proof of prose correctness.

---

## 6. Next action

**Stage 2, Prompt 04 — Economy, Resources, Treasury and Finances.**

Read, in order: [AI_CONTEXT](../AI_CONTEXT.md), [AI_HANDOFF](../AI_HANDOFF.md), [PROJECT_PROGRESS](../PROJECT_PROGRESS.md), [DECISIONS](../DECISIONS.md), [ROADMAP](../ROADMAP.md), [the 15-prompt register](01_stage_2_prompt_roadmap.md), then [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) §13 (P3), §19 (reservation) and §23 (digest), [B-03 §8](09_account_onboarding_nation_creation_and_progression.md) (starting-state contract) and §12.3 (fresh-nation transfer rule), the [outline](02_master_game_design_bible_outline.md) Part B-04, and the [unresolved register](05_unresolved_design_decisions.md) UD-005/006/007.

Prompt 04 inherits from Prompt 03: the **standard starting state's structure** with every number unset (NAT-043/NAT-044), the one-sided transfer restriction (ONB-031) whose band and duration Prompt 07/14 own, and the rule that a reroll neither creates nor preserves value (RRL-013/RRL-014). It must **not** invent a starting-grant size that Prompt 14 cannot test, quietly add catch-up acceleration (D-021), or treat the B-03 provisional parameters as approved.

---

## 7. Prompt 03 checkpoint (2026-10-24)

### 7.1 What was produced

| Item | Result |
|---|---|
| Authoritative document | [09_account_onboarding_nation_creation_and_progression.md](09_account_onboarding_nation_creation_and_progression.md) — 1,700+ lines, 22 sections: purpose and scope, source documents and design authority, research, account policy, shared-network policy, creation, naming, starting state, reroll, lifecycle, onboarding, protection, dormancy, privacy/data, invariants, journeys, messages, cross-system contracts, requirements, tests, decisions, research log, completion |
| Rule families created | `ACC-001…ACC-049`, `NET-001…NET-061`, `NAT-001…NAT-053`, `RRL-001…RRL-034`, `ONB-001…ONB-052`, `DAT-001…DAT-012`, `MSG-01…MSG-25`, `J-01…J-20`, `INV-001…INV-032`, `T03-A01…E08` |
| Requirements | REQ-061…REQ-097 added (37); no existing ID reused |
| Decisions | D-031…D-042 (12) in [DECISIONS](../DECISIONS.md); DD-049…DD-060 in [the design register](04_approved_and_provisional_decisions.md) |
| Unresolved register | UD-031…UD-033 added as deferred rows (33 total: 17 resolved / 11 deferred / 5 open) |
| Outline | B-03 marked **Draft**, real path and content recorded |
| Continuity | AI_CONTEXT, AI_HANDOFF, PROJECT_PROGRESS, the Stage 2 handoff and this log updated; next prompt set to 04 |
| Later-prompt inheritance | [01 prompt roadmap](01_stage_2_prompt_roadmap.md) carries a **B-03 carry-in** line for Prompts 04–15, naming each prompt's reroll and shared-network obligations |

### 7.2 Design positions that bind later prompts

1. **One account, one active nation** (ACC-001…ACC-016, D-031/D-032): account-owned; transaction-safe; session-derived ownership; no perfect-identification claim.
2. **Shared networks restrict pairs, not people** (NET-001…NET-061, D-033…D-037): five states, a separate review status, a complete verb matrix, indirect routes covered, no bank use while restricted, a review route without identity documents, and an explicit refusal of a co-resident exemption.
3. **The IP signal is trusted infrastructure, not a form field** (NET-005…NET-013, D-036): Pages Function → `CF-Connecting-IP` → normalise → HMAC digest → server-only write; no raw IP stored; check inside the committing transaction.
4. **Nation creation is idempotent and atomic** (NAT-001…NAT-025): per-account lock, partial uniqueness, one starting grant, no partial nation.
5. **Naming is a validation class, not a claim system** (NAT-026…NAT-042, D-038): NFC, case/diacritic fold, reserved list, 30-day release hold, cooldowns, immutable ID.
6. **Reroll is instant, total and account-preserving** (RRL-001…RRL-034, D-039): typed confirmation, no cooldown, everything destroyed, sanctions and pair records survive, blocked during a campaign/settlement/hold, abuse handled by review not timers.
7. **Protection is a shield, not a subsidy** (ONB-019…ONB-035, D-040): first nation only, seven days, visibility-only, skipped between a restricted pair, never re-granted.
8. **The lifecycle is three separate state machines** (D-031, D-041): account, nation and pair; recovery restores the existing account; closure deletes private data but not required history.

### 7.3 What this checkpoint deliberately leaves open

| Item | Owner | Why |
|---|---|---|
| Every numeric anti-abuse parameter | Prompt 12/14 (see B-03 §21.2) | Chosen to be defensible, not measured |
| Review tooling, staffing, case management | Prompt 12 | Policy fixed, operations not designed |
| Starting grant, material stock, upkeep, deficit rule | Prompt 04 | Economy numerics; Prompt 03 fixed only the shape |
| Transfer window, fair-value band | Prompt 07/14 | Needs market rules |
| Campaign forfeit on reroll (UD-032) | Prompt 10 | Needs the campaign lifecycle |
| Diplomatic reputation scope after reroll (UD-033) | Prompt 08 | Needs the reputation model |
| Supabase Auth configuration, SMTP vendor, session values | Stage 6 | Technical configuration, not Stage 2 |
| Schema, constraints, RLS, functions | Stage 5 | This is a rulebook, not a schema |
| Jurisdiction, age gate, legal basis (UD-017) | Owner / Prompt 12 | Not self-assignable |

### 7.4 Validation performed

| Check | Command / method | Result |
|---|---|---|
| Requirements register structure | `python docs/qa_backups/validate_final.py` | **PASS** — `VALIDATION: ALL CHECKS PASSED` (B-03 section, REQ-061…REQ-097 rows, decision-range and counts all reconciled) |
| Stage 1 document hygiene | `python docs/qa_backups/09_validate.py` | **PASS** — 338/338 checks |
| Decision-register state | `python docs/qa_backups/test_decision_registers.py` | **PASS** — 12 tests, OK; expectations advanced to Prompt 04, 33 UD rows and REQ-097; no check weakened |
| Stale next-action detector | `python docs/qa_backups/test_next_action.py` | **PASS** — 15 tests, OK; expectations advanced to Prompt 04, plus four current-state regressions added by the finalization micro-correction |
| Document consistency | Manual review of links, IDs, counts and cross-references | Performed; results in the final report and §7.5 |
| Any runtime behaviour | — | **Not tested. No game code exists.** |

### 7.5 Honest limits

- The 51 T03 tests are **specifications**. None has run; none can run until Stages 5–8 exist.
- The trust-boundary design is consistent with current Cloudflare and Supabase documentation but **was not exercised**; `T03-D03` is the future proof.
- The thresholds (24 h, 180 days, 25 accounts, 7 days protection, 3 rerolls in 30 days) are judgement calls with no playtest evidence.
- Review capacity is unknown; the 7-day target is a service target, not a promise.
- The research could not read the two P&W forum threads' reply bodies, and P&W's live mechanics were not tested logged-in.
- No rule here is balanced, and the document says so rather than implying otherwise.

### 7.6 Finalization micro-correction (2026-10-24)

Bounded documentation pass after Prompt 03 closure. Fixed: the outline's §5 current-state table (Prompts 01–03, the B-03 link, and 5 drafted / 2 gameplay sections derived from the outline itself); the duplicate Prompt 04 row in `PROJECT_PROGRESS.md`; the unlabelled Prompt 03 brief in `AI_HANDOFF.md`, now a labelled historical snapshot followed by a current Prompt 04 carry-in; the market summary, reconciled with D-016/D-017 while keeping the genuine open questions; and a glued `## G.` heading in the handoff. Added four current-state regressions to `test_next_action.py`: outline status/counts, one next-task row, labelled-history boundary, and market-versus-decision-register consistency.

| Check | Result |
|---|---|
| `python docs/qa_backups/09_validate.py` | **PASS** — 338/338 |
| `python docs/qa_backups/validate_final.py` | **PASS** — ALL CHECKS PASSED |
| `python docs/qa_backups/test_next_action.py` | **PASS** — 15 tests |
| `python docs/qa_backups/test_decision_registers.py` | **PASS** — 12 tests |

No application code, migration, authentication setting, credential, deployment or hosting-provider change was made.

---

## 8. Prompt 04 checkpoint (2026-10-24)

**Status:** Prompt 04 **complete** as a design specification. Nothing in B-04 is implemented, migrated, deployed or runtime-tested.

### 8.1 What was produced

| Deliverable | Content | Status |
|---|---|---|
| [`research/04_politics_and_war_economy_research.md`](research/04_politics_and_war_economy_research.md) | P&W research report: income, taxation, population, improvements, resource classes, production, manufacturing, operating costs, market, military competition, scaling, reporting; each finding tagged **Verified reference mechanic / Interpretation / Nation Supremacy recommendation**, with source list and confidence grades | Draft |
| [`10_economy_resources_treasury_and_finances.md`](10_economy_resources_treasury_and_finances.md) — B-04 | 25 sections: philosophy, the 11-resource roster with a lifecycle profile per resource, capacity/batches/standing policy, power, four recipes, food and the shortage contract, treasury and finance, storage and reservations, action states, the P3 two-hour settlement, the append-only ledger, reporting and forecasts, balance targets, 20 worked examples, reroll economics, cross-system contracts, 90 requirements, 54 test specifications | Draft |
| [`10_economic_formula_and_balance_register.md`](10_economic_formula_and_balance_register.md) | The single authoritative formula register: constants, starting bundle, extraction coefficients, recipes, generators, reference prices, ~50 formulas with units/bounds/rounding/timing, margin and dominance table, worked-example index, change control | Draft |

### 8.2 Design positions that bind later prompts

| Position | Decision | Later prompt |
|---|---|---|
| Production capacity, power and the four recipes | Capacity is a per-chain batch count owned by Prompt 05; extraction coefficients, recipes (10 oil→8 gasoline; 10 iron + 6 coal→8 steel; 12 bauxite→8 aluminium; 8 lead + 4 coal→10 ammunition) and power draws are fixed in B-04 and may not change without a new decision | 05 |
| Food and population | One food unit feeds 1,000 people for one turn; demand `ceil(population/1000)`; consumption at P3.6; a 0–30% hunger penalty applies to the **next** turn's tax income and is replaced, not stacked. Prompt 06 owns population growth, stability and any political consequence | 06 |
| Trade and market | Reference prices are **book values**, not market prices or promises; fees, price formation and the fair-value band belong to Prompt 07; a restricted pair's market match moves nothing (B-03 matrix) | 07 |
| Transfers and embargo | Inter-nation transfers are reserved/committed atomically under B-02, use the same ledger event classes and are subject to the B-03 pair matrix; embargo rules are Prompt 08's | 08 |
| Alliance pools | An alliance pool is separate from the national treasury, is audited, and may not be used by a restricted pair; the pool's governance is Prompt 09's | 09 |
| Military consumption | Ammunition, gasoline, steel and aluminium consumption rates and readiness upkeep are Prompt 10's; B-04 fixes only that consumption is a P3/P7 obligation and that unfunded readiness falls | 10 |
| Rewards and rankings | New crowns enter only through tax, the one-time starting grant, a disclosed event reward or an administrative correction; national wealth is a report statistic, not a spendable balance | 11 |
| Audit and corrections | The ledger is append-only with unique event keys, signed deltas, `balance_after`, origin and visibility; corrections are linked reversals. Prompt 12 owns the operator procedure and disclosure | 12 |
| Screens | Prompt 13 renders total/available/reserved, income and expense provenance, per-chain margin, food forecast, power, storage and the six number types; it may not redefine a number | 13 |
| Tuning | Every coefficient, cost and threshold is provisional and must be simulated or confirmed by Prompt 14 | 14 |

**Reroll and shared-network carry-in.** A reroll destroys every crown, resource, reservation, pending order and open offer; the replacement receives only the standard bundle (D-063), once, with no protection re-grant; sanctions, pair restrictions, cases, evidence and history survive (B-03 §9). A restricted pair's economic verbs move nothing, and a shared address alone never blocks a trade. These are recorded in B-04 §21 and applied to Prompts 07, 08, 09, 10, 11 and 13.

### 8.3 What this checkpoint deliberately leaves open

| Item | Owner | Why it is not settled here |
|---|---|---|
| All numeric values (UD-005/006/007) | Prompt 14 | Design structure is fixed; balance needs simulation, not another document |
| Construction costs, building catalogue, warehouse expansion | Prompt 05 | Belongs to the capacity model |
| Population growth, stability effects, taxation policy | Prompt 06 | Prompt 04 fixes only the contract and the default 300 bp |
| Market price, fees, fair-value band, transfer window | Prompt 07 | Needs the trade rules |
| Military consumption and readiness | Prompt 10 | Needs the warfare model |
| Campaign forfeit on reroll (UD-032) | Prompt 10 | The B-03 block is the safe interim rule |
| Diplomatic reputation scope after reroll (UD-033) | Prompt 08 | Needs the reputation model |

### 8.4 Validation performed

All five checks were run from `docs/` on 2026-10-24 after the last edit to any register, specification or continuity file.

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`**, including the B-04 block (25 sections, the 11-resource roster, all four recipes in both documents, 20 worked examples, complete T04 coverage, every REQ-098…REQ-187 cited, every cited `F-EC-` present in the register) |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** (D-001…D-065, status block, UD-status reconciliation, and the then-current next action — that assertion now reads Prompt 06) |
| `python qa_backups/test_next_action.py` | **15 tests — OK** (no stale next action; the outline, the progress table and the continuity set agree) |
| `python qa_backups/verify_economy_numbers.py` | **146/146 arithmetic checks passed** — recomputes the bundle, all 20 examples and the register's index from the published constants, compares the rulebook's Example 5 with the register's index row, and fails on any stale figure or an unsynchronised version header |

Hand checks and the arithmetic script (`qa_backups/verify_economy_numbers.py`, now **146/146 checks**) recompute the starting bundle and all 20 examples from the register's constants. An independent review then found three substantive defects, all corrected at source: the **starting bundle total** (350 → **310** units; the listed quantities had never summed to 350), **Example 3** (opening total 1,560 not 1,360; uranium, bauxite and lead yields had been read from their crown costs; ammunition had run two batches with capacity one; closing stock **1,673** units, book value **5,128**, wealth **6,375**, change **+146**), and **Example 5** (a 2-crown market fee that B-04 never adopted; closing **1,428**, with the fee retained only as a labelled hypothetical in Example 16). Examples 7/8 keep the published margin definitions (base margin excludes power; fully loaded includes it at ≈3.0 crowns/GU; gasoline sensitivity **+8 per batch**). No coefficient, recipe or formula changed. Register counts were verified against the tables, not asserted: 187 requirements (14 approved / 166 provisional / 5 open / 2 deferred), 65 decisions, 80 design positions, UD 17 Resolved / 8 Deferred / 5 Open.

**Not run:** no runtime, database, scheduler, ledger, market or simulation check. None exists, and **0 of the 54 T04 tests** has been executed.

### 8.5 Honest limits

- B-04 is a **design specification**: no economy, scheduler, ledger, warehouse or market exists, and no runtime test has run.
- The 54 T04 tests are specifications. The 20 worked examples were checked by recomputation against the formula register, not by an engine.
- The numbers are internally consistent and deliberately provisional; they are not balanced. Prompt 14 must retune or confirm every coefficient.
- The P&W research is documentary (wiki API pages, the official site, community FAQ) and P&W may have changed; no logged-in test was performed.
- The food/population contract is one-directional by design: Prompt 06 may add effects Prompt 04 did not model, and must then update this contract rather than contradict it.
- No application code, database migration, authentication setting, credential or deployment was touched.

### 8.6 Final micro-correction (2026-10-24)

A third, narrowly bounded pass closed two documentation residues of the v1.1 correction and the regression gap that let them survive.

| Defect | Before | After |
|---|---|---|
| Register worked-example index, row 5 | `Closing 1,426; identity holds` — the fee-inclusive figure the rulebook had already replaced | **`Closing 1,428; identity holds`** |
| Version header, B-04 and the register | `Version: 1.0` although both revision histories describe v1.1 | **Version 1.1** plus an explicit `Revised:` line pointing at ECN-230 / F-EC-044 |

The arithmetic verifier was strengthened rather than the numbers re-explained. It now (a) recomputes Example 5's treasury from the published transaction amounts, (b) requires the rulebook's Example 5 to state that input line and the resulting `1,428`, and that it charges no fee, (c) parses the register's index row for Example 5 and compares its result cell with the recomputed value, (d) requires Example 16's fee to remain labelled hypothetical in the rulebook and illustrative in the index, and (e) requires both headers to read v1.1. Two stale tokens were added (`Closing 1,426; identity holds` and the fee-bearing sum), so restoring the old text fails the check. The mutation test was performed: setting the index row back to 1,426 and the header back to 1.0 produced **three failures and exit 1**, and the files were restored.

Validation was rerun after the last edit: `09_validate.py` **338/338**, `validate_final.py` **ALL CHECKS PASSED**, `test_decision_registers.py` **12 tests OK**, `test_next_action.py` **15 tests OK**, `verify_economy_numbers.py` **146/146**. A repository-wide audit found no copy of 1,426 that presents it as a current result: the remaining occurrences are the verifier's own stale-token definitions and labelled correction histories (both headers, both revision histories, this log and the rulebook's arithmetic note), all correct as history. **Prompt 04 is accepted**; Prompt 05 remains unstarted.
---

## 9. Prompt 05 — Cities, infrastructure, production and research (2026-10-25)

This is the **Prompt 05 checkpoint**: what the prompt produced, the decisions it recorded, the contracts it hands to later prompts, the validation it actually ran, and the limits a reader must not mistake for proof.

### 9.1 What was produced

| Deliverable | Path | State |
|---|---|---|
| B-05 rulebook (26 sections, 172 numbered rules) | [`11_cities_infrastructure_production_and_research.md`](11_cities_infrastructure_production_and_research.md) | **Draft v1.3** — design only; v1.2 corrected three internal cross-references, v1.3 states Example 3's opening treasury and closes two catalogue gaps (the institute and civic centre IDs, and the eighteenth-type ordinal) |
| Formula and balance register (42 `F-CI-` definitions) | [`11_city_infrastructure_production_and_research_formula_register.md`](11_city_infrastructure_production_and_research_formula_register.md) | **Draft v1.0** — the single formula authority for B-05 |
| P&W research report | [`research/05_politics_and_war_city_infrastructure_production_research.md`](research/05_politics_and_war_city_infrastructure_production_research.md) | **Complete** — wiki API pages with access dates, reliability grades and a comparison matrix |
| Arithmetic checker | [`qa_backups/verify_city_numbers.py`](../qa_backups/verify_city_numbers.py) | **New** — 150 assertions over the register's constants and all 20 examples |

The design in one line: a city is a **named, non-geographic development centre** whose infrastructure yields **development capacity** and **housing**; capacity is spent by a **17-type closed catalogue**; one construction action per city resolves at **P4.1**; research is a **facility output** (1 RP per institute per turn) spent on **12 technologies** and **4 branch capstones**; every effect is an **integer modifier with a declared cap**.

### 9.2 Decisions recorded

**15 project decisions, D-066…D-080**, and **20 design positions, DD-081…DD-100**:

| Decision | Rule |
|---|---|
| D-066 | A city is a named, non-geographic development centre (no coordinates, land, borders or deposits) |
| D-067 | One capital; at most 12 cities; **no city deletion** |
| D-068 | Founding city *k* needs national infrastructure ≥ 100(k−1), an expansion slot, `400 + 150k²` crowns and 20 steel; no cooldown |
| D-069 | Infrastructure is an integer 10–500, yields only capacity and housing, and **cannot be reduced** |
| D-070 | Weighted development capacity per class (1/2/2/1/3/2) |
| D-071 | Per-city limits are the specialisation lever (8/4/6/6/2/3) |
| D-072 | A closed 17-type catalogue; no commerce, pollution, culture or military buildings |
| D-073 | One construction slot per city per turn; one founding and one programme per nation; no queue object |
| D-074 | Demolition refunds 25% of crowns paid, never materials; granted start facilities refund 0 |
| D-075 | Power plants on B-04's grid; uranium and nuclear gated by `tech_nuclear_engineering` |
| D-076 | Research as a facility output; one active project; 12 technologies, 448 RP and 3,180 crowns |
| D-077 | Integer modifier classes with caps (+3 food, +1 others, 2,000 bp discounts) |
| D-078 | Four branch-capstone programmes, one named effect each |
| D-079 | Housing `45,000 + 100I + 25,000 × civic` is the hard Prompt 06 contract |
| D-080 | Construction is capex; research and programmes are expensed investment |

**Unresolved register:** UD-010 resolved (universal resource access; no deposits or affinities), UD-011 resolved (there is no emphasis setting; a role change is demolition plus construction), UD-007 narrowed to values only. No new row was added.

### 9.3 Contracts handed forward

| Prompt | Contract |
|---|---|
| 06 | National housing is a hard growth cap; Prompt 06 owns population, disease, crime, stability and tax and may not add a second housing source (URB-124…127) |
| 07 | Facilities produce into the national inventory under B-04's reservations; no deposit luck to price |
| 08 / 09 | No diplomacy or alliance mechanic may grant capacity, technology or a programme outside the register |
| 10 | Capacity, fuel and ammunition output are inputs; Prompt 10 owns consumption and combat values |
| 11 | An event reward may grant a programme only through a decision and a register row |
| 12 | Twelve new ledger event types and the demolition/founding/correction audit trail |
| 13 | Capacity, cost preview, blocking reason and research status must be visible before commitment |
| 14 | Every cost, coefficient and threshold is provisional; ten named balance questions |
| 15 | B-05 is linked from the Bible outline and its register is the formula authority |

### 9.4 Validation performed

All six checks were run from `docs/` on 2026-10-25 after the last edit to any register, specification or continuity file.

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`**, including the new B-05 block (26 sections, the 11-resource roster, all four recipes, 20 worked examples, complete T05 coverage, every REQ-188…REQ-257 cited, every cited `F-CI-` present in the register, v1.3 header, and two new catalogue guards — all 17 types carry a `bld_` ID and the "nineteenth" ordinal cannot return) |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** (D-001…D-080, status block, UD reconciliation 19/9/5, Prompt 06 next) |
| `python qa_backups/test_next_action.py` | **15 tests — OK** (outline §5, progress table, handoff history labels and the bounded stale-next-action rule) |
| `python qa_backups/verify_city_numbers.py` | **150/150 arithmetic checks passed** — recomputes every register constant and all 20 examples, including the capacity invariant, the refund, the research completion and the duplicate-settlement cases |
| `python qa_backups/verify_economy_numbers.py` | **146/146 arithmetic checks passed** — B-04 unchanged by this prompt |

**Counts, derived from the files rather than asserted:** 257 requirements (14 approved / 236 provisional / 5 open / 2 deferred), 80 decisions, 100 design positions, 33 UD rows (19 Resolved / 9 Deferred / 5 Open). The traceability's `§3` summary, the two decision registers, `AI_CONTEXT` and the handoff blocks agree.

**Not run:** no runtime, database, scheduler, build or simulation check. None exists for B-05, and **0 of the 64 T05 tests** has been executed. The arithmetic checker validates the documents, not a game.

**Superseded on the same day:** this §9.4 table is the **pre-review** run. The independent review that followed found inconsistencies these checks did not catch; §9.6 records the corrections, §9.7 that run's results (**219/219**) and §9.8–§9.9 the final micro-correction (**267/267**). The 150/150 and 219/219 figures are history and must not be quoted as the current count.

### 9.5 Honest limits

- B-05 is a **design specification**. No city, building, research project or programme has been implemented, and no runtime test exists.
- The 20 worked examples are checked by recomputation against the register, not by an engine. Internal consistency is not balance.
- Every number is deliberately provisional. Prompt 14 must retune or confirm the infrastructure curve, the founding gate, the research rates and the programme costs.
- The P&W research is documentary (community wiki via the MediaWiki API, plus the official site) and the reference game may have changed; no logged-in test was performed.
- The housing/population boundary is a contract. Prompt 06 may add crowding or migration rules that change the player experience, and must then update the contract rather than contradict it.
- The 12-city bound, the 500-infrastructure cap and the 25% refund are judgement calls, not measurements.
- The strongest single technology (`tech_ext_deep`, +1 uranium on a base of 1) is flagged for simulation, not justified as balanced.
- There is no city-destruction rule: warfare can destroy resources and units, not cities, until a decision says otherwise.
- No application code, database migration, authentication setting, credential or deployment was touched.

### 9.6 Independent-review reconciliation (2026-10-25)

An independent review of B-05 found cross-document inconsistencies that the 150 assertions of §9.4 did not catch. They were fixed **at source**, not papered over, and the checker was strengthened so each defect is now a failing assertion. No city, cost, coefficient, recipe or design intent was redesigned; the corrections make the existing design say one thing.

| # | Defect found | Correction |
|---|---|---|
| A | **Example 12** reported `treasury −22` with no opening balance, implying debt in a no-debt economy | Opening treasury **1,000** stated; closing **978**; a second paragraph shows that a 21-crown nation cannot run the batch, consumes nothing, and owes only maintenance, which is cancelled rather than borrowed (ECN-102/106/147). No Prompt 05 example now ends negative |
| B | **Research points were counted twice** — URB-095 added generation to the pool *and* to progress — while F-CI-021 subtracted programme spending from unrelated progress | One model: `need = max(0, cost_rp − progress)`, `rp_applied = min(rp_per_turn, need)`, `progress += rp_applied`, `rp_pool += rp_per_turn − rp_applied`, `rp_available = rp_pool − rp_reserved`. A point goes to the project **or** the pool. Programmes reserve and consume **banked** points only, at P4.1d before generation. Example 15B shows completion overflow; 15C shows 100 banked points funding `prg_granary` while a 10/44 project advances to 15, reconciling `100 + 35 = 100 + 34 + 1` |
| C | **Two infrastructure cost formulas.** URB-043 used a flat `n × (8 + floor(I/10))` (50→500 = 5,850) while F-CI-005 and D-069 used the stepped sum (15,750); the register's bound of 28,420 was 490 × 58, not a real order | URB-043 now states F-CI-005's marginal sum. 50→500 = **15,750**; 10→500 = **16,170**; 10→500 at the 2,000 bp cap = **12,936**. Splitting an order changes nothing. The stale flat formula and the 28,420 bound are now forbidden tokens in the checker |
| D | **Discount vocabulary was wrong** — “reduces by 10% (9,000 bp)” confused the discount with the remaining multiplier — and Civil Survey (infrastructure) plus Civil Methods (which listed infrastructure) appeared to stack | 1,000 bp is the discount; 9,000 basis points is the remaining multiplier; 2,000 bp is the cap. **One source per cost at launch:** Civil Survey on `UPGRADE_INFRASTRUCTURE`, Civil Methods on `BUILD_FACILITY`/`EXPAND_WAREHOUSE` only. A future source is additive, applied once to the base, capped at 2,000 bp |
| E | **Reservations read as charges.** URB-066 reserved without debiting, but Example 8 reported 880/15 immediately after acceptance | Total, reserved and available are now defined for every value, with `available = total − reserved`; affordability reads `available`. Example 8 is a three-state table: 1,000/0/1,000 → 1,000/120/880 → 880/0/880 (steel 20/0/20 → 20/5/15 → 15/0/15) |
| F | **URB-014 cited D-004 as provisional**, contradicting D-015's supersession | URB-014 now states D-015 as current (model approved, values provisional for Prompt 10) and D-004 as superseded history. DECISIONS.md keeps D-004 visible with its supersession |
| G | **Derating prose said “pro-rata”** while Example 11 produced 0 batches at 66% | B-04's rule is restated exactly: `power_pct` is a percentage, but `batches_available = floor(capacity × power_pct / 10,000)` allocates **whole batches**, with no proportional output and no threshold. A reserved manual batch is already in demand and is counted once. Example 11 now shows capacity 2 at 66% running 1 batch (8 units, never 13.2); balance remains a Prompt 14 question, not a claim |
| H | **Assertion counts disagreed**: traceability said 141, the spec said 150, and neither was guarded | The traceability row now names the verifier and its coverage instead of freezing a number; the dated count lives in the validation records. The checker reads the traceability and fails if a frozen count returns |

**Files changed by the reconciliation:** B-05 rulebook and register (v1.4 / v1.1), `DECISIONS.md` (D-069 and the header), `03_requirements_traceability.md`, `00_stage_2_handoff.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `verify_city_numbers.py`, and `validate_final.py` (header guard moved to v1.4). B-04's documents, the research reports and the requirement counts were not changed: the defects were all B-05's own.

### 9.7 Validation after the reconciliation (2026-10-25)

Run from `docs/` after the last edit, all six checks:

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`** — including the B-05 block with the v1.4 header |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** |
| `python qa_backups/test_next_action.py` | **15 tests — OK** |
| `python qa_backups/verify_city_numbers.py` | **219/219 arithmetic checks passed** — 69 more than §9.4, covering the stepped bound, basis-point vocabulary, Example 8 reservation states, Example 12 affordability, whole-batch derating, the two research-allocation flows and cross-document checks against D-069/D-004/traceability |
| `python qa_backups/verify_economy_numbers.py` | **146/146 checks passed** — B-04 untouched |

**Negative tests were executed, not assumed.** A temporary driver (`qa_backups/_negcheck.py`, deleted after the run) mutated the documents one defect at a time and restored every file: the flat `n × (8 + floor(I/10))` formula, the 9,000 bp discount phrasing, the 28,420 bound, `treasury −22`, the `paid_rp` subtraction, Civil Methods scoped to infrastructure, and `D-004 stays provisional` were **7 of 7 detected**, each making `verify_city_numbers.py` exit 1 through a named required- or forbidden-token assertion. The checker then re-passed 219/219 on the restored files. No assertion was deleted or weakened.

**Still not run:** any runtime, database, scheduler, build or simulation check. **0 of the 64 T05 tests** has been executed, and no city, building, research project or programme exists. Balance remains Prompt 14's work.

### 9.8 Final micro-correction (2026-10-25)

A second independent review found two defects that survived §9.6.

**A — F-CI-021's worked example contradicted its own citation.** The register stated "23/24, 3 RP → applied 1, progress 24, pool +2" and attributed it to Example 15B, which actually runs **22/24 with 3 RP → applied 2, progress 24, pool +1**. Both are valid arithmetic; only the label was wrong. F-CI-021 now states 22/24 for 15B and keeps 23/24 correctly labelled as Example 20's one-point completion. No allocation rule changed.

**B — capacity and power demand disagreed in two places.** `F-EC-006` and `ECN-060` defined `planned_batches = capacity + accepted manual batches`, while `ECN-053` said a manual order *reserves* batches **within** capacity. The first reading breaks the second: a chain of capacity 2 with a 2-batch manual order would plan 4 batches, demand 8 GU instead of 4, and derate itself to 25% and zero runnable batches — which contradicts B-04's own Example 12, where the same state gives 50%, one available batch, and one standing batch after the manual order fails.

The authoritative rule is now one sentence in both books: **manual batches occupy slots inside capacity; `planned_batches = M + A ≤ C`.** `M` is the accepted manual batches, `A` is what the standing policy schedules in the slots they leave (`RUN_AT_CAPACITY`: `A = C − M`; `RUN_TO_TARGET`: capped by the remaining target; `IDLE`: `A = 0`), and power demand is `Σ(M + A) × draw`. A manual batch is counted once, as part of the plan; `C + M` is explicitly invalid. B-04 Example 12 gained a capacity-accounting table and the numerical proof; B-05 formalised the rule in URB-074 and added the matching sentence to Example 11. D-048 was clarified in place rather than given a new ID, because the decision already fixed the reservation model and only the register's wording contradicted it.

**Files changed:** B-04 rulebook and register (v1.2), B-05 rulebook (v1.5) and register (v1.2), `DECISIONS.md` (D-048 and the header), `03_requirements_traceability.md` (REQ-115/REQ-120), `04_approved_and_provisional_decisions.md` (DD-066), `verify_city_numbers.py`, `verify_economy_numbers.py` (B-04 header version) and `validate_final.py` (B-05 header version).

### 9.9 Validation after the micro-correction (2026-10-25)

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`** — including the B-05 v1.5 header |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** |
| `python qa_backups/test_next_action.py` | **15 tests — OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 checks passed** — recomputes the unchanged B-04 numbers and now checks the v1.2 headers |
| `python qa_backups/verify_city_numbers.py` | **267/267 arithmetic checks passed** — 48 more than §9.7, covering the Example 15B state, the `M + A ≤ C` cases, the rejected `C + M` plan, whole-batch execution against supply, the retry identity and the B-04 cross-document tokens |

The strengthened checker detects both defects. A temporary mutation driver (`qa_backups/_negcheck2.py`, deleted after the run) reintroduced five regressions and restored every file: relabelling F-CI-021 as 23/24, reverting F-EC-006 to `capacity + accepted manual batches`, reverting ECN-060 to “chain capacities plus accepted manual orders”, dropping URB-074's `M + A ≤ capacity`, and misstating Example 12's plan table were **5 of 5 detected**, each by a named assertion. Every file was restored and the checker re-passed; the assertion total grew by one further guard (reservations must not include grid units), giving the 267/267 reported in §9.9. **Still not run:** any runtime, database, scheduler or simulation check; **0 of 64 T05 tests** executed.

---

## 10. Prompt 06A — population and domestic-politics foundation (2026-10-25)

**Deliverables.** [B-06](12_population_and_domestic_politics.md) (rulebook, v1.2, 22 sections), [its formula register](12_population_and_domestic_politics_formula_register.md) (v1.1, F-PD-001…F-PD-025) and [the P&W research report](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md) (v1.0). The foundation covers the population model, the food and housing interfaces, approval, stability, derived legitimacy, six fixed constituencies, six permanent governments with five channels each, two policy axes, the political state and the P3.8 settlement, the 06B interfaces, the cross-system contracts, the exploit register, the UX requirements, the balance target and **18 worked examples**.

### 10.1 Research

P&W's live pages were readable; `politicsandwar.fandom.com` returned **403** and `forum.politicsandwar.com` **timed out** on every attempt. The report therefore grades every finding: **V1** live page, **V2** archived wiki snapshot (snapshot dates recorded), **V3** search snippet, **C** community proposal, **N** Nation Supremacy recommendation. The verified position is that P&W's government type, social policy and economic policy are **cosmetic**, that its national tax rate is deliberately **revenue-neutral**, and that its approval rating is an unbounded score with **no mechanical effect**. Forum threads appear only as snippets, with no author, date or consensus invented. No P&W account was created and no in-game test was run.

### 10.2 What was decided

Eleven decisions, **D-081…D-091**, with **DD-101…DD-111** as their design positions:

| Decision | Substance |
|---|---|
| D-081 | National population, 50,000 start, 1,000 floor, four-term growth, housing cap, gradual crowding decay |
| D-082 | Approval is the weighted mean of six supports, ±5 points per turn, no random drift |
| D-083 | Stability is administrative capacity and feeds tax once; legitimacy is derived and consequence-free until 06B |
| D-084 | **Government identity is permanent** (Model A), with no change verb; only a reroll changes it |
| D-085 | Six launch governments, closed roster |
| D-086 | Five numeric government channels and no others |
| D-087 | Two policy axes, three settings each, free, one change per axis per 12 turns, effective next turn |
| D-088 | One political state row, idempotent P3.8 settlement, append-only political events, no sentiment in the crown ledger |
| D-089 | Six fixed constituencies with fixed weights summing to 100 |
| D-090 | Elections, retention, crises and every proposed penalty reserved for 06B; none of the proposed numbers adopted |
| D-091 | No government economically dominant (spread under 10% at every approval level tested) |

The permanent-government proposal was **evaluated, not assumed**. Model B (costly transition) was rejected because a transition is a hidden second balancing lever and needs a crisis design 06B owns; Model C (exceptional transition) because the exception becomes the model; Model D (free change) because it is the reference game's cosmetic model. The mitigation for regret is the already-approved instant reroll (D-039), not a new cooldown.

### 10.3 What was written and what was not

**Written:** population and its four inputs, the housing and food interfaces, six support formulas with named terms, approval movement, the stability target and its movement cap, derived legitimacy, the government table and its five channels, the policy tables, the political state fields, the settlement order, the event catalogue, ten invariants, the 06B input bundle and leadership-state vocabulary, the exploit register, the UX and accessibility requirements, the balance target and 18 examples.

**Deliberately not written:** every election, campaign, candidate, turnout, vote, retention, crisis, unrest and recovery rule; the proposed 240-turn interval, 24-turn aftermath, 36–48-turn crisis, 75% production cut and zero-tax period; any military modifier; any per-city or per-building government effect; any new resource, currency or income source.

### 10.4 Registers

| Register | Change |
|---|---|
| Requirements | **REQ-258…REQ-325** added (68 rows, all **Provisional**); total **325** |
| Decisions | **D-081…D-091** added; total **91** |
| Design positions | **DD-101…DD-111** added; total **111** |
| Unresolved | **UD-009 resolved** (two axes; stability multiplies tax only); **UD-034** (elections/thresholds) and **UD-035** (crisis penalties) added as 06B-deferred; total **35** (20 resolved, 10 deferred, 5 open) |
| Outline | B-06 now names both authoritative documents, the research report, what 06A delivered and what 06B owns; status **06A foundation complete; 06B pending** |
| Roadmap | Prompt 06 split into **06A (complete)** and **06B (next)** |

### 10.5 Validation (actual results, 2026-10-25)

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **234/234 checks passed** — all 18 examples, the government table, the weights and vectors, every published term range, the prose tokens of the corrected values, and the document guards (18 examples, F-PD-001…F-PD-025, D-084/D-091, REQ-325) |
| `python qa_backups/09_validate.py` | **340/340 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`** |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** |
| `python qa_backups/test_next_action.py` | **15 tests — OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 checks passed** — B-04 was not edited by 06A |
| `python qa_backups/verify_city_numbers.py` | **267/267 checks passed** — B-05 was not edited by 06A |

**Mutation check (executed, restored):** changing Example 8's prose token from `= 5,520` to `= 5,519` made the politics checker fail with **`E8 weighted sum in prose: false`** and exit 1; the file was restored and the checker re-passed **234/234**. This proves the guard reads the specification, not only its own constants. It is a document check, not a runtime test.

**What these checks are:** document arithmetic and cross-file consistency. **What they are not:** a runtime test, a simulation, or evidence that any political rule is implemented. **0 of the 68 T06 validation methods has been executed**; they remain planned.

### 10.6 Corrections found and fixed during this prompt

| Defect | Fix |
|---|---|
| The register's first draft listed F-PD-011 before F-PD-010 | Sections reordered so the IDs run in sequence |
| Example 10's junta net was first written as 125 | Recomputed to **126** (`ceil(31 × 1.05) = 33`), and the democracy/junta crossover corrected to **approval 75** |
| Example 8's weighted approval sum was first written as 5,510 | Recomputed to **5,520** (approval 55) |
| DMP-031 said crowding "converges on housing over roughly 22 turns" | Corrected: the excess falls by about **10% a turn**, so under 1,000 people remain over the cap after 22 turns |
| Example 1 said stability reaches 10,200 on turn 2 | Corrected: creation stores 10,000 and the **first** settlement moves it to 10,200 (inside the 250 bp cap) |

### 10.6a Acceptance reconciliation (v1.2 / register v1.1, 2026-10-25)

A second read of the published formulas against their own examples found seven defects that the first checker had not covered. All were corrected in the documents, not only in the prose, and the checker was extended so they cannot return:

| Defect | Fix |
|---|---|
| The register's six constituency **Range** cells understated or misstated their own terms: food and processing shares said +16 where the formula allows **0…+40**; rural service said +8 where the maximum is **+5**; the stability terms said ±4 where the floor of 5,000 gives **−10** (rural) or **−13** (industry, commerce, security); labour tax said ±3 where floor gives **−3…+2**; industry said ±6 where floor gives **−7…+6**; commerce said ±8 where floor gives **−9…+8** | Each Range cell now states the true bound at the documented input limits, and the verifier computes those bounds and guards the constant table (38 checks more than v1.1) |
| DMP-066 called labour's tax sensitivity "the lowest of the taxed groups (−3…+3)" | Scholars are lower (±2) and the range was wrong; rewritten as "small (−3…+2)" with no superlative |
| DMP-094 valued 300 bp of stability at **0.45 crowns** per turn | At 50,000 people and a 300 bp rate it is **4.5 crowns**; corrected |
| DMP-097 illustrated `HIGH` with 300 bp tax and a 75-crown cost, which is not a setting | Corrected to `HIGH`'s 400 bp: tax 200, service 100, **net 100** — consistent with Example 5 and DMP-168 |
| DMP-169 said `OPEN` *costs* about 2 approval points | `OPEN` **gains** about 2 points (57 vs 55); `FIRM` loses them (53). Rewritten, with the 64 bp / 20 bp stability equivalence |
| Example 10's junta target read 10,550 at approval 60; Example 16 said the technocracy and junta give up 360 crowns | The junta target is **10,600** (the cap); the ten-day gaps against the absolute monarchy are **600** and **240** crowns. DMP-166's approval-40 spread is stated as **8.1% of the best** to match the denominator used at the other approval levels |
| DMP-112 claimed "exactly these fields" but DMP-120 and DMP-123 referenced `approval_last_turn`, `stability_last_turn` and `politics_version`, which were not stored | The three fields were added to the state table; DMP-113's creation values and DMP-114's write step now set them |

**Result after the reconciliation:** `verify_politics_numbers.py` **234/234**, `09_validate.py` **340/340**, `validate_final.py` pass, `test_decision_registers.py` 12 tests OK, `test_next_action.py` 15 tests OK, `verify_economy_numbers.py` **146/146**, `verify_city_numbers.py` **267/267**. No coefficient, formula or example input changed — only bounds, prose and two example figures that disagreed with their own arithmetic.

### 10.6b Final micro-correction (v1.3 / register v1.2, 2026-10-25)

An independent review found two mathematical inconsistencies and three stale handoff instructions. Both inconsistencies were fixed at their authoritative source; no coefficient, weight, government or policy changed.

| Defect | Fix |
|---|---|
| **F-PD-002 did not enforce the 1,000 floor on the growth path.** A nation at 1,000 people with approval 0, housing 45,000 and hunger 3,000 gives `growth_bp = 50 + floor(−55/2) + 15 − 100 = −63`, `natural = 1,000 + floor(1,000 × −63/10,000) = 993`, and the published expression returned **993** | The expression now computes `raw` on both the growth/cap and crowding paths and returns **`max(1,000, raw)`**; the 993 case is documented as raw-with-floor-applied. The floor is applied **after** the growth rounding and the crowding decline, so no path can return below 1,000, and at the floor a further negative rate holds the population at 1,000 rather than banking a debt of people |
| **Three constituency tax terms exceeded their published ranges** because `−floor((tax − 300)/step)` rounds negative values up: Labour reached **+3** (range −3…+2), Industry **+7** (−7…+6) and Commerce **+9** (−9…+8) at the `LOW` rate | The three terms are now the signed **`(300 − tax_bp) // divisor`**, which gives exactly **+2 / +6 / +8** at 200 bp, 0 at 300 bp and **−3 / −7 / −9** at 400 bp. DMP-071a publishes the endpoints; Example 5 supports became **59/63/49/42/58/50** (approval 54), DMP-099 and DMP-168's `LOW` approval became **56**, and D-091's fiscal triple became **56 / 55 / 54** |
| The verifier's `apply_growth()` had the same missing floor, so it could not catch the first defect | `apply_growth()` now clamps both branches; the review example, ordinary positive and negative growth, the housing cap, the crowding path, rounding and repeated settlement are asserted |
| The register's Range cells did not state the permitted tax rates | Cells now read `−3…+2 at 200/300/400`, `−7…+6 at 200/300/400` and `−9…+8 at 200/300/400` |
| `stage-2/00_stage_2_handoff.md` §10 still sent the reader to the general Prompt 06; `stage-2/01_stage_2_prompt_roadmap.md` §0 still showed row 06 as "Next task — not started"; `PROJECT_PROGRESS.md` still said "Prompt 06 is next and not started" and "the current next action is Prompt 06" | All four now name **Prompt 06B** as the next task, state that 06A is complete as a foundation only, and instruct 06B to reuse the accepted population, government, constituency, approval and policy formulas instead of creating a second foundation. Historical rows are labelled historical |

This is recorded as a **specification correction**, not a new design decision: the 1,000 floor was already approved (DMP-025, REQ-259) and the endpoints were already published (REQ-275). No new `D-` entry was created for it.

### 10.6c Validation after the final micro-correction (2026-10-25)

All commands were run from `docs/` with `PYTHONIOENCODING=utf-8`:

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **309/309 checks passed** (234 at the acceptance run, +73 for the floor, the signed tax terms, endpoint/threshold/range/monotonicity checks and the document guards, +2 for repeated settlement) |
| `python qa_backups/09_validate.py` | **340/340 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`** |
| `python qa_backups/test_next_action.py` | **15 tests — OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 checks passed** — B-04 was not edited |
| `python qa_backups/verify_city_numbers.py` | **267/267 checks passed** — B-05 was not edited |

**Mutation checks (executed on temporary copies, then deleted; the repository files were not altered):** restoring the unfloored growth path produced **5 failures** (`FLOOR applied: got 993, want 1000`; `FLOOR raw below minimum`; `FLOOR crowding path: got 999`; both repeated-settlement checks), and restoring `−((tax − 300) // step)` produced **42 failures**, including all six `REGRESSION … not …` assertions, the three range checks and the affected Example 5 approval figures. The checker therefore fails if either defect returns.

### 10.6d Source synchronisation and verifier repair (v1.4, 2026-10-25)

A second independent review found that the formula **blocks** had not followed the register, that the verifier still held the superseded helpers, and that one AI-context index row was stale. A green checker had hidden a red document: this pass fixes both and makes the checker read the published blocks.

| Defect | Fix |
|---|---|
| **DMP-066, DMP-068 and DMP-069 still carried `− floor((tax_bp − 300) / divisor)`** although F-PD-004/006/007 had been corrected to the signed form in v1.3. The same tax rate therefore produced different support depending on which document a developer read | All three blocks now publish `+ (300 − tax_bp) // divisor`, exactly matching the register |
| The same latent divergence existed in **DMP-067 (Rural, 20)** and **DMP-070 (Scholars, 50)**, which v1.3 had left in the floor form on the argument that 100 divides exactly by 20 and 50. It does — at 200/300/400 only. At 250 the floor form gives **+3** where the register gives **+2**, so the argument was wrong and the prose disagreed with its own authority | Both blocks now use the signed form too, and DMP-071a says why: the two notations are not interchangeable between settings. **All five** tax terms are signed |
| The verifier's **“term ranges stated in the register”** section still defined `labour_tax_term`, `industry_tax_term` and `commerce_tax_term` as the old `-((tax - 300) // step)` and expected **+3 / +7 / +9** and **−2 / −6 / −8** — directly contradicting the register it claimed to check, while the rest of the file used the corrected term | The three helpers are replaced by one `tax_term(tax, step)` implementation, used for all five groups; the block now asserts the true endpoints (+2/−3, +6/−7, +8/−9, +5/−5, +2/−2), the bounds over 200…400, and the 250 bp divergence that defeats the “exact divisor” argument |
| No check read the DMP entries themselves, so a stale block passed indefinitely | Four new assertions per group extract the published section (`dmp_section`) and require the signed term in **both** B-06 and the register, forbid the old term in both, plus one global absence check per divisor (25 checks) |
| `AI_CONTEXT.md` line 111 still described the Stage 2 handoff's next action as “**Prompt 06** (Prompts 01–05 complete)” while the STATUS block said `stage_2_next_prompt: 06B` | The index row now names **Prompt 06B** and states that 06A is a completed foundation and the full Prompt 06 is not complete until 06B is accepted |
| The same headers still counted **309** checks and **B-06 v1.3** | `AI_CONTEXT`, `AI_HANDOFF`, `PROJECT_PROGRESS`, the Stage 2 handoff, the roadmap row and this log were re-synchronised to **345/345** and **v1.4**; the earlier 234 and 309 runs stay visible as history |

**Mutation checks (executed on temporary copies, then deleted; the repository files were not altered):** restoring the floor form in each group in turn made the checker exit **1** with **3 failures** every time — `<group> signed tax term in B-06`, `<group> superseded floor term absent from B-06`, and `no superseded tax term /<divisor> anywhere in B-06`; the clean copy passed **345/345**. The population floor was mutated three ways with the same result: removing `max(1,000, raw)` from F-PD-002 failed **`F-PD-002 floor expression`**, changing the register's 993 example failed **`F-PD-002 floor example`**, and removing the clamp from DMP-030a failed **`DMP-030a states the clamp`** — one failure each, exit 1. The earlier arithmetic mutation still holds: the old `−((tax − 300) // step)` term fails the six `REGRESSION` checks.

**Limits.** These are document and arithmetic checks. Nothing here is a runtime test: population, approval, stability, elections and unrest are **not implemented**, and **0 of the 68 T06 validation methods has been executed**.

### 10.7 What Prompt 06B was asked to do — historical snapshot

1. Read [B-06 §17](12_population_and_domestic_politics.md) and the register's §12 reserved list.
2. Consume — never redefine — `approval`, `stability_bp`, `legitimacy`, the six supports, the weights and the political state.
3. Define the election interval, turnout, vote, candidate registration, campaigns and the consequence of losing; the non-electoral retention test; crisis severity; unrest; recovery; and the leadership-state transitions.
4. Publish every formula as a new `F-PD-` row in the **same** register and every requirement from **REQ-326** onward.
5. Test any crisis penalty against B-04's ledger and B-05's capacity before adopting it — the brief's 75% production cut and zero-tax period are **not** adopted.
6. State explicitly that the economic balance table (D-091) does not yet price any political consequence.

---

## 11. Prompt 06B — the interactive political system (complete, 2026-10-25)

### 11.1 What was written

| Deliverable | Content |
|---|---|
| [B-06](12_population_and_domestic_politics.md) **v2.0**, Part II §24–§39 | The one abstraction that makes defeat survivable; the election cycle and its five dates; candidacy; the three campaign actions; the vote and its turnout weights; the tie-break; the confidence motion; the 12-turn transition; continuous retention; the crisis and recovery; the six-state machine; the P4.4 settlement; the modelling of the rejected penalties; fairness and anti-exploit; the Prompt 07–15 contracts; the verification map; **31 worked examples E19–E49** |
| [formula register](12_population_and_domestic_politics_formula_register.md) **v2.0** | **F-PD-026…F-PD-044** — the stability penalty by state, the schedule, the campaign window, the action cost, the capped bonus, the election score, the incumbent and challenger scores, the result and tie-break, the confidence score, the control margin and band, the pressure counter, the state durations, postponement, early exit, immunity, the first contest, contest idempotency and the audit record. F-PD-017 gains the single `political_stability_penalty_bp` term |
| [research](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md) | The 06B section: P&W has no live election system, no mechanical approval, and changeable government types; the forum proposals and their objections; the player-experience and feasibility analysis of every proposal |
| [requirements](03_requirements_traceability.md) **v1.9** | **REQ-326…REQ-426** — 101 rows across schedule, candidacy, campaign, vote, confidence, transition, retention, crisis, state, economics, anti-exploit and documents |
| [design decisions](04_approved_and_provisional_decisions.md) **v2.1** | **D-092…D-105** and **DD-112…DD-119** |
| [unresolved register](05_unresolved_design_decisions.md) **v1.10** | **UD-034** and **UD-035** resolved; the register is now 22 resolved / 8 deferred / 5 open, with no class-A row |

### 11.2 Final disposition of every proposal

| Proposal | Disposition |
|---|---|
| Elections every 240 turns | **Adopted unchanged**, with a per-nation anchor and published phases |
| Campaigning by the incumbent | **Adopted**, as three capped actions and a six-point platform |
| 24-turn democratic loss of office | **Rejected**; a **12-turn transition** that blocks new orders but not access |
| Non-electoral retention systems | **Adopted**, as one continuous legitimacy test per government |
| 36–48-turn unrest | **Rejected**; an **18-turn crisis**, ending early on recovery |
| 75% production reduction | **Rejected**; production is untouched in every state |
| Zero tax during unrest | **Rejected**; tax continues through the one stability term |
| Permanent government identity | **Preserved**; a defeat replaces the administration |
| More interactive politics | **Adopted**; the campaign, the retention test and the interventions are the interaction |
| Caretaker / restricted command | **Adopted in the narrower form**: a caretaker with six duties, no budget and no discretion |

### 11.3 Validation actually run (2026-10-25)

| Command | Result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **488/488 checks passed** — the 31 examples, the schedule, the campaign costs and cap, the turnout weights, the vote and challengers, the confidence motion, the retention thresholds and band, the state durations, the crisis and recovery economics, the rejected-penalty record and the published blocks |
| `python qa_backups/verify_economy_numbers.py` | **146/146 passed** — B-04 was not edited |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** — B-05 was not edited |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** after the true UD counts (22/8/5) and D-001…D-105 were adopted |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/09_validate.py` | passed |
| `python qa_backups/validate_final.py` | passed |

**Limits.** These are document and arithmetic checks. No scheduler, database, campaign-action table, contest record, state machine, interface or player test exists. **0 of the 101 T06B methods has been executed as a runtime test**, and the design is not proven fun, balanced or exploit-free: it is proven arithmetically consistent with B-04, B-05 and Part I at the published points.

### 11.4 What Prompt 07 inherits

Prompt 07 must read [B-06 Part II §36](12_population_and_domestic_politics.md) before writing a trade rule: market **read** access survives a transition and a crisis, no offer may be created, accepted or cancelled while authority is suspended, accepted trades settle normally, and 06B imposes no trade tax, tariff, embargo or market fee. It must not revise a political formula, and it must not treat `TRANSITION` as player inactivity.

---

## 12. Prompt 06B micro-correction (2026-10-28)

**Scope.** A corrective pass on the accepted Prompt 06. Six defects were confirmed against the real files: two election-state rules contradicted each other, the schedule's anchor could be read two ways, long dormancy had no catch-up policy, the rejected-crisis counterfactual mixed two rounding results, the formula register's metadata still described the 06B formulas as missing, and Part II's opening rule IDs collided with Part I's cross-system contracts. Prompt 07 was **not** started; no game code, schema, configuration or deployment was touched.

### 12.1 What changed

| Defect | Correction |
|---|---|
| A `NORMAL`-only postponement condition (old DMP-181, old F-PD-039, old REQ-330) sat beside a resolution rule that required `NORMAL` **or** `ELECTORAL` (DMP-236/F-PD-034) | A due contest resolves in `NORMAL` **or** `ELECTORAL`: the campaign window opens at the first eligible turn at or after `T − 24` and runs 24 turns to the resolution; `ELECTORAL` is preparation and is never a postponement condition. Preparation, scheduled resolution, forced postponement and exceptional challenges are now four distinct, published concepts (D-106, DD-120) |
| The next term could be read as `resolved_contest_turn + 240` (old DMP-177) while DMP-181/F-PD-027 used the scheduled turn | One rule everywhere: `next_contest_turn = scheduled_contest_turn + 240 × k`; `resolved_contest_turn` is recorded for the audit and **never** anchors the next term (D-106) |
| Long dormancy could leave the next contest in the past and a campaign window already expired | **DMP-181a** publishes the catch-up multiplier `k = ceil((resolved + 25 − scheduled) / 240)`; **DMP-181b** publishes the once-only window, opened as early as eligibility allows and never in the past. The worked table gives exact turns for recovery, dormancy, one missed cycle, several cycles and return at scale (D-107, DD-121) |
| DMP-246/E41/E42 computed `11 + 110 × 25 // 100 = 38` in one cell and used a rounded `39/turn` with `96` and `−372` in the others | One floor per division: **`38/turn`**; `1,500 − 36×38 = 132` (solvent); `1,500 − 48×38 = −324`; the first unpaid operating obligation is on **turn 40** (`39 × 38 = 1,482 ≤ 1,500`). "Insolvent" is defined as a cancelled obligation under D-052's no-debt rule, never an overdraft. This corrects a rejected counterfactual only — no accepted B-04 expense rule changed |
| The register's header said election/crisis formulas were absent and that Prompt 06B must append them; B-06's header still called 06B pending | Both headers now describe the real coverage (register **F-PD-001…F-PD-044**; B-06 Part I + Part II), the reconciliation date, and that nothing is implemented, migrated or runtime-tested and no balance is approved (B-06 v2.1, register v2.1) |
| DMP-134…172 were each defined **twice** — Part I's cross-system contracts and Part II's opening 39 rules | Part II renumbered **+39** (DMP-134…235 → DMP-173…274); every reference in B-06, the register and the checker updated; the checker now fails on a duplicate or unresolved rule ID (D-108, DD-122) |
| The election-consequence question had no register row | **UD-036** opened — a design-risk hypothesis for Prompt 14's simulation and a later experience review, explicitly **not** a confirmed player complaint |

### 12.2 Validation actually run on 2026-10-28

| Command | Result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **612/612 checks passed** — includes the new schedule model (16 state and edge cases with exact expected turns) and seven document guards |
| `python qa_backups/verify_politics_numbers.py --self-test` | **7/7 guards detected their reintroduced defect** — the failure-behaviour demonstration, run against in-memory copies only; no project file is modified by that mode |
| `python qa_backups/09_validate.py` | **341/341 passed** |
| `python qa_backups/validate_final.py` | **ALL CHECKS PASSED** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 passed** — B-04 was not edited |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** — B-05 was not edited |

**Limits.** These are document and arithmetic checks. No scheduler, database, contest record, state machine, interface or player test exists. Nothing in this correction is implemented or runtime-tested, the design is not proven fun or balanced, and UD-036 remains open.

### 12.3 What Prompt 07 inherits

Unchanged from §11.4, plus two rules: the political layer now publishes **one** schedule rule — window opened at the first eligible turn, resolution at the end of its 24 turns, anchor always taken from the scheduled turn — and every future document must cite the renumbered IDs (Part I holds DMP-001…172, Part II holds DMP-173…274).

---

## 13. Second 06B micro-correction — campaign lifecycle, no-debt accounting, status records (2026-10-28)

| Defect | Fix |
|---|---|
| `verify_politics_numbers.py` modelled every delay as a new 24-turn window: `max(scheduled − 24, eligible_from) + 24`. A campaign opened at 976 and blocked until 1010 therefore resolved at **1034** — 24 turns after the interruption — while DMP-181b said the clock does not restart. The old "Case C" asserted the wrong figure, so helper and test agreed with each other and not with the rule | The model is now a lifecycle: `simulate_contest()` finds the opening **once**, sets `window_deadline = opening + 24`, and resolves at the first eligible turn at or after `max(scheduled, deadline)`. 1000/976/1010 → **1010**. The superseded helper survives only as `superseded_resolution()`, asserted to return 1034 so a revert fails |
| **DMP-181** gave the rule in two clauses ("24 turns, or the first eligible turn after it") that could be read as either model | DMP-181 publishes the three-line rule, the word **once**, and the 1000/976/1010 → 1010 case with **not 1034**. DMP-181b adds the two-interruption case; F-PD-028 publishes `window_deadline` and the same resolution expression |
| DMP-246, E41 and E42 called `−324`, `−2,856` and `−4,308` "treasury". B-04 forbids a negative balance (ECN-102), has no debt (ECN-103) and **cancels** an unaffordable obligation (ECN-105/106), so those figures cannot be balances | Every negative figure is an **unconstrained cumulative cash-flow result**, defined once. The actual path is stated: A pays 12 full turns, turn 13 pays maintenance and only 37 of 110 variable cost, turn 14 loses maintenance; B pays 39 full turns, then turn 40 pays maintenance from 18, cancels the 27 of variable cost and ends at **7**. `+132` at 36 turns stays an actual balance because it is positive |
| The prompt table still read `06B … **Next — not started**` while the header and `PROJECT_PROGRESS.md` said complete; `09_validate.py` only required the labels to appear | The row is **Complete (with the 06B micro-corrections, 2026-10-28)** and row 07 is **Next task**. Both validators now read the structured status cell and require 06A/06B complete, 07 next, and eight pending rows |
| `SUCCESSION` was implied by "not one of the three blocking states", but DMP-236 named only `NORMAL` and `ELECTORAL` | DMP-235, DMP-236 and REQ-330 name `SUCCESSION` explicitly; the state table says it blocks no scheduled contest; the early motion keeps its separate 12-turn precondition |

**Regression coverage.** Four new document guards (the suite now has 11 self-tests, all detected) cover the once-only opening and the named 1034 defect, the cash-flow terminology and the forbidden "treasury −324" forms, `SUCCESSION` in the resolving-state list, and progress summary/table agreement. The schedule model's 16 cases were re-derived under the lifecycle model — old Case C and E expected values encoded the restart — and a six-state matrix was added: `NORMAL`, `ELECTORAL` and `SUCCESSION` resolve at 1000; `TRANSITION`, `CRISIS` and `RECOVERY` resolve at 1010 from the same interrupted window.

**Validation actually run after the final edit.**

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **670/670 checks passed** |
| `python qa_backups/verify_politics_numbers.py --self-test` | **11/11 guards detected their reintroduced defect** |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 passed** — B-04 not edited |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** — B-05 not edited |

**Limits.** Document and arithmetic checks only. No scheduler, contest record, state machine, interface or player test exists; nothing here is implemented or runtime-tested, and no balance is claimed.

**What Prompt 07 inherits.** Unchanged from §11.4 and §12.3, plus: a campaign is **one** window computed once at its first eligible turn and never reopened; a negative multi-turn figure is a cash-flow projection, never a treasury; and `SUCCESSION` does not postpone a scheduled contest.

---

## 14. Third 06B micro-correction — restoration, campaign deadlines, atomic batches (2026-10-28)

| Defect | Fix |
|---|---|
| An interrupted campaign that still had turns left returned to `NORMAL` when the blocker cleared, so the nation had an open window but no campaign actions | **DMP-181b** adds the restoration rule: the last blocker to clear before `window_deadline` restores **`ELECTORAL`** for the remaining turns; **DMP-235**'s table and **DMP-236**'s priority order state it; consecutive blockers with no eligible turn between them restore nothing; **DMP-183** says the window does not close |
| Deadline offsets were anchored on `T` in the narrative while F-PD-028 anchored them on `campaign_open_turn`, so a delayed campaign could be told to register at `T − 12` after it had opened | **DMP-178/183/184** and **F-PD-028** now all use `campaign_open_turn + 12/+22/+24`; `T − 12` and `T − 2` are the on-time coincidences. Worked: contest 1000 opened 980 → registration **992**, notice **1002**, deadline and resolution **1004** |
| E41's turn-13 narrative said "37 crowns against 110 of variable cost" without saying which whole batches could run; E42 still presented 38/turn as an actual trajectory | **DMP-246/E41/E42** now separate **A** (every batch runs, 121/turn; turn 13 = maintenance 11 + food `3 × 12 = 36` = 47, leaving 1; turn 14 unmaintained), **B-atomic** (`floor(3 × 25 / 100) = 0` per chain, 11/turn, **1,104** left at 36 and **972** at 48) and **B-proportional** (27 is not a batch cost; illustration only) |
| The "two interruptions" case was not two interruptions of the same open campaign | The 377 case is renamed; a genuine 1000/976 case with blocks 980–985 and 988–995 was added, plus restoration, no-gap and per-batch assertions |

**Regression coverage.** The suite grew to **809 checks** and **12 self-tested guards**: the new `campaign state and deadlines` guard catches a `T`-based registration row and a `NORMAL`-only restoration; `arithmetic_problems` now requires ECN-054, `B-atomic`, `1,104`, `972`, `3 × 12 = 36` and `floor(3 × 25 / 100) = 0`, and forbids calling the proportional 132 an actual balance. The model adds `campaign_record`, `campaign_actionable`, `restored_state`, seven deadline cases and a whole-batch payment simulator.

**Validation actually run after the final edit.**

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **809/809 checks passed** |
| `python qa_backups/verify_politics_numbers.py --self-test` | **12/12 guards detected their reintroduced defect** |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 passed** — B-04 not edited |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** — B-05 not edited |

**Limits.** Document and arithmetic checks only. No scheduler, contest record, state machine, interface or player test exists; nothing is implemented or runtime-tested, and no balance is claimed.

**What Prompt 07 inherits.** Unchanged from §11.4, §12.3 and §13.4, plus: an interrupted campaign restores `ELECTORAL` for its remainder; every campaign date belongs to the campaign's own opening; and a rejected counterfactual is modelled batch by batch, never as a percentage of a cost.

---

## 15. Fourth 06B micro-correction — delayed ballots, food stock, maintenance allocation, DMP-184 (2026-10-28)

| Defect | Fix |
|---|---|
| DMP-188 and DMP-190 fixed the ballot and the platform lock at `T − 12`, which for a delayed campaign is already in the past (a campaign opened at 980 has an authoritative registration close of 992) | **DMP-188/DMP-190** use the campaign's **`registration_close_turn`**; `T − 12` is named only as the on-time coincidence. Register **F-PD-028/F-PD-029** publish the submission limit as `turn_id < resolution_turn`, not `< T` |
| E41's Model A food stock said 120 → 85 → 35 with a first shortage on turn 15, contradicting its own 15-a-turn production, Example 43 and DMP-247 | The stock is recomputed from turn 1: **85, 50, 15, 0**; first shortage **turn 4** (unmet 20, 1,200 bp penalty), 35 a turn from turn 5, 50 on turn 14 with the food chain unmaintained. **DMP-246**, **E41** and **E42** now agree with **Example 43** |
| E41 treated the 11-crown maintenance as wholly paid or wholly cancelled, so the 1 crown left on turn 14 "cancelled everything" | Maintenance is one whole obligation per chain (ECN-147) paid in the §8.6 order, and ECN-105 continues past an unaffordable item: food (3) and coal (2) are cancelled, **oil (1) is paid**, iron (1), refining (2) and the generator (2) are cancelled. Five chains are `UNMAINTAINED`, the oil chain is maintained but idle, and the treasury closes at **0**, not 1 |
| DMP-184 ended in the fragment "At the next turn: the sta" and ran into the next section | Reconstructed from DMP-178/DMP-181a as a statement that adds no rule (banner returns to `NORMAL`, the term's first digest is published, the next contest date is shown). No earlier copy exists — the document is untracked in Git and has no backup — so the original wording is recorded as **unrecoverable** and the reconstruction is identified here. A new truncation guard prevents a repeat |

**Regression coverage.** **856 checks** and **14 self-tested guards**. New numeric models: `pay_maintenance` (whole-chain obligations, §8.6 order, skip-and-continue), `food_series` (production then consumption, stock clamped at 0, unmet demand), `ballot_turn`/`submission_legal` (the delayed ballot at 992, legal at `T`, closing at `resolution_turn`), with 20 new deadline and ballot assertions. New guards: `delayed ballots and accounting` and `truncated rules`; the latter catches the exact DMP-184 fragment when reintroduced into an in-memory copy and passes DMP-038/DMP-055, whose sentences legitimately continue after a display block.

**Validation actually run after the final edit.**

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **856/856 checks passed** |
| `python qa_backups/verify_politics_numbers.py --self-test` | **14/14 guards detected their reintroduced defect** |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **146/146 passed** — B-04 not edited |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** — B-05 not edited |

**Limits.** Document and arithmetic checks only. No scheduler, contest record, production engine, interface or player test exists; nothing is implemented or runtime-tested. The maintenance allocation is the whole-chain reading of ECN-147: B-04 defines no partial-maintenance state, so the chain is the only coherent unit. One unrelated B-04 observation is carried forward without change: Example 15 states maintenance 3 for capacities food 3 / coal 2 / oil 1, where F-EC-014 gives `3 + 2 + 1 = 6`; it is outside this pass's scope and is recorded for the next Prompt 04 touch.

**What Prompt 07 inherits.** Unchanged from §11.4–§14, plus: a delayed campaign's ballot closes at its own `registration_close_turn`; and the rejection of the 25% proposal now rests on a trajectory that is short of food from turn 4, not turn 15.

---

## 16. Consolidation and definitive acceptance audit (2026-10-28)

**Two findings remained after the fourth pass, and both were closed at their source rather than in a test.**

| Finding | Resolution |
|---|---|
| **DMP-184** returned the banner to `NORMAL` after *every* contest, including a defeat, which the state machine sends to `TRANSITION` for 12 turns | DMP-184 now states the **outcome-dependent** rule: `NORMAL` at `T + 1` when the incumbent is returned, `TRANSITION` for 12 turns with the 800 bp penalty when the incumbent loses (DMP-204, DMP-235), and the same after a postponed resolution. A new `post_election` model and 14 assertions cover win, loss, postponed win, postponed loss, the exact 12-turn window and repeat evaluation |
| The maintenance allocation existed only as a test assumption: B-04 published the priority class, the cancellation and the `UNMAINTAINED` mark, but not the **unit** or the **within-class order** | **ECN-147a** (B-04 **v1.3**) publishes both: maintenance is one **whole obligation per chain** (`capacity_batches × rate`, `generator_levels × 2`), attempted in the settlement order **extraction → generation → processing**, paid in full or cancelled in full, with the engine continuing past an unaffordable chain exactly as ECN-105 does for a batch. The standard-start 1-crown case is published: **oil** (1) is paid, food (3), coal (2), iron (1), generator (2) and refining (2) are cancelled, five chains are `UNMAINTAINED`, and the treasury is **0** |

**Consequences recorded, not hidden.** D-050 and DD-068 gained the allocation clause; D-106 and DD-120 gained the outcome rule. No decision or position ID was added, so the registers remain 108 decisions / 122 positions. The formula register is unchanged at **v2.4** because no formula value or definition changed; B-06 is **v2.5**, B-04 and its register are **v1.3**.

**Cross-document audit performed in this pass.**

- DMP-188/DMP-190 and F-PD-028/F-PD-029 use `registration_close_turn` / `turn_id < resolution_turn`; no unqualified `T − 12` or `T − 2` remains outside the "when on time" qualification.
- The 240-turn anchor, the once-only window, the restoration rule, the no-gap rule and the `NORMAL`/`ELECTORAL`/`SUCCESSION` resolving states are unchanged and still tested.
- Model A's food trajectory is recomputed from turn 1 (`85 / 50 / 15 / 0`, first shortage **turn 4**); B-atomic starves from turn 3; the proportional reading remains labelled an illustration. No negative stock or negative treasury is asserted anywhere.
- Every continuity file that quoted a version or a check count was searched and corrected: AI_CONTEXT, AI_HANDOFF, PROJECT_PROGRESS, the Stage 2 handoff, the roadmap, the outline and the decision register.
- The truncation guard now scans B-04 and its register as well as B-06, and still passes DMP-038/DMP-055, whose sentences resume after a display block.
- **Example 15** was carrying the same defect in miniature: it charged maintenance **3** for capacities food 3 / coal 2 / oil 1, where F-EC-014 gives 6. It now charges 6 and closes at **8** (was 11), with the obligation cancelled against 8. The economy checker recomputes the example and passed.

**Validation actually run after the final edit.**

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **870/870 checks passed** |
| `python qa_backups/verify_politics_numbers.py --self-test` | **14/14 guards detected their reintroduced defect** |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **164/164 passed** |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** |

**Limits.** Document and arithmetic checks only. No scheduler, contest record, production engine, interface or player test exists; nothing is implemented or runtime-tested. The maintenance allocation is a design rule awaiting Prompt 14 simulation, not a measured balance. The election-consequence question (UD-036) remains open by design.

**What Prompt 07 inherits.** Everything in §11.4–§15, plus: the post-election state follows the result; maintenance is allocated per chain in the settlement order; and B-04 v1.3 is the authoritative statement of both.

---

## 17. Cross-document reconciliation (2026-10-28)

**Trigger.** The final review of the accepted 06B set found that the arithmetic passed while the records around it had drifted: two confirmed decisions still described the pre-06B timing, six requirements carried unqualified `T-24`/`T-12`/`T-2` values or the `NORMAL`-only postponement, several continuity files quoted older register versions and counts, the Stage 2 roadmap stopped at §15, the root ROADMAP still showed Prompt 03 as next, and the handoff's opening still called Prompt 06B the next task. A green numeric suite had not caught any of it.

**Decision-log reconciliation.** **D-092** and **D-096** keep their original rationale and gain a dated revision clause rather than a silent rewrite. D-092 now derives every phase from `campaign_open_turn` (`T-24`/`T-12`/`T-2` are the on-time values), names `NORMAL`, `ELECTORAL` and `SUCCESSION` as the resolving states instead of `NORMAL` alone, and states that at the next turn the result is applied: a returned incumbent continues, while a defeated incumbent's account keeps the nation and enters the 12-turn caretaker `TRANSITION`. D-096 qualifies the 24-turn `ELECTORAL` period as anchored on the actual opening and records that a blocker may carry resolution past the deadline without reopening the window. No decision ID was added or removed; the registers remain **108 decisions / 122 positions**.

**Post-election administration.** B-06's DMP-178 table and Example 21 no longer say a "new administration takes office" as if a challenger received the nation. They now state the outcome-dependent result, and DMP-184 adds that the account remains the nation's controller in both cases while the caretaker runs only the committed state (DMP-175, DMP-207). This aligns the rulebook with D-097 and removes the last reading in which a simulated challenger could be mistaken for the account holder. The arithmetic verifier now asserts the authority consequence, not only the banner: `TRANSITION` and `CRISIS` block new executive orders, while a win, `RECOVERY` and `SUCCESSION` retain them (DMP-206/224/225/229).

**Requirements.** **REQ-328**, **REQ-332**, **REQ-337**, **REQ-338**, **REQ-356** and **REQ-419** now use the authoritative fields: `campaign_open_turn`, `registration_close_turn` and the resolution turn, with the ordinary `T-24`/`T-12`/`T-2` values labelled "when on time". REQ-328 states the caretaker result and that ownership never changes. REQ-332 no longer treats `T` as the universal closing boundary. The traceability header is **v1.13**; the requirement count is unchanged at **426**.

**Version and section references.** Actual headers are **B-06 v2.5** and **register v2.4** (B-04 and its register **v1.3**). `PROJECT_PROGRESS` row 06, the Stage 2 handoff's Prompt 06 record, the roadmap row, the outline entry, the AI context header and the AI handoff record now cite v2.4; the handoff's own "B-06 v2.3 / next 06B" opening is corrected to v2.5 and Prompt 07. The Stage 2 roadmap's Prompt 06 range now ends at **§17**, this section, and the root ROADMAP records Prompts 01–06 complete with Prompt 07 next.

**New source-reference guard.** `validate_final.py` now checks six current-status rows against the register's own header, the roadmap's progress-log range against the sections that exist, and the decision/requirement wording against the superseded phrases. Its `--self-test` feeds three in-memory fixtures (stale version, stale section range, stale election wording) and requires each guard to reject its defect; the normal run adds the same checks to the cross-file verdict.

**Validation actually run after the final edit.**

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **876/876 checks passed** |
| `python qa_backups/verify_politics_numbers.py --self-test` | **14/14 guards detected their reintroduced defect** |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py --self-test` | **3/3 reference guards detected their defect** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **164/164 passed** |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** |

**Limits.** These remain document, arithmetic and mutation checks. No scheduler, contest record, production engine or interface exists, so nothing here is runtime-tested. D-092/D-096's revision is a clarification of an accepted rule, not a new balance decision; the maintenance allocation and campaign costs still await Prompt 14 simulation. **Prompt 07 has not started.**


---

## 18. Publication timing and catch-up correction (2026-10-28)

**Trigger.** The final review of the accepted set found two decision-log defects that the arithmetic could not see, because both are statements in [DECISIONS](../DECISIONS.md) rather than formulas: **D-093** published the two challengers "at `T-24`", which reads as universal although a delayed campaign publishes at its own opening (DMP-186: "At campaign open"); and **D-092** advanced the anchor with "`scheduled_contest_turn + 240` afterwards", which is silent about D-107's `k > 1` catch-up after long dormancy.

**D-093 — publication follows the opening.** The authoritative rule was already correct: DMP-186 publishes the challengers at campaign open, and DMP-178/DMP-184 derive every date from `campaign_open_turn`. D-093 now says "published at `campaign_open_turn` — `T-24` only when the campaign opens on time (D-106, DMP-186)", with a dated revision clause that keeps the original wording's history visible. No publication content, standing floor, score formula or candidate rule changed; the on-time `T-24` case remains documented.

**D-092 — the catch-up stays in D-107.** D-092 now records `creation_turn + 240` for the first contest, then a scheduled-turn anchor with no resolution-turn step, and defers the complete calculation — the ordinary one-interval step and the `scheduled_contest_turn + 240 × k` skip after long dormancy — to **D-107**, including its `next ≥ resolved_turn + 25` guarantee. A dated revision clause states that the original `+240` is the `k = 1` case only. D-107 itself was not edited, so the authoritative formula keeps one owner.

**Decision summary.** [stage-2/04](04_approved_and_provisional_decisions.md) is **v2.8**: **D-092**, **D-093**, **DD-112** and **DD-120** carry the same publication and catch-up language. No decision ID, position ID or tally changed.

**Regression coverage.** `qa_backups/verify_politics_numbers.py` gained two guards that read the operative decision row rather than a summary mention:

- `publication_timing_problems` rejects a universal `T-24` publication in D-093, requires `campaign_open_turn`, requires the explicit on-time qualification, checks the D-093 summary row, and checks that DMP-186 still says "At campaign open".
- `catch_up_crossref_problems` rejects the superseded single-step phrase, requires the D-107 cross-reference and `240 × k` in D-092, requires D-107 in the summary's D-092/DD-112/DD-120 rows, and confirms that D-107 still owns its formula and 25-turn guarantee.

Both run in `--self-test`, which reintroduces the original wording in memory and requires each guard to reject it. Existing election, deadline, ballot, dormancy, state, outcome, caretaker, identifier, version and next-action checks were left unchanged.

**Focused experiment.** The original D-093 and D-092 wording was temporarily restored in the working `DECISIONS.md`. The checker exited **1** with exactly the two new guard failures, was restored from a byte-for-byte backup, and its SHA-256 was confirmed unchanged (`487896f8…`); the checker then passed **878/878** again.

**Cross-document check.** D-107 is unchanged; the domestic-politics rulebook stays **v2.5** and its formula register **v2.4** because no rule content changed; REQ-327/REQ-328 already publish `scheduled_contest_turn + 240 × k` and `campaign_open_turn`; the Stage 2 handoff, both roadmaps, the AI context and the AI handoff still name **Prompt 07** as next and do not claim it has started.

**Validation actually run after the final edit.**

| Command | Actual result |
|---|---|
| `python qa_backups/verify_politics_numbers.py` | **878/878 checks passed** |
| `python qa_backups/verify_politics_numbers.py --self-test` | **16/16 guards detected their reintroduced defect** |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** |
| `python qa_backups/validate_final.py --self-test` | **3/3 reference guards detected their defect** |
| `python qa_backups/test_next_action.py` | **15 tests OK** |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** |
| `python qa_backups/verify_economy_numbers.py` | **164/164 passed** |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** |

**Limits.** Document, arithmetic and mutation checks only. No scheduler, contest record, publication surface or interface exists, so none of this is runtime-tested. The correction changes decision-register wording, not an election mechanic: 240-turn cadence, the 24-turn window, registration, ballot and platform locking, resolution states, caretaker rules and D-107's catch-up all stand as accepted.

---

## 19. Handoff election-timing clarification (2026-10-28)

**Trigger.** The final review of the accepted set found the last ambiguity outside the register: the opening summary in [AI_HANDOFF](../AI_HANDOFF.md) described the cycle as "`campaign_open_turn` = `T-24`" and "a delayed opening takes the same offsets". DMP-181 computes the opening as the first eligible turn ≥ `scheduled_contest_turn − 24`, **once**, so `T-24` is only the on-time coincidence; a contest due at 1000 that opens at 980 runs its 24 turns from 980. [AI_CONTEXT](../AI_CONTEXT.md) carried the same class of wording ("phases at `T-24`/`T-12`/`T-2`").

**Correction.** The handoff opening now keeps four concepts apart: the **scheduled contest turn** `T` (the anchor), the **actual `campaign_open_turn`** (first eligible turn ≥ `T − 24`, computed once), the **ordinary on-time values** (`T-24` opening, `T-12` registration, `T-2` notice, `T` deadline) and the **resolution turn** (the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)`). It records registration at `campaign_open_turn + 12` (992 in the delayed case), notice at `+22` (1002), deadline at `+24` (1004) and the no-second-window rule. AI_CONTEXT anchors its phases on `campaign_open_turn` and labels the fixed dates as the on-time values only. No rule, decision, requirement, formula, version or ID changed: D-093 remains as corrected in §18, D-092 defers to D-107, and D-107 was not edited.

**Regression coverage.** `handoff_timing_problems` reads the handoff paragraph that names `campaign_open_turn` and rejects the unconditional identity (`campaign_open_turn = T-24`), then requires the actual-opening definition, `computed once`, the explicit on-time qualification, `campaign_open_turn + 12`, `max(scheduled_contest_turn, window_deadline)` and the no-second-window rule. It also rejects fixed `phases at T-24` in AI_CONTEXT and requires that summary to anchor on `campaign_open_turn` and qualify the ordinary dates. Two `--self-test` mutations restore the original handoff clause and the original context phase list, and each must fail the guard. The script now also reconfigures stdout to UTF-8 so its `−`/`≥` diagnostics cannot crash a cp1252 console; assertions and exit codes are unchanged. Existing election, deadline, ballot, dormancy, state, outcome, caretaker, identifier, version, publication/catch-up and next-action checks were unchanged.

**Focused experiment.** The opening definition was temporarily replaced in the working `AI_HANDOFF.md` with the unconditional identity (`campaign_open_turn = T-24`). The checker exited **1** with one failure — `guard: handoff election timing` — naming the identity, the missing `computed once` and the missing on-time qualification; the file was restored in the same process and its SHA-256 matched (`0669ad18…`), after which the checker passed **879/879**. The context mutation is covered by `--self-test`, which proves the same rejection in memory.

**Cross-document check.** D-092, D-093 and D-107 are unchanged by this pass; the rulebook stays **v2.5** and its register **v2.4**; the Stage 2 handoff, both roadmaps, AI_CONTEXT, the AI handoff and this log name **Prompt 07** as next and do not claim it has started.

**Validation actually run after the final edit.**

| Command | Actual result | Exit |
|---|---|---|
| `python qa_backups/verify_politics_numbers.py` | **879/879 checks passed** | 0 |
| `python qa_backups/verify_politics_numbers.py --self-test` | **18/18 guards detected their reintroduced defect; 879/879 document checks passed** | 0 |
| `python qa_backups/09_validate.py` | **343/343 passed — ALL CHECKS PASSED** | 0 |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** | 0 |
| `python qa_backups/validate_final.py --self-test` | **3/3 reference guards detected their defect** | 0 |
| `python qa_backups/test_next_action.py` | **15 tests OK** | 0 |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** | 0 |
| `python qa_backups/verify_economy_numbers.py` | **164/164 passed** | 0 |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** | 0 |

**Limits.** Document, arithmetic and mutation checks only. No scheduler, contest record, publication surface or interface exists, so nothing here is runtime-tested. No election rule changed: the pass corrects two summaries and adds one guard. **Prompt 07 had not started at the time of this pass**; its research stage is recorded in §20.

---

## 20. Prompt 07A — Politics & War market research (2026-10-28)

**Trigger and scope.** The owner split Prompt 07 into **07A research**, **07B market foundations** and **07C workflows/acceptance**, and authorized 07A as a **research-and-documentation-only** task. 07A was required to investigate Politics & War as the **only** external game reference, preserve Prompts 01–06B, and hand evidence to 07B without designing Nation Supremacy's market. No game code, schema, migration, deployment or account action was authorized or performed.

**Deliverable.** [research/07A_politics_and_war_market_research.md](research/07A_politics_and_war_market_research.md) — **v1.0**, **1,083 lines**, **14 sections**, **22 sources** (`PWS-001`…`PWS-022`) and **30 findings** (`PWR-001`…`PWR-030`). Each finding carries an evidence class, a confidence level, its sources, a current/historical status and an open question. The report includes a source register, a gaps section, a relevance-to-Nation-Supremacy section and a self-contained 07B handoff.

**What the evidence establishes.** Politics & War's global market is a **posted-offer board with manual acceptance**; no automatic matching is documented, and a 2019 player states there is none. An offer shows a **quantity, a money return and a unit price**; the public history's totals are arithmetically consistent with `return = quantity × unit price`. Offers **persist for days** and can be accepted later. A clicked offer can fail for **insufficient resources or cash**, which is consistent with **no reservation at posting** — a historical, single-source observation whose mechanism is inferred. The trade page publishes a **Current Market Index**, per-resource **Average Prices** and a **60-day history**; the averages are end-of-day and, per players, **global-market-only**. Completed trades are **public per nation**. **Global, alliance and private** surfaces are referred to. Official rules impose **one nation per person**, **same-network interaction bans**, a **new-nation transfer restriction** and an **anti-automation** rule; the community FAQ adds a **±30% band** for nations under 30 days and for same-network-flagged nations. **No trade fee is documented** in the sources reached; **matching priority, partial fills and expiry are undocumented**.

**Player experience.** Best-supported positive experiences: the two-path model (take an offer or make one), asynchronous offers, legible quantity/total/unit price, public price context and history, public trade history, and multiple trust-level channels. Best-supported frustrations: stale or unfunded offers failing on click (2015, single source), crossed offers with no matching (2019, single player), trade spam and the 2022 per-resource offer-cap direction (official staff post), confirmation fatigue (2022, single player) and a 2014 trade-activity display complaint. **No prevalence, liquidity, volume, fee or balance claim is made.**

**Authenticated access.** The owner's existing Chrome session was **not accessible**. The environment's Chromium preview tool does not share the Chrome profile or the Politics & War session; no sign-in was attempted, no password/code/cookie was requested, and no order, cancellation or account change was made. Only the **public logged-out** trade page and a **public nation trade-activity page** were observed (2026-10-28). The create-offer form, any reservation display, fees, partial fills, cancellation, expiry and failure messages were therefore **not observed**. Several official-forum bodies rendered only as indexed excerpts; the limitations are recorded per source (`PWS-007`…`PWS-018`, `PWS-022`). The Fandom HTML returned 403, so the same pages' wikitext was read through `?action=raw`.

**No design change.** 07A added **no** `D-`, `DD-`, `UD-`, `REQ-`, `F-` or `T` ID and changed **no** existing rule. The decision register, requirements register and unresolved register were **not edited**. The report states repeatedly that it approves **no** Nation Supremacy market model, fee, limit, price band, reservation rule, settlement rule or tradable-resource list. Its §14.7 records the existing constraints 07B must reconcile, including D-016, D-017, REQ-010's **unpassed** G-1…G-6 gate, ECN-211's P4/`transfer_id`/warehouse contract, ECN-027/ECN-109's book-versus-market distinction, B-03 ONB-031/ONB-032 and ECN-208's band/window, the D-034 pair matrix and **DMP-262** (B-06 §36: read-only market during `TRANSITION`/`CRISIS`).

**Continuity updated.** [AI_CONTEXT](../AI_CONTEXT.md) (header, status paragraph and a new index row), [AI_HANDOFF](../AI_HANDOFF.md) (header, status sentence, a new §0 and the existing market-questions note), [PROJECT_PROGRESS](../PROJECT_PROGRESS.md) (header, Stage 2 heading, row 07 and the paragraph below the table), [stage-2/00](00_stage_2_handoff.md) (revision header, status and §10 next action), [the roadmap](01_stage_2_prompt_roadmap.md) (status, row 07 and the Prompt 07 section) and this log (header, row 07 and §20). `stage_2_next_prompt` stays **07** in all three STATUS blocks because 07 is the active prompt number; the prose distinguishes **07A complete** from **07B next**. No historical section was rewritten except to mark §19's "Prompt 07 has not started" as true **at that time**.

**Validation actually run after the edits.**

| Command | Actual result | Exit |
|---|---|---|
| `python qa_backups/verify_politics_numbers.py` | **879/879 checks passed** | 0 |
| `python qa_backups/verify_politics_numbers.py --self-test` | **18/18 guards detected their defect; 879/879 document checks passed** | 0 |
| `python qa_backups/09_validate.py` | **343/343 checks passed — ALL CHECKS PASSED** | 0 |
| `python qa_backups/validate_final.py` | **VALIDATION: ALL CHECKS PASSED** | 0 |
| `python qa_backups/validate_final.py --self-test` | **3/3 guards detected their defect** | 0 |
| `python qa_backups/test_next_action.py` | **15 tests OK** | 0 |
| `python qa_backups/test_decision_registers.py` | **12 tests OK** | 0 |
| `python qa_backups/verify_economy_numbers.py` | **164/164 passed** | 0 |
| `python qa_backups/verify_city_numbers.py` | **267/267 passed** | 0 |

**Report-integrity checks (manual, this pass).** 14 `## Section` headings present in order; **22** unique `PWS-` register rows; **30** unique `PWR-` register rows; **no** duplicate source or finding ID; **no** `<!-- APPEND -->` sentinel left; all seven evidence labels used. The report's internal cross-references were spot-checked against the source register.

**One validator repair, disclosed.** The first run after §20 was added failed `validate_final.py` with **`roadmap log range ends at §19, latest is §20`**. The check had assumed the **Prompt 06** roadmap row must end at the newest log section; that assumption stopped being true when a later prompt's research section was appended. The check now (a) still verifies every section the Prompt 06 row cites exists, and (b) requires **some** roadmap row to cite the latest log section, across the register's rows. The `--self-test` fixture was updated to the new, stronger coverage assertion (`no roadmap row cites the latest log §16`). This is a repair of a stale assumption, not a weakened check: an uncited newest section still fails. Rerun: **3/3 guards** and **ALL CHECKS PASSED**; `09_validate.py` remains **343/343**.

**Limits.** Documentary research only. No interface state was changed and no runtime behaviour was tested. The report's 07A status is **conditionally complete in evidence depth**: the structure, public interfaces and official rules are documented, but the authenticated form/fee/reservation/partial-fill questions remain open and are explicitly listed in §12. This does **not** make 07A a failed prompt; it makes the limits visible. **Prompt 07B has not started; Prompt 07C and Prompt 08 have not started.**

## 21. Prompt 07B — market foundations (2026-10-28)

**Trigger and scope.** The owner split Prompt 07 into **07A research**, **07B market foundations** and **07C workflows and acceptance**, and authorized 07B as a **design-and-documentation-only** task. 07B had to use the completed 07A report as evidence, preserve Prompts 01–06B and every accepted decision, define the **directed-trade** system and the **required long-term Global Trade** market, register new formulas, requirements and decisions, and leave 07C an unambiguous handoff. No game code, migration, deployment or live-world change was authorized.

### 21.1 What was written

| Deliverable | State |
|---|---|
| [`13_trade_and_markets.md`](13_trade_and_markets.md) | **v1.0**, **1,367 lines**, **32 sections**, **237** `MKT-` rules (**235 numbered** `MKT-001`…`MKT-235`, plus sub-rules `MKT-215a`/`215b`), **21** worked examples (`E01`…`E21`) and **35** enumerated failure cases |
| [`13_trade_and_markets_formula_register.md`](13_trade_and_markets_formula_register.md) | **v1.0**, **531 lines**; formulas `F-TM-001`…`F-TM-039`, plus register notes `F-TM-000`/`000a`…`000f` |
| [`qa_backups/verify_market_numbers.py`](../qa_backups/verify_market_numbers.py) | New deterministic checker: **76** document/arithmetic checks and **12** negative self-tests |
| [requirements](03_requirements_traceability.md) | **REQ-427…REQ-512** added (86 rows), re-evaluating REQ-009, REQ-010, REQ-087, REQ-170 and REQ-174 rather than duplicating them |
| [decision register](04_approved_and_provisional_decisions.md) | **DD-123…DD-135** added, one per `D-109…D-121` |
| [unresolved register](05_unresolved_design_decisions.md) | **UD-037** (band and limit calibration) and **UD-038** (post-gate liquidity evidence) opened |

### 21.2 Decisions recorded

| ID | Rule, in one line |
|---|---|
| **D-109** | Two systems: directed trades are first-playable and fee-free; Global Trade is a **required long-term** public board, **release-gated** by G-1…G-6 |
| **D-110** | A **public listing reserves at posting** (units for a sell, `quantity × unit_price` crowns for a buy); **D-016 is unchanged** for directed offers, which reserve nothing at creation |
| **D-111** | Execution is **taker-selected posted price** with **partial fills** and **no matcher**; a crossed book is displayed and warned, never auto-crossed |
| **D-112** | A counteroffer creates a **new revision**; only the live revision can settle; 10 revisions, 72-turn expiry, three consecutive expiries close the chain |
| **D-113** | Declared limits: 5 active outgoing chains, 1 live chain per pair, 10 revisions, 5 resource lines per side, 100,000 units per line, 10,000,000 crowns per side, 20 directed actions per 12 turns, 3 open listings per resource per nation |
| **D-114** | Fair value is a **3,000 bp band on the two sides' reference values**, inclusive; a **fresh nation** is blocked out-of-band and from one-sided sends for its first **360 turns**; a mature out-of-band trade is permitted and **signalled** |
| **D-115** | Directed terms are parties-plus-restricted-audit; an **open** listing is public by design; completed public executions publish resource, quantity, unit price and turn, **not** the parties' wider account data |
| **D-116** | Both legs settle at **P4** in one transaction, one `transfer_id`, `TRADE_SELL`/`TRADE_BUY` pairs, no fee, no debt, no negative balance |
| **D-117** | **No statistic is public at first playable**; after the gate a 12-turn VWAP and volume band need **five trades and five nations** and obey `k = 5` |
| **D-118** | Ten review signals, none of which is proof; price alone never triggers a sanction; no automatic ban or confiscation |
| **D-119** | Stable code families `MKT-A/D/E/G/L`; one accepted execution per idempotency key |
| **D-120** | Bounded work: directed expiry in B0, daily off-path statistic job, no matcher or poller, one-page board reads, and a **5,000-executions-per-turn world guard** |
| **D-121** | 07B is complete **at the documentation level**; 07C is the next task; no implementation claim |

### 21.3 How the 07A evidence was used

The evidence-to-decision matrix in **B-07 §3** links every major rule to a 07A finding, an existing project constraint or a declared rationale. The load-bearing cases:

- **`PWR-002`/`PWR-006`** (posted offer with manual acceptance; no documented matcher) → **D-111**: keep manual taker selection at first playable, and say plainly that no matcher exists.
- **`PWR-005`/`PWR-022`** (a clicked offer can fail because the other side has nothing) → the one documented frustration the design refuses to copy: **directed offers re-validate at acceptance** and **public listings reserve at posting** (**D-110**).
- **`PWR-016`…`PWR-019`** (identity, network and ±30% band rules) → the fresh block and the **3,000 bp** band (**D-114**), with the shared-network non-proof rule preserved from D-034.
- **`PWR-012`/`PWR-013`** (public averages and trade history) → statistics are **withheld until the gate** (**D-117**) and public execution records are narrow (**D-115**).
- **`PWR-024`** (offer caps as a readability response) → declared limits (**D-113**) rather than an unstated throttle.
- The report's **`PWR-004`** (no observed expiry) and **`PWR-023`** (crossed offers) were treated as *observations to decide differently from*, not as rules to copy: 72-turn expiry and an explicit crossed-book warning.

No 07A finding was presented as proof of liquidity, prevalence or balance, and none was used to reopen an accepted Prompt 01–06B rule.

### 21.4 Validation actually run (2026-10-28)

| Command | Result | Exit |
|---|---|---|
| `python3 qa_backups/verify_market_numbers.py` | **76/76 checks passed** | 0 |
| `python3 qa_backups/verify_market_numbers.py --self-test` | **12/12 guards detected their defect** | 0 |
| `python3 qa_backups/verify_economy_numbers.py` | **164/164 passed** | 0 |
| `python3 qa_backups/verify_city_numbers.py` | **267/267 passed** | 0 |
| `python3 qa_backups/verify_politics_numbers.py` | **879/879 passed** | 0 |
| `python3 qa_backups/validate_final.py` | **ALL CHECKS PASSED** | 0 |
| `python3 qa_backups/validate_final.py --self-test` | **3/3 guards detected their defect** | 0 |
| `python3 qa_backups/test_decision_registers.py` | **12 tests OK** | 0 |
| `python3 qa_backups/test_next_action.py` | **15 tests OK** | 0 |
| `python3 qa_backups/09_validate.py` | **345/345 checks passed** | 0 |

**What the new checker actually proves.** It recomputes all 21 examples from the register's constants, checks the 35 failure rows for a stated final state, verifies that every `MKT-` and `F-TM-` identifier cited by the rulebook exists, checks the eleven-resource roster and the reference prices against B-04, checks the fresh-window boundary (turn 359 fresh, 360 not), the band's inclusive edge, the reservation identities, the crown-conservation identity and the absence of a launch fee. Its 12 self-tests each corrupt one input and require the guard to reject it, so a silently disabled check fails the run.

**Two defects found and fixed during this pass.** (1) A **duplicate `MKT-` number** was reported by the first `sort | uniq -d` scan; inspection showed `MKT-215`, `215a` and `215b` are three distinct numbered sub-rules, so no renumbering was needed and none was done. (2) The register's closing notes carried **formula-style IDs `F-TM-040`/`F-TM-041`**, which made the advertised formula range `001…039` untrue; they are now `F-TM-000e`/`000f`, in the register's existing note namespace, with no formula renumbered.

**Validator repairs in the same pass.** Three inherited checkers still encoded the pre-07B register totals and therefore failed on the new rows rather than on a defect: `validate_final.py` compared the requirement range against 426 while its own message said 512, required `UD-001..UD-036` and `22/8/6`, and accepted only prompts `02–15`/`06B` in the requirement prompt column; `09_validate.py` carried the same ranges plus `14 approved / 405 provisional` and the older `AI_CONTEXT` counts; `test_decision_registers.py` still expected 36 UD rows. Each was corrected to the recounted truth — **REQ-001…REQ-512**, **UD-001…UD-038**, **22 Resolved / 8 Deferred / 8 Open**, **18 approved / 487 provisional / 5 open / 2 deferred**, prompt tokens `07B`/`07C` — and the `AI_HANDOFF` decision count was extended to **121**. A fourth guard in `validate_final.py` required the stage roadmap row to end with the literal "Prompt 07 next"; it now requires **07B market foundations complete** *and* **Prompt 07C next**, so it checks more than before. No assertion was removed, skipped or weakened; every changed check still fails on a wrong count or a wrong stage, and all self-test suites were rerun afterwards.

**Before this section was written**, one documentation inconsistency was found in the continuity set itself: the Stage 2 roadmap already cited `§20–§21` while §21 did not yet exist. The section was added rather than the citation being weakened, and `validate_final.py` now sees the citation resolve.

### 21.5 Limits — what this pass does not claim

- **No implementation.** No market table, endpoint, screen, migration, scheduler or deployment exists. The design is a contract for a later stage.
- **No runtime test.** The checker reads documents; it does not exercise a server, a transaction or a concurrent race. Every atomicity and idempotency rule is a specification, not a demonstrated property.
- **No balance.** The 3,000 bp band, the caps, the 72-turn expiry, the five-trade/five-nation sample, the 12-turn VWAP and the 5,000-execution world guard are **provisional working values** (UD-037/UD-038, D-014). Correct example arithmetic is not evidence that a value is well tuned.
- **No liquidity or anti-fraud proof.** Nothing here measures whether players will post, whether a book will clear, or whether the signals detect real abuse.
- **The gate is not passed.** G-1, G-2, G-3, G-5 and G-6 are **NOT MET** and G-4 is **PARTIAL**. Global Trade remains unavailable for release; it has not been removed from the product.

### 21.6 What Prompt 07C inherits

B-07 supplies the rule set, the code families, the 35 failure cases and the 21 worked examples; **07C owns the workflow and acceptance layer**: the end-to-end action sequences, screen-by-screen states, the acceptance-test matrix that turns each `MKT-` rule into a checkable case, the evidence plan for G-1…G-6, and the decision on whether any gate can be evidenced before implementation. 07C must not re-decide the market model. If it finds a contradiction, it follows the established amendment route: exact decision ID, scope, rationale, dependencies and approval status.

---

## 22. Prompt 07B status reconciliation and sub-prompt guard (2026-10-29)

**Why this pass exists.** The independent review of Prompt 07B's acceptance found the market design and its arithmetic checks sound, but the **continuity documentation contradicted itself**: the handoff, the progress summary and the roadmap all said 07B was complete and 07C next, while one paragraph in the progress summary and two clauses of the handoff still described 07B as the next, unstarted task. A reader could not tell which statement was current. No market rule, formula, requirement or decision was in question.

### 22.1 The contradictions, and how each was classified

| Location | Statement found | Class | Action |
|---|---|---|---|
| `PROJECT_PROGRESS.md` Stage 2 summary | "Prompt 07B — market foundations is the next intended task and has not started" (with 07C also listed as not started) | **Current status** | Corrected: 07B completed 2026-10-28; **07C is the next intended task**; 08 and implementation not started |
| `PROJECT_PROGRESS.md` continuity paragraph | "The current next action is Prompt 07 — Trade and Markets" | **Current status** (imprecise) | Narrowed to **Prompt 07C — market workflows and acceptance**, with the 07A/07B completion dates added |
| `AI_HANDOFF.md` §H opening | "Stage 2 — Create the Master Game Design Bible — is authorized and is the next activity" | **Current status** (stale: Stage 2 has been in progress since 2026-10-23) | Corrected: Stage 2 in progress; **07C is the next task** within it |
| `AI_HANDOFF.md` §I item 14 | "its next outstanding prompt is Prompt 07 — Trade and Markets" | **Current status** | Corrected to **07C**, with 07A/07B recorded complete |
| `AI_HANDOFF.md` header status recap (line 3) | "07A … is complete; **07B — market foundations is the next intended task**" and "next **Stage 2, Prompt 07 — Trade and Markets**" | **Current status** embedded in a long summary | Both clauses corrected to name 07B complete and 07C next; the surrounding history was left intact |
| `stage-2/research/07A_…_research.md` header and §14 table | "Next intended task: Prompt 07B … Prompt 07B and 07C have not started" | **Historical record** (dated report, correct at publication) | Preserved verbatim, relabelled **"at publication (2026-10-28)"** and annotated with the superseding completion; no finding, source or recommendation changed |
| `stage-2/06_stage_2_progress_log.md` §20 (dated 07A record) | "Prompt 07B has not started; Prompt 07C and Prompt 08 have not started" | **Historical record** (true when written) | **Not edited.** The new guard reads only the log's current-status header, never its dated sections |

### 22.2 Why every existing check passed while the statements were wrong

`status_rules.stale_next_actions()` compares **prompt numbers**: it reads `stage_2_next_prompt: 07` and rejects a next-action sentence naming a number below it. **07B and 07C are both "Prompt 07"**, so a sentence saying 07B was the next task carried the current number and passed every validator — `09_validate.py`, `validate_final.py` and `test_next_action.py` included. The defect was structural, not a missed phrase: the check had no concept of a **sub-prompt**.

### 22.3 The guard added

`qa_backups/status_rules.py` gains **`subprompt_status_problems(text)`**, with `CURRENT_SUBPROMPT = "07C"` and `COMPLETED_SUBPROMPTS = ("07A", "07B")`:

- it splits text into **clauses** (line, then `;`/`.`) so one sub-prompt's claim cannot leak into another's;
- it attributes a claim to a sub-prompt **only up to the next sub-prompt mention**, so "07B is complete; 07C is next" is never read as a 07B claim;
- it flags a completed sub-prompt described as **"the next … task/action/prompt"**, as **not started**, or as **pending** — whether the claim follows the identifier or precedes it ("**Next action:** 07B …");
- it **skips clauses with a historical marker** ("was the next", "at the time", "superseded", …), so dated records stay legal;
- it is wired into `validate_final.py` as check **§7b-3**, over AI_CONTEXT, AI_HANDOFF, PROJECT_PROGRESS, ROADMAP, the Stage 2 handoff, the Stage 2 roadmap, the Bible outline and the progress log's **header only** — not its dated sections.

**Regression fixtures.** `test_next_action.py` adds five tests: a contradictory current-status fixture is rejected (and names 07B); a "has not started" claim about 07A is rejected; "07B complete; 07C next" is accepted; a labelled history is accepted; the real continuity set contains 07C and no sub-prompt claim. `validate_final.py --self-test` gains a fourth fixture that must detect the defect.

**Negative experiment, file level.** The stale sentence was reintroduced into `PROJECT_PROGRESS.md` verbatim. `validate_final.py` **failed at exit 1**, naming the file and the clause: `PROJECT_PROGRESS: completed sub-prompt still described as live :: … "07B — market foundations is the next intended task" and has not started`. The file was then restored from a byte copy and its **SHA-256 verified unchanged** (`ac4f936b…54fa65`); the validator passed again and the temporary `.bak` was removed.

### 22.4 Validation actually run (2026-10-29, after the last edit)

| Command | Actual result | Exit |
|---|---|---|
| `python3 qa_backups/validate_final.py` | **ALL CHECKS PASSED** | 0 |
| `python3 qa_backups/validate_final.py --self-test` | **4/4** guards detected their defect | 0 |
| `python3 qa_backups/test_next_action.py` | **20** tests OK | 0 |
| `python3 qa_backups/test_decision_registers.py` | **12** tests OK | 0 |
| `python3 qa_backups/09_validate.py` | **345/345** checks passed | 0 |
| `python3 qa_backups/verify_market_numbers.py` | **ALL CHECKS PASSED** | 0 |
| `python3 qa_backups/verify_market_numbers.py --self-test` | **12/12** guards detected their defect | 0 |
| `python3 qa_backups/verify_economy_numbers.py` | **164/164** passed | 0 |
| `python3 qa_backups/verify_city_numbers.py` | **267/267** passed | 0 |
| `python3 qa_backups/verify_politics_numbers.py` | **879/879** passed | 0 |

### 22.5 Scope and limits

- **No design change.** B-07 and its formula register were not edited: no `MKT-` rule, formula, worked example, requirement, decision or gate status changed. G-1/G-2/G-3/G-5/G-6 remain **NOT MET** and G-4 **PARTIAL**.
- **No new register IDs.** This pass records no decision, requirement or formula: it corrects status statements and strengthens a checker.
- **No implementation, migration or deployment**, and no runtime test — the checks read documents.
- **History preserved.** Dated log sections, the 07A report's findings and the earlier validation runs are kept as they were; only present-tense status statements were reconciled.
- **Prompt 07C has not started.** It remains the next intended task.

---

## 23. Prompt 07C — market workflows, acceptance and the Global Trade product commitment (2026-10-29)

**Scope.** Prompt 07C was a specification and acceptance task: workflows, edge cases, cross-system integration, the acceptance matrix, the G-1…G-6 evidence plan and the final Prompt 07 acceptance. No game code, migration, endpoint, screen, deployment or hosting change was made.

**Deliverable.** [`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md) v1.0 (1,024 lines): the directed workflows W-D01…W-D20, the Global Trade workflows W-G01…W-G30, the cross-system interface table, fourteen edge-case walkthroughs, the 83-test catalogue, the **237/237**-rule matrix with 0 unmapped rules, the six-gate evidence plan, the player-experience risks and the operational bounds.

**Product decision.** **D-122** (with **DD-136** and **REQ-513**) records Global Trade as an **approved, mandatory, long-term product feature**. Feature approval is separate from release: G-1, G-2, G-3, G-5 and G-6 remain **NOT MET**, G-4 remains **PARTIAL**, and no implementation or readiness claim is made. A reversal requires a new explicit owner-authorized decision.

**Three confirmed B-07 defects, corrected in v1.1.**

1. **E1 ledger.** The example put `+200` and `−200` on both sides' two events. Each treasury therefore netted to zero while the closing balances moved by ±200 — the same payment counted twice. The 200 crowns now appear once: a debit on Aurelia's `TRADE_BUY` and a credit on Borealis's `TRADE_SELL`; the food leg carries 0. MKT-165 states the attribution rule.
2. **Warehouse reservations.** MKT-039, MKT-095 and MKT-129 said "free space plus existing space reservations", and MKT-058 treated an earlier trade filling the warehouse as an ordinary `F4`. But `free_space = W − total_inventory − space_reserved` already subtracts the reservations; adding them back ignores them and overbooks. All four now use the single predicate; MKT-135 states that `space_reserved` is never added back, and a P4 space failure is treated as an invariant defect, not ordinary competition.
3. **Fair-value wording.** MKT-145 called the 3,000 bp rule a "symmetric ratio" and implied a ±30% band. It is asymmetric: the larger side may be at most 30% bigger. `100 vs 130` passes; `70 vs 100` fails, because `floor(70 × 1.30) = 91`. E20 now records the reversed and discount boundaries; E5's message states the rule in plain words.

**Registers.** D-122; DD-136; REQ-513. No existing ID was renumbered or overwritten; no new `MKT-`, `F-TM-` or `UD-` row was created. UD-037 and UD-038 remain open with their owners and exit conditions.

**Tests added.** `verify_market_workflows.py` (237-rule matrix, catalogue IDs, E1/space/band guards, gate statuses, product approval and continuity) with **8/8** self-tests; `verify_market_numbers.py` extended with the E1 ledger, the space predicate and the band-asymmetry cases (**95/95**, **14/14** self-tests); `validate_final.py` and `test_next_action.py` advanced to Prompt 08 and the new counts.

**Validation (documentation only).** `verify_market_workflows.py` 237/237 and 8/8; `verify_market_numbers.py` 95/95 and 14/14; `validate_final.py` ALL CHECKS PASSED and 4/4; `test_next_action.py` 20 tests; `test_decision_registers.py` 12 tests; `09_validate.py` 345/345; `verify_economy_numbers.py` 164/164; `verify_city_numbers.py` 267/267; `verify_politics_numbers.py` 879/879.

**Limits.** No market server, database, scheduler, queue, browser or player exists. The acceptance catalogue is a test design, not executed evidence. No gate was passed. No balance, liquidity, capacity, security or production-readiness claim is made.
## 24. Prompt 08A — diplomacy research, evidence, requirements and cross-system integration (2026-10-29)

**Scope.** Prompt 08A was the first subphase of Stage 2 Prompt 08: research, requirements traceability, cross-system integration, UD-033 analysis and handoffs. It authorised **no implementation and no design rule**. No game code, schema, migration, API, screen, scheduler, service, deployment or hosting change was made, and no runtime, load or security test was run because there is nothing to run.

**Deliverable.** [`research/08A_diplomacy_research.md`](research/08A_diplomacy_research.md) v1.0 (19 sections): purpose and exclusions; the project-document inventory and the pre-08A diplomacy baseline; methodology and evidence labels; comparator selection; the **source register**; findings by research topic; the comparative matrix; design implications; approved requirements and constraints; **unapproved** candidate recommendations; the UD-033 analysis; the **Prompts 01–07C integration matrix** (36 rows); the **Prompt 09 interface and ownership matrix** (`A-01`…`A-12`); the conflict inventory (`DPX-01`…`DPX-06`); risks and evidence gaps; the requirements/open-question traceability (`DQ-01`…`DQ-16`); the **Prompt 08B handoff**; the **Prompt 09 handoff**; and the completion checklist with the actual validation record.

**Evidence.** **19 sources** (`DPS-001`…`DPS-019`): Politics & War (6), eRepublik (3), Call of War (3), Stellaris (2), EVE Online (3) and one P&W glossary; 8 publisher-official, 4 publisher-hosted but community-edited, 7 community. **54 findings** (`DPR-001`…`DPR-054`). Source conflicts are recorded rather than smoothed: P&W's treaty record in-game versus forum (`DPS-001`/`DPS-005`), the community-only P&W embargo approval effect (`DPS-003`/`DPS-007`), the uncorroborated Call of War popularity claim (`DPS-013`), and EVE's war cost with the official page current (`DPS-016`/`DPS-018`). **EU4, CK3 and Victoria 3 were excluded** because their wikis returned a client challenge; no claim is made from a snippet, and the resulting narrowness in truce-breaking/aggressive-expansion evidence is disclosed.

**What it establishes (evidence, not rules).**

1. **Three layers, not one.** A directional posture, a mutual agreement and an enforceable obligation are distinct in every comparator that goes beyond war/peace (`DPR-013`, `DPR-014`); only the last changes behaviour. B-02 TR-019 already separates posture from Agreement, and the research supports keeping that split.
2. **Enforcement is selective.** P&W records ten treaty types and enforces only non-aggression (`DPR-001`); Stellaris applies effects and charges an exit cost (`DPR-019`); eRepublik triggers a mutual-defence pact and blocks embargoed trade (`DPR-004`, `DPR-041`). The design question is *which* promises the game enforces.
3. **Authority is explicit where the mechanic works.** eRepublik splits proposal from legislative approval (`DPR-026`); EVE names the CEO/director (`DPR-027`); P&W leaves it undocumented (`DPR-028`) — a warning, not a model.
4. **Reputation is not one object.** Trust versus opinion, player-set labels, or no register at all (`DPR-033`…`DPR-040`). A single global score is unsupported.
5. **Sanctions are usually a time-boxed act or a relation, not a treaty** (`DPR-041`…`DPR-044`); their market effect must be read from the diplomacy rule and never implemented as a hidden fee.
6. **Public outcomes, private negotiation** (`DPR-045`…`DPR-049`).
7. **Documented abuse clusters on timing and slots** — war-slot filling, bank evasion, beige cycles (`DPR-051`…`DPR-053`) — plus duplicate reciprocal records (`DPR-054`) and stale authorization (`DPR-031`).
8. **No comparator documents proposal expiry or a formal counterproposal** (`DPR-023`, `DPR-024`). Either would be an innovation and must be justified.

**Integration audit.** All ten applicable deliverables (Prompts 01, 02, 03, 04, 05, 06A, 06B, 07A, 07B, 07C) are represented in 36 rows; **19 rows name a material dependency** and **six conflicts** are carried with owners (`DPX-01`…`DPX-06`): the public moment of a signed treaty (08B), posture versus mutual agreement (08B), reroll versus account reputation (08B/Prompt 12), the diplomacy–market embargo interface (08B/08C), read-only diplomacy during `TRANSITION`/`CRISIS` (08B/08C) and alliance-treaty ownership (08B/09). **No prior rule was edited**: B-02…B-07, their formula registers, the 07C companion, D-122/DD-136/REQ-513 and G-1…G-6 are unchanged.

**UD-013 and UD-033.** Both were examined against their registered wording and both **remain open**. UD-013 (what a treaty does beyond a non-aggression analogue) now has evidence on selective enforcement but no decision. UD-033 ("Is in-game diplomatic/treaty reputation account-scoped or nation-scoped after a reroll?") is **not answerable by analogy** — no comparator has Nation Supremacy's reroll model — so the report records its options, dependencies and downstream effects and leaves the choice to 08B as a product decision. No `UD-` row was added, and neither row was marked resolved.

**Prompt 09 boundary.** Prompt 09's ownership of the Alliance System was preserved in full: founding, constitution, governance, leadership, ranks, internal permissions, membership, shared resources, alliance diplomacy, collective decisions and operations are **not designed** in the 08A report. It records only the interface (`A-01`…`A-12`), the state and permission questions 09 must answer, the ownership ambiguities (`DPX-06`) and a handoff (§18). `A-02` explicitly assigns an alliance-to-alliance treaty to Prompt 09, with 08B publishing the reusable object contract.

**Filename finding.** The outline and this register still named `14_diplomacy.md`, but `14_` is the accepted 07C companion. The report confirms the collision, recommends `15_diplomacy.md`, and **does not create it**; 08B confirms the next free prefix at its start and updates the register and the outline together. A filename note now records this.

**Registers.** No `D-`, `DD-`, `UD-` or `REQ-` row was added: 08A makes no decision and writes no rule. `03_requirements_traceability.md` records the pass at v1.16 with unchanged counts (**19 Approved / 487 Provisional / 5 Open / 2 Deferred**); `05_unresolved_design_decisions.md` moves to v1.13 with UD-013/UD-033 annotated and unchanged counts (**22 Resolved / 8 deferred / 8 Open**). The report's `DPS-`, `DPR-`, `DPX-`, `DCR-` and `DQ-` identifiers are scoped to the report and are **not** project decisions or requirements.

**Validator advances (no check removed or weakened).**

1. `status_rules.py` — `08A` joins the completed sub-prompt set and the pattern accepts `0[78][A-C]`, so "08A is the next task" is caught like 07B/07C were; a new fixture proves it.
2. `validate_final.py` — pending count **8 → 7** (Prompts 09–15), a row-08 assertion, `stage-2/00 §10` now requires **Prompt 08B**, continuity requires **08A and 08B**, the roadmap check requires "Prompt 08A complete" plus `08B`, and the report is a required document; self-test **6/6**.
3. `test_next_action.py` — the progress-table check requires one row naming the next **sub-prompt** (`08B`); a new test covers 08A; the real-continuity test asserts 08A/08B (**23 tests**).
4. `test_decision_registers.py` — row 08 must read `08A complete` and `08B next`, and "Prompt 08 is complete" is still forbidden (**12 tests**).
5. `09_validate.py` — pending count 7 and a row-08 assertion (**346/346**).
6. `verify_politics_numbers.py` — the progress-status guard reads the 08A/08B row (**879/879**, self-test **18/18**).

**Validation actually run (documentation only).** `validate_final.py` — ALL CHECKS PASSED; `--self-test` 6/6; `test_next_action.py` 23 tests OK; `test_decision_registers.py` 12 tests OK; `09_validate.py` 346/346; `verify_market_workflows.py` 14/0 document checks, 237 unique `MKT-` rules, 237-row matrix, 83-test catalogue, ALL CHECKS PASSED, self-test 8/8; `verify_market_numbers.py` ALL CHECKS PASSED, self-test 14/14; `verify_economy_numbers.py` 164/164; `verify_city_numbers.py` 267/267; `verify_politics_numbers.py` 879/879; relative-link resolution over the new report — 49 links checked, 0 missing.

**Limits.** No player research, no live play in any comparator, three intended comparators inaccessible, P&W's creation flow unverified, and no implementation exists. Every experience statement in the report is labelled analysis, not user evidence. PASS is claimed **at the research and documentation level only**.

**Next authorised action.** **Prompt 08B — diplomacy foundations** ([Stage 2 register](01_stage_2_prompt_roadmap.md) §3 Prompt 08). Prompt 08C has not started, and Prompt 09 is not authorised.
## 25. Prompt 08B — diplomacy foundations, player authority, treaties and system design (2026-10-30)

**Scope.** Prompt 08B was the second subphase of Stage 2 Prompt 08. It converted the accepted 08A evidence into the authoritative **B-08** diplomacy foundations: the relationship model, the treaty catalogue, the proposal and agreement lifecycles, consent and amendment, permissions, reputation, one sanction, timing, visibility, history, failure and integrity, the cross-system contracts, the Prompt 09 interface, twelve worked examples and the 08C handoff. It approved **no implementation** and did not start 08C or Prompt 09.

**Deliverables.** [`15_diplomacy.md`](15_diplomacy.md) v1.0, corrected to **v1.1** by 08B-C (§26) and to **v1.2** by 08B-D (§27) — 22 sections, **157 `DIP-` rules**, **15 `DPF` failure codes**, twelve worked examples (E1–E12), a 26-row cross-system matrix and the Prompt 09 contract — and [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md) v1.0, with **`F-DP-001`…`F-DP-012`**, units, bounds, rounding, timing, edge cases, examples and validation expectations. Every value is **Provisional** and belongs to Prompt 14.

**The design in one paragraph.** Diplomacy is **three layers**: a directional posture (`FRIENDLY`/`NEUTRAL`/`TENSE`/`HOSTILE`) owned by each nation, a mutual agreement with immutable terms and versions, and a separate effect owned by the system that enforces it. The catalogue is deliberately small: `DP-T01` non-aggression (a war-declaration block, **inert until Prompt 10**), `DP-T02` consultation (a notice gate before `HOSTILE` posture or an embargo), `DP-T03` aid (**crowns only**, reserved at acceptance, delivered at P4 with matched ledger events), and `DP-A01` embargo (24 turns, requires `HOSTILE`, blocks **new** directed trades and aid, grandfathers accepted transfers, charges no fee). There is **no** mutual-defence pact, trade treaty, protectorate, peace treaty or alliance-level treaty.

**Player sovereignty.** The sole diplomatic authority is the **authenticated owner of the active nation** (D-032). No delegation to another player, an AI, an alliance leader or an office exists. The system may validate, record, activate an agreement both parties accepted, expire an agreed deadline and run the closed cleanup list (reroll, dormancy, political freeze); it **never** accepts, rejects, proposes, declares, sanctions, surrenders, breaks, renews or changes posture for a player. Every consequential action requires a confirmation showing the counterparty, terms, activation, expiry, cost, visibility and breach consequence. `TRANSITION`/`CRISIS` makes diplomacy read-only and **freezes** deadlines instead of expiring them (DMP-263). The eight-question authority test is applied to all fourteen actions.

**Resolved questions.** **UD-013** is resolved by **D-124**: a treaty does exactly three things — blocks a war declaration (NAP), requires a notice before hostility (consultation), or moves crowns (aid) — and nothing else. **UD-033** is resolved by **D-128** as option **(a)**: there is **no reputation score** and no account-level diplomatic record; the only derived value is a nation-scoped public **breach count** over 4,380 turns with no mechanical effect, and a replacement starts at zero. The laundering limitation is disclosed, not hidden. **DPX-01** (publication moment) is resolved at **activation**; **DPX-02** (symmetry) by directional posture; **DPX-03** (reroll reputation) by the nation scope; **DPX-04** (embargo ownership) by B-08 owning the act and B-07 reading it; **DPX-05** (read-only) by the freeze. **DPX-06** is split: nation-level treaties are B-08's; alliance-level reuse and delegation are **UD-039**, deferred to Prompt 09.

**Breach and sanctions.** A party may **break** an active agreement unilaterally. The effect ends, a public class-P event names the breaker, the derived count rises and a 36-turn same-pair same-type cooldown applies; nothing is confiscated, frozen, fined or auto-retaliated. Mutual termination is free and creates no breach. Breach cannot be caused by a failed or voided turn, dormancy, transition/crisis, reroll or delayed settlement. The one sanction is the embargo; asset freezes, construction/research/policy bans and collective alliance sanctions are **not adopted**.

**Limits and timing.** Declared limits: 3 outgoing proposals, 1 per pair+type, 8 active agreements, 36-turn proposal expiry, 12-turn posture cooldown, 12–36-turn notice window, 12-turn notice cooldown, 36-turn breach cooldown, 24-turn embargo, 12-turn re-imposition cooldown, 360-turn term, 4,380-turn breach window. Effects resolve at B-02 boundaries: P2 re-validation, P4 application, P6 publication, P7 invariants; one priority band orders expiry/termination before activation before breach before embargo; every action is idempotent.

**Cross-system integration.** The matrix covers B-02 (TR-019/020/021/022/096 and the §24 contract), B-03 (pair block, reroll, dormancy), B-04 (ECN-212 reservation/transfer/ledger, no debt), B-05 (URB-155, untouched by the adopted catalogue), B-06 (DMP-138 and DMP-263 freeze/persistence), B-07 (MKT-185/217/218/220; the embargo is a permission block, never a fee) and 07C §6/§15 (the new B-08 restriction is recorded, no `MKT-` rule is edited). **Global Trade, D-122, DD-136, REQ-513 and G-1…G-6 are unchanged.** The only forward dependency is the NAP's enforcement by Prompt 10; it is declared and inert, not claimed as working.

**Prompt 09 boundary.** B-08 owns **nation-level** diplomacy and publishes the treaty object, authority, membership-change rule, pair contract, embargo contract, visibility, notifications and acceptance scenarios. Prompt 09 owns founding, constitution, governance, leadership, ranks, membership, shared resources, alliance diplomacy and operations, and must decide **UD-039** (reuse of the B-08 object and any delegation) with a new `D-` entry. No alliance rule is written here. The planned Prompt 09 document moves to **`16_alliances.md`**; `15_` is B-08.

**Canonical files.** `15_diplomacy.md` is B-08; `15_diplomacy_formula_register.md` is its formula register. The outline's `14_diplomacy.md` is not created; `14_` is the accepted 07C companion. Later planned prefixes shift by one in the register (Prompt 09 → `16_`, and later names follow); no existing file was renamed.

**Registers.** **D-123…D-132**; **DD-137…DD-146**; **REQ-514…REQ-533** (count **533: 19 Approved / 507 Provisional / 5 Open / 2 Deferred**); **UD-013** and **UD-033** resolved; **UD-039** opened; the UD register is **24 Resolved / 7 Deferred / 8 Open = 39**. No earlier ID was renumbered, no approved decision was reversed, and no `MKT-`, `F-TM-`, `ECN-`, `URB-` or `DMP-` rule was edited.

**Limits.** No player research, no runtime, load, concurrency or security evidence. The NAP effect cannot be exercised until Prompt 10. The reroll escape is real and disclosed. The break-before-delivery ordering is a judgement 08C must test. The examples are illustrations, not balance proofs.

**Validation actually run (documentation only).** From `docs/qa_backups/` on 2026-10-30: `validate_final.py` **ALL CHECKS PASSED** and `--self-test` **7/7**; `test_next_action.py` **23 tests OK**; `test_decision_registers.py` **12 tests OK**; `09_validate.py` **347/347**; `verify_politics_numbers.py` **879/879** and `--self-test` **18/18**; `verify_market_workflows.py` **14 checks, 0 failed** with 237 rules, 237 matrix rows and 83 tests, `--self-test` **8/8**; `verify_market_numbers.py` **95 passed, 0 failed**; `verify_economy_numbers.py` **164/164**; `verify_city_numbers.py` **267/267**. The validators were advanced, not weakened: the register totals, the UD inventory, the row-08 status and the handoff count now expect the values 08B wrote, `08B` joined the completed sub-prompt set with its own self-test fixture, and `15_diplomacy.md` joined the outline's gameplay-rule derivation. No `MKT-`, `F-TM-`, `ECN-`, `URB-`, `DMP-` or `TR-` assertion changed. The B-08 document-level checks — ID ranges and gaps, the 15 `DPF` codes, the twelve `F-DP-` formulas, §1–§22 continuity, E1–E12, and the 26-row matrix — are recorded in B-08 §22.2 with their results. **No runtime, load, concurrency, security or usability test exists.**

**Next authorised action.** **Prompt 08C — diplomacy workflows and acceptance** ([Stage 2 register](01_stage_2_prompt_roadmap.md) Prompt 08). It must use B-08 §20/§21, may not add a mechanic, and must not claim a runtime test. Prompt 09 remains not authorised.
## 26. Prompt 08B-C — diplomacy specification correction and consistency audit (2026-10-30)

**Scope.** Prompt 08B-C corrected the completed B-08 deliverable after an audit found seven confirmed defects. It is a correction pass, not a rewrite: no treaty type, sanction, permission, value, player-authority rule or Prompt 09 boundary changed, and nothing was implemented.

**The seven mandatory corrections.**

| # | Defect as found | Correction | Evidence |
|---|---|---|---|
| 1 | The Stage 2 register's Prompt 09 row still named `15_alliances.md`, which would collide with B-08 | Row 09 now names **`16_alliances.md`**; the outline and D-132 already used it. The remaining prose that says "not `15_alliances.md`" is the explanation, not a deliverable | `verify_diplomacy_numbers.py` checks row 09 and rejects a `15_alliances.md` deliverable cell |
| 2 | DIP-103 ordered expiry/termination → activation → breach → embargo while DIP-130/DIP-131 described break before delivery and DIP-101's P4 list put activation first | One band, **five steps**: `EXPIRY_AND_TERMINATION` → `BREACH` → `ACTIVATION` → `SCHEDULED_OBLIGATION` → `EMBARGO`. DIP-101, DIP-103, DIP-104, DIP-130 and DIP-131 now agree; each step re-reads the previous step's committed state | Checker asserts the five-step order and the absence of "activation before breach" |
| 3 | DIP-044 keyed proposals by ordered pair while F-DP-002 used an unordered pair and called reciprocals different ordered pairs | DIP-124 now states three keys: proposals **ordered** `(from, to, type, PENDING)`, agreements **unordered** `({a,b}, type, ACCEPTED|ACTIVE)`, embargoes ordered. F-DP-002, DIP-134 and DIP-052 follow; **E1 gains a reciprocal variant** (A→B and B→A both pending, the first acceptance wins, the loser fails `DPF-04`) | Checker asserts the ordered key in both files **and the E1 variant** |
| 4 | F-DP-006 ignored freeze and had no notice-cooldown formula; F-DP-008 ignored freeze | DIP-105 now names **two freeze scopes** — pair-scoped (`frozen_pair`, each boundary once) and actor-scoped (`frozen_turns(actor)`) — and four explicit non-extensions. F-DP-006 is split into **6a validity** (end + pair freeze) and **6b cooldown** (+ actor freeze); F-DP-008 extends re-imposition by the imposer's freeze and states the term is not extended; F-DP-004/009 use `frozen_pair` | Checker asserts each formula's freeze function and DIP-105's exception list |
| 5 | F-DP-010's example used current turn 4380 and still called the turn-100 breach "outside" | Example recalculated at **current turn 4480**: bound `4480 − 4380 = 100`; the 100 breach is excluded, 200 included, 5000 excluded (future); counts at 4380, 4580 and 5000 also shown | Checker asserts turn 4480, the bound 100 and the exclusion |
| 6 | §4.2 listed 6 real transitions and three guards; `FRIENDLY→TENSE`, `FRIENDLY→HOSTILE`, `TENSE→NEUTRAL`, `TENSE→FRIENDLY`, `HOSTILE→FRIENDLY`, `NEUTRAL→HOSTILE` were unstated | All **12** ordered transitions are listed as `T1`–`T12` (renamed from `P` to avoid colliding with B-02's P0–P7 phases), plus three guard rows. No transition between postures is prohibited; every transition **to** `HOSTILE` carries the consultation-notice precondition (DIP-031) | Checker asserts all 12 pairs and the notice rows |
| 7 | DIP-061 pointed reroll cleanup at DIP-130 | DIP-061 now cites **DIP-127**; no other stale internal reference found (all 158 `DIP-` IDs resolve) | Checker asserts DIP-061 cites DIP-127 and not DIP-130 |

**Additional findings, corrected in the same pass.**

1. **DIP-124 and DIP-134** repeated the unordered "pair+type" key for proposals; both now distinguish ordered proposals from unordered agreements (part of correction 3).
2. **DIP-104** said "a partial write is a defect" without saying what happens when a later step fails; it now states that each object's outcome is atomic, a step-3 failure does not roll back a step-1 expiry, and a half-applied boundary is never visible.
3. **DIP-130's withdrawal row** implied a boundary race when withdrawal and acceptance are both submission-time changes; the first recorded submission now wins.
4. **`REQ-522`, `REQ-533` and `DD-139`** were worded "per pair"; they now say **per direction** of a pair, and REQ-533 records the five-step band.
5. **`D-131`** was edited in place (it is today's decision, not history) to record the five steps, with a dated correction note in its Notes cell.
6. **`DIP-094` and the limits table** now state which timers freeze affects, including the explicit decision that the 24-turn embargo term is not extended.

**New checker.** `docs/qa_backups/verify_diplomacy_numbers.py` — eight document groups (structure, filenames, same-turn order, proposal/agreement keys, freeze arithmetic, rolling window, posture matrix, cross-reference and authority) with an eight-case in-memory self-test. It exists because the general validators check registers and continuity, not diplomacy semantics.

**Changed files.** `stage-2/15_diplomacy.md` (v1.1: posture matrix, band, keys, freeze, examples, DIP-061), `stage-2/15_diplomacy_formula_register.md` (v1.1: F-DP-002, 004, 006a/6b, 008, 009, 010, limits), `stage-2/01_stage_2_prompt_roadmap.md` (Prompt 09 deliverable, 08 row, 08B result), `stage-2/03_requirements_traceability.md` (v1.18; REQ-522/533), `stage-2/04_approved_and_provisional_decisions.md` (v3.2; DD-139), `stage-2/00_stage_2_handoff.md`, `DECISIONS.md` (D-131 note only), `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`. New: `qa_backups/verify_diplomacy_numbers.py`. Reviewed and left unchanged: `ROADMAP.md` and `stage-2/02_master_game_design_bible_outline.md` (both already correct), the 08A report, B-02…B-07 and 14_market_workflows.

**Validation actually run (documentation only).** `validate_final.py` **ALL CHECKS PASSED** and `--self-test` **7/7**; `test_next_action.py` **23 tests OK**; `test_decision_registers.py` **12 tests OK**; `09_validate.py` **347/347**; `verify_politics_numbers.py` **879/879**; `verify_market_workflows.py` **14 checks, 0 failed** (237 rules, 237 matrix rows, 83 tests) and `--self-test` **8/8**; `verify_market_numbers.py` **95 passed, 0 failed**; `verify_economy_numbers.py` **164/164**; `verify_city_numbers.py` **267/267**; `verify_diplomacy_numbers.py` **8 groups, 0 failed** and `--self-test` **8/8**. No validator was weakened and no market, economy, city or politics assertion changed.

**No new decision was made.** The seven corrections implement approved rules; none is a new design choice. The one interpretive choice — the exact position of `BREACH` before `ACTIVATION` — makes DIP-131's already-approved break-before-delivery rule reachable, and is recorded in D-131's correction note. No owner-only decision is outstanding for B-08.

**Next authorised action.** **Prompt 08C — diplomacy workflows, edge cases, safeguards and acceptance.** It must use B-08 v1.1 §20–§21, may add no mechanic, and must not claim a runtime test. Prompt 09 remains not authorised.

## 27. Prompt 08B-D — diplomacy formula, validator and handoff corrections (2026-10-30)

**Scope.** A final micro-correction pass on the completed B-08 pair, not a redesign. Three freeze-aware cooldowns and their consolidated limits rows disagreed with DIP-105, and the Stage 2 handoff header still called 08B "next" while its own §10 named 08C. No treaty type, sanction, permission, value, player-authority rule, alliance boundary or Global Trade gate changed, and nothing was implemented.

**The formula defects, as found.**

1. **F-DP-005** read `eligible_turn = last_posture_change_turn(pair, direction) + 12 + frozen_turns(actor)`. `frozen_turns` takes three arguments (`nation, start_turn, end_turn`), so the posting named the right nation but never said which interval it counted, and its §3 limits row said a flat "12 turns".
2. **F-DP-007** had the same defect with a 36-turn base and a flat "36 turns" row.
3. **F-DP-008** carried the correct three-argument interval in its formula but described its value as "12-turn cooldown" and its §3 row as "12 turns", so the register contradicted itself.

**Corrections.**

| Formula | Corrected expression | Freeze interval | Nation whose freeze counts | Limits row and value |
|---|---|---|---|---|
| F-DP-005 | `eligible_turn(t) = last_posture_change_turn(pair, direction) + 12 + frozen_turns(actor, last_posture_change_turn, t)` | `(last_posture_change_turn, t]` | the actor (the nation that changed posture) | "12 turns **+ actor freeze**"; value "12 turns + actor freeze" |
| F-DP-007 | `eligible_turn(t) = breach_turn + 36 + frozen_turns(actor, breach_turn, t)` | `(breach_turn, t]` | the breaker | "36 turns **+ actor freeze**"; value "36 turns + actor freeze" |
| F-DP-008 | `reimpose_eligible(t) = end_turn + 12 + frozen_turns(imposer, end_turn, t)` (unchanged) | `(end_turn, t]` | the imposer | "12 turns **+ imposer freeze**"; value "12-turn base + imposer freeze" |

Each entry now states its base duration, its nation, its interval, the exclusive/inclusive boundaries, a numerical example with and without freeze, a counterparty-freeze control, and a validation line naming the boundary cases. The embargo's 24-turn term is marked **never freeze-extended** in the same table, so the exception is as visible as the rule.

**A derived property, not a new rule.** `t ≥ start + N + frozen_turns(n, start, t)` is the same statement as "`N` boundaries in `(start, t]` on which `n` was not frozen have elapsed". The register's §1 now says so and forbids a bare `frozen_turns(actor)`: every actor-scoped cooldown is a count of **unfrozen** boundaries from the event that started it. This derives from DIP-105(b) and changes no value.

**Cross-document consistency.** DIP-027 (posture), DIP-039a (notice window end and notice cooldown), DIP-073 (breach), DIP-093 precondition 4 (re-imposition) and the `DP-T02` effect row now state the same extension the limits table already carried. DIP-006, DIP-034, DIP-044 and DIP-106 say **per direction** rather than per pair for proposals, matching DIP-124 and the fixed non-aggression row count; agreements remain per pair and type, as they must. Two framework errors were also repaired: the Stage 2 register row 07 still said "08A complete, 08B next", and its rows 10–15 used `16_`–`21_`, colliding with B-09's `16_alliances.md`; they now use `17_`–`22_` plus `23_stage_2_completion_report.md`, matching this log and leaving B-09's slot free. No file was renamed, because none of those planned documents exists.

**Handoff correction.** `stage-2/00_stage_2_handoff.md` opened with "Prompt 08 — diplomacy between nations is next" and "08B — diplomacy foundations — is next" while §10 named 08C. The header now records 08B complete (B-08 v1.2, corrected by 08B-C and 08B-D) and 08C next; the §2 state table gained B-06 v2.5, B-07 v1.1 and B-08 v1.2 rows so the project state no longer stops at B-06. The dated 2026-10-29 record is retained inside the revised line rather than rewritten.

**Validator strengthening.** `verify_diplomacy_numbers.py` gained a ninth group: each of F-DP-005/007/008 must state its base duration, its exact three-argument interval, its freeze phrase and the unfrozen-boundary property, must not use a one-argument `frozen_turns()`, and its §3 row must cite the formula and the matching freeze label (actor, imposer or pair), with the embargo term marked non-extended; DIP-027/039a/073/093 must state their extensions. The self-test grew from 8 to 14 defect guards plus a clean fixture (15/15). `validate_final.py` gained `handoff_header_problems`, which fails when the stage-2/00 header calls a completed sub-prompt "next" — the "is next" wording the existing "is the next task" patterns could not see — with a negative and a positive fixture (9/9).

**No new decision.** Every correction restates or applies DIP-105/DIP-106; none changes a value, a permission or a boundary. No new `D-`, `DD-`, `REQ-` or `UD-` row was created.

**Changed files.** `stage-2/15_diplomacy.md` (v1.2: DIP-027, DIP-039a, DIP-044, DIP-073, DIP-093, DIP-106, §22 self-check row), `stage-2/15_diplomacy_formula_register.md` (v1.2: §1, F-DP-002 heading, F-DP-005, F-DP-007, F-DP-008, §3 table and footnote), `qa_backups/verify_diplomacy_numbers.py` (ninth group, six new guards), `qa_backups/validate_final.py` (header guard and two fixtures), `stage-2/00_stage_2_handoff.md` (header, state table, §10 v1.2), `stage-2/01_stage_2_prompt_roadmap.md` (rows 07–15, 08B result), `stage-2/02_master_game_design_bible_outline.md` (B-08 version), `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `stage-2/06_stage_2_progress_log.md` (this entry and the header). Not changed: `DECISIONS.md` (no new decision), the requirements and unresolved registers, the 08A report, B-02…B-07, `14_market_workflows_and_acceptance.md`, `ROADMAP.md` (already correct).

**Validation actually run (documentation only).** `validate_final.py` **ALL CHECKS PASSED** and `--self-test` **9/9**; `test_next_action.py` **23 tests OK**; `test_decision_registers.py` **12 tests OK**; `09_validate.py` **347/347**; `verify_diplomacy_numbers.py` **9 groups, 0 failed** and `--self-test` **15/15** (14 defect guards + 1 clean fixture); `verify_politics_numbers.py` **879/879**; `verify_market_workflows.py` **ALL CHECKS PASSED** and `--self-test` **8/8**; `verify_market_numbers.py` **ALL CHECKS PASSED**; `verify_economy_numbers.py` **164/164**; `verify_city_numbers.py` **267/267**. The new guards were exercised against deliberately broken inputs — a one-argument F-DP-005 freeze, a flat F-DP-005 limits row, F-DP-007 with a missing and with a partial interval, a flat F-DP-008 row, a limits row naming the wrong freeze, and a handoff header calling 08B next — and each was rejected while the corrected files passed. No validator was weakened. No runtime, multiplayer, load, security, performance or production test was run, because no implementation exists.

**Next authorised action.** **Prompt 08C — diplomacy workflows, edge cases, safeguards and acceptance.** It must use B-08 v1.2 §20–§21 and the v1.2 formula register, must treat F-DP-005/007/008 as the freeze arithmetic and must not claim a runtime test. Prompt 09 remains not authorised.

## 28. Prompt 08C — diplomacy workflows, safeguards, edge cases and acceptance (2026-10-30)

**Scope.** Prompt 08C was the third and final subphase of Stage 2 Prompt 08. It turned B-08 v1.2 and the 08A evidence into an operational specification: the workflows a player and the system follow, the states they move through, the permissions and consent each action requires, the edge cases and failure paths, the notifications and history, the abuse-prevention requirements, the acceptance tests and the implementation handoff. It is **specification and documentation only**. No diplomacy code, database, migration, endpoint, screen, scheduler, service or deployment exists (D-012), and no runtime, load, concurrency, security or usability test was run because there is nothing to run.

**Deliverable.** [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md) v1.0 (1,863 lines, 19 sections): the canonical semantics; **30 workflows** (`DPW-001`…`DPW-030`), each with the same **23 fields**; **8 player journeys**; the proposal, agreement and termination **state machines** (`PT-01`…`PT-08`, `AT-01`…`AT-10`, `ET-01`…`ET-05`); the **treaty lifecycle matrix** for `DP-T01`/`DP-T02`/`DP-T03`/`DP-A01`; **54 edge cases** (`DPE-001`…`DPE-054`); the failure and recovery catalogue reusing the fifteen `DPF` codes; the **authority and permission matrix** (8 actor columns × `A1`–`A14`); the notification matrix (`N1`–`N9`) and the breach-count display rules; the six required views and the confirmation contents; the abuse matrix (18 scenarios); **72 acceptance tests** (`DPA-001`…`DPA-072`); the **21-row requirement trace** (`REQ-012`, `REQ-514`…`REQ-533`) and the twelve-formula trace; the gate evidence register (`DP-RD-01`…`DP-RD-10`); the open-decision disposition; and the implementation handoff.

**Player authority, applied rather than restated.** Every workflow names its initiating actor, the permission, the counterparty consent, and the B-08 rule that authorises it. The specification keeps the 08B boundary intact: the authenticated nation owner is the only diplomatic authority; **no delegation exists**; a proposal becomes an agreement only when both owners accept the exact version; **silence, expiry, dormancy, a view and an administrative act are never consent**; and the automatic list is closed to activation of an accepted proposal, expiry at an agreed deadline, delivery under an accepted aid agreement, embargo term expiry and the reroll/dormancy/political-freeze cleanup. The eight-question authority test is applied to all fourteen actions, and the confirmation contents (counterparty, terms, activation, expiry, cost, visibility, breach consequence) are specified as a requirement, not a screen suggestion.

**What 08C added without adding a mechanic.** It defines operational semantics the rulebook left implicit: a failed action changes nothing except its failure line (no event, notification, reservation or cooldown consumption); the five-step boundary band is cited by every timing workflow; a frozen timer shows its extension; activation is a boundary step, not a receipt; a duplicate submission is refused by its key before any state change; and an accepted proposal turns into an agreement with immutable versioned terms. Where the rulebook was silent, 08C records the question rather than inventing an answer. It proposes no treaty type, sanction, reputation score, delegation model or failure code.

**Traceability.** All **21** diplomacy requirements are accounted for: **20 Covered** and **1 Partially covered** — `REQ-518`, because an active NAP can only block a war declaration once Prompt 10's validator exists. **0 not covered, 0 blocked by an owner decision, 0 deferred.** The twelve formulas each map to workflows and tests; all nine notifications and fifteen failure codes are exercised by at least one test; every `DPW` and every `DPE` appears in at least one `DPA` row.

**Preservation.** No B-08 rule, value or decision changed; `D-123`…`D-132` and `DD-137`…`DD-146` stand; `UD-013` and `UD-033` remain resolved; `UD-039` remains open for Prompt 09 and no delegation is assumed. Global Trade remains approved mandatory long-term scope (D-122, DD-136, REQ-513) with **G-1/G-2/G-3/G-5/G-6 NOT MET and G-4 PARTIAL** — unchanged. No `MKT-`, `F-TM-`, `ECN-`, `URB-`, `DMP-` or `TR-` rule was edited. No `D-`, `DD-`, `REQ-` or `UD-` row was added: 08C makes no design decision and opens no owner question.

**Validator work (no check removed or weakened).**

1. `qa_backups/verify_diplomacy_workflows.py` — a new document checker with **12 groups**: the 19 sections in order; 30 sequential workflows each carrying fields 1–23; 54 sequential `DPE` rows; 72 sequential `DPA` rows with every workflow, edge-case, `DIP-`, `REQ-` and formula reference resolving; the 21-row requirement trace; the twelve formula rows; exactly `N1`–`N9`; exactly `DPF-01`…`DPF-15`; no re-introduced `DRAFT`/`COUNTERED`/`INVALIDATED` state; the authority, silence and Prompt 09 statements; five `NOT MET` plus one `PARTIAL` gate; and the claimed counts. Its **14/14** self-test injects each defect in memory (missing edge case, broken test sequence, undefined workflow/requirement/rule, missing notification, sixteenth failure code, reintroduced state, missing trace row, missing formula row, silence-as-consent, gates marked passed, a stale identifier range) and requires the clean file to pass.
2. `qa_backups/status_rules.py` — **08C joins the completed sub-prompt set**, and `CURRENT_SUBPROMPT` advances to `09`, so a current-status sentence that still calls 08C the next task is caught the same way 07B/07C and 08A/08B were.
3. `qa_backups/validate_final.py` — continuity now requires **08C complete and Prompt 09 next**; `stage-2/00 §10` must name both; log row 08 must record 08A, 08B **and 08C** complete; row 09 must be **Next**; the pending count moves **7 → 6** (Prompts 10–15); the ROADMAP assertion now requires **Prompts 01–08 complete and Prompt 09 next**; a 08C split-prompt fixture was added and the clean header fixture advanced — **10/10**.
4. `qa_backups/09_validate.py` — STATUS expects **09**, pending **6**, row 08 all three sub-prompts, row 09 Next, and the current next-action blocks (§H, §10, log header) must name **Prompt 09** — **348/348**.
5. `qa_backups/test_next_action.py` — the progress table must show exactly one next row, **row 09**, and pending **10–15**; the split-prompt fixtures now use 08C complete / Prompt 09 next and include a **new stale-08C guard**; the real-continuity test asserts 08C and Prompt 09 — **23 tests**.
6. `qa_backups/test_decision_registers.py` — the status block must read **09**, row 08 must record all three sub-prompts plus "designed, **not implemented**", and row 09 must be Next; the old "Prompt 08 must never be called complete" assertion is replaced by the now-true, scoped completion claim — **12 tests**.
7. `qa_backups/verify_politics_numbers.py` — the progress-status guard reads rows 08 and 09 and requires 08C complete / Prompt 09 next — **879/879**, self-test **18/18**.
8. `qa_backups/verify_market_workflows.py` — the continuity guard now requires Prompt 09 as the next task (07C remains recorded as complete) — **14 checks, 0 failed**, self-test **8/8**.

**Continuity updated.** `ROADMAP.md` (Prompts 01–08 complete; Prompt 09 next), `stage-2/01_stage_2_prompt_roadmap.md` (row 08 complete with the 08C deliverable and §28; row 09 Next; a stray "Prompt 08 complete" clause removed from row 07), `stage-2/00_stage_2_handoff.md` (header, state table and §10), `stage-2/02_master_game_design_bible_outline.md` (B-08 entry, prompt row and the 09-only next-prompt cell), `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md` (header, STATUS, §H.6, item 14 of the reading list) and this log (header, row 08, row 09 and this entry). No historical section was rewritten.

**Validation actually run (documentation only, 2026-10-30, from `docs/qa_backups/`).** `verify_diplomacy_workflows.py` **12 groups, 0 failed** and `--self-test` **14/14**; `verify_diplomacy_numbers.py` **9 groups, 0 failed** and `--self-test` **15/15**; `validate_final.py` **ALL CHECKS PASSED** and `--self-test` **10/10**; `test_next_action.py` **23 tests OK**; `test_decision_registers.py` **12 tests OK**; `09_validate.py` **348/348**; `verify_politics_numbers.py` **879/879** and `--self-test` **18/18**; `verify_market_workflows.py` **14 checks, 0 failed** (237 rules, 237 matrix rows, 83 tests) and `--self-test` **8/8**; `verify_market_numbers.py` **ALL CHECKS PASSED** (95/95) and `--self-test` **14/14**; `verify_economy_numbers.py` **164/164**; `verify_city_numbers.py` **267/267**. Each new guard was exercised against a deliberately broken input and rejected it while the corrected file passed.

**Limits.** No player research, no playtest and no runtime evidence. The 72 tests are a design that a future implementation must satisfy, **not executed tests**. The NAP effect remains inert until Prompt 10, `UD-039` remains Prompt 09's, and every numeric value remains Provisional for Prompt 14. The workflows assume the B-02 boundary, B-03 ownership and B-04 transfer semantics exactly as published; they prove nothing about their implementation.

**Next authorised action.** **Stage 2, Prompt 09 — Alliance System and alliance management** ([`16_alliances.md`](16_alliances.md)), as recorded in the Stage 2 register, the ROADMAP, the handoff and this log. Prompt 09 owns alliance founding, constitution, governance, leadership, ranks, membership, shared resources, alliance diplomacy and collective decisions, and must answer **UD-039** by reading B-08 §18 and 08C §9.5/§17.1. It must not reopen Prompt 08, treat the acceptance catalogue as executed, or assume a delegation model.

## 29. Prompt 08C-C — acceptance-matrix, edge-case traceability and reference corrections (2026-10-30)

**Scope.** A focused correction pass on 08C, not a redesign. The audit found that several `DPE` rows named tests that shared a subject but did not exercise the edge case; that `§14.2`'s heading said `DPA-001`…`DPA-012` while its table ran to `DPA-026`; that `§14.9`'s category counts double-counted a supposed "14 embedded lifecycle rows"; and that `DPW-001` cited `§12.7` and `DPW-002` cited `§12.4` instead of `§12.5` and `§12.2` (with `B-08 §13.2`). The pass corrected those defects and hardened the checker that had passed them. No rule, value, decision, requirement or gate changed.

**Complete semantic audit.** All 54 edge cases in `§7.2`–`§7.8` were re-read against the complete `§14` test matrix, not just the nine examples in the audit. Beyond the reported mismatches, the audit found seven more: `DPE-022` was mapped to a freeze test (`DPA-041`), `DPE-023` to the both-frozen test (`DPA-042`), `DPE-024` to a termination/break test (`DPA-032`), `DPE-030` to the freeze read-only test (`DPA-058`), `DPE-037` to a retry test (`DPA-048`), `DPE-038` to the happy-path transfer (`DPA-045`) and `DPE-054` to an audit test (`DPA-070`). Several tests also cited edge cases they did not establish: `DPA-063`/`DPA-064` cited `DPE-045`, `DPA-069` cited `DPE-054`, and `DPA-036` cited `DPE-023`. Each cell was corrected or set to `—`, and where no genuine test existed a new test was specified rather than weakening the edge case.

**Fourteen tests added (`DPA-073`…`DPA-086`).** `DPA-073` logout with a proposal pending; `DPA-074` unanswered renewal; `DPA-075` embargo/trade same-boundary race; `DPA-076` consultation-window freeze (minimum unchanged, end extended); `DPA-077` timer spanning two frozen blocks (union counted once); `DPA-078` notification failure after a committed transfer; `DPA-079` tampered request / client-flag bypass; `DPA-080` acceptance versus expiry; `DPA-081` amendment versus expiry; `DPA-082` activation versus mutual termination; `DPA-083` payer crisis before delivery; `DPA-084` duplicate transfer event; `DPA-085` multiple same-turn breaches and count manipulation; `DPA-086` breach-cooldown exact boundary. Total **86** tests. They sit at the end of their subject section, so `§14.2` is `DPA-001`…`DPA-026` plus `DPA-073`, `§14.3` is `027`–`036` plus `074`, `075`, `080`–`082`, and so on; every heading now lists exactly the rows beneath it.

**New coverage matrix (`§7.10`).** One row per edge case with title, risk, primary and additional tests, the exact assertion that proves coverage, status and follow-up. **53 COVERED, 1 PARTIAL, 0 NOT COVERED, 0 NOT APPLICABLE** at the end of 08C-C. `DPE-049` is PARTIAL because its operator-correction path belongs to Prompt 12; `DPA-062` covers the diplomacy-side publish/append-only behavior. The matrix is explicitly a document review by the agent (AI), **not** a human sign-off and **not** test execution. **Historical note:** 08C-D later separated `DPE-054`'s three disclosure scenarios and made that combined row PARTIAL; the current totals are **52 COVERED / 2 PARTIAL** in §30.

**Reference corrections.** `DPW-001` field 16 now cites `§12.5` (empty states); `DPW-002` field 19 cites `§12.2` (six required views) and `B-08 §13.2` (visibility). A full local-reference scan found every other `§` reference resolving; cross-document references are excluded from the local check.

**Validator hardening (`qa_backups/verify_diplomacy_workflows.py`).** Sixteen groups: sections; 30 workflows × 23 fields; 54 `DPE`; 86 `DPA` with every workflow, edge-case, `DIP-`, `REQ-` reference resolving; `§14` heading sets equal to their tables; category counts equal to the sections and summing to 86; the 54-row coverage matrix with valid status, a real test for every COVERED row, a non-empty assertion, and an explanation for PARTIAL/NOT COVERED; `§7.11` totals matching actual statuses; the two corrected `DPW` references; local `§` references; the 21-row requirement trace; the twelve formulas; `N1`–`N9`; `DPF-01`–`DPF-15`; no re-introduced state; authority/silence/Prompt 09; five `NOT MET` plus one `PARTIAL` gate; and the claimed counts. **16/16 self-tests** (15 negative fixtures plus the clean file), including a wrong DPE→DPA mapping, a COVERED row without a test, a wrong heading range, a count mismatch, both wrong `DPW` references, a sovereignty contradiction inside a test, silence-as-consent inside a test, automatic diplomacy, and a changed Global Trade gate. The checker cannot prove semantic equivalence; the assertion column is the human-readable evidence it is not pretending to automate.

**Preservation.** No B-08 rule, formula, value, decision, requirement or gate changed. `D-122`, `DD-136`, `REQ-513` and **G-1/G-2/G-3/G-5/G-6 NOT MET, G-4 PARTIAL** are untouched. Player sovereignty, explicit bilateral consent, the no-delegation rule and Prompt 09's alliance ownership are intact. No implementation was added.

**Changed files.** `stage-2/15_diplomacy_workflows_acceptance.md` (`§1.5`–`§1.6`, `DPW-001`, `DPW-002`, `DPW-006`, `DPW-013`, DPE test cells, test-row precondition/assertion clarifications, 14 new `DPA` rows, `§14` headings and `§14.9`, new `§7.10`/`§7.11`, traceability/formula test references, `§19.3`), `qa_backups/verify_diplomacy_workflows.py` (rewritten, 16 groups, 16/16 self-test), `ROADMAP.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `stage-2/00_stage_2_handoff.md`, `stage-2/01_stage_2_prompt_roadmap.md` and this log. No decision/requirements/UD register was edited.

**Validation actually run (documentation only, 2026-10-30).** `verify_diplomacy_workflows.py` **16 groups, 0 failed** and `--self-test` **16/16**; plus the full regression suite recorded in `§19.3` of the companion. No runtime, concurrency, security, load or play test exists, because no implementation exists.

**Next authorised action.** **Stage 2, Prompt 09 — Alliance System and alliance management**, unchanged. 08C is accepted at the specification level with `DPE-049` explicitly PARTIAL; Prompt 09 must not treat that as a completed operator-correction design.

---

## 30. Prompt 08C-D — semantic coverage, requirement traceability and acceptance reconciliation (2026-10-30)

**Scope.** A final correction pass on 08C/08C-C after an archive audit found four residual issues: `DPE-054` was treated as one COVERED row although its privileged-read audit is deferred; `DPE-051` named only a generic idempotency test; five requirement rows carried incomplete or wrong references; and the 08C-C log count did not match its list. No rule, formula, value, decision, requirement, treaty, gate or Prompt 09 boundary changed. Nothing was implemented.

**`DPE-051` — replayed acceptance.** `DPA-088` now exercises the actual decision, not a generic retry: B accepts A→B `DP-T01` with key K, the agreement activates, and the identical acceptance is replayed. The assertion is one `ACCEPTED` transition, one exactly-`ACTIVE` agreement, one acceptance event and no second activation, event or consent record; the NAP has no reservation or transfer, so none is invented. `DPE-006`/`DPA-004` remain the generic same-key retry; they are no longer cited as proof of the acceptance case.

**`DPE-054` — three scenarios, one deferred audit.** `§7.10a` records the combined row's three disclosure scenarios separately: unauthorized history read (`DPA-065`), restricted pending terms/public profile (`DPA-065`, `DPA-068`) and notification leakage (`DPA-087`). `DPA-087` proves C — allied to B but not a party — receives no `N1`, no amount or rejection reason, that retry duplicates neither notice nor state, and that the proposal stays `PENDING`. The three disclosure scenarios are **COVERED**. The combined `DPE-054` row stays **PARTIAL** because its stated outcome also includes `DIP-121`'s privileged-read audit, which belongs to Prompt 12's restricted class and cannot be asserted by a B-08 test. No audit behaviour was invented or pulled forward.

**Requirement traceability.** `REQ-514` now points at `DPA-066`/`DPA-068` and no longer at the privacy case; `REQ-515` points at `DPA-001` and no longer at the logout case; `REQ-519` names `DPA-076`; `REQ-532` names `DPA-076`, `DPA-077` and `DPA-083`; `REQ-533` lists `DPA-080`, `DPA-081`, `DPA-082`, `DPA-084` and `DPA-088` explicitly. The checker now expands bare `DPA-080…DPA-082` ranges; previously it silently omitted the interior and falsely reported `REQ-533` as incomplete. Every listed test exists and each verification cell states what proves the requirement.

**Counts.** 54 edge cases: **52 COVERED, 2 PARTIAL, 0 NOT COVERED, 0 NOT APPLICABLE**. 88 acceptance tests: 27 + 15 + 10 + 7 + 11 + 11 + 7. The two partials are `DPE-049` (operator correction) and `DPE-054` (privileged-read audit); both are Prompt 12 dependencies, stated as such in §7.10/§7.10a and not claimed as covered.

**Validator hardening.** `qa_backups/verify_diplomacy_workflows.py` now has targeted checks that `DPE-051` names `DPA-088`, `DPE-054` names `DPA-087`, remains PARTIAL and names its Prompt 12 dependency, the five requirement rows carry their support, and bare DPA ranges expand fully. Its self-test grew to **26/26**: 23 defect guards plus the clean document, the five/seven progress-log guard and the clean log. New guards include `DPE-054` marked COVERED while its audit is deferred, loss of the notification test, a primary DPE→DPA link not mirrored in its test row, `DPE-051` falling back to generic idempotency, the REQ-514/REQ-515 mismatches, an omitted supporting test and a stale 53/1 summary.

**Preservation.** Player sovereignty, explicit bilateral consent, no silence-as-consent, the no-delegation rule, freeze-aware formulas, Prompt 09's alliance ownership, `D-122`, `DD-136`, `REQ-513` and **G-1/G-2/G-3/G-5/G-6 NOT MET, G-4 PARTIAL** are unchanged. No `DIP-`, `DPF-`, `F-DP-`, `MKT-` rule or formula was edited. No human semantic review is claimed; the evidence is the agent's row-by-row document review in §7.10/§7.10a and the structural checks above.

**Changed files.** `stage-2/15_diplomacy_workflows_acceptance.md` (v1.2 header, §7.10a, §13 rows 5/16, REQ-533 support, §19 checklist/validation record), `qa_backups/verify_diplomacy_workflows.py` (bare-range expansion, targeted guards, primary-link reverse traceability, 26/26 self-test), `ROADMAP.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `stage-2/00_stage_2_handoff.md`, `stage-2/01_stage_2_prompt_roadmap.md`, `stage-2/02_master_game_design_bible_outline.md` and this log. `03_requirements_traceability.md`, `04_approved_and_provisional_decisions.md`, `05_unresolved_design_decisions.md`, `DECISIONS.md`, B-08, the formula register and the 08A report were inspected and intentionally left unchanged: no requirement text, decision, UD status or rule changed.

**Validation actually run (documentation only, 2026-10-30).** `verify_diplomacy_workflows.py` **17 groups, 0 failed**; `--self-test` **26/26**; `verify_diplomacy_numbers.py` **9 groups, 0 failed**; `test_next_action.py` **23 tests OK**; `test_decision_registers.py` **12 tests OK**; `validate_final.py` **ALL CHECKS PASSED**; `09_validate.py` **348/348**. No runtime, concurrency, security, load or play test exists, because no implementation exists.

**Next authorised action.** **Stage 2, Prompt 09 — Alliance System and alliance management** (`16_alliances.md`). 08C is accepted at the specification level with two documented Prompt 12 dependencies; Prompt 09 must not treat them as completed designs or reopen Prompt 08's rules.

---

## 31. Prompt 08C-E — exhaustive bidirectional traceability and acceptance closure (2026-10-30)

**Scope.** A final traceability and QA correction pass on 08C/08C-C/08C-D. It did not redesign Diplomacy, change a `DIP-`, `DPF-`, `F-DP-` or `MKT-` rule, alter a decision or requirement status, or begin implementation. The canonical companion is now **v1.3**.

**Methodology.** `§15.1.1` states that the project uses **exhaustive bidirectional traceability**, not a representative test list. `§15.1` is the requirement summary; **`§15.5` is the authoritative relationship ledger**; `§14` owns each scenario and assertion; this register and `03_requirements_traceability.md` own requirement text and status. Every test-side `REQ-` cell must appear in the ledger, every ledger row must appear in its test, and every **DIRECT** row must appear in the requirement's `Test` cell. **SUPPORTING** evidence is listed but never counted as direct; **DEFERRED** names its owner and is not covered; **NOT COVERED** has no qualifying test and no owner.

**The three reported relationships.** `DPA-041` is **DIRECT for `REQ-532`** (freeze-extended proposal expiry; the earlier omission was a ledger gap, not an invalid test). `DPA-087` is **DIRECT for `REQ-012`** (a non-party notification carries no private term, amount, rejection reason or P2 data) and **SUPPORTING for `REQ-533`** (it proves notification privacy and retry idempotency, not the full boundary band or P6 publication). `DPA-088` is **DIRECT for `REQ-523` and `REQ-533`**: it exercises an authorized explicit acceptance, initial processing, activation, replay of the identical acceptance, one agreement, one acceptance event, no second activation and no duplicate resource effect.

**Full audit.** All 88 `DPA` rows and all 21 traced requirements (`REQ-012`, `REQ-514`…`REQ-533`) were re-read. The final ledger has **118 relationship rows**: **101 DIRECT**, **16 SUPPORTING** and **1 DEFERRED** (`REQ-518`, because Prompt 10 owns war-declaration enforcement). Twenty requirements have direct test coverage; `REQ-518` has none by design. There are no remaining bidirectional mismatches, no duplicate pair, no supporting row counted as direct and no unowned uncovered requirement. `DPE-051` keeps its acceptance-replay test `DPA-088`; `DPE-054` keeps its three separated disclosure scenarios (`DPA-065`, `DPA-068`, `DPA-087`) and remains **PARTIAL** only for the Prompt 12 privileged-read audit.

**Coverage counts.** 30 workflows, 54 edge cases, **52 COVERED / 2 PARTIAL / 0 NOT COVERED / 0 NOT APPLICABLE**, 88 acceptance tests, 12 traced formulas, 15 failure codes and 9 notifications. These are **designed tests**, not executed tests. No runtime, concurrency, load, security or playability claim is made.

**Validator hardening.** `qa_backups/verify_diplomacy_workflows.py` now parses `§15.5` and enforces: all 21 requirement groups; exactly 117 direct/support pairs (101/16) plus the `REQ-518` deferred row; each test claim classified; each ledger row mirrored in the test; each direct row present in the summary; supporting rows not counted as direct; group counts equal to their rows; duplicate-pair detection; and defined `DPE`/`DIP` references. The self-test is **31/31** (28 defect guards, clean document, progress-log guard, clean log), including six new ledger-negative fixtures (missing pair, wrong classification, wrong group count, summary over-count, duplicate pair and a supporting row counted as direct).

**Preservation.** Player sovereignty, explicit bilateral consent, no silence-as-consent, no delegation, freeze-aware formulas, proposal/treaty lifecycles, resource and trade integrity, embargo behaviour, reputation/breach rules, Politics/Military boundaries, Prompt 09's alliance ownership, `D-122`, `DD-136`, `REQ-513` and **G-1/G-2/G-3/G-5/G-6 NOT MET, G-4 PARTIAL** are unchanged. No owner decision was made and no gate was promoted.

**Changed files.** `stage-2/15_diplomacy_workflows_acceptance.md` (v1.3 header/status, `§1.6`, `§15.1.1`, `§15.5` ledger, `§19` acceptance/validation record), `qa_backups/verify_diplomacy_workflows.py` (ledger parser, bidirectional checks, six new fixtures, 31/31 self-test), `stage-2/03_requirements_traceability.md` (traceability methodology), `stage-2/02_master_game_design_bible_outline.md`, `stage-2/01_stage_2_prompt_roadmap.md`, `stage-2/00_stage_2_handoff.md`, `ROADMAP.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md` and this log. B-08, the formula register, the decision/UD registers, the 08A report and all market documents were not edited.

**Validation actually run (documentation only, 2026-10-30).** `verify_diplomacy_workflows.py` **17 groups, 0 failed**; `--self-test` **31/31**; `verify_diplomacy_numbers.py` **9 groups, 0 failed**; `--self-test` **15/15**; `validate_final.py` **ALL CHECKS PASSED**; `--self-test` **10/10**; `test_next_action.py` **23 tests OK**; `test_decision_registers.py` **12 tests OK**; `09_validate.py` **348/348**; `verify_politics_numbers.py` **879/879**; `--self-test` **18/18**; `verify_market_workflows.py` **all passed**; `--self-test` **8/8**; `verify_market_numbers.py` **all passed**; `--self-test` **14/14**; `verify_economy_numbers.py` **164/164**; `verify_city_numbers.py` **267/267**. No runtime test exists, because no implementation exists.

**Final status.** **PASS at the documentation and traceability level.** Two documented Prompt 12 dependencies remain (`DPE-049` operator correction and `DPE-054` privileged-read audit); `REQ-518` remains deferred to Prompt 10. No implementation occurred.

**Next authorised action.** **Stage 2, Prompt 09 — Alliance System and alliance management** (`16_alliances.md`). It owns alliance governance and must answer `UD-039` without assuming a delegation model, and must not reopen Prompt 08.

---

## 32. Prompt 09A — alliance research, requirements baseline and cross-system integration (2026-10-31)

**Scope.** Research and documentation only. 09A read the canonical Prompts 01–08C material, researched Politics & War across official, community, live-practice, third-party and anecdotal sources, compared eRepublik, Stellaris, EVE and Call of War, inspected UD-039, and produced the evidence base for B-09. No rule was approved, no gameplay was implemented and no schema, endpoint, screen or deployment exists.

**Deliverables.** `research/09A_alliance_research.md` (main report, 22 sections), `research/09A_alliance_sources_findings.md` (25 sources `ALS-001`…`ALS-025`, 40 findings `ALR-001`…`ALR-040`, 7 conflicts, 10 candidate recommendations, 8 open questions) and `research/09A_alliance_integration_matrix.md` (`AX-01`…`AX-26`, 20 fields each).

**Registers.** **REQ-534…REQ-617** (84 rows, all **Proposed**; total **617 = 19 Approved / 507 Provisional / 5 Open / 2 Deferred / 84 Proposed**); **DD-147…DD-150** (total **150**); **UD-040…UD-049** added and **UD-039** left deferred with a recorded recommendation (total **49 = 24 Resolved / 7 Deferred / 18 Open**); **D-133** (no real-time chat; Discord external only) and **D-134** (09A/09B/09C split and B-09 path). No earlier ID was renumbered or reopened, and the Diplomacy and Market canonical documents were not edited.

**Boundary.** `D-133` and `DD-147` exclude chat, DMs, presence, typing, read receipts, message storage, bots, Discord API/OAuth/linking, role sync, mirroring and hosted chat. `DD-148` limits the Discord surface to one optional static, allowlisted, audited invite URL. `DD-149` preserves the existing ownership boundaries; 09A recommends **no alliance-level treaty object** at first release, with member-nation consent for anything binding; this no-object path is outside UD-039's recorded a/b/c options, so UD-039 stays deferred and 09B must obtain the owner's choice.

**Checks.** `09_validate.py`, `validate_final.py`, `test_decision_registers.py`, `test_next_action.py`, `verify_politics_numbers.py`, `verify_market_workflows.py`, `verify_diplomacy_numbers.py`, `verify_diplomacy_workflows.py` and `verify_market_numbers.py` were rerun after the register and continuity updates; the hard-coded totals and next-action expectations were advanced to the values above, with no assertion deleted or weakened.

**Next authorised action.** **Stage 2, Prompt 09B — Alliance foundations (B-09, `16_alliances.md`).** It must resolve or carry forward UD-012, UD-039 and UD-040…UD-049, write the B-09 specification, and may not add chat or any Discord integration.

---

## 33. Prompt 09A-C — alliance corrections, permissions audit, semantic traceability and handoff reconciliation (2026-10-31)

**Scope.** A focused correction of 09A. It did not repeat the research stage, redesign the Alliance System, approve a candidate requirement, resolve UD-039, change an owning subsystem's rule, or begin Prompt 09B. No gameplay, schema, API, screen, Discord integration or communication infrastructure was created.

**AX semantic audit.** All 26 AX records were re-read against the canonical requirement text. The matrix now has **76 requirement relationships**: **41 DIRECT DEPENDENCY**, **17 RELATED CONSTRAINT**, **6 SUPPORTING CONTEXT** and **12 explicit NO EXISTING REQUIREMENT rows**. **Eleven invalid references were removed**: REQ-012 from AX-01/03/04/09, REQ-176 from AX-01/02, REQ-530 from AX-06/08/11 and REQ-532 from AX-16/17. Replacements were chosen from the requirements' actual rules: ownership and identity (REQ-002/061/043/004), dormancy and reroll (REQ-091/085), alliance roles and succession (REQ-013), economy conservation and ledger (REQ-005/153/154/170/176), storage (REQ-141/142), city contracts (REQ-172/218), visibility (REQ-057), diplomacy authority and consent (REQ-523/529/530/531/175), audit and moderation (REQ-021/025/026/027), and Global Trade (REQ-513/010). `DIP-146`–`149` were relabelled from "decisions" to B-08 rules. Seven candidate dependency cells were also corrected (REQ-534/535/548/562/571/576/579); no requirement text, status, ID or count changed.

**Permissions research.** The current Fandom `Alliance_Permissions` page was read directly on 2026-10-31 and records **15** permissions: View Bank; Withdraw Bank; Change Permissions; See Spies; See Reset Timers; Tax Brackets; Post Announcements; Manage Announcements; Manage Applicants; Remove Members; Edit Alliance Info; Manage Treaties; Manage Market Share; Manage Embargoes; Promote Self to Leader. The report documents the default Leader/Heir/Officer/Member/Applicant bundles, custom positions, per-permission risk, treasury/treaty/embargo/tax implications, and a 15-row comparison table. **Promote Self to Leader is explicitly not adopted**: it permits self-promotion "at any time"; an Heir can also self-appoint when no Leader exists; Change Permissions can define a custom position carrying it. No permission model was approved.

**Black Knights correction.** `bkpw.net/apply` and the live alliance page (id 877) were read on 2026-10-31. The verified process is: (1) become an Applicant through the official in-game join screen; (2) join the alliance Discord, which the live page calls a joining requirement; (3) run `/apply nationid:<id>` so an alliance-operated bot creates an interview workflow; `/applications status` reports progress. The bot is third-party tooling ("Powered by Nexus AMS"), not a P&W feature. The page's "Requirements and policies" panel is unpublished placeholder text, so no minimum requirement or review duration is asserted. The earlier 24-hour interview claim belongs to Rose and was not transferred.

**Sources.** ALS-013 is now directly accessed (HTTP 200) and still classified `COMMUNITY DOCUMENTATION` with no published revision date. ALS-016 and ALS-017 now use exact thread permalinks (`topic/9902-tiered-bank-access/` and `topic/6269-alliance-heirarchy-permissions-member-titles-and-seniority/`); ALS-027 adds the 2018 self-promotion thread; ALS-026 adds the live Black Knights alliance page. The register now has **27 sources**, **49 findings** (`ALR-001`–`ALR-049`), **9 conflicts**, **14 candidate recommendations** and **10 open questions**. ALR-032's unsupported "most alliances use five ranks" claim was withdrawn.

**Handoff reconciliation.** The opening status, current prompt, next-action section, prompt-status table, Stage 2 roadmap, project roadmap, project progress, AI context and AI handoff now all state **09A accepted after 09A-C, 09B next**. Dated history is retained. 09A-C is recorded as correction-in-progress and accepted in the same pass because every mandatory correction criterion passed; 09B remains blocked until this record is accepted.

**Validator.** New `qa_backups/09A_validate_alliance.py` checks AX completeness, identifier existence, classification vocabulary, evidence presence, stale pairs, subsystem ownership, Global Trade gates, Discord/chat exclusions, register counts and statuses, candidate dependencies, the 15-permission inventory, forum permalinks, change logs and one next action. It distinguishes structural/reference checks from the human semantic review in `09A_alliance_reference_review.md`. Its clean fixture passes and all **15** declared negative fixtures fail as required.

**Validation actually run (documentation only, 2026-10-31).**

- `python docs/qa_backups/09A_validate_alliance.py` — **790 checks, 0 failed**.
- `python docs/qa_backups/test_09A_alliance_validator.py` — **16 tests, OK** (1 clean fixture + 15 negative fixtures, including the UD-039 no-object mislabelling guard).
- `python docs/qa_backups/09_validate.py` — **358/358 checks passed**.
- `python docs/qa_backups/validate_final.py` — **ALL CHECKS PASSED**.
- `python docs/qa_backups/test_decision_registers.py` — **12 tests, OK**.
- `python docs/qa_backups/test_next_action.py` — **23 tests, OK**.
- `python docs/qa_backups/verify_politics_numbers.py` — **879/879**.
- `python docs/qa_backups/verify_market_workflows.py` — **ALL CHECKS PASSED**.
- `python docs/qa_backups/verify_diplomacy_numbers.py` — **9 groups, 0 failed**.
- `python docs/qa_backups/verify_diplomacy_workflows.py` — **17 groups, 0 failed**.
- `python docs/qa_backups/verify_market_numbers.py` — **ALL CHECKS PASSED**.
- `python docs/qa_backups/verify_economy_numbers.py` — **164/164**.
- `python docs/qa_backups/verify_city_numbers.py` — **267/267**.

No runtime, load, security, usability or playtest check exists, because no implementation exists.

**Preservation.** `D-133`, `DD-147`, `DD-148` (Provisional), `DD-149`, `DD-150`, `UD-039` (Deferred) and `UD-040`–`UD-049` (Open) are unchanged; `REQ-534`–`REQ-617` remain 84 Proposed rows; Global Trade remains approved scope (`D-122`, `DD-136`, `REQ-513`) and release-gated by `G-1`…`G-6`. No owning document was edited.

**Changed files.** `research/09A_alliance_research.md` (v1.1), `research/09A_alliance_sources_findings.md` (v1.1), `research/09A_alliance_integration_matrix.md` (v1.1), `research/09A_alliance_reference_review.md` (new), `03_requirements_traceability.md` (v1.21), `04_approved_and_provisional_decisions.md` (v3.3 note), `05_unresolved_design_decisions.md` (v1.16 and tally fix), `00_stage_2_handoff.md`, `01_stage_2_prompt_roadmap.md`, `02_master_game_design_bible_outline.md`, `06_stage_2_progress_log.md`, `ROADMAP.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `qa_backups/09A_validate_alliance.py` (new) and `qa_backups/test_09A_alliance_validator.py` (new).

**Final status.** **PASS at the documentation, evidence and traceability level.** No gameplay was implemented and no requirement or decision was approved.

**Next authorised action.** **Stage 2, Prompt 09B — Alliance foundations (B-09, `16_alliances.md`).** It must resolve or carry forward UD-012, UD-039 and UD-040–UD-049, and may not add chat or any Discord integration.

---

## 34. Prompt 09A-D — final alliance treasury storage traceability correction, AX-08 validation and Prompt 09A acceptance closure (2026-10-31)

**Scope.** Final documentation, research-traceability and QA correction pass on Prompt 09A and its correction sequence. Prompt 09A research was not repeated; no gameplay, schema, API, screen, Discord integration or communication infrastructure was created; and Prompt 09B was not started. No existing Diplomacy, Economy, City, Market, Global Trade or Military rule was changed.

**Distinction between national warehouse and Alliance Treasury.**
- National warehouse storage rules (`ECN-120` / `REQ-141`) establish one shared warehouse capacity `W` holding 11 resources for a single nation's inventory.
- National overflow blocking (`ECN-124` / `REQ-142`) blocks production batches and market purchases when `free_space < output`.
- Alliance pools (`REQ-176`) are separate audited pools with their own ledger and permissions, and may not mint crowns or resources or bypass restrictions.
- Neither `REQ-141` nor `REQ-142` establishes storage capacity, deposit limits or overflow behaviour for a separate Alliance Treasury pool. An alliance deposit is a transfer of already-owned assets into a segregated audited pool, not a national production or market purchase action.
- Alliance pool capacity, deposit limits, and over-capacity deposit behaviour remain an unresolved design decision (`UD-046`), scheduled for Prompt 09B in coordination with the Economy system owner.

**AX-08 requirement classifications.**
- `REQ-141`: Reclassified from `DIRECT DEPENDENCY` to `RELATED CONSTRAINT`. Governs national warehouse storage capacity; informs future Alliance design but does not define Alliance Treasury capacity.
- `REQ-142`: Reclassified from `DIRECT DEPENDENCY` to `RELATED CONSTRAINT`. Governs national production/purchase overflow blocking; does not establish alliance deposit restrictions or overflow handling.
- `REQ-176`: Retained as `DIRECT DEPENDENCY` for separate audited pool ownership, ledger separation, auditability and resource integrity boundaries, without extending to an unapproved numerical capacity limit.
- Added explicit missing requirement row: `| AX-08 | — | No existing requirement defines alliance pool capacity or over-capacity deposit behaviour | **NO EXISTING REQUIREMENT** | ... | No | UD-046 |`.
- Explicit AX-08 clarification added: *"Existing national warehouse capacity and production/purchase restrictions do not automatically establish Alliance Treasury storage capacity or deposit behaviour. Alliance pool capacity and over-capacity handling remain unresolved and require an explicit Alliance System design decision, coordinated with the Economy system owner."*

**Reconciled relationship counts.**
The integration matrix now has **77 requirement relationships**:
- **39 DIRECT DEPENDENCY** (-2 from REQ-141, REQ-142)
- **19 RELATED CONSTRAINT** (+2 from REQ-141, REQ-142)
- **6 SUPPORTING CONTEXT** (unchanged)
- **13 explicit NO EXISTING REQUIREMENT rows** (+1 from AX-08; across 13 AX records: AX-01, AX-08, AX-09, AX-12, AX-13, AX-14, AX-16, AX-18, AX-19, AX-20, AX-22, AX-24, AX-26).
- All summary tables, reference reviews, handoffs and continuity documents reconciled.

**Wider economic integration review.**
Verified resource ownership, direction and boundaries across all economic integration records:
- `AX-06` (deposits): Contributing nation owns assets before; pool owns after; value-conserving transfer; `REQ-176`, `REQ-005`, `REQ-154`, `REQ-170` DIRECT.
- `AX-07` (withdrawals): Pool owns before; member owns after; two-phase reserve/commit draw; `REQ-013`, `REQ-176`, `REQ-005`, `REQ-153`, `REQ-170` DIRECT; `UD-046` Open.
- `AX-08` (storage limits): Segregated pool holding owned resources; `REQ-176` DIRECT; `REQ-141`, `REQ-142` RELATED; capacity Open under `UD-046`.
- `AX-11` (city support): B-05/B-04 cost validation and ledger transfer of already-owned value; `REQ-172` DIRECT; `REQ-218`, `REQ-005` RELATED.
- `AX-12` (readiness): Voluntary member self-declarations; `REQ-091` SUPPORTING; `REQ-023` RELATED; no private play data inference.
- `AX-17` (embargo checks): Shared-network pair checks and embargo enforcement on transfers; `REQ-529`, `REQ-175`, `REQ-170` DIRECT.
- `AX-18` (war coordination): Deferred to Prompt 10; B-10 owns warfare; no alliance execution power.
- `AX-26` (Global Trade): B-07 owns market; no alternate trade channel; `REQ-513`, `REQ-010` DIRECT; release gates `G-1`…`G-6` intact.

**Preservation audit.**
- `UD-046` preserved as Open and unresolved for Prompt 09B; scope clarified to explicitly cover alliance-pool storage capacity and deposit overflow handling alongside withdrawals and dual approval; AX-08 cross-reference added.
- `UD-039` (Deferred), `UD-040`–`UD-049` (Open) preserved with original questions and options.
- `REQ-534`–`REQ-617` remain 84 Proposed rows; no candidate requirement approved, deleted or renumbered.
- `D-133` and `DD-147`–`DD-150` preserved: no chat, no real-time messaging, Discord external only.
- Prompts 01–08C, Global Trade (`D-122`, `DD-136`, `REQ-513`, `G-1`…`G-6`) intact.

**Validator strengthening and verification results.**
- `09A_validate_alliance.py`: Added group `12-treasury-storage` (835 checks, 0 failed) checking AX-08 structure, REQ-141/142 classifications/evidence, REQ-176 scope, missing requirement row, open `UD-046` reference, prohibited national-warehouse substitution, prohibited deposit-as-purchase claims, and exact count reconciliations (39/19/6/13 = 77).
- `test_09A_alliance_validator.py`: Extended to **27 tests, OK** (1 clean fixture + 26 negative fixtures, including the 11 new AX-08 negative test fixtures).
- All regression suites rerun and passed clean:
  - `python docs/qa_backups/09A_validate_alliance.py` — **835 checks, 0 failed**.
  - `python docs/qa_backups/test_09A_alliance_validator.py` — **27 tests, OK**.
  - `python docs/qa_backups/09_validate.py` — **358/358 checks passed**.
  - `python docs/qa_backups/validate_final.py` — **ALL CHECKS PASSED**.
  - `python docs/qa_backups/test_decision_registers.py` — **12 tests, OK**.
  - `python docs/qa_backups/test_next_action.py` — **23 tests, OK**.
  - `python docs/qa_backups/verify_politics_numbers.py` — **879/879**.
  - `python docs/qa_backups/verify_market_workflows.py` — **ALL CHECKS PASSED**.
  - `python docs/qa_backups/verify_diplomacy_numbers.py` — **9 groups, 0 failed**.
  - `python docs/qa_backups/verify_diplomacy_workflows.py` — **17 groups, 0 failed**.
  - `python docs/qa_backups/verify_market_numbers.py` — **ALL CHECKS PASSED**.
  - `python docs/qa_backups/verify_economy_numbers.py` — **164/164**.
  - `python docs/qa_backups/verify_city_numbers.py` — **267/267**.

**Final status.** **PASS at the documentation, research-traceability and QA level.** Prompt 09A is formally accepted.

**Next authorised action.** **Stage 2, Prompt 09B — Alliance foundations (B-09, `16_alliances.md`).** It must resolve or carry forward UD-012, UD-039 and UD-040–UD-049 (including the treasury storage capacity decision under UD-046), write the B-09 specification, and may not add chat or any Discord integration.


## 35. Prompt 09A-E — final AX-08 wording corrections, treasury policy status, handoff reconciliation and acceptance closure (2026-10-31)

**Mission:** Focused final correction pass on Prompt 09A and its correction sequence through Prompt 09A-D, addressing four specific issues identified in the archive audit:
1. Replaced the AX-08 summary in `09A_alliance_integration_matrix.md` §2 to explicitly state that national warehouse capacity does not establish Alliance Treasury capacity.
2. Corrected the AX-08 failure/recovery and economic impact descriptions in `09A_alliance_integration_matrix.md` §4 to explicitly establish that over-capacity deposit behaviour and capacity rules are unresolved under `UD-046` for Prompt 09B.
3. Reconciled four stale current-status references in the Stage 2 handoff and Master Game Design Bible outline that cited Prompt 09A acceptance after 09A-C instead of Prompt 09A-D/09A-E, while strictly preserving historical completion logs.
4. Reconciled validator check counts across the handoff, research, and progress records: corrected the stale 829 count to the 835 checks executed in 09A-D, and recorded the 849 checks executed in 09A-E.

**Scope & Governance Boundaries:**
- Strictly documentation, QA validators, self-tests, and handoff records.
- No gameplay, database schema, API, UI, Discord bot or real-time communication infrastructure created.
- Product decision `D-133` and technical positions `DD-147`–`DD-150` strictly preserved: no chat, no real-time messaging, Discord is external only.
- Candidate requirements `REQ-534`–`REQ-617` remain 84 **Proposed** rows; none approved.
- Unresolved design decisions `UD-039` (Deferred) and `UD-040`–`UD-049` (Open) preserved; `UD-046` remains Open for Prompt 09B.
- Prompts 01–08C, Global Trade (`D-122`, `DD-136`, `REQ-513`, `G-1`…`G-6`) intact.

**AX-08 Wording Corrections:**
- Summary (§2, row AX-08): Replaced `"Hold pooled resources within Economy capacity"` with:
  `"Determine whether a separately approved Alliance Treasury capacity rule is required; national warehouse capacity does not establish Alliance-pool capacity."`
- Economic impact (§4, row AX-08): Clarified from `"Capacity only"` to:
  `"Alliance Treasury capacity unestablished; national warehouse capacity cannot be substituted; storage impact subject to UD-046; no capacity formula approved"`.
- Failure & recovery (§4, row AX-08): Replaced `"Reject over-capacity deposit cleanly"` with:
  `"Over-capacity deposit behaviour is unresolved under UD-046 (do not assume rejection, partial acceptance, queuing, resource loss or any other outcome; Prompt 09B must define policy)"`.

**Handoff & Outline Reconciliation:**
- Reconciled all current-status statements in `docs/stage-2/00_stage_2_handoff.md` (lines 3, 4, 41, 140) and `docs/stage-2/02_master_game_design_bible_outline.md` (lines 145, 304) to reflect Prompt 09A accepted after Prompt 09A-E (with 09A-D substantive treasury storage correction), Prompt 09B next.
- Reconciled current status in `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/ROADMAP.md`, `docs/PROJECT_PROGRESS.md`, and `docs/stage-2/01_stage_2_prompt_roadmap.md`.
- Preserved all historical completion entries (§33 Prompt 09A-C, §34 Prompt 09A-D).

**Validator Strengthening and Verification:**
- `09A_validate_alliance.py`:
  - Added outline document to mandatory structure validation.
  - Added checks verifying Prompt 09A-E correction record in research §25 and matrix §6.
  - Added negative checks verifying AX-08 summary does NOT contain `"hold pooled resources within economy capacity"` and positive checks verifying it states `"national warehouse capacity does not establish"`.
  - Added negative checks verifying AX-08 failure/recovery does NOT contain `"reject over-capacity deposit cleanly"` and positive checks verifying it states over-capacity behaviour is unresolved under `UD-046`.
  - Added checks verifying AX-08 resource impact is not unclarified `"capacity only"` and states capacity is unestablished under `UD-046`.
  - Added checks detecting stale `"accepted after 09A-C"`, `"Accepted (09A/09A-C)"`, and `"following the 09A-C correction"` current-status text in handoff and outline.
  - Added check detecting stale `"829 checks"` count in handoff.
  - Total checks executed: **849 checks, 0 failed**.
- `test_09A_alliance_validator.py`:
  - Added 6 new negative self-test fixtures:
    - `test_27_ax08_summary_economy_capacity`: verifies failure if AX-08 summary claims "Hold pooled resources within Economy capacity".
    - `test_28_ax08_failure_reject_overcapacity`: verifies failure if AX-08 failure/recovery claims "Reject over-capacity deposit cleanly".
    - `test_29_ax08_resource_impact_capacity_only`: verifies failure if AX-08 resource impact is "Capacity only".
    - `test_30_stale_handoff_09ac_status`: verifies failure if handoff contains stale 09A-C current status.
    - `test_31_stale_outline_09ac_status`: verifies failure if Bible outline contains stale 09A-C current status.
    - `test_32_stale_validator_count_829`: verifies failure if handoff cites stale 829 count.
  - Total self-tests: **33 tests, OK** (1 clean fixture + 32 negative fixtures).

**Validation Record:**
- `python docs/qa_backups/09A_validate_alliance.py` — **849 checks, 0 failed**.
- `python docs/qa_backups/test_09A_alliance_validator.py` — **33 tests, OK**.

**Final Status:** **PASS**. Prompt 09A is accepted at the research, integration matrix, and requirements baseline level. Prompt 09B is authorized as the next task.


## 36. Prompt 09A-F — final project status reconciliation, handoff validation and alliance research acceptance closure (2026-10-31)

**Mission:** Perform the final status reconciliation, handoff validation hardening, and formal acceptance closure for Prompt 09A:
1. Reconciled every stale current-status statement across `AI_CONTEXT.md`, `AI_HANDOFF.md`, `01_stage_2_prompt_roadmap.md`, `06_stage_2_progress_log.md`, `00_stage_2_handoff.md`, `02_master_game_design_bible_outline.md`, `ROADMAP.md`, and `PROJECT_PROGRESS.md` to reflect Prompt 09A acceptance after Prompt 09A-F (with 09A-D and 09A-E substantive corrections), with Prompt 09B authorized as the next task.
2. Strictly preserved genuine historical completion entries for Prompt 09A (§32), Prompt 09A-C (§33), Prompt 09A-D (§34), and Prompt 09A-E (§35).
3. Hardened the documentation validator with group `13-current-status` verifying cross-document status consistency, presence of 09A-F closure evidence, and absence of stale current-status claims, backed by 10 new negative self-test fixtures.
4. Confirmed that AX-08 national warehouse distinction, unapproved deposit policy under `UD-046`, and 77 relationship totals remain preserved.
5. Formally accepted Prompt 09A at the research, integration matrix, and candidate requirements baseline level, and authorized Prompt 09B as next.

**Scope & Governance Boundaries:**
- Strictly documentation, QA validators, self-tests, and handoff records.
- No gameplay, database schema, API, UI, Discord bot or real-time communication infrastructure created.
- Product decision `D-133` and technical positions `DD-147`–`DD-150` strictly preserved: no chat, no real-time messaging, Discord is external only.
- Candidate requirements `REQ-534`–`REQ-617` remain 84 **Proposed** rows; none approved.
- Unresolved design decisions `UD-039` (Deferred) and `UD-040`–`UD-049` (Open) preserved; `UD-046` remains Open for Prompt 09B.
- Prompts 01–08C, Global Trade (`D-122`, `DD-136`, `REQ-513`, `G-1`…`G-6`) intact.

**Current-Status Reconciliation Inventory:**
- `AI_CONTEXT.md`: lines 3, 20 (STATUS block), 33, 118, 128 updated to 09A accepted after 09A-F, 09B next; progress-log index updated to §36.
- `AI_HANDOFF.md`: lines 3, 22 (STATUS block), 286, 290, 392, 404, 438 updated to 09A accepted after 09A-F, 09B next; added explicit Prompt 09B instructions regarding research inheritance, UD-046, AX-08, and communication boundaries.
- `01_stage_2_prompt_roadmap.md`: line 4, line 24 (row 09), line 242 updated to 09A accepted after 09A-F, 09B next, citing log sections `[§32]–[§36]`.
- `06_stage_2_progress_log.md`: lines 4, 6, 8, 34 updated to 09A accepted after 09A-F, 09B next; Section 36 added.
- `00_stage_2_handoff.md`: lines 3, 4, 41, 140 updated to 09A accepted after 09A-F, 09B next.
- `02_master_game_design_bible_outline.md`: lines 145, 304 updated to 09A accepted after 09A-F, 09B next.
- `ROADMAP.md`: lines 5, 15 updated to 09A accepted after 09A-F, 09B next, citing log sections `[§32–§36]`.
- `PROJECT_PROGRESS.md`: lines 3, 20 (STATUS block), 53, 67, 75, 79 updated to 09A accepted after 09A-F, 09B next.
- `09A_alliance_research.md`: bumped to v1.4, status updated, Section 26 added.
- `09A_alliance_integration_matrix.md`: bumped to v1.4, Section 6 and 7 updated.

**Validator Strengthening and Verification:**
- `09A_validate_alliance.py`:
  - Added checks verifying Prompt 09A-F correction records in research §26 and matrix §6 and §7.
  - Added group `13-current-status` (checks 1–10) verifying cross-document status consistency.
  - Verified absence of stale current-status claims (09A-C, 09A-D, 09A-E as current acceptance state) across all 8 continuity documents.
  - Prompt 09A-F completion record presence verified.
  - Command: `python docs/qa_backups/09A_validate_alliance.py` — **904 checks, 0 failed**.
- `test_09A_alliance_validator.py`:
  - Added 10 new negative self-test fixtures (`test_33`–`test_42`) covering each stale current-status failure mode and false-positive protection.
  - Command: `python docs/qa_backups/test_09A_alliance_validator.py` — **43 tests OK (1 clean fixture + 42 negative fixtures)**.

**Final Status:** **PASS**. Prompt 09A is accepted at the research, integration matrix, and requirements baseline level. Prompt 09B is authorized as the next task.

## 37. Prompt 09B completion — Alliance Foundations, Player-Defined Constitutions, Governance Rules, Permissions, Treasury, and Cross-System Specification (2026-10-31)

**Mission:** Complete the canonical Alliance System rulebook (`B-09`), formula register, integration contracts, and decision registers for Nation Supremacy:
1. Authored canonical Alliance System rulebook `docs/stage-2/16_alliances.md` (`B-09`) containing all 28 required sections (`ALL-001` through `ALL-178`).
2. Established Mandatory Owner-Approved Design Direction: Open-ended, player-authored Alliance Constitutions (`D-135`). Nation Supremacy does not impose a mandatory political system, constitution template, ideology, or fixed internal hierarchy. Established 4-tier governance taxonomy: Documented Constitutional Rule (Tier 1), System-Enforceable Governance Control (Tier 2), Internal Political Agreement (Tier 3), and Global Platform Rule (Tier 4). Prose is never parsed into executable mechanics (`ALL-025`, `ALL-026`).
3. Authored Alliance formula register `docs/stage-2/16_alliances_formula_register.md` specifying `F-AL-001` through `F-AL-005` (dedicated pool capacity, founding fee, 240-turn dormancy window, 12-turn rejoin cooldown, and 50,000 crowns / 10% multi-signature dual authorization threshold).
4. Authored cross-system integration contracts ledger `docs/stage-2/16_alliances_integration_contracts.md` defining complete 20-field specifications for all 26 `AX-01` through `AX-26` integration contracts with explicit rule links to `TRN-`, `ACC-`, `ECN-`, `CIT-`, `DMP-`, `MKT-`, `DIP-`, and future Prompt 10/11/12/13/14 interfaces.
5. Recorded approved decisions `D-135` through `D-139` contiguously in `docs/DECISIONS.md` and `DD-151` through `DD-160` in `docs/stage-2/04_approved_and_provisional_decisions.md`.
6. Reconciled all 84 candidate requirements (`REQ-534` through `REQ-617`): promoted 83 to `Provisional` and marked `REQ-591` as `Deferred to Prompt 10` (total register: 19 Approved, 590 Provisional, 5 Open, 3 Deferred, 0 Proposed = 617 total).
7. Preserved unresolved decisions register counts (24 Resolved, 7 Deferred, 18 Open = 49 total), with `UD-046` architectural principles decided and operational workflows carried forward to Prompt 09C and Prompt 14.
8. Preserved all core system boundaries: player sovereignty over national diplomacy (`B-08`), zero real-time chat (`D-133`, `DD-147`), static external Discord link only (`DD-148`), and Global Trade independence (`D-122`, `DD-136`).
9. At that time advanced the project status to Prompt 09B Complete and Prompt 09C next *(superseded by Prompt 09B-E)*.

**Final Status:** **PASS** *(historical 09B entry; its 09C authorization is superseded by Prompt 09B-E — Prompt 09C is blocked pending independent acceptance of 09B)*. Canonical B-09 specification established.

## 38. Prompt 09B-C completion — Alliance Foundations Correction, Architectural Integrity, Autonomous Decision-Making, Owner-Authority Protection, Validator Hardening, and Project-Wide Reconciliation (2026-10-31)

**Mission:** Complete the targeted Prompt 09B-C correction and reconciliation pass across the Alliance specification and all Stage 2 master registers:
1. **Integration Contract Restoration (AX-01 through AX-26):** Restored all 26 contracts in `docs/stage-2/16_alliances_integration_contracts.md` (v2.0) to their exact canonical Prompt 09A definitions, resolving the contract shift defect. Complete 26-row reconciliation matrix provided with 20-field specifications. Preserved explicit traceability between `AX-08`, `REQ-141`, `REQ-142`, and `REQ-176`.
2. **Formula Notation & D-014 Audit (F-AL-001 through F-AL-005):** Cleaned all corrupted escape sequences and restored clean LaTeX notation in `docs/stage-2/16_alliances_formula_register.md` (v2.0). Audited and classified all five formulas under D-014 Category C Provisional defaults subject to calibration in Prompt 14.
3. **Open-Ended Constitution & Rulebook Hardening (B-09):** Updated `docs/stage-2/16_alliances.md` (v2.0) across all 178 rules (`ALL-001` through `ALL-178`). Eliminated all mandatory political models (no mandatory Leader office, no mandatory Heir, no mandatory council, no hardcoded 1–10 tiers, no 20-position cap, no mandatory 75% impeachment threshold, no 12-turn deadline, no mandatory 80% dissolution threshold). Implemented neutral role primitives with custom display titles, orthogonal permissions, and anti-escalation safeguards. Replaced mangled Section 27 with an authentic `UD-039` through `UD-049` reconciliation ledger. Preserved national sovereignty, no collective treaty object, and static Discord URL boundary (`discord.gg/`).
4. **Decision Register Alignment & Owner Protection:** Reconciled `D-135` through `D-139` in `docs/DECISIONS.md` and `DD-151` through `DD-160` in `docs/stage-2/04_approved_and_provisional_decisions.md` under D-014. Clarified that Category B autonomous decisions approve architecture and role primitives, while owner-reserved decisions (`UD-040` through `UD-049`) remain genuinely Open without false approval claims.
5. **Requirements Traceability Matrix Reconciliation:** Reconciled `docs/stage-2/03_requirements_traceability.md` (v1.22) restoring all 617 contiguous requirements (`REQ-001` through `REQ-617`), mapping the restored AX contracts for `REQ-534` through `REQ-617`, and verifying the canonical count (19 Approved / 590 Provisional / 5 Open / 3 Deferred / 0 Proposed = 617 total).
6. **Dedicated B-09 Semantic Validator & Fixture Suite:** Authored `docs/qa_backups/09B_validate_alliance_semantic.py` guarding against all 30 defect classes, accompanied by `docs/qa_backups/test_09B_alliance_semantic_validator.py` with 1 clean passing fixture and 30 negative defect fixtures.
7. **Full Regression Validation:** Executed complete test suite (`09_validate.py`, `validate_final.py`, `09A_validate_alliance.py`, `test_09A_alliance_validator.py`, `test_decision_registers.py`, `test_next_action.py`) with 100% pass rate.
8. **Next Action at that time:** Prompt 09B corrected and validated under Prompt 09B-C, ready for independent audit, with Prompt 09C as the next task *(superseded by Prompt 09B-E — 09C is blocked pending acceptance)*.

**Final Status:** **PASS** *(historical 09B-C entry; its 09C authorization is superseded by Prompt 09B-E — Prompt 09C is blocked pending independent acceptance of 09B)*. All defective patterns were addressed in that pass.

## 39. Prompt 09B-D completion — Authoritative Correction, Governance Recovery, and Semantic Validation (2026-11-01)

**Mission:** Complete the targeted Prompt 09B-D governance recovery, owner authority restoration, diplomatic non-delegation enforcement, treasury proposal classification, and project-wide reconciliation:
1. **Restoration of Owner Authority (UD-040 through UD-049):** In strict accordance with Autonomous Decision Policy D-014 and the authoritative unresolved design decisions register (`05_unresolved_design_decisions.md`), all explicit owner reservations `UD-040` through `UD-049` remain Open. Removed unauthorized Confirmed and Approved claims from `DECISIONS.md` (`D-136`..`D-139`), `docs/stage-2/04_approved_and_provisional_decisions.md` (`DD-153`..`DD-160`), and `docs/stage-2/16_alliances.md` (Section 27). Preserved owner-approved constitutional flexibility under `D-135` / `DD-151`.
2. **Restoration of B-08 and REQ-530 Diplomatic Authority:** Enforced absolute national diplomatic sovereignty. In strict adherence to B-08 (`DIP-015`, `DIP-148`, `D-126`) and `REQ-530`, the authenticated owner of the active nation is the sole diplomatic authority. Zero delegation of diplomatic authority to another player, an AI, an alliance office, or an alliance diplomatic representative exists. Completely removed `DELEGATE_DIPLOMACY` capability, purged all delegated foreign representative mechanisms, and rewrote `ALL-125`.
3. **Treasury & Formula Status Reconciliation (ALL-095..ALL-110, F-AL-001..F-AL-005):** Strictly separated approved Category A constraints (`REQ-176` non-minting value conservation) from candidate architecture and provisional parameters. Classified dedicated pool storage capacity (`F-AL-001`), founding fee (`F-AL-002`), 240-turn inactivity vacancy window (`F-AL-003`), 12-turn rejoin cooldown (`F-AL-004`), and multi-signature dual authorization thresholds (`F-AL-005`) as non-authoritative candidate proposals and provisional baselines awaiting explicit owner decisions under `UD-040`, `UD-043`, `UD-044`, and `UD-046` and Prompt 14 calibration. Removed false claims that 50,000 crowns or 10% multi-sig thresholds are approved or engine-enforced rules. **09B-E correction to this historical sentence:** REQ-176 is a Provisional requirement; the non-minting constraint is binding inherited, not an approved Category A constraint.
4. **Historical Decision Alignment:** Transparently reconciled `D-136` through `D-139` in `docs/DECISIONS.md` and `DD-153` through `DD-160` in `docs/stage-2/04_approved_and_provisional_decisions.md`. Re-titled entries to reflect candidate architecture and provisional recommendations under D-014 Category D/C, without silently altering historical decision IDs.
5. **Open-Ended Constitution & Role Primitives:** Removed fixed political rank requirements ("Rank 9 and Leader only") from `MANAGE_SUCCESSION`, `MANAGE_ROLES`, and `REMOVE_MEMBERS`. Defined the Primary Administrative Contact strictly as a technical communication endpoint for game engine notices, not a mandated political office.
6. **Cross-System Integration Contracts Hardening (AX-01 through AX-26):** Updated all 26 integration contracts in `docs/stage-2/16_alliances_integration_contracts.md` (v2.1) to reflect open owner decisions `UD-040` through `UD-049`, enforce zero diplomatic delegation under `AX-15` and `AX-16`, and preserve warehouse capacity isolation under `AX-08`.
7. **Semantic Validator Rebuild & Verification:** Rebuilt `docs/qa_backups/09B_validate_alliance_semantic.py` and `docs/qa_backups/test_09B_alliance_semantic_validator.py` covering all 14 defect classes from Project 30 audit, removing false requirement for 50,000 crowns / 10% thresholds, and enforcing project-wide status consistency. **09B-E correction to this historical sentence:** the 09B-D validator still required the `50,000` / `10%` thresholds; the requirement was actually removed in the 09B-E rebuild.
8. **Project-Wide Status Reconciled:** Updated all continuity files (`AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/stage-2/16_alliances.md`) to uniformly state: "Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance."
9. **Final Status:** **PASS** *(historical 09B-D entry; superseded by Prompt 09B-E, which reports correction complete and independent acceptance pending, not PASS)*. Full governance recovery and semantic validation were attempted in that pass.

## 40. Prompt 09B-E correction — Owner-Reserved Authority, Diplomatic Non-Delegation, Treasury Neutrality, AX Reconciliation, and Validator Rebuild (2026-11-01)

**Mission:** Correct every remaining defect identified by the independent Project 31 audit without inventing owner approval and without starting Prompt 09C:
1. **Owner-reserved leakage removed from B-09:** `ALL-054` now states that succession and stewardship are owner-reserved under `UD-043`; `ALL-100` and `ALL-111` explicitly say no treasury control is approved or enforced; `ALL-124` is a candidate position feature under `UD-047`; `ALL-166` presents the allowlist as an unapproved candidate under `UD-048`; `ALL-176` states that treasury ownership, capacity and withdrawal policy remain owner-reserved under `UD-046` and must not be described as settled.
2. **UD-040 through UD-049 remain Open:** The unresolved-decision register keeps all ten rows Open with `Yes — owner`; the B-09 Section 27 ledger shows `Resolved` only for `UD-012` (by B-09) and `UD-039` (by `D-137`). Current-state wording that implied Prompt 09B could close an owner decision was corrected; the closure authority is the owner.
3. **Diplomatic sovereignty enforced:** `ALL-125` and `D-137` retain the sole-authority rule for the authenticated owner of the active nation and prohibit delegation to another player, an AI, an alliance office, a representative, a leader or an administrator. Silence is never consent and an alliance majority never binds a sovereign nation. `REQ-530` remains Provisional and no `DELEGATE_DIPLOMACY` capability exists.
4. **AX-01 through AX-26 reconciled:** All 26 contracts retain the 21-field specification. `AX-08` keeps the boundary that national warehouse rules (`REQ-141`, `REQ-142`) do not establish alliance pool capacity, while ownership and capacity remain Open under `UD-046`. `AX-18` is deferred to Prompt 10, `AX-19` is Provisional under `UD-048`, `AX-20` is candidate under `UD-049`, and only `AX-26` carries approved Global Trade scope (`D-122`, `DD-136`, `REQ-513`).
5. **All 84 Alliance requirements audited:** `REQ-534` through `REQ-617` were checked row by row. Twelve owner-policy rows are Open (`REQ-548`, `REQ-549`, `REQ-556`, `REQ-573`, `REQ-574`, `REQ-575`, `REQ-579`, `REQ-580`, `REQ-586`, `REQ-598`, `REQ-599`, `REQ-600`); 71 are Provisional; `REQ-591` is Deferred to Prompt 10. `REQ-593` was corrected from an incorrect military-rule mapping (`ALL-136`–`ALL-141`) to the actual privacy rules (`ALL-086`, `ALL-156`, `AX-10`, `DD-031`). Totals are 19 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed = 617.
6. **Treasury and formula neutrality:** Entity ownership, dedicated capacity, member bonuses, overflow rejection, two-phase withdrawals, dual signatures and every threshold are documented only as candidate or provisional material under `UD-046`. `F-AL-001` through `F-AL-005` are unapproved candidates. `REQ-176` is a binding inherited constraint under a Provisional requirement, not an approved Category A rule.
7. **Constitution neutrality:** No mandatory Leader, Heir, council, office template, rank tier, government model, succession rule or amendment procedure is imposed. Ballots and treasury controls are labelled candidate; optional templates remain editable illustration only.
8. **Historical decisions corrected transparently:** `D-135`, `D-136`, `D-137`, `D-138` and `D-139` and `DD-153` through `DD-160` retain their IDs and history. Overclaims such as `Approved Category A`, `Approved (exit sovereignty)` and `Approved (D-028 dormancy lattice)` were replaced with `binding inherited`, `Confirmed` or `Candidate` labels. `D-135` and `DD-151` remain the owner-approved open-ended-constitution principle.
9. **Semantic validator rebuilt:** `09B_validate_alliance_semantic.py` now checks AX inventory and field completeness, AX status-to-UD mapping, `UD-039` reconciliation, `UD-040`–`UD-049` owner reservation, B-09 sensitive-rule leakage, diplomatic delegation, treasury approval leakage, formula candidate status, mandatory hierarchy, requirement counts and deep traceability, decision-register consistency, continuity status and premature Prompt 09C work. The previous false requirement for `50,000` and `10%` was removed; a clean project with `UD-046` Open passes without those values.
10. **Project-wide status reconciled:** All continuity files state the exact status required for this phase: **Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance.**
11. **Register tallies and continuity ranges corrected:** The Stage 2 decision register §3 heading now reads `DD-001…DD-160`; §6 tallies were recomputed from the rows (125 Approved / 26 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred = 160) and the project-decision paragraph now names 139 decisions including D-135…D-139. `AI_CONTEXT.md` carries the same DD breakdown. The roadmap, progress log, outline and handoff statements now name §40 / Prompt 09B-E rather than stopping at §39 / 09B-D.
12. **Historical delegation invitations superseded transparently:** `D-132`, `DD-140`, `DD-146`, B-08 `DIP-148` and B-08 `DIP-015` are annotated that `D-137` adopts zero diplomatic delegation and no alliance treaty object. No historical row was deleted or renumbered, and no new approval was created.
13. **D-135 clarification:** The owner-approved open-ended-constitution principle is unchanged; a 09B-E note records that its infrastructure list is capability-neutral and approves neither ballots (`UD-042`) nor any treasury pool, ownership, capacity or withdrawal mechanism (`UD-046`).
14. **Cross-system reference repair:** `D-106` cited a non-existent `D-204`; the reference now points to `DMP-204`, the rule actually intended. This is the only D-2xx reference in the decision log.
15. **Version and field-count wording corrected:** B-09 now says 21-field contracts (20 specification fields plus the `AX` identifier), matching the ledger; the formula register reconciliation notice and B-09 contract note now name Prompt 09B-E rather than 09B-D. Historical §37–§39 entries keep their original text with supersession notes.
16. **Progress and decision headers updated:** `DECISIONS.md` names the 09B-E correction and the D-135/D-132 annotations; the Stage 2 decision register v3.4 note records the tally correction and DD-140/DD-146 annotations.
17. **Phantom turn-rule references removed:** B-09 and the integration contracts cited `TRN-020` and `TRN-037`, but no `TRN-` identifier space exists. The citations now point to B-02 `TR-024` (slot arithmetic), `TR-029` (boundary assignment) and `TR-060` (resolution validation), and the contracts' cross-system prefix list names `TR-` instead of `TRN-`. No rule in B-02 or B-09 changed meaning.
18. **Ancillary validators, tests and outline counts reconciled to the 09B-E state:** the 09A validator's group 13 now requires the exact 09B/09C status and rejects a contradictory "09C/09D is next" claim (910 checks; 43 tests OK); the Stage 2 validator's row-09 assertion and `validate_final.py` now expect pending acceptance and the `26 Resolved / 5 Deferred / 18 Open` register counts; `test_decision_registers.py` and `test_next_action.py` expect 26/5/18, one pending-acceptance row and no "next task"; `verify_politics_numbers.py`'s guard expects the same status (879/879 checks). The outline's "Sections drafted" row now counts B-09 (10 drafted) and the gameplay-rule derivation includes `16_alliances`. `PROJECT_PROGRESS.md`, the Stage 2 handoff, both roadmaps and the progress log's row 09 now state pending acceptance and cite §37–§40; DD-150 and the 09A research baseline carry dated snapshot notes that the 84 rows are now 71 Provisional / 12 Open / 1 Deferred. No historical row, decision or rule was deleted or renumbered.
19. **Seventeen-area research evaluation recorded:** B-09 §28.1 now records, for founding, membership, identity, member status, governance, leadership, permissions, treasury, diplomacy, collective discussion, announcements, inactivity, security, dissolution, integrations, UX and scalability, what 09A established, what gap remained, how 09B treated it, the authority label, and the affected `ALL`/`REQ`/`AX` identifiers and validator check groups. The ledger adds no rule, approval or mandatory feature; areas with insufficient evidence remain candidate or owner-reserved.

**Final Status:** **Correction complete; independent acceptance review pending.** No PASS claim is made and Prompt 09C has not started. No production code, migration, deployment or gameplay implementation was created.

## 41. Prompt 09B-F correction — Final Authority Audit, Semantic Validation, and Project-Wide Consistency (2026-11-01)

**Mission:** Complete the final correction pass authorized for Prompt 09B-F: correct `ALL-057` and `REQ-551`, audit every indirect route to the owner-reserved decisions `UD-040`–`UD-049`, strengthen the semantic validator with isolated negative tests A–F, complete the Project-Wide Consistency and Preservation Audit for Prompts 01–09A, and leave Prompt 09C blocked.

1. **`ALL-057` corrected:** The rule is retitled "Competing Succession Claims — Audit Evidence Only". The platform records each claim, actor, turn and timestamp as immutable audit evidence; timestamp order, transaction order and workflow completion are evidence only and do not decide which claim prevails, recognise a successor or steward, assign or transfer any office or establish political authority. Any resolution rule remains owner-reserved under `UD-043` and is not in force. Technical auditability is preserved; political adjudication is removed.
2. **`REQ-551` corrected:** Dispute and disciplinary records are retained and the game never adjudicates the merits or grants authority over another player's nation. No appeal or dispute-resolution mechanism is required or approved while `UD-044` is Open; any future declared path and recorded decision are conditional on explicit owner approval.
3. **Related leakage corrected:** `REQ-013` (no platform succession model), `REQ-568` (no expulsion mechanism while `UD-044` is Open), `REQ-569` (no rejoin cooldown or blacklist in force), `ALL-055`, `ALL-079`, `ALL-130`, `ALL-133`, `ALL-142`, `ALL-143`, `ALL-145`, `ALL-150` and `ALL-158` were re-read and corrected where needed. `AX-03`, `AX-04` and `AX-09` now say no office, authority or seat transfers automatically and no candidate lifecycle rule is enforced while `UD-043`/`UD-044` are Open. `F-AL-003` states that no declaration or consequence is in force.
4. **Other systems corrected only where the authoritative source required it:** B-02 `TR-021` is conditional on candidate native ballots under `UD-042`/`UD-049`; the B-03 reroll row treats succession/vacancy as candidate under `UD-043`; B-04 `ECN-152` no longer calls alliance dues approved; B-08's header now records that 08C is complete at v1.3; the Prompt 09 roadmap paragraph now records the `D-137` resolution instead of the superseded instruction to choose a treaty model. No approved rule, value, permission or owner-reserved status was changed.
5. **Project-wide audit completed:** [`16_alliances_project_wide_consistency_audit.md`](16_alliances_project_wide_consistency_audit.md) records the eight required fields for accounts/auth, nation creation/ownership, permissions/authority, economy/treasury, domestic politics, diplomacy, warfare, Global Trade, progression, security/audit, UI/UX, technical architecture/data ownership and the registers/formulas/gates. It also reconciles all 26 `AX` contracts and records the accepted work preserved, corrections made, decisions unchanged, unresolved owner decisions and limitations.
6. **Validator strengthened:** `09B_validate_alliance_semantic.py` now runs 26 checks. `C24` fails a document that treats timestamp, transaction or workflow order as deciding a succession claim under open `UD-043`; `C25` fails a mandatory alliance/member appeal, expulsion or rejoin policy under open `UD-044` while excluding legitimate platform moderation; `C26` checks each `UD-040`–`UD-049` reservation and its settled-language guards. The validator still accepts labelled candidates, negations and platform audit records.
7. **Negative and clean fixtures added:** The test suite now has 79 tests, including fixture A (timestamp succession rule), fixture B (mandatory appeal), fixture C (contract assigns succession authority by timestamp), fixture D (appeal removed from `REQ-551` but relocated to a contract), fixture E (unauthorized policy for each of `UD-040`, `UD-041`, `UD-042`, `UD-045`, `UD-046`, `UD-047`, `UD-048`, `UD-049`) and fixture F (clean canonical project passes). Tests copy `docs/` into temporary directories and never modify the real documents.
8. **Registers and continuity synchronized:** B-09, the contracts and the formula register are v2.3 / Prompt 09B-F; the requirements register is v1.24; the decision register is v3.5; the unresolved-decision register is v1.19. Counts are unchanged: 617 requirements = 19 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed; 84 Alliance requirements = 71 Provisional / 12 Open / 1 Deferred; 49 `UD` rows = 26 Resolved / 5 Deferred / 18 Open; 160 `DD` rows = 125 Approved / 26 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred. `D-122`, `DD-136`, `REQ-513` and `G-1`–`G-6` remain intact.
9. **Regression executed:** The corrected 09B validator, the full 09B test suite, the 09A validator and tests, the Stage 2 validator, the decision-register tests, the next-action tests and the politics, market, diplomacy, economy and integration checks were run. Exact commands, exit codes, pass/fail counts, warnings and skips are reported in the Prompt 09B-F completion report; no test result is asserted from memory.
10. **Final Status:** **Correction complete; independent acceptance review pending.** No PASS claim is made. Prompt 09C has not started and remains blocked pending independent acceptance. No production code, migration, deployment, UI or gameplay implementation was created.

## 42. Prompt 09B-G — semantic validator hardening, adversarial regression and false-negative closure (2026-11-01)

**Mission:** Close the two validator false negatives demonstrated in independent review (`C24` and `C25` skipped a whole sentence when any negation or conditional appeared), add the exact compound sentences as permanent isolated fixtures G and H, add positive controls for legitimate prohibitions, audit-only wording and labelled proposals, re-check the `UD-040`–`UD-049` boundary and re-run the full regression. No canonical rule, requirement, contract, formula or decision was changed.

1. **Root cause confirmed:** `C24` and `C25` evaluated whole sentences and skipped any sentence containing a `NEGATION` or `CONDITIONAL` token. A disclaimer in the first clause therefore immunised a mandatory policy in the second. This was a validator defect; `ALL-057` and `REQ-551` themselves remained correctly worded from 09B-F.
2. **Validator corrected:** `CLAUSE_SPLIT`/`clauses()` split contrastive and coordinated compounds (`but`, `however`, `yet`, `nevertheless`, `nonetheless`, `whereas`, `although`, `though`, `and`); each clause is evaluated independently and only the clause containing the negation/conditional is skipped. `order_re` gained `earliest claimant`, earlier recorded timestamp/claimant and time-of-record variants. Diagnostics now name the source label, the nearest rule/requirement id (`ALL-057`, `REQ-551`, …), the owner-reserved decision and the offending clause.
3. **Fixture G (succession):** injecting "Timestamp ordering is not sufficient by itself, but the earliest claimant must become the successor." into `ALL-057` now fails `C24` with `[C24] B-09 ALL-057 imposes an unauthorized succession outcome under owner-reserved UD-043: the earliest claimant must become the successor.`
4. **Fixture H (appeal):** injecting "Appeals are generally not required, but members must have the right to appeal every expulsion." into `REQ-551` now fails `C25` with `[C25] requirements REQ-551 mandates an alliance appeal or dispute procedure under owner-reserved UD-044: members must have the right to appeal every expulsion.` and the corresponding expulsion rule diagnostic.
5. **Positive controls added:** direct prohibition; audit-only timestamp; labelled succession proposal; no approved appeal; conditional non-enforced appeal proposal; neutral recordkeeping/evidence retention; approved audit reference. All seven pass without a `C24`/`C25` failure, so the fix does not reject every mention of succession or appeals, does not treat every conditional as approved and does not rely on one keyword.
6. **Owner-reserved audit re-run:** `UD-040`–`UD-049` remain `Open` / `Yes — owner`; the B-09 ledger remains Open; the 84 Alliance requirements remain 71 Provisional / 12 Open / 1 Deferred / 0 Approved; `REQ-551` retains its no-approval anchors; `UD-039` remains resolved by `D-137`; `D-135`/`DD-151`, `B-08`/`REQ-530`, the treasury/formula corrections, the Discord/communications boundary, the 26 `AX` contracts and the 09A research are unchanged.
7. **Preservation:** no canonical document was modified by a test; every fixture copies `docs/` into a temporary directory. The [09B-F project-wide audit](16_alliances_project_wide_consistency_audit.md) is preserved and amended in §7.3 and §10 to record the false negatives, the clause-level fix, fixtures G/H and the positive controls.
8. **Regression executed:** the canonical 09B validator (26/26, exit 0), the full 09B suite (**88 tests, OK, 376.954 s, exit 0**), the 09A validator/tests (910 checks / 43 tests), the Stage 2 validator (358/358), `validate_final.py` and its self-test (10/10), the decision-register tests (12), the next-action tests (23), and the politics (879/879), market (95/95), market-workflow (14/14), diplomacy numbers (9 groups, 0 failed), diplomacy workflows (17 groups, 0 failed), economy (164/164) and city (267/267) checks. Exact commands, exit codes, counts, skips and warnings are in the Prompt 09B-G completion report; no result is asserted from memory. No test was skipped and no warning was reported.
9. **Final Status:** **Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance.** No PASS or independent-acceptance claim is made. Prompt 09C has not started. No production code, migration, deployment, UI or gameplay implementation was created.

## 43. Prompt 09B-H — negative-polarity entitlement detection, validator correction and acceptance readiness (2026-11-01)

**Mission:** Close the remaining `C25` false negative in which a negation token exempted a whole clause, so an appeal entitlement asserted through negative wording passed while `UD-044` is Open. Apply the same analysis to `C24`/`UD-043`, add permanent fixtures I–M and six positive controls, preserve every valid 09B-A–09B-G artefact and re-run the full regression. No canonical rule, requirement, contract, formula or decision was changed.

1. **Root cause confirmed:** `C25` skipped any clause containing a `NEGATION` or `CONDITIONAL` token. Negative wording can itself establish an entitlement or a prohibition, so the policy asserted by the clause has to be classified before any exemption. This was a validator defect; `ALL-057` and `REQ-551` remained correctly worded from 09B-F.
2. **Validator corrected:** policy classification now runs before the negation/conditional exemption. `C25` distinguishes neutral status, recordkeeping and proposal wording from deprivation/denial protection, an appeal made a condition of expulsion, a prohibition on appeals and a positive appeal grant. `C24` distinguishes neutral claim recording and audit evidence from claimant-protection entitlement. `nearest_id()` now prefers a rule or requirement id inside the clause, and diagnostics name the source label, the rule/requirement id, the owner-reserved decision and the offending clause.
3. **Fixtures I–M added (permanent):** I `Alliance members cannot be expelled without a right to appeal.`; J `Members must not be deprived of a right to appeal an expulsion.`; K `No member may be expelled unless an appeal opportunity is provided.`; L `No expelled member may appeal the expulsion.`; M `Every expelled member must be allowed to challenge the expulsion through an appeal.` Each fails `C25` with `UD-044` and the `ALL-079` source; the reasons are respectively condition-of-expulsion, deprivation, condition-of-expulsion, denial and grant.
4. **Positive controls added:** six new cases (must-not-create-or-deny appeal rights; no approved or required appeal mechanism; storing evidence without deciding appeal rights; a future proposal not currently enforced; recordkeeping not an appeal entitlement; an expulsion record that does not establish an appeal mechanism) all pass. The seven 09B-G positives and fixtures G/H remain green, so the correction does not reject legitimate prohibitions, audit wording or labelled proposals.
5. **`C24`/`UD-043` checked for the same weakness:** claimant-cannot-be-bypassed, successor-cannot-be-denied and claimant-cannot-be-displaced fail `C24` with `UD-043` and the `ALL-057` source; neutral claim recording passes; genuine prohibitions, audit-only timestamps and labelled proposals remain accepted.
6. **Preservation verified:** every fixture copies `docs/` into a temporary directory and no canonical document was modified by a test. `ALL-057` and `REQ-551` are intact; `UD-040`–`UD-049` remain `Open` / `Yes — owner`; the B-09 §27 ledger remains Open; the 84 Alliance requirements remain 71 Provisional / 12 Open / 1 Deferred / 0 Approved; the 26 `AX` contracts, `D-135`/`DD-151`, `B-08`/`REQ-530`, `D-137`, the treasury/formula corrections, the Discord/communications boundary and the 09A research are unchanged. The [09B-F project-wide audit](16_alliances_project_wide_consistency_audit.md) is preserved unchanged: the correction found no new inconsistency in the canonical corpus.
7. **Regression executed:** canonical 09B validator **26/26, exit 0**; full 09B suite **103 tests, OK, 473.372 s, exit 0** (no skips, no warnings); targeted 09B-H fixtures **17 tests, OK, 75.861 s** and G/H/I–M **7 tests, OK, 52.240 s**; 09A validator **910 checks**; 09A tests **43, OK, 28.459 s**; Stage 2 validator **358/358**; `validate_final.py` all checks passed; self-test **10/10**; decision-register tests **12, OK**; next-action tests **23, OK**; politics **879/879**; market **95/95**; 07C workflows **14/14**; diplomacy numbers **9 groups, 0 failed**; diplomacy workflows **17 groups, 0 failed**; economy **164/164**; cities **267/267**. Exact commands and exit codes are in the Prompt 09B-H completion report; no timeout or skipped test is reported as a pass.
8. **Final Status:** **Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance.** No PASS or independent-acceptance claim is made. Prompt 09C has not started. No production code, migration, deployment, UI or gameplay implementation was created.

## 44. Prompt 09B-I correction — C25 semantic hardening, Alliance taxation, donations, treaties, NAP and same-Alliance attack ban (2026-11-01)

**Historical record — superseded in part by §45 (Prompt 09B-J).** Items 3, 6 and 7 below describe the 09B-I owner-consent tax model, the P4 collection timing and the NAP membership treatment as written on that date; §45 replaces the tax model with automatic per-turn production withholding, corrects the NAP rule so a non-consenting nation joins as a non-covered member, and extends the tests. The rest of §44 remains the record of what 09B-I changed.

**Mission:** Close the remaining `C25` appeal-policy false negative for sentences N/O/P, then implement the five owner-requested Alliance changes without resolving any unlisted owner-reserved question: player-defined member taxation with explicit owner consent, voluntary donations, withdrawal of the `ALL-093` confiscation clause, a separate Alliance-to-Alliance treaty object with NAP consent and enforcement, and the mandatory server-side same-Alliance attack ban. No earlier rule, decision or requirement is renumbered.

1. **`C25` root cause corrected:** The prior check classified a clause from its main verb only. It treated a prohibition on denying an appeal (`must not deny appeal rights`) as neutral, and it ignored entitlements introduced by `except that` or `unless` branches after an otherwise neutral create-or-deny clause. `C25` now evaluates the complete policy assertion: main clause, exception, unless/except and subordinate branches, polarity, and whether the sentence grants, denies, conditions or merely records an appeal outcome. Statements that decide whether an appeal right exists fail while `UD-044` is Open; accurately labelled non-enforced proposals and neutral recordkeeping still pass.
2. **Permanent N/O/P fixtures:** N `The platform must not deny appeal rights to any expelled member.` (denial protection), O `The platform must not create or deny appeal rights except that expelled members shall retain a right to appeal.` (except-branch entitlement) and P `The platform must not create or deny appeal rights unless every expelled member has a right to appeal.` (unless-branch entitlement) each fail `C25` with `UD-044` and the `ALL-079` source. Positive controls 106–108 keep a bare create-rights holding, a coordinated create-or-deny reservation and technical recordkeeping valid. Fixtures G–M and `C24` are unchanged and still pass.
3. **Member taxation authorized, not parameterized:** B-09 §29.1 adds `ALL-179`–`ALL-187` and `REQ-618`–`REQ-625`. A tax requires an active player-authored policy and the explicit authenticated consent of each affected nation owner to the exact version; silence, dormancy, majority, ballot, office, AI and platform are never consent. Policy terms are player-defined across percentage of gross tax income, fixed crowns or a fixed resource quantity, temporary or recurring, with no default rate, frequency, base or fallback. Collection is atomic in the P4 transfer phase, never partial, never silent, never creates debt or confiscation, records paired ledger events and fails closed with notice. `F-AL-006` states the integer arithmetic only; `UD-046` still owns treasury ownership, capacity, withdrawal and dual approval.
4. **Voluntary donations authorized and separated from tax:** B-09 §29.2 adds `ALL-188`–`ALL-195` and `REQ-626`–`REQ-632`. A donation is one-time, personally initiated and authenticated by the donor owner, irrevocable after settlement and conserved through the canonical `ECN-212`/`TR-060` transfer. It uses an idempotency key, produces an immutable receipt and audit record, cannot be a relabelled compulsory deduction, creates no cap, fee or frequency by default, cannot bypass market gates, and confers no treasury withdrawal authority. `F-AL-007` states conservation and idempotency only; no limit or fee is invented.
5. **`ALL-093` withdrawn without deleting its neighbors:** `ALL-093` is now an ID-preserving tombstone withdrawn by `D-140` at the owner's direction. It grants no right, protection, authority or confiscation power and points to the independent protections in `ALL-087`, `ALL-142` and `ALL-145`. Authentication, authorization, server-side validation, audit logging and transaction integrity remain in force; no arbitrary confiscation capability was created.
6. **Nation treaty system inspected before design:** B-08 remains the nation-level treaty authority (`DIP-037`, `DP-T01` NAP, `DIP-039`, `DIP-147`, `DIP-150`). No Alliance treaty object existed. `D-140` therefore amends only the no-object component of `D-137` and creates a separate B-09 object identified by `alliance_agreement_id` with its own `AT-T01`–`AT-T05` catalogue, lifecycle, consent record and audit. B-08 objects are not reused, copied or mutated; zero diplomatic delegation and national diplomatic sovereignty remain binding.
7. **Treaties, NAP consent and pact effects:** B-09 §29.3 adds `ALL-196`–`ALL-208` and `REQ-633`–`REQ-644`. Every affected nation owner must explicitly consent per version; silence, inactivity, default membership, inference, constitution clause, ballot, office and majority are never consent, and no alliance actor consents for a nation. An active `AT-T01` NAP prohibits every attack method between covered members of the two alliances, is enforced by a server-side validator before execution, returns a clear reason and writes an audit event where required; no leader, officer, ballot, majority, AI, administrator or player may waive it while active. Membership change, expiry, termination, breach and multi-Alliance coverage are defined without silent extension. `AT-T02`–`AT-T05` create only their declared effects; mutual defence creates no automatic war entry or deployment, and no pact creates a collective diplomatic position or delegation.
8. **Same-Alliance attack ban:** B-09 §29.4 adds `ALL-209`–`ALL-215` and `REQ-645`–`REQ-647`. Two nations sharing at least one active alliance must not attack each other, independent of constitution, treaty, office, majority or preference. Every attack path must call one canonical server-side validator at submission and again at execution or settlement; UI hiding and client checks are not enforcement. The validator reads current membership, fails closed with no cost or damage on a block, and covers join, leave, transfer, expulsion (only if approved), dissolution, rejoin and multi-membership. Prompt 10 runtime enforcement is a binding contract, not an implemented feature.
9. **Registers and integration synchronized:** B-09 is v2.4 with 29 sections, `ALL-001`–`ALL-219`, `F-AL-001`–`F-AL-007`, `AX-01`–`AX-30`, `ALF-01`–`ALF-26`, `REQ-534`–`REQ-647`, `D-135`–`D-140` and `DD-151`–`DD-163`. The requirements register is v1.25 with 647 rows (49 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed) and 114 Alliance rows (30 Approved / 71 Provisional / 12 Open / 1 Deferred). The decision register is v3.6 with 163 `DD` rows, 128 Approved; `DECISIONS.md` carries 140 decisions including `D-140`; the unresolved register remains 26 Resolved / 5 Deferred / 18 Open. `AX-27`–`AX-30`, `F-AL-006`/`F-AL-007`, `ECN-213a`, `DIP-039`/`DIP-147`, `UD-039`/`UD-046`/`UD-047` notes, the project-wide audit and the roadmap/handoff files record the same state. `D-122`, `DD-136`, `REQ-513`, `G-1`–`G-6`, `D-135`/`DD-151` and `B-08`/`REQ-530` are preserved.
10. **Validator and tests extended:** `09B_validate_alliance_semantic.py` now runs 31 checks. `C27`–`C31` verify consented non-default taxation, voluntary non-withdrawable donations, the `ALL-093` tombstone and independent security anchors, the separate treaty object with NAP consent and server-side enforcement, and the mandatory same-Alliance ban. The suite is now **142 tests**: focused negative fixtures for each guard, status regressions for `REQ-618`, `REQ-626`, `REQ-633` and `REQ-645`, ten structural tests (`test_132`–`test_141`) that remove a tax recurrence term, a donor asset-selection term, a donor/receiver confirmation term, an insufficient-value rule, a NAP player explanation, a treaty-approval term, two attack-trigger/validator terms, the `ALL-212` membership-change enumeration and the `ALL-199` mandatory-consent wording, and positive controls that keep neutral security, audit, treaty and attack wording valid. `C30` and `C31` additionally inspect the `ALL-199` and `ALL-212` rule text directly, so an incidental occurrence elsewhere in the section cannot mask a removed consent or membership term. Every fixture operates on a temporary copy of `docs/`.
11. **Final Status:** **Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance.** No PASS or independent-acceptance claim is made. No production code, migration, deployment, UI or gameplay runtime was created; Prompt 10 attack enforcement and Prompt 14 calibration remain unimplemented. The executed regression results are recorded in the Prompt 09B-I completion report; no result is asserted from memory.

## 45. Prompt 09B-J correction — Politics & War per-turn taxation, treaty/NAP consistency and C25 semantic completion (2026-11-01)

**Mission:** Correct the independent audit findings without restarting the Alliance work: replace the 09B-I per-policy consent interpretation with the owner-clarified automatic per-turn production tax, align formulas, contracts, economy and decision registers, correct non-covered NAP membership, make blocked-attack auditing mandatory, and close the five plain-language appeal escapes in `C25`. No rule, requirement, formula, decision or test identifier is renumbered, and no owner-reserved decision is closed.

1. **Tax model corrected:** B-09 §29.1 now specifies an automatic tax on each active member nation's current-turn production at the frozen turn snapshot. The base is gross P3.1 Crowns income and gross P3.3/P3.5 resource output; opening balances, existing stockpiles, earlier-turn output, donations, gifts, aid, market receipts and other non-production inflows are excluded. Collection is source withholding inside the national production settlement, not a P4 invoice.
2. **Rates and brackets:** `ALL-181` defines player-created named brackets with a separate Crowns rate and a separate rate for every taxable resource. Rates are integer basis points from 0 through 10,000 inclusive (0%–100%, 0.01 percentage-point precision), any integer is valid, and 10%, 20%, 30%, 37%, 55%, 73% and 100% are all permitted. There is no engine bracket, default rate or 10-point restriction; `ALL-182` makes the unassigned-member fallback an explicit, visible and recorded 0%.
3. **Role governance and turn cutoff:** `ALL-183` separates nine tax permissions and attaches them to player-defined roles, never to a mandatory Leader, Treasurer, President or hierarchy. `ALL-184` freezes membership, bracket, version and rates at one cutoff: a change before the freeze applies that turn, a change after the freeze applies next turn, and completed turns are never recomputed. No member nation owner approves each policy version; taxation is an internal Alliance economic rule, not B-08 diplomacy.
4. **Collection, receipts and `UD-046`:** `ALL-185` fixes `tax = floor(gross × rate_bp / 10,000)` per asset, with `0 ≤ tax ≤ gross`, atomic paired ledger postings and a deterministic idempotency key. `ALL-186` records the per-turn member statement, versioned edits and historical receipts. `ALL-187` makes the Alliance Receiving Ledger a credit-only accounting boundary that assumes no capacity and may never reject, destroy or lose generated tax. Treasury ownership, custody, capacity, withdrawal, spending, distribution and dual approval remain `Open` under `UD-046`; `UD-047`, `UD-044` and every other owner-reserved row are unchanged.
5. **Formulas and economy synchronized:** `F-AL-006` now models the per-asset source-withholding formula, the frozen snapshot, the 0% fallback, the rate sweep and the current-turn-only exclusions; `F-AL-007` models the separate voluntary donation with no destination-capacity term. B-04 v1.5 `ECN-213a` specifies the same six-step settlement sequence and names the P3.1, P3.3 and P3.5 withholding points without changing the national production order. `AX-27` and `AX-28` were rewritten to the same contracts.
6. **Donations preserved and separated:** `ALL-188`–`ALL-195`, `AX-28`, `F-AL-007` and `REQ-626`–`REQ-632` remain the voluntary donation model. A donation is initiated and confirmed by the donor, is never mandatory or automatic, is never taxed as new production, carries no capacity assumption and confers no withdrawal or ownership authority.
7. **Treaty and NAP consistency:** B-08 remains the national treaty authority and its objects are never reused. B-09's separate `alliance_agreement_id` object is unchanged in identity. `ALL-204` and `REQ-641` now require a nation whose owner declines NAP coverage to be admitted or retained as a **non-covered member**, with no refusal, removal, cooldown, fine, punishment or ineligibility; coverage is only the recorded consenting set, new members are never added automatically, and membership changes update coverage deterministically. Dissolution of either party terminates the bilateral treaty as a whole. `ALL-197` states that custom prose is descriptive and only structured `AT-T01`–`AT-T05` effects execute.
8. **Attack restriction and audit:** Same-Alliance and active-NAP checks remain independent and cumulative so leaving one Alliance cannot bypass a NAP. `ALL-210`–`ALL-212` and `AX-30` require every attack method, API, handler and service route to call the same server-side validator at submission and execution, and `ALL-214`/`REQ-642` require a mandatory blocked-attempt audit event independent of optional audit settings. UI hiding remains non-enforcement; Prompt 10 runtime work has not started.
9. **`C25` root cause and regression fixtures:** The five audit escapes (`Members may appeal an expulsion.`, `An expelled member can appeal the expulsion decision.`, `Every expelled member may appeal.`, `An appeal may be lodged within the review window.`, `The expelled member has access to an appeal process.`) all use permissive modals or procedural access rather than `must`/`shall`. `C25` now classifies plain modal grants, passive lodging and access-to-procedure wording; it evaluates each clause and exception branch instead of skipping a whole clause on any negation or conditional marker; and a neutral holding exempts only the branch it actually governs. Tests 142–157 add the five permanent fixtures plus denial, conditional, negation-in-clause, compound, exception, subordinate and positive controls; fixtures G–P, `C24` and the earlier positive controls remain.
10. **Regression executed:** full 09B semantic suite **Ran 177 tests in 1194.447 s; OK; exit 0**; canonical 09B validator **31/31, exit 0**; `verify_alliance_numbers.py` **217/0, exit 0**, self-test **22/22**; 09A validator **911 checks**; 09A tests **43, OK, 31.351 s**; Stage 2 validator **358/358**; `validate_final.py` all checks passed; self-test **10/10**; decision-register tests **12, OK, 0.041 s**; next-action tests **23, OK, 0.121 s**; politics **879/879**; market arithmetic all passed; 07C workflows all passed; diplomacy numbers **9 groups, 0 failed**; diplomacy workflows **17 groups, 0 failed**; economy **164/164**; cities **267/267**. No timeout or skipped test is reported as a pass.
11. **Final Status:** **Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance.** No production code, migration, deployment, UI or gameplay runtime exists. The executed regression results above are the actual run outcomes; no result is asserted from memory.


## 46. Prompt 09B-K correction — final C25 semantics, failure-code cleanup, multiple-membership safeguard and production-chain accounting (2026-11-02)

**Mission:** Complete the final targeted correction to Prompt 09B-J without restarting or regenerating the Alliance specification: close the five remaining positive appeal-grant escapes in `C25`, rewrite `ALF-21`/`ALF-23`/`ALF-24` to the production-tax and receipt model, name the Alliance Receiving Ledger in `REQ-626`, add the provisional `UD-040` multiple-membership tax safeguard, fix the production-chain accounting rule, and re-run every affected validator and test while preserving all earlier identifiers, decisions and owner reservations.

1. **`C25` root cause corrected:** The five audit statements (`Every expelled member receives an opportunity to appeal.`, `The member's right to appeal is established.`, `Expelled members are afforded an appeal.`, `Appeals are available to expelled members.`, `An expelled member may file an appeal.`) assert a positive appeal entitlement through a benefit verb, an establishment predicate, a passive availability predicate or a permissive modal rather than through `must`/`shall`. `C25` now separates positive grant families (receipt/benefit, establishment/existence, availability/access, opportunity/ability, bare-verb provision, bare permissive modal) from denial and restriction families, evaluates main and subordinate clauses independently, and preserves historical, explanatory, disclaimer, reserved, illustrative, fixture and rejected-proposal text through an explicit non-policy-context check. A neutral holding exempts only the residual text it actually governs; it no longer returns the whole sentence safe, and the earlier whole-clause negation/conditional skip is removed.
2. **Permanent `C25` fixtures:** Tests 177–198 add separate fixtures for the five statements plus `Every member is permitted to appeal.`, `The platform guarantees an appeal opportunity.`, `An appeal right exists for expelled members.`, `Expelled members have access to an appeal procedure.`, `No appeal is available to an expelled member.` and `The platform must not grant any appeal right.`; disclaimer→entitlement, entitlement→disclaimer, subordinate entitlement, compound entitlement, historical mention, rejected proposal, illustrative fixture, negated historical framing, `only` restriction and create-or-deny controls. Each fixture asserts the exact validator result; the earlier C25 fixtures and `C24` remain green.
3. **`ALF-21` corrected:** The failure is now a rejected bracket, rate or assignment change because the authenticated actor lacks the required active alliance permission or the change fails authorization or version validation; no collection occurred. It no longer requires per-policy national-owner consent and does not weaken authenticated role authorization.
4. **`ALF-23` corrected:** The failure is now a missing, incomplete or inconsistent authoritative current-turn production record or frozen turn snapshot, or a failed paired ledger commit; no existing stockpile or balance is charged, no partial collection exists and a retry cannot create a second charge. The stale insufficient-unreserved-value meaning was removed; this is not a stockpile tax and cannot draw one.
5. **`ALF-24` corrected:** A donation is rejected for an unsupported or invalid asset, insufficient donor unreserved value, missing/failed/stale authorization or confirmation, a conflicting duplicate settlement, or an atomic Alliance Receiving Ledger credit failure; an exact replay returns the original receipt and no destination-capacity limit exists. No capacity model is assumed or required.
6. **`REQ-626` and ARL terminology:** `REQ-626` now names the credit-only **Alliance Receiving Ledger** instead of an "alliance treasury". Tax and donation destinations are consistently the ARL; the ARL remains a credit-only receipt record and no ownership, custody, capacity, withdrawal, spending, distribution or dual-approval rule is created. `UD-046` remains Open.
7. **Multiple-membership safeguard:** `ALL-179`, `ALL-185`, `ALL-186`, `F-AL-006`, `AX-27` and `ECN-213a` now state that one eligible production event is deducted at most once, the same asset never loses more than 100% of gross, multiple membership never authorizes multiple deductions and no Alliance receives priority. When attribution is ambiguous, the provisional behaviour is an explicit, visible and recorded 0% Alliance-tax fallback for the affected asset and turn: gross is credited in full and is not delayed, reduced or destroyed, no Alliance is credited, the member and authorized roles can see the reason, normal collection resumes at the first later unambiguous turn, and a safeguarded turn is not retroactively re-taxed. The safeguard is reversible and does not resolve `UD-040`; no single-Alliance assumption is made.
8. **Production-chain accounting:** `ALL-180`, `ALL-185`, `F-AL-006`, `AX-27` and `ECN-213a` now tax at the eligible production event; later same-turn P3 stages consume only the post-tax net; a 100% rate leaves zero for later same-turn consumption; existing stockpiles consumed later are not taxed; a processing input is not taxed again; and a newly generated different output is taxed once at its own rate. The seven-step sequence is snapshot, authoritative gross, per-asset rate/attribution, one ARL credit, net national available, later stages consume post-tax only, and atomic paired events/receipt/audit. No parallel economy calculation is created; the existing B-04 production figures are used.
9. **Examples and tests added:** `F-AL-006` carries production-chain examples A–G (0%, 50%, 100%, a production chain with 107 total tax, an existing stockpile, transformed output and retry/duplicate). `verify_alliance_numbers.py` now runs 269 document/arithmetic checks including ten membership scenarios and the seven chain examples, with 31 self-test guards. The semantic validator remains at 31 checks and the isolated 09B suite grows from 177 to 210 tests (tests 177–198 cover the new `C25` grants and controls; tests 199–209 cover the ALF, ARL, multiple-membership and production-chain requirements).
10. **Regression executed (final post-edit state):** complete isolated 09B semantic suite **`Ran 210 tests in 27,210.874 s; OK; exit 0`** (the elapsed time includes a host sleep during the run; it is wall-clock, not test execution time); canonical 09B validator **31/31, exit 0**; `verify_alliance_numbers.py` **269 checked / 0 failed, exit 0**, self-test **31/31**; 09A validator **911 checks, exit 0**, 09A tests **43, OK, 28.708 s**; Stage 2 validator **358/358**; `validate_final.py` all checks passed, self-test **10/10**; decision-register tests **12, OK, 0.041 s**; next-action tests **23, OK, 0.124 s**; politics **879/879**, self-test **18/18**; market arithmetic **95/95**, workflows **14/14**; diplomacy numbers **9 groups / 0 failed**, workflows **17 groups / 0 failed**; economy **164/164**; cities **267/267**. Every command was rerun after the final 09B-K document edits; no test was skipped, no timeout is reported as a pass, and no selected subset is offered as proof that the complete suite passed.
11. **Final Status:** **Prompt 09B: correction completed by the primary writing agent; independent acceptance review pending. Prompt 09C: blocked pending independent acceptance.** No production code, migration, deployment, UI or gameplay runtime exists. `UD-040`, `UD-044`, `UD-046` and `UD-047` remain Open; `D-137` and its partial `D-140` amendment are preserved; `D-135`/`DD-151`, B-08/`REQ-530`, `D-014` and zero diplomatic delegation are unchanged.

---

## 47. Prompt 09B-L correction — consolidated Alliance taxation, operational funding, treasury authority, semantic validation, treaty governance and project-wide acceptance readiness (2026-11-02)

**Mission:** Apply one consolidated correction to the whole Phase 09B package without restarting, regenerating or renumbering it: reconcile automatic Alliance taxation with the original tax rules, separate national/municipal tax settings from Alliance brackets, define the ARL as a receipt/accounting record with one purpose-limited operational debit path, record the narrow `UD-045` and `UD-046` partial authorizations without closing either, close the remaining `C25` appeal-entitlement false negatives, correct `AT-T05` record-only treaty handling against a structured effect catalogue, reconcile `AX-01`–`AX-30`, and re-audit every active statement that still describes the earlier credit-only, voluntary-only or 26-contract model.

1. **Correction map first:** A file-by-file correction map was built before editing, covering B-09, the formula register, integration contracts, requirements, decision registers, the economy specification, continuity documents and the research/history files. Valid work from 09A and 09B-C through 09B-K is preserved; no rule, requirement, contract, formula, decision or test identifier was renumbered or removed.
2. **`ALL-006`–`ALL-008` reconciled:** `ALL-006` distinguishes national and municipal tax settings from Alliance taxation and states that an Alliance cannot alter either; `ALL-007` no longer prohibits automatic withholding, while retaining the bans on confiscation, stockpile access, unauthorized withdrawals or spending, transfers and changes to national financial policy; `ALL-008` separates automatic tax withholding, voluntary donations and other ordinary transfers as distinct transaction classes. `ALL-087`/`ALL-088` and the §14 treasury introduction were aligned with the same boundary. No per-policy national-owner consent was reintroduced.
3. **Per-turn production tax preserved:** `ALL-179`–`ALL-187`, `F-AL-006` and `ECN-213a` keep the Politics & War-style sequence: only gross eligible current-turn Crowns and resource production is taxed, opening balances and stockpiles are not, donations/purchases/transfers/market receipts are not production, separate Crowns and resource rates apply at any integer 0–10,000 bp, member brackets may differ, and collection is atomic, idempotent and never retroactive. Player-created brackets and per-Alliance assignment remain; a visible recorded 0% fallback covers an unconfigured or ambiguous case.
4. **ARL and operational funding:** The Alliance Receiving Ledger is a receipt and accounting record in `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` categories, not a treasury ownership decision. `ALL-220`–`ALL-226`, `REQ-648`–`REQ-653`, `F-AL-008`, `AX-27`, `ALF-27`–`ALF-29` and `AUD-AL-019` define one purpose-limited operational debit to a registered platform cost sink under a closed `AOP-01`–`AOP-04` purpose registry, exact cost schedule, authorization record, permission check, idempotency key, receipt, reconciliation and duplicate-payment protection. No member distribution, player payment, arbitrary transfer, general withdrawal, debt or negative balance exists.
5. **`UD-045` and `UD-046`:** `UD-045` records a narrow partial authorization for role-based tax-management permissions (bracket create/edit, Crowns and resource rate configuration, member bracket assignment/reassignment and reporting access) and remains Open for the wider catalogue, delegation and governance. `UD-046` records the authorized automatic tax receipt, ARL accounting and narrow operational funding mandate and remains Open for ownership, custody, capacity, general withdrawal, general spending beyond the narrow mechanism, distributions, unrestricted transfers and dual approval. Neither reservation is closed or reclassified.
6. **`C25` strengthened:** The semantic validator now detects retained/preserved entitlements, reviewability, appeal avenues, opportunities and procedural access in active, passive, direct, subordinate, conditional, compound and negative-polarity formulations; it evaluates the whole relevant policy assertion and rejects disclaimers that purport to immunize a grant. Historical, explanatory, non-normative, fixture and `UD-044`-reserved text remains exempt only when genuinely meta. The four required statements and their required equivalents fail with specific reasons; non-normative controls pass. Adversarial limitations and the conservative review gate are documented rather than presented as universal detection.
7. **`AT-T05` and treaty effects:** `ALL-197` now distinguishes explicitly registered record-only treaty types (valid diplomatic records that execute no mechanic) from unknown or unsupported types (rejected with `ALF-25`). `AT-E00` is record-only for `AT-T02`–`AT-T05`; `AT-E01` is the no-attack effect available only through `AT-T01`; `AT-T01` cannot be record-only. Custom text is never parsed and can never create an attack restriction, financial power or diplomatic authority; only structured supported effects trigger mechanics. `ALL-203`, `AX-29`, `REQ-634`/`REQ-640` and `C33` were aligned.
8. **Crowns and resource examples:** `F-AL-006`, `F-AL-008` and `ECN-213a` carry example sets covering 0%, 50%, 100%, opening balances, maintenance, later same-turn production costs, insufficient available balance, no negative national balance, no unauthorized withdrawal, retry/duplicate and exact reconciliation. A gross of 100,000 Crowns at 50% yields 50,000 to the Alliance and 50,000 net; at 100% it yields 100,000 and zero of that turn's new production; an opening balance is not taxed merely because maintenance later consumes it. The 0–100% range is not reduced and no debt, forced borrowing, confiscation or negative balance is invented.
9. **Per-Alliance assignment:** `ALL-182`, `REQ-621`, `AX-27`, `F-AL-006` and `ECN-213a` state that a member nation has at most one active bracket assignment per Alliance at a given effective turn, that an assignment identifies its Alliance, that one Alliance's bracket is not another's, and that overlapping memberships never stack deductions, create priority or exceed 100%. The multiple-membership safeguard and 0% fallback are preserved; `UD-040` remains Open.
10. **`AX-01`–`AX-30` reconciled:** `ALL-010` and every current-scope statement now name 30 contracts; genuine historical 09A records that state the earlier count are preserved as history. `AX-01`, `AX-16`, `AX-27`, `AX-28`, `AX-29` and `AX-30` were reconciled so automatic production withholding, voluntary transfers, ARL destination, structured treaty effects and attack blocking at every authoritative server entry point have distinct, non-duplicated responsibilities and mandatory audit.
11. **`ALL-093` and sovereign diplomacy:** The arbitrary confiscation clause remains withdrawn with an accurate tombstone; unrelated security, authentication, fraud, transaction and audit protections are preserved, and no disguised equivalent was found in the active specification. B-08 national treaty sovereignty and `REQ-530` are unchanged; B-09 alliance-to-alliance treaties require explicit authenticated owner consent for every covered nation, silence or majority is not consent, NAP refusal still permits non-covered membership, new members are not auto-covered, NAP blocks attacks both ways only between covered nations while active, other pacts create no automatic attack restriction, same-Alliance nations cannot attack regardless of treaty, leaving or changing membership creates no unintended consent or bypass, dissolution terminates the bilateral treaty, and every blocked attack is audited server-side.
12. **Validators and tests updated:** `09B_validate_alliance_semantic.py` now runs 34 checks (`C01`–`C34`) against B-09 v2.7, 653 requirements (55 Approved / 578 Provisional / 17 Open / 3 Deferred; 120 Alliance = 36 / 71 / 12 / 1), 164 decision rows (129 Approved) and the 30-contract `AX` set, and adds `C32` (ARL/operational funding), `C33` (record-only/NAP effects) and `C34` (national/municipal tax boundary). The permanent test suite and `verify_alliance_numbers.py` are extended for the new statements, and all earlier `C24`/`C25`, `G`–`P`, 142–146 and 177–209 fixtures are retained. Exact commands, counts and outcomes are recorded after the final run.
13. **Status distinction:** Everything in this pass remains **specified/designed and documentation-tested only**. No tax engine, ARL, treaty service or attack-enforcement code exists, no runtime or integration test demonstrates those mechanics, and passing documentation validators is not implementation evidence. Prompt 09B remains **correction completed by the primary writing agent; independent acceptance review pending**; Prompt 09C remains blocked.
14. **Final validation (2026-11-02):** The complete isolated suite `python docs/qa_backups/test_09B_alliance_semantic_validator.py -v` ran **253 tests in 1,658.410 s: OK, exit 0** (0 failures, 0 errors, 0 skips). An earlier complete run on the same corpus ran 253 tests in 1,938.511 s with **one failure**: `test_55_dd_tally_regression_fails` still tried to find the pre-09B-L `| Approved | 128 |` row; the fixture was corrected to mutate the current 129 tally to 128 and require the validator to reject it, and the full suite was rerun green. Canonical and documentation checks after the final edits: `09B_validate_alliance_semantic.py` 34/34, exit 0; `verify_alliance_numbers.py` 318/318 and `--self-test` 31/31, exit 0; `09_validate.py` 358/358, exit 0; `validate_final.py` all checks passed, exit 0; `09A_validate_alliance.py` 911 checks, exit 0; `test_09A_alliance_validator.py` 43 tests OK in 27.312 s; `verify_economy_numbers.py` 164/164, exit 0; `verify_politics_numbers.py` 879/879 and self-test 18/18, exit 0; `verify_city_numbers.py` 267/267, exit 0; `verify_market_numbers.py` 95/95 and `verify_market_workflows.py` 14/14, exit 0; `verify_diplomacy_numbers.py` 9 groups/0 failed and `verify_diplomacy_workflows.py` 17 groups/0 failed, exit 0; `test_decision_registers.py` 12 tests OK; `test_next_action.py` 23 tests OK. No test timed out and no timeout was treated as a pass.

---

## 48. Prompt 09B-M correction — final Phase 09B closeout (2026-11-02)

**Status:** correction complete by the primary writing agent; independent acceptance review pending. Phase 09B is ready for independent acceptance. Prompt 09C remains blocked pending independent acceptance.

This entry records the six 09B-M corrections: the C25 fail/review/safe semantic gate; the correction of the blanket owner-reservation statement in `05_unresolved_design_decisions.md`; the restoration of the historical five-capability `D-140` (2026-11-01) and the addition of `D-141` (2026-11-02) for the later narrow operational-funding authorization; the separation of ARL receipt accounting, allocation, approved operational expenditure and general treasury authority, with no approved cost schedule and therefore no spendable purpose; cumulative tax rounding across multiple same-asset production events; and the test-harness optimization without reduced coverage. `D-140` authorizes five Alliance capabilities and no operational-funding paragraph. `D-141` authorizes only the narrow purpose-limited operational-funding boundary; the AOP labels, four-category mechanics and permission name are project technical design choices under `D-014`, not owner selections. `UD-040`–`UD-049` remain owner-reserved except the narrow partial authorizations in `D-140`/`D-141`; no owner-reserved decision is marked resolved. The final commands, elapsed times, counts and timeout status are recorded in item 7.

1. **C25 conservative semantic gate.** `09B_validate_alliance_semantic.py` now separates three outcomes: confirmed active normative appeal policy (fail), uncertain active wording that may or may not be policy (manual review, which blocks a pass), and historical, disclaimer, rejected-proposal, illustrative or otherwise non-normative text (safe). A review finding is printed under `[REVIEW]`, and `main()` returns exit 1 when either a failure or a review exists, so uncertain text cannot silently pass. The earlier `C24`, `C25` `G`–`P` fixtures, tests 142–146 and 177–209 and every other control are retained. Tests `253`–`256` add independent regressions for appeal rights, appellate review, reconsideration, challenges to expulsion, procedural access, opportunities and abilities, passive wording, negative/restrictive wording, disclaimer-plus-active-policy, ambiguous future or under-consideration wording and historical/non-normative explanations, and cover all three outcomes. The detector is pattern-based and is not claimed to be exhaustive natural-language understanding.
2. **Owner-reservation statement corrected.** `05_unresolved_design_decisions.md` now states that an explicit owner reservation is not overridden by `D-014`, that assigning a row to a prompt does not authorize that prompt to resolve the reserved portion, and that a partial authorization resolves only the exact authorized portion. The required positions for `UD-040`–`UD-049` are preserved; active summaries that repeated the blanket claim were corrected, and historical entries were not rewritten.
3. **`D-140` restored and `D-141` added.** `D-140` is again the historical 2026-11-01 decision with exactly five capabilities (automatic member taxation, voluntary donations, the separate Alliance treaty object, NAP enforcement and the same-Alliance attack ban), the partial amendment of `D-137` and the withdrawal of `ALL-093`, with no operational-funding paragraph. `D-141` (2026-11-02) records the later narrow purpose-limited operational-funding authorization and its explicit relationship as an amendment to `D-140`. `D-141` states that the `AOP-01`–`AOP-04` labels, registry shape, `AUTHORIZE_OPERATIONAL_EXPENDITURE` permission name, four accounting categories and settlement mechanics are project technical design choices under `D-014`, not owner selections, and that no fee, price, amount, office or implementation is approved.
4. **ARL concepts separated.** Receipt accounting, allocation, approved operational expenditure and general treasury authority are four distinct concepts: only the third pays value, and the fourth is unavailable. `ALL-187`, `ALL-220`–`ALL-226`, `F-AL-008`, `AX-27`, `AX-28`, `REQ-648`–`REQ-653` and `DD-164` keep the `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` categories with `AVAILABLE = RECEIVED − RESERVED − EXPENDED`. No `AOP` purpose has an approved cost schedule naming its asset and exact amount, so `Valid(q) = 0` for every purpose today: tax and donation value is received and accounted, the assets remain in the ARL, and every actual expenditure is blocked pending the required approvals. This is recorded as a specification dependency, not a spending feature. The proposed `AOP` records are retained and labelled unavailable rather than deleted; `UD-046` remains Open for ownership, custody, capacity, general withdrawal, general spending, distributions and dual approval.
5. **Cumulative tax rounding.** `ALL-185`, `ALL-186`, `F-AL-006` and `ECN-213a` use one rule for an asset with production events `j = 1..m`: `C_j = Σ_{k≤j} g_k`, `D_j = floor(C_j × rate_bp / 10,000)`, `TaxAtEvent_j = D_j − D_{j−1}` and `TaxAlreadyCollectedForTurn = D_{j−1}`, with the end-of-turn identity `D_m = floor(G × rate_bp / 10,000) = Σ TaxAtEvent_j`. A single-event asset, including Crowns in P3.1, reduces to the per-turn floor. Independent per-event floors are explicitly forbidden. The arithmetic is integer-only; each event's tax is non-negative and never exceeds that event's gross, and a retry does not advance the accumulator. Cases covered include two 1-unit events at 50% (collects 1, not 0), four 1-unit events at 3,333 bp (collects 1), one larger event with the same total (same result), 0%, 100%, retry, different per-asset rates with separate accumulators, and end-of-turn reconciliation with no over- or under-collection. `verify_alliance_numbers.py` exercises these identities.
6. **Test-harness optimization without reduced coverage.** The 09B suite builds one shared pristine `docs/` baseline in `setUpClass` and gives each test a hardlink copy, falling back to `copy2` when a hardlink is unavailable; a write unlinks the target first, so modifications stay private to that test. The 09A suite uses the same helper. No test was deleted, skipped or weakened, no assertion was relaxed and no integration coverage was removed. A microbenchmark measured a full docs-tree copy at 124.0 ms versus a hardlink fixture at 42.2 ms per test; the 09A suite fell from 27.312 s to 10.580 s. The 09B end-to-end time remains dominated by validator execution, so it is not proportionate to the copy saving. No cached or earlier result was used as evidence for changed files.
7. **Final validation (2026-11-02).** The complete isolated suite `python docs/qa_backups/test_09B_alliance_semantic_validator.py` ran **257 tests in 1,833.109 s: OK, exit 0** — 0 failures, 0 errors, 0 skips, no timeout, all 257 tests completed. It started at 22:36:51 and finished at 23:07:32 local time. An earlier full run on the same 257-test corpus took 2,031.053 s and reported one failure, `test_05_header_version_regression_fails`, whose fixture still mutated the pre-09B-M `**Version:** 2.7`; the fixture was corrected to mutate the current `2.8` to `2.7` and require the validator to reject it, the test was re-run green on its own, and the full suite was then re-run green from scratch. For comparison, the accepted Prompt 09B-L run was 253 tests in 1,658.410 s. The three targeted groups were run once after the substantive changes: the C25 group (58 selected tests, 511.808 s, 0 failures/errors/skips), the ARL/operational-funding group (10 selected tests, 98.669 s, 0 failures) and the taxation/rounding group (25 selected tests, 248.913 s, 0 failures); every selected test ran. After the final register edits the fast checks were re-run against the current workspace: `09B_validate_alliance_semantic.py` 34/34 checks in 8.563 s; `09_validate.py` 358/358 in 1.180 s; `validate_final.py` all checks passed in 1.369 s; `verify_alliance_numbers.py` 375/375 in 0.527 s and `--self-test` 40/40 in 0.377 s; `verify_economy_numbers.py` 164/164 in 0.361 s; `09A_validate_alliance.py` 911 checks in 0.531 s; `verify_politics_numbers.py` 879/879 in 0.460 s; `verify_city_numbers.py` 267/267 in 0.349 s; `verify_market_numbers.py` passed in 0.395 s and `verify_market_workflows.py` in 0.588 s; `verify_diplomacy_numbers.py` 9 groups/0 failed in 0.417 s and `verify_diplomacy_workflows.py` 17 groups/0 failed in 0.462 s; `test_decision_registers.py` 12 tests OK in 0.037 s; `test_next_action.py` 23 tests OK in 0.142 s; `test_09A_alliance_validator.py` 43 tests OK in 10.580 s. No documented command timed out, and no timeout or absent run was treated as a pass. The full suite and the three targeted groups ran after the substantive corrections and the fixture fix; the two later edits were limited to the `DD` register header and this progress-log entry, after which the affected validators were re-run on the current tree and passed: `09B_validate_alliance_semantic.py` 34/34 (8.551 s), `09_validate.py` 358/358 (1.037 s), `validate_final.py` all checks passed (1.224 s), `verify_politics_numbers.py` 879/879 (0.414 s), `test_next_action.py` 23 tests (0.705 s) and `test_decision_registers.py` 12 tests (0.480 s), exit 0 in each case. No Alliance rule text changed in those two edits.
8. **Status distinction.** Everything in this pass remains **specified and designed, with documentation-level tests only**. No Alliance tax engine, ARL, operational-funding, treaty or attack-enforcement code exists; no runtime, load, integration, security or usability test demonstrates those mechanics; and passing document validators and fixtures is not implementation evidence. Phase 09B is ready for independent acceptance, and Prompt 09C remains blocked until that acceptance is granted.

---

## 49. Prompt 09B-N correction — recourse, former-member challenges and uncertain redress routing (2026-11-02)

**Purpose.** Close the two C25 false negatives found by the independent 09B-M audit and route uncertain appeal/remedy wording to manual review, without changing any Alliance rule or owner-reserved decision. This entry is appended for history; no earlier entry was rewritten.

**Files changed.** `docs/qa_backups/09B_validate_alliance_semantic.py` (recourse patterns, subject detection, people-label scrubbing before the historical/disclaimer exemption, segment-level review detection, banner), `docs/qa_backups/test_09B_alliance_semantic_validator.py` (permanent tests 257–259), `docs/stage-2/16_alliances_project_wide_consistency_audit.md` (§15 acceptance-closeout record) and the current-status documents synchronized on 2026-11-02. No B-09 rule, requirement, contract, formula or decision identifier was added, removed, renumbered or reworded.

**Decisions preserved.** `D-140` (2026-11-01) and `D-141` (2026-11-02) keep their historical and dated scopes; `UD-040`–`UD-049` remain **Open / Yes — owner** with only the documented partial authorizations; `UD-039` remains Resolved by `D-137`; `UD-044` remains owner-reserved and is not decided by an appeal detector. `ALL-006`–`ALL-008`, the four-category ARL, the 0–10,000 bp tax rates, the `AOP-01`–`AOP-04` registry, the `AT-E00`/`AT-E01` catalogue, B-08 national treaty sovereignty and `REQ-530` are unchanged.

**Tests actually executed.** The 09B-N record in audit §15 preserves these executed results: `09B_validate_alliance_semantic.py` 34/34 checks, exit 0, 7.342 s; `test_257_` 1 test, OK, 7.620 s; `test_258_` 1 test, OK, 7.363 s; `test_259_` 1 test, OK, 7.509 s; a temporary 83-test C24/C25/appeal selection reported `Ran 83 tests in 618.901 s`, OK, exit 0; `validate_final.py` all checks passed, 1.110 s; `09_validate.py` 358/358, 0.914 s; `verify_politics_numbers.py` 879/879, 0.419 s; `verify_alliance_numbers.py` 375/375, 0.450 s. **The complete 260-test suite was not rerun for 09B-N.** The earlier 257-test full-suite run in §48 is retained as historical evidence and is not presented as a 09B-N execution.

**Audit outcome.** Recourse wording and former-member challenge wording now **FAIL** when they assert a policy; uncertain redress/remedy wording returns **MANUAL REVIEW** and blocks a clean pass; genuine historical, disclaimer, rejected-proposal and `UD-044`-reserved text remains **SAFE**, while a disclaimer cannot neutralize a separate active entitlement in the same compound sentence. Tests 257–259 exercise all three outcomes and the compound-disclaimer bypass.

**Specified vs implemented.** The change is to a documentation validator and its fixtures. No appeal mechanic, expulsion process, notification, migration or UI is implemented, and no runtime test of an Alliance feature exists.

---

## 50. Prompt 09B-O correction — eight procedural C25 false negatives (2026-11-02)

**Purpose.** Close the eight remaining audited procedural false negatives in C25: petition for reconsideration, permitted review, mandatory hearing, decisions subject to reconsideration, right to challenge removal, request for review, a fixed denial of review and a petition for redress. Introduce a bounded person/action/normative-force gate so a procedural statement is evaluated as policy only when a person, an action and normative force are present.

**Files changed.** `docs/qa_backups/09B_validate_alliance_semantic.py` (bounded procedural detection, three-outcome handling, banner), `docs/qa_backups/test_09B_alliance_semantic_validator.py` (permanent tests 260–261) and the current-status documents synchronized in the 09B-O pass. No Alliance rule, requirement, contract, formula or decision identifier changed.

**Decisions preserved.** No owner decision was resolved. `UD-044` remains owner-reserved, `UD-040`–`UD-049` remain Open with only the partial `D-140`/`D-141` authorizations, and every accepted Alliance rule in B-09, the formula register and the integration contracts is unchanged. The correction is deliberately conservative: a pattern match permits a **FAIL** or **MANUAL REVIEW** outcome but never approves a policy.

**Fixtures and expected outcomes.** `test_260_eight_audited_false_negatives` encodes seven **FAIL** outcomes (`ZZ-O1`–`ZZ-O7`) and one **MANUAL REVIEW** outcome (`ZZ-O8`, a petition for redress). `test_261_procedural_domain_controls` encodes ten controls: active grants and denials **FAIL**, an ambiguous remedy **REVIEW**, and rejected-proposal, `UD-044`-reserved, unrelated-budget and unrelated-strategy text **SAFE**. The repository does not preserve a separate 09B-O execution log with counts or durations, so this entry does not claim a 09B-O run beyond the permanent fixture definitions it records. The later 09B-P record documents its own narrower execution and does not claim a full-suite run.

**Audit outcome.** The eight audited false negatives are represented by permanent fixtures with the expected classifications above; C25 still returns exactly **FAIL**, **MANUAL REVIEW** and **SAFE**, and the positive, negative, ambiguous, historical and unrelated controls keep the detector from over-matching. The `UD-044` reservation and the ban on inventing an appeal policy are preserved.

**Specified vs implemented.** Documentation validator and fixtures only. No procedural review, hearing, appeal or expulsion mechanic is implemented.

---

## 51. Prompt 09B-P correction — dismissal, grievance and redress classification (2026-11-02)

**Purpose.** Apply the three final audited C25 cases: an ambiguous challenge to “dismissal” and an unspecified grievance process must be surfaced for **MANUAL REVIEW**, while an express right to seek redress for an expulsion is a confirmed **FAIL**. Preserve the rule that a historical or reserved disclaimer cannot neutralize a separate active entitlement.

**Files changed.** `docs/qa_backups/09B_validate_alliance_semantic.py` (dismissal and grievance review patterns, explicit redress failure handling, banner), `docs/qa_backups/test_09B_alliance_semantic_validator.py` (permanent tests 262–265), `docs/stage-2/01_stage_2_prompt_roadmap.md` (09B correction record) and the four current-status documents synchronized on 2026-11-02/03. No Alliance rule, requirement, contract, formula or decision identifier changed.

**Decisions preserved.** `UD-044` remains owner-reserved and no appeal, grievance, hearing or redress policy is approved. `D-140`/`D-141`, `UD-040`–`UD-049`, the Global Trade scope under `D-122`, and every accepted Alliance rule are unchanged. The new classifications describe the validator's treatment of active policy text; they do not create a member right or an Alliance procedure.

**Tests actually executed.** The 09B-P record states that this pass executed **only Python compilation, its four new tests (`test_262`–`test_265`), the affected C25 group and the relevant C24 controls — not the complete suite**. The runtimes and selection counts for that narrower execution are not preserved in the audit, and this entry does not invent them. The permanent fixtures are: `test_262` (`ZZ-P1` “A former member may challenge dismissal” → **REVIEW**), `test_263` (`ZZ-P2` “A grievance process is available for expelled members” → **REVIEW**), `test_264` (`ZZ-P3` “There is a right to seek redress for an expulsion” → **FAIL**) and `test_265` (six compact controls: historical rejection and `UD-044`-reserved text **SAFE**; a current guarantee and a compound disclaimer-plus-entitlement **FAIL**; ambiguous dismissal **REVIEW**; explicit redress **FAIL**). The isolated suite now contains **266 tests**. The complete suite was not rerun.

**Audit outcome.** The three remaining audited false negatives are classified correctly by their fixtures, the three-outcome contract is unchanged, and the negative and non-normative controls pass. C25 remains a pattern- and context-based detector with documented limits, not a general natural-language policy oracle.

**Specified vs implemented.** Documentation validator and fixtures only. No Alliance appeal, grievance, dismissal, redress or expulsion mechanic exists, and no runtime, load, integration, security or usability test of an Alliance feature has been run.

---

## 52. Phase 09B acceptance record — specification and documentation ACCEPTED (2026-11-03)

**Status.** **Phase 09B Alliance specification and documentation: ACCEPTED at the specification/documentation level (D-142 / DD-165).** This is an acceptance record, not an implementation record and not a new owner authorization.

**What acceptance covers.** The canonical B-09 rulebook (`16_alliances.md` v2.8), its formula register and integration contracts, requirements `REQ-534`–`REQ-653`, the `ALL-*`, `AX-01`–`AX-30`, `AT-*`, `ALF-*`, `AUD-AL-*` and `F-AL-*` identifiers as specified, design decisions `D-135`–`D-141` / `DD-151`–`DD-165`, and the independent acceptance review outcome as applied by the 09B-N, 09B-O and 09B-P corrections. The acceptance is bounded by the audit evidence in [audit §15–§16](16_alliances_project_wide_consistency_audit.md) and the documentation validators.

**What acceptance does not cover.** It is not production implementation, live-game integration testing, release or operational readiness. No tax engine, Alliance Receiving Ledger service, treaty service, NAP check, attack validator, permission service, migration, API or UI exists. It is not a new owner authorization: `D-140` and `D-141` remain the owner-authorization records. It resolves and closes no unresolved decision: `UD-040`–`UD-049` remain **Open / Yes — owner**, and `UD-044` (appeal and expulsion rights), `UD-046` (treasury ownership, custody, capacity, general withdrawal and spending) and `UD-047` (collective diplomacy without delegation) are not decided by acceptance.

**Files changed for the record.** `docs/DECISIONS.md` (D-142 and the dated header), `docs/stage-2/04_approved_and_provisional_decisions.md` (v3.11, DD-165, tallies 130/26/3/2/2/1/1 of 165, project decisions 142), `docs/stage-2/05_unresolved_design_decisions.md` (v1.24 acceptance note, no status change), `docs/ROADMAP.md`, `docs/PROJECT_PROGRESS.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md` (Prompt 09C registration and B-09 dependencies for Prompts 10–15), `docs/stage-2/02_master_game_design_bible_outline.md` (B-10–B-19 filename mapping), this log, `docs/stage-2/16_alliances_project_wide_consistency_audit.md` (§16) and the B-09 status headers. No Alliance rule was rewritten.

**Decisions preserved.** `D-122` Global Trade remains approved mandatory product scope with G-1–G-6 unchanged; `D-140`/`D-141` keep their historical and dated scopes; `UD-039` remains Resolved by `D-137`; `UD-040`–`UD-049` remain Open; `D-014` is not used to override an owner reservation.

**Specified vs implemented.** Specified and documentation-tested only. **Prompt 09C is registered next and has not started**; the canonical deliverable `docs/stage-2/16_alliances_workflows_acceptance.md` has not been created. No new 09B redesign or research is authorized.

**Validation evidence (2026-11-03, targeted only).** `python docs/qa_backups/validate_final.py` — ALL CHECKS PASSED (1.2 s). `python docs/qa_backups/09_validate.py` — 358/358 checks passed, ALL CHECKS PASSED (0.9 s). `python docs/qa_backups/09A_validate_alliance.py` — 919 checks, PASS (0.4 s). `python docs/qa_backups/09B_validate_alliance_semantic.py` — 34 semantic checks, PASS (9.6 s). `python docs/qa_backups/test_next_action.py` — 23 tests OK (0.1 s). `python docs/qa_backups/test_decision_registers.py` — 12 tests OK (0.04 s). `python docs/qa_backups/test_09A_alliance_validator.py` — 43 tests OK (10.5 s). Selected `test_09B_alliance_semantic_validator.py` status/register regressions (`test_00`, `test_06`, `test_54`–`test_60`) — 9 tests OK (85.8 s). `python docs/qa_backups/verify_politics_numbers.py` — 879/879 checks passed. `python docs/qa_backups/verify_alliance_numbers.py` — 375 passed, 0 failed. Syntax compilation of the eleven modified QA scripts passed. The full historical 260/266-test Alliance semantic suite and unrelated economy, warfare and taxation suites were **not** rerun in this pass.

---

## 53. Prompt 09C — Alliance workflows, edge cases, acceptance matrix and release-gate evidence (2026-11-03)

**Status.** **Prompt 09C is COMPLETE at the specification/documentation level.** This is not implementation, integration testing, release or playability evidence. **Prompt 10 — Warfare, campaigns and postwar settlements — is next and has not started; Stage 2 is not complete.**

**Deliverable.** [`16_alliances_workflows_acceptance.md`](16_alliances_workflows_acceptance.md) is the single canonical companion. The B-09 rulebook remains the rule source of truth, its formula register the arithmetic source, its integration contracts the cross-system source and `03_requirements_traceability.md` the wording/status source. No competing canonical workflow document was created.

**Coverage produced.**
- 49 workflows `ALW-001`–`ALW-049` in groups A–J, each with all 18 mandatory fields.
- 20 player journeys J1–J20.
- 60 edge cases `ALE-001`–`ALE-060`, each mapped to a real rule and acceptance test; owner-dependent cases name the relevant `UD-040`–`UD-049`.
- Failure contract for `ALF-01`–`ALF-29`, including the undefined `ALF-13`–`ALF-20` gap and the `ALF-07`, Discord-URL and `ALF-25` inconsistencies, recorded rather than silently corrected.
- 20-row concurrency integrity matrix, 16 internal notification labels `AN-01`–`AN-16`, and a 25-threat security matrix that preserves `R-AL-01`–`R-AL-21`.
- 110 specification acceptance tests `AAT-001`–`AAT-110`, including every mandatory high-risk negative in §19.2.
- Exhaustive ledgers covering `ALL-001`–`ALL-226`, `REQ-534`–`REQ-653`, `AX-01`–`AX-30`, `F-AL-001`–`F-AL-008`, `AUD-AL-001`–`AUD-AL-019`, `D-135`–`D-142`, `DD-151`–`DD-165` and `UD-040`–`UD-049`.
- Cross-prompt handoffs to Prompts 10, 12, 13, 14 and 15; release dependencies `AL-RD-01`–`AL-RD-12` all NOT MET; implementation handoff and do-not-build list.

**Files changed.** `docs/stage-2/16_alliances_workflows_acceptance.md` (created); `docs/qa_backups/verify_alliance_workflows.py` (new documentation validator); `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/06_stage_2_progress_log.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/AI_HANDOFF.md`, `docs/AI_CONTEXT.md`, `ROADMAP.md`, `PROJECT_PROGRESS.md` and `docs/stage-2/02_master_game_design_bible_outline.md` (status and next-action continuity); the phase-specific QA guards and their regression tests were updated to the 09C-complete / Prompt-10-next state. B-09, its formula register, its integration contracts, `03_requirements_traceability.md`, `04_approved_and_provisional_decisions.md`, `05_unresolved_design_decisions.md` and `DECISIONS.md` were **not** edited.

**Decisions preserved.** `D-122`/`REQ-513`/`G-1`–`G-6` Global Trade remains authoritative and NOT MET (G-4 PARTIAL for design); `D-140` and `D-141` keep their exact scopes; `UD-039` remains Resolved by `D-137`; `UD-040`–`UD-049` remain Open and 09C resolves none. The exact tax model, ARL invariant, treaty catalogue, NAP coverage, same-Alliance attack ban, audit/privacy rules and zero-chat boundary are unchanged.

**Validation evidence (2026-11-03, focused).** `python docs/qa_backups/verify_alliance_workflows.py` — ALL CHECKS PASSED, 49 workflows / 60 edge cases / 110 tests (0.615 s); `--self-test` — 5/5 seeded defects detected (1.016 s). `python docs/qa_backups/verify_alliance_numbers.py` — 375 passed, 0 failed (0.653 s). `python docs/qa_backups/09B_validate_alliance_semantic.py` — 34/34 checks PASS (12.980 s). `python docs/qa_backups/09_validate.py` — 358/358 checks PASS (1.433 s). `python docs/qa_backups/validate_final.py` — ALL CHECKS PASSED (1.749 s). `python docs/qa_backups/09A_validate_alliance.py` — 943 checks PASS (0.781 s). `python docs/qa_backups/verify_politics_numbers.py` — 879/879 checks PASS (0.640 s). `test_next_action.py` — 23 tests OK (0.169 s); `test_decision_registers.py` — 12 tests OK (0.064 s); `test_09A_alliance_validator.py` — 43 tests OK (17.574 s); selected `test_09B_alliance_semantic_validator.py` C18/C19 status and boundary regressions (`test_57`, `test_58`, `test_58b`, `test_59`, `test_60`) — 5 tests OK (40.119 s). Syntax compilation of the eleven QA scripts passed. **NOT RUN in this pass:** the full 267-test historical `test_09B_alliance_semantic_validator.py` suite and unrelated economy, warfare and taxation suites, deliberately omitted under the focused-validation instruction. All results are documentation checks; no runtime, load, database, browser, security or playability test was executed, because no implementation exists.

**Specified vs implemented.** Workflow specification and acceptance-test plan only. No gameplay code, database, migration, scheduler, endpoint, ledger service, treaty service, attack validator, notification surface or UI was created. The correct status is: **"Alliance rules accepted; workflows and tests specified; implementation not started; no runtime evidence."**

**Next action.** **Prompt 10 — Warfare, campaigns and postwar settlements** — is the next official task and has not started.

---

## 54. Prompt 09C correction — succession authority, permission boundaries, exhaustive traceability, acceptance-test detail and downstream handoff (2026-11-03)

**Status.** **The Prompt 09C correction is COMPLETE at the specification/documentation level.** The existing companion was amended, not regenerated. This entry records a documentation correction pass; it is not implementation, integration testing, runtime evidence, release or playability evidence. **Prompt 10 — Warfare, campaigns and postwar settlements — remains next and has not started; Stage 2 is not complete.**

**Why the pass happened.** A review of the §53 deliverable found five substantive/structural defects that a validator-only pass could have hidden: succession and Primary Administrative Contact text that could be read as an executable transfer; general-permission workflows that treated owner-reserved powers as executable; traceability that grouped relationships instead of identifying each one; incomplete acceptance-test records; and incorrect B-section ownership in §15.12, the implementation handoff and `AL-RD-06`. The §53 record and its counts are preserved above as history and are not rewritten.

**Corrections made.**
1. **Succession and contact authority.** `ALL-057` claims and transaction order are audit evidence only. `ALW-013` and §4.11 no longer imply an executable position change; a vacancy remains unresolved unless the owner decides. `ALW-012` no longer describes a concrete contact-transfer procedure; the contact candidate under `ALL-053` is retained as candidate and is not executable while `UD-043` is Open. `AAT-111`–`AAT-118` assert the boundaries, including that a claim, contact request, constitution clause, vacancy or audit record creates no office, authority or caretaker.
2. **Permission boundaries.** Only the `D-140`/`DD-164` narrow tax-management set is treated as authorized: bracket create/edit, Crowns/resource rate configuration, member bracket assignment/reassignment and relevant tax-reporting access. `ALW-008`–`ALW-011`, office/rank assignment, constitution publication/amendment, general permission grant/revocation and privileged-operation validation record `PROPOSED` or refuse; they do not execute. A role title is never accepted as evidence of permission. `AAT-119`–`AAT-124` assert title, scope, over-grant, revocation and stale-authority boundaries.
3. **Classified bidirectional traceability.** §15.14 and §15.15 identify each relationship separately — source ID, status, authoritative source, class, workflows, edge cases, tests, cross-system dependency, owner decision, evidence status and justification forward; own ID, exact `ALL`/`REQ`/`AX`/`F-AL`/`AUD`/`ALF`/`D`/`DD`/`UD` refs, class per ref, justification, authorisation and downstream owner reverse. Reverse scope covers all 49 workflows, 65 edge cases, 132 tests, 16 notification events, 25 security safeguards and 20 concurrency scenarios. Owner-reserved items are `DIRECT` only as block assertions with authorisation `blocked`; tests proving a requirement stays blocked are `DIRECT`.
4. **Acceptance-test detail.** All 132 tests carry the 26 mandatory fields, numbered 1–26 in the prescribed order, with no blank field and a prescribed evidence status. `AAT-001`–`AAT-110` keep their original IDs; `AAT-111`–`AAT-132` were added for previously missing boundary and evidence assertions (22 new tests). §14.7 totals are calculated: 20 founding/membership, 28 constitution/governance, 22 taxation, 16 donations/ARL, 16 treaties/NAP, 12 attack validation, 10 audit/boundaries/recovery and 8 traceability/evidence. §15.16 reports 3,432 populated fields, 0 tests without a source ref and calculated, not estimated, coverage.
5. **Downstream ownership.** §15.12, §16, §16.3, `AL-RD-06` and related handoff rows use the official B titles: B-03 accounts/nation creation/progression, B-08 diplomacy, B-09 alliances, B-10 warfare/campaigns/settlements, B-12 fair play/player protection/privacy/reporting/moderation/administration, B-13 interface/player journeys, B-14 formulas/numerical rules/balance, B-15 Bible assembly. Moderation is assigned to B-12, never B-14.

**Secondary semantic audit.** Succession, successor, heir, caretaker, vacancy, contact, transfer, inheritance, role authority, constitution publication, office assignment, delegation, moderation, appeal, voting, treasury, approval and executable were scanned across the document. Positive hits were limited to negations, record-only statements, candidate status or owner-reserved prohibitions. No positive conflict remained after correction.

**Counts (calculated).** 49 workflows unchanged; 65 edge cases `ALE-001`–`ALE-065` (60 at §53, five added for the corrected boundaries); 132 tests `AAT-001`–`AAT-132` (110 at §53, 22 added); 16 notifications; 25 security rows; 20 concurrency rows. Traceability classes: ALL 146 DIRECT / 42 SUPPORTING / 37 DEFERRED / 1 NOT APPLICABLE; REQ 119/0/1/0; AX 20/1/9/0; F-AL 2/5/1/0; AUD 14/1/4/0; ALF 14/3/4/8; decisions 18/5/0/0; UD 10/0/0/0. Unexplained orphans: 0. Deliberate unmapped source identifiers: 45. Deferred relationships naming an owner: 56/56.

**Files changed in this pass.** `docs/stage-2/16_alliances_workflows_acceptance.md` (amended in place; original §§1–14 material and all valid §53 content preserved); `docs/qa_backups/verify_alliance_workflows.py` (extended with the five correction checks and 17 seeded-defect self-tests); `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/06_stage_2_progress_log.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/AI_HANDOFF.md` and `docs/AI_CONTEXT.md` (correction status and next action). B-09, its formula register, its integration contracts, `03_requirements_traceability.md`, `04_approved_and_provisional_decisions.md`, `05_unresolved_design_decisions.md` and `DECISIONS.md` were **not** edited. No new canonical workflow document was created.

**Validation evidence (2026-11-03, focused).** `verify_alliance_workflows.py` — ALL CHECKS PASSED, 49 workflows / 65 edge cases / 132 tests (0.500 s); `--self-test` — 17/17 seeded defects detected (6.598 s). `verify_alliance_numbers.py` — 375/375 (0.236 s). `09B_validate_alliance_semantic.py` — 34/34 (10.417 s). `09_validate.py` — 358/358 (0.653 s). `validate_final.py` — PASS (0.956 s). `09A_validate_alliance.py` — 943 checks (0.240 s). `verify_politics_numbers.py` — 879/879 (0.182 s). `test_next_action.py` — 23 tests (0.128 s); `test_decision_registers.py` — 12 tests (0.042 s); `test_09A_alliance_validator.py` — 43 tests (13.558 s); selected `test_09B` C18/C19 status and boundary regressions (`test_57_continuity_status_removed_fails`, `test_58_09c_authorized_fails`, `test_58b_09c_complete_without_spec_qualifier_fails`, `test_59_next_prompt_changed_fails`, `test_60_09c_companion_without_boundary_fails`) — 5 tests (52.442 s). Syntax compilation of the eleven QA scripts passed. The full 267-test historical `test_09B` suite also passed in a separate background run (267 tests OK, 2,743.679 s); because that run overlapped the final continuity edits, the five status-sensitive tests were re-executed against the final files and passed (52.442 s). Unrelated economy, warfare and taxation suites were not run. No unexecuted suite is reported as passed. All results are documentation checks; no runtime, load, database, browser, security or playability test was executed, because no implementation exists (`D-012`).

**Specified vs implemented.** Workflow specification, traceability register and acceptance-test plan only. No gameplay code, database, migration, scheduler, endpoint, ledger service, treaty service, attack validator, notification surface or UI was created. The correct status is: **"Alliance rules accepted; workflows, traceability and tests specified and documented-validated; implementation not started; no runtime evidence."**

**Owner decisions.** `UD-040`–`UD-049` remain Open and unchanged; the correction resolves none. `D-140`/`DD-164` remain the narrow tax-management authorisation and `D-141`/`DD-161` the narrow operational-funding boundary, exactly as recorded. No owner authorization was created and no owner-reserved policy was made executable.

**Next action.** **Prompt 10 — Warfare, campaigns and postwar settlements** — is the next official task and has not started.

---

## 55. Prompt 09C-B correction — position management and constitution capability authority boundary (2026-11-03)

**Status.** **The Prompt 09C-B correction is COMPLETE at the specification/documentation level.** The existing companion was amended in place; no replacement specification was created. This entry records a documentation correction pass. It is not implementation, integration testing, runtime evidence, release or playability evidence. **Prompt 10 — Warfare, campaigns and postwar settlements — remains next and has not started; Stage 2 is not complete.**

**Why the pass happened.** A further review found that `ALW-010` and `AAT-027`/`AAT-028` still described executable structured position creation and deletion through `MANAGE_ROLES`, and that constitution publication/amendment wording could still be read as a currently available capability. That conflicted with Open `UD-045` and the rule that only the narrow tax-management set is executable. §54's statement that general permission features record `PROPOSED` is superseded by this entry.

**Corrections made.**
1. **`ALW-010` is descriptive-only.** Players may express, discuss and record a proposed position or governance arrangement as non-operative descriptive content. The workflow creates, modifies, deletes, activates, assigns or grants no structured position, office, role, permission or capability; `MANAGE_ROLES` does not execute; no structured `PROPOSED` or `ACTIVE` permission set is stored. A structured position operation is refused with `ALF-08`, the refusal is recorded as `AUD-AL-004` rejection evidence only, and no `AUD-AL-003` position/assignment row is written.
2. **`ALW-008` and `ALW-009` are descriptive-only.** Descriptive constitution and amendment text remains writable and discussable, but structured drafting, approval, publication, activation, supersession and enforcement are future conditional and blocked under `UD-045`. A structured attempt is refused with `ALF-08` and recorded as `AUD-AL-005` rejection evidence; no version, hash, approval record, permission or office is created, and no `AN-05` publication notice is sent.
3. **`AAT-027`–`AAT-029` now test the block.** They require refusal with `ALF-08`, no position/office/role/permission/assignment/capability creation, deletion or change, no cascade, no `AUD-AL-003` row, `AUD-AL-004` rejection evidence, `AN-11` refusal and an explicitly unchanged state. `AAT-021`–`AAT-026` likewise assert refusal and no version or retroactive effect, rather than successful publication or amendment.
4. **`ALW-011` remains the narrow exception.** Executable assignment and revocation is limited to the narrow tax-management set under `D-140`/`DD-164`; every wider request is descriptive content only, never a structured active or `PROPOSED` permission.
5. **Cross-document reconciliation.** The §3.2 capability matrix, §3.5 execution-time rules, §4.3 constitution-version states, §2.11 automatic acts, §3.1 active-member visibility, §6.2 state ledger, §7.4 authorisation matrix, §13 threat row, J2 expected outcome, §15.2 rule ledger, §15.9 audit ledger, §15.14 forward traceability, §15.15 reverse traceability, §18.1 conceptual objects and §18.2 build order now describe the same authority boundary. `ALL-031`–`ALL-043` traceability no longer claims execution by `ALW-008`/`ALW-009`. `ALF-08` recovery no longer points to an executable constitution route.
6. **Baseline membership distinction.** `ALW-003` and `AAT-007` clarify that the acceptance-time default member position is a baseline membership position that grants no capability and is not a general position-management operation. The authoritative `ALL-082` behaviour is unchanged.

**Occurrence classification.** Descriptive/proposed constitutional and position content (Category A) is retained. Structured constitution publication/amendment and structured position management are explicitly future conditional and blocked (Category B); no occurrence remains as a currently executable capability (Category C). Candidate permission names in the matrix, workflows, tests and handoff are labelled candidate and non-executable.

**Validator changes.** `docs/qa_backups/verify_alliance_workflows.py` gained checks for the `ALW-008`/`ALW-009`/`ALW-010`/`ALW-011` descriptive-only boundaries, the §3.2 matrix and §4.3 future-conditional status, blocked `ALL-031`–`ALL-043` traceability, refusal expectations in `AAT-021`–`AAT-029`, and the `AAT-119`–`AAT-124` authority assertions. It rejects the prior positive phrases for publication, position records, configured positions and executable traceability. The seeded-defect self-test increased from 17 to 24 cases.

**Counts.** 49 workflows, 65 edge cases and 132 tests are unchanged. No test ID, workflow ID, edge-case ID, audit ID, notification ID or decision was added, removed or renumbered. `D-139` and its candidate architecture are preserved; `UD-045` remains Open and unresolved. Only `D-140`/`DD-164` narrow tax-management permissions remain executable, plus the `AUTHORIZE_OPERATIONAL_EXPENDITURE` boundary whose purposes are unavailable.

**Files changed in this pass.** `docs/stage-2/16_alliances_workflows_acceptance.md` (amended in place); `docs/qa_backups/verify_alliance_workflows.py` (new checks and seeded defects); `docs/stage-2/06_stage_2_progress_log.md` (this entry); `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/AI_HANDOFF.md`, `docs/AI_CONTEXT.md` and `docs/stage-2/00_stage_2_handoff.md` (status citations now include §55). B-09, its formula register, its integration contracts, `03_requirements_traceability.md`, `04_approved_and_provisional_decisions.md`, `05_unresolved_design_decisions.md` and `DECISIONS.md` were **not** edited.

**Validation evidence (2026-11-03, focused).** `verify_alliance_workflows.py` — ALL CHECKS PASSED, 49 workflows / 65 edge cases / 132 tests; `--self-test` — 24/24 seeded defects detected. `09B_validate_alliance_semantic.py` — 34/34 checks PASS. `09_validate.py` — 358/358 checks PASS. `validate_final.py` — initially FAILED with `no roadmap row cites the latest log §55`; after the roadmap and continuity citations were updated, ALL CHECKS PASSED. `test_09A_alliance_validator.py` — 43 tests OK. Syntax compilation of the corrected validator passed. **NOT RUN in this pass:** the full 267-test historical `test_09B_alliance_semantic_validator.py` suite and unrelated economy, warfare and taxation suites, deliberately omitted under the focused-validation instruction. All results are documentation checks; no runtime, load, database, browser, security or playability test was executed, because no implementation exists.

**Specified vs implemented.** Workflow specification, traceability register and acceptance-test plan only. No gameplay code, database, migration, scheduler, endpoint, ledger service, permission service, notification surface or UI was created. The correct status is: **"Alliance rules accepted; workflows, traceability and tests specified and documented-validated; structured position and constitution management blocked under `UD-045`; implementation not started; no runtime evidence."**

**Owner decisions.** `UD-040`–`UD-049` remain Open and unchanged; this pass resolves none. `D-139` and its candidate permission architecture are preserved. No owner authorization was created and no owner-reserved or candidate capability was made executable.

**Next action.** **Prompt 10 — Warfare, campaigns and postwar settlements** — is the next official task and has not started.


---

## 56. Prompt 10A — Politics and War warfare research, evidence, requirements and cross-system integration (2026-11-03)

**Status.** **Prompt 10A is COMPLETE at the research/documentation level.** The canonical deliverable is [`research/10A_politics_and_war_warfare_research.md`](research/10A_politics_and_war_warfare_research.md) — 35 sections, 40 sources, 52 findings, 26 P&W-to-Nation-Supremacy classifications and 44 research-scoped candidate requirements. It writes **no B-10 rule**, approves **no formula or number**, and creates **no code, migration, endpoint, screen or deployment**. At the time of §56, **Prompt 10B — Warfare Foundations and Complete Rules — was next and had not started; Prompt 10C was pending; Prompt 11 was not started; Stage 2 was not complete.**

**Why the pass happened.** The roadmap item — Prompt 10, Warfare, campaigns and postwar settlements — needs a researched evidence base before B-10 can be written. 10A collects and grades that evidence from Politics and War only, records what is actually observable, separates it from inference, tests every mechanic against the mapless constraint, and publishes the handoffs 10B and 10C must follow. It is the same split used for Prompts 07, 08 and 09 (A research, B specification, C workflows/acceptance).

**Research scope and restrictions actually observed.** Sources were limited to the P&W game's public interface, official P&W documentation and P&W-dedicated community wikis; no other game, wiki, forum, Reddit, Discord, YouTube, blog, encyclopedia, military source or AI summary was used as evidence. No sign-in, credential request, transaction, war declaration, message or any other state-changing action was performed; no private API, database, source code, hidden endpoint, developer-tool extraction, automated scrape, modification or data-mining was used. Search engines were used only to discover pages, and every citation is a page actually opened and examined, with its URL, heading, category, access date and — where shown — revision date. Where sources disagree, the disagreement is recorded as `WFX-01`…`WFX-12` rather than silently resolved. Wiki ownership is stated per source; no community wiki is called official.

**What the report contains.** §1 executive summary; §2 scope and restrictions; §3 dates and method; §4 project-document inventory; §5 the existing Nation Supremacy warfare baseline; §6 the source register (`WFS-001`…`WFS-040`) with `WFX-01`…`WFX-12`; §7 the mechanics catalogue in fifteen areas (war lifecycle and slots, declarations and ranges, resistance and victory, operations and MAPs, units, policies, blockades, espionage, missiles and nukes, protection, beige/grey, alliance war, inactivity and moderation, interface and information, and turn/update timing); §8 fifty-two findings (`WFR-001`…`WFR-052`); §9 the twenty-field attack/operation matrix; §10 sixteen formula-evidence records (`WFE-01`…`WFE-16`); §11 readiness and resources; §12 supply and logistics; §13 the `S0`–`S7` lifecycle; §14 protection; §15 losses; §16 termination and postwar; §17 alliance warfare; §18 abuse; §19 the strict mapless-suitability analysis; §20 the 26-row classification (`WFC-01`…`WFC-26`, ADOPT CANDIDATE / ADAPT / REJECT / NOT APPLICABLE / INVESTIGATE FURTHER); §21 the inherited constraints and invariants; §22 the 16-system integration matrix (B-02, B-03, B-04, B-05, B-06, B-08, B-09, B-11, B-12, B-13, B-14, B-15, B-16/17) with eleven fields per row; §23 forty-four candidate requirements (`WCR-01`…`WCR-44`) across 22 areas; §24 twenty formula questions (`WQN-01`…`WQN-20`); §25 twelve conflicts and sixteen gaps (`GAP-01`…`GAP-16`); §26 fifteen risks (`WRK-01`…`WRK-15`); §27 twenty-two open questions (`WFQ-01`…`WFQ-22`); §28 the dedicated UD-032 analysis; §29 the `WFH-A`…`WFH-F` Prompt 10B handoff; §30 the 10C and downstream handoffs; §31 the completion checklist; §32 the validation record; §33 files created and updated; §34 files intentionally not changed; §35 limitations.

**UD-032.** The report's §28 analyses all three options — keep the block, forfeit with a recorded outcome, and finish under the old identity — against exploit resistance, fairness to the opponent, record integrity, B-03/B-04 compatibility, complexity, player clarity, settlement interaction, risk and mitigation. **It selects none.** UD-032 remains **Deferred to Prompt 10** in the [05 register](05_unresolved_design_decisions.md); Prompt 10B must decide it explicitly and may not resolve it by assumption. No `D-` or `DD-` decision was added and `DECISIONS.md` was not edited.

**Binding constraints preserved.** The report restates and does not alter D-014, D-015, D-023 and D-024; REQ-014, REQ-063, REQ-085/086, REQ-090, REQ-099, REQ-108/109, REQ-177, REQ-518, REQ-588–591 and REQ-640/642/645–647; B-03 `NET-`/`RRL-`/`ONB-`; B-04 `ECN-214`/`ECN-130`; B-05 `URB-111`/`URB-157`/`URB-061`; B-06 `DMP-092`/`DMP-127`/`DMP-140`; B-08 `DP-T01`/`DIP-039`/`DIP-070`/`DIP-141`; and B-09 `ALL-089`/`ALL-139`/`ALL-140`, `ALL-206`–`ALL-215`, `AX-18`/`AX-30`, `AT-E01` and `AUD-AL-017`. No Alliance military power, delegation, shared pool or collective command is created.

**Counts.** 40 sources `WFS-001`…`WFS-040`; 52 findings `WFR-001`…`WFR-052`; 16 formula-evidence records `WFE-01`…`WFE-16`; 12 source conflicts `WFX-01`…`WFX-12`; 26 classifications `WFC-01`…`WFC-26`; 44 candidate requirements `WCR-01`…`WCR-44`; 20 formula questions `WQN-01`…`WQN-20`; 15 risks `WRK-01`…`WRK-15`; 22 open questions `WFQ-01`…`WFQ-22`; 16 gaps `GAP-01`…`GAP-16`; 36 `WFH-` handoff items (`WFH-A1`…`WFH-F6`). None is a `REQ-` row, a B-10 rule or an approved number; the [requirements register](03_requirements_traceability.md) is unchanged at 55 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed = 653.

**Files changed in this pass.** `docs/stage-2/research/10A_politics_and_war_warfare_research.md` (new); `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/stage-2/03_requirements_traceability.md` (metadata only), `docs/stage-2/05_unresolved_design_decisions.md` (UD-032 evidence/handoff references only) and this log (header, table rows, this entry). QA maintenance is recorded below.

**QA maintenance (narrow, 2026-11-03).** The split was registered without weakening any assertion: `status_rules.py` sets `CURRENT_SUBPROMPT = "10B"`, adds `10A` to `COMPLETED_SUBPROMPTS` and widens the sub-prompt pattern to the 10 family; `test_next_action.py` and `test_decision_registers.py` assert `stage_2_next_prompt: 10B`, the new row 09/row 10 text, and two new regressions (`test_completed_10a_cannot_be_the_next_task_but_10b_may_be`, `test_regex_recognises_the_10_family`); `validate_final.py` advances the expected next prompt to 10B, recognises the 10 family in the handoff-header guard, requires the row 09/row 10 wording, requires the 01 roadmap to register 10A with its canonical report and 10B/10C, adds the 10A report to the required-document list and requires `Prompt 10A`/`Prompt 10B` in `ROADMAP.md`; `09_validate.py` advances its status, header, §H and row checks to 10B and adds the row 10 checks; `09A_validate_alliance.py` accepts the 10 family and its fixture was updated; `09B_validate_alliance_semantic.py` accepts `10`/`10A`/`10B`/`10C` on the STATUS line and its printed status was corrected; the `test_09B` fixture was updated; and `verify_politics_numbers.py` checks row 09 and row 10. In `test_decision_registers.py` the row-10 selector now matches the Stage 2 warfare row by title because `PROJECT_PROGRESS.md` also carries a Stage 1 report row numbered 10 — the assertions were not relaxed, and the earlier selector could only ever test the Stage 1 row. No B-02–B-09 rulebook, formula register, Alliance workflow companion, 08/09 research, decision, owner policy or Stage 1 report was edited.

**Validation evidence (2026-11-03, focused).** `validate_final.py` — ALL CHECKS PASSED (exit 0). `09_validate.py` — 359/359 checks passed (exit 0). `09B_validate_alliance_semantic.py` — 34/34 semantic checks passed (exit 0). `09A_validate_alliance.py` — 943 checks passed (exit 0). `verify_politics_numbers.py` — 879/879 (exit 0). `test_next_action.py` — 25 tests OK (0.149 s, exit 0). `test_decision_registers.py` — 12 tests OK (exit 0). `test_09A_alliance_validator.py` — 43 tests OK (12.487 s, exit 0). Six status-sensitive `test_09B_alliance_semantic_validator.py` regressions (`test_06`, `test_57`, `test_58`, `test_58b`, `test_59`, `test_60`) — 6 tests OK (58.480 s, exit 0). `python -m py_compile` over the ten modified QA scripts — OK. **Not run:** the full 267-test historical `test_09B` suite (long-running and outside this focused pass), the unrelated economy, city, market, diplomacy workflow and diplomacy number verifiers, and the full `test_09A`/other prompt suites beyond those listed. **No runtime, database, browser, load, security or playability test was executed**, because no gameplay implementation exists. All results are documentation checks.

**Owner decisions.** No owner-reserved decision was touched. **UD-032 remains Open/Deferred and unresolved**; `UD-040`–`UD-049` remain exactly as recorded; no new authorization exists and no B-10 rule is approved.

**Next action.** **Prompt 10B — Warfare Foundations and Complete Rules** — is the next official task and has not started.

---

## 57. Prompt 10A correction — Alliance NAP authority attribution, empty-source count and P&W geographic wording (2026-11-03)

**Status.** **The Prompt 10A correction is COMPLETE at the research/documentation level.** The existing 10A report was amended in place; no replacement report and no new research phase was created. This entry records a documentation correction pass. It is not implementation, runtime evidence, release or playability evidence. **Prompt 10A remains complete; Prompt 10B remains next and has not started; Prompt 10C remains pending; Prompt 10 remains IN PROGRESS; Stage 2 is not complete.**

**Objective.** Remove three defects identified by the independent review of the 10A report without reopening the research, redesigning B-09 or deciding any owner-reserved question: (A) Alliance NAP, `AT-T01`, `AT-E01` and `ALL-206` authority was wrongly attributed to `UD-047`; (B) the source register counted three empty pages although four identifiers are empty; and (C) the report described P&W over-broadly as having "no geography" and a city as its only spatial object.

**Correction A — authority attribution.** The erroneous wording in report §17.4 — "B-09 Alliance NAP — ALL-206 for covered nations under the authorized `UD-047` framework" — was replaced by: *"B-09 Alliance NAP — ALL-206 for the explicitly consenting covered nations under the separate Alliance-to-Alliance treaty framework authorized by `D-140` (`AT-T01` / `AT-E01`). Membership alone does not cover a nation; a non-consenting member remains a member and is outside the NAP. `UD-047` remains Open / Owner-Reserved for collective diplomatic positions and any delegation model and authorizes no part of this framework."* The corrected chain is: **`D-140`** authorizes the narrow, separate Alliance-to-Alliance treaty object, treaty type **`AT-T01`**, effect **`AT-E01`**, the NAP restriction between explicitly consenting covered nations, and the other limited treaty types within `D-140`'s scope. **`UD-047` remains Open / Owner-Reserved** for broader collective diplomacy, positions and delegation. `D-140` does not authorize general collective diplomacy, alliance-wide national diplomatic delegation, automatic war declarations on behalf of members, general control of national militaries, or any power beyond its recorded scope. The same false authorization link was corrected in the 01 roadmap (status blockquote, 09C workflow group G and the B-09 Alliance dependency), `AI_CONTEXT.md`, `AI_HANDOFF.md` (two places), `PROJECT_PROGRESS.md`, `DECISIONS.md` (the D-142 cross-reference only) and the 09B consistency audit (two cross-references). No B-09 rule, B-09 register, D-140 text, UD status or UD wording was changed.

**Correction B — source count.** All four rows were inspected individually: `WFS-035` (Military Action Points) — empty; `WFS-036` (War Range) — empty; `WFS-037` (Peace) — empty; `WFS-038` (DEFCON) — empty, with the note that the War Policy page references DEFCON but documents no mechanic. **All four are empty pages.** The source-count line was corrected from "3 are empty pages (`WFS-035`–`WFS-038`)" to "4 are empty pages (`WFS-035`, `WFS-036`, `WFS-037` and `WFS-038`)". IDs were kept stable; no source was deleted, renumbered or invented; the `Empty/absence: 4` subtotal already agreed, and the total remains 40 entries.

**Correction C — geographic wording.** The over-broad claim that P&W has "no geography" and that "the only spatial object is a city" was replaced with evidence-backed wording that distinguishes **(1) geographic concepts in P&W's game world** from **(2) map-based warfare mechanics**. P&W does use continents and named cities as game-world concepts (`WFS-028`, `WFS-031`); its **warfare**, however, targets a nation, or for missiles and nukes a city within that nation, and the examined pages document no geographic front, province or tile, geographic adjacency, physical troop movement across a territorial map, coordinate-based battlefield targeting or geographic supply route (`WFS-022`, `WFS-031`, `WFS-032`). Executive summary item 3, the executive-summary verdict, §11, §12, `WFR-013`, `WFR-052`, the peace and missile mapless-fit rows, §19.1 (a new distinction paragraph), §19.3/§19.4, and `WFC-01`, `WFC-15` and `WFC-26` were narrowed accordingly; no remaining line claims that P&W has no geography at all. **Nation Supremacy's binding mapless requirement is unchanged and not weakened:** no geographic fronts, no territorial world map and no physical troop movement.

**Files changed in this pass.** `docs/stage-2/research/10A_politics_and_war_warfare_research.md` (in-place correction; v1.0 → v1.1); `docs/stage-2/01_stage_2_prompt_roadmap.md`; `docs/AI_CONTEXT.md`; `docs/AI_HANDOFF.md`; `docs/PROJECT_PROGRESS.md`; `docs/DECISIONS.md` (D-142 cross-reference only); `docs/stage-2/16_alliances_project_wide_consistency_audit.md` (two historical cross-references only); and this log. **Not changed:** B-02–B-09 rulebooks and their registers, 08/09 research reports, `03_requirements_traceability.md` (row/status/count), `04_approved_and_provisional_decisions.md` (decision state), `05_unresolved_design_decisions.md` (status/owner/count), Stage 1 reports, application code, schema, migrations, infrastructure and live-game data.

**Validator commands and results (2026-11-03, focused).** All commands were run from `docs/qa_backups` with `python`. `validate_final.py` — `VALIDATION: ALL CHECKS PASSED` (exit 0), including the roadmap-citation check after row 10 and this log were advanced to §57. `09_validate.py` — `359/359 checks passed`, `ALL CHECKS PASSED` (exit 0), including `PASS UD-047 is genuinely Open in its Status cell` and the row 09/row 10 status checks. `python -m unittest test_next_action test_decision_registers -v` — `Ran 37 tests in 0.179s`, `OK` (exit 0), including `test_completed_10a_cannot_be_the_next_task_but_10b_may_be` and the unresolved-status and decision-range tests. `verify_politics_numbers.py` — `879/879 checks passed` (exit 0); run because row 09/row 10 text and citations changed. `09B_validate_alliance_semantic.py` — `All 34 semantic checks passed with no review findings` (exit 0); run because the 09B consistency audit and the D-142 cross-reference were edited. The first four were re-run unchanged after the final wording edits in this pass, with the same results. **Not run:** the full 267-test historical `test_09B` suite, the long-running `test_09A` suite, and the unrelated economy, city, market and diplomacy verifiers. **No runtime, database, browser, load, security or playability test was executed**, because no gameplay implementation exists; every result above is a documentation check.

**Limitations.** This is a documentation correction only. No P&W page was re-fetched, so the four empty-source findings rely on the 10A access-date register rather than a fresh fetch. The pass does not re-audit the rest of the 10A report, creates no B-10 rule, approves no formula or number, and resolves neither `UD-032` nor any other owner-reserved decision. Historical 09B audit text was corrected only for the false authority cross-reference; its substantive findings and dates are preserved.

**Owner decisions.** No owner-reserved decision was touched. **`UD-047` remains Open / Owner-Reserved** for collective diplomacy, positions and delegation. **`UD-032` remains Deferred and unresolved**; `UD-040`–`UD-049` remain exactly as recorded. No `D-` or `DD-` decision was added, removed, renumbered or reworded beyond the narrow false cross-reference in D-142.

**Next action.** **Prompt 10B — Warfare Foundations and Complete Rules** — is the next official task and has not started.

## 58. Prompt 10B — Warfare foundations, complete rules, formula register and 10A disposition (2026-11-03)

**Status.** **Prompt 10B is COMPLETE at the specification/documentation level.** The canonical deliverables are [B-10 — Warfare, campaigns, military operations and settlements](17_warfare_and_settlements.md) (30 sections, 188 `WAR-` rules) and the [B-10 formula register](17_warfare_formula_register.md) (35 formulas `F-WR-001`–`F-WR-035`, 20 mandatory fields each). The pass records 25 architecture decisions (`B10-AD-01`–`B10-AD-25`, mirrored as DD-166–DD-190), disposes every 10A identifier, resolves **UD-032** as **Option A**, and preserves `UD-040`–`UD-049`. It is **not** implementation, runtime testing, numeric approval, balance evidence or release. **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence — is next and has not started; Prompt 11 is not started; Stage 2 is not complete.**

**Pass 1 — architecture and conflict resolution.** B-10 defines a mapless, national-sovereignty war system: a `WAR` containing exactly one `CAMPAIGN`, one primary and one secondary objective per side, a closed six-objective catalogue (ATTRITION, INTERDICTION, BLOCKADE, AIR, DEFENCE, STRIKE), a closed nine-operation catalogue (RAID, ASSAULT, AIR_STRIKE, BLOCKADE, MISSILE_STRIKE, INTERCEPT, FORTIFY, BREAK_BLOCKADE, RESUPPLY), an 84-turn deadline with one 42-turn extension, deterministic power plus one seeded ±500 bp fortune roll, bounded strength and readiness losses (20% per battle, 60% per campaign), and a closed-six-term settlement object. The 34-row conflict register `B10-C01`–`B10-C34` resolves each inherited or research conflict by rule; the 25 architecture decisions are stated in §26.1. No map, province, tile, front, coordinate, distance, adjacency, border, territorial capture, unit movement, geographic supply or occupation exists anywhere in the design; **D-015** is preserved exactly (one national OP pool, military-only, refill to cap, non-transferable, reserved at acceptance, consumed at resolution, no per-war or shared pool), and no Alliance military command, delegation, shared OP, military treasury, member war declaration or automatic war drag is created.

**Pass 2 — complete rulebook and formula register.** B-10 has exactly 30 required sections and 188 rules. The register separates structural constants from provisional coefficients: every number is labelled **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** unless it is a structural zero, bound or integer rule, and the register is authoritative where its arithmetic diverges from rulebook prose (`WAR-177`, `WAR-178`). The 35 formulas cover upkeep, readiness, attack and defence power, ratio, fortune, battle tiers, losses, supply bundles, objectives, progress caps, OP costs, reparations and every other arithmetic path; each carries the 20 mandatory fields of `WF-002`. Upkeep coefficients that the rulebook had named without rates are defined once in `F-WR-003` (`ceil(total_strength × 5000/10000)` crowns, `200/10000` ammunition, `100/10000` gasoline), and the mixed-type attack formula is correctly expressed as a per-type sum in `WAR-077`/`F-WR-021`.

**Pass 3 — integration, registers and closure.** §27 disposes the complete 10A inheritance: 44 `WCR`, 20 `WQN`, 22 `WFQ`, 15 `WRK`, 12 `WFX`, 26 `WFC`, 16 `GAP` and 36 `WFH` items. `WFC` counts are **3 adopted, 13 adapted, 6 rejected, 2 not applicable, 1 replaced and 1 transferred = 26** (`WAR-173`); the five named GAP handoffs are closed by rule and only `GAP-13` is transferred; `WFH-D3` is the only handoff invariant amended (facility damage rejected, no city loss preserved); no conflict is closed by inventing evidence (`WAR-172`). The 40 new requirements **REQ-654–REQ-693** are Provisional, and **REQ-014** and **REQ-591** move from Deferred to Provisional because B-10 now specifies the design they depended on. The [requirements register](03_requirements_traceability.md) is **55 Approved / 620 Provisional / 17 Open / 1 Deferred / 0 Proposed = 693**. The [04 decisions register](04_approved_and_provisional_decisions.md) gains **DD-166–DD-190** and stands at **130 Approved / 51 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred = 190**. The [05 unresolved register](05_unresolved_design_decisions.md) is **27 Resolved / 4 Deferred / 18 Open = 49**, with **UD-032 Resolved by B-10 `WAR-025`–`WAR-028` / DD-185 (`B10-AD-20`)** and `UD-040`–`UD-049` still Open and owner-reserved.

**Files changed in this pass.** `docs/stage-2/17_warfare_and_settlements.md` (new); `docs/stage-2/17_warfare_formula_register.md` (new); `docs/stage-2/03_requirements_traceability.md` (40 rows added, two status changes, counts); `docs/stage-2/04_approved_and_provisional_decisions.md` (DD-166–DD-190, counts); `docs/stage-2/05_unresolved_design_decisions.md` (UD-032 resolved, counts); `docs/stage-2/06_stage_2_progress_log.md` (this entry); and the continuity set `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md` and `docs/ROADMAP.md`. **Not changed:** B-02–B-09 rulebooks and their registers, the 08/09/10A research reports, Stage 1 reports, `DECISIONS.md`, application code, schema, migrations, infrastructure and live-game data. No `D-` decision is added; **D-015** and **D-024** are preserved unchanged, and no fabricated `D-`/`DD-` ID, owner approval or P&W value is imported.

**Validation evidence (2026-11-03, focused).** Every command below was executed from the repository root with `PYTHONIOENCODING=utf-8`; the result shown is the actual output.

| Command | Result |
|---|---|
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 634` — `PASS: all B-10 structure, disposition, formula, register and boundary checks` |
| `python docs/qa_backups/09_validate.py` | `359/359 checks passed` — `ALL CHECKS PASSED` |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943` — `PASS` |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `All 34 semantic checks passed with no review findings` |
| `python docs/qa_backups/test_next_action.py` | `Ran 25 tests` — `OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests` — `OK` |
| `python docs/qa_backups/verify_politics_numbers.py` | `879/879 checks passed` |

During the pass, five summary rows in §27.1 were found to disagree with the verdicts in §27.2–§27.9 (`WCR`, `WFQ`, `WFX`, `WFC`, `GAP`), and `WAR-170` said eight where seven rows are **not applicable**; each was corrected in the rulebook against the row-level verdicts, and the focused validator now checks the summary against those rows so the mismatch cannot recur. **Not run:** no gameplay, battle, declaration, settlement, reroll, block, P5-recovery, database, browser, security, load or live-integration test; no simulation or balance run; no Prompt 10C acceptance suite. None is claimed.

**Owner decisions.** **`UD-032` is resolved as Option A** on the evidence of the [10A §28 option analysis](research/10A_politics_and_war_warfare_research.md) and B-03's existing `RRL-021` block: the reroll block is retained, it covers pending, active, suspended and settling campaigns, and surrender is the off-ramp. **No other owner-reserved decision is touched:** `UD-040`–`UD-049` remain **Open / Yes — owner**, the Alliance military boundary and ARL credit-only rules are unchanged, and B-10 approves no owner policy.

**Limitations.** Documentation only. Every coefficient is provisional pending Prompt 14 calibration; no simulation, playtest, load, security or runtime test exists; the 10C workflow suite does not exist; no number is validated and no P&W value is adopted as a Nation Supremacy value. The rulebook is specification-complete, not implementation-complete.

**Next action.** **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence** — is the next official task and has not started. Its canonical deliverable is `docs/stage-2/17_warfare_workflows_acceptance.md`; B-10 §29 is its handoff, and it may not invent architecture or reopen a B-10 decision.

## 59. Prompt 10B-C — Final warfare correction, military Food upkeep, city infrastructure damage and acceptance closure (2026-11-04)

**Status.** **Prompt 10B-C is COMPLETE at the specification/documentation level.** It corrects B-10 in place and adds the two authorized features — recurring **military Food upkeep** and **city-targeted infrastructure damage** — without restarting the warfare design, creating a replacement project, renumbering an existing ID, deleting valid evidence or reopening an accepted decision. The canonical deliverables remain [B-10 — Warfare, campaigns, military operations and settlements](17_warfare_and_settlements.md) (**v1.1**, 30 sections, 188 numbered `WAR-` rules plus 38 lettered sub-rules) and the [B-10 formula register](17_warfare_formula_register.md) (**v1.1**, **39 formulas** `F-WR-001`–`F-WR-039`). It is **not** implementation, runtime testing, numeric approval, balance evidence or release. **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence — is next and has not started; Stage 2 is not complete.**

**Pass 1 — military Food upkeep and B-04 integration.** B-10 now charges a recurring military Food ration every turn at **P3.7 rank 6(a)**, before readiness upkeep 6(b), settlement 6(c) and other obligations 6(d). Quantity is derived from soldier-equivalents, not strength points: `ration_equivalents = Σ_t (strength_points_t × e_t)` with `e_t` = 10 infantry, 4 armour, 2 air and 20 naval, and `military_food_demand = ceil(ration_equivalents / 1000)` (`WAR-053a`–`WAR-053k`, `F-WR-036`). The rules place civilian Food at P3.6 ahead of every military obligation, charge the ration from **unreserved** Food only, cancel the whole obligation under `ECN-106` when unreserved Food is short (`RATION_SHORT`, `WRF-35`), leave no negative inventory and no debt, and apply a bounded readiness consequence with recovery; political `TRANSITION`/`CRISIS` grants no exemption. The ration is distinct from `OP-09 RESUPPLY` operational rations, cannot be double-counted, and every rate is labelled **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. B-04 is revised in place to **v1.9**: `ECN-019`/`ECN-028` record Food as a military sink; `ECN-081`–`ECN-084` correct consumption to P3.6; `ECN-105`, `ECN-144`, `ECN-145` and `ECN-152` place the ration at P3.7 6(a) and readiness at 6(b); `ECN-214` hands quantity and consequence to B-10. No tax, production, maintenance, reservation or ledger coefficient changed. Requirements **REQ-694–REQ-698** are added, and the ten-point Food integration matrix is `WAR-163a`.

**Pass 2 — city targeting, infrastructure damage and B-05 integration.** `OP-05 MISSILE_STRIKE` is now a valid city-targeting operation against a B-05 city identity, subject to the canonical validator and to the campaign's objective and target rules. On attacker victory, `removed_raw = ceil(I × 500/10,000)` and `removed = min(removed_raw, 20, campaign_headroom, I − 10)`, so infrastructure can never fall below the absolute floor of 10 or exceed a 20-level per-strike cap or the 30%-of-campaign-start headroom (`WAR-109a`–`WAR-109f`, `F-WR-037`). Capacity and housing are then recalculated from the new level (`10 + floor(I/10)`; `45,000 + 100 × I + 25,000 × civic_centres`), an over-capacity city enters `CAPACITY_OVERDRAWN`, facilities are preserved untouched, and fixed-asset book value is impaired by `floor(city_book_value_before × removed / I)` (`WAR-109g`, `F-WR-038`). *(10B-C2 supersedes this basis: §60 and B-05 `URB-118a`/`URB-118b` replace `city_book_value_before` with the infrastructure-only carrying value; the arithmetic above is the 10B-C snapshot, preserved as history.)* Repair is an ordinary P4.1 capex order at `Σ_{j=I}^{I+n−1}(8 + floor(j/10))`, bounded by `min(10, 500 − I, unrepaired_levels)`; because construction is P4.1 and damage is P5, a repair and a strike in the same turn resolve in that order and cannot repair damage not yet inflicted (`WAR-109h`–`WAR-109l`, REQ-703). No city is captured, transferred or deleted; no facility is damaged or destroyed; no direct population casualty exists. B-05 is revised in place to **v1.6** with the sole warfare effect, and `URB-157` is amended for infrastructure damage only, every other protection preserved. Requirements **REQ-699–REQ-703** are added, and the ten-point city integration matrix is `WAR-163b`.

**Pass 3 — OP, reservation, validator, political and modifier corrections.** The OP pool is corrected from a P0-refilled stored counter to a **turn-scoped derived ledger** that opens at the P7 close of the prior turn only after every reservation is terminal, verifies `reserved = 0`, and performs no OP mutation at P0, P3 or acceptance beyond the `HELD` reservation (`WAR-005a`, `WAR-039`–`WAR-043b`, `F-WR-001`/`F-WR-002`). D-015 is preserved exactly: one national, military-only, non-transferable, non-purchasable pool, reserved at acceptance while the turn is OPEN and consumed at P5 resolution, with no per-war, per-campaign, shared or Alliance pool. The hostile validator is one canonical **twelve-check, fail-closed** procedure run at submission, P2 and immediately before P5 (`WAR-009a`–`WAR-009f`); it treats B-08 `DP-T01` as **declaration-only**, applies B-09 same-Alliance and `AT-E01` protections, uses `AUD-AL-017` only for a B-09 block, admits no city-target bypass, and moves no OP or resource when any check blocks. Political `TRANSITION`/`CRISIS` is implemented mechanically in ten scenarios (`WAR-053j`/`WAR-053k`): no new order reserves, an accepted defensive commitment still resolves, an accepted offensive order fails at the first later check and releases everything, war does not pause and nothing is retroactively revived. Protection expiry between P2 and P5 is governed by **execution-time state**, not a stale P2 snapshot (`WAR-116a`). Supply denial and blockade are combined once, additively and before rounding into one capped surcharge — 25% for either, **50% for both, never 56.25%** — in `WAR-071`/`WAR-071a`/`WAR-072` and `F-WR-039`. Espionage is recorded honestly as excluded and **unassigned**: no owner is identified for any current or future prompt (§13.3, `B10-AD-24`, `B10-C30`, `WQN-19`).

**Pass 4 — dispositions, conflicts and registers.** Every conflict entry was reviewed against the rule that now implements its resolution. `WCR-01` describes the twelve-check validator; `B10-C26` is repaired for the political state; `B10-C30` and `WQN-19` record espionage as excluded with no owner; `WQN-12` is Provisional under `F-WR-037`; `WFC-13`, `WFC-19`, `WCR-25`, `WQN-15`, `WFX-04`, `GAP-08`, `WFH-D3`, `B10-AD-16`, `B10-AD-21`, `B10-C23` and `B10-C25` were corrected where the correction changed their disposition. The §27.1 summaries now match the row-level verdicts: `WQN` **17 / 1 / 2**, `WFC` **3 adopted, 14 adapted, 5 rejected, 2 not applicable, 1 replaced, 1 transferred = 26**, `WFX` **4 carried, 1 context, 2 irrelevant, 3 closed by design, 1 applied, 1 open = 12**, and `GAP` **8 closed by design, 3 closed as irrelevant, 1 transferred, 4 open = 16**. History is preserved: no verdict row is deleted, no `B10-C` ID is renumbered, and no conflict is closed by inventing evidence (`WAR-172`).

**Registers and counts.** The [requirements register](03_requirements_traceability.md) is **55 Approved / 630 Provisional / 17 Open / 1 Deferred / 0 Proposed = 703**, with **REQ-694–REQ-703** added and **REQ-654, REQ-664, REQ-676, REQ-678, REQ-681, REQ-686 and REQ-689** updated in place to match the corrected rules. The [04 decisions register](04_approved_and_provisional_decisions.md) is unchanged at **130 Approved / 51 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred = 190**, with **DD-179**, **DD-181** and **DD-186** amended in place. The [05 unresolved register](05_unresolved_design_decisions.md) is unchanged at **27 Resolved / 4 Deferred / 18 Open = 49**; **UD-032 remains resolved as Option A**, `UD-040`–`UD-049` remain **Open / owner-reserved**, and no owner decision was taken by this pass.

**Files changed in this pass.** `docs/stage-2/17_warfare_and_settlements.md` (v1.1: Food, city damage, validator, political, protection, modifier, espionage and the corrected dispositions); `docs/stage-2/17_warfare_formula_register.md` (v1.1: `F-WR-036`–`F-WR-039`); `docs/stage-2/10_economy_resources_treasury_and_finances.md` (v1.9: B-04 Food integration); `docs/stage-2/11_cities_infrastructure_production_and_research.md` (v1.6: the sole warfare effect); `docs/stage-2/03_requirements_traceability.md` (v1.31: ten rows, seven in-place updates, counts); `docs/stage-2/04_approved_and_provisional_decisions.md` (v3.13: three in-place updates, counts unchanged); `docs/stage-2/06_stage_2_progress_log.md` (this entry); the continuity set `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md` and `docs/ROADMAP.md`; and the QA tools `docs/qa_backups/10B_validate_warfare.py`, `09_validate.py`, `validate_final.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `verify_city_numbers.py` and `verify_economy_numbers.py`. **Not changed:** B-02, B-03, B-06, B-08 and B-09 rulebooks and registers, the 08/09/10A research reports, Stage 1 reports, `DECISIONS.md`, application code, schema, migrations, infrastructure and live-game data.

**Validation evidence (2026-11-04).** Every command below was executed from the repository root with `PYTHONIOENCODING=utf-8`; the result shown is the actual output. The B-10 validator now also executes **34 mandatory negative fixtures** (every one must be rejected), **one clean fixture** (`CF-01`, hand-computed: 120 → 114 infrastructure, capacity 21, housing 81,400, impairment 12,000, repair 114, bundle 5 → 7 under +25%) and **12 structured semantic evidence records** whose anchors and fixture coverage are checked.

| Command | Result |
|---|---|
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 779` — `Negative fixtures: 34/34 rejected; clean fixture CF-01 PASS; semantic evidence records: 12` — `PASS` |
| `python docs/qa_backups/09_validate.py` | `359/359 checks passed` — `ALL CHECKS PASSED` |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943` — `PASS` |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `All 34 semantic checks passed with no review findings` |
| `python docs/qa_backups/test_next_action.py` | `Ran 25 tests` — `OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests` — `OK` |
| `python docs/qa_backups/verify_politics_numbers.py` | `879/879 checks passed` |
| `python docs/qa_backups/verify_city_numbers.py` | `267/267 checks passed` |
| `python docs/qa_backups/verify_economy_numbers.py` | `164/164 checks passed` |
| `python docs/qa_backups/verify_alliance_numbers.py` | `375 passed` |
| `python docs/qa_backups/verify_alliance_workflows.py` | `49 workflows, 65 edge cases, 132 tests` — `ALL CHECKS PASSED` |

**Limitations.** Documentation and documentation-validator evidence only. Every coefficient added by this pass is provisional pending Prompt 14 calibration; no simulation, playtest, balance, load, security, database, browser or live-integration test exists; the Prompt 10C workflow and acceptance suite does not exist; no number is approved and no P&W value is adopted as a Nation Supremacy value. The rulebook is specification-complete, not implementation-complete.

**Owner decisions.** No owner-reserved decision was touched. **`UD-032` remains resolved as Option A**; **`UD-040`–`UD-049` remain Open / owner-reserved**; B-10 approves no owner policy and no `D-` decision was added to `DECISIONS.md`.

**Next action.** **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence** — is the next official task and has not started. Its canonical deliverable is `docs/stage-2/17_warfare_workflows_acceptance.md`; B-10 §29 is its handoff, and it may not invent architecture or reopen a B-10 decision.

---

## 60. Prompt 10B-C2 — Final semantic closure: protected Food, force snapshot, defensive commitments, infrastructure accounting, repair timing and crowding (2026-11-04)

**Status.** **Prompt 10B-C2 is COMPLETE at the specification/documentation level.** It is a narrow correction pass on B-10 and its companion systems. It does not restart Prompt 10B, begin Prompt 10C, implement gameplay, renumber an ID, delete history, resolve an owner-reserved decision or approve a number. The canonical deliverables remain [B-10](17_warfare_and_settlements.md) (**v1.2**, 30 sections, 188 numbered `WAR-` rules plus **42** lettered sub-rules) and the [B-10 formula register](17_warfare_formula_register.md) (**v1.2**, **39 formulas**, no formula added or renumbered). The seven specified defects are closed against their authoritative B-02/B-04/B-05/B-06 sources.

**Defect 1 — protected civilian Food and the `OP-09` reservation.** `WAR-053l` defines `protected_civilian_food = food_demand`, accepts an `OP-09` field ration only from `eligible_op09_surplus` above that requirement, re-tests the actual stock at P3.6, and releases reservations in reverse acceptance order until the requirement is met; a released action fails whole with `WRF-25`. `WAR-053c`/`WAR-053f` forbid taking protected Food, and `WAR-053g` keeps the recurring and operational rations as two separate charges. B-04 is reconciled: **ECN-081**/**ECN-082** publish `food_after_other`, `available_if_held`, `food_after_other − op09_held_after_release`, `food_consumed` and `unmet_food`; **ECN-108** publishes the carrying-value aggregation; **F-EC-003** carries the same variables. Six worked cases cover acceptance, sufficient surplus, other reservations, stale population, a P3.7 plus `OP-09` turn, and the release path.

**Defect 2 — P3.0 removed and one force snapshot.** `WAR-053m` removes the undefined `P3.0`. B-10 declares one step at the opening of P3.7 inside the authorized subphase, materialises recruitment whose completion turn has arrived, and stores one immutable snapshot. `WAR-050`, `WAR-053b`, `WAR-058`, `F-WR-003` and `F-WR-036` all read that snapshot; current-turn P4 recruitment, pending, cancelled, failed and P5-lost strength are excluded. The P5 force differs only by voluntary P4 disbanding, stated as an explicit, justified difference. Six worked cases cover recruitment arrival, training turns, pending and cancelled orders, P5 losses and the next turn's obligations.

**Defect 3 — accepted defensive commitments across `TRANSITION`/`CRISIS`.** Row 8 continues to deny **new** actions. `WAR-009c` and `WAR-009g` add a narrow P2/pre-P5 exemption for a commitment that meets all seven conditions (accepted before the state began, recorded `action_id`, still held, `defensive = TRUE`, resources still reserved, not expired, valid target). Submission has **no** exception, and only row 8 is exempt: checks 1–7 and 9–12 continue independently and cumulatively, so a B-03/B-09 block still rejects the same commitment. `B10-C26` carries the eight-scenario table; `WAR-053k` states the same boundary. `REQ-666` records the exemption.

**Defect 4 — infrastructure-only asset accounting.** `WAR-109g` and `WAR-109m`, with B-05 `URB-118a`/`URB-118b`, replace the undefined `city_book_value_before` with a per-city subledger: gross capitalised upgrade lots, accumulated impairment and carrying value. The 50-level capital and the 10-level new city are a **zero-cost opening lot**; facilities and other assets are excluded and never impaired; `fixed_asset_book_value = Σ infrastructure_carrying_value + Σ other recognised assets` (ECN-108, F-CI-019). Impairment is `min(carrying_before, floor(carrying_before × removed / I_combat))`, never exceeds carrying value, reads the post-impairment value on repeated damage and is idempotent on `damage_event_id = (turn_id, strike_action_id, city_id)`. The worked case proves the facility stays 5,000 while carrying moves 130 → 124 → 163 → 155.

**Defect 5 — repair cost and capitalisation.** `WAR-109h` uses exactly B-05's `URB-043` stepped sum `Σ_{j=I}^{I+n−1}(8 + floor(j/10))` and the single `URB-044` Civil Survey ceiling; it adds **no** material charge, no second discount and no parallel repair formula. Crowns are reserved at acceptance and charged as capex at P4.1; the spend capitalises one new lot, leaves accumulated impairment unchanged and never reverses it; the event is keyed on `order_id` and a replay applies nothing. A failed or cancelled repair heals nothing and releases once. `B10-C21` now states **two distinct paths, never one pool** — military recovery and city infrastructure repair are not interchangeable.

**Defect 6 — P4.1/P5/next-turn boundaries.** `WAR-109m` names the authoritative values (`I_open`, `I_pre`, `I_post_P4_1`, `I_combat`, `I_post_P5`, `capacity_construction(T)`, `capacity_effective(T+1)`, `housing_population(T)`, `housing_effective(T+1)`, `BV_post_P4_1`, `BV_post_P5`). P5 combat reads the physical post-P4.1 level; construction capacity reads the opening level in T and the post-P5 level in T+1; population housing reads the opening level at P3.8 and the post-P5 level in T+1; national wealth at P3.8 reads the prior turn's written book value. B-05 `URB-046` is rewritten to the same boundaries, so "available next turn" and the same-turn strike are reconciled rather than contradictory. Seven timing cases cover repair alone, repair plus a strike, interception, construction before/after damage, two strikes and an interrupted retry.

**Defect 7 — housing and B-06 crowding.** `WAR-109f`/`WAR-109m` and B-06 `DMP-031a` make infrastructure damage a **housing-source change**, not a casualty rule: no kill, eviction, deletion, movement or transfer at P5. The reduced `housing_effective(T+1)` is read at the next P3.8, where `DMP-034` settles population once and `DMP-031` applies `decline = max(ceil(excess/10), max(0, population − natural))` with the 1,000 floor. The numerical case (50,000 people, housing 49,000, `growth_bp` 50 → decline 100 → 49,900; natural 49,500 → decline 500) shows the crowding path; repair restores housing at the same boundary and crowding stops. `F-PD-011` reads the named housing input.

**Registers, conflicts and handoff.** `B10-C17` now states rank 6 sub-order **(a) military Food, (b) readiness, (c) settlement, (d) other military obligation**. `B10-C30` and `WAR-166` classify espionage as **EXCLUDED FROM CURRENT B-10 SCOPE — UNASSIGNED FUTURE-SCOPE CANDIDATE**, with no owner identified and nothing transferred. The project handoff §147 now records **city targeting with bounded, recoverable infrastructure damage** and states that city identity, existence and ownership, facilities and geography remain protected. Stale `WAR-109a`–`WAR-109l` ranges are corrected to `WAR-109m`; the dated 10B-C arithmetic in §59 is preserved with an inline supersession note rather than rewritten.

**Registers and counts.** The [requirements register](03_requirements_traceability.md) is v1.32 and remains **55 Approved / 630 Provisional / 17 Open / 1 Deferred / 0 Proposed = 703**; seven B-10 rows (REQ-654, REQ-664, REQ-666, REQ-694–REQ-703 where applicable) are clarified in place and **no row is added, removed or renumbered**. The [04 decisions register](04_approved_and_provisional_decisions.md) is unchanged at **130 Approved / 51 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred = 190**; only DD-186's anchor range is corrected to `WAR-109m`. The [05 unresolved register](05_unresolved_design_decisions.md) is unchanged at **27 Resolved / 4 Deferred / 18 Open = 49**; **UD-032 remains resolved as Option A**, `UD-040`–`UD-049` remain **Open / owner-reserved**, and no owner decision was taken.

**Files changed in this pass.** `docs/stage-2/17_warfare_and_settlements.md` (v1.2: `WAR-009g`, `WAR-053l`/`WAR-053m`, `WAR-109f`–`WAR-109m`, `B10-C17`/`B10-C21`/`B10-C30`, `WAR-166`); `docs/stage-2/17_warfare_formula_register.md` (v1.2: `F-WR-016`, `F-WR-019`, `F-WR-036`, `F-WR-037`, `F-WR-038`); `docs/stage-2/10_economy_resources_treasury_and_finances.md` (v2.0: ECN-081/082/108); `docs/stage-2/10_economic_formula_and_balance_register.md` (v1.4: F-EC-003); `docs/stage-2/11_cities_infrastructure_production_and_research.md` (v1.7: URB-046, URB-118, URB-118a/118b, URB-157); `docs/stage-2/11_city_infrastructure_production_and_research_formula_register.md` (v1.3: F-CI-019); `docs/stage-2/12_population_and_domestic_politics.md` (v2.6: DMP-031, DMP-031a); `docs/stage-2/12_population_and_domestic_politics_formula_register.md` (v2.5: F-PD-011); `docs/stage-2/03_requirements_traceability.md` (v1.32); `docs/stage-2/04_approved_and_provisional_decisions.md` (v3.13, DD-186 anchor); `docs/stage-2/06_stage_2_progress_log.md` (this entry); the continuity set `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md` and `docs/ROADMAP.md`; and the QA tools `docs/qa_backups/10B_validate_warfare.py`, `validate_final.py`, `verify_city_numbers.py`, `verify_economy_numbers.py`, `test_09A_alliance_validator.py` and `verify_market_workflows.py`. **Not changed:** B-02, B-03, B-08 and B-09 rulebooks and registers, the 08/09/10A research reports, Stage 1 reports, `DECISIONS.md`, application code, schema, migrations, infrastructure and live-game data.

**Validation evidence (2026-11-04).** Every command below was executed from the repository root; the result shown is the actual observed output. The B-10 validator now executes **58 mandatory negative fixtures** (all rejected), **one clean fixture** (`CF-01`, hand-computed and separately traced to 19 canonical sentences covering every §13.2 bullet) and **19 structured semantic evidence records** — 12 area summaries plus **7 full ten-field records**, one per 10B-C2 defect, each checked for non-empty fields, resolving anchors and `expected == actual`. The 10B-C figures in §59 (779 / 34 / 12) are that pass's snapshot; this pass supersedes them.

| Command | Result |
|---|---|
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 980` — `Negative fixtures: 58/58 rejected; clean fixture CF-01 PASS; semantic evidence records: 12 summaries + 7 full` — `PASS` |
| `python docs/qa_backups/09_validate.py` | `359/359 checks passed` — `ALL CHECKS PASSED` |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943` — `PASS` |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `All 34 semantic checks passed with no review findings` |
| `python docs/qa_backups/verify_economy_numbers.py` | `164/164 economy arithmetic checks passed` |
| `python docs/qa_backups/verify_city_numbers.py` | `267/267 city arithmetic checks passed` |
| `python docs/qa_backups/verify_politics_numbers.py` | `879/879 checks passed` |
| `python docs/qa_backups/verify_alliance_numbers.py` | `375 passed, 0 failed` |
| `python docs/qa_backups/verify_alliance_workflows.py` | `49 workflows, 65 edge cases, 132 tests` — `ALL CHECKS PASSED` |
| `python docs/qa_backups/test_next_action.py` | `Ran 25 tests` — `OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests` — `OK` |
| `python docs/qa_backups/test_09A_alliance_validator.py` | `Ran 43 tests` — `OK` |
| `python docs/qa_backups/verify_diplomacy_numbers.py` | `9 groups checked`, `0 failed` |
| `python docs/qa_backups/verify_diplomacy_workflows.py` | `17 groups checked`, `0 failed` |
| `python docs/qa_backups/verify_market_numbers.py` | `ALL CHECKS PASSED` |
| `python docs/qa_backups/verify_market_workflows.py` | `ALL CHECKS PASSED` |
| `python docs/qa_backups/09_register_counts.py` | exit 0 |

**Validator expectation updates.** Four QA expectations lagged the intentional document edits and were updated, not bypassed: `validate_final.py` now expects B-05 v1.7 and B-06 register v2.5; `verify_city_numbers.py` expects B-05 v1.7 and its register v1.3; `verify_economy_numbers.py` expects B-04 v2.0 and its register v1.4; `test_09A_alliance_validator.py` mutates the current `stage_2_next_prompt: 10C`; `verify_market_workflows.py` accepts the ROADMAP wording "Prompt 08 is complete". No rule, formula, threshold or decision was changed to make a check pass.

**Not applicable / known stale.** `08_sweep.py` is a Stage-1 script that crashes on `TypeError: unhashable type: 'list'`; `08_sweep2.py` retains the Stage-1 invariant "no new D-007+ rows", which later stages intentionally superseded — its own historical result file already records that line as FAIL before this pass. Neither is a B-10, B-02, B-03, B-04 or B-05 acceptance test, and neither was altered.

**Limitations.** Documentation and documentation-validator evidence only. Every coefficient added or reused by this pass is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. No simulation, playtest, balance, load, security, database, browser or live-integration test exists; the Prompt 10C workflow and acceptance suite does not exist. The semantic records prove that the written rules, formulas, worked examples and companion documents agree; they do not prove an implementation matches them.

**Owner decisions.** No owner-reserved decision was touched. **`UD-032` remains resolved as Option A**; **`UD-040`–`UD-049` remain Open / owner-reserved**; B-10 approves no owner policy and no `D-` decision was added to `DECISIONS.md`.

**Next action.** **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence** — is the next official task and has not started.

---

## 61. Prompt 10B-C3 — Operations Point regeneration, turn-phase reconciliation, project-wide link repair and handoff closure (2026-11-04)

**Status.** **Prompt 10B-C3 is COMPLETE at the specification/documentation level.** It is the final consistency correction after 10B-C2. It does not restart Prompt 10B, begin Prompt 10C, implement gameplay, renumber an ID, change an operation cost or cap value, rewrite a battle or settlement rule, reopen an owner-reserved decision, or delete history. The canonical deliverables are [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) **v1.6**, [B-10](17_warfare_and_settlements.md) **v1.3**, the [B-10 formula register](17_warfare_formula_register.md) **v1.3**, [D-015](../DECISIONS.md) as amended in place, the [04 register](04_approved_and_provisional_decisions.md) **v3.14**, and the [requirements register](03_requirements_traceability.md) **v1.33**. No phase, rule identifier or numeric value was added.

**OP decision — four models compared.** The audit examined (A) one OP at each turn boundary up to the cap, (B) a full refill to the cap at each boundary, (C) a full refill only at P3, and (D) a P7 period opening. **Model A was adopted**, because B and C are per-turn resets that make saving impossible and let a nation spend the whole cap every turn; D moves the write into the settle/publish phase and creates a second boundary. Model A keeps scarcity, makes recovery linear, rewards banking, still allows a meaningful opening burst after several quiet turns, and prevents perpetual maximum-rate spending. The audit found that D-015's "refilled to its cap" wording conflated the **rate** with the **cap**; the cap and the one-point rate are now separate properties and are calibrated together by Prompt 14.

**Canonical lifecycle.** There is exactly one national, military-only, non-transferable pool with no per-war, per-campaign, per-shared or Alliance pool and no general action budget. The internal state is a persistent `op_balance`; `reserved` is the sum of live `HELD` items; `available = max(0, op_balance − reserved)`. Acceptance while the turn is OPEN writes one `HELD` and reserves economic resources. At the **opening of P3.7, once per successful boundary**, the nation writes `op_balance = min(op_cap, op_balance + 1)` and exactly one `REGENERATED` item keyed `(nation_id, turn_id)`, including a recorded `0` at the cap. P0 writes no OP mutation; P7 performs no regeneration, releases unresolved actions under `WAR-043`, verifies `reserved = 0` and publishes the turn; newly regenerated OP becomes spendable only when the next OPEN window begins after P7 publication. Failure, cancellation or expiry writes one `RELEASED` and restores availability without refunding the balance; P5 success writes one `CONSUMED` and debits `reserved` and `op_balance` exactly once. A duplicate boundary or action key returns the original receipt and writes nothing. Dormancy, protection and political-state rules are never bypassed. The cap remains **10 (PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED)**; the rate is structural at +1; operation costs remain the closed 1–4 OP table and are unchanged.

**Worked examples.** B-10 §8.1 supplies one full worked accounting plus **twelve** event-identified examples (`R(T)`, `H(A)`, `C(A)`, `X(A)`) covering zero balance, one below cap, at cap, reservation across the boundary, multiple accepted operations, resolution after the boundary, cancellation, failed P5 processing and retry, duplicate boundary processing, a restricted political state, dormancy and reaching the cap with an old reservation outstanding. Every case ends with `0 ≤ available ≤ op_balance ≤ op_cap` and `reserved ≤ op_balance`; no case creates or loses a point without a recorded event.

**Cross-system reconciliation.** B-02 TR-005 now states the one-point P3.7 regeneration, cap enforcement, carry below the cap, the `available`/`reserved`/`op_balance` accounting and the next-OPEN-window spend gate; its P3 phase row records that the national OP balance may change at P3.7; §24 replaces the ambiguous Alliance "war-room scope" with the `AX-18`/`UD-049` coordination-notice boundary. B-10 §8.1, `WAR-039`–`WAR-043b`, `WAR-157`, `B10-C03`, `B10-C20`, `WCR-09`, `WCR-10`, `WQN-01`, `WQN-04`, `WFH-A3`, `F-WR-001` and `F-WR-002` carry the same model. D-015 is amended in place: its status marks the amendment, its notes prepend the dated owner-directed change and preserve the original text, and the original "refilled to cap / unused points do not bank" rate is explicitly superseded while every other property is unchanged. DD-033 is annotated in place, the 04 register is v3.14, and REQ-654/REQ-681 state the single P3.7 item and the persistent-pool formula. UD-018's resolved row records the amendment. No DD or D row was added, so the register totals are unchanged.

**Alliance and Prompt 13 boundary.** The war interface is the **Nation-owner War Operations Board** — nation-level, owner-only, B-10 visibility, never an Alliance surface. The Alliance receives a **restricted Alliance management interface**, which is not a war room: it carries membership, governance, tax, donation, treaty, receipt and audit functions and no military command, no member OP spending, no private war visibility, no shared pool and no delegation. `AX-18`, `UD-047`, `UD-049`, `REQ-589`–`REQ-591`, `WAR-148` and `WAR-161` are preserved. The roadmap, the Bible outline, B-08 §1.3 and the closure audit use the corrected wording; **no Prompt 13 screen or journey was designed**.

**Markdown-link repair.** The project link validator found **89 unresolved links** across 64 Markdown files and 2,989 links (2,607 local, 382 external, 29 anchors). All 89 were corrected: **86** `stage-2/13_trade_and_markets.md` targets in `03_requirements_traceability.md` (now same-directory `13_trade_and_markets.md`), **one** `../04_approved_and_provisional_decisions.md` in `16_alliances_workflows_acceptance.md` (now `04_approved_and_provisional_decisions.md`), **one** `qa_backups/verify_market_numbers.py` in this log (now `../qa_backups/verify_market_numbers.py`), and **one** stale Stage-1 anchor `#appendix-c--change-log-for-this-pass` (now `#appendix-c--change-log-for-this-pass-2026-10-23`). The new [`validate_links.py`](../qa_backups/validate_links.py) resolves targets against the containing file, validates GitHub-style heading anchors and explicit HTML anchors, accepts URL-encoded spaces, existing scripts and directory links, skips HTTP/HTTPS and other external schemes, rejects paths that escape the repository root, and exits nonzero on any unresolved link. Its ten-fixture `--self-test` passes 11/11 checks (ten fixtures plus one aggregate count check). Final scan after every edit in this pass: **64 files, 2,998 links, 2,616 local, 382 external, 29 anchors, 0 unresolved**.

**Files changed in this pass.** `docs/stage-2/07_core_gameplay_loop_symbolic_world_and_turn_system.md` (v1.6: TR-005, P3 row, §24, revision history); `docs/stage-2/17_warfare_and_settlements.md` (v1.3: §8.1, `WAR-039`–`WAR-043b`, `WAR-157`, `B10-C03`, `WCR-09`/`WCR-10`, `WQN-01`/`WQN-04`, `WFH-A3`, handoff); `docs/stage-2/17_warfare_formula_register.md` (v1.3: `F-WR-001`, `F-WR-002`); `docs/DECISIONS.md` (D-015 amended in place); `docs/stage-2/04_approved_and_provisional_decisions.md` (v3.14: DD-033 annotation); `docs/stage-2/03_requirements_traceability.md` (v1.33: REQ-654, REQ-681, 86 link repairs); `docs/stage-2/05_unresolved_design_decisions.md` (UD-018 amendment note); `docs/stage-2/09_account_onboarding_nation_creation_and_progression.md` (v1.1: `NAT-018`, the creation-state OP row and the reroll-loss note reconciled with the cap start, the +1 regeneration and the below-cap carry; no other rule changed); `docs/stage-2/01_stage_2_prompt_roadmap.md` (Prompt 09/13 wording and boundary); `docs/stage-2/02_master_game_design_bible_outline.md` (B-09/B-13 wording); `docs/stage-2/15_diplomacy.md` (§1.3 scope row and header note); `docs/stage-2/08_final_decision_closure_audit.md` (Prompt 09 row); `docs/stage-2/11_cities_infrastructure_production_and_research.md` (URB-014 rate); `docs/stage-2/16_alliances_workflows_acceptance.md` (one link); `docs/stage-1/09_integrated_design_synthesis_and_readiness_audit.md` (one anchor); `docs/stage-2/research/08A_diplomacy_research.md` (a dated terminology note on the `A-09` interface row; no research content changed); the continuity set `docs/stage-2/00_stage_2_handoff.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md` and this log; and the QA tools `docs/qa_backups/10B_validate_warfare.py` and new `docs/qa_backups/validate_links.py`. **Not changed:** operation costs, the nine-operation catalogue, battle and settlement formulas, Food upkeep, B-05 infrastructure damage, D-122/DD-136/REQ-513 and the Global Trade gates, B-03 protection/reroll, B-04 Food/ledger, B-06 political states, B-08 diplomacy sovereignty, B-09 Alliance military sovereignty, and the 09/10A research reports (08A received only the dated terminology note recorded above).

**Registers and counts.** The requirements register remains **55 Approved / 630 Provisional / 17 Open / 1 Deferred / 0 Proposed = 703**; two rows are clarified in place and no row is added or renumbered. The 04 register remains **130 Approved / 51 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred = 190**. The 05 register remains **27 Resolved / 4 Deferred / 18 Open = 49**. **`UD-032` remains resolved as Option A**; **`UD-040`–`UD-049` remain Open / owner-reserved**; no owner decision was taken.

**Validation evidence (2026-11-04).** Every command below was executed from `docs/`; the shown output is the observed result. Structural, arithmetic, OP-scenario and semantic-review evidence only — no runtime, database, browser or live-integration test exists.

| Command | Result |
|---|---|
| `python qa_backups/10B_validate_warfare.py` | `Checks run: 1035` — `Negative fixtures: 73/73 rejected; clean fixtures CF-01 and CF-02 PASS; semantic evidence records: 13 summaries + 7 full` — `PASS` |
| `python qa_backups/09_validate.py` | `359/359 checks passed` — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python qa_backups/09A_validate_alliance.py` | `Checks run: 943` — `PASS` |
| `python qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed with no review findings.` |
| `python qa_backups/verify_economy_numbers.py` | `164/164 economy arithmetic checks passed` |
| `python qa_backups/verify_city_numbers.py` | `267/267 city arithmetic checks passed` |
| `python qa_backups/verify_politics_numbers.py` | `879/879 checks passed` |
| `python qa_backups/verify_alliance_numbers.py` | `375 passed, 0 failed` |
| `python qa_backups/verify_alliance_workflows.py` | `49 workflows, 65 edge cases, 132 tests` — `ALL CHECKS PASSED` |
| `python qa_backups/verify_diplomacy_numbers.py` | `9 groups checked`, `0 failed` |
| `python qa_backups/verify_diplomacy_workflows.py` | `17 groups checked`, `0 failed` |
| `python qa_backups/verify_market_numbers.py` | `ALL CHECKS PASSED` |
| `python qa_backups/verify_market_workflows.py` | `ALL CHECKS PASSED` |
| `python qa_backups/test_next_action.py` | `Ran 25 tests` — `OK` |
| `python qa_backups/test_decision_registers.py` | `Ran 12 tests` — `OK` |
| `python qa_backups/test_09A_alliance_validator.py` | `Ran 43 tests` — `OK` |
| `python qa_backups/09_register_counts.py` | exit 0 |
| `python qa_backups/validate_links.py --self-test` | `11/11 checks passed` (ten fixtures plus the aggregate count check) |
| `python qa_backups/validate_links.py` | `64` files, `2,998` links, `2,616` local, `382` external, `29` anchors, `0` unresolved |

**Bounded test and known-stale record.** `test_09B_alliance_semantic_validator.py` contains 267 tests and is slow because each test re-reads the corpus. A bounded 240-second run reached `test_115` with every completed test passing; a longer bounded run under a 900-second `timeout` reached `test_187` with **105 tests reported `... ok`, 0 failures and 0 errors** before the timeout stopped it (`exit=124`). Neither is a completed suite, so this file is **not reported as passing**; the fast `09B_validate_alliance_semantic.py` (34 checks) covers the same C25 rules and passes. `08_sweep.py` still crashes on `TypeError: unhashable type: 'list'`; `08_sweep2.py` still reports `26/27` because its Stage-1 invariant "no new D-007+ rows" was intentionally superseded. Neither is a current acceptance test and neither was altered.

**Limitations.** Documentation and documentation-validator evidence only. No gameplay implementation, migration, deployment, runtime test, load test, security test, browser test or live-game integration test exists; the Prompt 10C workflow and acceptance suite does not exist. The cap (10), all operation costs and all readiness/calibration values remain **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**; the +1 rate is structural but must be calibrated together with the cap. The semantic evidence proves that the written rules, formulas and companion documents agree; it does not prove an implementation matches them.

**Next action.** **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence** — is authorized by the roadmap as the next task and has not started. Its canonical deliverable is `docs/stage-2/17_warfare_workflows_acceptance.md`; it must not invent campaign architecture, OP economics, battle formulas, operation costs, settlement logic or permissions. **Prompt 14 owns all numeric calibration.** This pass is documentation-only and makes no implementation, balance or production claim.

---

## 62. Prompt 10B-C4 — Final handoff status synchronization, continuity and acceptance closure (2026-11-04)

**Status.** **Prompt 10B-C4 is COMPLETE at the documentation level, and Prompt 10B-C3 is now verified and marked PASS at the specification/documentation level.** This pass changes no warfare rule, no operation cost, no cap value, no OP regeneration rate, no phase boundary, no reservation or consumption rule, no B-02/B-03/B-04/B-05/B-06/B-08/B-09 content, and no Global Trade scope or gate. It does not begin Prompt 10C, design Prompt 13 screens, or implement anything. It corrects stale current-status summaries in the continuity set so that every handoff describes one verified state.

**What was inconsistent.** Four current-status records lagged the documents they summarise, and two metadata lines were stale:

| File | Previous state / inconsistency | Correction made | Reason |
|---|---|---|---|
| `docs/stage-2/00_stage_2_handoff.md` | Opening `10B status (2026-11-03)` block described B-10 as pre-correction, with no version, no OP model, no C/C2/C3 and no link repair, while the `Revised` line and the detailed next-task paragraph described all three passes and v1.3 | Opening block rewritten to the current state: 10B complete plus 10B-C/C2/C3 verified, B-10 v1.3 and formula register v1.3, the +1 P3.7 OP model, the link repair, no runtime claim, 10C next | The opening summary and detailed handoff must not state different completion states |
| `docs/stage-2/00_stage_2_handoff.md` | State table row for B-10 said **v1.2** | Row now says **v1.3**, with the three correction passes listed | Version must match the canonical file |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 10 row stopped at 10B-C2, gave B-10 **v1.2** and its register **v1.2**, and omitted 10B-C3 | Row now records 10B-C3 complete and verified PASS, B-10 v1.3 and register v1.3, the OP model, the link repair and 10C not started | Roadmap must match the verified state |
| `docs/stage-2/02_master_game_design_bible_outline.md` | Header recorded B-10 **v1.1** and 38 lettered sub-rules; the "Prompts executed" and "Next prompt" rows stopped at 10B-C; the Bible-status row still listed B-10 among Planned sections | Header is v1.12 and records B-10 v1.3 / 42 lettered sub-rules / three correction passes; both status rows include 10B-C2 and 10B-C3; B-10 is now described as drafted at the specification level, with 7 sections remaining Planned | The outline is a current-status index and cannot contradict the rulebook |
| `docs/PROJECT_PROGRESS.md` | Stage table row 10 said B-10 **v1.2** and ended at 10B-C2 | Row now says **v1.3**, adds 10B-C3 complete and **PASS**, points to log §§61–§62 and states the OP model and link repair; the historical header paragraph was already current and was left in place | The stage tracker is the primary reader-facing status |
| `docs/AI_CONTEXT.md` | The Stage-2 `Status` paragraph and the `Last updated` paragraph both ended at "Prompt 10B specification complete" with no correction sequence | Both now name 10B-C/C2/C3 complete and verified, B-10 v1.3, register v1.3 and the +1 P3.7 OP model; both still say 10C next and not started, and the document keeps the specification-versus-runtime distinction | The primary stage-plan summary must not lag the detailed handoff |
| `docs/AI_HANDOFF.md` | The 10B narrative paragraph stopped at §58 with no B-10 version and no correction passes, although the header block was current | Paragraph now records 10B-C/C2/C3 verified, B-10 v1.3 and register v1.3, the OP model, the link repair and the provisional-number status | Current handoff paragraphs must agree with the header |
| `docs/DECISIONS.md` | `Last updated` said 2026-11-03, although D-015 was amended on 2026-11-04 and DD-033 annotated the same day | `Last updated` is now 2026-11-04 with a dated note on the D-015 amendment and the DD-033 annotation; the 2026-11-03 Phase 09B acceptance text is preserved verbatim after it | The register's own metadata must be accurate; no decision meaning changed |
| `docs/ROADMAP.md` | `Last updated` said 2026-11-03 although the file was modified on 2026-11-04 | `Last updated` is now 2026-11-04 with the verified B-10 v1.3 / OP / link-repair state, 10C next and the unchanged Global Trade gates | Same reason; no dependency or scope changed |

**Nothing else was changed.** The authoritative [B-10](17_warfare_and_settlements.md) v1.3 text, its [formula register](17_warfare_formula_register.md) v1.3, B-02 v1.6, the requirements register v1.33, the 04 register v3.14, the 05 register and D-015's decision text are untouched by this pass. The 10B-C3 §61 entry is preserved unaltered; §62 is added, not substituted.

**OP design preservation.** The verified canonical statement remains: one national military-only non-transferable pool; `op_balance` persistent; `available = max(0, op_balance − reserved)`; **+1 OP at the opening of P3.7, once per successful boundary**, `op_balance = min(op_cap, op_balance + 1)`, one idempotent `REGENERATED` item keyed `(nation_id, turn_id)` including a recorded 0 at the cap; P0 and the P7 close never regenerate; acceptance reserves, resolution consumes once, failure/cancellation/expiry releases without refunding; cap 10 and costs 1–4 unchanged and **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**; no per-war, per-campaign, shared or Alliance pool; P3.7 precedes P5 resolution under the documented phase model. No wording in this pass alters any of these.

**Validation evidence (2026-11-04).** Every command below was run from the repository root; the shown text is the observed output.

| Command | Result |
|---|---|
| `python docs/qa_backups/validate_links.py` | `Markdown files scanned: 64`; `Links found: 3009`; `Links checked locally: 2627`; `External links skipped: 382`; `Anchors checked: 29`; `Unresolved: 0` (final scan after this entry was written) |
| `python docs/qa_backups/validate_links.py --self-test` | `Link-validator self-test: 11/11 checks passed` |
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 1035`; `Negative fixtures: 73/73 rejected; clean fixtures CF-01 and CF-02 PASS; semantic evidence records: 13 summaries + 7 full`; `PASS` |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python docs/qa_backups/09_validate.py` | `359/359 checks passed`; `ALL CHECKS PASSED` |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943`; `PASS` |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `All 34 semantic checks passed with no review findings` |
| `python docs/qa_backups/test_next_action.py` | `Ran 25 tests`; `OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests`; `OK` |
| `python docs/qa_backups/test_09A_alliance_validator.py` | `Ran 43 tests`; `OK` |
| `python docs/qa_backups/09_register_counts.py` | exit 0 |
| `python -m unittest` (repository root) | `Ran 0 tests`; `NO TESTS RAN`; exit 5 — no root-level discovery is configured; the project's test files are run individually above, and this command is therefore **not** reported as a passing suite |

**Regression evidence carried from the same verified state.** `verify_economy_numbers.py` 164/164; `verify_city_numbers.py` 267/267; `verify_politics_numbers.py` 879/879; `verify_alliance_numbers.py` 375 passed / 0 failed; `verify_alliance_workflows.py` 49 workflows / 65 edge cases / 132 tests PASS; `verify_diplomacy_numbers.py` 9 groups / 0 failed; `verify_diplomacy_workflows.py` 17 groups / 0 failed; `verify_market_numbers.py` and `verify_market_workflows.py` PASS, including the "no market release claim" guard. `test_09B_alliance_semantic_validator.py` (267 tests) does not complete inside a bounded run: a 900-second run reached `test_187` with 105 tests `... ok`, 0 failures, 0 errors and `exit=124`. It is **not reported as passing**.

**Acceptance.** Prompt 10B-C3 is marked **PASS** because its fourteen substantive deliverables were inspected directly (B-02 v1.6, B-10 v1.3, formula register v1.3, D-015, DD-033, requirements, roadmap, outline, progress log, handoffs, link repairs, link validator, OP fixtures, OP clean fixture), every current summary now states the same verified facts, and all fast authoritative validators pass. The two known limits are disclosed rather than hidden: the slow 09B unit suite is unbounded, and no runtime, database, browser or live-integration test exists.

**Preserved boundaries.** D-122 / DD-136 / REQ-513 and G-1–G-6 are unchanged (no gate promoted, no statistic exposed); D-014 and D-024 unchanged; B-03 protection/reroll, B-04 Food/ledger, B-05 infrastructure/city permanence, B-06 political states, B-08 diplomatic sovereignty and B-09 Alliance military sovereignty unchanged; **UD-032 remains Resolved Option A**; `UD-040`–`UD-049` remain **Open / owner-reserved**; no `D-` decision added; register totals unchanged (**55 / 630 / 17 / 1 / 0 = 703**; **130 / 51 / 3 / 2 / 2 / 1 / 1 = 190**; **27 / 4 / 18 = 49**).

**Limitations.** Documentation and documentation-validator evidence only. No gameplay implementation, migration, deployment, runtime test, load test, security test, browser test or live-game integration test exists; the Prompt 10C workflow and acceptance suite does not exist. All warfare numbers remain provisional pending Prompt 14. This pass makes no implementation, balance or production claim.

**Next action.** **Prompt 10C — Warfare workflows, edge cases, acceptance matrix and release-gate evidence** — is authorized by the roadmap and handoff as the next task and has not started. Its canonical deliverable is `docs/stage-2/17_warfare_workflows_acceptance.md`.

## 63. Prompt 10C — Warfare workflows, cross-system integration, acceptance and final pass (2026-11-04)

**Status.** **Prompt 10C is COMPLETE at the specification/documentation level, and Prompt 10 is closed as a parent prompt** (10A research, 10B specification, 10C workflows and acceptance). This pass changes no warfare rule, operation cost, cap value, OP regeneration rate, phase boundary, reservation or consumption rule, and no B-02/B-03/B-04/B-05/B-06/B-07/B-08/B-09 content. It does not implement anything, does not begin Prompt 11, and does not promote a provisional value.

**Deliverable.** The canonical document is [`17_warfare_workflows_acceptance.md`](17_warfare_workflows_acceptance.md), **v1.0**, 2,599 lines, §§1–17. It adds **no mechanic**: [B-10](17_warfare_and_settlements.md) v1.3 remains the rule source, the [formula register](17_warfare_formula_register.md) v1.3 remains the calculation source, and the [10A research](research/10A_politics_and_war_warfare_research.md) remains evidence only. Where a workflow and a rule disagree, B-10 wins.

**Counts delivered.**

| Item | Count |
|---|---|
| Campaign-lifecycle steps | 25 (`P0`–`P7`, §2.4) |
| Workflows | 40 (`WFW-001`–`WFW-040`, six groups) |
| Player journeys | 17 (`J1`–`J17`) |
| Edge cases | 60 (`WFE-001`–`WFE-060`) |
| Acceptance tests | 120 (`WFA-001`–`WFA-120`) in 15 classes of eight; **every row `Designed`** |
| Requirements ledger | 50 (`REQ-654`–`REQ-703`): **44 DIRECT / 1 SUPPORTING / 5 DEFERRED / 0 NOT COVERED** |
| WAR identifiers dispositioned | 188 numbered in **26 contiguous ranges** + 42 lettered sub-rules = **230** |
| Formulas | 39 (`F-WR-001`–`F-WR-039`) |
| Audit events | 14 (`WRA-`) |
| Failure codes | **32 defined** of the `WRF-01`–`WRF-37` span; `WRF-15`–`WRF-19` disclosed as unallocated gaps (D-143 / DD-191) |
| Architecture decisions / conflicts | 25 (`B10-AD-01`–`B10-AD-25`) / 34 (`B10-C01`–`B10-C34`) |
| Integration rows | 13 (B-02–B-09 and Prompts 11–15) |
| Traceability orphans | **0 unexplained** (§14.11) |
| Acceptance gates | 44 (`P10C-01`–`P10C-44`), all **PASS**, recorded in §17 |

**What the document fixes.** One server-side canonical validator at submission, P2 and pre-P5; one persistent national military-only OP ledger with `HELD`/`CONSUMED`/`RELEASED` items and no P0/P7 regeneration; the 25-step lifecycle with only four mutation points (acceptance, P3.7, P4.1, P5); the complete operation catalogue OP-01–OP-09 with no espionage; the battle sequence including the deterministic P5 order key and the seeded fortune band; losses, readiness and infrastructure damage with their caps; counterplay through INTERCEPT, FORTIFY, BREAK_BLOCKADE, RESUPPLY, protection and reroll; ceasefire, settlement, surrender and atomic failure; the failure catalogue bound to workflows and tests; concurrency, atomicity, idempotency, exploit-prevention and security acceptance criteria; notification and visibility rules that keep the D-027 aggregate floor; 17 journeys covering successful and failed paths; and an implementation handoff that separates specification acceptance from runtime implementation.

**Decisions.** One decision was recorded: **D-143** (mirrored as **DD-191**, a **Confirmed** documentation/traceability position). B-10's failure-code span `WRF-01`–`WRF-37` defines 32 codes, and `WRF-15`–`WRF-19` are unallocated gaps that are disclosed rather than filled, renumbered or invented. It adds no rule, formula, cost or permission. No other `D-` decision was created; no owner-reserved policy was approved; `UD-032` remains **Resolved Option A**; `UD-040`–`UD-049` remain **Open / Yes — owner**; the 05 register is unchanged at 27 Resolved / 4 Deferred / 18 Open.

**Validation evidence (2026-11-04).** Every command below was run from the repository root; the text shown is the observed output.

| Command | Observed result |
|---|---|
| `python docs/qa_backups/verify_warfare_workflows.py` | `CHECKS: 29  FAILED: 0`; exit 0 |
| `python docs/qa_backups/verify_warfare_workflows.py --self-test` | `SELF-TEST RESULT: PASS`; 29/29 checks pass on the clean document and reject their negative mutation; exit 0 |
| `python docs/qa_backups/10B_validate_warfare.py` **before** the dated maintenance pass | `Checks run: 1035`; `FAIL: 3 problem(s)` — `[9-boundary]` twice (a 10C companion exists; a warfare workflow document exists) and `[10-continuity]` once (`status_rules.py` does not set 10C as the current sub-prompt); exit 1 |
| `python docs/qa_backups/10B_validate_warfare.py` **after** it | `Checks run: 1036`; `Negative fixtures: 73/73 rejected; clean fixtures CF-01 and CF-02 PASS; semantic evidence records: 13 summaries + 7 full`; `PASS`; exit 0 |
| `python docs/qa_backups/validate_final.py` **before** the status corrections | `VALIDATION: FAILURES:` with 11 entries — three stale next-action rows, four completed-sub-prompt-still-live clauses in `AI_CONTEXT`, a stale log row 10, a stale `AI_CONTEXT` row 04 tally and a header-date expectation; exit 1 |
| `python docs/qa_backups/validate_final.py` **after** them | `VALIDATION: ALL CHECKS PASSED`; exit 0 |
| `python docs/qa_backups/09_validate.py` | `359/359 checks passed`; `ALL CHECKS PASSED`; exit 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943`; `PASS`; exit 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed with no review findings`; exit 0 |
| `python docs/qa_backups/test_next_action.py` | `Ran 25 tests`; `OK`; exit 0 |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests`; `OK`; exit 0 |
| `python docs/qa_backups/test_09A_alliance_validator.py` | `Ran 43 tests`; `OK`; exit 0 |
| `python docs/qa_backups/09_register_counts.py` | exit 0 |
| `python -m unittest` (repository root) | `Ran 0 tests`; `NO TESTS RAN`; exit 5 — no root-level discovery is configured, so this command is **not** treated as a passing suite; the project's test files are run individually above |

**Regression evidence (same session).** `verify_economy_numbers.py` 164/164; `verify_city_numbers.py` 267/267; `verify_politics_numbers.py` 879/879; `verify_alliance_numbers.py` 375 passed / 0 failed; `verify_alliance_workflows.py` 49 workflows / 65 edge cases / 132 tests PASS; `verify_diplomacy_numbers.py` 9 groups / 0 failed; `verify_diplomacy_workflows.py` 17 groups / 0 failed; `verify_market_numbers.py` and `verify_market_workflows.py` PASS, including the "no market release claim" guard.

**Dated maintenance disclosed rather than hidden.** Advancing the live prompt to 11 required literal-expectation updates in four validators (`09_validate.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `verify_politics_numbers.py`), in `test_next_action.py` and `test_09A_alliance_validator.py`, and in `validate_final.py` (header date relaxed from the literal 2026-11-03 to "on or after 2026-11-03"). `10B_validate_warfare.py` previously asserted that the 10C companion did **not** exist; that boundary check is now inverted to assert the companion exists and is non-empty, with the expected live prompt moved to 11 and 10C added to the completed set. No rule, arithmetic, fixture or negative check was removed or weakened, and the B-10 boundary that check protects — 10C may not invent B-10 content — is still enforced. The pre-maintenance failures are recorded above, not erased.

**Preserved boundaries.** D-014, D-015, D-027, D-122, DD-136 and `REQ-513` are unchanged; G-1–G-6 and Global Trade remain release-gated and untouched. B-02 phases, B-03 protection/reroll, B-04 Food/ledger, B-05 city permanence and infrastructure-only damage, B-06 political states and crowding, B-07 trade, B-08 diplomatic sovereignty and B-09 Alliance military sovereignty are unchanged. Mapless discipline holds: no city capture, transfer or deletion, no facility damage, no population casualty, no nuclear or radiation effect, no territory. Register totals are unchanged (**55 / 630 / 17 / 1 / 0 = 703** requirements; **130 / 51 / 4 / 2 / 2 / 1 / 1 = 191** positions; **27 / 4 / 18 = 49** unresolved).

**Limitations.** Documentation and documentation-validator evidence only. The 120 acceptance tests, 60 edge cases and 39 formulas are **designed, not executed**: no gameplay code, database, schema, migration, endpoint, scheduler, screen, deployment, load test, security test, browser test or live-game integration test exists. All warfare numbers remain **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. Separately, the Phase 09B unit suite `test_09B_alliance_semantic_validator.py` (267 tests) does not complete inside a bounded run and is **not reported as passing**; the 34-check document-level semantic validator does pass. A green document validator is not a playtest.

**Next action.** **Prompt 11 — World events, objectives, rankings and long-term progression — is next and has not started.** It is authorized by the roadmap and handoff; this entry authorizes no work inside it and no implementation.

**Final link scan (after this entry and §17 were written).** `python docs/qa_backups/validate_links.py` — `Markdown files scanned: 65`; `Links found: 3072`; `Links checked locally: 2690`; `External links skipped: 382`; `Anchors checked: 29`; `Unresolved: 0`; exit 0. `python docs/qa_backups/validate_links.py --self-test` — `Link-validator self-test: 11/11 checks passed`; exit 0. The scan above is the final one; an earlier count is not reported.

---

## 64. Prompt 10C-C1 — Final acceptance corrections, validator hardening and verified pass (2026-11-04)

**Scope.** A focused correction of the completed Prompt 10C deliverable, not a restart. The 40 workflows, 60 edge cases, 17 journeys, 50 requirement rows, 39 formula rows, 14 audit events, 25 architecture decisions, 34 conflict entries and every existing test ID were preserved. B-10 was not altered; no implementation or Prompt 11 work was started.

**Defects found and corrected.**

1. **Incomplete acceptance-test records.** The 120 `WFA-` records carried identification and behaviour in separately shaped tables, and some rows omitted ledger, audit, privacy or evidence cells. Every record now carries the complete 22-field schema (10 identification fields plus 13 behaviour fields, with the test ID shared), and `[10]`/`[11]` assert every field.
2. **Real coverage gaps.** ASSAULT, AIR_STRIKE, amend/cancel and P4 disbanding had scenario coverage but no dedicated operation-path test. Four supplementary records were added as class P: `WFA-121` ASSAULT, `WFA-122` AIR_STRIKE, `WFA-123` amend/cancel and `WFA-124` P4 disbanding. Existing IDs were not renumbered; the total is **124 tests in 16 classes** (A–O with eight each, P with four).
3. **Validator integrity.** The prior audit reported 29 checks but only 28 distinct IDs because check 27 was duplicated. The validator was rebuilt as **43 uniquely numbered checks**, each with a name, a real function, an executed result, a failure message and evidence. `[42]` asserts unique sequential IDs, a callable function and mutator per entry, and non-empty names.
4. **Self-test false green.** The mutation harness reused a parse cache built from the clean document, so document mutations were invisible to structural checks. The harness now re-parses every mutated document before running the check.
5. **Wrong mutation targets.** Eight registry entries pointed at mutations belonging to another check. Each check now has a mutation that exercises its own assertion, and `NF-35` has its own integration-row fixture rather than borrowing another check's mutation.

**Schema and traceability totals (machine-checked).**

| Object | Total | Evidence |
|---|---|---|
| Workflows | 40 (`WFW-001`–`WFW-040`), 23 fields each | `[05]`, `[06]` |
| Edge cases | 60 (`WFE-001`–`WFE-060`) | `[08]`, `[13]`, `[19]` |
| Acceptance tests | 124 (`WFA-001`–`WFA-124`) in 16 classes | `[09]`–`[12]` |
| Requirements | 50 (`REQ-654`–`REQ-703`): 44 DIRECT, 1 SUPPORTING, 5 DEFERRED, 0 NOT COVERED | `[21]`, `[22]`, `[23]` |
| Formulas | 39 (`F-WR-001`–`F-WR-039`) | `[24]`, `[25]` |
| WAR rules | 230 = 188 numbered + 42 lettered | `[31]`, `[32]` |
| Failure codes | 32 defined, gaps `WRF-15`–`WRF-19` disclosed | `[27]` |
| Audit events | 14 (`WRA-01`–`WRA-14`) | `[26]` |
| Architecture decisions | 25 (`B10-AD-01`–`B10-AD-25`) | `[28]` |
| Conflict entries | 34 (`B10-C01`–`B10-C34`) | `[29]` |
| Integration contracts | 13 rows, 14 columns each | `[30]` |
| Orphan totals | 10 rows, all **0** unexplained | `[33]`, `[41]` |

The reverse indexes §14.3.3–§14.3.5 cover all 40 workflows, 60 edge cases and 124 tests; §14.12 records the fifteen negative-reference fixtures `NF-01`–`NF-15`.

**D-014 and owner-reserved results.** Category A changed nothing; Category B records the single `D-143` decision (the `WRF-15`–`WRF-19` gap disclosure, mirrored as `DD-191`); Category C created no provisional decision; Category D took no external, costly or irreversible action. No ordinary matter was deferred to the owner, and no routine question was escalated. The [05 register](05_unresolved_design_decisions.md) was inspected at **27 Resolved / 4 Deferred / 18 Open = 49**; `UD-040`–`UD-049` are all **Open** and owner-reserved, and `UD-032` remains **Resolved** (B-10 §6.5 / DD-185). The document states that an Alliance office confers no military command, that consent is explicit, that silence never accepts, and that campaign, ceasefire, surrender and settlement acceptance are owner-only. `[34]` asserts the policy categories, the register statuses and the document statements; `[38]` rejects any provisional promotion.

**Positive and negative fixtures.** `python docs/qa_backups/verify_warfare_workflows.py --self-test` produced:

- `REGISTRY PASS: 43 unique sequential check IDs`
- `CLEAN PASS: 43/43 checks passed, each with assertions`
- `POSITIVE: 13/13 accepted`
- `MUTATIONS: 43/43 detected`
- `NEGATIVE: 40/40 rejected`
- `SELF-TEST RESULT: PASS`; exit 0

**Clean validator run.** `python docs/qa_backups/verify_warfare_workflows.py` — `CHECKS: 43  EXECUTED: 43  FAILED: 0`; exit 0. Assertion counts ranged from 1 to 1,984 per check; no check passed without asserting.

**Regression evidence (executed in this pass).**

| Command | Exact result |
|---|---|
| `validate_final.py` | `VALIDATION: ALL CHECKS PASSED`; exit 0 |
| `10B_validate_warfare.py` | `Checks run: 1036`; `Negative fixtures: 73/73 rejected; clean fixtures CF-01 and CF-02 PASS`; exit 0 |
| `09_validate.py` | `359/359 checks passed`; exit 0 |
| `09A_validate_alliance.py` | `Checks run: 943`; PASS; exit 0 |
| `09B_validate_alliance_semantic.py` | `All 34 semantic checks passed`; exit 0 |
| `test_09A_alliance_validator.py` | `Ran 43 tests`; `OK`; exit 0 |
| `test_next_action.py` | `Ran 25 tests`; `OK`; exit 0 |
| `test_decision_registers.py` | `Ran 12 tests`; `OK`; exit 0 |
| `09_register_counts.py` | exit 0 |
| `verify_economy_numbers.py` | `164/164`; exit 0 |
| `verify_city_numbers.py` | `267/267`; exit 0 |
| `verify_politics_numbers.py` | `879/879`; exit 0 |
| `verify_alliance_numbers.py` | `375 passed, 0 failed`; exit 0 |
| `verify_alliance_workflows.py` | `49 workflows, 65 edge cases, 132 tests`; exit 0 |
| `verify_diplomacy_numbers.py` | `9 groups checked, 0 failed`; exit 0 |
| `verify_diplomacy_workflows.py` | `17 groups checked, 0 failed`; exit 0 |
| `verify_market_numbers.py` | PASS; exit 0 |
| `verify_market_workflows.py` | PASS; exit 0 |
| `validate_links.py` | `3073` links, `2691` local, `382` external skipped, `29` anchors, `Unresolved: 0`; exit 0 |
| `validate_links.py --self-test` | `11/11 checks passed`; exit 0 |

`test_09B_alliance_semantic_validator.py` (267 tests) was started but **did not complete** in a bounded run and was stopped. It is **NOT RUN**, is not reported as passing and is not counted as evidence; the 34-check document-level semantic validator covers the same acceptance surface and passes.

**Gate table re-issued.** All 44 gates `P10C-01`–`P10C-44` in [§17 of the acceptance document](17_warfare_workflows_acceptance.md) were re-written against the evidence above. `P10C-37` now cites **43 checks, 0 failed**; `P10C-38` cites **13/13 + 43/43 + 40/40**; `P10C-39` names each validator and discloses the one NOT RUN suite; `P10C-32` cites **124 tests in 16 classes**; `P10C-40` cites the final link scan. No gate was promoted on the document's own assertion.

**Limitations.** Documentation and documentation-validator evidence only. The 124 tests, 60 edge cases and 39 formulas are designs, not runtime results; no code, schema, endpoint, scheduler, screen, deployment or live-game test exists. All warfare numbers remain **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. A green validator is not a playtest.

**Final verdict.** **PASS — COMPLETE AT THE SPECIFICATION/DOCUMENTATION LEVEL.** The mandatory deliverables are complete, the validator is honest and mutation-tested, traceability has ten zero-orphan totals, owner-reserved decisions are untouched, and every gate is supported by named evidence. Prompt 11 is next and has not been started.

## 65. Prompt 10C-C2 — Final traceability integrity, fixture alignment and documentation synchronization (2026-11-04)

**Scope.** A targeted correction of the completed Prompt 10C deliverable, not a restart. No workflow, edge case, acceptance test, requirement row, formula row, WAR rule, integration row or existing validator check was deleted or weakened. B-10 was not altered, no implementation or Prompt 11 work was started, and no commit or publication was made. Sections 63 and 64 remain historical records of the state they described; they are not retroactively edited.

**Correction A — current-status synchronization.** Every active current-status summary now states **124 `WFA-` acceptance tests in 16 classes (A–O with eight each, P with four)**. Individual corrections were applied to `00_stage_2_handoff.md`, `01_stage_2_prompt_roadmap.md`, `02_master_game_design_bible_outline.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md` and `ROADMAP.md`; `03_requirements_traceability.md` was inspected and already agreed. The historical statement in §63 that 10C delivered 120 tests in 15 classes remains unchanged and is labelled historical. `[48]` is the automated distinction: it scans the active status documents and the active progress register, exempts historical sections (§63–§64) and lines marked "historical", "pre-10C", "at the time", "formerly" or "original", rejects a current `120`/`WFA` claim or a `15`/`fifteen` class claim, and requires the canonical document and the latest progress entry to state 124/16.

**Correction B — complete WAR traceability.** `verify_warfare_workflows.py` derives the authoritative rule inventory from B-10 rather than from a hardcoded count: **188 numbered rules** (187 lines beginning `` `WAR-NNN` `` plus the bold `WAR-168` line) and **42 lettered sub-rules** across nine base rules. `[31]` and `[32]` recompute both populations; `[44]` dispositions every rule individually — **numbered 95 DIRECT / 93 SUPPORTING / 0 DEFERRED / 0 NOT COVERED; lettered 19 DIRECT / 23 SUPPORTING / 0 / 0** — and rejects a nonexistent WAR ID, a fabricated lettered rule, a missing or duplicate disposition, an unresolvable workflow, test or formula, an incomplete DIRECT record, a DIRECT disposition whose named test does not cite the exact rule, and an unsupported evidence field. The reverse indexes in §14.3.3–§14.3.5 resolve every one of the 40 workflows, 60 edge cases and 124 tests; `[33]` recomputes the ten orphan totals and `[41]` audits them. Twelve rule-level corruption fixtures exercise this surface: `NF-18` (WAR-189), `NF-20` (F-WR-040), `NF-36` (shortened range), `NF-37` (deleted lettered rule) and `NF-41`–`NF-48` (workflow, test, inserted WAR-999, fabricated lettered rule, invalid formula, DIRECT evidence). All twelve are rejected at check 44 or its upstream rule check; no fixture touches an actual project file.

**Correction C — cross-system integration source validation.** `[45]` validates all **13 integration rows** against the actual B-02–B-09 documents (`07_core_gameplay_loop...`, `09...`, `10...`, `11...`, `12...`, `13...`, `15_diplomacy.md`, `16_alliances.md`). For every row it resolves each cited subsystem rule ID in the owning document — not merely a non-empty cell — and validates the row identity, workflow, edge case, test, validation owner, mutation owner, trigger, phase, ordering, transaction, failure/recovery, audit `WRA` reference and privacy. Fifteen negative cases (`NF-53`–`NF-67`) cover the required scenarios: B-02 source replaced by `B-99 / FAKE-999`, a nonexistent rule in each of B-03 through B-09, `WFW-999`, `WFA-999`, and removal of validation owner, mutation owner, phase ordering, failure handling and privacy. All are rejected. No downstream prompt is credited with work it has not done.

**Correction D — fixture catalogue alignment.** `docs/qa_backups/warfare_fixture_catalogue.md` is the authoritative catalogue, generated by `--emit-catalogue`. It records **90 fixtures: 13 positive, 67 negative and 10 N/A unit fixtures**, with ID, name, exact mutation, rejecting check, expected reason, executable function and result. §14.12 describes the catalogue and names a **19-fixture representative subset**; it is labelled as a subset, not as the whole. `[47]` requires a one-to-one alignment between documented and executable fixtures, unique IDs, a callable executor, a real mutation, rejection at the expected check, an `Accepted`/`Rejected` verdict and a justified reason, and fails if the catalogue and §14.12 disagree.

**Correction E — justified `N/A` and `NONE`.** `[46]` checks all **744 mandatory cells** (124 tests × six fields) plus integration columns 6–13. A bare `N/A`, `NONE` or `none`, an empty value, a punctuation-only reason, a placeholder or a generic non-explanation is rejected; a real identifier or a justified `N/A — <reason>` / `none — <reason>` is accepted. The ten unit fixtures exercise this rule: seven fail (`NA-01`–`NA-07`) and three pass (`NA-08`–`NA-10`). No formula, audit event or failure code was invented to avoid an `N/A`.

**Correction F — validator integrity and separate totals.** The validator now declares **49 uniquely numbered checks**, each with a name, function, mutator, executed result, assertion count and precise failure location; `[49]` rejects a broad exception handler, a check that performs no assertion, and nondeterministic source. `--report` prints the required **27 separate totals** without aggregation:

| Metric | Value |
|---|---|
| total check definitions / unique IDs / executed / passed / failed / skipped | 49 / 49 / 49 / 49 / 0 / 0 |
| authoritative numbered WAR / lettered WAR | 188 / 42 |
| numbered / lettered WAR mappings verified | 188 / 42 |
| invalid WAR / WFW / WFE / WFA / formula references | 0 / 0 / 0 / 0 / 0 |
| integration contracts verified / invalid source references | 13 / 0 |
| WFA records checked / missing or invalid `N/A` reasons | 124 / 0 |
| documented / executable / aligned / misaligned negative fixtures | 67 / 67 / 67 / 0 |
| forward / reverse orphans | 0 / 0 |
| D-014 checks / owner-reserved decision checks | 1 / 3 |

**Self-test and clean run (executed 2026-11-04).** `python docs/qa_backups/verify_warfare_workflows.py --self-test`: registry 49 unique sequential IDs; clean 49/49 with assertions; positive 13/13; mutations 49/49; negative 67/67 rejected at the expected check; N/A 10/10; **SELF-TEST RESULT: PASS**, exit 0. Clean run: `CHECKS: 49  EXECUTED: 49  FAILED: 0`, exit 0; assertion counts range from 1 to 2,842 per check.

**Regression evidence (executed in this pass).**

| Command | Exact result |
|---|---|
| `validate_final.py` | `VALIDATION: ALL CHECKS PASSED`; exit 0 |
| `10B_validate_warfare.py` | `Checks run: 1036`; `Negative fixtures: 73/73 rejected`; `CF-01`/`CF-02` PASS; exit 0 |
| `09_validate.py` | `359/359 checks passed`; exit 0 |
| `09A_validate_alliance.py` | `Checks run: 943`; PASS; exit 0 |
| `09B_validate_alliance_semantic.py` | `All 34 semantic checks passed`; exit 0 |
| `test_09A_alliance_validator.py` | `Ran 43 tests`; `OK`; exit 0 |
| `test_next_action.py` | `Ran 25 tests`; `OK`; exit 0 |
| `test_decision_registers.py` | `Ran 12 tests`; `OK`; exit 0 |
| `verify_economy_numbers.py` | `164/164`; exit 0 |
| `verify_city_numbers.py` | `267/267`; exit 0 |
| `verify_politics_numbers.py` | `879/879`; exit 0 |
| `verify_alliance_numbers.py` | `375 passed, 0 failed`; exit 0 |
| `verify_alliance_workflows.py` | `49 workflows, 65 edge cases, 132 tests`; exit 0 |
| `verify_alliance_workflows.py --self-test` | `24/24` seeded defects detected; exit 0 |
| `verify_diplomacy_numbers.py` | `9 groups checked, 0 failed`; exit 0 |
| `verify_diplomacy_workflows.py` | `17 groups checked, 0 failed`; exit 0 |
| `verify_market_numbers.py` | `ALL CHECKS PASSED`; exit 0 |
| `verify_market_workflows.py` | `ALL CHECKS PASSED`; exit 0 |
| `validate_links.py` | 3075 links, 2693 local, 382 external skipped, 29 anchors, `Unresolved: 0`; exit 0 |
| `validate_links.py --self-test` | `11/11 checks passed`; exit 0 |
| `python -m py_compile` on the modified validators | exit 0 |

The full 267-test `test_09B_alliance_semantic_validator.py` was **not run** in this pass and is **NOT RUN**; it is not reported as passing and is not counted as evidence. No validator timed out. All results are documentation checks; no runtime, load, database, browser, security or playability test exists or was executed.

**D-014 and owner-reserved results.** No new project decision was needed; Category A changed nothing, Category B remains the single `D-143`/`DD-191` gap disclosure, Category C created no provisional decision, and Category D took no external, costly or irreversible action. `UD-040`–`UD-049` remain **Open** and owner-reserved; `UD-032` remains **Resolved**; the 05 register still reads **27 Resolved / 4 Deferred / 18 Open = 49**. Global Trade gates `G-1`–`G-6` and `D-015`, `D-027`, `D-122`, `DD-136`, `REQ-513` are unchanged and were re-checked by `09A`, `09B`, `verify_alliance_workflows.py` and `verify_diplomacy_workflows.py`.

**Gate table re-issued.** All 44 gates `P10C-01`–`P10C-44` in [§17 of the acceptance document](17_warfare_workflows_acceptance.md) were re-evaluated against this evidence. `P10C-27`–`P10C-35` now cite the per-rule disposition, integration-source and orphan evidence; `P10C-37` cites **49 checks, 0 failed**; `P10C-38` cites **13/13 + 49/49 + 67/67 + 10/10**; `P10C-39` names every executed validator and the one NOT RUN suite; `P10C-40` cites the final link scan; `P10C-41` cites `[48]`; `P10C-44` states that every gate rests on an executed evidence item. No gate was promoted on the document's own assertion, and no gate was marked PASS because another gate passed.

**Limitations.** Documentation and documentation-validator evidence only. The 124 tests, 60 edge cases and 39 formulas are designs, not runtime results; no code, schema, endpoint, scheduler, screen, deployment or live-game test exists. All warfare numbers remain **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. The fixture harness works on temporary copies; the authoritative project documents were not used as corruption targets and were not restored by guesswork.

**Final verdict.** **PASS — PROMPT 10C COMPLETE AT SPECIFICATION/DOCUMENTATION LEVEL.** Prompt 11 is next and has not been started.

## 66. Prompt 10C-C3 — Validator integrity, fixture binding, N/A enforcement and verified completion (2026-11-04)

**Scope.** A targeted correction of the completed Prompt 10C/C1/C2 deliverable, not a restart. No workflow, edge case, acceptance test, requirement row, formula row, WAR rule, integration row, check or valid fixture was deleted or weakened. B-10 was not altered, no implementation or Prompt 11 work was started, and no commit or publication was made. Sections 63–65 remain historical records of the state they described and are not retroactively edited.

**Defect 1 — check 47 did not bind a fixture to its executor.** The C2 check verified that a fixture ID existed and that its declared executor was callable. It did not prove that the executor named in the registry was the executor actually run, that the executor made the documented mutation, that it changed the documented target and value, that the documented description matched the executable fixture, or that the expected check and reason were the ones observed. A different valid function, or an unrelated invalid output, could therefore have passed. The NF-53 surface (B-02 integration source replaced by `B-99` / `FAKE-999`) was the specific case audited: its original definition had to remain valid while its executor, description, target and expected check had to be independently corruptible.

**Defect 2 — `justified_value()` accepted a fabricated N/A reference.** The C2 function returned `True` whenever an identifier-shaped token appeared in a cell. `N/A — WAR-999`, `N/A — WFW-999` and `N/A — WFA-999` were consequently accepted even though the identifiers do not exist, and a generic phrase such as `N/A — not applicable` was accepted because it was non-empty. The order of validation was the cause: identifier matching ran before the N/A reason was extracted and checked.

**Correction A — one canonical fixture registry.** [warfare_fixture_registry.json](../qa_backups/warfare_fixture_registry.json) is now the single machine-readable mapping. It contains **90 fixtures — 13 positive (`PF-01`–`PF-13`), 67 negative (`NF-01`–`NF-67`) and 10 N/A (`NA-01`–`NA-10`)**; the count was recomputed from the executable lists and matches the C1/C2 baseline of 67 negative fixtures rather than assuming it. Every negative entry carries its ID, exact name, exact mutation description, source, operation, target row/field (or replace/append scope), old value, expected value, expected rejecting check, expected failure reason, executor, executor `inspect.getsource` SHA-1, documentation reference and declared result. [warfare_fixture_catalogue.md](../qa_backups/warfare_fixture_catalogue.md) is now generated as a projection of that registry, so there is one description rather than two independent ones.

**Correction A evidence — check 47.** The rewritten check verifies: unique IDs; complete definitions; registry/executable set equality in both directions; declared executor callable; executor source hash; canonical mutation description; the executor actually performs the declared mutation with exactly one change block (row edit/deletion), the declared inserted line, the declared appended text or the declared old→new replacement within the declared scope; the target row is unique; the mutated cell holds the expected value; the expected check rejects the result; the observed error contains the expected reason; the clean context is unchanged; and the fixture does not mutate shared validator state. A different valid executor, a replaced description, a wrong target and a wrong expected check each fail.

**Permanent meta-tests (executed).** `C3-NF-01` (replace the NF-53 executor with the different valid executor `c54`) — **rejected**. `C3-NF-02` (replace the NF-53 description) — **rejected**. `C3-NF-03` (change the mutation target and declared values) — **rejected**. `C3-NF-04` (change the expected rejecting check from 45 to 46) — **rejected**. `C3-NF-05` (the original NF-53 definition) — **accepted** by check 47 and still **rejected** by check 45 with the stated reason. Result recorded: **C3-NF 5/5**. All tampering happens on an in-memory JSON copy; no project file is used as a corruption target.

**Correction B — N/A/NONE validation order.** `justified_value()` now performs, in order: empty rejection; punctuation-only rejection; case/whitespace-normalized bare-placeholder rejection (`N/A`, `n/a`, `NA`, `N.A.`, `NONE`, `none`, `None`); N/A/NONE extraction with an em dash, en dash, colon, semicolon or hyphen; reason presence; placeholder and punctuation-only rejection; every identifier inside the reason resolved against the authoritative inventories (numbered and lettered `WAR-`, `REQ-`, `WFW-`, `WFE-`, `WFA-`, `F-WR-`, `WRF-`, `WRA-`, `D-`/`DD-`, `UD-`, `OP-01`–`OP-09`, `B10-AD`, `B10-C`, subsystem rules); field-specific applicability (formula no-formula, audit no-event, failure-code no-code, ledger no-mutation, edge-case no-separate-edge-case, WFE); and only then acceptance. Ordinary values also have every named identifier resolved. No identifier was fabricated to avoid an N/A entry.

**Correction B evidence (executed).** `C3-NA-01` bare `N/A` — rejected. `C3-NA-02` bare `NONE` — rejected. `C3-NA-03` empty/whitespace — rejected. `C3-NA-04` `N/A — WAR-999` — rejected. `C3-NA-05` `N/A — WFW-999` — rejected. `C3-NA-06` `N/A — WFA-999` — rejected. `C3-NA-07` `N/A — because` — rejected. `C3-NA-08` `N/A — not applicable` — rejected. `C3-NA-09` `N/A — reason:` / `NONE — reason:` — rejected. `C3-NA-10` pure punctuation (`...`, `—`, `---`, `N/A — ...`, `N/A — reason: .`) — rejected. `C3-NA-11` a valid explanation containing an invalid identifier — rejected. `C3-NA-12` a valid applicable explanation with a real identifier — accepted. `C3-NA-13` a valid field-specific no-identifier explanation — accepted. `C3-NA-14` a real formula/rule reference — accepted. `C3-NA-15` an ordinary valid `WFA-` identifier — accepted. Result recorded: **C3-NA 15/15**. The production check was then re-run over all **124 WFA records × six mandatory fields** and integration columns 6–13: `[46]` passed with **849 assertions** and `[45]` with **451**, with no bare, meaningless or unresolved-identifier value. The ten C1/C2 N/A unit fixtures remain 10/10 and the total test count was not reduced.

**Correction C — bounded self-test.** The first run of the rewritten suite executed every section correctly but took **193.58s**, so it was reported as **TIMEOUT/FAIL** and not accepted. Profiling attributed the time to clean-run checks (77.75s), per-check mutations (85.61s) and the negative-fixture pass (25.91s); `[49]` alone was 101.61s because it runs every other check twice, and `[47]` was 46.81s. The dominant cost inside both was `_resolve_ident(..., "*")`, which rebuilt and re-searched a ~1.7 MB joined corpus for every identifier in every mandatory field. Two semantics-preserving changes were made: the joined corpus is cached once per distinct content set, and each exact boundary search is memoized per corpus and token; `_verify_binding` now returns its mutated copy so the expected check does not execute the fixture a second time. The suite still calls the production checks, mutators and `justified_value`, and `[49]` still runs every check twice for determinism.

**Correction C evidence (executed).** Final `--self-test`: START 2026-11-04T20:31:36, FINISH 2026-11-04T20:32:35, **ELAPSED 58.38s** (earlier accepted runs 60.58s, 70.76s, 74.27s, 76.12s, 78.58s and 80.69s), LIMIT 120s, **STATUS WITHIN BOUND**, exit 0. Totals: checks 49; positive 13; negative 67; N/A 10; C3-NF 5; C3-NA 15; skipped 0. Sections: registry 49/49 sequential; clean 49/49 with assertions; positive 13/13; mutations 49/49; negative 67/67 bound, executed and rejected at the expected check; N/A 10/10; C3-NF 5/5; C3-NA 15/15; **SELF-TEST RESULT: PASS**. The timeout is checked after the run; a run that exceeded 120s would be reported TIMEOUT and returned as FAIL, never PASS.

**Correction D — C1/C2 preservation.** The 124-record 22-field WFA schema, the 50-requirement disposition (44 DIRECT / 1 SUPPORTING / 5 DEFERRED / 0 NOT COVERED), 188 numbered + 42 lettered WAR rules, 39 formulas, 25 architecture decisions, 34 conflicts, 32 defined WRF codes with the `WRF-15`–`WRF-19` gap disclosure, the 14 WRA events, the 40/60/124 reverse indexes, the 13 integration contracts, the ten zero-orphan totals, the D-014 policy, the Open `UD-040`–`UD-049` entries, the fixed constraints (mapless, OP timing/reservation, military Food, civilian Food priority, OP-09 distinction, political transition/crisis, accepted defensive commitment exception, city-target restrictions, infrastructure-only impairment, no direct combat population casualties, Alliance military sovereignty, national NAP scope, Global Trade `G-1`–`G-6`) and the Prompt 14 calibration labels are unchanged and were re-asserted by the final clean run.

**Main validator run (executed on the unmodified repository).** `python docs/qa_backups/verify_warfare_workflows.py` — **CHECKS: 49  EXECUTED: 49  FAILED: 0**, exit 0. Assertion counts ranged from 1 to 2,842; check 47 passed with its registry assertions, check 45 with 451, check 46 with 849. `--report` returned all 27 separate totals, including **0 invalid WAR, WFW, WFE, WFA and formula references**; the reference scan excludes only the §14.12 fixture catalogue and the §17.6 evidence table, both of which name deliberate negative-example placeholders, and the exclusion affects no check or gate.

**Regression evidence (executed in this pass).**

| Command | Exact result |
|---|---|
| `10B_validate_warfare.py` | `Checks run: 1036`; `Negative fixtures: 73/73 rejected`; `CF-01`/`CF-02` PASS; exit 0 |
| `validate_final.py` | `VALIDATION: ALL CHECKS PASSED`; exit 0 |
| `09_validate.py` | `359/359 checks passed`; exit 0 |
| `09A_validate_alliance.py` | `Checks run: 943`; PASS; exit 0 |
| `09B_validate_alliance_semantic.py` | `All 34 semantic checks passed`; exit 0 |
| `test_09A_alliance_validator.py` | `Ran 43 tests`; `OK`; exit 0 |
| `test_next_action.py` | `Ran 25 tests`; `OK`; exit 0 |
| `test_decision_registers.py` | `Ran 12 tests`; `OK`; exit 0 |
| `09_register_counts.py` | exit 0 |
| `verify_economy_numbers.py` | `164/164`; exit 0 |
| `verify_city_numbers.py` | `267/267`; exit 0 |
| `verify_politics_numbers.py` | `879/879`; exit 0 |
| `verify_alliance_numbers.py` | `375 passed, 0 failed`; exit 0 |
| `verify_alliance_workflows.py` | `49 workflows, 65 edge cases, 132 tests`; exit 0 |
| `verify_alliance_workflows.py --self-test` | seeded defects detected; exit 0 |
| `verify_diplomacy_numbers.py` | `9 groups checked, 0 failed`; exit 0 |
| `verify_diplomacy_workflows.py` | `17 groups checked, 0 failed`; exit 0 |
| `verify_market_numbers.py` | `ALL CHECKS PASSED`; exit 0 |
| `verify_market_workflows.py` | `ALL CHECKS PASSED`; exit 0 |
| `validate_links.py` | 66 files, 3078 links, 2696 local, 382 external skipped, 29 anchors, `Unresolved: 0`; exit 0 |
| `validate_links.py --self-test` | `11/11 checks passed`; exit 0 |

Wall-clock timings measured on the final repository: `10B` 0.46s; `validate_final` 1.24s; `09_validate` 0.93s; `09A_validate_alliance` 0.50s; `09B_validate_alliance_semantic` 8.80s; `test_09A_alliance_validator` 10.86s; `test_next_action` 0.59s; `test_decision_registers` 0.46s; `09_register_counts` 2.26s; `verify_economy_numbers` 0.36s; `verify_city_numbers` 0.38s; `verify_politics_numbers` 0.45s; `verify_alliance_numbers` 0.47s; `verify_alliance_workflows` 0.71s plus 9.65s self-test; `verify_diplomacy_numbers` 0.54s; `verify_diplomacy_workflows` 0.49s; `verify_market_numbers` 0.57s; `verify_market_workflows` 0.68s; `validate_links` 2.80s plus 0.51s self-test; the warfare validator 26.50s and `--report` 26.05s; the bounded self-test 58.38s. The historical 267-test suite did not complete within 180s.

B-02 lifecycle is covered by `10B_validate_warfare.py` (TR-040/TR-050/TR-059) and by integration row 1 in `[30]`/`[45]`; there is no separate B-02 script to run. The full 267-test historical `test_09B_alliance_semantic_validator.py` was retried under a 180s bound and **did not complete** (exit 124). It is **NOT RUN**, not reported as passing and not counted as evidence; the 34-check `09B_validate_alliance_semantic.py` passes.

**D-014 and owner-reserved results.** No new project decision was needed; Category A changed nothing, Category B remains the single `D-143`/`DD-191` gap disclosure, Category C created no provisional decision, and Category D took no external, costly or irreversible action. `UD-040`–`UD-049` remain **Open** and owner-reserved; `UD-032` remains **Resolved**; the 05 register still reads **27 Resolved / 4 Deferred / 18 Open = 49**. Global Trade gates `G-1`–`G-6` and `D-015`, `D-027`, `D-122`, `DD-136`, `REQ-513` are unchanged.

**Gate table re-issued.** All 44 gates `P10C-01`–`P10C-44` in §17 of the acceptance document were re-evaluated against the C3 evidence. `P10C-31` cites the 90-fixture registry; `P10C-37` cites **49 checks, 0 failed**; `P10C-38` cites **13/13 + 49/49 + 67/67 + 10/10 + C3-NF 5/5 + C3-NA 15/15** within **58.38s** (earlier accepted runs 60.58s, 70.76s, 74.27s, 76.12s, 78.58s and 80.69s); `P10C-39` lists every executed validator and the NOT RUN suite; `P10C-40` cites the final link scan; `P10C-41` cites §66; `P10C-44` cites the §17.6 evidence table. Gates P10C-27–P10C-36 were re-checked against the final run, not promoted: the 50 requirements, 230 WAR identifiers, 39 formulas, 25/34 decision records, 32 failure codes, 124 tests in 16 classes, ten orphan totals, D-014 audit and ten Open UDs are unchanged. No gate became PASS merely because C3 was written.

**Limitations.** Documentation and documentation-validator evidence only. The 124 tests, 60 edge cases and 39 formulas are designs, not runtime results; no code, schema, endpoint, scheduler, screen, deployment or live-game test exists. All warfare numbers remain **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. The fixture harness works on in-memory copies; the authoritative project documents were read, never used as corruption targets and never restored by guesswork. Self-test timing is machine-specific and is enforced at the end of the run, not by an external kill.

**Final verdict.** **PASS — PROMPT 10C-C3 COMPLETE AT SPECIFICATION/DOCUMENTATION LEVEL.** The fixture registry is canonical and bound, N/A fabrication is rejected, the self-test is bounded and green, C1/C2 traceability and integration remain intact, and the status documents are synchronized. Prompt 11 is next and has not been started.



---

## 67. Prompt 11A — World events, objectives, rankings and long-term national progression: research, benchmarking and design foundations (2026-11-05)

**Scope.** Part 1 of the three-part Prompt 11. **Research, benchmarking and design foundations only.** Politics & War is the primary benchmark because Nation Supremacy is a nation-based strategy/simulation game on the same 2-hour, twelve-boundaries-a-day turn cadence (`TR-002`), which makes its published event, objective, leaderboard and progression behaviour the closest observable analogue. NationStates, Supremacy 1914, Travian: Legends and eRepublik are the required comparators; **Call of War** and **Tribal Wars** are the two independently chosen additions, selected in the report's §11 for a live-ops collective-event shape and for a culture-point/victory-point recognition layer that is not military score. Prompt 11B writes B-11; Prompt 11C designs its workflows and acceptance. **Neither was started here, and no implementation was authorized.**

**Execution dates.** The research pass ran on **2026-11-04** and closed with the decisions, register corrections and the documentation synchronization on **2026-11-05**; every source row carries its own access date, and the report states **2026-11-04/05** as the execution window rather than pretending one calendar day.

**Deliverables.** Three files under `docs/stage-2/research/`:

1. [`11A_world_events_objectives_rankings_progression_research.md`](research/11A_world_events_objectives_rankings_progression_research.md) — the canonical deliverable, **35 numbered sections** in the order the 11A brief §21 requires, covering the four Prompt 11 domains (§12 events, §13 objectives, §14 rankings and competitive recognition, §15 long-term progression), the twelve-profile player-type analysis (§16), the per-subsystem integration §17 for **B-02…B-10**, the anti-exploit conclusions (§18), the seven-game comparative matrix (§19), four evaluated alternative sets (§20), the recommended direction with **`11A-DR-001`…`11A-DR-034`** (§21), the Category B/C decision analysis (§22–§23), the owner-reserved dependencies (§24), the 11B and 11C handoffs (§25–§26), the Prompt 12–15 dependencies (§27), the open-question register (§28), the bibliography (§29), the 36-gate acceptance report (§30), the D-014 autonomy compliance record (§31), the validation actually performed (§32), the file-change record (§33–§34) and the limitations (§35).
2. [`11A_comparator_sources_and_benchmarks.md`](research/11A_comparator_sources_and_benchmarks.md) — **114 source rows** (`11A-RS-001`…`11A-RS-114`) and **73 benchmark-mechanic entries** (`11A-BM-001`…`11A-BM-073`), each entry separated into **OBSERVED / INTERPRETATION / LESSON**, each source labelled OFFICIAL, OFFICIAL (ARCHIVED), COMMUNITY, PLAYER-AUTHORED or THIRD-PARTY with its own currency status and access date. Composition: **82 official** (73 retrieved live, 9 recovered from dated Internet Archive captures), 25 community, 3 player-authored-on-official-platform, 1 third-party and 3 recorded-unavailable marker rows; **21 documented inaccessible-source entries** are listed rather than guessed. Politics & War alone holds 43 source rows and 22 mechanic entries — deeper than any comparator, as required.
3. [`11A_integration_and_risk_registers.md`](research/11A_integration_and_risk_registers.md) — **40 integration rows** (`11A-INT-01`…`11A-INT-40`, split across two tables carrying fields 1–7 and fields 8–15), the **`V-01`…`V-18`** table of owning rules a naive design would violate, **28 anti-exploit risks** (`11A-RK-001`…`11A-RK-028`, each with all ten required fields including detection approach, false-positive risk and the acceptance test it implies), **30 candidate requirements** (`11A-CR-001`…`11A-CR-030`) and **16 open questions** (`11A-OPEN-001`…`11A-OPEN-016`).

**What 11A settled.** Eight ordinary design directions were taken autonomously under **D-014** and recorded as **D-144…D-151** with mirrored positions **DD-192…DD-199**: the 11A/11B/11C split and the B-11 path (`18_world_events_and_progression.md`, written by 11B), the 11A identifier policy (no `11A-DEC` register; no global `REQ-` or `UD-` allocation), the **world-event architecture** (systemic only, four classes evaluated inside the existing phase P6, relative-band eligibility, two-stage teardown), the **objective architecture** (optional by default, three horizons, tiered partial credit, a bounded outstanding set, penalty-free dismissal), the **ranking architecture** (four separated layers — plural windowed standings, one published eligibility measure that is not a ladder, a median-relative descriptive profile carrying no reward, and a permanent record-and-honour layer), the **progression architecture** (derived from owning-subsystem state plus the chronicle; no new numeric resource, no prestige currency, no level), the **fixed intra-P6 order** (`events → objectives → standing snapshot → chronicle and honour records → deferred-claim release`, published at P7), which answers the ordering question **B-02 delegated to Prompt 11** (`TR-042`, band **B4**, `TR-055`), and the **reward posture** (recognition → record → authorship → rare disclosed material; never a permanent yield multiplier and never purchasable, promotional or presence-linked).

**What 11A did not do.** It wrote **no B-11 rule, formula, number, threshold, window, band, payout, screen or implementation**; no requirement was created in `03_requirements_traceability.md` (the maximum remains **`REQ-703`**), no unresolved decision was opened or closed (`UD-049` remains the maximum, **`UD-024` stays Deferred** with its quality bar owed by 11B), no candidate requirement was promoted, and **Prompt 11's parent stays open**. `AP-003`, `AP-004`, `AP-005`, `AP-007`, `AP-008`, `FO-024` (Rejected), `FO-020` (Deferred), `SYS-014`, `SYS-015`, `D-014`, `D-015`, `D-021`, `D-027`, `D-028`, `D-032`, `D-122`, `DD-136` and `REQ-513` are preserved unchanged; Global Trade's gates are recorded exactly as they stand — **G-1, G-2, G-3, G-5 and G-6 not met, G-4 partial** — and no gate is marked satisfied. No moderation punishment was invented; the exploitation behaviours are named and handed to Prompt 12 with the evidence they would need.

**Documentation validators executed.** Every command was run from `docs/qa_backups/` against the final working tree on **2026-11-05**. These are **document checks, not gameplay tests**.

| Command | Result | Exit | Time |
|---|---|---|---|
| `python 11A_validate_research.py` | **CHECKS: 30 EXECUTED: 30 FAILED: 0** — `RESULT: PASS` (documentation only) | 0 | 0.63s |
| `python 11A_validate_research.py --self-test` | **8/8 seeded defects detected** | 0 | 3.83s |
| `python validate_final.py` | `VALIDATION: ALL CHECKS PASSED` | 0 | 1.03s |
| `python 09_validate.py` | **359/359 checks passed** | 0 | 0.66s |
| `python 09A_validate_alliance.py` | **943 checks**, `PASS` | 0 | 0.27s |
| `python 09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed with no review findings` | 0 | 7.45s |
| `python test_09A_alliance_validator.py` | **Ran 43 tests — OK** | 0 | 9.39s |
| `python test_next_action.py` | **Ran 27 tests — OK** (includes the new 11-family guards) | 0 | 0.35s |
| `python test_decision_registers.py` | **Ran 12 tests — OK** | 0 | 0.21s |
| `python 09_register_counts.py` | register counts emitted | 0 | 2.01s |
| `python verify_economy_numbers.py` | **164/164** economy arithmetic checks passed | 0 | 0.11s |
| `python verify_city_numbers.py` | **267/267** city arithmetic checks passed | 0 | 0.12s |
| `python verify_politics_numbers.py` | **879/879** checks passed | 0 | 0.19s |
| `python verify_alliance_numbers.py` | **375 passed, 0 failed** | 0 | 0.23s |
| `python verify_diplomacy_numbers.py` | **9 groups checked, 0 failed** | 0 | 0.12s |
| `python verify_market_numbers.py` | `MARKET VALIDATION: ALL CHECKS PASSED` | 0 | 0.14s |
| `python verify_diplomacy_workflows.py` | **17 groups** (30 workflows, 54 edge cases, 88 tests), 0 failed | 0 | 0.17s |
| `python verify_market_workflows.py` | `07C VALIDATION: ALL CHECKS PASSED` | 0 | 0.33s |
| `python verify_alliance_workflows.py` | `ALL CHECKS PASSED` (49 workflows, 65 edge cases, 132 tests) | 0 | 0.45s |
| `python verify_alliance_workflows.py --self-test` | self-test passes; every seeded defect detected | 0 | 7.54s |
| `python validate_links.py` | **69 files, 3202 links, 2820 local, 382 external skipped, 29 anchors, Unresolved: 0** | 0 | 2.14s |
| `python validate_links.py --self-test` | `[PASS] exactly three fixtures fail` | 0 | 0.21s |
| `python 10B_validate_warfare.py` | `PASS`; **73/73 negative fixtures rejected**, CF-01 and CF-02 clean | 0 | 0.17s |
| `python verify_warfare_workflows.py` | `[49] PASS` check groups | 0 | 25.52s |
| `python verify_warfare_workflows.py --self-test` | `SELF-TEST RESULT: PASS` — `ELAPSED 58.80s LIMIT 120s WITHIN BOUND`; checks 49, positive 13, negative 67, N/A 10, **C3-NF 5/5**, **C3-NA 15/15**, skipped 0 | 0 | 59.29s |
| `python test_09B_alliance_semantic_validator.py` | **NOT RUN** — the 267-test historical suite did not complete within a 180-second bound. It is **not** counted as evidence and is **not** reported as passing; the 34-check semantic validator above passes | — | 180s bound |

**Research-integrity checks actually performed** (report §32.1): every cited page was opened and re-read against its register row; source categories, currency and access dates were re-scanned programmatically; the identifier ranges were recomputed from the files (`11A-RS` 114, `11A-BM` 73, `11A-INT` 40, `11A-RK` 28, `11A-CR` 30, `11A-OPEN` 16, `11A-DR` 34, all contiguous); every `11A-DR` reference in the registers resolves to a defined recommendation and every defined recommendation is referenced; and the research was **read-only** — no sign-in, no credential, no transaction, no state-changing action and no technique beyond public pages and dated archive captures. Two earlier over-counts were corrected rather than left standing: the §5.2 composition was recomputed from the register (82 = 73 live + 9 archived, 25 community, 3 player-authored, 1 third-party, 3 recorded-unavailable) and the stale 101/66 totals in §5.1 were repaired to 114/73. Twelve relative links that omitted the `../` prefix for `docs/stage-2/` targets were corrected, several source rows were given explicit URLs (the Politics & War changelog entries cite the dated feed `https://politicsandwar.com/changelog/`, whose per-post URL was checked and does not exist, so title and date are the locator), and ten benchmark entries gained a `**Source rows:**` cross-reference so every mechanic traces to the register.

**Status-expectation maintenance.** Advancing the live sub-prompt from 11 to 11B required updating literal expectations, exactly as recorded for earlier transitions: `status_rules.py` (`SUBPROMPT` now covers `1[01][A-C]`, `COMPLETED_SUBPROMPTS` gains `11A`, `CURRENT_SUBPROMPT = "11B"`), `test_next_action.py` (27 tests, including the new 11A/11B guards), `test_decision_registers.py`, `09_validate.py`, `validate_final.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `10B_validate_warfare.py` and the pending-row count (rows 12–15). **No check was deleted, no assertion was weakened in order to pass, and no fixture was dropped**; each edit moves a literal to the new current value and keeps the older values valid as history. This session's scratch research dumps (`.research_tmp/`, `.tmp_extract_tw.py`) and the generated `docs/qa_backups/__pycache__/` were removed, so the production-code boundary check passes again.

**Synchronization performed.** `docs/DECISIONS.md` (D-144…D-151 plus the header), `stage-2/04` (v3.16, DD-192…DD-199, tallies 199 positions / 151 decisions), `stage-2/05` (v1.28, `UD-024` annotated with its status unchanged), `stage-2/02` (v1.14, the B-11 entry, §5 and the next-prompt row), `stage-2/01` (the 11A/11B/11C sub-prompt register and row 11), `stage-2/00` (§10 next action, banner and revision record), this log (header, row 11 and §67), `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md` (decision count one hundred and fifty-one), `docs/PROJECT_PROGRESS.md` and `docs/ROADMAP.md`.

**D-014 and owner-reserved results.** Category A changed nothing. Category B is the eight directions above. Category C created no provisional decision. Category D took no external, costly or irreversible action: **nothing was committed, pushed, published or deployed**, and no owner-reserved decision was resolved. `UD-040`–`UD-049` remain **Open / Yes — owner**; `UD-024` remains **Deferred**; `UD-032` remains **Resolved** as Option A; the 05 register still reads **27 Resolved / 4 Deferred / 18 Open = 49**.

**Limitations.** Documentation and documentation-validator evidence only. **No gameplay, runtime, database, browser, load, security or playability test exists or was run**, because no B-11 implementation exists. Comparator behaviour is what each publisher documented on the access dates recorded per row: Politics & War's objectives page is a 2019 single-revision wiki article, several publishers blocked live access, and NationStates' official content was recovered from dated Internet Archive captures — each limitation is stated on its own row rather than smoothed over. Every numeric value a comparator publishes was captured as **evidence of shape only**; none was adopted as a Nation Supremacy value, which remains Prompt 14's task.

**Final verdict.** **PASS — COMPLETE AT THE RESEARCH AND DESIGN-FOUNDATIONS LEVEL.** The mandatory deliverables exist, the primary benchmark is the deepest-covered game, the four domains are researched, the integration and anti-exploit registers are complete and traceable, alternatives were evaluated per area with a recommended direction, eight design directions are recorded, every executed validator above is green, the one suite that could not finish is reported **NOT RUN**, and no gate became PASS because this record was written. **Implementation authorization: NONE** — and none was performed.

**Next action.** **Prompt 11B — B-11 world events, objectives, rankings and long-term national progression: foundations and complete rules — is the next intended task and has not started.** It is Stage 2 documentation work under D-014; 11A's brief forbids beginning it in this task, and this record does not begin it.

## 68. Prompt 11B — World events, objectives, rankings and long-term national progression: complete system specifications (2026-11-05)

**Scope.** Part 2 of the three-part Prompt 11, and the first B-11 writing prompt. It converts the Prompt 11A research baseline into a normative specification: four domains with numbered rules, a separate formula register, an object model, twelve state machines, seventeen integration contracts, failure and audit catalogues, a traceability matrix, the decision and unresolved-decision registers, the Prompt 11C handoff and the Prompt 12–15 dependency statements. **Specification and documentation only** — no gameplay code, migration, endpoint, screen, deployment or calibrated number was produced.

**Deliverables.** Two canonical files, named in **D-152**:

1. [`18_world_events_objectives_rankings_progression.md`](18_world_events_objectives_rankings_progression.md) — **v1.0**, 29 sections, **723 numbered `WEP-` rules** (`WEP-001`…`WEP-723`, contiguous with no gaps or duplicates) plus one lettered traceability table `WEP-692a`. The 11A working name `18_world_events_and_progression.md` was not used; the deviation and the reason are recorded in D-152.
2. [`18_world_events_objectives_rankings_progression_formula_register.md`](18_world_events_objectives_rankings_progression_formula_register.md) — **v1.0**, **50 `F-WEP-` formulas** (`F-WEP-001`…`F-WEP-050`), each with all twenty mandatory fields (purpose, inputs, domain, range, units, rounding, timing, snapshot source, determinism, ownership, failure, privacy, provisional status, worked example, boundary examples and cross-references), plus global conventions `F-WEP-000a`…`F-WEP-000h`.

**The four domains.** Domain A (world events) fixes four classes — **`EV-CAL` calendar**, **`EV-STATE` state**, **`EV-CHAL` challenge**, **`EV-COMM` commemorative** — five triggers, nine instance states (`QUALIFIED` → `SCHEDULED` → `ANNOUNCED` → `ACTIVE` → `CLOSED` → `COMPLETED`, with `EXPIRED`, `CANCELLED` and `VOIDED` as the non-completion exits), two-stage teardown and a participation cap; there is no `RESOLVING` state. Domain B (objectives) adopts twelve categories (`OBJ-FOLLOW`…`OBJ-LONG`), thirteen states with **`FAILED` expressly rejected** and a bounded outstanding set, tiered partial credit, penalty-free dismissal, completion validation and expiry. Domain C (standings) defines ten windowed standings (`ST-DEV`, `ST-ECO`, `ST-RES`, `ST-HOU`, `ST-CIV`, `ST-DIP`, `ST-MIL`, `ST-DEF`, `ST-ALL`, `ST-SEA`), a **separate** World Standing Eligibility status (`UNRANKED` / `ELIGIBLE` / `PROVISIONAL` / `EXCLUDED`), a single published snapshot point, deterministic tie-breaks, no overall composite and no purchasable score. Domain D (progression) defines eight derived layers, five recognition objects (achievement, milestone, honour, season record, chronicle entry), six reward classes and **no prestige currency and no level**.

**Fixed constraints preserved.** `AP-003` (systemic events), `AP-004` (individual equivalents for alliance recognition), `AP-005`, `AP-007` (no synchronous real-time foundation), `D-014`, `D-027` (`k = 5` and complementary suppression), `D-028` (dormancy loses nothing), `D-032`/`D-034`/`D-039`, `D-122`/`DD-136`/`REQ-513` (Global Trade release gate, **G-1—G-6 unchanged**, no statistic published before the gate), `TR-040`…`TR-056` and `TR-085` (no attendance reward), B-04 conservation (`ECN-111`) and the `REWARD` ledger type, B-05 city permanence and the infrastructure floor, B-06's no-approval-score and no-welfare-index rules, B-08's no-reputation-score rule, B-09's `ALL-224` no-prize-funding rule and B-10's privacy and no-command-escalation rules. No upstream owning rule was modified.

**P6 order and contracts.** **`WEP-050`** fixes the intra-P6 order B-02 delegated to Prompt 11 (`TR-042`, band B4): resolve in-flight event state → evaluate objectives → take the standing snapshot → write chronicle, honour and achievement records → release deferred claims, with all publication at P7. Seventeen contracts **`WPC-01`…`WPC-17`** bind B-02…B-10 and Prompts 12–15; every contract names its producer, consumer, data, phase, failure behaviour and owning rule.

**Rewards, security, privacy and history.** Rewards are one of six classes (`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`) and are refused if they would create a permanent yield multiplier, a purchasable standing or a repeatable transfer. Every grant carries an achievement key `(nation_id, achievement_id, achievement_version, scope_key, tier_id)`, is ledgered once and is reconciled at P7 under `ECN-101`/`ECN-111`. Section 18 records **24 abuse scenarios**, idempotency and atomicity tables; section 19 records the disclosure rules, including B-10's combat-detail boundary and the alliance `k ≥ 5` aggregate rule (`WEP-335`); section 20 defines **40 `WPF-` failure codes**; section 21 defines **50 `WPA-` audit events**, the P-class chronicle bar (`WEP-681`) and the correction-is-appended rule.

**Traceability, requirements and decisions.** Section 23 dispositions every `11A-CR-001`…`11A-CR-030` and `11A-OPEN-001`…`11A-OPEN-016`, adds **REQ-704…REQ-763** (60 rows: 30 adopted candidate requirements and 30 specification requirements), and contains the rule-range traceability matrix. Section 24 handles **D-144…D-161** and **DD-192…DD-209** row by row. Ten new decisions were made autonomously under D-014: **D-152** (canonical path and namespaces), **D-153** (objective terminology), **D-154** (event system), **D-155** (objective system), **D-156** (standing system), **D-157** (progression system), **D-158** (chronicle quality bar, resolving **UD-024**), **D-159** (reward catalogue), **D-160** (alliance recognition) and **D-161** (warfare receipt rule), mirrored as **DD-200…DD-209**. Two new unresolved matters were opened because the missing evidence belongs to another prompt: **UD-050** (alliance standings at plausible membership sizes; Prompt 12/14) and **UD-051** (the material-reward rarity bound; Prompt 14).

**Owner-reserved decisions and gates.** `UD-040`–`UD-049` remain **Open / Yes — owner**; none was resolved, narrowed or bypassed. No Global Trade gate was marked met. No provisional number was promoted. No candidate was treated as approved because 11A listed it.

**Documentation validators executed.** Every command was run against the final working tree on **2026-11-05**. They are **document checks, not gameplay tests**.

| Command | Result | Exit |
|---|---|---|
| `python 11B_validate_b11.py --self-test` | **checks passed 50/50**, **positive fixtures 8/8**, **negative fixtures 23/23**, `RESULT: PASS — specification and fixtures are internally consistent at the documentation level` | 0 |
| `python 09_validate.py` | **361/361 checks passed**, `ALL CHECKS PASSED` | 0 |
| `python test_decision_registers.py` | **Ran 12 tests — OK** | 0 |
| `python test_next_action.py` | **Ran 27 tests — OK** | 0 |
| `python validate_links.py` | **Unresolved: 0** (count recorded in the acceptance report; every new file and section anchor resolved) | 0 |

The 11B validator parses the rule IDs and formula blocks rather than trusting a count in prose, enforces the twenty formula fields, resolves every `F-WEP-` reference, checks the twelve state machines, the seventeen contracts, the failure and audit catalogues, the requirement and decision ranges, the `11A-CR`/`11A-OPEN` dispositions, the owner-reserved rows, the Global Trade gate state and the Prompt 11C handoff. Its 23 negative fixtures each mutate a copy of the parsed model and must fail for the stated reason (missing lifecycle, missing eligibility, missing completion validation, missing formula, duplicate ID, undefined variable, missing rounding or snapshot, invalid tie-break, unbounded stacking, duplicate claim, broken history correction, invalid source reference, broken B-10 privacy, alliance command escalation, gate promotion, owner-reserved resolution, missing D-014, missing consent rule, unjustified provisional, missing Prompt 14 dependency and missing 11C handoff). No check was deleted or weakened to obtain a pass, and no fixture was dropped.

**D-014 and owner-reserved results.** Category A changed nothing. Category B is the ten decisions above. Category C is the provisional-parameter set: B-11 structural formulas and inherited approved constants retain their documented classifications and approval status; all unapproved numerical calibration parameters remain provisional and require Prompt 14 review; **Structural formulas containing provisional parameters are structurally specified but are not numerically finalized.** Category D took no external, costly or irreversible action: **nothing was committed, pushed, published or deployed**.

**Synchronization performed.** `docs/DECISIONS.md` (D-152…D-161 and the header), `stage-2/04` (v3.17, DD-200…DD-209, tallies 209 positions / 161 decisions), `stage-2/03` (v1.35, REQ-704…REQ-763, counts 55 Approved / 688 Provisional / 19 Open / 1 Deferred / 0 Proposed = 763), `stage-2/05` (v1.29, UD-024 resolved by D-158, UD-050/UD-051 opened; 28 Resolved / 3 Deferred / 20 Open = 51), `stage-2/02` (the B-11 entry and §5 next-prompt row), `stage-2/01` (sub-prompt register and row 11), `stage-2/00` (banner, status and next action), this log (header, row 11 and §68), `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/qa_backups/status_rules.py`, `test_next_action.py`, `test_decision_registers.py` and `09_validate.py`.

**Limitations.** Documentation and document-validator evidence only. **No gameplay, runtime, database, browser, load, security, privacy-enforcement or playability test exists or was run**, because no B-11 implementation exists. Balance, live fairness, abuse resistance in practice, free-tier storage cost, player comprehension and the numerical viability of `k = 5` are **not proven** and are assigned to Prompts 12, 13, 14 and Stage 3. No event fired, no objective progressed, no standing was computed and no reward was granted.

**Final verdict.** **PASS — PROMPT 11B COMPLETE AT THE SYSTEM-SPECIFICATION LEVEL.** The two canonical deliverables exist and are internally consistent, all four domains are specified, the formula register resolves every calculation, the state machines and contracts are complete, the failure and audit catalogues are complete, every research row is dispositioned, the registers and continuity files are synchronized, every executed validator is green, and no gate became PASS merely because this record was written. **Implementation authorization: NONE** — and none was performed. **Prompt 11C has not started.**


## 69. Prompt 11B-C — Reward-class, provisional-status and 52-gate acceptance corrections (2026-11-05)

**Scope.** A targeted correction pass over the completed Prompt 11B specification. It corrects three closeout inconsistencies, adds an evidence-based acceptance crosswalk for the original fifty-two Prompt 11B gates, extends the B-11 validator, and synchronizes the status surfaces. **No B-11 rule, formula, formula classification, state machine, contract, reward mechanic or design decision was redesigned.** Documentation and traceability only; no code, migration, deployment or runtime test exists.

**Correction 1 — reward classes.** The authoritative set in `WEP-499` and **D-159** is `RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`. The 11B progress-log summary had listed MATERIAL and COSMETIC before an unsupported third token, “ACCESS”, which introduced a seventh class. The log entry was corrected to the authoritative six. A project-wide search found no other six-class list; `ACCESS` remains valid where it means access control (`WEP-656`), not a reward class. The validator now extracts the class set from `WEP-499`, cross-checks D-159 and every six-name list in the status documents, and rejects `ACCESS` as a class (`B11-51`, `B11-52`; `NEG-34`).

**Correction 2 — provisional-number precision.** The per-formula field 20 is authoritative, and the correction pass verified it rather than trusting the previous prose. The actual result is **44 structural formulas and 6 provisional formulas** (`F-WEP-011`, `021`, `029`, `030`, `033`, `046`). Of the 44 structural formulas, **20 contain a Prompt 14 parameter** and **24 contain no calibration parameter**. The register's earlier derived counts (41 structural / 9 provisional / seven structural-with-parameter) did not match field 20: `F-WEP-031` and `F-WEP-036` were counted as provisional in prose while field 20 marks them structural, and the “further seven” list omitted most of the structural formulas that carry a Prompt 14 parameter. The derived counts and lists were corrected in both places (§1 and the closing summary); **no formula was reclassified**. The five status banners and the §68 D-014 paragraph now use the precise statement that structural formulas and inherited approved constants retain their documented status, unapproved calibration parameters remain provisional for Prompt 14, and structural formulas containing provisional parameters are structurally specified but not numerically finalized (`B11-53`, `B11-54`; `NEG-35`, `NEG-36`).

**Correction 3 — original 52-gate crosswalk.** The original Prompt 11B §23 gates `P11B-01`…`P11B-52` were recovered from the original prompt as recorded in the project conversation and preserved verbatim in [`18_world_events_objectives_rankings_progression_acceptance_crosswalk.md`](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md). The crosswalk records, for every gate, the original criterion, primary evidence, supporting evidence, validator coverage, status, explanation and any remaining action. **Actual status: 52 PASS, 0 PARTIAL, 0 FAIL, 0 BLOCKED; 0 missing evidence; 0 invalid evidence references.** The crosswalk and the validator keep the 52 prompt gates separate from the **59** `B11-` checks, the positive and negative fixtures, and the link validator. A gate is never passed because a related document exists or because a validator check passed.

**Validator changes.** `11B_validate_b11.py` now has **59 checks** (`B11-01`…`B11-59`). The nine new checks cover the authoritative reward set, reward-summary consistency, field-20 formula classification, precise provisional wording, crosswalk completeness, status-count integrity, PASS-evidence resolution, requirement-to-rule references and gate/check separation. Fixtures now total **11 positive and 36 negative**; the new negatives reject a missing gate, a duplicate gate, an unknown gate, a PASS with no evidence, a PASS with a broken file reference, a PASS with a nonexistent rule ID, a PARTIAL or BLOCKED gate counted in the PASS total, a mismatched gate count, a check count presented as a gate count, a reintroduced `ACCESS` class, a stale formula count and overbroad provisional wording. Each negative fails for its stated reason. The report prints gate coverage, validator checks, positive fixtures, negative fixtures and documentation-link validation in separate sections.

**Documentation validators executed on 2026-11-05.** These are document checks, not gameplay tests.

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/11B_validate_b11.py --self-test` | **checks 59/59; positive fixtures 11/11; negative fixtures 36/36; gates 52 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED; 0 missing evidence; 0 invalid references** | 0 |
| `python docs/qa_backups/09_validate.py` | **361/361 checks passed** | 0 |
| `python docs/qa_backups/test_decision_registers.py` | **Ran 12 tests — OK** | 0 |
| `python docs/qa_backups/test_next_action.py` | **Ran 27 tests — OK** | 0 |
| `python docs/qa_backups/validate_links.py` | **72 files, 3358 links, 2976 local, 382 external skipped, 29 anchors, Unresolved: 0** | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | **1036 checks**, 73/73 negative fixtures rejected, `PASS` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | **943 checks**, `PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | **34 semantic checks**, `[PASS]` | 0 |
| `python docs/qa_backups/verify_economy_numbers.py` | **164/164** | 0 |
| `python docs/qa_backups/verify_city_numbers.py` | **267/267** | 0 |
| `python docs/qa_backups/verify_politics_numbers.py` | **879/879** | 0 |
| `python docs/qa_backups/verify_alliance_numbers.py` | `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/verify_diplomacy_numbers.py` | 9 groups, 0 failed | 0 |
| `python docs/qa_backups/verify_market_numbers.py` | `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/verify_diplomacy_workflows.py` | 17 groups, 0 failed | 0 |
| `python docs/qa_backups/verify_market_workflows.py` | `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/verify_alliance_workflows.py` | `ALL CHECKS PASSED` | 0 |
| `python -m py_compile` on the modified validators | `PY_COMPILE OK` | 0 |

Three legacy validators (`09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `10B_validate_warfare.py`) still asserted the pre-11B register maxima and the pre-11C sub-prompt. Their expectations were advanced to the current register facts (763 requirements, 55/688/19/1/0; 209 DD positions, 130/51/22/2/2/1/1; 28 Resolved / 3 Deferred / 20 Open = 51; current sub-prompt 11C). No check was deleted or weakened; this is the same literal-maintenance performed for `09_validate.py` at earlier prompt boundaries.

**Files changed in this pass.** `docs/stage-2/18_world_events_objectives_rankings_progression.md` (crosswalk link, acceptance record, precise status wording), `docs/stage-2/18_world_events_objectives_rankings_progression_formula_register.md` (derived counts and precise status wording), the new crosswalk file, `docs/qa_backups/11B_validate_b11.py` (59 checks, 47 fixtures, separated report, link invocation), `docs/qa_backups/09A_validate_alliance.py`, `docs/qa_backups/09B_validate_alliance_semantic.py` and `docs/qa_backups/10B_validate_warfare.py` (current register literals and sub-prompt), `docs/stage-2/06_stage_2_progress_log.md` (this entry and header), `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md` and `docs/ROADMAP.md`.

**D-014 and owner-reserved results.** The three corrections are ordinary documentation and traceability decisions under D-014; they create no design decision and no new decision ID. `UD-040`–`UD-049` remain **Open / Yes — owner**; `UD-024` remains Resolved by D-158; `UD-050`/`UD-051` remain Open. Global Trade gates are unchanged. No owner approval is inferred and no unresolved decision is closed.

**Limitations.** Documentation and document-validator evidence only. No gameplay, runtime, database, browser, load, security, privacy-enforcement or playability test exists or was run. Validator success is not runtime proof; specification completion is not implementation, balance or release readiness.

**Final verdict.** **PASS — Prompt 11B-C complete; Prompt 11B may be closed at the system-specification level.** All 52 original gates are accounted for and PASS with resolving evidence, the reward-class and provisional-status inconsistencies are corrected, the validator and fixtures pass, links and compilation pass, and the status surfaces agree. **Prompt 11C has not started.**


## 70. Prompt 11B-C2 — Source provenance, independent gate audit and reward-formula retirement (2026-11-05)

**Scope.** A narrow integrity-correction pass over the completed Prompt 11B and 11B-C work. It corrects four findings (A–D), preserves the original 52 acceptance criteria in a hashed source artifact, independently re-audits every gate against its cited evidence, and retires one formula that had no lawful use case. **No gameplay mechanic, no other rule, no formula classification, no decision and no owner-reserved matter was redesigned.** Documentation and traceability only; no code, migration, deployment or runtime test exists.

**Finding A — provisional-status summaries.** The `b11_progression` rows in `AI_CONTEXT.md` and `PROJECT_PROGRESS.md` had described all B-11 numbers as provisional for Prompt 14. That statement is false for structural formulas and inherited approved constants. Both rows now use the precise baseline: 50 formula IDs (49 active and `F-WEP-048` retired), 43 active structural (20 with Prompt 14 parameters, 23 without) and 6 Provisional; structural formulas and inherited approved constants retain their documented status; only unapproved calibration remains with Prompt 14. The same precise statement is present in `AI_HANDOFF.md`, `ROADMAP.md`, `00_stage_2_handoff.md` and the formula register. `B11-54` now scans only active B-11 status lines and rejects the exact stale sentence plus three semantic variants (`all numbers/values/formulas/parameters are provisional`, `every number is provisional`, and a false calibrated/completed claim). `NEG-36`, `NEG-37` and `NEG-38` inject the defect into the handoff, `AI_CONTEXT` and `PROJECT_PROGRESS`; `POS-12` retains the accurate wording.

**Finding B — original 52-gate provenance and independent audit.** The original Prompt 11B §23 criteria were recovered from the preserved conversation record, not from the crosswalk. The record is `C:/Users/suren/.qoder/projects/C--Users-suren-Downloads-Project-X/0f46245a-8c76-4433-b4d6-cfa63d424147.jsonl`, line 3, role `user`, `message.content[].text`, timestamp `2026-11-05T09:33:08.190Z`, section `# 23. FINAL PROMPT 11B ACCEPTANCE GATES` through the line before `# 24. IMPLEMENTATION AND WORKFLOW BOUNDARIES`. The whole Prompt 11B message is 68,161 characters and hashes to `5b45dfe230862d3527aaa089a83807929c92dc0c20af6c78710532d494f307a8`. The 52-row gate table is preserved verbatim in [`18_world_events_objectives_rankings_progression_acceptance_source.md`](18_world_events_objectives_rankings_progression_acceptance_source.md) between machine-readable markers; its block hash is `d2e6c35e1b85f772a5b8273e821a62bcf5b3af406c2c3d42e96fea379086f766`. The hash proves the preserved block has not changed since extraction; it does not prove authorship or semantic sufficiency.

Every crosswalk criterion was compared character-for-character to the source: **52 identifiers, 52 criteria and their order match exactly**. The audit did find and correct six wrong section citations in the crosswalk (`P11B-08` WEP-099 is §6 not §13; `P11B-13` WEP-232 is §7 not §13; `P11B-23` WEP-487 is §10 not §9; `P11B-28` WEP-585 is §14 not §15; `P11B-40` now cites §19 WEP-659 rather than §18 WEP-647; `P11B-42` WEP-692a is correctly in §23). A path plus an identifier is not sufficient evidence: `B11-57` now also verifies that a cited `WEP-` rule actually belongs to the cited section of the main specification. `NEG-43` reintroduces the WEP-099/§13 mismatch and must fail.

The independent audit also found that mandatory check #20 of the original brief — **all 11A recommendations have a recorded disposition** — was not met. Eight `11A-DR` IDs (`002`, `003`, `017`, `020`, `022`, `023`, `026`, `028`) appeared nowhere, and no 34-row disposition existed. A disposition table was added in §23.1, immediately after the existing `WEP-692`; it records `ADOPTED`, `REJECTED` or `NOT APPLICABLE` and a rule/decision locator for every recommendation. No new `WEP-` ID was created and no rule meaning changed. `B11-20` now requires all 34 rows with a valid disposition and locator; `NEG-44` removes one row and must fail; `POS-16` retains the valid table.

**Finding C — requirement identifier resolution.** `B11-58` now resolves every non-formula `WEP-` reference in `REQ-704`…`REQ-763` against the parsed canonical rule set (plus the lettered `WEP-692a`), rejects malformed IDs, nonexistent IDs, inverted ranges and ranges whose endpoints exist but whose interior IDs do not. `NEG-39` changes a valid `WEP-499…WEP-514` range to `WEP-499…WEP-999` and must fail for that reason; `POS-13` retains a fully resolvable requirement set.

**Finding D — `F-WEP-048` retired.** `F-WEP-048` allocated a numeric total among contributors. Its only rule references were `WEP-548` and `WEP-555`, neither of which authorizes a collective material pool; `WEP-515` makes the recipient the nation satisfying the condition, `WEP-519` makes event participation explicit, `WEP-540` permits only a system grant from an authorized pool, and `WEP-541` forbids alliance-funded and nation-to-nation prizes. No authorized non-Alliance collective material-reward use exists. The formula is therefore **Retired**, not Provisional and not Structural: no active calculation, no active rule reference and no lawful funding source. The register now reports 50 IDs (49 active + 1 retired), 43 active structural, 6 Provisional, 20 with Prompt 14 parameters and 23 without. `WEP-540`, `WEP-541`, `WEP-548`, `WEP-555`, `WEP-499`–`WEP-556`, `ALL-224`, `D-159` and `D-160` are unchanged. `NEG-35` reclassifies the retired formula as Structural and must fail.

**Validator changes.** `11B_validate_b11.py` now has **61 checks** (`B11-01`…`B11-61`) and **16 positive + 44 negative fixtures**. The new checks are `B11-60` (source artifact exists, markers present, block hash equals the preserved hash, 52 ordered IDs with non-empty criteria and provenance fields) and `B11-61` (crosswalk criteria and order equal the source exactly, statuses valid, explanation and remaining action non-empty). The nine earlier checks are retained. `B11-57` is strengthened as described. Neither `B11-60` nor `B11-61` claims authenticity or semantic quality.

**Documentation validators executed on 2026-11-05.** Document checks, not gameplay tests.

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/11B_validate_b11.py --self-test` | **checks 61/61; positive fixtures 16/16; negative fixtures 44/44; gates 52 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED; 0 missing evidence; 0 invalid references** | 0 |
| `python docs/qa_backups/09_validate.py` | **361/361 checks passed** | 0 |
| `python docs/qa_backups/test_decision_registers.py` | **Ran 12 tests — OK** | 0 |
| `python docs/qa_backups/test_next_action.py` | **Ran 27 tests — OK** | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | **1036 checks**, 73/73 negative fixtures rejected, `PASS` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | **943 checks**, `PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | **34 semantic checks**, `[PASS]` | 0 |
| `python docs/qa_backups/verify_economy_numbers.py` | **164/164** | 0 |
| `python docs/qa_backups/verify_city_numbers.py` | **267/267** | 0 |
| `python docs/qa_backups/verify_politics_numbers.py` | **879/879** | 0 |
| `python docs/qa_backups/verify_alliance_numbers.py` | `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/verify_diplomacy_numbers.py` | 9 groups, 0 failed | 0 |
| `python docs/qa_backups/verify_market_numbers.py` | `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/verify_diplomacy_workflows.py` | 17 groups, 0 failed | 0 |
| `python docs/qa_backups/verify_market_workflows.py` | `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/verify_alliance_workflows.py` | `ALL CHECKS PASSED` | 0 |
| `python -m py_compile` on the modified validators | `PY_COMPILE OK` | 0 |
| `python docs/qa_backups/validate_links.py` | **2990 local links, 382 external skipped, 29 anchors, Unresolved: 0** | 0 |

**Git scope in this pass.** The working tree was not reset, cleaned, staged, committed, pushed or published. The pre-existing unrelated modifications and untracked files recorded at the start of the prompt were preserved. The C2 pass changed exactly: the B-11 rulebook (the 34-row `11A-DR` disposition under WEP-692, the header/acceptance record and the `F-WEP-048` note); the formula register (retirement, derived counts and header); the crosswalk (source comparison, six section-citation repairs, audit record and current counts); the new acceptance source artifact; the progress log (this entry and header); the five status/handoff surfaces (`AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `ROADMAP.md`, `00_stage_2_handoff.md`); the prompt roadmap row 11; the B-11 validator (B11-20 strengthening, B11-54/57/58/60/61 and fixtures); and the `09B_validate_alliance_semantic.py` printed status line. No other validator or historical record was edited. No historical log entry was deleted or rewritten.

**Superseded and blocked prior claims.** The 11B-C entry (§69) is retained as history. Its claims that the correction was complete, that the crosswalk was 52 PASS with no independent source audit, that the validator had 59 checks and 47 fixtures, and that the register had 44 active structural formulas are **superseded by this entry**: the current counts are 61 checks, 60 fixtures, 49 active + 1 retired formulas and 43 active structural. Its statement that the original gates were "recovered from the original prompt" was a claim without a preserved, hashed artifact; the artifact now exists. §68's formula count likewise predates the retirement of `F-WEP-048`. No earlier claim is treated as evidence for this pass.

**D-014 and owner-reserved results.** The corrections are ordinary documentation and traceability work under D-014. They create no decision ID, resolve no owner-reserved question and change no Global Trade gate. `UD-040`–`UD-049` remain Open; `UD-024` remains resolved by D-158; `UD-050`/`UD-051` remain Open.

**Limitations.** Documentation and document-validator evidence only. No gameplay, runtime, database, browser, load, security, privacy-enforcement or playability test exists or was run. All 52 gate rows are PASS on documentary evidence, but **B11-60/B11-61 do not prove semantic quality, authorship or runtime behaviour**, and **independent acceptance of this correction has not been recorded**.

**Final verdict.** **PARTIAL — 11B-C2 corrections applied and locally verified; independent acceptance pending.** The original criteria are preserved and matched, the source and crosswalk checks pass, the 11A recommendation gap is closed, `F-WEP-048` is lawfully retired, the status surfaces agree and every executed validator is green. **Prompt 11C has been executed after the C3 acceptance. Prompt 14 calibration has not started.**

*(Superseded by §71: the original transcript and a genuine change baseline were located; 11B-C2 received FULL PASS on 2026-11-05, and Prompt 11C is complete at the specification/documentation level (log §72).)*


## 71. Prompt 11B-C3 — Independent source authentication, change-scope verification and final acceptance (2026-11-05)

**Scope.** An independent closeout audit of Prompt 11B-C2. It located and verified the original Prompt 11B transcript record, recovered a genuine pre-C2 baseline, rechecked the four C2 corrections and reran the B-11 validator and the requested regression suite. It made no B-11 design change, no gameplay change, no formula rebalance and no owner-reserved decision change.

**Source authentication result — PASS.** The claimed transcript path exists and was read directly: `C:/Users/suren/.qoder/projects/C--Users-suren-Downloads-Project-X/0f46245a-8c76-4433-b4d6-cfa63d424147.jsonl`, line 3. The record is role `user`, timestamp `2026-11-05T09:33:08.190Z`, session `0f46245a-8c76-4433-b4d6-cfa63d424147`, UUID `aeb56dd3-a6c4-4ff7-886f-895cc49ae97b`, written by Qoder `1.1.79-hotfix.7` with recorded cwd `C:\Users\suren\Downloads\Project X` and branch `prototype/free-tier-feasibility`.

| Check | Result |
|---|---|
| Message text length | 68,161 characters; 68,291 UTF-8 bytes |
| Recomputed message SHA-256 | `5b45dfe230862d3527aaa089a83807929c92dc0c20af6c78710532d494f307a8` — matches |
| Raw line-3 bytes / SHA-256 | 142,789 bytes / `a33274dadf252d1786117d9bc75996b3ae96b881979a265690d8ac23211a27d9` |
| Gate-block SHA-256 | `d2e6c35e1b85f772a5b8273e821a62bcf5b3af406c2c3d42e96fea379086f766` — matches |
| Gate IDs | 52; exactly `P11B-01`…`P11B-52` once each, in order |
| Source artifact vs original | All 52 criteria exact |
| Crosswalk vs original | All 52 criteria exact |
| Imported conversation attachment | Does not contain Prompt 11B (it is the 08A attachment); not used as evidence |

The transcript file is the live session log and continues to append, so its whole-file hash changes; the line-3 raw record and message-text hash are the stable identity. This authenticates the record content, not the authorship of the prompt.

**Change-scope result — PASS.** A genuine baseline was located: `C:/Users/suren/Downloads/Project X (61).zip`, 66,877,694 bytes, SHA-256 `fbc7a054cfa626a2fa19e3325a714c2704518ed6f2e719d687b8b617495e9e77`, archive timestamp 2026-11-05 16:02. The C2 result snapshot is `C:/Users/suren/Downloads/Project X (62).zip`, 67,114,711 bytes, SHA-256 `a174c18f5515fc2a4b05b0de864bef97fb4f176523132984522913f740b49c76`, timestamp 18:14. Both archives passed `zipfile.testzip()` and contain the project's `.git` state at the same branch/HEAD (`prototype/free-tier-feasibility` / `8f4e20e`).

Hash comparison of every file, excluding `.git/`, `.cloud-attachments/`, `.freebuff/`, `__pycache__/` and `node_modules/`, gives **1 added, 12 modified, 0 deleted, 0 renames**. The only added file is the acceptance source artifact. All 12 modified files are B-11 specification, B-11 validator or B-11 status surfaces. No B-02…B-10 rulebook, formula register, decision register, unresolved-decision register or unrelated Stage 2 system changed. The current workspace is byte-identical to the C2 snapshot under the same exclusions (0 added, 0 deleted, 0 modified). The file-by-file manifest with before/after hashes is [`18_world_events_objectives_rankings_progression_c2_change_manifest.md`](18_world_events_objectives_rankings_progression_c2_change_manifest.md).

The baseline itself contains 81 pre-existing porcelain entries from earlier prompts (including modified `DECISIONS.md`, `08_sweep_result.txt`, `09_validate.py`, `validate_final.py` and two Stage 1 files). Their hashes are identical in both archives, so they are **not** C2 changes and were preserved. No unknown-origin change exists inside the C2 set.

**C2 correction recheck — PASS.** `B11-53` reports 6 Provisional, 43 active Structural, 20 structural with Prompt 14 parameters, 23 without, and `F-WEP-048` retired. `B11-54` reports no missing precise wording and no overbroad B-11 status line. `B11-58` resolves 60/60 B-11 requirement rows with no reference problem. `B11-60` reports 52 source rows and the preserved hash. `B11-61` reports 52 matching crosswalk criteria and no wording problem. `B11-20` reports 30/30 candidate requirements and 34/34 recommendations dispositioned.

`F-WEP-048` remains **Retired**: field 5 is `None — retired. No active calculation.` and field 20 is `**Retired**`. Every mention outside the block is historical, index/count text or the `WEP-683` retirement note; it has no active rule reference. `WEP-515`, `WEP-519`, `WEP-540`, `WEP-541`, `WEP-548`, `WEP-555`, `WEP-499` and `ALL-224`, plus `D-159` and `D-160`, are byte-identical between the baseline and the C2 snapshot. The six reward classes remain `RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`.

**Validator and regression results (2026-11-05).** Documentation checks only.

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/11B_validate_b11.py --self-test` | 723 rules, 50 formula IDs, **61/61 checks**, **52 gate rows PASS**, 16/16 positive, 44/44 negative, 0 missing evidence, 0 invalid refs | 0 |
| `python docs/qa_backups/validate_links.py` | 2,991 local links, 382 external skipped, 29 anchors, **Unresolved 0** | 0 |
| `python -m compileall -q docs/qa_backups/11B_validate_b11.py docs/qa_backups/status_rules.py` | No output; success | 0 |
| `python docs/qa_backups/09_validate.py` | 361/361 checks passed | 0 |
| `python docs/qa_backups/test_decision_registers.py` | 12 tests OK | 0 |
| `python docs/qa_backups/test_next_action.py` | 27 tests OK | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | 1,036 checks; 73/73 negatives rejected; CF-01/CF-02 pass | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | 943 checks; PASS | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | 34 semantic checks; `[PASS]` | 0 |
| `python docs/qa_backups/verify_economy_numbers.py` | 164/164 | 0 |
| `python docs/qa_backups/verify_city_numbers.py` | 267/267 | 0 |
| `python docs/qa_backups/verify_politics_numbers.py` | 879/879 | 0 |
| `python docs/qa_backups/verify_alliance_numbers.py` | ALL CHECKS PASSED | 0 |
| `python docs/qa_backups/verify_diplomacy_numbers.py` | 9 groups, 0 failed | 0 |
| `python docs/qa_backups/verify_market_numbers.py` | ALL CHECKS PASSED | 0 |
| `python docs/qa_backups/verify_diplomacy_workflows.py` | 17 groups, 0 failed | 0 |
| `python docs/qa_backups/verify_market_workflows.py` | ALL CHECKS PASSED | 0 |
| `python docs/qa_backups/verify_alliance_workflows.py` | ALL CHECKS PASSED | 0 |
| `python docs/qa_backups/verify_warfare_workflows.py` | 49 checks executed; 0 failed | 0 |

**Files changed by C3.** **Added (1):** `docs/stage-2/18_world_events_objectives_rankings_progression_c2_change_manifest.md`. **Modified (12):** `docs/stage-2/18_world_events_objectives_rankings_progression_acceptance_source.md` (authentication record), `docs/stage-2/18_world_events_objectives_rankings_progression_acceptance_crosswalk.md` (source authentication, audit limits, gate evidence, closeout), `docs/stage-2/18_world_events_objectives_rankings_progression.md` (acceptance record and header), `docs/stage-2/18_world_events_objectives_rankings_progression_formula_register.md` (header only), `docs/stage-2/06_stage_2_progress_log.md` (this section and header), `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` and `docs/stage-2/01_stage_2_prompt_roadmap.md` (status synchronization) and `docs/qa_backups/09B_validate_alliance_semantic.py` (printed status sentence only). **Deleted (0).** No B-11 rule, formula, fixture, validator check, decision or requirement was changed by C3.

**Owner-reserved and boundary results.** `UD-040`–`UD-049` remain Open; `UD-024` remains resolved by D-158; `UD-050`/`UD-051` remain Open. No Global Trade gate was promoted. C3 created no decisions and no requirements. No staging, commit, push or publication occurred.

**Limitations.** The authentication proves the located line-3 record and its hashes match the artifact and crosswalk; it does not cryptographically prove who authored the prompt. The baseline is a local ZIP snapshot, not a signed artefact, though its content and `.git` state are consistent. All validator evidence is documentary. No gameplay, runtime, database, load, security, privacy-enforcement or playability test exists; balance and release readiness are not proven.

**Outstanding owner actions.** None for source authentication or change scope. If a future audit requires cryptographic authorship proof, the owner would need to supply a signed or independently witnessed copy of the original Prompt 11B message.

**Final decision.** **FULL PASS — Prompt 11B-C2 independently accepted on 2026-11-05.** All C3 acceptance requirements C3-01…C3-14 are supported. **Prompt 11C is authorized to begin but has not started. Prompt 14 calibration has not started.**
*(Superseded on 2026-11-06 by §72: Prompt 11C is now complete at the specification/documentation level.)*

## 72. Prompt 11C — B-11 workflows, cross-system integration and acceptance (2026-11-06)

**Scope.** Tasks A–M of Prompt 11C: end-to-end player and administrative journeys, implementation-ready workflows for the four B-11 lifecycles, the cross-system integration matrix and dependency graph, the security and privacy analysis with a threat register, edge cases and concurrency, the acceptance-test suite, bidirectional traceability, an independent validator, the developer handoff, project-wide documentation synchronization, and an evidence-based gate assessment. **Documentation, specification and QA artefacts only.** No gameplay code, migration, API, screen, deployment, hosting change, runtime test, executed acceptance test, load test, security test or calibrated value exists or is claimed, and no Prompt 12/13/14/15 work was started.

**Canonical deliverable.** [`19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md`](19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md) — 34 sections. Identifier spaces created: `WJ-001`…`WJ-025` (25 journeys × 17 fields), `WWF-001`…`WWF-050` (50 workflows × 14 fields), `WEE-001`…`WEE-084` (84 edge cases), `WTA-001`…`WTA-272` (272 tests in 16 classes), `WTS-001`…`WTS-030` (30 threats), `WEG-01`…`WEG-11` (11 registered specification gaps), `INV-01`…`INV-09`, `P11C-01`…`P11C-20` (gates), `11C-01`…`11C-31` (validator checks). No new `WEP-`, `F-WEP-`, `WPC-`, `WPF-`, `WPA-` or `REQ-` identifier was created; the 17 `WPC-` contracts and the closed `WPF-01`…`WPF-40` / `WPA-01`…`WPA-50` catalogues are **reused**, and the `WIG-` prefix was considered and deliberately not adopted (§0.6).

**Design preservation, verified by execution rather than asserted.** The formula classification stays **43 active Structural (20 carrying a Prompt 14 parameter, 23 not) + 6 Provisional (`F-WEP-011`, `F-WEP-021`, `F-WEP-029`, `F-WEP-030`, `F-WEP-033`, `F-WEP-046`) + 1 Retired (`F-WEP-048`)**, recomputed from register field 20 by `11C-14`. The six reward classes (`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`), the four event classes, five triggers, twelve objective categories, ten standings, eight progression layers and `k = 5` are unchanged. `11C-24` verifies every one of the 14 mentions of `F-WEP-048` in the new document is negative: no proportional collective material allocation, alliance-funded prize, inter-nation prize pool or alternative contribution mechanism is introduced anywhere. Nothing was calibrated; Prompt 14 remains the calibration owner (`WEP-700`, `WEP-706`).

**Decisions.** One ordinary Category B decision was recorded: **D-162 / DD-210** — an unauthorized write is refused with the existing `WPF-13` plus `WPA-50`, the closed code set is not extended, and the missing distinct authorization-failure code is registered as gap `WEG-01` for the rulebook owner. DECISIONS.md now holds 162 rows and the design register 210 (tally corrected: **23 Confirmed**, total **210**). `UD-040`…`UD-049` remain Open and owner-reserved; `UD-050` and `UD-051` remain Open; `UD-024` stays resolved by D-158. No Global Trade gate was promoted and no owner approval was invented.

**Executed validation (2026-11-06).** Documentation checks only; every row below is actual output.

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/11C_validate_b11_workflows.py --self-test` | journeys=25 workflows=50 edge=84 tests=272 threats=30 gates=20 checks=31 · **31/31 checks passed, 0 failed** · **POSITIVE 8/8 accepted** · **NEGATIVE 17/17 rejected for the expected reason** · links `Unresolved: 0` | 0 |
| `python docs/qa_backups/11B_validate_b11.py --self-test` | **61/61 checks** · 16/16 positive · **44/44 negative** · all 52 gate rows PASS · links 3065 local / 382 external / 29 anchors / 0 unresolved | 0 |
| `python docs/qa_backups/validate_links.py` | 75 files, 3447 links, 3065 checked locally, 382 external skipped, 29 anchors, **Unresolved 0** | 0 |
| `python docs/qa_backups/09_validate.py` | **361/361 — ALL CHECKS PASSED** | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | 943 checks, **PASS** | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | **[PASS] all 34 semantic checks** | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | 1,036 checks · 73/73 negatives rejected · CF-01/CF-02 PASS · 13 summaries + 7 full | 0 |
| `python docs/qa_backups/test_decision_registers.py` | Ran 12 tests — **OK** | 0 |
| `python docs/qa_backups/test_next_action.py` | Ran 27 tests — **OK** | 0 |
| `verify_economy_numbers.py` / `verify_city_numbers.py` / `verify_politics_numbers.py` | 164/164 · 267/267 · 879/879 | 0 |
| `verify_alliance_numbers.py` / `verify_diplomacy_numbers.py` / `verify_market_numbers.py` | ALL CHECKS PASSED · 9 groups 0 failed · ALL CHECKS PASSED | 0 |
| `verify_diplomacy_workflows.py` / `verify_market_workflows.py` / `verify_alliance_workflows.py` / `verify_warfare_workflows.py` | 17 groups 0 failed · 07C ALL CHECKS PASSED · 49/65/132 ALL CHECKS PASSED · CHECKS 49 EXECUTED 49 FAILED 0 | 0 |
| `python docs/qa_backups/11A_validate_research.py` | 30 executed, **1 FAILED** — check 29 `REQ max 763, D max 162` vs its research-time assumption `REQ-703`. Pre-existing debt `D-1`, **not modified** | 1 |
| `python docs/qa_backups/validate_final.py` | **12 failures — the same twelve pre-existing stale assertions as at the 11C baseline**, two re-rendered with the advanced values. Debt `D-2`, **not weakened, not fixed** | 1 |

**Two defects in 11C's own work that only execution caught.** (1) The status rewrite dropped the clause `only unapproved calibration remains with Prompt 14` from the `b11_progression` row; `11B`'s `NEG-37`/`NEG-38` mutate exactly that clause, so they silently became no-ops and `11B_validate_b11.py` fell to 42/44 and `RESULT: FAIL`. The clause was restored in `AI_CONTEXT.md`, `AI_HANDOFF.md` and `PROJECT_PROGRESS.md`; no fixture or check was edited. (2) Adding DD-210 raised the declared register total to 210 while the `Confirmed` tally row still read 22, so the status rows summed to 209; `09B` C17 reported it and the register was corrected to 23 Confirmed. Both are recorded in §32.5a and as debt `D-10`, together with `D-9`, which names the recurring hazard that five continuity suites hard-code the live prompt and register totals and must be advanced on every prompt (this pass advanced `09_validate.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `test_decision_registers.py` and `test_next_action.py`, each with a dated comment).

**Acceptance gate result.** `P11C-01`…`P11C-20` assessed individually against existing evidence: **12 PASS · 8 PARTIAL · 0 FAIL · 0 BLOCKED · 0 NOT RUN · 0 NOT APPLICABLE**, recomputed from the rows by `11C-29`. The eight PARTIAL gates are `P11C-05` (ranking workflows conditional on the two owner-blocked branches and the Global Trade gate), `P11C-06` (progression workflows conditional on `UD-051` reward rarity and on runtime observation), `P11C-09` (security controls specified but never enforced, and the prototype defect open), `P11C-10` (`k = 5` and the visibility matrix documented, enforcement unproven, `UD-050` open), `P11C-14` (category 14 blocked without an approved capacity target; all 272 tests `Execution: NOT RUN`), `P11C-15` (two owner-blocked branches and eleven registered gaps stay open by design), `P11C-17` (the two pre-existing failing suites above) and `P11C-20` (no independent reviewer signed this pass). No gate was marked PASS because the validator ran successfully.

**Security posture stated honestly.** §16 documents controls; §16.6 states that the Supabase feasibility prototype remains client-writable on `profiles.treasury` (`grant update … to authenticated` plus a row-scoped `UPDATE` policy) and is **not security-verified**. Its architectural implication for B-11 is stated in §16.6 and carried into §31: no B-11 table, workflow or contract may inherit a pattern where a player-writable column holds a value another subsystem owns, and the production architecture must place reward value where the store — not a policy that can be widened — denies the write. Nothing in this pass re-tested the prototype at runtime.

**Files changed by 11C.** **Added (2):** `docs/stage-2/19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md`, `docs/qa_backups/11C_validate_b11_workflows.py` (plus the throwaway synchroniser `docs/qa_backups/11C_sync_docs.py`). **Modified:** `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/DECISIONS.md` (D-162), `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, `docs/stage-2/04_approved_and_provisional_decisions.md` (DD-210, tally and narrative), `docs/stage-2/06_stage_2_progress_log.md` (this entry), and the five continuity suites named in `D-9`. **Deleted (0).** No B-11 rule, formula, contract, failure code, audit event, requirement or owner-reserved decision was changed; `docs/stage-2/18_*`, `03_requirements_traceability.md`, `05_unresolved_design_decisions.md`, `prototypes/`, `status_rules.py`, `validate_final.py`, `11A_validate_research.py`, `11B_validate_b11.py` and every other validator are **unchanged by this prompt** (several of them were already modified in the working tree by earlier, unrelated prompts).

**Git.** No commit, checkpoint, staging, stash, branch or cleanup operation was performed; the pre-existing working-tree state was preserved as found.

**Limitations.** No event fired, no objective progressed, no standing computed, no reward granted, no privacy suppression executed, no race resolved and no screen rendered. The validator proves internal consistency and reference integrity of documentation; it does not prove that any described behaviour works, that any control is enforced, that any cost fits a free tier, or that this pass was independently reviewed.

**Verdict.** **PARTIAL — Prompt 11C complete at the specification/documentation level.** Implementation readiness for the B-11 workflow layer: **CONDITIONALLY READY** — a developer can build against §5–§22 and §31 today, provided the eight §29 owner decisions and the eleven `WEG-` gaps are dispositioned and the §16.6 prototype defect is closed in the production design. **Prompt 12 — fair play, player protection, privacy and administration — is the next roadmap prompt; it has not started and is not authorized to start by this entry (D-002). Prompt 14 calibration has not started. Prompt 11's parent closes only when the owner accepts this PARTIAL verdict.**

---

## 73. Prompt 12A — Fair play, privacy, moderation and administration: research, evidence, requirements and design foundations (2026-11-06)

**Scope.** Research, evidence, requirements and design foundations for Bible part **B-12** across eight interconnected systems: fair play and anti-cheat, multi-account abuse, collusion and coordinated manipulation, privacy and information protection, player reporting and moderation, disciplinary enforcement and appeals, administrative authority and accountability, and security governance and auditability. This is an **A-phase pass**: research and foundations, not a rulebook. It allocated **no** global `REQ-`, wrote **no** B-12 rule, set **no** penalty or duration, finalised **no** permission set, designed **no** workflow or schema, ran **no** production security test, calibrated **no** number, and began no later prompt.

**Authoritative inspection first.** Before any external research the pass read the authority hierarchy, the D-014 autonomy policy, both decision registers, the unresolved-decision register, the requirement register, the Stage-2 prompt roadmap, the Bible outline, the Stage-1 handoff, Report 08's four registers, and every subsystem specification the eight systems touch, plus the Supabase feasibility migrations and grants. §3 of the report records the result as a 16-row table classifying each existing control as **approved design requirement / documented-not-implemented / implemented in a prototype / executed and verified / unverified or blocked**. No control fell in the fourth class: **nothing in this repository has been executed and verified**. Three known issues were checked rather than assumed — the 11A validator's skipped check 29 (still a skip, recorded as debt `D-1`), the stale `validate_final.py` assertions (**12** failures, debt `D-2`, not weakened), and the prototype's client-writable `profiles.treasury` column (**still open**; the published 8/8 permission result does not cover it, and `revoke delete` is not an `update` restriction).

**Canonical deliverables.** Three files in the established research path, using the 07A–11A naming convention:

- [`12A_fair_play_privacy_moderation_administration_research.md`](research/12A_fair_play_privacy_moderation_administration_research.md) — the main report, 33 sections: the five-class baseline, the method and evidence hierarchy, benchmarking coverage, the fair-play foundations (clientless architecture, the 16-category source-of-truth table, the exploit taxonomy, the five evidence states, the value-and-standing versus conduct-sanction split, the six-way behavioural distinction and the eleven false-positive classes), the multi-account, collusion, privacy, information-classification, moderation, disciplinary, reporting, appeals, administrative-authority, separation-of-duties, emergency-authority, auditability, dependency, threat, failure, requirements and decision sections, the legal and operational dependency table, 32 recommendations, and the gate register with the executed-validation record.
- [`12A_sources_and_benchmarks_register.md`](research/12A_sources_and_benchmarks_register.md) — **152** contiguous source rows in five registers, **40** benchmark mechanics, **18** comparator profiles, the retrieval-failure tables and the totals reconciliation.
- [`12A_requirements_integration_and_risk_registers.md`](research/12A_requirements_integration_and_risk_registers.md) — **106** candidate requirements (`12A-CR-001`…`106`) in fifteen fields across all twenty brief categories, **30** twelve-field dependency rows over fifteen systems, **32** eighteen-field threat rows, **15** failure postures, **15** open questions, the 22-rejection quality review, the overlap audit against the fourteen pre-existing Prompt-12 `REQ-` rows and the seven corpus conflicts.

**Decisions.** Fifteen ordinary design positions were taken autonomously under `D-014` and recorded as **D-163…D-177 / DD-211…DD-225**: the 12A/12B/12C split with the B-12 path reserved as `20_fair_play_and_player_protection.md`, the identifier policy, two-class enforcement, the clientless anti-cheat architecture, the five evidence states, the demotion of network evidence, the declared shared-context record, the manufactured-false-agency collusion test, the three-axis information classification, flow-and-outcome offence drafting, administrative authority by prohibition list, the tamper-evident spine with an actively-run verifier, per-category failure postures, the accepted critical residual and the prevention-heavy posture. The registers now hold **177** decisions and **225** design positions. Nine unresolved rows were opened — **UD-052…UD-060** — of which seven are owner-reserved and two are legal (`UD-055`, `UD-060`), taking the register to **60** rows at **28 Resolved / 3 Deferred / 29 Open**. `UD-040`–`UD-049`, `UD-050` and `UD-051` were **not** touched, and no owner-reserved decision was closed, reinterpreted or inferred.

**Executed validation.**

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 35/35 passed; 0 failed`, inventory `sources=152 benchmark=40 comparators=18 candidates=106 dependencies=30 threats=32 postures=15 open-questions=15 recommendations=32 categories=11 · D=177 DD=225 UD=60 REQ max=763` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `POSITIVE FIXTURES: 10/10 accepted`, `NEGATIVE FIXTURES: 15/15 rejected for the expected reason` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --verbose` | 35 per-check lines, each reporting a measured count rather than a heading | 0 |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` (3,527 links found, 3,145 checked locally) — run standalone and again inside check `12A-34` | 0 |
| `python docs/qa_backups/09_validate.py` | `370/370 checks passed — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943`, all passed | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed with no review findings` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | `PASS: all B-10 structure, disposition, formula, register and boundary checks`; 73/73 negative fixtures rejected | 0 |
| `python docs/qa_backups/11B_validate_b11.py`; `11C_validate_b11_workflows.py` | both report `RESULT: PASS` at the documentation level | 0 each |
| the ten `verify_*` scripts (alliance ×2, city, diplomacy ×2, economy, market ×2, politics, warfare workflows) | all pass; politics `879/879`, warfare workflows `49/49` | 0 each |
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — check 29 still asserts its research-era `REQ max 703`; pre-existing debt `D-1`, not modified | 1 |
| `python docs/qa_backups/validate_final.py` | **10** failures, all frontier expectations that predate Prompt 12 (`11B` as next prompt, `REQ-001..703`, `DD-001..199`, `UD-001..049` twice, the acceptance-record and 27/4/18 UD counts, `UD-024`'s deferral and the 55/630/17/1 requirement counts). Recorded as debt `D-2`; none was weakened | 1 |

**Acceptance gate result.** Twenty-two gates **P12A-01…P12A-22**, each with the eight fields the brief requires, close at **15 PASS · 7 PARTIAL · 0 FAIL · 0 BLOCKED · 0 NOT RUN · 0 NOT APPLICABLE**. The seven `PARTIAL` rows are the honest ceiling for an A-phase pass: benchmarking completeness (nine unread primaries), moderation and discipline (two irreconcilable sanction ladders the pass has no authority to settle), reporting and evidence plus auditability (the audit spine does not exist and the prototype table is unprotected), appeals (no operator publishes an overturn rate and `UD-059` is open), requirement closure (candidates only; 20 rows depend on an owner or legal decision), and independent reviewability (project-wide suite debt `D-1` and `D-2`).

**Files changed.** Created: the three deliverables above, [`docs/qa_backups/12A_validate_foundations.py`](../qa_backups/12A_validate_foundations.py) and [`docs/qa_backups/12A_sync_docs.py`](../qa_backups/12A_sync_docs.py) (the one-shot live-status synchroniser, in the shape `11C_sync_docs.py` established — it rewrote 63 current-status claims). Updated: `docs/DECISIONS.md`, `docs/stage-2/04_approved_and_provisional_decisions.md`, `docs/stage-2/05_unresolved_design_decisions.md`, `docs/stage-2/03_requirements_traceability.md` (synchronisation note only), `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md`, this log (the §73 record plus its live-status header), the DD register's decision-count lead-in and the B-12 outline row. Six checkers had a hard-coded register frontier advanced to the value this pass created, with no expectation loosened and no check deleted: `docs/qa_backups/status_rules.py` (`CURRENT_SUBPROMPT` → `12A`, `11C`/`12A` completed, and the sub-prompt pattern extended to the `12` family — before it, `12A` was not a recognised sub-prompt token at all), `09_validate.py`, `test_decision_registers.py`, `test_next_action.py` (row 12 stops being a bare `Pending` row, and the 11C-as-live fixture became a stale-claim case with `12B` as the live case), `10B_validate_warfare.py` and `09B_validate_alliance_semantic.py` (C17 registers to D-177 / DD-225 / UD-060 at 38 Confirmed). `validate_final.py`'s ten pre-Prompt-12 assertions (`D-2`), 11A's check 29 (`D-1`) and the two broken Stage-1 sweep tools (`D-10`) were recorded, not repaired. No gameplay specification, prototype file or approved register row was modified and no file was deleted.

**Git.** No Git operation was performed by this entry: nothing was staged, committed, pushed, branched, reverted, reset or cleaned, and no file was removed.

**Limitations.** This is a documentation pass. No cheat detection, privacy enforcement, RLS behaviour, moderation tooling, authentication, appeal execution, audit-log tamper resistance or playability behaviour was tested, because none is implemented. The validator grades the research record; it cannot prove that a cited page still says what the row records, that a threat band is correct, or that any future control works. Nine sources were unreadable and are labelled as such; nineteen rows carry a disclosed non-URL reference. No number in this pass was measured.

**Verdict.** **PARTIAL — Prompt 12A complete at the research and design-foundations level.** B-12's foundations are established, traceable and internally validated; the specification itself is not written. **Prompt 12B — B-12 rulebook and formula register — is the next sub-prompt; it has not started and is not authorized to start by this entry (D-002).** `UD-052`…`UD-060` and `UD-017`, `UD-040`–`UD-051` remain Open or Deferred and the nine new rows await decisions, and Prompt 14 calibration has not started.


**CodeRabbit review remediation (2026-11-06).** Nine review findings were checked against the current files before any edit. All nine were still valid and were corrected in place; none required a specification or register value to change. (1) The `AI_CONTEXT.md` unresolved-decision index row now covers `UD-001…UD-060` at **28 Resolved / 3 Deferred / 29 Open** and states §6's 32-row non-resolved split, instead of the pre-12A 27/4/18 text. (2) The synchroniser's rule list gained the two residual claim shapes, and `PROJECT_PROGRESS.md`, `ROADMAP.md` and this log's live header now say **12A complete / 12B next**. (3) `demote_and_insert` is idempotent: a surface already carrying a 12A blockquote is returned unchanged, verified by a direct call test. (4) `check_33`'s negation exemption is scoped to the claim's own sentence, and fixture **12A-N16** proves that an earlier unrelated negation cannot excuse a later implementation claim. (5) `check_05` now keeps the full cited set for dangling references and builds a separate usage set after stripping each row's defining identifier; the register gained **§11**, a supporting-only index that states what each of the twenty previously unnamed rows supports and where. (6) `status_rules.py` sets `CURRENT_SUBPROMPT = "12B"` and `10B_validate_warfare.py` asserts the same value. (7) `test_next_action.py` and `test_decision_registers.py` assert 12B as next in progress rows 10 and 11. (8) The Bible outline's B-11 prompt cell and §5 summary record 11C and 12A complete with 12B next. (9) Every function in the two scripts created by this pass now carries a docstring; pre-existing test files were left untouched. Re-run after remediation: `12A_validate_foundations.py` **35/35, exit 0**; `--self-test` **10/10 positive and 19/19 negative, exit 0**; `09_validate.py` **370/370**; `test_next_action test_decision_registers` **39 tests OK**; `09A` **943 checks**; `09B` **34/34**; `10B` **1036 checks, 73/73 negative fixtures**; `11B` and `11C` PASS; all ten `verify_*` scripts exit 0; `validate_links.py` **0 unresolved**. `11A_validate_research.py` still exits 1 on its recorded `D-1` debt and `validate_final.py` still reports the same **10** pre-Prompt-12 failures (`D-2`); neither was weakened. No Git operation was performed.

**Second CodeRabbit review remediation (2026-11-07).** Eight further findings were checked against the current files; all eight were valid and were corrected in place. (1) The "No fair-play rule … exists" sentence in the 12A status blocks is narrowed to "no **new B-12** rule was written by 12A" and now states that **B-03 already specifies the inherited enforcement rules** that B-12 must adopt rather than re-decide; the same correction was applied to `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md` (blockquote and row 12), `ROADMAP.md` and the Stage 2 handoff. (2) `check_19` returns a clear failure for an empty DD register and reports the captured declaration value instead of a tuple repr. (3) `run_fixtures` now adds every unexpected result to the problems collection with its fixture id, check id and expected/actual outcome, while keeping the diagnostic print. (4) `check_03` reads the Type token only from the Type cell (`c[3]`), so a token elsewhere cannot rescue an empty cell. (5) `check_33` now scopes negation to the claim's own sentence *or table cell*, and "only" no longer excuses a claim; fixtures **12A-N17** (staging-only claim) and **12A-N18** (negation in another cell) cover both cases. (6) `_gates` reads only the Result cell (column 6); fixture **12A-N19** leaves an illegal Result while placing a legal token in another cell and now rejects it. (7) `check_23`, `check_24` and `check_25` verify row lengths and matching threat halves before indexing, returning FAIL rather than raising; verified directly with a truncated integration row, a missing risk-control row and a short control row. (8) The roadmap status paragraph and table now record Prompt 12A complete and 12B next throughout, the progress-log Prompt 12 row moves from `19_fair_play_and_player_protection.md` / Pending to the reserved `20_` path with 12A complete, and the `09_validate.py` and `validate_final.py` pending-count expectations were advanced from 4 to 3 because row 12 is no longer Pending. Re-run after this round: `12A_validate_foundations.py` **35/35, exit 0**; `--self-test` **10/10 positive and 19/19 negative, exit 0**; `09_validate.py` **370/370**; `test_next_action test_decision_registers` **39 tests OK**; `09A` **943 checks**; `09B` **34/34**; `10B` **1036 checks, 73/73 negative fixtures**; `11B` and `11C` PASS; all ten `verify_*` scripts exit 0; `validate_links.py` **0 unresolved**; `11A` and `validate_final` retain only their recorded `D-1` and `D-2` failures (10, unchanged). No Git operation was performed. A planning collision remains visible rather than silently renumbered: B-12 reserves `20_fair_play_and_player_protection.md` while Prompt 13's guidance path is still `20_interface_and_player_journeys.md`; resolving that is a planning decision outside this remediation.

**Third CodeRabbit review remediation (2026-11-07).** Nine further findings were checked against the current files; all nine were valid and were corrected in place. (1) `check_24` now requires the full 5.4 layout before reading a residual, so a row truncated before the residual column fails as short instead of having its outstanding-decision cell read as the residual; the short-row report is unchanged. (2) `check_24` now requires explicit `L1`–`L5` and `I1`–`I5` tokens in the assessment cells and a band word with a score on the 1–25 scale, while preserving the register's deliberate label/score overrides; four negative fixtures (`12A-N20`–`12A-N23`) cover a missing likelihood token, a band without a score, a score outside the scale and the truncated residual column. (3) `check_10`'s `12A-N04` fixture now removes only the verification-approach cell, keeping the statement and rationale intact, so the check fails for the intended reason. (4) `run_fixtures` now compares each negative fixture's failure detail with a declared expected reason, so a check that rejects for an unrelated cause is reported as a wrong-reason failure; `12A-N19` declares `illegal status`, isolating its gate-Result detection. (5) Progress-log row 10 now records Prompt 11 complete and Prompt 12B next; row 11 records 11C complete, keeps the pending owner acceptance of its PARTIAL verdict, and states that 12B authorization is pending. (6) `AI_CONTEXT.md`'s official stage plan now marks 10C complete, 11 complete, 12A complete and 12B next, retaining the separate authorization requirement. (7) `validate_final.py`'s pre-Prompt-12 frontiers were advanced to the current registers — `REQ-001..763`, `DD-001..225`, `UD-001..060`, the **28 Resolved / 3 Deferred / 29 Open** reconciliation, `UD-024` Resolved, the §6 inventory, `stage_2_next_prompt` `12` and the 55/688/19/1/0 requirement counts — with the row-10 assertion naming 12B and a new row-12 assertion; debt `D-2` is closed and no check was weakened or deleted. (8) The research report's fixture inventory now lists `12A-N16`–`12A-N23`, states 23 negative and 33 total fixtures, and keeps the ten clean fixtures accounted for. (9) `09_validate.py` and `validate_final.py` gained a row-level `log_status("12")` check for 12A complete / 12B next, with the pending-count check unchanged. Regression: the 12A validator passes 35/35 with 10/10 positive and 23/23 negative fixtures; `--self-test` passes; `09_validate.py` 371/371; the 39 unit tests OK; `09A` 943 checks; `09B` 34/34; `10B` 1,036 checks and 73/73 fixtures; `11B` and `11C` PASS; all ten `verify_*` scripts exit 0; the link gate reports 0 unresolved; `validate_final.py` now passes; and `11A_validate_research.py` still exits 1 on its pre-existing `REQ-703` assertion (`D-1`), unchanged by this remediation.

**Fourth CodeRabbit review remediation (2026-11-07).** Five findings were checked against the current files; all five were valid and were corrected in place. (1) The three machine-readable STATUS blocks in `AI_CONTEXT.md`, `AI_HANDOFF.md` and `PROJECT_PROGRESS.md` now record `stage_2_next_prompt: 12B` rather than the bare `12`, so the declared value names the live sub-prompt instead of only its parent. (2) Every reader of that value was advanced with it: `09_validate.py`, `validate_final.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py` (C18) and the 12A continuity check now accept `12B`; `12A_validate_foundations.py` already parsed the numeric prefix and continues to pass. (3) `test_next_action.py` expects `12B` in the real STATUS set and passes the three declarations through a new `continuity_problems()` helper that combines the stale-next-action and completed-sub-prompt detectors; `test_decision_registers.py` expects `12B` as well. (4) The Stage 2 handoff's closing 10C sentence no longer says "Prompt 11 has not started"; the Stage 2-not-complete, no-implementation, no-runtime-test and warfare-calibration status is unchanged. (5) The progress log's current-status header now records 11C and 12A complete and **Prompt 12B next and not started**, replacing the stale "11C is next" clause while leaving the surrounding status text intact. Regression: the 12A validator passes 35/35 with 10/10 positive and 23/23 negative fixtures; `09_validate.py` 371/371; the 39 unit tests OK; `09A` 943 checks; `09B` 34/34; `10B` 1,036 checks and 73/73 fixtures; `11B` and `11C` PASS; all ten `verify_*` scripts exit 0; the link gate reports 0 unresolved; `validate_final.py` passes; and `11A_validate_research.py` still exits 1 on its pre-existing `D-1` assertion, unchanged by this remediation. The affected legacy fixture tests were also checked: `test_09A_alliance_validator.py` passes all 43 tests, and the 09B C18 fixture (`test_59_next_prompt_changed_fails`) passes; the full 267-test 09B fixture suite was not run to completion because it re-executes the whole validator per test.

---

## 74. Prompt 12A-C1 — documentary reconciliation of counts, evidence access, source taxonomy and decision references (2026-11-07)

**Scope.** A targeted corrective pass on Prompt 12A after an independent count audit. It rewrites no 12A deliverable from scratch, changes no approved mechanic, resolves no owner-reserved or legal decision, allocates no global `REQ-`, writes no B-12 rule, penalty, duration or permission, creates no Prompt 12B or 12C deliverable, and implements no security control. Documentation, validator and fixture work only.

**Corrections applied, each verified against the current rows.**

1. **Benchmark and comparator counts.** The canonical set is **40 `12A-BM` benchmark mechanisms** and **18 `12A-CMP` comparator profiles**. Report §5 now states `12A-BM-001`…`12A-BM-040` and `12A-CMP-01`…`12A-CMP-18`; earlier prose that said 32 and 12 is gone. The register's §10 totals table declares the same 40 and 18.
2. **Confidence and access are separated and recomputed from the rows.** Across **153** registered evidence rows the leading-token confidence is `High` **65**, `Medium` **71**, `Low` **14**, `Unverified` **3**. Access is a different measurement: **140** rows read in full, **9** read partially or through extracts, **3** inaccessible or unreadable and **1** internal research finding, totalling 153. Nine rows are substantive retrieval failures, four carry a snippet-only flag and one is an absence finding; **13** rows were not read in full. The old “six rows” and “45 of 120 read rows” figures are removed; no requirement rests on a retrieval-failed row alone.
3. **Source taxonomy.** `12A-RS-152` keeps its identifier and its absence conclusion but is now typed `RESEARCH FINDING (absence of evidence)`, classed internally as both `INTERNAL RESEARCH FINDING` and `ABSENCE-OF-EVIDENCE FINDING`, and explicitly denied an external URL or external-publication status. The type vocabulary now includes `RESEARCH FINDING` and drops the unused `RETRIEVAL-FAILED` token.
4. **AGCM source registered as `12A-RS-153`, preserving `12A-RS-152`.** The row records the official AGCM press release of **8 October 2026** (retrieved **2026-11-07**), AGCM's lead role with the Norwegian and Danish consumer authorities, the action against Activision Blizzard UK and other Microsoft group companies, the “widespread infringement” question under Article 3(3) of Regulation (EU) 2017/2394, and the topics — virtual currencies, multiple currencies and bundles, dark patterns, parental controls and assistance when accounts are blocked. Its limitation states that this is an **ongoing coordinated action with no infringement finding and no outcome**, that relevance is conditional on product, monetisation model, population and jurisdiction, and that it creates **no automatic legal obligation**. Owner and legal-counsel authority remains `UD-017`.
5. **Decision references corrected.** `D-176` / `DD-224` are the **accepted critical residual**; `D-177` / `DD-225` are the **prevention-heavy posture**. Gate `P12A-05` and the §33 boundary paragraph now cite `D-176` / `DD-224` for the residual and `D-177` / `DD-225` only for the posture. The earlier `D-165` network-evidence reference was also corrected to `D-168` / `DD-216`. Multi-account wording now uses the canonical sentence “Identity-layer multi-accounting cannot be reliably detected under the current fixed constraints”; absolute words such as “undetectable” are removed, and §8.4, §21 and the gate row distinguish **proving common identity** from using behavioural, transactional and outcome evidence against coordinated abuse.
6. **Validator hardened without weakening any check.** `12A_validate_foundations.py` gains checks `12A-36`–`12A-45` for cross-document benchmark and comparator counts, confidence, access completeness, taxonomy, `RS-152` classification, `RS-153` registration and citation, `D-176`/`DD-224` references, absolute-wording prohibition and §1.5 access-date consistency. `check_08` now requires all nine retrieval-failure rows to carry a disclosure instead of counting any row that merely mentions “blocked”. Ten new negative fixtures `12A-N24`–`12A-N33` each corrupt one of those properties and declare the expected failure reason; `run_fixtures` rejects a fixture that fails for an unrelated cause. All prior checks and fixtures are retained.
7. **The 22 gates were reassessed, not upgraded.** The tally stays **15 PASS / 7 PARTIAL / 0 FAIL / 0 BLOCKED / 0 NOT RUN / 0 NOT APPLICABLE**. `P12A-03` remains PARTIAL because nine rows are substantive retrieval failures, no operator publishes an overturn rate and the AGCM action has no outcome; `P12A-08` remains PARTIAL on the unresolved sanction-ladder conflict; `P12A-09`, `P12A-10`, `P12A-12`, `P12A-16` and `P12A-22` remain PARTIAL with their owner, legal or implementation evidence still absent. No gate was raised because a validator passes.
8. **Project documentation synchronized.** `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `ROADMAP.md`, `00_stage_2_handoff.md`, `01_stage_2_prompt_roadmap.md`, `02_master_game_design_bible_outline.md`, the three 12A deliverables, `12A_sync_docs.py` and the 09B validator's status line now record **153** rows, **44/44** checks, **10/10** positive and **32/32** negative fixtures, and the 12A-C1 reconciliation. Prompt 12B remains the next prompt, has not started, and needs separate owner authorization once this reconciled foundation is accepted.

**Outstanding obligations, deliberately not fixed here.** The feasibility prototype still grants `authenticated` a table-wide `UPDATE` on `feasibility.profiles` including `treasury`, with only a row-scoped policy. The designed column-level correction exists only in abandoned bytecode: there is no `0005` migration, no `tests/sql/` directory and no SQL permission test on disk. The prototype's `audit` table has no protective trigger and no delete revocation outside the player role; no tamper-evident implementation and no executed verification job exists. These are Stage 5 build obligations tracked by `12A-RK-007` and `12A-RK-026`; they are not claimed as fixed.

**Validation actually run after the corrections (2026-11-07).** `12A_validate_foundations.py`: **CHECKS 45/45 passed**, inventory `sources=153 benchmark=40 comparators=18`, exit **0**. `--self-test`: **10/10 positive**, **33/33 negative rejected for the expected reason**, exit **0**. `09_validate.py`: **371/371**, exit **0**. `validate_final.py`: **ALL CHECKS PASSED**, exit **0**. `validate_links.py`: **Unresolved: 0** (3,535 links found, 3,153 checked locally, 382 external skipped, 29 anchors checked), exit **0**. Unit tests: **39 tests OK**, exit **0**. `09A`: **943 checks**, exit **0**. `09B`: **34/34**, exit **0**. `10B`: **1,036 checks and 73/73 fixtures**, exit **0**. `11B` and `11C`: PASS, exit **0** each. All ten `verify_*` scripts: exit **0**. `11A_validate_research.py`: exit **1** on its pre-existing `D-1` assertion, which expects a maximum of **REQ-703** and observes a maximum textual reference of **REQ-764**; that reference is reserved for Prompt 12B and is not allocated, so the canonical requirement frontier remains **REQ-763**. This pass did not alter or weaken the legacy check. The modified Python files compile. The 12A-C1-M1 micro-correction added `check_45` and fixture `12A-N33` for §1.5 access-date consistency and re-ran the suites with the results above.

**Verdict.** **Documentary reconciliation complete; Prompt 12A remains complete at the research and design-foundations level.** This entry is not an acceptance, not an independent review and not evidence of implementation readiness; no runtime control, database permission, moderation workflow, appeal or audit verification was tested, because none is implemented. **Prompt 12B is still the next roadmap prompt, has not started, and requires separate owner authorization after the reconciled foundation is accepted.**

## 75. Prompt 12B — B-12 fair play, privacy, moderation and administration: complete system specifications (2026-11-07)

**Scope.** Prompt 12B converts the reconciled 12A research foundation into authoritative B-12 specifications. It writes rules, requirement records, formulas and acceptance gates; it writes no migration, grant, RLS policy, audit trigger, application code, screen, workflow or gameplay change. It resolves no owner-reserved or legal decision and does not authorize Prompt 12C.

**Deliverables created (four documents plus one validator).**

| Artefact | Content |
|---|---|
| [B-12 rulebook](../stage-2/20_fair_play_and_player_protection.md) | 344 normative rules across `FP` 35, `EVD` 42, `MA` 12, `CO` 10, `EX` 12, `PRV` 25, `MOD` 60, `ADM` 30, `COR` 18, `SEC` 40, `INT` 20, `FR` 15 and `GOV` 25; 16 violation classes `V-01`…`V-16` with 11 elements each; 9 privacy classes, 8 actor classes and 6 actions; 8 administrative roles with 11 fields; 15 failure postures; 20 cross-system contracts; Annex E rule inventory |
| [B-12 formula and parameter register](../stage-2/20_fair_play_and_player_protection_formula_register.md) | 16 formulas `F-FP-001`…`F-FP-016`, 20 mandatory fields each; six value classes; 12 parameters `FP-P01`…`FP-P12`, none calibrated; four non-claims |
| [B-12 requirement register](../stage-2/20_fair_play_and_player_protection_requirements.md) | `REQ-764`…`REQ-869` allocated one-to-one from `12A-CR-001`…`12A-CR-106`; 86 Provisional / 20 Open / 0 Approved / 0 Deferred; 106 rows in two halves covering all required fields |
| [B-12 acceptance framework](../stage-2/20_fair_play_and_player_protection_acceptance.md) | 26 gates at 23 PASS / 3 PARTIAL / 0 FAIL / 0 BLOCKED / 0 NOT RUN / 0 NOT APPLICABLE; ten-area coverage; requirement, cross-system and formula coverage; later-stage evidence; 12C handoff; validator specification |
| [`12B_validate_b12.py`](../qa_backups/12B_validate_b12.py) | 62 document checks plus 12 positive and 22 negative fixtures; parses the four documents and the decisions, DD, UD, ledger and continuity registers |

**Decisions and statuses.** Ten Category B decisions **D-178…D-187** are recorded and mirrored as **DD-226…DD-235**: one rule family; the sixteen-class taxonomy; the evidence-sufficiency matrix; the six-tier ladder; the eight-role catalogue; the privacy matrix; six correction transaction types with confirmed-only repetition; the one-appeal architecture; the `REQ-764`–`REQ-869` allocation; and the security boundary with Supabase/audit obligations and the known prototype defects. DD tallies become **130 Approved / 51 Provisional / 48 Confirmed / 2 Binding inherited / 2 Candidate / 1 Superseded / 1 Deferred = 235**; project decisions become **187**. Requirement counts become **55 Approved / 774 Provisional / 39 Open / 1 Deferred / 0 Proposed = 869**. `UD-017`, `UD-052`…`UD-060` and `UD-040`–`UD-051` remain Open; no owner or legal decision was closed.

**Security and implementation boundary, stated not fixed.** The prototype still grants `authenticated` a table-wide `UPDATE` on `feasibility.profiles` including `treasury`; there is no `0005` profile-permission migration, no `tests/sql/` directory, no protective `audit` trigger and no executed verification job. B-12 specifies the obligations and discloses the defects; it does not correct them, and no document claims the grant is fixed, that tamper-evident protection exists, or that any control is running.

### 75.1 Change manifest

| File | Change |
|---|---|
| `docs/stage-2/20_fair_play_and_player_protection.md` | **Created** — B-12 rulebook v1.0 |
| `docs/stage-2/20_fair_play_and_player_protection_formula_register.md` | **Created** — 16 formulas and 12 parameters |
| `docs/stage-2/20_fair_play_and_player_protection_requirements.md` | **Created** — 106 requirement records |
| `docs/stage-2/20_fair_play_and_player_protection_acceptance.md` | **Created** — 26-gate acceptance framework |
| `docs/qa_backups/12B_validate_b12.py` | **Created** — 62 checks, 34 fixtures |
| `docs/DECISIONS.md` | Added D-178…D-187; updated the last-updated header |
| `docs/stage-2/04_approved_and_provisional_decisions.md` | Added DD-226…DD-235; tallies 235; version 3.19 |
| `docs/stage-2/03_requirements_traceability.md` | Added `REQ-764`–`REQ-869` (106 rows); counts 869; version 1.37 |
| `docs/stage-2/05_unresolved_design_decisions.md` | Frontier note only; every row stays Open; version 1.31 |
| `docs/stage-2/02_master_game_design_bible_outline.md` | B-12 row now cites the four documents and the B-12 status |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row and split record updated; 12C next |
| `docs/stage-2/00_stage_2_handoff.md` | 12B status block added; 12C next and not authorized |
| `docs/stage-2/06_stage_2_progress_log.md` | This §75 and the top status table |
| `docs/AI_CONTEXT.md` | 12B status, four inventory rows, frontiers and counts |
| `docs/AI_HANDOFF.md` | 12B status, decision list, 187 entries |
| `docs/PROJECT_PROGRESS.md` | 12B status block and Prompt 12 row |
| `docs/ROADMAP.md` | 12B status block, stage-2 row and last-updated record |
| `docs/qa_backups/09_validate.py` | Frontier refresh to REQ-869 / DD-235 / 187 decisions / next 12C; counts 774/39 |
| `docs/qa_backups/validate_final.py` | Same frontier refresh; counts 774/39 |
| `docs/qa_backups/test_next_action.py` | Live sub-prompt 12C; row 10/11/12 expectations |
| `docs/qa_backups/test_decision_registers.py` | `stage_2_next_prompt: 12C`; row expectations |
| `docs/qa_backups/status_rules.py` | `12B` added to completed sub-prompts |
| `docs/qa_backups/09A_validate_alliance.py` | Requirement rows 869; statuses 774/39; prompt regex 12C |
| `docs/qa_backups/09B_validate_alliance_semantic.py` | Frontiers 869 / D-187 / DD-235; tallies 48/235; C25 scoped to Alliance rows |
| `docs/qa_backups/12A_validate_foundations.py` | Frontier checks accept the later D-187 / DD-235 / REQ-869 state without weakening the 12A content checks |

### 75.2 Validation actually run

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 62/62 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `12/12` positive and `22/22` negative fixtures accepted or rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py` | `45/45` checks after the frontier refresh; `10/10` positive and `33/33` negative fixtures | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed — ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | `PASS`; 73/73 negative fixtures; CF-01/CF-02 clean | 0 |
| `python docs/qa_backups/11B_validate_b11.py` | `RESULT: PASS` | 0 |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS` | 0 |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` (3,388 local links, 382 external skipped, 29 anchors) | 0 |
| `verify_city/economy/market(+workflows)/politics/diplomacy(+workflows)/warfare/alliance(+workflows)` scripts | all pass: politics `879/879`, warfare workflows `49/49`, diplomacy `17 groups`, market `07C VALIDATION: ALL CHECKS PASSED`, others `ALL CHECKS PASSED` | 0 each |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 still expects the pre-12A `REQ-703` frontier; pre-existing debt `D-1`, not fixed or hidden here | 1 |

Every `PASS` above is documentary. No runtime control, database permission, moderation workflow, appeal, audit protection or legal obligation was tested, because none is implemented.

**Outstanding obligations, deliberately not fixed here.** The prototype privilege and audit defects named above; every Open requirement and UD; Prompt 12C itself, which is not started and not authorized; and legacy validator debt `D-1` (11A check 29) and `D-10` (the broken Stage-1 sweep tools). None is B-12 evidence and none is disguised as fixed.

**Verdict.** **Prompt 12B is complete at the specification/documentation level only.** It supplies ten-area rules, formulas, requirements, decisions and acceptance gates; it does not implement, verify, deploy or release a control, does not resolve an owner or legal decision, and does not authorize Prompt 12C. **Specified ≠ implemented ≠ independently verified ≠ operating ≠ compliant.**

## 76. Prompt 12B-C1 — formula corrections, integration traceability, prompt archival and closeout (2026-11-07)

**Scope.** A targeted corrective pass on the completed Prompt 12B package. It corrects identified formula, parameter and integration-mapping defects, archives the original Prompt 12B instruction, records a policy-reading attestation, extends the validator and synchronizes the affected documents. It rewrites no completed specification unnecessarily, allocates no new requirement, closes no owner-reserved or legal decision, and implements no migration, grant, RLS policy, audit trigger or gameplay change. Prompt 12C remains not started and not authorized.

**Autonomous decision policy reading attestation.** Canonical path: `docs/AUTONOMOUS_DECISION_POLICY.md` (absolute `C:\Users\suren\Downloads\Project X\docs\AUTONOMOUS_DECISION_POLICY.md`). The complete document (**version 1.0**, created 2026-10-23, D-014; **121 lines**) was read on **2026-11-07 at 14:46 IST** during Prompt 12B-C1. **Line-count method (reproducible):** `wc -l docs/AUTONOMOUS_DECISION_POLICY.md` = 121, independently confirmed by Python `len(text.splitlines())` = 121; the file is CRLF-terminated and ends with a trailing newline, so a reader that renders a phantom final empty line may display 122 — the authoritative count is 121. The 12B-C1 attestation originally stated 122; **12B-C1-R1 corrected it to 121** after re-reading the complete file on **2026-11-07 at 18:51 IST** and verifying the policy is unchanged (version 1.0; SHA-256 `697dd52d895ff897c498c1acb987535178da42e96bb3458297e762addb8ad479`). Confirmation: the full document was read; D-014 was followed throughout this pass; no Category A fixed constraint was changed; no owner-reserved or legal decision was closed; and the policy file itself was not modified. **Historical distinction:** the policy was also read during the earlier Prompt 12B session before specification work, but no timestamped attestation was recorded then, so that historical reading is asserted from the session record and is not independently timestamped. This attestation records the verifiable C1 reading and the R1 re-verification only and does not backdate compliance. If the policy is legitimately edited later, this version-specific attestation must be superseded by a new reading record rather than silently re-counted.

**Corrections applied.**

1. **F-FP-002 direction.** The 1.0 expression `min(max(V_law − V_obs, 0), B_i)` contradicted its own worked example (`V_law=100`, `V_obs=140`, `B_i=40` → claimed 40, actual 0). The intended semantics is removal of the observed excess, so the expression is corrected to `C = min(max(V_obs − V_law, 0), B_i)`, the boundary statement to `V_obs ≤ V_law → C = 0`, and five boundary examples added. A shortfall is a loss handled by `F-FP-015`, not by this removal formula.
2. **F-FP-014 sign convention.** The ambiguous `O + L − C − R + P − X = Z` is replaced by the explicit signed-delta identity `Z = O + L + C + R + P + X + A`, where every term is the sum of signed ledger deltas of its `COR-001` type and `A` is `ADMIN_ADJUSTMENT`. Reversal, partial-reversal, duplicate-reversal, missing-original and failed-transaction behaviour is specified, with eight worked examples. `COR-003` is aligned to the same convention.
3. **Repeat-violation double count.** `F-FP-001` no longer contains a repetition term; `F-FP-011` is documented as the sole bounded repetition adjustment. Examples recomputed (`SEV=5`; with one prior `SEV_R=6`). `MOD-039` states repetition is applied once and never increases economic correction.
4. **Parameter completeness.** `w` (`F-FP-008`) and `f` (`F-FP-009`) are independently configurable and were unregistered; they are added as `FP-P13` and `FP-P14`, both Provisional, none approved. A formula-to-parameter mapping (§3.1) covers all 16 formulas and separates configurable parameters from derived inputs and structural constants. Parameter count is now 14.
5. **Integration mapping.** The acceptance §5 table mis-assigned several B-systems. It is corrected to the canonical rulebook §16 associations (B-03→`INT-001`, B-04→`INT-003`, B-05→`INT-004`, B-06→`INT-005`, B-07→`INT-006`, B-08→`INT-007`, B-09→`INT-008`, B-10→`INT-009`, B-11 events→`INT-010`, B-11 rankings→`INT-011`, B-02 turn→`INT-013`, B-02 spine→`INT-014`). The ten-area matrix contract references are corrected to match.
6. **Seven-field dependency traceability.** Rulebook §16.1 now states all seven Prompt 12B §13 fields for each of the 20 contracts; acceptance §5.2 adds the consolidated requirement/decision/status linkage. No new contract or B-system identifier was invented.
7. **Prompt archival.** The complete original Prompt 12B instruction (36,010 bytes) is archived verbatim at `docs/prompts/prompt_12B_complete_system_specifications.md`, indexed in `docs/prompts/INDEX.md` with its SHA-256, and referenced from the Stage 2 prompt roadmap. No duplicate prompt file was created.
8. **Acceptance reassessment.** Acceptance §2.1 records the evidence-based reassessment. The tally remains 23 PASS / 3 PARTIAL; `P12B-14`, `P12B-16` and `P12B-23` stay PARTIAL because their missing evidence is implementation or external ruling.

### 76.1 Change manifest (12B-C1)

| File | Change |
|---|---|
| `docs/stage-2/20_fair_play_and_player_protection_formula_register.md` | F-FP-001/002/008/009/011/014 corrected; FP-P13/P14 added; §3.1 mapping; counts updated |
| `docs/stage-2/20_fair_play_and_player_protection.md` | COR-003 signed convention; MOD-039 repetition-once; §16.1 seven-field table |
| `docs/stage-2/20_fair_play_and_player_protection_acceptance.md` | §2.1 reassessment; §3 contract refs; §5 canonical mapping and traceability; §6 counts |
| `docs/prompts/prompt_12B_complete_system_specifications.md` | **Created** — verbatim original instruction |
| `docs/prompts/INDEX.md` | **Created** — prompt archive index |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Archive reference added |
| `docs/qa_backups/12B_validate_b12.py` | Checks 63–75 and fixtures P13–P25 / N23–N30 added; gate parsing scoped; parameter count 14 |
| `docs/stage-2/06_stage_2_progress_log.md` | This §76 |

**Manifest completeness correction (12B-C1-R1).** The original §76.1 table above omitted five continuity files that Prompt 12B-C1 actually modified (each received a 12B-C1 status block and updated parameter/validator counts). They are recorded here rather than by rewriting the historical table: `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, and `docs/stage-2/00_stage_2_handoff.md`. The R1 follow-up corrections themselves are manifested in §77.1.

### 76.2 Validation actually run (2026-11-07)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 75/75 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `25/25` positive, `30/30` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45` checks; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed — ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | `PASS`; 73/73 negative fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` | `RESULT: PASS` | 0 |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS` | 0 |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` (3,397 local, 382 external, 29 anchors; 84 files) | 0 |
| ten `verify_*` number/workflow scripts | all `ALL CHECKS PASSED` / group PASS (politics 879/879, warfare 49/49) | 0 each |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, not altered | 1 |

Every `PASS` is documentary. No runtime control, database permission, moderation workflow, appeal, audit protection or legal obligation was tested. The legacy 11A failure is preserved transparently and was not manipulated.

**Outstanding obligations, unchanged.** The prototype `profiles` table-wide `UPDATE` including `treasury`, the missing `0005` migration, absent SQL permission tests, the unprotected `audit` table and the absent verification job remain unfixed and disclosed. `UD-017`, `UD-052`–`UD-060` and `UD-040`–`UD-051` remain Open. Legacy `D-1` (11A check 29) and `D-10` remain. Prompt 12C is not authorized.

**Verdict.** **Prompt 12B-C1 corrective documentation work is complete at the specification level.** The identified mathematical and mapping defects are corrected and statically verified; no runtime control, security permission or legal obligation was implemented or tested. **Specified ≠ implemented ≠ independent audit ≠ operating.**

## 77. Prompt 12B-C1-R1 — final documentation synchronization and validator closure (2026-11-07)

**Scope.** A targeted closeout correction on Prompt 12B-C1. It synchronizes the remaining stale 12-parameter current-state references to the canonical 14-parameter register, corrects the policy-reading attestation's line count, completes the C1 change manifest, strengthens the 12B validator with cross-document and historical-protection checks, and archives the corrective prompts. It changes no approved formula, integration ID, requirement ID, decision or acceptance meaning; implements nothing; and does not authorize Prompt 12C.

**Corrections applied.**

1. **Acceptance parameter counts.** Gate `P12B-19` now cites `FP-P01`–`FP-P14`; §9.1 reports 14 parameters; the §11 acceptance statement reports 14 uncalibrated parameters. The gate's meaning and PASS status are unchanged.
2. **AI_CONTEXT.** The B-12 formula-register inventory entry now reports 14 parameters `FP-P01`…`FP-P14`, naming `FP-P13` (report-cluster window) and `FP-P14` (action-class rate factor).
3. **Attestation line count.** The §76 attestation's "122 lines" was incorrect. The live policy file is **121 lines** by `wc -l` and by Python `len(text.splitlines())` (CRLF, trailing newline; a renderer may show a phantom 122nd line). The attestation now states 121 with the reproducible method, the version (1.0) and SHA-256, and records the R1 complete re-read on **2026-11-07 at 18:51 IST**. The original C1 reading date (14:46 IST) is preserved; nothing is backdated. The policy file itself was not modified.
4. **C1 manifest completeness.** A correction note under §76.1 records the five continuity files C1 actually changed but omitted (`AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `ROADMAP.md`, `00_stage_2_handoff.md`), without rewriting the historical table.
5. **Validator.** Checks `12B-76`–`12B-81` added: canonical parameter set (E1), acceptance current-state synchronization (E2), AI_CONTEXT synchronization (E3), reproducible attestation line-count comparison (E4), manifest inclusion of `AI_CONTEXT.md` (E4), and historical §75 12-parameter record protection (E5). The stale-reference scan skips lines marked historical/reassessment; check `12B-81` positively requires the historical record to survive. Fixtures `12B-P26`–`12B-P31` and `12B-N31`–`12B-N38` added. No existing check or fixture was weakened.
6. **Archival.** The operative Prompt 12B-C1 instruction and this Prompt 12B-C1-R1 instruction are archived verbatim under `docs/prompts/` and indexed with byte counts and SHA-256. The original Prompt 12B archive is unchanged.

### 77.1 Change manifest (12B-C1-R1)

| File | Change |
|---|---|
| `docs/stage-2/20_fair_play_and_player_protection_acceptance.md` | P12B-19 range, §9.1 count, §11 statement synchronized to 14 parameters |
| `docs/AI_CONTEXT.md` | B-12 formula-register entry synchronized to 14 parameters / FP-P01…FP-P14 |
| `docs/stage-2/06_stage_2_progress_log.md` | §76 attestation line count corrected; §76.1 completeness note; this §77 |
| `docs/qa_backups/12B_validate_b12.py` | Checks 76–81; fixtures P26–P31 / N31–N38; historical-record protection |
| `docs/prompts/INDEX.md` | C1 and R1 archive rows added |
| `docs/prompts/prompt_12B-C1_formula_corrections_and_closeout.md` | **Created** — verbatim operative C1 instruction |
| `docs/prompts/prompt_12B-C1-R1_final_documentation_synchronization.md` | **Created** — verbatim R1 instruction |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row cites §77 |

### 77.2 Validation actually run (2026-11-07)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 81/81 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `31/31` positive, `38/38` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45`; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34 PASS` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | PASS; 73/73 fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` / `11C_validate_b11_workflows.py` | PASS | 0 |
| ten `verify_*` scripts | all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, preserved | 1 |

`validate_final.py` is re-run after this entry and the roadmap citation are added; its result is recorded in the final delivery report. Every PASS is documentary; no runtime, database, security or production verification is claimed.

**Outstanding obligations, unchanged.** Prototype `profiles` privilege and audit defects; `UD-017`, `UD-052`–`UD-060`, `UD-040`–`UD-051`; the 20 Open requirements; legacy `D-1`/`D-10`; Prompt 12C not authorized. Acceptance remains 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`).

**Verdict.** **Prompt 12B-C1-R1 is complete at the documentation/validator level.** Current-state parameter references are synchronized, the attestation is accurate and reproducible, the manifest is complete, and the validator detects the identified stale-reference defects while protecting historical records. No Prompt 12C work, production implementation, database security change or Git operation was performed.

## 78. Prompt 12B-C1-R2 — validator completeness, adversarial mutation tests and final closeout (2026-11-07)

**Scope.** A targeted validator-maintenance and documentation-closeout pass. It strengthens three checks that could pass on incomplete information, adds adversarial negative fixtures reproducing the audited bypasses, archives the R2 instruction, and synchronizes status. It rewrites no B-12 specification, changes no approved identifier, decision or acceptance meaning, implements nothing, and does not authorize Prompt 12C. The complete `AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0) was read in full during this task; D-014 followed.

### 78.1 The three reproduced defects and their closure

| Defect | Old check | Bypass mutation | Why the old check passed | Corrective implementation | New negative fixture | Demonstrated outcome |
|---|---|---|---|---|---|---|
| Acceptance gate incomplete range | `12B-77` | Gate range replaced with `FP-P01, FP-P02, FP-P14` | Old check only tested for `FP-P14` presence and a `FP-P12` endpoint, not the full set | `extract_param_ids` expands ranges/lists; `param_set_problems` compares against the canonical 14-ID set and names missing IDs | `12B-N39` (also `N40` missing FP-P13, `N41` missing FP-P14, `N42` missing FP-P07) | Rejected: `P12B-19 missing parameters: FP-P03 … FP-P13` |
| AI_CONTEXT incomplete range | `12B-78` | FP-P13 removed while the 14-count and FP-P14 retained | Old check only tested `14 parameters` + `FP-P14` strings | Same canonical extraction applied to the B-12 inventory row only; missing/unexpected IDs reported | `12B-N43` (also `N44` range ends FP-P12, `N45` missing FP-P07) | Rejected: `AI_CONTEXT B-12 entry missing parameters: FP-P13` |
| R1 manifest satisfied elsewhere | `12B-80` | `docs/AI_CONTEXT.md` removed from §77.1 but kept in §76.1 | Old check searched the whole log after §76.1, so a §76.1 entry satisfied it | Check scoped strictly to `### 77.1`…`### 77.2`; requires all eight R1-changed files as rows; empty/malformed manifest rejected | `12B-N37` and `12B-N46` (also `N47` emptied manifest) | Rejected: `R1 §77.1 manifest missing: docs/AI_CONTEXT.md (a §76.1 entry cannot satisfy §77.1)` |

**Canonical extraction (correction D).** One helper, `extract_param_ids`, parses compact range notation (`FP-Paa`–`FP-Pbb` / `…`) into the full consecutive sequence and collects explicit IDs; reversed ranges are reported, not normalized. `param_set_problems` compares the result with `EXPECTED_PARAM_SET` (the 14 canonical IDs) and emits actionable missing/unexpected diagnostics. Checks `12B-77` and `12B-78` reuse it; no partial hard-coded list is duplicated.

**Diagnostics and historical protection (corrections E/F).** Historical/reassessment lines are excluded from the current-state stale scan; `12B-81` positively requires the historical §75 12-parameter record to survive, and the new `12B-82` positively requires the C1 §76.1 manifest-completeness note to survive. Mutations run on in-memory copies (`copy.deepcopy`); live files are never corrupted by a fixture.

### 78.2 Change manifest (12B-C1-R2)

| File | Change |
|---|---|
| `docs/qa_backups/12B_validate_b12.py` | Canonical extraction helpers; checks 77/78/80 strengthened; check 82 added; fixtures P32 / N39–N48 added; existing fixture expectations updated to new diagnostics |
| `docs/prompts/prompt_12B-C1-R2_validator_completeness.md` | **Created** — verbatim R2 instruction |
| `docs/prompts/INDEX.md` | R2 archive row added |
| `docs/stage-2/06_stage_2_progress_log.md` | This §78 |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row cites §78; validator counts 82/32/48 |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` | R2 status block added; live validator counts updated |

### 78.3 Validation actually run (2026-11-07)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 82/82 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `32/32` positive, `48/48` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45`; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34 PASS` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | PASS; 73/73 fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` / `11C_validate_b11_workflows.py` | PASS | 0 |
| ten `verify_*` scripts | all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, preserved | 1 |

`validate_final.py` is re-run after this entry and the roadmap citation are added; its result is recorded in the final delivery report. No tests were skipped. Every PASS is documentary; no runtime, database, security or production verification is claimed.

**Acceptance and governance, unchanged.** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`); `REQ-764`–`REQ-869`, `D-178`–`D-187`, `DD-226`–`DD-235`, 16 formulas, 14 parameters, 20 INT contracts preserved; `UD-017`, `UD-052`–`UD-060`, `UD-040`–`UD-051` remain Open; Prompt 12C not authorized.

**Verdict.** **Prompt 12B-C1-R2 is COMPLETE at the validator/documentation level.** The three audited bypasses are demonstrably rejected by explicit negative fixtures, the full canonical parameter set is enforced in both the acceptance gate and AI_CONTEXT, and the R1 manifest is validated in its own section. C1/R1/R2 closeout is complete to the extent demonstrated by these tests; production implementation and owner/legal rulings remain outstanding.

## 79. Prompt 12B-C1-R3 — duplicate-ID detection, stale-reference validation and final validator closure (2026-11-07)

**Scope.** A targeted validator-maintenance and documentation-closeout pass closing the four additional bypasses found by independent mutation testing of R2. It rewrites no B-12 specification, changes no approved identifier, decision or acceptance meaning, implements nothing, and does not authorize Prompt 12C. The complete `AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0) was read in full during this task; D-014 followed.

### 79.1 The four reproduced bypasses and their closure

| Bypass | Check | Mutation | Why R2 passed | Correction | New fixture | Demonstrated outcome |
|---|---|---|---|---|---|---|
| Duplicate ID in acceptance gate | `12B-77` | added a second `FP-P01` to the complete P12B-19 range | R2 extracted identifiers into a set, erasing duplicate evidence | `extract_param_occurrences` preserves ordered occurrences; `compare_param_occurrences` reports duplicate frequency before any set comparison | `12B-N49` (also `N50` duplicate FP-P07, `N51` unexpected FP-P15) | Rejected: `P12B-19 contains duplicate parameter FP-P01 (×2)` |
| Duplicate ID in AI_CONTEXT | `12B-78` | repeated `FP-P01` in the B-12 entry | set conversion erased the duplicate | same occurrence-preserving comparison on the entry | `12B-N52` (also `N53` duplicate FP-P07, `N54` unexpected FP-P15) | Rejected: `AI_CONTEXT B-12 entry #1 contains duplicate parameter FP-P01 (×2)` |
| Stale range elsewhere in acceptance | `12B-77` | kept correct gate/§9 but inserted `Current formula-register range: FP-P01–FP-P12` elsewhere | R2 stale scan only matched the literal "12 parameters" text, not a stale range | `acceptance_stale_problems` scans every current-state range/enumeration in the document (excluding the dated §2.1 reassessment and genuinely historical lines) and compares each with the canonical set | `12B-N57` (also `N58` stale 12-count, `N59` fake-historical current claim) | Rejected: `stale current-state parameter range \`FP-P01\`–\`FP-P12\` in acceptance` |
| Conflicting second AI_CONTEXT entry | `12B-78` | added a second current-state B-12 row reporting 12 parameters | R2 selected only the first matching row | check now collects all current-state B-12 inventory rows, requires exactly one, and validates each | `12B-N55` (also `N56` second entry with incomplete 14 claim) | Rejected: `AI_CONTEXT contains 2 conflicting current-state B-12 formula-register entries (expected exactly one)` |

**Shared extraction (correction E).** `extract_param_occurrences` parses the first parameter representation (a comma/`and`-separated chain of IDs or compact ranges), expands ranges to their full consecutive sequence without double-counting endpoints, and returns an ordered occurrence list plus parse problems. `compare_param_occurrences` derives duplicate counts, missing IDs and unexpected IDs against `EXPECTED_PARAM_SET` (the canonical 14). A lone single-ID reference (e.g. an implementation-dependency cell) is not treated as a register-range claim. No partial hard-coded list is duplicated across checks.

**Historical protection.** The current-state stale scan excludes the dated §2.1 reassessment block and lines marked historical/previously/originally/superseded — but a line that still says "current" is not excused by adding "historical" (`12B-N59` proves this). `12B-81` still requires the historical §75 12-parameter record to survive, and `12B-82` the C1 §76.1 note. No project-wide ban on the number 12 was introduced.

### 79.2 Change manifest (12B-C1-R3)

| File | Change |
|---|---|
| `docs/qa_backups/12B_validate_b12.py` | Occurrence-preserving extraction/comparison; checks 77/78 strengthened (duplicates, unexpected IDs, stale-range scan, conflicting entries); fixtures P33 / N49–N59 added; P27/P28 expectations updated to new diagnostics |
| `docs/prompts/prompt_12B-C1-R3_duplicate_id_and_stale_reference_validation.md` | **Created** — verbatim R3 instruction |
| `docs/prompts/INDEX.md` | R3 archive row added |
| `docs/stage-2/06_stage_2_progress_log.md` | This §79 |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row cites §79; validator counts 82/33/59 |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` | R3 status block added; live validator counts updated |

### 79.3 Validation actually run (2026-11-07)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 82/82 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `33/33` positive, `59/59` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45`; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34 PASS` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | PASS; 73/73 fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` / `11C_validate_b11_workflows.py` | PASS | 0 |
| ten `verify_*` scripts | all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, preserved | 1 |

`validate_final.py` is re-run after this entry and the roadmap citation are added; its result is recorded in the final delivery report. No tests were skipped. Every PASS is documentary; no runtime, database, security or production verification is claimed.

**Acceptance and governance, unchanged.** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`); `REQ-764`–`REQ-869`, `D-178`–`D-187`, `DD-226`–`DD-235`, 16 formulas, 14 parameters, 20 INT contracts preserved; `UD-017`, `UD-052`–`UD-060`, `UD-040`–`UD-051` remain Open; Prompt 12C not authorized.

**Verdict.** **Prompt 12B-C1-R3 is COMPLETE at the validator/documentation level.** All four newly identified bypasses and all three earlier R2 bypasses are rejected by explicit negative fixtures; duplicate, unexpected, missing and discontinuous identifiers are detected; stale current-state ranges and conflicting AI_CONTEXT entries are caught; historical records remain valid. C1/R1/R2/R3 closeout is complete to the extent demonstrated by these tests; production implementation and owner/legal rulings remain outstanding.

## 80. Prompt 12B-C1-R4 — gate uniqueness, complete occurrence scanning, historical-section validation and canonical parameter extraction (2026-11-07)

**Scope.** A targeted validator-hardening and documentation-closeout pass closing the seven additional bypasses found by independent mutation testing of R3. It rewrites no B-12 specification substantive content, changes no approved identifier, decision or acceptance meaning, implements nothing, and does not authorize Prompt 12C. The complete `AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0, SHA-256 `697dd52d…b8ad479`) was read; D-014 followed.

**Canonical-source note.** The R4 instruction §8 lists "12 numerical parameters" among items to preserve. The canonical formula register actually defines **14** parameters (`FP-P01`–`FP-P14`, the last two added by 12B-C1). Per R4 §4 the canonical register is the source of truth, so the validator and all current-state documents preserve **14**; the "12" in the instruction is recorded here as an instruction discrepancy, not applied. No parameter was removed or added by R4.

### 80.1 The seven reproduced defects and their closure

| Defect | Check | Mutation | Why R3 passed | Correction | Fixture | Demonstrated outcome |
|---|---|---|---|---|---|---|
| 1 Duplicate P12B-19 row | `12B-77` | inserted a second identical gate row | first-match selection | gate rows collected from the §2 gate-register section; exactly one required | `12B-R4-01` | Rejected: `expected exactly one P12B-19 gate row, found 2` |
| 2 Unexpected ID after semicolon | `12B-77` | `…FP-P14; FP-P15` | only the first comma-chain representation was scanned | `scan_param_occurrences` scans the whole row, formatted or not | `12B-R4-02` | Rejected: `P12B-19 unexpected parameters: FP-P15` |
| 3 Duplicate ID after semicolon | `12B-77` | `…FP-P14; FP-P01` | first-chain extraction missed the extra occurrence | full occurrence counting before any set conversion | `12B-R4-03` | Rejected: `P12B-19 contains duplicate parameter FP-P01 (×2)` |
| 4 Stale current claim inside §2.1 | `12B-77` | inserted `Current formula-register range: FP-P01–FP-P12` in §2.1 | whole §2.1 section was exempted | no section exempt; per-line historical context only; current claims scanned everywhere | `12B-R4-04` | Rejected: `stale current-state parameter range … in acceptance` |
| 5 Unformatted stale range | `12B-77` | `Current formula-register range: FP-P01-FP-P12` (no backticks) | scanner required backticked ranges | range/ID regexes accept optional backticks and hyphen/en-dash/em-dash/ellipsis | `12B-R4-05` (also `N66` em-dash) | Rejected: `stale current-state parameter range FP-P01-FP-P12 …` |
| 6 Unexpected ID outside AI_CONTEXT chain | `12B-78` | appended `Also FP-P15.` to the entry | only the first structured chain validated | whole-entry occurrence scan | `12B-R4-06` | Rejected: `AI_CONTEXT B-12 entry #1 unexpected parameters: FP-P15` |
| 7 Duplicate ID outside AI_CONTEXT chain | `12B-78` | appended `Also FP-P01.` | first-chain extraction | whole-entry occurrence counting | `12B-R4-07` | Rejected: `AI_CONTEXT B-12 entry #1 contains duplicate parameter FP-P01 (×2)` |

### 80.2 Canonical parameter extraction (architectural correction)

The hard-coded `EXPECTED_PARAMS`/`EXPECTED_PARAM_SET` production globals were removed. `Model.rebuild()` now captures the raw ordered parameter IDs (`param_raw`) from the canonical formula register, including malformed tokens. `canonical_params(m)` validates presence, format (`FP-P\d{2}`) and uniqueness, and returns the authoritative ordered collection; a missing/empty register is a failure, never a fallback. `check_76` additionally requires the collection to be contiguous from `FP-P01`. `check_77`/`check_78` derive their expected set and count from this collection and compare full occurrence sequences (duplicates, missing, unexpected, out-of-order). `scan_param_occurrences` expands ranges without double-counting endpoints and counts every other occurrence regardless of punctuation. The AI_CONTEXT inventory entry was reworded so its sole parameter representation is the range (removing redundant bare-ID prose mentions that would otherwise read as duplicates); its substantive meaning is unchanged.

### 80.3 Change manifest (12B-C1-R4)

| File | Change |
|---|---|
| `docs/qa_backups/12B_validate_b12.py` | Canonical extraction; full-occurrence scanner; gate uniqueness; §2.1 current-claim scanning; unformatted/em-dash detection; checks 76/77/78 refactored; fixtures R4-01…R4-07 and N60–N66 added; two R3 ctx fixtures retargeted to the reworded entry |
| `docs/AI_CONTEXT.md` | B-12 inventory entry reworded (sole range representation); R4 status block; live validator counts |
| `docs/prompts/prompt_12B-C1-R4_gate_uniqueness_and_canonical_extraction.md` | **Created** — verbatim R4 instruction |
| `docs/prompts/INDEX.md` | R4 archive row added |
| `docs/stage-2/06_stage_2_progress_log.md` | This §80 |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row cites §80; validator counts 82/33/73 |
| `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` | R4 status block added; live validator counts updated; handoff notes the next audit is against the separate R4 instruction |

### 80.4 Validation actually run (2026-11-07)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 82/82 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `33/33` positive, `73/73` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45`; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34 PASS` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | PASS; 73/73 fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` / `11C_validate_b11_workflows.py` | PASS | 0 |
| ten `verify_*` scripts | all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, preserved | 1 |

`validate_final.py` is re-run after this entry and the roadmap citation are added; its result is recorded in the final delivery report. No tests were skipped or timed out. The R1–R3 fixture suite (33 positive / 59 negative) ran unchanged before and after the R4 edits and continues to pass; R4 adds 14 negative fixtures (73 total). Every PASS is documentary; no runtime, database, security or production verification is claimed.

**Acceptance and governance, unchanged.** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`); 344 rules, 106 requirements `REQ-764`–`REQ-869`, 16 formulas, 14 parameters, `D-178`–`D-187`, `DD-226`–`DD-235`, 20 INT contracts preserved; `UD-017`, `UD-052`–`UD-060`, `UD-040`–`UD-051` remain Open; Prompt 12C not authorized. Supabase `profiles` privilege and audit-log obligations remain documented and unimplemented.

**Verdict.** **Prompt 12B-C1-R4 is COMPLETE at the validator/documentation level.** All seven newly identified bypasses are rejected by explicit fixtures; the canonical register is the genuine source of truth; full occurrence scanning closes alternate-punctuation and extra-text bypasses; stale current claims are caught even inside §2.1 while historical references remain valid; all R1–R3 protections are preserved. Production implementation and owner/legal rulings remain outstanding.

## 81. Prompt 12B-C1-R5 — malformed identifier detection, complete current-state scanning, canonical definition integrity and gate register hardening (2026-11-07)

**Scope.** A targeted validator-hardening, adversarial-testing and documentation-synchronization pass closing the seven additional bypasses reproduced against the live validator (Project X (74) audit baseline). It rewrites no B-12 specification substantive content, changes no approved identifier, decision or acceptance meaning, implements nothing, and does not authorize Prompt 12C. The complete `AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0, SHA-256 `697dd52d…b8ad479`) was read; D-014 followed.

**Canonical-source note.** The R5 instruction §8 again lists "12 numerical parameters" among items to preserve. The canonical formula register defines **14** FP-P parameters (`FP-P01`–`FP-P14`). Per R5 §4/§7 the canonical register is the source of truth, so the validator and current-state documents preserve **14**; the "12" is recorded as an instruction discrepancy, not applied. There is no separate 12-parameter collection in the live documentation.

### 81.1 Independent reproduction and closure of the seven findings

Each finding was first reproduced against the live validator (all returned PASS = bypass), then corrected and re-tested (all now REJECT with a specific diagnostic).

| Defect | Reproduced mutation | Before | Correction | After (fixture) |
|---|---|---|---|---|
| 1 Malformed gate token | append `FP-PXX` to P12B-19 | PASS | `malformed_param_tokens` scans the FP-P namespace; check_77 gate diagnostic | REJECT `P12B-19 contains malformed parameter identifier(s): FP-PXX` (`R5-01`; also `N67` FP-P1, `N68` FP-P001, `N69` FP-P01X) |
| 2 Stale individual IDs | `Current formula-register identifiers: FP-P01, FP-P12.` | PASS | register-claim lines scanned for individual-ID sets vs canonical | REJECT `stale current-state parameter identifiers …` (`R5-02`, `R5-03` backticked, `R5-12` partial) |
| 3 Unformatted canonical duplicate | duplicate `FP-P14` row without backticks | PASS | `param_raw` extracts §3 definition first-cells regardless of backticks | REJECT `duplicate canonical parameter definition: FP-P14` (`R5-04`, `R5-10`) |
| 4 Historical-label bypass | `Historical note: … now contains only FP-P01–FP-P12.` | PASS | meaning-based `is_historical_exempt` (historical marker AND no present-state marker) | REJECT `stale current-state parameter range …` (`R5-05`, `R5-20` mixed) |
| 5 AI_CONTEXT narrow scan | unexpected `FP-P15` in b12 registry key | PASS | check_78 also scans the `b12_fair_play` current key for unexpected/malformed/count | REJECT `AI_CONTEXT b12_fair_play current entry unexpected parameters: FP-P15` (`R5-06`) |
| 6 Malformed gate ID | add `P12B-19X` gate-like row | PASS | check_61 validates every gate-like first cell format + uniqueness | REJECT `malformed gate identifier(s): P12B-19X` (`R5-07`, `R5-15` P12B-19A) |
| 7 Hard-coded count in check_45 | `len(m.params) == 14` | hard-coded | check_45 derives count from `canonical_params` and validates the register's declared count | PASS source-derived (`R5-08`); a changed canonical count desyncs the declaration and is detected |

### 81.2 Canonical extraction and scanning architecture

`Model.param_raw` now extracts the leading `FP-P` token of each §3 parameter-register definition row with or without backticks (explanatory mentions outside the definition table are not definitions). `canonical_params` validates presence/format/uniqueness; `check_76` enforces contiguity; `check_45` derives the count and validates the declared `**Parameters: N**` sentence. `scan_param_occurrences` preserves ordered occurrences (ranges expanded without double-counting endpoints); `compare_param_occurrences` reports duplicate/missing/unexpected/out-of-order before any set conversion. `malformed_param_tokens` flags any FP-P namespace token failing `FP-P\d{2}`. `acceptance_stale_problems` scans the whole acceptance document (including §2.1) for malformed tokens, count claims, ranges and individual-ID register assertions, with meaning-based historical exemption. `check_78` validates the inventory row plus the `b12_fair_play` current key. `check_61` validates gate-ID format and uniqueness. The fixture harness now supports positive fixtures that apply a mutation (used to prove historical/explanatory content is accepted).

### 81.3 Change manifest (12B-C1-R5)

| File | Change |
|---|---|
| `docs/qa_backups/12B_validate_b12.py` | Malformed-token detection; meaning-based historical classification; register-claim individual-ID scanning; canonical definition extraction unformatted; check_45 source-derived; check_61 gate format/uniqueness; check_78 full current B-12 scanning; positive-mutation fixture support; fixtures R5-01…R5-20 and N67–N69 added |
| `docs/prompts/prompt_12B-C1-R5_malformed_id_and_canonical_integrity.md` | **Created** — verbatim R5 instruction |
| `docs/prompts/INDEX.md` | R5 archive row added |
| `docs/stage-2/06_stage_2_progress_log.md` | This §81 |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row cites §81; validator counts 82/37/92 |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` | R5 current-status block added; outdated validator totals synchronized; historical R3/R4 results preserved as dated snapshots; handoff notes Project X (74) baseline, R5 current task, R5 prompt must accompany the fresh ZIP, independent adversarial audit still required, Prompt 12C unauthorized |

### 81.4 Validation actually run (2026-11-07)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 82/82 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `37/37` positive, `92/92` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45`; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34 PASS` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | PASS; 73/73 fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` / `11C_validate_b11_workflows.py` | PASS | 0 |
| ten `verify_*` scripts | all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, preserved | 1 |

`validate_final.py` is re-run after this entry and the roadmap citation are added; its result is recorded in the final delivery report. No tests were skipped or timed out; no broad pytest run was attempted (targeted unittest suites used). The R1–R4 suite (33 positive / 73 negative) ran unchanged before and after the R5 edits and continues to pass; R5 adds 4 positive and 19 negative fixtures (37 / 92 total). Every PASS is documentary; no runtime, database, security or production verification is claimed, and no independent audit acceptance is claimed.

### 81.5 Working-tree disruption and recovery (disclosed for audit)

During R5 execution an external `git stash`/checkout operation (stash "Qoder 检出分支临时保存", HEAD `bdbdd14` initial snapshot) introduced stash-apply conflicts across 24 tracked files and cleanly deleted the 12A requirements/integration register. With owner authorization ("Take Stashed changes"), the conflicted files were restored directly from the stash blobs (the consistent advanced state: UD-001…UD-060, 28/3/29, REQ-869, DD-235, D-187, §81), the deleted `12A_requirements_integration_and_risk_registers.md` was restored from the stash, and the R5 current-status blocks/roadmap §81 citation were re-applied to the continuity files. The `10B_validate_warfare.py` frontier assertions, reverted to the 11C-era baseline by the checkout, were re-synchronized to the current frontier (UD 28/3/29; current sub-prompt 12B) — a frontier advance, not a weakening. No Git staging, commit or push was performed; the index still reflects the owner's in-progress stash workflow. All results in §81.4 were re-confirmed after recovery.

**Acceptance and governance, unchanged.** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`); 344 rules, 106 requirements `REQ-764`–`REQ-869`, 16 formulas, 14 parameters, `D-178`–`D-187`, `DD-226`–`DD-235`, 20 INT contracts preserved; `UD-017`, `UD-052`–`UD-060`, `UD-040`–`UD-051` remain Open; Prompt 12C not authorized. Supabase `profiles` privilege and audit-log obligations remain documented and unimplemented.

**Verdict.** **Prompt 12B-C1-R5 is COMPLETE at the validator/documentation level.** All seven reproduced bypasses are rejected by explicit fixtures with specific diagnostics; malformed identifiers, stale individual claims, unformatted canonical duplicates, historical-label bypasses, narrow AI_CONTEXT scanning and malformed gate IDs are closed; check_45 is source-derived; all R1–R4 protections are preserved. Independent adversarial acceptance remains pending; production implementation and owner/legal rulings remain outstanding.

## 82. Prompt 12B-C1-R6 — final validator hardening, full document-block parsing, semantic claim classification and complete canonical integrity (2026-11-08)

**Scope.** The final planned corrective pass for Prompt 12B-C1. It hardens the validator architecture (complete document-block parsing, full occurrence accounting, semantic current/historical/explanatory classification, canonical definition integrity in table and prose, complete AI_CONTEXT entry scanning), adds adversarial fixtures, and synchronizes documentation. It rewrites no B-12 specification substantive content, changes no approved identifier/decision/acceptance meaning, implements nothing, and does not authorize Prompt 12C. The complete `AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0, SHA-256 `697dd52d…b8ad479`) was read; D-014 followed.

**Canonical-source note.** The R6 instruction §9 again lists "12 numerical parameters" alongside "14 canonical FP-P parameters". The canonical formula register defines **14** FP-P parameters (`FP-P01`–`FP-P14`); there is no separate 12-parameter FP-P collection in the live documentation. Per R6 §5 the canonical register is the source of truth, so validation preserves 14; the "12" is recorded as an instruction discrepancy, not applied.

### 82.1 Pre-implementation reproduction and closure of the six R5 bypasses

Each was reproduced against the live complete validator (all accepted = bypass) before correction, then re-tested through the production checks (all rejected):

| Defect | Reproduced mutation | Before | Correction | After |
|---|---|---|---|---|
| 1 AI_CONTEXT entry not fully scanned | continuation line with FP-P15 / duplicate FP-P01 / incomplete list | accepted | `check_78` parses the complete entry block (authoritative row + continuation lines until next row/heading/blank) plus the `b12_fair_play` key; whole-block occurrence accounting + per-statement collection claims | rejected (`R6-01/02/03`) |
| 2 Acceptance stale-claim scanning incomplete | "parameter set includes FP-P01, FP-P12"; assertion split across lines | accepted | `logical_statements` joins continuation lines; `REGISTER_CLAIM_RE` expanded (parameter set, authoritative parameters, register parameters); per-statement collection-claim validation | rejected (`R6-04/05/07`) |
| 3 Canonical prose definitions escape | prose "FP-P14 is also defined…"; "FP-P-01 = …" | accepted | `Model.param_raw` extracts §3 definition region as a structured document: table first cells AND ordinary-text definition records (`FP-P…` followed by `=`/`is`/`defined`/separator) | rejected (`R6-10/11`) |
| 4 Historical classification keyword-heavy | "Historical note: … includes FP-P01, FP-P12" | accepted | `CURRENT_MARKERS` extended (includes/uses/consists); a historical qualifier with a present-tense assertion is evaluated as current | rejected (`R6-06`) |
| 5 Malformed tokens not comprehensive | FP-P01_extra / FP-P. / FP-P-01 | accepted (or misclassified as duplicate) | `namespace_tokens` lexical scanner preserves raw token text; `scan_param_occurrences` refuses to extract a valid prefix from a malformed larger token | rejected as malformed (`R6-08/09`, `N70`) |
| 6 Complete occurrence accounting | occurrences lost via line-only/first-match parsing | accepted | reusable `logical_statements`, `namespace_tokens`, `scan_param_occurrences`, `compare_param_occurrences`; ordered occurrences validated before set conversion | rejected (`R6-02/17/18`) |

### 82.2 Architecture

- **Document-block parsing:** `logical_statements(text)` joins prose continuation lines into logical statements while keeping table rows and headings as separate boundaries; `check_78` builds the complete B-12 entry block structurally; the canonical §3 definition region is parsed as a structured document.
- **Occurrence model:** `namespace_tokens(text)` returns `(raw, normalized, is_valid, start)` for every FP-P candidate, excluding valid-range spans and retaining original token text; trailing sentence punctuation is stripped for classification only. `scan_param_occurrences` expands ranges without double-counting endpoints and skips IDs embedded in malformed candidates. `compare_param_occurrences` reports duplicate/missing/unexpected/out-of-order before any set conversion.
- **Classification:** `is_historical_exempt` requires genuine historical context AND no present-state marker; collection claims (`REGISTER_CLAIM_RE`) are validated against the canonical ordered collection; explanatory mentions of canonical IDs remain valid; non-canonical IDs in current content are rejected.
- **Canonical source-of-truth:** `canonical_params` derives the ordered collection from actual §3 definition records (table + prose), validates format/uniqueness; `check_76` enforces contiguity; `check_45` derives the count and validates the declared `**Parameters: N**` sentence. No hard-coded production fallback remains.

### 82.3 Change manifest (12B-C1-R6)

| File | Change |
|---|---|
| `docs/qa_backups/12B_validate_b12.py` | `namespace_tokens`, `logical_statements`; refactored `scan_param_occurrences`, `malformed_param_tokens`, `is_historical_exempt`, `acceptance_stale_problems`, `check_78`; canonical prose extraction in `Model.rebuild`; fixtures R6-01…R6-30 and N70; P28 diagnostic wording updated |
| `docs/prompts/prompt_12B-C1-R6_full_document_block_and_semantic_validation.md` | **Created** — verbatim R6 instruction (36,689 bytes; LF/UTF-8) |
| `docs/prompts/INDEX.md` | R6 row + reproducible checksum convention |
| `docs/stage-2/06_stage_2_progress_log.md` | This §82 |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row cites §82; validator counts 82/45/115 |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` | R6 current-status block; live validator counts updated; historical R3/R4/R5 totals retained as dated snapshots |

### 82.4 Validation actually run (2026-11-08)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 82/82 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `45/45` positive, `115/115` negative rejected for the expected reason | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45`; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 — ALL CHECKS PASSED` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34 PASS` | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | `1036 — PASS`; 73/73 fixtures | 0 |
| `python docs/qa_backups/11B_validate_b11.py` / `11C_validate_b11_workflows.py` | PASS | 0 |
| ten `verify_*` scripts | all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — legacy check 29 expects `REQ-703`; pre-existing `D-1`, preserved | 1 |

`validate_final.py` is re-run after this entry and the roadmap citation are added; its result is recorded in the final delivery report. No tests were skipped or timed out; no broad pytest run was attempted (targeted unittest suites used). The R1–R5 suite (37 positive / 92 negative) ran unchanged and continues to pass; R6 adds 8 positive and 23 negative fixtures (45 / 115 total). Every PASS is documentary; no runtime, database, security or production verification is claimed, and no independent audit acceptance is claimed.

### 82.5 Git state (read-only inspection, no changes)

Branch `main`, HEAD `bdbdd14` ("Initial complete Nation Supremacy project snapshot"). The working tree has **no conflict markers** (R5 resolved the content), but the Git index still carries 24 unmerged `UU`/`DU` entries from the owner's prior stash workflow. Per R6 §10 no staging/commit/push/merge/rebase/reset/checkout/stash or conflict resolution was performed; the index is reported exactly as observed and left untouched. R6 changes are confined to authorized validator/archive/synchronization files.

**Acceptance and governance, unchanged.** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`); 344 rules, 106 requirements `REQ-764`–`REQ-869`, 16 formulas, 14 canonical FP-P parameters, `D-178`–`D-187`, `DD-226`–`DD-235`, 20 INT contracts preserved; `UD-017`, `UD-052`–`UD-060`, `UD-040`–`UD-051` remain Open; Prompt 12C not authorized. Supabase `profiles` privilege and audit-log obligations remain documented and unimplemented.

**Verdict.** **Prompt 12B-C1-R6 is COMPLETE at the implementation/documentation level.** All six independent R5 bypasses are rejected by the production validator through reusable document-block parsing and complete occurrence accounting; canonical definitions in table and prose are extracted; current/historical/explanatory classification is semantic; the complete AI_CONTEXT entry is scanned; gate integrity and source-derived counting are preserved; all R1–R5 protections remain operational. Independent R6 acceptance remains pending; production implementation and owner/legal rulings remain outstanding.

## 83. Prompt 12B-C1-R7 — final structural validation, complete AI_CONTEXT entry integrity, semantic assertion parsing and canonical definition discovery (2026-11-09)

**Scope.** A targeted corrective pass on the Prompt 12B-C1 validator-hardening sequence after R6 failed independent acceptance. It replaces line-selected and keyword-selected parsing with structural document parsing, semantic statement classification and occurrence-level accounting; makes the canonical register the only production source of truth for the FP-P collection; runs every fixture through the complete check registry; adds an end-to-end subprocess mutation audit; and synchronizes documentation. It rewrites no B-12 specification substantive content, changes no approved identifier, decision or acceptance meaning, closes no PARTIAL gate, implements nothing, and does not authorize Prompt 12C. The complete `docs/AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0, SHA-256 `697dd52d…db8ad479`) was read in full before the work; D-014 was followed: parsing architecture, fixture design, diagnostic wording and documentation layout were decided autonomously as Category B and recorded here, with no owner-reserved or legal-dependent decision touched.

**Audited baseline.** `Project X (76).zip` is the previous independently audited snapshot. Its bundled validator reported 82/82 checks, 45/45 positive and 115/115 negative fixtures with exit 0, and all 30 numbered R6 fixtures passed; independent mutation testing nevertheless demonstrated eight further bypasses. R7 is the corrective response to those eight. **Independent R7 acceptance is pending** and is not claimed here. R6's own implementation totals (82/45/115) remain historical R6 results, not current results.

### 83.1 Pre-implementation reproduction of the eight R7 bypasses

Each mutation was applied to an isolated copy of the live corpus and executed against the **complete 82-check production validator** (every registered check, not a helper) before any correction. Seven of the eight were accepted outright (exit 0). The eighth, R7-04, was accepted in all three faithful constructions of "additional continuation text containing a parameter assertion"; one stronger construction (a conflicting chain on the line immediately after the authoritative inventory row) was already caught by R6's block-level duplicate accounting and is recorded as covered by R6 rather than as a bypass.

| ID | Mutation | Result against the pre-R7 production validator |
|---|---|---|
| R7-01 | duplicate `FP-P01` inside the current `b12_fair_play` entry | **accepted — bypass** |
| R7-02 | current B-12 entry states no parameter representation at all | **accepted — bypass** |
| R7-03 | incomplete current assertion in a paragraph separated from the entry row | **accepted — bypass** |
| R7-04 | continuation of the status entry / blank-line-separated continuation / status blockquote, each stating a conflicting collection | **accepted — bypass (all three variants)** |
| R7-05 | additional B-12 parameter inventory row naming no register file | **accepted — bypass** |
| R7-06 | incomplete current collection asserted inside acceptance §2.1 | **accepted — bypass** |
| R7-07 | `Historical record: the B-12 formula parameters remain FP-P01 and FP-P12.` | **accepted — bypass** |
| R7-08 | duplicate canonical definition carried in a Markdown heading | **accepted — bypass** |

### 83.2 Corrections

| Defect | Root cause found in the live file | R7 correction | Evidence |
|---|---|---|---|
| 1 — AI_CONTEXT entry parsed by selected lines | `check_78` selected one table row plus directly-adjacent non-table lines and read the `b12_fair_play:` line as a single line; duplicates, ordering, missing representations, extra inventory rows and paragraphs outside that slice were invisible | `iter_blocks()` parses the whole document into headings, table rows, list items, key entries, paragraphs, blockquotes and code with line spans; `b12_entry_blocks()` builds the entry transitively from the status record and the register row plus every attached block; the entry then requires exactly one authoritative register entry, at least one complete representation in the status record, and per-representation plus cross-representation occurrence comparison | `12B-R7-01/02/03/04/05`, `12B-R7-N01`–`N06`, `N13`–`N15` |
| 2 — acceptance claims matched by a phrase whitelist | `REGISTER_CLAIM_RE` was a fixed keyword alternation and `acceptance_stale_problems` skipped any statement it did not recognize, so "The current parameter list is …", "The B-12 inventory contains …" and any unlisted wording escaped | claims are detected structurally: a range, a count claim, a collective noun with an equative predicate (verb or colon) positioned **before** the enumeration, or a present-state reference to the entry/register/inventory locus; every detected representation is compared with the full ordered canonical collection, and a representation that cannot be decided is reported as ambiguous instead of skipped | `12B-R7-06`, `12B-R7-N07`, `N09`–`N12`, `N27`, `12B-85` |
| 3 — keyword historical exemption | `is_historical_exempt(low)` exempted any statement containing a historical word and lacking a short current-marker list, so `remain` — and any unlisted present-state verb — let a present claim escape | classification is clause-governed: the clause preceding the enumeration decides tense; a present-state predicate in that clause always wins; exemption requires a date, a past-tense predicate or an explicit supersession; the seven classes are current-assertion, historical, superseded, explanatory, canonical-definition, malformed-candidate and ambiguous | `12B-R7-07`, `12B-R7-N13`, `12B-86`, positives `12B-R7-P09`/`P10` |
| 4 — canonical headings skipped | `Model.rebuild()` iterated the §3 region and discarded every line beginning with `#`, so a definition carried in a heading was never a candidate | `canonical_region_blocks()` determines the region boundary structurally and reports an undeterminable boundary; `canonical_definitions()` inspects every block kind (table first cell, heading, list item, paragraph, definition list), keeps malformed candidates as failures, rejects duplicates across formats, rejects definition records outside the boundary, and never counts a plain mention as a definition | `12B-R7-08`, `12B-R7-N16`–`N23`, `12B-84` |
| 5 — occurrence accounting lost before comparison | scanning reduced matches to sets or to first matches, so a token split across a wrapped line, a token followed by punctuation, or a valid prefix inside a larger malformed token disappeared or was misreported | `scan_occurrences()` returns an `Occurrence` per token carrying source, section heading path, line, span, original raw text, normalised identifier, form (`range`/`standalone`/`malformed`), statement, structural context, classification, order and outcome; ranges expand before any set is built; maximal-munch candidates plus a preceding-character contamination test prevent prefix extraction; containment is measured on the identifier body so trailing punctuation cannot hide a range endpoint; document order is restored by span before comparison | `12B-R7-N03`/`N04`/`N05`/`N08`, `12B-83` |
| 6 — the fixture harness proved a helper, not the validator | `run_fixtures` executed only the single named check per fixture, so an aggregate pass said nothing about the complete validator | `evaluate()` deep-copies the corpus, applies the mutation, rebuilds and runs **all 87 checks**; a positive fixture requires zero failures and zero exceptions; a negative fixture requires the named check to fail with the expected reason and requires that no check raised | all 212 fixtures |
| 7 — no independent-style end-to-end proof | mutations were applied only to in-memory strings | `--mutation-audit` copies every file the validator reads into an isolated tree, writes the mutated file, runs this validator as a subprocess and asserts the exit code plus the rejecting check and reason (23 audited mutations: 19 rejected for the intended reason, 4 legitimate variants still accepted) | `MUTATION AUDIT: 23/23` |

### 83.3 Architecture now in the production path

- **Structural parsing:** `Block`, `iter_blocks()`, `split_statements()`. Block kinds are heading, table-row, list-item, key-entry, paragraph, blockquote and code. Continuation and indented lines join the block they continue; a heading is a block, never a discarded line.
- **Occurrence model:** `Occurrence`, `scan_occurrences()`, `occurrence_stream()`; `namespace_tokens()`, `malformed_param_tokens()` and `scan_param_occurrences()` are thin wrappers over the same scanner, so there is one lexical path rather than parallel regular expressions. Lookup sets are built only after occurrence-level validation.
- **Semantics:** `classify_statement()`, `is_historical_exempt()` (now delegated), `representation_problems()`, `param_representation()`, `acceptance_current_problems()`, `b12_entry_blocks()`.
- **Canonical truth:** `canonical_region_blocks()`, `canonical_definitions()`, `canonical_params()` reading the records discovered by `Model.rebuild()`. The ordered collection, the expected identifier sequence, the expected count and the expected unique set all derive from the register: no fixed list, no hidden duplicate expectation, no silent fallback and no reliance on the number 14. `check_45` keeps its source-derived count behaviour, and the separate Prompt 12B "12 numerical parameters" metric stays distinct from the FP-P collection.
- **Strict versus explanatory scope:** inside the AI_CONTEXT B-12 entry a statement that adds an identifier to the enumeration extends the authoritative representation, so a duplicate cannot escape; a well-formed explanatory mention of a canonical identifier remains valid in both documents. The acceptance document legitimately restates the collection in several sections, so cross-section duplicate accounting is applied per representation there rather than document-wide.

### 83.4 Change manifest (12B-C1-R7)

| File | Change |
|---|---|
| `docs/qa_backups/12B_validate_b12.py` | `Block`/`Occurrence` models; `iter_blocks`, `split_statements`, `scan_occurrences`, `occurrence_stream`, `leading_index`, `after_token`; rewritten `namespace_tokens`, `malformed_param_tokens`, `scan_param_occurrences`, `is_historical_exempt`, `logical_statements`; new `classify_statement`, `representation_problems`, `param_representation`, `acceptance_current_problems`, `b12_entry_blocks`, `canonical_region_blocks`, `canonical_definitions`; rewritten `Model.rebuild()` parameter extraction, `canonical_params`, `check_76`, `check_77`, `check_78`; new checks `12B-83`–`12B-87` (87 checks); fixtures now run the complete registry via `evaluate`; `--mutation-audit`; 8 named R7 fixtures, 30 further negative fixtures and 14 positive fixtures (212 fixtures in total) |
| `docs/prompts/prompt_12B-C1-R7_final_structural_validation_and_canonical_integrity.md` | **Created** — verbatim R7 instruction (25,689 bytes; LF/UTF-8; SHA-256 `010bbd0f…ed4f7`) |
| `docs/prompts/INDEX.md` | R7 row with path, date, source, size and SHA-256; checksum convention extended to R7 |
| `docs/stage-2/06_stage_2_progress_log.md` | This §83 |
| `docs/stage-2/20_fair_play_and_player_protection_acceptance.md` | §9.1 check groups extended to `12B-87`; §9.2 fixture totals plus the complete-registry and subprocess-audit wording updated. Gate rows, rule counts and the three PARTIAL classifications untouched |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md` | R7 current-status entry added; the synchronized `b12_fair_play:` status line and live validator counts updated; R1–R6 dated totals preserved as historical snapshots |

### 83.5 Validation actually run (2026-11-09)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 87/87 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `59/59` positive accepted and `153/153` negative rejected for the expected reason, each through the complete registry; `CHECKS: 87/87` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --mutation-audit` | `MUTATION AUDIT: 23/23` handled by the production validator as a subprocess (19 rejected for the intended reason, 4 legitimate variants accepted); 0 wrong | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `45/45` checks; `10/10` positive, `33/33` negative | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed — ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943 — PASS` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `34/34` semantic checks passed | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 1036 — PASS`; `73/73` negative fixtures rejected | 0 |
| `python docs/qa_backups/11B_validate_b11.py` | `61/61` checks; `16/16` positive, `44/44` negative | 0 |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `31/31` checks; `8/8` positive, `17/17` negative | 0 |
| ten `verify_*` scripts | alliance, alliance-workflows, city, diplomacy, diplomacy-workflows, economy, market, market-workflows, politics (`879/879`), warfare-workflows (`49/49`) — all PASS | 0 each |
| `python docs/qa_backups/validate_links.py` | link gate passed; self-test `11/11` | 0 |
| `python -m unittest test_next_action test_decision_registers` | `Ran 39 tests … OK` (run from `docs/qa_backups`) | 0 |
| `python -m unittest test_09A_alliance_validator` | `Ran 43 tests in 17.891s — FAILED (failures=1)`; the one failure is stale fixture text, independently disproven above | 1 |
| `python -m unittest test_09B_alliance_semantic_validator` | `Ran 267 tests in 2912.500s — FAILED (failures=3)`; all three are stale alliance-era fixture premises, root-caused below | 1 |
| four-module combined unit run | `Ran 349 tests in 2655.762s — FAILED (failures=4)`, all four inside the alliance modules | 1 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 EXECUTED, 1 FAILED` — legacy check 29 still expects `REQ-703`; pre-existing `D-1` frontier debt, unchanged by R7 and not repaired here | 1 |

Every 12B run completed: the checks, both fixture classes and the subprocess mutation audit all finished with exit 0, and no fixture was skipped. Alliance unit-test outcomes are recorded below exactly as observed, with each failure root-caused rather than smoothed over. `python -m unittest test_09A_alliance_validator` runs **43 tests in 17.9s with 1 failure**, `test_40_disagreement_on_next_prompt`, whose fixture mutates the string `stage_2_next_prompt: 11` — a value that no longer exists in the corpus (the registered next prompt is `12C`), so the mutation is a no-op and the validator correctly reports nothing. The failure is **pre-existing stale test data, not an R7 regression and not a lost protection**: re-running the alliance validator against an isolated copy in which the value really is changed to `09C` produces `Checks run: 943`, `FAIL: 1 problem(s) — 8-handoff :: AI_CONTEXT status block does not set Prompt 10/10A/10B/10C, 11/11A/11B/11C or 12/12A/12B/12C as the active prompt`, so cross-file STATUS disagreement is still detected. `python -m unittest test_09B_alliance_semantic_validator` completed in the background after this entry was first written: **267 tests in 2912.500s, FAILED (failures=3)**, and every one of the three is a stale alliance-era premise rather than a lost protection. `test_49_req591_deferral_removed_fails` sets REQ-591's status cell to `**Provisional**`, but the corpus already records it as Provisional (the requirements tracker states that REQ-014 and REQ-591 moved to Provisional because B-10 now specifies military combat), so the mutation is a no-op. `test_54_missing_decision_fails` expects the `[C17]` diagnostic to read `D-001..D-142` while the decision register legitimately spans `D-001..D-187`, and the deletion **is** still detected, as `[C06] AX-01` through `AX-09 references non-existent D id D-138`. `test_59_next_prompt_changed_fails` anchors on `stage_2_next_prompt: 10B`, a value that no longer exists. The combined four-module run observed **349 tests in 2655.762s, 4 failures** — these three plus the `test_09A` case above — and none of the 39 continuity/decision-register tests failed. R7 changed no alliance document, no decision register and no requirement tracker, so none of these was repaired here: correcting another prompt family's stale test fixtures is outside the authorized R7 file scope and would alter behaviour the Prompt 09 and Prompt 10 owners still rely on. The R6 regression baseline (82 checks, 45 positive, 115 negative, all 30 numbered R6 fixtures and the seven numbered R4 fixtures) ran unchanged and still passes: every earlier fixture keeps its original id, target check and expected reason, and no earlier check was weakened or removed. Two diagnostics were **strengthened**, not relaxed, and the reason is recorded: `check_76` now separates a missing identifier from a reordered one (a reordered register can no longer be reported as merely "non-contiguous"), and the R6/R4 AI_CONTEXT reason strings are now asserted through the complete registry instead of through one isolated check.

### 83.6 Git state (read-only inspection, nothing modified)

Branch `main`, HEAD `bdbdd14` ("Initial complete Nation Supremacy project snapshot"), up to date with `origin/main`. The working tree still carries the owner's prior unmerged index state — `UU` entries for the continuity files, several validators and the Stage 2 registers, plus `DU` entries for `12A_sync_docs.py`, `12A_validate_foundations.py` and the two `12A` research files — and no conflict markers exist in the file contents. Per R7 §1 nothing was staged, committed, pushed, merged, rebased, reset, checked out, stashed or resolved; `git status` was inspected read-only and the index left exactly as found.

**Acceptance and governance, unchanged.** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`) / 0 FAIL / 0 BLOCKED; 344 rules, 106 requirements `REQ-764`–`REQ-869`, 16 formulas, 14 canonical FP-P parameters as extracted from the register, `D-178`–`D-187`, `DD-226`–`DD-235` and 20 `INT-` contracts preserved; `UD-017`, `UD-052`–`UD-060` and `UD-040`–`UD-051` remain Open; no owner-reserved decision was closed and no provisional requirement was approved. Outstanding production obligations remain documented and unimplemented: the authenticated table-wide `UPDATE` on `feasibility.profiles`, the missing corrective migration `0005`, the absent `tests/sql/` permission tests, the unprotected `audit` table (no protective trigger), unverified production tamper-evidence and no production audit-digest verification job. **Prompt 12C is not started and remains unauthorized.**

## 84. Prompt 12B-C1-R8-D — formal deferral of R8, residual-defect preservation and project progression authorization (2026-11-10)

**Scope.** A governance and deferral record only. It preserves the owner's decision that **R8 is deferred**, states the R7 result accurately, keeps the five independently demonstrated validator bypass classes on the record as known residual weaknesses, and confirms that nothing was corrected, implemented, accepted or closed. No validator code, fixture, formula, requirement, acceptance gate or specification was changed. `docs/AUTONOMOUS_DECISION_POLICY.md` (121 lines, version 1.0) was read in full before the work, and D-014 was followed: the record's layout and wording are Category B documentation, while the deferral itself is an owner decision and is transcribed here rather than reinterpreted. No `D-`, `DD-` or `UD-` identifier was allocated and `D-001..D-187` is unchanged, because this is a status and deferral record, not a new design decision.

**Audited baseline for the deferral.** The independent audit of `Project X (77)` reported **five further bypass classes** in the R7 validator even though its registered checks and fixtures reported success. That audit is the basis of the owner's decision; it is **not** an audit performed by this pass, and this section does not re-run, re-derive or confirm its findings. `Project X (76)` remains the baseline recorded by R7; `Project X (77)` is the snapshot on which R7 failed independent acceptance. No new archive or ZIP is produced here.

### 84.1 R7 status, preserved without conversion

| Item | Recorded status |
|---|---|
| R7 implementation | **RETAINED** |
| Registered validator checks | **87/87 PASS** |
| Positive fixtures | **59/59 PASS** |
| Negative fixtures | **153/153 PASS** |
| Subprocess mutation audit | **23/23 PASS** |
| Eight R6 regression reproductions | **REJECTED** (by the retained R7 implementation) |
| R7 independent acceptance | **NOT ACCEPTED** |
| Five independently discovered bypass classes | **KNOWN RESIDUAL WEAKNESSES** |

Registered test success is **not** independent acceptance. The four R7 figures describe the validator's own checks, fixtures and audit cases executed against the corpus they were written for; they say nothing about a bypass class designed from outside that set. Both statements hold at once and neither is converted into the other.

### 84.2 The five known residual weaknesses

Preserved in the owner's wording. These labels (`R8-D-W1`…`R8-D-W5`) are record markers, not specification or acceptance identifiers.

| Label | Residual weakness (owner's wording) | Recorded state |
|---|---|---|
| `R8-D-W1` | Unrecognized incomplete current-state parameter assertions | KNOWN RESIDUAL WEAKNESS — not corrected |
| `R8-D-W2` | AI_CONTEXT block-boundary parsing weakness | KNOWN RESIDUAL WEAKNESS — not corrected |
| `R8-D-W3` | Canonical register table parsing weakness | KNOWN RESIDUAL WEAKNESS — not corrected |
| `R8-D-W4` | Unicode malformed identifier suffix detection weakness | KNOWN RESIDUAL WEAKNESS — not corrected |
| `R8-D-W5` | Multiline malformed identifier suffix detection weakness | KNOWN RESIDUAL WEAKNESS — not corrected |

The specimen mutations and file or line references that demonstrated these classes were reported through the independent audit of `Project X (77)` and are **not present in this repository**; they are not reconstructed, replaced with paraphrases, re-executed or claimed here. If the owner supplies them, they can be appended to this table without changing any recorded fact. No root-cause analysis, fix, fixture or coverage expansion was performed for any of the five, and none is described as corrected anywhere in this project.

### 84.3 Deferral terms

| Term | Record |
|---|---|
| R8 status | **DEFERRED BY OWNER** |
| Decision date | 2026-11-10 |
| Reason | Avoid endless validator-hardening cycles and prioritize actual game development |
| Reopening condition | Explicit owner authorization only |
| Automatic reopening | **PROHIBITED** |
| Unsolicited additional R8 correction prompts | **PROHIBITED** |
| Relationship to the five weaknesses | The deferral accepts known residual weakness; it is **not** approval, correction or dismissal of the five classes |

No R8 implementation and no R8 correction prompt was created. This section is the only R8 record; no row was added to `docs/prompts/INDEX.md`, because the R8-D instruction is a governance instruction rather than a corrective prompt, and creating an "R8 prompt" file would contradict the prohibition above.

### 84.4 Governance state preserved

- **12B-C1: NOT CLOSED.** R7 is retained; independent acceptance was not achieved; no artificial acceptance or closure is recorded.
- **Acceptance:** 23 PASS / 3 PARTIAL (`P12B-14`, `P12B-16`, `P12B-23`) / 0 FAIL / 0 BLOCKED — unchanged; no gate was reassessed, renamed or reclassified.
- **Specification content:** 344 rules, 106 requirements `REQ-764`–`REQ-869` (86 Provisional / 20 Open), 16 formulas, 14 canonical parameters, `D-178`–`D-187` / `DD-226`–`DD-235` and 20 `INT-` contracts — unchanged.
- **Open decisions:** `UD-017`, `UD-040`–`UD-051` and `UD-052`–`UD-060` remain Open or Deferred exactly as recorded; no owner-reserved decision was closed, no provisional requirement approved and no legal-dependent question resolved.
- **Prompt 12C:** not started, not authorized; no 12C deliverable, workflow, journey or acceptance artifact exists.
- **Security obligations, outstanding and unclaimed:** authenticated table-wide `UPDATE` on `feasibility.profiles` including `treasury`; missing corrective migration `0005`; missing SQL permission tests; missing protective audit-log trigger; unverified production tamper-evident audit implementation; unverified operating audit-digest job.
- **Progression:** the next development task requires separate owner authorization. No stage was initiated, selected or expanded by this record.

### 84.5 Documentation changed

| File | Change |
|---|---|
| `docs/stage-2/06_stage_2_progress_log.md` | This §84; the header `Last updated` record and prompt row 12 |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Prompt 12 row records the R8 deferral and cites §84 |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md` | R8-D current-status block added above the R7 block; the R7 block marked superseded; the `b12_fair_play:` status clause extended identically in all three files |
| `docs/ROADMAP.md`, `docs/stage-2/00_stage_2_handoff.md` | R8-D current-status block added; the R7 block marked superseded; the Stage 2 handoff's next-action paragraph records the deferral |

No validator file, fixture registry, formula, requirement, acceptance gate, rulebook, formula register or prompt archive was modified.

### 84.6 Validation actually run (2026-11-10)

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 87/87 passed; 0 failed` | 0 |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | `POSITIVE FIXTURES: 59/59 accepted`; `NEGATIVE FIXTURES: 153/153 rejected for the expected reason`; `CHECKS: 87/87 passed; 0 failed` | 0 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed` — `ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/validate_links.py` | `Links checked locally: 3415`; `External links skipped: 382`; `Anchors checked: 29`; `Unresolved: 0` | 0 |
| `sha256sum docs/qa_backups/12B_validate_b12.py` before and after the pass | `854549b9928ffa7618c680b1be4c932641bbf6648352445fcdaafdff6cbb8ea3` in both readings — the validator file is byte-identical, so no validator implementation was modified | — |

These runs verify document consistency and continuity only. They do **not** execute any R8 audit case, do not test the five residual weaknesses and are **not** independent acceptance; that is exactly why R7's 87/87 does not contradict the audit's five bypass classes.

### 84.7 Git state (read-only inspection, nothing modified)

Branch `main`, HEAD `bdbdd14` ("Initial complete Nation Supremacy project snapshot"). The working tree still carries the owner's prior unmerged index state — **20 `UU` and 4 `DU` entries, the same 24 unmerged entries observed by R6 and R7** — plus seven untracked artifacts created by earlier prompts and one pre-existing modification to `docs/qa_backups/10B_validate_warfare.py`. Nothing was staged, committed, pushed, merged, rebased, reset, checked out, stashed or resolved; `git status` was inspected read-only and the index left exactly as found. The R8-D edits touch only files already inside the unmerged set.

**Verdict.** **Prompt 12B-C1-R8-D is COMPLETE as a governance record.** R7's implementation is retained at 87/87 checks, 59/59 positive and 153/153 negative fixtures with the 23/23 subprocess mutation audit, while its independent acceptance is **NOT ACCEPTED**; the eight R6 reproductions remain rejected; the five bypass classes reported by the independent audit of `Project X (77)` are preserved as known residual weaknesses and are not corrected; **R8 is DEFERRED BY OWNER** with reopening only on explicit owner authorization; **12B-C1 remains NOT CLOSED**; the three PARTIAL gates, every owner-reserved decision and every security obligation are unchanged; **Prompt 12C is not authorized**; no validator code was modified; and no R8 correction was performed.

**Verdict.** **Prompt 12B-C1-R7 is COMPLETE at the implementation and documentation level.** The eight reproduced bypasses are rejected by the complete production validator for their intended reasons, in-process through the fixture registry and again as a subprocess against isolated file copies; the AI_CONTEXT B-12 entry, the acceptance document and the canonical register are parsed structurally; every relevant identifier occurrence is accounted for with provenance and classification; historical classification cannot disguise a present-state assertion; ambiguous authoritative records fail closed; legitimate historical, superseded and explanatory content still passes; the canonical register is the sole source of truth for the derived collection; and all R1–R6 protections and fixtures remain operational. What R7 does **not** establish: independent audit acceptance (pending — the owner must supply the next ZIP together with this archived R7 instruction), any runtime, database, security or legal verification, and any authorization to begin Prompt 12C.

## 85. Prompt 12C — fair-play operational workflows, cross-system integration, edge cases and acceptance (2026-11-10)

### 85.1 Authority and inputs

Executed under the owner's Prompt 12C instruction supplied in the working session. **It is deliberately not archived in `docs/prompts/` in this pass:** its bytes could not be verified against the supplied text here, and an unverifiable file presented as a verbatim archive would be a false provenance record. Its authorized scope and prohibitions are restated in §85.2–§85.4 and are enforced by validator checks `12C-17`–`12C-21`; a later pass may archive it with a recorded SHA-256 under the [`docs/prompts/INDEX.md`](../prompts/INDEX.md) convention. [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) was read in full before this work began, including §2 categories A–D, §4 priorities, §5 "what approved means", §6 stopping conditions and §8 change control; **D-014 is preserved unchanged.** Authoritative inputs: the four 12B canonical documents (`REQ-764`…`REQ-869`, 344 rules, 16 formulas, 14 parameters, 26 gates), the three 12A research registers (106 `12A-CR` candidates, 30 `12A-INT` dependencies, 32 `12A-RK` threats, 15 `12A-FR` postures, 15 `12A-OPEN` questions, 32 `12A-DR` recommendations, 11 categories, 40 benchmarks, 18 comparators, 22 gates at 15 PASS / 7 PARTIAL) and the Prompt 11C companion (25 journeys, 50 workflows, 84 edge cases, 17 `WPC-` contracts, 272 tests, 30 threats, 20 gates). The live project directory was the working tree throughout; no uploaded audit snapshot was used as a working directory.

### 85.2 Deliverables

| File | Owns | Volume |
|---|---|---|
| [`20_fair_play_and_player_protection_workflows.md`](20_fair_play_and_player_protection_workflows.md) | `FPJ-` journeys, `FPW-` workflow library, schemas, terminology and the journey-to-workflow map | 10 journeys `FPJ-001`…`FPJ-010`; 52 workflows `FPW-001`…`FPW-052` in 13 families, each a twelve-field record |
| [`20_fair_play_and_player_protection_integration.md`](20_fair_play_and_player_protection_integration.md) | the cross-system integration matrix, the nine system consistency assessments, dependency preservation and the conflict/gap register | 20 `INT-` contracts in two matrix parts (15 operational fields), 12 consistency rules verified, 2 conflicts, 10 gaps `FPG-01`…`FPG-10`, all 30 `12A-INT-` rows consumed |
| [`20_fair_play_and_player_protection_edge_cases_acceptance.md`](20_fair_play_and_player_protection_edge_cases_acceptance.md) | `FPE-` edge cases, `FPA-` acceptance specifications, the traceability ledger, the `P12C-` gate register, decisions, unresolved issues and the validator specification | 100 edge cases; 378 acceptance specifications (368 `SPECIFIED`, 10 `BLOCKED`, 0 executed); 106-row requirement ledger with 0 orphans; 20 gates at 15 PASS / 3 PARTIAL / 2 BLOCKED at the 12C close, reassessed to **16 PASS / 2 PARTIAL / 2 BLOCKED** by §86.5 on the repaired evidence |
| [`qa_backups/12C_validate_fair_play_workflows.py`](../qa_backups/12C_validate_fair_play_workflows.py) | independent structural, referential, traceability and governance checks over the 12C corpus | 24 checks `12C-01`…`12C-24`; 16 negative fixtures; exit codes 0/1/2 |

### 85.3 Coverage achieved

Workstream A translated the B-12 rules into 10 journeys and 52 workflows, each with a trigger, actors, systems, inputs, validation sequence, normal and alternative paths, failure behaviour drawn from the existing fifteen postures, resulting state, player experience, permitted administrative action, audit requirement, security and privacy constraints, traceability and tests. Workstreams B and D expanded all twenty `INT-` contracts to fifteen operational fields without adding a contract identifier, assessed market, diplomacy, alliances, warfare, world events, objectives, rankings, progression and shared infrastructure, and tested the twelve cross-system consistency rules. Workstream C added 100 `FPE-` cases while citing — never restating — the 84 existing `WEE-` rows. Workstream E produced 378 `FPA-` specifications across all eight classifications and fourteen mandatory coverage areas. Workstream F traced 106 of 106 requirements with zero orphans and stated a reason for the three requirements that are not workflow-shaped. Workstream G carried every outstanding security obligation into the affected workflows, contracts, edge cases and the `BLOCKED` test block. Workstream H recorded `D-188`…`D-197` / `DD-236`…`DD-245`, resolved no owner-reserved question, and answered `12A-OPEN-001`, `003`, `011`, `012` and `013` from existing rules while leaving the remaining ten open.

### 85.4 Explicitly not done

No gameplay code, production architecture, migration, grant, RLS policy, trigger, job or moderation feature was implemented. `12B_validate_b12.py` was not modified, no R8 correction work or R7 hardening was performed, the five R7 residual weaknesses remain known and unfixed, R8 remains deferred by the owner, 12B-C1 remains not closed, `P12B-14`/`P12B-16`/`P12B-23` and the seven 12A PARTIAL gates remain PARTIAL, no Open requirement was closed, no provisional parameter was promoted, no number was invented, and no Prompt 13, 14 or 15 work was started. No Git operation of any kind was performed: nothing was staged, committed, merged, reset, stashed or pushed, and the pre-existing committed merge-conflict markers were not resolved.

### 85.5 Validation actually run

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12C_validate_fair_play_workflows.py` | `CHECKS: 24/24 passed; 0 failed` — `RESULT: PASS at the documentation level` | 0 |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py --self-test` | positive baseline `24/24`; `NEGATIVE FIXTURES: 16/16 rejected for the expected reason` | 0 |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` across all scanned markdown files | 0 |
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 86/87 passed; 1 failed` — `12B-78` fails because `AI_CONTEXT` carries two conflicting `b12_fair_play` status entries from the pre-existing committed merge markers | 1 |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS` — 11C's own artefacts remain internally consistent with B-11 | 0 |
| `python docs/qa_backups/11B_validate_b11.py` | exit 0, documentary gate grading unchanged | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — check 29 ("no global REQ ID allocated by 11A, max stays `REQ-703`") fails because the canonical ledger now ends at `REQ-869`; this is the recorded pre-existing legacy debt `D-1`, and it failed before this pass for the same reason | 1 |
| `python docs/qa_backups/12A_validate_foundations.py`, `validate_final.py`, `09_validate.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `10B_validate_warfare.py`, `test_decision_registers.py`, `test_next_action.py`, `status_rules.py`, `12A_sync_docs.py`, `verify_politics_numbers.py` | **could not run** — `SyntaxError: invalid decimal literal` (or `unmatched ')'`) at a committed conflict-marker line inside each script | 1 |

The two 12C failures found during this pass were real defects and were repaired in the documents, not in the checks: six journey records were missing a required field, and one contract reference was written as `INT-024` where the dependency identifier is `12A-INT-24`. Every remaining failure above is a pre-existing baseline condition, distinguished here from 12C work and not fixed under §17. **A documentation validator PASS is not runtime evidence:** no workflow, contract, edge case or acceptance specification has been executed.

### 85.6 Verdict and next action

**Verdict: COMPLETE WITH DOCUMENTED LIMITATIONS.** All authorized Prompt 12C workstreams are delivered at the specification level; the limitations are the twenty Open owner- and legal-dependent requirements, the two `BLOCKED` 12C gates that depend on outstanding Stage 5 security work, the two registered conflicts reserved to the owner, and the pre-existing repository conflict-marker defect that Prompt 12C §17 forbids repairing here.

**Next action (as recorded on 2026-11-10 at the close of Prompt 12C):** a separately authorized repository-hygiene pass to resolve the pre-existing committed merge-conflict markers in nine status or register documents and twelve QA scripts. *(That pass was then authorized and executed as Prompt 12C-FINAL-C1, recorded in §86; this §85 line is preserved as the Prompt 12C record.)* **Nothing else is authorized:** R8 remains DEFERRED BY OWNER, 12B-C1 remains NOT CLOSED, and Prompts 13–15 remain unauthorized and unstarted.

## 86. Prompt 12C-FINAL-C1 — controlled status reconciliation, conflict-marker remediation and final documentation acceptance (2026-11-10)

### 86.1 Authority and boundary

Executed under the owner's Prompt 12C-FINAL-C1 instruction as a **bounded repository-integrity and documentation-reconciliation task**, not as a repetition of Prompt 12C, not as a new design stage, and not as authorization for any gameplay, security, moderation or database implementation. [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (`D-014`) was read in full again before any change; the owner confirmed that commits `2537606` and `94f5ec4` are owner-made and authorized, so the earlier Git-governance concern is closed and neither commit was altered. All Prompt 12C substantive deliverables were preserved: 10 journeys, 52 workflows, 20 reused contracts, 30 dependencies, 100 edge cases, 378 acceptance specifications, 106/106 requirements mapped and 0 orphans.

### 86.2 Forensic finding

117 line-anchored merge-conflict hunks were committed in **25 files** (14 Markdown, 11 Python), reproducing the Project X (79) audit inventory exactly. Git evidence: `94f5ec4` is a merge commit whose first parent `2537606` is the main line and whose second parent `4111120` is `review/12A`; the conflicted blobs are committed content, and the working index reports **zero** unmerged entries. `<<<<<<< HEAD` is therefore the main line and `>>>>>>> 4111120…` the 12A-era branch. Marker-looking byte sequences inside `prototypes/free-tier-feasibility/node_modules/` binaries were classified as coincidental and untouched. No legitimate documentation example, fixture or historical record uses a line-anchored triplet, so nothing that should have been preserved sat inside a hunk.

### 86.3 Resolution and verification

Every hunk was resolved to its HEAD side after verifying that this reproduces `2537606` exactly: at the moment of resolution 17 of the 25 files were byte-identical to `2537606` and in the remaining 8 the only differences were the seventeen status, version and tally lines that Prompt 12C and this pass deliberately rewrote, plus two blank lines. **Final measure after the whole reconciliation pass (reproduced by [the inventory](../qa_backups/12C_FINAL_C1_conflict_reconciliation.md) §10):** across the 26 tracked files this pass touched, `2537606` versus the working tree shows **11 files byte-identical, 0 main-line lines deleted anywhere and 56 lines rewritten** — every rewritten line is a current-status, version, tally or dated-annotation line, plus the two disclosed validator frontier snapshots of §86.4. Nothing from the authorized main line was dropped. Automatic union of both sides was rejected because it duplicates every `UD-052`–`UD-060` and `DD-226`–`DD-245` identifier and re-creates the contradictory current-status entries. Both sides stay retrievable at `2537606`, `4111120` and `94f5ec4`, and the complete per-file classification, impact, evidence and validation record is [`docs/qa_backups/12C_FINAL_C1_conflict_reconciliation.md`](../qa_backups/12C_FINAL_C1_conflict_reconciliation.md). **No Git write operation of any kind was performed** — nothing was staged, committed, pushed, reset, reverted, amended, merged, cleaned or stashed, and the pre-existing stash was left alone.

### 86.4 Status reconciliation and Python restoration

`AI_CONTEXT.md` now holds exactly **one** `b12_fair_play` entry and exactly one CURRENT B-12 status block; the `12B-C1-R8-D` block is relabelled as superseded **only as to Prompt 12C authorization**, with its R7, R8, 12B-C1, PARTIAL-gate and security-obligation wording intact. The machine status keys `status_updated` (2026-11-10), `decisions_range` (`D-001..D-197`) and `b12_fair_play` agree byte-for-byte across `AI_CONTEXT.md`, `AI_HANDOFF.md` and `PROJECT_PROGRESS.md`. Current-status lines in `ROADMAP.md`, `00`, `01`, `02`, `03`, `04`, `05` and this log were synchronized; dated blocks and log sections §1–§85 were preserved as history. **Verification classes, kept separate (corrected by Prompt 12C-FINAL-C1-R1).** **Syntax:** all 32 Python files under `docs/qa_backups/` parse (`ast.parse`, 0 failures), including all 11 previously affected scripts. **Functional execution:** recorded per command in §86.6 for the ten previously affected scripts that are checks or validators. The eleventh, `12A_sync_docs.py`, is a **one-shot bulk documentation-rewriting tool**: it was deliberately **not executed as part of this repair**, its functional behaviour is **not** claimed as verified, and every status edit in this pass was instead made by targeted, anchor-asserted edits so that each change stays reviewable. For completeness: it was invoked once by an automated whole-directory sweep at the close of FINAL-C1, and that invocation is evidence-verified to have **written nothing** — all 13 of its rewrite rules match **0** times across the seven surfaces it targets, and its status-blockquote insertion short-circuits because a `> **12A status (` block already exists in each of the five surfaces that receive it. `11C_sync_docs.py`, the same class of tool, aborted on its `docs/`-relative target paths before reaching any write. The post-sweep runs of `09_validate.py` (371/371) and `validate_final.py` (ALL CHECKS PASSED) independently confirm that neither tool reintroduced a superseded claim. Python syntax success is not functional-execution success and is not reported as such anywhere in this package. Two scripts needed disclosed frontier-snapshot refreshes (`09_validate.py`, `validate_final.py`) because their committed hard-coded register snapshots predated the Prompt 12C move of the register to `D-197` / `DD-245`; only the snapshot values and the spelled-number lookup table moved, no assertion was weakened, and `12B_validate_b12.py` is byte-unchanged.

### 86.5 Gate reassessment

`P12C-20` moves PARTIAL → **PASS** on recorded evidence, and the 12C tally recomputes to **16 PASS / 2 PARTIAL / 2 BLOCKED**. `P12C-09` and `P12C-10` stay PARTIAL on the two owner-reserved conflicts `C-01`/`C-02`; `P12C-17` and `P12C-18` stay BLOCKED pending Stage 5 work. `P12B-14`, `P12B-16` and `P12B-23` remain PARTIAL, the seven 12A PARTIAL gates and the 11C tally are unchanged, **12B-C1 remains NOT CLOSED**, R7 remains retained and not independently accepted with its five residual weaknesses unfixed, and R8 remains **DEFERRED BY OWNER**. Requirements stay 86 Provisional / 20 Open / 0 Approved / 0 Deferred. This pass mints no new decision identifier: `DECISIONS.md` stays at `D-001…D-197` and `04` at `DD-001…DD-245`, so nothing in the decision registers was added, removed, renumbered or status-changed; the resolution basis, the disclosed snapshot refreshes and the archival-provenance rule are recorded in this section and in [the reconciliation inventory](../qa_backups/12C_FINAL_C1_conflict_reconciliation.md).

### 86.6 Validation actually run

| Command | Actual result | Exit |
|---|---|---|
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 87/87 passed; 0 failed` — `12B-78` restored by the documentation repair; file byte-identical throughout | 0 |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py` | `CHECKS: 24/24 passed; 0 failed` | 0 |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py --self-test` | baseline `24/24`; `NEGATIVE FIXTURES: 16/16 rejected for the expected reason` | 0 |
| `python docs/qa_backups/validate_links.py` | `Markdown files scanned: 97`; `Links found: 3929`; `Links checked locally: 3547`; `External links skipped: 382` (skipped by design, not verified); `Anchors checked: 29`; `Unresolved: 0` | 0 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 44/45 passed; 1 failed` — `12A-31` accepts only the `D-001..D-177`/`D-001..D-187` frontier snapshots while the register now reads `D-001..D-197`; the script was **not** edited (see §86.7) | 1 |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed; ALL CHECKS PASSED` after artifact removal plus the two disclosed snapshot values in §86.4 | 0 |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS` | 0 |
| `python docs/qa_backups/11A_validate_research.py` | `30 executed, 1 failed` — pre-existing debt `D-1` | 1 |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests` — `OK` (0 failures). The test code was not changed: the Stage-2 progress rows it grades now carry the dated frontier wording, including the 2026-11-07 `Prompt 12C is next` snapshot quoted as superseded | 0 |
| `python docs/qa_backups/test_next_action.py` | `Ran 27 tests` — `OK` (0 failures), same reason; no assertion was edited | 0 |
| `python docs/qa_backups/11B_validate_b11.py`; `09A_validate_alliance.py`; `10B_validate_warfare.py`; `verify_politics_numbers.py`; `11C_validate_b11_workflows.py` | `all 52 gates PASS`; `Checks run: 943 … PASS`; `Checks run: 1036 … PASS`; `879/879 checks passed`; `RESULT: PASS` | 0 each |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[FAIL] 6 semantic defect(s)`, all `[C17]` register-snapshot assertions — exit 1 | **left unfixed deliberately**; see §86.7 |
| `python docs/qa_backups/12A_sync_docs.py` | **not executed as a repair step.** Its one incidental invocation inside the whole-directory script sweep exited 0 and wrote nothing: 0 matches for all 13 rewrite rules over the seven target surfaces and the `> **12A status (` guard already short-circuits on the five surfaces that receive the blockquote. **Syntax verified; functional behaviour NOT claimed** | n/a |
| `python docs/qa_backups/11C_sync_docs.py` | same sweep; aborted on its `docs/`-relative target paths before reaching any write | 1 (no writes) |
| `python docs/qa_backups/12B_validate_b12.py --self-test` | not re-run in this pass: the R7 record (§83) already documents its `23/23` subprocess mutation audit and this pass changed no R7 fixture or check | skipped by scope |
| `python -m unittest test_09A_alliance_validator` / `test_09B_alliance_semantic_validator` | **not executed in this pass** — §83 measured them at `43 tests, 1 failure` and `267 tests in 2912.5s, 3 failures`, all four being stale alliance-era fixtures outside this task's file scope; a single run costs ~49 minutes | skipped, with the reason recorded |

### 86.7 Residual validator frontier debt (recorded, deliberately not repaired)

Three phase validators fail only because their own hard-coded register snapshots predate registers that later passes moved legitimately. Each keeps its full detection power, and this pass left their source untouched — Task D forbids using syntax remediation as an opportunity to redesign validators, and Task §11 forbids altering validator logic to force passing results.

| Script | Result | Stale snapshot | What a future authorized pass must do |
|---|---|---|---|
| `12A_validate_foundations.py` | 44/45, exit 1 | check `12A-31` accepts `decisions_range` of `D-001..D-177` or `D-001..D-187`; the register is `D-001..D-197` | extend the accepted frontier set; add no new assertion |
| `09B_validate_alliance_semantic.py` | `[C17]` × 6, exit 1 | expects `D-001..D-187`, `DD-001..DD-235`, `Confirmed` 48 and tally total 235; the register is `D-001..D-197`, `DD-001..DD-245`, `Confirmed` 58, total 245 | refresh the four snapshot values only |
| `11A_validate_research.py` | 29 of 30, exit 1 | check 29 expects the `REQ-703` frontier; `REQ-869` is current | already recorded as project debt `D-1`; unchanged |

`09_validate.py` and `validate_final.py` carry the same class of snapshot and were refreshed here because they are the project-wide status validators that Task E's baseline restoration targets; the disclosure sits in §86.4 and in the reconciliation inventory §5. The asymmetry is intentional and is reported as a limitation, not hidden: two frontier snapshots moved, three were left failing with their reasons named.

### 86.8 Superseded wording inside the 12B canonical set, deliberately not edited

Two sentences in the B-12 specification described the pre-12C state as at this pass's close: **GOV-025** in [`20_fair_play_and_player_protection.md`](20_fair_play_and_player_protection.md) says "Prompt 12C is not started and not authorized", and the 12B acceptance companion's Prompt-12C handoff row says "12C is not authorized and its deliverables are prohibited". Both were true when written and both are now factually superseded.

They were **not** edited here for three reasons: `12B-C1` remains **NOT CLOSED**, so corrections to 12B canonical text belong to that open thread; Prompt 12C-FINAL-C1 §13 forbids using this pass to expand 12B work; and Task I forbids updating unrelated specifications. The repair a future 12B-facing pass should make is a wording change only — GOV-025's second sentence and the acceptance row's authorization clause — with no rule, requirement, formula, parameter, gate or status moved. The contradiction is therefore recorded rather than silently rewritten, and no 12C document relies on those two sentences: the 12C deliverables state their own authorization basis in §1 and §86.1.

**Superseded as to action, 2026-11-11 (Prompt 12C-FINAL-C2).** The owner then authorized exactly this narrow wording correction, and it was applied: GOV-025 and the acceptance companion's §7 row and §8 lead-in now separate the dated 12B baseline restriction — which is preserved verbatim as a labelled snapshot, including the original "not started and not authorized" sentence that `12B-58` continues to verify — from the current state, namely that Prompt 12C was subsequently authorized by the owner, its documentation deliverables are complete, and owner acceptance of that specification set remains pending. No rule, requirement, formula, parameter, gate status or decision identifier moved; `P12B-25`'s own gate row still grades only 12B's deliverables and was deliberately left as written.

**Verdict.** **Prompt 12C-FINAL-C1 is COMPLETE WITH DOCUMENTED LIMITATIONS.** The conflict-artifact, current-status and Python-parsing defects are resolved and evidenced; the remaining failures are stale unit-test and frontier expectations that predate this work, and correcting them would require altering assertions outside this bounded task. Nothing was implemented, executed or verified at runtime, and Prompt 13, 14 and 15 remain unauthorized and unstarted.

**Reporting correction (Prompt 12C-FINAL-C1-R1, 2026-11-11).** Two reporting inaccuracies in this section were corrected, with no remediation result altered and no new decision identifier created: (1) the `Last updated` header claimed the decision frontier moved to `D-200 / DD-248` with `D-198…D-200` and `DD-246…DD-248` recorded, which matched neither canonical register — the registers are and were `D-001…D-197` / `DD-001…DD-245`; (2) §86.4 and the header said all eleven restored QA scripts "run", while `12A_sync_docs.py` is a bulk documentation-rewriting tool verified by syntax only and never executed as a repair step. The syntax-versus-execution classes are now stated in §86.4, §86.6 and in the reconciliation inventory §5.1, and the inventory's earlier claim that the phantom-frontier grep was clean is corrected in §3.1.

**Next action:** the owner accepts or rejects the Prompt 12C specification set. No further repair, no R8 work and no later prompt is authorized by this pass.


---

## 87. Prompt 13A — UI research, architecture and design foundations (2026-11-11)

### 87.1 Authority and inputs

Executed under the owner's Prompt 13A instruction (2026-11-11), which also recorded the owner's **formal acceptance of Prompt 12C**. Read first: `AUTONOMOUS_DECISION_POLICY.md` (D-014, 121 lines), the three continuity STATUS blocks, the handoff, the roadmap and progress log, the registers at their 2026-11-10 state (D-197 / DD-245 / REQ-869 / UD-060), and all accepted 12A/12B/12C companions; the repository was verified live (`git status`: tree clean at `ec8662a` on 2026-11-11 before this pass wrote any file). The working directory is the live project; no ZIP snapshot was used.

### 87.2 Deliverables

| File | Owns | Volume |
|---|---|---|
| [`research/13A_politics_and_war_ui_research.md`](research/13A_politics_and_war_ui_research.md) | evidence classes, retrieval method, the P&W source register, supplementary register, boundary rows, findings, benchmark patterns, recommendations, limitations | 36 dated source rows (33 P&W incl. the 2026-11-11 live public-interface retrieval; 2 supplementary; 1 negative); 40 findings; 28 retain/adapt/reject patterns; 24 recommendations |
| [`research/13A_ui_design_principles_and_architecture.md`](research/13A_ui_design_principles_and_architecture.md) | design principles, visual-direction evaluation, application shell, navigation model, application states | 16 principles; four evaluated visual directions with a reasoned recommendation (brand values untouched); eight-section navigation; 13 application states |
| [`research/13A_master_screen_inventory.md`](research/13A_master_screen_inventory.md) | the screen register, category detail records, hierarchy, transitions, overlay register, quality audit | `SCR-001…SCR-100` (85 Mandatory + 4 Conditional + 1 Provisional player-facing; 10 administrative); mermaid hierarchy; 7-risk navigation audit; `OVL-01…08` |
| [`research/13A_responsive_and_design_system_foundations.md`](research/13A_responsive_and_design_system_foundations.md) | responsive philosophy and design-system foundations | `13A-RD-01…08`; `13A-DS-01…15`; state matrix; chart-integrity rules; accessibility foundations; provisional breakpoints labelled |
| [`research/13A_ui_requirements_open_questions_and_acceptance.md`](research/13A_ui_requirements_open_questions_and_acceptance.md) | UI candidate requirements, dependency map, open questions, acceptance gates, preservation checklist, validation record | `13A-UR-001…048` in two parts; `13A-OQ-001…016`; 24 `P13A` gates at **23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED** |
| [`prompts/prompt_13A_ui_research_architecture_and_design_foundations.md`](../prompts/prompt_13A_ui_research_architecture_and_design_foundations.md) | the archived owner instruction, with its provenance paragraph and the digest recorded in [`prompts/INDEX.md`](../prompts/INDEX.md) | 38,594 bytes; 1,383 LF and 0 CRLF newlines; SHA-256 `c8add1081c9b31a57b07de1c31eac4de7f9529ce203112d5bb4a92a2dcc84c99` over the stored bytes (the recovered instruction itself hashes to `1a55aee6d6be92f3e6d7952daa43192db3d683972fedde6d4b8ee6890f50c61e`) |

### 87.3 Decisions

**D-198** 13A/13B split; B-13 serial realignment to `21_interface_and_player_journeys.md` with B-14/B-15/B-18/B-19 planned names shifted to `22_`/`23_`/`24_`; **D-199** evidence-class discipline for the P&W benchmark; **D-200** `SCR-` identifier family and inventory classes; **D-201** persistent-shell and eight-section navigation position; **D-202** responsive position with provisional breakpoint values; **D-203** design-system position with brand values held owner-reserved; **D-204** no global `REQ-`/`UD-` allocation, `REQ-870` reserved for 13B; **D-205** P13A gate separation and the focused validator instead of further R7-family hardening. Mirrored as **DD-246…DD-253**. No owner-reserved decision was resolved and no earlier decision was amended.

### 87.4 Research boundaries recorded honestly

The authenticated P&W surfaces (the actual nation console, market UI, notifications, alliance interiors, war-timeline bodies) were **not observable** without login; no account was created and no access control was circumvented. Those areas are registered as `NOT-RETRIEVABLE` rows with their documented/secondary sources named (`13A-SRC-009/024/025/026/027`, §5 boundaries 032–036, and the in-repo 11A/10A/09A/07A registers as `SECONDARY`). NationStates and the fandom wiki returned HTTP 403 to the fetcher. Single-day retrieval; P&W changes continuously.

### 87.5 Validation actually run

The pass executed across the 2026-11-11/2026-11-12 boundary: the research, the five deliverables, the decisions and the synchronization are recorded as the 2026-11-11 Prompt 13A record, and this final validation sweep completed on 2026-11-12. Every number below is copied from the console output of the command named, not from a register.

| Command actually run | Result as printed |
|---|---|
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` (exit 0) |
| `python docs/qa_backups/validate_links.py` | 103 Markdown files, 4,035 links, 3,653 checked locally, 382 external skipped, 29 anchors, **Unresolved: 0** |
| `python docs/qa_backups/test_next_action.py` | `Ran 27 tests … OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests … OK` |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed` |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943` — `PASS: all Alliance integration, source, permission and handoff checks` |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed with no review findings` |
| `python docs/qa_backups/test_09A_alliance_validator.py` | `Ran 43 tests … OK` |
| `python docs/qa_backups/test_09B_alliance_semantic_validator.py` | **2026-11-11 Prompt 13A execution record (corrected 2026-11-12 by Prompt 13A-C1 §88):** the initial full-suite run on the tree returned `Ran 267 tests in 2268.523s` — `FAILED (failures=3)` (`test_49`, `test_54`, `test_59`); those three stale fixtures were diagnosed and repaired with dated comments and individually re-verified standalone (`Ran 3 tests … OK`); **no full 267-test rerun was completed or logged during the 2026-11-11 Prompt 13A session** (the earlier text claiming "the repeat of the whole suite is recorded in the closing line of this section" was erroneous and removed by 13A-C1). Separate 34-check `09B_validate_alliance_semantic.py` passed (`[PASS] All 34 semantic checks passed with no review findings`). Post-repair full-suite execution on the 13A-C1 tree is recorded separately in **§88**. |
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 1036`; `Negative fixtures: 73/73 rejected`; CF-01 and CF-02 PASS; `PASS: all B-10 structure, disposition, formula, register and boundary checks` |
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — check 29 (`no global REQ ID allocated by 11A (max stays REQ-703)`) fails; recorded debt, untouched, see below |
| `python docs/qa_backups/11B_validate_b11.py` | `CLOSEOUT ELIGIBILITY: all 52 gates PASS` — `RESULT: PASS` |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS — 11C workflows, integration and acceptance documents are internally consistent with the B-11 sources at the documentation level` |
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 45/45 passed; 0 failed`; register line `D=205 DD=253 UD=60 REQ max=869` |
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 87/87 passed; 0 failed` |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py` | `CHECKS: 24/24 passed; 0 failed` — `RESULT: PASS at the documentation level` |
| `python docs/qa_backups/13A_validate_ui_foundations.py` | `CHECKS: 32/32 passed; 0 failed` |
| `python docs/qa_backups/13A_validate_ui_foundations.py --self-test` | `SELF-TEST: 14/14 seeded defects detected` |
| `verify_alliance_numbers.py` / `verify_alliance_workflows.py` | `375 passed, 0 failed`; `ALL CHECKS PASSED` |
| `verify_diplomacy_numbers.py` / `verify_diplomacy_workflows.py` | `9 groups checked … 0 failed`; `17 groups checked … 0 failed` |
| `verify_economy_numbers.py` / `verify_city_numbers.py` | `164/164`; `267/267` |
| `verify_market_numbers.py` / `verify_market_workflows.py` | `MARKET VALIDATION: ALL CHECKS PASSED`; `07C VALIDATION: ALL CHECKS PASSED` |
| `verify_politics_numbers.py` | `POLITICS NUMBERS: 879/879 checks passed` |
| `verify_warfare_workflows.py` | `CHECKS: 49 EXECUTED: 49 FAILED: 0` |

**Validator expectations that this pass advanced, and why.** The frontier constants in the checkers were moved to the values this pass created, each with a dated comment, and no check was loosened, deleted or inverted: `status_rules.py` (`CURRENT_SUBPROMPT` → `13B`, `12C` and `13A` added to the completed set, the sub-prompt token range extended to the `13` family — without it `13A` was not a recognised sub-prompt token at all), `validate_final.py` (`stage_2_next_prompt` → `13B`, DD contiguity 245 → 253, progress-log pending rows 3 → 2, log rows 10 and 12 now require the 12C completion and `Prompt 13B next`, AI_CONTEXT row-04 totals `D-205`/`DD-253`, the outline mapping to the D-198 serial names, and the spelled-count map gaining `two hundred and five`), `test_next_action.py` (live value `13B`; rows 14–15 are the only bare `Pending` rows; row 13 is now read itself; the `12C is next` fixture became a stale-claim case and `13B` became the live case), `test_decision_registers.py` (same two frontier readings), `12A_validate_foundations.py` check 31 (`13` family and `D-001..D-205`), `10B_validate_warfare.py` (`CURRENT_SUBPROMPT` milestone), `09_validate.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py` (C17 register frontiers `D-205`/`DD-253`/Confirmed 66/total 253 and the C18 live-prompt pattern; the `D-204` guard is now scoped to the D-106 row it protects, because `D-204` is a real decision from this pass onward), `verify_politics_numbers.py` (row 10 names `13B`) and `test_09A_alliance_validator.py` (fixture 40 now mutates the live `13B` value). None of these edits changes a rule, a gate verdict, a fixture count or a protected status; each only moves a recorded milestone to the value the record now holds.

**Three stale 09B regression fixtures, diagnosed and repaired.** `test_49` set `REQ-591`'s status cell to `**Provisional**`, which has been that row's real value since Prompt 10B, so the mutation was a no-op and check C16 could not fire; it now reverts the row to `Deferred`, the regression the check exists to catch. `test_54` compared against the C17 frontier label as at D-142 while the register has run past D-187 and D-197 for a long time; the needle now names the current label and the proved defect (a gap in the decision sequence must be reported) is unchanged. `test_59` mutated `stage_2_next_prompt: 12B`, a value the tree stopped carrying when 12C closed, so again the mutation never applied; it now mutates the live `13B` value and still expects rejection of a closed prompt. None of the three masked a Phase-09B rule, contract, register row or status: the 09B validator itself reports `[PASS] All 34 semantic checks passed with no review findings` on this tree.

**Debt this pass did not repair, reported rather than hidden.** `11A_validate_research.py` check 29 still asserts `REQ-703` as the global maximum. Prompt 11B allocated `REQ-704`…`REQ-763` and Prompt 12B allocated `REQ-764`…`REQ-869`, so the check has been failing since 2026-11-07 and was explicitly recorded as debt in the 12A report §32; 13A left it untouched, and its failure does not indicate a 13A defect — 13A allocated no global `REQ-` row and the tracker still ends at `REQ-869`. `validate_final.py`'s pre-Prompt-12 assertions are likewise unchanged, as 12A recorded.

**Known validator limitation encountered, reported per instruction §20.** The 12A checker's `12A-31` continuity rule hard-codes the *family prefix* rather than reading the live value, so it had to be advanced with the frontier even though its substance (three STATUS blocks must agree) is unchanged; that is a limitation of the check, not of the documentation set. The 09B C17 whole-file `D-204` substring guard was the same class of limitation and is now scoped to the row it protects.


### 87.6 Verification commands

```
python docs/qa_backups/validate_final.py
python docs/qa_backups/validate_links.py
python docs/qa_backups/test_next_action.py
python docs/qa_backups/test_decision_registers.py
python docs/qa_backups/12B_validate_b12.py
python docs/qa_backups/12C_validate_fair_play_workflows.py
python docs/qa_backups/12A_validate_foundations.py
python docs/qa_backups/13A_validate_ui_foundations.py
python docs/qa_backups/13A_validate_ui_foundations.py --self-test
python docs/qa_backups/09_validate.py
python docs/qa_backups/09A_validate_alliance.py
python docs/qa_backups/09B_validate_alliance_semantic.py
python docs/qa_backups/test_09A_alliance_validator.py
python docs/qa_backups/test_09B_alliance_semantic_validator.py
python docs/qa_backups/10B_validate_warfare.py
python docs/qa_backups/11A_validate_research.py
python docs/qa_backups/11B_validate_b11.py
python docs/qa_backups/11C_validate_b11_workflows.py
python docs/qa_backups/verify_politics_numbers.py
```

### 87.7 Status after this checkpoint

**Prompt 13A: COMPLETE WITH DOCUMENTED LIMITATIONS at the research/design-foundations level** (P13A-10 PARTIAL: inventory fields compressed in places; 13B must expand). Owner acceptance is pending; **Prompt 13B is next, not started and not authorized (D-002)**; Prompt 12A's seven PARTIAL gates, Prompt 12B's three PARTIAL gates, 12B-C1 NOT CLOSED, R7 non-acceptance with five known weaknesses, the owner's R8 deferral, Prompt 12C's accepted 16/2/2 close, and every outstanding security obligation are unchanged. No gameplay code, screen, component, framework, migration, deployment or runtime test exists; nothing was executed. The next action is the owner's review of this package.

---

## 88. Prompt 13A-C1 — Semantic Cross-Reference, Research-Evidence, Validator and QA-Reporting Reconciliation (2026-11-12)

### 88.1 Authorization and scope boundaries

Executed the strictly bounded Prompt 13A-C1 correction pass on the existing live repository (`HEAD=5406c1f` plus working-tree reconciliation) against the Project X (83) independent audit findings without restarting research, redesigning the UI architecture, adding screens or modifying historical owner-authorized commits (`2537606`, `94f5ec4`). Re-read `AUTONOMOUS_DECISION_POLICY.md` (D-014) prior to edits; preserved every protected status (12A seven PARTIAL gates, 12B `P12B-14/16/23` PARTIAL, 12C owner-accepted `16 PASS / 2 PARTIAL / 2 BLOCKED` with 378 unexecuted `FPA-` specs, `12B-C1` NOT CLOSED, `R7` NOT ACCEPTED with five known weaknesses, `R8` DEFERRED BY OWNER, all Supabase `0005` / `audit` trigger / `tests/sql` obligations, `Prompt 13B` unauthorized and unstarted, `D-001..D-205`, `DD-001..DD-253`, `REQ-001..REQ-869`, `UD-001..UD-060`).

### 88.2 Semantic cross-reference & Politics & War evidence reconciliation

1. **Research register ([`13A_politics_and_war_ui_research.md`](research/13A_politics_and_war_ui_research.md)):** Reconciled `13A-FND-026` (explicitly bounded to the logged-out public catalogue boundary and `NOT-RETRIEVABLE` authenticated Home row `13A-SRC-032`), `13A-FND-031` (records that fetched P&W Alliance/Nation tables expose both `Alliance` and `Color` text columns across `13A-SRC-002/005/007`, while visual CSS swatch redundancy remains unverified in static HTML fetches), and `13A-FND-032` (restricted to unauthenticated GET HTML shell fallback on `13A-SRC-009/025` plus `13A-SRC-032`, removing any claim that P&W hides authenticated action failures). Reconciled dependent `13A-BP-015/018/021`, `13A-DR-001/015/018/021` (removing stray `13A-BP-017` Discord citation from `13A-DR-021` in favor of `WAR-149`, `ALL-161/167/168`, roadmap B-09 paragraph and `13A-FND-010/012`), and §10.1 evidence summary (`21 OBSERVED` — 20 strictly OBSERVED plus `13A-SRC-028` hybrid OBSERVED + DOCUMENTED — `2 DOCUMENTED`, `5 NOT-RETRIEVABLE`).
2. **UI architecture ([`13A_ui_design_principles_and_architecture.md`](research/13A_ui_design_principles_and_architecture.md)):** Reconciled mismatched citations across `13A-PR-02/04/05/09/10/12`, §3.2 `suppressed` (`13A-DR-006` instead of `13A-DR-005`), §4 shell frame/bullets (`13A-BP-001`/`13A-SRC-017`, `13A-DR-009/010`, `13A-DR-011`, `13A-DR-013`, `13A-FND-026/027`), §5.2 Inbox (`13A-DR-001` instead of `13A-DR-003`), §6 Empty/Blocked states, and §7 boundaries.
3. **Master screen inventory ([`13A_master_screen_inventory.md`](research/13A_master_screen_inventory.md)):** Reconciled §1.3–1.4, table rows `SCR-002` (`13A-BP-014`), `SCR-008` (`13A-BP-001`, `13A-SRC-017`), `SCR-014` (`13A-DR-001`, `13A-BP-018`), `SCR-017` (`13A-BP-024`, `13A-DR-020`), `SCR-018` (`13A-BP-006`, `13A-BP-016`, `13A-DR-003`), `SCR-024` (`13A-BP-010`, `13A-DR-009`), `SCR-029` (`13A-BP-026`), `SCR-056` (`13A-SRC-021`, `13A-DR-022`), `SCR-062` (`13A-BP-008`, `13A-DR-008`), `SCR-072` (`13A-BP-005`, `13A-BP-020`, `13A-DR-007`), `SCR-078` (`13A-BP-009`, `13A-DR-010`), `SCR-088` (`13A-BP-012`, `13A-DR-014`; invalid `035` pattern suffix removed), §3 screen detail notes, and §5 audit (`13A-DR-009/010`, `13A-UR-044`).
4. **Responsive & design-system foundations ([`13A_responsive_and_design_system_foundations.md`](research/13A_responsive_and_design_system_foundations.md)):** Reconciled §1.2 (`13A-FND-003/027`), §2.3 (`13A-BP-026`, `13A-BP-010`, `13A-DR-009`), §2.6 (`13A-DR-020` for historical retention; `13A-DR-006`/`13A-DR-020`/`13A-BP-020` for comparisons), `13A-DS-07` (`13A-FND-013/028`), and `13A-DS-10` (`13A-FND-017/031` bounded wording + `13A-DR-015`).
5. **UI requirements, decisions & acceptance ([`13A_ui_requirements_open_questions_and_acceptance.md`](research/13A_ui_requirements_open_questions_and_acceptance.md), [`../DECISIONS.md`](../DECISIONS.md)):** Audited all 48 `13A-UR` rows, reconciled 27 rows (`UR-003`..`UR-046`) and `§2.2` `UR-044` with explicit `13A-` prefixes and verified B-system dependencies, and reconciled `D-201`–`D-203` in `DECISIONS.md` (preserving `2026-11-11` creation dates with dated `2026-11-12` reconciliation notes). Reassessed `P13A-02/03/10/19/20/21/22/24`, **preserved `P13A-10` as PARTIAL** (`23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED`), and recorded explicitly that **Prompt 13A has NOT received owner acceptance**.

### 88.3 Validator upgrade, CRLF verification & QA execution record

- **Validator upgrade ([`13A_validate_ui_foundations.py`](../qa_backups/13A_validate_ui_foundations.py)):** Expanded from 32 checks / 14 self-tests to **34 checks / 29 self-tests**, adding `13A-33` (`c33_semantic_cross_refs` enforcing `SEMANTIC_CROSS_REFS` topic-to-citation bindings and `UR` system tokens), `13A-34` (`c34_research_evidence_alignment`), `13A-04` unsupported-suffix and wrong-family rejection, and `13A-24` compound/range/shorthand citation expansion + `D-198..D-205` / `DD-246..DD-253` checking.
- **Line-ending inspection (Task 5):** Verified live Git history at `HEAD=5406c1f` vs pre-13A baseline `ec8662a`: `5406c1f` already eliminated CRLF-only drift (0 CRLF-only files in diff, 24 substantive modifications + 7 new files), and the live working tree had zero pre-13A-C1 uncommitted edits or CRLF-only changes; no mass normalization of unrelated tracked files was required or performed.
- **QA & `09B` execution record:** Post-edit verification executed across the complete untouched tree covers `py_compile`, `13A_validate_ui_foundations.py` (`34/34` checks; `--self-test` `29/29`), `validate_final.py`, `validate_links.py` (`Unresolved: 0`), `test_next_action.py` (`27/27`), `test_decision_registers.py` (`12/12`), `09_validate.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py` (`34/34`), `test_09A_alliance_validator.py` (`43/43`), `10B_validate_warfare.py`, `11A_validate_research.py` (historical `REQ-703` check-29 debt `FAILED: 1`), `11B_validate_b11.py`, `11C_validate_b11_workflows.py`, `12A_validate_foundations.py` (`45/45`), `12B_validate_b12.py` (`87/87`), `12C_validate_fair_play_workflows.py` (`24/24`), and `verify_politics_numbers.py` (`879/879`). For `test_09B_alliance_semantic_validator.py`, only the three continuity-sensitive tests (`test_49_req591_deferral_removed_fails`, `test_54_missing_decision_fails`, `test_59_next_prompt_changed_fails`) were executed during Prompt 13A-C1 (`Ran 3 tests … OK`); the full 267-test `test_09B` suite was **not** rerun under Prompt 13A or 13A-C1 (3 sequential tests take ~43s) and is reported accurately without extrapolation alongside the updated §87.5 record. **Prompt 13A has not received independent owner acceptance, `P13A-10` remains `PARTIAL`, and Prompt 13B remains unauthorized and unstarted.**

---

## 89. Prompt 13A-C1-R1 — Accessibility Evidence Reconciliation, Strict Claim Allowlists & Status Synchronization (2026-11-12)

### 89.1 Scope & Governance Boundaries

Executed the narrowly scoped final **Prompt 13A-C1-R1** reconciliation pass against the independent **Project X (84)** audit baseline without restarting Prompt 13A research, redesigning the UI architecture, running any mutating Git command, or touching historical owner-authorized commits (`2537606`, `94f5ec4`). Re-read [`AUTONOMOUS_DECISION_POLICY.md`](../AUTONOMOUS_DECISION_POLICY.md) (**D-014**); preserved all protected historical statuses (`12A` 7 PARTIAL, `12B` `P12B-14/16/23` PARTIAL, `12B-C1` NOT CLOSED, `R7` retained / NOT ACCEPTED with 5 weaknesses, `R8` DEFERRED BY OWNER, `12C` owner-accepted `16 PASS / 2 PARTIAL / 2 BLOCKED` with 378 unexecuted `FPA-` specs, all Supabase `0005` / audit-trigger / `tests/sql` obligations, `P13A-10` **PARTIAL**, Prompt 13A owner acceptance **PENDING**, and Prompt 13B **unauthorized and unstarted**).

### 89.2 Task-by-Task Corrections

1. **Task 1 — `UR-010` & `13A-DS-07` accessibility evidence ([`13A_ui_requirements_open_questions_and_acceptance.md`](research/13A_ui_requirements_open_questions_and_acceptance.md), [`13A_responsive_and_design_system_foundations.md`](research/13A_responsive_and_design_system_foundations.md)):** Removed inappropriate Politics & War API/export citations (`13A-FND-013`, `13A-FND-028`) from both records while keeping keyboard-accessibility, visible-focus, and WCAG 2.2 AA design-intent requirements intact; explicitly classified both as `INDEPENDENT_ACCESSIBILITY_REQUIREMENT` grounded in `13A-PR-14`, `DMP-164`, and `REQ-321` without fabricating observed P&W keyboard evidence.
2. **Task 2 — Strict claim-level citation allowlist validation ([`13A_validate_ui_foundations.py`](../qa_backups/13A_validate_ui_foundations.py)):** Replaced partial required/forbidden-only checks with strict `CLAIM_ALLOWLISTS` (`_claim(...)` records per family covering `doc1` FND/DR rows, `doc2`, `doc3`, `doc4`, `doc5`, and `D-201`–`D-203`) inside `c33_semantic_cross_refs` and `c34_research_evidence_alignment` so any extra/unpermitted citation on a claim fails deterministically while valid `INDEPENDENT_ACCESSIBILITY_REQUIREMENT` entries without P&W citations pass cleanly; added 16 targeted regression fixtures (`fx_c1r1_bp022_bypass_on_pr02` plus the 15 Project X (84) semantic/allowlist cases), expanding `--self-test` from **29** to **45** regression cases.
3. **Task 3 — Continuity `STATUS` synchronization ([`AI_CONTEXT.md`](../AI_CONTEXT.md), [`AI_HANDOFF.md`](../AI_HANDOFF.md), [`PROJECT_PROGRESS.md`](../PROJECT_PROGRESS.md), [`ROADMAP.md`](../ROADMAP.md), [`00_stage_2_handoff.md`](00_stage_2_handoff.md), [`01_stage_2_prompt_roadmap.md`](01_stage_2_prompt_roadmap.md)):** Verified exact `STATUS` keys in `AI_CONTEXT.md` (and mirrors): `politics:` held no `"Prompt 12B is next"` claim; `diplomacy:` carried `Prompt 12B is next` and `b11_progression:` carried `Prompt 12C is next and is not authorized to start`. Reconciled both `diplomacy:` and `b11_progression:` in `AI_CONTEXT.md`, `AI_HANDOFF.md`, and `PROJECT_PROGRESS.md` as clearly labelled historical baseline records superseded by accepted `12B`/`12C` and completed `13A` docs, updated `ui_foundations:` identically across all three continuity files, and kept `stage_2_next_prompt: 13B` and `Prompt 13A` owner acceptance **PENDING**.
4. **Task 4 — Line-ending provenance preservation:** Preserved existing working-tree CRLF/LF state untouched with zero bulk CRLF normalization and zero mutating Git commands (`add`, `commit`, `push`, `reset`, `revert`, `checkout`, `restore`, `merge`, `amend`). Project X (84) recorded 131 modified tracked files (`117` line-ending-only diffs of unverified provenance plus `14` substantive changes); provenance of historical line-ending differences cannot be conclusively established in the live workspace without modifying tracked files and is recorded transparently as a preserved limitation.
5. **Task 5 — Gate & QA reporting accuracy:** Kept `P13A-10` **PARTIAL** (`23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED`) and Prompt 13A owner acceptance **PENDING**; updated `P13A-03/16/19/20/21/22/24` notes and §7 execution records in `13A_ui_requirements_open_questions_and_acceptance.md` with post-final-edit outputs (`13A_validate_ui_foundations.py` `34/34` checks and `45/45` self-tests, plus explicit honest distinction for the 267-test `test_09B` suite and historical `11A_validate_research.py` `REQ-703` check-29 debt).

---

## 90. Prompt 13A-C1-R2 — Legacy Requirement Identifier Allowlist Completeness & Final Semantic Acceptance (2026-11-12)

### 90.1 Scope & Governance Boundaries

Executed the narrowly scoped **Prompt 13A-C1-R2** semantic-validator correction pass against the independent **Project X (85)** audit baseline without restarting Prompt 13A research, redesigning the UI architecture, running any mutating Git command, touching historical owner-authorized commits (`2537606`, `94f5ec4`), or performing bulk CRLF normalization on the preserved working-tree differences. Re-read [`AUTONOMOUS_DECISION_POLICY.md`](../AUTONOMOUS_DECISION_POLICY.md) (**D-014**); preserved all protected historical statuses (`12A` 7 PARTIAL, `12B` `P12B-14/16/23` PARTIAL, `12B-C1` NOT CLOSED, `R7` retained / NOT ACCEPTED with 5 weaknesses, `R8` DEFERRED BY OWNER, `12C` owner-accepted `16 PASS / 2 PARTIAL / 2 BLOCKED` with 378 unexecuted `FPA-` specs, all Supabase `0005` / audit-trigger / `tests/sql` obligations, `P13A-10` **PARTIAL**, Prompt 13A owner acceptance **PENDING**, and Prompt 13B **unauthorized and unstarted**).

### 90.2 Legacy Identifier Namespace Discovery, Allowlist Completeness & Self-Test Expansion

1. **Task 1 — Complete legacy identifier discovery across all five Prompt 13A deliverables:** Audited every legacy/project identifier family referenced across `docs/stage-2/research/13A_*.md`, discovering and verifying all 40 Stage-1/Stage-2/bible-outline legacy prefixes (`F-PD`, `TR`, `ACC`, `NAT`, `NET`, `ONB`, `RRL`, `ECN`, `URB`, `DMP`, `MKT`, `DIP`, `DPE`, `ALL`, `AX`, `AN`, `WAR`, `WEP`, `WPC`, `ADM`, `EVD`, `FP`, `FR`, `MOD`, `PRV`, `SEC`, `V`, `B`, `FO`, `CX`, `AP`, `UXD`, `DP`, `SYS`, `SIM`, `ECON`, `ECV`, `F`, `G`, `R`) plus `REQ`, `D`, and `UD` against their canonical register definitions on disk (3,197 dynamic canonical legacy IDs plus `REQ-001..REQ-869`, `D-001..D-205`, and `UD-001..UD-060`).
2. **Task 2 — Strict legacy-namespace & `§2.2` allowlist enforcement ([`13A_validate_ui_foundations.py`](../qa_backups/13A_validate_ui_foundations.py)):** Added dynamic canonical legacy discovery (`LEGACY_REGISTER_SPECS`, `_load_legacy_universe`), unified compound/slash/range/ellipsis/en-dash expansion (`_expand_prefixed_tokens`) across legacy, `REQ-`, and `D-/UD-` citations, unsupported legacy-suffix rejection in `13A-04` (`DMP-164x`), list-adjacent duplicate citation detection (`_find_list_duplicate_citations`), and full per-claim `allow_legacy` + `allow_deps` + `§2.2` ledger enforcement across all five 13A deliverables (`13A-FND-*`, `13A-BP-*`, `13A-DR-*`, `13A-PR-*`, `SCR-001..100`, `OVL-01..08`, `13A-RD-02..08`, `13A-DS-01..15`, `UR-001..048` in both `§2.1` and `§2.2`) and `D-198..D-205`. Unrelated canonical legacy citations such as `DMP-268`, `WAR-148`, `ALL-161`, and `AX-18` on `UR-010` or `13A-DS-07` fail deterministically under `13A-33`, while valid `DMP-164` + `REQ-321` independent accessibility dependencies remain accepted under `INDEPENDENT_ACCESSIBILITY_REQUIREMENT` (with P&W research citations forbidden).
3. **Task 3 — Regression test expansion:** Preserved all 45 existing `--self-test` fixtures and added 21 targeted legacy-allowlist, compound/range parser, duplicate-citation, positive-control, and accessibility-dependency regression fixtures (`66/66` passing). Disclosed non-NLP parser boundaries cleanly in `13A_ui_requirements_open_questions_and_acceptance.md` §7 while keeping `P13A-10` **PARTIAL** (`23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED`) and Prompt 13A owner acceptance **PENDING**.

---

## 91. Prompt 13B — complete screen and component specifications (2026-11-13)

### 91.1 Authorization and scope boundaries

Executed Prompt 13B against the live repository at the owner's explicit authorization, which also records **Prompt 13A as OWNER ACCEPTED / COMPLETED**. Re-read `AUTONOMOUS_DECISION_POLICY.md` (D-014) and the five accepted 13A deliverables before writing. The pass is documentation only: no frontend code, screen, component, route, migration, authentication change, gameplay rule, formula, parameter or numeric value was created or modified. Prompt 13C, Prompt 13D, Prompt 14 and Prompt 15 were not started. Every protected historical status was preserved: 12A's seven PARTIAL gates, 12B's `P12B-14/16/23` PARTIAL gates, 12B-C1 NOT CLOSED, R7 not independently accepted with five known weaknesses, R8 DEFERRED BY OWNER (not reopened), Prompt 12C OWNER ACCEPTED (16 PASS / 2 PARTIAL / 2 BLOCKED), the 378 unexecuted `FPA-` specifications, all outstanding Supabase/audit/security obligations, and `UD-017` / `UD-040`…`UD-060`.

### 91.2 Deliverables

The canonical B-13 family is three files under the D-198 `21_` serial: [`21_interface_and_player_journeys.md`](21_interface_and_player_journeys.md) (authority, methodology, navigation register, responsive/accessibility rules, map reconciliation, Matrices A–C, requirements, decisions, dependencies, documentation impact and 13C handoff), [`21_screen_specifications.md`](21_screen_specifications.md) (the complete A–K body of all 100 screens) and [`21_component_specifications.md`](21_component_specifications.md) (90 `UI-CMP` components and the eight `OVL` overlays).

### 91.3 Screen and component coverage

All **100** `SCR-` identifiers are accounted for with no duplicates or omissions: 85 Mandatory player-facing, 4 Conditional (`SCR-020`, `SCR-038`, `SCR-039`, `SCR-077`), 1 Provisional (`SCR-068`) and 10 administrative (`SCR-091`…`SCR-100`). Every screen has all eleven A–K fields; every screen has desktop, tablet and mobile presentation (blocked screens specify their deliberate absence). Matrix A status: **95 SPECIFIED / 2 PROVISIONAL / 3 BLOCKED**. The component catalogue defines **90 `UI-CMP` components** across seven families, each with all 19 required fields, plus the **8 `OVL` overlays** with page-reachable equivalents. A derived reverse index maps every screen to its component set.

### 91.4 Requirements, decisions and traceability

The B-13 block allocates **`REQ-870`…`REQ-1089`** (220 requirements): one per screen (`REQ-870`…`REQ-969`) and 120 cross-cutting shell/component/responsive/accessibility/permission/visualization/traceability requirements. Status: **213 SPECIFIED / 4 PROVISIONAL / 3 BLOCKED**. `REQ-869` remains the last pre-B-13 row and `REQ-1090` is the next free identifier. Decisions **D-206…D-219 / DD-254…DD-267** are recorded: thirteen Category B design positions and one Category C provisional bundle. Matrices A, B and C, the navigation register, the map/Network View reconciliation and the documentation impact register are present. No game rule, formula, parameter or existing requirement row was changed or duplicated.

### 91.5 Documentation impact

Updated: `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `ROADMAP.md`, `stage-2/00_stage_2_handoff.md`, `stage-2/01_stage_2_prompt_roadmap.md`, `stage-2/02_master_game_design_bible_outline.md` (B-13 moved to **Drafted at v1.0 — specification complete, not implemented**), `stage-2/03_requirements_traceability.md` (frontier pointer only), `stage-2/04_approved_and_provisional_decisions.md` (DD-254…DD-267 and tallies) and `DECISIONS.md` (D-206…D-219). The three B-13 files, the focused 13B validator and this §91 entry are new. The five accepted 13A documents, the B-02…B-12 rulebooks and `05_unresolved_design_decisions.md` were inspected and intentionally left unchanged. The Prompt 13B instruction was **not** archived verbatim (documented limitation; the 12B/12C/13A archives are unchanged). No historical entry was rewritten; the only dated historical-tail reconciliation is the progress-table row-10 live-prompt pointer, which now names Prompt 13C as the live next prompt, consistent with the 13A precedent.

### 91.6 Validation actually run

| Command | Result as printed |
|---|---|
| `python docs/qa_backups/13B_validate_ui_specifications.py` | `CHECKS: 24/24 passed; 0 failed` — `RESULT: PASS at the documentation level` |
| `python docs/qa_backups/13B_validate_ui_specifications.py --self-test` | `SELF-TEST: 3/3 cases passed` |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python docs/qa_backups/validate_links.py` | 106 files, 4,139 links, 3,757 checked locally, 382 external skipped, 32 anchors, `Unresolved: 0` |
| `python docs/qa_backups/test_next_action.py` | `Ran 27 tests … OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests … OK` |
| `python docs/qa_backups/13A_validate_ui_foundations.py` | `CHECKS: 34/34 passed; 0 failed` |
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 45/45 passed; 0 failed`; registers `D=219 DD=267 UD=60 REQ max=869` |
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 87/87 passed; 0 failed` |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py` | `CHECKS: 24/24 passed; 0 failed` |
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed` |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943` — `PASS` |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed` |
| `python docs/qa_backups/10B_validate_warfare.py` | `Checks run: 1036`; `73/73` negative fixtures rejected — `PASS` |
| `python docs/qa_backups/11B_validate_b11.py` | `RESULT: PASS` |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS` |
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — check 29 (`REQ-703` historical frontier) remains recorded debt, untouched since 12A §32 |
| `python docs/qa_backups/verify_politics_numbers.py` | `POLITICS NUMBERS: 879/879 checks passed` |
| `python -m py_compile` on every modified validator/test module | exit `0` |
| Full `test_09B_alliance_semantic_validator.py` 267-test suite | **NOT RERUN** (last complete pass precedes Prompt 13A; the 34-check semantic validator passed) |
| Runtime UI / browser / device / screen-reader verification | **NOT PERFORMED** — no UI exists and none is authorized |

**Validator expectations advanced, and why.** Current-status constants were moved to the values this pass created, with no rule, gate verdict, fixture count or protected status changed: `status_rules.py` (`CURRENT_SUBPROMPT` → `13C`, `13B` added to completed), `validate_final.py` (next prompt `13C`, DD contiguity 253 → 267, decision spelling 219, AI_CONTEXT row-04 totals), `test_next_action.py` (live value `13C`; row 13 now records 13B completion and Prompt 13C next), `test_decision_registers.py` (`13C`), `09_validate.py` (prompt `13C`, DD 267, spelling 219), `09A_validate_alliance.py` (`13[ABC]`), `09B_validate_alliance_semantic.py` (D-219/DD-267, Confirmed 79 / Provisional 52 / total 267, prompt `13C`), `10B_validate_warfare.py` (`13C`), `12A_validate_foundations.py` (`REQ max 1089`, `D-001..D-219`), `13A_validate_ui_foundations.py` (DD 267, current status `13C` / `D-001..D-219` / `2026-11-13`), `verify_politics_numbers.py` and the `test_09A`/`test_09B` live fixtures. These are frontier refreshes, not relaxations; the 13A validator's rule behaviour is otherwise untouched.

### 91.7 Limitations

No frontend, screen, component, route, migration or runtime test exists; no WCAG conformance is claimed. Responsive breakpoints remain provisional Category C values. Global Trade (`SCR-038/039`), favorites (`SCR-020`), world-health charts (`SCR-077`) and intelligence (`SCR-068`) remain absent/BLOCKED or PROVISIONAL as specified. The battle-report layout is derived from WAR-088 because the benchmark's report internals were `NOT-RETRIEVABLE`. The Prompt 13B instruction is not archived verbatim. The full 267-test 09B suite was not rerun. `11A_validate_research.py` check 29 remains historical debt. Prompt 13B has not received independent owner acceptance; the owner's review is the next acceptance step.

### 91.8 Next action

**Prompt 13C — complete player journeys and interaction sequences — is next but is NOT AUTHORIZED and NOT STARTED.** Prompt 13D, Prompt 14 and Prompt 15 remain unauthorized and unstarted. No frontend implementation is authorized by this record.

### 91.9 Prompt 13B-C1 correction record (2026-11-13)

A bounded Prompt 13B-C1 pass corrected four post-13B reconciliation issues without reopening the screen or component design.

**Internal references.** The main B-13 document had references written against the original thirty-section prompt map: `20–22`, `21`, `23`, `18`, `22.10`, `23.1–23.7`, `22`, plus catalogue labels `5.1–5.10` with no local subsections. They were corrected to the actual structure (`8–10`, `9`, `11`, `3.2` with the screen companion's administrative section, `29`, `27.1`), the catalogue labels lost the misleading section marker, and a numbering note now explains that the planned family sections 13–23 live in the screen companion. One ambiguous `12.3` reference in the screen companion was clarified as `WAR §12.3`. The component companion had no broken section or anchor reference. The 13B validator was extended from 24 to **28 checks** with deterministic section-reference and heading-anchor validation (`13B-25`, `13B-26`), plus archive and correction-register checks (`13B-27`, `13B-28`). Self-tests are **7/7** (four new positive/negative fixtures).

**Prompt archive.** `docs/prompts/prompt_13B_screen_and_component_specifications.md` now exists, created from the authorized Prompt 13B instruction. It contains all 26 instruction sections, **64,585 bytes**, **2,306 LF and 0 CRLF newlines**, and stored-bytes SHA-256 `20a76855c2e7a0b0d3ae436a7136d25ee8ec27a2a448ec100cb080b326dff2f7`. `docs/prompts/INDEX.md` carries the matching row and digest. One provenance paragraph was added after the title; no independent external original exists for byte-for-byte comparison, so this is recorded as a recovery limitation rather than a false verbatim-verification claim.

**Working-tree classification.** At the start of 13B-C1 the tree contained **24 substantive modifications** and **116 line-ending-only modifications**; at its completion it contains **25 substantive modifications** (the same 24 plus `docs/prompts/INDEX.md`) and the same **116 line-ending-only modifications**. The line-ending-only files are byte-different but content-identical after CRLF/LF normalisation and are pre-existing, uncertain-provenance changes. They were not normalised, restored, discarded or attributed to this pass. At the start of 13B-C1 there were **4 untracked B-13/validator files**; this pass adds one new prompt archive. The substantive files attributable to this pass are the B-13 parent, screen companion, 13B validator, `INDEX.md`, this progress log, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `stage-2/00_stage_2_handoff.md`, `stage-2/01_stage_2_prompt_roadmap.md` and `stage-2/02_master_game_design_bible_outline.md`; the remaining pre-existing modifications are preserved.

**Link-count reconciliation.** The Prompt 13B record (§91.6) reported 106 files / 4,139 links / 3,757 local / 382 external / 0 unresolved. The 13B-C1 rerun on the current tree reports **107 files / 4,146 links / 3,764 local / 382 external / 32 anchors / 0 unresolved** (`python docs/qa_backups/validate_links.py`). The +1 file and +7 links are the new prompt archive and its INDEX row. The independent audit's intermediate figures (4,142/3,760) are not reproducible from the current tree and are recorded as a different scan point or scope, not as an unresolved-link defect. §91.6 is preserved as the original dated result.

**Scope.** No gameplay rule, formula, requirement status, decision, owner-reserved matter, screen specification or component design was changed. D-219 / DD-267 remain the decision frontier. Prompt 13C and Prompt 13D remain NOT STARTED and NOT AUTHORIZED. The owner's review of the corrected 13B package is the next action.

**Prompt 13B-C1-R1 historical clarification (2026-11-13).** §29 of the B-13 parent is now explicitly labelled as the historical documentation impact assessment at original Prompt 13B completion. Its original findings are preserved unchanged, it cross-references §31, and §31 states that it records the subsequent Prompt 13B-C1 corrections without rewriting §29. The added §29→§31 reference changes the current documentation-link result to **4,147 links / 3,765 local / 33 anchors / 0 unresolved**; the 13B-C1 figures above remain the record of that pass. No other document required a status or handoff change.
