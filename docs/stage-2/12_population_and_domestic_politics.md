# B-06 — Population and domestic politics

**Version:** 2.6 · **Created:** 2026-10-25 · **Revised:** 2026-11-04 (v2.6 Prompt 10B-C2 adds `DMP-031a`: warfare infrastructure damage is a **housing-source change** resolved at the next P3.8 by the existing `DMP-031` crowding rule, with no casualty, eviction, movement or migration rule and no new formula. The v2.5 text follows for history: v2.5 is the consolidation pass: **DMP-184** now makes the post-election banner depend on the **result** — `NORMAL` for a returned incumbent, `TRANSITION` for 12 turns with the 800 bp penalty for a defeat — instead of returning every contest to `NORMAL`, and the maintenance citations move from §8.6 to **ECN-147a**, whose whole-obligation order (extraction → generation → processing) B-04 v1.3 now publishes. The register is unchanged at v2.4. v2.4 is the fourth 06B micro-correction: DMP-188 and DMP-190 fix the ballot and the platform lock at the campaign's own **`registration_close_turn`**, so a delayed campaign opened at 980 closes both at **992**, not at the already-past 988; DMP-184's truncated final sentence is restored as a statement that adds no new rule (the banner returns to `NORMAL`, the term's first digest is published and the next contest date is shown, DMP-178/181a); and E41/E42/DMP-246 recompute Model A from turn 1 — food production 15 a turn means the **first shortage is turn 4** (unmet 20, then 35) — and allocate the last crown by maintenance obligation under ECN-105/ECN-147, which pays the **oil** chain (1), marks the other five chains `UNMAINTAINED` and closes the treasury at **0**, not 1. v2.3 is the third 06B micro-correction: an interrupted campaign now **restores `ELECTORAL`** for its remaining turns when the last blocker clears before its deadline, and restores nothing in a gap between consecutive blockers; every campaign date — registration `+12`, final notice `+22`, deadline `+24` — is derived from `campaign_open_turn`, so a delayed campaign opened at 980 for a contest due at 1000 closes registration at 992, notices at 1002 and resolves at 1004 instead of using `T − 12`/`T − 2`; and the rejected-crisis models are separated into the batch-atomic output multiplier, the whole-batch cap (`floor(3 × 25 / 100) = 0`, 11/turn) and an explicitly labelled proportional illustration. v2.2 was the second 06B micro-correction: the campaign window is computed **once** — a blocking state that begins after it opens delays the resolution to the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)` and never restarts the 24 turns (1000/976/1010 → **1010**, not 1034); and the negative multi-turn counterfactual figures are published as **unconstrained cumulative cash-flow results**, never as treasury balances, because B-04's no-debt and austerity rules (ECN-102…106) cancel an unaffordable obligation rather than producing a negative balance. `SUCCESSION` is now named alongside `NORMAL` and `ELECTORAL` as a resolving state in DMP-235/DMP-236. v2.1 was the first micro-correction: the election-state contradiction is resolved so a due contest resolves in `ELECTORAL` or `NORMAL` and never waits for a state its own preparation displaced; the schedule is anchored on `scheduled_contest_turn + 240 × k` with the new catch-up rule (DMP-181a) and the once-only window rule (DMP-181b) for a return from long dormancy; the rejected batch-cap counterfactual is recomputed with one floor per division (`38/turn`, `+132` at 36 turns, `−324` at 48, first unpaid obligation on turn 40); and Part II's rule IDs were renumbered `+39` to DMP-173…DMP-274 to remove a duplicate-ID collision with Part I's cross-system contracts. v2.0 completes Prompt 06 with the Part II political layer: the 240-turn per-nation election cycle and 24-turn campaign, the incumbent-plus-two-simulated-challengers contest, three campaign actions, the turnout-weighted vote, the 12-turn TRANSITION after a lost election or confidence vote, the continuous legitimacy-pressure test and government-specific thresholds, the 18-turn CRISIS, the 12-turn RECOVERY, the leadership state machine and the P4.4 settlement step. **No production or tax multiplier is created**; a crisis reaches the economy only through the new `political_stability_penalty_bp` term in DMP-053. It also adds 31 worked examples (E19–E49), the 06B contracts and the resolved UD-034/UD-035. v1.4 is the source-synchronisation pass: the code blocks of DMP-066, DMP-067, DMP-068, DMP-069 and DMP-070 now carry the signed tax term `+ (300 − tax_bp) // divisor` that F-PD-004…F-PD-008 already published, instead of the superseded `− floor((tax_bp − 300) / divisor)` form that DMP-071a rejects. No number, range, coefficient or example changed; the paragraphs already stated the corrected ranges. v1.3 was the final micro-correction: F-PD-002 now clamps the result of both the growth and crowding paths to the **1,000** floor, with the review's 993 case documented; the Labour, Industry and Commerce tax terms use the signed `(300 − tax_bp) // divisor` form so their published endpoints hold, with DMP-071a stating the endpoints and Example 5, DMP-099, DMP-168 and D-091 recalculated. No coefficient or design choice changed. v1.2 was the acceptance-reconciliation pass; v1.1 corrected five arithmetic/wording defects; v1.0 was the first issue.)
**Status:** **Draft — Prompt 06 documentation complete (Part I foundation + Part II political layer) and reconciled on 2026-10-28; no rule here is implemented, migrated or runtime-tested, and Prompt 14's balance simulation has not run.**
**Bible part:** B-06 · **Authoritative for:** population, population growth, public approval, political stability, legitimacy, political constituencies, government types and permanent government identity, government modifiers, national policy, and the political state and contracts that Prompt 06B builds on.
**Companions:** [research report](research/06_politics_and_war_domestic_politics_elections_and_policy_research.md) · [formula register](12_population_and_domestic_politics_formula_register.md) · [B-04 economy](10_economy_resources_treasury_and_finances.md) · [B-05 cities](11_cities_infrastructure_production_and_research.md) · [B-02 turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [B-03 account and nation lifecycle](09_account_onboarding_nation_creation_and_progression.md) · [requirements](03_requirements_traceability.md)

---

## 1. Purpose and scope

**DMP-001 — What this document decides.** *Provisional.* B-06 defines **who the people are and what they want**. It fixes the national population, how it grows and declines, how food and housing constrain it, how public approval and political stability are measured and moved, how six political constituencies react to the economy and to policy, which governments exist and why they are permanent, what each government permanently changes, and which two national-policy axes the player may adjust. It also defines the political state, the settlement step and the interfaces Prompt 06B must consume.

**DMP-002 — What this document does not decide.** *Provisional.* B-06 does **not** define elections, campaigns, candidate registration, vote calculation, the election interval, the consequence of losing an election, leadership retention in non-electoral governments, political crises, unrest, the duration or severity of a crisis, leadership-loss recovery, or the final political balance numbers. Those belong to **Prompt 06B**, which extends this document and its register. B-06 also does not define trade, prices or market conduct (Prompt 07); diplomacy or sanctions (Prompt 08); alliances (Prompt 09); warfare, military units or combat (Prompt 10); world events, rankings or rewards (Prompt 11); moderation, audit procedure or data retention beyond the records named here (Prompt 12); screens, layout or flows (Prompt 13); the final balance numbers (Prompt 14); or Bible assembly (Prompt 15). Every boundary is stated as a contract in §18.

**DMP-003 — The one-sentence design.** *Provisional.* A nation has **one people**, who live inside the housing its cities provide, eat the food it produces, judge the government through six constituencies, and reward a government that is stable, fed and legitimate — while the form of that government is chosen once and never changes.

**DMP-004 — Design-only status.** *Provisional.* Nothing in B-06 exists as code. There is no population column, no approval meter, no policy table and no political scheduler. The 18 worked examples are hand calculations re-checked by an independent script; no player has governed anything. The words "election", "campaign", "crisis" and "unrest" appear here only as reserved interfaces and are not specified.

---

## 2. Authority and precedence

**DMP-005 — Precedence.** *Provisional.* When documents disagree, this order applies:

1. [DECISIONS.md](../DECISIONS.md) — a recorded project decision.
2. [B-04](10_economy_resources_treasury_and_finances.md) and [its register](10_economic_formula_and_balance_register.md) — food production and consumption, the hunger penalty, tax income, treasury, reservations, settlement and the ledger.
3. [B-05](11_cities_infrastructure_production_and_research.md) and [its register](11_city_infrastructure_production_and_research_formula_register.md) — housing capacity, civic centres, research institutes, `CIVIC_UNFUNDED` and `LAB_IDLE`.
4. [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) — turn identity, phases, action states, recovery and idempotency.
5. [B-03](09_account_onboarding_nation_creation_and_progression.md) — the account model, nation creation, reroll, protection and dormancy.
6. **This document** — population, approval, stability, legitimacy, constituencies, government and policy.
7. [The B-06 register](12_population_and_domestic_politics_formula_register.md) — the authoritative formula definitions for everything this document owns.

If B-06 and its register disagree, **the register wins until one of them is corrected**. If B-06 and B-04 disagree about food or tax, **B-04 wins**; B-06 may supply the population and stability inputs, never change the formulas that consume them.

**DMP-006 — Ownership map.** *Provisional.* One quantity, one owner:

| Quantity | Owner | B-06 may |
|---|---|---|
| Food production, storage, consumption, `hunger_penalty_bp` | B-04 (ECN-080…091) | read `hunger_penalty_bp`; add a demographic and support consequence |
| Tax formula, treasury, operating cost, austerity order | B-04 (ECN-094…107) | supply `population` and `stability_factor_bp`; add a service-cost line through the published rule |
| Housing `45,000 + 100×I + 25,000×civic` | B-05 (URB-042) | consume it as a hard cap; never redefine it |
| `CIVIC_UNFUNDED`, `LAB_IDLE`, institute count | B-05 | consume the flags; never reinterpret a civic centre or a laboratory |
| Population size and growth | **B-06** | owns |
| `approval`, `stability_bp`, `legitimacy`, support values | **B-06** | owns |
| Elections, campaigns, retention, crises, unrest | **Prompt 06B** | reserved; B-06 supplies inputs only |
| Screens and flows | Prompt 13 | B-06 supplies the information contract |

---

## 3. Established constraints

**DMP-007 — Fixed constraints preserved.** *Provisional.* B-06 changes none of the following: one shared persistent world; a mapless, symbolic representation with no coordinates, land, borders or distance; one global turn every two hours on UTC boundaries (12 per day); server-resolved effects that continue while a player is offline; Cloudflare Pages for the site and Supabase for the database and turn engine, with no second scheduler; the free-first hosting posture; the eleven approved resources and the crown as the only currency; the one-account/one-active-nation policy and the instant-reroll policy; and Operations Points as the single **military** action resource (D-015), whose values remain Prompt 10's and 14's.

**DMP-008 — No new resource, currency or income source.** *Provisional.* Population is not a resource: it has no warehouse space, no ledger balance, no price and no trade. Approval, stability and legitimacy are not currencies. No policy, government or political event may create a crown or a unit. The only treasury movement B-06 introduces is a **cost** — the public-service cost of §16 — and it is paid out of existing tax income.

**DMP-009 — Account and reroll policy untouched.** *Provisional.* B-06 does not create a reroll cooldown, an account sanction, a political amnesty or a way to preserve political advantage across a reroll. A replacement nation receives the standard bundle (D-063) and a new political state (§17.3); it inherits no approval, stability, legitimacy, policy, government modifier, constituency support or history from the retired nation. Pair restrictions and account sanctions survive a reroll (D-059).

**DMP-010 — No general action currency.** *Provisional.* D-024 requires every subsystem to declare a visible limit for each action. B-06 declares exactly two: the **policy change cooldown** (§16.6) and the **once-per-nation government selection** (§14.5). There is no political action point, no influence currency and no daily click budget.

---

## 4. What the reference game contributed

**DMP-011 — The verified reference position.** *Provisional (research §2).* In Politics & War, government type is a cosmetic label with 32 standard options, freely changeable at will, and social and economic policies are questionnaires that the game's own documentation calls cosmetic. The national tax rate is deliberately revenue-neutral. The one policy with a mechanical effect is Domestic Policy: six mutually exclusive emphases, each a flat percentage (mostly −5% cost or +1% income), changeable once every 60 turns and amplified by a national project. Approval Rating is an unbounded score displayed as a clamped percentage, driven mainly by war and espionage, and the documentation states that it does not affect the nation in any way. Population is a capacity derived from infrastructure and land, reduced by disease and crime. There are no elections.

**DMP-012 — What we adopted.** *Provisional.* (1) A **small, mutually exclusive set** of policy settings with a real cooldown. (2) A **displayed percentage** for public sentiment. (3) The idea that a **major investment** can move public sentiment. (4) A **capacity-based** relationship between development and population. (5) The discipline of **flat, published arithmetic** rather than hidden multipliers.

**DMP-013 — What we rejected.** *Provisional.* (1) Cosmetic government: a label with no consequence cannot support a strategy. (2) Cosmetic policy questionnaires: a choice that changes nothing is noise. (3) A revenue-neutral tax rate: it removes a decision B-04 deliberately makes real. (4) Percentage-only policy effects: they collapse into "pick the discount for your next purchase". (5) Additive discount stacking: B-05 already allows one source per cost. (6) An amplifier project that multiplies the same effect again. (7) An inert approval rating: a number with no consequence is decoration. (8) Unbounded scores displayed as percentages: the player sees `0% (−596.02)` and learns nothing actionable. (9) Disease and crime as separate mortality meters: they would be a second and third penalty on the same infrastructure.

**DMP-014 — Evidence limits.** *Provisional (research §1).* The wiki was read through archived snapshots because the live site returned HTTP 403; the forum timed out and is cited only at snippet level. No P&W account was created and no in-game test was run. The research is documentary and its limitations are recorded in the report rather than papered over.

---

## 5. Design principles

**DMP-015 — One causal path per effect.** *Provisional.* An input changes an outcome through exactly one published chain. Food affects approval **only** through the hunger terms in constituency support; it does not also subtract approval directly. Policy affects approval **only** through support; it does not also add a flat approval bonus. Government affects tax **only** through stability (and service cost); it has no separate tax multiplier. This is the rule that makes the arithmetic auditable and prevents the same event from being counted twice.

**DMP-016 — Decisions, not sliders.** *Provisional.* Two categorical policy axes with three settings each, plus a fixed government, are enough to express a strategy. Intermediate tax rates, percentage dials and per-group favour meters are rejected as false precision: a player cannot feel the difference between 305 and 310 basis points, and every extra dial is a screen that must be explained.

**DMP-017 — Explain every number.** *Provisional.* Every change to approval, stability, support or population must be attributable to a named term in a published formula. No random drift, no hidden "mood" and no unexplained modifier. The interface must be able to answer "why did this move?" with the exact terms (DMP-130).

**DMP-018 — No permanent punishment.** *Provisional.* A nation can always recover from a political low. There is no bankruptcy, no game-over, no permanent approval scar and no policy that cannot be reversed. The recovery path is published: fix food, fund services, change policy, wait for approval to converge. This follows B-04's no-debt austerity posture and D-028's protective dormancy.

**DMP-019 — Absence tolerant.** *Provisional.* The political system resolves at the boundary whether or not the player is present. Nothing requires a login: a policy persists, a government persists, approval and stability move on their own terms, and a dormant nation keeps its political state (D-028). No bonus, streak or penalty depends on attendance.

**DMP-020 — Permanent identity, adjustable policy.** *Provisional.* The **form** of government is chosen once and is permanent for the life of the nation. The **policy** inside that form is adjustable within the government's legal settings. This separates the long-horizon decision (who rules, and with what structural advantage) from the medium-horizon decision (how the state spends and how it keeps order).

**DMP-021 — No double counting.** *Provisional.* A quantity is applied once. A government's stability shift is added once to the stability target. A policy's service share sets the service cost once. A research bonus is added once to the institute count. A modifier may not enter through two channels, and no effect may be applied both to a gross value and to a derived value that already contains it.

---

## 6. Population: what it is

**DMP-022 — Population is national, integer and singular.** *Provisional (REQ-258).* A nation has exactly one population value: `population`, an integer number of people. It is national, not per-city. It is the tax base (B-04 ECN-094), the food demand base (B-04 ECN-080) and the denominator for housing sufficiency. There is no second population count, no "working population", no "citizens" versus "subjects" and no per-city population field.

**DMP-023 — Cities do not hold people; they hold housing.** *Provisional (REQ-258).* B-05's city has no population of its own (URB-026). A city contributes `housing_capacity` (URB-042) to the national total. The interface may display a city's **share** of the national population, computed as `floor(population × housing(city) / national_housing)`, but that share is a presentation device: it is not stored, not simulated, not moved and never used by a formula. People do not migrate between cities, because there is nowhere to migrate to.

**DMP-024 — The standard starting population is 50,000.** *Provisional (REQ-259; D-063).* Every nation begins with **50,000 people**. A standard capital at infrastructure 50 houses exactly 50,000 (URB-042), so a new nation begins **exactly housed with no headroom**. Population cannot grow until the player adds housing — a civic centre or infrastructure — which makes the first population decision a city decision (B-05 §19).

**DMP-025 — The population floor is 1,000.** *Provisional (REQ-259).* Population may not fall below **1,000** by any rule in B-06. At the floor the nation is in `DEPOPULATED` distress: tax income is negligible, food demand is 1 unit and recovery is still possible by fixing food, housing and services. B-06 never deletes a nation, never declares a game-over and never evicts the last residents. Any removal of a nation is Prompt 12's, under a separate decision.

**DMP-026 — Population is not a resource.** *Provisional (REQ-260).* Population has no warehouse space, no ledger balance, no book value, no price and no trade. It cannot be bought, sold, gifted, transferred or stored. It is not part of national wealth (B-04 ECN-093). A reroll destroys it with the nation; nothing carries over.

**DMP-027 — The population record.** *Provisional (REQ-260).* The political state stores `population` (integer ≥ 1,000), `population_last_turn` (for the digest delta) and `population_changed_turn`. It stores no per-city population, no birth rate, no death rate and no migration flow. Growth is computed once per turn from the opening state and written once.

---

## 7. Population growth and decline

**DMP-028 — Growth is a rate in basis points.** *Provisional (REQ-260).* Population changes once per settlement. The rate is an integer in basis points:

```
growth_bp = clamp(
    50
    + floor((approval − 55) / 2)
    + min(15, floor(headroom × 100 / population))
    − floor(hunger_bp / 30)
    − floor(crowding_bp / 100),
    −100, 100)
```

- `approval` is the value at the start of P3.8 (§17.4).
- `headroom = max(0, housing − population)`, where `housing` is the national housing for growth (§8.3).
- `hunger_bp` is B-04's `hunger_penalty_bp` for this turn, 0…3,000.
- `crowding_bp` is defined in DMP-044; it is 0 when population is at or below housing.
- The base rate is **50 bp** (0.5% per turn). At 12 turns per day a nation that is fed, housed and content grows about **6.2% per day** before the headroom term slows it.
- The result is clamped to **−100…+100 bp**. A nation can lose at most 1% of its people per turn to these terms.

**DMP-029 — The four growth inputs.** *Provisional (REQ-260).* Only four things move the rate:

| Input | Effect on `growth_bp` | Why |
|---|---|---|
| Approval above or below 55 | ±1 bp per 2 points, capped by the clamp | People who back the government are more willing to raise families under it |
| Housing headroom | 0…+15 bp, proportional to `headroom / population` | Room to grow; the term falls smoothly as the cap approaches |
| Food shortage | 0…−100 bp at `hunger_bp` 0…3,000 (`/30`) | Hunger suppresses growth and, at the maximum, causes decline |
| Crowding | 0…−100 bp (`/100`) | People above the housing cap leave |

Nothing else moves population. There is no random event, no disease roll, no war mortality (Prompt 10 may add a **separate** war-loss rule through a decision and a register row) and no migration.

**DMP-030 — Housing is a hard cap on growth.** *Provisional (REQ-261; URB-124).* Population may not grow above national housing. If the computed natural increase would exceed housing, the new population is **exactly housing**, not housing plus the excess. The excess is not stored, banked or converted. B-05 owns the number; B-06 owns the rule that reads it.

**DMP-030a — The 1,000 floor binds every path.** *Provisional (REQ-259; F-PD-002).* The order of calculation is fixed: read the opening population → compute `growth_bp` (DMP-028) → compute `natural` with the **floored** growth → take the growth/cap branch or the crowding branch (DMP-031) → apply **`max(1,000, raw)`** → store. The floor is applied **after** the growth rounding and after the crowding decline, so no path can return a population below 1,000. At the floor a further negative rate holds the population at **1,000**: it does not bank a debt of people, create food or income, or grant a recovery bonus, and a later positive rate resumes from 1,000. Settlement runs once at P3.8 and reads the stored result, so the same growth is never applied twice (DMP-034). The floor example: population 1,000, approval 0, housing 45,000 and `hunger_bp` 3,000 give `growth_bp = 50 + floor(−55/2) + 15 − 100 = −63`; `natural = 1,000 + floor(1,000 × −63/10,000) = 993`; `raw = min(993, 45,000) = 993`; the result is **1,000**, not 993.

**DMP-031 — Crowding is a gradual decline, never an eviction.** *Provisional (REQ-262; URB-124).* If population is already above housing — because a civic centre's upkeep went unpaid and its housing is no longer counted, because warfare damage lowered a city's infrastructure level, or because a future rule removed housing — the nation is **crowded**:

```
crowding_bp = min(10,000, floor((population − housing) × 10,000 / population))
```

and population falls by **10% of the excess per turn**, rounded up, or by the natural decline if that is larger:

```
excess  = population − housing
decline = max(ceil(excess / 10), max(0, population − natural))
new_population = population − decline
```

No one is evicted in a single turn, and the result is never taken below the **1,000** floor (F-PD-002). At an excess of 10,000 the decline is 1,000 in the first turn and about 900 in the second. The excess decays by about **10% a turn**, so less than 1,000 people remain over the cap after 22 turns; the last few hundred take longer, because the decline is proportional and never a single eviction. The digest reports the excess, the decline and the reason (`CIVIC_UNFUNDED`, `INFRASTRUCTURE_DAMAGED` or another named cause).

**DMP-031a — Infrastructure damage is a housing-source change, not a casualty rule.** *Provisional.* A warfare strike never kills, evicts, moves or deletes people (`WAR-109f`). It lowers a city's infrastructure level, and the lower level yields less housing (`DMP-037`, B-05 `URB-042`). The new `housing_population(T)` (B-05 `URB-046`, B-10 `WAR-109m`) is read at the **next P3.8**, where `DMP-034` computes population once. If that housing is below the population, `DMP-031` applies the ordinary crowding decline; if housing still covers the population, nothing happens. A repair restores housing from the next P3.8 and crowding stops once housing covers the population again. No separate warfare population formula exists and none may be added.

**DMP-032 — Food shortage slows growth and can reverse it.** *Provisional (REQ-263; ECN-088).* B-04 owns the shortage and the economic penalty. B-06 adds the demographic consequence through DMP-028: at `hunger_bp` 1,500 (a half-fed nation) growth falls by 50 bp; at 3,000 (a total shortfall) it falls by 100 bp, which turns the base rate negative and produces a decline of about 0.5% per turn before crowding. A fed nation recovers at the next settlement; the demographic penalty has no memory.

**DMP-033 — No migration at launch.** *Provisional (REQ-263).* People do not move between nations, between cities or into a "population pool". There is no refugee flow, no immigration policy and no brain drain. A future migration rule would need a decision, a register row and a stated source and sink; it may not be added by reinterpreting an existing term.

**DMP-034 — Timing: P3.8, effective next turn.** *Provisional (REQ-264).* Population is computed **once** at P3.8 of the settlement, after food (P3.6) and obligations (P3.7), from the opening population and the post-settlement food and housing. The new value is stored at P3.8 and is used by the **next** turn's tax (P3.1) and food demand (P3.6). It never changes the current turn's tax, food consumption or production. A resumed settlement reads the stored result and does not grow the population twice.

---

## 8. Food, housing and welfare interfaces

**DMP-035 — Food demand is B-04's.** *Provisional (REQ-265; ECN-080).* `food_demand = ceil(population / 1,000)`. At 50,000 people demand is **50 units**. B-06 supplies the population; B-04 owns the formula, the stock, the consumption order and the shortage ratio.

**DMP-036 — The hunger penalty is read, not recomputed.** *Provisional (REQ-265; ECN-084).* B-04 computes `hunger_penalty_bp = min(3,000, floor(3,000 × unmet_food / food_demand))`. B-06 consumes that integer in growth, in constituency support and in stability. B-06 may not change the cap, the formula or the recovery rule (ECN-085).

**DMP-037 — Housing is B-05's.** *Provisional (REQ-265; URB-042).* `housing(city) = 45,000 + 100 × infrastructure + 25,000 × civic_centres`. National housing is the sum over cities. B-06 may not add a second housing source, change the formula or reinterpret a civic centre as anything other than housing (URB-126).

**DMP-038 — An unfunded civic centre does not house.** *Provisional (REQ-265; URB-120).* When a civic centre's upkeep is unpaid at P3.7, B-05 sets `CIVIC_UNFUNDED` for that city. Its 25,000 housing is **excluded from the housing used for growth** in that settlement. The people already living there are not evicted (DMP-031); the nation is crowded until the centre is funded again. Housing used for growth is therefore

```
housing_growth = Σ_cities (45,000 + 100 × infrastructure + 25,000 × funded_civic_centres)
```

where `funded_civic_centres` counts only centres whose upkeep was paid this turn.

**DMP-039 — An unfunded service is no service.** *Provisional (REQ-265; DMP-097).* If the public-service cost is not paid at P3.7, `SERVICES_UNFUNDED` is set and the effective service share for this settlement is **zero**: the support bonus disappears, but the cost is also not charged. The player cannot receive the political benefit of a service the nation did not pay for.

**DMP-040 — No eviction and no destruction.** *Provisional (REQ-262).* A housing shortfall, a food shortage or a political low never destroys a city, a building, a resource, a technology or a crown. It changes people and sentiment. The only destructive actions in the game remain B-05's demolition and B-04's consumption.

**DMP-041 — Forecast before the boundary.** *Provisional (REQ-266).* The interface must show, before the turn closes, the projected `population` change, the projected `approval` and the projected `stability_bp` under the current policy and the current food and housing state. Every projection is labelled a forecast, not a result, because trade, construction and war can change the inputs before the boundary (B-04 ECN-090's rule applies to political forecasts as well).

**DMP-042 — Welfare is a relationship, not a meter.** *Provisional (REQ-266).* B-06 deliberately has **no welfare index**. A separate 0–100 "welfare" score would be a near-duplicate of approval and would have no decision attached to it (DMP-016). The things a welfare meter would summarise — food security, housing sufficiency, funded services, employment-like opportunity — enter the formulas directly and visibly:

| Welfare input | Published source | Where it enters |
|---|---|---|
| Food security | `hunger_penalty_bp` (B-04) | growth, labour/rural/security support, stability |
| Housing sufficiency | `housing_bp` (DMP-044) | labour support |
| Funded services | `service_share_bp` if funded, else 0 | labour/scholar/rural/security support, service cost |
| Economic opportunity | production mix, warehouse headroom, institutes | rural/industry/commerce/scholar support |
| Governance | `approval`, `stability_bp` | stability target, growth |

**DMP-043 — No separate employment variable.** *Provisional (REQ-265).* B-06 rejects a workforce, employment rate or unemployment meter. Production in Nation Supremacy is **capacity-based**, not labour-based: a facility runs if it has capacity, inputs, power and money (B-04/B-05). Adding employment would impose a second constraint on the same facilities, penalise the same idleness twice and create a variable no formula needs. The political meaning of "people have work" is carried by the **production mix** and the **warehouse/institute** terms already in the support formulas, which reward a diversified, operating economy without inventing a labour market.

**DMP-044 — Housing sufficiency.** *Provisional (REQ-266).* Two derived integers describe the housing relationship:

```
housing_bp  = min(10,000, floor(housing × 10,000 / population))     (0…10,000)
crowding_bp = 0 if population ≤ housing
              else min(10,000, floor((population − housing) × 10,000 / population))
```

`housing_bp` is 10,000 when every person is housed, 5,000 when housing covers half the population, and 0 when there is no housing. It enters labour support once (DMP-066). `crowding_bp` enters growth and stability once each.

---
## 9. Public approval

**DMP-045 — Approval is a bounded integer from 0 to 100.** *Provisional (REQ-267).* `approval` measures how well the population regards the government. It is stored as an integer **0…100**, displayed as a percentage and never stored as an unbounded score. The reference game's unbounded underlying value is rejected (DMP-013): a displayed `0%` must mean "no support", and a player must be able to compute the next value by hand.

**DMP-046 — Approval follows the constituencies.** *Provisional (REQ-267).* Approval is the **population-weighted mean** of the six constituency support values:

```
approval_target = clamp(floor(Σ (support_i × weight_i) / 100), 0, 100)
```

with the weights and support formulas of §12. There is no separate national "mood" term, no random drift and no direct event modifier. If an event moves approval, it does so by moving one or more constituency supports, and the movement is attributable to that group (DMP-015).

**DMP-047 — Approval moves at most five points per turn.** *Provisional (REQ-268).* Approval does not jump to its target:

```
approval_next = clamp(approval + clamp(approval_target − approval, −5, +5), 0, 100)
```

The cap is what makes a shock legible. A 20-point collapse in the target takes four turns (eight hours) to register, and the digest can show both the target and the distance still to travel. The cap also prevents a one-turn policy flip from harvesting a support swing and reversing it before the population notices.

**DMP-048 — No random drift, no hidden mood.** *Provisional (REQ-268).* Approval changes only through the formula above. There is no daily random walk, no "the people are restless" modifier and no secret decay. If a nation does nothing and its inputs do not change, approval converges to a fixed target and stays there.

**DMP-049 — Approval is shown with its causes.** *Provisional (REQ-269).* The interface must display the current approval, the target, the distance, the six support values with their weights, and the named terms that moved each support since the last turn. The history must be inspectable for at least the retention window of class-S digests (D-026). A player must be able to answer "why is my approval 41?" without opening a spreadsheet.

**DMP-050 — Approval 0 and 100 are states, not deaths.** *Provisional (REQ-269).* At approval 100 the nation is `UNANIMOUS`; at 0 it is `NO_CONFIDENCE`. Both are presentation states. Neither deletes the nation, changes the government or blocks play. Approval 0 still leaves a stability target above the 5,000 floor for every government, so a hated government is inefficient, not dead. *(Prompt 06B decides what a sustained low approval does to a leader; B-06 deliberately does not.)*

**DMP-051 — Approval is not a success ladder.** *Provisional (REQ-269).* A high approval is not a score, an achievement currency or a ranking criterion. It is an input to stability (DMP-055) and growth (DMP-028), and in Prompt 06B it will be an input to elections and leadership challenges. It grants no resource, no crown and no permanent modifier (D-024 and D-027's posture: no ladder that can be bought).

---

## 10. Political stability

**DMP-052 — Stability is administrative capacity.** *Provisional (REQ-270).* `stability_bp` measures the government's ability to administer the nation: collect tax, run services, enforce decisions and keep the country legible to itself. It is **not** approval and **not** legitimacy. A government can be disliked and still administratively effective (a junta), or popular and administratively weak (a fragmented democracy). Stability is the only political variable that enters an economic formula, and it enters exactly one: B-04's `stability_factor_bp` (ECN-094).

**DMP-053 — The stability target.** *Provisional (REQ-270).*

```
stability_target_bp = clamp(
    10,000
    + (approval − 55) × approval_weight_bp
    + stability_shift_bp
    + order_stability_bp
    − floor(hunger_bp / 2)
    − floor(crowding_bp / 10)
    − political_stability_penalty_bp,
    5,000,
    stability_cap_bp)
```

| Term | Source | Range | Meaning |
|---|---|---|---|
| `10,000` | fixed | — | 100% at the reference point (approval 55, balanced order, no hunger, no crowding) |
| `(approval − 55) × approval_weight_bp` | government (DMP-086) | −1,760…+1,440 | How much public opinion matters to this government |
| `stability_shift_bp` | government (DMP-086) | −150…+400 | Structural administrative capacity |
| `order_stability_bp` | policy (DMP-094) | −200…+300 | Repression versus openness |
| `−floor(hunger_bp / 2)` | B-04 | 0…−1,500 | A hungry nation cannot be administered |
| `−floor(crowding_bp / 10)` | B-06 | 0…−1,000 | People outside housing are outside the administration |
| `−political_stability_penalty_bp` | 06B (F-PD-026) | 0…−1,500 | A leadership transition or crisis. It is **one** term, zero in every ordinary state, and it is the only route from 06B to the economy |

The result is clamped to **5,000…`stability_cap_bp`**, where the cap is the government's (DMP-086) and never exceeds B-04's 11,000 hard bound.

**DMP-054 — Stability moves slowly.** *Provisional (REQ-271).*

```
stability_next = stability_bp + clamp(stability_target_bp − stability_bp, −250, +250)
```

Stability moves at most **250 bp (2.5 points) per turn**. A famine that removes 1,500 bp from the target takes six turns to be fully felt; a new government's structural shift takes two to three turns to settle. This is the political equivalent of a capacitor: it prevents a one-turn tax collapse and gives the player time to respond.

**DMP-055 — Stability feeds tax, once.** *Provisional (REQ-272; ECN-094).* B-04 computes

```
tax_income = floor(population × tax_rate_bp × stability_factor_bp / 1,000,000,000)
```

with `stability_factor_bp = stability_bp`. B-06 does not add a second tax multiplier, a government tax bonus, a policy tax bonus or an approval tax bonus. The **only** route from politics to tax is stability, and the only routes into stability are the six terms above. At 50,000 people and 300 bp, a 1,000 bp stability change is worth **15 crowns per turn** — which is why the movement cap and the published terms matter.

**DMP-056 — Stability is not a second approval.** *Provisional (REQ-272).* The two values have different drivers and different speeds. Approval is a weighted mean of six groups and moves up to 5 points per turn; stability is a formula over approval, government, order, hunger and crowding, and moves up to 2.5 points per turn. A government can have approval 70 and stability 9,850 (a popular democracy with a contentious system) or approval 40 and stability 10,400 (an unpopular junta). The interface must show both, labelled separately, and must never merge them into a single "support" bar.

**DMP-057 — Stability is bounded by the government, not by the player.** *Provisional (REQ-272).* The per-government cap is a **ceiling on coercion**: an authoritarian system can be stable quickly, but it cannot convert fear into the same administrative quality that sustained consent produces. The cap is published before nation creation (DMP-083) and is part of the government's visible identity.

---

## 11. Legitimacy

**DMP-058 — Legitimacy is derived, not stored.** *Provisional (REQ-273).* `legitimacy` measures whether the groups that can remove the government still support it. It is **computed**, never stored as a third meter:

```
legitimacy = clamp(floor(Σ (institutional_weight_i × support_i) / 100), 0, 100)
```

Each government declares an **institutional weight vector** over the six constituencies (DMP-059). The vector sums to 100. Legitimacy is recomputed whenever support changes and is displayed alongside approval with the label "support among the institutions that can remove this government".

**DMP-059 — The institutional vectors.** *Provisional (REQ-273).*

| Government | Labour | Rural | Industry | Commerce | Scholars | Security | Who can remove the government |
|---|---:|---:|---:|---:|---:|---:|---|
| Democracy | 30 | 15 | 20 | 15 | 10 | 10 | The electorate — same as approval |
| Constitutional monarchy | 10 | 20 | 15 | 15 | 20 | 20 | Parliament, the court, the countryside and the officer corps |
| Absolute monarchy | 20 | 20 | 10 | 5 | 5 | 40 | The court, the countryside and, decisively, the army |
| Dictatorship | 5 | 10 | 20 | 10 | 0 | 55 | The security apparatus, with industry's acquiescence |
| Military junta | 0 | 0 | 0 | 0 | 0 | 100 | The officer corps alone |
| Technocracy | 5 | 0 | 15 | 5 | 65 | 10 | The academies, with industry's support |

Each row sums to 100. A democracy's legitimacy equals its approval by construction; a junta's legitimacy equals security support, which is why a junta can be hated and still legitimate — and why its legitimacy collapses if the army turns.

**DMP-060 — Legitimacy is used by Prompt 06B only.** *Provisional (REQ-273).* B-06 computes and displays legitimacy but attaches **no consequence** to it. Prompt 06B decides what a legitimacy threshold does to a non-electoral leader, how fast it is tested and what happens when it fails. B-06 must not pre-empt that with a stability or tax effect, or 06B would inherit a double penalty.

**DMP-061 — Why three concepts and not one.** *Provisional (REQ-273).* The brief asks whether approval and legitimacy should be separate. They should, because the game has both electoral and non-electoral governments: an elected leader is removed by the population, a monarch or junta by institutions. Stability is separate again because it is the only one that changes tax. Three concepts, two stored values (approval, stability) and one derived value (legitimacy) is the smallest model that lets 06B describe both kinds of removal without inventing a fourth meter.

---

## 12. Political constituencies

**DMP-062 — Six groups, fixed launch roster.** *Provisional (REQ-274).* The population is represented by six aggregated groups. There is no seventh group at launch, no individual citizens and no per-city groups.

| ID | Name | Weight | What the group is |
|---|---|---:|---|
| `con_labour` | Labour | **30** | People who work for wages in extraction, processing, construction and services |
| `con_rural` | Rural producers | **15** | The food-producing and country-based interest |
| `con_industry` | Industry | **20** | The owners and managers of processing capacity and construction |
| `con_commerce` | Commerce | **15** | Traders, distributors and the warehouse-and-market interest |
| `con_scholars` | Scholars | **10** | Researchers, institutes and the educated professions |
| `con_security` | Security institutions | **10** | The officer corps, the police and the internal security establishment |

The weights sum to **100**. They are the population weights used by approval (DMP-046).

**DMP-063 — Weights are fixed.** *Provisional (REQ-274).* The six weights are constants. They do **not** vary with population, employment, the number of cities, the production mix or policy. A variable weight would make approval and elections depend on a hidden composition function — a player could not predict a vote without modelling the whole economy — and would violate DMP-017. The economy still matters politically through **support**: building farms raises rural support, building industry raises industry support, and neglecting a group lowers its support even though its weight does not move.

**DMP-064 — Support is a small sum of named terms.** *Provisional (REQ-274).* Each group's support is a base of **48** plus a handful of integer terms, clamped to **0…100**. Every term is published in the register (F-PD-004…F-PD-009) and every input is a value another accepted document already owns. There is no random component, no hidden "group mood" and no per-group memory beyond the current state.

**DMP-065 — The inputs.** *Provisional (REQ-274).*

| Input | Owner | Definition |
|---|---|---|
| `hunger_bp` | B-04 | 0…3,000 |
| `tax_bp` | B-06 policy | 200 / 300 / 400 (DMP-094) |
| `service_share_bp` | B-06 policy, effective | 0 / 2,000 / 5,000, or 0 if `SERVICES_UNFUNDED` |
| `stability_bp` | B-06 | opening value at P3.8 |
| `housing_bp` | B-06 (from B-05) | DMP-044 |
| `food_share_bp` | B-06 (from B-05 capacity) | `floor(food_capacity × 10,000 / production_capacity)`, 0 if the denominator is 0 |
| `processing_share_bp` | B-06 (from B-05 capacity) | `floor(processing_capacity × 10,000 / production_capacity)` |
| `warehouse_bp` | B-04 (from B-05) | `floor(free_warehouse × 10,000 / warehouse_total)`, 10,000 if total is 0 |
| `institutes_active` | B-05 | institutes that produced research this turn (`LAB_IDLE` excluded) |
| `order` | B-06 policy | OPEN / BALANCED / FIRM |

`production_capacity` is the sum of **extraction and processing** capacity only. Generators, warehouses, institutes and civic centres are excluded, so a nation cannot raise rural support by building power plants.

**DMP-066 — Labour.** *Provisional (REQ-275).*

```
support_labour = clamp(48
    + floor(service_share_bp / 400)
    + (300 − tax_bp) // 40
    + (floor(housing_bp / 500) − 18)
    − floor(hunger_bp / 100)
    + order_labour, 0, 100)
```

Labour is the largest group and cares about three things: **services** (a generous state is worth paying for), **food** (hunger hits it hardest, −30 at a total shortfall), and **housing** (`+2` when fully housed, negative below 90% sufficiency). Its tax sensitivity is small (−3…+2), because a wage earner experiences the tax rate through services rather than as a business cost. `order_labour` is +6 (OPEN), 0 (BALANCED), −6 (FIRM).

**DMP-067 — Rural producers.** *Provisional (REQ-275).*

```
support_rural = clamp(48
    + floor(food_share_bp / 250)
    + floor(service_share_bp / 1,000)
    + (300 − tax_bp) // 20
    − floor(hunger_bp / 150)
    + floor((stability_bp − 10,000) / 500)
    + order_rural, 0, 100)
```

Rural support rises with the **share of production capacity devoted to food** (+15 at the starting 37.5%, up to +40 at an all-food economy), with services, and with stability; it falls with tax (−5…+5) and hunger (−20 at a total shortfall). `order_rural` is −4 (OPEN), 0, +4 (FIRM).

**DMP-068 — Industry.** *Provisional (REQ-275).*

```
support_industry = clamp(48
    + floor(processing_share_bp / 250)
    + (300 − tax_bp) // 15
    + (floor(warehouse_bp / 1,000) − 5)
    + floor((stability_bp − 10,000) / 400)
    + order_industry, 0, 100)
```

Industry cares about **processing capacity share** (+5 at the starting 12.5%, up to +40 at an all-processing economy), **warehouse headroom** (a full warehouse blocks output and raises cost), stability and tax (−7…+6). `order_industry` is +2 (OPEN), 0, −2 (FIRM). It is deliberately **not** moved by services: industry pays for them through tax and does not consume them.

**DMP-069 — Commerce.** *Provisional (REQ-275).*

```
support_commerce = clamp(48
    + (floor(warehouse_bp / 1,000) − 5)
    + (300 − tax_bp) // 12
    + floor((stability_bp − 10,000) / 400)
    + order_commerce, 0, 100)
```

Commerce is the **most tax-sensitive** group (−9…+8): it has the most mobile interest and the least attachment to a particular facility. It values warehouse headroom and stability, and it is the group most moved by civil order (+8 OPEN, −8 FIRM). It has no service term: it buys services privately.

**DMP-070 — Scholars.** *Provisional (REQ-275).*

```
support_scholars = clamp(48
    + min(12, 3 × institutes_active)
    + floor(service_share_bp / 400)
    + (300 − tax_bp) // 50
    + order_scholars, 0, 100)
```

Scholars care about **research institutes** (+3 each, capped at +12), services and **civil liberties** (+10 OPEN, −10 FIRM). They are the least tax-sensitive group (−2…+2). A nation that builds institutes and opens its society keeps its scholars even on a high tax rate; a nation that builds none and represses begins at 38 under FIRM.

**DMP-071 — Security institutions.** *Provisional (REQ-275).*

```
support_security = clamp(48
    + floor(service_share_bp / 2,000)
    − floor(hunger_bp / 200)
    + floor((stability_bp − 10,000) / 400)
    + order_security, 0, 100)
```

Security is the **order group**: +15 under FIRM, −15 under OPEN. It also values funded services (+2 at generous), stability and food (a hungry country is an ungovernable one, −15 at a total shortfall). It is not moved by tax, because its budget is not modelled here (Prompt 10 owns military spending).

**DMP-071a — The tax term's signed endpoints.** *Provisional (REQ-275).* The tax term is `(300 − tax_bp) // divisor`, a signed step that rounds **toward the high-tax penalty**. This is not the same as `−floor((tax_bp − 300)/divisor)`, which produced one point more at the low-tax end and one point less at the high-tax end. The published endpoints are:

| Group | Divisor | `LOW` 200 | `STANDARD` 300 | `HIGH` 400 | Published range |
|---|---:|---:|---:|---:|---|
| Labour | 40 | **+2** | 0 | **−3** | **−3…+2** |
| Rural | 20 | +5 | 0 | −5 | ±5 |
| Industry | 15 | **+6** | 0 | **−7** | **−7…+6** |
| Commerce | 12 | **+8** | 0 | **−9** | **−9…+8** |
| Scholars | 50 | +2 | 0 | −2 | ±2 |

The asymmetry is deliberate: a tax rise is felt slightly more sharply than a tax cut is welcomed. The values are monotone across the permitted rates, the neutral rate is exactly zero, and the register's Range cells state these endpoints. **All five tax terms use it** — Labour 40, Rural 20, Industry 15, Commerce 12, Scholars 50 — so no support formula carries the superseded `floor` expression. Two earlier drafts kept it for Rural and Scholars on the grounds that 100 divides exactly by 20 and 50; that is true only at the three policy settings, not between them, where the forms differ by one point. Since the register is authoritative at every input, the prose follows it rather than relying on the coincidence.

**DMP-072 — Support reacts differently by group.** *Provisional (REQ-275).* The six formulas deliberately load on different inputs: services move labour and scholars, food share moves rural, processing share moves industry, warehouse headroom moves commerce and industry, institutes move scholars, and order moves security against scholars and commerce. No two groups have the same vector, and no single input moves all six equally. This is the requirement that the political system not be a single "economy score" in disguise.

**DMP-073 — The player can see why.** *Provisional (REQ-276).* For each group the interface must show: its name and role, its weight, its current support, its support last turn, and each named term with its current value and contribution. A player must be able to see that, for example, labour is at 40 because hunger is −15, housing is −2 and services are +5. No term may be hidden behind an aggregate.

**DMP-074 — Groups are abstractions, not stereotypes.** *Provisional (REQ-276).* The six groups are game interests, not descriptions of real people. Copy must describe what a group wants in the game's economy ("processing capacity", "warehouse headroom") and must not attribute ethnicity, religion, region or real-world politics to it. A group can be wrong, appeased, ignored or bought off; it cannot be an identity.

---
## 13. Government types and permanent identity

**DMP-075 — The proposal was evaluated, not assumed.** *Provisional (REQ-277).* The brief proposes that a player chooses a government at nation creation and cannot change it, and that the choice carries permanent positive and negative effects. B-06 treated that as a hypothesis. The benefits are real: the choice is the first strategic decision, it gives nations a durable identity, it makes rivals legible ("that is a junta; expect order and slow science"), and it removes the "switch to whatever bonus fits this week" behaviour that makes cosmetic governments irrelevant. The risks are equally real: a new player can regret an irreversible choice; one government can become dominant; permanent modifiers can compound into unequal growth; and repeated creation to fish for a favoured start is a farming route.

**DMP-076 — Decision: government identity is permanent for the life of the nation.** *Provisional (REQ-277; D-084).* B-06 adopts **Model A — permanent government identity**. The government is chosen once during nation creation, is recorded immutably on the nation, and **no rule in the game changes it**. Leadership changes, elections, succession, coups, crises and recovery (all Prompt 06B) change **who governs**, never **what the government is**. A monarchy that suffers a disputed succession remains a monarchy; a democracy that loses a leader remains a democracy; a junta that replaces its chair remains a junta.

**DMP-077 — The alternatives and why they were rejected.** *Provisional (REQ-277).*

| Model | What it would do | Why it was not adopted |
|---|---|---|
| **B — costly transition** | Allow a change through a major, expensive political process | A transition is a second, hidden balancing lever: the optimal play becomes "start as the growth government, transition to the war government". It also needs a crisis design that belongs to 06B, and it would let a nation escape a permanent disadvantage it was warned about |
| **C — exceptional transition only** | Prohibit routine change but allow a strictly controlled exception | The exception is the model. Once one exists, every player asks when to use it, and the design must price it, gate it and test it. At launch there is no evidence to price it correctly |
| **D — free change** | Let the player switch at any boundary | This is the reference game's cosmetic model with extra steps. It destroys the identity the choice is supposed to create and makes every modifier a temporary rental |

A future revision may add a transition **only** through a new decision, a new register row and a 06B crisis design; it may not be inferred from Model C's existence as an option.

**DMP-078 — The launch roster is six governments.** *Provisional (REQ-278).* Six types, each with a distinct leadership model and a distinct mechanical profile. The roster is **closed** at launch: a seventh type requires a decision, a leadership model, a modifier row, an institutional vector and a policy-permission row.

| ID | Display name | Leadership model | Who holds executive authority | Legitimacy base (DMP-059) | Policy permission (DMP-090) |
|---|---|---|---|---|---|
| `gov_democracy` | Democracy | Elections (06B) | An elected executive accountable to the electorate | The electorate (same weights as approval) | May not choose `FIRM` |
| `gov_constitutional_monarchy` | Constitutional monarchy | Hereditary head of state with a parliamentary confidence process (06B) | A monarch bound by a parliament | Parliament, court, countryside, officer corps | No restriction |
| `gov_absolute_monarchy` | Absolute monarchy | Hereditary succession (06B) | The monarch alone | Court, countryside, army | May not choose `OPEN` |
| `gov_dictatorship` | Dictatorship | Self-succession with a coup risk (06B) | One ruler and the security apparatus | Security apparatus, with industry's acquiescence | May not choose `OPEN` |
| `gov_military_junta` | Military junta | Council succession with a coup risk (06B) | An officer council | The officer corps alone | `FIRM` only |
| `gov_technocracy` | Technocracy | Appointment by peer institutions (06B) | Appointed experts | The academies, with industry's support | May not choose `FIRM` |

The six were chosen by merging the brief's eight candidates: Parliamentary Republic is folded into Democracy (the difference is which chamber appoints the executive, not what the player decides); Oligarchy is folded into Dictatorship (the difference is how many people hold power, not what the state does); Stratocracy is the Military Junta. Constitutional and Absolute Monarchy are kept as separate types because their leadership models and their stability profiles are genuinely different.

**DMP-079 — Leadership model is an interface, not a formula.** *Provisional (REQ-279).* B-06 records each government's leadership model so Prompt 06B can write the process. B-06 does **not** define the election interval, the campaign, the vote, the succession rule, the coup threshold, the crisis or the recovery. The words "elections", "confidence" and "coup risk" above are labels for 06B's work, not mechanics approved here.

**DMP-080 — Government, leader and administration are three different things.** *Provisional (REQ-279).*

| Concept | What it is | Changed by |
|---|---|---|
| **Government type** | The formal constitutional order (`gov_*`) | Nothing. Chosen at creation; permanent |
| **Leader** | The named person or body currently in office | Prompt 06B's elections, succession or crisis |
| **Administration** | The current policy settings and the governing style they express | The player, through `SET_POLICY` |

A player controls the **administration**. The leader is the office the administration holds. The government is the system that decides how the office is won. Confusing the three is how a political game turns a monarchy into a republic by accident; B-06 forbids it explicitly.

**DMP-081 — A leadership change never changes the government.** *Provisional (REQ-279).* If a democratic incumbent loses an election, the nation is still a democracy. If a monarch dies, the nation is still a monarchy. If a junta's chair is replaced, the nation is still a junta. No 06B outcome may write `government_id`. The only way a nation has a different government is a **new nation** (reroll), which is a total reset (DMP-084).

**DMP-082 — There is no government-change verb.** *Provisional (REQ-280).* The action catalogue contains no `SET_GOVERNMENT`, `REFORM_GOVERNMENT`, `REVOLUTION`, `COUP` or equivalent. A client that sends one is rejected as an unknown action, not silently ignored. The absence is a design rule, not an omission: adding the verb requires a new decision (DMP-077).

**DMP-083 — Selection happens at creation and requires confirmation.** *Provisional (REQ-280).* The government is the **last** step of nation creation, after the nation name and the capital. The player sees the full comparison panel (DMP-084), selects one, and confirms on a screen that states in plain language: *"This choice is permanent for this nation. You cannot change it later. If you want a different government, you must retire this nation and create a new one, which loses all progress."* The confirmation is recorded with the nation's creation record. A creation request without a valid `government_id` or without the confirmation flag is rejected; there is no default government.

**DMP-084 — The selection screen must show the whole trade.** *Provisional (REQ-280).* Before confirmation the player must be able to see, for every government: its leadership model and how a leader is removed; its approval weight (how much popularity matters); its stability shift and cap; its service-cost modifier; its research adjustment; its policy permissions; its institutional vector (who can remove the government); and a one-line statement of the strategic identity. The screen must show the **disadvantages** with the same prominence as the advantages. A government may not be described only by its bonus.

**DMP-084a — The six identity lines.** *Provisional (REQ-317).* The selection screen uses one sentence of strategic identity and one sentence of warning per government. These are the published words, not marketing copy:

| Government | Player-facing identity | Player-facing warning |
|---|---|---|
| Democracy | "Rule with consent: the most responsive economy in the game when you are popular, and the weakest when you are not." | "Your approval is your stability, and a lost election costs you the administration, not the nation." |
| Constitutional monarchy | "A flexible middle: no policy lock, a court and a parliament to satisfy, and no single weakness to exploit." | "You never lead by much. Expect to be second-best and to pay for it with adaptability." |
| Absolute monarchy | "Order from the top: a stable, orderly state that cannot open its society and struggles to convert popularity into efficiency." | "You may not choose `OPEN`. Your stability cap is 10,800, so a loved absolute monarch still taxes less than a loved president." |
| Dictatorship | "A cheap, closed administration: the lowest service bill in the game and the smallest circle of people who can remove you." | "You may not choose `OPEN`. Your cap is 10,600 and your legitimacy rests on the security apparatus." |
| Military junta | "The most stable government at low approval and the slowest research in the game; the army is the only constituency that matters." | "`FIRM` is your only legal order and you produce one fewer research point per institute. You cannot open." |
| Technocracy | "Government by experts: the strongest research in the game, a weaker tax base, and no taste for repression." | "Your stability is 150 bp below neutral and your cap is 10,900. You may not choose `FIRM`." |

**DMP-085 — Permanence is safe because reroll is instant.** *Provisional (REQ-281; D-039).* The mitigation for regret is not an undo button; it is the existing reroll policy. A player who dislikes their government may retire the nation and create a replacement **immediately**, on the same account, with no gameplay cooldown. The replacement loses every crown, resource, building, technology, programme, approval, stability, legitimacy and policy, and receives only the standard bundle (D-059/D-063). That is a real cost, which is why the choice matters, but it is not a trap: the player is never stuck. B-06 adds no reroll cooldown, no "government reselect" token and no protection re-grant.

---

## 14. Permanent government modifiers

**DMP-086 — Five channels, no others.** *Provisional (REQ-282).* A government changes exactly five things:

| Channel | Symbol | Unit | Where it applies |
|---|---|---|---|
| Approval weight | `approval_weight_bp` | bp per approval point | The stability target (DMP-053) |
| Stability shift | `stability_shift_bp` | bp | The stability target, once |
| Stability cap | `stability_cap_bp` | bp | The ceiling of the stability target, never above 11,000 |
| Service-cost modifier | `service_cost_mod_bp` | bp | The public-service cost (DMP-097), once |
| Research adjustment | `research_adjustment` | whole RP per turn | `rp_per_turn` (DMP-089), once |

Policy permissions (DMP-090) are a sixth, non-numeric channel. There is no government tax multiplier, production bonus, construction discount, upkeep discount, trade fee, combat modifier or approval offset. A future government that needs a new channel requires a decision and an amendment to B-04 or B-05; it may not invent a multiplier.

**DMP-087 — The government table.** *Provisional (REQ-282).*

| Government | `approval_weight_bp` | `stability_shift_bp` | `stability_cap_bp` | `service_cost_mod_bp` | `research_adjustment` |
|---|---:|---:|---:|---:|---:|
| Democracy | 32 | −100 | 11,000 | 0 | 0 |
| Constitutional monarchy | 22 | +200 | 10,900 | 0 | 0 |
| Absolute monarchy | 14 | +400 | 10,800 | 0 | 0 |
| Dictatorship | 16 | 0 | 10,600 | −1,000 | 0 |
| Military junta | 10 | +250 | 10,600 | +500 | −1 |
| Technocracy | 24 | −150 | 10,900 | 0 | +1 |

The table is the whole mechanical identity. Read across a row and the strategic shape is visible: the democracy is the most responsive to popularity and has the highest ceiling, but the lowest floor; the absolute monarchy is stable early and capped late; the dictatorship is administratively cheap but cannot open; the junta is the most stable at low approval and the slowest at research; the technocracy trades economic strength for research; the constitutional monarchy is the flexible middle with no policy lock.

**DMP-088 — Applied once, never compounded.** *Provisional (REQ-282).* Each channel is applied exactly once in its own formula: the stability shift is a single term in DMP-053, the cap is a single clamp, the service modifier is a single multiplication in DMP-097, the research adjustment is a single integer in DMP-089. No government effect is multiplicative with another government effect, with a technology, with a programme or with a policy. A second source of the same effect is **additive** and subject to the receiving system's cap.

**DMP-089 — The research adjustment is a flat integer.** *Provisional (REQ-283).* B-05's research rate is one point per standing institute (F-CI-020). A government may adjust it by a flat integer:

```
rp_per_turn = 0 if institutes_active = 0
              else max(0, institutes_active + research_adjustment)
```

The technocracy therefore produces **2** points from one institute and **4** from three; the junta produces **0** from one and **2** from three; every other government produces one per institute. The rule has three deliberate properties: it is an integer, not a percentage (so B-05's URB-101 "no percentage yield" still holds); it cannot create research without an institute (0 institutes → 0 points, so the technocracy cannot science its way past the building requirement); and it is floored at 0 (a junta with one institute is not a negative rate).

**DMP-090 — Policy permissions.** *Provisional (REQ-284).* A government may restrict which settings of the two policy axes are legal:

| Government | `POL-FISCAL` | `POL-ORDER` |
|---|---|---|
| Democracy | all three | `OPEN`, `BALANCED` |
| Constitutional monarchy | all three | all three |
| Absolute monarchy | all three | `BALANCED`, `FIRM` |
| Dictatorship | all three | `BALANCED`, `FIRM` |
| Military junta | all three | `FIRM` only |
| Technocracy | all three | `OPEN`, `BALANCED` |

A proposed policy that the government does not permit is rejected at validation, before any reservation, with the government named as the reason. The default policy of a new nation is `STANDARD` / `BALANCED`, except that a junta starts and remains `FIRM` (§16.3). No government restricts the fiscal axis, because tax-and-spend is an administrative choice rather than a constitutional one.

**DMP-091 — The caps are real and published.** *Provisional (REQ-285).* `stability_cap_bp` is never above B-04's 11,000 and never below 10,000; a government with a 10,600 cap can never reach the 110% tax multiplier a democracy can reach at very high approval. The cap is displayed on the selection screen and on the political panel. A future government may not have a cap above 11,000; a cap below 10,000 would make the government strictly worse than the neutral point and needs a compensating benefit in the same decision.

**DMP-092 — No military modifiers here.** *Provisional (REQ-285).* Prompt 10 owns warfare, units, readiness, Operations Points and combat. B-06 attaches **no** military effect to any government, including the junta. If Prompt 10 wants a military government advantage, it must propose it through a decision, state whether it is a new channel, and register the effect; it may not assume one from the junta's name.

**DMP-093 — No per-city or per-building modifiers.** *Provisional (REQ-285).* Every government effect is **nation-scoped**. A government does not change a city's capacity, housing, construction cost, building upkeep or research output per institute. This preserves B-05's rule that a modifier is either city-scoped (none at launch) or nation-scoped, and it keeps the interaction between government and city development legible: a government changes the national totals, not the local arithmetic.

---

## 15. National policy

**DMP-094 — The order axis.** *Provisional (REQ-286).* `POL-ORDER` has three settings. It changes the stability target once and six support values once:

| Setting | `order_stability_bp` | Labour | Rural | Industry | Commerce | Scholars | Security |
|---|---:|---:|---:|---:|---:|---:|---:|
| `OPEN` | −200 | +6 | −4 | +2 | +8 | +10 | −15 |
| `BALANCED` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `FIRM` | +300 | −6 | +4 | −2 | −8 | −10 | +15 |

`OPEN` is civil liberties: the academy and the trader gain, the security establishment loses, and administration is slightly harder. `FIRM` is public order: the security establishment gains, the academy and the trader lose, and administration is easier. Neither setting is "good": each buys one coalition at the expense of another, and the stability term is a real but bounded advantage (300 bp is 4.5 crowns per turn at 50,000 people and a 300 bp tax rate).

**DMP-095 — The fiscal axis.** *Provisional (REQ-286).* `POL-FISCAL` has three settings. It sets the tax rate and the public-service share together:

| Setting | `tax_bp` | `service_share_bp` | What the state is |
|---|---:|---:|---|
| `LOW` | 200 | 0 | A minimal state: low tax, no public services |
| `STANDARD` | 300 | 2,000 | A working state: the B-04 default rate, services at 20% of tax income |
| `HIGH` | 400 | 5,000 | A generous state: high tax, services at 50% of tax income |

The two are deliberately coupled. A player cannot run high tax with no services (extraction without a state) or low tax with generous services (spending without revenue). The three settings are the **only** tax rates a player may set at launch; B-04's `tax_rate_bp` is therefore 200, 300 or 400. Intermediate rates are rejected (DMP-016): a 25-bp slider would be 17 settings that no player can feel, and every one would need a stability and support curve.

**DMP-096 — Why two axes and not twelve.** *Provisional (REQ-286).* The brief lists twelve candidate policy areas. B-06 selects two and rejects the rest with reasons:

| Candidate area | Decision | Reason |
|---|---|---|
| Taxation and revenue | **Adopted** as `POL-FISCAL` | A real trade-off between revenue and coalition |
| Welfare and public services | **Adopted** inside `POL-FISCAL` | Coupled to tax so the state has a size, not two dials |
| Civil liberties and public order | **Adopted** as `POL-ORDER` | A real trade-off between coalitions and stability |
| Economic administration | Rejected | Would duplicate tax and services |
| Infrastructure investment | Rejected | B-05's construction decisions already are the investment policy |
| Education and research | Rejected | B-05's institutes and technologies already are the research policy |
| Industrial development | Rejected | B-05's facility choices already are the industrial policy |
| Agriculture and food security | Rejected | B-05's farms and B-04's food contract already are the food policy |
| Public employment | Rejected | No employment variable exists (DMP-043) |
| Regulation and commerce | Rejected | Would duplicate `POL-ORDER`'s commerce effect |
| Anti-corruption | Rejected | Would be a second stability term with no distinct decision |
| Permanent vs temporary policy | Rejected as a category | All policy is permanent until changed; the cooldown is the limit |

This is the answer to UD-009: **two axes, and stability multiplies tax income and nothing else.**

**DMP-097 — The public-service cost.** *Provisional (REQ-287).* The service cost is a **share of this turn's gross tax income**, not a per-capita charge:

```
service_cost_base = floor(tax_income × service_share_bp / 10,000)
service_cost      = ceil(service_cost_base × (10,000 + service_cost_mod_bp) / 10,000)
```

- `tax_income` is B-04's P3.1 result for this turn.
- `service_share_bp` is 0, 2,000 or 5,000 from the fiscal setting in force this turn.
- `service_cost_mod_bp` is the government's (DMP-087).
- The cost is charged at **P3.7** as a discretionary obligation, after maintenance, food, extraction, power, processing and readiness. It is an operating expense, not capex, and it is excluded from book value.
- If the unreserved treasury cannot pay it, the obligation is **cancelled**, `SERVICES_UNFUNDED` is set, the cost is not charged, and the effective service share for this settlement is zero (DMP-039).
- The cost cannot exceed tax income before the modifier, so it can never create a negative balance by itself; the modifier can push it above the base, which is why the affordability check runs on the **available** treasury.

A service share of 50% is deliberately expensive: at 50,000 people, `HIGH`'s 400 bp rate yields `tax_income` 200 and a 100-crown base cost, so `HIGH` nets **100** before other expenses while `STANDARD` nets **120** (DMP-168). The generous state is a political choice, not a revenue strategy.

**DMP-097a — The six tax quantities stay distinct.** *Provisional (REQ-287; ECN-177).* The brief requires the boundary between politics and the treasury to be explicit, so the player and the implementer see one owner per quantity:

| Quantity | Owner and formula | How B-06 policy enters | What B-06 must never do |
|---|---|---|---|
| Tax rate | B-06 chooses 200/300/400 bp; B-04's `tax_rate_bp` stores it (ECN-081) | The `POL-FISCAL` setting | Add a second rate, a rate modifier or a per-city rate |
| Gross tax income | B-04: `floor(population × tax_rate_bp × stability_bp / 1e9)` (ECN-094) | Only through `stability_bp` (F-PD-018) | Add a government or policy tax multiplier |
| Policy modifier | B-06's `service_cost_mod_bp`, applied once in F-PD-020 | The government's service-cost channel | Apply an approval, production or upkeep modifier through the tax line |
| Operating expenses | B-04 (ECN-097); the service cost is one named line | `service_cost` from F-PD-020 | Add an expense outside B-04's obligation order |
| Net operating income | B-04's derived report figure | Not a B-06 quantity; B-06 quotes it only in examples | Define a second net-income formula |
| Actual treasury change | B-04's closing-balance rule (ECN-101) and append-only ledger | Only via the service-cost entry `POLICY_SERVICE_COST` | Write crowns, refund a cancelled service or hold a balance |

A political event never writes a crown. The only political number that reaches the treasury is `stability_bp`, and the only political number that leaves it is the service cost.

**DMP-098 — Policy affects support, not approval directly.** *Provisional (REQ-288).* A policy setting enters the six support formulas (DMP-066…DMP-071) through `tax_bp`, `service_share_bp` and `order_*`. It has **no** direct approval term. A policy that pleases four groups and angers two moves approval by the weighted difference; the player can compute it. This is DMP-015 applied to policy: one path, no bonus on top.

**DMP-099 — Policy redistributes support; it does not manufacture it.** *Provisional (REQ-288).* The three fiscal settings produce almost the same weighted approval at the starting state — 56 (`LOW`), 55 (`STANDARD`) and 54 (`HIGH`) — while producing very different coalitions and very different revenue. The three order settings produce 57 (`OPEN`), 55 (`BALANCED`) and 53 (`FIRM`). A player cannot "buy" approval with a policy; they can choose **whose** approval they want, and pay for it in revenue or stability. This is the central balance rule of the policy system.

**DMP-100 — `SET_POLICY` is the only political action.** *Provisional (REQ-289).* The action has two parameters: the axis (`FISCAL` or `ORDER`) and the setting. It is submitted while the turn is `OPEN`, validated against the government's permissions (DMP-090), the cooldown (DMP-102) and the setting's existence, and resolved at **P4.3**. A malformed request, an illegal setting or a locked setting fails at validation with a named reason and changes nothing.

**DMP-101 — A policy change takes effect next turn.** *Provisional (REQ-289).* A change resolved at P4.3 of turn T is recorded on the nation and is **not** used by turn T's own P3, which has already run. It is used by every phase of turn T+1. This prevents a player from changing the fiscal setting after seeing the turn's food result and before the tax is recomputed, and it makes the P3/P4 order meaningful. The interface must show "effective from turn T+1" on the confirmation.

**DMP-102 — One change per axis per twelve turns.** *Provisional (REQ-290).* After a policy change resolves on an axis, that axis cannot be changed again for **12 turns** (one real day at 12 turns/day). The cooldown is per axis, so a player may change fiscal and order in the same turn, then neither for 12 turns. The cooldown is counted from the **resolution** turn, not the submission turn. A rejected or cancelled request does not start a cooldown. The remaining turns are displayed.

**DMP-103 — Policy changes are free.** *Provisional (REQ-290).* There is no crown cost, no material cost and no action point. The cooldown is the entire limit. A price would make policy a wealth sink, punish poor nations for experimenting and create a "pay to flip" dynamic; a cooldown limits the exploit (harvesting a support swing for one turn) without taxing the decision.

**DMP-104 — The limit is declared.** *Provisional (REQ-290; D-024).* B-02's subsystem contract requires every action to declare a visible limit. `SET_POLICY` declares: one change per axis per 12 turns, no cost, effective next turn. There is no hidden limit, no daily cap and no "political capital".

**DMP-105 — No policy stacking.** *Provisional (REQ-291).* Exactly one setting per axis is in force. There is no "active policies" list, no overlapping modifiers and no way to have `LOW` and `HIGH` simultaneously. A change replaces the previous setting; it does not add to it. The political state stores one value per axis, not a history of active effects (the history is in the event log).

**DMP-106 — Rejected: a policy for every ministry.** *Provisional (REQ-291).* Twelve ministries with twelve toggles would be twelve screens, twelve formulas and twelve ways to double-count the same effect. The brief asks for "only the categories that produce meaningful and distinct decisions"; two axes with three settings each produce nine combinations, each with a different coalition and a different revenue profile, and all nine are computable by hand.

**DMP-107 — Starting policy.** *Provisional (REQ-292).* Every new nation starts at `POL-FISCAL = STANDARD` and `POL-ORDER = BALANCED`, except a military junta, which starts at `FIRM` because `FIRM` is its only legal setting. The starting state is recorded with `policy_changed_turn = 0` on both axes, so the first change is available immediately.

**DMP-108 — Legality is checked against the government, not the player.** *Provisional (REQ-292).* A setting is legal if the government permits it (DMP-090). The check is server-side and runs before the cooldown check, so an illegal request never starts a cooldown. A client that displays a locked setting as available is a UI defect; the server still rejects it.

**DMP-109 — The forecast is part of the decision.** *Provisional (REQ-293).* Before submitting `SET_POLICY`, the player must be able to see the projected effect of each setting on: tax income, service cost, net operating income, each constituency's support, approval target, stability target and population growth. The projection uses the current state and is labelled a forecast. Without it, a policy choice is a guess, and DMP-017 is not satisfied.

**DMP-110 — Reversibility.** *Provisional (REQ-293).* Every policy setting can be changed back after the cooldown. There is no one-way policy, no permanent policy scar and no "reform lock". A nation that chooses `HIGH` and finds it unaffordable can return to `STANDARD` after 12 turns; the approval and stability consequences are gradual by construction (DMP-047/DMP-054), so the return is a curve, not a cliff.

**DMP-111 — No new resource, no new income.** *Provisional (REQ-293; DMP-008).* No policy creates a resource, a crown or a unit. The fiscal axis moves existing tax income and adds a cost; the order axis moves support and stability. Nothing in §15 changes B-04's conservation identity.

---
## 16. The political state and the settlement step

**DMP-112 — The political state record.** *Provisional (REQ-294).* One row per nation, holding exactly these fields. Every field has one owner (B-06 unless marked), one type and one update point.

| Field | Type | Range / values | Updated | Notes |
|---|---|---|---|---|
| `nation_id` | uuid | — | creation | Foreign key; one row per nation |
| `government_id` | enum | `gov_*` (six) | creation | **Immutable** (DMP-076) |
| `leader_name` | text | 1…40 characters | 06B | Display only; B-06 does not change it |
| `leadership_state` | enum | `NORMAL`, `ELECTORAL`, `SUCCESSION`, `TRANSITION`, `CRISIS`, `RECOVERY` | 06B | B-06 only defines the vocabulary (DMP-128) |
| `population` | integer | 1,000…no upper bound | P3.8 | §7 |
| `population_last_turn` | integer | ≥ 1,000 | P3.8 | For the digest delta |
| `approval` | integer | 0…100 | P3.8 | §9 |
| `approval_last_turn` | integer | 0…100 | P3.8 | For the digest delta and invariant 2 |
| `stability_bp` | integer | 5,000…`stability_cap_bp` | P3.8 | §10; `stability_factor_bp` for B-04 |
| `stability_last_turn` | integer | 5,000…`stability_cap_bp` | P3.8 | For the digest delta and invariant 3 |
| `support_labour` | integer | 0…100 | P3.8 | DMP-066 |
| `support_rural` | integer | 0…100 | P3.8 | DMP-067 |
| `support_industry` | integer | 0…100 | P3.8 | DMP-068 |
| `support_commerce` | integer | 0…100 | P3.8 | DMP-069 |
| `support_scholars` | integer | 0…100 | P3.8 | DMP-070 |
| `support_security` | integer | 0…100 | P3.8 | DMP-071 |
| `policy_fiscal` | enum | `LOW`, `STANDARD`, `HIGH` | P4.3 | §15 |
| `policy_order` | enum | `OPEN`, `BALANCED`, `FIRM` | P4.3 | §15 |
| `policy_fiscal_changed_turn` | integer | ≥ 0 | P4.3 | Cooldown anchor |
| `policy_order_changed_turn` | integer | ≥ 0 | P4.3 | Cooldown anchor |
| `legitimacy` | integer | 0…100 | derived | Not stored; computed on read (DMP-058) |
| `services_unfunded` | boolean | — | P3.7 | Set when the service cost is cancelled |
| `politics_settled_turn` | integer | ≥ 0 | P3.8 | Idempotency marker |
| `politics_version` | integer | ≥ 1 | creation | Formula-set version (DMP-123) |
| `next_contest_turn` | integer | ≥ 0 | 06B | The world turn on which the next election or confidence motion is due (F-PD-027) |
| `last_contest_turn` | integer | ≥ 0 | 06B | The turn of the last resolved contest; 0 before the first (F-PD-034) |
| `leadership_state_until_turn` | integer | ≥ 0 | 06B | The exclusive exit boundary for `TRANSITION`, `CRISIS` and `RECOVERY` (F-PD-038) |
| `pressure_turns` | integer | 0…12 | 06B | Consecutive turns of legitimacy below the government's control threshold (F-PD-037) |
| `challenge_immune_until_turn` | integer | ≥ 0 | 06B | No new non-electoral challenge before this turn (F-PD-041) |

`legitimacy` is listed for completeness but is **derived**, not persisted: storing it would create a second source of truth that could drift from the supports. Every other field is stored.

**DMP-113 — Values at nation creation.** *Provisional (REQ-295).* Nation creation (B-03 §7) writes:

1. `government_id` — the confirmed choice (DMP-083); no default.
2. `population = 50,000`.
3. `stability_bp = 10,000` — the neutral point, before the government's shift is felt.
4. `policy_fiscal = STANDARD`, `policy_order = BALANCED` (or `FIRM` for a junta).
5. `support_*` — computed from the starting state (B-04's standard bundle and B-05's standard capital) with the chosen policy.
6. `approval` — **equal to `approval_target` computed from those supports**, so the panel is internally consistent from the first turn. It is 55 for five governments and 53 for a junta (whose `FIRM` setting lowers three groups). It is not always 55.
7. `population_last_turn = 50,000`, `approval_last_turn = approval`, `stability_last_turn = 10,000`, `policy_*_changed_turn = 0`, `politics_settled_turn = 0`, `politics_version = 1`, `services_unfunded = false`.
8. `leadership_state = NORMAL`, `leader_name` — the name the player chose, or a generated default.

The creation transaction writes all of these once. A retry of nation creation that finds an existing nation for the account does **not** re-write them (D-032's uniqueness rule).

**DMP-114 — The settlement step is P3.8.** *Provisional (REQ-296).* Domestic politics resolves inside phase **P3 (Recurring)**, after P3.6 (food) and P3.7 (obligations), as the named sub-step **P3.8**. The order inside P3.8 is fixed:

1. **Read** the frozen opening state and the P3 results: `hunger_bp` (P3.6), `services_unfunded` and the funded service share (P3.7), funded civic centres and active institutes (B-05), capacity composition and warehouse headroom, and this turn's `approval` and `stability_bp` (**the values stored at the end of the previous turn**).
2. **Supports** — compute the six values from DMP-066…DMP-071. They use the **opening** `stability_bp`, not the value this step is about to compute, so the step is acyclic.
3. **Approval** — compute `approval_target` (DMP-046) and move `approval` by at most 5 (DMP-047).
4. **Stability** — compute `stability_target_bp` (DMP-053) using the **new** approval and move `stability_bp` by at most 250 (DMP-054).
5. **Population** — compute `growth_bp` (DMP-028) using the new approval, the post-settlement `hunger_bp`, the post-settlement housing for growth and the crowding state, then apply DMP-030/DMP-031.
6. **Write** the new values, the three `*_last_turn` mirrors, `politics_settled_turn = turn_id`, and the events of DMP-117.

Why after food and obligations: approval must see this turn's hunger and whether the services were actually paid. Why after tax: the tax already used the previous turn's stability, so the political step never rewrites an economic result. Why before P4: a policy change resolved at P4 must not affect the settlement that produced the state it is reacting to.

**DMP-115 — P3.8 is idempotent.** *Provisional (REQ-296).* The step writes a settlement marker `politics_settled_turn`. A resumed or retried settlement that finds `politics_settled_turn = turn_id` **reads the stored values and writes nothing**. It never recomputes supports from a changed state, never moves approval twice and never grows the population twice. The marker is written in the same transaction as the values, so a crash either leaves both or neither. This is B-02's checkpoint rule and B-04's exactly-once rule applied to politics.

**DMP-116 — One turn of lag, by design.** *Provisional (REQ-297).* Tax (P3.1) and food demand (P3.6) use the population and stability **stored at the end of the previous turn**. A political change therefore shows up in the economy exactly one turn later. The lag is not an accident: it makes the settlement order deterministic, prevents a P3.8 result from rewriting a P3.1 tax that has already been charged, and gives the player a full turn to see a forecast before it bites. The interface must state the lag ("your new stability applies from turn T+1").

**DMP-117 — Events written by P3.8.** *Provisional (REQ-298).* Each event has a unique key of the form `(turn_id, nation_id, event_type)` and is written once:

| Event | When | Payload |
|---|---|---|
| `APPROVAL_CHANGED` | approval moves | `from`, `to`, `target`, and the six support deltas |
| `STABILITY_CHANGED` | stability moves | `from`, `to`, `target`, and the six target terms |
| `SUPPORT_CHANGED` | any support moves | group, `from`, `to`, and the named terms that changed |
| `POPULATION_CHANGED` | population moves | `from`, `to`, `growth_bp`, and the term breakdown |
| `POPULATION_CAPPED` | growth is clipped by housing | `would_be`, `housing` |
| `CROWDING_DECLINE` | population is above housing | `excess`, `decline`, reason (`CIVIC_UNFUNDED` etc.) |
| `SERVICES_UNFUNDED` | the service cost is cancelled | `amount`, `tax_income` |
| `POLICY_CHANGED` | P4.3 resolves a change | axis, `from`, `to`, effective turn |
| `GOVERNMENT_CONFIRMED` | creation | `government_id` |
| `CAMPAIGN_OPENED` | 06B, campaign open | contest turn, challengers, campaign-action budget |
| `CAMPAIGN_ACTION` | 06B, action accepted | action id, target group(s), points, crowns, ledger key |
| `ELECTION_RESOLVED` | 06B, P4.4 | contest turn, candidate scores, winner, margin, formula version |
| `CONFIDENCE_RESOLVED` | 06B, P4.4 | motion turn, `confidence_bp`, threshold, outcome |
| `LEADERSHIP_CHANGED` | 06B | from/to holder, cause (`ELECTION`, `CONFIDENCE`, `PRESSURE`), contest turn |
| `PRESSURE_WARNING` | 06B | `legitimacy`, threshold, `pressure_turns` |
| `TRANSITION_STARTED` / `TRANSITION_ENDED` | 06B | boundary turn, cause |
| `CRISIS_STARTED` / `CRISIS_ENDED` | 06B | boundary turn, cause, early exit flag |
| `RECOVERY_STARTED` / `RECOVERY_ENDED` | 06B | boundary turn |

A settlement that changes nothing writes no event of that type. Events are class-P records where they affect a player's durable state (approval, stability, population, policy, government) and follow D-026's retention.

**DMP-118 — No ledger entry for people or sentiment.** *Provisional (REQ-298).* Population, approval, stability, support and legitimacy are **not** crowns or resources, so they do not enter B-04's append-only economic ledger (ECN-108…). The one exception is the public-service cost: it is an operating expense and is written to the economic ledger as `POLICY_SERVICE_COST` with the amount, the tax income it was derived from and the government modifier. A failed service payment writes `POLICY_SERVICE_CANCELLED`. The political events are a separate, append-only political log with the same no-edit rule.

**DMP-119 — What the digest reports.** *Provisional (REQ-299).* Every turn's digest contains a **Domestic** section with: population and its change; approval and its change, with the target; stability and its change; the six supports with their direction; the current policy and any change; and any special state (`POPULATION_CAPPED`, `CROWDING_DECLINE`, `SERVICES_UNFUNDED`, `NO_CONFIDENCE`, `DEPOPULATED`). A nation with no political movement gets one line stating that nothing moved and why (for example "approval unchanged: all six groups unchanged"). Silence is not an explanation.

**DMP-120 — Invariants.** *Provisional (REQ-299).* Checked at P7 for every nation-turn:

1. `1,000 ≤ population`.
2. `0 ≤ approval ≤ 100`, and `|approval − approval_last_turn| ≤ 5`.
3. `5,000 ≤ stability_bp ≤ stability_cap_bp ≤ 11,000`, and `|stability_bp − stability_last_turn| ≤ 250`.
4. Each support is an integer in 0…100.
5. `approval` equals the previous approval moved toward `approval_target` by the cap (not necessarily equal to the target).
6. `policy_fiscal` and `policy_order` are legal for `government_id`.
7. `government_id` has not changed since creation.
8. `population > housing` implies a `CROWDING_DECLINE` event exists for the turn, and `population ≤ housing` implies no crowding decline.
9. `legitimacy`, recomputed, is an integer in 0…100 and uses a vector that sums to 100.
10. No crown or resource was created by any political event.
11. `leadership_state` is one of the six values in DMP-128, and `leadership_state_until_turn = 0` unless the state is `TRANSITION`, `CRISIS` or `RECOVERY`.
12. `0 ≤ pressure_turns ≤ 12`, and `pressure_turns > 0` implies `legitimacy < control_threshold` for that government (F-PD-036).
13. A resolved contest appears **once** in the contest record for its `contest_turn`, and `last_contest_turn` is the greatest resolved turn.
14. `government_id` is unchanged after a contest, transition or crisis — the 06B layer never writes it (DMP-081).

A violated invariant is a **defect**, not a rounding difference: the turn is `INTERRUPTED` and the B-02 recovery path applies.

**DMP-121 — Recovery.** *Provisional (REQ-299).* A failed P3.8 resumes forward from its checkpoint. Because the step is a pure function of the frozen opening state and the P3 results, a resume produces the same values; the marker prevents a second application. If the failure happened after the values were written but before the events, the resume writes the missing events from the stored values and does not recompute them. If the failure happened before the values, nothing was written and the step runs once.

**DMP-122 — Administrative correction is a reversal.** *Provisional (REQ-300).* An operator may not edit `population`, `approval`, `stability_bp`, a support value, a policy or a government. A correction is an `ADJUSTMENT` event that names the original event, states the case and writes a compensating change with its own key. A correction may not set `government_id` to a different value (that is a new decision, DMP-077), and may not create population or approval without a recorded restitution. The same rule as B-04's ledger and B-05's assets.

**DMP-123 — Versioning.** *Provisional (REQ-300).* The political state records `politics_version`. A change to a formula constant or a support term creates a new version; existing nations are **not** retroactively recalculated. On the next settlement they use the new version and the change is disclosed in the digest. A change to `government_id`'s modifier row is a new decision and a new version; it must state whether existing nations of that government are migrated (and why) or keep the old row.

---

## 17. Interfaces for Prompt 06B

**DMP-124 — The input bundle.** *Provisional (REQ-301).* Prompt 06B may read, and must not recompute, the following at any boundary:

| Input | Source | Use in 06B |
|---|---|---|
| `government_id` | state | Selects the leadership process |
| `approval` | state | Electoral support and crisis pressure |
| `stability_bp` | state | Administrative capacity during a campaign or crisis |
| `legitimacy` | derived | Non-electoral retention |
| Six supports + weights | state / DMP-062 | Per-group vote or coalition calculation |
| `population` | state | Turnout base, if 06B adopts one |
| `policy_fiscal`, `policy_order` | state | Campaign issues and crisis triggers |
| `hunger_bp`, `housing_bp`, `crowding_bp` | B-04 / B-06 | Crisis severity inputs |
| `leadership_state` | state | Which process is running |
| `protection` / `dormant` | B-03 | Whether a political process is suspended |

**DMP-125 — Elections are 06B's formula, not 06A's.** *Provisional (REQ-301).* B-06 does not define vote share, turnout, candidate registration, campaign spending, the election interval or the consequence of losing. It supplies approval, the six supports and their fixed weights, and the state fields. 06B must publish its election formula in the same register (`F-PD-…`) and must state which of these inputs it uses and how. The brief's proposed 240-turn interval is **not adopted here**; it is a 06B decision.

**DMP-126 — Non-electoral retention is 06B's formula.** *Provisional (REQ-301).* B-06 supplies `legitimacy` and the institutional vectors (DMP-059). 06B decides whether a monarch, dictator or junta is removed when legitimacy falls, over what window, with what warning and with what consequence. The brief's proposed 24-turn consequence is **not adopted here**.

**DMP-127 — Crisis hooks are inputs, not triggers.** *Provisional (REQ-302).* B-06 exposes the conditions a crisis system may read — low approval, low stability, high hunger, crowding, an unfunded service, a policy change, a war (Prompt 10) — but defines **no** crisis, no unrest, no production penalty and no tax holiday. The brief's proposed 36–48 turn crisis and 75% production reduction are **not adopted here**; they are 06B decisions, and any production effect must be routed through B-04's batch and power rules rather than applied as a second multiplier.

**DMP-128 — The leadership-state vocabulary.** *Provisional (REQ-302).* Six states, one active at a time:

| State | Meaning | Who sets it |
|---|---|---|
| `NORMAL` | Ordinary administration | Default |
| `ELECTORAL` | A campaign or election window is open | 06B |
| `SUCCESSION` | A non-electoral leadership contest is running | 06B |
| `TRANSITION` | A decided handover is being executed | 06B |
| `CRISIS` | A political crisis restricts command | 06B |
| `RECOVERY` | The post-crisis recovery window | 06B |

Transitions between states are 06B's. B-06 requires only that (a) no state changes `government_id`, (b) a state has a published entry and exit condition, and (c) `NORMAL` is always reachable. These are candidate states; 06B may rename or merge them only by amending this table.

**DMP-129 — Reserved decisions.** *Provisional (REQ-303).* The following are explicitly **not decided** by B-06 and must be decided by 06B with its own evidence:

1. The election interval (proposed 240 turns).
2. Candidate registration and the campaign.
3. Vote calculation and turnout.
4. The consequence of losing an election (proposed 24 turns).
5. Retention rules for monarchies, dictatorships and juntas.
6. Unrest and political crisis (proposed 36–48 turns).
7. Any production or tax penalty during a crisis (proposed 75% production and zero tax).
8. Leadership-loss recovery and player access.
9. Whether a political process is suspended during a war or a reroll block.

B-06's silence on these is deliberate and must not be read as approval.

**DMP-130 — No double consequence.** *Provisional (REQ-303).* 06B may not attach a second consequence to a variable B-06 already uses. If it wants a stability penalty during a crisis, it must **change the stability target** through a published 06B term, not subtract stability a second time after B-06's formula. If it wants production to fall, it must change a B-04 input (capacity, power or batches), not multiply output after the fact. This is DMP-015 at the cross-prompt boundary.

**DMP-131 — The register is shared.** *Provisional (REQ-303).* 06B extends [`12_population_and_domestic_politics_formula_register.md`](12_population_and_domestic_politics_formula_register.md) with new `F-PD-…` rows. It does not create a second political register, a second approval formula or a second stability formula. A 06B formula that needs a new input must name its owner and add the input to DMP-065's table by amendment.

**DMP-132 — The political state is not a fourth status machine.** *Provisional (REQ-304).* B-03's three objects remain the account, the nation and the account pair (D-031). `leadership_state` is a **sub-state of the nation**, not a fourth object: it does not suspend an account, does not create a pair restriction and does not change `nation_status`. A nation in `CRISIS` is still `active` unless B-03 or Prompt 12 says otherwise. The interface must not present a crisis as a ban or an account sanction.

---

## 18. Cross-system contracts

**DMP-133 — Prompt 02 (turn system).** *Provisional (REQ-305).* B-06 declares, in B-02's subsystem contract: entities (political state, policy, government); actions (`SET_POLICY`); prerequisites (government permission, cooldown); costs (none); boundary phase (P3.8; policy at P4.3); ordering (DMP-114); effects (tax via stability, food demand via population, growth); failure (validation reasons; `SERVICES_UNFUNDED`); player results (DMP-119); visibility (§20); invariants (DMP-120); recovery (DMP-115/DMP-121); and validation (§26). No item is left to a later prompt without an owner.

**DMP-134 — Prompt 03 (account and nation lifecycle).** *Provisional (REQ-305).* Nation creation writes the political state once (DMP-113) and requires a confirmed government (DMP-083). A reroll destroys the state with the nation; the replacement re-chooses a government and receives a fresh state with no carry-over (DMP-009). Dormancy (D-028) suspends nothing political: the state continues to settle, because the world does not stop for an absent player. Protection (D-040) is a visibility/attack rule and has no political effect.

**DMP-135 — Prompt 04 (economy).** *Provisional (REQ-306).* B-04 owns food production, food consumption, `hunger_penalty_bp`, the tax formula, operating expenses, the austerity order and the ledger. B-06 supplies `population` and `stability_bp`, and adds the public-service cost as a P3.7 obligation. B-06 may not change ECN-080…091 or ECN-094…107. The P3.8 sub-step is added to B-04's P3 table as a pointer, with B-06 authoritative for its content. `POLICY_SERVICE_COST` and `POLICY_SERVICE_CANCELLED` are the only new economic ledger event types.

**DMP-136 — Prompt 05 (cities).** *Provisional (REQ-306).* B-05 owns housing, civic centres, institutes, `CIVIC_UNFUNDED`, `LAB_IDLE`, capacity, production mix and warehouse size. B-06 consumes `housing_growth`, `housing_bp`, `crowding_bp`, `food_share_bp`, `processing_share_bp`, `warehouse_bp`, `institutes_active` and the funded civic-centre count. B-06 may not add a building, change a housing formula or reinterpret a civic centre. B-05's F-CI-020 gains the government research adjustment (DMP-089) as a single integer; every other B-05 formula is unchanged.

**DMP-137 — Prompt 07 (trade and market).** *Provisional (REQ-307).* Trade moves crowns and resources, never people, approval or stability. A trade may not be used to buy approval, transfer a policy or move a political state. The market's prices and fees are Prompt 07's; B-06's reference prices are B-04's book values and are not a market promise.

**DMP-138 — Prompt 08 (diplomacy).** *Provisional (REQ-307).* A sanction may freeze a policy change (the action fails with a reference to the sanction) but may not change a government, delete a policy or create a negative balance. Aid moves crowns and resources, not approval or population. A diplomatic act may move a constituency support only through a **named 08 term** added to the support formula by a decision; B-06 provides no diplomatic modifier and no "prestige" input.

**DMP-139 — Prompt 09 (alliances).** *Provisional (REQ-307).* An alliance may not hold a nation's political state, set its policy, choose its government or transfer approval, stability, legitimacy or population. An alliance pool may not be used by a restricted pair (D-035). Alliance membership may be displayed as a political fact but has **no** support or stability effect at launch; a later "alliance solidarity" modifier would need a decision and a named term.

**DMP-140 — Prompt 10 (warfare).** *Provisional (REQ-308).* War may move approval and supports only through terms Prompt 10 defines and registers (for example a war-weariness term in `support_labour`). B-06 supplies no combat modifier and attaches no military effect to a government (DMP-092). A war may change `leadership_state` only through 06B's rules. War mortality, if adopted, is a separate population term with its own decision; it may not be folded into `hunger_bp`.

**DMP-141 — Prompt 11 (events, rankings).** *Provisional (REQ-308).* An event may move a support through a **named event term** added to the formula by a decision, or grant a one-time approval change through the normal target-and-cap path; it may not set `approval` directly. A reward may not grant population, a policy, a government or legitimacy. Rankings may display approval and population as statistics but may not treat them as a score that can be bought (D-027).

**DMP-142 — Prompt 12 (administration).** *Provisional (REQ-309).* Prompt 12 owns the audit procedure, the retention policy beyond DMP-117, the sanctions ladder and the disclosure of political records. B-06's political log is append-only and class-P where it affects durable state; a correction is a linked reversal (DMP-122). No operator may edit the state directly.

**DMP-143 — Prompt 13 (interface).** *Provisional (REQ-309).* B-06 supplies the information contract (§20): what must be shown, at what precision, with what explanation, and what must be labelled a forecast. Prompt 13 owns layout, navigation and accessibility. A screen that shows an approval number without its target and causes does not satisfy B-06.

**DMP-144 — Prompt 14 (balance).** *Provisional (REQ-310).* Prompt 14 must simulate the six governments, the three fiscal settings, the three order settings, the growth curve and the service cost across new, developing and mature nations, and must test the no-dominant-government target (DMP-167). B-06's numbers are provisional; Prompt 14 may change a constant, not the structure, and must record every change.

**DMP-145 — Prompt 15 (assembly).** *Provisional (REQ-310).* B-06 enters the Bible as part B-06 and must be assembled with its register, its research report and its requirement/test rows. The assembly must not merge B-06's formulas with B-04's or B-05's; the ownership map (DMP-006) is the check.

**DMP-146 — The boundary in one table.** *Provisional (REQ-310).*

| B-06 owns | B-06 reads | B-06 must not |
|---|---|---|
| Population, growth, approval, stability, legitimacy, supports, government, policy | Food shortage, housing, institutes, capacity mix, warehouse, tax income | Change a B-04 formula, a B-05 cost, a resource, a crown, a building or a technology |
| P3.8 | P3.1–P3.7 results | Rewrite a P3.1 tax, a P3.5 batch or a P3.6 food result |
| The political state and its log | Account, nation and pair status | Create a fourth status machine, a sanction or a cooldown on reroll |
| The 06B input bundle | 06B outputs only as state transitions | Define an election, a crisis, a leader or a removal rule |

---
## 19. Fairness, security and anti-exploit

**DMP-147 — The server owns every political number.** *Provisional (REQ-311).* `population`, `approval`, `stability_bp`, `legitimacy`, every support value, every policy effect and every government modifier are computed on the server from the frozen state. A client may display a projection; a client-supplied population, approval, stability, support, policy effect, government modifier or cooldown value is ignored and the action is re-validated. No B-06 rule is enforced only in the interface. This is B-05's URB-135 applied to politics.

**DMP-148 — One evaluation per turn.** *Provisional (REQ-312).* P3.8 runs once and writes once (DMP-115). A retry, a resumed settlement, a duplicate scheduler firing or a manual re-run reads the stored result. The political log's unique key `(turn_id, nation_id, event_type)` makes a duplicate event impossible. A duplicate that would change a value is a defect and blocks publication (B-02's one-outcome rule).

**DMP-149 — Policy cannot be farmed.** *Provisional (REQ-313).* Four rules together prevent the obvious exploits:

| Exploit | Why it fails |
|---|---|
| Flip to `HIGH` for the service support, then back before the cost is charged | The change resolves at P4.3 and is effective only from T+1; the cost is charged in every turn the setting is in force (DMP-097), and the cooldown is 12 turns (DMP-102) |
| Flip policy every turn to harvest a support swing | Approval moves at most 5 points per turn (DMP-047) and the target is a weighted mean, so a one-turn flip cannot bank a swing |
| Change policy after seeing the food result but before tax | P3.8 and P3.1 have already run; the change is effective next turn (DMP-101) |
| Run `HIGH` services without paying | The cost is an obligation at P3.7; if unpaid, the service bonus is zero and `SERVICES_UNFUNDED` is recorded (DMP-039) |
| Stack two fiscal settings | One setting per axis (DMP-105); the state stores one value |

**DMP-150 — Government cannot be gamed.** *Provisional (REQ-314).* The government is chosen once, confirmed explicitly and stored immutably (DMP-076/DMP-083). There is no verb to change it (DMP-082). Repeated creation to fish for a start is bounded by the existing account rules: one active nation per account (D-032) and a total reset on reroll (D-059). B-06 adds **no** reroll cooldown, because D-039 forbids one; the protection is the loss of all progress, the creation confirmation and the audit trail. B-03's reroll review signal (RRL-030/UD-031) remains the detection route.

**DMP-151 — No duplicate benefit.** *Provisional (REQ-314).* A government's modifier is applied once (DMP-088). A policy's effect is applied once (DMP-098). A support term appears in exactly one formula (DMP-066…DMP-071). An approval change enters only through the target and the cap (DMP-046/DMP-047). A service cost is charged once (DMP-097). The invariant is checked by the verifier: two applications of the same term must change a worked example, and the verifier fails if they do not.

**DMP-152 — No hidden modifier.** *Provisional (REQ-314).* There is no "political difficulty", no secret new-player bonus, no hidden catch-up and no invisible penalty for inactivity. Every term in every formula is published in the register. A modifier that cannot be shown to the player does not exist.

**DMP-153 — The political log is append-only.** *Provisional (REQ-315).* Events are written once, never edited and never deleted inside the retention window (D-026). A correction is a linked `ADJUSTMENT` that names the original (DMP-122). The log records the actor (`SYSTEM` for P3.8, the account for `SET_POLICY`), the turn, the before and after values and the reason. A player can inspect their own history; a third party cannot (D-027's aggregate rule applies to any published statistic).

**DMP-154 — Abuse signals are behavioural, not political.** *Provisional (REQ-315).* A political pattern — always `FIRM`, never changing policy, changing policy exactly every 12 turns — is **not** an abuse signal. The only political abuse signals are the ones B-03 and Prompt 12 already own: multiple accounts, coordinated transfers and reroll farming. B-06 does not add a political sanction, a "sedition" flag or a penalty for opposition.

**DMP-155 — The exploit register.** *Provisional (REQ-316).*

| ID | Attempt | Control | Residual risk |
|---|---|---|---|
| PX-01 | Send a client-side approval or stability value | Server recomputes from the frozen state (DMP-147) | None known |
| PX-02 | Change government through a crafted request | No verb; creation-only; immutable column (DMP-082) | A database-level edit is an operator action and is audited |
| PX-03 | Replay a policy change | Unique event key; cooldown anchor (DMP-102/DMP-148) | None known |
| PX-04 | Farm a service bonus without paying | Obligation at P3.7; zero effective share if unpaid (DMP-039) | A nation that pays and then loses the service to a later failure sees the cost charged; documented |
| PX-05 | Use a trade or aid to move approval | No such transfer exists (DMP-137) | Prompt 08/09 must not add one without a decision |
| PX-06 | Reroll to escape a political low | Allowed and intended; the new nation starts at 55 approval and 10,000 stability with no progress (DMP-085) | Reroll frequency is B-03's review signal |
| PX-07 | Create many accounts to hold many governments | One active nation per account (D-032); multi-accounting prohibited (D-018) | Detection is behavioural and never perfect (D-018) |
| PX-08 | Crowd a rival's housing through a shared mechanism | No mechanism moves housing between nations | A future rule must be reviewed for this |
| PX-09 | Exploit the one-turn lag to dodge a tax rise | The lag is symmetric and published; a change is visible one turn before it bites (DMP-116) | Intended, not an exploit |
| PX-10 | Force a support value below 0 or above 100 | Clamp in every formula; invariant at P7 (DMP-120) | None known |

---

## 20. Player experience and interface requirements

**DMP-156 — The selection screen sells the trade, not the bonus.** *Provisional (REQ-317).* The government-selection screen (DMP-084) must show, for each government: leadership model and removal route; approval weight and what it means in plain language ("popularity matters a lot / little"); stability shift and cap; service cost; research adjustment; policy permissions; institutional vector; strategic identity in one sentence; and the sentence "permanent for this nation". The screen must not sort governments into tiers or label one "recommended". A comparison table is required; a wall of tooltips is not acceptable.

**DMP-157 — Explain every move.** *Provisional (REQ-317).* The political panel must show, for approval and stability, the current value, the target, the distance and the named terms that produced the target. For each constituency it must show the support, the weight, the change since last turn and every term with its value. The test is simple: a player who has never read this document must be able to explain, from the panel alone, why their approval fell after a famine. If they cannot, the panel is defective.

**DMP-158 — Permanent and temporary are visually distinct.** *Provisional (REQ-318).* A permanent government effect, an adjustable policy effect, a current condition (hunger, crowding, an unfunded service) and a forecast must be presented as four different kinds of thing, with different labels and different placement. A player must never mistake a government's permanent cap for a temporary penalty, or a forecast for a result.

**DMP-159 — Forecast before commitment.** *Provisional (REQ-318).* Every policy confirmation and every government selection must show a forecast: for policy, the projected tax income, service cost, net operating income, each support, approval target and stability target; for government, the first-turn stability and the long-run cap. The forecast must state its assumptions and must be labelled as an estimate (DMP-041).

**DMP-160 — A gradual first session.** *Provisional (REQ-319).* A new player meets politics in three steps: the **government choice** at creation (one screen, six options, the trade explained); the **first digest** (population, food, approval and stability, with one sentence each); and the **policy panel** (two axes, three settings, the forecast). Constituency detail is available from the first turn but is not required to play. No mechanic is hidden; only the presentation is staged. This follows the project's in-context teaching posture (F-010/PXE-016) and adds no gameplay difference between a guided and an unguided player.

**DMP-161 — New players are not trapped.** *Provisional (REQ-319).* Every government is playable from the standard start. No government begins with an unpayable service, a negative balance, a stability below 9,000 or an approval below 50. The worst starting position is the junta's 53 approval, which is a consequence of its own `FIRM` setting, is visible on the selection screen and is recoverable by policy after 12 turns. A new player who does nothing but feed their nation does not lose population or approval.

**DMP-162 — Absence is safe.** *Provisional (REQ-320).* A nation that is not logged in still settles: services are paid from tax income, approval and stability converge, population grows toward housing. Nothing requires a decision at a boundary. A dormant nation (D-028) keeps its political state and is not punished politically. The digest explains what happened while the player was away in one section (DMP-119).

**DMP-163 — Recovery is visible and actionable.** *Provisional (REQ-320).* When approval or stability is low, the panel must present at least three concrete recovery actions with their projected effect: fix food (if hunger), fund services (if `SERVICES_UNFUNDED`), change policy (if a setting is hurting a coalition), build housing (if crowded or capped). A warning without an action is not acceptable.

**DMP-164 — Accessible by construction.** *Provisional (REQ-321).* Support and approval are shown as integers with a text label ("55% — content"), not by colour alone. Direction is stated in words ("up 2", "down 5"), not only by an arrow or a colour. The panel must be usable with a keyboard and a screen reader. No number is shown to more than the precision the formulas use (no `54.73%`). These are requirements on Prompt 13, not suggestions.

---

## 21. Balance and progression

**DMP-165 — The balance target.** *Provisional (REQ-322).* No government is universally superior; each is the best choice in at least one condition or brings a capability the others cannot buy; the spread in steady-state net operating income between the best and worst government is **under 10%** at every approval level tested; and no policy setting is dominant on both revenue and approval.

**DMP-166 — The government comparison.** *Provisional (REQ-322).* Steady state, 50,000 people, `STANDARD` fiscal, `BALANCED` order (a junta is evaluated at its forced `FIRM`), stability at target:

| Approval | Democracy | Const. monarchy | Abs. monarchy | Dictatorship | Junta | Technocracy |
|---:|---:|---:|---:|---:|---:|---:|
| 40 | 113 | 119 | 122 | 119 | **123** | 114 |
| 55 | 119 | 123 | **125** | 123 | **125** | 118 |
| 70 | 124 | 126 | **128** | 126 | 126 | 123 |
| 85 | **130** | **130** | **130** | 129 | 126 | 127 |
| 100 | **132** | 131 | 130 | 131 | 126 | 131 |

Cells are **net operating income** (tax income minus the public-service cost) in crowns per turn; other operating costs are government-independent and are omitted because they cancel in the comparison. The pattern is the design: the junta and absolute monarchy lead at low approval, the field converges by 70, and the democracy and constitutional monarchy lead at high approval while the junta is capped. The spread is 10 crowns (8.1% of the best) at approval 40, 7 (5.6%) at 55, 5 (3.9%) at 70, 4 (3.1%) at 85 and 6 (4.5%) at 100 — inside the target everywhere. The technocracy is consistently below the fiscal leaders but produces one extra research point per turn, which the table cannot show; the junta is above the fiscal leaders at low approval but produces one fewer.

**DMP-167 — No government is dominant.** *Provisional (REQ-322).* The test is not "every government wins somewhere" but "no government wins everywhere". The junta does not: at approval 85 and 100 it is last, its research is the slowest and its policy is fixed. The democracy does not: at approval 40 it is last. The absolute monarchy does not: it is capped at 10,800 and its approval weight is 14, so a popular nation cannot convert its popularity into the same stability a democracy can. The constitutional monarchy is the flexible middle and never leads by more than 2 crowns, which is the intended "safe but not special" identity. The technocracy is never the fiscal best, which is why its research adjustment must be worth roughly 5–8 crowns per turn in research terms — a Prompt 14 question, not a B-06 claim.

**DMP-168 — Fiscal posture is a coalition choice, not an approval purchase.** *Provisional (REQ-323).* At the standard start, the three fiscal settings produce:

| Setting | Tax | Service cost | Net | Approval target | Coalition |
|---|---:|---:|---:|---:|---|
| `LOW` | 100 | 0 | **100** | 56 | Rural, industry and commerce; scholars and labour lose |
| `STANDARD` | 150 | 30 | **120** | 55 | Balanced |
| `HIGH` | 200 | 100 | **100** | 54 | Labour and scholars; commerce and industry lose |

The revenue-maximising setting is `STANDARD`; the approval-maximising setting is `LOW`; `HIGH` buys the labour/scholar coalition at the cost of revenue. A player cannot have the highest revenue and the most popular coalition at once, and no setting is best on all three columns. This is the policy equivalent of DMP-167 and is the answer to "which fiscal setting is optimal?" — none, in general.

**DMP-169 — Order is a stability-versus-coalition choice.** *Provisional (REQ-323).* `OPEN` gives up 200 bp of stability but gains about 2 approval points and buys scholars, commerce and labour; `FIRM` gains 300 bp of stability and loses about 2 approval points, buying security and rural support. For a government with a high approval weight (democracy, 32), the approval swing is worth about 64 bp of stability, so the net stability trade is much smaller than the headline 300 bp; for a junta (10) it is worth about 20 bp. The setting is therefore worth more to an authoritarian government in stability terms and more to a democracy in approval terms — which is exactly the intended asymmetry.

**DMP-170 — Growth pacing.** *Provisional (REQ-324).* At the standard start a nation is exactly housed, so population does not grow until housing is added. With 5,000 headroom, growth is 60 bp (300 people per turn, 3,600 per day); as headroom closes, the term falls and growth approaches 50 bp. A fully fed, fully housed nation with approval 70 grows at about 57 bp before the headroom term. A nation at a total food shortfall loses about 0.5% per turn. These rates are provisional; the shape (slow, housing-bound, food-sensitive) is the design.

**DMP-171 — 06B is the missing half of the balance.** *Provisional (REQ-324).* The comparison above prices only revenue and research. Approval's decisive consequences — losing an election, a leadership challenge, a crisis — are 06B's and are not in any number here. B-06 therefore claims only that the **economic** spread is inside the target and that no government is economically dominant; it does **not** claim the political balance is proven. Prompt 14 must re-run the comparison with 06B's consequences included, and Prompt 06B must not assume the economic table already justifies its thresholds.

---
## 22. Worked numerical examples

**DMP-172 — How to read the examples.** *Provisional (REQ-325).* Every example uses the formulas in this document and the accepted inputs from B-04 and B-05. All values are integers; every division is a floor unless a ceiling is written. "Standard start" means the D-063 bundle and the B-05 standard capital: 50,000 people, 50 infrastructure, housing 50,000, food capacity 3, coal 2, oil 1, iron 1, refining 1, a 2,000-unit warehouse holding 310 units, no institutes, `STANDARD` fiscal and `BALANCED` order. The arithmetic is re-checked by `qa_backups/verify_politics_numbers.py`; the checker, not this prose, is the regression guard.

### Example 1 — A new nation at creation

**Government and policy.** Constitutional monarchy; `STANDARD` (`tax 300`, `service share 2,000`); `BALANCED`. No hunger, no crowding, stability 10,000.

**Supports.** Using 48 as the base and DMP-066…DMP-071:

| Group | Terms | Support |
|---|---|---:|
| Labour | 48 + `floor(2,000/400)` = 5 + (`floor(10,000/500)` − 18) = 2 | **55** |
| Rural | 48 + 15 (food share 3,750/250) + 2 (services) | **65** |
| Industry | 48 + 5 (processing share 1,250/250) + 3 (warehouse 8,450/1,000 − 5) | **56** |
| Commerce | 48 + 3 (warehouse) | **51** |
| Scholars | 48 + 5 (services) | **53** |
| Security | 48 + 1 (services) | **49** |

**Approval.** `(55×30 + 65×15 + 56×20 + 51×15 + 53×10 + 49×10) / 100 = 5,530 / 100 = 55.3 → 55`. Because DMP-113 seeds approval at the target, the nation begins at **55%**.

**Stability.** `10,000 + (55−55)×22 + 200 = 10,200`. Creation stores the neutral **10,000**; the first settlement moves it by 200 (inside the 250 bp cap) to **10,200**.

**Legitimacy.** Constitutional-monarchy vector (10/20/15/15/20/20): `5.5 + 13.0 + 8.4 + 7.65 + 10.6 + 9.8 = 54.95 → 54`.

**Population and food.** Population 50,000; housing 50,000; `housing_bp = 10,000`; food demand `ceil(50,000/1,000) = 50`; food supply `3 × 20 = 60`; surplus 10. Growth 50 bp = 250 people, capped at housing, so **population stays 50,000**.

**Player sees.** "Population 50,000 (housed exactly). Approval 55%, stable. Stability 100%, rising to 102%. Food 60 produced, 50 eaten, 10 surplus. No housing headroom: build a civic centre or infrastructure to grow."

### Example 2 — Growth with housing headroom

**Inputs.** Population 50,000; capital infrastructure raised to 55, so `housing = 45,000 + 5,500 = 55,000`; approval 55; no hunger.

**Turn 1.** `headroom = 5,000`; `floor(5,000 × 100 / 50,000) = 10`, capped at 15, so the term is +10. `growth_bp = 50 + 0 + 10 = 60`. `delta = floor(50,000 × 60 / 10,000) = 300`. New population **50,300**.

**Turn 2.** `headroom = 4,700`; `floor(4,700 × 100 / 50,300) = 9`. `growth_bp = 59`; `delta = floor(50,300 × 59 / 10,000) = 296`. New population **50,596**.

**Player sees.** "Population 50,300 (+300). Growth 0.60%: 0.50% base, +0.10% housing headroom." The headroom term shrinks as the cap approaches, so growth eases instead of stopping abruptly.

### Example 3 — Growth capped by housing

**Inputs.** Population 50,000; housing 50,200; approval 55; no hunger.

`growth_bp = 50 + 0 + floor(200 × 100 / 50,000) = 50`. `delta = 250`, so the natural population would be 50,250. `min(50,250, 50,200) = 50,200`. New population **50,200 (+200)**; the missing 50 people are not stored.

**Event.** `POPULATION_CAPPED` with `would_be = 50,250`, `housing = 50,200`.

**Player sees.** "Population 50,200 (+200). Growth was capped by housing: 50 more people would have arrived. Build housing to keep growing."

### Example 4 — Food shortage slows and reverses growth

**Inputs.** Population 50,000; housing 55,000 (headroom term +10); approval 55.

| `hunger_bp` | Shortfall | `growth_bp` = 50 + 10 − `floor(hunger/30)` | Delta | Result |
|---:|---|---|---:|---:|
| 750 | 25% | 50 + 10 − 25 = **35** | +175 | 50,175 |
| 1,500 | 50% | 50 + 10 − 50 = **10** | +50 | 50,050 |
| 3,000 | 100% | 50 + 10 − 100 = **−40** | −200 | 49,800 |

**Player sees.** "Population 49,800 (−200). Growth −0.40%: 0.50% base, +0.10% housing, −1.00% famine." At the maximum shortfall the nation loses people even with housing available; the decline stops as soon as food is restored (DMP-032 has no memory).

### Example 5 — A policy change from `STANDARD` to `HIGH`

**Inputs.** Standard start, stability 10,000, approval 55.

| | `STANDARD` | `HIGH` | Difference |
|---|---:|---:|---:|
| Tax rate | 300 | 400 | +100 bp |
| Service share | 2,000 | 5,000 | +3,000 bp |
| Tax income | 150 | 200 | +50 |
| Service cost | 30 | 100 | +70 |
| Net operating income | **120** | **100** | **−20** |
| Labour support | 55 | 59 | +4 |
| Rural support | 65 | 63 | −2 |
| Industry support | 56 | 49 | −7 |
| Commerce support | 51 | 42 | −9 |
| Scholar support | 53 | 58 | +5 |
| Security support | 49 | 50 | +1 |
| Approval target | 55 | **54** | −1 |

**Result.** The change is submitted during turn T, resolves at P4.3 and is effective in turn T+1. Approval moves from 55 to 54 (one point, inside the 5-point cap). The player has traded 20 crowns per turn and the commerce/industry coalition for the labour/scholar coalition and a larger state. The tax term explains the exact sizes: labour gains 4, scholars 5, while industry loses 7 and commerce 9.

**Player sees.** "Fiscal posture: `HIGH`. Tax 40%, services 50% of tax income. Net income 100 (was 120). Labour +4, scholars +5, commerce −9, industry −7. Approval target 54%. Effective turn T+1."

### Example 6 — Approval rises when a famine ends

**Inputs.** Constitutional monarchy, `STANDARD`, `BALANCED`; population 50,000; housing 55,000; approval 48; `hunger_bp` 1,500 (the target under that state is 48, so approval is at rest).

**Famine ends.** `hunger_bp` 0. Supports return to 55/65/56/51/53/49, target 55. `approval_next = 48 + min(55−48, 5) = 53`. The following turn: `53 + min(2, 5) = 55`.

**Player sees.** "Approval 53% (+5, target 55%). Food security restored: labour +15, rural +10, security +7. Approval will reach 55% next turn."

### Example 7 — Approval falls when a famine begins

**Inputs.** The same nation at approval 55, no hunger, then `hunger_bp` 3,000.

Supports become labour 25, rural 45, industry 56, commerce 51, scholars 53, security 34. Weighted: `750 + 675 + 1,120 + 765 + 530 + 340 = 4,180 / 100 = 41`.

`approval_next = 55 + max(41−55, −5) = 50`. Turn 2: `50 − 5 = 45`. Turn 3: `45 − 4 = 41`.

**Player sees.** "Approval 50% (−5, target 41%). Famine: labour −30, rural −20, security −15. Approval is falling toward 41%."

### Example 8 — Three constituency supports in a developed nation

**Inputs.** Population 140,000; housing 161,000 (`housing_bp = 10,000`); food capacity 8 of production capacity 24 (`food_share_bp = 3,333`); processing 5 of 24 (`processing_share_bp = 2,083`); warehouse free 1,200 of 4,000 (`warehouse_bp = 3,000`); 3 active institutes; stability 10,400; `STANDARD`; `BALANCED`; no hunger.

| Group | Calculation | Support |
|---|---|---:|
| Labour | 48 + 5 + 2 | **55** |
| Rural | 48 + `floor(3,333/250)` = 13 + 2 + `floor(400/500)` = 0 | **63** |
| Industry | 48 + `floor(2,083/250)` = 8 + `floor(3,000/1,000) − 5` = −2 + `floor(400/400)` = 1 | **55** |
| Commerce | 48 − 2 + 1 | **47** |
| Scholars | 48 + `min(12, 9)` = 9 + 5 | **62** |
| Security | 48 + 0 + 1 | **50** |

**Approval.** `55×30 + 63×15 + 55×20 + 47×15 + 62×10 + 50×10 = 1,650 + 945 + 1,100 + 705 + 620 + 500 = 5,520`; `floor(5,520/100) = 55`.

**Treasury.** Stability 10,400: `tax = floor(140,000 × 300 × 10,400 / 1e9) = 436`; service `floor(436 × 2,000/10,000) = 87`; net **349** before other operating costs.

**Player sees.** Three groups, three different stories: labour is held up by services and housing, rural by the food share, industry by processing and logistics, scholars by institutes, commerce by a thin warehouse margin.

### Example 9 — Aggregating constituency influence

**Inputs.** The supports of Example 1 and the fixed weights 30/15/20/15/10/10.

`Σ support × weight = 55×30 + 65×15 + 56×20 + 51×15 + 53×10 + 49×10 = 1,650 + 975 + 1,120 + 765 + 530 + 490 = 5,530`.

`approval_target = floor(5,530 / 100) = 55`.

**Why the weights are fixed.** If industry's weight rose with the number of factories, the same six supports would produce a different approval and a different election result without the player changing a policy. A player could not predict a vote without modelling the whole production mix, and DMP-017 would fail. The weights sum to exactly 100, so the aggregation is a true weighted mean and cannot exceed the highest support or fall below the lowest.

### Example 10 — Two governments at the same state

**Inputs.** Population 50,000; `STANDARD`; no hunger; approval 60. The junta is evaluated at its forced `FIRM`.

| | Democracy | Military junta |
|---|---:|---:|
| `approval_weight_bp` | 32 | 10 |
| `stability_shift_bp` | −100 | +250 |
| Order term | 0 (`BALANCED`) | +300 (`FIRM`) |
| Stability target | 10,000 + 5×32 − 100 = **10,060** | 10,000 + 5×10 + 250 + 300 = 10,600 → cap **10,600** |
| Tax income | 150 | 159 |
| Service cost | 30 | 33 (`ceil(31 × 1.05)`) |
| Net | **120** | **126** |
| Research per institute | 1 | 0 |

The democracy overtakes at **approval 75** — the first point at which its stability target (10,540) yields tax 158 and net 127 — and at approval 90 it reaches its 11,000 cap and nets **132**, while the junta stays capped at 10,600 and nets 126. The junta never reaches the democracy's ceiling. That is the intended trade: the junta is stable when unpopular and capped when popular; the democracy is weak when unpopular and the strongest when loved.

### Example 11 — A government and a research modifier, applied once

**Inputs.** One active institute; the B-05 rate is one point per institute.

| Government | `research_adjustment` | Formula | Points |
|---|---:|---|---:|
| Technocracy | +1 | 1 + 1 | **2** |
| Constitutional monarchy | 0 | 1 + 0 | **1** |
| Military junta | −1 | max(0, 1 − 1) | **0** |

With three institutes: technocracy **4**, constitutional monarchy **3**, junta **2**. With zero institutes every government produces **0**, including the technocracy, because DMP-089 gates the adjustment on a standing institute.

**No percentage.** A "+20% research" rule would give `floor(1 × 1.2) = 1` at one institute and `floor(3 × 1.2) = 3` at three — no effect at either count. The flat integer is the only form that is visible, integer and compatible with B-05's no-percentage rule. It is applied **once**, in F-CI-020; it does not also multiply the points generated, the project progress or the pool.

### Example 12 — A policy change with treasury consequences and a one-turn delay

**Inputs.** Standard start; opening treasury 1,529 (B-04 Example 2's closing balance); `STANDARD`; stability 10,000; approval 55. Other operating costs are omitted because they do not change.

**Turn T.** The player submits `SET_POLICY(FISCAL, HIGH)` while the turn is open. P3 of turn T still uses `STANDARD`: tax 150, service 30, **net +120**. Treasury after P3: 1,649. P4.3 resolves the change; `policy_fiscal_changed_turn = T`.

**Turn T+1.** P3.1 uses the new rate 400 and the stability stored at the end of T (10,000): tax `floor(50,000 × 400 × 10,000/1e9) = 200`. P3.7 charges `floor(200 × 5,000/10,000) = 100`. **Net +100**. Treasury after P3: 1,749.

**Cooldown.** The axis may next be changed on turn T+12; turns T+1…T+11 are blocked and the panel shows the remaining turns.

**Player sees.** "Fiscal posture changed to `HIGH`. It applies from turn T+1. Next change available on turn T+12." The player cannot change the rate after seeing turn T's food result and before turn T's tax, because turn T's tax already ran.

### Example 13 — Selecting a government: the technocracy panel

**What the player sees before confirming.**

| Field | Value |
|---|---|
| Leadership | Appointment by peer institutions; removal is a 06B process |
| Approval weight | 24 bp per point — popularity matters more than in a monarchy, less than in a democracy |
| Stability shift | −150 bp |
| Stability cap | 10,900 bp (109%) |
| Service cost | no modifier |
| Research | **+1 point per turn while at least one institute stands** |
| Fiscal policy | all three settings |
| Order policy | `OPEN` or `BALANCED`; `FIRM` is not legal |
| Institutional vector | labour 5, industry 15, commerce 5, scholars 65, security 10 |
| Stability at creation | 10,000; first settlement 9,750 (the 250 bp cap), target 9,850 reached on the second |
| Identity | "Government by appointed experts: the strongest research in the game, a weaker tax base, and no taste for repression." |
| Warning | "Permanent. You cannot change this government later; a different government requires a new nation." |

**Legitimacy at the standard start.** Supports 55/65/56/51/53/49 with the vector above: `2.75 + 8.4 + 2.55 + 34.45 + 4.9 = 53.05 → 53`. The technocracy is legitimate when its academies are content, not when the crowd is.

### Example 14 — A delayed policy change, step by step

**Timeline.** Turn T is open. At 11:40Z the player submits `SET_POLICY(ORDER, OPEN)`. The action is validated (democracy permits `OPEN`; the order axis has no cooldown) and recorded as pending.

- **P1 (freeze):** the action is in the accepted set.
- **P2 (revalidate):** the government permission and the cooldown are re-checked against the frozen state.
- **P3 (recurring):** the **old** setting (`BALANCED`) is in force. Supports, approval and stability settle with `order_stability_bp = 0` and zero order support terms.
- **P4.3 (orders):** the change resolves. `policy_order = OPEN`, `policy_order_changed_turn = T`, `POLICY_CHANGED` is written.
- **Turn T+1 P3:** the new setting is in force: stability target −200, scholars +10, commerce +8, security −15, and so on.

**Why not immediate.** An immediate change would let the player react to the digest of turn T inside turn T, and would make the P3/P4 ordering meaningless. The one-turn delay is the price of a deterministic settlement and is disclosed on the confirmation.

### Example 15 — A reroll does not carry political advantage

**Old nation.** Population 140,000; approval 41; stability 9,200; `HIGH`/`FIRM`; three completed technologies; legitimacy 58 under a dictatorship; a 12-turn policy cooldown anchor.

**Reroll (D-039).** The nation is retired. `NATION_RETIRED` closes its ledger. The political state is destroyed with it.

**New nation on the same account.** Chosen government (say constitutional monarchy); population **50,000**; approval **55** (the target of the starting state); stability **10,000**; `STANDARD`/`BALANCED`; no completed technology; legitimacy **54**; `policy_*_changed_turn = 0`; no protection re-grant; no asset, crown, resource or queue.

**What survives.** The account, its sanctions, any pair restriction, any open case and the audit history. The old nation's political record remains attributed to the old nation and is not deleted inside its retention window (D-026), but it cannot be used by the new nation.

**Player sees.** "Your new nation begins at 50,000 people, 55% approval and 100% stability. Nothing from your previous nation carries over."

### Example 16 — Long-run comparison across the six governments

**Steady state, 50,000 people, `STANDARD`, 120 turns (10 days).** Net operating income per turn from DMP-166 × 120:

| Government | Net/turn at approval 70 | 120-turn total | Research at 3 institutes |
|---|---:|---:|---:|
| Democracy | 124 | 14,880 | 3 |
| Constitutional monarchy | 126 | 15,120 | 3 |
| Absolute monarchy | 128 | 15,360 | 3 |
| Dictatorship | 126 | 15,120 | 3 |
| Military junta | 126 | 15,120 | 2 |
| Technocracy | 123 | 14,760 | 4 |

The fiscal spread over ten days is **600 crowns (4%)**, which is inside the 10% target. The technocracy gives up **600 crowns** against the absolute monarchy and gains **120 research points** over the same period — a quarter of the 448-point technology tree. The junta gives up **240 crowns** against the absolute monarchy and loses 120 points against its three-per-turn research. Those are the trades the table cannot price in crowns, and they are why no government is dominant (DMP-167).

### Example 17 — An unfunded service

**Inputs.** Standard start, `STANDARD`; tax 150; service cost `floor(150 × 2,000/10,000) = 30`. At P3.7 the unreserved treasury is 20 — enough for maintenance and food, not for the service.

**Result.** The obligation is cancelled, `SERVICES_UNFUNDED` is set, nothing is charged, and the effective service share for this settlement is **0**. Supports become labour 50, rural 63, industry 56, commerce 51, scholars 48, security 48; the weighted sum is `1,500 + 945 + 1,120 + 765 + 480 + 480 = 5,290 / 100 = 52`. Approval target **52**. The nation keeps its 30 crowns and loses the political benefit; it does not get both.

**Next turn.** If the treasury can pay, the service is funded and the supports return to 55/65/56/51/53/49. The digest states which turn was unfunded.

### Example 18 — Crowding after a civic centre goes unfunded

**Inputs.** Population 60,000; three cities housing 75,000, of which 25,000 is one civic centre. At P3.7 the centre's upkeep is unpaid, so `housing_growth = 50,000`.

`excess = 60,000 − 50,000 = 10,000`; `crowding_bp = min(10,000, floor(10,000 × 10,000/60,000)) = 1,666`; `decline = ceil(10,000/10) = 1,000`; new population **59,000**. The natural growth term would have added 204 people (`growth_bp = 50 − floor(1,666/100) = 34`), but the crowding decline is larger and is applied instead.

**Stability.** `−floor(1,666/10) = −166` bp in the target, plus the government's terms.

**Next turn.** Excess 9,000 → `crowding_bp` 1,500, decline 900. The excess falls by about 10% a turn, so **less than 1,000 people remain over the cap after 22 turns**; the last few hundred take longer, because the decline is proportional and never an eviction (DMP-031).

**Player sees.** "Population 59,000 (−1,000). You are 10,000 people over housing because a civic centre is unfunded. Fund it or build housing; nobody is evicted." This is the only route by which population falls without hunger, and it is always caused by a named, fixable condition.

---

---

## 23. Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-25 | First issue: the Prompt 06A foundation — population, food and housing interfaces, approval, stability, legitimacy, six constituencies, six governments and five channels, two policy axes, the political state and P3.8, the 06B interfaces, the exploit register, the UX requirements, the balance target and 18 worked examples |
| 1.1 | 2026-10-25 | Example 1 stores 10,000 and reaches 10,200 at the first settlement; Example 8's weighted sum corrected to 5,520; Example 10's junta service cost corrected to 33 (net 126) with the crossover at approval 75; DMP-031 describes the crowding excess as decaying 10% a turn rather than "converging" in 22 turns; register IDs reordered. No formula or coefficient changed |
| 1.2 | 2026-10-25 | Acceptance reconciliation: register ranges for F-PD-004…F-PD-009 replaced with the true term bounds (labour tax −3…+2, industry −7…+6, commerce −9…+8, stability terms −10/−13…+2, food and processing shares 0…+40, rural service 0…+5); DMP-066 drops the false "lowest tax sensitivity" claim; DMP-067/DMP-068 publish the +40 share maximum; DMP-094's 300 bp value corrected from 0.45 to 4.5 crowns; DMP-097's `HIGH` example corrected to tax 200, service 100, net 100; DMP-169 distinguishes the OPEN approval gain from the FIRM loss; Example 10's junta target corrected to 10,600; Example 16's technocracy and junta ten-day costs corrected to 600 and 240 crowns; DMP-166's approval-40 spread stated as 8.1% of the best; DMP-112 gains `approval_last_turn`, `stability_last_turn` and `politics_version`, with DMP-113's creation values and DMP-114's write step updated. Verifier extended to 234 checks |
| 1.4 | 2026-10-25 | Source synchronisation: every tax term in DMP-066…DMP-070 (Labour 40, Rural 20, Industry 15, Commerce 12, Scholars 50) now uses the authoritative signed `+ (300 − tax_bp) // divisor` already published by F-PD-004/005/006/007/008, replacing `− floor((tax_bp − 300) / divisor)`. No behaviour at the three policy settings, no range, constant, example or decision changed; this is the prose catching up with v1.3's register, and the verifier now checks the published blocks. |
| 1.3 | 2026-10-25 | Final micro-correction: F-PD-002 applies `max(1,000, raw)` after both the growth/cap and crowding paths (stated in the prose as **DMP-030a**, with the calculation order and the no-people-debt rule), so the 1,000-person example with approval 0, housing 45,000 and hunger 3,000 returns **1,000** instead of 993; the tax term for Labour, Industry and Commerce is the signed `(300 − tax_bp) // divisor`, restoring the published endpoints (−3…+2, −7…+6, −9…+8); DMP-071a publishes that behaviour; Example 5 supports become 59/63/49/42/58/50 (approval 54), DMP-099 and DMP-168's LOW approval becomes **56**, and D-091 records 56/55/54; requirements REQ-259, REQ-260 and REQ-275 now name the clamp and endpoints. No coefficient or design choice changed |

---

# Part II — The interactive political system (Prompt 06B)

## 24. Scope and the one abstraction that makes loss survivable

**DMP-173 — Part II completes Prompt 06.** *Provisional (REQ-326).* Sections 24–39 add elections, campaigns, leadership retention, political crises, unrest-equivalent consequences, recovery and the state machine that connects them. They **extend** Part I; they do not replace its population, approval, stability, legitimacy, constituency, government or policy rules. The formula register remains the single authority and grows by new `F-PD-` rows.

**DMP-174 — No second political economy.** *Provisional (REQ-326).* A political outcome may change exactly three things: **who holds executive authority**, **which actions the player may submit**, and **`political_stability_penalty_bp`** in DMP-053. It may not create a crown, a resource, a tax multiplier or a production multiplier. The rejected penalty models and their arithmetic are in §33.

**DMP-175 — The player is the nation's continuing leadership, not a mortal politician.** *Provisional (REQ-326).* This is the abstraction that lets a lost election cost something real without deleting twenty days of play. The account always remains the nation's controlling account. A contest decides **how much executive authority that account may exercise**, not whether the account still owns the nation. Losing an election opens a **12-turn TRANSITION**: the player keeps the account, the nation, its cities, its treasury, its alliance and its history, but cannot issue new executive orders while a caretaker administration runs the standing state. At the end of the transition the player resumes as the nation's leadership with the same government, a lower stability target and a recorded defeat.

The alternative — the player is a politician who leaves office for the rest of a 20-day term — is rejected because it would either require handing a nation to an AI for 240 turns or remove the player from the game for 20 days. Both are worse than the transition. The abstraction is stated openly in the interface: *"You are the nation's leadership. An election can take your mandate for a day; it never takes your nation."*

**DMP-176 — Part II does not decide later systems.** *Provisional (REQ-326).* Trade and market conduct (07), diplomacy (08), alliances (09), warfare and Operations Points (10), world events and rankings (11), moderation procedure (12), final screen layout (13) and final balance numbers (14) remain theirs. §36 states the contracts; it does not write those systems.

## 25. The election cycle

**DMP-177 — A 240-turn term, anchored per nation.** *Provisional (REQ-327; D-092).* An electoral government holds a contest every **240 shared world turns**. At two-hour turns that is:

```
240 × 2 = 480 hours = 20 days
```

The 240-turn proposal is **adopted unchanged**. The calendar is **staggered by nation**, not global:

```
next_contest_turn = creation_turn + 240                 (first contest)
next_contest_turn = scheduled_contest_turn + 240 × k    (every later contest)
```

`scheduled_contest_turn` is the turn the contest was **due** on. `resolved_contest_turn` is the turn it actually resolved; it is recorded for the audit and the explanation, but it **never anchors the next contest by itself**. `k` is the catch-up multiplier of DMP-181a: `k = 1` in the ordinary case, including every postponement an active nation can produce (a resolution at most 215 turns after the anchor still leaves a full campaign window at the next anchor); `k > 1` only when dormancy or protection postponed the contest so far that the next ordinary anchor could no longer deliver one.

A global election day was rejected: it would concentrate every democracy's campaign and every resolution into one boundary, and it would make the shared world's politics move in a single pulse. A per-nation anchor spreads the load and lets each nation's term begin when it was founded.

**DMP-178 — The cycle's five dates.** *Provisional (REQ-327).* All dates are world-turn IDs. `T` is `next_contest_turn`.

| Phase | Turn | What happens |
|---|---|---|
| Campaign opens | `campaign_open_turn` — `T − 24` when on time | `leadership_state = ELECTORAL`; the two challengers and their published scores appear; the campaign-action budget opens |
| Registration closes | `campaign_open_turn + 12` — `T − 12` when on time | No new candidate can appear; the ballot is fixed. The incumbent was nominated automatically at the opening |
| Final notice | `campaign_open_turn + 22` — `T − 2` when on time | The digest states the projected result and the actions still available |
| Campaign closes | the moment the resolution turn opens | For an on-time contest that is `T`; a postponed contest closes at its own resolution turn (DMP-181b). The last accepted action is the turn before |
| Resolution | **P4.4 of the resolution turn** (`T` when on time) | The contest is calculated, recorded and applied; at the next turn DMP-184 sets the state the result produced — the returned incumbent continues, or the defeated incumbent's account enters the 12-turn caretaker `TRANSITION` (DMP-175, DMP-207) |

The campaign is **24 turns (48 hours)**, not a single click and not the whole term. A player who logs in once during the window can still act; a player who is offline for the whole window stands with no campaign bonus and is not otherwise penalised.

**Preparation is not a postponement.** Every date in the table is derived from **`campaign_open_turn`**, which equals `scheduled_contest_turn − 24` only when the window opens on time. A campaign that opens late because the nation was ineligible at `T − 24` takes the same four offsets from its own opening (DMP-181b): a campaign opened at 980 for a contest due at 1000 closes registration at **992**, sends the final notice at **1002** and reaches its deadline at **1004**. It cannot be made to obey `T − 12`/`T − 2`, because those turns are already in its past. Entering `ELECTORAL` at `T − 24` **prepares** the contest; it is not a condition the due contest must clear, and it must never be read as one. A contest in `ELECTORAL` at `T` **resolves at the P4.4 of `T`** (DMP-181, DMP-236). Both resolving states are ordinary and the state table records both: a contest inside an open window resolves in `ELECTORAL`; one whose window has closed while resolution was still blocked resolves in `NORMAL` (DMP-181b). For a postponed contest every date moves with the window defined by DMP-181b — and the window is never opened in the past.

**DMP-179 — Which governments contest.** *Provisional (REQ-327).* Only two of the six governments hold a scheduled contest:

| Government | Contest | Electorate |
|---|---|---|
| `gov_democracy` | **Popular election** every 240 turns | The population weights (DMP-062) |
| `gov_constitutional_monarchy` | **Confidence motion** every 240 turns; the monarch remains head of state, the administration is what survives | The institutional vector (DMP-059) |
| `gov_absolute_monarchy` | No scheduled contest; continuous legitimacy pressure (§29) | — |
| `gov_dictatorship` | No scheduled contest; continuous pressure | — |
| `gov_military_junta` | No scheduled contest; continuous pressure | — |
| `gov_technocracy` | No scheduled contest; continuous peer pressure | — |

The constitutional monarchy is **not** treated as a popular election. Its head of state is hereditary; its administration is accountable to parliament. The same campaign actions are used, but the score is computed over the institutional vector, and the motion is a yes/no confidence question rather than a multi-candidate race.

**DMP-180 — The first contest.** *Provisional (REQ-328).* `next_contest_turn = creation_turn + 240`. A nation therefore has a full 20-day term before its first election or motion. B-03's creation protection and the tutorial both expire long before it. There is **no** early first election and **no** shortened term: a new player must not face a vote before they have governed.

**DMP-181 — Postponement, its states and its causes.** *Provisional (REQ-328).* A scheduled contest is **due** at `scheduled_contest_turn`. Its **campaign window** opens at the first turn at or after `scheduled_contest_turn − 24` on which the nation is **eligible**; it runs 24 turns to its deadline, and its **resolution turn** is the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)`. The opening is computed **once**:

```
campaign_open_turn = the first eligible turn ≥ scheduled_contest_turn − 24   (computed once)
window_deadline    = campaign_open_turn + 24
resolution_turn    = the first eligible turn ≥ max(scheduled_contest_turn, window_deadline)
```

**The opening is computed once, and only once.** `campaign_open_turn` is fixed the first time the nation is eligible; a blocking state that begins *after* the window has opened changes only *when* the contest may resolve, never the opening or its deadline. A window opened at `T − 24` and interrupted ten turns later still ends at `T`; the contest then resolves at the first eligible turn at or after `T` — not 24 turns after the interruption. A nation that was ineligible at `T − 24` is the other case entirely: its window has **not** opened, so it opens at the first eligible turn and runs a full 24 turns (DMP-181b). The two cases must never be conflated in an implementation, because the second opens a window and the first does not.

A nation is **eligible** when it is `active`, is not `dormant`, is not under B-03 protection, and `leadership_state` is **not** one of the three blocking states `TRANSITION`, `CRISIS` or `RECOVERY`. `NORMAL`, `ELECTORAL` and `SUCCESSION` are all **resolving states**: `ELECTORAL` is the state of an open window — where a scheduled contest is prepared and normally resolved — and it is never a condition the contest must clear. `SUCCESSION` is not a blocking state either: an unpopular monarch is still removable at the ballot or by the early motion. A contest is **never brought forward**, and it never resolves before `scheduled_contest_turn` (DMP-181b).

Four concepts are kept distinct, and every other rule in this section uses these words:

| Concept | Rule |
|---|---|
| **Preparation** | The campaign window opens — as early as `scheduled_contest_turn − 24`, or at the first eligible turn — and sets `leadership_state = ELECTORAL`. Preparation enables the campaign; it never blocks the contest |
| **Scheduled resolution** | At the resolution turn a contest whose nation is eligible resolves — normally in `ELECTORAL`; from `NORMAL` if the window has closed while resolution was still blocked |
| **Forced postponement** | Only a blocking state, dormancy, inactivity or protection delays a due contest: the window opens at the first eligible turn, and the contest resolves at the first eligible turn once its 24 turns have run and its anchor has passed, from the state as it stands then (DMP-181b) |
| **Early or exceptional challenge** | The constitutional monarchy's early motion (DMP-201) and the non-electoral challenges of DMP-218 are **not** scheduled contests: they never open a campaign window and never enter `ELECTORAL`, and their own eligibility rules are unaffected by this rule |

Postponement does not change the anchor: the next contest is derived from `scheduled_contest_turn`, never from `resolved_contest_turn`, by DMP-181a. An active nation's contest resolves as soon as the blocking state that delayed it clears. The longest single interruption the state machine can impose is a crisis (18 turns) followed by its recovery (12), so an active nation resolves at most **30 turns** after its anchor and still keeps `k = 1`; a nation dormant or protected for longer resolves after DMP-181b's window and then re-anchors (DMP-181a).

**DMP-181a — The catch-up rule: one resolution, and the first anchor that can still be delivered.** *Provisional (REQ-328).* A contest postponed for a long time must not leave the nation with an overdue election, a campaign whose deadlines are in the past, or a burst of catch-up elections. One rule prevents all three:

```
resolved_turn     = the resolution turn of the postponed contest (DMP-181)
k                 = ceil( (resolved_turn + 25 − scheduled_contest_turn) / 240 ),  k ≥ 1
next_contest_turn = scheduled_contest_turn + 240 × k
```

- `k = 1` is the ordinary case: a resolution on the anchor or up to 215 turns late keeps the original 240-turn cadence exactly.
- `k > 1` **skips the cycles that were wholly missed while the nation was unavailable.** Those elections are not held late and in a burst, and the nation does not receive the mandate they would have decided; it faces exactly one contest, and the schedule moves to the next anchor on the original grid.
- The **25-turn gap** guarantees that the next campaign window opens strictly after the resolution turn, so a returned nation's next campaign is never already past its deadlines.
- The anchor grid never drifts: every anchor is `creation_turn + 240 × n`, `n ≥ 1`, whatever the resolutions in between.

| Situation | Anchor | Resolved | `k` | Next contest |
|---|---:|---:|---:|---:|
| On time — eligible from `377 − 24` (window opens 353) | 377 | 377 | 1 | 617 |
| Blocked until 17 turns before the anchor (window opens 360) | 377 | 384 | 1 | 617 |
| Blocked until 10 turns after the anchor (window opens 387) | 377 | 411 | 1 | 617 |
| Returned after one fully missed cycle (window opens 700) | 377 | 724 | 2 | 857 |
| Returned after several cycles (window opens 2,700) | 377 | 2,724 | 10 | 2,777 |

**DMP-181b — One window per contest, opened as early as the rules allow, and never in the past.** *Provisional (REQ-328).* Every scheduled contest is prepared in **exactly one** campaign window of 24 turns. Where it opens depends only on when the nation becomes eligible:

- **Eligible at `anchor − 24` or earlier:** the published window, `anchor − 24` … `anchor`; resolution at the anchor (E21).
- **Eligibility begins inside what would have been the window** (0–24 turns before the anchor): the window opens at that first eligible turn and the contest resolves exactly 24 turns later — a postponement of at most 24 turns, never an acceleration, and never a window whose deadlines are already behind the nation.
- **Eligibility begins after the anchor** (long dormancy or protection): the same rule. The window opens at the first eligible turn, runs its 24 turns and the contest resolves at its end; the cycles wholly missed while the nation was unavailable are not re-run (DMP-181a moves the next anchor).
- **A blocking state inside an open window:** the clock does not restart, the opening does not move, and no second window is created. `window_deadline = campaign_open_turn + 24` is unchanged; campaign actions are rejected while the condition lasts (`CAMPAIGN_CLOSED`), actions already accepted stand, and the contest resolves at the first eligible turn **at or after** `max(scheduled_contest_turn, window_deadline)`. An interruption therefore delays resolution without ever extending the campaign, and a contest is never resolved before its anchor merely because a window closed early. The worked cases are 1000/976/990 → **1000** (block cleared before the anchor), 1000/976/1010 → **1010** (block cleared after it, not 1034), and 1000/980/— → open **980**, resolve **1004** (the window had not opened).
- **Two interruptions in one window:** each clears on its own turn; the deadline is still `campaign_open_turn + 24` and resolution still the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)`. Repeated evaluation of the same closed window returns the same turn and never advances the contest a second time (DMP-182).
- **Restoration before the deadline:** when the **last** blocking state clears while `window_deadline` is still ahead, `leadership_state` returns to **`ELECTORAL`**, not `NORMAL`. The opening, registration close, final notice and deadline are unchanged; actions already accepted and the ballot stand; the remaining turns are actionable again (DMP-183/DMP-236). A campaign that still has 10 turns left when a transition ends therefore has 10 turns left, not a closed window and not a new one.
- **Consecutive blockers leave no gap:** if a second blocking state begins on the turn the first would have cleared, there is no eligible turn between them, so no restoration occurs and no campaign action is accepted in the interval. `CRISIS` → `RECOVERY` is the ordinary case: the nation is never `ELECTORAL` between them. Restoration happens once, when the last blocker clears before the deadline.
- **The audit record** states `campaign_open_turn`, `scheduled_turn` and `resolved_turn`, and the state-restoration turn if any. There is no path that opens two windows for one contest, and no path that resolves one while its window is still open.

**DMP-182 — Exactly once, even when the job is late.** *Provisional (REQ-328).* The contest's identity is the pair **`(nation_id, scheduled_contest_turn)`**. The resolver writes a contest record with that key and sets `last_contest_turn`. A retry, a resumed settlement or a duplicate scheduler message finds the record and **returns it without recalculating**. If the boundary is processed late, the contest uses the state **at the boundary where it resolves**, not a reconstructed state from the due turn; the record states both `scheduled_turn` and `resolved_turn`, and the next anchor comes from `scheduled_turn` under DMP-181a. This is DMP-115's idempotency rule applied to contests.

**DMP-183 — Deadlines are turn boundaries, not wall-clock times.** *Provisional (REQ-329).* A campaign action is legal only while the target contest's window is open (`leadership_state = ELECTORAL`) and the current turn is before its **resolution turn** — for an on-time contest, `< T`. While a blocking state is active the submission is rejected (`CAMPAIGN_CLOSED`), but the window does not close: it is restored before `window_deadline` (DMP-181b). The submission is validated against the opening state of the turn in which it arrives. A request that arrives at the same moment as the resolution turn opens is **too late** and is rejected with `CAMPAIGN_CLOSED`; it is not silently applied to the next election. The server's turn ID, not the player's clock, decides.

**DMP-184 — What the player is told, and when.** *Provisional (REQ-329).* At `campaign_open_turn` (`T − 24` when on time): campaign opened, the two challengers, their published scores, the campaign budget and the projected result. At `campaign_open_turn + 12` (`T − 12` when on time): ballot fixed. At `campaign_open_turn + 22` (`T − 2` when on time): final projection and a warning if the incumbent is behind. At the resolution turn (`T` when on time): the result, the group-by-group table and the cause. At the next turn: the banner shows the state **the result produced** — `NORMAL` when the incumbent is returned, `TRANSITION` for **12 turns** with the 800 bp penalty when the incumbent loses (DMP-204, DMP-235; the 12 turns run from the turn after resolution and authority returns at the end of the 12th, DMP-210) — the term's first digest is published, and the date of the next contest is shown (DMP-178, DMP-181a). The account remains the nation's controller in both cases; on a loss the caretaker runs only the committed state and never receives the account or the nation (DMP-175, DMP-207). A postponed contest applies the same outcome rule: postponement moves the date, never the consequence.

## 26. Candidacy and the campaign

**DMP-185 — The incumbent, and two simulated challengers.** *Provisional (REQ-330; D-093).* The account's leader is nominated automatically. Two challengers stand against them:

| Candidate | Publication | Base score (bp) | What it represents |
|---|---|---|---|
| **Incumbent** | The player | `vote_bp` (F-PD-032) | The record of the administration |
| **Popular Front** | Simulated | `clamp(4,400 + (60 − approval) × 40, 3,600, 6,400)` | A protest vote against an unpopular government |
| **Institutional Bloc** | Simulated | `clamp(4,300 + (55 − legitimacy) × 30, 3,600, 6,400)` | An elite/establishment alternative |

The challengers are **not accounts, players, AI citizens or second nations**. They cannot be controlled, traded with, allied with or messaged. They are deterministic movements with a published platform, generated from the nation's own state. This is the only candidate model that respects D-032 (one account, one active nation): player-versus-player candidacy would require a second account inside one nation, which the account policy forbids.

**DMP-186 — The challengers are published, not hidden.** *Provisional (REQ-330).* At campaign open the player sees each challenger's name, one-line platform, current score and the formula that produces it. There is no fog: the player can compute the result before acting. Surprise is not a substitute for strategy.

**DMP-187 — Uncontested contests.** *Provisional (REQ-330).* A challenger **stands only if its score is at least 4,000 bp**. If neither qualifies — which requires a very popular and legitimate government — the incumbent is returned **unopposed**. The contest is still recorded, with `UNCONTESTED` as its outcome and no campaign spending required. An unopposed election is not a bug and not a mandate for anything beyond the ordinary term.

**DMP-188 — Who may not stand.** *Provisional (REQ-330).* The incumbent is ineligible while the nation is `dormant`, under B-03 protection, or in `TRANSITION`, `CRISIS` or `RECOVERY`; in those cases the contest is postponed (DMP-181). A challenger is ineligible if its computed score falls below 4,000. There is no player registration and no withdrawal: the ballot is fixed at the campaign's **`registration_close_turn`** (`campaign_open_turn + 12`; `T − 12` only when the campaign opened on time — DMP-178), and a candidate cannot leave it. A delayed campaign opened at 980 for a contest due at 1000 therefore fixes its ballot at **992**, not at the already-past 988.

**DMP-189 — Three campaign actions, no more.** *Provisional (REQ-331; D-094).* The launch roster is deliberately small. Each action has one strategic job:

| Action | Limit | Cost | Effect (campaign points) |
|---|---|---|---|
| `CAMPAIGN_PLATFORM` | once per contest | 0 | Allocate **6 points**, maximum **2 per group**, across **at least 3 groups** |
| `CAMPAIGN_RALLY` | once per contest | `2 × ceil(population / 1,000)` crowns | **+3 Labour, +2 Rural** |
| `CAMPAIGN_ADVERTISE` | up to **2** per contest | `3 × ceil(population / 1,000)` crowns each | **+2 Commerce, +2 Industry, +1 Scholars** |

No fourth action exists at launch. A "speech" button that adds +1 to everything would be a click, not a choice; the platform forces the player to decide **which coalition they are building**, and the two paid actions force a decision between **numbers and money**.

**DMP-190 — The platform is an allocation, not a button.** *Provisional (REQ-331).* The player distributes six points with a maximum of two per group and at least three groups represented. The allocation is submitted once and cannot be revised after the campaign's **`registration_close_turn`** — `T − 12` only for an on-time opening (DMP-178). A delayed campaign opened at 980 closes platform edits at **992**, not 988. It is recorded per group, so the election explanation can show exactly where each point went. The allocation is **ephemeral**: it affects this contest only and never edits a stored support value.

**DMP-191 — Paid actions scale with the nation, and are capped.** *Provisional (REQ-331).* Costs use `unit = ceil(population / 1,000)`: 100 and 150 crowns at 50,000 people; 1,000 and 1,500 at 500,000. The scaling prevents a mature treasury from buying a campaign a small nation cannot afford, and it keeps the campaign a real budget line rather than a rounding error. A campaign's maximum paid cost at 50,000 people is **400 crowns** (one rally + two adverts), against B-04's standard 1,500-crown opening treasury.

**DMP-192 — The bonus is capped and never compounds.** *Provisional (REQ-331).* `campaign_bonus_i` is the sum of the platform points, the rally and the adverts for group `i`, **clamped to 0…6**. It is added to `support_i` only inside the election formula (F-PD-031). It never changes `support_*`, `approval`, `stability_bp`, `legitimacy` or a policy. A second campaign in a later election starts from zero. This is DMP-130's no-double-consequence rule at the contest boundary.

**DMP-193 — Paid campaign money is charged once, at submission.** *Provisional (REQ-332).* A paid campaign action is validated, charged and recorded in the same transaction while the turn is `OPEN`:

1. Validate `leadership_state = ELECTORAL`, the per-contest limit, and `available_crowns ≥ cost`.
2. Charge the cost and write the B-04 ledger entry `CAMPAIGN_RALLY` or `CAMPAIGN_ADVERTISE` with the contest turn and action id.
3. Write the campaign-action row with a unique key `(nation_id, contest_turn, action_id, sequence)`.
4. Return the new campaign total and the projected vote.

There is no reservation and no cancellation: a campaign advertisement that has run cannot be un-run, and a rejected action charges nothing. A retry with the same key returns the stored row and does not charge twice. The action is ordinary operating expenditure, not capex, and it is never refunded.

**DMP-194 — Campaign promises are deferred, not forgotten.** *Provisional (REQ-333; D-102).* Binding promises were evaluated and are **not** adopted at launch. A promise needs a consequence for failure; the only honest channels are support (which would need a new support term and would double-count the policy that broke it) and stability (which would add a second political penalty on top of the crisis term). Both violate DMP-130. The platform declaration therefore expresses a **priority**, not a contract. A future revision may add promises together with a single new penalty channel and a decision; it may not smuggle one in as flavour text.

**DMP-195 — Campaign spending cannot buy an election.** *Provisional (REQ-334; D-095).* The maximum campaign swing is about **470 bp** (the weighted effect of six points on the highest-turnout groups plus the paid actions, all capped). The challenger formulas move by **40 bp per approval point** and **30 bp per legitimacy point**. A government that has lost 15 approval points therefore faces a challenger about 600 bp stronger, which no legal campaign can fully offset. Money can decide a close contest; it cannot reverse a failed term. The exact arithmetic is Example 26 and Example 27.

## 27. How the contest is calculated

**DMP-196 — Turnout weights are fixed, published and not the population weights.** *Provisional (REQ-335; D-096).* Elections are not a second approval score. Each group turns out at a different rate, and the election weights are the population weights multiplied by turnout and normalised to exactly 10,000 bp:

| Group | Population weight | Turnout factor | Election weight (bp) |
|---|---:|---:|---:|
| Labour | 30 | 9 | **2,443** |
| Rural producers | 15 | 13 | **1,765** |
| Industry | 20 | 11 | **1,991** |
| Commerce | 15 | 10 | **1,357** |
| Scholars | 10 | 15 | **1,358** |
| Security institutions | 10 | 12 | **1,086** |
| **Total** | **100** | — | **10,000** |

The weights are constants. They do **not** move with policy, population, cities or campaign spending. The design consequence is deliberate: rural producers and scholars turn out above their population share, labour below it, so a government that is popular in the cities can still lose if the countryside stays home. A player who ignores the difference between approval and the vote has missed the election.

**DMP-197 — Each group's election score.** *Provisional (REQ-335).*

```
election_score_i = clamp(support_i + campaign_bonus_i, 0, 100)
```

`support_i` is the P3.8 value; `campaign_bonus_i` is the capped 0…6 of DMP-192. The clamp is applied **after** the addition, so a group at 97 support cannot exceed 100 with advertising.

**DMP-198 — The incumbent's vote.** *Provisional (REQ-335).*

```
vote_bp = min(10,000, floor(Σ (election_weight_i × election_score_i) / 100) + 200)
```

The division by 100 converts `10,000 bp × 100 points` into basis points. The **+200 bp incumbency allowance** represents the advantage of holding office — name recognition, the state's information, the civil service. It is deliberately small: it is worth two approval points, not a term. It applies only when the player is the incumbent; a first contest after a transition still has it, because the player remains the nation's leadership (DMP-175).

**DMP-199 — The challengers' scores.** *Provisional (REQ-335).* As published in DMP-185:

```
popular_front_bp  = clamp(4,400 + (60 − approval) × 40, 3,600, 6,400)
institutional_bp  = clamp(4,300 + (55 − legitimacy) × 30, 3,600, 6,400)
```

`approval` and `legitimacy` are the values stored at the end of the previous turn, the same values the election explanation shows. There is no separate "campaign" for a challenger and no hidden momentum: the challenger is a function of the government's record.

**DMP-200 — The winner, and the tie-break order.** *Provisional (REQ-336).* The candidate with the highest `vote_bp` wins. Ties are broken in this fixed order, and the rule invoked is published with the result:

1. The **incumbent**, if the incumbent is tied for first.
2. The **higher approval** at resolution (the electorate's own ranking).
3. The **lower candidate index** (`incumbent = 0`, `popular_front = 1`, `institutional = 2`).

The order is total and deterministic. There is no coin flip and no hidden tie-breaker.

**DMP-201 — The constitutional monarchy's confidence motion.** *Provisional (REQ-336; D-097).* The monarchy's contest is a yes/no motion, not a race:

```
confidence_bp = Σ (institutional_weight_i × election_score_i)
```

`institutional_weight_i` is the government's vector from DMP-059 (it sums to 100), so `confidence_bp` is 0…10,000. The motion **carries** — the administration survives — when `confidence_bp ≥ 4,500`. It fails at 4,499 or below, and a failed motion opens a `TRANSITION` exactly as a lost election does. There is no incumbency allowance and no simulated challenger: the question is whether the institutions still support the administration.

A scheduled motion is **not tabled** when `legitimacy ≥ 70` at `campaign_open_turn` (`T − 24` when on time); the administration is returned automatically and the record states `CONFIDENCE_NOT_TABLED`. An **early motion** is tabled at the next P4.4 when `legitimacy < 45` for **12 consecutive turns** (the same pressure counter as §29), and it has **no campaign window**: the player has been warned for 24 hours and the institutions have already decided. An early motion is the constitutional monarchy's equivalent of a mid-term collapse; it is the price of a system that can remove an administration without a general election.

**DMP-202 — No randomness, and nothing hidden.** *Provisional (REQ-336).* The contest is a pure function of the stored political state, the campaign actions and the published constants. There is no random roll, no seed, no "momentum" and no last-minute event. Two servers computing the same inputs produce the same result. This is a deliberate rejection of the "surprise election" model: a player who loses must be able to see the arithmetic that beat them, and a player who wins must not be able to claim luck.

**DMP-203 — The audit record.** *Provisional (REQ-337).* Every resolved contest writes one append-only record:

| Field | Content |
|---|---|
| `nation_id`, `scheduled_turn`, `resolved_turn` | Identity and timing |
| `kind` | `ELECTION`, `CONFIDENCE`, `EARLY_MOTION` |
| `outcome` | `INCUMBENT`, `POPULAR_FRONT`, `INSTITUTIONAL`, `UNCONTESTED`, `CONFIDENCE_CARRIED`, `CONFIDENCE_FAILED`, `NOT_TABLED` |
| `scores` | The six `election_score_i`, the six weights, `vote_bp`, both challenger scores, `confidence_bp` where relevant |
| `campaign` | Every action id, its points and its crowns, with ledger keys |
| `state_in` | `approval`, `legitimacy`, six supports, `stability_bp`, policy, population |
| `formula_version` | `politics_version` at resolution |
| `tie_break` | The rule invoked, or `NONE` |

The record is immutable. A correction is a new adjustment record that names it (DMP-122's rule), not an edit.

**DMP-204 — Every edge case has one rule.** *Provisional (REQ-337).*

| Case | Rule |
|---|---|
| Incumbent wins | `leadership_state` returns to `NORMAL` at `T + 1`; no transition |
| Incumbent loses | `TRANSITION` from `T + 1` for 12 turns (§28) |
| Uncontested | Incumbent returned; record `UNCONTESTED`; no transition |
| Tie | DMP-200 order; the invoked rule is recorded |
| No valid challenger | Same as uncontested |
| Nation offline for the campaign | The incumbent stands with zero campaign bonus; the contest resolves; no additional penalty |
| Candidate withdrawal | Not possible after `campaign_open_turn + 12` (`T − 12` when on time); before it, only the player's platform can still change |
| Action at the deadline | Rejected with `CAMPAIGN_CLOSED`; nothing is charged |
| Election due while `ELECTORAL` | The contest **resolves** at the P4.4 of the resolution turn; `ELECTORAL` is the state that prepares and resolves a scheduled contest, never a postponement condition (DMP-181) |
| Blocking state, dormancy or protection at the anchor | Postponed to the first eligible window (DMP-181b); the next anchor comes from the scheduled turn, not the resolution turn (DMP-181a) |
| Window interrupted by a blocking state | Actions already accepted stand, further ones are rejected, the clock does not restart; `ELECTORAL` is restored for the remainder if the deadline is still ahead, and resolution follows at the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)` (DMP-181b) | |
| Return after long dormancy or protection | One 24-turn window from the return turn, one resolution at its end, and the first anchor that is still ahead (DMP-181a/181b) |
| Interrupted resolution | The `(nation_id, scheduled_turn)` record makes a retry a read |
| Repeated resolution request | Returns the stored record; no second calculation, charge or transition |
| Duplicate paid action | Unique key rejects the second; no second charge |
| Dormant nation | Contest postponed; no result is fabricated while dormant |

## 28. Losing an election: the 12-turn TRANSITION

**DMP-205 — The 24-turn lockout is rejected; the transition lasts 12 turns.** *Provisional (REQ-338; D-098).* The proposal would have made a losing player unable to operate the nation for 24 turns (48 hours). It was compared with four alternatives:

| Model | What it does | Verdict |
|---|---|---|
| **A — Complete executive lockout, 24 turns** | No ordinary executive action for 48 h | **Rejected.** It punishes the player's absence, not the defeat; it is longer than many players' weekly play time; and it makes a democracy a trap for a casual player |
| **B — Caretaker administration, 24 turns** | An automatic government runs the nation while the player is locked out | **Rejected as proposed.** The duration is the problem, not the caretaker; an AI that optimises for 48 h also hides the consequences from the player |
| **C — Limited executive powers, 24 turns** | The player keeps some actions, loses high-impact ones | **Rejected.** It keeps the 48-hour cost while blurring what the player may do; the restriction list becomes arbitrary |
| **D — Political transition, 12 turns** | The player keeps the account and the nation, loses new executive orders for 24 h, resumes with a stability scar | **Adopted.** It is a real cost (a day of construction, research, policy and military decisions), it is proportionate to a defeat, and it is recoverable |

The adopted rule is **12 turns (24 hours)**, not 24. A close loss and a landslide produce the same transition length: the player either has the mandate or does not. The margin is recorded and explained, but it does not shorten or lengthen the transition.

**DMP-206 — What is restricted, and what remains.** *Provisional (REQ-338).*

| Capability | During `TRANSITION` |
|---|---|
| Sign in, view the nation, read the digest and the contest record | **Available** |
| Alliance chat, diplomacy read, news, rankings | **Available** |
| Market *read* (prices, own orders, reservations) | **Available** |
| Submit construction, infrastructure, facility, research, programme or city-founding orders | **Blocked** (`EXECUTIVE_AUTHORITY_SUSPENDED`) |
| Change policy (`SET_POLICY`) | **Blocked** |
| Create or accept trade offers, sign or cancel treaties, change alliance permissions | **Blocked** by the 06B contract; Prompt 07/08/09 must honour the flag |
| New military orders or Operations Point spending | **Blocked** by the Prompt 10 contract |
| Reroll or delete the nation | **Available** (it destroys the nation; no political advantage survives) |
| Prepare for the next contest, read the challengers, plan a campaign | **Available** (campaign actions are not legal until the next `ELECTORAL` window) |

The restriction is on **new executive orders**, not on the account. No feature outside the executive catalogue may use the transition as a reason to deny access; that would turn a political defeat into an account sanction, which DMP-132 forbids.

**DMP-207 — The caretaker is narrow, and cannot create value.** *Provisional (REQ-339).* A caretaker administration runs only what is already committed:

1. Standing production policy and any batches already accepted.
2. Maintenance and upkeep, through B-04's normal obligation order.
3. Tax collection, food consumption and P3.8 political settlement.
4. Research already active, at its normal rate.
5. Construction already accepted and due to resolve, at its reserved cost.
6. Treaties and alliance commitments, unchanged.

It **may not**: start a new order, change a policy, change the production policy, accept or cancel a trade, sign or leave a treaty, spend Operations Points, declare war, or move crowns or resources between pools. It has no budget of its own and no discretion. It is a caretaker, not an AI player.

**DMP-208 — Reservations and queues survive.** *Provisional (REQ-339).* A reservation made before the transition remains valid and is consumed by its original order at its original resolution turn. A construction that resolves during the transition completes normally; a research project continues to accrue points. Nothing is cancelled because the player lost a vote. A reservation is not duplicated, extended or released by the transition; B-04's reservation identity is unchanged.

**DMP-209 — The economy does not stop and is not multiplied.** *Provisional (REQ-340).* Production, food, trade settlement and tax continue. There is **no production multiplier and no tax multiplier** during a transition. The only economic effect is the stability penalty `political_stability_penalty_bp = 800` (F-PD-026), which lowers the stability target and therefore tax through B-04's single tax formula. At the standard start the penalty costs at most **12 crowns per turn** once fully felt (Example 21); it does not threaten solvency.

**DMP-210 — Return is automatic and on time.** *Provisional (REQ-340).* At the P3.8 of the 12th transition turn, `leadership_state` returns to `NORMAL` and `leadership_state_until_turn` is cleared. The player's authority is restored at `T + 1` after that boundary, whether or not the player is online. A missed login does not extend the transition; a scheduler retry does not shorten it. The next scheduled contest is unchanged (`scheduled_turn + 240`); a transition does not reset the term.

**DMP-211 — No protection is re-granted.** *Provisional (REQ-340).* A lost election is not a new nation. B-03's creation protection, the standard starting bundle and the tutorial are **not** re-applied. The player keeps the nation's cities, technology, inventory, treasury and history; that is the point of DMP-175. A reroll during or after a transition is the ordinary instant reroll (D-039): it deletes the nation and creates a new one with the standard bundle, and it transfers no political state.

**DMP-212 — A loss is a loss, however narrow.** *Provisional (REQ-341).* There is no "close result" exception, no runoff and no second round. A 1 bp defeat opens the same transition as a 2,000 bp defeat. The record states the margin so the player can learn from it, but the rule does not soften because the margin is small. A runoff would double the campaign and give the incumbent a second chance that the first vote already denied.

**DMP-213 — The player is told why, on the night.** *Provisional (REQ-341).* The result screen shows: every candidate's score; the six group scores and weights; the contribution of each group to the winner's total; the campaign actions and their points; the approval and legitimacy used by the challengers; the tie-break if any; and one sentence naming the largest single cause ("the countryside turned against you: rural support fell 12 points and rural turnout is 17.65% of the electorate"). The audit record (DMP-203) is linked. A player who cannot explain the result has been failed by the interface, not by the dice.

**DMP-214 — The caretaker does not change policy for the player.** *Provisional (REQ-341).* The winning candidate's platform is **not** imposed during the transition. A forced policy change would let a player lose an election to escape a policy cooldown, and it would make the caretaker a second government. The platform is displayed as the mandate the player must now answer for in the next contest; it has no mechanical effect. This is the same boundary as DMP-194: a platform is a promise, not a policy.

## 29. Non-electoral governments: continuous retention

**DMP-215 — A monarchy is not safe for twenty days because no election is scheduled.** *Provisional (REQ-342; D-099).* The four non-electoral governments (absolute monarchy, dictatorship, military junta, technocracy) and the constitutional monarchy's early motion use a **continuous** test, evaluated at every P4.4. The test reads `legitimacy` — the support of the groups that can actually remove the ruler (DMP-058) — against a published threshold. A calendar would let an unpopular monarch govern unchallenged; a continuous test makes institutions respond to how the nation is run.

**DMP-216 — The control thresholds.** *Provisional (REQ-342).*

| Government | `control_threshold` (legitimacy) | Who can remove the ruler | Starting legitimacy | Cushion |
|---|---:|---|---:|---:|
| Absolute monarchy | **40** | Court, countryside, army | 54 | 14 |
| Dictatorship | **35** | Security apparatus, with industry | 52 | 17 |
| Military junta | **40** | Officer corps alone | 49 | 9 |
| Technocracy | **42** | Academies, with industry | 53 | 11 |
| Constitutional monarchy (early motion) | **45** | Parliament, court, countryside, officers | 54 | 9 |

The thresholds sit **below** every starting value by at least nine points. A new nation therefore begins safe, and the warning band (DMP-217) gives it a further visible margin. The junta has the smallest cushion because its legitimacy is security support alone; a junta that loses the army has lost everything, which is the point of its design.

**DMP-217 — The warning band is five points and it is visible.** *Provisional (REQ-343).* `leadership_state` enters `SUCCESSION` when `legitimacy < control_threshold + 5`. It returns to `NORMAL` when `legitimacy ≥ control_threshold + 5`. While in `SUCCESSION`:

- The digest names the government's institutional vector and the groups that are below their removal threshold.
- The political panel shows `pressure_turns / 12` and the exact legitimacy needed to reset it.
- A notification is sent at the first `SUCCESSION` turn and again at `pressure_turns = 6` and `11`.

The band is five points, not a percentage: it is one ordinary support change. A government that ignores the warning has been told twice.

**DMP-218 — Twelve consecutive turns below the threshold.** *Provisional (REQ-343).*

```
pressure_turns = pressure_turns + 1   if legitimacy < control_threshold
pressure_turns = 0                    if legitimacy ≥ control_threshold
```

The counter increments **after** the P3.8 settlement of the turn, at P4.4, using the legitimacy computed from that settlement's supports. It is capped at 12. At **12**, the challenge resolves in the same P4.4:

- **Absolute monarchy, dictatorship, military junta** → `CRISIS` (§30) for 18 turns. The fiction is a disputed succession, a coup or a command split.
- **Technocracy** → `TRANSITION` for 12 turns, as in §28. A peer review removes an appointed administration; it does not require a national emergency.
- **Constitutional monarchy early motion** → a confidence motion under DMP-201; if it fails, `TRANSITION`.

The challenge is **not random**. A government at 39 legitimacy facing a 40 threshold with 12 pressure turns loses control with certainty; one at 41 never accumulates pressure. The player can compute the exact turn of removal and act before it.

**DMP-219 — A warning that is answered is a warning, not a countdown to defeat.** *Provisional (REQ-343).* Every turn at or above the threshold resets `pressure_turns` to zero. A government that restores legitimacy at any point before the twelfth turn keeps control; the record states that the challenge was avoided and at which turn the counter reset. The state leaves `SUCCESSION` as soon as legitimacy is at least `threshold + 5`; between `threshold` and `threshold + 4` the state remains `SUCCESSION` but the counter is zero, because the ruler is safe but not comfortable.

**DMP-220 — There is no universal "stabilize" button.** *Provisional (REQ-344).* The interventions are the game's existing levers, and each addresses a different cause:

| Cause of low legitimacy | Intervention | Which group it moves |
|---|---|---|
| Hunger | Restore food capacity, imports or reserves | Rural, labour, security |
| Unfunded services | Raise the fiscal setting or restore the service payment | Labour, scholars, rural |
| Crowding | Fund civic centres or build housing | Labour |
| Repression | Change the order setting toward `BALANCED`/`OPEN` | Scholars, commerce |
| Over-taxation | Lower the fiscal setting | Industry, commerce |
| Weak institutional support | Build the group's economic base (farms, industry, institutes) | The relevant vector group |

A generic "grant concession" action was rejected: it would be a fifth resource and would let a player skip the economic cause. The player stabilizes by governing, not by clicking a loyalty button.

**DMP-221 — The ruler may change; the government may not.** *Provisional (REQ-344).* A lost challenge in an absolute monarchy is a **disputed succession within the monarchy**, not a revolution. The government remains `gov_absolute_monarchy`; the player remains the account; the crisis ends with the same dynasty (or the player's chosen leader name) restored. No `government_id` write exists (DMP-081).

**DMP-222 — Dormancy and protection freeze the counter.** *Provisional (REQ-344).* While a nation is `dormant` or under B-03 protection, `pressure_turns` does not increment, no challenge resolves and no contest is tabled. The counter resumes at the first active turn. A player who is away is not removed by a clock; a player who is present and ignores the warning is. A postponed contest opens its single 24-turn window at the first active turn and resolves at the end of it (DMP-181b), and the next anchor is recomputed by DMP-181a — so a long absence can never leave an overdue contest, a campaign whose deadlines are in the past or a burst of catch-up elections behind it.

**DMP-223 — A recovery buys time, not immunity for ever.** *Provisional (REQ-345).* After a `CRISIS` ends (or a technocracy's transition ends), `challenge_immune_until_turn = end_turn + 24` and `pressure_turns = 0`. During immunity a new challenge cannot resolve, but legitimacy is still displayed and the warning band still applies; the government can be unpopular without immediately facing a second removal. The immunity is **48 hours**, one fifth of an election term. It prevents a death spiral, not accountability.

**DMP-224 — The warning is not a penalty.** *Provisional (REQ-345).* `SUCCESSION` changes no economic value, blocks no action and adds no stability term. It is a **state of information**, so that a player can see the risk before it becomes a crisis. Only `TRANSITION`, `CRISIS` and `RECOVERY` carry the stability penalty (F-PD-026). This is deliberate: a warning that hurts would make the warning itself the punishment.

## 30. Political crisis and recovery

**DMP-225 — A crisis is 18 turns of suspended authority, not an economic shutdown.** *Provisional (REQ-346; D-100).* When a non-electoral ruler loses control (§29), the nation enters `CRISIS` for **18 turns (36 hours)**. During it:

- The player may not issue new executive orders (the same list as DMP-206).
- A caretaker runs the standing state exactly as in DMP-207.
- **Production continues unchanged.** No batch is cancelled, no capacity is derated, no output multiplier is applied.
- **Tax continues unchanged**, through B-04's single formula; the only political effect is `political_stability_penalty_bp = 1,500`.
- Food consumption, upkeep, trade settlement and existing queues continue.
- The player keeps the account, the nation, its assets, its alliance and its records.

The crisis costs **authority and stability**, not inventory. A coup does not burn the factories, and a disputed succession does not stop the harvest. This is the central rejection of the brief's 75%-production/zero-tax model: those penalties would destroy the nation that the political system is supposed to make worth governing.

**DMP-226 — Why 18 turns, not 36–48.** *Provisional (REQ-346).* Eighteen turns is **36 hours** — one and a half days. It is long enough to be a real interruption (three construction windows, eighteen research turns, eighteen chances to be attacked) and short enough that a player who logs in daily loses one day, not a week. The proposed 36–48 turns are 72–96 hours; §33 shows that they also empty the treasury and starve the population under the accepted economy. The duration was reduced first, and the economic multipliers were removed entirely, because the multipliers were the part that made the proposal unsurvivable.

**DMP-227 — What the player may still do.** *Provisional (REQ-347).* The permitted list is DMP-206's: sign in, view the nation and the crisis record, chat, read diplomacy and news, read the market, reroll or delete, and plan. The blocked list is also DMP-206's: no new construction, research, programme, facility, city, policy, trade, treaty or military order. Campaign actions are not legal because `leadership_state != ELECTORAL`.

**DMP-228 — A crisis can end early, and the player can see how.** *Provisional (REQ-347).* At the P4.4 of any crisis turn **at or after turn 6**, the crisis ends early if `legitimacy ≥ control_threshold + 5`. The condition is the same warning-band boundary used in DMP-217, so the player knows the number. Early exit sets `CRISIS_ENDED` with `early_exit = true`, starts `RECOVERY`, and grants no other benefit. A crisis that is not resolved early ends at the 18th turn regardless of legitimacy: the maximum is fixed, and there is no random extension.

**DMP-229 — Recovery is a real state, not a formality.** *Provisional (REQ-348).* After a crisis (early or full) the nation enters `RECOVERY` for **12 turns (24 hours)**:

- Full executive authority returns immediately.
- `political_stability_penalty_bp = 400` — a quarter of the crisis penalty — so stability climbs back over several turns rather than snapping to normal.
- No new non-electoral challenge can resolve; `challenge_immune_until_turn = recovery_end + 24` (DMP-223).
- A scheduled election or confidence motion that falls inside the recovery is postponed under DMP-181: its window opens at the first eligible turn and the contest resolves at the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)`.

Recovery is the player's window to fix the cause before the immunity expires. It is not a second punishment and not a second crisis.

**DMP-230 — The state ends on time, or the turn is defective.** *Provisional (REQ-348).* `leadership_state_until_turn` is the exclusive exit boundary for `TRANSITION`, `CRISIS` and `RECOVERY`. At the P4.4 of that turn the state exits, whatever the player did. A resumed or repeated settlement that finds the state already ended writes nothing. If the state is still active one turn after its boundary, the turn is `INTERRUPTED` and B-02's recovery path applies — an unending crisis is a defect, not a design.

**DMP-231 — Nothing is confiscated.** *Provisional (REQ-349).* A crisis does not delete cities, buildings, technology, inventory, crowns, treaties or alliance membership. It does not cancel a reservation, reset a research project or clear the warehouse. The only durable changes are `leadership_state`, `pressure_turns`, the contest record, the stability penalty and the ordinary economic results of the turns that ran. A player who loses a crisis still has a nation worth returning to.

**DMP-232 — Food and upkeep are paid, not paused.** *Provisional (REQ-349).* The caretaker continues B-04's obligation order. Food is consumed, maintenance is paid and variable costs are incurred for the batches that run. If the treasury cannot meet an obligation, B-04's published austerity order applies (maintenance → food → other extraction → power → processing → readiness → discretionary upkeep) and the unpaid obligation is cancelled with its disclosed consequence. The crisis does not create debt, credit or a negative balance; the no-debt rule (D-052) is unchanged.

**DMP-233 — A crisis is not a war, and war is not a crisis.** *Provisional (REQ-349).* Prompt 10 owns warfare. A war does not automatically place a nation in `CRISIS`; a crisis does not suspend defensive combat or change Operations Points. The only interaction is the contract in §36: a nation in `TRANSITION` or `CRISIS` cannot issue **new** military orders, and its existing defensive commitments resolve under Prompt 10's rules. No military penalty is attached to a political state in 06B.

**DMP-234 — A crisis can postpone a contest, never cancel one.** *Provisional (REQ-350).* If a scheduled election or confidence motion falls on a turn when the nation is in `TRANSITION`, `CRISIS` or `RECOVERY`, it is postponed under DMP-181 to the first eligible boundary and then resolved under §27; the anchor is unchanged and the next contest follows DMP-181a. The political system does not use a crisis to escape accountability, and it does not hold an election while the executive is suspended.

## 31. The leadership state machine

**DMP-235 — Six states, one active at a time.** *Provisional (REQ-351).* The vocabulary is DMP-128's. Part II defines the transitions; it does not add a seventh state and does not create a second status machine.

| State | Entry | Exit | Duration | Executive actions | Stability penalty |
|---|---|---|---|---|---|
| `NORMAL` | Default; incumbent re-elected; restoration when no window is open; a contest whose window has closed while resolution was blocked resolves from here (DMP-181b) | A window opens, a warning begins, a blocking state restores to `ELECTORAL` if a window is open, or a contest resolves | — | All legal | 0 |
| `ELECTORAL` | The first eligible turn ≥ `T − 24` — the campaign window opens; also the restoration target when a blocker clears before `window_deadline` (DMP-181b) | Resolution at the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)` — the window itself is always 24 turns | 24 turns (some turns may be blocked) | All legal, plus campaign actions; a blocker suspends them and restoration resumes the remainder | 0 |
| `SUCCESSION` | `legitimacy < threshold + 5` (non-electoral), or an early-motion warning | `legitimacy ≥ threshold + 5`, or the challenge resolves | Open | All legal; **does not block a scheduled contest** (DMP-181/236) | 0 |
| `TRANSITION` | Lost election, failed confidence motion, failed early motion, technocracy peer review | `leadership_state_until_turn`; then `ELECTORAL` if a campaign window is still open, otherwise `NORMAL` | **12 turns** | Locked (DMP-206) | **800 bp** |
| `CRISIS` | 12 pressure turns in an absolute monarchy, dictatorship or junta | `leadership_state_until_turn`, or early exit at turn ≥ 6; then `RECOVERY` | **18 turns** | Locked (DMP-206) | **1,500 bp** |
| `RECOVERY` | Crisis end, early or full | `leadership_state_until_turn`; then `ELECTORAL` if a campaign window is still open, otherwise `NORMAL` | **12 turns** | All legal | **400 bp** |

**DMP-236 — The priority order is total.** *Provisional (REQ-351).* When more than one condition is true at the same P4.4, exactly one transition runs, in this order:

1. An active `TRANSITION`, `CRISIS` or `RECOVERY` continues or ends; no other transition starts while it is active. **When the last blocker ends, the nation enters `ELECTORAL` if a campaign window is still open (`now < window_deadline`) and `NORMAL` otherwise** (DMP-181b). A transition into another blocker (`CRISIS` → `RECOVERY`) skips this restoration entirely, so no campaign action is accepted in the gap.
2. A scheduled contest resolves at its resolution turn if the nation is active, not dormant, not under B-03 protection and not in `TRANSITION`, `CRISIS` or `RECOVERY`. **`NORMAL`, `ELECTORAL` and `SUCCESSION` all resolve a due contest** — `ELECTORAL` while its window is open, `NORMAL` when the window has closed but resolution was blocked (DMP-181/181b), and `SUCCESSION` whenever the warning band is active, because it is a state of information that restricts no contest (DMP-224) — and the resolution never waits for `NORMAL`. **`SUCCESSION` blocks a non-electoral challenge only through its own 12-turn counter (DMP-218), never the ballot.**
3. An early motion resolves for a constitutional monarchy with 12 pressure turns.
4. A non-electoral challenge resolves at 12 pressure turns.
5. `SUCCESSION` is entered or left from the warning band.
6. Otherwise `NORMAL`.

A contest cannot resolve during a transition, and a challenge cannot resolve during a recovery. The ordering makes those combinations impossible rather than merely discouraged.

**DMP-237 — Impossible combinations are rejected, not repaired.** *Provisional (REQ-352).* The following are invalid states and are caught by the DMP-120 invariants:

- `leadership_state` not one of the six values.
- A non-zero `leadership_state_until_turn` in `NORMAL`, `ELECTORAL` or `SUCCESSION`.
- A zero `leadership_state_until_turn` in `TRANSITION`, `CRISIS` or `RECOVERY`.
- `pressure_turns > 0` while legitimacy is at or above the threshold.
- A second contest record for the same `(nation_id, scheduled_turn)`.
- A `government_id` different from the creation value.

A detected invalid state turns the nation-turn `INTERRUPTED`; the recovery path reads the last checkpoint. It is never "fixed" by guessing which value was intended.

**DMP-238 — Every transition writes one event and one digest line.** *Provisional (REQ-352).* The event names the from-state, the to-state, the cause, the boundary turn and — for a contest — the audit record. The digest line states what the player can and cannot do, and the exact turn on which the state ends. A transition with no explanation is a defect.

**DMP-239 — Retrying a transition is reading it.** *Provisional (REQ-352).* The transition writes `leadership_state`, `leadership_state_until_turn` and the event in one transaction. A retry finds the event key and returns the stored state. A retry after a partial write cannot extend a crisis, shorten a recovery or start a second transition; the checkpoint decides.

## 32. Where the political layer runs

**DMP-240 — Contests and pressure resolve at P4.4.** *Provisional (REQ-353).* P3.8 (DMP-114) remains the political **settlement**: supports, approval, stability and population. Part II adds **P4.4** in B-02's action phase, after construction (P4.1), research (P4.2) and policy (P4.3). P4.4 does four things and nothing else:

1. Reads the state written by P3.8.
2. Updates `pressure_turns` and enters or leaves `SUCCESSION`.
3. Resolves a due contest or challenge, writing its record.
4. Writes the state transition and sets the penalty that the **next** P3.8 will read.

Why after policy: a policy resolved at P4.3 must be visible to the contest at the same boundary. Why after P3.8: the contest must use the supports the player saw in the digest, not a half-computed state. Why not in P3.8: the settlement must remain acyclic and must not depend on campaign actions submitted during the turn.

**DMP-241 — The P4.4 sequence.** *Provisional (REQ-353).*

1. Read `nation_status`, `dormant`, protection, `leadership_state`, `leadership_state_until_turn`, `next_contest_turn`.
2. If a timed state is due to end, end it and write `*_ENDED`; stop this step for the nation.
3. If the state is `TRANSITION`, `CRISIS` or `RECOVERY` and not due to end, stop.
4. Compute `legitimacy` from the P3.8 supports and the government's vector.
5. Update `pressure_turns` (DMP-218); enter/leave `SUCCESSION`.
6. If a contest's window has opened and its resolution turn has arrived, and the nation is eligible, resolve it (F-PD-027…F-PD-034) and record it.
7. Else if an early motion is due, resolve it (F-PD-035).
8. Else if `pressure_turns = 12`, resolve the challenge (F-PD-037/F-PD-038).
9. Apply the new state, its boundary and its penalty.
10. Advance `next_contest_turn` if a contest resolved: `scheduled_contest_turn + 240 × k` under DMP-181a, never from the resolution turn.
11. Write events, the digest and the audit link; set the P4.4 marker for the turn.

**DMP-242 — One turn of lag, again.** *Provisional (REQ-354).* A transition or crisis set at P4.4 of turn `T` changes `political_stability_penalty_bp` for the **P3.8 of T + 1**. Tax at P3.1 of `T + 1` already used the stability stored at the end of `T`, so the first economic effect appears at P3.8 of `T + 1` and the first tax effect at `T + 2`. This is DMP-116's lag applied to 06B, and it is published in the interface ("your new stability applies from turn T+1"). The alternative — rewriting the tax already charged — would violate B-04's exactly-once rule.

**DMP-243 — P4.4 is idempotent.** *Provisional (REQ-354).* A `politics_actions_settled_turn` marker is written with the transition, pressure update and contest record in one transaction. A resumed P4.4 that finds the marker reads the stored state and writes nothing. A contest is additionally protected by its `(nation_id, scheduled_turn)` record. A campaign action is protected by its unique key. Three layers, one rule: a turn is applied once.

**DMP-244 — What P4.4 never touches.** *Provisional (REQ-354).* It does not compute tax, production, food, upkeep, research points, construction or trade. It does not write the economic ledger except for the campaign charges, which happen at submission, not at P4.4. It does not change `government_id`, `population`, `approval`, a support value or a policy. Its only durable outputs are leadership state, pressure, contest records, the stability penalty and events.

**DMP-245 — A failed P4.4 resumes forward.** *Provisional (REQ-355).* If the failure happens before the marker, nothing was written and the step runs once. If it happens after the state write but before the events, the resume writes the missing events from the stored state and does not recalculate the contest. If it happens after a campaign charge but before the action row, B-04's ledger key makes the charge idempotent and the action row is reconstructed from it. No path charges twice or resolves twice.

## 33. The economic test of the proposed penalties

**DMP-246 — The proposal was modelled, not dismissed.** *Provisional (REQ-356; D-100).* The brief proposed **36–48 turns** of unrest with **75% of production removed** (25% remaining) and **zero tax income**. Because "75% production reduction" can mean more than one thing under B-04, three readings were modelled at the standard start (50,000 people, 1,500 crowns, tax 150, operating cost 121, food production 60, demand 50, stock 120).

**Batch atomicity is binding.** B-04's batch is atomic: it runs completely or not at all (ECN-042, ECN-054), and it must be affordable **in full** or it does not run (ECN-048). A rule that takes 25% of a *cost* is therefore not a production rule; it is a proportional cash-flow illustration. The two batch-level readings are **A** (every batch runs, output scales) and **B-atomic** (only whole batches survive the cap). At the standard start B-atomic is a shutdown — `floor(3 × 25 / 100) = 0` food batches — which is itself the finding: "75% of production removed" cannot be expressed in whole batches without stopping the chain.

| Interpretation | What it means in B-04 | 36 turns | 48 turns |
|---|---|---|---|
| **A — Output multiplier** | Every batch still runs and consumes its inputs and variable cost; yield is 25%, floored per chain | Batch-atomic: **121/turn**; **unconstrained** `1,500 − 36×121 = −2,856`; the exact sequence is below | **Unconstrained** `1,500 − 48×121 = −4,308`; the same sequence begins on turn 13 |
| **B-atomic — Batch cap on whole batches** | `batches_run = floor(planned × 25 / 100)` per chain; at the standard start the 3/2/1/1 planned batches all floor to **0**, so only maintenance (11) remains | **11/turn**, zero output; `1,500 − 36×11 = 1,104` — a real balance | `1,500 − 48×11 = 972` — a real balance |
| **B-proportional — illustration only** | The aggregate variable cost is scaled: `floor(110 × 25 / 100) = 27`, so `11 + 27 = 38/turn`. This is **not** a batch charge and cannot be paid batch by batch | Projection `1,500 − 36×38 = 132`; **not** an actual trajectory | Projection `1,500 − 48×38 = −324`; **not** a balance |

**One term, used exactly.** A figure such as `1,500 − 48×38` is an **unconstrained cumulative cash-flow result**: the starting treasury minus every planned expense of the period, computed *as if each one could be paid*. It is a projection for comparing interpretations, not a balance the game can produce. B-04's treasury never goes negative (ECN-102), there is no debt (ECN-103), and an obligation that cannot be paid is **cancelled** under the austerity order (ECN-105/106) with its declared consequence. The actual trajectory is therefore a sequence of fully paid turns, then cancelled obligations and their consequences, ending at or above zero — and the counterfactual is reported that way below.

All three columns use the register's default arithmetic — **one `floor` per stated division and no rounding of an intermediate value** (register §2). Only **A** is a batch-level sequence, because it leaves each batch's cost unchanged. **B-atomic** is a batch-level cap on whole batches. **B-proportional** is an explicitly labelled illustration: `27` is not the cost of any batch, so its 36- and 48-turn figures are comparisons, not trajectories. Nothing here changes an accepted B-04 expense, rounding or austerity rule, and "first unaffordable obligation" means the first obligation the austerity order cancels (ECN-105/106), never an overdraft or a debt.

**Reading A, turn by turn.** Turns 1–12 cost 121 each and are paid in full (`12 × 121 = 1,452`, leaving **48**). Turn 13: P3.2 pays maintenance **11** (37 left); P3.3 runs food first under ECN-105 — `3 × 12 = 36` is affordable, leaving **1** — and coal (20), oil (14) and iron (10) are not, so none of those batches runs; P3.4 needs 10 and does not run; P3.5 has no power and runs nothing; P3.6 has the 15 food just produced against a demand of 50, so it consumes 15 and 35 are unmet. Turn 14: the single crown is allocated by maintenance obligation in **ECN-147a**'s order, extraction → generation → processing — food (3) and coal (2) are unaffordable and cancelled, **oil (1) is paid**, and iron (1), refining (2) and the generator (2) are cancelled — so the oil chain alone stays maintained, every other chain is `UNMAINTAINED` and cannot run, and **0** crowns remain. P3.3 produces nothing (the oil batch costs 14 and there is nothing to spend), P3.4 has no generator, P3.5 has neither refining nor power and P3.6 has no food. The treasury closes at **0** and never goes below zero. The first obligation that cannot be paid is the **turn-14 food maintenance** (3 against 1); the turn-13 industrial batches are simply unaffordable and do not run (ECN-048). Food production is 15 a turn from turn 1, so the stock is 85, 50, 15 and 0 after turns 1–4: the first shortage is **turn 4** (unmet 20), not turn 15. From turn 5 the shortfall is 35 a turn, and on turn 14 it is 50.

None of the three is acceptable, and each fails differently:

- **A empties the treasury while keeping only the food chain alive.** Turn 13 still pays 47 crowns — maintenance and the three food batches — but coal, oil, iron, power and processing stop. Turn 14 loses almost all of its maintenance: only the oil chain is paid, every other chain is `UNMAINTAINED`, output stops, and the shortage that began on turn 4 becomes total. The `−2,856` is the projection of that failure, not a balance; the treasury never goes negative.
- **B-atomic is a shutdown that a solvency test cannot see.** Every chain floors to zero batches, so the nation produces nothing while its treasury drains by 11 a turn: **1,104** left at 36 turns and **972** at 48. The 120-unit food stock covers two turns and turn 3 is short by 30. The nation is solvent and starving, which is exactly why "can it pay?" is the wrong test.
- **B-proportional stays solvent on paper but starves.** Food is `floor(60 × 25 / 100) = 15` against demand 50. The stock covers three turns at that rate (`120 + 3×15 − 3×50 = 15`), and turn 4 is short. Its 38/turn is an illustration, so neither 132 nor −324 is a balance the game could hold; the hunger and the lost output are the real consequence.
- **Zero tax** adds `36 × 150 = 5,400` crowns of lost income at 36 turns (`48 × 150 = 7,200` at 48) and removes the only income that could buy food or pay maintenance.

A 36-turn crisis would therefore be **worse than losing the nation**: it destroys the economy that the player is supposed to return to. The proposal is **rejected**.

**DMP-247 — The five models compared.** *Provisional (REQ-356).*

| Model | Duration | Economic effect | Verdict |
|---|---|---|---|
| **A — Full proposal** | 36–48 turns | 25% output, zero tax | **Rejected.** Insolvent or starving within four turns; the punishment exceeds the crime |
| **B — Shorter, same severity** | 12 turns | 25% output, zero tax | **Rejected.** Still starves (food shortage from turn 4) and still costs ~1,800 crowns of tax; twelve turns of starvation is not a "short" crisis |
| **C — Graduated** | 36 turns, severity falling | 25%→50%→75% output, tax ramp | **Rejected.** Needs a second multiplier schedule, still starves early, and is harder to explain than a fixed rule |
| **D — Negotiated recovery** | 6–18 turns | Player actions shorten; no multiplier | **Adopted in shape**, but without an economic multiplier: the crisis ends early if legitimacy recovers (DMP-228) |
| **E — Protected essential production** | 18 turns | Food and power exempt, other output cut | **Rejected.** Requires a second definition of "essential" per facility, a separate cost path and a new B-05 rule; the complexity buys nothing that the adopted model does not |

**DMP-248 — The adopted model costs authority, not solvency.** *Provisional (REQ-357).* The crisis is **18 turns**, with **no production or tax multiplier**. At the standard start:

| Item | Normal 18 turns | Crisis 18 turns |
|---|---:|---:|
| Tax income | `18 × 150 = 2,700` | **2,366** (stability falls to 8,500 by turn 6; tax 127 thereafter) |
| Operating cost | `18 × 121 = 2,178` | 2,178 (unchanged) |
| Net operating income | **+522** | **+188** |
| Closing treasury from 1,500 | 2,022 | **1,688** |
| Food | 60 produced vs 50 consumed | 60 vs 50 (unchanged) |

At 500,000 people (tax 1,500, operating cost 1,210), the same crisis costs `27,000 − 23,736 = 3,264` crowns of tax over 18 turns and still produces **+1,956** net. The nation is poorer, not ruined; the player loses **eighteen turns of decisions**, which is the real cost. A mature nation can absorb it; a new one is not pushed into insolvency.

**DMP-249 — Why removing the multiplier is the design, not a softening.** *Provisional (REQ-357).* A production multiplier would have to be applied either after output (violating B-04's per-batch identity) or to capacity (violating B-05's `Σ DC ≤ capacity` invariant). Either route creates a second place where output is decided, which is exactly what DMP-130 forbids. The crisis therefore changes **what the player may do**, and the economy changes only through the one stability term that B-06 already owns. This is simpler to implement, impossible to double-count, and legible to the player: "you lost the argument; the country still works."

**DMP-250 — The distribution of pain is deliberate.** *Provisional (REQ-357).* A crisis hurts a nation with low reserves more than one with high reserves, because the low-reserve nation cannot buy its way through a shock and has less slack to absorb a stability dip. But it does not **delete** either nation's means of recovery: production continues, food continues, tax continues. The design target is a player who logs in after 36 hours to find a nation that is angrier and poorer by a few hundred crowns — not one that is starving, bankrupt or gone.

## 34. Fairness, interface and anti-exploit

**DMP-251 — Nothing political happens off-screen.** *Provisional (REQ-358).* Every contest, warning, transition, crisis and recovery is announced in the digest with its cause, its boundary and its economic effect. A player who logs in after 36 hours can reconstruct the whole sequence from the digest and the audit record. A hidden political change is a defect, not a surprise mechanic.

**DMP-252 — Absence is not a political strategy, and it is not punished as one.** *Provisional (REQ-358).* An offline incumbent stands with zero campaign bonus and the same challenger formulas; an offline ruler accumulates pressure only from the state, not from a login requirement. No election requires attendance, no crisis requires a click to end and no deadline falls before a notified window. The game processes politics while the player is away; it does not require the player to be present to avoid a penalty that is not about the nation's condition.

**DMP-253 — The anti-exploit table.** *Provisional (REQ-359; D-104).*

| Exploit | Prevention |
|---|---|
| Resolve the same election twice | `(nation_id, scheduled_turn)` record; retry returns it (DMP-182) |
| Charge a campaign action twice | Unique action key and B-04 ledger key; retry returns the stored row (DMP-193) |
| Fund a campaign from a second account | Campaigns are nation-scoped and paid from the nation treasury; a second account cannot act inside the nation (D-032) |
| Reroll to escape a transition or crisis | Reroll destroys the nation and creates a new one with no political state; it is not a way to keep the assets (DMP-211) |
| Toggle policy to farm support | Policy cooldown is 12 turns per axis; supports read the setting, not the act of changing (DMP-102) |
| Trigger and end a crisis to gain immunity | A crisis can be entered only by 12 turns below threshold; immunity is 24 turns and does not reset approval or grants |
| Extend a crisis through a scheduler failure | `leadership_state_until_turn` is absolute; a state still active one turn late is `INTERRUPTED` (DMP-230) |
| Manipulate a deadline with the player's clock | All deadlines are world-turn IDs (DMP-183) |
| Use a caretaker to optimise the nation | The caretaker is a fixed list of continuing obligations with no discretion and no budget (DMP-207) |
| Candidate withdrawal to avoid a result | The ballot is fixed at `campaign_open_turn + 12` (`T − 12` when on time); no withdrawal exists (DMP-188) |
| Vote buying through the market | Campaign actions are the only political spending; no transfer of crowns changes a vote (DMP-195) |
| Create a second nation to stand as a challenger | Challengers are simulated and cannot be accounts (DMP-185) |

**DMP-254 — New-player protection is time, information and a cushion.** *Provisional (REQ-360).* A new nation gets: a full 240-turn first term (DMP-180); starting legitimacy at least nine points above its control threshold (DMP-216); the five-point warning band before any pressure (DMP-217); a digest that names the exact number needed to reset pressure; and a first election that cannot occur before it has governed for 20 days. There is **no** separate "political tutorial immunity" that suspends the rules, because a suspension would teach the wrong system. The protection is that the first crisis cannot arrive quickly.

**DMP-255 — The experience targets are explicit.** *Provisional (REQ-360).* A lost election costs **24 hours** of executive authority, not the nation. A lost non-electoral challenge costs **36 hours** in crisis plus **24 hours** of recovery, with production and tax continuing. A player who logs in daily never misses more than one day of orders; a player who logs in weekly may lose a campaign or a challenge, but returns to a nation with its assets and a clear explanation. Those are the numbers the design is judged against.

**DMP-256 — The screens the political layer needs.** *Provisional (REQ-361).* Prompt 13 must provide: a **political panel** (approval, stability, legitimacy, all six supports, `pressure_turns/12`, the threshold); an **election dashboard** (term, campaign window, ballot, projected vote, campaign budget and remaining actions); a **group table** (support, turnout weight, election score, contribution); a **warning panel** (which groups are below the removal threshold and what moves them); a **state banner** (state, cause, end turn, what is locked and what is not); a **result screen** (DMP-213); and a **crisis/recovery digest** with the exact end turn.

**DMP-257 — Every number the player needs is shown before the action.** *Provisional (REQ-361).* The projected vote, the campaign cost, the remaining budget, the effect of a platform point and the pressure needed to reset are displayed **before** submission. A player must not have to spend 150 crowns to discover what an advertisement does. This is the same rule as DMP-073 (show the terms) applied to contests.

## 35. Worked examples E19–E49

Part I's Examples 1–18 remain valid and unchanged. These examples use the same standard start (50,000 people, supports 55/65/56/51/53/49, approval 55, stability 10,000, treasury 1,500, tax 150, operating cost 121) unless stated.

### Example 19 — The term in days

`240 turns × 2 hours = 480 hours = 20 days`. The proposal's arithmetic is correct; the design question was whether 20 days is a good term, not whether the conversion works.

### Example 20 — A nation's election anchor

A nation is created on turn **137**. Its first contest is `137 + 240 = 377`. If it resolves on turn 377, the next is `377 + 240 = 617`. If a recovery interrupts a window that opened at 359 and clears on turn 383, the contest resolves at **383** — its 24 turns had already run — and the next is still `377 + 240 = 617`, not `383 + 240 = 623`.

### Example 21 — The campaign window

For `T = 1000`: campaign opens at `976` (48 h before), registration closes at `988` (24 h before), final notice at `998` (4 h before), and the campaign closes when turn `1000` opens. Resolution is P4.4 of 1000; at 1001 the result is applied — the incumbent continues if returned, or the account enters the 12-turn caretaker `TRANSITION` if defeated (DMP-184).

### Example 22 — A platform allocation

The player allocates **2 Rural, 2 Scholars, 2 Security** — six points, three groups, two each. On the Example 28 state the election totals change:

| Group | Support | Points | Election score | Weight | Contribution |
|---|---:|---:|---:|---:|---:|
| Labour | 55 | 0 | 55 | 2,443 | 134,365 |
| Rural | 40 | 2 | 42 | 1,765 | 74,130 |
| Industry | 47 | 0 | 47 | 1,991 | 93,577 |
| Commerce | 45 | 0 | 45 | 1,357 | 61,065 |
| Scholars | 40 | 2 | 42 | 1,358 | 57,036 |
| Security | 50 | 2 | 52 | 1,086 | 56,472 |
| **Total** | | | | | **476,645** |

`floor(476,645 / 100) + 200 = 4,766 + 200 = 4,966`. The allocation is worth **+84 bp** over the same state with no campaign (4,882). It is enough to flip Example 28.

### Example 23 — A rally's cost at two sizes

`unit = ceil(population / 1,000)`. At 50,000: unit 50, rally `2 × 50 = 100` crowns. At 500,000: unit 500, rally `2 × 500 = 1,000` crowns. The rally always adds +3 Labour and +2 Rural; only the price scales.

### Example 24 — Two advertisements

At 50,000, each advertisement costs `3 × 50 = 150`; two cost **300**. At 500,000, each costs `3 × 500 = 1,500`; two cost **3,000**. A full campaign (one rally + two advertisements) therefore costs **400** at 50,000 and **4,000** at 500,000 — about 27% of the standard opening treasury in both cases.

### Example 25 — The campaign cap binds

A player allocates 2 Labour, then rallies (+3 Labour): the Labour bonus is **5**, under the cap of 6. Another allocates 2 Industry and buys two advertisements (+2 each): the Industry bonus is **6**, exactly the cap. A third tries 2 Labour + rally + an advertisement that also gives Labour: the formula clamps to **6**; the extra point is wasted, and the interface warns before purchase.

### Example 26 — The standard-start election

| Group | Support | Weight (bp) | Contribution |
|---|---:|---:|---:|
| Labour | 55 | 2,443 | 134,365 |
| Rural | 65 | 1,765 | 114,725 |
| Industry | 56 | 1,991 | 111,496 |
| Commerce | 51 | 1,357 | 69,207 |
| Scholars | 53 | 1,358 | 71,974 |
| Security | 49 | 1,086 | 53,214 |
| **Total** | | **10,000** | **554,981** |

`floor(554,981/100) + 200 = 5,549 + 200 = 5,749`. Challengers: approval 55 → Popular Front `4,400 + 5×40 = 4,600`; legitimacy 55 → Institutional `4,300 + 0 = 4,300`. The incumbent wins by **1,149 bp**. No campaign is needed.

### Example 27 — A clear defeat

The same nation after a famine: supports 40/50/41/36/38/34, approval 40, legitimacy 40. The vote is `floor(404,981/100) + 200 = 4,049 + 200 = 4,249`. Challengers: Popular Front `4,400 + 20×40 = 5,200`; Institutional `4,300 + 15×30 = 4,750`. The incumbent finishes **third**, 951 bp behind. No legal campaign (maximum ~469 bp) could have saved this term.

### Example 28 — A narrow defeat

Supports 55/40/47/45/40/50, approval 47, legitimacy 47. Vote: `floor(468,227/100) + 200 = 4,682 + 200 = 4,882`. Popular Front `4,400 + 13×40 = 4,920`; Institutional `4,300 + 8×30 = 4,540`. The incumbent loses by **38 bp** — the narrowest kind of defeat, and still a full transition (DMP-212).

### Example 29 — A campaign that flips the narrow seat

On Example 28's state the player spends **0 crowns** on the platform allocation of Example 22 (2 Rural, 2 Scholars, 2 Security): the vote becomes **4,966**, beating the Popular Front's 4,920 by **46 bp**. A free allocation, chosen well, is worth more than a paid advertisement chosen badly; the same six points on Labour, Industry and Commerce would add `(2×2443 + 2×1991 + 2×1357)/100 = 115` bp, which also wins, by 77. The point is not that one allocation is uniquely correct; it is that **where** the points go changes the coalition, and the player can see both results before submitting.

### Example 30 — A tie

The incumbent and the Popular Front both finish on **5,000 bp**. Rule 1 applies: the incumbent is returned. If the tie is between the two challengers at 4,800 with the incumbent at 5,100, the incumbent wins on score, and the challengers' order is irrelevant. If the incumbent were absent (impossible in the current model), rule 2 would compare approval and rule 3 the candidate index. The invoked rule is written into the record; there is no coin flip.

### Example 31 — A constitutional monarchy's confidence motion

The standard start. The institutional vector is 10/20/15/15/20/20. Confidence:

| Group | Support | Vector | Contribution |
|---|---:|---:|---:|
| Labour | 55 | 10 | 550 |
| Rural | 65 | 20 | 1,300 |
| Industry | 56 | 15 | 840 |
| Commerce | 51 | 15 | 765 |
| Scholars | 53 | 20 | 1,060 |
| Security | 49 | 20 | 980 |
| **Total** | | **100** | **5,495** |

`confidence_bp = floor(5,495/1) = 5,495 ≥ 4,500` — the motion carries by **995 bp**. There is no incumbency allowance and no challenger.

### Example 32 — A failed confidence motion

Supports 44/40/44/40/42/44, legitimacy 42. Confidence: `440 + 800 + 660 + 600 + 840 + 880 = 4,220`, below 4,500. The motion fails by **280 bp** and a `TRANSITION` begins at `T + 1`. Note that the government is still a constitutional monarchy: the monarch remains head of state; the administration has lost parliament.

### Example 33 — An early motion

A constitutional monarchy's legitimacy falls to 44 and stays there. The warning band is `< 50` (45 + 5), so `SUCCESSION` begins immediately. `pressure_turns` reaches **12** after 24 hours. Because 44 < 45, the early motion is tabled at the next P4.4 under DMP-201 — with **no campaign window** — and, at 4,300 confidence, fails. The player had twelve turns of visible warning; a scheduled election would have given twenty-four turns of campaign.

### Example 34 — The transition's length

`12 turns × 2 hours = 24 hours = 1 day`. The player loses one day of new orders. At 12 turns per day, that is three construction windows, twelve research turns and one policy cooldown's worth of delay.

### Example 35 — The transition's economics

Penalty 800 bp: target `10,000 − 800 = 9,200`; stability moves 250 bp per turn and reaches the target on turn 4. Taxes: 150, 146, 142, 138, then 138 for eight turns = **1,680** total (a normal 12 turns would be 1,800; the cost is **120 crowns**). Operating cost 1,452. Closing treasury `1,500 + 1,680 − 1,452 = 1,728`. The nation is **228 crowns ahead** of where it started; the defeat cost authority, not solvency.

### Example 36 — A junta's warning

A military junta has security support 44, so legitimacy 44 (the junta's vector is 100% security). Threshold 40, warning band `< 45`: the nation enters `SUCCESSION` with `pressure_turns = 0`, because 44 is not below 40. If security support falls to **39**, legitimacy is 39 < 40 and `pressure_turns` becomes **1**; the warning panel says "one turn below the threshold; eleven more begin the crisis". The junta has nine points of cushion at creation and no cushion once the army turns.

### Example 37 — Twelve turns to a crisis

The junta stays at legitimacy 39 for twelve consecutive turns. `pressure_turns` = 1…12; at 12 the challenge resolves at P4.4 and `CRISIS` begins. If legitimacy returns to 40 on turn 11, the counter resets to 0 and no crisis occurs. The rule is consecutive, not cumulative: a government that oscillates 39/40/39 never accumulates twelve.

### Example 38 — A dictatorship's challenge

A dictatorship at legitimacy 34 (threshold 35) begins pressure. Twelve turns later it enters `CRISIS` for 18 turns. The formal government remains `gov_dictatorship`; the fiction is a coup within the regime, not a revolution. The player keeps the account and the nation.

### Example 39 — The crisis at the standard start

Penalty 1,500 bp: target 8,500, reached on turn 6. Taxes: 150, 146, 142, 138, 135, 131, then 127 for twelve turns = **2,366**. Operating cost 2,178. Closing treasury `1,500 + 2,366 − 2,178 = 1,688`. Food is unchanged (60 produced, 50 consumed). The crisis costs **334 crowns of tax** against a normal 18 turns and **18 turns of orders**.

### Example 40 — The crisis at scale

A 500,000-person nation with tax 1,500 and operating cost 1,210. The same stability path gives taxes 1,500, 1,462, 1,425, 1,387, 1,350, 1,312, then 1,275 for twelve turns = **23,736** (a normal 18 turns would be 27,000). Operating cost 21,780. Closing treasury from 20,000: `20,000 + 23,736 − 21,780 = 21,956`. The nation is **1,956 crowns ahead**; the cost is 3,264 crowns of tax and 36 hours of decisions. Scale changes the size of the bill, not its nature.

### Example 41 — The rejected proposal at 36 turns

Standard start (food capacity 3, coal 2, oil 1, iron 1, refining 1, one generator), 25% output and zero tax for 36 turns. Maintenance is **11**; running every batch costs **110** of variable expense, so an ordinary turn is **121**.

- **A — output multiplier, batch-atomic.** Every batch still runs while it is affordable, so an ordinary turn stays 121 and the **unconstrained** result is `1,500 − 36×121 = −2,856`, not a balance. Turns 1–12 are paid in full (`1,452`, leaving 48). Turn 13 pays maintenance **11** (37 left), then food `3 × 12 = 36`, leaving **1**; coal (20), oil (14), iron (10), power (10) and refining (20) are unaffordable and do not run. Turn 14 allocates the single remaining crown under ECN-105/ECN-147a in the published maintenance order — each chain's maintenance is one whole obligation (`capacity_batches × rate`), in the order extraction → generation → processing: food (3) and coal (2) cannot be paid and are cancelled, **oil (1) is paid**, and iron (1), refining (2) and the generator (2) are cancelled. The oil chain is therefore maintained and **every other chain is `UNMAINTAINED`**; with 0 crowns left no chain can run, and the treasury closes at **0**, not 1. Food production is `floor(60 × 25/100) = 15` a turn from the start, so the stock runs `120 → 85 → 50 → 15 → 0` and the **first shortage is turn 4** (unmet 20, penalty 1,200 bp stored for turn 5) — not turn 15. From turn 5 the shortfall is 35 a turn; on turn 14, with the food chain unmaintained, it is the full 50.
- **B-atomic — batch cap on whole batches.** `floor(3 × 25 / 100) = 0` food batches, and likewise 0 coal, 0 oil, 0 refining and 0 generators: no batch runs at all. The cost is maintenance only, **11/turn**, so `36 × 11 = 396` and **1,104** remains — solvent, with zero output and a food shortage from turn 3 (`120 − 2×50 = 20`, then −30).
- **B-proportional — illustration only.** `floor(110 × 25 / 100) = 27` is an aggregate, not a batch charge, so `11 + 27 = 38/turn`. `1,500 − 36×38 = 132` is a projection, and food at `floor(60 × 25 / 100) = 15` against demand 50 starves from turn 4. It is kept only to compare the readings' cash flow.
- **Zero tax** loses `36 × 150 = 5,400` crowns of income in every reading.

There is no interpretation under which the proposal is a consequence rather than a catastrophe.

### Example 42 — The rejected proposal at 48 turns

- **A:** **unconstrained** `1,500 − 48×121 = −4,308`; the turn-13/turn-14 sequence is unchanged — the oil chain is the only maintained chain, nothing runs from turn 14, the treasury closes at **0**, and the food shortfall is 50 a turn for the remaining 34 turns.
- **B-atomic:** `48 × 11 = 528`, leaving **972** — solvent with no output for 48 turns.
- **B-proportional:** **unconstrained** `1,500 − 48×38 = −324`, not a balance; its 36-turn 132 is a projection too, because 27 is not a batch charge.
- Zero tax loses `48 × 150 = 7,200` crowns.

The longer duration makes every failure worse without adding a single new decision. The duration was the second problem; the multipliers were the first.

### Example 43 — Food under the proposal

At 100% output the standard start produces 60 food and consumes 50, leaving a surplus of 10. At 25% output it produces `floor(60 × 0.25) = 15` and consumes 50. With a 120-unit stock: after three turns `120 + 45 − 150 = 15`; on the fourth, `15 + 15 = 30` against demand 50, so 30 are eaten, **20 are unmet** and the stock is **0** — ECN-082 clamps the stock, so there is no negative balance. Hunger rises toward the 3,000 bp cap, approval falls, and the shortage repeats every turn for the rest of the crisis. This is why the proposal is rejected even in the "solvent" reading.

### Example 44 — Food under the adopted crisis

The adopted crisis does not change production. The standard start still produces 60 and consumes 50; the warehouse grows by 10 a turn; hunger stays 0. A nation that was already short of food stays short for the ordinary reasons — the crisis neither causes nor cures it. That is the correct scope: a political crisis changes who decides, not what the farms do.

### Example 45 — An early exit

A junta enters crisis with threshold 40. At the P4.4 of crisis turn **6**, legitimacy has recovered to **46**, which is at least `40 + 5 = 45`. The crisis ends early; `RECOVERY` begins with a 400 bp penalty. At turn 6 the player had already lost six turns of orders; the early exit returns the remaining twelve. Had legitimacy been 44, the crisis would have run all 18 turns — safe is not the same as recovered.

### Example 46 — A repeated resolution

The election at turn 377 resolves with `vote_bp = 5,749` and the incumbent returned. The scheduler sends the same job again. The resolver finds the `(nation_id, 377)` record, returns 5,749 and writes nothing: no second campaign charge, no second transition, no second `next_contest_turn` advance. The digest still shows one election. This is the test that must fail if the idempotency key is removed.

### Example 47 — A new nation's first contest

Created on turn 100: first contest at `100 + 240 = 340`; campaign opens at `316`. The nation has 20 days and 240 settlements to build an economy before it faces a vote. No early election, no shortened term and no political protection beyond the cushion in DMP-216.

### Example 48 — A reroll does not transfer politics

A player in `TRANSITION` deletes the nation and creates a new one on the same account. The new nation has `government_id` chosen at creation, `population = 50,000`, `approval` from its starting supports, `leadership_state = NORMAL`, `pressure_turns = 0`, `next_contest_turn = new_creation + 240`, and no contest history. Nothing from the old nation's term, campaign, transition or crisis is copied. The reroll is instant (D-039) and total (DMP-211).

### Example 49 — Scheduled and early motions are not the same contest

A constitutional monarchy's scheduled motion is due at turn 240. The campaign opens at 216 and the player can spend 24 turns building a coalition. If instead legitimacy falls to 44 at turn 150 and stays there, the early motion is tabled at turn 162 — twelve turns later, with **no campaign window**. Same threshold, same vector, different warning: the scheduled motion is a general election; the early motion is a parliamentary collapse. The player who keeps legitimacy above 45 never sees the second.

## 36. Contracts with the other prompts

**DMP-258 — Prompt 02 (turn engine).** *Provisional (REQ-362).* B-06's subsystem entry gains: the actions `CAMPAIGN_PLATFORM`, `CAMPAIGN_RALLY`, `CAMPAIGN_ADVERTISE`; the phase **P4.4**; the state machine of §31; the idempotency markers `politics_actions_settled_turn` and the contest record; the invariants of DMP-120 and DMP-237; and the recovery rule of DMP-245. P3.8's order is unchanged.

**DMP-259 — Prompt 03 (accounts and nations).** *Provisional (REQ-362).* The political state belongs to the **nation**, never the account. A transition or crisis never changes `nation_status`, never suspends the account and never creates an account-pair restriction (DMP-132). The existing reroll is total and instant; it copies no political state (DMP-211). A dormant nation's contests and pressure freeze (DMP-222). No political feature may require a second account or a transfer between accounts.

**DMP-260 — Prompt 04 (economy).** *Provisional (REQ-363).* 06B adds two things to B-04's contract and nothing else:

1. `political_stability_penalty_bp`, consumed by F-PD-017, which changes `stability_bp` and therefore B-04's single tax formula. No new tax line.
2. Two operating-expense ledger entries, `CAMPAIGN_RALLY` and `CAMPAIGN_ADVERTISE`, charged at submission from `available_crowns` (DMP-193).

No crown, resource, debt, credit or interest is created. The no-debt rule, the austerity order and the append-only ledger are unchanged.

**DMP-261 — Prompt 05 (cities).** *Provisional (REQ-363).* A transition or crisis does **not** change capacity, housing, output per batch, construction cost or upkeep. Existing construction and research continue; new orders are blocked (DMP-206). No facility is destroyed, downgraded or made `UNMAINTAINED` by a political state, and the `Σ DC ≤ capacity` invariant is untouched.

**DMP-262 — Prompt 07 (trade and markets).** *Provisional (REQ-364).* While `leadership_state` is `TRANSITION` or `CRISIS`, the player may **read** the market and may not create, accept or cancel a trade offer or a reservation. Existing accepted trades settle normally under Prompt 07's rules. 06B imposes **no** trade tax, tariff, embargo or market fee; those are Prompt 07's decisions, and if it adds one it must not reuse the political stability term.

**DMP-263 — Prompt 08 (diplomacy).** *Provisional (REQ-364).* Treaties, diplomatic standing and obligations persist through a transition or crisis. The player may read them and may not sign, ratify, denounce or renegotiate one while authority is suspended. A leadership change does not void a treaty (DMP-081 applied to diplomacy). Prompt 08 owns reputation; 06B supplies the state flag.

**DMP-264 — Prompt 09 (alliances).** *Provisional (REQ-365).* Alliance membership, rank and shared obligations persist. A caretaker cannot change permissions, spend a shared pool, accept an alliance application or leave an alliance. The player retains alliance **chat** during a transition (DMP-206) so that a political defeat does not cut them off from their community. Prompt 09 must not expose a shared asset to a caretaker's authority.

**DMP-265 — Prompt 10 (warfare).** *Provisional (REQ-365).* A nation in `TRANSITION` or `CRISIS` cannot issue **new** military orders or spend Operations Points. Existing defensive commitments resolve under Prompt 10's rules; a war does not pause because a government fell. 06B attaches no combat, readiness or OP modifier to any political state, and D-015 remains the Operations Points model. Political actions never consume Operations Points (D-103).

**DMP-266 — Prompt 11 (world events).** *Provisional (REQ-366).* An event may move a **published input** — food, approval through its normal formula, a support term, a stability term — but may not set `leadership_state`, resolve a contest, remove a leader or grant a campaign bonus. A scripted event that removes a government would be a second removal system, which DMP-018 forbids. Event effects are applied once, with a key, and are visible in the digest.

**DMP-267 — Prompt 12 (fair play and administration).** *Provisional (REQ-366).* The contest record, campaign-action rows and state events are the audit evidence. An operator cannot edit a contest result, a campaign charge, `pressure_turns` or `leadership_state`; a correction is an adjustment that names the original record (DMP-122). A political state is **not** a sanction and may not be imposed as one. Account-level sanctions remain account-level (D-040).

**DMP-268 — Prompt 13 (interface).** *Provisional (REQ-367).* The screens and disclosures are DMP-256 and DMP-257. The interface must show the **state banner** on every political screen and must never present a transition or crisis as a ban, a suspension or an account penalty.

**DMP-269 — Prompt 14 (balance) and Prompt 15 (assembly).** *Provisional (REQ-367).* Prompt 14 receives the constants in register §3.8 and the scenarios in §35; it may change a **value** by a new revision, not a formula's structure, and every change is versioned by `politics_version` (DMP-123). Prompt 15 includes Part I, Part II and the register in the Bible and must not split them into separate political documents.

## 37. Verification and what has actually been checked

**DMP-270 — The verification map for Part II.** *Provisional (REQ-368).*

| Formula area | Formula IDs | Examples | Checker |
|---|---|---|---|
| Schedule and window | F-PD-027, F-PD-028 | E19–E21, E34, E47, E49 | `verify_politics_numbers.py` |
| Anchoring, resolving states and catch-up | F-PD-027, F-PD-039 | E20, E34, E47, E49 | `verify_politics_numbers.py` — schedule model, election-state cases and document guards |
| Campaign costs and cap | F-PD-029, F-PD-030 | E22–E25 | `verify_politics_numbers.py` |
| Vote and challengers | F-PD-031…F-PD-034 | E26–E30, E46 | `verify_politics_numbers.py` |
| Confidence | F-PD-035 | E31–E33 | `verify_politics_numbers.py` |
| Pressure and thresholds | F-PD-036, F-PD-037 | E36–E38 | `verify_politics_numbers.py` |
| States and durations | F-PD-038, F-PD-039 | E34, E37, E45 | `verify_politics_numbers.py` |
| Crisis economics | F-PD-026, F-PD-038 | E39–E44 | `verify_politics_numbers.py` |
| Early exit, immunity and the first contest | F-PD-040, F-PD-041, F-PD-042 | E45, E47, E48 | `verify_politics_numbers.py` |
| Contest idempotency and the audit record | F-PD-043, F-PD-044 | E46 | `verify_politics_numbers.py` |

The checker recomputes every number from the register's constants. It is a **document** check: it does not run a scheduler, a database or a game. Since the 2026-10-28 corrections it also **models the schedule** (anchor, catch-up multiplier and once-only window delivery, with every campaign date derived from `campaign_open_turn`), asserts the lifecycle and state cases (1000/976/1010 → 1010 while the superseded helper would say 1034; 1000/976/990 → 1000 with `ELECTORAL` restored for the last ten turns; 1000/980 → 1004; `NORMAL`, `ELECTORAL` and `SUCCESSION` resolve, `TRANSITION`, `CRISIS` and `RECOVERY` postpone and leave no gap between consecutive blockers), recomputes the **atomic batch** account (37 crowns after maintenance run 3 food batches and no coal; 35 run 2 and 1; 11 skip food and run coal under ECN-105), and runs **12 document guards** against the superseded `NORMAL`-only postponement condition, a resolution-turn anchor, a restarted campaign window, a `NORMAL`-only restoration, a `T`-based registration deadline, a negative "treasury" balance, a non-atomic batch reading, and a progress log whose summary and table disagree. `--self-test` proves each guard fails when its defect is reintroduced into an in-memory copy; no project file is modified by that mode.

**DMP-271 — The invariant list of Part II.** *Provisional (REQ-368).* In addition to DMP-120's ten and DMP-237's six:

1. `0 ≤ campaign_bonus_i ≤ 6` for every group, and the paid actions never exceed their per-contest limits.
2. A campaign charge has exactly one ledger entry with the action key.
3. `pressure_turns` changes by at most 1 per turn and only at P4.4.
4. A contest record is unique on `(nation_id, scheduled_turn)`.
5. `next_contest_turn` advances from the **scheduled** turn by `240 × k`, `k ≥ 1` (DMP-181a), is never anchored on the resolution turn, and is always at least 25 turns after the resolution turn, so the next campaign's open turn is never in the past.
6. A state's `leadership_state_until_turn` is exactly `entry_turn + duration` for its state (12, 18 or 12).
7. A political state never changes `government_id`, `population`, `approval`, a support, a policy or a reservation.
8. The stability penalty applied at P3.8 equals F-PD-026 for the state that was active at the start of the turn.

**DMP-272 — Planned test methods.** *Provisional (REQ-368).* The requirement rows use the identifiers **T06B-S** (schedule), **T06B-C** (campaign), **T06B-V** (vote), **T06B-F** (confidence), **T06B-R** (retention), **T06B-X** (crisis/recovery), **T06B-E** (economics), **T06B-A** (anti-exploit) and **T06B-D** (documents). **None has been executed as a runtime test**; they are specifications for Stage 5 and for the document checker.

**DMP-273 — What is not validated, and must not be claimed.** *Provisional (REQ-368).* There is no scheduler, no database, no `campaign_action` table, no contest record, no political state machine, no UI and no player test. The 31 examples are hand calculations checked by a script against the register. The design is **not** proven fun, balanced or exploit-free; it is proven arithmetically consistent with B-04 and B-05 at the published points. Prompt 14 must simulate it before launch.

**DMP-274 — The examples are part of the specification.** *Provisional (REQ-368).* A change to a formula that invalidates E19–E49 is a specification change, not a documentation edit. The checker must be updated with it, and the revision history must say which examples changed. This is the rule that caught the stale 309-check register in the 06A correction, and it applies with more force now that there are twice as many examples.

## 38. Revision history of Part II

| Version | Date | Change |
|---|---|---|
| 2.5 | 2026-10-28 | Consolidation pass. **State:** DMP-184 publishes the outcome-dependent banner — `NORMAL` on a win, `TRANSITION` (12 turns, 800 bp) on a loss, the same after a postponed resolution — matching DMP-204/DMP-235; it no longer returns every contest to `NORMAL`. **Accounting:** E41/E42/DMP-246 cite **ECN-147a** rather than §8.6 for the maintenance allocation, whose order is extraction → generation → processing and whose unit is one whole chain obligation (B-04 v1.3). No campaign, tax, vote or formula value changed. |
| 2.4 | 2026-10-28 | Fourth 06B micro-correction. **Deadlines:** DMP-188 (ballot) and DMP-190 (platform lock) now use `registration_close_turn` — `campaign_open_turn + 12`, `T − 12` only on time — with the delayed 992 case; register F-PD-028/F-PD-029 publish the submission window as `turn_id < resolution_turn`. **Example 41/42 and DMP-246:** Model A's food stock is recomputed from turn 1 (`120 → 85 → 50 → 15 → 0`, first shortage **turn 4**, unmet 20 then 35, 50 on turn 14), and turn 14 pays the **oil** chain's 1-crown maintenance while food (3), coal (2), iron (1), refining (2) and the generator (2) are cancelled, leaving five `UNMAINTAINED` chains and a closing treasury of **0**. **Integrity:** DMP-184's truncated final sentence is reconstructed from DMP-178/DMP-181a, with a new truncation guard in the checker. |
| 2.3 | 2026-10-28 | Third 06B micro-correction. **Restoration:** DMP-181b/DMP-204/DMP-235/DMP-236 and F-PD-039 now state that a campaign interrupted before its deadline returns to `ELECTORAL` for the remaining turns, while consecutive blockers with no eligible turn between them restore nothing; DMP-183/DMP-184 follow the same rule. **Deadlines:** DMP-178 anchors registration, notice and deadline on `campaign_open_turn` (`+12`/`+22`/`+24`), with the delayed 980 → 992/1002/1004 example; `T − 12`/`T − 2` are the on-time coincidences, not universal rules. **Accounting:** DMP-246, E41 and E42 now treat batch atomicity as binding (ECN-042/048/054), report the whole-batch cap as `floor(3 × 25 / 100) = 0` and 11/turn with 1,104 and 972 left, give the exact turn-13 sequence (maintenance 11, food 36, one crown left) and label the 38/turn reading an illustration. |
| 2.2 | 2026-10-28 | Second 06B micro-correction. **Campaign lifecycle:** DMP-181 now publishes the three-line rule — opening computed once, `window_deadline = campaign_open_turn + 24`, resolution the first eligible turn at or after `max(scheduled_contest_turn, window_deadline)` — so an already-open campaign interrupted by `TRANSITION`, `CRISIS` or `RECOVERY` resolves when the block clears, not 24 turns later (1000/976/1010 → 1010, explicitly not 1034); DMP-181b adds the two-interruption case and the three worked values; F-PD-028 publishes the same deadline. **Accounting:** DMP-246, E41 and E42 now label every negative multi-turn figure an **unconstrained cumulative cash-flow result** and state the actual B-04 path (ECN-102 no negative balance, ECN-105/106 cancelled obligations): A pays 12 full turns then loses maintenance from turn 14; B pays 39 full turns, and on turn 40 pays maintenance and cancels the 27 of variable cost, ending at 7. **State:** DMP-235/DMP-236 list `SUCCESSION` as resolving a scheduled contest while keeping the early motion's own 12-turn precondition. |
| 2.1 | 2026-10-28 | Final 06B micro-correction. **Election-state consistency:** DMP-178, DMP-181, DMP-204, DMP-235, DMP-236 and register F-PD-039 now state that `NORMAL` **and** `ELECTORAL` are resolving states — a due contest resolves in the very state its preparation created — and the superseded `NORMAL`-only condition is removed everywhere, including the requirements register. **Anchor:** DMP-177, DMP-241 and DMP-271 use `scheduled_contest_turn + 240 × k`, never the resolution turn. **Dormancy:** DMP-181a publishes the catch-up multiplier and its table, DMP-181b the one-window rule and the never-in-the-past guarantee, so a returned nation never faces an overdue contest, a campaign that opens in the past or a burst of elections. **Arithmetic:** the rejected batch-cap model in DMP-246, E41, E42 and the checker uses one floor per division (`38/turn`; `+132` at 36 turns; `−324` at 48; first unpaid obligation on turn 40) and defines insolvency as a cancelled obligation, not an overdraft. **Register integrity:** Part II's rule IDs are renumbered `+39` (DMP-134…235 → DMP-173…274) to remove the collision with Part I's cross-system contracts; no design content changed in the move. **Records:** D-106…D-108, DD-120…DD-122 and UD-036 record the policy, the renumbering and the preserved election-consequence question |
| 2.0 | 2026-10-25 | Prompt 06B: elections every 240 turns on a per-nation anchor; 24-turn campaign with a 6-point platform, one rally and two advertisements; turnout weights 2,443/1,765/1,991/1,357/1,358/1,086; incumbent +200 bp and two deterministic challengers; 12-turn TRANSITION after a lost election or confidence vote; continuous legitimacy pressure with thresholds 40/35/40/42/45 and a 12-turn window; 18-turn CRISIS and 12-turn RECOVERY; the P4.4 settlement step; `political_stability_penalty_bp` as the only economic route; 31 worked examples E19–E49; the Prompt 07–15 contracts. Part I is unchanged apart from the DMP-053 term, the DMP-112 fields, the DMP-117 events and the DMP-120 invariants |

**End of B-06.** Part I is the 06A foundation; Part II is the 06B political layer; both are required for the complete Prompt 06.
