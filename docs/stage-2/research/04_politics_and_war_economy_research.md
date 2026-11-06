# Politics & War economy — reference research

**Version:** 1.0 · **Created:** 2026-10-24 · **Stage 2, Prompt 04**
**Status:** Research record. It informs [B-04](../10_economy_resources_treasury_and_finances.md); it is **not** a rulebook and approves nothing.
**Evidence date:** all pages were read on **2026-10-24** (UTC). Politics & War is a live commercial game; any figure below can change without notice.

---

## 1. Purpose, method and evidence grading

This report studies the economic design of **Politics & War (P&W)** because it is the closest operating reference for a persistent, turn-based nation-strategy game with a fixed resource roster. The purpose is to learn **what the mechanics do to player decisions**, not to copy numbers.

Every important statement is labelled:

| Label | Meaning |
|---|---|
| **Verified** | An official or community source states the mechanic or figure directly, and the statement is quoted or closely paraphrased with its URL |
| **Partly verified** | A source states part of the mechanic; another part is inferred from related pages or the structure of the game |
| **Interpretation** | The analyst's judgement about what the mechanic achieves or why it exists |
| **Uncertain** | Sources disagree, are stale, or the mechanic was not directly observed |

**Method.** I read the P&W wiki pages for Resources, Improvements/Resources, Improvements/Manufacturing, Improvements/Power, Improvements/Commerce, Nation Formulas, City Formulas, National Tax Rate and City. I attempted the official `politicsandwar.com` pages and the community wiki through their public APIs. No account was created, no game action was taken, and no logged-in state was observed. The research is therefore **documentary only**: it establishes stated mechanics, not current runtime behaviour.

**What this report does not claim.** It does not claim that any formula is current, complete, or optimally balanced. It does not claim that the wiki is official. It does not reproduce P&W text at length, and it does not copy a formula into Nation Supremacy without an independent design argument.

---

## 2. Source inventory

| ID | Source | Type | Accessed | Reliability | Used for |
|---|---|---|---|---|---|
| S1 | `https://politicsandwar.fandom.com/wiki/Resources` (read via `api.php?action=parse&page=Resources&prop=wikitext`) | Community wiki | 2026-10-24 | Medium; long-lived community reference, not official | Resource roster, natural/manufactured split, continent availability, stockpile cap |
| S2 | `https://politicsandwar.fandom.com/wiki/Improvements/Resources` (API as above) | Community wiki | 2026-10-24 | Medium | Extraction improvements, yields, construction and operating costs, limits, pollution, food formula |
| S3 | `https://politicsandwar.fandom.com/wiki/Improvements/Manufacturing` (API) | Community wiki | 2026-10-24 | Medium | Conversion recipes, power requirement, manufacturing bonus |
| S4 | `https://politicsandwar.fandom.com/wiki/Improvements/Power` (API) | Community wiki | 2026-10-24 | Medium | Power plant capacity, fuel, upkeep, pollution, slot pressure |
| S5 | `https://politicsandwar.fandom.com/wiki/Improvements/Commerce` (API) | Community wiki | 2026-10-24 | Medium | Commerce buildings, income multiplier, steel/aluminium construction inputs |
| S6 | `https://politicsandwar.fandom.com/wiki/Nation_Formulas` (API) | Community wiki | 2026-10-24 | Medium; the page itself contains a work-in-progress section | Income formula, food-shortage multiplier, score formula |
| S7 | `https://politicsandwar.fandom.com/wiki/City_Formulas` (API) | Community wiki | 2026-10-24 | Medium | City, infrastructure and land cost curves |
| S8 | `https://politicsandwar.fandom.com/wiki/National_Tax_Rate` (API) | Community wiki | 2026-10-24 | Medium | Tax-rate range and the revenue-neutrality observation |
| S9 | `https://politicsandwar.fandom.com/wiki/City` (API) | Community wiki | 2026-10-24 | Medium | City components, improvement groups, power requirement, population factors, city cooldown |
| S10 | `https://politicsandwar.com/pwpedia/article/tax-brackets` | Official in-game encyclopedia | 2026-10-24 | High for the existence of alliance tax brackets; not used for economy formulae | Alliance taxation context |
| S11 | `https://politicsandwar.com/` | Official site | Attempted 2026-10-24 | High for branding, low for mechanics without login | Confirms the game is live and browser-based |

**Not obtained.** The official market fee schedule, the current combat consumption rates, the full upkeep formula, the current improvement catalogue, and any 2026 patch notes. The wiki's market pages were not read in this pass. Claims about market fees are therefore marked **uncertain** and are not used as a design premise.

---

## 3. Verified reference mechanics

### 3.1 The resource roster is the same 11-resource shape

**Verified (S1).** P&W divides resources into **natural** and **manufactured**. The natural resources are Coal, Oil, Iron, Bauxite, Lead, Uranium and Food. The manufactured resources are Gasoline, Steel, Aluminum and Munitions (P&W's name for ammunition). The page states that natural resources are extracted through their respective mine improvement, that availability differs by continent, and that manufactured resources consume natural resources and can be built on any continent.

**Interpretation.** The 11-resource roster is not an arbitrary list: it is a **two-tier industrial chain** with one food staple, three energy/industrial inputs (coal, oil, uranium), three metallic inputs (iron, bauxite, lead) and four outputs. The shape is legible because every manufactured good has one obvious raw parent, and every raw good except food has an obvious industrial child. This is exactly the structure Nation Supremacy's mandatory roster adopts.

**Nation Supremacy recommendation.** **Adopt the shape, not the names of the P&W improvements.** Keep the seven raw / four manufactured classification, the one clear parent for each manufactured good, and food as the population staple. Do **not** adopt P&W's "Munitions" label; the project's mandatory name is **Ammunition**.

### 3.2 Natural resources are gated by continent

**Verified (S1).** The wiki publishes a continent-availability matrix. Every continent has a combination of Coal or Oil, Iron or Bauxite, and Lead or Uranium; Food is available everywhere (Antarctica at −50%). A nation therefore cannot extract every raw resource at home.

**Interpretation.** This is P&W's primary engine for trade and diplomacy. Scarcity is **exogenous and legible**: a player knows from the first session which raw goods they must import. It also creates a permanent strategic identity (an "oil continent" versus a "steel continent") without requiring a map.

**Nation Supremacy recommendation.** **Reject geographic gating** because the project has **no geographic map** (REQ-041). Replace it with the Stage 1 **structural asymmetry** engine: every nation can build every extraction capacity, but **capacity is expensive, land-free and limited by slots/energy**, so specialization is a choice rather than an accident of birth. The design must preserve P&W's legibility benefit (a player can tell what they are short of) without a continent. B-04 does this through **capacity investment and operating-cost asymmetry**, not through a hidden resource roll.

### 3.3 Extraction improvements: fixed yields, money costs, pollution and slot limits

**Verified (S2).** The resource improvements produce:

| Improvement | Output | Construction | Operating cost | Limit | Notes |
|---|---|---|---|---|---|
| Coal Mine | 3 tons/day (0.25/turn) | $1,000 | $400/day ($34/turn) | 10 per city | +12 pollution |
| Oil Well | 3 tons/day | $1,500 | $600/day ($50/turn) | 10 per city | +12 pollution |
| Bauxite Mine | 3 tons/day | $9,500 | $1,600/day ($134/turn) | 10 per city | +12 pollution |
| Iron Mine | 3 tons/day | $9,500 | $1,600/day ($134/turn) | 10 per city | +12 pollution |
| Lead Mine | 3 tons/day | $7,500 | $1,500/day ($125/turn) | 10 per city | +12 pollution |
| Uranium Mine | 3 tons/day | $25,000 | $5,000/day ($417/turn) | 5 per city | +20 pollution |
| Farm | `Land × 3 / 125` tons/day, or `Land / 500` tons/turn | $1,000 | $300/day ($25/turn) | 20 per city | +2 pollution; Antarctica −50% |

**Interpretation.** Three design choices stand out:

1. **A mine is a fixed-yield unit with a money operating cost.** The player's decision is "how many mines", not "how much to extract". This is easy to understand and easy to compute at a boundary.
2. **Uranium is deliberately expensive** — 25× the construction cost of a coal mine and 12× the operating cost — while producing the same physical tonnage. The scarcity is **economic**, not physical. That is a useful pattern: a resource can be rare because it is expensive to extract, not because it is absent.
3. **Pollution is a real cost** attached to extraction/manufacturing. It couples the economy to a second system (environment/population) without a separate pollution market.

**Nation Supremacy recommendation.** **Adopt the "capacity unit with a money operating cost" pattern** but change two things: (a) operating cost is charged **per batch actually run**, not per facility per turn, so an idle facility does not punish an absent player; (b) a small **capacity maintenance** charge remains, so holding idle capacity is not free. **Reject pollution** at this stage: it requires an environment system that Prompt 06 has not designed, and it would add a second resource-like meter. The project's equivalent pressure is **power and money**, which are already in B-04.

### 3.4 Manufacturing recipes are simple, multiplicative and bonus-scaled

**Verified (S3).** P&W's manufacturing improvements convert:

| Improvement | Conversion per day | Construction | Upkeep | Limit |
|---|---|---|---|---|
| Oil Refinery | 3 Oil → 6 Gasoline | $45,000 | $4,000/day ($334/turn) | 5 per city |
| Steel Mill | 3 Coal + 3 Iron → 9 Steel | $45,000 | $4,000/day | 5 per city |
| Aluminum Refinery | 3 Bauxite → 9 Aluminum | $30,000 | $2,500/day ($209/turn) | 5 per city |
| Munitions Factory | 6 Lead → 18 Munitions | $35,000 | $3,500/day ($292/turn) | 5 per city |

All manufacturing requires **power**. There is a **12.5% production bonus for the 2nd–5th matching improvement, up to 50%**, and the corresponding raw-resource usage is increased to create the extra output.

**Interpretation.** P&W's recipes are deliberately **generous and legible**: oil doubles into gasoline; iron+coal triples into steel; bauxite triples into aluminium; lead triples into munitions. The player does not need a spreadsheet to see that manufacturing is worth more than selling raw ore. The 50% concentration bonus rewards **specialization within a city** and makes "build five of the same thing" a meaningful plan, while the increased input usage prevents the bonus from being a pure free lunch.

**Nation Supremacy recommendation.** **Adopt simple integer recipes with a clear value-added margin**, but **do not copy the exact ratios**. B-04 uses:

- Refining: **10 Oil → 8 Gasoline** (0.8 output per input; oil is valuable and gasoline is a fuel, so the margin is in price, not volume).
- Steel: **10 Iron + 6 Coal → 8 Steel** (two inputs, one output; coal is the reducing agent).
- Aluminium: **12 Bauxite → 8 Aluminium** (the most energy-intensive chain).
- Ammunition: **8 Lead + 4 Coal → 10 Ammunition** (lead is the payload; coal is process heat).

The deliberate difference is that **our recipes lose mass**, while P&W's gain mass. A mass-gaining recipe is easy to explain ("refining adds value") but it makes physical conservation meaningless and can create resource out of nowhere. A mass-losing recipe is more honest and makes the **value-added** the point: the output is worth more per unit because it is usable, not because there is more of it. The numbers are set so each chain earns a positive margin at the reference prices, but a poor market price can turn it into a loss.

**Reject the 50% concentration bonus for Prompt 04.** It belongs to Prompt 05's building/slot design, where "five of the same building" can be represented. B-04 instead uses **capacity** as a single number per chain, and Prompt 05 may add a specialization bonus later. The formula register reserves the interface so a later bonus cannot silently break the recipes.

### 3.5 Power is a prerequisite with fuel-specific trade-offs

**Verified (S4).** P&W's power improvements:

| Plant | Powers | Construction | Upkeep | Pollution |
|---|---|---|---|---|
| Coal Power | 500 infrastructure | $5,000 | $1,200/day + 1.2 coal/day | +8 |
| Oil Power | 500 infrastructure | $7,000 | $1,800/day + 1.2 oil/day | +6 |
| Nuclear Power | 2,000 infrastructure | $500,000 + 100 steel | $10,500/day + 2.40 uranium/day | 0 |
| Wind Power | 250 infrastructure | $30,000 + 30 aluminium | $500/day | 0 |

The wiki states that 4 of the 6 improvement groups require power, and that a city counts as powered only when it has power for **all** of its infrastructure.

**Interpretation.** Power is the **capacity multiplier** that forces a nation to choose between cheap dirty fuel, expensive clean fuel, and slot-efficient nuclear. It also creates a **second use for coal, oil and uranium**, which is exactly what prevents those raw goods from being purely export commodities. The "all infrastructure must be powered" rule is a harsh binary: a city is either fully powered or not, which can create cliff effects.

**Nation Supremacy recommendation.** **Adopt the concept, soften the binary.** B-04 uses **grid units (GU)**, with three generator types:

- **Coal Generator** — cheap, fuel-heavy, low capital.
- **Oil Generator** — mid-cost, uses oil that could otherwise become gasoline.
- **Nuclear Generator** — high capital, high output, consumes uranium and a small lead shielding input.

Instead of "a city is powered or not", B-04 applies a **published pro-rata derating**: if supply is below demand, every processing chain runs `floor(capacity × supply / demand)` batches. This is deterministic, avoids a binary cliff, and makes the shortfall visible in the digest. It also gives **uranium a clear, non-military purpose** and **lead a second use** (shielding), which the mandatory roster requires.

### 3.6 Income is population × tax, with food and policy multipliers

**Verified (S6, S8).** The wiki gives:

```
Minimum Wage   = 725 / (Tax Rate × 1000)
Average Income = ((Commerce / 50) × Minimum Wage) + Minimum Wage
Gross Income   = Weighted Average Income × Population × Tax Rate
```

and notes that the tax-rate terms cancel, so the tax rate does not change revenue. Gross income is further multiplied by **1.01** under Open Markets, by **0.67** if the nation is out of food, and by colour/trade-block and treasure bonuses. The National Tax Rate page confirms a **5%–50%** range and repeats that the rate has no effect on revenue.

**Interpretation.** This is the most important **negative** finding in the research. P&W presents a tax-rate slider that looks like a strategic decision but is **revenue-neutral by construction**. The player's real income levers are population, commerce and modifiers, not tax policy. The food multiplier (×0.67) is a blunt but effective starvation penalty: a starving nation loses a third of its gross income immediately.

**Nation Supremacy recommendation.** **Reject the revenue-neutral tax rate.** A tax rate that does nothing is a false choice, and the project's design pillar DP-004 (self-explaining world) forbids it. B-04 makes the tax rate a **real but bounded** revenue lever, with the stability/population consequences owned by Prompt 06. The formula is:

```
tax_income = floor(population × tax_rate_bp × stability_factor_bp / 1,000,000,000)
```

At the standard start (50,000 people, 300 bp, 100% stability) this is 150 crowns. A higher rate raises revenue but lowers stability (Prompt 06), which lowers the stability factor and can offset the gain. This preserves P&W's legibility while making the choice real.

**Adopt a graduated hunger penalty, not a flat ×0.67.** B-04's penalty is 0–30% of the **next turn's** tax income, proportional to the unmet food share. It is smaller than P&W's one-third cut at full starvation, but it is gradual, forecastable and recoverable. Population decline and stability loss remain Prompt 06's.

---

### 3.7 Commerce converts a second system into income

**Verified (S5).** Commerce improvements raise a city's **Commerce percentage**, which raises citizens' average income and therefore tax revenue. The published buildings are Supermarkets (+3%, $5,000, 6 per city), Banks (+5%, $15,000 + 5 steel + 10 aluminium, 5 per city), Shopping Malls (+9%, $45,000 + 20 steel + 25 aluminium, 4 per city) and Stadiums (+12%, $100,000 + 40 steel + 50 aluminium, 3 per city). All commerce buildings require power.

**Interpretation.** Commerce is P&W's **second income lever**, separate from population. It also creates a permanent demand for **steel and aluminium** in peacetime, which is important: without commerce, those two manufactured goods would be almost purely military. The escalating steel/aluminium requirements make late-game commerce a visible industrial commitment.

**Nation Supremacy recommendation.** **Adopt the idea that manufactured goods are construction inputs**, and let Prompt 05 own the commerce buildings. B-04 establishes the contract: **steel and aluminium are required by construction and upgrade actions**, and **gasoline is a site fuel for construction**, so all three have peacetime demand even before warfare. Prompt 05 sets the exact quantities. B-04 does **not** add a separate commerce percentage; income stays a population × tax formula until Prompt 06/07 can justify a second multiplier.

### 3.8 Food shortage is a blunt multiplier

**Verified (S6).** If a nation is out of food, gross income is multiplied by **0.67**.

**Interpretation.** P&W treats food as a binary: fed or starving. There is no partial hunger, no forecast, and no gradual recovery. The penalty is large enough to matter and simple enough to explain, but it is also a cliff: one missing unit triggers the full one-third loss.

**Nation Supremacy recommendation.** **Adapt, do not copy.** B-04 uses a **graduated** penalty based on the unmet share of demand, applies it to the **next** turn's tax income (so the player can see it coming and recover), and caps it at 30%. Population and stability consequences remain Prompt 06's. The contract is explicit: B-04 owns food accounting, consumption and the economic penalty; Prompt 06 owns population growth, stability and any demographic loss.

### 3.9 Stockpiles are capped per resource and excess is lost

**Verified (S1).** The current stockpile limit is **9,999,999.99 per resource**, and anything over that is lost.

**Interpretation.** The cap is so high that it is effectively a database guard, not a game mechanic. It prevents unbounded storage but does not create a storage decision. Excess is destroyed silently, which is exactly the kind of unexplained loss the project's design principles forbid.

**Nation Supremacy recommendation.** **Reject per-resource caps and silent loss.** B-04 uses a **shared warehouse capacity** measured in units. Production that would exceed capacity **does not run** (inputs, money and fuel are not consumed), and the digest states that the batch was blocked. This is predictable, visible and does not destroy value. The shared pool makes storage a real decision (which goods to hold) without eleven separate caps.

### 3.10 City and infrastructure costs rise steeply

**Verified (S7, S9).** New city cost follows `50000×(X−1)^3 + 150000×X + 75000`; infrastructure cost per unit follows `((Current Infra − 10)^2.2 / 710) + 300`; land cost follows `0.002×(Current Land − 20)^2 + 50`. Cities start with 10 infrastructure and 250 land. A nation cannot create or delete a city within the last 120 turns (10 days), except nations with fewer than 20 cities.

**Interpretation.** The cubic city cost and exponential infrastructure cost are P&W's **anti-snowball** mechanism: growth becomes progressively more expensive, so a mature nation cannot simply buy its way to dominance. The 120-turn city cooldown is a second brake, and it is a **presence-adjacent** mechanic: it forces planning around a multi-day timer.

**Nation Supremacy recommendation.** **Adapt the anti-snowball intent, reject the cooldown.** B-04 does not design city costs (Prompt 05 owns construction), but it requires that **capacity expansion has a rising marginal cost** and that **no economic action imposes a multi-day real-time cooldown**. Rising costs are a legitimate brake; a 10-day timer is not compatible with the project's absence-tolerant, 2-hour-turn design.

### 3.11 Market and alliance taxation

**Partly verified (S10, forum search).** P&W has a player-driven global market and alliance tax brackets with monetary and resource percentages. The exact global-market fee schedule was **not** established in this pass. Forum discussion about taxing the market is not evidence of a current mechanic.

**Interpretation.** The market is the main **transfer** channel: it moves money and goods between players without creating either. Alliance taxation is a **governance** mechanism, not an economic one, and belongs to Prompt 09.

**Nation Supremacy recommendation.** **Defer the market design to Prompt 07.** B-04 defines only the accounting contract: a purchase or sale transfers crowns and inventory atomically, never creates value, writes matched ledger events, and applies any fee as an explicit, disclosed sink. D-016 (offers do not reserve) and D-017 (terms are parties-only) remain binding. No market fee is adopted in B-04.

### 3.12 War consumption is the demand side of the military economy

**Partly verified (S1, S3).** Gasoline fuels tanks, aircraft and ships; munitions arm soldiers, tanks, aircraft and ships; steel and aluminium are used to construct improvements and military units. The exact per-unit combat consumption is **not** established here and belongs to Prompt 10.

**Interpretation.** P&W's military is a **resource sink** with three different demand curves: fuel (continuous), ammunition (per combat), and steel/aluminium (capital). This is what makes the economy strategic in wartime: a nation can have money and still lose because it lacks fuel or munitions.

**Nation Supremacy recommendation.** **Adopt the demand structure, defer the numbers.** B-04 defines **what each resource is for** and the **reservation/ledger contract** for military consumption; Prompt 10 defines quantities, order costs and readiness. D-015 (Operations Points) remains the military action model; B-04 does not touch its values.

---

## 4. Comparison matrix

The required columns are: **Reference mechanic**, **Evidence/source**, **Gameplay purpose**, **Nation Supremacy decision**, **Rationale**. The decision vocabulary is **Adopt**, **Adapt** or **Reject**.

| Reference mechanic | Evidence/source | Gameplay purpose | Nation Supremacy decision | Rationale |
|---|---|---|---|---|
| Seven raw + four manufactured resources | S1 | A two-tier industrial chain that is legible without a tutorial | **Adopt the shape** | The project's mandatory roster has the same shape; keeping it preserves legibility and gives every manufactured good an obvious parent |
| Continent-gated raw resources | S1 | Exogenous scarcity drives trade and diplomatic identity | **Reject** | The world is mapless (REQ-041); a continent roll would reintroduce geography and could make a nation permanently unviable |
| Fixed-yield extraction improvements with money operating costs | S2 | Simple per-turn arithmetic; the player chooses how many units, not how much to extract | **Adapt** | Keep the capacity-unit idea; charge operating cost per batch run and add a small capacity maintenance so idle capacity is not free |
| Pollution as a cost of extraction/manufacturing | S2, S3, S4 | Couples economy to environment/population | **Reject for Prompt 04** | It needs an environment system Prompt 06 has not designed; power and money already provide the pressure |
| Simple multiplicative conversion recipes | S3 | Manufacturing is obviously more valuable than raw sales; easy to compute | **Adapt** | Keep simple integer recipes, but make them mass-losing and value-adding rather than mass-gaining; set margins so a bad price turns a chain into a loss |
| 12.5%–50% concentration bonus for matching improvements | S3 | Rewards within-city specialization | **Defer to Prompt 05** | The bonus depends on building counts and slots, which Prompt 05 owns; B-04 reserves the interface so it cannot silently break a recipe |
| Manufacturing requires power | S3, S4 | Forces an energy decision and gives coal/oil/uranium a second use | **Adopt** | It is the cleanest way to make uranium meaningful and to keep coal and oil strategic |
| Power plants with different fuel/capital/pollution trade-offs | S4 | A genuine long-term infrastructure choice | **Adapt** | Keep coal/oil/nuclear fuel trade-offs; drop pollution and the binary "all infrastructure powered" rule; use published pro-rata derating |
| Binary "out of food" ×0.67 gross income | S6 | A severe, simple starvation penalty | **Adapt** | Use a graduated 0–30% penalty on next turn's tax income; it is forecastable and recoverable, and population effects stay in Prompt 06 |
| Revenue-neutral tax rate (5%–50%) | S6, S8 | Presents a policy choice | **Reject** | A slider that cannot change revenue is a false choice; B-04 makes tax a real but bounded lever with a stability trade-off |
| Commerce percentage as a second income multiplier | S5 | A peacetime demand for steel/aluminium and a growth lever | **Adapt** | Adopt the demand for manufactured construction inputs; do not add a second income multiplier until Prompt 06/07 can justify it |
| Per-resource stockpile cap with excess lost | S1 | A database guard against unbounded storage | **Reject** | Silent loss is prohibited; use a shared warehouse capacity and block the batch instead |
| Cubic city cost and exponential infrastructure cost | S7, S9 | Anti-snowball growth brake | **Adapt the intent** | Rising marginal cost is legitimate; Prompt 05 owns the curves, and B-04 forbids multi-day real-time cooldowns |
| 120-turn city cooldown | S9 | Slows growth and forces planning | **Reject** | Incompatible with absence-tolerant 2-hour turns; no economic action may impose a multi-day real-time timer |
| Player-driven market with alliance taxation | S10; uncertain fee evidence | Transfers value between players; governance funding | **Defer to Prompt 07/09** | B-04 defines only the accounting contract; D-016/D-017 already bind the trade design |
| Military consumes gasoline, ammunition, steel and aluminium | S1, S3 | Makes war an economic test, not only a combat test | **Adopt the demand structure; defer numbers** | Prompt 10 owns quantities and order costs; B-04 owns reservation and ledger behaviour |
| Nation score includes cities, infrastructure, projects and military | S6 | A single visible progress number | **Defer to Prompt 11** | Rankings and score are Prompt 11's; B-04 defines national wealth separately and does not conflate it with score |

---

## 5. What P&W's economy does well, and what it does badly

### 5.1 Strengths worth learning from

| Strength | Evidence | Why it works | Nation Supremacy use |
|---|---|---|---|
| **Legible chain** | S1, S3 | Every manufactured good has one obvious raw parent; a new player can understand the economy in one screen | Keep the 11-resource chain and the four simple recipes |
| **Two-tier value** | S3 | Manufacturing is visibly more valuable than raw sales, so the player wants to climb the chain | Give every manufactured good a positive reference margin and a real sink |
| **Scarcity creates other players** | S1 | Continent gating means no nation is self-sufficient, so trade is structurally necessary | Replace geography with capital cost, power and capacity limits, but keep the necessity |
| **Power as a multiplier** | S4 | The energy choice is a compact, understandable infrastructure decision | Adopt a three-generator system with clear fuel trade-offs |
| **Simple per-turn computation** | S2–S4 | The boundary can be computed deterministically without a simulation engine | Use integer batches, fixed recipes and a published order |
| **Visible operating costs** | S2–S4 | A player can see that a building costs money every turn, not only when built | Show per-batch cost and capacity maintenance separately from construction |

### 5.2 Weaknesses to avoid

| Weakness | Evidence | Consequence in P&W | Nation Supremacy avoidance |
|---|---|---|---|
| **Revenue-neutral tax slider** | S6, S8 | A choice that does nothing; players learn the UI lies | Make tax real and bounded, with a disclosed stability trade-off |
| **Binary starvation cliff** | S6 | One missing food unit causes a one-third income loss; recovery is opaque | Graduated, forecast next-turn penalty with a clear recovery path |
| **Silent overflow loss** | S1 | Excess resources vanish at the cap | Block the batch and report it; never destroy value silently |
| **Pollution as a hidden second meter** | S2–S4 | Adds a cost the economy screen must explain separately | Defer until an environment system exists; use money and power instead |
| **Multi-day real-time cooldowns** | S9 | Punishes players who cannot log in at the right time | No multi-day cooldown on any economic action |
| **Opaque bonus stacking** | S3, S5, S6 | Many multiplicative bonuses make the final number hard to explain | One reference-price margin, one derivative rule, one published bonus hook for Prompt 05 |
| **No separation of stock and flow** | S1–S6 | Players confuse cash, inventory and score | B-04 separates treasury, available balance, reserved balance, inventory, book value and national wealth |

### 5.3 The single most important lesson

**P&W's economy is legible because it is a chain, not a spreadsheet.** A player can say "I have oil, so I can refine gasoline; I need iron and coal for steel; I need power for all of it." That sentence is the whole economy. Nation Supremacy should be able to say the same sentence with its own 11 resources, its own three-chain power system, and its own two-hour boundary.

The second lesson is negative: **a displayed choice must change an outcome.** P&W's tax slider is the cautionary example. B-04 therefore states, for every economic lever, what it changes, when it changes it, and what it cannot change.

---

## 6. Design implications carried into B-04

| # | Implication | B-04 response |
|---|---|---|
| 1 | Keep the 11-resource, two-tier chain | Resource roster is fixed; each resource has a full lifecycle profile |
| 2 | Replace geography with investable capacity | Capacity is a per-chain integer; every nation can build any chain at a rising cost |
| 3 | Make power a real but non-binary constraint | Three generators, grid units, published pro-rata derating |
| 4 | Give uranium a meaningful non-military use | Nuclear generation; lead has a second use as shielding |
| 5 | Avoid silent overflow loss | Shared warehouse capacity; blocked batches; no destruction |
| 6 | Avoid a false tax choice | Tax formula with a stability interface; Prompt 06 owns the curve |
| 7 | Avoid a starvation cliff | Graduated hunger penalty on next turn's tax, 0–30% |
| 8 | Keep manufacturing arithmetic simple | Fixed integer recipes, integer batches, floor division, no floats |
| 9 | Separate stock, flow and wealth | Treasury, available, reserved, inventory, book value, national wealth are distinct |
| 10 | Keep the boundary deterministic | Published P3 order, idempotency keys, phase checkpoints |
| 11 | Make every change auditable | Append-only ledger, reversal events, reconciliation check |
| 12 | Protect the reroll boundary | No asset transfer; new nation gets the standard bundle only; history retained |
| 13 | Do not import P&W numbers | All recipes and costs are independently set and labelled provisional |
| 14 | Respect the free-tier architecture | One digest row per nation-turn; ledger events are bounded; no per-tick polling |

---

## 7. Evidence limitations and uncertainty

1. **The wiki is community-maintained, not official.** S1–S9 are Fandom pages. They are useful and internally consistent, but they can be stale or wrong. The official site (S11) was reachable but does not expose mechanics without an account.
2. **The per-day/per-turn conversions imply a 12-turn day.** The resource pages state 3 tons/day and 0.25 tons/turn. That is consistent with a two-hour turn, but the wiki does not state the clock explicitly on those pages. I treat the 12-turn cadence as **partly verified**, not as a verified P&W design statement.
3. **No market fee was established.** Forum posts about market taxation are not evidence of a current fee. B-04 therefore adopts no market fee and leaves it to Prompt 07.
4. **No combat consumption rate was established.** The resource pages state that gasoline and munitions are used by military units, but not how much per battle. B-04 defines only the demand structure and the accounting contract; Prompt 10 owns the numbers.
5. **No current patch notes were read.** P&W changes; a 2026 wiki page may describe a 2024 mechanic. The report therefore uses P&W for **patterns**, not for current values.
6. **No player-behaviour data was collected.** Statements about what players "feel" or "choose" are interpretation, not measurement.
7. **The comparison matrix is analyst judgement.** The Adopt/Adapt/Reject calls are design decisions, recorded as D-043…D-065 and the DD rows in the Stage 2 decision register; they are not research findings.

---

## 8. Source access log

| Time (UTC) | Source | Result |
|---|---|---|
| 2026-10-24 | S1 Resources (API) | 200; wikitext read |
| 2026-10-24 | S2 Improvements/Resources (API) | 200; wikitext read |
| 2026-10-24 | S3 Improvements/Manufacturing (API) | 200; wikitext read |
| 2026-10-24 | S4 Improvements/Power (API) | 200; wikitext read |
| 2026-10-24 | S5 Improvements/Commerce (API) | 200; wikitext read |
| 2026-10-24 | S6 Nation Formulas (API) | 200; wikitext read; page contains a work-in-progress section |
| 2026-10-24 | S7 City Formulas (API) | 200; wikitext read; long code blocks truncated by the reader |
| 2026-10-24 | S8 National Tax Rate (API) | 200; wikitext read |
| 2026-10-24 | S9 City (API) | 200; wikitext read; large cost table truncated |
| 2026-10-24 | S10 Tax Brackets (official pwpedia) | Reachable; used only for the existence of alliance tax brackets |
| 2026-10-24 | S11 politicsandwar.com | Reachable; no mechanics without an account |

**Research verdict:** the evidence is sufficient to support **pattern-level** design decisions (chain shape, power, food penalty, storage, tax, anti-snowball) but **not** sufficient to copy a single P&W number. B-04's numbers are independently derived and labelled provisional.

---

## 9. Cross-references

- [B-04 — Economy, resources, treasury and finances](../10_economy_resources_treasury_and_finances.md)
- [Economic formula and balance register](../10_economic_formula_and_balance_register.md)
- [B-02 — Core gameplay loop and turn system](../07_core_gameplay_loop_symbolic_world_and_turn_system.md)
- [B-03 — Account, nation creation and progression](../09_account_onboarding_nation_creation_and_progression.md)
- [Requirements traceability](../03_requirements_traceability.md)
- [Stage 2 decision register](../04_approved_and_provisional_decisions.md)

**Revision history.** v1.0 (2026-10-24): first issue for Prompt 04. No earlier version exists.

<!-- END -->
