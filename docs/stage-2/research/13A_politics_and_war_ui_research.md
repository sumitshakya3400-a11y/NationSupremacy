# 13A — Politics & War UI research, benchmark register and supplementary browser-game research

**Prompt:** Stage 2 Prompt 13A — UI research, architecture and design foundations. **Created:** 2026-11-11. **Reconciled:** 2026-11-12 (Prompt 13A-C1 evidence and cross-reference reconciliation).
**Research date:** 2026-11-11 for all live retrievals; prior in-repo P&W registers keep their own dated retrieval days.
**Status:** research evidence, benchmarking and recommendations only — **approves no rule, screen, component, number or implementation** (D-003/D-199 inputs-only discipline).
**Companions:** [design principles & architecture](13A_ui_design_principles_and_architecture.md) · [master screen inventory](13A_master_screen_inventory.md) · [responsive & design-system foundations](13A_responsive_and_design_system_foundations.md) · [UI requirements, open questions & acceptance](13A_ui_requirements_open_questions_and_acceptance.md)

---

## 1. How to read this register

### 1.1 What this file is and is not

This is Prompt 13A's evidence file for the mandated primary benchmark — **Politics & War** — plus the two gap-driven supplementary titles. It is evidence and reasoning, not rules. Approved positions live only in [DECISIONS.md](../../DECISIONS.md) (**D-198…D-205**) and their mirrors in [the 04 register](../04_approved_and_provisional_decisions.md). The screen register is [the master screen inventory](13A_master_screen_inventory.md); UI requirement candidates `13A-UR-###` and open questions `13A-OQ-###` live in [the requirements and acceptance register](13A_ui_requirements_open_questions_and_acceptance.md). This file creates **no** global `REQ-`, `UD-`, `DD-` or `SCR-` identifier.

Politics & War is the design **reference**, not the design **authority**: its existence of a feature is never a Nation Supremacy requirement, and its limitations are not inherited (13A instruction §4.2). Nation Supremacy's mechanics remain owned by B-02…B-12.

### 1.2 Identifier convention

| Namespace | Meaning | Range |
|---|---|---|
| `13A-SRC-###` | One registered evidence row: a live retrieval, an official-documentation read, a secondary-source description or a recorded access limitation | `13A-SRC-001`…`13A-SRC-036`, contiguous, §3–§5 |
| `13A-FND-###` | One UI finding about Politics & War (P&W) with an evidence class | `13A-FND-001`…`13A-FND-040` in §7 |
| `13A-BP-###` | One benchmark **UI pattern** with a retain / adapt / reject disposition for Nation Supremacy | `13A-BP-001`…`13A-BP-028` in §8 |
| `13A-DR-###` | One independent design recommendation grounded in evidence plus reasoning | `13A-DR-001`…`13A-DR-024` in §9, contiguous |

### 1.3 Evidence classes (mandatory on every finding; D-199)

| Class | Meaning |
|---|---|
| `OBSERVED` | Directly retrieved by this pass on 2026-11-11 from the public response of the live site (server-rendered HTML/JSON). Quoted labels/columns/headings from that response are OBSERVED. |
| `DOCUMENTED` | Stated by an official Politics & War property (PWPedia article, changelog, test-server notice) retrieved live, describing behaviour this pass did not itself execute. |
| `SECONDARY` | Prior dated research already registered in this repository (11A, 10A, 09A, 08A, 07A) — cited by its own register IDs and retrieval dates, not re-verified today. |
| `INFERRED` | This pass's reading of retrieved material; never presented as an interface fact. |
| `NOT-RETRIEVABLE` | Content behind login, client-side rendering the retriever cannot execute, or an HTTP refusal — recorded with exactly what was returned; **no appearance or behaviour is invented for it.** |

Research boundaries (instruction §4.1): no account was created; no authenticated page was accessed; no external game state was altered; no access control was circumvented; no player was interacted with; no automated game action was taken.

### 1.4 Retrieval method and its honest limits

Each source row was fetched on 2026-11-11 through ordinary HTTPS GET requests, and the returned document text was read. The fetcher sees the server's HTML/JSON response but **does not execute heavy client-side JavaScript**; where a page's body is materially client-rendered or session-gated, the row records exactly what came back and is classified `NOT-RETRIEVABLE` (sometimes with observable shell text noted as partial `OBSERVED` evidence). This is a limitation of the pass, not a claim about how pages render in a human browser. Screenshots are **not** used anywhere: they cannot be verified by the next session, so every claim rests on retrievable text with a URL.

## 2. Primary benchmark identity

| Item | Value |
|---|---|
| Game | **Politics & War** |
| Official website | https://politicsandwar.com/ |
| Browser-based? | Yes — a browser nation-strategy game at ordinary URLs; no client download; it also exposes an external API and a public test server |
| Research date | 2026-11-11 (live); earlier dated rows come from this repository's prior P&W registers (2026-10-28 … 2026-11-05) |
| Why relevant | It is the genre-defining politics-and-war browser game and the owner-mandated primary UI benchmark; NS's own design already benchmarks against its economy, cities, politics, market, diplomacy, alliance, warfare, progression and fair-play systems |
| Screens/areas inspected (this pass) | Landing, nation search, alliance search, alliance page, nation profile, leaderboards, conflicts list, war timeline (boundary), treaty web, bounties, embargoes, radiation, advertisements, world graphs, world map, login, register, changelog, PWPedia, API price endpoint, test server |
| Functionality publicly observable | The full public read-side: world catalogue navigation, nation/alliance profiles, board and ledger tables with filters and pagination, treaty graph, world-risk data, advertisements, documentation index, changelog |
| Officially documented functionality | Authenticated-area behaviour (tax-bracket management path, war-policy screen options, alliance leadership surfaces) via PWPedia; test-server purpose via its own notice |
| Unavailable/inaccessible | All authenticated surfaces (economy/industry/military screens, market UI, notifications, alliance interiors), war timeline bodies, bulletin bodies, the fandom wiki and the API index (403 to the fetcher) — recorded, not invented |
| Relevant UI patterns | Persistent global shell; flat linkable world catalogue; universal table+filter+pagination grammar; tabbed leaderboards; relation graph with legend and filter tokens; public risk/aggregate screens; in-product changelog; option-with-cooldown policy screens |
| Strengths | Findability; transparency of the world state; consistent grammar; observable long history |
| Weaknesses/limitations | Desktop-first density; logged-out catalogue menu with no visible task aggregation (authenticated shell `NOT-RETRIEVABLE`); single-metric boards; knowledge displaced to Discord/wiki; geographic metaphor (not transferable); unverified non-colour CSS redundancy on `Color` bloc cells |
| Lessons for NS | §7–§9 |
| What NS must not copy | The map, the Discord-external membership flow, any hue-only visual encoding where `Color` bloc or status cues lack non-colour redundancy (NS enforces colour+glyph+text independently), an un-aggregated world-catalogue landing in place of Digest/Inbox, any proprietary graphic or branding, and any P&W mechanic treated as an NS rule |

**Supplementary titles qualify because** they are long-running browser nation-management politics-and-war games (Cyber Nations, eRepublik); they are used only for named gaps and never as the benchmark. NationStates, the genre's other major browser nation game, returned HTTP 403 to this fetcher and is recorded as an access limitation, consistent with the same limitation logged in Stage-1 reports. Prohibited categories (instruction §4.4 — mobile-only strategy, fantasy/medieval RTS, MOBA, shooters, 4X, grand strategy single-player, city builders, MMORPGs, card games, banking/SaaS dashboards) were **not** consulted as UI research comparators anywhere in this package.

## 3. Source register — Politics & War public interface (retrieved 2026-11-11)

| ID | Surface / URL | Class | What the retrieval returned | Limitation |
|---|---|---|---|---|
| `13A-SRC-001` | `https://politicsandwar.com/` | OBSERVED | Public landing "Politics and War"; entry links `Start Playing` → `/register/`, `Login` → `/login/`; sections on nation creation, alliances, war, trade, history; footer `Terms`, `Rules`, `Privacy` | Logged-out view only |
| `13A-SRC-002` | `https://politicsandwar.com/nations/` | OBSERVED | "Nation Search | Politics & War"; columns `Nation/Leader`, `Date Created`, `Alliance`, `Color`, `Cities`, `Score`; filter `Hide Gray Nations`; range pagination "0-15 of 14388"; global nav `World`/`Community` menus | Default sort only |
| `13A-SRC-003` | Global header navigation (as rendered on `/nations/`) | OBSERVED | Three top menus with exact hrefs — **Play:** `Home` `/`, `Start Playing` `/register/`, `Login` `/login/`; **World:** `Nations` `/nations/`, `Alliances` `/alliances/`, `Leaderboards` `/leaderboards/`, `Treaty Web` `/alliances/treatyweb/`, `Conflicts` `/world/conflicts/`, `Bounties` `/world/bounties/`, `Embargoes` `/world/embargoes/`, `Radiation` `/world/radiation/`, `Advertisements` `/world/advertisements/`, `Data Visualization` `/world-graphs/`, `World Map` `/worldmap/`; **Community:** `Forum` (forum.politicsandwar.com), `Discord`, `Wiki` (fandom), `Reddit`, `Test Server` (test.politicsandwar.com) | Logged-out menu set; authenticated shell menus are `NOT-RETRIEVABLE` |
| `13A-SRC-004` | `https://politicsandwar.com/nation/id=810166` | OBSERVED | Public nation profile sections in order: `Basic Information`, `International Relations`, `Economic`, `Domestic`, `Military`, `Nation Stats`, `Bounties`, `Map`, `Nation Activity`, `Nation Score Over Time`, `Score Component Breakdown`, `Nation Militarization Over Time`; fields incl. `Nation Name`, `Leader Name`, `Population: 1,000`, `GDP: $1.00`, `Government Type: Monarchy`, `Social Policies: Moderate`, `War Policy: Turtle`; empty state "There are no posted bounties" | One small young nation sampled; chart bodies client-rendered |
| `13A-SRC-005` | `https://politicsandwar.com/alliances/` | OBSERVED | "Alliance Search | Politics & War"; columns `Alliance`, `Date Created`, `Members`, `Color`, `Avg Score`, `Score`; filters incl. category/name/color/acronym, sort by score or date; detail URL `/alliance/id=745` family | Logged-out list |
| `13A-SRC-006` | `https://politicsandwar.com/alliance/id=7450` | OBSERVED | Public alliance page: `Leadership` with roles such as `Commander` and `Specialist`; `Members` list restricted (applicants visible to visitors); `Treaties` and `Wars` sections present; no `News`; member-authored text on the page reads "Applying on Discord is MANDATORY." | Interior alliance management (embassies, treasury, forum) not observable |
| `13A-SRC-007` | `https://politicsandwar.com/leaderboards/` | OBSERVED | Tabs `Nation`, `Alliance`, `Continent`, `Color Trade Bloc`, `Treasures`, `Moon Landing`, `Mars Landing`, `Commendations & Denouncements`; heading "Top 100 Nations by Score"; headers `Nation Name`, `Leader Name`, `Alliance`, `Color`, `Score`; 100 rows; no sidebar | Single-metric per tab |
| `13A-SRC-008` | `https://politicsandwar.com/world/conflicts/` | OBSERVED | Conflicts table columns `Date`, `Aggressor`, `Defender`, `Information`; scope tab `Active War`; detail links `/nation/war/timeline/war=<id>` (e.g. `2739562`) | Active scope only |
| `13A-SRC-009` | `https://politicsandwar.com/nation/war/timeline/war=2739562` | NOT-RETRIEVABLE | Response carried the global navigation, a language modal and cookie consent only; no timeline body text returned; an `Orbis Date` calendar label was visible in the returned navigation text | Timeline structure known only from `SECONDARY` 10A rows — no layout claimed |
| `13A-SRC-010` | `https://politicsandwar.com/alliances/treatyweb/` | OBSERVED | Public network visualization: alliance nodes, treaty edges; filter tokens `MDP MDoAP ODoAP ODP Protectorate NAP PIAT NPT Extension Offshore`; legend "MDP: Mutual Defense Pact." | Alliance-level only |
| `13A-SRC-011` | `https://politicsandwar.com/world/bounties/` | OBSERVED | Bounty table with type/amount filters; `Post a New Bounty` link visible to logged-out visitors (action login-gated) | — |
| `13A-SRC-012` | `https://politicsandwar.com/world/embargoes/` | OBSERVED | Columns `Date`, `Embargoer`, `Embargoed`, `Reason`; pagination "0-10 of 7200" | No filter row returned |
| `13A-SRC-013` | `https://politicsandwar.com/world/radiation/` | OBSERVED | Global and Regional Radiation Index tables with corresponding Food Production percentage decreases; counter "Nuclear Weapons Detonated in Last 24 Hours" | Aggregate risk presentation precedent |
| `13A-SRC-014` | `https://politicsandwar.com/world/advertisements/` | OBSERVED | "Player Advertisements"; 62 ads listed; columns incl. `Nation`, `Audience`, `Image`, `Votes`/`Upvotes`; "Create your own advertisement" login-gated | UGC surface; content rights not inspected |
| `13A-SRC-015` | `https://politicsandwar.com/world-graphs/` | OBSERVED | "Data Visualization" area with 30+ charts, e.g. "Active Nations in Last 3 Days"; public | Chart bodies client-rendered |
| `13A-SRC-016` | `https://politicsandwar.com/worldmap/` | OBSERVED | Canvas "World Map" showing the "Top 250 Nations"; links for `Nuclear Proliferation Map` and "All Nations: 14,388" | NS cannot adopt a geographic map (fixed constraint) — recorded as contrast only |
| `13A-SRC-017` | `https://politicsandwar.com/login/` | OBSERVED | Fields `E-mail Address`, `Password`, checkbox `Keep Me Logged In`, link `Forgot Password?` → `/login/reset/`; the page still renders the global shell (nav; resource strip showing `Money`, `Food`, `Coal` at `0.00`; language selector English/Spanish/French) | The zero-state shell proves the persistent frame; exact authenticated values unobservable |
| `13A-SRC-018` | `https://politicsandwar.com/register/` | OBSERVED | `E-mail Address`, `Confirm E-mail Address`, referrer's name; multiple-account warning; agreement to Terms and Rules | — |
| `13A-SRC-019` | `https://politicsandwar.com/changelog/` | OBSERVED | Dated operator changelog with inline expansion; recent entries `Donation Limit Reset` (11/01/2026), `Trick or Treating` (10/25/2026), `PW Patched for PHP2Shell` (10/22/2026), `Annual Pumpkin Contest` (10/21/2026); menu-toggle mobile notes appear in change code text | Official record of continuous UI/mechanic change |
| `13A-SRC-020` | `https://politicsandwar.com/pwpedia/` | OBSERVED | Official Q&A documentation; categories incl. `Alliance`, `Api`, `Basic Guides`, `City`, `Community Info`, `Faq`, `Improvements`, `Misc`, `Nation`, `National Projects`, `Resource`, `Units`, `War`; browse by category | Documents features; not screen captures |
| `13A-SRC-021` | `https://politicsandwar.com/pwpedia/article/tax-brackets` | DOCUMENTED | Alliance tax-bracket flow: in-game path "Bank then Taxes"; create a bracket (name + rates); "Change Member's Tax Bracket"; member dropdown | Official path naming an authenticated screen |
| `13A-SRC-022` | `https://politicsandwar.com/pwpedia/article/war-policy` | DOCUMENTED | War Policy screen options: `Attrition, Turtle, Blitzkrieg, Fortress, Moneybags, Pirate, Tactician, Guardian, Covert, Arcane`; wording "War Policy directly affects how your wars will look like"; "You can only change policy once every 60 turns" | Official documentation; NS never adopts the mechanic by citing it |
| `13A-SRC-023` | `https://politicsandwar.com/api/tradeprice/resource=coal` | OBSERVED | JSON `{"success": false, "general_message": "Invalid API key."}` — the same datum the UI publishes, exposed over a key-gated API | Automation surface evidence |
| `13A-SRC-024` | `https://politicsandwar.com/api/` | NOT-RETRIEVABLE | HTTP 403 to this fetcher | API documentation known via `SECONDARY` 11A rows |
| `13A-SRC-025` | `https://politicsandwar.com/bulletins/` | NOT-RETRIEVABLE | Shell-only response (language modal, cookie consent, `Start Playing`/`Login`); bulletin content requires a session | In-game news surface unobservable logged-out |
| `13A-SRC-026` | `https://politicsandwar.com/achievements/` | NOT-RETRIEVABLE | HTTP 403 to this fetcher | Achievement UI not observed; existence corroborated by `SECONDARY` 11A rows and the `Treasures`/`Commendations & Denouncements` leaderboard tabs |
| `13A-SRC-027` | `https://politicsandwar.fandom.com/wiki/Politics_and_War_Wiki` | NOT-RETRIEVABLE | HTTP 403 to this fetcher | Community-wiki displacement is itself a finding (`13A-FND-030`) |
| `13A-SRC-028` | `https://test.politicsandwar.com/` | OBSERVED + DOCUMENTED | "The test server is a copy of the game that runs a separate database."; "Do NOT expect any progress on the test server to be permanent."; registration disabled 3 days pre-tournament | Staging surface is player-facing — a genre-rare affordance |

## 4. Supplementary browser-game research (gap-driven, non-displacing)

| ID | Title / URL | Class (2026-11-11) | Retrieved | Gap it fills |
|---|---|---|---|---|
| `13A-SRC-029` | **Cyber Nations** — `https://www.cybernations.net/` and `https://www.cybernations.net/game_update_log.asp` | OBSERVED | Landing: browser nation simulation; `Register`, `Login`, `Top 10 Nations`; public activity log (aid offers, senate votes). Update log: 4 Apr 2025 "A more mobile-friendly version of the site is now available… improves navigation on phones and tablets with better scaling"; profile checkboxes `Enable Mobile Friendly View`, `Auto-Detect Mobile Browser`; 20 May 2014 merged resource rows plus "new bar charts to clean up scrolling"; 21 May 2014 "alliance activity log screen" for managers; 26 May 2014 improvement page shows unaffordable items "to see full descriptions"; 2014-era per-message alert opt-outs; 16 Jul 2014 comments on the Team Messages screen | (a) user-selectable mobile/desktop rendering; (b) inline charts as density control; (c) manager activity log as a first-class screen; (d) show-unaffordable-with-reason shopping; (e) notification opt-out granularity |
| `13A-SRC-030` | **eRepublik** — `https://www.erepublik.com/` | OBSERVED (landing) | "A new world is emerging"; browser-play strategy; `Sign up` / `Sign in with Facebook`; rule countries, build companies, fight battles | Genre corroboration of third-party-login entry and marketing framing; deeper surfaces authenticated and not probed |
| `13A-SRC-031` | **NationStates** — `https://www.nationstates.net/` | NOT-RETRIEVABLE | HTTP 403 to this fetcher (same limitation recorded in Stage-1 reports) | Recorded as an access limitation |

No other title was consulted; the prohibited-category list of instruction §4.4 was honoured.

## 5. Registered limitations / boundary rows

| ID | Boundary |
|---|---|
| `13A-SRC-032` | The authenticated P&W shell (economy, industry, military, market, diplomacy, notification surfaces) is not observable by this pass; statements about it are `DOCUMENTED` or `SECONDARY`, never `OBSERVED` |
| `13A-SRC-033` | Chart and graph bodies (score history, militarization, world graphs, treaty web layout) are client-rendered; container names and controls were seen, pixel behaviour was not claimed |
| `13A-SRC-034` | War timeline and battle-report bodies: `NOT-RETRIEVABLE` (`13A-SRC-009`); their information structure is carried by the dated 10A register (`WFS-*`), labelled `SECONDARY` |
| `13A-SRC-035` | Notification/alert placement: `NOT-RETRIEVABLE`; only the persistent shell's existence is `OBSERVED` (`13A-SRC-017`) |
| `13A-SRC-036` | Mobile rendering of P&W itself was not testable by this fetcher; changelog code-notes (`13A-SRC-019`) are the only signal and are marked `INFERRED`, low confidence |

## 6. Register integrity note

`13A-SRC-001`…`13A-SRC-036` occur once each and contiguously: §3 numbers 001–028 (Politics & War rows, including the recorded 403/session boundaries), §4 numbers 029–031 (the supplementary titles, with the NationStates 403 as the negative row), §5 numbers 032–036 (the registered limitation boundaries). Uniqueness and contiguity are machine-checked by `docs/qa_backups/13A_validate_ui_foundations.py`.

## 7. Findings register — Politics & War interface (primary benchmark)

| ID | Finding | Evidence | Class |
|---|---|---|---|
| `13A-FND-001` | The public world is a flat catalogue of independently addressable destinations (11 World items + leaderboards/treatyweb), all one click from the persistent header — findability without hierarchy | `13A-SRC-003` | OBSERVED |
| `13A-FND-002` | The application frame is persistent even outside a session: login and error surfaces render the same nav, resource strip (`Money`/`Food`/`Coal`) and calendar label (`Orbis Date`); zero-state values prove the strip is shell chrome, not page content | `13A-SRC-017`, `13A-SRC-009` | OBSERVED (+INFERRED placement) |
| `13A-FND-003` | The nation profile is the genre's central object: twelve stacked sections covering identity, relations, economy, domestic policy, military, stats, activity and three score/militarization chart areas | `13A-SRC-004` | OBSERVED |
| `13A-FND-004` | List screens share one grammar: table + filter controls + range pagination ("0-15 of 14388", "0-10 of 7200") across nations, alliances, conflicts, embargoes, bounties | `13A-SRC-002/005/008/011/012` | OBSERVED |
| `13A-FND-005` | Leaderboards are one-metric-per-tab, Top-100 by default, with quirky metric tabs (`Moon Landing`, `Mars Landing`, `Treasures`, `Commendations & Denouncements`) | `13A-SRC-007` | OBSERVED |
| `13A-FND-006` | War data disclosure is tiered: a public conflicts ledger with date/belligerents/detail-link, richer timeline pages behind session or client rendering this pass could not read | `13A-SRC-008/009` | OBSERVED + NOT-RETRIEVABLE |
| `13A-FND-007` | Treaty topology gets a first-class public visualization with named filter tokens and a legend (MDP/MDoAP/ODoAP/ODP/Protectorate/NAP/PIAT/NPT/Extension/Offshore) | `13A-SRC-010` | OBSERVED |
| `13A-FND-008` | Risk data is surfaced as world aggregates paired to consequences (radiation → food-production % decrease; detonations in last 24 h) plus a proliferation overlay | `13A-SRC-013/016` | OBSERVED |
| `13A-FND-009` | Social coordination migrates off-platform: alliance pages instruct "Applying on Discord is MANDATORY"; the Community menu itself lists Forum/Discord/Wiki/Reddit as parallel surfaces | `13A-SRC-006/003` | OBSERVED (implication INFERRED) |
| `13A-FND-010` | The public alliance page exposes leadership roles and applicant lists but hides member internals — graduated disclosure is enforced by page, not by note | `13A-SRC-006` | OBSERVED |
| `13A-FND-011` | In-game management paths are documented officially ("Bank then Taxes"; "Change Member's Tax Bracket"), showing stable menu vocabulary players can rely on | `13A-SRC-021` | DOCUMENTED |
| `13A-FND-012` | Policy surfaces present a closed set of named options (ten war policies) with cooldown disclosure ("once every 60 turns") and consequence preview language ("affects how your wars will look") | `13A-SRC-022` | DOCUMENTED |
| `13A-FND-013` | The world is machine-readable: the same market datum visible in UI is published through a key-gated public API — power users are expected, not fought | `13A-SRC-023/024` + `SECONDARY` 11A | OBSERVED + DOCUMENTED |
| `13A-FND-014` | The operator changes are public, dated and inline-expandable in a product changelog, including security-incident notices | `13A-SRC-019` | OBSERVED |
| `13A-FND-015` | A public **test server** with its own copy of the game is offered from the Community menu with explicit impermanence warning | `13A-SRC-003/028` | OBSERVED |
| `13A-FND-016` | Onboarding is a bare entry funnel (e-mail, referrer, terms) with the multi-account warning placed at registration itself; there is no observed in-product tutorial surface from the logged-out side | `13A-SRC-018` (+ boundary `13A-SRC-032`) | OBSERVED + boundary |
| `13A-FND-017` | Across public lists (`13A-SRC-002/005/007`), tables include both an explicit `Alliance` text column and a `Color` (color-bloc) column; HTML carries text labels, while rendered CSS swatch styling is unverified | `13A-SRC-002/005/007` | OBSERVED (HTML structure) + INFERRED limit |
| `13A-FND-018` | The benchmark world is geographic: a canvas World Map, `Continent` leaderboards — spatial situational awareness | `13A-SRC-016/007` | OBSERVED (non-transferable to NS) |
| `13A-FND-019` | Long-range history is browsable: 14,388 nations in the ledger, 7,200 embargo records, per-nation score-history charts | `13A-SRC-002/012/004` | OBSERVED |
| `13A-FND-020` | Aggregate world-health charts (activity in last 3 days, etc.) are public — meta-situation awareness without personal data | `13A-SRC-015` | OBSERVED |
| `13A-FND-021` | The header language selector (English/Spanish/French) and cookie banner show an international audience handled in the shell | `13A-SRC-017/009` | OBSERVED |
| `13A-FND-022` | Advertisements are a public, rated, player-authored content surface — UGC inside the navigation | `13A-SRC-014` | OBSERVED (governance implication INFERRED) |
| `13A-FND-023` | **Strength:** one-frame completeness — everything the world knows is reachable without leaving the persistent shell | `13A-SRC-003/017` | OBSERVED |
| `13A-FND-024` | **Strength:** table grammar consistency makes new screens cheap to learn | `13A-SRC-002…012` | OBSERVED |
| `13A-FND-025` | **Strength:** graduated disclosure (profile public → alliance interior gated → timeline gated) supports diplomacy research | `13A-SRC-004/006/009` | OBSERVED |
| `13A-FND-026` | **Logged-out boundary:** in the unauthenticated public navigation (`Play / World / Community`), no task aggregation ("what needs me") is present — the logged-out catalogue is world-centric; whether authenticated P&W surfaces provide task/alert queues is `NOT-RETRIEVABLE` (`13A-SRC-032`) | `13A-SRC-003`; boundary `13A-SRC-032` | OBSERVED (logged-out public catalogue) + NOT-RETRIEVABLE (authenticated shell) |
| `13A-FND-027` | **Limitation:** density without progressive disclosure (12-section profile page; Top-100 tables) — long-page scrolling as the navigation model | `13A-SRC-004/007` | OBSERVED (usability reading INFERRED) |
| `13A-FND-028` | **Limitation:** single-metric boards give no multi-dimensional comparison; players export to the API for that | `13A-SRC-007/023` | OBSERVED |
| `13A-FND-029` | **Limitation:** knowledge and coordination live off-platform (Discord mandatory for alliance entry; wiki external) — the UI under-serves its own social systems | `13A-SRC-006/027` | OBSERVED + NOT-RETRIEVABLE |
| `13A-FND-030` | **Limitation:** the geographic map and continent framing cannot be ported; NS must supply relational awareness instead | `13A-SRC-016`; fixed constraints | OBSERVED + constraint |
| `13A-FND-031` | **Accessibility boundary (corrected 13A-C1):** retrieved HTML tables (`13A-SRC-002/005/007`) display both a text `Alliance` column and a text `Color` (bloc) column — P&W does not omit alliance text labels in those tables; however, CSS swatches/badges and whether client-rendered colour cells carry non-colour symbols were not verified from server HTML | `13A-SRC-002/005/007` | OBSERVED (HTML columns) + NOT-RETRIEVABLE / unverified CSS visual channel |
| `13A-FND-032` | **Logged-out shell-fallback boundary (corrected 13A-C1):** unauthenticated GET requests to gated/script-dependent routes (`13A-SRC-009` timeline, `13A-SRC-025` bulletins) returned global shell chrome without an inline login-required body notice; this records unauthenticated route fallback behaviour only and does not establish whether authenticated player error/session states are hidden (`13A-SRC-032`) | `13A-SRC-009/025`; boundary `13A-SRC-032` | OBSERVED (logged-out HTTP fallback) + NOT-RETRIEVABLE (authenticated error states) |
| `13A-FND-033` | The benchmark's documentation is centralized, official, and category-stable (PWPedia mirrors the in-game section vocabulary) | `13A-SRC-020` | OBSERVED |
| `13A-FND-034` | Public aggregates are paired to mechanics consequences (radiation → production) — cause-and-effect disclosure | `13A-SRC-013` | OBSERVED |
| `13A-FND-035` | Deep history (score over time, activity feeds on profile) makes the nation page a retrospective dashboard | `13A-SRC-004` | OBSERVED |
| `13A-FND-036` | The treaty web encodes alliance-relation **type** per edge with a legend and per-type filters | `13A-SRC-010` | OBSERVED |
| `13A-FND-037` | Player-made content (ads) is integrated into world navigation with community rating | `13A-SRC-014` | OBSERVED |
| `13A-FND-038` | The world exposes machine symmetry: UI-visible data ↔ API-visible data | `13A-SRC-023` | OBSERVED + SECONDARY |
| `13A-FND-039` | The game ships its own staging surface (test server) as part of the public product | `13A-SRC-028` | OBSERVED |
| `13A-FND-040` | Logged-out visitors still get the full navigational frame — marketing, world and entry are one application | `13A-SRC-001/017` | OBSERVED |

## 8. Benchmark pattern register — retain / adapt / reject

| ID | Pattern (P&W evidence) | Disposition | NS reasoning |
|---|---|---|---|
| `13A-BP-001` | Persistent global frame with resource/status strip and calendar in every state (`13A-SRC-017`) | **Retain** | NS: identity strip = nation name, treasury band, stability, protection, turn countdown (D-027-safe values only) |
| `13A-BP-002` | Flat, deep-linkable catalogue of world destinations (`13A-FND-001`) | **Adapt** | NS keeps URL-addressability of every screen but organizes the authenticated shell task-first (Inbox/Digest), not world-first |
| `13A-BP-003` | One profile page per nation with stacked sections (`13A-SRC-004`) | **Adapt** | NS nation profile keeps the object-centric page but sections become tabbed/progressive to control density (Report 02 frustration evidence) |
| `13A-BP-004` | Universal table+filter+pagination grammar (`13A-FND-004`) | **Retain** | Adopt as a design-system rule (`13A-DS`); add saved views, column priority, and a card fallback on mobile |
| `13A-BP-005` | Top-100 single-metric leaderboards (`13A-SRC-007`) | **Adapt** | NS standings already require denominators and named populations (WEP-324/325): boards list *the* standing, not a rank number, and never imply live updating |
| `13A-BP-006` | Treaty web with typed edges + legend + filters (`13A-SRC-010`) | **Retain (as direction)** | Direct ancestor of NS's mapless Network View (FO-013, DP-003, SIM-012), filtered by posture/treaty class; edge labels must state the governing rule class |
| `13A-BP-007` | World-risk aggregate screens (`13A-SRC-013/015`) | **Retain with gate** | NS may publish aggregates only after the k=5/complementary-suppression check (D-027; TR-022) — pattern is the screen, rule is the disclosure policy |
| `13A-BP-008` | Public conflict ledger → gated timeline detail (`13A-FND-006/025`) | **Adapt** | NS follows B-10 visibility (WAR-085…088 band-not-exact; WAR-148 alliance isolation) — a War public list + owner-only board split |
| `13A-BP-009` | In-game menu vocabulary mirrored in official docs (`13A-FND-011/033`) | **Retain** | NS help surfaces (B-13 journeys) must use the same section names as screens; Report 07's legibility criteria already demand visible cause chains |
| `13A-BP-010` | Named-option policy screens with cooldown disclosure (`13A-SRC-022`) | **Retain** | NS axes changes (one axis per 12 turns, D-087) must show the cooldown **on the control**, echoing REQ-257 affordability-before-commitment |
| `13A-BP-011` | Machine API symmetry with UI (`13A-FND-038`) | **Defer** | Any NS automation surface is architecture/fair-play territory (B-12, UD rows); 13A records the *consistency* duty only: API-visible and screen-visible data must not diverge |
| `13A-BP-012` | Public changelog with incident notices (`13A-SRC-019`) | **Adapt** | NS TR-049/B-12 disclosure duties: a changelog surface is required; content rules come from B-12 MOD-017/notice discipline |
| `13A-BP-013` | Public test server (`13A-SRC-028`) | **Provisional → owner** | Cost/infrastructure territory (Category A/D); recorded as `13A-OQ`; NS design docs note only that any such surface must run identical rules |
| `13A-BP-014` | Multi-account warning placed at registration (`13A-SRC-018`) | **Retain** | Matches D-018's policy-first and B-03 §11 onboarding honesty; NS adds accessibility-compliant notice patterns |
| `13A-BP-015` | Colour-bloc and affiliation presentation across public lists (`13A-FND-017/031`: `Alliance` + `Color` text columns present; client CSS swatch/symbol channel unverified) | **Reject hue-only swatch reliance** | Even where text columns accompany colour blocs, NS independently bans relying on hue alone for any status, bloc or affiliation indicator and enforces colour + glyph + text (`13A-DR-015`, WCAG 1.4.1 / 2.2 AA intent, `DMP-164`, `REQ-321`) |
| `13A-BP-016` | Geographic world map (`13A-SRC-016`) | **Reject (constraint)** | Fixed constraint: mapless symbolic world (AI_CONTEXT §2; AP-002). The relational Network View is the situational-awareness surface instead |
| `13A-BP-017` | Off-platform social dependency (`13A-FND-029`) | **Reject** | NS bans real-time chat/Discord integration (D-133; ALL-161); the UI must therefore carry alliance coordination affordances B-09 defines — this pass's roadmap B-09 dependency paragraph |
| `13A-BP-018` | World-centric logged-out public navigation without visible task aggregation (`13A-FND-026`; authenticated P&W console `NOT-RETRIEVABLE` per `13A-SRC-032`) | **Reject (as authenticated landing model)** | NS's absence-respecting cadence (`DP-002`), `TR-089` and `REQ-022` independently require an Inbox/Digest spine as the authenticated Home surface rather than a world-catalogue landing (`13A-DR-001`) |
| `13A-BP-019` | Long-page density as the default view (`13A-FND-027`) | **Adapt** | Progressive disclosure + configurable panels (Report 02 overload evidence; Report 04 persona session shapes) |
| `13A-BP-020` | Single-metric boards limit comparison (`13A-FND-028`) | **Adapt** | NS's ten standings + World Standing Eligibility design (B-11) needs a comparison surface inside visibility rules — recorded as candidate screen `SCR-077`-area, owner/Prompt 14 dependencies kept |
| `13A-BP-021` | Unauthenticated GET on gated/script-dependent routes falls back to global shell without inline body notice (`13A-FND-032`; authenticated P&W error states `NOT-RETRIEVABLE` per `13A-SRC-032`) | **Adapt (replace with explicit states)** | NS defines loading/empty/error/permission-denied states as first-class surfaces anchored in NS rules (`08C §12.5/12.7`, `D-194`, `REQ-821`) so gated or failing routes never fail silently or omit state explanation |
| `13A-BP-022` | UGC surfaces inside world navigation (ads) (`13A-SRC-014`) | **Reject for launch** | NS has no advertising design; adding one would invent scope (policy §4: no unnecessary features) |
| `13A-BP-023` | Multilingual shell (`13A-FND-021`) | **Provisional** | Localization is not in any accepted requirement; recorded as a question, no screens designed |
| `13A-BP-024` | Public history depth (`13A-SRC-019/004`) | **Retain in bounds** | NS history disclosure is ruled by D-026 retention classes and the chronicle (B-11); browsability duty survives, raw-scale claim does not |
| `13A-BP-025` | CN: user-selectable mobile/desktop rendering (`13A-SRC-029`) | **Adapt** | Evidence the genre's audiences are cross-device; NS responsive philosophy treats mobile as first-class (see responsive doc); the *switch* itself is provisional |
| `13A-BP-026` | CN: inline bar charts replacing scrolling numbers (`13A-SRC-029`) | **Retain** | Matches NS's six-number-type discipline when paired with correct state labelling (forecast vs actual) |
| `13A-BP-027` | CN: manager activity-log screen + alert opt-outs (`13A-SRC-029`) | **Adapt** | NS notification presentation tiers must respect non-opt-out rules (DIP N-series "cannot opt out"; REQ-731 no second channel) |
| `13A-BP-028` | CN: show-unaffordable-with-reason purchase listing (`13A-SRC-029`) | **Retain** | Direct match to ECN-181/URB-152/08C §12.7 duty: disabled action must state why before the click |

## 9. Independent recommendations (grounded, not imitative)

| ID | Recommendation | Basis (P&W / supplementary / NS requirement / reasoning) |
|---|---|---|
| `13A-DR-001` | Home is a **Command Digest + Inbox pair**, not a dashboard of world stats: "what happened since last slot" + "what needs you before the next slot" | Independently required by NS rules (`TR-089` digest-first, `REQ-022` re-entry, `DP-002`, `Report 04` persona time-shape); contrasted with logged-out P&W world-catalogue navigation (`13A-FND-026`; authenticated Home `NOT-RETRIEVABLE` per `13A-SRC-032`) |
| `13A-DR-002` | One persistent identity strip: nation, treasury band, stability band, protection badge, **next-boundary countdown** in turns + UTC | P&W frame persistence (`13A-FND-002`) adapted to NS cadence (D-027-safe bands; B-02 slot clock) |
| `13A-DR-003` | A relational **Network View** as the world-situational surface (typed edges, filters, legend), explicitly replacing the map | `13A-BP-006/016`; FO-013 keystone; DP-003; fixed mapless constraint |
| `13A-DR-004` | One table grammar project-wide (columns/filters/pagination/saved views/mobile cards) declared in the design system | `13A-FND-004` strength; PR-07 consistency principle |
| `13A-DR-005` | Object pages keep the benchmark's profile-as-central-object pattern but adopt progressive sectioning and a sticky section index | `13A-SRC-004` + `13A-FND-027` + Report 02 overload evidence |
| `13A-DR-006` | Every aggregate on every screen carries its disclosure gate visibly (`k=5` suppression states are a designed state, not an absence) | P&W aggregates (`13A-FND-034`); D-027/TR-022/WEP-663 |
| `13A-DR-007` | Standings screens present *named standings* with denominator/window/eligibility, never a single "rank" | `13A-BP-005`; B-11 WEP-324/325/361/362 |
| `13A-DR-008` | War surfaces split exactly along B-10 lines: public ledger, owner-only operations board, alliance *management-only* view — three audiences, three visibility classes, no merged view | `13A-FND-006`; WAR-085…088; WAR-148–150; roadmap Prompt-13 boundary paragraph |
| `13A-DR-009` | Cooldowns and change-limits render **on the control** with the governing rule named | P&W policy screens (`13A-SRC-022`); NS D-087, REQ-257 pattern |
| `13A-DR-010` | An in-product help layer keyed to the same section vocabulary as the nav, carrying what P&W displaces to wiki/Discord | `13A-FND-029/033`; DP-004; SYS-018; Report 02 F-010 |
| `13A-DR-011` | Notification presentation tiers (blocking / digest / ambient) built over existing events only — no new notification facts invented by UI | `13A-BP-027`; REQ-731; DIP/AN/WAR matrices already fixed |
| `13A-DR-012` | Mobile is a *re-prioritized* view (Inbox, Digest, countdown, confirmations first; Network View optional deep mode), not a shrunken desktop; a rendering-mode switch is deferred as provisional | `13A-SRC-029`; RD rules in the responsive doc; owner-reserved numbers stay open |
| `13A-DR-013` | Administrative surfaces live in a separate shell with role-gated entry and no player-visible affordance leakage | P&W role-graduated pages (`13A-FND-010`); D-042; ADM reviewer rules; instruction §8.I |
| `13A-DR-014` | A public changelog surface exists in B-13 scope with content governed by existing disclosure rules | `13A-FND-014`; TR-049; MOD-017 |
| `13A-DR-015` | Colour usage rule: nation/affiliation/status colour may inform, may never encode alone (require colour + glyph + text) | Independent NS accessibility requirement (`DMP-164`, `REQ-321`, WCAG 1.4.1 / 2.2 AA design intent); bounded against `13A-FND-017/031` (P&W HTML pairs `Alliance` text with `Color` columns; CSS swatch redundancy unverified) |
| `13A-DR-016` | The application never renders a permission grant: all actionability is server-decided and denial states name their category | P&W gated pages (`13A-FND-010`); REQ-553/645; audit §4.11 |
| `13A-DR-017` | Deep-link every screen and every object; treat URLs as part of the UI contract | `13A-FND-001`; Stage-2 traceability culture |
| `13A-DR-018` | Design error/empty/denied states as named first-class states with copy from owning rules | Independently grounded in NS rules (`08C §12.5/12.7`, `B-02..B-12` failure catalogues, `PROVISIONAL_BLOCK` `D-194`); informed by bounded logged-out shell-fallback observation (`13A-FND-032`, `13A-SRC-032`) |
| `13A-DR-019` | Session-safety: nothing on screen may make absence feel like loss (no streaks, no FOMO timers); countdowns mark opportunity, never obligation | AP-001; DP-002; D-021; Report 04 cadence policy |
| `13A-DR-020` | Comparison and history views must state their source slot and retention boundary (what is no longer hot is *labelled*, not silently missing) | `13A-FND-019` adapted to D-026 |
| `13A-DR-021` | Alliance screens render the *blocked* cases explicitly (NAP block, same-Alliance ban) with reason strings from B-09/B-10, no leak | WAR-149; ALL-161/167/168; roadmap B-09 paragraph; `13A-FND-010/012` graduated/cooldown disclosure |
| `13A-DR-022` | Tax/ARL/funding screens are per the owner-authorized B-09 rule set only; UI adds no capability the rules do not grant (e.g. no implicit delegation) | `13A-SRC-021` analogy; D-140/D-141/UD-045/046 boundaries |
| `13A-DR-023` | Prototype/staging questions (public test server) stay out of screen scope until owner decides cost | `13A-FND-039` vs Category A/D |
| `13A-DR-024` | 13B must re-verify every P&W assumption used in screen specs against this register's classes; `NOT-RETRIEVABLE` areas stay hypothesis-flagged, never drawn from memory | D-199; instruction §4.6 |

## 10. What Politics & War demonstrated, honestly bounded

The benchmark study covered all eight instruction areas (A overall interface / shell; B nation management pages; C politics surfaces; D economy/market pages; E diplomacy/alliance pages; F war/conflict surfaces; G rankings/progression surfaces; H player-experience qualities). Its logged-out reach gave direct OBSERVED evidence for the frame, the catalogue, profiles, boards, ledgers, the treaty web, risk aggregates, entry surfaces and official documentation, and documented (not observed) evidence for authenticated management paths. The authenticated core — the actual nation console — remains this pass's largest evidence boundary; it is carried as `NOT-RETRIEVABLE` rows and `SECONDARY` cross-references, and it constrains gate P13A-02 to the completeness of *publicly accessible* investigation, which is what instruction §4.1 mandates.

### 10.1 Primary-attention distribution

Yes — Politics & War received the primary research effort. Of the 36 numbered source rows, **33 are Politics & War**: `13A-SRC-001`…`13A-SRC-028` (21 `OBSERVED` live public-interface reads — 20 strictly `OBSERVED` plus `13A-SRC-028` hybrid `OBSERVED + DOCUMENTED` — 2 `DOCUMENTED` official-documentation reads (`13A-SRC-021/022`), and 5 `NOT-RETRIEVABLE` rows recording what could not be retrieved and why) and the five P&W registered boundaries `13A-SRC-032`…`13A-SRC-036`. `13A-SRC-029` (Cyber Nations) and `13A-SRC-030` (eRepublik) are the two supplementary evidence rows and `13A-SRC-031` (NationStates) is the supplementary negative access row. The findings register is 40 of 40 rows about Politics & War; the benchmark-pattern register is 24 of 28 rows P&W-derived, the four exceptions being the Cyber Nations gap-fillers. No prohibited research category (instruction §4.4) was consulted anywhere in this package. Gates `P13A-02/03/04` grade this distribution.

## 11. Research limitations recorded

1. Single-day live retrieval (2026-11-11); P&W ships changes continuously (`13A-SRC-019`) — tomorrow's layout may differ; nothing in this register claims permanence.
2. The retriever sees server HTML, not executed client state (`13A-SRC-009/025/033`).
3. No login, therefore no authenticated-surface observation of any kind (instruction §4.1 boundary respected).
4. eRepublik/Cyber Nations pages were skimmed for named gaps only; their depth is deliberately not benchmark-grade.
5. NationStates, fandom wiki, P&W API index and achievements returned 403 to the fetcher; those are recorded access limits, not absence of functionality.
