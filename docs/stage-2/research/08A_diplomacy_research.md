# Diplomacy research, evidence, requirements and cross-system integration — Stage 2 Prompt 08A

**Version:** 1.0 · **Created:** 2026-10-29 · **Stage 2, Prompt 08A** · **Research and documentation only** · **Dated annotation 2026-11-04 (Prompt 10B-C3):** the `A-09` integration row carries a terminology note — the Alliance owns no war room; the war surface is B-10's nation-level, owner-only War Operations Board. No source, finding, conflict, question or candidate recommendation changed.
**Status:** Research complete at the documentation level. **No Nation Supremacy diplomacy rule, relationship status, treaty type, sanction, reputation register, permission or formula is approved by this document.** The findings are evidence for **Prompt 08B**, not decisions. **Prompt 08B and Prompt 08C have not started.**
**Research access date:** 2026-10-29. Every URL in §5 was read on that date unless the row states otherwise. No authenticated session, account action, in-game action or API credential was used.
**Parent task:** Stage 2, **Prompt 08 — diplomacy between nations** ([stage-2/01 §3](../01_stage_2_prompt_roadmap.md)). This report is the **08A** subphase only: research, requirements analysis, integration audit and handoff. It is **not** the B-08 diplomacy specification, which remains **08B's** deliverable.
**Identifier spaces used here:** sources **`DPS-001…DPS-019`** ("diplomacy politics source"); findings **`DPR-001…DPR-054`**; conflicts **`DPX-01…DPX-06`**; candidate recommendations **`DCR-01…DCR-12`**; questions for 08B/08C/09 **`DQ-01…DQ-16`**. None of these collides with the project's `D-`, `DD-`, `UD-`, `REQ-`, `DMP-`, `MKT-`, `F-`, `PWS-`, `PWR-`, `T` or `CF-` spaces. They are **research identifiers**, not decisions or requirements.
**Canonical B-08 path:** the outline and the Stage 2 register still name `14_diplomacy.md`, but `14_` is now occupied by the Prompt 07C companion ([`14_market_workflows_and_acceptance.md`](../14_market_workflows_and_acceptance.md)). Under the repository's serial-prefix rule ([outline §1](../02_master_game_design_bible_outline.md)), **Prompt 08B must claim the next free prefix**; this report recommends `15_diplomacy.md` and says so in §17.4. It does **not** create that file.

---

## 1. Purpose, scope and exclusions

### 1.1 Purpose

Prompt 08A establishes a reliable, evidence-based foundation for designing Nation Supremacy's Diplomacy system. It:

1. inventories what the project already has and what it still owes on diplomacy;
2. traces every applicable approved requirement, decision and contract from Stage 2 Prompts 01–07C;
3. researches comparable diplomacy systems with traceable sources and records the limits of that evidence;
4. identifies patterns, trade-offs and design questions without finalising the design;
5. examines **UD-033** using its exact registered wording;
6. documents the boundary with **Prompt 09's Alliance System** without designing it;
7. protects the completed Prompt 07A–07C market work and Global Trade's approved-but-gated status;
8. hands a structured, honest baseline to **Prompt 08B**, and a narrower interface handoff to **Prompt 09**.

### 1.2 In scope

- Comparative research on diplomacy in persistent multiplayer nation/strategy games.
- Evidence classification, source registration and limitation recording.
- Requirements and decision traceability for diplomacy.
- Cross-system integration with Prompts 01–07C.
- UD-033 analysis and its actual status.
- Diplomacy–Alliance interface questions and ownership.
- Risk, abuse and evidence-gap analysis.
- Candidate recommendations, explicitly unapproved.
- Documentation and continuity updates required by the 08A brief.

### 1.3 Out of scope — not done, not authorised

- **No diplomacy rule is approved.** No relationship catalogue, treaty type, duration, cooldown, penalty, sanction, embargo, reputation formula, permission or acceptance rule is fixed here.
- **No implementation.** No game code, schema, migration, API, UI, scheduler, service, deployment or environment change was made. No runtime, load, security or integration test was run, because there is nothing to run.
- **No Prompt 08B or 08C work.** No B-08 rulebook, formula register, workflow catalogue or acceptance matrix was written.
- **No Prompt 09 work.** No alliance constitution, leadership model, ranks, internal permissions, membership lifecycle, shared-resource rule, voting mechanism or alliance operations workflow was designed. The alliance material below is **interface research only**.
- **No market change.** D-122, DD-136 and REQ-513 are unchanged; B-07, its formula register and the 07C companion are unchanged; G-1, G-2, G-3, G-5 and G-6 remain **NOT MET** and G-4 remains **PARTIAL**.
- **No approved decision was reopened.** No earlier `D-`, `DD-`, `UD-`, `REQ-` or stage report was rewritten to fit this research.

### 1.4 What this document is not

It is **not** the finished diplomacy design and must not be cited as one. Where it recommends an option, the recommendation is a **candidate** for 08B. Where it reports another game's rule, that rule is **comparator evidence**, not a Nation Supremacy rule. Where it records a project rule, it cites the authoritative file and identifier.

---

## 2. Project-document inventory and current Diplomacy baseline

### 2.1 Method

The inventory was built by reading the continuity set and the registered Stage 2 deliverables, then following every diplomacy reference found in them. Paths were verified on disk; no path was assumed from a prompt summary. A document that does not exist, or that exists under a different name, is recorded as such.

### 2.2 Continuity and register documents

The inventory records each file **as inspected at the start of 08A**, before this pass's own updates. Where a row says "Prompt 08 next", that was the position on entry; §19.3 lists the changes 08A then made, and the current position is "08A complete, 08B next".

| Path | Role | Status as inspected at the start of 08A (2026-10-29) | Relevance to Diplomacy |
|---|---|---|---|
| [`docs/ROADMAP.md`](../../ROADMAP.md) | Official stage roadmap (D-012) | Stage 2 **IN PROGRESS**; Prompts 01–07 complete; Prompt 08 next | Names Prompt 08 as diplomacy and Prompt 09 as alliances |
| [`docs/PROJECT_PROGRESS.md`](../../PROJECT_PROGRESS.md) | Stage tracker and authoritative status block | 07C complete; Prompt 08 next | Records the pre-08A state and the market status that must be preserved |
| [`docs/DECISIONS.md`](../../DECISIONS.md) | Project decision log | D-001…D-122; D-122 approves Global Trade scope | Source of every binding position cited below |
| [`docs/AI_CONTEXT.md`](../../AI_CONTEXT.md) | Master context and fixed constraints | 07C complete; Prompt 08 next | Constraints: mapless world, 2-hour turns, one account, free-first, architecture |
| [`docs/AI_HANDOFF.md`](../../AI_HANDOFF.md) | Cross-AI handoff | 07C complete; Prompt 08 next | Carries the next-action statement 08A must update |
| [`docs/AUTONOMOUS_DECISION_POLICY.md`](../../AUTONOMOUS_DECISION_POLICY.md) | Decision authority (D-014) | Confirmed policy | Explains why 08A makes no approvals and why UD-033 is not an owner question |
| [`docs/stage-2/00_stage_2_handoff.md`](../00_stage_2_handoff.md) | Stage 2 working package | Revised for 07C; Prompt 08 next | Boundaries, deliverables, out-of-scope list |
| [`docs/stage-2/01_stage_2_prompt_roadmap.md`](../01_stage_2_prompt_roadmap.md) | The **only** Stage 2 prompt register | Prompt 08 pending; 09–15 pending | Authoritative Prompt 08 and Prompt 09 scope |
| [`docs/stage-2/02_master_game_design_bible_outline.md`](../02_master_game_design_bible_outline.md) | Bible outline and authority map | B-08 and B-09 **Planned**; `14_diplomacy.md` and `15_alliances.md` named | The canonical B-08/B-09 slots; the `14_` collision is recorded in §1 and §17.4 |
| [`docs/stage-2/03_requirements_traceability.md`](../03_requirements_traceability.md) | Requirement register REQ-001…REQ-513 | **19 Approved / 487 Provisional / 5 Open / 2 Deferred**; REQ-012 is the diplomacy row | REQ-012, REQ-013, REQ-014 and the cross-system rows bind 08B |
| [`docs/stage-2/04_approved_and_provisional_decisions.md`](../04_approved_and_provisional_decisions.md) | D/DD register for design use | D-001…D-122; DD-001…DD-136 | DD-031, DD-048, DD-052, DD-078, DD-136 bear on diplomacy |
| [`docs/stage-2/05_unresolved_design_decisions.md`](../05_unresolved_design_decisions.md) | UD register UD-001…UD-038 | 22 Resolved / 8 Deferred / 8 Open | **UD-013** and **UD-033** are the diplomacy-owned rows |
| [`docs/stage-2/06_stage_2_progress_log.md`](../06_stage_2_progress_log.md) | Progress log and validation record | §23 is the 07C checkpoint | The 08A entry is appended as §24 after this report is written |

### 2.3 Stage 2 deliverables inspected

| Prompt | Deliverable(s) | Status | Diplomacy-relevant content |
|---|---|---|---|
| 01 | [`02` outline](../02_master_game_design_bible_outline.md), [`03` requirements](../03_requirements_traceability.md), [`04` design decisions](../04_approved_and_provisional_decisions.md), [`05` unresolved](../05_unresolved_design_decisions.md) | Complete | B-08 purpose/content/validation; REQ-012/013/014; UD-013/UD-033 |
| 02 | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](../07_core_gameplay_loop_symbolic_world_and_turn_system.md) **B-02** | Draft (v1.5) | TR-019 relationship families; TR-020/D-030 pending-act visibility; TR-021 visibility classes; TR-022 k = 5; P0–P7; class Q/S; reservation; failure codes; TR-096 Prompt 08 inheritance |
| 03 | [`09_account_onboarding_nation_creation_and_progression.md`](../09_account_onboarding_nation_creation_and_progression.md) **B-03** | Draft | §5.5 pair matrix (treaty block); §9.6 RRL-019 diplomacy cleanup; RRL-021 reroll blocks; §18 CON-001 diplomacy row; §19.2 REQ-012 partial coverage; §21.3 UD-033 |
| 04 | [`10_economy_resources_treasury_and_finances.md`](../10_economy_resources_treasury_and_finances.md) **B-04** + [register](../10_economic_formula_and_balance_register.md) | Draft (v1.3) | **ECN-212** authorises Prompt 08 aid, reparations, embargoes and sanctions as transfers with matched ledger events; ECN-087 aid route; ECN-092 one currency; D-060 contract |
| 05 | [`11_cities_infrastructure_production_and_research.md`](../11_cities_infrastructure_production_and_research.md) **B-05** + [register](../11_city_infrastructure_production_and_research_formula_register.md) | Draft (v1.5) | **URB-155** sanctions may freeze construction/research, never delete or create negative balance; aid never moves capacity, DC, housing or RP |
| 06A | [`12_population_and_domestic_politics.md`](../12_population_and_domestic_politics.md) Part I + [register](../12_population_and_domestic_politics_formula_register.md) | Draft (v2.5) | **DMP-138** sanctions may freeze a policy change but not change government/delete policy; aid moves crowns/resources, not approval/population; no diplomatic modifier without a named 08 term |
| 06B | Same B-06 document, Part II | Draft (v2.5) | **DMP-263** treaties persist through `TRANSITION`/`CRISIS`; diplomacy is read-only while authority is suspended; a leadership change does not void a treaty; REQ-360/361; REQ-307 contracts |
| 07A | [`research/07A_politics_and_war_market_research.md`](07A_politics_and_war_market_research.md) | Complete (v1.0) | 22 sources `PWS-001…PWS-022`; 30 findings `PWR-001…PWR-030`; P&W trade surfaces, restrictions, public history, abuse evidence; **approves no rule** |
| 07B | [`13_trade_and_markets.md`](../13_trade_and_markets.md) **B-07** + [register](../13_trade_and_markets_formula_register.md) | Draft (v1.1) | **MKT-185** diplomacy restriction is separate and may not be a market fee; **MKT-217/218/220** one rule, one owner; the market reads a B-08 embargo and never defines one; no silent value movement |
| 07C | [`14_market_workflows_and_acceptance.md`](../14_market_workflows_and_acceptance.md) | Complete and accepted (v1.0) | §6 Diplomacy row: "nothing at launch; no treaty, sanction or embargo rule exists"; §15.3 and §15.5: 08 inherits the market, may not add a trade tax/tariff/embargo without a new decision, and must add any restriction to B-08 and record the interface; 237/237 acceptance; gates unchanged |

### 2.4 Existing Diplomacy baseline — what the project actually has

There is **no B-08 rulebook**. The baseline consists of framework rules, contracts and one open question. The substantive positions are:

| Baseline item | Source | Status | What it actually says |
|---|---|---|---|
| Bilateral relationships are typed, event-sourced and visibility-scoped | REQ-012 ([`03`](../03_requirements_traceability.md)) | **Provisional** | The requirement exists; the state catalogue, transitions and effects do not |
| Relationship families | B-02 **TR-019** | **Provisional** | Posture is **directional** (friendly/neutral/tense/hostile); **Agreement** (treaty, pact, trade term) is mutual and owned by Prompt 08; alliance membership is Prompt 09; conflict is Prompt 10 |
| Relations transparent, intent opaque | B-02 **TR-020**; **D-030**; **DD-048** | **D-030 Confirmed**; TR-020 Provisional | A pending proposal is visible to its named counterparty while open; third parties see nothing until declaration, effect at a boundary, or publication; rejection/withdrawal is private unless published |
| Visibility classes and aggregation | B-02 **TR-021/TR-022**; **D-027** | **Provisional/Confirmed** | One class per field (public/alliance/private/restricted); k = 5 and complementary suppression for aggregates |
| Pending-act visibility | **D-030** | **Confirmed** | As above; Prompt 08 implements it rather than re-deciding it |
| Treaty effects are open | **UD-013** | **Deferred to Prompt 08** | "What does a treaty *do* beyond a non-aggression analogue?" Options: (a) NAP + two promises, (b) full treaty types |
| Reputation scope is open | **UD-033** | **Deferred to Prompt 08** | Account-scoped or nation-scoped after a reroll; see §11 |
| Restricted pair cannot conclude a treaty | B-03 §5.5 row 15, §18 CON-001 | **Provisional** | A shared-network restricted pair cannot sign a treaty with each other |
| Reroll terminates treaties | B-03 **RRL-019** | **Provisional** | Termination is a class-P event attributed to the old nation; the replacement starts neutral with no treaties; breach-reputation scope is Prompt 08's |
| Aid, reparations, embargoes, sanctions are permitted | B-04 **ECN-212** | **Provisional** | Any crown/resource movement is a transfer with matched ledger events; an embargo blocks a transfer but destroys nothing; a sanction may freeze an action but may not create a negative balance; diplomatic trade effects apply at P4; D-030 applies |
| Sanctions may freeze construction/research | B-05 **URB-155** | **Provisional** | A sanction may fail an action by reference to the sanction; it may not delete owned assets or create a negative balance; aid never moves capacity, DC, housing or RP |
| Sanctions may freeze policy | B-06 **DMP-138** | **Provisional** | A sanction may freeze a policy change but may not change a government, delete a policy or create a negative balance; no "prestige" input and no diplomatic approval modifier without a named 08 term |
| Treaties survive transition/crisis | B-06 **DMP-263** | **Provisional** | Treaties persist; the player may read them but may not sign, ratify, denounce or renegotiate while authority is suspended; a leadership change does not void a treaty |
| The market reads a diplomacy restriction | B-07 **MKT-185/217/218/220** | **MKT-185 approved constraint** (DMP-262); the rest Provisional | A diplomacy restriction is a separate rule; it may not be implemented as a market fee, a tariff or a silent value movement; B-08 owns an embargo rule if one exists |
| Diplomacy is not a general action currency | **D-024** | **Confirmed** | Every non-military action must declare a visible limit in the B-02 §24 contract; no general per-turn click budget |
| Operations Points are military-only | **D-015** | **Confirmed** (model) | OP must not leak into diplomacy; no diplomatic cost may be denominated in OP |
| One currency | **D-049/DD-067** | **Confirmed** (design) | Crowns only; no prestige currency, no second diplomatic currency |
| No map | **REQ-041/DD-013** | **Approved** | Diplomacy must produce no geographic borders, fronts or distance effects |
| Two-hour boundaries | **REQ-015** | **Approved** | Any diplomatic effect with a cost/duration resolves at a boundary under B-02 |
| One account, one active nation | **D-032/REQ-061** | **Confirmed/Provisional** | Diplomatic authority resolves from the account's active nation |
| Shared-network pair restrictions | **D-031/D-034/D-035**; B-03 §5.5 | **Confirmed/Provisional** | A restricted pair is blocked from treaties; indirect routes through alliances, third nations or markets are covered |
| Reroll blocks | **D-039/RRL-021** | **Confirmed** (design) | A reroll is blocked by an active campaign, unsettled settlement, preservation hold or disqualifying account state |

### 2.5 What is missing, contradictory or unverified at the start of 08A

| Gap | Evidence | Consequence for 08B |
|---|---|---|
| **No relationship catalogue** | REQ-012 names "typed" relationships; TR-019 names only four families and one directional posture | 08B must decide the actual statuses, transitions and symmetry |
| **No treaty type list or effects** | UD-013 explicitly defers the question | 08B must decide which treaties exist and what each does |
| **No breach, penalty or enforcement rule** | No project document defines breach; only B-03's reroll termination exists | 08B/08C must define breach consequences or explicitly decide that none are enforced |
| **No reputation register** | UD-033 defers scope; B-02/06 forbid an unnamed modifier | 08B must decide whether a register exists at all; see §11 |
| **No sanction or embargo mechanics** | B-04/B-05/B-06 only bound what a sanction may **not** do | 08B must define eligibility, scope, duration, activation, effects and visibility, or record that sanctions are out of scope |
| **No proposal/acceptance lifecycle** | D-030 fixes pending visibility; B-02 fixes reservation and class Q/S timing | 08B/08C must define the full lifecycle, expiry, withdrawal, amendment and stale authorization |
| **No diplomacy action limits** | D-024 requires a visible limit for every non-military action | 08B must declare treaty slots, proposal caps, cooldowns or another limit |
| **No diplomacy formula register** | 08B/14 own formulas | 08A records possible formula needs but invents no value |
| **No B-08 canonical file** | Outline names `14_diplomacy.md`; `14_` is taken by 07C | 08B must confirm `15_diplomacy.md` and update the outline and register together |
| **No alliance interface contract** | Roadmap B-08 says "treaties"; B-09 says "alliance diplomacy" | Ownership is ambiguous for alliance-level treaties; see §13 |
| **`DPX-01` public timing ambiguity** | D-030/TR-020 vs TR-021's "treaty texts once signed" public | 08B must state the exact moment a treaty becomes public |
| **No player research** | No survey, playtest or interview exists | Every experience claim below is analysis, not user evidence |

None of these gaps is filled with an invented rule in this report.

---

## 3. Research methodology

### 3.1 Questions

The research followed the eight topics in the 08A brief: relationship models; treaty/agreement lifecycle; negotiation and authorization; reputation and consequences; sanctions and diplomatic actions; player experience and communication; integrity/fairness/abuse; and cross-system interactions. Each topic was translated into specific questions before searching (for example, "does the game expose a relationship status that is separate from an agreement, and is it symmetric?").

### 3.2 Selection rule for evidence

Preference order:

1. **Official game rules, official support pages and official game pages** — strongest for factual claims about mechanics.
2. **Official wikis maintained by the game's publisher** — strong for mechanics, but community-editable; labelled as such.
3. **Community wikis and reference sites** — used only where official documentation is silent; labelled and limited.
4. **Player forum/community posts** — used only for player-experience or abuse reports, never as proof of an official rule.
5. **Project documents** — used for Nation Supremacy's own approved constraints, never as evidence about another game.

No source was treated as authoritative for a claim it does not actually state. Where the only evidence is an absence (for example, no documented reputation metric), that is recorded as an **absence finding**, not as proof that the feature does not exist.

### 3.3 Method actually followed

1. Read the project continuity set and the Stage 2 deliverables in §2 before selecting comparators.
2. Selected comparators for a specific design contrast, not for genre popularity (§4).
3. Searched for each game's official rules/support/wiki pages, then fetched the pages directly.
4. Where a page body was blocked by a client challenge, either used the same wiki's `?action=raw` content endpoint (a public content endpoint, not a cache) or recorded the limitation. The EU4 wiki could not be read this way and was therefore **not used** (§4.3).
5. Read the specific sections that answer the question; did not rely on search snippets for a finding unless the snippet was the only accessible content, and then labelled it.
6. Recorded each source with URL, access date, publisher, type, the exact claim it supports and its limitations (§5).
7. Separated source-reported mechanics from comparative findings, design implications and recommendations (§6–§10).
8. Cross-checked the project's own rules against the evidence, and recorded conflicts rather than resolving them by assertion (§14).

### 3.4 Evidence labels used in this report

| Label | Meaning |
|---|---|
| **Verified official rule** | Stated by the game's own rulebook, official support page or official game page, read on the access date |
| **Verified interface observation** | Directly observed on a public page, logged out, on the access date |
| **Official-wiki mechanic** | Stated by a wiki hosted by the publisher but community-editable; strong but not a rulebook |
| **Community-reported mechanic** | Stated by a community wiki or reference site; used only where official documentation is silent |
| **Player-reported experience** | A player's account of play; used for experience/abuse analysis only |
| **Comparative finding** | A pattern supported by at least two of the comparators |
| **Design implication** | An inference about what the evidence may mean for Nation Supremacy; not a rule |
| **Candidate recommendation** | An option for 08B; explicitly unapproved |
| **Approved requirement or decision** | An existing Nation Supremacy position, cited to its authoritative file and ID |
| **Open question** | Requires 08B/08C/09 or another owner; recorded with an ID |

A sentence carries one label. A paragraph that moves from evidence to implication says so.

### 3.5 Limitations that apply to the whole report

1. **No authenticated play.** No game account was used, no in-game action was taken and no live match was observed. Everything about another game is documentation or public-interface evidence, not first-hand play.
2. **Wiki drift.** Community wikis may lag the live game; official wikis may be edited by volunteers. Version/date is recorded where the page states it.
3. **Publisher-hosted ≠ official rule.** eRepublik's and Call of War's wikis are publisher-hosted but community-edited. They are labelled *official-wiki mechanic*, not *verified official rule*.
4. **Absence is not proof.** "No documented reputation register" means the sources reached did not document one; it does not prove none exists.
5. **No frequency data.** No survey, telemetry or player count was found or is claimed. One forum post is one post.
6. **Different scales and genres.** Stellaris is a single-player grand strategy game; EVE is a sandbox MMO; eRepublik and P&W are persistent browser games; Call of War is a session-based strategy game. Their mechanics are not automatically suitable for a 2-hour-turn, mapless, free-first browser game.
7. **No user research for Nation Supremacy.** All usability statements are design analysis, not verified player findings.
8. **One wiki could not be read.** The Europa Universalis IV wiki returned a client challenge on every endpoint attempted; EU4 was therefore excluded rather than cited from snippets (§4.3).

---

## 4. Comparator selection and justification

### 4.1 Required comparator — Politics & War

Politics & War (P&W) is mandatory because the project already uses it as its primary genre reference and because Prompt 07A researched its market. It is the closest structural analogue: a persistent browser game with nations, alliances, a 2-hour tick, a global market, war and player-run diplomacy. Its diplomacy is unusually revealing for Nation Supremacy because the game **records formal treaty types but enforces only non-aggression** (`DPS-001`). That single fact separates three things Nation Supremacy must keep distinct: a relationship record, an agreement, and an enforceable obligation.

P&W is **not** a model to copy. Its diplomacy is largely played on forums and Discord (`DPS-004`, `DPS-005`); it has no in-game proposal/accept flow; its reputation is social, not a game register; and its enforcement is moderator action against abuse, not a treaty engine.

### 4.2 Additional comparators and why each was selected

| Comparator | Why selected | What it can evidence | What it cannot evidence |
|---|---|---|---|
| **eRepublik** | A persistent browser game with formal, state-authored treaties (MPP, peace, embargo) that require **two legislatures** and have fixed durations and costs | Proposal → approval → activation → expiry → renewal; permission split between executive and legislature; automatic conflict resolution; sanctions as time-boxed law | Modern player expectations; a mapless world; a 2-hour turn; any nation-level reputation register (none documented) |
| **Call of War** (Bytro) | A session-based strategy game whose diplomacy screen exposes **directional** relations and market effects | Asymmetric relationship states; unilateral granting; relation-to-market coupling; stale display risk; "relations can be bought" | Persistent multi-month worlds; legislature/authorization depth; a reputation formula |
| **Stellaris** (Paradox) | A grand-strategy game with the richest documented treaty catalogue, acceptance factors, trust and opinion | Bilateral offer/accept; treaty-end penalties; truces; cooldowns; trust as an accumulated value; opinion as a derived value; action gating by relation level | Persistent multiplayer politics; player-to-player negotiation; free-to-play constraints |
| **EVE Online** | A persistent multiplayer sandbox with formal wars, corporate/alliance authority and player-set standings | War lifecycle, warm-up, cost, surrender, membership transitions, eligibility; one-way private standings; public war reports; anti-spam pricing | A nation economy; a 2-hour turn; any global diplomatic reputation |
| **Europa Universalis IV** | Considered for truce-breaking, aggressive expansion and trust | — | **Excluded:** every wiki endpoint returned a client challenge; no accessible primary text was read, so no EU4 claim is made |

### 4.3 Why EU4, CK3 and Victoria 3 were not used

They were the obvious candidates for truce-breaking and reputation penalties. The Paradox wikis blocked automated reads with a JavaScript client challenge, and no accessible primary page was found. Citing a search snippet would have violated the brief's source standard, so they were dropped. Stellaris covers treaty-end penalties, truces, trust and opinion with an accessible text, and EVE covers war termination and anti-abuse. The loss is a narrower view of "aggressive expansion"-style reputation; §15 records that gap.

### 4.4 What the set does and does not cover

**Covered well:** relationship catalogues; symmetry/asymmetry; proposal and approval; durations and renewal; activation delays; treaty-end penalties; war termination; sanctions/embargoes; visibility; role-based authority; anti-spam costs; membership-transition edge cases.

**Covered weakly or not at all:** formal counterproposals; proposal expiry deadlines; reputation that follows an **account** across nation rerolls (no comparator has Nation Supremacy's exact reroll model); alliance-constitution design (deliberately out of scope; see §13); player-experience research with sample sizes.

---

## 5. Source register

All URLs were read on **2026-10-29**. "Official" means published by the game's operator; "official wiki" means a wiki hosted by the operator but community-editable; "community" means an independent wiki or reference site.

| ID | Title | Publisher / author | Type | URL | Date | Supports | Reliability / limitation |
|---|---|---|---|---|---|---|---|
| **DPS-001** | Alliance Treaty Web | Politics & War (Yellowstone Digital Media) | Official game page | https://politicsandwar.com/alliances/treatyweb/ | Accessed 2026-10-29 | The ten in-game treaty types; the statement that treaties are **not enforced by the game except non-aggression**; NAP blocks war declarations between treated alliances | **Strong.** Live page, logged out. It lists types and enforcement, not proposal/acceptance, duration or breach procedure |
| **DPS-002** | Game Rules | Politics & War | Official rules | https://politicsandwar.com/rules/ | Accessed 2026-10-29 | One nation per person; same-network restrictions; alliance-bank evasion is bannable; same-network nations may share an alliance but not declare on the same targets; war-slot filling; automated play; moderation points | **Strong.** Current rules page. It states prohibitions, not treaty mechanics |
| **DPS-003** | World Trade Embargoes | Politics & War | Official game page | https://politicsandwar.com/world/embargoes/ | Accessed 2026-10-29 | A public, dated embargo list with embargoer, embargoed and a free-text reason; 7,300 rows; reciprocal pairs appear as two records | **Strong** for the interface. It does not state duration, eligibility or the full effect |
| **DPS-004** | Terminology and Glossary (P&Wpedia) | Politics & War | Official reference | https://politicsandwar.com/pwpedia/article/Terminology-Glossary | Accessed 2026-10-29 | "Embassy" = a place where alliances converse, "typically via a discord channel"; "Paperless" = no in-game treaties; a 2-month NAP is a player practice; "wardodger"; "beige"; "blockade" | **Strong** for vocabulary. It describes player practice, not a rule |
| **DPS-005** | Alliance Treaty (wiki) | Politics & War Wiki (Fandom) | Community wiki | https://politicsandwar.fandom.com/wiki/Alliance_Treaty?action=raw | Accessed 2026-10-29 | Treaty statuses (Active, Upgraded/Downgraded, Cancelled, Defunct, Dissolved, Expired, Inactive); treaty and declaration types; open treaties; blocs; the claim that treaties are forum-published and have no fixed convention | **Moderate.** Community-maintained and partly historical; it conflicts with `DPS-001` on whether treaties are in-game, which is recorded as a source conflict |
| **DPS-006** | Alliance (wiki) | Politics & War Wiki (Fandom) | Community wiki | https://politicsandwar.fandom.com/wiki/Alliance?action=raw | Accessed 2026-10-29 | Alliances sign treaties and form blocs; market-sharing circles; bank deposit/withdraw roles; "at least a government member" can declare war; disbanding and a 5-day recreate wait | **Moderate.** Community wiki; role detail is illustrative, not an official permission matrix |
| **DPS-007** | Embargoes (wiki) | Politics & War Wiki (Fandom) | Community wiki | https://politicsandwar.fandom.com/wiki/Embargoes?action=raw | Accessed 2026-10-29 | Embargo is placed by an individual player, cannot be forced by an alliance government, blocks both sides from accepting each other's offers, slightly affects approval, and accepts any reason | **Moderate.** Consistent with `DPS-003`; the approval effect is not shown on the official page |
| **DPS-008** | Mutual protection pact | eRepublik Official Wiki | Official wiki (community-edited) | https://wiki.erepublik.com/index.php/Mutual_protection_pact | Accessed 2026-10-29 | President proposes; both congresses vote; 10,000 local currency from each treasury; active on acceptance for 30 days; renewal extends; failed proposal refunds; automatic "friend of a friend" cancellation; deployment roles | **Strong** for the described mechanics. Publisher-hosted but community-edited; the 30-day value may change |
| **DPS-009** | Trade embargo | eRepublik Official Wiki | Official wiki (community-edited) | https://wiki.erepublik.com/index.php/Trade_embargo | Accessed 2026-10-29 | President/dictator proposes; congress approves; 30 days; renewal extends; based on citizenship; existing offers remain but cannot be updated or added to; wars act like embargoes | **Strong** for the described mechanics; same caveat |
| **DPS-010** | Peace treaty | eRepublik Official Wiki | Official wiki (community-edited) | https://wiki.erepublik.com/index.php/Peace_treaty | Accessed 2026-10-29 | President/dictator proposes; both congresses; the counterparty's proposal appears 24 hours later; gold can be demanded; war ends on passage; natural-enemy status must be unset and is locked for 7 days | **Strong** for the described mechanics; same caveat |
| **DPS-011** | Diplomatic relations | Call of War Wiki | Official wiki | https://wiki.callofwar.com/wiki/DIPLOMATIC_RELATIONS | Last edited 2021-12-22; accessed 2026-10-29 | Seven relations: War, Cease fire, Trade embargo, Peace, Right of Way, Shared Map, Shared Intelligence; separate "your relation" and "their relation" columns; market effects of war/embargo | **Strong** for the relation catalogue. It does not document acceptance, duration or expiry |
| **DPS-012** | What do the Diplomatic Relations mean? | Bytro Help Center | Official support | https://bytro.helpshift.com/hc/en/4-call-of-war/faq/135-what-do-the-diplomatic-relations-mean/?p=web | Last updated 1386 days before access (2026-10-29) | Relation effects in plain language; ceasefire/trade embargo share a slot depending on war state; war/embargo block market trade | **Strong** but dated; it describes effects, not the permission model |
| **DPS-013** | Relations (wiki) | Call of War Wiki (Fandom) | Community wiki | https://call-of-war-by-bytro.fandom.com/wiki/Relations?action=raw | Accessed 2026-10-29 | Relations need not be equal on both sides; relations can be exchanged or "bought" through trade; declaring war lowers popularity with every country; AI embargoes/declares on low-reputation countries; the other player may not see a change quickly | **Moderate.** Community wiki; the popularity claim is not corroborated by an official page |
| **DPS-014** | Diplomacy (wiki, v3.10) | Stellaris Wiki (Fandom mirror) | Community wiki mirroring the official wiki | https://stellaris.fandom.com/wiki/Diplomacy?action=raw | Version 3.10; accessed 2026-10-29 | Envoys locked for a year; many actions have a 10-year cooldown; unilateral vs bilateral agreements; bilateral offers require acceptance; treaty-end opinion penalties and truces; trust generated by lasting treaties, capped by the most valuable treaty, decaying without one; acceptance factors | **Strong** for the documented mechanics. Mirror of a community wiki; version 3.10, not necessarily current |
| **DPS-015** | Relations (wiki, v3.10) | Stellaris Wiki (Fandom mirror) | Community wiki mirroring the official wiki | https://stellaris.fandom.com/wiki/Relations?action=raw | Version 3.10; accessed 2026-10-29 | Each empire has a unilateral opinion; relation level is the sum of both opinions; levels gate actions; permanent and relationship modifiers; at-war and treaty modifiers | **Strong** for the documented model; same version caveat |
| **DPS-016** | Wars | EVE Online Support | Official support | https://support.eveonline.com/hc/en-us/articles/115004152745-Wars | Updated 2026-10-21; accessed 2026-10-29 | War declaration and 24-hour warm-up; weekly 500M ISK bill; ends on non-payment, accepted surrender, loss of eligibility or HQ loss; 24-hour cooldown; surrender blocks re-declaration for 14 days; corp/alliance join/leave war transitions; defender ally offers, 4-hour entry | **Strong.** Current official support. It documents the mechanics, not every edge case |
| **DPS-017** | War Eligibility | EVE Online Support | Official support | https://support.eveonline.com/hc/en-us/articles/360001975920-War-Eligibility | Accessed 2026-10-29 | Eligibility requires a structure; losing the last structure ends the war 24 hours later; mutual wars survive eligibility loss | **Strong.** Current official support |
| **DPS-018** | Corporation diplomacy | EVE University Wiki | Community wiki | https://wiki.eveuniversity.org/Corporation_diplomacy | Revised 2026-09-23; accessed 2026-10-29 | Standings can be personal/corporate/alliance, are **one-way only**, are invisible to the other side unless reciprocated, accept a free-text label, and can control structure behaviour; war roles; ally offers; public war report; 500M ISK/week (raised from 100M in 2026-09-22) | **Moderate–strong.** Detailed and current, but an independent university wiki, not the operator |
| **DPS-019** | Standings | EVE Online Support | Official support | https://support.eveonline.com/hc/en-us/articles/203217152-Standings | Accessed 2026-10-29 | NPC standings use diminishing-returns formulas and derived faction standings; player entities can set standings directly through contact lists; player standings can control customs tax and tower fire | **Strong** for the NPC formula and the existence of player standings. It does not define a diplomatic reputation |

**Source count:** 19 (`DPS-001`…`DPS-019`). **Publisher-official:** 8 (`DPS-001`…`DPS-004`, `DPS-012`, `DPS-016`, `DPS-017`, `DPS-019`). **Publisher-hosted but community-edited:** 4 (`DPS-008`…`DPS-011`). **Community:** 7 (`DPS-005`…`DPS-007`, `DPS-013`…`DPS-015`, `DPS-018`).

**Source conflicts recorded, not smoothed over:**

1. **P&W treaty records: in-game or forum?** `DPS-001` says the treaty web is "now operated automatically through in-game mechanics". `DPS-005` says treaties are published on the Alliance Affairs forum and have "no convention". Both can be true — the record is in-game, the negotiation and text are on the forum — but no accessible source states the creation flow. **Unresolved; not used as evidence for a creation workflow.**
2. **P&W embargo effect.** `DPS-003` shows the list and reason; `DPS-007` claims a slight approval effect. The official page does not show that effect. **Treated as community-reported, not official.**
3. **Call of War popularity.** `DPS-013` says declaring war lowers popularity with every country and AI reacts to low reputation; `DPS-011`/`DPS-012` do not document a popularity formula. **Treated as community-reported and weak.**
4. **EVE war cost.** `DPS-016` states 500M ISK/week; `DPS-018` states it was raised from 100M on 2026-09-22. **Compatible; the official page is current and wins.**

---

## 6. Evidence-backed findings by research topic

Each finding states its label, its sources and what the source actually establishes. A finding is not a Nation Supremacy rule.

### 6.1 Diplomatic relationships

**DPR-001 — P&W records formal treaty types but enforces only non-aggression.** *Verified official rule* (`DPS-001`). The official treaty web lists MDP, MDoAP, ODP, ODoAP, Protectorate, NAP, PIAT, NPT, Extension and Offshore, and states: "Treaties are not enforced by the game, except non-aggression. Nations in treatied alliances will not be able to declare wars on each other." The same page describes the web as "a visualization of alliances and their in-game formal obligations to each other". This is the clearest evidence that a game can have a **typed obligation register** whose entries mostly do not create a mechanical effect.

**DPR-002 — P&W's treaty parties are alliances, not nations.** *Verified interface observation* (`DPS-001`, `DPS-004`, `DPS-006`). The treaty web is an alliance-level graph; the glossary defines a treaty as an "in game political tie between 2 alliances"; the alliance page says most alliances sign treaties and form blocs of three or more signatories. Nation-to-nation treaties are not part of the documented model. **Design implication:** a nation-level treaty system cannot copy P&W's party model; it would be a different object.

**DPR-003 — P&W's treaty status vocabulary is richer than its enforcement.** *Community-reported mechanic* (`DPS-005`). The community wiki lists Active, Upgraded, Downgraded, Cancelled, Defunct, Dissolved, Expired and Inactive, and says a Cancelled treaty "is still in effect for other remaining parties". It also says there is "no convention" establishing treaty standards. **Limitation:** this is a community description of player practice, not an official state machine. It is useful as a **vocabulary warning**: a single "active/inactive" flag cannot represent upgrade, partial cancellation, party dissolution or expiry.

**DPR-004 — eRepublik's MPP is a symmetric, time-boxed, automatically triggering treaty.** *Official-wiki mechanic* (`DPS-008`). A mutual protection pact is proposed by a president, must pass **both** congresses, costs 10,000 local currency from **each** treasury, is valid from acceptance for **30 days**, can be renewed for another 30, and triggers automatically when either party attacks or is attacked by a non-pact country. If either congress rejects it, both treasuries are refunded. A pact is automatically cancelled if a party attacks a country that shares a common pact ("friend of a friend"). The pact does not require a later acceptance of a call to arms.

**DPR-005 — eRepublik distinguishes signature, activation and trigger.** *Official-wiki mechanic* (`DPS-008`). The pact is "valid starting the day it was marked as accepted"; it protects only wars declared after activation in the beta description; its **trigger** is a later attack. Signature, validity and the moment an obligation fires are three different events. **Design implication:** a treaty's "active" state is not the same as its obligation being invoked.

**DPR-006 — Call of War exposes directional relations, not a single mutual status.** *Official-wiki mechanic* (`DPS-011`) and *community-reported mechanic* (`DPS-013`). The diplomacy screen lists "your diplomatic relation towards each nation ... as well as their diplomatic relation towards you". The community wiki states explicitly: "Relations doesn't need to be equal for both sides. You can get Right of Way through a country or see another's map without sharing your map or granting Right of Way." The relation set is War, Cease fire, Trade embargo, Peace, Right of Way, Shared Map and Shared Intelligence.

**DPR-007 — Call of War's relations are changed unilaterally.** *Official-wiki mechanic* (`DPS-011`) and *community-reported mechanic* (`DPS-013`). The official page describes changing a relation in the diplomacy menu; no acceptance step is documented for Right of Way, Shared Map or Shared Intelligence. The community wiki says the other player "may not see the change quickly and won't usually change relations with you unless already agreed". **Limitation:** the absence of a documented acceptance step is not proof that none exists; it is a documentation gap.

**DPR-008 — Stellaris separates unilateral opinion from the bilateral relation level.** *Community-reported mechanic mirroring the official wiki* (`DPS-015`). "The relation level between two empires is based on the sum of their unilateral opinions of each other." Each opinion ranges from −1,500 to +1,500 and is influenced by permanent, relationship, policy and ethics modifiers. The relation level (Terrible / Tense / Neutral / Positive / Excellent) determines which diplomatic actions are available without an envoy.

**DPR-009 — Stellaris treats a relationship status, a treaty and an obligation as different layers.** *Community-reported mechanic* (`DPS-014`, `DPS-015`). The relation level gates what can be offered; a bilateral agreement requires acceptance; the agreement then creates effects (for example, a Non-Aggression Pact prevents war) and contributes to Trust. Ending it has a type-specific Opinion penalty and sometimes a Truce. The status alone does not create the obligation.

**DPR-010 — EVE's player "standings" are private, one-way labels, not a shared relationship state.** *Community-reported mechanic* (`DPS-018`) corroborated by *official support* (`DPS-019`). EVE University: "Standings are one-way only. The player, corporation or alliance will not see what standings you have set for them, and will not automatically set your corporation at the same standings." Standings can be personal, corporate or alliance-level, can carry a free-text label, and can control structure behaviour such as customs tax or tower fire. The official support page confirms player entities "can have standings set towards each other, which can be adjusted by the players directly".

**DPR-011 — EVE's formal war is a separate two-party object with named roles.** *Verified official rule* (`DPS-016`, `DPS-017`). A war has an attacker, a defender and (for the defender only) allies; it requires war eligibility; it is declared against a corporation or alliance; the attacker's war HQ is part of the object; the war ends on non-payment, accepted surrender, loss of eligibility or HQ destruction. War is not a "relationship status" in a list; it is an object with its own lifecycle and records.

**DPR-012 — P&W's alliance-level treaty web is the world's public relationship surface.** *Verified interface observation* (`DPS-001`). A logged-out visitor can see which alliances have which formal obligations. The page hides NAP/PIAT by default "to reduce clutter", which is itself a visibility decision: the full graph exists, but the default view suppresses the least hostile ties.

**DPR-013 — Comparative finding: symmetric status is rare; directional posture plus mutual agreements is the common structure.** *Comparative finding* (`DPS-008`, `DPS-011`, `DPS-014`, `DPS-015`, `DPS-018`). eRepublik's MPP is symmetric once ratified. Call of War is directional. Stellaris is asymmetric at the opinion layer and symmetric at the agreement layer. EVE is asymmetric and private. P&W's treaty types are mutual between alliances. **No comparator uses a single symmetric "relationship status" for everything.** This is the strongest structural finding of the research.

**DPR-014 — Comparative finding: a relationship can exist without an agreement, and an agreement without enforcement.** *Comparative finding* (`DPS-001`, `DPS-011`, `DPS-014`, `DPS-018`). P&W's MDP is a record with no game effect; its NAP is enforced. Call of War's Right of Way is a relation with an effect but no formal treaty record. Stellaris's Trust can exist from a treaty; its Opinion exists without one. EVE's standings exist without any agreement. **Design implication:** "relationship status", "agreement record" and "enforceable obligation" are three separate concepts and should not share one field.

### 6.2 Treaties, agreements and lifecycle

**DPR-015 — eRepublik's MPP lifecycle is explicit and auditable.** *Official-wiki mechanic* (`DPS-008`): proposal by the president, simultaneous votes in both congresses, active on acceptance, 30-day expiry, optional renewal before expiry, automatic disable. Failure refunds both treasuries. A pact can be proposed "at any point before they expire". This is the clearest complete lifecycle in the evidence set.

**DPR-016 — eRepublik's peace treaty inserts a deliberate 24-hour counterparty delay.** *Official-wiki mechanic* (`DPS-010`). "Law proposal in one country will trigger law proposal in the proposed country 24 hours later." A peace treaty can demand gold; it ends the war when both congresses pass it; a natural-enemy designation must be unset first and cannot be changed for 7 days. **Design implication:** a fixed delay before the counterparty can act is a fairness device, but it also creates a stale-proposal window.

**DPR-017 — eRepublik's embargo is a time-boxed law with grandfathering.** *Official-wiki mechanic* (`DPS-009`). Proposed by the president or dictator, approved by congress, valid from acceptance for 30 days, renewable. It is based on **citizenship**, not residence. Existing offers remain on the foreign market until removed or sold out, but cannot be updated and no new offers may be created. Wars act like embargoes. **Design implication:** a sanction that applies to future actions while grandfathering existing commitments avoids retroactive destruction but creates a two-speed market.

**DPR-018 — P&W's treaty expiry and cancellation are not documented as game-automatic.** *Verified official rule* (`DPS-001`) plus *community-reported mechanic* (`DPS-005`). The official page states the enforcement boundary but not expiry, renewal or cancellation mechanics. The community wiki lists Expired and Cancelled statuses while saying there is no convention. **Absence finding:** no accessible source establishes an automatic expiry or renewal for P&W treaties. The 2-month NAP in the glossary is described as a player practice (`DPS-004`), which supports the interpretation that duration is social, not enforced — but it is not proof.

**DPR-019 — Stellaris documents type-specific exit costs.** *Community-reported mechanic* (`DPS-014`). Bilateral agreements "can be ended at any time by either empire but doing so will cause a temporary Opinion penalty". The table gives different penalties by type (Embassy 0, NAP −50, Research Agreement −25, Commercial Pact −25, Migration Treaty −15, Defensive Pact −100, Federation −200) and marks whether a Truce follows (NAP, Commercial Pact, Defensive Pact, Federation: yes; Research Agreement, Migration Treaty: no). Some agreements can only be made or broken when neither empire is at war.

**DPR-020 — Stellaris uses cooldowns to stop treaty churn.** *Community-reported mechanic* (`DPS-014`). "Many diplomatic actions have a 10-year cooldown once chosen." Envoys, once assigned, cannot be reassigned for a year. Rivalries can only end 10 years after they were proposed. **Design implication:** a cooldown is a cheaper anti-spam device than a proposal cap, but it must be visible or players will read it as a bug.

**DPR-021 — EVE's war has explicit activation and termination timings.** *Verified official rule* (`DPS-016`). Declaration notifies all parties; combat becomes legal **24 hours later**; the first week's bill is paid at declaration and the second is issued immediately; the war ends on non-payment, accepted surrender, loss of eligibility or HQ destruction. After any end, hostilities may continue for **24 hours**. Surrender prevents re-declaration for **14 days**. A defender joining an alliance moves the war to alliance level; a corporation leaving an alliance has the war copied onto it for its current paid cycle.

**DPR-022 — EVE's ally entry is a separate accepted offer with its own delay.** *Verified official rule* (`DPS-016`) and *community-reported mechanic* (`DPS-018`). Only a defender can open for allies; an ally offer may include a fee; once accepted, the ally is treated as part of the defenders for **two weeks** before renewal, and hostilities can start **4 hours** after acceptance. Attackers cannot recruit allies this way; they must declare their own wars.

**DPR-023 — Comparative finding: activation delays are common; documented proposal expiry is rare.** *Comparative finding* (`DPS-008`, `DPS-010`, `DPS-016`, `DPS-018`). eRepublik's MPP is active on both approvals; its peace proposal appears 24 hours later; EVE's war has a 24-hour warm-up and its ally entry 4 hours. **No comparator documents a deadline after which an unanswered proposal automatically lapses.** P&W's offers wait indefinitely; Stellaris's offers wait for an answer. This is a genuine evidence gap, not a pattern to copy.

**DPR-024 — Comparative finding: counterproposals are not documented anywhere in the set.** *Comparative finding* (`DPS-005`, `DPS-008`, `DPS-010`, `DPS-014`, `DPS-016`, `DPS-018`). eRepublik uses a yes/no law vote; Stellaris uses an offer with an acceptance score; EVE uses surrender and ally offers; P&W negotiates on forums. None documents an in-game counterproposal object. **Design implication:** if Nation Supremacy wants formal counterproposals, it is designing beyond the evidence and must justify the added complexity. B-07's directed-trade "counteroffer creates a new revision" model (D-112) is the project's nearest precedent.

**DPR-025 — Comparative finding: treaty-end consequences are either none, an opinion penalty, a truce, or a hard lockout.** *Comparative finding* (`DPS-001`, `DPS-014`, `DPS-016`). P&W: no game consequence outside NAP. Stellaris: opinion penalty plus optional truce. EVE: 24-hour cooldown and, after surrender, a 14-day no-redeclare lockout. eRepublik: the treaty simply expires; no breach penalty is documented. **Design implication:** "breach" is not a universal mechanic; most comparators punish **exit timing**, not promise-breaking.
### 6.3 Negotiation and authorization

**DPR-026 — eRepublik splits authority between executive proposal and legislative approval.** *Official-wiki mechanic* (`DPS-008`…`DPS-010`). The president proposes MPPs, peace and embargoes; congress votes; a dictator may propose "any of the above Laws except New citizen message and President impeachment". The wiki's law list is an explicit authority matrix. This is the strongest evidence that a diplomacy permission model can be **role-and-chamber**, not a single "leader can do anything" flag.

**DPR-027 — EVE ties authority to corporate/alliance office.** *Verified official rule* (`DPS-016`) and *community-reported mechanic* (`DPS-018`). War is declared by the CEO or a director (the executor corporation's CEO/director for an alliance); surrender is offered by the CEO or a director; ally offers are made by the CEO or a director. The support page does not enumerate every role, but it consistently names these offices.

**DPR-028 — P&W documents alliance offices but not a treaty permission matrix.** *Official reference* (`DPS-004`) and *community wiki* (`DPS-006`). The glossary names leader, 2ic, high gov and low gov; the alliance page says "at least a government member" has war authority and that only certain members can withdraw from the bank. **No accessible source states who may sign, amend or cancel a treaty.** This is an evidence gap, not a finding that any member can.

**DPR-029 — P&W's diplomacy is conducted outside the game.** *Verified official reference* (`DPS-004`, `DPS-005`). The glossary defines "Embassy" as a place where alliances converse, "typically via a discord channel". The community treaty page says treaties are "published and circulated" in the Alliance Affairs forum. The official treaty web records the resulting obligations. **Design implication:** a browser game with no chat system cannot assume an external embassy; Nation Supremacy must either provide an in-game negotiation surface (Prompt 13) or accept that diplomacy happens off-platform, which creates integrity and record problems.

**DPR-030 — Call of War permits relations to be traded or "bought".** *Community-reported mechanic* (`DPS-013`). "You can trade with the other country. Usually you exchange relations (right of way for right of way, or shared map for shared map), but you can also 'buy' relations by offering resources, units, provinces." The official wiki documents the diplomacy screen but not side payments. **Limitation:** community evidence; it shows that a relation grant can be bundled with a transfer, which is a cross-system interface Nation Supremacy would have to authorise explicitly.

**DPR-031 — Comparative finding: proposals are usually one-shot; permissions are rarely re-checked after proposal.** *Comparative finding* (`DPS-008`, `DPS-010`, `DPS-014`, `DPS-016`). eRepublik checks congress at the vote; EVE checks office at declaration; Stellaris checks acceptance factors at offer time. No source documents what happens if the proposer loses office, the counterparty changes government, or the target becomes ineligible between proposal and acceptance. **Design implication:** stale authorization is an unaddressed risk across the genre, not a solved pattern to import.

**DPR-032 — Comparative finding: a treaty can be invalidated by a third-party conflict.** *Official-wiki mechanic* (`DPS-008`) and *verified official rule* (`DPS-016`). eRepublik's "friend of a friend" rule cancels an MPP when a party attacks a country that shares a pact with it. EVE moves a war to alliance level when a defending corporation joins an alliance, and drops existing allies. **Design implication:** overlapping commitments need an explicit conflict-resolution rule; otherwise the same treaty can be both active and impossible to honour.

### 6.4 Reputation and diplomatic consequences

**DPR-033 — Stellaris separates accumulated Trust from derived Opinion.** *Community-reported mechanic* (`DPS-014`, `DPS-015`). "Maintaining any form of lasting treaty generates Trust, which increases Opinion. The maximum amount of Trust obtainable is limited by the most valuable treaty between both parties." Trust decays by 0.25 per month if no treaty generates it. Opinion is a sum of many modifiers, including permanent ethics, relationship modifiers, at-war and treaty modifiers. **Design implication:** "reputation" can be two registers with different lifetimes: a slow, treaty-fed trust value and a fast, event-fed opinion value.

**DPR-034 — Stellaris makes treaty exit visible in the relationship value.** *Community-reported mechanic* (`DPS-014`, `DPS-015`). Ending a treaty applies a temporary Opinion penalty whose size depends on the treaty; the relationship table shows the penalty before the player acts. At-war applies −50 Opinion; a Defensive Pact +20; a Federation +50. **Design implication:** if Nation Supremacy stores a reputation effect, the player should see the consequence before confirming, not after.

**DPR-035 — EVE's standings are labels, not a game-computed reputation.** *Community-reported mechanic* (`DPS-018`) plus *official support* (`DPS-019`). A corporation can set another entity to Excellent/Good/Neutral/Bad/Terrible or an intermediate value, add a free-text label, and use it for rules of engagement. The other side does not see it unless it sets a reciprocal standing. There is no global "trust" or "credibility" score. The NPC standing formula (diminishing returns toward ±10, derived faction standings) is a separate NPC-only system.

**DPR-036 — EVE's NPC standing formula is a documented diminishing-returns curve.** *Verified official rule* (`DPS-019`). Gains are `ns = ((10 − s) × i) + s`; losses use −10 as the target. Derived standings cannot push a standing beyond the source entity's own standing. **Design implication:** a reputation formula can be bounded and self-limiting without a hard cap, but it needs a published expression and a rounding rule (Prompt 14).

**DPR-037 — P&W has no formal diplomatic reputation register.** *Absence finding* (`DPS-001`…`DPS-007`). The official treaty web, rules, glossary and embargo pages document treaty types, enforcement, abuse rules and embargoes, but no credibility, trust, honour or standing value. Enforcement is moderator action (war-slot filling, bank evasion) plus player memory on forums and Discord. **Limitation:** absence from the pages reached is not proof that no hidden or new metric exists.

**DPR-038 — Call of War's popularity is a global consequence of war declarations.** *Community-reported mechanic, weak* (`DPS-013`). "Declaring war decreases your popularity with every country. A small morale penalty is incurred for being at war." The same page says AI countries "automatically embargo (and eventually declare war) on countries with a low reputation". No official page reached documents the formula, the visibility or the recovery. **Limitation:** one community wiki; not used as a model, only as evidence that a global standing metric can exist.

**DPR-039 — eRepublik documents no diplomatic reputation register.** *Absence finding* (`DPS-008`…`DPS-010`). The law history, active MPP list and war record provide an audit trail, but no trust, honour or credibility value is documented. **Limitation:** the wiki pages reached are mechanic pages, not a full game manual.

**DPR-040 — Comparative finding: no comparator exposes a single global "diplomatic score", and none scopes reputation to an account across nation rerolls.** *Comparative finding* (`DPS-001`…`DPS-019`). Reputation is either a derived opinion sum (Stellaris), an accumulated trust value (Stellaris), a manual player label (EVE), a vague popularity value (Call of War, community-reported), or absent (P&W, eRepublik). No comparator has Nation Supremacy's reroll model (one account, many successive nations), so **UD-033 cannot be answered by analogy**. This is the central evidentiary finding for §11.
### 6.5 Sanctions and diplomatic actions

**DPR-041 — eRepublik's embargo is bounded, renewable and non-retroactive.** *Official-wiki mechanic* (`DPS-009`). It requires executive proposal and congressional approval, lasts 30 days, can be renewed, applies by **citizenship**, blocks new offers and offer updates, leaves existing offers in place until sold or removed, and is automatically equivalent to a state of war. There is no fine or reparations mechanic attached. **Design implication:** the evidence supports a sanction that is a **time-boxed legal state** with a legislative check, not a permanent treaty clause.

**DPR-042 — P&W's embargo is individual, bilateral in effect and public.** *Verified official page* (`DPS-003`) plus *community-reported mechanic* (`DPS-007`). The public list shows 7,300 embargoes with date, embargoer, embargoed and a free-text reason. The community wiki says a player places it, an alliance government cannot force it, and neither side can accept the other's offers. The wiki also claims a slight approval effect, which the official page does not show. **Design implication:** a unilateral act with bilateral effect is possible, but it creates a duplicate-record problem: a reciprocal pair appears as two rows (`DPS-003`).

**DPR-043 — Call of War couples war and embargo to market access.** *Official-wiki mechanic* (`DPS-011`, `DPS-012`). Nations at war cannot buy each other's offers; a trade embargo blocks the same purchases while both remain at peace; ceasefire and trade embargo occupy one relation slot depending on whether the pair is at war. **Design implication:** a diplomacy-owned restriction can be read by the market without the market inventing a tariff. This matches B-07's MKT-218 contract exactly.

**DPR-044 — Comparative finding: sanctions are usually a relation state or a time-boxed law, not a treaty.** *Comparative finding* (`DPS-007`, `DPS-009`, `DPS-011`, `DPS-014`). eRepublik uses a 30-day law; P&W uses a standing unilateral embargo; Call of War uses a relation; Stellaris has no documented embargo action in the pages read (it has war, rivalry, closed borders and fleet actions). **Design implication:** Nation Supremacy should decide whether a sanction is a **relationship**, an **agreement**, or a **separate time-boxed act**. The comparators do not converge.

### 6.6 Player experience and communication

**DPR-045 — P&W's public treaty web makes the alliance graph legible at a glance.** *Verified interface observation* (`DPS-001`). The page lists the types, explains each acronym, draws the graph and hides the least hostile ties by default. **Design implication:** a public, explained relationship view is achievable; the default filter is itself a design choice that can hide relevant obligations.

**DPR-046 — Call of War shows both sides of a relation, and warns that the display can be stale.** *Official-wiki mechanic* (`DPS-011`) and *community-reported mechanic* (`DPS-013`). The diplomacy list shows "your diplomatic relation" and "their diplomatic relation" separately, plus activity status. The community wiki warns that the other player "may not see the change quickly". **Design implication:** a two-column display is honest about asymmetry, but it needs a freshness indicator or players will act on stale information.

**DPR-047 — Stellaris previews acceptance factors and exit costs.** *Community-reported mechanic* (`DPS-014`). The diplomacy tables publish the modifiers that affect an AI's acceptance and the Opinion penalty/truce that follows ending each agreement. **Design implication:** publishing the consequence before the action is a testable UX standard; it costs nothing in rules complexity.

**DPR-048 — EVE exposes a public war report and a war history.** *Verified official rule* (`DPS-016`) and *community-reported mechanic* (`DPS-018`). The war report is visible to anybody and lists ships killed and ISK value by side, with lossmails; the War tab shows finished, current and pending wars. Start and end notifications go to all parties and shareholders. **Design implication:** a diplomacy record can be public without exposing private messages; the public object is the **outcome**, not the negotiation.

**DPR-049 — eRepublik makes the legislative record visible.** *Official-wiki mechanic* (`DPS-008`, `DPS-010`). Proposals are laws; votes are recorded; active MPPs are listed; a counterparty's peace proposal appears 24 hours after the proposer's. **Design implication:** a proposal that is visible to the counterparty only after a fixed delay is a deliberate anti-rush device, but it must be explained or it reads as a missing notification.

**DPR-050 — Comparative finding: no comparator documents a complete "what does this treaty oblige me to do?" surface.** *Comparative finding* (`DPS-001`…`DPS-019`). P&W explains treaty types but not obligations in context; Stellaris lists effects; EVE shows war status; eRepublik lists laws. None provides an obligation dashboard that names the next deadline, the action required and the consequence of failure. **This is an evidence gap and a design opportunity, not a proven player need.**

### 6.7 Integrity, fairness and abuse

**DPR-051 — P&W documents war-slot filling as a named violation, including declaring on allies.** *Verified official rule* (`DPS-002`). Declaring war without intent to fight, declaring to block others from attacking, coordinating to fill slots, and declaring on allies are violations; moderators may manually peace the war. **Design implication:** a formal war/peace system creates a new abuse surface — declaring to occupy a slot rather than to fight — which the diplomacy rules must either prevent or hand to moderation.

**DPR-052 — P&W treats alliance-bank routing around same-network trade restrictions as bannable.** *Verified official rule* (`DPS-002`). Two nations on one network may share an alliance but may not declare on the same targets; using an alliance bank to evade trade restrictions is explicitly bannable. **Design implication:** the alliance interface is not optional for diplomacy integrity; this is exactly the B-03 D-035 contract.

**DPR-053 — P&W documents protection-timing exploitation by name.** *Verified official reference* (`DPS-004`). The glossary defines "beige cycle" as timing wars so a defeated nation cannot rebuild, and "wardodger" as a player who avoids alliance wars by desertion or vacation mode. **Design implication:** peace/ceasefire timing is an abuse surface; a ceasefire that resets protection or a surrender that clears obligations can be farmed.

**DPR-054 — Comparative finding: duplicate, reciprocal and race-prone records are handled by a handshake or a single authoritative object, not by trusting the UI.** *Comparative finding* (`DPS-003`, `DPS-008`, `DPS-016`, `DPS-018`). P&W's embargo list shows reciprocal pairs as two records (`DPS-003`). eRepublik uses a proposal/vote with escrowed funds and refunds on failure (`DPS-008`). EVE gives each war one object with named sides and a single end transition (`DPS-016`). EVE standings are explicitly one-way and private, so two sides can hold different labels without contradiction (`DPS-018`). **Design implication:** Nation Supremacy needs one authoritative record per agreement plus an explicit rule for what a second reciprocal act means; the comparators show both the failure mode and the remedy.

## 7. Comparative matrix

The matrix compares what the sources actually establish. "Unknown" means the sources reached do not answer the question; it is not a negative finding. Cell references point to the findings in §6.

| Dimension | Politics & War | eRepublik | Call of War | Stellaris | EVE Online | Nation Supremacy implication |
|---|---|---|---|---|---|---|
| **Relationship model** | Alliance-level treaty web with ten types; only NAP enforced (`DPR-001`, `DPR-002`); no nation-level posture documented | Symmetric MPP plus separate peace/war and embargo laws (`DPR-004`); no general posture ladder | Seven directional relations; each side can differ (`DPR-006`, `DPR-007`) | Unilateral opinion summed into a bilateral relation level that gates actions (`DPR-008`) | Private one-way standings plus a separate formal war object (`DPR-010`, `DPR-011`) | Two layers are defensible: a directional posture and a mutual agreement record. A single symmetric status cannot express the evidence (`DPR-013`). |
| **Diplomatic agreements** | Treaty records; expiry/cancellation not documented as automatic (`DPR-018`); rich status vocabulary is community-only (`DPR-003`) | MPP: proposal, dual approval, 30 days, renewal; peace: dual approval with 24 h delay; embargo: 30-day law (`DPR-015`…`DPR-017`) | No formal agreement object documented; relations are the agreement (`DPR-006`) | Bilateral offer/accept; type-specific effects; exit penalties and truces (`DPR-019`) | War object with declaration, warm-up, bills, surrender, HQ loss (`DPR-021`) | A lifecycle must name proposal, activation, duration, renewal, amendment, termination and breach separately. Most comparators leave at least two of these undocumented (`DPR-023`…`DPR-025`). |
| **Authorization** | Alliance offices exist; no treaty permission matrix documented (`DPR-028`); negotiation is external (`DPR-029`) | President proposes, congress approves, dictator overrides (`DPR-026`) | Player changes the relation directly; no acceptance documented (`DPR-007`) | Offer accepted by recipient; federation invites need other members (`DPR-014` table) | CEO/director roles for declaration, surrender, ally offers (`DPR-027`) | Nation Supremacy needs an explicit authority rule for propose, accept, withdraw, amend and terminate — and a re-check at acceptance (`DPR-031`). |
| **Timing** | Offers/treaties appear to wait; no expiry documented (`DPR-018`) | 30-day terms; 24 h counterparty delay; renewal before expiry (`DPR-015`…`DPR-017`) | Relation change is immediate; display may lag (`DPR-007`, `DPR-046`) | 10-year action cooldowns; 1-year envoy lock; treaty-end truces (`DPR-020`) | 24 h warm-up; weekly bills; 24 h end cooldown; 14-day surrender lockout; 4 h ally entry (`DPR-021`, `DPR-022`) | Activation delay, duration, cooldown and expiry are four different timers. A 2-hour turn game must state which boundary each one lands on. |
| **Reputation** | No formal register; moderator enforcement and player memory (`DPR-037`) | No register documented; law history is the record (`DPR-039`) | Popularity falls on war declaration; AI reacts to low reputation (community, weak) (`DPR-038`) | Trust (accumulated, treaty-fed, decaying) plus Opinion (derived sum) (`DPR-033`, `DPR-034`) | Player-set one-way standings; NPC standing formula only (`DPR-035`, `DPR-036`) | "Reputation" is not one thing. 08B must decide whether it is a stored register, a derived value, a player label, or absent — and what scope it has (`DPR-040`). |
| **Sanctions** | Unilateral embargo with bilateral effect, public reason, no documented duration (`DPR-042`) | 30-day renewable law; citizenship-based; grandfathers existing offers; war acts as embargo (`DPR-041`) | Trade embargo or war blocks market purchases (`DPR-043`) | No embargo action documented in the pages read (`DPR-044`) | War/standing consequences; no general embargo documented | A sanction can be a relation, a law, or a separate act. Its effect must be owned by Diplomacy and read by the market, never invented as a market fee (`DPR-043`, `DPR-044`). |
| **Information** | Public treaty web; NAP hidden by default; public embargo list with reasons (`DPR-045`, `DPR-042`) | Laws, votes and active MPP list visible; counterparty delay (`DPR-049`) | Two-column relation display; stale-display warning (`DPR-046`) | Acceptance factors and exit costs published (`DPR-047`) | Public war report and war history (`DPR-048`) | Publish the outcome and the obligation, not the private negotiation. D-030's pending-act rule already supplies the boundary. |
| **Integrity** | War-slot filling, ally declarations, bank evasion and protection timing are documented abuses (`DPR-051`…`DPR-053`) | Escrow and refund on failed proposal; automatic friend-of-a-friend cancellation (`DPR-054`) | Relations can be bought; asymmetric grants can mislead (`DPR-030`) | Cooldowns and truces deter churn (`DPR-020`) | Cost, eligibility, surrender lockout and war-copy on membership change (`DPR-054`) | Duplicate proposals, reciprocal records, stale authorization, protected-state farming and membership transitions are the material abuse surfaces. |
| **Cross-system interactions** | Treaty enforcement tied to war declaration only; embargo tied to trade; alliance bank restricted (`DPR-001`, `DPR-042`, `DPR-052`) | MPP triggers war; embargo affects markets; peace ends war; natural-enemy lock (`DPR-004`, `DPR-016`, `DPR-041`) | War/embargo affect market access; relations can bundle transfers (`DPR-030`, `DPR-043`) | Treaties gate war and generate trust; federation is a separate governance layer (`DPR-009`) | Membership changes move wars; standings control structure behaviour (`DPR-021`, `DPR-035`) | Every diplomacy effect must name its owning system and its resolution phase. War, trade, politics and alliances already have owners. |
| **Complexity** | Low rule count, high social complexity; the game enforces little (`DPR-001`) | Moderate rule count; heavy legislative ceremony (`DPR-026`) | Low rule count; high per-action opacity (`DPR-007`, `DPR-046`) | High rule count; many treaties, modifiers and cooldowns (`DPR-014`, `DPR-015`) | Moderate diplomacy rules; very high war-object complexity (`DPR-016`) | Nation Supremacy's first playable diplomacy should be **smaller than Stellaris and more explicit than P&W**: few states, few treaties, one visible lifecycle, one limit per action (D-024). |

### 7.1 What the matrix establishes, and what it does not

**Establishes:**

1. **A layered model is the norm.** Every comparator with more than a war/peace switch separates a relationship state from an agreement and from an enforceable effect (`DPR-009`, `DPR-013`, `DPR-014`).
2. **Enforcement is selective.** P&W enforces only NAP; eRepublik enforces MPP triggers and embargo blocks; Stellaris enforces treaty effects; EVE enforces war and standings only where coded. No comparator enforces every promise (`DPR-001`, `DPR-019`, `DPR-037`).
3. **Time-boxing is common for sanctions and treaties.** 30 days (eRepublik), weekly war bills (EVE), 10-year cooldowns (Stellaris) (`DPR-015`, `DPR-020`, `DPR-021`).
4. **Public outcomes, private negotiation.** P&W, EVE and eRepublik publish records; none publishes the negotiation itself (`DPR-045`, `DPR-048`, `DPR-049`).

**Does not establish:**

1. That a 30-day treaty or a 10-year cooldown is right for a 2-hour-turn game; those durations belong to different session shapes.
2. That a reputation register improves play; two comparators have none and one has only a community-reported popularity value (`DPR-037`…`DPR-039`).
3. That formal counterproposals, proposal expiry or obligation dashboards are needed; the evidence is absent, not positive (`DPR-024`, `DPR-050`).
4. Any player-experience finding for Nation Supremacy; no survey or playtest exists (§15).

## 8. Nation Supremacy design implications

These are **design implications** and **analysis**, not approved rules. Each names the evidence and the existing project constraint it touches. 08B may accept, reject or reshape any of them, with a recorded decision.

### 8.1 Structure: keep three layers separate

The strongest finding is that a relationship, an agreement and an enforceable obligation are different objects (`DPR-013`, `DPR-014`). B-02 already gestures at this: **TR-019** lists a directional **posture** family and a mutual **Agreement** family separately. The implication is to keep them separate in B-08:

1. **Posture (directional):** A's attitude to B, recorded immediately, visible as a posture, with no automatic obligation. This matches TR-019 and Call of War's two-column display (`DPR-006`).
2. **Agreement (mutual):** a recorded instrument with parties, terms, status and a lifecycle. This is the object D-030's pending rule applies to.
3. **Effect (enforced):** the subset of agreements that changes what another system will permit (for example, a non-aggression instrument that blocks a war declaration). P&W proves a game can have many agreements and few effects (`DPR-001`).

**Why not one status field:** a single field cannot represent "friendly posture, no treaty", "hostile posture, binding NAP", "neutral posture, aid agreement" or "treaty signed but not yet active". Every comparator that tried to collapse these layers documents an anomaly (`DPR-003`, `DPR-009`, `DPR-014`).

### 8.2 Scope: a minimal first-playable treaty set is defensible

UD-013 offers "(a) NAP + two promises" or "(b) full treaty types". The evidence favours a **small, typed set with explicit effects** over a P&W-style catalogue of ten (`DPR-001`, `DPR-003`). P&W's ten types are mostly **social labels**; copying them would create a rulebook full of entries with no mechanical consequence, which conflicts with the Bible's "one authoritative rule per family" discipline and with D-024's requirement that every action have a real limit.

A defensible candidate shape for 08B (not approved):

| Layer | Candidate content | Evidence | Project constraint |
|---|---|---|---|
| Posture | A small directional set (for example friendly / neutral / tense / hostile) | TR-019; CoW (`DPR-006`) | Must not create a map or a border |
| Record agreements | Non-aggression; a promise/consultation instrument; an aid or transfer agreement | P&W PIAT/ODP as social records (`DPR-001`); eRepublik MPP (`DPR-004`) | Aid is a B-04 transfer with matched ledger events (ECN-212) |
| Enforced effects | At most a non-aggression block on war declaration; an aid delivery obligation if the design wants one | P&W enforces only NAP (`DPR-001`); Stellaris enforces NAP (`DPR-019`) | War is Prompt 10's; B-08 may only define the diplomatic permission, not the campaign |
| Sanctions | A separate, time-boxed act, if adopted at all | eRepublik embargo (`DPR-041`); P&W embargo (`DPR-042`) | May not be a market fee (MKT-185/218) |

**Why not copy eRepublik's MPP:** it is an **automatic war-entry** treaty. Nation Supremacy's war system is Prompt 10's, and D-023 keeps warfare out of the first playable. An MPP would bind 08B to a war rule that does not exist yet. **Open question `DQ-04`.**

### 8.3 Lifecycle: name every state, including the boring ones

The comparators collectively demonstrate the states a treaty needs, even where no single game documents all of them (`DPR-015`…`DPR-025`):

`DRAFT` (optional, local) → `PROPOSED` → `COUNTERED` (only if adopted) → `ACCEPTED` (both parties) → `ACTIVE` (at a boundary, if an activation delay exists) → `AMENDED` / `RENEWED` → `EXPIRED` / `WITHDRAWN` / `CANCELLED` / `TERMINATED` / `BREACHED` → `HISTORICAL`.

Three implications:

- **Signature ≠ activation.** eRepublik activates on acceptance; EVE activates 24 hours later; a boundary-resolved game should state which boundary makes a treaty active (`DPR-005`, `DPR-021`).
- **Expiry needs an owner.** P&W's expiry is undocumented (`DPR-018`); eRepublik's is automatic (`DPR-015`). If Nation Supremacy has durations, the boundary must expire them and write a record; if it has no durations, it must say so.
- **Withdrawal before activation is not documented anywhere.** `DQ-06` asks 08B to decide it rather than import a guess.

### 8.4 Authority: resolve it from the nation and the political state

Nation Supremacy has no alliance offices yet (Prompt 09) and no cabinet offices in B-06; the player is the nation's leadership (B-06's abstraction). The evidence still matters:

- eRepublik's executive/legislature split (`DPR-026`) cannot be copied because B-06's player is the executive and there is no parliament with a veto. A **role-and-chamber** model would require a political institution the project has not designed.
- EVE's office-based authority (`DPR-027`) is a Prompt 09 matter for alliances, not a nation rule.
- P&W's missing treaty permission matrix (`DPR-028`) is a warning: **do not leave "who may sign" implicit.**

The minimum defensible rule for 08B is: **the authenticated owner of the active nation is the only authority for nation-level diplomacy**, subject to B-06's `TRANSITION`/`CRISIS` read-only state (DMP-263) and B-03's pair restrictions. If a later prompt adds delegation (alliance roles, officials), it must extend this rule explicitly. **`DQ-07`.**

### 8.5 Timing: four timers, one clock

The evidence distinguishes four timers (`DPR-020`…`DPR-023`):

1. **Activation delay** — time between acceptance and effect (EVE 24 h).
2. **Duration** — how long an active agreement lasts (eRepublik 30 days).
3. **Cooldown** — how soon the same action can be repeated (Stellaris 10 years).
4. **Expiry deadline** — when an unanswered proposal lapses (not documented anywhere).

Nation Supremacy has a 2-hour boundary and a class Q/S model. Any of these timers must be expressed in **turns**, state which **boundary phase** applies, and be visible before commitment (B-02 TR-006/TR-008). A timer that resolves off-boundary would violate the turn model.

### 8.6 Economy: no new currency, no OP, no invented fee

- Diplomacy may move crowns/resources only as a **transfer** with matched ledger events (ECN-212).
- Operations Points are military-only (D-015) and must not become a diplomacy cost.
- There is no prestige, influence or diplomatic-point currency (`DD-067`), and 08B must not invent one without a decision.
- A treaty cost, if any, is a crown cost with a B-04 ledger row; a sanction is not a fee (MKT-185/218).
- Aid must not move capacity, DC, housing or research points (URB-155); it may not move approval or population (DMP-138).

### 8.7 Reputation: decide the purpose before the metric

The evidence offers four models (`DPR-033`…`DPR-040`):

1. **Derived opinion** — a sum of modifiers, no stored history (Stellaris Opinion).
2. **Accumulated trust** — a stored value fed by treaties and decaying (Stellaris Trust).
3. **Player label** — private, one-way, free-text (EVE standings).
4. **Absent** — no register; social consequences only (P&W, eRepublik).

A design implication, not a recommendation: **if the purpose is to make breach costly, a stored breach record with a defined effect is needed; if the purpose is to help players judge counterparts, a derived or player-set display may be enough.** A single global "honour" score is not supported by any comparator and would be hard to explain. UD-033 is analysed in §11; the purpose question is `DQ-08`.

### 8.8 Sanctions: a separate act, bounded and visible

If 08B adopts sanctions, the evidence supports (`DPR-041`…`DPR-044`):

- an explicit **eligibility** rule (who can be sanctioned; not the same as war);
- a **scope** list (what is blocked: new aid, new directed trades, new market listings, new construction/research/policy actions — each already bounded by B-04/B-05/B-06);
- a **duration** and a renewal path, or an explicit "until lifted" rule;
- an **activation** and **termination** path, with the market reading the restriction rather than inventing one;
- a **visibility** rule: the fact of the sanction public, the reason and terms as D-030 permits;
- a **grandfathering** rule for already-accepted trades and already-started construction (eRepublik's model; `DPR-041`);
- an **abuse** rule for reciprocal duplicate records and for sanctioning to dodge a pair restriction.

**Boundary:** a sanction is not a war and must not declare one; a blockade is a warfare mechanic (Prompt 10), not a diplomacy one, unless 08B explicitly defines a diplomatic permission that Prompt 10 enforces.

### 8.9 Communication: publish outcomes, deadlines and consequences

The evidence supports (`DPR-045`…`DPR-050`):

- a two-sided display of directional posture (CoW);
- a clear list of agreements with status, parties, start/end turns and next deadline;
- a preview of the consequence before accepting or terminating (Stellaris);
- a public record of signed agreements and their outcomes, with private terms hidden (D-030; EVE war report);
- an explanation of every failure ("expired", "withdrawn", "counterparty in transition", "restricted pair"), not a generic error.

No comparator documents a full obligation dashboard (`DPR-050`); that is an opportunity for Prompt 13, not a proven requirement.

### 8.10 Abuse: design the timing, not just the button

The documented abuses that map to Nation Supremacy are:

| Abuse | Evidence | Project surface | Candidate mitigation (08B/08C) |
|---|---|---|---|
| Proposal/cancellation spam | Stellaris cooldowns (`DPR-020`); D-024 | Proposal caps, per-pair cooldown | Declare a visible limit; no hidden throttle |
| Declaring/accepting to occupy a slot | P&W war-slot filling (`DPR-051`) | War is Prompt 10; diplomacy may create a "declaration" record | Do not let a diplomatic act reserve a war slot; keep declaration and campaign separate |
| Reciprocal duplicate records | P&W embargo list (`DPR-054`) | Two nations embargo each other | One authoritative record per pair+type, or an explicit reciprocal state |
| Stale authorization | `DPR-031` | Leadership transition (B-06), reroll (B-03), pair restriction | Re-validate at acceptance and at activation; fail with a named reason |
| Protection/ceasefire farming | P&W beige cycle (`DPR-053`) | Peace/ceasefire is Prompt 10 | 08B must not let a diplomatic act reset protection; coordinate with 10 |
| Membership-change escape | EVE war copy (`DPR-021`) | Reroll/alliance join-leave | Reroll termination is B-03's; alliance change is Prompt 09's; 08B must not create an escape |
| Treaty as a transfer disguise | CoW bought relations (`DPR-030`); B-03 D-035 | Aid/reparations | Every transfer is a B-04 ledger event and passes the pair check |

### 8.11 What 08B should **not** do

- Do not design a world parliament, a global vote, or a reputation score for the whole world; none is in scope, and no comparator supports it.
- Do not define war declarations, campaigns, ceasefires or peace terms; Prompt 10 owns them.
- Do not define alliance membership, roles, banks or governance; Prompt 09 owns them.
- Do not add a market fee, tariff, tax or price band; B-07 owns them and MKT-185 forbids the shortcut.
- Do not add a new currency or a new action currency.
- Do not make a treaty's effect depend on geography, distance or borders.
- Do not treat P&W's ten treaty labels as a requirement.

## 9. Existing approved requirements and constraints

### 9.1 Approved constraints and confirmed decisions that bind 08B

These are **fixed** unless a new decision changes them. They are not reopened by this report.

| ID | Position | Status | Source | Consequence for Diplomacy |
|---|---|---|---|---|
| **REQ-041 / DD-013** | Fictional **mapless** world; a symbolic network of nations and relationships | **Approved** | AI_CONTEXT §2; B-02 TR-012 | No borders, distances, provinces, fronts or geographic eligibility |
| **REQ-015** | One global turn every 2 hours on fixed UTC boundaries | **Approved** (cadence) | AI_CONTEXT §2; B-02 TR-024…TR-031 | Every duration, cooldown, expiry and activation resolves at a boundary |
| **D-015** | Operations Points are the single **military-only** action resource, refilled to cap, non-transferable, reserved/consumed under B-02 | **Confirmed** (model); values Provisional | DECISIONS.md D-015 | Diplomacy may not cost, grant or trade OP |
| **D-018 / REQ-043** | One account per person is prohibited where multiple; enforcement is proportionate and review-first | **Confirmed** (policy) | DECISIONS.md; B-03 | Diplomacy cannot be a route around account restrictions |
| **D-020** | CP/FPB taxonomy; Stage 2 completion is neither | **Confirmed** | DECISIONS.md | No "first playable" claim for diplomacy |
| **D-023** | Warfare is in scope, designed in Prompt 10, **not in the first playable** | **Confirmed** | DECISIONS.md | 08B must not require a war rule to make a treaty work |
| **D-024** | No shared general action budget; every non-military subsystem declares a visible limit | **Confirmed** | DECISIONS.md; B-02 §24 | 08B must declare treaty/proposal/sanction limits |
| **D-025** | Forward-only recovery; a FAILED turn waits; accepted actions stay pending | **Confirmed** (policy) | DECISIONS.md | A diplomatic action accepted before a failed turn must not vanish or double-apply |
| **D-026** | Class-S hot 30 days → monthly summary 12 months; class-P permanent; audit spine permanent | **Confirmed** (policy) | DECISIONS.md | Treaty and breach records need a data class; a class-P event is permanent |
| **D-027** | k = 5 aggregate threshold, stable merging, complementary suppression | **Confirmed** | DECISIONS.md | No diplomatic statistic may expose a small group's private terms |
| **D-028** | Dormancy at 14 days/168 turns; no offensive targeting or initiation; no decay; rankings excluded; reversible archival | **Confirmed** (policy); threshold Provisional | DECISIONS.md | A dormant counterparty cannot be newly attacked or initiate; what happens to its pending proposals is 08B/08C's |
| **D-030 / DD-048** | A pending proposal is visible to its named counterparty, not to third parties until declared/effective/published; rejection/withdrawal private unless published | **Confirmed** (design) | DECISIONS.md; B-02 TR-020 | 08B implements this rule; it does not re-decide it |
| **D-031** | Account status, nation status and pair status are three separate state machines | **Confirmed** (design) | DECISIONS.md; B-03 §4.2/§5.4/§10.1 | A diplomatic restriction is not an account suspension and not a nation status |
| **D-032 / REQ-061** | One account owns 0..1 active nation; ownership from the session; no re-parenting | **Confirmed/Provisional** | DECISIONS.md; B-03 | Only the active nation's owner can act |
| **D-034** | Five pair states, 24 h observation window, 180-day life, 25-account large-network rule | **Confirmed** (design); thresholds Provisional | DECISIONS.md; B-03 §5.3 | A restricted pair cannot treaty; a pair check runs in the committing transaction |
| **D-035 / DD-052** | A pair cannot achieve through an alliance, third nation or market what is blocked directly; no alliance-bank use while restricted | **Confirmed** (design) | DECISIONS.md; B-03 §5.5 | A treaty, aid or sanction may not be an indirect route |
| **D-039** | Instant reroll; total reset; account sanctions and pair restrictions survive; blocked during a campaign/settlement/hold | **Confirmed** (design); thresholds Provisional | DECISIONS.md; B-03 §9 | Reroll terminates treaties (RRL-019); UD-033 governs breach reputation |
| **D-042** | Eighteen data categories; no raw IP; permanent audit spine; least privilege; no silent history rewrite | **Confirmed** (design); values Provisional | DECISIONS.md; B-03 §14 | Treaty history, private terms and reasons need a data class and access rule |
| **D-049 / DD-067** | One currency (the crown); one national pool; no second currency; an alliance pool is separate and audited | **Confirmed** (design) | DECISIONS.md; B-04 §12 | No prestige, influence or diplomatic-point currency |
| **D-050** | No debt, zero floor, published austerity order | **Confirmed** (design) | DECISIONS.md; B-04 | A treaty or sanction may not create a negative balance |
| **D-055** | Append-only ledger; corrections are new disclosed events | **Confirmed** (design) | DECISIONS.md; B-04 | Every diplomatic value movement writes matched ledger events |
| **D-109…D-122** | The two-system market; directed first-playable; Global Trade approved scope but release-gated; D-122 separates feature approval from release | **Confirmed/Provisional as each row states** | DECISIONS.md; B-07; 07C | 08B may add a diplomacy rule that the market reads, but may not change a `MKT-` rule or release a gate |

### 9.2 Provisional contracts that 08B must satisfy or amend explicitly

| Contract | Source | What it requires of Diplomacy | Status |
|---|---|---|---|
| **Relationship families** | B-02 **TR-019** | Posture is directional and recorded immediately; an Agreement is mutual and owned by Prompt 08; alliance membership is Prompt 09; conflict is Prompt 10 | Provisional |
| **Pending-act visibility** | B-02 **TR-020**; **D-030** | Counterparty-only while pending; public on declaration/effect/publication; private rejection/withdrawal | **D-030 Confirmed**; TR-020 Provisional |
| **One class per field; aggregates do not leak** | B-02 **TR-021/TR-022**; **D-027** | Every diplomatic field needs a class; no aggregate may expose terms or a small group | Provisional/Confirmed |
| **Declared limits** | B-02 **§24**; **D-024** | At least one visible limit per diplomacy action | Confirmed |
| **Reservation and class Q/S timing** | B-02 **§17–§19** | Cost-bearing actions reserve at acceptance, charge at resolution; accepted actions re-validate at P2; failure uses `F` codes | Provisional |
| **Failure codes** | B-02 **§17.4** | Use the shared vocabulary; subsystem-specific codes may wrap, not replace | Provisional |
| **Recovery/idempotency** | B-02 **§20–§21**; **D-025** | One outcome per action; no double publication; retries safe | Confirmed policy |
| **Restricted pair cannot treaty** | B-03 **§5.5 row 15**, **§18 CON-001** | Treaty block; no indirect route | Provisional |
| **Reroll cleanup** | B-03 **RRL-019** | Treaties terminate; class-P event attributed to the old nation; replacement neutral; breach reputation scope is Prompt 08's | Provisional |
| **Reroll blocking conditions** | B-03 **RRL-021** | A reroll is blocked during an active campaign, unsettled settlement, preservation hold or disqualifying state | Provisional |
| **Aid, reparations, embargo, sanctions** | B-04 **ECN-212** | Transfer with matched ledger events; embargo blocks but destroys nothing; sanction freezes but cannot create a negative balance; effects at P4; D-030 applies | Provisional |
| **Sanction scope in cities/research** | B-05 **URB-155** | May freeze a construction/research action; may not delete owned assets; aid never moves capacity/DC/housing/RP | Provisional |
| **Sanction scope in politics** | B-06 **DMP-138** | May freeze a policy change; may not change government/delete policy/create negative balance; no prestige input or approval modifier without a named 08 term | Provisional |
| **Treaties survive transition/crisis** | B-06 **DMP-263**; **REQ-360/361** | Treaties persist; diplomacy is read-only while authority is suspended; a leadership change does not void a treaty | Provisional |
| **Market reads a diplomacy restriction** | B-07 **MKT-185/217/218/220** | A diplomacy restriction is a separate rule; the market reads it; no fee, tariff or silent value movement; B-08 owns an embargo rule if one exists | **MKT-185** is an **approved constraint** (DMP-262); MKT-217/218/220 are Provisional |
| **07C inheritance** | 07C **§15.3/§15.5** | 08 inherits the two market systems and may not add a trade tax, tariff or embargo to the market without a new decision; it adds any restriction to B-08 and records the interface | Accepted at specification level |
| **Alliance boundary** | Roadmap Prompt 09; B-02 TR-019 | Alliance membership, roles, governance, bank, succession and operations are Prompt 09's | Registered |

### 9.3 What this report does not change

No `D-`, `DD-`, `UD-`, `REQ-`, `DMP-`, `MKT-`, `F-TM-`, `PWR-` or gate status is changed by 08A. The only register edits are the status notes and index links required to record that 08A exists; they are listed in §19.3 and in the final report.

---
## 10. Candidate recommendations (unapproved)

Each item is a **candidate recommendation** for Prompt 08B. None is approved; none is a requirement; 08B may reject any of them with a recorded reason. The evidence and trade-offs are stated so 08B can decide rather than re-research.

| ID | Candidate recommendation | Evidence | Trade-offs / limitations | Integration constraint | Status |
|---|---|---|---|---|---|
| **DCR-01** | Model diplomacy in **three layers**: a directional posture, a mutual agreement record, and a separate enforced effect. Do not use one status field for all three. | `DPR-013`, `DPR-014`; B-02 TR-019 | More objects and screens; players must understand the difference. Simpler than hiding effects inside a status. | TR-019 already separates posture and agreement; B-08 must not redefine TR-019 | **Candidate** |
| **DCR-02** | Keep the **first-playable treaty set minimal**: posture + non-aggression + one promise/consultation record + a transfer/aid agreement. Exclude mutual-defence and automatic war-entry treaties until Prompt 10 exists. | `DPR-001`, `DPR-004`, `DPR-019`; D-023 | A small set may feel thin; a large set creates many no-effect labels. | War is Prompt 10's; D-023 excludes it from the first playable | **Candidate** |
| **DCR-03** | Use **one authoritative agreement object per pair and type**, with a stable ID and an append-only event history; a reciprocal act updates the existing object or is explicitly a second, different act. | `DPR-003`, `DPR-054` | Requires a pair+type uniqueness rule; may block deliberately separate instruments. | B-02 idempotency and append-only history; D-042 data classes | **Candidate** |
| **DCR-04** | Define the full lifecycle: `PROPOSED → ACCEPTED → ACTIVE → TERMINATED/EXPIRED`, with `WITHDRAWN`, `REJECTED`, `COUNTERED` (if adopted) and `BREACHED` as explicit outcomes. State the boundary that activates and expires each. | `DPR-005`, `DPR-015`, `DPR-018`, `DPR-021` | More states than a simple on/off switch; each state needs a player-facing label. | B-02 class Q/S, P2 re-validation and P4 application; D-030 pending visibility | **Candidate** |
| **DCR-05** | Resolve nation-level authority from the **authenticated owner of the active nation**, and re-validate at acceptance and activation. Do not invent delegation; leave it to Prompt 09. | `DPR-026`…`DPR-031`; D-032; B-06 DMP-263 | Coarse: no ministers or parliaments. Honest: the project has not designed them. | D-032 session ownership; B-06 transition/crisis read-only | **Candidate** |
| **DCR-06** | Declare **visible limits**: a small number of open outgoing proposals per nation, one live proposal per pair and type, a turn-based expiry, and a short cooldown after withdrawal or rejection. Leave every number to Prompt 14. | D-024; `DPR-020`, `DPR-023` | Caps can frustrate legitimate negotiation; without caps, spam is predictable. | D-024 requires a visible limit; B-02 §24 contract | **Candidate** |
| **DCR-07** | If a reputation register is adopted, prefer a **narrow, event-recorded breach record** over a single global score; make its purpose, scope and decay explicit. If no purpose can be stated, adopt no register. | `DPR-033`…`DPR-040` | Any register can be gamed; a score is hard to explain; an event record is auditable but less visible. | UD-033; D-042 retention; no unnamed modifier (B-06 DMP-138) | **Candidate** |
| **DCR-08** | If sanctions are adopted, make them a **separate time-boxed act** with an explicit effect list, grandfather existing accepted commitments, and have the market read the restriction rather than adding a fee. | `DPR-041`…`DPR-044`; MKT-185/218 | Adds a second diplomacy object; may duplicate war/embargo effects. | B-04 ECN-212; B-05 URB-155; B-06 DMP-138; B-07 MKT-217/218 | **Candidate** |
| **DCR-09** | Implement **D-030 exactly**: pending terms to the counterparty only; a **completed** agreement public (08B must fix whether that means both signatures or activation — see `DPX-01`); private reasons and messages protected; rejection/withdrawal private unless published. | D-030; `DPR-045`, `DPR-048` | Public records can embarrass; private terms can hide collusion. D-030 already chose the balance, and TR-021's “once signed” wording needs the exact event. | B-02 TR-020/TR-021; D-027 aggregates; `DPX-01` | **Candidate** |
| **DCR-10** | Specify **notifications** for proposal received, proposal expiring, accepted, rejected, withdrawn, activated, terminated and breached, with a bounded feed and no duplicate notices. | `DPR-046`…`DPR-049`; B-02 TR-008 | Notification spam; missing a deadline is worse. | Prompt 13 owns the taxonomy (UD-022); B-02 digest | **Candidate** |
| **DCR-11** | Keep **nation-level treaties in B-08** and **alliance-level treaties/governance in B-09**; define a joint contract for what happens when a member joins or leaves an alliance during an active treaty. | `DPR-002`, `DPR-021`; roadmap B-08/B-09 | Splits a natural object; needs a shared schema contract. | Prompt 09 ownership; §13 interface matrix | **Candidate** |
| **DCR-12** | Classify treaty signature, activation, termination and breach as **permanent class-P events**; classify routine proposals and rejections as class-S, subject to D-026. | D-026; B-03 RRL-019 | More permanent rows; better audit and history. | D-026 retention; D-042 audit spine | **Candidate** |

### 10.1 What these recommendations deliberately do not decide

- The actual relationship names and numbers.
- The actual treaty list, durations, cooldowns, caps or costs.
- Whether a reputation register exists, and its scope (UD-033).
- Whether sanctions exist, and their scope.
- Whether counterproposals or proposal expiry exist.
- The phase or ordering band for each diplomatic action.
- Any alliance rule.

Those are 08B's decisions. This section is a starting menu, not a decision record.

---

## 11. UD-033 analysis and status

### 11.1 The exact registered question

From [`05_unresolved_design_decisions.md`](../05_unresolved_design_decisions.md) row **UD-033** (verbatim):

> **UD-033 | Is in-game diplomatic/treaty reputation account-scoped or nation-scoped after a reroll? | B | Prompt 03 fixes only that *enforcement* sanctions survive and that old acts stay attributed to the old nation; the reputation model is Prompt 08's | (a) nation-scoped, reputation dies with the nation (b) account-scoped for breach patterns (c) mixed | B-03, B-08 | No — Prompt 08 decides | 08 | Deferred to Prompt 08 — depends on the reputation registers; the anti-abuse contract is already fixed (RRL-019)**

The same question is recorded in B-03's §2.2 conflicts table as **C-10** ("Account-level vs nation-level reputation"). Its cells say that Report 08 and the diplomacy material did not settle whether a treaty breach follows the account or the nation; that Prompt 03 requires "the **old nation's acts to remain attached to the old nation identity**" and requires that a reroll must not erase an *enforcement* sanction; and that whether in-game diplomatic reputation is account-scoped is left to Prompt 08, with an explicit anti-abuse contract. The row cites `RRL-014`, UD-033 and Prompt 08.

**Meaning, in plain terms:** when a nation breaks a treaty and then its player rerolls into a new nation, does the diplomatic consequence follow the **new nation** (because the same person is behind it), stay on the **old nation** (which no longer exists as an actor), or split between an account-level integrity record and a nation-level public standing?

### 11.2 Why the question matters

1. **Reroll can launder a reputation.** If all diplomatic consequences are nation-scoped and a reroll is free, a player can break a treaty and start clean. B-03 already blocks reroll during a campaign and keeps **enforcement** sanctions, but it does not keep a **diplomatic** penalty (`RRL-017`, `RRL-019`).
2. **A new nation is not the old one.** The replacement starts neutral, with no treaties and no history (RRL-019). Punishing it for the old nation's breach may be unfair to a player who rerolled for unrelated reasons, and confusing to third parties who see a new name.
3. **The game already separates account, nation and pair** (D-031). UD-033 asks which of those objects owns a diplomatic record. A fourth object would violate D-031's discipline.
4. **The answer determines the schema and the history.** An account-scoped register needs account-linked rows that survive nation deletion; a nation-scoped register can die with the nation; a mixed model needs both and a clear display rule.
5. **It affects the anti-abuse contract.** D-035 and B-03's pair matrix already treat indirect routing as a violation. A reputation that can be shed by reroll is an indirect route around the consequences of breach.

### 11.3 Evidence found

| Evidence | What it establishes | Limit |
|---|---|---|
| `DPR-040` | **No comparator exposes a single global diplomatic score, and none scopes reputation to an account across nation rerolls.** P&W and eRepublik document no register; EVE's standings are player-set labels; Stellaris has Trust/Opinion but no account/nation split; Call of War's popularity is community-reported and global. | Comparative absence, not proof that no game does it |
| `DPR-033` | Reputation can be split into an accumulated trust value and a derived opinion value, with different lifetimes. | Single-player grand strategy; no reroll model |
| `DPR-034` | Treaty exit can carry a visible, type-specific penalty. | Stellaris applies it to empires, not accounts |
| `DPR-035`, `DPR-036` | Player labels and NPC standings are different objects; a formula can be bounded and self-limiting. | EVE's player standings are private and one-way, so they are not a public reputation |
| `DPR-037`, `DPR-039` | Two close genre comparators have **no** formal diplomatic reputation register. | Absence findings |
| `DPR-038` | A global popularity value can exist and affect AI. | Community wiki, weak, no formula |
| B-03 `RRL-014`, `RRL-017`, `RRL-019` | Old acts stay attributed to the old nation; enforcement sanctions survive a reroll; treaties terminate and the replacement starts neutral. | Project rules, provisional |
| B-03 C-10 | The question was deliberately left to Prompt 08 with an anti-abuse contract. | Project record |
| B-06 DMP-138 | No diplomatic modifier to approval/population without a named 08 term. | Project rule, provisional |

**Conclusion of the evidence review:** the comparators cannot answer UD-033. They show that reputation can be designed in several ways, but none has Nation Supremacy's exact account/nation/reroll structure. The question is a **product-design decision for 08B**, not a research question that further evidence would settle.

### 11.4 Options, advantages and disadvantages

The options are the three recorded in UD-033. They are reproduced here; no fourth option is invented.

| Option | What it means | Advantages | Disadvantages | Project compatibility |
|---|---|---|---|---|
| **(a) Nation-scoped** | The diplomatic reputation belongs to the nation. A reroll destroys it; the replacement starts neutral. | Simple; matches the "new nation starts neutral" rule (RRL-019); no account-level punishment for a new identity; one owner (the nation) | Reroll launders a breach; third parties cannot distinguish a genuine fresh start from an escape; weakens the cost of breaking a commitment | Compatible with D-031 (nation object) and RRL-019; weak on anti-abuse |
| **(b) Account-scoped for breach patterns** | The breach record follows the account. The new nation inherits a visible or hidden penalty. | Closes the laundry route; makes breach costly across identities; fits D-031's account object for integrity records | Punishes a new nation for the old one's acts; may confuse third parties; could become a de facto account ban; needs a display and appeal rule; risks double-counting with enforcement sanctions | Compatible with D-018/D-039 account sanctions only if it is an **integrity** record, not a new sanction; needs a decision |
| **(c) Mixed** | The historical breach stays attributed to the old nation (public record); the account carries a non-public integrity record for review; the new nation's **diplomatic standing** starts neutral. | Preserves history and fairness; closes the "invisible" part of the laundry route without punishing the new nation publicly; fits D-031's separation; lets Prompt 12 use the record | Two records and a display rule; players may not understand why a hidden account record exists; requires a retention and access rule; the public consequence of breach may still feel weak | Most compatible with B-03 and D-031; requires 08B to define the public/private split and Prompt 12 to own the review use |

### 11.5 Dependencies

- **Whether a reputation register exists at all.** If 08B decides there is no diplomatic reputation register (as P&W and eRepublik), UD-033 becomes moot for in-game reputation; the historical record is still handled by B-03's class-P rule.
- **The definition of "breach".** A register needs an event taxonomy (broken NAP, unfulfilled aid, premature termination). Without it, there is nothing to scope.
- **The reroll rules.** RRL-019 terminates treaties and starts the replacement neutral; RRL-021 blocks reroll in some states. UD-033 must not contradict them.
- **Account sanctions.** D-018/D-039 enforcement sanctions are separate. A diplomatic reputation must not be stored as, or displayed as, an account suspension (D-031).
- **Data retention and access.** D-026 and D-042 determine whether the record is permanent and who can read it.
- **Prompt 12 procedure.** If the account carries an integrity record, Prompt 12 owns its use, review and appeal.
- **Prompt 09 membership.** An alliance may care about a member's breach history; Prompt 09 must not invent a parallel reputation.

### 11.6 Downstream effects

| If 08B chooses | Effect on 08C workflows | Effect on Prompt 09 | Effect on Prompt 12 | Effect on Prompt 14 |
|---|---|---|---|---|
| (a) Nation-scoped | Simple: breach dies with the nation; no cross-reroll display | Alliance sees only the current nation's history | No new account record | No cross-reroll decay formula |
| (b) Account-scoped | Needs a "recent breach" warning on the new nation, an appeal path, and a rule for stale records | Alliance can see an account-linked warning (permission question) | Owns the review, appeal and evidence | Needs decay/expiry and a display threshold |
| (c) Mixed | Needs two records and a clear public/private display | Alliance sees the public nation record only, unless 09 decides otherwise | Owns the integrity record's use | Needs a public-record lifetime, not a score |

### 11.7 What Prompt 08B must decide

08B must decide, with a recorded `D-` entry and a B-08 rule:

1. **Does a diplomatic reputation register exist at all?** If no, say so and record UD-033 as resolved by "no in-game diplomatic reputation; history only" — that is a decision, not a non-answer.
2. **If yes, what is it?** A breach record, a trust value, a derived opinion, or a player label. Do not create a global "honour" score by default.
3. **What is its scope?** Nation, account, or mixed, using the analysis above.
4. **What is public, what is private, and what is permanent?** Cite D-030, D-026 and D-042.
5. **What counts as breach, and what is the consequence?** If there is no consequence, the register is informational; say so.
6. **How does it interact with reroll, account sanctions and pair restrictions?** It must not become a fourth state machine (D-031).
7. **Who reviews and appeals it?** Prompt 12.

### 11.8 Authorization required

**No owner approval is required for the design choice itself.** Under D-014, this is an ordinary design decision (Category B) and 08B records it. Owner approval would be required only if the choice created a **new account-level sanction** or a **legal/regulatory obligation**; D-018's prohibition and D-039's reroll rules already exist, and a diplomatic reputation must not be used as a covert ban. If 08B's option (b) would restrict account access, it must say so explicitly and treat that as a policy change requiring a superseding decision, not a quiet extension of UD-033.

### 11.9 Status

**UD-033 remains `Deferred to Prompt 08`.** 08A examined it, recorded the evidence and the options, and did **not** resolve it. The row's status is unchanged; a status note records that 08A has completed the research and that 08B must decide. Declaring it resolved because "Stellaris uses trust" or "P&W has no register" would violate the brief and the project's evidence discipline.

---
## 12. Stage 2 Prompts 01–07C integration matrix

### 12.1 How to read the matrix

Every applicable Stage 2 prompt from **01 to 07C** is represented. "Relationship" uses five values: **compatible** (no change needed), **dependency** (08B must consume the rule), **unresolved question** (a decision is still owed), **potential conflict** (a real tension recorded in §14), or **not applicable** (with a reason). No prompt is silently omitted.

### 12.2 The matrix

| Prompt / deliverable | Requirement, decision, constraint, formula or rule | Source path and ID | Current status | Relevance to Diplomacy | How 08A accounts for it | Relationship | Required follow-up |
|---|---|---|---|---|---|---|---|
| **01 — Bible frame** | B-08 is "Diplomacy": relationship types, treaties and lifecycle, negotiation, sanctions, diplomatic actions, breach and termination, consequences and reputation routing, 3–5 worked interactions | [`02_master_game_design_bible_outline.md`](../02_master_game_design_bible_outline.md) §B-08 | **Planned** | Defines the deliverable's content | Recorded as the canonical scope; 08A supplies research, not the rulebook | **Dependency** | 08B writes B-08; 08C adds workflows and acceptance |
| **01 — Bible frame** | B-08 validation: every diplomatic state is reachable, exitable and visible to both parties | Same, B-08 validation row | **Planned** | The acceptance bar for 08B/C | Recorded; §8.3 proposes a state list for 08B to test against | **Dependency** | 08B/08C |
| **01 — Requirements** | **REQ-012**: bilateral relationships are typed, event-sourced and visibility-scoped | [`03_requirements_traceability.md`](../03_requirements_traceability.md) REQ-012 | **Provisional** | The core diplomacy requirement | Traced in §2.4/§9; the state catalogue is still missing; §8 proposes a layered model | **Dependency / unresolved question** | 08B; status stays Provisional until design exists |
| **01 — Requirements** | **REQ-013**: alliances have explicit roles, audited pool draws and a succession rule before any pool exists | `03` REQ-013 | **Open** | Alliance, not diplomacy | Recorded as Prompt 09's; not designed here | **Not applicable to 08B** (Prompt 09) | 09 |
| **01 — Requirements** | **REQ-014**: strategic orders exist only with a war rule set, protection states and settlement enforcement | `03` REQ-014 | **Deferred** | War, not diplomacy | Recorded as Prompt 10's; 08B must not create a war rule | **Not applicable to 08B** (Prompt 10) | 10 |
| **01 — Requirements** | **REQ-015/016/018/019/020/021/027/057** (turn, idempotency, server authority, provenance, history, audit, visibility) | `03`; B-02 | Provisional/Approved as each row states | Every diplomatic action needs them | Listed in §9; §8.5 and §8.9 apply them | **Dependency** | 08B/08C |
| **01 — Unresolved** | **UD-013**: what does a treaty *do* beyond a non-aggression analogue? | [`05_unresolved_design_decisions.md`](../05_unresolved_design_decisions.md) UD-013 | **Deferred to Prompt 08** | The treaty-effect question | Analysed in §8.2; remains open; 08B must decide | **Unresolved question** | 08B |
| **01 — Unresolved** | **UD-033**: reputation account- or nation-scoped after reroll | `05` UD-033 | **Deferred to Prompt 08** | The reputation-scope question | Analysed in §11; remains open; 08B must decide | **Unresolved question** | 08B; Prompt 12 for procedure |
| **02 — B-02** | **TR-019**: posture is directional; Agreement is mutual and owned by Prompt 08; alliance membership 09; conflict 10 | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](../07_core_gameplay_loop_symbolic_world_and_turn_system.md) TR-019 | **Provisional** | The relationship-family framework | §8.1 adopts the three-layer reading; §14 DPX-02 records the symmetry tension | **Dependency** | 08B must not redefine TR-019 |
| **02 — B-02** | **TR-020 / D-030 / DD-048**: pending proposals visible to counterparty only; public on declaration/effect/publication | B-02 TR-020; DECISIONS D-030; DD-048 | **D-030 Confirmed**; TR-020 Provisional | The visibility rule for every proposal | §8.9/§9 apply it; DPX-01 records the "signed treaty public" ambiguity | **Dependency / potential conflict** | 08B states the exact publication moment; 13 displays |
| **02 — B-02** | **TR-021/TR-022**: one visibility class per field; k = 5; complementary suppression | B-02 §9; D-027 | Provisional/Confirmed | Treaty terms, history and aggregates | §9 lists it; §8.9 applies it | **Dependency** | 08B assigns a class per field; 12 audits |
| **02 — B-02** | **TR-006/TR-008**: feedback contract (cost, eligibility, state, timing, failure, digest) | B-02 §5–§6 | **Provisional** | Player-facing diplomacy | §8.9 adopts the requirement; DCR-10 | **Dependency** | 08C/13 |
| **02 — B-02** | Class Q/S timing; P0–P7; P2 re-validation; P4 application; reservation; `F` codes; idempotency; recovery | B-02 §13–§21, §24 | **Provisional** | Every cost-bearing or effect-bearing diplomatic action | §8.5 and §9 require 08B to declare phase/order; DCR-04 | **Dependency** | 08B declares the phase; 08C writes failure paths |
| **02 — B-02** | **TR-096**: Prompt 08 inherits relationship types, consent semantics, visibility, ordering edges and D-030; must return treaty effects, breach consequences, public-declaration timing | B-02 §25 TR-096 | **Provisional** | The formal handoff from 02 to 08 | §17 hands these back; §14 records gaps | **Dependency** | 08B returns them in B-08 |
| **03 — B-03** | A restricted pair cannot sign a treaty with each other | [`09_account_onboarding_nation_creation_and_progression.md`](../09_account_onboarding_nation_creation_and_progression.md) §5.5 row 15; §18 CON-001 | **Provisional** | Blocks diplomacy between restricted accounts | §9 lists it; §13/§14 require 08B to implement the block and its reason code | **Dependency** | 08B |
| **03 — B-03** | **RRL-019**: reroll terminates treaties; class-P event; replacement neutral; breach-reputation scope is Prompt 08's | B-03 §9.6 | **Provisional** | The reroll/diplomacy contract | §9 lists it; §11 analyses UD-033 against it | **Dependency / unresolved question** | 08B (scope); 12 (record use) |
| **03 — B-03** | **RRL-021**: reroll blocked during an active campaign, unsettled settlement, preservation hold or disqualifying state | B-03 §9.6 | **Provisional** | Prevents escaping a diplomatic commitment by reroll | §9 lists it; §8.10 notes the escape risk | **Dependency** | 08B must not create an unblocked escape; 10 owns the campaign block |
| **03 — B-03** | **D-031/D-032/D-034/D-035/D-039/D-042**: three state machines; one nation per account; pair states; no indirect routes; reroll; data classes | DECISIONS.md; B-03 | Confirmed/Provisional as each row states | Authority, eligibility, privacy | §9.1 lists them; §8.4 derives the authority rule | **Dependency** | 08B |
| **04 — B-04** | **ECN-212**: Prompt 08 may create aid, reparations, embargoes and sanctions; any movement is a transfer with matched ledger events; embargo does not destroy; sanction cannot create a negative balance; effects at P4; D-030 applies | [`10_economy_resources_treasury_and_finances.md`](../10_economy_resources_treasury_and_finances.md) §22 | **Provisional** | The economic interface for every diplomatic transfer | §8.6/§9 apply it; DCR-08 constrains sanctions | **Dependency** | 08B; 08C settlement paths |
| **04 — B-04** | **ECN-087**: no automatic food purchase; aid is a route | B-04 **§11** (ECN-087) | **Provisional** | Aid as a diplomatic action | §8.6 notes it; no new rule | **Dependency** | 08B if aid is adopted |
| **04 — B-04** | **ECN-092/DD-067**: one currency, one pool, no second currency; alliance pool separate | B-04 §12; D-049 | **Confirmed** (design) | No prestige/influence currency | §8.6 and §9.1 forbid a new currency | **Compatible / constraint** | 08B |
| **04 — B-04** | **D-055**: append-only ledger; corrections are new events | DECISIONS.md; B-04 | **Confirmed** (design) | Aid, reparations and any cost | §9.1; DCR-12 | **Dependency** | 08B/08C |
| **05 — B-05** | **URB-155**: a sanction may freeze a construction or research action; may not delete owned assets; aid moves crowns/resources, never capacity/DC/housing/RP | [`11_cities_infrastructure_production_and_research.md`](../11_cities_infrastructure_production_and_research.md) §23 | **Provisional** | Sanction scope in the city system | §8.8 and §9.2 apply it | **Dependency** | 08B if sanctions are adopted |
| **05 — B-05** | No direct diplomacy rule beyond URB-155; city capacity is not a diplomatic object | B-05 §23 | **Provisional** | None beyond aid/sanction | Recorded as not applicable beyond URB-155 | **Not applicable otherwise** | — |
| **06A — B-06 Part I** | **DMP-138**: a sanction may freeze a policy change but may not change a government, delete a policy or create a negative balance; aid moves crowns/resources, not approval/population; no diplomatic modifier without a named 08 term | [`12_population_and_domestic_politics.md`](../12_population_and_domestic_politics.md) §18 | **Provisional** | Sanction scope in politics; no prestige input | §8.8 and §9.2 apply it; DCR-07 forbids an unnamed modifier | **Dependency** | 08B |
| **06A — B-06 Part I** | Six governments, five channels, approval/stability/legitimacy, two policy axes | B-06 Part I; D-081…D-091 | **Provisional** | A diplomatic action may not silently move these | §8.6/§8.8 record the boundary | **Compatible / constraint** | 08B must name any term it wants; 06 does not provide one |
| **06B — B-06 Part II** | **DMP-263**: treaties persist through `TRANSITION`/`CRISIS`; diplomacy read-only while authority is suspended; a leadership change does not void a treaty | B-06 Part II; REQ-360/361 | **Provisional** | The political-state interface | §8.4/§9.2 apply it; DPX-05 records the read-only/expiry question | **Dependency / potential conflict** | 08B/08C |
| **06B — B-06 Part II** | **REQ-307**: trade, diplomacy and alliances receive explicit reroll and internal-politics contracts | `03` REQ-307 | **Provisional** | The contract requirement | §9.2/§12 record it | **Dependency** | 08B |
| **06B — B-06 Part II** | **REQ-387**: nothing is confiscated; treaties and alliance membership survive a crisis | `03` REQ-387 | **Provisional** | Treaty persistence | §9.2 | **Compatible** | 08B must not add confiscation |
| **07A — market research** | P&W trade surfaces, posted offers, public averages, account/network restrictions, player experience; 22 sources, 30 findings; **no rule approved** | [`research/07A_politics_and_war_market_research.md`](07A_politics_and_war_market_research.md) | Complete (v1.0) | P&W evidence base and methodology | §3.3 reuses its method; §5 sources are new (diplomacy-specific), not copied; §7 notes the restriction to P&W | **Compatible / evidence reuse** | 08B may reuse `PWR-016`…`PWR-019` for P&W restrictions |
| **07B — B-07** | **MKT-185**: a diplomacy/war restriction is separate; it may not be implemented as a market fee | [`13_trade_and_markets.md`](../13_trade_and_markets.md) **§21** (MKT-185) | **Approved constraint** (DMP-262) | The market/diplomacy boundary | §8.8/§9.2; DCR-08 | **Dependency / potential conflict** (DPX-04) | 08B defines any restriction in B-08; 08C records the interface |
| **07B — B-07** | **MKT-217/218/220**: one rule, one owner; the market reads a B-08 embargo and does not grow one; the political interface is one-way | B-07 §28 | **Provisional** | Ownership of an embargo | §8.8/§9.2; §14 DPX-04 | **Dependency** | 08B + 07 owner (documentation only) |
| **07B — B-07** | **D-016/D-017/D-109…D-121**: directed trades, no reservation at creation, parties-only terms, public listing rules, fair-value band, gates | DECISIONS.md; B-07 | Confirmed/Provisional as each row states | Any diplomacy–trade interaction | §9.1 records that none is reopened; §14 DPX-04 records the interface | **Compatible / constraint** | 08B must not change a `MKT-` rule |
| **07C — acceptance** | §6 Diplomacy row: "nothing at launch; no treaty, sanction or embargo rule exists" | [`14_market_workflows_and_acceptance.md`](../14_market_workflows_and_acceptance.md) §6 | Complete/accepted | Confirms the market has no diplomacy rule yet | §2.3 and §9.2 record it; §14 DPX-04 | **Dependency** | 08B adds the rule; 08C records the interface |
| **07C — acceptance** | §15.3/§15.5: 08 inherits the market; may not add a trade tax/tariff/embargo without a new decision; must add any restriction to B-08 and record the interface; must not release Global Trade | `14` §15 | Complete/accepted | The market's handoff to 08 | §9.2/§17.6 record it; §19 checks gates unchanged | **Dependency / constraint** | 08B/08C |
| **07C — acceptance** | 237/237-rule matrix; 83-test catalogue; G-1…G-6 evidence plan; G-1/G-2/G-3/G-5/G-6 not met, G-4 partial | `14` §10, §15 | Complete/accepted | Must remain unchanged | §9.3 and §19 confirm no gate changed | **Compatible / constraint** | No action; preserve |

### 12.3 Integration audit result

- **Coverage:** all ten applicable Stage 2 deliverables (01, 02, 03, 04, 05, 06A, 06B, 07A, 07B, 07C) are represented in **36 traceability rows**. No applicable prompt is omitted.
- **Compatible:** the majority of rows; the market, economy, politics and turn contracts do not need amendment to accommodate 08A.
- **Dependencies:** **19 rows** name a material dependency, concentrated in B-02's visibility/timing, B-03's reroll/pair rules, B-04's transfer contract, B-06's political states, and B-07's ownership boundary.
- **Potential conflicts:** six, recorded in §14 (`DPX-01`…`DPX-06`). None is a contradiction that invalidates prior work; each is an ambiguity or an interface that 08B/08C/09 must resolve explicitly.
- **Unresolved questions:** UD-013 and UD-033 remain open; `DQ-01`…`DQ-16` are research questions for 08B/08C/09.
- **Not applicable:** REQ-013/REQ-014 (alliance and war ownership), and B-05 beyond URB-155. They are marked, not ignored.

---
## 13. Diplomacy–Alliance interface and ownership matrix for Prompt 09

### 13.1 Boundary statement

**Prompt 09 owns the Alliance System and Alliance Management.** Its registered scope is: founding and organizing alliances; alliance constitutions; governance and management; leadership roles and ranks; internal alliance permissions; membership rules and operations (joining, leaving, removal); shared resources if permitted; alliance diplomacy; collective decisions; and the alliance operations framework ([`01_stage_2_prompt_roadmap.md`](../01_stage_2_prompt_roadmap.md) §Prompt 09; B-09 outline row).

**Prompt 08 owns Diplomacy between nations**: relationships, treaties, negotiation, sanctions, diplomatic actions and the cost of breaking commitments. **08A does not design any alliance rule.** The matrix below records only the **interface**: who owns each shared question, what state crosses the boundary, and what cannot be finalised until both designs exist.

### 13.2 Interface and ownership matrix

| # | Interaction or question | Authoritative owner | Existing evidence / requirement | State exchanged (if known) | Constraint the other system must respect | Unresolved decision or contract | Responsible prompt |
|---|---|---|---|---|---|---|---|
| **A-01** | A treaty between two **nations** that happen to be in alliances | **Diplomacy** | REQ-012; B-02 TR-019 (Agreement = Prompt 08) | Nation IDs, treaty ID, status | An alliance membership must not silently make the alliance a party | Does membership create any obligation for the alliance? **`DQ-11`** | 08B defines; 09 may add a membership consequence only by explicit contract |
| **A-02** | A treaty between two **alliances** | **Alliance System** (per B-09 "alliance diplomacy") | Roadmap Prompt 09; B-09 outline | Alliance IDs, treaty ID, status | 09 may reuse B-08's treaty object and lifecycle, but must not redefine a B-08 rule | Whether 09 reuses or extends the B-08 object; **`DQ-12`** | 09; 08B publishes the object contract |
| **A-03** | An alliance acting **on behalf of** a member (signing, accepting, terminating) | **Alliance System** for the delegation; **Diplomacy** for the treaty effect | B-06 has no cabinet delegation; 09 creates roles | Delegation scope, role ID, member nation ID | A delegated act must be re-validated against the nation's own eligibility (pair restriction, dormancy, transition) | Whether delegation exists at all; **`DQ-12`** | 09 defines; 08B states the validation it requires |
| **A-04** | A member **joins or leaves** an alliance during an active nation treaty | **Joint** — 09 owns membership; 08B owns the treaty's survival rule | EVE copies wars on membership change (`DPR-021`); RRL-019 ends treaties on reroll | Membership event, treaty IDs, timestamps | 08B must state whether the treaty persists, lapses or requires re-confirmation; 09 must emit the event | The persistence rule; **`DQ-11`** | 08B/09 coordinated; 08C tests it |
| **A-05** | A **restricted pair** in the same alliance, or treating with each other | **Account/Fair play** (B-03) for the restriction; **Diplomacy** for the treaty block | B-03 §5.5 row 15; D-035; D-052 | Pair state, nation IDs | 09 may not create an alliance route around the block; 08B must reject the treaty | None: the block is fixed; the reason code is 08B's | 08B implements; 09 respects |
| **A-06** | An **alliance-wide sanction or embargo** | **Joint** — 08B owns the sanction object; 09 owns who may authorize it | B-04 ECN-212; B-07 MKT-218; P&W's alliance government **cannot** force an embargo (`DPR-042`) | Sanction ID, scope, alliance ID, authorizing role | A collective sanction must have an explicit authority rule and must not bypass a pair restriction | Whether collective sanctions exist; **`DQ-13`** | 08B/09; 08C tests |
| **A-07** | **Visibility** of a treaty to alliance members | **Diplomacy** assigns the class; **Alliance System** displays it | B-02 TR-021; D-030 | Treaty ID, visibility class, alliance membership | 09 may not widen a private treaty's audience; 08B may not assume an alliance channel exists | Which fields are alliance-visible; **`DQ-13`** | 08B assigns; 09 renders |
| **A-08** | **Notifications** to an alliance about a member's treaty | **Diplomacy** emits the event; **Alliance System** distributes; **Prompt 13** renders | B-02 TR-008; D-030 | Event ID, recipient set | No third-party disclosure of pending terms | The recipient set; **`DQ-13`** | 08B/09/13 |
| **A-09** | A **war** involving an alliance or a member | **Warfare** (Prompt 10) owns the war; **Alliance System** owns the war-room; **Diplomacy** owns only a declaration/permission if one exists | D-023; roadmap Prompt 10 | War ID, side, member IDs | 08B must not define a campaign, a front or a peace term; 09 must not either | Whether a diplomatic declaration is a precondition; **`DQ-14`** | 10; 08B only if it adds a diplomatic permission. **Terminology superseded 2026-11-04 (Prompt 10B-C3):** the Alliance owns no war room; the war surface is B-10's nation-level, owner-only War Operations Board, and the Alliance surface is a restricted management interface with no military command and no member OP spending. The assignment of war ownership to Prompt 10 stands. |
| **A-10** | **Alliance reputation / standing** | **Alliance System** if it exists; **Diplomacy** owns nation reputation | UD-033; §11 | Account/nation/alliance IDs | 09 must not invent a parallel national reputation; 08B must not scope a nation register to an alliance | Whether alliance standing exists; **`DQ-13`** | 09; 08B for the nation side |
| **A-11** | **Shared pool** funding aid, reparations or a treaty cost | **Alliance System** owns the pool; **Economy** owns the ledger; **Diplomacy** owns the agreement | B-04 ECN-213; D-049/DD-067; D-035 | Pool ID, transfer ID, amount | A pool may not mint, bypass a pair restriction or act as a second currency | Whether a pool may fund diplomacy; **`DQ-15`** | 09; 08B states the transfer contract; 04 owns the ledger |
| **A-12** | **Reroll** while in an alliance and party to a treaty | **Account** (B-03) for the reroll; **Alliance System** for membership; **Diplomacy** for the treaty | B-03 RRL-019/RRL-021; UD-033 | Nation ID, alliance ID, treaty IDs | 09 ends membership and vacates roles; 08B terminates treaties; neither may transfer assets | The combined event order and record; **`DQ-11`** | 08B/09; 08C tests |

### 13.3 What Prompt 09 must eventually receive from B-08

- The **treaty object contract**: identity, parties (nation/alliance), lifecycle states, visibility classes, event classes and the effect interface.
- The **authority contract**: what a nation-level signatory must prove, and what a delegation would have to supply.
- The **membership-change rule**: whether a nation treaty survives a join/leave, and what event 09 must emit.
- The **pair-restriction contract**: the check 09 must call and the reason code it must surface.
- The **sanction contract**, if a collective sanction exists: who authorizes, what it may affect, and how it is recorded.
- The **visibility contract**: which treaty fields are alliance-visible and which remain parties-only.
- **Acceptance scenarios** to test after both designs exist (see §18.4).

### 13.4 What this report does **not** do

It does not define alliance founding, constitutions, leadership, ranks, internal permissions, membership admission/removal, voting, collective decision rules, shared-resource caps, alliance treasury, alliance war-room operations or alliance diplomacy. Those are Prompt 09's deliverables. No statement in this section may be read as a proposed alliance rule.

---

## 14. Other cross-system dependency and conflict inventory

### 14.1 Method

Each conflict is analysed in the six steps the 08A brief requires: (1) identify the source and the exact conflict; (2) decide whether it is real or hypothetical; (3) state the likely impact; (4) name the owner of the existing rule; (5) recommend a next action; (6) carry it into the correct prompt or register. A conflict is **not** resolved here by editing the earlier rule.

### 14.2 The conflict register

| ID | Source and exact conflict | Real or hypothetical? | Likely impact | Owner of the existing rule | Recommended next action | Carried to |
|---|---|---|---|---|---|---|
| **DPX-01** | **Public moment of a signed treaty.** B-02 **TR-021** lists "treaty texts once signed" as **public**. **D-030/TR-020** says third parties see nothing until **both parties declare it, it takes effect at a boundary, or a party publishes it**. If one party signs and the other has not, TR-021 appears to make the text public immediately; D-030 appears to keep it private until a later event. | **Real ambiguity**, not a direct contradiction. Both can be reconciled if "signed" means "both signatures complete", but no document says so. | A treaty could leak before the counterparty accepts, or a completed treaty could remain hidden when the rules say it is public. Either outcome damages trust and D-030's intent. | B-02 (TR-020/TR-021); D-030 | 08B defines the exact publication event: signature by **both** parties, or activation at a boundary, whichever it chooses; it states whether a one-sided signature is public. No earlier rule is edited. | **08B**; B-08 §visibility. 08C tests the pending/signed/active/public sequence. |
| **DPX-02** | **Symmetry of the relationship model.** B-02 **TR-019** makes **posture directional** and **Agreement mutual**. A candidate design that introduces a single mutual "relationship status" (for example "allied", "at war", "neutral") would overwrite the directional posture and lose the ability to represent "A is friendly, B is hostile". | **Potential conflict**, depending on 08B's design. The evidence (`DPR-013`) says directional posture plus mutual agreements is the common structure, so the conflict is avoidable. | If collapsed, the game cannot represent asymmetric attitudes; if kept, the UI needs two columns. | B-02 TR-019 | 08B keeps the two layers (DCR-01) or records why it departs from TR-019 and amends B-02 explicitly. | **08B**; B-08; §8.1 |
| **DPX-03** | **Reroll and reputation.** B-03 **RRL-019** says the replacement starts **neutral** with **no treaties**, and old acts stay attributed to the old nation. **UD-033 option (b)** would make a breach reputation **account-scoped**, so the new nation could inherit a consequence. That is not a contradiction if the consequence is an account-level **integrity record** rather than a nation-level diplomatic state, but no rule says which. | **Hypothetical until 08B chooses (b)**. Under (a) or (c) the rules are compatible. | If (b) is implemented as a nation-level penalty, it contradicts RRL-019's neutral restart; if it is hidden, it becomes an unappealable shadow ban. | B-03 (RRL-019, RRL-017); D-031 | 08B records the scope decision and states explicitly that the new nation's **public diplomatic standing** starts neutral; any account record is an integrity record owned by Prompt 12, not a nation status. | **08B**; §11; Prompt 12 procedure |
| **DPX-04** | **Diplomacy–market embargo ownership.** B-07 **MKT-185** says a diplomacy/war restriction is separate and "may not be implemented as a market fee". **MKT-218** says if B-08 adds an embargo, "the market reads it; it does not grow its own". **MKT-217** lists Prompt 08 as a future dependency with "a hook for a diplomatic restriction". The 07C companion §6 says "nothing at launch; no treaty, sanction or embargo rule exists". The conflict is not between rules; it is an **undefined interface**: no B-08 rule yet says what the market should read. | **Real interface gap**, not a contradiction. | If 08B defines an embargo without a market interface row, the market may duplicate it as a fee or ignore it; if 07 changes a `MKT-` rule to accommodate it, it breaks the 07C acceptance. | B-07 (market); 08B (diplomacy) | 08B adds the embargo/sanction rule to B-08 and records the exact interface in 08C; B-07 is **not** edited. If a `MKT-` rule must change, that is a separately justified correction with the 07 owner, not a side effect. | **08B/08C**; §9.2; §17.6 |
| **DPX-05** | **Read-only diplomacy during `TRANSITION`/`CRISIS` versus pending proposals.** B-06 **DMP-263** says the player may read treaties but may not sign, ratify, denounce or renegotiate while authority is suspended. It does not say what happens to a **proposal** that expires, or is accepted by the counterparty, during that window. | **Real edge case**, not a conflict. | A proposal could expire without the player being able to act; or the counterparty could accept while the proposer is in transition, creating a "signature" the player cannot make. | B-06 (DMP-263); B-02 (expiry/reservation) | 08B/08C define: proposals are frozen (not expired) during the read-only state, or they expire normally with a disclosed reason; acceptance during the counterparty's transition is rejected with a named code. | **08B/08C**; §17.3 |
| **DPX-06** | **Alliance treaty ownership.** The Stage 2 roadmap's Prompt 08 says "relationships, treaties, negotiation, sanctions..." without limiting treaties to nations. Prompt 09 says "alliance diplomacy" and its outputs include "alliance diplomacy". B-02 **TR-019** assigns "Agreement" to Prompt 08 and "Alliance membership" to Prompt 09, but does not assign an **alliance-to-alliance treaty**. | **Real ownership ambiguity.** | Both prompts could define a treaty object, producing two incompatible registers; or neither could define alliance-level treaties, leaving a gap. | Joint: Stage 2 register (scope) + B-02 TR-019 | 08B defines the **nation-level** treaty object and publishes it as a contract; 09 decides whether alliance-level treaties reuse it. The Stage 2 register records the split. Neither prompt silently overrides the other. | **08B + 09**; §13; §18 |

### 14.3 Conflicts considered and dismissed

| Candidate | Why it is not a conflict |
|---|---|
| B-04 ECN-212 authorises "aid, reparations, embargoes and sanctions" while no B-08 rule exists | It is an **authorisation envelope**, not a rule; 08B may use it or leave it unused. It does not require 08B to create all four. |
| D-023 keeps warfare out of the first playable while a NAP is a war-related treaty | A NAP can be a **permission block** on a war declaration that Prompt 10 will implement later; it does not require a war system to exist now. 08B must state that the block is inert until Prompt 10 exists. |
| B-03 RRL-019 terminates treaties on reroll while DMP-263 says a leadership change does not void a treaty | They apply to different events: a **reroll** retires the nation; a **leadership change** keeps it. Compatible. |
| B-07 D-017 makes trade terms parties-only while D-030 makes signed treaties public | They apply to different objects: a trade's terms vs a treaty's existence/text. A treaty may be public while its trade annex is private; 08B must say which is which. |
| D-027 k = 5 applies to diplomatic statistics | No diplomatic statistic is required; if one is added, the rule applies. Compatible. |
| Prompt 12 owns sanctions/appeals while Prompt 08 owns diplomatic consequences | B-03/D-018 assign **enforcement** to Prompt 12; 08B assigns **in-game diplomatic** consequences. They must not share a penalty record (D-031). |

---
## 15. Risks, evidence gaps and limitations

### 15.1 Design and integrity risks

| Risk | Evidence or reasoning | Likely impact | Evidence limitation | Design question for 08B/08C |
|---|---|---|---|---|
| **Treaty catalogue inflation** | P&W lists ten treaty types but enforces one (`DPR-001`); its community wiki needs eight statuses to describe player practice (`DPR-003`) | A rulebook full of labels with no effect; players cannot tell what a treaty does; testing burden grows | P&W's labels are social; no effect data | Which treaties exist, and which of them actually change a system's behaviour? (`DQ-02`) |
| **Status collapse** | Directional posture and mutual agreement are distinct in every comparator (`DPR-013`) | A single status cannot represent asymmetric attitudes or a signed-but-inactive treaty | No comparator uses one field | Does B-08 keep posture and agreement separate? (`DQ-01`, DPX-02) |
| **Reroll reputation laundering** | UD-033; RRL-019; `DPR-040` | A player can break a treaty and start clean; third parties lose trust in the record | No comparator has the same reroll model | Account, nation or mixed? (`DQ-08`) |
| **Proposal spam and cancellation churn** | Stellaris cooldowns (`DPR-020`); D-024 requires a limit | Notification fatigue; wasted attention; harassment | No frequency data | What visible limit applies? (`DQ-10`) |
| **Stale authorization** | `DPR-031`; B-06 transition/crisis; reroll; pair restriction | An action accepted under one authority resolves under another; contradictory outcomes | No comparator documents the case | Re-validate at acceptance and activation; what failure code? (`DQ-07`, `DQ-05`) |
| **Duplicate/reciprocal records** | P&W embargo list (`DPR-054`) | Two rows for one relationship; double penalties; confusing history | One interface observation | One object per pair+type, or an explicit reciprocal state? (DCR-03) |
| **Sanction as a trade fee in disguise** | MKT-185/218; 07C §15.5 | Breaks the market's accounting and ownership; a hidden tariff | None: the contract is explicit | If sanctions exist, which B-08 rule does the market read? (`DQ-09`, DPX-04) |
| **Sanction scope creep** | B-04/B-05/B-06 bound what a sanction may **not** do, not what it may do | A sanction could freeze the whole game or delete assets by accident | Project contracts only | List the permitted effects and the grandfathering rule (`DQ-09`) |
| **Protection/ceasefire farming** | P&W beige cycle (`DPR-053`) | A diplomatic act resets protection or clears a war; abuse of timing | Player glossary, not a rule | 08B must not create a reset; coordinate with Prompt 10 (`DQ-14`) |
| **Treaty as a transfer disguise** | CoW bought relations (`DPR-030`); D-035 | Value moves outside the ledger or around a pair restriction | Community evidence | Every transfer is a B-04 ledger event and passes the pair check (`DQ-09`) |
| **Off-platform negotiation** | P&W's "Embassy" is a Discord channel (`DPR-029`) | No auditable offer; scams; moderation burden; no record for a dispute | Official glossary | Does Nation Supremacy provide an in-game message/offer surface, or accept off-platform deals? (`DQ-05`) |
| **Alliance boundary ambiguity** | DPX-06 | Two treaty registers or a missing alliance-level rule | Roadmap scope only | 08B publishes the object; 09 decides reuse (`DQ-12`) |
| **Public/private leak** | DPX-01; D-030 | A pending treaty becomes public early, or a signed treaty stays hidden | Project rules only | Define the exact publication event (`DQ-05`, `DQ-16`) |
| **Read-only state deadlock** | DPX-05; DMP-263 | A proposal expires or is accepted while the player cannot act | Project rule only | Freeze or expire during transition/crisis (`DQ-05`) |
| **Complexity / comprehension** | Stellaris's many treaties and modifiers (`DPR-014`); P&W's social complexity (`DPR-001`) | New players cannot tell what a treaty obliges; support burden | No Nation Supremacy user research | Keep the first-playable set small and explain each effect (`DQ-02`, DCR-02) |

### 15.2 Evidence gaps

| Gap | What is missing | Why it matters | How it is handled |
|---|---|---|---|
| **No EQ/role research** | No data on how Nation Supremacy players understand treaties, deadlines or obligations | A design can be logically correct and unreadable | All UX statements are labelled analysis; Prompt 13 and CV/PXE validation must test them later |
| **No counterproposal evidence** | No comparator documents a formal counterproposal | 08B may add one; it must justify the complexity | `DQ-05`; B-07's revision model is the nearest precedent |
| **No proposal-expiry evidence** | No comparator documents an unanswered proposal lapsing | Expiry is a likely anti-spam device but is unevidenced | `DQ-06`; DCR-06 proposes a turn-based expiry as a candidate only |
| **No account/nation reputation comparator** | No game has Nation Supremacy's reroll model | UD-033 cannot be answered by analogy | §11; `DQ-08` |
| **No sanction-duration evidence for a 2-hour game** | eRepublik's 30 days and EVE's weekly bills belong to other cadences | A copied duration would be wrong | `DQ-09`; Prompt 14 tunes |
| **No frequency/prevalence data** | No survey, telemetry or playtest | Cannot claim an abuse is common | Risks are labelled documented vs hypothetical |
| **EU4/CK3/Victoria 3 unavailable** | The Paradox wikis returned a client challenge | Narrower evidence for truce-breaking and "aggressive expansion" reputation | Disclosed in §4.3; no claim made |
| **P&W creation flow unverified** | `DPS-001` says in-game mechanics; `DPS-005` says forum-published | Cannot describe P&W's proposal/accept flow | Recorded as a source conflict; no workflow claim |
| **No live play** | No account, no in-game action | Interface behaviour beyond public pages is unobserved | Disclosed in §3.5 |
| **No Nation Supremacy implementation** | No code, schema, endpoint or scheduler | No runtime, load or security test is possible | §19 reports documentation checks only |

### 15.3 Limitations of the comparative method

1. **Genre distance.** Stellaris is single-player; EVE is a sandbox MMO; eRepublik and P&W are browser games with different turn lengths; Call of War is session-based. A pattern that works in one may fail in a 2-hour, mapless, free-first browser game.
2. **Social vs mechanical.** P&W's diplomacy is largely social; its treaty labels are not effects. Treating them as mechanics would be a category error.
3. **Wiki reliability.** Publisher-hosted wikis are community-editable; community wikis may lag. Findings are labelled accordingly.
4. **No counterfactual.** The research cannot say what would have happened in a comparator under a different rule.
5. **Selection bias.** The comparators were chosen for relevance to Nation Supremacy's questions, not randomly; they over-represent games with formal treaty systems.

### 15.4 Risks to this document's own conclusions

- **Over-reading P&W.** Its treaty web is the most directly analogous artefact, but its lack of enforcement is a design choice, not a law. 08B may choose more enforcement.
- **Under-reading the market interface.** B-07's ownership rule is strict; a diplomacy rule that ignores it would create a second market rule. §14 DPX-04 is the guard.
- **Treating "no evidence" as "no feature".** The absence findings (no reputation register, no proposal expiry) are recorded as gaps, not as proof.
- **Assuming 08B will accept DCR-01…DCR-12.** They are candidates; the handoff in §17 says so explicitly.

---

## 16. Requirements and open-question traceability

### 16.1 Classification of the baseline

The table classifies every material entry in this report. "Source" is the authoritative file or the research ID.

| Class | Entries | Source |
|---|---|---|
| **Existing approved requirement** | REQ-015 (cadence), REQ-041 (mapless), REQ-043 (one account, policy), REQ-046 (one Bible entry point), REQ-047 (labels), REQ-513 (Global Trade scope) | [`03`](../03_requirements_traceability.md); AI_CONTEXT §2 |
| **Existing approved decision** | D-015, D-018, D-020, D-023, D-024, D-025, D-026, D-027, D-028, D-030, D-031, D-032, D-034, D-035, D-039, D-042, D-049, D-050, D-055, D-109…D-122 | [`DECISIONS.md`](../../DECISIONS.md) |
| **Documented project constraint** | Mapless world; 2-hour UTC turns; one account/one nation; free-first ₹0 target; Cloudflare + Supabase; no implementation in Stage 2 | AI_CONTEXT §2; D-008/D-012 |
| **Verified research finding** | `DPR-001`…`DPR-054` (with the label each carries) | §6; `DPS-001`…`DPS-019` |
| **Candidate recommendation** | `DCR-01`…`DCR-12` | §10 |
| **Open question** | UD-013, UD-033; `DQ-01`…`DQ-16` | [`05`](../05_unresolved_design_decisions.md); §16.2 |
| **Known dependency** | B-02 TR-019/020/021/022/096; B-03 §5.5/RRL-019/RRL-021; B-04 ECN-212; B-05 URB-155; B-06 DMP-138/DMP-263; B-07 MKT-185/217/218/220; 07C §15 | §9.2; §12 |
| **Conflict requiring resolution** | `DPX-01`…`DPX-06` | §14 |
| **Not applicable or outside the phase** | REQ-013 (alliance roles), REQ-014 (war orders), B-05 beyond URB-155, Prompt 09's constitution/governance, Prompt 10's campaigns | §12 |

### 16.2 Open questions `DQ-01`…`DQ-16`

These are **research questions for the owning prompt**, not decisions and not a second UD register. 08B should convert any that remain unresolved into `UD-` rows, using the existing register, rather than keeping a private list.

| ID | Exact question | Why it matters | Evidence collected | Options (only where established) | Consequences / trade-offs | Cross-system dependency | Owner | Authorization | Prompt |
|---|---|---|---|---|---|---|---|---|---|
| **DQ-01** | What relationship states exist, are they directional or mutual, and what transitions are allowed? | The core of REQ-012; every action depends on it | `DPR-006`, `DPR-008`, `DPR-013`; TR-019 | (a) directional posture + mutual agreements (b) one mutual status | (a) expresses asymmetry, needs two displays; (b) simpler, loses nuance | B-02 TR-019; B-13 | 08B | None (Category B) | 08B |
| **DQ-02** | Which treaty types exist, and which create an enforceable effect? | UD-013; determines the rulebook size | `DPR-001`, `DPR-003`, `DPR-019` | (a) NAP + two promises (b) full catalogue | (a) small, testable; (b) rich, label-heavy | War (10), trade (07), politics (06) | 08B | None | 08B |
| **DQ-03** | What counts as breach, and what consequence follows? | Without it, "reputation" has no event and treaties have no cost | `DPR-019`, `DPR-025` | (a) no enforced breach; social only (b) opinion/standing penalty (c) a hard lockout | (a) low complexity, weak deterrence; (b) visible, needs a register; (c) strong, punitive | UD-033; Prompt 12 | 08B | None; if it becomes an account sanction, a new decision is required | 08B/08C |
| **DQ-04** | Is any treaty allowed to drag a nation into war automatically? | A mutual-defence treaty needs Prompt 10's war rules | `DPR-004`, `DPR-021`; D-023 | (a) no automatic war-entry (b) only after Prompt 10 | (a) keeps 08 independent; (b) couples 08 to 10 | Prompt 10 | 08B + 10 | None | 08B, revisited after 10 |
| **DQ-05** | What is the full proposal lifecycle, including counterproposal, withdrawal, amendment and stale authorization? | 08C cannot write workflows without it | `DPR-015`…`DPR-024`, `DPR-031` | (a) offer/accept only (b) add counter/revision (c) add amendment | More states = more tests and UI | B-02 class Q/S; B-13 | 08B | None | 08B (design), 08C (workflows) |
| **DQ-06** | Does an unanswered proposal expire, and can it be withdrawn before activation? | Anti-spam; stale proposals block slots | `DPR-023`; no comparator evidence | (a) no expiry (b) turn-based expiry (c) expiry + cooldown | (a) simple, clutter; (b) needs a boundary job; (c) stronger, more state | B-02; D-024 | 08B | None | 08B |
| **DQ-07** | Who may propose, accept, reject, withdraw, amend and terminate, and when is authority re-checked? | The permission matrix; D-024 | `DPR-026`…`DPR-031`; D-032; DMP-263 | (a) nation owner only (b) delegated roles (09) | (a) simple, no ministers; (b) requires 09 | B-03; B-06; Prompt 09 | 08B (nation), 09 (alliance) | None | 08B/09 |
| **DQ-08** | Does a diplomatic reputation register exist; what is it; what is its scope after reroll? | **UD-033**; breach deterrence vs fairness | `DPR-033`…`DPR-040`; §11 | (a) nation (b) account (c) mixed | See §11.4 | B-03; D-031; Prompt 12 | 08B | None for design; a new account sanction needs a decision | 08B |
| **DQ-09** | Do sanctions exist; who can be sanctioned; what may they block; how long; what is grandfathered? | B-04/B-05/B-06 authorise the envelope but not the rule | `DPR-041`…`DPR-044` | (a) no sanctions (b) one time-boxed embargo (c) a broader sanction set | (a) smaller; (b) needs a market interface; (c) scope creep | B-04, B-05, B-06, B-07 | 08B | None | 08B/08C |
| **DQ-10** | What visible limit applies to diplomacy actions? | D-024 requires one | `DPR-020`; B-02 §24 | (a) per-pair open proposals (b) per-nation cap (c) cooldown | Caps can frustrate; no cap invites spam | B-02; Prompt 14 | 08B | None | 08B/14 |
| **DQ-11** | What happens to a nation's treaties when it joins or leaves an alliance, or rerolls? | Membership transitions are documented abuse surfaces | `DPR-021`; RRL-019; §13 | (a) persist (b) lapse (c) require re-confirmation | (a) simple, binds the alliance indirectly; (b) clean, disruptive; (c) explicit, more steps | B-03; Prompt 09 | 08B + 09 | None | 08B/09 |
| **DQ-12** | Do alliance-level treaties reuse the B-08 object, and can an alliance delegate authority to act for a member? | DPX-06; prevents two treaty registers | `DPR-002`; roadmap B-09 | (a) reuse the object (b) separate object | (a) one schema, one test suite; (b) duplication risk | Prompt 09 | 09 (with 08B's contract) | None | 09 |
| **DQ-13** | What may an alliance see or do with a member's diplomacy (visibility, notifications, collective sanctions, standing)? | D-030 and D-027 apply; 09 needs an interface | `DPR-045`…`DPR-050`; §13 | (a) public only (b) alliance-scoped view (c) collective action | (a) minimal; (b) useful, privacy risk; (c) powerful, needs an authority rule | Prompt 09; Prompt 13 | 09 + 08B | None | 09 |
| **DQ-14** | Is a diplomatic declaration a precondition for war, and can diplomacy stop a war? | War is Prompt 10's; 08B must not define a campaign | `DPR-021`; D-023 | (a) no precondition (b) a declaration record (c) a ceasefire permission | (a) simple; (b) creates an abuse surface (war-slot filling); (c) couples 08/10 | Prompt 10 | 10 (08B only if it adds a permission) | None | 10 |
| **DQ-15** | May an alliance pool fund aid, reparations or a treaty cost? | B-04 ECN-213 says a pool is separate and audited; B-03 says no bank use while restricted | ECN-213; D-035 | (a) no pool funding (b) capped, audited transfers | (a) simple; (b) needs 09 caps and 04 ledger rows | Prompts 04/09 | 09 + 04 | None | 09 |
| **DQ-16** | What data class and retention apply to proposals, signed treaties, breach records and private reasons? | D-026/D-042 require a class per record; history is permanent only for class P | D-026; D-042; `DPR-048` | (a) class P for signatures/terminations (b) class S for routine proposals | (a) auditable, more rows; (b) lighter, less history | Prompts 11/12/13 | 08B + 12 | None | 08B/12 |

### 16.3 Identifier discipline

- No `UD-` row was added. UD-013 and UD-033 remain the authoritative unresolved rows; 08B must decide them.
- No `REQ-` row was added. 08A is research; 08B adds requirements only when it writes rules.
- No `D-`/`DD-` row was added. 08A makes no design decision.
- `DPS-`, `DPR-`, `DPX-`, `DCR-` and `DQ-` are scoped to this report. They are not project decision identifiers and must not be cited as approvals.

---
## 17. Prompt 08B handoff

### 17.1 Requirements and decisions that must be preserved

08B must treat the following as **inputs it may not silently change**. If it cannot satisfy one, it must amend the owning document and record why.

1. **Fixed constraints:** fictional mapless world; 2-hour UTC cadence; one account/one nation; free-first ₹0 target; Cloudflare + Supabase; no Stage 2 implementation (AI_CONTEXT §2; D-008/D-012).
2. **D-030 pending-act visibility:** counterparty-only while open; public on declaration, effect or publication; private rejection/withdrawal. 08B implements it.
3. **B-02 TR-019:** posture is directional; Agreement is mutual and owned by 08; alliance membership 09; conflict 10.
4. **B-02 TR-021/TR-022 and D-027:** one visibility class per field; k = 5 aggregates; no leakage.
5. **D-024:** a visible limit for every diplomacy action; no general action currency.
6. **D-015:** Operations Points are military-only; no diplomacy cost in OP.
7. **D-049/DD-067 and D-050:** one currency; no debt; no second currency; no negative balance.
8. **B-03 §5.5/RRL-019/RRL-021 and D-031/D-032/D-034/D-035/D-039:** pair restriction, reroll termination, neutral restart, three state machines, indirect-route prohibition.
9. **B-04 ECN-212:** every transfer has matched ledger events; an embargo destroys nothing; a sanction cannot create a negative balance; effects at P4.
10. **B-05 URB-155 and B-06 DMP-138:** sanctions may freeze an action, not delete an asset or change a government; aid moves crowns/resources only.
11. **B-06 DMP-263:** treaties persist through `TRANSITION`/`CRISIS`; diplomacy is read-only while authority is suspended; a leadership change does not void a treaty.
12. **B-07 MKT-185/217/218/220 and 07C §15.3/§15.5:** the market owns its rules; diplomacy may add a restriction only as a B-08 rule that the market reads; no fee/tariff/tax; Global Trade remains gated.
13. **Prompt 09 ownership:** no alliance constitution, governance, roles, ranks, membership, pool, voting or operations in B-08.

### 17.2 The strongest relevant findings

1. **Separate the layers.** Relationship status, agreement and enforceable obligation are distinct in every comparator that has more than war/peace (`DPR-013`, `DPR-014`). This is the single most useful structural finding.
2. **Enforcement is selective.** P&W records ten treaty types and enforces only NAP (`DPR-001`); Stellaris enforces effects and charges an exit cost (`DPR-019`); eRepublik enforces MPP triggers and embargo blocks (`DPR-004`, `DPR-041`). 08B must choose **which** promises the game enforces, not assume all are.
3. **Time-boxing is normal.** 30-day treaties/embargoes (eRepublik), weekly war bills (EVE), 10-year cooldowns (Stellaris) (`DPR-015`, `DPR-020`, `DPR-021`). Durations are design choices, not constants to copy.
4. **Authority is explicit in the comparators that work.** eRepublik splits proposal and approval (`DPR-026`); EVE names CEO/director (`DPR-027`); P&W leaves it undocumented (`DPR-028`). The last is a warning, not a model.
5. **Reputation is not one object.** Trust vs opinion (Stellaris), player labels (EVE), no register (P&W, eRepublik) (`DPR-033`…`DPR-040`). A single global score is unsupported.
6. **Sanctions are usually a time-boxed act or a relation, not a treaty** (`DPR-041`…`DPR-044`). Their market effect is read from the diplomacy rule, not invented as a fee.
7. **Public outcomes, private negotiation.** P&W, EVE and eRepublik publish records, not the negotiation (`DPR-045`, `DPR-048`, `DPR-049`).
8. **Documented abuses concentrate on timing and slots:** war-slot filling, bank evasion, beige cycles (`DPR-051`…`DPR-053`); duplicate reciprocal records (`DPR-054`); stale authorization (`DPR-031`).
9. **No comparator documents proposal expiry or counterproposal** (`DPR-023`, `DPR-024`). If 08B adds them, it is innovating and must test them.
10. **No comparator answers UD-033** (`DPR-040`). It is a product decision.

### 17.3 Candidate approaches requiring deliberate design decisions

08B should decide each of these explicitly; the research does not decide them:

| Decision | Candidate options | What the evidence says | What 08B must record |
|---|---|---|---|
| Relationship model | (a) directional posture + mutual agreements (b) one mutual status | (a) is the common structure; (b) is simpler but loses asymmetry | The chosen model, the states, the transitions and the display |
| Treaty set | (a) NAP + promise + aid (b) a larger catalogue | P&W's large catalogue is mostly social; Stellaris's is mechanical | The list, each effect, and which system enforces it |
| Enforcement | (a) NAP only (b) NAP + aid delivery (c) more | P&W enforces one; Stellaris enforces several | The enforcement map and the failure path |
| Breach | (a) none (b) reputation/standing penalty (c) lockout | No comparator has a full breach engine; exit penalties are more common | The definition, the consequence and the record |
| Reputation | (a) none (b) nation (c) account (d) mixed | No comparator answers; UD-033 | The scope, the purpose, the visibility and the decay |
| Sanctions | (a) none (b) one embargo (c) a set | eRepublik/P&W have embargoes; Stellaris does not in the pages read | The object, eligibility, scope, duration, grandfathering |
| Proposal lifecycle | (a) offer/accept (b) + counter (c) + expiry (d) + amendment | Counter/expiry are unevidenced | The states, the deadlines and the failure codes |
| Limits | (a) per-pair open proposals (b) per-nation cap (c) cooldown | D-024 requires one; comparators use cooldowns | The limit, its visibility and its reset |
| Visibility | (a) D-030 as written (b) a narrower rule | D-030 is confirmed | The exact publication moment (DPX-01) |
| Alliance interface | (a) nation-only B-08 (b) shared object with 09 | Ownership is ambiguous (DPX-06) | The contract 09 will read |

### 17.4 Deliverable path and next steps

- **Recommended B-08 path: `docs/stage-2/15_diplomacy.md`.** The outline's `14_diplomacy.md` is unavailable because `14_` is the 07C companion. Under the serial-prefix rule, 08B claims the next free prefix at its start and updates the outline and Stage 2 register **together**. Prompt 09's planned `15_alliances.md` then shifts to `16_`, and later planned names shift by one; no already-written file is renamed.
- **08B must not create B-08 in this report's name.** This report is `research/08A_diplomacy_research.md`; it is evidence, not the rulebook.
- **08B's first actions:** read this report, D-030, B-02 §9/§13–§19/§24/§25, B-03 §5.5/§9.6/§18, B-04 §22, B-05 §23, B-06 Part II §41, B-07 §28 and 07C §6/§15; then decide UD-013 and UD-033; then write the rulebook.
- **08B's requirements:** add the `REQ-` rows its rules create (next free ID), a formula register if it has formulas (Prompt 14 owns values), and a decision entry for every settled design choice.

### 17.5 Relationship and treaty lifecycle questions

08B must answer:

1. Are relationships directional, mutual or both? (`DQ-01`)
2. Which treaty types exist, and what does each do? (`DQ-02`)
3. What is the exact state machine, including counter, withdrawal, amendment, renewal and expiry? (`DQ-05`)
4. Which boundary activates, expires or terminates a treaty? (B-02 class Q/S)
5. What happens to a proposal when a party enters `TRANSITION`/`CRISIS`, becomes dormant, or rerolls? (`DQ-05`, DPX-05)
6. Can a treaty be amended in place, or must it be replaced? (`DQ-05`)
7. What is the public/private timeline for a signed treaty? (DPX-01)
8. What is the conflict rule when two treaties imply contradictory actions? (eRepublik's friend-of-a-friend; `DPR-032`)

### 17.6 Permissions and abuse-prevention questions

1. Who may propose, accept, reject, withdraw, amend and terminate? (`DQ-07`)
2. Is authority re-checked at acceptance and activation? (`DPR-031`)
3. What is the visible limit per action? (`DQ-10`, D-024)
4. How are duplicate/reciprocal proposals and records prevented? (`DPR-054`)
5. How is a restricted pair blocked, and what reason code is shown? (B-03 §5.5)
6. Can a treaty be used to route value around the pair check? (D-035)
7. Can a diplomatic act be used to fill a war slot or reset protection? (`DPR-051`, `DPR-053`)
8. What happens when a counterparty is dormant or inactive? (D-028; `DQ-05`)
9. Is off-platform negotiation permitted, and what record does the game keep? (`DPR-029`)

### 17.7 Reputation and UD-033 status

- **UD-033 is not resolved.** Its exact question and options are in §11; 08B must decide.
- The evidence does not support a single global score (`DPR-040`).
- If 08B chooses a register, it must state: purpose, object (nation/account/mixed), events, formula or table, visibility, decay/expiry, and the reroll interaction.
- If 08B chooses no register, it must say so explicitly and record UD-033 as resolved by that decision; silence is not a resolution.
- Any account-level restriction beyond a record requires a new decision; it cannot be smuggled in as "reputation" (D-031, D-018).

### 17.8 Timing, expiration, visibility, history and notification questions

| Area | 08B must state | Existing rule |
|---|---|---|
| Timing | Phase and ordering band for proposal, acceptance, activation, expiry, termination | B-02 §13–§19, §24 |
| Expiration | Whether proposals expire; whether treaties expire; which boundary | `DQ-06`; B-02 TR-024…TR-031 |
| Visibility | Class per field; pending vs signed vs active vs terminated; public reason vs private terms | D-030; TR-021; DPX-01 |
| History | What is class P (permanent) vs class S; what is public; what is audited | D-026; D-042; `DQ-16` |
| Notifications | Which events notify whom; how duplicates are suppressed; how a deadline is warned | B-02 TR-008; `DCR-10` |
| Failure | Stable codes for expired, withdrawn, rejected, restricted, unauthorized, counterparty unavailable, stale | B-02 §17.4 |

### 17.9 Formula and accounting implications

08A does **not** invent a formula or a value. If 08B's rules need numbers, they belong in a **B-08 formula register** with the same discipline as B-04/B-05/B-06/B-07: variable, unit, rounding, timing, bounds and label. Likely candidates, listed only to show the shape:

- a treaty **duration/expiry** in turns (integer, boundary-aligned);
- a **proposal limit** per nation/pair (integer);
- a **cooldown** in turns (integer);
- a **breach penalty** (if any) as an integer modifier or a basis-point adjustment;
- a **reputation/standing** value with a bounded range and a decay rule (if adopted; EVE's diminishing-returns curve is one documented shape, `DPR-036`);
- an **aid/reparations transfer** amount (integer crowns/resources, B-04 ledger).

**Accounting:** any crown/resource movement is a B-04 transfer with matched ledger events (`ECN-212`); a treaty itself should not mint, burn or escrow value unless B-04 defines the row. Prompt 14 labels and tests every number; no value in 08B may be called balanced.

### 17.10 Interfaces requiring explicit cross-system contracts

08B must publish a contract table (like B-07 §28) covering at least:

| System | What B-08 needs | What B-08 returns |
|---|---|---|
| B-02 turn engine | Phases, class Q/S, reservation, idempotency, failure codes, visibility classes | Action types, phase/band, limits, event classes |
| B-03 account/nation | Ownership, pair check, reroll cleanup, dormancy, data classes | Treaty termination event, neutral restart, pair-block reason |
| B-04 economy | Transfer/ledger contract, no debt, one currency | Aid/reparation transfer intent, no mint/burn |
| B-05 cities/research | Sanction freeze semantics | Which action is blocked, with a reason code |
| B-06 politics | `TRANSITION`/`CRISIS` read-only, no approval modifier | Treaty persistence, read-only acknowledgement |
| B-07 market | The market reads a diplomacy restriction; no fee | The restriction object and its scope |
| Prompt 09 alliances | Nation vs alliance party, delegation, membership change | The treaty object, authority and visibility contract |
| Prompt 10 warfare | War declaration/peace permissions, if any | A permission/record, not a campaign |
| Prompt 11 chronicle | Public treaty/breach events | Event records and visibility |
| Prompt 12 fair play | Audit, appeals, account integrity record | Restricted data and review hooks |
| Prompt 13 interface | Screens, notifications, explanations | States, labels, deadlines, failure messages |
| Prompt 14 formulas | Values, units, rounding, timing | Formula list and labels |

### 17.11 Integration obligations inherited from Prompts 01–07C

08B inherits, at minimum:

- **From 01:** the B-08 purpose and validation; REQ-012; UD-013/UD-033.
- **From 02:** TR-019/020/021/022/096; class Q/S; P0–P7; P2 re-validation; reservation; `F` codes; recovery; the feedback contract.
- **From 03:** the pair block; reroll termination and neutral restart; reroll blocking; three state machines; data classes.
- **From 04:** the transfer/ledger contract; no debt; one currency; no automatic food purchase; `P4` effect timing.
- **From 05:** sanction freeze, not deletion; aid never moves capacity/DC/housing/RP.
- **From 06A/06B:** no approval/population modifier without a named term; treaties persist through transition/crisis; read-only diplomacy; a leadership change does not void a treaty.
- **From 07A:** the P&W evidence base and its limits; `PWR-016`…`PWR-019` for restrictions.
- **From 07B:** MKT-185/217/218/220; the no-fee/no-tariff rule; the two-system market; Global Trade gates.
- **From 07C:** §6's "nothing at launch"; §15.3/§15.5's handoff; the 237/237 acceptance and the unchanged gates.

### 17.12 Research limitations that could materially affect the design

1. No Nation Supremacy player research; usability claims are analysis.
2. No comparator with Nation Supremacy's reroll model; UD-033 is a product decision.
3. No evidence on proposal expiry or counterproposals; both would be innovations.
4. EU4/CK3/Victoria 3 unavailable; truce-breaking and "aggressive expansion" reputation are under-evidenced.
5. P&W's creation flow is unverified; its treaty web is an interface, not a workflow.
6. No live play in any comparator; no frequency data.
7. No implementation exists, so no formula, load or security claim can be tested.

### 17.13 What "08B done" should mean

08B is complete only when:

- every diplomatic state is reachable, exitable and visible to both parties (B-08 validation);
- every treaty type has a stated effect or an explicit "record only" label;
- every action has an authority rule and a visible limit (D-024);
- every effect names its owning system and resolution phase;
- UD-013 and UD-033 have recorded decisions (not necessarily "yes");
- the B-08 cross-system contract table exists;
- a formula register exists if any formula exists, with every value labelled provisional;
- the Prompt 09 interface is published;
- no market rule, gate or Global Trade status is changed;
- the continuity files and roadmap record 08B's actual outcome, not the whole of Prompt 08.

### 17.14 What 08B must not do

- Approve a rule by describing it as approved; only a `D-` entry does that.
- Copy a comparator's numbers or labels as if they were Nation Supremacy's.
- Design Prompt 09's alliance system or Prompt 10's war.
- Change a `MKT-`, `DMP-`, `ECN-` or `URB-` rule to make diplomacy easier.
- Claim that a research finding is a player-validation result.
- Mark Prompt 08 complete when only 08B is done.

---

## 18. Prompt 09 handoff for alliance-side dependencies

### 18.1 What Prompt 09 will need from the completed Diplomacy specification

Prompt 09 must read the completed B-08 and use it, not a summary, for:

1. **The treaty object contract** — identity, parties, states, visibility classes, event classes and the effect interface.
2. **The authority contract** — what a nation signatory proves; what a delegation would have to supply.
3. **The membership-change rule** — whether a nation treaty survives a join/leave, and which event 09 must emit.
4. **The pair-restriction contract** — the check 09 must call and the reason code it surfaces.
5. **The sanction contract**, if collective sanctions exist — who authorizes, what is affected and what is recorded.
6. **The visibility contract** — which fields are alliance-visible and which remain parties-only.
7. **The notification/event contract** — what 09 receives and what it may distribute.

### 18.2 Diplomacy requirements the Alliance System must respect

- **D-030:** a pending proposal's terms are visible only to its named counterparty; an alliance may not see a member's pending terms unless B-08 explicitly allows it.
- **D-027:** no alliance aggregate may expose a private treaty term or a small group.
- **B-03 §5.5/D-035:** an alliance may not be used to route around a pair restriction, including through its bank.
- **D-031:** an alliance role is not an account status or a nation status.
- **D-032:** a nation is owned by an account and is never re-parented; alliance membership does not transfer ownership.
- **B-03 RRL-019/RRL-021:** a reroll ends membership and vacates roles; it also terminates the nation's treaties.
- **B-06 DMP-263:** a treaty persists through a member's `TRANSITION`/`CRISIS`; the member cannot sign or denounce while authority is suspended.
- **D-024:** any alliance action that affects diplomacy needs a visible limit in the alliance rulebook, not a hidden one.
- **No new currency / no pool minting:** B-04 ECN-213 and D-049/DD-067.
- **No map:** DD-013.

### 18.3 Potential alliance-related diplomatic actions or agreements (interface only)

This is a list of **questions**, not proposed alliance mechanics:

1. An alliance-to-alliance non-aggression or consultation treaty.
2. An alliance guarantee or protectorate over a nation.
3. An alliance-wide embargo or sanction.
4. A collective recognition of a nation's status (for example, a public declaration).
5. A membership condition that requires or forbids certain treaties.
6. An alliance-level aid or reparations commitment funded by a shared pool.
7. A bloc or coalition record (P&W's "bloc", `DPS-005`).
8. A joint war declaration or a collective peace (Prompt 10's, not 08's).

Prompt 09 decides which of these exist, who authorizes them, how they are recorded and what they do. 08A does not design any of them.

### 18.4 Cross-system dependencies and questions

| Dependency | 09 needs from 08B | 08B needs from 09 | Joint decision | Prompt |
|---|---|---|---|---|
| Nation treaty vs alliance membership | Whether membership creates an obligation | The membership event and role model | Persistence on join/leave (`DQ-11`) | 08B/09 |
| Alliance-level treaty | The reusable object/lifecycle | Whether to reuse or create a separate object | Object ownership (`DQ-12`, DPX-06) | 09 |
| Delegated authority | The validation a delegated act must pass | The delegation scope and role | Whether delegation exists (`DQ-12`) | 09 |
| Collective sanction | The sanction object and effect list | Who authorizes and how | Whether it exists (`DQ-13`) | 08B/09 |
| Visibility | The class per treaty field | The alliance membership set | Alliance-visible fields (`DQ-13`) | 08B/09 |
| Notifications | The event and recipient set | The distribution channel | Recipient set (`DQ-13`) | 08B/09/13 |
| Pool funding | The transfer intent | The pool and caps | Whether a pool may fund diplomacy (`DQ-15`) | 09/04 |
| Reroll | Treaty termination | Membership end and role vacation | Event order (`DQ-11`) | 08B/09 |
| War | A declaration/permission, if any | The war-room and alliance side | Whether 08 has a war role (`DQ-14`) | 10 |

### 18.5 State, permission, visibility and event-record questions

Prompt 09 must answer, without contradicting B-08:

1. Does an alliance have a **state** that is separate from its members' states? (D-031's discipline suggests a separate object, not a fourth status on the nation.)
2. Can an alliance **act** for a member, and if so, what is the scope and the revocation rule?
3. Can an alliance **see** a member's treaties, and which fields?
4. Can an alliance **require** a member to terminate a treaty, and what happens if the member refuses?
5. What **event** does 09 emit when a member joins, leaves, is removed, or rerolls?
6. What **record** does 09 keep of a collective decision, and for how long (D-026/D-042)?
7. How does 09 prevent a restricted pair from using the alliance as a route (D-035)?
8. How does 09 avoid creating a second reputation register (UD-033/§11)?
9. How does 09 handle a member in `TRANSITION`/`CRISIS` (DMP-263)?
10. How does 09 handle a dormant member (D-028)?

### 18.6 Conflicting or ambiguous ownership requiring a coordinated decision

- **DPX-06:** alliance-to-alliance treaties are claimed by neither B-08 nor B-09 explicitly. 08B should publish the object; 09 should decide reuse. The Stage 2 register should record the split.
- **A-06/DQ-13:** a collective sanction is a diplomacy object with an alliance authorizer. Neither prompt can define it alone.
- **A-11/DQ-15:** a shared pool funding diplomacy crosses 04/08/09. The ledger row is 04's, the agreement is 08's, the authorization is 09's.
- **A-09/DQ-14:** a war involving an alliance crosses 08/09/10. 10 owns the war; 08 may own a declaration permission; 09 owns the war-room. The three must not each define "declaration".

### 18.7 Acceptance scenarios to check after both designs exist

These are **cross-system scenarios**, not executed tests:

1. A nation in an alliance signs a NAP with another nation; the alliance is not a party; the alliance sees only what B-08 permits.
2. The nation leaves the alliance mid-treaty; the treaty's fate matches B-08's rule; the alliance receives the correct event.
3. A restricted pair in the same alliance attempts a treaty; the attempt is blocked with the B-03 reason code; no bank route is possible.
4. A member rerolls while party to a treaty; membership ends, roles are vacated, the treaty terminates, the replacement is neutral, and the record is attributed to the old nation.
5. An alliance signs an alliance-level treaty; the object, lifecycle and visibility match the contract 09 chose.
6. A collective sanction is proposed; the authorizing role, the affected members and the market effect are all recorded and visible as B-08/09 specify.
7. A member in `TRANSITION` cannot sign or denounce; the treaty persists; no proposal silently expires without a disclosed reason.
8. A dormant member's treaty remains readable; no new offensive action is initiated; the alliance's view shows the dormancy.
9. An alliance pool funds aid; the ledger has matched events; no mint, no negative balance, no pair-route.
10. A public treaty record exposes no private term; a k = 5 aggregate hides a small group.

### 18.8 What this handoff does not do

It does not define the alliance constitution, founding, leadership, ranks, internal permissions, membership admission/removal, voting, collective decision rules, shared-resource caps, alliance treasury, war-room operations or alliance diplomacy. Prompt 09 remains the sole owner of those deliverables.

---
## 19. Completion checklist and actual validation results

### 19.1 Acceptance criteria — this report's own assessment

Each criterion is checked against the artefact that satisfies it. "Met" means the artefact exists in this report or in a named project file; it does not mean a game rule exists.

| # | Criterion | Evidence | Verdict |
|---|---|---|---|
| 1 | Existing project documentation and approved requirements inspected | §2.2–§2.3 inventory; every path verified on disk | **Met** |
| 2 | Diplomacy-related decisions and constraints traced | §2.4 baseline table; §9.1 approved/confirmed; §9.2 provisional contracts | **Met** |
| 3 | UD-033 examined using its actual registered definition | §11.1 quotes the row verbatim; §11.3–§11.9 analyse it | **Met** |
| 4 | Comparative research with traceable, credible sources | §4 comparator justification; §5 register, 19 sources with URLs and access dates; §6 findings | **Met**, with the access limitations disclosed in §4.3 and §15.2 |
| 5 | Source claims, findings and limitations recorded honestly | §3.4 evidence labels; §5 source conflicts; §15 risks and gaps | **Met** |
| 6 | Comparison matrix and requirements baseline complete | §7 comparative matrix; §16 classification and `DQ-01`…`DQ-16` | **Met** |
| 7 | Every applicable Stage 2 prompt from 01 to 07C considered | §12: 36 rows covering 01, 02, 03, 04, 05, 06A, 06B, 07A, 07B and 07C; none omitted | **Met** |
| 8 | Material dependencies and actual or potential conflicts documented with ownership | §12.2 (19 dependency rows); §14.2 (`DPX-01`…`DPX-06`, each with owner and next action) | **Met** |
| 9 | Prompt 09's Alliance System ownership explicitly respected | §13.1, §13.4, §18.8 | **Met** |
| 10 | Diplomacy–Alliance interface documented without duplicating the Alliance System | §13.2 (`A-01`…`A-12`); §18 | **Met** |
| 11 | Global Trade's mandatory scope and existing market gates preserved | §1.3, §9.3; no `MKT-`, `F-TM-` or gate row was edited | **Met** |
| 12 | Candidate recommendations not recorded as approved mechanics | §10 header; every `DCR-` is labelled candidate; §17.13 repeats it | **Met** |
| 13 | Prompt 08B and Prompt 09 have clear handoffs | §17 (08B); §18 (09) | **Met** |
| 14 | Research document exists and is properly indexed | This file; indexed in [AI_CONTEXT §5](../../AI_CONTEXT.md), the [Stage 2 register](../01_stage_2_prompt_roadmap.md) row 08, the [outline](../02_master_game_design_bible_outline.md) B-08 row and the [progress log §24](../06_stage_2_progress_log.md) | **Met** |
| 15 | Roadmap, progress, context, decision/requirement registers and handoff updated | §19.3 list | **Met** |
| 16 | Active next-action statements consistent with the authoritative roadmap | `validate_final.py`, `test_next_action.py` and `09_validate.py` stale-next-action and sub-prompt guards pass; `verify_politics_numbers.py`'s progress-status guard passes | **Met** |
| 17 | No implementation performed | §1.3; no code, schema, migration, endpoint, screen, scheduler or deployment change; `git status` shows documentation and QA-script changes only | **Met** |
| 18 | Applicable validators run and actual results reported | §19.2, with exact commands and outcomes | **Met** |
| 19 | Final changed-file list accurate | §19.3 | **Met** |

**Verdict: PASS at the research and documentation level.** The limitations in §15 remain: no player research, no live play in any comparator, three intended comparators inaccessible, and no runtime, load or security evidence — because no implementation exists. This verdict is **not** a claim that diplomacy is designed, implemented, tested or release-ready. Prompt 08B and 08C remain outstanding, and UD-013 and UD-033 remain open.

### 19.2 Validation actually run on 2026-10-29

The Python validators were run from `docs/qa_backups`; the link and URL checks were run from `docs/stage-2/research`. These are **documentation and arithmetic checks**; no server, database, browser or game runtime was started.

| Command | Actual result |
|---|---|
| `python3 validate_final.py` | **VALIDATION: ALL CHECKS PASSED** (exit 0) |
| `python3 validate_final.py --self-test` | **6/6 guards detect their defect** |
| `python3 test_next_action.py` | **23 tests, OK** |
| `python3 test_decision_registers.py` | **12 tests, OK** |
| `python3 09_validate.py` | **346/346 checks passed — ALL CHECKS PASSED** |
| `python3 verify_politics_numbers.py` | **879/879 checks passed** |
| `python3 verify_politics_numbers.py --self-test` | **18/18 guards detect their defect; 879/879 document checks passed** |
| `python3 verify_market_workflows.py` | **14 document checks, 0 failed; B-07 237 unique rules; matrix 237 rows; 83-test catalogue; ALL CHECKS PASSED** |
| `python3 verify_market_workflows.py --self-test` | **8/8 guards detect their defect** |
| `python3 verify_market_numbers.py` | **ALL CHECKS PASSED** |
| `python3 verify_market_numbers.py --self-test` | **14/14 guards detect their defect** |
| `python3 verify_economy_numbers.py` | **164/164** |
| `python3 verify_city_numbers.py` | **267/267** |
| Relative-link resolution over this report (inline script, 2026-10-29) | **49 relative links checked, 0 missing** |
| `curl -L -s -o /dev/null -w "%{http_code}"` against the 19 registered URLs (inline script) | **19 attempted, all returned `000`** — the shell has no network egress in this environment, so this check produces **no accessibility evidence**. Accessibility rests on the successful reads through the research tool on 2026-10-29; one attempt during research (`https://politicsandwar.com/embargoes/`) returned **404**, and the working pages actually used are the ones registered (`/world/embargoes/` and the community wiki) |

**Validators were advanced to the split-Prompt-08 state**, because several checks still asserted the pre-08A status. No check was removed and no assertion was weakened; each change is listed so it can be audited:

1. `status_rules.py` — `COMPLETED_SUBPROMPTS` now includes `08A`, and the sub-prompt pattern accepts `0[78][A-C]`, so a sentence calling **08A** the next task is caught exactly as 07B/07C were. A new self-test fixture in `validate_final.py` proves it (6/6).
2. `test_next_action.py` — the progress-table check now requires one row to name the next **sub-prompt** (`08B`) instead of the literal string "Next task"; a new test asserts that 08A is caught as next and that "08A complete; 08B next" is accepted (23 tests). The real-continuity test now asserts `08A` and `08B` in each current-status file.
3. `test_decision_registers.py` — row 08 must read `**08A complete**` and `**08B next**`, and the test still forbids "Prompt 08 is complete" and "Prompt 08B is complete".
4. `validate_final.py` — the progress-log pending count is **7** (Prompts 09–15) instead of 8, and row 08 must record 08A complete/08B next; the `stage-2/00 §10` check requires **Prompt 08B**; the continuity check requires **08A** and **08B**; the roadmap check requires "Prompt 08A complete" and `08B`; this report is added to the required-document list.
5. `09_validate.py` — pending count 7 and a row-08 assertion.
6. `verify_politics_numbers.py` — the progress-status guard reads the 08A/08B row instead of requiring "Pending".

The counts that changed (8 → 7 pending; 345 → 346 checks; 5 → 6 self-test fixtures) track the split, not a relaxed standard. `verify_market_workflows.py`, `verify_market_numbers.py`, `verify_economy_numbers.py`, `verify_city_numbers.py` and every `MKT-`, `F-TM-` and gate assertion pass **unchanged**.

### 19.3 Files created and updated by 08A

**Created**

- [`docs/stage-2/research/08A_diplomacy_research.md`](08A_diplomacy_research.md) — this report.

**Updated** (each change serves 08A; nothing else was edited by this pass)

| Path | Reason |
|---|---|
| [`docs/ROADMAP.md`](../../ROADMAP.md) | Records Prompt 08A complete, 08B next, 08C not started; keeps Stage 2 in progress and does not advance to Prompt 09 |
| [`docs/PROJECT_PROGRESS.md`](../../PROJECT_PROGRESS.md) | Header, STATUS block (`diplomacy:` line), Stage 2 table row 08 and the continuity paragraph record the 08A outcome, the research path, the open questions and the next authorised task |
| [`docs/AI_CONTEXT.md`](../../AI_CONTEXT.md) | Header, STATUS block, stage-plan line, document index (new 08A row; rows 00/06 updated) and a new §7 risk bullet record 08A and the B-08 gap |
| [`docs/AI_HANDOFF.md`](../../AI_HANDOFF.md) | New §0.2 with the 08A findings, integration audit, UD-033 status, Prompt 09 boundary and validation; §H opening and §H.6 rewritten; instruction 14 advanced |
| [`docs/stage-2/00_stage_2_handoff.md`](../00_stage_2_handoff.md) | §10 next action becomes Prompt 08B with the 08A result and the filename constraint |
| [`docs/stage-2/01_stage_2_prompt_roadmap.md`](../01_stage_2_prompt_roadmap.md) | Registers 08A/08B/08C under parent Prompt 08; row 08 and the Prompt 08 block record the 08A result; new filename note resolves the `14_` collision |
| [`docs/stage-2/02_master_game_design_bible_outline.md`](../02_master_game_design_bible_outline.md) | B-08 row links the research, records that no rule exists and that 08B confirms the next prefix; §5 current state updated |
| [`docs/stage-2/03_requirements_traceability.md`](../03_requirements_traceability.md) | Version header records that 08A adds no requirement and identifies what REQ-012 still lacks; counts unchanged |
| [`docs/stage-2/05_unresolved_design_decisions.md`](../05_unresolved_design_decisions.md) | UD-013 and UD-033 rows gain the 08A evidence and the explicit "08B decides" statement; both stay deferred and open; no row added or resolved |
| [`docs/stage-2/06_stage_2_progress_log.md`](../06_stage_2_progress_log.md) | Header, prompt table row 08 and new **§24** checkpoint with the objective, findings, integration audit, boundary, validation and next action |
| [`docs/qa_backups/status_rules.py`](../../qa_backups/status_rules.py) | Accepts 08A in the completed sub-prompt set and `0[78][A-C]` identifiers |
| [`docs/qa_backups/test_next_action.py`](../../qa_backups/test_next_action.py) | Split-Prompt-08 regression test; row-08 and real-continuity assertions |
| [`docs/qa_backups/test_decision_registers.py`](../../qa_backups/test_decision_registers.py) | Row 08 must record 08A complete/08B next and must not call Prompt 08 complete |
| [`docs/qa_backups/validate_final.py`](../../qa_backups/validate_final.py) | 08A/08B continuity, §10, roadmap and progress-log checks; pending count 7; new self-test fixture; report added to required documents |
| [`docs/qa_backups/09_validate.py`](../../qa_backups/09_validate.py) | Pending count 7; row-08 assertion |
| [`docs/qa_backups/verify_politics_numbers.py`](../../qa_backups/verify_politics_numbers.py) | Progress-status guard reads the 08A/08B row |

### 19.4 Files intentionally not changed

| File | Why it was left alone |
|---|---|
| [`docs/DECISIONS.md`](../../DECISIONS.md) | 08A makes no design decision. No `D-` entry was required, and adding one would falsely promote research into approval |
| [`docs/stage-2/04_approved_and_provisional_decisions.md`](../04_approved_and_provisional_decisions.md) | Same reason: no D/DD row exists for 08A |
| B-02, B-03, B-04, B-05, B-06, B-07 and their formula registers | Owned by earlier prompts; 08A found no defect that justified an edit. The `DPX-` conflicts are recorded here, not patched into their sources |
| [`docs/stage-2/14_market_workflows_and_acceptance.md`](../14_market_workflows_and_acceptance.md) | 07C is complete and accepted; its §6 and §15 were used as inputs, not edited |
| `MKT-`, `F-TM-`, `ECN-`, `URB-`, `DMP-`, `TR-` rules | Prior approved/provisional work; no rule was reopened. Global Trade (D-122/DD-136/REQ-513) and G-1…G-6 are unchanged |
| `docs/stage-2/08_final_decision_closure_audit.md` | A historical audit record, not a live register |
| `docs/stage-1/*` | Stage 1 is closed (D-011) and was not reopened |
| Application code, migrations, prototypes | 08A authorised no implementation; none exists to change |

### 19.5 What this validation does not establish

- It does not establish that any diplomacy rule is correct, complete, balanced, secure or implementable — there are no rules yet.
- It does not verify a source's *current* content beyond 2026-10-29. Game wikis change; §5 records versions where they were stated.
- It does not test player comprehension, notification behaviour, race conditions or load. Those need 08C's acceptance work and, later, an implementation.
- `git status` in this checkout also lists unrelated pre-existing modifications and untracked files from earlier sessions, so the §19.3 list — not `git status` — is the authoritative record of this pass's edits.

---
