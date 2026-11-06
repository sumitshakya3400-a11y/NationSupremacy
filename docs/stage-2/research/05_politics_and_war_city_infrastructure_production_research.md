# Politics & War research — cities, infrastructure, production and national projects

**Version:** 1.0 · **Research date:** 2026-10-25 · **Stage 2, Prompt 05**
**Status:** Research report. It is **evidence for design**, not a rulebook. Nothing here is implemented, and no P&W mechanic is adopted by being described.

**Companions:** [B-05 specification](../11_cities_infrastructure_production_and_research.md) · [Formula register](../11_city_infrastructure_production_and_research_formula_register.md) · [B-04 economy](../10_economy_resources_treasury_and_finances.md) · [P&W economy research](04_politics_and_war_economy_research.md)

---

## 1. Method and evidence grades

The reference game is **Politics & War** (`politicsandwar.com`), a long-running browser nation simulator with a two-hour turn. Its public wiki is community-maintained and mixes current mechanics with obsolete pages; the official site yields almost nothing mechanically without an account. Every claim below therefore carries one of three grades:

| Grade | Meaning |
|---|---|
| **Verified reference mechanic** | The cited page states the mechanic explicitly, in a formula or a table, and the page is not marked obsolete |
| **Interpretation** | A reasoned explanation of why the mechanic exists or what behaviour it rewards; not stated by the source |
| **Nation Supremacy decision** | Our adopt / adapt / reject / defer choice, with the reason |

Pages that could not be read are named in §7 rather than guessed at.

## 2. Sources

| ID | Source | Access | Reliability | What it was used for |
|---|---|---|---|---|
| **S1** | `https://politicsandwar.fandom.com/wiki/City` (read via `api.php?action=parse&page=City&prop=wikitext`) | 2026-10-25 | Medium — long-lived community reference; the city-cost table is large and appears maintained | City components; 50 infrastructure per improvement; improvement groups; power coverage rule; city starting values; the 120-turn city cooldown; the new-city cost table |
| **S2** | `https://politicsandwar.fandom.com/wiki/Infrastructure` | 2026-10-25 | Medium — direct HTML page, with a worked cost table | Infrastructure's population effect (100 people per unit); the exponential unit-cost curve; the 5% project discount |
| **S3** | `https://politicsandwar.fandom.com/wiki/Improvements` | 2026-10-25 | Medium — short index page | Improvement slots (50 infrastructure each); power requirement by category; the 50% sale refund |
| **S4** | `https://politicsandwar.fandom.com/wiki/Improvements/Resources` (API) | 2026-10-25 | Medium; the page mixes old ("per day") and current ("per turn") units | Mine yields, construction and operating costs, pollution, per-city limits, continent availability, farm output |
| **S5** | `https://politicsandwar.fandom.com/wiki/Improvements/Manufacturing` (API) | 2026-10-25 | Medium | The four conversion recipes, power requirement, construction cost, upkeep, pollution, per-city limits, the same-building production bonus |
| **S6** | `https://politicsandwar.fandom.com/wiki/Improvements/Power` (API) | 2026-10-25 | Medium | Plant capacities in infrastructure, fuel burn, costs, pollution, the coal/oil/nuclear/wind trade-off |
| **S7** | `https://politicsandwar.fandom.com/wiki/Improvements/Commerce` (API) | 2026-10-25 | Medium | Commerce buildings' percentage effects, costs, material inputs, upkeep, limits |
| **S8** | `https://politicsandwar.fandom.com/wiki/Commerce` | 2026-10-25 | Medium | What the commerce percentage does; the 100/115/125% caps |
| **S9** | `https://politicsandwar.fandom.com/wiki/City_Formulas` (API) | 2026-10-25 | Medium — contains a section explicitly marked as a scratchpad | City, infrastructure and land cost formulas; base population; crime and disease formulas; farm output formula |
| **S10** | `https://politicsandwar.fandom.com/wiki/National_Project` (API) | 2026-10-25 | Medium — 39 projects, a long cost table; may lag a patch | Project slot rules, cooldown, refund policy, project categories and effects, example costs |
| **S11** | `https://politicsandwar.fandom.com/wiki/City_building_from_0_to_1000` (API) | 2026-10-25 | **Low** — marked "under construction and review"; it is player advice, not rules | How players actually sequence early growth; the practical meaning of slots and power |
| **S12** | `https://politicsandwar.com/` | 2026-10-25 | High for branding and existence, low for mechanics | Confirms the game is live and browser-based; no mechanics visible without an account |

The Prompt 04 research report (S1–S11 there) already established the resource, recipe and income evidence; this report does not repeat it, and it cross-references rather than re-derives those numbers.

## 3. What a city is in the reference game

**Verified (S1).** A city is the unit that holds three things: infrastructure, land and improvements. Cities exist to (a) hold and grow population and (b) harvest or manufacture resources. Every nation starts with one city of 10 infrastructure and 250 land.

**Verified (S1).** A city has six improvement groups: Power, Resources, Manufacturing, Civil, Commerce and Military. The first is a prerequisite for the rest: a city counts as powered only if its power supply covers **all** of its infrastructure.

**Interpretation.** The city is the game's atomic investment container. Almost every decision is "which city, which improvement", which keeps the interface legible at 40 cities but makes national planning a spreadsheet exercise. It also means a new city is a large, discrete jump in capability rather than a gradual expansion.

**Verified (S1).** A new city can be founded only if the player has not created or deleted a city in the last **120 turns (10 days)**, except that the cooldown does not apply below 20 cities. City cost rises steeply and is tabulated from the 2nd city ($225,000) to the 41st.

**Nation Supremacy decision — adapt the container, reject the geography and the cooldown.** Cities remain the investment container because that is the genre's legible unit, but a city in Nation Supremacy is a **named development centre** with no coordinates, land, borders or continental resources. The 10-day city cooldown is rejected: it punishes a player for a decision they already paid for and interacts badly with a two-hour cadence. Our pacing device is the construction slot (one order per city per turn) plus an infrastructure prerequisite for each new city.

## 4. Infrastructure, land and slots

**Verified (S1, S2, S9).** Infrastructure does two jobs: `Base Population = Infrastructure × 100`, and **50 infrastructure buys one improvement slot**. Its unit cost is exponential, `300 + (Infrastructure − 10)^2.2 / 710`, and the cheapest unit is not at zero because of the `−10` term.

**Verified (S1, S9).** Land's two jobs are to reduce disease (population density) and to raise farm output, `Food = Farms × Land / 500`. Land cost is quadratic, `0.002 × (Land − 20)^2 + 50`. Land must be bought in multiples of 500 to be efficient.

**Verified (S11).** Player advice is blunt: keep infrastructure in multiples of 100, buy land in multiples of 500, and never let infrastructure exceed land.

**Interpretation.** Land exists to price population density and to make farms a land decision rather than a slot decision. It is also the mechanic that ties farms to geography-adjacent space.

**Nation Supremacy decision — adapt infrastructure, reject land.** Infrastructure is kept as the development level that supplies capacity and housing, because it gives a single legible "develop this city" lever. Land is **rejected**: it is a second area currency whose only jobs (density and farm yield) can be served by infrastructure and by the capacity model, and it would smuggle a geographic notion of space into a mapless game. Farm output in Nation Supremacy depends on the number of farm facilities and on research, not on land.

**Nation Supremacy decision — replace slots with capacity points.** The reference's "50 infrastructure = 1 slot" is crisp but forces every building to occupy the same space, so a refinery and a mine compete one-for-one. Our model uses **development capacity points (DC)**: infrastructure yields DC, and a building consumes DC according to its footprint (an extraction facility 1, a processing plant 2, a generator level 2, a research institute 3, a civic centre 2, a warehouse expansion 1). This preserves the one-lever city while letting heavy industry cost more of the city than a mine.

## 5. Improvements: the catalogue and its economics

**Verified (S3).** Improvements are built per city and capped by infrastructure. All categories except Power and Resources require power; an unpowered improvement "will not affect the city". Selling an improvement refunds **50% of the money and resources** used.

**Verified (S4).** Resource improvements: coal/oil/iron/bauxite/lead mines produce 3 tons per day (0.25/turn), cost $1,000–$9,500, upkeep $300–$5,000/day, add pollution, and are limited to 10 per city (uranium 5). Farms produce `Land/500` food per turn, cost $1,000, limit 20.

**Verified (S4).** Mines are **continent-locked**: coal is available in Antarctica, Australia, Europe and North America; oil in Africa, Antarctica, Asia and South America; and so on. Antarctica farms suffer a 50% food penalty.

**Verified (S5).** Manufacturing: refinery 3 oil → 6 gasoline per day; steel mill 3 coal + 3 iron → 9 steel; aluminium refinery 3 bauxite → 9 aluminium; munitions factory 6 lead → 18 munitions. Each costs $30,000–$45,000, upkeep $2,500–$4,000/day, adds pollution, and is limited to 5 per city. The **2nd–5th copy** of the same improvement gets +12.5% each, up to **+50%**, and input usage rises with the bonus.

**Interpretation.** Continent locking is the reference's resource-scarcity engine: it forces trade and makes geography matter. The 50% same-building bonus is a specialisation incentive that rewards stacking one chain in one city, and the rising input usage keeps it from being free.

**Nation Supremacy decision — reject continent locking, adopt a national resource base.** Continent locks are geography, and Nation Supremacy has no map. Every nation may build every extraction facility; what differentiates nations is *what they choose to build and research*, not where they spawned. This is also fairer at creation: no player is born without coal.

**Nation Supremacy decision — reject the 50% same-building bonus.** A bonus for stacking identical buildings is a snowball on the winning chain and makes the fifth copy strictly better than the first. Our specialisation comes from **per-city limits** (max 8 units of one resource, max 4 of one processing chain) and from **capacity costs**, which already make heavy industry a commitment. This keeps the marginal building equal and moves the interesting decision to *which chains* and *which cities*.

**Nation Supremacy decision — adopt a 25% crown-only demolition refund.** The reference's 50% refund of money **and resources** makes build-sell cycling cheap and lets a player recover real materials. We refund 25% of the crowns paid, never materials, and remove the asset's full book value; cycling is a loss, as it should be.

## 6. Power

**Verified (S6).** A coal plant powers **500 infrastructure** and burns 1.2 coal/day; an oil plant powers 500 and burns 1.2 oil/day; nuclear powers **2,000** and burns 2.4 uranium/day plus 100 steel to build; wind powers 250 and costs 30 aluminium. Coal is cheapest and dirtiest, oil slightly dearer and cleaner, nuclear expensive but slot-efficient and pollution-free.

**Verified (S1).** A city is powered only if the supply covers **all** its infrastructure; a partially powered city is not partially productive.

**Interpretation.** Power in the reference is a **binary city-level gate with a slot cost**, not a fungible commodity. Its real function is to make infrastructure expensive to operate and to force a fuel decision (coal vs oil vs nuclear), which in turn drives trade.

**Nation Supremacy decision — keep an explicit power system, already fixed by B-04.** The economy prompt already adopted grid units, three generator classes, fail-closed fuel checks, pro-rata derating and no storage or trade (D-048, ECN-056…065). B-05 owns only the **plants**: their capacity points, costs, limits and prerequisites. Two differences from the reference are deliberate: our derating is **pro-rata rather than binary** (a 60% grid runs 60% of batches), and our generators are **per level** rather than per city, so a city can hold several. This avoids the reference's cliff where one point of missing power disables an entire city.

## 7. Commerce, civil buildings and adverse effects

**Verified (S7, S8).** Commerce buildings add a city-level commerce percentage: supermarket +3%, bank +5%, shopping mall +9%, stadium +12%; subways +8%. Commerce raises citizens' average income and therefore tax revenue. The default cap is 100%, raised to 115% and 125% by projects.

**Verified (S9).** Crime is `((103 − Commerce)^2 + Infrastructure × 100) / 111111 − 2.5 × Police`; disease is a function of population density, base population, pollution and hospitals. Both kill population and therefore reduce tax income.

**Interpretation.** Commerce is the reference's answer to "my city is built out; what now?" — a second income multiplier that scales with population. Disease and crime are the counter-pressure that stops pure infrastructure stacking.

**Nation Supremacy decision — reject commerce buildings and the pollution/disease/crime layer at launch.** Three reasons. (1) B-04's income is `population × tax rate × stability`; a commerce multiplier would be a second multiplier on the same base and would make the tax-rate decision harder to read, not richer. (2) Pollution, disease and crime are three more per-city numbers whose effects are all "less population, less income" — high bookkeeping, low decision variety. (3) Population, health and public order are **Prompt 06's** subject; pre-empting them here would create two owners for one effect. B-05 therefore supplies **housing capacity** (which Prompt 06 consumes) and a **civic centre** that adds housing, and explicitly hands all disease/crime/stability rules to Prompt 06.

## 8. National projects

**Verified (S10).** A nation has **1 free project slot**, plus 1 per **5,000 national infrastructure**, plus 1 for 100 wars. A project costs tens of millions and thousands of resources, and can be destroyed with **no refund**. A new project may be built only every **120 turns**, unless reset with a credit. Projects fall into nine types: production boosters (+20% to +100% to one chain), pollution reducers, disease/crime reducers, land/infrastructure cost reducers (−5% each), commerce boosters, city-cost reducers, war boosters and novelty projects. Built projects survive the loss of the infrastructure that unlocked their slot.

**Interpretation.** Projects are the reference's long-horizon layer: expensive, permanent, mostly percentage modifiers, and gated by infrastructure so they arrive after the city build. They create a second progression axis without a second currency.

**Nation Supremacy decision — adopt a bounded second layer, the National Programme.** We keep the *idea* of a permanent national-scale project but change four things: programmes are **branch capstones** unlocked by finishing a research branch (not bought from a free-standing catalogue); each has a **single named effect** rather than a cluster of percentages; there are **four** at launch, not thirty-nine; and there is **no project-slot currency** — the gate is the research branch itself. The 120-turn cooldown is rejected: it is a real-time gate on a decision the player has already earned.

## 9. Costs, scaling and progression

**Verified (S9).** New-city cost is **cubic**: `50,000 × (X − 1)^3 + 150,000 × X + 75,000`. Infrastructure is exponential in the current level; land is quadratic. Building (improvement) costs are **flat** per copy.

**Verified (S11).** The practical early sequence is: power a city, stack one raw resource to its limit for the 50% bonus, then diversify; commerce and farms are explicitly *not* early purchases.

**Interpretation.** The reference puts all of its scaling into the **city and infrastructure** curves and none into individual buildings. That is a sound separation: it keeps the building menu readable while making each new city a major decision. But the cubic city curve plus the 10-day cooldown makes expansion lumpy.

**Nation Supremacy decision — scale the city and infrastructure, keep buildings flat.** Adopted: flat building costs, rising infrastructure unit cost, rising city cost. Rejected: the cubic explosion and the cooldown. Our city cost is quadratic and mild (about 1,000 crowns for the second city, 22,000 for the twelfth against a mature income), and the gate is national infrastructure, not elapsed days. The result is that expansion is limited by *development*, which the player controls, rather than by a timer.

## 10. Comparison matrix

| Reference mechanic | Evidence | Gameplay purpose | Nation Supremacy decision | Rationale |
|---|---|---|---|---|
| City as the investment container | S1 | Legible unit of growth | **Adopt, adapted** | Keeps the genre's clearest unit; no geography |
| 50 infrastructure = 1 improvement slot | S1, S3 | Couples development to build capacity | **Adapt** | Capacity points, weighted by building footprint |
| Infrastructure × 100 = base population | S2, S9 | Ties housing to development | **Adopt, adapted** | `45,000 + 100 × I` per city, plus civic housing; Prompt 06 consumes it |
| Land area | S1, S9 | Density and farm yield | **Reject** | Second area currency; smuggles in geography |
| Continent-locked resources | S4 | Scarcity and trade | **Reject** | No map; unfair at creation |
| 50% same-building bonus | S5 | Specialisation | **Reject** | Snowballs the winning chain; limits do the job |
| Binary city power gate | S1, S6 | Makes infrastructure costly to run | **Reject** | Pro-rata derating is fairer and already fixed by B-04 |
| Coal/oil/nuclear plant choice | S6 | Fuel trade-off | **Adopt** | Already fixed by B-04; B-05 prices the plants |
| Commerce percentage | S7, S8 | Second income multiplier | **Reject at launch** | Double-counts population; income is B-04's and population is Prompt 06's |
| Pollution / disease / crime | S9 | Counter-pressure on stacking | **Reject at launch** | Three numbers, one effect; Prompt 06 owns public health and order |
| National projects | S10 | Long-horizon progression | **Adopt, adapted** | Four branch capstones, no slot currency, no cooldown |
| Cubic city cost + 120-turn cooldown | S1, S9 | Pacing | **Reject** | Timer-gated, not development-gated |
| Flat improvement costs | S4, S5 | Readable menu | **Adopt** | Scaling lives in infrastructure and cities |
| 50% sale refund | S3 | Reversibility | **Reject** | 25% crown-only refund prevents cycling |
| Instant build | S1, S11 | Immediate feedback | **Reject** | Everything resolves at the next boundary, matching the two-hour turn |

## 11. What the reference does *not* answer

1. **A mapless city.** P&W has no equivalent; every city is a place. The symbolic development centre is our own construction, and its risks (cities feeling interchangeable) are addressed by naming, per-city limits and the capital/colony distinction, not by geography.
2. **A two-hour construction cadence.** The reference resolves improvements instantly on purchase. Our one-boundary rule is inferred from B-02/B-04, not copied.
3. **Research as a facility output.** P&W's progression is projects and policies; it has no research-point building. Our research institutes, RP pool and branch tree are original.
4. **A capacity economy without land.** No source describes a slot system with weighted footprints.
5. **Absence tolerance.** The reference assumes a daily login; our standing-policy and boundary rules must work for a player who is away for days. B-02/B-04 already solve this; B-05 must not reintroduce a per-login action.

## 12. Limitations

- The wiki is **community-maintained**. Two pages mix "per day" and "per turn" units (S4, S5), one is marked as a scratchpad (S9), and one is an unfinished player guide (S11). Figures were used for *shape and ratio*, never copied as our values.
- The official site (S12) exposes no mechanics without an account. No logged-in test was performed, so no claim here is a statement about the live server today.
- The city page's cost table is long and appears current, but its later rows were truncated in retrieval; only the early rows were read, and no P&W cost is used in our design.
- Project costs (S10) are large tables; only the structure, slot rule, cooldown and refund policy were relied on.
- P&W may have patched any of this since the access date.
- **Nothing in this report is a Nation Supremacy rule.** The rules are in [B-05](../11_cities_infrastructure_production_and_research.md), and the numbers are in the [formula register](../11_city_infrastructure_production_and_research_formula_register.md).
