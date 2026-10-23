# Stage 1, Prompt 4 — Target Audience, Player Personas, and Player Experience Strategy

**Project X** — original persistent multiplayer browser-based nation-strategy game (fictional, mapless world; shared 2-hour UTC turns, 12/day; free-first infrastructure).
**Report:** v1.0 · 2026-10-22 · author: Prompt 4 session.
**Read first:** [AI_CONTEXT.md](../AI_CONTEXT.md) → [AI_HANDOFF.md](../AI_HANDOFF.md). Sources in [Section 21](#section-21--source-register); prior-report IDs (F-xxx, O-x, FO-xxx) are reused exactly as defined in [Prompt 2](02_strengths_weaknesses_player_frustrations.md) and [Prompt 3](03_feature_comparison_opportunity_analysis.md).

---

## Section 1 — Executive summary

**Tasks completed:** all 18 deliverables. **Recommendation in one line:** design first for *steady-check-in multiplayer strategists* — players who want a persistent world of peers they can develop, trade with, negotiate with, fight, and belong to, in short casual-friendly sessions (1–3 × 5–15 min typical day), with depth that emerges over weeks.

Most important supported findings for audience decisions:

- **A1. The genre's proven sustainable audiences span a productivity spectrum, not a skill spectrum.** NationStates sustains ~290k–"8M nations" scale on a *twice-daily, five-minutes-at-coffee* habit ([NS-1](https://maxbarry.com/2022/11/12/news.html), [NS-2](https://www.superjumpmagazine.com/nationstates-browser-based-games/), [NS-3](https://nationstates.fandom.com/wiki/Issue), [NS-4](https://armaitus.wordpress.com/2011/11/02/nationstates-online-political-roleplaying-game/)); Prosperous Universe sustains spreadsheet-deep optimizers; P&W sustains community-first alliance players [Prompt 2 F-001]. A small, cheap game does not need hardcore reflex players or whale economies — it needs *stayers*.
- **A2. Repeated qualitative signal: low-effort daily habits are real, and the "check-in between other things" pattern is documented in our genre.** One eRepublik player describes a "quick fight in your covfefe break" ([ER-6]); NationStates' cadence is explicitly built around a few decisions per day ([NS-3], [NS-4]). This is *anecdotal* — no survey-quality data was found. Confidence: Moderate.
- **A3. The 2-hour cadence is an *information/notification* design problem more than a participation requirement.** P&W's official materials reward *daily* login, not 12× daily logins ([PW-1]); its 2-hour ticks are background income ([PW-2]). Nothing in official or community evidence demands that players appear at every boundary [Prompt 2 F-009 remains an *absence of evidence* about whether the cadence is loved, not evidence that it works]. Confidence: Moderate.
- **A4. The strongest documented churn risks for our design are: knowledge burden at the door (F-010), first-week multi-cause friction (F-011), veteran/newcomer gap (F-012), waiting-without-feedback (F-021/F-006), and re-entry disorientation (F-023).** Each has a cheap experience-level mitigation documented in the earlier research (O-1/O-2/O-3/O-4/O-12).
- **A5. Social design evidence supports *optional* belonging.** Forced alliance funneling is contested even inside the community proposing it (F-013); the genre's fun engine is groups (F-001); the newcomer question is not "how do we force friends?" but "how do we make not-yet affiliated players respectably busy?" (Prompt 3 FO-004's relationship surface is the structural answer).

**Most consequential open questions** (validation plan in Section 19): which of the two leading audience candidates (casual-leaning world-watchers vs. alliance-community players) constitutes the *primary* early adoption wave; whether a 5–15-min session delivers enough perceived progress (F-021 risk); and what a "reasonable missed-turn experience" is for players in unfavorable time zones.

---

## Section 2 — Scope, method, and evidence standards

**Built on:** Prompt 1 (genre/competitor mechanics + infrastructure limits), Prompt 2 (player-experience evidence: F-001…F-029 findings, O-1…O-12 opportunities), Prompt 3 (feature-comparison matrix; FO-001…FO-027 opportunity register). No full re-research performed; only audience-decision-relevant gaps investigated.

**New research pass (2026-10-22):** three targeted tracks — (1) NationStates audience/motivation evidence; (2) P&W/eRepublik time-commitment, retention/churn and micro-session evidence; (3) Sim Companies/P&W/Prosperous Universe new-player-journey evidence. All delivered source title + URL + type. Findings from the prior reports are reused without re-verification (per the project's own source-of-truth rules); anything re-verified this pass is labeled.

**Evidence labels used in this report** (consistent with Prompt 3's scheme):

- **Verified (V):** supported directly by an accessible official source or directly read page this pass.
- **Repeated qualitative signal (RS):** theme independently reported by multiple sources; *not* prevalence data. Self-selected commenters caveat applies throughout: a strongly upvoted review is evidence the complaint exists, not a population statistic.
- **Reasoned interpretation (RI):** our explanation of what evidence means for Project X.
- **Design hypothesis (H):** a proposition requiring testing (flagged for the validation plan).
- **Unknown (U):** no access or no suitable evidence.
- Evidence-quality labels from Prompt 2's registers (Strong/Moderate/Weak) are quoted where reused.

**Limitations (inherited from Prompts 1–3, unchanged):** Reddit unreadable; Discord/Telegram layers invisible without accounts; Sim Companies official in-app pages app-shell (`[SC-1]` purpose text readable only); no player count/mix statistics in the genre are published researching-grade; all "how many players" statements in this report are qualitative or source-labeled, never invented.

---

## Section 3 — Deliverable 1: Target-audience landscape

Ten candidate segments. These are *behavioral-need clusters*, not demographics; real players span several. Per-segment coverage: motivations, desired activities, decision styles, complexity tolerance, expected cadence behavior, multiplayer appetite, 2-hour-turn compatibility, frustration points, retention hook, leave triggers, Project X fit, evidence, confidence. (Table 3.1 summarizes; prose below adds what tables cannot.)

### 3.1 Nation builders
Grow a country's economy, cities/infrastructure, and capability curve; decisions are allocation choices ("build now vs save now"). Low-to-medium complexity tolerance; prefer clean cost/projection transparency (Prompt 2 F-014/F-022). Sessions: short and habitual (SC/PU/NationStates evidence: minutes-to-an-hour, daily [NS-4], [RS]). 2-hour cadence: excellent — one turn visibly advances the ledger. Frustrations: opaque profitability traps (F-022), early irreversible mistakes (F-026/O-3 family), rigid chore loops (F-019). Retention hook: the next visible milestone (flagship project completion, citygate). Leave trigger: "nothing new to do" (F-006) or punishing decay while away. Project X fit: strong; **FO-002/FO-009/FO-013/FO-014** directly serve them. Evidence: RS (multi-game) + V for systems' existence. Confidence: High.

### 3.2 Political strategists
Domestic policy, governance choices, approval/stability trade-offs, political consequence. Tolerance: medium-high; dislike systems labeled "politics" that don't matter (P&W 2025 thread: "centrally war; politics thin" — F-015). Sessions: variable; often bundled with social play. 2-hour fit: good if policy changes resolve at turn boundaries with visible effects (Prompt 3 FO-005 pattern). Frustration: politics-as-decoration. Retention hook: consequential choices changing national trajectory. Leave trigger: realizing votes/policies have no mechanical teeth. Fit: strong *if* FO-005-class mechanics exist; weak otherwise. Evidence: Weak-Moderate (single strong thread + structural). Confidence: Medium.

### 3.3 Diplomats and negotiators
Treaties, bargaining, reputation, relationships as strategy surface. Decisions: when/what to commit to, with whom. Complexity tolerance: medium; *social* complexity welcome, interface complexity not desired (diploapps minimal tools [FV Prompt 3]). Sessions: irregular, event-driven (a negotiation dramatizes a week). 2-hour fit: excellent — deadline-bound negotiation ("answer the treaty proposal before the 18:00 turn") creates rhythm without reflex demands. Frustrations: invisible past relationships; treaty terms with no consequences; alliance-mandatory diplomacy. Retention hook: to be someone the world must deal with. Leave trigger: nothing to negotiate (empty world / world stagnation — F-003b). Fit: strong; **FO-004/FO-006** are their structural home. Evidence: RS (treaty web usage; eRep/eDom patterns) + V for existing tools. Confidence: Medium-High.

### 3.4 Economic optimizers
Markets, production chains, arbitrage, margin math. Complexity tolerance: high (PU players enjoy spreadsheet-grade depth [PU-3 RS]). Sessions: longer, less frequent; bursts around market shifts. 2-hour fit: excellent (price data accrues per turn; PU/SC run similar loops). Frustrations: fee opacity (F-022), late-entrant niche lockouts, automatable-list grind. Retention hook: informational edge + a resolvable-to-many market. Leave trigger: market stagnation or unwinnable incumbency. Fit: medium-strong; must *not* be the primary pre-release audience to serve, but a healthy market must exist (FO-009) or they bounce. Evidence: RS + V. Confidence: High.

### 3.5 Alliance and community players
Belonging, shared goals, group identity, helping newcomers, organized projects. Complexity tolerance: medium (tools should carry organization burden; F-018 pain). Sessions: variable; the alliance *is* the game for many (F-001 Strong). 2-hour fit: good if coordination tools are async-native (roles, ledgers, scheduled polls at turn boundaries; FO-007/FO-008). Frustrations: admin drudgery, Discord fragmentation, security fears (treasury theft). Retention hooks: group projects; institutional legacy; being needed. Leave triggers: leader burnout (watchlist F-029), group decay while away, application walls. Fit: **strong — this is the segment the genre's evidence says carries retention** (F-001). Evidence: Strong-Moderate (multi-game). Confidence: High.

### 3.6 Military and competitive strategists
Campaigns, counterplay, risk, prestige in conflict. tolerate high complexity; want *concrete rules* and transparent outcomes ([Prompt 2 related: outcome-opaqueness complaint], Prompt 3 FO-010/FO-011). Sessions: event-driven bursts; coalition peaks. 2-hour fit: good (a turn-locked action budget pacing attacks [FV P&W MAP]) *provided* resolution is legible. Frustrations: unfair-range ambushes, protection-gaming, stalemates; being benched during peacetime. Retention hooks: named wars (F-003), rank/prestige, defenses that reward preparation. Leave triggers: repeated unexplainable losses. Fit: strong *if* war design is later-stage-priority; **do not make them the primary design target** (their needs impose high balance scope; Prompt 3 keeps war at "Candidate, minimal-v1" status). Evidence: RS + V. Confidence: Medium.

### 3.7 Roleplayers and narrative-oriented players
National identity, lore, factbooks, emergent history (NS evidence: roleplay mentors/lore as structural pillar [NS-1][NS-2]). Complexity tolerance: low-to-medium *systems*; high *expression*. 2-hour fit: good (daily events become chronicle entries). Frustrations: no place to *write* a nation; purely numerical identity. Retention hook: a page that shows "the story of my nation so far." Leave trigger: nothing to narrate. Fit: medium — **we can scaffold (profiles, news, history logs) cheaply without scripting RP**; they may be a tertiary audience. Evidence: RS (NS/Cantr); games studied here differ in how far they support it. Confidence: Medium.

### 3.8 Casual strategy players
Meaningful decisions, limited time, no obligation culture. Tolerance: low-to-medium. Sessions: 1–2 × 5–15 min [NS-4 anecdote; ER-6 anecdote]. 2-hour fit: excellent *if* progress is visible per turn and missing turns is non-punitive (Section 9's core design commitment). Frustrations: "I must log in 12 times"; chore lists; punishing decay. Retention hook: a world that visibly moved since yesterday. Leave trigger: any FOMO-obligation mechanic (F-019). Fit: strong — candidly *the most probable first-wave adopter* for a new free browser game discovered organically. Evidence: RS (multiple games' low-effort retention patterns + our own O-4 analysis). Confidence: Medium-High.

### 3.9 Hardcore optimization players
Deep systems, experimentation, long arcs, complex interactions. Tolerance: very high. Sessions: long; analytical. 2-hour fit: fine (banking/budgeted action economy rewards planning [FO-010]). Frustrations: shallow systems, discoverable-optimum meta, hidden-in-veteran-hands knowledge. Retention hook: skill expression *within transparent rules*. Leave trigger: mathematically collapsed metas. Fit: secondary — worth one solid depth loop, not a whole design. Evidence: RS (PU/SC). Confidence: Medium.

### 3.10 Socially motivated newcomers
Arrive by invitation or via a friend's/alliance's pitch; would leave quickly if the systems gauntlet is the gateway. Tolerance: low initially. Sessions: short; anchored by the person who brought them. 2-hour fit: fine (they follow one turn's outcome with a guide). Frustrations: jargon walls, mandatory alliance hops, unfriendliness (F-008 signals the opposite works in PU). Retention hook: a first week with (a) one thing to nurse and (b) one person to talk to. Leave trigger: cold empty world + wiki-walled rules (F-010/F-003b). Fit: strong as a **first-week experience problem** rather than a distinct segment. Evidence: RS + discussion of our own acquisition model (H — validationquestion 1). Confidence: Medium.

### 3.11 Landscape comparison table

| # | Segment | Core motivation | Complexity tolerance | Cadence behavior | Multiplayer appetite | 2h-turn fit | Leave trigger headline | Project X fit | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Nation builders | make it grow | low–mid | short daily | medium | Excellent | nothing new to do | Strong (FO-002/009/013/014) | RS+V | High |
| 2 | Political strategists | policy that matters | mid–high | bundled w/ social | medium | Good (if FO-005) | politics-that-doesn't-matter | Medium-Strong | Weak-Mod | Medium |
| 3 | Diplomats | relationships as leverage | mid | event-driven | High | Excellent | nothing to negotiate | Strong (FO-004/006) | RS+V | Medium-High |
| 4 | Economic optimizers | margins & edges | high | longer bursts | medium | Excellent | market stagnation | Medium-Strong (FO-009) | RS+V | High |
| 5 | Alliance/community | belong & accomplish | mid | highly variable | **High** | Good (async tools) | leader burnout / group decay | **Strong (FO-007/008)** | **Strong-Mod** | High |
| 6 | Military/competitive | beat prepared rivals | high | coalition bursts | High | Good (if legible) | opaque unfair losses | Strong-but-late (FO-010/011) | RS+V | Medium |
| 7 | Roleplayers | express a nation | low–mid (systems) | short+daily | medium | Good | nothing to narrate | Medium (scaffold only) | RS | Medium |
| 8 | Casual | meaningful but light | low–mid | 1–2 × 5–15 min | low–med | **Excellent (see §9)** | obligation creep | Strong | RS | Medium-High |
| 9 | Hardcore optimizers | deep puzzles | very high | long sessions | med-high | Fine | collapsed metas | Secondary | RS | Medium |
| 10 | Social newcomers | follow a friend | low initially | guided sessions | High | Fine | cold world + jargon | Strong as *first-week xp* | RS | Medium |

(no forced exclusivity; ordering does not equal priority — see Section 4 of the deliverable sequence for the actual priority decision.)

---

## Section 4 — Deliverable 2: Primary, secondary, and deferred audiences

### 4.1 Primary audience (first playable version): the **steady-check-in multiplayer strategist** (Segments 8 + 1 + the *everyday life* of 5)

**Definition:** players who want a persistent, shared strategic world they can meaningfully engage in **1–3 short sessions a day** (5–15 min typical, longer on occasion), who want their nation to visibly respond to their decisions, who accept that their competitors are other humans *also* being strategic — and who leave if the game demands chore-cadence constant presence or wiki-grade knowledge.

**Why this is the defensible choice:**

1. **The genre's own scale evidence** (NationStates; see [NS-1]: "as many players as ever" after 20 years on twice-daily micro decisions; [NS-3] cadence; [NS-4] 5-min/day anecdote) shows this is the *largest documented stable population in the browser nation genre* — RS, Moderate confidence on size.
2. **Product physics:** free-first, browser-only, 2-hour background ticks. These conditions *naturally* create a low-intensity ambient world. PU would have said "no — target spreadsheet players" because their product is deep. Ours is accessible by construction (Section 2 constraints) — serving this audience is simply honest with what we are building [RI].
3. **Failure-mode evidence:** the documented expense risks (F-019 chore expectations; F-021 waiting-without-reward; F-010 jargon walls) are precisely the *rejection causes* of this segment; conversely the documented cheap wins (O-2/O-4/O-12 turn reporting + visible per-turn progress + re-entry digest) are the *retention knobs* of this segment. Design-for-this-audience ≈ design-anti-churn [RI]. 
4. **Compatibility:** this primary audience *superset-includes* casual nation builders (Seg 1) and the everyday life of alliance players (Seg 5) whose daily instrument is the transparent ledger the builders want (FO-002); the strategic layer (FO-004/FO-006) gives their week texture.

**What the primary audience needs:** a legible per-turn world (reports, provenance — FO-002/FO-015), visible small progress per session (O-4), a week-1 safety ramp (FO-003), a social layer with **optional** affiliation depth (Section 12), no payments-for-power path (F-020/O-11).

**Acceptable compromises:** fewer deep-mechanics systems at v1 (deferred FOs); slower richer-politics rollout; market reduced to listings+reference prices (FO-009 v1 form). **Identity-breaking compromises to avoid:** live participation windows (FO-026 rejected); map-based geography to chase "grand strategy" players; compulsory alliance membership; daily-chore design (violates Section 18's principles).

### 4.2 Secondary audience: the **organized community player** (Segment 5) and the **diplomat** (Segment 3) — served through alliance/diplomacy tooling

Evidence-driven (F-001 Strong; F-018 real admin pain), and structurally served by Prompt 3's Group-A/Candidate tools (FO-004/006/007/008/012). Their *vertical* experiences (treasury rules, bulk actions, treaty authorities) are design-stage work; our audience decision commits only to: **the alliance experience cannot be Discord-only**, and **leadership must not be unpaid-login drudgery**. They tolerate the 2-week learning ramp; we must not base their core loop on it.

### 4.3 Tertiary/future audiences: economic optimizers (Seg 4), competitive strategists (Seg 6), roleplayers (Seg 7), hardcore optimizers (Seg 9)

Serving these at v1's quality bar would each consume scope (markets integrity; war balancing; editor/profile surfaces; deep depth loops; see Prompt 3's per-item complexity labels). They join when the world *has* population for markets and wars to be worth exercising. Post-v1 roadmap hooks: FO-012/FO-014 deepen economy; FO-010/FO-011 war; FO-019 intel; profile/news/chronicle structures for RP.

### 4.4 Audiences that should **not** drive initial design

- **Live-ePlay participation audiences (eRep-class war-cohort rhythms):** rejected outright as incompatible (FO-026 rejection) — their expectations require presence we deliberately do not sell.
- **Whale/monetization-driven power players:** not an audience without a monetization scope (none approved); adopting this priority re-emerges every documented "power gap" failure (F-020). Avoid also because free-first constraint forecloses big prize pools.
- **Grand-strategy map players** chasing borders/tile conquest: structurally incompatible with our confirmed mapless constraint FO-025 "Rejected".
- **Full-SIM politics-institution audiences** (elections/congress mass-voting): FO-023 deferred (needs a population the game won't have at v1).

**Assumptions left untested (logged for Section 19):** that "steady-check-in strategists" in fact find *our fictional, mapless* expression of the genre attractive (no studied game sells maplessness; our differentiation is a hypothesis, not an established demand); that a 5–15-min session is *sufficiently* rewarding (F-021 says not always; FO-002/004 mitigate but this is a design hypothesis); that word-of-mouth/organic adoption can occur without viral loops (we have no funded marketing; see §19 V-1).

---

## Section 5 — Deliverable 3: Player personas

Five personas. Priority labels: **[P] primary**, **[S] secondary**, **[F] future**. Personas are strategic design tools — construction bridges evidence + reasoning; none is presented as a real player; no demographic guessing is used.

### Persona 1 — "Mira, the steady nation-builder" [P]
*Primary.* A capable professional who enjoys strategy in short doses; wants "my country grew because I decided X."

| Field | Content |
|---|---|
| Primary motivations |Visible compounding progress; mastery at comfortable depth; a private-garden feeling in a public world |
| Desired outcomes | A prosperous, well-governed nation whose numbers she can explain |
| Preferred activities | Allocating resources, one policy change, trading, reading turn report |
| Cadence hypothesis | 1–2 sessions/day, 5–20 min, anchored at a turn boundary or (odd-shift work) once/twice-at-rare-noon; catch-up on weekends |
| Complexity attitude | Medium; hostile to wiki-dependent rules; loves in-page explanations (FO-001) |
| Competition attitude | Ambient ranking; not combative; wants to *not* be attacked while growing |
| Cooperation attitude | Trades, treaties-of-friendship, light alliance membership maybe; leader-averse |
| 2h/progression fit | Excellent if turn reports show *why* numbers moved; bad if she must compute decay rules herself (F-010/F-021) |
| Why try Project X | shortcut to "nation strategy" on a laptop, no client, no map-table complexity |
| Why stay | every turn yields a digestible "here's what changed and why" (FO-002); milestones weekly |
| Why disengage | obligation creep; jargon; invisible setbacks; stolen-by-war while unprotected (F-017/MIT—covered by FO-003) |
| Usability needs | keyboard-friendly forms; per-number tooltips; light mobile reading |
| Fairness needs | transparent costs; protection that can't be farmed; no pay-for-power |
| Served by (FO) | FO-001/002/003/009/013/014 |
| Might be alienated by | any pay-for-power path; live-participation events; chore loops |
| Evidence / inference / assumption | RS+RI+HY (session pattern from [NS-4]/[ER-6] is anecdote-level; the *need profile* is evidence-backed via F-006/F-010/F-021/F-022) |

### Persona 2 — "Tomas, the alliance officer & builder" [P→S]
Leads or co-leads an organized group; treats the game as a civic platform. Evidence: P&W's 15-permission matrix usage; F-001/F-018. Sessions: 3–5/day short + 1 weekly planning hour. Wants: role permissions that mean something, shared ledgers, auditability (FO-007), bulk actions to cut drudgery (FO-008), an institution page his members read. Experiences that alienate: Discord-fragmentation (his body of knowledge scattered), admin being *unbounded*, "glorified chat rooms" with no tools. Risks to watch: leader burnout (F-029 watchlist — noted uncertified); the temptation to make membership compulsory. Priority note: serve [P] level support in v1 for *tools*, but not drive entire design; he is the strongest *organic-growth vector* (recruits matter more than ads [RI]).

### Persona 3 — "Yuna, the market optimizer" [S→F]
Spreadsheets, margins, contract negotiation. Evidence: PU's community spreadsheets/price-research stories [PU-3], SC competitive reviews. 2-hour fit excellent. Served by FO-009 v1 market, FO-016 later transparency surfaces. Alienated by: fee surprises, incumbent locks (F-022), pay-gated late-game features (F-020). Priority rationale: v1 market must exist and be *fair*; depth and contracts (FO-021/022) deferred. She is a **second-6-months audience**, not a launch-met audience.

### Persona 4 — "Ade, the diplomatic storyteller" [S]
Loves inter-nation drama, treaties, writing national history. NS/Cantr evidence [NS-2 RS]. Served by FO-004 (relationship-to-history web), news + chronicle surfaces, treaty terms as story (FO-006), in-world biography (alu profile). Low systems tolerance. Pricing:**scaffold, don't script** — we provide forums-free (in-site) channels and event logs; we do not build a lore engine at v1.

### Persona 5 — "Kwame, the competitive strategist" [F]
Reads war math; plans campaigns; respects counterplay. Served (post-v1): FO-010/011/017; DO NOT sell him fake complexity. Alienated by: dominant alliances everywhere, unclear resolution math, being parked in a protection Forever. He is exactly who the genre's existing player base *has* — the risk is building for him *first* (Prompt 3's war-first-fear: highest design-scope risk). Priority: **Future; limited v1 commitments to exist-so-we-can-balance-later.**

### 5.6 Cross-persona tension summary

| Dimension | Mira (builder) | Tomas (alliance) | Yuna (market) | Ade (diplo-story) | Kwame (competitor) |
|---|---|---|---|---|---|
| Wants most | clear per-turn outcomes | shared instruments | margin information | relationship history | transparent war |
| Hates | chores, jargon | admin drudgery | opaque fees | silent world | opaque losses |
| Complexity appetite | low–mid | mid | high | low–mid | high |
| Multiplayer depth | light | deep | medium | medium | deep |
| Priority | **P** | **P–S** | S→F | S | F |

---

## Section 6 — Deliverable 4: Player jobs, motivations, and rewards (jobs-to-be-done)

Format: *the job* → decision types that serve it → progress feedback needed → social context amplifiers → frustration risks → Project X approach (with FO links) → evidence tier.

| # | Job ("when I play, I want to…") | Decisions that fulfill it | Feedback needed | Social amplifier | Frustration risk | Project X approach | Evidence |
|---|---|---|---|---|---|---|---|
| J1 | …see my decisions compound | build/budget allocation | per-turn delta & growing ledger | rankings right-size not race | incrementalism feels dead if invisible | per-turn **provenance report** + milestone log (FO-002/FO-014) | RS (multi-game optimization-love F-002; waiting complaints F-021) |
| J2 | …make consequential choices | policy/treaty/war entry calls | narrated consequence at next boundary | outcomes become news others react to | consequences invisible or tiny | FO-005/006 + FO-002 narration | RS (F-015: politics must *matter*; F-023) |
| J3 | …express a national identity | naming, emblem-ish choices, policy character | the world treats my choices as meaningful | references in news/diplomacy | identity sliders w/o consequence | lightweight national profile + policy-character coherence signals | RS (NS factbooks/lore) |
| J4 | …grow wealth | trade/allocation choices | margin visibility (FO-016 later) | trading relationships | profitability traps (F-022) | FO-009 market with *built-in* reference prices | RS+V |
| J5 | …gain influence & reputation | diplomacy commitments | visible relationship standing (FO-004) | treaties/others react | reputation opaque | FO-004/006 visible typed relationships | RS |
| J6 | …negotiate | treaties/trade agreements | deadline-driven notes; counters | counter-parties react; web shows outcome | negotiation wither (no counterpart) | FO-006 + async negotiation surface | RS |
| J7 | …belong & contribute | alliance roles, projects; helping | group scoreboard/task state | the group itself | admin drudgery (F-018) | FO-007/008 tools + **optional** membership | **Strong** (F-001) |
| J8 | …lead a group | setting courses, delegating | member activeness/at-a-glance | shared rooms | burnout (F-029-watchlist) | FO-008 bulk tools + limits | RS |
| J9 | …outsmart a rival | war/campaign/plan designs | transparent resolution *after* the fact | wars become shared drama | opaque math, unfair ambush | FO-010/011 + FO-002 war reports | RS+V |
| J10 | …react to events | sudden-choice play | events visible *before* resolution | news reactions desktop | surprise departure *unclear* | turn-ahead **visibility** contract (§9.5) | RS |
| J11 | …chronicle a history | accumulating log of national milestones | a story-space (auto-generated) | others read it | no place to be a *nation* | low-cost national timeline (event logs) | RS (NS/Cantr) |
| J12 | …recover from setbacks | restructure after a loss | recovery path is real & explained (no failure-hopium) | alliances help | punishment without repair (F-026/F-017) | FO-003 protection + recovery digest (FO-015) | RS |
| J13 | …master a system | depth investments | mastery = understood rules; **not** hidden formulas | forum/others respect experts | knowledge gate-keeping (F-010) | FO-001 in-page teaching + transparent internals (bounded) | **Strong** (F-010) |
| J14 | …participate in a living world | ambient instruments | the world moved while I slept | others' actions visible | empty-world demotivation [F-003b] | FO-004 network view + news + FO-015 re-entry digest | RS |

**Long-term outcome forms of success** (deliberately plural): economic prosperity (J4), diplomatic influence (J5/J6), political stability (J2), military achievement (J9), institutional legacy (J7/J8), narrative prestige (J11). No single definition is privileged at v1; the visible *ranking* system (post-v1 design) must not conflate all six into one number without design review.

---

## Section 7 — Deliverable 5: Core player-experience promise (PROPOSED)

**One sentence:** *In Project X, your nation matters in a living world — you can understand what happened and why, decide what to do next inside a few short sessions a day, and see other players respond to what you chose to become.*

### 7.2 Intended experience (paragraph)
Project X is a persistent community of nations that keeps turning while you sleep. When you return, the world explains itself: every turn digestible; change narrated; costs and consequences honest. You grow at your own pace — an hour a week or an hour a day both remain rational play. Other players are the real strategic texture: relationships, treaties, trade, and (when chosen) conflict. The systems are transparent enough for a motivated newcomer to *keep up* without external homework — depth comes from *responses to a changing shared world*, not from wall-of-secret math.

### 7.3 Experience pillars (proposed)

| Pillar | What it promises | How we'd know it's achieved (recognizability signal) |
|---|---|---|
| **PX-P1 Legible world** | Any player can interpret why the world is the way it is (turn reports, provenance, costs). | Survey/feedback: "I can explain yesterday's change" yes-rate; support tickets asking "why did X happen?" declining |
| **PX-P2 Fair pacing** | Meaningful play fits short sessions; nothing joins the day that requires being online at fixed times. | Deferrable-action queues empty without penalty; "I felt I *had* to log in at XX:00" complaints stay rare |
| **PX-P3 Play together by choice** | Affiliation is opt-in and supported at every depth; being unaffiliated is respectable, being together is *tool-supported*. | Solo players report independent fun; alliances form without funnel pressure; both stats tracked in feedback |
| **PX-P4 Honest consequences** | Actions have real consequences that are understandable *before* they resolve and reviewable *after* (no "cheated feeling"). | First-loss cases: post-battle reports named factors; dispute tickets unresolvable-by-explanation trend |
| **PX-P5 Safe onramps** | First weeks protect and teach simultaneously; mistake recovery exists. | New-player week-1 retention trend; "found my way" reflections; first-trade friction rate |

### 7.4 Supporting and contradicting decision examples

- Supports: turn reports with provenance (FO-002); stable UTC schedule documented in-service; in-page explanations of every rule surface (FO-001); newborn protection with adversarial review (FO-003); market reference prices (FO-009); re-entry digest for returners (FO-015).
- Contradicts: participation-window raids (FO-026-class); "must log in by 12:00 or lose a day" mechanics; paying for power or late-game social features; rule-affecting knowledge kept in Discord only; "proving" your worth by theatre obligations; burying costs in tiers.

**NOT approved anywhere.** Unless DECISIONS records otherwise, this is a proposed framework whose *violations list is also provisional* — notably "no pay-for-power" is *proposed* as a free-first posture (D-005's hosting framing doesn't yet require it and no monetization decision exists in either direction, so this report explicitly avoids declaring it an approved constraint).

---

## Section 8 — Deliverable 6: First-time player journey (stages A–J)

| Stage | Player goal | Key question | Minimum information | Desired feeling | Friction | Recommended UX response | Evidence/hypothesis label | Success signal |
|---|---|---|---|---|---|---|---|---|
| **A — Discovered the game** | understand what it is | "Is this for me? Will it eat all my time?" | pitch of "nation strategy, turns while you sleep, play in short sessions, no map to learn, multiplayer world of real people" | curiosity, no anxiety | overpromise about depth or instant conquest | landing page with honest time-commitment statement (a design hypothesis, V-6) | H (no evidence on what converts) | landing → registration conversion; expectation-mismatch complaints |
| **B — First visit** | get-what's-going-on | "What do I do?" | 3 fixed elements: *what a turn is*, *what you'll build first*, *how much time it takes* | orientation | everything-at-once screens (F-014 class) | onboarding-first dashboard; a single obvious CTA ("Choose your nation") | RI (competitor onboarding evidence PU/SC/NS) | % leaving landing page without CTA interaction |
| **C — Registration & account** | get in quickly | "How much info?" | one short form; e-mail/username+password; no optional personal data unless needed | speed | multi-step forms; vague terms | minimal fields; abuse defenses *informed* but not user-hostile (anti-multi is design-stage) | RI | form-abandonment rate | 
| **D — Nation creation** | define themselves | "What will my nation be?" | name + 2–3 *low-stakes, un-regretable* orientation choices | ownership | choices that feel consequential-yet-irreversible (F-026/F-012) | few irreversible options; tooltips ("this choice affects Y: later, at cost Z") | H (validated in prototype) | nation-creation completion %; wrong-expectation reports |
| **E — First session** | accomplish one thing | "What is my first decision?" | one *guided but tactically-meaningful* first decision; light explanation inline | "I made a decision and it was mine" | tutorial dump | interactive first-decision pattern; FO-001 tooltips where explanation is needed | RI (competitor guided-start evidence) | first-decision completion rate |
| **F — First turn boundary** | see consequences | "Did it work? What happened?" | a turn report with *why* — deltas narrated | awe of change | numbers without meaning (F-010) | per-turn digest — the FO-002 deliverable | RI (this is the single highest-leverage moment; see [§9.5]) | report-read rate; follow-up action taken within session |
| **G — First day complete** | feel established | "What's next?" | a short *suggested goal path* (FO-003) | momentum | chore-fragmentation | one next-goal, rest visible but not compulsory | RS (NS objectives pattern [PW-3]) | session 2 occurs same-day |
| **H — First week** | grow competence | "How deep does this go?" | progressive disclosure of systems; always-searchable glossary (FO-001); protection window visible+expiring (FO-003) | growing mastery, safe  | wall-of-features | systems unlock *on the basis of context*, not time alone *(design H)* | RS (F-011 multi-cause friction; P&W objectives set) | week-1 retention; support-topic counts |
| **I — First social contact** | find people (if wanted) | "Who's out here?" | visible world: other nations' pages, a news feed, alliance openings (non-mandatory) [F-013 lesson: don't force] | welcoming | elitist/non-responsive rooms; no integration to any | profile pages + world news + "open groups" list (FO-007 minimal) | RS (F-008 PU evidence; F-013 debate; F-003b empty-world risk) | first social interaction occurs *and is* positively evaluated (qualitative) |
| **J — First setback** | recover and learn | "Is my nation ruined?" | the loss explained; a *recovery path* visible; protection/fairness rules clear | resilience, not rage-quit | ruin-feeling (P&W restart-request [F-026]); opaque loss | setback digest with cause-and-effect narrative; no fail-state beyond rules-declared ones; design-stage H about war-loss magnitude | RS (F-017 exploit complaints; F-012 gap) | player returns within 48h of first loss; loss-related churn trend |

**Longer-term continuation notes (first month, beyond):** the goals ladder (J1/J9) ends anywhere; there should then be **generative goals** (world-changing events, alliance institutional projects); a *story* surface makes the game last (J11). Post-v1 designs must answer F-025 (late-game scarcity) — noted, not solved this pass.

---

## Section 9 — Deliverable 7: The two-hour turn experience

**Policy bottom-line (proposed):** *no player is ever owed presence at a turn boundary.* The turn is the world's metronome; the player's calendar is private.

1. **Planning before resolution:** the interface should show, at any moment: pending actions, their costs, the *next* boundary time in UTC (+local label). *(interface task)*
2. **When actions take effect:** contracts of effect — immediate / at-boundary / conditional — must be visible at decision time, not remembered lore (FO-001 strategy). *(interface task)*
3. **Seeing meaningful results:** every boundary should yield at most one screen of what-changed-why (FO-002). Over-completeness is a design-stage decision. *(interface+mechanic H)*
4. **Decisions between turns:** queuing is the default affordance — many decisions are naturally "set orders and live your life" (P&W-pattern; our own FO-010 FO-014). *(mechanic pattern)*
5. **One-or-two-a-day players** (Mira): the re-entry digest + due-items queue — the day is safe if you arrive once (FO-015). *(interface task)*
6. **Frequent players** (Tomas): we avoid rewarding *attendance at boundaries* with bonuses (this would manufacture FOMO): no "be online at 12:00" mechanics. Rather, the frequent use-case is *attention-limited group strategy* — balance-awareness, not timing races. *(policy)*
7. **Can't play at specific hours (time zones)** (Work-shifted players): nothing may be structurally *locked* by local clock except the shared clock itself; scheduling-sensitive options (e.g., a treaty window) must have multi-day validity so every time zone can participate once. *(policy; mechanic H)*
8. **Missing several turns:** absence is a state, not a sin: missed turns *resolve without player horror* if no irreversible window was open; the re-entry digest must carry the reading-order (FO-015). Any decay/production-continuation has a **cap** so a vacation is a pause, not an apocalypse (design-stage). *(mechanic H; adversarially to F-017)*
9. **Newcomers in an old world:** catch-up is a major design-station (FO-018 Needs Research); *experience-level* interim answer: onboarding rails are not affected by world age (the same first-week experience works day 1 or day 200). *(interface commitment)*
10. **Coordinated alliance activity:** coordination is **turn-anchored, not minute-anchored**: votes/orders resolve at boundary; live rooms optional. *(policy)*
11. **Time-sensitive diplomacy/military decisions:** where timing *has* teeth (a war declaration deadline), deadlines must be generous (≥1 day) and visible in *both* UTC and localhabit label. *(interface task)*
12. **Server delays / failed turns:** the outcome should never *look* like a player error: transparent incident-neutral language ("world caught up—at 14:05; your queued actions resolved"); no missed-window punishments for processing failures. *(interface task; architecture must be idempotent [Prompt-1 §6.1 requirement])*
13. **Time-zone fairness & notification preferences (policy §18):** notificationstogglable per-category, batched, digest-choice at most 1/day + event-triggered ones for *consequential* changes only. *(interface task)*
14. **Never-constantly-online principle (the whole §9 compressed):** a design is anti-this-report if a mechanic's value flips only when a player is present at a boundary (live-window mechanics [FO-026 rationale]) or inverts absence into punishment without explanation.

**Both extremes audited:** too slow (12 rewards/day *that nobody can feel*) fails if per-turn deltas are trivial: fix = make the *day* a meaningful macro-cycle (production goals completing across ~2 days) without *manufacturing* urgency. Too demanding: any mechanic that *requires* boundary presence fails this report. 

**PG: this deliverable proposes requirements for §interface behavior at turn boundaries (FO-002/FO-015 implementation contracts); it does not approve any mechanic.**

---

## Section 10 — Deliverable 8: Session patterns & time-commitment philosophy

| Pattern | What happens | Who it fits | Expectation to fulfill | Friction risk | Coexists with 2h cadence? | Must never demand |
|---|---|---|---|---|---|---|
| **P-A: Short check-in** (5–15 min, 1–2×/day) | read digest → resolve queue → one decision → glance at news | Mira primary | at least one *meaningful* decision-able; visible progress without busywork | "nothing to do" (F-021) | **Yes — this is the cadence's natural mode** | Log-in- rituals; reboots of the same screen reading 
| **P-B: Working session** (30–90 min, occasional, e.g. weekly) | plan production, negotiate treaties, write | all, esp. Tomas/Ade/Yuna | depth is *available* by choice (browsing history, projecting) | no deep surface to work in | Yes (world had time to accumulate) | that planning only "counts" at minute-granular deadlines |
| **P-C: Event-driven peak session** (economic window, war-coordination, group crisis) | joint mobilization | alliance/competitive personas | one shared target, clear roles, async-first coordination tools | race-to-time gameplay | Yes, if coordination resolves at *boundaries* | live participation windows (conflict with FO-026-rejection) |

**Time-commitment philosophy (proposed):**
- Meaningful must **fit** free time, not consume it; growth is a function of *decisions* not *session minutes*. (This is the report's most load-bearing hypothesis — validation V-4.)
- We avoid: daily-chore lists styled as progression (F-019 eRep evidence), artificial wait/walled grind to stretch content, notifications as engagement levers, achievements that require streaks. Such patterns raise *session* metrics and lower *trust* — the failure mode of our genre's documented monetization-pressure era (F-020).
- Acceptable long-session play exists for those who want it; the difference between persona Mira and Kwame is *when their depth unlocks*, not whether they're allowed it.

---

## Section 11 — Deliverable 9: Complexity, learning, and mastery

**Distinctions the design must maintain:** strategically deep ≠ poorly explained; useful uncertainty ≠ hidden essential info; skill-of-decisions ≠ hours-available. (Prompt 2 F-010/F-013; Prompt 3 FO-001.)

**Complexity framework (proposed):**

| Tier | What it contains | When delivered | Examples (not finalized) |
|---|---|---|---|
| **C0 Immediate essentials** | What a turn is; where my nation stands; where my decision buttons are; how I see consequences | literally first interaction | the five surfaces: nation board, turn report, action queue, market index, news |
| **C1 Early learnings (week 1)** | economy basics (production/flows/upkeep), how trade works at listing level, how to read another nation's public profile | in-context, FO-001 glossary + guided dock | tooltips on every number; "first trade" mission |
| **C2 Intermediate concepts (weeks 2–5)** | policy trade-offs; treaty types & their consequences; alliance roles/taxes; military readiness & budget (if wars not chosen) | as the player reaches contexts | treaty web walkthrough; alliance bank tour |
| **C3 Advanced mastery (months)** | market arbitrage; bulk alliance ops; war counter-play nuances; re-specialization trade-offs | on-demand depth surfaces; community escalation | deep economics raw charts (FO-016); war-case studies |
| **On-demand info** | any number's provenance ("why is upkeep $X: formula & factors") | search at will; avoid forced reading | FO-001 "explain this number" |

**Delivery strategy (proposed):** progressive disclosure governed by *need* (you meet the concept when relevant), not just by linear checklists; worked examples for ambiguous firsts (a first trade preview); *searchable reference* always available (Protects against documentation decay — F-027 — because it's shipped with the game, not outsourced). We simplify **explanations**; we do not simplify **rules** to look nicer. depth supply stays honest (C3 can be rich without deception).

**Boundaries:** do not onboard players onto systems that don't exist yet (politics/war depth) — launch-limited depth is a stated limitation, not a cowardice; keep C0/C1 the *whole* of v1's teaching burden; the number of concept families a v1 player must master is a *testable number* (validation V-5).

---

## Section 12 — Deliverable 10: Social experience and community

### 12.1 Affiliation spectrum experiences (each a *taste* to design for; none approved)

| State | Experience sketch | Design challenge | cheap v1 shape |
|---|---|---|---|
| **Independent** | respectable play alone: trading, growing, riding the news | be *interesting alone* (news, market, world texture) | world surfaces above + solo achievements none-chorey |
| **Curious → first contact** | see a nation, negotiate lightly, join nothing | low-stakes first socialization | post/DM/neighbor-treaty structure; no "applicant funnel" |
| **Member** | role with tools, shared bank visibility, group goals | role clarity without bureaucracy | FO-007 minimal roles; ledger view |
| **Officer/Leader** | delegation, diplomacy, campaign planning | protect against unpaid-drudgery | FO-008 bulk actions; delegation is *in-game*; audittee (FO-007) |
| **Group coordinator at scale** | inter-alliance negotiation/summit politics | legible collective diplomacy | FO-004/006; treaty web |
| **Leaver / inactive** | exit friendly, no role-locks or punishment | free exits; records persist | profile-visible history remains |

### 12.2 Risks and lightweight safeguards (theme table)

| Risk | Reality-check evidence | Cheap safeguard direction | What needs more tools later |
|---|---|---|---|
| Established groups dominate newcomers | contested idea (F-012 resolution is FO-018-level; F-016 smaller-nation debate); funneling debate (F-013) | visible protection states (FO-003); formal alliance *openness* listing so newcomers can find groups voluntarily | none at v1 |
| Social exclusion / unwelcoming vets | F-008 shows kindness works in PU; games without seeded kindness suffer | early "welcome-culture" seeding — invite-mission templates; visibility of helpers | moderation tools growth |
| Leader burnout | F-018 documented admin pain; F-029 *watchlist* (unverified) | tools-first (FO-008); role separation | later: activity caps |
| Excessive communication demands | auto-debates (P&W automation debate) | async-first coordination (turn-anchored) | none likely |
| Harassment/intimidation | [*unknown this pass; genre-adjacent not invented*] | report/report-flow + visible moderation policy; content rules apply in-game text | moderation capacity decision (**flag: needs a real plan at launch; small world first**) |
| Coordinated abuse (multis, bot rings) | P&W rules ban automation/anti-multis [FV Prompt-3 P28] | identity requirements (C/D stage), anti-multi rules from design-stage | machine-AI detection later |
| Information overload | the *oldest* documented genre pain (F-010) | digests not streams; C0–C3 scaffolding | customization UI later |
| Forced alliance | eRep/P&W real debates (F-013) | **never** mechanically funnel; opt-in surfaces only | — |
| Newcomer dependency on veterans for basics | F-010 in-game knowledge vacuum | self-serve documentation (FO-001) from day one | — |

**Social principles (proposed, brief):** communication is turn-anchored, not live-locked; membership is *never* compulsory; leaders get tools, not checkboxes; abuse cases get *visible*, honest process even when the world is small; solo play is a legitimate first-class existence (see PX-P3, §7.3).

---

## Section 13 — Deliverable 11: Fairness, agency, and player trust

### 13.1 Fairness axes (genre-weighted)

| Axis | Meaningful disadvantage (acceptable) | Unfair-feeling disadvantage (design against) | Mitigation direction |
|---|---|---|---|
| Information | rivals know more because they studied/market-timed | rivals know more because *rules are unverifiable in-service* | FO-001/FO-002; rules pages ship with game (O-10 family) |
| Time available | diplomats reach further because they played regularly | war/decay punishes a person for *life schedule* (shift-worker double-jeopardy) | §9 policy; seeded asynchronous windows |
| Experience & knowledge | finesse differences | wiki-outsourced math (F-010 evidence: community keeps formula docs *because games don't*) | FO-001/FO-002 transparency bounds |
| Group power | large alliances yield coordination advantages (fine) | gangs can farm weaker players under rules (the F-017 engineering world) | FO-003/FO-017 adversarial design; war entry gates |
| Recovery | you lost a battle and must rebuild | a silly thing at day 3 makes long-run play worse forever (F-026/F-012) | recovery paths (FO-003); no "ruin" outside declared rules; re-entry digest |
| Competition transparency | you were outmaneuvered — and can see why | you were outmaneuvered and *can't tell why* (community writes formula wikis to fix this — F-014 class) | post-event reports with named factors (FO-002 war reports) |

### 13.2 "Perceived unfair even when rules applied correctly" (genre-real cases) and their experience-level fixes

- **Out-of-range aggression** felt as no-warning ambush → any turn-ahead visibility contract (§9.5, ahead-of-resolution states) + range lint explanation.
- **Protection confusions** — beige-adjacent designs get gamed (F-017); the *bystander* sees a protected player as either angel or cheat; the interface must *name states publicly* so third parties don't invent rumors.
- **Fee/economic opacities** — a tax or market deductions visible only post-loss reads as "the game lied" (F-022/F-020 evidence in other games). **Fix:** before-the-action price preview *everywhere numbers change money* (cheap, pure UI).
- **Turn-absence asymmetry** — being offline during a strategic window (e.g., a war) feels unfair *even mechanically fair*; fix = generous deadlines + the absence-digest; also a *declared* simultaneity contract ("durables resolve at boundary for everyone, no matter when you acted").

**No promise of equal outcomes** — equal opportunity, unequal strategic results. This is not an emotional hedge; it's core to the genre's competitive pleasure (J9) and should be *stated* in new-player communication to govern expectations.

---

## Section 14 — Deliverable 12: Retention without exploitative design

### 14.1 Positive return-reasons (as built-up surface, not mechanics)

Following-through a plan across days (J1); turn stories (F-003 war histories; treaty sagas) (J11/J2); community work (J7/J8); negotiating something that mattered (J6); mastering a system (J13); world texture (J14 — market moves, seasons, events [FO-020 note]; being reacted-to (world news responsiveness).

### 14.2 The anti-pattern blocklist (proposed as design principle PR-10's concrete face)

| Anti-pattern | Why genre evidence flags it | Our commitment |
|---|---|---|
| FOMO by manufactured deadlines | the *whole* genre hates it in eRep form (F-019; ER-6 pop-up complaint) | deadlines exist only where strategy requires them, generous, and announced |
| Daily mandatory check-ins styled as progress | eRep daily-tasks complaints; SC waiting complaints co-occur (F-021) | queue-based, no streaks, no "attendance" bonuses |
| Punishing reasonable absence | eRep returning-player essays (F-023); F-017 family | absence is respected; digests not dread |
| Alert fatigue | ER-6 notification complaints | per-category toggles; digest batching; no alert-spam |
| Sunk-cost cultivation | retirement essays of every long-runner | no variable-reward surfaces; exits stay possible |
| Pay-for-power or pay-for-social gears | F-020 documented across 3 games | no such product surface exists in our *proposed* scope; note: monetization is otherwise undecided (§7.4) |

### 14.3 Notification policy direction (user-controlled support, not a demand system)

Default: digests (1 daily + alert-on-*consequential* only: attacker-declared war on you, treasury event, treaty action on you); granular off-switches; no alerts about nothing; "seen twice? → it's not an alert" (subject to design-stage).

---

## Section 15 — Deliverable 13: Accessibility and usability needs

| Need | Priority | Low-cost baseline | Notes |
|---|---|---|---|
| Desktop+mobile-browser legibility | P0 | responsive tables; mobile is a *reading/messaging* surface v1, growth surface later | turn-report reading on a phone in a break = core primary-audience moment |
| Dense tables made readable | P0 | tables with row-scanhierarchy; fixed decimal alignment; keep tables short | F-014 across games |
| Status clarity (e.g., is my action pending?) | P0 | one status language (pending/queued/resolved/cancelled), always explainable (FO-001) | |
| Error messages that explain | P0 | "what failed / why / what to do" | |
| Color independence | P1 | shapes/icons accompany color | cheap from day one |
| Keyboard usability where sensible | P1 | forms/tab-order | full accessibility audit is later work |
| Confirmation for consequential actions | P0 | explicit preview windows (battle declarations; treaty; orders) | "what will happen at next boundary" preview |
| Help discoverability | P0 | "? explain this" affordance near every novel surface (FO-001) | |
| Returner comprehension (several days off) | P0 | FO-015 re-entry digest | |
| Reduced motion / no distracting animation | P1 | minimal animation baseline | near-zero effort; removes a whole complaint class |
| Avoid unnecessary UI time-pressure | P0 | no self-destructing dialogs; "no countdown" rule *except* genuinely deadline-bound strategic windows | carries §9's philosophy into pixels |

**P2/later (not v1):** light/dark themes beyond default; localization; screen-reader deep-audio pass; mobile-app-grade gesture surfaces.

---

## Section 16 — Deliverable 14: Failure modes and early warning signals (PXE register)

Severity × likelihood judgment (qualitative; explicitly analyst estimates); IDs stable for lifecycle (PXE-xxx). "Test in prototype" columns.

| ID | Risk | Personas hit | Sev | Like | Confidence | Consequence | Prevention shape | Early-warning signal | Testable pre-launch? |
|---|---|---|---|---|---|---|---|---|---|
| PXE-001 | Newcomer doesn't "get it" in first visit (genre purpose opaque) | all | High | High | RS | instant bounce | Landing + C0 framing; expectation messaging | landing→register conversion | Yes (mock test) |
| PXE-002 | First useful decision arrives too late | Mira | High | Med | RS | day-1 churn | session-E first-decision design | first-session decision rate | Yes |
| PXE-003 | Turn cycle *feels* lifeless or too slow (nothing changed) | Mira | High | Med- High | RS + F-021 | churn on week 1 | FO-002 quality; day-arc balancing | digest-reading drop-off; "boring" mention rate | Beta |
| PXE-004 | Turn-feels-like-obligation (FOMO creep) | all | High | Low-Med | H | retention of wrong kind; trust decay | PR-10; no boundary-attendance bonuses | complaint language "had to" | Beta |
| PXE-005 | Returning player can't reassemble (world confusing) | all, Tomas | High | Med | F-023 | re-entry churn | FO-015 digest | digest-unopened; returner-2-week churn gap | Beta |
| PXE-006 | Game rewards hours more than judgment | Mira vs Kwame | High | Med-High | F-019/F-021/F-022/treaty debates | wrong audience, grind resentment | PR-2/PR-3 | time-vs progression correlation anomaly (survey) | Beta |
| PXE-007 | Newcomers find no meaningful role (nobody needs me yet) | social-newcomer | Med-High | Med- High | F-012 world stage | early churn | FO-003 path + onboarding; options to matter cheaply | first-week peace/role satisfaction | Yes (beta) |
| PXE-008 | Alliance membership becomes socially compulsory | Mira | High | Med | F-013 + F-017 debate | wrong retention; solo exodus | PR-5; presence of *meaningful solo arc* | (solo players' 30-day retention delta vs members) | Beta |
| PXE-009 | Economic optimization unknowable → outsiders stumble into traps | Yuna, | High | Med | F-022 | economic churn | FO-016-ish; margin previews | first-trade experience reports | Beta |
| PXE-010 | War dominance / diplomacy overshadowed | Ade/Mira | Med-High | genre-known | F-015 | wrong flavor emerges | war-visibility design care; politics-teeth (FO-005) | share-of-outcomes sentiment | Beta |
| PXE-011 | Social conflict poisons a small launch community | all | Med-High | Med- High | genre-adjacent real (F-008 opposite evidence) | exodus wave | visible moderation posture at launch | report rate vs warm language share | Partial (policy prototype) |
| PXE-012 | First mistake = long-run ruin | Mira | High | Med | F-026/F-012 | rage-quits | never-ruin rules; FO-003 | return-after-fatality | Beta |
| PXE-013 | Players can't tell whether actions had an effect | all | High | Med | F-010/F-014 | faith collapse | FO-002 provenance | "why did X happen" support tickets | Beta |
| PXE-014 | Busywork replaces choice (turn-tune chores) | Mira | High | Med | F-019 | grind resentment | PR-2; drain-taxonomy care (FO-014) | "cheat-like" automation urge (iset discussions) | Beta |
| PXE-015 | World feels empty: other players invisible | all | High | **High (small-launch)** | F-003b, F-021 | core failure of a small world | launch-world seeding; FO-004 surfaces; social design | concurrents clustering; news volume | Beta |
| PXE-016 | Rules hidden in external docs (jargon wall) | all | High | High | **F-010** | knowledge gate-keeping | FO-001 from day 1; O-10 maintained docs | external-doc reliance share | Yes (content test) |
| PXE-017 | Notification fatigue | all | Med | Med | ER-6 | trust damage | §14.3 | notification-off rates | Beta |
| PXE-018 | Veteran experience shallow (nothing to master) | Kwame/Yuna | Med | Med | F-025 CST | veteran churn | C3 depth supply; watch post-v1 | weekly active veterans trend | Later |
| PXE-019 | Trying to be all audiences → for all, for none | product-level | High | Low-Med | RI | identity diffusion | this report's audience strategy | scope-creep drift review at design gates | Design review |

**Recommended prototype/beta test set (bounded, small-cost):** PXE-001/002/003/007 purely by mockups & world sim; PXE-013 via FO-002 prototype; PXE-015 seeded group flow; PXE-016 doc-content test. **Do not** build analytics infrastructure beyond event counters + a feedback thread in the pre-launch stages.

---

## Section 17 — Deliverable 15: Player-experience principles (PROPOSED)

Ten principles. Each: name / statement / need protected / evidence-reason / supporting-example / violating-example / evaluation method / priority & confidence. **All PROPOSED; DECISIONS.md approved none.**

| ID | Principle | Statement | Need protected | Evidence/reason | Follows (-example) | Violates (-example) | Evaluation | Priority/Conf |
|---|---|---|---|---|---|---|---|---|
| PR-1 | **The world explains itself** | Costs, formulas and consequences are discoverable in-service, never behind external docs or community-only knowledge. | F-010 newcomers | Strong genre evidence | why-was-this-cost? drill-down everywhere | "ask on Discord/see wiki" as rule resolution | content audit; complaint tickets | P0/High |
| PR-2 | **Sessions earn choices, not attendance** | Games progress on decisions, not log-ins; no mechanic rewards presence at a boundary nor punishes reasonable absence | F-019/F-021 | Strong eRep/SC evidence | queue systems；no streak bonuses | "must return by noon or lost day" | user complaints language; absence-impact stats | P0/High |
| PR-3 | **One real decision per short session** | A 5–15 min session always leaves with something meaningful done and visible. | F-021 waiting fear | RS; F-002 optimization-love | turn-report ends→decision-ready action maquet | turn output requiring 40-min spiral | session-length X decision-rate correlation | P1/High |
| PR-4 | **Consequences explained before & after** | All outcomes narrated honestly: before (what will happen at boundary, classed) and after (what happened & why). | F-014/F-017 + trade scams | RS+V | preview + provenance delivery (FO-002) | outcome-visible only post-hoc w/o reasons | anomalous-outcome ticket rates | P0/High |
| PR-5 | **Affiliation is optional; support is internal** | Belonging is offered, never orchestrated; alliance tools exist in-game (no Discord-mandatory). | F-001/F-013/F-018 | Strong | FO-003 voluntary openings | auto-funneling to alliances; requiring Discord for rules | comparison of solo/member retention | P1/Med-High |
| PR-6 | **Fairness is *visible*** | Protection/restriction states are publicly named, and their exits/cooldowns explained — no secret states delegated to rumor. | F-017; bystander confusion | RS+V | public nation states | beige-like hidden states | abused-state anecdote audit | P1/Med-High |
| PR-7 | **Recovery is a designed state** | Every disposition-damage-point has an intended recovery mechanism or is explicitly declared no-recovery. | F-026/F-012 | RS | loss digest + rebuild path | quiet permanent descoping | return-after-loss rate | P1/Med |
| PR-8 | **Multiple wins are real wins** | Economic, diplomatic, political, institutional, narrative, military success each have legitimate visible rewards; no single score "true". | all members thrives | RS (multi-motivation evidence) | wall awards per axis | singleकs score supremacy | rank usage sentiment | P2/Med |
| PR-9 | **Respect for attention** | Notification design never manufactures urgency; digests exist; no "check now" spam. | burnout/annoyance | ER-6 + F-020 | digestion batching | multiple daily "you must act NOW!" pings | opt-out rate per category | P1/High |
| PR-10 | **Free-to-fair operations** | Player-experience commitments come before monetization pressure: we do not reproduce any documented genre pay-power patterns. | F-020/free-first identity | RS documented; our own project's posture | market fee *free preview*; reference prices | boosts-shaped commerce | fee-scheme review at design gates | P1/Med-High (framework unapproved) |

---

## Section 18 — Deliverable 16: Experience opportunity register (PXO-###)

Universe basis: problems left open by my analysis; each maps (only where genuine) to a Prompt 3 FO. Each: PXO-ID / name / problem / target persona / why it matters / experience-level response / evidence / confidence / expected benefit / complexity (Low/Med/High) / ops-moderation burden / dependencies / negative side effects / validation shape / priority (P0/P1/P2/Defer).

| ID | Name | Problem/persona | Response | Evidence→Conf | Complexity | Deps | Sides | Validation | Priority |
|---|---|---|---|---|---|---|---|---|---|
| PXO-001 | **Landing honesty pack** ("what this game asks of your time") | expected-time & genre translation wrongness at bust | landing page contract + expectation set (§8-A) | H → Low | Low | copy/design | marketing honesty constrains pitch | A/B landing test | **P0** |
| PXO-002 | **Turn-report provenance v1** | every number has why | FO-002's *report surface at v1 scope* | RS → Med-High | High | FO-002/turn-engine | reveals balance internals | digest-comprehension test | **P0** |
| PXO-003 | **World-serialization contract** (what resolves when) | player certainty about when things *take effect* | three-class contract visible at decision time (immediate/queue/at-boundary) | RI → High | Low | UI layer | limits flexibility at v1 design | scenario walk test | **P0** |
| PXO-004 | **First-decision moment** | tutorial dump fails | one guided-but-real first decision (§8-E) | RS → Med | Low-Med | content | could feel scripted | first-decision completion & sentiment | **P0** |
| PXO-005 | **One-screen turn digest** | information overload vs boredom balance force | turn output as single digest with optional details | RS → Med-High | Med | FO-002 | hides detail behind second level | digest-read-rate | **P0** |
| PXO-006 | **Recovery digest after setbacks** | first loss feels like ruin | setback explanation + path (§8-J) | RS → Med | Med | FO-015/003 | could soften strategy stakes | return-after-loss rate | **P1** |
| PXO-007 | **Week-1 goal ladder** | aims drift | 5–8-goal starter path (FO-003 adjacent) | RS → Med | Low-Med | content | feels on-rails if strict | week-1 progression cohort | **P1** |
| PXO-008 | **Explain-this-number** | jargon wall | contextual help affordance (FO-001) | RS → High | Low-Med | content engine | tooltips over-checked becomes nag | tooltip use on novel surfaces | **P1** |
| PXO-009 | **Open-groups directory** | newcomers can't find affiliations voluntarily | alliance openings listed (in-game) | F-013 → Med | Low-Med | alliance tools | promotes grouping trend | directory→first-contact rate | **P1** |
| PXO-010 | **Price-preview everywhere money moves** | fee/loss surprises read as deceit | before-confirm preview of every money action | F-022 → High | Low | UI | n/a | pre-trade preview usage | **P1** |
| PXO-011 | **Notification contract** | alert fatigue | category toggles + digest batching + consequential-only alerts | ER-6 → Med | Low-Med | push infra | slows "must-know" moments | per-category opt-out stats | **P1** |
| PXO-012 | **Re-entry digest (returners)** | what changed while away? | FO-015's flow v1 | F-023 → Med | Low-Med | FO-002 | over-length digest fatigue | returner-2nd-session rate | **P1** |
| PXO-013 | **National timeline (story surface)** | identity persistence | auto-generated milestone log/persona Ade | RS → Med | Low-Med | event logs | surface clutter | profile visits | **P1** |
| PXO-014 | **Turn-ahead visibility contract** | ambush-feel (rages) | pending-actions & announced windows visible (§9.5/§9.11) | RI → Med-High | MED | rules UI | reduces "surprise element" as strategy | declared-war-rage complaint rate | **P1** |
| PXO-015 | **Searchable reference/glossary** | knowledge decay (F-027) | maintained in-game doc (O-10/FO-001) | Strong → High | Low-Med | content ops | maintenance obligation | doc-freshness checks | **P1** |
| PXO-016 | **Time-zone fairness statement** | schedule-locked feelings | multi-day-confirmed window rights + clock labels (UTC + local) | §9 → Med | Low | UI | — | complaint-free windows | **P1** |
| PXO-017 | **Solo-respectability pass** | independent players crowded out | solo-usable surfaces in every system; solo achievements optional | F-013-gap analysis → Med | MED | design | belittles group play? | solo 30-day retention | **P1/P2** |
| PXO-018 | **Market-integrity onboarding** | newcomer trades get burned (fees/collusion) | onboarding cards + young-nation trade guides (FO-009 v1 rules), market preview | F-022 → Med | MED | FO-009 | trade skill reduced? | newcomer scam-loss rate | **P1** |
| PXO-019 | **Group-health indicator for leaders** | admin burden invisible (F-018) | role/membership status surfaces v1-min (FO-007 first slice) | RS → Med | Low-Med | alliance tools | feels surveillance-ish | leader-reported burden qualitative | **P2** |
| PXO-020 | **Content-localization pass** | accessibility for non-anglo markets | untranslated is fine at v1; keep strings localizable | U → Low | Low | nothing to design | reduces early translation quality | — | **Defer** |
| PXO-021 | **Companion mobile-experience pass** | Mira's work-break reading | responsive tables + digest-via-phone | RS (primary-audience persona) → Med | MED | responsive CSS | scope slip risk | mobile-return-usage rate | **P2** |
| PXO-022 | **Analytics-lite hitmap** | can't measure PXE signals | page/action counters + feedback thread only (no big analytics) | RI → High | Low | nothing to design | privacy design choices | — | **P1** |

**Highest-priority set (P0/P1, bounded):** PXO-001 → 006 + 008/010/011/012. These are the *interface/content cube* of the experience promise (§7); untouched-by-this-report are economy/war *mechanics* (stay in FO space).

---

## Section 19 — Deliverable 17: Research gaps and validation plan

| V-ID | Open question | Why it matters | Current assumption | Confidence | Cheapest credible method | Evidence that would change our recommendation | Must answer before prototype? |
|---|---|---|---|---|---|---|---|
| V-1 | Which of two candidate primary-adopters actually arrives at a *mapless* nation game (casual-leaning watchers vs alliance-led cohorts)? | audience & launch economics | casual-leaning + community-led spread | Low (no prioritized mapless-game audience data exists in studied games) | concept test page + 5–8 short interviews of genre players + option: seeded Discord pilot | strong alliance-first demand sign | No (design can accommodate either in early surfaces) |
| V-2 | What does a 5–15 min session need to deliver to feel progressed? | session pattern P-A solving F-021 | ≥1 meaningful decision + visible change | Med | clickable mock test on 3 session plans | wait-complaints persist | Before commit (P0) |
| V-3 | What is a *reasonable* missed-turn experience (absence design)? | Section 9, item 8 — "Missing several turns"; FO-015 boundary | digest + no-punish default | Med | absence prototype scenario (beta) | absence resentment invoices | Before beta |
| V-4 | Is "the world explains itself" partnership or exposure problem (provenance reveal vs mystery)? | FO-001/FO-002 depth policy | transparency-first | Med-High | digest A/B (transparent vs opaque variants) | experts object overwhelmingly that it kills strategema kind | Design-stage admit decision |
| V-5 | How many concept-families can a v1 player absorb before overwhelm? | C0–C3 framework | ≤4 at v1 | Med | interview + incremental disclosure test | overwhelm complaints collapse | Before beta |
| V-6 | Does honest-expectation messaging *reduce* conversion more than it *improves* retention? | PXO-001 | honesty-net-positive | Med | landing A/B | labor to see comms costs big | Pre-launch |
| V-7 | Will small worlds suffer F-003b badly at launch (news/social scarcity)? | PXE-015 | launch-seeding partially mitigates | Low-Med | closed-beta seeded world test | boredom signals in first cohort | Beta design |
| V-8 | Does "optional" socialization actually *suffice* for genre-strength retention, or is F-001 community-dominance unescapable? | PR-5 | optional succeeds for *most* | Low-Med | beta cohort comparison | solo retention collapses | Beta |
| V-9 | Which *one* extra depth loop (economy / war / politics) should v1 commission best-in-class? | scope decision | economy-first per Prompt 3 priorities | Med | cost/benefit review at next stage | war demand overwhelming | Before roadmap |
| V-10 | How do players rate *different definitions of national success* (J-axis plural outcomes)? | fairness + ranking design | plural wins acceptable | Med | short ranking-preference survey | single-rank expectation tight | Post-v1 |

**Methods the project can realistically afford (all small-N):** concept page with analytics-lite; 5–12 targeted interviews (genre players/Redditless: recruit via genre communities/later Discord); clickable mockups; closed beta with seeded world; ONE A/B at a time. No statistically representative study is needed at this decision stage — qualitative sufficiency is explicitly the current adequacy bar.

**Not yet answerable by any feasible research now (logged honestly):** long-run retention curves of mapless nation games *at 2-hour cadence* (no comparable product exists; our data will be ours); moderation-load reality in a real community's growth spurt (PXE-011) — treated as an *operating risk*, not a researchable-now question.

---

## Section 20 — Deliverable 18: Executive conclusion

1. **Who should Project X serve first?** The steady-check-in multiplayer strategist (§4.1): Mira-primary, Tomas-secondary within the same first experience — not because they're commoner-in-abstract, but because the product's physical properties (free, browser, 2h background cadence, no account costs) naturally deliver what they want, and because the genre's own long-run evidence ([NS-1] 20-year persistence on micro-daily habits; F-001 community primacy) shows this population is both large and *stays*.
2. **Why defensible?** It aligns design-for-retention with anti-churn evidence (F-010/F-011/F-012/F-021/F-023 mitigations are precisely this audience's needs), avoids the documented wrong-for-small-project engines (live windows, map services, whale economics, institution complexity), and fits the free-first hosting budget.
3. **Strongest motivations to serve** (evidence-tiered): compounding visible progress [RS High], consequential choices [RS Med-High], belonging/contribution (for the social) [**Strong**], transparent competition [RS], identity-expression [RS Med]; *not* time-trials, streaks, or pay-levers.
4. **What should the experience promise be?** (§7, PROPOSED): a living world that keeps turning and *explains itself*; short-session agency; optional yet first-class community; honest consequences; safe onramps.
5. **What early?** register → nation making → guided first decision → a turn report that actually explains → a visible week-1 ladder with protection → first optional social surface.
6. **How to respect the 2-hour cycle?** No presence requirements; turn-anchored coordination; queue-first interaction model; absence = digest, not dread (§9; PR-2).
7. **Support both casual and highly engaged?** by *when depth unlocks* (§11 C0→C3) not by *who it exists for*: same world, different reading speeds; group depth gets tools (FO-007/008) while solo play remains legitimate (PR-5/PXO-017).
8. **Highest-priority experience risks** (PXE): empty-world demotivation at small scale (PXE-015), jargon wall (PXE-016), meaning-invisible turns (PXE-003/013), first-week friction stack (PXE-002/007/012), obligation creep (PXE-004), hours-over-judgment drift (PXE-006).
9. **Assumptions needing validation before later design** (§19): V-1..V-6 primarily, then V-7/V-8 at beta.
10. **Which player-experience principles?** PR-1…PR-10 (§17, all proposed) — particularly *world-explains-itself* (PR-1) and *sessions-earn-choices* (PR-2) as the two that most govern future design disputes.

**What this phase establishes:** an evidence-aware audience strategy, five personas with distinct needs, a proposed experience promise/pillars, a first-journey map, a turn-cycle policy direction, a risk register with early-warning observables, ten proposed principles, and a bounded experience-opportunity register (PXO) that leaves *game mechanic determination entirely to later stages*.

**What remains open:** the validation answers (V-1…V-10), absence/protection/catch-up mechanic designs (FO-003/017/018), monetization-direction decisions (none exist), and the war/economy/politics scope choices of later prompts.

---

## Section 21 — Source register

**New research this pass (accessed 2026-10-22). Types: [O] official · [C] community · [3] independent.**

### NationStates
| # | Source | Type | Date | Supports |
|---|---|---|---|---|
| NS-1 | [NationStates Turns Twenty — Max Barry, maxbarry.com](https://maxbarry.com/2022/11/12/news.html) | [O] | 2022-11-12 | Community roles as structural pillars (regional leaders, WA delegates, RP mentors, dispatch authors); "8 million nations"; volunteer moderation; longevity of low-cadence play |
| NS-2 | [NationStates and the Age of Browser-Based Games — SUPERJUMP](https://www.superjumpmagazine.com/nationstates-browser-based-games/) | [3] | 2023-03 (access 2026-10-22) | Casual-to-deep user spectrum (coffee-break issue checks ↔ roleplayers); factbooks/lore expression |
| NS-3 | [Issue — WikiStates (Fandom)](https://nationstates.fandom.com/wiki/Issue) | [C] | n.d. (access 2026-10-22) | Officially-designed micro-cadence: default 1 issue/6h (up to 4/day); throttles 12/24/48h; pre-2016 two-per-day |
| NS-4 | [NationStates: Online Political Roleplaying Game — Armaitus](https://armaitus.wordpress.com/2011/11/02/nationstates-online-political-roleplaying-game/) | [C] | 2011-11-02 (access 2026-10-22) | First-person ≈5 minutes/two decisions per day; RP/maps/lore as personal texture |

### Politics & War
| # | Source | Type | Date | Supports |
|---|---|---|---|---|
| PW-1 | [Daily Login Bonus — P&W-pedia](https://politicsandwar.com/pwpedia/article/daily-login-bonus) | [O] | access 2026-10-22 | Official reward is *daily* login, not per-2h check-ins |
| PW-2 | [Fundamentals of Gameplay — P&W Fandom](https://politicsandwar.fandom.com/wiki/Fundamentals_of_Gameplay) | [C; page self-warns may be outdated] | access 2026-10-22 | 2-hour citizen income automatic; market/wars/alliances framing |
| PW-3 | [Objectives — Politics and War Wiki](https://politicsandwar.fandom.com/wiki/Objectives) | [C] | access 2026-10-22 | Sequential objectives incl. first trade offer, first alliance, second/third city — guided early paths exist |

### eRepublik
| # | Source | Type | Date | Supports |
|---|---|---|---|---|
| ER-1 | [Train — eRepublik Official Wiki](https://wiki.erepublik.com/index.php/Train) | [O] | access 2026-10-22 | Once-daily training cadence (formalized chores) |
| ER-2 | [Missions — eRepublik Official Wiki](https://wiki.erepublik.com/index.php/Missions) | [O] | access 2026-10-22 | "Everyday" work/train/fight mission loops (daily task framing) |
| ER-3 | [Erepublik Guide for Noobs, starting out, tips and tricks](https://www.erepublik.com/en/article/1896953) | [C] | n.d. (access 2026-10-22) | Daily work/train/fight routine advice; "mindless button clicking" phrase |
| ER-4 | [So incredibly bored...](https://www.erepublik.com/en/article/2078117) | [C] | n.d. (access 2026-10-22) | Boredom between exciting wars; event-driven engagement |
| ER-5 | [Erepublik game info for beginners](https://www.erepublik.com/en/article/1576096) | [C] | n.d. (access 2026-10-22) | Social participation central; roles enumerated |
| ER-6 | [EREPUBLIK — 'GAME OPTIONS' UPDATE](https://www.erepublik.com/en/article/2643558) | [C] | n.d. (access 2026-10-22) | Notification/pop-up annoyance; "quick fight in your covfefe break" micro-session anecdote |

### Sim Companies / Prosperous Universe
| # | Source | Type | Date | Supports |
|---|---|---|---|---|
| SC-1 | [Guide for beginners — Sim Companies](https://www.simcompanies.com/pages/guide-for-beginners/) | [O; readable purpose text only — official onboarding *content* app-shelled] | access 2026-10-22 | Official guide exists and is framed optional/beginner-targeted |
| PU-1 | [Prosperous Universe handbook (root)](https://handbook.apex.prosperousuniverse.com/index.html) | [O] | access 2026-10-22 | Tutorial structure: fundamentals-first, advanced-later |
| PU-2 | [1. APEX overview — handbook tutorial](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/apex-overview/index.html) | [O] | access 2026-10-22 | Interface learning demands of a deep-EPC design |
| PU-3 | [New Player Experience — UI, Tutorial and Bulletin Board (forum thread 7566)](https://com.prosperousuniverse.com/t/new-player-experience-ui-tutorial-and-bulletin-board/7566) | [C] | access 2026-10-22 | First-week testimonial enjoying price research (spreadsheet-joy) + learning-curve/UI concerns |

### Prior-report sources
Propagated references (not re-verified here) remain registered in: **Prompt 2 Section 11** (P1–P18 sentiment sources for F-001…F-029) and **Prompt 3 Section 13** (mechanics sources: P20–P31, X1–X13, plus prior-register index for P1–P19, C1–C5, E1–E5, PU1–PU4, S1–S4). This report's claims reuse those findings by ID (F-x, FO-xxx), and the underlying source lists there remain the traceable origin.

---

## Section 22 — Handoff to Prompt 5

**Project constraints (unchanged, confirmed):** browser-only; persistent; 2h/UTC shared turn; fictional mapless world (symbolic relationship network); free-first hosting (Cloudflare Workers/D1 candidates pending write-budget validation — D-005); no live-participation windows; no production code or mechanic decisions made in any research stage.

**Documents Prompt 5 should read:** all of `docs/AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `DECISIONS.md` (six entries D-001…D-006), plus full text of reports 01–04. Don't act from summaries alone.

**Core carries:**
- **Audience strategy (proposed):** primary = steady-check-in multiplayer strategist (persona Mira; Tomas as tool-backed secondary-in-same-week); secondary = organized community + diplomat (personas Tomas/Ade full); future = optimizer/competitor/roleplay (Yuna/Kwame full). NOT for primary design: live-participation, map, whale, election-institution audiences (rejected/deferred — mirrors Prompt 3's FO-025/026/027/023 rejections).
- **Experience promise + pillars (proposed PX-P1…P5)** — treat as a draft identity contract for design stages; each pillar's recognizability signal is a QC hook.
- **Key finding IDs:** strongest carries F-001/F-004/F-006/F-010/F-011/F-012/F-013/F-015/F-017/F-018/F-019/F-021/F-022/F-023/F-003b/F-008/F-026/F-027/F-029-watchlist + Prompt-3's FO-001…FO-017 (candidate). **New IDs to registry:** personas Mira/Tomas/Yuna/Ade/Kwame; pillars PX-P1…P5; risks PXE-001…019 (19 risks, all unique); principles PR-1…PR-10 (all PROPOSED); opportunities PXO-001…022 (P0: 001–005; P1: 006–016, 018, 022; P2: 017, 019, 021; Defer: 020).
- **Two-hour cadence policy direction (§9)**: no presence requirements; turn-anchored coordination; queue-first; absence=digest; generous/deadline-announced windows — these are PROPOSED interface/policy requirements, not approved rules; **must not be implemented as mechanic facts without later approval**.
- **Top risks (PXE-015/016/003/013/002/004/006)** and their validation plan (§19 V-1…V-10) should drive prototype choices.
- **Open questions carried:** all of §19; plus monetization direction (undecided), moderation-capacity plan at launch (PXE-011 operational risk), D1 write-budget analysis; FO-018 catch-up remains Needs-Research.

**What Prompt 5 needs to do next** (per pipeline order as authorized by the user; not executed here): likely security/anti-cheat/fair-play systems research (Prompt-3 handoff note) OR architecture feasibility (per Stage-1 plan); it must reconcile *whichever prompt the user authorizes* with the audience strategy in this report — particularly PR-2/PR-6 constraints on any war/anti-abuse system and PXE-013/FO-002 obligations on reporting.

**Report path:** `docs/stage-1/04_target_audience_and_player_experience.md` (v1.0, 2026-10-22).

---

### Report status footer
- **Completion:** all 18 deliverables present; reuses prior registers; no research invented; all citations carry URL+date where the source displayed one (several community eRep articles show no date — disclosed).
- **New research limitations (this pass):** no accessible Reddit/Discord as before; no genre-wide audience-preference survey exists; NS scale numbers are community-claimed not audited; Sc in-app content remains unreadable (SC-1 purpose-level only); Pu Steam-review mix not fetched (noted PU-3 instead).
- **Decision-entry status:** no new DECISIONS entry added — the audience strategy, pillars, principles and cadence policies are all **proposed**; user approval required to elevate any of them (per the "do not auto-approve your own recommendations" rule).
- **Document version:** 1.0. Prepared 2026-10-22.
