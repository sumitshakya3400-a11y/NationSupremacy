# Politics & War research — domestic politics, government, policy and approval

**Version:** 1.0 · **Created:** 2026-10-25 · **Stage 2, Prompt 06A**
**Status:** Research record. Every finding is labelled; nothing here is a Nation Supremacy rule. The rules are in [B-06](../12_population_and_domestic_politics.md).
**Access date:** 2026-10-25 (all pages below were read on this date).

---

## 1. Scope and method

Prompt 06A needs to know what Politics & War (P&W) actually does with **population, government type, national policy, public approval and leadership** before Nation Supremacy designs its own system. This report records:

1. the current implemented mechanics, read from the game's own public pages and from archived copies of its community wiki;
2. community proposals and criticisms, read only at snippet level because the P&W forum would not load;
3. the design conclusions drawn for Nation Supremacy.

**Evidence grades used below**

| Grade | Meaning |
|---|---|
| **V1** | Read directly from the live game at `politicsandwar.com` on 2026-10-25 |
| **V2** | Read from an archived copy of the community wiki (Wayback Machine snapshot, date recorded) |
| **V3** | Read from a search-engine snippet; the page itself could not be loaded |
| **C** | Community proposal, criticism or opinion — never evidence of an implemented mechanic |
| **N** | Nation Supremacy recommendation |

**Known limitations.**

- `politicsandwar.fandom.com` returned **HTTP 403** to this session. Archived snapshots were used instead and their snapshot dates are recorded with each page. The wiki is community-maintained and may lag the live game.
- `forum.politicsandwar.com` **timed out** on every attempt. Forum threads are therefore described from search-result snippets only; no thread was read in full, and no quotation beyond the snippet is claimed. No thread date, author or consensus is invented.
- P&W's live nation pages expose only the fields a logged-out visitor can see. Nation creation, the edit page and the policy questionnaire require an account and were not exercised.
- No P&W account was created and no in-game test was run. Every "current mechanic" claim below is documentary.

---

## 2. What the game currently does

### 2.1 Government type is cosmetic and freely changeable

**V2 — [Government Type](https://web.archive.org/web/20260203185320/https://politicsandwar.fandom.com/wiki/Government_Type), snapshot 2026-02-03.** The page states:

> "Government Type is an option you are able to pick in order to define the political system by which your nation is controlled. This option does not provide any nation bonuses and exists merely for role-playing reasons."

There are **32 standard types** plus one Easter-Egg type (`Mindhive`, reached by editing the page source). The list is a glossary of real-world forms — Absolute Monarchy, Anarchy, Aristocracy, Banana Republic, Communist Democracy, Constitutional Monarchy, Constitutional Republic, Demarchy, Democracy, Democratic Republic, Dictatorship, Federal Republic, Monarchy, Noocracy, Oligarchy, Parliamentary Democracy, Parliamentary Republic, People's Republic, Republic, Social Democracy, Socialist Dictatorship, Socialist Republic, Socialist Theocracy, Stratocracy, Theocracy, Theocratic Democracy, Theocratic Dictatorship, Theocratic Republic and others. The player may change it **"whenever you want"** on the nation Edit page.

**V1 — live nation page, `politicsandwar.com/nation/id=1`, 2026-10-25.** The page shows `Government Type: Republic` alongside `Domestic Policy: Manifest Destiny`, `Social Policies: Moderate`, `Economic Policies: Moderate`, `State Religion: Mysticism`, `National Animal: Bald eagle` and `War Policy: Turtle`. These are nation-page customisation fields, not a cabinet or a parliament.

**N.** P&W's government is a label with an icon. It has no opportunity cost, no permanence and no mechanical consequence, so it cannot support a strategy. Nation Supremacy's whole reason for a six-type permanent roster is to make this choice *the* long-horizon identity decision.

### 2.2 Social and economic policies are questionnaires with no effect

**V2 — [Social Policies](https://web.archive.org/web/20251230141257/https://politicsandwar.fandom.com/wiki/Social_Policies), snapshot 2025-12-30.** Social Policies are set by "an in-game questionnaire which rates responses on a scale from anarchist to fascist". Seven ratings exist (Anarchist, Libertarian, Liberal, Moderate, Conservative, Authoritarian, Fascist), the default is Moderate, and the page says the policies "are entirely cosmetic, and have no effect on the game."

**V2 — [Economic Policies](https://web.archive.org/web/20260101134501/https://politicsandwar.fandom.com/wiki/Economic_Policies), snapshot 2026-01-01.** A second questionnaire rates a seven-point left–right scale (Extreme Left … Extreme Right), default Moderate. The page calls them "entirely cosmetic", adding that they affect only the national tax rate, "which is itself purely cosmetic".

### 2.3 The national tax rate is deliberately revenue-neutral

**V2 — [National Tax Rate](https://web.archive.org/web/20220715054932/https://politicsandwar.fandom.com/wiki/National_Tax_Rate), snapshot 2022-07-15.** The rate is used to determine income, floats between 5% and 50%, and is set by the economic-policy questionnaire. The page states that citizens' average income moves **inversely** with the rate, so "no matter how high or low your national tax rate is, you cannot manipulate it to earn more money"; the rate "has no effect on the nation's revenue".

**N.** This is an explicit rejection of the tax rate as a lever. Nation Supremacy's B-04 makes the rate a real lever and Prompt 06A gives it a real political cost (`stability_factor_bp` and constituency support). The reference is useful precisely as the thing not to copy: a cosmetic tax slider removes a decision and teaches players that the number is noise.

### 2.4 Domestic Policy is the one policy with a mechanical effect

**V2 — [Domestic Policy](https://web.archive.org/web/20251118170338/https://politicsandwar.fandom.com/wiki/Domestic_Policy), snapshot 2025-11-18.** Six mutually exclusive emphases, each a flat percentage:

| Policy | Effect | Description on the page |
|---|---|---|
| Manifest Destiny | new city cost **−5%** | "The pursuit of rapid expansion." |
| Urbanization | infrastructure cost **−5%** | "The pursuit of industrialization and development." |
| Technological Advancement | national project cost **−5%** | "The pursuit of increasing scientific knowledge." |
| Open Markets | gross income **+1%** | "The pursuit of maximizing gains from trade." |
| Imperialism | military upkeep **−5%** | "The pursuit of growth through military dominance." |
| Rapid Expansion | land cost **−5%** | "The pursuit of sprawling land areas for your nation." |

The page states three additional rules:

1. **Cooldown:** "You can only do this once every 60 turns (5 days), so be careful."
2. **Amplifier:** the effect is increased by the Government Support Agency national project (5% → 7.5%, 1% → 1.5%).
3. **Stacking:** policy and project discounts stack **additively** — Urbanization (−5%) + Center for Civil Engineering (−5%) + Advanced Engineering Corps (−5%) = −15% infrastructure cost. Manifest Destiny is applied **after** city-cost project discounts.

**N.** This is the strongest single lesson in the report. One mutually exclusive emphasis, a clear label, a visible percentage and a real cooldown is legible and strategic. Nation Supremacy adopts the *shape* — a small number of mutually exclusive settings with a cooldown — and rejects three parts: the percentage-discount-only effect (it collapses into "pick the discount for your next purchase"), the additive stacking (B-05 already fixes one discount source per cost), and the amplifier project (it makes the rich richer and doubles the same effect).

### 2.5 Approval Rating is an unbounded score displayed as a percentage and has no effect

**V2 — [Approval Rating](https://web.archive.org/web/20260131173457/https://politicsandwar.fandom.com/wiki/Approval_Rating), snapshot 2026-01-31.** Approval is "a point-based system represented as a percentage, between 0 and 100%". The underlying points "can vary from infinitely negative, to infinitely positive"; below 0 the display is 0%, above 100 it is 100%. The page states plainly: "The Approval Rating does not affect your nation in any way. It is merely used for roleplay purposes." Two achievements exist for reaching thresholds.

The drivers are published as a table:

| Action-based factor | Points |
|---|---:|
| Declaring a war | −5 |
| Winning a war | +8 |
| Losing a war | −5 |
| Having war declared on your nation | −3 |
| Failed espionage operation | −5 |
| Successful but exposed espionage operation | −3 |
| Someone else's successful espionage on you | −5 |
| Someone else's failed espionage on you | +2 |
| Building a new city | +5 |
| Building a new national project | +5 |

| Turn-based factor | Points |
|---|---:|
| Base increase | +0.025 |
| Population density | (150 − density) × 0.001 |
| Pollution | −(pollution) × 0.0001 |
| Unable to pay expenses | −0.5 |
| Out of food | −0.5 |

**V1 — live nation page, 2026-10-25.** Nation 1 shows `Approval Rating: 0% (-596.02)`, confirming the unbounded underlying score and the clamped display.

**N.** Two findings matter. First, the *representation* is good: an underlying score with a clamped, familiar percentage display. B-06 instead stores a bounded 0–100 value with a movement cap, because a bounded value makes the arithmetic auditable and prevents the "−596" display, which tells a player nothing actionable. Second, the *drivers* are almost entirely war and espionage, with a near-zero per-turn drift; approval is a war record, not a judgement on governance. B-06 inverts that: peace-time governance drives approval continuously, and Prompt 10 will add war as one input among several.

### 2.6 Population is capacity-based, with disease and crime mortality

**V2 — [City](https://web.archive.org/web/20251119062441/https://politicsandwar.fandom.com/wiki/City), snapshot 2025-11-19.** Cities are "the major building blocks"; they increase maximum population and maintain current population, and hold infrastructure, land and improvements. Infrastructure raises the maximum population and gives one improvement slot per 50 infrastructure. Land lowers disease and raises farm output. The final population is affected by **city age** ("the older the city, the larger a bonus"; negligible below 200 days), **disease** (kills people and lowers the working population), and **crime** (kills citizens; rises with base population, falls with commerce and police stations).

**N.** P&W's population is a *capacity* number with two mortality meters attached; it is not a political variable and has no growth decision beyond buying infrastructure and land. B-05 already replaced the land/improvement model with development capacity and housing. B-06 therefore adds the missing half: a national population that grows toward housing and responds to food and approval, without disease or crime meters (they would be a second and third penalty on the same infrastructure).

### 2.7 There are no elections and the leader is a custom name

**V1 — live nation page, 2026-10-25.** The page names a leader ("led by President Wallace Drake") but exposes no election, party, cabinet, confidence vote or succession mechanic.

**V2 — Government Type page.** Nothing about leadership change; the government label can be edited at will, which implies the leader is a cosmetic field too.

**V3 — search results.** No P&W election mechanic surfaced in any query. Searches for P&W elections returned only real-world political science. This is absence of evidence, not proof of absence, but the wiki's mechanics pages list no election, and the Approval Rating page — which lists every approval driver — has no election factor.

**N.** Prompt 06B designs elections, campaigns, retention and crises from scratch. P&W supplies no precedent to copy, only a warning: a political system without consequences is decoration.

### 2.8 Same-network restrictions exist, and they are narrow

**V1 — [Game Rules](https://politicsandwar.com/rules/), 2026-10-25.** Rule 1 prohibits more than one nation per player. Rule 2 permits multiple nations per network "so long as each nation is owned and controlled by a separate individual", imposes automatic restrictions on same-network nations, forbids using alliance banks to evade them, and forbids two same-network nations declaring war on the same target. Rule 3 forbids new nations sending "all or most" of their money and resources away.

**N.** This corroborates B-03's pair model (D-034/D-035) and its no-perfect-identification posture. It does not change B-06. It is recorded because the political system must not create a new transfer route (for example, a policy that moves value between nations) — it does not.

---

## 3. Community proposals and criticisms

The forum could not be loaded. The rows below are **snippet-level only**; they establish that a proposal exists and roughly what it argues, not its full text, its support or its outcome. Dates are those shown by the search result.

| Topic / thread | Date shown | What the snippet shows | Status | Relevance |
|---|---|---|---|---|
| **Government Type Bonuses** (`forum.../topic/21742`) | 2017-11-22 (comment) | "Democracies have lower gross income every X number of turns because of election uncertainty, but higher satisfaction. Dictatorships have lower …" | **C** — proposal; not implemented | The earliest proposal found for permanent government modifiers with election-driven income swings. Nation Supremacy adopts permanent modifiers, but not periodic income shocks. |
| **Make Approval Rating Mean Something** (`forum.../topic/23354`) | undated in snippet | A reply: "just make it so that you get a …" | **C** — proposal | Confirms that players noticed approval is inert and wanted a payoff. |
| **How Does Approval Ratings Work?** (`forum.../topic/36187`) | undated in snippet | A reply: "Winning wars is usually the best way to improve your …" | **C** — community explanation | Matches the wiki's war-dominated driver table; approval is read as a war record. |
| **Proposal: Policy & Approval Rating rework** (`forum.../topic/53421`) | 2025 | Author Danzek; "Per the result of design poll: 'Nation Simulation/RP - Improved nation …'" | **C** — proposal | A recent, poll-driven attempt to make policy and approval matter. No evidence of implementation. |
| **Roberts' Grand Comprehensive Roleplay-Update Suggestion** (`forum.../topic/53234`) | 2025-08-20 | "Government Types -- Give each government type a bonus and a malus that directly relate to economic specialization." | **C** — proposal | The closest community statement of Nation Supremacy's direction: a bonus *and* a malus, tied to strategy. |
| **Effect of Leader's Rating + AI-Powered Local News** (`forum.../topic/50173`) | not retrieved | Not retrieved beyond the title | **C** — unverified | Suggests appetite for leader-level feedback; Prompt 06B may revisit. |
| **Internal Politics** (`forum.../topic/24270`) | not retrieved | Not retrieved beyond the title | **C** — unverified | Suggests long-standing interest in an internal-politics layer. |
| **Please Add More Decisions in P&W** (`forum.../topic/31162`) | not retrieved | Not retrieved beyond the title | **C** — unverified | Genre demand for decisions with consequences. |

**No claim of consensus is made.** The forums show recurring, multi-year interest in making government and approval meaningful; they do not show that any specific proposal was adopted. The game's own wiki and live pages show that none of the numeric proposals is live.

---

## 4. Comparison table

| Topic | Verified P&W mechanic | Community proposal or criticism | Evidence quality | Nation Supremacy recommendation |
|---|---|---|---|---|
| Government type | 32 + 1 labels; **no bonuses**; changeable at will | Give each type a bonus and a malus (2025); election-linked income swings (2017) | **V2/V1** for the mechanic; **C** for proposals | Six types, chosen once at creation, **permanent**, each with a benefit, a cost, a stability cap and policy locks (D-084/D-085) |
| Leadership | Player-named leader; no elections, parties or succession | Leader-rating and AI-news ideas | **V1**, absence of evidence | Prompt 06B owns elections, succession and crises; 06A defines the state and the inputs |
| Social policy | 7-point questionnaire; **cosmetic** | Rework proposals | **V2** | Rejected as a mechanic. A questionnaire that changes nothing is noise; B-06 uses two named axes instead |
| Economic policy | 7-point questionnaire; cosmetic; tax rate revenue-neutral | Policy rework (2025) | **V2** | Rejected. Tax is a real lever (B-04) and the fiscal axis is a real choice |
| Domestic policy | 6 emphases, each **5%** (or +1% income); 60-turn cooldown; amplifier project; additive stacking | — | **V2** | Adopt the shape (few, exclusive, cooldown); reject discount-only effects, stacking and amplifiers. Two axes with support and revenue effects (D-086) |
| Approval rating | Unbounded score shown 0–100%; **no effect**; driven by war/espionage, tiny per-turn drift | "Make approval mean something" | **V2 + V1** | Bounded 0–100 approval, driven by governance and constituencies, feeding stability, elections and crises (D-082) |
| Tax rate | 5–50%, **revenue-neutral by design** | — | **V2** | Real lever with a stability and support cost (B-04 + D-086) |
| Population | Capacity from infrastructure/land; disease and crime kill; city-age bonus | — | **V2** | National population, housing hard cap, food- and approval-sensitive growth, no disease/crime meters (D-081) |
| Same-network rules | One nation per player; multiple per network if separate people; pair restrictions; no bank evasion | — | **V1** | Already fixed by B-03; B-06 adds no transfer route |

---

## 5. What Nation Supremacy takes from the reference

**N1 — A label is not a government.** P&W proves that a cosmetic government type is ignored. The six-type roster must change at least four measurable things: stability, service cost, research rate and which policies are legal.

**N2 — Few, exclusive, legible settings beat long questionnaires.** The one policy with an effect (Domestic Policy) is the one players discuss. Two axes with three settings each is the smallest frame that still supports different strategies.

**N3 — A cooldown is the right limit for policy.** P&W uses 60 turns; B-06 uses 12 turns per axis because a two-hour turn makes 60 turns five days, which is too slow for a game whose whole cadence is a two-hour boundary. The cooldown exists to stop cost/support farming, not to punish experimentation.

**N4 — Approval needs a consequence to be worth showing.** P&W's own wiki says approval does nothing. B-06 makes it the input to stability, growth and (06B) elections and crises.

**N5 — Do not copy the discount stack.** P&W's 5% + 5% + 5% = 15% stack is exactly the compounding B-05 already forbids. B-06's government and policy effects are flat integers or single basis-point shifts applied once.

**N6 — Keep the arithmetic hand-checkable.** P&W's approval table is a list of flat point changes; that is why players can understand it. Every B-06 formula is integer arithmetic with a stated floor or ceiling.

---

## 6. What Prompt 06B must add

This report deliberately stops at the foundation. The following are **not** researched to decision level here and must be researched and decided in Prompt 06B:

1. The election interval (the brief proposes 240 turns) and the campaign window.
2. Candidate registration, campaigning and vote calculation.
3. The consequence of losing an election (the brief proposes 24 turns).
4. Retention rules for monarchies, dictatorships and juntas.
5. Unrest and political crisis (the brief proposes 36–48 turns).
6. The proposed 75% production reduction and zero-tax period.
7. Leadership-loss recovery and player access.

Prompt 06B must extend the same formula register (`F-PD-…`) rather than create a second one, and must consume — not redefine — `approval`, `stability_bp`, `legitimacy`, the constituency supports and the political state defined in B-06.

---

## 7. Sources read

| Source | URL | Read | Grade |
|---|---|---|---|
| P&W home | https://politicsandwar.com/ | 2026-10-25 | V1 |
| P&W game rules | https://politicsandwar.com/rules/ | 2026-10-25 | V1 |
| Live nation page (id=1) | https://politicsandwar.com/nation/id=1 | 2026-10-25 | V1 |
| Government Type (wiki) | https://web.archive.org/web/20260203185320/https://politicsandwar.fandom.com/wiki/Government_Type | 2026-10-25 | V2 |
| Approval Rating (wiki) | https://web.archive.org/web/20260131173457/https://politicsandwar.fandom.com/wiki/Approval_Rating | 2026-10-25 | V2 |
| Domestic Policy (wiki) | https://web.archive.org/web/20251118170338/https://politicsandwar.fandom.com/wiki/Domestic_Policy | 2026-10-25 | V2 |
| Social Policies (wiki) | https://web.archive.org/web/20251230141257/https://politicsandwar.fandom.com/wiki/Social_Policies | 2026-10-25 | V2 |
| Economic Policies (wiki) | https://web.archive.org/web/20260101134501/https://politicsandwar.fandom.com/wiki/Economic_Policies | 2026-10-25 | V2 |
| National Tax Rate (wiki) | https://web.archive.org/web/20220715054932/https://politicsandwar.fandom.com/wiki/National_Tax_Rate | 2026-10-25 | V2 |
| City (wiki) | https://web.archive.org/web/20251119062441/https://politicsandwar.fandom.com/wiki/City | 2026-10-25 | V2 |
| Government Type Bonuses (forum) | https://forum.politicsandwar.com/index.php?/topic/21742-government-type-bonuses/ | snippet only | V3/C |
| Make Approval Rating Mean Something (forum) | https://forum.politicsandwar.com/index.php?/topic/23354-make-approval-rating-mean-something/ | snippet only | V3/C |
| How Does Approval Ratings Work? (forum) | https://forum.politicsandwar.com/index.php?/topic/36187-how-does-approval-ratings-work/ | snippet only | V3/C |
| Policy & Approval Rating rework (forum) | https://forum.politicsandwar.com/index.php?/topic/53421-proposal-policy-approval-rating-rework/ | snippet only | V3/C |
| Roberts' roleplay update suggestion (forum) | https://forum.politicsandwar.com/index.php?/topic/53234-roberts-grand-comprehensive-roleplay-update-suggestion/ | snippet only | V3/C |
| Effect of Leader's Rating + AI news (forum) | https://forum.politicsandwar.com/index.php?/topic/50173-effect-of-leader-s-rating-ai-powered-local-news/ | title only | C |
| Internal Politics (forum) | https://forum.politicsandwar.com/index.php?/topic/24270-internal-politics/ | title only | C |
| Please Add More Decisions (forum) | https://forum.politicsandwar.com/index.php?/topic/31162-please-add-more-decisions-in-pw/ | title only | C |

---

## 8. Revision history

**v1.0 (2026-10-25).** First issue for Prompt 06A. Records the verified P&W mechanics (cosmetic government, cosmetic social/economic policy, revenue-neutral tax, six discount policies with a 60-turn cooldown and additive stacking, inert unbounded approval, capacity-based population, no elections), the snippet-level forum proposals, the comparison table and the six design lessons. The forum and the live wiki were unreachable; both limitations are recorded rather than worked around with invented quotations.

---

# Part II — Prompt 06B re-verification: elections, leadership and crises

## 9. What was re-checked on 2026-10-25

Prompt 06A read the community wiki through search snippets because the wiki returned **403**. On 2026-10-25 the same pages returned **200** and were read directly. The claims below are therefore **re-verified**, not repeated from 06A, and each carries the page that was actually read.

| Page | Status on 2026-10-25 | Claim re-checked | Result |
|---|---|---|---|
| [politicsandwar.com](https://politicsandwar.com/) | 200, live | The game is a persistent browser strategy game with a shared world and a turn countdown | **Confirmed.** The page exposes "Next turn in 1:13"; it does not state the interval |
| [Government Type](https://politicsandwar.fandom.com/wiki/Government_Type) | 200 | Government type is cosmetic and freely changeable | **Confirmed verbatim:** "This option does not provide any nation bonuses and exists merely for role-playing reasons"; 32 standard types plus one Easter Egg; "You can change your Government Type whenever you want at the 'Edit' page" |
| [Approval Rating](https://politicsandwar.fandom.com/wiki/Approval_Rating) | 200 | Approval is unbounded behind a 0–100 display and has no mechanical effect | **Confirmed verbatim:** "The Approval Rating does not affect your nation in any way. It is merely used for roleplay purposes." The page lists action factors (war, espionage, cities, projects) and turn factors (population density, pollution, unpaid expenses, no food) and two achievements |
| [Policies](https://politicsandwar.fandom.com/wiki/Policies) | 200 | Social and economic policy questionnaires are cosmetic | **Confirmed verbatim:** "Neither kind of policies has any impact on your nation mechanically, so there is no 'best' setting" |
| [Domestic Policy](https://politicsandwar.fandom.com/wiki/Domestic_Policy) | 200 | Six emphases, one mechanical choice, 60-turn cooldown | **Confirmed:** six policies (5% cost reductions or +1% gross income), changed on the Edit page, "once every 60 turns (5 days)", amplified by the Government Support Agency project |
| [Edit Nation](https://politicsandwar.fandom.com/wiki/Edit_Nation) | 200 | Leader and government are editable labels | **Confirmed:** the page lists **Leader Name**, **Government Type** and **Domestic Policy** among freely editable fields |

### 9.1 What is *not* there

There is **no election, campaign, term, vote, confidence, succession or coup mechanic** in the pages read, and no wiki page for any of them was found. The leader is a **name field** on the Edit Nation page; the government is a **label** chosen from a list. The absence is evidence of absence only for the documented interface: a mechanic could exist undocumented, but nothing on the live nation-edit or wiki pages suggests one, and the Approval Rating page explicitly says approval has no effect.

This is the single most important finding for Prompt 06B: **the reference game has no interactive domestic politics at all.** It is not a model to copy with gentler numbers; it is a model to replace.

## 10. Forum and community evidence

The forum remained **inaccessible** on 2026-10-25. Four attempts (the Internal Politics thread, *Make Approval Rating Mean Something*, *Government Type Bonuses*, and the forum index) each **timed out after 20 seconds**. The only community evidence available is what a search engine has indexed:

| Thread | Evidence | Grade |
|---|---|---|
| [Government Type Bonuses](https://forum.politicsandwar.com/index.php?/topic/21742-government-type-bonuses/) | Title, forum section (Game Suggestions), author and date visible in the snippet: "By Matthew Mann November 22, 2017". No body text | **V3** (snippet), **C** (proposal) |
| [Make Approval Rating Mean Something](https://forum.politicsandwar.com/index.php?/topic/23354-make-approval-rating-mean-something/) | Title and "Game Suggestions" section; no date or body | **V3/C** |
| [Proposal: Policy & Approval Rating rework](https://forum.politicsandwar.com/index.php?/topic/53421-proposal-policy-approval-rating-rework/) | Title and section; no date or body | **V3/C** |
| Internal Politics; How Does Approval Ratings Work?; Please Add More Decisions; Effect of Leader's Rating | Title only; pages timed out | **C** |

**Do not read these as a mandate.** A thread title proves that at least one player wanted a mechanic to matter; it does not prove support, consensus, implementation, or a date for any argument. No quotation, vote count, player count or developer response is recorded here because none was read. The forum's inaccessibility is a **limitation of this report**, not a finding about the community.

## 11. Why the reference model fails for Nation Supremacy

Three verified facts combine badly:

1. **Government is free and reversible.** A player changes it on the Edit page at no cost. It cannot carry an identity, so it cannot carry a strategy.
2. **Approval is inert.** The game tracks it, displays it and awards achievements for it, but nothing reads it. A player who ignores it loses nothing.
3. **The only mechanical domestic choice is a discount.** Domestic Policy changes one cost by 5% (or income by 1%) every 60 turns. It is a build-order modifier, not a political decision.

The result is a game where the word "politics" describes a **role-play layer** while the actual decisions are economic and military. That is a legitimate design for a war game, but it is the opposite of Nation Supremacy's goal: the government choice is permanent, approval is stored, stability taxes the economy, and legitimacy is derived from the groups that can remove the ruler. Prompt 06B must make those four facts **matter interactively** without importing the reference's two failure modes — cosmetic choice and unbounded punishment.

## 12. Evaluation of the Prompt 06B proposals against the evidence

| Proposal | Evidence | Disposition | Reason |
|---|---|---|---|
| **A — Election every 240 turns (20 days)** | No reference equivalent; the interval is a design choice. A 20-day term is long enough for policy to change the economy and short enough to be remembered | **Adopted**, with a **staggered per-nation anchor** and a 24-turn campaign | A global election day would concentrate load and make every democracy campaign at once; a per-nation anchor spreads both. 240 turns is exactly 20 days at two-hour turns |
| **B — Candidacy and campaigning** | The reference has no campaign; its leader is a text field | **Adopted with modifications**: the incumbent is automatically nominated; two **simulated** challengers stand; three campaign actions | Candidacy by other players would need one account per nation (D-032) and would let a second account capture a nation. Simulated challengers give a contest without breaking the account model |
| **C — 24-turn loss-of-office penalty (48 h)** | No evidence supports the number; it is longer than many players' weekly play time | **Rejected**; replaced by a **12-turn TRANSITION** (24 h) with restricted executive authority | Two full days of lockout punishes absence, not decisions. Twelve turns still costs a real day of construction, research and policy, and the account keeps its nation |
| **D — Non-electoral retention** | The reference has none; a monarchy, dictatorship or junta has no removal process | **Adopted** as a continuous legitimacy test with a 12-turn pressure window, a published warning band and a deterministic challenge | A calendar alone would let an unpopular monarch rule for 20 days; a continuous test makes institutions react to how the nation is governed |
| **E — 36–48 turns of unrest, 75% production, zero tax** | The reference has no unrest. B-04's cost identity and B-05's per-batch output show the proposal is not survivable | **Rejected**; replaced by an **18-turn CRISIS** with no production or tax multiplier, a stability penalty and an executive-action lockout | At the standard start the proposal is insolvent by turn 13 and starves the population by turn 4 (B-06 §33). A crisis must cost authority, not the nation |
| **F — Permanent government identity** | The reference does the opposite: government is freely changeable | **Already adopted** (DMP-076/D-084); 06B preserves it | Leadership changes, never the government. This is the structural difference from the reference |
| **G — More interactive politics** | The reference offers role-play, not interaction | **Adopted** as the design goal, delivered through campaigns, retention pressure, warnings, crises and recovery | Interaction must be legible and bounded: the player should always know why a political outcome happened |

### 12.1 The lesson Prompt 14 must not lose

The reference proves that a political stat with no reader becomes decoration. Nation Supremacy already routes approval → supports → stability → tax. Prompt 06B adds a second reader — **removal** — but must not add a third currency, a second support meter or a hidden random roll. Every political outcome in 06B is computed from values the player can already see.


## 13. Evidence limits

- The forum was unreachable; community claims are **snippet-level** and are not used to justify any adopted number.
- The wiki is community-maintained and may lag the live game; the live homepage and the wiki agree on the cosmetic government and inert approval, which is the load-bearing evidence.
- No developer statement, patch note or changelog was read for this section.
- The election, campaign, retention and crisis numbers are **Nation Supremacy design choices**, not reference mechanics. They are calibrated against B-04 and B-05 and remain **provisional** (D-091, DMP-000e).

## 14. Sources added for Prompt 06B

| Source | URL | Accessed | Grade |
|---|---|---|---|
| Live homepage | https://politicsandwar.com/ | 2026-10-25 | V1 |
| Government Type | https://politicsandwar.fandom.com/wiki/Government_Type | 2026-10-25 | V1 |
| Approval Rating | https://politicsandwar.fandom.com/wiki/Approval_Rating | 2026-10-25 | V1 |
| Policies | https://politicsandwar.fandom.com/wiki/Policies | 2026-10-25 | V1 |
| Domestic Policy | https://politicsandwar.fandom.com/wiki/Domestic_Policy | 2026-10-25 | V1 |
| Edit Nation | https://politicsandwar.fandom.com/wiki/Edit_Nation | 2026-10-25 | V1 |
| Government Type Bonuses (forum) | https://forum.politicsandwar.com/index.php?/topic/21742-government-type-bonuses/ | 2026-10-25 | V3/C (snippet; 2017-11-22) |
| Make Approval Rating Mean Something (forum) | https://forum.politicsandwar.com/index.php?/topic/23354-make-approval-rating-mean-something/ | 2026-10-25 | V3/C (title) |
| Policy & Approval Rating rework (forum) | https://forum.politicsandwar.com/index.php?/topic/53421-proposal-policy-approval-rating-rework/ | 2026-10-25 | V3/C (title) |

## 15. Revision history (06B)

**v2.0 (2026-10-25).** Prompt 06B re-verification: the wiki pages that returned 403 during 06A were read directly and the cosmetic-government, inert-approval, questionnaire-policy and editable-leader claims were confirmed verbatim; the leader/government edit fields were verified on the Edit Nation page; the absence of any election, campaign, term, confidence or succession mechanic was recorded as absence-of-interface evidence; four forum threads timed out and only snippet-level titles remain, which are not used as consensus. Adds the evaluation of the seven Prompt 06B proposals and the evidence limits. Prompt 06A's §1–§8 are unchanged.
