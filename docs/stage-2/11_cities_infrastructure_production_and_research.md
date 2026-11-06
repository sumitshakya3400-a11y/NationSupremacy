# B-05 — Cities, infrastructure, production and research

**Version:** 1.7 · **Created:** 2026-10-25 · **Revised:** 2026-11-04 (v1.7 Prompt 10B-C2 adds the **infrastructure-only asset subledger** `URB-118a`/`URB-118b`: gross capitalised upgrade lots, accumulated impairment, carrying value, zero-cost opening lot, facility exclusion, B-04 reconciliation, repeated-damage cap, repair capitalisation with no impairment reversal, and idempotency. `URB-046` now names the exact P4.1/P5/next-turn boundaries; `URB-157` items 3 and 5 invoke the B-06 `DMP-031` crowding rule and the infrastructure-only impairment formula. No cost, recipe, DC cost, limit, yield or decision changed. The v1.6 text follows for history: v1.6 Prompt 10B-C adopts the single warfare effect on B-05: `OP-05 MISSILE_STRIKE` may target a city and reduce **infrastructure only**, under B-10 `WAR-109a`–`WAR-109l` and `F-WR-037`/`F-WR-038`. The absolute floor is 10, the per-strike cap is 20 levels, the per-city per-campaign cap is 30% of the campaign-start level, damage applies only on attacker victory, capacity and housing are recalculated, book value is impaired proportionally, and repair is an ordinary P4.1 capex order. No city, facility, population or territory may be destroyed or transferred. No construction cost, recipe, DC cost, limit or yield changed. The v1.5 text follows for history: v1.5 reconciles two cross-system caption defects: F-CI-021 now cites Example 15B's actual **22/24** state instead of a 23/24 calculation, and the manual-production contract is stated as `planned_batches = M + A ≤ capacity` here and in B-04's ECN-053/060 and F-EC-006, so a manual batch occupies a slot instead of being added to capacity. No design changed. v1.4 is the consistency pass after independent review. Infrastructure cost now uses D-069's stepped marginal sum in the rulebook as well as the register: 50→500 is 15,750 and the largest order, 10→500, is 16,170, replacing the stale 28,420 bound. Discounts are stated in basis points with exactly one source per cost at launch and no stacking on infrastructure. Research points are allocated exactly once, to the active project or the pool; programmes spend only banked RP and never an active project's progress. Reservations distinguish total, reserved and available balances. Example 12 opens at 1,000 crowns instead of implying a debt; Example 8 shows reservation states. URB-014 cites D-015. No design was redesigned. v1.3 states Example 3's opening treasury, marks Example 1 as the founding balance, gives the research institute and civic centre their register IDs (`bld_lab`, `bld_civic`) and corrects the catalogue ordinal; no number changed. Acceptance audit: the catalogue is counted at **17 types**, not 18, and the tree at **12 technologies**, not 11, here and in every register that cites them; URB-146 now cites REQ-207 instead of a non-existent REQ-258; URB-044 and URB-081 now cite URB-102 and URB-107; URB-167 names the full DD-081…DD-100 range. No cost, formula or worked example changed.) · **Stage 2, Prompt 05**
**Status:** **Draft** — design specification. **No rule here is implemented, migrated or runtime-tested.**
**Bible part:** B-05 · **Authoritative for:** the city model, infrastructure, development capacity, the building catalogue, construction and demolition, power plants, raw-resource and manufacturing facilities, research, national programmes, and the development contracts with Prompts 06–15.
**Companions:** [research report](research/05_politics_and_war_city_infrastructure_production_research.md) · [formula and balance register](11_city_infrastructure_production_and_research_formula_register.md) · [B-04 economy](10_economy_resources_treasury_and_finances.md) · [B-04 register](10_economic_formula_and_balance_register.md) · [B-02 turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [B-03 account and nation lifecycle](09_account_onboarding_nation_creation_and_progression.md) · [requirements](03_requirements_traceability.md)

---

## 1. Purpose and scope

**URB-001 — What this document decides.** *Provisional.* B-05 defines how a nation turns crowns, materials and time into **productive capacity**: what a city is, how infrastructure and development capacity work, which buildings exist and what they cost, how construction resolves inside the two-hour turn, how the four manufacturing recipes and seven raw resources are housed, how research and national programmes progress, and what later prompts may and may not add.

**URB-002 — What this document does not decide.** *Provisional.* B-05 does **not** define population growth, tax policy, stability, disease, crime or domestic politics (Prompt 06); trade, prices, fees or matching (Prompt 07); diplomacy and sanctions (Prompt 08); alliances (Prompt 09); warfare, military units or combat consumption (Prompt 10); world events, rankings or rewards (Prompt 11); moderation and audit procedure (Prompt 12); screens, layout or flows (Prompt 13); the final balance numbers (Prompt 14); or Bible assembly (Prompt 15). Each boundary is stated as a contract in §23.

**URB-003 — The one-sentence design.** *Provisional.* A nation is a **portfolio of named development centres**; each centre has an infrastructure level that yields development capacity and housing; capacity is spent on facilities that either produce the eleven approved resources, generate grid power, or generate research; research unlocks better yields and four national programmes; and every investment resolves at the next two-hour boundary under B-04's accounting.

**URB-004 — Design-only status.** *Provisional.* Nothing in B-05 exists as code. There is no city table, no construction queue, no research job and no scheduler. The 20 worked examples are hand calculations checked by an independent script; no player has built anything.

## 2. Source documents and design authority

**URB-005 — Precedence.** *Provisional.* When documents disagree, this order applies:

1. [DECISIONS.md](../DECISIONS.md) — a recorded project decision.
2. [B-04](10_economy_resources_treasury_and_finances.md) and [its register](10_economic_formula_and_balance_register.md) — the economy's coefficients, recipes, treasury rules, reservation model, settlement order and ledger.
3. [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) — turn identity, phases, action states and recovery.
4. [B-03](09_account_onboarding_nation_creation_and_progression.md) — account and nation policy, starting state and reroll.
5. **This document** — the city, infrastructure, building, research and programme rules.
6. [The B-05 register](11_city_infrastructure_production_and_research_formula_register.md) — the authoritative formula definitions for everything this document owns.

If B-05 and its register disagree, **the register wins until one of them is corrected**. If B-05 and B-04 disagree about a recipe, a coefficient or an accounting rule, **B-04 wins**; B-05 may add a cost, a prerequisite or a modifier, never change what a batch consumes or produces.

**URB-006 — What B-05 inherits unchanged.** *Provisional.* From B-04: the eleven resources (D-044); integer units and crowns (D-045); the four recipes and their power draws (D-046); grid units as derived capacity (D-048); the crown, one pool, no debt (D-049/D-050); capex at P4 and fixed-asset book value (D-051); one shared warehouse and overflow-blocking (D-052); standing policy plus manual orders (D-053); the P3 order (D-054); the append-only ledger (D-055); reference prices (D-058); the standard start (D-063); integer arithmetic (D-064); the food contract (D-065). B-05 adds **no** resource, **no** currency, **no** second warehouse and **no** second clock.

**URB-007 — The register is mandatory for every number.** *Provisional.* Every cost, capacity, yield modifier, research cost and programme effect in this document appears in the register with an expression, units, bounds, rounding, timing and a worked example. A number in prose that is not in the register is a defect.

## 3. Established constraints

**URB-008 — The game.** *Provisional.* Nation Supremacy is a persistent, single-world, browser-based nation strategy game on a **mapless** world: nations, cities and alliances have identities and relationships, not coordinates. A city is never placed, never adjacent, never conquered for its land and never shown on a map.

**URB-009 — The turn.** *Provisional.* The world advances every **two hours on UTC**. All construction, research, production and upkeep in B-05 resolve inside B-02's P3/P4 phases. No rule in B-05 depends on real elapsed time, a login, a click or a page refresh.

**URB-010 — The platform.** *Provisional.* Cloudflare Pages and Supabase remain fixed (D-008/D-009/D-010). B-05 adds no service, no queue product, no cron job and no background worker. Construction and research are **rows with a due turn and a phase**, resolved by the same settlement that already exists in the design; they are not timers.

**URB-011 — The roster is closed.** *Provisional.* The eleven resources are Food, Coal, Oil, Uranium, Lead, Bauxite, Iron (raw) and Gasoline, Ammunition, Steel, Aluminum (manufactured). Grid units and **research points** are non-tradable derived values, not resources: they have no warehouse space, no price, no ledger balance and no trade. Adding a twelfth resource or a second research currency needs a new decision, not a building.

**URB-012 — Account and nation policy.** *Provisional.* One account, one active nation (D-032); a reroll destroys every city, building, infrastructure level, research point, completed technology and programme, and the replacement nation starts from the standard bundle with **no** transfer (D-039/D-059). A shared address alone never blocks a build or a research action (D-035); value-moving actions between a restricted pair do, under B-03's matrix.

**URB-013 — Free-first operation.** *Provisional.* The design assumes a free-tier database and one scheduled settlement per boundary. B-05 is therefore written to add **bounded** work per nation-turn: a fixed number of cities (12), a fixed building catalogue, one construction order per city per turn and one research project per nation. No rule may require iterating an unbounded list per nation.

**URB-014 — Operations Points are D-015's, and their numbers are Prompt 10's.** *Provisional.* D-015 is the current Operations Points decision: a single military-only persistent pool per nation, regenerated by one OP at each boundary's P3.7 opening up to its cap and carried below the cap (amended 2026-11-04), non-transferable, reserved at acceptance and consumed at resolution. Its **numerical values remain provisional** for Prompt 10. D-004 is retained only as history and is marked **superseded by D-015**; no current rule may cite D-004 as the active decision. B-05 does not use, refill, reserve or mention Operations Points as a construction cost.

## 4. Research summary and the design stance

**URB-015 — What the reference game contributed.** *Provisional (research §3–§10).* Politics & War's city is an investment container holding infrastructure, land and improvements; 50 infrastructure buys one improvement slot; infrastructure sets base population at 100 people per point; improvements are flat-cost and category-gated by power; resources are continent-locked; the fifth copy of a building is 50% better; city cost is cubic and gated by a 10-day cooldown; and national projects are expensive permanent percentage modifiers gated by infrastructure and a cooldown. The research report grades each claim and records what was read.

**URB-016 — What we kept.** *Provisional.* (1) The city as the legible investment container. (2) Infrastructure as a single "develop this city" lever that yields both capacity and housing. (3) A building catalogue with explicit costs, prerequisites and per-city limits. (4) An explicit power system with a fuel choice. (5) A long-horizon second progression layer, bounded to four programmes. (6) Flat building costs with the scaling placed in infrastructure and city acquisition.

**URB-017 — What we rejected, and why.** *Provisional.*

| Reference mechanic | Rejected because |
|---|---|
| Geographic placement, land, continents, borders | The world is mapless by design (URB-008); geography would also decide resource access at creation |
| Continent-locked resources | Unfair at creation and impossible without a map; specialisation must be a choice, not a spawn |
| 50% bonus for the fifth identical building | Makes the winning chain win harder and the marginal building unequal; per-city limits do the specialisation job |
| Binary "city powered or not" | B-04 already adopted national, uniform derating, which is fairer and more explainable. The percentage is pro-rata but production is allocated in **whole batches** (`floor(capacity × power_pct / 100)`); B-05 restates that rule rather than inventing proportional output |
| Commerce percentage as a second income multiplier | B-04's income is population × rate × stability; a second multiplier muddies the tax decision and collides with Prompt 06 |
| Pollution, disease and crime as three per-city numbers | Three bookkeeping numbers with one effect (fewer people, less income); Prompt 06 owns public health and order |
| Cubic city cost and a 120-turn city cooldown | Expansion should be gated by development the player controls, not by elapsed real time |
| 50% refund of money **and materials** on sale | Build–sell cycling recovers real value; our refund is 25% of crowns only |
| Instant construction | Everything resolves at the next boundary, so an offline player is never behind a clicking player |
| A free-standing catalogue of 39 projects | Four branch capstones give the same long-horizon feeling with a fraction of the surface |

**URB-018 — The originality claim.** *Provisional.* Nation Supremacy's development system is **not** a P&W clone. Its distinguishing choices are: cities as non-geographic development centres; **weighted capacity points** instead of uniform slots; **national access to every resource** with specialisation by choice; **one-boundary construction** with a per-city construction slot; **research as a facility output** feeding an twelve-technology tree; and **four branch-capstone programmes** instead of a project catalogue. No P&W formula, cost table, building name or project name is copied.

## 5. Design principles

**URB-019 — Every investment has a visible cost, effect and opportunity cost.** *Provisional.* A building must state what it costs in crowns and materials, what capacity it consumes, what it produces or enables, what it costs to keep, and what the player cannot build with the same capacity. A building whose only description is "+X%" is not admissible.

**URB-020 — Capacity is the scarce thing, not clicks.** *Provisional.* The player's real constraint is development capacity and the materials to fill it. B-05 deliberately has **no** per-action energy, no daily build limit, no cooldown and no premium currency. A player who is online all day gains nothing over one who logs in at the boundary.

**URB-021 — Development is legible at a glance.** *Provisional.* A city must be describable in one line: name, infrastructure, capacity used/total, housing, and its facilities by chain. If a city needs a spreadsheet to understand, the model has failed.

**URB-022 — Nothing is destroyed by neglect.** *Provisional.* An offline nation keeps its cities, buildings, research progress and completed technologies. The only recurring losses are the ones B-04 already defines (maintenance unpaid → capacity idle; food short → next-turn tax penalty). B-05 adds no decay, no abandonment and no rust.

**URB-023 — Reversibility is priced, not free.** *Provisional.* Infrastructure cannot be sold; a building can be demolished for 25% of its crown cost; a research project can be abandoned but its crowns and accumulated points are lost. Every reversal is a loss, so a player cannot cycle assets to dodge a decision.

**URB-024 — The economy stays B-04's.** *Provisional.* B-05 changes **what capacity exists**, never what a batch consumes, produces or costs to run. If a building seems to need a new recipe, the answer is a new decision in B-04, not a quiet exception here.

**URB-025 — The design is implementable by one small team.** *Provisional.* The catalogue is 17 building types, 12 technologies and 4 programmes. Every number is an integer. Every rule has a deterministic outcome that a single settlement function can apply in a fixed order.

---

## 6. The city model

**URB-026 — A city is a named development centre.** *Provisional (REQ-188).* A city is a persistent, non-geographic unit of national development. It has a stable identifier, a name, an infrastructure level, a development-capacity pool, a housing capacity and a list of facilities. It has **no** coordinates, land, borders, neighbours, resources in the ground, population of its own, or distance to anything. Two cities of the same nation are interchangeable in rule terms and differ only by what the player built in them and what they are called.

**URB-027 — Cities hold capacity; the nation holds the economy.** *Provisional.* Production capacity, power and research are **national** pools (B-04 §8; URB-073). A city does not produce on its own; it contributes capacity to the national vector, generation to the national grid and points to the national research pool. This is the single most important difference from the reference game and it is deliberate: it keeps B-04's national settlement intact and prevents a city-by-city production loop.

**URB-028 — The capital.** *Provisional (REQ-189).* Every nation has exactly one **capital**, created with the nation (B-03 §8). The capital is a normal city in every mechanical respect except three: it is created with 50 infrastructure rather than 10; it cannot be renamed to a name used by another of the nation's cities; and it is the only city that exists at nation creation. If a nation somehow has no capital, the oldest city is treated as the capital for display; the engine never creates a second one.

**URB-029 — The city record.** *Provisional.* Every city stores: `city_id` (immutable, server-assigned), `nation_id`, `name`, `name_folded` (for uniqueness), `is_capital`, `founded_turn`, `infrastructure`, `capacity_used` (derived), `housing_capacity` (derived), a facility list, and the standard audit columns. The record never stores a coordinate, a region, a terrain type or a resource deposit. `capacity_used` and `housing_capacity` are **derived** from the facility list and infrastructure; they are never editable fields.

**URB-030 — City names are cosmetic and unique within the nation.** *Provisional (REQ-190).* A city name is 3–24 characters after Unicode NFC normalisation; it is folded (case and diacritics) for uniqueness within the nation; leading and trailing whitespace is stripped; control characters and angle brackets are rejected. A rename is free, takes effect immediately, and is limited to one per city per 24 hours to prevent name-spam in public logs. A city name has **no** mechanical effect. Two nations may use the same city name; a nation may not use it twice.

**URB-031 — The city count is bounded at twelve.** *Provisional (REQ-191).* A nation may hold at most **12** cities. The bound is a design and operational choice, not a balance claim: twelve is enough for meaningful specialisation, small enough that a city list is one screen, and it bounds the per-nation work of the settlement. The number is provisional and Prompt 14 may retune it; the **existence of a hard bound** is fixed by this document.

**URB-032 — Founding a city requires development, not elapsed time.** *Provisional (REQ-192).* A nation may found its `k`-th city (`k` from 2 to 12) only when all of the following hold:

1. `k ≤ 12` and the nation currently holds `k − 1` cities.
2. **National infrastructure** — the sum of `infrastructure` across all cities — is at least `100 × (k − 1)`.
3. The nation has **1 expansion slot** available this turn (one founding per nation per turn, §10).
4. The nation has the crown and steel cost of §6.3 unreserved.
5. No construction order for that nation is already resolving as a founding in the same turn.

There is **no** real-time cooldown. A nation that develops quickly may found quickly; a nation that does not develop cannot found at all. This replaces the reference game's 120-turn city cooldown (research §3).

**URB-033 — Founding cost.** *Provisional (REQ-193).* The crown cost of the `k`-th city is

```
city_cost(k) = 400 + 150 × k²
```

plus **20 steel**, charged as capex at P4.1. The cost is flat per city number — it does not depend on the nation's other cities' infrastructure, on the turn, or on a discount. The steel is material cost and is capitalised into the new city's fixed-asset book value at the reference price (D-058); the crown cost is capitalised in full. Examples: the 2nd city costs **1,000 crowns + 20 steel**; the 3rd **1,750**; the 4th **2,800**; the 12th **22,000**.

**URB-034 — A new city starts undeveloped.** *Provisional (REQ-194).* A founded city enters play at the **next** boundary with `infrastructure = 10`, `capacity = 11`, `housing_capacity = 46,000`, and **no facilities**. Its crown and steel cost was charged at founding; its book value is the crown cost plus `20 × 7 = 140` crowns of steel at the reference price. A player who cannot afford to develop a new city has bought an empty shell — a real and visible opportunity cost.

**URB-035 — Cities are permanent for the life of the nation.** *Provisional (REQ-195).* A city cannot be deleted, sold, abandoned, merged, renamed out of existence, or transferred to another nation. There is **no** city-deletion action at launch. The only ways a city ceases to exist are (a) the nation is retired by a reroll or account closure, which destroys every city (B-03 §9.4) and (b) an audited administrative correction under Prompt 12, which must use the reversal mechanism and must not create value. This closes the entire class of "found, strip, delete and repeat" exploits at the root: there is nothing to strip and nothing to delete.

**URB-036 — Specialisation is emergent, not a city class.** *Provisional (REQ-196).* Cities have no declared type, no archetype and no irreversible specialisation choice at founding. What a city specialises in is whatever the player builds there, bounded by per-city limits (URB-060). A player may therefore change a city's role over time by demolishing and rebuilding, at the priced loss of URB-023. This is preferable to a class system because it does not force a new player to choose a build before understanding the economy, and it does not create a "wrong" city that must be rerolled.

**URB-037 — City progression is distinct from nation progression.** *Provisional.* **City-level** development is infrastructure and the facilities inside one city. **Nation-level** development is research, national programmes, city count and the national capacity vector. The two interact only through the published formulas: infrastructure yields capacity and housing; facilities yield capacity, grid units or research points; research yields yield/cost modifiers and unlocks; programmes yield one national effect each. No bonus is applied twice: a modifier is either city-scoped (none at launch) or nation-scoped (all research and programmes), and the register states which.

**URB-038 — A reroll destroys everything B-05 owns.** *Provisional (REQ-197).* On a reroll, every city, infrastructure level, building, reservation, pending construction order, research project, accumulated research point, completed technology, national programme and fixed-asset book value is destroyed with the old nation. The replacement receives the standard bundle and a new capital at 50 infrastructure with the nine starting facilities (URB-047); it receives **no** research, **no** programme, **no** extra city and **no** construction discount. History stays attributed to the old nation (D-059).

---

## 7. Infrastructure

**URB-039 — What infrastructure means.** *Provisional (REQ-198).* Infrastructure is a city's **general development level**: roads, services, utilities, administration and the physical organisation that lets a place hold people and industry. It is not a building, not a resource and not a prerequisite list. It has exactly two mechanical effects: it yields **development capacity** (URB-041) and it raises **housing capacity** (URB-042). It does **not** directly multiply production, tax or research; those effects belong to facilities, research and Prompt 06. Warfare may reduce the level under `OP-05` (URB-157); the damage flows through exactly these two effects and adds no third yield multiplier.

**URB-040 — Infrastructure levels and bounds.** *Provisional.* `infrastructure` is an integer from **10 to 500**. A capital starts at **50**; a newly founded city starts at **10**; the maximum is **500** per city. Levels are discrete: there is no fractional infrastructure, no partial level and no "infrastructure points". The starting values are provisional; the bounds and the integer rule are fixed by this document unless Prompt 14 records a change. The **floor of 10 is absolute**: no construction, demolition, event or `OP-05` strike may take a city below it. Raising the level is a player order (URB-046); lowering it is possible **only** through the warfare damage rule in URB-157, never through a sell, downgrade or transfer action.

**URB-041 — Development capacity.** *Provisional (REQ-199).* A city's development capacity in **capacity points (DC)** is

```
capacity(city) = 10 + floor(infrastructure / 10)
```

A capital at 50 therefore has **15 DC**; a new city at 10 has **11**; a fully developed city at 500 has **60**. DC is a city-scoped integer. It is consumed by facilities (§8) and is never stored, traded or transferred. Capacity is recalculated from infrastructure whenever infrastructure changes; there is no separate "capacity pool" field to drift.

**URB-042 — Housing capacity.** *Provisional (REQ-200).* A city houses

```
housing(city) = 45,000 + 100 × infrastructure + 25,000 × civic_centres(city)
```

people. A capital at 50 with no civic centre houses exactly **50,000** — the standard starting population (D-063) — so a new nation begins with its people exactly housed and no headroom. A new city at 10 houses **46,000**. A city at 500 with three civic centres houses **170,000**. National housing is the sum over cities; **Prompt 06 owns population growth and must treat national housing as a hard input** (§23). B-05 does not grow, move or kill population.

**URB-043 — Infrastructure cost.** *Provisional (REQ-201).* Buying `n` levels from a current level `I` costs

```
infrastructure_cost(I, n) = Σ_{j=I}^{I+n−1} (8 + floor(j / 10))   crowns, before discounts
```

and is charged as capex at P4.1. Each level bought pays the marginal price of **its own** level, so the sum telescopes and splitting an order changes nothing: ten 10-level orders cost exactly one 100-level order. The last level bought is `I + n − 1`; an order whose target would exceed 500 is rejected, never clamped. Examples: 50 → 60 costs `10 × 13 = 130`; 100 → 110 costs `10 × 18 = 180`; 400 → 410 costs `10 × 48 = 480`; 50 → 100 costs `130 + 140 + 150 + 160 + 170 = 750`; 50 → 500 costs **15,750 crowns**; the largest legal order, 10 → 500, costs **16,170 crowns** (490 levels). Both totals are before discounts and are recomputed by `verify_city_numbers.py`. Infrastructure creates **no** material requirement: it is paid work, not steel. This is D-069's model, and F-CI-005 is its authoritative formula.

**URB-044 — The infrastructure discount.** *Provisional.* The Civil Survey technology (`tech_civ_survey`, URB-102) removes **1,000 basis points** — 10% — from the infrastructure crown cost, so the player pays `ceil(base × (10,000 − 1,000) / 10,000) = ceil(base × 9,000 / 10,000)`. Terminology is fixed: **1,000 bp is the discount**, **9,000 basis points is the remaining multiplier**; the two are never written as the same number. The discount is applied **once to the whole order**, after the marginal sum, and the result is a whole crown. At launch there is **no second infrastructure discount**: Civil Methods (URB-072) covers facilities and warehouse expansions only and does not apply to `UPGRADE_INFRASTRUCTURE`, so the two technologies never stack on one order. The registered cap is **2,000 bp**; a future second source must be registered, is **additive** with Civil Survey (never multiplicative), is applied once to the base, and may not take the combined discount above 2,000 bp. A cancelled or failed order pays nothing, so no refund of a discount arises.

**URB-045 — Infrastructure cannot be reduced by the owner.** *Provisional (REQ-202).* There is no sell, downgrade, demolish or transfer action for infrastructure. A city's infrastructure never falls by a player action. The **only** reduction is the bounded warfare damage of URB-157, applied by `OP-05` at P5 and capped per strike and per campaign; retirement still removes the whole city. This keeps the "build to the cap, strip, rebuild" exploit closed while allowing war to have a material, recoverable effect. The cost of a voluntary mistake is the opportunity cost, not a refund.

**URB-046 — Upgrade and repair timing, and cancellation.** *Provisional (REQ-203).* An infrastructure order — including a **repair order** after warfare damage (URB-157) — is submitted while the turn is OPEN, validated and reserved at acceptance, and resolved at **P4.1 of the same turn's boundary**. The new level is physically present for the rest of that turn, so a P5 strike is measured against `I_post_P4_1` (B-10 `WAR-109m`). **Capacity and housing become effective at the next-turn boundary** from the level at the end of the turn: `capacity_effective(T+1) = 10 + floor(I_post_P5(T) / 10)` and `housing_effective(T+1) = 45,000 + 100 × I_post_P5(T) + 25,000 × civic`. Inside turn T itself, an order is checked against `capacity_construction(T) = 10 + floor(I_open(T) / 10)` and population is tested against `housing_population(T) = 45,000 + 100 × I_open(T) + 25,000 × civic`, so a repair bought at P4.1 of T does not retroactively enlarge T's construction capacity or T's housing test. A P5 strike never reverses, cancels or refunds a P4.1 order; it is a separate damage event applied to the post-construction level, and its effect on capacity and housing is likewise read at the next-turn boundary. The order may be cancelled while the turn is OPEN, releasing its crowns; after the turn is LOCKED it cannot be cancelled, and if it fails at P4.1 nothing is charged and the reservation is released (B-02 `F5`/B-04 ECN-138).

---

## 8. Development capacity and the building rules

**URB-047 — The standard capital is fully furnished.** *Provisional (REQ-204).* A new nation's capital is created with **50 infrastructure**, **15 DC**, housing **50,000**, and nine granted facilities: **3 farms, 2 coal mines, 1 oil well, 1 iron mine, 1 refinery and 1 coal power plant**. They consume `3 + 2 + 1 + 1 = 7` DC for extraction, `2` for the refinery and `2` for the generator: **11 of 15 DC**, leaving **4 DC free**. The nine facilities are **granted**, not purchased: their fixed-asset book value is **0** crowns, so the standard-start national wealth stays 2,100 (B-04 Example 1) and no free asset inflates it. Their capacity is exactly the standard capacity vector of D-063: food 3, coal 2, oil 1, iron 1, bauxite 0, lead 0, uranium 0, refining 1, steel 0, aluminum 0, ammunition 0, and one coal generator level.

**URB-048 — Capacity cost by building class.** *Provisional (REQ-205).* Every facility consumes capacity points as follows. The cost is a property of the **class**, not of the individual building, so the player can reason about a category before reading the catalogue.

| Class | DC per unit | Why |
|---|---:|---|
| Extraction facility (one batch of one raw resource) | **1** | A mine or farm is a plot and a crew |
| Processing facility (one batch of one manufactured good) | **2** | A plant needs feedstock handling, process heat and a larger footprint |
| Generator level (6 or 20 GU) | **2** | A plant plus its fuel handling and grid connection |
| Warehouse expansion (+250 units) | **1** | Shelving and handling, not a process |
| Research institute | **3** | Laboratories, staff and instruments |
| Civic centre (+25,000 housing) | **2** | Civic administration and services |

**URB-049 — Per-city limits are the specialisation lever.** *Provisional (REQ-206).* A single city may hold at most:

| Facility class | Per-city limit |
|---|---:|
| Extraction facilities, per resource | **8** |
| Processing facilities, per chain | **4** |
| Generator levels, all classes combined | **6** |
| Warehouse expansions | **6** |
| Research institutes | **2** |
| Civic centres | **3** |

A fully maxed city would need `8×1 + 4×2×4 + 6×2 + 6×1 + 2×3 + 3×2 = 70` DC but has only **60** at infrastructure 500. **Capacity and limits therefore bind together**: a player who fills every limit cannot also max the city's capacity, and must choose which chain to leave short. This is the intended tension and the reason both rules exist.

**URB-050 — Capacity is checked twice.** *Provisional (REQ-207).* An order is checked at **submission** against `capacity_used + order_dc ≤ capacity(city)`, and again at **resolution** against the frozen state (B-02 P2). Because infrastructure can fall only through P5 warfare damage (`URB-045`, `URB-157`), an order accepted before the strike is re-checked at P2 against the execution-time level; if the damage has made it unaffordable in DC, it fails at P2 and releases every reservation. On failure the order is rejected at submission (`F5`) or fails at resolution (`F5`). A P5 strike itself is never rejected for capacity; it can create the **capacity-overdraw** state in URB-051a.

**URB-051 — No order may exceed capacity.** *Provisional.* There is no borrowing, overflow or "unused building" when an order is placed. If the free DC is smaller than the order's DC, the order does not exist. A player who wants a 2-DC refinery with 1 DC free must first upgrade infrastructure (which adds 1 DC per 10 levels) or demolish something. The one exception is the **existing** overdraw caused by warfare damage, which is defined by URB-051a and never authorises a new order.

**URB-051a — Capacity overdraw after damage.** *Provisional.* If `OP-05` damage lowers a city's capacity below the DC its **existing** facilities consume, the city enters `CAPACITY_OVERDRAWN`:

```
overdrawn_dc = max(0, capacity_used − capacity(city))
```

The state changes no facility and deletes no building. It has three effects. (1) **No new construction or DC-claiming order** may be accepted in that city until `overdrawn_dc = 0`; the order fails with the published capacity reason. (2) The city's **production continues at the existing facilities' capacity**, because the facilities still exist and the damage is to general development, not to their equipment; B-04's batch planning is unchanged. (3) The city view shows the overdraw and the two legal remedies: repair infrastructure (URB-157) or demolish a facility. A player is never forced to demolish. The flag clears at the P4.1 check in which `overdrawn_dc = 0`.

**URB-052 — The capacity display is mandatory.** *Provisional.* The city view shows `used / total` DC, a per-class breakdown, and the DC and limit of every buildable facility. It also shows, before commitment, the projected `used / total` after the order. A player must never discover a capacity problem after paying.

---

## 9. The building catalogue

**URB-053 — The launch catalogue is closed at seventeen types.** *Provisional (REQ-208).* The catalogue contains exactly seven extraction facilities, four processing facilities, three generator classes, one warehouse expansion, one research institute and one civic centre. An eighteenth type requires a new decision, a register entry, a capacity cost, a limit and a construction rule; it may not be added as a patch or a seasonal exception.

**URB-054 — Every building declares the same fields.** *Provisional (REQ-209).* For every type: stable `building_id`; display name; class; purpose; DC cost; crown cost; material cost; prerequisites (technology, city count, infrastructure); per-city limit; effect; production chain and batch contribution (if any); grid contribution or draw (if any); upkeep; construction timing; demolition rule; ledger events; failure conditions; UI fields; and the formulas it uses.

**URB-055 — Extraction facilities.** *Provisional (REQ-210).* Each extraction facility adds **one batch** of capacity to its resource chain. Its output per batch, variable cost and maintenance are **B-04's** (register §3.2) and are not restated as new numbers here. A farm therefore adds one batch of `20 food for 12 crowns`; a coal mine one batch of `10 coal for 10 crowns`; and so on.

| ID | Name | Chain | DC | Crowns | Materials | Prerequisite | Limit/city |
|---|---|---|---:|---:|---|---|---:|
| `bld_farm` | Farm | Food | 1 | 120 | 5 steel | — | 8 |
| `bld_coal_mine` | Coal mine | Coal | 1 | 160 | 5 steel | — | 8 |
| `bld_oil_well` | Oil well | Oil | 1 | 220 | 5 steel | — | 8 |
| `bld_iron_mine` | Iron mine | Iron | 1 | 180 | 5 steel | — | 8 |
| `bld_bauxite_mine` | Bauxite mine | Bauxite | 1 | 220 | 5 steel | — | 8 |
| `bld_lead_mine` | Lead mine | Lead | 1 | 260 | 5 steel | — | 8 |
| `bld_uranium_mine` | Uranium mine | Uranium | 1 | 600 | 10 steel, 5 aluminum | `tech_nuclear_engineering` | 8 |

**URB-056 — Processing facilities.** *Provisional (REQ-211).* Each processing facility adds **one batch** to its chain, at **2 DC**. The recipe is B-04's (register §3.3): 10 oil → 8 gasoline; 10 iron + 6 coal → 8 steel; 12 bauxite → 8 aluminum; 8 lead + 4 coal → 10 ammunition. A facility never changes those ratios.

| ID | Name | Chain | DC | Crowns | Materials | Prerequisite | Limit/city |
|---|---|---|---:|---:|---|---|---:|
| `bld_refinery` | Refinery | Refining | 2 | 320 | 15 steel | — | 4 |
| `bld_steel_mill` | Steel mill | Steel | 2 | 380 | 15 steel | — | 4 |
| `bld_smelter` | Aluminum smelter | Aluminum | 2 | 420 | 20 steel | `tech_ind_chem` | 4 |
| `bld_ammo_plant` | Ammunition plant | Ammunition | 2 | 360 | 15 steel | `tech_ind_heat` | 4 |

**URB-057 — Generator plants.** *Provisional (REQ-212).* A generator order buys **one level** (2 DC) and adds that level's grid capacity. Fuel, variable cost, maintenance and derating are B-04's (register §3.4; ECN-056…065).

| ID | Name | GU/level | Fuel/level/turn | Variable cost | DC | Crowns | Materials | Prerequisite | Limit/city |
|---|---|---:|---|---:|---:|---:|---|---|---:|
| `bld_coal_plant` | Coal plant | 6 | 6 coal | 10 | 2 | 280 | 10 steel | — | 6 levels |
| `bld_oil_plant` | Oil plant | 6 | 5 oil | 14 | 2 | 340 | 10 steel, 5 aluminum | — | 6 levels |
| `bld_nuclear_plant` | Nuclear plant | 20 | 1 uranium + 1 lead | 40 | 2 | 1,200 | 30 steel, 20 aluminum | `tech_nuclear_engineering` | 6 levels |

**URB-058 — Warehouse expansion.** *Provisional (REQ-213).* One expansion adds **250 units** to the national warehouse (B-04 ECN-120/122) and costs **180 + 40 × n** crowns (where `n` is the number of expansions already built nationally, starting at 0) plus **5 steel**, for **1 DC**. The rising price satisfies B-04's requirement that expansion have a rising marginal cost. Limit **6 per city**; no national cap beyond the city limit. A `bld_warehouse` is a facility for capacity and demolition purposes even though it produces nothing.

**URB-059 — Research institute (`bld_lab`).** *Provisional (REQ-214).* **2 per city**, **3 DC**, **500 crowns + 20 steel**, upkeep **2 crowns/turn**, produces **1 research point per turn**. Requires no technology. A nation with no institute does not accumulate research points; a project may not be started without at least one institute at the moment of submission.

**URB-060 — Civic centre (`bld_civic`).** *Provisional (REQ-215).* **3 per city**, **2 DC**, **300 crowns + 10 steel**, upkeep **1 crown/turn**, adds **25,000 housing** (URB-042). It produces no resource and no research; its only effect is that more people can live in the city, which Prompt 06 turns into population and B-04 turns into tax income. This is the **only** civic building at launch.

**URB-061 — Why there are no commerce, culture or military buildings.** *Provisional.* Commerce buildings are rejected (URB-017): a commerce percentage would multiply the same tax base as population and blur Prompt 06's tax-rate decision. Culture and prestige buildings have no mechanic behind them and would be decoration. Military buildings belong to Prompt 10, which owns units, training and combat; B-05 deliberately supplies only the **industrial** inputs that warfare will consume (steel, aluminum, gasoline, ammunition).

**URB-062 — The capacity invariant.** *Provisional (REQ-216).* At all times, for every city, `Σ DC of facilities ≤ capacity(city)`, **except** for the declared `CAPACITY_OVERDRAWN` state created by `OP-05` damage (URB-051a). The settlement checks the invariant at P4.1 for every nation; a violation that is not accompanied by a recorded `INFRASTRUCTURE_DAMAGED` event in the same turn is a defect, aborts the turn as `INTERRUPTED`, and is never "fixed" by deleting a building. A recorded overdraw is legal, is displayed, and blocks new DC-claiming orders until it is cleared. Because no facility is created outside a validated order, the invariant is preserved by construction everywhere except the declared damage path.

---

## 10. Construction, demolition and the action lifecycle

**URB-063 — The construction action catalogue.** *Provisional (REQ-217).* B-05 adds exactly seven player actions. Each is a B-02 action with the standard record (B-04 ECN-132) and the standard states `SUBMITTED → ACCEPTED → RESOLVED`, with `REJECTED`, `FAILED` and `CANCELLED` branches (B-02 §18). `PENDING` is the display label for `ACCEPTED`.

| Action | Scope | Reserves | Resolves | Effect |
|---|---|---|---|---|
| `FOUND_CITY` | nation | crowns, 20 steel, expansion slot | P4.1 | new city at the next turn |
| `UPGRADE_INFRASTRUCTURE` | city | crowns, construction slot | P4.1 | +n levels at the next turn |
| `BUILD_FACILITY` | city | crowns, materials, construction slot, DC claim | P4.1 | facility at the next turn |
| `EXPAND_WAREHOUSE` | city | crowns, materials, construction slot, DC claim | P4.1 | +250 warehouse at the next turn |
| `DEMOLISH_FACILITY` | city | construction slot | P4.1 | facility removed; 25% crown refund |
| `START_RESEARCH` / `CANCEL_RESEARCH` | nation | crowns (start), project slot | P4.1 / immediate | project active or abandoned |
| `COMMISSION_PROGRAMME` | nation | crowns, materials, **banked RP**, programme slot | P4.1d | programme active at the next turn |

**URB-064 — One construction slot per city per turn.** *Provisional (REQ-218).* Each city may resolve at most **one** construction-class action per turn (`UPGRADE_INFRASTRUCTURE`, `BUILD_FACILITY`, `EXPAND_WAREHOUSE`, `DEMOLISH_FACILITY`). A nation may also resolve at most **one** `FOUND_CITY` and at most **one** `COMMISSION_PROGRAMME` per turn. The slot is claimed at **acceptance**, not at resolution, so two accepted orders for one city in one turn are impossible: the second is rejected `F5`. This is the pacing device that replaces the reference game's cooldowns and timers: the limit is one build per city per two-hour boundary.

**URB-065 — Validation order at submission.** *Provisional (REQ-219).* The server checks, in this order, and stops at the first failure: (1) the actor owns the nation and the nation is active; (2) the turn is `OPEN`; (3) the action is enabled for this nation; (4) parameters are integers within bounds; (5) the city exists and belongs to the nation (for city actions); (6) the construction slot is free; (7) prerequisites — technology, city count, infrastructure and per-city limit; (8) capacity: `used + DC ≤ capacity`; (9) the idempotency key is new; (10) available crowns cover the crown cost after existing reservations; (11) available materials cover the material cost; (12) for a founding, the national-infrastructure threshold and the 12-city bound. A failure is `REJECTED` with one B-02 code and one sentence; nothing is reserved and the slot is not claimed.

**URB-066 — Acceptance reserves, never charges.** *Provisional.* Every stored value has three balances: **total** (the ledger balance), **reserved** (the sum held by accepted actions) and **available** (`total − reserved`). On acceptance the engine writes `RESERVATION_HELD` for the crowns and every material, claims the construction slot and records the **DC claim** (`dc_claimed`) on the action. It does **not** debit the total: the crowns remain in the treasury and the materials in the warehouse until P4.1. Only `available` falls, and every affordability check (URB-065 steps 10–11) reads `available`, never `total`. Resolution consumes the reserved amount exactly once and closes the reservation in the same transaction (URB-067); cancellation or failure releases it and charges nothing (URB-068/069). The DC claim is not a transferable reservation object; it exists so the city view can show `used + claimed` and so the resolution check is comparable. The same three-balance rule governs research points reserved by `COMMISSION_PROGRAMME` (URB-095). The bare word "balance" is a defect in this specification: it must always be qualified as total, reserved or available.

**URB-067 — Resolution at P4.1.** *Provisional (REQ-220).* At the boundary, after P3 closes, B-05 resolves before trade:

| Sub-phase | What resolves | Ordering |
|---|---|---|
| **P4.1a** | `FOUND_CITY` | one per nation; cost charged; city created for the next turn |
| **P4.1b** | `DEMOLISH_FACILITY` | per city, before builds in the same city |
| **P4.1c** | `UPGRADE_INFRASTRUCTURE`, `BUILD_FACILITY`, `EXPAND_WAREHOUSE` | per city, in B-02 B1 `(submitted_at, action_id)`; at most one per city by URB-064 |
| **P4.1d** | `COMMISSION_PROGRAMME` | one per nation |
| **P4.2** | research progress and completion | one active project per nation |
| **P4.3** | trade settlement (Prompt 07) | B-04's rules; unchanged |

The sub-phase order is published, deterministic and independent of request arrival order. A construction at P4.1 cannot change a P3 production result (B-04 ECN-162); it takes effect next turn.

**URB-068 — Cancellation.** *Provisional.* An order may be cancelled while the turn is `OPEN` (B-02 §18). Cancellation releases every reservation, releases the construction slot and the DC claim, writes `CANCELLED`, and charges **no fee**. After `LOCKED` the order cannot be cancelled; it either resolves or fails.

**URB-069 — Failure.** *Provisional (REQ-221).* At P4.1 the order is re-validated against the frozen state. If a material, crown, slot, limit or capacity check fails, the order writes `FAILED` with a B-02 code, releases every reservation and charges nothing. A failed construction never partially builds and never leaves a half-charged asset. Because capacity cannot fall and the slot is exclusive, the only realistic failures are a materials shortfall caused by an earlier P3 consumption and an administrative freeze (Prompt 12).

**URB-070 — Exactly-once construction.** *Provisional (REQ-222).* Every construction event carries a deterministic `event_key` of `(turn_id, nation_id, 'P4.1', building_id_or_action_id, sequence)` (B-04 ECN-155). A retried settlement reads the stored event and does nothing; an attempt to write a *different* event under the same key aborts the turn. A completed order can never build twice, and a retried request with the same idempotency key returns the original result (B-04 ECN-141).

**URB-071 — Demolition.** *Provisional (REQ-223).* A facility may be demolished by its owner. It occupies the city's construction slot for that turn, frees its DC at the **next** turn, removes its full book value, refunds **25% of the crown cost actually paid** (rounded down, materials never refunded), and writes `ASSET_RETIRED` and `REFUND`. It cannot be demolished while a construction order in the same city is pending. The starting granted facilities have crown cost 0, so their demolition refunds **0** — a player cannot mine the starting grant for cash.

**URB-072 — The construction discount.** *Provisional.* The Civil Methods technology removes **1,000 basis points** (10%) from the **crown** cost of `BUILD_FACILITY` and `EXPAND_WAREHOUSE`: `ceil(crown_base × 9,000 / 10,000)`. It applies to nothing else. Materials, city founding, programmes and **`UPGRADE_INFRASTRUCTURE`** pay full price; infrastructure's only discount is Civil Survey (URB-044). A nation holding both technologies therefore receives exactly **one** 10% discount on any single order, never 20% on infrastructure. The cap is 2,000 bp, a future second construction source is additive and applied once to the base, and no discount is applied per level, per material or twice through overlapping categories.

**URB-073 — The national capacity vector.** *Provisional (REQ-224).* For each chain, national capacity is the number of facilities of that chain across all cities. For power it is the sum of generator levels by class. For research it is the number of research institutes. B-04's settlement reads this vector; it never iterates cities to produce. A facility's city affects only capacity accounting and the per-city limit, not the output it contributes.

---

## 11. Power plants and the grid

**URB-074 — The grid is national and B-04 owns it.** *Provisional (REQ-225).* Grid units, fuel burn, fail-closed generator checks, demand, uniform derating and the no-storage rule are fixed by B-04 (ECN-056…065, D-048). B-05 adds only the **plants**: their DC, costs, limits and prerequisites (URB-057). A city does not have its own grid and there is no transmission loss, distance or interconnection rule.

**The power rule, restated without ambiguity.** For each chain, `planned_batches = M + A`, where `M` is the accepted manual batches and `A` is what the standing policy schedules in the slots they leave, with `M + A ≤ capacity`. `power_demand` is the sum of `planned_batches × draw`. A manual batch **occupies** a slot inside capacity and is therefore counted once as part of the plan; `capacity + M` would exceed the chain's own limit and is invalid (ECN-053/060, F-EC-006). If supply is short, `power_pct = floor(10,000 × supply / demand)` and each chain gets `batches_available = floor(capacity × power_pct / 10,000)` **whole batches**. There is no proportional output, no fractional unit and no minimum-power threshold: a chain with capacity 1 at 66% runs **0** batches, and a chain with capacity 2 at 66% runs **1**. Accepted manual orders take the available batches first, in B1 order, and fail atomically if they cannot all run (ECN-062/063). B-05 adds no priority list, no per-chain power allocation and no "essential" exemption.

**URB-075 — Generator levels are additive.** *Provisional.* A nation's supply is `6 × (coal levels + oil levels) + 20 × nuclear levels`, subject to each level passing its own fuel check at P3.4. Levels may be spread across cities; the grid does not care which city a level stands in. The per-city limit is 6 levels, so a nation needs at least two cities to exceed 36 GU from coal.

**URB-076 — Nuclear power is researched, not bought.** *Provisional (REQ-226).* `bld_nuclear_plant` and `bld_uranium_mine` require `tech_nuclear_engineering` (URB-131). Before that technology, a nation cannot mine uranium or build a nuclear plant; it can still hold uranium from trade or a reward, and it can still build coal and oil plants. The gate is a **building prerequisite**, not a change to B-04's uranium sink (ECN-073).

**URB-077 — Overbuilding is a real mistake.** *Provisional.* Because surplus GU is discarded (ECN-059), a generator level that never runs still costs its 2 DC, its construction and its 2 crowns/turn maintenance, and burns fuel when it does run. The interface must show projected supply, demand and surplus **before** a plant is ordered (URB-146).

**URB-078 — What B-05 does not add to power.** *Provisional.* No batteries, no storage, no dispatch orders, no per-city brownouts, no priority chain, no emergency generator and no electricity resource. A future change to any of these is a B-04 decision, not a building.

---

## 12. Raw-resource production facilities

**URB-079 — Every raw good has a facility and every nation may build it.** *Provisional (REQ-227).* The seven raw goods map to the seven extraction facilities of URB-055. There is **no** national resource affinity, no spawn bonus, no continent lock and no hidden deposit. A nation's raw-resource profile is exactly what it builds and researches. This is the central fairness choice of the mapless economy (research §5): no player is born unable to make steel.

**URB-080 — Output.** *Provisional (REQ-228).* For resource `r`, with `B_r` national batches and `Y_r` B-04's output per batch:

```
output(r) = B_r × (Y_r + yield_bonus(r))
```

`yield_bonus(r)` is the sum of completed technology and programme bonuses for that resource, capped by the register (§4.9). B-04's `batches_run` limits — money, space, and the food chain's priority — still apply; the bonus changes the output of a batch that runs, never whether it runs. There is no percentage compounding and no rounding inside the bracket: the bonus is an integer number of units.

**URB-081 — Food is the survival chain and has no land.** *Provisional (REQ-229).* A farm produces B-04's 20 food per batch for 12 crowns and 1 crown of maintenance; B-05 adds no land, season, weather, irrigation or fertility rule. The only food modifiers are the two Agriculture technologies and the Granary programme (URB-102, URB-107). Food storage, consumption and shortage remain B-04's (ECN-080…091, D-065); Prompt 06 owns population and may not change the food formula.

**URB-082 — Uranium is deliberately late.** *Provisional.* The uranium mine's technology prerequisite (URB-076) means a new nation runs coal or oil power for its first cities. Uranium's only sink remains nuclear generation (ECN-073); B-05 adds no uranium building and no enrichment step.

**URB-083 — Shortages fail closed.** *Provisional (REQ-230).* If a facility's variable cost cannot be paid, the batch does not run; if its output would not fit the warehouse, the batch does not run; if a processing facility lacks an input, its batch does not run (B-04 ECN-048/050, ECN-124). B-05 adds no partial run, no throttling and no "efficiency" state. The digest names the blocking reason (ECN-055).

**URB-084 — The extraction upkeep is B-04's.** *Provisional.* Each extraction batch pays B-04's **1 crown maintenance** whether or not it runs (ECN-051). The Survey Directorate programme reduces the batch **variable cost** by 2 crowns (minimum 2), never the maintenance.

---

## 13. Manufacturing facilities

**URB-085 — One facility class per chain.** *Provisional (REQ-231).* Refining, steel, aluminum and ammunition each have exactly one facility (§9). A facility adds one batch; four facilities of a chain give four batches, subject to B-04's power, input, money and space limits. There is no second-tier "heavy" facility, no alternate recipe and no per-facility recipe choice at launch.

**URB-086 — The facility owns nothing.** *Provisional (REQ-232).* Inputs come from the **national** inventory, output goes to the **national** warehouse, and power comes from the **national** grid. A city does not have a local stockpile, a local grid or a local workforce number. This is what makes the B-04 settlement a single national pass rather than a per-city simulation.

**URB-087 — Multiple facilities share the national limits.** *Provisional.* Four refineries in one city and four in another are eight batches of refining with one combined input check, one power demand and one space check. The per-city limit (4) constrains where they stand; the national vector constrains what they do.

**URB-088 — Insufficient input or money.** *Provisional (REQ-233).* A batch that lacks any input does not run and consumes **nothing** — not the other inputs, not the money (B-04 ECN-068). A batch whose variable cost is unaffordable does not run. A manual order that cannot run all its batches fails atomically and releases everything (ECN-139). B-05 adds no queue that would "wait" for an input within the same turn.

**URB-089 — Storage and output timing.** *Provisional.* Output is added in the same P3.5 step (ECN-079) and is available to a later step but not an earlier one. If the warehouse is full, the batch is `SPACE_BLOCKED` and nothing is consumed. B-05's only storage contribution is the warehouse expansion (URB-058).

**URB-090 — The facility is the only way to add manufacturing capacity.** *Provisional.* Technology adds **yield** (`+1` unit per batch) and the Standards Bureau reduces processing maintenance, but nothing adds a batch except a facility. A nation cannot buy capacity with crowns alone, cannot rent it and cannot receive it as a reward without a Prompt 11 decision and a register row.

**URB-091 — The recipe cannot be changed by a building.** *Provisional (REQ-234).* No facility, technology or programme may alter a recipe's input list. The only permitted changes are B-04's, through a new B-04 revision with a decision (ECN-066/076).

---

## 14. Research and technological progression

**URB-092 — Research is a facility output, not a currency.** *Provisional (REQ-235).* Research points (**RP**) are produced by research institutes (URB-059) and spent on projects and programmes. RP is a **non-tradable progression value**: it has no warehouse space, no price, no ledger balance, cannot be traded, gifted, sold or destroyed by a raid, and is not a twelfth resource. The pool is an integer stored on the nation.

**URB-093 — One active project per nation.** *Provisional (REQ-236).* A nation may have at most **one** research project in progress. Starting a second is rejected. This is a deliberate pacing choice: it makes research an ordered sequence of commitments rather than a parallel shopping list, and it keeps the per-nation settlement bounded. The limit is a design rule, not a technical limit.

**URB-094 — Starting a project.** *Provisional (REQ-237).* `START_RESEARCH` requires: at least one research institute standing at submission; the technology's prerequisites already completed; the technology not already completed or in progress; the crown cost unreserved; and the project slot free. On acceptance the crowns are charged immediately as a **research investment** (B-04 ECN-093) and the project records `progress = 0`, `started_turn`, `cost_rp`, `cost_crowns`. The crowns are **not** capitalised into fixed assets and are **not** refunded on abandonment.

**URB-095 — Progress at P4.2.** *Provisional (REQ-238).* At each boundary, after construction:

```
rp_generated = research_institutes(nation)              # F-CI-020
need         = max(0, cost_rp − progress)              # 0 when no project is active
rp_applied   = min(rp_generated, need)
progress    += rp_applied                              # capped by construction of `need`
rp_pool     += rp_generated − rp_applied               # overflow or idle banks
rp_available = rp_pool − rp_reserved                   # reserved by accepted programmes
```

**One assignment, never two.** A point generated at P4.2 is assigned to exactly one destination: the active project's progress, or the pool. `progress` is not a balance and is never added to the pool; the pool is never applied to progress automatically. A point that finishes a technology's last unit is not banked as well, and no point is ever counted in both places. The per-settlement identity the engine checks is `Δprogress + Δrp_pool + rp_consumed_by_programmes = rp_generated`: every generated point is accounted for exactly once, and the identity fails loudly if a retry applies a point twice.

**Timing.** RP is generated first and then applied, so an institute built at P4.1 of turn T does **not** produce in turn T (it is available next turn, URB-046/067); an institute demolished at P4.1b of turn T does **not** produce at P4.2 of turn T. If the nation has no active project, `need = 0`, `rp_applied = 0` and the whole generation banks. If the nation has no institute, no RP is generated and the project makes no progress.

**Programmes spend banked RP only.** `COMMISSION_PROGRAMME` requires `rp_required` **banked** points. At acceptance they are reserved: `rp_reserved += rp_required`, so `rp_available` falls but `rp_pool` does not. At **P4.1d**, before generation, the engine consumes them (`rp_pool −= rp_required`, reservation closes) and activates the programme. Cancellation before acceptance, or failure at P4.1d, releases the reservation and leaves the pool unchanged. Because a programme reads `rp_required` from the pool and never from `progress`, **spending banked points cannot reduce an unrelated active technology**, and a project's progress is never a currency. Because P4.1d precedes P4.2, a programme cannot be funded by points generated in the same settlement; the player must have banked them earlier — by running without a project or by completing one with overflow. This is the planning cost that makes programmes a real alternative to research rather than a free parallel track.

**Overflow rule.** When `rp_generated > need`, the surplus banks in the same step. Nothing is discarded, nothing is carried into the next project automatically, and a completed technology's progress is not converted back into points. Example 15B shows the arithmetic and Example 15C shows a banked programme funded while a separate technology runs.

**URB-096 — Completion.** *Provisional (REQ-239).* When `progress` reaches `cost_rp` exactly — URB-095 never lets it exceed the cost — the project completes at that P4.2: the technology is recorded as completed with the completion turn, `progress` is closed at `cost_rp` and is **not** converted into pool RP, `RESEARCH_COMPLETED` is written, and the effect becomes active **at the next turn**. A completed technology cannot be started again, cannot be cancelled, and cannot be lost by a later change of prerequisites. Prerequisites are checked only at start.

**URB-097 — Abandonment.** *Provisional (REQ-240).* `CANCEL_RESEARCH` may be issued while the turn is OPEN. It releases the project slot, writes `RESEARCH_ABANDONED`, and **loses** the crown cost and all accumulated progress. This is the priced reversibility rule (URB-023): a player who changes their mind pays for the change, and no "research refund" loop exists.

**URB-098 — Research is national and survives city changes.** *Provisional.* Completed technologies and the RP pool belong to the **nation**, not to a city. Demolishing the institute that produced the points does not remove the points, the completed technology or the modifier. A reroll destroys all of it (URB-038).

**URB-099 — Research takes effect at the next boundary and is never retroactive.** *Provisional (REQ-241).* A technology completed at P4.2 of turn T applies from turn T+1. It never changes a P3 result of turn T, never refunds a cost already paid, and never re-runs a batch. This is B-04 ECN-162 applied to research.

**URB-100 — The modifier classes and their caps.** *Provisional (REQ-242).* Every technology and programme effect is one of five declared classes. A new technology must choose one; an effect outside these classes needs a new decision and a register entry.

| Class | Unit | Cap | Stacking |
|---|---|---|---|
| Yield bonus | `+n units per batch` for one or more named resources | **+3** for food (20→23); **+1** for each other raw; **+1** for each manufactured good | Additive within the class |
| Variable-cost bonus | `−n crowns per batch` | Never below **2** crowns per batch | Additive, then floor at 2 |
| Maintenance bonus | `−n crowns per batch` | Never below **1** crown per batch | Additive, then floor at 1 |
| Construction/infrastructure discount | basis points | **2,000 bp** (20%) | Exactly **one source per cost** at launch: Civil Survey on infrastructure (URB-044), Civil Methods on facilities and warehouse expansions (URB-072). A future second source is additive, applied once to the base, never multiplicative |
| Structural | a named unlock or a `+n DC` | Declared per technology | Never repeated |

**URB-101 — No percentage yield, no compounding.** *Provisional.* Yields are integers added per batch, never percentages and never multiplied by another bonus. This keeps B-04's integer guarantee (D-045) and makes every research effect checkable by hand. A future percentage modifier would need a rounding rule and a decision, and is not admissible at launch.

**URB-102 — The initial technology tree is twelve technologies.** *Provisional (REQ-243).* Five branches: Agriculture, Extraction, Industry, Civil works and Energy. Costs are provisional; the structure is fixed. A technology's `rp` is the number of research points required; its `crowns` is the one-time investment.

| ID | Name | Branch | RP | Crowns | Prerequisite | Effect |
|---|---|---|---:|---:|---|---|
| `tech_agri_rotation` | Crop rotation | Agriculture | 24 | 160 | — | **+1 food** per farm batch |
| `tech_agri_mechanisation` | Mechanised harvesting | Agriculture | 44 | 300 | `tech_agri_rotation` | **+1 food** per farm batch |
| `tech_ext_coal` | Deep coal shafts | Extraction | 20 | 140 | — | **+1 coal** per batch |
| `tech_ext_oil` | Enhanced recovery | Extraction | 32 | 220 | `tech_ext_coal` | **+1 oil** per batch |
| `tech_ext_metals` | Ore beneficiation | Extraction | 40 | 280 | `tech_ext_coal` | **+1 iron** and **+1 bauxite** per batch |
| `tech_ext_deep` | Deep extraction | Extraction | 56 | 360 | `tech_ext_metals` | **+1 lead** and **+1 uranium** per batch |
| `tech_ind_heat` | Process heat | Industry | 28 | 200 | — | **+1 steel** per batch; unlocks the ammunition plant |
| `tech_ind_chem` | Industrial chemistry | Industry | 48 | 340 | `tech_ind_heat` | **+1 gasoline** and **+1 aluminum** per batch; unlocks the aluminum smelter |
| `tech_ind_ordnance` | Precision ordnance | Industry | 36 | 260 | `tech_ind_heat` | **+1 ammunition** per batch |
| `tech_civ_survey` | Civil survey | Civil works | 20 | 140 | — | Infrastructure cost **−10%** |
| `tech_civ_methods` | Prefabrication | Civil works | 40 | 280 | `tech_civ_survey` | Construction crown cost **−10%** |
| `tech_nuclear_engineering` | Nuclear engineering | Energy | 60 | 500 | `tech_civ_methods`, `tech_ind_chem` | Unlocks the **uranium mine** and the **nuclear plant** |

Total: **448 RP** and **3,180 crowns** to complete the launch tree. The tree is deliberately short: twelve technologies, every one of which changes a number a player can see. There is no "+0.5%" filler.

**URB-103 — Branch completion.** *Provisional.* A branch is **complete** when every technology in it is completed:

| Branch | Technologies | Complete when |
|---|---|---|
| Agriculture | 2 | both completed |
| Extraction | 4 | all four completed |
| Industry | 3 | all three completed |
| Civil works | 2 | both completed |
| Energy | 1 | `tech_nuclear_engineering` completed |

Branch completion is what unlocks a national programme (§15). The Energy branch has no programme: its technology is already a structural unlock.

**URB-104 — Research does not expire and cannot be lost by inactivity.** *Provisional (REQ-244).* A completed technology is permanent for the life of the nation. A dormant nation (D-028) keeps its technologies, its RP pool and any in-progress project; the project simply does not advance while no institute stands, and resumes when one does. There is no research decay, no upkeep on completed technology and no "use it or lose it" rule.

**URB-105 — Adding technology later.** *Provisional (REQ-245).* New technologies may be added in a later revision or prompt, provided each has a stable ID, a branch, a cost, a prerequisite, one declared effect class and a register entry. Adding a technology may **not** rename an existing ID, change an existing cost, move a technology between branches, or invalidate a completed project. Save data stores IDs and completion turns, never tree positions.

**URB-106 — Research and warfare.** *Provisional.* B-05 does **not** define combat technology, unit unlocks, weapons or war bonuses. Prompt 10 owns them and may add a Military branch with its own technologies, provided it registers them and respects URB-100's classes. The interface between the two is a **branch table** and the completion record; B-05 supplies no combat modifier.

---

## 15. National programmes

**URB-107 — Programmes are branch capstones.** *Provisional (REQ-246).* A **national programme** is a permanent, nation-wide capability unlocked by completing a research branch. There are four at launch, one per branch that has one. A programme is not a technology, not a building and not a project slot: it is a single named effect that a nation either has or does not have.

| ID | Name | Branch | RP | Crowns | Materials | Effect |
|---|---|---|---:|---:|---|---|
| `prg_granary` | National Granary Network | Agriculture | 100 | 900 | 100 steel, 50 aluminum | **+500 warehouse** capacity; **+1 food** per farm batch |
| `prg_survey` | National Survey Directorate | Extraction | 100 | 1,000 | 100 steel, 50 gasoline | Extraction variable cost **−2 crowns** per batch (min 2) |
| `prg_standards` | National Standards Bureau | Industry | 100 | 1,200 | 150 steel, 50 aluminum | Processing maintenance **−1 crown** per batch (min 1) |
| `prg_civil_works` | Civil Works Directorate | Civil works | 100 | 1,100 | 120 steel, 60 aluminum | **+2 DC** in every city |

**URB-108 — Commissioning a programme.** *Provisional (REQ-247).* `COMMISSION_PROGRAMME` requires the branch to be complete, the programme not already held, the programme slot free (one per turn), and the crowns, materials and `rp_required` **banked** points unreserved. At acceptance the crowns and materials are reserved and the RP are reserved (`rp_reserved`), so the RP leave `rp_available` but stay in `rp_pool`. At P4.1d the reserved crowns and materials are charged and the RP are consumed from the pool; a failure releases everything and charges nothing. The programme is active from the **next** turn. It cannot be cancelled after acceptance, destroyed, sold, refunded or transferred. A reroll destroys it.

**URB-109 — Programmes do not stack with themselves.** *Provisional.* Each programme exists once per nation. Its effect is applied once, in its declared class, under URB-100's cap. A second source of the same effect (for example a future technology granting food yield) is additive but may not exceed the cap; at launch no cap is reached by the four programmes.

**URB-110 — Why four programmes and not thirty-nine.** *Provisional.* The reference game's projects are a broad catalogue of percentage modifiers. A catalogue that large is content the design cannot yet balance, and most entries are invisible in play. Four capstones give the long-horizon layer a clear shape: each is the payoff for a branch a player deliberately completed, each changes a different decision (storage, extraction cost, processing upkeep, city capacity), and none is a prerequisite for another. Prompt 11 may add a reward that grants a programme only through a decision and a register row; B-05 does not.

**URB-111 — What a programme is not.** *Provisional.* A programme is not a city building, occupies no DC, needs no institute, has no upkeep, does not count toward any per-city limit, and cannot be lost by losing a city (cities cannot be lost). It is a line on the nation record, not a facility.

---

## 16. Queues and the two-hour settlement

**URB-112 — There is no queue object.** *Provisional (REQ-248).* B-05 does not create a FIFO construction queue, a build timer or a research timer. An order is a B-02 action with a `resolves_at_turn` and a phase; the settlement reads all accepted actions for the turn and applies them in the published order (URB-067). This is what makes the system resumable: the state is the action set, not a process.

**URB-113 — The per-turn limits are the pacing.** *Provisional.* One construction action per city, one founding and one programme per nation, one active research project. A nation with twelve cities can therefore resolve at most twelve construction actions per boundary — a bounded number that the settlement can iterate without a queue table.

**URB-114 — Ordering inside a city.** *Provisional.* Demolition resolves before construction in the same city (URB-067), so a player may demolish a facility and build another in the same turn **only if** both orders were accepted in the same turn and the city's single construction slot allowed it — which it does not. In practice, therefore, a city does one thing per turn: the ordering rule exists so that a future multi-action change has a defined answer, not because a player can use it now.

**URB-115 — Recovery.** *Provisional (REQ-249).* B-05's actions use B-04's checkpoint and event-key machinery (ECN-154…161). A settlement interrupted after P4.1a resumes at the next unfinished sub-phase; a completed founding or building is not repeated; an action that had not resolved is still pending and is re-validated against the same frozen state. A duplicate scheduler invocation reads the stored result. Nothing in B-05 introduces a second recovery path.

**URB-116 — No action depends on wall-clock time.** *Provisional.* A construction order submitted at 09:59 and one submitted at 10:01 resolve at the same boundary if both are in the same OPEN window, and neither resolves "after two hours" on its own. The scheduler, not the order, decides when time passes.

**URB-117 — Player notification.** *Provisional (REQ-250).* At the boundary the digest lists, per nation: construction completed, construction failed and why, city founded, infrastructure level, research progress and completion, programme commissioned, upkeep charged, and any capacity or storage warning. A player who logs in after three turns can reconstruct exactly what happened without reading a database.

---

## 17. Accounting, cost, upkeep and book value

**URB-118 — Construction is capex.** *Provisional (REQ-251).* Every construction, infrastructure and founding charge is **capital expenditure** at P4.1 under B-04 ECN-098: the crowns and the materials are charged when the order resolves, the asset's **book value** is the crown cost plus the reference-price value of the materials, and it is added to `fixed_asset_book_value` (B-04 ECN-108). Capex never appears in net operating income. A building's cost is never charged twice and never expensed. Warfare damage **impairs infrastructure book value only** in proportion to the levels removed (URB-157); impairment is a reduction of the recorded infrastructure asset, not a sale, refund or expense, and it creates no crown. Facility book value is **excluded** from infrastructure impairment and is never reduced by a strike.

**URB-118a — The city infrastructure asset subledger.** *Provisional (REQ-251a).* City infrastructure is the only B-05 asset that warfare damage may impair, so it has its own subledger per city:

```
infrastructure_gross_capital(city)        = Σ capitalised crown cost of completed UPGRADE_INFRASTRUCTURE lots
infrastructure_accumulated_impairment(city) ≥ 0
infrastructure_carrying_value(city)       = infrastructure_gross_capital − infrastructure_accumulated_impairment
fixed_asset_book_value (B-04 ECN-108)     = Σ_city infrastructure_carrying_value + Σ other recognised fixed assets
```

- **Initial treatment.** The levels a city starts with — **50** for the standard capital (URB-047) and **10** for a new city (URB-042) — are an opening lot with **zero capitalised cost**. They contribute **0** to gross capital and **0** to carrying value. The starting fixed-asset book value therefore stays 0 for infrastructure, exactly as the granted facilities are 0 (URB-047).
- **Upgrade-lot capitalisation.** Every completed `UPGRADE_INFRASTRUCTURE` order adds one lot: `gross += crown cost actually charged` (after the URB-044 discount), `accumulated` unchanged, `carrying += the same cost`. A 50 → 60 purchase is one lot of 130 crowns; gross 130, carrying 130.
- **Owner-only, single ledger.** The subledger is not a second account beside B-04: `fixed_asset_book_value` is defined as its sum plus the other recognised fixed assets. No parallel "city book value" number exists and none may be introduced.
- **Facilities excluded.** Facility capex keeps its own book value under URB-118 and URB-121 and is never touched by infrastructure impairment.
- **No new ledger type.** Lots, impairment and capitalisation reuse the existing `CAPEX`, `INFRASTRUCTURE_UPGRADED`, `INFRASTRUCTURE_DAMAGED` and `INFRASTRUCTURE_REPAIRED` events.

**URB-118b — Infrastructure impairment, repair capitalisation and idempotency.** *Provisional (REQ-251b).* On a `OP-05` strike that removes `removed` levels (B-10 `WAR-109`):

```
carrying_before     = infrastructure_carrying_value(city)
impaired            = min(carrying_before, floor(carrying_before × removed / I_combat))
infrastructure_accumulated_impairment += impaired
carrying_after      = carrying_before − impaired
fixed_asset_book_value −= impaired
```

`I_combat` is the physical level read at P5 after P4.1 (B-10 `WAR-109m`), never a stale opening level. Impairment is capped at the existing carrying value, so it can never drive the carrying value below 0 and can never exceed gross capital: the invariant `accumulated ≤ gross` holds after every event, and repeated damage reads the **post-impairment** carrying value, so a second strike in the same turn cannot over-impair the asset.

A repair order is capitalised as a **new infrastructure lot**, not as a reversal:

```
gross += repair_cost;   accumulated unchanged;   carrying += repair_cost
fixed_asset_book_value += repair_cost
```

Earlier impairment is therefore never reversed. The `INFRASTRUCTURE_DAMAGED` event carries `damage_event_id = (turn_id, strike_action_id, city_id)`; replaying the same id applies nothing. `INFRASTRUCTURE_REPAIRED` is keyed on the repair `order_id`; replaying it applies nothing. Neither event creates crowns, materials or a new ledger type. A failed or cancelled repair charges nothing and releases its reservation once.

Worked check: zero-cost opening at `I = 50`; upgrade 50 → 60 costs 130, gross 130, carrying 130; a 5,000-crown facility is untouched, so national fixed assets are 5,130. A strike removes `ceil(60 × 500 / 10,000) = 3`; `impaired = min(130, floor(130 × 3 / 60)) = 6`; carrying 124, gross 130, accumulated 6, national 5,124, facility still 5,000. Repairing 3 levels at `I = 57` costs `3 × (8 + floor(57/10)) = 39`; gross 169, accumulated 6, carrying 163, national 5,163. A second strike of 3 levels then impairs `floor(163 × 3 / 60) = 8`; accumulated 14, carrying 155.

**URB-119 — Research and programmes are investments, not assets.** *Provisional (REQ-252).* A research project's crown cost and a programme's crown and material cost are **economic investment** (B-04 ECN-093): they leave the treasury and the warehouse and are **not** added to fixed-asset book value, because there is no durable asset to sell or demolish. They are reported on their own line, separate from capex and from operating expenses. National wealth therefore falls by the amount spent on research and programmes — a real, visible trade-off.

**URB-120 — Upkeep.** *Provisional (REQ-253).* Two B-05 buildings have a recurring cost of their own:

| Building | Upkeep | Charged | If unpaid |
|---|---:|---|---|
| Research institute | 2 crowns/turn | P3.7 (B-04 ECN-152) | the institute produces **no RP** this turn (`LAB_IDLE`) |
| Civic centre | 1 crown/turn | P3.7 | its housing is **not counted for population growth** next turn (`CIVIC_UNFUNDED`); existing people are not evicted |

Production facilities have **no** separate upkeep: their B-04 maintenance (1 or 2 crowns per batch) is the recurring cost, and a facility whose maintenance is unpaid is `UNMAINTAINED` and cannot run (ECN-147). Warehouses are passive and cost nothing to keep. Upkeep is charged in the published order **research institutes first, then civic centres**, after production and food, under B-04's austerity rule (ECN-105 item 7). Unpaid upkeep is cancelled, never carried as debt (ECN-106).

**URB-121 — Demolition accounting.** *Provisional.* Demolition removes the asset's full book value, writes `ASSET_RETIRED` with the removed value, and credits `floor(crown_cost_paid × 2,500 / 10,000)` as a `REFUND`. The difference between the book value removed and the refund is an **impairment**: national wealth falls by it. Materials are never returned. The loss is reported on its own line, so a player can see that demolition is not free.

**URB-122 — The ledger event types B-05 adds.** *Provisional (REQ-254).* These are declared in addition to B-04 §16's list; each has a unique event key, the action ID and the resulting balance:

| Event | When | Delta |
|---|---|---|
| `CITY_FOUNDED` | P4.1a | crowns −cost, steel −20, fixed assets +book |
| `INFRASTRUCTURE_UPGRADED` | P4.1c | crowns −cost, fixed assets +cost |
| `BUILDING_COMPLETED` | P4.1c | crowns −cost, materials −qty, fixed assets +book |
| `BUILDING_UPKEEP` | P3.7 | crowns −upkeep |
| `LAB_IDLE` / `CIVIC_UNFUNDED` | P3.7 | none (a state change with a reason) |
| `DEMOLITION_REFUND` | P4.1b | crowns +refund; fixed assets −book; impairment recorded |
| `RESEARCH_STARTED` | acceptance | crowns −cost (investment) |
| `RESEARCH_PROGRESS` | P4.2 | RP +generated, project +progress |
| `RESEARCH_COMPLETED` | P4.2 | project closed; technology recorded |
| `RESEARCH_ABANDONED` | cancellation | none (the cost is already spent) |
| `PROGRAMME_COMMISSIONED` | P4.1d | crowns −cost, materials −qty, RP −cost |
| `CAPACITY_CHECK` | P4.1 close | none (audit line: used, capacity, per-city) |

**URB-123 — The reconciliation identity.** *Provisional (REQ-255).* For every nation-turn:

```
closing_treasury = opening_treasury
                 + tax_income − operating_expenses
                 − construction_capex − research_investment − programme_investment
                 + demolition_refunds
                 + trade_and_transfer_flows
```

and, on the fixed-asset ledger: `closing_fixed_assets = opening + construction_book_value − retired_book_value`. Both identities must hold to the crown; a mismatch sets the turn `INTERRUPTED` (B-04 ECN-116). B-05 adds no term that B-04's ledger cannot already express.

---

## 18. Population, housing and the civic contract

**URB-124 — Housing is a hard cap on growth, not on people.** *Provisional (REQ-256).* National housing is the sum of URB-042 over all cities. **Prompt 06 must not grow population above national housing.** If population is already above housing — because a civic centre's upkeep went unpaid, or because a future rule removed housing — the excess is **not** evicted: Prompt 06 applies its own crowding or decline rule, and B-05 supplies only the number. This is the division of ownership: B-05 owns the capacity, Prompt 06 owns the people.

**URB-125 — What B-05 supplies to Prompt 06.** *Provisional.* `housing_capacity(city)`, `housing_capacity(nation)`, the `civic_centres(city)` count, and the `CIVIC_UNFUNDED` flag for the turn. Nothing else. B-05 does not supply a growth rate, a death rate, a migration rule, a disease rate or a stability value.

**URB-126 — What Prompt 06 may not do.** *Provisional.* Prompt 06 may not add a second housing source, change the housing formula, grow population past housing without a published crowding rule, or make a civic centre produce anything other than housing. If it needs a hospital, a police station or a commerce building, it must ask for a new building through a decision and a register row; it may not reinterpret the civic centre.

**URB-127 — Housing is not a resource and is never traded.** *Provisional.* Housing is a derived capacity, like DC and GU. It has no warehouse space, no ledger balance and no price. A city cannot "sell housing" or transfer people.

---

## 19. Balance and progression

**URB-128 — The intended shape of a nation's life.** *Provisional.* A nation passes through four loose phases. They are descriptive, not enforced; no rule checks a phase.

| Phase | Rough state | The decision that matters |
|---|---|---|
| **Settlement** | 1 city, 15 DC, 9 granted facilities, 1,500 crowns | Build a research institute or a fourth farm; keep food above demand |
| **Specialisation** | 2–5 cities, 20–40 DC each, first technologies | Which two or three chains to concentrate on; whether to power with coal or oil |
| **Industrialisation** | 5–9 cities, 40–55 DC, nuclear and programmes | Whether to pay for nuclear, which programme first, whether to export manufactures |
| **Maturity** | 10–12 cities, 55–60 DC, tree complete | Which chains to leave short; how much warehouse to hold; how to convert capacity into trade |

**URB-129 — Affordability at the start.** *Provisional.* With 1,500 crowns and 20 steel, a new nation can afford exactly one of: a research institute (500 + 20 steel, 3 DC); a refinery (320 + 15 steel, 2 DC) plus a farm (120 + 5 steel, 1 DC); a warehouse expansion (180 + 5 steel, 1 DC) plus two farms; or a second coal plant (280 + 10 steel) plus a farm. It cannot afford a steel mill plus its inputs, a new city, or a nuclear plant. The starting choice is therefore real and legible, and no option is a trap: each is a different route into the first thirty turns.

**URB-130 — Cost of a developed city.** *Provisional.* Taking one city from 50 to 500 infrastructure costs **15,750 crowns** before discounts, plus the facilities built in it. A representative mid-game city (8 extraction facilities, 8 processing, 4 generator levels, 2 laboratories, 1 civic centre and 1 warehouse) costs `15,750 + 1,440 + 2,960 + 1,240 + 1,000 + 300 + 220 = 22,910` crowns in construction. Against a mid-game income of several hundred crowns per turn, that is tens of turns of investment — which is the intended horizon.

**URB-131 — Research is worth roughly one extra building per branch.** *Provisional.* `tech_agri_rotation` costs 160 crowns + 24 RP and adds 1 food per farm batch. With four farms that is 4 food/turn for 160 crowns — cheaper per unit than a fifth farm (120 crowns for 20 food, but 1 DC). The comparison is deliberately close: research is a **capacity-free** way to raise output, and its real cost is the RP that could have funded the next technology. Prompt 14 must measure this trade-off, not assume it.

**URB-132 — Anti-snowball measures.** *Provisional.* (1) City count is bounded at 12, so a large nation cannot convert age into an unbounded city lead. (2) Research is one project at a time, so a rich nation cannot buy the whole tree at once. (3) Per-city facility limits mean a mature nation's marginal city is worth less than its first. (4) Maintenance and upkeep recur, so idle capacity bleeds crowns. (5) Research and programme costs are **not** capitalised, so they reduce national wealth. (6) No building, technology or programme grants a percentage that compounds with another. None of this is a claim that the numbers are balanced; it is a statement of the mechanisms that keep a lead from compounding without limit.

**URB-133 — The balance questions Prompt 14 must answer.** *Provisional.* At minimum:

1. Does a new nation have a viable build in its first three turns, and is any starting choice strictly dominated?
2. Is the second city reachable in a reasonable number of turns, and does the national-infrastructure gate bind before the crown cost?
3. Does any single chain dominate the others in crowns per DC per turn at reference prices, before and after research?
4. Is `tech_ext_deep` (+1 uranium on a base of 1) so strong that it must be reduced or the uranium sink enlarged?
5. Does nuclear power pay back within a reasonable horizon against coal and oil, including the technology cost?
6. Do the four programmes arrive late enough to feel earned and early enough to matter?
7. Does the 12-city cap bind before or after the per-city limits, and is the resulting endgame varied?
8. Is one research institute per city the right rate, or does research stall for a nation that spends its DC on production?
9. Does warehouse expansion keep pace with production, or does `SPACE_BLOCKED` dominate the mid-game?
10. Does the housing formula make population growth a city decision rather than a formula outcome?
11. Does whole-batch derating create an unacceptable cliff — one missing GU idling an entire capacity-1 chain — at the published 6 GU and 20 GU generator sizes, and does the player see it early enough to fix it?

**URB-134 — What is not claimed.** *Provisional.* B-05 does **not** claim that its numbers are balanced. It claims that they are internally consistent, expressed in integers, traceable to a register, and accompanied by the questions above. Every coefficient is provisional.

---

## 20. Worked numerical examples

Twenty examples cover the required cases. Every number is recomputed by `qa_backups/verify_city_numbers.py` from the constants in the [formula register](11_city_infrastructure_production_and_research_formula_register.md); if this section and the register disagree, the register wins.

### Example 1 — The standard capital

**Inputs.** Standard start (D-063) at the moment of founding, before any settlement: 1,500 crowns, 50,000 people, a capital at infrastructure **50**, no research, no programmes.

**Capacity.** `10 + floor(50/10) = 15 DC`. Granted facilities: 3 farms (3 DC) + 2 coal mines (2) + 1 oil well (1) + 1 iron mine (1) + 1 refinery (2) + 1 coal plant (2) = **11 DC**. Free: **4 DC**.

**Housing.** `45,000 + 100×50 + 0 = 50,000` — exactly the starting population.

**Book value.** The nine facilities are granted, so `fixed_asset_book_value = 0`. National wealth = `1,500 + 600 inventory + 0 = 2,100`, matching B-04 Example 1.

**Capacity vector.** Food 3, coal 2, oil 1, iron 1, bauxite 0, lead 0, uranium 0; refining 1, steel 0, aluminum 0, ammunition 0; coal generators 1 level.

### Example 2 — Founding the second city

**Inputs.** Capital at infrastructure 100 (Example 3), treasury 1,529, steel 20, one city. National infrastructure = **100**, which meets `100 × (2 − 1) = 100`.

**Cost.** `city_cost(2) = 400 + 150×2² = 1,000` crowns + **20 steel**. Book value = `1,000 + 20×7 = 1,140`.

**Result.** Treasury `1,529 − 1,000 = 529`; steel `20 − 20 = 0`; fixed assets `+1,140`; city count 2; national housing `55,000 + 46,000 = 101,000` (the capital now houses 55,000); national infrastructure still 100. The new city has `infrastructure 10`, `capacity 11`, `housing 46,000`, no facilities.

**Third city.** Requires national infrastructure ≥ 200 and costs `400 + 150×3² = 1,750` crowns + 20 steel.

### Example 3 — Infrastructure 50 → 100

**Inputs.** Capital at 50; opening treasury **1,529** (B-04 Example 2's closing balance, one settlement after founding — Example 1 above shows the founding balance of 1,500); no Civil Survey. The order is 50 levels, bought as five 10-level steps.

| Step | Unit cost | Cost |
|---|---:|---:|
| 50 → 60 | `8 + floor(50/10) = 13` | 130 |
| 60 → 70 | 14 | 140 |
| 70 → 80 | 15 | 150 |
| 80 → 90 | 16 | 160 |
| 90 → 100 | 17 | 170 |
| **Total** | | **750** |

**With Civil Survey** (`−10%`): `ceil(750 × 9,000 / 10,000) = 675`.

**Result.** Treasury `1,529 − 750 = 779`. Capacity `10 + 10 = 20`. Housing `45,000 + 10,000 = 55,000`. Book value `+750`.

### Example 4 — Capacity before and after the upgrade

**Before.** Capacity 15, used 11, free 4.

**After Example 3.** Capacity 20, used 11, free **9**. The player may now add, for example, a 3-DC research institute and a 2-DC steel mill, with 4 DC left. The upgrade did not add a facility by itself; it added the **room** for one.

### Example 5 — Building a fourth farm

**Inputs.** City capacity 15, used 11, free 4; treasury 779; steel 20.

**Cost.** Farm `120 crowns + 5 steel`. Book value `120 + 5×7 = 155`. DC 1.

**Result.** Treasury 659; steel 15; used 12, free 3; food capacity 3 → **4**; fixed assets `+155`. With Civil Methods (`−10%` crowns only): `ceil(120 × 9,000/10,000) = 108` crowns, book `108 + 35 = 143`; steel unchanged.

### Example 6 — Food production for one turn

**Inputs.** Four farms; population 50,000; opening food 120; no bonus; unreserved crowns ample.

**Production.** Each batch yields 20 for 12 crowns: `4 × 20 = 80` food, variable cost `4 × 12 = 48`, maintenance `4 × 1 = 4`. Total cost **52**.

**Consumption.** Demand `ceil(50,000/1,000) = 50`.

**Result.** Food `120 + 80 − 50 = 150`. The chain's contribution to net operating income is `80×1 − 52 = +28` at the reference price.

### Example 7 — Coal extraction and its upkeep

**Inputs.** Three coal mines; one coal plant; opening coal 60.

**Production.** `3 × 10 = 30` coal, variable `3 × 10 = 30`, maintenance `3 × 1 = 3`.

**Power.** One coal plant burns 6 coal and 10 crowns for 6 GU; maintenance 2.

**Result.** Coal `60 + 30 − 6 = 84`. The mines' own margin is `30×1 − 30 − 3 = −3`: **coal is not a cash crop**, it is fuel and a steel input. This is intentional (B-04 register §5) and is the first lesson the economy teaches.

### Example 8 — A facility that does not fit

**Inputs.** A city with capacity 20, used 19, free 1; treasury 1,000; steel 20.

**Attempt A — refinery (2 DC, 320 crowns + 15 steel).** `19 + 2 = 21 > 20` → **rejected at submission** (`F5`). Nothing is reserved, the construction slot is not claimed, and the treasury is unchanged.

**Attempt B — farm (1 DC, 120 crowns + 5 steel).** `19 + 1 = 20 ≤ 20` → **accepted**. The cost is reserved, not charged. The three balances are the point of the example:

| State | Treasury total | Treasury reserved | Treasury available | Steel total | Steel reserved | Steel available | DC used | DC claimed | DC free |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Before acceptance | 1,000 | 0 | 1,000 | 20 | 0 | 20 | 19 | 0 | 1 |
| After acceptance (turn OPEN) | **1,000** | **120** | **880** | **20** | **5** | **15** | 19 | 1 | **0** |
| After resolution (P4.1) | **880** | **0** | **880** | **15** | **0** | **15** | **20** | 0 | 0 |

At acceptance the total is untouched and only `available` falls. The construction slot is claimed and `RESERVATION_HELD` (120 crowns, 5 steel) is written. At P4.1 the farm resolves: `BUILDING_COMPLETED` charges `−120` crowns and `−5` steel, adds fixed assets `155` (120 + 5 × 7) and closes both reservation rows in the same transaction. A cancellation before `LOCKED`, or a failure at P4.1, would release 120/5 and leave the totals at 1,000/20 (URB-068/069).

**Attempt C — second farm.** `20 + 1 = 21 > 20` → rejected. The player must upgrade infrastructure (+1 DC per 10 levels) or demolish something (Example 17).

### Example 9 — Refining through a facility

**Inputs.** One refinery (book value 425) and one coal plant (350); oil 30; gasoline 20; coal 60; treasury 1,529.

**Power.** Supply 6 GU; demand `1 × 2 = 2 GU`; `power_pct = 100`.

**Processing.** `10 oil → 8 gasoline`; variable 20; maintenance 2. **Generator.** Burns 6 coal and 10 crowns; maintenance 2.

**Result.** Oil 20; gasoline 28; coal 54; treasury `1,529 − 20 − 10 − 2 − 2 = 1,495` (before tax and the other chains). The batch's base margin is `8×6 − 10×2 − 20 − 2 = +6` (B-04 register §5); at 6 crowns per GU fully loaded it is `6 − 6 = 0`, which is why refining is a volume business, not an arbitrage.

### Example 10 — Steel through a facility

**Inputs.** Example 9 plus a steel mill (380 crowns + 15 steel, book 485). Iron 30; coal 54; steel 20.

**Power.** Demand `2 + 3 = 5 GU` ≤ 6 → 100%.

**Processing.** `10 iron + 6 coal → 8 steel`; variable 24; maintenance 2. The generator burns 6 coal, 10 crowns.

**Result.** Iron 20; coal `54 − 6 − 6 = 42`; steel 28; treasury `1,495 − 24 − 2 − 10 − 2 = 1,457`. Base margin `8×7 − (10×1 + 6×1) − 24 − 2 = +14`; fully loaded at 3 GU × 3 = `+5`.

### Example 11 — Aluminum and the power cliff

**Inputs.** Example 10 plus an aluminum smelter (420 crowns + 20 steel, book 560), requiring `tech_ind_chem`. Bauxite 24.

**Attempt A — one coal plant.** Demand `2 + 3 + 4 = 9 GU`; supply 6; `power_pct = floor(100×6/9) = 66`. Every chain has capacity 1, so `batches_available = floor(1 × 66 / 100) = 0`: **nothing runs**. No inputs, no money and no fuel are consumed by the processing chains; the generator still burns its 6 coal and 10 crowns for 6 GU that nothing uses. The result is deterministic and is **not** proportional output: the same 66% with capacity 2 would run `floor(2 × 66 / 100) = 1` batch at full recipe, producing 8 units, not 13.2. A reserved manual order does not change the percentage: it is already one of the planned batches in the demand, and here `batches_available` is 0, so the order fails atomically with all reservations released (ECN-062/063).

**Attempt B — a second coal plant** (280 crowns + 10 steel, 2 DC, book 350). Supply `6 + 6 = 12` ≥ 9 → 100%. Each chain runs one batch: gasoline 8, steel 8, aluminum 8; processing cost `20 + 24 + 24 = 68`; two generators burn 12 coal and 20 crowns.

**Manual orders do not change the denominator.** A manual batch occupies one of the planned slots rather than adding a batch (B-04 Example 12). Capacity 2 with two accepted manual batches plans **2** batches and draws 4 GU for refining, not 4 batches and 8 GU; capacity 3 with one manual batch plans 3 (1 manual + 2 automatic), not 4. The percentage is therefore measured against the work the chain can actually do, so a player cannot create a power shortfall — or extra demand — by issuing an order that merely fills capacity.

**Lesson.** The third processing chain is where a single coal plant stops paying. The 2 DC and ~350 crowns for the second plant are part of the aluminum decision, not an afterthought.

### Example 12 — Ammunition through a facility

**Inputs.** Ammunition plant (360 crowns + 15 steel, book 465), requiring `tech_ind_heat`; **treasury 1,000**; lead 20; coal 42; power ample.

**Processing.** `8 lead + 4 coal → 10 ammunition`; variable 20; maintenance 2; draw 2 GU. Base margin `10×6 − (8×3 + 4×1) − 20 − 2 = +10`; fully loaded `+4` at 2 GU.

**Result.** Lead 12; coal 38; ammunition 10; treasury **978** (`1,000 − 20 − 2`). The batch is affordable, so it runs whole: no partial consumption and no debt.

**If it were not affordable.** With `treasury 21` the batch would be refused before consuming anything: `available 21 < 22`, so lead stays 20, coal stays 42, ammunition stays 10 and no variable cost is charged. Maintenance is still owed because the plant stands (ECN-051); if the remaining crown cannot cover it the obligation is cancelled and the capacity idles (`MAINTENANCE_UNPAID`, ECN-106/147), never borrowed. There is no state in which this example produces a negative total: Prompt 04's floor is zero (ECN-102, D-050), and B-05 adds no debt.

**With research.** With `tech_ind_ordnance` and no other ammunition bonus, the same batch yields **11** ammunition (URB-080), not 10 and not 12: the bonus is an integer added per batch, applied once.

### Example 13 — Insufficient inputs, money and prerequisites

**A — materials.** A steel mill costs 380 crowns + **15 steel**; the nation holds 10 steel. Submission is `REJECTED` (`F5`); nothing is reserved.

**B — crowns.** The same nation holds 300 crowns. Submission is `REJECTED` for crowns even if the steel were present. A partial payment is impossible.

**C — production.** A steel batch needs 10 iron and 6 coal; the nation has 9 iron and 40 coal. The batch does **not** run: the 9 iron and the 6 coal are **not** consumed, and the 24 crowns are not charged (B-04 ECN-068). One missing input blocks the whole batch; there is no partial consumption.

**D — prerequisite.** An aluminum smelter without `tech_ind_chem`, or a nuclear plant without `tech_nuclear_engineering`, is rejected before any cost is computed. The message names the missing technology.

### Example 14 — Cancellation, retry and duplicate settlement

**A — cancellation.** A refinery order (320 crowns, 15 steel) is accepted at turn 40. Before `LOCKED` the player cancels: both reservations are released, the construction slot is freed, `CANCELLED` is written. No fee is charged and the balances are exactly as before submission.

**B — retry with the same key.** The player resubmits with the same idempotency key and the same payload after a dropped response: the server returns the original `action_id` and result and creates nothing new. A different payload under the same key is `F9` (B-04 ECN-141).

**C — duplicate settlement.** Turn 40 resolves the order: `BUILDING_COMPLETED`, 320 crowns and 15 steel charged, 425 book value added. A second scheduler invocation for turn 40 reads the completed settlement and rewrites nothing: the event key `(40, nation, 'P4.1', action_id, 1)` already exists (URB-070). The refinery appears once and the treasury is charged once.

### Example 15 — Research from zero to the first technology

**Inputs.** Treasury 1,500; steel 20; capital capacity 15, used 11, free 4.

**Build.** Research institute: 500 crowns + 20 steel, **3 DC**, book value `500 + 140 = 640`. Capacity used 14, free 1. Upkeep 2 crowns/turn.

**Start.** `tech_agri_rotation` costs **160 crowns + 24 RP**. The crowns are charged at acceptance; the project starts at `progress = 0`.

**Progress.** With one institute, 1 RP/turn:

| Turn | RP generated | Progress | Treasury effect |
|---|---:|---:|---|
| 1 | 1 | 1 | 160 crowns already paid; upkeep 2 |
| 2 | 1 | 2 | upkeep 2 |
| 3 | 1 | 3 | upkeep 2 |
| … | … | … | … |
| 24 | 1 | **24 → complete** | upkeep 2 |

A second institute (another 500 + 20 steel, 3 DC) halves this to twelve turns, at the cost of 3 DC that could have been a refinery. The technology is active on turn 25 and adds +1 food to every farm batch thereafter.

**B — overflow at completion.** Three institutes (3 RP/turn) and `tech_agri_rotation` at **22/24**, pool 0. At P4.2: `need = 2`, `rp_generated = 3`, `rp_applied = min(3, 2) = 2`, `progress = 24` → complete, and `rp_pool += 3 − 2 = 1`. The extra point is **not** discarded and **not** added to progress as well: 3 generated = 2 to the project + 1 to the pool. At the next boundary, with no active project, all 3 new points bank and the pool is 4.

**C — a programme funded from the pool while a technology runs.** The nation has `tech_agri_mechanisation` (44 RP) at **progress 10**, five institutes (5 RP/turn), and a pool of **100** banked earlier by running without a project. It commissions `prg_granary` (100 RP, 900 crowns, 100 steel, 50 aluminum).

| Step | Pool total | Pool reserved | Pool available | Project progress |
|---|---:|---:|---:|---:|
| Before commissioning | 100 | 0 | 100 | 10 / 44 |
| `COMMISSION_PROGRAMME` accepted | 100 | 100 | **0** | 10 / 44 |
| P4.1d — programme resolves | **0** | 0 | 0 | 10 / 44 |
| P4.2 — 5 RP generated | 0 | 0 | 0 | **15 / 44** |

Spending 100 banked points did **not** reduce the 10 already in the project, and the 5 generated at P4.2 went to the project, not to the programme: the two accounts are disjoint. Six turns later `need = 4` against 5 generated, so 4 complete the technology and **1 banks** — the same overflow rule as B. Over the seven turns the arithmetic reconciles: `100 banked + 35 generated = 135 = 100 programme + 34 progress + 1 pool`.

### Example 16 — A modifier is applied once

**Inputs.** Four farms; `tech_agri_rotation` (+1), `tech_agri_mechanisation` (+1), `prg_granary` (+1).

**Output.** `4 × (20 + 1 + 1 + 1) = 4 × 23 = 92` food. The bonuses are **added**, not multiplied: `20 × 1.1 × 1.1 × 1.1 ≈ 26.6` is not a valid calculation here, and no round-off occurs because every term is an integer.

**Cap check.** Food's cap is +3 (URB-100): 20 + 3 = 23. A future fourth food bonus would be rejected at design time, not silently capped at runtime.

**One chain only.** The +1 applies to farm batches, not to food bought, food received in aid, or food produced by any other source. There is no other food source at launch.

### Example 17 — Demolition, refund and the capacity it frees

**A — a purchased farm.** Crown cost paid 120; book value 155; city used 12. Demolition: refund `floor(120 × 2,500/10,000) = 30`; book value removed 155; impairment `155 − 30 = 125`; capacity used 12 → 11 at the **next** turn. Net wealth effect: `+30 − 155 = −125`. Materials are not returned.

**B — a granted starting farm.** Crown cost paid **0**; book value 0. Demolition refunds **0**, removes **0** book value, and frees 1 DC. The starting grant cannot be converted into crowns.

**C — cycling check.** Build a farm for 120, demolish for 30, rebuild for 120: net cost 210 crowns for the same facility. Cycling is a loss, so no refund loop exists.

### Example 18 — Power shortfall with four refineries

**Inputs.** Four refineries (capacity 4), one coal plant (6 GU). Oil ample; coal 60; treasury ample.

**Demand.** `4 × 2 = 8 GU`; supply 6; `power_pct = floor(100 × 6/8) = 75`.

**Batches.** `floor(4 × 75/100) = 3`. The fourth batch does not run; it consumes no oil, no 20 crowns and no maintenance beyond the fixed 2 per batch (total maintenance 8, paid whether or not the batch runs).

**Result.** 3 batches: 30 oil → 24 gasoline, 60 crowns variable, 6 GU used, 0 surplus. The digest reports `power_pct 75`, one batch lost to derating, and the reason. The player's fix is a second generator level, not a reroll.

### Example 19 — Treasury and wealth reconciliation for a construction

**Inputs.** Opening treasury 1,529; steel 20 (book 140); fixed assets 0; no other flows.

**Order.** One refinery: 320 crowns + 15 steel. Book value `320 + 105 = 425`.

**Result.** Treasury `1,529 − 320 = 1,209`; steel `20 − 15 = 5` (book 35); fixed assets 425.

**Wealth.** Opening `1,529 + 140 = 1,669`; closing `1,209 + 35 + 425 = 1,669`. Construction converts liquid assets into a fixed asset and changes **no** wealth. With Civil Methods (`−10%` crowns): cost 288, book `288 + 105 = 393`, treasury 1,241, wealth `1,241 + 35 + 393 = 1,669`.

**Ledger.** `RESERVATION_HELD` (320, 15 steel) at acceptance; `BUILDING_COMPLETED` at P4.1 with `crowns −320`, `steel −15`, `fixed_assets +425`, `book_value_after 425`; the reservation rows close in the same transaction.

### Example 20 — A research completion cannot happen twice

**Inputs.** One institute; `tech_agri_rotation` at progress 23/24; turn 41.

**P4.2.** `progress = min(24, 23 + 1) = 24` → complete. `RESEARCH_COMPLETED` records the technology, the completion turn 41 and the effect pending for turn 42. The RP pool is unchanged (the point was consumed by the project), and the farm yield is **still 20** during turn 41: the effect applies from turn 42.

**Resume.** The settlement is interrupted after P4.2 and retried. The retry reads the completed project and writes nothing; it does not add a second technology, does not re-award the effect and does not re-deduct points. The event key `(41, nation, 'P4.2', tech_agri_rotation, 1)` is already present.

**Turn 42.** Farms yield 21 per batch. Only now does the change appear in production. A player who checks the report sees the completion at 41 and the effect at 42, with both lines labelled.

---

## 21. Fairness, security and anti-exploit requirements

**URB-135 — The server owns every number.** *Provisional (REQ-257).* Cost, capacity, housing, output, upkeep, refund and progress are computed on the server from the frozen state. A client may display a projection, but a client-supplied cost, capacity, output or technology flag is ignored and the action is re-validated. No B-05 rule is enforced only in the interface.

**URB-136 — Duplicate city founding is impossible.** *Provisional.* Four independent guards: the 12-city bound; the national-infrastructure threshold; one founding per nation per turn; and the idempotency key. A repeat with the same key returns the original city, not a second one; a different key that would exceed the city bound is rejected before any charge.

**URB-137 — Double-spending construction is impossible.** *Provisional.* Crowns and materials are reserved at acceptance (URB-066), re-validated at P4.1 (URB-069), and charged exactly once inside the settlement transaction. A second order cannot see reserved funds as available. A failed resolution releases the reservation and charges nothing.

**URB-138 — Capacity cannot be oversubscribed by orders.** *Provisional.* The construction slot is one per city per turn, so two orders in one city cannot race. The DC check runs at submission and at resolution. Capacity is derived from infrastructure; the only way it falls is `OP-05` damage, which produces the declared overdraw state (URB-051a) and never makes an already-accepted order look like a second order. New orders are blocked while overdrawn.

**URB-139 — Production and research cannot be double-collected.** *Provisional.* Production is B-04's exactly-once settlement (ECN-155). Research adds `RESEARCH_COMPLETED` under a deterministic key; a resumed settlement reads the stored completion. A completed technology cannot be started again (URB-096).

**URB-140 — Refund cycling is a loss.** *Provisional.* The demolition refund is 25% of crowns paid, materials are never returned, and the full book value is removed. The granted starting facilities have a crown cost of 0 and refund 0. No sequence of build, demolish and rebuild produces a profit or recovers materials (Example 17).

**URB-141 — No voluntary infrastructure or city reduction exists to exploit.** *Provisional.* There is no sell-infrastructure, no delete-city, no transfer-city and no abandon-city action. The only reduction paths are the bounded `OP-05` infrastructure damage of URB-157, a reroll (which destroys everything and grants the standard bundle once) or an audited administrative correction. This removes an entire class of duplication and refund exploits by construction rather than by surveillance: war damage returns no crowns, no materials and no capacity to spend, so it cannot be cycled for value.

**URB-142 — A reroll is a total loss.** *Provisional.* The reroll destroys every city, level, facility, project, point, technology and programme, and the replacement receives the standard bundle and the nine granted facilities **once**. It cannot inherit a fixed asset, a research discount, a programme or a city count. The starting grant cannot be claimed twice by cancelling a creation partway: the bundle is written in the same transaction that creates the nation (B-03).

**URB-143 — Administrative corrections are reversals.** *Provisional.* Prompt 12 may remove or restore a facility only by an `ADJUSTMENT`/`REVERSAL` event that references the original and states the case. No operator may edit `capacity`, `housing` or `fixed_asset_book_value` directly, and no correction may create a facility without its construction cost or a technology without its research cost (except an explicitly recorded restitution).

**URB-144 — Name and text safety.** *Provisional.* City names are length-bounded, NFC-normalised, folded for uniqueness and stripped of control characters and angle brackets (URB-030). They are rendered as text, never as HTML. A rename cooldown prevents log spam. No city name is ever used as an identifier.

**URB-145 — The audit trail is complete.** *Provisional.* Every B-05 action writes its submission, acceptance, resolution or failure, its reservations, its ledger events, its cost breakdown and its resulting capacity and book value. The `CAPACITY_CHECK` audit line records `used` and `capacity` per city per turn, which is the evidence a later investigation needs.

---

## 22. Interface requirements for Prompt 13

**URB-146 — The city list must answer four questions.** *Provisional (REQ-207).* For each city: its name and capital flag; its infrastructure; `used / total` capacity; and its housing versus the nation's population share. The list must show which cities are at their capacity limit and which have free DC.

**URB-147 — The city detail must show, before commitment.** *Provisional.* Current infrastructure and the next 10-level step's cost and DC gain; the facility list by chain with each facility's DC, book value and (for production) its B-04 output and cost at the reference price; free DC and every per-city limit's remaining count; and the projected `used / total` after a proposed order.

**URB-148 — Construction preview.** *Provisional.* Before a player commits, the interface shows: crown and material cost after every applicable discount; the DC and limit check; the construction slot; the turn the asset becomes available; the book value added; the effect on national wealth; and, for a generator, the projected supply, demand and surplus.

**URB-149 — Production view.** *Provisional.* Per chain: batches, inputs at current stock, expected output, variable cost, maintenance, power draw, the blocking reason if any, and the applied research bonus as a separate line. This restates B-04's digest requirements in the city context; it does not redefine them.

**URB-150 — Research view.** *Provisional.* The tree by branch with each technology's cost in RP and crowns, prerequisites, effect, status (locked / available / in progress / complete), current progress and turns at the current institute count; the RP pool and generation rate; and the programme's availability and cost once its branch is complete. A completed technology is shown with its completion turn and its effect, never as "available".

**URB-151 — Warnings have one meaning each.** *Provisional.* `CAPACITY_FULL`, `LIMIT_REACHED`, `MATERIAL_SHORT`, `CROWNS_SHORT`, `NO_SLOT`, `NO_INSTITUTE`, `PREREQUISITE_MISSING`, `POWER_SHORT`, `SPACE_BLOCKED` and `UPKEEP_UNPAID` each mean exactly one thing and link to the rule that causes them. Prompt 13 may style them; it may not rename or merge them.

**URB-152 — No projection is a promise.** *Provisional.* Every projected number is labelled as a projection computed from the current state and the published formulas. A projection that depends on a future boundary (next turn's output, next turn's cost) must say so. No screen may present a projection as a completed balance.

---

## 23. Cross-system contracts for later prompts

**URB-153 — Prompt 06 (population and domestic politics).** *Provisional.* Prompt 06 receives `housing_capacity` per city and nation, the `civic_centres` count and the `CIVIC_UNFUNDED` flag. It **must not** grow population above national housing, add a second housing source, change the housing formula, or reinterpret the civic centre as a health, order or commerce building. It owns growth, decline, migration, disease, crime, stability, tax policy and legitimacy. It may add a new building only through a decision and a register row.

**URB-154 — Prompt 07 (trade and markets).** *Provisional.* Facilities produce into the national inventory; Prompt 07 may sell or buy any of the eleven resources under B-04's reservation and ledger rules. A trade cannot add capacity, bypass a per-city limit, deliver a building or transfer research points. Warehouse space is checked on the buyer before a trade settles (B-04 ECN-124); B-05's expansion is the only way to raise it besides the Granary programme.

**URB-155 — Prompt 08 (diplomacy).** *Provisional.* A sanction may freeze a construction or research action (the action fails with a reference to the sanction) but may not delete a city, a building, a technology or a programme already owned, and may not create a negative balance. Aid and reparations move crowns and resources, never capacity, DC, housing or research points. An embargo does not destroy goods.

**URB-156 — Prompt 09 (alliances).** *Provisional.* An alliance may coordinate builds, share intelligence or pool resources through transfers, but it may not hold cities, own facilities, grant DC or housing, research for a member, or transfer a technology or programme. If Prompt 09 wants a shared construction project, it must define a new mechanism, an ownership rule and an audit trail; B-05 does not provide one. An alliance pool may not be used by a restricted pair (D-035).

**URB-157 — Prompt 10 (warfare).** *Provisional (revised 2026-11-04).* Prompt 10 consumes ammunition, gasoline, steel, aluminum and Food under B-04's reservation and ledger rules. It may add a **Military** research branch and military buildings through a decision and register rows; it may not change a B-05 facility's output, a recipe, DC costs or per-city limits.

One warfare effect on B-05 is **adopted** and bounded: `OP-05 MISSILE_STRIKE` may target a B-05 `city_id` and reduce that city's **infrastructure level**. The authoritative rules are B-10 `WAR-109a`–`WAR-109m` and formulas `F-WR-037`/`F-WR-038`; B-05 owns the state and the recalculation:

1. **Target.** The city must exist and belong to the target nation. A city is an asset identifier, never a location; the rule creates no map, coordinate, distance, border, front or movement.
2. **Damage.** `removed = min(ceil(I × 500 / 10,000), 20, campaign_headroom, I − 10)` on `ATTACKER_VICTORY` or `DECISIVE_VICTORY` only. The floor is **10** and the per-city per-campaign cap is **30%** of the campaign-start level.
3. **Recalculation.** `capacity = 10 + floor(I/10)` and `housing = 45,000 + 100 × I + 25,000 × civic_centres` are recomputed immediately (`URB-041`, `URB-042`). A capacity shortfall produces `CAPACITY_OVERDRAWN` (URB-051a). A housing shortfall is **not** a warfare casualty rule: no strike kills, moves or evicts people. The reduced housing is passed to the **next P3.8**, where B-06 `DMP-034` computes population against the current housing input and B-06 `DMP-031` applies the ordinary crowding decline (excess ÷ 10 rounded up, or the natural decline if greater, floor 1,000). Repair restores housing at the same boundary and crowding stops once housing covers the population again.
4. **Facilities are preserved.** Damage never deletes, disables or transfers a facility, never changes a recipe and never reduces a per-city limit. The city keeps every building it had. Facility book value is excluded from impairment.
5. **Book value.** Only the **city infrastructure subledger** is impaired (`URB-118a`, `URB-118b`): `carrying_before = infrastructure_gross_capital − infrastructure_accumulated_impairment`; `impaired = min(carrying_before, floor(carrying_before × removed / I_combat))`; accumulated impairment rises by `impaired` and `fixed_asset_book_value` falls by the same amount (`ECN-108`). Impairment creates no crown and is not an expense. A second strike reads the reduced carrying value, so repeated damage never over-impairs. A repair capitalises a new lot at its B-05 cost and does **not** reverse earlier impairment.
6. **Repair.** A repair order is an ordinary `UPGRADE_INFRASTRUCTURE` at P4.1: `repair_cost = infrastructure_cost(I, n)` (URB-043/044), with **no material component and no second discount**; `1 ≤ n ≤ min(10, 500 − I, unrepaired)`, charged as capex, with `INFRASTRUCTURE_REPAIRED`. P4.1 completes before P5, so the same turn's strike is measured against the repaired level (`I_post_P4_1`, `URB-046`, `WAR-109m`); `I_combat` is that level.
7. **Prohibited.** No city destruction, deletion, capture or ownership transfer; no facility destruction; no direct population casualty, migration or eviction; no territorial or geographic effect. Those remain out of scope and require a separate decision.

Damage to a city or a facility beyond point 3 is **not** in scope. The default position remains that warfare destroys **resources and military units**; infrastructure damage is the single adopted exception, and it is recoverable.

**URB-158 — Prompt 11 (events, objectives, rankings).** *Provisional.* A reward may grant crowns, resources, RP or a one-time programme only through a disclosed, keyed, ledgered event. It may not grant a city, a facility, capacity, a technology or a permanent yield multiplier without a decision and a register row. National wealth (B-04) may be used in a ranking; capacity, housing and research points may be shown as statistics but never as a score that can be bought.

**URB-159 — Prompt 12 (fair play and administration).** *Provisional.* Prompt 12 may read every B-05 action, ledger event, capacity check and book-value change. A correction is an `ADJUSTMENT`/`REVERSAL` with a case reference; no operator may edit a city's capacity, a nation's technology list or the fixed-asset book value in place. Removing a facility for a proven exploit must also remove or reverse the value it created, or the correction is incomplete.

**URB-160 — Prompt 13 (interface and journeys).** *Provisional.* Prompt 13 owns screens, layout, accessibility and notifications. It must show the city list, the capacity split, construction previews, production blocking reasons, research status and upkeep warnings (URB-146…152). It may not redefine a term; a new number needs a B-05 or register definition first.

**URB-161 — Prompt 14 (numerical balance).** *Provisional.* Prompt 14 must validate every B-05 formula and constant, answer the ten questions in URB-133, and either confirm or retune the provisional numbers. It may change a cost, a yield bonus, a research cost, a limit or the 12-city bound with a recorded decision. It may not change the structure — capacity points, one construction slot, one project, four programmes — without a new B-05 revision.

**URB-162 — Prompt 15 (Bible assembly).** *Provisional.* Prompt 15 must incorporate B-05, the research report and the register, resolve any duplicate formula in favour of the register, check both directions of every declared edge, and verify that no later part contradicts URB-001…URB-172. It must not silently rewrite a B-05 rule; a change is a new revision with a decision.

**URB-163 — The subsystem declaration is complete.** *Provisional.* In B-02's fifteen-item subsystem contract, B-05 declares: entities (city, facility, research project, programme); actions (URB-063); prerequisites (URB-065); costs and reservations (URB-066); boundary phase (P3.7 upkeep, P4.1 construction, P4.2 research); ordering (URB-067); effects on other systems (§23); failure and cancellation (URB-068/069); player results (URB-117, §22); visibility (§22); invariants (URB-062/113/123); edge cases (the 20 examples); requirements and decisions (§24/§25); and validation (§26). No item is left to a later prompt without a named owner.

---

## 24. Requirements and test matrix

**URB-164 — Requirements.** *Provisional.* B-05 adds **REQ-188…REQ-257** (70 requirements) to [the traceability register](03_requirements_traceability.md). Every requirement cites a section here, has a verification method and an owning prompt, and is Provisional unless marked otherwise. The full text lives in the register; the grouped list below is the map, not a second copy.

| Group | Requirements | Subject |
|---|---|---|
| City model | REQ-188…197 | Non-geographic city, capital, naming, 12-city bound, founding, cost, new-city state, no deletion, emergent specialisation, reroll |
| Infrastructure | REQ-198…203 | Meaning, capacity formula, housing formula, cost, no reduction, timing |
| Capacity and catalogue | REQ-204…216 | Standard capital, DC costs, limits, double check, closed catalogue, building fields, three facility classes, warehouse, institute, civic centre, invariant |
| Construction | REQ-217…224 | Actions, one slot, validation, P4.1, failure, exactly-once, demolition, national vector |
| Production | REQ-225…234 | National grid, nuclear gate, all resources, output, food, shortages, one facility per chain, national inventory, insufficient input, recipe immutability |
| Research | REQ-235…245 | RP, one project, start, progress, completion, abandonment, timing, modifier caps, 12 technologies, permanence, safe extension |
| Programmes | REQ-246…247 | Capstones, commissioning |
| Settlement and accounting | REQ-248…255 | No queue object, recovery, notification, capex, research expensed, upkeep, events, reconciliation |
| Housing and authority | REQ-256…257 | Housing hard cap, server-owned numbers |

**URB-165 — Test specifications.** *Provisional (REQ-249).* B-05 defines **64 tests** in ten groups. They are specifications, not executed tests.

| Group | IDs | What the group proves |
|---|---|---|
| A — City model | T05-A01…A06 | Capital creation, founding gate, cost, 12-city bound, naming, no deletion |
| B — Infrastructure | T05-B01…B06 | Cost table, discounts, capacity, housing, no reduction, timing |
| C — Capacity | T05-C01…C08 | DC per class, limits, double check, invariant, full city, demolition freeing DC |
| D — Construction | T05-D01…D08 | Validation order, reservation, P4.1, failure release, idempotency, duplicate settlement, cancel |
| E — Production | T05-E01…E08 | Each chain's facility, power derate, shortage, storage block, fuel check |
| F — Research | T05-F01…F08 | RP rate, one project, progress, completion, abandon, effect timing, cap, programme |
| G — Accounting | T05-G01…G06 | Capex/book value, research expensed, upkeep, refund, wealth identity, ledger keys |
| H — Security | T05-H01…H06 | Double founding, double spend, capacity race, grant mining, reroll loss, admin reversal |
| I — Interface | T05-I01…I04 | Preview cost, capacity display, blocking reason, research status |
| J — Continuity | T05-J01…J04 | Research report, register coverage, requirement citations, cross-document agreement |

**URB-166 — The arithmetic checker.** *Provisional.* `qa_backups/verify_city_numbers.py` recomputes every example in §20 and every constant in the register, and fails if this document and the register disagree. It is document QA, not game code: it holds no state and writes nothing.

---

## 25. Decision register — Prompt 05

**URB-167 — Decisions recorded.** *Provisional.* The following project decisions are recorded in [DECISIONS.md](../DECISIONS.md) as **D-066…D-080** and summarised in [the Stage 2 design register](04_approved_and_provisional_decisions.md) as **DD-081…DD-100**. This table is the cross-reference; the log is authoritative.

| ID | Decision | Status |
|---|---|---|
| D-066 | A city is a named, non-geographic development centre holding capacity and housing; no land, map, borders or deposits | Confirmed (design) |
| D-067 | One capital; at most 12 cities; no city deletion or transfer; cities are permanent for the nation's life | Confirmed (design); bound Provisional |
| D-068 | Founding is gated by national infrastructure (`100 × (k−1)`) and a quadratic crown cost plus 20 steel; no real-time cooldown | Confirmed (design); numbers Provisional |
| D-069 | Infrastructure 10–500 per city, integer, cost `n × (8 + floor(I/10))`, **cannot be reduced by the owner**; the only reduction is bounded `OP-05` damage (URB-157) | Confirmed (design); numbers Provisional |
| D-070 | Development capacity `10 + floor(I/10)`, spent by weighted class costs (extraction 1, processing 2, generator 2, warehouse 1, lab 3, civic 2) | Confirmed (design); numbers Provisional |
| D-071 | Per-city limits (8 extraction per resource, 4 processing per chain, 6 generator levels, 6 warehouse, 2 labs, 3 civic) are the specialisation lever | Confirmed (design); numbers Provisional |
| D-072 | Seventeen-type closed catalogue; no commerce, pollution, culture or military buildings at launch; one civic building (housing only) | Confirmed (design) |
| D-073 | One construction-class action per city per turn, one founding and one programme per nation; all resolve at P4.1; assets available next turn | Confirmed (design) |
| D-074 | Demolition refunds 25% of crowns paid, never materials, removes full book value; granted facilities refund 0 | Confirmed (design); percentage Provisional |
| D-075 | Power plants cost DC and crowns; nuclear requires `tech_nuclear_engineering`; B-04's grid, fuel and derating are unchanged | Confirmed (design); numbers Provisional |
| D-076 | Research is produced by institutes (1 RP each per turn), one active project per nation, 12 technologies in 5 branches | Confirmed (design); numbers Provisional |
| D-077 | Modifier classes are integer yield bonuses, cost/maintenance floors, and discounts capped at 20%; no percentage compounding | Confirmed (design) |
| D-078 | Four national programmes, one per research branch, are permanent branch capstones with one named effect each | Confirmed (design) |
| D-079 | Housing `45,000 + 100×I + 25,000×civic` per city is a hard input to Prompt 06, which owns all population rules | Confirmed (design); formula Provisional |
| D-080 | Construction is capex with book value; research and programmes are expensed investments; labs and civic centres have upkeep at P3.7 | Confirmed (design); numbers Provisional |

---

## 26. Validation, acceptance and next action

**URB-168 — Acceptance checklist.** *Provisional.*

| Criterion | Status | Evidence |
|---|---|---|
| P&W city, infrastructure, improvements, production and project research with sources and limitations | **Met (document)** | [Research report](research/05_politics_and_war_city_infrastructure_production_research.md) |
| Original city model that works without a map | **Met (design)** | §6 |
| City creation, expansion and lifecycle complete | **Met (design)** | §6; URB-031…038 |
| Infrastructure levels, costs, scaling and capacity complete | **Met (design)** | §7; URB-039…046 |
| Building types, costs, prerequisites, capacity and outcomes | **Met (design)** | §9; URB-053…062 |
| All seven raw goods have facilities | **Met (design)** | URB-055; §12 |
| All four manufactured goods have facilities using B-04's recipes | **Met (design)** | URB-056; §13 |
| Power/utility decision explicit | **Met (design)** | §11; D-075 |
| Research system and progression defined | **Met (design)** | §14; URB-092…106 |
| Technology costs, effects, prerequisites, stacking and timing | **Met (design)** | URB-100…106 |
| National projects evaluated and decided | **Met (design)** | §15; D-078 |
| Construction, production and research follow the two-hour turn | **Met (design)** | §10, §16; URB-067 |
| Reservations, costs, refunds, upkeep and ledger consistent with B-04 | **Met (design)** | §17; URB-118…123 |
| All formulas have stable IDs and authoritative definitions | **Met (document)** | [Register](11_city_infrastructure_production_and_research_formula_register.md) |
| At least 15 worked examples, independently checked | **Met (document)** | §20, 20 examples; `verify_city_numbers.py` |
| Security and anti-exploit requirements defined | **Met (design)** | §21 |
| Population and domestic-politics dependencies assigned to Prompt 06 | **Met (design)** | §18, URB-153 |
| Corrected formulas agree across rulebook, register, decisions and examples | **Met (document)** | URB-043/044/066/072/095; F-CI-004/005/011/021; D-069; Examples 8, 11, 12, 15; `verify_city_numbers.py` cross-document checks |
| Requirements, decisions and supporting records updated | **Met** | §24, §25; traceability, DECISIONS, progress log |
| Validators executed and recorded | **See URB-169** | Actual run below |
| No implementation, migration or deployment | **Met** | Scope confirmation |

**URB-169 — Validation record.** *Provisional.* Run from `docs/` on 2026-10-25, after the last edit to this document, the register and the continuity files.

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338 checks passed** — `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`**, including the B-05 block: 26 sections, the 11-resource roster, four recipes, 20 examples, complete T05 coverage, every REQ-188…REQ-257 cited, every `F-CI-` cited present in the register, the v1.4 header |
| `python qa_backups/test_decision_registers.py` | **12 tests — OK** (D-001…D-080, UD 19/9/5, Prompt 06 next) |
| `python qa_backups/test_next_action.py` | **15 tests — OK** (no stale next action; outline, progress table and continuity set agree) |
| `python qa_backups/verify_city_numbers.py` | **267/267 arithmetic checks passed** — every register constant and all 20 examples recomputed, plus the v1.5 guards: the stepped bound (16,170), basis-point vocabulary, the three reservation balances, Example 12 affordability, whole-batch derating, both research-allocation flows, F-CI-021's **22/24** Example 15B state, the `M + A ≤ C` capacity cases and cross-document checks against B-04's F-EC-006/ECN-053/ECN-060, D-069 and D-004 |
| `python qa_backups/verify_economy_numbers.py` | **146/146 checks passed** — B-04 is unchanged by this prompt |

Counts were derived from the files, not asserted: **257** requirements (14 approved / 236 provisional / 5 open / 2 deferred), **80** decisions, **100** design positions, **33** UD rows (19 Resolved / 9 Deferred / 5 Open). **Nothing runtime was tested:** no city, building, research project or programme exists, and **0 of the 64 T05 tests** has been executed.

**URB-170 — Limitations.** *Provisional.* (1) No code, schema, scheduler or player exists; no B-05 rule is runtime-tested. (2) Every number is provisional; Prompt 14 must validate or retune it. (3) The 64 test specifications are unexecuted. (4) The research is documentary and P&W may have changed; no logged-in test was performed. (5) The housing and population interaction is a contract; Prompt 06 may add crowding rules that change the player experience. (6) The 12-city bound and the 500-infrastructure cap are operational judgement calls, not measured. (7) The `tech_ext_deep` uranium bonus is flagged as the strongest single technology and must be simulated (URB-133 question 4). (8) Infrastructure may be reduced only by the bounded, recoverable `OP-05` damage of URB-157; there is still no city destruction, city transfer, facility destruction or direct population-casualty rule, and adding one requires a separate decision. (9) The interface requirements are inputs to Prompt 13, not screens. (10) The starting capital's nine granted facilities have zero book value by design; this is an accounting convention, not a claim that they are worthless. (11) The v1.4/v1.5 corrections repaired internal consistency; they did not measure balance, and the 267 assertions are document checks rather than a simulation.

**URB-171 — Next action.** *Provisional.* If the acceptance criteria are met, the next scheduled task is **Stage 2, Prompt 06 — Population and Domestic Politics**. Prompt 06 must consume the housing formula as a hard input (URB-153), must not add a second housing or commerce source, and must not change B-04's tax or food formulas. Prompt 05 is **not** implemented, deployed or runtime-tested.

**URB-172 — Revision history.** v1.0 (2026-10-25): first issue for Prompt 05. No earlier version exists. All numbers are the v1.0 provisional calibration; no value has been tuned or measured. v1.1 (2026-10-25): three internal references corrected during the acceptance audit — two that pointed at URB-124 (the housing rule) when they meant the technology tree and the programme table, and the DD range in URB-167, which stopped at DD-095 although the register now runs to DD-100. v1.2 (2026-10-25): two counting defects and one dangling citation fixed after the tables were counted rather than trusted — the catalogue has **17** types (7 extraction + 4 processing + 3 generator + warehouse + institute + civic), not 18, and the technology tree has **12** technologies, not 11; URB-146's dead `REQ-258` now cites REQ-207. The checker gained seven assertions so either count and the citation cannot silently regress. No cost, coefficient or worked example changed between v1.0 and v1.2. v1.3 (2026-10-25): Example 3 now states its opening treasury of **1,529** (B-04 Example 2's closing balance) instead of leaving it implicit, and Example 1 is marked as the founding balance before any settlement. Two catalogue defects found by counting rather than reading were also fixed: the research institute and civic centre now carry the stable IDs the register already used (`bld_lab`, `bld_civic`), so all **17** types have a `building_id`, and URB-053/D-072's "nineteenth type" now reads "eighteenth". No rule, cost, coefficient or result changed; the arithmetic checker's 150 assertions still pass unchanged, and `validate_final.py` now fails if the catalogue loses an ID or the "nineteenth" ordinal returns. v1.4 (2026-10-25): independent-review reconciliation. URB-043 now states D-069's stepped marginal sum (`Σ (8 + floor(j/10))`): 50→500 is 15,750 and 10→500 is 16,170, and the register's 28,420 bound is gone. URB-044 and URB-072 fix the basis-point vocabulary (1,000 bp is the discount; 9,000 basis points is the remaining multiplier) and restrict launch discounts to one source per cost, so Civil Methods no longer covers infrastructure and nothing stacks. URB-066 separates total, reserved and available. URB-095/096 give research one assignment rule (project or pool, never both) and fund programmes from banked points only. URB-014 cites D-015 and keeps D-004 as superseded history. Example 12 opens at 1,000 and closes at 978 instead of implying a debt; Example 8 shows the three balances; Example 11 states whole-batch derating. No design, cost or coefficient was changed and no assertion was removed: the checker grew from 150 to 219. v1.5 (2026-10-25): micro-correction after a second independent review. F-CI-021's example now states Example 15B's actual **22/24 with 3 RP → applied 2, pool +1** and keeps the 23/24 case only as Example 20's one-point completion. The manual-capacity contract is stated as `planned_batches = M + A ≤ capacity` in URB-074 and in B-04's ECN-053/060 and F-EC-006, ending the reading in which accepted manual batches were added on top of capacity; Example 11 shows why the demand is 4 GU and not 8. No design changed, and the checker now has 267 assertions. v1.6 (2026-11-04): Prompt 10B-C reads the Prompt 10B-C authorization forward into B-05. `OP-05 MISSILE_STRIKE` may now target a city and reduce **infrastructure only**, under B-10 `WAR-109a`–`WAR-109l` and `F-WR-037`/`F-WR-038`: URB-039/040 state the damage path and the absolute floor of 10; URB-045/046 distinguish owner action from war damage and place repair at P4.1 before P5; URB-050/051/051a/062/138 define the `CAPACITY_OVERDRAWN` state; URB-118 records proportional book-value impairment; URB-141/157 state that no city, facility, population or territory may be destroyed or transferred. No construction cost, recipe, DC cost, limit, housing formula or capacity formula changed.

<!-- END -->

