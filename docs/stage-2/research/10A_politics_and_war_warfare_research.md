# Politics and War warfare research, evidence, requirements and cross-system integration — Stage 2 Prompt 10A

**Version:** 1.1 · **Created:** 2026-11-03 · **Corrected:** 2026-11-03 (three defect corrections: Alliance NAP authority attributed to **`D-140`**, empty-source count corrected to four, and P&W geographic wording narrowed to distinguish game-world geography from map-based warfare mechanics) · **Stage 2, Prompt 10A** · **Research and documentation only**
**Status:** Research complete at the documentation level. **No Nation Supremacy warfare rule, unit, operation, formula, cost, readiness value, protection state, victory threshold or settlement term is approved by this document.** Every recommendation is a candidate for **Prompt 10B**. **Prompt 10B and Prompt 10C have not started.**
**Research access date:** 2026-11-03. Every URL in §6 was opened on that date unless the row says otherwise. No authenticated session, account action, in-game action, war declaration, message, transaction or API credential was used.
**Parent task:** Stage 2, **Prompt 10 — Warfare, campaigns and postwar settlements** ([stage-2/01 §Prompt 10](../01_stage_2_prompt_roadmap.md)). This report is the **10A** subphase only. It is **not** the B-10 warfare rulebook, which remains **10B's** deliverable.
**Research-scoped identifier spaces:** sources **`WFS-001…WFS-040`** ("warfare source"); findings **`WFR-001…WFR-052`**; formula evidence **`WFE-01…WFE-16`**; conflicts **`WFX-01…WFX-12`**; P&W-to-Nation-Supremacy classifications **`WFC-01…WFC-26`**; candidate requirements **`WCR-01…WCR-44`**; risks **`WRK-01…WRK-15`**; open research questions **`WFQ-01…WFQ-22`**; formula and numerical questions **`WQN-01…WQN-20`**; local evidence gaps **`GAP-01…GAP-16`**; handoff items **`WFH-A1…WFH-F6`**. None collides with the project's `D-`, `DD-`, `UD-`, `REQ-`, `DIP-`, `ALL-`, `ECN-`, `URB-`, `DMP-`, `NET-`, `ONB-`, `RRL-`, `TR-`, `F-`, `PWS-`, `DPS-` or `ALS-` spaces. They are **research identifiers, not decisions or registered requirements**.

---

## 1. Executive summary

1. **P&W is a nation-vs-nation war system built on a bounded, readable progress meter.** Each side starts a war with **100 Resistance**; the side that reduces the opponent to zero wins. The meter is advanced by a small catalogue of operations, each costing **Military Action Points (MAPs)**, and every operation has four possible victory levels. A war is capped at **60 turns (5 days)** and each nation may hold **5 offensive and 3 defensive wars**. This is the strongest comparator evidence for Nation Supremacy's central B-10 objective: a strategically meaningful conflict with a readable outcome and a natural stop, without a map.
2. **MAPs are close to D-015 in purpose but not in structure.** P&W starts each war at 6 MAPs, adds 1 per 2-hour turn, caps at 12, and lets the pool persist only inside that war. D-015 instead fixes **one per-nation pool, refilled to its cap at P3, non-transferable, reserved at acceptance and consumed at resolution**, with no banking above the cap. P&W's numbers, its per-war reset and its in-war accumulation **must not be copied**; its *design lesson* — a single military pool that forces attack-type choice — is directly relevant.
3. **P&W's warfare has no geographic front or map-based troop movement.** P&W does use geographic concepts in its game world — nations are associated with **continents**, radiation is tracked at continent and world level, and wars are fought over named **cities** (WFS-028, WFS-031). Its **warfare**, however, targets a nation, or for missiles and nukes a city within that nation; the examined pages document no front, province or tile, geographic adjacency, physical troop movement across a territorial map, coordinate-based battlefield targeting or geographic supply route. Cities function as development and damage-allocation units, not as battlefield positions, and continents do not create a theatre. This confirms that a complete, readable war system can operate without map-based warfare. It also means map geography is **not** the source of P&W's strategic depth; resource costs, unit composition, MAP allocation and domain control are.
4. **P&W's "supply" is an inventory-and-upkeep model, not logistics.** Units cost cash and resources to build, charge cash and food/resource upkeep every turn, and consume gasoline/munitions per battle. A nation with no gasoline or munitions cannot use its tanks, ships or aircraft in battle. There is **no stockpile-to-front route, no distance, no convoy, no encirclement and no supply-line cut**. The correct Nation Supremacy reading is **readiness and resource reservation**, not logistics.
5. **P&W's war lifecycle is thin at the end.** Declaration is immediate and unilateral; the attacker chooses one of three war types and cannot change it; a war ends by Resistance reaching zero, by mutual **Offer Peace**, or by the 60-turn cap. There is **no surrender button, no negotiated terms object, no mechanically enforced reparations, no enforced ceasefire terms and no postwar treaty**. Post-defeat **beige** gives 2 days of immunity from new declarations while existing wars continue. Reparations exist only as social agreements executed through ordinary transfers.
6. **P&W's protection stack is real but narrow.** New nations are beige for up to **14 days** and cannot be declared on; defeated nations get **2 days** of beige; gray nations (inactive 5 days) lose bonuses but are not protected; score range (75%–250%) and 5/3 war slots limit target selection; the official rules prohibit **war-slot filling**, **spy-slot filling**, same-network target stacking and bank protection through vacation mode or a new nation. There is no general "cannot attack a much weaker nation repeatedly" rule beyond the score band and slot limits.
7. **P&W's losses are a mix of destruction and transfer.** Combat destroys units and infrastructure and can destroy improvements; victory transfers **10% of money and 10% of resources**, destroys up to **4% of infrastructure in every city**, and loots the defeated nation's **alliance bank** by a score-ratio formula capped at 33%. Cities themselves are not destroyed by war. Value is destroyed (units, infrastructure, improvements) and transferred (loot), never minted.
8. **Alliance warfare is coordination, not command.** P&W has no alliance war entity, no alliance declaration, no delegated use of a member's military and no alliance-level combat resolution. Allies coordinate outside the game; the game records nation wars, allows alliance-bank looting, and punishes slot filling and same-network target stacking. This aligns with B-09's national military sovereignty, but B-09's own attack checks are **stricter** and must be treated as binding.
9. **The evidence has material internal conflicts.** P&W's official unit pages and its **July 2025 military update** disagree on plane, missile and nuclear costs and on plane upkeep; the Fandom War page and the PWPedia ship page disagree on ship operating resources; missile infrastructure damage is stated as capped at 300 in one place and 350 in another; the 250% maximum war range is announced but unconfirmed as deployed; the airstrike MAP cost is not documented; and the live war-declaration screen is behind login, so declaration eligibility could not be directly observed. These are recorded in §25, not silently resolved.
10. **Verdict.** P&W supplies a credible bounded-war skeleton without a geographic battlefield: **declaration → a small operation catalogue with costs and victory levels → a progress meter → a hard time cap → a mutual peace exit → a short post-defeat protection window**. It does **not** supply a settlement system, a supply system, an alliance command model or a protection model strong enough for Nation Supremacy's anti-attrition requirement. Nation Supremacy should **adopt the bounded-progress and off-ramp pattern, adapt the operation economy to D-015 and B-04/B-05, and reject any assumption that conflicts with B-03, B-08, B-09 or the mapless world model**.

**No rule is approved. Prompt 10B is next.**

---

## 2. Prompt scope and restrictions

### 2.1 What this report does

- Inventories the project's existing warfare baseline and every binding cross-system constraint.
- Researches the **Politics and War** browser game and P&W-specific documentation for warfare, military operations, readiness, protection, losses and war termination.
- Grades every source and records what it actually establishes, including contradictions and access failures.
- Assesses each mechanic against Nation Supremacy's **mapless** world model.
- Produces classification, integration, candidate-requirement, formula-question, risk and open-question registers for 10B.
- Analyses **UD-032** without resolving it.
- Hands structured work to 10B, 10C and downstream prompts.

### 2.2 What this report does not do

- **No B-10 rule is approved.** No unit roster, operation, formula, cost, cooldown, readiness value, protection duration, victory condition, loss rule, settlement term or re-entry rule is fixed here.
- **No new `D-` or `DD-` decision** is created. `DECISIONS.md`, the approved/provisional register and the unresolved register are not changed in decision state.
- **No global `REQ-` row** is added. Candidate requirements use the research-scoped `WCR-` prefix and are not registered.
- **No B-10 rulebook, formula register or workflow companion** is created. `17_warfare_and_settlements.md` is not created; the outline's B-10 slot remains Planned.
- **No implementation.** No game code, schema, migration, API, UI, scheduler, service, deployment or environment change was made. No runtime, load, security or multiplayer test was run, because there is nothing to run.
- **No other game was used as evidence.** The external research restriction in §3 is absolute.
- **No P&W state was changed.** No login, account, transaction, war declaration, message, espionage operation or settings change occurred.

### 2.3 External research restriction (binding)

All external game-mechanic evidence comes only from:

1. the Politics and War browser game and its publicly accessible interface;
2. official Politics and War documentation, PWPedia and the official rules page;
3. community wikis dedicated specifically to Politics and War.

**Prohibited and not used:** any other browser strategy game; any other game's wiki; general strategy-game sites; Reddit; Discord; YouTube; social media; general gaming blogs; unrelated military wikis; Wikipedia or generic encyclopedias; academic military research; real-world doctrine or history; unverified AI summaries; unrelated forum posts.

**Prohibited methods and not used:** private APIs; direct database access; source-code inspection; hidden endpoints; developer-tools extraction; automated scraping; unpublished internal data; game modifications or data-mining tools.

Search engines were used only to discover candidate P&W pages. A search snippet was never treated as evidence; every cited page was opened. No page was invented, and no revision date was guessed.

### 2.4 Evidence classes used

| Class | Meaning in this report |
|---|---|
| **LIVE-DIRECT** | A current mechanic or interface element directly observed in the public P&W browser game while logged out |
| **OFFICIAL-DOC** | The official P&W rules page or a PWPedia article maintained by the operator / Team PnWPedia |
| **P&W-WIKI** | A Politics and War-specific community wiki (Fandom) |
| **HISTORICAL** | A dated or archived statement that may no longer describe the live build |
| **INFERRED** | A reasoned interpretation of verified observations, explicitly not a documented rule |
| **UNVERIFIED** | Insufficient evidence; recorded as a gap, not used as a premise |

---

## 3. Date and methodology

### 3.1 Date and access

- **Access date:** 2026-11-03 (UTC).
- **Session:** logged out, public pages only.
- **Live interface observations:** the public nation page rendered a **War Policy** field (`Arcane`) and a military/nation panel; the public game shell, rules page and PWPedia rendered normally.
- **Access failure:** navigating the war-declaration screen redirected to **Login to Your Nation**. Declaration eligibility, the declaration form, the target picker and any live cooldown were therefore **not observed**. This is recorded as a limitation in §25 and §35, not inferred.
- **No P&W state change:** nothing was submitted, purchased, declared, messaged or modified.

### 3.2 Method

1. Read every project continuity and Stage 2 register document required by §2.1 of the brief, then the B-02…B-09 rulebooks and registers.
2. Built a warfare baseline from the project's own rules before opening any external source, so that P&W could not silently define the design.
3. Discovered P&W pages through targeted search and the PWPedia index, then opened each page directly in a browser.
4. Captured the rendered page text and the relevant headings, tables and formulas.
5. Classified each statement by evidence class and recorded access/revision limits.
6. Compared P&W statements against each other; recorded disagreements rather than selecting one.
7. Assessed each mechanic against the mapless constraint and the binding project rules.
8. Produced the registers in §§20–28 and the handoffs in §§29–30.
9. Updated project status and validators only after the research was closed (see §§32–33).

### 3.3 What counts as a "formula" here

A formula is recorded as **verified** only when an allowed page states the expression. Where a page states only part of an expression, the known part is quoted and the rest is marked **INFERRED** or **UNKNOWN**. No formula was reverse-engineered from outcomes, and no undocumented constant was invented. P&W formulas are evidence of *how one game does it*; they are **not** Nation Supremacy formulas and no value is adopted.

### 3.4 Limitations of the method

- P&W is a live service. A page may lag the build; the July 2025 update proves this.
- PWPedia and Fandom are not the same authority; Fandom is community-maintained.
- The live declaration screen was inaccessible.
- No player interview, survey, telemetry or playtest exists. Every experience claim is analytical.
- No P&W combat was executed, so no formula was empirically tested.

---

## 4. Project-document inventory

### 4.1 Continuity and authority documents

All paths were verified on disk and read at the start of 10A. Status shown is the position **on entry**; §33 records what 10A changed.

| Path | Role | Status on entry (2026-11-03) | Warfare relevance |
|---|---|---|---|
| [`docs/AI_CONTEXT.md`](../../AI_CONTEXT.md) | Master context and fixed constraints | 09C complete; Prompt 10 next | Mapless world, 2-hour turns, one account, free-first architecture |
| [`docs/AI_HANDOFF.md`](../../AI_HANDOFF.md) | Cross-AI handoff | 09C complete; Prompt 10 next | Carries the next-action statement 10A must update |
| [`docs/PROJECT_PROGRESS.md`](../../PROJECT_PROGRESS.md) | Stage tracker and status block | Prompt 09C complete; Prompt 10 next | Records the pre-10A state |
| [`docs/DECISIONS.md`](../../DECISIONS.md) | Project decision log | D-001…D-142 | D-015, D-023, D-024 are the warfare anchors |
| [`docs/ROADMAP.md`](../../ROADMAP.md) | Official stage roadmap (D-012) | Stage 2 in progress; Prompts 01–09 complete; Prompt 10 next | Names Prompt 10 as warfare |
| [`docs/AUTONOMOUS_DECISION_POLICY.md`](../../AUTONOMOUS_DECISION_POLICY.md) | Decision authority (D-014) | Confirmed | Explains why 10A makes no approvals and why UD-032 is not an owner question |

### 4.2 Stage 2 foundation and registers

| Path | Role | Status on entry | Warfare relevance |
|---|---|---|---|
| [`00_stage_2_handoff.md`](../00_stage_2_handoff.md) | Stage 2 working package | Revised for 09C | Boundaries, deliverables, out-of-scope list |
| [`01_stage_2_prompt_roadmap.md`](../01_stage_2_prompt_roadmap.md) | The only Stage 2 prompt register | Prompt 10 pending; 10–15 pending | Prompt 10 purpose, outputs, must-preserve list, B-09 dependency |
| [`02_master_game_design_bible_outline.md`](../02_master_game_design_bible_outline.md) | Bible outline and authority map | B-10 **Planned** | The canonical B-10 slot; no file yet |
| [`03_requirements_traceability.md`](../03_requirements_traceability.md) | Requirement register REQ-001…REQ-653 | 19 Approved / 487 Provisional / 5 Open / 2 Deferred (as recorded) | REQ-014, REQ-063, REQ-085/086, REQ-090, REQ-099, REQ-108/109, REQ-177, REQ-518, REQ-588–591, REQ-640/642/645–647 |
| [`04_approved_and_provisional_decisions.md`](../04_approved_and_provisional_decisions.md) | D/DD register for design use | D-001…D-142; DD-001…DD-165 | DD-033, DD-041, DD-042 |
| [`05_unresolved_design_decisions.md`](../05_unresolved_design_decisions.md) | UD register | 26 Resolved / 5 Deferred / 18 Open | **UD-032** is the warfare-owned row |
| [`06_stage_2_progress_log.md`](../06_stage_2_progress_log.md) | Progress log and validation record | §55 is the 09C-B correction | The 10A entry is appended as §56 |

### 4.3 Existing subsystem rulebooks and registers

| Prompt | Document(s) | Status | Warfare-relevant content |
|---|---|---|---|
| 02 | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](../07_core_gameplay_loop_symbolic_world_and_turn_system.md) **B-02** | Draft v1.5 | **TR-005** no global action currency; **D-015** OP block at lines 116–125; **TR-040** P5 Conflict owned by Prompt 10; **§19** reservation; **§24** subsystem contract; **TR-042** open question on pre/post-P3 campaign costs |
| 03 | [`09_account_onboarding_nation_creation_and_progression.md`](../09_account_onboarding_nation_creation_and_progression.md) **B-03** | Draft | **NET-025/026/029** restricted pairs and indirect routes; **RRL-019** warfare cleanup; **RRL-021** reroll block; **ONB-019/020** 7-day/84-turn protection; **ONB-023/024** protected nation cannot be attacked or attack; **ONB-031** 30-day/360-turn one-sided transfer restriction |
| 04 | [`10_economy_resources_treasury_and_finances.md`](../10_economy_resources_treasury_and_finances.md) **B-04** + [register](../10_economic_formula_and_balance_register.md) | Draft v1.3 | **ECN-214** Prompt 10 owns readiness/campaign resource quantities, order costs and shortage consequences; reserve at acceptance, consume at resolution, write ledger events, never mint; **ECN-130** reroll destroys inventory |
| 05 | [`11_cities_infrastructure_production_and_research.md`](../11_cities_infrastructure_production_and_research.md) **B-05** + [register](../11_city_infrastructure_production_and_research_formula_register.md) | Draft v1.5 | **URB-111** cities cannot be lost; **URB-157** Prompt 10 may add a Military research branch and military buildings only through a decision; default warfare destroys resources/units, not cities; **URB-014** OP numbers owned by Prompt 10; **URB-061** supplies steel/aluminum/gasoline/ammunition |
| 06 | [`12_population_and_domestic_politics.md`](../12_population_and_domestic_politics.md) **B-06** + [register](../12_population_and_domestic_politics_formula_register.md) | Draft v2.5 | **DMP-092** no military modifiers from government; **DMP-127** war is a crisis input only; **DMP-140** war may move approval only through Prompt 10 terms |
| 08 | [`15_diplomacy.md`](../15_diplomacy.md) + [formula register](../15_diplomacy_formula_register.md) | Complete | **DP-T01** NAP blocks declaration; **DIP-039** treaty parties are nations; **DIP-070** war-declaration ordering owned by Prompt 10; **DIP-141** NAP hook declared and inert until Prompt 10; **DIP-074** restricted pairs |
| 09 | [`16_alliances.md`](../16_alliances.md), [formula register](../16_alliances_formula_register.md), [integration contracts](../16_alliances_integration_contracts.md), [consistency audit](../16_alliances_project_wide_consistency_audit.md), [workflows](../16_alliances_workflows_acceptance.md) | Accepted at specification level | **ALL-089/139/140** national military sovereignty; **ALL-206** NAP attack prohibition; **ALL-209** same-Alliance ban; **ALL-210/211** one canonical validator, fail-closed at submission and execution; **ALL-213** Prompt 10 integration; **ALL-214** mandatory `AUD-AL-017`; **ALL-215** no confiscation/retaliation; **AX-18/AX-30** deferred coordination and binding attack-validation contract |

### 4.4 Existing research documents inspected

| Document | Status | Use in 10A |
|---|---|---|
| [`04_politics_and_war_economy_research.md`](04_politics_and_war_economy_research.md) | Complete | P&W economy discovery lead; not treated as proof of current warfare mechanics |
| [`05_politics_and_war_city_infrastructure_production_research.md`](05_politics_and_war_city_infrastructure_production_research.md) | Complete | City/building discovery lead; P&W city semantics |
| [`06_politics_and_war_domestic_politics_elections_and_policy_research.md`](06_politics_and_war_domestic_politics_elections_and_policy_research.md) | Complete | Policy/war-policy discovery lead |
| [`07A_politics_and_war_market_research.md`](07A_politics_and_war_market_research.md) | Complete | P&W source conventions; market/blockade interface |
| [`08A_diplomacy_research.md`](08A_diplomacy_research.md) | Complete | Prior finding that P&W enforces only NAP among treaty types (not re-verified here) |
| [`09A_alliance_research.md`](09A_alliance_research.md) + companions | Complete | Alliance coordination evidence; prior source-register conventions |

### 4.5 QA and documentation conventions

The following scripts under `docs/qa_backups/` were inspected: `status_rules.py`, `test_next_action.py`, `test_decision_registers.py`, `validate_final.py`, `09_validate.py`. The material findings are:

- `status_rules.py` detects the current sub-prompt from `CURRENT_SUBPROMPT` and recognises only `07A…09C`; its `SUBPROMPT` regex matches `0[789][A-C]`.
- `test_next_action.py` hard-codes `status_next_prompt(...) == "10"`, a `01[–-]0?7.*09C` history regex, row-09 and row-10 text, pending rows `10…15`, and sub-prompt status tests.
- `validate_final.py` hard-codes `stage_2_next_prompt == "10"`, the requirement count, DD/UD counts, the six `Pending` rows, and Prompt 10's B-09 dependency text.
- `09_validate.py` hard-codes the Stage 2 `IN PROGRESS` state, next prompt `10`, six `Pending` rows, and the row-09/row-10 keys.

**Consequence for 10A/10B/10C.** The three subphases are one official roadmap item. Status checks must continue to show **Prompt 10 as the active item** while distinguishing `10A complete / 10B next / 10C pending`. The existing checks that "the next prompt is 10" and that Prompts 11–15 are pending remain valid and must not be weakened; only the sub-prompt recognition and the row/next-action text need narrow extension. §33 records the exact changes made.

---

## 5. Existing Nation Supremacy warfare baseline

### 5.1 There is no B-10 rulebook

The Master Game Design Bible has **no warfare section**. B-10 is Planned; `17_warfare_and_settlements.md` does not exist. The baseline is therefore a set of **bindings, contracts and one deferred question**, not a design.

### 5.2 Binding rules the future B-10 must inherit

| Baseline item | Source | Status | What it actually fixes |
|---|---|---|---|
| Operations Points are the single military action resource | **D-015**; B-02 lines 116–125; **DD-033** | **Confirmed model; values Provisional** | One pool per nation; refilled **to cap** at P3; no accumulation above cap; military orders only; never purchasable, tradeable, giftable or transferable; reserved at acceptance; consumed at resolution; unused points do not bank. Cap, per-order costs and readiness scaling are **Provisional** |
| Warfare is in scope, not in the first playable build | **D-023**; **DD-041** | **Confirmed scope** | Bounded conflict, protection states, counterplay and postwar settlement remain requirements (REQ-014) |
| No shared action currency | **D-024**; **DD-042**; B-02 **TR-005** | **Confirmed** | Military orders draw on OP; every other subsystem declares its own visible limit. No universal per-turn click budget |
| Conflict resolves at **P5** | B-02 **TR-040** | Provisional | P5 resolves campaigns and adversarial interactions; bounded losses and an off-ramp are invariants; internal P5 order is Prompt 10's to publish |
| Campaign costs may draw on pre- or post-P3 balances | B-02 **TR-042** | **Open — Prompt 10 decides** | A real B-10 decision, with economy consequences |
| Every subsystem declares 15 contract items | B-02 **TR-093** | Provisional | State, actions/timing class, prerequisites, submission validation, costs/reservation, phase, ordering, effects, failure, results, visibility, invariants, edge cases, requirements, worked boundary |
| Strategic orders exist only with a war rule set, protection states and settlement enforcement | **REQ-014** | **Deferred** | B-10 must supply all three |
| Newcomer protection | B-03 **ONB-019/020/023/024**; **REQ-090** | Provisional; **D-021** | First nation only; **7 days / 84 turns** or first offensive action; cannot be targeted by a new offensive campaign, raid, espionage or hostile event; cannot initiate offensive action; once per account |
| Restricted pairs cannot fight | B-03 **NET-025/026/029**; **REQ-063** | Provisional | A blocked action moves nothing, declares no war and charges no OP; indirect routes are covered |
| Reroll during a campaign | B-03 **RRL-019/RRL-021**; **REQ-085/086** | Provisional | Reroll is **blocked** while a participant in an active campaign; battle history remains; Prompt 10 may define a forfeit that replaces the block — **UD-032** |
| War consumes resources through reservation and ledger | B-04 **ECN-214**; **REQ-177** | Provisional | B-10 owns gasoline/ammunition/steel/aluminum quantities, order costs and shortage consequences; reserve at acceptance, consume at resolution; `OBLIGATION_PAID`/`CONSUME`; never mint; leave D-015 untouched |
| One currency; no minting | B-04 **ECN-092**; D-049 | Confirmed design | Loot and reparations, if any, are **transfers** with matched ledger events |
| Cities are non-geographic and cannot be lost | B-05 **URB-111**; **URB-157** | Provisional | Warfare destroys resources/units by default; city loss is not a normal outcome; military buildings/research need a decision |
| No military modifiers from government | B-06 **DMP-092** | Provisional | Any military-government advantage needs a new decision and register row |
| War is a crisis input | B-06 **DMP-127**; **DMP-140** | Provisional | B-06 defines no crisis and no combat modifier; any war-weariness term must be a registered Prompt 10 term |
| NAP blocks a declaration | B-08 **DP-T01**; **DIP-141**; **REQ-518** | Provisional; inert until Prompt 10 | B-10 owns the declaration and must call the NAP hook |
| Alliance NAP and same-Alliance ban | B-09 **ALL-206/209/210/211/213/214/215**; **REQ-640/642/645–647** | **Accepted at specification level** | Every attack path calls **one canonical server-side validator**, independently for the same-Alliance ban and every applicable Alliance NAP, at **submission and execution**, fails closed, consumes nothing, and writes `AUD-AL-017`. No delegation, waiver, confiscation or retaliation |
| National military sovereignty | B-09 **ALL-089/139/140**; **REQ-588–591** | Accepted at specification level | An alliance cannot order, move, attack with or spend for a member's military; no private military view; coordination features deferred to B-10 |
| UD-032 | [`05`](../05_unresolved_design_decisions.md) | **Deferred to Prompt 10** | Reroll during an active campaign: (a) keep the block, (b) forfeit with a recorded outcome, (c) finish under the old identity; owner: **No — Prompt 10 decides** |

### 5.3 What is missing at the start of 10A

| Gap | Evidence | Consequence for 10B |
|---|---|---|
| No warfare state model | B-10 absent | Must define declaration, active war, operation, resolution, termination, settlement, protection and history states |
| No operation catalogue | B-10 absent | Must define every permitted hostile action and its costs |
| No battle-resolution model | B-10 absent | Must define strength, randomness (if any), victory levels, loss allocation, caps and rounding |
| No readiness model | B-10 absent; B-05 has no military branch | Must define units, recruitment, upkeep, resource consumption and recovery, with a decision if buildings are needed |
| No protection/counterplay model | Only B-03 newcomer protection and B-09 attack checks exist | Must define war-specific protection, target limits and defensive options |
| No settlement model | B-04 allows transfers; B-08 has no war settlement object | Must define victory, peace, terms, enforcement and postwar protection, or explicitly state that none is enforced |
| No war limits | D-024 requires a visible limit | Must declare war slots, operation caps, cooldowns and per-target limits |
| No war visibility model | B-02 visibility classes exist | Must assign a class to every war field and define opponent/third-party view |
| No formula register | B-10 absent | 10B must create one; 10A only records P&W evidence and questions |
| UD-032 unresolved | 05 register | 10B must decide; 10A must not |

---

## 6. P&W source register

All sources were accessed **2026-11-03** unless the row states otherwise. "Official" means published by Politics & War / Yellowstone Digital Media; PWPedia is the operator's encyclopedia and states that pages are "maintained by Team PnWPedia". Fandom is an independent community wiki and is **never** called official here.

| ID | Title | Publisher / author | Category | Exact URL | Heading / section used | Access date | Revision date | Currency | Mechanic | Limitations |
|---|---|---|---|---|---|---|---|---|---|---|
| **WFS-001** | Game Rules | Politics & War (official) | OFFICIAL-DOC | https://politicsandwar.com/rules/ | Game & Community Rules; 17 Game Rules; Inactivity Deletion Schedule | 2026-11-03 | Not published on page | Current | One nation; same-network restrictions; war-slot filling; spy-slot filling; bank protection; coerced city deletion; automation; exploit abuse; inactivity deletion | Rules state prohibitions, not combat formulas; no revision date |
| **WFS-002** | July 2025 Update | Politics & War PWPedia (official) | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/july-2025-update | Military Research; Ship Rebalance; Cost Tweaks; Beige Buff | 2026-11-03 | Titled "July 2025"; exact day not shown | Current | Plane upkeep 750/1000; plane cost 10 aluminium; nuke 1000 aluminium/500 gasoline/500 uranium; missile 150 aluminium/100 gasoline/100 munitions; ship upkeep 3300/5000; ship operations 1 gasoline/1.75 munitions; beige +15% recruitment | An update notice, not a consolidated rulebook; conflicts with unit pages |
| **WFS-003** | War Types | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/War-Types | War Types | 2026-11-03 | Not shown | Current | Three war types; attacker chooses; defender cannot choose or change; damage/loot asymmetry | No numeric table on this page |
| **WFS-004** | Fortify | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Fortify | Fortify | 2026-11-03 | Not shown | Current | 3 MAP; no resistance change; +25% attacker casualties; ends on own offensive attack | Does not state stacking beyond "same as one" |
| **WFS-005** | Missile Strike | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Missile-Strike | Missile Strike | 2026-11-03 | Not shown | Current | 8 MAP; 2 improvements; 18 resistance; infra cap 350; city target | Conflicts with Fandom Missiles page's 300 wording |
| **WFS-006** | Nuclear Attack | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Nuclear-Attack | Nuclear Attack | 2026-11-03 | Not shown | Current | 12 MAP; 4 improvements; 25 resistance; infra cap 2000; city target; pollution | No formula for population killed |
| **WFS-007** | Naval Battles | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Naval-Battles | Naval Battles | 2026-11-03 | Not shown | Current | 4 MAP; 14/11/8 resistance by victory; 1 ship minimum; 15% improvement chance; blockade | No formula; airstrike/ground MAP costs not stated |
| **WFS-008** | Ground Control | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Ground-Control | Ground Control | 2026-11-03 | Not shown | Current | Immense Triumph ground battle; tanks kill aircraft; break by victory, third nation or destroying ground units; naval ground defense | No aircraft-kill formula |
| **WFS-009** | Air Superiority | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Air-Superiority | Air Superiority | 2026-11-03 | Not shown | Current | Immense Triumph airstrike; halves enemy tank combat value; break by victory, third nation, losing aircraft or naval air defense | No formula |
| **WFS-010** | Blockade | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Blockade | Blockade | 2026-11-03 | Not shown | Current | Immense Triumph naval battle; trade/bank restrictions; ends with war or break | Consequence list is descriptive |
| **WFS-011** | Soldiers | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Soldiers | Soldiers | 2026-11-03 | Not shown | **Outdated in part** | $5; barracks 1000/day, 3000 hold; 175% with munitions; 3 MAP; 10 resistance on immense | Conflicts with July 2025 on unrelated numbers only; no revision date |
| **WFS-012** | Tanks | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Tanks | Tanks | 2026-11-03 | Not shown | Current | $60 + 0.5 steel; factory 50/day, 250 hold; $50/$75; 1 munitions + 1 gasoline per 100; 40-soldier value | No formula; values may lag |
| **WFS-013** | Planes | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Planes | Planes | 2026-11-03 | Not shown | **Outdated** | $4,000 + 5 aluminium; hangar 3/day, 15 hold; $500/$750; 1 munitions + 1 gasoline per 4 | Superseded by WFS-002 on cost/upkeep |
| **WFS-014** | Ships | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Ships | Ships | 2026-11-03 | Not shown | Current | $50,000 + 30 steel; drydock 1/day, 5 hold; $3,300/$5,000; 1 gasoline + 1.75 munitions; 4 attack options | No formula |
| **WFS-015** | Spies | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Spies | Spies | 2026-11-03 | Not shown | Current | $50,000; $2,400 upkeep; 50 default / 60 with Intelligence Agency; 2/day base | No espionage success formula |
| **WFS-016** | Missiles | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Missiles | Missiles | 2026-11-03 | Not shown | **Outdated** | Missile Launch Pad; 2/day (3 with Space Program); $150,000 + 100 aluminium/75 munitions/75 gasoline; $21,000/$31,500 | Superseded by WFS-002 on cost |
| **WFS-017** | Nukes | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Nukes | Nukes | 2026-11-03 | Not shown | **Outdated** | $1.75m + 750 aluminium/500 gasoline/250 uranium; 1/day (2 with Nuclear Launch Facility); $35,000/$52,500; 12 MAP | Superseded by WFS-002 on cost |
| **WFS-018** | Airstrike | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Airstrike | Airstrike | 2026-11-03 | Not shown | Current | Aircraft required; target types; always some aircraft casualties; 3 aircraft minimum | MAP cost and resistance values not stated |
| **WFS-019** | Ground Battles | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Ground-Battles | Ground Battles | 2026-11-03 | Not shown | Current | 3 MAP; 50 soldiers minimum; 10 resistance on immense; ground control; loot | No formula on PWPedia page |
| **WFS-020** | Espionage | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/Espionage | Espionage | 2026-11-03 | Not shown | Current | Operations; no war required; cash cost; once/day (twice with Intelligence Agency) | No full success formula |
| **WFS-021** | War Policy | Politics & War PWPedia | OFFICIAL-DOC | https://politicsandwar.com/pwpedia/article/war-policy | War Policy | 2026-11-03 | Not shown | Current | A war-policy emphasis exists and can be changed | PWPedia page did not expose the 10-policy table in the captured render; Fandom WFS-023 supplies it |
| **WFS-022** | War | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/War | The War System; Starting a War; Units; Attacks | 2026-11-03 | Not shown | Community-maintained, likely mixed-age | 100 resistance; 6 MAP start; +1/turn; cap 12; 60 turns; 9 actions; 4 victory types; space control; 3 war types; 7 units; 5/3 slots; unit table | Community wiki; unit table predates July 2025 on some values |
| **WFS-023** | War Policy | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/War_Policy | Overview; War Policies table | 2026-11-03 | Not shown | Current as rendered | 10 policies; 60-turn change cooldown; exact bonuses/downsides | Community-maintained; no revision date |
| **WFS-024** | Ground Battles | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Ground_Battles | Loot; Infrastructure Damage; Casualties | 2026-11-03 | Not shown | Mixed-age | Loot formula; infra formula; army value; casualty formulas; 3 rolls | Formula parentheses are ambiguous/possibly mis-transcribed |
| **WFS-025** | Airstrike | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Airstrike | Airstrike Formula; Targeted Unit Damage | 2026-11-03 | Not shown | Mixed-age | Airforce value = aircraft × 3; 3 rolls; infra and unit formulas | Community; no revision date |
| **WFS-026** | Naval Battle | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Naval_Battle | Naval Battle Formula; Blockade | 2026-11-03 | Not shown | Mixed-age | Infra formula; army value = ships × 4; 3 rolls; blockade | Community; no revision date |
| **WFS-027** | Missiles | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Missiles | Cost; Infrastructure Damage | 2026-11-03 | Not shown | Outdated in part | Cost table; infra formula `RAND(300, MAX(350, popdensity×3))`, cap `infra×0.3+100` | Conflicts with WFS-002 and WFS-005 |
| **WFS-028** | Nuclear Weapons | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Nuclear_Weapons | Overview; Cost | 2026-11-03 | Not shown | Outdated in part | 25 resistance; 4 improvements; 12 MAP; 400 pollution; costs | Conflicts with WFS-002 |
| **WFS-029** | Espionage | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Espionage | Espionage Operations; Safety Level; Caught; Failure | 2026-11-03 | Not shown | Current as rendered | 9 operations; success levels; 1% caught/failure; spy-loss formula | Community; no revision date |
| **WFS-030** | Blockade | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Blockade | Overview; Mechanics; Consequences; Breaking | 2026-11-03 | Not shown | Current as rendered | Trade/bank restrictions; break conditions | Community; no revision date |
| **WFS-031** | Victory | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Victory | Overview | 2026-11-03 | Not shown | Mixed-age | Beige 2 days; 10% money/resources; 4% infra; alliance-bank loot formula | Community; no revision date |
| **WFS-032** | Color | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Color | Beige; Gray | 2026-11-03 | Not shown | Current as rendered | Beige invulnerable to new declarations; new nation up to 14 days; gray after 5 days inactive; bonuses | Community; no revision date |
| **WFS-033** | Nation Formulas | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Nation_Formulas | Nation Score; War Range; Espionage Range | 2026-11-03 | Text refers to 2023-11-04 | Mixed-age | Score formula; war range 0.75/2.50; espionage range 0.40/2.50; 250% note | Community; the 250% change is explicitly unconfirmed |
| **WFS-034** | Nation Score | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Nation_Score | Overview | 2026-11-03 | Not shown | Current as rendered | Score components; missile/nuke caps | Community; duplicates WFS-033 |
| **WFS-035** | Military Action Points | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Military_Action_Points | — | 2026-11-03 | — | **Empty page** | No article text | Evidence of absence only |
| **WFS-036** | War Range | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/War_Range | — | 2026-11-03 | — | **Empty page** | No article text | Evidence of absence only |
| **WFS-037** | Peace | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/Peace | — | 2026-11-03 | — | **Empty page** | No article text | Evidence of absence only |
| **WFS-038** | DEFCON | Politics and War Wiki (Fandom) | P&W-WIKI | https://politicsandwar.fandom.com/wiki/DEFCON | — | 2026-11-03 | — | **Empty page** | No article text | War Policy page references DEFCON; no mechanic documented |
| **WFS-039** | Login to Your Nation | Politics & War (live) | LIVE-DIRECT (access failure) | https://politicsandwar.com/login/ (redirect target) | Login | 2026-11-03 | — | Current | The war-declaration screen redirected here | **No declaration eligibility observed**; no login attempted |
| **WFS-040** | Nation page (live public) | Politics & War (live) | LIVE-DIRECT | https://politicsandwar.com/nation/id=1 (representative public page) | Nation panel; War Policy field | 2026-11-03 | — | Current | A live public nation page exposes a War Policy value and military/nation fields | One public page; no combat state observed |

**Source count:** 40 entries, of which 4 are empty pages (`WFS-035`, `WFS-036`, `WFS-037` and `WFS-038`), 1 is an access failure (`WFS-039`) and 1 is a live-interface observation (`WFS-040`). **Publisher-official:** 21 (`WFS-001`–`WFS-021`). **Community wiki:** 13 (`WFS-022`–`WFS-034`). **Live/access:** 2 (`WFS-039`–`WFS-040`). **Empty/absence:** 4.

### 6.1 Source conflicts recorded, not smoothed over

| Conflict | Sources | What each says | Treatment |
|---|---|---|---|
| Plane build cost | WFS-013 vs WFS-002 | 5 aluminium vs 10 aluminium | **WFX-01**; July 2025 update is later and official; unit page is treated as outdated |
| Plane upkeep | WFS-013/WFS-022 vs WFS-002 | $500/$750 vs $750/$1,000 | **WFX-01**; same treatment |
| Missile build cost | WFS-016/WFS-022 vs WFS-002 | 100 aluminium/75 gasoline/75 munitions vs 150 aluminium/100 gasoline/100 munitions | **WFX-02** |
| Nuke build cost | WFS-017/WFS-022 vs WFS-002 | 750 aluminium/500 gasoline/250 uranium vs 1,000/500/500 | **WFX-02** |
| Ship operating resources | WFS-022 vs WFS-014/WFS-002 | 2 gasoline/3 munitions vs 1 gasoline/1.75 munitions | **WFX-03**; PWPedia + July 2025 agree, Fandom War table is older |
| Missile infra cap | WFS-027 vs WFS-005 | Formula `RAND(300, MAX(350, …))` and prose "more than 300" vs "capped at 350" | **WFX-04**; both can describe a random range and a cap, but the wording is inconsistent |
| Aggressor/defender effect | WFS-022 | "Being an aggressor or a defender does not have any affect" in the role section, while war types give defender-specific modifiers | **WFX-05**; role itself has no effect, but the war type does; the prose is imprecise |
| War range maximum | WFS-033 | Formula says 250%; text says the 175%→250% change was announced in August 2023 and "as of November 4th, 2023, it has not been confirmed" | **WFX-06**; current deployment is **UNVERIFIED** |
| War duration/expiry | WFS-022 | "Wars can last for up to 60 turns (5 days)" | **WFX-07**; a bound is stated, but the exact expiry routine is not |
| Peace/settlement | WFS-022, WFS-037 | Offer Peace requires acceptance; the Peace page is empty | **WFX-08**; no settlement object documented |
| MAP costs per operation | WFS-022, WFS-007, WFS-005, WFS-006, WFS-004, WFS-019 | Ground 3, naval 4, missile 8, nuke 12, fortify 3; airstrike not stated | **WFX-09**; airstrike MAP cost is a gap, not a value to guess |
| P&W alliance NAP enforcement | 08A `DPS-001` (prior project research) | P&W's treaty web enforces only non-aggression | **WFX-10**; **not re-verified in 10A**; used only as prior context, not as new evidence |
| PWPedia vs Fandom authority | WFS-002…WFS-021 vs WFS-022…WFS-034 | PWPedia is operator-maintained; Fandom is community-maintained | **WFX-11**; official wins on conflict, community is used for formulas PWPedia does not publish |
| Live declaration screen | WFS-039 | Redirect to login | **WFX-12**; declaration eligibility not directly observed |

---

## 7. Detailed P&W mechanics catalogue

This section describes what Politics & War does. It is descriptive. It does not recommend, approve or port any rule. Every factual statement carries a source ID and an evidence class; where the examined pages disagree, the disagreement is named rather than averaged.

### 7.1 Declaration eligibility

| Condition | P&W rule as documented | Evidence | Confidence |
|---|---|---|---|
| Score window | A nation may declare on a target whose score is between **75%** and **250%** of its own score (`Min Score = Nation Score × 0.75`; `Max Score = Nation Score × 2.50`) | WFS-033 (P&W-WIKI), WFS-034 (P&W-WIKI) | High for the min; **medium** for the max — the wiki itself says the 175%→250% change was announced in August 2023 and was still unconfirmed on 2023-11-04 (WFX-06) |
| Espionage window | Espionage may target scores between **40%** and **250%** of the actor's score | WFS-033 | Medium (community formula; wider than the war window) |
| Offensive slots | **5** concurrent offensive wars; **+1** with the Pirate Economy project | WFS-022, WFS-040 context | High |
| Defensive slots | **3** concurrent defensive wars | WFS-022 | High |
| Beige | A beige nation is **invulnerable to new war declarations** | WFS-032 | High |
| New-nation beige | A newly created nation may stay beige for **up to 14 days** and cannot return once it leaves; new nations are beige unless the creator opts into combat | WFS-032 | High |
| Gray | A nation becomes gray on leaving beige or after **5 days** of inactivity; gray is **not** immune to declarations | WFS-032 | High |
| Consent | None. The attacker declares unilaterally; the defender does not accept or refuse the declaration | WFS-022, WFS-003 | High |
| War type | Chosen by the attacker at declaration; cannot be changed afterwards; the defender cannot choose it | WFS-003, WFS-022 | High |
| Cost and cooldown | No declaration cost and no inter-war cooldown are documented on the examined pages | WFS-022; absence in WFS-001…WFS-038 | **UNVERIFIED** (absence of evidence, not evidence of absence) |
| Declaration screen fields | Not observed: the live declaration screen redirected to `https://politicsandwar.com/login/` | WFS-039, WFX-12 | **No direct observation**; no login was attempted |

The score window is the only structural anti-prey rule P&W documents. It is a **relative-strength** gate, not a protection status: a small nation can be attacked by any nation within 250% of its score, and a very large nation is equally limited from attacking far smaller ones. WFS-034 states the purpose explicitly: to prevent very large nations from picking on very small nations.

### 7.2 War categories and objectives

P&W documents **three war types**. They are damage-and-loot presets, not objectives:

| War type | Attacker infrastructure damage | Attacker loot | Defender infrastructure damage | Defender loot | Source |
|---|---|---|---|---|---|
| **Ordinary** | 50% of potential | 50% of potential | 50% of potential | 50% of potential | WFS-022 |
| **Attrition** | 100% of potential | 25% of potential | 100% of potential | 50% of potential | WFS-022 |
| **Raid** | 25% of potential | 100% of potential | 50% of potential | 100% of potential | WFS-022 |

Two consequences follow directly. First, every war type is a **two-sided economic contract**: the attacker's choice also sets the defender's damage and loot percentages, and the defender's raiding ability is never reduced to the attacker's raiding percentage. Second, no war type declares a political objective. There is no "capture," "regime change," "demilitarise" or "reparations" war goal in the documented system. The only win condition is reduction of the opponent's resistance to zero (§7.5). The free-text war reason is explicitly cosmetic: "The reason has no affect on the gameplay or outcome of a war" (WFS-022).

### 7.3 Resistance, Military Action Points, slots and duration

| Element | P&W value | Evidence | Note |
|---|---|---|---|
| Resistance | **100** per side per war; reduced by successful attacks; at **0** the war ends | WFS-022 | Per-war pool, not a national pool |
| MAP start | **6** per side per war | WFS-022 | Blitzkrieg makes attackers start with **7**; Fortress makes **both** start with **5** |
| MAP regeneration | **+1 per turn**, both sides | WFS-022 | A turn is 2 hours, so 12 MAP/day |
| MAP cap | **12** ; further regeneration is lost | WFS-022 | Explicit time advantage for the side that spends |
| War duration | **Up to 60 turns (5 days)** | WFS-022 | The expiry routine itself is not documented (WFX-07) |
| Offensive slots | 5 (+1 Pirate Economy) | WFS-022 | Slots are national, not per-alliance |
| Defensive slots | 3 | WFS-022 | A nation can be in more than 3 defensive wars only if slots are freed or rules change |
| MAP scope | **Per war.** Each war has its own MAP balance and resistance pool | WFS-022 (implied by "each nation starts with 6 MAPs upon declaration of war" and per-war turn regeneration) | This is the single most important structural difference from D-015 |

The per-war scope is decisive for Nation Supremacy. D-015 specifies **one national Operations Points pool**, refilled to cap at the boundary and spent on military orders. P&W instead gives each war its own small action budget. A nation in five wars therefore has five separate 6→12 MAP pools, not one pool of 30→60. P&W's model rewards **opening many small wars**; D-015's model forces a **national prioritisation** across all wars. The two are not interchangeable, and 10B cannot assume P&W's per-war pool is compatible with D-015.

### 7.4 The nine military actions

P&W documents exactly nine military actions (WFS-022):

| # | Action | Category | MAP | Resistance effect | Targets | Minimum force | Source |
|---|---|---|---|---|---|---|---|
| 1 | **Ground Battle** | Offensive | 3 | IT 10; lower tiers less; UF 0 | Soldiers, tanks; loot; infrastructure; ground control | 50 soldiers | WFS-019, WFS-022, WFS-024 |
| 2 | **Airstrike** | Offensive | **Not stated** | **Not stated** | Aircraft, tanks, soldiers, ships, infrastructure, money | 3 aircraft (per WFS-018) | WFS-018, WFS-025 |
| 3 | **Naval Battle** | Offensive | 4 | IT 14 / MS 11 / PV 8 / UF 0 | Ships, infrastructure, improvements; blockade | 1 ship | WFS-007, WFS-026 |
| 4 | **Launch Missile** | Offensive | 8 | 18 | City infrastructure; 2 improvements; city chosen | 1 missile + Missile Launch Pad | WFS-005, WFS-027 |
| 5 | **Nuclear Attack** | Offensive | 12 | 25 | City infrastructure; 4 improvements; radiation | 1 nuke + Nuclear Research Facility | WFS-006, WFS-028 |
| 6 | **Fortify** | Defensive | 3 | None | Self; +25% attacker casualties | None | WFS-004, WFS-022 |
| 7 | **Espionage** | Covert | 0 | None | 9 operations (see §7.14) | Spies; cash | WFS-020, WFS-029 |
| 8 | **Offer Peace** | Diplomatic | 0 | None | The war | None | WFS-022, WFS-037 |
| 9 | **Timeline** | Information | 0 | None | Read-only war log | None | WFS-022 |

The action set is **small and legible**. Five actions reduce resistance; one mitigates incoming damage; one operates outside the resistance race; one exits the war; one is a log. There is no manoeuvre, no front, no encirclement, no interception and no supply-line raid. The only "space" is the abstract **control state** in §7.5.

### 7.5 Victory types, space control and the resolution shape

Every ground, air and naval battle is resolved by **three independent rolls** per side, each between **40% and 100%** of that side's combat value. The side that wins more rolls wins the exchange (WFS-022, WFS-024, WFS-025, WFS-026):

| Rolls won | Victory type | Damage/resistance multiplier |
|---|---|---|
| 3 of 3 | **Immense Triumph** | 3/3 |
| 2 of 3 | **Moderate Success** | 2/3 |
| 1 of 3 | **Pyrrhic Victory** | 1/3 |
| 0 of 3 | **Utter Failure** | 0 |

The four **space-control** states are consequences of an Immense Triumph:

| State | Gained by | Effect | How it is broken | Source |
|---|---|---|---|---|
| **Ground Control** | Immense Triumph in a Ground Battle | Subsequent non-failure ground victories let the holder's tanks destroy enemy aircraft; also nullifies the defender's ground control in all wars | A non-failure ground victory by the opponent; a third nation's Immense Triumph; naval "Ground Defense" option on an Immense Triumph; destruction of the ground force (per PWPedia) | WFS-008, WFS-022 |
| **Air Superiority** | Immense Triumph in an Airstrike | Enemy tanks fight at **50%** combat value | A non-failure airstrike; a third nation's Immense Triumph; loss of all aircraft; naval "Air Defense" option on an Immense Triumph | WFS-009, WFS-022 |
| **Blockade** | Immense Triumph in a Naval Battle | Enemy cannot trade or move cash/resources into or out of the nation; cannot deposit to or retrieve from the alliance bank | A non-failure naval battle; a third nation's Immense Triumph | WFS-010, WFS-030 |
| **Fortified** | Fortify (3 MAP) | Attackers suffer **+25% casualties** | The fortified nation launches an offensive attack | WFS-004, WFS-022 |

Two design properties matter here. **Control is personal, not territorial**: it attaches to a nation in a war, not to a province or a map region. **Control is contestable every turn**: one successful low-cost action can remove it, and a third nation can remove it in a war that is not its own. This is a mapless abstraction that already behaves like a symbolic world.

### 7.6 Units, buildings, recruitment and upkeep

P&W has **seven units** (WFS-022). Soldiers, tanks, aircraft and ships are recruited through city buildings; spies need no building; missiles and nuclear weapons need national projects.

| Unit | Build cost | Building | Recruitment per building per day | Hold per building | Peacetime upkeep | Wartime upkeep | Per-battle resources | Source |
|---|---|---|---|---|---|---|---|---|
| Soldiers | $5 each | Barracks | 1,000 | 3,000 | $1.25 + 1 food/750 | $1.88 + 1 food/500 | 0.0002 munitions each when armed | WFS-011, WFS-022 |
| Tanks | $60 + 0.5 steel | Factory | 50 | 250 | $50 | $75 | 0.01 gasoline + 0.01 munitions | WFS-012, WFS-022 |
| Aircraft | $4,000 + **5 aluminium** (PWPedia) / **10 aluminium** (July 2025) | Hangar | 3 | 15 | $500 (PWPedia) / **$750** (July 2025) | $750 (PWPedia) / **$1,000** (July 2025) | 0.25 gasoline + 0.25 munitions | WFS-013 vs WFS-002, WFX-01 |
| Ships | $50,000 + 30 steel | Drydock | 1 | 5 | **$3,300** | **$5,000** | **1 gasoline + 1.75 munitions** (July 2025) | WFS-014, WFS-002, WFX-03 |
| Spies | $50,000 | None | 2 (3 with Intelligence Agency) | 50 (60 with Intelligence Agency) | $2,400 | $2,400 (unchanged) | None; cash per operation | WFS-015, WFS-022 |
| Missiles | $150,000 + 100 aluminium + 75 munitions + 75 gasoline (July 2025) | Missile Launch Pad project | 2 (3 with Space Program) | Unlimited | $21,000 | $31,500 | None to fire | WFS-016 vs WFS-002, WFX-02 |
| Nuclear weapons | $1.75m + **1,000 aluminium + 500 gasoline + 500 uranium** (July 2025) | Nuclear Research Facility project | 1 (2 with Nuclear Launch Facility) | Unlimited | $35,000 | $52,500 | None to fire | WFS-017 vs WFS-002, WFX-02 |

Three properties are load-bearing:

1. **Recruitment is daily and building-capped.** A nation cannot convert money into units without the right city buildings, and cannot exceed a fixed hold per building. Military power is therefore a function of **city development and time**, not just treasury.
2. **Wartime upkeep is roughly 1.5× peacetime** for soldiers, tanks and aircraft, and exactly 1.515× for ships ($3,300 → $5,000). A large army is a permanent drain that intensifies when used.
3. **Operations consume resources per battle, not per turn.** Tanks, aircraft and ships burn gasoline and munitions when they fight; soldiers optionally burn munitions. A nation with units but no resources can still be attacked and can still defend, but its offensive output degrades. This is the closest P&W comes to logistics (§7.8, §12).

The **beige buff** added in July 2025 gives a beige nation with no active wars **+15%** to daily recruitment of soldiers, tanks, aircraft and ships, additive with the Propaganda Bureau project (WFS-002). It is explicitly a recovery mechanic for knocked-down nations.

### 7.7 Battle resolution: what is rolled and what is deterministic

| Attack | Resolution | Randomness | Deterministic elements | Source |
|---|---|---|---|---|
| Ground | 3 rolls of army value; victory tier; loot, infra damage and casualties follow | Rolls 40–100%; loot random 0.8–1.1; damage random 0.85–1.05 | Minimum 50 soldiers; MAP cost; resource burn; improvement chance 10% on IT | WFS-024, WFS-019 |
| Airstrike | 3 rolls of airforce value; target type chosen before the strike | Rolls 40–100%; damage random 0.85–1.05 | Targets always take some aircraft casualties; 70%/40%/0% of calculated unit casualties at MS/PV/UF | WFS-025, WFS-018 |
| Naval | 3 rolls of ship value; victory tier; blockade on IT | Rolls 40–100%; damage random 0.85–1.05 | 15% improvement chance on IT; 1 ship minimum | WFS-026, WFS-007 |
| Missile | Deterministic hit once launched | Infra roll `RAND(300, MAX(350, population density × 3))` | 18 resistance; 2 improvements; city and improvement type chosen | WFS-005, WFS-027 |
| Nuclear | Deterministic hit once launched | Infra roll documented as capped at 2,000 | 25 resistance; 4 improvements; radiation | WFS-006, WFS-028 |
| Fortify | No roll | None | +25% attacker casualties until the fortified nation attacks | WFS-004 |
| Espionage | Probabilistic | Safety level modifies price and success; at least 1% caught and 1% failure | Once per day (twice with Intelligence Agency); no MAP | WFS-029, WFS-020 |

The system is **readable in outcome, opaque in formula**. The in-game timeline shows what happened (victory type, losses, loot), but the examined public pages do not expose a pre-battle odds calculator; the community wiki reconstructs the rolls. That distinction matters for Nation Supremacy's "transparent resolution both sides can read" requirement: P&W is transparent **after** the fact, not **before** it.

### 7.8 Supply and logistics

P&W's **warfare** has **no geographic supply system**. Within the examined combat and logistics mechanics there is no distance, no supply line, no convoy, no depot, no encirclement and no attrition from being cut off. Logistics is a national **inventory** problem:

| Mechanism | What it does | Evidence |
|---|---|---|
| Per-battle resource burn | Tanks, aircraft and ships consume gasoline/munitions; armed soldiers consume munitions | WFS-011, WFS-012, WFS-013, WFS-014, WFS-002 |
| Stockpile gate | A nation without steel/aluminium cannot build tanks, ships or aircraft; without gasoline/munitions it cannot use them in battle | WFS-030 |
| Power gate | A nation without power cannot operate military buildings and therefore cannot buy more troops, but can still execute military actions with existing units | WFS-030 |
| Blockade | Cuts trade and bank transfers, not production or existing stockpiles; can be broken by a naval victory | WFS-010, WFS-030 |
| Missile/nuke one-use | Launchers and warheads are consumed; no reload in the same battle | WFS-005, WFS-006 |
| Radiation | Nukes raise continent and world radiation, increasing disease and reducing food production for 100 turns | WFS-028 |
| Upkeep | Daily cash and food drain; war multiplier | WFS-011…WFS-017, WFS-022 |

The strategic choice P&W creates is therefore **what to stockpile and what to spend it on**, not **where to move it**. Within the examined warfare mechanics, a nation can be "cut off" only economically (blockade, resource exhaustion), not by a geographic supply line. This is unusually close to a mapless warfare design already.

### 7.9 Campaign lifecycle

The documented lifecycle is short and thin:

| Stage | P&W behaviour | Evidence |
|---|---|---|
| Declaration | Unilateral; attacker chooses war type; defender notified; both start with MAPs | WFS-022, WFS-003 |
| Active war | Turn-based exchange of actions; MAPs regenerate; resistance falls | WFS-022 |
| Victory | One side reaches 0 resistance; winner loots; loser loses infrastructure and goes beige for 2 days | WFS-031 |
| Peace | Either side offers peace; the other must accept; war ends without a victor | WFS-022 |
| Expiry | Wars "can last for up to 60 turns"; the exact expiry routine is undocumented | WFS-022, WFX-07 |
| Postwar | Beige protection from new defensive wars; existing wars may continue; beige recruitment buff | WFS-031, WFS-032, WFS-002 |
| Inactivity | Gray after 5 days; automatic deletion schedule at 31/60/90/97 days depending on cities and wars | WFS-032, WFS-001 |

There is **no campaign object** above the war. No alliance war, no coalition war, no front, no objective chain, no ceasefire period, no surrender conference and no enforced peace terms. A "campaign" in P&W is a set of independent nation-wars that players coordinate socially.

### 7.10 Protection and counterplay

| Layer | Rule | Evidence | Is it mechanical? |
|---|---|---|---|
| Beige after defeat | 2 days of immunity to new declarations | WFS-031, WFS-032 | Yes |
| New-nation beige | Up to 14 days | WFS-032 | Yes |
| Score window | 75%–250% | WFS-033 | Yes (250% unconfirmed) |
| Defensive slots | 3 | WFS-022 | Yes |
| Beige recruitment buff | +15% | WFS-002 | Yes |
| Fortify | 3 MAP, +25% attacker casualties | WFS-004 | Yes |
| War policies | Turtle, Fortress, Guardian, Arcane reduce damage/losses | WFS-023 | Yes |
| Projects | Iron Dome (30% missile shoot-down), Vital Defense (25% nuke nullification), Intelligence Agency, Spy Satellite | WFS-027, WFS-028, WFS-015 | Yes |
| Space-control counters | Naval Ground Defense / Naval Air Defense remove control on IT; any non-failure action breaks control | WFS-007, WFS-008, WFS-009 | Yes |
| Blockade breaking | Non-failure naval battle | WFS-030 | Yes |
| NAP / treaty | No mechanical enforcement documented | WFS-001, WFS-022; absence | **No** |
| Alliance protection | No mechanical rule; social and moderation only | WFS-001, WFS-022 | **No** |
| Vacation Mode | Allowed to avoid wars; using it to protect an alliance bank is a rule violation | WFS-001 | Policy, not combat |

The protection stack is **narrow and time-boxed**. Beige is the only true immunity, and it lasts 2 days after a loss (up to 14 days for a new nation). There is no lasting "new player" shield beyond that, no ally shield, no treaty shield and no score-based invulnerability below a threshold.

### 7.11 Losses and economic effects

| Loss channel | P&W rule | Evidence |
|---|---|---|
| Victory loot | Winner takes **10% of money** and **10% of all resources**; credits cannot be looted | WFS-031 |
| Victory infrastructure | Loser loses **up to 4%** of infrastructure in every city | WFS-031 |
| Alliance bank loot | `MIN((Nation Score / Alliance Score) × R%, 33%)`, R random 0–1 | WFS-031 |
| Ground loot | Formula based on attacking soldiers/tanks, victory factor, random 0.8–1.1, war type and war policy; cannot take more than 75% of cash or the last $1m | WFS-024 |
| Infrastructure damage | Per-action formulas with city caps | WFS-024, WFS-025, WFS-026, WFS-027 |
| Improvement destruction | Ground 10% on IT; naval 15% on IT; missile 2; nuke 4 | WFS-024, WFS-026, WFS-005, WFS-006 |
| Unit casualties | Per-action formulas; ground, air and naval differ | WFS-024, WFS-025, WFS-026 |
| Upkeep | Daily cash/food; wartime multiplier | WFS-011…WFS-017 |
| Resource burn | Per-battle gasoline/munitions | WFS-002, WFS-011…WFS-014 |
| Radiation | Disease up, food production down for 100 turns | WFS-028 |
| Reparations | **None.** No mechanical indemnity, no forced transfer, no occupation | WFS-022, WFS-037 (empty Peace page) |

Losses are therefore **destructive and transferable but not territorial**: infrastructure, units, stockpiles and cash move or disappear; cities, land and population do not change hands. There is no annexation, no occupation, no puppet state and no resource-region capture.

### 7.12 War termination and postwar

| Route | Mechanism | Evidence | Gap |
|---|---|---|---|
| Victory | Resistance to 0 | WFS-022, WFS-031 | None material |
| Negotiated peace | Offer Peace; opponent must accept | WFS-022 | No terms, no enforcement, no ceasefire timer |
| Expiry | 60-turn bound | WFS-022 | Exact routine undocumented (WFX-07) |
| Surrender | Not a distinct mechanic; losing is the surrender | WFS-031 | No terms |
| Reparations | Not a mechanic | WFS-037, WFS-022 | None |
| Postwar protection | Beige 2 days | WFS-031 | Existing wars may continue |
| Postwar recovery | Beige recruitment +15% | WFS-002 | Only while beige and war-free |

The **thin end** is the most important finding for Nation Supremacy. P&W can end a war, but it cannot conclude a **settlement**. There is no object that records "who won, what they demanded, what the loser conceded, and when the terms expire." Peace is binary: the war stops, or it does not. Any Nation Supremacy settlement framework must be designed, not ported.

### 7.13 Alliance warfare and military coordination

| Question | P&W answer | Evidence |
|---|---|---|
| Is there an alliance war entity? | **No.** Wars are nation-to-nation; alliances are social and economic containers | WFS-022, WFS-001 |
| Can an alliance declare war? | **No.** Only a nation can declare on a nation | WFS-022 |
| Is there delegated military command? | **No.** No role can spend another nation's MAPs, units or resources in war | WFS-022; absence |
| Is there a shared MAP pool? | **No.** MAPs are per nation per war | WFS-022 |
| Is there an alliance war chest for operations? | **No.** The alliance bank can be looted, but it does not fund attacks mechanically | WFS-031 |
| Can allies join a war? | Only by declaring their own separate wars | WFS-022 |
| Is there an alliance NAP enforcement? | **No.** No treaty mechanic enforces non-aggression; moderation handles slot filling | WFS-001, WFS-022; 08A `DPS-001` as prior project context only |
| What coordination exists? | External communication, shared intelligence, and the social norm of "counter-declaring" | **INFERRED** from the absence of mechanical coordination plus WFS-001 rule 4 |

This is a critical boundary for B-09. P&W's alliance warfare is **coordination without command**. Nation Supremacy's B-09 already forbids delegation and collective military powers (ALL-089/139/140, AX-18/AX-30, AT-E01). P&W therefore offers a **compatible precedent** for "allies fight alongside each other, not through each other," but it offers no model for an Alliance war, an Alliance NAP enforcement layer or an Alliance operations board — because it has none.

### 7.14 Espionage adjacent to war

Espionage is a separate action economy, not a MAP action:

| Property | P&W rule | Evidence |
|---|---|---|
| War required? | **No**; spies can act without a war | WFS-022, WFS-020 |
| MAP cost | 0 | WFS-022 |
| Frequency | Once per day; twice with Intelligence Agency | WFS-022, WFS-015 |
| Range | 40%–250% of score | WFS-033 |
| Cost | Cash per operation; safety level sets price and success | WFS-029 |
| Operations | Intelligence; sabotage infrastructure, soldiers, tanks, aircraft, ships; assassinate spies; sabotage missile; sabotage nuclear weapon | WFS-029 |
| Failure | At least 1% caught; at least 1% failure; attacker loses spies on failure | WFS-029 |
| Counters | Defending spies; Covert/Arcane war policies; Intelligence Agency | WFS-029, WFS-023 |

Espionage matters to Prompt 10 because it is the only **pre-war and parallel-war** action that can degrade a nation's military without a declaration. It is also the source of a distinct abuse category (spy slot filling, WFS-001 rule 5).

### 7.15 Abuse and integrity rules specific to warfare

P&W's Game Rules contain a substantial warfare-integrity layer (WFS-001). The rules most relevant to Prompt 10 are:

| Rule | Prohibition | Relevance to warfare design |
|---|---|---|
| 1 | More than one nation per player; nation-sitting | Multi-accounting can multiply war slots and MAP pools |
| 2 | Same-network nations may not declare on the same target; bank use to evade trade restrictions is bannable | Network-based coordination is restricted, not banned |
| 4 | War slot filling: declaring without intent to fight; filling slots to shield a target; attacking allies; minimal attacks or Fortify-only "wars" | Directly targets the "declare to protect" exploit |
| 5 | Spy slot filling: espionage against allies or with minimal damage | Parallel to rule 4 |
| 6 | Bounty coordination | Removes a wartime economy exploit |
| 7 | Treasure transfer coordination through wars | Removes a war-as-transfer exploit |
| 8–10 | Automated trading, banking and gameplay; scripts that automate wars/attacks/espionage prohibited | Botting and scripted war is a named violation |
| 11–12 | Account selling; real-world transactions for in-game goods | Prevents externalising war outcomes |
| 15 | Coerced city deletion, including as a peace term | Directly constrains "settlement" demands |
| 16 | Protecting an alliance bank with Vacation Mode or a new nation's beige | Closes a bank-safety exploit |
| 17 | Exploit abuse; obligation to report | Covers unknown future war bugs |

The enforcement model is **moderation with points and expiry**, not automated prevention. There is no published detection system, no guarantee of detection, and several rules explicitly rely on moderator discretion (rules 4 and 17). Nation Supremacy's B-03 principles (least privilege, evidence standards, no IP-only permanent bans) are compatible with this posture but go further in specifying evidence and appeal.

---

## 8. Evidence-backed findings

Each finding states what the evidence supports, its class, the sources, a confidence level, and why it matters to Nation Supremacy. Findings are numbered `WFR-001`…`WFR-052`; they are research findings, not requirements.

| ID | Finding | Class | Sources | Confidence | Relevance to Nation Supremacy |
|---|---|---|---|---|---|
| **WFR-001** | P&W war is a bounded **resistance race** between two nations, not a territorial conquest. Victory is reducing the opponent's 100 resistance to 0. | OFFICIAL-DOC / P&W-WIKI | WFS-022, WFS-019 | High | Confirms a mapless war can be strategically legible without fronts |
| **WFR-002** | Declarations are **unilateral and instant**; the defender has no consent step. | P&W-WIKI | WFS-022, WFS-003 | High | NS must decide whether declaration requires consent; B-08 NAP already blocks some declarations |
| **WFR-003** | The attacker chooses one of **three war types** at declaration and cannot change it; the type sets both sides' damage and loot percentages. | OFFICIAL-DOC / P&W-WIKI | WFS-003, WFS-022 | High | A single pre-commitment choice is a candidate model for NS campaign posture |
| **WFR-004** | War types are **economic presets, not objectives**. There is no capture, regime-change, demilitarisation or reparations goal. | P&W-WIKI | WFS-022, WFS-003 | High | NS needs an explicit objective layer that P&W does not provide |
| **WFR-005** | Declarations are gated by a **score window** of 75%–250% (250% unconfirmed) and by **5 offensive / 3 defensive slots**. | P&W-WIKI | WFS-033, WFS-022 | Medium-High | A strength gate limits one-sided predation without a map |
| **WFR-006** | **MAPs are per war**, not per nation: each war starts at 6, regenerates 1 per 2-hour turn, caps at 12. | P&W-WIKI | WFS-022 | High | **Structurally different from D-015's single national pool**; 10B must choose, not assume |
| **WFR-007** | A war lasts **at most 60 turns (5 days)**; the expiry routine itself is not documented. | P&W-WIKI | WFS-022 | High for the bound; low for the routine | A hard time bound prevents infinite attrition and is a candidate off-ramp |
| **WFR-008** | Resistance is **100 per side per war** and is independent of national size, score or cities. | P&W-WIKI | WFS-022 | High | A flat pool equalises wars between unequal economies |
| **WFR-009** | Battles resolve through **three rolls** of 40%–100% of combat value; 3/2/1/0 rolls won map to Immense Triumph / Moderate Success / Pyrrhic Victory / Utter Failure. | P&W-WIKI | WFS-022, WFS-024, WFS-025, WFS-026 | High | A bounded-randomness model with readable tiers |
| **WFR-010** | Ground, air and naval combat values are **soldiers + tanks**, **aircraft × 3**, and **ships × 4** respectively. | P&W-WIKI | WFS-024, WFS-025, WFS-026 | High | Simple force aggregates suit a symbolic world |
| **WFR-011** | **Ground Control** lets tanks destroy aircraft on later victories and is broken by a non-failure ground attack, a third party or a naval ground-defense action. | OFFICIAL-DOC / P&W-WIKI | WFS-008, WFS-022 | High | A non-geographic "control" state that is contestable every turn |
| **WFR-012** | **Air Superiority** halves enemy tank combat value and is broken by a non-failure airstrike, a third party or a naval air-defense action. | OFFICIAL-DOC / P&W-WIKI | WFS-009, WFS-022 | High | A force-multiplier state, not a territory |
| **WFR-013** | **Blockade** blocks trade and bank transfers but not production or existing stockpiles, and is broken by a naval victory. | OFFICIAL-DOC / P&W-WIKI | WFS-010, WFS-030 | High | Economic strangulation without a geographic theatre |
| **WFR-014** | **Fortify** costs 3 MAP, does not change resistance and adds **+25%** to attacker casualties until the fortified nation attacks. | OFFICIAL-DOC | WFS-004 | High | A cheap defensive counterplay that trades tempo for survival |
| **WFR-015** | There are exactly **nine military actions**: five resistance-reducing, one defensive, one espionage, one peace offer, one log. | P&W-WIKI | WFS-022 | High | A small action set is legible to both sides |
| **WFR-016** | **Airstrike MAP cost and resistance reduction are not stated** on any examined page; the wiki documents its formula but not its price. | P&W-WIKI (absence) | WFS-018, WFS-025, WFS-022 | High that it is undocumented; value **UNVERIFIED** | A direct evidence gap; do not import a guessed airstrike cost |
| **WFR-017** | **Missiles** cost 8 MAP, remove 18 resistance, destroy 2 improvements and are city-targeted. | OFFICIAL-DOC | WFS-005 | High | A high-cost precision action; candidate for a strategic strike |
| **WFR-018** | **Nuclear weapons** cost 12 MAP, remove 25 resistance, destroy 4 improvements and create radiation for 100 turns. | OFFICIAL-DOC / P&W-WIKI | WFS-006, WFS-028 | High | The least MAP-efficient attack but the most destructive |
| **WFR-019** | **Improvement destruction** is probabilistic: 10% per Immense Triumph ground battle, 15% per Immense Triumph naval battle, deterministic 2 for missiles and 4 for nukes. | P&W-WIKI / OFFICIAL-DOC | WFS-024, WFS-026, WFS-005, WFS-006 | High | Permanent-ish damage without city loss |
| **WFR-020** | **Victory loot** is 10% of money and 10% of all resources; credits are immune. | P&W-WIKI | WFS-031 | Medium-High | A bounded transfer, not confiscation; aligns with B-04 conservation only if sourced from the loser |
| **WFR-021** | **Victory infrastructure loss** is up to 4% in every city. | P&W-WIKI | WFS-031 | Medium-High | Damages development without destroying cities |
| **WFR-022** | **Alliance bank loot** is `MIN((Nation Score / Alliance Score) × R%, 33%)`, R random 0–1. | P&W-WIKI | WFS-031 | Medium | A rare case of alliance-level economic exposure |
| **WFR-023** | **No reparations, indemnity, occupation or forced transfer** exists as a war-ending mechanic. | P&W-WIKI + absence | WFS-022, WFS-037 | High | Prompt 10 must design settlement terms from scratch |
| **WFR-024** | **Peace requires mutual acceptance** of an Offer Peace; there is no ceasefire timer or partial peace. | P&W-WIKI | WFS-022 | High | Mutual consent is a candidate off-ramp |
| **WFR-025** | Defeat sends the loser to **beige for 2 days**, protected from new declarations but not from existing wars. | P&W-WIKI | WFS-031, WFS-032 | High | A short, bounded post-defeat shield |
| **WFR-026** | A **new nation** may remain beige for up to 14 days and cannot return once it leaves. | P&W-WIKI | WFS-032 | High | A long initial shield; B-03 uses a shorter 7-day model |
| **WFR-027** | **Gray** follows beige or 5 days of inactivity; gray nations are **not** protected from attack and receive no colour bonus. | P&W-WIKI | WFS-032 | High | Inactivity does not create invulnerability |
| **WFR-028** | **No treaty or NAP is mechanically enforced** in P&W; non-aggression is social and moderated. | P&W-WIKI + absence; 08A prior context | WFS-001, WFS-022 | High | B-08/B-09 go beyond P&W by making NAPs mechanical |
| **WFR-029** | There is **no alliance war entity** and no delegated military command. | P&W-WIKI + absence | WFS-022, WFS-001 | High | Confirms B-09's national-sovereignty direction |
| **WFR-030** | **No shared MAP or resource pool** exists for allies; each nation fights with its own units, MAPs and stockpiles. | P&W-WIKI | WFS-022 | High | No precedent for collective military powers |
| **WFR-031** | **No geographic supply line, distance, depot, convoy or encirclement** exists; logistics is national inventory. | P&W-WIKI + absence | WFS-022, WFS-030 | High | The strongest evidence that mapless logistics is viable |
| **WFR-032** | **Per-battle resource burn** is the logistics mechanic: tanks 0.01 gas/0.01 munitions; aircraft 0.25/0.25; ships 1/1.75; armed soldiers 0.0002 munitions. | OFFICIAL-DOC | WFS-002, WFS-012, WFS-013, WFS-014 | High | A clean model for B-04 resource coupling |
| **WFR-033** | **Blockade cuts trade and bank access, not production**, and can be broken by a naval victory. | OFFICIAL-DOC / P&W-WIKI | WFS-010, WFS-030 | High | Economic pressure that is recoverable |
| **WFR-034** | **No power** prevents troop purchases but not military actions with existing units. | P&W-WIKI | WFS-030 | Medium | A dependency that is softer than it first appears |
| **WFR-035** | P&W has **no readiness statistic**; readiness is emergent from units, resources, MAPs and war policy. | P&W-WIKI + absence | WFS-022, WFS-023 | High | NS may need an explicit readiness concept; P&W does not supply one |
| **WFR-036** | Recruitment is **daily and building-capped**: barracks 1,000/day (3,000 hold), factory 50/day (250), hangar 3/day (15), drydock 1/day (5), spies 2/day (50). | OFFICIAL-DOC | WFS-011…WFS-015 | High | Military power is gated by city development |
| **WFR-037** | **Wartime upkeep** is about 1.5× peacetime for soldiers, tanks and aircraft, and 1.515× for ships. | OFFICIAL-DOC / P&W-WIKI | WFS-011…WFS-014, WFS-002 | High | War has a continuous economic cost, not just a one-off build cost |
| **WFR-038** | The **July 2025 rebalance** raised aircraft and missile/nuke costs, changed ship operations, and added the beige recruitment buff. | OFFICIAL-DOC | WFS-002 | High | Unit pages lag the live rules; source currency matters |
| **WFR-039** | **Military research** gives permanent upgrades to unit caps, purchase costs and upkeep, and contributes to nation score. | OFFICIAL-DOC | WFS-002 | High | A long-term military progression layer P&W added in 2025 |
| **WFR-040** | There are **10 war policies** in 5 counterpart pairs; changing costs nothing but has a **60-turn cooldown**. | P&W-WIKI | WFS-023 | Medium-High | A posture choice with a long lock-in |
| **WFR-041** | **War policies** alter damage, loot, improvement destruction, espionage success and starting MAPs (Blitzkrieg/Fortress). | P&W-WIKI | WFS-023 | Medium-High | Multiple small modifiers rather than one dominant strategy |
| **WFR-042** | **National projects** are significant combat modifiers: Iron Dome (30% missile interception), Vital Defense (25% nuke nullification), Pirate Economy (+1 offensive slot), Intelligence Agency/Spy Satellite (spies). | OFFICIAL-DOC / P&W-WIKI | WFS-027, WFS-028, WFS-022, WFS-015 | High | Permanent strategic choices shape war capability |
| **WFR-043** | **Espionage is a separate daily economy** with no MAP cost, no war requirement and a wider score range (40%–250%). | OFFICIAL-DOC / P&W-WIKI | WFS-020, WFS-029, WFS-033 | High | A second action currency; D-024 forbids NS sharing one currency, so espionage needs its own budget |
| **WFR-044** | **Espionage can degrade military capability without a declaration** (sabotage units, missiles, nukes; assassinate spies). | P&W-WIKI | WFS-029 | High | Pre-war coercion and intelligence are part of the conflict space |
| **WFR-045** | Espionage has **at least 1% caught and 1% failure** chances; failure kills attacking spies by a published formula. | P&W-WIKI | WFS-029 | Medium | Covert action carries a readable risk |
| **WFR-046** | **War slot filling, spy slot filling, bounty coordination and treasure-transfer coordination** are named violations, with moderator discretion and strike/point penalties. | OFFICIAL-DOC | WFS-001 | High | Confirms that "declare to shield" is an abuse category, not a strategy |
| **WFR-047** | **Same-network nations** may not declare on the same target; using alliance banks to evade network trade restrictions is bannable. | OFFICIAL-DOC | WFS-001 | High | A precedent for network-aware enforcement without banning shared networks |
| **WFR-048** | **Automated war declarations, attacks and espionage** are prohibited; scripts that only inform or provide an interface are generally allowed if a human triggers the action. | OFFICIAL-DOC | WFS-001 | High | A usable line between automation and assistance |
| **WFR-049** | **Coerced city deletion**, including as a peace term, is prohibited. | OFFICIAL-DOC | WFS-001 | High | Directly limits what a settlement may demand |
| **WFR-050** | **Inactivity deletion** is scheduled by city count: 31 days (1 city), 60 days (<3 cities), 90 days + Vacation Mode (1–19 cities), 97 days (not in Vacation Mode). | OFFICIAL-DOC | WFS-001 | High | Wars against inactive nations have a natural end |
| **WFR-051** | **War reasons are cosmetic** and have no gameplay effect. | P&W-WIKI | WFS-022 | High | Flavour text must not be mistaken for an objective or a casus belli |
| **WFR-052** | P&W's **warfare is already mapless**: the examined pages document no provinces, tiles, geographic adjacency, borders, physical troop movement, territorial capture or coordinates; cities are development and damage-allocation units, and continents do not create a battlefield. P&W still uses geographic concepts outside combat (continents, named cities). | P&W-WIKI + absence | WFS-022, WFS-028, WFS-031, WFS-032 | High | Strong precedent for Nation Supremacy's symbolic warfare; the geographic game-world concepts are not a warfare precedent |

---

## 9. Complete attack and operation matrix

The matrix covers all nine documented military actions plus the four naval attack options and the nine espionage operations. Each action is described with the same twenty fields so that no capability is silently omitted. "Not stated" means the examined pages do not state the value; it is **not** a zero.

### 9.0 Summary

| Action | MAP | Resistance (IT) | Prerequisite | Primary target | Control effect | Evidence |
|---|---|---|---|---|---|---|
| Ground Battle | 3 | 10 | 50 soldiers | Units, cash, infrastructure | Ground Control | WFS-019, WFS-022, WFS-024 |
| Airstrike | **Not stated** | **Not stated** | 3 aircraft | Aircraft, tanks, soldiers, ships, infrastructure, money | Air Superiority | WFS-018, WFS-025 |
| Naval Battle | 4 | 14 | 1 ship | Ships, infrastructure, improvements | Blockade | WFS-007, WFS-026 |
| Launch Missile | 8 | 18 | 1 missile + project | City infrastructure, 2 improvements | None | WFS-005, WFS-027 |
| Nuclear Attack | 12 | 25 | 1 nuke + project | City infrastructure, 4 improvements, radiation | None | WFS-006, WFS-028 |
| Fortify | 3 | 0 | None | Self | Fortified | WFS-004 |
| Espionage | 0 | 0 | Spies + cash | Units, infrastructure, missiles, nukes, intelligence | None | WFS-020, WFS-029 |
| Offer Peace | 0 | 0 | None | The war | Ends war if accepted | WFS-022 |
| Timeline | 0 | 0 | None | War log (read-only) | None | WFS-022 |

### 9.1 Ground Battle

| Field | Value |
|---|---|
| **1. Action** | Ground Battle |
| **2. Category** | Offensive; resistance-reducing |
| **3. MAP cost** | 3 |
| **4. Prerequisites** | At least 50 soldiers; soldiers and/or tanks; munitions optional for soldiers, required for tanks |
| **5. Minimum force** | 50 soldiers (WFS-019) |
| **6. Target selection** | The enemy nation. Infrastructure damage lands in the defender's **highest-infrastructure city**; loot comes from the defender's cash |
| **7. Resistance effect** | Immense Triumph **10**; Moderate Success and Pyrrhic Victory lower (exact values not stated on the examined pages); Utter Failure 0 |
| **8. Infrastructure effect** | `MAX(MIN((Attacking Soldiers − (Defending Soldiers × 0.5) × 0.000606061 + (Attacking Tanks − (Defending Tanks × 0.5)) × 0.01) × RAND(0.85,1.05) × (Victory Type / 3), City Infrastructure × 0.2 + 25), 0)` (WFS-024; parentheses transcribed as published and flagged in WFE-08) |
| **9. Improvement effect** | **10%** chance to destroy one improvement on an Immense Triumph, excluding power plants (WFS-019, WFS-022) |
| **10. Attacker casualties** | Soldier casualties `(DTSR × 0.0084) + (DTTR × 0.0092)`; tank casualties depend on which side wins the aggregate roll (WFS-024) |
| **11. Defender casualties** | Soldier casualties `(ATSR × 0.0084) + (ATTR × 0.0092)`; tank casualties complementary to the attacker's (WFS-024) |
| **12. Resource consumption** | Armed soldiers 0.0002 munitions each; tanks 0.01 gasoline + 0.01 munitions each (WFS-011, WFS-012, WFS-022) |
| **13. Loot** | `MaxMoneyStolen = (Attacking Soldiers × 1.1 + Attacking Tanks × 25.15) × VictoryFactor × RAND(0.8,1.1) × WarTypeFactor × WarPolicyFactor`; cannot exceed 75% of cash or take the last $1m (WFS-024) |
| **14. Space-control effect** | An Immense Triumph grants **Ground Control** and nullifies the defender's Ground Control in all wars; any non-failure victory nullifies the defender's Ground Control against the attacker (WFS-022, WFS-008) |
| **15. Victory dependence** | Fully dependent: damage, loot, casualties and control all scale with the victory tier |
| **16. Counterplay** | Defending soldiers/tanks; Fortify; Ground Control; Air Superiority (halves tanks); war policies; terrain is absent |
| **17. Evidence class** | OFFICIAL-DOC for cost and resistance; P&W-WIKI for formulas |
| **18. Sources** | WFS-019, WFS-022, WFS-024, WFS-011, WFS-012 |
| **19. Confidence** | High for mechanics; medium for formula transcription |
| **20. Mapless fit** | **Excellent.** No location, movement or frontage is required; the target is a nation and the damage lands in an abstract city |

### 9.2 Airstrike

| Field | Value |
|---|---|
| **1. Action** | Airstrike |
| **2. Category** | Offensive; resistance-reducing |
| **3. MAP cost** | **Not stated** on any examined page (WFX-09) |
| **4. Prerequisites** | Aircraft; gasoline and munitions |
| **5. Minimum force** | 3 aircraft (WFS-018) |
| **6. Target selection** | The player chooses a target class: aircraft, tanks, soldiers, ships, infrastructure or money. Aircraft casualties occur regardless of the class chosen |
| **7. Resistance effect** | **Not stated** on the examined pages; the wiki states that a victory reduces resistance but does not publish the per-tier values |
| **8. Infrastructure effect** | `MAX(MIN(Attacking Aircraft − (Defending Aircraft × 0.5) × 0.35353535 × RAND(0.85,1.05) × (Victory Type / 3), City Infrastructure × 0.5 + 100), 0)` (WFS-025) |
| **9. Improvement effect** | **None.** Airstrikes cannot destroy improvements (WFS-026 contrast, WFS-025) |
| **10. Attacker casualties** | Aircraft casualties occur on every strike; the targeted-unit formulas apply at 100% on IT, **70%** on MS, **40%** on PV and **0%** on UF (WFS-025) |
| **11. Defender casualties** | Depends on the target class: aircraft, tanks, soldiers or ships; infrastructure or money targets destroy value rather than units |
| **12. Resource consumption** | 0.25 gasoline + 0.25 munitions per aircraft per battle (WFS-013, WFS-022) |
| **13. Loot** | **None.** Aircraft never loot; targeting money **destroys** it (WFS-022, WFS-025) |
| **14. Space-control effect** | An Immense Triumph grants **Air Superiority** (enemy tanks at 50%) and nullifies the defender's Air Superiority in all wars; any non-failure victory nullifies the defender's Air Superiority against the attacker (WFS-022, WFS-009) |
| **15. Victory dependence** | High; casualties and control depend on the tier |
| **16. Counterplay** | Defending aircraft; Air Superiority; war policies; naval air-defense option; projects |
| **17. Evidence class** | OFFICIAL-DOC for targets; P&W-WIKI for the formula; **absence** for MAP and resistance |
| **18. Sources** | WFS-018, WFS-025, WFS-022 |
| **19. Confidence** | High for targets and formula; **unverified** for cost and resistance |
| **20. Mapless fit** | **Excellent.** Air power is a national capability, not a sortie from a base to a hex |

### 9.3 Naval Battle

| Field | Value |
|---|---|
| **1. Action** | Naval Battle |
| **2. Category** | Offensive; resistance-reducing |
| **3. MAP cost** | 4 |
| **4. Prerequisites** | At least 1 ship; gasoline and munitions |
| **5. Minimum force** | 1 ship (WFS-007) |
| **6. Target selection** | The enemy nation; four attack options in the July 2025 rebalance (see §9.10) |
| **7. Resistance effect** | Immense Triumph **14**, Moderate Success **11**, Pyrrhic Victory **8**, Utter Failure **0** (WFS-007) |
| **8. Infrastructure effect** | `MAX(MIN(Attacking Ships − (Defending Ships × 0.5) × 2.625 × RAND(0.85,1.05) × (Victory Type / 3), City Infrastructure × 0.5 + 25), 0)` (WFS-026) |
| **9. Improvement effect** | **15%** chance on an Immense Triumph (WFS-007, WFS-026) |
| **10. Attacker casualties** | `opponent's roll × 0.01375` per roll, across 3 rolls (WFS-026) |
| **11. Defender casualties** | `attacker's roll × 0.01375` per roll, across 3 rolls (WFS-026) |
| **12. Resource consumption** | **1 gasoline + 1.75 munitions** per ship per battle (WFS-002 supersedes WFS-022's older 2/3) |
| **13. Loot** | **None.** Ships cannot loot money (WFS-026) |
| **14. Space-control effect** | An Immense Triumph grants **Blockade** (trade and bank restrictions) (WFS-010, WFS-030) |
| **15. Victory dependence** | High; resistance, damage, improvement chance and blockade all depend on the tier |
| **16. Counterplay** | Defending ships; naval air/ground defense; a later naval victory; third-party Immense Triumph |
| **17. Evidence class** | OFFICIAL-DOC / P&W-WIKI |
| **18. Sources** | WFS-007, WFS-026, WFS-030, WFS-002 |
| **19. Confidence** | High for mechanics; high for the July 2025 resource values |
| **20. Mapless fit** | **Excellent.** "Sea control" is a national state, not a sea zone |

### 9.4 Launch Missile

| Field | Value |
|---|---|
| **1. Action** | Launch Missile |
| **2. Category** | Offensive; resistance-reducing; strategic strike |
| **3. MAP cost** | 8 |
| **4. Prerequisites** | At least 1 missile; Missile Launch Pad project |
| **5. Minimum force** | 1 missile |
| **6. Target selection** | A chosen enemy city and a chosen improvement type; power plants are **not** valid targets |
| **7. Resistance effect** | **18** (deterministic on a hit) (WFS-005) |
| **8. Infrastructure effect** | `MAX(MIN(RAND(300, MAX(350, Population Density × 3)), City Infrastructure × 0.3 + 100), 0)` (WFS-027); PWPedia describes more than 300 and a 350 cap, with reports of breaches (WFX-04) |
| **9. Improvement effect** | **2** improvements, deterministic; power plants excluded (WFS-005) |
| **10. Attacker casualties** | None; the missile is consumed |
| **11. Defender casualties** | No unit casualties documented; infrastructure and improvements only |
| **12. Resource consumption** | The missile itself; no in-battle resource cost (WFS-016) |
| **13. Loot** | None |
| **14. Space-control effect** | None |
| **15. Victory dependence** | None; a launched missile hits deterministically, subject to Iron Dome interception |
| **16. Counterplay** | Iron Dome (30% shoot-down; prevents 1 improvement), war policies, missile stockpile destruction via espionage |
| **17. Evidence class** | OFFICIAL-DOC |
| **18. Sources** | WFS-005, WFS-027, WFS-002 |
| **19. Confidence** | High for MAP, resistance and improvements; medium for the exact infrastructure formula |
| **20. Mapless fit** | **Good.** City targeting selects a development centre, not a coordinate or tile; it needs adaptation if NS cities are not attackable |

### 9.5 Nuclear Attack

| Field | Value |
|---|---|
| **1. Action** | Nuclear Attack |
| **2. Category** | Offensive; resistance-reducing; strategic strike |
| **3. MAP cost** | 12 |
| **4. Prerequisites** | At least 1 nuclear weapon; Nuclear Research Facility project |
| **5. Minimum force** | 1 nuclear weapon |
| **6. Target selection** | A chosen enemy city; improvement types are not chosen |
| **7. Resistance effect** | **25** (deterministic on a hit) (WFS-006) |
| **8. Infrastructure effect** | Documented as capped at **2,000** infrastructure (WFS-006); the exact roll is not published on the examined pages |
| **9. Improvement effect** | **4** improvements: two of any type and two non-power-plant, non-military; if those are unavailable, any improvement (WFS-006) |
| **10. Attacker casualties** | None; the warhead is consumed |
| **11. Defender casualties** | No direct unit casualties documented; radiation raises disease and lowers food production for 100 turns (WFS-028) |
| **12. Resource consumption** | The warhead itself; no in-battle resource cost (WFS-017) |
| **13. Loot** | None |
| **14. Space-control effect** | None |
| **15. Victory dependence** | None; deterministic hit, subject to Vital Defense |
| **16. Counterplay** | Vital Defense System (25% nullification; removes one non-power/non-military improvement), espionage against the stockpile, war policies |
| **17. Evidence class** | OFFICIAL-DOC / P&W-WIKI |
| **18. Sources** | WFS-006, WFS-028, WFS-002 |
| **19. Confidence** | High for MAP, resistance and improvements; medium for infrastructure |
| **20. Mapless fit** | **Good with caution.** Radiation is a global/continental effect; NS has no continents, so it would need a world-level or nation-level analogue |

### 9.6 Fortify

| Field | Value |
|---|---|
| **1. Action** | Fortify |
| **2. Category** | Defensive; non-resistance |
| **3. MAP cost** | 3 |
| **4. Prerequisites** | None |
| **5. Minimum force** | None |
| **6. Target selection** | Self |
| **7. Resistance effect** | None (WFS-004) |
| **8. Infrastructure effect** | None directly; reduces incoming casualties, not damage |
| **9. Improvement effect** | None |
| **10. Attacker casualties** | **+25%** while the nation is fortified (WFS-004) |
| **11. Defender casualties** | No documented change |
| **12. Resource consumption** | None |
| **13. Loot** | None |
| **14. Space-control effect** | Creates the **Fortified** state; ends when the fortified nation launches an offensive attack (WFS-022) |
| **15. Victory dependence** | None |
| **16. Counterplay** | Attack anyway and absorb the casualties; wait for the defender to attack; the state does not stack in effect |
| **17. Evidence class** | OFFICIAL-DOC |
| **18. Sources** | WFS-004, WFS-022 |
| **19. Confidence** | High |
| **20. Mapless fit** | **Excellent.** A pure defensive posture with no location |

### 9.7 Espionage

| Field | Value |
|---|---|
| **1. Action** | Espionage |
| **2. Category** | Covert; non-resistance |
| **3. MAP cost** | 0 |
| **4. Prerequisites** | Spies; cash; target within 40%–250% score range |
| **5. Minimum force** | 1 spy (implied); operation cost scales with spies and safety level |
| **6. Target selection** | Enemy nation; one of nine operations (see §9.11) |
| **7. Resistance effect** | None |
| **8. Infrastructure effect** | Sabotage Infrastructure destroys up to **34.5** infrastructure at 60 spies vs 0 in the target's highest-infrastructure city (WFS-029) |
| **9. Improvement effect** | None documented |
| **10. Attacker casualties** | On failure, `MIN(((1 / Odds of Success) × 5.36) × Attacking Spies, Attacking Spies)` spies are killed (WFS-029) |
| **11. Defender casualties** | Depends on the operation: 1–5% of soldiers/tanks/aircraft/ships; spies assassinated by formula; 1 missile or nuke destroyed |
| **12. Resource consumption** | Cash per operation; no MAP; no gasoline/munitions |
| **13. Loot** | None; intelligence reveals stockpiles rather than taking them |
| **14. Space-control effect** | None |
| **15. Victory dependence** | Probabilistic; safety level sets price and success; at least 1% caught and 1% failure |
| **16. Counterplay** | Defending spies; Covert/Arcane policies; Intelligence Agency; operations are once per day |
| **17. Evidence class** | OFFICIAL-DOC / P&W-WIKI |
| **18. Sources** | WFS-020, WFS-029, WFS-015, WFS-033 |
| **19. Confidence** | High for operations; medium for formulas |
| **20. Mapless fit** | **Excellent.** Espionage is already abstract and needs no territory |

### 9.8 Offer Peace

| Field | Value |
|---|---|
| **1. Action** | Offer Peace |
| **2. Category** | Diplomatic; war-termination |
| **3. MAP cost** | 0 |
| **4. Prerequisites** | An active war |
| **5. Minimum force** | None |
| **6. Target selection** | The opponent in that war |
| **7. Resistance effect** | None |
| **8. Infrastructure effect** | None |
| **9. Improvement effect** | None |
| **10. Attacker casualties** | None |
| **11. Defender casualties** | None |
| **12. Resource consumption** | None |
| **13. Loot** | None; peace is not a victory and pays no loot |
| **14. Space-control effect** | Ends the war; control states end with it |
| **15. Victory dependence** | None |
| **16. Counterplay** | The opponent can refuse; there is no forced peace |
| **17. Evidence class** | P&W-WIKI |
| **18. Sources** | WFS-022, WFS-037 |
| **19. Confidence** | High for the mechanic; low for any settlement detail (none documented) |
| **20. Mapless fit** | **Excellent.** A bilateral stop requiring no geographic targeting |

### 9.9 Timeline

| Field | Value |
|---|---|
| **1. Action** | Timeline |
| **2. Category** | Information |
| **3. MAP cost** | 0 |
| **4. Prerequisites** | An active war |
| **5. Minimum force** | None |
| **6. Target selection** | The war log |
| **7. Resistance effect** | None |
| **8. Infrastructure effect** | None |
| **9. Improvement effect** | None |
| **10. Attacker casualties** | None |
| **11. Defender casualties** | None |
| **12. Resource consumption** | None |
| **13. Loot** | None |
| **14. Space-control effect** | None |
| **15. Victory dependence** | None |
| **16. Counterplay** | None |
| **17. Evidence class** | P&W-WIKI |
| **18. Sources** | WFS-022 |
| **19. Confidence** | High |
| **20. Mapless fit** | **Excellent.** A readable public record is a requirement for NS transparency |

### 9.10 Naval attack options (July 2025 rebalance)

The July 2025 update gave ships **four attack options**, each trading infrastructure damage against casualties or control (WFS-002):

| Option | Infrastructure damage | Naval casualties | Special effect |
|---|---|---|---|
| **Target Infrastructure** | Original infrastructure damage | **−30%** naval casualties | None |
| **Target Ships** | **−30%** infrastructure | **+30%** naval casualties | None |
| **Naval Ground Defense** | **−30%** infrastructure | **−30%** naval casualties | Removes the enemy's **Ground Control** on an Immense Triumph |
| **Naval Air Defense** | **−30%** infrastructure | **−30%** naval casualties | Removes the enemy's **Air Superiority** on an Immense Triumph |

Additionally, **all naval battles have 20% more ship casualties** than before, and ship operating costs fell to **1 gasoline + 1.75 munitions** per ship per battle (WFS-002). This is a rare case of an action whose **strategic purpose** is chosen at execution, not only its target.

### 9.11 Espionage operations

| Operation | Effect | Source |
|---|---|---|
| **Intelligence** | Reveals enemy stockpiles and military information | WFS-029 |
| **Sabotage Infrastructure** | Up to 34.5 infrastructure in the highest-infrastructure city (60 spies vs 0) | WFS-029 |
| **Sabotage Soldiers** | 1%–5% of total soldiers destroyed | WFS-029 |
| **Sabotage Tanks** | 1%–5% of total tanks destroyed | WFS-029 |
| **Sabotage Aircraft** | 1%–5% of total aircraft destroyed | WFS-029 |
| **Sabotage Ships** | 1%–5% of total ships destroyed | WFS-029 |
| **Assassinate Spies** | `RAND(85%,105%) × [Attacking Spies − (Defending Spies × 0.4)] × 0.335`, capped at `(Defending Spies × 0.25) + 4` | WFS-029 |
| **Sabotage Missile** | Destroys 1 missile; 25% chance of one additional missile | WFS-029 |
| **Sabotage Nuclear Weapon** | Destroys 1 nuclear weapon | WFS-029 |

All operations have **at least 1% caught** and **at least 1% failure** chances; failure kills attacking spies by the published formula (WFS-029). Safety level changes price and success rate; it does not eliminate risk.

---

## 10. Battle-resolution and formula evidence

This section records the formula evidence without approving any number for Nation Supremacy. It is a research register (`WFE-01`…`WFE-16`), not a B-10 formula register.

| ID | Quantity | Published formula / value | Variables | Source | Confidence | Issue |
|---|---|---|---|---|---|---|
| **WFE-01** | Resistance pool | 100 per side per war | None | WFS-022 | High | Flat pool ignores nation size |
| **WFE-02** | MAP start / regen / cap | 6 / +1 per 2-hour turn / 12 | War policy modifies start (5 or 7) | WFS-022 | High | Per-war pool, not national |
| **WFE-03** | War duration | Up to 60 turns (5 days) | None | WFS-022 | High for bound; low for routine | Expiry routine undocumented |
| **WFE-04** | Ground army value | `Unarmed Soldiers × 1 + Armed Soldiers × 1.75 + Tanks × 40` | Unit counts | WFS-024 | High | "Armed" means munitions-equipped |
| **WFE-05** | Airforce value | `Aircraft × 3` | Aircraft count | WFS-025 | High | — |
| **WFE-06** | Naval value | `Ships × 4` | Ship count | WFS-026 | High | — |
| **WFE-07** | Roll resolution | Three rolls per side, each `RAND(40%,100%)` of value; 3/2/1/0 wins → IT/MS/PV/UF | Rolls | WFS-022, WFS-024, WFS-025, WFS-026 | High | Bounded randomness; no published seed or UI odds |
| **WFE-08** | Ground infrastructure damage | `MAX(MIN((AS − DS×0.5)×0.000606061 + (AT − DT×0.5)×0.01) × RAND(0.85,1.05) × (VT/3), City Infra×0.2 + 25), 0)` | AS/DS soldiers, AT/DT tanks, VT | WFS-024 | Medium | Parentheses in the published text are ambiguous; the wiki may have mis-transcribed the nesting |
| **WFE-09** | Airstrike infrastructure damage | `MAX(MIN((AA − DA×0.5)×0.35353535 × RAND(0.85,1.05) × (VT/3), City Infra×0.5 + 100), 0)` | AA/DA aircraft, VT | WFS-025 | Medium | Same transcription concern |
| **WFE-10** | Naval infrastructure damage | `MAX(MIN((AShips − DShips×0.5)×2.625 × RAND(0.85,1.05) × (VT/3), City Infra×0.5 + 25), 0)` | Ships, VT | WFS-026 | Medium | Same transcription concern |
| **WFE-11** | Ground loot | `(AS×1.1 + AT×25.15) × VT × RAND(0.8,1.1) × WarTypeFactor × WarPolicyFactor`; cap 75% cash, floor $1m | AS/AT, VT, factors | WFS-024 | High for structure; medium for constants | Constants are community-derived |
| **WFE-12** | Ground casualties | `Attacker Soldier Casualties += DTSR×0.0084 + DTTR×0.0092`; tank formulas depend on aggregate roll | Rolls, unit counts | WFS-024 | Medium | Typo in published `DTTR` description ("attacking tank army value") |
| **WFE-13** | Airstrike unit casualties | 100% of formula on IT, 70% on MS, 40% on PV, 0% on UF | VT | WFS-025 | High | Applied to targeted class |
| **WFE-14** | Naval casualties | `opponent's roll × 0.01375` per side per roll; 3 rolls | Rolls | WFS-026 | Medium | July 2025 adds 20% casualties (WFS-002), so the current multiplier may differ |
| **WFE-15** | Missile infrastructure damage | `MAX(MIN(RAND(300, MAX(350, PopDensity×3)), City Infra×0.3 + 100), 0)` | Pop density, city infra | WFS-027 | Medium | Conflicts with PWPedia's "more than 300 / cap 350" prose (WFX-04) |
| **WFE-16** | Victory and bank loot | Money 10%, resources 10%, infra 4%; alliance bank `MIN((Nation Score / Alliance Score) × R%, 33%)` | Scores, R | WFS-031 | Medium | Community-sourced; no official formula page examined |

**What the formula evidence establishes.** P&W's battle model is a **bounded-random comparison of aggregate force values**. The randomness is narrow (40%–100% per roll), the tiers are discrete, and the economic consequences are formula-driven. A defender with fewer units can still win a roll exchange; a larger force is advantaged but not guaranteed. This is a readable, low-variance model suitable for a 2-hour turn game.

**What it does not establish.** The published formulas do not tell us:
- whether the live game uses the same constants after the July 2025 rebalance;
- how the server orders simultaneous actions within a turn;
- whether rolls are independent or seeded per battle;
- how the UI explains an outcome to a player;
- how multi-war MAP pools are displayed and refreshed.

Those are implementation questions for 10B and 10C, not research facts.

---

## 11. Military readiness and resource research

### 11.1 The readiness problem

P&W has **no readiness statistic**. A nation is "ready" to the extent that it has (a) units, (b) the resources those units burn, (c) MAPs in the relevant war, and (d) a war policy that suits the fight. Readiness is therefore an **emergent state**, not a tracked value (WFR-035). Nation Supremacy must decide whether to keep that emergence or to introduce an explicit readiness layer. The D-015 Operations Points pool already supplies one explicit layer (action tempo); it does not supply unit condition.

### 11.2 Readiness inputs observed in P&W

| Input | How it gates war | Evidence |
|---|---|---|
| Unit count | Damage, casualties, loot and control | WFS-024, WFS-025, WFS-026 |
| Unit composition | Soldiers enable ground attacks; tanks add value; aircraft enable airstrikes; ships enable naval battles | WFS-019, WFS-018, WFS-007 |
| Munitions | Armed soldiers +75% effectiveness; tanks and aircraft require it | WFS-011, WFS-012, WFS-013 |
| Gasoline | Tanks, aircraft and ships require it | WFS-012, WFS-013, WFS-014 |
| Steel/aluminium | Required to build tanks, ships and aircraft | WFS-030 |
| Power | Required to operate military buildings; without it, no new troop purchases | WFS-030 |
| MAPs | Required for every attack and Fortify | WFS-022 |
| War policy | Damage, loot, casualties, starting MAPs, espionage | WFS-023 |
| Projects | Iron Dome, Vital Defense, Intelligence Agency, Pirate Economy, Military Research Center | WFS-027, WFS-028, WFS-015, WFS-022, WFS-002 |
| Military research | Permanent unit-cap, purchase-cost and upkeep upgrades | WFS-002 |
| Beige status | +15% recruitment while beige and war-free | WFS-002 |

### 11.3 Unit economics as a readiness cost

| Unit | Build cost | Wartime upkeep/day | Battle resource | Approximate wartime daily cost if idle |
|---|---|---|---|---|
| Soldier | $5 | $1.88 + 1 food/500 | 0.0002 munitions per armed soldier | Low cash, food-intensive at scale |
| Tank | $60 + 0.5 steel | $75 | 0.01 gasoline + 0.01 munitions | Moderate |
| Aircraft | $4,000 + 10 aluminium | $1,000 | 0.25 gasoline + 0.25 munitions | High |
| Ship | $50,000 + 30 steel | $5,000 | 1 gasoline + 1.75 munitions | Very high |
| Spy | $50,000 | $2,400 | None (cash per op) | High |
| Missile | $150,000 + 100 aluminium + 75 munitions + 75 gasoline | $31,500 | None to fire | Very high |
| Nuclear weapon | $1.75m + 1,000 aluminium + 500 gasoline + 500 uranium | $52,500 | None to fire | Extreme |

The important design property is the **ratio**, not the absolute numbers: a ship costs roughly 12.5× an aircraft to build and 5× to keep, while contributing 4 combat value versus an aircraft's 3. P&W balances this with the ship's blockade and improvement-destruction utility. Nation Supremacy should decide its own ratios from its own economy, not import these.

### 11.4 Recruitment and mobilisation

Recruitment is **daily**, not per turn: barracks 1,000 soldiers/day, factories 50 tanks/day, hangars 3 aircraft/day, drydocks 1 ship/day, spies 2/day, missiles 2/day, nukes 1/day (WFS-011…WFS-017). This means mobilisation is measured in **days**, while combat is measured in **2-hour turns**. A nation cannot rebuild a destroyed air force within a war; it fights the war with what it had at declaration plus a slow trickle. That mismatch is the core of P&W's strategic pacing, and it is a candidate model for Nation Supremacy's "bounded war" requirement.

### 11.5 Military research and projects

The July 2025 update added **military research**: permanent upgrades to unit caps, purchase costs and upkeep, purchased with cash and resources, resettable for 1 credit with cash refunded but not resources (WFS-002). It also added two projects: **Military Research Center** (enables research; +2 project slots) and **Military Doctrine** (−5% research cost). Research contributes to nation score (4 points per air upgrade, 3 per ground, 2 per naval) (WFS-002).

This is a **long-term readiness** layer separate from unit count. It lets a nation specialise without buying more cities, which is directly relevant to Nation Supremacy's design goal of avoiding a single dominant "buy more cities" ladder.

### 11.6 The DEFCON gap

The War Policy page refers to DEFCON as a factor in choosing a policy (WFS-023), but the DEFCON article is empty (WFS-038). No DEFCON mechanic, level, or effect is documented on the examined pages. Any claim that DEFCON changes combat values would be **UNVERIFIED** and must not be used.

---

## 12. Supply and logistics findings

### 12.1 What P&W's logistics is

P&W's logistics is **inventory-based, national and instantaneous**. Resources exist in a national stockpile; units consume them at the moment of battle; a blockade or a resource shortage can stop production or offensive use, but nothing travels between places. There is no map distance to traverse, no convoy to intercept, no depot to capture and no supply line to cut (WFR-031).

### 12.2 The five logistics levers

| Lever | Mechanism | Evidence | Strategic effect |
|---|---|---|---|
| **Stockpile depth** | Build and hold gasoline, munitions, steel, aluminium before war | WFS-030 | Rewards preparation; punishes just-in-time economies |
| **Per-battle burn** | Each battle consumes resources per unit committed | WFS-002, WFS-011…WFS-014 | Large armies consume faster; small elite forces are cheaper per battle |
| **Blockade** | Cuts trade and bank transfers, not production | WFS-010, WFS-030 | Isolates a nation from alliance resupply but not from its own stockpile |
| **Power** | No power → no military building operation → no new troop purchases | WFS-030 | A soft gate: existing units can still act |
| **Strategic strikes** | Missiles/nukes destroy infrastructure and improvements; espionage destroys stockpiles and launchers | WFS-005, WFS-006, WFS-029 | Can erode the industrial base that produces resupply |

### 12.3 What is absent

- No distance, route, adjacency or theatre.
- No supply-line unit, convoy, depot or stockpile location.
- No encirclement, siege or cut-off state.
- No attrition from being blockaded beyond the loss of trade/bank access.
- No fuel cost for movement (there is no movement).
- No food consumption by units in battle beyond daily upkeep.
- No ammunition stockpile separate from munitions; no fuel stockpile separate from gasoline.
- No repair or replacement delay beyond daily recruitment.

### 12.4 Why this matters for Nation Supremacy

Nation Supremacy's mapless constraint removes geographic warfare but not **scarcity**. P&W demonstrates that scarcity can be created entirely through:
1. **build caps** (how many units a city can support),
2. **daily recruitment** (how fast losses can be replaced),
3. **per-battle resource burn** (what a fight costs),
4. **upkeep** (what standing ready costs), and
5. **blockade/trade restriction** (what allies can send).

Those five levers are sufficient to make logistics strategically meaningful without a single coordinate. A Nation Supremacy design that uses them can honestly claim "supply and strategic choice" while remaining mapless. A design that tries to import "supply lines" would violate the mapless constraint and should be rejected.

---

## 13. Campaign lifecycle

### 13.1 The lifecycle P&W actually implements

P&W implements a **nation-war lifecycle**, not a campaign lifecycle. The stages are:

| Stage | Trigger | What happens | What the player sees | Evidence |
|---|---|---|---|---|
| **S0 — Pre-declaration** | Player chooses a target in range | Score gate and slot check; war type chosen; optional reason typed | Target list, score, slot count, war-type selector | WFS-022, WFS-033; declaration screen not observed (WFX-12) |
| **S1 — Declaration** | Attacker confirms | War created; both sides start at 6 MAPs (5/7 with policies); resistance 100 each | New war on the wars list; MAP count; timeline entry | WFS-022 |
| **S2 — Opening** | First turns | Both sides spend MAPs; attacks resolve; control states may be taken | Per-attack results; resistance bars; control badges | WFS-022, WFS-008…WFS-010 |
| **S3 — Attrition** | Turns 1–59 | MAPs regenerate; resources burn; units die; infrastructure falls; loot moves | Resistance, MAPs, losses, loot, blockade status | WFS-022, WFS-024…WFS-026 |
| **S4 — Endgame** | Resistance low or turn 60 near | One side seeks the final hit; the other fortifies, defends or offers peace | Resistance close to 0; peace offer | WFS-022, WFS-004 |
| **S5a — Victory** | Resistance reaches 0 | War ends; winner loots; loser loses infrastructure and goes beige 2 days | Victory message with loot list and infrastructure loss | WFS-031 |
| **S5b — Peace** | Offer accepted | War ends with no victor and no loot | War removed/closed; no settlement record | WFS-022 |
| **S5c — Expiry** | Turn 60 | War ends (routine undocumented) | Expected war end; no official detail | WFS-022, WFX-07 |
| **S6 — Beige** | Defeat | 2 days of immunity to new declarations; beige recruitment +15% if war-free | Beige status; immunity notice | WFS-031, WFS-032, WFS-002 |
| **S7 — Postwar** | Beige ends | Nation returns to gray/normal; can be declared on again; existing wars may continue | Normal status; new declarations possible | WFS-032 |

### 13.2 Lifecycle properties

| Property | P&W behaviour | Consequence |
|---|---|---|
| **Entry** | Unilateral; no defender consent | A defender can be in a war before logging in |
| **Exit** | Victory, mutual peace, expiry, or (undocumented) abandonment | No unilateral exit; a losing side cannot simply leave |
| **Duration** | Bounded at 60 turns | Prevents infinite wars; caps attrition |
| **Escalation** | A nation can open up to 5 offensive wars | A "campaign" is a bundle of wars, not an object |
| **De-escalation** | Offer Peace; Fortify; blockade breaking; control breaking | Several small off-ramps, no formal ceasefire |
| **Record** | Timeline per war; no campaign record | History is war-scoped, not campaign-scoped |
| **Postwar** | 2-day beige; no terms; no reparations | The war ends, but the dispute is not settled |
| **Persistence** | Existing wars may continue after defeat | Beige protects against new wars, not old ones |

### 13.3 The missing campaign layer

P&W has no object that corresponds to a **campaign**: no shared objective, no coalition membership, no front, no phase, no ceasefire, no surrender, no terms and no postwar enforcement. A "campaign" is an emergent label players apply to a cluster of wars. This is both a warning and an opportunity for Nation Supremacy:

- **Warning:** A design that assumes P&W has a campaign lifecycle will invent mechanics that P&W never validated.
- **Opportunity:** Nation Supremacy can define a campaign object that is still mapless — a bounded, multi-nation conflict with objectives, phases and a settlement — without importing geography.

Prompt 10's "done when" test — two nations can fight a bounded war with a readable outcome, a way to stop, and no infinite one-sided attrition — is satisfied by P&W's **war** lifecycle. It is not satisfied at the **campaign** level, because P&W has no campaign level.

---

## 14. Protection and counterplay

### 14.1 Protection layers

| Layer | Who is protected | Duration | What it blocks | What it does not block | Evidence |
|---|---|---|---|---|---|
| **New-nation beige** | Every new nation unless it opts into combat | Up to **14 days** | New declarations | Existing wars (none at creation); leaving beige is permanent | WFS-032 |
| **Defeat beige** | Loser of a war | **2 days** | New declarations | Existing wars may continue | WFS-031, WFS-032 |
| **Score window** | Every nation | Continuous | Declarations outside 75%–250% (250% unconfirmed) | Declarations inside the window | WFS-033 |
| **Defensive slots** | Every nation | Continuous | More than 3 simultaneous defensive wars | Offensive wars the nation starts | WFS-022 |
| **Vacation Mode** | Any nation | Player-selected | Attacks while on vacation (implied) | Using it to protect an alliance bank is a violation | WFS-001 |
| **Gray** | Inactive or post-beige | Until changed | Nothing; gray is attackable | — | WFS-032 |
| **NAP / treaty** | None mechanically | — | Nothing in P&W | — | WFR-028 |
| **Alliance** | None mechanically | — | Nothing in P&W | — | WFR-029 |

### 14.2 Counterplay layers

| Counter | Counters what | Cost | Evidence |
|---|---|---|---|
| **Fortify** | Incoming casualties (+25%) | 3 MAP, loses tempo | WFS-004 |
| **Ground Control** | Enemy aircraft; enemy ground control | Requires an Immense Triumph ground win | WFS-008 |
| **Air Superiority** | Enemy tanks (50%) | Requires an Immense Triumph airstrike | WFS-009 |
| **Blockade** | Enemy trade and bank access | Requires an Immense Triumph naval win | WFS-010 |
| **Naval Ground/Air Defense** | Enemy Ground Control / Air Superiority | One naval attack option; −30% infrastructure | WFS-002 |
| **War policies** | Damage, loot, improvement loss, espionage | 60-turn lock-in | WFS-023 |
| **Projects** | Missiles, nukes, spies, slots | Build cost and project slot | WFS-027, WFS-028, WFS-022 |
| **Espionage** | Units, infrastructure, missiles, nukes | Cash and spies; daily limit | WFS-029 |
| **Offer Peace** | The war itself | Requires opponent acceptance | WFS-022 |
| **Score management** | Being in range of larger nations | Economic/development trade-off | WFS-033 |

### 14.3 What the protection stack does well

1. **It prevents immediate re-farming after a loss.** Two days of beige is short but real.
2. **It gives a new player a long runway.** Fourteen days is generous by genre standards.
3. **It limits predatory declarations by strength.** The score window is a structural anti-snowball rule.
4. **It offers cheap defensive counterplay.** Fortify costs 3 MAP and is available to everyone.
5. **It makes control states contestable.** No control state is permanent.

### 14.4 What it does not do

1. **It does not protect a small nation after beige.** Once the 14 days end, the nation is in range of anything within 250% of its score, with only 3 defensive slots and no ally shield.
2. **It does not protect allies.** There is no mechanical alliance defence.
3. **It does not enforce treaties.** A NAP is social only.
4. **It does not stop repeat farming.** A nation can be declared on again the moment beige ends.
5. **It does not create a comeback path beyond recruitment.** The beige buff helps rebuild units, not infrastructure or stockpiles.
6. **It does not distinguish an absent player from a present one.** Gray status follows inactivity, but gray is still attackable.

These gaps are exactly the space Nation Supremacy's B-03 protections and B-08/B-09 NAP layers are designed to fill. P&W is a **baseline**, not a benchmark to copy.

---

## 15. Losses and economic effects

### 15.1 Loss channels

| Channel | Magnitude | Bounded? | Recoverable? | Evidence |
|---|---|---|---|---|
| **Victory cash loot** | 10% of money | Yes, percentage | Yes, by income | WFS-031 |
| **Victory resource loot** | 10% of each resource | Yes, percentage | Yes, by production/trade | WFS-031 |
| **Victory infrastructure** | Up to 4% per city | Yes, percentage | Yes, by construction | WFS-031 |
| **Alliance bank loot** | Up to 33% of the bank, scaled by score ratio | Yes, capped | Yes, by contributions | WFS-031 |
| **Ground loot** | Formula; ≤75% of cash and never the last $1m | Yes | Yes | WFS-024 |
| **Infrastructure damage** | Per-action formula with city cap | Yes, per action | Yes, by construction | WFS-024…WFS-027 |
| **Improvement destruction** | 10%/15% chance; 2 per missile; 4 per nuke | Probabilistic or fixed | Yes, by rebuilding | WFS-024, WFS-026, WFS-005, WFS-006 |
| **Unit casualties** | Per-action formula | Yes | Yes, by daily recruitment | WFS-024…WFS-026 |
| **Resource burn** | Per battle | Yes | Yes, by production/trade | WFS-002 |
| **Upkeep** | Daily; wartime multiplier | Continuous | Yes, by income | WFS-011…WFS-017 |
| **Radiation** | Disease up; food down for 100 turns | Time-bounded | Yes, after 100 turns | WFS-028 |
| **City loss** | **None** | — | — | WFS-031 (no city loss); B-05 URB-111 independently forbids it |
| **Territory loss** | **None** | — | — | WFR-052 |
| **Reparations** | **None** | — | — | WFR-023 |

### 15.2 Is P&W's loss model bounded?

Yes, in the narrow sense that every channel has a cap, a percentage or a formula. No single battle can delete a nation. No war can transfer cities. A loser retains its cities, population, buildings and production base; it loses stockpiles, infrastructure percentage, improvements and units. This is a **damage-and-transfer** model, not a **conquest** model.

It is **not** bounded in the strategic sense: a nation can be repeatedly defeated, and each defeat costs 10% of stockpiles, up to 4% of infrastructure and a portion of the alliance bank. Over many wars, the cumulative effect can be severe. P&W relies on the score window, beige and the recruitment buff to soften this, not on a hard lifetime cap.

### 15.3 Snowball and catch-up analysis

| Force | Direction | Mechanism | Evidence |
|---|---|---|---|
| Victory loot | Winner gains, loser loses | 10% transfer | WFS-031 |
| Infrastructure damage | Loser loses development | Up to 4% | WFS-031 |
| Alliance bank loot | Winner's alliance gains, loser's loses | Up to 33% | WFS-031 |
| Unit losses | Both sides lose | Combat casualties | WFS-024…WFS-026 |
| Upkeep | Both sides pay | Wartime multiplier | WFS-011…WFS-017 |
| Beige | Loser protected | 2 days | WFS-031 |
| Beige recruitment buff | Loser catches up | +15% recruitment | WFS-002 |
| Score window | Limits predation | 75%–250% | WFS-033 |
| Daily recruitment | Both sides rebuild | Building caps | WFS-011…WFS-015 |
| No war exhaustion | Neither side weakens from duration alone | No mechanic | Absence |

The model is **mildly snowballing**: the winner takes value and keeps its units, while the loser loses value and must rebuild. The counterweights are beige, the recruitment buff, the score window and the absence of city transfer. A Nation Supremacy design that wants a stronger catch-up effect must add one explicitly; P&W does not.

### 15.4 Economic effects beyond the war

- **Upkeep persists after the war.** Units and missiles/nukes continue to cost money in peacetime, so a large military is a permanent fiscal commitment (WFS-011…WFS-017).
- **Improvement loss changes production.** Destroyed improvements reduce output until rebuilt (WFS-024, WFS-026).
- **Radiation has a regional/world effect.** In Nation Supremacy there are no continents, so this mechanic needs adaptation or rejection (WFS-028; §19).
- **Blockade has trade effects beyond the war.** A blockaded nation cannot trade or bank, which can affect third parties (WFS-030).
- **Beige has an economic bonus.** $50,000 per turn colour bonus while beige (WFS-032), plus the +15% recruitment buff (WFS-002).

---

## 16. War termination and postwar findings

### 16.1 Termination routes

| Route | Who can trigger | Requirements | Effect on loser | Effect on winner | Evidence |
|---|---|---|---|---|---|
| **Victory** | Either side | Reduce opponent resistance to 0 | Beige 2 days; loot loss; infrastructure loss | Loot; no lasting control | WFS-031 |
| **Mutual peace** | Either side offers; other accepts | Both agree | No loot; war ends | No loot; war ends | WFS-022 |
| **Expiry** | System | Turn 60 | War ends (routine undocumented) | War ends | WFS-022 |
| **Inactivity deletion** | System | 31/60/90/97 days | Nation deleted | No gain | WFS-001 |
| **Moderation peace-out** | Moderator | War-slot-filling finding | War manually ended | War manually ended | WFS-001 rule 4 |

### 16.2 What "postwar" means in P&W

Postwar is **beige and nothing else**:

- 2 days of immunity to new declarations (WFS-031, WFS-032).
- Existing wars may continue (WFS-031).
- +15% recruitment while beige and war-free (WFS-002).
- $50,000 per-turn colour bonus while beige (WFS-032).
- No reparations, no demilitarisation, no occupation, no treaty, no truce timer, no war-guilt record.

### 16.3 The settlement gap

Nation Supremacy's Prompt 10 brief requires a **ceasefire and settlement framework**. P&W provides no settlement object to adapt. The following components therefore have **no P&W precedent** and must be designed from first principles:

1. **Settlement record** — who conceded what, when, and until when.
2. **Terms catalogue** — what may be demanded (resources? demilitarisation? a NAP? a public acknowledgement?).
3. **Enforcement** — what makes terms binding after the war ends.
4. **Duration and expiry** — how long terms last and how they end.
5. **Consent** — whether the loser must accept, and what happens if it refuses.
6. **Audit and visibility** — who can see the terms and the record.
7. **Interaction with reroll (UD-032)** — whether an unsettled settlement blocks a reroll.
8. **Interaction with B-03 protections** — whether a protected nation can be a party.
9. **Interaction with B-04 conservation** — reparations must move value, not mint it.
10. **Interaction with B-09** — no alliance may be bound without owner consent; no collective military power.

The only P&W rules that constrain settlement design are the **prohibition on coerced city deletion** (WFS-001 rule 15) and the **absence of any forced-transfer mechanic** (WFR-023). Both point toward **consensual, bounded, resource-based terms**, not territorial or existential demands.

### 16.4 War termination and UD-032

UD-032 asks what happens to an active campaign when a participant rerolls. P&W's reroll analogue is nation deletion/recreation, and it has **no campaign object** to be affected. Its closest rules are:

- Inactivity deletion removes the nation entirely (WFS-001).
- Beige follows defeat, not reroll (WFS-031).
- There is no rule for "the old nation's war continues under a new identity" because identities are not transferable (WFS-001 rules 1 and 11).

This means P&W provides **no evidence** for any of UD-032's three options. The dedicated analysis is in §28.

---

## 17. Alliance warfare and military coordination

### 17.1 What P&W provides

| Function | P&W | Evidence |
|---|---|---|
| Alliance as an economic container | Yes: taxes, bank, colour bloc | WFS-032, WFS-001 |
| Alliance as a social container | Yes: membership, roles, communication | WFS-001; absence of mechanical roles in war |
| Alliance war declaration | **No** | WFS-022 |
| Alliance-level war object | **No** | WFS-022 |
| Shared MAP pool | **No** | WFS-022 |
| Shared unit pool | **No** | WFS-022 |
| Delegated attack authority | **No** | WFS-022; absence |
| Alliance bank used to fund attacks | **No** mechanical path | WFS-031 |
| Alliance bank exposed to looting | **Yes** | WFS-031 |
| Alliance NAP enforcement | **No** | WFR-028 |
| Same-alliance attack ban | **No** mechanical ban in P&W | WFS-022; WFR-029 |
| Coordination rules | War-slot filling, spy-slot filling, bounty and treasure coordination are prohibited | WFS-001 rules 4–7 |

### 17.2 What coordination exists

The examined sources document **rules against abusive coordination**, not a coordination system. Rule 4 prohibits declaring war on allies or filling slots to shield a target; rule 5 prohibits spy slot filling; rule 6 prohibits bounty coordination; rule 7 prohibits treasure-transfer coordination (WFS-001). The existence of these rules implies that players coordinate, but the public pages do not describe how. Any statement that "alliances coordinate on Discord" would be **UNVERIFIED** and is not used here.

### 17.3 The B-09 boundary

B-09 is far more specific than P&W. It already specifies:

- **ALL-089/139/140** — national military sovereignty; no alliance may order, move, attack with or spend for a member's military.
- **ALL-206** — active NAP attack prohibition across every method.
- **ALL-209** — same-alliance attack ban.
- **ALL-210/211** — one canonical server-side validator; fail-closed at submission and execution.
- **ALL-213** — Prompt 10 integration contract.
- **ALL-214** — mandatory audit `AUD-AL-017`.
- **ALL-215** — no confiscation or retaliation for a blocked attack.
- **AX-18/AX-30** — no delegation and no collective military powers.
- **AT-E01** — the only treaty effect that creates an attack ban.
- **REQ-640/642/645–647** — approved implementation requirements.

P&W is compatible with this boundary at the level of **"allies fight alongside each other, not through each other."** It is silent on every enforcement detail. Nation Supremacy must therefore treat P&W as a **cultural precedent**, not a mechanical one.

### 17.4 The four attack-prevention layers and Prompt 10

Prompt 10 must design around four cumulative layers:

1. **B-03 restricted-pair ban** — two restricted nations cannot attack each other, join the same side or support each other (NET-025/026/029).
2. **B-08 national treaty/NAP block** — DP-T01 blocks war declaration; DIP-141 hook is inert until Prompt 10.
3. **B-09 Alliance NAP** — ALL-206 for the explicitly consenting covered nations under the separate Alliance-to-Alliance treaty framework authorized by **`D-140`** (`AT-T01` / `AT-E01`). Membership alone does not cover a nation; a non-consenting member remains a member and is outside the NAP. `UD-047` remains **Open / Owner-Reserved** for collective diplomatic positions and any delegation model and authorizes no part of this framework.
4. **B-09 same-Alliance ban** — ALL-209.

Enforcement must be **server-side at every attack entry point and path**, not UI hiding. P&W's rule-based moderation is the opposite model (detect and punish after the fact). Nation Supremacy's model is **prevent at submission and execution**, with mandatory audit. This is a deliberate divergence and should be stated as such in 10B.

---

## 18. Abuse and fairness research

### 18.1 Abuse catalogue relevant to warfare

| Abuse | P&W rule | Detection evidence | Consequence | Residual risk |
|---|---|---|---|---|
| **Multi-accounting** | Rule 1: one nation per player | Account/network investigation | 50–100 moderation points; 1-year expiry | Hard to prove; VPNs |
| **Same-network target stacking** | Rule 2: no two same-network nations on the same target | Network records | 25–50 points; 1-year expiry | Shared households, schools, cafés |
| **Bank evasion of network restrictions** | Rule 2 | Bank/trade records | Bannable | Requires transaction analysis |
| **War slot filling** | Rule 4 | Battle logs, unit counts, Fortify-only wars, ally targeting | 25–75 points; 2-year expiry; war manually peaced | Intent is hard to prove; moderator discretion |
| **Spy slot filling** | Rule 5 | Operation logs, damage levels, ally targeting | 25–75 points; 2-year expiry | Same intent problem |
| **Bounty coordination** | Rule 6 | Bounty and battle records | 25–75 points; 2-year expiry | Collusion is hard to distinguish from hunting |
| **Treasure transfer coordination** | Rule 7 | War and treasure records | 25–75 points; 2-year expiry | Same |
| **Automated war/attacks/espionage** | Rule 10 | Timing patterns, API use, reports | 25–100 points; 2-year expiry | Detection is probabilistic |
| **Account selling** | Rule 11 | Ownership evidence | 100 points; permanent | Off-platform |
| **Real-world trading** | Rule 12 | Payment evidence | 75–100 points; permanent | Off-platform |
| **Coerced city deletion** | Rule 15 | Peace terms, messages | 50–100 points; 2-year expiry | Requires message evidence |
| **Bank protection via Vacation Mode/new nation** | Rule 16 | VM/bank timing, nation age | Bank returned, 20% deleted | Requires investigation |
| **Exploit abuse** | Rule 17 | Bug reports, logs | 50–100 points; 2-year expiry; discretion | Unknown bugs |

### 18.2 Fairness properties of P&W's model

**Strengths:**
- The rules are **published** and specific about prohibited behaviour.
- Penalties are **graded** (points and expiry), not binary.
- Several rules target **intent** explicitly (slot filling, coordination).
- The game **does not promise perfect detection**; it relies on reports and moderation.
- Same-network restrictions are **narrow** (no same-target declarations), not a blanket ban.

**Weaknesses:**
- Enforcement is **manual and discretionary**; two similar cases can be treated differently.
- Detection of collusion, botting and multi-accounting is **probabilistic**.
- There is **no published evidence standard** or appeal process in the examined pages.
- The rules **do not prevent** the abuse; they punish it after the fact.
- A blocked or punished war is **not automatically reversed** except in slot-filling cases.

### 18.3 Implications for Nation Supremacy

Nation Supremacy's B-03 already goes further than P&W on evidence, least privilege, preservation orders and appeals. Prompt 10 should not import P&W's moderation model. It should:

- **Prevent** where a server-side validator can (B-09 attack blocks).
- **Record** every blocked attempt (`AUD-AL-017`).
- **Explain** the block in plain language (ALL-214).
- **Avoid** confiscation or retaliation for a blocked attempt (ALL-215).
- **Leave** intent-based abuse (slot filling, collusion) to Prompt 12's policy, not to the war engine.

P&W's most useful contribution is the **taxonomy of abuses**, not its enforcement mechanics.

---

## 19. Mapless suitability analysis

### 19.1 The strict test

Nation Supremacy forbids geographic fronts, world maps, provinces, tiles, adjacency, borders, troop movement, territory capture, coordinate targeting, geographic supply routes and geographic control. Each P&W mechanic is tested against that list.

**Game-world geography is not the same as map-based warfare.** P&W's world does use geographic concepts: nations are associated with **continents**, radiation is tracked at continent and world level (WFS-028), and wars target named **cities** (WFS-005, WFS-006, WFS-031). The test below applies only to **warfare mechanics** — whether an attack requires a geographic front, a province or tile, geographic adjacency, physical troop movement across a territorial map, coordinate-based battlefield targeting or a geographic supply route. The examined P&W pages document none of those. A P&W city is a targetable development centre, not a map position; a continent is an environmental context, not a battlefield. Nation Supremacy's own constraint is stricter and remains intact: it forbids geographic fronts, a territorial world map and physical troop movement.

| P&W mechanic | Geographic dependency | Verdict | Why |
|---|---|---|---|
| **Resistance race** | None | **Suitable** | A national counter, not a location |
| **MAPs** | None | **Suitable** | A per-war action budget |
| **War types** | None | **Suitable** | Economic presets |
| **Score range** | None | **Suitable** | A strength gate |
| **Slots** | None | **Suitable** | A national cap |
| **Ground Battle** | None | **Suitable** | Targets a nation and its highest-infrastructure city; no front |
| **Airstrike** | None | **Suitable** | A national air capability; no sortie geography |
| **Naval Battle** | None | **Suitable with renaming** | "Naval" is a domain label; there is no sea zone or coast |
| **Missile** | Weak: city targeting | **Suitable with adaptation** | Targets a P&W city as a development centre, not a coordinate or tile; Nation Supremacy would map it to a B-05 non-geographic city |
| **Nuclear** | Weak: city + continent radiation | **Suitable with adaptation** | Radiation needs a world/nation analogue because NS has no continents |
| **Fortify** | None | **Suitable** | A posture |
| **Ground Control** | Name only | **Suitable with renaming** | It is a control state over a nation, not territory |
| **Air Superiority** | Name only | **Suitable with renaming** | A force multiplier, not airspace |
| **Blockade** | Name only | **Suitable with renaming** | Trade/bank restriction, not a sea zone |
| **Espionage** | None | **Suitable** | Fully abstract |
| **Offer Peace** | None | **Suitable** | Bilateral stop |
| **Victory loot** | None | **Suitable** | Percentage transfer |
| **Infrastructure damage** | None | **Suitable** | Development-centre damage |
| **Beige/gray** | None | **Suitable** | Status colours, not locations |
| **War policies** | None | **Suitable** | National posture |
| **Projects** | None | **Suitable** | National investments |
| **Alliance bank loot** | None | **Suitable** | A shared account, not a place |
| **Daily recruitment** | None | **Suitable** | Time-gated production |
| **Upkeep** | None | **Suitable** | National cost |
| **Inactivity deletion** | None | **Suitable** | Account state |

### 19.2 Labels that imply geography but do not create it

Four P&W labels are geographic metaphors. They must be treated as **names**, not mechanics:

1. **"Ground Control"** — P&W's own description is a control state that lets tanks destroy aircraft and is broken by a successful ground attack. It does not grant territory, movement or occupation. The name is misleading for Nation Supremacy and should be replaced (e.g. "Land Dominance" or "Ground Initiative") if adopted.
2. **"Air Superiority"** — a 50% tank penalty. It does not create airspace, interception zones or sortie ranges.
3. **"Blockade"** — a trade and bank restriction. It does not create a sea zone, a coast or a fleet position.
4. **"Naval Battle"** — a battle between two nations' ship stocks. It does not create a sea, a route or a port.

Renaming is not cosmetic housekeeping. In a mapless design, a geographic label invites players and future designers to assume geographic behaviour. 10B should use symbolic names.

### 19.3 The two mechanics that need real adaptation

**Missile and nuclear city targeting.** P&W lets the attacker choose an enemy **city** and, for missiles, an improvement type. B-05 defines cities as **non-geographic development centres**, not map locations. A Nation Supremacy strategic strike can therefore target a **development centre** (a named city) without coordinates, distance or adjacency. That is compatible **if and only if** the design treats the city as an abstract asset, not a place on a map. The risk is not the mechanic; it is the UI language ("strike this city") implying geography.

**Nuclear radiation.** P&W raises radiation in the **continent** and the **world** for 100 turns. Nation Supremacy has no continents. The mechanic can be adapted as:
- a **world-level** radiation pool, or
- a **nation-level** contamination state, or
- rejected entirely if it cannot be made legible without geography.

The world-level version preserves the "everyone pays" quality; the nation-level version preserves the "target suffers" quality. Both are mapless. 10B must choose, and the choice must be recorded as a design decision, not left implicit.

### 19.4 What P&W proves about mapless war

P&W's **warfare** is the strongest available evidence that a **commercial, long-running, multiplayer war game can conduct conflict without a geographic battlefield and still produce**:
- bounded wars with a readable winner,
- meaningful force composition,
- economic attrition,
- control states that are contestable,
- protection and recovery,
- alliance-level social coordination,
- and a live moderation regime for abuse.

It does **not** prove that a mapless game can support:
- a campaign object above the nation-war,
- a negotiated settlement with terms,
- an alliance-level war,
- a supply system with interdiction,
- or a territorial objective.

Those are Nation Supremacy design problems, not P&W features to port.

---

## 20. P&W-to-Nation Supremacy classification matrix

**Classification values.** `ADOPT CANDIDATE` — the mechanic can be proposed to 10B with little structural change. `ADAPT` — the purpose is useful but the P&W form conflicts with a Nation Supremacy constraint. `REJECT` — the mechanic should not be proposed in its P&W form. `NOT APPLICABLE` — P&W's context does not exist in Nation Supremacy. `INVESTIGATE FURTHER` — the evidence is insufficient to classify responsibly.

**No row is approval.** "Adopt candidate" means "worth proposing", not "approved". Every numeric value remains for 10B and B-14.

| ID | P&W mechanic | NS target | Class | Rationale | Evidence | Binding constraint | Adaptation sketch | Depends on | Risks | Confidence | 10B action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **WFC-01** | Resistance race (100 → 0) | Conflict progress meter | **ADOPT CANDIDATE** | Bounded, readable, no geographic battlefield; gives both sides the same target | WFS-022, WFS-019 | REQ-014; D-015 | Per-war or per-campaign progress pool; winner at 0 | B-02 P5 | A flat pool ignores strength differences | High | Define pool size and reduction values |
| **WFC-02** | Unilateral declaration | Attack submission | **ADAPT** | P&W has no consent; NS has NAP/alliance blocks and protections | WFS-022; DP-T01; ALL-206/209 | B-08 DP-T01; B-09 ALL-206/209–215; B-03 ONB-019…024 | Keep unilateral declaration, but every path calls the cumulative validators; blocked attempt moves nothing | B-08, B-09 | Bypass at a non-covered entry point | High | Map every entry point to the validator |
| **WFC-03** | Three war types (Ordinary/Attrition/Raid) | Campaign posture | **ADAPT** | Useful pre-commitment, but percentages are P&W-specific and asymmetric | WFS-003, WFS-022 | Mapless; B-04 conservation | Two to four postures chosen at declaration, immutable; each states damage/loot trade-off | B-04, B-14 | Defender asymmetry surprises players | High | Define postures and disclosure |
| **WFC-04** | Score window 75%–250% | Strength gate | **ADAPT** | Prevents extreme mismatch, but NS has its own power metric | WFS-033 | REQ-014; B-11 rankings | NS-specific power range with a disclosed formula | B-11, B-14 | 250% is unverified even in P&W | Medium | Define NS metric and range |
| **WFC-05** | 5 offensive / 3 defensive slots | Campaign/war caps | **ADAPT** | Caps exposure and coordination load; P&W slots are war-specific | WFS-022 | D-015; D-024 | Caps on simultaneous campaigns or declarations, with a declared limit | B-02, B-12 | Slot filling and shield wars | High | Define cap and abuse rule |
| **WFC-06** | Per-war MAP pools (6→12) | Action economy | **REJECT** | Directly conflicts with D-015's single national Operations Points pool | WFS-022; D-015 | D-015; D-024 | Use one national OP pool, not per-war pools | B-02 | Losing P&W's "many small wars" tempo | High | Confirm OP-only model |
| **WFC-07** | 60-turn / 5-day war bound | Campaign duration | **ADOPT CANDIDATE** | A hard bound prevents infinite attrition; expiry routine must be defined | WFS-022 | REQ-014 | Maximum campaign length in turns, with an explicit expiry and settlement step | B-02 | P&W does not document expiry | High | Define expiry and tie |
| **WFC-08** | 3-roll, 40–100%, four tiers | Battle resolution | **ADAPT** | Bounded randomness and readable tiers; pre-battle odds are opaque in P&W | WFS-022, WFS-024…WFS-026 | Transparency requirement | Keep tiers; expose odds or a confidence range before commitment | B-14 | Players cannot evaluate risk | High | Define resolution and disclosure |
| **WFC-09** | Ground Control / Air Superiority / Blockade / Fortified | Abstract control states | **ADAPT** | Control without territory; contestable; excellent mapless fit | WFS-008…WFS-010, WFS-004 | Mapless | Three or four symbolic states with explicit break conditions; rename geographic labels | B-02 P5 | Names imply geography | High | Rename and define counters |
| **WFC-10** | Ground Battle | Core land operation | **ADAPT** | Core resistance-reducing operation; targets a nation, not a front | WFS-019, WFS-024 | B-05 URB-111/157; B-04 | Operation with OP cost, resource burn, casualties and progress reduction | B-04, B-05, B-14 | Formula import without calibration | High | Define operation and values |
| **WFC-11** | Airstrike | Air operation | **INVESTIGATE FURTHER** | The examined pages do not state its MAP cost or resistance values | WFS-018, WFS-025 | Transparency | Do not import until the cost and effect are established or independently designed | B-14 | Guessing a cost | Low | Research or design from scratch |
| **WFC-12** | Naval Battle | Maritime/domain operation | **ADAPT** | Blockade and improvement destruction are useful; "naval" is a domain label, not a sea zone | WFS-007, WFS-026, WFS-030 | Mapless | Rename as a domain operation or drop it if NS has no naval concept | B-14 | Domain may not fit NS | Medium | Decide keep/rename/drop |
| **WFC-13** | Missiles (8 MAP, 18 resistance, 2 improvements) | Strategic strike | **ADAPT** | Precision strike on a development centre; high OP cost | WFS-005, WFS-027 | B-05 cities non-geographic | Target a city-as-asset, not a coordinate; cap improvements | B-05, B-14 | UI language implies geography | High | Define target model |
| **WFC-14** | Nuclear weapons + radiation | Strategic escalation | **REJECT** | Radiation is continental/world and disproportionate; incompatible with NS scale and B-04 conservation posture | WFS-006, WFS-028 | B-04, B-05, mapless | Do not port radiation; if escalation is needed, design a bounded alternative | B-14 | Losing an escalation layer | Medium | Record rejection or design alternative |
| **WFC-15** | Fortify (3 MAP, +25% casualties) | Defensive operation | **ADOPT CANDIDATE** | Cheap, legible, no geographic requirement; strong stalling risk | WFS-004 | D-015 | Defensive OP action with a bounded duration and a break condition | B-02 | Stalling the war to expiry | High | Define duration and cap |
| **WFC-16** | Espionage (0 MAP, daily) | Covert action | **ADAPT** | Separate daily economy; D-024 forbids a shared currency | WFS-020, WFS-029 | D-024 | Separate covert budget/cooldown, player-visible | B-12 | Creating a second unconstrained currency | High | Define covert limits |
| **WFC-17** | Offer Peace (mutual acceptance) | War termination | **ADAPT** | A bilateral stop with no terms; NS needs a settlement layer | WFS-022 | REQ-014; UD-032 | Peace offer/accept plus a separate settlement step | B-08, UD-032 | A peace with no recorded terms | High | Define offer/accept and settlement |
| **WFC-18** | Victory loot (10%/10%; bank ≤33%) | Postwar transfer | **ADAPT** | Bounded transfer; must move value, never mint | WFS-031 | B-04 ECN-214; REQ-177 | Transfer from the loser's actual stockpile with a cap and ledger entry | B-04 | Snowballing | High | Define caps and ledger |
| **WFC-19** | Infrastructure and improvement damage | Development damage | **ADAPT** | Damages development without city loss | WFS-024…WFS-027 | B-05 URB-111/157 | Damage infrastructure/improvements; cities never transfer | B-05 | Permanent loss without repair | High | Define repair and floors |
| **WFC-20** | Units, build caps, daily recruitment, upkeep | Readiness economics | **ADAPT** | Creates strategic depth without geography | WFS-011…WFS-017, WFS-002 | B-04, D-015 | NS unit roster with build caps, daily recruitment, upkeep and resource burn | B-04, B-05, B-14 | Complexity and balance | High | Define roster and costs |
| **WFC-21** | Military research | Long-term military progression | **ADAPT** | Avoids a pure "more cities" ladder; may duplicate B-05 research | WFS-002 | B-05 research ownership | Coordinate with B-05; military-specific upgrades only | B-05, B-14 | Duplicate research systems | Medium | Coordinate with B-05 |
| **WFC-22** | 10 war policies, 5 pairs, 60-turn cooldown | Posture choice | **ADAPT** | Multiple small modifiers; long lock-in | WFS-023 | B-14 | Four to six postures with explicit trade-offs and a cooldown | B-14 | Dominant policy | Medium | Define postures |
| **WFC-23** | Beige / gray / 14-day new-nation protection | Protection states | **ADAPT** | Time-boxed protection works; NS already has 7-day/84-turn protection | WFS-031, WFS-032; ONB-019/020 | B-03 ONB-019…024; REQ-090 | Reuse NS protection states; do not import 14 days or 2 days blindly | B-03 | Conflicting durations | High | Align with B-03 |
| **WFC-24** | No alliance war, no delegated command | Alliance boundary | **ADOPT CANDIDATE** | Matches B-09's national-sovereignty rule; P&W proves coordination can be social | WFS-022; ALL-089/139/140 | ALL-206/209–215; AX-18/30; AT-E01 | No collective military power; cumulative validators; audit | B-09 | Pressure to add alliance command | High | Integrate B-09 contract |
| **WFC-25** | Moderation of war abuses | Fair-play taxonomy | **ADAPT** | Useful taxonomy, but NS requires prevention and evidence | WFS-001 | B-03 §5.6–5.10; Prompt 12 | Use the taxonomy; prevention and audit are NS-specific | B-12 | Intent-based abuse | High | Hand taxonomy to Prompt 12 |
| **WFC-26** | Mapless conflict itself | Architectural precedent | **ADOPT CANDIDATE** | A live commercial game proves mapless warfare is legible | WFS-022, WFS-031, WFS-032 | Mapless constraint | Adopt the abstraction; reject geographic labels | B-02 | Copying labels that imply geography | High | State mapless conformance |

### 20.1 Classification counts

| Classification | Count | IDs |
|---|---|---|
| ADOPT CANDIDATE | 5 | WFC-01, WFC-07, WFC-15, WFC-24, WFC-26 |
| ADAPT | 18 | WFC-02…WFC-05, WFC-08…WFC-10, WFC-12, WFC-13, WFC-16…WFC-23, WFC-25 |
| REJECT | 2 | WFC-06, WFC-14 |
| INVESTIGATE FURTHER | 1 | WFC-11 |
| NOT APPLICABLE | 0 | — |
| **Total** | **26** | — |

### 20.2 Why nothing is "NOT APPLICABLE"

Every P&W mechanic examined has a possible Nation Supremacy analogue, even where the analogue is "do not do this". The absence of a "not applicable" row is itself a finding: P&W's conflict system is close enough to Nation Supremacy's intended shape that the interesting question is **how to adapt**, not **whether the domain matches**.

---

## 21. Existing approved and provisional constraints

This section lists the constraints that bind 10A and will bind 10B. It does not restate them as new rules; it records how the research respects them.

### 21.1 Decisions

| ID | Binding content | Status | Effect on this research |
|---|---|---|---|
| **D-014** | Autonomous decision policy: ordinary design decisions are Category B and may be made and recorded without waiting for the owner | Confirmed | 10A records findings and candidate requirements; it does not stall on owner input |
| **D-015** | One national Operations Points pool; refilled to cap at the boundary; military-only; non-transferable; reserved at acceptance; consumed at resolution; cap/costs/readiness scaling provisional | Confirmed model; values Provisional | **P&W's per-war MAP pools are rejected** (WFC-06); every candidate operation must draw on OP |
| **D-023** | Warfare is in Stage 2 Prompt 10 but not in the first playable build | Confirmed | 10A is research only; no implementation is implied |
| **D-024** | No shared general action budget and no universal per-turn click budget; each subsystem declares its own limits | Confirmed | Espionage needs its own declared limits (WFC-16); no second general currency |

### 21.2 Requirements traceability

| REQ | Binding content (summary) | Status | Research treatment |
|---|---|---|---|
| **REQ-014** | Strategic orders exist only with a war rule set, protection states and settlement enforcement | Deferred → B-10 | Drives §16 and WCR-07/29 |
| **REQ-063** | Every value-moving or coordinating action is classified; indirect routes covered; a blocked attempt moves nothing | Provisional | Applied to every attack path in §22 and §28 |
| **REQ-085** | Reroll cleanup across warfare is deterministic | Provisional | UD-032 analysis (§28) |
| **REQ-086** | A reroll is blocked by an active campaign, unsettled settlement, preservation hold or disqualifying state | Provisional | UD-032 analysis (§28) |
| **REQ-090** | Newcomer protection is visibility-only, once per account, skipped between restricted pairs, never an economic multiplier | Provisional | Protection analysis (§14); beige buff would conflict if imported |
| **REQ-099** | Exactly seven raw goods and four manufactured goods | Approved (roster) | Limits which resources war may consume |
| **REQ-108** | Gasoline is a manufactured good used as construction fuel, military fuel and trade | Provisional | Per-battle gasoline burn (§11) |
| **REQ-109** | Ammunition is a manufactured good consumed by readiness and campaigns | Provisional | Per-battle munitions burn (§11) |
| **REQ-177** | Prompt 10 consumes gasoline, ammunition, steel and aluminium through reservation and ledger, without minting | Provisional | B-04 coupling (§22) |
| **REQ-518** | An active NAP prohibits war declaration; enforced by Prompt 10; inert until Prompt 10 exists | Provisional | Declaration validator (§7.1, §17.4) |
| **REQ-588** | Alliance rosters show declared readiness, not private military data | Provisional | Readiness visibility (§22) |
| **REQ-589** | An alliance cannot order, move, attack with or spend for a member's military | Provisional | No delegated command (WFC-24) |
| **REQ-590** | War information follows the Military system's visibility rules; no private alliance view | Provisional | Visibility contract (§22) |
| **REQ-591** | Military coordination features are deferred until the Military rulebook exists | Deferred → Prompt 10 | 10B must define or explicitly defer |
| **REQ-640** | Only AT-T01 creates a mandatory cross-alliance attack restriction; other treaties are record-only | Approved | Attack validator must check only AT-T01 |
| **REQ-642** | Active AT-T01 NAP blocks every attack method; server-side validator at every entry point; clear reason; mandatory audit | Approved | §17.4 and §22 B-09 row |
| **REQ-645** | Same-alliance attack ban; one canonical validator; UI hiding is not enforcement | Approved | §17.4 |
| **REQ-646** | Validator runs at submission and execution; fail-closed; no partial execution or resource consumption | Approved | §17.4 |
| **REQ-647** | Prompt 10 calls both checks independently; cumulative; mandatory `AUD-AL-017`; no confiscation or retaliation | Approved | §17.4 and §28 |

### 21.3 Rulebook constraints

| Source | Binding content | Research treatment |
|---|---|---|
| **B-03 NET-025/026/029** | Restricted pairs cannot attack each other, join the same side or support each other; indirect routes are covered; a blocked action moves nothing | Every attack path must include the restricted-pair check |
| **B-03 RRL-019** | Reroll cleanup includes warfare; a reroll is blocked during an active campaign; Prompt 10 may define forfeit | UD-032 (§28) |
| **B-03 RRL-021** | Blocking conditions for a reroll | UD-032 (§28) |
| **B-03 ONB-019/020** | First-nation protection: 7 days / 84 turns or first offensive action | Protection analysis (§14) |
| **B-03 ONB-023/024** | A protected nation cannot be attacked or attack | Every attack validator must check protection status |
| **B-03 ONB-031** | 30 days / 360 turns one-sided transfer restriction | Loot and settlement transfers must respect it |
| **B-04 ECN-214** | Prompt 10 owns gasoline/ammunition/steel/aluminium consumed by readiness/campaigns; reserve at acceptance, consume at resolution; never mint | §11 and §22 B-04 row |
| **B-04 ECN-130** | Reroll destroys inventory | UD-032 (§28) |
| **B-05 URB-111** | Cities cannot be lost | No city capture or transfer (WFC-19) |
| **B-05 URB-157** | Default warfare destroys resources/units, not cities; military branch/buildings only via a decision | Loss model (§15) |
| **B-05 URB-061** | Cities supply steel, aluminium, gasoline and ammunition | Resource coupling (§11) |
| **B-06 DMP-092** | No military modifiers from government | No government-based war bonus |
| **B-06 DMP-127** | War is a crisis input only | Approval effects are Prompt 10-registered, not invented |
| **B-06 DMP-140** | War may move approval only through registered Prompt 10 terms | Settlement and war outcomes need a registered approval hook |
| **B-08 DP-T01** | NAP blocks declaration | Declaration validator |
| **B-08 DIP-039** | Treaties are nation-party | No alliance-party NAP except B-09's AT-T01 |
| **B-08 DIP-070** | War ordering is owned by Prompt 10 | 10B defines ordering |
| **B-08 DIP-141** | NAP hook is declared and inert until Prompt 10 | 10B activates it |
| **B-09 ALL-206** | Active NAP attack prohibition across every method | Attack validator |
| **B-09 ALL-209** | Same-alliance attack ban | Attack validator |
| **B-09 ALL-210/211** | One canonical server-side validator; fail-closed at submission and execution | Attack validator |
| **B-09 ALL-213** | Prompt 10 integration contract | 10B deliverable |
| **B-09 ALL-214** | Mandatory `AUD-AL-017` and plain-language reason | 10B deliverable |
| **B-09 ALL-215** | No confiscation, fine, freeze or retaliation for a blocked attack | 10B deliverable |
| **B-09 AX-18/AX-30** | No delegation; no collective military powers | No alliance command (WFC-24) |
| **B-09 AT-E01** | The only treaty effect that creates an attack ban | Validator scope |
| **UD-032** | Reroll during an active campaign: block, forfeit, or finish under the old identity | **Deferred; not resolved by 10A** (§28) |

---

## 22. Cross-system integration matrix

Each row states what Prompt 10 needs from the owning system, what it provides back, the interface, the data and timing, the failure behaviour, the audit duty, the open questions, the dependency and the handoff. "P10" means Prompt 10.

| System | Owner / scope | What P10 needs | What P10 provides | Contract / interface | Data and timing | Failure / edge | Audit | Open questions | Depends on | Handoff |
|---|---|---|---|---|---|---|---|---|---|---|
| **B-02** Core loop and turn system | B-02; P0–P7 | P5 Conflict phase, OP refill at P3, reservation at acceptance, settlement at P7, phase-failure behaviour | Conflict resolution inside P5, no mutation before P5, digest at P7 | TR-040 phase contract; TR-093 subsystem declaration | P5 runs after P4; OP refilled at P3; reservations at acceptance | P5 failure → `INTERRUPTED`; resume from checkpoint | Turn digest and conflict events | Whether campaign costs draw on pre- or post-P3 balances (TR-042) | B-02 | 10B must answer TR-042 |
| **B-03** Accounts and protection | B-03; NET/RRL/ONB | Restricted-pair check, protection state, reroll block, transfer restriction | War state for cleanup, campaign status for reroll eligibility | Attack validator calls B-03 checks first | At submission and execution | Fail-closed; no block consumes value | Blocked attempt record (non-Alliance path) | Reroll forfeit (UD-032) | B-03 | UD-032 analysis (§28) |
| **B-04** Economy and resources | B-04; ECN-214 | Resource definitions, ledger, reservation/consume semantics, no-mint rule | Demand for gasoline/ammunition/steel/aluminium; loot/settlement transfer requests | Reservation at acceptance; `CONSUME`/`OBLIGATION_PAID` at resolution | Every operation; every turn for upkeep | Insufficient resources → operation refused or deficit rule | Resource ledger entries | Whether upkeep is a P3 obligation or P4 order | B-04 | 10B resource schedule |
| **B-05** Cities and production | B-05; URB-111/157 | City list, infrastructure, improvements, production, repair | Damage requests; no city loss; no territory | Damage API with floors | At P5 resolution | City cannot be removed; infrastructure floors enforced | Damage record | Whether cities can be targeted at all | B-05 | 10B target model |
| **B-06** Population and politics | B-06; DMP-092/127/140 | No military modifiers; crisis input; approval hook | War outcome and settlement events | Registered Prompt 10 approval terms only | At P6/P7 | No approval change without a registered term | Approval event | Which war events move approval | B-06 | 10B approval terms |
| **B-07** Trade and markets | B-07 | Trade routes, market access, blockade interaction | Blockade state; resource demand | Trade restriction flag | At P3/P5 | Blockade must not create value | Trade/blockade event | Whether blockade affects market orders | B-07 | 10B blockade scope |
| **B-08** Diplomacy | B-08; DP-T01/DIP-141 | NAP state, treaty parties, war declaration hook | War status to diplomacy; peace/settlement outcome | Declaration validator calls DP-T01 | At submission and execution | Fail-closed | Diplomatic event | Whether peace requires a treaty record | B-08 | 10B NAP activation |
| **B-09** Alliances | B-09; ALL-206…215 | Same-alliance and AT-T01 validators; audit `AUD-AL-017`; no delegation | Attack path calls both checks; war visibility per REQ-590 | Canonical server-side validator | Submission and execution | Fail-closed; no value consumed | Mandatory `AUD-AL-017` | How membership change at boundary affects a pending attack | B-09 | 10B integration contract |
| **B-11** World events, objectives, rankings | B-11 | War outcome events; ranking inputs; objective progress | Conflict results, winners, losses, settlement record | Event feed and ranking snapshot | P6 World evaluation | No retroactive ranking change | World chronicle event | Whether war creates objectives | B-11 | 10B event contract |
| **B-12** Fair play and administration | B-12 | Abuse taxonomy, evidence rules, moderation actions | Detection signals, block records, audit trails | Policy and audit interfaces | Continuous | No automatic punishment from the war engine | Moderation audit | How intent-based abuse is evidenced | B-12 | 10B/P12 boundary |
| **B-13** Interface and journeys | B-13 | War Operations Board, attack confirmation, timeline, settlement screen | Screen requirements and state model | UI specification | At submission and resolution | Clear block reason; no hidden failure | Player-visible history | How odds and outcomes are displayed | B-13 | 10B UI requirements |
| **B-14** Formulas and balance | B-14 | Calibration of OP costs, unit costs, damage, losses, durations | Candidate formulas and ranges | Formula register (B-14, not 10A) | Balance pass | No uncalibrated value ships | Balance change log | Every numeric question in §24 | B-14 | 10B formula proposals |
| **B-15** Cross-system interactions | B-15 | Conflict interactions with economy, politics, alliances, events | A conflict interaction table | Cross-system matrix | Continuous | Conflicting rules resolved by owner | Interaction record | Unresolved cross-system conflicts | B-15 | 10B interaction table |
| **B-16/17** Requirements and unresolved questions | B-16/17 | Traceability, open questions, risks | WCR candidate requirements, WFQ questions, risks | Traceability matrix | At 10B/10C | No orphan requirement | Register update | Which WCR candidates become global REQs | B-16/17 | 10B/10C registers |

### 22.1 Integration invariants

1. **P5 only.** Prompt 10 mutates conflict state only in P5, except for the P3 upkeep/obligation draw that B-04 owns.
2. **Reserve then consume.** Every operation reserves at acceptance and consumes at resolution (B-02 §19; B-04 ECN-214).
3. **No minting.** Loot, reparations and settlement transfers move existing value (B-04).
4. **No city loss.** Infrastructure and improvements may be damaged; cities never transfer (B-05 URB-111).
5. **No delegation.** No alliance or third party spends another nation's OP, units or resources (B-09).
6. **Cumulative validation.** Restricted-pair, protection, national NAP, Alliance NAP and same-alliance checks all run (B-03/B-08/B-09).
7. **Fail closed.** A failed check rejects before execution and moves nothing (ALL-211/215).
8. **Mandatory audit.** Every blocked Alliance-related attack writes `AUD-AL-017` (ALL-214).
9. **No retroactive change.** P6 evaluations describe the turn that happened (B-02 TR-040).
10. **Published only at P7.** No outcome is visible before settlement (B-02).

---

## 23. Candidate warfare requirements

These are **research-scoped candidates** (`WCR-01`…`WCR-44`). They are not global `REQ-` rows, are not approved, and do not bind 10B until 10B adopts or rejects them. They cover 22 areas. Every row has a binding constraint and a proposed 10B action.

| ID | Area | Candidate requirement | Evidence / rationale | Binding constraint | 10B action / verification |
|---|---|---|---|---|---|
| **WCR-01** | Declaration eligibility | Every declaration must pass the restricted-pair, protection, national NAP, Alliance NAP and same-alliance checks before acceptance, on every entry point | B-03 NET-025/026; B-08 DP-T01; B-09 ALL-206/209; REQ-518/642/645 | Cumulative validation; fail closed | Map every entry point; test each block |
| **WCR-02** | Declaration eligibility | A declaration must be refused if the target is outside the declared strength range or the declarer lacks a campaign slot | WFS-033, WFS-022; REQ-014 | REQ-014 | Define NS range and slot count |
| **WCR-03** | War types | A declaration must choose one immutable posture with publicly disclosed damage, loot and cost trade-offs | WFS-003, WFS-022 | Transparency; B-04 | Define postures and disclosure |
| **WCR-04** | War types | A posture must not alter a target's protection status or bypass any attack block | B-03; B-09 | Protection is independent of posture | Test posture × block matrix |
| **WCR-05** | Campaign objectives | Every campaign must state at least one readable objective beyond reducing a meter | WFS-022 shows the gap; REQ-014 | REQ-014 | Define objective catalogue |
| **WCR-06** | Campaign objectives | Objectives must be achievable without geography: no capture, occupation, movement or coordinate | Mapless constraint | Mapless | Review every objective |
| **WCR-07** | Campaign lifecycle | A campaign must have explicit states and one terminal outcome | WFS-022; REQ-014 | B-02 P5 | State machine for 10C |
| **WCR-08** | Campaign lifecycle | A campaign must not remain active indefinitely; expiry must have a defined settlement step | WFS-022; WFR-007 | REQ-014 | Define expiry and settlement |
| **WCR-09** | Operations economy | All military orders must draw on the single national OP pool; no per-war pool | D-015; WFR-006 | **D-015** | Confirm and remove per-war MAP idea |
| **WCR-10** | Operations economy | OP cap, costs and readiness scaling must be published, validated and never purchasable or transferable | D-015 | D-015; D-024 | Propose values for B-14 |
| **WCR-11** | Readiness | Readiness must be player-visible and derivable from declared inputs | WFR-035 | Transparency | Define readiness inputs and display |
| **WCR-12** | Readiness | Readiness must not be an economic multiplier and must not be purchasable with real money | REQ-090; D-015 | REQ-090 | Test no-multiplier rule |
| **WCR-13** | Unit roster | A finite, enumerated unit roster with build caps, upkeep and per-operation resource burn | WFS-011…WFS-017 | B-04; B-05 | Define roster and costs |
| **WCR-14** | Unit roster | Unit losses must be bounded per operation and recoverable through declared production | WFS-024…WFS-026 | B-05 | Define loss caps and rebuild |
| **WCR-15** | Operation catalogue | The operation set must be closed and enumerated; no hidden operation | WFS-022 | Transparency | Publish the list |
| **WCR-16** | Operation catalogue | Each operation must declare OP cost, prerequisites, target class, effects, counterplay and resource burn | WFS-022, WFS-004…WFS-007 | D-015; B-04 | Produce the operation schema |
| **WCR-17** | Battle resolution | Resolution must be deterministic given a published record, or bounded-random with published odds | WFS-022, WFE-07 | Transparency | Choose model and disclose |
| **WCR-18** | Battle resolution | Both sides must be able to read the outcome and its reason after settlement | WFS-022 timeline | Transparency | Define the battle report |
| **WCR-19** | Supply and logistics | Logistics must be inventory/resource-based; no distance, route, depot or convoy | WFR-031 | Mapless | Review every supply rule |
| **WCR-20** | Supply and logistics | A blockade or trade restriction must not stop production or create value, and must be breakable | WFS-010, WFS-030 | B-04 | Define blockade scope |
| **WCR-21** | Protection states | Protection states must be explicit, time-boxed and enforced at every attack path | WFS-032; B-03 ONB-019/020 | B-03; REQ-090 | Align durations |
| **WCR-22** | Protection states | Protection must not be an economic multiplier | REQ-090 | **REQ-090** | Reject P&W's +15% buff form |
| **WCR-23** | Counterplay | Every offensive operation must have at least one declared defender counter | WFS-004, WFS-008…WFS-010 | Transparency | Build the counter matrix |
| **WCR-24** | Counterplay | Control states must be contestable and must expire or break on a declared condition | WFS-008…WFS-010 | Mapless | Define break conditions |
| **WCR-25** | Losses | All losses must be bounded, attributed and recorded; no city or population loss | WFS-031; B-05 URB-111 | **B-05 URB-111** | Define loss ledger |
| **WCR-26** | Losses | Loot and reparations must move existing value, never mint, and respect transfer restrictions | WFS-031; B-04 ECN-214 | **B-04**; ONB-031 | Define transfer caps |
| **WCR-27** | War termination | Victory, mutual peace and expiry must be defined; no unilateral exit may bypass protection | WFS-022, WFS-031 | REQ-014 | Define termination routes |
| **WCR-28** | War termination | Termination must produce a record and a post-conflict protection state | WFS-031 | REQ-014 | Define record and beige analogue |
| **WCR-29** | Settlement | A settlement object must record parties, terms, duration, enforcement and audit | WFS-037 (empty); REQ-014 | UD-032; B-04 | Define settlement schema |
| **WCR-30** | Settlement | Settlement must not compel city deletion, real-world payment or an Alliance obligation without owner consent | WFS-001 rule 15; B-09 | B-05; B-09 | Define prohibited terms |
| **WCR-31** | Alliance integration | Every attack path must call the same-alliance and AT-T01 validators independently and fail closed | ALL-206/209/210/211 | **B-09** | Implement contract in 10B |
| **WCR-32** | Alliance integration | No alliance may order, move, attack with or spend for a member's military; no delegation | ALL-089/139/140; AX-18/30 | **B-09** | Reject any collective power |
| **WCR-33** | Abuse and fair play | War-slot filling, spy-slot filling, collusion and botting must be defined as prohibited with evidence and consequence | WFS-001 rules 4–10 | B-03; Prompt 12 | Hand taxonomy to Prompt 12 |
| **WCR-34** | Abuse and fair play | The war engine must record sufficient evidence without surveillance overreach | WFS-001; B-03 §5.6–5.10 | B-03 | Define evidence fields |
| **WCR-35** | Transparency | Attack confirmation must state OP cost, resource cost, expected effects, counterplay and block reasons | WFS-022; ALL-214 | Transparency | Define confirmation screen |
| **WCR-36** | Transparency | The timeline must be legible to both sides and must not reveal private treaty data beyond the block reason | ALL-214 | B-09 privacy | Define visibility rules |
| **WCR-37** | Mapless conformance | No operation may use coordinates, distance, adjacency, borders, movement, territory or geographic control | Mapless constraint | **Mapless** | Audit every operation |
| **WCR-38** | Mapless conformance | Geographic labels must be renamed or explicitly defined as symbolic | WFC-09, WFC-12 | Mapless | Rename Ground Control/Air Superiority/Blockade if adopted |
| **WCR-39** | Progression | Military progression must be plural and must not dominate economic development | WFS-002; B-11 | B-11 | Define progression tracks |
| **WCR-40** | Progression | Military research/upgrades must be bounded, visible and resettable under declared rules | WFS-002 | B-05/B-14 | Coordinate with B-05 |
| **WCR-41** | Conservation | Every resource and OP movement must be ledgered; no minting, negative balance or hidden transfer | B-04 ECN-214; REQ-177 | **B-04** | Define ledger entries |
| **WCR-42** | Conservation | Reservation and consumption must be atomic; a failed operation releases the reservation | B-02 §19 | B-02 | Define failure path |
| **WCR-43** | Audit and records | Every declaration, operation, block, settlement and termination must write an audit record | B-09 ALL-214; REQ-647 | B-09; B-03 | Define event catalogue |
| **WCR-44** | Audit and records | Audit records must be readable only to authorized roles and must not leak private military or treaty data | B-03 §5.6–5.10; ALL-214 | B-03; B-09 | Define access matrix |

### 23.1 Candidate requirement coverage

| # | Area | IDs |
|---|---|---|
| 1 | Declaration eligibility | WCR-01, WCR-02 |
| 2 | War types | WCR-03, WCR-04 |
| 3 | Campaign objectives | WCR-05, WCR-06 |
| 4 | Campaign lifecycle | WCR-07, WCR-08 |
| 5 | Operations economy | WCR-09, WCR-10 |
| 6 | Readiness | WCR-11, WCR-12 |
| 7 | Unit roster | WCR-13, WCR-14 |
| 8 | Operation catalogue | WCR-15, WCR-16 |
| 9 | Battle resolution | WCR-17, WCR-18 |
| 10 | Supply and logistics | WCR-19, WCR-20 |
| 11 | Protection states | WCR-21, WCR-22 |
| 12 | Counterplay | WCR-23, WCR-24 |
| 13 | Losses | WCR-25, WCR-26 |
| 14 | War termination | WCR-27, WCR-28 |
| 15 | Settlement | WCR-29, WCR-30 |
| 16 | Alliance integration | WCR-31, WCR-32 |
| 17 | Abuse and fair play | WCR-33, WCR-34 |
| 18 | Transparency | WCR-35, WCR-36 |
| 19 | Mapless conformance | WCR-37, WCR-38 |
| 20 | Progression | WCR-39, WCR-40 |
| 21 | Conservation | WCR-41, WCR-42 |
| 22 | Audit and records | WCR-43, WCR-44 |

**22 areas, 44 candidates.** None is approved. 10B must adopt, amend or reject each, and 10C must define acceptance tests for the adopted set.

---

## 24. Formula and numerical research questions

These are the values 10A deliberately did **not** choose. Each row states the question, the available evidence, the owner, the dependency and the decision 10B needs to make. No number here is a Nation Supremacy value.

| ID | Question | P&W evidence | Owner | Depends on | 10B decision |
|---|---|---|---|---|---|
| **WQN-01** | What is the national OP cap? | P&W has no national pool; MAP cap is 12 per war (WFS-022) | Prompt 10 / B-14 | D-015 | Propose a cap and refill rule |
| **WQN-02** | What does a declaration cost in OP? | P&W declaration has no documented cost (WFS-022) | Prompt 10 | D-015 | Propose cost or zero |
| **WQN-03** | What does each operation cost in OP? | P&W: ground 3, naval 4, missile 8, nuke 12, fortify 3; airstrike unknown (WFS-004…WFS-007, WFS-022) | Prompt 10 / B-14 | D-015 | Propose NS costs |
| **WQN-04** | Does OP refill scale with readiness or nation size? | P&W MAP regen is flat +1/turn (WFS-022) | Prompt 10 / B-14 | D-015 | Choose flat or scaled |
| **WQN-05** | What is the conflict progress pool? | P&W resistance is 100 (WFS-022) | Prompt 10 / B-14 | B-02 P5 | Propose pool and reduction values |
| **WQN-06** | How much progress does each victory tier remove? | P&W IT values: ground 10, naval 14, missile 18, nuke 25; air unknown (WFS-005…WFS-007, WFS-019) | Prompt 10 / B-14 | B-02 P5 | Propose a coherent table |
| **WQN-07** | How long may a campaign last? | P&W 60 turns / 5 days (WFS-022) | Prompt 10 | B-02 | Choose duration and expiry |
| **WQN-08** | How many simultaneous campaigns may a nation have? | P&W 5 offensive / 3 defensive (WFS-022) | Prompt 10 | B-02 | Choose NS caps |
| **WQN-09** | What are the unit build caps and recruitment rates? | P&W: 1,000/50/3/1 per building per day (WFS-011…WFS-014) | Prompt 10 / B-14 | B-05 | Propose NS rates |
| **WQN-10** | What are unit build and upkeep costs? | P&W values are specific and rebalanced in July 2025 (WFS-002) | Prompt 10 / B-14 | B-04 | Propose NS costs from NS economy |
| **WQN-11** | What resources does each operation consume? | P&W per-battle gasoline/munitions by unit (WFS-002, WFS-011…WFS-014) | Prompt 10 / B-04 | B-04 ECN-214 | Propose burn table |
| **WQN-12** | What is the infrastructure-damage formula and cap? | P&W formulas in WFE-08…WFE-10, WFE-15 | Prompt 10 / B-14 | B-05 | Propose NS formula |
| **WQN-13** | What is the casualty formula? | P&W formulas in WFE-12…WFE-14 | Prompt 10 / B-14 | B-05 | Propose NS formula |
| **WQN-14** | What percentage of value can loot transfer? | P&W 10% money/resources; 4% infra; bank ≤33% (WFS-031) | Prompt 10 / B-04 | B-04 | Propose caps |
| **WQN-15** | What is the improvement-destruction chance? | P&W 10% ground, 15% naval, 2 missile, 4 nuke (WFS-024…WFS-028) | Prompt 10 / B-14 | B-05 | Propose NS model |
| **WQN-16** | How long does post-defeat protection last? | P&W 2 days; new nations up to 14 days (WFS-031, WFS-032) | Prompt 10 / B-03 | B-03 ONB-019/020 | Align with NS 7-day/84-turn rule |
| **WQN-17** | How long does a settlement last and how is it enforced? | **No P&W evidence** | Prompt 10 / B-08 | UD-032; B-04 | Design from scratch |
| **WQN-18** | What is the reparations cap? | **No P&W evidence** | Prompt 10 / B-04 | B-04; ONB-031 | Design from scratch |
| **WQN-19** | What is the espionage budget and frequency? | P&W: 0 MAP; once/day; cash per op; 1%/1% risk (WFS-022, WFS-029) | Prompt 10 / B-12 | D-024 | Choose separate limits |
| **WQN-20** | How are battle odds disclosed before commitment? | P&W does not publish pre-battle odds; the timeline shows outcomes (WFS-022) | Prompt 10 / B-13 | Transparency | Choose disclosure model |

---

## 25. Source conflicts and evidence gaps

### 25.1 Source conflicts (cross-reference)

The detailed conflict register is §6.1 (`WFX-01`…`WFX-12`). Their effect on this research:

| Conflict | Impact | Treatment in 10A |
|---|---|---|
| **WFX-01** Plane cost/upkeep | Unit economics table has two versions | July 2025 official update (WFS-002) preferred; PWPedia marked outdated |
| **WFX-02** Missile/nuke cost | Strategic-strike economics uncertain | July 2025 preferred; PWPedia marked outdated |
| **WFX-03** Ship operating resources | Logistics cost uncertain | PWPedia + July 2025 agree (1/1.75); Fandom older |
| **WFX-04** Missile infrastructure cap | Exact damage uncertain | Both values reported; no NS value chosen |
| **WFX-05** Aggressor/defender effect | Role itself has no effect; war type does | Stated precisely in §7.1–§7.2 |
| **WFX-06** War range 250% | Upper bound unconfirmed | Marked **UNVERIFIED** |
| **WFX-07** War expiry | Bound known, routine unknown | Recorded as a gap (`GAP-03`) |
| **WFX-08** Peace/settlement | No settlement object | Recorded as a gap and a design requirement |
| **WFX-09** Airstrike MAP/resistance | Air operation cannot be fully specified | WFC-11 is `INVESTIGATE FURTHER` |
| **WFX-10** P&W NAP enforcement | Prior project research says none; not re-verified in 10A | Used only as prior context |
| **WFX-11** PWPedia vs Fandom authority | Official wins on conflict | Applied throughout |
| **WFX-12** Live declaration screen | No direct UI observation | Declared limitation |

### 25.2 Evidence gaps

| ID | Gap | Why it matters | What would close it |
|---|---|---|---|
| **GAP-01** | Airstrike MAP cost and resistance values | Air operations cannot be costed or compared | Official page or in-game action panel (not accessible without login) |
| **GAP-02** | Live declaration screen fields and validation messages | Eligibility UI cannot be described from direct observation | Public documentation or a future access-limited observation |
| **GAP-03** | War expiry routine at turn 60 | Determinism of campaign end is unknown | Official rules page or observed war expiry |
| **GAP-04** | Peace/settlement process and record | No settlement model exists | No P&W equivalent; design from scratch |
| **GAP-05** | Whether 250% war range is live | Strength gate may be 175% or 250% | Official announcement or live UI |
| **GAP-06** | Complete July 2025 changelog date and scope | Currency of unit values | Official changelog archive |
| **GAP-07** | Unit-page revision dates | Some pages are visibly outdated | Revision history not exposed |
| **GAP-08** | Missile 300/350 wording | Exact damage model | Official formula page |
| **GAP-09** | Parentheses in published damage formulas | Formula reproduction risk | Official formula or community re-derivation with tests |
| **GAP-10** | Simultaneous action ordering within a turn | Determinism and fairness | Server behaviour or official statement |
| **GAP-11** | Pre-battle odds disclosure | Transparency model | Live UI or official statement |
| **GAP-12** | Alliance coordination practice | Social layer is undocumented | Not allowed sources (Discord/Reddit); remain inferred |
| **GAP-13** | Moderation evidence standard and appeal process | Fair-play design | Official moderation policy or published appeals page |
| **GAP-14** | DEFCON mechanics | Referenced but undocumented | Official page |
| **GAP-15** | Repair and rebuild rates after damage | Recovery pacing | Official building/repair rules |
| **GAP-16** | Any war-exhaustion equivalent | P&W appears to have none | Design decision, not an evidence gap |

### 25.3 What the gaps mean for confidence

The **structural findings** (mapless, bounded, no alliance command, no supply lines, no settlement) are high confidence because they rest on both positive documentation and documented absence. The **numeric findings** are medium confidence because P&W's pages are partially outdated and the live values are rebalanced over time. The **airstrike** and **pre-battle odds** findings are low confidence and are explicitly marked for further investigation rather than guessed.

---

## 26. Risk register

| ID | Risk | Likelihood | Impact | Evidence / trigger | Mitigation | Owner |
|---|---|---|---|---|---|---|
| **WRK-01** | 10B imports P&W's per-war MAP pools, contradicting D-015 | Medium | High | WFR-006; WFC-06 | State D-015 as a hard constraint in the 10B brief; reject per-war pools at review | Prompt 10B |
| **WRK-02** | 10B copies P&W numbers without calibrating to the NS economy | High | High | WFS-002, WFS-011…WFS-017 | Require every number to pass B-14 calibration; no "P&W value" as justification | 10B / B-14 |
| **WRK-03** | Airstrike cost/effect is guessed because the evidence is missing | High | Medium | WFX-09, GAP-01 | Keep WFC-11 `INVESTIGATE FURTHER`; design air operations from first principles if evidence stays missing | 10B |
| **WRK-04** | Fortify or a similar defensive action enables indefinite stalling | Medium | High | WFS-004; WRK-04 | Bound the defensive state, cap stacking, require an expiry or an attacker counter | 10B |
| **WRK-05** | The loss model is one-sided and produces a runaway snowball | Medium | High | WFS-031; §15.3 | Add catch-up, protection and loss caps; test long-run outcomes | 10B / B-14 |
| **WRK-06** | War-slot filling or shield wars undermine campaign integrity | High | High | WFS-001 rule 4 | Define prohibited intent, evidence and consequence; audit blocked/empty wars | 10B / Prompt 12 |
| **WRK-07** | Multi-accounting or same-network collusion multiplies war slots | Medium | High | WFS-001 rules 1–2 | One-account policy; network-aware restrictions; collusion evidence; no IP-only ban | B-03 / Prompt 12 |
| **WRK-08** | Settlement terms become coercive (city deletion, real-world payment, forced alliance obligation) | Medium | High | WFS-001 rule 15; B-05; B-09 | Prohibited-terms list; owner consent for alliance obligations; audit | 10B / 10C |
| **WRK-09** | Loot or reparations mint value or bypass B-04 conservation | Medium | High | B-04 ECN-214; REQ-177 | Ledger-only transfers from existing stockpiles; negative-balance prevention; tests | 10B / B-04 |
| **WRK-10** | Alliance command creep: a "war room" or "operations" feature starts spending member resources | Medium | High | ALL-089/139/140; AX-18/30 | No delegation; no shared pool; read-only coordination; contract tests | 10B / B-09 |
| **WRK-11** | Geographic language ("front", "territory", "blockade line") reintroduces map thinking | High | Medium | Mapless constraint; §19.2 | Rename states; audit every operation and screen for geographic terms | 10B / B-13 |
| **WRK-12** | Opaque resolution destroys player trust and invites "rigged" accusations | Medium | High | WFR-009; §7.7 | Publish odds or a confidence range; publish the battle record; explain blocks | 10B / B-13 |
| **WRK-13** | Audit or visibility leaks private treaty/military data | Low | High | ALL-214; REQ-590 | Role-based audit access; redact private terms; test negative cases | B-09 / B-12 |
| **WRK-14** | Protection durations conflict with B-03 (P&W 14 days vs NS 7 days/84 turns) | High | Medium | WFS-032; ONB-019/020 | Treat B-03 as authoritative; do not import P&W durations | 10B |
| **WRK-15** | UD-032 stays unresolved and a reroll escapes a losing campaign | Medium | High | RRL-021; UD-032 | Keep the interim block; require 10B to decide among the three options; audit | Prompt 10B |

---

## 27. Open research-question register

These are **research** questions, not design decisions. `WFQ-01`…`WFQ-22` remain open unless the Status column says otherwise.

| ID | Question | Status | What we know | What is missing | Impact if unresolved | Owner |
|---|---|---|---|---|---|---|
| **WFQ-01** | What are the airstrike MAP cost and resistance values? | **Open** | The action exists and has a formula; cost/effect not stated | Official values | Air operations cannot be compared or costed | 10B |
| **WFQ-02** | Is the 250% war-range maximum live? | **Open** | Formula says 2.50; wiki says unconfirmed in 2023 | Deployment confirmation | Strength gate uncertain | Research / 10B |
| **WFQ-03** | What exactly happens at turn 60? | **Open** | Wars "can last up to 60 turns" | Expiry routine | Campaign end determinism | 10B |
| **WFQ-04** | Are simultaneous attacks resolved in a fixed order? | **Open** | No public statement | Server ordering | Fairness and reproducibility | 10B / B-02 |
| **WFQ-05** | Are pre-battle odds shown to players? | **Open** | Timeline shows outcomes; no odds page observed | UI behaviour | Transparency model | 10B / B-13 |
| **WFQ-06** | Is there a hidden war score beyond resistance? | **Open** | Only resistance is documented | Any secondary score | Win-condition clarity | 10B |
| **WFQ-07** | Does blockade affect production, not just trade/bank? | **Likely no** | WFS-030 says trade/bank; production not mentioned | Explicit statement | Logistics model | 10B |
| **WFQ-08** | Does radiation affect combat values or only disease/food? | **Likely only economy** | WFS-028 says disease and food | Explicit statement | Escalation design | 10B |
| **WFQ-09** | Do defensive wars consume the same slot rules as offensive wars? | **Partially answered** | 3 defensive slots documented | Interaction with offensive slots | Slot design | 10B |
| **WFQ-10** | Can a nation declare on a nation whose beige expires mid-war? | **Open** | Beige blocks new declarations; expiry rules unclear | Edge-case rule | Protection integrity | 10B |
| **WFQ-11** | Do existing wars continue after defeat? | **Yes** | WFS-031 says existing wars may continue | Exact scope | Postwar model | 10B |
| **WFQ-12** | Is there any peace-treaty record? | **No evidence** | Offer Peace only | Any record | Settlement design | 10B |
| **WFQ-13** | Can a blockaded nation still receive alliance-bank transfers? | **Partially answered** | WFS-030 says no deposit/withdraw; a high-rank member may transfer out | Exact permission rules | Blockade design | 10B |
| **WFQ-14** | Are inactive wars auto-peaced? | **Open** | Inactivity deletion exists | War cleanup | Stale-war handling | 10B |
| **WFQ-15** | Is there a declaration cooldown after peace? | **No evidence** | No rule found | Any cooldown | Tempo abuse | 10B |
| **WFQ-16** | Does war type affect resistance reduction? | **Likely no** | War type affects damage/loot, not resistance | Explicit statement | Posture design | 10B |
| **WFQ-17** | Does Fortify stack with a war policy? | **Likely yes, no extra effect** | Fortify says multiple uses = one effect; policy is separate | Explicit interaction | Defense stacking | 10B |
| **WFQ-18** | Does Ground Control transfer between wars? | **Partially answered** | It nullifies enemy control in all wars; control is per war | Exact scope | Multi-war design | 10B |
| **WFQ-19** | Does Air Superiority affect naval battles? | **No evidence** | It halves tanks only | Any naval effect | Domain interaction | 10B |
| **WFQ-20** | How are multiple wars' MAP pools displayed? | **Open** | Pools are per war | UI | Player comprehension | 10B / B-13 |
| **WFQ-21** | Is there any war-exhaustion or morale mechanic? | **No evidence** | None found | Any hidden state | Long-war design | 10B |
| **WFQ-22** | What happens to war state when a nation is deleted? | **Open** | Deletion is irreversible; war cleanup not documented | Exact rule | Reroll/deletion edge | 10B / UD-032 |

---

## 28. Dedicated UD-032 analysis

### 28.1 The question and its current state

**UD-032:** "What happens to an active campaign when a participant rerolls: block, forfeit, or finish for the old nation?" (B-03 §21.3; `05_unresolved_design_decisions.md` row UD-032).

- **Class:** B (provisional choice).
- **Current interim rule:** Prompt 03 **fails closed** — `RRL-021` blocks the reroll while a campaign is active, because no forfeit rule exists.
- **Owner:** "No — Prompt 10 decides."
- **Status:** **Deferred to Prompt 10.** 10A does **not** resolve it.
- **Related requirements:** REQ-085 (deterministic warfare cleanup), REQ-086 (reroll blocked by active campaign, unsettled settlement, preservation hold or disqualifying state).
- **Related rules:** B-03 RRL-019 (warfare cleanup; reroll blocked during an active campaign), RRL-021 (blocking conditions), B-03 §18 (attribution: battle history stays with the old nation; reroll removes ranking and writes a retirement event); B-04 ECN-130 (reroll destroys inventory).

### 28.2 Why the question is hard

A reroll is simultaneously:
1. a **player-protection** act (a player may want a fresh start),
2. a **campaign-integrity** event (an opponent may lose a war they were winning),
3. an **attribution** event (records must remain with the old nation),
4. an **economic** event (inventory is destroyed; B-04 ECN-130),
5. an **abuse** vector (reroll to escape a loss, to shed a settlement, or to launder a reputation).

Any option must satisfy all five. P&W provides **no evidence** for any option because it has no campaign object and no transferable identity; its closest rules are inactivity deletion and one-nation-per-player (WFS-001). The analysis below is therefore **Nation Supremacy-internal**, not comparative.

### 28.3 Option A — Keep the block

| Dimension | Analysis |
|---|---|
| **Mechanism** | The reroll is refused while the campaign is active. The player must finish, settle or wait out the campaign before rerolling |
| **Current status** | This is the **existing interim rule** (`RRL-021`); it is safe and observable |
| **Exploit resistance** | **High**: the player cannot escape a losing war, a settlement or an attribution record |
| **Fairness to the opponent** | **High**: the opponent keeps the war they earned |
| **Record integrity** | **High**: the old nation's history remains intact; no successor ambiguity |
| **B-03 compatibility** | **High**: it is already the B-03 rule; REQ-086 names it |
| **B-04 compatibility** | **High**: no transfer occurs; inventory is not duplicated |
| **Implementation complexity** | **Low**: the block already exists; 10B only needs to define "active campaign" precisely |
| **Player clarity** | **Medium**: a player may feel trapped; the reason must be explicit and the path to reroll must be shown |
| **Settlement interaction** | **High**: an unsettled settlement also blocks; the two blocks must not double-punish |
| **Risks** | Player frustration; support burden; a player who wants to leave the game may feel forced to stay; an indefinitely active campaign could block a legitimate reroll |
| **Mitigations** | Clear explanation; a visible countdown or completion path; a campaign expiry; a support/exception process owned by Prompt 12, not invented here |
| **Evidence** | None from P&W; the rule is NS-internal |

### 28.4 Option B — Forfeit with a recorded outcome

| Dimension | Analysis |
|---|---|
| **Mechanism** | The reroll is allowed; the active campaign ends with a **forfeit** recorded against the old nation; the opponent receives a defined outcome (win by forfeit) |
| **Exploit resistance** | **Medium**: a player can still escape a losing war, but at the cost of a recorded loss; the forfeit must not be rewardable |
| **Fairness to the opponent** | **Medium-High**: the opponent gets a win, but not the loot or satisfaction of a fought victory |
| **Record integrity** | **Medium**: the record must name the old nation, the forfeit, the turn and the opponent; the successor must not inherit the win |
| **B-03 compatibility** | **Medium**: requires new rules for attribution, ranking and retirement; must not transfer first-time rewards |
| **B-04 compatibility** | **Medium**: a forfeit must not create loot from nothing; any transfer must come from the old inventory, which is destroyed on reroll (ECN-130), so a forfeit likely pays **no loot** |
| **Implementation complexity** | **High**: forfeit object, outcome attribution, ranking update, audit, settlement interaction |
| **Player clarity** | **High**: "you may reroll, but you forfeit the war" is understandable |
| **Settlement interaction** | **High**: an unsettled settlement must not be erased by a forfeit; the settlement must survive against the old identity or be explicitly voided |
| **Risks** | Reroll-to-escape; collusive forfeits; a opponent receiving a hollow win; a successor being treated as the same player for abuse purposes |
| **Mitigations** | No loot for a forfeit; a recorded loss; a cooldown; audit; no reward transfer; collusion detection; settlement survival rule |
| **Evidence** | None from P&W; a new NS rule |

### 28.5 Option C — Let the campaign finish under the old identity

| Dimension | Analysis |
|---|---|
| **Mechanism** | The reroll proceeds; the campaign continues to its end under the **old nation's identity**; the new nation does not inherit the war |
| **Exploit resistance** | **Low-Medium**: the player can start a new nation while the old one is still a target; the old identity may be a "ghost" that cannot fight back |
| **Fairness to the opponent** | **Low**: the opponent may be fighting an abandoned identity with no player behind it |
| **Record integrity** | **High for attribution** (the old identity keeps its history) but **low for outcome** (a ghost may auto-lose or stall) |
| **B-03 compatibility** | **Medium**: requires a rule for who controls the old identity after reroll; likely "nobody", which means auto-resolution |
| **B-04 compatibility** | **Medium-High**: the old inventory is destroyed; the campaign must not mint or transfer it |
| **Implementation complexity** | **High**: a "ghost nation" state, auto-resolution, turn processing, protection, settlement |
| **Player clarity** | **Medium**: "your old nation will finish its war without you" is unusual and may feel unfair either way |
| **Settlement interaction** | **High**: a settlement could be imposed on a ghost; who consents? |
| **Risks** | Ghost farming; auto-loss exploitation; opponent frustration; identity confusion; support burden |
| **Mitigations** | Auto-resolution after a short grace period; no player control; no loot from a ghost; audit; a clear retirement event |
| **Evidence** | None from P&W; a new NS rule |

### 28.6 Comparative matrix

| Criterion | A — Keep block | B — Forfeit | C — Finish under old identity |
|---|---|---|---|
| Exploit resistance | **High** | Medium | Low-Medium |
| Fairness to opponent | **High** | Medium-High | Low |
| Record integrity | **High** | Medium | High attribution / low outcome |
| B-03 compatibility | **High** (existing rule) | Medium | Medium |
| B-04 compatibility | **High** | Medium | Medium-High |
| Implementation complexity | **Low** | High | High |
| Player clarity | Medium | **High** | Medium |
| Settlement interaction | **High** | High | High |
| Support burden | Low-Medium | Medium | **High** |
| Evidence from P&W | None | None | None |

### 28.7 Research observations (not a resolution)

1. **Option A is the only option already implemented as an interim rule**, and it is the only one that requires no new attribution or economic rule.
2. **Option B is the only option that gives the player a path out** while preserving a record; it requires a no-loot rule to avoid minting and a settlement-survival rule.
3. **Option C creates a control vacuum** (a nation with no player) and therefore needs an auto-resolution rule, which is itself a new campaign mechanic.
4. **All three options interact with settlement** and with B-03 §18 attribution. None can be decided without 10B's campaign and settlement model.
5. **10A does not select an option.** UD-032 remains **Deferred to Prompt 10**. 10B must decide, record the decision, and update the UD register through the normal process.

---

## 29. Prompt 10B handoff

Prompt 10B must produce the authoritative warfare rulebook (B-10). This handoff is organized as six blocks, `WFH-A`…`WFH-F`, each with six items.

### A. Scope and non-goals

| ID | Handoff item |
|---|---|
| **WFH-A1** | Write B-10 as a rulebook, not research. Do not repeat the P&W catalogue; cite this report where evidence is needed |
| **WFH-A2** | Keep warfare mapless: no fronts, maps, provinces, tiles, adjacency, borders, movement, capture, coordinates, geographic supply or geographic control |
| **WFH-A3** | Keep the D-015 Operations Points model: one national pool, military-only, refilled to cap, non-transferable, reserved at acceptance, consumed at resolution |
| **WFH-A4** | Do not resolve UD-032 by assumption; decide it explicitly and record the decision |
| **WFH-A5** | Do not create an Alliance military power, delegation, shared pool or collective command; B-09 owns that boundary |
| **WFH-A6** | Do not approve numeric values in 10B without B-14 calibration; mark every number Provisional until then |

### B. Decisions 10B must make

| ID | Decision needed | Input from 10A |
|---|---|---|
| **WFH-B1** | Campaign model: nation-war only, or a campaign object above it | §13.3; WFC-01, WFC-07 |
| **WFH-B2** | Progress model: one pool per war, one per campaign, or one national | WFR-006; WFC-06 |
| **WFH-B3** | Posture/war-type model and whether it is immutable | WFC-03 |
| **WFH-B4** | Operation catalogue and OP costs | §9; §24 |
| **WFH-B5** | Resolution model and disclosure of odds | WFC-08; §7.7 |
| **WFH-B6** | Termination and settlement model, including the UD-032 choice | §16; §28 |

### C. Proposed B-10 structure

| ID | Section |
|---|---|
| **WFH-C1** | Purpose, scope, binding constraints and mapless conformance |
| **WFH-C2** | Declaration, eligibility, protection and cumulative validation |
| **WFH-C3** | Campaign states, objectives, duration and expiry |
| **WFH-C4** | Operations, OP costs, readiness, units and resources |
| **WFH-C5** | Resolution, control states, counterplay and losses |
| **WFH-C6** | Termination, settlement, postwar, audit and open questions |

### D. Constraints and invariants

| ID | Invariant |
|---|---|
| **WFH-D1** | P5-only mutation; reserve at acceptance; consume at resolution |
| **WFH-D2** | No minting; all value moves through the B-04 ledger |
| **WFH-D3** | No city loss; infrastructure and improvements may be damaged |
| **WFH-D4** | Cumulative attack validation: restricted pair, protection, national NAP, Alliance NAP, same-alliance |
| **WFH-D5** | Fail closed; a blocked attack moves nothing; mandatory `AUD-AL-017` |
| **WFH-D6** | No delegation; no collective military power; no alliance spending of member resources |

### E. Acceptance and done criteria

| ID | Criterion |
|---|---|
| **WFH-E1** | Two nations can fight a bounded war with a readable outcome |
| **WFH-E2** | There is a way to stop: mutual peace, expiry and/or settlement |
| **WFH-E3** | No infinite one-sided attrition: a bound, a catch-up or an off-ramp exists |
| **WFH-E4** | Every offensive operation has a declared counter |
| **WFH-E5** | Every attack path is covered by the cumulative validator and tested for bypass |
| **WFH-E6** | Every number is Provisional and traceable to B-14 |

### F. Open questions carried into 10B

| ID | Question |
|---|---|
| **WFH-F1** | Airstrike cost/effect (GAP-01) |
| **WFH-F2** | War expiry routine (GAP-03) |
| **WFH-F3** | Simultaneous action ordering (GAP-10) |
| **WFH-F4** | Pre-battle odds disclosure (GAP-11) |
| **WFH-F5** | Settlement enforcement and duration (GAP-04) |
| **WFH-F6** | UD-032 option (A, B or C) |

---

## 30. Prompt 10C and downstream handoffs

### 30.1 Prompt 10C — workflows and acceptance

| Item | Handoff |
|---|---|
| **States** | Campaign states, operation states, block states, settlement states, termination states, recovery states |
| **Happy paths** | Declaration → operation → resolution → control → victory/peace → settlement → postwar |
| **Permission failures** | Restricted pair, protection, NAP, Alliance NAP, same-alliance, insufficient OP, insufficient resources, no slot, invalid target |
| **Edge cases** | Membership change at boundary, NAP expiry during a campaign, reroll during a campaign (UD-032), target protection expiry, simultaneous attacks, expiry at 60 turns |
| **Recovery** | Failed P5 phase, interrupted turn, reservation release, duplicate-run refusal |
| **Matrix** | Bidirectional and exhaustive; no orphan identifiers |
| **Boundary** | Workflows are specifications, not code; tests are defined, not executed |
| **Must not add** | No new Alliance rule, no NAP coverage/consent rule, no treasury-spending authority, no appeal right |

### 30.2 Downstream prompts

| Prompt | Receives from 10A/10B | Must not assume |
|---|---|---|
| **Prompt 11** — world events, objectives, rankings | Conflict outcome events, ranking inputs, campaign objectives, settlement record | That P&W's rankings or war score exist in NS |
| **Prompt 12** — fair play, protection, privacy, administration | Abuse taxonomy, block records, audit duties, evidence fields | That P&W's moderation model or penalties apply |
| **Prompt 13** — interface and journeys | War Operations Board, attack confirmation, timeline, settlement screen, block reasons | That the UI may hide a block instead of explaining it |
| **Prompt 14** — formulas and balance | WQN questions, WFE evidence, calibration needs | That P&W numbers are NS values |
| **Prompt 15** — cross-system interactions | Integration matrix and invariants | That P5 can mutate other systems outside their phases |
| **Prompt 16/17** — requirements and unresolved questions | WCR candidates, WFQ questions, WRK risks | That WCR candidates are approved REQs |
| **Prompt 18** — revision and change control | Version, sources, conflict register | That a source revision silently changes a rule |
| **Prompt 19** — completion and acceptance | Checklist, validation evidence, limitations | That documentation tests are gameplay tests |

### 30.3 What downstream must not inherit

- P&W's per-war MAP pools (rejected).
- P&W's 14-day new-nation beige (conflicts with B-03's 7 days/84 turns).
- P&W's +15% beige recruitment buff (conflicts with REQ-090's no-economic-multiplier rule).
- P&W's nuclear radiation as a continental effect (no continents in NS).
- P&W's moderation-only enforcement (NS requires prevention and audit).
- P&W's absence of settlement (NS requires a settlement framework).

---

## 31. Completion checklist

| # | Check | Status |
|---|---|---|
| 1 | Exactly 35 numbered sections | Complete (§1–§35) |
| 2 | Section 1 is an executive summary | Complete |
| 3 | Section 2 states scope and restrictions | Complete |
| 4 | Section 3 states date and methodology | Complete |
| 5 | Section 4 inventories project documents | Complete |
| 6 | Section 5 states the existing NS warfare baseline | Complete |
| 7 | Section 6 is a P&W source register with exact URLs, categories, access dates and limitations | Complete (40 sources) |
| 8 | Section 7 catalogues P&W mechanics | Complete |
| 9 | Section 8 records evidence-backed findings | Complete (52 findings) |
| 10 | Section 9 is a complete attack/operation matrix | Complete (9 actions + 4 naval options + 9 espionage operations) |
| 11 | Section 10 records battle-resolution and formula evidence | Complete (16 formula entries) |
| 12 | Section 11 covers readiness and resources | Complete |
| 13 | Section 12 covers supply and logistics | Complete |
| 14 | Section 13 covers the campaign lifecycle | Complete |
| 15 | Section 14 covers protection and counterplay | Complete |
| 16 | Section 15 covers losses and economic effects | Complete |
| 17 | Section 16 covers war termination and postwar | Complete |
| 18 | Section 17 covers alliance warfare and coordination | Complete |
| 19 | Section 18 covers abuse and fairness | Complete |
| 20 | Section 19 performs the mapless suitability analysis | Complete |
| 21 | Section 20 classifies P&W mechanics for NS | Complete (26 classifications) |
| 22 | Section 21 lists approved and provisional constraints | Complete |
| 23 | Section 22 is the cross-system integration matrix | Complete (16 systems) |
| 24 | Section 23 provides candidate requirements | Complete (44 candidates, 22 areas) |
| 25 | Section 24 lists formula and numerical research questions | Complete (20 questions) |
| 26 | Section 25 records source conflicts and evidence gaps | Complete |
| 27 | Section 26 is a risk register | Complete (15 risks) |
| 28 | Section 27 is an open research-question register | Complete (22 questions) |
| 29 | Section 28 analyses UD-032 without resolving it | Complete |
| 30 | Section 29 is the 10B handoff | Complete (A–F) |
| 31 | Section 30 is the 10C and downstream handoff | Complete |
| 32 | Section 31 is the completion checklist | Complete |
| 33 | Section 32 records validation actually performed | Complete |
| 34 | Section 33 lists files created and updated | Complete |
| 35 | Section 34 lists files intentionally not changed | Complete |
| 36 | Section 35 states limitations | Complete |

**Current status:** all 35 sections are written. The report is **complete at the research/documentation level**. It approves no B-10 rule and no formula value, and claims no implementation or runtime evidence.

---

## 32. Validation actually performed

This section records only checks that were executed and inspected. **Documentation checks are not gameplay, runtime, database, browser, load, security or playability tests**, and none of those was run because no warfare implementation exists.

### 32.1 Research-integrity checks

| Check | Method | Result |
|---|---|---|
| Every cited source is a page actually opened | Manual re-read of each `WFS-` row against the page it names; URL, heading, category and access date re-checked | Complete for all 40 sources; the register states the evidence limit per row |
| Source categories are correct | Each source classified as LIVE-DIRECT, OFFICIAL-DOC, P&W-WIKI or HISTORICAL, with community-wiki ownership named and never called official | Complete |
| Findings are evidence-backed | Each `WFR-` row cites at least one `WFS-` source or is explicitly marked INFERRED or UNVERIFIED | Complete for all 52 findings |
| Disagreements are recorded, not resolved silently | Every conflicting pair is carried in `WFX-01`…`WFX-12`; the report does not pick a winner where the sources disagree | Complete |
| No prohibited source or technique | Sources re-scanned for non-P&W games, forums, Reddit, Discord, YouTube, blogs, encyclopedias, military research and AI summaries; no private API, database, source-code, hidden-endpoint, developer-tools extraction, scraping, modification or data-mining technique is used | Complete; no violation found |
| No state-changing action | Research was read-only: no sign-in, credential request, transaction, war declaration, message, account change or other game-state change | Complete |
| Mapless conformance | Every mechanic in §19 tested against the ban on fronts, maps, provinces, tiles, adjacency, borders, movement, capture, coordinates, geographic supply and geographic control; incompatible mechanics are classified REJECT or ADAPT, not imported | Complete |
| Identifier integrity | `WFS` 40, `WFR` 52, `WFE` 16, `WFX` 12, `WFC` 26, `WCR` 44, `WQN` 20, `WRK` 15, `WFQ` 22, `GAP` 16, `WFH` 36 unique | Complete |
| No global requirement or decision created | `03_requirements_traceability.md`, `04_approved_and_provisional_decisions.md`, `05_unresolved_design_decisions.md` and `DECISIONS.md` inspected; no `REQ-` row, `D-` entry or `DD-` position was added by 10A | Complete |
| UD-032 unresolved | All three options analysed; no selection, no owner decision, no status change | Complete |

### 32.2 Documentation validators executed

All commands were run from `docs/qa_backups` against the final working tree on 2026-11-03.

| Command | Result | Exit code |
|---|---|---|
| `python validate_final.py` | ALL CHECKS PASSED | 0 |
| `python 09_validate.py` | 359/359 checks passed | 0 |
| `python 09B_validate_alliance_semantic.py` | 34/34 semantic checks passed; printed status names 10A complete and 10B next | 0 |
| `python 09A_validate_alliance.py` | 943 checks passed | 0 |
| `python verify_politics_numbers.py` | 879/879 checks passed | 0 |
| `python -m unittest test_next_action` | 25 tests OK (0.149 s) | 0 |
| `python -m unittest test_decision_registers` | 12 tests OK | 0 |
| `python -m unittest test_09A_alliance_validator` | 43 tests OK (12.487 s) | 0 |
| Six status-sensitive `test_09B_alliance_semantic_validator` regressions (`test_06`, `test_57`, `test_58`, `test_58b`, `test_59`, `test_60`) | 6 tests OK (58.480 s) | 0 |
| `python -m py_compile` over the ten modified QA scripts | Compiled without error | 0 |

**Not run.** The full 267-test historical `test_09B_alliance_semantic_validator` suite (long-running and outside this focused pass); the economy, city, market, diplomacy workflow and diplomacy number verifiers and the other prompt-specific suites beyond those listed; and every runtime, database, browser, load, security and playability test. No unexecuted suite is reported as passed.

### 32.3 What the validators prove — and do not prove

The validators prove that the continuity files agree on `stage_2_next_prompt: 10B`, that the Stage 2 registers and the progress log record 10A complete with 10B next and 10C pending, that the roadmap and outline register Prompt 10A with its canonical report, that the Phase 09B acceptance sentence and every UD status survive unchanged, and that the existing rule, formula, requirement and decision identifiers remain intact. They do **not** prove that any Politics and War statement in this report is true beyond the cited access date, that a Nation Supremacy rule is correct, or that any mechanic works in a game. No such claim is made.

## 33. Files created and updated

### 33.1 Created

| File | Purpose |
|---|---|
| `docs/stage-2/research/10A_politics_and_war_warfare_research.md` | This report — the canonical 10A deliverable (35 sections, 40 sources, 52 findings, 26 classifications, 44 candidate requirements) |

### 33.2 Updated (documentation only)

| File | Change |
|---|---|
| `docs/AI_CONTEXT.md` | 10A status in the opening blockquote, Last updated line and STATUS block (`stage_2_next_prompt: 10B`); research index row; stage-plan, progress-log index, risk and war-system bullets |
| `docs/AI_HANDOFF.md` | 10A status, Last updated line, STATUS block, §H opening and §H.6, and the 10A paragraph with its registers and counts |
| `docs/PROJECT_PROGRESS.md` | 10A status, Last updated line, STATUS block, Stage 2 heading, rows 09 and 10, continuity paragraph and alliance status tail |
| `docs/ROADMAP.md` | 10A complete / 10B next / 10C pending in the status blockquote, Status line, Stage 2 table row and its research link |
| `docs/stage-2/00_stage_2_handoff.md` | 10A status in the opening blockquote, revision line, Status and Next task |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | 10A/10B/10C registered; the 10A row links the canonical report; the Prompt 10 section gains the sub-prompt register; 11–15 remain pending |
| `docs/stage-2/02_master_game_design_bible_outline.md` | B-10 row links the 10A report, records that it approves no rule, keeps the `17_warfare_and_settlements.md` path and moves to v1.9; §5 prompts-executed, next-prompt and Bible-status rows updated |
| `docs/stage-2/03_requirements_traceability.md` | Metadata only (v1.29): records that the 44 `WCR-` candidates are research-scoped and that no `REQ-` row, status or count changed (55/578/17/3/0 = 653) |
| `docs/stage-2/05_unresolved_design_decisions.md` | UD-032 only (v1.25): evidence and 10B-handoff references; status, owner, class and counts unchanged (26/5/18 = 49) |
| `docs/stage-2/06_stage_2_progress_log.md` | Header, table rows 09 and 10, and the §56 entry |
| `docs/qa_backups/status_rules.py` | `CURRENT_SUBPROMPT = "10B"`; `10A` added to `COMPLETED_SUBPROMPTS`; sub-prompt pattern widened to the 10 family |
| `docs/qa_backups/test_next_action.py` | 10B/row 09/row 10 assertions; two new 10A/10B regressions |
| `docs/qa_backups/test_decision_registers.py` | 10B/row 09/row 10 assertions; Stage 2 row-10 selector corrected by title |
| `docs/qa_backups/validate_final.py` | Expected next prompt 10B; 10-family handoff guard; row 09/row 10 wording; 01-roadmap 10A/10B/10C registration; 10A report in the required-document list; ROADMAP check |
| `docs/qa_backups/09_validate.py` | Status, header, §H and row checks advanced to 10B; row 10 checks added |
| `docs/qa_backups/09A_validate_alliance.py` | Accepts the 10 family on the STATUS line |
| `docs/qa_backups/test_09A_alliance_validator.py` | Fixture status changed from 10B to 09C so the negative test still exercises its own case |
| `docs/qa_backups/09B_validate_alliance_semantic.py` | Accepts `10`/`10A`/`10B`/`10C`; printed status corrected |
| `docs/qa_backups/test_09B_alliance_semantic_validator.py` | Fixture status changed from 10B to 09 so the C18 negative test still fails as intended |
| `docs/qa_backups/verify_politics_numbers.py` | Row 09 and row 10 checks added |

## 34. Files intentionally not changed

| Area | Files | Why |
|---|---|---|
| Warfare rulebook | none exists — `17_warfare_and_settlements.md` was **not** created | 10A is research; B-10 belongs to Prompt 10B |
| Approved rulebooks | B-02 `07_…`, B-03 `09_…`, B-04 `10_…`, B-05 `11_…`, B-06 `12_…`, B-07 `13_…`, B-08 `15_…`, B-09 `16_alliances.md` | Research must not rewrite an approved rule |
| Formula registers | `10_economic_…`, `11_city_…`, `12_population_…`, `13_trade_…`, `15_diplomacy_…`, `16_alliances_…` | No 10A formula is approved; B-10's register does not exist yet |
| Alliance workflow companion | `16_alliances_workflows_acceptance.md` | Accepted at the documentation level; out of scope |
| Earlier research | `04_…`, `05_…`, `06_…`, `07A_…`, `08A_…`, `09A_…` reports | Historical evidence base; not regenerated |
| Decisions | `DECISIONS.md`, `04_approved_and_provisional_decisions.md` | No new `D-` or `DD-` entry; UD-032 unresolved |
| Owner policy | `AUTONOMOUS_DECISION_POLICY.md`, `05_unresolved_design_decisions.md` statuses | Owner-reserved decisions preserved |
| Stage 1 | `docs/stage-1/*` | Closed record; not reopened |
| Application | application source, `prototypes/*` | No implementation work in 10A |
| Data and infrastructure | database schemas, migrations, Cloudflare/Supabase configuration, live data | Read-only research; no state change |

`03_requirements_traceability.md` and `05_unresolved_design_decisions.md` were edited for **metadata and evidence references only**; no requirement or decision row was added, removed, renumbered or status-changed.

## 35. Limitations

1. **Access limits.** The research observed only publicly reachable pages. Pages behind a login, an account, a war screen, an alliance screen or any player-specific state were not examined, and the report does not describe them as if they were. Some pages expose no revision date; where that is so, the register says so rather than inventing one.
2. **Interface change.** Politics and War is a live service. A value or rule described here was true on its access date and may change without notice; the access date is recorded per source precisely because of this.
3. **Community sources.** Community wikis dedicated to Politics and War are player-maintained. Their ownership is named, they are graded `P&W-WIKI` or `HISTORICAL`, and they are never treated as official documentation or as stronger evidence than the live interface.
4. **Disagreement.** Where sources conflict, the conflict is preserved as `WFX-01`…`WFX-12`. The report does not claim a single authoritative value when the evidence does not support one.
5. **No internal access.** No private API, database, source code, hidden endpoint, developer-tools extraction, automated scrape, modification or data-mining was used, so internal implementation details — rounding order, concurrency, server timing — are not evidenced.
6. **Design distance.** Every `WFC-` classification is a design judgement about Nation Supremacy, not a finding about Politics and War. A mechanic that works in one game may be unsuitable here, and the report says so where it applies.
7. **Mapless constraint.** The `S0`–`S7` lifecycle, the operation catalogue and the loss model are abstractions built to fit a mapless symbolic world. They are proposals for 10B, not validated designs and not approved rules.
8. **Numbers.** No cap, cost, damage, resistance, readiness, duration or formula value is approved. All `WFE` and `WQN` entries are evidence or questions for B-14 calibration; every number stays Provisional until then.
9. **UD-032.** The question is analysed, not answered. Prompt 10B must decide it explicitly; 10A neither selects an option nor manufactures an owner decision.
10. **Candidate requirements.** The 44 `WCR-` items are research-scoped candidates. They are not `REQ-` rows, carry no approval, and may be promoted, adapted or rejected only by Prompt 10B.
11. **No implementation or runtime evidence.** There is no warfare code, table, endpoint, scheduler, validator or screen. No runtime, database, browser, load, security, multiplayer or playability test was run, and this report claims none.
12. **Validation scope.** The validators listed in §32 are documentation checks over the continuity files, registers and report structure. They cannot prove a Politics and War fact, the correctness of a rule or the behaviour of a game.

---
