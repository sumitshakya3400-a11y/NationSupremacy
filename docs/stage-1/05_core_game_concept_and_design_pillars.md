# Stage 1, Prompt 5 — Core Game Concept, Unique Identity, and Design Pillars

**Report:** v1.0 · 2026-10-22 · author: Prompt 5 session
**Scope:** Concept-level definition of Project X: what it is, what is distinctive about it, what fantasy it offers, who it serves, which systems form its foundation, which principles govern future development, and which directions stay outside the project's identity. This is NOT a game design document. No mechanics, values, interfaces, or implementation are finalized. All recommendations are **provisional** until a design stage records an approval in [DECISIONS.md](../DECISIONS.md).
**Prerequisites verified:** Prompt 4 report exists and is complete (audience strategy registered [P#4]); DECISIONS holds D-001…D-006; Prompt 1–3 reports read in relevant sections this session.

---

## Section 1 — Executive summary

Project X's recommended concept (**CX-5 "The Community of Nations"**, working label): a persistent, browser-based nation-strategy game on a shared two-hour world clock in which players *steward a developing nation inside a community of interdependent, rival nations*, and where the world is organized as a legible **relationship network** (nations + treaties + market + alliances + institutions) instead of a geographic map.

- **Central fantasy (recommended):** stewardship of one nation among many — first a developer/manager of your own state, growing over time into a strategist and negotiator whose country has *standing* in a world other players help shape. Two supporting entry fantasies — the nation-builder and the strategist-at-the-table — funnel into the same loop.
- **Why this concept wins:** it is the only candidate that simultaneously (a) serves Prompt 4's evidence-backed primary audience (steady-check-in multiplayer strategists [P#4]), (b) makes multiplayer gravity structural rather than optional through trade interdependence (FO-013/FO-009), (c) turns the mapless constraint into the game's organizing identity (FO-004/FO-006), and (d) stays buildable by a small team on a free-first stack (Prompt 1 §6).
- **What carries the experience:** one core loop (observe → decide → commit → resolve → interpret → adapt) that a 5–15-minute session [P#4] can honor, plus shorter-arc strategic cycles that give the world meaning between sessions.
- **Six provisional design pillars** (DP-001…DP-006) and **eight anti-pillars** (AP-001…AP-008) are proposed as the concept's constitution. None is approved.
- **Five proposed differentiators** (UXD-001…UXD-005) are grounded in prior findings; none claims industry uniqueness beyond what evidence supports ("the game that explains itself", the relationship-network-as-world, absence-respecting sessions, settlement-first conflict vocabulary, adversarially-designed protection).
- **Six debate questions are left open and validated in Section 17 (CV-001…CV-006):** concept resonance with real players, mapless-world comprehension, multi-path perception, cadence acceptance, success-framing preference, and provenance trust. Of Prompt 4's V-1…V-10 register, the design-blocking subset (V-2, V-4) plus CV-001…CV-006 themselves are next-stage items; V-3/V-5/V-6 route to beta/pre-launch, V-7/V-8 to beta, V-9 to roadmap, V-10 to post-v1 (mapping in Section 21). None has been executed.

Rejected directions retained in Section 18: a geographic world (FO-025 confirmed), a war-first concept (CX-4), a politics-first sim (CX-2), an economy-first optimizer island (CX-1).

---

## Section 2 — Scope, method, and evidence limitations

**Method.** This report is a synthesis-and-concept task, not a new primary-research task. It reads the four prior stage reports plus the continuity files, extracts what materially constrains a concept, generates candidate directions, evaluates them with a stated weighting, and commits to one concept with pillars and risk/validation registers. Where a claim leans on primary evidence, it cites the prior report's stable IDs (F-xxx, O-x, FO-xxx, PXE-xxx, PXO-xxx, PR-x, V-x) rather than re-deriving it. No new external web research was performed this session; no new external sources are introduced.

**What this report can legitimately establish:** conceptual coherence, fit with documented findings, feasibility posture, and hypothesis structure for later stages.
**What it cannot establish:** real player interest, mechanical balance, market viability, or the correctness of any pillar — those belong to Section 17's validation plan and later stages.

**Evidence limitations inherited and restated for this concept phase:**
- Prior audience findings rest on public sources and reasoning, not on interviews of our players (Prompt 4 limitation, disclosed there). The primary audience is a **well-evidenced hypothesis**, not a measured fact.
- Politics-first directions are burdened by weak/moderate evidence (F-015's "politically thin" critique is a single disciplined thread plus inference).
- The 2-hour cadence has never had a "players love this turn rate" body of evidence — F-009 is an *uncertainty*, and this report deliberately builds the concept so that cadence acceptance is validated (CV-004), not assumed.
- No study in the genre — including our four — has shipped a fully mapless relationship-network world. Every mapless claim in this report is composition reasoning (AI-) rather than observed market behavior. This is the largest single evidence gap the concept carries, and Section 17 targets it first.

**Claim-label discipline.** Per [DECISIONS.md](../DECISIONS.md) D-003 and D-006 and AI_CONTEXT §4, this report uses:
- **Confirmed requirement** — constraints from AI_CONTEXT §2 (unchanged this session).
- **Evidence-backed finding** — prior F-xxx / O-x / FO-xxx items carrying real observation.
- **Recommended direction / provisional proposal** — this session's synthesis work: concepts CX-x, pillars DP-xxx, differentiators UXD-xxx, anti-pillars AP-xxx.
- **Open hypothesis** — flagged explicitly per item; tested in Section 17's CV-x plan.
Nothing here is recorded as approved in DECISIONS.md. The decision log is unchanged by this prompt.

---

## Section 3 — Synthesis of previous research (Deliverable 1)

### 3A. Genre lessons that materially shape a concept

Pooling the four prior reports, the genre demonstrates the following at the level of *patterns* (not individual-product mechanics):

| Genre pattern | Evidence base | Concept implication |
|---|---|---|
| Long-horizon development is the core appeal | P&W/CN/PU/eRep's shared "build a thing that grows" loop [P#1 §3] | The nation must be a persistent project with visible compounding progress |
| Progress without management becomes a chore; drains create decisions | F-019 (eRep chore fatigue), F-014; FO-014 | Abundance must be managed, not merely accumulated |
| Scarcity + interdependence force trade and diplomacy | P&W continent raw-resources, PU per-location systems, eRep regions [P#1 §3] | The mapless design must replace geographic scarcity with *structural* scarcity (FO-013) |
| A legible market is trust infrastructure, not polish | F-022, FO-009/FO-016 | Economics must be explainable to a newcomer at entry price |
| Social fabric is the genre's fun engine — and its fragility | F-001 / F-003b (flip side), F-013, F-018 | Group belonging must be *available and rewarding*, never mandatory [P#1 §7.9] |
| War generates excitement but dominates balance cost | FO-010/011/017 complexity ratings; F-016/F-017 fairness pressure | Conflict must be present, bounded, and coexist with peaceful success |
| Politics is under-served but demand is niche and thin-evidenced | F-015 (weak-moderate) | Politics stays a modifier layer (FO-005), not the concept's spine |
| Onboarding/knowledge transfer is genre-wide churn | F-010/F-027; FO-001 | A self-explaining world is an identity-level commitment, not a feature |
| Longevity rewards persistence over resets; rounds trade legacy away | Utopia/Earth Empires pattern; FO-024 rejected | Persistent single world — matches confirmed requirement |
| Reputation/treaty webs organize community politics everywhere | P&W treaty web [P#1 §7.5] | A visible relationship layer is the natural "world map" substitute |
| Community-seeded worlds die quietly at launch when empty | F-003b | Launch plan (PXE-015) must be concept-level, not ops-only |

Concept-relevant product-specific observations (kept distinct from genre patterns): P&W's treaty *objects* in-game vs CN's off-game culture; NS's twice-daily decision rhythm proving micro-session nation games can hold players two decades [P#4 NS-1/NS-3/NS-4]; PU handbook-driven depth showing slow-burn teaching works when paired with community warmth (F-008).

### 3B. Player frustrations a *concept* level answer (not interface-level)

The following documented problems are big enough that a concept should be structured to answer them structurally rather than with UI patches:

1. **Time burden / attendance pressure (F-004, F-005, F-019; PXE-004).** *Concept-level answer:* the two-hour shared turn plus absence-tolerant action queues means the game's unit of play is a **decision batch**, not watch-hours. Attendance yields no mechanical edge (PR-2's stance, P#4).
2. **Newcomer disadvantage and knowledge walls (F-010, F-012, F-027; PXE-016).** *Concept-level answer:* transparent reporting (FO-002) with provenance ("why did this change?") as a first-class system, and structured scarcity limiting veteran lock-in (FO-013 re-specialization, Section 10).
3. **Unclear consequences / invisible mechanics causing churn** (F-014 is a generic churn signal; the transparency family F-010/FO-002 is the backed suite). *Concept-level answer:* every turn's report reads like an audit, and complexity arises from interacting visible choices rather than hidden formulas (PXE-013).
4. **Narrow success definitions at coin-heavy / war-heavy games** (F-020; F-001/F-017 adjoining). *Concept-level answer:* multiple independent paths to national standing (Section 10), not one ranked dominator axis.
5. **Social exclusion / mandatory alliance culture (F-013, F-018 partially).** *Concept-level answer:* alliance tools are rich (FO-007/008) but *solo play is structurally viable* (Section 10's stability-supported trade/diplomacy paths).
6. **Community decline and empty worlds (F-003b, F-023; PXE-015).** *Concept-level answer:* low-population-shape concept (small-world legibility, shared objectives) rather than assuming a bustling crowd on day one.
7. **Protection mechanics exploited (F-017).** *Concept-level answer:* protection designed *adversarially first* (FO-003/FO-017) as a differentiating method (UXD-005), not an afterthought.
8. **Late-arriving handicap (F-012).** *Concept-level answer:* structural scarcity + re-specialization economics give latecomers a dynamic target, not a static mountain (kept explicit as a balance risk: CCR-005).

Frustrations that the concept deliberately does NOT re-answer at concept level (they are tactics in later stages): moderation/bots (F-029 watchlist), tournament-format complaints, exact market fee policy.

### 3C. Audience implications for the core concept

Prompt 4's recommended audience (proposed): **steady-check-in multiplayer strategists** — 1–3 sessions of 5–15 minutes/day [P#4], motivated by compounding visible progress, consequential choices, optional-but-real community, honest consequences, and identity/history; secondary audience = organized community + diplomatic players; future = optimizers, competitive warmongers, roleplayers.

Implications the concept must honor:
1. **Session-shaped decisions.** The concept's recurring activity must be divisible: a player with 6 minutes can make one important call; a player with 40 can plan arcs. The turn digest's placement at either end of that window is the concept's social glue (PR-2).
2. **Community without obligation.** Opportunities for belonging (treaties, trade partners, alliance tools, shared campaigns) must reward the *dip-in* player rather than require scheduled coordination.
3. **Depth visible but not gatekept.** Mastery rewards judgment and planning, not reflexes or grind — while the jargon wall (PXE-016) and reward-drift (PXE-006) stay guarded against.
4. **Identity and legacy are mechanics, not flavor.** The world should surface "what my nation did" (history) and "how others see me" (reputation) as legible, encodable game state (Section 10/12).
5. **No map, no geography.** Every audience need maps cleanly onto a mapless abstraction; no design assumption carries coordinates.

### 3D. Differentiation opportunities carried forward from Prompt 3

From the FO register, the items that are *identity-shaping* rather than feature-level:
- **FO-002 / FO-001:** provenance-complete turn reporting + in-context teaching → "the game that explains itself" (UXD-001).
- **FO-004 / FO-006:** world-network view + treaty objects → relationships as the world (UXD-002).
- **FO-013:** specialization/interdependence without geography → the multiplayer *gravity* engine.
- **FO-003 / FO-017:** adversarially-designed protection → fairness as method (UXD-005).
- **FO-011 (partial):** peace/settlement term selection vocabulary → conflict that generates story rather than only scores (UXD-004, the most "promising but unverified" item).
- **FO-015:** re-entry digest → absence-respecting sessions (UXD-003).

Feature-level register items (FO-009, FO-007, FO-010, FO-014, FO-005, FO-008, FO-012) support whichever concept is chosen; they are not, themselves, identity — the concept decides their *relative prominence*.

### 3E. Constraints and their concept implications

| Confirmed constraint | Concept-level |
|---|---|
| Browser-first, free-first, small infra | No continuous real-time subsystem; tick-friendly math; transparency via reports, not dashboards requiring heavy queries (D-005 write-budget consciousness) |
| 2h shared turns, 12/day, players act between turns | Cadence must be the *strategic rhythm* (plan → commit → resolve) rather than a login-per-turn treadmill; queue-first actions |
| Persistent shared world, no resets | Long-arc progression (identity/history) is possible; catch-up pressure must be managed structurally |
| No conventional geographic map | The relationship network IS the world (Section 12); all "positional" gameplay translated to relational/institutional terms |
| Fictional world, original identity | No copied competitor distinctive combos; our own treaty/war/market vocabulary (FO-011 note, FO-006 note) |
| Small budget, AI-assisted build | Concept must not depend on hand-authored daily content or large moderator staff |
| Game-experiment norms of AI Context §4: F/O recorded, only DECISIONS approves | All concept work here stays provisional |

**End-of-synthesis digest (the concept brief, compressed):**
- Constraints: browser & free-first · 2h shared turn · persistent · mapless · original identity · small/lean ops.
- Evidence-backed opportunities: legibility-as-system (F-010 family), interdependence engine (FO-013), protection-as-method (FO-003/017), visible relationship world (FO-004), settlement-word conflict (FO-011), digest-first absence handling (FO-015).
- Open assumptions: real audience resonance for the specific concept; mapless comprehensibility; 2h-cadence acceptance; how much politics/economy depth the primary audience wants; market-integrity scope.
- Concept-level decisions still required (Section 18): which candidate direction, which power paths are central, conflict's structural role, who the launch world serves.

---

## Section 4 — The central game fantasy (Deliverable 2)

Five candidate fantasies were assessed against the criteria in scope (role, emotional/strategic appeal, natural decisions, player relationships, progression, 2h-fit, mapless-fit, audience fit, ops complexity, drawbacks).

### 4.1 Candidate fantasies evaluated

| # | Fantasy | Player role | Appeal | Key appeal risks |
|---|---|---|---|---|
| FX-A | "Steward of one nation in a community of nations" | You *develop and govern* one country, continuously | Compounding progress + identity + standing; directly rewards the primary audience's stated motivations [P#4 §3] | Guarding against "spreadsheets with flags" — needs relationship drama to stay alive |
| FX-B | "Strategist at the table of nations" | You *negotiate, position, and signal* among equals | Social chess; every session reads the world's pulse | Social-first fantasy fails the solo-leaning part of the primary audience; heavier burden on the early phase |
| FX-C | "The national optimizer" | You *tune* production, trade, tech | Deep-systems pleasure; throughput shaped by short sessions | Opt-in only: attracts mainly the optimizer-lite subset; community optional at best |
| FX-D | "Coalition leader / warlord" | You organize a bloc or fight wars | Highest-adrenaline genre path | Conflicts with primary-audience goals substantially; balance & ops risk highest |
| FX-E | "Chronicle author" | You author national history into the record | Long-arc identity; rich stories emerge | Risk that the fantasy sounds passive; content-generation burden |

### 4.2 Recommended fantasy structure

**Primary fantasy (recommended): FX-A — "Steward of one nation in a community of nations."**
You hold a country's development plan in one hand and its foreign policy in the other. What makes it emotional is that the world around you persists: every treaty you sign, price you undercut, or war you abstain from shifts relationships that you will still be reading about in six months of digests. Strategic identity is built by *choosing a development identity for your nation* (Section 10) and defending it against both circumstance and rivals.

**Supporting fantasies (recommended, as entry ramps, not parallel games):**
- **FX-A′ "The Builder"** — early-game face of FX-A: productive choices, visible compounding, first trade/treaty. This is how a newcomer meets the same loop.
- **FX-A″ "The Strategist"** — later-game face of FX-A: your nation has enough history/standing that *relationships* carry weight — what you promise, whom you back, what you decline. This is where Tomas (secondary persona) lives without demanding a separate game.

**Why one fantasy with two faces and not three fantasies?** A three-track game forces every system to be three things at once, fragments balance, contradicts the small-project scope constraint, and contradicts the multi-path-as-*one*-system evidence (FO-013's pairing logic) that trade and relationships must touch the same economy to matter. Funneling both into the single steward loop keeps every system earning its place.

---

## Section 5 — Candidate concept directions (Deliverable 3)

Five materially different concepts, each conforming to the confirmed constraints (browser, 2h turn, persistent, mapless, small/lean). All working labels only.

### CX-1 "The National Ledger" — economy-first development game
| Field | Content |
|---|---|
| One-line | You run an export-driven nation's production/logistics in a simulated world economy; trade is the main activity; politics/diplomacy exist but are thin. |
| Fantasy | FX-C (optimizer) with FX-A accents. |
| Primary audience | Optimizers (Future tier [P#4]), plausibly also Mira (short sessions fit ledger checks). |
| Main activities | Reading margins, setting production orders, moving goods, pricing, and the occasional policy adjustment. |
| Strategic tension | Scarce input specialties vs cost of re-specialization; global price vs local cost; cash vs strategic reserves. |
| Multiplayer experience | Other players are price-setters and supply-chain partners; interdependence is real but interaction is *transactional*. |
| Mapless identity | "Where can I source X cheaply?" is answered via the market, not geography — but the world *feels* like a market screen, not a living world. |
| Turn-cycle fit | Excellent (orders resolve per turn; ledger reads quick). |
| Differentiator | Reference prices as first-class tools (FO-009/FO-016 patterns). |
| Scope/ops | Moderate-high tech on market integrity (FO-009 High); moderate balance risk; low social-binding risk if played solo. |
| Risks | Can become a trading sim with flags — drifts from the audience's identity/history motivations [P#4]; community gravity is thin (F-001 flip: F-003b danger); persistence-without-people is a dead world. |
| Evidence/confidence | Well-founded for Mira's session shape; under-backed for the multiplayer drive. Confidence: medium. |
| Verdict | **Rejected as primary version of the concept** — retained in Section 18 (RC-2) as the "economic spine only" fallback fragment. |

### CX-2 "The Parliament" — politics-first nation sim
| Field | Content |
|---|---|
| One-line | You govern through domestic politics: policy, institutions, elections-as-light-stakes, stability management; foreign affairs react. |
| Fantasy | FX-E-rich statesmanship; close to NS's "decide and see the consequence" hook. |
| Primary audience | Politics-curious niche; Yuna-type future persona [P#4]. |
| Main activities | Legislative choices, policy changes, stability management, reacting to events. |
| Strategic tension | Policy trade-offs (efficiency vs legitimacy); events vs plans; public trust vs hard choices. |
| Multiplayer experience | Thin unless the world includes *other nations' politics* — the mapless answer (a FO-005-style cross-nation politics layer) — but the evidence for demand is weak (F-015 single-thread, Weak-Moderate [P#2]). |
| Mapless identity | Fine (politics is coordinates-free). |
| Turn-fit | Good (policy changes on cooldown per FO-005 pattern). |
| Differentiator | A dedicated "consequence trail" of your political choices. |
| Scope/ops | Seemingly small but the *content* burden of events/discipline is deceptive; event design is hand-authored content — CCR-008 territory. |
| Risks | Demand not evidenced (the nearest analog is NS's decide→consequence hook, NS-1/NS-3 [P#4]); under-serves strategy/tactics genre expectations; hard to bolt competition onto later. |
| Evidence/confidence | Generous reading of NS's decision-feedback loop; low-to-medium confidence. |
| Verdict | **Rejected** (RC-3): too speculative vs its cost; politics deferred to FO-005 layer inside the recommended concept. |

### CX-3 "The Diplomatic Order" — relationships-first game
| Field | Content |
|---|---|
| One-line | You play an ambitious smaller nation whose leverage is *relationships*: treaties, reputation, market position, and good offices; war is a last resort with heavy braking. |
| Fantasy | FX-B as primary (strategist at the table), FX-A as secondary. |
| Primary audience | Tomas (secondary persona); Mira partially. |
| Main activities | Cultivating allies, reading the treaty web, mediating, market positioning, corralling blocs. |
| Strategic tension | Reputation is slow to build/fast to spend; commitments bind; favors create obligation webs. |
| Multiplayer experience | Other players are the game. |
| Mapless identity | Excellent — the relationship network *is* the world, most purely. |
| Turn-fit | Good (web changes at turn boundaries; correspondence can be async). |
| Differentiator | Mapless "a community that plays like a ledger of promises" is a strong identity. |
| Scope/ops | Economic engine still needed underneath (dependency: FO-013/FO-009); moderate build; social-binding risk is *low-mid* because activity wants partners. |
| Risks | Excitement scarcity if conflict is too restrained; newcomer agency is thin before you *have* standing; reputation systems are notoriously gameable (F-029 watchlist). |
| Evidence/confidence | Strong fit to FO-004/006 + Prompt 4's secondary persona (Tomas); medium-high confidence it would please that audience — but it under-serves Mira's day-to-day primary needs and Kwame's future appetite. |
| Verdict | **Runner-up.** Section 6 shows the specific sacrifice CX-3 makes. Retained as a *dialect inside the recommended concept*, not a separate concept. |

### CX-4 "The Standing Armies" — competition & campaign-first
| Field | Content |
|---|---|
| One-line | You develop a nation whose success is measured by leagues, campaigns, and enforced military seasons; development exists to enable competition. |
| Fantasy | FX-D. |
| Primary audience | Competitive war-focused players (Kwame, future tier [P#4]); esports-adjacent leagues. |
| Main activities | Preparing forces, planning campaigns, executing turn-bound attacks, alliance war management. |
| Strategic tension | Military readiness vs economic; aggression vs reputation; coalition vs solo glory. |
| Multiplayer experience | Intense; other players are adversaries and teammates. |
| Mapless identity | Feasible but weakest — campaigns need objective spaces that risk becoming "maps by another name." |
| Turn-fit | Strained — high-expression war wants more synchronous attention than 2h dips [P#4 session evidence]. |
| Differentiator | Smartest war UX in a browser would be notable. |
| Scope/ops | Highest: war balance (FO-010/011 High), anti-abuse, anti-multi attack surface huge; live-ops expectation rises. |
| Risks | Contradicts the no-insistence-on-presence requirement if campaigns reward attendance; F-001's flip (F-003b) — hostile to the primary audience's casual core; F-017 pathologies multiply. |
| Evidence/confidence | Genre demand for competitive war is real and large (P&W's dominance [P#1]) but is evidence about *that game's* audience, not this project's chosen one. Confidence: low that this is our concept. |
| Verdict | **Rejected** (RC-4): preserves conflict as a *bounded layer* (CX-5, Section 11) rather than the concept's spine. |

### CX-5 "The Community of Nations" — balanced multi-path stewardship *(recommended)*
| Field | Content |
|---|---|
| One-line | You steward a developing nation in a shared world whose *framework* is a legible network of relationships — treaties, trade, alliances, reputation — where economic development is the engine, diplomacy is the surface, and bounded conflict is a consequential option, all on a two-hour world clock. |
| Fantasy | FX-A primary; FX-B/FX-C as the two faces of development (builder early, strategist later). |
| Primary audience | Steady-check-in multiplayer strategists (Mira primary; Tomas secondary) [P#4]. |
| Main activities | Reading the digest; committing orders; trading; negotiating; organizing/joining cooperative structures; occasionally planning a limited campaign; watching consequences land. |
| Strategic tension | Multiple: growth-vs-stability (internal), commitments-vs-options (diplomatic), specialization-vs-flexibility (economic), deterrence-vs-campaign (military). |
| Multiplayer experience | Other players change what is *viable* (market shape, treaty web, threat posture), not merely what your numbers show — interdependence is the gravity (FO-013/FO-009). |
| Mapless identity | Foundational: the relationship network, market, institutions, and shared chronicle *are* the world (Section 12). |
| Turn-fit | Strong: short sessions read the digest/commit orders; long sessions plan arcs; the cadence paces both. |
| Differentiator | The composition — self-explaining world + network-native mapless identity + absence-respecting sessions + adversarially-designed protection — not any single feature. |
| Scope/ops | Largest-but-bounded concept; manageable if Section 15's boundary holds (war and economics are the two largest builds, both with designed floors in FO-010/011/009). |
| Risks | Breadth risk (CCR-002); "balanced" risks meaning "unstable"; demands prioritization discipline (Section 18's staging). |
| Evidence/confidence | Highest across candidates; medium-high confidence overall, with every differentiator dependent on real comprehension testing (Section 17). |

---

## Section 6 — Concept evaluation framework (Deliverable 4)

**Scale (1–5):** 5 = direct, productive fit; 4 = strong fit with notable qualifications; 3 = workable but strained; 2 = weak fit / requires compensation; 1 = directly conflicts.
**Confidence note per row where the score is judgment-heavy:** scores on criteria A, B, E, F, I, and K are especially judgment-laden (subjective) — marked ⚠ where applied and defended in the row notes; all weighted results are treated as a *decision aid*, not truth.

### 6.1 Criteria and weights

| # | Criterion | Weight | Why it matters / why this weight |
|---|---|---|---|
| A | Fit with primary target audience | 12% | The audience decision (P#4) is the filter through which the other evidence is weighted; mis-fitting it voids everything downstream. |
| B | Strength & coherence of the central fantasy | 12% | A concept that cannot state what you *are* collapses into a feature list (Section 7's test). |
| C | Distinctiveness | 6% | Differentiation matters for identity but not more than fit; novel-but-failed beats nothing. |
| D | Quality of recurring decisions | 8% | Session-by-session "what do I do?" drives daily attraction. |
| E | Persistent/asynchronous play compatibility — meaning survives absence | 9% | A core constraint: the world must reward the player between sessions, not only inside them. |
| F | Two-hour cadence fit | 6% | The shared clock must structure planning, not pressure logins. |
| G | Mapless compatibility | 7% | No geo-map assumption; world is legible as network. |
| H | Diplomacy & social meaning | 6% | Community gravity: pledged interdependence makes others matter. |
| I | Newcomer accessibility | 7% | First-day / first-week clarity reduces drop-off (PXE-002/007/012). |
| J | Progress beyond numeric totals — richer goals matter over time | 2% | Guard against "bigger numbers" as the only progression (PXE family). |
| K | Development & balance feasibility for a small team | 10% | Scope-confidence feasibility — project's constraints. |
| L | Operational / live-ops burden | 6% | Free-first posture. |
| M | Evidence consistency (with P1–P4 findings) | 3% | Contradicting strong evidence is costly. |
| N | Ability to support long-term strategic development | 2% | The concept must sustain months-scale arcs, not only week-scale loops. |
| O | Support for multiple approaches (multi-path power) | 2% | DP-001's premise must be present conceptually, not bolted on later. |
| P | Newcomer-onboarding & future-budget compatibility | 2% | Onboarding burden and future cost ceilings constrain the concept's growth. |

*Note: weights sum to exactly 100%. Weights favor fit (A/B) and feasibility (K) — the two things the project controls and that most predictions hinge on; differentiation matters for identity but not more than fit, and a differentiated concept that cannot ship is worthless. Criteria J/O/P are weighted low because the evidence base cannot yet distinguish candidates on them — they are inputs, not discriminators at this stage.*

### 6.2 Weighted comparison (1–5 scores; weighted value per row; ⚠ = judgment-heavy)

| Criterion (weight) | CX-1 Ledger | CX-2 Parliament | CX-3 Diplomatic | CX-4 Standing Armies | CX-5 Community |
|---|---|---|---|---|---|
| A — audience fit (12) | 3 (optimization lite; weak for multiplayer drive) | 2 (niche; F-015 evidence thin) | 4 ⚠ (Tomas strong; Mira partial) | 2 (future-tier; excludes core) | 5 ⚠ (both primary + secondary) |
| B — fantasy strength (12) | 3 (thin emotional payload) | 3 (statesmanlike but inward) | 4 ⚠ (compelling but demanding) | 3 (potent but single-minded) | 5 ⚠ (clear, compounding, layered) |
| C — distinctiveness (6) | 3 (market sims exist) | 4 (politics-first is rare) | 5 (relationship-first is rare) | 3 (military-first is well-trodden) | 4 (balanced network-native is original) |
| D — recurring-decision quality (8) | 4 (high-frequency choices; low *stakes variety*) | 3 (event-chasing rhythm) | 5 (every promise/scarcity/pricing reads) | 5 (confrontational, high-stakes) | 4 (diversified decisions) |
| E — async / between-session meaning (9) | 4 | 4 | 5 | 3 ⚠ (war demands presence at campaign peaks) | 5 |
| F — 2h-cadence fit (6) | 5 | 4 | 4 | 2 ⚠ (attendance pressure risk) | 5 |
| G — mapless fit (7) | 3 (network-simulation fine but "world" reads thin) | 3 | 5 | 2 (campaign spaces risk becoming geo-maps) | 5 |
| H — diplomacy/social meaningfulness (6) | 2 | 3 | 5 | 4 | 5 |
| I — newcomer accessibility (7) | 4 (market literacy helps) | 2 (politics lacks reference) | 3 ⚠ (agency before standing) | 2 (burly onboarding) | 4 (compounds via digest+teaching) |
| J — progress beyond numeric totals (2) | 2 | 2 | 3 | 1 | 3 |
| K — small-team feasibility (10) | 4 | 3 ⚠ (event content crushes) | 4 | 1 (war balance + pvp balance) | 3 ⚠ (largest scope; disciplined floor) |
| L — live-ops burden (6) | 4 | 3 | 4 | 2 (event cadence inherits) | 3 |
| M — evidence consistency (3) | 3 | 2 (F-015 weak) | 4 | 2 (F-003b conflicts) | 5 (no evidence contradiction found) |
| N — long-term strategic development (2) | 4 | 3 | 3 | 4 | 4 |
| O — support for multiple approaches (2) | 2 | 3 | 4 | 4 | 5 |
| P — onboarding & future-budget fit (2) | 3 | 3 | 4 | 2 | 4 |
| **Weighted total** | **3.44** | **2.97** | **4.25** | **2.59** | **4.39** |

*Weighted total = Σ(score × weight%, weights normalized to 100%) so totals sit on the 1–5 scale. Rounded to two decimals; do not treat ranking as evidence — use the "what would change the ranking" notes in 6.3.*

### 6.3 Per-candidate adjudication

| | Strongest case | Weakness | Highest-risk assumption | Compromise it asks of you | Who it sacrifices | What could change the ranking |
|---|---|---|---|---|---|---|
| CX-1 | Cleanest tech footprint; strong fit for solo optimizers and Mira's short sessions | Overlooks the genre's multiplayer gravity; drifts into a trading sim with flags | That audience motivation "growth and optimization" can outrun "identity/history/standing" | Shrinks the community/identity value the genre's players expect | Tomas & Kwame entirely; Mira's second-half motivations | Evidence that the primary audience rides *solo* would move it up; F-003b empty-world risk drops it further |
| CX-2 | Most original in emotional register; strong hook for writers/strategists | Demand is weakly evidenced (F-015); biggest content/editorial burden | That NS-style "decide → consequence" desire generalizes beyond NS's audience | Overlooks the genre's core: market/military breadth in balance | Kwame & competitive players | A future F-015-quality study raising that evidence definitively |
| CX-3 | Most defensible mapless identity; strongest for the secondary persona | Newcomer agency is thin before standing exists; excitement scarcity | That relationship-play alone can generate near-term fun without an economic engine | Dilutes the genre's competitive gravity; the pitch to the primary persona sags | Mira's early weeks; Kwame | If CV-002 shows players *expect* diplomatic-first framing, it rises; if empty-world evidence grows, it falls |
| CX-4 | Best fit for the largest competitor in genre revenue terms | Directly contradicts presence-respect and F-003b risks; the largest balance surface | That session-cadence-compatible competitive war can be made on 2h dips | Forces a live-ops and anti-cheat program a small team can't sustain | Mira/Tomas wholesale; our constraint set | Only if validation (CV-004) refutes the session-shape evidence — unlikely |
| CX-5 | Only candidate honoring every confirmed constraint while keeping plural paths open; composition is original | The hardest one to scope; "balanced" risks incoherence | That multi-path power can be *balanced* at small-team scale without one path emerging dominant (CV-003 feedback) | Needs discipline to not become a kitchen-sink | Nobody fully, but all four partially | If CV-001 shows players find it unfocused, trim its theatre (usually economy/military — see Section 18) |

**Concluded recommendation: CX-5 "The Community of Nations", with CX-3 declared runner-up** and a stated trade-off rather than an artificial winner for the *top-two* question: CX-5 is chosen for constraint-fit + audience fit + feasibility; CX-3 would have been the choice if the *secondary* "strategist-at-the-table" persona were primary and if earlier-stage session-shape evidence supported the heavier social lift. CX-3's identity practices survive inside CX-5 (its diplomatic-first *surface*, its reputation vocabulary) without becoming the *whole* game.

---

## Section 7 — The recommended concept (Deliverable 5)

### 7A. Core concept statement (working identity, name not final)
> **You steward a developing nation in a persistent community of rival and interdependent states, making meaningful political, economic, and military decisions on a shared two-hour world clock in a world that is a transparent network of relationships — not a map — and where your choices leave legible consequences in a shared history other players are writing alongside you.**

### 7B. The concept in play (what playing Project X should *feel* like)
*(Three paragraphs.)*

**The player role.** You begin with a small
fictional country and a world clock that advances one shared global turn every two hours (12 turns a day). Your day is shaped by *strategic
commitments* — what to produce, what to buy, whom to
court, what to defend — and the shared world responds. You make trade deals, sign treaties,
grow your economy, develop institutions, or expand your military — all without ever seeing a
spatial map: a world whose size is *relationships, prices, reputations, histories, institutions — a
network that is legible as stories and numbers, not territory.*

**The multi-player structure.** Driving in a persistent world: no rounds [FO-024 rejected], no
geography [FO-025 rejected], no live-timed windows [FO-026 rejected], no pay-for-power surfaces [FO-027 rejected as a *pattern*]. Other players' choices matter
as your context of options: a market partner's pricing shifts your margins tomorrow; an enemy's
mobilization reshapes the safe space you bring your goods to; an ally's declaration of Washington-1
war rule changes what you must lawfully abstain from. Nothing about the world's gravity depends
on you being *online* at once: the 2h clock keeps the world moving and every player's input is
registered, so "when can we all meet at once?" never needs an answer.

**The player's fantasy in play.** You are at once the *steward administering a national plan* — economic, political, scientific — and *a persona at
the table*: someone whose word is worth something, whose boundaries are respected, whose
decisions are consequential. Progress is legible: the "turn digest" explains what changed in your
country and *why* [FO-002; DP-004's provenance principle]. Growth is compounding but bounded [FO-014]: every gain is a decision you trade
stability or alliances to sustain. Power is plural: several roads lead to a "big" nation [Section 10] — so success stays legible,
and competing goals never force a permanent either-or choice of "do I play economy or war?" at all times.

### 7C. Intended audience (who is served first — and why)
Confirmed by Section 6: Mira-type (primary [P#4]) voice: the "steady-check-in strategist" (5–15-minute sessions
1–3×/day) whose play is shaped by **progress-compounding decisions, honest consequences, earned standing**; Tomas-type (secondary)
voice: organized-community and diplomatic players who fill the world's treaty web and institutions.
Kwame/Yuna-style competitive-minded optimizers are future-tier audiences addressed by this concept through
multiple-success-path design but NOT made the center of design: this is deliberate. Prompt 4's
evidence supports the *primary* audience; CX-5 is its most feasible home.

### 7D. Main sources of strategic interest (the few that make decisions meaningful)
1. **Compounding national build-out vs. bounded drains** — what to grow and what it costs to sustain (FO-014): the “why did my advantage erode while I slept” question.
2. **Structural scarcity and re-specialization** — following what to specialize in has a cost; no map, but specialization means depending on partners (FO-013).
3. **Volatility & commitments in others** — your allies, treaties, markets, and rivals' visible posture (NOT secret numbers); your word, once given, is *binding* (FO-006) — and
reputation and standing are slow-growing and fast-spent.
4. **Multi-path national standing** — several *independent *but interacting* success registers (Section 10); none is mandatory.
5. **Shared chronology** — the world's cumulative record (who won what, who was where, who promised what) is
part of the strategic terrain [FO-004/FO-006; Section 12].

### 7E. Why multiplayer matters at all (what a single-key simulation cannot offer)
- *Strategic variety that no team could author finite-content-wise:* other players change the shape of what's smart (markets, blocs, wars have outside "angle").
- *Commitment as texture:* being trusted or betrayed is a one-of-one story generated by play, not
authored content, and unlike a scripted NPC scheme, other players actually *remember* — turning
the persistent world's value into a shared, ongoing social chronicle [P#4 FX-E/FX-A pillar evidence].
- *Community without judgment:* the game serves both alliances AND independent play without *forcing* community: cooperate *when it works for you*.

### 7F. Why this works *without* a geographic map
Because the strategic "space" of this world is **structural**: market position, treaty web, reputation, records, institutional weight, standing in
individual groups. Prompt 1 §7.2 confirmed no genre game ships a fully mapless symbolic-network world — we are making the deliberate product bet that a
perceptible, memorable relationship space can substitute for geography, and our "map" is derived directly from *known recorded behavior*: trade relationships,
treaties, standings, message logs. Every geo-function is analyzed to a network/institution equivalent in Section 12 — no geo-look projection is grafted onto the concept.

### 7G. Why the 2-hour cadence supports the experience
- **Synchronous rhythm without requirement:** everyone shares the same clock, meaning the world is "the same age" for everyone — you and your
trade partner read the same prices "today".
- **Paces strategy, not attention:** resolution pacing generates planning (what to commit for *this* turn, and
what to queue), and the commitment lull forms natural check-in points; attention is *asked for*, never *required* (DP-002).
- **Early decisions matter, but don't spiral:** turn-resolution updates come in *batches* (production, upkeep, market renewals, war actions) — one clear decision horizon for reactions and planning and no "second-by-second" pressure in either an action or a reporting sense.

### 7H. Long-term appeal (no promise of infinite novelty)
Effective retention theory (P1 §7.9) names three things: *predictable check-in rhythm*, *visible progression*, *group bonds.* CX-5 addresses all three without promising tight-loop event
novelty. A player may reasonably play CX-5 for a season: develop a nation to a personally meaningful milestone, ride one
or two stories through the treaty web, and retire with a completed national identity. The persistent world supports that — no resets wipe their story away.
Attempting to promise "unbounded content forever" against a small team's reality would violate the scope constraints;
the concept's explicit *staging* (Section 16B) replaces novelty with *history depth* as the renewable resource.

### 7I. Explicit non-goals (all proposed, none from an approved decision)
1. **Not a real-time action/reflex game** — no twitch-mechanics entanglement; game response unaffected at 2h cadence (FO-026 rejected).
2. **Not a conquest-and-territory game** — no geographic map, no territory capture as the primary success metric (FO-025 rejected).
3. **Not an attendance/streak-driven game** — those mechanics are anti-pillars (AP-001).
4. **Not alliance-required** — AP-004: independent play is structurally supported.
5. **Not an exhaustive institution simulation** — elections/congresses (FO-023) deferred, not in v1 scope.
6. **Not content-scaled by manual authoring** — no dependence on hand-written daily events; community + systemic structure fabricates narrative.
7. **Not whale-playable** — no pay-for-power (FO-027 rejected pattern; D-003).
8. **Not a copy** — no recognized competitor *combination* is reconstructed; the treaty/war/market vocabularies are our own [FO-006/FO-011 "our own vocabulary" notes].

### 7J. Remaining uncertainties before the concept can be considered validated (blockquote all-go list)
1. **CX-5 vs CX-3:** whether the *primary* audience actually wants a diplomatic-first focus; CV-001 in Section 17.
2. **Mapless comprehension:** whether the world-network presentation reads as "a world" to newcomers; CV-002.
3. **2h cadence acceptance:** whether 12/day rhythm *feels like a plan*, or like nagging; CV-004.
4. **Multi-path coherence:** whether several success registers can coexist without one metric becoming dominant (sim-test CV-003).
5. **Diplomatic-first language:** whether "steward/strategist" vocabulary lands better than "war/territory" in explaining to newcomers; CV-005.
6. **Differentiator value:** whether "the game that explains itself" is *valued* by playtesters, not just novel; CV-006.

---

## Section 8 — Proposed design pillars (Deliverable 6)

Working identity pillars for CX-5, all **provisional** (not approved; no DECISIONS entries). Pillars differ from Prompt 4's experience principles (PR-x): PR-x governs *player experience policy* at interface/moment level; DP-x governs *system design principles* at architecture/balance level.

### DP-001 "Multiple legitimate paths to national standing"
- **Principle:** any major player goal in the game must be reachable by at least two distinct strategies; no single resource, stat, or mechanic may be a universal prerequisite.
- **Player need:** identity choice + fairness (PXE-016, PXE-006); counters the "one true build" drift seen genre-wide (F-020's narrow success).
- **Concept relationship:** the CX-5 spine (Section 10's multi-path table).
- **Evidence/reasoning:** F-020's defining pain from narrow coin-race success; F-012 late-join friction partially caused by static-advantage structures.
- **What future design must do:** balance *all* power sources; define standing contributions without a single dominating metric; subject every new system to "does this make path X mandatory?"
- **Violations:** a feature whose absence makes most strategies unplayable; a "success metric" that is just GDP-rebranded.
- **Example:** a diplomatic nation without a market economy niche stays vital *because* of treaty reputation; blocked wars don't ruin a diplomatic playstyle.
- **Trade-offs:** harder balance; slower tuning; more initial design surface requires dedication on sections 10/11's staged builds.
- **Evaluation in testing:** CV-003 (multi-path preference); player interviews on "what does a *successful* player do" — no single answer form.
- **Confidence:** medium-high. **Approval status:** provisional.

### DP-002 "Decisions over presence"
- **Principle:** the game rewards planning and judgment, never session count, attendance streaks, or continuous online behavior; presence beyond a useful session is mechanically valueless.
- **Player need:** F-004/F-005/F-019's attendance-burnout family; Prompt 4's PR-2 cadence-respect principle.
- **Concept relationship:** the CX-5 "queue-first action system" + "digest what changed while away" [FO-015].
- **Evidence:** F-019/F-004 travel; NS-3/NS-4's short-session longevity [P#4].
- **What future design must do:** any unlock/frequency design must have a *zero* effect on offline players beyond natural time-passing; no login streaks, no live-event windows (FO-026 already rejected), no urgency timers on claims or limited offers.
- **Violations:** bonus multipliers for consecutive turns logged in; activity contests as success criteria.
- **Example:** a player who logs in twice a week plans *arcs* with multi-turn orders and loses nothing strategic (FO-015's "what changed while away" reads the whole week).
- **Trade-offs:** weaker engagement metrics; fewer hooks for retention by *habit* vs *structure* (a monitoring risk, noted in Section 16).
- **Evaluation:** onboarding test in CV-004 cadence study.
- **Confidence:** high. **Approval status:** provisional.

### DP-003 "The relationship network is the world"
- **Principle:** the game's "world view" is a legible network of typed relationships (treaties, trade, alliances, reputation, histories) — spatial-free — and no system requires coordinates, geography, or map-art assets.
- **Player need:** understanding "where do I stand" without a minimap; the geographic-independent international narrative.
- **Concept relationship:** CX-5's mapless identity (Section 12).
- **Evidence/reasoning:** FO-004/FO-006's research; Prompt 1 §7.2's confirmation that nothing in genre does this (making it original territory, not a copied mechanic).
- **What future design must do:** every feature spec must state its world-network representation; no "map-like" sub-interfaces in early releases.
- **Violations:** "distance" mechanics expressed as xy; "frontier/region" tiles.
- **Example:** instead of "your neighbor's border," you see "3 treaty links, 2 markets in tension, shared-alliance partnership — give the relationships legibility."
- **Trade-offs:** interface design work (learning curve PXE-016 risk); pure-list views need strong taxonomy work; some players *want* a map back (validation risk in CV-002).
- **Evaluation:** CV-002 mapless comprehension test.
- **Confidence:** medium. **Approval status:** provisional (biggest single new ground).

### DP-004 "The world explains itself"
- **Principle:** every player-visible number, event, or outcome must be traceable to causes the player can examine without leaving the game; provenance is not a meta wiki but an in-game property.
- **Player need:** the genre's largest documented churn family (F-010, F-014, F-027; PXE-003/013/016).
- **Concept relationship:** CX-5's "transparent turn reports" [FO-002] + in-context teaching [FO-001].
- **Evidence:** multi-game churn path [P#2].
- **What future design must do:** every new system ships with its explanation surface at release; no feature whose consequences a newcomer cannot understand without community documents.
- **Violations:** hidden multipliers revealed later; "you had to be there" mechanics; obfuscated randomness without disclosed probability.
- **Example:** digest entries read "Your manufacturing margins fell 4% — 70% from your trade partner's tariff change, 30% from market-wide price drift [underlying data]." (Illustrative, not a spec.)
- **Trade-offs:** competitive-information hiding (some fog is strategically fun — see the DP-004 boundary note); higher data/reporting engineering work.
- **Evaluation:** CV-006 comprehension tests with players.
- **Confidence:** high. **Approval status:** provisional.

### DP-005 "Interdependence is structural, not social polish"
- **Principle:** players' strategic success must be meaningfully coupled through economic and diplomatic structures — your nation's options depend on what *others* do, not merely on your own play; but coupling must never *force* one player to be another's prerequisite for basics.
- **Player need:** the multiplayer *reason* for a multiplayer game; belonging without obligation (F-013's forced-alliance criticisms).
- **Concept relationship:** CX-5's "multi-paired gravity" through trade [FO-013] + treaty stakes [FO-006].
- **Evidence:** FO-013's analysis (pairing logic in CN's circles + P&W's trade dependence with geography excised).
- **What future design must do:** economy design must ensure structural reasons for trade beyond preference; must verify a *solo-capable baseline* (no forced alliance to trade).
- **Violations:** every nation being able to autarkically produce everything at string; or the opposite, severe lock-in where a missing partner starves you.
- **Example:** two nations specializing differently trade at a structural advantage neither could reach alone — and if one falls, the other has an adverse, legible gap to manage.
- **Trade-offs:** balancing vulnerability vs autonomy; protecting newcomers from being forced into bad partnerships.
- **Evaluation:** CV-003 + economic sim in a later design stage.
- **Confidence:** medium-high. **Approval status:** provisional.

### DP-006 "Conflict is bounded, consequential, and coexists"
- **Principle:** military conflict exists, is decisive *inside* its domain, respects a player's right to plan around it rather than be present, and never renders peaceful or diplomatic strategies invalid; conflict design is adversarially pre-designed (abuse-testing before shipping).
- **Player need:** genre excitement (Kwame-like future tier) + newcomers'/dove players' fairness (F-016/F-017).
- **Concept relationship:** CX-5's bounded conflict layer (Section 11); ties to FO-010/011/017 *only* as design input, not as approved rules.
- **Evidence:** F-016/F-017's fairness failures; FO-011's settlement vocabulary as our own "our own end-conditions and term vocabulary" design premise.
- **What future design must do:** war system design documents are run through abuse-scenario tests; conflicts respect the 2h cadence and the *absence-tolerant action queue*; conflict escalation has off-ramps (negotiated peace terrain).
- **Violations:** mechanic that lets war instantly destroy economy-level standings of non-dirigble nations; no way for a peaceful strategy to be *invalidated by force* without genuine provocation.
- **Example:** an attacked nation's economy is *harmed* in a bounded, reportable way; the political harm (reputation to the attacker's network) puts *standing*, not just numbers, at stake — and the war ends in negotiated terms rather than "target lies in ruins."
- **Trade-offs:** less adrenaline than free-form war; more design work; limits the size of the "military-first" audience appeal.
- **Evaluation:** war-design abuse walkthrough (Prompt 3 Section 8's anti-abuse questions); a later-stage dedicated design prompt.
- **Confidence:** medium. **Approval status:** provisional.

### How the pillars interlock — and their conflicts
- **DP-001 vs DP-005:** a tension that matters *early*: structural coupling can *go too far* and destroy multi-path viability. Future design should treat DP-005 as bounded by DP-001 ("coupled but not prerequisite-bound") — as the tie-break rule.
- **DP-002 vs DP-006:** conflict escalations *want* attention; bounded conflict design must keep its attention-needs within "queue-first" norms — no mechanic that punishes an offline player with an unavoidable tactical outcome.
- **DP-003 vs DP-004:** telling players "the world is a network" while retaining strategically relevant *uncertainty* about rivals' plans is a deliberate gap — recommend: keep *relations* transparent, keep *probabilities/intent* opaque; DP-004's boundary note guards this.
- **DP-001 vs DP-004:** full transparency plus multi-path balance is harder to tune than either alone; expect iterative balancing with full data visibility as an enabler — the trade is spent in design time, not in hidden opacity-on-purpose.

---

## Section 9 — The core strategic activity (Deliverable 7)

### 9A. The core loop (one turn cycle's shape; 5–15 minutes)
1. **Observe** — read the turn digest: what changed in your nation and *why* (provenance); what changed in your relationships.
2. **Assess** — set/confirm priorities: one or two things your nation must address *this turn cycle*; notice any trade or alliance needs.
3. **Commit** — issue or pre-schedule orders: production targets, market cancels/posts, policy/research starts, military preparations if relevant.
4. **Engage (optional)** — check messages and the register: a partner needs a look; your ally wants something; a rival did something notable.
5. **Resolve** — the critical point of CX-5: actions never "instantly" resolve; outcomes land on turn boundaries. Pre-commit or queue.
6. **Interpret** — at the *next* digest, your input's effects are visible with provenance [FO-002's mechanism, the pillar DP-004].
7. **Adapt** — your development plan or treaty posture receives its first feedback; next turn's decisions are more interesting because of it.

**What makes a decision consequential in this loop:** (a) resource scarcity (something not done); (b) *irreversibility gradients* — some choices are cheaper to reverse than others, all are traceable [DP-004]; (c) *other players' visibility* — anything publicly committed affects reputation/standing; (d) *resolution timing* — the 2h cadence means a decision is a *bet on the next twelve* — and its results are individually attributable.

**What information the player needs (and gets):** current state + per-src change deltas + provenance (FO-002); market reference prices (FO-009/016 as design-stage item); relationship states (FO-004); *not*: rivals' *intent*, hidden commitment plans — strategic uncertainty is the game, not a UX bug (DP-004's boundary note).

**Where the loop stays interesting over months:** from each turn's micro-loop, players build *arcs* (Section 9B). The micro-loop's interest comes from the context of *what I am trying to do this month* — month-scale plans make turn-scale calls non-repetitive.

### 9B. Arc-scale (the long-arc cycles — days-to-weeks horizon)
Three classes, matching the concept:
| Arc type | Length | What it looks like | Loop relationship |
|---|---|---|---|
| **Development arcs** | days–weeks | A research program, an infrastructure building wave, an industrial transition, a market entry. | Feeds the micro-loop with "which turn-level action is there for the *arc* rather than the day — giving the turn decisions meaning." |
| **Relationship arcs** | days–indefinite | Courtship of a possible ally; the rise of a bloc; a long-building rivalry; a trade corridor. | Reputation/standing mechanics give these arcs a *history*, not just a state. |
| **Episodic crises** | hours–days | A border incident, a supply shortfall, an election-year-style turbulence, an unauthorized strike. | *No manual authoring required:* these emerge from the system (a market shock, a war action, a treaty broken); manual events are NOT a manual content dependency (AP-003). |

### 9C. The loop is *not* these things (deliberate anti-loops)
- Not a notification-chasing app: no reward for *responding* to a prompt within minutes (DP-002).
- Not a chore wheel: "feed your people / restock your smithy / clear the tick list" is rejected as a loop-shape; upkeep exists as *decision pressure* [FO-014], not as *daily click-throughs*.
- Not a "click everything" experience: resolution happens at boundaries; the player commits *once* and goes. This is the deliberate difference from P&W/CN's per-turn click loops on war-turn mechanics differences and similar [P#1 §7.1].

### 9D. Short vs long sessions (confirmed against the audience)
| | 5-minute check-in of a Mira session | 40-minute plan-and-negotiate session |
|---|---|---|
| Does | Digest reads (2 min); commit queued orders; one market/trade/treaty action; done. | Digest + trend exploration; a development-arc decision; a negotiation thread; queueing multi-turn plans; possibly a war review. |
| Loses | Nothing (digest is complete with provenance; queue avoids penalty). | Excess in *negotiations not concluded* (asynchronous; resolves later). |
| Feels | "I made one real decision and one bet; the world moved on without me; my plan is intact." [PR-2 alignment] | "I set this month's direction; the next 36 turns have a plan." |
| Both | Supported by one shared information surface (the digest) — the same tool at both depths (a deliberate design commitment, not UX polish). | |

---

## Section 10 — Multiple paths to national power (Deliverable 8)

### 10A. Candidate paths assessed

| Path | Motivation served | Decisions generated | Independent progress viable? | Interactions with other paths | Mandatory-risk | Design/maintenance burden | Audience relevance | Evidence quality / uncertainty |
|---|---|---|---|---|---|---|---|---|
| **Economic prosperity** (production, trade) | Builder/optimizer (Mira-level) | What to produce, what to sell, means, pricing; niche/positioning | Yes — self-contained skips wars entirely | Feeds diplomacy (trade leverage), military (sustainment), research (materials); is affected by all | Medium (DP-005 coupling can overpower) | Moderate–High (market integrity) | Primary audience | Strong genre evidence [P#1 §7.3]; our composition is original (FO-013) |
| **Diplomatic influence & reputation** | Strategist (Tomas) | Whom to court, whom to trust, which promises tie your hands | Yes — a treaty-and-mediation nation can thrive | Trades options for options (protection, market access, credibility); affected by military posture | Medium (reputation can game) | Moderate (FO-004/006 design + reputation rules) | Primary + secondary | Strong (P&W treaty-web proof; FV) + our mapless composition |
| **Stability & institutions** (internal order) | Planner/roleplay-lite (Yuna, Mira) | Governance structures, policy priorities, reaction to internal shocks | Partially — meaningful as a *floor* (a collapsing nation loses every other path) but not as a *ladder* on its own; deliberately *not* a separate zero-sum register | Acts as a multiplier/penalty on all others (a stable nation grows faster; a fragile one is vulnerable) | **High** (inadvertent mandatory-feature risk) | Low–Moderate (FO-005) | Primary | Mixed: "stability matters" genre-wide, but *as a ladder* it's our composition; treat as enabler, not a success path |
| **Research & technology** | Builder/analytics players; the "compounding" personas | What to research first, when to share or embargo | Partial — meaningful as a *force multiplier*, not a solo ladder; research alone does not define late-adopter positions | Couples to economy (materials), military (readiness), diplomacy (sharing/embargo ethics) | Medium-High | Moderate | Primary | Genre reference exists but thin: eRep/P&W both have tech layers; the *modifier-not-ladder* positioning is our composition |
| **Military strength & effectiveness** | Kwame-adjacent/future tier | Readiness posture, campaign targets, coalitions, deterrence | Yes with bounds (attainable but bounded by DP-006) | Feeds diplomacy (deterrence), is fed by economy; can *harm* reputation if misused | Medium (DP-001's "don't let war be every-losing") | **High** (war is the hardest build) | Secondary/future | OK: genre-wide (F-016/F-017 concern is gameability, not nonviability) |
| **Cultural/informational influence** | Roleplay-communities (future) | What to broadcast, whom, how | Uncertain — mapless fit is genuinely unknown | Would need both content-generation + network-visibility mechanics not in any prior evidence | High (deferred) | High | Future only | **Thin — deferred, not recommended at concept level** |

### 10B. Verdict and the danger-dependency map (per Del.8's required checks)
- **Central paths (Deliverable-verdict):**: economy & diplomatic standing — these two carry most "national power" meaning in the concept; they are *co-equal*.
- **Structural but supporting (~"no separate registers, no zero-sum ratchets"):** stability and research. Stability is a *floor/enabler* different: a broken nation has no path; strong stability is not itself a *success ladder*. It is a multiplier, not a track. Research is a *convertibility engine* (turning economy into utility and options), not a standing axis.
- **Optional but real:** military strength — bounded conflict (Section 11), deliberately *not* the dominance axis.
- **Deferred:** cultural/informational influence (no evidence from research to make it meaningful; would commit to system design without a player need yet demonstrated — revisit if the community generates organic "national identity"/"information politics" demand in alpha).
- **The two dangerous dependencies the research specifically flags:**
  1. **Economy → military sustainment runaway:** a market leader funding the largest permanent military could invalidate diplomatic playstyles; countermeasure (proposed, not approved): DP-001's "no path is dominant" test + bounded-conflict design (DP-006), with balance owned by a dedicated design stage.
  2. **Reputation → treaty lock-in runaway:** a nation whose standing is everything can become trapped by obligations; countermeasure (proposed): treaty design must be *selectable in scope* (a small NAP is not a world-commitment), and reputation should be *affected by actions* rather than purely stored as a crown to lose.
- **Balance questions this treatment raises for a later design stage (not solved here):** relative *value flows* across paths; how much coupling DP-005's "structural" interdependence has *before* it becomes a choke; what actions cost on a path versus another (e.g., research time vs production time vs negotiation time — should they compete on *attention* or on *resources*?); whether *stability* trades off against *growth* (FO-005's "efficiency vs legitimacy" axis) reads as a *rule* or a *choice*.

---

## Section 11 — Diplomacy, cooperation, and conflict as identity (Deliverable 9)

**Structural answer: these four are *interconnected aspects of one strategic environment* — not four parallel games.** The concept builds them into one substrate: the relationship network (DP-003). Every diplomatic, cooperative, or conflict action *is* a record in the same world state the economy reads and the chronicle remembers. The hierarchy is of *prominence*, not of systems:

| Layer | Conceptual role | Source evidence | Primary motivation served | Boundary rules (concept-level) |
|---|---|---|---|---|
| **Development & interdependence** | The base layer: what nations *do* | FO-013 (mapless interdependence design) | Builder/optimize (Mira); optimizer-lite | Interdependence never makes a partner a *prerequisite for baseline operation* (DP-005's bound) |
| **Diplomacy & reputation** | The every-day strategic surface: where nations *compete and cooperate* | P&W treaty-web precedent [P#1 §7.5]; F-006's mapless read; FO-006 | Strategist (Tomas); Mira's second-half | Promises are selectable in scope; reputation is affected by acts (not a pure score); no secret-treaty-only system at v1 (transparency tension resolved: keep *relations public*, *intent opaque*) |
| **Cooperation & alliances** | The collective-action layer: structures *belonging without mandating* | P&W alliance tools [FO-007/008]; F-013 both readings; F-018 | Community seekers (Tomas); secondary persona | Alliance membership is a *choice* whose benefits are real but whose absence is not a lockout (AP-004) |
| **Conflict (bounded)** | The consequential last-mile: a *chosen* escalation with real, bounded stakes | FO-010/011/017 *as design inputs*; F-016/F-017's fairness warnings; Prompt 1 §7.7's abstract-warfare analysis | Competitive players (future tier); defender's justice (universal) | Never the default decider of standing (DP-001); never requires attendance (DP-002); always has off-ramps; adversarially pre-designed (DP-006's adversarial-first method); our own end-conditions & term vocabulary (FO-011's "settlement story" design premise) |

### What war can *mean* in a mapless world (candidates, not approved mechanics)
- **Campaign-objective conflicts:** abstract, non-geographic "objectives" (e.g., a competitor for a contested market's access rights, a dispute over a resource-pairing arrangement, a reputational challenge) — resolved within a bounded, discrete campaign structure with off-ramps and settlement terms (FO-011). The FO-012 "shared campaign focus" is the *cooperative* variant of this (alliance-member optional).
- **Economic pressure / blockades:** a "soft war" (trade breaks, market access restriction, supply withholding); friendly to peaceful strategies *and* to aggressive ones — the FO-011 note's "blockades econ-warfare on production/market access" observation.
- **Reputation and prestige competition:** multiple nations compete for a *standing title* or a *chronicle-marked outcome* rather than for a coordinate — no geographic conquest, no "win," just legible records with consequences.
- Both individual and *coalition*-based versions of the above (which can pull in FO-008's "official bulk actions").

### A conflict that is *bounded* looks like this (concept sketch — not final rules)
- The **decision to go to war is a real decision** (cost, reputation, opportunities at risk), not a free click.
- Both sides plan around the shared turn cycle; the attacker queues operations, the defender sees escalation factors and can respond with what they control.
- War actions have *budgeted costs* (FO-010's action-budget *as design input*), discourages burst-attacks, and keeps pace with a 2h cadence rather than attendance pressure.
- Wars produce **legible stories** (settlement terms, recorded chronicle histories), not mere scores: the post-conflict record is part of the contest (FO-011's "settlement story" design premise).
- **Farming/stalemate/fake-war exploitation** is *adversarially designed against* before shipping (FO-017) — this is UXD-005's differentiator, not a patch chore.
- **Newcomers and small nations are protected by structure:** protection is designed so that its presence doesn't "shield farming" (FO-003/FO-017's adversarial-first basis); a small nation's *harm* from a war is bounded in part by scale-safety rules (design-stage, not approved here).

### What this treatment *sacrifices* (honest trade-offs, per prompt scope)
- War-thrill players who want constant combat with maximal expression won't find CX-5 ideal (that is the rejected CX-4 direction).
- Emphasis on the settlement-and-consequence story narrows the design scope available for war gameplay's breadth.
- The **F-016 evidence's "small nations drop out under war pressure"** is treated as a design-goal, but a fully solved answer requires a dedicated war-design stage (not this concept).

---

## Section 12 — The mapless world as an identity strength (Deliverable 10)

### 12A. What the world *is* (the organizing metaphor)
A **community of nations** — a *ledger of relations* as its recognizable structure — the substrate:
1. **The Register of Nations and their relationships** (FO-004's typed-relationships world view): every treaty, trade connection, alliance, and reputation state, with histories.
2. **The Market** (FO-009's listings + reference prices): whose pricing and exchange structure creates interdependence (FO-013) and scarcity *without* geography.
3. **The institutional layer** (alliance structures, FO-007/008; the shared chronicle; the standing registers).
4. **The shared chronicle of the world's history** — an accumulating record of notable events, wars, settlements, treaties, and

country trajectories, which functions as the "world's memory" [FO-004's "changes over time"].

### 12B. Ten questions answered (per prompt)
1. **How does a player understand where their nation fits?** Their own "national card" (summary, standing, treaties, partners, positions, history), plus the full register view — relationships and standings are visible, not an unseen world of hidden coordinates.
2. **How can relationships change visibly?** Relationship records are event-sourced in the shared chronicle; growth and decay are visible (a relationship "cools," a bloc grows), and every relationship has a *type*, which players read like a status (alliance → tension), not just a numeric affinity.
3. **How can a player discover potential allies/rivals?** Register search and sorting by compatibility of *structural needs* (e.g., "I need what they have, they might want what I produce") — the FO-013 pairing mechanic is not just economy: it is the mapless world's *functional* "geography."
4. **How is economic/diplomatic interdependence conveyed?** Market and registry views *show dependencies* — what flows from where to whom (a dependency map *of relationships*, not a map of continents).
5. **How can campaigns feel significant without tiles?** Conflict produces *chronicled outcomes* with consequences (standing shifts, market changes, settlement terms recorded); a chronicle entry carries *stakes and stories* in a way territorial maps carry *distance and geography*.
6. **How does the interface avoid a graph/menu maze?** *One spine*: the national card is the daily screen; the register, market, chronicle, and *institutions* are reachable from *one* node, each revealed as needed; the graph view is a *tool*, not the world (FO-004's "list/timeline-first" staging); there is no "map" to dwell on.
7. **What goes in a world overview vs a detailed nation view?** World overview: market pulse, register headlines, institutional news, tallies of nations & blocs; detailed nation view: that nation's full *card* (economy, treaties, positions, history) — plus the *chronicle entries they cause*.
8. **Which representations are easiest to build browser-first, free-tier?** *Lists, tables, timelines, text-first cards* (low asset cost, low data weight), *graphs later* (FO-004's staged polish). Map content production is *structurally non-existent* (a positive scope win).
9. **What makes mapless legibility come across immediately?** A strong first-visit story: the onboarding trail *teaches the structure* — "here is your country card; here's its register entry; the market you can trade in; the chronicle where your history will be written" — with mapless *composition* baked into the teaching [FO-001/FO-002].
10. **Which assumptions require a prototype/usability test?** DP-003 (whether network-as-world *reads* as a world); specific interface no-maze-test; CV-002 in Section 17 for the comprehension test; the DP-004 boundary note (how much *opacity* the strategic layer tolerates without hurting trust).

### 12C. What cannot be done without more design work (deferred)
A *fully* mapless world still needs an answer to "what is 'far' from me?" — distance analogs (market position, bloc distance, treaty distance) are concept-level implied (Section 10's "geographic-distance analogs"), but each one is a design-stage decision, not a set of numbers here. Risk recorded: CCR-003 (comprehension) and CCR-005 (whether distance-analog balance holds).

---

## Section 13 — Originality and differentiation (Deliverable 11)

### 13A. Genre foundations Project X may use (not claimed as distinctive)
Resource management, persistent access, nations, alliances, trade, wars with resolution mechanics, treaties-as-objects, and player-driven politics — all present in genre and free to use *as* conventions. The *combination and their framing* is where originality lives.

### 13B. Proposed differentiators (with deliberately cautious claims about their novelty)
| ID | Differentiator | Player benefit | Prior-finding link | Distinct from generic convention? | Evidence/reasoning | Ops/impl weight | Superficial-novelty risk | How to test | Central or optional |
|---|---|---|---|---|---|---|---|---|---|
| UXD-001 | **The world explains itself** — provenance-complete turn reports + in-context teaching as system, not wiki (FO-001/FO-002) | Newcomers stop churning; veterans trust numbers; disputes about "why" have a source of truth | F-010/F-014/F-027/F-023; PXE-003/013/016 | Yes: no P-genre game claims *provenance-complete* reporting [FO-002's analysis] | Strong (multi-game churn evidence) | Moderate–High (journaling + taxonomy) | Could reduce to "nice tooltips" if not systematic | CV-006 comprehension + trust test | **Central** |
| UXD-002 | **The relationship network is the world map** (FO-004/FO-006 + FO-013) | Strategic landscape is legible; trade partners and treaty partners are the "geography" | PR-1 §7.2's "original territory" analysis | Yes: no studied game does this *fully*; composition original | Medium (components proven, composition novel) | Moderate (list-first) to High (graph later) | Could degenerate into a *messaging-graph* feel without chronicle/institutions | CV-002 comprehension test | **Central** |
| UXD-003 | **Absence-respecting sessions** — queue-first actions + re-entry digest as a first-class flow (FO-015 + the digest family) | Player's legitimate "life outside" respected; world feels alive without demanding you watch | F-004/F-005/F-019/F-023; V-2/V-3 [P#4] | Yes: genre's typical shape is "log in to the world" — CX-5 inverts it | Strong (multi-game evidence) | Low–Moderate (queue + digest on same journaling as FO-002) | Could reduce to "an email digest" without *arc-scale* queueing | CV-004 cadence check | **Central** |
| UXD-004 | **Settlement-word diplomacy over domination vocabulary** — conflicts *end in earned terms*, not scores (FO-011's design *premise*; F-016/F-017's fairness) | Negotiated terms and narratives matter; small nations keep standing; histories feel hand-made, not procedural | F-016/F-017's fairness failures | Yes: no competitor centers *terms-selection* as the end-of-war experience [FO-011's "our own end-conditions & term vocabulary"] | **Medium — our most promising-but-unverified differentiator** | High (with the war system) | Could become "the war that ends in a dull, consequence-free settlement" without real stakes | CV-003 + dedicated design-stage test | Optional at CX-5 concept level; *strongly recommended* for its identity role |
| UXD-005 | **Adversarially-designed fairness** — protection and anti-abuse mechanics *beaten in design first* (FO-003/FO-017 + F-017's evidence of exploit styles) | Newcomers stay; competitive integrity holds up; the game's fairness is *engineered*, not decorative | F-017's documented exploit case-study | Yes: genre *ships* protection that players reverse-engineered; shipping *pre-hardened* is a method change | Strong | Moderate (isolated states; testing cost) | Could degenerate into "some bolted-on cooldowns" without the *method* | War-design walkthrough at a later stage | **Central as method** (supports UXD-004) |

**Unverified-claim discipline.** UXD-001 through UXD-003 are in strong evidence within their findings; UXD-004 is a promising direction backed chiefly by design argumentation rather than observed player demand; UXD-005 rests on a strong *problem* (F-017) but the "our method is different" claim is a design-intent claim, not a result. No "unique in the industry" language is used anywhere in this report. Final tests: CV-002/CV-006.

### 13C. Deliberately avoided approaches (and the player need behind each)
| Avoided | Why | Player need protected |
|---|---|---|
| Geographic world map | FO-025's confirmed rejection; Prompt 1 §5.3 cost evidence | Newcomers can orient without cartography; small-team budgets don't burn on map assets |
| Rounds/seasonal resets | FO-024's rejection | Player-built identity is *kept*; the game's persistent-world promise is honored |
| Live-timed participation windows | FO-026's rejection | "Play when life allows" is a design property, not a wish |
| Pay-for-power surfaces | FO-027's rejection pattern; F-020's coin-elite pain | Fair game in which standing is *earned by play* |
| Mandatory alliance membership | F-013's "forced-alliance" critique | Independent play is a legitimate style |
| The "click every turn" chore loops | F-019's chore fatigue; DP-002 | Sessions shape decisions; queues resolve at boundaries |
| Hand-authored daily content dependence | CCR-008 (Section 16) | World texture emerges from *systems* (FO-015's digest + FO-013's trade pairs), not editorial calendars a small team can't sustain |
| Risky handling of "secret intel/spy" systems | FO-019's deferred watchlist | Trust in information as a foundation (DP-004) |

### 13D. What originality is *not* claimed
That our *war system* will be unprecedented (it draws on genre), that our *economy* is a new species of market sim (it draws on market designs), that any single mechanic is "industry-first." Project X's originality is a *composite identity*: a self-explaining, absence-respecting, relationship-native, adversarially-fair persistent world — something the studied genre set does not offer as a *whole*. The composite identity's test is in Section 17.

---

## Section 14 — Design anti-pillars & scope boundaries (Deliverable 12)

Eight proposed anti-pillars (provisional; deliberate *scope warnings*, not feature vetoes — any can be revisited through evidence obtained later). Each states what to avoid, what it prevents, the temptation that produces it, the "check" a future feature proposal runs, and its status.

| ID | What to avoid | Risk it prevents | Why the temptation arises | Check for a future feature | Status |
|---|---|---|---|---|---|
| AP-001 | Requiring login at every turn boundary, or mechanics that reward attendance/streaks | DP-002 violation; the attendance-burnout family (F-004/F-019) | Retention-metrics pressure; "engagement = DAU" metrics | "Does skipping this punish the player in any way beyond what happens naturally?" | Provisional (drawn from constraint set but not formally approved) |
| AP-002 | Requiring a geographic map or territory-capture as the core metric | FO-025's confirmed rejection; DP-003; mapless-identity dilution | Genre gravity ("everyone has a map"); war "needs" a visual | "Can the feature be restated in relationship/institution terms?" | **Confirmed via FO-025** in DECISIONS only as an *opportunity-rejection*. No map-forward feature enters the design stage without a vote |
| AP-003 | A dependence on hand-authored daily content or a large moderator/live-ops staff | CCR-008's scope risk; free-first posture | "Events" are how games stay fresh; F-003b's empty-world is urgent | "Would this feature fail if the team were one person + the AI assist?" | Provisional |
| AP-004 | Making alliance membership a functional requirement for basic play | F-013's forced-alliance critique; Mira's solo viability | War/market balance pressure ("people will just group anyway"); balancing burden | "Can a new player reach a meaningful, *successful* baseline without joining anything?" | Provisional |
| AP-005 | Allowing one power path to dominate the success metric | DP-001 violation; F-020's "narrow success" | Balancing simplicity; "the same one that just tuned best" | "Which path gives the fastest returns? If it's one, revise." | Provisional |
| AP-006 | Complexity through unexplained rules; jargon that must be learned from out-of-game wikis | DP-004 violation; F-010's churn family | Depth pressure ("rich systems feel deep"); content creep | "Can a new player trace this mechanic's consequence in-game?" | Provisional |
| AP-007 | Continuous real-time engagement windows or synchronous events as a foundation | FO-026's confirmed rejection; 2h-cadence constraint | "Live events" and "real-time adrenaline" in every game pitch | "Does this break the shared-clock cadence, or require all players online simultaneously?" | **Confirmed via FO-026** rejection |
| AP-008 | Copying a competitor's distinctive combination of mechanics/presentation | Original-identity constraint; legal/ethical originality risk | "It works for P&W; just do what they do" (FO-006/FO-011's caution about typed treaties & war *values* — structure inspiration allowed, vocabulary/values not) | "Would our design still make sense if the competitor never existed? Is our vocabulary our own?" | Provisional |

*(Two additional prompt-suggested anti-pillars — "numbers-only progression" and "unwanted social obligations" — are covered by AP-005's and AP-004's boundaries and by DP-001's "no path is dominant" rule and the PR family; they are folded deliberately rather than getting separate IDs.)*

---

## Section 15 — First playable concept boundary (Deliverable 13)

The purpose of the *first playable concept* is to validate CX-5's **core loop + mapless-world comprehension** (CV-002/CV-006 in Section 17), *not* to build a miniature of every proposed system.

### 15A. Essential (must be present to test the concept)
| Element | Question it answers | Dependency | Complexity |
|---|---|---|---|
| E1 A functioning nation model with a *few* systems: production, a simple economy (no market yet — a director-managed "national card"), and one domestic-policy-style axis | Does compounding, drain-bound national development *feel* like the fantasy? (CV-003) | – | Moderate |
| E2 **Scheduled turn resolution** on the 2h shared clock: orders queue; outcomes land at boundaries | Does the cadence read as *rhythm* rather than nagging? (CV-004) | E1 | Moderate |
| E3 A **transparent turn digest** with per-line provenance | Does "the world explains itself" *land* as a benefit? (CV-006) | E2 | Moderate–High |
| E4 **At least two distinct value sources** so that DP-001's multi-path premise can be probed (e.g., an economic niche vs a relationship/prestige niche) | Do players perceive multiple legitimate paths? (CV-003) | E1 | Moderate |
| E5 **A basic player-to-player interaction** in a *tiny shared world*: a simple trade handshake + a public "relationship" record with a visible history | Does interdependence make multiplayer feel *structurally* coupled (FO-013/DP-005)? | E1+E2+E3 | Moderate |
| E6 A **static/dummy representation of the rest of the world** (a small register of additional nations, run by scripts) — the player can *see* the register | Does the mapless "community of nations" *read* as a world? (CV-002) | E5 | Low–Moderate |

### 15B. Simulated or simplified (representable without full implementation)
| Element | Simulated how | Question it still answers |
|---|---|---|
| S1 Treaty & reputation systems | Two or three "types" with non-negotiable records (visual treaty web can be text) | Does *reputation-as-legible-record* feel like standing? |
| S2 Alliance structures | A single validated "partnership" object (not a full permission system) | Does cooperation feel rewarding without being mandatory? |
| S3 Military/war | A *scripted* conflict vignette or a "watch a defined war resolve" demo, not a war system | Does *bounded conflict* add tension without attendance pressure? |
| S4 Market dynamics | A world with *one* exchange surface, with scripted price drift | Does trade feel interdependence-driven (CV-003)? |
| S5 Research/technology | A few turn-gated advances (no full tree) | Does the "compounding/advancement" button register? |

### 15C. Out of scope for the first playable (deliberately)
| Element | Rationale |
|---|---|
| O1 Full anti-multi/anti-automation/admin systems | Not needed for *concept* validation; integrity work waits until the real market design stage (FO-009's "architecture stage" scoping) |
| O2 War balancing at all | War is the largest build; its *concept* test is a scripted vignette, not a tuned system |
| O3 Months/years of progression depth | 3–6 sessions of CX-5's shape prove (or don't) the core loop; depth is post-concept |
| O4 Full alliance-permission role systems (FO-007) | Concept test: does *cooperation* exist — not does *governance* exist |
| O5 Rival/nation-vs-nation competitive content | Implied by success-path design, not needed for the core loop test |
| O6 Any production/authentication/hosting selection/construction | Concept test is scoped to gameplay; engineering/architecture format is a later stage per D-002 and D-005 |

---

## Section 16 — Concept risks, conflicts, and trade-offs (Deliverable 14)

### 16A. Risk register (provisional; qualitative estimates only)
| ID | Risk | Underlying assumption | Evidence quality | Likelihood | Impact | Confidence | Affected pillars/audience | Mitigation or validation | What would make us reconsider |
|---|---|---|---|---|---|---|---|---|---|
| CCR-001 | The primary audience is under-defined (P#4's tests not yet run) | That P#4's persona-type audience exists at the scale of a small game | Medium (genre-pattern evidence, no direct survey) | M | H | M | All DP-x; Mira | CV-001 concept-preference test | If CV-001 shows weak resonance with CX-5's shape, CX-5 reduces scope to CX-3/CX-1 synthesis |
| CCR-002 | The concept is *too broad* (a balanced everything drifts into a kitchen-sink) | That "multi-path" can be a spine, not a list | Medium | M–H | H | M | DP-001; scope viability | Section 18's staging (economy + diplomacy first, war & market-integrity staged); Section 15's floor | If staging proves unworkable, defer a whole path out of v1 completely (probably the economic exchange, keeping only directed trade) |
| CCR-003 | The mapless world fails comprehension (newcomers can't read a world made of relationships) | That relationship+chronicle+register can substitute for geography *and* be legible | Medium (no market precedent; composition is novel) | M | H | M | DP-003; everyone | CV-002 mapless-comprehension test before any interface design lock | If CV-002 fails, a *symbolic* world-schematic (not geographic; an abstract "positions" view) becomes a design candidate — still FO-025-compliant |
| CCR-004 | Multi-power-path balance is genuinely hard; one path dominates despite design | That DP-001's "no dominant path" is achievable at small-team tuning | Medium | M–H | H | M | DP-001; everyone | Section 10's verdict to keep stability/research as modifiers-not-ladders; dedicated balance stage; sim tests | If a path still dominates in playtests, cut that path's leverage at v1 (a whole tier delayed) |
| CCR-005 | Structural-coupling (DP-005) creates choke/vulnerability feel rather than opportunity | That FO-013-style pairing can be tuned to feel enabling, not trapping | Medium | M | M | M | DP-005; Mira/Tomas | 15A-E5's structural coupling probe | If coupling feels oppressive, retreat to "agreements-based" cooperation (FO-008 style), accepting less structural gravity |
| CCR-006 | Conflict's "bounded" promise doesn't deliver adrenaline; competitive players bounce | That bounded conflict can *still* feel consequential | Medium | M | M | M | DP-006; Kwame-type | Scripted war vignette in the first playable | If the vignette reads as toothless, war scope is re-examined (never at the cost of DP-002) |
| CCR-007 | Small launch world feels empty (PXE-015's documented risk, F-003b) | That a small team's world can still feel *populated* at low numbers | Strong for risk (documented); medium for our mitigation | M–H | H | M | DP-005 (coupling fills gaps); Mira/Tomas | Launch plan: curated micro-world (fewer but actively-managed nations) + insurance mechanics (15A-E6's scripted nations as visible population backfill) | If empty-world effects stay bad, a semi-private "merge" or "regional shards" concept is a later-stage candidate |
| CCR-008 | Community and market-integrity systems are audit-grade work not scoped anywhere yet | That free-first ops can hold the integrity of a player economy | Strong (Prompt 3 §8's FO-009 complexity) | M–H | H | H | DP-004/DP-005; everyone | Dedicated architecture stage with actual D1 write-budget modeling (per D-005) | If budget math is infeasible, the economy's scale/scope is ratcheted down to directed trades (CCR-002's fallback) |
| CCR-009 | Diplomacy and social activity pile up unwelcome interpersonal obligations for players who don't want them | That "community-by-choice" (AP-004) is actually achievable when reputation systems exist | Medium | M | M | L–M | DP-001/DP-006; Mira who won't lean on diplomacy | Reputation as *affected by acts* — not a "score to hoard"; AP-004 checks in every design review | If independent players report social-pressure fatigue in CV-003 post-play, soften reputation's mechanical pull |
| CCR-010 | Turn-digest-sourced reporting wants more D1 writes than the free tier tolerates | That transparency (FO-002) is *affordable* at 12 turns/day | Strong (Prompt 1 §6.1's 100k/day free-tier cap plus its 2026-09 enforcement change) | M | H | H | DP-004; everyone | Architecture stage's write-budget analysis (D-005); digest retention policy as a first-class design item | If the budget fails, reporting becomes delta-timestamped text (lighter) but with the same scope |
| CCR-011 | "Balanced" CX-5's vocabulary doesn't *sound* coherent to new prospects (a marketing/positioning risk, not a gameplay risk) | That "steward of a nation in a community of nations" reads distinctly enough for CV-001 testing | Medium | M | M | M | All | CV-001 includes *concept pitch descriptions* (not just menus) | If pitches fail comprehension, tighten the statement (shorter, more concrete wording) |
| CCR-012 | The concept's *originality* claims may not survive contact with a larger audience (players may say "this is [X competitor] minus Y") | That the *composite* identity is experienced as a composite, not fragments | Medium | M | H | M | All DP-x | UXD-001…005's "how to test" columns | If playtesters say "derivative," reframe which differentiator is the *headline* (most likely UXD-001) |

### 16B. The material trade-offs that cannot be simultaneously satisfied
1. **Depth vs. accessibility:** full multi-path systems are hard for newcomers; the compromise is *staged depth* (FO-001's in-context teaching + a gradually expanding features floor) revisited when the newcomer journey (P#4's stage journey) is better understood.
2. **Structural interdependence vs. autonomy:** coupling creates meaning *and* vulnerability; the compromise is *graded coupling* (specialization choices are *optional* but rewarded; autarky is possible-but-inferior) — reviewed at every economic-balance iteration.
3. **Transparency vs. strategic mystery:** full provenance *incl.* rivals' plans would kill competitive secrecy; the compromise is relations/reports-of-reality fully transparent, *intent and commitment plans* opaque (this
         reconciliation must be explicit in the design stage; see the DP-004 boundary note).
4. **Bounded conflict vs. competitive adrenaline:** strictly bounded conflict appeals to the primary audience but limits the appeal to competitive (future-tier) players; the compromise is bounded-conflict design that keeps real stakes and consequences while deferring maximal-expression war (Kwame is not primary); reviewed if the first-playable war vignette reads toothless (CCR-006).
5. **Free-first feasibility vs. market-integrity sophistication:** a strong in-game economy requires integrity engineering whose budget may not fit D-005's free-tier posture; the compromise is a *staged economy* (directed trades → listings market when infrastructure allows) — reviewed at the architecture stage with actual write-budget math.

---

## Section 17 — Concept validation plan (Deliverable 15)

No validation below is complete research. Each is a *proposed* experiment with defined evidence for/against. IDs CV-001…CV-006 (these also appear in the AI_HANDOFF open-assumptions as H-1…H-6).

| ID | Question tested | Hypothesis | Participants | Method (proposed) | Min. materials | Effort | Positive evidence | Negative evidence | Result that would change the recommendation | Needed before next design stage? |
|---|---|---|---|---|---|---|---|---|---|---|
| CV-001 | Does CX-5's pitch resonate with the primary audience *as described*? | The one-line statement + 3 supporting sentences draw genuinely positive reactions from 5–10 target-player profiles (community recruiting at genre forums/sites *is* attempted publicly prior to launch) | Genre-forum natives who match Mira/Tomas signatures | Short-form written pitch; structured feedback prompts | Pitch text; 3 short supporting pitches = 1 paragraph each | Low | ≥3 distinct participants describe an *imagined session* that matches CX-5's shape (not geo-war rush) | Participants consistently misread it as "war/map game" or "idle chart game" | A misread *shape* would re-trigger CX-3-vs-CX-5 (the CX-3/CX-1 fragments at Section 5 stay on the shelf) | Yes |
| CV-002 | Does the *mapless relationship network* read as a place/world to newcomers? | Material with 2 sample "national cards" + 1 register excerpt is understood *without* prompting | 5–8 target players, no prior context | Comprehension exercise; "explain back what you see" | Mock-up cards + register page | Low | Participants describe inter-nation dynamics correctly; "where is everyone?" confusion is rare | Participants reach for a map or reject the abstraction | If most reach for maps, *the identity, not the UI, needs re-designing* — a symbolic-scheme rework becomes the candidate | Yes |
| CV-003 | Do players perceive multiple *legitimate* success registration types? (DP-001's core test) | Given two sample nations, participants identify others as co-viable, not "worse" | 5–8 same as above | Concept cards of two fictional nations' strategies; ask "which wins?" (answer: both do, differently) | Card descriptions 1 page | Low | Participants accept plural paths without demanding a single metric | "But which one is *actually* best?" is consensus | Would trigger rebalancing of Section 10's central/supporting assignments before deeper design | Post-first-playable |
| CV-004 | Does the 2h-shared cadence *feel* like a rhythm rather than an obligation? | Framing "the world advances one shared turn every two hours (12 per day); you plan when you like" is not read as a login treadmill | 5–8; include at least 3 non-hardcore | Description + one mock day-in-3-sessions walkthrough | Rough day diagram | Low | Participants express "fits my day" reactions | Participants expect punishment for missed turns (or want streak alarms) | If obligation-framing dominates, CX-5's digest-first framing needs rewriting *before* deeper design | Yes |
| CV-005 | Which success framing resonates: "stewardship" (growth) or "standing" (community)? (also V-1 feed) | The wording of the pitch's *success language* shapes how participants imagine they would play | Same cohort as CV-001 | A/B of two one-sentence framings | Two sentences | Low | A consistent preference identifies the pitch's center of gravity | Inconsistent/mixed — that's fine, both framings are considered | If neither framing resonates, CV-002's shape question may be a symptom, not the cause | Before next stage (pairs with CV-001) |
| CV-006 | Does provenance-complete reporting (UXD-001) *register* as valuable when seen? | Seeing a sample digest makes players *trust* the game's truthfulness | Same cohort as CV-002 | Show a mock digest; ask "do you trust this? what's unclear?" | A realistic sample digest page | Low | Trust signals, and no "I'd need a wiki translated for this" reactions | Confusion, or "too much text" | If "too much text" dominates, digest taxonomy (short vs long-form) becomes a flagged design risk | Yes |

**Three kinds of evidence, kept distinct per the prompt's warning:**
- *Interest* (CV-001/CV-005): does the concept *attract*?
- *Understanding* (CV-002/CV-004): does the concept *explain*?
- *Enjoyment* (later): the first playable (Section 15) is where enjoyment gets measured, NOT here; CV-003/CV-006 straddle comprehension and values, not enjoyment claims.

**Not planned here (explicit):** statistical-survey-grade studies; paid studies; the actual *concept test subjects* (we have no player pool yet — this is a *plan*, and its targets are drawn publicly if/when the user authorizes promotion).

---

## Section 18 — Concept decision register (Deliverable 16)

No item below moves to [DECISIONS.md](../DECISIONS.md) without explicit owner approval — per the prompt's scope constraints and DECISIONS.md's own rules.

### 18A. Existing approved decisions invoked (restated, not new)
- **Confirmed (Constraint-frame certs; from original briefs):** browser-first; 2h shared turn; persistent (no resets); fictional mapless world; free-first posture; original identity (no competitor *combos*). [AI_CONTEXT §2]
- **Provisional items in DECISIONS (still pending, relevant here):** OP concept (D-004); hosting candidates (D-005); FO register status-only (D-006). Resolution of each of D-004/D-005 remains a *later-stage* design task, not this concept's.

### 18B. Recommended directions (this report's synthesis; NOT approved)
| ID | Topic | Position | Rationale | Evidence | Consequences | What could change it |
|---|---|---|---|---|---|---|
| DIR-1 | Primary candidate concept | **CX-5 "Community of Nations"** recommended; CX-3 declared runner-up | Only candidate hitting constraint-fit + audience fit + feasibility simultaneously (Section 6) | Synthesis of all four prior reports; FO-004/006/013; F-010/017/019-family | Future design stages treat CX-5 as the working concept, subject to CV-001/002/004 | CV-001/002 failures; a competing direction's stronger validation |
| DIR-2 | Primary fantasy | **FX-A steward** primary, with FX-A′builder/FX-A″strategist as *entry faces*, not parallel games | One-funnel concept keeps scope & coherence | P#4 personas' motivation structure | Pillars and systems target one loop with two faces | CV-005's framing result |
| DIR-3 | Central paths | Economy + diplomatic standing are central; stability & research are *supporting* (multiplier, not ladder); military optional-but-real; cultural/informational deferred | Mapping each candidate path to motivation + balance risk (Section 10) | F-020/F-015/F-016/FO-013 | Design stages must test DP-001's no-domination rule on *these* assigned roles | CV-003's results |
| DIR-4 | Conflict's structural role | Bounded, settlement-vocabulary conflict (UXD-004) present from early release; not the concept's flagship feature | Bounded conflict keeps CX-5 coherent; adversarial design (UXD-005) is the right method | F-016/F-017; FO-003/010/011/017 *as inputs* | War design gets a dedicated later stage; not blocked by this concept | CV-006/vignette showing conflict reads toothless |
| DIR-5 | Mapless identity's role | Relationship-network-native (UXD-002) with *staged* representation (list-first, graph later) | Both cheap-to-build and identity-defining | FO-004's staged plan; §7.2's no-precedent analysis | Interface specs start with *structure*, not visuals | CV-002's result |
| DIR-6 | Differentiators' headline | UXD-001 (self-explaining world) as the concept's advertised headline differentiator; UXD-002/003 as supporting; UXD-004/005 as method differentiators | UXD-001 is the most-evidence-backed; others are *stronger claims* but weaker evidence | F-010 family's churn path | Positioning language in future materials *leads* with the self-explaining world; never overclaims | CV-001/006 results |

### 18C. Open hypotheses (carry forward; tested per Section 17)
- **H-1:** The mapless "community of nations" world reads as legible to genre newcomers (CV-002).
- **H-2:** The 2h shared cadence is perceived as rhythm and planning aid, not obligation (CV-004).
- **H-3:** The primary audience exists at the described pattern (5–15min sessions; identity + planning motivations) (CV-001/V-1/V-2 continuity with P#4).
- **H-4:** Multi-path "no dominant success metric" is achievable in balance practice (CV-003, later-stage sims).
- **H-5:** Provenance-complete transparency *increases* trust and comprehension without becoming noise (CV-006).
- **H-6:** Bounded settlement vocabulary *adds* strategic interest without removing war adrenaline entirely (post-first-playable).

### 18D. Deferred questions
- Economies' *exact* market shape: exchange vs directed-trades vs hybrid (FO-009's open question; deferred to the economy design stage).
- Politics *depth* beyond FO-005-style levers (F-015's evidence is weak; deferred to post-alpha if demand emerges).
- Espionage/intel systems (FO-019); consumer-demand sim (FO-021); contracts/escrow (FO-022); elections (FO-023) — all deferred per FO statuses.
- Name/brand. Out of scope everywhere: the working label "Community of Nations" is descriptive only.

### 18E. Rejected candidates (for the record; with reason preserved)
- **RC-1 Geographic world** — covered by FO-025 (per DECISIONS-adjacent rejection at research level); not this concept's.
- **RC-2 Economy-first-only (CX-1)** — falls to community-glow risk; retained on the shelf as a *fallback fragment* if the economy is staged down (Section 16's staging fallback).
- **RC-3 Politics-first (CX-2)** — demand not evidenced; returns only if a future F-015-quality evidence base appears (Section 6 note).
- **RC-4 Competitive-first (CX-4)** — contradicts no-default-war, session-shape evidence; returns only if validation refutes the session-shape evidence (unlikely, per CV-004's current shape).
- **RC-5 Alliance-permission-first (e.g., FO-007 as a *spine*)** — toolset-first is not a concept; real integration into CX-5's structure is at Section 11's layer 3, not as the core.

---

## Section 19 — Conclusion

CX-5 is the synthesis response to evidence across all four prior reports: it uses every *used* differentiator (UXD-001's self-explaining

world, UXD-002's relationship-native world, UXD-003's absence-respecting sessions) that has multi-source evidence; it carries forward the genre's *tested* conventions where they serve the primary audience's needs; it *stages* the risky, expensive, or evidence-thin directions (economy formalization, war depth, 

politics, consumer-demand, elections, espionage) so that validation (Section 17) precedes commitment. It *rejects* the directions whose evidence, constraints, or audience fit fails (geography, live windows, resets, pay-power) — consistent with the FO-024…FO-027 rejections and confirmed constraints.

**What this phase establishes:** a coherent, evidence-aware, *provisional* concept for Project X with an ID-registered structure of pillars, differentiators, anti-pillars, risks, and validation steps. **What remains open:** every item in Section 18C's H-1…H-6 — the concept is not yet *correct*, only *defensible as the current best direction awaiting its own validation cycle*.

---

## Section 20 — Source register

No new external research was performed for this report. All claims trace to one of the following project-internal sources. (IDs cross-reference prior reports' registers; no source URLs are reproduced here — navigate via the referenced report files.)

| Ref | Internal source | What it grounds in this report |
|---|---|---|
| [P#1] | [stage-1/01_competitor_research.md](01_competitor_research.md) | Genre conventions, per-product specific observations, code and hosting constraints (§6), abstract-warfare analysis (§7.7), the mapless-precedent analysis (§7.2), new-player evidence, the "no decided values" procedure (D-004/D-006) |
| [P#2] | [stage-1/02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) | All F-xxx findings cited; O-x opportunities; the "attendance/chore illegibility" family; F-029 watchlist; no-new-uncited-sources discipline |
| [P#3] | [stage-1/03_feature_comparison_opportunity_analysis.md](03_feature_comparison_opportunity_analysis.md) | All FO-xxx items cited; complexity/dependency assessments; the market-integrity warning (§8 §10 FO-009); the cross-confirmation of which features are candidates vs rejected |
| [P#4] | [stage-1/04_target_audience_and_player_experience.md](04_target_audience_and_player_experience.md) | Personas; primary/secondary/future audience attribution; PR-1…PR-10; PXE-001…019; V-1…V-10; NS/PW/ER/SC/PU source citations whose numbers are restated here only through their Prompt-4 IDs |
| [D-###] | [DECISIONS.md](../DECISIONS.md) | Approved/provisional decisions with IDs, cited where they channel this concept (D-003's finding/opportunity-only rule; D-004 OP; D-005 hosting; D-006 FO register) |
| [§2] | [AI_CONTEXT.md](../AI_CONTEXT.md) Section 2 | The confirmed-constraint set (browser, 2h turns, mapless, free-first, original identity, AI-assisted build) |

### A note on evidence labels in this report
- **Strong:** multi-game / two-source corroboration [P#2's evidence-quality discipline].
- **Moderate:** credible but single-threaded.
- **AI- (analytic inference):** composition reasoning not observed in any game (applies predominantly to CX-5's *composites*, not to the underlying findings).
- **FV/FE/PXE/PR/V:** source-document citation families, used without re-verifying each claim's original source in this session (the sources are current as of their original reports' sessions; this report introduces no new claims *from* them).

---

## Section 21 — Handoff to the next research phase

### Project snapshot for a fresh AI
- **What Project X is:** a persistent, multiplayer, browser-based nation-strategy game; a shared two-hour (12/day, UTC) global turn cycle; a fictional *mapless* world represented as a symbolic network of nations and relationships; free-first, small-team, AI-assisted build; original identity (no competitor combos copied); no design/implementation finalized; Stage 1 (research) prompt 5 of 8. See [AI_CONTEXT.md](../AI_CONTEXT.md) §1–2 for full constraint framing.
- **What this report adds:** the *recommended concept direction* — (provisional, unapproved) CX-5 "Community of Nations" — with pillars, anti-pillars, differentiators, validation plan, and a decision-register framing what is decided versus still open.

### Read first (in order)
1. [AI_CONTEXT.md](../AI_CONTEXT.md) §1–2, §4, §6, §7
2. [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md)
3. [DECISIONS.md](../DECISIONS.md) (D-001…D-006)
4. This report in full (id registers: CX-x, FX-x, DP-001…006, UXD-001…005, AP-001…008, CCR-001…012, CV-001…006, DIR-x, H-1…H-6, RC-x)
5. Prompt 1–4 reports (files 01…04 under [stage-1/](.)), especially Prompt 3 §10's FO register (statuses) and Prompt 4 Section 19's validation register (V-1…V-10)

### The concept's current state (for accurate future references)
- **Recommended concept (provisional):** CX-5; runner-up CX-3's *dialect* is preserved inside CX-5's diplomatic *surface*; CX-4 remains rejected as a *direction*, not as a feature class; one linear path (CX-2's politics) is deliberately *deferred* into FO-005's policy-lever framing.
- **Primary fantasy:** FX-A stewardship with FX-A′(builder) and FX-A″(strategist) as entry faces — **one** funnel, not parallel tracks.
- **Pillars:** DP-001 paths-plural; DP-002 decisions-over-presence; DP-003 relationship-network-as-world; DP-004 self-explaining world; DP-005 interdependence-structural; DP-006 conflict-bounded. **Anti-pillars:** AP-001…AP-008. **All provisional — none approved.**
- **Differentiators:** UXD-001 (headline), UXD-002/003 (structural), UXD-004/005 (method-level; UXD-004 is the weakest-evidence claim). **None claims industry uniqueness beyond what evidence states.**
- **Validation still open:** H-1…H-6 (CV-001…CV-006 above). From Prompt 4's full register V-1…V-10, all remain open and none has been executed. Before the next design stage: V-2 (P0), V-4 (DP-004's transparency-vs-mystery boundary), plus CV-001…CV-006 themselves. Before beta/pre-launch: V-3, V-5, V-6. Beta: V-7, V-8. Before roadmap: V-9. Post-v1: V-10.

### What a future AI must NOT assume
- That CX-5, any pillar, any differentiator, or any anti-pillar is **approved** — every one is *provisional* until recorded in [DECISIONS.md](../DECISIONS.md) by the owner.
- That MAP/OP values, war mechanics, or the market structure are *decided* (FO-010/FO-011/FO-009 are *inputs*, no numbers exist).
- That Stage 1 is complete (it isn't; this is prompt 5 of 8).
- That this concept was "validated by play" — it was validated *only as a written analysis*; no playtests exist yet.

### What a future AI *must* respect
- Every future feature/system proposal checks against the anti-pillar list AP-001…008 and the pillar list DP-001…006 explicitly, with an id citation, before doing any design work.
- Existing ID spaces are never renumbered; new ids continue in their own families (DP/UXD/AP/CCR/CV/CX/DIR/RC as established here; FO/F/O/PXE/PR/V/PXO from prior reports).
- No new DECISIONS entries without owner authorization; a *concept approval decision* requires explicit owner action. Until such an entry exists, CX-5 and all DP/UXD/AP/DIR items stay provisional (PROJECT_PROGRESS.md already records that Prompt 5's outputs are user-unapproved).

### What the next authorized research task should address
Per the pipeline's remaining Stage 1 prompts (6–8, order user-authorized): the highest-evidence *bounded* pending design input this report flags for the next research pass is the **economy design structure question** — the market/exchange decision (FO-009/FO-013/FO-022's open question cluster; D-005's write-budget viability; CCR-008's dependency chain) — **provided the user authorizes it explicitly**. Do not begin it now; do not execute any prompt without the user's word.

---

*(End of report. Not to be mistaken for approved design; reader is reminded of [DECISIONS.md](../DECISIONS.md)'s D-003 finding/opportunity-only rule and [AI_CONTEXT.md](../AI_CONTEXT.md) §4's claim-type discipline.)*