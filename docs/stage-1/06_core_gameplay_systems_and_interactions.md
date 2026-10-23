# Stage 1, Prompt 6 — Core Gameplay Systems, Mechanics, and Interaction Framework

**Report:** v1.1 · 2026-10-22 · author: Prompt 6 session (v1.0 same day; v1.1 correction and consistency pass — system/tier counts reconciled, OP-status wording corrected, section numbering repaired to 1–27, wording repairs; no research or substantive recommendations changed)
**Scope:** High-level gameplay architecture for Project X — which systems the game needs, what each is for, which decisions it creates, how systems interact over the shared two-hour turn cycle, what is essential/optional/simplified/deferred, and which questions must be answered before anything can be specified in detail. This is NOT a game design document: no formulas, values, interfaces, or final rules. Every recommendation is **provisional** until a design stage records an approval in [DECISIONS.md](../DECISIONS.md).
**Prerequisites verified this session:** all four continuity files read; Prompt 5 report read in full *after* its 2026-10-22 correction pass (cadence wording fixed to "one shared turn every two hours / 12 per day"; concept count fixed to five CX-1…CX-5; validation references reconciled to Prompt 4's real V-1…V-10 register). DECISIONS.md holds D-001…D-006; no new entries added by this prompt.

---

## Section 1 — Executive summary

Project X's gameplay architecture (recommended framework, **provisional**) is a small system set organized around **one decision loop on the shared world clock**. The core proposal:

1. **A single national economy.** One currency, one treasury, a small set of national **development lines** (improvable capability families) with upkeep drains — replacing the genre's default of many buildings, many resources, and many menus (SYS-001…SYS-004).
2. **Structural interdependence instead of geography.** Specialization is chosen as *emphasis among lines*, trading efficiency against autonomy; missing capabilities must be sourced from other nations through **directed trades first, a listings market later** (SYS-005; FO-013/FO-009; CCR-008's staged-economy trade-off).
3. **A legible polity, not an institution sim.** Domestic governance = a light policy-lever layer (FO-005) whose main structural role is *stability as an enabler for every other path* — never a mandatory second game (SYS-006).
4. **Research as a convertibility engine.** A few national programs that turn economy into capability options — a modifier, not a success ladder (SYS-007; consistent with DIR-3).
5. **The relationship network is the interaction surface.** Bilateral relationship records, a minimal set of typed treaties with selective mechanical gates, reputation *affected by acts*, alliances as valuable-but-optional structures, and the world chronicle as shared memory (SYS-008…SYS-010, SYS-013, SYS-015).
6. **Bounded, settlement-terminated conflict.** A belt-tightened military capability, staged campaigns, and a declared end-condition vocabulary — adversarially pre-designed, attendance-tolerant (SYS-011/SYS-012; FO-010/011/017 as inputs; D-004's OP stays provisional and *undecided* here by design — §15G evaluates alternatives without approving one).
7. **The turn engine and its reporting as first-class systems.** The 2-hour shared turn (12/day, UTC boundaries), a three-class action-timing contract (immediate / queued / at-boundary), a provenance-complete digest, and re-entry summaries are systems with budgets and failure modes, not UI afterthoughts (SYS-016/SYS-017; FO-002/FO-015).

**Loops.** Four loops (per-turn, arc-scale, multiplayer, return-after-absence) are defined in Section 4 and deliberately share the *same* information surfaces — short sessions and long sessions read the same digest (PR-2/PXO-005).

**Prioritization.** Tier A: 5 build units covering 6 system IDs (foundation); Tier B: 5 systems (multiplayer gravity); Tier C: 7 expansion entries (staged in); Tier D: excluded areas (elections/congress, contracts/escrow, consumer-demand sim, espionage, seasonality/events, meta-progression, plus the constraint-rejected rounds/resets, geographic map, live-timed windows, and pay-gated late-game features). But note: those Tier-D areas were never catalog IDs — the catalog itself carries **18 systems, SYS-001…018**, reached by excluding four candidate areas (cities/districts, population, notifications, multi-currency storage), not by merging retained systems.

**What must be answered later (and is NOT answered here):** no economic rates, no war formulas, no treaty text, no ranking algorithm, no catch-up philosophy (FO-018), no alliance permission set, no market fee policy. 18 system-dependency questions (SDQ-001…SDQ-018) and 8 mechanics-level opportunities (MO-001…MO-008) are registered to route future design work.

Nothing in this report is approved. It extends the *provisional* CX-5 concept; if validation (CV-001…CV-006) refutes the concept, this framework inherits the refutation.

---

## Section 2 — Scope, method, and evidence limitations

**Method.** This is a synthesis-and-architecture task. It read the four prior stage reports (in relevant sections, with Prompt 5 in full plus its correction-pass state verified through PROJECT_PROGRESS.md), extracted the material design inputs (findings F-x, opportunities O-x/FO-x/PXO-x, constraints §2, pillars DP/UXD/AP, risks CCR, validations CV/V), and proposes an integrated framework with explicit tiering, interaction mapping, simplification analysis, and dependency registers. No new external web research was performed; every external-fact claim traces to a prior report's source register. New internal-only ID families are introduced (SYS-xxx, INT-xxx, SDQ-xxx, MO-xxx) and follow the project's claim-label discipline.

**What this report can legitimately establish:** conceptual completeness (no critical system missing), system purposes, dependency structure, feasibility posture under free-first constraints, simplification alternatives, and the open-question map.
**What it cannot establish:** player demand for specific mechanics, balance, write-budget viability, market integrity sufficiency, or war design correctness. Those belong to later dedicated stages and to the validation plan (Prompt 5 Section 17; Prompt 4 Section 19).

**Inherited evidence limitations (restated because they constrain this report):**
- The primary audience is a *well-evidenced hypothesis*, not a measured population [P#4]. If CV-001/CV-003 fail, the Tier-A/B assignments below need re-evaluation.
- The mapless world has no market precedent; every "the network can replace geography" claim is composition reasoning [AI-], to be checked by CV-002 before interface design locks.
- F-015 (politics demand) is weak-to-moderate single-thread evidence [P#2]; the politics layer is deliberately minimal here.
- No write-budget math exists yet (D-005/CCR-010); every "cheap to maintain" claim in this report is posture, not arithmetic.

---

## Section 3 — Project context and prerequisite report synthesis

### 3A. What the prior reports fix for this task

| Input | Where | Fix applied in this report |
|---|---|---|
| Confirmed constraints (browser, 2h shared turn/12 per day, persistent no-resets, fictional mapless, free-first, original identity) | [AI_CONTEXT.md](../AI_CONTEXT.md) §2 | Non-negotiable frame; the framework is built *inside* them, and any system that would require live windows, resets, maps, or heavy content ops was a priori disqualified (Section 21) |
| The recommended concept CX-5 and its pillars DP-001…006 / anti-pillars AP-001…008 | [05_core_game_concept_and_design_pillars.md](05_core_game_concept_and_design_pillars.md) §7–8, §14 | Every system's status is checked against the pillar/anti-pillar list (columns in Section 21's register); DP-002 and AP-001/003/004/005 in particular shape the prioritization |
| Prompt 3's FO register (FO-001…027, statuses: 8 Group-A candidates, FO-018/019 Needs Research, FO-020…023 Deferred, FO-024…027 Rejected) | [03_feature_comparison_opportunity_analysis.md](03_feature_comparison_opportunity_analysis.md) §10 | The candidate systems' evidence backbone; no FO status was upgraded — Tier placement reflects Group-A membership and Prompt 3's complexity/dependency assessments |
| Prompt 4's experience layer (PXO-001…005 P0 items; PXE risks; PR-1…10; V-1…V-10 all open) | [04_target_audience_and_player_experience.md](04_target_audience_and_player_experience.md) | The turn-digest/onboarding/serialization systems are specified to serve PXO-001…005; none of V-1…V-10 is treated as answered |
| Prompt 5's first-playable boundary (E1–E6 essential, S1–S5 simulated, O1–O6 out of scope) and risks CCR-001…012 | Prompt 5 §15–16 | Section 24's recommended framework stages land on the same boundary; the E1–E6 list is honored, not expanded |
| Decision-log discipline (D-003/D-006: findings are inputs; nothing approves itself) | [DECISIONS.md](../DECISIONS.md) | This report creates zero decisions; OP (D-004) remains unapproved and is *analyzed*, not adopted (Section 15G evaluates four models; none approved) |

### 3B. Design questions the prior research leaves open and this report deliberately leaves open (pointer-list, not resolutions)

1. **Market shape:** listings exchange vs directed trades vs hybrid (FO-009/FO-013/FO-022 cluster; Prompt 5 §21 flagged it as the highest-bound input). This report *compares* them (Section 9D) and recommends a staged answer, but does not decide it.
2. **Catch-up philosophy** (FO-018, Needs Research): no mechanism proposed; only its structural constraints are stated (Section 19).
3. **Protection/absence state machine** (FO-003/FO-017): adversarial enumeration is a future war-design task; only the state *classes* are named here.
4. **Treaty-type minimum** (FO-006): the minimal mechanical gate concept (NAP-analogue) is carried, not enumerated.
5. **Action-resource model for the military layer** (OP vs alternatives; D-004): compared in §15G; decision recorded open as SDQ-008.
6. **How much of relationships is public** (FO-004's unresolved info-leakage policy): carried as SDQ-004 with the DP-004 boundary noted.
7. **Write-budget math** (D-005/CCR-010, Prompt 3 §12 tier-1): architecture-stage task; this report states each system's write-posture qualitatively only.

---

## Section 4 — Gameplay framework overview (Deliverable 1)

### 4A. The player's conceptual loop

A player's ordinary turn-to-turn activity, synthesized from the 2h cadence, Prompt 4's session shapes, and Prompt 5 §9 (with this report's adjustments):

1. **Read the state of your nation and of the world around it** — the turn digest (private) plus the relationship/news surface (shared): what changed, *why* it changed, what is now possible.
2. **Decide what your nation is trying to do** — at three nested horizons: this turn (which queued orders to adjust before they resolve), this arc (which development line, deal, or diplomatic effort is progressing), this *idea* (what kind of nation this is becoming — the identity layer Prompt 4's personas demand).
3. **Commit limited resources and limited attention** — treasury allocations across development lines and upkeep; a small number of per-domain diplomatic/military actions; optionally a trade or treaty proposal to another player.
4. **Interact (where the game says so)** — respond to a partner, negotiate (asynchronously), participate in an alliance decision if in one, review a rival's public posture.
5. **Wait for resolution — or keep planning.** The turn boundary is the only time anything *mechanically* happens; between boundaries the player can queue, pre-schedule, negotiate, or do nothing without loss.
6. **Interpret and adapt** — the next digest reports outcomes *with provenance*; failed or worse-than-expected outcomes come with causes and options, not raw deltas.

The design commitment is that steps 1–6 are **the same loop at both session depths**: a 6-minute session honors it with one good call plus a digest read; a 40-minute session adds arc planning and negotiation threads (Prompt 5 §9D's table; strap-in for PXO-005).

### 4B. The four loops (distinct, connected)

**Core per-turn loop** (every turn, or every session): observe → prioritize → commit → resolve → interpret → adapt. *Satisfying when:* outcomes are legible, attributable, and change the *options available next turn*, not just numbers. Failures this loop must prevent: notification-chasing (DP-002 violation), chore wheels (F-019), unexplained deltas (PXE-013).

**Long-term strategic loop** (arcs, days-to-weeks): development lines rise/fall; specialization strengths and dependency exposures accumulate; reputation and treaty webs thicken; the nation acquires a *record* in the chronicle. *Satisfying when:* the player can point at something concrete ("we became the region's lending hub; everyone's treaties route through us") rather than "numbers went up" (criterion J of Prompt 5; guardian anti-pillar AP-005).

**Social/multiplayer loop** (persistent, asynchronous): offers, treaties, reputation events, alliance decisions, campaign commitments, and chronicle entries are *made by other players* and reshape each nation's option set. *Satisfying when:* others' choices create both help and hazards that are attributable and negotiable — without requiring anyone's scheduled presence (DP-002; the F-003b empty-world mitigation is structural — fewer, deeper couplings — not an activity demand).

**Return-after-absence loop** (on each long absence): the re-entry summary (FO-015) reports what changed while away — nation state, relationship movements, market drift, alliance/institution news, and pending decisions whose resolution windows approach. *Satisfying when:* re-entry feels like resuming a project, not paying a penalty; the FO-018 catch-up question is deliberately NOT answered by the absence loop mechanics (Section 20's boundary).

**How the loops connect:** the digest is the *same surface* for loops 1 and 4 (a per-turn report up to now; a re-entry report over weeks); arc planning in loop 2 is expressed through *queued multi-turn orders* (MO-008) inside loop 1; loop 3's inputs (other players' actions) are what loop 1's interpretation step is *about*. One shared chronological journal (FO-002's machinery, SYS-017) backs all four — a deliberate simplification (Section 21, SIM-006).

### 4C. The smallest system set that can produce this experience

Turn engine + clock with the timing contract (SYS-016) · nation model with treasury, production/development lines, drains (SYS-001…003) · specialization and structural scarcity (SYS-004) · one exchange/trade surface (SYS-005) · policy/stability levers (SYS-006) · relationship records + minimal treaty objects (SYS-008/009) · reputation-by-acts + chronicle (SYS-013/SYS-015) · digest/re-entry journal (SYS-017) · onboarding system (SYS-018). Research, alliances, military/campaigns, and rankings are staged (Tier C) — each boots later in a minimal form without re-architecting Tier A/B. This matches and elaborates Prompt 5 §15's E1–E6 first-playable boundary (Section 24).

---

## Section 5 — Gameplay system catalog (Deliverable 2)

The task's 22 candidate areas were consolidated **by exclusion, not by ID-merging**: every retained area keeps its own catalog ID below (contrary to any impression that treasury and production/upkeep were merged — SYS-002 and SYS-003 are separate IDs that *prioritization* treats as one build unit). Four areas were removed before cataloguing (cities/districts and population fold conceptually into SYS-003's abstract development lines; notifications fold into SYS-017's digest; public-stockpile/consumption do the same into SYS-002's abstract finance view). The remaining Tier-D areas (elections, contracts layer, consumer-demand sim, espionage, seasonality, meta-progression) were excluded entirely, not carried as systems — see §5.2. The result is **18 named systems** (SYS-001…018). Table legend: *Status* — Ess = essential candidate; Opt = optional candidate; Def = deferred out (recorded here, not carried); Rej = rejected. Complexity/Maintenance: L/M/H.

### 5.1 The catalog (compact full entries)

**SYS-001 "Nation Profile & Identity"** — Purpose: the player's persistent persona object: name, flavor identity, standing snapshots, chronicle links, and the *self-declared national direction* (which development lines the nation emphasizes). Player need: identity/legacy motivations [P#4]; the "what kind of nation am I running" anchor. Decisions: choosing/changing emphasis weights (MO-001), profile presentation. Inputs: player choices; Outputs: displayed card, emphasis weights to SYS-002…007. Timing: continuously editable between turns; snapshot at boundaries. Importance: essential (the CX-5 steward fantasy object). Complexity L; maintenance L. Dependencies: all. Risks: emphasis re-litigation (metagaming emphasis resets — track per SDQ-002). Status: **Ess**. Evidence: FX-A/FX-A′/FX-A″ structure [P#5]; F-001 family motivations [P#2].

**SYS-002 "Treasury & Finances"** — Purpose: single national currency pool plus the *finance view*: income sources, expense obligations, projected next-turn balance, and the explanation of each projected line (provenance). Player need: plan-without-surprise (PXO-002/PXO-005); PXO-002's "every number has a why". Decisions: allocation of surplus between lines, reserves, and gifts/contributions; accepting/declining deficit exposes. Inputs: production sales, trade, taxes-abstracted-to-income, upkeep bills; Outputs: spendable currency; commitments (alliance contributions, treaty obligations, construction in progress) recorded as pending deductions. Timing: flows resolve at boundaries; *commitments* are locked when made. Importance: essential. Complexity L–M; maintenance L. Dependencies: SYS-003 (income/expenses), SYS-005 (trade), SYS-010 (contributions), SYS-016 (advanced clock and timing contract). Risks: chronic death-spiral deficits (Section 20's "no agency after one mistake" — a floor rule is an SDQ, not a rule here); unbounded hoarding (moot for a single currency with drains — no storage stack). Status: **Ess**. Evidence: FO-014 (drains as designed pressure, "Yes" first-release); F-019 chore-fatigue caution.

**SYS-003 "Production & Development Capacity"** — Purpose: what the nation *does* each turn: production from active development lines; drains (upkeep on lines, readiness, services); the "national ledger" of capability states. *Deliberately replaces* per-tile/per-city/per-population models: one set of development lines (final count an SDQ; candidates: production, commerce, administration, science, readiness, works/infrastructure) each with level + efficiency + upkeep; no buildings, no city grids, no population sim (Section 21's SIM-001/SIM-002). Player need: compounding growth without menu sprawl (F-019-safe). Decisions: which lines to raise this arc; what to let stagnate; how much upkeep overhang to accept. Inputs: investments (funds), drains; Outputs: production per turn, line levels, upkeep obligations, capability unlocks (affects SYS-004 specialization options, SYS-007 progress, SYS-011 readiness). Timing: resolves at boundaries. Importance: essential. Complexity L–M; maintenance L. Dependencies: SYS-002 investment, SYS-004 emphasis, SYS-016. Risks: "worst-line" degeneracy (only production matters — DP-001 check; SDQ-001); invisible upkeep creep. Status: **Ess**. Evidence: FO-013/FO-014 [P#3]; Prompt 1 §7.3's skeleton (a); "build a thing that grows" pattern [P#1 §3].

**SYS-004 "Structural Scarcity & Specialization"** — Purpose: the mapless interdependence engine: nations cannot be max-strength at everything cheaply; specialization requires *sourcing* gaps from partners — creating the structural reason to trade, ally, and negotiate. Player need: multiplayer gravity (FO-013's keystone); trade sociability. Decisions: which niches to hold; whom to source from ( redundancy vs lean supply chains: resilience vs margin); when to re-specialize (slow, per FO-013's "slow re-specialization"; the cost level is an SDQ). Inputs: line emphasis weights (from SYS-001), partner availability, market prices; Outputs: capability gaps (materials the nation needs), surplus (what it exports), dependency map entries. Timing: specialization decisions commit at boundaries; trade flows per SYS-005. Importance: essential (DP-005's substrate and the concept's identity). Complexity M–H; maintenance M. Dependencies: SYS-003/005/007/008; FO-009's market for price signals. Risks: chokepoint bullying over one dependent nation (CCR-005's coupling-vulnerability risk; partial mitigations: multiple sourcing routes allowed, gap-classes solvable from ≥2 directions — both recorded as design checks, not rules); specialization-convergence (every nation builds the same best niche — CV-003's test). Status: **Ess**. Evidence: FO-013 [P#3]; DP-001/DP-005 boundaries [P#5].

**SYS-005 "Trade & Exchange"** — Purpose: how nations obtain gaps and monetize surpluses: (v1) *directed trades* — bilateral offers with mutual approval; (staged) *listings market* with day-boundary reference prices and integrity rules. Player need: F-022's legible economics; newcomers' first trade; FO-009's trade-as-relationship. Decisions: what to post/quote; when to hold reserves vs sell; which partners to prefer (relationship-weighted). Inputs: surpluses/needs (SYS-004), treasury, listings (players), reference prices; Outputs: transactions, relationship *trade-credit* (friendliness from reliable exchange), market drift signals. Timing: direct-trade offers persist until accepted/declined/expired (between-turn interaction); settlement at boundary; market listings per FO-009's shape when staged. Importance: essential (the concept's multiplayer engine). Complexity: M (directed) / H (market integrity). Maintenance: L→H as market stages in. Dependencies: SYS-002/004/008; anti-multi/anti-collusion defenses (Section 22, FO-009's §8 warning; PXE-foreign integrity family). Risks: collusion/automation/alternate-account flows (Section 20, R-01/R-02); liquidity death if the market stages in too early (Prompt 3's order-book defer logic). Status: **Ess** (directed trades first; market *staged*). Evidence: FO-009 [P#3], CCR-008, Prompt 5 §16B-5's staged-economy compromise.

**SYS-006 "Domestic Policy & Stability"** — Purpose: a *light* internal-governance layer: a small set of togglable policy levers (FO-005's candidates: growth↔stability, openness↔security-style trade-off axes; exact set = SDQ-005) with cooldowns; stability as a state that *multiplies or taxes every other path*. Player need: governance flavor without an institution sim; the "steward" feel of managing a country. Decisions: which levers are on; how fast to change course (cooldown + tempo politics reactions); which policy trade-offs the nation lives with. Inputs: lever states, events (systemic only), recent changes; Outputs: stability state, efficiency multipliers, documented policy history. Timing: lever changes at boundaries with cooldown; stability re-evaluated per turn. Importance: essential-not-dominant: it is the *floor/enabler* per DIR-3 — explicitly not a success ladder. Complexity L–M; maintenance L–M. Dependencies: SYS-002 (policy costs), SYS-003 (efficiency coupling), SYS-015 (policy chronicle). Risks: adversarial "best-picks" degeneracy (SDQ-005's balance test); F-015's weak demand — if playtests show levers feel arbitrary, the layer is a *cut candidate* (Section 21's status). Status: **Ess (minimal), Enhancement story in Tier C**. Evidence: FO-005 [P#3]; F-015 [P#2]; Prompt 1 §7.4's light-politics recommendation.

**SYS-007 "Research & Capability Programs"** — Purpose: *slow* convertibility from economy into new option-classes: a few national programs (not a tree) that unlock capability modifiers and new action types (e.g., better trade efficiency, defensive readiness options, administrative improvements). Player need: long-arc compounding; differentiation over time. Decisions: which program(s) to run (few at once), whether to *share* results with a partner/alliance (diplomacy-coupled generosity embargo choice). Inputs: funds + science-line level; Outputs: capability unlocks/modifiers, occasional shared research credit. Timing: progress accumulates at boundaries; completion grants at boundaries. Importance: optional candidate (Tier C boots first): modifier-not-ladder per DIR-3; v1 might ship with zero programs and one placeholder to keep scope honest. Complexity M; maintenance L–M. Dependencies: SYS-002/003/004; SYS-008 for sharing mechanics. Risks: convergence (everyone runs the same program order — counter via tradeable benefits and front-loading different program *classes* per emphasis; CV-003 checks perception); balance burden over a persistent world (no reset means no retune moment) — flagged as a staged-design risk (SDQ-006). Status: **Opt**. Evidence: DIR-3 [P#5]; Prompt 1 §7.3's thin evidence note; FO-013's "specialization earned via research/infrastructure".

**SYS-008 "Bilateral Relationships"** — Purpose: the relationship record layer of the world network: typed relationship states per nation-pair (cooperative, neutral, tense, adversarial, hosting-specific states like trade-credit or grievance), with *visible histories* and event-sourced changes. Player need: FO-004's mapless orientation; "where do I stand with whom". Decisions: initiating/ending relationship actions; interpreting another nation's posture; curating own public posture (declared stances). Inputs: events from all other systems; Outputs: relationship states displayed everywhere (SYS-009 treaty gates, SYS-012 campaign posture, SYS-013 reputation contributions). Timing: changes at event time (records) with public news where policy says so. Importance: essential (UXD-002's data layer). Complexity M; maintenance L. Dependencies: SYS-009/012/013; FO-004's schema. Risks: privacy policy design (SDQ-004: what is public, what visible-to-partner, what private — DP-004's boundary: *relations* transparent, *intent* opaque); message spam not a system (chat is out-of-scope for the register; the world view is the system). Status: **Ess**. Evidence: FO-004 [P#3]; P&W treaty-web precedent [P#1 §7.5].

**SYS-009 "Treaties & Agreements"** — Purpose: typed, inspectable, *scope-limited* commitments: v1 minimum = a non-aggression-analogue (mechanically enforced block on hostile actions between signatories) + an information-typed set of promise records (trade handshake of record, mutual-assistance spirit-of, etc.) with *no* enforcement beyond the NAP-analogue (matching P&W's verified reality: "treaties not enforced except non-aggression" [P#3 P22]). Player need: legible diplomacy; commitments that show up in the world; CX-3's "ledger of promises" dialect. Decisions: offering/accepting/refusing; scope negotiating (small bilateral instruments vs Bloc commitments — *separate objects*, never one mega-treaty); exiting (visible withdrawal with reputation cost — record as an act). Inputs: relationship history (SYS-008); Outputs: active-treaty records, mechanical gates (only for the block-type), reputation events. Timing: signing/exit records immediately; consequences at boundaries. Importance: essential in *minimal* form (Prompt 5 §15 S1's simulated form is enough for concept testing; real typing arrives Tier C). Complexity M; maintenance L–M. Dependencies: SYS-008/013. Risks: obligation lock-in runaway (Prompt 5 §10B-2's reputation→treaty trap; counter: always scope-limited, always exitable, exit is recorded not prevented); type inflation (keep the v1 set ≤ enumerable count — SDQ-014). Status: **Ess in minimal form**. Evidence: FO-006 [P#3]; Prompt 5 §11 layer 2.

**SYS-010 "Alliances & Collective Administration"** — Purpose: structured collective action: minimal v1 alliance object (shared name/banner, bank view, one tax bracket, role-lite permissions) with an **audit-first** record culture (FO-007's differentiator); plus curated collective actions (FO-008's small legitimate set) later. Player need: community gravity (F-001); coordination without Discord-only (F-18 eased). Decisions: join/leave; contribute/spend shared funds (permission-gated); leadership's public stances; (later) designate collective focus campaigns (FO-012 analog, capped small). Inputs: member contributions; Outputs: shared treasury, collective records, member permissions. Timing: treasury transfers resolve at boundaries; role changes immediate-with-audit. Importance: optional candidate — *never mandatory* (AP-004): independent play stays structurally viable (SYS-004's sourcing works outside alliances). Complexity M (v1) → H (full matrix deferred); maintenance M. Dependencies: SYS-002/005/009/012. Risks: treasury theft/misuse (audit logs + permission gating; SDQ-012's abuse walkthrough); permanence (a defunct alliance holding assets — succession rule needed, SDQ-013); FO-007's High complexity means *minimal-first shipping* is the standing posture. Status: **Opt**. Evidence: FO-007/008 [P#3]; F-013/F-018 [P#2]; AP-004 [P#5].

**SYS-011 "Military Capability & Readiness"** — Purpose: the nation's *defensive reality check under bounded conflict*: readiness as a maintained capability class (upkeep-burning), posture states (dormant/ready/mobilizing) affecting deterrence reading by others; *not* a conquest engine. Player need: security assurance for doves; a real option for hawks (bounded). Decisions: invest in readiness vs trade/development posture; mobilization (visible — posture is public); what to spend spare budget on. Inputs: funds; Outputs: readiness level, posture, deterrence signal; capability floor for SYS-012 campaigns. Timing: readiness drifts at boundaries; posture changes at boundaries. Importance: optional-but-real (Tier C minimal form; Prompt 5 §15 S3's scripted vignette is the first-playable stand-in). Complexity M (capability) / H (campaign rules — deferred to SYS-012's dedicated stage). Maintenance: M (balance-sensitive). Dependencies: SYS-002/003; SYS-012 depends on *this* system's outputs. Risks: dominant-army runaway (Prompt 5 §10B-1's economy→military spiral; counter: DP-006's bounded-conflict design + DP-001's no-dominance check; SDQ-008's action-resource question); F-016/F-017 fairness family (Section 20, R-04/R-05). Status: **Opt (Tier C, minimal first)**. Evidence: FO-010/011/017 [P#3]; DP-006 [P#5].

**SYS-012 "Strategic Campaigns & Settlements"** — Purpose: how bounded conflict *happens* season-to-season: declared, discrete campaign objects over non-geographic objectives (market-access disputes, pairing claims, reputational challenges, protective operations); planning → resolution via a small action set → **settlement stage** where outcome vocabulary (terms, concessions, chronicle records) is chosen or negotiated — FO-011's settlement-flow premise and UXD-004's differentiator. Player need: consequential drama for future-tier players; defender justice for everyone else. Decisions: initiate (a real, reputation-bearing decision); which objective-type; the settlement package to pursue/accept. Inputs: readiness (SYS-011), objectives, relationship state, protection states; Outputs: campaign records, settlement terms, chronicle entries, bounded attachment effects on the loser's economy/market posture. Timing: campaign actions land at boundaries; *no live activity windows* (FO-026 rejected — attendance-tolerant). Importance: optional candidate; the *dedicated war-design stage* supplies real rules (Section 15's boundary). Complexity: H (the project's largest design surface — Prompt 3's assessment). Maintenance: H. Dependencies: SYS-008/009/011/013/015. Risks: farming/fake-wars/term abuse (Section 22, R-05; FO-017's adversarial-first requirement); "toothless theater" if boundedness overcorrects (CCR-006 — the vignette test). Status: **Opt (Tier C; scripted first)**. Evidence: FO-011/FO-017 [P#3]; UXD-004 [P#5]; Prompt 1 §7.7.

**SYS-013 "Reputation & International Standing"** — Purpose: how the world *remembers*: an acts-driven reputation layer (recorded acts change states; no hoardable single score) feeding standing registers — multiple *named registers* (economic standing, diplomatic reliability, military respect, institutional stewardship) rather than one ladder (DP-001's structural answer; MO-007). Player need: identity/legacy; fair standing for diplomatically-sized nations. Decisions: which standing register to invest toward; acts whose costs include standing (declined trades, treaty exits, war postures). Inputs: acts from all systems; Outputs: reputation states, register placements, "how others see me" displays. Timing: updates with acts/boundaries. Importance: essential (the diplomat path's currency; the mapless world's "scoreboard"). Complexity: L–M; maintenance M (act-taxonomy). Dependencies: SYS-008/009/012/015. Risks: gaming (staged-act inflation, R-06 in Section 20); mandatory-homogeneity: don't let one register swallow the others (DP-001's balance check; CV-003's test). Status: **Ess**. Evidence: DIR-3 [P#5]; F-029 watchlist caution [P#2].

**SYS-014 "Rankings, Objectives & Achievements"** — Purpose: *comparative visibility*: the standing registers' public views + optional national objective milestones (player-picked, non-required) + chronicle-linked achievements; NO single global "best nation" ladder as a design driver (AP-005). Player need: goal-setting for non-diplomat builders; spectator legibility. Decisions: which milestone set to pursue; whether to display progress publicly. Inputs: all systems' states; Outputs: visible rankings (per-register), milestone progress. Timing: re-computed at boundaries. Importance: optional candidate (early boot optional; the standing registers from SYS-013 might make a separate ranking UI unnecessary at v1 — SIM-007's simplification). Complexity L; maintenance L. Dependencies: SYS-013/015. Risks: leaderboard-collusion farming (minor at small worlds; R-06); myopia (if the visible register becomes "the" score, dominates thematic play — DP-001's check). Status: **Opt (Tier C/deferrable to Tier B-lite via SYS-013)**. Evidence: F-020's narrow-success finding [P#2]; DIR-3.

**SYS-015 "World Chronicle & News"** — Purpose: the world's shared memory: a chronological public record of notable world events (treaties signed/exited, settlements, market shocks, institutional changes, standing movements) — *systemic* generation only (AP-003: no editorial calendars); the "stories" surface that makes a small world feel dense. Player need: world aliveness at low populations (PXE-015/F-003b's mitigation); legacy ("what my nation did" is *findable*). Decisions: (for the design) which events qualify; players don't author chronicle entries directly. Inputs: sys-events; Outputs: public timeline, national history views, digest headlines. Timing: entries on event; retention policy per write budget (SYS-016/SDQ-003). Importance: essential (UXD-002's story layer; the CF-003b counterweight). Complexity L–M; maintenance L. Dependencies: SYS-016/017's journaling. Risks: noise flood (needs entry taxonomy + quality bar — SDQ-017); write-budget pressure (CCR-010). Status: **Ess**. Evidence: Prompt 5 §12A's chronicle layer; PXE-015 [P#4].

**SYS-016 "Turn Engine & World Clock"** — Purpose: the shared 2-hour cadence (12/day, UTC), the **three-class action-timing contract** (PXO-003): (i) *immediate-with-record* (profile/posture edits, messages of record), (ii) *queued-until-boundary* (orders, listings, investments, treaty offers), (iii) *boundary-scheduled* (multi-turn arcs); plus idempotent, recoverable resolution processing and the deterministic ordering policy (a recorded-order catalog per SDQ-018). Player need: certainty about "when things take effect" (PXO-003's P0). Decisions: players don't decide engine internals; the design decides the ordering catalog. Inputs: all queues; Outputs: resolved states, journal entries, digest source. Timing: boundary-resolution processing; between-boundary commits land pending-records. Importance: essential foundation. Complexity M (concurrency/integrity engineering heavy in later stage); maintenance M. Dependencies: every SYS. Risks: duplicate-execution bugs, replay drift (the reason this is a *system*, not plumbing);missed-boundary timing ambiguities (Section 20's R-07). Status: **Ess**. Evidence: §2 constraint; FO-002's deterministic-tick dependency; PXO-003 [P#4].

**SYS-017 "Turn Digest, Re-entry & Explanation"** — Purpose: the *world explains itself* layer: per-turn nation digests with per-line provenance (FO-002), the re-entry summary across absences (FO-015), the digest's shared taxonomy (per-line detail one click deeper — PXO-005's one-screen-first), and the in-context explanation surface (FO-001's terms-of-art explanations). Player need: the genre churn family's systemic answer (F-010/F-014/F-027; PXE-013/016). Decisions: (design) which lines get provenance at v1. Inputs: journal (SYS-016), relationship states, chronicle; Outputs: digest pages, re-entry summary, hover explanations. Timing: rendered on-demand; generated from journals. Importance: essential (UXD-001's data layer). Complexity M; maintenance M. Dependencies: SYS-016/015; SYS-001…013's outputs. Risks: write volume (CCR-010's budget math); information-overload if unprovenanced richness ships at once (SDQ-017's taxonomy-first rule). Status: **Ess**. Evidence: FO-001/002/015 [P#3]; PXO-002/003/005 [P#4].

**SYS-018 "Onboarding & First-Decision"** — Purpose: the guided-but-real entry experience: no tutorial-dump; one real first decision in the first session (PXO-004), progressive surface-reveal (Prompt 5 §12A-9's teaching-the-structure path: nation card → register → market → chronicle), and the mapless-reading teaching that CV-002 will verify. Player need: PXE-002/007/012's first-week friction family; PXE-016's jargon wall. Decisions: (design) the first-decision choice set; reveal order. Inputs: player state; Outputs: guided start, glossary-in-place. Timing: first-session flow; ongoing hover explanations (from SYS-017). Importance: essential (a system with content-role, not "polish" — Prompt 4's conviction). Complexity L–M; maintenance M. Dependencies: SYS-017/001/003; SYS-016's timing contract. Risks: scripted feel (PXO-004's noted risk); content maintenance without AP-003's editorial dependence (keep it systemic/system-generated where possible). Status: **Ess**. Evidence: PXO-004 [P#4]; FO-001 [P#3].

### 5.2 Excluded areas (recorded, not carried as systems)

| Excluded candidate area | Disposition | Pointer |
|---|---|---|
| Cities/districts & population sim | Merged conceptually into SYS-003's abstract development lines; no per-city model | Section 21 SIM-002; Prompt 3 §11 rejection |
| Contracts/escrow/supply layer | Deferred (FO-022 Deferred); revisit with alliance-supply needs | §5.1 SYS-005 note |
| Consumer/retail demand sim | Deferred (FO-021 Deferred) | Prompt 3 §10 |
| Elections/congress governance | Deferred (FO-023 Deferred); only if SYS-006 proves under-powered | Prompt 3 §10 |
| Espionage/intel | Needs Research (FO-019) — watchlist only | Prompt 3 §10 |
| Seasonality/event calendar | Deferred (FO-020 Deferred) | Prompt 3 §10 |
| Account meta-progression | Rejected for concept: no evidence-base; conflicts with the "the nation is the account" identity | Not a system; a watchlist note |
| Multiple currencies / resource stacks beyond the economy model | Rejected by this report's simplification analysis | Section 21 SIM-001 |

### 5.3 System-ID register (unique, for cross-referencing)

SYS-001…SYS-018 above, hard-listed here for tooling: SYS-001 Nation Profile & Identity · SYS-002 Treasury & Finances · SYS-003 Production & Development Capacity · SYS-004 Structural Scarcity & Specialization · SYS-005 Trade & Exchange · SYS-006 Domestic Policy & Stability · SYS-007 Research & Capability Programs · SYS-008 Bilateral Relationships · SYS-009 Treaties & Agreements · SYS-010 Alliances & Collective Administration · SYS-011 Military Capability & Readiness · SYS-012 Strategic Campaigns & Settlements · SYS-013 Reputation & International Standing · SYS-014 Rankings, Objectives & Achievements · SYS-015 World Chronicle & News · SYS-016 Turn Engine & World Clock · SYS-017 Turn Digest, Re-entry & Explanation · SYS-018 Onboarding & First-Decision. (18 IDs; no gaps.)

---

## Section 6 — System prioritization (Deliverable 3)

### 6.1 Tier A — Core foundation (cannot be omitted; the identity would be untestable)

| System | Why Tier A | What becomes impossible to test if omitted | Links |
|---|---|---|---|
| SYS-016 Turn Engine & World Clock | The game *is* the shared clock; everything else times to it | Nothing else can resolve; cadence acceptance (CV-004) untestable | E2 [P#5] |
| SYS-002+SYS-003 Treasury/Production/Development | Compounding national progress is the fantasy's spine | E1's "does compounding feel like stewardship" untestable (CV-003) | E1, FO-013/014 |
| SYS-004 Specialization & Structural Scarcity | The mapless interdependence engine; multiplayer gravity's source | DP-005/independence/DP-005-as-cause untestable; CV-003's two-value-source probe degenerates | E4/E5, FO-013 |
| SYS-017 Digest & Explanation | DP-004/UXD-001's medium; the churn answer | E3 untestable (CV-006); the "why did this change" pillar collapses to marketing | E3, FO-002/015 |
| SYS-018 Onboarding & First-Decision | Entry friction is a genre-verified churn axe (PXE-002/007/012/016) | The first-session experience (the moment most likely to be abandoned) untestable | PXO-004 |

*Tier A total: 5 build units covering 6 system IDs (SYS-002/003 counted as one build unit). Complexity posture: moderate per system, none high; the collective scope is Prompt 5 §15's E1–E6 plus onboarding — deliberately the whole of what the first playable needs and nothing else.*

### 6.2 Tier B — Core interaction (the multiplayer layer; some may boot simplified)

| System | Why Tier B | Initial simplification / simulation option |
|---|---|---|
| SYS-005 Trade & Exchange | The interdependence engine's transaction surface | Directed bilateral trades only at first (no market); FO-009's market stages in when integrity work is defensible (CCR-008) |
| SYS-008 Bilateral Relationships | The world network's record layer (UXD-002's data) | Typed records with small fixed type set; no graph UI (list/first per FO-004 staging) |
| SYS-009 Treaties & Agreements | Commitments-as-objects; NAP-analogue block as the only mechanical gate | v1: block-type + display records only (FO-006's minimal); treaty web listing view |
| SYS-013 Reputation & Standing | The diplomat path's currency; "how others see me" | Acts-driven records feeding 2–3 standing registers; no numeric public scores at v1 |
| SYS-015 World Chronicle & News | Small-world aliveness (the F-003b counterweight); legacy record | Systemic event entries with a strict quality bar; retention-first |

*Each Tier-B system has a "lightest defensible v1" above; the full versions are staged with the dedicated design stages (Section 24's roadmap).*

### 6.3 Tier C — Expansion systems (enhance depth after the core is validated)

| System | Why deferred, and what evidence would promote it |
|---|---|
| SYS-001 Emphasis/features depth (identity presentation) | Clean enough at v1 (weights + flavor); presentation expansions after CV-002/CV-005 wording evidence |
| SYS-006 Policy & Stability (full lever set) | v1 ships 1–2 levers; the rest after playtest shows which axes players actually trade off (F-015's thin demand) |
| SYS-007 Research & Programs | Boot after economy settles; promote if playtests show a compounding-hunger for option-unlocks beyond development lines |
| SYS-010 Alliances (full governance) | Minimal object first; full role/tax/audit matrix only when community density justifies it (F-001's gravity once real) |
| SYS-011 Military Capability (real readiness layer) | After the war-design stage exists; the first playable uses SYS-012's vignette instead |
| SYS-012 Campaigns & Settlements (real rules) | The dedicated war-design stage concludes its rules; until then the concept tests via a scripted vignette (Prompt 5 §15 S3) — promoted by CV-006/vignette tests |
| SYS-014 Rankings/Objectives | Ship as standing-register views (SYS-013) first; a dedicated objective system only if players ask for explicit goals |

*Tier C total: 7 entries (SYS-001 depth, SYS-006, SYS-007, SYS-010, SYS-011, SYS-012, SYS-014). Tier-C membership is not "unimportant": SYS-012 in particular carries UXD-004's differentiator. The tier means: *not before the core validates*, not "never".*

### 6.4 Tier D — Deferred or rejected areas

| Area | Disposition and the plausible trigger that would change it |
|---|---|
| Elections/congress (FO-023) | Deferred: only if SYS-006's light politics proves under-powered in play (F-015 weakness remains the blocker) |
| Contracts/escrow/supply (FO-022) | Deferred: revisit if alliance-supply logistics emerges as a real need or market fraud pressure demands escrow |
| Consumer-demand sim (FO-021) | Deferred/mostly rejected: nation-scale abstraction has no demonstrated need; retail framing is individual-scale |
| Espionage (FO-019) | Needs Research only: costs outweigh proven demand; revisit only for mapless-war *counterplay* design if wars feel too predictable |
| Seasonality/events (FO-020) | Deferred post-v1 texture; not a system | 
| Rounds/resets (FO-024) | **Rejected**: persistent world by constraint |
| Geographic map (FO-025) | **Rejected**: confirmed constraint (AP-002) |
| Live-timed windows (FO-026) | **Rejected**: confirmed constraint (AP-007; DP-002) |
| Pay-gated late-game features (FO-027) | **Rejected** as a pattern; monetization unscoped elsewhere |
| Account meta-progression | Rejected for now: no evidence; watchlist only |

---

## Section 7 — System interaction map (Deliverable 4)

### 7.1 How this map was built

Not all pairs interact: the concept's discipline is *meaningful interdependence* (Prompt 5 §DP-005's bound; "avoid coupling for coupling's sake"). The 14 candidate interactions below were selected because each (a) creates a decision the player must *choose on*, (b) closes a loop, or (c) is structurally unavoidable. Each row carries the 12 required fields, compressed: **source→target · nature · decision enabled · why interesting · PFB(+)/NFB(−) feedback loops · exploit risks · complexity · essential? · evidence/confidence · now/later**. The prose after each row group expands the four most consequential couplings.

### 7.2 Interaction matrix

| ID | Source → Target | Nature | Decision it enables | Why interesting | Feedback loops | Exploit/balance concern | Cx | Ess? | Evidence / confidence | When |
|---|---|---|---|---|---|---|---|---|---|---|
| INT-001 | SYS-003 Production → SYS-002 Treasury | Per-turn income; upkeep drains against it | What to produce/sell vs hold; upkeep-overhang tolerance | The steward's solvency question, every turn | +: investment → output → surplus → investment; −: overexpansion → upkeep crisis → forced austerity | Death-spiral deficits; hoarding (moot — single currency + drains) | L | Yes | FO-014 [P#3] / H | Now |
| INT-002 | SYS-002 Treasury → SYS-003 Development | Investment converts surplus to line levels | Which lines this arc; how much to hold in reserve | Budgets vs ambitions; visible compounding | +: compounding; −: upkeep drag as lines grow | Worst-line degeneracy (only production matters — DP-001 check) | L | Yes | FO-013/014 [P#3] / H | Now |
| INT-003 | SYS-004 Specialization → SYS-005 Trade | Gaps sourced, surpluses sold | Sourcing routes vs lean chains; redundancy vs margin | Structural trade reasons without geography | +: pairing bonuses → deeper specialization; −: partner loss → gap shock (CCR-005's vulnerability risk) | Chokepoint bullying; collusion in pairings | M–H | Yes | FO-013 [P#3] / M–H | Now |
| INT-004 | SYS-005 Trade → SYS-008 Relationships | Trade history builds trade-credit/grievance records | Whom to trade with; reliability as reputation capital | Doing business as a *relationship*, not a transaction | +: reliable partners compound; −: betrayal records stick | Alternate-account farming (Section 22 R-01) | M | Yes | FO-009 [P#3] / H | Now |
| INT-005 | SYS-006 Policy → SYS-003 Production | Stability/efficiency multipliers | Which policy trade-offs to live with | Governance feels connected to economy — but never dominates | +: stability → growth; −: growth-first → fragility (vulnerability multiplies) | Best-pick degeneracy (SDQ-005's balance test) | M | Yes (minimal) | FO-005 [P#3] / M | Later (v1 ships 1–2 levers) |
| INT-006 | SYS-003/006 → SYS-013 Reputation via SYS-015 Chronicle | Systemic events become standing records | Which acts to accumulate (generosity, consistency) | "How others see me" as earned state, not opinion | +: reliable actors attract better terms; −: fail-streaks reprice you fast | Act-farming; staged-sockpuppet boosts | M | Yes (acts taxonomy) | DIR-3 [P#5] / M–H | Now (records) / Later (tuning) |
| INT-007 | SYS-009 Treaties → SYS-012 Campaign posture | NAP-analogue blocks hostile action; promise records shape war legitimacy | What to sign; what a signature costs | Promises have game state, not just chat | −: staggered exits burnstanding; +: reliability compounds | Obligation web lock-in (Prompt 5 §10B-2) | M | Yes | FO-006 [P#3] / H | Now (minimal types) |
| INT-008 | SYS-011 Readiness → SYS-012 Campaign outcomes | Readiness levels gate campaign viability | Invest in readiness vs alternative uses | The hawk's trade-off is legible, not infinite | +: deterrence feeds standing; −: readiness drains solvency (F-019 caution) | Economy→military runaway (Prompt 5 §10B-1; DP-006 bound) | M | Yes (bounded) | FO-010/011 [P#3] / M | Later (war design) |
| INT-009 | SYS-012 Settlements → SYS-013/008/015 | Settlement terms write relationship, reputation, and chronicle records | Which terms to pursue/accept | Conflict *produces records*, not just ruins (UXD-004) | −: war-weariness discounts; +: genuine settlement prestige | Fake-war/term abuse (FO-017's adversarial list) | H | Yes (design-stage-bound) | FO-011 [P#3] / M | Later (war design) |
| INT-010 | SYS-016 Turn Engine → all systems | The three-class timing contract PXO-003 | Which orders to queue vs commit | "Bet on the next twelve turns" clarity | (structural, not loop) | Ordering-race exploits at boundaries (Section 20 R-07) | M | Yes | PXO-003 [P#4] / H | Now |
| INT-011 | SYS-017 Digest ← all systems' journals | Provenance reporting; re-entry across absence | How to read the last N turns; what to react to | The world explains itself (DP-004); churn answer | +: trust; −: privacy tension (DP-004 boundary note) | Write-volume (CCR-010); overload (SDQ-017) | M | Yes | FO-002/015 [P#3] / H | Now |
| INT-012 | SYS-010 Alliance → SYS-005/012 collective surfaces | Shared projects/focuses; permission-gated actions | Contribute to what; designate focus | Group play with *optional* depth (AP-004) | +: collective focus multiplies each member; −: dependency on leadership (F-018) | Treasury misuse (R-08); membership-for-edge cycling | M–H | No (Tier C) | FO-007/008/012 [P#3] / M | Later |
| INT-013 | SYS-014 Rankings/objectives ← SYS-013 registers | Comparative visibility | Pick milestone sets | Goals for non-diplomat builders | +: clarity; −: scoreboard homogenization (AP-005) | Collusion farming at small N | L | No | F-020 [P#2] / M | Later |
| INT-014 | SYS-018 Onboarding ← SYS-016/017 | First-decision scripting; progressive reveal | (player: the first real decision) | visualizes the world's structure (CV-002's teaching) | +: early trust; −: scripted feel (PXO-004) | Content maintenance creep | L–M | Yes | PXO-004 [P#4] / M–H | Now |

### 7.3 The four consequential couplings, in prose

**(1) The economy–specialization coupling (INT-002+INT-003).** This is CX-5's gravity engine. Its danger is the two-sided lock: if a nation specializes deeply, its gaps are others' leverage; if the design overcorrects toward autarky, interdependence dies the quiet death (everyone grows everything; trade becomes flavor). This report's structural check — *every gap-class must be fillable from at least two sourcing routes, and every surplus must have more than one prospective buyer class* — is a **design-time test recorded as SDQ-009**, not a rule; the exact urgency (post-hoc) belongs to a later economy stage. The coupling also deserves a CV-003-visible demo: two mock nations with complementary emphasis, and what each needs from the other.

**(2) The reputation–commitment coupling (INT-006+INT-007+INT-009).** Acts, treaties, and settlements all write into the national and relationship memory; reputation prices future agreements. Two exploitable shapes must be adversarially considered at design: *penitent cycling* (sign, profit, exit, repent, re-sign — the counter is recorded exits decaying slowly and visibly, a design-stage rule), and *reputation transfer across accounts* (small fresh accounts doing veteran nations' good-faith acting — an integrity control question for Section 20's R-06). Honest trade-off: a purely act-driven reputation without decay becomes a permanent record that makes newcomer nations feel like second-class players — the opposite of F-012's late-join friction; the decay-vs-permanence question is SDQ-011.

**(3) The conflict–everything coupling (INT-007+INT-008+INT-009).** Conflict touches relationships, economy (via settlement effects), reputation, and the chronicle — deliberately *not* production arithmetic directly. Structural risk per DP-006: a cascade where a minor grievance escalates into someone's economy collapsing. This report's containment approach: conflict's economic attachment is *bounded and itemized* (visible scheduled effects, capacity-uncapped, no compounding debt) and its escalation has stated off-ramps — parameters for the future war-design stage, not finished rules.

**(4) The transparency coupling (INT-010+INT-011).** The journal feeding the digest means every systemic change is *traceable*; this is the concept's fairness spine — and its biggest privacy/strategic-mystery tension (Prompt 5 §16B-3). Carried controls: provenance depth is *tiered by sensitivity* (public relations events, partner-visible terms, private internal math only for self) with the exact tiering as a small-v1 information policy question (SDQ-004, inherited from Prompt 3 §12 tier-2 #5).

### 7.4 Isolated-system audit

Findings from the matrix: no proposed system exhibits a *total* isolation problem. Three flagged partial cases:
- **SYS-007 Research** at v1-minimum would influence little; if it boots, it must couple to SYS-003's efficiency and SYS-004's emphasis mechanics from day one, or it becomes a decorative progress bar (retained as Tier C partly for this reason).
- **SYS-014 Rankings** risks being read-only (SYS-013's display layer already covers it). Kept as a Tier-C "may never be built" candidate; this is the intended verdict of SIM-007 in Section 21.
- **SYS-006 Policy (full version)**'s event-stream was identified in CX-2's rejection as content-hungry (AP-003's boundary). v1 keeps the lever set tiny and systemic (no hand-scripted events), which per FO-005's analysis is the only shape that respects both moderation-budget and F-019's chore-fatigue.

### 7.5 Dangerous-coupling audit

Beyond the four couplings above, three cascades that could have multiplied across whole system families were explicitly considered and bounded:

1. **Stability cascade** (if stability hits production, research, trade AND diplomacy simultaneously — the task's example): rejected in this shape. Stability is implemented as *one* multiplier gate on the economy and a gate on policy changes (Section 10's posture) — defined in prose as a *floor*, not a five-way tax. Trade/relations penalties come only from *specific* recorded acts (defaulted deals, treaty exits), not from a global fragility aura.
2. **Reputation cascade** (every act touching everything): kept out by the act-taxonomy discipline (SDQ-010): an act is registered under *one primary* standing register plus at most one secondary effect — not omnidirectional.
3. **Conflict→economy→conflict spiral** (loser can't sustain readiness → attacked again): bounded by the settlement structure (Section 15E's bounded-consequence candidates) rather than by formula hard-wiring; the war-design stage owns the actual ratchet controls.

---

## Section 8 — National development framework (Deliverable 5)

### 8A. The simplest coherent model: development lines

Six candidate lines (final set an SDQ-001 decision): **Production** (output per turn) · **Commerce** (trade efficiency, market posture options) · **Administration** (action capacity, order slots, institution quality) · **Science** (research throughput) · **Works/Infrastructure** (reduces drains, unlocks efficiency modifiers) · **Readiness** (SYS-011's military floor). Each line = level (progressed by investment) + efficiency modifiers (from works, policy, research) + upkeep (grows with level). No buildings, no city grids, no population counts, no per-line resource trees. This single abstraction carries the genre's "build a thing that grows" appeal while staying auditable (FO-002's provenance-friendly: tiny state, explainable transitions).

### 8B. The ten questions

1. **What can a player improve?** The six lines' levels and the emphasis weights among them (SYS-001's identity dial), plus capabilities unlocked by research (Tier C).
2. **What trade-offs arise?** Investments are finite vs upkeep obligations that grow with every level — *abundance is managed* (FO-014/FO-019's discipline). Emphasis weights trade peak-efficiency against flexibility (a heavily-weighted line is stronger; un-weighted lines are slower to develop). Some coherence questions (SDQ-001) later determine whether emphasis changes are instant or phased.
3. **Which capabilities grow over time?** Lines, standing registers (SYS-013), treaty-web position (SYS-009), chronicle record (SYS-015).
4. **What limits development?** Upkeep solvency (INT-001), drain growth, attention (a small per-turn order-capacity from Administration — *not* a grid), and other players (market posture, sourcing routes, campaign threats).
5. **How does development create future options?** Line thresholds unlock *classes* of decisions (a commerce threshold enabling listing-market participation; a science threshold enabling a program class) — progress is expressed in options, not only totals.
6. **How can strategies specialize?** Via emphasis weights + sourcing needs: an export-led nation emphasizes production/commerce and buys administration support; a diplomatic-mediator nation emphasizes administration/science and buys production; a defensive posture emphasizes readiness/works.
7. **How is a universal build avoided?** DP-001's test at each threshold design; the *structural-scarcity* engine (SYS-004) is the deep answer — scarcity curves make "all meta" expensive; CV-003 verifies perception.
8. **What makes development decisions non-trivial?** Irreversibility gradients: line levels are slow to move; emphasis changes are moded *slowly* if at all (as FO-013's "slow re-specialization" requires); orders and posture are cheap to change — a three-speed commitment model rather than one undifferentiated game.
9. **Understandability at scale?** The national card's digest-first supply: every line's per-turn delta carries provenance; the long-term trend view is one click deeper (PXO-005's one-screen-first).
10. **First-playable version?** Lines (a minimal 3-line variant of SYS-003), emphasis weights (a static demo-level form), and the derivation/progression loop (Prompt 5 §15's E1).

### 8C. Specialization vs flexibility (the prompt's required tension, explicitly addressed)

The framework's commitment: **no choice permanently locks a nation out of any path**. Structural scarcity (SYS-004) creates *costs*, not walls: re-specialization is a slow, paid, visible project (FO-013's design premise), which means a 2-year-old nation can pivot, but deliberately expensively — giving newcomers a *moving target* rather than a static veteran mountain (one of FO-018's candidate levers, kept honest: this is a *design posture*, not a resolved catch-up policy). The research-level question remains open (SDQ-001): whether emphasis changes cost funds, time, or *both time and a stability period* is a numeric-design-stage balancing matter; the concept only mandates that re-specialization exists and is legible.

---

## Section 9 — Economic system framework (Deliverable 6)

### 9A. Economic identity (what economic decisions should *feel* like)

Recommended posture (provisional): **steward balancing ambition against solvency**, expressed through three recurring financial decisions — (i) *allocation*: where this arc's surplus goes; (ii) *specialization*: what we grow and what we intentionally buy rather than grow; (iii) *resilience*: how much dependency and reserve risk the nation accepts. Not a spreadsheet-optimizer identity (CX-1's rejected presidency — kept as a fallback fragment, not the spine), not a click-chore identity (F-019's rejected). The primary audience's 5–15-minute session must permit "one allocation decision that matters."

### 9B. What a player must understand (the economic information contract)

Current treasury; expected income (line-item provenance); expected expenses (line-item, *with which are contractual obligations vs discretionary*); what changed after the last turn and why (digest lines, PXO-002); major risk exposures (dependency map entries from SYS-004's sourcing routes); the consequences of a *proposed* investment (a preview line whose format is an interface SDQ — the requirement is the *existence* of consequence-preview, per PXO-002's P0; its precision is not decided here). This contract is DP-004 applied to the economy and should be validated in the CV-006 digest mock test.

### 9C. Economic risks (each with a structural response the design stage will need to choose or test)

| Risk | Concept-level structural response direction |
|---|---|
| Unbounded accumulation | Single currency + growing drains + no storage stacks: accumulation is *always* priced; no bank-interest loops |
| Chronic deficit death-spirals | Need a floor rule (stability-affecting austerity, bankruptcies as *events* not wipes); SDQ-007 — a rule family to be selected, not decided here |
| Mandatory optimization chores | Drains resolve per turn without daily clicks ( queued/batch); F-019's discipline maintained by keeping the drain-count small (SIM-003) |
| Economy overwhelming all other strategies | DP-001's tests at each design step; standing registers exist independently of wealth (SYS-013's register separation) |
| One mistake destroying agency | Austerity floors *reduce* volatility rather than amplifying it; no compounding debt mechanics at concept level |
| Unavoidable maintenance chores | The re-entry digest (FO-015) reports obligations first; nothing exists that *requires* turning up at boundary T |
| Resources with too little purpose | Few resource classes (candidates: the six *capability outputs*, not raw stacks — exact set SDQ-002); every material class must feed ≥2 line-types or a trade function |
| Economic manipulation/exploits | Section 20's integrity register; anti-multi/anti-collusion defenses are a market-stage requirement, not deferred indefinitely (FO-009's §8 warning; CCR-008) |

### 9D. Multiplayer economy (what's justified, matched to evidence)

Three candidate structures were compared for the *first playable*, using Prompt 3's verified contrasts (P&W listings [FV]; CN mutual-approval transactions [FV-lite]; PU order-books [FV]) and CX-1/CX-3's findings:

| Approach | Player need served | Relationship/standing gain | Explainability | Abuse surface | DB/ops posture | Verdict for Project X |
|---|---|---|---|---|---|---|
| **Directed bilateral trades** (mutual approval; SAs can't automate) | First trades; a novice's reciprocity | High — every trade is a *record* (INT-004) | Very high | Multi-account *transfer* risk only with listing-market posture; needs identity checks | Low: bilateral records | **v1** |
| **Listings market + reference prices** (FO-009's shape) | Price discovery; scale; "who's selling" legibility | Moderate — market postures aggregate | High *if* reference prices are honest; FO-016's transparency surfaces later | High: collusion, wash trading, automation, spoofing — the FO-009 §8 family | Moderate (listing storage, day-end reference jobs) | **Staged — after integrity design** (CCR-008) |
| **Contract/escrow layer** (FO-022) | Long-chain reliability | High for allies | Medium | Escrow abuse; dispute resolution | High | Deferred — with alliance-supply needs |
| **Order-book exchange** (PU-style) | Liquidity at scale | Low–Moderate | High | Real-time integrity; D1 write pressure | High | Deferred (Prompt 3 §11's fallback, not default) |

*The multiplayer economy's first-release shape is therefore the narrowest one that still creates interdependence:* directed trades + structural scarcity (SYS-004) + the trade-credit relationship layer. The market stages in once (a) integrity design exists, (b) write-budget math is in (CCR-010/D-005), and (c) playtests show directed-trade friction in a small world.

### 9E. Conceptual economic flow (no numbers)

**In:** market sales (SYS-005), tiered trade-partners' surplus purchases, passive income from production lines (SYS-003), incoming treaty/alliance contributions (SYS-009/010 as *responses*, never entitlements), and systemic event effects (rare; systemic only). **Generated:** production per turn per active line (capped by line levels). **Out:** upkeep drains (level-proportional), investments (line progress), research programs (Tier C), readiness (SYS-011), alliance contributions (SYS-010, permission-gated). **Exchanged:** bilateral trades and (later) market listings — *both* produce relationship records. **Constraints:** upkeep solvency; order capacity (Administration); sourcing needs (SYS-004); market-integrity rules (SYS-005). Every arrow above is intended to be *provenance-logged* (SYS-016's journal) so the digest can explain it (INT-011).

---

## Section 10 — Domestic politics and governance framework (Deliverable 7)

**Verdict (provisional):** the game needs a *minimal* domestic layer whose gameplay purpose is **stability as a managed resource** — a floor/enabler for everything else — not an institution simulation. This follows FO-005's candidate analysis, F-015's thin demand evidence, Prompt 1 §7.4's light-politics recommendation, and CX-2's rejection logic (RC-3).

1. **Motivations served:** steward-identity (managing a country, not just an economy); governance flavor for planner personas (Mira's secondary motivations; Yuna's future tier); a *pressure* surface that keeps growth from being purely math (FO-014's companion).
2. **Meaningful decisions:** which policy levers sit where (small fixed set, with trade-off axes — the *set of axes* is SDQ-005); how fast to change course (tempo has a cost — reaction-momentum mechanics are a lever-family candidate); how much internal investment the nation accepts vs exports.
3. **Coupling:** stability multiplies economic efficiency mildly and enables/disables *policy-change frequency*; specific recorded acts (broken contracts, austerity overruns) *dock* stability — no global fragility aura (Section 7.5's anti-cascade).
4. **Consequence understanding:** policy changes are digest-recorded with expected direction; changed-at-boundary with cooldown; an unstable nation's digest says what is at risk *before* it hits (provenance of fragility, not surprise collapses).
5. **Political risk:** systemic — mis-set levers that don't match national activity, over-rapid tempo, security posture mismatches. NOT random-model "political events" simulated as token occurrence (AP-003: no hand-authored daily events; systemic randomness only where disclosed).
6. **Complexity control:** v1 ships 1–2 lever axes + the stability state; more only with playtest evidence.
7. **Not a chores wheel:** stability *decays only from specific act classes and negative tempo choices*, never time-passing generosity lows; no "keep the stability meter up by clicking" loops.
8. **Non-political players stay served:** the levers have sane defaults; a never-touching-the-politics player suffers *at most* mild suboptimal multipliers, never forced participation.
9. **Core-set element:** just the stability state + 1–2 levers at v1; expansion deferred to Tier C.
10. **Needs further evidence:** which axes actually matter to our audience; whether stability's floor role *reads* as interesting or as background noise (a CV-003-adjacent read).

---

## Section 11 — Research and technological progression framework (Deliverable 8)

**Verdict (provisional):** research = a small number of national **programs** (not a tree), acting as *convertibility engines* — slow, paid, and limited to "one or two active at once" — whose outputs are capability unlocks and modest efficiency/capacity modifiers, some made *shareable* with allies (a diplomatic hedge). No giant tech trees exist in this concept; the "thousands of nodes" model is rejected for scope (free-first; cost and Prompt 3's complexity discipline) and for the convergence risk the task warns about.

| Proposed direction class | Choices it introduces | Systems affected | Differentiation | Lock-in risk | Newcomer-veteran effect | Convergence risk | Balance burden | Ongoing vs passive | Evidence posture |
|---|---|---|---|---|---|---|---|---|---|
| Economic efficiency programs (drain reduction, yield modifiers) | Program order; share-vs-embargo decisions | SYS-003/005 | Moderate — affects margins, not identity | Low (with share/embargo diversity) | Mild late-adopter gap | Moderate | Medium | Ongoing (degree decisions) | Genre-standard class; safe posture |
| Infrastructure/administrative programs (capacity) | Capacity thresholds (order slots, positions limit) | SYS-002/003/016 | Low-moderate | Low | Low | Moderate | Medium | Ongoing/up-front | FO-013's "research-earned specialization" premise |
| Diplomatic/standing programs (signals, mediation capacity) | *Who you can play as* internationally (mediator posture, treaty-class access) | SYS-008/009/013 | High (identity-bearing) | Moderate (posture sticky) | Small — social practice matters more | Low | Medium | Ongoing | Novel in this genre set — our composition |
| Readiness/defensive programs (defensive posture options, deterrence quality) | *What the nation can defend* (defensive options rather than attack forms) | SYS-011 | Moderate | Moderate | Multiple — deterrence asymmetries | Low | High (war-balance coupling; war-design stage) | Ongoing | FO-011's boundary; uniontouched values |

**Passive vs active progression:** almost everything is an *active* decision (what to run, when to switch, whether to share); the only automatic part is that a *chosen program accrues progress* per turn. No passive research points accrue from idleness — DP-002 tells us presence isn't a resource.

**The open posture:** research might ship in v1 at all only if economy stage reveals a *specific* capability gap that a program fixes; otherwise it's a Tier-C system. This report deliberately places it there rather than assuming "games need tech trees."

---

## Section 12 — Trade and economic relationships framework (Deliverable 9)

Covered under SYS-005 and Section 9D's comparison. The framework's added commitments (all provisional):

1. **Trade is a central strategic activity for most nations** (not an optional minigame): sourcing gaps (INT-003) forces every specialized nation into the trade surface at least occasionally.
2. **Trade strengthens relationships mechanically:** each completed trade writes a *trade-credit*/"reliability" record into SYS-008's pair-state; repeat-reliable trade partners see better terms *from each other* (mutual, not unilateral discounting — no "loyalty discount" magic; the exact terms shape is SDQ — and honesty: whether this is numeric or descriptive-standing is a design question in SDQ-004's register).
3. **Negotiation is structured but textual:** trade offers carry structured fields + a visible history-of-negotiation surface (offer/counter/accept/decline/expiry — no chat dependency; chat is *outside* the game's guarantee).
4. **Abuse prevention is enter-level design, not an afterthought:** identity constraints for trade eligibility (adult-level accounts; *no fresh-account trade highways*); anti-collusion posture from FO-009's §8 family — *these are the integrity stage's work; listed here as requirements, not rules*.
5. **Honor failure has recorded consequences:** a trade agreement's breach is a *recordable act* — credibility cost, not mechanical confiscation (the contracts layer that could enforce confiscation is deferred, FO-022).
6. **No live moderation dependency** in the directed-trade layer.
7. **DB posture:** bilateral trade records only (small); the market stage adds listings + daily reference jobs (Prompt 3's assessment).
8. **Primary-audience fit:** yes — a Mira session can complete one offer+commit; a Tomas session can run negotiations.
9. **Initial concept membership:** directed trades in; market staged; escrow deferred (Section 9D's verdict).
10. **Mapless interconnection:** the dependency map (which nations sell what to which other nations' needs) *is* the trade layer of the world view (FO-013's "pairing as the functional geography").

---

## Section 13 — Diplomacy and international relationships framework (Deliverable 10)

**Verdict (provisional):** diplomacy is the *primary interaction surface* for a large part of the audience — as the mapless world's relationship layer (SYS-008 + SYS-009 + SYS-013) — but it is encoded only where encoding *creates* legible decisions: the v1 minimum is (i) typed bilateral records, (ii) a small set of commitment instruments with exactly ONE mechanical gate (a non-aggression analogue; matching P&W's verified reality [P#3 P22] and FO-006's "minimal gate" note), and (iii) act-recorded reputation events. A full treaty *engine* (typed obligations, escalation clauses, automatic consequences) is deferred not because the concept wouldn't eventually use one, but because its build cost is high and its legibility risk is high (complex "true law" systems are the genre's documented jargon-wall accelerant — F-010's family).

1. **Why negotiate instead of act alone:** structural scarcity needs partners (SYS-004's engine) + protection reliability (the NAP-analogue's mechanical promise) + standing gains via *other players' recognition* of constructive action (SYS-013's records).
2. **What makes an agreement valuable:** it changes game state in legible, *enforced-cheaply* ways: the block-analogue prevents hostile action; the rest creates *records* the world reads (trustworthiness surfaced without a numeric "trust score").
3. **How relationships change over time:** every cited act class writes a state-event (cooldown decay in this concept — frequent Action at boundaries, enough that change is visible *and* understandable via the chronicle, not a mood meter).
4. **How players communicate intentions:** structured offers (treaty drafts with types and scope), the world's visible *postures* (declared stances, national profile statements), and the chronicle record. Back-channel chat exists outside the system and is neither required nor recorded *(communication-science note: former posture that "the game doesn't care where you talk" is recorded as a design boundary rather than as integration)*.
5. **What makes commitments understandable:** every instrument is *one line* in profile + full text one click deep; scope is always *small* (the "no mega-treaties" discipline from Prompt 5 §10B's countermeasures: *selectable-in-scope* commitments).
6. **Betrayal consequences without human arbitration:** exits and invasions write *visible, attributed* record-acts (SYS-008/013; INT-007/009), priced by reputation's decay-and-friction choices in design — final rules belong to a later stage.
7. **Weaker nations can participate:** the *variously-insured* proposals: every relationship record is readable; smaller nations get real standing via behavior (trade-credit, mediation acts) rather than start-power; no "minnow tax".
8. **Independent nations remain viable:** AP-004's rule; independent play reaches all Tier-A systems; alliance membership is an option-class, not a tax.
9. **Interaction with economics and campaigns:** treaties gate campaigns; sourcing flows boost standing; campaigns' settlements *write* relationship and chronicle entries — the triangulated coupling of Section 7.3(2).
10. **What the interface shows about a relationship:** the pair's events (signed/broken/traded), current posture basis, standing-register contributions, and *both sides' declaration text* — private reasoning *stays private* (DP-004 boundary note).

---

## Section 14 — Alliance and collective-action framework (Deliverable 11)

The alliance system's full treatment (sys-010 above) reduces to a small number of proposed capabilities, alongside their *deliberately-not-yet* answers:

| Capability | Player motivation served | Problem it solves | Decision change | Distinct interface? | Admin cost | Solo/casual risk | Abuse potential | Leadership succession/inactivity issue | v1 membership |
|---|---|---|---|---|---|---|---|---|---|
| Shared bank + contribution + tax bracket (1) | Community identity | Coordinationless pooling | Fund strategies a single nation couldn't fund | Bank view (yes) | Low | None (voluntary) | Theft by insiders (audit-first per FO-007) | Founder-key lockout — needs succession rule (SDQ-013) | Yes-minimal |
| Role-limited permissions (2) | Organized groups (Tomas) | Accountability | Who can act publicly for the group | Role edit surface | Low–M | None | Privilege abuse (audit trail) | Succession (same as above) | Yes-minimal |
| Collective campaign designation (3) | Focused common cause | One decision replaces many (FO-012's logic) | Which focus to designate | Banner surface | Low | Mild — nonparticipants see gamed focuses | Fake-focus farming (cap small; SDQ-012's abuse list) | Inactive leader designations rising — auto-expiry rule | No (Tier C) |
| Official bulk actions (4) | Reduce bookkeeping (F-018's debate) | Admin labor | Fewer clicks for legitimate bulk distributions | Bulk-action form | Low | None | Automation blur (keep explicit ban + audit) | n/a | No (Tier C) |
| Member-visible decision log (the **audit-first** differentiator) | Trust | Leadership opacity | Sees what happened | Log tab | Low | None | Logspam (cap rate) | Complete history survives leaders | Yes-minimal |

**Mandatory-alliance risk is rejected in advance (AP-004):** the framework gives independent nations *all* Tier-A systems; alliance membership changes *degree* (larger-scale projects, pooled insurance), not *access*. The design principle that no Tier-B system should require alliance participation is stated so that future spec work can be checked against it.

**Succession & inactivity** are recorded as SDQ-013 because both P&W's internal-accounts problems and genre folk-lore point to founder-lockout as a real failure mode; a rule will be needed but not here.

---

## Section 15 — Military and mapless strategic campaigns (Deliverable 12)

### 15A. Strategic purpose (what conflict is *for*)

In CX-5, conflict is present because (i) some disputes (sourcing captures, reputation challenges, market posture clashes) lack non-violent outcomes otherwise, (ii) the future-tier audience (Kwame-like) needs a real competitive path, and (iii) a *bounded* adversarial layer keeps peaceful strategies honest — deterrence requires a military base to deter *with*. It is NOT for: conquest territory, session-filling adrenaline, or as the metric of national worth (AP-005; CX-4's rejection RC-4 preserved).

### 15B. Mapless campaign structure (candidates, not approved rules)

Conceptual candidates (each would be *specified* in the future war-design stage; none is final here):

- **Declared-objective campaigns:** a campaign is a discrete *object* with a named objective class (market-access dispute; pairing-claim challenge; reputational challenge; protective intervention), a declared participation set, a declared duration-multiple (a whole number of turns), and public record. Objectives *read as relational claims*, not coordinates.
- **Campaign tracks with fronts-as-classes:** abstraction of "fronts" as *activity domains* (economic disruption track, capability-suppression track, standing contest track) rather than spatial tiles — resolution pertains to the *objective's* domain.
- **Influence/posture contests (families of alternatives to violence):** contested-claim mechanisms where *standing weight* (reputation, sourcing roles, coalition breadth) can decide a claim without any armed campaign at all — the peaceful-first escalation ladder.
- **Shared-cohesion campaigns (alliance-scaled):** SYS-010's capability (3) — designated collective focuses; the concept *allows* collective campaigns but leaves the rules to the war-design stage.

**Boundary discipline:** every campaign object must be attendance-tolerant (actions land at boundaries), itself *bounded* (declared end-multiples), and *settled* (ends in negotiated terms or mechanical exhaustion — never a ceasefire-when-bored state).

### 15C. Meaningful decisions (what separates a planned campaign from a random one)

Choice of objective class and timing (declaring at all is reputation-bearing — INT-007); the *shape* of force committed (readiness spending before vs during); coalition composition and its *promise* (who else declared — the biggest diplomatic tell); operational tempo (how many boundary-commitments per turn-cycle); the *settlement posture* — which concessions the attacker will *actually* pursue vs hold up as deterrence, and what the defender will concede to preserve solvency. NOT decided and still open: exact attack types/count; the operational-action resource; resolution mathematics (war-design stage).

### 15D. Time and coordination (2h cadence)

Campaign actions resolve at boundaries; planning horizons are *stated in turns* (declared duration-multiples); coalition coordination happens asynchronously (orders + declarations), never requiring co-presence — the F-017/P&W-cooldown family's lessons honored; nothing about a campaign that *must* happen at a specific wall-clock hour can exist (FO-026/DP-002).

### 15E. Conflict outcomes (candidate consequences; all bounded, itemized)

*Damage classes:* production/output capacity reduction (recoverable over declared turns); sourcing-route interruptions (temporarily "glitched" trade lanes → legible economy digest entries); market-access restrictions (FO-009's blockade-analog, declared); readiness attrition (the attacker's too); *standing classes:* reputation tributes (recorded acts), chronicle entries, standing-register effects; *settlement classes:* concessions (durative restrictions the loser accepts — bounded, declared, expiring), indemnity analogues recorded as *pending-act obligations* (never confiscatory transfers without rules; the war-design stage defines shape), territorial-class outcomes — none (no map; "cession" candidates expressed as *proxy claims* instead, if ever). Not all of these would ship together — the war-design stage chooses a minimal outcome bundle.

### 15F. Fairness and recovery (candidates, further assessment required — not invented rules)

Requirements the future stage must reconcile (recorded here as *inputs*, not decisions): newcomer protection windows (FO-003; adversarially enumerated per FO-017's *method* for the abuse walkthrough); the F-016 finding's "small nations drop out under war pressure" wave; defender-while-absent exposure (SYS-016's queue + declared multi-turn campaigns bound it); CCR-006's boundedness/adrenaline trade-off. **No precise protection/brands/peace/retreat/catch-up mechanic is proposed** — the FO-018 catch-up question and the FO-003/FO-017 protection state machine both explicitly await dedicated design stages.

### 15G. Operations Points — the provisional resource evaluated (D-004's status preserved)

D-004 names OP as *provisional, unapproved*. This report's job was to *compare* a dedicated action-resource model with alternatives, without approving one:

| Option | Shape | Pros | Cons for Project X | Verdict stance (open) |
|---|---|---|---|---|
| **A. National action budget** (OP-like: turn-regenerated, capped, domain-split or unified) | A currency across all "operations" (military, possibly diplomatic/admin) | Clean scarcity; anti-burst (FO-010's premise); per-turn regen respects the clock | Adds a bookkeeping layer to *every* domain it touches; risks unifying diplomacy/military in ways that couple awkwardly (diplomacy-as-budget is unproven); tuning burden | **Open (SDQ-008)** — plausible for the military domain *only* |
| **B. Per-domain order caps with cooldowns** (P&W MAP-shaped for war; simple per-domain counts) | Domain-scoped counts, fixed per boundary | Cheap; tunable domain-by-domain; understandability high | Less elegant for combined-arms plans; multiple caps to explain | **Open** — simplest v1 |
| **C. Commit-based w/o numeric budget** (declare slots and wait; cooldowns gate re-commit) | Slot-completion semantics | Highly legible *causally*; no budget accounting; respects "decisions-over-presence" | Harder to price urgency; burst-farming needs cooldown design (a rule but no arithmetic) | **Open** — conceptually elegant, riskier to balance |
| **D. Hybrid** B-within-A (budget for the military domain; caps elsewhere) | Scoped budget | Focused scarcity where it matters | Coupling complexity between domains grows | Possible, later |

**Recommendation posture (provisional):** boot the military layer with **B** (simplest defensible) and leave the *eventual* action-economy decision — including whether OP becomes real — to the war-design stage with a prototype comparison (A vs B vs C's posture). Nothing here upgrades or retires D-004.

### 15H. Lightweight vs complex campaign simulation (concept-level comparison)

| | Lightweight (declared-object campaigns; outcome-bundle resolution; itemized effects) | Complex (continuous fronts, multi-resolution, victory-point races) |
|---|---|---|
| Development cost | Low-M | High |
| Balance burden | Moderate (few levers) | Very high |
| Abuse risk | Manageable (object-bounded; adversarial enumeration tractable) | High (many interacting timing states; timing/race exploits) |
| Explainability | High (digest-native) | Medium–low (fog everywhere) |
| Maintenance | Low | Ongoing tuning |
| Audience fit | Primary + secondary; bounded scope | Future-tier adrenaline — CX-4's rejected shape |

**Verdict posture:** lightweight campaigns first; heavyweight simulation is *out of the project's identity* (CX-4 rejected at Prompt 5). This is a posture recommendation, not a decision.

---

## Section 16 — National success and multiple strategic paths (Deliverable 13)

**Consistent with DIR-3 [P#5]:** economy + diplomatic standing are the central paths; stability & research are supporting multipliers; military is optional-but-bounded; cultural/informational influence stays deferred (no evidence; would require systems with no demonstrated player need). This report adds the *systems-level* view of what each path needs (which prior reports had only at concept level):

| Path | Goals the player pursues | What matters | Systems that support it | How progress is evaluated | Alliance-dependent? | High-activity-dependent? | How it can be disrupted | Long-run relevance | Exploitation vector | Evidence confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| **Economic prosperity** | Margins, growth, market posture | Production/commerce lines, sourcing position, treasury | SYS-002/003/004/005/016 | Standing register (wealth/price-leadership), personally set milestones | No | No (arcs tolerate absence) | Market shocks, sourcing capture, campaign damage | Yes — compounding is the game | Wash-trading to inflate register (integrity stage's work) | Strong [P#1 §7.3]; composition novel |
| **Diplomatic influence & standing** | Trust, mediation role, bloc role | Treaty-web centrality, reliability record, declared posture | SYS-008/009/013/015 | Standing register (reliability/centrality), chronicle presence | Not required but blocs help | No | Betrayal acts, campaign damage, act-context shifts | Yes — reputation compounds slowly | Staged-act farming (R-06) | Medium-high (P&W treaty-web precedent; mapless composition novel) |
| **Institutional / stewardship identity** (stability & administration) | Stability, a well-run country | Administration line, policy discipline, works | SYS-001/002/003/006/018 | Stability state + register (stewardship); *not* a ladder | No | No | Shock events, over-levered tempo | Moderate — a *floor* role | Stat-stacking to "park" stability | Medium (DIR-3's positional rationale; F-015's thin demand) |
| **Research & capability** | Programs completed, capabilities unlocked | Science line, program order, sharing posture | SYS-007 (Tier C) | *Sharing* yields standing; completion yields capability | Shareable (optional) | No | Program lock-out by economy (see 9C) | Moderate | Program-share collusion (minor; watch) | Thin-moderate (genre precedent; our *modifier-not-ladder* posture is compositional) |
| **Military effectiveness (bounded)** | Deterred threats, successful bounded campaigns | Readiness, coalition standing, operational tempo | SYS-011/012/013 (Tier C) | Standing register (respect); settlement outcomes | Coalitions help | No high-activity requirement in the bounded design | Reputation loss on misuse, economy drains | Yes as *long-run* threat | Fake-war farming (FO-017's list) | Evidence for *demand* strong; design risk high [P#3 §8] |

**Dominant-strategy risk, structurally managed here by:** (i) *register separation* (no single "score" merges the paths — SYS-013's design brief), (ii) DP-001's path-design test applied at every threshold design, (iii) CV-003's perception check before deep design, (iv) the future economy stage's mandate to avoid a single wealth-price lever (SDQ-009's sourcing-competition test). **Not promised here:** that all paths are *tunable-equivalent* — the honest statement per the prompt is that each path must deliver a coherent, worthwhile experience; numeric parity is a later, feasibility-gated question.

**How success is communicated without finalizing the ranking algorithm:** the standing-register *views* exist with names and descriptions; the *measurement weights* behind register placement are deliberately an SDQ-011 (open) — and the *display* question (rank positions vs percentile bands vs non-comparative registries) also stays open; the only commitment asserted is that *one merged scoreboard is not v1's shape* (AP-005's structural test).

---

## Section 17 — Turn resolution and action timing (Deliverable 14)

**The established cadence (restated as the framework's fixed frame):** **one shared global turn every two hours — 12 turns per day — with fixed UTC boundaries.** Players act between turns; the server resolves scheduled flows at boundaries. Nothing in this report is a continuous-real-time design (FO-026/DP-002/AP-007).

**The three-class timing contract (PXO-003's P0, elaborated per action category):**

| Action category | When decided | State change | Needs other player? | Mind-change window | Display before resolution | Prerequisites that can lapse | Result communication | Explanation needed? | Decided rules? |
|---|---|---|---|---|---|---|---|---|---|
| Profile/posture/declared-stance edits (class i) | Any time | Immediate + journal record | No | Immediate (over-write anytime) | Live card | None (always allowed) | Card + chronicle entry if notable | Light | No (SDQ-018's catalog will document) |
| Orders (production/investment/listings/policy requests) (class ii) | Between boundaries | **At boundary** (queued) | No | Editable until boundary | Pending-orders list | Insufficient funds at boundary → order fails *with reason* | Digest line w/ provenance | Yes (per-line) | Order *ordering* inside a boundary: SDQ-018 |
| Trade offers / treaty drafts (bilateral) (class ii-b) | Between boundaries | Pending until counterpart's action | **Yes** (counterpart accepts/rejects/expires) | Withdrawable until response or boundary | Pending-offers view (+partners see own pending items) | Capital insufficiency; relationship-class changes; expiry | Digest + relationship event record | Yes (esp. declines/expiry) | Offer expiry length: open |
| Treaty signing (once offered+accepted) (class iii) | Both sign between boundaries | Record at signature; *consequences* at boundary | Yes | Cannot retract once signed (visible exit route is the only path; exits cost standing) | Signature preview with *consequences block* | Block-type void if counterpart leaves | Chronicle + relationship event | Yes; non-negotiable text | Gate semantics = the minimal gate from SYS-009; full types defer |
| Multi-turn arc orders (develop-line targets, program schedules) (class iii) | Any time | Scheduled commitment | No | Revocable-with-cost (spec design) | Arc view (commitments outstanding) | Funds/runway; program slots | Digest per boundary; arc summary at completion | Yes (whole-arc summary) | Cost-of-revocation: open |
| Military/operations commands (Tier C) | Between boundaries | At boundary | Often (targets, coalitions) | Withdrawable until boundary (fair for defender-readiness) | Declared campaign object | Readiness thresholds; protection states | War-room digest + chronicle | Yes (wartime digests are a first-class requirement) | All rules defer to war-design stage |
| Alliance contributions/roles (Tier C) | Between boundaries | Transfers at boundary; role edits immediate-with-audit | Yes (in-group) | Contribution revocable until boundary | Contribution line + pending | Membership state | Group ledger + member digests | Yes (audit-first log) | Permission matrix: SDQ-012 |
| Campaign settlement approvals (Tier C) | Between boundaries | At boundary/when both consent | Yes | Withdrawable until consent | Settlement draft with terms preview | Campaign-state sanity | Chronicle + bound effects digest | Yes (terms explained) | Terms vocabulary: war-design stage |
| Deferred/async *negotiations* (non-binding threads) | Any time | No state (until instrument created) | Yes | Freeform | Thread view | n/a | n/a | n/a | Out of the mechanical layer by design |

**Timing risks identified (design-stage items, not resolved rules):**
- **Boundary-order races:** two nations' offers hitting the same boundary (trade pairing ordering) — SDQ-018's ordering catalog must be deterministic and documented; the *player-facing* guarantee proposed here: *at the boundary snapshot, all decisions are evaluated again for feasibility; failures produce explained failures, not silent ones* (PXO-002's provenance in the mechanical layer).
- **Last-second coordination pressure:** the framework's answer is the *pending-state visibility* of counterpart-bound items (offers, drafts, settlements are all visible before boundary — timing games stay legible) plus *no* mechanic that rewards being online *at* T-0 (DP-002 check).
- **Missed boundary:** nothing fails catastrophically; queued orders simply resolve with best-available inputs and the digest explains what was impossible and why (provenance again); *no* attendance/streak penalty exists anywhere in this framework.
- **Conflict actions on absence:** Section 15's bounded campaigns + declared-multiples bounds the exposure; the *specific* offline-defense posture is the war-design stage's adversarial enumeration task (FO-017).
- **Duplicate execution / replay drift:** the engine must be idempotent; this belongs to the architecture stage (Prompt 3 §12 tier-1's tick-idempotency item; carried verbatim as SDQ-018's tech clause).

---

## Section 18 — News, feedback, and consequence visibility (Deliverable 15)

**Principle (per DP-004/UXD-001):** every *outcome* the gameplay produced must be attributable; every *major* outcome must be *explained*; small states change silently only when noise-avoidance demands it, and those *are recorded in the journal* so provenance is never lost — silent *visibility*, not silent *causation*.

**Feedback layers (proposed, with the design guidelines per layer):**

| Layer | Purpose | Essential info | Optional info | "Important" recognition | Overload guard | Visibility class |
|---|---|---|---|---|---|---|
| National turn digest (SYS-017) | Own-nation changes with provenance | Per-line deltas + causes; failed orders with reasons | Trend hints | A stability/obligation banner when the state risks the next arc | One screen; detail is a click deeper (PXO-005) | Private |
| Re-entry digest | Absence wrap-up (FO-015) | What changed in your absence, at arcs-resolution granularity | Complete tenure-history links | Pending decision flags; relationship-threat flags | Same digest surface, condensed phrasing | Private |
| Relationship summary | Who moved, and why it matters | Signed/exited/likely-movement records (from SYS-008) | Commentary-free history links | Partner-offer pending badges | Only *your* edges' summary | Private (per-pair detail partner-visible per SDQ-004) |
| World chronicle (SYS-015) | Shared memory of notable events | Typed, quality-gated entries | National-history views | Headline list on digest; per-type filters | Strict entry bar (SDQ-017); *systemic only* | Public |
| Alliance ledger & news (Tier C) | Group bookkeeping legibility | Contributions, decisions, designations | Role-change detail | Pending-group-decision flags | Capped rate; audit-first culture | Group-visible |
| Campaign report (Tier C) | During/after conflict | Turn-by-turn operational digest + settlement terms | Operational *causes* breakdown | Escalation/settlement-pending flags | Digest-native only (no live feeds) | Participants + public chronicle at outcome |
| Historical record (long run) | Legacy: "what my nation did" | National history view (from chronicle + journals) | Accessibility niceties | Specific achievements from SYS-014 (Tier C) | Searchable; no flood | Public (player-name per privacy policy; SDQ-004) |

**Guardrails (deferred decisions noted):** the exact *quality gate* for chronicle entries (SDQ-017); the retention depth of journals (budget-driven — SDQ-003); the *v1* set of these layers (Tier-A guidance: national digest, re-entry digest, relationship summary, chronicle — the rest Tier C).

---

## Section 19 — Progression, momentum, and recovery (Deliverable 16)

**What progression means here (the anti-"just-numbers" discipline):** every permanent development is expressed in *options unlocked* (threshold-driven decision classes), *record earned* (standing registers, chronicle visibility, treaty-web centrality), *capability composition* (emphasis mix), or *dependency structure improved* (resilience in sourcing). A wealthy nation that is alone in the web and has no standing is NOT (structurally) the definition of "advanced" — a deliberate DP-001-supporting sentence.

**Growth-stage progression:**
- *Early capability growth* (turns 1–~tens): line levels from small investments; first trade; first treaty; the first-decision onboarding chain (SYS-018).
- *Medium-term specialization* (arc-scale): emphasis sets; sourcing routes; registration posture; mediation/first-alliance options.
- *Longer-term ambitions* (months): program completions (Tier C), chronicle legacy, standing-register positions, bloc role, campaign history.
- *Unlocking new decisions:* thresholds (Section 8B-5).
- *Increasing interdependence:* standing + supply positions raise counterpart exposure (INT-003's' coupling awareness — *by design*).
- *Uncertainty/setback:* bounded shock classes (sourcing loss; market shock; campaign impairments — all itemized, recoverable per Section 15E's bounded candidates).
- *Recovery/success change:* re-specialization exists (slow, paid); standing decay is slow-and-visible; nothing in the framework consumes *identity* or re-writes history.

**The anti-risks the prompt names, each with this framework's structural posture (open questions preserved):**

| Risk | Framework posture (no numbers decided) |
|---|---|
| Veterans impossible to challenge | The *structural scarcity* engine means veteran strength depends on web position, not parked stats; SDQ-009's sourcing-competition test |
| Newcomers permanently behind | Emphasis/re-specialization + candidate levers (structural niches per FO-018's option list — *no mechanism selected*) |
| Excessive power concentration | DP-001's path-design test at each design step; register separation |
| Progression becomes automatic maintenance | Threshold-driven option-unlocks + standing *decay-by-acts* keeps everything act-linked; DP-002 bans pure-idle growth |
| One bad turn destroying months | Austerity floors reduce volatility (SDQ-007's rule family); bounded campaign effects (16E); nothing confiscates identity |
| Recovery too easy | Re-specialization is slow+paid (FO-013's premise); recovery *takes arcs*, not clicks |
| Resets introduced without justification | Not proposed; FO-024's standing rejection is the project's posture |

**Core-rules vs interface-design resolution split (a standing re-summary):** the *rules* own: solvency floors, re-specialization cost categories, campaign-attachment bounds, standing-decay shape. The *interface/onboarding* owns: digest taxonomy, expectation-setting copy, dependency-map legibility, jargon mirrors. (None decided in numbers here.)

---

## Section 20 — Abuse, exploits, and system integrity (Deliverable 17)

**Discipline note:** per DECISIONS D-003/D-006, none of this is a rule-set; this is the *structural threat map* a later design stage will use. Prompt 3 §8 and Prompt 2's F-029 watchlist are the upstream evidence.

| ID | Risk | Incentive creating it | High-level exploit shape | Legitimate behavior that must survive | Prevention/mitigation candidates | Cost of safeguards | Effect on ordinary players | Before first playable? |
|---|---|---|---|---|---|---|---|---|
| R-01 | Alternate-account resource transfer | Newcomer-boost via self-trades | Chain of exchanges inflating a fresh account | Genuine small-partner trades | Trade-eligibility rules for fresh accounts; velocity/cumulative caps; P&W's verified rule-shape family [P#3 P28 as precedent] | Moderate | Mild (fresh-account verification friction) | Not for the *concept* test (O1 boundary); yes before public economy |
| R-02 | Collusion/automation in a staged market | Price control; margin farming | Wash trading; order spoofing; bots | Honest listing/posting | P&W's automation ban posture [FV-prior]; audit trails; reference-price plausibility checks | High (integrity stage per CCR-008) | Low if rules are simple | Yes before market *stages in* (not for v1 directed trades) |
| R-03 | Fresh-account reputation farming | Cheap standing for a mains' proxy acts | Mini-accounts accumulating reliable-trade credit then "gifted" | Genuine newcomer reliability growth | Registration-age floors on standing-register contribution; act-class rate limits | Moderate | Low | Later (with standing tuning) |
| R-04 | Protection-farming / shield-fishing | Safe staging of attacks | Faking weakness inside protection; farming resets | Real newcomer protection | FO-017's adversarial walk; cooldowns; emerging-state disclosure | Moderate | Low | With the war-design stage (not for v1 vignette) |
| R-05 | Fake wars / term farming (settlement abuse) | Cheap reputation/term harvesting | Staged conflicts; term abuse patterns | Real disputes settled in good faith | FO-011/FO-017 adversarial requirements; repeat-counterpart flags; frequency caps | Moderate | Low | War-design stage |
| R-06 | Standing-register collusion | Manufactured standing | Block-voting-like act coordination; cross-account boosts | Real coalition coordination | One-primary-register-per-act discipline (7.5-2); rate/context limits | Moderate | Low | Later (standing tuning) |
| R-07 | Boundary-ordering exploits | Do X "this boundary" advantage | Timing games at resolution snapshots (pending-state visibility mitigates — Section 17's design check) | Predictable resolutions | Deterministic ordering catalog + snapshot feasibility recheck | Low–moderate | None | Yes (rule of the engine design, pre-concept-test) |
| R-08 | Alliance treasury misuse | Insider theft; leadership lockout | Withdraw-and-vanish; founder-key holding | Trustworthy shared pools | Audit-first ledger (FO-007's differentiator); role gates; succession rule (SDQ-013) | Moderate | Low | With alliance boot (Tier C) |
| R-09 | Group churn advantage (join/leave for perk classes) | Optimize group hopping | Perk-hopping | Real group dynamics | Entry/exit cooldowns on group-derived benefits | Low | Mild | With alliance boot |
| R-10 | Initiatives/public-objective manipulation (Tier C) | Rank/standing hype | Staged public milestone farming | Genuine objective participation | Milestones bound to systemic achievements (SYS-014's posture), not volunteer-vote counts | Low | Low | Later |
| R-11 | Inactivity protection abuse | Free-ride safety | Perma-vacation as armor | Real absence handling | Vacation-class states with exits and preview-visibility per genre precedent/no new rules *decided here* (noted as a war-design/open-classed item) | Moderate | Low | War-design stage |
| R-12 | Loopholes in turn-resolution order | Sequence-dependent abuse states | Cross-order race conditions | Order-independent fairness expectations | Deterministic ordering catalog (SDQ-018); sim-integrity tests | Moderate | None | Architecture stage |

**Rule-of-thumb the design stage is handed:** where a safeguard's cost exceeds the mechanic's value, *simplify the mechanic*, don't armor it — several candidates above (R-03, R-06) are examples where small mechanics might be *cut* instead of hardened (the SIM register's philosophy).

---

## Section 21 — Simplification and alternative mechanics (Deliverable 18)

The simplification register (SIM-xxx). Each entry: *full-complexity approach → simpler alternative · value kept/lost · depth kept/lost · learning impact · balance/exploit impact · build/maintenance impact · when the simple version is enough · prototype-comparable?*

| ID | Full version | Simpler alternative | What's kept / lost | Depth | Learning | Balance/abuse | Build/maintenance | Simple-is-enough when | Prototypable |
|---|---|---|---|---|---|---|---|---|---|
| SIM-001 | Multiple specialized currencies/resources per domain | **One currency + few material classes** | Kept: allocation tension, scarcity; lost: "economy zoo" flavor | High kept | Much easier | Fewer exploit surfaces | Lower | v1 *and possibly forever* (retain only if real need emerges) | Yes |
| SIM-002 | Cities/buildings/population | **Development lines** (SYS-003) | Kept: compounding, identity; lost: spatial anchoring (map-independent anyway) | High kept | Much easier | Lower | Much lower | v1, indefinite | Yes |
| SIM-003 | Many drain classes | **3 drain families** (sustain services, readiness, works) | Kept: drains-as-decisions; lost: fine texture | High kept | Easier | Easier to keep visible/honest | Lower | v1 | Yes |
| SIM-004 | Full policy-lever matrix + approval dynamics | **1–2 levers + stability state** | Kept: governance feel, floor role; lost: political texture | Moderate kept | Easier | Fewer axes to tune | Lower | v1; expand only on evidence (F-015) | Yes |
| SIM-005 | Big tech tree | **Programs (2–3 at once max)** | Kept: compounding choices; lost: optimization breadth | High kept | Easier | Fewer convergence paths to check | Lower | Tier C boots | Yes |
| SIM-006 | Event/notification subsystem | **One journal + digest renderer** (FO-002 machinery reused by FO-015's view) | Kept: everything except custom notification classes; lost: nothing material | ~ All | Easier | Same | Lower | v1 | Yes |
| SIM-007 | Standalone rankings UI | **SYS-013 standing-register displays (doubles as rankings)** | Kept: goal visibility; lost: separate vanity top-list | High kept | Easier | Fewer leaderboard-collusion surfaces | Lower | Likely permanent (Tier C re-evaluation only) | Yes |
| SIM-008 | Order-book exchange | **Directed trades, then listing market** | Kept: exchange function at each stage; lost: liquidity tech | (staged) | Much easier | Far smaller abuse surface before market | Much lower (staged) | Until integrity work is defensible (CCR-008) | Yes |
| SIM-009 | Full treaty engine (typed obligations, auto-enforcement) | **NAP-analogue + typed records** | Kept: commitments as objects, minimal enforcement; lost: fine-grained enforcement | Moderate kept | Easier | Simpler arbitrage | Lower | v1 | Yes |
| SIM-010 | Continuous war simulation | **Declared-object campaigns with itemized bounded effects** | Kept: consequential conflict; lost: tactical depth | (deliberate) | Much easier | Fewer timing/race exploits; FO-017 tractable | Lower | Concept's *identity* posture (CX-4 rejected) | Vignette-testable (15-S3) |
| SIM-011 | Full alliance permission matrix | **Role-lite + audit log** | Kept: accountability; lost: fine-grained group design | Moderate kept | Easier | Simpler to audit | Lower | Until density justifies more | Yes |
| SIM-012 | Hand-authored events | **Systemic emergent stir only** | Kept: world texture via systemic events; lost: curated narrative timing | (identity posture — AP-003) | Easier | No editorial calendar to keep | Lower | v1 and *standing posture* | n/a |

**Prioritized simplifications (strongest first):** SIM-002 · SIM-001 · SIM-006 · SIM-007 · SIM-003. Each of these is a *permanent* posture unless player need emerges against it — not just v1 expedience (the genre's precedent is that simple turn-native designs historically stand the test of NS's micro-decision longevity [P#4 NS-family] — though NS's *twice-daily* cadence is NOT our cadence, a caution against over-generalizing its lesson).

---

## Section 22 — System dependencies and open questions (Deliverable 19)

The dependency register. **Priority legend:** P0 = must be resolved before the affected system can be specified responsibly; P1 = important for the next design stage; P2 = can stay open while the core is tested; Deferred = not needed for this stage.

| ID | Question | Why it matters | Systems affected | References | Current hypothesis (if any) | Confidence | Cheapest investigation | Consequence if unanswered | Priority |
|---|---|---|---|---|---|---|---|---|---|
| SDQ-001 | Final development-line set + threshold model (how many lines; what a "level threshold" unlocks) | The whole progression architecture hangs on it | SYS-001/003/004; tiering overall | FO-013/014; §15A-E1 of [05] | ~4–6 lines; option-class thresholds | M | Paper design + economy-stage review | Design churn; each later stage redoes it | **P0** |
| SDQ-002 | Material-class list for trade (what actual "things" get traded) | Trade layer needs concrete goods; every material needs ≥2 uses | SYS-004/005 | §9C (few-purposes rule); FO-013 pairing logic | Few classes (c. 6–10) each crossing ≥2 lines | M–H | Economy-stage comparative pass | Trade layer can't be styled; CCR-002's scope drift risk | **P0** |
| SDQ-003 | Journal/chronicle retention depth and write budget | SYS-016/017 cost; D-005/CCR-010's write math | SYS-015/016/017 | D-005; CCR-010; Prompt 3 §12 tier-1 #1 | Delta-timestamped text; retention windows | H (posture), no numbers | Architecture-stage arithmetic (D-005's task) | Digest/v1 commitment may fail on free tier | **P0** |
| SDQ-004 | Information-visibility policy: what of relationships, terms, economics, and history is public/partner-private/private | Integrity & mystery balance; DP-004 boundary note implementation | SYS-008/009/013/015/017 | FO-004's unresolved policy; Prompt 3 §12 tier-2 #5; DP-004's boundary note [05] | Public relations events; partner-visible terms; private internal math-offset | M | Small-v1 policy table draft + CV-006 reaction probe | Trust/leakage failures; rework after public data exists | **P0** |
| SDQ-005 | Exact policy-lever axes + stability mechanics (what moves stability; what it multiplies) | SYS-006's scope; the floor role's shape | SYS-006/003 | FO-005; §10 | 2 axes at v1; stability gates tempo, not output | M–L | Economy/politics-stage comparative | Arbitrary-feeling politics layer (F-015-level risk materialized) | **P1** |
| SDQ-006 | Research program classes + share/embargo mechanics | SYS-007's shape if booted | SYS-007/008 | §11; DIR-3 | 2–4 classes; shareable via treaty-textured records | M | Paper design + economy-stage check | Stalled Tier-C boot; "decorative research bar" failure mode (7.4 audit) | P1 (needed only if SYS-007 boots) |
| SDQ-007 | Bankruptcy/solvency floor rule family (what happens at negative treasury) | INT-001's death-spiral answer | SYS-002/003/016 | §9C | Austerity multiplier + event class; no wipes | M–H | Economy-stage rules + sim check | Newcomer-unfriendly deaths; balance patch-later pain | **P1** |
| SDQ-008 | Military action-resource model (OP vs domain-cap vs commit slots) | SYS-011/012's operational layer; D-004's eventual resolution | SYS-011/012/016 | D-004; §15G | Simple domain caps first (Verdict posture) | M | War-design stage + prototype comparison A/B/C | Burst-exploits; D-004 unresolved indefinitely | **P1** (a blocker for war design, not for the concept test) |
| SDQ-009 | Sourcing-competition structure (the ≥2-routes rule's mechanical form; how structural scarcity is actually priced) | DP-005's bound; CV-003's substance | SYS-004/005 | FO-013; §7.3(1); §15A's "all-meta expensive" intent | Route-classes with scarcity floors; market as price signal | M–L | Economy-stage comparative + CV-003 probe | Chokepoints or autarky-drift; biggest DP-001 hazard | **P0** |
| SDQ-010 | Reputation act-taxonomy (what counts as an act; register routing; decay-by-acts shape) | SYS-013/015's integrity; INT-006's noise discipline | SYS-013/015/008 | §7.5(2); §20 R-06 | Small taxonomy; one-primary-register rule | M | Paper design + CV-003/V-10 alignment | Standing inflation; the whole diplomat path's currency compromised | **P0** |
| SDQ-011 | Standing-register metrics + display class (numeric vs descriptive; decay/permanence) | "How others see me" legibility; newcomer-fairness tension (7.3-2) | SYS-013/014 | §19 anti-risks; F-012; V-10's alignment | Bands/percentiles over raw ranks; slow visible decay | M–L | Design-stage mock + CV-003/CV-001 wordings | Either gatekeeping or scoreboard-domination | P1 |
| SDQ-012 | Alliance permission-minimum set + audit-log shape | SYS-010 v1 freeze | SYS-010 | FO-007; §14; §20 R-08 | One tax bracket + 2–3 roles + full ledger | M | Requirements-first paper design + abuse walkthrough | Redesign post-boot; theft incident risk | P1 (before alliance boot) |
| SDQ-013 | Alliance succession/inactive-leader rule | Group-death failure mode | SYS-010 | §14 | Auto-transfer on inactivity threshold + member vote | M | Requirements-first paper design | Founder lockouts; defunct-asset pools | P1 (before alliance boot) |
| SDQ-014 | Treaty-type minimum set (which types at v1 beyond the block-analogue) | SYS-009's enumeration; FO-006's unresolved question | SYS-009/008/013 | FO-006; §7-INT-007 | Block + 1–2 promise types; no more at v1 | M–H | Requirements-first paper design | Type inflation (jargon wall) or thin diplomacy | P1 |
| SDQ-015 | Trade-credit/relationship-terms shape (numeric vs descriptive; how reliability compounds) | SYS-008/005's relationship gains | SYS-005/008/013 | INT-004; SDQ-004's family | Descriptive state + pair-history; no unilateral loyalty discounts | M | Economy-diplomacy pair-stage design | Trade-as-loop decays into a transaction queue | P1 |
| SDQ-016 | Emphasis-change mechanics (cost, tempo, reversibility) | SYS-001/004's flexibility contract (§8C) | SYS-001/003/004 | FO-013's slow re-specialization posture | Paid + turn-distance-based (both) | M | Economy-stage comparative + playtest | Permanent-locks (DP-001 violation) or trivial re-specialization (scarcity die-off) | **P0** |
| SDQ-017 | Chronicle-entry quality bar + entry taxonomy | SYS-015's signal/noise; SDQ-004's class rules | SYS-015/017 | §18 guardrails | Typed entry classes; minimum-grade gate | M | Sample corpus draft + playtest read-rate | Either silence (dead chronicle) or noise (flood) | P1 |
| SDQ-018 | Boundary-resolution ordering catalog + idempotency pattern (which queue order; how failures recheck; replay determinism) | SYS-016's integrity (R-07/R-12); engineering contract for digest truth | SYS-016 all-dependency | §17 risks; Prompt 3 §12 tier-1's tick-idempotency item; CCR-010 | Deterministic declared-order catalog; snapshot recheck; fail-with-reason | H (design), M (tech) | Architecture-stage spec + integrity tests | Digest lies; race exploits | **P0** |

**Dependency chain in one line:** SDQ-001 → SDQ-002 → SDQ-003 (write math) → SDQ-018 (engine contract); SDQ-004/010/011 are the *information* backbone (digest treaty layer); SDQ-009/016 are the *economy structure* pair; SDQ-007/005 fold after those; SDQ-006/012/013/014 are Tier-C boot prerequisites, and SDQ-008/015 belong to the war/market stages respectively.

---

## Section 23 — Mechanics opportunity register (Deliverable 20)

Mechanics-level opportunities with concept-level substance (not approved; MO-xxx family). Statuses: RE = recommended for exploration; OP = optional; DF = deferred; RJ = rejected.

| ID | Name | Player problem/motivation | Conceptual mechanic | Systems | Strategic benefit | Evidence / references | FO/PXO links | Complexity | Ops burden | Dependencies | Exploit side | Side effects | Validation path | Status | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MO-001 | **Development-line emphasis weights** | "Identity choice" needs a *mechanical* home; avoids universal builds | Weight allocation across lines shifts efficiency multipliers; act-recorded changes | SYS-001/003/004 | Visible, legible specialization without hard locks | DP-001; F-020's anti-narrow | FO-013 | M–H | M | SDQ-001/016 | Reset-abuse if free (SDQ-016's answer) | Fewer "plain" buildspossible | CV-003; economy-stage sims | **RE** | M |
| MO-002 | **Structural pairing niches** | Interdependence must be structural, not social | Gap-classes solvable only via partners; pairing bonuses where 2 nations' emphasis complement | SYS-004/005/008 | Trade becomes *the* multiplayer engine | FO-013's pairing analysis; DP-005 | FO-013 | M–H | M | SDQ-002/009 | Collusion; chokepoint bullying | Dependency-fragility (CCR-005) | CV-003; economy-stage design | **RE** | M–H |
| MO-003 | **Provenance as a journaling system** (not tooltips) | F-010's churn family's systemic answer | Engine emits cause-records with every state change; digest renders them | SYS-016/017 (+ all) | Trust; dispute reduction; CV-006's value anchor | FO-002; DP-004; PXE-013 | FO-001/002; PXO-002/005 | M–H | M–H (write budget) | SDQ-003/018 | None (integrity-positive) | Cost per line (budget) | CV-006 | **RE** | H |
| MO-004 | **Relationship typology + visibility classes** | "Where do I stand with whom" without mood meters | Typed pair-states (trade-credit/grievance/promise/posture) with per-class visibility | SYS-008/009/013 | Diplomacy becomes readable to newcomers | FO-004; P&W treaty-web precedent | FO-004/006 | M | L–M | SDQ-004 | Dox-spoofing via staged acts (R-06's discipline) | Privacy tension (DP-004 boundary) | CV-006; CV-002 | **RE** | M |
| MO-005 | **Settlement-term vocabulary** (conflict ends in offered terms) | War's *story* as gameplay; defender justice | Post-resolution term packages (concession/indemnity/posture) selectable/negotiable | SYS-012/008/013/015 | Conflict produces *records*, not just numbers | FO-011; UXD-004 | FO-011/017 | H | H | War-design stage | Term-abuse (R-05) | Boundedness risks toothlessness (CCR-006) | War-design adversarial walkthrough | **RE** (staged) | M |
| MO-006 | **National chronicle as a gameplay object** | Legacy must be *findable*, not vibes | Nations' history views auto-assembled from journals; milestone marks | SYS-015/013/018 | Identity/long-run retention driver | PXE-015's opposite; §12A-5 | FO-004's "changes over time" | L–M | L | SDQ-003/017 | Name-squatting/chronicle spam (SDQ-017) | Retention cost | CV-001/002 | **RE** | M–H |
| MO-007 | **Standing registers (plural, named)** | No single score (AP-005); plural paths legible | Multiple public registers (economic standing/reliability/respect/stewardship), bands not raw ranks | SYS-013/014 | Distinct success meanings; newcomer-friendlier | DP-001; F-020; F-012 | — | M | M | SDQ-010/011 | Block-vote farming (R-06) | Register-homogenization drift | CV-003; V-10 alignment | **RE** | M |
| MO-008 | **Arc-length orders** (multi-turn commitments) | Long-arc play for 40-min sessions; short sessions *lose nothing* | Queue multi-turn directives with visible milestones; revocable-with-cost | SYS-016/003 + all | Absence-tolerant planning; DP-002-native | FO-015's queue-first posture; DP-002 | PXO-003 | M | L | SDQ-016/018 | Commit-and-revise abuse (small; revocation cost covers) | Complexity of pending-state display | CV-004 | **RE** | H |

**(No mechanics-opportunity was invented that lacks an evidence hook; the two "recipes" (MO-001/002) are the direct mechanic-level expressions of FO-013's open questions, flagged to the economy stage — which may reject or morph them.)**

---

## Section 24 — System framework recommendation (Deliverable 21)

### A. Recommended core systems (the smallest set)

**SYS-016 Turn Engine & World Clock** — the world's beat; the timing contract (PXO-003) lives here and everything else depends on it. · **SYS-002+003 National Economy** (treasury/production/development-lines/drains) — the compounding fantasy's spine. · **SYS-004 Specialization & Structural Scarcity** — the multiplayer gravity engine (FO-013's deployment). · **SYS-005 Trade & Exchange (directed first)** — the interdependence engine's transaction surface. · **SYS-017 Digest & Explanation** — DP-004/UXD-001's medium. · **SYS-018 Onboarding & First-Decision** — the entry contract. · Plus *records* systems: **SYS-001 Nation Profile, SYS-008 Relationships, SYS-009 Treaties (minimal), SYS-013 Reputation (act-driven), SYS-015 Chronicle**. This set *is* the CX-5 concept expressed as machinery; each is essential because each carries a pillar's load directly (DP-001's SDQ-009/016, DP-002's SYS-016/MO-008, DP-003's SYS-008/015, DP-004's SYS-017/MO-003, DP-005's SYS-004/005, DP-006's deferred-to-war-design SYS-011/012).

### B. Supporting systems (valuable, but do not dominate scope)
SYS-006 Policy & Stability (minimal v1) · SYS-010 Alliances (minimal, audit-first) · SYS-007 Research (Tier C boot) · SYS-014 Rankings/Objectives (mostly *via SYS-013*) · SYS-011 Military capability/readiness (minimal; the vignette carries SYS-012's concept test first).

### C. Deferred systems
SYS-012's real campaign rules (war-design stage) · SYS-010's full governance (when density justifies) · SYS-007's full program set · SYS-011's real combat math · all FO-020/021/022/023/019 watch-list areas · account meta-progression (rejected for now).

### D. Proposed player-decision loop
Section 4A's six-step loop; MO-008's arc-orders connect session-scale to arc-scale; the *loops* defined in 4B interconnect through the journal (SIM-006). Explicitly: the loop is *identical* for short and long sessions; only the number of executed decisions differs.

### E. Proposed long-term progression loop
Development lines → thresholds unlock decision-classes → standing-register movement → chronicle record → treaty-web centrality → (Tier C) program completions & campaign history — a chain of *legible, attributable, mostly act-linked* progression (Section 19's posture). Re-specialization keeps the topology open (SDQ-016).

### F. Proposed interaction structure
The five load-bearing couplings (Section 7.3): economy↔specialization; acts/treaties/settlements↔reputation; conflict↔everything (bounded, itemized); transparency↔journal; alliance↔collective surfaces (Tier C). Every other interaction is either a digestive one (into SYS-008/009/013/015 records) or the timing contract (SYS-016).

### G. Key unresolved questions
SDQ-001/002/003/004/009/010/016/018 (P0s) and the discussed P1s — plus the concept-level validations (CV-001…006) that gate everything. Note two *external* dependencies beyond this report: the dedicated war-design stage (which owns FO-010/011/017's specification), the architecture/economy stage (which owns D-005's write math and FO-009's integrity posture), and the *user's* future authorization for both — this report does not schedule either.

### H. Rationale (why this framework fits what it must fit)

- **The concept (CX-5):** the system set *is* CX-5's pillar-load mapping — no pillar lacks a system; no system lacks a pillar; the treaty/war/market shapes deliberately use our own vocabulary per AP-008 (structure inspiration allowed, no copied distinctive combos).
- **Primary audience (Prompt 4):** decision-batched, short-session-compatible, absence-tolerant, identity-bearing, legible (each pillar's load lands in Tier A/B systems; nothing requires scheduled presence).
- **Two-hour cadence:** timing is a *contract* (SYS-016's three classes), not a presence demand; boundaries are the only mechanical moment (DP-002's posture throughout).
- **No-geographic-map:** the relationship network (SYS-008) + market/dependency map (SYS-004/005) + chronicle (SYS-015) *are* the world; zero systems require coordinates; campaigns are objective-declared, not spatial (Section 15B).
- **Manageable complexity:** 18 systems carried by a staged boot of 5 Tier-A build units + 5 Tier-B systems + 7 Tier-C entries; the SIM register's 12 simplifications are *permanent postures* where evidence supports (SIM-001/002/006/007 especially); every digest-explained surface honors AP-006 (no unexplained complexity) rather than hiding rules behind depth.
- **Low-cost operation:** digest/journal reuse (SIM-006); directed-trade-first economy (SIM-008); no content-ops dependency (SIM-012/AP-003); the write-budget P0 (SDQ-003/018) is explicitly an architecture-stage gate, not assumed away.
- **Multiple approaches to success:** standing registers (MO-007), emphasis weights (MO-001), and structural scarcity (MO-002) are the *mechanical* load-bearers of DP-001; CV-003 is the perception gate.

### I. Confidence statement

**What the research supports (evidence-backed foundations):** the genre's drainage/compounding discipline (FO-014, F-019), the market-integrity requirement (FO-009's family), the treaty-objects minimal-gate reality (P#3 P22 verified), the digest/teaching churn answer (F-010 family), P&W's turn-locked action-budget precedent pattern (FO-010 [FV prior]), and the audience/session-shape evidence [P#4]. **What is a reasoned posture (composition, not observed):** the specific development-line abstraction, standing-register plurality, settlement-vocabulary conflict (UXD-004 — the weakest-evidence differentiator, flagged as such), escalatory impact bounds, and the framework's *specific* simplification postures. **What is unvalidated entirely:** the mapless world's comprehension (CV-002), cadence acceptance (CV-004), multi-path perception (CV-003), resonance (CV-001) — no CV/V item has been executed (Prompt 4 Section 19's V-1…V-10 all open; Prompt 5 Section 17's CV-001…006 all open; none is marked complete here). This framework is a *research-informed proposal*; nothing in it has been playtested, simulated, or approved.

---

## Section 25 — Conclusion

This report turns CX-5 from a concept into a *machinery proposal*: 18 systems, 14 interactions, 18 open dependency questions, 8 mechanics opportunities, 12 simplification postures, and a 4-tier boot/staging plan — all provisional, all decision-log-clean, all consistent with the confirmed constraints (2h shared turn, mapless, persistent, free-first, original identity) and with the provisional pillars DP-001…006 and anti-pillars AP-001…008 as currently recorded.

**What this phase establishes:** the high-level gameplay architecture — which systems exist, why, how they relate, what must be answered before detail, and what needs no answer yet.
**What remains open:** everything the P0/P1 SDQ list and the CV/V validation plan wait for; nothing here is approved, playtested, or final.

The framework's own honesty note: the *larger* risk it carries is not any single system's design but the accumulation posture ("18 systems" is many). Its answer is staged booting (Tier A first, B with concept test, C by evidence) and the simplification register's *cut* bias — if the user's validation experiments return weak signals, the right response is *removal*, not patch-layering (CX-1/CX-3 fragments remain on the shelf as narrowed fallbacks, just as Prompt 5 recorded).

---

## Section 26 — Source register

No new external research was performed for this report; every external-fact claim traces to a prior report's register, cited by stable IDs. (Source-family mapping — the prior reports' own registers remain authoritative; navigation is via the referenced documents.)

| Ref | Internal source | What it grounds in this report |
|---|---|---|
| [SR-1] | [stage-1/01_competitor_research.md](01_competitor_research.md) | Genre conventions ([P#1 §7] analysis family): turn cadence norms, abstract-war analysis, mapless-precedent analysis, alliance-tooling norms, and §7.7's abstract-war posture boundaries ([P#1 §7]'s genre-convention findings) |
| [SR-2] | [stage-1/02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) | F-001…F-029 findings cited (community gravity F-001/F-003b, chore fatigue F-019, jargon wall F-010, catch-up gap F-012, admin burden F-018, narrow success F-020, exploit families F-016/F-017, watchlist F-029); O-x opportunities |
| [SR-3] | [stage-1/03_feature_comparison_opportunity_analysis.md](03_feature_comparison_opportunity_analysis.md) | FO-001…FO-027 (statuses preserved); FO-009's §8 integrity warning; the complexity/dependency assessments; verified market/war/treaty facts (P22's NAP-only enforcement; P20/P21/P24…) |
| [SR-4] | [stage-1/04_target_audience_and_player_experience.md](04_target_audience_and_player_experience.md) | Personas; session-shape evidence; PXO-001…022 (P0s especially); PXE risk register; PR-1…10; V-1…V-10 all open |
| [SR-5] | [05_core_game_concept_and_design_pillars.md](05_core_game_concept_and_design_pillars.md) | CX-5 concept; FX/DP/UXD/AP/CCR/CV/DIR/H/RC families; first-playable boundary E1–E6/S1–S5/O1–O6; trade-offs (§16B); staged-economy compromise |
| [SR-6] | [DECISIONS.md](../DECISIONS.md) | D-001…D-006 (none added here; D-003/D-006's input-only discipline governs everything above) |
| [SR-7] | [AI_CONTEXT.md](../AI_CONTEXT.md) | §1–2 confirmed constraints; §4 claim-type discipline; §7 open-question recap |

**New ID families this report:** SYS-001…018 · INT-001…014 · SDQ-001…018 · SIM-001…012 · MO-001…008 · R-01…R-12 (integrity-risk register, appended hereunder as a family rather than inside earlier registers). Each family is internally unique; existing families (F/O/FO/PXO/PXE/PR/V/CX/FX/DP/UXD/AP/CCR/CV/DIR/H/RC/D) were reused where they apply and never renumbered.

---

## Section 27 — Handoff to the next research phase

### Project snapshot for a fresh AI
- **What Project X is:** a persistent, multiplayer, browser-based nation-strategy game; a shared **one-turn-every-two-hours** clock (12/day, UTC); a fictional **mapless** world as a symbolic relationship network; free-first, small-team, AI-assisted build; original identity; **no design finalized, no code**; Stage 1 (research), prompt 6 of 8. See [AI_CONTEXT.md](../AI_CONTEXT.md) §1–2.
- **What Prompt 6 established (proposed, not approved):** the 18-system gameplay architecture (SYS-001…018), its 4-tier prioritization (Tier A: 5 build units covering 6 IDs; B: 5; C: 7 entries; D: excluded areas), the 14-interaction map (INT-001…014), the SDQ dependency register (SDQ-001…018), the SIM simplification register (SIM-001…012), the MO mechanics register (MO-001…008), the R integrity-risk register (R-01…012), and the Section 17 three-class turn-timing contract — all reconciled against the provisional CX-5 concept, its DP/AP pillars/anti-pillars, and the CV-001…006 + V-1…V-10 validation plans (all still open and unexecuted).

### Read first (in order)
1. [AI_CONTEXT.md](../AI_CONTEXT.md) §1–2, §4, §6, §7
2. [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md)
3. [DECISIONS.md](../DECISIONS.md) (D-001…D-006)
4. [Prompt 5's report](05_core_game_concept_and_design_pillars.md) in full (CX/FX/DP/UXD/AP/CCR/CV/DIR/H/RC families) — noting its correction-pass state (verified this session)
5. [Prompt 6's report](06_core_gameplay_systems_and_interactions.md) in full — the SYS/INT/SDQ/SIM/MO/R families established here
6. Prompt 3 §10's FO register (statuses), Prompt 4 §19's validation register (V-1…V-10, all open)

### What a future AI must NOT assume
- That CX-5, this framework, any SYS/INT/SIM/MO item, or the three-class timing contract is *approved* — everything is provisional until an owner decision records it (DECISIONS.md D-003's rule; no such entry exists after this prompt).
- That any SDQ belongs resolved — the P0s (SDQ-001/002/003/004/009/010/016/018) are open on purpose; the question count is accurate (18), not "complete."
- That OP (D-004) was approved or retired — §15G evaluated four models and recorded the decision as open (SDQ-008); the provisional status is untouched.
- That the 2h cadence means anything but one global turn every two hours, 12/day (many prior-report phrasings were corrected; don't reintroduce confusion).
- That validation experiments know their results — CV-001…006 and V-1…V-10 are all unexecuted plans.

### What the next authorized research task should address
Per the pipeline's remaining Stage 1 prompts (7–8, order user-authorized), the two highest-bound candidates this report flags are: (a) **the economy design structure stage** — the SDQ-001/002/003/009/016 cluster, resolving the market shape question (FO-009/FO-013/FO-022 open cluster; CCR-008's integrity-chain dependency; Prompt 5 §21's flagged top candidate), and (b) **the security/anti-cheat/fairness stage** — the §20 R-register's design work (FO-009/FO-017's adversarial requirements), Prompt 3's own suggested handoff. **The order is the user's call; do not begin either without explicit authorization.** Whichever runs, it must reconcile against this report's system framework — *provisional* status intact — and the DP/AP checks every future feature proposal requires (Prompt 5 §21's standing instruction).

---

*(End of report. Not approved design; the reader is reminded of DECISIONS.md's D-003 finding/opportunity-only rule and [AI_CONTEXT.md](../AI_CONTEXT.md) §4's claim-type discipline.)*
