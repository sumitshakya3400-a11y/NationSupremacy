# World events, objectives, rankings and long-term national progression — research, benchmarking and design foundations — Stage 2 Prompt 11A

**Version:** 1.0 · **Created:** 2026-11-05 · **Stage 2, Prompt 11A** · **Research and documentation only**
**Status:** Research and design-foundations complete at the documentation level. **This document approves no Nation Supremacy event, objective, achievement, ranking, reward, milestone, chronicle rule or progression mechanic.** Every recommendation is a **candidate** for **Prompt 11B**. **Prompt 11B and Prompt 11C have not started**, and no gameplay implementation, runtime test or release exists or is authorised here.
**Research execution date:** **2026-11-04/05** (the work began on 2026-11-04 and completed on 2026-11-05). Every source row carries its own access date. No authenticated session, account action, in-game action, transaction, message, form submission or API credential was used. Research was read-only throughout, and where a surface required login that is recorded rather than bypassed.
**Parent task:** Stage 2, **Prompt 11 — World events, objectives, rankings and long-term progression** ([stage-2/01 §Prompt 11](../01_stage_2_prompt_roadmap.md)). This is the **11A** subphase only. It is **not** the B-11 rulebook, which remains **11B's** deliverable at `18_world_events_and_progression.md` ([stage-2/02 §B-11](../02_master_game_design_bible_outline.md)).
**Supporting registers, both part of this deliverable and both linked from here:**
- [`11A_comparator_sources_and_benchmarks.md`](11A_comparator_sources_and_benchmarks.md) — the source register (`11A-RS-001`…`11A-RS-114`) and the benchmark-mechanic catalogue (`11A-BM-001`…`11A-BM-073`).
- [`11A_integration_and_risk_registers.md`](11A_integration_and_risk_registers.md) — the integration matrix (`11A-INT-01`…`11A-INT-40`), the owning-rule violation register (V-01…V-18), the anti-exploit register (`11A-RK-001`…`11A-RK-028`), the candidate requirements (`11A-CR-001`…`11A-CR-030`) and the open research questions (`11A-OPEN-001`…`11A-OPEN-016`).
**Research-scoped identifier spaces:** sources **`11A-RS-###`**; benchmark mechanics **`11A-BM-###`**; design recommendations **`11A-DR-###`**; risks **`11A-RK-###`**; integration findings **`11A-INT-###`**; candidate requirements **`11A-CR-###`**; open questions **`11A-OPEN-###`**. None collides with the project's `D-`, `DD-`, `UD-`, `REQ-`, `TR-`, `NAT-`, `ONB-`, `RRL-`, `ACC-`, `NET-`, `INV-`, `DAT-`, `CON-`, `ECN-`, `URB-`, `DMP-`, `MKT-`, `DIP-`, `ALL-`, `AX-`, `WAR-`, `WRA-`, `WFS-`, `WFR-`, `WCR-`, `PWS-`, `DPS-`, `ALS-` or `F-` spaces. They are **research identifiers, not decisions or registered requirements**.
**`11A-DEC-###` deliberately not created.** The Prompt 11A brief lists it as a possible space. It is not used, because [`../../AUTONOMOUS_DECISION_POLICY.md`](../../AUTONOMOUS_DECISION_POLICY.md) §5 forbids "creating a second register for a decision that already has an ID", and `D-`/`DD-` already exist. Category B decisions are recorded as `D-144`…`D-151` / `DD-192`…`DD-199` (§22); Category C matters as Provisional rows (§23).

---

## 1. Executive summary

1. **Politics & War is the right primary benchmark, and the reason is arithmetic.** Its own official guide states that one credit buys "60 Days (**720 Turns**)" and that an advertisement "will run for 20 days (**240 turns**)" — both resolve to **12 turns per day, a two-hour turn**, which is Nation Supremacy's fixed cadence (`11A-BM-001`, `11A-RS-019`, `11A-RS-020`). Its live changelog expresses event windows against a named world boundary ("until after **day change** on Nov 8"), exactly the two-clock structure B-02 already specifies. No other benchmark in this study matches our cadence.
2. **The single most important finding is a warning about one number.** Politics & War's Nation Score simultaneously determines competitive ranking, who may attack whom, and which nations are eligible for a rotating world event — and its own July 2025 balance patch, which added military research to score, therefore changed *attack eligibility* and *event targeting* as a side effect of a military tuning change (`11A-BM-001`, `11A-RS-002`, `11A-RS-012`). Nation Supremacy already forbids the equivalent merge in several places (`DMP-051`, `ECN-108`, `ECN-118`), so the recommended direction is structural separation, not a better composite (§21, `11A-DR-010`).
3. **A permanent recognition layer can exist without becoming a power layer, and the evidence is live.** A current Politics & War nation profile still displays badges for "Finished #2 Rank in Beta", "Speed Round – Highest GDP", "This nation existed when P&W turned 1" and "CN Milestone – this nation was around when P&W surpassed CN in nation count" — twelve years after the fact, with no documented mechanical effect (`11A-BM-009`, `11A-RS-027`). Nation Supremacy's own `NAT-052` already says milestones "are records, not power"; this confirms the shape works in production.
4. **The best recurring-event machinery found anywhere is deterministic and self-scaling.** Politics & War's Treasures rotate on a published 60-day per-object timer, spawn only inside **15–65 % of the current leader's score**, are excluded from newcomer and inactive states, and pay a **square-root-scaled** alliance bonus (`11A-BM-014`). Supremacy 1914 normalises its whole score pool to `2000 × player count` so thresholds never need retuning (`11A-BM-023`). Travian's daily quests rotate rewards in a **fixed published order** identical for every player on a world (`11A-BM-060`). Those three devices — relative band, pool normalisation and deterministic rotation — are the reusable core, and none requires a content author.
5. **Nation Supremacy's existing rules are already stricter than every comparator on the two points that matter most, and Prompt 11 must inherit that rather than dilute it.** `TR-085` forbids login streaks, presence bonuses and act-within-X-minutes rewards outright, which excludes the daily-login and rewarded-ad loops found in Politics & War, Travian and eRepublik (`11A-BM-005`, `11A-BM-060`, `11A-BM-062`). `D-028` grants a dormant nation no loss of any kind, which excludes Travian's "collect your rewards before reset — otherwise, they are lost" (`11A-BM-060`) and Politics & War's stepped inactivity deletion (`11A-BM-022`). Both are approved; both are protective; neither may be reopened by an objective or event.
6. **The most valuable non-military progression evidence is not a score at all.** Tribal Wars computes standing as "points for the **completion of buildings**", recalculated lazily at boundaries (`11A-BM-042`); Call of War and Supremacy 1914 both include a **hold-an-objective** victory in which the win is *sustained control* rather than accumulated total (`11A-BM-039`, `11A-BM-024`); Supremacy 1914's account rank "unlocks **more types of maps to choose from**" and never grants in-round power (`11A-BM-028`); NationStates measures nations against a **world median** in descriptive categories that carry no reward (`11A-BM-054`). Together these point at a progression model built from **completed development, held contested positions, unlocked choices and descriptive identity** — none of which is a new numeric resource, which matters because `ECN-092` forbids a prestige currency at launch.
7. **Ranking integrity is the dominant risk, and comparators show the cost of getting it wrong in three specific ways.** A hidden tie-break favouring the operator is documented in Politics & War ("in any instance where there is a tie, the award is configured to go to [the developer's] nation", `11A-BM-008`); snapshot-edge manipulation is created by rewarding instantaneous position with a published reassignment time; and small-group disclosure through standings is exactly what `D-027` was written to prevent. Supremacy 1914's **pre-draw participation freeze** ("tickets are also not available for purchase on the turn leading to the drawing") is the single most transferable integrity device in the study (`11A-BM-032`), and it is already structurally available to us through `TR-032` and `TR-037`.
8. **Political participation can be a genuine second path, but every comparator that tried it attached power, and we cannot.** NationStates' influence is a **spendable** budget that gates a delegate's power and drains as it is used, created explicitly to stop a newcomer from seizing a region and ejecting everyone (`11A-BM-055`); eRepublik's legislature holds direct hands on **tax and minimum wage** but not on war (`11A-BM-050`); Supremacy 1914 grants diplomatic tiers real trade and information rights (`11A-BM-035`). Nation Supremacy's `DIP-084` forbids a diplomatic reputation value and `DMP-051` forbids approval as a ranking criterion, so the lawful direction is recognition by **durable record and published count**, with authority capped rather than accumulated (`11A-DR-023`, `11A-DR-028`).
9. **A peaceful path must be viable by construction, not by balance.** NationStates demonstrates that identity formation (issues that reshape civil rights, economy and political freedom, with a **player-adjustable** cadence from six to forty-eight hours) sustains a persistent nation without conflict at all (`11A-BM-058`). Travian demonstrates the inverse hazard: an official guide telling players to "maintain your village population within the top 200–300 players" as anti-farming advice converts development level into personal safety (`11A-BM-065`), which our `ONB-023`/`D-028` design must never do.
10. **Recommended architecture — four layers, one shared evaluation point.** (i) **Events:** systemic, parameterised, generated only in B-02's existing phase **P6** as **four event classes** — calendar, state, challenge and commemorative — over one shared parameterised machinery using the five observed trigger types, with relative-band eligibility, a published timer and a two-stage teardown (`11A-DR-001`…`11A-DR-006`). (ii) **Objectives:** optional by default, tiered with partial credit, dismissal-not-forfeiture, and never attendance-linked (`11A-DR-009`, `11A-DR-029`). (iii) **Rankings:** plural domain standings plus **one separate eligibility measure**, windowed rates alongside cumulative totals, snapshot once per turn, k ≥ 5 for every aggregate, published tie-break (`11A-DR-010`, `11A-DR-019`). (iv) **Progression:** **derived** from owning-subsystem state and the chronicle, with no new numeric resource, honour-only permanence, and a strict permanent-versus-seasonal split (`11A-DR-013`, `11A-DR-017`, `11A-DR-024`). This closes the one ordering question B-02 left explicitly assigned to Prompt 11 (`TR-042`) and supplies the fixed evaluation order B-02 band **B4** requires (`TR-044`).
11. **Scope honesty.** Six of the ten most-cited starting surfaces named in the Prompt 11A brief are community wiki pages whose last revisions are **six to eight years old**, and two whole games (NationStates, Supremacy 1914) had their official primary surfaces return **403** or a login shell for unauthenticated requests. Where a live official surface was reachable it is the citation of record; where it was not, the claim is marked HISTORICAL or UNVERIFIED and is **not** used as load-bearing evidence. §5.3 lists every inaccessible source. The recommendation set is deliberately built so that no proposal depends on an unverified comparator claim.
12. **What 11A does not do.** It sets no number, allocates no global `REQ-` row, resolves no owner-reserved decision, modifies no B-02…B-10 rule, and implements nothing. Prompt 11B converts the accepted foundations into formal specifications; Prompt 11C supplies workflows, integration contracts and acceptance.

---

## 2. Research purpose and scope

### 2.1 Purpose

Prompt 11 must eventually specify four interconnected systems that give players meaningful long-term goals beyond ordinary economy, diplomacy, domestic politics and warfare. **11A's job is to establish the evidence and the design foundations for that work — not to write the rules.**

Concretely, 11A was asked to: research these systems in existing games at the level of actual mechanics, incentives, scoring models, eligibility rules, reward structures, timing, exploit surfaces and long-term consequences; separate successful from unsuccessful approaches; evaluate suitability for Nation Supremacy specifically; and independently recommend a design direction under `D-014`.

### 2.2 In scope

| Area | Covered |
|---|---|
| Domain A | World events: categories, lifecycle, governance, timing, taxonomy |
| Domain B | Objectives and challenges: categories, lifecycle, design principles, harmful patterns, rewards |
| Domain C | Rankings and competitive recognition: categories, methodology, fairness, eligibility, snapshots, tie-breaks, history, privacy |
| Domain D | Long-term national progression: dimensions, six candidate models, progression inflation, permanent versus seasonal |
| Benchmarks | Politics & War (primary), NationStates, Supremacy 1914, Travian: Legends, eRepublik, plus two independently selected additional games (Call of War, Tribal Wars) |
| Integration | B-02…B-10 dependencies, plus Prompt 12/13/14/15 boundaries, at ID level |
| Cross-cutting | Player-type diversity (12 profiles), anti-exploit and fair play, comparative matrix, design alternatives, recommendations, decisions, handoffs |

### 2.3 Explicitly out of scope

| Excluded | Why | Owner |
|---|---|---|
| Any gameplay rule, formula, cost, threshold, weight or payout | 11A is research; Prompt 11A §20 forbids deciding formulas, and `D-014` Category C defers balance | Prompt 11B (rules), Prompt 14 (numbers) |
| Global `REQ-` allocation and new `UD-` rows | Project convention: research sub-prompts register **candidates**; specification sub-prompts allocate. Precedent: 08A, 09A and 10A added no `REQ-` row | Prompt 11B |
| Final event effects, reward amounts, ranking weights, snapshot intervals | Balance-sensitive and simulation-sensitive | Prompt 14 |
| Screens, layouts, components | "Prompt 13 owns the final UI specification" | Prompt 13 |
| Moderation rules, punishments or detection capability | "Do not invent moderation punishments" | Prompt 12 |
| Any B-02…B-10 rule change | Fixed by the acceptance records; §17 documents what may and may not be touched | Owning subsystem |
| Implementation, schema, migrations, deployment | Stage 2 writes no code (`D-012`) | Stage 5+ |

### 2.4 Relationship to the existing research corpus

Five Politics & War research reports already exist in this repository, covering economy ([`04`](04_politics_and_war_economy_research.md)), cities and production ([`05`](05_politics_and_war_city_infrastructure_production_research.md)), domestic politics and elections ([`06`](06_politics_and_war_domestic_politics_elections_and_policy_research.md)), markets ([`07A`](07A_politics_and_war_market_research.md)), diplomacy ([`08A`](08A_diplomacy_research.md)), alliances ([`09A`](09A_alliance_research.md) with its three companion registers) and warfare ([`10A`](10A_politics_and_war_warfare_research.md)). **This report does not re-derive them.** Where a mechanic from those domains feeds an event, objective, ranking or progression design, the row cites the existing report and the accepted rule ID instead of restating the evidence.

Two deliberate extensions were made because the existing corpus did not cover them. First, **national measurement and recognition** — Nation Score, leaderboards, awards, achievements, bounties, treasures and commemorative badges — which no earlier report examined, because no earlier prompt needed them. Second, **the live official surfaces** (`/rules/`, `/leaderboards/`, `/changelog/`, `/world/bounties/`, `/world-graphs/`, `/nation/id=…`, `/achievement/166`, `pwpedia/article/…`), which earlier reports cite sparsely: the earlier corpus relied mainly on the PWPedia and the community wiki, and this study found that several of those wiki pages are years out of date. Where live and wiki evidence disagree, this report uses the live official page and says so (§5.2).

---

## 3. Project baseline and existing constraints

### 3.1 Repository state at commencement

Inspected on 2026-11-04 before any research:

| Item | Verified value |
|---|---|
| Working directory | `C:\Users\suren\Downloads\Project X` — the Nation Supremacy repository root; `git rev-parse --show-toplevel` agrees |
| Branch | `prototype/free-tier-feasibility` |
| HEAD | `8f4e20ef6c0c8edbfe18adf280e569c0b80e0926` — "docs: close Stage 1 and authorize Stage 2" |
| Working tree | **65** modified-or-untracked entries, including the whole Stage 2 document set and the QA validators. All preserved; nothing reset, reverted, stashed, committed or pushed |
| Stage 1 | **CLOSED** (`D-011`) |
| Stage 2 | **IN PROGRESS**; Prompts 01–10 complete at the specification/documentation level, including 09A–09C, 10A, 10B and 10C |
| Prompt 10C | **Verified complete** at the specification/documentation level, canonical companion [`17_warfare_workflows_acceptance.md`](../17_warfare_workflows_acceptance.md), log §63–§66; **B-10 is v1.3**, 188 numbered `WAR-` rules plus 42 lettered sub-rules, 39 formulas, 25 architecture decisions; **preserved unchanged by 11A** |
| Next prompt | `stage_2_next_prompt: 11` in the STATUS block of `AI_CONTEXT.md`, `AI_HANDOFF.md` and `PROJECT_PROGRESS.md` |
| Bible outline | B-11 **Planned**; authoritative document `18_world_events_and_progression.md`; prerequisites listed as **B-02, B-04, B-10**; validation "Returning players can see what changed and why; **no single dominant ladder**" |
| Register maxima | **`REQ-703`, `D-143`, `DD-191`, `UD-049`** — confirmed by inspection, and unchanged by this report's candidate registers |
| Prompt 11 carry-in | [stage-2/01 §Prompt 11](../01_stage_2_prompt_roadmap.md): B-03 §18 contract; outputs = strategic objectives, world-event framework and timing relative to the boundary, achievements, "ranking criteria (**plural standings, no single dominant ladder**)", world chronicle, long-term progression, endgame/seasonal concepts if any; **guardrail: "No manual content team exists (AP-003): events are systemic, not authored live-ops"**; done-when = "A player returning after a month can see what changed in the world and why" |

**Continuity discipline.** The STATUS blocks and validators were read as the authority for current state, and dated prose in `AI_CONTEXT.md`, the handoffs and the outline was treated as history. One structural gap was found and is recorded in §31: the sub-prompt detector in `docs/qa_backups/status_rules.py` recognises `0[789]|10` only, so **11A/11B/11C status claims are not machine-checked** by the existing rule.

### 3.2 Fixed constraints (Category A) that bind Prompt 11

| ID | Constraint | Effect on this prompt |
|---|---|---|
| `D-007` | The game is **Nation Supremacy**; `Project X` is an internal codename | No comparator branding, names or conditions may be reproduced |
| `D-008` | Cloudflare Pages + Supabase; one authoritative `pg_cron` scheduler | Event and snapshot machinery must fit one scheduler; no second cron |
| — | **₹0/month** target for required services; free-first | Reward content must not require an author, a CDN, a render farm or a paid API. This is why `TR-092` retention shapes the archive recommendation (§14.6) |
| `D-012` | Stage 2 is a design-specification stage; no code, migration or hosting change | 11A writes documents only |
| — | **2-hour global turn, 12/day, fixed UTC boundaries**; players act between turns | All timing in this report is expressed in turns and boundaries; §12.4 evaluates cadence against this |
| — | **Fictional, mapless world; no geographic map, provinces or borders** | Excludes province capture, geographic control points, map movement, territorial objectives and distance-based scoring from every recommendation; §11 and §8 record the exclusions explicitly |
| `D-014` | Autonomous decision policy, Categories A/B/C/D | Governs §21, §22, §23, §24 and §31 |
| `D-015` (amended 2026-11-04) | Operations Points are one persistent **military-only** national pool, +1 at the P3.7 opening, cap 10 provisional | OP may never be an objective or event reward (`11A-INT-33`) |
| `D-021` | **No catch-up acceleration at launch** | Rejects the Politics & War new-player income slope and any age-graded assistance (§13.4, §15.3) |
| `D-027` | Aggregate disclosure threshold **k = 5**, complementary suppression, no cross-turn or cross-table differencing | Bounds every ranking and statistic design; §14.7 |
| `D-028` | Dormancy at 14 days/168 turns; **no resource, progression or ownership loss**; excluded from public rankings and published aggregates as a **presentation rule** | Settles "how should inactive nations be treated" without decay (§14.3) |
| `D-032`/`D-034`/`D-039` | One account, one active nation; pair restrictions; instant reroll | Bounds multi-account and reroll surfaces in §18 |
| `D-122`, `DD-136`, `REQ-513` | Global Trade is approved mandatory scope but **release-gated** | No trade statistic may be published; §16.6 |
| `D-040`/`D-041`/`D-042` | Onboarding and once-only protection; account lifecycle; data classes and retention | Tutorial progress is account-scoped and survives reroll; public nation history and the audit spine are permanent |

### 3.3 Accepted subsystem rules that Prompt 11 must obey (not restate)

The full ID-level inventory is in [`11A_integration_and_risk_registers.md`](11A_integration_and_risk_registers.md) §2–§4. The nine constraints that most strongly determine the recommendations are:

1. **B-02 owns the turn.** `TR-040` fixes P0…P7 and assigns **P6 "World — Evaluate objectives, rankings, systemic events" to Prompt 11**, with P3's recurring event ticks and P7's record writing shared with it. `TR-042` leaves one ordering question **explicitly assigned to Prompt 11** ("Are world events generated before or after objective evaluation?"). `TR-044` band **B4** requires a "Fixed evaluation order declared by Prompt 11". `TR-055` already resolves concurrent reward claims: "Rewards for the same achievement — **First in B4 order is granted; later claims are deduplicated by achievement key**. Owner: Prompt 11". `TR-013` lists **Objective**, **World event** and **Ranking/record** as vocabulary owned by Prompt 11, and `TR-096` names the decisions Prompt 11 must make. **No competing scheduler may be created.**
2. **B-02 already forbids the engagement patterns most comparators use.** `TR-006`/`TR-007`/`TR-085`: waiting is a valid strategy; no decay, no streak, no bonus for acting every turn, no presence requirement, no rule requiring action during resolution.
3. **B-03 owns the account boundary and the nation's first appearance.** `NAT-016` unranked until the first completed boundary; `NAT-043`/`NAT-045` identical starting state and **no differential by account age, reroll, referral or purchase**; `NAT-046` no transferable first-time rewards; `NAT-051` "progression is **chosen**, not handed out"; `NAT-052` milestones are records with **no ranking weight**, and "Prompt 11 owns the achievement framework"; `ONB-025` a protected nation may appear in rankings and take part in **non-offensive** world events; `RRL-013`/`RRL-016`/`RRL-019` the reroll's exact effect on ranks, achievements, objectives and the chronicle.
4. **B-04 owns value.** `ECN-113` a reward must be approved by Prompt 11's rules, **non-repeatable with an achievement key**, disclosed, ledgered, non-convertible and **never a permanent yield multiplier**; `ECN-013(c)` new crowns only as "a **rare**, disclosed, system-generated event adjustment approved by Prompt 11"; `ECN-165` the `REWARD` ledger type already exists; `ECN-111` the world money-conservation identity already carries a `one_time_rewards` term; `ECN-108`/`ECN-109` national wealth is **not** a score or ranking, though Prompt 11 may use it as a labelled estimate; **`ECN-092` no prestige currency at launch**.
5. **B-05 owns development, and already protects it from events.** `URB-040` "no construction, demolition, **event** or `OP-05` strike may take a city below" the infrastructure floor; `URB-035` cities are permanent; `URB-158` a reward may grant crowns, resources, research points or a one-time programme only through a disclosed keyed ledgered event, and capacity, housing and research points "may be shown as statistics but **never as a score that can be bought**"; `URB-110` Prompt 11 may add a programme-granting reward only through a decision and a register row.
6. **B-06 owns politics and bars the obvious ranking inputs.** `DMP-051` "Approval is not a success ladder… not a score, an achievement currency or a ranking criterion"; `DMP-042` no welfare index; `DMP-063` constituency weights "do not vary with population, **events** or approval"; `DMP-141` an event may move a named support term or grant a one-time approval change **through the normal target-and-cap path** but "may **not set `approval` directly**", and no reward may grant population, a policy, a government or legitimacy; `DMP-266` an event "may **not set `leadership_state`**, resolve a contest, remove a leader or grant a campaign bonus", and "event effects are applied once, with a key, and are visible in the digest".
7. **B-07 blocks market statistics.** `MKT-072`…`MKT-076` keep Global Trade unreleased behind **G-1…G-6**, with G-1, G-2, G-3, G-5 and G-6 **not met** and G-4 partial; "the market is dark until the gate passes"; no readiness claim may be made.
8. **B-08 bars a reputation value.** `DIP-084` "There is **no diplomatic reputation score**… no other system may read a diplomatic reputation from B-08 because none exists"; `DIP-086` the breach count is nation-scoped and dies with the nation; `DIP-088` the count has **no mechanical effect** — "A player may use it; the game does not"; `DIP-089` no hidden account record; `REQ-523` "silence, expiry, dormancy, a leadership change and an administrative state are **never consent**".
9. **B-09 and B-10 set the military and Alliance limits.** B-09: `ALL-224` Alliance operational funding "may not fund a grant, loan, aid payment, reparation, refund, dividend, salary, **prize**, compensation or private debt"; `ALL-156` member and applicant data use the existing visibility classes; `ALL-134` nothing binds a member nation's military; `AX-18`/`UD-047`/`UD-049` no Alliance military command, no shared OP pool, no military treasury. B-10: `WAR-147` "The campaign record is permanent. **Rankings and world events receive the outcome under B-11's rules**; no aggregate is published below k = 5" — the one place a subsystem places a **positive obligation** on Prompt 11; `WAR-162` "no exact readiness, force or inventory is ever public"; `WAR-006` and `WRA-06` already use the word "objective" for a campaign objective, creating a vocabulary collision that Prompt 11 must resolve.

### 3.4 Design laws inherited from Stage 1

These are **provisional** Stage 1 outputs, not approved decisions, but the Stage 2 roadmap already invokes `AP-003` as a Prompt 11 guardrail, so the whole set is treated as binding on this analysis. Each carries its own self-test question ([`stage-1/05`](../../stage-1/05_core_game_concept_and_design_pillars.md) §AP table):

| ID | Statement | Test question | Consequence for Prompt 11 |
|---|---|---|---|
| **AP-001** | No login-at-every-boundary or attendance/streak mechanics | "Does skipping this punish the player?" | Kills the daily-login reward class in every comparator |
| **AP-002** | No geographic map or territory capture as the core metric | "Can the feature be restated in relationship/institution terms?" | Excludes province, control-point and distance scoring |
| **AP-003** | No dependence on hand-authored daily content or a live-ops staff | "Would this feature fail if the team were one person?" | **The decisive event constraint** — §12.5 |
| **AP-004** | Alliance membership is never a functional requirement | "Can a new player reach a meaningful goal alone?" | Every collective objective needs an individual equivalent |
| **AP-005** | No single power path may dominate the success metric | "Which path gives the fastest returns? If it's one, revise." | The ranking architecture must be plural by construction |
| **AP-006** | No unexplained rules or jargon requiring out-of-game wikis | "Can a new player trace this mechanic's consequence?" | Standings and objectives must be self-explanatory, not merely visible |
| **AP-007** | No continuous real-time windows or synchronous events as a foundation | "Does this break the shared-clock cadence?" | Excludes live-drawn, time-boxed synchronous events as a base layer |
| **AP-008** | No copying a competitor's distinctive combination of mechanics and presentation | — | Names, badges, conditions and reward tables from comparators are excluded by design, not by taste |

Two Stage 1 registers also bind directly: **FO-024 (age/round resets) is already *Rejected*** — "N/A — conflicts with persistence" ([`stage-1/03`](../../stage-1/03_feature_comparison_opportunity_analysis.md) §10) — which means a full-season wipe of national state is not an available option; and **FO-020 (seasonality/events calendar) is a Tier C "Deferred"** area, so seasonality is permitted as design but not yet as commitment. The Stage 1 system catalogue names **SYS-014 "Rankings, Objectives & Achievements"** with the purpose "comparative visibility… **NO single global 'best nation' ladder** as a design driver (AP-005)", and **SYS-015 "World Chronicle & News"** as "the world's shared memory… **systemic generation only** (AP-003: no editorial calendars)" ([`stage-1/06`](../../stage-1/06_core_gameplay_systems_and_interactions.md) §13).

---

## 4. Research methodology

### 4.1 Source hierarchy applied

The Prompt 11A brief's order was applied as written: official game websites → official help centres and rulebooks → official game wikis and developer documentation → official announcements and changelogs → established community-maintained wikis → detailed player guides → public community discussions → independent design analysis.

In practice the achievable depth varied sharply by publisher, and the differences matter:

| Game | Best source actually reached | Consequence |
|---|---|---|
| **Politics & War** | **Live official pages** (`/rules/`, `/leaderboards/`, `/changelog/`, `/world/bounties/`, `/world-graphs/`, `/nation/id=…`, `/achievement/166`, `/tools/`) **plus the official in-game guide PWPedia** (149 articles enumerated) | Highest-confidence benchmark in the study; current mechanics verified against running pages, not descriptions of them |
| **Travian: Legends** | **Official help centre** `support.travian.com/en/articles/…` (12 articles retrieved; the 231-article sitemap was used only to discover slugs) | Strong official evidence for daily quests, medals, season pass, protection, tournament and the Wonder |
| **Supremacy 1914** | Official help centre **and** official publisher news for the 2026 seasons; the staff-authored Game Manual is legacy/read-only | Current for the seasonal system and rules; **HISTORICAL for all numeric detail** |
| **Call of War** | Bytro's own official wiki and help centre; `callofwar.fandom.com` returned **403** | Official but thin; several expected systems unconfirmed |
| **Tribal Wars** | Official InnoGames knowledge base; no dedicated rankings article exists in it | Official on points and world types; **negative findings** important (§11.2) |
| **eRepublik** | Official wiki (partially dated) and official update articles; the changelog appears frozen at ~2023-12-31 | **Weakest currency assurance**; most current-state claims marked HISTORICAL or UNVERIFIED |
| **NationStates** | The live site and its forum return **403** to unauthenticated requests; **the same official pages were recovered from dated Internet Archive captures**, including a 2026-10-24 capture of the official FAQ | **OFFICIAL (ARCHIVED)** evidence available and used; the first, community-only pass is retained as a second source and explicitly superseded (companion register §5.5b) |

### 4.2 Verification procedure per mechanic

For every important mechanic the following were recorded: source page title; full URL; access date; publication or last-modified date where obtainable; whether it describes **current** mechanics; official versus community status; evidence confidence; second-source confirmation; and relevance to the four domains. Nothing was accepted on the strength of a search-result snippet alone: where a search surfaced a claim, the page was opened and read, and if it could not be opened the claim was recorded as **inaccessible** rather than cited.

Revision ages were obtained **programmatically from each wiki's own MediaWiki API** rather than estimated, because the estimate proved wrong. For example, an initial query using `rvdir=newer&rvlimit=1` returned each page's **creation** comment, which would have mis-dated the Politics & War achievements page to 2019 when its actual last revision is **2023-08-28** across 130 revisions; the method was corrected and every date in the source register was re-derived before use.

### 4.3 Fact/recommendation separation

Every benchmark entry in the companion register is labelled **OBSERVED** (a cited source states it — a claim about *that game*), **INTERPRETATION** (the author's reading), or **LESSON / DIRECTION** (a candidate for Nation Supremacy, never an existing rule). Recommendations appear only as `11A-DR-###` in §21 and §22, each with its evidence, confidence and provisional details. No comparator rule is presented as a Nation Supremacy rule anywhere in this document.

### 4.4 Read-only discipline and its limits

No login, registration, form submission, purchase, trade, message, declaration or API key was used. Public pages were read with an ordinary browser user-agent. Two limits follow and are disclosed rather than hidden: first, **login-gated surfaces could not be examined at all**, which is why the Politics & War objectives screen, the Supremacy 1914 alliance ranking page, eRepublik's `ERU`/`Nation` articles and all of NationStates are gaps (§5.3); second, several publishers serve JavaScript-rendered shells to non-browsers, so official content was sometimes reachable at a different path (`support.travian.com/en/articles/…` rather than `/hc/en-us`, `pwpedia/article/…` body text rather than the SPA) — each substitution is recorded in the register.

### 4.5 Counter-evidence and negative findings

Absence was treated as a finding, not as silence. Three of the most useful results in this study are negative: **Tribal Wars has no culture-point victory** — the mechanic expected of it belongs to **Travian**, whose World Wonder is the real non-military win path (`11A-BM-043`); **the official Politics & War game guide, with 149 articles, contains no Awards, Achievements, Objectives or Events article** even though achievements demonstrably exist (`11A-RS-029`, `11A-RS-025`); and **no comparator in this study documents an alliance scoring formula at all** despite several asserting alliance rankings (`11A-BM-034`, `11A-BM-041`). Each negative is recorded with the queries that produced it. Where evidence was missing, this report says "not found" and does **not** treat the absence as proof of non-existence — a rule the Prompt 11A brief §19 requires and the comparative matrix in §19 applies.

---

## 5. Sources and evidence register

### 5.1 Where the evidence lives

The complete register is [`11A_comparator_sources_and_benchmarks.md`](11A_comparator_sources_and_benchmarks.md): **114 source rows** and **73 benchmark-mechanic entries**, each in the fifteen-field format required by the Prompt 11A brief §5.3. This section states the totals, the integrity findings and the gaps; §6–§11 give per-game analysis; §19 gives the comparative matrix.

### 5.2 Totals and composition

| Measure | Count | Notes |
|---|---|---|
| Games researched | **7** | Politics & War (primary), NationStates, Supremacy 1914, Travian: Legends, eRepublik, Call of War, Tribal Wars |
| Source rows | **114** (`11A-RS-001`…`11A-RS-114`) | Per-game: P&W 43; Supremacy 1914 17; Call of War 5; Tribal Wars 6; eRepublik 10; NationStates **22** (9 first-pass `11A-RS-082`…`090` + 13 second-pass `11A-RS-102`…`114`); Travian 11 (including one recording blocked official paths) |
| **Official** source rows | **82** | Publisher-authored: **73** retrieved live (game pages, official rules, official in-game guide and help centre, official developer changelogs and announcements, official mirrored store feeds, official terms of service, official forum posts) plus **9** recovered from dated Internet Archive captures (`11A-RS-102`…`108`, `11A-RS-110`, `11A-RS-111`), labelled **OFFICIAL (ARCHIVED)** and never presented as live |
| **Community** source rows | **25** | Community-maintained wikis and forum threads; **never presented as confirmed developer rules** |
| Player-authored-on-official-platform rows | **3** | `11A-RS-080`, `11A-RS-081` and `11A-RS-113` — in-game player articles, country-authored wiki pages and a player guide dispatch; counted here rather than in the community row, classified apart from both official documentation and community wikis |
| **Third-party** source rows | **1** | Wikipedia, used only for NationStates scale and its 2026 incident record, and for the absence of NationStates war/trade mechanics |
| Recorded-unavailable marker rows | **3** | `11A-RS-090`, `11A-RS-101` and `11A-RS-114` enumerate blocked or unreachable official surfaces rather than supporting a claim |
| Official sources that are **legacy or unmaintained** | 4 | Supremacy 1914's read-only staff Game Manual (the source of all its numeric values), the mirrored 2006 NationStates influence thread, the Tribal Wars 2 corroboration, and the 2019-05-09 census capture — each marked HISTORICAL where used |
| Benchmark-mechanic entries | **73** (`11A-BM-001`…`11A-BM-073`) | Politics & War **22** entries and **43** sources — by far the deepest coverage, as required. NationStates has 13 entries across two passes (`11A-BM-054`…`11A-BM-059`, `11A-BM-067`…`11A-BM-073`) |
| Entries marked **CURRENT** | 52 | Verified against a live or dated-2025/2026 source |
| Entries marked **HISTORICAL** | 15 | Documented but current status not confirmed |
| Entries marked **UNVERIFIED** | 6 | Single thin source, a stub, or an analyst inference from cited rules |
| Entries that are **negative findings** | 4 | `11A-BM-043` (Tribal Wars has no culture victory), `11A-BM-073` (NationStates has no achievement system and no composite national rating), plus two absence records in §5.3(a)/(b) |
| Claims with second-source confirmation | 33 of 73 | Stated per entry |
| Documented **inaccessible** source entries | **21 entries** (§5.4), each naming one or more URLs; **7** further per-game inaccessible lists in the companion register | §5.4 |
| Explicitly recorded unverifiable claims | **95** | The "could not verify" lists in the companion register, §5.1.1 through §5.6 |
| Design recommendations | **34** (`11A-DR-001`…`11A-DR-034`) | §21 |
| Integration findings | **40** (`11A-INT-01`…`11A-INT-40`) | Companion register §2–§3 |
| Owning-rule violations catalogued | **18** (V-01…V-18) | Companion register §4 |
| Risk and exploit entries | **28** (`11A-RK-001`…`11A-RK-028`) | §18 |
| Candidate requirements | **30** (`11A-CR-001`…`11A-CR-030`) | §25 |
| Open research questions | **16** (`11A-OPEN-001`…`11A-OPEN-016`) | §28 |

### 5.3 Source-integrity findings

Four findings materially changed how the evidence could be used.

**(a) The five Politics & War wiki pages named in the brief as "starting points" are between three and eight years stale.** Verified last revisions: `Leaderboards` **2018-08-08** (5 revisions; its own edit comments read "This is my current project, it is a major work in progress"), `Awards` **2023-08-01** (84 revisions), `Objectives` **2019-01-29** (**one revision only — never edited since creation**), `Nation Score` **2021-03-26** (9 revisions), `Achievements` **2023-08-28** (130 revisions). The Nation Score page is **superseded on the point that matters** by the official in-game guide, which added military research to score in July 2025 (`11A-RS-012`). Consequence: for each of these five topics the **live official page became the citation of record**, and the wiki row is retained only as a second source or as a historical record. This is also direct empirical evidence for one of the brief's own research questions — §6.2's "can objectives become outdated when game mechanics change?" is answered by a page that has literally not been updated since the mechanics changed around it.

**(b) The official Politics & War guide's own article inventory is itself evidence.** The 149-article PWPedia index (`11A-RS-029`) contains **no** article titled Awards, Achievements, Objectives, Events or Leaderboards — yet achievements demonstrably exist and are live, since an official achievement page publishes completion statistics (`11A-RS-025`) and an official changelog post specifies four event achievements with payouts (`11A-RS-007`). The inference, held as INTERPRETATION rather than fact, is that the guide documents **systems** and leaves **recognition** undocumented. Nation Supremacy should not repeat that: recognition objects need their own authoritative document, which is precisely what B-11 will be.

**(c) Official surfaces were blocked for two games, with different outcomes.** The live NationStates domain and its forum returned **HTTP 403** on every unauthenticated attempt (`11A-RS-090`); a second pass then recovered the **same official pages from dated Internet Archive captures**, including a **2026-10-24 capture of the official FAQ**, so NationStates evidence is official-but-archived and is labelled **OFFICIAL (ARCHIVED)** throughout (`11A-RS-102`…`11A-RS-108`). The first, community-only pass is retained as a second source and is explicitly superseded. For Supremacy 1914, `supremacy1914.com` serves only a login shell and `supremacy1914.fandom.com` returned **403** on every attempt, so the Index-of-Power formula there is **community-derived and never officially confirmed** (`11A-BM-023`). Where a claim rested only on such a source, the recommendation does not depend on the number — it depends on the structure.

**(d) One game's documentation is frozen, and one is self-contradictory.** eRepublik's official wiki changelog stops at **day 5,874 (~2023-12-31)** while individual articles carry 2025 dates (`11A-RS-078`), and its day-numbering cannot be reconciled (day 2,586 / day 3,910 / day 5,874 cannot share one clock), so every eRepublik day-number is treated as relative and undated. Supremacy 1914's sources disagree with each other on whether 1,000 / 1,500 points are creator-selected **modes** (legacy manual) or solo **versus** coalition bars (current official help plus community) — recorded as a conflict in `11A-BM-025`, not silently resolved.

### 5.4 Complete list of inaccessible or failed sources

Recorded because the brief requires it and because a gap stated is safer than a gap filled by assumption.

| URL or surface | Result | Effect |
|---|---|---|
| `politicsandwar.com/api/` | **403** | API field inventory unavailable; award/achievement fields could not be confirmed programmatically |
| `politicsandwar.com/achievements/` | **403** | Achievement list is not obtainable from an official surface; wiki page used and marked stale |
| `politicsandwar.com/awards/`, `/objectives/`, `/treasures/`, `/events/`, `/history/`, `/news/` | **404** | No dedicated official pages exist at those paths |
| `politicsandwar.com/bulletins/` | 200, **empty body** | Announcement surface could not be read |
| `politicsandwar.com/tutorial/`, `/nation/tutorial/`, `/objectives` | 200 with no substantive content (login-gated) | **The live objectives screen could not be verified**; no current objective list is claimed (`11A-OPEN-001`) |
| `politicsandwar.com/pwpedia/article/*` via generic HTML fetch | SPA shell for unknown slugs | Resolved by enumerating the real 149 slugs from the index and category pages |
| `nationstates.net/`, `/page=dispatch`, `/page=qa`, `/page=trade`, `forum.nationstates.net` | **403** on every attempt | **No official NationStates evidence**; the whole NationStates benchmark is community-sourced (`11A-RS-090`) |
| `wiki.nationstates.net`, `www.nationstateswiki.org` | Did not resolve | The reachable community source was `nationstates.fandom.com` via its MediaWiki API |
| `supremacy1914.fandom.com/wiki/Index_of_Power`, `/Ranks`, `/The_Daily_European`, `s1914.fandom.com/wiki/Coalition` | **403** on every attempt | Rank ladder and IoP formula remain community-derived and unconfirmed |
| `supremacy1914.com/`, `…/game.php?bust=1#/ranking/alliances/` | Login shell; login-gated SPA route | **Alliance scoring formula unverified** (`11A-BM-034`) |
| `supremacy1914.com/en/game-rules`; `bytro.helpshift.com/hc/en/3-supremacy-1914/categories/`; `playsupremacy.com/en/news/1914` | **404** | Correct paths found and used instead |
| Several Facebook post bodies and one Steam announcement body | Rendered without article text | Coalition-rework text and one event description not obtained |
| `playsupremacy.com/en/academy` | Video tutorials only; no article index | **No formal Supremacy 1914 tutorial could be confirmed** |
| `callofwar.fandom.com` | **403** | No Fandom evidence for Call of War |
| `www.callofwar.com`, its help root | Login/SPA shell | Relied on Bytro's official wiki and help centre |
| `support.travian.com/hc/en-us`, `/hc/en-gb` | **404** | The working official pattern is `/en/articles/<id>-<slug>`, discovered via the reachable sitemap |
| `www.travian.com/international/help` | JavaScript shell, no article text | Relied on the article pages directly |
| `travian.fandom.com/wiki/Medals` | 69 characters — an empty redirect | Travian medal evidence is official-only (`11A-RS-092`, `11A-RS-100`) |
| `erepublik.com` wiki `…/ERU`, `…/Nation` | **404** | The real-money cash-out loop is **unverified**, contrary to the brief's assumption (`11A-BM-053`) |
| `…/Battle` (energy), `…/Company`, `…/Country` | **403**, disambiguation, and no statistics respectively | Daily energy economics, company mechanics and any national leaderboard remain unverified |
| Tribal Wars rankings/snapshot article | **Does not exist** in the official knowledge base; a targeted search returned no results | Snapshot frequency and archives remain unverified (`11A-BM-044`) |

**Confidence consequence.** Politics & War and Travian evidence is largely CURRENT and official. Supremacy 1914's *structures* are official and current while its *numbers* are historical. Call of War and Tribal Wars are official but thin. eRepublik is official-but-dated. **NationStates is community-only and must be read as directional evidence.** Every recommendation in §21 is constructed so that it survives the removal of any single unverified claim.

---

## 6. Politics & War benchmark (primary)

Politics & War receives the deepest coverage because it is the only benchmark that is simultaneously a **persistent** multiplayer **browser nation-strategy** game, a **mapless-capable abstraction of nations and relationships**, and — as §1.1 established — a **two-hour, twelve-turn-per-day** world. It is also the only comparator whose recognition systems (score, leaderboards, awards, achievements, bounties, treasures, commemorative badges) are all observable on public live pages in a single sitting.

The detailed evidence for all 22 entries cited here is [`11A_comparator_sources_and_benchmarks.md`](11A_comparator_sources_and_benchmarks.md) §3.

### 6.1 Nation development and Nation Score (`11A-BM-001`)

**Observed.** The official guide states that "Score is generally the **main determinant of war and spy ranges**", determined through "Cities, Infrastructure, Projects, Military and Military Research", and gives the full arithmetic: `(City Count − 1) × 100 + (Nation Infra Total ÷ 40) + (Project Count × 20) + (Soldiers × 0.0004 + Tanks × 0.025 + Aircraft × 0.3 + Ships × 1 + Missiles × 5 + Nuclear Weapons × 15) + (Air Upgrades × 4) + (Ground Upgrades × 3) + (Naval Upgrades × 2) + 10` (`11A-RS-002`). The community page describes the three uses: **Ranking**, **War Range** — "only similarly sized nations are able to declare war on each other. This prevents very large nations from picking on very small nations" — and **Treasure** eligibility (`11A-RS-036`). The live nation page publishes the score, a **Nation Score Over Time** chart, a **Score Component Breakdown**, a rank **with a percentile** ("#55 of 11,958 Nations (0.46%)"), and a separate **War Policy** field (`11A-RS-026`, `11A-RS-027`). A public **Score Range Calculator** on the official tools page lets any player compute the attackable band at a given score (`11A-RS-028`).

**Analysis of the one-number-for-many-purposes design.** The design is genuinely economical: one recomputation serves the leaderboard, the fairness gate and event eligibility, and because eligibility is *relative* it self-scales as the world grows without retuning. Its cost is coupling, and the game's own changelog demonstrates it: the July 2025 update added military research to score at +4/+3/+2 per upgrade as part of a **military-balance** change, which mechanically altered **ranking** and **who-attacks-whom** at the same time (`11A-RS-012`). A developer tuning one purpose silently changed the other two. Three further symptoms: the additive weights mean raw stockpiling raises score, so an arsenal never used is still counted; cities contribute 100 each while infrastructure contributes 1 per 40, so the number is dominated by expansion rather than by intensity; and because the score is a sum of holdings, a nation that specialises in trade or diplomacy has no way to be *legible* in it at all.

**The four distinctions the brief asks about are real and separable.** Absolute national development (what exists) is observable from asset state; comparative ranking (how it compares) needs a window and a population; war eligibility (who may act against whom) needs a bounded, published, relative test; competitive progression (whether a nation is improving) needs a rate. Politics & War collapses all four into one scalar. **Recommendation preview (§21, `11A-DR-010`):** Nation Supremacy should **separate an eligibility measure from the public standings**, because our own subsystems already refuse the merge — `ECN-108` states national wealth "is **not** a score, a ranking or a spendable balance", `DMP-051` states approval is "not a score, an achievement currency or a ranking criterion", and `URB-158` forbids showing capacity, housing or research points "as a score that can be bought". The lawful design is therefore **several labelled domain measures plus one distinct eligibility function**, not a composite that means everything.

### 6.2 Objectives and onboarding (`11A-BM-004`)

**Observed (HISTORICAL).** A new nation is "presented with a tutorial and a series of **objectives** they must complete **in sequential order**. Some, such as #21 (Like the Facebook Page) are optional, but most need to be completed by the player to progress." The recorded list has 26 steps, including system-discovery steps that cost nothing (View Your Dossier; View the Changelog; Visit Notifications Page; Read the Game Rules), creative-identity steps (Edit Your Nation's Description; Update your Nation's Policies; Change Cover Image), economic and trade steps (Create a Trade Offer; Embargo a Nation), social steps (Send a Message; **Visit Discord Server**; **Visit the Alliance Recruitment Page**; **Join an Alliance**; Read the Game Rules), development steps (Build a New City; Build a Third City), military steps (**Recruit 5,000 Soldiers**; **Manufacture 25 Tanks**; **Stockpile 250 Munitions**; **Stockpile 150 Gasoline**; **Recruit 10,000 Soldiers**; Customize Military), and marketing steps (**Like the P&W Facebook Page**) (`11A-RS-035`, one revision, 2019-01-29).

**Can the live system be verified?** Partially. A live official nation page still states "This nation is part of the **tutorial system** and is operated by a script" (`11A-RS-026`), so a tutorial exists in 2026; the objectives screen itself is login-gated and its current content **could not be verified** (`11A-OPEN-001`). No reward amount for completing objectives is documented by any reachable source, so **no reward claim is made**.

**Evaluation against the brief's four questions.**
- *Do mandatory sequential tutorials teach useful systems?* Mostly yes for discovery steps — every "view the changelog / read the rules / open your dossier" objective is cheap and genuinely reduces the wiki-dependency problem `AP-006` names.
- *Do optional objectives create healthy goals?* This list contains only two optional items and both are **external marketing actions**, not gameplay goals, so the optional/mandatory split is drawn in the wrong place.
- *Do objectives improperly force players into activities?* **Yes, demonstrably.** Objective #16 compels alliance membership and #19/#20/#22/#23/#24 compel military stockpiling before the player has chosen a play style. That directly violates our `AP-004` ("Can a new player reach a meaningful goal alone?") and would violate `NAT-051` ("progression is **chosen**, not handed out").
- *Do objectives become outdated when mechanics change?* **Yes, empirically.** This is the strongest evidence in the study for the maintenance risk: the objectives page has exactly one revision, dated 2019-01-29, while the official guide confirms the military-research system beneath it was renamed and restructured in July 2025 (`11A-RS-012`). Objectives referencing specific unit counts and stockpiles are referencing a mechanic that has since moved. This is why `11A-CR-010` requires an objective to reference **owning-subsystem state** rather than a screen path or an incidental value, and why V-10/V-24 in the companion register treat objective staleness as an integrity risk (`11A-RK-024`).
- *Repetitive chores?* The list is a tour rather than a treadmill — the chore risk in Politics & War lives in the **daily login bonus** and **rewarded ads**, not in the objectives (`11A-BM-005`, `11A-BM-006`).

**One live consequence worth recording.** The same nation page's public activity feed shows other players repeatedly declaring war on the scripted tutorial nation, with 2026 declaration reasons reading "for the tutorial", "I want acheivement", "Part of the tutorial...i'm truly sorry, Avalon." and "Zero" (`11A-RS-026`). An **indestructible named target combined with an achievement for defeating it** converts onboarding content into a renewable farm. That is a direct lesson for §13.4's "objectives that reward attacking protected or weaker nations" and for `11A-RK-008`.

### 6.3 Awards and leaderboards (`11A-BM-002`, `11A-BM-003`, `11A-BM-008`)

**Observed — live leaderboards.** The official leaderboard page offers tabs **Nation · Alliance · Continent · Color Trade Bloc · Treasures · Moon Landing · Mars Landing · Commendations & Denouncements**, and within the Nation tab, "Top 100 Nations by **Score**" switchable across **Cities, GDP, Population, Age, Highest Approval, Lowest Approval, Soldiers, Tanks, Aircraft, Ships, Missiles, Nuclear Weapons, Casualties** (`11A-RS-003`). The list at access showed two nations at 13,891.25 occupying ranks 32 and 33 — equal values with **distinct ordinal positions**, i.e. no shared rank.

**Observed — awards (community, 2023-08-01).** "Awards are in-game badges… gained for reaching the top of certain leaderboards, for obtaining special achievements recognized by [the developer], or for having had a nation during a special event." Leaderboard awards are "**not permanent**… reassigned **every day just before update**, server time", there is "only one award for each category, so in any instance where there is a tie, **the award is configured to go to [the developer's] nation**"; the documented category list runs to 25 entries including Highest Score, Most Cities, Most Infrastructure, **Most Infrastructure Destroyed**, unit counts, **Most Casualties**, **Most Nukes Eaten**, Oldest Nation, Largest GDP, **Worst Environment**, Most Wars Won, Most Wars Lost and Best Wars Won to Wars Lost Ratio (`11A-RS-033`).

**Observed — awards live.** A current official nation profile's `Awards:` row is populated, and the page defines it: "Awards are special badge icons recognizing something special about a nation." The badges displayed are permanent commemorative ones — "Finished #2 Rank in Beta", "Participated in the P&W Beta", "Speed Round – 4th Place / Highest Population / Highest GDP", "This nation existed when P&W turned 1", "Played the full first year of P&W!", "**CN Milestone** – this nation was around when P&W surpassed CN in nation count", "**Singularity** – Game Date and Real Date Converged 25 June 2017" (`11A-RS-027`).

**How leaderboard position and permanent achievement differ, in practice.** Position is **ephemeral, comparative and reassigned**; the honour is **closed, dated and permanent**. Politics & War runs both, plus a third object — the **event badge** — and the distinction holds because none of them carries documented yield. Whether leaderboard awards are *still* being issued could not be confirmed (`11A-OPEN-002`), since no official page describes current issuance; the permanent class is confirmed live.

**Answering the brief's six ranking design questions from evidence, not preference.**

| Question | Comparator evidence | Position taken in §14 |
|---|---|---|
| Immediate update or scheduled snapshots? | P&W: daily reassigned awards, live-looking boards with no stated cadence; **Supremacy 1914** publishes daily but evaluates continuously — "scoring clock ≠ publishing clock" (`11A-BM-023`); **Travian** awards weekly at a fixed instant (Monday 00:00) for the previous week (`11A-BM-061`); **Tribal Wars** recalculates on completion but "sometimes the recalculation can be **delayed** to reduce server load" (`11A-BM-042`) | **Snapshot once per turn at a declared point**, publish at P7 only, and add a separate weekly window for medal-style honours. Consistent with `TR-041` ("world evaluation last means **rankings describe the turn that happened**") |
| Permanent or transferable leadership awards? | P&W separates them cleanly (`11A-BM-008` versus `11A-BM-009`) | Both, as **distinct object types**; a transferred standing must never be a permanent record |
| Can players manipulate a leaderboard just before a snapshot? | Yes: the reassignment instant is public, and P&W's documented tie rule is itself an admission that ties are frequent at the top; **Supremacy 1914 solved this by closing lottery purchases one turn before the draw** (`11A-BM-032`) | **Participation freeze before the snapshot**, plus windowed/rate metrics that a single boundary action cannot move |
| Should historical records be retained? | P&W retains 2014-era awards live in 2026 (`11A-BM-027`); Supremacy 1914 deletes finished rounds two weeks after completion (`11A-BM-027`) and promises a Hall of Fame (`11A-BM-030`) | **Yes, permanently for anchors**, within `TR-092`'s compaction model; our `TR-090` already makes major events P-class |
| Should rankings distinguish national strength from player skill? | No comparator does this explicitly. Supremacy 1914's **seasonal ladder is per-account and nation-isolated**, which is the closest thing to a skill measure (`11A-BM-030`); P&W's boards are purely national | Yes, but via **scope**, not a second score: nation-scope standings measure the nation; account-scope honours may recognise the player only where non-transferable and not re-earnable (`RRL-016`) |
| How treat inactive or retired nations? | P&W moves them to the **Grey** colour bloc, which "gives no bonus", and excludes them from all colour-bonus formulas (`11A-RS-012`, `11A-RS-015`); Supremacy 1914 applies a **small inactivity penalty** to seasonal points when a nation is taken over by AI (`11A-BM-030`) | **Neither.** `D-028` already decides it: excluded from public rankings as a **presentation rule** with **no loss** — which is more protective than either comparator and must not be weakened to a penalty |

### 6.4 Achievements (`11A-BM-010`)

**Observed.** "Achievements are unlocked in P&W by completing pre-determined tasks. **Three at a time can be showcased** on the nation page… On August 14, 2019, the initial set of **36** achievements were released, later followed the same day by a further 8, bringing the total to **44**. **They are not retroactive**" (`11A-RS-034`, last revised 2023-08-28). The catalogue spans development, military, diplomatic and social, economic, identity and policy, **attendance**, project and milestone, **event**, **purchase and promotion**, hostile-relationship and **staff/employment** families — including "*Login for a week consecutively*", "*Log In for a Year Consecutively*", "*Nation Over 3,000 Days Old*", "*Purchase the Limited Edition 9th Anniversary Package*", "*Subscribe to Politics & War*", "*Have VIP*", "*Watch a Rewarded Ad*", "*Like… Facebook*" adjacent promotional entries, "*Moderate the Politics & War Discord*", and "*Be attacked by someone with the Hannibal achievement*".

**Live confirmation of the data model.** An official achievement page for "Golden Treasures — Collect all the eggs added as part of the 2025 Easter Event" publishes **"This achievement has been earned by 1449 nations out of 14630 nations (9.90%)"** followed by a dated nation-by-nation list (`11A-RS-025`). That is the most reusable single idea in this benchmark: achievement definitions are fixed, grants are dated and attributed, and **the population that holds them is published**, which converts a badge list into legible rarity information without inventing artificial scarcity, and gives the operator a free health metric per feature.

**Assessment for Nation Supremacy.**

| Achievement dimension | Comparator evidence | Nation Supremacy position |
|---|---|---|
| Fixed definitions | P&W: "completing pre-determined tasks" | Supported; `11A-CR-010` requires state references, not paths |
| Historical/closed achievements | P&W permanent awards still displayed (`11A-RS-027`) | Supported as a **distinct** honour class (`11A-DR-016`) |
| One-time versus repeatable | P&W mixes; event achievements are per-year | Must be declared per object; `REQ-073` and `NAT-046` forbid re-earning by reroll |
| Military/economic/social families | P&W covers all four | Supported; **plus** defensive and non-conflict categories, following Travian's Defender and PvE separation (`11A-BM-061`) |
| Showcasing | P&W: three at a time (community-sourced, unconfirmed) | A **Prompt 13** presentation question; 11A specifies only that a set-claimable showcase must exist |
| Retroactivity | P&W: "**They are not retroactive**" | Adopted: retroactive grants would silently re-rank and re-reward. Consistent with `URB-099` "research never retroactive" and `NAT-050` starter-bundle versioning |
| Paid/promotional achievements | P&W anniversary packages, subscriptions, VIP, rewarded-ad, staff achievements | **Rejected outright.** `NAT-045` bars any differential by purchase or referral; `ECN-092` bars a prestige currency; and an employment badge in the same display family as play achievements conflates contribution-to-the-product with achievement-in-the-game |
| Victim-requiring conditions | "*Be attacked by someone with the Hannibal achievement*"; "*Win a war against someone with the Karma achievement*"; "*Defeat [the tutorial nation]*" | **Rejected.** A condition that names or requires a specific victim imports the farm-and-harass surface documented in §6.2 |

**Whether Nation Supremacy should distinguish five recognition types.** Yes, and the evidence supports exactly the split the brief proposes: **achievement** (a fixed condition met, dated, keyed), **milestone** (a state threshold reached — `NAT-052` already says these are records with no ranking weight), **seasonal award** (windowed, resettable, must not erase history — `11A-BM-030`), **historical honour** (closed eligibility, permanent, commemorative — `11A-BM-009`), and **competitive standing** (comparative, snapshot-based, may be reassigned — `11A-BM-002`/`11A-BM-008`). These differ in *eligibility closure*, *persistence* and *reassignment*, and collapsing any two is where the comparators' problems come from. §21 `11A-DR-013` adopts the five-layer model. Per `AP-008` and the brief's own instruction, **no comparator achievement name, icon or condition is reproduced.**

### 6.5 Warfare-related recognition

**Observed.** A live nation profile publishes, per unit type, **current holdings beside lifetime counters** — "Soldiers: / Casualties: / Killed:", "Tanks: / Lost: / Destroyed:", "Missiles / Launched / Eaten", "Nuclear Weapons / Launched / Eaten" — plus a **Nation Stats** block of **Infrastructure Destroyed, Infrastructure Lost, Money Looted, Wars Won, Wars Lost**, a dated public **Nation Activity** feed of declarations, embargoes, commendations and denouncements with timestamps, and an official **World Conflicts** page listing recent declarations for 1,541 wars with per-war timelines (`11A-RS-026`, `11A-RS-023`). Award categories include Most Casualties, Most Infrastructure Destroyed, Most Wars Won, Most Wars Lost and Best Wars Won to Wars Lost Ratio (`11A-RS-033`).

**Lessons only — B-10 is authoritative and unchanged.** Three transferable observations, and no battle mechanic is copied.
1. **Separate state from history.** P&W distinguishes *what a nation has now* from *what it has lost and inflicted over its life*. That is the correct shape for a chronicle input, and `WAR-147` ("the campaign record is **permanent**") already provides it. Prompt 11 must consume that record, not recreate it (`11A-INT-30`).
2. **Loss counters are not merit.** Ranking or awarding raw casualties and infrastructure destroyed measures human and material cost as an achievement, with no distinction between inflicted and suffered. Nation Supremacy's own privacy rule forbids the inputs anyway — `WAR-162` "no exact readiness, force or inventory is ever public" — so the lawful recognition surface is **participation, defensive outcome in published bands, and bounded campaign records** (`11A-DR-015`).
3. **A dated public activity feed is the cheapest chronicle primitive that exists**, and it is already specified for us: `TR-088` requires the digest to include world events and ranking/objective movement, `TR-090` makes major events P-class, and `WAR-153` already defines fourteen immutable append-only warfare event types. Prompt 11 should reuse that machinery rather than inventing a parallel event taxonomy — and must resolve the resulting **vocabulary collision**, since `WAR-006`/`WRA-06` already use "objective" for a campaign objective (`11A-INT-32`).

### 6.6 Politics & War benchmark table

| # | Mechanic observed | Source (status) | Design intent | Strengths | Weaknesses | Exploit risks | Lesson for Nation Supremacy | Must not copy |
|---|---|---|---|---|---|---|---|---|
| 1 | Nation Score, one scalar | `11A-RS-002` OFFICIAL CURRENT | Rank, gate war/spy ranges, gate treasure eligibility in one value | Legible, cheap, relative and self-scaling; the band is **published** (`11A-RS-028`) | Balance changes leak across all three purposes at once (`11A-RS-012`); stockpiling scores; specialisation invisible | Score suppression and snapshot inflation | Separate eligibility from standings; keep them in one *document family* but never one *number* (`11A-DR-010`) | The single-score triple duty |
| 2 | Leaderboards: one board, 13 metric columns, plus Treasures/Moon/Mars/Commendations boards | `11A-RS-003` OFFICIAL CURRENT | Comparative visibility | Cheap pluralism; percentile shown with rank; **Age** and **Lowest Approval** are rankable | No window; cumulative totals; casualties ranked without context | Metric-switching to a thin category | Plural standings derived from one lawful dataset; always show a window beside a total (`11A-DR-019`) | Casualty totals as a merit board |
| 3 | World Graphs aggregate dashboard | `11A-RS-024` OFFICIAL CURRENT | Explain the world's state | Averages, histograms, rolling activity windows, Top-25 slices | Suppression rule unstated | Differencing two tables | Aggregates are a **separate object** from rankings, governed by `D-027` k = 5 | — |
| 4 | Sequential tutorial objectives (26 steps) | `11A-RS-035` COMMUNITY **HISTORICAL** | Teach every system | Broad coverage; discovery steps are cheap | Compels alliance membership and military stockpiling; marketing tasks; single-revision page proves staleness | — | Objectives optional by default; B-03 already owns onboarding; reference subsystem state, not screens (`11A-CR-010`) | Forced alliance membership; external-platform tasks |
| 5 | Daily login bonus, two-step fallback | `11A-RS-013` OFFICIAL CURRENT | Habit formation | **Graduated** penalty instead of a cliff — genuinely better than reset-to-zero | Converts presence into currency; caps newcomers lower | Bot logins; alt stacking | Only the graduated-recovery *shape* may survive, and only where presence is not the trigger (`11A-BM-005` lesson) | Presence-for-currency of any kind (`TR-085`) |
| 6 | New Player Bonus income slope | `11A-RS-014` OFFICIAL CURRENT | Catch-up | **Transparent, finite, published table** | Age differential; distorts GDP comparisons | Bonus-window arbitrage | If assistance ever exists it must be a disclosed expiring table — but `D-021`/`NAT-045` currently forbid it | A 100 %-→5 % income multiplier by city count |
| 7 | Monthly donation-cap reset (recurring scheduled event) | `11A-RS-011`, `11A-RS-020` OFFICIAL CURRENT | Monetisation cadence | Calendar-deterministic, published effect, predictable, unfarmable by timing | Rewards purchase regularity | Coordinated purchase timing | **Deterministic calendar events are the cheapest lawful event class** (`11A-DR-003`) | Paid-advantage framing |
| 8 | VIP badge and paid custom graphics | `11A-RS-019` OFFICIAL CURRENT | Monetisation | Cosmetic; clearly labelled | Purchased recognition shares display space with earned | — | No purchasable recognition (`NAT-045`, `ECN-092`) | A paid badge in the honour set |
| 9 | 20-credit-per-month advantage cap, itemised | `11A-RS-020` OFFICIAL CURRENT | Limit pay-to-win | **Publishing exactly what is *not* for sale, item by item** | Timers and infrastructure are purchasable | External trading | Adopt the disclosure *format* if anything is ever monetised | Credit-purchased infrastructure/timer resets |
| 10 | Rewarded ads, $2M/day cap | `11A-RS-021` OFFICIAL CURRENT | Revenue plus retention | Voluntary, capped | Attention-for-currency | Automation | Barred by `TR-085` and AP-001 | The whole mechanism |
| 11 | Bounties (player-created, escrowed, no self-claim, **no expiry**) | `11A-RS-022` OFFICIAL CURRENT | Player-driven competition | Reserve-at-posting; first-claimant award; anonymity; blockade-deferred payout | Irrevocable capital lock; laundering potential | **Bounty coordination**, explicitly prohibited by the rules | Player-triggered events need reservation **and** expiry **and** counterparty independence (`11A-DR-007`) | Permanent un-cancelable escrow |
| 12 | Treasures: 30 rotating objects, 60-day respawn, 15–65 % of leader's score, Beige/Grey excluded, square-root alliance bonus | `11A-RS-004`/`005`/`012` OFFICIAL CURRENT | Recurring contested world event | **Relative band self-scales**; published per-object timers; protection-aware exclusion; diminishing collective return | 5–9 % income each, stackable → possession compounds; war is the main route | **Treasure transfer coordination** | Band-relative eligibility + published timers + exclusion of protected/inactive states (`11A-DR-003`) | Permanent yield multipliers (`ECN-113`) |
| 13 | Colour Trade Blocs incl. Beige (newcomer/defeated) and Grey (inactive) | `11A-RS-015`/`012` OFFICIAL CURRENT | Non-geographic grouping with bonuses | World-average-derived caps; explicit exclusion of newcomer/inactive/unallied from competition formulas | Unallied nations gain nothing from the layer; silent Grey assignment | Colour hopping; recruit concentration | Group competition is viable without geography, **but independence must remain viable** (`AP-004`) | State assignment by silence |
| 14 | Commendations / denouncements as public counts | `11A-RS-026`, `11A-RS-003` OFFICIAL CURRENT | Social signal | Cheap, player-generated, board-visible | Inflatable by rings | Mutual-endorsement farming | **Counts are lawful; a computed reputation is not** (`DIP-084`, `DIP-088`) | A derived trust score |
| 15 | Leaderboard awards, reassigned daily before update, **tie → developer's nation** | `11A-RS-033` COMMUNITY HISTORICAL | Transient recognition of current leadership | Snapshot-boundary reassignment; honour-only; includes non-combat categories | **The tie rule is indefensible**; single-winner daily prize invites last-instant gaming | Pre-boundary spikes | Honour reassignment must be at a declared snapshot with a **published** tie-break (`11A-DR-013`) | Operator-favouring ties; daily single-winner prizes |
| 16 | Permanent commemorative awards (Beta places, Speed Round, anniversaries, "CN Milestone", "Singularity") | `11A-RS-027` OFFICIAL CURRENT | Historical recognition | **Zero mechanical weight, twelve years live**; world-state triggers are computable without an author | Fossilises; later players can never earn | Identity laundering via account transfer | The strongest support for a permanent honour layer decoupled from power (`11A-DR-016`) | Donation-tier badges |
| 17 | Achievements with published completion counts and percentages | `11A-RS-025` OFFICIAL CURRENT | Recognition | **Rarity becomes legible**; dated attribution; free feature-health telemetry | — | Duplicate claims | Adopt the data model wholesale (`11A-DR-008`) | Attendance, purchase and employment achievements |
| 18 | Event achievements with payouts, 2-give/1-receive daily caps, per-city food cost, blockade escrow | `11A-RS-007` OFFICIAL CURRENT | Seasonal engagement | **Asymmetric receive cap** bounds farming; costed interaction; variety-plus-volume conditions; **escrow instead of forfeiture** | Pure-currency payout volume | Multi-account mutual servicing | Adopt all four structural properties (`11A-DR-004`, `11A-DR-005`); the escrow rule pairs with `D-028` | $150M-scale payouts |
| 19 | Annual Easter Egg Hunt: white reset / blue prior-claim-excluded / gold new; set achievements; hard UTC expiry; **second teardown boundary** | `11A-RS-008` OFFICIAL CURRENT | Annual event | **Two-stage teardown** honours in-flight work; recurring-but-not-renewable structure; cooperative discovery | Missing the window excludes you entirely; prior-claim tier is an account-history differential | Scripted URL hunting; location leaks | Teardown staging is directly adoptable (`11A-DR-004`) | Age-conditional value without a stated justification |
| 20 | Weekly lottery: fixed Sunday instant, 15-city and non-Vacation eligibility, **purchase freeze one turn before the draw**, player-funded pot, 10 % sink, rollover, achievement + notification, live reveal | `11A-RS-009` OFFICIAL CURRENT | Recurring scheduled event | **The pre-draw freeze is the single best integrity device found**; self-funding with a declared sink; published odds | Wealth floor excludes newcomers; randomness-as-achievement | Late-instant purchase racing the boundary | Adopt the freeze (`11A-DR-006`); determinism limits are set by `TR-047` | Long-odds randomness as a merit award |
| 21 | Pumpkin Art Contest: human-authorship requirement, in-game vote | `11A-RS-010` OFFICIAL CURRENT | Community event | A **voting** mechanic gives players a shared participatory action; integrity rule addresses a real modern failure | Needs an intake channel outside the game | Ballot stuffing; multiple entries | A player-voted annual recognition is lawful; **the submission channel is not** (no chat/upload surface in scope) | External-forum submission as the mechanism |
| 22 | Moon Landing / Mars Landing project chain: "no competitive advantage", **cannot be destroyed**, unique first badge + general badge + leaderboard + small daily approval effect | `11A-RS-016`/`017`/`018` OFFICIAL CURRENT | Long-term non-military goal | **One completion emits several recognition types**; explicitly non-competitive; indestructible; prerequisite chain makes intent legible | $200M gate bounds who can do it; permanent approval effect rides on a milestone | Very low | The template for lawful national progression (`11A-DR-014`, `11A-DR-017`) | A permanent recurring approval modifier granted by an event (`DMP-141`) |
| 23 | Unique-ID disclosure on every nation page for multi-account checking | `11A-RS-026` OFFICIAL CURRENT | Community-assisted enforcement | Makes detection a **shared, visible** activity | Player-surfed suspicion; privacy trade-off | False accusations | Evidence shapes for `11A-RK-009`; note our own stricter posture (`REQ-066` IP is never sufficient; `D-042` no raw IP) | Publishing identity-derived values |
| 24 | Public aggregate statistics with Top-25 cut-offs | `11A-RS-024` OFFICIAL CURRENT | World transparency | Distribution plus average plus window | No stated suppression rule | Differencing | `D-027` already gives the compliant answer (`11A-INT-27`) | — |
| 25 | Moderation Points: published bands, per-rule expiry, two-moderator approval, notify-but-not-execute automation line | `11A-RS-001` OFFICIAL CURRENT | Graduated enforcement | Predictable, expiring, dual-approved; a **workable automation boundary** | Moderator-dependent | — | Hand every risk in §18 to **Prompt 12** with an evidence shape | Any punishment schedule |
| 26 | Stepped inactivity: deletion at 31/60/97 days, automatic Vacation Mode by city count up to 365 days | `11A-RS-001` OFFICIAL CURRENT | Population hygiene | Recovers automatically on login | **Destroys the smallest, newest nations** while veterans park safely for a year | Absence gaming | Rejected: `D-028`/`ONB-041`/`ONB-046`/`ONB-047` are stricter and already accepted (`11A-DR-018`) | Any automatic deletion of an absent nation |
| 27 | World clock and boundary language ("Orbis Date"; "Next turn in"; "until after **day change**") | `11A-RS-026`/`007` OFFICIAL CURRENT | Shared fictional time | Events expressed as **boundaries, not timestamps** — the same discipline as `TR-028`…`TR-032` | Two clocks can confuse | — | Express every event window in turns and named boundaries (`11A-CR-026`) | — |
| 28 | Tools page incl. **Score Range Calculator**, infra/land/city cost calculators, battle simulators | `11A-RS-028` OFFICIAL CURRENT | Explain the mechanics | Publishing the eligibility band makes fairness **checkable by the player** | — | — | A published, computable eligibility band is a transparency win; `AP-006` demands the equivalent | — |
| 29 | Official API v3 with rate limits and a separate mutation key; third-party bots permitted to notify but not execute | `11A-RS-032`, `11A-RS-001` OFFICIAL CURRENT | Ecosystem openness | A clear line between convenience and automation | — | Scripted trading/banking | Useful boundary statement for `11A-RK-020` | — |
| 30 | Achievement page denominator (14,630 nations) versus leaderboard denominator (11,958) | `11A-RS-025`/`026` OFFICIAL CURRENT | — | — | **Two different populations for "how many nations"** | — | Any percentage we publish must state its **denominator and window** — adopted in `11A-CR-015` | — |

---

## 7. NationStates benchmark

**Why it matters:** NationStates is the only benchmark whose core loop is **policy expression**, which makes it the primary evidence for political identity, political participation and recognition-without-power. **Access limitation and its resolution:** every live `nationstates.net` and `forum.nationstates.net` URL returned **HTTP 403** to unauthenticated requests, so no live official page was readable. Official content was then recovered from **dated Internet Archive captures** — including a **2026-10-24 capture of the official FAQ**, a 2026 capture of the news index and dispatch index, a 2024 capture of the world-statistics page and a 2026 capture of the API documentation. Evidence below is therefore **OFFICIAL (ARCHIVED)** unless marked COMMUNITY; the archived status is recorded because currency is weaker than a live page, and the official Q&A archive (`page=qa`) could not be reached by either route (`11A-RS-114`).

### 7.1 National policy and identity (`11A-BM-058`)

Issues are "political decisions that players make, which **shape their nations as a result**", directly affecting civil rights, economy, political freedom and tax rate, and they "determine and change the **type of government** a nation has" across a named spectrum. Since 2016-02-29 decisions "take effect **immediately**, and players can view the effects in detail"; before that, consequences arrived the next day. Five generation classes exist — **General** (random, no preconditions), **Population-Based** (unlocked by population; **a dismissed one can return later**), **Issue-Option** (unlocked by a prior *choice*), **Statistic-Based** (unlocked by a statistic threshold), and **Special** (rare, membership-gated), plus easter-egg issues awarding a unique badge. Cadence is **player-configurable**: one every six hours by default, with 12/24/48-hour options.

**Design lesson.** The five trigger classes are a **complete taxonomy for systemic content generation** — unconditional, state-threshold, prior-decision-chained, statistic-gated and membership-gated — and require no editorial calendar (`11A-DR-001`). The **player-settable cadence** is the best answer in the whole study to the notification-fatigue question the brief §12.4 raises, because it moves the choice to the player instead of the operator. And "**dismissal is not forfeiture**" is the humane rule that our `D-028` logic already implies for absence.

### 7.2 Political and international participation (`11A-BM-057`)

World Assembly membership is "**entirely voluntary**", requires e-mail verification, permits **one member per player** with a stated consequence for violation ("ejected for one year"), and may be resigned at any time. The Security Council's institutional instruments are **to condemn or commend** nations and regions and to liberate regions; the General Assembly legislates.

**Design lesson.** Two things transfer. The **named, time-bounded, stated consequence** is exactly the form Prompt 12 needs ("each prohibited behaviour has a rule, a consequence and an evidence source"). And the observation that a world body's only standing instruments are **records of approval and disapproval** is precisely what `DIP-084`/`DIP-088` permit us to build: **factual public counts, never a computed standing** (`11A-DR-023`).

### 7.3 Regional influence and reputation (`11A-BM-055`, `11A-BM-056`)

Influence "was created **as a way to prevent new members of a region from seizing the delegate position and *immediately* ejecting & banning everyone else**". Nations earn influence by **remaining** and by accumulating **WA endorsements**, and — the notable part — "**Delegates consume some of their Influence to exercise their power, so the more often the Delegate uses their influence, the more difficult it is for them to wield those powers in the future.**" Delegate selection is decided "**during the daily game update**", with the tie "the nation that has been in the region **longer**"; a delegate's votes equal endorsements plus one. The community page also records the abuse honestly: endorsement battles are "the heart and soul of **region crashing**".

**Interpretation.** Influence is the inverse of a prestige currency: **standing as a spendable budget on authority**, so seniority buys *durability of office* rather than *more power*. For Nation Supremacy it must not be ported — it is a power currency, and `ECN-092` bars a new accumulating resource while `DMP-051`/`DIP-084` bar exactly this kind of derived standing. What is worth keeping is the **principle**: cap and rate-limit authority rather than grant it, and let recognition be durable while power stays bounded (`11A-DR-028`).

### 7.4 What NationStates teaches Nation Supremacy, and what it must not import

1. **A purely descriptive measurement layer can carry an entire game.** The World Census publishes dozens of categories, generates **a random category report each day against the world median**, and grants nothing (`11A-BM-054`). This is the strongest available evidence that "no single dominant ladder" is not a handicap — a game can have *many* ladders that all matter little and one *identity* that matters a lot. It maps directly onto a lawful Nation Supremacy object: a national profile assembled from already-public statistics, compared to the world distribution, with **no** reward attached (`11A-DR-027`).
2. **Long-term political activity should be recognised, and recognition is enough.** Endorsements, delegate tenure and commendation counts are all visible and all inert. This is the same line `DIP-088` already draws — "A player may use it; the game does not."
3. **Political participation can be a genuine second path only if it moves shared parameters, not personal scores.** eRepublik's congress moving tax and wage (`11A-BM-050`) shows the mechanism; NationStates shows the *identity* payoff. Our equivalent already exists: the B-06 policy axes and the 240-turn election cycle (`DMP-094`, `DMP-177`).
4. **Not imported, by instruction and by rule:** region mechanics, the delegate/founder structure, influence as currency, endorsement-weighted voting, and any player-created grouping that is not an Alliance. §7.4's own instruction is that "Nation Supremacy must preserve its own political and Alliance architecture", and `UD-047`/`UD-049` are owner-reserved. Nothing in this section proposes an Alliance change.

### 7.5 The strongest NationStates finding: milestones that grant authorship, not power (`11A-BM-067`)

**Observed (official, archived).** "Why can't I set my nation's pretitle, Capital City, Leader, or Religion? This becomes possible at particular population levels: **250 million**: …issue that allows you to set a **Capital City**… **500 million**: You can write a custom **pretitle**… **750 million**: The **Leader** issue… **1 billion**: The **Faith** issue. **If you dismiss the issue, the custom field will remain locked and you will receive the same issue again at some point in the future**" (`11A-RS-102`).

This is the single best-fitting progression mechanism in the entire study, because the reward for growth is **the right to name your own nation** — capital, leader, pretitle, faith. It cannot create a capability gap, cannot be farmed into advantage, cannot be transferred, and becomes more meaningful precisely as a player becomes more invested. Its decline rule is the "dismissal is not forfeiture" property in practice: nothing is lost, and the offer returns.

It is admissible under our constraints in a way no comparator's progression ladder is: it touches neither `ECN-092` (no new currency), nor `DMP-051` (approval is not an achievement currency), nor `URB-158` (no purchasable score), nor `NAT-052` (milestones grant no ranking weight), and it literally instantiates `NAT-051`'s "progression is **chosen**, not handed out". **The one part that must not be copied is the driver:** NationStates' population "grows steadily over time no matter what you do", so its ladder advances on elapsed time. Our `NAT-045` forbids a differential by age and `INV-025` forbids catch-up introduced through age or protection, so any equivalent ladder must advance on **achieved state**, not duration (`11A-DR-017`, `11A-DR-032`).

### 7.6 Inert collectibles, bounded queues and post-decision obligations (`11A-BM-068`, `11A-BM-069`, `11A-BM-070`)

Three official, archived findings that bear directly on Domain B.

**Cosmetics declared inert in the rule text itself.** "Postcards, which can be used in your nation banner, are awarded when you reach a particular state. If your nation is already close to that state, a small step in that direction can get you over the line"; and of trading cards, "**Cards are cosmetic. They grant no benefits other than the warm fuzzy feeling of owning them**", with an auction deliberately designed to reduce "the ability of puppet nations to feed valuable cards to their masters" (`11A-RS-102`). **Lesson:** *state-triggered* recognition ("you reached a condition") generates no chore, and publishing a reward's inertness in the rule text is a stronger fairness guarantee than an assurance. Both are adopted in `11A-DR-008` and `11A-DR-033`.

**A hard cap on outstanding content, with penalty-free dismissal.** "**Nations can hold a maximum of five issues.** Dismiss or deal with some first, and new ones will begin flowing in"; dismissal is a named option — "**Dismiss it!** This is the equivalent of ignoring an issue" (`11A-RS-102`). No other benchmark bounds its outstanding content this way: Travian destroys uncollected rewards at reset, Politics & War's event windows simply close, and Supremacy 1914 lets pots roll over. A bounded queue makes content pressure a **player-visible state** rather than a duty, and it composes with our `TR-089` single bounded digest row. Adopted as `11A-DR-005` and `11A-DR-009`, and it is the most concrete answer available to the brief's §12.4 notification-fatigue question.

**Voluntary jurisdiction with an ongoing obligation.** World Assembly membership "is not compulsory. If you remain outside, you're mostly unaffected by its decisions", but members who fail to adopt at least **75 %** of passed law "will be deemed non-compliant, and **not allowed to participate in future WA votes**", and that threshold was raised by an official post on 2026-08-19 (`11A-RS-102`, `11A-RS-103`). Legislative access is tiered — **≥2 endorsements to propose, only Delegates approve, 6 % of Delegates for a quorum** — and the elected Secretariat requires **≥5 endorsements** to stand and a **30 million population** floor to vote. **Lesson:** membership-as-jurisdiction, where opting out is a legitimate permanent choice with a stated and *proportional* consequence, is exactly the right model for voluntary cooperative objectives under `AP-004`, and a **post-decision obligation** is what turns a one-off event into a lasting participation path (our analogue is already accepted: B-06's continuous retention tests, `DMP-215`…`DMP-224`). **Rejected:** endorsement-weighted voting and population-gated franchise, which conflict with `DMP-195` and `NAT-045`.

### 7.7 Influence, magnetism, and the honest negative findings (`11A-BM-071`…`11A-BM-073`)

**Influence, corrected (`11A-BM-071`).** The official FAQ gives a more precise account than the community page used in the first pass: influence accrues from remaining and from endorsements; "**when a nation leaves, its influence in that region begins to decline**"; and "**the more influence a nation has, the more influence the Delegate requires to eject it from the region**" — so a target's own standing raises the cost of removing it, and Delegates "must spend Regional Influence" while Governors need not. The 2006 origin thread confirms the intent was to cap how much power a newly arrived cohort could immediately exercise. **Assessment:** still inadmissible for Nation Supremacy, because it is a *power* currency and `ECN-092`/`DIP-084`/`DMP-051` together close that door. The two reusable *principles* are: **make removal of an established actor cost more than removal of a newcomer**, and **rate-limit an office rather than grant it** — both handed to Prompt 12 as governance observations, with `UD-047`/`UD-049` left untouched (`11A-DR-028`, `11A-OPEN-015`).

**Magnetism (`11A-BM-072`).** A community-documented official behaviour assigns a Frontier region's share of new spawns from **freshness and hospitality** — a welcome telegram, an active message board, a delegate with five or more endorsements — with negatives including a password, no delegate, and more than **5,000 residents**, and a deliberately **inverted** incumbent rule: a delegate in office "at least 2 days, and ideally **less than 6 months**" scores better than a long-term incumbent. **Assessment:** the most interesting collective-progression object in the study, because almost nothing in it is power, and its anti-entrenchment inversion is a considered answer to exactly the fossilisation problem that Politics & War's permanent awards (`11A-BM-009`) and eRepublik's preserved-advantage rewrite (`11A-BM-049`) both fail to solve. **Confidence is Medium** (community-mirrored; no official page reachable), so only the *shape* is adopted, and only as honour-only and capped (`11A-DR-011`, `11A-DR-016`).

**Two negative findings, recorded as findings (`11A-BM-073`).** First, **NationStates has no achievement system at all** — its official FAQ enumerates its sections completely and includes none, and its only award-like objects are postcards, cosmetic cards, commendation/condemnation badges and easter-egg issue badges; the live "award" publications are player-run bodies. A game with an eighteen-year lifespan sustains long-term motivation on identity, status and description rather than on a checklist. Second, **no composite national rating exists**: the term sometimes used for one could not be traced to any official mechanic, and the real objects are per-category census percentiles ("Rank 171,969th (Top 100%)") and a 27-way government type derived from three freedoms. Third, and relevant to our trade integration, a third-party source records that NationStates has **no war or trading mechanics between nations at all** (`11A-RS-112`). **Consequence for this report:** the achievement framework Prompt 11 owns is **permitted, not obligatory** (`NAT-052` gives ownership; nothing requires maximal use), which is why §13 recommends a deliberately small achievement layer and puts the weight on records, standings and authorship.

---

## 8. Supremacy 1914 benchmark

**Why it matters:** the clearest documented **cross-round seasonal progression** system and the clearest **relative-index** design. **Critical limitation:** it is built entirely on provinces, morale-per-province, control points and coastline. Everything geographic is excluded; only the abstractions are considered.

### 8.1 Victory and ranking (`11A-BM-023`, `11A-BM-024`, `11A-BM-025`, `11A-BM-026`)

**Index of Power.** Officially "players are ranked by their Index of Power score, or 'IoP'… **relative** and denotes the **share of power across all players participating in the match**", raised by conquering territory, building and upgrading structures and improving morale. Community sources derive a per-province formula normalised so the **total pool is `2000 × player count`**, which is why the win thresholds are stated as percentages. Because the index is relative and its components are destructible ("Buildings can be destroyed without annexing a province. Morale can be damaged directly"), the game ships an **erosion strategy** alongside the accumulation strategy.

**Victory conditions.** The official rules enumerate **four** ways a round ends — Victory-Points threshold; a Dominion **hold-control-points-for-N-days** condition; the **round timer reaching zero**; and a **Retire option available when three or fewer users remain active** — plus an explicit deviation channel: "Certain official rounds may have special rules… **Such deviation… will be mentioned in the event announcement**." Two further findings are directly relevant: **solo and coalition victory bars are separate and non-convertible** ("Coalition points will **not count** toward a solo win"), and a **second, in-round Victory Progress leaderboard now pays a daily bonus to its top positions, where "the longer you maintain your lead, the greater the reward"**.

**Abstract lessons only.** (i) **Normalise the pool, then express thresholds as percentages** — this is what makes a competitive structure survive population change (`11A-DR-019`). (ii) **A closed end-condition enum with a published deviation channel** is the correct shape for any season or event termination (`11A-DR-003`, `11A-DR-018`). (iii) **Group and individual bars must be separate and non-fungible**, which our `ALL-224` already enforces from the funding side (`11A-DR-011`). (iv) **Distinguish attained position from sustained position**, with a published curve (`11A-DR-020`) — noting that a duration-weighted leader bonus is a compounding loop and must be bounded.

### 8.2 Events and competitive structures (`11A-BM-030`, `11A-BM-032`, `11A-BM-033`)

**Seasons.** Season 1 (2026-04-30) introduced **Seasonal Ranking Points**: "**every player starts the season with the same amount of rank points**… killing enemy units and conquering provinces will **increase** your points, while **losing** units and provinces will **decrease** them… **Every match will have an impact on your rank**", with cross-platform accrual, an honest staged rollout ("ranks will not be visible in the beginning… we will periodically update you"), and a promised **Hall of Fame**. Season 2 (2026-07-31) is the anti-exploit tuning pass: **infantry excluded from the kill economy**, a **higher penalty for losing units**, a **one-time defeat penalty** for quitting early, and a **small inactivity penalty** for nations taken over by AI. The finale (2026-11-02) publishes live standings and the reward band (**top 5,000** unlock a unit).

**Events as parameter tuples.** The anniversary campaign rotates event maps each defined by (speed multiplier, fixed runtime, country-assignment mode, inactivity limit, reward multiplier, victory variant, identity visibility), with published start instants. Legacy creation parameters include an **Anonymous Round** ("it will **not be visible which character in the game is played by which user** until the game ends"), team configurations with hard non-betrayability, a maximum-inactivity setting, and a **Peace Period** that is **symmetric and unbreakable** ("not possible to declare war, attack any human players, **or be attacked by them**… This non-aggression pact cannot be broken").

**Objectives.** No formal tutorial could be found. Engagement is mission-shaped: **Operations** with **two reward lanes** where the vendor's own fairness statement is "**There's no extra grind: each completed task advances both tracks simultaneously**", plus one deliberately trivial re-entry operation, and rewards **claimed** rather than auto-granted.

**Fairness.** The rulebook defines three competitive offences with intent-based tests: **wolf-packing** (including "joining a game round with a group that **exceeds the maximum coalition size** and playing cooperatively… you need to play the game **as if you were not allied**"), **account pushing** ("solely or mainly joining a game to aid another user… **not contingent on a certain date of joining**"), and **capital farming** ("recruiting other users **with the purpose of harvesting** capital cities"). Anti-cheat opt-out means "no points will be awarded on your **service record**".

### 8.3 Long-term lessons, and the geographic exclusions

| Abstract lesson adopted | Where it goes |
|---|---|
| Equal-start-per-season ladders remove veteran advantage without touching permanent history | `11A-DR-013`, `11A-DR-018` |
| Symmetric gain-and-loss scoring, with penalties anchored to existing game-state events rather than separate timers | `11A-DR-019` — but **capped by `D-028`**: a season may stop accruing during dormancy and may **never subtract** |
| Exclude the cheapest repeatable action from a scored source (the infantry exclusion) | `11A-DR-015`, `11A-RK-023` |
| Normalised pool, percentage thresholds | `11A-DR-019` |
| Participation freeze before any draw or snapshot | `11A-DR-006` |
| Intent-based, cap-referencing fairness definitions | Handed to **Prompt 12** (`11A-RK-005`…`11A-RK-007`) |
| Progressive-unlock-by-rank (ladder buys *options*, never power) | `11A-DR-017`, bounded by `NAT-045` and `URB-158` |

**Excluded as geographic, per the brief §8:** province capture and conquest; geographic control points; map movement and adjacency; territorial objectives; distance-based scoring (including capital-distance morale); coastline and harbour effects; terrain combat modifiers; frontline and border-friction concepts; per-province morale and revolt-driven ownership transfer; capital capture and capital-farming; and every named historical scenario. The `13` geographic dependencies are listed in full in the companion register §5.1.2.

---

## 9. Travian: Legends benchmark

**Why it matters:** Travian supplies the fully documented **recurring-objective system**, a **weekly scheduled medal cycle**, and the genre's only **officially documented non-military victory path**. Uniquely, its evidence is almost entirely **official** — twelve help-centre articles retrieved verbatim (`11A-RS-091`…`11A-RS-098`).

### 9.1 Daily and recurring objectives (`11A-BM-060`, `11A-BM-066`)

**Official structure.** "Each day you'll receive **up to 10 tasks**… Each quest you finish earns **points**… You can earn rewards at **25, 50, 75, and 100 points** — up to **4 rewards per day**. **Quests and rewards reset once per day at the same time your gameworld started**… **Important: You must collect your rewards before reset — otherwise, they are lost.** **Rewards cycle in a fixed order (not random), and every player on the same gameworld sees the same reward set.**" Published reward contents across the four tiers include resources, hero experience, culture points, consumables, an extra adventure, **+1 day of +25 % production of a named resource**, and **+1 day of the paid Travian Plus account**. Official notes: rewards activate immediately; "**server speed does not affect rewards**"; and "some quests require **bulk actions** — for example, **train 20 units at once**. Training them individually will not count."

**Separately**, the persistent **Task System** gives per-village building tasks (levels 1, 3, 7, 12, 20) and whole-avatar general tasks whose thresholds run "500, 1000, 1500, 2500, 5000, 10000, 20000… (**unlimited increments, doubling each time**)", with rewards scaling by task-type multiplier, **increasing for each repeat**, and a hero-level bonus.

**Design lessons.** *Adopt:* the bounded-container shape — **N tasks, a few cumulative thresholds, a deterministic published rotation identical across the world, one reset derived from the world clock, and value invariant to world speed** (`11A-DR-029`); **geometric thresholds with an unlimited tail**, which never saturate and never need an artificial new rank tier (`11A-DR-031`); and the **two-scope split** (per-city and whole-national) which mirrors our own nation-versus-account division. *Reject:* **destruction of unclaimed rewards at reset**, which `D-028` and `ONB-041` forbid; the **production-multiplier reward**, forbidden by `ECN-113` and `URB-101`; **escalating repeat rewards**, a snowball generator; the **bulk-action** requirement, which rewards an interaction shape rather than an outcome and pressures automation; and a paid-account trial inside an objective reward.

### 9.2 Performance recognition (`11A-BM-061`)

"Weekly medals are granted **every Monday at 00:00 (server time)** for the **previous week's performance**." Player medals: **Top-10** in **Attackers, Defenders, Raiders, PvE**. Streak tiers in **both** consecutive and non-consecutive forms (Top-3 in a category 3/5/10 times, not consecutive; Top-10 in a category 3/5/10 times, consecutive; Top-10 in **both** Attacker and Defender in the same week 1/2/3 times). Alliances receive Top-10 medals for Attack, Defense, Raiding and **Climbers (population growth replaces PvE)**, displayed with laurel branches. Tournament medals cover Attack, Defense, Population, World Wonder and **Survivor ("played to the end")**. Local medals recognise participation in community-designed local worlds; special medals include **Veteran medals for 3/5/10 years** and one-time awards, and the very first medal — the **dove of peace** — "**shown during beginner's protection and then fades**".

This is the best competitive-recognition design in the study, and the reason is that it is **windowed, category-separated, and includes defensive and non-conflict categories**. The cross-category exclusion is made explicit elsewhere: "killing Natar troops gives **PvE points, not attack points**, so it won't help you climb the attacker ranking" (`11A-BM-064`) — a live game closing the laundering path between two boards by design (`11A-DR-015`).

### 9.3 Seasonal and event competition (`11A-BM-061`, `11A-BM-062`, `11A-BM-063`)

**Tournament.** Annual, two stages: **Qualification** from June across four regional game worlds (America, Arabics, Asia, Europe), then **Finals** on one global server from November, entry **by key only**, with a **wild-card raffle**. Qualification keys require remaining active to the end **and at least 10 villages**. Prizes are real-world: a **€4,000 digital voucher and a unique trophy** for the winning Wonder holder; €2,000 for ranks 2–5; €1,000 for ranks 6–13; Gold vouchers for alliance members of top-Wonder alliances; 1,600 Gold for top-20 in offense, defense or population.

**The decisive line is on the same page:** "**Winning a normal Travian: Legends server does not provide a prize or medal.**" Ordinary competitive success is honour-only; real prizes are reserved for a separate, explicitly framed spectacle. Per the brief §9.4 and `AP-008`, **no cash or voucher structure is proposed**; the transferable insight is the *separation* — a routine ladder pays recognition, and only a bounded, announced spectacle pays anything else (and in Nation Supremacy, under the ₹0 constraint and `NAT-045`, even that spectacle pays recognition only).

**Season Pass.** Account-level progression "**shared across your lobby account**… **not tied to a single avatar or game world**", five missions per day (2 Daily + 3 Random), missions with **tiers granting partial points**, cross-world completion permitted, and a random mission **rerollable once per day only via watching a video or spending a shard**. Two features are disqualifying for us: one Daily Mission is literally "**Daily Login**", and "**actions performed on your avatar by duals and sitters also count** toward the avatar owner's lobby account" — i.e. multi-account activity credited to the owner as a designed behaviour, against our `D-032`/`REQ-061` one-account rule and `11A-RK-009`.

### 9.4 Design lessons, including the anti-farming evidence

**Victory without warfare (`11A-BM-063`).** "The first player or alliance to build their Wonder of the World to **level 100** wins the server… Each level requires hundreds of thousands — even millions — of resources… it's **impossible for a single player to complete one alone**… **Once level 1, the village cannot be conquered**", and inside the wonder village "**no Gold usage**", no treasury, no culture points. The lawful Nation Supremacy analogue is *shape, not mechanic*: a long, visible, cumulative, cooperative accomplishment whose **investment cannot be confiscated** and whose reward is completion plus record. We already own a compatible object — B-05's **four branch capstone programmes** (`URB-107`, 100 RP each, indestructible and non-tradable) — so a **capstone-completion record** is available without creating new infrastructure (§16.4, `11A-DR-030`).

**Fairness (`11A-BM-064`).** Beginner protection is **symmetric** (the protected player also cannot attack), **cannot be ended early**, scales down with world speed, and is **explicitly separated from the attacker ranking**. The market rules add a population-scaled **1:1-or-better acceptance** restriction and candidly document their own leak: players post unacceptable offers "so nobody can accept them… **use them as extra storage**". The symmetry matches `ONB-023`/`ONB-024`; the ranking separation is adopted (`11A-DR-015`); the no-early-exit rule is **not**, because `ONB-020` is an accepted rule we may not silently tighten.

**The uncomfortable finding (`11A-BM-065`).** Travian ships **farm lists** as a free universal feature — "up to **100 farm lists**, each holding up to **100 targets**… send raids to all of them with **one click**" — and separately publishes a guide, "How to avoid getting farmed", advising players to keep growing visibly and to "maintain your village population within the **top 200–300 players**". Two constraints follow: **no 11B objective or event may be materially cheaper through a bulk tool than through the considered action**, and **no design may make development level a precondition of safety** (`11A-DR-024`, `11A-RK-003`, `11A-RK-008`).

**Other exclusions:** resource-field geography, village coordinates, marching distance and speed, wall levels, oasis and Natar geography, and grey-zone mechanics.

---

## 10. eRepublik benchmark

**Why it matters:** the only benchmark running **military, economic, political and media careers on one account** — the structure §17 requires. **Critical limitation:** its official wiki changelog appears frozen at ~**2023-12-31**, the `ERU` and `Nation` articles return **404**, and no anti-cheat or moderation policy page could be found, so most current-state claims are **HISTORICAL or UNVERIFIED** and the 23-item gap list in the companion register §5.4 is the longest in the study.

**Parallel paths, and why they are only semi-parallel (`11A-BM-048`).** The tracks exist as navigation-level first-class clusters, but **one hidden ladder gates them**: a newspaper needs level 9, congressional candidacy level 15, and the founding artefacts cost premium currency (company 10, unit/party 40, war 200, newspaper 2 Gold). **Lesson:** if Nation Supremacy offers parallel paths, **no path may be gated behind another path's grind or currency**, or the design silently collapses into one ladder with cosmetics (`11A-DR-024`). Our own rules already block the easy version of the mistake — `ECN-092` (no prestige currency), `DMP-051` (approval is not an achievement currency) and `NAT-045` (no differential by purchase).

**Military progression (`11A-BM-049`).** Rank derives from cumulative damage (reported at 10 % of damage), rank-up grants a free energy bar plus a permanent damage bonus, and the top of the ladder was extended twice ("Titan" at day 2,032, "Legends of the New World" at day 2,586) before being **re-based** onto **Protectors of Nations**, where points come from "**damage, country, and vehicle enrollment in the Armory**" and veterans keep "the same or higher bonuses". **Lesson:** the multi-input re-basing is genuinely good — recognising **personal performance, national service and logistical contribution** in one track rather than one damage counter (`11A-DR-025`) — while "preserve existing advantage across a rewrite" is exactly how an elite fossilises (`11A-RK-009`). The energy-gated daily battle loop is barred by `TR-085`.

**Politics (`11A-BM-050`).** A **monthly triple-election calendar** (Party President on the 15th, Congress on the 25th, President on the 5th) with Congress described as a 40-seat body holding power over "**taxes and minimum wage, but not war declarations**", and candidacy gated by level and a party-president-chosen slate with "no minimum". **Lesson:** a predictable political calendar is the strongest event-rhythm device here, and making the political track move **shared parameters that every standing measures** is what gives it weight without its own experience points. We already have a better version — `DMP-177`'s 240-turn per-nation cycle with five published dates and exactly-once contest identity (`DMP-182`) — so the transfer is a confirming precedent, not a new proposal. Slate control is recorded as a cautionary gatekeeping pattern.

**Recognition (`11A-BM-051`).** "Decorations are special achievements granted for acts of great valour in tournaments and events… Citizens find them in their profile", with criteria such as "**One of the first 50 citizens from (country)** to win 10 Freedom Fighter medals." **Lesson:** a **sub-population-scoped first-N honour** creates permanent, non-inflating scarcity that remains reachable for a small community — directly implementable within `D-027`'s aggregation rules (`11A-DR-016`), at the cost of fossilising (`11A-BM-009`).

**Media as a soft path (`11A-BM-052`).** A paper costs 2 Gold and level 9; owners may edit or delete **within 30 days**; "players **endorse** articles". The bounded correction window is a good integrity rule and matches `TR-091` (corrections are appended disclosed events). **Boundary note:** this must not be read as a proposal for in-game publishing or chat. Stage 2's register already requires that Prompt 13 "**must not** design native real-time Alliance chat, voice, or a Discord or other third-party messaging integration; in-game notifications and audit visibility are the supported surface."

**The pattern to avoid (`11A-BM-053`).** Verified: real money buys premium currency which buys **rights** — to found a company, form a party or unit, declare a war, publish a paper. Player testimony in the game's own article space: "**Players are forced to either grind their way up or use their credit card**", answered with "far too **pay-to-win**". **Not verified:** the ERU→cash-out loop (the `ERU` page is 404). **Lesson:** no rule, objective, event or ranking may price a right of any kind — already fixed by `NAT-045`, `ECN-092`, `REQ-073` and the ₹0 constraint (`11A-DR-012`).

**Player-authored structure over a flat primitive (`11A-BM-049`).** The engine supplies a single unit object; players layer battalion, division, army group and high command, ranks and promotion tables themselves, and the wiki now describes "regiments" while players say "division". **Lesson:** decide early how much hierarchy to bake in. Unofficial structure is unenforceable, unauditable and forkable — and in a game with no moderation staff it cannot be relied upon at all. Our B-09 already chooses a player-authored **constitutional** model (`D-135`/`DD-151`) with a *bounded* permission set, which is the middle position.

---

## 11. Additional game benchmarks

Two games were selected independently. Neither was added to increase a count; each supplies evidence no other source does.

### 11.1 Call of War: World War 2

**Why selected:** same publisher lineage as Supremacy 1914 but with **four simultaneous termination channels** and a **partly account-persistent research tree** — the best available model for ending a competitive structure without geography, and for longitudinal progression that survives a reset. Evidence is official (`11A-RS-061`…`11A-RS-064`); `callofwar.fandom.com` returned **403**.

| Finding | Entry | Lesson adopted |
|---|---|---|
| VP threshold detected, then the round "will end **at the next day change event**"; the winner is the highest scorer at that point | `11A-BM-038` | Evaluate on state, **apply at a boundary** — already mandated by `TR-038` and `TR-030`; adopted for seasons and events (`11A-DR-003`) |
| Duration tiers (Small 35 / Medium 49 / Big 70 days) plus a **dissolution rule at three active players** | `11A-BM-038` | A bounded competitive structure needs a **termination and dissolution** clause stated in advance, not improvised |
| Dominion: **hold >50 % of a fixed set of objectives for 3 days** | `11A-BM-039` | **Sustained majority control of a scarce, abstract, non-spatial slot** is the strongest non-accumulation competitive idea for a mapless game (`11A-DR-002`, `11A-DR-022`) |
| Research: two concurrent slots; elite tiers gated by **collectible blueprints**; "Research persists if all elite blueprints collected" | `11A-BM-040` | **Slot-limited, time-gated** progression is adoptable as a shape; **all-or-nothing persistence is not** — `RRL-013` destroys rerolled research and `URB-099` forbids retroactivity (`11A-DR-017`) |
| Wolf-packing and account-pushing prohibited as rules, alongside victory conditions | `11A-BM-041` | Confirms the two canonical exploit classes for any round-based competitive ladder; handed to **Prompt 12** (`11A-RK-005`…`11A-RK-007`) |

**Gaps honestly recorded:** no evidence of a national strength index or leaderboard, no objectives/tutorial/daily-reward documentation, and no documented event or special-round system — the community's 2017 account of surprise round endings is anecdote, not a rule.

### 11.2 Tribal Wars

**Why selected:** the best-documented **derived, non-military national standing** in existence, plus a **persistence seam declared per competitive mode** rather than globally. Evidence is the official InnoGames knowledge base (`11A-RS-066`…`11A-RS-070`).

**(a) Points are a pure function of completed construction (`11A-BM-042`).** "You receive points for the **completion of buildings**. As soon as the building is finished, your points **and place in the ranking** are newly calculated (sometimes the recalculation can be **delayed to reduce server load**)." This is a mapless-legible strength model: standing = what you finished, computed lazily at boundaries — exactly B-02's shape — and it is the empirical basis for recommending a **development-derived** standing (`11A-DR-010`). **Recorded conflict:** the same sentence claims "no points are awarded for research or the recruitment of units", which contradicts widely held community expectation about unit and wall values; the claim is marked single-source and must be re-verified before any number enters a specification.

**(b) A corrected premise (`11A-BM-043`).** Tribal Wars **has no culture-point or World Wonder victory** — four targeted queries produced no Tribal Wars source, and the mechanic belongs to **Travian** (§9.4). The lawful non-military win paths evidenced in this study are therefore **Travian's** wonder race and **Tribal Wars'** own points/Casual endgames, not a Tribal Wars culture track. This is reported because the Prompt 11A brief's §11 candidate list anticipated otherwise, and a corrected premise is worth more than a convenient one.

**(c) Persistence is declared per mode (`11A-BM-045`).** "Hall of Fame **persists** in Normal/Casual but **resets** in Classic/Special/Speed", with a longevity escape valve on Casual: transfer to a fresh world after village loss or two weeks idle. **Lesson:** persistence must be a **property of each competitive object**, announced in advance (`11A-DR-013`). The forced-transfer device is a *retention* answer, and ours is `D-028`/`ONB-042` (return ends dormancy, shield until first boundary), which achieves the same without relocation.

**(d) Ratio-gated protection (`11A-BM-046`).** "Other players can't attack you at all, **or**; attacks are blocked when the attacker is much stronger (e.g. **20:1 point ratio**)" — a power-ratio veto computed from the **same abstract points number** used for ranking. Three comparator games converge on relative-band gating (Tribal Wars ratio, P&W 15–65 % treasure band, Supremacy 1914 percentage-of-pool), so the shape is adopted (`11A-DR-003`) **with the coupling rejected**: eligibility must read its own measure, and ratio gates invite deliberate score stunting (`11A-RK-016`).

**(e) Registration lock as a decider state (`11A-BM-044`).** A community-reported "once a tribe reaches 55 % dominance, the world will automatically **close to registrations**" — the pattern (a threshold closes *new entry* before it ends the competition) is adopted for seasonal eligibility (`11A-DR-021`); the specific figure is a single 2013 post and is **not** relied upon.

**Gaps honestly recorded:** no official article exists for rankings hierarchy, snapshot frequency or historical archives — a targeted search returned no results; medals and lifetime stats as named systems were not evidenced; concrete anti-farming mechanics were absent from the FAQ, while an **official tutorial video titled "Who to Farm"** exists, meaning farming is *taught* rather than *prohibited*.

---

## 12. Domain A — world events research

### 12.1 Event taxonomy

The seven category families proposed in Prompt 11A §12.1 were each tested against comparator evidence and against Nation Supremacy's fixed structure. **A, C, E and F are adopted; B is adopted only in a non-territorial form; D is adopted in a narrow, validated form; and one family the brief did not propose — calendar-deterministic state changes — is added because the evidence supports it as the cheapest lawful class.**

**A. Global events — adopted, with a caution.** Genuine world-wide events exist in every benchmark, but the honest observation is that most are *parameters changing*, not *stories happening*: Supremacy 1914's colour-bloc-equivalent bonuses derive from world averages, Politics & War's colour-turn bonus is capped by "(Average daily monetary revenue × 18 / Total Nations)" (`11A-BM-018`), and its commodity prices and radiation index are global aggregates published as world state (`11A-RS-024`, `11A-RS-026`). **Recommendation:** global events should be expressed as **published modifiers on shared parameters with a stated window and a stated derivation**, not as scripted narratives. This keeps them inside `ECN-215` (a world event "may change a price, a population or a resource stock **only through a published rule and a ledger event**") and `DMP-266` (event effects applied once, keyed, digest-visible). The caution: a global modifier that changes every nation's income simultaneously interacts with `ECN-111`'s conservation identity, so each one needs an explicit funding statement.

**B. Regional or group events — adopted only as non-territorial grouping.** Every comparator's "region" is geographic (Politics & War continents, Supremacy 1914 provinces, Call of War regions, Travian's map) and is excluded by `AP-002`. But two comparators supply **non-geographic** groupings, and they are the useful ones: Politics & War's **Colour Trade Blocs**, which are chosen, alliance-aligned and carry a competition bonus from which beige/grey/vacation/unallied nations are **excluded by rule** (`11A-BM-018`); and NationStates' **regions**, which are pure player-selected **lists of nations with no adjacency at all** (`11A-BM-071` region evidence). Nation Supremacy's only lawful group is the **Alliance**, so a group event must be Alliance-scoped, honour-only, aggregate at k ≥ 5, and must not make membership necessary (`AP-004`, `ALL-224`, `ALL-156`). **Explicit rejection:** the NationStates region object itself, and any "community-based event" that would function as a second grouping institution — that would be an Alliance redesign, which is not authorised here.

**C. National events — adopted, and this is the richest lawful class.** The comparators show domestic events generated from a nation's own state, without any author: NationStates' five issue trigger classes — random, **population-gated**, **prior-decision-chained**, **statistic-gated** and membership-gated (`11A-BM-069`, `11A-BM-058`); Politics & War's milestone national projects with prerequisite chains (`11A-BM-016`); and Tribal Wars' development-derived points (`11A-BM-042`). **Recommendation:** national events are generated by evaluating **published thresholds over owning-subsystem state** — cities founded, infrastructure totals, research completed, population bands, stability entering or leaving a state, a treaty signed, a campaign ended. This is the class with the fewest fairness hazards because the trigger is the nation's own history, no other nation is required, and the effect is informational or recognition-bearing rather than redistributive.

**D. Player-triggered events — adopted narrowly, with three mandatory controls.** Only one comparator has a working player-initiated event object: Politics & War's **bounties** — anonymously posted, funds forfeited immediately on posting, paid to the **first** nation to defeat the named target in the named war type, minimum $1,000,000, **no self-claim**, **no cancellation and no refund**, and deferral rather than forfeiture if the claimant is blockaded (`11A-BM-015`). Two properties are directly adoptable: reservation at creation, matching `TR-067`, and the explicit no-self-claim rule. One is a defect: an unclaimable posting locks value forever. The third control the evidence forces is counterparty independence — Politics & War had to write a specific rule against **bounty coordination** (`11A-RS-001`), which proves the laundering risk is not theoretical. **Also adopted from a different direction:** Politics & War's **pumpkin contest**, where players author content and the population votes in-game (`11A-RS-010`) — the *voting* is lawful in-game action; the forum submission channel is not in scope for us, and no chat or upload surface may be assumed (§16.11 and the Prompt 13 no-chat boundary).

**E. System-triggered events — adopted as the default class.** This is what nearly every benchmark actually does, and it is the only class that satisfies `AP-003` without argument: treasure respawn timers, colour-bonus recomputation, lottery draws, milestone project unlocks, dormant-state reassignment. The strongest design precedent is that the trigger is **state plus time**, both of which our engine already produces at every boundary (`TR-040`).

**F. Seasonal and annual events — adopted for recognition, deferred for structure.** Comparators show annual recurrence working (Politics & War's Easter and Halloween events with per-year closed achievement sets, `11A-BM-012`; Travian's annual tournament, `11A-BM-061`/`11A-BM-062`; Supremacy 1914's three-month seasons, `11A-BM-030`). But **Stage 1 already rejected round/age resets**: **FO-024** is recorded as *Rejected* — "N/A — conflicts with persistence" — and **FO-020 (seasonality/events calendar)** remains *Deferred*. Nation Supremacy has **one persistent shared world**, so a "season" cannot be an instance. The lawful form is an **in-place seasonal window**: a named period with its own ladder and honours, which resets the ladder and **never** the record (§15.4, `11A-DR-013`, `11A-DR-018`).

**G. Calendar-deterministic state changes — added.** Recurring scheduled rule-instant events are the cheapest class in the study and appear everywhere: Politics & War's monthly donation-limit reset (`11A-BM-007`), its weekly lottery at a published Sunday instant (`11A-BM-013`), Travian's weekly medals "every Monday at 00:00 (server time)" (`11A-BM-061`), eRepublik's three fixed election days (`11A-BM-050`), and NationStates' 27 government categories recomputing against fixed thresholds. Their defining virtue for us is **predictability without authorship**: a player can derive the event entirely from a published rule, and the operator never has to write anything. The design test adopted is: *can a player predict both the occurrence and the effect from published rules alone?* (`11A-DR-003`).

### 12.2 Event lifecycle

The fifteen lifecycle stages in Prompt 11A §12.2 map onto B-02's existing machinery, and the mapping is the most useful output of this section because it shows how little new machinery is required.

| # | Stage | System or player | Existing mechanism that owns it |
|---|---|---|---|
| 1 | Eligibility | **System** | B-03 protection/dormancy/pair states (`ONB-023`/`ONB-024`/`ONB-025`, `D-028`, `NET-025`…`NET-029`); relative band (`11A-BM-014`) |
| 2 | Creation | **System**, from published rules | P6 evaluation (`TR-040`); no scheduler of its own |
| 3 | Validation | **System** | P2 re-validation discipline (`TR-050`…`TR-054`); fail closed |
| 4 | Scheduling | **System** | Slot arithmetic and half-open windows (`TR-024`…`TR-027`); turn-count durations only (`11A-CR-026`) |
| 5 | Announcement | **System**, into the bounded digest | `TR-088` item 6 ("world events visible to the nation"), `TR-089` one bounded row |
| 6 | Activation | **System** at a boundary | `TR-028`/`TR-029` boundary semantics |
| 7 | Participation | **Player**, explicitly | `D-014` sovereignty; `REQ-523` silence is never consent — **no auto-acceptance** |
| 8 | Progress tracking | **System**, keyed | `ECN-155` deterministic event keys; `TR-073` G2 no double grant |
| 9 | Event updates | **System**, as appended records | `TR-090` history classes; `TR-091` corrections are appended events |
| 10 | Completion | **System**, evaluated at the snapshot | `TR-041` "rankings describe the turn that happened" |
| 11 | **Expiry** | **System**, at a named boundary | Comparators do this two ways: hard destroy (Travian, inadmissible) or **two-stage teardown** (Politics & War's eggs at one day-change, leftovers removed a week later — adopted, `11A-DR-004`) |
| 12 | Reward eligibility | **System**, with state re-check | `TR-052` eligibility re-checked at P2; deferred rather than voided when a state blocks collection |
| 13 | Reward distribution | **System**, ledgered | `ECN-113`/`ECN-165` keyed `REWARD` event; conservation re-checked at P7 |
| 14 | Historical record | **System**, P-class append-only | `TR-090`; `WAR-147` campaign records already permanent |
| 15 | Review and reporting | **Player-facing aggregate + Prompt 12** | `TR-092` compaction; `11A-RS-025`'s completion-percentage model as the review surface |

**The one ordering decision B-02 delegated to Prompt 11 is therefore answered:** within P6, **resolve in-flight event state → evaluate objectives → take the ranking snapshot → write chronicle records → release any deferred claims**, and publish all of it at P7. This is `11A-DR-002`, and it discharges the open row in `TR-042` plus the "Fixed evaluation order declared by Prompt 11" requirement in `TR-044` band B4. It is a *research-level recommendation*; 11B must write it as a rule, because only the owning document may.

### 12.3 Event governance

| Question | Evidence-based answer | Governing rule |
|---|---|---|
| Who may create an event? | The **system**, from published rules. A player may create a *challenge* object, never a world event | `AP-003`; `11A-CR-001`, `11A-CR-008` |
| May the system generate events automatically? | Yes — this is the default, and the only class that survives the one-person-team test | `AP-003`; `TR-040` P6 |
| May players nominate an event? | As a **recorded request**, yes; as an automatic effect, no | `D-014` sovereignty; NationStates' player-idea pipeline is gated by its staff, not automated (`11A-BM-070` news/dispatch evidence) |
| Randomised or deterministic? | **Deterministic**, except a bounded seeded selection with published odds, which `TR-044` B2 and `WAR-074` already sanction | `TR-044`, `TR-047`, `TR-048` |
| How is fairness maintained? | Relative-band eligibility; **participation freeze before the deciding boundary**; published timers; exclusion of protected and dormant nations from hostile effects | `11A-DR-003`, `11A-DR-006`, `ONB-025` |
| May one player repeatedly trigger an event? | Not through volume: per-window occurrence caps, asymmetric receive/give limits, and a real cost per interaction, all three of which Politics & War's Halloween event demonstrates working | `11A-BM-011`, `11A-DR-005` |
| What if an event becomes invalid? | Fail closed; write a disclosed record; **never** silently delete a grant already earned | `TR-056`, `TR-091` |
| What if a nation becomes protected mid-event? | Non-hostile participation continues; hostile involvement is blocked at validation and **progress is not confiscated** | `ONB-023`/`ONB-024`/`ONB-025`, `D-028` |
| What if a nation becomes inactive? | Excluded from public standings as presentation; **loses nothing**; queued effects continue | `D-028`, `ONB-039`…`ONB-041` |
| How are incomplete events handled? | Two-stage teardown honours in-flight work, then cleans residuals at a later boundary | `11A-BM-012`, `11A-DR-004` |
| How are rewards protected from duplication? | One canonical keyed identity; first-in-B4-order wins and later claims deduplicate | `TR-055`, `TR-073` G2, `ECN-155` |
| Is there a chronicle quality bar? | **Open** — `UD-024` is *Deferred to Prompt 11*; §14.6 proposes the direction and 11B must state the bar | `UD-024` |

### 12.4 Event timing

**Evaluation against a two-hour, twelve-turn-per-day world.** Frequencies observed in the comparators, converted to our cadence: per-turn (nothing sane does this), hourly (Supremacy 1914's combat tick — faster than our turn and therefore a warning), **daily** (Travian quests reset and Politics & War award reassignment; = **12 turns** for us), **weekly** (Travian medals at a fixed Monday instant; Politics & War's lottery; = **84 turns**), **60-day cycles** (Politics & War treasures), monthly (donation reset; eRepublik's three election dates), seasonal/quarterly (Supremacy 1914's three-month seasons), and annual (Politics & War's Easter and Halloween; Travian's tournament).

**Assessment.** Daily is the dangerous frequency for us, because every daily comparator mechanic examined is either a presence reward (barred by `TR-085`) or a forfeit-if-absent timer (barred by `D-028`). **A daily *generation* cadence is acceptable; a daily *obligation* is not** — the distinction is whether the player who does nothing that day loses anything. Weekly is the sweet spot the evidence supports: Travian's weekly medal snapshot gives a meaningful competitive window without demanding attendance, and an 84-turn window is long enough to survive a weekend of absence and short enough for a returning player to recognise.

**Recommended frequency band, and the fatigue control.** The concrete answer to notification fatigue is not "fewer events" but three mechanisms that comparators each proved separately: **a bounded outstanding queue** (NationStates' five-issue cap, `11A-BM-069`), **a single bounded digest row per nation-turn** (already mandatory under `TR-089`), and **player-adjustable cadence** (NationStates' 6/12/24/48-hour throttle, `11A-BM-058`). Together they let event *generation* stay frequent while the player's *experience* of it stays chosen. **No synchronous real-time window may be a foundation** (`AP-007`), so every window must be expressible as a turn count or a named boundary — the format Politics & War itself uses ("until after day change on Nov 8"). Seasonal periods must be long enough to be meaningful at a two-hour cadence; the specific lengths are Prompt 14 parameters (`11A-DR-005`, `11A-CR-026`).

### 12.5 Event design recommendation

A four-class taxonomy, one evaluation point, and one shared machinery:

1. **Calendar events** — deterministic, published in advance, derived from world aggregates; the default class.
2. **State events** — generated from a nation's own published state (national events) or from world state (relative-band selection, rotating objects).
3. **Challenge events** — player-initiated, reservation-backed, expiring, counterparty-independent.
4. **Commemorative events** — one-time world-state anchors that create permanent honours (the "when the world passed X" pattern, `11A-BM-009`), which cost nothing to run and produce the most durable recognition in the study.

Each is a **row over shared machinery** — trigger class, scope, eligibility band, duration in turns, effect class, reward class, teardown rule — exactly the parameter-tuple model Supremacy 1914 and Call of War use for their scenario variants (`11A-BM-032`, `11A-BM-038`). That is what makes the recommendation survive the `AP-003` test: adding an event means adding a row, not writing a feature. Recommendations `11A-DR-001`…`11A-DR-007`, candidates `11A-CR-001`…`11A-CR-008`.

---

## 13. Domain B — objectives and challenges research

### 13.1 Objective categories

The sixteen categories proposed in §13.1 were assessed for evidence, legality under our rules, and whether they create a goal or merely a task. **Verdicts: 11 adopt, 2 adopt conditionally, 3 reject or defer.**

| # | Category | Verdict | Basis |
|---|---|---|---|
| 1 | New-player onboarding | **Belongs to B-03, not B-11** | `REQ-089` and the ten-step journey already exist; B-03 `NAT-046` forbids first-login/first-trade/first-victory **rewards**. 11 may add *optional* goals after the journey, never gate it |
| 2 | Economic | **Adopt** | Output, treasury, resilience and production-mix measures exist in B-04 state; `ECN-108`/`ECN-109` permit wealth as a labelled estimate |
| 3 | National development | **Adopt — the strongest lawful class** | Tribal Wars' points-from-completed-buildings (`11A-BM-042`); B-05's catalogue, 12-city bound, 12 technologies and four capstones give ready-made tiers (`URB-031`, `URB-102`, `URB-107`); `URB-128` offers descriptive life phases already labelled "not enforced" |
| 4 | Political | **Adopt with a rewritten target** | `DMP-051` bars approval as a criterion and `DMP-042` there is no welfare index, so "good governance" cannot be measured. What *is* measurable: holding an election to term, surviving a crisis cycle, policy continuity, institutional completion. eRepublik and NationStates both show political participation sustaining a career with no personal stat at all |
| 5 | Diplomatic | **Adopt, positive-only** | `DIP-088` permits published counts with no mechanical effect. Objective conditions must be **positive** (an agreement concluded, a consultation honoured), never "break a treaty to test something" |
| 6 | Trade | **Defer behind the gate** | No trade statistic may be published before G-1…G-6 (`MKT-072`); volume-shaped objectives also create the circular-trade surface (`11A-RK-010`). Design may proceed; publication may not |
| 7 | Population | **Adopt as a statistic, not a target to maximise** | `DMP-025` sets a floor and `DMP-040` forbids eviction; growth is basis-point driven with four inputs, so a "grow to N" objective must be read as a housing-and-capacity objective, not a headcount race |
| 8 | Infrastructure | **Adopt** | B-05 gives integer bounds, costs and a permanent floor; `URB-040`'s explicit "no **event**" clause means development cannot be attacked through an event, so development goals are safe to state |
| 9 | Military (offensive) | **Reject as an objective; adopt as a record** | `AP-005`, `REQ-063`, the four inherited attack blocks, and Politics & War's documented farm-the-tutorial-nation behaviour (`11A-BM-010`) all point the same way. Campaign participation is *recorded* by `WAR-147`; that record is enough |
| 10 | Defensive | **Adopt — the evidence-backed military alternative** | Travian's separate **Defenders** and **PvE** medal categories, with the official statement that PvE kills do not feed the attacker ranking (`11A-BM-064`), show category separation working in production |
| 11 | Alliance participation | **Adopt, honour-only** | `ALL-224` forbids prize funding from alliance value; `AP-004` requires an individual equivalent; `ALL-156`/`D-027` bound what may be published |
| 12 | World-event | **Adopt** | Politics & War's event achievements with tiered conditions (`11A-BM-011`) and Travian's tiered missions with partial credit (`11A-BM-062`) are the two working models |
| 13 | Long-term national | **Adopt** | `11A-BM-016` (project chains), `11A-BM-063` (a long terminal cooperative accomplishment), `11A-BM-067` (authorship unlocks) |
| 14 | Seasonal challenges | **Adopt** | `11A-BM-030` (equal-start seasonal ladder), `11A-BM-061` (windowed medals) |
| 15 | Historical achievements | **Adopt as honours, not tasks** | `11A-BM-009`: closed eligibility, permanent, zero mechanical weight, twelve years live |
| 16 | Community participation | **Conditional** | Legitimate only where the activity is already an in-game action; the Prompt 13 no-chat/no-integration boundary and the absence of any upload surface exclude the NationStates dispatch and Politics & War forum-contest forms |

**Independence, exclusion, sequence and optionality.** The evidence is one-sided: **sequential is for teaching, optional is for everything else.** Politics & War's forced sequence compelled alliance membership and military stockpiling (`11A-BM-004`), while NationStates keeps a bounded queue with free dismissal (`11A-BM-069`) and Travian's mission tiers award partial credit without gating later content (`11A-BM-062`). Recommended posture: **one** sequential path, which is B-03's existing journey and is not re-opened here; everything else **optional, parallel, non-exclusive**, with tiers. Mutual exclusion should be reserved for genuinely rival specialisations, which is what B-06's two policy axes already provide — and note `AP-005`'s own test ("Which path gives the fastest returns? If it's one, revise") implies the objective set must be *audited for dominance*, which is a Prompt 14 check, not a Prompt 11 assertion (`11A-DR-024`).

### 13.2 Objective lifecycle

Twelve stages, and only one genuinely new object is needed. Creation (system, from a published condition set), availability (gated by B-03 states), eligibility (re-checked, never cached), activation (**explicit player acceptance** — no auto-enrolment, because `REQ-523` makes silence non-consent), progress tracking (keyed, per `ECN-155`'s deterministic key model), milestone completion (**partial credit**, per `11A-BM-062`'s tiers), final completion (once per key, first-in-order wins under `TR-055`), reward claim (**deferred, never voided**, per `D-028` and Politics & War's own escrow rule), expiry (**two-stage teardown**, per `11A-BM-012`), cancellation (system-initiated only, with an appended disclosed record under `TR-091`), repetition (**declared per objective**; the default is once, and a reroll cannot re-earn anything under `REQ-073`), and historical recording (P-class under `TR-090`).

Recommended lifecycle states, expressed in our existing action-lifecycle vocabulary (`TR-057`…`TR-062`) plus two additions Prompt 11B must formalise: `AVAILABLE`, `ACCEPTED`, `IN_PROGRESS`, `TIER_REACHED`, `COMPLETE`, `AWARDED`, `DEFERRED` (entitlement held, collection blocked by a state such as protection or dormancy), `EXPIRED` (with a grace variant distinct from forfeiture), `WITHDRAWN` (system-side, recorded) and `SUPERSEDED` (when the referenced mechanic changes — the direct mitigation for `11A-RK-024`).

### 13.3 Objective design principles

Nine principles survive both comparator evidence and our rules, and each is stated as a testable property rather than a taste.

1. **Every objective must be completable alone.** `AP-004`; the outline's "membership never mandatory"; and NationStates, which sustains an 18-year game with no objective system whatsoever (`11A-BM-073`).
2. **Choice, with a visible alternative.** Travian's rerollable random missions are the right *shape* and the wrong *mechanism* (pay-with-attention, `11A-BM-062`); the lawful version is a bounded offered set the player picks from, echoing NationStates' five-slot queue.
3. **Multiple paths, no cross-path entry fee.** eRepublik's level-9/level-15 gates make its four careers semi-parallel at best (`11A-BM-048`); ours must not repeat that.
4. **Difficulty as scope, not as grind.** Travian's geometric doubling thresholds (`11A-BM-066`) give an unbounded ladder without inventing new tiers; the escalating *reward per repeat* is rejected as a snowball.
5. **Three horizons.** Comparators show short (daily/weekly), medium (a season or a project chain) and permanent (honours, chronicle); an objective set with only one horizon is the failure mode.
6. **Transparent conditions referencing subsystem state.** `AP-006`; `11A-CR-010`; and the counter-example of NationStates' own FAQ admitting players cannot explain context-dependent effects.
7. **Fair rewards that do not compound.** `ECN-113` in full; recognition-first as the default.
8. **Anti-exploit validation at design time, not detection time.** Every hostile or volume-based condition must be checked against `REQ-063`'s "a blocked attempt moves nothing".
9. **Accessibility and honesty.** `REQ-094` (messages state the outcome and the next step, no private data, no enumeration risk); Politics & War's own seizure and escrow rules show that stating a rule plainly is cheaper than patching an expectation.

### 13.4 Avoiding harmful objective design

| Harm | Comparator evidence | Our binding constraint | Verdict |
|---|---|---|---|
| Mandatory daily logins | P&W daily login bonus; Travian "collect before reset, otherwise lost"; Supremacy 1914 "Daily Login" mission; eRepublik daily energy loop | `TR-085`, `TR-006`/`TR-007`, `D-028` | **Barred structurally**, not by tuning. Even deferred claims must never expire because of absence |
| Excessive repetition | Travian's ten-task day; P&W's 26-step list; eRepublik's grind-or-pay testimony | `AP-001`; `TR-089` | Cap outstanding content; prefer state-triggered recognition (`11A-BM-068`) |
| Objectives encouraging pointless warfare | P&W war slot filling, explicitly a rule violation with a 2-year expiry; the tutorial-nation farm | `REQ-063`, four attack-prevention layers, `AP-005` | **No offensive objective.** Records only |
| Rewarding attacks on protected or weaker nations | P&W bounties/treasures on the eligible band; Travian's official "top 200–300 population" self-help advice | `ONB-023`/`ONB-024`, `D-028`, `REQ-090` | Eligibility must exclude protected targets; safety must never depend on development level |
| Forced alliance membership | P&W objective #16 | `AP-004`, outline validation line | Individual equivalent mandatory for every collective objective |
| Requiring real money | P&W paid anniversary packages as achievements; eRepublik premium-priced rights; Supremacy 1914 Battle Pass lanes | `NAT-045`, `ECN-092`, ₹0 constraint, `REQ-073` | **Absolutely barred**, including any purchasable skip, boost or reroll |
| Unfairness to inactive players | P&W's 31/60/90-day deletion ladder; Supremacy 1914's inactivity penalty; Travian's lost rewards | `D-028`, `ONB-041`, `ONB-046`, `ONB-047`, `REQ-091` | Exclusion-as-presentation is our answer; no penalty may attach |
| Rewarding exploitative trading | eRepublik shell-company risk; P&W same-network trade restrictions and the alliance-bank evasion rule | `REQ-063`, `MKT` pair blocks, gate dark | Deferred behind the gate; volume metrics rejected in favour of ratio/relationship shapes |
| Duplicate completion | Every comparator's weak point; P&W solved by an achievement key (`TR-073` G2) | `TR-055`, `ECN-155` | One key per completion, tested |
| Conflict with protection or diplomacy | P&W's war/treaty abuse rules exist because the abuse was real | `REQ-516`, `REQ-523`, `DP-T01`, `ALL-206`/`ALL-209` | Positive-only conditions; every hostile path validated |

### 13.5 Objective reward research

Comparator reward types, ranked against what Nation Supremacy may lawfully do: **recognition** (universal, unproblematic, and the only thing Supremacy 1914's ordinary-round winner gets — "Winning a normal Travian: Legends server does not provide a prize or medal" is the same posture (`11A-BM-062`)); **badges with published completion rates** (P&W's achievement page, `11A-RS-025`, which is the best realisation in the study); **profile cosmetics and authorship unlocks** (NationStates' postcards and population-gated identity fields, `11A-BM-067`/`11A-BM-068` — the highest-value transfer in this domain, because authorship cannot compound); **historical records** (`TR-090` already provides the class); **prestige** (blocked as a currency by `ECN-092`, available only as an honour count); **small economic rewards** (permitted only as "rare, disclosed, system-generated event adjustments" under `ECN-013(c)`, and never as a yield multiplier under `ECN-113`); and **progression unlocks** (admissible only for non-power options, per `URB-158`'s explicit bar on granting cities, facilities, capacity or technologies without a decision and a register row).

**Reward inflation, compounding and pay-to-win.** The inflation mechanism is visible in three comparators at once: Travian's escalating repeat rewards, P&W's 5–9 %-per-treasure stackable income bonuses, and eRepublik's rank-up-grants-more-capacity loop. Our three independent guards are `ECN-113` (no permanent yield multiplier), `URB-101` (no compounding percentage yields) and `TR-085` (no presence income). **Recommended default hierarchy: recognition → record → authorship → (rarely, disclosed, keyed) material.** No amount is chosen here (§23).

---

## 14. Domain C — rankings and competitive recognition research

### 14.1 Ranking categories, assessed against what our subsystems actually expose

| Category | Constructible? | Permitted inputs | Blocking rule |
|---|---|---|---|
| **National development** | **Yes — the strongest** | City count, infrastructure totals, facility counts, research completions, capstones; `URB-128`'s descriptive phases | `URB-158`: may be *shown*, never a purchasable score |
| **Economic performance** | **Yes, with two labels** | Output, production mix, treasury movement, capacity utilisation; wealth as a labelled estimate | `ECN-108`/`ECN-109` (not money, not spendable); `ECN-215` (label it an estimate) |
| **Economic stability / resilience** | **Yes** | Shortfall and austerity events, deficit durations, reserve depth — all already recorded by B-04 | Must read ledger facts, not a new state |
| **Political performance** | **Only after redesign** | Election completion, crisis survival, institutional continuity, policy consistency | `DMP-051` bars approval as a criterion; `DMP-042` there is no welfare index → `11A-OPEN-007` |
| **Population and domestic development** | **Partly** | Population and housing as **statistics** | `DMP-051`; "public welfare" is not constructible at all |
| **Military performance** | **Bands and counts only** | Participation, repelled actions, bounded campaign outcomes, discipline (no rule violation recorded) | `WAR-162` no exact readiness/force/inventory public; `D-027` k ≥ 5; `WAR-147` gives B-11 the receipt rule |
| **Diplomatic performance** | **Counts only** | Agreements concluded, treaties honoured, consultation notices issued, breach counts | `DIP-084` no reputation value; `DIP-088` counts have no mechanical effect |
| **Alliance performance** | **Aggregates only** | Collective development, member participation counts, contribution aggregates ≥ k | `ALL-156`, `D-027`, `ALL-224` (no prizes), `AX-18` (no military command) |

The recurring lesson across all eight is that a **standing may expose a published fact and must not create a new value.** That is precisely the distinction B-08 already encodes — a breach count is displayed and inert — and it is what makes a multi-dimensional ranking safe here where Politics & War's single score is not.

### 14.2 Ranking methodology

| Method | Evidence | Verdict |
|---|---|---|
| **Raw totals** | P&W boards (`11A-BM-002`), Travian points (`11A-BM-042`) | Legible and cheap; **age-biased by construction**, so always pair with a window |
| **Ratios** | P&W GDP per capita; Tribal Wars' 20:1 protection ratio | Good for fairness across sizes; denominator gaming risk (`11A-RK-016`) |
| **Rates** | Nothing measures rate directly; Supremacy 1914's Growth Bonus is the closest (`11A-BM-018`) | **The strongest anti-snowball device available**, and no comparator implements it well. Recommended as a first-class addition (`11A-DR-019`) |
| **Weighted composites** | P&W score | Rejected as *the* measure; permitted only as a labelled, non-eligibility index (`11A-DR-010`) |
| **Percentiles** | P&W "#55 of 11,958 (0.46%)"; NationStates "Rank 171,969th (Top 100%)" | Adopted as the **default presentation**; makes a small world and a large world comparable |
| **Median-relative description** | NationStates World Census (`11A-BM-054`) | Adopted for the **descriptive layer only**, with no reward — the study's cleanest separation of "measured" from "winning" |
| **Time-windowed performance** | Travian weekly medals; Supremacy 1914 seasonal points | Adopted as the primary competitive basis |
| **Snapshots** | Every comparator; best practice is a published instant | Adopted (`11A-DR-006`) |
| **Historical archives** | P&W permanent badges; Supremacy 1914 Hall of Fame (promised); Travian Hall of Fame persisting per world type | Adopted subject to `TR-092` |
| **Normalised pool (percent of total)** | Supremacy 1914's `2000 × player count` | Adopted for any threshold semantics (`11A-DR-019`) |

**No weights are chosen here** — the brief reserves them for 11B and Prompt 14, and the register rule that a design decision "settles the rule but does not approve the requirement" applies.

### 14.3 Fairness and eligibility

Sixteen named fairness concerns were tested; the resolution for each either already exists in an accepted rule or becomes a recommendation.

New-player disadvantage is handled by **windowed measures plus rate measures** rather than by assistance, because `D-021` and `NAT-045` forbid assistance and age differentials. Nation age is displayable and commemoratable, never ranked as merit (`11A-BM-019`). Inactive nations are excluded as presentation under `D-028`, which also answers "inactive leaderboard domination" without decay. Protected nations appear in non-hostile standings under `ONB-025`, and a **new nation is unranked until its first completed boundary** under `NAT-016` — a rule this report adopts unchanged and which also fixes the "immediate rank manipulation" question, since there is nothing to manipulate in the first turn. Seasonal resets must reset ladders only (§15.4). Score manipulation is met by the participation freeze and by refusing instantaneous-total rewards. Multi-account exploitation is bounded by `D-032`, `REQ-061`, the pair model and `REQ-066` (IP alone is never sufficient) — and the anti-pattern to avoid is Travian's official statement that "duals and sitters" activity counts to the owner (`11A-BM-062`). Alliance collusion is bounded by `ALL-224`, `ALL-156` and Prompt 12. Strategic inactivity needs no new rule because dormancy exclusion already removes the domination. Repeated low-risk farming is addressed by excluding cheap repeatable actions from scored sources — Travian's infantry exclusion and the PvE/attacker separation are the working precedents (`11A-BM-061`, `11A-BM-064`). Public-statistic privacy is entirely governed by `D-027`. **Reroll interaction is resolved by B-03, not by us**: `RRL-013` removes current rank and progression counters while historical snapshots remain, and `REQ-085` requires that cleanup be deterministic. Finally, **denominator disclosure** is added as a requirement because the study found two different nation populations in one game (11,958 versus 14,630) — every percentage we publish must state its population and window (`11A-CR-015`).

### 14.4 Ranking snapshots

Real-time calculation is the one option the evidence rejects: it maximises both manipulation surface and cost. The comparator spread is informative — Politics & War reassigned awards **daily immediately before the update**, Travian snapshots **weekly at a fixed instant**, Supremacy 1914 publishes daily while evaluating continuously (a deliberate two-clock split), and Tribal Wars recalculates on completion but "sometimes the recalculation can be **delayed to reduce server load**".

**Recommendation.** One authoritative snapshot per turn, taken in P6 after P5 completes and published at P7 — which is exactly what `TR-041` already reasons ("world evaluation last means **rankings describe the turn that happened**"). Weekly, monthly and seasonal standings are then **derived from the archived turn snapshots**, not computed separately, so no second truth can exist. Three constraints follow. Publication is at P7 only (`TR-038`). A **participation freeze** applies to anything a standing decides, per Supremacy 1914's pre-draw rule (`11A-DR-006`). And cost is bounded by `TR-092`'s retention model plus the fact that compaction is "an idempotent daily job, **not a turn phase**", so historical queries must never become turn work. The concrete intervals (daily/weekly/monthly/seasonal) are Prompt 14 parameters (`11A-DR-019`).

### 14.5 Tie-breaking

The brief's rule — never rely on an arbitrary or hidden tie-break — is tested by exactly one bad example and two good ones. **Bad:** Politics & War's documented "in any instance where there is a tie, the award is configured to go to [the developer's] nation" (`11A-BM-008`), which is neither derivable from player-visible data nor defensible. **Good:** NationStates' delegate tie breaks to "the nation that has been in the region **longer**" — published, deterministic, derivable, though tenure-based and therefore inadmissible for us as a merit rule (`11A-BM-056`). **Good:** our own B-02, which already resolves contested indivisible allocations by a **seeded lottery keyed on `(turn_id, allocation_id)`**, forbids hidden ordering keys (`TR-045`) and requires that published ordering be player-readable (`TR-049`).

**Recommended hierarchy, to be formalised by 11B:** (1) **shared standing** by default, since a tie is information rather than an error; (2) where exactly one winner is structurally required, an **earlier sustained achievement** — whoever reached the position first in a published snapshot, which is auditable from the archive; (3) where a genuine contest must break, the **existing seeded selection**, with its seed published; (4) **never** operator identity, account age, insertion order or an undisclosed value. Ties observed on the live P&W board (two nations at 13,891.25 taking ranks 32 and 33) show the ordinal alternative produces silently arbitrary outcomes (`11A-BM-002`).

### 14.6 Historical rankings and the chronicle

Comparators establish four archive layers, each already available to us: **all-time totals** (P&W cumulative counters — with the casualty-merit warning attached), **seasonal standings** (Supremacy 1914, resetting each season with a promised Hall of Fame), **periodic recognition** (Travian's weekly medals, permanent once granted), and **records/milestones as history** (P&W's world-state badges, `11A-BM-009`). Nation Supremacy's storage classes are already assigned: `TR-090` makes "major world events, milestones" **P-class permanent append-only**, `TR-092` compacts operational history on a 30-day-then-monthly-summary schedule as a non-turn job, and `D-042` makes public nation history permanent.

**Recommended sustainable archive:** permanent **anchors** (event occurred, standing snapshot digest, honour granted, record set) plus **monthly rollups**, with full per-turn detail deliberately compacted. This is the only shape that satisfies both "should historical records be retained" and the free-tier storage reality measured in Stage 1 (≈264–291 bytes per nation-turn, a 500 MB free database described as a ~140-day budget without retention). **`UD-024` — "What quality bar does the world chronicle meet?" — is deferred to Prompt 11 and remains open**; §12.2 and this section give it a direction (notability = anything that created a permanent record, a standing change, or a closed-eligibility honour), but the bar itself is 11B's to state (`11A-DR-016`, `11A-OPEN-008`, `11A-OPEN-013`).

### 14.7 Privacy

`D-027` is the whole answer and is **not** re-thresholded here: at least five contributing members; otherwise merge into a stable "other" group only if the merged group is still ≥ 5, else **withhold or coarsen into a band**; complementary suppression so a total plus all-but-one component cannot reveal the remainder; and **no differencing across turns or across related tables**. `TR-020` adds a useful boundary that most comparators lack: "an individual nation's public ranking is **not** an aggregate", so a per-nation standing may publish an already-public national value while group statistics stay protected. `WAR-162` and `WAR-053h` then bar exact military values outright, `ECN-215` bars revealing private balances through a wealth ranking, `ALL-156` keeps member data inside the existing visibility classes, `DIP-089` forbids hidden account records, and `REQ-094` requires that player messages state an outcome without private data or enumeration risk.

**Four techniques, in the order they should be tried:** **aggregate** (only above k), **band** (readiness-style published bands, which B-10 already uses), **redact** (a standing exists but a component is withheld, with the withholding stated, never silent), and **delay** (publish a derived rollup after a fixed lag where a live value would identify a small group). Delay is the one genuinely new device this report adds, and its justification is comparative: Politics & War publishes a *daily* world newspaper yet no per-nation military value, and `TR-077`…`TR-080` already make visibility wait for a completed turn, so a lag is native to our model rather than bolted on (`11A-DR-016`, `11A-DR-019`).

---

## 15. Domain D — long-term national progression research

### 15.1 Progression dimensions

Thirteen candidate dimensions were tested. **Measurable development** — national age and continuity, economic development, infrastructure milestones, institutional maturity, population and welfare milestones, trade relationships, achievement history — is all derivable from owning-subsystem state plus the chronicle, which is the property `NAT-051` requires ("progression is chosen, not handed out"). **Commemorative recognition** — diplomatic reputation, military history, world-event participation, cultural and national identity — is partly available and partly blocked: military history exists as permanent campaign records (`WAR-147`) but is privacy-bounded (`WAR-162`); event participation is inherently recordable; **diplomatic "reputation" is not** (`DIP-084`), and neither is **cultural identity as a score**, because B-06 has no culture mechanic. Science and technology **is** supported — B-05's twelve technologies and four capstones are the one clean, already-owned progression spine — but `URB-092` fixes research points as a **non-tradable progression value**, which is a useful property rather than a limitation.

**The measurable/commemorative split is the load-bearing distinction**, and the comparators show what happens when it is collapsed: Politics & War's score is simultaneously a measurement, an eligibility gate and a leaderboard, which makes every tuning change a policy change (`11A-BM-001`). Nation Supremacy can hold the line because three separate rules already do the work: `NAT-052` (milestones grant no ranking weight), `DIP-088` (a published count with no mechanical effect) and `URB-158` (statistics may be shown, never sold).

### 15.2 Progression models compared

**Model A — Milestone-based.** *Evidence:* Tribal Wars' task thresholds double "unlimited… (doubling each time)" (`11A-BM-066`); P&W project chains (`11A-BM-016`). *Strengths:* legible, derivable, no new state. *Weaknesses:* thresholds are age-biased; a milestone ladder alone rewards only duration. *Exploits:* threshold-edge snapshot gaming. *Legality:* **fully admissible** under `NAT-052` provided milestones stay records.

**Model B — Achievement-based.** *Evidence:* P&W's keyed, dated achievements with published completion rates (`11A-RS-025`); event achievements with tiered conditions (`11A-BM-011`). *Strengths:* expresses diverse play styles; rarity becomes information. *Weaknesses:* P&W's catalogue shows how easily it degrades into attendance, purchase, employment and victim-requiring conditions. *Exploits:* duplicate claims; farming. *Legality:* admissible; `NAT-052` and `REQ-073` do the containment. **But note the honest counter-evidence:** NationStates runs 18 years with **no** achievement system (`11A-BM-073`), so this is optional, not mandatory.

**Model C — Prestige-based.** *Evidence:* P&W's VIP badge and paid packages; eRepublik's rank ladder. *Strengths:* a single accumulative social number is trivially legible. *Weaknesses:* every implementation studied converts status into advantage. *Exploits:* infinite prestige farming. *Legality:* **rejected as a numeric system** — `ECN-092` forbids a prestige currency at launch and `NAT-045` forbids purchasing standing. Admissible **only** as an honour count with no spend and no weight.

**Model D — Historical-record progression.** *Evidence:* P&W's live twelve-year-old badges including world-state anchors (`11A-BM-009`); `TR-090`'s P-class permanence; `WAR-147`'s permanent campaign record. *Strengths:* **cannot snowball, cannot be bought, cannot be farmed**, and gives a nation a continuity that survives every other reset. *Weaknesses:* fossilses for late joiners; retention cost. *Exploits:* identity laundering across rerolls — answered by `RRL-013`/`RRL-016`. *Legality:* the best-fitting model in the study.

**Model E — Seasonal progression.** *Evidence:* Supremacy 1914's SRP (equal start, symmetric gain/loss, quit and inactivity taxes, permanent unit unlocks) (`11A-BM-030`); Travian's windowed weekly medals (`11A-BM-061`). *Strengths:* solves veteran advantage by construction. *Weaknesses:* **FO-024 already rejected resets**, so no national state may reset; inactivity taxes conflict with `D-028`. *Exploits:* alt farming of a fresh ladder. *Legality:* admissible **for standings only**, never for records.

**Model F — Hybrid.** Every successful comparator is in fact hybrid: P&W runs score + boards + transient awards + permanent honours + achievements + milestones; Supremacy 1914 runs IoP + Victory Progress + SRP + account rank + heroes. **No studied game uses exactly one model, and no studied game's single-model component is uncontaminated.**

**Recommendation: F, with the components sharply separated** — Model D as the spine, Model A supplying its structure, Model B as a deliberately small optional layer, Model E confined to standings, and Model C rejected as a currency (`11A-DR-017`, `11A-DR-013`, `11A-DR-034`).

### 15.3 Avoiding progression inflation

| Inflation risk | Mechanism that creates it | Constraint that blocks it here |
|---|---|---|
| Excessive permanent bonuses | P&W treasure income 5–9 % each; Travian +25 % production rewards | `ECN-113` "may not be a permanent yield multiplier"; `URB-101` no compounding percentages |
| Snowball / runaway leader | Travian escalating repeat rewards; Supremacy 1914 daily leader-sustain bonus | `11A-DR-019` windowed **rates**; `ECN-190` bounded money growth |
| New-player disadvantage | Age-biased cumulative totals; eRepublik level gates | `NAT-045`, `D-021`, `INV-025` — **windows and rates, not assistance** |
| Infinite prestige farming | Any renewable honour source | `11A-DR-016` closed eligibility or a fixed window; `11A-RK-023` |
| Reward stacking | Multiple simultaneous grants for one completion | `TR-055`/`TR-073` G2 one key per completion |
| Economic reward inflation | Presence- or activity-linked currency | `ECN-013(c)` rare+disclosed only; `TR-085` |
| Military power creep | Recognition granting capability | `NAT-052`, `WAR-033`/`WAR-040` OP has exactly one lawful increase |
| Account-age advantage | Age-gated eligibility (`11A-BM-019`) | `NAT-045`; commemorated, never ranked |
| Inactive domination | Cumulative all-time boards | `D-028` exclusion; windowed standings |

**The structural answer to "how does progression stay meaningful without making old nations unbeatable"** is the one no comparator applies but all of them gesture at: **make the permanent layer non-comparative and the comparative layer non-permanent.** Records, honours and authorship accumulate forever and buy nothing; standings and seasons reset, compare, and grant no capability. Nation Supremacy is unusually well placed to do this because `NAT-052` already forbids milestone ranking weight, `DIP-088` already demonstrates the "displayed but inert" pattern, and `ECN-092` already refuses the prestige currency that would otherwise corrupt both layers.

### 15.4 Permanent versus seasonal

| Object | Persistence | Seasonal reset may affect it? | Rule |
|---|---|---|---|
| Permanent national history | Forever, append-only | **No** | `TR-090`, `REQ-071`, `REQ-093` |
| Permanent achievements and honours | Forever, nation-scoped | **No** (and reroll forfeits nation-scope ones) | `RRL-013`, `NAT-052` |
| Seasonal standings | One season | **Yes — that is their purpose** | `11A-BM-030` |
| Temporary objectives and challenges | Declared window | Yes, with a grace and no forfeiture | `D-028`, `ONB-041` |
| Event participation records | Forever | **No** | `TR-090` |
| Competitive awards | Transient holding of a standing; permanent record of having held it | Yes for the standing; **no for the record** | `11A-BM-008` vs `11A-BM-009` |
| Resettable challenge progress | Explicitly declared | Yes, only where declared in advance | `11A-DR-018` |

The brief's rule — a seasonal reset must never erase permanent national history without an explicit authorising rule — is **independently supported by Stage 1**, which already rejected age/round resets (**FO-024: "N/A — conflicts with persistence"**). Two comparator cautionaries reinforce it: Supremacy 1914 archives rounds then **deletes them two weeks after a round finishes** (`11A-BM-027`), and NationStates hard-reset its entire accumulated body of World Assembly law in 2026 (`11A-BM-070`) — the second shows that even an eighteen-year institution's accumulated continuity is one decision away from zero, which is precisely what a permanent record layer exists to prevent. **`11A-DR-013` and `11A-DR-018` adopt the separation; nothing in it is provisional** (`11A-DR-018`).

---

## 16. Player-type and gameplay-diversity analysis

The twelve profiles in Prompt 11A §17 are assessed against the recommended architecture. The controlling requirement is the brief's own: "The design must support **peaceful and non-military national development as meaningful progression paths**. Do not make military victory the only meaningful way to advance" — which `AP-005` states as a test ("Which path gives the fastest returns? If it's one, revise.").

| # | Profile | Meaningful goals available | Relevant events | Objective categories | How performance is recognised | Can progress without warfare? | Needs an Alliance? | Fairly limited? | Exploit / balance concern |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Economic developer** | Build output, mix, resilience, treasury depth | Calendar and state events; commodity-shock-class global modifiers | 2, 3, 6 (deferred), 8 | Development standing; rate-of-growth standing; milestones; descriptive census-style profile | **Yes** | No | No limitation | Snapshot-edge production timing (`11A-RK-002`); `ECN-113` bars the reward becoming yield |
| 2 | **Military strategist** | Campaign conduct, bounded outcomes, defensive skill | War-derived records via `WAR-147`; contested-slot events | 10 (defensive), 12, 14 | Participation records, defensive bands, campaign history | Yes, but warfare remains a legitimate path | Often, informally | No | **War slot filling**; loss inflation (`11A-RK-003`, `11A-RK-006`) |
| 3 | **Defensive nation** | Survive, repel, endure | Protection-aware events; siege-style challenge events | 10, 3, 7 | **Travian's model**: a separate Defender category, and a Survivor honour | **Yes — explicitly designed for** | No | No — this is the profile most comparators fail | Deliberate non-response to farm defensive credit (`11A-RK-017`) |
| 4 | **Diplomatic nation** | Conclude agreements, honour them, consult, mediate | Diplomatic milestones as world-event inputs | 5, 12, 16 | **Counts of published acts only** (`DIP-084`/`DIP-088`); treaty participation records | **Yes** | No | Partly limited: no reputation score may exist, so influence is social, not mechanical | Commendation rings (`11A-RK-011`); objectives pressuring breach |
| 5 | **Political player** | Hold office, complete cycles, sustain stability, keep a polity coherent | B-06's own published election calendar as a scheduled event class | 4, 13 | Cycle completion records, institutional continuity, crisis-survival records | **Yes** | No | Limited by design: `DMP-051` bars approval as a ladder, so political standing must be re-expressed (`11A-OPEN-007`) | Election-window manipulation; manufactured crisis (`11A-RK-013`) |
| 6 | **Trade-focused nation** | Volume is **not** available pre-gate; relationship breadth, counterparty diversity, market-making quality | Trade events deferred | 6 (**deferred**), 11 | Records now, statistics after the gate | **Yes** | No | **Yes — materially limited**, and this limitation is deliberate (`MKT-072`) | Circular volume inflation (`11A-RK-010`) |
| 7 | **Population and infrastructure developer** | Housing, capacity, city founding, capstones | State events on threshold crossings | 3, 7, 8 | **The best-served profile**: development standing, milestone tiers, capstone honours, authorship unlocks | **Yes** | No | No — and Tribal Wars' points model is precisely this profile's scoreboard | Wealth-ranking bias against research spend (`11A-OPEN-006`) |
| 8 | **Alliance contributor** | Collective goals, member participation, shared projects | Group-scope events, honour-only | 11, 12, 14 | Aggregates ≥ k; laurel-style alliance variants (Travian model); **no prizes** | Yes, and independently too | **Optional** | Must remain optional (`AP-004`) | Collusion and unattributed pooling (`11A-RK-007`, `11A-RK-011`) |
| 9 | **Independent nation** | Everything available to profiles 1, 3, 4, 5, 7 | Individual and national events | 2, 3, 4, 5, 7, 8, 10, 13 | Individual standings, honours, records, authorship | **Yes** | **No — a hard requirement** | At risk if any collective reward lacks an individual equivalent | Isolation-by-design if group bonuses dominate (`11A-DR-024`) |
| 10 | **Casual or returning player** | Short sessions; catch up through the digest | Windowed events with grace, never forfeiture | 3, 7, 12 (**never 1**) | Milestones and records accumulate without attendance | **Yes** | No | Protected by `D-028`, `TR-085`, `ONB-041` | The single largest design hazard: every comparator's casual-hostile mechanic is a presence or expiry rule |
| 11 | **Competitive leaderboard player** | Standings across several domains; seasonal ladders; contested objectives | Calendar and challenge events | 12, 14 | Snapshots, seasonal standings, sustained-position recognition | Yes — non-military boards exist | Often | No | Snapshot manipulation; tie games (`11A-RK-002`, `11A-RK-025`) |
| 12 | **Long-term historical player** | Accumulate a nation's story; complete long chains | Commemorative world-state events | 13, 15 | **The permanent layer is this profile's reward**: chronicle, honours, records, capstones | **Yes** | No | No | Fossilisation of closed-eligibility honours (`11A-BM-009`) |

**Verdict on the controlling requirement.** Peaceful progression is available on **seven** of the twelve profiles through development, defensive, political, diplomatic, infrastructural, historical and independent paths, and each is grounded in state an owning subsystem already publishes rather than in a new mechanic. The **two genuine limitations are trade (deferred behind the release gate) and political performance (blocked as an approval ranking)** — and both limitations are the result of accepted decisions rather than of this report's choices, so §24 records them as dependencies rather than resolving them silently. The architecture's decisive property is that **no layer feeds capability**: records buy nothing, honours weight nothing, and standings gate nothing, which is what allows twelve profiles to coexist without one dominating (`AP-005`) — and it is already B-03's own rule at `NAT-052`.

**One profile the comparators expose as a hazard rather than a success.** eRepublik's media/propaganda track (`11A-BM-052`) and Politics & War's advertisements surface are the closest analogues to a "narrator" player type. Nation Supremacy has **no supported surface for it**: Prompt 13 must not design chat or third-party messaging, and the digest is a bounded system surface (`TR-089`). Rather than leave that player unserved, the lawful outlet is the chronicle itself — the descriptive profile and the authorship unlocks of `11A-BM-067` give an expressive role to a player who wants to be recognised for who their nation *is* rather than what it did.

---

## 17. Cross-system integration analysis

The complete matrix, with all fifteen required fields per row across **40** integration findings, plus the **18**-row register of owning rules that a naive design would violate, is in [`11A_integration_and_risk_registers.md`](11A_integration_and_risk_registers.md) §2–§4. This section states the conclusion per subsystem so that no reader has to open the companion to understand the coupling.

### 17.1 B-02 — turn lifecycle

**Prompt 11 is already assigned a place in B-02, and it is exactly the right one.** `TR-040` fixes **P6 "World — Evaluate objectives, rankings, systemic events"** with owning prompt **11**, gives P3's recurring event ticks partly to 11, and shares P7's record writing and publication with 11. `TR-044` band **B4** requires a "Fixed evaluation order declared by Prompt 11"; `TR-055` already resolves concurrent reward claims in B4 order with achievement-key deduplication; `TR-013` lists **Objective**, **World event** and **Ranking/record** as vocabulary owned by Prompt 11; and `TR-096` names the decisions Prompt 11 must make. **No competing scheduler is proposed or permitted.** The one delegated open question — `TR-042`'s "Are world events generated before or after objective evaluation?" — is answered in §12.2, which closes it at research level and hands the rule to 11B. Duplicate prevention, replay and idempotency are inherited rather than reimplemented: `TR-016`/`TR-018` exactly-once, `TR-043`/`TR-048` checkpoint resume and replay determinism, `ECN-154`/`ECN-155` settlement and event keys. Rows `11A-INT-01`…`11A-INT-07`, `11A-INT-39`, `11A-INT-40`.

### 17.2 B-03 — protection and eligibility

Every eligibility question in the four domains resolves to B-03 rather than to Prompt 11: unranked until the first boundary (`NAT-016`), protected nations may join **non-offensive** events and appear in rankings (`ONB-025`), dormancy is exclusion-as-presentation with no loss (`D-028`), reroll removes current rank while history survives (`RRL-013`, `RRL-019`), first-time rewards are non-transferable and non-re-earnable (`NAT-046`, `REQ-073`), and **the achievement framework belongs to Prompt 11 while the milestone semantics belong to B-03** (`NAT-052`). No objective or event may bypass a protection, and no objective may be gated on presence. Rows `11A-INT-08`…`11A-INT-12`.

### 17.3 B-04 — economy and resources

Rewards are already fully governed: `ECN-113`'s five conditions (approved, keyed and non-repeatable, disclosed, ledgered, non-convertible) plus the ban on a permanent yield multiplier; `ECN-013(c)`'s "rare, disclosed, system-generated event adjustment" as the only lawful new-crown path; `ECN-165`'s existing `REWARD` ledger type, so no new ledger vocabulary is created; and `ECN-111`'s conservation identity, which Prompt 11's grants must not break. `ECN-108`/`ECN-109` permit wealth in a ranking **as a labelled estimate only**; `ECN-092` removes prestige currency from the option space entirely. Rows `11A-INT-13`…`11A-INT-16`.

### 17.4 B-05 — cities and infrastructure

Development recognition reads B-05's state and adds none of its own: the 12-city bound, the 10–500 infrastructure range with a floor that **explicitly names events** as unable to breach it (`URB-040`), permanent non-deletable cities (`URB-035`), the closed 17-type catalogue, twelve technologies, four capstone programmes and the four descriptive-but-unenforced life phases (`URB-128`) as ready milestone vocabulary. `URB-110` and `URB-158` permit a reward to grant crowns, resources, research points or a **one-time programme** only through a disclosed keyed ledgered event, and bar granting a city, facility, capacity, technology or yield multiplier without a decision and a register row. `URB-119`'s expensing of research against national wealth is recorded as an unresolved ranking bias (`11A-OPEN-006`). Rows `11A-INT-17`…`11A-INT-19`.

### 17.5 B-06 — population and domestic politics

The two most restrictive inputs in the study: `DMP-051` removes approval from the ranking and achievement-currency space, `DMP-042` removes welfare entirely, and `DMP-063` fixes constituency weights against variation by events. Event effects are permitted only through a **named event term** or the normal target-and-cap path (`DMP-141`), applied once, keyed, digest-visible, and never able to set a leadership state, resolve a contest or remove a leader (`DMP-266`). The election cycle is already a published, per-nation scheduled calendar with exactly-once contest identity, so the comparator lesson from eRepublik is confirming rather than new. **No objective may punish a political state for being one**, which is the direct answer to the brief's §16.5 warning about instability becoming an objective penalty. Rows `11A-INT-20`…`11A-INT-22`.

### 17.6 B-07 — trade and markets

The gate governs everything: `MKT-072`…`MKT-076` leave G-1, G-2, G-3, G-5 and G-6 **not met** and G-4 partial, the market is "dark until the gate passes", and no readiness claim may be made. **This report adds no claim and marks no gate satisfied.** Trade statistics may be *designed* and may not be *published*; volume-shaped objectives are the circular-trade surface (`11A-RK-010`). `D-122`, `DD-136` and `REQ-513` are preserved exactly as written. Rows `11A-INT-23`, V-09.

### 17.7 B-08 — diplomacy

`DIP-084` removes the temptation to build a reputation score, and `DIP-088` supplies the permitted alternative: displayed counts with no mechanical effect, "A player may use it; the game does not." `DIP-086` makes diplomatic history nation-scoped, which sets the honour scope for diplomatic recognition. `REQ-516` (posture changes only by the owner's action, never by decay) and `REQ-523` (silence is never consent) are the two rules that bound any diplomatic objective or event, and `DIP-091` keeps embargoes as the only sanction so no event may invent a new one. **No objective may reward breaking a valid agreement.** Rows `11A-INT-24`…`11A-INT-26`, V-07.

### 17.8 B-09 — alliances

Four prohibitions bind every alliance-facing design: no Alliance military command, no member OP spending, no Alliance military treasury, no shared pool (`AX-18`, `UD-047`, `UD-049`). `ALL-224` independently removes **prizes** from the possible funding, so alliance recognition must be honour-only — which the comparator evidence happens to support (Travian's alliance medals add laurels to the same ribbon, `11A-BM-061`). `ALL-156` keeps member and applicant data inside the existing visibility classes, so an alliance standing is aggregate-or-nothing under `D-027`. Membership change must neither credit nor debit a standing, and `AP-004` plus the outline's "membership never mandatory" require an individual equivalent for every collective objective. Rows `11A-INT-27`…`11A-INT-29`, V-03, V-04.

### 17.9 B-10 — warfare

**B-10 places the study's only positive obligation on Prompt 11:** `WAR-147` states that "rankings and world events receive the outcome **under B-11's rules**", so 11B must write the receipt rule that B-10 deliberately left to us. `WAR-162` and `WAR-150` bound it — no exact readiness, force or inventory is ever public, and anything identifying fewer than five nations is withheld or coarsened. `WAR-006` and `WRA-06` already use "objective" for campaign objectives and define fourteen immutable warfare audit event types, creating the **vocabulary collision** 11B must resolve by naming ours *national/strategic objectives* and reusing `WAR-153` machinery only where its fields genuinely fit. No B-10 rule, formula, operation, settlement mechanism or military restriction is altered here, and Operations Points stay military-only (`TR-005`, `D-015`, `WAR-040`). Rows `11A-INT-30`…`11A-INT-34`, V-06, V-11.

### 17.10 Downstream prompt boundaries

**Prompt 12** receives twenty-eight named behaviours with an evidence shape each, and owns every rule, consequence and detection capability; this report invents no punishment and claims no detection ability (`REQ-077`). **Prompt 13** receives eight required concepts — world-event surface, objective tracker, achievement page, standings interface, progression overview, historical timeline, event notifications, reward history — and owns every screen; `ONB-036` and `AP-006` make legibility a *design* obligation, so a self-explanatory standing is not a UI nicety. **Prompt 14** receives every numeric parameter, classified in §23 and §27. **Prompt 15** consolidates into **B-11 `18_world_events_and_progression.md`**, whose two-digit prefix is a serial number to be confirmed when 11B starts, not a part number. Rows `11A-INT-35`…`11A-INT-38`.

---

## 18. Anti-exploit and fair-play research

The complete register — **28** entries with risk ID, targeted mechanic, exploit method, potential advantage, severity, detection approach, prevention options, false-positive risk, subsystem owner and future acceptance-test requirement — is in [`11A_integration_and_risk_registers.md`](11A_integration_and_risk_registers.md) §5. **No moderation punishment is proposed anywhere in this report**, per §16.10 and §18 of the brief; every "prevention option" is a *design* control and every "detection approach" is an *evidence requirement handed to Prompt 12*.

**Severity summary:** Critical `11A-RK-001` (duplicate reward), `11A-RK-009` (multi-account progression stacking), `11A-RK-022` (reward compounding and currency inflation) — **High** `11A-RK-002` (snapshot manipulation), `003` (objective-driven pointless or protected-target warfare), `004` (challenge collusion and laundering), `005` (participation-volume account pushing), `008` (new-nation targeting), `010` (circular trade volume), `012` (event re-trigger), `013` (political-state manipulation), `018` (reward conversion), `019` (aggregate disclosure by differencing), `020` (automation), `027` (identity laundering of honours) — the remainder **Medium**.

**Five cross-cutting conclusions, each traceable to comparator harm rather than to theory.**

1. **The cheapest defence is metric shape, not detection.** Every volume-shaped, instantaneous-total-shaped or loss-shaped metric studied here generated a named prohibition in its own game — war slot filling, espionage slot filling, bounty coordination, treasure transfer coordination, capital farming, account pushing, wolf-packing, region crashing. A design that measures **windows, rates, variety and defensive outcomes** removes the target rather than policing it. `TR-044`'s existing "first in B4 order, later claims deduplicated by achievement key" already settles the duplicate-claim class for us (`11A-RK-001`).
2. **The highest-risk surfaces are the ones where a reward is transferable or convertible.** P&W's same-network restrictions, its "alliance banks to evade trade restrictions is a bannable offence", and NationStates' auction designed against "puppet nations feeding valuable cards to their masters" are all the same fight. `ECN-113` and `REQ-073` already forbid conversion, so our exposure is smaller **only if 11B holds that line for every reward type** (`11A-RK-004`, `11A-RK-010`, `11A-RK-018`).
3. **Two comparator features must be treated as active hazards, not neutral conveniences.** Travian ships **farm lists** as a free universal one-click raid tool and publishes advice implying that population rank is personal safety (`11A-BM-065`); Politics & War keeps a **scripted, undeletable tutorial nation** that its own activity feed shows being attacked for achievement completion (`11A-BM-004`, `11A-BM-010`). Both convert a design choice into a moderation burden.
4. **The absence-protection trade-off is real and we have already chosen correctly.** Every comparator that punishes absence (Travian's destroyed rewards, Politics & War's deletion ladder, Supremacy 1914's inactivity tax) creates automation pressure and churn; `D-028`'s exclusion-with-no-loss is the only stable position, and it makes `11A-RK-014` (strategic inactivity) a non-issue by construction.
5. **Detection claims must stay honest.** `REQ-077` forbids claiming perfect person-level identification and `REQ-066` forbids resting a permanent sanction on a shared address. NationStates' own multi-account enforcement is candid — automated pattern-matching plus player reports with a required structure (`11A-RK-009`) — and Supremacy 1914 admits "while we work on improving our Multiaccounting detection". Our report therefore names evidence shapes and detection *limits* rather than capabilities.

**Prompt 12 dependency summary.** Achievement farming, ranking manipulation, event abuse, objective collusion, fake trade volume, multi-account exploitation, reward exploitation, bot-assisted repetition and public-statistic manipulation are each recorded with a targeted mechanic, a method, an advantage and an evidence requirement, and **the rule, the consequence and the enforcement capability are Prompt 12's to specify**. Two items additionally require Prompt 12's privacy work: `11A-RK-019` (aggregate differencing) interacts with `D-027` and `ALL-156`, and the alliance-contribution visibility question already sits in Prompt 12's registered obligations (`DPE-049`, `DPE-054`).

---

## 19. Comparative research matrix

Legend: **Strong** = a substantial, documented implementation; **Partial** = present but limited, gated or contested; **None found** = no evidence obtained (explicitly **not** proof of absence); **N/A** = structurally inapplicable to that game; **Hist./Unv.** = documented but historical or unverified.

| Game | World events | Objectives | Rankings | Achievements | Long-term progression | Political systems | Economic systems | Competitive recognition |
|---|---|---|---|---|---|---|---|---|
| **Politics & War** | **Strong** — treasures on 60-day timers, annual Easter/Halloween events, weekly lottery, monthly cap reset, player bounties, pumpkin contest | **Partial/Hist.** — 26-step sequential tutorial documented once in 2019; live screen unverifiable | **Strong** — one board, 13 metrics, plus Treasures/Moon/Mars/Commendation boards; percentile shown | **Strong** — keyed, dated, non-retroactive, **completion rates published**; but includes attendance, purchase and staff entries | **Strong** — project chains, milestone projects, permanent badges, tenure display | **Partial** — policy axes and approval, no office or legislature | **Strong** — full production, market, income and monetary system | **Strong** — three distinct layers: transient leaderboard awards, permanent honours, achievements |
| **NationStates** | **Strong** — five issue trigger classes, player-throttleable cadence, ~weekly official news events, annual contests *(official-but-archived)* | **Partial** — no objective system; issues, queue cap and dismissal instead | **Strong (descriptive)** — dozens of census categories ranked against the world median, **no reward attached** | **None found** — no achievement system; postcards, cosmetic cards, SC badges, easter-egg badges instead | **Strong** — population milestones unlocking **authorship**, permanent identity, chronicle-style factbook | **Strong** — WA General Assembly, Security Council, elected Secretariat, voluntary jurisdiction with a compliance floor | **Partial** — taxes and spending are automatic; no nation-to-nation resource trading found | **Partial** — commendation/condemnation, delegate tenure, influence ranks; all **inert** |
| **Supremacy 1914** | **Strong** — event maps as parameter tuples, three-month seasons, weekly lottery-style draws, anniversary campaigns | **Partial** — Operations with dual reward lanes and tiered progress; **no tutorial found** | **Strong** — Index of Power plus a Victory Progress board; daily publication against tick-level evaluation | **Partial** — Hero Medals, medals and badges, season-placed unlocks; terminology overlaps | **Strong** — account rank gating *content choice*; SRP; permanent hero/unit unlocks | **Partial** — six-tier diplomatic ladder with trade and information effects | **Strong** — resources, upkeep, market, morale-production coupling | **Strong** — seasonal standings with real reward bands (top 5,000); placement payouts |
| **Travian: Legends** | **Strong** — annual tournament, Natars release schedule, seasonal special pass, weekly medal cycle | **Strong** — up to 10 daily tasks with four reward thresholds; per-village and avatar task ladders with geometric tiers | **Strong** — population and development points; medals derived from weekly Top-10 | **Partial** — medal families (weekly, streak, alliance, tournament, local, special, veteran) rather than an achievement list | **Strong** — Wonder level-100 terminal race; culture points as an expansion gate; permanent medals | **Partial** — alliance diplomacy and native institutions; no legislature *(local-world governance noted)* | **Strong** — four resources, production chains, market, upkeep | **Strong** — weekly snapshots, dual consecutive/non-consecutive streaks, alliance laurels; **ordinary round victory pays nothing** |
| **eRepublik** | **Partial/Hist.** — monthly triple-election calendar, wars, campaigns and epic battles; changelog appears frozen | **Partial/Hist.** — workout and battle participation implied; no documentation obtained | **None found** — no national strength index or leaderboard could be verified (`Nation`/`Country` pages 404) | **Partial/Hist.** — Decorations with first-N-in-country criteria; medal system revised once | **Strong** — four career tracks on one account; rank ladders; Protectors multi-input points | **Strong** — parties, monthly presidential and congressional elections, legislature moving tax and wage | **Partial/Hist.** — companies, labour, marketplace; internals not retrievable | **Partial/Hist.** — medals and orders; money buys *rights*, which is the cautionary case |
| **Call of War** | **Partial** — special rounds implied by official rules; no documented event system | **None found** | **Partial** — VP-based standings implied; no leaderboard documentation obtained | **None found** | **Strong** — research tree with slots and elite blueprints; partly account-persistent | **Partial** — coalition and team structures | **Strong** — economy, production and research | **Partial** — four termination channels including a hold-objective win and a retirement rule |
| **Tribal Wars** | **Strong** — seasonal special worlds on a real calendar; timed end-game phases | **Partial** — per-village and avatar task ladders with unbounded geometric tiers | **Strong** — points from completed construction; lazily recalculated rank; **snapshot cadence undocumented** | **Partial/Hist.** — medals and Hall of Fame referenced; no dedicated article found | **Strong** — persistence declared **per world type**; honour accumulation | **Partial** — tribe and alliance governance, off-game agreements | **Strong** — resource, population and building economy | **Strong** — weekly and tournament medals; **dominance threshold closes registration** |

**Reading of the matrix.** No game is strong in all eight columns, and the two games structurally closest to Nation Supremacy — Politics & War and eRepublik, both persistent single-world nation games — are the two weakest on *non-military recognition with no compounding*, which is precisely the gap §21 addresses. Conversely the games furthest from us structurally (Travian's round-based world, Supremacy 1914's rounds) are the strongest at **separating a resetting ladder from a permanent record** — the single architectural property this report recommends most strongly. **Two blanks are load-bearing rather than incidental:** no comparator documents an alliance scoring formula, and no comparator documents trade-derived standings safely, which together mean §14's alliance and trade rows are designed from our own rules and not from anyone else's practice.

---

## 20. Design alternatives

Four areas, each with the competing options the brief requires, evaluated before any recommendation. The recommendation itself is in §21.

### 20.1 World events

| Option | What it means | Advantages | Disadvantages | Evidence | Verdict |
|---|---|---|---|---|---|
| **A. Global scheduled events only** | A fixed calendar of world-wide modifiers and windows | Fully predictable; zero authoring; derivable by players | Becomes a routine; no responsiveness to state; every nation gets the same thing at the same time | P&W monthly cap reset; Travian Monday medals; eRepublik's triple election (`11A-BM-007`, `11A-BM-061`, `11A-BM-050`) | Insufficient alone |
| **B. System-triggered events only** | Thresholds over world or national state generate events | Responsive, personal, unbounded in variety without authoring cost | Hard to predict; can feel arbitrary unless the rule is published; risk of silent triggers | P&W treasure spawning with published timers; NationStates' statistic-gated issues (`11A-BM-014`, `11A-BM-069`) | Insufficient alone |
| **C. Player-triggered events** | Players create challenges the world can answer | Most socially vivid; free content | Needs escrow, expiry and counterparty independence; laundering surface; every comparator that tried it wrote an abuse rule | P&W bounties (`11A-BM-015`) | Adopt **narrowly**, with three controls |
| **D. National events only** | Events happen *to* one nation from its own state | No cross-nation fairness problem; perfectly legible; safe | Not "world" events; a solo player cannot see the world change | NationStates issue classes; P&W milestone projects (`11A-BM-058`, `11A-BM-016`) | Adopt as one class, not the whole |
| **E. Seasonal events** | Periodic named seasons with their own ladders | Solves veteran advantage; gives rhythm | Conflicts with one persistent world; FO-024 rejected resets | Supremacy 1914 seasons; Travian special worlds (`11A-BM-030`) | Adopt as **in-place windows**, never as instances |
| **F. Hybrid, parameterised** | One machinery, event types as data rows over the classes above | Satisfies `AP-003`; cheap variety; consistent semantics; one lifecycle to test | More surface area to specify; needs a strict taxonomy or it sprawls | Supremacy 1914's event tuple; Call of War's four termination channels (`11A-BM-032`, `11A-BM-038`) | **Recommended** |

**Recommended starting architecture: F** — four event classes (calendar, state, challenge, commemorative) on one shared machinery, each event type a published parameter row. Decisive reason: it is the only option that passes `AP-003`'s own test — "would this feature fail if the team were one person?" — because adding an event is adding a row, not writing a feature.

### 20.2 Objectives

| Option | Advantages | Disadvantages | Evidence | Verdict |
|---|---|---|---|---|
| **A. Sequential onboarding** | Guaranteed system coverage; no choice paralysis | Forces activities; goes stale; compels membership and militariness | P&W's 26-step list, one revision since 2019 (`11A-BM-004`) | **Only** for B-03's existing journey |
| **B. Optional objectives** | Respects `NAT-051`; suits twelve profiles | A player may never see a system; harder to reason about in tutorials | NationStates' five-slot bounded queue with free dismissal (`11A-BM-069`) | **Adopt as the default** |
| **C. Daily/weekly challenges** | Rhythm; measurable engagement | Daily = presence income or forfeiture, both barred; weekly is survivable | Travian daily quests with destroy-on-expiry; weekly medals without a login requirement (`11A-BM-060`, `11A-BM-061`) | **Weekly yes, daily only as generation, never as obligation** |
| **D. Long-term national goals** | The strongest retention object; matches development | Slow feedback; risks being only about size | P&W project chains; Tribal Wars' unbounded geometric tiers (`11A-BM-016`, `11A-BM-066`) | **Adopt** |
| **E. Event-linked objectives** | Timely; shared reference point | Window exclusion; escrow complexity | P&W event achievements and Easter tiers (`11A-BM-011`, `11A-BM-012`) | **Adopt** |
| **F. Hybrid with tiers** | Combines horizons; partial credit sustains momentum | Requires tier accounting and per-tier keys | Supremacy 1914 tiered Operations; Travian's partial-credit missions (`11A-BM-033`, `11A-BM-062`) | **Recommended** |

**Recommendation: F**, with three hard rules: no objective may require presence, membership or money; every collective objective has an individual equivalent; and dismissal or absence defers rather than destroys. The chore-avoidance test is the P&W case study: an objective list is a chore exactly when its completion condition is an *action count* rather than a *state reached* — which is why `11A-BM-068`'s state-triggered recognition is the preferred form.

### 20.3 Rankings

| Option | Advantages | Disadvantages | Evidence | Verdict |
|---|---|---|---|---|
| **A. One overall score** | Legible; cheap; a clear headline | **Fails on our own rules**: `AP-005`, the outline's "no single dominant ladder", `ECN-108`, `DMP-051`; and demonstrably couples balance to fairness | P&W Nation Score (`11A-BM-001`) | **Rejected** |
| **B. Multiple independent rankings** | Recognises many achievements; honest about dimensions | No headline; harder to parse; more surfaces to keep honest | P&W's 13 metric columns; NationStates' census categories (`11A-BM-002`, `11A-BM-054`) | **Adopt as the base** |
| **C. Composite national performance** | One number for broad comparison | Weights become the argument; a composite silently *is* option A | P&W score; Call of War strength index (undocumented) | **Permitted only as a labelled, non-eligibility index** |
| **D. Seasonal rankings** | Neutralises incumbency; gives rhythm | Needs an archive or history silently disappears | Supremacy 1914 SRP; Travian medals (`11A-BM-030`, `11A-BM-061`) | **Adopt** |
| **E. Historical records instead of rankings** | Cannot snowball; permanent | Not competitive; satisfies the archivist, not the contender | P&W permanent honours (`11A-BM-009`) | **Adopt as the permanent layer** |
| **F. Hybrid, four layers** | Separates measurement, competition, commemoration and description | Must keep the layers from leaking into each other | Every strong comparator is already hybrid (§19) | **Recommended** |

**Recommendation: F** — four layers: (i) **plural domain standings** (windowed, snapshot, percentile-displayed), (ii) **one separate eligibility measure** that is not a public ladder, (iii) a **descriptive profile** compared against the world distribution and rewarding nothing, and (iv) a **permanent record layer**. Decisive reason is empirical, not aesthetic: the one game that unified these (`11A-BM-001`) demonstrably converted a military tuning change into a fairness and eligibility change in the same patch.

### 20.4 Progression

| Option | Advantages | Disadvantages | Evidence | Verdict |
|---|---|---|---|---|
| **A. Milestones** | Derivable, legible, ungameable if records only | Age-biased if it drives rewards | `NAT-052` already fixes semantics; Travian tiers (`11A-BM-066`) | **Adopt as structure** |
| **B. Achievements** | Expresses diverse play | Catalogue drift toward attendance and purchase; needs completion-rate discipline | P&W (`11A-BM-010`) | **Adopt, deliberately small** |
| **C. Prestige** | Single accumulative status | Every implementation converts status to advantage; barred by `ECN-092` | eRepublik rank ladder (`11A-BM-049`) | **Rejected as a currency; honoured as a count** |
| **D. Historical record** | Cannot compound; permanent; cheapest to run | Fossifies; retention cost | P&W live badges; Tribal Wars per-mode persistence (`11A-BM-009`, `11A-BM-045`) | **Adopt as the spine** |
| **E. Seasonal** | Kills veteran advantage | Must not touch the permanent layer | Supremacy 1914 (`11A-BM-030`) | **Adopt for standings only** |
| **F. Hybrid** | Each layer does what it is good at | Requires the sharpest scope discipline | §19 | **Recommended** |

**Recommendation: F with D as the spine.** Progression is **derived** from owning-subsystem state plus the chronicle and introduces **no new numeric resource**; its highest-value reward is **authorship over one's own nation**, following `11A-BM-067`, because authorship cannot compound, cannot be bought, cannot be transferred and cannot make an old nation unbeatable. On "does this become an RPG level system": no — and the reason is that a level is a single accumulative comparator, which is option A under another name and fails the same three rules.

---

## 21. Recommended design direction

### 21.1 Field format and how to read it

Prompt 11A §20.5 requires fifteen fields per recommended direction. The **four domain-level directions** (§21.2–§21.5) carry all fifteen as an explicit block. The **thirty supporting recommendations** (§21.6) carry the identical fifteen fields in a grouped table; the grouping is declared here so no field is silently omitted.

| §20.5 field | Where it appears in §21.6 |
|---|---|
| Decision area; Problem | **Area / problem** |
| Options; Advantages; Disadvantages | **Options weighed** |
| Recommended direction | **Direction** |
| Evidence from benchmark games | **Evidence** |
| Nation Supremacy compatibility; Cross-system consequences | **Compatibility and cross-system effect** |
| Exploit risks; Player-experience impact | **Risk and experience** |
| Rationale | **Rationale** |
| Confidence; Provisional details | **Confidence / provisional** |
| Prompt 11B follow-up requirement | **11B follow-up** |

### 21.2 Primary direction 1 — World events

| Field | Content |
|---|---|
| **Decision area** | Domain A — world-event architecture |
| **Problem** | A persistent, mapless, shared world must stay interesting over months with **no content team**, without creating presence obligations, and without a second scheduler |
| **Options** | Global-only; system-triggered-only; player-triggered; national-only; seasonal-only; hybrid parameterised machinery (§20.1) |
| **Advantages** (of the choice) | One lifecycle, one key discipline, one test surface; event *types* are data rows; four distinct player-facing rhythms that can be tuned independently; passes the `AP-003` self-test by construction |
| **Disadvantages** | Requires the strictest taxonomy work in Prompt 11; a parameter row can still be badly designed; four classes means four documentation surfaces |
| **Evidence from benchmarks** | `11A-BM-014` (relative band, published timers, protection-aware exclusion), `11A-BM-012` (two-stage teardown, tiered annual content), `11A-BM-011` (asymmetric caps, costed interaction, escrow), `11A-BM-013` (pre-draw freeze, sink-funded reward), `11A-BM-015` (player challenge with escrow), `11A-BM-007` (calendar-deterministic state change), `11A-BM-032` (event as a parameter tuple), `11A-BM-058`/`11A-BM-069` (five trigger classes, bounded queue, dismissal) |
| **NS compatibility** | Fits `TR-040` P6 ownership and the B4 ordering duty; `AP-003`, `AP-007` satisfied; `ECN-215` and `DMP-141`/`DMP-266` constrain effects to named, keyed, published-input changes; `ONB-025` and `D-028` fit the eligibility shape exactly; no new scheduler, ledger type or state machine |
| **Cross-system consequences** | Closes the delegated `TR-042` row; requires `ECN-113`-conformant reward rows; must not touch B-05 floors, B-06 political state, or B-08 counts; reuses `WAR-153` machinery where fields fit and resolves the objective-term collision; consumes the digest under `TR-088`/`TR-089` rather than a new notification channel |
| **Exploit risks** | `11A-RK-012` re-triggering; `11A-RK-002` snapshot-edge play; `11A-RK-004` challenge laundering; `11A-RK-016` band suppression; `11A-RK-021` notification flooding |
| **Player-experience impact** | A world that visibly changes on a schedule a player can predict, with no day that must be attended; a returning player finds a bounded, digestible set of changes rather than a backlog |
| **Recommended direction** | **Four event classes — calendar, state, challenge, commemorative — generated only in P6 over one shared parameterised machinery, with relative-band eligibility, published timers, a participation freeze before any deciding snapshot, and two-stage teardown** |
| **Rationale** | It is the only architecture that simultaneously satisfies a hard scope constraint (`AP-003`), an existing assignment (`TR-040`/`TR-044`/`TR-055`) and the empirical failure modes of every comparator's bespoke events. Each device chosen is one where a live game demonstrated the *problem* first: unbounded content (NationStates' cap), destroyed rewards (Travian), frozen-out absentees (P&W escrow), instant racing (Supremacy 1914's freeze) |
| **Confidence** | **High** on structure and constraints; **Medium** on the four-class split being the minimal set; **Low** on any frequency, duration or magnitude |
| **Provisional details** | Event frequency, duration in turns, band bounds, occurrence caps, teardown lag, participation-freeze length, and any payout — all Prompt 14. Whether a challenge-class event exists at all in the first release is a 11B scope decision |
| **11B follow-up** | Write the event-definition schema (all parameter fields), the intra-P6 order as a rule, the eligibility function, the effect catalogue bounded to published inputs, the teardown rule, and the reward row per event class — then satisfy `TR-093`'s fifteen mandatory subsystem declarations |

### 21.3 Primary direction 2 — Objectives and challenges

| Field | Content |
|---|---|
| **Decision area** | Domain B — objectives and challenges |
| **Problem** | Give twelve player profiles meaningful goals without forcing any of them down one path, and without manufacturing chores |
| **Options** | Sequential onboarding; optional objectives; daily/weekly challenges; long-term national goals; event-linked objectives; hybrid with tiers (§20.2) |
| **Advantages** | Player-chosen goals across horizons; partial credit sustains momentum; dismissal is safe; the twelve-profile test can be met |
| **Disadvantages** | No guaranteed coverage of any system; the objective catalogue becomes the largest new document in B-11; tier accounting needs keys |
| **Evidence from benchmarks** | `11A-BM-004` (forced sequence compels alliance membership and military stockpiles, and froze in 2019), `11A-BM-069` (a hard five-item queue with penalty-free dismissal), `11A-BM-062` (tiered missions with partial credit; and the Daily-Login counter-example), `11A-BM-066` (geometric unbounded thresholds; escalating-reward counter-example), `11A-BM-060` (destroy-on-expiry as the harm case), `11A-BM-068` (state-triggered recognition needs no new task), `11A-BM-016` (chain-shaped long goals) |
| **NS compatibility** | Extends rather than re-opens B-03's journey; `NAT-051`/`NAT-052` are satisfied because objectives are chosen and milestones stay weightless; `REQ-073`/`NAT-046` bound first-time conditions; `AP-004` forces individual equivalents; `TR-085` removes the whole daily-obligation family; `ECN-113` shapes every material reward; `DMP-051` forces the political category to be re-expressed |
| **Cross-system consequences** | Every hostile condition routes through the cumulative B-03/B-08/B-09/B-10 validator set (`REQ-063`); trade objectives are publication-blocked until the gate; alliance objectives must remain aggregate-visible only; the "objective" term must be disambiguated from B-10's campaign objective |
| **Exploit risks** | `11A-RK-003`, `005`, `008`, `010`, `011`, `017`, `020`, `024`, `026` |
| **Player-experience impact** | A player sees a bounded set of goals they chose, can ignore any of them without loss, and receives partial recognition on the way to full completion |
| **Recommended direction** | **Optional-by-default objectives in three horizons, with tiered partial credit, a bounded outstanding set, penalty-free dismissal, state-triggered rather than action-counted conditions, and no objective that requires presence, membership, expenditure or aggression** |
| **Rationale** | The comparator record is one-sided on the harms and near-silent on the benefits of mandatory objective sequences, while the two most humane mechanics found — a bounded queue with free dismissal, and tiered partial credit — are both cheap and both compatible with our rules. Making recognition **state-triggered** removes the chore problem at its root rather than managing it |
| **Confidence** | **High** on the prohibitions and the tiered/optional structure; **Medium** that three horizons is the right cut; **Low** on difficulty scaling |
| **Provisional details** | Outstanding-objective cap, tier thresholds, per-tier rewards, repeat policy, expiry and grace lengths, randomisation of offered sets — all Prompt 14. Whether any objective grants a material reward at all is a 11B decision constrained by `ECN-013(c)` |
| **11B follow-up** | Write the lifecycle with its states (`AVAILABLE`…`SUPERSEDED`), the acceptance rule that makes silence non-consent, the tier and key model, the individual-equivalent requirement per collective objective, the validator mapping for hostile conditions, and the mechanic-change review hook for `11A-RK-024` |

### 21.4 Primary direction 3 — Rankings and competitive recognition

| Field | Content |
|---|---|
| **Decision area** | Domain C — rankings and competitive recognition |
| **Problem** | Recognise several kinds of national excellence without a single number dominating the game, without exposing private or small-group data, and without creating a manipulable target |
| **Options** | One overall score; multiple independent rankings; composite performance; seasonal rankings; historical records; hybrid (§20.3) |
| **Advantages** | Plural dimensions serve twelve profiles; windowed standings neutralise incumbency; percentiles scale across world sizes; the eligibility measure stays separable |
| **Disadvantages** | No single headline; several metrics must each be defined, tested and explained; aggregation limits may make some boards unpublishable at small populations |
| **Evidence from benchmarks** | `11A-BM-001` (one scalar coupling balance to fairness, demonstrated by a real patch), `11A-BM-002` (cheap plural columns; percentile-plus-rank display), `11A-BM-054` (descriptive median-relative layer with no reward), `11A-BM-061` (weekly windowed medals with defensive and non-conflict categories and dual streak forms), `11A-BM-030` (equal-start seasonal ladder; taxes as counter-example), `11A-BM-008` (transient awards and a bad tie rule), `11A-BM-023` (normalised pool), `11A-BM-042` (development-derived standing computed lazily), `11A-BM-019` (tenure as a hazard) |
| **NS compatibility** | `AP-005` and the outline's "no single dominant ladder" are satisfied structurally rather than by tuning; `D-027` governs every group figure; `TR-020`'s "an individual nation's public ranking is not an aggregate" defines the boundary; `WAR-162` and `ECN-215` bound military and wealth content; `DMP-051`/`DMP-042` remove approval and welfare; `DIP-084`/`DIP-088` shape diplomatic standing as counts; `ALL-224`/`ALL-156` bound alliance recognition; `REQ-091` and `D-028` settle inactivity; `TR-044`/`TR-045`/`TR-049` supply the tie-break mechanism |
| **Cross-system consequences** | Implements B-10's `WAR-147` receipt obligation; consumes only published state from B-04…B-09; writes P-class snapshots under `TR-090` within `TR-092`'s compaction; exposes movement through the existing digest; requires denominator disclosure because comparators publish inconsistent populations |
| **Exploit risks** | `11A-RK-002`, `006`, `011`, `014`, `015`, `016`, `017`, `019`, `023`, `025`, `027` |
| **Player-experience impact** | A nation can be *notable* in more than one way, sees where it stands relative to the whole rather than only whom it lost to, and is never displaced from a board by a rule it cannot see |
| **Recommended direction** | **Four separated layers — plural windowed domain standings; one distinct, published eligibility measure; a descriptive median-relative national profile that rewards nothing; and a permanent record-and-honour layer — snapshotted once per turn at a declared P6 point, published at P7, aggregated only at k ≥ 5, banded where exact values would identify, and tied only by published rules** |
| **Rationale** | This is the domain where our own constraints are most specific and comparators most instructive. Every accepted subsystem already refuses some single-number fusion; the study shows what happens when they are fused anyway. Separating the four layers lets each be tuned for its own purpose, which is the only arrangement under which a balance change to military inputs cannot silently rewrite fair-eligibility — the exact failure Politics & War demonstrated in its July 2025 update |
| **Confidence** | **High** on separation, snapshot discipline, aggregation limits and tie-break hierarchy; **Medium** on the four-layer cut; **Low** on which specific standings exist and on all weights |
| **Provisional details** | Every weight, window length, band boundary, snapshot interval, k-application detail, top-N size and eligibility threshold; which military measures survive `WAR-162` at a given band width; the k = 5 viability of alliance boards at launch population (`11A-OPEN-004`, `11A-OPEN-011`) — all Prompt 14 / Prompt 12 |
| **11B follow-up** | Define each standing as inputs + window + snapshot point + tie rule + eligibility set + exclusion rule; write the `WAR-147` receipt rule; specify band tables for military standings; specify the aggregate/withhold/coarsen decision procedure; specify the archive schema and the denominator disclosure |

### 21.5 Primary direction 4 — Long-term national progression

| Field | Content |
|---|---|
| **Decision area** | Domain D — long-term national progression |
| **Problem** | Give a nation durable identity and a sense of advancement over months and years without an RPG level, without a compounding advantage, and without making old nations unbeatable |
| **Options** | Milestones; achievements; prestige; historical record; seasonal; hybrid (§20.4) |
| **Advantages** | Records cannot snowball; authorship rewards are meaningful and inert; seasons neutralise incumbency; the whole layer is derivable, so it adds no state to keep consistent |
| **Disadvantages** | Little short-term feedback; closed honours fossilise; the layer is invisible to a player who wants power growth, so it must be paired with genuinely winnable standings |
| **Evidence from benchmarks** | `11A-BM-009` (twelve-year permanent, world-state-triggered, zero-effect honours), `11A-BM-016` (chains emitting several recognition types from one completion), `11A-BM-067` (milestones unlocking **authorship**), `11A-BM-073` (a game succeeding for eighteen years **without** an achievement system), `11A-BM-063` (a long cooperative terminal accomplishment), `11A-BM-045` (persistence declared per competitive object), `11A-BM-030`/`11A-BM-061` (ladder resets, honours persist), `11A-BM-049` (preserving advantage across a rewrite as the anti-pattern), `11A-BM-066` (geometric thresholds without new tiers) |
| **NS compatibility** | `NAT-051` "progression is chosen, not handed out" and `NAT-052` "milestones are records, not power" make this the *least* novel domain; `ECN-092` removes prestige currency; `FO-024` already rejects resets; `RRL-013`/`RRL-016` supply the two-scope model; `URB-158`/`URB-107` provide capstone objects and forbid capability grants; `NAT-045`/`INV-025` bar age and purchase differentials; `AP-008` bars reproducing any comparator's names or conditions |
| **Cross-system consequences** | Reads B-04/B-05/B-06/B-07/B-08/B-10 published state; writes chronicle and honour records; grants nothing that another subsystem must later reconcile; interacts with B-03's reroll and dormancy on every permanent object |
| **Exploit risks** | `11A-RK-015`, `023`, `024`, `027`; plus the general snowball risk in `11A-RK-022` |
| **Player-experience impact** | A nation accumulates a *biography* — what it built, held, signed, survived, named and was recognised for — which is legible to a visitor and unassailable by an attacker, while its competitive standing stays winnable by a newcomer |
| **Recommended direction** | **Model F with Model D as the spine: a derived, non-authoritative progression layer in which the permanent component is records, honours and authorship and the comparative component is seasonal and windowed; no new numeric resource, no level, no prestige currency, and no permanent capability** |
| **Rationale** | It is the only option that satisfies the brief's own worst-case list simultaneously — no runaway leader, no new-player wall, no infinite prestige farming, no age advantage, no inactive domination — because each of those risks is attached to a *specific* layer that the separation removes it from. It is also the best-evidenced: the permanent layer is demonstrated live, at zero mechanical weight, twelve years on |
| **Confidence** | **High** on the permanence/season split, the no-currency rule and the derived-not-stored model; **Medium** on authorship-unlock as the primary reward type; **Low** on threshold values |
| **Provisional details** | All milestone and honour thresholds, season length and reset scope, any authorship tiering, retention of archived progression, and whether the achievement layer exists at all in the first release — Prompt 14 and 11B scope |
| **11B follow-up** | Specify the derivation of each progression dimension from owning-subsystem state; the honour classes and their eligibility-closure rules; the season/record separation as a rule; the reroll and dormancy treatment per object; and the notability bar that discharges `UD-024` |

### 21.6 Supporting recommendations

| DR | Area / problem | Options weighed | Direction | Evidence | Compatibility and cross-system effect | Risk and experience | Rationale | Confidence / provisional | 11B follow-up |
|---|---|---|---|---|---|---|---|---|---|
| `11A-DR-001` | Event **generation mechanism** | Bespoke per-event code; a rule-evaluation layer; hand-authored content | **Systemic generation only**: events are published rules evaluated at P6 over frozen state; an event type is a parameter row | `11A-BM-032`, `11A-BM-058`, `11A-BM-008` | Satisfies `AP-003`; no second scheduler (`TR-040`); `TR-093` declarations apply | Removes operator dependency; players see derivable causality (helps `AP-006`) | Only class that survives a one-person team | **High** / none | Write the event-definition schema and its published fields |
| `11A-DR-002` | **Intra-P6 order** (the delegated `TR-042` question) | Events then objectives; objectives then events; interleaved | **Events → objectives → snapshot → records → deferred claims**, published | `TR-041`'s own reasoning; `TR-044` B4 duty | Closes a B-02 open row; makes `TR-055` first-in-order meaningful | Deterministic and auditable | Only one order can be tested; ambiguity is the risk | **High** on structure / order details to re-verify against 11B rules | State the order as a rule; amend `TR-042` |
| `11A-DR-003` | **Eligibility selection** | Absolute thresholds; fixed constants; relative bands | **Relative band against the current world maximum**, published, plus **world-average-derived caps** | `11A-BM-014` (15–65 % of leader), `11A-BM-046` (ratio veto), `11A-BM-023` (pool normalisation) | Reads B-03 states, never overrides them; distinct from the standing (`11A-DR-010`) | Self-scales without rebalancing; band suppression is the residual risk (`11A-RK-016`) | Three independent comparators converge on relative bands | **High** on shape / **Low** on every value; band bounds are Prompt 14 | Define the band inputs, the maximum used, and the publication text |
| `11A-DR-004` | **Event teardown** | Hard destroy at expiry; keep forever; two-stage teardown | **Two-stage**: stop accepting participation at one boundary; clean residual artefacts at a later declared boundary | `11A-BM-012` (eggs removed at day change, projects and in-flight items removed a week later) | Honours in-flight effects without extending the event; no ledger orphans | No "I was mid-action and lost it" class of complaint | Hard destroy conflicts with `D-028`'s no-loss principle | **High** / teardown lag is Prompt 14 | Specify both boundaries and what may still resolve between them |
| `11A-DR-005` | **Content pressure and fatigue** | Fewer events; player-throttled cadence; bounded outstanding queue | **Bounded outstanding set + penalty-free dismissal + player-adjustable cadence**, all inside one bounded digest row | `11A-BM-069` (five-item cap), `11A-BM-058` (6/12/24/48 h), `11A-BM-011` (2-give/1-receive daily caps, per-action cost) | `TR-089` unchanged; `TR-085` respected because throttling reduces content, not rewards presence | Frequency becomes a player choice | Every comparator that omitted this created an obligation | **High** / caps and throttle values are Prompt 14 | Specify caps, throttle range and the digest mapping |
| `11A-DR-006` | **Snapshot and draw integrity** | Real-time position; freeze window; random draw | **Participation freeze for one turn before any deciding snapshot or selection**; any randomness bounded, seeded and published | `11A-BM-013` (sales close one turn before the draw), `TR-032`, `TR-037` | Native to B-02's freeze model; no new phase | Removes last-instant racing; `TR-047` satisfied | The only integrity device with a direct comparator precedent | **High** / freeze length is Prompt 14 | State which decisions are freeze-guarded |
| `11A-DR-007` | **Player-initiated challenges** | Banned; free-form with no expiry; reservation + expiry + independence | Allow, with **reservation at creation**, **stated expiry or release**, **no self-claim** and counterparty independence validated | `11A-BM-015` and P&W's bounty-coordination prohibition | `TR-067`/`TR-069` reuse; `REQ-063`; Prompt 12 owns collusion | Enables the liveliest free content in the study with bounded capital risk | P&W's permanent escrow lock is the counter-example | **Medium** / minimum stake, expiry are Prompt 14 | Decide whether this class ships at all; else specify fields |
| `11A-DR-008` | **Achievement data model** | Ad hoc badges; a keyed register | **Fixed definition, binary keyed grant, dated attribution, published completion count and percentage with an explicit denominator** | `11A-RS-025` (1,449 of 14,630 = 9.90 %, with a dated list) | `TR-055` dedup; `TR-090` P-class record; `REQ-094` wording | Rarity becomes information; doubles as a health metric | Nothing else in the study yields this much value at this little cost | **High** / none | Specify the achievement record fields |
| `11A-DR-009` | **Objective acceptance and dismissal** | Auto-enrol; explicit accept; timed offers | **Explicit acceptance; dismissal never forfeits; a declined goal may return** | `11A-BM-069`, `11A-BM-067` (dismissed field "will receive the same issue again") | `REQ-523` non-consent; `D-028`; `TR-063`…`TR-066` amendment discipline | Removes consent-by-silence entirely | The brief's explicit "no consent by silence" requirement | **High** / return policy is 11B scope | Define the state machine and re-offer rule |
| `11A-DR-010` | **Score architecture** | One score; several scores; several scores + separate eligibility | **Plural standings and one separate published eligibility measure; a composite only if labelled and non-eligibility** | `11A-BM-001`, `11A-BM-042`, `11A-BM-054` | `AP-005`; outline's validation line; `ECN-108`, `DMP-051`, `URB-158` | Balance changes stop leaking into fairness | The single strongest empirical finding in the report | **High** / which measures exist is 11B | Enumerate the standings and the eligibility function separately |
| `11A-DR-011` | **Group-scope recognition** | Alliance ladder; alliance prizes; honour-only aggregates | **Honour-only, aggregate at k ≥ 5, diminishing returns; never a funding source; never mandatory** | `11A-BM-018` (square-root alliance bonus), `11A-BM-061` (alliance laurels) | `ALL-224` (no prizes), `ALL-156`, `D-027`, `AP-004` | Small alliances are protected; independents keep parity | Both directions are blocked by rule, so honour-only is the only lawful shape | **High** / threshold and bands are Prompt 14 | Specify aggregation and the withhold rule |
| `11A-DR-012` | **Purchased recognition** | Allowed cosmetic; allowed advantage; banned | **No purchasable or promotional achievement, honour, standing, eligibility or skip, in any form** | `11A-BM-010`, `11A-BM-020`, `11A-BM-053`, `11A-BM-033` | `NAT-045`, `ECN-092`, `REQ-073`, ₹0 constraint | Keeps the honour layer credible | Every comparator that allowed it created a two-tier recognition economy | **High** / none | Add a negative rule; no parameter |
| `11A-DR-013` | **Recognition object types** | One achievement list; four or five distinct types | **Five distinct objects**: achievement, milestone, seasonal award, historical honour, competitive standing — each declaring persistence, eligibility closure and reassignment | `11A-BM-008` vs `11A-BM-009`, `11A-BM-030`, `11A-BM-061` | `TR-090`, `RRL-013`/`RRL-016`, `NAT-052` | Stops permanent honours behaving like current standings | Collapsing any two is the documented source of each game's complaint | **High** / none | Write the type table with persistence per type |
| `11A-DR-014` | **One completion, several recognitions** | One reward per action; layered emission | **A single completion may emit a record, an honour and a standing entry at once**, deduplicated by one key | `11A-BM-016` (first-place badge + general badge + leaderboard from one build) | `TR-073` G2 prevents double value; `ECN-113` per material grant | Satisfies competitor and participant alike | Cheapest motivational win in the study | **High** / which layers apply is 11B | Specify the emission set per condition |
| `11A-DR-015` | **Military recognition shape** | Loss and kill totals; participation and defensive outcomes | **Participation, defensive outcomes in bands, and bounded campaign records — one activity feeds one standing only; never raw casualty or destruction totals** | `11A-BM-017`, `11A-BM-061`, `11A-BM-064` (PvE "won't help you climb the attacker ranking"), `11A-BM-030` (infantry exclusion) | `WAR-162`, `WAR-147` receipt duty, `D-027` | Removes the loss-scoreboard pathology | Directly mandated by B-10's privacy rule | **High** / band design is Prompt 14 | Write the `WAR-147` receipt rule and bands |
| `11A-DR-016` | **Honour eligibility closure** | First-N ever; first-N per window; world-state anchors | **Prefer world-state and window-scoped triggers**; permit closed first-N honours only where the closure is disclosed in advance | `11A-BM-009` (world-state badges live), `11A-BM-051` (first-50 per country), `11A-BM-061` (windowed medals) | `NAT-045` (no age differential), `TR-090` | Small-community lanes survive; permanent unobtainability is limited | Fossilisation is the documented cost of closed honours | **Medium** / closure policy is 11B | Specify per-honour closure and disclosure |
| `11A-DR-017` | **Progression mechanism** | New level/currency; derived records; unlock ladder | **Derived only** from owning state plus the chronicle; any unlock grants **options or authorship, never capability** | `11A-BM-028` (rank unlocks content choice, not power), `11A-BM-067` | `ECN-092`, `URB-158`, `NAT-052`, `AP-005` | No new state to keep consistent | A derived layer cannot silently desynchronise | **High** / unlock catalogue is 11B | Specify each dimension's derivation and its publication |
| `11A-DR-018` | **Seasonal reset boundary** | Reset all; reset standings only; no seasons | **Reset standings and seasonal progress; never records, honours or attributed history**; no national state resets | `11A-BM-030`, `11A-BM-045`; counter-examples `11A-BM-027`, `11A-BM-070` | `FO-024` (Rejected), `TR-090`, `REQ-071` | Continuity survives competition | The brief states it and Stage 1 already decided it | **High** / season length is Prompt 14 | Write the reset-scope table |
| `11A-DR-019` | **Standing methodology** | Cumulative totals; windows; rates; percentiles | **Windowed totals plus rates plus percentile display**, thresholds expressed as **share of a normalised pool**, archived snapshots as the source of truth | `11A-BM-023`, `11A-BM-061`, `11A-BM-002`, `11A-RS-025` | `TR-041`, `TR-092` cost limits | Removes both the incumbency and the manipulation bias | Cumulative-only boards are the study's clearest failure | **High** / every window and weight is Prompt 14 | Define each standing's window and normalisation |
| `11A-DR-020` | **Sustained versus attained position** | Snapshot only; duration-weighted; both | **Distinguish them**, and publish any duration-based curve | `11A-BM-026` (leader-sustain bonus; tiers undisclosed) | `TR-049`, `TR-071` (no silent cap loss; declared deterministic rules) | Prevents an invisible compounding rule | Undisclosed curves would breach our own publication rules | **Medium** / whether to reward sustain at all is open | Decide; if yes, publish the curve |
| `11A-DR-021` | **Competitive eligibility floors** | None; population minimum; decider-state closure | **Minimum-participation floor before a standing means anything**, and a **threshold that closes new entry before it closes the competition** | `11A-BM-029` (ranked only with two active), `11A-BM-044` (registration closure) | `TR-023` withhold rule; `D-028` exclusion is a different, already-settled case | Protects small worlds and late joiners from a decided race | Both thresholds must be published, never silent | **Medium** / values Prompt 14 | Specify floors and closure conditions |
| `11A-DR-022` | **Contested-objective class** | Absent; scored accumulation; held majority | Consider **sustained majority control of a fixed scarce set of abstract, non-spatial positions** as one event class | `11A-BM-039`, `11A-BM-024`, `11A-BM-031` (claim-window until stability ≥ threshold) | Must not imply territory, adjacency or an Alliance command role (`AP-002`, `AX-18`) | Creates a competitive lane that is not combat and not grind | The most promising *unproven* idea here; hence a candidate, not a conclusion | **Medium-Low** / all magnitudes open | Prototype the abstraction or drop it |
| `11A-DR-023` | **Diplomatic and political recognition** | Reputation score; computed standing; factual counts | **Counts of published acts, records of office held and cycles completed — never a derived standing, never mechanical** | `11A-BM-035`, `11A-BM-050`, `11A-BM-070` | `DIP-084`/`DIP-088`/`DMP-051`/`DMP-266` | Keeps politics consequential without making it measurable-as-virtue | B-08 chose this before the study confirmed it | **High** / which counts are displayed is 11B | Enumerate permitted counts and their display |
| `11A-DR-024` | **Path independence** | Shared gate; per-path entry fee; free parallel paths | **No path gated behind another's currency or grind; every collective goal has an individual equivalent; no cross-path entry fee** | `11A-BM-048` (level 9 / level 15 gates), `11A-BM-004` (forced #16) | `AP-004`, `NAT-045`, outline's "membership never mandatory" | Twelve profiles stay viable | The clearest anti-pattern across all four domains | **High** / none | Audit the catalogue for dominance per `AP-005`'s test |
| `11A-DR-025` | **Multi-input recognition** | One damage counter; several inputs | **Credit personal performance, service to a shared goal and logistical contribution separately**, and let one honours track read all three | `11A-BM-049` (Protectors: damage, country, equipment contribution) | Must not expose member data (`ALL-156`) or private military values (`WAR-162`) | Recognises support play that a single metric erases | Support roles are invisible in every comparator's primary ladder | **Medium** / input weights Prompt 14 | Specify permitted input classes |
| `11A-DR-026` | **Scheduled political calendar as an event source** | Invented event calendar; reuse the existing one | **Reuse B-06's published per-nation cycle dates as world-event anchors** rather than adding a second calendar | `11A-BM-050` (monthly triple election), `DMP-177`/`DMP-182` | No new scheduler; `DMP-266` forbids affecting outcomes | Gives the world predictable rhythm at zero cost | Already implemented as a subsystem; only needs exposure | **High** / none | Reference cycle dates as event inputs |
| `11A-DR-027` | **Descriptive layer versus competitive layer** | One; two; none | **Maintain a descriptive national profile compared against the world distribution, carrying no reward**, separate from standings | `11A-BM-054`, `11A-BM-073` | `DMP-051`/`URB-158` permit display and bar scoring | Gives identity-focused players something the ladder cannot supply | The one comparator without a leaderboard sustains itself for 18 years | **Medium** / which descriptors are lawful is 11B | Define permitted descriptive fields |
| `11A-DR-028` | **Office authority shape** | Accumulated influence; spendable authority; capped records | **Do not build an influence currency.** Record the direction — *rate-limit an office rather than empower it* — for **Prompt 12**, leaving `UD-047`/`UD-049` untouched | `11A-BM-055`, `11A-BM-071`, `11A-BM-018` (seniority as an eligibility floor) | `ECN-092`, `DIP-084`, `ALL-134` | Prevents authority accumulation | Recorded as a dependency, deliberately not as a proposal | **Medium** / owner-reserved areas untouched | None in 11B; referred onward |
| `11A-DR-029` | **Recurring-objective container** | Per-feature code; a parameterised container | **N tasks, a few cumulative thresholds, a deterministic published reward rotation identical across the world, one reset derived from the world clock, value invariant to world speed, and no forfeiture** | `11A-BM-060` (all five properties, plus the destroy-on-expiry defect) | `TR-085`, `D-028`, `ECN-113` (rotation may not contain yield multipliers) | Predictable without being compulsory | The best-engineered and worst-compelling system studied | **High** on the container / caps and tiers are Prompt 14 | Specify the container schema |
| `11A-DR-030` | **Terminal cooperative accomplishment** | New wonder mechanic; reuse capstones | **Reuse B-05's capstone programmes as the lawful shape** of a long, cooperative, indestructible accomplishment; recognition and record only | `11A-BM-063`, `URB-107`, `URB-035` | §16.4 forbids new infrastructure mechanics; `NAT-052` forbids ranking weight | Gives a peaceful long game a finish line without new machinery | The Wonder's virtue is that it cannot be confiscated, which our cities already share | **High** / cost and completion shape are Prompt 14 | Specify capstone-based honours |
| `11A-DR-031` | **Milestone threshold shape** | Linear; fixed tiers; geometric | **Geometric thresholds with an open tail**, and a **nation-scope versus account-scope split** declared per object | `11A-BM-066`, `11A-BM-062` (dual scope) | `RRL-013`/`RRL-016`, `D-040` (tutorial progress is account-scoped) | Never needs a new tier invented to escape saturation | Escalating *repeat rewards* rejected alongside it | **High** on shape / every threshold Prompt 14 | Specify the series and per-object scope |
| `11A-DR-032` | **Progression reward type** | Capability; currency; authorship | **Authorship over one's own nation** — naming, describing, presenting — as the top of the reward ladder | `11A-BM-067` (capital, leader, pretitle, faith at milestones) | `NAT-045` (driver must be achieved state, not age), `B-03` naming rules `NAT-027`…`NAT-040` already govern | Meaningful, untransferable, uncompoundable | The only reward class that is simultaneously valuable and inert | **Medium** / how many authorship tiers is 11B | Map onto existing B-03 naming and identity rules |
| `11A-DR-033` | **Inertness disclosure** | Silent; stated in rule text | **State a recognition object's inertness in its own definition** — what it does not grant — as a required field | `11A-BM-068` ("Cards are cosmetic. They grant no benefits…") | `AP-006`, `NAT-052`, `TR-049` | Prevents the reward being read as a capability | Costs one field and removes a whole dispute class | **High** / none | Add the field to the schema |
| `11A-DR-034` | **Achievement-layer size** | Maximal checklist; small optional layer; none | **Deliberately small and optional**; carry long-term motivation on records, standings, honours and authorship instead | `11A-BM-073` (a game with no achievements at all), `11A-BM-010` (how a large layer decays) | `NAT-052` gives ownership but not a mandate | Keeps the achievement set honest and maintainable | Ownership of the framework does not imply an obligation to fill it | **Medium** / final scope is an 11B decision | Decide scope, then apply `11A-DR-008` |

---

## 22. Category B decisions

These are ordinary design-direction decisions made autonomously under `D-014` and recorded in [`../../DECISIONS.md`](../../DECISIONS.md) as **D-144…D-151** with mirrored positions **DD-192…DD-199** in [`../04_approved_and_provisional_decisions.md`](../04_approved_and_provisional_decisions.md). Each is a **research-level design direction**: it settles which way Prompt 11B should specify a system and does **not** approve a rule, a value, an implementation or this prompt's own output. No fixed constraint is touched, and no owner-reserved decision is resolved.

| New ID | Topic | Position adopted | Alternatives rejected | Primary evidence | What it binds |
|---|---|---|---|---|---|
| `D-144` | 11A execution split and deliverable paths | Prompt 11 is executed as **11A** research, **11B** specification, **11C** workflows and acceptance, against one roadmap item; canonical research deliverable is this file with two named registers; B-11's authoritative document stays `18_world_events_and_progression.md`, with the filename confirmed by 11B before writing | One monolithic prompt; a four-way split; renaming `18_` | The 07/08/09/10 precedent in [stage-2/01](../01_stage_2_prompt_roadmap.md); the serial-number rule in [stage-2/02](../02_master_game_design_bible_outline.md) §1 | Follows the sub-prompt convention the validators already track |
| `D-145` | Identifier policy for 11A | Use `11A-RS/BM/DR/RK/INT/CR/OPEN`; **do not** create `11A-DEC`; **do not** allocate global `REQ-` or `UD-` IDs at research level | A parallel `11A-DEC` decision register; allocating `REQ-704`+ now | `D-014` policy §5 forbids a second register for an existing ID; 08A/09A/10A precedent (candidates first, `REQ-` rows at specification) | Keeps `REQ-703`, `D-143`, `DD-191`, `UD-049` maxima intact until 11B |
| `D-146` | **World-event architecture** | Four event classes on one shared parameterised machinery, generated only at **P6**; systemic generation only, no authored live ops | Global-only; system-only; player-only; national-only; seasonal-only; bespoke per-event code | `AP-003`; `11A-BM-032`, `11A-BM-014`, `11A-BM-058` (`11A-DR-001`…`11A-DR-007`) | 11B writes the event schema and effect catalogue |
| `D-147` | **Objective architecture** | Optional-by-default objectives in three horizons with tiered partial credit, a bounded outstanding set, penalty-free dismissal, state-triggered conditions; **no** presence, membership, expenditure or aggression requirement; B-03's journey is extended, not re-opened | Sequential mandatory chain; daily obligation; single long-goal track | `11A-BM-004`, `11A-BM-069`, `11A-BM-062`, `NAT-051`/`NAT-052` (`11A-DR-009`, `11A-DR-024`, `11A-DR-029`) | 11B writes the lifecycle and catalogue constraints |
| `D-148` | **Ranking architecture** | Four separated layers: plural windowed domain standings; **one separate published eligibility measure**; a descriptive median-relative profile; a permanent record-and-honour layer. No single dominant ladder; no composite that also gates anything | One national score; a weighted composite as the headline; season-only; records-only | `11A-BM-001` (the coupling failure demonstrated by a real patch), `11A-BM-054`, `11A-BM-042`, the outline's validation line (`11A-DR-010`, `11A-DR-013`, `11A-DR-019`) | 11B writes each standing and the `WAR-147` receipt rule |
| `D-149` | **Progression architecture** | Hybrid with **historical record as the spine**, milestones as structure, a deliberately small optional achievement layer, seasons confined to standings, **no** prestige currency and no new numeric resource; top reward class is **authorship**, not capability | An RPG level; a prestige currency; a maximal achievement checklist; milestones granting ranking weight | `11A-BM-067`, `11A-BM-073`, `11A-BM-009`, `ECN-092`, `FO-024` (`11A-DR-017`, `11A-DR-032`, `11A-DR-034`) | 11B writes the derivation table and honour classes |
| `D-150` | **P6 evaluation order** (the row delegated by B-02) | Fix the intra-P6 order as **events → objectives → standing snapshot → record writes → deferred-claim release**, published at P7 | Events after objectives; interleaved; per-subsystem local ordering | `TR-041`'s own rationale; `TR-044` B4; `TR-055`; `11A-BM-023` | Closes the open row in `TR-042` at research level; 11B must state it as a rule and `TR-042` must then be annotated as dispositioned |
| `D-151` | **Reward posture** | Default hierarchy **recognition → record → authorship → (rare, disclosed, keyed, ledgered) material**. No permanent yield multiplier; no purchasable or convertible recognition; no presence-linked reward of any kind; alliance recognition is honour-only | Material-first; attendance-linked; production-bonus rewards; alliance-funded prizes | `11A-BM-060`, `11A-BM-005`, `11A-BM-020`, `ECN-113`, `ECN-013(c)`, `ALL-224`, `TR-085` (`11A-DR-012`, `11A-DR-011`) | Bounds every reward row 11B may write |

**Why these eight and not more.** Only decisions that would otherwise force a later session to re-litigate a direction are promoted to `D-` entries; the remaining thirty `11A-DR-###` recommendations stay in this report as evidence-linked recommendations that 11B may accept, modify or reject with a stated reason. This keeps the decision log to material positions, as `DECISIONS.md` line 4 requires.

---

## 23. Category C provisional decisions

Each row is a **safe working assumption adopted provisionally under `D-014` Category C**, with the exact evidence that would confirm or replace it. A provisional position blocks only the rule that depends on it, never this prompt's completion. **All numeric calibration belongs to Prompt 14**, which is the registered owner of every value below.

| # | Provisional assumption | Why provisional | Evidence that finalises it | Owner |
|---|---|---|---|---|
| P-01 | A **turn-expressible** cadence band works: generation may be daily (12 turns), standings refresh per turn, medals-style awards weekly (84 turns), seasons monthly-to-quarterly, commemorative events rare | No player-population data exists; comparators' day counts are theirs, not ours | Playtest cadence data; churn by session length; a simulation of award frequency vs perceived value | Prompt 14 |
| P-02 | **Relative-band eligibility** against the current world maximum beats an absolute threshold | Unproven in our own world; the band bounds are comparator-derived only | A balance model of band membership over a growing population; band-suppression behaviour (`11A-RK-016`) | Prompt 14 |
| P-03 | **k = 5 is sufficient** for the standings and awards this design contemplates | Alliance and small-cohort sizes are unknown; a board may be lawful yet empty | Population and alliance-size distribution at realistic scale (`11A-OPEN-004`, `11A-OPEN-011`) | Prompt 12 with Prompt 14 |
| P-04 | A **windowed rate measure** can be computed from archived per-turn snapshots without a new stored state | Derivation cost is unmeasured; `TR-092` compaction may destroy the needed window | A storage and query cost model at 1,000 nations × 12 turns/day | Stage 5 with Prompt 14 |
| P-05 | The **material-reward class exists at all**, and if so is "rare" within `ECN-013(c)`'s meaning | "Rare" is undefined; a threshold-free grant risks `11A-RK-022` | An economy model of reward share against money supply growth (`11A-OPEN-012`) | Prompt 14 |
| P-06 | **Seasons are in-place windows**, not instances, and require no new state beyond a season identifier | FO-020 stays Deferred; the persistence model for a season identifier is unspecified | A 11B design review plus a reroll/dormancy interaction test | Prompt 11B, values to 14 |
| P-07 | **Authorship unlocks** can be layered on B-03's existing naming and identity rules without changing them | `NAT-027`…`NAT-040` were written for creation and renaming, not for progressive unlocking | A 11B compatibility review against B-03 §7 | Prompt 11B |
| P-08 | A **participation freeze of one turn** before a deciding snapshot is enough | Attack and manipulation timing at boundaries is unmeasured; comparators use one turn (Supremacy 1914) but at a different cadence | An adversarial timing test; `TR-032`'s existing next-turn-join behaviour may already suffice | Prompt 14 with Prompt 12 |
| P-09 | A **two-stage teardown** (stop accepting, then clean) needs no exception path for in-flight player actions | Unproven against B-10 campaign timing and B-07 reservation release | A workflow test of an event ending mid-campaign and mid-offer | Prompt 11C |
| P-10 | **Defensive recognition** can be expressed in published bands that survive `WAR-162` | Band width versus identifiability is untested; a band over a small population may still identify | A privacy review of the proposed bands plus a differencing test (`11A-OPEN-014`) | Prompt 12 with Prompt 14 |
| P-11 | **Trade standings** can be fully specified now and remain unpublished until G-1…G-6 pass | The gate's own evidence schedule is owned elsewhere; the statistic's cost is unknown | The gate evidence itself (Prompt 07/12/14 owners) | Prompt 07 gate, not 11 |
| P-12 | A **descriptive median-relative profile** can be built only from already-public values, adding no new computed score | Some descriptors would need a novel aggregate, which would inherit the ranking rules | A field-by-field source audit against owning subsystems (`11A-OPEN-007`) | Prompt 11B |

**Structural versus numerical.** P-01, P-02, P-05, P-08 and P-10 are **Prompt 14 calibration dependencies**; P-03 and P-11 are **gated on evidence owned by other prompts**; P-04 is an **architecture-stage measurement** with a Prompt 14 parameter; P-06, P-07 and P-12 are **11B design questions**. Every non-numeric recommendation in §21 is a **structural requirement**, and every threshold, weight, cap, interval or amount named there is a **candidate parameter**, not a provisional value.

---

## 24. Owner-reserved dependencies

**Nothing owner-reserved is resolved, widened or bypassed by this report.** The items below are recorded because Prompt 11 must design *around* them, and 11B must not silently assume an answer.

| Item | Status | Why it matters to Prompt 11 | Required handling |
|---|---|---|---|
| **`UD-040`…`UD-049`** (alliance policy set) | **Open / owner-reserved**, unchanged | `UD-046` (alliance treasury ownership, custody, capacity, withdrawal, spending) and `UD-047` (collective positions and delegation) bound any alliance ranking, collective objective or alliance-scoped honour. `UD-040` membership/founding policy bounds contribution attribution | 11B specifies alliance-facing recognition **only** as k ≥ 5 aggregates, honour-only, and with no military command, no shared pool and no member-value exposure |
| **`UD-024`** — chronicle quality bar | **Deferred to Prompt 11** by `05_unresolved_design_decisions.md`; **still open** | Determines what the world chronicle must contain and therefore what history a returning player can read | §12.2 and §14.6 give it a direction; **11B must state the bar.** 11A does not mark it resolved |
| **`D-027`** aggregate threshold | **Confirmed** by the owner | Governs every alliance, military and group-facing standing | Reused verbatim; **no new privacy threshold is invented anywhere in this report** |
| **`D-021`** no catch-up acceleration | **Confirmed** by the owner | Rules out the comparator catch-up mechanisms (new-player income slopes, age tiers) | Respected; any future catch-up design must satisfy `ECON-012`'s constraints |
| **`D-122`, `DD-136`, `REQ-513`**, gates **G-1…G-6** | Approved mandatory scope; **release-gated**, five gates not met, one partial | Blocks all trade-performance standings and volume objectives | Preserved exactly; **no gate is marked satisfied** and no readiness claim is made |
| **`REQ-518`** inert-until-Prompt-10 pattern | Provisional | Precedent that a designed restriction may exist before it is enforceable | Cited only as precedent for sequencing discipline |
| **`AP-001`…`AP-008`** | Provisional Stage 1 pillars | `AP-003` is already a registered Prompt 11 guardrail; `AP-004`, `AP-005`, `AP-007` shape the recommendations | Treated as binding design law; **promoting or altering any pillar is an owner decision** and is not attempted here |
| **`FO-020`** seasonality; **`FO-024`** resets | Deferred; **Rejected** | Seasonal progression must be in-place; no reset of national state | Respected; a season may reset a standing only |
| **`OSQ-001`…`OSQ-012`** (Stage 1 security owner questions) | Open owner questions | Multi-account policy and monitoring scale affect `11A-RK-009` and `11A-RK-020` | Handed to Prompt 12; no assumption made |
| **`UD-017`** jurisdiction/legal review | Open, owner | Community-submitted content (the contest pattern) has legal dimensions | Only the in-game voting half is proposed; the submission channel is not |
| **Real-money prize structures** | Out of policy for this project | Travian's €4,000/€2,000/€1,000 voucher model is explicitly **not** adopted (§9.3) | No cash, voucher or external-prize concept is proposed anywhere |

---

## 25. Prompt 11B research-to-specification handoff

**Prompt 11B is the next task: World Events, Objectives, Rankings and National Progression — Complete System Specifications.** It converts the accepted design foundations here into the normative B-11 rulebook at `18_world_events_and_progression.md`. 11A approves no rule; 11B owns the rules.

### 25.1 What 11B may rely on as settled

| Foundation | Source | Binding on 11B |
|---|---|---|
| Four separated ranking layers, with one distinct eligibility measure and **no single dominant ladder** | `D-148`/`DD-196`; §14; §21.4 | Yes as a direction; a departure needs a new recorded decision |
| Four event classes on one systemic P6 machinery; no authored content | `D-146`/`DD-194`; §12.5 | Yes; `AP-003` is the underlying reason |
| Optional-by-default objectives, tiered credit, bounded queue, penalty-free dismissal | `D-147`/`DD-195`; §13 | Yes |
| Derived progression with the record layer as spine; seasons reset standings only | `D-149`/`DD-197`; §15 | Yes |
| Fixed intra-P6 order closing `TR-042` | `D-150`/`DD-198`; §12.2 | Yes, and 11B must also cause `TR-042`'s row to be annotated as dispositioned |
| Reward hierarchy recognition → record → authorship → rare material | `D-151`/`DD-199`; §13.5 | Yes |
| Five recognition object types (achievement, milestone, seasonal award, historical honour, standing) | `11A-DR-013`; §6.4, §19 | Direction |
| **30 candidate requirements** `11A-CR-001`…`11A-CR-030` | Companion register §6 | **Not requirements.** Each must be adopted, modified or rejected with a stated reason; adoption converts it to `REQ-704` onward |

### 25.2 What 11B must decide (research-level questions closed by a rule)

1. **The standing set.** Which domain standings exist, by name, with inputs, window, snapshot point, tie rule, eligibility and exclusion. §14.1 gives the per-category legality verdict; **`11A-OPEN-007`** (what a political-performance standing may be, given `DMP-051`/`DMP-042`) must be resolved here or the category dropped.
2. **The eligibility measure.** Its inputs and its publication form, kept separable from every standing (`11A-DR-010`) and reusing B-03's states rather than duplicating them.
3. **The event catalogue.** Concrete event rows per class, each with its parameter values referenced to Prompt 14; whether the **challenge class** ships at all (`11A-DR-007`); the notability bar for the chronicle (**`UD-024`**, §14.6).
4. **The objective catalogue.** Categories from the 16 assessed in §13.1, per-objective horizons and tiers, and the mechanic-change review hook for `11A-RK-024`.
5. **The achievement and honour classes.** Their eligibility-closure rules (world-state preferred over first-mover, `11A-DR-016`), their scope (nation or account, `11A-DR-024`), and **whether an achievement layer exists at all** (`11A-DR-034`).
6. **The season boundary.** What a season resets, what it never may, and how a season identifier is stored — respecting **FO-024**'s rejection of resets.
7. **B-10's receipt rule.** `WAR-147` obliges B-11 to define how rankings and world events receive a campaign outcome, within `WAR-162` bands (`11A-DR-015`).
8. **Terminology.** Adopt **"national objective"/"strategic objective"** for B-11 and leave "campaign objective" to B-10 (`11A-INT-32`).
9. **The B-02 §18 contract rows.** Write the ranking-entry, retirement-event and historical-attribution behaviours that B-03's `CON-001` row already commits Prompt 11 to (companion register §3, `11A-INT-10`).
10. **Confirm the file path.** `18_world_events_and_progression.md` is the planned serial name; confirm it is still free before writing.

### 25.3 Constraints 11B inherits unchanged

Every rule in §3.3, §24 and companion register §2–§4 applies. Most likely to be breached by an enthusiastic specification: `ECN-113` (no permanent yield multiplier), `ECN-013(c)` (rare material grants only), `ECN-092` (no prestige currency), `DMP-051`/`DMP-042` (no approval or welfare standing), `DMP-141`/`DMP-266` (event effects only through named terms, never setting political state), `DIP-084` (no diplomatic score), `URB-040` (events cannot breach the infrastructure floor), `URB-158` (no capability grants without a decision and a register row), `ALL-224` (no alliance-funded prizes), `ALL-156`/`D-027` (member data and k ≥ 5), `WAR-162` (no exact military values public), `MKT-072` (no pre-gate market statistic), `TR-085` (no presence mechanics), `TR-005`/`D-015` (OP is not a reward), `REQ-073`/`NAT-046` (no re-earnable first-time benefit), `D-028` (no loss through absence), and `D-014` player sovereignty (**no consent by silence** — an objective never auto-accepts, an event never acts for a player).

### 25.4 Register work 11B must perform

Allocate `REQ-704` onward only for requirements actually specified; mirror adopted `11A-CR` rows; annotate `TR-042`; keep `UD-024` moving and open `UD-050` onward only for genuinely unresolved matters; add `D-`/`DD-` rows for each new binding position; update [stage-2/03](../03_requirements_traceability.md), [stage-2/04](../04_approved_and_provisional_decisions.md), [stage-2/05](../05_unresolved_design_decisions.md), [stage-2/02](../02_master_game_design_bible_outline.md) (B-11 Planned → Draft), [stage-2/06](../06_stage_2_progress_log.md), and the three continuity files; and extend `status_rules.py`'s sub-prompt detector to the 11 family (§31.7).

---

## 26. Prompt 11C workflow and acceptance handoff

**Prompt 11C is not started**, and 11A pre-empts none of it. Its registered shape follows the 08C/09C/10C precedent: workflows, edge cases, an acceptance matrix, a bidirectional requirement ledger, failure codes, and the pass decision.

| # | 11C deliverable | What 11A already supplies | What 11C must add |
|---|---|---|---|
| 1 | **Event lifecycle workflows** | §12.2's fifteen-stage mapping onto P6/P7 | End-to-end flows per event class, including mid-event protection onset, dormancy, reroll, and a failed or interrupted turn |
| 2 | **Objective lifecycle workflows** | §13.2's ten states | Accept → tier → complete → claim → defer → expire, with the mechanic-change supersession path |
| 3 | **Snapshot and publication workflow** | §14.4's one-snapshot-point rule | Archive derivation, weekly/monthly rollup, denial and withhold paths |
| 4 | **Reward accounting workflow** | §13.5's hierarchy; `REWARD` ledger type | Conservation check at P7; duplicate-claim rejection; deferral ledger behaviour |
| 5 | **Edge cases** | 28 risks in §18, each with a detection shape | A numbered case catalogue, each tied to a rule and a test |
| 6 | **Acceptance matrix** | Candidate requirements and the §30 gates | Tests per rule, each **Designed, not executed** — the project's standing convention until a build exists |
| 7 | **Bidirectional requirement ledger** | 30 candidates → whatever 11B allocated | DIRECT / SUPPORTING / DEFERRED / NOT COVERED classification with group totals, per the 08C-E precedent |
| 8 | **Failure codes** | The action-lifecycle code families in B-02 and B-10 (`WRF` gaps disclosed by `D-143`) | A B-11 code set that must **not** silently fill an existing gap |
| 9 | **Free-tier evidence plan** | §14.6's storage reality and `TR-092`'s compaction | Measured rows-and-bytes per nation-turn for snapshot and chronicle writes, against the Stage 1 measurement (~264–291 bytes/nation-turn; ≈140-day budget at 500 MB without retention) |
| 10 | **Validator** | This report's §32 checks | A B-11 workflow validator with negative fixtures and a self-test, following `verify_warfare_workflows.py`'s 49-check shape |

**Explicitly not 11C's to invent:** moderation punishments (Prompt 12), screens (Prompt 13), numeric values (Prompt 14), or any change to B-02…B-10.

---

## 27. Prompt 12–15 dependencies

### 27.1 Prompt 12 — fair play, protection, privacy and administration

Twenty-eight risks are registered in companion register §5 with an owner and a required evidence shape each. The five that most constrain Prompt 11's design and must be named for Prompt 12: **achievement/reward duplication** (`11A-RK-001`, mitigated by the existing key rule), **ranking manipulation at a snapshot edge** (`11A-RK-002`), **objective-driven aggression against protected or weak nations** (`11A-RK-003`, `11A-RK-008`), **multi-account progression stacking** (`11A-RK-009` — including Travian's official dual-crediting as the anti-pattern), and **aggregate disclosure by differencing across standings and turns** (`11A-RK-019`). Also handed over: challenge-collusion (`11A-RK-004`), participation-volume pushing (`11A-RK-005`), manufactured-loss farming (`11A-RK-006`, `11A-RK-017`), undeclared-cooperation gaming of collective objectives (`11A-RK-007`), forced-membership pressure (`11A-RK-026`) and honour laundering across rerolls (`11A-RK-027`). **No punishment, threshold or detection capability is proposed here**, and `REQ-077` remains the governing honesty rule. Prompt 12 additionally owns the visibility of member contribution history and the audit rules for privileged reads — both already registered to it (`DPE-049`, `DPE-054`).

### 27.2 Prompt 13 — interface and player journeys

Eight concepts are named as required surfaces, and **no component, layout or screen is designed here**: a world-event surface; an objective tracker with tier progress; a national achievement and honour page; a standings interface showing window, percentile and denominator; a progression overview; a historical timeline (the chronicle); event and award notifications; a reward and claim history. Two constraints from elsewhere land on Prompt 13: legibility is a **design** obligation (`ONB-036`: progression must be legible without a spreadsheet; `AP-006`: no rules requiring out-of-game wikis), and **no native chat, voice or third-party messaging integration may be designed** — in-game notifications and audit visibility are the supported surface. The `11A-BM-052` media/press pattern is therefore explicitly **not** transferred. Prompt 13 must keep the War Operations Board and the Alliance management interface distinct, and Prompt 11 adds neither.

### 27.3 Prompt 14 — numerical calibration

Every numeric dependency this report identifies, classified as required by §16.12. **None is decided here.**

| Class | Items |
|---|---|
| **Structural requirement** (shape fixed, value open) | One snapshot per turn; percentile display with denominator; k ≥ 5 for any group figure; band-only military values; relative-band eligibility; two-stage teardown; bounded outstanding objective set; geometric milestone series; one key per completion |
| **Candidate parameter** | Standing windows and their count; band upper/lower fractions; tie hierarchy thresholds; objective tier counts and spacing; outstanding-objective cap; cadence throttle range; honour-closure form; season length; achievement-layer size |
| **Provisional assumption** (§23) | P-01 cadence band; P-02 band bounds; P-03 k = 5 sufficiency; P-05 material-reward existence and "rare"; P-08 one-turn freeze; P-10 defensive band width |
| **Prompt 14 calibration dependency** | Event frequency, duration and overlap limits; objective difficulty and reward value; ranking weights; snapshot and award intervals; achievement and milestone thresholds; progression thresholds; season duration; honour accumulation rules; reward caps; eligibility window lengths; **and explicitly no decay or retention curve**, since `D-028`/`TR-085` make decay out of scope rather than untuned |

Prompt 14 must additionally resolve **`11A-OPEN-006`** — whether `URB-119`'s expensing of research against national wealth makes any wealth-anchored standing structurally anti-development — and **`11A-OPEN-012`** (the currency-impact bound for `ECN-013(c)`'s "rare").

### 27.4 Prompt 15 — Game Design Bible consolidation

Prompt 15 will need from B-11: the event catalogue and lifecycle; the objective catalogue and lifecycle; the standing definitions and their snapshot discipline; the achievement, milestone, honour and record classes; the chronicle content bar (`UD-024`); the season boundary; the cross-system contract rows; the `TR-042`/`TR-044`/`TR-055` annotations; and every open item. **11A assembles nothing into the Bible**, and B-11 remains **Planned** until 11B drafts it. Prompt 15 also inherits the compile step for B-15's interaction matrix, into which the 40 integration rows here feed.

---

## 28. Open research questions

The full register with owners and closing evidence is companion register §7 (`11A-OPEN-001`…`11A-OPEN-016`). Summarised:

| ID | Question | Owner |
|---|---|---|
| `11A-OPEN-001` | Does the live P&W objectives screen still present a sequential list compelling alliance membership? | Research gap (login-gated) |
| `11A-OPEN-002` | Are P&W leaderboard awards still issued, on what cadence, and is the developer-tie rule real? | Research gap (no official page) |
| `11A-OPEN-003` | How does a rate-based standing behave as the world grows, and does it re-create a snowball? | Prompt 14 |
| `11A-OPEN-004` | What is the smallest population at which each standing stays meaningful **and** non-identifying? | Prompt 12 / 14 |
| `11A-OPEN-005` | Can a season exist at all in one persistent, mapless, shared world without splitting the population? | 11B (direction proposed in §20.1/§15.4) |
| `11A-OPEN-006` | Does `URB-119` make wealth-anchored standings structurally anti-development? | Prompt 14 with B-04/B-05 |
| `11A-OPEN-007` | With approval and welfare barred, what is a legitimate political-performance standing? | 11B, under a new decision |
| `11A-OPEN-008` | Should the chronicle be browsable or exportable by period, and at what retention cost? | 11B then Prompt 13 |
| `11A-OPEN-009` | Is a closed-eligibility "first to X" honour fair in a growing world? | 11B |
| `11A-OPEN-010` | Which `WRA-##` types may B-11 legitimately reuse? | 11B |
| `11A-OPEN-011` | Do alliance standings survive k = 5 at plausible alliance sizes? | Prompt 12 / 14 |
| `11A-OPEN-012` | Is there any lawful material reward that avoids `11A-RK-022` compounding, and what does "rare" mean? | Prompt 14 |
| `11A-OPEN-013` | What chronicle quality bar discharges `UD-024`? | 11B |
| `11A-OPEN-014` | Can defensive success be recognised without an attack having occurred? | 11B |
| `11A-OPEN-015` | Are identity-visibility event variants compatible with pair restrictions, moderation evidence and `D-030`? | 11B with Prompt 12 |
| `11A-OPEN-016` | Does the returning-player journey close with the existing digest, or need a distinct re-entry surface? | 11B with Prompt 13 |

---

## 29. Source and citation bibliography

Every URL below was opened on **2026-11-04 or 2026-11-05**; per-entry access dates, revision dates and confidence are in the companion register. **OFFICIAL** = publisher-authored. **COMMUNITY** = community-maintained; never cited as a confirmed developer rule. **OFFICIAL (ARCHIVED)** = publisher-authored content recovered from a dated Internet Archive capture because the live site was inaccessible.

### 29.1 Politics & War — OFFICIAL

`https://politicsandwar.com/rules/` · `/leaderboards/` · `/leaderboards/display=treasures` · `/changelog/` (and `?page=2`, `?page=3`) · `/world/bounties/` · `/world/conflicts/` · `/world-graphs/` · `/nation/id=1` · `/nation/id=300` · `/achievement/166` · `/tools/` · `/pwpedia/index` · categories `nation`, `misc`, `faq`, `basic+guides`, `alliance`, `improvements`, `national+projects` · articles `Score`, `Treasures`, `daily-login-bonus`, `New-Player-Bonus`, `vip-status`, `credits`, `how-do-rewarded-ads-work`, `july-2025-update`, `Moon-Landing`, `Mars-Landing`, `Space-Program`, `Colour-Trade-Blocs`, `Alliance-Positions`, `Alliance-Ranks`, `Alliance-Departments`, `population-cap`, `Average-Income`, `Activity-Center`, `Beige-Buff`, `Factbook`, `War-Policy`, `Continent`, `hall-of-fame`, `what-is-the-api`, `api-faq`, `Terminology-Glossary`. **Blocked:** `/api/` (403), `/achievements/` (403), `/awards/`, `/objectives/`, `/treasures/`, `/events/`, `/history/`, `/news/`, `/bulletins/` (empty), `/tutorial/` (no content).

### 29.2 Politics & War — COMMUNITY

`https://politicsandwar.fandom.com/wiki/` **Nation_Score** (2021-03-26) · **Objectives** (2019-01-29, one revision) · **Achievements** (2023-08-28) · **Awards** (2023-08-01) · **Leaderboards** (2018-08-08) · **Politics_and_War_Awards** (2019-01-20) · **Nation_Formulas** (2018-10-24) · **Treasures** (2017-05-15) · **Moon_Landing** (2022-08-13) · **Mars_Landing** (2023-07-20) · **Vacation_Mode** (2022-08-31, stub) · **Color** (2014-10-10). Revision dates obtained from the site's own MediaWiki API.

### 29.3 NationStates — OFFICIAL (ARCHIVED) and third-party

`https://web.archive.org/web/20261024223020/https://www.nationstates.net/page=faq` · `…/web/2026/https://www.nationstates.net/page=news` · `…/web/2026/…/page=dispatches` · `…/web/20250706171750/…/page=dispatch/id=2677878` · `…/web/2026/…/region=The_Pacific` · `…/web/20240120042653/…/page=world` · `…/web/20190509164917/…/nation=simamerica/detail=trend?censusid=0` · `…/web/2026/…/pages/api.html` · `…/web/2026/…/page=wasec` · `…/web/2024/https://forum.nationstates.net/viewtopic.php?f=15&t=356700` · `…/web/2025/…viewtopic.php?f=12&t=330760` · official news posts `…/page=news/2026-08-19/index.html`, `…/2025-07-24/`, `…/2026-03-30/` · Jolt archive mirror of the 2006 influence thread `https://nationstates.ermarian.net/jolt/1224/477177`. **COMMUNITY:** `https://nationstates.fandom.com/wiki/` Regional_Influence · World_Census · Issue · List_of_issues · WA_Delegate · World_Assembly · General_Assembly · Security_Council · Region · World_Assembly_Category · Political_spectrum · Raiding_and_Defending · Banlist · Boneyard · Nation; `https://wiki.npowned.net/view/Region_(NationStates)`; `https://nsindex.net/`. **THIRD-PARTY:** `https://en.wikipedia.org/wiki/NationStates`. **Blocked live:** `www.nationstates.net` and `forum.nationstates.net` (403 challenge).

### 29.4 Supremacy 1914 — OFFICIAL

Help centre `https://bytro.helpshift.com/hc/en/3-supremacy-1914/faq/` articles `1-how-do-i-win-a-game-round`, `268-game-rules`, `2-what-are-game-rounds-and-how-do-they-work`, `4-what-is-morale…`, `47-how-do-i-acquire-more-resources…`, `43-i-won-a-game-round…`, `3-what-are-goldmarks`, `19-what-is-premium`, `132-all-about-ad-rewards`, `107-everything-about-alliances`, `206-i-can-t-accept-applications…`, `16-why-can-t-i-join-a-new-game`, `34-how-do-i-leave-or-delete…`, `131-what-do-the-diplomatic-relations-mean`, `7-what-is-diplomacy…`, `44-spies-and-espionage`, `537-heroes-and-how-they-work`, `279-how-do-i-report-multiaccounting`, `649`/`573`/`570` dated release notes. Official Game Manual (legacy, read-only) `https://forum.supremacy1914.com/index.php?` `2-joining--creating-games-en`, `3-governing-your-country-en`, `4-economy-en`, `6-warfare-en`, `7-diplomacy-en`, `9-goldmark--premium-account-en`. Official news `https://www.playsupremacy.com/en/news/1914/` `knights-of-the-sky`, `tip-of-the-spear`, `end-of-the-spear`, `1914-battle-pass-operation`, `1914-the-hero-pass-returns`, `supremacy-turns-17`; `https://www.playsupremacy.com/en/terms`. Official mirrored Steam announcements for app 979920. **COMMUNITY:** `playsupremacy.com/en/forums/…` IoP FAQ, rewards and victory-condition threads; `forum.supremacy1914.com/forum/…` threads 17, 743, 754, 7501. **Blocked:** `supremacy1914.com` (login shell), `supremacy1914.fandom.com` (403).

### 29.5 Travian: Legends — OFFICIAL

`https://support.travian.com/en/articles/` `16-daily-quests`, `168-how-medals-work`, `229-season-pass-missions-and-rewards`, `17-task-system`, `51-culture-points-cp`, `174-passive-culture-points`, `103-wonder-of-the-world`, `106-special-servers-ancient-powers-and-victory-points`, `12-beginner-s-protection`, `107-travian-tournament-overview`, `108-travian-tournament-game-worlds-setup`, `109-travian-tournament-prizes`, `236-travian-tournament-finals-entry-key`, `140-how-to-avoid-getting-farmed`, `69-farm-lists`, `185-oasis-farming-after-beginner-protection`, `190-early-game-oasis-farming`, `5-the-romans-and-their-advantages`, `33-buildings-and-resource-fields-statistics`; `https://support.travian.com/sitemap.xml` (slug discovery). **COMMUNITY:** `https://travian.fandom.com/wiki/` Quests (2019-02-21), Tasks_(t4) (2016-01-09), End_game (2023-12-02), World_Wonder (2023-03-08), Culture_points (2021-01-11), Beginner's_Guide (2026-02-14), Travians_Tribes (2026-07-03), Tournament_square, Population, Medals (empty redirect). **Blocked:** `www.travian.com/international/help` (JS shell), `support.travian.com/hc/en-us` (404).

### 29.6 eRepublik — OFFICIAL and COMMUNITY

`https://www.erepublik.com/`; `https://wiki.erepublik.com/index.php/` Military_rank, One:Military_rank, Military_unit, War, Congress, Congress_elections, Elections, Presidential_elections, President, Party, Party_president, Politics, Gold, Company, Newspaper, Decorations, Latest_Game_Changes, United_States_Army, United_States_Army_Group_East, United_States_Army_High_Command; `https://www.erepublik.com/ru/main/latest-updates/0/329`, `…/en/main/latest-updates/0/204`, `…/0/208`; player-authored in-game articles `…/en/article/2494942` and `…/2676982`. **Blocked:** `ERU` (404), `Nation` (404), `Battle` (403), `Company` (disambiguation), `Country` (no statistics).

### 29.7 Call of War and Tribal Wars — OFFICIAL

`https://wiki.callofwar.com/wiki/VICTORY_CONDITIONS`, `…/RESEARCH`; `https://bytro.helpshift.com/hc/en/4-call-of-war/faq/196-game-rules/` and the help index; `https://support.innogames.com/kb/TribalWars/en_DK/1264`, `/5970`, `/6995/World-Types-in-Tribal-Wars`, `/kb/TribalWars2/en_DK/1536`; `https://www.tribalwars.us/page/rules`; `https://www.innogames.com/games/tribal-wars/`. **COMMUNITY:** `https://forum.callofwar.com/index.php?thread/20901-victory-conditions/`; `https://forum.tribalwars.us/index.php?threads/winning-condition.5534/`; `https://forum.tribalwars.net/index.php?threads/summer-special-2026.294215/` and `…/victory-conditions.159560/`; `https://en.wikipedia.org/wiki/Travian` (culture-point cross-reference only). **Blocked:** `callofwar.fandom.com` (403), `www.callofwar.com` (SPA shell).

**Aggregate:** **114 source rows** — **82 official** (73 retrieved live and 9 recovered from dated archive captures), **25 community**, **3** player-authored-on-official-platform, **1** third-party, and **3** rows recording blocked surfaces as gaps — across **7 games**, with **21** documented inaccessible-source entries in §5.4 and seven further per-game gap lists in the companion register. Per-row classification, access date, revision date and confidence are in the companion register.

---

## 30. Final 11A acceptance report

**Required status:** **PASS — COMPLETE AT THE RESEARCH AND DESIGN-FOUNDATIONS LEVEL.**

Every gate below was evaluated against the **final** working tree on **2026-11-05**, after the register repairs and the document
synchronization described in §32 and §33. `NOT RUN` is used where a check was not executed; nothing is inferred upward. No gate
became PASS because this table was written.

| Gate | Required result | Status | Evidence actually inspected |
|---|---|---|---|
| **11A-01** | Canonical research document exists | **PASS** | [`11A_world_events_objectives_rankings_progression_research.md`](11A_world_events_objectives_rankings_progression_research.md) — 35 numbered sections in the brief §21 order; validator check 01 passes; `validate_links.py` resolves every relative link inside it |
| **11A-02** | Repository continuity inspected | **PASS** | §3.1 records the branch (`prototype/free-tier-feasibility`), the inspected HEAD (`8f4e20e docs: close Stage 1 and authorize Stage 2`), the full `git status` inventory of modified and untracked files, and the register maxima read at the start (`REQ-703`, `D-143`, `DD-191`, `UD-049`). No reset, revert, deletion, new folder, duplicate repository or archive swap was performed; no commit or push was made |
| **11A-03** | Prompt 10C constraints preserved | **PASS** | Prompt 10C is recorded complete and untouched: `17_warfare_workflows_acceptance.md` mtime **2026-11-04 20:33**, before this pass began, and it appears in no 11A write operation (§34). `verify_warfare_workflows.py` re-runs **49/49** check groups and `--self-test` **58.80s within the 120s bound** with **C3-NF 5/5** and **C3-NA 15/15**; `10B_validate_warfare.py` passes with **73/73 negative fixtures rejected**. `D-143`/`DD-191` and the `WRF-15`–`WRF-19` gap remain as recorded |
| **11A-04** | D-014 followed | **PASS** | §31 records the four autonomy categories. Category A changed nothing; Category B is the eight directions **D-144…D-151 / DD-192…DD-199**; Category C is **P-01…P-12** (provisional, no owner consent implied); Category D took no external, costly or irreversible action. No owner-reserved decision was resolved, silence was never read as consent, and no candidate name was treated as approval |
| **11A-05** | Politics & War deeply researched | **PASS** | **43 source rows** (`11A-RS-001`…`11A-RS-043`) and **22 benchmark-mechanic entries** (`11A-BM-001`…`11A-BM-022`) — deeper than any comparator on **both** measures (largest other entry count: Supremacy 1914 with 15; the largest other row count is NationStates with 22 rows across its two passes). Validator checks 03 and 30 pass |
| **11A-06** | P&W nation score and development examined | **PASS** | `11A-RS-002` (official guide `…/pwpedia/article/Score`), `11A-RS-012` (July 2025 update, score composition change), `11A-RS-024` (World Graphs), `11A-RS-028` (Score Range Calculator); `11A-BM-001`…`11A-BM-004` and the §6 development/score analysis; the wiki's stale score page is kept as `11A-RS-036` **HISTORICAL** and explicitly superseded |
| **11A-07** | P&W objectives and achievements examined | **PASS** | `11A-RS-034`/`11A-RS-035` (community Objectives, single 2019 revision, and Achievements), `11A-RS-025` (live achievement page 166 with completion percentage and dated earners), `11A-RS-027` (live nation page Awards row); `11A-BM-005`…`11A-BM-009`; §13's 16-category objective verdict table |
| **11A-08** | P&W awards and rankings examined | **PASS** | `11A-RS-003` (live leaderboards), `11A-RS-033`/`11A-RS-038` (award taxonomy, HISTORICAL), `11A-RS-026`/`11A-RS-027` (commendation and denouncement counters, badge tooltips), `11A-RS-005` (Treasures leaderboard); `11A-BM-010`…`11A-BM-014`; §14 answers the six ranking questions the brief §7.3 lists |
| **11A-09** | NationStates researched | **PASS** | **22 source rows** across two passes (`11A-RS-082`…`090` and `11A-RS-102`…`114`), **13 entries** (`11A-BM-054`…`059`, `11A-BM-067`…`073`); the live site is blocked, so official content is labelled **OFFICIAL (ARCHIVED)** with dated Internet Archive captures, and the negative findings (no achievement system, no composite national rating) are recorded as findings rather than gaps |
| **11A-10** | Supremacy 1914 researched | **PASS** | **17 source rows** (`11A-RS-044`…`060`) and **15 entries** (`11A-BM-023`…`037`), all numeric values from the read-only staff Game Manual marked **HISTORICAL**; §8.3 lists the **13 geographic dependencies** excluded as mapless-non-conforming |
| **11A-11** | Travian: Legends researched | **PASS** | **11 source rows** (`11A-RS-091`…`101`) and **7 entries** (`11A-BM-060`…`066`) from the official Help Center (`https://support.travian.com/en/articles/…`, discovered through the publisher's own sitemap after `/hc/en-us` returned 404); the blocked official surfaces are recorded, not guessed |
| **11A-12** | eRepublik researched | **PASS** | **10 source rows** (`11A-RS-072`…`081`) and **6 entries** (`11A-BM-048`…`053`) plus a 23-item evidence-gap list; the official wiki's `Latest Game Changes` index is marked **HISTORICAL** (last entry day 5,874, index dated 2023-12-31) |
| **11A-13** | At least two additional games researched | **PASS** | **Call of War** (`11A-RS-061`…`065`, `11A-BM-038`…`041`) and **Tribal Wars** (`11A-RS-066`…`071`, `11A-BM-042`…`047`, including the negative finding that Tribal Wars has **no culture victory** — the brief's premise was corrected, and the culture-point mechanic belongs to Travian). §11 states the selection rationale; validator check 05 passes |
| **11A-14** | World events research complete | **PASS** | §12: a seven-class taxonomy (A–G), a 15-stage event lifecycle, a 12-question governance table, timing/cadence analysis and the recommended architecture; the lifecycle section carries the **P6 ordering answer** the brief §7.1 requires |
| **11A-15** | Objectives and challenges research complete | **PASS** | §13: a 16-category verdict table, the objective lifecycle, nine design principles, the harm table and the reward analysis |
| **11A-16** | Rankings research complete | **PASS** | §14: ranking categories assessed against what our subsystems actually expose, methodology, fairness and eligibility, snapshots, tie-breaking, historical standings and the chronicle, and privacy under **D-027** |
| **11A-17** | Long-term progression research complete | **PASS** | §15: the progression-lifetime analysis, the season/reset question against **FO-024 (Rejected)** and **FO-020 (Deferred)**, the achievement question against the NationStates negative finding, and the return-player journey |
| **11A-18** | Player-type diversity analysis complete | **PASS** | §16 profiles **twelve** player types, each with its motivation, exposure to each domain and the design consequence; validator check 19 passes, including peaceful and non-military progression |
| **11A-19** | Anti-exploit analysis complete | **PASS** | §18 plus **`11A-RK-001`…`11A-RK-028`**, each risk carrying all ten required fields including detection approach, false-positive risk and the acceptance test it implies. §18 and §27 keep the **sanction** question with Prompt 12; **no moderation punishment is invented** |
| **11A-20** | B-02 through B-10 integration analysis complete | **PASS** | §17.1–§17.9 gives one subsection per Bible part (B-02, B-03, B-04, B-05, B-06, B-07, B-08, B-09, B-10) plus §17.10 for downstream prompts, backed by the **40-row `11A-INT` matrix** and the **`V-01`…`V-18`** violation register; validator check 17 passes |
| **11A-21** | All important research claims have evidence | **PASS** | Every `11A-BM` entry carries a `11A-RS` cross-reference and a confidence grade; validator checks 08 and 11 pass (73/73). Where evidence was thin the entry says so: 6 entries are graded Low/UNVERIFIED and 15 remain HISTORICAL |
| **11A-22** | Official and community sources distinguished | **PASS** | Every `11A-RS` row is labelled **OFFICIAL**, **OFFICIAL (ARCHIVED)**, **COMMUNITY**, **PLAYER-AUTHORED** or **THIRD-PARTY**, or sits under a subsection that declares the class once; validator check 06 finds no unclassified row. **No community statement is presented as a confirmed developer rule** |
| **11A-23** | Current and historical mechanics distinguished | **PASS** | Every source row carries **CURRENT**, **HISTORICAL** or **UNVERIFIED** with its access date; revision dates were taken from each site's own MediaWiki API (and corrected mid-pass after an initial query returned creation dates); validator checks 07 and 10 pass |
| **11A-24** | Comparative research matrix complete | **PASS** | §19: **7 games × 8 comparison columns**, validator check 13 passes |
| **11A-25** | Alternative design models evaluated | **PASS** | §20.1–§20.4: four design areas, **six options each** (24 alternatives), with the rejection reasons stated; validator check 14 passes |
| **11A-26** | Four design areas have recommendations | **PASS** | §21.2–§21.5 give one fifteen-field recommended-direction block per area, and §21.6 lists **`11A-DR-001`…`11A-DR-034`**; validator check 15 passes and check 28 confirms every recommendation is referenced by the registers and every reference resolves |
| **11A-27** | Numerical calibration deferred to Prompt 14 | **PASS** | No value in this deliverable is adopted as a Nation Supremacy number. Comparator figures are recorded as **evidence of shape only**; §24 and §27 route every threshold, weight, window, band, cadence and payout to **Prompt 14**, and §23 lists them as **P-01…P-12** provisional dependencies |
| **11A-28** | Requirements and decisions traced | **PASS** | **30 candidate requirements** (`11A-CR-001`…`11A-CR-030`), each with its owning subsystem and conversion note for 11B; **8 decisions** (`D-144`…`D-151`) with mirrored positions (`DD-192`…`DD-199`). No global `REQ-` or `UD-` ID was allocated — validator check 29 confirms `REQ-703` remains the maximum |
| **11A-29** | Prompt 11B handoff complete | **PASS** | §25 (validator check 21): what 11B must write, what it inherits unchanged, the candidate-requirement conversion list, the `TR-042`/B-02 annotation it must make, the register allocation it owns and the items it must not silently decide |
| **11A-30** | Prompt 11C handoff complete | **PASS** | §26 (validator check 22): the workflow, edge-case and acceptance scope 11C owns, explicitly recorded as **designed, not executed** and **not started** |
| **11A-31** | Prompt 12–15 dependencies documented | **PASS** | §27.1–§27.4 (validator check 23): one subsection each for Prompt 12 (protection, privacy, moderation of event and ranking abuse), Prompt 13 (screens, journeys and disclosure), Prompt 14 (calibration of every number) and Prompt 15 (assembly and traceability) |
| **11A-32** | No unauthorized changes to B-02 through B-10 | **PASS** | The B-02…B-10 rulebooks and registers all carry modification times **on or before 2026-11-04** (§3.1 and the §34 record): `07_` 11:57, `09_` 12:21, `10_` 11:12, `11_` 12:08, `12_` 10:38, `13_` 2026-10-29, `14_` 2026-10-29, `15_` 12:03, `16_` 2026-11-03, `17_` 11:59/12:00/20:33. Their validators re-run green (`verify_politics_numbers` **879/879**, `verify_city_numbers` **267/267**, `verify_economy_numbers` **164/164**, `verify_market_*`, `verify_diplomacy_*`, `verify_alliance_*`, `10B_validate_warfare`, `verify_warfare_workflows`). Validator check 24 confirms no fixed mechanic is described as modified |
| **11A-33** | Research validator/checklist passes | **PASS** | `python 11A_validate_research.py` → **CHECKS: 30 EXECUTED: 30 FAILED: 0** and `RESULT: PASS`; `--self-test` → **8/8 seeded defects detected**. §32.4 states what the checker cannot prove, and the manual-review items are named there rather than claimed as automated coverage |
| **11A-34** | Documentation links pass | **PASS** | `python validate_links.py` → **69 files, 3202 links, 2820 local, 382 external skipped, 29 anchors, Unresolved: 0**; `--self-test` → `[PASS] exactly three fixtures fail`. Twelve report links that omitted the `../` prefix, and the same class of error in the registers, were repaired before this gate could be recorded; validator check 26 passes independently |
| **11A-35** | Project-wide handoffs and status records synchronized | **PASS** | §33 lists the twelve updated project documents. `validate_final.py` **ALL CHECKS PASSED**, `09_validate.py` **359/359**, `test_next_action.py` **27 tests OK**, `test_decision_registers.py` **12 tests OK**, `09A_validate_alliance.py` **943**, `09B_validate_alliance_semantic.py` **34/34**. All three STATUS blocks read `stage_2_next_prompt: 11B`, `decisions_range: D-001..D-151`, `status_updated: 2026-11-05`; **11B and 11C are not marked complete and Prompt 11's parent is recorded as open** |
| **11A-36** | Final research evidence supports PASS | **PASS** | The evidence above is the basis: 114 sourced rows across 7 games with the primary benchmark deepest, 73 traceable mechanic entries, four researched domains, 40 integration rows, 28 risks, 30 candidates, 16 open questions, 34 recommendations, 24 evaluated alternatives and 8 recorded directions — with **no implementation, no number adopted, no owner-reserved decision resolved and no gate claimed satisfied**. The one suite that could not finish is reported **NOT RUN** (§32.5) instead of being counted as evidence |

**Gate tally:** **36 PASS / 0 FAIL / 0 BLOCKED / 0 NOT RUN** at gate level. At *test* level the honest record is different and is kept visible: the 267-test
historical `test_09B_alliance_semantic_validator.py` remains **NOT RUN**, and **no gameplay, runtime, database, browser, load, security or
playability test exists or was executed**.

**Verdict.** **PASS — COMPLETE AT THE RESEARCH AND DESIGN-FOUNDATIONS LEVEL.** Research and design foundations only: **Prompt 11B is
next**, Prompt 11C follows it, and **implementation authorization for Prompt 11A was NONE and none was performed.**

---

## 31. D-014 autonomous decision policy compliance

[`../../AUTONOMOUS_DECISION_POLICY.md`](../../AUTONOMOUS_DECISION_POLICY.md) was read in full before research began and applied throughout.

### 31.1 Category A — fixed constraints respected

No fixed constraint was overridden, relaxed or reinterpreted. The ones most likely to be breached by this subject matter were checked explicitly and all remain intact: the **mapless world** (no province, territory, distance or adjacency mechanic is recommended anywhere; §8.3 and §11.2 list the exclusions instead); the **2-hour / 12-turn cadence** (every timing recommendation is expressed in turns and named boundaries — §12.4, `11A-CR-026`); **free-first ₹0** (the archive recommendation is shaped by it, §14.6, and no real-money prize or paid reward is proposed, §9.3, `11A-DR-012`); **one authoritative scheduler** (no event machinery introduces a second cron, `11A-INT-01`); **one account, one nation** (`11A-RK-009` records Travian's dual-crediting as the anti-pattern); **original identity and `AP-008`** (no comparator achievement name, badge, condition, reward table or term is reproduced — §6.4, §9.2); and **Stage 2 is design-only** (no code, migration, schema or hosting change).

### 31.2 Category B — ordinary decisions made autonomously

`D-014` was applied rather than cited: state the question, name two or three realistic alternatives, gather external evidence, check the fixed constraints first, apply the policy §4 priority order, choose, record and propagate. No owner decision was requested for any of them.

The **benchmark selection** was itself a Category B decision: the five mandated games were kept and **Call of War** and **Tribal Wars** were chosen as the two additions on stated relevance grounds — one supplying multiple termination channels and a partly persistent research tree, the other a development-derived standing and a per-mode persistence seam. The brief's other candidate games (OGame, Pulsar, Dominations) were not added merely to raise a count.

Eight positions were promoted to [`../../DECISIONS.md`](../../DECISIONS.md) as **D-144…D-151** with mirrors **DD-192…DD-199** (§22); thirty further recommendations remain `11A-DR-###` candidates that 11B may adopt, modify or reject with a stated reason. They were deliberately **not** all promoted, because `DECISIONS.md`'s own rule 4 reserves that log for material decisions. The identifier policy itself — no `11A-DEC`, no early `REQ-` allocation, `11A-CR` candidates instead — is recorded as **D-145**, following the 08A/09A/10A precedent rather than inventing a convention.

### 31.3 Category C — provisional decisions

Twelve provisional working assumptions are recorded in §23, each with the specific evidence that would confirm or replace it, and each labelled rather than presented as settled. **Prompt 14 retains numerical calibration ownership:** no threshold, weight, cap, interval, band bound, tier spacing or payout in this report is a value, and each is classified as structural, candidate, provisional or a Prompt 14 dependency (§27.3). Where a question cannot be answered from documents — cadence adequacy, k = 5 sufficiency, rate behaviour under world growth — the answer is deferred with a named test rather than invented, and no deferral is dressed as an owner question.

### 31.4 Category D — owner-only matters preserved

No owner approval was invented and no silence was read as consent. `UD-040`…`UD-049` remain open; `UD-024` remains deferred to Prompt 11 and is **not** marked resolved here; `D-027` and `D-021` are reused verbatim rather than re-derived; the Global Trade gates remain unmet with no readiness claim made; the Stage 1 `OSQ-…` security owner questions pass to Prompt 12 untouched. §24 lists every such dependency with the handling 11B must apply. Nothing ordinary was escalated to the owner; nothing owner-reserved was dressed as ordinary.

### 31.5 Explicit player sovereignty — authoring autonomy distinguished from in-game autonomy

These are different things and this report keeps them apart. **Development AI** made ordinary design choices autonomously under `D-014`. **The game must not decide for a player.**

Four sovereignty guarantees follow from that distinction. Objectives are **never auto-accepted**, and a declined one may return without penalty (§13.2, `11A-DR-009`). **No event, ranking or season may complete, extend, accept, decline or terminate a player action**, because `REQ-523` makes silence, expiry, dormancy and leadership change non-consent — so **no future objective or event may introduce consent by silence**, and an objective's activation is an explicit player act, which is why an auto-enrolment option was rejected outright. **No event may set a political state, resolve an election, remove a leader, command a military action or move an Alliance position** (`DMP-141`, `DMP-266`, `AX-18`, `UD-047`). And automation already approved is respected without extension: B-04's automatic recurring settlement, B-09's automatic per-turn production taxation and B-02's boundary evaluation remain the only automatic paths.

### 31.6 Honesty discipline

Every source row was opened; **114** carry their own access date and currency status; **21** inaccessible-source entries and **95** explicitly unverifiable claims are recorded rather than filled by assumption; no community statement is presented as a developer rule; every recommendation is labelled a candidate; and **11A does not declare itself accepted**. `D-014` §5 forbids a prompt approving its own output by declaring it, so §30 records a gate-by-gate **self-assessment** with the acceptance decision left open to the owner and to Prompt 11C's workflow layer.

### 31.7 Tooling gap disclosed, not hidden

`docs/qa_backups/status_rules.py`'s sub-prompt detector matches `0[789]|10` and therefore cannot detect a stale **11A/11B/11C** status claim, and `test_next_action.py` hard-codes the previous prompt's expectations. Extending the detector and updating those assertions is the established convention at each prompt boundary and is done in this pass; the gap is recorded so no later reader mistakes a passing suite for complete coverage of the 11 family (§32.4).

---

## 32. Validation actually performed

This section records only checks that were **executed and inspected**. **Document checks are not gameplay, runtime, database, browser, load, security or playability tests**, and none of those was run, because no events, objectives, rankings or progression exist as software.

### 32.1 Research-integrity checks

| Check | Method | Result |
|---|---|---|
| Every cited source is a page actually opened | Each `11A-RS` row re-read against the page it names; URL, title, access date and revision date re-checked | Complete for all 114 rows; 21 inaccessible entries recorded as gaps rather than cited |
| Official and community status correct | Every row classified; the P&W community wiki is named as community and never called official; NationStates official content labelled **OFFICIAL (ARCHIVED)** with the capture date | Complete |
| Current versus historical separated | Wiki revision dates obtained from each site's own MediaWiki API, not estimated | Complete — and corrected mid-pass, because an initial query returned **creation** dates rather than last-edit dates |
| Findings evidence-backed | Every `11A-BM` entry cites at least one `11A-RS` source row and carries a confidence grade; the 15-field table-form entries additionally state Source, Second source and Exploit-risk fields | Complete for 73 entries — verified by validator checks 08 and 11, after ten prose-form entries were repaired to add the missing cross-reference |
| Disagreements recorded, not resolved silently | P&W stale-wiki-versus-live-guide conflicts; Supremacy 1914's mode-versus-tier threshold conflict; Tribal Wars' building-points-versus-unit-points conflict — each carried as a stated conflict | Complete; no winner invented |
| Negative findings recorded | Tribal Wars has no culture victory; NationStates has no achievement system and no composite national rating; the official P&W guide has no recognition articles; no comparator documents alliance scoring | Complete — four negatives |
| No fabricated citation | No URL is quoted that was not fetched; unverifiable specifics (numbers, thresholds, cadences) are marked rather than asserted | Complete |
| Mapless conformance | Every recommended mechanism tested against the ban on provinces, territory, adjacency, borders, movement, distance and geographic control; §8.3 lists 13 excluded geographic dependencies by name | Complete; nothing imported |
| No existing rule modified | B-02…B-10 rule IDs are cited as constraints only; the 18-row violation register checks each recommendation against them | Complete; no rule restated in a competing form |
| Global Trade gate preserved | G-1…G-6 recorded as five not met and one partial; no readiness claim | Complete; nothing marked satisfied |
| Owner-reserved decisions preserved | `UD-024` still deferred; `UD-040`…`UD-049` untouched; no owner approval inferred | Complete |
| No state-changing action taken | No login, registration, form submission, purchase, trade, message, declaration or API credential used | Complete |
| Register maxima unchanged by 11A | `REQ-703`, `UD-049` intact; `D-151`/`DD-199` are this pass's eight direction decisions and nothing else | Complete |

### 32.2 11A research-quality validator

`docs/qa_backups/11A_validate_research.py` implements the brief §24 checklist as **30** machine checks (the 26 required plus
identifier-integrity, cross-reference-resolution, register-maxima and primary-depth checks). Run against the final working tree on
**2026-11-05**:

| Command | Result |
|---|---|
| `python 11A_validate_research.py` | **CHECKS: 30 EXECUTED: 30 FAILED: 0** — `RESULT: PASS — 11A research-quality checks satisfied (documentation only; no rule approved, no implementation executed)`, exit **0**, 0.63s |
| `python 11A_validate_research.py --self-test` | **SELF-TEST: 8/8 seeded defects detected** — domain-section deletion (check 02), identifier-range removal (27), a gate falsely marked met (24), an implementation claim (25), a deleted risk row (18), a dangling recommendation reference (28), stripped access dates (10) and a broken internal link (26). Exit **0**, 3.83s |

Two classes of failure were found by the **first** execution of this validator and repaired rather than waived. The checker itself was
wrong in four places — a heading extractor that did not run in multiline mode, an integration-matrix count that double-counted the
deliberate two-part field split, a gate regex that matched the honest phrase "**not met**", and an implementation-claim regex that
matched "**Nothing** is implemented" — and each of those four corrections was re-proven by the seeded self-test, which still detects
every defect it used to detect. The documents were genuinely wrong in three places, and those were fixed in the documents:
**twelve relative links** in this report omitted the `../` prefix for `docs/stage-2/` targets, **several source rows** carried only a
shorthand or no locator at all (the Politics & War changelog rows now cite the dated feed
`https://politicsandwar.com/changelog/`, whose per-post URL was checked and does not exist, so the post title and date are the
locator), and **ten benchmark entries** described a mechanic without pointing at the rows that evidence it, so each now opens with

### 32.3 Existing validators re-run

Every project validator that touches the changed files was re-run on the final tree, so that this pass cannot silently break earlier
work. Full command list and timings in §32.5.

| Validator | Result |
|---|---|
| `validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `09_validate.py` | **359/359** checks passed |
| `09A_validate_alliance.py` | **943** checks, `PASS` |
| `09B_validate_alliance_semantic.py` | **34/34** semantic checks, `[PASS] … no review findings` |
| `test_09A_alliance_validator.py` | **43 tests OK** |
| `test_next_action.py` | **27 tests OK**, including the new 11A/11B guards and the 11-family detector test |
| `test_decision_registers.py` | **12 tests OK**, including the new Stage 2 Prompt 11 row assertions |
| `verify_politics_numbers.py` | **879/879** |
| `verify_economy_numbers.py` | **164/164** |
| `verify_city_numbers.py` | **267/267** |
| `verify_alliance_numbers.py` | **375 passed, 0 failed** |
| `verify_diplomacy_numbers.py` | **9 groups, 0 failed** |
| `verify_market_numbers.py`, `verify_market_workflows.py` | `ALL CHECKS PASSED`, `07C VALIDATION: ALL CHECKS PASSED` |
| `verify_diplomacy_workflows.py` | **17 groups** (30 workflows, 54 edge cases, 88 tests), 0 failed |
| `verify_alliance_workflows.py` (+ `--self-test`) | `ALL CHECKS PASSED` (49 workflows, 65 edge cases, 132 tests); self-test detects every seeded defect |
| `10B_validate_warfare.py` | `PASS`; **73/73 negative fixtures rejected**; CF-01 and CF-02 clean fixtures pass |
| `verify_warfare_workflows.py` (+ `--self-test`) | **49/49** check groups; self-test **58.80s within the 120s bound**, **C3-NF 5/5**, **C3-NA 15/15**, skipped 0 |
| `validate_links.py` (+ `--self-test`) | **69 files / 3202 links / 2820 local / 382 external skipped / 29 anchors / Unresolved: 0**; self-test `[PASS] exactly three fixtures fail` |
| `09_register_counts.py` | exit **0**; register inventories emitted |
| `test_09B_alliance_semantic_validator.py` | **NOT RUN** — 267 tests; did not complete within a 180-second bound on this machine. Not counted as evidence and not reported as passing; the 34-check semantic validator above passes |

Advancing the live sub-prompt from `11` to `11B` required **status-expectation maintenance**, the same class of edit Prompt 10C
recorded for itself: `status_rules.py` (the sub-prompt detector now covers `1[01][A-C]`, `11A` joins `COMPLETED_SUBPROMPTS`,
`CURRENT_SUBPROMPT = "11B"`), and the literal current-status expectations in `test_next_action.py`, `test_decision_registers.py`,
`09_validate.py`, `validate_final.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py` and
`10B_validate_warfare.py`, plus the pending-prompt count (rows **12–15**). **Nothing was deleted, no assertion was weakened in order
to pass, and no fixture was dropped**: the widened patterns still reject a stale sub-prompt, and the self-tests above

### 32.4 Known limits of these checks

A document checker proves **presence, traceability, internal consistency and correct status language**. It cannot prove that the research is *correct*, that a recommended design is *fun*, that a metric is *balanced*, that a control *resists a determined colluder*, or that any of this is *implementable at the projected cost*. Three specific gaps are named rather than glossed: the `status_rules.py` detector had to be extended to see the 11 family (§31.7); **human review is still required** for the judgement-heavy items — whether §21's four directions are the right ones, whether §16's twelve-profile assessment is credible, and whether the 30 candidate requirements are worth specifying at all; and the 26-check brief list is satisfied by machine **only** for the structural items, with the rest covered by the §32.1 manual re-reads recorded above.

### 32.5 Executed commands and results

All commands run from `docs/qa_backups/` against the final working tree on **2026-11-05**. Timings are wall-clock and
machine-specific.

| Command | Result | Exit | Time |
|---|---|---|---|
| `python 11A_validate_research.py` | **CHECKS: 30 EXECUTED: 30 FAILED: 0** | 0 | 0.63s |
| `python 11A_validate_research.py --self-test` | **8/8 seeded defects detected** | 0 | 3.83s |
| `python validate_final.py` | `ALL CHECKS PASSED` | 0 | 1.03s |
| `python 09_validate.py` | **359/359** | 0 | 0.66s |
| `python 09A_validate_alliance.py` | **943 checks** | 0 | 0.27s |
| `python 09B_validate_alliance_semantic.py` | **34/34**, no review findings | 0 | 7.45s |
| `python test_09A_alliance_validator.py` | **43 tests OK** | 0 | 9.39s |
| `python test_next_action.py` | **27 tests OK** | 0 | 0.35s |
| `python test_decision_registers.py` | **12 tests OK** | 0 | 0.21s |
| `python 09_register_counts.py` | inventory emitted | 0 | 2.01s |
| `python verify_economy_numbers.py` | **164/164** | 0 | 0.11s |
| `python verify_city_numbers.py` | **267/267** | 0 | 0.12s |
| `python verify_politics_numbers.py` | **879/879** | 0 | 0.19s |
| `python verify_alliance_numbers.py` | **375 / 0 failed** | 0 | 0.23s |
| `python verify_diplomacy_numbers.py` | **9 groups / 0 failed** | 0 | 0.12s |
| `python verify_market_numbers.py` | `ALL CHECKS PASSED` | 0 | 0.14s |
| `python verify_diplomacy_workflows.py` | **17 groups / 0 failed** | 0 | 0.17s |
| `python verify_market_workflows.py` | `07C VALIDATION: ALL CHECKS PASSED` | 0 | 0.33s |
| `python verify_alliance_workflows.py` | `ALL CHECKS PASSED` | 0 | 0.45s |
| `python verify_alliance_workflows.py --self-test` | every seeded defect detected | 0 | 7.54s |
| `python validate_links.py` | **Unresolved: 0** (69 files, 3202 links, 2820 local, 382 external skipped, 29 anchors) | 0 | 2.14s |
| `python validate_links.py --self-test` | `[PASS] exactly three fixtures fail` | 0 | 0.21s |
| `python 10B_validate_warfare.py` | `PASS`; **73/73 negative fixtures rejected** | 0 | 0.17s |
| `python verify_warfare_workflows.py` | **49/49** check groups | 0 | 25.52s |
| `python verify_warfare_workflows.py --self-test` | `PASS`; **58.80s / 120s bound**; 49 checks, 13 positive, 67 negative, 10 N/A, **C3-NF 5/5**, **C3-NA 15/15**, 0 skipped | 0 | 59.29s |
| `python test_09B_alliance_semantic_validator.py` | **NOT RUN** — did not complete within a 180-second bound; not counted as evidence | — | 180s bound |

---

## 33. Files created and updated

| File | Change |
|---|---|
| [`docs/stage-2/research/11A_world_events_objectives_rankings_progression_research.md`](11A_world_events_objectives_rankings_progression_research.md) | **Created** — the canonical 11A deliverable, 35 sections |
| [`docs/stage-2/research/11A_comparator_sources_and_benchmarks.md`](11A_comparator_sources_and_benchmarks.md) | **Created** — 114 source rows, 73 benchmark-mechanic entries across 7 games |
| [`docs/stage-2/research/11A_integration_and_risk_registers.md`](11A_integration_and_risk_registers.md) | **Created** — 40 integration rows, 18 violations, 28 risks, 30 candidate requirements, 16 open questions |
| [`docs/qa_backups/11A_validate_research.py`](../../qa_backups/11A_validate_research.py) | **Created** — 30-check research-quality validator with an 8-defect self-test |
| [`docs/DECISIONS.md`](../../DECISIONS.md) | **Updated** — D-144…D-151 added; header "Last updated" refreshed with the 11A record |
| [`docs/stage-2/04_approved_and_provisional_decisions.md`](../04_approved_and_provisional_decisions.md) | **Updated** — DD-192…DD-199 added; tallies and the D-001…D-151 range corrected |
| [`docs/stage-2/06_stage_2_progress_log.md`](../06_stage_2_progress_log.md) | **Updated** — new §67 Prompt 11A record; status header and prompt table advanced |
| [`docs/stage-2/00_stage_2_handoff.md`](../00_stage_2_handoff.md) | **Updated** — next action is Prompt 11B; 11A recorded complete at research level |
| [`docs/stage-2/01_stage_2_prompt_roadmap.md`](../01_stage_2_prompt_roadmap.md) | **Updated** — Prompt 11 row gains its 11A/11B/11C sub-prompt register |
| [`docs/stage-2/02_master_game_design_bible_outline.md`](../02_master_game_design_bible_outline.md) | **Updated** — B-11 row links the 11A research and records its status; version and current-state rows advanced |
| [`docs/stage-2/05_unresolved_design_decisions.md`](../05_unresolved_design_decisions.md) | **Updated** — `UD-024` annotated: 11A supplied a direction, the bar remains with 11B, status unchanged |
| [`docs/AI_CONTEXT.md`](../../AI_CONTEXT.md), [`docs/AI_HANDOFF.md`](../../AI_HANDOFF.md), [`docs/PROJECT_PROGRESS.md`](../../PROJECT_PROGRESS.md), [`docs/ROADMAP.md`](../../ROADMAP.md) | **Updated** — STATUS blocks to `stage_2_next_prompt: 11B`, current-status prose, document index rows |
| [`docs/qa_backups/status_rules.py`](../../qa_backups/status_rules.py), [`docs/qa_backups/test_next_action.py`](../../qa_backups/test_next_action.py) | **Updated** — sub-prompt detector extended to the 11 family; `11A` added to the completed set; `CURRENT_SUBPROMPT = "11B"`; next-action assertions moved to 11B and two new 11-family guard tests added (27 tests, all pass) |
| [`docs/qa_backups/09_validate.py`](../../qa_backups/09_validate.py), [`docs/qa_backups/validate_final.py`](../../qa_backups/validate_final.py), [`docs/qa_backups/09A_validate_alliance.py`](../../qa_backups/09A_validate_alliance.py), [`docs/qa_backups/09B_validate_alliance_semantic.py`](../../qa_backups/09B_validate_alliance_semantic.py), [`docs/qa_backups/10B_validate_warfare.py`](../../qa_backups/10B_validate_warfare.py), [`docs/qa_backups/test_decision_registers.py`](../../qa_backups/test_decision_registers.py) | **Updated — status-expectation maintenance only.** Each literal current-status expectation advanced with the live sub-prompt (`11` → `11B`), the decision range (`D-143` → `D-151`), the position range (`DD-191` → `DD-199`), the DD tallies (199 / 12 Confirmed), the project-decision count (151) and the pending-prompt set (rows 12–15). **No check was deleted, no assertion weakened to pass and no fixture dropped**; every widened pattern still rejects the stale case, and the suites' own self-tests still detect every seeded defect |
| Scratch removal | This session's throwaway research dumps (`.research_tmp/`, `.tmp_extract_tw.py`) and the generated `docs/qa_backups/__pycache__/` were deleted. They were created by this session, are untracked, are referenced by no document, and their presence failed the project's own "no code outside `docs/qa_backups/` and `prototypes/`" boundary check. **No pre-existing project file was deleted** |

## 34. Files intentionally not changed

| File or set | Why untouched |
|---|---|
| `docs/stage-2/17_warfare_and_settlements.md`, `17_warfare_formula_register.md`, `17_warfare_workflows_acceptance.md` | B-10 is complete and accepted at the specification/documentation level; 11A consumes its rules and the `WAR-147` hand-off and changes nothing |
| `07_…` (B-02), `09_…` (B-03), `10_…`/`11_…` (B-04/B-05), `12_…` (B-06), `13_…`/`14_…` (B-07), `15_…` (B-08), `16_…` (B-09) | Accepted subsystem rulebooks. 11A cites them as constraints; `TR-042`'s annotation belongs to 11B, which will write the rule that disposes of it |
| `docs/stage-2/03_requirements_traceability.md` | No global `REQ-` row is allocated by a research prompt (D-145); 11B allocates `REQ-704` onward for what it actually specifies |
| `docs/stage-1/…` | Stage 1 is CLOSED; its reports stay the evidence base and keep their internal numbering |
| `docs/stage-2/research/04_…`…`10A_…` | Prior research is not rewritten; §2.4 explains where 11A extends rather than duplicates it |
| `prototypes/…`, hosting resources, Supabase, Cloudflare | Stage 2 is design-only; no code, migration, deployment or hosting change was made or authorised |
| Existing modified and untracked working-tree files | All 65 pre-existing entries were preserved; nothing was reset, reverted, stashed, committed or pushed |

## 35. Limitations

1. **Research level only.** This document specifies no rule. Its four directions, 34 recommendations and 30 candidate requirements become normative only if Prompt 11B writes them into `18_world_events_and_progression.md` and records the decisions.
2. **No number is chosen**, deliberately: cadences, band bounds, weights, thresholds, caps, durations, tier spacings, season lengths and every payout are Prompt 14's. A reader cannot compute an outcome from this report, and that is the intended state.
3. **Official access varied by publisher**, and it materially changed what can be claimed. NationStates' live site is blocked, so its official content comes from dated archive captures. Supremacy 1914's wiki is blocked and its site is a login shell, so all of its numeric detail is legacy-manual and HISTORICAL. eRepublik's changelog appears frozen at ~2023-12-31 and its `ERU`/`Nation` pages 404, so its national-ranking and cash-out claims are **unverified** rather than absent. Call of War's and Tribal Wars' community and rankings documentation were partly unreachable. **95 unverifiable claims and 21 inaccessible-source entries are listed rather than filled in.**
4. **Login-gated surfaces could not be examined at all**, which leaves two gaps that matter to this subject: the current Politics & War objectives screen and its award-issuance behaviour (`11A-OPEN-001`, `11A-OPEN-002`), and alliance scoring in every game that claims one.
5. **Community evidence is bounded by its own maintenance.** The five suggested P&W wiki starting points are three to eight years stale; one has a single revision. Where live official pages existed they replaced the wiki, which is why this report's P&W evidence is mostly live-official — but the Awards category list, the achievement catalogue and the objective list remain community-and-historical, and are used as such.
6. **Single author.** Like [`09A_alliance_reference_review.md`](09A_alliance_reference_review.md), this is one author's synthesis; the semantic judgements — that four layers rather than three, that authorship is the right top reward class, that seasons must be in-place — are argued from evidence but not independently reviewed. They are flagged as manual review items in §32.4.
7. **No population, cadence or balance data exists.** The recommendations that depend on world size, event frequency or rate behaviour are provisional by necessity (§22), and k = 5 viability, snowball behaviour and cadence adequacy remain simulation and measurement questions rather than open owner questions.
8. **Comparators are evidence, not authority.** Several studied mechanics are explicitly rejected here because our own rules exclude them (presence rewards, deletion of absent nations, prestige currency, purchased rights, real-money prizes, geographic objectives). Where a comparator's practice and an accepted Nation Supremacy decision conflict, the decision wins and the conflict is recorded.
9. **No gameplay implementation, runtime test, migration or release exists or is authorised.** Everything in this report is documentation.

---






