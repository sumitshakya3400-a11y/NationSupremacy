# STAGE 1 — COMPETITOR RESEARCH AND GENRE ANALYSIS

**Project:** Untitled browser-based persistent multiplayer nation-strategy game ("the project")
**Document:** `docs/stage-1/01_competitor_research.md`
**Version:** 1.0 — prepared 2026-10-22 (all web sources accessed 2026-10-22 unless noted)
**Status:** Complete for Prompt 1. Does not begin Prompt 2, the Game Design Bible, or any implementation.

---

## Section 1 — Executive summary

### The landscape

Persistent browser-based nation-strategy games form a small but durable genre with working precedents that are, in several cases, remarkably aligned with this project's constraints.

**The single most important validation finding:** Politics & War — the largest and most mechanically complete reference in this investigation — already uses a **2-hour turn (12 turns per day)** with server-side revenue/production calculation and player actions between turns ([P&W-pedia — Terminology and Glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary), accessed 2026-10-22). The project's proposed UTC-based 2-hour turn schedule is therefore an established, playable genre convention, not a novel experiment.

### Principal game types found

| Type | Examples | Core activity |
|---|---|---|
| **Nation-builder + player economy + abstract war** | Politics & War, Cyber Nations, eDominations | Build a nation's economy/infrastructure; trade; wage alliance-level abstract wars |
| **Policy/roleplay simulation** | NationStates, Cantr II | Answer issues / inhabit a persistent social world; diplomacy is social and roleplay-driven |
| **Geo-political MMO with a real-world map** | eRepublik, eDominations | Country-level politics, production, region-conquest wars |
| **Company/industry economy sim** | Prosperous Universe, Sim Companies | Production chains, market trading, contracts; no combat or abstract competition only |
| **Round-based text strategy / kingdom teamwork** | Earth Empires, Utopia | Server rounds or "ages"; coordinated kingdom/clan warfare |

### Key findings for the project

1. **The 2-hour turn is proven.** P&W runs income/production on a 2-hour cycle and survives operationally; the pattern "server calculates per turn, players act between turns" is the genre's idiom.
2. **Resource chains across player economies are the genre's economic engine.** P&W's 11-tradeable-resource system (7 raw, geographically restricted; 4 manufactured) exists specifically to force trade and interdependence. A mapless game must find its own substitute for "geographic scarcity" as the trade driver (see Section 7).
3. **Alliances are the real player organization layer.** In P&W, in-game alliance ranks, taxes, banks, and treaty types (MDP/MDoAP/ODA/NAP/PIAT, per the official glossary) coexist with off-game Discord coordination. A new game should treat alliance tooling as a first-class system, not a bolt-on.
4. **Abstract warfare is feasible and precedented.** P&W resolves wars between two nations via discrete mutual actions (ground/air/naval attacks, raid/attrition war types, looting, peace offers) with no meaningful battlefield map. This is the closest analogue to the project's "warfare without geographic fronts."
5. **Free-to-play with anti-P2W donation models precedes and works.** P&W states it is 100% free to play with a limited donation system "intended to prevent pay-to-win" ([Game Rules](https://politicsandwar.com/rules/)). Monetization that preserves fairness is a genre-informed decision, not a forced paid-product build.
6. **Free-tier infrastructure limits are a real constraint for tick-based games.** Cloudflare's D1 free tier is **100,000 rows written per day** (5M rows read/day, 5 GB storage), and since **September 1, 2026** failures to exceed limits cause queries to fail ([D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/); [D1 changelog 2026-09-01](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/)). A 12-turns/day simulation writing per-nation rows must be designed around this from day one (Section 6).
7. **Older genre games persist but shrink.** Cyber Nations (2006) still operates (official update log shows a mobile-friendly update dated April 4, 2025) but appears to be a much smaller community than its peak. Lesson: longevity requires low-friction onboarding and active live-ops; several once-major games (Cyber Nations, eRep-facing era) have become small.

### What this report does NOT do

It does not finalize mechanics, formulas, or resource values. It does not reproduce any single game. Section 7 connects findings to the project's constraints; Section 8 lists what remains uncertain.

---

## Section 2 — Research methodology

### Games investigated

Nine games were researched in depth, plus two noted as context:

- **Politics & War** — primary reference (two parallel research tracks: economy/nation-building; war/monetization/alliances).
- **NationStates**
- **Cyber Nations**
- **eRepublik**
- **Prosperous Universe**
- **Sim Companies**
- **eDominations** (discovered during research; valuable as an additional currently-operating nation MMO with politics)
- **Earth Empires**, **Cantr II**, **Utopia** (context/brief profiles; each contributes one or two design lessons)
- **Cold War 2** — investigated and set aside: available evidence did not establish the multiplayer nation-competition needed for the current comparison.

### Source priority used

1. Official game sites, official official-maintained wiki/pedia pages, official rules/FAQ/press/store listings.
2. Official changelogs and store listings for current-status evidence.
3. Community wikis where official documentation is thin (Fandom, simulation-specific handbooks) — **always labeled community-maintained**, never treated as proof of current official rules.
4. Credible third-party overview sources (Wikipedia for NationStates context) — labeled secondary.

### Verification and labeling conventions

- Every important claim is cited inline with source title + URL.
- **Access date:** all web access for this report was performed on **2026-10-22**, unless a specific dated claim (e.g., an official changelog entry with its own date) is called out separately.
- **Official-maintained vs community-maintained** is labeled where it matters.
- Where official sources were inaccessible (NationStates' own pages returned 403 to the reading tool), findings from that source are flagged as unverified rather than asserted.
- Recent-but-live community wikis could still be stale; where numbers look formula-specific (e.g., P&W's exact production or war math), they were read from community-maintained sources and labeled accordingly, since official P&W pages only describe formulas at the level of intent/strategy, not current values.
- No game was tested by the author; this is documentary research, and no personal accounts, dashes, or in-game screens were used.

### Research limitations

- **NationStates' official pages** consistently returned 403 to the fetch tool used; all NationStates mechanics come from a secondary overview plus a community wiki description, so all such claims are flagged as secondary/unverified.
- **Sim Companies' in-app guide pages** (FAQ, beginner guide, encyclopedia) rendered only app-loader shells; exact fees, tax rates, tick times, and worker/wage math could not be verified.
- **eRepublik's official wiki** is user-initiated and partially outdated (its own Tutorial page says so); specific current numbers are treated as historical.
- **Cyber Nations'** live rules details come partly from a community Fandom FAQ; its official index is accessible, but some details (inactivity deletion policy, exact daily update time, exact war-range rules) came from the community wiki.
- **Player counts, revenues, server costs, and hosting technologies of competitors** are not publicly documented and were not asserted.
- No competitor's architecture is publicly documented; hosting-related observations about competitors are therefore limited to what their own sites publicly state.

---

## Section 3 — Game-by-game research profiles

### 3.1 Overview table

| Game | General type | Core loop | Economic structure | Diplomacy & alliances | Warfare / competition | Time & progression model | Relevance to project | Research confidence |
|---|---|---|---|---|---|---|---|---|
| **Politics & War** | Persistent nation-builder with player economy, alliances, abstract war | Grow nation via cities/infrastructure; trade; wage alliance wars | 11 player-tradeable resources (7 raw/continent-locked, 4 manufactured), per-turn income/upkeep, city-cost progression, alliance taxes/banks | First-class: in-game alliances with ranks/treaty web; player-run off game | Abstract, non-geographic: mutual discrete attacks, raid/attrition wars, looting, peace offers, nukes | **2-hour turns (12/day)** + daily reset; offline progression | **Highest** | High for official-maintained wiki facts; medium for exact current formulas |
| **NationStates** | Policy/roleplay simulation + large community | Answer "Issues" that alter hidden national statistics; participate in regions and World Assembly | None mechanical (only economic statistics as flavor) | Social/diplomatic: regions, embassies, WA resolutions, endorsements | No mechanical war; "invasion/defence" is a regional-control subgame | Issue cadence configurable (~daily default); no economy-based progression | Moderate — contracted social/org layer only | Low–medium (official pages blocked; secondary sources) |
| **Cyber Nations** | Persistent text nation-builder, abstract war | Daily taxes/upkeep; choose govt/religion/currency; balance happiness | GNP via taxes on citizen income; trade circles to combine resources; improvements capped (5 of a type, 1 per 1,000 citizens); wonders (1 per 30 days, $5,000/day upkeep) | Alliances are explicitly player-run with **no hard-coded game benefits**; treaty types are community conventions | Simple abstract ground war (soldiers/tanks/CMs/nukes), limits like 2 attacks/day per front, nuke ≥24h after war declaration | **Daily update** (community-reported 6:00 GMT), taxes once/day, land grows 0.5 mi/day | Moderate — validates daily-update precedent, trade-circles idea | Medium (official index accessible; some details community wiki) |
| **eRepublik** | Geo-political MMO on real-world-derived map | Work/produce, fight in region battles, politicize in country structure | Companies producing intermediate goods; dual currency (gold + local); congress-voted taxes; player market | Country-level: president, congress, alliances/military units (player orgs) | Region-conquest wars with timed 90–120-minute battle rounds; Resource wars events; occupation/resistance | Real-time with signed events; continuous, not turn-based; ongoing operation still in 2025/2026 | Moderate as a cautionary/parallel example; teaches dual-currency, congress-driven taxes, event-war conventions | Medium (official wiki user-maintained and partially outdated) |
| **Prosperous Universe** | Economic MMO, no combat | Build bases, run production chains, trade on local commodity exchanges, contract-ship | Player-driven market via exchange-specific order books, custom contracts, logistics as gameplay | Corporations + political/governor roles; PRO-gated | No combat; competition is economic/political; "piracy" only via contract abuse | Real-time persistent; slow-paced; browser APEX client | High for market/trading design only | High (official site + handbook) |
| **Sim Companies** | Business/industry sim in shared economy | Build facilities, run production, wholesale/retail, contracts | Quality (Q0/Q1…) researched progression; player market and retail pricing trade-offs; logistics | Light — business partnerships/contracts; no formal alliances | Asymmetric-competitive (niche competition), not combat-based | Real-time asynchronous; check-in style | Medium — teaches quality/production progression and retail-vs-wholesale | Medium (official off-app pages not readable) |
| **eDominations** | Geo-political nation MMO (eRepublik-like, now operating) | Work/produce, fight daily national battles, vote in elections | Company production; trading center w/ taxes; gold cost for some actions (e.g., alliance creation) | Monthly presidential/congress elections; president has war/peace/embargo powers; alliance system w/ "campaign of the day" | 24-hour battles in 3×8-hour rounds; resistance wars | Persistent account progression + scheduled collective events (daily battles, monthly elections) | Useful wallpaper for connecting politics → economy → war | Medium (official wiki + game site; monetization unverified) |
| **Earth Empires** | Round-based text strategy (Succession-era style) | Grow a country, attack for land/resources | Investment/land/resource economy (detail not fully public) | Clans as the team unit | Server-mode-dependent attacks; anti-multi rules | **Round-based servers** with defined start/end; many formats (Alliance/Cooperation/Conquest/Classic/Express/FFA) | Low-moderate — teaches server-format diversity and anti-fairness rules | Medium (official homepage/rules only) |
| **Cantr II** | Persistent roleplay society simulation | Inhabit characters in a slow, player-written world | Emergent player-made production/exchange; no formal macro-economy | Player-created institutions, politics, religion | Roleplay aggression (limits on attack frequency documented as design) | Persistent, deliberately slow; multiple characters; 100% free | Low — mapped differently; shows how much organization can be player-authored | Medium (official homepage/rules; funding info 2013-dated) |
| **Utopia** | Kingdom-teamwork text strategy | Build/research, then strategic attacks/thieves/magic | Not verified in detail | Kingdoms as the organized team | Kingdom-scale PvP; complementary team roles | Persistent; historic "ages" (community-reported ~3 months) | Low-moderate — kingdom coordination analog for alliance play | Low–medium (official fetched pages limited) |

Comparison of tools: only **P&W and Cyber Nations** are turn/schedule-driven nation simulations (P&W 2h; CN daily). eRepublik and eDominations are event-driven. Prosperous Universe/Sim Companies are continuous but management-paced. NationStates/Cantr are community-roleplay-first. The project's 2-hour UTC turn schedule is realized chiefly by P&W.

---

### 3.2 Politics & War (primary reference)

**What it is.** A persistent browser nation-simulation where a player governs one nation, develops it through cities, infrastructure, land, and improvements, trades raw and manufactured resources with other players, joins player-created alliances, and fights abstract one-vs-one wars with global political consequences ([official homepage](https://politicsandwar.com/)).

**A. Core loop.** Onboarding: create a nation (name, leader, flag, currency, policies), choose a continent (this determines which raw resources the nation can mine). First objectives recorded in official strategy guidance: get cities and infrastructure going, establish farms (farmable on all continents), and either trade or ally. Between 2-hour turns players act; per-turn, the server applies income/upkeep/production.

- Source: [P&W-pedia — Cities](https://politicsandwar.com/pwpedia/article/Cities), [Continent](https://politicsandwar.com/pwpedia/article/Continent), [Improvements](https://politicsandwar.com/pwpedia/article/Improvements) — official-maintained.

**B. Nation development.** Cities are the unit of growth; the city purchase cost curve is steep (official example formula `50,000 × (X−1)³ + 150,000 × X + 75,000` where X = current count). Each city has infrastructure (one improvement slot per 50 infrastructure), land (reduces density/disease; boosts farms), and improvements (power, resource extraction, commerce). Buildings have upkeep and power demands (e.g., the official coal-plant page documents 500-infrastructure capacity, 1.2 coal per day/100 infrastructure, $1,200/day). ([Cities](https://politicsandwar.com/pwpedia/article/Cities), [Infrastructure](https://politicsandwar.com/pwpedia/article/Infrastructure), [Land](https://politicsandwar.com/pwpedia/article/Land), [Coal Power Plant](https://politicsandwar.com/pwpedia/article/Coal-Power-Plant), [Improvements](https://politicsandwar.com/pwpedia/article/Improvements))

**C. Economy.**
- **Resource structure:** 11 tradeable resources, commonly itemized as Food, Coal, Oil, Uranium, Lead, Iron, Bauxite (raw) and Gasoline, Munitions, Steel, Aluminum (manufactured); classification per community wiki, consistent with the official pedia's resource interface. Raw-resource production is continent-dependent except Food (farmable everywhere) — this is the intended scarcity mechanism that makes every nation a supplier of some value and a demander of others. ([Resources — community wiki](https://politicsandwar.fandom.com/wiki/Resources); [Food](https://politicsandwar.com/pwpedia/article/food), [Continent](https://politicsandwar.com/pwpedia/article/Continent) — official)
- **Production examples (official, per building):** coal mine 3 coal/day; oil well 3/day; bauxite mine 3/day; uranium mine 3/day; munitions factory 18 munitions from 6 lead/day. ([Coal Mine](https://politicsandwar.com/pwpedia/article/Coal-Mine), [Oil](https://politicsandwar.com/pwpedia/article/oil), [Bauxite](https://politicsandwar.com/pwpedia/article/bauxite), [Uranium Mine](https://politicsandwar.com/pwpedia/article/Uranium-Mine), [Munitions Factory](https://politicsandwar.com/pwpedia/article/Munitions-Factory))
- **Income and expenses:** population × commerce drives tax income; commerce improvements raise citizen income. A community-maintained formula page gives `dailyCityIncome = ((Commerce / 50) × 0.725 + 0.725) × Population` — **community-reported, not verified as current**. Expenses: improvement upkeep, power/fuel/feed (running out of food cuts gross income by 33% per official Food page), military upkeep. Policy levers alter costs (Open Markets +1% gross income; policies reduce city/infra costs, project costs, or military upkeep). ([Nation Formulas — community](https://politicsandwar.fandom.com/wiki/Nation_Formulas); [Population](https://politicsandwar.com/pwpedia/article/Population); [Food](https://politicsandwar.com/pwpedia/article/food); [Domestic Policy](https://politicsandwar.com/pwpedia/article/Domestic-Policy))
- **Seasonality:** food production +20% summer / −20% winter ([official Food page](https://politicsandwar.com/pwpedia/article/food)).
- **Trade and the market:** the official homepage markets the economy as "100% Player Driven"; trades are player-to-player offers of resources/cash, and the market is where strangers trade. Raw-resource geography is the stated driver of specialization and interdependence. Officially, trade rules prohibit automated trading; scripts that notify of opportunities while leaving action manual are allowed ([Game Rules](https://politicsandwar.com/rules/)). **Not verified:** current average prices, market matching/fee internals (a community API page describing the price feed was marked deprecated on the community wiki itself).
- **Alliance-level economy:** alliances run banks, loans, grants, and "city circles" growth programs, and may tax money and/or resources, with tax brackets like "70/40" (70% money + 40% resources per turn) — documented on the official P&W-pedia economics guides ([Basics of Econ](https://politicsandwar.com/pwpedia/article/Basics-of-Econ), [Tax Brackets](https://politicsandwar.com/pwpedia/article/tax-brackets)).

**D. Time and progression.**
- **Turn:** 2 hours ([official glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary)); 12/day. Per official glossary, a **turn** ticks revenue and taxes; separately there is a **day** change.
- **Offline progression:** the nation accrues income/upkeep impersonally while the player is away; resources accrue; between turns the player makes purchases/trades/construction.
- **Protection and absence:** **Vacation Mode** freezes in-game actions and lasts until it expires or is cancelled ([official glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary)).
- **Separate "beige" mechanic:** after certain war endings, the community wiki (and [official glossary's "beige" entry](https://politicsandwar.com/pwpedia/article/Terminology-Glossary) describes 2 days of protection from new declarations). The exact current rule wording was not re-verified in this pass but is consistently described across recent community material as an anti-grief measure.

**E. Politics/domestic systems.** There is no simulation of internal party politics, elections, or a parliament inside the game client: the game emphasizes domestic **policy chips** (mini-choices that toggle modifiers) and population/stability numbers. Anything resembling parliamentary politics happens through alliance governance, not a national parliament. **Decision:** this absence is an official-shaped gap in the game, and the community relies on the player economy/alliance layer for political texture.

**F. Diplomacy.**
- Nation-level: embargoes and preferred markets vs "trade bloc color-bonus" incentives (the official glossary defines color-bloc bonuses; exact values not verified here).
- Peace/diplomatic UI includes a communication channel and a war-ending "offer peace" interaction ([community War wiki](https://politicsandwar.fandom.com/wiki/War)).
- Between alliances: **treaties** with widely standardized abbreviations (MDP, MDoAP, ODP, NAP, PIAT, protectorate) and a publicly displayed **treaty web** among top alliances — an emergent political visualization supported officially ([Terminology and Glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary)).

**G. Alliances.**
- Created in-game; admission often handled off-game (Discord/forum) per community wiki.
- Roles: **Leader / 2iC / High Government / Low Government** as customary in-game rank classes; internal constitutions vary (elected, meritocratic, departmental). ([Alliance Ranks — official](https://politicsandwar.com/pwpedia/article/Alliance-Ranks); [Alliance — community](https://politicsandwar.fandom.com/wiki/Alliance))
- **Banks, taxes, supply, MMR:** alliance banks hold money/resources and issue loans/grants; tax brackets up to the documented maximums; **MMR** ("Minimum Military Requirement", e.g. `4/3/2/1` barracks/factories/hangars/drydocks) is an alliance readiness convention, not a battle mechanic ([official glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary)).
- **Collective action:** treaty webs, coordinated "blitzes" (official strategy guide), coordinated raid campaigns, and diplomatic communication systems.
- **Not verified in this pass:** current exact permission matrix per rank, alliance size caps, alliance-level combat bonuses ([community Alliance Permissions page returned 403](https://politicsandwar.fandom.com/wiki/Alliance_Permissions)).

**H. Warfare — the most important reference for the project's abstract war.**
- **War types:** Raid (loot-focused), Ordinary, Attrition (infrastructure-damage-focused); war policy changes limited to once per 60 turns ([official war-strategy page](https://politicsandwar.com/pwpedia/article/Basics-of-War-Strategy), [War Policy](https://politicsandwar.com/pwpedia/article/War-Policy)).
- **Offensive/defensive war slots:** 5 offensive / 3 defensive; max war duration 60 turns (5 days) — **community wiki figures, not verified as current** ([War — community wiki](https://politicsandwar.fandom.com/wiki/War)).
- **Combat actions:** ground battles (soldiers/tanks), airstrikes (aircraft), naval battles (ships), missiles, and nuclear attacks; each attack succeeds with a projectile outcome described on the community wiki as **Immense Triumph / Moderate Success / Pyrrhic Victory / Utter Failure**; success states can establish **Ground Control / Air Superiority / Blockade** — blockade halts target cash/resource transfers. **Resistance** is the opponent's "will to fight" that must be reduced to 0 to end a war as a win. ([War — community](https://politicsandwar.fandom.com/wiki/War), [official Basics of War Strategy](https://politicsandwar.com/pwpedia/article/Basics-of-War-Strategy))
- **Loot and destruction:** raids steal cash/resources; attacks destroy improvements and infrastructure; blockades stop transfers. Airstrikes can destroy money rather than steal it.

**Notable war-limit mechanics:** vacation-mode immunity [official], "beige" post-war protection (2 days), cooldown-protected declarations — all anti-grief mechanisms worth studying for the project's own conflict design.

**I. Nukes / economic warfare.** Nuclear weapons as single-use strategic arm (community wiki describes production, launch cost, one-per-day plus possible project-side extra, fallout affecting food/productivity, defensive projects). Community-maintained, so numbers are unverified currently ([Nuclear Weapons — community](https://politicsandwar.fandom.com/wiki/Nuclear_Weapons); [official homepage](https://politicsandwar.com/) notes fallout affects more than the target).

**J. Monetization.** Officially "100% free to play" with a **limited donation system intended to prevent pay-to-win**; VIP Status (via credits) is described in the official glossary as providing "slight roleplay and in-game perks." ([homepage](https://politicsandwar.com/); [Game Rules](https://politicsandwar.com/rules/); [glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary)). **Not verified:** the current full store contents and whether credits can be bought with real money; no claim was found in the sources fetched that peace offers or wars are purchasable with real money.

---

### 3.3 NationStates

**What it is.** A policy-simulation community platform: a player governs a fictional nation by answering **Issues** (policy dilemmas), which shift a national profile across civil, economic, and political axes; nations live in **regions** and can join the **World Assembly (WA)**, a fictional international legislature. It has no built-in war or trading.

**Sources used and their limits.** The reading tool could not open nationstates.net pages (FAQ, API docs, forum); the assembled picture rests on[Wikipedia's overview](https://en.wikipedia.org/wiki/NationStates) (secondary) plus the community wiki's Issue page ([https://nationstates.fandom.com/wiki/Issue](https://nationstates.fandom.com/wiki/Issue)). All specific mechanics below carry **secondary-source confidence**.

**Core loop:** receive issues (configurable cadence — community wiki reports a default ~6-hour setting after the new-nation period, tunable to 12/24/48 hours), pick options or dismiss, watch the nation's profile (e.g., 27 government type classifications on three axes — civil, economic, political freedom) change over time. Meanwhile participate through regions, telegrams, dispatches/factbooks, and roleplay.

**Progression:** statistics drift, classification changes, regional politics (founder vs elected-WA Delegate, endorsements), and WA resolution authorship. No building, no money, no combat; "invasion/defence" gameplay is about regional influence via WA membership and endorsements, not armies.

**Diplomacy/social:** embassy system (inter-regional), dispatches, taunts/roleplay, treaties are textual, not mechanical. Multination rule commonly reported: multiple nations allowed but **one WA member per person** — flagged as commonly reported, not re-verified here ([community/overview material only](https://en.wikipedia.org/wiki/NationStates)).

**Monetization:** publicly it's a free game supported by donations; official wording and current privacy/donation statements could not be reached in this pass, so treat any exact claim as unverified.

**Why it matters to the project:** NationStates demonstrates how a *low-effort, check-in cadence* can sustain a huge multiplayer world, and shows a working model of community diplomacy (embassies, factbooks, treaties as social artifacts). But it is instructive mostly by contrast — the project intends mechanical economy, trade, and war, which NationStates deliberately lacks.

---

### 3.4 Cyber Nations

**What it is.** A long-running (2006-present) browser nation simulation with a **daily** update cycle, a text-heavy UI, GNP/taxes, trade circles, improvements, wonders, and simple abstract war.

**Key facts (official index pages where possible).**
- **Nation creation:** government type (11 options), religion, tax rate, ethnicity, currency choice. A possible mismatch between chosen and citizen-preferred government reduces happiness; government/religion can be re-chosen once every 3 days ([About Topics index](https://www.cybernations.net/about_topics.asp)). Currency mechanical effect: **unverified**.
- **Economy:** daily tax collection as a percentage of citizens' income; land grows naturally at 0.5 mi/day; population density, happiness, improvements all affect both population and earnings. "GNP" is an income indicator, not a production simulation ([official index](https://www.cybernations.net/about_topics.asp); [official about page](https://www.cybernations.net/about.asp)).
- **Trade circles:** a national resource pair can be traded with allies; trades require mutual approval; community guides optimize **6-nation circles** (5 normal slots + 1 from a harbor) to assemble bonus-resource sets like Steel/Construction/Asphalt/Automobiles ([community economics guide](https://cybernations.fandom.com/wiki/BASICS:_Economics_Guide)). Two nations can share duplicate resources without double-benefit ([official index](https://www.cybernations.net/about_topics.asp)).
- **Improvements:** stack to 5 of a type, limited by citizen count (1 per 1,000 citizens); have recurring bills.
- **Wonders:** one wonder per 30 days, $5,000/day upkeep, only one of each type; some prerequisites (e.g., Manhattan Project enables nukes, Stock Market boosts income, SDI reduces nuke effectiveness, Pentagon strengthens ground combat) ([official index](https://www.cybernations.net/about_topics.asp)).
- **Alliances:** officially described as **player-created and managed; no hard-coded in-game benefits** for membership; treaty types (MDP/MDoAP/ODoAP etc.) are community diplomatic conventions, not built-in mechanics ([official index](https://www.cybernations.net/about_topics.asp)). This is the key contrast with P&W, whose alliances are in-game organizations with tools.
- **War:** soldiers/tanks/cruise missiles/nukes/aircraft/navy/spies; **cruise missiles and aircraft limited to 2 attacks per day per front**; **nuclear launch locked for 24 hours after war declaration**; land and infrastructure damage; inactivity-based deletion at **>25 days** without tax collections — **community-FAQ figure, not re-verified** ([official index](https://www.cybernations.net/about_topics.asp); [community FAQ](https://cybernations.fandom.com/wiki/Frequently_Asked_Questions_about_Cyber_Nations)).
- **Schedule:** once-day taxes; community FAQ cites 6:00 a.m. GMT / 00:00 CN time as the declared update; **not re-verified as today's official schedule**.
- **Security/limits:** 2,000-action daily hit limit documented officially.
- **Status:** officially active with a mobile-friendly update logged **April 4, 2025** ([Update Log](https://www.cybernations.net/game_update_log.asp)); community scale appears much smaller than peak (a 2018 forum page noting <4,000 active nations could not be fetched for verification; not asserted).

**Lesson for the project:** Cyber Nations shows the fully player-run alliance model (rich social, thin mechanical) versus P&W's tooling-rich model, and validates resource-circle design (which the project may adapt as "trade networks" once it removes geography).

---

### 3.5 eRepublik

**What it is.** A persistent political/economic/military MMO set in a fictionalized real-world map: real countries, regions, borders, conquest. Players are citizens and can be workers, entrepreneurs, soldiers, party members, congress members, or presidents in their country.

**Verified highlights (official wiki, with the caveat that it is user-maintained and partially outdated).**
- **Politics:** citizenship-based voting; parties; monthly elections (documented in a wiki tutorial explicitly marked outdated); congress can pass laws on taxes, citizenship, etc.; president has war/peace/embargo instruments ([Citizenship](https://wiki.erepublik.com/index.php/Citizenship), [Taxes](https://wiki.erepublik.com/index.php/Taxes), [Tutorial (dated)](https://wiki.erepublik.com/index.php/Tutorial)).
- **Economy:** companies produce goods from raw materials; marketplaces sell in local currency; **gold** is a global reserve currency exchangeable on a monetary market; work/import taxes and VAT set by Congress ([Marketplace](https://wiki.erepublik.com/index.php/Marketplace), [Gold](https://wiki.erepublik.com/index.php/Gold), [Taxes](https://wiki.erepublik.com/index.php/Taxes)).
- **War:** region-based conquest; battles divided into timed rounds (90–120 minutes per round per official wiki) where players contribute damage from their inventory (weapons, food) and sidepoints accrue; occupation, resistance wars, and resource-wars events ([Battle](https://wiki.erepublik.com/index.php/Battle), [Wars](https://wiki.erepublik.com/index.php/Wars), [Resource wars](https://wiki.erepublik.com/index.php/Resource_wars)).
- **Anti-multi:** one citizen per person; sharing accounts prohibited ([Multi-accounts](https://wiki.erepublik.com/index.php/Multi-accounts)).
- **Monetization:** gold purchasable with real money (US listing showed ~$4.99 → $99.99 tiers) ([Apple App Store listing](https://apps.apple.com/us/app/erepublik/id1381347591)).
- **Status:** still operating with 2025 app updates (Google Play updated 2025-Q4, Apple App Store v2025.8.0); live site is signed-up-friendly. **Player counts unverified**.

**Relevance:** eRepublik is the project's cautionary example of a *map-anchored* game whose depth (congress, companies, dual currencies, region wars) comes at the cost of heavy complexity and long onboarding. Its dual-currency design and congress-voted taxes are two specific, well-sourced design devices worth considering for the project's own toolbelt.

---

### 3.6 Prosperous Universe

**What it is.** A browser (APEX) economic MMO by **simulogics** where players run a company: planet bases, extraction, manufacturing, shipping, and trading on **exchange-specific commodity markets**. No combat; competition is economic and political.

**Core facts (official site + official handbook).**
- **Market:** commodity exchanges host buy/sell orders that don't auto-match unless prices line up; different exchanges list different goods → spatial price differentiation, exploiting transport and logistics ([official trading tutorial](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/trading/index.html)).
- **Contracts:** shipping agreements let one player transport for another; contracts make logistics a gameplay activity ([official contracts tutorial](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/contracts/index.html)).
- **Production:** buildings on planet bases with recipes and efficiency factors ([production tutorial](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/production/index.html), [efficiency factors](https://handbook.apex.prosperousuniverse.com/wiki/efficiency-factors/index.html)).
- **Free-to-play model:** FREE (5 bases, 2 ships in flight, no corporation founding), PRO (**€8/month**, non-recurring per official FAQ), and BASIC (a downgrade state that retains key features of PRO partially) ([official PRO page](https://prosperousuniverse.com/premium), [official FAQ](https://handbook.apex.prosperousuniverse.com/wiki/faq/index.html), [licenses tutorial](https://handbook.apex.prosperousuniverse.com/tutorials/current-tutorials/06-licenses/index.html)).
- **Design philosophy:** developer-stated values are deep simulation, fairness, consequences, and "no looming destruction" — the explicit anti-combat positioning ([About page](https://prosperousuniverse.com/about), [Steam listing](https://store.steampowered.com/app/1761220/Prosperous_Universe/)).

**Why it matters:** it is the cleanest proof that a *no-war* economy-first multiplayer can sustain itself with subscriptions locked behind feature access (not direct power). Its exchange-per-location and contract-for-shipping mechanics are directly transferable to the project's "symbolic network" concept, where "location" is replaced by "where a nation's enterprises sit inside the network".

---

### 3.7 Sim Companies

**What it is.** A free-to-play business-simulation MMO in a shared player economy: build factories/stores/farms, research **quality progression**, buy inputs, sell wholesale or retail, use contracts and logistics.

**Verified highlights (officially accessible pages only).**
- Developer is Sim Companies s.r.o.; free to play with in-game purchases ([Terms](https://www.simcompanies.com/terms/); [Steam](https://store.steampowered.com/app/2253720/Sim_Companies/); [Google Play](https://play.google.com/store/apps/details?id=com.simcompanies.simcompaniespwa&hl=en_US)).
- Real-time, **asynchronous multiplayer**; the game aims for brief check-ins ([Steam / homepage](https://www.simcompanies.com/)).
- Profitability depends on market conditions; strategies decay in profitability as other players copy them ([Google Play description](https://play.google.com/store/apps/details?id=com.simcompanies.simcompaniespwa&hl=en_US)).
- Retail is a distinct activity: the shop owner sets a price; the game simulates demand/sales speed versus wholesale dumping. A "quality ladder" (researched) constrains what a company can produce, with higher-quality inputs gating higher-quality outputs (community wiki detail; not verified for current numbers) ([community Research page](https://simcompanies.fandom.com/wiki/Research)).
- **Unverified (cannot be checked this pass):** current tax/admin percentages, exact wages/worker formulas, offline progression rules, land/plot costs. The official FAQ/guides pages fail to render (app-shell). Treat any precise number from community sources as dated.

**Why it matters:** Sim Companies is the niche example of a *no-war but highly competitive* sim showing (a) quality/tech ladders as progression, (b) retail sim (a demand model driven by the player's own pricing) that could inspire a future "consumer market" in the project's economy, and (c) that profit from price-setting (not just from production) is a satisfying gameplay surface.

---

### 3.8 eDominations (discovered during research)

An eRepublik-lineage nation MMO currently operating, with a distinct twist: **monthly presidential and congressional elections** run as official modules (president has war/peace/embargo powers; congress votes tax laws), an alliance-level political system with a game-announced "Campaign of the Day" battle for coalitions, and 24-hour battles in three 8-hour rounds. Economic modules link company production to weapon/food demand in combat. Monetization: listed as free to play with a gold currency; some actions have gold costs (community wiki documents an alliance-creation gold cost). Monetary purchase policy **not verified** this pass. ([Short Look article](https://edominations.com/en/article/21642/SHORT%20LOOK%20TO%20EDOM%C3%84%C2%B0NAT%C3%84%C2%B0ONS), [Elections wiki](https://wiki.edominations.com/elections/), [Alliance wiki](https://wiki.edominations.com/alliance/), [War wiki](https://wiki.edominations.com/war/), [Trading Center wiki](https://wiki.edominations.com/trading-center/), [Companies wiki](https://wiki.edominations.com/companies/))

**Lesson:** a currently-operating, moderate-scale geopolitics MMO that **explicitly connects politics ↦ economic policy ↦ military competition** — the loop the project aims for — while showing how heavy complexity can burden onboarding.

---

### 3.9 Earth Empires, Cantr II, Utopia (brief profiles)

- **Earth Empires** — round-based server strategy game with different server formats (Alliance / Cooperation / Conquest / Classic / Express / FFA) and explicit anti-multi/anti-automation rules; homepage showed ~1,227 active countries and ~107 online at access time (a snapshot, not durability evidence) ([homepage](https://www.earthempires.com/), [rules](https://www.earthempires.com/rules)). Lesson: server-format diversity and explicit automation rules.
- **Cantr II** — persistent, player-authored society: residents create goods, buildings, institutions, religions inside a slow, text world; "Capital Rule" (act only on in-character knowledge) is a famous social-design constraint; explicitly 100% free; donation requests had no material benefits (a 2013-dated community page; funding status today unverified) ([homepage](https://www.cantr.net/), [rules](https://cantr.net/en/index.php?page=rules), [community finance page (2013)](https://wiki.cantr.net/index.php/Game_Finances)). Lesson: social/organizational depth can be player-authored rather than mechanically simulated.
- **Utopia** — kingdom-teamwork text strategy with complementary roles, thief/mage/military actions, and long-lived "Ages" (rounds); official homepage confirms live operations; engagement/economy details not verified this pass ([homepage](https://utopia-game.com/shared/)). Lesson: role-specialization inside a team (divided labor inside an alliance) is a durable multiplayer retention device worth evaluating.

---

## Section 4 — Core gameplay and systems analysis

### 4.0 Why these games cluster this way

Two structures dominate the genre:

1. **Economy-first with a defined tick / action economy:** P&W (2h), Cyber Nations (daily), eDominations (heat-clock battles), Prosperous Universe/Sim Companies (continuous management). The player acts between scheduled updates; the world changes at a server-driven cadence.
2. **Community-first where the "world" is social:** NationStates, Cantr II. The mechanics are light; the players' diplomacy, roleplay, and organization do the heavy lifting.

There is also a significant anti-pattern: eRepublik's accumulate-over-time complexity — real-world-map countries multiply region variables and onboarding pain.

---

### 4.1 Nation development and progression

Common patterns:

- **Growth is bought per-step and costs scale steeply** (P&W cities; CN improvements/wonders; Sim Companies facility upgrades). This creates long-term investment goals and pacing (a big purchase is a mindset goal, not a rush).
- **Progression is bounded by soft resource floors** (population, citizens, commerce) rather than hard unlocks.
- **Choices in nation creation matter but mainly via bonuses/happiness** (CN's government/religion/currency choice; P&W's continent choice is the most impactful because it constrains raw-resource access).
- **Wonders / big exclusive projects** (CN: 1 of each type, 1 per 30 days, steep upkeep; P&W something similar in the official project language but not fully verified this pass). Rare-but-major choices let mature nations differ qualitatively, not just quantitatively.

Trade-off structure: eRepublik and NationStates invert the pattern by making all "progress" relational: reputation, offices, history — proving that a persistent game can also reward *visibility and status*.

### 4.2 Economic systems

- **Resource spectra and specialization:** P&W's raw/manufactured split with continent-locked raws drives trade. CN's trade circles demonstrate a formulaic cooperation design that is the antecedent of P&W's trade-economy. Prosperous Universe implements the most literal version (spatial price arbitrage). eRepublik/eDominations implement trade under nation-level taxes and embargoes.
- **Dual currencies** (eRepublik gold + local) or a global reserve currency (Sim Companies uses in-game money only; eDominations uses gold heavily) let designers separate **global** (gold) from **national/local** flows — a design tool the project should evaluate early because it affects how raids, taxes, and trade circulate value.
- **Tax authority as governance gameplay** (eRepublik/eDominations congress votes tax rates; P&W alliance tax brackets; CN relies on static personal tax-rate choice) — an example of "policy levers as shared social decisions."
- **Connection of economics to war demand:** munitions/weapons/food all pull production into war logic in P&W and eDominations. War is an economic event, not merely a score event.
- **Upkeep / drains are as important as income.** In P&W, food scarcity alone can cut gross income 33%; CN has daily bills that accrue if unpaid; Prosperous Universe's logistics costs. This is what makes "economy" a *management* problem rather than an idle accumulator.

### 4.3 Time and progression structure

| Schedule | Games | What it does |
|---|---|---|
| **Short recurring turn (2 hours)** | Politics & War | Income/production tick; players act between; balance between urgency and rest |
| **Daily update** | Cyber Nations | Once-a-day income, bills, war limits; simpler management |
| **Configurable issue cadence** | NationStates | Player-chosen check-in (~daily) — cadence is traveler-friendly |
| **Real-time w/ short battle windows** | eRepublik (90–120 min rounds), eDominations (24 h / 3×8 h rounds) | Combat is a scheduled event with player participation windows |
| **Continuous management-paced** | Prosperous Universe, Sim Companies | No ticks; queues/markets run whenever the player's orders resolve |
| **Rounds/Ages** | Earth Empires, Utopia | Competitive equality via periodic resets; different game modes per server |

Key observations:

- **Action-based pull economy** (P&W war initiative, CN 2-attacks/front/day) prevents "wars are won by logging in most" and forces strategic patience.
- **Offline progression is the norm** — the nation accrues when the player is away; absence is priced via idle vulnerability (war targets) or absence-decay (CN's inactivity deletion is the extreme).
- **Vacation / peace modes as anti-grief** appear in P&W (Vacation Mode officially; "beige" post-war protection) and CN (community-FAQ peace mode). Any persistent project needs an explicit absence policy.

### 4.4 Politics and national management

- **P&W** has "policy chips" and domestic modifiers but **no in-game parliament**; domestic politics are effectively a resource-management surface. Community conventions (leaders, MMR compliance, alliance council culture) fill the role of political texture.
- **CN** has nominal government/currency/religion choices and a hidden preference mechanic (citizen happiness).
- **eRepublik/eDominations** make politics a first-class citizen with elections, congress, tax laws, and (trusted) presidency war powers — the strongest examples of **governance with real stakes**, but also with the associated onboarding/complexity costs and encourage low-information voting.
- **NationStates/Cantr** render politics as social roleplay (and handle "what is true" via roleplay rules like the Capital Rule).

**Design interpretation:** a project wanting domestic politics has to choose between (a) light modifiers (P&W-style), (b) heavy real institutions (eRep-style), or (c) social-authored politics (NationStates-style). This is a *genre fork*, not a slider.

### 4.5 Diplomacy and international relations

- **Mechanical levers (limited):** embargoes, preferred trade partnerships, war declarations, peace offers, vacation/peace modes. Nothing more complex.
- **Treaties:** text-based agreements between alliances/organizations; in P&W *in-game treaty objects* exist with standard abbreviations; in CN they are purely social conventions with no in-game object. Having official in-game treaty objects (as P&W does) makes the diplomatic world inspectable — a notable user-facing advantage.
- **Norms and etiquette are player-authored:** both P&W and CN communities have deep norms around what constitutes "just cause", raid etiquette, size-abuse rules, etc. **Design insight:** diplomacy is half rules, half culture; the game can *support* culture (public treaty web, embassies, visible history) without encoding every norm.

### 4.6 Alliances and social organization

- **Formal structures exist** in P&W: ranks, permissions, banks, taxes, in-game diplomats, official treaty objects. Alliance-level tools (supply, growth programs, city circles, MMR requirements) are part of what makes large-scale communities function.
- **CN** deliberately minimal: any group is "player-managed outside the game". Its community instead uses external tools (forums, Discord) to organize.
- **Earth Empires / Utopia** show clans/kingdoms as *the primary social atom* — a game where a single player is weak and the group is the unit of competition.
- **Social per-player layers** (P&W's leader/seniority structures, Utopia's role specialization, eDominations nation/coalition layers) suggest a hierarchy the project should consider: **player ↦ nation ↦ alliance ↦ bloc/treaty**. P&W also practically shows that in-game tools + off-game Discord coexist: a new game can sponsor in-game tools without needing to absorb all coordination.

### 4.7 Military and warfare

- **Geographic battle model** (eRepublik/eDominations): regions fought over with timed rounds; borders constrain targets; resistance wars recapture territory. High theatrical richness; heavy map/complexity cost.
- **Abstract duel model** (P&W, CN): a pair of nations at war, mutual discrete attacks with consequences for both sides, no front lines. P&W's model is the project's best deeper-time reference for abstract war because it already solves: war *opening* (declared or raid), war *limiting* (max concurrent wars, cooldowns, vacation-mode), *war-range* constraints (score/index range rules), *war economics* (loot vs destruction mix), *co-leadership* (alliance war coordination), and *symmetric resolution* (peace offers, intermittent beige-immunity grace periods).
- **Round-based** (Earth Empires/Utopia): war is an in-round social-institution problem, not battle simulation; useful only as an analogy for alliance-level coordination.
- **Anti-grief tools recur:** vacation/peace mode, post-war immunity, war range/score-band restrictions, sanctioned loot-vs-attrition quotas, cooldowns on re-declaration.

**Key takeaway:** the abstract duel model (b) is the genre's proven route for a "mapless, symbolic" war system like the project's; the political layer (who is allowed to attack whom, with what escalation history) is where most of the design intelligence lives, not in the combat math.

### 4.8 Multiplayer interaction and player activity

- **News and social feeds:** P&W's global/alliance news and event pages; eDominations' "latest updates" and event coverage; NationStates' region-government pages and dispatches. A *world timeline* is a stated feature of every healthy game in this genre.
- **Rankings/leaderboards:** all major games surface power/economy rankings; P&W exposes score and alliance rank leaders; CN and eRep nations lists.
- **Player interaction surfaces:** direct messaging (all), trade systems (P&W/CN/eRep/PU/SimCo), and social spaces off the game proper (Discord/forums). Officially supported interaction — and enforcement *of interaction limits* (automation bans in P&W games; anti-multis in eRep; P&W's no-sitter/no-automation rules) — is a shared genre feature.
- **New-player protection:** P&W's Vacation Mode, a starting score-band for "newbie" raid targets (community-described, specific bands unverified here), and CN's peace mode give newer players breathing room; eRepublik's long-run churn shaped its own protections (the exact current "new citizen protection" rule could not be verified). This is a recurring genre **must-have** for retention design.

---

## Section 5 — Genre patterns

### 5.1 Common genre patterns (appear in most games)

| Pattern | What it does | Demonstrated by | Player need | Strong evidence? |
|---|---|---|---|---|
| Scheduled world update (tick/turn) | Removes real-time pressure; gives the server one canonical state-advance event | P&W (2h), Cyber Nations (daily) | Fairness, low FOMO economy | Strong (official docs) |
| Server-authoritative accrual while offline | A player who logs off still accumulates income and suffers ongoing costs — the world is alive without them | P&W, CN, PU, SimCo | Continuity, "my nation is real" | Strong |
| Player-to-player resource trade as the economy engine | Specialization + interdependence | P&W, CN, PU, eRep, eDominations | Social binding, strategic choice | Strong |
| Alliance/clan as the durable social unit | Group loyalty, shared banks, coordinated diplomacy, collective war | P&W (in-game), CN (social), Earth Empires/Utopia (primary unit), eDominations (coalitions) | Belonging, scale | Strong |
| Calibrated anti-grief (vacation/peace modes; score-band targeting; cooldowns; inactivity rules) | Protects casual/new players; limits mutual destruction spirals | P&W, CN, eRep, Earth Empires | Onboarding, fairness | Strong |
| News feed + rankings as world presence | Makes the world legible; motivates status play | P&W, CN, eRep, eDominations, Earth Empires | Visibility, narrative | Strong |
| Multi-account/automation prohibition | Preserve fairness in a slow-economy game | P&W, CN, eRep, Earth Empires, PU | Integrity | Strong (official rules) |
| Taxation/upkeep as ongoing pressure | Turns growth into management, not accumulation | P&W, CN, PU, SimCo | Meaningful decisions | Strong |
| Standardized treaty abbreviations and alliance etiquette conventions | Speeds up diplomacy among strangers | P&W (official glossary), CN (community) | Low-cost coordination | Strong |
| Long-run progression on a shared world (months/years) | Builds legacy, rivalry, attachment | all persistent games | Belonging | Strong |

### 5.2 Less common or specialized patterns

| Pattern | Demonstrated by | Player need / caveat |
|---|---|---|
| In-game treaty objects with a public treaty web | P&W (official) | Makes the diplomatic network inspectable; unusual — most games leave treaties off-game |
| Wonders / one-per-period mega-projects | Cyber Nations, (P&W variant unverified) | Late-game differentiation; risk: "rich get richer" |
| Bonus resource sets from combination rules ("trade circles") | Cyber Nations (community), related mechanics in P&W color-trading | Cooperative optimization puzzles; vulnerable to trading-colusion if unmoderated |
| Simultaneous nation creation choices w/ hidden preference | Cyber Nations (govt/religion/currency) | Early identity choice; weak if unverifiable |
| Retail demand simulation | Sim Companies | Price-setting as gameplay; needs careful con/balance |
| Contract/shipping-based logistics economy | Prosperous Universe | Makes *moving goods* a gameplay act; precursor to "supply & logistics" designs |
| Seasons/ages as fairness resets | Utopia, Earth Empires | Recreates competitive equality; destroys legacy — depends on audience |
| Player-authored social rule sets (Capital Rule etc.) | Cantr II | Deep emergent institutions, but depends on moderation & culture |
| Regional-control subgame without combat | NationStates WA/endorsement invasion-defence scene | Political intrigue at scale; niche and *not* mechanical |

### 5.3 Context-dependent patterns

- **Real-world map (geographic anchoring).** Works for eRepublik/eDominations because their core fantasy is real-world geopolitics and border conquest; heavy cost (map UI, regional resources, onboarding). A *fictional, mapless* game like the project should probably not adopt geographic map Warfare; this report's other evidence (P&W's 2-hour-turn, no-map abstract duels) shows the alternative works.
- **Dual/global currency.** Valuable where the game wants a stable unit of account for cross-nation exchange, but adds complexity (eRep's gold; PU's premium). If resources and per-turn income already provide a value taxonomy, a dual currency may be overkill for a v1.
- **Parliamentary/election politics.** Rich (eRep/eDominations monthly elections, congress, tax votes) but expensive to operate (moderation, low-information voting risk, churn). For a v1 on a 2-hour turn cycle, light institutional policies may be wiser than full elections; revisit later.
- **Heavy progress without skips/waiting.** Prosperous Universe and Sim Companies are continuous; in a *turn-based* game the clock discipline must be preserved — building skip/pause features soon erodes what makes the schedule fair.
- **One-nation-per-player enforcement.** Practical necessity demonstrated by every money-using persistent game (P&W official rules; eRep anti-multi; PU agreement). Enforcing via identity/behavior analytics is a hard engineering problem.

---

## Section 6 — Browser-game and operational considerations

These are **engineering/operational** considerations for a persistent browser game like ours. They are stated as generally applicable engineering knowledge and *clearly distinguished* from the competitor facts above; no competitor's internal architecture is publicly known.

### 6.1 Scheduled processing (turn engine)

**Requirement.** The project proposes a 2-hour fixed-UTC turn, i.e. 12 simulation boundaries per day, no reliance on an active browser tab, and no missed/duplicate execution. P&W's 2-hour-turn precedent shows the design is playable; the engineering challenge is executing it reliably on free-tier infrastructure.

**Cloudflare free-tier limits relevant to hosting this design** (as of 2026-10-22; official):

| Limit (Workers Free plan) | Value | Source |
|---|---|---|
| Worker requests per day | 100,000 | [Workers Limits](https://developers.cloudflare.com/workers/platform/limits/) |
| CPU time per HTTP request | 10 ms | [Workers Limits](https://developers.cloudflare.com/workers/platform/limits/) |
| CPU time per Cron Trigger invocation | 50 ms | [Workers Limits](https://developers.cloudflare.com/workers/platform/limits/) |
| D1 rows read per day | 5,000,000 | [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/) |
| D1 rows written per day | **100,000** | [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/) |
| D1 storage | 5 GB total (account-wide) | [D1 limits](https://developers.cloudflare.com/d1/platform/limits/) |
| D1 free-tier enforcement | Queries **fail** when exceeded (since 2026-09-01) | [Changelog 2026-09-01](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/) |
| D1 single-database size cap | 10 GB | [D1 FAQ](https://developers.cloudflare.com/d1/reference/faq/) |

**Design implications (engineering analysis, not competitor fact):**

- **12 Cron Trigger invocations per day are trivially affordable** (the binding constraint is *runtime*, not scheduling).
- **100,000 D1 row writes per day ≈ 8,300 rows' worth of writes per turn** at 12 turns/day — and every action a player takes between turns also writes (trades, purchases, alliance changes, war declarations). A design that writes one row per nation per turn already consumes ~N rows per turn for N nations; with updates to cities/resources/news rows multiplied, hitting the cap is realistic at a few hundred active nations *unless* writes are batched (single SQL statements updating many rows, delta tables, event-sourcing with periodic compaction). This must be a first-class architectural constraint, and cheaper designs (batching aggregates, deferred news rows) are a **research item for the architecture stage**.
- **Idempotency/duplicate protection:** industry-standard patterns for scheduled tick processing are (a) a *tick table* row keyed by `turn_id` with a state machine (claimed → running → done), (b) atomic claim (e.g., conditional `UPDATE ... WHERE turn_id=X AND state='pending'`), and (c) idempotent per-entity effect semantics. This is engineering practice, not genre research.
- **Missed job defense:** turn computation should be a *pure function over the last committed turn boundary*, so it can be recomputed/skipped for any missed cron firing (i.e., compute from tick N−1 to N, and only mark done on commit); "missed" turns can be re-run on the next trigger given idempotent design.

### 6.2 Database integrity and server authority

- All world-changing action must resolve **server-side**, validated against the current committed world state; the client is a presenter only. Genre evidence is indirect but consistent: every serious game in this genre exposes economy numbers that players rely on, and P&W's official rules again criminalize automated *trading*, precisely because automation threatens authoritative sequencing.
- Concurrency design risk in a 2-hour-turn game: a battery of player actions may hit a shared row (e.g., the same alliance bank) simultaneously. Standard remedies — transactions, row-level ordering, optimistic locking with version counters — are engineering practice, not genre facts.
- Multi-account/automation handling needs a plan regardless of which game is built; every reference game forbids automation and multis explicitly (official rules: P&W, CN, eRep), which implies the *detection* tooling (rate-limiting, device/behavior heuristics) is a recurring operational cost, not a one-time feature.

### 6.3 Free-tier operational strategy

- **Keep heavy logic off every request**: page/API requests and the tick worker are the billed surfaces; static assets served directly by the platform avoid spending code-CPU per request. D1 quota and Worker invocation count are the true hard constraints. This document does not recommend a specific architecture — that belongs to a later stage.
- **Economy of the "web-only" requirement**: the project explicitly wants no persistent open tab. Both P&W and CN rely on this; nothing in this report found a persistent-world browser game that requires a live connection except for real-time combat phases (eRep's battles), which the project avoids.

### 6.4 Summary: which operations are *unlike* the competitors

- The project's **12-turn/day** cadence is more frequent than any studied game except P&W's own 12; it is proven for gameplay, but its server-write volume per turn on the free tier must be engineered carefully (Section 6.1).
- The project's **no-map** rule means the world's state is a **graph**, not a map: there is no spatial interpolation work per turn — turn work is per-nation/per-relationship/per-market arithmetic, which is favorable to a short CPU window per invocation.

---

## Section 7 — Relevance to our game

For each system the project intends, here are what the findings mean *before* any design is finalized. These are design **inputs**, not decisions.

### 7.1 The 2-hour UTC turn
**What to understand:** P&W already ships a 2-hour turn (12/day) with server-side accrual and player actions between turns; Cyber Nations shows the daily variant. Our proposal is thus conventional enough to retain player trust and balance-timeoff (12 tick/day risk vs P&W's equivalent). **Open design question:** how our per-turn *action allowances* are structured (P&W uses war-specific action counts; CN uses attack/day front limits) — no design has been chosen.

### 7.2 Mapless "symbolic network" of nations
**What to understand:** No studied game ships a fully symbolic relationship-network with no map, so this is our genuine original territory. Precedents that *use* geography to generate scarcity/trade pressure (P&W continent-limited raws; PU's per-location exchanges; eRep's region resources) must be **replaced by something else** — candidate inspirations: CN's resource trade circles (combination bonuses as the trade engine), treaty-web layers (P&W's official treaty web), and alliance-supply channels (P&W's alliance banks and supply conventions). Any of these can create interdependence without coordinates. **Not decided; to be researched in later stages.**

### 7.3 Economy and resources
**What to understand:** three proven economic skeletons: (a) P&W's raw→manufactured two-tier chain with trade dependence, (b) CN's mutually-approved resource-sharing "circles" with combination bonuses, and (c) PU/SimCo's order-book markets + contract logistics. Any future project design should evaluate which of these bodies (or a mix) *fits a turn cadence* well: P&W's chain model and CN's circles are turn-friendly; PU's order book is more real-time. **Open question:** how much of the economy is "world market" (an exchange) vs "relationship network" (direct trade), and whether a reserve currency exists (eRep's gold pattern).

### 7.4 Domestic politics and stability
**What to understand:** three genre models exist — light policy modifiers (P&W), real institutions/elections with real stakes (eRep/eDominations), and social-authored politics (NationStates/Cantr). None currently combines heavy parliamentary politics with a 2-hour world cadence. **Recommendation-level note (not a decision):** the evidence suggests starting with a lighter domestic system, to keep the first release manageable; a heavier political layer can grow later.

### 7.5 Diplomacy and treaties
**What to understand:** P&W shows the value of *in-game treaty objects* (MDP/MDoAP/ODA/NAP/PIAT) plus a visually exposed treaty web; CN shows the opposite (no in-game objects; communities self-organize off-game treaties). The project's diplomatic system must choose how much is encoded (targeted obligations? automated consequences?) and how much is text/social. Open question: does a **treaty web visual** justify its engineering cost this early?

### 7.6 Alliances and shared coordination
**What to understand:** P&W's Alliance ranks/permissions, alliance banks, taxes, and MMR/supply conventions are the feature set that supports large-scale cooperation in-game; CN's alliance design shows communities will tolerate tool-poor games. The project needs at minimum: roles/permissions, shared funds, member taxes (like P&W's alliance taxes), and some coordination channel (like nearly every rival, off-game Discord remains possible). Open question: how much alliance-managed supply (e.g., an alliance war chest, strategic resource dumps) to provide.

### 7.7 Abstract warfare
**What to understand:** P&W is the strongest reference for abstract war: a duel war "object" with war types (raid/ordinary/attrition), mutual discrete attacks (ground/air/naval/missile/nuclear equivalents), resistance-to-zero end state, loot/destruction economics, blockades (econ-warfare on production/market access), anti-grief mechanisms (vacation mode, beige-like post-war protection, war caps/cooldowns), and peace offers. War *does not need a map* to have tactical texture — the "texture" in P&W comes from resource destruction and the economic consequences of loss. **Design discipline needed:** exactly how much the project borrows (e.g., resistance concept, war types) must be decided later as our own system, not copied values.

### 7.8 Operations Points (OP)
No studied game ships an action budget quite like a general-purpose strategic-action currency as described; P&W's per-attack "attack points" (community-sourced terminology; exact cost figures unverified this pass) and CN's daily per-front attack limits are the closest precedents. **Do not treat the provisional OP concept as final here** — it must be designed in a later stage against our own constraint set.

### 7.9 New-player protection, retention, and presence
**What to understand:** vacation/peace modes and score-band targeting are recurring tools. Retention appears tied to (a) predictable check-in rhythm (the 2-hour turn already gives this), (b) visible progression (rankings, news), and (c) group bonds (alliances). These map cleanly onto the project's existing structure.

### 7.10 Hosting and operations
**What to understand:** the Cloudflare free-tier arithmetic (Section 6.1) matters concretely at small-to-medium scale: 100k D1 writes/day is the tight constraint, and the D1 free tier now *fails queries* past the cap rather than merely warning. Architectural mitigation (batching, sparsity of per-turn writes, news retention policy) is a later-stage task. Nothing in the competitor findings prescribes a specific host; it only validates *that* such a game can be run web-based with server-driven turn logic.

---

## Section 8 — Uncertainties and research gaps

Classified by importance for later design. "High" = affects mechanics design; "Medium" = affects scope; "Low" = affects polish.

### High importance
1. **Current exact P&W market/trade internals** — fees, offer matching, current *standard* prices: not verified from official sources this pass; the community-market API documentation present on Fandom is marked deprecated there. **Needed before design of the market layer could begin.**
2. **Current P&W combat/economic formulas** (resistance math, attack outcome probabilities, war durability lengths, loot multipliers): community wiki-sourced; official sources describe at the level of strategy only. **Needed if the project ever borrows the P&W war sub-system structure** — not needed as literature, but would be needed before any adaptation.
3. **Current P&W alliance permission matrix / alliance caps**: community page returned 403; official pages do not include the tables. Medium for our design.
4. **Exact current Cloudflare free-tier limits in the *architectural* sense** (what counts as a row written in a batched statement, D1 effective throughput): official docs explain the *limits*, not behavior details. **Needed in the architecture stage.**

### Medium importance
5. **P&W's current monetization catalog** (what is actually purchasable via donation credits): only "limited donation system"/VIP status confirmed officially. Medium for the project's own monetization decisions.
6. **Sim Companies' exact fees/wage/tax formulas and offline-progression rules:** official FAQ pages failed to render. Medium.
7. **eRepublik's current war/protection rules** (a "new citizen protection" rule was not verified; the wiki's own Tutorial is dated). Medium–Low.
8. **Cyber Nations' current daily schedule and inactivity policies** (values came from the community Fandom FAQ, not current official configuration). Low–Medium.
9. **"Beige" post-war protection exact current duration/rules in P&W:** official glossary says 2 days, but community rules have evolved; flagged rather than forced. Low-quality, low-impact for our design if we design our own.

### Low importance
10. Player-count/economic stats of every competitor (no reliable public figures were found).
11. Cantr II funding status today (2013-dated community page only).
12. Cold War 2 thesis of play (we set it aside purely on the multiplayer-nation evidence).

### Inaccessible this pass (documented as a limitation, not as "no info exists")
- **nationstates.net** (403): FAQ, official rules, and API pages.
- **simcompanies.com** in-app FAQ/guide pages (app-shell rendering).
- Most **Fandom wiki pages** for P&W not already cited (rate limits/403s).
- Discord/community hubs, which cannot be researched without an account.

---

## Section 9 — Source register

All sources read 2026-10-22 unless otherwise noted. Official sources marked **[O]**, community-maintained marked **[C]**, third-party/second-hand marked **[3]**.

### Politics & War
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| P1 | [P&W homepage](https://politicsandwar.com/) | [O] | 2026-10-22 | Nation creation, "100% Player Driven" economy, resource trade, embargoes, scarcity, one-nation rule framing idea |
| P2 | [P&W Game Rules](https://politicsandwar.com/rules/) | [O] | 2026-10-22 | One nation per player, no automation of trades, limited donation system "intended to prevent pay-to-win" |
| P3 | [P&W-pedia — Game Guide](https://politicsandwar.com/pwpedia) | [O] | 2026-10-22 | Confirms P&W-pedia is the official-maintained information database |
| P4 | [P&W-pedia — Terminology and Glossary](https://politicsandwar.com/pwpedia/article/Terminology-Glossary) | [O] | 2026-10-22 | 2-hour turns (12/day), Vacation Mode, "beige" 2-day protection, MDP/MDoAP/ODA/NAP/PIAT definitions, MMR meaning, color-bloc bonuses, raid/attrition definitions, treaty web |
| P5 | [P&W-pedia — Cities](https://politicsandwar.com/pwpedia/article/Cities) | [O] | 2026-10-22 | City-purchase cost formula (official as published) |
| P6 | [P&W-pedia — Continent](https://politicsandwar.com/pwpedia/article/Continent) | [O] | 2026-10-22 | Continent determines raw-resource access |
| P7 | [P&W-pedia — Infrastructure](https://politicsandwar.com/pwpedia/article/Infrastructure) · [Land](https://politicsandwar.com/pwpedia/article/Land) · [Population](https://politicsandwar.com/pwpedia/article/Population) | [O] | 2026-10-22 | Improvement slot per 50 infra; land's density/disease/farm effects; population–commerce income |
| P8 | [P&W-pedia — Improvements](https://politicsandwar.com/pwpedia/article/Improvements) · [Coal Power Plant](https://politicsandwar.com/pwpedia/article/Coal-Power-Plant) | [O] | 2026-10-22 | Improvement categories, power/coal/upkeep example |
| P9 | [P&W-pedia — coal/oil/bauxite/uranium/munitions factory pages](https://politicsandwar.com/pwpedia/article/Coal-Mine), [Oil](https://politicsandwar.com/pwpedia/article/oil), [Bauxite](https://politicsandwar.com/pwpedia/article/bauxite), [Uranium Mine](https://politicsandwar.com/pwpedia/article/Uranium-Mine), [Munitions Factory](https://politicsandwar.com/pwpedia/article/Munitions-Factory) | [O] | 2026-10-22 | Official per-building production figures for these buildings |
| P10 | [P&W-pedia — Food](https://politicsandwar.com/pwpedia/article/food) | [O] | 2026-10-22 | Food as a produced/consumed resource; 33% income penalty for starvation; seasonal +20%/−20% |
| P11 | [P&W-pedia — Domestic Policy](https://politicsandwar.com/pwpedia/article/Domestic-Policy) | [O] | 2026-10-22 | Policy modifiers incl. Open Markets +1% |
| P12 | [P&W-pedia — Basics of Econ](https://politicsandwar.com/pwpedia/article/Basics-of-Econ) · [Tax Brackets](https://politicsandwar.com/pwpedia/article/tax-brackets) | [O] | 2026-10-22 | Alliances' banks/grants/city circles; tax brackets (monetary + resource shares) |
| P13 | [P&W-pedia — Alliance Ranks](https://politicsandwar.com/pwpedia/article/Alliance-Ranks) | [O] | 2026-10-22 | Leader/2iC/High Gov/Low Gov as customary roles; internal govt varies |
| P14 | [P&W-pedia — Basics of War Strategy](https://politicsandwar.com/pwpedia/article/Basics-of-War-Strategy) · [War Policy](https://politicsandwar.com/pwpedia/article/War-Policy) | [O] | 2026-10-22 | War types; blitz strategy; policy-change cooldown (60 turns) |
| P15 | [Community wiki — Resources](https://politicsandwar.fandom.com/wiki/Resources) | [C] | 2026-10-22 | 7 raw + 4 manufactured classification of the 11 tradeable resources |
| P16 | [Community wiki — Nation Formulas](https://politicsandwar.fandom.com/wiki/Nation_Formulas) | [C] | 2026-10-22 | Community-reported city-income formula (not verified as current) |
| P17 | [Community wiki — War](https://politicsandwar.fandom.com/wiki/War) | [C] | 2026-10-22 | 5 offensive/3 defensive war slots; 60-turn max war; attack outcome labels; ground/air control states incl. blockade; resistance-to-zero as the win condition; peace-offer mechanic |
| P18 | [Community wiki — Nuclear Weapons](https://politicsandwar.fandom.com/wiki/Nuclear_Weapons) | [C] | 2026-10-22 | Fallouts; nuke production/limits; treated as community, unverified |
| P19 | [Community wiki — Tradeprice API](https://politicsandwar.fandom.com/wiki/Tradeprice_API) | [C] | 2026-10-22 | Deprecated price-feed description; historical |

### NationStates
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| N1 | [NationStates — Wikipedia](https://en.wikipedia.org/wiki/NationStates) | [3] | 2026-10-22 | Overall shape: issues, 27 classifications/3 axes, WA, regions, no built-in war/trade, roleplay-present |
| N2 | [NationStates Fandom — Issue](https://nationstates.fandom.com/wiki/Issue) | [C] | 2026-10-22 | Issue cadence (default ~6 h, configurable to 12/24/48) and effects, from community documentation |
| — | NationStates official pages (FAQ, API docs, forum) | [O] | **403 — NOT accessed** | Any official claim that depends on these is unverified this pass |

### Cyber Nations
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| C1 | [About The Game](https://www.cybernations.net/about.asp) | [O] | 2026-10-22 | Persistent-world framing, daily taxes, play loops |
| C2 | [About Topics Index](https://www.cybernations.net/about_topics.asp) | [O] | 2026-10-22 | Nation setup choices, govt/religion/currency, 11 govts, 3-day change, improvement/war details, 2,000-action cap, alliance description (player-run), tax/land behavior |
| C3 | [Game Update Log](https://www.cybernations.net/game_update_log.asp) | [O] | 2026-10-22 | Mobile-friendly update 2025-04-04 as evidence of continued operation |
| C4 | [Homepage](https://www.cybernations.net/) · [Stats Screens](https://www.cybernations.net/stats.asp) | [O] | 2026-10-22 | Live operations, stats pages incl. resource distribution |
| C5 | [Community FAQ (Fandom)](https://cybernations.fandom.com/wiki/Frequently_Asked_Questions_about_Cyber_Nations) | [C] | 2026-10-22 | Daily update time claim, peace mode advice, inactivity deletion >25 days, war-range summary — community, not re-verified |
| C6 | [BASICS: Economics Guide (Fandom)](https://cybernations.fandom.com/wiki/BASICS:_Economics_Guide) | [C] | 2026-10-22 | Trade circles (six nations), resource combination bonuses, examples |

### eRepublik
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| E1 | [Official wiki — Main](https://wiki.erepublik.com/index.php/Main_Page) · [Game overview](https://wiki.erepublik.com/index.php/ERepublik) | [C] | 2026-10-22 | The wiki is user-created; overview of world design and version history |
| E2 | [World map](https://wiki.erepublik.com/index.php/World_map) · [War](https://wiki.erepublik.com/index.php/War) · [Wars](https://wiki.erepublik.com/index.php/Wars) · [Battle](https://wiki.erepublik.com/index.php/Battle) · [Resistance](https://wiki.erepublik.com/index.php/Resistance) | [C] | 2026-10-22 | Real-world-derived map, region ownership, war campaign/round structure (90–120 min rounds), conquest/resistance |
| E3 | [Citizenship](https://wiki.erepublik.com/index.php/Citizenship) · [Taxes](https://wiki.erepublik.com/index.php/Taxes) · [Marketplace](https://wiki.erepublik.com/index.php/Marketplace) · [Gold](https://wiki.erepublik.com/index.php/Gold) | [O/C] | 2026-10-22 | Citizenship voting, congress-voted tax laws, dual currency with monetary market |
| E4 | [Multi-accounts](https://wiki.erepublik.com/index.php/Multi-accounts) · [Latest Game Changes](https://wiki.erepublik.com/index.php/Latest_Game_Changes) · [Resource wars](https://wiki.erepublik.com/index.php/Resource_wars) | [C] | 2026-10-22 | Anti-multi rule; version changelog; event history |
| E5 | [Official site](https://www.erepublik.com/en) · [Google Play](https://play.google.com/store/apps/details?id=com.erepubliklabs.erpkmobile&hl=en_US) · [Apple App Store](https://apps.apple.com/us/app/erepublik/id1381347591) | [O] | 2026-10-22 | Still operating; store listings with 2025 updates and gold price tiers |

### Prosperous Universe
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| PU1 | [Official homepage](https://prosperousuniverse.com/) · [About](https://prosperousuniverse.com/about) | [O] | 2026-10-22 | Player-driven economy, no-combat positioning, flexible pace, free/PRO pricing idea |
| PU2 | [Handbook — FAQ](https://handbook.apex.prosperousuniverse.com/wiki/faq/index.html) · [Licenses](https://handbook.apex.prosperousuniverse.com/tutorials/current-tutorials/06-licenses/index.html) · [PRO page](https://prosperousuniverse.com/premium) | [O] | 2026-10-22 | FREE/PRO/BASIC distinctions, no-auto-renew, PRO feature list (Local Markets, FX, corp founding, contracts) |
| PU3 | [Handbook — Trading](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/trading/index.html) · [Production](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/production/index.html) · [Contracts](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/contracts/index.html) · [Efficiency factors](https://handbook.apex.prosperousuniverse.com/wiki/efficiency-factors/index.html) | [O] | 2026-10-22 | Exchange-specific order books, production recipes/efficiency, contract shipping |
| PU4 | [Press kit (simulogics)](https://press.simulogics.games/prosperousuniverse/) · [Steam listing](https://store.steampowered.com/app/1761220/Prosperous_Universe/) | [O] | 2026-10-22 | Developer identity and design philosophy |

### Sim Companies
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| S1 | [Terms and conditions](https://www.simcompanies.com/terms/) | [O] | 2026-10-22 | Developer identity, F2P + in-game purchase status |
| S2 | [Steam listing](https://store.steampowered.com/app/2253720/Sim_Companies/) · [Google Play description](https://play.google.com/store/apps/details?id=com.simcompanies.simcompaniespwa&hl=en_US) | [O] | 2026-10-22 | Core loop, asynchronous/competitive framing, retail-vs-wholesale trade-offs, quality-research concept (Q0/Q1…) |
| S3 | [Research (Fandom)](https://simcompanies.fandom.com/wiki/Research) | [C] | 2026-10-22 | Quality-ladder concept; numbers treated as potentially outdated |
| — | simcompanies.com FAQ / guides / encyclopedia | [O] | **App-shell only — NOT fully readable** | Any precise fee/rate claim is unverified this pass |

### Additional games
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| A1 | [eDominations "Short Look"](https://edominations.com/en/article/21642/SHORT%20LOOK%20TO%20EDOM%C3%84%C2%B0NAT%C3%84%C2%B0ONS) · [Latest Updates](https://edominations.com/en/latest-updates) | [O] | 2026-10-22 | Modules overview, live operation |
| A2 | [eDominations wiki — Elections](https://wiki.edominations.com/elections/) · [Companies](https://wiki.edominations.com/companies/) · [Trading Center](https://wiki.edominations.com/trading-center/) · [War](https://wiki.edominations.com/war/) · [Alliance](https://wiki.edominations.com/alliance/) | [O] | 2026-10-22 | Elections/cabinet powers; production/trade; 24-h battles/3×8-h rounds; alliance & campaign-of-the-day; gold costs |
| A3 | [Earth Empires homepage](https://www.earthempires.com/) · [Rules](https://www.earthempires.com/rules) | [O] | 2026-10-22 | Server formats, clan orientation, anti-multi/automation rules, live snapshot |
| A4 | [Cantr II homepage](https://www.cantr.net/) · [Rules](https://cantr.net/en/index.php?page=rules) | [O] | 2026-10-22 | Player-authored society, slow-paced, 100% free |
| A5 | [Cantr II wiki — Game Finances (2013)](https://wiki.cantr.net/index.php/Game_Finances) | [C] | 2013-modified; read 2026-10-22 | Donations-only funding (dated) |
| A6 | [Utopia homepage](https://utopia-game.com/shared/) | [O] | 2026-10-22 | Kingdom teamwork framing; live site |
| A7 | [Cold War 2 creator page](https://riseofthewhitesun.com/index.php/our-other-games/) · [Game site](https://cold-war2.com/) | [O] | 2026-10-22 | Set aside: multiplayer nation fit not established |

### Hosting/operations (used in Section 6)
| # | Source | Type | Access | What it supports |
|---|---|---|---|---|
| H1 | [Cloudflare Workers — Limits](https://developers.cloudflare.com/workers/platform/limits/) | [O] | 2026-10-22 | 100k requests/day free plan; 10 ms CPU per request; 50 ms CPU per Cron Trigger invocation (free) |
| H2 | [Cloudflare D1 — Pricing](https://developers.cloudflare.com/d1/platform/pricing/) | [O] | 2026-10-22 | 5M rows read/day, 100k rows written/day, 5 GB free tier |
| H3 | [Cloudflare D1 — Limits](https://developers.cloudflare.com/d1/platform/limits/) · [FAQ](https://developers.cloudflare.com/d1/reference/faq/) | [O] | 2026-10-22 | Account storage 5 GB free; 7-day Time Travel; 10 GB per-database cap |
| H4 | [D1 changelog 2026-09-01](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/) | [O] | 2026-10-22 | Free-tier query *failure* enforcement since 2026-09-01 |

*(Other web-search-derived snippets (e.g., third-party pricing blogs) were used only as corroboration and are not relied on for any claim in this report.)*

---

## Section 10 — Handoff to Prompt 2

Concise findings summary for the next research task:

1. **Constraints validated.** Browser-based, persistent, no-tab-required, server-driven tick is proven by P&W's 2-hour turn (12/day) and Cyber Nations' daily cycle; eRepublik/eDominations show heavier, event-based alternatives we should probably not copy.

2. **Closest analogues per system we intend:**
 - Nation progression: P&W cities/infrastructure (abstract unit model) — the closest working analogue for a mapless nation grown through "network position" rather than territory.
 - Economy with interdependence: P&W raw/manufactured split with geographic lock (mechanism needs a *non-map replacement*); CN resource circles (cooperative combination design); PU's localized exchanges (spatial price differentiation → could become network-position differentiation in our design).
 - Politics: three models identified (light modifiers / heavy institutions / social roleplay); earlier-stage guidance is to favor the lighter end for v1.
 - Diplomacy: P&W's in-game treaty objects + public treaty web vs CN's social-only; the choice between encoded and social diplomacy is open and should be decided in later stages.
 - Alliances: P&W's ranks/permissions/limitations, banks, taxes, supply/MMR rules; CN's off-game self-organization as the contrast case. Key unresolved: how deep in-game alliance supply/tax tools should go.
 - Warfare: abstract duel-war model (P&W) proven; features worth studying: war types, resistance end state, loot/destruction, blockades, cooldowns/vacation-mode/beige-like protection, peace offers; **values unverified/community-sourced — do not reuse numbers without re-checking.**
 - Time/action budget: P&W war-action and CN per-front daily limits; OP must be designed fresh.

3. **Open design conflicts to resolve in later stages:** in-game market vs direct trade (or both); whether a treaty-web visualization is worth early investment; the depth of domestic politics; whether OP is a single general-purpose budget or per-system budgets; how cooperation-resource bonuses (CN-like) coexist with a market (PU/PW-style).

4. **Operational constraint to carry forward:** Cloudflare free tier limits, especially D1's **100,000 row writes per day**, make per-turn write-batching an early architectural priority; scheduled-tick idempotency patterns (state-claimed → committed) are the standard answer to the "reliable, no duplicate, no missed" requirement.

5. **Highest-value next research step:** source-level verification of the current official documentation for the *war* and *market* systems of P&W (the current closest reference), and a deeper check of availability/access for any off-game coordination plugins we'd need (Discord/alternative), before any mechanics are drafted.

---

### Report status footer

- **Research completion status:** Complete (Prompt 1 scope). Does not cover Prompt 2.
- **Games investigated:** Politics & War, NationStates, Cyber Nations, eRepublik, Prosperous Universe, Sim Companies, eDominations, Earth Empires, Cantr II, Utopia (+1 set aside: Cold War 2).
- **Important research limitations:** official NationStates pages inaccessible (403); Sim Companies in-app official pages app-shelled (unreadable this pass); exact P&W current formulas/community-maintained figures flagged as such; all web coverage is documentary — no hands-on testing of any game; competitor hosting and population data remain unknown and were not asserted.
- **Unresolved questions:** listed in Section 8, classified High/Medium/Low for later stages.
- **Recommended next action:** proceed to Prompt 2 with the Section-10 handoff summary; treat the P&W war/market/formula verification as the highest-value follow-up inside Prompt 2's own scope.
- **Document version:** 1.0. Prepared 2026-10-22.
