# STAGE 1 — PROMPT 2: STRENGTHS, WEAKNESSES, PLAYER FRUSTRATIONS, AND IMPROVEMENT OPPORTUNITIES

**Project:** Browser-based persistent multiplayer nation-strategy game ("the project")
**Document:** `docs/stage-1/02_strengths_weaknesses_player_frustrations.md`
**Version:** 1.0 — prepared 2026-10-22 (all web sources accessed 2026-10-22 unless a source carries its own publication date)
**Builds on:** `docs/stage-1/01_competitor_research.md` (Prompt 1, reviewed in full before this work)
**Status:** Complete for Prompt 2. Does not begin Prompt 3, the Game Design Bible, or any implementation.

---

## Section 1 — Executive summary

### The most important supported findings

1. **Community is the genre's core product, not the mechanics.** Across games, the best-evidenced "strength" is the social layer. For Politics & War, a Google Play reviewer (listing updated 2025-10-13) describes the game as fun when engaged with its community and otherwise like a "farm simulation"; a long player essay on the official forum credits interactions and social recognition as the main attraction; NationStates' own creator credits the community with much of the site's value ([Max Barry, 2022-11-12](https://maxbarry.com/2022/11/12/news.html)). The symmetric warning: P&W players have also complained the game becomes boring when player-driven activity is absent ([official forum, "Boring game," 2019-04-13](https://forum.politicsandwar.com/index.php?/topic/25296-boring-game/)). **Implication:** mechanics that could help a community form and coordinate matter as much as any combat math.
2. **Steep learning curves and jargon burden are the genre's most consistent documented weakness.** Nearly every game investigated maintains large glossaries of private terminology (P&W's official glossary documents dozens of community acronyms; NationStates regional communities publish their own; eRepublik and Prosperous Universe players have written dedicated interface guides). A 2020 P&W forum proposal explicitly links the learning curve, difficulty of getting sound advice without existing contacts, and retention problems. Prosperous Universe forum threads document costly early mistakes and requests for clearer tutorials. **Implication:** in-context explanation is not polish — it is a first-class system for this genre.
3. **The newcomer catch-up gap is real and repeatedly documented in the reward-time-compressed games.** eRepublik (2018 player article with corroborating comments; 2023 official-oriented guide noting old accounts' lasting strength advantage), Sim Companies (2023 Steam review on veteran market power and squeezed margins), and P&W (2024 multi-participant forum discussion about effects on new/small nations) all show the same shape: long-lived accounts accumulate advantages that latecomers cannot readily counter. **Implication:** our design needs an explicit, honest answer for late entry.
4. **Pace polarizes, and both halves are legitimate players.** The slow check-in cadences that one Steam reviewer loves in Sim Companies ("daily check-in routine", described positively) cause another to quit after just over an hour of waiting; Prosperous Universe reviewers split the same way over its intentionally slow real-time economy. **Implication:** a 2-hour turn world should let *short sessions produce visible progress* while permitting longer planning.
5. **There is little evidence that players love the turn cadence itself.** Documented appreciation centers on communities, progression, and supply chains; the 2-hour turn and "always-on world" are documented but not evidenced as beloved. **Implication:** our turn schedule should be treated as an enabling structure players tolerate — the daily experience around it must carry the value.
6. **Anti-grief and protection mechanics work but generate their own exploit debates.** P&W's "beige" post-war protection is actively strategized around (2022 forum thread proposing changes); vacation/peace modes and score-band targeting recur across games as necessary-but-contested tools. **Implication:** protection systems need to be designed with exploit analysis from day one.
7. **The catch-up burden of automation or manual repetition is a live dispute about workload, not morality.** P&W's 2022 forum debate (103 replies) about banning third-party automation centers on alliance military management workload. Sim Companies and Prosperous Universe complaints include repetitive waiting-driven check-ins. **Implication:** a turn-based design should reduce bookkeeping friction without enabling unfair automation.

### The most important uncertainties

- **Reddit content could not be read by any research tool** (all platforms). Reddit is where many current-tier complaints live; therefore findings here skew toward official forums and store reviews, and cannot measure what proportion of players hold any view.
- **Small-player-base claims** (decline, ghost nations, "dead" markets) rest on player-authored articles and are not independently verified for any game.
- **Moderation disputes, bot prevalence, and "toxicity" claims** could not be verified as patterns across games; where seen, they are single voices or uncorroborated leads (explicitly labeled as hypotheses rather than findings).
- **One review's complaint is one review:** several findings (e.g., P&W "no restart" request, Sim Companies late-game-goal request) rest on single comments, and are labeled accordingly.

### The implications for our game

Our project stands to differentiate less on raw mechanics and more on **(a) transparent onboarding (explain everything in-context), (b) honest late-entry answers, (c) frictionless but fair action interfaces, (d) a turn outcomes report that explains the world state without a manual, (e) protection systems designed to survive exploitation analysis, and (f) community-first tooling (alliance coordination without forcing orphans into alliances)**. No mechanic in this report is finalized; everything is an opportunity for later design stages.

---

## Section 2 — Research methodology

### Previous research reviewed

`docs/stage-1/01_competitor_research.md` (Prompt 1, v1.0) was located, read in full, with re-verification of its Executive summary, methodology, and Section 10 handoff), and treated as the foundation for this task. Its game profiles, system analysis, and the "closest analogues per system" handoff were reused as the baseline, and this report deliberately does not repeat that material — it adds evidence about *player experience* to it. No conflicts with Prompt 1 findings were found; two Prompt 1 topics (2-hour-turn acceptance; player-driven-market praise) are **qualified** here as lacking player-praise evidence, which is recorded rather than silently changing Prompt 1's conclusions.

### Games and sources investigated

Primary game set (from Prompt 1): **Politics & War** (primary reference, dedicated praise–track and complaints–track), **NationStates**, **Cyber Nations**, **eRepublik**, **Prosperous Universe**, **Sim Companies**, plus cross-genre onboarding/retention lookups for **Cantr II, Earth Empires, Utopia, eDominations**.

Source types actually used:

- Official game websites, homepages, official wiki/pedia pages, official update logs, official license/handbook pages.
- Official game forum threads (P&W forum, Earth Empires forum, Prosperous Universe community platform, Sim Companies community forum).
- App-store reviews: Google Play and Apple App Store listings for Politics & War, Sim Companies, eRepublik; Apple App Store review pages for Politics & War.
- Steam community review pages for Sim Companies and Prosperous Universe.
- Independent articles and retrospectives (Wikipedia, SUPERJUMP 2023, PopMatters 2007, indie blogs, IndieDB review).
- Player-authored essays and guides (P&W forum blog, eRepublik in-game articles 2012–2025, NationStates community glossaries).

### How claims were identified and corroborated

- **Strengths and weaknesses** were first searched separately from frustrations, to prevent confirmation bias.
- **Reddit was a target for all games, but the reading tool could not return readable Reddit text on any attempt.** Reddit search-result snippets were therefore NOT treated as evidence anywhere in this report. This limitation is stated here once and affects every game.
- Where a finding could be corroborated across ≥2 independent sources, it is labeled **Strong evidence** or **Moderate evidence**; single-source observations are labeled **Weak evidence**. The labels follow the definitions in Section 11 of the task.
- Direct quotations are used sparingly and paraphrased where appropriate; no quotations, statistics, percentages, populations, or review scores were invented anywhere. Where a source's own post text was not readable, it is marked unused.
- Historical vs current status is labeled per finding.

### Limitations

- **Representativeness unknown:** store reviews and forum posters are self-selected.
- **Discord and Telegram** content (a major venue for these communities) cannot be researched without accounts, and is therefore a general blind spot of this report.
- **No live accounts were used**; nothing here is based on hands-on testing.
- **P&W's state on Reddit matter** (a major current-era complaint venue) is not represented; conclusions about current-day prevalence should be considered provisional.

---

## Section 3 — What existing games do well

Findings are organized by game, then by system within each. For every item: what is claimed, what evidence supports it, who benefits, and the trade-off.

### 3.1 Politics & War

**A. The social sandbox and alliance community (Strong-moderate).** A Google Play reviewer (listing updated 2025-10-13, ~4.2-star/~3,900 reviews displayed at fetch) calls the game "incredibly fun" if you engage with its "atmosphere/community," while characterizing it otherwise like a farm simulation without that social layer; another player blog on the official forum uses social recognition and measurement of progress ("tweaking numbers to perfection") as the game's central appeal ([forum blog, undated](https://forum.politicsandwar.com/index.php?/blogs/entry/54-politics-war-vs-nationstates/)). Trade-offs: the same community dependence means the game reportedly feels empty when community activity is quiet ("Boring game," 2019-04-13, forum).

**B. Measurable optimization: cities/infrastructure progression (Moderate).** The community wiki's detailed growth path (e.g., [City building from 0 to 1000](https://politicsandwar.fandom.com/wiki/City_building_from_0_to_1000)) demonstrates an established, formulaic progression loop with visible milestones; the player blog above indicates some players find it intrinsically satisfying. Trade-off (documented): a Google Play reviewer says early building is *too slow* initially — the same pacing both gives a long-term goal and frustrates early on.

**C. Wars as shared narrative and history (Moderate).** Official positioning and the player blog agree that wars, rankings, and alliance politics give players something to talk about and remember (P&W homepage; forum blog). Trade-off: wars as *mechanic* are the genre's most contested system (Section 4).

**D. Player-driven market (Documented, praise unestablished).** Officially, the economy is 100% player-driven and trading is central (P&W homepage); a community wiki guide explicitly teaches treating prices like a stock market. What could NOT be established: evidence that players specifically like it more than they'd like alternatives — no strong player-praise evidence found. Lesson: having a real market *is* essential to the genre; celebrating it to players may not win loyalty by itself.

### 3.2 NationStates

**A. Flexibility of commitment (Strong).** Multiple independent accounts (Wikipedia; SUPERJUMP 2023; a long-time player's blog 2023) describe the same pattern: a two-minute-ish daily session answering issues can be the whole game, or the experience can expand into years-long roleplay diplomacy and regional politics. Player benefit: it welcomes the busy and the deeply invested. Trade-off: the two halves share one interface and one jargon layer, badly confusing newcomers (enumerated in Section 4).

**B. Community-created depth (Strong).** The creator's own 20-year anniversary essay credits the community with most of what makes the site worthwhile ([Max Barry, 2022-11-12](https://maxbarry.com/2022/11/12/news.html)); independent retrospectives agree. This supports a general genre lesson: the best systems are the ones the *players* fill meaning into — the game's job is to scaffold them, not replace them.

**C. World Assembly political drama (Moderate).** WA voting, delegate contests, endorsements, and Security Council actions give the community real stakes (WikiStates; Wikipedia). Players compete for political recognition *without any combat or money at all* — evidence that political recognition systems can be intrinsically motivating.

### 3.3 Cyber Nations

**A. Social/alliance strategy as the durable pleasure (Moderate, historical review).** PopMatters' 2007 independent review describes alliance play — trading, diplomacy, forums, elections, war councils — as where the game becomes rewarding ([PopMatters, 2007-09-19](https://www.popmatters.com/cyber-nations-2496238708.html)). The game's slow once-daily loop makes every meaningful interaction social rather than mechanical (though "players praise variety" was *not* independently established for current-day Cyber Nations; the game is much smaller now than historically).

**B. Once-daily cadence is deliberate, not an accident (Documented).** Official material and a 2007 review converge on one-collection-per-day and once-daily troop deployment as the model ([official FAQ rules text in community FAQ](https://cybernations.fandom.com/wiki/Frequently_Asked_Questions_about_Cyber_Nations); PopMatters). Lesson: very slow cadences are viable *when social play carries the excitement*.

### 3.4 Sim Companies

**A. Accessible business variety and supply-chain play (Strong by store-review corroboration).** Steam reviews praise range of products, free trade with other companies, and supply-chain planning as the core fun (reviews dated 2023-08-31 and 2024-05-26); the official app descriptions frame market-sensitive business as core mechanics. Player: anyone who enjoys building and choosing production lines. Trade-off: economy depth hides behind imperfect onboarding (Section 4).

**B. Short management sessions work well (Moderate).** Steam reviews on both sides (2023, 2024) converge that session shape — set up work, come back later — is the intended and for many the enjoyable structure. Trade-off: the same shape is a quitting point for impatient players (a 2023-11-11 review quit after >1-hr waiting early in the tutorial).

### 3.5 Prosperous Universe

**A. Logistics/planning depth as the core product (Strong).** Steam reviews (2022-04-20 positive one describes "extract-manufacture-ship-cooperate") and the Steam store descriptions agree the game is about multi-step production chains and shipping. Trade-off: depth requires the genre's steepest command interface.

**B. Enthusiastic community helps (Moderate).** In-game community channel and forum support is praised in a 2026 Steam review; forum threads from 2020 show genuine mutual instruction. Trade-off: helpful players don't scale unless the game itself scales knowledge (its tutorials have been found wanting since 2020).

### 3.6 Cross-game strengths worth carrying forward

- **A world that goes on without the player** (all studied games) — supports fantasy of "my nation exists while I sleep." The turn/income engine is proven.
- **Language of recognition**: rankings, titles, wars, public histories recur in every praised game.
- **The games that survived longest** (NationStates 20+ years, Cyber Nations ~20 years) lean on social layers rather than mechanics — supporting the Prompt 1 finding that live-ops/community is decisive.

---

## Section 4 — Documented weaknesses

The classification per item: **[Confirmed]** = documented by sources with named links; **[Historical]** = documented but dated, may no longer apply; **[Hypothesis]** = plausible, not corroborated.

### 4.1 Steep learning curves and jargon burden (Genre-wide) — **Strong evidence, Confirmed**

- P&W's official glossary currently documents dozens of community-only abbreviations and terms ([P&W-pedia Terminology and Glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary)) — the *game itself* acknowledges the vocabulary burden.
- A 2020 P&W forum proposal says the learning curve and slow daily mechanics hurt retention and that newcomers struggle to get sound advice without existing contacts ([Alliance Creation Restrictions, 2020-09-02](https://forum.politicsandwar.com/index.php?/topic/29803-alliance-creation-restrictions/)).
- NationStates regional communities maintain their own glossaries explicitly "for new players" ([community example](https://www.tapatalk.com/groups/kantrias/glossary-of-nationstates-terms-and-acronyms-t26.html), 2012).
- eRepublik players have produced dedicated GUI explainers ([2015 guide](https://www.erepublik.com/en/article/2488034), [2019 guide](https://www.erepublik.com/en/article/2702627)) because the interface alone doesn't teach itself.
- Prosperous Universe players in 2020 forum threads describe making **costly early mistakes** and ask for clearer tutorials on profitability/market/shipping tasks ([forum thread Mar 2020](https://com.prosperousuniverse.com/t/new-player-feedback/2068)).

*What it is:* the games' knowledge lives in community documents (wikis, glossaries, Discord) rather than in-game. *Who's hurt:* new and returning players. *Trade-off:* complexity can be depth; not all of it is removable. *Confidence:* strong for the existence of the burden; unknown for how often it causes quitting.

### 4.2 Newcomer catch-up gap / veteran advantage (eRepublik, Sim Companies, P&W) — **Strong evidence (eRep), Moderate (SC, P&W), Confirmed**

- eRepublik 2018 article "Is Erepublik fair for new players? Players are forced to buy gold to advance" ([2018-08-04](https://www.erepublik.com/en/article/2676982)) with commenters agreeing the game is too P2W; corroborated structurally by a 2023 guide noting old accounts' accumulated ground-battle strength advantage ([2023-06-11](https://www.erepublik.com/en/article/2770076)). **Historical-but-current-layer:** the claim is about durable account accumulation, which is still the architecture.
- Sim Companies: high-hours Steam review (2023-12-06) argues established players and thin margins make growth hard for newcomers ([reviews page](https://steamcommunity.com/app/2253720/reviews/?browsefilter=toprated)). Moderate: one review + an older forum example of unprofitable upgrades (2019).
- P&W: 61-reply 2024 forum discussion on how core design affects new nations, new alliances, and smaller alliances ([May 2024](https://forum.politicsandwar.com/index.php?/topic/40471-the-problem-at-the-core-of-pnw/)). Moderate: multi-participant, no consensus stated.

*Trade-off:* deep long-term progression is a *feature* (reward commitment), and catch-up mechanics that erase it would hurt the committed. The problem is not that veterans are strong — it's whether a newcomer's *first weeks* feel meaningful and safe.

### 4.3 Interface/usability complaints (P&W, Sim Companies, PU) — **Moderate evidence, Confirmed[current-ish]**

- P&W App Store reviews (2021-02-22, 2021-08-06): trade tables require excessive scrolling; interface poorly laid out and hard to navigate ([Apple review page](https://apps.apple.com/au/app/1552461332?see-all=reviews&platform=iphone)). A July 2025 forum user proposes a "Modern UI / PnW Refresh" — evidence the base interface still feels dated to at least some current players ([2025-07-24](https://forum.politicsandwar.com/index.php?/topic/52736-modern-ui-pnw-refresh/)).
- Sim Companies: Google Play review (2023-08-27) says the interface and initial explanation make it hard to understand the game — though the same reviewer says the game became compelling on a later attempt, indicating onboarding, not the game, is the bottleneck.
- Prosperous Universe: a negative 2023-10-04 Steam review criticizes UI usability and reliance on wiki visits.

*Trade-off:* none — this is largely an execution-quality problem, i.e., a fixable weakness.

### 4.4 Repetitive waiting and check-in pressure (Sim Companies, PU, eRepublik) — **Moderate evidence, Confirmed (design-shaped, differently judged)**

- Sim Companies: a review quit after hitting a >1-hour wait right after the tutorial (2023-11-11); another sees "daily check-in routine" as a *positive* (2024-05-26). Polarized.
- eRepublik: routine daily work/train/food/energy/weapon maintenance documented across guides 2015–2023 as the required loop; guides warn against *paying* for energy. The chore loop is real; whether it frustrates depends on the player.

### 4.5 Protection mechanics are strategizable/exploitable (P&W beige) — **Moderate evidence, Confirmed (single discussion, sustained system debate)**

- A 2022 forum thread ("Proposed Beige Change", 2022-03-15) documents players engineering wars to *expire on schedule* so a victor can put a loser into beige, and proposes changing the mechanic. Confirms: the protection state, intended as mercy, is used as a tool.

### 4.6 War system complaints (P&W) — **Weak-to-Moderate evidence**

- P&W's "politics and war but it is centrally around war" critique (2025-01-02) argues the nonwar political gameplay is thin relative to the name ([thread](https://forum.politicsandwar.com/index.php?/topic/48019-the-game-name-is-politics-and-war-but-it-is-centrally-around-war/)). Single voice; weak.
- "War Changes" (2025-01-22) proposal argues nations with minimal military shouldn't be able to declare on established nations — documents *readiness-requirement* concerns, not a widespread "farming" epidemic. Weak evidence of prevalence.
- The 2024 "Problem at the Core of PnW" thread (61 replies) is the strongest structural critique surface, focused on effects of the war/design system on new/smaller alliances. Moderate.
- **Not established (labeled hypothesis):** systematic "farming" of small nations, ubiquitous combat determinism, and universal loser-friendliness complaints. The IndieDB 2019 negative review alleges newcomer disadvantage and toxicity — one reviewer.

### 4.7 Automation/administration workload disputes (P&W) — **Moderate evidence, Confirmed as ongoing debate**

- The 2022 forum debate on bots/in-house tooling (103 replies, 2022-02-10) reveals that running an alliance's military management *manually* is a real burden for working adults, and that automation is demanded by some and feared by others ([thread](https://forum.politicsandwar.com/index.php?/topic/32750-my-thoughts-on-bots-and-a-plea-to-blanket-ban-all-third-party-automation-and-develop-the-tools-inhouse/)). The trade-off question is genuinely unresolved in the source game.

### 4.8 Monetization friction (eRepublik, Sim Companies, PU) — **Moderate evidence, Confirmed[current]**

- eRepublik gold purchases and pay-to-win perception (2018 article + comments, historical; structure persists).
- Sim Companies: paid "boosts" criticized by one 2024 Steam reviewer as an efficiency advantage; the game is otherwise free-play formidable by design.
- Prosperous Universe: PRO subscription (€8/month, official Manual) gates Local Markets/custom contracts/recurring production and other late-game-relevant features; reviews from 2022/2023 question value for a slow game on a small playerbase.

### 4.9 Community decline and re-entrant discouragement (eRepublik) — **Moderate evidence from player-authored analysis (labeled accordingly)**

- 2022 in-game returning-player essay "A quiet welcome to eRepublik" (2022-02-23) finds fewer parties/units in eUS than memory, commenters describe forum decline and activity migrating to Discord/Telegram ([link](https://www.erepublik.com/en/article/2749278)).
- 2024 player-authored "Demographics and Player Retention" argues active-player measures fell over time, while acknowledging mixed definitions and recompiled sources ([2024-06-14](https://www.erepublik.com/en/article/2780184)). Its causal explanation (military drift, strength gap) is the author's analysis.
- **Not established:** any current planet-wide player count for any game examined.

### 4.10 Public documentation decay (Earth Empires, eRepublik, Sim Companies explicit; genre-wide tendency) — **Moderate evidence**

- Earth Empires 2017 forum thread documents public guides missing/dead links and a moderator-requested restoration ([2017 thread](https://www.earthempires.com/forum/strategy-room/public-guides-and-turn-for-turn-startups-42844)).
- eRepublik's own wiki Tutorial page is explicitly marked outdated by the wiki itself.
- Sim Companies official FAQ/guide pages still fail to render fully in web research (2026 pass), so their wiki/guides remain primary learning aids.

### 4.11 Late-game motivation scarcity (Sim Companies) — **Weak evidence (single review)**

- Google Play reviewer requests additional prestige/audit/goal layers after multimillion-company status (2024-10-22). Single review; labeled hypothesis.

### 4.12 First-failure punishment (P&W) — **Weak evidence (single review)**

- App Store reviewer (2025-06-23) asks for a "restart" because a new nation can be destroyed by another player with no recovery path — a single explicit request but consistent with genre-wide damage systems.

### 4.13 Technical debt in very old codebases (NationStates) — **Strong evidence (creator's statement), Confirmed[2022 + 2026 Wikipedia assertion]**

- NationStates' creator described its 2002-era technology as slow, insecure, missing features, and difficult to replace without losing accumulated fixes ([Max Barry, 2022-11-12](https://maxbarry.com/2022/11/12/news.html)). Wikipedia's current article also records a temporary shutdown after a reported security incident in January 2026 (secondary; individual reporting sources not fetched here). Lesson: persistent games accumulate maintenance debt that *directly constrains* new features; a new project's newer stack (e.g., serverless) is a structural advantage *if* it's built to not become the legacy of tomorrow.

### 4.14 Hypotheses explicitly NOT supported in this pass

No suitable evidence was found in readable sources to support, on a genre-wide basis: **moderation burnout** as a game-killing cause; **veteran hoarding** as a widespread genre disease; **upkeep spirals** as an established player complaint; **alliance application walls** as a confirmed cross-game anti-pattern (the P&W proposals *about routing new players to alliances* are real, and the debate itself is the evidence); **Discord fragmentation** as a churn cause; and Sim Companies **botting** as a documented problem. These are recorded as hypotheses for later verification, not findings.

---

## Section 5 — Player frustrations and unmet needs

Organized by player type. Each entry: the frustration, its evidence (source, date, corroboration), and classification (**direct complaint** / **corroborated pattern** / **researcher interpretation** / **hypothesis for our game**).

### New-player experience

- **"Hard to start / confusing start."** Direct complaint (P&W App Store 2023-01-28: difficulty starting a nation successfully, complex and hard to play; corroborated structurally by Sim Companies 2023-08-27 and Prosperous Universe 2020 forum posts about costly early mistakes). Supported pattern: dedicated GUI guides and community glossaries exist for nearly every game in the genre, which is strong indirect evidence the first weeks are not self-explanatory.
- **"Advice is behind cliques."** Direct complaint (P&W 2020 forum proposal: getting sound advice requires already knowing players). Corroborated in PU (2020 forum mutual instruction, helpful but community-dependent) and Earth Empires (2017 dead guides).
- **"Irreversible early mistakes."** Corroborated pattern in PU (2020: costly early mistakes) and P&W (2025 single review requesting a restart after being killed). Researcher interpretation: in persistent worlds, "no undo" is a design choice that needs a designed mitigation (protection windows, graceful on-ramps).
- **"No clear early objectives"** — Supported in P&W (tutorial changes proposal 2021: many nations created then not revisited) as *community observation of churn*, indirect. Hypothesis for our game: needs testing with an actual player base.

### Returning-player experience

- **"Decline and decay of my community while away."** Direct complaint (eRepublik 2022 returning-player essay + commenters; 2025 returning-player critique of modules but praise for Discord people). Corroborated by 2024 demographics article's long-decline argument (player-authored). Re-entry experience is genre-green — no studied game has a returned-player flow beyond "read the news since you left".
- **"What changed while I was gone?"** — Researcher interpretation, backed only by P&W's long news feed and eRepublik's summary-notification approaches. No strong complaint evidence either way; a design-space observation for our game.

### Casual-player experience

- **"Waiting feels like nothing to do."** Direct complaint (Sim Companies 2023-11-11 quit review; PU 2022-06-08 negative). Corroborated pattern: the same claim appears for both games, independently, while other reviews of the same systems are positive. Not universal — pace preference is real.
- **"Coordination demands exceed attention budgets."** Researcher interpretation of P&W's automation debate (2022, 103 replies) and alliance-supply conventions. The games do not demand being online at fixed times (except event war windows in eRep-class games); the demands are bookkeeping and coordination overhead instead.

### Competitive-player experience

- **"Old whales dominate and buying in is the shortcut."** Direct complaint field (eRepublik 2018 article and comments; 2023 guide's structural corroboration). Moderately corroborated in Sim Companies (2023-12-06 veteran market power review; 2024-04-25 boosts complaint). Evidence strong in aggregate, each source individually limited.
- **"War's not meaningful for the small."** Corroborated pattern-level discussion inside P&W's 2024 core-thread; directly stated war-outcome complaints could not be verified as widespread. Labeled: corroborated *discussion*, not corroborated *prevalence*.
- **"Protection mechanics can be gamed."** Direct complaint-adjacent (P&W 2022 beige-change proposal). Researcher interpretation: anti-grief tools need adversarial review.

### Economic-player experience

- **"Market incumbents own niches."** Corroborated pattern (Sim Companies 2023 review; 2019 mine-upgrade thread as second data point). Hypothesis about eRepublik-level market manipulation: not verified this pass beyond the 2023 economy-analysis article's claim that many company types are unprofitable (player-authored).
- **"Repetitive optimization replaces interesting economic choices after a while."** Researcher interpretation from P&W's "tweaking numbers" essay (which frames it positively) + P&W "Boring game" thread (which shows the enervation when the social layer is thin). Neither alone is a complaint about the economy per se; the pattern is a risk signal for our design.

### Diplomatic/alliance-player experience

- **"Alliance running is unpaid admin work."** Corroborated pattern (P&W 2022 automation debate; P&W 2021/2022 proposals about alliance routing; Earth Empires 2017 dependence on alliance access to strategy knowledge). Direct complaint: none cleanly worded; the pattern is what matters.
- **"Forced/alliance-first funnels are contested."** Direct proposals (P&W 2021 "Tutorial Changes and New Player changes", 2022 "Railroad New Players into joining established alliances") show both: that the *community* sees alliance routing as a retention fix, and that it's controversial as a forced funnel. The debate itself is the finding.

### Military-player experience

- **"Politics is under-symbolized compared to war."** Direct complaint (P&W 2025-01-02 thread). Single-source at present, but it matches the game's own reputation and design history — labeled weak-to-moderate.
- **"War interaction granularity is opaque; outcomes need community math."** Indirect (P&W's large tutorial section on infrastructure damage/airstrike formulas; the *existence* of community formula docs is evidence that the in-game explanation is insufficient, though no direct complaint was verifiable this pass).

---

## Section 6 — Underlying causes and design trade-offs

These are the *systemic* reasons the problems above keep recurring. Each is framed as: system → intended benefit → unintended consequence → who is affected → when the trade-off flips.

1. **Sandbox + community as the fun engine** (P&W, NationStates, Cantr, eRep). *Benefit:* infinite player-authored content, high loyalty. *Consequence:* empty-state boredom, reliance on community know-how, moderation workload, vulnerability to community decline. *Flip:* unacceptable when the game expects to be fun for a *small* community without scaffolding; acceptable when player-generated activity is actively cultivated (whole-game social layer).
2. **Long-horizon progression / compounding accounts** (P&W cities, eRep strength, SC capital). *Benefit:* commitment is rewarded; a reason to stay and care. *Consequence:* newcomer catch-up frustration, "old money" resentment, delayed gratification for new players. *Flip:* becomes a defect when the first-week experience yields no agency at all (eRep complaint), versus being an ordinary strategy-game reality when early weeks still have meaningful choices.
3. **Slow/real-time cadence** (CN daily; PU real-time; SC check-ins). *Benefit:* low time pressure, fits adult schedules, drops busy-session exclusivity. *Consequence:* waiting perception, delayed gratification, "nothing to do between sessions" boredom, and the exploit surface that automation promises to solve. *Flip:* fine when each session yields *visible* progress; damaging when progress is measured in days not actions.
4. **Player-run markets and industries** (all studied games). *Benefit:* emergent economy, real interdependence, specialization. *Consequence:* incumbent ownership of niches, thin-margin traps for new players, and possible monotony of optimal play. *Flip:* acceptable when the market has accessibility channels and visible price transparency; harmful when the only way to learn is to burn capital on a bad first month.
5. **Protection/anti-grief mechanics** (vacation modes, beige, score bands, peace modes). *Benefit:* mercy for small/new players, an exit from war. *Consequence:* gaming the system (beige expiration engineering, "shield camping"), resentment from attackers. *Flip:* acceptable when an exploit-spree produces a patch loop (P&W debates show the community watches this closely); damaging if unmonitored.
6. **Complexity-as-depth** (PU command UI, eRep multi-module economy, P&W formula-heavy combat). *Benefit:* high skill ceiling, long mastery curve. *Consequence:* outsourced learning (wikis, forums, Discord), first-week bailouts, community inequality of expertise. *Flip:* the more the game's *rule surface* is hidden from UI, the worse this becomes — the problem is not depth itself but opacity of presentation.
7. **Alliance-first social design** (every studied game, but with different tooling). *Benefit:* retention at scale, coordinated war. *Consequence:* unallied players have little content; alliance leadership becomes unpaid labor; recruitment becomes spammy in small worlds. *Flip:* clear if the game ensures solo/small-group play is viable and alliance bureaucracy is minimized.
8. **Legacy software** (NationStates 2002 stack). *Benefit:* stability-by-stability, community trust. *Consequence:* every change is expensive; security risk grows; modern features arrive late. *Flip:* irrelevant if a project starts on modern infra and mitigates its own future debt by keeping dependencies lean and data models upgradeable.

**Interaction causes (multiple systems meeting in one failure):** the newcomer funnel failure in this genre is *not one bug*: it requires low-visibility rules (jargon), slow first progress (cadence * progression economy), expert-help living off-game (community structure), and no designed first-week protection (war rules) all at once. Designing a fix for only one of the four unlikely solves the funnel; a full onboarding *system* must address them jointly.

---

## Section 7 — Cross-game comparison

Evidence-quality labels: **S** = Strong; **M** = Moderate; **W** = Weak. A dash (—) means the report does not have usable evidence in that column for that game.

| Game | Principal supported strengths | Principal supported weaknesses / complaints | Principal unmet needs | Evidence quality basis |
|---|---|---|---|---|
| **Politics & War** | Social sandbox/alliance community (M); measurable progression/optimization (M); wars as shared narrative (M) | Jargon burden + advice behind contacts (M, 2020 thread); UI dated (M, 2021 reviews + 2025 proposal); new/small-nation disadvantage debate (M, 2024); war-centric activity balance (W, single); beige exploitable (M, single discussion); admin-workload automation debates (M, 2022) | Clear early objectives; more political gameplay; better in-game explanations of combat math; UI modernization | Forum threads at multiple dates + App Store reviews + official wiki; Reddit inaccessible |
| **NationStates** | Flexibility of commitment (S); community-created depth (S); WA political drama (M) | Core-vs-community complexity gap for newcomers (M); documentation/moderation disputes unverifiable (—); 2002-era stack technical debt (S, creator statement) + 2026 shutdown assertion (M, secondary) | In-game explanations of regional political rules; reliable infrastructure | Wikipedia + SUPERJUMP + creator essay + WikiStates; official forum blocked; Reddit inaccessible |
| **Cyber Nations** | Social/alliance strategy as the reward (M, PopMatters 2007); deliberate slow daily loop (Documented) | None robustly documented from readable sources (community-size claims unverified); inactivity deletion rule documented (official FAQ) | — (current-day complaint evidence insufficient) | PopMatters (historical) + official rules; current-day player sentiment not accessible |
| **eRepublik** | Politics-and-community as the attraction (M); playing roles with real power (Documented) | P2W/power gap from old accounts (M–S); daily chore loop (M); interface steepness (M, guides' existence); war-module change whiplash (M, historical); community decline reports (M, player-authored); unprofitable industries critique (M, player-authored) | New-citizen power parity; reduced daily chore pressure; honest economy profitability information | In-game player articles 2012–2025 + official wiki (partially outdated) |
| **Sim Companies** | Business variety/supply-chain fun (S, Steam); light check-in structure appeal (M) | Onboarding/UI confusion (M); market incumbency hurt newcomers (M); paid boosts fairness complaint (W, single); early wait gate quits (M single); late-game goals request (W, single) | Better first-hour clarity; greater economic long-tail goals; veteran-transition protections | Steam + Google Play reviews (several dates); official in-app pages not crawled |
| **Prosperous Universe** | Logistics/planning depth (S, Steam + handbook); helpful community (M) | Steep command UI and wiki dependence (M); slow pace polarizing (M, both directions); PRO-gated mid/late-game features (M); thin-market/population complaints (M, player reports) | First-week profitability guidance; UI learnability; paid-tier value story | Steam reviews + official forum + handbook |
| **eDominations / Earth Empires / Utopia / Cantr** | (Earth Empires) multiple server formats Documented; (Cantr) explicit first-day risk documentation (M); (Utopia) age-reset structure Documented | (EE) guide/story documentation gaps 2017 (M); (Cantr) first-day harsh, unforgiving (M, wiki) | — | Small evidence set; no widespread complaint corroboration |

The table deliberately rewards the games with richer public feedback traces (P&W, eRep, SC, PU, NS) and does not treat absence of complaint as absence of problems.

---

## Section 8 — Improvement opportunities for our game

Opportunities listed here are **evidence-backed option space**, not decisions. Each notes: addressed finding(s), who benefits, trade-offs, platform/turn fit, and what must be designed later. Findings referenced by ID appear in Section 9.

**O-1. In-context teaching layer.** The genre pushes learning off-game (F-010, F-027). Our game could surface rule explanations, price/cost transparency, and progress projections *in the interface* (e.g., an always-available "how was this number computed" drill-down), reducing wiki dependence. Every studied game demonstrates demand; benefit to newcomers and veterans alike; trade-off is UI complexity and content upkeep. Browser/format fit: excellent, zero conflict with turn cadence. To design later: which concepts earn inline explanation first.

**O-2. Transparent turn reports.** F-010 and F-014 show communities write their own math docs when games don't show their math. A turn-outcome report ("what changed and why, per city and per relationship") would directly answer new-player confusion and returning-player disorientation. Trade-off: reveals balance internals, narrowing niche expert advantage; fits browser UI and 2-hour reports naturally. To design later: report granularity, interpretations, and updates frequency.

**O-3. First-week safety net + optional repositories.** F-012, F-026 and F-011 imply the first weeks must be agency-rich and low-risk. A starter sequence (a few clearly stated goals) plus an explicit protection window (equivalent to P&W's vacation-mode / CN peace-mode precedent, in a mapless setting) is strongly precedented. Trade-off: protection tools invite exploit (F-017 beige evidence); must be adversarially designed. Fits the 2-hour turn structure directly. To design later: exact protection rules, expiry, and how networks handle a "protected but raid-able" world.

**O-4. Shorter-loop visible progress.** F-021 (waiting complaints) and F-006 (both subs) suggest that each 2-hour turn should make progress visible in a small session (5–10 minutes) without making daily chores compulsory (F-019 eRep warnings). Browser + 2-hour turn structure is ideal; the risk is that "visible progress every turn" actually drives compulsion — a deliberate design problem, not automatic.

**O-5. Honest economics transparency.** F-022 (eRep unprofitable industries; SC mine traps) shows opaque profitability is a costly trap for latecomers. Our market could show realized per-unit margin history and production cost hints, letting players audit before committing. Trade-off: reduces the "figure it out yourself" fun some veterans enjoy; significant UI data-visualization work; no conflict with free hosting if done as static pages computed at turns.

**O-6. Alliance tooling that lowers the admin cost, not the social ink.** F-018 shows alliance admin work is a genuine burden (P&W's 103-reply debate) whereas community is the genre's fun core. Our in-game alliance features (shared ledgers, bulk member actions, member-onboarding checklists) should reduce bookkeeping while keeping coordination decisions human. Anti-bot rules must be explicit and mechanical (P&W's official rules ban automated trading) — offering *official* bulk actions is the genre's cleanest answer to its own automation disputes. Trade-off: building good tools is work; poorly scoped tools can trivialize strategy. To design later: which actions are legitimate bulk actions.

**O-7. Adversarially-designed protection and absence systems.** F-017 (beige engineering) shows protection states get exploited; F-014 (vacation/peace modes across games) shows their necessity. Our equivalent must be designed with specific exploit scenarios enumerated (e.g., "protection fishing", "refusing to engage to farm", "shield-camping stalemates"). This is a design-analysis task for later stages, not a mechanic choice to be made now.

**O-8. Late-entry answer.** F-012 is the strongest cross-game frustration family. For mapless diplomacy-first design, the honest options (future stage) include faster catch-up mechanics that trade something for veterans, structural niches where a small nation's position matters more than size, or a *soft-staggered* world (new "generations" of nations entering without reset). Any choice reshapes the core loop; note explicitly: **this decision changes our core game design and must be reviewed as such later**, not decided from this report.

**O-9. Politics gameplay with real consequences ≠ war game with a politics label.** F-015 (P&W "it's centrally war") and the genre's strongest praise evidence for community-generated politics (F-005) suggest a real market gap: mechanically consequential domestic/diplomatic politics that don't require eRepublik-scale election/complexity overhead. Fits the project's stated intent to include domestic politics. Trade-off: every political mechanic we add multiplies rule surface; a lighter-touch version could meaningfully differentiate without dominating scope. Worst risk: adding politics that *doesn't matter*, which is the current P&W complaint.

**O-10. Documentation as a product surface, not a remainder.** F-027 (dead Earth Empires guides; outdated eRep wiki; P&W glossary necessity) suggests committing to *maintained, in-game documentation* as part of v1 scope, not an afterthought. Minimal cost; maximal fit to the browser medium; ongoing content-operations responsibility.

**O-11. Reduced monetization-risk posture.** F-020 shows three distinct monetization friction modes (eRep direct gold purchase power gap; SC boost complaints; PU subscription value-question). Our free-first project has no obligation to monetize players at launch; the design opportunity is to avoid the genre's two documented negative modes (selling power; gating late-game social features behind payment) entirely. Monetization strategy is out of scope for this report beyond noting the evidence.

**O-12. A "what changed while I was away" re-entry flow.** F-023 shows returning players face both world decay and a blank cognitive state. A summary-of-events-since-last-session surface is low-cost, browser-native, and turn-cadence-native, and addresses both returning and absent players. To design later: report depth, retention policy of news items, notification policy.

---

## Section 9 — Prioritized findings register

IDs are stable across the project; subsequent stages should reference them (e.g., "see F-012"). Evidence labels: **Strong** / **Moderate** / **Weak** per the Section-11 task definitions. Priority tiers are qualitative: **Core** (reshapes core design), **High** (shaping major systems), **Medium** (important UX/scope), **Low** (polish/future).

| ID Finding | Finding (paraphrase) | Type | Evidence | Games | Player groups | Impact if valid | Project relevance | Design opportunity | Risk/complexity | Open questions |
|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | Community/alliance social layer is the genre's core attraction | Strength | Strong-mod (multiple sources, several games) | P&W, NS, CN, eRep, PU | All; social players | Core to retention | Core — our game must be a place groups can grow | F scaffolding (O-6) | Community ops, not UI | How big must the world be to self-sustain? |
| F-010 | Learning curve/jargon burden is genre-wide and community-outsourced | Weakness | Strong (glossaries + 2020 P&W thread + guides across games) | all | New/returning players | Retention damage | Core (browser, no manual) | O-1, O-2, O-10 | Moderate (UI+content work) | Which in-game explanations matter most? |
| F-012 | Veteran/newcomer power gap + insufficient catch-up | Weakness/frustration | Strong-mod (eRep M-S; SC M; P&W M) | eRep, SC, P&W | New players, esp. mid-layer | New-entrant churn | Core — mapless design forces an explicit answer | O-8 | High (design-risky) | Which catch-up philosophy fits a 2h-turn world? |
| F-002 | Measurable optimization/progression is intrinsically rewarding | Strength | Mod (P&W blog + wiki) | P&W | Strategy/optimizer players | Long-term goal supply | High | (Design space) | Low | How much visible math? |
| F-003 | Wars supply shared drama/history | Strength | Mod (official + community essays) | P&W, eRep | Social/strategist players | Narrative value | High | (Design space) | Low | Clear, transparent war outcomes later |
| F-004 | Commitment-flexibility (casual↔deep) is a proven design | Strength | Strong (NS accounts, multiple) | NS; partially all | Casual and deep players | Broadens audience | High | (Session ambiguity design) | Low | Does our 2h turn support both? |
| F-005 | Community-created depth (roleplay, institutions) is the longevity engine | Strength | Strong (NS creator essay + retrospectives; Cantr) | NS, Cantr, CN | Roleplay/social | Participation supply | High | (Scaffold, don't script) | Low | Roleplay support mechanics? |
| F-011 | First-week friction is a multi-cause system problem | Weakness | Strong (multi-game evidence) | all | New players | Churn | Core | O-3, O-1, O-4 | High | What's our protection philosophy? |
| F-006 | Slow pace: lowest-commitment appeal for some, quit-driver for others | Trade-off weakness+strength | Mod (SC + PU, both directions) | SC, PU | Both casual & busy committed | Session design | High | O-4 | Medium | How often must progress be visible? |
| F-019 | Daily chore loop perception (eRep) / manual repetition | Weakness/Trade-off | Mod (guides; routine documented) | eRep, P&W automation debate | Working adults | Frustration, automation temptation | High | O-6 | Medium | Which chores are design-worthy vs noise? |
| F-020 | Monetization friction (power sales, boosts, subscription gates) | Weakness/Trade-off | Mod (eRep 2018; SC 2024; PU 2022/23) | eRep, SC, PU | All paying-averse players | Fairness concerns | High (for a free-first project) | O-11 | Low if avoided | None urgent |
| F-021 | Waiting/nothing-to-do complaints | Weakness/Trade-off | Mod (SC + PU reviews, both sides) | SC, PU | Impatient players; busy players | Early churn | Medium | O-4 | Medium | What does a 5–10 min session deliver? |
| F-014 | UI/UX complaints; dated interface | Weakness | Mod (P&W 2021 + 2025; SC 2023; PU 2023) | P&W, SC, PU | All | Frustration | Medium | (Our new UI; budget for data tables) | Medium | None urgent |
| F-018 | Alliance admin workload & automation debate | Tactical/organizational pain | Mod (P&W 2022, 103 replies) | P&W; constellation in others | Alliance leaders | Leader burnout | High (affects retention) | O-6 | Medium | Which bulk actions stay legitimate? |
| F-017 | Protection mechanics exploitable (beige engineering) | Weakness/Trade-off | Mod (P&W 2022 thread) | P&W | All competitive players | Fairness friction | Medium-High | O-7 | Medium | How does our absence/protection design resist farming? |
| F-015 | "It's centrally war; politics is thin" | Weakness/game-direction complaint | Weak-mod (single thread, 2025) | P&W | Peace-economy players | Niche addressed | High — matches our political-integration intent | O-9 | Medium-High | How much politics in v1? |
| F-022 | Market incumbency; opaque profitability traps | Weakness/frustration | Mod (SC 2023 review + 2019 forum; eRep 2023 economy article) | SC, eRep | Aspiring traders/producers | Economic churn | High | O-5 | Medium | Which transparency is fair? |
| F-023 | Community decline + re-entrant discouragement | Weakness | Mod (player-authored; multi-source in eRep) | eRep (+generic) | Returning players | Re-entry churn | Medium | O-12 | Low-Medium | News retention policy |
| F-027 | Documentation decay (dead guides, outdated wikis) | Weakness/context | Mod (EE 2017; eRep wiki self-marking; SC app pages) | EE, eRep, SC | New players | Knowledge inequality | Medium | O-10 | Low | Which docs are we committing to maintain? |
| F-009 | The 2h turn cadence itself is documented but not evidenced as loved | Proxy/uncertainty | Weak (absence of praise evidence) | P&W | n/a | Uncertainty, not finding | Informational | — | — | Is there current-turn-cadence love anywhere? |
| F-013 | Alliance-routing/funneling is debated as retention fix and as autonomy loss | Trade-off | Mod (P&W 2021+2022 proposals + 2020 thread) | P&W | New players; alliance recruiters | Recruitment ethics | Medium | O-3/O-6 refinement | Medium | Should our game auto-openlines or leave social free? |
| F-024 | Technical debt constrains the longest-running games | Weakness (engineering) | Strong (creator statement + 2026 shutdown report, secondary) | NS (primary); general | All players | Feature velocity | Informational — supports our modern-stack choice | — | — (architecture stage) | How to avoid building tomorrow's debt |
| F-016 | War-system design debates affect new/smaller nations | Weakness/Trade-off | Mod (P&W 2024 61-reply thread) | P&W | New/small entities | Fairness concerns | Medium-High | (feeds O-7/O-8) | Medium | What's our small-nation safety plan? |
| F-008 | Welcoming community aids onboarding (PU evidence) | Strength signal | Mod (PU forum/2026 review) | PU | New players | Onboarding success | Medium | (Community ops) | Low | How to seed welcoming culture |
| F-025 | Late-game goal scarcity (single request) | Weakness/Feature gap | Weak (single 2024 review) | SC | Veteran players | Veteran churn | Low for v1 | (Post-v1 roadmap) | Low | n/a |
| F-026 | No restart / first-failure punishment | Weakness/Feature gap | Weak (single 2025 review) | P&W | New players | Early churn | Medium | (Feeds O-3) | Low | Is destroy-and-restart even a path we allow? |
| F-003b | "Boring when the community is quiet" | Weakness/Trade-off (flip of F-001) | Weak-mod (single 2019 thread; corroborated conceptually) | P&W | Low-activity periods | Motivation collapse | Medium | (Live-ops plan later) | Medium | What's our "empty world" plan for launch? |
| F-029 | Moderation burnout / veteran hoarding / upkeep spiral / application walls / botting: hypotheses NOT corroborated this pass | Hypotheses (explicitly unverified) | — (no suitable readable evidence) | genre | n/a | Unknown | Unknown | (Watchlist for Stage 2+) | — | Add per-game verification when access improves |

**Register range and numbering (declared 2026-10-23).** This register defines **28 entries**. The continuous range used by later reports — "F-001…F-029" — is correct as a *range*: **F-007 and F-028 are unassigned** (never issued; no finding was withdrawn or merged into them), and **F-003b** is a deliberate sub-ID of F-003 (the "boring when the community is quiet" flip side), not a renumbering. Nothing is renumbered by this note and no identifier changes meaning. Any future finding must take F-030 or later; the gap numbers stay unassigned. *(Added by the Prompt 9 correction pass to close DEF-008.)*

Notes on evidence quality:
- **Strong** claims rest on ≥2 independent corroborating sources across at least two games or one game with both official and independent confirmation.
- **Moderate** claims have credible support but limited independence (often one discussion thread plus reasonable structural evidence).
- **Weak** claims are single journalist/review observations or untested interpretations, included deliberately as signals, never as confirmed problems.

Priority rationale (qualitative): Core finds the ones that reshaping core design (onboarding system, newcomer parity, community scaffolding, transparent rules). High finds systems design inputs (protection/anti-grief, alliance tooling, visible progress, market transparency). Medium finds UX and content-ops items. Low items are noted but should not drive v1 scope.

---

## Section 10 — Research gaps

1. **Reddit content access.** All platforms' Reddit could not be read this pass. This is where contemporary complaints most likely appear (especially current-era P&W, Sim Companies, Prosperous Universe); a future pass with working Reddit access should re-test the F-015/F-017/F-021/F-022/F-029 families.
2. **Discord/Telegram.** Not researchable without accounts; a large unseen layer of these communities.
3. **Quantitative prevalence.** No claim in this report should be read as measuring how many players hold any view; store-review and forum-post prevalence is structurally unknowable from the sources used.
4. **Current-era complaint sourcing for P&W after 2022** — the most recent usable thread in the readable-sources set is 2025; a proper study should check whether beige/vacation/UI complaints persist.
5. **Uncorroborated topics on our watchlist:** moderation-burnout, veteran hoarding, botting, upkeep spirals, alliance application walls, "toxicity", inactivity-migration to Discord — all need per-game verification before they can drive any design choice.
6. **No live player interviews or prototype testing** have occurred; our own game's funnel can only be validated by later-stage testing.
7. **Praise evidence for turn cadence** in all games remains unestablished — a genuine research gap since our project's identity leans on it (F-009).

---

## Section 11 — Source register

All sources accessed 2026-10-22 unless a date is given by the source itself. **[O]** official, **[C]** community/player-generated, **[3]** independent third-party.

### Politics & War
| # | Source | Type / date | Supports |
|---|---|---|---|
| P1 | [P&W homepage](https://politicsandwar.com/) | [O], undated | Community role, alliance ecosystems, market/player-driven economy positioning |
| P2 | [P&W-pedia — Terminology and Glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary) | [O], live | Jargon burden evidence (official acknowledgment); beige definition |
| P3 | [Apple App Store review page](https://apps.apple.com/au/app/1552461332?see-all=reviews&platform=iphone) | [C], 2021–2025 reviews | Complexity complaint (2023-01-28); trade-table scroll (2021-02-22); UI layout (2021-08-06); restart request (2025-06-23) |
| P4 | [Google Play listing](https://play.google.com/store/apps/details?id=com.game.politicsandwar&hl=en_US) | [O listing + C reviews], 2025-10-13 | 4.2/~3,900 rating; community-as-fun review; slow-early-building complaint |
| P5 | ["The Problem at the Core of PnW"](https://forum.politicsandwar.com/index.php?/topic/40471-the-problem-at-the-core-of-pnw/) | [C], 2024-05-13, 61 replies | New/small-nation disadvantage discussion; core-design critique surface |
| P6 | ["The game name is politics and war but it is centrally around war"](https://forum.politicsandwar.com/index.php?/topic/48019-the-game-name-is-politics-and-war-but-it-is-centrally-around-war/) | [C], 2025-01-02 | War-dominance complaint (single) |
| P7 | ["War Changes"](https://forum.politicsandwar.com/index.php?/topic/48364-war-changes/) | [C], 2025-01-22 | Readiness-requirement concern (single suggestion) |
| P8 | ["Proposed Beige Change"](https://forum.politicsandwar.com/index.php?/topic/32903-proposed-beige-change/) | [C], 2022-03-15 | Beige strategic exploitation discussion |
| P9 | ["My thoughts on bots and a plea to blanket ban..." ](https://forum.politicsandwar.com/index.php?/topic/32750-...) | [C], 2022-02-10, 103 replies | Automation/workload debate; alliance-management burden |
| P10 | ["Alliance Creation Restrictions"](https://forum.politicsandwar.com/index.php?/topic/29803-alliance-creation-restrictions/) | [C], 2020-09-02 | Learning curve, advice-social barriers, retention link |
| P11 | ["Tutorial Changes and New Player changes"](https://forum.politicsandwar.com/index.php?/topic/30794-tutorial-changes-and-new-player-changes/) | [C], 2021-02-24 | New-player funnel proposals; "created but not revisited" observation |
| P12 | ["Railroad New Players into joining established alliances"](https://forum.politicsandwar.com/index.php?/topic/32822-railroad-new-players-into-joining-established-alliances/) | [C], 2022-02-25 | Funneling proposal + controversy |
| P13 | ["Modern UI / PnW Refresh"](https://forum.politicsandwar.com/index.php?/topic/52736-modern-ui-pnw-refresh/) | [C], 2025-07-24 | UI-refresh demand (proposal) |
| P14 | ["Boring game."](https://forum.politicsandwar.com/index.php?/topic/25296-boring-game/) | [C], 2019-04-13 | Community-dependence counterpoint |
| P15 | [Politics & War Vs. NationStates (forum blog)](https://forum.politicsandwar.com/index.php?/blogs/entry/54-politics-war-vs-nationstates/) | [C], undated | "Tweaking numbers to perfection" player essay; wars/social recognition |
| P16 | [IndieDB review by Dubayoo](https://www.indiedb.com/games/politics-and-war/reviews/709978) | [3], 2019-07-01 | Negative review: newcomer disadvantage/toxicity (single) |
| P17 | [P&W forum — Tutorials & Knowledge index](https://forum.politicsandwar.com/index.php?/forum/34-tutorials-knowledge/) | [O forum], incl. 2024 guides | Community-maintained formula/strategy docs (indirect UI-explanation gap) |
| P18 | [City building from 0 to 1000 (Fandom)](https://politicsandwar.fandom.com/wiki/City_building_from_0_to_1000) | [C], undated | Progression path shape |

### NationStates
| # | Source | Type / date | Supports |
|---|---|---|---|
| N1 | [NationStates — Wikipedia](https://en.wikipedia.org/wiki/NationStates) | [3], current | Core design, 2026 security-incident shutdown assertion, multi-nation rule (unverified details) |
| N2 | [Max Barry — "NationStates Turns Twenty"](https://maxbarry.com/2022/11/12/news.html) | [3/creator], 2022-11-12 | Community-as-value moderation necessity; tech-debt statement |
| N3 | [SUPERJUMP — "NationStates and the Age of Browser-Based Games"](https://www.superjumpmagazine.com/nationstates-browser-based-games/) | [3], 2023-03-07 | Casual/deep play patterns; roleplay extension |
| N4 | [Other Strangeness — "The Web Game I've Been Playing Daily..." ](https://www.otherstrangeness.com/2023/01/18/the-web-game-ive-been-playing-daily-for-almost-two-decades/) | [3], 2023-01-18 | Low-commitment loop viability |
| N5 | [TV Tropes — NationStates(Website)](https://tvtropes.org/pmwiki/pmwiki.php/Website/NationStates) | [3], undated | Play-style taxonomy |
| N6 | [WikiStates — World Assembly](https://nationstates.fandom.com/wiki/World_Assembly), [Regional Influence](https://nationstates.fandom.com/wiki/Regional_Influence) | [C], undated | WA/delegate/influence complexity |
| N7 | [Community glossary (2012)](https://www.tapatalk.com/groups/kantrias/glossary-of-nationstates-terms-and-acronyms-t26.html) | [C], 2012-10-27 | Jargon-burden corroboration |
| — | NationStates official pages | 403 — not accessed | Official claims remain unverified this pass |

### Cyber Nations
| # | Source | Type / date | Supports |
|---|---|---|---|
| C1 | [PopMatters — Cyber Nations review](https://www.popmatters.com/cyber-nations-2496238708.html) | [3], 2007-09-19 | Social/alliance strategy praise, once-daily cadence framing (historical) |
| C2 | [Community FAQ](https://cybernations.fandom.com/wiki/Frequently_Asked_Questions_about_Cyber_Nations) | [C], undated | 25-day inactivity deletion, daily update time (community-sourced), peace-mode advice |
| C3 | [Official update log](https://www.cybernations.net/game_update_log.asp) | [O], 2025-04-04 | Mobile-view update (interface refresh evidence, not complaint) |

### eRepublik
| # | Source | Type / date | Supports |
|---|---|---|---|
| E1 | ["Is Erepublik fair for new players?…"](https://www.erepublik.com/en/article/2676982) | [C], 2018-08-04 | P2W/newcomer power-gap complaint + comments |
| E2 | ["New Player's Guide to the Military Module"](https://www.erepublik.com/en/article/2770076) | [C], 2023-06-11 | Strength-gap caution; do-not-buy-energy guidance |
| E3 | ["Guide to Erepublik"](https://www.erepublik.com/en/article/2488034) | [C], 2015-01-16 | GUI explainer existence; daily routine documentation |
| E4 | ["A Beginners Guide to eRepublik"](https://www.erepublik.com/en/article/2702627) | [C], 2019-08-16 | Community as central attraction; orientation material |
| E5 | ["10 steps in eRepublik for new players"](https://www.erepublik.com/en/article/2145862) | [C], 2012-10-26 | Community praise (historical) |
| E6 | ["A quiet welcome to eRepublik"](https://www.erepublik.com/en/article/2749278) | [C], 2022-02-23 | Returnee decline experience + comments |
| E7 | ["eRepublik Demographics and Player Retention"](https://www.erepublik.com/en/article/2780184) | [C], 2024-06-14 | Player-authored decline analysis (mixed definitions acknowledged in article itself) |
| E8 | ["The Economist ~ What is wrong with eRepublik? (part 1)"](https://www.erepublik.com/en/article/2785300) | [C], 2025-01-14 | Modern critique: political module, military drift, module whiplash |
| E9 | ["Complete eRepublik Economy – Quo Vadis, Plato?"](https://www.erepublik.com/en/article/2772582) | [C], 2023-09-26 | Economy profitability critique (player analysis) |
| E10 | ["Future Changes in eRepublik"](https://www.erepublik.com/en/article/2288511) | [C], 2013-07-09 | War-module-change commentary (historical) |
| E11 | [Official wiki Tutorial (marked outdated)](https://wiki.erepublik.com/index.php/Tutorial) | [C], undated | Documentation-decay evidence |

### Sim Companies
| # | Source | Type / date | Supports |
|---|---|---|---|
| S1 | [Steam reviews page](https://steamcommunity.com/app/2253720/reviews/?browsefilter=toprated) | [C], 2023–2024 | Variety/supply-chain praise (2023-08-31); check-in positive (2024-05-26); veteran market power (2023-12-06); >1hr wait quit (2023-11-11); boosts complaint (2024-04-25); newcomer difficulty (2023-08-27 style) |
| S2 | [Google Play listing](https://play.google.com/store/apps/details?id=com.simcompanies.simcompaniespwa&hl=en_US) | [O + C reviews], 2023–2024 | Onboarding difficulty (2023-08-27); late-game goals request (2024-10-22); core-loop framing |
| S3 | [Sim Companies forum — Mine Upgrades](https://simcompanies.freeforums.net/thread/29/mine-upgrades) | [C], 2019-09-04 | Unprofitable-upgrade trap example (historical) |
| S4 | [Terms](https://www.simcompanies.com/terms/) | [O], 2026 | F2P + purchases status |

### Prosperous Universe
| # | Source | Type / date | Supports |
|---|---|---|---|
| PU1 | [Steam reviews page](https://steamcommunity.com/app/1761220/reviews/?browsefilter=toprated) | [C], 2022–2026 | Loop praise (2022-04-20); UI/wiki reliance (2023-10-04); PRO-value complaint (2022-06-08, 2023-10-04); slow-pace both ways (2022-06-08, 2022-04-20); community-welcoming/2026 review |
| PU2 | [New Player Feedback forum thread](https://com.prosperousuniverse.com/t/new-player-feedback/2068) | [C/O forum], 2020-03 | Costly early mistakes; tutorial/profitability tutorial requests; peer help |
| PU3 | ["Let's talk about the price of PRO"](https://com.prosperousuniverse.com/t/lets-talk-about-the-price-of-pro/3179) | [C/O forum], 2021-04-27 | PRO value vs small playerbase discussion |
| PU4 | [Handbook FAQ](https://handbook.apex.prosperousuniverse.com/wiki/faq/index.html) | [O], 2026 | Slow-paced positioning (official), non-recurring PRO, free-play constraints |
| PU5 | [PRO License page](https://prosperousuniverse.com/premium) · [Licenses tutorial](https://handbook.apex.prosperousuniverse.com/tutorials/current-tutorials/06-licenses/index.html) | [O], 2026 | PRO feature gating (Local Markets, contracts, corp founding) |

### Other games (brief-source items)
| # | Source | Type / date | Supports |
|---|---|---|---|
| O1 | [Cantr II wiki — Your First Cantr Day](https://wiki.cantr.net/index.php/Your_First_Cantr_Day) | [C], modified 2025-08-30 | Harsh/uneventful first days; no newcomer protection |
| O2 | [Earth Empires — "Public guides and turn for turn start-ups"](https://www.earthempires.com/forum/strategy-room/public-guides-and-turn-for-turn-startups-42844) | [O/C], 2017 | Dead public guides; alliance-held strategy knowledge |
| O3 | [Earth Empires homepage](https://www.earthempires.com/) | [O], fetched 2026-10-22 | Server-mode diversity; activity snapshot (no trend claim) |
| O4 | [Utopia Fandom — "Utopia Time"](https://utopiagame.fandom.com/wiki/Utopia_Time) | [C], fetched 2026-10-22 | Age-reset structure (no retention claim) |

*(Search-result snippets only — e.g., unopenable Reddit pages, App Store rate-limited pages, or the ModDB reviews page — were not used as evidence anywhere in this report.)*

---

## Section 12 — Handoff to Prompt 3

### What Prompt 3 receives

**Most important strengths (referencable by ID):**
- F-001 community/alliance social layer as the genre's core attraction (multiple games, tier-S/M).
- F-002 measurable optimization; F-003 war-as-drama; F-004 commitment-flexibility; F-005 community-created depth; F-006 pace polarization (both kinds of players valid); F-008 welcoming communities help onboarding.
- F-009 the 2-hour turn is *not itself* the value driver; what surrounds it must carry daily value.

**Most important weaknesses:**
- F-010 steep learning curve/jargon, community-outsourced knowledge.
- F-011 multi-cause first-week friction; F-012 veteran/newcomer power gap; F-014 UI/UX datedness; F-018 alliance admin burden + automation disputes; F-022 market incumbency/opaque profitability; F-024 legacy technical debt (validates our modern-stack plan); F-017 protection-mechanic exploitability.

**Most significant player frustrations:**
- New players: confusing start, advice behind social barriers, irreversible early mistakes, no restart on catastrophic loss.
- Casual players: waiting instead of playing; no-visible-progress loops.
- Competitive players: whale-dominated economies (eRep strongest); war unfairness debates; exploit-able protections.
- Alliance players: unpaid admin work; recruitment/funneling controversies.

**Most promising opportunities:** O-1 in-context teaching, O-2 transparent turn reports, O-3 first-week safety net, O-4 short-loop visible progress, O-5 honest economics transparency, O-6 alliance tools to reduce admin, O-7 adversarially-designed protection, O-8 late-entry answer (design-stage decision), O-9 politics that matters, O-10 documentation-as-product, O-11 avoid game's two documented monetization failure modes, O-12 re-entry summary flow.

**Most important trade-offs:**
- Community-dependence vs self-sufficiency at small scale (F-001 vs F-003b).
- Commitment-reward vs newcomer agency (F-012 context).
- Depth vs legibility (F-010 context).
- Protection vs exploitability (F-017 context).
- Legal automation vs manual grind (F-018 context).

**Strongest sources for Prompt 3's use:** P&W official glossary + forum threads (2020/2022/2024/2025); NationStates creator's 2022 essay; eRepublik 2018/2022/2023/2024/2025 player articles; Steam reviews for SC/PU (dated individually); PopMatters 2007 for CN's historical social-games framing; Max Barry's tech-debt statement.

**Unresolved questions priority order for the next stage:**
1. Reddit-era corroboration of F-015, F-017, F-021, F-022 (current-day complaint status).
2. Any evidence that per-session value in a 2-hour-turn world can also satisfy the "impatient" player type (O-4).
3. What level of rule-explanation tooling (O-1/O-2) is affordable to a small project.
4. Whether a war-protection design can be proven exploitable-free before implementation (O-7).
5. Which of F-029's watchlist hypotheses (moderation burnout, hoarding, spiral upkeep) genuinely recur (for eventual project risk planning).

### Implementation status notes

- **No code written** throughout this task; no game mechanics decided.
- **No continuity file conflicts introduced**; the continuity documents (AI_CONTEXT.md, AI_HANDOFF.md, PROJECT_PROGRESS.md, DECISIONS.md) were created this session and are authoritative going forward.

---

### Report status footer

- **Prompt 2 research completion status:** Complete within source-access constraints; no fabrication of player quotes, ratings, or population figures at any point.
- **Games investigated for player sentiment:** P&W (full two-track), NationStates, Cyber Nations, eRepublik, Sim Companies, Prosperous Universe, plus spotlight lookups for Cantr II, Earth Empires, Utopia, eDominations.
- **Important research limitations:** Reddit unreadable everywhere; store-platform cross-check limited by rate limits; Discord/Telegram layer invisible; prevalence of any attitude cannot be measured from these sources.
- **Unresolved questions:** Section 10.
- **Recommended next action:** Proceed to Prompt 3 only with explicit user authorization, carrying Section 12.
- **Document version:** 1.0. Prepared 2026-10-22.
