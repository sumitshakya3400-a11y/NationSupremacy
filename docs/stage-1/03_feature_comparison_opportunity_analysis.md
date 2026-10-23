# STAGE 1 — PROMPT 3: FEATURE COMPARISON AND OPPORTUNITY ANALYSIS

**Project:** Browser-based persistent multiplayer nation-strategy game ("the project")
**Document:** `docs/stage-1/03_feature_comparison_opportunity_analysis.md`
**Version:** 1.0 — prepared 2026-10-22 (all web sources accessed 2026-10-22 unless otherwise noted)
**Builds on:** [01_competitor_research.md](01_competitor_research.md) (Prompt 1) and [02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) (Prompt 2), both read in full; finding IDs F-xxx refer to Prompt 2 Section 9.
**Status:** Complete for Prompt 3. Does not begin Prompt 4, the Game Design Bible, or any implementation.

---

## Section 1 — Executive summary

### The most important similarities and differences across researched games

**Similarities (genre-wide, well-evidenced):** every deeply studied persistent nation game combines (a) a server-resolved world clock (tick or cadence), (b) offline accrual of income and obligations, (c) player-to-player economic interdependence, and (d) alliances or equivalent teams as the durable social unit. News feeds, rankings, anti-grief protections, and one-nation-per-player rules also recur everywhere.

**Key differences that matter for design:**

1. **Market architecture is a genuine fork, not a spectrum.** Politics & War (P&W) uses player-created listings manually accepted, with displayed average prices as context (verified this pass — no matching engine); Prosperous Universe runs local **order books** (bids/asks per exchange) alongside **bulletin-board contracts**; Sim Companies combines an exchange (fee-charged, ~3% example rate, buy orders hidden) with fee-free direct contracts. NationStates, eRepublik, and Cyber Nations solve trade far more simply (or socially). The matching-engine choice is the single most consequential economic decision we face.
2. **Treaties are mechanical in very different degrees.** P&W's in-game treaty system is displayed on an official Alliance Treaty Web and is **mechanically enforced exactly once: non-aggression pacts prevent war declarations between treatied alliances** — every other treaty type is a social commitment enforced by reputation (verified on the official [Treaty Web page](https://politicsandwar.com/alliances/treatyweb/)). Cyber Nations has no in-game alliance objects at all (community wiki: alliances function "almost entirely outside game mechanics"); OGame's own diplomacy page states there is **no official treaty interface**. This shows diplomacy can be encoded minimally and still support a rich political culture.
3. **War action economy differs structurally.** P&W war is a **Resistance race** (each side starts at 100, reduced by attacks; first to zero the opponent's resistance wins) governed by a **Military Action Points (MAP)** budget: start 6 MAPs, +1 per 2-hour turn, variant policies modify the start (Blitzkrieg 7 / Fortress 5), attacks cost differing MAP amounts (verified from the community War page and official NAV page). Cyber Nations uses simpler daily limits (2 attacks/day per front, nukes locked 24h). eRepublik/eDominations use timed battle *rounds* requiring live participation — structurally dependent on a map and troop economy we do not have.
4. **Alliance tooling is where games most clearly diverge in ambition.** P&W: up to 9 position levels and 15 documented permissions (bank view/withdraw, taxes, treaties, applicant management, etc.) in-game. eDominations: alliance creation costs 100 gold, and its shared-battle incentive (**Campaign of the Day**, +5% damage to qualifying members on *either* side of the sponsored battle) is unique. Utopia: elected Monarch + Stewards, war forum, relation-escalation mechanics. Cyber Nations: none in-game by design.
5. **Politics is mechanically loaded in some games, absent in others — the genre fork from Prompt 1 stands.** (eRepublik/eDominations: congress/elections; P&W: policy toggles only; NationStates: whole game is politics; CN: flavor choices.)

### The strongest feature-design patterns

- **Budgeted actions regenerate on the shared clock** (P&W MAPs: +1/turn, cap 12) — action scarcity is expressed in the same currency as the world clock. This directly answers our two-hour turn design question (Category G).
- **Reference prices let player-set prices stay legible** (P&W average prices updated at day end; Sim Companies reference-price pages) — price discovery without real-time engines.
- **Sponsorship as coordination** (eDominations COTD): leadership picks a shared target; members gain a mechanical bonus for joining. A cheap, effective, mapless-compatible collective-war coordination tool.
- **Protection phases as a war-state machine** (P&W beige: 2 days no-declaration + a documented July 2025 recruitment buff while beige; vacation mode with explicit anti-abuse rules). Protections that are *states with exits*, not unconditional shields.

### The most promising original opportunities

The leading candidates (full register in Section 10): the **world-network view with treaty visualization** (FO-004), **transparent turn reports** (FO-002), **a MAP-style military action budget** as the provisional OP basis (FO-010), **war types + a peace/settlement flow** (FO-011), **a listings market with reference prices** (FO-009), **resource interdependence without geography** (FO-013), and the **in-context teaching layer** (FO-001). None is decided; all are candidate opportunities with evidence attached.

### The largest implementation risks

- **Database write throughput** on Cloudflare D1's free tier (100k rows/day enforced) versus 12 turns/day of scheduled processing — the top architecture risk carried from Prompt 1 Sections 6.1 (re-checked, unchanged, and reaffirmed).
- **Market-integrity engineering**: a player market with cash-and-resource settlement requires atomic transactions, anti-multi and anti-automation (bot) measures — every market-running game studied bans trade automation and machine-enforces one-nation-per-player.
- **War-system balancing**: P&W's community-maintained war math is elaborate and its exact formulas are *not* officially documented; building our own abstract war without reproducing their formulas is a real design-scale challenge (Prompt 1 Section 7.7).
- **Complexity budget**: Prompt 2's strongest documented weakness (F-010 jargon/learning-curves) is partly caused by feature interconnection; every cross-system opportunity in Section 6 adds rule surface.

### The most important unresolved questions

Leading with full lists in Section 12: (1) which catch-up/late-entry philosophy fits a persistent 2-hour-turn world (F-012); (2) how resource interdependence is generated without geographic scarcity (Prompt 1 Section 7.2); (3) how transparent to make economic data (profitability surface vs trader skill; F-022 context); (4) how much treaty type vocabulary to encode mechanically (Section 9 below); (5) the precise 12-turn/day write budget per nation (architecture stage).

---

## Section 2 — Previous research reviewed

### Documents and locations confirmed

- [01_competitor_research.md](01_competitor_research.md) — Prompt 1, v1.0, 624 lines. **Read in full this session** (see its own source register: sources P1–P19, N1–N2, C1–C6, E1–E5, PU1–PU4, S1–S4, A1–A7, H1–H4).
- [02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) — Prompt 2, v1.0, 511 lines. **Read in full this session.** Finding IDs F-001…F-029 reused below.

### Which findings were reused

- P&W's 2-hour turn (official glossary) as the schedule precedent — reused throughout.
- Prompt 1 Section 6 (Cloudflare Workers/D1 limits, turn-engine integrity patterns) — reused in Sections 8/9; no re-verification needed this pass (the docs are 2026-10-22 and anchor the analysis).
- Prompt 1's per-game profiles (Sections 3.1–3.9) and genre patterns (Section 5) — reused as the feature matrix's baseline so this report adds detail rather than duplicating them.
- Prompt 2's finding IDs — cited wherever a feature comparison connects to player experience evidence.

### Claims rechecked (new verified, this pass)

Three focused verification passes were run against gaps Prompt 1 itself flagged (its Section 8):

| Prompt-1 gap | Recheck result |
|---|---|
| P&W market/fee internals (medium-high) | **Partially resolved.** Market is a listing/offer system with player-set prices and displayed average prices; no current market fee verifiable; trade restrictions (<30-day nations, shared-network nations) and ban on automated trading confirmed from official rules. Remaining unknowns listed in Section 12. |
| P&W alliance permission matrix (Prompt 1 flagged the community page 403) | **Resolved via official source.** [Alliance Positions page](https://politicsandwar.com/pwpedia/article/Alliance-Positions): unlimited positions, 9 levels, Leader/Heir/Officer/Member defaults, 15 named permissions. |
| P&W war action economy | **Partially resolved.** Resistance (start 100 each) + MAP (start 6, +1/turn) verified; P&W-pedia documents a 4-MAP naval attack and the official Treaty Web text verified directly. Exact damage/probability formulas still community-only, not verified (and not needed at this stage). |

### Gaps that remain (carried forward)

P&W's exact market schema/fee; P&W current damage formulas; Sim Companies in-app pages (unreadable again this pass — claims are labeled provisional where indexed-text-only); all Discord-layer community norms (unresearchable without accounts).

---

## Section 3 — Research methodology and source quality

### What was newly researched this pass

Three parallel focused investigations plus two direct verifications:

1. **P&W feature mechanics** (market/fees, war declaration & MAP economy, alliance permissions) — official P&W-pedia first.
2. **Alliance tooling across games** (P&W, Cyber Nations incl. the 2011 Tournament-Edition distinction, eDominations, Utopia; OGame discovered as an additional operating comparison).
3. **Market/trading system mechanics** (Prosperous Universe handbook: exchanges, local markets, contracts; Sim Companies official pages — app-shell again; indexed-text claims labeled provisional).
4. **Direct verifications by the analyst:** [P&W Treaty Web](https://politicsandwar.com/alliances/treatyweb/) and the community [War page](https://politicsandwar.fandom.com/wiki/War) (Resistance + MAP section) read directly.

### Evidence hierarchy used

1. Official documentation/rules (P&W-pedia, P&W rules, PU handbook, official treaty web).
2. Official changelog/log (eRepublik app-store 2025 updates, CN 2011 Tournament Edition log).
3. Maintained community wikis (P&W Fandom, CN Fandom, Utopia Fandom), always labeled [C].
4. Credible independent analyses (from Prompts 1–2 registers).
5. Community discussions/forums (from Prompts 1–2 registers).

### Claim-type classification used in this report

Per the task's Section 5.4: **Verified fact (FV)** (reliable official source), **Reported player experience (FE)** (documented player observation, usually from the Prompt 2 register), **Analytical interpretation (AI-)** (this report's reasoning), **Design opportunity (DO-)** (possible direction for our game), **Unverified hypothesis (UH)** (requires more evidence). These labels appear on load-bearing claims.

### Limitations

- Sim Companies official in-app pages again app-shelled; their indexed-text claims are provisional.
- No live logged-in testing of any game (unchanged from Prompts 1–2).
- eRepublik/NationStates mechanics rely on Prompt-1-era sources; current-state re-verification was not repeated where the feature comparison did not hinge on it.
- Complexity/feasibility labels in Section 8 are analyst judgments, not measurements.

---

## Section 4 — Master feature comparison matrix

Label key for evidence state: **FV** verified fact (official or directly read source); **NF** not found in reviewed documentation (absence of our evidence, absence not asserted); **CA** confirmed absent (officially established absence); **UNK** unknown/inaccessible; **NA** not applicable to that game/column. Sources abbreviated as `[P#]` `[C#]` `[E#]` `[PU#]` `[S#]` per Section 13; `[F#]` = Prompt 2 finding IDs.

### 4.1 Nation development / progression

| Feature | P&W | Cyber Nations | eRepublik / eDominations | NationStates | Prosperous Universe / Sim Companies | Key differences |
|---|---|---|---|---|---|---|
| Nation/entity creation choices | Continent (resource access) [P6 FV prior] | Government/religion/currency, re-choosable every 3 days [C2 prior FV] | Citizenship in a real-world country; class/jobs [FV prior] | Ideological issue choices from birth [FV prior] | Company name/industry start [FV prior] | P&W's continent choice is a lasting strategic input; CN's are happiness modifiers; PU/SC choices are corporate identity |
| Core development unit | Cities (steep cost curve) [P5 FV] | Improvements (5/type cap) + Wonders (1/30d, steep upkeep) [C2 FV] | Companies (production units) [FV prior] | None — statistics drift [FV prior] | Facilities/bases [FV prior] | Same "build units" idea, very different cost curves and strategic meaning |
| Research/tech | No dedicated research/tech system traceable in the reviewed documentation (Prompt 1 documents cities/improvements only) [NF prior; untraceable placeholder source removed 2026-10-22] | not applicable (CA: no research system documented) [NF prior] | not applicable [NF] | CA [CA prior] | SC: quality ladder Q0…Q99 [FV-ish community, then PU: efficiency factors] [C/PU3] | Research is the differentiator for the sim-economy games; nation games mostly lack it |
| Progression limiting | Population/commerce floors [P7 FV] | Citizen counts gate improvements [C2 FV] | Gold costs + citizenship [FV] | n/a | Ships-in-flight caps, licence gates (PU FREE = max 2 ships in flight) [X3 FV verified — the handbook states "FREE users may not have more than 2 ships in flight simultaneously"] | PU gates by subscription tier — a unique paywall-gated design |
| Long-term goals | City count, wonders [NF-lite] | Wonders [FV] | Territory/elections [FV] | Classifications, WA standing [FV prior] | Market position, quality [FV] | Territory-based goals are map-games' privilege; others use accumulation/status |

### 4.2 Economy and trade

| Feature | P&W | Cyber Nations | eRepublik / eDominations | NationStates | PU / Sim Companies | Key differences |
|---|---|---|---|---|---|---|
| Currency | National cash, single global value [P1 FV] | National cash [FV] | Dual: gold + local (eRep) / gold-weighted (eDom) [FV] | n/a (CA) | SC in-game dollars; PU: multiple + credit [FV] | Dual-currency is a map-game device; we have no map and shouldn't copy that rationale |
| Resource system | 11 tradeables: raw (continent-locked unless food) + manufactured [P15/FV] | Resources assigned, traded in "circles" for bonus combinations [C6/FV] | Country resources/regions (eRep) [FV] | CA | PU: extracted/refined chains; SC: many products [FV] | Scarcity location: geography (P&W/eRep) vs composition (CN circles) vs recipes (PU/SC) |
| Player trade construction | Player listings/offers, manually accepted [FV this pass] | Mutual-approval resource trades + optional circle coordination [FV] | Marketplace orders + monetary market [FV prior] | CA (trade is social/off-game) | PU: CX order book + LM bulletin contracts; SC: exchange + direct contracts [FV] | The biggest fork — see Section 5.2 |
| Market fees/tax | No current fee verified [NF this pass] | no resource-spec tax verified [NF] | Congress-voted import/sales taxes (eRep) [FV prior] | NA | PU: LM ad fee set by governor; CX fee NF; SC: exchange fee (~3% indexed example, variable), contracts fee-free [FV-provisional] | Fees are policy levers, not architecture |
| Price legibility | Average prices, updated at day end [FV this pass] | none verified [NF] | market listings with prices [FV prior] | NA | PU: bid/ask spread per CX; SC: reference prices page [FV] | Reference prices are the adapter between player pricing and player understanding |
| War↔economy interlock | Loot/blockades, resource destruction, food-and-war interplay [FV prior] | inactivity deletion is the harshest drain [FV-ish, community] | damage consumes food/weapons [FV] | NA | PU n/a; SC competitive-only | War economies are a nation-game device; sim games avoid combat deliberately |

### 4.3 Politics and governance

| Feature | P&W | Cyber Nations | eRepublik/eDominations | NationStates | Notes for our project |
|---|---|---|---|---|---|
| Government/system choices | Policy chips (mod-level toggles) [FV prior] | 11 governments, 3-day rechoice [FV prior] | party/election/congress systems [FV] | issue-driven classification | FV |
| Approval/stability | happiness/stability numbers [FV-lite] | happiness via government/religion fit [FV prior] | popularity/election outcomes [FV] | stats axes | FV |
| Factions/parliament | CA in-game; social only | CA | real: congress w/ tax law powers [FV] | n/a (roleplay) | FV — mechanically consequential politics is map-game territory; NationStates does it socially |
| Political consequences of war | stability effects of loss (community-described; current status unknown) | UNK | war affects elections (eRep) [FV prior] | NA | NF |

### 4.4 Diplomacy and international relations

| Feature | P&W | Cyber Nations | eRepublik/eDominations | NationStates | PU/SC/notes |
|---|---|---|---|---|---|
| In-game treaty objects | 10 types incl. NAP, PIAT, MDP, MDoAP, protectorate; visible treaty web; auto-operated in-game [FV this pass] | CA (treaties exist only as conventions) [FV-ish community] | alliances (100-gold creation) + embargoes by president [FV] | embassies (inter-regional), text treaties [FV prior] | P&W only mechanically enforces NAPs; all else is social [FV] |
| Sanctions/embargoes | yes, embargoed trade states [FV] | no equivalent verified [NF] | presidential embargoes [FV] | NA (in some sense — WA sanctions as RP) | FV |
| Visualizations | alliance treaty web [FV this pass]; world map, radiation map | none verified [NF] | world map, battle pages [FV] | none (region pages only) | Mapless network view is our design space (Prompt 1 §7.2) |
| Diplomatic prerequisites | war-declaration ranges, treaty blocks on war [FV] | UNK (inactivity-window effect on war targets) [NF] | citizenship eligibility, alliance rules [FV] | NA | P&W shows mechanical diplomacy blocks are viable |

### 4.5 Alliances and collective organization

| Feature | P&W | CN (standard; league variant) | eRepublik/eDominations | Utopia | OGame (new comparison, not deep) |
|---|---|---|---|---|---|
| Create/join | in-game; alliance governments often handle recruitment off-game (Discord) [FV] | player-run only [FV] | president-foundable (100 gold eDom) [FV] | kingdom (25 provinces max) [FV-ish C] | alliances/ranks [FV] |
| Roles/permissions | 15 permissions × 9 position levels; Leader/Heir/Officer/Member defaults [FV this pass] | none legal in-game (CN TE 2011 had richer but explicitly a tournament edition) [FV] | president/alliance leadership; sanctions [FV] | Monarch + 2 Stewards + elections [FV-ish C] | Founder/Admiral/Officer delegations [FV] |
| Shared treasury | bank with loans/grants as *administered programs*, not built-in workflows [FV this pass] | no bank verified [NF] | not verified [NF] | not verified [NF] | alliance depot as fleet staging [FV] |
| Taxes of members | tax brackets on money+resources, with default bracket and Bank Access gating [FV this pass] | none legal [FV] | UNK [NF] | UNK [NF] | CA-ish [NF] |
| Collective war coordination | treaties + war states, alliance-level slots; no official "one shared target" mechanic [NF] | none in-game [FV] | eDom **COTD** +5% bonus, either side of sponsored battle [FV this pass] | war forum, relations escalation thresholds [FV-ish C] | **ACS** joint attacks + Alliance Depot mutual defense positioning [FV this pass] |
| Internal governance | configurable constitutions in practice (off-game) [FV prior] | fully off-game | president/congress cycles [FV] | elected Monarch + Stewards [FV-ish C] | rank system [FV] |

### 4.6 Warfare and military strategy

| Feature | P&W | CN | eRepublik/eDominations | Utopia | Notes |
|---|---|---|---|---|---|
| War entry requirements | war types (Ordinary/Raid/Attrition) at declaration; score-range tools; treaty-web NAPs auto-block war; repeat-declaration cooldown community-reported at 12 turns (~24h) [FV/Cooldown this pass — community source for cooldown] | land/infrastructure targets; nukes locked 24 h post_declaration [FV-lite] | region-locked fronts; alliance alliance gates [FV] | relations thresholds gate war [FV-ish C] | All workable without a map |
| Action economy | **Resistance race** (100→0) + **MAP** (start 6, +1/turn, cap 12, policy modifiers; naval attack 4 MAP) [FV this pass] | 2 attacks/day/front (+missiles/nukes limits) [FV-lite prior] | battle rounds (eRep 90–120 min; eDom 24h/3×8h) requiring live participation [FV] | attack waves + magic/thief ops per game hour [FV-ish C] | P&W's MAP is the cleanest budgeted war action economy and turn-locked |
| Defense/counterplay | peace offers, defensive war buffs (Fortress/Blitzkrieg policy), reinforcements via defensive policies [FV-lite] | minimal counterplay documented [NF] | region defence, resistance wars [FV] | war stances, forts, elite rotations [NF] | genuine strength/weakness — most TF open |
| Intelligence/spies | spies as military unit [FV] | spies [FV-lite] | UNK [NF] | thieves = intelligence operations [FV-ish C] | coverage thin across all games; confidence low |
| War resolution & aftermath | resistance 0 (victory) → peace offers/beige (2-day no-declaration, + a documented buff while beige without wars [FV this pass]) | infrastructure damage persists; beige-threshold UNK | territory change (map-bound) | land/gold gains, war scores, relations reset | meaningful aftermath question for us: Prompt 2 F-012 (catch-up) ties into it |

### 4.7 Time, actions and multiplayer activity

| Feature | P&W | CN | eRepublik/eDominations | NationStates | PU/SC |
|---|---|---|---|---|---|
| Shared clock | 2h turns; server header shows "Next turn in x:xx"; per-turn revenue/MAP [FV] | daily cycle [FV prior] | event-clock battles [FV] | user-configurable issue cadence [FV prior] | continuous market/order timing |
| Actions between turns | purchases, trades, attacks| one collection/day | battle rounds | issue answers | order mgmt (real-time, uncoupled from clock) |
| Offline progression | full (nation accrues, losses accrue) | yes (with 25-day inactivity deletion caveat) | yes but war participation requires being online | full (issues per cadence) | full |
| Scheduled-processing surface | per-turn revenue, MAP regen, war state checks, buffs (beige buff is per-day-recruitment), Day rollover [A-interpretation] | daily wealth/war | round timers (in-battle), monthly elections | daily data dumps | per-second/market engine (continuous) |
| Sessions pressure | testimonials show "all-day-integrated" discussion (Prompt 2 F-019 family) | lower (once-daily) | high (battle windows) | lowest | medium |

### 4.8 Social/onboarding

| Feature | P&W | CN | eRepublik/eDominations | NationStates | PU/SimCo |
|---|---|---|---|---|---|
| Teaching | big glossary; forum tutorials do the teaching [FV prior] | guides do it [FV-lite] | in-game articles written by veterans [FV] | none in-game; community wikis [FV] | PU: handbook; SC: official FAQ (shell) + community |
| Notifications/digests | news feed + graphs; eRep summary approach [FV prior] | UNK | yes [FV] | issues/telegram | PU in-game mail; SC notifications [FV-lite] |
| New-player protection | vacation mode; beige; trade/embargo restrictions for new nations; war rules against slot filling [FV this pass] | "peace mode" in traditional advice [FV-lite] | new-citizen protection was historically claimed; UNK current [NF] | WA member rules etc [FV prior] | SC: newcomer onboarding helper [FV-lite] |

**What the matrix says about our design space:** we inherit a working template (P&W's turn-clock, action budgets, protection states, alliance permissions, treaty web) but must deliberately re-place the *geographic* scarcity engine (P&W's continent-locked raw resources) that our mapless design removes — this remains the project's central original-design problem (Prompt 1 §7.2). PU/SC show markets can be simpler than real-time engines when price legibility (reference prices, spreads) is built in.

---

## Section 5 — Category-by-category analysis

Label prefixes per Section 3.

### 5.1 Nation development

**How the systems actually work ([FV everywhere]).** P&W growth is *serial-accumulative*: cities are bought on a steeply rising cost curve (official example formula), each unlocks improvement slots gated by infrastructure which itself raises upkeep — progression is a resource-allocation ladder where pacing choices matter (small cities first, larger commitments later). CN growth is *bill-capped*: improvements exist in at most 5 copies each, gated by citizens, each with recurring bills and wonders adding unique permanent one-offs with severe upkeep. eRepublik-style games grow through *companies* and territory simultaneously. PU/SC grow through *facilities + recipes*, where inputs come from other players.

**What creates meaningful choices (AI-):** each model yields choices only when build options trade against each other (upkeep vs income; cap boundaries; city-count trade-offs). P&W's system gives a strong *planning* loop (multi-city multi-turn), CN gives a strong *portfolio* loop (slot caps force variety), PU/SC a *chain* loop (you must interact with other players to complete value). Do not conclude which is better — evidence only says that *choices exist when caps/upkeep force trade-offs*, matching Prompt 2's F-002 finding that "measurable optimization is intrinsically rewarding" [FE].

**Repetitive-optimization risk (AI-).** Prompt 2's F-001/F-002 tension: P&W's blog-evidence celebration of "tweaking numbers to perfection" coexists with its "Boring game" thread when the social layer is thin. A turn-report-driven design must provide *new* information per turn, not just larger numbers (feeds into FO-002, FO-004).

### 5.2 Economy and trade

**Architecture divides, verified this pass:**

- **P&W: listings market.** Players post offers at per-unit prices, others accept; average prices are displayed reference data updated daily. No matching engine, no verified fee. Player-set pricing plus reference data + restrictions (young nations, shared networks) + automation bans. This is *very browser-appropriate*: no real-time engine, low D1 write cost, legible.
- **Prosperous Universe: dual system.** Exchange (order books per location with spreads) + **Local Markets** (governor-ad-fee'd bulletin boards where acceptance creates a *contract*, not a transfer). Contracts carry missing-deadline/breach consequences and a trust rating. This shows *contracts can encode trust* — an intriguing tool for our diplomacy layer, at the cost of more bookkeeping UI.
- **Sim Companies: exchange + contracts.** Exchange fee (~3% indexed example, variable) when orders fill; buy orders hidden from others; contracts fee-free and half the transport requirement. Much of this is provisional because official pages wouldn't render.

**Do-not-conclude (UH):** we should not assert "P&W's model has no fee therefore P&W economy is fine without fees." Overall: fees, matching, and settlement rules are *tunable policy options*, not the architectural fork. The fork is: **(a) player listings (cheap, legible, but slow discovery)**, **(b) order books with matching (fast, standardized, but real-time-ish + riskier integrity)**, **(c) contracts/escrow (trustable, but bookkeeping-heavy)**. This prompt's job is to say — all three are precedented; the second one is more expensive; the first + third mix is what PU does (orders for price discovery, contracts for negotiated deals) — **a combination worth evaluating for us** (FO-009, FO-022).

**Economy↔war interlocks (FV in P&W):** blockade halts target market trading/bank transactions; aerial attacks destroy money; naval blockades matter; P&W's official text is the clearest demonstration that *war is an economic event*. For us, "economy as war consequence" is a promising but careful candidate: it makes war impactful without geographic fronts (see Section 6, XL-3).

### 5.3 Politics and governance

**Verified landscape:** the *shift* is between **light policy toggles** (P&W; ±% modifiers, once-per-cooldown changes — our cheapest option), **hidden-preference identity choices** (CN governments/religion with "citizen happiness"), **real elective institutions** (eRep/eDom congress+elections with real consequences), and **pure roleplay** (NationStates). Prompt 2's F-015 (P&W "centrally war" complaint) plus NationStates' strong community-value evidence [FE] together suggest a *middle path* our genre-comparison has not tested mechanically: **policy choices with real-but-bounded consequences, without an election apparatus** (see Section 6, XL-1).

### 5.4 Diplomacy and international relations

**Encoding spectrum (FV):** from CN (nothing in-game) through OGame (alliance objects + ACS joint attacks; no treaty interface) through eDominations (alliance object + sanction powers) to P&W (a full treaty taxonomy + treaty web + NAP mechanical execution). Two lessons: (1) **the minimal viable encoding is 'NAP blocks war' + a visible graph of relationships** — everything else can be social; (2) a visible treaty web distinguishes "who can/can't fight whom" instantly, which is a mapless game's *reputation surface* (our world has no borders, so relationships ARE the geography — the strongest original-opportunity anchor; FO-004).

### 5.5 Alliances and collective organization

**Verified.** P&W: 15 permissions across limitless custom positions (9 levels), taxes on money and resources with brackets + Bank-Access gating, loans/grants as administered (not automated) programs, treaty management as a permission. eDominations: president-founded alliances, +5% damage bonus on the COTD battle; leadership sets the shared target; members coordinate via in-game channels. Utopia: elected monarchy with Stewards, war forum, relation-escalation thresholds. OGame: founder/admiral/officer ranks + ACS joint-fleet attacks and depot(defensive staging). Cyber Nations standard: *deliberately game-mechanics-free*, all collective play is off-game social.

**Implications for our alliance systems (AI-):**
- In-game alliance tools work even at P&W's depth, but **they are a large surface** (roles × permissions × bank flows × audit trails). Section 8 rates P&W-style full parity as **High** complexity.
- eDominations' COTD shows **shared-target coordination can be small and mechanical** (a single designation + a bonus modifier). Mapless-compatible, cheap, and caters to Prompt 2's F-018 (alliance admin burden) by *replacing coordination labor with one shared decision* (FO-012).
- Utopia's relation *escalation* (normal→unfriendly→hostile→war) is a pre-war state machine quite compatible with a symbolic network (see Section 6, XL-4).
- Prompt 2 F-013 warns that **alliance routing/funneling** (activity gated behind off-game platforms) creates accountability and continuity risks; F-001 (community) warns that too-thin in-game tooling offloads all coordination value to Discord, where the rules of play are invisible to newcomers. P&W (rich in-game tools) and CN (tools-free) both operate — our design task, deferred to later design stages, is to choose which load the game carries natively (FO-006/007/008 as the native-tooling package).

### 5.6 Warfare and military strategy

**P&W's structural solution [FV this pass, the model our war design should be evaluated against]:**

- Wars are a **Resistance race**: both sides start at 100; each offensive/defensive/air/naval action *reduces the defending/attacking side's* resistance; first to reduce theirs to zero wins (community doc, consistent with official descriptions of war rounds... verify-qualified).
- The war **action economy is MAP**: start 6 (policy-adjustable 5–7), +1 per 2-hour turn, cap 12; attacks cost differing MAP (naval 4). Strategic consequence: a war cannot be "flooded" with attacks in one session; *every side gets one decision-point per 2 hours*. Clean, turn-locked, browser-appropriate.
- **War declaration is rule-gated**: score range (attack/defend ranges via an official calculator; 25%-below/75%-above is community-reported), NAP-treaty mechanical blocking, repeat-declaration cooldown (~24h per community FAQ), designated filters for new/small nations (trade restrictions + anti-slot-filling rules).
- **Post-war states with exits**: beige = 2 days of no new declarations + a 15% recruitment buff while beige-and-warless [FV July 2025 page]; vacation mode = insured absence with explicit anti-abuse conditions.
- Consent limits were *reportedly* the strongest documented [FE] anti-farmer tools — they exist precisely because Prompt 2's F-017 (who is exploited by protection mechanics) and 4-16 (war fairness debates for small nations) are real documented experiences.

**What mapless P&W proves for us (AI-):** geography is NOT required for tactical texture — resource destruction, blockade, peace-offer timing, and alliance coordination are the meat. When our design "war without a map" is started (not this stage), the variables to anchor are: initiation conditions (what disputes start wars), action economy pacing (a MAP-like budget), post-war states (protection/cooldown phases), and *consequences that live in the economy and diplomacy rather than in territory*. **FO-010, FO-011, FO-017 encode this as candidate features.**

**eRepublik-style timed rounds: rejected here** — they depend on territory, live participation windows, and a different action economy; incompatible with the no-map + "no-download live sessions needed at fixed hours" fit our design.

### 5.7 Time, actions and multiplayer activity

**Verified cadence:** P&W 2h/12-turn clock as the only exact precedent of our speed; the server header's "Next turn in" countdown is a UI convention worth copying as a *pattern* (player/planning legibility), not as visual design.

**Prompt-1/Prompt-2-established principle** (Section 6.1 architecture and F-006/F-021 qualitative), carried forward: in a scheduled world, "action scarcity does not come from online time — it comes from budgets that regenerate on the clock." MAP regeneration in P&W is the best instantiation seen (war actions regenerate per turn and cap at 12). Applied to our game, any mapless "Operational Points" system should be paced against the 2-hour turn rather than against online time or pay-to-skip shortcuts (design principles for this are carried into FO-010).

### 5.8 Social features and player experience

Forward-listed to FO-001/002/003/015/016 and the Prompt 2 report Sections 3–5: in the genre, teaching, turn legibility, onboarding flow, re-entry flows, and constant-visible explanation are the genre's biggest under-built surfaces (F-010, F-011, F-023) — no game evidenced doing all five excellently, which *is our opening*.

---

## Section 6 — Cross-system interactions

Each item: **inspired by** → **opportunity** → **risks** → **dependencies** → **test-before-adopt** → **release phase (v1 / later)**.

### XL-1. Domestic policy ↔ economics
*Inspired by:* CN's government/religion→happiness; P&W's Open Markets policy chip (+1% income, once-per-window change).
*Opportunity:* policy toggles that trade a domestic value (stability) against an economic value (income/efficiency), changeable only on turn boundaries; FO-005.
*Risks:* if consequences are purely numerical, it collapses into P&W's *too-thin politics* complaint (F-015); too complex and it becomes eRep's learning-curve tax (F-010).
*Dependencies:* stable economy; stability stat; turn reporting (FO-002).
*Test:* simulate policy values; measure whether a player consistently prefers one "best" policy (a broken pick) — needs later simulation.
*Phase:* v1 possible but **lightweight**; heavy versions later.

### XL-2. War ↔ economy (war as an economic event)
*Inspired by:* P&W blockade/cash-destruction/loot [FV]; food starvation as an income penalty; eRep damage-vs-weapon consumption.
*Opportunity:* our mapless war could make **blockades/market-access restrictions** and **infrastructure destruction** the two headline war effects, so war's impact is legible in economic reports (FO-011, FO-016-relevant). Also: war consumes produced military resources, coupling the trade economy to conflict, as P&W does.
*Risks:* if losses are too punishing or bundle-cascade (losing a war ⇒ total economic ruin), we recreate the genre's punishing-loss frustration (F-026 single-evidence, plus F-012); if too light, war becomes low-stakesleys spam.
*Dependencies:* mature economy; stable war structure; protection systems (FO-003, FO-017).
*Test:* later-stage numeric simulation of "loser's recovery arc".
*Phase:* v1 minimal (one automatic consequence: resource destruction), richer later.

### XL-3. Diplomacy ↔ trade
*Inspired by:* P&W embargoes and trade-restriction states; eRep congress-voted tariff laws.
*Opportunity:* our treaty set could include an **economic treaty type** granting mutual market-access discounts while a **blockade/embargo state** restricts access — both are relationship-graph states, not map states (FO-004 + FO-006).
*Risks:* market access as a poison pill — an alliance could "wall off" newcomer traders; F-013/F-029's alliance-monopoly family. Requires anti-walls-by-design scrutiny.
*Dependencies:* market exists (FO-009); relationship/state engine (FO-004).
*Test:* whether restricted-trade states produce legible player plans (design-stage question).
*Phase:* later (v1 might ship with only the minimal NAP + embargo types).

### XL-4. Alliance structure ↔ pre-war escalation
*Inspired by:* Utopia's relations ladder (normal → unfriendly → hostile → war) — a *state machine* relationship concept; P&W's mechanically-enforced NAPs.
*Opportunity:* our symbolic world could display relationship *heats* in the network view, and gate war declaration behind (a) documented rivalry states, or (b) one side not being protected — making the network view itself the diplomatic status board (FO-004 + FO-017).
*Risks:* over-rigid states could slow resolution; over-permissive states re-open grievance-free farming (F-017).
*Dependencies:* war structure; protection states; relationship graph storage.
*Test:* adversarial walkthroughs of "can this be grief-farmed?" (FO-017's stated goal).
*Phase:* later — v1 only needs the minimum gate set.

### XL-5. Alliance tooling ↔ genre-wide automation debate
*Inspired by:* P&W's 15-permission matrix + loans/grants as non-built-in flows [FV]; Prompt 2 F-018 automation debate.
*Opportunity:* **official bulk actions inside the alliance UI** (multimember resource grants/donations/taxing once per turn) — *legitimating* what third-party botsnde currently do — plus a **tamper-evident treasury audit log** (FO-007/FO-008).
*Risks:* tools can erede strategy (trust: "which actions stay manual"); permissions misconfiguration is a security surface.
*Dependencies:* roles/permissions engine; bank atomiaty per Prompt 1 §6.2; market.
*Test:* permissions-security review (design-stage adversarial walkthrough).
*Phase:* v1 minimal (bank + basic roles); richer later.

### XL-6. Shared battle focus ↔ mapless alliance coordination
*Inspired by:* eDominations COTD (+5% damage on the alliance-sponsored battle, either side) [FV this pass].
*Opportunity:* in a mapless world, alliance leadership periodically sets a "current campaign/shared focus" (a war, a trade initiative, a project) and members earn a *capped* bonus for participating — one shared decision replaces coordination labor (FO-012).
*Risks:* incentivises focus on one thing (a loss of free-choice strategy); bonus must be capped small (like equal-effect +5%) to avoid domination; could be gamed by staging fake campaigns.
*Dependencies:* war/campaign structure; member action accounting.
*Test:* is a small, capped, shared bonus enough to matter? Needs later numeric work.
*Phase:* later.

### XL-7. Research/specialization ↔ long-term economy
*Inspired by:* Sim Companies' quality ladder + PU's efficiency factors (FV prior); CN's re-choosable government identity; P&W's continent scarcity.
*Opportunity:* in a mapless world, **network position substitutes for geography**: resource classes *earned through development/research choices*, not starting geography, could create P&W-style "everyone produces something scarced" interdependence — the answer to Prompt 1 §7.2's open question (FO-013).
*Risks:* permanent specialization (fixed paths) re-creates P&W's veteran advantage; fully fluid specialization destroys identity. Candidate mix: **initial choice + slow re-specialization** (a staged path, unlike P&W's fixed start).
*Dependencies:* resource economics; research tree (or its mapless equivalent).
*Test:* does a beginner reach useful interdependence within their first week of turns?
*Phase:* v1 (this is *the* replacement engine — core design priority).

### XL-8. Turn schedule ↔ session and recovery design
*Inspired by:* P&W MAP-on-turn regen; Prompt 2 F-006/F-021 waiting complaints; PU contract deadlines; SC's "come back later" shape.
*Opportunity:* every 2-hour turn surfaces a **small, bounded report** (FO-002) and a **bounded action budget** (MAP-style; FO-010), so a 5–10 minute session yields *visible progress* without "must be online at time X" participation (see F-004 commitment-flexibility).
*Risks:* visible-per-turn systems create compulsion risk (design problem, not automatic); under-scheduled players still need a recovery concept (FO-003/FO-015).
*Dependencies:* turn engine integrity (Prompt 1 §6.1); digests; digests digesting *only* committed state.
*Test:* prototype turn-report legibility with new players (design-stage testing).
*Phase:* v1 core.

---

## Section 7 — Original feature opportunities

The register (Section 10) carries stable IDs; this section explains the leading opportunities in enough depth to inform later design stages. None is approved; all are candidates. Claim labels per Section 3.

### 7.1 The world-network view as the primary world representation (FO-004)
**What it is (DO-):** our fictional world is a *relationship graph*: nations as nodes; edges typed by treaties, rivalries, blockades, trade routes, and war states. The player-facing representation combines a legible graph view with **lists and timelines** (P&W's treaty web is the closest precedent — officially auto-generated from in-game treaty objects [FV this pass]).
**Why it fits our design (AI-):** with no geography, relationships ARE the world's shape. The genre has no full precedent (Prompt 1 §7.2), so this is genuine original territory rather than a replication. Prompt 2's F-004 (both casual and deep players) is served: the graph is glanceable; the timelines are deep.
**Evidence anchor:** P&W treaty web page [FV]; Utopia's relation-escalation concept [FV-ish C]; NationStates' embassies as social edges [FV prior].
**Distinctiveness:** the network view is load-bearing (war/peace/trade states are visible in it) rather than decorative — our task words ("identify strategic opportunities, monitor changes") come from the task's Section 15 (World network and diplomacy).
**Risks:** visual complexity (graphs can confuse more than they help if over-built); relationship data must be stored as structured, first-class state (a real schema cost); F-029 watchlist note — private-information leaks (who is allied with whom covertly?) need policy answers.
**Dependencies:** structured relationship records; treaty/embargo/rivalry state engine; turn report renderer for changes.

### 7.2 Transparent turn reports (FO-002)
**What it is (DO-):** every turn, each player gets a structured digest of *what changed and why* (income, expenses, production, consumption, war effects, relationship changes) — with per-line provenance (which buildings, which policies, which events).
**Evidence anchor:** Prompt 2 F-010 (knowledge lives off-game because games don't surface it) and Prompt 1 §7.2's "report granularity" open question. P&W's per-turn mechanics make this natural (revenue/taxes/MAP all tick per turn [FV]).
**Why it matters (AI-):** the two-hour cadence means players rethink 12×/day; without a legible report the game *teaches* via community wikis (the genre weakness), with one it teaches via the product itself.
**Risks:** reveals balance internals (narrower expert edge — a real trade-off); report volume must be bounded to stay D1-cheap; report content competes with core-feature scope.
**Dependencies:** deterministic turn engine; per-action audit trail; D1 write budget (bounded history).

### 7.3 New-player protection + guided first-turn sequence (FO-003)
**What it is (DO-):** a documented, explicit multi-day protection state (modeled on the *behavior* of P&W's beige/vacation mechanics and CN/Kingdom peace modes) combined with a guided first objectives sequence (e.g., "get your first city producing", "sign one trade", "read one embassy log").
**Evidence anchor:** F-011/F-012/F-026 (first-week friction, veteran advantage, no-restart request) and Prompt 1's new-player protection as a genre must-have §4.8.
**Distinctiveness:** protections designed *against* known exploit families from day one (F-017 teaches the exploit pressure — P&W's beige is gamed by engineering war expiry [FE]).
**Risks:** exploit surface (protection fishing, shield camping); must not be an unconditional shield.
**Dependencies:** war structure; absence system; survey of exploit scenarios.

### 7.4 Military action budget as the provisional OP basis (FO-010)
**What it is (DO-):** a turn-regenerated, capped action budget for all military actions, in the *shape* of P&W's MAP system [FV this pass]: start ~6; +1 per 2-hour turn; hard cap ~12; actions cost differing amounts (the naval-attack-4-MAP pattern [FV]). This is the closest verified precedent for the project's provisional Operations Points concept — but note (DO-): values, regeneration, action costs, and whether costs scale are *our* design decisions, nothing copied.
**Why it fits (AI-):** it converts "online time" into "scheduled scarcity", directly compatible with the shared clock and the no-live-participation requirement. It also creates meaningful de-escalation pressure (a banked budget can be saved or spent).
**Risks:** balancing per-action costs; exploit: hoarding up to cap then surprise-bursting (a budget *max* per immediate commit window addresses this, a later-design question); OP remains provisional (AI_CONTEXT D-004) and must not inherit P&W numbers.
**Dependencies:** war structure (FO-011); turn engine; action cost model.

### 7.5 War types + peace/settlement flow (FO-011)
**What it is (DO-):** a small typed taxonomy of conflict intents (raiders vs prolonged-attrition shop — *structurally* like, but not copied from, P&W's Ordinary/Raid/Attrition war types) plus a **peace-offer/settlement stage** where the outcome terms (reparations, transfers, treaty changes, relationship resets) are chosen and recorded.
**Evidence anchor:** P&W war types at declaration [FV]; Prompt 2 Section 8's O-7-peer "consequential peace negotiations" opportunity space; F-016/F-017 for fairness pressures.
**Why it matters (AI-):** settlements are where wars become *stories*; a settlement UI is cheap compared to battle math and differentiates us from games whose wars end in a resistance-zero clutch.
**Risks:** settlement economists (reparations too strong → vassalization engines; too weak → wars are pointless); exploit: fake-war-for-terms; must integrate protection phases.
**Dependencies:** FO-010; protection states (FO-017); ledger of war losses for settlement terms.

### 7.6 Listings market with reference prices (FO-009)
**What it is (DO-):** a player-listing market (post offers at per-unit prices; others accept) with **neutral reference prices** (day-end averages in P&W's pattern [FV this pass]) and optional **direct contracts** for negotiated deals — a deliberately *non*-matching-engine economy for v1.
**Evidence anchor:** verified P&W market shape; PU's contract layer [FV]; Sim Companies' fee-vs-contract distinction (provisional). F-022 (incumbency/opaque profitability) motivates the reference-price layer.
**Why it fits (AI-):** no engine-writes per order; turn-friendly; legible for newcomers; automatability is *banned by rule* (P&W precedent) rather than fought with tech.
**Risks:** slow discovery for illiquid goods; incumbency (F-022) still possible; an anti-manipulation stance must handle collusion (e.g., wash trades) — later design question.
**Dependencies:** safe resource balances; atomic transfers; trade-restriction rules (young nations, multi-account risk); anti-automation rules.

### 7.7 Resource interdependence without geography (FO-013)
**What it is (DO-):** replace P&W's continent-locked rares with **development-earned specialization**: nations unlock production niches through research/infrastructure choices and can re-specialize slowly; combined bonuses from *cooperative arrangements* (CN trade-circle inspirations: mutually agreed resource pairings with bonus effects) create interdependence without coordinates.
**Evidence anchor:** Prompt 1 §7.2 (the central mapless question — "find a substitute for geographic scarcity"); CN trade circles [FV]; PU's per-location exchanges (a different scarcity model) [FV prior].
**Why it is core:** without it, our mapless economy loses its trade engine and P&W-style interdependence; this is the single most design-critical opportunity (XL-7).
**Risks:** specialization composition rules must be adversarially reviewed (an "auto-best-pairing" collapses trade); re-specialization pacing must not punish early choices too hard (F-026) or too little (F-012 catch-up).
**Dependencies:** resource/production system; research/equivalent progression; trust-based arrangements; settlement-term machinery.

*(Secondary opportunities FO-015 re-entry digest, FO-016 economic transparency surfaces, FO-017 anti-farming protection states, FO-012 shared campaign focus, FO-005/FO-006/FO-007/FO-008 politics-light + alliance-tooling package, and FO-001 in-context teaching are registered in Section 10 with the same evidence style.)*

---

## Section 8 — Technical feasibility assessment

Complexity labels: **Low / Moderate / High / Unknown-until-prototyped**, always with a rationale. These are analyst judgments grounded in the prior reports' verified facts (Prompt 1 §6 for limits; §6.2 for integrity patterns), never measured benchmarks.

### 8.1 Cross-cutting platform facts carried from Prompt 1

- Cloudflare Workers free tier: 100k requests/day; 10 ms CPU per request; **50 ms CPU per Cron Trigger invocation**; D1 free tier: 5M rows read/day, **100k rows written/day (query-failure enforcement since 2026-09-01)**, 5 GB account storage. (D1 single-DB cap 10 GB.) [FV, H1–H4]
- Twelve cron triggers/day are trivially affordable; the constraint is *per-turn compute and write volume*: at 12 turns/day, ~8.3k rows' worth of writes per turn. A per-nation tick that writes one row per nation per turn leaves budget only for small worlds unless writes are **batched (single statements updating many rows)**, deltas-only, or event-sourced with compaction [AI-, carried from Prompt 1 §6.1].
- **Implication for every opportunity below:** any candidate that creates *per-player, per-turn row writes* must be justified against this budget, or designed to read-free (e.g., computed digests rather than stored history).
- Workers' 50 ms cron CPU: turn processing must be a **cheap, deterministic tick** (per-nation/per-relationship arithmetic, no geographic interpolation — favorable per Prompt 1 §6.4), with market matching avoided at ticks (listings resolve on-demand [AI-]).

### 8.2 Feasibility table for leading opportunities

| FO | Name | Frontend | Backend | Database | Tick fit | Security/abuse | Balance risk | Maintenance | Free-tier risk |
|---|---|---|---|---|---|---|---|---|---|
| FO-001 | In-context teaching | Low (tooltips, glossary) | Low (content) | Low (docs rows) | n/a (static) | Low | none | **Moderate — content upkeep** | Low |
| FO-002 | Turn reports | Moderate | **Moderate-to-High** (auditable per-turn computation) | Moderate (digests as bounded writes) | good (computed at tick) | Low | reveals internals (design) | Moderate | Moderate (write volume) |
| FO-003 | New-player protection | Low | Moderate (state machine, expiry) | Low | good | **High — adversarial** (F-017) | High (protects, must not be gamed) | Low | Low |
| FO-004 | World-network view | **High if graph-heavy**; Moderate if list+timeline-first | Moderate (relationship state engine) | Moderate | good | Moderate (hidden-treaty/info policy) | Moderate (info leaks) | Moderate | Low |
| FO-005 | Policy levers | Low | Low-moderate (modifiers) | Low | good | Low | Moderate (best-pick risk) | Low | Low |
| FO-006 | Treaty objects + web | Moderate | Moderate (treaty lifecycle, NAP gate) | Moderate | good | Low | Low | Moderate | Low |
| FO-007 | Alliance bank/roles | Moderate | **High** (permissions, atomic transfers, audit) | Moderate-high (audit logs) | good | **High** | Moderate | **High** | Moderate |
| FO-008 | Official bulk actions | Low-moderate | Moderate | Low | n/a (on-demand) | Moderate (rate-limit) | Low | Moderate | Low |
| FO-009 | Listings market + ref prices | Moderate | **High** (atomic settlement, restrictions) | Moderate | good (listings on-demand; averages at day boundary) | **High** (multi-acct, automation bans) | Moderate (collusion) | Moderate | Moderate |
| FO-010 | MAP-style action budget | Low | Low-moderate (budget counters, cap) | Low | good (+1/turn/cap) | Moderate (burst exploitation) | High (cost tuning) | Low | Low |
| FO-011 | War types + peace flow | Moderate | **High** (war state machine, settlements) | Moderate | good | High (fake wars) | **High** | High | Moderate |
| FO-012 | Shared campaign focus | Low | Low | Low | good | Low | Moderate (capped bonus) | Low | Low |
| FO-013 | Specialization engine | Moderate | Moderate | Moderate | good | Low | **High** (composition rules) | High | Moderate |
| FO-015 | Re-entry digest | Low | Low (on news already stored) | Low | n/a | Low | none | Low | Low |
| FO-016 | Economic transparency | Moderate | Moderate (history queries) | Moderate (history) | good | Low | reveals internals (design) | Moderate | Moderate |
| FO-017 | Anti-farming states | Low | Moderate | Low | good | High | High | Moderate | Low |
| FO-019 | Abstract intelligence | Moderate | Moderate-High | Moderate | n/a | High | High | High | Moderate |
| FO-021 | Consumer demand retail | Moderate | High (demand sim) | Moderate | good | Low | High | High | Moderate |
| FO-022 | Contracts/escrow | Moderate | High (guarded, escrowed transfers + breach) | Moderate | n/a | High | Moderate | High | Moderate |
| FO-023 | Elections/parliament | High (voting UIs) | High (fraud-resistant voting) | High | n/a | **High** (vote fraud/multis) | High | High | High |

### 8.3 Prototype-first assumptions (UH)

1. **Write budget per turn** for a realistic mid-size world — needs a Numbers + batching prototype at architecture stage.
2. **Listing market liquidity** — does a small new world produce enough visible offers for the reference-price layer to help? Needs a design prototype/end-stage experiment.
3. **The teaching layer's content size** — a filled glossary is content-ops work (Prompt 2 F-010 and O-10); estimate before committing.
4. **Complexity-vs-balance of relationship states** (XL-4) — scenario-walkthrough, not code.

---

## Section 9 — Feature dependency analysis

Order matters conceptually AND technically; both are documented.

### 9.1 Hard technical chain (implementation-order reasoning, AI-)

1. **Identity/accounts (one-nation-per-player enforcement plan)** — every other system trusts it (genre-wide rule; FV across all games' rules pages).
2. **Turn scheduler + tick engine (idempotent)** — Prompt 1 §6.1/6.2; *all* scheduled systems depend on trustworthy boundaries.
3. **Nation state + resource balances + atomic transfers** — base for economy, alliance bank, war losses.
4. **Production/upkeep computations** — the core tick workload; also its biggest D1 consumer.
5. **Economy: listings market + reference prices (FO-009)** — needs 3; also optional contracts (FO-022) *later* (added trust/complexity).
6. **Alliance organization (roles, permissions, treasury: FO-007/FO-008)** — depends on 3 (atomic moves) and benefits from 5 (taxes).
7. **Diplomacy states: treaties, embargoes, rivalries (FO-006)** — depends on relationship records; gates war (NAP block).
8. **War structure: types, MAP-budget (FO-010), resistance race, peace/settlement (FO-011), protection states (FO-017)** — depends on 3,4,6; the *largest single system* — budget accordingly.
9. **Reports/digests/teaching (FO-001/002/015/016)** — late but *cheap*; best layered on final system state.

### 9.2 Risks of premature implementation

- **War before diplomacy**: war systems shipped without the NAP-like blocks and protection states recreate the genre's farming complaints (F-016/F-017).
- **Market before identity/anti-multi**: raw settlement primitives without per-nation restrictions allow misuse (multi-account abuse; wash trades).
- **Alliance tools before logged audit trails**: trust breaks, and the F-018 burden recurs into power-trader malpractice disputes.
- **Reports before deterministic ticks**: digest content will be wrong if effects are non-deterministic; deterministic turn semantics is the **hard prerequisite** for all reporting.

### 9.3 Conceptual (non-sequencing) dependencies

FO-013's specialization feeds the entire economy; it is conceptually foundational but its *rules* can be designed later. FO-023 (politics-heavy) is conceptually powerful but its *release phase* depends on our v1 complexity budget (see Section 11). These conceptual relationships should shape design thinking, not necessarily implementation order.

---

## Section 10 — Prioritized feature opportunity register

**Status values:** `Candidate` (worth serious consideration later), `Needs Research` (evidence/design gap), `Deferred` (later phase), `Rejected` (established conflict). Evidence labels per Section 3.

### 10.1 Summary table

| ID | Name | Category | Priority group | Complexity | First-release relevance | Status |
|---|---|---|---|---|---|---|
| FO-001 | In-context teaching layer | Social/UX | B | Moderate | Yes | Candidate |
| FO-002 | Transparent turn reports | Time/UX | A | Moderate–High | Yes | Candidate |
| FO-003 | New-player protection + guided start | Time/UX | A | Moderate | Yes | Candidate |
| FO-004 | World-network view (relationships as world) | Diplomacy | A | Moderate (list-first) to High (graph) | Yes | Candidate |
| FO-005 | Domestic policy levers with bounded consequences | Politics | B | Low–Moderate | Possible | Candidate |
| FO-006 | Treaty objects + treaty web | Diplomacy | B | Moderate | Partially (NAP-block + minimal types) | Candidate |
| FO-007 | Alliance roles/permissions + treasury + audit | Alliances | B | High | Yes (minimal), richer later | Candidate |
| FO-008 | Official bulk/alliance actions (anti-automation stance) | Alliances | B | Moderate | Yes | Candidate |
| FO-009 | Listings market + reference prices | Economy | A | High (integrity) | Yes | Candidate |
| FO-010 | Military action budget (OP provisional basis) | Warfare | A | Moderate | Yes | Candidate |
| FO-011 | War types + peace/settlement flow | Warfare | A | High | Yes (minimal), richer later | Candidate |
| FO-012 | Shared battle/campaign focus (COTD-inspired) | Alliances | B | Low | Later | Candidate |
| FO-013 | Resource interdependence without geography | Economy | A | Moderate–High | Yes | Candidate |
| FO-014 | Upkeep/expense pressure as designed drains | Economy | A | Low | Yes. | Candidate |
| FO-015 | Re-entry digest ("what changed while away") | Social/UX | B | Low | Yes | Candidate |
| FO-016 | Economic transparency surfaces | Economy/UX | B | Moderate | Later | Candidate |
| FO-017 | Anti-farming war protections/state machine | Warfare | B | Moderate | Yes | Candidate |
| FO-018 | Late-entry catch-up mechanism | Economy/Design | C | High | **not v1** | Needs Research |
| FO-019 | Abstract intelligence/espionage | Warfare | C | High | Not decided here | Needs Research |
| FO-020 | Seasonality/events calendar | Time/Design | C | Moderate | Later | Deferred |
| FO-021 | Consumer/retail demand sim | Economy | C | High | later | Deferred |
| FO-022 | Contracts/escrow shipping layer | Economy | C | High | Later | Deferred |
| FO-023 | Elections/congress governance | Politics | C | High | **Not v1** | Deferred |
| FO-024 | Age/round resets | Time | D | N/A — conflicts with persistence | — | Rejected |
| FO-025 | Geographic world map | World | D | N/A — violates confirmed constraint | — | Rejected |
| FO-026 | Live-timed battle participation windows | Warfare | D | N/A — excludes offline participation | — | Rejected |
| FO-027 | Payment-gated late-game features | Monetization | D | N/A — free-first posture + F-020 | — | Rejected |

### 10.2 Register entries (compact full form; field order per task Section 18)

Format per entry: ①name ②category ③player experience ④inspired by ⑤sources/finding IDs ⑥evidence status ⑦player need/problem addressed ⑧main gameplay benefit ⑨distinctiveness ⑩dependencies ⑪risks/trade-offs ⑫complexity ⑬hosting/database implications ⑭first-release relevance ⑮recommended next action ⑯unresolved questions ⑰status — with ⓫ combined as one line where it shortens; ⓮ and ⓯ and ⓰ are terms where one line suffices. (Field 18 of the task's list ~ "Current status" appears as the last label per entry.)

**FO-001 In-context teaching layer** — Social/UX. ①Player experience: players hover/reference in-game to understand any number or term without leaving the browser session. ②Inspired-by: F-010/F-027 (knowledge lives in community documents); genre-wide glossary dependence. ③Evidence: F-010 Strong (multi-game corroboration). ④Need: newcomers' confusion is churn. ⑤Benefit: self-serve onboarding; veteran offload. ⑥Distinctive: our report says *nobody does all five* legible surfaces (Prompt 2 §5.8) — being the game that explains its own world. ⑦Deps: content design; deterministic turn engine (FO-002). ⑧Risk/trade-off: content-ops upkeep; reveals internals. ⑨Complexity: Moderate (content, not tech). ⑩Hosting: Low. ⑪First release: Yes. ⑫Next action: prioritize glossary core concepts list in later design pass. ⑬Unresolved: which concepts first; how deep to explain formulas. ⑭Status: **Candidate**.

**FO-002 Transparent turn reports** — Time/UX. ①Every turn: per-nation digest of deltas + provenance. ②Inspired-by: F-010, F-014, F-023; P&W turn structure [FV]. ③Evidence: F-010 Strong. ④Need: newcomers/returning loss of comprehension. ⑤Benefit: taught world; trust; battle/economy legibility. ⑥Distinctive: no studied game promises a provenance-complete turn report. ⑦Deps: deterministic ticks; journaling. ⑧Risk: D1 write volume if digests stored; content volume caps are transparent-internals trade. ⑨Complexity: Moderate–High. ⑩Hosting: Moderate (bounded digest writes; compute at tick). ⑪First release: Yes. ⑫Next action: report content taxonomy in design stage; prototype ordering. ⑬Unresolved: digest retention depth; per-line provenance granularity. ⑭Status: **Candidate**.

**FO-003 New-player protection + guided start** — Time/UX. ①A few explicitly-protected days + a short goal path. ②Inspired-by: F-011/F-012/F-026; P&W beige/vacation [FV] + CN peace mode [FV-lite]. ③Evidence: strong multi-source. ④Need: genre's must-have. ⑤Benefit: first-week agency. ⑥Distinctive: *adversarially designed* (FO-017 links; F-017 evidence teaches us the exploit style). ⑦Deps: war structure; absence system; bounds. ⑧Risk: exploit families (shield camping, protection fishing). ⑨Complexity: Moderate. ⑩Hosting: Low. ⑪First release: Yes. ⑫Next action: enumerate adversarial scenarios in the war-design stage. ⑬Unresolved: exact duration/adopted behavior under protection. ⑭Status: **Candidate**.

**FO-004 World-network view** — Diplomacy. ①See the world as nations + typed relationships with changes-over-time. ②Inspired-by: Prompt 1 §7.2; P&W treaty web [FV this pass]; Utopia relation ladder [FV-ish]. ③Evidence: FV for components; AI- for composition. ④Need: mapless world's legibility. ⑤Benefit: strategy surface = the graph. ⑥Distinctive: genuine original composition; nobody ships a full relationship-as-world view. ⑦Deps: structured relationship data; treaty/embargo engine. ⑧Risk: info leakage policy (secret treaties); graph-for-reference complexity. ⑨Complexity: Moderate (list-first)–High (graph UI). ⑩Hosting: Low. ⑪First release: Yes, **list/timeline-first**; graph polish later. ⑫Next action: schema sketch for relationship records in next design stage. ⑬Unresolved: how much of relationships is public (design). ⑭Status: **Candidate**.

**FO-005 Domestic policy levers** — Politics. ①Bounded toggles (stability↔efficiency etc.), changed on turn boundaries with cooldowns (P&W's policy-change cooldown pattern [FV]). ②Inspired-by: F-015 (politics under-served); Prompt 1 §7.4 (light-politics start recommended). ③Evidence: F-015 Weak-Moderate; AI- for the middle path. ④Need: politics that matters without eRep overhead. ⑤Benefit: cheap depth flavor. ⑥Distinctive: consequence-bounded toggles forming a *coherent small system*, not an exhaustive table. ⑦Deps: FO-002 reporting. ⑧Risk: best-pick degeneracy; thin-politics repeat. ⑨Complexity: Low–Moderate. ⑩Hosting: Low. ⑪First release: Possible. ⑫Next action: candidate policy set list in design stage. ⑬Unresolved: how many axes. ⑭Status: **Candidate**.

**FO-006 Treaty objects + treaty web** — Diplomacy. ①In-game typed treaties, visible web, with a minimal mechanical gate (NAP-style block on war declarations). ②Inspired-by: P&W treaty web [FV this pass]. ③Evidence: FV for what P&W does; AI- for our composition. ④Need: F-013 (alliance routing debates) — a native visible relationship layer is accountability without enforcement. ⑤Benefit: legible diplomacy; culture support. ⑥Distinctive: our treaty vocabulary is our own (and typenames will NOT be copied). ⑦Deps: FO-004 structure. ⑧Risk: over-encoding type variety (design creep). ⑨Complexity: Moderate. ⑩Hosting: Low-moderate. ⑪First release: Minimal form (one block-type + visibility). ⑫Next action: define v1 treaty-type minimum in design stage. ⑬Unresolved: what types earn mechanical enforcement. ⑭Status: **Candidate**.

**FO-007 Alliance roles/treasury/audit** — Alliances. ①Configurable roles, shared bank, taxes, with a tamper-evident decision/transfer audit log. ②Inspired-by: P&W's 15-permission matrix + tax brackets [FV this pass]; F-018 admin burden. ③Evidence: strong (official). ④Need: P&W-proven toolset; our F-018 evidence that admin burden is real. ⑤Benefit: coordination without Discord-only; who can do what is legible. ⑥Distinctive: **audit-first** culture vs P&W's opacity (community-observed). ⑦Deps: identity; atomic transfers; roles engine. ⑧Risk: security/ordering surface; scope creep. ⑨Complexity: High. ⑩Hosting: Moderate (audit logs = writes; bound them). ⑪First release: minimal (one tax bracket + bank view/withdraw + default roles); richer later. ⑫Next action: requirements-first design of the permissions minimal set. ⑬Unresolved: how small the v1 set can be. ⑭Status: **Candidate**.

**FO-008 Official bulk/alliance actions** — Alliances. ①In-game multimember actions (bulk grants/donations/tax application) reducing admin labor; explicit anti-automation rule preserved (P&W's automated-trading ban [FV]). ②Inspired-by: F-018 automation debate (103 replies). ③Evidence: Moderate (single rich discussion) + FV ban pattern. ④Need: reduce bookkeeping while blocking bot unfairness. ⑤Benefit: the genre's cleanest answer to its own dispute. ⑥Distinctive: making *tool-vs-automation boundary* a first-class design conversation. ⑦Deps: roles/permissions (FO-007). ⑧Risk: scope creep in "which actions can be bulked". ⑨Complexity: Moderate. ⑩Hosting: Low. ⑪First release: Yes (define the legitimate set). ⑫Next action: enumerate candidate bulk actions in design stage. ⑬Unresolved: rate limits per action type. ⑭Status: **Candidate**.

**FO-009 Listings market + reference prices** — Economy. ①Player-listed offers, per-unit prices, world-average reference prices (day-end), plus young-nation/multi-account trade restrictions; direct trade option (mutual-approval). ②Inspired-by: verified P&W market shape + CN mutual-approval trades [FV]; anti-automation rules [FV]. ③Evidence: FV for P&W's shape; prices unverified as *current* — reuse carefully. ④Need: F-022 (legible economics); newcomers' first trade. ⑤Benefit: low engine cost; trade as social relationship; ledger-friendliness. ⑥Distinctive: reference prices as a *built-in* fairness tool. ⑦Deps: identity/anti-multi; atomic settlement; anti-collusion rules. ⑧Risk: liquidity; collusion; action-spam clicks (rate-limits). ⑨Complexity: High (settlement integrity). ⑩Hosting: Moderate-High (listing storage + settlement disputes). ⑪First release: Yes — core. ⑫Next action: define the anti-abuse rule set + settlement design in architecture stage. ⑬Unresolved: fee policy; contract layer timing (FO-022). ⑭Status: **Candidate**.

**FO-010 Military action budget (MAP-shaped; OP provisional)** — Warfare. ①Turn-regenerated, capped budget; actions cost differing amounts; war entry also gated by range/cooldown. ②Inspired-by: verified P&W MAP mechanics [FV this pass] + CN 2-attacks/day/front [FV-lite]. ③Evidence: FV for the pattern; our values are our own. ④Need: turn-locked action scarcity; anti-burst fairness. ⑤Benefit: strategic pacing (bank vs spend); matches 2h cadence. ⑥Distinctive: no values copied; our own action set. ⑦Deps: FO-011; turn engine. ⑧Risk: balance tuning; burst-hoarding exploit (cap-per-commit question); concept creep. ⑨Complexity: Moderate. ⑩Hosting: Low. ⑪First release: Yes. ⑫Next action: enumerate the candidate action set + rough cost ranges for later prototyping (NOT final values). ⑬Unresolved: how many action types; budget-per-war vs budget-per-nation. ⑭Status: **Candidate**.

**FO-011 War types + peace/settlement flow** — Warfare. ①Typed conflict intents; a Resistance-race-shaped resolution *pattern*; explicit settlement term selection. ②Inspired-by: P&W war types [FV], resistance concept [FV-ish, community doc]; Prompt 2 O-7-adjacent peace opportunity. ③Evidence: FV for the pattern; formulas unverified (not needed). ④Need: F-016 small nations; F-017; meaningful post-war consequences. ⑤Benefit: settlement story-telling as the differentiator. ⑥Distinctive: our own end-conditions and term vocabulary. ⑦Deps: FO-010; protection states FO-017; ledger of war economic losses. ⑧Risk: hardest balance problem in the game; fake-wars-for-terms; term abuse. ⑨Complexity: High. ⑩Hosting: Moderate. ⑪First release: minimal (one attack type-space, one settlement stage — later deepening). ⑫Next action: separate Prompt-5+ design stage (likely a dedicated stage). ⑬Unresolved: end-conditions; reparations shape. ⑭Status: **Candidate**.

**FO-012 Shared battle/campaign focus** — Alliances. ①Alliance leadership periodically designates a campaign; members participating gain a small capped modifier. ②Inspired-by: eDominations COTD (+5% damage, both sides) [FV this pass]. ③Evidence: FV for the precedent. ④Need: coordination without labor (F-018). ⑤Benefit: one decision replaces many. ⑥Distinctive: mapless and treaty/web-native (FO-004 integrates). ⑦Deps: war/campaign structure. ⑧Risk: pushes depth to one focus; gamed fake-campaigns; must cap small. ⑨Complexity: Low. ⑩Hosting: Low. ⑪First release: later. ⑫Next action: evaluate with FO-011 in a later pass. ⑬Unresolved: cap values/campaign type set. ⑭Status: **Candidate**.

**FO-013 Resource interdependence without geography** — Economy. ①Specialization earned via research/infrastructure + cooperative pairing bonuses; slow re-specialization. ②Inspired-by: Prompt 1 §7.2 open question; CN trade circles [FV]; P&W continent scarcity as the *problem to replace*, not the solution. ③Evidence: gap-filling AI- + FV components. ④Need: the trade engine of a mapless world. ⑤Benefit: interdependence; trade sociability; planetary identity. ⑥Distinctive: whether a *network-position* specialization exists could be our signature economy. ⑦Deps: research/equivalent progression; FO-009 market. ⑧Risk: composition degeneracy (single best pairing), too rigid vs too fluid; vulnerable to catch-up (F-012). ⑨Complexity: Moderate–High. ⑩Hosting: Moderate. ⑪First release: Yes — foundational. ⑫Next action: dedicated design exploration stage (economy). ⑬Unresolved: specialization axes; re-specialization cost; pairing vs market mix. ⑭Status: **Candidate**.

**FO-014 Upkeep/expense pressure as designed drains** — Economy. ①Continuous expenses (food/infrastructure/military/readiness) that make growth a management problem (Prompt 1 §4.2 evidence: drains as first-class design). ②Inspired-by: P&W starvation penalty & CN's bills; eRep's maintenance churn (cautionary — F-019). ③Evidence: FV pattern; FE caution. ④Need: accumulation without management is boring; drains create choices. ⑤Benefit: sessions have purpose. ⑥Distinctive: calibrated to avoid F-019's chore-loop *fatigue*. ⑦Deps: production; FO-002 reporting. ⑧Risk: chore perception; automation temptation (F-018). ⑨Complexity: Low. ⑩Hosting: Low. ⑪First release: Yes. ⑫Next action: drain taxonomy in economy stage. ⑬Unresolved: how many drain classes; food-analogue necessity. ⑭Status: **Candidate**.

**FO-015 Re-entry digest** — Social/UX. ①"What changed while away" — high-level summary + flagged relationship changes, distinct from daily turn reports. ②Inspired-by: F-023; O-12 in Prompt 2. ③Evidence: Moderate. ④Need: returning-player churn. ⑤Benefit: graceful absence flow. ⑥Distinctive: nobody in the studied set ships it as a first-class flow. ⑦Deps: FO-002 machinery. ⑧Risk: notification fatigue if over-warned. ⑨Complexity: Low. ⑩Hosting: Low (on-demand rendering). ⑪First release: Yes. ⑫Next action: retention window policy decision later. ⑬Unresolved: how far back digests reach. ⑭Status: **Candidate**.

**FO-016 Economic transparency surfaces** — Economy/UX. ①Realized per-unit margins, cost hints, trend views. ②Inspired-by: F-022 (profitability opacity as churn trap); PU/SC reference-price conventions. ③Evidence: Moderate. ④Need: honest economics; trading skill ≠ wiki access. ⑤Benefit: reduces newcomer burn; increases meaningful specialization choices. ⑥Distinctive: explicitly anti-"opaque-trap". ⑦Deps: FO-009; history storage. ⑧Risk: reveals strategy internals to competitors; charts maintenance burden. ⑨Complexity: Moderate. ⑩Hosting: Moderate (data volume vs D1 reads). ⑪First release: Later. ⑫Next action: define which datasets are public vs private (design). ⑬Unresolved: privacy of wallet/production data. ⑭Status: **Candidate**.

**FO-017 Anti-farming war protections/state machine** — Warfare. ①Explicit protection states with exits, cooldowns on re-declarations, and documented abuse-fish limits — all embedded in the relationship graph, not a map (XL-4). ②Inspired-by: P&W beige/vacation/score-range/cooldown mechanics + P&W's *own* anti-abuse rules [FV this pass]; F-017/F-016 evidence of exploit pressure. ③Evidence: FV for the precedents + FE for the harms. ④Need: protection must exist; unadapted protection becomes an exploit. ⑤Benefit: protected newcomers without shielding farmers. ⑥Distinctive: adversarial-first design method as a stated principle. ⑦Deps: FO-010/011; relationship records. ⑧Risk: complex states harm comprehension; must be bounded. ⑨Complexity: Moderate. ⑩Hosting: Low. ⑪First release: Yes (minimal state set). ⑫Next action: adversarial walkthrough + walkthrough scenario list. ⑬Unresolved: the exact state machine. ⑭Status: **Candidate**.

**FO-018 Late-entry catch-up mechanism** — Economy/Design. ①Options explored: re-specialization pace, small-nation structural niches, generation-aware progression (staged entry, no resets), and others; *no mechanics decided here*. ②Inspired-by: F-012 (Strong-multi-source); Prompt 2 O-8. ③Evidence: gap-filling analysis, no game precedents for our mapless context. ④Need: the strongest cross-game frustration family. ⑤Benefit: honest answer for late joiners. ⑥Distinctive: avoided by map-games (P&W's own answer is "score ranges + beige"; we could go further). ⑦Deps: FO-013; FO-002; war design. ⑧Risk: any option changes core economy identity; must be a major design-stage decision with simulation. ⑨Complexity: High. ⑩Hosting: Unknown-until-simulated. ⑪First release: not-for-v1. ⑫Next action: dedicated Prompt-5+/design-stage exploration; require numeric sim. ⑬Unresolved: which option; how much equalization. ⑭Status: **Needs Research**.

**FO-019 Abstract intelligence/espionage** — Warfare/Politics. ①Intelligence ops influencing knowledge (EP, defense hints; dangerous for scope). ②Inspired-by: P&W spies [FV]; Utopia thieves [FV-ish]; the espionage-uncouncil papers (Plate 1 §7.7). ③Evidence: thin across the board (NF-ish everywhere). ④Need: uncertainty/counterplay. ⑤Benefit: asymmetric shortcuts. ⑥Distinctive: possible, but the genre's documentation is so thin that nearly everything is our choice — which is often a warning, not a green light. ⑦Deps: war + FO-002 legibility (spy games *need* reporting). ⑧Risk: scope/abuse (bot farming, information-walling), meta-gaming. ⑨Complexity: High. ⑩Hosting: Moderate. ⑪First release: no. ⑫Next action: keep on Stage-2 watchlist only. ⑬Unresolved: whether espionage makes mapless wars *better* or just *longer*. ⑭Status: **Needs Research**.

**FO-020 Seasonality/events calendar** — Time. ①Seasonal global modifiers (P&W food +20%/−20% precedent [FV]) or scheduled world events. ②Inspired-by: P&W seasonality; complicated a synopsized event-layer. ③Evidence: FV(P&W only). ④Need: world texture. ⑤Benefit: rhythm + planning variety. ⑥Risk: holiday FOMO; balancing; extra rule surface. ⑦Deps: turn engine; FO-002. ⑧Complexity: Moderate. ⑨Hosting: Low. ⑩First release: later. ⑪Next action: revisit post-v1. ⑫Unresolved: none urgent. ⑬Status: **Deferred**.

**FO-021 Consumer/retail demand sim** — Economy. ①A demand model where player-set prices drive consumer purchases (Sim Companies' retail gameplay). ②Inspired-by: SC retail [FV-lite]; the "price-setting as gameplay" lesson. ③Evidence: moderate precedent; SC interface only. ④Need: adds an economic role distinct from production/trading. ⑤Benefit: economic *strategy* diversity. ⑥Risk: demand tuning; niche marginalization; UI. ⑦Deps: FO-009 + FO-016. ⑧Complexity: High. ⑨Hosting: Moderate-High (per-tick demand writes). ⑩First release: no. ⑪Next action: defer until market+economy are stable. ⑫Unresolved: does our world want "consumer demand" at all (nation-scale, not individual beliefs)? ⑬Status: **Deferred**.

**FO-022 Contracts/escrow/supply layer** — Economy. ①Negotiated, escrowed delivery arrangements (PU contracts style; Sim Co fee-less contracts distinction [FV; provisional]). ②Inspired-by: PU contracts/shipping; the trust-rating device [FV]. ③Evidence: FV(PU). ④Need: reliable large deals; supply lines. ⑤Benefit: logistics gameplay inside a graph world. ⑥Risk: escrow-integrity bookkeeping; breach/penalty design; UI breadth. ⑦Deps: FO-009 + FO-013 + atomic transfers. ⑧Complexity: High. ⑨Hosting: Moderate. ⑩First release: no. ⑪Next action: revisit with alliance-supply flow needs. ⑫Unresolved: whether *players* or *alliance tools* carry supply (FO-008 overlap). ⑬Status: **Deferred**.

**FO-023 Elections/congress governance** — Politics. ①Full elected institutions (presidents, congress, tax law powers). ②Inspired-by: eRep/eDom [FV prior]. ③Evidence: FV for the pattern; FE evidence that they add onboarding and low-info-voting burden (Prompt 1 §5.3; Prompt 2 F-010 family). ④Need: none demonstrated for our constraints. ⑤Risk: moderate-to-high complexity for shallow player numbers; multis/vote-fraud risk; vote-turnout tuning. ⑥Complexity: High. ⑦Hosting: High. ⑧First release: no. ⑨Next action: revisit only if our v1 politics (FO-005) proves under-powered. ⑩Unresolved: n/a for now. ⑪Status: **Deferred**.

### 10.3 Rejected entries (with rationale preserved)

**FO-024 Age/round resets** — Rejected: conflicts with the project's persistent-world identity and the documented genre evidence that rounds trade legacy for competitive fairness (Utopia/Earth Empires pattern) — our world is persistent by constraint. Preserve as a *possible later separate-format experiment*, not planned.
**FO-025 Geographic world map** — Rejected: violates a confirmed project constraint (fictional, mapless world); documented cost evidence (Prompt 1 §5.3) — geography multiplies scope (maps, regions, onboarding burden) for benefits we obtain differently.
**FO-026 Live-timed battle participation windows** — Rejected: excludes offline/off-schedule players (eRep-style live rounds conflict with the project's "close the browser, world continues" principle); incompatible with our 2-hour-turn architecture.
**FO-027 Payment-gated late-game features** — Rejected for roadmap purposes: free-first posture + documented monetization friction modes in the genre (F-020 eRep gold-power gap; PU PRO gating late-game features value-questioned by players). Monetization strategy remains out of scope for this report; the *reject* is about **not** adopting another game's late-game-gating pattern, not about all monetization ever.

---

## Section 11 — Deferred ideas and rejected directions

Beyond the register: substantial ideas explicitly *not* carried into candidate lists.

- **Full parliamentary political simulation (XL-1 expanded; FO-023)** — deferred, not rejected: the evidence supports *starting light* (Prompt 1 §7.4 recommendation; eRep's complexity as a warning). If FO-005's light politics proves weak, full institutions remain a possible later pivot.
- **Real-time order-book markets (FO-009 alternative)** — deferred: real matching engines (PU/SC precedent) are better for liquidity and player experience *at scale* but cost real-time integrity (D1 writes per order, fraud surface) and are less turn-native. If our listings market chokes on liquidity in playtest, this is the fallback, not the default.
- **Deep simulation of domestic populations (cities with fully simulated populations)** — rejected for this stage: high simulation cost and unclear payoff without a proven player demand; P&W's own model is abstract-population (community-described) and its simulation is D1-cheap; we could revisit a *predetermined* population model (a single city slot per player) later if city content emerges as the retention driver.
- **Client-side streaming/twatches (live world feeds)** — deferred: cool UX, but the project's browser-first, no-live-connection requirement + free-tier request limits argue for turn boundary fetches, with events/digests (FO-002/015) carrying freshness instead.
- **Third-party API integrations (Discord bots, kill feed etc.)** — deferred indefinitely: valuable only after our in-game tooling (FO-006/007/008) is proven, per the P&W pattern where Discord coordination is a community choice, not a game guarantee; and per prompt-2 F-013's evidence that off-game coordination is *controversial*, not automatically beneficial.

---

## Section 12 — Open research questions

Organized by importance, with dependency notes.

**Tier 1 — must be resolved before final design:**
1. **Write-budget mathematics per turn** (FO-002/FO-009/FO-013 interplay) — architecture stage; depends on: world size assumptions, batching design.
2. **Which catch-up philosophy for late entrants (FO-018)** — design stage; depends on: economy identity (FO-013/FO-014).
3. **How much of the economy is market vs relationship** (FO-009 vs FO-022 vs FO-013's pairing bonuses) — economy stage.
4. **Protection/absence state machine (FO-003/FO-017)** — design stage; adversarial scenario enumeration required.

**Tier 2 — needed for informed v1 choices:**
5. **Small-v1 public information policy** (what is public vs private in the network view, FO-004; in economic disclosures, FO-016) — design stage.
6. **Treaty-type minimum** (FO-006) + whether block-type mechanical enforcement is the right minimal gate — design stage.
7. **Specialization axis design (FO-013)** — economy stage; interdependent with #3.
8. **Realistic action cost ranges for a MAP-like budget (FO-010)** — design-stage prototyping, not values.

**Tier 3 — watchlist (timing flexible):**
9. Espionage scope (FO-019) — needs a later dedicated pass; nothing this stage concluded.
10. Consumer demand (FO-021) and contracts (FO-022) — market-maturity dependent.
11. Seasonality/event cadence (FO-020) — post-v1 texture.
12. Monetization strategy (rejected FO-027 as a *pattern*, not a plan) — separate stage; the free-first posture is established.
13. Current-state verification for eRep/NationStates feature detail — low priority; our comparisons on those games are structural, not formula-dependent.

**Dependencies in one line:** #2 depends on #7; #3 depends on #7 and #5; #4 depends on #8; #11 needs #1–#4 solved first.

---

## Section 13 — Source register

All sources accessed 2026-10-22. **[O]** official, **[C]** community-maintained, **[3]** independent, **[FV]** verified directly (by the analyst this pass). New this pass (not already in the Prompt 1/Prompt 2 registers):

### Politics & War (new this pass)
| # | Source | Type | Supports |
|---|---|---|---|
| P20 | [Alliance Positions (P&W-pedia)](https://politicsandwar.com/pwpedia/article/Alliance-Positions) | [O] | 9 position levels, Leader/Heir/Officer/Member, 15 permissions |
| P21 | [Tax Brackets (P&W-pedia)](https://politicsandwar.com/pwpedia/article/tax-brackets) | [O] | Alliance taxes on money+resources; default bracket; Bank-Access gating; Gray-nation exception |
| P22 | [Alliance Treaty Web](https://politicsandwar.com/alliances/treatyweb/) | [O/FV] | 10 treaty types with descriptions; auto-operated in-game; **"Treaties are not enforced by the game, except non-aggression"** |
| P23 | [War Types (P&W-pedia)](https://politicsandwar.com/pwpedia/article/War-Types) | [O] | War types chosen at declaration and locked |
| P24 | [Naval Battles (P&W-pedia)](https://politicsandwar.com/pwpedia/article/Naval-Battles) | [O] | 4-MAP naval attack; blockade effects on market/bank transactions |
| P25 | [Beige Buff (P&W-pedia)](https://politicsandwar.com/pwpedia/article/Beige-Buff) | [O] | July 2025 15% daily-recruitment increase for eligible beige nations |
| P26 | [War Score Range Calculator](https://politicsandwar.com/tools/score) | [O] | Separates attack/defend ranges (formula not stated) |
| P27 | [War (P&W community wiki)](https://politicsandwar.fandom.com/wiki/War) | [C/FV] | Resistance race (100→0), MAP start 6 / +1 per turn / cap 12, Blitzkrieg 7 / Fortress 5 |
| P28 | [Game Rules](https://politicsandwar.com/rules/) | [O] | Trade restrictions (young/same-network nations), automated-trading ban, Vacation Mode anti-abuse conditions, anti-war-slot-filling rules |
| P29 | [Community FAQ (Fandom)](https://politicsandwar.fandom.com/wiki/Frequently_Asked_Questions) | [C] | 12-turn repeat-declaration cooldown claim |
| P30 | [Average Prices (Fandom)](https://politicsandwar.fandom.com/wiki/Average_Prices) | [C] | Average-price reference layer; day-end measurement (example prices dated 2015 — NOT current data) |
| P31 | [Free Trade Market forum](https://forum.politicsandwar.com/index.php?/forum/43-free-trade-market/) | [3] | Listing/offer framing of the market |

### Other games (new this pass)
| # | Source | Type | Supports |
|---|---|---|---|
| X1 | [PU Market Guide](https://handbook.apex.prosperousuniverse.com/tutorials/current-tutorials/05-market-guide/index.html) | [O] | CX order books with bids/asks/spreads; exchange warehouse rental |
| X2 | [PU Local Markets](https://handbook.apex.prosperousuniverse.com/tutorials/legacy-tutorials/local-markets/index.html) | [O] | Bulletin-board ads → contracts, not auto-transfers; governor-set ad fees; breach/trust rating |
| X3 | [PU PRO License](https://handbook.apex.prosperousuniverse.com/wiki/pro-license/index.html) | [O] | FREE/BASIC/PRO gates: ships-in-flight caps, ad-posting vs accepting, contracts |
| X4 | [PU Corporations and Contracts](https://handbook.apex.prosperousuniverse.com/tutorials/current-tutorials/08-corporations-and-contracts/index.html) | [O] | Private contracts; shipping ads; contract workflow |
| X5 | [Sim Companies FAQ](https://www.simcompanies.com/pages/faq/) | [O, indexed only — provisional] | Exchange market fee (~3% example, variable); hidden buy orders; contracts fee-free; level gate for contracts |
| X6 | [eDominations Alliance (game-hosted)](https://edominations.com/en/article/12210/alliance) | [O] | 100-gold alliance creation; +5% damage COTD bonus |
| X7 | [eDominations Alliance (wiki)](https://wiki.edominations.com/alliance/) | [C-ish secondary wiki] | COTD logic; leadership powers; coordination advice |
| X8 | [CN Game Update Log 2011 (Tournament Edition)](https://www.cybernations.net/game_update_log.asp?theyear=2011) | [O] | Richer alliance tools existed **in TE only** — do not attribute to standard CN |
| X9 | [CN Alliance (community wiki)](https://cybernations.fandom.com/wiki/Alliance) | [C] | Alliances "almost entirely outside game mechanics" (standard game) |
| X10 | [CN Trade circle (community wiki)](https://cybernations.fandom.com/wiki/Trade_circle) | [C] | Up-to-six resource trades; bonus combos; alliance departments organizing circles |
| X11 | [Utopia Kingdom / Politics / Relations (community wiki)](https://utopiagame.fandom.com/wiki/Kingdom) | [C] | 25-province kingdoms; elected Monarch + 2 Stewards; war forum; relation escalation |
| X12 | [OGame Alliance Guide (Gameforge)](https://gameforge.com/en-GB/games/ogame-alliance-guide.html) | [O] | ACS joint fleet attack; alliance depot; rank delegation |
| X13 | [OGame diplomacy page (Gameforge)](https://gameforge.com/en-GB/games/browser-game-with-diplomacy.html) | [O] | **"no official diplomacy interface enforcing treaties"** — NAPs are trust-based |

### Prior-pass sources (not repeated)
The complete registers from Prompts 1 and 2 remain authoritative for their claims and are referenced in Sections 4–5 by their prior report IDs ([01_competitor_research.md](01_competitor_research.md) Section 9 for P1–P19, N1–N2, C1–C5, E1–E5, PU1–PU4, S1–S4, A1–A6, H1–H4; [02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) Section 11 for P1–P18 player-sentiment sources, N1–N7, C1–C3, E1–E11, S1–S4, PU1–PU5, O1–O4).

### Evidence limitations (re-confirmed)
Sim Companies in-app pages app-shelled again this pass (X5's indexed-FAQ claims provisional). No logged-in testing (n/a). Complexity labels in Section 8 are analyst judgments. P&W exact current combat formulas remain community-doc-only and were NOT retried this pass (not needed beyond the structural facts above).

---

## Section 14 — Handoff to Prompt 4

### What Prompt 4 receives

**Carry-forward context:**
- Project constraints: browser-based multiplayer persistent game; fictional, **mapless** world (symbolic relationship network); **2-hour UTC turns (12/day)**; server-authoritative state; free-first infrastructure (Cloudflare Workers/D1 candidates, with D1 free tier's 100k-row-writes/day as a first-class constraint). [AI_CONTEXT.md](../AI_CONTEXT.md) Section 2.
- Prior reports: [01](01_competitor_research.md) (Prompt 1) and [02](02_strengths_weaknesses_player_frustrations.md) (Prompt 2), plus **this report** [03](03_feature_comparison_opportunity_analysis.md).

**Principal feature comparisons (fast recap):**
- Market architecture: listings (P&W, verified) vs order books + contracts (PU, verified) vs exchange+contracts (SC, provisional).
- National development: serial-accumulative (P&W), portfolio/bill-capped (CN), chain (PU/SC).
- Politics: light toggles (P&W) vs institutions (eRep/eDom) vs roleplay (NS).
- Diplomacy encoding: from social-only (CN/OGame) to in-game types + visible web with **NAP-only mechanical enforcement** (P&W).
- Alliance tooling: the P&W full-permission matrix vs minimal tools; the COTD shared-target device (eDom) as a cheap coordination pattern; audit logs as our standout trust-offering.
- War: P&W's resistance-race + MAP budget as the verified turn-locked pattern; CN's simpler daily limits; eRep/eDom live-round systems incompatible with our design.
- Time: turn-locked budgets (P&W MAP +1/turn/cap 12) as the cleanest verified precedent for action economy.

**Major finding IDs (Prompts 1–2)** used here: F-001, F-002, F-004, F-006, F-010–F-013, F-015–F-019, F-021–F-023, F-026, F-027, F-029.

**Feature-opportunity IDs created here:** FO-001…FO-027 (Section 10); FO-024…FO-027 rejected, FO-018/FO-019 Needs Research, FO-020/FO-021/FO-022/FO-023 Deferred, others Candidate.

**Prioritized register groups:** see Section 10.1's Priority column; Group A (strongest first-release candidates): FO-002, FO-003, FO-004, FO-009, FO-010, FO-011, FO-013, FO-014.

**Major implementation / balance risks (from Section 8):**
- D1 free-tier write budget (per-turn, per-nation) — the top architecture-only constraint; FO-002/FO-009 especially.
- War-system balance (FO-010/FO-011/FO-017) — highest design-scope risk; still untouched by values.
- FO-013 as the mapless-economy keystone — dedicated exploration stage needed.
- Market integrity (FO-009) — anti-multi + anti-automation + collusion defenses required.

**Open questions (Section 12, tier-1 first):** write-budget math; catch-up philosophy; economy shape guides; protection state machine.

**What the next prompt needs to examine:** Prompt 4's own scope, as authorized by the user; suggested focus given the gaps: security/anti-cheat/fair-play systems, or economy design structure, depending on the intended prompt order — **the pipeline's prompt order will be provided by the user, not decided here**.

**Path of this report:** `docs/stage-1/03_feature_comparison_opportunity_analysis.md` (v1.0, 2026-10-22).

**Do not execute Prompt 4 in this task.**

---

### Report status footer

- **Prompt 3 research completion status:** Complete within source-access constraints; no fabricated evidence; direct verifications (P&W treaty web + war page) newly performed this pass.
- **Games/novel comparisons:** P&W (market/war/alliance mechanics re-verified), Cyber Nations (incl. CN-TE distinction), eDominations (alliance & COTD detail), Utopia (kingdom governance detail), OGame (new: ACS/depot/treaty-absence pattern), Prosperous Universe (market/contract detail), Sim Companies (fee/contract detail, provisional).
- **Feature-opportunity register:** 27 stable IDs.
- **Research limitations:** Sim Companies provisional claims remain; P&W exact current formulas unchanged-from-Prompt-1 gap; no logged-in testing. No new limitations this pass.
- **Recommended next action:** user authorizes Prompt 4; this report's Section 14 defines the handoff.
- **Document version:** 1.0. Prepared 2026-10-22.
