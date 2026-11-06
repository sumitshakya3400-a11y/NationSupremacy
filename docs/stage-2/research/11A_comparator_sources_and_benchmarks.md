# Prompt 11A comparator evidence — source register and benchmark mechanics

**Version:** 1.0 · **Created:** 2026-11-05 · **Stage 2, Prompt 11A** · **Research and documentation only**
**Status:** Research evidence record. **This file approves no Nation Supremacy rule.** Every entry describes an **observed mechanic in another game** or an **interpretation/design lesson drawn from it**. A recommendation is always labelled as such and is carried in the main report as `11A-DR-###`, never as a rule.
**Parent document:** [`11A_world_events_objectives_rankings_progression_research.md`](11A_world_events_objectives_rankings_progression_research.md) — this file is its evidence register and is linked from there (§5, §6–§11).
**Research execution dates:** Politics & War, Call of War and Tribal Wars were examined on **2026-11-04/05**; NationStates, Supremacy 1914, Travian: Legends and eRepublik on **2026-11-05**. Each row carries its own access date.
**Identifier spaces:** sources **`11A-RS-###`**; benchmark mechanics **`11A-BM-###`**. Neither collides with the project's `D-`, `DD-`, `UD-`, `REQ-`, `TR-`, `NAT-`, `ONB-`, `RRL-`, `ECN-`, `URB-`, `DMP-`, `MKT-`, `DIP-`, `ALL-`, `WAR-`, `WRA-`, `WFS-`, `WFR-`, `PWS-`, `DPS-` or `ALS-` spaces. These are **research identifiers, not decisions or registered requirements**.

---

## 1. How to read this file

Each `11A-BM-###` entry uses the fields required by the Prompt 11A brief §5.3: game, system, mechanic, how it works, trigger, eligibility, timing, scoring, reward, restrictions, strengths, weaknesses, exploit risks, source, evidence confidence and relevance.

Three labels are kept strictly separate throughout:

| Label | Meaning |
|---|---|
| **OBSERVED** | A mechanic that a cited source states. It is a claim about **that game**, not about Nation Supremacy |
| **INTERPRETATION** | The author's reading of why the mechanic behaves as it does. Not a source claim |
| **LESSON / DIRECTION** | A design inference for Nation Supremacy. Always a candidate; never an approved rule |

**Source status** is recorded on every entry:

- **OFFICIAL** — publisher-authored surface (game site, official rules, official in-game guide, official developer changelog or official developer announcement).
- **COMMUNITY** — community-maintained wiki, forum or player article. A community statement is **never** presented here as an officially confirmed developer rule.

**Currency** is recorded on every entry: **CURRENT** (evidence describes the live game at the access date), **HISTORICAL** (the mechanic is documented but its current status is not confirmed) or **UNVERIFIED**.

### 1.1 A note on the suggested research starting points

The Prompt 11A brief names five Politics & War community-wiki pages as starting points. Their actual revision state was checked page-by-page through the wiki's own MediaWiki API rather than assumed. The result materially changes how they may be used:

| Suggested starting point | True last revision | Revisions | Consequence |
|---|---|---|---|
| `Nation_Score` | **2021-03-26** | 9 | Superseded on the point that matters: the official in-game guide now states that military research also contributes to score. **Not used for the formula** |
| `Objectives` | **2019-01-29** | **1** | Never edited since creation. Historical only |
| `Leaderboards` | **2018-08-08** | 5 | Its own edit comments read "this is my current project, it is a major work in progress". Historical and incomplete |
| `Awards` | **2023-08-01** | 84 | Substantive, but three years stale at the access date |
| `Achievements` | **2023-08-28** | 130 | Substantive, but three years stale; its table is not exhaustive |

Where the same mechanic was also reachable on an official live surface, **the official surface is the citation of record** and the wiki row is retained only as a second source or as a historical record. This is why most Politics & War entries below cite `politicsandwar.com` rather than the wiki, despite the wiki pages being named in the brief.

---

## 2. Politics & War source register

Confidence is about **the source**, not the mechanic. Relevance is to Prompt 11's four domains: **Events**, **Objectives**, **Rankings**, **Progression**.

### 2.1 Politics & War — official sources

| ID | Source | Type | Accessed | Currency | Used for |
|---|---|---|---|---|---|
| `11A-RS-001` | **Game & Community Rules**, `https://politicsandwar.com/rules/` — "The Game Rules govern what actions and content are acceptable in the game". Seventeen numbered Game Rules plus Community Rules, each with a **Moderation Points Guideline** and an **Expiration** period | OFFICIAL | 2026-11-04 | CURRENT | Anti-exploit, fair play, ranking manipulation, all four domains |
| `11A-RS-002` | **Nation Score**, official in-game guide (PWPedia), `https://politicsandwar.com/pwpedia/article/Score` — states score's purposes and gives its full arithmetic | OFFICIAL | 2026-11-04 | CURRENT | Rankings, development, war eligibility |
| `11A-RS-003` | **Leaderboards**, live page `https://politicsandwar.com/leaderboards/` — "Top 100 Nations by Score" with the ranked metric list and the leaderboard tabs | OFFICIAL | 2026-11-04 | CURRENT | Rankings, snapshot behaviour, ties |
| `11A-RS-004` | **Treasures**, official in-game guide, `https://politicsandwar.com/pwpedia/article/Treasures` | OFFICIAL | 2026-11-04 | CURRENT | System events, eligibility bands, rewards |
| `11A-RS-005` | **Treasures leaderboard**, live page `https://politicsandwar.com/leaderboards/display=treasures` — per-treasure spawn date, respawn countdown, holder, colour, continent and score | OFFICIAL | 2026-11-04 | CURRENT | Event lifecycle, public tracking, transfer rules |
| `11A-RS-006` | **Changelog**, live developer feed `https://politicsandwar.com/changelog/` — dated posts by named developers, each with a like count; 106 pages | OFFICIAL | 2026-11-04 | CURRENT | World events, seasonal events, monetisation cadence |
| `11A-RS-007` | Changelog entry **"Trick or Treating"** on the dated feed `https://politicsandwar.com/changelog/` (page 1 at access; the feed carries no per-post URL, so the post title and date are the locator), posted 2026-10-25 by DrRush — the live Halloween event specification, including its four event achievements and payouts | OFFICIAL | 2026-11-04 | CURRENT | Event design, per-player limits, cost, escrow |
| `11A-RS-008` | Changelog entries **"Easter Egg Hunt"** and **"Easter Egg Hunt Ending Today"** on the dated feed `https://politicsandwar.com/changelog/`, posted 2026-04-01 by DrRush, with the follow-up **"Easter Egg Hunt Ending Today"** posted 2026-04-14 | OFFICIAL | 2026-11-05 | CURRENT | Annual event, tiered claim rules, expiry, cleanup |
| `11A-RS-009` | Changelog entries **"In-Game Chat & Lottery"** on the dated feed `https://politicsandwar.com/changelog/` (2026-06-12) and **"Chat, Lets go gambling!"** (2026-06-12) — the weekly lottery specification | OFFICIAL | 2026-11-05 | CURRENT | Scheduled recurring event, eligibility, funding model, pre-draw freeze |
| `11A-RS-010` | Changelog entry **"Annual Pumpkin Contest"** on the dated feed `https://politicsandwar.com/changelog/`, posted 2026-10-21 by DrRush — 7thDecoration contest, human-authorship rule, in-game vote | OFFICIAL | 2026-11-04 | CURRENT | Player-driven content event, judging, integrity |
| `11A-RS-011` | Changelog entries **"Donation Limit Reset"** on the dated feed `https://politicsandwar.com/changelog/`, posted 2026-10-01 and 2026-11-01 by Alex — monthly credit-cap reset | OFFICIAL | 2026-11-04 | CURRENT | Recurring system-scheduled event cadence |
| `11A-RS-012` | **July 2025 Update**, official in-game guide, `https://politicsandwar.com/pwpedia/article/july-2025-update` — military-research renaming, research added to score, four new colour blocs with their bonus formulas, eight new treasures, changed treasure eligibility, project-slot cadence | OFFICIAL | 2026-11-04 | CURRENT | Evidence that score composition and event eligibility change over time |
| `11A-RS-013` | **Daily Login Bonus**, official in-game guide, `https://politicsandwar.com/pwpedia/article/daily-login-bonus` | OFFICIAL | 2026-11-04 | CURRENT | Login-linked reward, streak design, newcomer cap |
| `11A-RS-014` | **New Player Bonus**, official in-game guide, `https://politicsandwar.com/pwpedia/article/New-Player-Bonus` — the full city-count-to-income-bonus table | OFFICIAL | 2026-11-04 | CURRENT | Catch-up design evidence |
| `11A-RS-015` | **Colour Trade Blocs**, official in-game guide, `https://politicsandwar.com/pwpedia/article/Colour-Trade-Blocs` — including the Beige and Grey bloc rules | OFFICIAL | 2026-11-04 | CURRENT | Non-geographic grouping, newcomer and inactive states |
| `11A-RS-016` | **Moon Landing**, official in-game guide, `https://politicsandwar.com/pwpedia/article/Moon-Landing` | OFFICIAL | 2026-11-04 | CURRENT | Milestone project, achievement grant, no competitive advantage |
| `11A-RS-017` | **Mars Landing**, official in-game guide, `https://politicsandwar.com/pwpedia/article/Mars-Landing` | OFFICIAL | 2026-11-04 | CURRENT | First-completion exclusivity, dedicated leaderboard, small recurring benefit |
| `11A-RS-018` | **Space Program**, official in-game guide, `https://politicsandwar.com/pwpedia/article/Space-Program` | OFFICIAL | 2026-11-04 | CURRENT | Prerequisite chains |
| `11A-RS-019` | **VIP Status**, official in-game guide, `https://politicsandwar.com/pwpedia/article/vip-status` — paid badge, custom graphics, raised API quota | OFFICIAL | 2026-11-04 | CURRENT | Paid recognition, fairness boundary |
| `11A-RS-020` | **Credits**, official in-game guide, `https://politicsandwar.com/pwpedia/article/credits` — the credit price list and the "each nation can only spend 20 credits on 'pay-to-win' benefits" limit | OFFICIAL | 2026-11-04 | CURRENT | Monetisation caps, seniority-gated package |
| `11A-RS-021` | **How do Rewarded Ads work?**, official in-game guide, `https://politicsandwar.com/pwpedia/article/how-do-rewarded-ads-work` | OFFICIAL | 2026-11-04 | CURRENT | Attention-for-currency loop and its daily cap |
| `11A-RS-022` | **Bounties**, live page `https://politicsandwar.com/world/bounties/` — the full posting and claiming rule set, shown on the page itself | OFFICIAL | 2026-11-04 | CURRENT | Player-triggered event, escrow, first-claim award, irreversibility |
| `11A-RS-023` | **World Conflicts**, live page `https://politicsandwar.com/world/conflicts/` — "the most recent war declarations", 1,541 wars at access | OFFICIAL | 2026-11-04 | CURRENT | Public conflict record surface |
| `11A-RS-024` | **World Graphs**, live page `https://politicsandwar.com/world-graphs/` — the published aggregate-statistics catalogue | OFFICIAL | 2026-11-04 | CURRENT | Aggregation and public-statistic design |
| `11A-RS-025` | **Achievement page 166 "Golden Treasures"**, live page `https://politicsandwar.com/achievement/166` — definition, completion count, completion percentage and the dated list of earning nations | OFFICIAL | 2026-11-05 | CURRENT | Achievement data model, rarity disclosure, dated attribution |
| `11A-RS-026` | **Nation profile, live** `https://politicsandwar.com/nation/id=1` (Avalon) — rank, score, war policy, cumulative loss counters, commendation and denouncement totals, nation-page-visit count, page age statement, activity feed, "part of the tutorial system and operated by a script" | OFFICIAL | 2026-11-04 | CURRENT | Public nation record surface, tenure language, activity history |
| `11A-RS-027` | **Nation profile, live** `https://politicsandwar.com/nation/id=300` (BEPU) — the populated **Awards:** row with seven badges and their tooltip definitions, alliance seniority, rank percentile | OFFICIAL | 2026-11-05 | CURRENT | Permanent commemorative awards, milestone awards, seniority |
| `11A-RS-028` | **Helpful Tools**, live page `https://politicsandwar.com/tools/` — including the "**Score Range Calculator**: find the range of nation scores that can be attacked at a particular score level" | OFFICIAL | 2026-11-05 | CURRENT | Score-as-eligibility-gate, published rather than hidden |
| `11A-RS-029` | **PWPedia index**, `https://politicsandwar.com/pwpedia/index` and its category pages (`nation`, `misc`, `faq`, `basic+guides`, `alliance`, `improvements`, `national+projects`, `war`, `units`, `resource`, `city`, `api`, `community+info`) — **149 articles** enumerated | OFFICIAL | 2026-11-04 | CURRENT | Negative evidence: the official guide's article inventory |
| `11A-RS-030` | **Alliance Positions** and **Alliance Ranks**, official in-game guide, `…/article/Alliance-Positions`, `…/article/Alliance-Ranks` — 15 permissions, 9 levels, four default positions | OFFICIAL | 2026-11-04 | CURRENT | Alliance recognition and role structure |
| `11A-RS-031` | Six official in-game guide articles, enumerated from `https://politicsandwar.com/pwpedia/index`: `https://politicsandwar.com/pwpedia/article/population-cap`, `…/article/War-Policy`, `…/article/Factbook`, `…/article/Continent`, `…/article/Beige-Buff`, `…/article/hall-of-fame` | OFFICIAL | 2026-11-04 | CURRENT | Derived caps, policy cadence, player-authored history, geographic grouping, comeback bonus, staff commemoration |
| `11A-RS-032` | **What is the API?** and **API FAQ**, official in-game guide, `https://politicsandwar.com/pwpedia/article/what-is-the-api`, `https://politicsandwar.com/pwpedia/article/api-faq` | OFFICIAL | 2026-11-04 | CURRENT | Public data surface, rate limits, mutation keys, bot ecosystem |

### 2.2 Politics & War — community sources

All rows in this subsection are **COMMUNITY**. They are used for structure and history, never as proof of a current developer rule.

| ID | Source | Accessed | Last revision | Currency | Used for |
|---|---|---|---|---|---|
| `11A-RS-033` | **Awards**, `https://politicsandwar.fandom.com/wiki/Awards` | 2026-11-05 | 2023-08-01 (84 rev) | HISTORICAL, partially corroborated CURRENT by `11A-RS-027` | Award taxonomy: leaderboard awards, special-achievement awards, event awards |
| `11A-RS-034` | **Achievements**, `https://politicsandwar.fandom.com/wiki/Achievements` | 2026-11-05 | 2023-08-28 (130 rev) | HISTORICAL; release date and count stated in text; showcase rule unconfirmed | Achievement condition inventory, non-retroactivity, showcase limit |
| `11A-RS-035` | **Objectives**, `https://politicsandwar.fandom.com/wiki/Objectives` | 2026-11-05 | 2019-01-29 (**1 rev, never edited**) | HISTORICAL | The 26-step sequential tutorial objective list |
| `11A-RS-036` | **Nation Score**, `https://politicsandwar.fandom.com/wiki/Nation_Score` | 2026-11-05 | 2021-03-26 | HISTORICAL — superseded by `11A-RS-002`/`11A-RS-012` on score composition | Triple-purpose statement (ranking, war range, treasure eligibility) |
| `11A-RS-037` | **Leaderboards**, `https://politicsandwar.fandom.com/wiki/Leaderboards` | 2026-11-05 | 2018-08-08 | HISTORICAL, author-described work-in-progress | Historical leaderboard inventory |
| `11A-RS-038` | **Politics and War Awards**, `https://politicsandwar.fandom.com/wiki/Politics_and_War_Awards` | 2026-11-05 | 2019-01-20 | HISTORICAL | Award context and history |
| `11A-RS-039` | **Nation Formulas**, `https://politicsandwar.fandom.com/wiki/Nation_Formulas` | 2026-11-05 | 2018-10-24 | HISTORICAL | Income formula family, score reference |
| `11A-RS-040` | **Treasures**, `https://politicsandwar.fandom.com/wiki/Treasures` | 2026-11-05 | 2017-05-15 | HISTORICAL | Early treasure inventory |
| `11A-RS-041` | **Moon Landing** / **Mars Landing**, `…/wiki/Moon_Landing`, `…/wiki/Mars_Landing` | 2026-11-05 | 2022-08-13 / 2023-07-20 | HISTORICAL; superseded by official `11A-RS-016`/`11A-RS-017` | Achievement names, leaderboard framing |
| `11A-RS-042` | **Vacation Mode**, `https://politicsandwar.fandom.com/wiki/Vacation_Mode` | 2026-11-05 | 2022-08-31 | **UNVERIFIED — 411-character stub, incomplete** | Nothing load-bearing; official rules text is used instead |
| `11A-RS-043` | **Color**, `https://politicsandwar.fandom.com/wiki/Color` | 2026-11-05 | 2014-10-10 | HISTORICAL | Early colour-bloc bonus model |

**Inaccessible or unconfirmable Politics & War surfaces, recorded rather than guessed:** the official API index `https://politicsandwar.com/api/` returned **HTTP 403**; `https://politicsandwar.com/achievements/` returned **HTTP 403**; `https://politicsandwar.com/awards/`, `/objectives/`, `/treasures/`, `/events/`, `/history/` and `/news/` returned **HTTP 404**; `https://politicsandwar.com/bulletins/` rendered an empty page; `/tutorial/`, `/nation/tutorial/` and `/objectives` returned no substantive content to an unauthenticated request. **The live in-game objectives screen therefore could not be verified**, and no current objective list is claimed here. Two community surfaces were also unavailable: `callofwar.fandom.com` returned **403** (see `11A-RS-070`).

---

## 3. Politics & War benchmark mechanics

Politics & War is the **primary benchmark**. Selection rationale is in the main report §3.1: it is a persistent multiplayer browser nation-strategy game with player-owned nations, and its own official documents state a **12-turns-per-day, two-hour cadence** — "1 credit for 60 Days (**720 Turns**)" and "An Advertisement will run for 20 days (**240 turns**)" (`11A-RS-019`, `11A-RS-020`) — which is arithmetic-identical to Nation Supremacy's fixed turn cadence. Its live pages also display a countdown to the next turn boundary and a separate daily boundary ("until after **day change** on Nov 8", `11A-RS-007`), matching a two-clock world like ours.

Relevance values: **Direct**, **Supporting**, **Limited**.

### 3.1 Nation development, score and eligibility

#### 11A-BM-001 — Nation Score as one number serving three purposes

| Field | Content |
|---|---|
| Game / System | Politics & War — nation development and competitive standing |
| Mechanic | A single **Nation Score** value per nation |
| How it works | **OBSERVED.** The official guide states: "Score is generally the **main determinant of war and spy ranges**. It is determined through Cities, Infrastructure, Projects, Military and Military Research", and gives the arithmetic directly: `(City Count − 1) × 100 + (Nation Infra Total ÷ 40) + (Project Count × 20) + ((Soldiers × 0.0004) + (Tanks × 0.025) + (Aircraft × 0.3) + (Ships × 1) + (Missiles × 5) + (Nuclear Weapons × 15)) + (Air Upgrades × 4) + (Ground Upgrades × 3) + (Naval Upgrades × 2) + 10` (`11A-RS-002`). The community page separately describes score as "a point-based indication of how strong a nation is compared to all other nations", related to **Ranking**, **War Range** — "only similarly sized nations are able to declare war on each other. This prevents very large nations from picking on very small nations" — and **Treasures** eligibility (`11A-RS-036`) |
| Trigger | Recomputed from nation state; a public **Nation Score Over Time** chart and a **Score Component Breakdown** are shown on each nation page (`11A-RS-026`) |
| Eligibility | Every nation |
| Timing | Continuous; charts are published per nation |
| Scoring | Additive across five domains with fixed weights; cities and infrastructure dominate (100 per city beyond the first; 1 infra ≈ 0.025), military is a linear sum of unit counts, and research adds 2–4 per upgrade (`11A-RS-012`) |
| Reward | Score itself grants nothing directly; it *gates* other things |
| Restrictions | Official rules prohibit manipulating it artificially: war slot filling, treasure-transfer coordination and new-nation funneling are rule violations with published point bands (`11A-RS-001`) |
| Strengths | One number is legible, cheap to compute, and gives newcomers an explicit "who can I fight" band. The weights make development and military both visible |
| Weaknesses | Three purposes in one value means a change for one purpose corrupts the others. `11A-RS-012` is the evidence: adding military research to score in July 2025 changed *ranking* and *attack eligibility* simultaneously, as a side effect of a military-balance patch. A peaceful developer and an arms builder raise the same number, so the number cannot answer "what is this nation good at". Raw unit counts dominate, so stockpiling scores as well as fighting |
| Exploit risks | Score suppression to enter a favourable attack band; score inflation immediately before a snapshot; arms accumulation that is never used but always counts; deliberate underperformance to farm a weaker band |
| Source | `11A-RS-002` (OFFICIAL, CURRENT, 2026-11-04); `11A-RS-012` (OFFICIAL, CURRENT); `11A-RS-036` (COMMUNITY, HISTORICAL 2021-03-26); `11A-RS-028` (OFFICIAL, CURRENT — a public **Score Range Calculator** publishes the attackable band) |
| Confidence | **High** (formula and purposes both official; the triple-purpose statement is official on the same page) |
| Second source | Yes — official guide plus community page agree on purposes; the *formula* has a single official source |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Separating "how developed is this nation" from "how does it rank" from "who may it fight" is not a refinement, it is the precondition for each of them surviving a balance change. Nation Supremacy's eligibility band must read an eligibility measure, and its public standings must read a performance measure; neither may be the other's alias. Whether a composite exists at all is decided in `11A-DR-010` |

#### 11A-BM-002 — Leaderboard set: one board, many columns, plus separate special boards

| Field | Content |
|---|---|
| Mechanic | The live leaderboard page |
| How it works | **OBSERVED.** Tabs are **Nation · Alliance · Continent · Color Trade Bloc · Treasures · Moon Landing · Mars Landing · Commendations & Denouncements** (`11A-RS-003`). Within the Nation tab, "Top 100 Nations by Score" is offered with the alternate metrics: **Cities, GDP, Population, Age, Highest Approval, Lowest Approval, Soldiers, Tanks, Aircraft, Ships, Missiles, Nuclear Weapons, Casualties**. Rows show rank, nation, leader, alliance and value |
| Trigger | Player navigation; content reflects current nation state |
| Eligibility | All nations; the page's own nation-count denominator on `11A-RS-026` reads "#8,050 of 11,958 Nations (67.32%)" for one nation and "#55 of 11,958 (0.46%)" for another |
| Timing | Visible continuously |
| Scoring | Raw totals per metric, descending; **Age** and both **Highest** and **Lowest** Approval are ranked, so a low value can win a category |
| Reward | Board position itself; certain positions additionally carry a reassigned badge (`11A-BM-004`) |
| Restrictions | Not documented on the page |
| Strengths | Cheap pluralism: one data source, thirteen visible dimensions, and the player chooses which matters. "Lowest Approval" and "Age" being rankable is honest — it recognises endurance and failure as categories rather than hiding them |
| Weaknesses | Because the underlying score is also the war gate, "highest" columns double as target selection. The board shows no window: a nation that grew this month and one that grew a decade ago occupy adjacent rows. Casualties are ranked without any context about whether they were inflicted or suffered, which invites reading a loss counter as a merit |
| Exploit risks | Snapshot-adjacent farming; metric-switching to win a thin category; ranking-driven escalation because rank is visible to attackers |
| Source | `11A-RS-003` (OFFICIAL, CURRENT, 2026-11-04); `11A-RS-037` (COMMUNITY, HISTORICAL) |
| Confidence | **High** for the tab and column inventory (read from the live page); **Medium** for update semantics, which the page does not state |
| Second source | No for current structure (single live page); the stale community board list disagrees on scope, which is why it is not used |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Plural standings are cheap to produce if they are columns of one lawful dataset rather than separate scored systems. A percentile and a total position should be shown together, because a raw rank among 11,958 rows conveys almost nothing to the nation in row 8,050 |

#### 11A-BM-003 — Public aggregate statistics as a separate, deliberately coarsened surface

| Field | Content |
|---|---|
| Mechanic | **World Graphs** — the published world-level statistics catalogue |
| How it works | **OBSERVED.** The page "exists to allow you to visualize the data being processed in the game" and lists, among others, **Active Nations in Last 3 Days / Last Week / Last Month**, **Avg Daily Income by Cities**, **Cities Histogram**, **Total <resource> Over Time**, **Total <resource> per Nation**, **Top 25 Alliances by Members / by Nukes / by Avg Score / by Score**, **Top 25 Nations by Nukes / by Score / by Wars Won** and a chart labelled **Total Nations Simulated** (`11A-RS-024`) |
| Trigger | Continuous, from processed game data |
| Eligibility | Public |
| Timing | Rolling windows expressed in days and weeks, plus per-resource time series |
| Scoring | Averages, sums, histograms, top-N |
| Reward | None — informational |
| Restrictions | Top-25 cut-offs; averages rather than per-nation values outside the top list |
| Strengths | Time-windowed and averaged, so it answers "is the world healthy" without exposing individuals. Distinguishing **mean** from **top-N** from **distribution** is exactly the three-shape separation a ranking system needs. "Active Nations in last 3 days / week / month" is the population metric a returning player actually needs |
| Weaknesses | A fixed Top-25 threshold can still isolate a small group at the boundary; the page does not explain its suppression rule |
| Exploit risks | Differencing two published aggregates across turns to recover one nation's value |
| Source | `11A-RS-024` (OFFICIAL, CURRENT, 2026-11-04) |
| Confidence | **High** for the catalogue; **Low** for the suppression rule, which is not stated |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** A world dashboard is a different object from a leaderboard and must be designed with its own aggregation rule. Nation Supremacy already fixes that rule — **D-027**: publication only at k ≥ 5, stable "other" merging, complementary suppression, and no differencing across turns or tables — so this row's value is that it shows the *shape* a compliant dashboard takes, and that it must never be a second ranking ladder |

### 3.2 Objectives, onboarding and recurring engagement

#### 11A-BM-004 — Sequential tutorial objectives, most mandatory

| Field | Content |
|---|---|
| Mechanic | The onboarding **objectives** sequence |
| How it works | **OBSERVED (HISTORICAL).** "When a new player creates a nation, they are presented with a tutorial and a series of **objectives** they must complete **in sequential order**. Some, such as #21 (Like the Facebook Page) are optional, but most need to be completed by the player to progress." The recorded list is 26 items: *Edit Your Nation's Description; Update your Nation's Policies; Find the Nation "Mountania"; Create a Trade Offer; Embargo a Nation; Send a Message; View Your Dossier; View the Changelog; Visit Discord Server; Visit Notifications Page; Visit Account Page; Read the Game Rules; Create a Baseball Team; Host a Baseball Game; Visit the Alliance Recruitment Page; **Join an Alliance**; Build a New City; Customize Military; **Recruit 5,000 Soldiers**; **Manufacture 25 Tanks**; Like the P&W Facebook Page; **Stockpile 250 Munitions**; **Stockpile 150 Gasoline**; **Recruit 10,000 Soldiers**; Build a Third City; Change Cover Image* (`11A-RS-035`) |
| Trigger | Nation creation |
| Eligibility | New nations only |
| Timing | One sequential list, no expiry documented |
| Scoring | Binary complete/incomplete per step; progression gated on completion |
| Reward | Not stated in this source |
| Restrictions | Sequential order; only the marked steps optional |
| Strengths | Every step is a *different* system, so the list is a genuine tour rather than a grind; several steps are pure discovery (Dossier, Changelog, Notifications, Account, Rules) and cost nothing |
| Weaknesses | **Two steps compel social and military participation: #16 forces alliance membership, and #19/#20/#22/#23/#24 force military accumulation.** #9 and #21 send the player to Discord and Facebook — marketing tasks, not play. The list is single-source and has not been edited since 2019, while the game's own July 2025 update changed military research (`11A-RS-012`): a fixed step list goes stale exactly as the brief predicted |
| Exploit risks | Gating progression on an external platform is unverifiable in-game and creates a compliance theatre; a mandatory "join an alliance" step pushes newcomers into exactly the group where multi-account abuse originates |
| Source | `11A-RS-035` (COMMUNITY, **HISTORICAL**, last and only revision 2019-01-29) |
| Confidence | **Medium** that this was the design in 2019; **Low** that it is current |
| Second source | Partial: the official nation page for nation 1 still states "This nation is part of the **tutorial system** and is operated by a script" (`11A-RS-026`, CURRENT), so a tutorial exists; the **objectives screen itself is login-gated and could not be verified**, so no current objective list is claimed |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** A discovery tour is valuable; a gated chore list that compels alliance membership or military stockpiling is not. Nation Supremacy's onboarding is already owned by B-03 and its ten-step journey (`REQ-089`), and `NAT-046` already states that "tutorial completion, first-login, first-trade and first-victory rewards are not adopted". Any 11B objective must therefore *extend* B-03's journey, never re-open it, and must not require membership of any group |

#### 11A-BM-005 — Daily login bonus with a soft-reset streak

| Field | Content |
|---|---|
| Mechanic | Consecutive-login income reward |
| How it works | **OBSERVED.** "Every day that you login, your nation earns a minimum of $500,000. For each day that you consecutively login, you add $500,000 to that amount, **up to a maximum of $3,000,000 per day**. **When you miss a day, you go down two steps, not down to zero.** If you consistently log in every day, your nation can earn up to $21,000,000 per week just by being active." New nations under 60 days old have a lower maximum cap of $6,000,000 with the same $500,000 increment |
| Trigger | Authentication |
| Eligibility | Any nation; newcomer tier differs |
| Timing | Daily, resetting at day change |
| Scoring | Streak length in steps |
| Reward | Direct currency, up to ~7% of a top nation's weekly income scale |
| Restrictions | Capped increment; gentler penalty than full reset |
| Strengths | The two-step fallback is a genuinely better streak rule than reset-to-zero: one missed day does not destroy weeks of standing, which is the failure mode most streak systems have |
| Weaknesses | It converts *presence* into *money*, so the casual player is structurally poorer and the grind is rewarded regardless of what the player decided. Capping newcomers at a lower maximum means the mechanic taxes exactly the players it claims to help |
| Exploit risks | Scheduled logins as pure collection; automation pressure against a login-gated currency; multi-account login stacking |
| Source | `11A-RS-013` (OFFICIAL, CURRENT, 2026-11-04) |
| Confidence | **High** |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** This is the pattern Nation Supremacy must not import. **B-02 `TR-085` already forbids it outright — "no login streak, no presence bonus, no 'act within X minutes' reward" — and `TR-006`/`TR-007` forbid decay, streaks and any bonus for acting every turn.** The transferable part is narrow but real: *if* any absence-tolerant engagement measure is ever introduced, its recovery curve must be graduated rather than a cliff |

#### 11A-BM-006 — Rewarded ads and new-player income bonus: two monetisation-adjacent engagement levers

| Field | Content |
|---|---|
| Mechanic | Voluntary advertising revenue; catch-up income bonus |
| How it works | **OBSERVED.** Rewarded Ads: "a voluntary way for you to view advertisements … in exchange for receiving some money in the game … you can receive **up to $2,000,000 per day** for your nation, at **$80,000 per ad watched**"; skipping forfeits the reward, and completion writes a notification and credits the money (`11A-RS-021`). New Player Bonus: "a percentage boost to gross income for nations with less than 21 cities … The bonus decreases as you buy more cities. At 21 cities, you no longer get any bonus" — published as a table from **100% at 1 city down by 5 points per city to 5% at 20** (`11A-RS-014`) |
| Trigger | Player action (ad) / automatic while city count is low |
| Eligibility | Any nation; city count for the bonus |
| Timing | Daily ad cap; bonus until city 21 |
| Scoring | Currency amount; percentage of gross income |
| Reward | Money; higher income |
| Restrictions | Daily cap of 25 ads; bonus expiry at 21 cities |
| Strengths | The catch-up table is transparent and finite — a player can see exactly how long the help lasts and why it ends, which is more honest than an invisible rubber-band |
| Weaknesses | Both levers pay currency for *attention* rather than for *decisions*. The ad loop monetises presence directly. A 100%-to-5% income slope creates a discontinuity in comparisons between young and old nations, and it interacts with the leaderboard: a newcomer's GDP is partly an artefact of age |
| Exploit risks | Ad-loop automation; age-band arbitrage; new nations created purely to harvest the bonus window |
| Source | `11A-RS-021`, `11A-RS-014` (both OFFICIAL, CURRENT, 2026-11-04) |
| Confidence | **High** |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Both are prohibited patterns for us by fixed decisions: **D-021 sets "no catch-up acceleration" at launch**, `ONB-028` states protection "is not an economic multiplier", `NAT-045` forbids any differential "by account age, rerolls, referrals or purchase", and `INV-025` bars catch-up acceleration introduced through reroll or protection. The one thing worth copying is the *disclosure format*: any future age-linked assistance must be a published, finite, expiring table, never a hidden curve |

#### 11A-BM-007 — Monthly credit-cap reset as a recurring scheduled world event

| Field | Content |
|---|---|
| Mechanic | A system-scheduled monthly event with a published rule change |
| How it works | **OBSERVED.** The official changelog carries a recurring dated post: "**09/01/2026**, **10/01/2026**, **11/01/2026** Donation Limit Reset — Donations have now been reset for the new month! You can now redeem up to 20 Credits…". The guide states the cap itself: "Each nation can only spend **20 credits** on 'pay-to-win' benefits", while "unlimited … cosmetic bonuses" are permitted, and the "VIP party" package grants 30 days of VIP to "all nations in your alliance with **7 or more days of seniority**" (`11A-RS-011`, `11A-RS-020`) |
| Trigger | Calendar (first instant of the month) |
| Eligibility | Per nation |
| Timing | Monthly, deterministic |
| Scoring | Spend counter reset |
| Reward | Restored spending capacity |
| Restrictions | 20 credits per month on advantageous items; cosmetic purchases uncapped |
| Strengths | Demonstrates a legitimate class of event that needs no content author at all: a **deterministic calendar rule with a published effect**. It is announceable in advance, verifiable, and cannot be farmed by timing |
| Weaknesses | It rewards regularity of purchase rather than play, and the seniority gate (7 days in the alliance) is the only place the package recognises belonging |
| Exploit risks | Coordinated purchase timing; alliance seniority laundering by short memberships |
| Source | `11A-RS-011`, `11A-RS-020` (OFFICIAL, CURRENT) |
| Confidence | **High** |
| Second source | Yes (changelog and guide state the same cap) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Calendar-deterministic events are the cheapest and least abusable class, and the only class Nation Supremacy can author without a content team (**AP-003**, "events are systemic, not authored live-ops"). Their design test is: *can a player predict the event and its effect from a published rule alone?* |

### 3.3 Awards, achievements and commemoration

#### 11A-BM-008 — Leaderboard awards: a transient badge reassigned daily

| Field | Content |
|---|---|
| Mechanic | Awards attached to leaderboard positions |
| How it works | **OBSERVED (HISTORICAL, corroborated).** "Awards are in-game badges on a nation which can be gained for reaching the top of certain leaderboards, for obtaining special achievements recognized by [the developer], or for having had a nation during a special event." The leaderboard-award class: "These awards are those that are given to the nation currently at the top of a leaderboard. These awards can be obtained by anyone and are **not permanent awards**. They will change to a new nation when that nation reaches the top of a respective leaderboard. Not all leaderboards have a respective award. **They will be reassigned if applicable every day just before update, server time. There is only one award for each category, so in any instance where there is a tie, the award is configured to go to [the developer's] nation.**" Recorded categories include Highest Score, Most Cities, Most Infrastructure, Most Infrastructure Destroyed, Most Soldiers / Tanks / Aircraft / Ships / Missiles / Nuclear Weapons, Most Nukes Launched, Most Nukes Eaten, Most Populous Nation, Oldest Nation, Largest GDP, Largest GDP per Capita, Largest Nation By Land Area, Most Spies Captured, Most Spy Casualties, Worst Environment, Most National Projects, Most Casualties, Most Wars Won, Most Wars Lost, Best Wars Won to Wars Lost Ratio (`11A-RS-033`) |
| Trigger | Daily reassignment immediately before the update tick |
| Eligibility | Any nation at the top of a listed board |
| Timing | Once per day, at a fixed point relative to the update |
| Scoring | Top position on the named metric only |
| Reward | A badge on the nation page; **no documented economic effect** |
| Restrictions | One badge per category, so only one nation ever holds it |
| Strengths | Clean separation from progression: a transient badge is pure recognition and cannot compound into power. Reassigning "just before update" is exactly the snapshot-boundary discipline a deterministic engine needs. Categories include non-combat (Oldest Nation, Largest GDP per Capita, Most National Projects, Worst Environment) as well as military |
| Weaknesses | The documented tie rule is the worst possible tie-break: on a tie the badge goes to the developer's own nation, which is neither transparent to players nor defensible as fair. A daily reassigned single-winner badge is also a pure attention prize with no defence against last-instant manipulation, because the whole population can see the current leader and the reassignment time is public |
| Exploit risks | Last-moment metric spikes to take a badge at the daily boundary; contested-category escalation; badge hoarding through metric switching |
| Source | `11A-RS-033` (COMMUNITY, **HISTORICAL**, 2023-08-01) |
| Confidence | **Medium** — taxonomy and reassigned-badge behaviour are corroborated by the live profile surface (`11A-RS-027`), but the daily-reassignment timing and the developer-tie-break are single-source community claims and are **not** confirmed by any official page reachable at the access date |
| Second source | Partial (`11A-RS-027`, `11A-RS-003`) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Two rules follow. First, a transient standing and a permanent honour must be different objects — adopted in `11A-DR-013`. Second, **a tie-break must be derivable from published data and must never favour the operator.** Nation Supremacy's deterministic ordering already supplies the compliant form: **B-02 `TR-044` band B2 resolves contested indivisible allocations by a seeded lottery keyed on `(turn_id, allocation_id)`, and `TR-045` forbids hidden ordering keys.** Any 11B tie rule must therefore be *published and reproducible*, which is exactly what the P&W documented rule is not |

#### 11A-BM-009 — Permanent commemorative awards, still displayed twelve years later

| Field | Content |
|---|---|
| Mechanic | Closed-eligibility historical badges |
| How it works | **OBSERVED.** The community page defines the class: "These awards were given to nations for obtaining special achievements … **and can not be gained anymore. These awards are permanent and cannot be lost as long as the nation exists.**" Listed examples: *Finished #2 Rank In Beta; Finished #3 Rank In Beta; First Nuclear Armed Nation; First Test Server Tournament Victor; 1st Nation to Reach 10,000 Score; 1st Nation to Reach 40 Cities; Speed Round — 4th Place / Highest Population / Highest GDP; Most Soldier Casualties during Beta*, plus donation-tier awards (`11A-RS-033`). **The live official nation profile for BEPU (id 300) confirms the class is current**: its `Awards:` row is populated with seven badge icons whose tooltips read "**Finished #2 Rank in Beta**", "Participated in the P&W Beta", "Participated in the P&W Speed Round", "Speed Round - 4th Place", "Speed Round - Highest Population", "Speed Round - Highest GDP", and the page's own explanation of the row states "Awards are special badge icons recognizing something special about a nation" (`11A-RS-027`). Two further badges visible in the same markup are explicitly milestone-type: "**CN Milestone** — This nation was around when P&W surpassed CN in nation count" and "**Singularity** — Game Date and Real Date Converged 25 June 2017"; and the guide's separate **Hall of Fame** page commemorates former volunteer staff by name and role (`11A-RS-031`, `11A-RS-024`) |
| Trigger | A one-time historical condition, or an anniversary/world-state threshold |
| Eligibility | Only nations existing at the moment of the condition |
| Timing | Never re-issued; permanent while the nation exists |
| Scoring | None — commemorative |
| Reward | Badge only; **no documented economic or military effect** |
| Restrictions | Tied to the nation identity; `RRL-013`-equivalent behaviour in our own B-03 means a reroll would forfeit an equivalent badge |
| Strengths | This is the strongest evidence in the whole benchmark set that **a permanent record layer can exist without becoming a power layer.** A "first nation to reach 10,000 score" badge is simultaneously the most prestigious and the least exploitable object in the game, because eligibility is closed and the claim is a fact about history rather than a current measurement. The world-state forms ("when P&W surpassed CN in nation count", "game date and real date converged") are **system-triggered milestones computed from global data, not player requests** — precisely the class a no-content-team game can sustain |
| Weaknesses | The recognition economy fossilises: the founding generation holds badges no later player can ever earn, and "first to X" categories are permanently closed by definition. Donation-linked badges in the same display row conflate payment with achievement |
| Exploit risks | Identity laundering — because the badge belongs to the *nation*, transferring an account transfers history, which is why account selling is a permanent-expiry rule violation in the same game (`11A-RS-001`) |
| Source | `11A-RS-027` (OFFICIAL, **CURRENT**, 2026-11-05); `11A-RS-033` (COMMUNITY, HISTORICAL); `11A-RS-031` (OFFICIAL, CURRENT) |
| Confidence | **High** that the class is live and permanent (an official live page shows the badges and defines the row); **Medium** for the "can never be gained again" wording, which is community-sourced |
| Second source | Yes — official live profile and community inventory agree |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt a **closed-eligibility historical honour** as a distinct object from achievements and rankings (`11A-DR-013`, `11A-DR-016`), and prefer **world-state triggers** over "first player to do X" where possible, because a first-mover honour is permanently unobtainable for everyone who arrives later. The badge must carry no mechanical weight — which our own `NAT-052` already requires ("no resources, yield, military power, protection or ranking weight") |

#### 11A-BM-010 — Achievements: fixed conditions, non-retroactive, paid and promotional entries included

| Field | Content |
|---|---|
| Mechanic | The achievement catalogue |
| How it works | **OBSERVED (HISTORICAL).** "Achievements are unlocked in P&W by completing pre-determined tasks. **Three at a time can be showcased on the nation page**, changeable on the Nation Edit page. On **August 14, 2019**, the initial set of **36** achievements were released, this was later followed the same day by a further 8, bringing the total to **44**. **They are not retroactive.** In the years since individual achievements have been added at times for various reasons" (`11A-RS-034`). The recorded catalogue spans clearly separated families: **development** (*Build 50 Cities*, *Have 10 or more Cities*, *Have 20 or more Cities*, *Have at least 10 Nuclear Weapons*); **military** (*Win at least 25 wars*, *Win over 200 wars*, *Win over 1,000 wars*, *Win 10 wars in a single turn*, *Lose 10 wars in a single turn*, *Be Engaged in 9/10 Active Wars Simultaneously*, *Win an Attrition War*, *Win a Raid War*, *Defeat [the tutorial nation] in a War*, *Loot More than $100,000 Winning a War*, and a four-step lifetime-loot ladder at $10M / $100M / $1B / $50B); **diplomatic and social** (*Receive 50 / 100 commendations*, *Be Denounced 50 / 100 times*, *Commend another nation publicly*, *Denounce another nation publicly*, *End a war in a truce*, *Have your Approval Rating reach 100% / reach 0%*); **economic** (*Have $1,000,000 in your nation*, *Trade More than 50,000 Resources at Once*, *Make a Deposit to an Alliance Bank*, *Receive $1,000,000 from an Alliance Bank*, *Hold a Treasure / Hold 2 or more / Hold all 30*, *Steal a Treasure*); **identity and policy** (*Have an Anarchist / Fascist Social Policy rating*, *Extreme Left / Extreme Right Economic Policy*, *Move continents*, *Fight a Ground Battle in Antarctica*, *Locate your nation in Antarctica*); **attendance** (*Login for a week consecutively*, *Log In for a Month Consecutively*, *Log In for a Year Consecutively*, *Log In on Christmas Day*, *Nation Over 3,000 Days Old*, *Have a nation at least one year old*); **project and milestone** (*Build the Space Program / Moon Landing / Mars Landing / Spy Satellite / Nuclear Research Facility / Green Technologies*, *First Nation to Land on the Moon*, *First Nation to Land on Mars*); **event** (*Halloween 2021: Participant in 2021 P&W Pumpkin Carving Contest*, *2020 Pumpkin Carving Contest Participant*, *Participate in the June 2023 Test Server Tournament*, *June 23 Tournament: Top 10 Score / Top 10 Wars Won*, *Golden Treasures — Collect all the eggs added as part of the 2025 Easter Event*); **purchase and promotion** (*Purchase the Limited Edition 6th/7th/8th/9th Anniversary Award Package*, *Subscribe to Politics & War*, *Have VIP*, *Watch a Rewarded Ad*, *Donate to the Game*, *Support Politics and War on Twitter*, *A Very Generous Extra Contribution to Politics and War*, plus two named staff/bug-test contributions); **hostile-relationship** (*Be attacked by someone with the Hannibal achievement*, *Win a war against someone with the Karma achievement*, *Declare war on someone for a third time within a month*); and a separate **Staff/Team Achievements** section (*Moderate the Politics & War Discord / Subreddit / Wikia*, *Design Team Member*, *Quality Assurance Team Member*) |
| Trigger | Predefined condition met |
| Eligibility | Any nation, subject to the condition |
| Timing | Continuous; several are dated one-off releases |
| Scoring | Binary; **the live achievement page publishes the earning count and percentage** — "This achievement has been earned by **1449** nations out of **14630** nations (**9.90%**)" with a dated nation-by-nation list (`11A-RS-025`) |
| Reward | Badge, plus a currency payout in event cases (`11A-RS-007`) |
| Restrictions | Showcase limited to three at a time (community-sourced, unconfirmed); non-retroactive |
| Strengths | Publishing **completion counts and percentages** is the single most reusable idea in this benchmark: it turns an achievement list into legible rarity information, gives players a scarcity signal without any artificial scarcity mechanic, and doubles as an operational health metric for the developer. Dated per-nation attribution makes the record auditable |
| Weaknesses | The catalogue mixes incompatible justifications: *attendance* (login streaks — forbidden for us by `TR-085`), *purchase* (anniversary packages, subscriptions, VIP, donations, Twitter follows), *employment* (staff and wiki moderators — an achievement for having a job on the game), and *promotion* (Facebook page likes). Achievement space therefore stops meaning "what you did in the game". Several conditions also **directly incentivise harm**: "*Be attacked by someone with the Hannibal achievement*" and "*Win a war against someone with the Karma achievement*" require a specific other nation to be victimised; "*Defeat [the script nation]*" is farmable by design and its activity feed shows exactly that, with 2026 war reasons reading "**for the tutorial**", "I want acheivement" and "Part of the tutorial...i'm truly sorry, Avalon." (`11A-RS-026`) |
| Exploit risks | A named, permanent, low-risk target makes achievement farming a legal strategy; a script nation that cannot defend itself is an unlimited renewable source. Paid achievements create a two-tier recognition economy in which a spender holds badges a player cannot earn by playing |
| Source | `11A-RS-034` (COMMUNITY, **HISTORICAL**, 2023-08-28); `11A-RS-025` (OFFICIAL, **CURRENT**, 2026-11-05); `11A-RS-026` (OFFICIAL, CURRENT); `11A-RS-027` (OFFICIAL, CURRENT) |
| Confidence | **High** that achievements exist and are live (official live pages `11A-RS-025` and `11A-RS-007` both reference them); **Medium** for the full catalogue (community, stale, self-described as non-exhaustive); **High** for the four named purchase-linked entries appearing in the community list but *Low* that they remain obtainable |
| Second source | Yes for existence and for event-achievement payouts; no for the showcase limit and the catalogue's completeness |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **data model** (fixed definition, binary grant, dated attribution, published completion rate) and reject the **justification mix** (`11A-DR-008`, `11A-DR-009`, `11A-DR-012`). Nation Supremacy's own rules already exclude the worst parts: `NAT-045` bars any differential by purchase or referral; `TR-085` bars attendance grants; `D-021`/`NAT-028`-family protection rules bar targeting shielded nations; and because the game forbids paying for advantage, a purchased recognition badge would have to be cosmetic-only and separately disclosed. Also adopted: **no achievement may name or require a specific victim**, and **no permanent un-deletable target nation may exist as a renewable farm** |

#### 11A-BM-011 — Event achievements with payouts, per-player daily limits and blockade escrow

| Field | Content |
|---|---|
| Mechanic | A seasonal event implemented as a bounded interaction with four achievements |
| How it works | **OBSERVED.** The official 2026-10-25 changelog specifies the whole event: "It is now **Spooky Season** in P&W! … from now until after **day change on Nov 8**, you will be able to distribute tricks and treats to other players by visiting their nation page … **Each player can give out 2 tricks and 2 treats every day, but can only receive one each per day.** These limits reset with normal military buy resets for each player. However both tricking and treating another player **costs 1000 food for each city they have.** … there is **4 achievements worth $150M** to be had. **Event Achievements:** Experience all types treats once ($20M); Experience all types of tricks once ($20m); Be tricked or treated 20 times ($30M); Trick or treat other players 40 times ($80M). *Note if you are blockaded when you get the achievements the money will go to **escrow** until you are no longer blockaded.*" It closes by pointing at the separate community contest: "there is only a few days left to submit your pumpkin for the pumpkin art contest on the forum or discord" (`11A-RS-007`) |
| Trigger | Seasonal window opened by the developer's post, closed at a named day-change boundary |
| Eligibility | Any nation; cost scales with the recipient's own city count |
| Timing | ~2 weeks; **daily giving cap of 2 and daily receiving cap of 1**, resetting at the daily boundary |
| Scoring | Counts of distinct types experienced and of actions performed, both directions |
| Reward | Four event achievements with explicit currency payouts totalling $150M |
| Restrictions | Hard per-day bidirectional caps; a real resource cost per action; **payout is escrowed while the recipient is blockaded** |
| Strengths | This is the most complete single example in the benchmark of a *well-engineered* event. Four properties are worth taking almost verbatim: **(a) an asymmetric receive cap (1 per day) against a give cap (2 per day)**, which caps any one player's farming rate regardless of how many partners they find; **(b) a real resource cost per interaction**, which prevents free-volume grinding; **(c) completion conditions expressed as *variety* and *volume* rather than as dominance over others**; **(d) the escrow rule**, which means an adverse state defers a reward rather than forfeiting it. Also note the window is expressed as a *boundary name* ("after day change on Nov 8"), not a wall-clock timestamp |
| Weaknesses | The reward is pure currency, so a two-week event becomes an income event and $150M against a top nation's daily income is material; the payout tiers are unpublished outside the post; a player who misses the window cannot participate at all |
| Exploit risks | Multi-account mutual trick-and-treat to hit the "receive 20" and "give 40" counts at the maximum legal rate; coordinating alt nations to concentrate the volume; timing the final payouts against a blockade that will be lifted |
| Source | `11A-RS-007` (OFFICIAL, CURRENT, 2026-11-04) |
| Confidence | **High** — the complete specification is on an official developer page |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the four structural properties as event-design constraints (`11A-DR-004`, `11A-DR-005`), and the escrow idea as the reconciliation with **B-03 `ONB-023`/`ONB-024`** (a protected nation cannot be targeted by hostile events) and **`D-028`** (a dormant nation loses nothing): a state that blocks *collection* must never destroy *entitlement*. The currency-payout shape, however, collides with **`ECN-113`** — a reward must be "non-repeatable, with an achievement key", disclosed, ledgered and "not a permanent yield multiplier", and **`ECN-013(c)`** permits new crowns only as "a **rare**, disclosed, system-generated event adjustment approved by Prompt 11". So the volume of the P&W payout is not available to us; the *shape* is |

### 3.4 World events, timing and lifecycle

#### 11A-BM-012 — Annual egg hunt with three eligibility tiers and a hard cleanup

| Field | Content |
|---|---|
| Mechanic | A recurring discovery event with vintage tiers |
| How it works | **OBSERVED.** "The **Easter Bunny** has once more made their rounds and the yearly Easter Egg hunt has begun. **The Original 12 white eggs have been reset and can be claimed by all players, they are worth $400,000** when collected. **The 6 eggs added last year are now blue, they remain in the event but can only be claimed by players who have not previously claimed them. They are worth $800,000.** An additional **6 new golden eggs** have been hidden, also worth $800,000 each. **Each set of eggs has a matching achievement for completing the set.** … these … will remain available in the game **until Monday, April 13, 2026 23:59 UTC (server time). After which they disappear until next year.** … All eggs are on the P&W website proper … Some eggs have been hidden with the expectation that **community will need to work together** to find them. And finally, **both eggs and achievement payouts respect blockades**, if you are blockaded when you collect them the money will be placed in your escrow account." The closing post adds the cleanup rule: "**all eggs will be removed at this upcoming Day Change** … Today is also the final day to purchase the Triassic Park National Project **for the achievement** and to send out any raptor attacks. Any raptors dispatched before DC will be able to complete their deliveries however no further raptors will be able to be sent out after DC. **The projects and any remaining raptors will be removed in 1 week**" (`11A-RS-008`) |
| Trigger | Annual calendar window with a stated UTC end instant |
| Eligibility | All players for the reset tier; **only non-claimants** for the returning tier; new tier open to all |
| Timing | ~2 weeks; expiry at a named boundary; **residual artefacts removed on a second, later boundary** |
| Scoring | Set completion per vintage tier |
| Reward | Currency per item plus one achievement per completed set |
| Restrictions | Per-tier claim history; hard expiry; deferred cleanup window |
| Strengths | Three genuinely useful ideas. **(1) Vintage tiering with prior-claim exclusion** — repeatable content for a returning activity, but a *new* item each year that cannot be re-farmed by anyone who already got it, which is how a recurring event avoids becoming an income tap. **(2) Two-stage teardown** — the event ends at one boundary and its leftovers are cleaned at a later one, so in-flight work is honoured instead of annihilated. **(3) An explicit "the community must cooperate to solve this" content class**, which is collective without being competitive |
| Weaknesses | Currency per item makes the hunt an income routine; a fully-expiring event excludes anyone who missed it entirely, and a "can only be claimed by players who have not previously claimed them" rule silently advantages players who joined recently over veterans who already claimed |
| Exploit risks | Multi-account claiming of a per-player once-only item; scripted URL discovery; sharing locations is *encouraged* here but is the obvious leak path for a reward tied to discovery, which is why the same post makes spoiling a courtesy rule |
| Source | `11A-RS-008` (OFFICIAL, CURRENT, 2026-11-05) |
| Confidence | **High** |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **two-stage teardown** and the **vintage-tier with prior-claim exclusion** as lifecycle requirements (`11A-DR-004`, `11A-DR-005`). Note the fairness caveat for Nation Supremacy: because our own `D-021` bars catch-up acceleration and `NAT-045` bars age-based differentials, a tier whose value depends on whether you claimed it *last year* is an account-history differential and needs explicit justification in 11B |

#### 11A-BM-013 — Weekly lottery: a scheduled recurring event with eligibility, a pre-draw freeze and a sink

| Field | Content |
|---|---|
| Mechanic | A deterministic weekly drawing |
| How it works | **OBSERVED.** "The lottery is a **weekly drawing** where one code is drawn randomly and automatically **each week on Sundays at 11:55PM (server time)**. If there is a winner, they will receive **90% of the pot** (which is entirely funded by lottery ticket purchases.) The other **10% is removed from the game as an 'administrative fee' which will act as a money-sink mechanism** in the game. If there is no winner, the pot **rolls over** to the next week. **Your purchased tickets expire each week.** **Tickets are also not available for purchase on the turn leading to the drawing (about 2 hours before the drawing) to avoid any potential bugs/issues.** Each turn, each player can purchase up to 100 lottery tickets at $50,000 each. Each lottery ticket is assigned a unique 4 character code … 36^4 combinations (**1,679,616**) …" The companion post adds eligibility and recognition: "**Must have 15+ cities and not be in Vacation Mode**", "**Sales close Sunday 10:00 PM UTC (start of the drawing turn)**", "Match: Winner takes 90% of the pot (**paid to escrow if blockaded**)", "Winner also gets the **Lottery Winner achievement** and a notification", plus a live reveal: "There is a countdown on the lottery page. 30 seconds out the code reveals one character at a time - your tickets re-sort live as they're eliminated or stay alive" (`11A-RS-009`) |
| Trigger | Weekly, at a fixed published instant |
| Eligibility | **15+ cities; not in Vacation Mode** — a wealth/tenure-adjacent gate and a state exclusion |
| Timing | Weekly, with a one-turn purchase freeze before the draw |
| Scoring | Random draw against a fixed code space, with published odds |
| Reward | 90% of the pot plus a permanent achievement |
| Restrictions | Per-turn purchase cap, weekly ticket expiry, rollover, pre-draw freeze |
| Strengths | The **pre-draw freeze** is the single most transferable engineering detail in the whole benchmark set: closing participation one tick before the draw exists precisely to stop a submission racing a snapshot, which is what **B-02 `TR-032`** ("submissions during resolution join the next turn") and **`TR-037`** (freeze at LOCKED) achieve structurally in our engine. Also: the funding model creates nothing (the pot is player-funded, the residual is a declared **sink**, satisfying `ECN-112`'s no-free-money rule), the odds are published, the payout is escrowed under an adverse state, and the achievement and the notification are separate objects |
| Weaknesses | A 15-city eligibility gate is a wealth floor that excludes exactly the newcomers a recurring event should recruit; the odds are so long (about 0.00006% per ticket) that the achievement is effectively a random lottery for the rich rather than an accomplishment; gambling-adjacent mechanics are opt-in only in practice but not in framing |
| Exploit risks | Multi-account pooling of tickets and pot; a player deliberately staying under 15 cities to alter which population competes; last-instant purchase racing the boundary — which the freeze specifically closes |
| Source | `11A-RS-009` (OFFICIAL, CURRENT, 2026-11-05) |
| Confidence | **High** |
| Second source | Yes (two posts describe the same system, with consistent numbers) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **participation freeze before any snapshot or draw** (`11A-DR-006`) and the **player-funded-with-declared-sink** reward shape, and reject the **randomness-as-achievement** shape: **`TR-047`** requires determinism with "no wall-clock, no environment randomness", so a random drawing in Nation Supremacy can only exist as a bounded seeded outcome with published odds in exactly the way **B-10 `WAR-074`** already does it ("one bounded, seeded fortune roll… its bound is disclosed"). An eligibility floor expressed as a development threshold is legitimate in shape but must never become a pay-to-enter gate |

#### 11A-BM-014 — Treasures: a rotating system-generated world object

| Field | Content |
|---|---|
| Mechanic | The treasure spawn-and-transfer cycle |
| How it works | **OBSERVED.** "Politics and War has **30 Treasures**, each of which offers a percentage based income bonus to the nation possessing it, as well as an income bonus to that nation's alliance. **If you defeat another nation with a Treasure in a war, you will take one of their Treasures. If they have multiple Treasures, you will get only one, chosen at random.** **Each Treasure automatically respawns in a new nation every 60 days.** Some Treasures are restricted such that they can only spawn in a nation on a particular Color Trade Bloc. **Treasures cannot spawn in nations on the Beige or Gray Color Trade Blocs.** Treasures can also only spawn in nations with a **Score between 15%-65% of the #1 nation's Score.** Nations possessing Treasures can also sell their Treasures in the Treasure Trading Center." The guide adds the nation-side value ("Your nation's bonus depends on which treasure you get, **varying between 5 and 9 percent**"), the alliance-side formula ("**square root of (# of Treasures in the Alliance) × 4**"), the three acquisition routes ("Random Spawning, Treasure Trading, and Winning Through War") and the current eligibility change: "**There are no longer any continent restrictions. Alliance and Nation Colors must match to be eligible. A nation must have been on a color for at least 30 days to be eligible**" (`11A-RS-004`, `11A-RS-005`, `11A-RS-012`). The live tracking page publishes, per treasure, its **spawn date, days to respawn, name, possessing nation, nation colour, continent and current score** |
| Trigger | Deterministic 60-day respawn timer per object, independent of players |
| Eligibility | **A relative score band (15%–65% of the #1 nation), a matching colour-bloc membership, ≥30 days on that colour, and explicit exclusion of the newcomer (Beige) and inactive (Gray) states** |
| Timing | 60-day cycle per object, continuous and staggered across the set |
| Scoring | Possession; transfer on war victory |
| Reward | 5–9% national income plus an alliance-wide square-root-scaled bonus |
| Restrictions | One treasure seized per war regardless of holdings; blockade prevents completion; tradeable on a dedicated market |
| Strengths | This is a **complete, working model of a persistent system-generated world event with no content author at all.** The relative band is the key device: by targeting "15–65% of the leader" rather than an absolute score, the event self-adjusts as the world grows, so it never needs retuning and never selects the leader or the newest nation. The exclusion of the newcomer and inactive states is exactly the shape **B-03 `ONB-025`** prescribes — protected nations "may appear in rankings and participate in world events that are not offensive". The square-root alliance bonus is a diminishing return, which is how a collective reward avoids becoming winner-take-most. Publishing the per-object timer converts a random spawn into an *observable schedule*, which is what makes it feel like a world rather than a loot drop |
| Weaknesses | A 5–9% income gain per item, stackable to 30, is a large permanent economic effect riding on a recognition object, so possession compounds; the seizure rule means war is the primary acquisition route, which makes a peaceful nation structurally dependent on being attacked or on buying; the July 2025 changes show how much *eligibility* churns, and the documented anti-collusion rule exists precisely because transfer-by-arranged-war was real enough to prohibit |
| Exploit risks | **Treasure Transfer Coordination** — the official rules name it directly: "Coordinating with an opponent to transfer Treasures through wars with minimal damage" is a 25–75 point violation with a 2-year expiry (`11A-RS-001`); buying entry into a high-value group; deliberately sitting in the eligible band to receive a spawn |
| Source | `11A-RS-005` (OFFICIAL, CURRENT — the rule text is printed on the live page); `11A-RS-004` (OFFICIAL, CURRENT); `11A-RS-012` (OFFICIAL, CURRENT, for the eligibility change); `11A-RS-001` (OFFICIAL, CURRENT, for the prohibition) |
| Confidence | **High** (three official sources agree) |
| Second source | Yes |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt **relative-band eligibility against the current world maximum** and **explicit exclusion of newcomer and inactive states** as core event-selection rules (`11A-DR-001`, `11A-DR-003`), and adopt **diminishing-return collective bonuses** for any alliance-scope reward (`11A-DR-011`). **Do not** adopt a large permanent economic multiplier as the reward — `ECN-113` forbids "a permanent yield multiplier" outright, and `ECN-190` allows money-supply growth only from population, tax and disclosed rewards. The transferable object is therefore the *rotation, band and timer*, not the *yield* |

#### 11A-BM-015 — Player-triggered events: bounties with escrow, first-claim award and irreversibility

| Field | Content |
|---|---|
| Mechanic | A player-created public challenge with a locked prize |
| How it works | **OBSERVED.** "Bounties are **anonymously posted** rewards for defeating nations in war… To claim a bounty, **you must defeat a nation in an offensive war**, or in the case of a nuclear bounty use a nuclear weapon in an offensive war. **If you are blockaded when you claim a bounty, you will receive it once you are no longer blockaded. You cannot claim your own posted bounties.** … **By posting a new bounty, you will immediately forfeit the funds for the bounty from your nation. These funds will be automatically imbursed to the first nation to defeat your target** in the specified war type. If a blockaded nation defeats your target, they will not immediately receive the bounty, but instead will receive it upon the blockade ending. **Bounties must be at least $1,000,000** or greater. **Bounties cannot be canceled or refunded. Once you have posted a bounty, it will remain posted until it has been claimed.**" The live board lists date posted, target, target's alliance, war type, amount and message, with filters by type and amount band (`11A-RS-022`). The related rule is explicit: "**Coordinating with an opponent to remove bounties on their nation or your nation is against the rules. While bounty-hunting is legal and encouraged**, coordinating with allies or mercenaries to remove a bounty while doing minimal damage would be a violation" (`11A-RS-001`) |
| Trigger | A player's irreversible posting action |
| Eligibility | Any nation able to pay the minimum; anonymity for the poster |
| Timing | Open until claimed — **no expiry at all** |
| Scoring | First successful offensive defeat of the named target |
| Reward | Escrowed currency, paid to the first claimant |
| Restrictions | Minimum amount; no self-claim; no cancellation; escrow while blockaded |
| Strengths | A complete player-triggered event lifecycle implemented with only two rules — forfeit-on-post and first-claim-wins — which is why it needs no moderator, no authoring and no scheduler. Anonymity of the poster removes the deterrence problem ("who would take this on?"). Deferring rather than voiding a blockaded claimant is the same principle as `11A-BM-011`/`11A-BM-013` and matches **`D-028`**'s "no resource, progression or ownership loss" |
| Weaknesses | **No expiry is the flaw**: an unclaimed bounty is permanently escrowed dead capital, and an unremovable posting is irreversible money removal with no cooling-off. Anonymity plus no-refund plus a hostile target is exactly the shape that a moderation team must police, and the game does police it — the existence of a specific named prohibition proves the abuse was real |
| Exploit risks | **Bounty Coordination**: post a bounty on a colluding nation, have an alt or ally collect it, netting a laundered transfer that bypasses trade limits; bounties on protected or newly formed nations as bait; capital locked against a target nobody can beat |
| Source | `11A-RS-022` (OFFICIAL, CURRENT, 2026-11-04); `11A-RS-001` (OFFICIAL, CURRENT) |
| Confidence | **High** |
| Second source | Yes (the live board and the rules page describe the same object) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Player-triggered events are affordable and lively, but require three controls this design shows the cost of omitting: **reservation of the prize at creation** (mirroring **B-02 `TR-067`/`TR-069`** reserve-at-acceptance), **an expiry or release rule** so capital cannot be locked forever, and **counterparty-independence validation** so the claimant cannot be coordinated with the poster. The last is a **Prompt 12** fair-play rule, not an event rule, because **`REQ-063`** already requires that "every value-moving or coordinating action is classified; indirect routes are covered; a blocked attempt moves nothing". Recorded as `11A-DR-007` and `11A-RK-004` |

#### 11A-BM-016 — Milestone national projects as the progression spine

| Field | Content |
|---|---|
| Mechanic | A prerequisite chain of unique national achievements with deliberate non-advantage |
| How it works | **OBSERVED.** **Moon Landing** "is a national project that lands citizens on the lunar surface. **This project does not grant any competitive advantage and cannot be destroyed.** Moon Landing grants the **Lunar Wars** achievement. It costs $50 million, 5k oil, 5k aluminum, 5k munitions, 5k steel, 5k gasoline, and 10k uranium. In order to build Moon Landing, nations must have **Space Program**" (`11A-RS-016`). **Mars Landing** "does not benefit your nation competitively, but it provides a **unique achievement (A Whole New World) to the first player to build it** as well as the **Red Desert** achievement **to every other player who builds it**. **All players who complete it will be tracked on a leaderboard** like the Moon Landing project. **Nations will also gain a daily boost to their approval rating.** Requires the Space Program and Moon Landing National Projects to build. This national project cannot be destroyed. This project costs $200,000,000, 20,000 [each of] Oil, Aluminum, Munitions, Steel, Gasoline and Uranium" (`11A-RS-017`). **Space Program** sits mid-chain, "allows three missiles to be built per day instead of two", and is required for Green Technologies, Moon Landing, Spy Satellite, Telecommunications Satellite and Mars Landing (`11A-RS-018`). The project-slot cadence was retuned in July 2025: "Project slots are now awarded **every 4000 infra**, a reduction from the previous 5000" (`11A-RS-012`) |
| Trigger | Player construction, gated by predecessor completion and by cost |
| Eligibility | Any nation meeting the chain and affording the cost |
| Timing | Construction; permanent once built; indestructible |
| Scoring | Binary completion per project; **first-completion ordering** for the unique variant |
| Reward | Achievement (one exclusive, one general), a dedicated leaderboard, and a small daily approval effect |
| Restrictions | Chain depth, cost, slot cadence, **explicit "no competitive advantage"** |
| Strengths | The clearest non-military long-term progression path in the benchmark, and it is *designed* to be non-military: the developer states in the rule text that the object confers no competitive advantage and cannot be destroyed by an opponent. Three recognition layers come off one completion — **an exclusive badge for the first, a general badge for everyone else, and a permanent leaderboard row** — which satisfies both the competitor and the participant from the same action, with no extra content. The chain also makes progression *legible*: a viewer can tell what a nation has already committed to |
| Weaknesses | A $200M plus 120,000 resources cost is reachable only by very large nations, so the "anyone can do this" path is bounded by development; the approval boost, though small, is a permanent recurring effect on a milestone object; a permanently exclusive first-place badge means the second player's achievement is permanently worth less, which is a fossilisation cost paid by later players |
| Exploit risks | Very low by construction — the object is indestructible, non-tradeable and grants no combat benefit, so there is nothing to attack for. The residual risk is *ordering* dispute at the boundary rather than farming |
| Source | `11A-RS-016`, `11A-RS-017`, `11A-RS-018`, `11A-RS-012` (all OFFICIAL, CURRENT) |
| Confidence | **High** |
| Second source | Yes (community pages `11A-RS-041` describe the same achievements and leaderboard, though they are older) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the pattern "one completed national milestone emits several recognition types at once" and the explicit **non-competitive, indestructible** characterisation (`11A-RS-016`/`11A-RS-017`) (`11A-DR-014`, `11A-DR-017`). Both are already compatible with our registers: **`NAT-052`** says milestones "are records, not power" with "no resources, yield, military power, protection or ranking weight", and **`URB-035`** makes cities permanent and non-deletable while **`URB-040`** forbids any "construction, demolition, **event** or `OP-05` strike" from taking a city below its infrastructure floor — so an event in Nation Supremacy cannot damage the very development a milestone records. The permanent *approval* boost, however, is precisely what `DMP-141` forbids an event from doing casually: an event "may move a support through a **named event term** added to the formula by a decision, or grant a **one-time approval change** through the normal target-and-cap path; it **may not set approval directly**" |

### 3.5 Warfare-derived recognition

#### 11A-BM-017 — War-derived public statistics and cumulative counters

| Field | Content |
|---|---|
| Mechanic | What a nation page publishes about conflict |
| How it works | **OBSERVED.** A live profile publishes, under **Military**, per-unit current holdings each paired with a lifetime counter — "Soldiers: / Casualties: / Killed:", "Tanks: / Lost: / Destroyed:", "Aircraft / Spies (Lost, Captured)", "Missiles / Launched / Eaten", "Nuclear Weapons / Launched / Eaten" — plus a **Nation Stats** block: **Infrastructure Destroyed, Infrastructure Lost, Money Looted, Wars Won, Wars Lost**, and an **Espionage** military-research row. Below that, a dated public **Nation Activity** feed records "Avalon had war declared by Khanka for the reason of 'Zero'", "Avalon was embargoed by DemocraticPeoplesKorea", "SkeepBop of SkeepBopLand has publicly denounced the nation of Avalon" and similar entries with timestamps (`11A-RS-026`). The live **World Conflicts** page lists "the most recent war declarations by nations across the game" with aggressor, defender, alliances and a per-war timeline (`11A-RS-023`). Award categories include **Most Casualties**, **Most Infrastructure Destroyed**, **Most Wars Won**, **Most Wars Lost**, **Best Wars Won to Wars Lost Ratio**, **Most Nukes Eaten** and **Most Spies Captured** (`11A-RS-033`) |
| Trigger | War and operation events |
| Eligibility | Public |
| Timing | Cumulative counters never reset; activity feed is a rolling window |
| Scoring | Lifetime totals |
| Reward | Feeds leaderboard columns and award categories |
| Restrictions | Not documented on the page |
| Strengths | Separating *current holdings* from *lifetime losses and destruction* is exactly the distinction between a state measurement and a historical record, and putting both on one page lets a reader tell a nation that is strong from a nation that has been fighting a long time. A public dated activity feed is the cheapest possible chronicle primitive |
| Weaknesses | **Counting casualties as a rankable and awardable statistic measures human cost as merit**, with no distinction between inflicted and suffered and no context; combined with the visible "Eaten"/"Captured" columns it turns loss into a scoreboard entry. This is the specific pattern Nation Supremacy must not reproduce |
| Exploit risks | Casualty farming against weak targets; inflating a war-count column through war slot filling — the reason the official rules give that violation a **2-year** expiry, the longest band in the set (`11A-RS-001`) |
| Source | `11A-RS-026` (OFFICIAL, CURRENT); `11A-RS-023` (OFFICIAL, CURRENT); `11A-RS-033` (COMMUNITY, HISTORICAL) |
| Confidence | **High** for the published fields; **Medium** for the award-category linkage (stale community source) |
| Second source | Partial |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Two prohibitions follow from our own registers rather than from preference. **`D-027`** plus **B-10 `WAR-162`** — "a public war statistic that would identify fewer than five nations is withheld or coarsened… **no exact readiness, force or inventory is ever public**" — means a casualty or loss leaderboard cannot be built from private military values. And because **B-10 `WAR-147`** states "the campaign record is permanent. **Rankings and world events receive the outcome under B-11's rules**", the receiving rule is *ours to write*: the recommended direction is to derive recognition from **participation, defensive outcomes and bounded campaign records**, never from a raw casualty or destruction total (`11A-DR-015`) |

### 3.6 Group, tenure and state structures

#### 11A-BM-018 — Colour blocs: non-geographic group competition with published formulas

| Field | Content |
|---|---|
| Mechanic | Membership-group income bonuses with a newcomer/inactive state |
| How it works | **OBSERVED.** "Colour Trade Blocs are a feature where you decide what colour your nation is on. You want to match your colour with your alliance's colour, as that will give a bonus depending on the colour. **There are two special blocs: Beige and Grey. You cannot change to either of them, though you will not be taxed on either. Beige is for new nations or nations that have just lost a war. On Beige, you get a set $85,000 bonus. When your nation is created, you are given 14 days of time on Beige (Beige Time), and after you lose a war, you are given 2 days of Beige Time, which stacks per war. Grey is for inactive nations and gives no bonus** … You will be moved to Grey after Beige Time expires or if you have been inactive for at least 5 days" (`11A-RS-015`). The July 2025 update replaced the fixed per-colour bonus with **three published formulas**: "Turn Bonus Cap = (Average daily monetary revenue × 18 / Total Nations) (18 is the number of colors)", "Growth Bonus = MIN(((Average Daily Monetary Net Revenue of all nations on color × 0.75) / all Nations on Color), Turn Bonus Cap)", "Recruit Bonus = MIN((Total Nations <21 on Color × 10 / Total Nations <21 on Color), 1) × Turn Bonus Cap", "Final Turn Bonus = Growth Bonus + Recruit Bonus", and adds "**Nations in beige, gray, VM, or not in an alliance are excluded from all formulas**" (`11A-RS-012`) |
| Trigger | Group membership choice plus a state assignment the player cannot choose |
| Eligibility | Alliance members matching their alliance's colour; special blocs are assigned, not joined |
| Timing | Per-turn bonus, recomputed from rolling averages |
| Scoring | Group-relative: mean revenue per capita on the colour, capped by a world-wide mean term |
| Reward | A currency bonus added to gross income |
| Restrictions | Excluded states (Beige, Grey, Vacation Mode, unallied); a world-derived cap |
| Strengths | This is the benchmark's only **non-geographic group competition layer**, which matters because Nation Supremacy is mapless and its only group object is the Alliance. Two devices are worth taking: **(a) a cap derived from a world-wide average rather than a constant**, so the reward self-scales as the population grows without retuning; **(b) exclusion of the newcomer, inactive, vacationing and unaffiliated states from *competition* formulas while leaving them protected and paid elsewhere** — which is precisely the shape `D-028` prescribes ("excluded from public rankings and published aggregates… a presentation rule for a nation that may return"). A "recruit bonus" weighted to nations under 21 cities also makes *bringing in newcomers* a group objective rather than a chore |
| Weaknesses | Being placed in Grey after 5 days of inactivity while a nation is still visible is a silent state change; a world-derived cap makes every group's reward depend on the whole population, which couples balance globally and makes local tuning impossible; the unallied exclusion means a solo player gains nothing from the group layer at all, which conflicts with "membership never mandatory" |
| Exploit risks | Colour-hopping to chase the highest-paying bloc; alliance-level coordination to concentrate recruits on one colour; deliberately cycling between Grey and active status |
| Source | `11A-RS-015` (OFFICIAL, CURRENT); `11A-RS-012` (OFFICIAL, CURRENT) |
| Confidence | **High** |
| Second source | Weak — `11A-RS-043` is a 2014 community page and is not relied on |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Group-scope competition is viable without geography, but the exclusion half must be a **presentation and eligibility** rule only, and any group layer must leave an independent nation able to progress: **B-09 `ALL-134`** and the outline's validation line "**membership never mandatory**" bind this, and `11A-DR-011` requires diminishing returns for any collective bonus. World-average-derived caps are recommended over constants (`11A-DR-003`) because they survive population change without a rebalance |

#### 11A-BM-019 — Tenure as a first-class published quantity

| Field | Content |
|---|---|
| Mechanic | Age, seniority and continuity as visible, rankable values |
| How it works | **OBSERVED.** A live profile publishes **Founded: 08/05/2014 (4,474 Days Old)** and **Last Activity: Active 13 hours ago**, and its narrative block states "At 2,409 days old, Avalon is an **ancient nation**" (`11A-RS-026`, `11A-RS-027`). The leaderboard offers **Age** as a rankable column (`11A-RS-003`), and the award set includes an **Oldest Nation** badge (`11A-RS-033`). Inside alliances, **Alliance Seniority: 287 days** is published as its own field (`11A-RS-027`), and the paid "VIP party" package is gated on "**7 or more days of seniority**" (`11A-RS-020`). Achievements include *Have a nation at least one year old* and *Nation Over 3,000 Days Old* (`11A-RS-034`), and commemorative badges exist for surviving fixed historical intervals — "Played the full first year of P&W!", "This nation existed when P&W turned 1" (`11A-RS-027`) |
| Trigger | Time elapsed since creation or since joining |
| Eligibility | Any nation or member |
| Timing | Continuous |
| Scoring | Day counts |
| Reward | Rank placement, badges, eligibility for a package |
| Restrictions | None documented |
| Strengths | Tenure is honest: it recognises continuity, which is real and non-substitutable, and it is trivially un-gameable because it cannot be farmed faster. Anchoring several commemorative badges to fixed historical intervals rather than to thresholds is what makes them *history* rather than *grind* |
| Weaknesses | **Age is not merit.** A rankable Age column and an "Oldest Nation" award give an automatic, unbeatable advantage to the founding cohort for doing nothing, and an achievements list containing both "Log In for a Year Consecutively" and "Nation Over 3,000 Days Old" mixes attendance, survival and achievement into one indistinguishable set |
| Exploit risks | Account-age advantage in eligibility gates (a seniority floor excludes new members from collective benefits); alt nations aged deliberately |
| Source | `11A-RS-026`, `11A-RS-027`, `11A-RS-003`, `11A-RS-020` (all OFFICIAL, CURRENT); `11A-RS-033`, `11A-RS-034` (COMMUNITY, HISTORICAL) |
| Confidence | **High** for the published fields; **Medium** for the award linkage |
| Second source | Yes for the fields |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Tenure should be **displayed and commemorated, never ranked as a competitive score and never used as an eligibility floor for mechanical benefit.** Our own rules already require this: **`NAT-045`** forbids any differential "by account age", and `INV-006`/`RRL-013` destroy a rerolled nation's counters — so a ranking built on age would be both unfair and reroll-fragile. Interval-anchored commemorative records are recommended instead (`11A-DR-016`) |

### 3.7 Monetisation and its fairness boundary

#### 11A-BM-020 — Explicitly capped pay-for-advantage, and paid recognition

| Field | Content |
|---|---|
| Mechanic | Monetisation with a published hard limit and a cosmetic-only remainder |
| How it works | **OBSERVED.** "One credit is equivalent to ~$5 USD… You can buy more than 10 credits at a time and can spend as many Credits as you want per month on 'cosmetic' bonuses like VIP subscriptions and other options that do not give your nation any in-game advantage. **Important: Each nation can only spend 20 credits on 'pay-to-win' benefits.** You can only buy credits for your nation. **Credits cannot be looted in a war like other resources** and can only be kept on a nation and not in an alliance bank." The published table marks each item as counting toward the limit or not: money, resources, infrastructure and city/project timer resets **count**; name change, VIP, advertisement, continent change, baseball logo and alliance page upgrade **do not**. VIP itself grants "a **VIP badge** on your nation page", national anthem, custom graphics and a raised API quota (`11A-RS-020`, `11A-RS-019`). The community achievement list shows a *paid* achievement family (*Purchase the Limited Edition 6th/7th/8th/9th Anniversary Award Package*, *Subscribe to Politics & War*, *Have VIP*, *Watch a Rewarded Ad*) and a *donation* award family (`11A-RS-034`, `11A-RS-033`). The rules close the outside-market door: "**Real-World Transactions for In-Game Materials** … Moderation Points Guideline: 75-100 … **Expiration: Never** — Politics & War has a limited donation system to prevent the game from being 'pay-to-win'… it is against the rules for players to make exchanges of real-life money or goods for in-game materials" (`11A-RS-001`) |
| Strengths | The **published per-nation cap with an item-by-item "counts towards limit" column** is a far more legible fairness guarantee than a vague "no pay-to-win" claim, and the never-expiring prohibition on external real-money trading is what makes the internal cap enforceable at all. Keeping the paid currency unlootable and unbankable stops it becoming a war objective |
| Weaknesses | A purchased badge sits in the same recognition space as an earned one, and a purchased achievement makes recognition directly purchasable; timers purchasable for money mean progress speed has a price |
| Exploit risks | Real-money conversion outside the game's own cap; gifting as laundering |
| Source | `11A-RS-020`, `11A-RS-019`, `11A-RS-001` (OFFICIAL, CURRENT); `11A-RS-033`, `11A-RS-034` (COMMUNITY, HISTORICAL) |
| Confidence | **High** for the official cap and rule; **Low** that the paid achievements remain obtainable |
| Second source | Yes |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Nation Supremacy's boundary is stricter and already fixed: **`NAT-045`** bars any differential by purchase, **`ECN-092`** mandates one currency with **no prestige currency at launch**, **`REQ-073`** bars converting any first-time benefit into a transfer, and the free-first constraint makes a paid reward track out of scope. Therefore: **no achievement, milestone, ranking position or event eligibility may be purchasable, and no reward may be convertible** (`11A-DR-012`). The one transferable idea is presentational — if any cosmetic ever exists, publish exactly which advantages are *not* for sale, item by item |

### 3.8 Integrity rules that constrain events and rankings

#### 11A-BM-021 — Published moderation-point bands with per-rule expiry

| Field | Content |
|---|---|
| Mechanic | Graduated, expiring, dual-approved enforcement |
| How it works | **OBSERVED.** "Each player starts with **0 Moderation Points**. Violations … may result in the issuing of Moderation Points … If a player reaches **100 Moderation Points, they will be banned**. … **Moderation Points will expire over time. The length of time before expiration will vary based on the nature of the violation, and will be listed with the rule below.** … **All moderation actions will need to be approved by at least two moderators** to prevent any individual moderator from abusing their power." Each rule publishes its own band and expiry, e.g. Creating Multiple Nations 50–100 / 1 year; War Slot Filling 25–75 / **2 years**; Bounty Coordination 25–75 / 2 years; Treasure Transfer Coordination 25–75 / 2 years; Account Selling **100 / Never**; Real-World Transactions 75–100 / Never; Screenshot Abuse 20–40 / 1 year; Exploit Abuse 50–100 / 2 years ("players have an obligation not to abuse them **and an obligation to report these**"). Automation is split finely: automated trading and banking are prohibited, but "scripts that pull up-to-date trade information through the API and **notify** players … are allowed, so long as the player is still manually completing the trade" (`11A-RS-001`) |
| Strengths | Publishing the band, the expiry and the two-approver requirement turns enforcement into a *rule* a player can predict, which is exactly the standard **B-03 `REQ-064`** ("graduated, reasoned") and **`REQ-066`** ("a shared address is never sufficient by itself") set for us. The notify-but-do-not-execute automation line is a workable boundary for a game with a public API |
| Weaknesses | Discretionary bands depend on a moderator corps — the escalation to a **never-expiring** sanction shows how rarely that trust holds. The stated exception that the operator "reserves the right to not punish players for any exploits that he deems are his fault" is honest but makes outcomes non-predictable |
| Source | `11A-RS-001` (OFFICIAL, CURRENT) |
| Confidence | **High** — the bands, the expiry periods and the two-approver rule are quoted from the live official rules page, not from a wiki |
| Relevance | **Supporting** |
| Lesson | **LESSON / DIRECTION.** Event and ranking integrity controls belong to **Prompt 12**, not to 11 — Prompt 11 may only *name the behaviour and the evidence it would need*, which is precisely the instruction in Prompt 11A §16.10 and §18 ("Do not invent moderation punishments") (`11A-RK-001`…`11A-RK-004`, §27) |

#### 11A-BM-022 — Inactivity ladder: deletion, then automatic Vacation Mode, scaled by development

| Field | Content |
|---|---|
| Mechanic | A stepped absence policy with developmental thresholds |
| How it works | **OBSERVED** from the official rules page: "**At 31 days of inactivity**, any nation with only 1 city and no active wars **will be automatically deleted**. **At 60 days**, any nation with fewer than 3 cities and no active wars will be automatically deleted. **At 90 days**, any nation with 1–5 cities will be placed into automatic Vacation Mode for **60 days**… 6–9 cities → 90 days… 10–14 cities → 120 days… 15–19 cities → 150 days… 20 or more cities → **365 days**. During this time, if the player logs in their nation will be automatically removed from Vacation Mode. **At 97 days of inactivity or greater, any nation that is not in Vacation Mode (automatic or manually entered) will be deleted for inactivity. Automatic deletion is not reversible**" (`11A-RS-001`) |
| Strengths | It scales recovery time with what the player has built, and an automatic return on login is a clean re-entry with no appeal step. The two-branch design (small nations are deleted, developed nations are parked) is a defensible capacity policy for a free-tier host |
| Weaknesses | **Irreversible deletion of a small nation is the harshest possible answer to a newcomer's absence**, and it destroys exactly the record layer a long-term progression system would want to keep. A 365-day Vacation Mode for large nations means the veteran never loses anything while the newcomer loses everything — the opposite of the fairness intuition |
| Exploit risks | Aceding out a nation for its assets; using automatic states to shelter alliance banks, which the same rules page separately prohibits (`11A-RS-001` rule 16) |
| Source | `11A-RS-001` (OFFICIAL, CURRENT) |
| Confidence | **High** |
| Second source | No — and the community Vacation Mode page (`11A-RS-042`) is an unfinished stub, which is why the official page is used |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Nation Supremacy has already taken the opposite and better position, and Prompt 11 must preserve it exactly: **`D-028`** — dormancy at 14 days/168 turns, "**suffers no resource, progression or ownership loss**", "ranking exclusion is a **presentation rule** for a nation that may return"; **`ONB-041`** — "may fall in the rankings because it is not competing, but the game does not confiscate its state"; **`ONB-046`** — archival only after **12 months**, with a 30-day notice and restorable; **`ONB-047`** — **no automatic deletion**. Consequence for this prompt: **no objective, event or ranking may require continuity of presence, and no absence rule may forfeit a permanent record** (`11A-DR-018`) |

---

## 4. Politics & War benchmark summary

| Mechanic family | What P&W actually does | Adopt | Reject |
|---|---|---|---|
| National measurement | One Nation Score serving ranking, war eligibility and event eligibility simultaneously (`11A-BM-001`) | The idea that eligibility should be *relative* and *published* (`11A-RS-028`) | One number for three purposes; raw stockpiling as merit |
| Standings | One board with thirteen switchable metrics plus separate Treasures / Moon Landing / Mars Landing / Commendations boards (`11A-BM-002`) | Plural columns from one lawful dataset; percentile alongside rank | Windowless all-time totals; casualty counts as merit |
| Public statistics | A separate world-dashboard surface (`11A-BM-003`) | Averages, distributions, rolling activity windows | Any per-nation exposure below our k = 5 rule |
| Objectives | 26 sequential tutorial steps, most mandatory, including forced alliance membership and military stockpiles (`11A-BM-004`) | System-covering discovery steps | Sequential gating; compelled membership; marketing tasks |
| Recurring engagement | Daily login streak income; rewarded-ad currency; monthly cap reset (`11A-BM-005`, `11A-BM-006`, `11A-BM-007`) | Deterministic calendar events with published effects | Presence-for-currency of any kind (`TR-085`) |
| Transient awards | One badge per category reassigned daily, tie going to the developer's nation (`11A-BM-008`) | Snapshot-boundary reassignment | Operator-favouring tie-break; single-winner daily prizes |
| Permanent honours | Closed-eligibility commemorative badges still displayed after twelve years (`11A-BM-009`) | Historical honours with no mechanical weight; world-state triggers | First-mover exclusivity as the main form; purchase-tier badges |
| Achievements | Fixed conditions, dated attribution, **published completion counts and percentages** (`11A-BM-010`) | The data model and the rarity disclosure | Attendance, purchase, employment and victim-requiring conditions |
| Event achievements | Four event achievements with payouts, 2-give/1-receive daily caps, a per-city resource cost and blockade escrow (`11A-BM-011`) | Asymmetric caps; costed interaction; escrow-not-forfeit | Currency volume |
| Annual events | Vintage tiers with prior-claim exclusion, exact expiry, two-stage teardown (`11A-BM-012`) | Teardown staging; recurring-but-not-renewable structure | Account-history differentials without justification |
| Scheduled events | Weekly lottery with a published instant, eligibility floor, one-turn pre-draw freeze, player-funded pot and declared sink (`11A-BM-013`) | **Participation freeze before any draw or snapshot**; sink-funded rewards | Long-odds randomness as achievement; wealth floors |
| World objects | 30 rotating treasures with 60-day respawn, 15–65%-of-leader score band, newcomer/inactive exclusion, seizure on war, square-root alliance bonus (`11A-BM-014`) | Relative-band selection; published timers; diminishing collective returns | Permanent yield multipliers (`ECN-113`) |
| Player events | Anonymous bounties: forfeit-on-post, ≥$1M, no self-claim, first-claimant wins, blockade escrow, **never cancellable and no expiry** (`11A-BM-015`) | Reservation at creation; player-initiated public challenges | Irrevocable capital lock with no expiry; un-coordinatable counterparty |
| Progression spine | Prerequisite chains with explicit "no competitive advantage" and "cannot be destroyed", emitting exclusive + general badges and a leaderboard row from one completion (`11A-BM-016`) | Multi-layer recognition from one milestone; indestructibility | Permanent recurring effects attached to milestones |
| War recognition | Lifetime loss and destruction counters, war win/loss totals and a dated public activity feed (`11A-BM-017`) | Participation records and a dated activity feed | Casualty and destruction totals as merit |
| Group layer | Non-geographic colour blocs with world-average-derived caps and exclusion of newcomer/inactive/unallied states (`11A-BM-018`) | Self-scaling caps; exclusion-as-presentation | Any design where the unaffiliated nation cannot progress |
| Tenure | Published age and seniority, rankable Age column, Oldest Nation award, interval-anchored commemorative badges (`11A-BM-019`) | Display and interval commemoration | Age as a competitive score or eligibility floor (`NAT-045`) |
| Monetisation | A published 20-credit advantage cap, cosmetic-only remainder, unlootable currency, never-expiring ban on real-world trading, paid badges and paid achievements (`11A-BM-020`) | Publish exactly what is not for sale | Purchasable recognition of any kind (`NAT-045`, `ECN-092`) |
| Integrity | Published moderation-point bands, per-rule expiry, two-moderator approval, notify-but-not-execute automation boundary (`11A-BM-021`) | Named behaviours with evidence requirements | Inventing punishments — those are Prompt 12's |
| Absence | Stepped deletion and automatic Vacation Mode scaled by city count, irreversible at 97 days (`11A-BM-022`) | Nothing — our position is stricter and already decided | Deletion of the absent newcomer; forfeiting records (`D-028`, `ONB-041`, `ONB-046`, `ONB-047`) |

**Depth statement.** Politics & War receives **43 source rows** (`11A-RS-001`…`11A-RS-032` official, `11A-RS-033`…`11A-RS-043` community) and **22 benchmark-mechanic entries** (`11A-BM-001`…`11A-BM-022`), and is the only game analysed across all four Prompt 11 domains plus warfare-derived recognition. The per-game tallies for the remaining benchmarks, and the running totals, are stated in the main report §5.

---

## 5. Secondary and additional benchmarks

Each subsection lists its own sources, then its mechanics, in the same field format as §3. Subsection order here is by evidence-arrival order and is **not** the section order of the main report.

### 5.1 Supremacy 1914 (Bytro Labs)

**Why selected:** a persistent multiplayer browser nation-strategy game with the same publisher family as Call of War, a **round-based competitive ladder**, and — unlike every other game in this set — a documented **cross-round seasonal point system** with published tuning revisions. Its limitation is also its most useful output: its entire scoring stack is **province-native**, so it forces us to state exactly which parts of a scoring design are abstract and which are geographic.

#### 5.1.1 Sources

| ID | Source | Type | Accessed | Currency |
|---|---|---|---|---|
| `11A-RS-044` | **How do I win a game round?**, official help centre, `https://bytro.helpshift.com/hc/en/3-supremacy-1914/faq/1-how-do-i-win-a-game-round/` | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-045` | **Game Rules**, official help centre, `…/faq/268-game-rules/` — the four legal round-end methods plus the Wolf-Packing, Account Pushing and Capital Farming definitions | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-046` | **What are Game Rounds…?** `…/faq/2-what-are-game-rounds-and-how-do-they-work/` | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-047` | **What is Morale…?** `…/faq/4-what-is-morale-and-what-can-i-do-to-keep-it-high/`; **How do I acquire more resources…?** `…/faq/47-…`; **Spies and Espionage** `…/faq/44-…` | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-048` | **I won a game round, but it didn't end or grant rewards.**, `…/faq/43-…` (marked `Last Updated: 1392d`) — the solo-vs-coalition threshold rule | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-049` | **What are Goldmarks?** `…/faq/3-…`; **What is Premium?** `…/faq/19-…` (`Last Updated: 1366d`); **All About Ad Rewards** `…/faq/132-…` (`Last Updated: 1366d`) | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-050` | **Everything About Alliances** `…/faq/107-…`; **I can't accept applications to my Coalition** `…/faq/206-…`; **Why can't I join a new game?** `…/faq/16-…`; **How do I leave or delete a game…** `…/faq/34-…` | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-051` | **What do the Diplomatic Relations mean?** `…/faq/131-…` (`Last Updated: 1392d`); **What is Diplomacy…?** `…/faq/7-…`; **Heroes and How They Work** `…/faq/537-…` (`Last Updated: 763d`) | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-052` | **Report Multiaccounting** `…/faq/279-…`; **Communication Rules** `…/faq/42-…`; dated **Release Notes** `…/faq/649-…` (2025-08-19), `…/faq/573-…` (2025-05-27), `…/faq/570-…` (2025-05-06) | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-053` | **Official Game Manual**, staff-authored and now read-only legacy forum, chapters 1–9, e.g. `https://forum.supremacy1914.com/index.php?2-joining--creating-games-en/`, `…?3-governing-your-country-en/`, `…?6-warfare-en/`, `…?9-goldmark--premium-account-en` | OFFICIAL (legacy, unmaintained) | 2026-11-04/05 | **HISTORICAL** — the manual itself carries a "read-only legacy forum, we have a new forum" notice |
| `11A-RS-054` | **Welcome to Seasons! — Season 1: Knights of the Sky**, official news, `https://www.playsupremacy.com/en/news/1914/knights-of-the-sky`, published **30 Apr 2026** | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-055` | **Season 2 is here! — Tip of the Spear**, `…/1914/tip-of-the-spear`, published **31 Jul 2026** | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-056` | **Tip of the Spear Season 2 Finale**, `…/1914/end-of-the-spear`, published **2 Nov 2026** — live standings and season rewards | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-057` | **The First-Ever Battle Pass Operation** (14 Jul 2025) `…/1914/1914-battle-pass-operation`; **The Hero Pass Returns — Firepower Unleashed** (15 Jan 2026) `…/1914/1914-the-hero-pass-returns`; **Supremacy 1914 Turns 17 — The Anniversary Campaign** (21 May 2026) `…/1914/supremacy-turns-17` | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-058` | **Terms of Service & General Conditions**, `https://www.playsupremacy.com/en/terms`, dated **20 January 2026** | OFFICIAL | 2026-11-04/05 | CURRENT |
| `11A-RS-059` | **Steam announcements mirror** for app 979920, `https://steamcommunity.com/app/979920/announcements/` and the mirrored event-feed copies (Dominion, Free for All) | OFFICIAL (mirrored) | 2026-11-04/05 | CURRENT/HISTORICAL by item |
| `11A-RS-060` | **The Index of Power and You — A Comprehensive FAQ**, `https://forum.supremacy1914.com/forum/index.php?thread/17-the-index-of-power-and-you…`; **[INDEX] Frequently Asked Questions** `https://www.playsupremacy.com/en/forums/1914/1914-strategy-discussion/index-frequently-asked-questions-f66e86f5`; **Game Rewards and Payouts** `…/game-rewards-and-payouts-2eefb878`; **Question about victory conditions** `…/question-about-victory-conditions-a845b52a`; **Never Ending Game Mode Option** `…/thread/7501-…` | COMMUNITY | 2026-11-04/05 | **HISTORICAL** (2018–2024 posts) |

**Inaccessible Supremacy 1914 surfaces (recorded, not guessed):** `https://www.supremacy1914.com/` returns only a login/registration shell to an unauthenticated request; `https://supremacy1914.com/en/game-rules` returns **404**; `https://bytro.helpshift.com/hc/en/3-supremacy-1914/categories/` returns **404** (the indexed form is `…/?p=all`); **the whole Fandom wiki returned HTTP 403 on every attempt** (`/wiki/Index_of_Power`, `/wiki/Ranks`, `/wiki/The_Daily_European`), so rank-ladder values could not be read; `…/game.php?bust=1#/ranking/alliances/` is login-gated, which is why **alliance scoring remains unverified**; several Facebook post bodies and one Steam announcement body rendered without their text; `https://www.playsupremacy.com/en/academy` exposes video tutorials only, with no written onboarding document, so **no formal tutorial could be confirmed**.

#### 5.1.2 Benchmark mechanics

##### 11A-BM-023 — Index of Power: a relative, destructible, player-published strength index

| Field | Content |
|---|---|
| Game / System | Supremacy 1914 — competitive scoring and ranking |
| Mechanic | The **Index of Power (IoP)** |
| How it works | **OBSERVED.** Official: "players are ranked by their **Index of Power** score, or '**IoP**.' This number, **displayed beside each player's name in the Daily European**, is **relative** and denotes the **share of power across all players participating in the match**." It rises by "Conquering territory", "Building and upgrading structures" and "Improving the morale of your people"; morale is "measured on a province-specific basis, and the higher your overall morale, the better your Index of Power". Crucially the same page states the index is *not* monotone in the player's own effort: "The Index of Power is a **relative number, and can fluctuate depending on the performance of your neighbours and rivals**", and lists two deliberate negative levers — "Buildings can be destroyed without annexing a province. **Morale can be damaged directly**" — executed by bombardment, bombers and spies running "sabotage and misinformation campaigns, resulting in great effects with no risk to your own forces". A community-derived per-province formula exists (`11A-RS-060`): `16 × (provinceMoral/100) − 4 + numUpg × 0.5 + moralBonus`, normalised so the total pool is `2000 × player count` |
| Trigger | Continuous recalculation from state |
| Eligibility | Every participant |
| Timing | **Published** in a **daily** newspaper; victory is evaluated more often than that |
| Scoring | Share of a normalised pool |
| Reward | Gates round victory, in-round ranking position, end-of-round premium-currency payout size and the cross-round seasonal ladder |
| Restrictions | Territory and province-morale inputs are geographic |
| Strengths | Relativity plus normalisation means the index **never needs retuning as the population changes** — thresholds expressed as a percentage of a pool are valid for a 10-player and a 500-player round alike. Because score components are destructible, a **non-territorial counter-play lane** exists: a smaller nation can reduce a rival's standing without conquering it |
| Weaknesses | A relative index lets a passive player gain standing when a rival is attacked, which weakens the "reward for play" claim. The community-derived formula "would allow for **negative score** (very low morale provinces without or few upgrades)", so an index can go below zero and behaviour at the floor becomes undefined. **Research and technology do not appear in any official component list**, contradicting the common assumption that a tech axis feeds the score |
| Exploit risks | Attacking a rival to raise your own share without taking anything; manufacturing the destruction that a scored component rewards |
| Source | `11A-RS-044`, `11A-RS-047` (OFFICIAL, CURRENT); `11A-RS-053` (OFFICIAL, HISTORICAL); `11A-RS-060` (COMMUNITY, HISTORICAL, **formula never officially confirmed**) |
| Confidence | **High** for the official definition, publicity and relativity; **Medium** for the community formula; **Low** that the coefficients are current |
| Second source | Yes for the definition (three official surfaces); No for the formula |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Two abstract devices survive de-mapping and are recommended: **express any threshold as a share of a normalised pool rather than an absolute number** (`11A-DR-019`), and **make at least one scored component destructible or erodible so that reducing a rival is a strategy that does not require accumulating** — in a mapless Nation Supremacy that means a contested asset or a stability term, never a province. Note the guardrail: our own `TR-047` requires determinism with "no environment randomness", and the negative-score failure mode shows why **every index needs an explicit floor**, which `ECN-102` ("treasury never negative") already models for us |

##### 11A-BM-024 — Four legal ways a round can end, plus a contractual override channel

| Field | Content |
|---|---|
| Mechanic | Round termination conditions as a closed enum |
| How it works | **OBSERVED.** Official Game Rules: "To End a game there are **4 possible ways**; 1. Victory Points (VP) total for victory are reached. 2. The win condition of **holding the Control Points** for a certain amount of days in Dominion games is fulfilled by a player. 3. The **game round timer reaches 0**. 4. **Retire Option** is selected by remaining active users in a round (**becomes available when 3 or fewer users remain active**)." The same page adds: "**Certain official rounds may have special rules that deviate from the standard rules. Such deviation from the standard rules will be mentioned in the event announcement or description**" |
| Trigger | Any one of the four |
| Eligibility | Branch 4 requires a population threshold |
| Timing | Branch 1 is first-to-threshold and instantaneous; branch 2 requires a sustained hold; branch 3 is a wall-clock timeout; branch 4 is a consent condition |
| Scoring | Percentage of a total point pool — legacy manual: standard "50% of all available points, i.e. 1,000 points", Domination "75%… 1,500", Supremacy "100%… 2,000" |
| Reward | Round closure and placement rewards |
| Restrictions | Deviations must be published in the announcement |
| Strengths | A **closed end-condition enum with a published override channel** is the single most reusable structural idea in this report. It makes termination auditable ("the round ended because of condition N"), gives every scenario a common vocabulary, and — critically for us — the operator-favoured branch 4 is a *population* condition, not an administrative fiat. Expressing thresholds as **percentages first and absolutes second** is what makes a threshold survive player-count change |
| Weaknesses | A timer fallback means a stalled round can hand victory to whoever farmed fastest rather than whoever achieved most. Branch 2's Control Points are geographic and unusable |
| Exploit risks | Running out the clock deliberately; a coalition mass-departing to trigger the retire branch and cancel a loss |
| Source | `11A-RS-045` (OFFICIAL, CURRENT); `11A-RS-053` (OFFICIAL, HISTORICAL, for the 50/75/100% figures) |
| Confidence | **High** for the four branches; **Medium-High** for the percentages (single legacy manual, cross-stated in two chapters of it) |
| Second source | Yes for the branch list (official rules plus community restatement); No for the percentages |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Nation Supremacy is **persistent, not round-based** at the nation level, so it has no round to end — which means this pattern transfers to a different object: the **season** and the **event** each need a closed termination enum with a published deviation channel (`11A-DR-003`, `11A-DR-018`). This is the shape that satisfies our own `TR-038` ("one published outcome per turn") without an operator improvising an end |

##### 11A-BM-025 — Solo and coalition victory thresholds are separate and non-fungible

| Field | Content |
|---|---|
| Mechanic | Two victory bars over one unified ranking |
| How it works | **OBSERVED.** Official: "There are two ways to achieve first place in a match – you can either do it **alone**, or as part of a **coalition**… there are **two victory thresholds** as a result. **A solo win requires less points than a coalition win**, but can only be achieved by a single player. **Coalition points will not count toward a solo win**, so always remember that a coalition needs to meet the coalition threshold, not the solo." Community sources quantify it as 1,000 solo against 1,500 coalition and add that "Both coalition and players not in the coalition are **ranked in the same system**". The coalition itself is mechanically bounded: "Coalitions have a **member limit**. If full, no one can join… **Limits vary by map (2 to 5 members)**" |
| Strengths | This is the cleanest available answer to the problem every alliance-based competitive system has — **a group should not simply be the sum of its members.** A unified list keeps standings legible; separate, non-convertible bars stop a coalition from claiming an individual prize. Making the *cap itself* the reference for the fairness rule (see `11A-BM-036`) means one number serves two systems |
| Weaknesses | **An unresolved contradiction in the sources.** The legacy manual presents 1,000 / 1,500 / 2,000 as *creator-selected victory modes*, while the official help article and the community present 1,000 / 1,500 as *solo / coalition* bars. No single source states both purposes together, so the specific pairing is **not** confirmed. A coalition may also pool rewards regardless of individual contribution, per community report |
| Exploit risks | Coalition membership purely to share a bar; a member deliberately dropping so the remainder holds exactly a legal configuration |
| Source | `11A-RS-048` (OFFICIAL, CURRENT — the rule itself); `11A-RS-050` (OFFICIAL, CURRENT — the 2–5 cap); `11A-RS-060` (COMMUNITY — the numbers); `11A-RS-053` (OFFICIAL, HISTORICAL — the conflicting framing) |
| Confidence | **High** that two thresholds exist and are non-fungible; **Low** that the specific 1,000/1,500 pairing is correct |
| Second source | Yes for the rule; No for the numbers |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** **Group-scope and nation-scope standings must be separate objects with separate bars, and group performance must not be convertible into an individual award.** Our own registers already forbid the merge from the other side — **B-09 `ALL-134`** ("a ballot can never bind a member nation's private treasury, cities, military, treaties or diplomacy") and **`ALL-224`** (alliance funds "may not fund a grant, loan, aid payment, reparation, refund, dividend, salary, **prize**… or private debt") — so an alliance-placed prize funded from a shared pool is impossible here by rule, independent of this evidence (`11A-DR-011`) |

##### 11A-BM-026 — A daily lead-sustain bonus converting in-round standing into cross-round progression

| Field | Content |
|---|---|
| Mechanic | The **Victory Progress** leaderboard with a duration-weighted reward |
| How it works | **OBSERVED.** Official Season 2 announcement: "To better reward successful campaigns, commanders who occupy **the top positions on the Victory Progress leaderboard** will now earn **bonus SRP each day**. **The longer you maintain your lead, the greater the reward**, giving sustained battlefield success an even bigger impact on your seasonal ranking." This is the second of two distinct in-round boards: the IoP list published in the daily newspaper, and this Victory Progress list whose **occupancy over time** is monetised into the cross-round ladder |
| Trigger | Daily evaluation of position |
| Eligibility | Top positions |
| Timing | Daily, throughout a round |
| Scoring | Position × duration of occupancy |
| Reward | Seasonal Ranking Points (SRP) |
| Restrictions | Tier thresholds are not disclosed |
| Strengths | It answers the hardest question in any persistent-account/round-based design: **what makes being first interesting on a Tuesday when the round ends in three weeks.** Rewarding *sustained* position rather than *snapshot* position also removes the pure last-instant spike incentive that a snapshot-only award creates, which is exactly the manipulation risk Prompt 11A §6.3 names |
| Weaknesses | Duration-weighting is a compounding leader bonus and therefore a rich-get-richer loop; the official counterweights are only the relative-index erosion and the defeat/inactivity penalties. Undisclosed tiers mean a player cannot plan against the threshold |
| Exploit risks | Deliberately conceding and reclaiming to reset a rival's sustain clock; a leader coasting once the bonus exceeds the value of further play |
| Source | `11A-RS-055` (OFFICIAL, CURRENT, verbatim) |
| Confidence | **High** for the rule; **Low** for any magnitude |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Distinguish **attained position** from **sustained position**, and if standing is to earn anything over time, publish the curve (`11A-DR-020`). Our own `TR-071` requires that any cap-overflow rule "be declared, deterministic and reported", and `TR-049` requires that published ordering be player-readable, so an undisclosed bonus tier would fail our conventions outright |

##### 11A-BM-027 — Rounds are isolated silos; the account persists; a concurrency cap bounds them

| Field | Content |
|---|---|
| Mechanic | Round isolation and multi-instance limits |
| How it works | **OBSERVED.** Official: "Each 'game round' is a **self-contained map**… A player may be present in multiple game rounds simultaneously, and can play as a different nation in each **with no bearing on any other match**. **Resources, provinces, units and so on may not be transferred or carried over to other game rounds**, and will only exist in the game round in which they were created or acquired. Game rounds may be **ranked or unranked, public or private**, or even have **specific rules**". On concurrency: "you can play up to **50 games** at the same time. Once you reach this cap you will not be able to play any additional rounds until one has ended." On cleanup: "Games can only be **archived**, but will only be **deleted automatically two weeks after the game has finished**." And on bookkeeping latency: "Medals and awards will show up on your profile within **72 hours**"; "It can take up to **48 hours** for our servers to update with your recent activity" |
| Strengths | Absolute isolation is what makes a competitive ladder trustworthy: nothing leaks between instances, so no accumulation converts into advantage. The **hard concurrency cap** is the cheapest structural answer to both alt-farming and world bloat, and it creates real demand for rounds to finish. **Publishing the reward latency instead of pretending settlement is instant** is a genuinely better honesty practice — the help-centre article exists only to answer "I won but got nothing" |
| Weaknesses | Deletion two weeks after finish destroys the round's history permanently, which is the opposite of what a chronicle system needs. A 50-slot cap is generous enough that the isolation property becomes a multi-account surface rather than a protection |
| Exploit risks | Parallel-instance activity as an unbounded farming surface; account-level ladder farming across many isolated instances |
| Source | `11A-RS-046`, `11A-RS-050` (OFFICIAL, CURRENT); `11A-RS-048`, `11A-RS-052` (OFFICIAL, CURRENT, latency) |
| Confidence | **High** |
| Second source | Yes for isolation (two articles) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Three transfers, all bounded by existing decisions. First, the *opposite* of this isolation is our premise — Nation Supremacy has **one shared world** (`TR-011`, `REQ-060`) — so isolation is not available to us and fairness must come from rules instead. Second, **archive rather than delete**: our `ONB-046`/`ONB-047` already mandate 12-month archival with no automatic deletion, and `TR-090` makes major events a permanent append-only class, so this row is a confirming case, not a new idea. Third, the **latency disclosure** practice is worth adopting for any delayed reward claim, since our own recovery design (`TR-077`…`TR-083`, `D-025`) already produces visible delays at a failed boundary |

##### 11A-BM-028 — A lifetime rank ladder that buys content access, never power

| Field | Content |
|---|---|
| Mechanic | Account level / "service record" as a longitudinal progression store |
| How it works | **OBSERVED.** Legacy manual: "**Minimum Rank**: Some game rounds can only be joined by players of a certain rank (**account level**). If you rise in rank, you will have **more types of maps to choose from**", with concrete gates such as "South America 1914: This scenario can only be played by players which have the rank of Staff Sergeant. (**1600 Points**)" and "Middle East 1914: … Lieutenant. (**25000 Points**)". End-of-round play raises it: "Each ranked game will award you with a certain amount of Goldmark depending on your final Victory Points score, **as well as an increase in account level and combat stats**". The store has a documented name — deactivating anti-cheat means "**no points will be awarded on your service record**" |
| Strengths | **This is the cleanest persistence design in the whole benchmark set and it is entirely map-free.** The ladder is *earned across rounds and spent on content access*, not on competitive advantage: a veteran gets more *choices*, never more *power*. Naming the longitudinal store ("service record") separately from the in-round index also keeps the two concepts from merging |
| Weaknesses | The quoted gates are not monotonic in the rank ordering the same chapter implies, so the ladder's shape is unclear; a rank-only entry requirement can exclude a specialist who never grinded the general ladder; **the full rank table could not be obtained** because the Fandom page returned 403 |
| Exploit risks | Grind-through-low-difficulty content purely for ladder points |
| Source | `11A-RS-053` (OFFICIAL, **HISTORICAL**, legacy manual), `11A-RS-060` (COMMUNITY, fragmentary) |
| Confidence | **Medium** that the mechanic exists; **Low** for the specific values; current availability **UNVERIFIED** |
| Second source | Weak (two chapters of the same legacy manual) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** "Progression that unlocks *options* rather than *power*" is the single most transferable idea from this game, and it fits our constraints better than any P&W device because it can be expressed without touching the economy at all. Note the hard conflict, though: `NAT-045` bars any differential by account age, and `URB-158` forbids a reward that "grant[s] a city, a facility, capacity, a technology or a permanent yield multiplier" without a decision and a register row — so an access-unlock ladder in Nation Supremacy must unlock *non-power choices* only, which is exactly what `11A-DR-017` requires |

##### 11A-BM-029 — Ranked status as the precondition for any progression credit

| Field | Content |
|---|---|
| Mechanic | Anti-cheat opt-in gating the award of points |
| How it works | **OBSERVED.** Legacy manual: "**Anti-Cheat**: The Anti-Cheat System prevents multiple users from logging into the game from the same internet connection. You can **deactivate** the Anti-Cheat System to allow for family and friends to play together. However, **games with deactivated Anti-Cheat will not be ranked, meaning that no points will be awarded on your service record.**" Community: "For gold rounds the rule is that these are **ranked once 2 human players have joined and become active**" |
| Strengths | Elegant in three ways: the fairness system is a **precondition for scoring** rather than a separate policing layer; opting out is an **explicit, player-visible choice** with a stated cost rather than a hidden suspicion flag; and the "won't be ranked" framing means the excluded player is not accused of anything. A minimum-active-participants floor before a ladder engages is the correct answer to a low-population world |
| Weaknesses | It effectively taxes legitimate co-resident households out of progression — the very situation our own **D-034** and **`REQ-080`** handle by *reviewing* pair restrictions rather than penalising co-residence ("no standing co-resident exemption exists; co-residence is reviewed, not self-certified"). A 2-player floor is also a bare minimum for a ladder to mean anything |
| Source | `11A-RS-053` (OFFICIAL, **HISTORICAL**, single source); `11A-RS-060` (COMMUNITY) |
| Confidence | **Medium** |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Two adoptions and one rejection (`11A-DR-021`). Adopt the **eligibility-floor-before-a-ranking-means-anything** rule and the **"not ranked" rather than "you are suspected"** framing, which is honest about capability limits in the way **`REQ-077`** demands ("no text may claim perfect person-level identification"). Reject the co-residence opt-out, because our pair model deliberately separates a *pair state* from a *sanction* and a *ranking exclusion* |

##### 11A-BM-030 — Seasonal Ranking Points: symmetric gain and loss, equal start, every match counts

| Field | Content |
|---|---|
| Mechanic | A cross-round seasonal ladder, its Season 1 rules and its Season 2 revision |
| How it works | **OBSERVED.** Season 1 (official, 2026-04-30): "**Over the course of three months**, you will compete to climb the seasonal leaderboard… Our first season will run from **May 5th to August 3rd**… **every player starts the season with the same amount of rank points**. **Killing enemy units and conquering enemy provinces will increase your points, while losing units and provinces will decrease them.** The higher your points, the higher your position on the leaderboard. **Every match will have an impact on your rank**… all matches started after May 5th will impact your rank… Season 1 … serves as a **testing ground** … We will continue refining how points are gained and lost." Scoping and staging are explicit: "Your matches, **regardless of platform**, will contribute to your seasonal rank", but "the season's leaderboard will be exclusive to unity"; and "**as ranks will not be visible in the beginning, we will periodically update you with news posts and highlight the best players**"; "Looking ahead, we are preparing a **Hall of Fame**, where the greatest commanders of each season will be immortalized." Season 2 (official, 2026-07-31) is the tuning pass: SRP are earned "by eliminating enemy units (**excluding infantry**) and conquering provinces"; "**losing units will now carry a slightly higher penalty**"; "players who are **defeated before the match concludes will receive a one-time defeat penalty**"; "we've added a **small inactivity penalty**. Commanders whose nation is **taken over by AI** will lose a portion of their SRP"; rewards include "Hero Medals" and "unlock our new unit by **placing high enough on the leaderboard** by the end of the season". Season 2 finale (2026-11-02) publishes live standings — "SPQR with **210,752 SRP**", runners-up 166,554 / 148,212 / 141,639 / 118,904 — and the cut: "**Light Artillery unlock for top 5000**" |
| Strengths | **Four anti-inflation controls, all portable and none of them geographic:** (1) excluding the cheapest unit class from the kill economy protects the point source from volume farming; (2) **symmetric** gain and loss, so trading damage cannot be net-positive; (3) a **one-time defeat penalty**, which prices early exit without confiscating anything already earned; (4) an **inactivity penalty anchored to an existing game-state event** ("taken over by AI") rather than to a separate absence timer. Equal-start-per-season is the cleanest possible answer to veteran advantage, and a **top-5,000** reward band is wide enough that a committed mid-ladder player can realistically reach it |
| Weaknesses | The daily leader-sustain bonus (see `11A-BM-026`) is a compounding advantage and the published ladder shows the leader running away. **No numeric value for any SRP delta is disclosed anywhere** — the rules are qualitative, so the ladder cannot be independently reasoned about. Shipping the ladder before its user interface, substituted with news posts, is honest staging but a poor player experience. "Every match counts" also makes throwaway and alt matches score-bearing |
| Exploit risks | Multi-account match feeding; deliberately entering many low-effort matches to accumulate small positives; timing surrenders to dodge the defeat penalty in unranked settings |
| Source | `11A-RS-054`, `11A-RS-055`, `11A-RS-056` (OFFICIAL, CURRENT) |
| Confidence | **High** for the rules as announced; **Low** for any magnitude, none of which is published |
| Second source | Yes (third-party reporting confirms the top-5000 cut and medal names) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** This is the benchmark's most complete **seasonal-vs-permanent** separation: the ladder resets, the medals and unlocks persist, and the honours list is intended to be permanent. It is directly compatible with our rules and is adopted in `11A-DR-013`. Two explicit cautions for 11B. First, an **absence-linked penalty collides with `D-028`** — a dormant nation "suffers **no** resource, progression or ownership loss" and exclusion "is a presentation rule for a nation that may return" — so a season may *stop accruing* during dormancy but may never *subtract*. Second, the equal-start-per-season device is the answer to the progression-inflation problem in Prompt 11A §15.3, and it costs nothing to adopt |

##### 11A-BM-031 — Stability as a scored, erodible input with banded severity thresholds

| Field | Content |
|---|---|
| Mechanic | Province morale as a multi-determinant value feeding score, production and construction |
| How it works | **OBSERVED.** Official: morale is "the sum total of your people's will to fight, their loyalty toward you as their leader, and the overall health of a province", and low morale causes "longer construction and recruitment times, slower healing rates… and even **outright rebellion**". Restoration has three distinct paths: "**Propaganda campaigns. Strong garrisons. Growth over time**" — with the paid option "launch a propaganda campaign and directly raise your Morale on a province-by-province basis" and the asymmetry that recovery is slow and only applies "provided **nothing is acting directly against it**". Damage sources: "Bombardment, invasions, **border friction** and sabotage". The legacy manual gives the determinant list: capital distance, enemy armies present, buildings, "**Expansion**: each new province you own affects your province morale — **starts at 8% of all provinces owned — ends at 50%… max penalty is 35**", neighbours' alignment, and "**Availability of Resources**: if there is a shortage of certain resources in your overall economy province morale will suffer"; "provinces with **low morale (less than 33%) have a high risk of revolts**. Revolts damage or kill garrison troops or **change the owner of a province**"; and "If you find your province's morale dropping for no apparent reason, **a hostile spy might be the cause**". Combat effect is bounded: "Infantry strength is affected by their current morale… decreasing in a linear fashion with sinking morale (**up until 55% morale — after that, damage is not reduced further**)". Conquest sets a cliff: "**Conquering a province will also reduce its morale to 25%, making revolts very likely**", and "**as long as the new owner does not increase its morale to more than 80%, the previous owner will have the chance to re-conquer the lost province**" |
| Strengths | A **three-band severity ladder where different systems consume different bands** (combat floor at 55%, score-negative below 25%, loss-of-control at 33%) is a genuinely good architecture: it means one variable has several consumers, each reading a different threshold, and it is why the **linear-with-floor** combat curve prevents a death spiral — a degraded player is weakened but never powerless. The **over-expansion penalty as a bounded ramp between two percentages** is a reusable anti-snowball shape. The "**claim window until the holder demonstrates stable control**" is the strongest single comeback device found anywhere in this research set and needs no map at all |
| Weaknesses | Province-scoped throughout; revolt-driven ownership transfer is a non-military conquest path that presumes territory. Hidden sabotage detectable only "for no apparent reason" is an anti-pattern against our transparency pillar |
| Exploit risks | Capital farming — the game bans "recruiting other users **with the purpose of harvesting capital cities** with the intention to receive cash and/or morale boosts" (`11A-RS-045`), which documents exactly the exploit class a scored-destructible hybrid creates |
| Source | `11A-RS-047` (OFFICIAL, CURRENT); `11A-RS-053` (OFFICIAL, **HISTORICAL** — all numeric thresholds) |
| Confidence | **High** for the qualitative model; **Medium** for the numeric bands (single legacy chapter, internally consistent) |
| Second source | Partial (HS and manual agree on the morale→production→score linkage) |
| Relevance | **Supporting** (directly for `11A-BM-032` scoring; indirectly for progression) |
| Lesson | **LESSON / DIRECTION.** The claim-window and the bounded over-expansion ramp are the two transfers, recorded in `11A-DR-022`. Both are admissible under our own politics rules in a way they would not be in P&W: **`DMP-141`** permits an event to "move a support through a **named event term** added to the formula by a decision, or grant a **one-time approval change** through the normal target-and-cap path", but forbids setting approval directly and forbids any reward granting "population, a policy, a government or legitimacy" — so a stability-shaped event is legal only through a named, decisioned term |

##### 11A-BM-032 — Event as a parameter tuple, and the Anonymous Round as a map-free variant

| Field | Content |
|---|
| Mechanic | How special rounds and scenarios are specified |
| How it works | **OBSERVED.** The anniversary campaign lists a schedule of **rotating event maps** each defined by a tuple — "*Swift Strike: 10x speed, free country selection, inactive after 1 day, **fixed runtime of 4 days**. Starts immediately.*", "*Arms Race: 2x speed, random country selection, inactive after 48 hours, fixed runtime of 28 days*", "*Gold Rush: play on a 500 player map at 4x speed with **drastically increased Goldmark rewards***", plus "*FFA*", and an explicit start instant ("Event maps start at 11:00 AM CEST"). Round *creation* exposes the same knobs plus rule-changing paid options: "**Anonymous Round**: it will **not be visible which character in the game is played by which user until the game ends**"; "**Team Settings**: '**Betrayal among team members is not possible, because they cannot attack each other**'; "**Victory Conditions**" selecting the 50/75/100% ladder; "**Maximum Inactivity**: days of inactivity after which a human player is taken over by the AI… a value of **2 to 5 days**… standard value of **5 days**"; "**Peace Period**: during peace period it is not possible to declare war, attack any human players, **or be attacked by them**… **This non-aggression pact cannot be broken. You can set a peace period for up to 14 days**" |
| Strengths | Defining an event as a **tuple of existing knobs** — cadence multiplier, fixed runtime, assignment mode, inactivity limit, reward multiplier, victory variant, identity visibility — is precisely how a game with no content team ships variety. **The Anonymous Round is the best single event idea in this report for a mapless game**: hiding which player controls which nation is purely a *social-information* rule, costs nothing to implement, needs no geography, and changes the entire strategic texture by disabling reputation-based coordination. The **unbreakable symmetric peace period** — "or be attacked by them", "cannot be broken" — is also exactly the shape of our own `ONB-020`/`ONB-023` newcomer protection |
| Weaknesses | The paid creation options make *rules* a purchasable right ("**having a Premium Account is required to create games**"; a gold-feature round "subtract[s] 5,000 Goldmark from your account. The same amount will be subtracted from all players who are joining"), which is pay-to-shape-the-world, a category our constraints exclude. Anonymous rounds simultaneously *enable* undetected collusion until reveal |
| Exploit risks | Anonymous rounds used to hide a wolf-pack; reward-multiplier rounds timed for farming |
| Source | `11A-RS-053` (OFFICIAL, **HISTORICAL** for creation parameters), `11A-RS-057`, `11A-RS-059` (OFFICIAL, CURRENT for the event schedule) |
| Confidence | **High** for the event tuple and the 2026 schedule; **Medium-High** for creation parameters (legacy manual) |
| Second source | Yes (third-party reporting mirrors the 2026 event schedule) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **event-as-parameter-tuple** model as the core of the 11A event recommendation, because it is the only architecture compatible with the AP-003 guardrail "events are systemic, not authored live-ops" (`11A-DR-001`): each event type is a data row over shared machinery, not bespoke content. Adopt the **identity-visibility variant** as a candidate event modifier (`11A-DR-006`). Reject paid rule-shaping entirely — `NAT-045` bars any differential by purchase and `D-021`/`ECN-020` exclude paid progression |

##### 11A-BM-033 — Objectives as "Operations", with a two-track pass and a published non-paywalled floor

| Field | Content |
|---|---|
| Mechanic | Mission-style recurring objectives and their reward lanes |
| How it works | **OBSERVED.** No formal tutorial could be found in any official source — the written help centre, the video-only Academy and dated release notes are all that exist. Objectives instead appear as **Operations**: "a single Operation will feature **two reward tracks** — a **standard free lane**, and a second **premium lane** packed with additional spoils… **Free Track** – Accessible to all players. **Earn rewards by completing objectives**… **Premium Track** – Unlocked by purchasing the Battle Pass… grants substantial additional rewards, **all earned through the same mission progress**… '**There's no extra grind: each completed task advances both tracks simultaneously**'… '**Operations are not becoming pay-only. The majority will continue to be free** … the **Free Track still grants meaningful progress — including Hero unlocks**'". Difficulty is deliberately tiered at the trivial end for reactivation: "**Operation Happy Birthday Supremacy**: **Capture a single province** during the celebration period to complete the operation and claim your anniversary reward. One province. One advance. One gift", against "**Operation Trajan**: **Progression in this Operation is exclusive to the Anniversary event maps**". Rewards are **claimed rather than auto-granted** — a release note fixes "the UI when purchasing the Battlepass and **claiming previously unlocked rewards**". Daily engagement is ad-funded: "you can watch a **limited amount of ads every day**… 1. **Goldmark**… 2. **Premium Membership** (of a certain duration)… the respective Premium Membership time will be **added to whatever Premium Membership you have already acquired**" |
| Strengths | "Each completed task advances both tracks simultaneously" is **the clearest published fairness commitment in this entire research set** — it states that a paid lane cannot increase the *work* required, only the *return*, and it is the opposite of the double-grind most battle passes create. A one-action operation for lapsed players is a legitimate re-entry design distinct from a grind task. Making completion a **claim** step gives the player agency and gives the system one auditable transaction |
| Weaknesses | The premium lane still converts the same progress into materially more power ("significantly boosts your ability to level them quickly and fully"), so the fairness statement is about effort, not about outcome. Ad-watching for stackable premium time is presence-and-attention monetisation. The absence of any real tutorial means new players learn from Operations whose semantics are competitive |
| Exploit risks | Trivial-completion farming of anniversary operations; automation pressure against daily ad caps |
| Source | `11A-RS-057` (OFFICIAL, CURRENT), `11A-RS-049` (OFFICIAL, CURRENT), `11A-RS-052` (OFFICIAL, CURRENT) |
| Confidence | **High** |
| Second source | Yes (the anniversary post and the battle-pass post describe the same structure) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt two things (`11A-DR-009`, `11A-DR-012`). First, the **single-progress, multiple-outcome** discipline — one completed objective should emit all of its recognition at once rather than requiring repeated passes, which is the same shape as `11A-BM-016`. Second, **a low-barreled re-entry objective class distinct from the competitive class**, which is directly relevant to the "casual or returning player" profile in Prompt 11A §17. Reject the paid lane absolutely: our own `NAT-045`, `ECN-092` and the free-first constraint make a premium track impossible, and **`TR-085`** bars the ad-and-presence loop |

##### 11A-BM-034 — Separating the persistent group from the in-round competitive group

| Field | Content |
|---|---|
| Mechanic | Alliance (cross-round identity) vs Coalition (in-round scoring unit) |
| How it works | **OBSERVED.** Official: "An **alliance** is a group of players who've chosen to band together and **co-operate outside of individual game rounds**. Alliances can help you and your friends **forge a distinct identity** as a group, and co-operate to **move up the rankings**." A **coalition** is the in-round object: "Coalitions have a member limit… Limits vary by map (2 to 5 members)"; "Coalitions are diplomatic relations offering chat and rankings. Leaders manage applications." Recognition is split accordingly: **SRP and Victory Progress are individual**, while **the win itself is coalition-scoped**. **No official alliance scoring formula, ranking metric or alliance victory condition could be found** — `11A-RS-050` asserts "move up the rankings" without defining the measure, and the in-game alliance-ranking route is login-gated |
| Strengths | The two-layer separation is exactly the problem Nation Supremacy has: our B-09 Alliance is one persistent object with no separate competitive grouping, so an *alliance ranking* would have to be derived. Splitting identity from competition keeps the group meaningful without making it a scoring machine |
| Weaknesses | The alliance ranking is asserted but undefined — the flagship claim about the group object has no documented metric. Community report that a coalition "all get the same amount of rewards, even if 90% of the points are from one individual" is precisely the attribution failure a group ladder must solve |
| Source | `11A-RS-050`, `11A-RS-051`, `11A-RS-053` |
| Confidence | **High** that the two-layer split exists; **UNVERIFIED** for any alliance score |
| Second source | No |
| Relevance | **Supporting** |
| Lesson | **LESSON / DIRECTION.** **Do not assume an alliance ranking is well-defined — none in this benchmark documents its formula.** Combined with **`ALL-224`** (no prize funding) and **`ALL-156`**/`REQ-057` (visibility classes, applicant and member data minimisation), the supported conclusion is that alliance-scope recognition in Nation Supremacy must be **aggregate, k ≥ 5 protected and never a funding source** (`11A-DR-011`) |

##### 11A-BM-035 — Diplomacy as a graded ladder of information and economic rights

| Field | Content |
|---|---|
| Mechanic | Six-tier diplomatic relationship states |
| How it works | **OBSERVED.** Official: **At War** ("You will **not be able to trade** with this nation through the resource market, and your provinces will **suffer a morale penalty for being at war**"); **Ceasefire / Trade Embargo** ("If you are at war… this option will be listed as 'Ceasefire.' If you are at peace, it will be a 'Trade Embargo.' … trade via the resource market will not be possible"); **Peace**, "The **default setting**. A neutral state — trade is possible"; **Right of Way**; **Shared Map** (exposes "your map and the positions of your units… their **specific army composition**"); **Shared Intelligence (Premium-only)**, which additionally "provide[s] intel regarding any maps that have been shared with you by other nations" — a **transitive** information graph. Espionage has no friendship exemption: spies work "all around the world, **whether allied, enemy or neutral**". Diplomatic messages "while ostensibly private, **may be leaked by enemy Espionage operations, or even by the recipient**" |
| Strengths | **Default = neutral, not hostile** is a load-bearing choice that materially reduces forced conflict, and ours matches it (`DIP-023`: "the default is NEUTRAL"). The ladder's real currency is **information and trade rights, not buffs** — which is the correct shape for relationship tiers in a game where we forbid diplomatic reputation scores (`DIP-084`). The **transitive-intelligence tier** is a strong idea for a mapless world: alliance value becomes reach, not adjacency |
| Weaknesses | The top tier is paywalled, which converts information access into a purchasable. War's built-in morale penalty and trade lock are asymmetric costs that make diplomacy punitive rather than expressive |
| Source | `11A-RS-051`, `11A-RS-047`, `11A-RS-053` |
| Confidence | **High** |
| Second source | Yes |
| Relevance | **Supporting** |
| Lesson | **LESSON / DIRECTION.** A diplomatic-*activity* ranking is therefore expressible only as **counts of published facts**, never as a derived standing — which is what `DIP-084`/`DIP-088` already require ("The count has no mechanical effect… It is displayed on the public nation page and in the treaty history. **A player may use it; the game does not**"). Recorded in `11A-DR-023` |

##### 11A-BM-036 — Fairness definitions written as intent tests against a mechanical cap

| Field | Content |
|---|---|
| Mechanic | The three named competitive offences |
| How it works | **OBSERVED.** Official Game Rules: "**Wolf-Packing** … 1. A user or a group of users that **follows another user around games** with the purpose of harming his gaming experience. 2. **Joining a game round with a group of players that exceeds the maximum coalition size of that map and playing cooperatively. You may join a game round with a group of players that exceeds the maximum coalition size but you need to play the game as if you were not allied.**" "**Account pushing** … **solely or mainly joining a game to aid another user, not to play the game**. This includes but is not limited to giving away or willingly receiving resources and provinces or **allowing uncontested takeovers of territories**… Account pushing is **not contingent on a certain date of joining**." "**Capital farming** … It is not allowed to exercise capital farming, which is the act of **recruiting other users with the purpose of harvesting capital cities** with the intention to receive **cash and/or morale boosts**" |
| Strengths | These are the best-drafted competitive-integrity rules in the benchmark, for three reasons. (1) **The violation is defined against the mechanical cap** — "exceeds the maximum coalition size **and** playing cooperatively" — which preserves the right to join a round with friends while protecting the scoring invariant, and means the fairness rule and the balance parameter reference one number rather than two. (2) "**Not contingent on a certain date of joining**" shows they learned that timing-based defences are evaded and intent-based definitions are not. (3) Capital farming is defined by **purpose** ("recruiting other users with the purpose of harvesting"), which correctly identifies that the exploit is manufacturing the scored event, not performing the move |
| Weaknesses | All three are intent tests, which makes them moderator-judgement dependent and unverifiable by a machine — the same reason `REQ-077` forbids claiming perfect identification |
| Source | `11A-RS-045` (OFFICIAL, CURRENT, near-complete verbatim) |
| Confidence | **High** |
| Second source | Not required — it is the vendor's own rulebook |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Record the three patterns as **behaviours that our objectives, events and rankings must not make profitable**, and hand the rule and consequence to **Prompt 12** as required by §16.10 ("Prompt 12 owns the broader moderation and enforcement specification"). Specifically: any reward for *participation volume* invites account pushing; any reward for *being beaten* invites capital farming; any group threshold above a mechanical cap invites wolf-packing. Entries `11A-RK-005`…`11A-RK-007` carry these forward |

##### 11A-BM-037 — Score-credit latency, archiving and the terms-level account rule

| Field | Content |
|---|---|
| Mechanic | Operational promises around settlement and history |
| How it works | **OBSERVED.** "there may be a **delay in your rewards**"; "Medals and awards will show up on your profile **within 72 hours**"; "It can take **up to 48 hours** for our servers to update with your recent activity"; "Games can only be **archived**, but will only be **deleted automatically two weeks after the game has finished**". Reporting is player-initiated and evidence-shaped: "In order to report an incident of **Multiaccounting, Account Pushing, Wolfpacking or other examples of unfair play**… make sure the email contains **the title of the game** in the subject line… the **usernames** of the players you'd like to report, and **the game ID** you encountered the situation in. Any additional details are welcome… **the countries the players are using**, and **the situation that led you to suspect foul play**" — prefaced by the admission "**While we work on improving our Multiaccounting detection and response systems**". The Terms of Service (2026-01-20) state "**Each Participant may register for and use one Account only**… **Registering for and using multiple accounts is strictly prohibited**", prohibit "**the automated opening of gaming accounts**", prohibit mechanisms "which may interfere with the function or the course of the game", and prohibit attempts "to buy or sell these virtual items for **'real' money**". Multi-instance limits: "up to **50 games** at the same time" |
| Strengths | Stating detection is incomplete while specifying exactly what evidence a report must carry is the honest enforcement posture our own security report calls for (review-then-act, no surveillance posture, no claimed perfect detection). Naming the required evidence fields is a good template for the `11A-RK` register's "future acceptance-test requirement" column |
| Weaknesses | Two-week history deletion is the opposite of a chronicle. A 72-hour medal delay on a game with 2-hour turns means the recognition layer lags the game by ~36 turns |
| Source | `11A-RS-052`, `11A-RS-050`, `11A-RS-058`, `11A-RS-048` |
| Confidence | **High** |
| Second source | Yes |
| Relevance | **Supporting** |
| Lesson | **LESSON / DIRECTION.** Adopt the **evidence-field discipline** for every risk row in §18, and reject the deletion policy: our `TR-090` makes "major world events, milestones" a **P-class permanent append-only** record and `ONB-047` forbids automatic deletion |

### 5.2 Additional benchmark — Call of War: World War 2 (Bytro Labs)

**Selection rationale:** same publisher lineage as Supremacy 1914, but with **multiple simultaneous termination channels** and a **research tree that is partly account-persistent**. It is therefore the best available model for *how a competitive round ends without geography being the reason it ends*, which is exactly the problem a mapless game must solve abstractly.

| ID | Source | Type | Accessed | Currency |
|---|---|---|---|---|
| `11A-RS-061` | **VICTORY CONDITIONS**, Bytro's own official game wiki, `https://wiki.callofwar.com/wiki/VICTORY_CONDITIONS` | OFFICIAL | 2026-11-05 | CURRENT (index date 2020-12-18) |
| `11A-RS-062` | **Game Rules**, Call of War Help Center, `https://bytro.helpshift.com/hc/en/4-call-of-war/faq/196-game-rules/` | OFFICIAL | 2026-11-05 | CURRENT |
| `11A-RS-063` | **RESEARCH**, official game wiki, `https://wiki.callofwar.com/wiki/RESEARCH` | OFFICIAL | 2026-11-05 | CURRENT with caveat (index date 2022-01-04; the elite/blueprint economy has been revised repeatedly) |
| `11A-RS-064` | **Call of War Help Center index**, `https://bytro.helpshift.com/hc/en/4-call-of-war/` and `…/hc/en/4-call-of-war-world-war-2/` — categories Basics/Beginners, Your Account, Premium & Gold, Units, Economy, Research, Rules, News & Updates | OFFICIAL | 2026-11-05 | CURRENT (category listing only; article bodies unread) |
| `11A-RS-065` | **Victory Conditions?** forum thread, `https://forum.callofwar.com/index.php?thread/20901-victory-conditions/` | COMMUNITY | 2026-11-05 | **HISTORICAL** (2017-12-14) |

**Inaccessible:** `www.callofwar.com` and its help root return a login/SPA shell with no gameplay content; **`callofwar.fandom.com` returned HTTP 403**, so no Fandom evidence exists for this game.

##### 11A-BM-038 — Threshold-triggered end, adjudicated by ranking

**OBSERVED.** Victory Points are "gathered by conquering other nation's provinces"; once the threshold is exceeded, "**the game round will end at the next day change event**. The player or coalition with the most [VP wins]" (`11A-RS-061`). Thresholds vary per scenario; round tiers are documented as **Small 35 days, Medium 49 days, Big 70 days** (`11A-RS-061`), and rounds may also be dissolved administratively — "**Retirement occurs with 3 active players**" (`11A-RS-061`, `11A-RS-062`).

**INTERPRETATION.** Victory is a **two-stage process**: a condition detects the end, but the outcome is settled at the **next scheduled boundary**. That is exactly the shape our engine already mandates — `TR-030` (no grace period), `TR-028`/`TR-029` (a boundary instant belongs to the later turn) and `TR-038` (one published outcome per turn). A separate documented lesson is the **dissolution rule**: a stalemate/low-population termination condition is a necessary part of any bounded competitive structure and is routinely forgotten.

**Confidence** Medium-High (single official source for the day-change coupling; the "3" figure came from a summarised fetch). **Relevance Direct.** **Lesson** — any season or event end must be **evaluated on state and applied at a boundary**, never applied instantaneously; recorded in `11A-DR-003`.

##### 11A-BM-039 — Hold-an-objective victory as the non-accumulation win path

**OBSERVED.** A distinct mode where the win condition is *holding*, not scoring: "The win condition of **holding the Control Points for a certain amount of days** in Dominion games is fulfilled by a player" (`11A-RS-062`, echoing the Supremacy 1914 rules at `11A-RS-045`), quantified by the official wiki as **hold >50% of Control Points for 3 days** (`11A-RS-061`).

**INTERPRETATION.** This decouples victory from territory *area* and re-couples it to a **fixed scarce set of contested slots with a majority-hold requirement sustained for N periods**. The slot set is geographic in these games; the **structure** — fixed cardinality, majority, sustained, contestable, comeback-windowed — is not.

**Confidence** High (two official sources agree). **Relevance Direct.** **Lesson** — the strongest candidate for a non-military-but-competitive objective class in Nation Supremacy is **sustained majority control of an abstract, scarce, non-spatial slot**; `11A-DR-002`. Note the incumbent-lock-in risk, which the "sustained for N" clause both creates and limits.

##### 11A-BM-040 — Research tree as the longitudinal spine, with a persistence seam

**OBSERVED.** "Research is an important aspect in Call of War, as it allows you to unlock higher unit levels as well as new unit types"; **two research slots run concurrently**; elite unit tiers require **blueprints** as a collectible gating item; "Research **persists if all elite blueprints collected**"; "Upgrades cost 50% production time/resources" (`11A-RS-063`).

**INTERPRETATION.** Two useful and two dangerous properties. Useful: a **time-gated, slot-limited** tree caps how fast one nation can sprawl, and a **collectible-gated** tier gives a longitudinal reason to keep a record at all. Dangerous: an all-or-nothing persistence rule ("persists if **all** collected") strands investment, and slot queues make paid acceleration the dominant lever.

**Confidence** **Low-Medium** — the wiki render was terse and partly garbled; "50%" and the persistence clause were **not** confirmed by a second source. **Relevance Direct** (progression). **Lesson** — **slot-limited, time-gated progression is adoptable**; **all-or-nothing cross-round persistence is not**, because our `RRL-013` destroys a rerolled nation's research and achievements, and `URB-098`/`URB-099` make research national, permanent and never retroactive. `11A-DR-017`.

##### 11A-BM-041 — Conduct rules name the two canonical round-game exploits

**OBSERVED.** The official Game Rules article defines prohibited conduct including **wolf-packing** and **account pushing** ("feeding villages/units to another account") alongside the victory conditions, and states no rankings, quest or daily-reward rules at all (`11A-RS-062`).

**Confidence** Medium (concepts confirmed present; exact wording not captured). **Relevance Supporting.** **Lesson** — the same two patterns as `11A-BM-036`; they carry to `11A-RK-005`/`11A-RK-006`.

**Unverified for Call of War, recorded as gaps:** any national **strength index or leaderboard**; **objectives/quests, tutorial flow, daily-login rewards** and Gold-economy specifics; **events and special rounds** as documented mechanics (a 2017 community thread reports surprise round endings, `11A-RS-065`, which is anecdote not rule); per-scenario VP **threshold values**; whether research genuinely persists across rounds; the exact retire-at-3 number; the legal definitions of the two offences.

### 5.3 Additional benchmark — Tribal Wars (InnoGames)

**Selection rationale:** the best-documented **derived, non-military national strength score** in existence — points that are a pure function of *completed construction* — plus a per-world-type **persistence seam** that answers "what survives a reset" without a global rule.

| ID | Source | Type | Accessed | Currency |
|---|---|---|---|---|
| `11A-RS-066` | **What are Points and how to get them?**, Tribal Wars Support, `https://support.innogames.com/kb/TribalWars/en_DK/1264` | OFFICIAL | 2026-11-05 | CURRENT (with a conflicting clause — see below) |
| `11A-RS-067` | **World Types in Tribal Wars**, `https://support.innogames.com/kb/TribalWars/en_DK/6995/World-Types-in-Tribal-Wars` | OFFICIAL | 2026-11-05 | CURRENT |
| `11A-RS-068` | **FAQ – Game Mechanics & Features**, `https://support.innogames.com/kb/TribalWars/en_DK/5970` | OFFICIAL | 2026-11-05 | CURRENT (partial coverage) |
| `11A-RS-069` | **General Info**, Tribal Wars **2** Support, `https://support.innogames.com/kb/TribalWars2/en_DK/1536` | OFFICIAL | 2026-11-05 | CURRENT (different title, used only as corroboration) |
| `11A-RS-070` | **Rules**, `https://www.tribalwars.us/page/rules`; **Winning condition** forum thread `https://forum.tribalwars.us/index.php?threads/winning-condition.5534/` (2013-01-31); **New World – Summer Special 2026**, `https://forum.tribalwars.net/index.php?threads/summer-special-2026.294215/` (2026-07-17); **Victory conditions**, `https://forum.tribalwars.net/index.php?threads/victory-conditions.159560/` | OFFICIAL (rules) / COMMUNITY (forums) | 2026-11-05 | Mixed: 2026 forum post is CURRENT; the 2013 thread is HISTORICAL |
| `11A-RS-071` | **Travian** encyclopedia entry, `https://en.wikipedia.org/wiki/Travian` | COMMUNITY (encyclopedic) | 2026-11-05 | **HISTORICAL** — the 2026 encyclopedia text lags the live game; used only for the culture-point cross-reference in `11A-BM-043` |

**Inaccessible:** no official Tribal Wars rankings/snapshot or archive article could be found — a targeted support-knowledge-base search returned **"No results found"**; the mechanics FAQ returned "No info on culture points, farming, rankings, medals, NPC villages, dominance, or OGA".

##### 11A-BM-042 — Points as a pure function of completed construction, recalculated lazily

| Field | Content |
|---|---|
| Mechanic | The national/village **points** measure and its ranking coupling |
| How it works | **OBSERVED.** Official support article: "**You receive points for the completion of buildings. As soon as the building is finished, your points and place in the ranking are newly calculated (sometimes the recalculation can be delayed to reduce server load). No points are awarded for research or the recruitment of units.**" The sibling title states the display rule: "Each building has a point value, and the sum of all building points is displayed on your city in the map overview" (`11A-RS-066`, `11A-RS-069`) |
| Trigger | Building completion |
| Eligibility | Every village |
| Timing | Recalculated on completion, **deliberately batched under load** |
| Scoring | Sum of fixed per-building point values |
| Reward | Rank position |
| Restrictions | Research and recruitment excluded (single-source clause — see Weaknesses) |
| Strengths | This is the **mapless-legible scoring model**: `rank = f(things you finished)`. No army, no fleet, no territory adjacency — just durable completed development. That is directly compatible with our B-05 asset model, where cities are permanent and non-deletable (`URB-035`) and infrastructure has a hard floor (`URB-040`). The **lazy, load-shedding recalculation** is also a real engineering precedent for a 2-hour global turn: settle standing at boundaries, not on every action |
| Weaknesses | A **documented conflict**: the official clause "no points… for the recruitment of units" contradicts widespread community expectation that Tribal Wars points include unit and wall values which fall when troops die. The population-points-versus-building-points split could not be separated from the fetched text. A development-only score also rewards *accumulation*, so it is structurally age-biased |
| Exploit risks | Building-then-selling loops if refunds counted; deliberate completion batching to win a snapshot |
| Source | `11A-RS-066` (OFFICIAL, CURRENT — but the exclusion clause is contested); `11A-RS-069` (OFFICIAL, corroborating the core only) |
| Confidence | **High** that buildings generate points and that rank recalculates on completion, batched under load; **Low** on the recruitment-exclusion universal claim |
| Second source | Yes for the building-points core; **No** for the exclusion clause. Re-verification against in-game help is required before this number enters a specification |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** A development-derived standing is legitimate and is the best non-military scoring basis found anywhere in this set, but it must be **combined** with a rate/window measure, because a pure sum always favours the oldest nation — which is the §15.3 progression-inflation problem. `11A-DR-010`, `11A-DR-019` |

##### 11A-BM-043 — Negative finding: culture-point victory belongs to Travian, not Tribal Wars

**OBSERVED.** The brief expected a Tribal Wars "culture points / non-military victory path". Four targeted queries produced **zero Tribal Wars sources** for culture points or a World Wonder win condition, and instead surfaced the Travian rule: "**The number of culture points required depends on [the wonder level]… The first player to build their World Wonder to level 100 is declared to be the winner of the round**" (`11A-RS-071`). Tribal Wars' own documented endgames are **Dominance** and points/ODA-based metrics (`11A-RS-067`).

**INTERPRETATION.** This is recorded as a **corrected premise, not a gap**. The honest comparator for a peaceful victory path is **Travian's** culture/Wonder race (covered in §5.6) together with **Tribal Wars'** *Casual* and *points* endgames — not a Tribal Wars culture mechanic, which does not exist on the evidence available.

**Confidence** High for the negative. **Relevance Direct.** **Lesson** — a non-military *win* path exists in this genre but only in one documented form (a long, visible, single-object race to a terminal level), and every version of it makes the object the whole game's focus. `11A-DR-010` handles the consequences.

##### 11A-BM-044 — Endgame variants over one engine, and the registration-lock device

**OBSERVED.** Official: "**Win conditions vary: Normal/Casual/Classic/Special use Dominance or endgames like Runes. Speed rounds use varied metrics (points, ODA)**", and the world ladder is "**Normal (Prem/Non-Prem), Casual, Classic, Special (Classic), and Speed**", with "**Duration ranges from hours (Speed) to months (Normal)**" (`11A-RS-067`). A community-stated threshold: "The world has a dominance based winning condition. **Once a tribe reaches 55% dominance, the world will automatically close to registrations**" (`11A-RS-070`, 2013). "ODA" means an **off-game agreement**, i.e. the outcome is negotiated outside the game.

**INTERPRETATION.** Two separable ideas. (1) **One engine, several rule subsets and time compressions** is how cheap variety is shipped — the same lesson as `11A-BM-032`. (2) The **threshold → registration-closure** step is a genuinely good device: a decided competition stops absorbing new entrants *without* ending, protecting both late joiners and the integrity of the standing. (3) **ODA endings depend entirely on moderation the operator is willing to do.**

**Confidence** Medium — the 55% figure is a single 2013 community post and is likely superseded; the world-type list is official and current. **Relevance Direct** (rankings, fairness). **Lesson** — adopt *a decider-state that closes eligibility before it closes the competition*, since a seasonal ladder that keeps accepting entrants after the outcome is decided is a fairness hole. `11A-DR-021`. Reject the premium/non-premium rule split — incompatible with the free-first constraint and with `NAT-045` |

##### 11A-BM-045 — Per-mode persistence, not one global reset rule

| Field | Content |
|---|---|
| Mechanic | What survives a world/season reset, declared per mode |
| How it works | **OBSERVED.** Official: "**Hall of Fame persists in Normal/Casual but resets in Classic/Special/Speed**"; "Registration is direct for most; **Casual requires transfer after village loss or 2 weeks**" (`11A-RS-067`) |
| Strengths | This is the most directly actionable persistence finding in the set: Tribal Wars does **not** apply one reset rule globally, it declares **per mode** which longitudinal record survives. A lifetime honour (Hall of Fame) plus a per-mode reset gives both prestige accumulation and clean slates. The **forced-transfer** rule is also a real longevity device — losing your last village or idling two weeks *moves you to a fresh world* instead of ending your account, which keeps a demoted player in the game rather than churning them |
| Weaknesses | Per-mode inconsistency is confusing — "why does my history count here but not there?"; a lifetime hall of fame is the standard target for multi-account inflation; the idle-transfer is abusable by deliberate loss-to-reroll |
| Exploit risks | Farming the hall of fame across alts; engineered village loss to trigger a fresh-world transfer |
| Source | `11A-RS-067` (OFFICIAL, CURRENT, read as a summary — the medals/honour sub-system was not evidenced) |
| Confidence | **Medium** |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Persistence must be a **declared property of each competitive object**, not a global rule — which is exactly the permanent-versus-temporary distinction the brief §15.4 demands. Ours is already stricter and clearer: `TR-090` fixes P-class records as permanent append-only, `ONB-046` archives at 12 months, `RRL-013` destroys nation-scope state while historical snapshots remain, and `RRL-016` permits account-level survival **only** where the reward is non-transferable and not re-earnable. `11A-DR-013` |

##### 11A-BM-046 — Power-ratio beginner protection computed from the same abstract score

**OBSERVED.** Official FAQ: "**Q: How does Beginner's Protection work (20:1 ratio etc.)? A: During beginner protection: Other players can't attack you at all, or; Attacks are blocked when the attacker is much stronger (e.g., 20:1 point ratio)**" (`11A-RS-068`).

**INTERPRETATION.** Two layers: an **absolute immunity window**, then a **ratio veto** that keeps operating afterwards — and the ratio is expressed in **points**, i.e. the same derived development score from `11A-BM-042`. So one abstract number serves both the leaderboard and the fairness gate, which is efficient and also the exact coupling failure documented for Politics & War at `11A-BM-001`.

**Strengths** — a ratio veto needs no geography, is one division, protects late joiners and peaceful nations at any population, and scales without tuning. **Weaknesses** — ratio gates are metagamed by **deliberate score stunting**, and protection expiry produces a cliff event. **Confidence** Medium (the 20:1 example is quoted, but the threshold schedule was not enumerated; no second source). **Relevance Direct.** **Lesson** — the *relative-band* shape is confirmed as sound by three independent games (Tribal Wars ratio, P&W 15–65% treasure band, Supremacy 1914 percentage-of-pool), but the *shared-number* coupling is the failure mode to avoid; eligibility must read its own measure. `11A-DR-010`, `11A-DR-003`

##### 11A-BM-047 — Seasonal special worlds as events, and farming as a taught activity

**OBSERVED.** An official developer forum announcement: "**Thursday, July 23rd, a Summer Special world will open its gates around 10:00 AM.** As this is a 'special' world…" (`11A-RS-070`, 2026-07-17) — i.e. an event is a **new instance with a modified ruleset**, not a modifier on live worlds. Separately, an official tutorial video is titled "**Who to Farm**", and the rules page covers impersonation and account conduct (`11A-RS-070`); no mechanical anti-farming rule was retrievable (`11A-RS-068` returned none).

**Strengths** — instance-based events are zero-cost content and seasonal naming builds habit; splitting a world by *duration and commitment level* (Casual) is the right answer to the "time burden" question Prompt 11A §12.4 asks. **Weaknesses** — farming constrained by **social norms and moderator tolerance rather than by systems** is unmoderatable at zero budget, which is precisely our situation; and an official tutorial teaching whom to farm is the clearest example of an onboarding surface normalising predation on weaker players. **Confidence** Medium for the event cadence, Low for the farming rules. **Relevance Supporting.** **Lesson** — any objective or event that measures *successful action against another nation* must be bounded by an eligibility floor, because the tutorial-surface evidence shows the target choice is taught, not incidental. `11A-RK-008`

**Unverified for Tribal Wars:** the population-versus-building points split and any per-building point table; whether units contribute points (official text says no, community expectation says yes); the rankings hierarchy (village/player/tribe/nation), **snapshot frequency and historical archives — no official article found**; medals/honour and lifetime stats as a named system; the 55% dominance figure; seasonal quests or cup tournaments (only seasonal *worlds* were evidenced); concrete anti-farming rules; NPC-village mechanics; ODA enforceability.

### 5.4 Additional benchmark — eRepublik

**Selection rationale:** the only game in this set that runs **political, economic, military and media careers on one shared account**, which is the exact structure Prompt 11A §17 requires Nation Supremacy to support. Its value to us is as much cautionary as positive.

| ID | Source | Type | Accessed | Currency |
|---|---|---|---|---|
| `11A-RS-072` | **eRepublik** home page, `https://www.erepublik.com/` — landing copy: "Conquer your country's neighbours", "Build a company", "Fight against real people" | OFFICIAL | 2026-11-05 | CURRENT |
| `11A-RS-073` | **eRepublik Official Wiki** main page, `https://wiki.erepublik.com/` — Military / Politics / Economy / Media category clusters | OFFICIAL | 2026-11-05 | UNVERIFIED (structure plausible, detail thin) |
| `11A-RS-074` | **Military rank** `…/index.php/Military_rank` (`oldid=870634`, index 2025-06-27) and **One:Military_rank** FAQ `…/index.php/One:Military_rank` (2018-08-28) | OFFICIAL | 2026-11-05 | CURRENT (mechanism) / HISTORICAL (2018 corroboration) |
| `11A-RS-075` | **Military unit** `…/index.php/Military_unit` (`oldid=873796`, index 2025-11-21) | OFFICIAL | 2026-11-05 | CURRENT |
| `11A-RS-076` | **Elections** `…/index.php/Elections` (`oldid=838816`, 2023-03-22); **President** `…/index.php/President` (2025-03-27); **Party president** `…/index.php/Party_president` (2025-01-18); **Congress** `…/index.php/Congress`; **Congress elections** `…/index.php/Congress_elections` (2025-01-24); **Presidential elections** `…/index.php/Presidential_elections` (2020-11-20); **Politics** hub `…/index.php/Politics` (2020-06-05) | OFFICIAL | 2026-11-05 | CURRENT for the calendar; UNVERIFIED for seat counts, term lengths and office powers |
| `11A-RS-077` | **Gold** `…/index.php/Gold` (`oldid=816443`); **Newspaper** `…/index.php/Newspaper`; **Decorations** `…/index.php/Decorations` (2024-04-01); **Company** `…/index.php/Company`; **War** `…/index.php/War` (`oldid=795492`) | OFFICIAL | 2026-11-05 | **Mixed currency** — Gold price list retrieved **CURRENT** but undated; Decorations **HISTORICAL** (touched 2024); Company returned only a disambiguation page, so its content is **UNVERIFIED** |
| `11A-RS-078` | **Latest Game Changes**, `https://wiki.erepublik.com/index.php/Latest_Game_Changes` — highest entry **day 5,874**, index date 2023-12-31 | OFFICIAL | 2026-11-05 | **HISTORICAL — appears frozen at ~2023-12-31** |
| `11A-RS-079` | Official update articles: **"Protectors of Nations I"** `https://www.erepublik.com/ru/main/latest-updates/0/329`; **Resource Wars** `…/en/main/latest-updates/0/204`; **Dictatorship** `…/en/main/latest-updates/0/208` | OFFICIAL | 2026-11-05 | CURRENT as far as evidence goes (live update pages exist); rollout dates unconfirmed |
| `11A-RS-080` | In-game player-authored articles: **"Elections"** (Ministry of US Education) `https://www.erepublik.com/en/article/2494942`; **"Is Erepublik fair for new players? Players are forced to buy gold"** `https://www.erepublik.com/en/article/2676982` | OFFICIAL platform / **PLAYER-AUTHORED content** (treated as COMMUNITY) | 2026-11-05 | UNVERIFIED for 2026 |
| `11A-RS-081` | Country-authored pages on the official wiki host `https://wiki.erepublik.com/` (article paths not retained; cited by no benchmark entry): **United States Army**, **United States Army Group East**, **United States Army High Command** (2020-12-15), **Military Decorations, Medals and Insignia of the British Armed Forces** (2020-09-07) | PLAYER-AUTHORED (COMMUNITY-adjacent) | 2026-11-05 | **HISTORICAL** |

**Inaccessible eRepublik surfaces, recorded explicitly:** `…/index.php/ERU` → **404**; `…/index.php/Nation` → **404**; `…/index.php/Battle` (the energy/workout page) → **403**; `…/index.php/Company` → a disambiguation page with no substance; `…/index.php/Country` → no statistics. **No anti-cheat, moderation or ban-policy page could be found at all.**

##### 11A-BM-048 — Four career tracks that are only *semi*-parallel

| Field | Content |
|---|---|
| Mechanic | Military, economic, political and media careers on one citizen |
| How it works | **OBSERVED.** The product itself sells three of four tracks on its landing page ("Conquer your country's neighbours / Build a company / Fight against real people"), while the wiki navigation presents four structurally separate clusters — Military, Politics, Economy, Media (`11A-RS-072`, `11A-RS-073`). **However, the tracks share one hidden ladder**: a newspaper requires "**level 9**" and congressional candidacy requires "**level 15**" plus party membership (`11A-RS-077`, `11A-RS-076`), and founding artefacts cost premium currency — company **10 Gold**, party or military unit **40 Gold**, war **200 Gold**, newspaper **2 Gold** (`11A-RS-077`) |
| Strengths | Four visible careers on one account is the structural proof that a persistent nation game can sustain parallel play styles at all, and media at 2 Gold is deliberately the cheapest entry — a "soft" track can be near-free |
| Weaknesses | **A single shared level gate means the tracks are not independent**: a pure diplomat or pure journalist still pays a grind tax before their track opens, and the political track's own gate (level 15, party-controlled slate) means a whale can buy the party label and then the candidacy. Nothing in the political lane produces a personal stat that compounds — its output is *authority over shared parameters*, which evaporates at the next monthly vote |
| Exploit risks | Alt-leveling to feed level gates; party capture; slate control ("The party president will choose the candidates on the 24th of the month. **There is no minimum of how many candidates the president can propose**") |
| Source | `11A-RS-072`, `11A-RS-073`, `11A-RS-076`, `11A-RS-077` |
| Confidence | **Medium** for the gate pattern (two independent pages agree); **Low** for currency (undated pages) |
| Second source | Yes |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** If Nation Supremacy offers parallel paths, **no path may be gated behind another path's progression currency** — otherwise the design quietly collapses into one ladder with cosmetics. Our own `DMP-051` already refuses the worst version ("Approval is not… an achievement currency or a ranking criterion") and `ECN-092` forbids a prestige currency, so a shared gate would have to be *time/age* based, which `NAT-045` in turn forbids. The conclusion is structural, recorded as `11A-DR-024`: **each progression domain must be independently measurable from its own subsystem's published state, with no cross-track entry fee** |

##### 11A-BM-049 — One ladder with a single published driver: cumulative damage → rank → capacity

**OBSERVED.** Official wiki: military rank "showcases the amount of influence each individual soldier", derived from damage done, quantified at **10% of damage**; the FAQ states flatly "The military rank a citizen has depends on **how much damage that person has done**", and rank-up grants "a **free energy bar**" plus a rank bonus (`11A-RS-074`). Energy — the per-day battle allowance — gates how much damage a citizen can do, and the page describing energy economics returned **403**, so the daily figure is unverifiable. The ladder was extended at the top twice ("On day 2,032 a new Military rank 'Titan'… On day 2,586… 'Legends of the New World'"), and was later **re-based**: an official update describes "**Protectors of Nations**", where players "earn protector levels via **points for damage deployed**", "The Legend rank extra damage **will be migrated to protector levels**", and "Points earned based on **damage, country, and vehicle enrollment in the Armory**" (`11A-RS-079`).

**INTERPRETATION.** Two lessons, one good and one bad. **Bad:** a monotonic, non-decaying grind ladder whose top keeps being extended makes the visible elite permanent and monetises the ladder directly (better equipment → more damage → higher rank → more capacity). **Good, and the best idea in this game for us:** *Protectors of Nations* is a live example of converting **permanent prestige into a multi-input points track** that credits **three different contributions — personal performance, national service, and logistics contribution** — while promising that veterans "will have the same or higher bonuses".

**Confidence** High that damage drives rank (two sources); Low that "10%" is live; Medium-High for the Protectors migration (three pages of the same boilerplate). **Relevance Direct.** **Lesson** — a military recognition track should credit **defensive service, participation and contribution**, not a single damage counter, and a system rewrite should preserve prior investment without entrenching the top. `11A-DR-015`, `11A-DR-025`; the entrenchment risk is carried to `11A-RK-009`.

##### 11A-BM-050 — A predictable monthly triple-election calendar as the world's event rhythm

| Field | Content |
|---|---|
| Mechanic | Fixed-date recurring political events |
| How it works | **OBSERVED.** The political track runs on a **monthly triple cycle**: **Party President on the 15th, Congress on the 25th, Country President on the 5th**, voting closing at "00:00 (eRepublik time)", confirmed independently by an in-game player-published ministry notice listing the same three dates (`11A-RS-076`, `11A-RS-080`). Congress is described as a **40-seat** body, candidates needing **level 15** plus party membership, with a term ending **on the 27th**, holding power over "laws like **taxes and minimum wage**, **but not war declarations**" (`11A-RS-076`) |
| Strengths | This is the highest-value transferable structure in the whole eRepublik pack. **An event the entire world can predict from a calendar** creates a rhythm, gives every news surface something to anticipate, and generates perpetual opposition behaviour without any content author. Coupling it to real mechanical hands — the legislature moving **tax and wage parameters that everyone is graded on** — makes the political track consequential **without needing its own experience points**, and the explicit *exclusion* of war powers is a clean separation-of-powers template |
| Weaknesses | Fixed dates are gameable (policy pain and declarations timed around a vote); a one-month term makes policy unstable and elections perpetual; slate control by the party president can lock the ballot ("no minimum of how many candidates") |
| Exploit risks | Vote-burst coordination; ballot stuffing via alts; engineered vacancy to hand the office to a next-in-line party (a succession rule "the 6th largest party is the next in line" is reported on a 2020 page, UNVERIFIED) |
| Source | `11A-RS-076` (OFFICIAL, CURRENT for the calendar), `11A-RS-080` (player-authored corroboration) |
| Confidence | **High** for the calendar (2025-dated pages plus an independent in-game republication); **Medium** for powers; **Low** for the 40-seat figure (single undated extract, no second source) |
| Second source | Yes for the calendar; No for the seat count |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Our B-06 election cycle is already the same device and is stronger — **`DMP-177`** fixes a **240-turn** per-nation cycle anchored at creation with published dates, which avoids the global-campany-fatigue the monthly triple creates. The transferable rule is that **scheduled political events should move shared parameters that standings measure**, not merely award titles. `11A-DR-026`; the parameter-moving half is already bounded by `DMP-063` (constituency weights "do not vary with population, events or approval") and `DMP-141` |

##### 11A-BM-051 — Decorations as first-N, country-local, permanent honours

**OBSERVED.** Official wiki: "**Decorations** are special achievements granted for **acts of great valour in tournaments and events** of the New World. Citizens find them in their profile." Published criteria include "**One of the first 50 citizens from (country) to win 10 Freedom Fighter medals**" and "**Frontline of Freedom — One of the first 50 Freedom Fighters of…**" (`11A-RS-077`) — a two-tier structure of a repeatable medal and an evergreen **first-come limited** decoration gated on it, displayed on the profile with no stated mechanical bonus.

**INTERPRETATION.** The "**first 50 in your country**" formulation is the sharpest scarcity device in the set: it creates permanent, non-inflating recognition **scoped to a sub-population**, so a small nation still has an obtainable elite band rather than competing against one world list. Its cost is that first-N honours fossilise — latecomers can never earn them — and the awarding authority is not stated anywhere.

**Confidence** Medium on definition, **Low on live availability** (the changelog records "Day 2,610 Medal Changes", proving the system was altered, and the change text could not be read). **Relevance Direct.** **Lesson** — **sub-population-scoped award bands** are the correct answer to the "one world list is unwinnable for a small nation" problem, and are directly implementable with our `D-027` aggregate rules. Adopted in `11A-DR-016`; the fossilisation cost is noted against the P&W finding in `11A-BM-009`.

##### 11A-BM-052 — Media as the low-barrier fourth track, scored by endorsement

**OBSERVED.** Official wiki: "Citizens/orgs create papers for **2 gold, level 9**. **Owners edit/delete within 30 days. Editors manage content; players endorse articles**" (`11A-RS-077`).

**INTERPRETATION.** The cheapest artefact fee in the game (2 versus 10/40/200) makes media deliberately the most accessible track, and **endorsement** is the only reputation signal in this pack that measures **authored work** rather than extraction or violence. The **30-day edit/delete window** is an unusually good integrity rule: you may correct your history, but not silently rewrite it indefinitely.

**Confidence** Medium on the numbers, Low on currency. **Relevance Supporting.** **Lesson** — a nation's published chronicle entries are a candidate non-competitive recognition surface, and a bounded correction window matches our own `TR-091` ("corrections are appended disclosed events", never edits). **Note the boundary:** in-game chat is a **Prompt 13** decision that Prompt 11 must respect — the Stage 2 register states Prompt 13 "must **not** design native real-time Alliance chat, voice, or a Discord or other third-party messaging integration; in-game notifications and audit visibility are the supported surface" (`01_stage_2_prompt_roadmap.md`), so no social-feed objective class may be proposed here.

##### 11A-BM-053 — Real money buying *participation rights* — the pattern to avoid

| Field | Content |
|---|---|
| Mechanic | Premium currency purchasing the right to act, not items |
| How it works | **OBSERVED.** **Verified:** real money buys Gold, and Gold buys *game actions and rights* — **found a company (10)**, **form a party or create a military unit (40)**, **declare a war (200)**, **found a newspaper (2)**; personal income is "Salary via Work" in the national currency, and the same page notes **no real money cash-out** (`11A-RS-077`). A player article records the felt experience: "**Players are forced to either grind their way up or use their credit card**", with a reply agreeing it is "**far too pay-to-win**" (`11A-RS-080`). **Not verified:** the ERU→Gold exchange and any cash-out loop — the `ERU` page returned **404** |
| Strengths | As a cautionary artefact it is exactly the evidence needed: a clean, dated case of a persistent nation sim pricing **sovereignty acts** — founding a firm, forming a party, starting a war — in premium currency |
| Weaknesses | It converts the game's political and economic participation into a purchase decision, and the community's own words describe the resulting trap (grind or pay) as the reason new players leave |
| Exploit risks | Shell companies to launder premium currency between alts; cartel funding of wars for loot |
| Source | `11A-RS-077` (OFFICIAL, CURRENT price list, undated page), `11A-RS-080` (**COMMUNITY/player-authored**), `11A-RS-079` |
| Confidence | **High** that money buys Gold which buys game actions; **Low** on the cash-out direction, which could not be evidenced |
| Second source | Yes for the Gold side (Military_unit independently reports 40 Gold for unit creation) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Recorded as the explicit anti-pattern: **no rule, objective, event or ranking in Nation Supremacy may price a right** — office, war declaration, sovereignty, corporate charter or participation. Our fixed constraints already decide it (`NAT-045`, `ECN-092`, the ₹0 target, and `REQ-073`'s no-conversion rule), and the free-first architecture means no paid reward track is even available to design against. `11A-DR-012` |

**Unverified for eRepublik, recorded as gaps (the largest set in this study):** whether the game still runs at all in 2026 (the changelog freeze at day 5,874 leaves 2024–2026 activity unconfirmed, though 2025-dated wiki pages and live update pages suggest it does); **any national strength formula or national leaderboard** — `Nation` 404, `Country` returned no statistics, so the common claim of an eRepublik GDP/power board is **unverified**; whether individual activity feeds a published national statistic; daily energy figures and free-versus-paid refill; the current military hierarchy (the wiki now describes **regiments** while player-authored pages describe battalion/division/army group/High Command, and the game "supplies a flat unit primitive" that players layer themselves); who may award medals besides the game; whether Decorations are permanent or seasonal; Congress seat allocation; presidential powers and term lengths; which actor declares war; company, marketplace and industry internals; any economic badge or leaderboard (absence of evidence only); constitutional, referendum or impeachment mechanics; and botting, farming, cartel behaviour and moderation **as documented** problems — the exploitable *rules* are evidenced, no abuse report or policy page was found.

### 5.5 NationStates

**Selection rationale:** NationStates is the only benchmark whose central loop is **policy expression rather than accumulation**. It is therefore the best available evidence for the two things Prompt 11A §7.4 asks about — whether political participation can be an *independent* progression path, and how public recognition can be meaningful without granting overwhelming mechanical advantage.

**Access limitation, reported rather than worked around.** Every official NationStates surface returned **HTTP 403** to unauthenticated requests from this environment: `nationstates.net/`, `…/page=dispatch`, `…/page=qa`, `…/page=qa/q=…` (a Question & Answer entry), `…/page=trade`, and `forum.nationstates.net/`. The domains `wiki.nationstates.net` and `www.nationstateswiki.org` did not resolve at all. On this first pass, entries `11A-BM-054`…`11A-BM-059` therefore rest solely on the reachable community MediaWiki API at `nationstates.fandom.com`, and no community statement is presented as an officially confirmed developer rule.

**Second-pass update.** A later pass recovered the **same official pages from dated Internet Archive captures**, including a **2026-10-24 capture of the official FAQ**, so official NationStates evidence is available — just not from the live site. **§5.5b supersedes the currency assessments of this subsection** and adds entries `11A-BM-067`…`11A-BM-073`. Nothing here is deleted: the community-wiki entries remain valid as second sources and their identifiers are referenced from the main report. Where the two passes disagree, **§5.5b governs**.

| ID | Source | Type | Accessed | Last edit | Currency |
|---|---|---|---|---|---|
| `11A-RS-082` | **Regional Influence**, `https://nationstates.fandom.com/wiki/Regional_Influence` | COMMUNITY | 2026-11-05 | 2024-07-20 (47 rev) | CURRENT-ish; cites an official 2006 news post for the origin |
| `11A-RS-083` | **WA Delegate**, `…/wiki/WA_Delegate` | COMMUNITY | 2026-11-05 | 2024-08-04 | CURRENT-ish |
| `11A-RS-084` | **World Assembly**, `…/wiki/World_Assembly` | COMMUNITY | 2026-11-05 | 2024-11-24 | CURRENT-ish; names a Secretary-General elected 2018, so leadership detail is stale |
| `11A-RS-085` | **World Census**, `…/wiki/World_Census` | COMMUNITY | 2026-11-05 | 2020-08-10 (5 rev) | **HISTORICAL** for the category list; the 2016-02-29 overhaul is cited internally |
| `11A-RS-086` | **Issue**, `…/wiki/Issue` | COMMUNITY | 2026-11-05 | 2024-07-20 | CURRENT-ish; cites official news posts and forum update notices |
| `11A-RS-087` | **Region**, `…/wiki/Region` | COMMUNITY | 2026-11-05 | 2024-07-19 | CURRENT-ish |
| `11A-RS-088` | **General Assembly** `…/wiki/General_Assembly` (2024-08-04) and **Security Council** `…/wiki/Security_Council` (2024-08-04) | COMMUNITY | 2026-11-05 | 2024-08-04 | **HISTORICAL** (2024 revisions) and **Thin** — 759 and 781 characters; stubs |
| `11A-RS-089` | **List of issues**, `…/wiki/List_of_issues` | COMMUNITY | 2026-11-05 | 2024-07-20 | CURRENT-ish (102 KB index) |
| `11A-RS-090` | Blocked official surfaces (recorded as **inaccessible**, not as findings): `https://www.nationstates.net/`, `…/page=dispatch`, `…/page=qa`, `…/page=trade`, `https://forum.nationstates.net/` | OFFICIAL — **HTTP 403** | 2026-11-05 | — | **Unavailable** |

##### 11A-BM-054 — World Census: plural descriptive standings with no mechanical weight

| Field | Content |
|---|---|
| Game / System | NationStates — national measurement and identity |
| Mechanic | The **World Census** |
| How it works | **OBSERVED (community-sourced).** "A world census report of a **random category** is generated **every day** to compare all nations with the **world median**." Categories each have a name, a synopsis, a **rank descriptor** and a satirical **unit name** — the recorded set runs to dozens and includes **Civil Rights** ("Most Extensive Civil Rights", Martin Luther King, Jr. Units), **Economy** ("Most Efficient Economies"), **Political Freedom**, **Population**, **Wealth Gaps**, **Death Rate**, **Compassion**, **Eco-Friendliness**, **Social Conservatism**, **Nudity**, and named industry categories. A nation's standing is described by the rank descriptor rather than presented as a competitive position. Nations "can easily access all reports in the Analysis section" since 2011 |
| Trigger | Daily generation of one random category report |
| Eligibility | All nations |
| Timing | Daily; comparison is against a **median**, recomputed |
| Scoring | Relative position within a named dimension |
| Reward | **None documented** — descriptive only |
| Restrictions | Not stated |
| Strengths | This is the strongest available proof that **a game can sustain many public measurements without any of them becoming a ladder**. Three devices are worth taking: (a) standings expressed as a **descriptor against a median**, which tells a player what kind of nation they run rather than who is winning; (b) **one dimension spotlighted per day**, which gives the world a free recurring content beat and stops every board competing for attention at once; (c) categories that are **expressive rather than performative** (Compassion, Eco-Friendliness, Wealth Gaps), so a player's identity, not their power, is being measured |
| Weaknesses | Satirical naming means the layer is deliberately not load-bearing — it cannot carry progression weight; a daily random category is discoverable but not schedulable; and "compare with the median" hides the distribution shape |
| Exploit risks | Very low by design — nothing is awarded, so nothing can be farmed. The residual risk is players treating a descriptor as a target and distorting policy to chase it |
| Source | `11A-RS-085` (COMMUNITY, **HISTORICAL** 2020-08-10) |
| Confidence | **Medium** that the mechanism and its descriptive character are right; **Low** on the current category list (single stale community page, official page inaccessible) |
| Second source | No — official surfaces blocked (`11A-RS-090`) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **descriptive-against-median, non-rewarded** layer as a distinct object from competitive standings (`11A-DR-027`), and adopt the **rotating spotlight** as a zero-authoring recurring event class (`11A-DR-001`). It composes with our rules: `DMP-051` forbids approval as a ranking criterion, but a *descriptive* national profile assembled from published statistics is not a ranking. It also satisfies `AP-005` structurally, because no dimension can dominate when none carries a reward |

##### 11A-BM-055 — Influence as a spendable, decaying anti-coup resource

| Field | Content |
|---|---|
| Mechanic | Regional **Influence** |
| How it works | **OBSERVED (community-sourced).** "Regional influence is a system added to NationStates in **2006**. It was created **as a way to prevent new members of a region from seizing the delegate position and *immediately* ejecting & banning everyone else.** Nations earn influence in a region **the longer they remain there, and the more WA endorsements they have accumulated**. The ability of Delegates to eject and ban nations from their region, and to password-protect it, **is limited by their Influence. Delegates consume some of their Influence to exercise their power, so the more often the Delegate uses their influence, the more difficult it is for them to wield those powers in the future.**" A named rank ladder of **29 descriptors** runs from *Zero, Unproven, Hatchling, Newcomer, Minnow, Sprat, Shoeshiner, Page, Squire, Apprentice, Vassal, Truckler, Handshaker, Duckspeaker, Envoy, Diplomat, Ambassador, Auxiliary, Negotiator, Instigator, Dealmaker, Enforcer, Eminence Grise, Powerbroker, Power, Superpower, Dominator, Hegemony* to *Hermit* |
| Trigger | Accumulates with regional tenure and endorsements; spent on powers |
| Eligibility | Nations resident in a region |
| Timing | Continuous accrual; consumption on use |
| Scoring | An influence value mapped to a named rank |
| Reward | Capability, not currency — it gates how often a power can be used |
| Restrictions | Powers are unavailable below thresholds; use depletes capacity |
| Strengths | **The single most interesting political-progression idea in this research set.** Influence is a *spendable* form of standing whose entire stated purpose is **rate-limiting the abuse of an elected position**. Rather than making a leader all-powerful, accumulated legitimacy becomes a budget that drains as authority is exercised — which directly solves the "how should long-term political activity be recognised without granting overwhelming mechanical advantage" question in Prompt 11A §7.4 |
| Weaknesses | It accrues from **tenure and endorsement volume**, so it entrenches incumbents and rewards popularity contests; the same page records that the delegate's endorsement position is the target of "**region crashing**" |
| Exploit risks | Endorsement rings; mass migration to convert a fresh cohort into instant authority before influence checks exist — the exact attack the system was created to answer |
| Source | `11A-RS-082` (COMMUNITY, 2024-07-20), citing an official 2006 news post |
| Confidence | **Medium-High** for the design intent and the spend mechanic (specific, internally coherent, sourced to an official news item); **Low** that the rank list is current |
| Second source | No — official surfaces blocked |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Do **not** port influence: it is a *power* currency, and Nation Supremacy has no equivalent office, no region, and a fixed rule that political standing may not become a purchasable or accumulative advantage (`DMP-051`, `ECN-092`, `DIP-084`). **Do** port the inverse insight — *recognise* long-term political participation through durable records rather than through authority that compounds. Recorded as `11A-DR-028`, and the "rate-limit an office rather than grant it" pattern is flagged for **Prompt 12** as a governance idea, not adopted here |

##### 11A-BM-056 — Delegate election: a scheduled snapshot with a published tenure tie-break

| Field | Content |
|---|---|
| Mechanic | Regional **WA Delegate** selection |
| How it works | **OBSERVED (community-sourced).** "A region's delegate is the WA member nation with the **most endorsements** in that region. **If two nations have the same number of endorsements, then the nation that has been in the region longer will become the delegate.** **Endorsement counts are decided during the daily game update.** A delegate has extra voting power in the World Assembly (**the number of votes a delegate has is the total number of endorsements plus one more vote, which represents the nation itself**)… In non-game terms, the delegate usually becomes the head of the government of his region, and many regions have **election cycles** to vote on its next delegate." Consequences are recorded honestly: control of the delegacy gives regional control (banlist, password), "if there is no founder… then the delegate has **uncontested control**, until someone gets more endorsements", and "delegate endorsement battles are the heart and soul of **region crashing**" |
| Trigger | Daily game update |
| Eligibility | World Assembly members resident in the region |
| Timing | **Evaluated at a single daily snapshot**, not continuously |
| Scoring | Endorsement count; votes = endorsements + 1 |
| Reward | Office, additional voting weight, regional control |
| Restrictions | Founder can disable delegate powers; tie broken by tenure |
| Strengths | Three clean devices: **snapshot evaluation** (the standing settles once per day, so mid-day fluctuation cannot decide an outcome), a **published, derivable tie-break** (longer residence wins — transparent, deterministic, and the opposite of P&W's documented "tie goes to the developer's nation", `11A-BM-008`), and **delegated authority that a third party can revoke** (the founder's switch) |
| Weaknesses | The reward is **mechanical power proportional to popularity**, which is exactly what our B-06 and B-08 rules refuse to allow; a pure endorsement count is trivially inflatable by a coordinated group, and the source itself documents the resulting attack practice |
| Exploit risks | Endorsement farming and crashing; an absent delegate leaving a power vacuum; vote weight scaling without bound |
| Source | `11A-RS-083` (COMMUNITY, 2024-08-04); `11A-RS-087` |
| Confidence | **Medium**; no official confirmation available |
| Second source | Partial (Region page describes the same structure) |
| Relevance | **Supporting** (rankings methodology; political participation) |
| Lesson | **LESSON / DIRECTION.** Adopt only the **methodology**: snapshot at a declared point (`11A-INT-03`) and prefer a **published tenure-or-earliness tie-break** over a hidden one — which our `TR-044` B2 seeded-selection and shared-rank options already satisfy. Reject proportional mechanical power, because `DMP-195` ("campaign spending cannot buy an election") and `DIP-088` (a public count with no mechanical effect) set the opposite precedent. `11A-DR-028` |

##### 11A-BM-057 — Membership rules with a stated consequence, and one-member-per-player

**Source rows:** `11A-RS-083`, `11A-RS-084`, `11A-RS-088`, `11A-RS-102`.


**OBSERVED (community-sourced).** "Membership to the World Assembly is **entirely voluntary**, and done by clicking on the 'Apply to join' button… **Email verification is required for membership.** **Each player can only have one World Assembly member at a time, otherwise they will be ejected for one year.** Players may resign from the World Assembly whenever they wish to." The Security Council, added in 2009, "has powers to **condemn or commend** regions and nations, and liberate regions"; the General Assembly handles legislation.

**INTERPRETATION.** Two transferable properties. The rule is **specific, bounded and time-limited** ("ejected for one year") rather than open-ended — the pattern Prompt 12A §16.10 wants Prompt 12 to hold. And the World Assembly's only *institutional* recognition instrument is **condemn/commend**, which matches our own precedent that published factual counts, not computed reputations, are the lawful diplomatic record (`DIP-088`).

**Confidence** Medium (community, official surfaces blocked). **Relevance Supporting.** **Lesson** — collective bodies may issue **records**, not scores; and voluntary participation is a design requirement we already hold harder (`AP-004`, "membership never mandatory"). `11A-DR-023`

##### 11A-BM-058 — Issues: a state-triggered content pipeline the player can throttle

| Field | Content |
|---|---|
| Mechanic | National **issues** and their delivery rules |
| How it works | **OBSERVED (community-sourced).** "Issues are political decisions that players make, which **shape their nations as a result**. The choices a player makes on issues directly affect the nation's civil rights, economy, political freedom levels, national tax rate, etc. Issues also **determine and change the type of government a nation has**, with the game categorizing the type anywhere from 'Democratic Socialists' to 'Psychotic Dictatorship'." Since 2016-02-29 "issue decisions **take effect immediately**, and players can view the effects in detail" (previously the next day). Five generation classes: **General** ("randomly generated with no preconditions"), **Population-Based** ("can only be unlocked by a nation's population… If a player **dismisses** these issues or regrets an option chosen, they will still be able to receive them later"), **Issue-Option** ("unlocked when a nation chooses a specific option in an issue" — decision chains), **Statistic-Based** ("unlocked when a nation reaches a predetermined statistic"), and **Special** ("rare and occur infrequently", e.g. a WA-members-only issue), plus **Easter-egg issues that reward nations with a unique badge displayed on the nation's main page**. Cadence is player-settable: "over time, the frequency decreases until it settles at a new issue being received **every six hours**", with options **No Throttle (default, 6 h) / 12 hours / 24 hours / 48 hours**. Submitting an issue *idea* requires a minimum population (500 million, reduced to 50 million in 2016, raised to **250 million** since 2018-11-27). Inactivity for **28 days** leads to nation deletion, and **Vacation Mode** "stops the player's nation from receiving any new issues and extends the inactivity deletion period from 28 days to **60 days**" |
| Trigger | Cadence clock plus state conditions (population, statistic, prior decision, membership) |
| Eligibility | Every nation; some classes gated on state |
| Timing | Default one per six hours, player-throttled up to 48 hours |
| Scoring | None — the choice itself is the mechanic |
| Reward | Identity change; occasionally a unique badge |
| Restrictions | Dismissed gated issues may return later; deletion at 28/60 days |
| Strengths | This is the **event/objective generation model most compatible with a no-author architecture**, and it has four properties worth taking. (1) **Five explicit trigger classes** — unconditional, state-threshold, prior-decision-chained, statistic-gated and membership-gated — which is a complete taxonomy for systemic event generation and needs no editorial calendar. (2) **Player-settable cadence.** The single best answer in the entire benchmark set to the notification-fatigue question Prompt 11A §12.4 raises: the *player* chooses whether content arrives every six hours or every two days. (3) **Dismissal is not loss** — a declined or regretted opportunity can return, which is precisely the humane alternative to the P&W "collect before reset or it is lost" rule. (4) **Immediate, visible effect** — the 2016 change from next-day to instant feedback exists because delayed feedback is unreadable, which matches our own `TR-088` digest-and-explain duty |
| Weaknesses | Population is used as a **participation gate** for submitting ideas, which makes a small nation's voice structurally quieter; and the "unique badge from an Easter-egg issue" is an untracked, undocumented reward, so its scarcity is invisible |
| Exploit risks | Low: issues grant no resources, so there is nothing to farm. The residual risk is a player treating the badge hunt as the object |
| Source | `11A-RS-086` (COMMUNITY, 2024-07-20); `11A-RS-089` |
| Confidence | **Medium** for the category taxonomy and throttle options (specific and internally coherent); **Low** that the current figures match live values, since no official page was reachable |
| Second source | No |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **five-trigger-class taxonomy** as the spine of the event and objective catalogue (`11A-DR-001`), adopt **player-adjustable cadence** as the mitigation for event frequency and notification fatigue (`11A-DR-005`), and adopt **"dismissal is not forfeiture"** as the interaction rule for optional objectives (`11A-DR-009`). All three are compatible with our constraints: `TR-085` is untouched because cadence throttling reduces content rather than rewarding presence, and `TR-089`'s bounded digest row still holds. **Reject** size-gated participation, which `NAT-045` forbids as a differential |

##### 11A-BM-059 — Player-created grouping with revocable, founder-supervised authority

**OBSERVED (community-sourced).** "A region is an internal grouping of nations… There are two types of regions: regions that were created by the game admin… and regions created by NationStates **players themselves**." In a player-created region "there are two positions of leadership: a **Founder** and a **WA Delegate**", with powers including "access to the World Factbook Entry", "ability to eject nations", "the ability to set a regional password", and "**the Founder also has the ability to turn on or off the UN delegate's powers**". Regions can lose their founder: "the Founder has either **expired due to inactivity**, or the region was created prior to regional Founders being introduced".

**INTERPRETATION.** The transferable shape is *nested authority with a revocation switch*: an organisation's operational leader can be disabled by the body's founder, and the founder role itself can lapse through absence rather than requiring a resignation. That is a governance pattern, and governance is **B-09's** domain under the owner's open constitutional questions (`UD-047` collective positions and delegation, `UD-044` expulsion and appeal).

**Confidence** Medium; community only. **Relevance Supporting.** **Lesson** — **recorded as an observation for Prompt 11B to avoid, not to adopt**: Nation Supremacy's Alliance architecture is fixed and owner-reserved in exactly these areas, and "Nation Supremacy must preserve its own political and Alliance architecture" (§7.4). Nothing here may become an 11A Alliance rule. `11A-OPEN-015`

### 5.6 Travian: Legends (InnoGames)

**Selection rationale:** Travian contributes what no other benchmark does — a **fully documented recurring daily-objective system with published reward tiers**, a **weekly scheduled medal cycle**, and **the genre's only official non-military victory path** (the World Wonder). It also supplies the correct target for §9.4's warning, because its tournament prizes are real-money vouchers.

| ID | Source | Type | Accessed | Currency |
|---|---|---|---|---|
| `11A-RS-091` | **Daily Quests**, official Travian: Legends Help Center, `https://support.travian.com/en/articles/16-daily-quests` | **OFFICIAL** | 2026-11-05 | CURRENT |
| `11A-RS-092` | **How Medals work**, `…/articles/168-how-medals-work` | **OFFICIAL** | 2026-11-05 | CURRENT |
| `11A-RS-093` | **Season Pass, Missions & Rewards** — "Annual Special 2026 – Rise of Governors", `…/articles/229-season-pass-missions-and-rewards` | **OFFICIAL** | 2026-11-05 | CURRENT (2026 season content) |
| `11A-RS-094` | **Task System**, `…/articles/17-task-system`; **Culture Points (CP)**, `…/articles/51-culture-points-cp`; **Passive Culture Points**, `…/articles/174-passive-culture-points` | **OFFICIAL** | 2026-11-05 | CURRENT |
| `11A-RS-095` | **Wonder of the World**, `…/articles/103-wonder-of-the-world`; **Special Servers – Ancient Powers and Victory Points**, `…/articles/106-…`; **End game** wiki, `https://travian.fandom.com/wiki/End_game` (last edit 2023-12-02) | **OFFICIAL** + COMMUNITY | 2026-11-05 | CURRENT / HISTORICAL for the wiki page |
| `11A-RS-096` | **Beginner's Protection**, `…/articles/12-beginner-s-protection` | **OFFICIAL** | 2026-11-05 | CURRENT |
| `11A-RS-097` | **Travian Tournament Overview** `…/articles/107-…`; **Game Worlds Setup** `…/articles/108-…`; **Prizes** `…/articles/109-…`; **Finals Entry Key** `…/articles/236-…` | **OFFICIAL** | 2026-11-05 | CURRENT |
| `11A-RS-098` | **How to avoid getting farmed** `…/articles/140-…`; **Farm Lists** `…/articles/69-farm-lists`; **Oasis farming after beginner protection** `…/articles/185-…`; **Early game oasis farming** `…/articles/190-…` | **OFFICIAL** | 2026-11-05 | CURRENT |
| `11A-RS-099` | **Quests** (T3.6 tutorial chain), `https://travian.fandom.com/wiki/Quests` (last edit **2019-02-21**, 428 revisions); **Tasks (t4)** (2016-01-09); **Travians Tribes** (2026-07-03, which links the official `support.travian.com/en/articles/…` paths) | COMMUNITY | 2026-11-05 | **HISTORICAL** (Quests, Tasks t4) / CURRENT-ish (Tribes) |
| `11A-RS-100` | **Travian Medals** wiki stub `https://travian.fandom.com/wiki/Medals` (69 characters; a redirect — no content) | COMMUNITY | 2026-11-05 | **UNVERIFIED** — the page carries no text, so its currency cannot be judged; **uninformative** |
| `11A-RS-101` | Blocked or absent official surfaces (recorded, not guessed): `https://support.travian.com/hc/en-us` → **404**; `https://support.travian.com/hc/en-gb` → **404**; `https://www.travian.com/help` resolves to a **JavaScript-only shell** (`…/international/help`) containing no article text. The working official path pattern is `https://support.travian.com/en/articles/<id>-<slug>`, discovered through the reachable **`https://support.travian.com/sitemap.xml`** (231 articles enumerated) | — | 2026-11-05 | — |

**Method note.** Because the help-centre page bodies are client-rendered, the official article text was retrieved through `support.travian.com/en/articles/…` directly, with `<article>` content extracted; the sitemap was used only to discover article slugs. No authenticated or state-changing action was performed.

##### 11A-BM-060 — Daily Quests: a fully specified recurring objective system

| Field | Content |
|---|---|
| Game / System | Travian: Legends — recurring objectives |
| Mechanic | **Daily Quests** |
| How it works | **OBSERVED (official).** "Each day you'll receive **up to 10 tasks** — some easy, some more challenging. Completing them not only gives you **points** but also unlocks valuable prizes… Each quest you finish earns points… **You can earn rewards at 25, 50, 75, and 100 points — up to 4 rewards per day.** **Quests and rewards reset once per day at the same time your gameworld started.** Example: if your server started at 09:00, quests reset daily at 09:00. **Important: You must collect your rewards before reset — otherwise, they are lost.** **Rewards cycle in a fixed order (not random), and every player on the same gameworld sees the same reward set.**" The published tier table gives concrete rewards per threshold — e.g. 25 pts: `+50 Hero Experience`, `+5 Tablets`, `+1,000 resources of one random type`, `+200 resources of each type`; 50 pts: `+1 day +25% Lumber/Clay/Iron/Crop production`, `+5 Small Bandages`, `+400 Hero Experience`, `+4,000 resources of each type`; 75 pts: `+50 Culture Points`, `+5 Cages`, `+1 additional Adventure`; 100 pts: `+20,000 resources of one random type`, `+1 day Travian Plus`, `+400 Culture Points`, `+5 Ointments`, then "repeat from the top". Additional official notes: "Rewards activate **immediately** when you claim them"; "**Server speed does not affect rewards**"; "**Some quests require bulk actions** — for example, train 20 units at once. Training them individually will not count"; "Even if you miss a day, rewards keep cycling in the same order"; and the closing advice is explicit: "**Check your Daily Quests every day, hit the 100-point mark if you can, and collect your rewards before reset**" |
| Trigger | Daily generation at the gameworld's start-time boundary |
| Eligibility | Every player on the gameworld; identical reward set for all |
| Timing | Daily; resets at a per-server wall-clock hour derived from world start |
| Scoring | Points per quest; four cumulative thresholds at 25/50/75/100 |
| Reward | Resources, hero experience, culture points, temporary **+25% production for one day**, consumable items, an extra adventure, and **+1 day of the paid Travian Plus account** |
| Restrictions | **Four rewards maximum per day; uncollected rewards are destroyed**; quest completion must be in one bulk action where specified |
| Strengths | As an engineering object it is excellent: **ten tasks, four thresholds, a deterministic reward rotation, one reset boundary, and a per-server derived reset time.** Because the rotation is fixed and identical for everyone on the world, a player can *plan* rather than fish — deterministic rotation is strictly fairer than random drops, and it means the operator never has to author reward content again. "Server speed does not affect rewards" is also an explicit anti-scaling guarantee worth copying. The immediate-activation rule removes a whole class of "did it apply?" support questions |
| Weaknesses | **This is the exact system Prompt 11A §13.4 warns against, and it is documented in its own text.** Four defects: (1) **uncollected rewards are destroyed at reset**, so absence is punished by loss — the direct opposite of our `D-028` "suffers no resource, progression or ownership loss" and of `TR-085`; (2) the official advice is an instruction to **log in daily**, and the paid-account-day reward makes attendance convertible into premium value; (3) the **"train 20 units at once" bulk-action rule** rewards a specific interaction shape rather than an outcome, so it is a chore that can be failed for the wrong reason and it pressures automation; (4) **production-multiplier rewards** (+25% for a day) attach yield to attendance, which is the compounding vector `ECN-113` and `URB-101` exist to block. Its own framing — "one of the easiest ways to boost your progress" — concedes that the mechanic pays for presence rather than for judgement |
| Exploit risks | Multi-account daily collection cascades; automated quest completion; deliberately batching at the reset edge; alt nations harvesting production boosts |
| Source | `11A-RS-091` (**OFFICIAL**, CURRENT, verbatim) |
| Confidence | **High** — the entire specification is on one official page |
| Second source | Partial (`11A-RS-094` Task System and `11A-RS-099` community quest pages describe adjacent systems) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt the **container and reject the compulsion.** The reusable structure is: a bounded number of tasks, a small number of cumulative thresholds, a **deterministic published reward rotation**, one reset boundary derived from a world clock, and a guarantee that world speed does not change reward value (`11A-DR-029`). The compulsion layer is inadmissible: **`TR-085`** forbids presence rewards, **`ONB-041`** and **`D-028`** forbid absence penalties, so an 11B objective may *defer* an unclaimed reward but may never *destroy* it, and **`ECN-113`**/`URB-101` bar the yield-multiplier reward outright |

##### 11A-BM-061 — Weekly medals: a scheduled snapshot producing permanent honours, including defensive and PvE categories

| Field | Content |
|---|---|
| Mechanic | **Weekly medals** and their streak tiers |
| How it works | **OBSERVED (official).** "Weekly medals are granted **every Monday at 00:00 (server time)** for the **previous week's performance**." Player medals are earned by placing in the **Top-10** for **Attackers, Defenders, Raiders,** and **PvE** ("kills vs. Natars and unoccupied oases"). Streak and repeat tiers: "**Top-3 best** in the same category **3/5/10 times** (not consecutive)"; "**Top-10 best** in the same category **3/5/10 times** (consecutive)"; "**Top-10 both Attacker & Defender** in the same week **1/2/3 times** (consecutive)". "Alliances receive Top-10 medals for **Attack, Defense, Raiding, and Climbers (population growth replaces PvE for alliances)**", and "alliance medals show **laurel branches** around the ribbon". Tournament medals cover "Attack, Defense, Population, World Wonder, and **Survivor** (played to the end)". "Local medals" reward "participation in Local gameworlds (e.g. the first was **Titani—Italy—designed with community input)". Special medals cover "special test worlds (e.g. Loyal Legend)", winners of named events, and "**Veteran medals for 3/5/10 years of play**"; the page adds that "the rarest is the **Hammelburg meeting medal** (one-time award for attendees in 2009)" and that "the **first-ever medal** was the **dove of peace** (**shown during beginner's protection and then fades**)" |
| Trigger | Fixed weekly instant (Monday 00:00 server time) |
| Eligibility | Top-10 by category per gameworld |
| Timing | Weekly evaluation of the prior window; the medal itself is permanent |
| Scoring | Category-specific top-N over one week |
| Reward | A permanent displayed ribbon; laurel variants for alliances; no documented yield |
| Restrictions | Distinct consecutive and non-consecutive streak families |
| Strengths | The **best-performing competitive-recognition design in this benchmark set**, for four reasons. (1) **A weekly window**, not an all-time total, so a newcomer-era nation can win a medal the founding cohort cannot be locked into. (2) **Four player categories of which two are not offensive** — Defenders and PvE — and an explicit official note (see `11A-BM-064`) that PvE kills do **not** count toward the attacker ranking, i.e. the categories are actively defended against cross-farming. (3) **Streak tiers that come in both consecutive and non-consecutive forms**, which recognise both sustained dominance and durable relevance without forcing an unbroken run. (4) **Alliance medals replace, rather than duplicate, a category** — "population growth replaces PvE" — which is how a collective board can be meaningful without being the same board at a different size. Adding a **Survivor** award for "played to the end" also recognises endurance without recognising victimhood |
| Weaknesses | Top-10 on a per-gameworld basis is a very narrow band, and a medal whose rarity depends on world population is not comparable across worlds; streak systems reward incumbency, so the same few names accumulate; and the "one-time award for attendees in 2009" is pure fossilisation — a permanent honour obtainable only by people who were physically present at an offline event |
| Exploit risks | Coordinated week-boundary pushing; medal trading between alts to accumulate streaks; category-switching to win a thinner board |
| Source | `11A-RS-092` (**OFFICIAL**, CURRENT, verbatim) |
| Confidence | **High** |
| Second source | Partial (no second official page; the community medal stub `11A-RS-100` is empty) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Adopt five devices as the core of the recognition architecture (`11A-DR-013`, `11A-DR-016`): **fixed-instant snapshot**; **windowed rather than cumulative** evaluation; **separate categories that include defensive and non-conflict activity**; **cross-category exclusions enforced by design** so one activity cannot feed two boards; and **tiered streaks with both consecutive and non-consecutive forms**. Reject physical-presence and offline-event honours, which cannot exist in our model, and treat small-world top-N bands with care given `11A-OPEN-004` |

##### 11A-BM-062 — Season Pass: account-level progression that spans instances — and counts alt activity

**Source rows:** `11A-RS-093`, `11A-RS-091`.


**OBSERVED (official, 2026 content).** "The Season Pass is a progression system **shared across your lobby account**… By completing **Missions**, you earn **Season Pass Points**. These Points unlock Season Pass Rewards, including **Governor Stars and Shards**. Your Season Pass progress is **tied to your lobby account, not to a single avatar or game world**. This means you can make progress on different game worlds that participate in the same Season Pass." Daily allowance: "**You can complete five Missions per day: 2 Daily Missions, 3 Random Missions**"; "**Some Missions have one objective, while others have several tiers and grant part of their Season Pass Points as you complete those tiers**." The two Daily Missions are "**Daily Login** – Log in to any participating game world to receive Season Pass Points" and "**Task Rewards** – Collect task rewards in the game". Random-mission examples include collecting daily quest rewards, settling or conquering a village, increasing population, killing troops, defeating animals, finding an oasis with an elephant, training troops or scouts, improving a unit in the Smithy, changing your hero's appearance, activating or extending a production bonus, and transferring resources from the Hero inventory to a village. "Each Random Mission can be **rerolled once per day**, but only before you complete its first objective. **Rerolling requires either watching a video, or using a Video Skip Shard.**" And: "Actions performed on your avatar by **duals and sitters** **also count** toward the Season Pass progress of the avatar owner's lobby account."

**INTERPRETATION.** Three findings, one excellent and two severe. **Excellent:** *tiered missions that release partial credit as you pass each tier* — a strictly better motivation shape than a single cliff, because partial progress is never wasted; and a cross-instance account-level ledger, which is exactly the object our own `D-040`/`REQ-089` already use for tutorial progress. **Severe (1):** a mission called literally "**Daily Login**" that pays progression points, and a **video-for-reroll** loop — attendance monetisation and attention monetisation, both squarely forbidden for us by `TR-085` and AP-001. **Severe (2):** the official statement that **"duals and sitters"** — a player's other accounts and people playing in their place — **count toward the owner's progression**. Travian has institutionalised multi-account contribution as a feature. P&W's rules treat the same behaviours as 50–100-point violations with a one-year expiry (`11A-BM-021`), and Nation Supremacy's fixed rule is one account, one active nation (`D-032`, `REQ-061`).

**Confidence** High (official, verbatim, 2026 content). **Relevance Direct.** **Lesson** — adopt **tiered partial-credit missions** and an **account-scoped progression ledger that survives instance changes** (`11A-DR-024`, and `11A-DR-013` for the permanent layer); reject login-reward missions absolutely; and treat "activity by an associated account credits the owner" as the canonical **anti**-pattern, recorded as `11A-RK-009`. Note the mirror image: our reroll rules make account-level credit *safe* precisely because they forbid re-earning (`REQ-073`), which is the hole Travian's dual-crediting opens.

##### 11A-BM-063 — The World Wonder: an official non-military victory path that cannot be soloed

| Field | Content |
|---|---|
| Mechanic | Wonder of the World as the terminal objective |
| How it works | **OBSERVED (official).** "The Wonder of the World (WW) is the ultimate building in Travian: Legends — and **the key to winning the game world**. **The first player or alliance to build their Wonder of the World to level 100 wins the server.** Each level of the Wonder **requires hundreds of thousands — even millions — of resources**. Because of this enormous demand for materials and defense, **it's impossible for a single player to complete one alone**. Usually, entire alliances and their confederates work together to collect resources, defend the Wonder of the World, and manage logistics. Building and maintaining a Wonder of the World is the most challenging and coordinated task in the game." Special village rules: 14 Natars-held WW villages (8 outside the grey area with "50% more defending troops", 6 inside); "**No Gold Usage** — Gold cannot be used for any actions in this village (no NPC trade, no instant build)"; "**No Treasury** — a treasury cannot be built"; "**no… culture points are allowed**"; "Construction is 50% faster; troops use 50% less crop after plans appear"; and "**Once level 1, the village cannot be conquered**". Timing comes from the community page: on a normal server the end-game sequence "begins after about **280 days**, and for Speed3x servers… after about **80 days**"; "with every five levels that the Wonder is upgraded, the Natars attack the villages containing the Wonders until level 95"; the server "stops and restarts after a period of time (generally about 3 weeks)" |
| Trigger | A captured WW village plus construction plans obtained from the Natars |
| Eligibility | Whoever can hold a WW village |
| Timing | Terminal, gated by a late-game release schedule |
| Scoring | Wonder level 1 → 100 |
| Reward | **The win itself.** The official prizes page states plainly: "**Winning a normal Travian: Legends server does not provide a prize or medal**" |
| Restrictions | No purchasable acceleration inside the village; no treasury; level-1 lock-in |
| Strengths | This is the genre's documented **non-military victory path**, and it is worth taking seriously for three reasons. (1) It is an **accumulation race in which the objective itself is indestructible once begun** — the level-1 lock-in means a completed investment cannot be confiscated by force, which is precisely the property `URB-035`/`URB-040` give our cities. (2) It **purchases its own cooperation requirement** through scale rather than by mandate: "impossible for a single player to complete alone" is a consequence of the cost curve, not a rule forcing alliances, which keeps it compatible with AP-004's "membership never mandatory" in a way a hard requirement would not. (3) The official statement that ordinary victory carries **no prize and no medal** is the cleanest possible separation between *competitive outcome* and *reward economy* |
| Weaknesses | It is a geographic, seizeable structure — inadmissible for us as a *mechanic*; the cost curve makes the race unwinnable for a solo player *in practice*, which is a soft version of the same exclusivity AP-004 forbids hard; and a single terminal objective collapses all mid-game strategy into one track late in the world, exactly the "numbers-only progression" concern the Stage 1 pillars were written against |
| Exploit risks | Alliance-scale logistics dumping into one wonder; the level-1 lock-in making an early seizure permanently decisive |
| Source | `11A-RS-095` (**OFFICIAL**, CURRENT; end-game timing from **COMMUNITY**, HISTORICAL 2023-12-02) |
| Confidence | **High** for the official rules and the no-prize statement; **Medium** for the day counts |
| Second source | Yes (two official pages plus the community end-game page agree on the level-100 win) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** Take the **shape**, not the mechanic: a **long, visible, cumulative, cooperative terminal accomplishment** whose value is completion and record rather than payout, and whose investment cannot be confiscated once made (`11A-DR-030`). It is compatible with our rules through an object we already own: **B-05's four branch capstone programmes** (`URB-107`, each 100 RP) are indestructible, non-tradable, expensive national accomplishments, which makes a *capstone-completion* record the lawful mapless analogue of a Wonder — without inventing a new mechanic, which §16.4 forbids |

##### 11A-BM-064 — Beginner protection as a symmetric, unexitable, ranking-separated state

**Source rows:** `11A-RS-096`, `11A-RS-092`.


**OBSERVED (official).** "When you start Travian: Legends, your village gets **beginner's protection**. **Other players can't attack you**, so you have time to learn the game, build up resources and prepare your defence. While you're protected, other players can't send troops to you: **no attacks, raids, scouting or reinforcements. You can't send troops to other players either.** You can still send troops to targets that aren't players: **unoccupied oases**… **Natar villages**… If you try to scout another player, the game blocks it with the message 'You cannot attack other players while your beginner's protection is active'… **Note: killing Natar troops gives PvE points, not attack points, so it won't help you climb the attacker ranking.** … **You can't send resources to other players, but you can receive them** from players who are no longer protected. **Under 200 population, you can only accept marketplace offers that are 1:1 or better for you. You can still post worse offers. Nobody can accept them, so some players use them as extra storage.** **You can't end beginner's protection early.**" Duration scales with world speed: x1 → 5 days (+3 optional), x2 → 3 (+3), x3 → 3 (+3), x5 → 2 (+2), x10 → 1 (+1), with a **one-time** extension offered in the infobox. Separately, the medal page records that the very first medal, the **dove of peace**, is "**shown during beginner's protection and then fades**".

**INTERPRETATION.** Four properties are directly comparable to our own rules, and our design is stricter on three of them. **(a) Symmetry** — protected nations may neither be attacked nor attack — matches `ONB-023`/`ONB-024` exactly. **(b) No early exit** is *more* restrictive than ours, where `ONB-020` ends protection at the nation's first offensive action; our rule permits self-release, Travian's forbids it, which removes the "accept aid, then strike" exploit but also removes player agency. **(c) Ranking separation** — PvE kills score into a different category and explicitly "won't help you climb the attacker ranking" — is the single most useful fairness detail in this section: it shows a live game preventing one activity from laundering into another board, which is exactly `11A-DR-015`. **(d)** The one-way market asymmetry plus the population-scaled **1:1-or-better acceptance rule** is the same newcomer-funnel defence our `ONB-031` implements as a 30-day/360-turn one-sided transfer restriction, and the page candidly documents the leak its own design leaves: players post unacceptable offers and use them **as extra storage**.

**Confidence** High (official, verbatim). **Relevance Direct.** **Lesson** — adopt **(c)** as a hard design rule: an activity may feed **one** standing only, and cross-category laundering must be blocked at the metric definition (`11A-DR-015`, `11A-CR-014`). Reject (b) as a change to an accepted rule (`ONB-020` is fixed by `D-040`), and record (d) as evidence that one-sided transfer restrictions create predictable storage-and-shelter workarounds, which belongs to **Prompt 12** (`11A-RK-018`)

##### 11A-BM-065 — Institutionalised farming: official tooling and official self-help

**Source rows:** `11A-RS-098`.


**OBSERVED (official).** "**Farm lists** save your raid targets so you can **send raids to all of them with one click**. **Every player can use farm lists. You don't need the Gold Club.** You can have up to **100 farm lists**, each holding up to **100 targets**… For each target you set the target (a village or an oasis) and the troops sent in each raid… You can **deactivate a target** to skip it for now, for example when it has troops to defend it." Separately, an official guide "**How to avoid getting farmed**" states: "Getting farmed means other players repeatedly attack you to steal your resources. **Especially for new players, this can slow down your progress and make the game frustrating**", and prescribes self-help: "Increase your population regularly throughout the day… **Try to maintain your village population within the top 200–300 players on your gameworld**… upgrade your wall to at least **level 10–15**… keep at least **5 scouts early on**, later **20–30 scouts minimum**", adding "Frequent development signals that you're online and ready to defend yourself".

**INTERPRETATION.** This is the most uncomfortable and therefore the most instructive finding in the Travian set. The game ships **one-click mass raiding as a free, universal feature**, and separately publishes advice telling players that **being visibly growing and visibly populated is their protection**. Two consequences follow. First, where an objective or event measures *successful action against another player*, the platform's own tooling can make completion a bulk operation rather than a decision — which fails our `TR-085`/`D-014` requirement that play consist of judgements, and it makes volume metrics farmable by design. Second, the "stay in the top 200–300 or be targeted" guidance converts **population into safety**, which is exactly the §13.4 pattern "objectives that reward attacking protected or weaker nations" — inverted into "weakness is your own fault".

**Confidence** High (both official). **Relevance Direct.** **Lesson** — recorded as constraints, not suggestions: **no 11B objective or event may be completable by a bulk tool action at materially lower effort than the considered action**, and **no design may make a nation's development level a precondition of its safety** — `ONB-023`/`ONB-024` and `D-028` already make safety a status rather than a achievement threshold. `11A-RK-003`, `11A-RK-008`, `11A-DR-024`

##### 11A-BM-066 — Development tasks: geometric thresholds with an escalating reward curve

**OBSERVED (official).** "Throughout your Travian: Legends journey, you'll encounter many different **tasks** that guide your progress and reward you for development. **Each village has its own set of specific building and growth tasks, while your avatar also has general tasks that track your overall progress across all villages.** Most tasks have **multiple levels**… Completing a task grants a reward consisting of **resources (equal amounts of each type) and hero experience**. The reward amount depends on several factors: **each task type has its own reward multiplier; every new task of the same type grants a larger reward; your hero's level provides an additional bonus to all rewards.**" The published general thresholds are "**500, 1000, 1500, 2500, 5000, 10000, 20000… (unlimited increments, doubling each time)**" for population and for culture-point production, and building tasks run at "Levels 1, 3, 7, 12, 20". Community pages document the tutorial quest chain that precedes it, including a quest whose reward is "**2 Days Travian Plus**" and one whose promised "huge army" turns out to be "a single rat".

**INTERPRETATION.** Three genuinely reusable properties. **(1) Geometric thresholds with an unlimited tail** — doubling increments mean each milestone is a roughly constant *proportional* achievement, so the ladder never saturates and never needs an artificial new tier; this is the correct structural answer to the rank-ceiling problem eRepublik solved by bolting "Titan" and "Legends" onto a fixed ladder (`11A-BM-049`). **(2) Two scopes at once** — per-village tasks plus whole-avatar general tasks that aggregate across villages, which is the same nation-versus-account split our `RRL-013`/`RRL-016` must resolve. **(3) Escalating reward per repeat** ("every new task of the same type grants a larger reward") is a **compounding reward curve attached to a compounding development state**, which is precisely the runaway-leader mechanism `11A-RK-022` and §15.3 exist to prevent. The chain of tutorial quests handing out a paid-account trial is also a monetisation funnel built into the objective layer.

**Confidence** High (official). **Relevance Direct.** **Lesson** — adopt **geometric milestone thresholds** and the **two-scope split** (`11A-DR-031`); reject escalating repeat rewards, because a reward curve that steepens as capability grows is a snowball generator. Our own `URB-101` ("no percentage yields/compounding") and `NAT-052` ("milestones are records, not power") already bind this

**Unverified for Travian:** whether Daily Quests exist in the same form on every gameworld speed or variant; the exact per-quest point values (the official page publishes thresholds and rewards but not per-task point costs); current medal top-N band sizes per world population; whether the 2026 "Rise of Governors" Season Pass is permanent or annual-only; the live state of the "Local gameworlds" programme; and the full current quest list, since the community Quests page is a 2019 snapshot of the older T3.6 client.

### 5.5 NationStates — revised evidence base (official content recovered from archives)

**Correction to the earlier draft of this subsection.** The first pass at NationStates concluded that no official evidence was obtainable, because every live `nationstates.net` URL returned **HTTP 403** behind a scripted browser challenge (`11A-RS-090`). A second pass recovered the **same official pages through Internet Archive captures**, including a **2026-10-24 capture of the official FAQ**. The evidence base is therefore materially stronger than the first pass assumed, and this subsection supersedes the earlier one. **Status convention used here:** **OFFICIAL (ARCHIVED)** — publisher-authored content, retrieved from a dated capture rather than from the live site. It is still *official* content; only its **currency** is weaker. Where a claim rests on a community wiki or a third-party article, that is stated.

| ID | Source | Type | Accessed | Currency |
|---|---|---|---|---|
| `11A-RS-102` | **Frequently Asked Questions** (official), captured 2026-10-24, `https://web.archive.org/web/20261024223020/https://www.nationstates.net/page=faq` | **OFFICIAL (ARCHIVED)** | 2026-11-05 | CURRENT (capture is 11 days old at access) |
| `11A-RS-103` | **Official news index**, captured 2026, `https://web.archive.org/web/2026/https://www.nationstates.net/page=news` — dated staff posts through 01 Nov 2026, including "Z-Day15: So Long And Thanks For All The Brains" (01 Nov 2026), "N-Day15" (08 Oct 2026), "Ten Million Nations" (03 Sep 2026), "GA Compliance is Now 75%" (19 Aug 2026), "General Assembly 2026: Elections Imminent!" (22 Jun 2026), "Global Trade Fair III" (07 May 2026) | **OFFICIAL (ARCHIVED)** | 2026-11-05 | CURRENT |
| `11A-RS-104` | **Dispatch index**, captured 2026, `https://web.archive.org/web/2026/https://www.nationstates.net/page=dispatches`; and one player dispatch, `…/page=dispatch/id=2677878` (2025-07-06) | **OFFICIAL (ARCHIVED)** platform / **PLAYER-AUTHORED** content | 2026-11-05 | CURRENT |
| `11A-RS-105` | **Region page** `…/region=The_Pacific` (captured 2026) and **world statistics** `…/page=world` (captured 2024-01-20: "279,578 nations in 27,507 regions… Currently online: 10,737 nations") | **OFFICIAL (ARCHIVED)** | 2026-11-05 | CURRENT / 2024 |
| `11A-RS-106` | **Official census trend page** `…/detail=trend?censusid=0`, captured 2019-05-09 — "Civil Rights: 0.00 MLK Units. **Rank 171,969th (Top 100%)**" | **OFFICIAL (ARCHIVED)** | 2026-11-05 | **HISTORICAL** capture; mechanism corroborated by `11A-RS-102` |
| `11A-RS-107` | **Official API documentation** `…/pages/api.html` (capture of 2026) — nation shards `name, region, population, influence, income_tax, lastlogin, founded, policies, census`; region shards `officers, delegate, power`; world shards `numnations, censusranks`; rate limit "50 requests per 30 seconds" | **OFFICIAL (ARCHIVED)** | 2026-11-05 | CURRENT capture; full tables not wholly transcribable |
| `11A-RS-108` | **Secretariat page** `…/page=wasec` (capture of 2026) and official news "Introducing the World Assembly Secretariat" (2026-03-30) | **OFFICIAL (ARCHIVED)** | 2026-11-05 | CURRENT |
| `11A-RS-109` | **Community wikis:** WikiStates `https://nationstates.fandom.com` (Regional Influence 2024-07-20; World Census 2020-08-10; Issue 2024-07-20; WA Delegate 2024-08-04; Region 2024-07-19; World Assembly 2024-11-24; List of issues 2024-07-20; World Assembly Category; Raiding and Defending; Banlist; Boneyard), inheriting NSindex content under CC-BY-SA (NSindex closed 2022, read-only to 2025-07-20, now offline); and NPOWiki `wiki.npowned.net` (last edited 2025-11-22) | **COMMUNITY** | 2026-11-05 | Mixed; the census page is **HISTORICAL (2020)** |
| `11A-RS-110` | **Mirrored official forum posts:** staff answer on regional officers, `https://web.archive.org/web/2024/https://forum.nationstates.net/viewtopic.php?f=15&t=356700`; "What is a 'Native'", archived 2025 | **OFFICIAL (ARCHIVED)** forum, staff-authored | 2026-11-05 | **Mixed currency** — the underlying posts are **HISTORICAL** (2024/2025 captures of staff answers) |
| `11A-RS-111` | **Jolt Archive** mirror of the old official forum, `https://nationstates.ermarian.net/jolt/1224/477177`, posts dated **2006-04-12…04-16**, containing the developer's and a moderator's own statements of influence design intent | **OFFICIAL (ARCHIVED, mirrored)** | 2026-11-05 | **HISTORICAL** — origin of the influence system |
| `11A-RS-112` | **Third-party:** Wikipedia "NationStates" `https://en.wikipedia.org/wiki/NationStates` (fetched 2026-11-04; 337,296 active nations cited as of 2026-05-14; the 2026-01 dispatch-search breach; the absence of war/trading mechanics citing BBC 2004) | THIRD-PARTY | 2026-11-04 | CURRENT-ish; **not** a developer rulebook |
| `11A-RS-113` | **Player-authored guides:** "Beginner's Guide to OWL and the World Assembly" dispatch and the "Got Issues?" forum thread, both read through `https://web.archive.org/` captures of `https://www.nationstates.net/` and `https://forum.nationstates.net/`; per-capture locators not retained | COMMUNITY / PLAYER-AUTHORED | 2026-11-05 | HISTORICAL/Medium |
| `11A-RS-114` | **Still unreachable**, recorded as gaps: live `nationstates.net` and `forum.nationstates.net` (**403** challenge); `page=qa` Q&A archive (**403** and no captures found); `nationstateswiki.org` (dead); the "One-Stop Rules Shop" detail page | — | 2026-11-05 | **Unavailable** |

##### 11A-BM-067 — Population milestones that unlock **authorship**, not power

| Field | Content |
|---|---|
| Game / System | NationStates — long-term progression |
| Mechanic | Population-gated identity control |
| How it works | **OBSERVED (official).** "Why can't I set my nation's pretitle, Capital City, Leader, or Religion? This becomes possible at particular population levels: **250 million**: …issue that allows you to set a **Capital City**… **500 million**: You can write a custom **pretitle**… **750 million**: The **Leader** issue… **1 billion**: The **Faith** issue. **If you dismiss the issue, the custom field will remain locked and you will receive the same issue again at some point in the future.**" Population itself "grows steadily over time no matter what you do" |
| Trigger | Reaching a population threshold, which generates an issue |
| Eligibility | Every nation |
| Timing | Long-horizon; the offer **returns** if declined |
| Scoring | Population, which grows automatically |
| Reward | **The right to name things** — capital, leader, pretitle, faith |
| Restrictions | Must accept the issue; nothing is granted on decline, but nothing is lost either |
| Strengths | **This is the single best-fitting progression idea in the whole study for Nation Supremacy's constraints.** The reward for growth is *authorship over your own nation's identity*, not capability. It cannot create a power gap, cannot be farmed into advantage, cannot be transferred, and gets more valuable precisely as a player becomes more invested. The **return-on-decline** rule is also exactly the "dismissal is not forfeiture" property worth copying |
| Weaknesses | Tied to automatic time-based growth, so it rewards duration rather than decision — which for us collides with `NAT-045` (no differential by age) and the rejected `FO-024`; and the thresholds are absolute, so they do not scale with world population |
| Exploit risks | Essentially none, because nothing mechanical is granted |
| Source | `11A-RS-102` (**OFFICIAL (ARCHIVED)**, CURRENT) |
| Confidence | **High** |
| Second source | Partial (`11A-RS-109` confirms the population-gated issue family) |
| Relevance | **Direct** |
| Lesson | **LESSON / DIRECTION.** A progression ladder whose rungs are **identity rights and expressive authorship** rather than capability is lawful here in a way no comparator's is: it does not touch `ECN-092`, `NAT-045`, `DMP-051` or `URB-158`, and it satisfies `NAT-051`'s "progression is **chosen**, not handed out" literally. Adopted as the backbone of the recommended progression model (`11A-DR-017`, `11A-DR-032`), with the caveat that our thresholds must derive from **achievement of state**, not elapsed time |

##### 11A-BM-068 — Cosmetics that are explicitly inert, and a market built on them

**Source rows:** `11A-RS-102`, `11A-RS-109`.


**OBSERVED (official).** Postcards: "Postcards, which can be used in your nation banner, are awarded when you reach a particular state. **If your nation is already close to that state, a small step in that direction can get you over the line.** Similarly, approving a broad-based program can qualify your nation for a postcard specific to one thing." Trading cards: "Each time you answer an issue, you have a chance of receiving a new pack… **Cards are cosmetic. They grant no benefits other than the warm fuzzy feeling of owning them.**" A bank and timed double auction exist only for cards ("There are only two ways to acquire bank: junk cards or sell them"), the auction is deliberately "designed… **reducing the ability of puppet nations to feed valuable cards to their masters**", and cards and bank are deleted with a nation that is not restored.

**INTERPRETATION.** Two transferable ideas. (1) **Milestone recognition harvested from decisions the player already made.** Postcards arrive from *states reached*, not tasks performed — the reward is a by-product of play, so it adds no chore. The "a small step near a threshold can get you over the line" behaviour is an explicit, forgiving threshold-crossing rule. (2) **A collectible economy whose value is declared to be zero** — the official text says the cards grant no benefit, and the auction design is written to defeat alt-account feeding. That is the exact posture our `NAT-052` ("milestones are records, not power") and `REQ-073` (no first-time reward convertible into a transfer) require.

**Confidence** High (official). **Relevance Direct.** **Lesson** — `11A-DR-008`, `11A-DR-033`: prefer **state-triggered** recognition over **action-triggered** tasks, and if any collectible layer is ever specified, publish its inertness in the rule text as NationStates does |

##### 11A-BM-069 — A decision queue with a hard cap and a first-class dismissal

**Source rows:** `11A-RS-102`, `11A-RS-086`, `11A-RS-089`.


**OBSERVED (official + community).** Official: "A few times a day, you'll face an issue and need to decide what to do about it. How you respond determines almost everything about how your nation evolves. **There's no micro-management**." Dismissal is a named option: "**Dismiss it!** This is the equivalent of ignoring an issue… But it's usually more interesting if you take a position." Hard cap: "**Nations can hold a maximum of five issues.** Dismiss or deal with some first, and new ones will begin flowing in." Community-sourced detail: steady state settles around one issue per six hours, with 12/24/48-hour throttle options; vacation mode stops delivery entirely; effects are **status-dependent** ("shutting down a newspaper… is just another day at the office for a Psychotic Dictatorship, but a major policy shift in a nation with a history of protecting the free press"), deliberately **extreme-biased** ("everything tends to gravitate to the most extreme outcome… it's usually easy to reverse the effects") and **reversible-leaning**.

**INTERPRETATION.** The queue cap is the missing control in every other comparator's event system. Politics & War's seasonal event and Travian's daily quests both *add* content on a schedule and rely on the player to absorb it; NationStates **bounds the outstanding backlog to five** and generates no more until the player acts. Combined with a first-class "ignore this" that carries no penalty, the system makes content pressure a player choice rather than an imposed duty — a direct, implementable answer to the notification-fatigue question in Prompt 11A §12.4 that does not depend on player-facing settings screens.

**Confidence** High for the cap and dismissal (official); Medium for the cadence figures (community). **Relevance Direct.** **Lesson** — adopt **a bounded outstanding queue** and **penalty-free dismissal** as event and objective lifecycle requirements (`11A-DR-005`, `11A-DR-009`). The status-dependent effect model is also a warning for `AP-006`: NationStates' own FAQ contains the question "This issue boosted Civil Rights in one nation but not another. What gives?", which is a legibility failure caused by context-sensitive effects without visible attribution |

##### 11A-BM-070 — Compliance: an opt-in jurisdiction with an ongoing obligation

**Source rows:** `11A-RS-102`, `11A-RS-103`, `11A-RS-108`.


**OBSERVED (official).** WA membership "is not compulsory. **If you remain outside, you're mostly unaffected by its decisions.**" Resolutions may be "adopted by your nation, which can affect your laws and classification… **if you don't adopt at least 75 %, you will be deemed non-compliant, and not allowed to participate in future WA votes**" — and the threshold is live-tunable, confirmed by the official post "GA Compliance is Now 75%" (2026-08-19). Legislative access is tiered: **≥2 endorsements to propose**, **only Delegates approve**, a proposal needs **6 % of all Delegates** to reach the floor, and passed law then requires individual adoption. The Security Council's instruments are **Declarations, Commendations, Condemnations, Liberations and Injunctions**, with badges for commended and condemned nations. The Secretariat is five elected nations, candidacy needing **≥5 endorsements** and voting a **≥30 million population** gate, elected every six months, publishing **Opinions** (voting recommendations).

**INTERPRETATION.** Three structural ideas. (1) **Membership is jurisdiction, not account status** — opting out is a legitimate permanent choice with a stated consequence (you are simply unaffected), which is a far better model than a hidden penalty and matches `AP-004` directly. (2) **A post-decision obligation keeps a body alive** — the adoption requirement means legislation is not a one-off vote but an ongoing housekeeping act, which is what makes participation a *path* rather than an event. Our own analogue is B-06's continuous retention tests (`DMP-215`…`DMP-224`), so the shape is already accepted. (3) **A cheap multi-use social token** — the endorsement — elects executives, weights votes and gates candidacy. That leverage is precisely what makes it a target, which NationStates documents candidly ("organized groups… moving there en masse and endorsing each other").

**Confidence** High (official, with 2026 confirmation of the live threshold). **Relevance Direct** (rankings and progression; political participation). **Lesson** — adopt **membership-as-voluntary-jurisdiction** and **tiered social-token gating** only as *counts* (`11A-DR-023`); reject any token that confers mechanical vote weight, because `DMP-195` ("campaign spending cannot buy an election") and `DIP-084` already forbid a purchasable or accumulative influence (`11A-OPEN-015`). A compliance-style obligation is admissible for a voluntary cooperative event, where non-participation costs only exclusion from that event |

##### 11A-BM-071 — Influence with decay-on-departure, and ejection cost scaling with the target

**Source rows:** `11A-RS-105`, `11A-RS-107`, `11A-RS-111`, `11A-RS-082`.


**OBSERVED (official).** "It's a measure of how well-respected a nation is in its region. Nations earn influence in a region the longer they remain there and the more endorsements they have. **When a nation leaves, its influence in that region begins to decline.** **The more influence a nation has, the more influence the Delegate requires to eject it from the region.**" Delegates "must spend Regional Influence" for regional actions; "A Governor can strip power from a Delegate, but the reverse is not true… Governors may wield power as they see fit, while Delegates must spend Regional Influence… **This tends to limit the power of Delegates who aren't long-term residents.**" Design origin, from a mirrored 2006 official forum thread: "Nations accrue influence… by remaining in the region, and by receiving endorsements", and "**it's at the heart of a change to how UN Delegates get to wield power**". Community adds a 30-step rank ladder (Zero → Hermit) and the anti-coup rationale. Notably **influence is region-scoped and rebuilt from zero on each move**, and a **26-hour permission lockout on newly appointed officers** in game-created regions is reported by a community mirror of official material.

**INTERPRETATION.** Two devices are reusable in principle even though influence itself is inadmissible for us. **Decay-on-departure** is the only standing measure in the entire study that *loses* value through absence — the mirror image of our `D-028` dormancy protection — and it exists specifically to stop a newcomer cohort converting arrival into instant authority. **Cost-scaling-with-target** is an elegant anti-coercion primitive: the effort required to remove someone grows with that person's own standing, so tenure itself is a defence. Both are governance devices, and governance is B-09's and Prompt 12's territory.

**Confidence** High for the official statements; Medium for the ladder and the lockout. **Relevance Supporting.** **Lesson** — recorded as a **governance observation for Prompt 12**, not as an 11A proposal: `UD-047` and `UD-049` are owner-reserved, `ECN-092` bars a new accumulating currency, and nothing here may alter Alliance governance. `11A-DR-028`, `11A-OPEN-015`

##### 11A-BM-072 — "Magnetism": an official collective score built from hospitality and freshness

**Source rows:** `11A-RS-082`, `11A-RS-109`.


**OBSERVED (community, describing official behaviour).** A scoring rubric determines a Frontier region's share of newly founded nations. Positive conditions: "Being at least one week old (ideally, at least one year old); Having a **Welcome telegram**; Having a WA Delegate with **at least 5 endorsements** (ideally, at least 50); Having a WA Delegate **in office for at least 2 days, and ideally less than 6 months**; Having at least **one new post on its Message Board from the prior 12 hours**." Negative conditions: "It has a password / no WA Delegate / **more than 5,000 residents** / changing Frontier designation / No posts in prior 72 hours."

**INTERPRETATION.** This is the most interesting collective-progression object in the study, because **almost nothing in it is power**. A region attracts newcomers by being welcoming, active, open and recently turned over — and the delegate term sweet spot is **at least two days but under six months**, an explicit **anti-entrenchment inversion**: long-incumbent leaders make a region *less* attractive. The 5,000-resident ceiling prevents a winner-take-all pool. Population flow is therefore earned through behaviour the game can observe, not through assets.

**Confidence** Medium (community-mirrored; no official page reachable). **Relevance Direct** (progression; rankings). **Lesson** — the shape is worth one narrow adoption: a **participation-and-hospitality** style collective measure, computed only from already-public facts, capped rather than unbounded, and **never** paying material reward. That fits `ALL-224` (no prizes from alliance funds) and `AP-004` (never mandatory). Recorded as `11A-DR-011` and `11A-DR-016`, with its evidential weakness marked

##### 11A-BM-073 — Negative finding: NationStates has no achievement system, and no composite national rating

**Source rows:** `11A-RS-102`, `11A-RS-103`, `11A-RS-104`, `11A-RS-106`, `11A-RS-114`.


**OBSERVED (official, by absence).** The official FAQ enumerates its own sections completely and contains **no** achievements or awards section. The reward surfaces that do exist are postcards (`11A-BM-068`), cosmetic trading cards, Security Council commendation/condemnation badges, easter-egg issue badges, the region-scoped influence ladder, and editorially announced site milestones such as "Ten Million Nations" (official news, 2026-09-03). The only "award" publications in the live dispatch index are **player-run** bodies. No reachable source documents a single composite national rating either; the term sometimes used for one could not be traced to any official mechanic, and the closest real objects are a census category's percentile display ("Rank 171,969th (Top 100%)") and the 27-category government type.

**INTERPRETATION.** A game with an 18-year lifespan and millions of nations runs long-term motivation on **identity, status and description** rather than on a checklist of achievements — and its own FAQ answers "How do I win?" with "Beats the hell out of me." This is a genuine design datapoint, not a gap: **achievements are one solution to long-term goals, and at least one successful game demonstrably does not use them.** It tempers §13's recommendation: a Nation Supremacy achievement framework is *permitted* (`NAT-052` says Prompt 11 owns it) but is not *obligatory*, and the alternative — milestones that unlock authorship — is evidenced as sufficient.

It also supplies the honest counterweight to `D-021`'s no-catch-up posture: NationStates' population growth is automatic ("grows steadily over time no matter what you do"), so its progression ladder is partly time-based, which is exactly what our age-differential rule forbids. The transferable part is the **reward type** (authorship, not capability), not the **advancement driver** (elapsed time).

**Confidence** Medium-High (a bounded absence: full official FAQ text plus a wiki category scan, neither showing an achievement system). **Relevance Direct.** **Lesson** — `11A-DR-034`: keep the achievement layer **small and optional**, and let authorship, records and standings carry long-term motivation. No name, condition or presentation from any comparator is reproduced (`AP-008`)

