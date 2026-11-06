# B-04 — Economy, resources, treasury and national finances

**Version:** 2.0 · **Created:** 2026-10-24 · **Stage 2, Prompt 04** · **Revised:** 2026-11-04 (v2.0 Prompt 10B-C2 protects civilian Food from `OP-09`: **ECN-081**/**ECN-082** reserve the field ration only from the surplus above the protected civilian requirement, test the actual stock at P3.6 and release reservations in reverse acceptance order, and **ECN-108** defines `fixed_asset_book_value` as the sum of city infrastructure carrying values plus other recognised fixed assets, with the zero-cost opening lot, the facility exclusion and no impairment reversal. No tax, production, maintenance or other coefficient changed. The v1.9 text follows for history: v1.9 Prompt 10B-C integrates the military Food ration without changing any inherited coefficient: **ECN-019** and **ECN-028** record Food as a military sink; **ECN-081/082/083/084** correct the consumption sub-phase to **P3.6**; **ECN-105** and **ECN-144/145/152** place the military ration at **P3.7 rank 6(a)**, before readiness upkeep at **6(b)**; **ECN-214** hands the ration quantity and the `RATION_SHORT` consequence to B-10, which owns them under F-WR-036. No tax, production, maintenance, reservation or ledger rule changed. The v1.8 text follows for history: v1.8 Prompt 09B-M records that the purpose-limited operational-funding boundary is authorized by `D-141`, a later amendment to `D-140`, and that no AOP purpose has an approved cost schedule or is currently spendable; tax and donation value is received and accounted for and remains in the Alliance Receiving Ledger, the four categories are receipt/accounting records, the AOP labels, permission name and reservation/settlement mechanics are project technical design choices rather than owner selections, and general treasury authority remains Open under `UD-046`; **ECN-213a** also specifies cumulative fractional accrual for multiple same-asset production events, where each event's tax is the increment of the floored cumulative liability and the event taxes reconcile to the per-turn floor. The v1.7 text follows for history: v1.7 Prompt 09B-L corrects the Alliance Receiving Ledger and economy integration: **ECN-213a** now distinguishes `RECEIVED`, `AVAILABLE`, `RESERVED` and `EXPENDED`, makes the only debit a purpose-limited operational expense to a registered platform cost sink, makes bracket assignment per Alliance, and adds Crowns examples at 0%, 50% and 100% with opening balances, maintenance, insufficient post-tax funds, no negative balance and retry/reconciliation. The regulation does not create debt, forced borrowing, confiscation, general withdrawal or a capacity limit, and `UD-046` remains Open for ownership, custody, capacity, general withdrawal, general spending, distributions and dual approval. No national tax, coefficient or production-ordering rule changed. The v1.6 text follows for history: v1.6 Prompt 09B-K completes the `D-140` alliance-tax integration: **ECN-213a** now fixes the seven-step settlement sequence (snapshot, authoritative gross, per-asset rate and attribution, one ARL credit, net national available, later stages consume only post-tax available, atomic paired events/receipt/audit), states that a 100% rate leaves zero for later same-turn consumption, that existing stockpiles and already-taxed inputs are never re-taxed, that a newly generated different output is taxed once at its own rate, and adds the provisional `UD-040` multiple-membership safeguard (at most one deduction per eligible production event, never more than 100% of gross, no Alliance priority, ambiguous attribution uses a visible recorded 0% fallback while gross is credited in full, normal collection resumes at the first later unambiguous turn, no retroactive re-tax, reversible and not a UD-040 resolution). **ALF-21**, **ALF-23** and **ALF-24** are aligned to the production-tax and receipt model. No national tax, transfer, reservation, ledger, conservation, fee, recipe or production-ordering rule changed. The v1.5 text follows for history: v1.5 Prompt 09B-J clarifies the `D-140` alliance-tax integration: **ECN-213a** now specifies automatic per-turn collection from current-turn production only, with player-created brackets, separate Crowns and resource rates of 0–100% in basis points, role permissions, a frozen pre-P3 snapshot, no per-policy owner consent and a credit-only Alliance Receiving Ledger that assumes no capacity limit; **ECN-100**, **ECN-144/ECN-145**, **ECN-146**, **ECN-148** and **ECN-150** name the withholding points without changing any national tax, transfer, reservation, ledger, conservation, fee or production-ordering rule. The v1.4 text follows for history: v1.4 Prompt 09B-I records the owner-authorized alliance taxation and voluntary-donation capability under `D-140` in **ECN-213a**, clarifies ECN-100's tax sentence, and changes no national rule. The v1.3 text follows for history: v1.3 closes the maintenance-allocation ambiguity with **ECN-147a**: maintenance is one whole obligation per chain, attempted in the settlement order extraction → generation → processing, paid in full or cancelled in full, with the engine continuing past an unaffordable chain exactly as ECN-105 does for a batch; the standard-start 1-crown case pays the oil chain and leaves the other five `UNMAINTAINED`. No coefficient changed. Earlier: 2026-10-25 — v1.2 clarifies the manual-capacity contract after an independent review: ECN-053 states that a reservation occupies a slot inside capacity, ECN-060 defines `planned_batches = M + A ≤ C` instead of “capacity plus manual orders”, and Example 12 proves the difference numerically; no rule or coefficient changed. Earlier: v1.1 numerical correction pass — starting bundle, Examples 2/3/5, related totals; see ECN-230)
**Status:** **Draft** — design specification. **No rule here is implemented, migrated or runtime-tested.**
**Bible part:** B-04 · **Authoritative for:** economic philosophy, the 11-resource roster, production and manufacturing, power, food accounting, treasury and financial accounting, inventory and storage, economic actions, the two-hour economic settlement, the append-only ledger, economic reporting, economic balance and the economic contracts with Prompts 05–15.
**Companions:** [research report](research/04_politics_and_war_economy_research.md) · [formula and balance register](10_economic_formula_and_balance_register.md) · [B-02 turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [B-03 account and nation lifecycle](09_account_onboarding_nation_creation_and_progression.md) · [requirements](../stage-2/03_requirements_traceability.md) · [decision register](../stage-2/04_approved_and_provisional_decisions.md)

---

## 1. Purpose and scope

**ECN-001 — What this document is.** *Provisional (REQ-098…REQ-142).* This is the authoritative economic rulebook for Nation Supremacy. It defines how the 11 core resources are produced, converted, stored, consumed, valued, reported and audited; how the national treasury behaves; how economic actions are accepted and resolved; and how the shared two-hour boundary settles a nation's economy. It is written so that a future developer can implement the economy without inventing a rule or contradicting B-02 or B-03.

**ECN-002 — What this document is not.** *Provisional.* It is **not** an implementation, a database schema, a migration, a deployment, a market design, a building catalogue, a population model or a warfare model. It defines the **economic contract** for those systems, not their full rules. In particular:

| Area | Owner | What B-04 provides |
|---|---|---|
| Turn identity, phases, reservation, failure codes, idempotency | B-02 (Prompt 02) | The economic use of P3 and P4, and the internal P3 order |
| Accounts, nation creation, reroll, starting-state structure | B-03 (Prompt 03) | The starting **numbers** and the economic reset boundary |
| Buildings, slots, capacity acquisition, upgrades, research | Prompt 05 | The economic coefficients and the capital/operating distinction |
| Population, stability, tax policy, food politics | Prompt 06 | Food demand, hunger penalty and the tax formula's economic side |
| Market, prices, offers, fees | Prompt 07 | The accounting contract and the reference-price band |
| Diplomacy, alliances | Prompts 08–09 | The transfer and audit contract; no new diplomacy rules |
| Warfare, readiness, campaigns | Prompt 10 | The demand structure for gasoline, ammunition, steel and aluminium; no quantities |
| Events, rankings, objectives | Prompt 11 | The rule that rewards cannot bypass the ledger |
| Fair play, administration, audit access | Prompt 12 | The ledger and anomaly evidence |
| Screens, journeys, warnings | Prompt 13 | Report definitions and forecast semantics |
| Final numbers and balance simulation | Prompt 14 | The register, examples and balance targets to validate |
| Bible assembly | Prompt 15 | This document as B-04 authority |

**ECN-003 — Success condition.** *Provisional.* The economy is adequately specified when: (a) every one of the 11 resources has a complete lifecycle; (b) every manufactured good has a precise recipe; (c) every monetary and resource change has an accounting treatment; (d) a boundary can be computed deterministically and idempotently; (e) every change is auditable; (f) a new nation can survive and grow; (g) a mature nation faces real costs; and (h) no strategy is forced and no strategy is free.

---

## 2. Source documents and design authority

**ECN-004 — Inheritance.** *Provisional.* This document inherits, and may not contradict:

| Source | What it fixes | How B-04 uses it |
|---|---|---|
| [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) | Two-hour UTC slots, P0–P7 phases, reserve-at-acceptance, `F1`–`F10`, idempotency keys, digest content, one outcome per turn | Every economic action and every settlement step uses these rules unchanged |
| [B-03](09_account_onboarding_nation_creation_and_progression.md) | One account/one active nation, standard starting-state **structure**, instant reroll with total reset, protection, data classes | B-04 fills the economic numbers and enforces the reset boundary |
| [Report 07](../stage-1/07_economy_design_and_market_structure.md) | One treasury pool, no debt, no interest, four material **roles**, directed-first trade, finance-interface six number types | B-04 adopts the treasury and no-debt posture; retires the four-class **resource list** in favour of the 11 mandatory resources; keeps the role taxonomy |
| [Report 08](../stage-1/08_security_privacy_fair_play_and_trust.md) | Server-authoritative value, per-resource authorization, atomic single-spend, permanent audit spine | B-04's reservation and ledger rules implement the economic part |
| [DECISIONS.md](../DECISIONS.md) | D-008 (Cloudflare + Supabase), D-014 (autonomous policy), D-015 (OP), D-016/D-017 (trade), D-019 (income before upkeep), D-024 (no shared action budget), D-026 (retention), D-032/D-039 (account/reroll) | Binding constraints; no reopening |
| [Formula register](10_economic_formula_and_balance_register.md) | The definitive version of every formula cited here | B-04 summarises; the register is authoritative for the expression |

**ECN-005 — Conflicts resolved by this document.** *Provisional.* The following conflicts existed in the records. Each is resolved here and recorded as a decision in §24; no earlier text is silently rewritten.

| # | Conflict | Resolution |
|---|---|---|
| 1 | Report 07 defines **four material classes** (MAT-01…MAT-04); Prompt 04 mandates **11 named resources** | The 11 resources are the **physical resource list**. The four classes survive only as a **role taxonomy** in the register (sustenance, construction, industrial, ordnance). No resource is renamed, removed or merged. D-044 |
| 2 | Report 07 says "zero debt"; Prompt 04 asks for a debt decision | **No debt.** Treasury floors at zero; unpaid obligations are cancelled with a disclosed consequence. D-050 |
| 3 | B-03 fixes the starting-state **structure** but no numbers | B-04 sets the numbers (D-063) and preserves every structural row |
| 4 | B-02 places production/income at P3 and obligations after it (D-019) | B-04 places **tax income → production → power → processing → food → obligations** inside P3. Income still precedes obligations; production is discretionary and precedes mandatory upkeep. D-054 |
| 5 | B-02's `TR-070` says obligations draw only on unreserved funds; production also needs money | Production is **discretionary** and draws only on unreserved funds; **accepted manual orders** reserve their money and are protected from obligations. D-053 |
| 6 | Report 07 calls "crowns" a placeholder and defers naming | The currency is named the **crown** (plural crowns, internal `crown`). D-049 |
| 7 | Report 07's storage model has per-class buffers; Prompt 04 requires storage rules for 11 resources | One **shared warehouse capacity** in units; no per-resource cap and no decay. D-052 |
| 8 | P&W uses continent-gated resources; Nation Supremacy is mapless | No geographic gating; every nation can build every extraction capacity at a rising cost. D-044/D-046 |

**ECN-006 — Status discipline.** *Provisional.* "Provisional" means the design position is selected but not implemented, tested or balanced. No sentence in this document may be read as "the economy works". The only executed work in Prompt 04 is document validation (§25). Nothing here has been run against a database, a scheduler or a player.

---

## 3. Established constraints

**ECN-007 — Fixed constraints.** *Approved constraints (not new decisions).*

1. One shared world; no shards, realms or private timelines (B-02).
2. One global turn every **two hours**, aligned to UTC; 12 turns/day (B-02, REQ-015).
3. The world is **fictional and mapless**; no coordinates, continents or geographic resource rolls (REQ-041).
4. **Cloudflare Pages + Supabase** are the fixed platform (D-008/D-009/D-010); `pg_cron` is the only turn scheduler (D-008).
5. **Free-first** operation; no paid plan may be a routine requirement (D-022; the ₹0 target is a constraint, not a capacity guarantee).
6. **One account, one active nation** per person (D-032); shared-IP restrictions follow B-03 (D-034…D-037).
7. A reroll keeps the account, destroys the nation's assets and progression, and grants only the standard bundle to the replacement (D-039; B-03).
8. **Operations Points** are the military-only action resource; the model is approved (D-015), the values are Prompt 10/14's. B-04 does not create a general action currency (D-024).
9. Detailed market, building, population and warfare rules belong to Prompts 07, 05, 06 and 10 respectively.
10. No production implementation, migration, credential or deployment change is made in Stage 2.

**ECN-008 — What "free-first" does not mean.** *Provisional.* The design may not claim that the free tier supports unlimited players, transactions or storage. B-04 is written to be **budget-aware**: one digest row per nation-turn, bounded ledger events, no per-tick polling, no unbounded per-action history. Actual capacity remains a Stage 3 measurement (CF-01/CF-03/CF-07).

---

## 4. Research summary and the design stance

**ECN-009 — The reference is a pattern source, not a template.** *Provisional.* The [research report](research/04_politics_and_war_economy_research.md) establishes that Politics & War uses the same 11-resource shape, simple multiplicative manufacturing, power as a prerequisite, population-based income, a binary food penalty and per-resource stockpile caps. Nation Supremacy **adopts the chain shape, the capacity-unit idea, the power concept and the demand structure**, and **rejects** geographic gating, a revenue-neutral tax slider, silent overflow loss, pollution as a hidden second meter, and multi-day real-time cooldowns.

**ECN-010 — What we deliberately do differently.** *Provisional.*

| P&W pattern | Nation Supremacy choice | Why |
|---|---|---|
| Continent-gated raw resources | Investable capacity for every resource | The world is mapless; a birth roll would be unfair and unlegible |
| Mass-gaining conversions (3 oil → 6 gasoline) | Mass-losing, value-adding conversions (10 oil → 8 gasoline) | Physical conservation is honest; the margin comes from usefulness, not from created mass |
| Binary "out of food" ×0.67 | Graduated 0–30% next-turn tax penalty | Forecastable, recoverable, no cliff |
| Revenue-neutral tax rate | Real tax formula with a stability trade-off | A displayed choice must change an outcome |
| Per-resource cap with silent loss | Shared warehouse, blocked batch, no loss | Silent loss is prohibited |
| Pollution meter | No pollution in B-04; power and money are the pressure | Avoid a second system Prompt 06 has not designed |
| Multi-day city cooldown | No multi-day economic cooldown | Absence-tolerant design |

**ECN-011 — The economy's one-sentence story.** *Provisional.* *A nation taxes its people, spends that money to extract raw goods and generate power, converts raw goods into manufactured goods, feeds its population, maintains its capacity, and trades the surplus; every crown and every unit is recorded, and the boundary settles the whole chain in a fixed order.*

---

## 5. Economic philosophy and design principles

**ECN-012 — Production first, trade second, war third.** *Provisional.* The economy must be **solvent without trade**. A nation that never trades can still feed its people, build capacity and grow, but it forgoes the **margins** and **speed** that specialization and trade provide. This is the Stage 1 "autarky floor" carried into rules: trade is materially lucrative, never structurally mandatory for survival.

**ECN-013 — A closed monetary loop.** *Provisional.* New crowns are created only by: (a) the one-time standard starting grant; (b) **tax income** at P3; (c) a rare, disclosed, system-generated event adjustment approved by Prompt 11; and (d) an administrative correction recorded in the ledger. Everything else **transfers** crowns (trade, aid, indemnity) or **destroys** them (operating costs, maintenance, construction, military upkeep, fees). There is no interest, no yield on cash, no activity reward and no idle-income mechanic. This is the Stage 1 C1–C4 accounting identity carried forward.

**ECN-014 — Scarcity is structural, not geographic.** *Provisional.* Every nation can build every extraction and processing capacity. What differs is **cost**: capacity has a rising marginal cost, power has a fuel cost, processing has an input cost, and storage has a space cost. Specialization is cheaper because it concentrates capacity, power and logistics; it is not a birthright. No nation is permanently locked out of a resource.

**ECN-015 — Every lever must change an outcome.** *Provisional.* Every player-facing economic control must state (a) what it changes, (b) when it changes it, and (c) what it cannot change. A control that is decorative is a defect. The tax rate, production policy, power mix, storage, pricing and construction choices all satisfy this test; the document names the effect of each.

**ECN-016 — Absence tolerance.** *Provisional.* No economic action may require the player to be present at a boundary. Production runs from **standing policies**; manual orders are optional bursts; there is no per-turn click requirement, no real-time cooldown longer than a technical anti-automation limit, and no decay for absence. A player who misses a week finds a digest, not a ruined nation.

**ECN-017 — Liquidity is not wealth.** *Provisional.* The treasury is **liquid**; inventory and fixed assets are **illiquid**. A nation can be wealthy and unable to pay a bill, or liquid and poor. Both facts are displayed separately. Insolvency is a **liquidity** state, not a deletion state: a nation with no crowns can still own farms, food and capacity, and can recover by selling, idling or rebuilding.

**ECN-018 — Stocks are for use.** *Provisional.* Storage is finite and shared. Hoarding is allowed but consumes space that could hold something else. There is no bonus for holding resources and no spoilage by default; the cost of hoarding is **opportunity**, not decay.

**ECN-019 — War consumes value; it does not create it.** *Provisional.* Military operations consume gasoline, ammunition, steel and aluminium, military upkeep consumes crowns, and a garrison consumes Food at P3.7. No war action mints money or resources. A war may damage a city's infrastructure under Prompt 10, and that damage impairs book value without transferring or creating value; it cannot create anything outside the ledger. This is the economic side of D-023's bounded-conflict posture.

**ECN-020 — Fairness boundary.** *Provisional.* The economy must not create a repeatable advantage from account creation, rerolling, shared networks or starter grants. The standard bundle is granted once per nation; a replacement receives only the standard bundle; no old asset, reservation or pending order transfers; sanctions and pair restrictions survive. The detailed anti-abuse rules are B-03's, and B-04 adds the **economic** reset and audit rules in §21.

**ECN-021 — Balance is multiple viable strategies, not equality.** *Provisional.* The target is not "every strategy earns the same". It is: at least three viable early paths (food/agriculture, energy/refining, metals/construction), at least two viable mid-game paths (specialized exporter, diversified self-sufficient), and no single chain that dominates in every circumstance. The balance metrics and simulation plan are in §18 and the register.

**ECN-022 — The eight economic principles later prompts must respect.** *Provisional.*

| # | Principle | Binding consequence |
|---|---|---|
| P1 | **Survival floor** — a nation can always feed its people if it invests in food capacity | No design may make food dependent on another player's goodwill |
| P2 | **Specialization premium** — focus lowers average cost | Prompt 05 may add a concentration bonus, but it may not break the recipes |
| P3 | **No free money** — no interest, idle yield or activity reward | Prompt 11 rewards must be one-time, disclosed and ledgered |
| P4 | **Liquidity ≠ wealth** — both displayed | Prompt 13 must show treasury, available, reserved, inventory and wealth separately |
| P5 | **Stocks are for use** — storage is finite | Prompt 05 owns warehouse expansion; no infinite storage |
| P6 | **War is a sink** — no value creation | Prompt 10 may consume and transfer, never mint |
| P7 | **Explain every number** — formula or rule | Prompt 13 must show provenance for every digest line |
| P8 | **Fairness boundary** — no starter/reroll advantage | Prompt 12 audits the boundary; B-04 enforces the economics |

---


## 6. The 11-resource roster

**ECN-023 — The roster is closed.** *Approved constraint; design details provisional (REQ-099…REQ-109).* The starting economy contains **exactly eleven** resources: seven raw goods and four manufactured goods. They may not be removed, renamed, merged or replaced. Adding a twelfth resource requires a new decision, a new lifecycle, a new storage rule and a new formula-register entry; it may not be slipped into a later prompt.

**ECN-024 — Classification.** *Provisional.* A **raw good** is extracted or harvested from national capacity and does not require a manufactured input. A **manufactured good** is produced by a processing chain that consumes at least one raw good (and may consume another manufactured good only where a recipe explicitly says so). The classification is fixed:

| # | Display name | Internal ID | Class | Primary role | Reference price (crowns/unit) |
|---|---|---|---|---|---|
| 1 | Food | `food` | Raw | Population staple | 1 |
| 2 | Coal | `coal` | Raw | Steel, ammunition, coal power | 1 |
| 3 | Oil | `oil` | Raw | Gasoline refining, oil power | 2 |
| 4 | Uranium | `uranium` | Raw | Nuclear power | 30 |
| 5 | Lead | `lead` | Raw | Ammunition, nuclear shielding | 3 |
| 6 | Bauxite | `bauxite` | Raw | Aluminum smelting | 2 |
| 7 | Iron | `iron` | Raw | Steel | 1 |
| 8 | Gasoline | `gasoline` | Manufactured | Construction fuel, military fuel, trade | 6 |
| 9 | Ammunition | `ammunition` | Manufactured | Readiness and campaigns | 6 |
| 10 | Steel | `steel` | Manufactured | Construction, military equipment | 7 |
| 11 | Aluminum | `aluminum` | Manufactured | Advanced construction, military equipment | 8 |

**ECN-025 — Units and precision.** *Provisional (REQ-100).* Every resource is measured in **whole units** (an integer). There is no fractional resource, no fractional crown and no floating-point inventory. A unit is an abstract quantity, not a real-world tonne or bushel; the game never converts it to a physical unit. All arithmetic is integer arithmetic with an explicit floor or ceiling rule per formula. The formula register is authoritative for every rounding rule.

**ECN-026 — Identifiers are stable.** *Provisional.* The internal IDs in the table are the stable identifiers used by the engine, the ledger, the API and every later document. Display names may be localised by Prompt 13; the internal IDs may not change. The display spelling is **Aluminum** (the mandatory roster's spelling); a localisation may display "Aluminium" but the ID remains `aluminum`.

**ECN-027 — Reference prices are book values, not market prices.** *Provisional (REQ-110).* The reference price is the **accounting book value** of one unit for national-wealth reporting, fair-value checks and internal cost comparisons. It is **not** a market price, a price floor, a price ceiling or a promise that a unit can be sold for that amount. Prompt 07 owns the market. A trade at any price transfers value at that price; the difference from book value is a realised gain or loss, reported but not minted.

**ECN-028 — No resource is permanently worthless.** *Provisional (REQ-099).* Every resource must have at least one **sink** (a rule that consumes it) and at least one **strategic decision** (a choice whose outcome depends on it). The sinks are: food → population, garrison rations and `OP-09` field rations; coal → steel, ammunition, coal power; oil → gasoline, oil power; uranium → nuclear power; lead → ammunition, nuclear shielding; bauxite → aluminum; iron → steel; gasoline → construction fuel, military fuel; ammunition → readiness/campaigns; steel → construction, military equipment; aluminum → advanced construction, military equipment. If a later prompt removes a sink, it must add another before the removal takes effect.

**ECN-029 — The four material roles survive as a taxonomy, not a roster.** *Provisional.* Report 07's MAT-01…MAT-04 classes are retained only as **roles**: Sustenance (`food`), Construction (`steel`, `aluminum`), Industrial (`coal`, `oil`, `iron`, `bauxite`, `lead`, `uranium`), Ordnance (`gasoline`, `ammunition`). The taxonomy is used in balance analysis and in the trade contract; it does not create a second resource list and does not rename any resource.

---


## 7. Resource lifecycle profiles

**ECN-030 — How to read a profile.** *Provisional.* Each profile answers the twenty questions required by the Prompt 04 brief. "Automatic" means a standing production policy runs it at P3; "ordered" means a manual order can also run it; "both" means both paths exist. "Interval" is always the shared two-hour boundary. A resource's **capacity** is the number of batches per turn; a batch's output is fixed by its recipe.

### 7.1 Food (`food`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Food** / `food` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Food capacity (farms); trade; starting bundle; event reward |
| 5. Facilities / conditions | Food capacity owned by Prompt 05; no power required; no geographic condition |
| 6. Inputs | None (sun, land and labour are abstracted) |
| 7. Money / operating | 12 crowns per batch; plus 1 crown capacity maintenance per batch per turn |
| 8. Automatic or ordered | **Both** — standing policy or manual order |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Population demand `ceil(population / 1000)` per turn; no other mandatory sink |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse only; no food-specific cap |
| 13. Trade | Yes (Prompt 07) |
| 14. Transfer / gift / embargo | Transferable under Prompt 07/08; a famine-relief gift is a normal transfer; an embargo is Prompt 08 |
| 15. Strategic significance | Survival resource; a food shortfall hits tax income and (Prompt 06) stability |
| 16. Progression role | Early: secure the food floor. Mid: sell surplus or diversify. Late: buffer against war and blockade |
| 17. Shortage | Graduated hunger penalty (§11); never instant collapse; no death spiral by design |
| 18. Supply/demand evolution | Demand grows slowly with population; supply grows with capacity; price is low and stable |
| 19. Governing rules | ECN-066…ECN-079; F-EC-002/003; D-049 |
| 20. Edge cases | Zero population (no demand); food at zero (max penalty, next-turn recovery); warehouse full (batch blocked, no loss) |

### 7.2 Coal (`coal`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Coal** / `coal` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Coal capacity (mines); trade; starting bundle |
| 5. Facilities / conditions | Coal capacity owned by Prompt 05; no power required |
| 6. Inputs | None |
| 7. Money / operating | 10 crowns per batch; 1 crown maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Steel recipe (6 per batch); ammunition recipe (4 per batch); coal generator (6 per level per turn) |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes |
| 14. Transfer / gift / embargo | Transferable; a strategic export good |
| 15. Strategic significance | The industrial fuel: steel, ammunition and cheap power all depend on it |
| 16. Progression role | Early: cheap power. Mid: steel feedstock. Late: a blockade-sensitive input |
| 17. Shortage | Processing chains idle; coal generators stop; no partial fuel burn |
| 18. Supply/demand evolution | Demand rises with steel and ammunition capacity; supply is cheap to expand |
| 19. Governing rules | ECN-048…ECN-060; F-EC-007/011; D-045 |
| 20. Edge cases | Exactly enough coal for a generator (runs); one unit short (generator does not run); coal reserved by a manual order (unavailable to standing policy) |

### 7.3 Oil (`oil`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Oil** / `oil` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Oil capacity (wells); trade; starting bundle |
| 5. Facilities / conditions | Oil capacity owned by Prompt 05; no power required |
| 6. Inputs | None |
| 7. Money / operating | 14 crowns per batch; 1 crown maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Refining recipe (10 per batch); oil generator (5 per level per turn) |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes |
| 14. Transfer / gift / embargo | Transferable; a strategic export good |
| 15. Strategic significance | The fuel fork: burn it for power or refine it for gasoline |
| 16. Progression role | Early: cheap power. Mid: refining margin. Late: military-fuel supply |
| 17. Shortage | Refining idles; oil generators stop; gasoline supply tightens |
| 18. Supply/demand evolution | Demand rises with refining and power; oil is the most "dual-use" raw good |
| 19. Governing rules | ECN-048…ECN-060; F-EC-007/011; D-045 |
| 20. Edge cases | Oil reserved for refining vs burned for power (reservation wins); refinery input shortage (batch skipped, oil retained) |

### 7.4 Uranium (`uranium`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Uranium** / `uranium` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Uranium capacity (mines); trade; event reward |
| 5. Facilities / conditions | Uranium capacity owned by Prompt 05; nuclear generator requires Prompt 05's plant |
| 6. Inputs | None for extraction |
| 7. Money / operating | 28 crowns per batch; 1 crown maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Nuclear generator: 1 uranium per level per turn |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes, but concentrated demand: only nuclear powers and strategic stockpilers buy it |
| 14. Transfer / gift / embargo | Transferable; an embargo is a meaningful strategic act (Prompt 08) |
| 15. Strategic significance | The only fuel that produces high-density power without coal or oil; also a dual-use strategic material (Prompt 10 may add deterrence demand) |
| 16. Progression role | Mid: first nuclear plant. Late: high-output grid and strategic reserve |
| 17. Shortage | Nuclear plants stop; grid falls back to coal/oil; no partial uranium burn |
| 18. Supply/demand evolution | Demand is lumpy (one plant level consumes one unit); supply is expensive, so nuclear is a commitment |
| 19. Governing rules | ECN-039…ECN-047; F-EC-011; D-047 |
| 20. Edge cases | One mine feeding one plant level; uranium reserved for a plant (unavailable for trade); plant idle without fuel but still pays maintenance |

### 7.5 Lead (`lead`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Lead** / `lead` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Lead capacity (mines); trade; starting bundle |
| 5. Facilities / conditions | Lead capacity owned by Prompt 05 |
| 6. Inputs | None |
| 7. Money / operating | 16 crowns per batch; 1 crown maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Ammunition recipe (8 per batch); nuclear generator shielding (1 per level per turn) |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes |
| 14. Transfer / gift / embargo | Transferable; a strategic military input |
| 15. Strategic significance | The ammunition feedstock; the second use as nuclear shielding prevents it from being purely military |
| 16. Progression role | Early: cheap military stock. Mid: ammunition line. Late: nuclear grid + war reserve |
| 17. Shortage | Ammunition plant idles; nuclear plant stops if shielding unavailable |
| 18. Supply/demand evolution | Demand rises with ammunition capacity and nuclear power; lead is the clearest "war or power" fork |
| 19. Governing rules | ECN-048…ECN-060; F-EC-007/011; D-047 |
| 20. Edge cases | Lead reserved for ammunition vs shielding (reservation wins); ammo plant with 7 lead cannot run an 8-lead batch |

### 7.6 Bauxite (`bauxite`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Bauxite** / `bauxite` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Bauxite capacity (mines); trade; starting bundle |
| 5. Facilities / conditions | Bauxite capacity owned by Prompt 05 |
| 6. Inputs | None |
| 7. Money / operating | 14 crowns per batch; 1 crown maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Aluminum recipe (12 per batch) |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes |
| 14. Transfer / gift / embargo | Transferable |
| 15. Strategic significance | The only route to aluminum; aluminum is the advanced-construction and military-airframe input |
| 16. Progression role | Mid: first smelter. Late: advanced construction and military |
| 17. Shortage | Smelter idles; aluminum supply tightens; advanced construction is delayed |
| 18. Supply/demand evolution | Demand is low early and rises sharply when advanced construction unlocks |
| 19. Governing rules | ECN-048…ECN-060; F-EC-007; D-046 |
| 20. Edge cases | 11 bauxite cannot run a 12-bauxite batch; bauxite is never consumed by power |

### 7.7 Iron (`iron`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Iron** / `iron` |
| 2. Class | Raw good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Iron capacity (mines); trade; starting bundle |
| 5. Facilities / conditions | Iron capacity owned by Prompt 05 |
| 6. Inputs | None |
| 7. Money / operating | 10 crowns per batch; 1 crown maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Steel recipe (10 per batch) |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes |
| 14. Transfer / gift / embargo | Transferable |
| 15. Strategic significance | The steel feedstock; steel is the universal construction input |
| 16. Progression role | Early: first steel line. Mid: construction boom. Late: military equipment |
| 17. Shortage | Steel mill idles; construction slows; no substitute |
| 18. Supply/demand evolution | Demand tracks construction and steel exports; supply is cheap to expand |
| 19. Governing rules | ECN-048…ECN-060; F-EC-007; D-046 |
| 20. Edge cases | Iron and coal must both be present for a steel batch; one missing blocks the batch and consumes neither |

### 7.8 Gasoline (`gasoline`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Gasoline** / `gasoline` |
| 2. Class | Manufactured good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Refining recipe; trade; starting bundle |
| 5. Facilities / conditions | Refining capacity (Prompt 05) + grid power |
| 6. Inputs | 10 oil per batch |
| 7. Money / operating | 20 crowns per batch; 2 crowns maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Construction site fuel (Prompt 05); military fuel (Prompt 10); trade |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes; a liquid, high-value export |
| 14. Transfer / gift / embargo | Transferable; an embargo can stall a war economy |
| 15. Strategic significance | The link between oil and mobility; the first manufactured good most nations can make |
| 16. Progression role | Early: first manufactured export. Mid: construction fuel. Late: war stock |
| 17. Shortage | Refining continues (gasoline is output, not input); construction projects that require it are blocked or delayed per Prompt 05; military readiness falls per Prompt 10 |
| 18. Supply/demand evolution | Demand rises with construction and war; supply is easy to expand once refining exists |
| 19. Governing rules | ECN-048…ECN-060; F-EC-006/007/008; D-046 |
| 20. Edge cases | Zero gasoline does not stop refining; a construction order with a gasoline cost cannot be accepted without the gasoline |

### 7.9 Ammunition (`ammunition`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Ammunition** / `ammunition` |
| 2. Class | Manufactured good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Ammunition recipe; trade; event reward |
| 5. Facilities / conditions | Ammunition capacity (Prompt 05) + grid power |
| 6. Inputs | 8 lead + 4 coal per batch |
| 7. Money / operating | 20 crowns per batch; 2 crowns maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Military readiness and campaigns (Prompt 10); trade |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes, but demand is concentrated in armed nations and alliances |
| 14. Transfer / gift / embargo | Transferable; an embargo is a strategic act |
| 15. Strategic significance | The "can we fight?" stock; a nation with money but no ammunition is not ready |
| 16. Progression role | Mid: first ammunition line. Late: war reserve and alliance support |
| 17. Shortage | Readiness falls and campaigns are constrained (Prompt 10); no economic collapse |
| 18. Supply/demand evolution | Demand is cyclical: low in peace, high before and during war |
| 19. Governing rules | ECN-048…ECN-060; F-EC-006/007/008; D-046 |
| 20. Edge cases | Seven lead cannot run an eight-lead batch; ammunition is never consumed by production |

### 7.10 Steel (`steel`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Steel** / `steel` |
| 2. Class | Manufactured good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Steel recipe; trade; starting bundle |
| 5. Facilities / conditions | Steel capacity (Prompt 05) + grid power |
| 6. Inputs | 10 iron + 6 coal per batch |
| 7. Money / operating | 24 crowns per batch; 2 crowns maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Construction and upgrades (Prompt 05); military equipment (Prompt 10); trade |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes; the most liquid manufactured good |
| 14. Transfer / gift / embargo | Transferable |
| 15. Strategic significance | The universal construction input; a steel shortage slows everything |
| 16. Progression role | Early: first construction. Mid: export staple. Late: military equipment |
| 17. Shortage | Construction projects blocked or delayed (Prompt 05); military production constrained (Prompt 10) |
| 18. Supply/demand evolution | Demand is broad and steady; steel is the safest manufacturing business, and therefore the most competitive |
| 19. Governing rules | ECN-048…ECN-060; F-EC-006/007/008; D-046 |
| 20. Edge cases | Steel is not consumed by any generator; a steel batch with 9 iron fails and consumes nothing |

### 7.11 Aluminum (`aluminum`)

| Field | Rule |
|---|---|
| 1. Name / ID | **Aluminum** / `aluminum` |
| 2. Class | Manufactured good |
| 3. Unit / precision | Whole units; integer |
| 4. Sources | Aluminum recipe; trade; event reward |
| 5. Facilities / conditions | Smelting capacity (Prompt 05) + grid power |
| 6. Inputs | 12 bauxite per batch |
| 7. Money / operating | 24 crowns per batch; 2 crowns maintenance per batch per turn |
| 8. Automatic or ordered | Both |
| 9. Interval | Every boundary (P3) |
| 10. Consumption | Advanced construction and upgrades (Prompt 05); military equipment (Prompt 10); trade |
| 11. Storable | Yes |
| 12. Capacity limit | Shared warehouse |
| 13. Trade | Yes; a high-value, lower-volume good |
| 14. Transfer / gift / embargo | Transferable |
| 15. Strategic significance | The advanced-construction gate; a nation without aluminum cannot build the highest tiers |
| 16. Progression role | Mid: advanced construction. Late: military and prestige projects |
| 17. Shortage | Advanced construction is blocked or delayed; military equipment is constrained |
| 18. Supply/demand evolution | Demand is low early, then rises faster than bauxite supply, creating a trade opportunity |
| 19. Governing rules | ECN-048…ECN-060; F-EC-006/007/008; D-046 |
| 20. Edge cases | Aluminum is the most power-intensive chain; a power shortfall hits it first in percentage terms because its draw is highest |

**ECN-041 — Lifecycle completeness.** *Provisional (REQ-099).* Every resource profile above has a source, a sink, a storage rule, a trade rule, a shortage rule and at least one edge case. A later prompt that adds a new source or sink must update the profile, the formula register and the resource's requirement row; it may not leave the profile describing the old economy.

---


## 8. The production model: capacity, batches and standing policy

**ECN-042 — Capacity is measured in batches per turn.** *Provisional (REQ-111).* Each production chain has an integer **capacity** equal to the number of batches it can process in one world turn. A batch is the atomic unit: it consumes a fixed recipe and produces a fixed output. Capacity is not a percentage, a rate per hour or a float. A nation's capacity vector is the complete description of what it can produce before power, inputs and money are considered.

**ECN-043 — Capacity is acquired, not rolled.** *Provisional.* Every nation can acquire capacity in every chain. Prompt 05 owns the acquisition rules (construction, slots, prerequisites, upgrade costs). B-04 owns the **economic coefficients**: what a batch consumes, what it produces, what it costs to run, how much power it draws and how much space it needs. A nation's capacity vector is therefore an economic input, not a birthright.

**ECN-044 — Standing policy is the default.** *Provisional (REQ-112).* Each chain has one standing policy: `RUN_AT_CAPACITY`, `RUN_TO_TARGET` (a stored target per output resource) or `IDLE`. The default is `RUN_AT_CAPACITY`. A standing policy is a **recurring rule**, not an accepted action: it does not reserve money or inputs at submission, and it runs at P3 using whatever is unreserved and affordable at that moment. This is what makes the economy absence-tolerant.

**ECN-045 — Manual orders are optional bursts.** *Provisional (REQ-113).* A player may submit a **manual manufacturing order** for `n` batches of a chain, up to the chain's capacity. A manual order is an ordinary B-02 action: it is validated at submission, reserves its money, inputs and capacity at acceptance, and either runs fully at P3 or fails atomically with a B-02 failure code. Manual orders exist for bursts (a war stock, a construction push); they are never required for routine production.

**ECN-046 — Extraction formula.** *Provisional.* For each raw resource `r` with capacity `C_r`, output per batch `Y_r` and variable cost `V_r`:

```
batches_run(r) = min(C_r, floor(available_money_unreserved / V_r), space_available / Y_r)
output(r)      = batches_run(r) × Y_r
variable_cost  = batches_run(r) × V_r
```

The three limits are applied in the published priority order (§8.6). The formula is evaluated once per resource per turn; it is not a continuous market.

**ECN-047 — Processing formula.** *Provisional.* For each processing chain `c` with capacity `C_c`, input vector `I_c`, output `Y_c` and variable cost `V_c`:

```
power_batches(c)  = floor(C_c × power_supply / power_demand)      when supply < demand
                  = C_c                                            otherwise
batches_run(c)    = min(power_batches(c), input_limit(c), money_limit(c), space_limit(c))
inputs_consumed   = batches_run(c) × I_c
output            = batches_run(c) × Y_c
variable_cost     = batches_run(c) × V_c
```

`input_limit(c)` is the largest integer `k ≤ C_c` such that every input has at least `k × I_c` **unreserved** units. A manual order's reserved inputs are not available to standing policy; a standing policy's inputs are not available to a later manual order. This is the single-spend invariant (B-02 TR-068).

**ECN-048 — Affordability is per batch, not per capacity.** *Provisional.* A batch runs only if its **full** variable cost is available in unreserved crowns at the moment it is evaluated. A batch is never partially funded, partially run or run on credit. If the nation has 19 crowns and the batch costs 20, the batch does not run; the 19 crowns are not spent on a fraction.

**ECN-049 — The production priority order is published.** *Provisional (REQ-114).* When money, space or power is insufficient for every standing policy, the following fixed order applies:

1. **Food** (survival first).
2. **Coal**, **Oil**, **Iron**, **Bauxite**, **Lead**, **Uranium** (the order listed; raw materials before processing).
3. **Refining**, **Steel**, **Aluminum**, **Ammunition** (the order listed).

Within a processing chain, accepted manual orders run before standing policy, in B-02 B1 order `(submitted_at, action_id)`. The order is part of the published rulebook; it may not be changed by a hidden database order or a client-supplied sequence.

**ECN-050 — Warehouse space is checked before money and inputs are committed.** *Provisional.* A batch that would exceed the shared warehouse capacity does not run. Its money, inputs and fuel are **not** consumed, and the digest records a `SPACE_BLOCKED` line. This is the no-silent-loss rule; there is no overflow discard.

**ECN-051 — Capacity maintenance is a fixed operating expense.** *Provisional (REQ-116).* Every capacity batch costs **1 crown per turn** (extraction), **2 crowns per turn** (processing) or **2 crowns per generator level per turn**, whether or not it runs. Maintenance is charged at the start of the production sub-phase (P3.2), after tax income and from unreserved crowns, in the same fixed order. It is the economic reason not to hold idle capacity forever.

**ECN-052 — Idle capacity is allowed.** *Provisional.* A nation may set a chain to `IDLE` or simply lack inputs; idle capacity still pays maintenance but consumes nothing else. Idling is a legitimate response to a price crash, a blockade or absence. There is no penalty beyond maintenance and the opportunity cost of the missing output.

**ECN-053 — Manual orders reserve capacity.** *Provisional (REQ-115).* An accepted manual order reserves `n` batches of the chain's capacity for its turn, in addition to its money, inputs and output space. Total reserved capacity may not exceed the chain's capacity. A reservation occupies slots **inside** `C`; it never increases capacity and is never added to `C` again when planned demand is computed. If two orders would overbook the chain, the later submission is rejected at acceptance (`F5`); if a later event reduces capacity, the later order fails at P3 (`F5`) and releases everything. This extends B-02's reservation model to a non-resource capacity; it does not weaken it.

**ECN-054 — A batch is atomic.** *Provisional.* No partial batch, no partial input consumption, no partial output. A batch either runs completely or does not run. This is the economic application of B-02's zero-partial rule and Report 07's R-19 invariant.

**ECN-055 — Every production line is reported.** *Provisional (REQ-117).* The digest reports, per resource: capacity, batches planned, batches run, batches blocked and why (money, input, power or space), output, variable cost, maintenance allocated and the resulting stock. A player must be able to answer "why did my steel mill not run?" without reading the database.

---


## 9. Power and grid capacity

**ECN-056 — Grid units are a derived capacity, not a resource.** *Provisional (REQ-118).* Power is measured in **grid units (GU)**. GU is produced by generators at P3, consumed by processing batches in the same turn, and **not stored, traded, gifted or banked**. It is not a twelfth resource: it has no warehouse space, no ledger balance and no price. A nation's grid is described by its generator levels and its fuel supply.

**ECN-057 — Generator classes.** *Provisional.* The default generator classes are:

| Generator | Capacity per level | Fuel per level per turn | Variable cost per level | Maintenance per level | Notes |
|---|---|---|---|---|---|
| **Coal** `gen_coal` | 6 GU | 6 coal | 10 crowns | 2 crowns | Cheapest to build (Prompt 05), fuel-heavy, no strategic input |
| **Oil** `gen_oil` | 6 GU | 5 oil | 14 crowns | 2 crowns | Slightly cheaper fuel volume than coal, but oil competes with refining |
| **Nuclear** `gen_nuclear` | 20 GU | 1 uranium + 1 lead | 40 crowns | 2 crowns | High output, high capital (Prompt 05), consumes the two strategic raw goods |

A generator level is a capacity unit; Prompt 05 owns how many levels a nation may build, what they cost and what prerequisites they have. B-04 owns the fuel, output, variable cost and maintenance above.

**ECN-058 — A generator runs only if its full fuel is available.** *Provisional.* At P3.3, each generator level is evaluated in the fixed order **coal → oil → nuclear**. If the nation has the full fuel requirement (and the variable cost), the generator runs, consumes the fuel and produces its full GU; if not, it does not run and consumes **nothing**. There is no partial fuel burn and no fractional output. This is fail-closed, not fail-partial.

**ECN-059 — Surplus power is discarded and reported.** *Provisional.* If grid supply exceeds processing demand, the surplus is not stored and has no value. The digest reports `power_generated`, `power_used`, `power_surplus` and `power_shortfall`. Overbuilding generation is a real mistake; it burns fuel and money for nothing. This is the trade-off that makes the generator choice strategic.

**ECN-060 — Processing demand is the sum of batch draws.** *Provisional.* Each processing batch has a fixed draw:

| Chain | Draw per batch |
|---|---|
| Refining | 2 GU |
| Steel | 3 GU |
| Aluminum | 4 GU |
| Ammunition | 2 GU |

`power_demand = Σ (planned batches × draw)`, where `planned_batches = M + A ≤ C`: `M` accepted manual batches occupy slots **inside** the chain's capacity, and `A` is what the standing policy schedules in the slots they leave, both computed before derating. Manual batches are counted **once** as part of the plan, never added on top of capacity. Demand is computed once, before any processing runs.

**ECN-061 — Derating is published and pro-rata.** *Provisional (REQ-119).* If `power_supply < power_demand`:

```
power_pct = floor(100 × power_supply / power_demand)
batches_available(c) = floor(C_c × power_pct / 100)
```

Every processing chain is derated by the same percentage. There is no priority chain, no hidden "essential" list and no player-set priority that could advantage one nation over another. A chain with capacity 1 and `power_pct = 60` runs **0** batches; a chain with capacity 2 runs **1**. This floor is deliberate: a nation that cannot power a chain must build more power, not expect a fraction.

**ECN-062 — Power derating applies before input and money checks.** *Provisional.* The order is: compute demand → compute `power_pct` → compute `batches_available` → check manual orders → check inputs → check money → check space. A chain that is power-derated to zero does not consume inputs, money or space. A manual order that cannot run all its batches fails atomically (`F5`) and releases all reservations.

**ECN-063 — Manual orders have priority within the available batches.** *Provisional.* Accepted manual orders run first, in B1 order, up to `batches_available`. If the available batches are fewer than the sum of manual orders, the later orders fail with `F5`; their reservations are released and their capacity is freed for standing policy. The digest names the order and the reason.

**ECN-064 — Power is reported as a first-class number.** *Provisional (REQ-120).* The national report shows: generator levels by class, fuel consumed, grid supply, processing demand, `power_pct`, batches run and batches lost to derating. A player who wonders why production fell sees the grid number before the production number.

**ECN-065 — No grid storage or trade.** *Provisional.* GU cannot be stored, sold, gifted, reserved or carried between turns. A generator that runs with no demand wastes its fuel; a nation cannot "save" power for a later turn. This prevents a power-banking exploit and keeps the boundary deterministic.

---


## 10. Production chains and manufacturing recipes

**ECN-066 — The recipe table is authoritative.** *Provisional (REQ-121).* Every processing chain has exactly one default recipe. A recipe is a fixed integer vector; it does not vary by nation, turn or price. Later research may add an **alternative** recipe only through a new decision and a new register entry; a nation may never invent a recipe.

| Chain | Facility class (Prompt 05) | Inputs per batch | Money per batch | Power | Output per batch | Maintenance |
|---|---|---|---|---|---|---|
| **Refining** | Refinery | 10 oil | 20 crowns | 2 GU | 8 gasoline | 2 crowns |
| **Steel** | Steel mill | 10 iron + 6 coal | 24 crowns | 3 GU | 8 steel | 2 crowns |
| **Aluminum** | Smelter | 12 bauxite | 24 crowns | 4 GU | 8 aluminum | 2 crowns |
| **Ammunition** | Ammunition plant | 8 lead + 4 coal | 20 crowns | 2 GU | 10 ammunition | 2 crowns |

**ECN-067 — Refining.** *Provisional.* Ten oil become eight gasoline. The chain is the simplest manufactured good and the first most nations can build. It loses two units of mass; the value comes from gasoline's usefulness as construction and military fuel, not from volume. A refinery does **not** consume gasoline; a nation with zero gasoline can still refine.

**ECN-068 — Steel.** *Provisional.* Ten iron and six coal become eight steel. Both inputs must be present in full; if either is short, the batch does not run and neither input is consumed. Steel is the broadest construction input and the most liquid manufactured good.

**ECN-069 — Aluminum.** *Provisional.* Twelve bauxite become eight aluminum. The chain has the highest power draw (4 GU) and the highest input mass, which makes it the most infrastructure-dependent manufactured good. It is deliberately not gated by a technology at the economic layer: a nation with bauxite capacity and a smelter can make it, subject to Prompt 05's building prerequisites.

**ECN-070 — Ammunition.** *Provisional.* Eight lead and four coal become ten ammunition. Lead is the payload; coal is process heat. The recipe is the **adopted lead-based chain**; no alternative (for example a steel-cased or uranium-tipped round) is adopted at launch. Uranium's role is nuclear power, not ammunition; lead's second role is nuclear shielding.

**ECN-071 — The power chain is not a manufacturing recipe.** *Provisional.* Generators are not a processing chain: they have no warehouse output, no input reservation in the ordinary sense and no completed-goods ledger event. Their fuel consumption and GU output are recorded as `POWER_FUEL` and `POWER_GENERATED` events. A generator's fuel is checked and consumed in the same P3.3 step; it is never reserved across turns.

**ECN-072 — Candidate chains evaluated and rejected.** *Provisional.*

| Candidate | Decision | Reason |
|---|---|---|
| Oil → Gasoline | **Adopted** | The clearest value-add chain; gasoline has peacetime (construction) and wartime uses |
| Bauxite → Aluminum | **Adopted** | The only aluminum route; high power draw makes it a meaningful infrastructure commitment |
| Iron + Coal → Steel | **Adopted** | Two-input recipe creates a real coordination decision; steel is the universal construction input |
| Lead + Coal → Ammunition | **Adopted** | Lead needs a sink; coal as process heat is consistent with steel |
| Uranium → some manufactured good | **Rejected** | The four manufactured goods are fixed; uranium's meaningful role is nuclear power, not a fifth good |
| Coal + Oil → Gasoline (synfuel) | **Rejected** | It would make oil less distinctive and add a second gasoline route before the first is balanced |
| Bauxite + Coal → Steel (alternative) | **Rejected** | It would collapse the iron/bauxite distinction and make iron nearly worthless |
| Lead + Steel → Ammunition | **Rejected** | It would make ammunition a second-stage steel product and lengthen the early chain; lead + coal is simpler and still meaningful |

**ECN-073 — Uranium's purpose is explicit.** *Provisional (REQ-122).* Uranium is consumed **only** by nuclear generators in the launch economy (1 unit per generator level per turn). A nuclear generator produces 20 GU, more than three coal generator levels, and consumes no coal or oil. Uranium therefore has a clear economic role: it is the fuel that lets a nation escape the coal/oil power trade-off at a high capital and fuel cost. Prompt 10 may add a strategic deterrence demand; if it does, it must add a source/sink row and a ledger event, and it may not silently make uranium a currency.

**ECN-074 — Lead's purpose is explicit.** *Provisional.* Lead is consumed by ammunition (8 per batch) and by nuclear generator shielding (1 per generator level per turn). The second use is deliberate: without it, lead would be a purely military resource with no peacetime demand. With it, a nation choosing nuclear power also chooses a lead supply chain, and a nation choosing ammunition competes with its own reactors for lead.

**ECN-075 — Recipe invariants.** *Provisional (REQ-123).* For every recipe: inputs and outputs are integers; output is greater than zero; the recipe is not reversible at a profit; the reference-price margin is positive at the reference prices; the recipe cannot consume a good it produces (no self-loop); and the sum of input book values is less than the output book value. These invariants are checked by the formula register and a document validator.

**ECN-076 — No per-nation recipe variance.** *Provisional.* A later technology may modify **yield** or **cost** through a published modifier, but it may not change the recipe's input list. A modifier must be declared in the formula register with its source, its cap and its rounding rule. This prevents an invisible technology from making a chain unrecognisable.

**ECN-077 — Cancellation and refunds.** *Provisional (REQ-124).* A manual order may be cancelled while its turn is OPEN (B-02 §18). Cancellation releases the reserved money, inputs, capacity and output space; it charges **no fee** unless Prompt 05's construction contract says otherwise. A standing policy change is free and takes effect at the next boundary; it cannot retroactively cancel a batch that already ran. A completed batch is never refunded.

**ECN-078 — Failure and interruption.** *Provisional.* A manual order that fails at P2/P3 releases every reservation and writes a `MANUFACTURE_FAILED` event with the B-02 code. A batch interrupted by a turn-level failure is retried with the turn (B-02 `F8`); it is not half-charged. A cancelled or failed order leaves the inputs exactly as they were, except for any resource that an earlier B1 order legitimately consumed.

**ECN-079 — Output timing.** *Provisional.* A batch's output becomes available in the **same P3 step** in which it is produced, after the input consumption and the money charge. It can be used by a later P3 step (for example, coal produced before a generator runs) but **not** by an earlier step. It is never available before the boundary. This is the temporal ordering that makes the settlement deterministic.

---


## 11. Food, population and shortages

**ECN-080 — Food demand.** *Provisional (REQ-125).* One food unit feeds **1,000 people for one turn**. Demand is:

```
food_demand = ceil(population / 1000)
```

Population is owned by Prompt 06. The standard starting population is **50,000** (D-063), so starting demand is **50 units per turn**. Population growth, decline and migration are Prompt 06's; this document only consumes the current number and reports the demand. **Military Food demand is a separate obligation** owned by Prompt 10 (§9.3, F-WR-036); it is never added to `food_demand`, never affects the hunger ratio, and is paid after civilian demand at P3.7.

**ECN-081 — Food is consumed after production and after processing.** *Provisional.* **P3.6** consumes food from the post-production stock. Food produced this turn is available to feed the population this turn. Food consumed by a manual order or a trade settlement is not available for consumption; the reservation rules prevent double-counting. **P3.7 then consumes the military ration** from the Food left after P3.6; civilian demand always has priority. The `OP-09` field ration is different: it is reserved at acceptance **only from the surplus above the protected civilian requirement** (`ECN-082`, B-10 `WAR-053l`) and consumed at P5, and it is never part of either P3.6 or P3.7. If P3.6 cannot leave the protected requirement intact while the ration is held, the `OP-09` reservation is released and that action fails; civilians are never fed from Food that `OP-09` may not take.

**ECN-082 — Shortage is a ratio, not a boolean.** *Provisional.*

```
protected_civilian_food = food_demand                          = ceil(population / 1000)
food_after_other        = opening_food + food_produced − other_food_reservations
available_if_held       = food_after_other − op09_held_total
food_consumed           = min(food_after_other − op09_held_after_release, food_demand)
unmet_food              = max(0, food_demand − (food_after_other − op09_held_after_release))
shortfall_ratio         = unmet_food / food_demand          (0 when demand is 0)
```

`other_food_reservations` is Food held at P3.6 for accepted actions **other than** `OP-09`. `op09_held_total = 4 × (accepted OP-09 actions still holding their field ration)`.

The `OP-09` field ration is a **conditional claim on the surplus above the protected civilian requirement**, never a claim on the protected requirement itself (B-10 `WAR-053l`). At acceptance, B-10 reserves it only if

```
eligible_op09_surplus = opening_food + projected_food_production
                        − other_food_reservations − protected_civilian_food
```

can cover the 4 Food already held (otherwise the whole action fails `WRF-25`). At P3.6 this document runs the actual test: if `available_if_held ≥ protected_civilian_food`, every OP-09 reservation stands and `food_consumed = min(available_if_held, food_demand)`; otherwise the engine **releases** OP-09 reservations in reverse acceptance order (action ID descending, last accepted released first) until `available_if_held` would reach the protected requirement again. Each released action fails whole with `WRF-25` at P5; released Food is used for civilians, never for the garrison. One inventory is used: nothing is double-reserved, and no second Food pool exists.

`other_food_reservations` does **not** include the garrison ration: that is a P3.7 obligation computed by Prompt 10 under F-WR-036 and paid from the Food that remains unreserved **after** `food_consumed` is taken. Civilian demand therefore always resolves before the military ration, and the two quantities are never added into one demand.

There is no "starving / not starving" flag. A 10% shortfall is different from a 100% shortfall, and the penalty reflects the difference.

**ECN-083 — Hunger penalty formula.** *Provisional (REQ-126).*

```
hunger_penalty_bp = min(3000, floor(3000 × unmet_food / food_demand))
```

The result is 0–3000 basis points (0–30%). It applies to the **next** turn's tax income, not to the current turn's (the current turn's tax was already collected at P3.1). The cap is deliberate: even total starvation does not make tax income zero, so a nation can recover.

**ECN-084 — The penalty is applied once and then cleared unless it recurs.** *Provisional.* At P3.6, the engine computes this turn's `hunger_penalty_bp` and stores it as the **next-turn** modifier. At the next P3.1, it applies that modifier to tax income and then clears it to zero; if the next P3.6 also has a shortfall, a new modifier is computed. There is no stacking and no permanent scar. The military ration at P3.7 does **not** produce or change this modifier; its consequence is the B-10 `RATION_SHORT` state and the readiness loss.

**ECN-085 — Recovery is one good turn.** *Provisional.* A full-food turn clears the penalty for the following turn. A player who fixes the shortage sees the tax recovery in the next digest, not after a long decay. This is the economic side of the project's no-permanent-collapse principle (ECN-017).

**ECN-086 — Food does not spoil by default.** *Provisional.* There is no decay, rot or leakage. Food is storable indefinitely, subject to shared warehouse space. Spoilage remains an open option for a later decision (Report 07 ECOQ-010); if adopted, it must be a published rule with a rate, a trigger and a ledger event, and it may not be applied retroactively.

**ECN-087 — No automatic food purchase.** *Provisional.* The game does not buy food for a nation at the boundary. A nation that wants to cover a shortage must buy before the boundary (Prompt 07), receive aid (Prompt 08/09) or produce more. Automatic purchase would create money out of nowhere or require a debt mechanic, both of which are rejected. The UI may forecast the shortage and suggest a purchase, but the decision is the player's.

**ECN-088 — The Prompt 06 contract.** *Provisional (REQ-127).* B-04 owns: food production, food storage, civilian food consumption, the unmet quantity and the **economic** hunger penalty on tax income. Prompt 06 owns: population size and growth, stability, unrest, migration, health and any **demographic** consequence of hunger. Prompt 10 owns: the military ration quantity, its soldier-equivalent factors and the `RATION_SHORT` consequence (F-WR-036); B-04 only executes the debit at P3.7. Prompt 06 may add a stability penalty for a shortfall, but it may not change the economic formula or the 0–30% cap. Prompt 13 must show food reserves, demand, forecast and the penalty together.

**ECN-089 — Famine relief and food aid.** *Provisional.* A food transfer from another nation is a normal trade or aid action under Prompt 07/08. It is recorded as a transfer, not as production; it does not create food. A nation under a shared-network restriction may not use food aid to circumvent the restriction (B-03 D-035); the pair check applies to the transfer.

**ECN-090 — Warnings.** *Provisional (REQ-128).* The interface must warn a player when the projected end-of-turn food stock is below demand, and must state the projected penalty. A warning is an estimate, labelled as a forecast, because population, trade and military consumption can change before the boundary. A warning is never a guarantee.

**ECN-091 — Edge cases.** *Provisional.* Zero population → demand 0, no penalty. Food demand exactly equal to available → `consumed = demand`, `unmet = 0`, no penalty. Food available 1 unit short → penalty `floor(3000/demand)`, which may be 0 for a very large population; the digest must show the unmet unit even when the penalty rounds to zero. A nation with no food capacity and no stock → maximum penalty and a clear recovery path. A nation with enough Food for civilians but not for its garrison → P3.6 resolves fully, the P3.7 ration is cancelled in whole, `RATION_SHORT` is set and readiness falls; no civilian Food is diverted and no unit is deleted.

---


## 12. Treasury and the financial model

**ECN-092 — One currency, one pool.** *Provisional (REQ-129).* The national currency is the **crown** (`crown`). Each nation has exactly one treasury balance, an integer number of crowns. There is no second currency, no gold, no prestige currency and no alliance currency at launch. An alliance pool, if Prompt 09 creates one, is a separate audited pool, not a second national currency.

**ECN-093 — The financial vocabulary is fixed.** *Provisional (REQ-130).* The following terms have exactly one meaning in every document:

| Term | Definition | Changes treasury? |
|---|---|---|
| Opening balance | Treasury at the start of the turn, after the previous turn closed | No (reference) |
| Gross monetary income | Crowns created by tax income and disclosed one-time rewards before any expense | Yes (+) |
| Operating expenses | Recurring costs of running capacity: variable batch costs, generator costs and capacity maintenance | Yes (−) |
| Net operating income | Gross income − operating expenses | Derived |
| Capital expenditure (capex) | One-time spending that acquires or upgrades capacity or a building | Yes (−) |
| Economic investment | Capex plus any one-time research/programme cost | Derived |
| Resource-sale proceeds | Crowns received from a sale (a transfer, not creation) | Yes (+) |
| Resource-purchase cost | Crowns paid for a purchase (a transfer, not destruction) | Yes (−) |
| Manufacturing expenses | The variable and maintenance costs of processing (a subset of operating expenses) | Yes (−) |
| Construction cost | The crown and material cost of a construction order (capex) | Yes (−) |
| Military upkeep / operating cost | Recurring military spending (Prompt 10) | Yes (−) |
| Fees | A disclosed charge that destroys crowns (for example a market fee, if adopted) | Yes (−) |
| Refunds | A returned reservation or a cancelled order's charge | Yes (+) |
| One-time reward | A disclosed, non-repeatable grant (Prompt 11) | Yes (+) |
| Policy-based transfer | Aid, indemnity or alliance contribution (a transfer) | Yes (±) |
| Net cash flow | Closing − opening | Derived |
| Economic output | The book value of goods and services produced in the turn (a statistic, not money) | No |
| National wealth | Treasury + inventory book value + fixed-asset book value | Derived |

**ECN-094 — Tax income formula.** *Provisional (REQ-131).*

```
tax_income = floor(population × tax_rate_bp × stability_factor_bp / 1,000,000,000)
```

- `population`: integer, owned by Prompt 06.
- `tax_rate_bp`: integer basis points; 100 bp = 1 crown per 1,000 people per turn. The standard start is **300 bp** (3 crowns per 1,000 people).
- `stability_factor_bp`: integer 5,000–11,000 (50%–110%), owned by Prompt 06; the default is 10,000 (100%).
- The denominator is `1000 × 100 × 10,000`; it converts people, basis points and the stability factor into crowns.
- The result is floored to a whole crown. No fractional crown exists.

At the standard start: `floor(50,000 × 300 × 10,000 / 1,000,000,000) = floor(150.0) = 150` crowns.

**ECN-095 — Tax rate is a real lever with a real trade-off.** *Provisional.* A higher `tax_rate_bp` raises tax income linearly, but Prompt 06's stability model lowers `stability_factor_bp` as the rate rises above a published threshold. The two effects can offset; the player must choose a point on the curve. The rate is bounded by Prompt 06 (a minimum and maximum); B-04 does not set the bounds beyond the default. The interface must show the current rate, the projected income and the projected stability effect together.

**ECN-096 — Gross income is not profit.** *Provisional.* Tax income is gross. Operating expenses, capex, purchases and fees are separate lines. A nation with 150 tax income and 121 operating expenses has a net operating income of 29, not a profit of 150. The report must never label gross income as "profit" or "net".

**ECN-097 — Operating expenses are not capex.** *Provisional (REQ-132).* Operating expenses recur every turn and are consumed by the act of running the nation. Capex is a one-time purchase of a durable asset. A construction order at P4 is capex; the maintenance of the resulting capacity is operating expense. The two are reported on separate lines and reconciled separately.

**ECN-098 — Capital expenditure.** *Provisional.* A construction or upgrade order is accepted at P4 under B-02, reserves its crown and material cost at acceptance, and charges them when it resolves. The resulting capacity is available from the **next** turn (the construction completes at the boundary), not the current turn. Its **book value** is the crown cost paid **plus the reference-price book value of the material inputs** (D-058); the materials are capitalized, not expensed, so the construction converts liquid assets into a fixed asset rather than destroying wealth. Capex does not appear in net operating income.

**ECN-099 — Resource sales and purchases are transfers.** *Provisional.* A sale moves crowns from buyer to seller and units from seller to buyer. It creates no crown and no resource. The seller's proceeds are not "income" in the tax sense; they are a transfer. The buyer's cost is not an operating expense; it is an asset swap (crowns for inventory). The report shows both the cash effect and the book-value effect.

**ECN-100 — Fees, taxes and rewards are explicit.** *Provisional.* A fee destroys crowns and must be disclosed before the action. A tax is a transfer to a government: the Prompt 06 national tax is adopted under ECN-094/ECN-095, and the Prompt 09 automatic per-turn alliance production tax is adopted under ECN-213a as a withheld transfer from current-turn production. No other tax, tribute or automatic deduction is adopted. A reward creates crowns only if it is a disclosed one-time grant approved by Prompt 11; it must carry an achievement key and a ledger event. None of these may be hidden inside a recipe or a price. **B-04 adopts no fee**: the `fees` term in ECN-101 and the C1–C4 identity is reserved for a Prompt 07 fee (if one is ever adopted) and is zero at launch, so any example that shows a fee must label it hypothetical.

**ECN-101 — Net cash flow and closing balance.** *Provisional.*

```
net_operating_income = tax_income + one_time_rewards − operating_expenses
net_cash_flow        = closing_balance − opening_balance
closing_balance      = opening_balance
                       + tax_income
                       + one_time_rewards
                       + sale_proceeds
                       + transfers_in
                       + refunds
                       − operating_expenses
                       − capex
                       − purchase_costs
                       − transfers_out
                       − fees
```

Every term is an integer. The identity must hold exactly; a one-crown discrepancy is a defect, not a rounding difference.

**ECN-102 — The treasury never goes negative.** *Provisional (REQ-133).* No rule may produce a negative balance. Every charge checks the available balance first. A batch that cannot be afforded does not run; an obligation that cannot be paid is cancelled under §12.7; a trade that cannot be paid fails atomically. The database may enforce a non-negative check as a second line of defence, but the design rule is the primary guarantee.

**ECN-103 — No debt, no credit, no overdraft.** *Provisional (REQ-134; D-050).* There is no player debt, no loan, no credit line, no overdraft, no interest and no bond. A nation cannot borrow from another nation, an alliance or the system. This is a deliberate simplification: debt would require interest, collateral, default, enforcement and a second ledger, and the project's audience does not need it. Report 07's ECON-020 lending rejection is carried forward.

**ECN-104 — Insolvency is a liquidity state, not a deletion state.** *Provisional.* A nation with zero crowns still exists, still owns its capacity and inventory, and can recover by selling, idling, trading or waiting for tax income. There is no bankruptcy flag, no confiscation, no forced reset and no game-over. The only hard consequences are the cancelled obligations and the lost production that the player can see and reverse.

**ECN-105 — Austerity priority.** *Provisional (REQ-135).* When the resource an obligation needs (unreserved crowns for money obligations, unreserved Food for the military ration) is insufficient for all P3 obligations, they are paid in this order:

1. **Capacity maintenance** (the fixed cost of keeping the nation's assets alive).
2. **Food production** (the survival chain).
3. **Other extraction** (coal, oil, iron, bauxite, lead, uranium).
4. **Power generation** (fuel and variable cost).
5. **Processing** (refining, steel, aluminum, ammunition).
6. **Military obligations** (Prompt 10): first the **military Food ration** from unreserved Food (sub-order 6(a)), then **military readiness upkeep** from unreserved crowns and materials (6(b)), then any settlement (6(c)) and any other declared military obligation (6(d)).
7. **Discretionary upkeep and construction maintenance** (Prompt 05/09).

Within a category, the published order of §8.6 applies. The order is deterministic and player-readable; it is not a hidden priority.

**ECN-106 — Unpaid obligations are cancelled, not deferred.** *Provisional.* If an obligation cannot be paid, it is **cancelled** for that turn and the consequence is applied by its owner: a facility idles, readiness falls, the garrison goes on short rations (`RATION_SHORT`), a construction project pauses. The unpaid amount is **not** carried as debt and does not accrue interest. The digest states the amount, the obligation and the consequence. A player can choose to pay next turn by keeping enough crowns; the game does not automatically seize future income.

**ECN-107 — Recovery path.** *Provisional.* A distressed nation can: sell inventory (Prompt 07), idle loss-making capacity (free), lower military readiness (Prompt 10), cancel construction (Prompt 05), or wait for tax income. None of these requires a support ticket, a loan or a paid item. The interface must present at least three recovery options when the projected balance is negative.

**ECN-108 — National wealth is a derived statistic, not a spendable balance.** *Provisional (REQ-136).*

```
national_wealth = treasury
                + Σ (inventory_units(r) × reference_price(r))
                + fixed_asset_book_value
```

- `treasury` is liquid.
- Inventory is valued at the **reference price**, not at the last market price; it is an accounting estimate.
- `fixed_asset_book_value` is the sum of the crown cost of **completed construction and completed infrastructure lots**, less any explicit impairment:

  ```
  fixed_asset_book_value = Σ_city infrastructure_carrying_value(city)
                         + Σ other recognised fixed assets (facilities and other completed construction)
  infrastructure_carrying_value(city)
      = infrastructure_gross_capital(city) − infrastructure_accumulated_impairment(city)
  ```

  The city infrastructure subledger is owned by B-05 (`URB-118a`, `URB-118b`). Its basis is the capitalised crown cost of completed `UPGRADE_INFRASTRUCTURE` lots: the **initial city capital (50 levels) and the new-city capital (10 levels) are a zero-cost opening lot** and contribute 0 to book value. **Facility book value is excluded from infrastructure impairment** and is never reduced by a strike. Infrastructure damage impairs only the city's infrastructure carrying value, capped at that carrying value; a repair capitalises a new infrastructure lot at its B-05 cost (`URB-043`/`URB-044`) and does **not** reverse earlier impairment. Impairment and repair therefore reconcile exactly: B-04 never holds a second, parallel city-book-value number. There is no depreciation in v1 (a deliberate simplification; it would add a monthly job and a second number to explain).
- National wealth is **not** a score, a ranking or a spending limit. It is a report line that helps a player understand the difference between liquid and total value.

**ECN-109 — Book value is not market value.** *Provisional.* A nation that buys steel at 5 crowns and holds it has inventory book value 7 per unit (the reference price) but a realisable value of 5. The difference is a **fair-value gap**, reported as an estimate. Prompt 07 may use the gap for fair-value checks; Prompt 11 may use wealth for rankings, but must not present it as money.

**ECN-110 — Available, reserved and total.** *Provisional (REQ-137).*

```
total_treasury   = authoritative balance
reserved_total   = Σ active reservations (money)
available        = total_treasury − reserved_total
```

The three numbers are displayed separately (B-02 TR-069). A player must never have to subtract reservations mentally. The same three-way split applies to inventory: total, reserved and available. The sum of reservations may never exceed the total; the engine rejects any action that would break this invariant.

**ECN-111 — Money conservation identity.** *Provisional.* Across the whole world, for every turn:

```
Σ closing_treasury = Σ opening_treasury
                   + Σ tax_income
                   + Σ one_time_rewards
                   + Σ administrative_credits
                   − Σ operating_expenses
                   − Σ capex
                   − Σ fees
```

Transfers (trades, aid, indemnities) cancel between payer and payee and do not appear on either side of the world total. The identity is checked at P7; a mismatch is a defect and the turn must not publish a false total. This is the C1–C4 identity carried from Report 07.

**ECN-112 — No interest, no yield on cash, no idle income.** *Provisional.* The treasury earns nothing for existing. There is no savings account, no bond, no dividend and no "bank interest". The only way to turn crowns into more crowns is to produce something useful and sell it, or to tax a growing population. This is the anti-snowball core of the economy.

**ECN-113 — One-time rewards are bounded.** *Provisional (REQ-138).* A reward must be: (a) approved by Prompt 11's event/objective rules; (b) non-repeatable, with an achievement key; (c) disclosed before it is granted; (d) recorded in the ledger; and (e) not convertible into a repeatable transfer. A reward may be crowns, resources or a cosmetic; it may not be a permanent yield multiplier. This prevents an event from becoming a hidden money printer.

**ECN-114 — Administrative corrections are traceable.** *Provisional.* An operator may correct an economic error only by writing an `ADJUSTMENT` or `REVERSAL` event that references the original event, states the reason and the operator role, and is visible in the audit log. No operator may edit a balance directly or delete a ledger row. The correction is included in the reconciliation for that turn.

**ECN-115 — Refunds and cancellations.** *Provisional.* A refund is a positive ledger event linked to the original charge. A cancellation before LOCKED releases a reservation and writes a `RESERVATION_RELEASED` event; it does not write a refund because nothing was charged. A failed manual order at P3 releases the reservation and writes a `MANUFACTURE_FAILED` event; the money was never charged, so there is no refund. A cancelled construction order follows Prompt 05's refund rule, which must be disclosed before acceptance.

**ECN-116 — The treasury report reconciles.** *Provisional (REQ-139).* Every turn's report must satisfy:

```
closing_balance = opening_balance + Σ(all ledger deltas for the turn)
```

and the ledger's `balance_after` on the last event must equal the authoritative closing balance. A report that cannot reconcile is not published; the turn is `INTERRUPTED` and recovered. This is the accounting version of B-02's one-outcome rule.

**ECN-117 — Capital and operating example (contract).** *Provisional.* A construction order costing 150 crowns and 10 steel is capex: at P4 it charges 150 crowns and 10 steel, adds **150 + 10×7 = 220** to fixed-asset book value, and makes the new capacity available next turn. The next turn's maintenance is +1 crown (if extraction) or +2 (if processing); the variable cost applies only when a batch runs. The player can see why the build reduced cash now and why the facility may still lose money at a low output price. The full worked example is §20, Example 4.

**ECN-118 — What the treasury is not.** *Provisional.* The treasury is not national wealth, not score, not a credit rating, not a promise of solvency and not a measure of player skill. It is the liquid crown balance, and it is displayed with its reservations and its forecast. Every other meaning is a separate, labelled statistic.

---


## 13. Inventory, storage and reservations

**ECN-119 — Inventory is a per-resource integer ledger.** *Provisional (REQ-140).* Each nation has one inventory record per resource: `total_units`, `reserved_units` and `available_units = total − reserved`. The record is authoritative; a client display is a view. Total inventory may never be negative, and reserved may never exceed total.

**ECN-120 — Storage is one shared warehouse.** *Provisional (REQ-141).* Every resource unit occupies **one unit of warehouse space**, regardless of type. The warehouse has a single integer capacity `W`. There is no per-resource cap, no separate silo and no resource-specific storage building in the launch design. This keeps the storage decision legible: "what do I keep, and what do I sell?"

**ECN-121 — Starting warehouse capacity.** *Provisional.* A new nation starts with **W = 2,000 units**. Its standard bundle uses **310 units** (D-063), leaving **1,690 units** free for the first turns. The number is provisional and belongs to Prompt 14's balance validation; the structure (one shared capacity) is fixed by D-052.

**ECN-122 — Warehouse expansion is Prompt 05's.** *Provisional.* A later building or upgrade may add `W`. B-04 requires that expansion has a rising marginal cost and that the new capacity is available at the next boundary. The exact cost, prerequisite and maximum are Prompt 05's; they must be registered in the formula register and may not be a hidden multiplier.

**ECN-123 — No decay, spoilage or leakage by default.** *Provisional.* Resources do not disappear merely because they are stored. Food does not rot; uranium does not decay; gasoline does not evaporate. A later decision may add a specific loss rule, but it must be published, predictable and ledgered (ECN-086).

**ECN-124 — Overflow blocks the batch; it never destroys value.** *Provisional (REQ-142).* Before a batch runs, the engine checks `free_space = W − total_inventory`. If `free_space < batch_output_units`, the batch does not run; its money, inputs and fuel are not consumed. The digest reports `SPACE_BLOCKED` with the resource, the batch size and the free space. The same rule applies to a trade purchase: if the purchased units do not fit, the purchase fails at acceptance (`F5`) and nothing moves.

**ECN-125 — Reservations are exclusive and visible.** *Provisional.* A reservation is a claim on a specific quantity of a specific resource (or crowns, or capacity, or output space) held for an accepted action. Reserved units are still owned by the nation, still count toward warehouse capacity and still appear in the total, but they are **not available** to any other action. The reservation is released exactly once: on resolution (consumed), on failure, on cancellation or on expiry.

**ECN-126 — Reservation lifecycle.** *Provisional.*

| Event | Money reservation | Input reservation | Capacity reservation | Output-space reservation |
|---|---|---|---|---|
| Submission accepted | Held | Held | Held | Held |
| Amended while OPEN | Replaced (new key) | Replaced | Replaced | Replaced |
| Cancelled while OPEN | Released | Released | Released | Released |
| Resolved | Charged | Consumed | Used | Filled |
| Failed at P2/P3 | Released | Released | Released | Released |
| Expired | Released | Released | Released | Released |
| Nation retired | Released/destroyed | Released/destroyed | Released | Released |

No reservation may be released twice, and no unit may be both consumed and released. The ledger writes one `RESERVATION_HELD` and one `RESERVATION_RELEASED`/`RESERVATION_CONSUMED` event per reservation, with a shared reservation ID.

**ECN-127 — The four inventory views are distinct.** *Provisional (REQ-143).* The interface must distinguish:

- **Total** — everything owned, including reserved.
- **Available** — total minus reserved; what a new action can use.
- **Reserved** — claimed by accepted actions.
- **Committed to a pending operation** — a subset of reserved that is tied to a specific action, with a link to that action.

"Committed" is not a fifth balance; it is a labelled subset of reserved. A unit cannot be both available and reserved. A unit that has been consumed is no longer in any of these views; it is a ledger event, not a balance.

**ECN-128 — Inventory changes are ledgered.** *Provisional.* Every change writes an event with the resource, the signed delta, the resulting total, the reason and the source action or turn. There is no silent stock adjustment. A reconciliation check at P7 verifies that the sum of the turn's ledger deltas equals `closing_total − opening_total` for every resource.

**ECN-129 — Transfers do not create inventory.** *Provisional.* A trade or aid transfer moves units from one nation's total to another's. It does not create or destroy units. The two ledger events are linked by a `transfer_id`; the sum of the deltas is zero. If the receiving nation lacks warehouse space, the transfer fails atomically and neither side moves.

**ECN-130 — Nation retirement disposes of inventory deterministically.** *Provisional (REQ-144).* On a reroll, every unit of every resource is destroyed with the nation. Reservations are released; pending orders are cancelled; open offers are withdrawn; accepted-but-unsettled trades block the reroll under B-03 RRL-021 until they resolve or are cancelled. The final balances are written to a `NATION_RETIRED` event so the history is traceable. No unit and no crown transfers to the replacement.

---


## 14. Economic actions and state transitions

**ECN-131 — The economic action catalogue.** *Provisional (REQ-145).* Every economic action is one of the following types. The table fixes its owner, timing class and reservation profile. A later prompt may add an action, but it must add a row here and a B-02 declaration; it may not create an unlisted economic verb.

| Action | Owner | Timing class | Reserves |
|---|---|---|---|
| `SET_PRODUCTION_POLICY` | 04 | Immediate-with-record; effective next boundary | Nothing |
| `MANUFACTURE` (manual order) | 04 | Queued until boundary | Money, inputs, capacity, output space |
| `CANCEL_MANUFACTURE` | 04 | Immediate while turn OPEN | Releases all four |
| `CONSTRUCT_CAPACITY` | 05 | Queued until boundary | Money, materials, construction slot |
| `UPGRADE_CAPACITY` | 05 | Queued until boundary | Money, materials, construction slot |
| `EXPAND_WAREHOUSE` | 05 | Queued until boundary | Money, materials, construction slot |
| `BUY_RESOURCE` / `SELL_RESOURCE` | 07 | Immediate-with-record (directed) or queued (listing) | Money and/or goods, atomic at acceptance |
| `TRANSFER_RESOURCE` / `TRANSFER_CROWNS` | 07/08 | Immediate-with-record, atomic | Both sides' goods/money |
| `SET_TAX_RATE` | 06 | Immediate-with-record; effective next boundary | Nothing |
| `SET_MILITARY_POSTURE` / `CONSUME_MILITARY` | 10 | Queued until boundary | Money, gasoline, ammunition, steel, aluminum as declared |

**ECN-132 — The common action record.** *Provisional.* Every economic action carries: a server-assigned `action_id`; the `account_id` and `nation_id`; an idempotency key; the submission timestamp; the accepted turn ID; the action type; the parameters; the required crowns; the required resources; the reservations taken; the facility/capacity/technology checks; the recipe or price reference; the resolution timing; the resulting state; the failure code (if any); the ledger event IDs; and the player-facing explanation. A record missing any of these is incomplete.

**ECN-133 — Submission validation.** *Provisional (REQ-146).* At submission the server checks, in order: the actor owns the nation; the action type is enabled; the turn is OPEN; the parameters are integers and within bounds; the nation meets the prerequisites (capacity, technology, warehouse space); the **available** crowns cover the cost after existing reservations; the **available** resources cover the inputs after existing reservations; the output fits the free warehouse space; the capacity is not overbooked; and the idempotency key is new. Failure is `REJECTED` with a B-02 code and a sentence. Nothing is reserved.

**ECN-134 — Acceptance reserves, not charges.** *Provisional.* On acceptance the engine writes `RESERVATION_HELD` events for every reservation and moves the action to `ACCEPTED`. The money is still in the treasury; the inputs are still in the inventory; the capacity is still shown as reserved. The player sees the effect immediately in the available/reserved display.

**ECN-135 — Resolution.** *Provisional.* At P3 (production) or P4 (construction/trade), the action is re-validated against the frozen state. If it passes, it is applied atomically: the money is charged, the inputs consumed, the output produced or the asset created, and the reservations converted to charges. If it fails, nothing is applied and every reservation is released.

**ECN-136 — Success.** *Provisional.* A successful action writes a `RESOLVED` record, the corresponding ledger events, and a digest line with the action ID, the recipe or price, the amounts and the resulting balances. Success is final; the action cannot be replayed.

**ECN-137 — Rejection.** *Provisional.* A rejected action writes a `REJECTED` record and a digest line with the reason. It takes no reservation, changes no balance and leaves no pending state. A rejection is not a sanction and is not counted against the player.

**ECN-138 — Failure.** *Provisional.* A failed action writes a `FAILED` record, a `RESERVATION_RELEASED` event for each reservation, and a digest line with the B-02 code and a sentence. The inputs and money are exactly as they were before acceptance, except for any consumption by an earlier B1 action that legitimately ran first.

**ECN-139 — Partial execution is prohibited.** *Provisional.* A manual order of `n` batches either runs all `n` or fails all `n`. A construction order either completes or does not start. A trade either moves both legs or neither. A payment either transfers the full amount or fails. There is no "50% filled" state at launch; a later market design may add partial fills only with a new decision and a new ledger event type.

**ECN-140 — Cancellation.** *Provisional.* An action may be cancelled only while its turn is OPEN. Cancellation releases every reservation, writes a `CANCELLED` record and charges no fee (unless the owning system's disclosed rule says otherwise). A cancelled action is not a failure and does not count against a reliability metric.

**ECN-141 — Idempotency.** *Provisional (REQ-147).* Every action carries a client-generated key scoped to `(account_id, action_type, turn_id)`. A repeat with the same key and the same payload returns the original result; a repeat with a different payload is rejected (`F9`) and creates nothing. An amendment uses a new key and supersedes the old action (B-02 TR-064). The server-assigned `action_id` is the only ordering identity.

**ECN-142 — Every action is explainable.** *Provisional.* The digest must answer: what was attempted, whether it was accepted, what it reserved, whether it resolved, what it cost, what it produced and why. A failure must name the limiting factor (money, input, power, space, capacity, technology or target). "Something went wrong" is not an acceptable message.

---


## 15. The two-hour UTC economic settlement

**ECN-143 — One settlement per nation per turn.** *Provisional (REQ-148).* The economic settlement is identified by `(turn_id, nation_id)`. It runs inside B-02's P3 and P4 phases; it does not create a second clock, a second scheduler or a per-nation timer. A nation that was created after the turn opened is settled from the turn in which it was created; a nation retired before the boundary is not settled.

**ECN-144 — The authoritative P3 order.** *Provisional (REQ-149).* Within P3, the economy runs these sub-phases in this exact order:

| Sub-phase | Name | What happens | Money | Inventory |
|---|---|---|---|---|
| **P3.1** | Tax | Compute and credit national tax income; withhold the member's alliance Crowns tax from that income; apply the previous turn's hunger penalty | + tax, − alliance tax | — |
| **P3.2** | Maintenance | Charge capacity maintenance in the published order | − maintenance | — |
| **P3.3** | Extraction | Run food, coal, oil, iron, bauxite, lead and uranium batches; withhold alliance tax on each production event | − variable | + net raw output |
| **P3.4** | Power | Run coal, oil and nuclear generators; consume fuel; produce GU | − variable | − fuel |
| **P3.5** | Processing | Run manual orders, then standing policies, subject to power derating; withhold alliance tax on output at its production event | − variable | − inputs, + net output |
| **P3.6** | Food | Consume population food; record shortage; set next-turn hunger penalty | — | − food |
| **P3.7** | Obligations | Pay the military Food ration, then military readiness and other declared upkeep; cancel unpaid items | − upkeep | − food/ammo/gasoline if declared |
| **P3.8** | Close | Reconcile, compute wealth, write digest, mark settlement complete | — | — |

**ECN-145 — Why this order is correct.** *Provisional.*

1. **Tax before everything** satisfies D-019's income-before-obligations rule and lets this turn's income pay this turn's costs.
2. **Maintenance before production** is the cost of keeping the assets available; it cannot be skipped by idling after the fact.
3. **Extraction before power** means fuel produced this turn can power this turn's generators, avoiding a one-turn death spiral when coal is low.
4. **Power before processing** is a physical prerequisite: a batch cannot run without GU.
5. **Processing before food** lets a nation convert raw goods into the goods it needs before the population eats; food itself is produced in P3.3, so it is already available.
6. **Food before obligations** puts civilian survival ahead of military upkeep, consistent with the austerity priority (ECN-105). P3.7 then pays the garrison ration **before** readiness upkeep, so soldiers eat before the army trains.
7. **Obligations last** means the military ration and readiness are paid from what is left after the economy has run, not before; a nation that over-commits its military loses rations or readiness, not its civilians' food.
8. **Close last** means the report is generated from the same transaction as the state change (B-02 G10).

**Alliance production tax is a source withholding, not a new sub-phase.** At P3.1 the national tax income is computed and credited, then the member's frozen alliance Crowns rate is applied to that income and the tax is moved to the Alliance Receiving Ledger before P3.2. At P3.3 and P3.5, each supported stored resource production event is taxed at the point its net output is created, before any later P3 consumption. No alliance tax is collected in P4, from opening balances, from existing stockpiles, from earlier production, from donations, gifts, aid, reparations, market purchases or sale proceeds, from other non-production inflows, or from GU. The national calculations, amounts and ordering above are unchanged; the full contract is ECN-213a.

**ECN-146 — P3.1 Tax.** *Provisional.* Read the turn's frozen population, tax rate and stability factor; apply the stored `hunger_penalty_bp` from the previous turn; compute `tax_income` by F-EC-001; credit the treasury; clear the stored penalty. Write `TAX_INCOME` with the formula inputs and the resulting balance. If the population is zero, income is zero and no event is written. Immediately after crediting the gross income, and before P3.2, withhold the member's alliance Crowns tax from that gross income under ECN-213a when the nation is an active member in the frozen alliance snapshot; the tax moves to the Alliance Receiving Ledger's `RECEIVED` and `AVAILABLE` categories and the net remains in the national treasury in the same atomic transaction. No other income in the turn is part of the alliance tax base.

**ECN-147 — P3.2 Maintenance.** *Provisional.* Compute `maintenance = Σ(capacity_batches × rate) + Σ(generator_levels × 2)` in the published order. Charge it from unreserved crowns. If the unreserved balance is insufficient, pay in the ECN-105 order as ECN-147a defines it and cancel the unpaid remainder; a capacity whose maintenance is unpaid is marked `UNMAINTAINED` and cannot run this turn. Write one `MAINTENANCE` event per chain.

**ECN-147a — Maintenance is allocated per chain, in the settlement order.** *Provisional (REQ-116; D-050).* Maintenance is charged as **one obligation per chain**: `capacity_batches × rate` (1 per extraction batch, 2 per processing batch) or `generator_levels × 2` per generator class. The obligations are attempted in the order the settlement itself runs:

1. **Extraction:** food, coal, oil, iron, bauxite, lead, uranium.
2. **Generation:** coal, oil, nuclear.
3. **Processing:** refining, steel, aluminum, ammunition.

Each obligation is **whole**. If the remaining unreserved balance is at least the obligation, it is paid in full; otherwise it is **cancelled in full**. There is no partial maintenance and no partial `UNMAINTAINED` chain. The engine then continues to the next obligation with whatever remains, exactly as ECN-105 continues past an unaffordable batch (Example 15). A chain whose obligation is cancelled is marked `UNMAINTAINED` for that turn and cannot run; the mark is cleared at the next P3.2 in which its obligation is paid. The order is published, deterministic and independent of database order, so two nations in the same position always pay the same chains.

Extraction → generation → processing is the P3.3 → P3.4 → P3.5 sequence the player already reads, and it keeps the chain that produces power ahead of the chains that need it.

**Worked allocation.** At the standard start the obligations are food 3, coal 2, oil 1, iron 1, generator 2 and refining 2 — **11** in total. A nation holding **1** crown pays **oil** (1), cancels the other **10**, and ends at **0**; food, coal, iron, the generator and refining are `UNMAINTAINED` and cannot run that turn. A nation holding **3** crowns pays **food** and cancels the rest. A nation holding **11** pays all six and ends at 0 with nothing unmaintained.

**ECN-148 — P3.3 Extraction.** *Provisional.* For each raw resource in the order food, coal, oil, iron, bauxite, lead, uranium: compute `batches_run` by F-EC-004; check money, space and (for food) nothing else; consume the variable cost; add the output; write `RESOURCE_PRODUCED` and `PRODUCTION_COST`. For each supported stored resource, the alliance tax is withheld at this production event under ECN-213a: the gross output is the taxable gross, the tax moves to the Alliance Receiving Ledger and the net is added to inventory. A batch blocked by space writes `SPACE_BLOCKED`; a batch blocked by money writes `MONEY_BLOCKED`; neither consumes anything and neither creates a taxable production event.

**ECN-149 — P3.4 Power.** *Provisional.* For each generator level in the order coal, oil, nuclear: check the full fuel and variable cost; if both are available, consume them, produce 6 or 20 GU and write `POWER_FUEL`, `POWER_GENERATED` and `PRODUCTION_COST`; otherwise write `GENERATOR_IDLE` with the missing input. Sum the GU supply. Surplus is discarded and reported.

**ECN-150 — P3.5 Processing.** *Provisional.* Compute `power_demand` from all planned batches; compute `power_pct` and `batches_available`; run accepted manual orders in B1 order (each fully or not at all); then run standing policies in the order refining, steel, aluminum, ammunition. For each batch: check inputs (unreserved), money and space; consume inputs and money; add output; write `MANUFACTURE_INPUT`, `MANUFACTURE_OUTPUT` and `PRODUCTION_COST`. For each supported stored output, the alliance tax is withheld at this production event under ECN-213a on the gross output; manufacturing inputs are not production and are never taxed. A failed manual order writes `MANUFACTURE_FAILED` and releases its reservations; a blocked standing batch writes the limiting reason and creates no taxable output.

**ECN-151 — P3.6 Food.** *Provisional.* Compute `food_demand`, `food_available`, `food_consumed` and `unmet_food`; consume the food; write `FOOD_CONSUMED` and, if unmet > 0, `FOOD_SHORTFALL` with the ratio and the computed `hunger_penalty_bp`. Store the penalty for the next turn. Do not apply it to this turn's tax.

**ECN-152 — P3.7 Obligations.** *Provisional.* Read the frozen obligations from Prompt 10 (military Food ration first, then readiness and campaigns) and Prompt 05 (maintenance). Pay the Food ration from unreserved Food, then pay the money obligations from unreserved crowns in the ECN-105 order. If an obligation cannot be paid, write `OBLIGATION_CANCELLED` with the amount and the owner, and let the owner apply its consequence. Do not create a negative balance and do not create debt. An alliance tax is not an obligation: it is withheld at its production source under ECN-213a, and a voluntary donation is a P4 transfer.

**ECN-153 — P3.8 Close and reconcile.** *Provisional.* Before marking the settlement complete, the engine checks: (a) every ledger event's `balance_after` equals the running balance; (b) every resource's delta sum equals `closing − opening`; (c) the treasury identity holds; (d) every reserved amount has a matching action or has been released; (e) no negative balance or inventory exists. A failure sets the turn `INTERRUPTED` and no digest is published. On success, write `TURN_SETTLED` with the closing balances, compute national wealth, and hand the digest to P7.

**ECN-154 — The settlement marker.** *Provisional (REQ-150).* Each settlement writes one row keyed by `(turn_id, nation_id)`, with a unique constraint. The row stores the state (`PENDING`, `RUNNING`, `COMPLETE`, `FAILED`), the phase checkpoint, the opening balances, the closing balances, the configuration version and the completion timestamp. A second attempt for the same key reads the existing row; if it is `COMPLETE`, it returns the stored result and does nothing else.

**ECN-155 — Exactly-once effects.** *Provisional (REQ-151).* Every ledger event has a deterministic `event_key` derived from `(turn_id, nation_id, phase, entity, sequence)`. The key is unique. A retried settlement that tries to write the same event is a no-op; a retry that tries to write a *different* event for the same key is a defect and aborts the turn. This is how duplicate delivery, a retried job or a resumed phase cannot double-pay income, double-produce or double-consume.

**ECN-156 — Phase checkpoints and forward-only resume.** *Provisional.* The settlement records a checkpoint after each P3 sub-phase. Recovery resumes from the last completed checkpoint for the **same turn**, with the same frozen input. Completed sub-phases are not re-executed against changed input. If a later sub-phase fails, the turn is `INTERRUPTED`; it is retried from the checkpoint, not from P3.1. This is B-02 TR-078 applied to the economy.

**ECN-157 — Duplicate and out-of-order invocations.** *Provisional.* The scheduler may fire twice, late or out of order. The engine: (a) refuses a turn whose predecessor is not `COMPLETE` (serial resolution, B-02 TR-033); (b) refuses a duplicate `(turn_id, nation_id)` that is already `COMPLETE`; (c) resumes an `INTERRUPTED` settlement; (d) never resolves a future turn early; (e) never rewrites a past turn. A late trigger changes when the result appears, not which actions it contains (B-02 TR-081).

**ECN-158 — Deterministic inputs only.** *Provisional.* During settlement the rules may read: the frozen configuration, the turn ID, the nation's frozen state, the accepted action set, the published recipe table and the reference prices. They may not read wall-clock time, request arrival order beyond the frozen key, live market prices, another nation's private state or environment randomness. Any randomness (for example a B2 lottery) uses the published seed derivation from B-02.

**ECN-159 — Competing economic actions.** *Provisional.* Two accepted manual orders that claim the same capacity are ordered by B-02 B1 `(submitted_at, action_id)`; the later one is re-validated and fails with `F5` if capacity is exhausted. Two actions that claim the same input are prevented by reservation, not by ordering. A standing policy never outranks an accepted manual order. A trade settlement at P4 cannot retroactively change a P3 production result.

**ECN-160 — Settlement audit.** *Provisional (REQ-152).* The settlement writes an audit record with: the turn ID, the nation ID, the configuration version, the phase checkpoints, the opening and closing balances, the number of events, the reconciliation result and any recovery attempts. The record is part of the permanent audit spine (D-026) and is never deleted with class-S history.

**ECN-161 — Recovery is visible.** *Provisional.* If a settlement is retried or recovered, the digest states "recovered after an interruption" and the completion time. The player sees the same final numbers; they do not see a second, different outcome. If the turn cannot complete after the bounded retry budget, it is `FAILED`, the next turn waits, and the operator path is B-02/D-025's.

**ECN-162 — No economic action at P4 may change a P3 result.** *Provisional.* Construction, trade and diplomacy resolve at P4, after the economy. A construction order completed at P4 makes capacity available next turn; a trade at P4 changes inventory after this turn's production; a treaty payment at P4 changes the treasury after the economy. This separation is what makes the boundary deterministic.

---


## 16. The immutable accounting ledger

**ECN-163 — The ledger is append-only.** *Provisional (REQ-153).* Every monetary and resource change writes an immutable event. Completed events are never edited or deleted. A correction is a new event that references the original. The ledger is the authoritative history of the economy; the current balances are a derived state that must reconcile with it.

**ECN-164 — The event fields.** *Provisional.* Each event has at least:

| Field | Meaning |
|---|---|
| `event_id` | Server-assigned unique ID |
| `event_key` | Deterministic idempotency key |
| `nation_id`, `account_id` | Owner references |
| `turn_id` | The world turn |
| `event_type` | One of the types in ECN-165 |
| `resource` / `currency` | What changed |
| `delta` | Signed integer quantity or amount |
| `balance_after` | Resulting total for that resource/currency |
| `source_action_id` | The action that caused it, if any |
| `source_event_id` | The original event for a reversal/correction |
| `reason_code` | A stable machine-readable reason |
| `origin` | `SYSTEM`, `PLAYER`, `OPERATOR`, `EVENT` |
| `created_at` | Server timestamp |
| `status` | `POSTED`, `REVERSED`, `CORRECTED` |
| `visibility` | Public / private / restricted |

**ECN-165 — The event types.** *Provisional (REQ-154).* The minimum set is: `NATION_INIT`, `TAX_INCOME`, `PRODUCTION_COST`, `MAINTENANCE`, `RESOURCE_PRODUCED`, `POWER_FUEL`, `POWER_GENERATED`, `GENERATOR_IDLE`, `MANUFACTURE_INPUT`, `MANUFACTURE_OUTPUT`, `MANUFACTURE_FAILED`, `FOOD_CONSUMED`, `FOOD_SHORTFALL`, `OBLIGATION_PAID`, `OBLIGATION_CANCELLED`, `RESERVATION_HELD`, `RESERVATION_RELEASED`, `RESERVATION_CONSUMED`, `TRADE_BUY`, `TRADE_SELL`, `TRANSFER_IN`, `TRANSFER_OUT`, `CAPEX`, `REFUND`, `REWARD`, `FEE`, `ADJUSTMENT`, `REVERSAL`, `NATION_RETIRED`, `TURN_SETTLED`, `RECOVERY`. A new type requires a new decision and a new register row.

**ECN-166 — Corrections are traceable reversals.** *Provisional (REQ-155).* To correct a posted event, write a `REVERSAL` with the opposite delta and `source_event_id` pointing at the original, then write the corrected `ADJUSTMENT`. The original remains `REVERSED`; it is never deleted. A player-visible history shows both the original and the correction. An operator correction also records the operator role and the reason.

**ECN-167 — The current balance is derived and checked.** *Provisional.* The authoritative balance is stored on the nation for performance, but it must equal the sum of the ledger deltas for that nation at every checkpoint. A nightly reconciliation job (not a turn phase) recomputes the sums and reports any mismatch. A mismatch freezes value-changing actions for that nation until an operator resolves it; it does not silently rewrite history.

**ECN-168 — Duplicate events are impossible.** *Provisional.* The unique `event_key` prevents a retry from writing a second event for the same logical change. A duplicate insert is a no-op. The settlement also holds a `(turn_id, nation_id)` marker, so a second settlement run cannot even reach the event-writing stage.

**ECN-169 — Missing events are a defect.** *Provisional.* If a balance changed without an event, the reconciliation fails and the turn is `INTERRUPTED`. The design does not allow a "best effort" ledger; a completed economic change without an event is a release blocker.

**ECN-170 — Administrative adjustments are limited and logged.** *Provisional.* An operator may write an `ADJUSTMENT` only for a documented reason (a support case, a bug correction, a compensation). The event records the operator, the case reference, the amount and the reason. It is visible to the affected player and in the audit spine. There is no "silent fix" path.

**ECN-171 — Old requests cannot be replayed.** *Provisional.* An action is scoped to its turn. A request from an earlier turn cannot be re-submitted against a later turn with the same key; it is rejected as stale (`F9` or the owning system's equivalent). The idempotency key includes the turn, so a replay cannot become a new action.

**ECN-172 — Partial settlement cannot be published.** *Provisional.* If a settlement stops after some events are posted but before `TURN_SETTLED`, the turn is `INTERRUPTED` and the events are retained for recovery. No digest is published. Recovery resumes from the checkpoint and completes the same turn; the partial state is never shown as a final result.

**ECN-173 — Reports reconcile with the ledger.** *Provisional (REQ-156).* Every report line must be derivable from ledger events or from a stated formula. A report that cannot be traced to an event is a defect. The close step checks the report's totals against the ledger before publishing.

**ECN-174 — The ledger is not the database design.** *Provisional.* This section specifies required behaviour, not tables, indexes, partitions or retention jobs. The physical schema, the write budget and the retention implementation are Stage 5/Stage 8 work. What is fixed is: append-only, unique event keys, `balance_after`, reversal links, reconciliation and an operator audit trail.

**ECN-175 — Ledger visibility.** *Provisional.* A player sees their own events and the public events that concern them. Another player's private events are not visible. Aggregates respect D-027's k = 5 rule. The audit spine is restricted to authorized operators under Prompt 12. Visibility is a field on every event, not an afterthought.

---


## 17. Reporting, forecasts and explainability

**ECN-176 — The treasury dashboard must answer the player's questions.** *Provisional (REQ-157).* At minimum: how many crowns do I have; how many can I spend; how much is reserved; where did the money come from; what did I spend it on; why did the balance change this turn; how much did I invest; what are my recurring costs; which resources did I produce and consume; what is reserved; why did production rise or fall; what is scarce; what will next turn cost; which capacity is idle or unprofitable; can I afford this build; what happens if I change the chain; which future costs are uncertain; and does a shortage threaten my population, industry or readiness.

**ECN-177 — Six number types are never mixed.** *Provisional (REQ-158).* The report distinguishes: **historical results** (what happened), **current balances** (what exists now), **pending/reserved** (what is claimed), **forecasts** (what is expected), **market estimates** (what someone might pay) and **actual completed transactions** (what was paid). Each has a label and a different visual weight. A forecast is never displayed as a balance.

**ECN-178 — Forecasts are estimates.** *Provisional.* A forecast must state its assumptions and its uncertainty: market prices, other players' actions, population changes and military consumption can all change the outcome. The interface must not present a forecast as a promise. A forecast that cannot be computed (missing market data) is shown as "unknown", not as zero.

**ECN-179 — Every important change has a why.** *Provisional (REQ-159).* The digest explains each material change with a rule or formula reference: "Coal production fell from 20 to 10 because one of two batches was blocked by warehouse space (F-EC-012)." A player should be able to learn the economy by reading their own digests. The explanation is generated from the same data as the change, not written by hand.

**ECN-180 — Underused and unprofitable capacity is visible.** *Provisional.* The report shows, per chain: capacity, batches run, batches idle and the reason; variable cost per batch; revenue at the reference price; and a simple margin. A facility that appears productive but loses money at the current price is flagged. The player can then idle it, sell the output, or change the chain (subject to Prompt 05's respecialization rules).

**ECN-181 — Affordability is checked before commitment.** *Provisional.* A build or order screen must show the cost, the available balance, the reservation it will take, the effect on next turn's operating cost and the payback estimate at the reference price. The player must not discover the cost only after the order resolves.

**ECN-182 — Warnings are specific.** *Provisional.* A warning names the resource, the turn, the projected shortfall and the consequence. "Food may run out" is not enough; "Projected food: 38 available vs 50 demand at Turn 812; hunger penalty 720 bp next turn" is the standard.

**ECN-183 — Report definitions are fixed here.** *Provisional.* The accounting meanings (gross income, net operating income, capex, net cash flow, national wealth, available, reserved) are defined in this document. Prompt 13 owns the screens, layout and accessibility; it may not redefine a number. If a screen needs a new number, it must be added here or in the formula register first.

**ECN-184 — No false precision.** *Provisional.* A number is shown at the precision the engine actually uses: whole crowns and whole units. A percentage is shown to one decimal place at most. A forecast is rounded and labelled. The interface must not display 1,234.567 crowns when the engine stores 1,234.

---

## 18. Balance and progression

**ECN-185 — Balance targets are qualitative and testable.** *Provisional (REQ-160).* The economy targets:

1. A new nation reaches a stable food surplus and a positive net operating income within its first **three turns** under the standard start.
2. At least **three early paths** are viable: food/agriculture, energy/refining, and metals/construction.
3. At least **two mid-game paths** are viable: a specialized exporter and a diversified self-sufficient nation.
4. No single chain has a higher reference margin **and** a lower capital cost **and** a lower operating risk than every other chain.
5. A nation that loses its main export can recover within **ten turns** by idling, selling or switching, without a reset.
6. A mature nation's operating costs grow at least as fast as its tax income before optimization; optimization (specialization, power mix, trade) is what creates surplus.
7. No resource's reference price falls to zero in a world with at least one producer and one consumer.

**ECN-186 — The early game.** *Provisional.* The standard start gives food security (60 produced vs 50 consumed), a small refining chain, one coal generator and 1,500 crowns. The player's first decisions are: keep food at capacity, add a second extraction chain, build a refinery or a steel mill, and decide whether to sell raw goods or process them. The first three turns should produce a positive net operating income if the player does nothing but let the standing policies run (the start is designed to be solvent, not optimal).

**ECN-187 — The mid game.** *Provisional.* The player has enough capacity to specialize. The key decisions are: which chain to concentrate; whether to build nuclear power (uranium + lead) or stay on coal/oil; whether to export raw goods or manufactured goods; whether to hold a war stock; and whether to expand the warehouse. The reference margins are close enough that price and relationships, not a single dominant recipe, decide the winner.

**ECN-188 — The late game.** *Provisional.* The player faces rising maintenance, warehouse pressure, power demand and military upkeep. Growth is limited by capital and space, not by a hard level cap. The anti-snowball mechanism is **cost**, not a rule that forbids growth: capacity costs rise, maintenance rises, and a large nation needs more power, more food and more storage. A mature nation can stagnate if it stops investing; it cannot coast on an unassailable lead.

**ECN-189 — Anti-dominance checks.** *Provisional.* A chain is **dominant** if, at the reference prices, it has both the highest margin per batch and the lowest capital cost per batch, or if its output is required by every other chain with no substitute. The register records the margin table and a dominance test. If a chain becomes dominant after a number change, Prompt 14 must retune it or add a cost; it may not declare the imbalance acceptable without a recorded decision.

**ECN-190 — Inflation and money supply.** *Provisional.* New crowns enter only through tax income and disclosed rewards. The money supply grows with population and tax rate, not with player activity. The sinks (operating costs, maintenance, capex, fees, military upkeep) must be large enough that a mature economy does not accumulate idle crowns without a use. The register records the **money-creation test**: over a 30-turn simulation, total crowns should not grow faster than total economic output; if they do, the sinks are too small. This is a design target, not a measured result.

**ECN-191 — Hoarding and price manipulation.** *Provisional.* A player may hoard a resource, but warehouse space limits the hoard and the reference price does not rise merely because a player holds stock. A cartel can raise a market price (Prompt 07), but it cannot force a sale, and every other nation can build the same capacity at a cost. The design does not attempt to make cartels impossible; it makes them expensive and contestable.

**ECN-192 — New-player protection is economic, not a multiplier.** *Provisional.* A new nation gets the standard bundle and the B-03 protection window, not a yield bonus, free resources or a hidden subsidy. The food floor, the positive starting net income and the low early costs are the economic protection. Catch-up acceleration is rejected (D-021).

**ECN-193 — Simulation metrics for Prompt 14.** *Provisional (REQ-161).* Prompt 14 should simulate at least: a 30-turn solo nation on each of the three early paths; a 100-turn two-nation trade pair; a 100-turn world with 20 nations and random policies; a price-shock scenario; a food-shortage scenario; a war-consumption scenario; and a reroll scenario. The metrics are: turns to positive net operating income, turns to first manufactured export, treasury p90/p10, wealth Gini, food-shortage frequency, power-shortage frequency, idle-capacity share, and the share of turns with a negative cash flow. No metric is a pass/fail until Prompt 14 sets the threshold.

---


## 19. Numerical conventions and the formula register

**ECN-194 — Integer arithmetic only.** *Provisional (REQ-162).* Every economic quantity is an integer. Formulas use integer multiplication and division with an explicit floor or ceiling. No formula may depend on binary floating point, a locale-specific decimal separator or a client-side calculation. Where a percentage is needed, it is expressed in basis points (1 bp = 0.01%) and applied with integer arithmetic.

**ECN-195 — One rounding rule per formula.** *Provisional.* The formula register states, for each formula, whether the result is floored, ceiled, rounded half-up or capped. The default for money and resources is **floor**; the default for a minimum required quantity (such as food demand) is **ceil**. A formula may not inherit a rounding rule from another formula by accident. The same inputs must always produce the same output.

**ECN-196 — Units are labelled.** *Provisional.* Every formula states the unit of every input and output: crowns, units, batches, GU, people, basis points or turns. A formula without units is incomplete. A percentage is not a unit; it is a basis-point value with a stated denominator.

**ECN-197 — The register is authoritative.** *Provisional (REQ-163).* The definitive expression, variables, units, bounds, rounding, timing, dependencies and worked example for every formula live in [the economic formula and balance register](10_economic_formula_and_balance_register.md). This document may summarise a formula, but if the two disagree, the register wins until it is corrected. No third document may define a competing version.

---

## 20. Worked numerical examples

**ECN-198 — The standard test assumptions.** *Provisional.* All examples use the standard start unless stated: population 50,000; treasury 1,500; warehouse 2,000; tax rate 300 bp; stability 100%; food 120, coal 60, oil 30, iron 30, bauxite 20, lead 10, uranium 0, gasoline 20, ammunition 0, steel 20, aluminum 0; capacity food 3, coal 2, oil 1, iron 1, bauxite 0, lead 0, uranium 0; refining 1, steel 0, aluminum 0, ammunition 0; one coal generator level. Reference prices are the roster table. All arithmetic is integer with floor division. These are **illustrative test assumptions**, not balance claims.

**ECN-199 — Independent recalculation.** *Provisional (REQ-164).* Every example below was recalculated from the formulas and then checked against the register's worked values. A mismatch is a defect. The examples are not copied from a simulation because no simulation exists. Two correction passes ran on 2026-10-24. The first restated Example 8's break-even thresholds and aligned the margin sentences in Examples 7 and 8 to the register's published definitions (base margin excludes power; fully loaded includes it). The second, after an independent review, found and fixed:

- the **standard bundle's unit total** — the listed quantities sum to 310, not 350 (ECN-121, Example 1, Example 2's free-space expression, Example 17 and D-063);
- **Example 3 throughout** — its opening total was 1,560, not 1,360; uranium, bauxite and lead outputs had been read from their per-batch **costs** (28, 14, 16 crowns) instead of their yields (1, 8, 6 units); ammunition ran two batches although its capacity is **one**; every closing quantity, the closing book value (5,128), the closing wealth (6,375) and the wealth change (**+146**) were therefore wrong and are restated;
- **Example 5** — it charged a market fee of 2 crowns that B-04 has never adopted, so its closing treasury is **1,428**, and the fee is now shown only as a clearly labelled hypothetical in Example 16.

No formula, coefficient or recipe changed in either pass.

**ECN-200 — Coverage.** *Provisional (REQ-165).* Examples 1–20 cover all seventeen cases required by the Prompt 04 brief, plus power derating, hunger recovery and book-value versus market value. Each example states inputs, formulas, processing order, output, final balances, ledger events and any reservations or failures.

### Example 1 — New nation initialization

**Inputs.** The standard start. **Formulas:** F-EC-001 (tax), F-EC-013 (operating income), F-EC-016 (wealth).

**Starting bundle.** Treasury 1,500 crowns; population 50,000; warehouse 2,000. Inventory: food 120, coal 60, oil 30, iron 30, bauxite 20, lead 10, uranium 0, gasoline 20, ammunition 0, steel 20, aluminum 0 = **310 units**. Capacity: food 3, coal 2, oil 1, iron 1, refining 1; one coal generator. No debt, no reservations, no pending orders.

**Starting wealth.** `1,500 + (120×1 + 60×1 + 30×2 + 30×1 + 20×2 + 10×3 + 0×30 + 20×6 + 0×6 + 20×7 + 0×8) = 1,500 + 600 = 2,100 crowns.` Fixed-asset book value is 0 because the starting capacity was granted, not purchased.

**Why these values.** 1,500 crowns covers roughly twelve turns of full operating cost (121/turn) without income; the food stock plus production covers 3+ turns; the 20 steel and 20 gasoline let the first construction order start without a market. The bundle is intentionally **sufficient but not generous**: it teaches the chain without giving a free mid-game.

**Duplicate protection.** `NATION_INIT` is keyed by the new `nation_id` and a `starter_grant_version`. A retry with the same nation ID is a no-op; a reroll creates a **new** nation ID and grants the standard bundle once. The old nation's `NATION_RETIRED` event and balances remain in history. No account can receive two bundles for the same nation.

**Ledger.** `NATION_INIT` with the full bundle; no tax and no production yet. The first boundary settles under Example 2.

### Example 2 — Positive operating income

**Inputs.** Standard start; no manual orders; all standing policies `RUN_AT_CAPACITY`; no obligations.

**P3.1 Tax.** `floor(50,000 × 300 × 10,000 / 1,000,000,000) = 150`. Previous hunger penalty 0. Treasury 1,650.

**P3.2 Maintenance.** Food 3×1=3; coal 2×1=2; oil 1×1=1; iron 1×1=1; refining 1×2=2; generator 1×2=2. Total **11**. Treasury 1,639.

**P3.3 Extraction.** Food: `min(3, floor(1,639/12)=136, floor(2,000−310)/20=84) = 3` → 60 food, cost 36. Coal: `min(2, floor(1,603/10)=160, ...) = 2` → 20 coal, cost 20. Oil: 1 → 8 oil, cost 14. Iron: 1 → 10 iron, cost 10. Bauxite/lead/uranium capacity 0. Treasury 1,639 − 36 − 20 − 14 − 10 = **1,559**.

**P3.4 Power.** Coal generator: has 6 coal (stock 60+20=80) and 10 crowns → runs; consumes 6 coal, pays 10; produces 6 GU. Treasury 1,549. Coal 74.

**P3.5 Processing.** Refining capacity 1, draw 2; supply 6 → `power_pct = 100`; batches 1. Inputs: 10 oil (stock 30+8=38) → 28 oil; cost 20; output 8 gasoline (20+8=28). Treasury 1,529.

**P3.6 Food.** Demand `ceil(50,000/1,000)=50`; available 120+60=180; consume 50 → food 130; no shortage.

**P3.7 Obligations.** None. **P3.8 Close.** Treasury 1,529.

**Result.** Closing inventory: food 130, coal 74, oil 28, iron 40, bauxite 20, lead 10, uranium 0, gasoline 28, ammunition 0, steel 20, aluminum 0 = 350 units (310 opening + 106 produced − 66 consumed or burned; this closing total is not the starting bundle). Gross income 150; operating expenses 121; net operating income **29**; net cash flow +29. National wealth = `1,529 + (130+74+56+40+40+30+168+140) = 1,529 + 678 = 2,207`. Reconciliation: `2,100 + 29 + 78 (inventory value change) = 2,207`.

**Ledger.** `TAX_INCOME +150`; `MAINTENANCE −11`; four `PRODUCTION_COST` and four `RESOURCE_PRODUCED`; `POWER_FUEL −6 coal`, `PRODUCTION_COST −10`, `POWER_GENERATED +6 GU`; `MANUFACTURE_INPUT −10 oil`, `PRODUCTION_COST −20`, `MANUFACTURE_OUTPUT +8 gasoline`; `FOOD_CONSUMED −50`; `TURN_SETTLED`.

### Example 3 — Operating loss with rising inventory value

**Inputs.** A mature nation (not the standard start): population 50,000; opening treasury 1,529; capacities food 5, coal 4, oil 3, iron 2, bauxite 2, lead 1, uranium 1, refining 2, steel 2, aluminum 1, ammunition 1; three coal generators (18 GU). Opening inventory: food 200, coal 200, oil 200, iron 200, bauxite 200, lead 200, uranium 10, gasoline 100, steel 100, aluminum 100, ammunition 50 = **1,560 units**. All policies run at capacity; inputs are ample; no manual orders.

**Tax.** 150. **Maintenance.** Extraction 5+4+3+2+2+1+1 = 18; processing 4+4+2+2 = 12; generators 3×2 = 6; total **36**.

**Extraction.** Each batch yields the register's output per batch, and its cost is a charge, not a quantity:

| Chain | Batches | Output | Variable cost |
|---|---:|---|---:|
| Food | 5 | 100 | 60 |
| Coal | 4 | 40 | 40 |
| Oil | 3 | 24 | 42 |
| Iron | 2 | 20 | 20 |
| Bauxite | 2 | 16 | 28 |
| Lead | 1 | 6 | 16 |
| Uranium | 1 | **1** | 28 |
| **Total** | | | **234** |

**Generators.** 3×10 = **30** crowns; 18 coal burned; 18 GU produced. **Processing** (each at its stated capacity):

| Chain | Batches | Inputs consumed | Output | Variable cost | Power |
|---|---:|---|---:|---:|---:|
| Refining | 2 | 20 oil | 16 gasoline | 40 | 4 GU |
| Steel | 2 | 20 iron + 12 coal | 16 steel | 48 | 6 GU |
| Aluminum | 1 | 12 bauxite | 8 aluminum | 24 | 4 GU |
| Ammunition | **1** | 8 lead + 4 coal | 10 ammunition | 20 | 2 GU |
| **Total** | | | | **132** | **16 GU** |

**Total operating expenses = maintenance 36 + extraction 234 + generators 30 + processing 132 = 432.**

**Power.** Demand = refining 4 + steel 6 + aluminum 4 + ammunition 2 = 16; supply 18 → `power_pct=100`; all planned batches run.

**Closing inventory, line by line.** `closing = opening + produced − consumed − burned`:

| Resource | Opening | Produced | Consumed or burned | Closing |
|---|---:|---:|---:|---:|
| Food | 200 | 100 | 50 (population) | **250** |
| Coal | 200 | 40 | 12 (steel) + 4 (ammunition) + 18 (generators) | **206** |
| Oil | 200 | 24 | 20 (refining) | **204** |
| Iron | 200 | 20 | 20 (steel) | **200** |
| Bauxite | 200 | 16 | 12 (aluminum) | **204** |
| Lead | 200 | 6 | 8 (ammunition) | **198** |
| Uranium | 10 | 1 | 0 | **11** |
| Gasoline | 100 | 16 | 0 | **116** |
| Steel | 100 | 16 | 0 | **116** |
| Aluminum | 100 | 8 | 0 | **108** |
| Ammunition | 50 | 10 | 0 | **60** |
| **Total** | **1,560** | | | **1,673** |

No input is consumed twice, and no line exceeds the 2,000-unit warehouse (1,673 at close).

**Treasury.** `1,529 + 150 − 432 = 1,247`. Gross income 150; net operating income **−282**; net cash flow −282.

**Wealth.** Closing book value = `250×1 + 206×1 + 204×2 + 200×1 + 204×2 + 198×3 + 11×30 + 116×6 + 116×7 + 108×8 + 60×6` = `250 + 206 + 408 + 200 + 408 + 594 + 330 + 696 + 812 + 864 + 360` = **5,128 crowns**. Opening book value = **4,700 crowns**. Inventory value change **+428**. Closing national wealth = `1,247 + 5,128 = 6,375`; opening wealth = `1,529 + 4,700 = 6,229`; wealth **rises by 146** even though cash falls by 282 (`−282 + 428 = +146`).

**Interpretation.** An operating loss is not automatically a failure. The nation earned 150 in tax and spent 432 on operations, so cash fell by 282, while the inventory's book value rose by 428; wealth therefore rose by 146. The loss is real in cash but almost neutral in book terms. The gain is also fragile — it depends on selling those goods near the reference price. If the market price is below it, the "gain" is illusory. The report must show the cash loss, the inventory change and the estimated character of the valuation separately. This is the liquidity-versus-wealth distinction (ECN-017).

### Example 4 — Capital expenditure versus operating expense

**Inputs.** Standard start after Example 2 (treasury 1,529; food capacity 3; steel 20; gasoline 28). A construction order adds **1 food capacity** for **150 crowns + 10 steel + 5 gasoline**.

**P4 (same turn).** Charge 150 crowns, 10 steel, 5 gasoline. Treasury 1,379; steel 10; gasoline 23. Fixed-asset book value += `150 + 10×7 + 5×6 = 150 + 70 + 30 = 250`. National wealth is unchanged by the construction itself (liquid assets converted into a fixed asset); no fee is involved, because B-04 adopts none.

**Next turn.** Food capacity 4. Maintenance rises by 1 (to 12); variable food cost rises by 12 (to 48); total operating expenses 134; tax 150; net operating income **+16**, down from +29. Extra food output 20 units. At the reference price of 1, the extra batch earns 20 and costs 13 (12 variable + 1 maintenance), a margin of **7 crowns/turn**; payback on the 250 book value is about **36 turns**. At a market price of 0.5, the extra batch earns 10 and loses 3/turn, so it never pays back at that price.

**Interpretation.** The build reduces current cash and future net operating income, but adds capacity and food. It is rational only if the player values the food (security, growth, a future price) above the 13 crowns/turn it costs. A facility that "produces something" can still be a loss at the market price; the report must show the margin, not only the output.

### Example 5 — Treasury surplus reconciliation

**Inputs.** Opening 1,529; tax 150; operating expenses 121; capex 150; sale of 5 steel at 10 = +50; purchase of 10 coal at 3 = −30. **No market fee is charged**, because B-04 adopts none: market prices, matching and any fee belong to Prompt 07 (D-060, ECN-211). No other flows.

**Closing** = `1,529 + 150 − 121 − 150 + 50 − 30 = 1,428`. Net operating income = `150 − 121 = 29`. Net cash flow = `1,428 − 1,529 = −101`.

**Reconciliation.** `opening + net operating income − capex + net trade = 1,529 + 29 − 150 + 20 = 1,428`. The sale and purchase net to +20 because the sale is +50 and the purchase is −30. The identity holds to the crown, with no fee term to explain.

**Wealth note.** At reference prices the sale hands over a 35-crown asset for 50 (+15) and the purchase pays 30 for a 10-crown asset (−20), so trade alone lowers book wealth by 5; capex converts 150 of liquid assets into 150 of fixed-asset value, leaving wealth unchanged.

**Ledger.** `TAX_INCOME +150`; operating `PRODUCTION_COST` and `MAINTENANCE` totaling −121; `CAPEX −150`; `TRADE_SELL +50` and `INVENTORY_OUT −5 steel`; `TRADE_BUY −30` and `INVENTORY_IN +10 coal`; `TURN_SETTLED`.

### Example 6 — Raw-resource production with a warehouse limit

**Inputs.** Coal capacity 5; coal output 10/batch; variable cost 10/batch; maintenance 5; opening coal 1,975 units; warehouse 2,000; free space 25; unreserved treasury 100.

**Batches.** Batch 1: space 25 ≥ 10, money 100 ≥ 10 → runs; coal 1,985, free 15, money 90. Batch 2: space 15 ≥ 10, money 90 ≥ 10 → runs; coal 1,995, free 5, money 80. Batch 3: space 5 < 10 → **blocked**; no money consumed. Batches 4–5 would also be space-blocked, but the chain stops at the first blocked batch for that turn (a deterministic rule; it does not skip ahead).

**Result.** 2 batches run, 20 coal produced, variable cost 20, maintenance 5, total cost 25; closing coal 1,995; free space 5; treasury 75. Digest: "2 of 5 batches ran; 3 blocked by warehouse space (need 10, free 5)." No coal is destroyed.

### Example 7 — Oil to gasoline

**Inputs.** Treasury 1,529; oil 28; gasoline 28; refining capacity 2; coal generator supply 6 GU; refining maintenance 4; no manual order (standing policy).

**Power.** Demand 2×2=4; supply 6 → `power_pct=100`. **Batches.** 2. **Inputs.** 20 oil → oil 8. **Cost.** 40. **Output.** 16 gasoline → gasoline 44. **Treasury.** 1,489. **Space.** Output 16 units; inventory is far below 2,000, so no block.

**Ledger.** `MANUFACTURE_INPUT −20 oil`; `PRODUCTION_COST −40`; `MANUFACTURE_OUTPUT +16 gasoline`; `TURN_SETTLED`.

**Interpretation.** The nation turned 20 oil (book 40) into 16 gasoline (book 96) for 40 crowns of variable cost and 4 crowns of maintenance: a **base margin of +12** over the two batches (+6 each, register F-EC-036). The 4 GU of coal-fired power cost about 12 crowns (F-EC-037), so the **fully loaded margin is 0**. The break-even gasoline price is 6; below 6 the chain loses money, and at 7 it earns +8 per batch (one extra crown on each of eight units). At the reference price, running the refinery is a bet on the gasoline market, not a guaranteed profit. This is the margin the player must watch.

### Example 8 — Bauxite to aluminum

**Inputs.** Treasury 1,529; bauxite 100; aluminum 0; smelting capacity 1; supply 6 GU; maintenance 2.

**Power.** Demand 4 ≤ 6 → 100%. **Batch.** 1. **Inputs.** 12 bauxite → 88. **Cost.** 24. **Output.** 8 aluminum. **Treasury.** 1,505. **Ledger.** `MANUFACTURE_INPUT −12 bauxite`; `PRODUCTION_COST −24`; `MANUFACTURE_OUTPUT +8 aluminum`.

**Interpretation.** Aluminum is the most power-intensive chain: one batch consumes two-thirds of a coal generator's output. The nation must decide whether the higher book value (8×8=64 vs 12×2=24) justifies the power and the 24-crown variable cost. The **base margin is +14** (64 − 24 − 24 − 2, register F-EC-036) and the **fully loaded margin is +2** once the 12 crowns of coal-fired power are charged (F-EC-037). The batch stops paying when bauxite rises above **2.17** at the reference aluminum price, or aluminum falls below **7.75** at the reference bauxite price; ignoring the power cost, the thresholds are 3.17 and 6.25.

### Example 9 — Iron and coal to steel

**Inputs.** Treasury 1,529; iron 100; coal 100; steel 0; steel capacity 2; supply 6 GU; maintenance 4.

**Power.** Demand 2×3=6; supply 6 → 100%. **Batches.** 2. **Inputs.** 20 iron + 12 coal → iron 80, coal 88. **Cost.** 48. **Output.** 16 steel. **Treasury.** 1,481. **Ledger.** `MANUFACTURE_INPUT −20 iron`, `MANUFACTURE_INPUT −12 coal`; `PRODUCTION_COST −48`; `MANUFACTURE_OUTPUT +16 steel`.

**Interpretation.** Steel is the only two-input recipe in the launch set. A nation with iron but no coal cannot run it; a nation with coal but no iron cannot run it. This is the clearest reason to trade even if a nation is self-sufficient in one input.

### Example 10 — Ammunition

**Inputs.** Treasury 1,529; lead 50; coal 50; ammunition 0; ammunition capacity 2; supply 6 GU; maintenance 4.

**Power.** Demand 2×2=4 ≤ 6 → 100%. **Batches.** 2. **Inputs.** 16 lead + 8 coal → lead 34, coal 42. **Cost.** 40. **Output.** 20 ammunition. **Treasury.** 1,489. **Ledger.** `MANUFACTURE_INPUT −16 lead`, `MANUFACTURE_INPUT −8 coal`; `PRODUCTION_COST −40`; `MANUFACTURE_OUTPUT +20 ammunition`.

**Lead's adopted role.** Lead is the ammunition payload and a nuclear-generator shielding input. There is no steel or uranium in the ammunition recipe; the adopted chain is **8 lead + 4 coal → 10 ammunition**. A nation that wants both ammunition and nuclear power must split its lead supply; that is the intended trade-off.

### Example 11 — Population food consumption and shortage

**Case A — sufficient.** Population 50,000 → demand 50. Opening food 30; production 20 → 50; consume 50 → 0; unmet 0; penalty 0. Treasury unaffected.

**Case B — total shortage.** Next turn production 0; stock 0; demand 50; `unmet=50`; `hunger_penalty_bp = min(3000, floor(3000×50/50)) = 3000`. Stored for next turn. Next turn tax = `floor(150 × (10,000−3,000)/10,000) = floor(105) = 105`. The nation loses 45 crowns of tax, not a third of its gross output. Population/stability consequences are Prompt 06's.

**Case C — partial shortage.** Stock 30; demand 50; `unmet=20`; penalty `floor(3000×20/50)=1200`; next tax `floor(150×8,800/10,000)=132`. The penalty is proportional, not a cliff.

**Recovery.** If the next turn has no shortage, the stored penalty is cleared at the following P3.1; tax returns to 150. A player sees the penalty and its expiry in the digest.

### Example 12 — Insufficient inputs and an accepted-then-failed order

**Submission rejection.** Refining capacity 2; oil 15; a manual order for 2 batches needs 20 oil. At submission, available oil 15 < 20 → `REJECTED` (`F1`), no reservation, no ledger event beyond the rejection record. The player is told "need 20 oil, have 15; no reservation taken."

**Accepted-then-failed.** Same nation, but at acceptance it had 20 oil; the order reserved 20 oil, 40 crowns, 2 refining batches and 16 output space (power is **not** reserved — grid units are derived and cannot be held, ECN-065). At P3 the grid supplies only 2 GU (a generator is idle), demand 4, so `power_pct = floor(100×2/4) = 50` and `batches_available = floor(2×50/100) = 1`. The manual order needs 2 batches; it cannot run partially. It fails with `F5`, and **all** reservations are released: 20 oil, 40 crowns, 2 refining batches, 16 space. The standing policy then runs 1 batch: 10 oil + 20 crowns → 8 gasoline. Final oil 10, gasoline 8, treasury 1,529 − 20 = 1,509 before tax and maintenance, which this example leaves out because the failed order does not change them.

**Ledger.** `RESERVATION_HELD` (4 events) → `MANUFACTURE_FAILED` with `F5` → `RESERVATION_RELEASED` (4 events) → `MANUFACTURE_INPUT −10 oil`, `PRODUCTION_COST −20`, `MANUFACTURE_OUTPUT +8 gasoline`. The failed order consumed nothing. This is the exact rejection/release behaviour the brief requires.

**Capacity accounting — why the demand is 4 GU and not 8.** The chain has `C = 2`; the order reserved `M = 2`; the standing policy therefore has no unreserved slot to fill, `A = 0`, and `planned_batches = M + A = 2 ≤ C`. Demand is `2 × 2 = 4 GU`. Adding the manual batches to capacity (`C + M = 4` batches, 8 GU) would give `power_pct = floor(100×2/8) = 25` and `batches_available = 0`, so the standing policy would run nothing and this example's stated outcome (one batch, 8 gasoline) would be impossible. That is the proof that manual orders occupy capacity rather than extending it. The single automatic batch that runs after the manual order fails fills a slot the failure released; it was already covered by the planned demand, so no re-plan and no second demand is needed (ECN-063).

| Case | `C` | `M` | Policy | `A` | `P = M + A` | Refining demand |
|---|---:|---:|---|---:|---:|---:|
| Manual fills the chain | 2 | 2 | `RUN_AT_CAPACITY` | 0 | **2** | 4 GU, not 8 |
| Mixed | 3 | 1 | `RUN_AT_CAPACITY` | 2 | **3** | 6 GU, not 8 |
| Idle with spare capacity | 3 | 0 | `IDLE` | 0 | **0** | 0 GU |

In the idle case the chain still pays maintenance — `3 × 2 = 6` crowns at P3.2 — because idle capacity is a standing cost (ECN-051/052); it simply plans no batches and draws no power. The multi-chain shortfall case is Example 18, and the repeated-settlement case is Example 14.

### Example 13 — Storage capacity and overflow

**Extraction.** Food capacity 3; output 20/batch; free space 12; unreserved treasury 100; maintenance 3. Batch 1 needs 20 space > 12 → **blocked**. No batch runs; no variable cost. Treasury 100−3 = 97. Digest: `SPACE_BLOCKED` food, need 20, free 12, 3 batches blocked; "sell or expand storage." Nothing is destroyed.

**Processing.** Steel capacity 1; free space 5; output 8 steel; inputs 10 iron + 6 coal. The batch is blocked by space; the iron and coal are **not** consumed and the 24-crown variable cost is **not** charged. Maintenance 2 is still charged. This is the no-silent-loss rule (ECN-124).

### Example 14 — Duplicate settlement

**First run.** Settlement key `(turn 812, nation 42)`. It completes: opening 1,529, closing 1,529 (a no-op turn for simplicity), events `TAX_INCOME`, `MAINTENANCE`, `FOOD_CONSUMED`, `TURN_SETTLED`. The marker is `COMPLETE`.

**Second run.** The scheduler invokes the same key. The engine reads the marker, sees `COMPLETE`, and returns the stored digest. It writes **no** new events, charges nothing and produces nothing. A duplicate delivery is a no-op.

**Third run with a different config version.** The key matches but the frozen configuration version differs. The engine rejects the attempt as a conflict; it does not re-settle the turn with new rules. The original result stands.

**Event-key check.** The tax event has `event_key = H(812,42,'P3.1','tax',1)`. A retry computes the same key; the unique constraint makes the insert a no-op. A different event with the same key aborts the turn as a defect. This is exactly-once at the event level, not only at the settlement level.

### Example 15 — Insolvency without debt

**Inputs.** Population 6,667 (so `floor(6,667 × 300 × 10,000 / 1,000,000,000) = 20` tax income and `ceil(6,667/1,000) = 7` food demand); opening treasury 50; capacities food 3, coal 2, oil 1; no processing, no generator; maintenance **6** (`3 + 2 + 1`, ECN-147a); opening food 10, coal 5, oil 5; no reservations; military upkeep obligation 20 (Prompt 10).

**P3.** Treasury 50+20=70. Maintenance 6 → 64 (one whole obligation per chain, ECN-147a). Food 3 batches ×12=36 → 28. Coal 2×10=20 → 8. Oil 1×14=14 > 8 → 0 batches; the batch does not run and the 8 crowns are not spent on a fraction. Closing **8**. Food +60 (7 of the 70 on hand are eaten, leaving 63), coal +20; oil unchanged.

**Obligation.** Military upkeep 20 > 8 → `OBLIGATION_CANCELLED` for 20; readiness falls by the Prompt 10 rule (for example one readiness tier); no debt, no negative balance, no confiscation. The player can sell coal/food next turn, idle a chain, or wait for tax.

**Reservation protection.** If a manual order had reserved 20 crowns before the boundary, those 20 would be excluded from the 50 unreserved; the obligation could not touch them. The order would run or fail on its own terms. This is B-02 TR-070 applied to the economy.

### Example 16 — Market accounting contract

**Sale.** Seller has 1,529 crowns and 20 steel; buyer has 1,000 crowns and 0 steel. Directed sale of 20 steel at 8 crowns = 160. At acceptance the transfer is atomic: seller crowns 1,689, steel 0; buyer crowns 840, steel 20. No crowns are created or destroyed. The seller's book value falls by 140 and cash rises by 160 → wealth +20; the buyer's cash falls by 160 and book value rises by 140 → wealth −20; world wealth is unchanged.

**Hypothetical fee — illustrative only, not adopted.** *If* Prompt 07 later adopts a 2% fee, the accounting would be: `floor(160 × 200 / 10,000) = 3`. Seller receives 157; the 3 crowns are destroyed as a `FEE`; buyer still pays 160. World crowns fall by 3, world wealth falls by 3. The fee would have to be disclosed before acceptance and shown on both sides. **B-04 adopts no fee and fixes no rate**; this paragraph exists only to show how a fee, if adopted, must interact with the ledger and with both parties' balances.

### Example 17 — Nation deletion and replacement

**Old nation (N-100).** Treasury 1,529. Inventory: food 130, coal 74, oil 28, iron 40, bauxite 20, lead 10, uranium 0, gasoline 28, ammunition 0, steel 20, aluminum 0. Reserved: 40 crowns and 10 oil for a pending manual refining order; an open trade offer for 5 steel; no active campaign; no preservation hold.

**Retirement.** The pending order is cancelled and its reservations released; the open offer is withdrawn; every inventory unit is destroyed; the 1,529 crowns are destroyed. `NATION_RETIRED` records the final balances, the nation ID, the account ID, the turn and the reason (`REROLL`). No crown, unit, capacity, research or queue transfers. Public history (founding, treaties, wars, chronicle entries) remains attributed to N-100; the old page becomes a historical page (B-03 RRL-020).

**Replacement (N-101).** New nation ID; standard bundle: 1,500 crowns; 310 units (the Example 1 list); standard capacity; no protection (B-03 RRL-018); unranked until its first boundary; new ledger starting with `NATION_INIT`. National wealth 2,100, not the old nation's ~2,207. The account keeps its tutorial, sanctions, pair restrictions, moderation history and recovery codes. No old asset is converted, refunded, stored or gifted (RRL-014).

**Audit.** The old nation's ledger is not deleted; it is closed with `NATION_RETIRED` and remains queryable by the account and by authorized audit. The replacement's ledger is separate. A later dispute can trace exactly what was destroyed and when.

### Example 18 — Power shortfall and derating

**Inputs.** Refining capacity 2 (draw 2/batch), steel capacity 2 (draw 3/batch); grid supply 6 GU; ample inputs and money. `power_demand = 2×2 + 2×3 = 10`; `power_pct = floor(100×6/10) = 60`.

**Batches.** Refining `floor(2×60/100)=1`; steel `floor(2×60/100)=1`. The other refinery batch and steel batch are **power-blocked**, not input-blocked. Actual draw = 1×2 + 1×3 = 5 GU; 1 GU is surplus and discarded.

**Outcome.** Refining consumes 10 oil, costs 20, produces 8 gasoline. Steel consumes 10 iron + 6 coal, costs 24, produces 8 steel. Total processing cost 44. A manual order for 2 steel batches accepted earlier would fail atomically with `F5` because only 1 batch is available; its reservations would be released, and the standing steel policy would still run 1 batch. The digest names power as the cause, not inputs.

### Example 19 — Hunger penalty recovery

**Turn 1.** Demand 50; available 30; unmet 20; penalty `floor(3000×20/50)=1200` stored for Turn 2.

**Turn 2.** Tax = `floor(150×8,800/10,000)=132`. If Turn 2 has no shortage, the stored penalty is cleared at Turn 3's P3.1; Turn 3 tax returns to 150. If Turn 2 has a smaller shortage (unmet 10), a new penalty of `floor(3000×10/50)=600` is stored; Turn 3 tax = `floor(150×9,400/10,000)=141`. There is no stacking: the new penalty replaces the old one.

**Interpretation.** A single bad turn costs 18 crowns of tax in the following turn; a second bad turn costs another 9. The nation can recover in one good turn. This is deliberately gentler than a permanent famine or a one-third income cliff.

### Example 20 — Reference value versus market value

**Hold.** A nation holds 10 steel. Reference price 7 → book value 70; national wealth includes 70. No crowns are available from the holding.

**Sell at 5.** Market price 5 → proceeds 50. Treasury +50; inventory −10 steel; book value −70; national wealth −20. The nation is more liquid by 50 and less wealthy by 20. At a price of 7, wealth is unchanged; at 9, wealth rises by 20.

**Interpretation.** A high reference price does not mean a buyer exists. The report must show the reference value as an estimate, the last actual transaction as a fact, and the market price as a third number. This is the six-number discipline (ECN-177) applied to one holding.

---

## 21. Account policy, reroll and economic fairness

**ECN-201 — The standard bundle is once per nation.** *Provisional (REQ-166).* The `NATION_INIT` event is keyed by the new `nation_id` and a `starter_grant_version`. A retry or a duplicate request cannot grant a second bundle to the same nation. A reroll creates a new nation ID and therefore a new bundle, but the **account-level** protection is not re-granted (B-03 RRL-018) and the fresh-nation transfer restriction applies (B-03 ONB-019…ONB-035).

**ECN-202 — No asset transfer across a reroll.** *Provisional (REQ-167).* No crown, resource, capacity, research, queue, reservation or pending order may be carried, converted, refunded, stored, gifted or transferred to the replacement. The old nation's balances are destroyed; the replacement receives only the standard bundle. This is the economic application of B-03 RRL-013/RRL-014 and REQ-068.

**ECN-203 — Disposition of every pending economic object.** *Provisional (REQ-168).*

| Object at reroll | Required disposition |
|---|---|
| Open trade offers | Withdrawn, no fee, no value movement (B-03 RRL-019) |
| Accepted but unsettled trade | Must resolve or be cancelled before retirement; otherwise the reroll is blocked (B-03 RRL-021) |
| Pending manual manufacturing order | Cancelled; all reservations released; no charge |
| Pending construction order | Cancelled; reservations released; no refund of a completed stage (Prompt 05) |
| Reserved crowns/resources | Released and then destroyed with the nation; never transferred |
| Warehouse contents | Destroyed; no spillover, storage or gift |
| Tax income for the current turn | If the nation is retired before the boundary, it is not settled; no partial tax |
| Unpaid obligation | Dies with the nation; no debt survives |
| Ledger history | Retained under the old nation ID; `NATION_RETIRED` closes it |

**ECN-204 — Sanctions survive.** *Provisional (REQ-169).* An account-level warning, suspension, ban, pair restriction, preservation order or open case is unaffected by a reroll. A banned account cannot create a replacement. A preservation order blocks the reroll. A reroll is not an amnesty, an investigation escape or a protection reset (B-03 RRL-026…RRL-028).

**ECN-205 — Shared-network restrictions apply to economic actions.** *Provisional (REQ-170).* A restricted pair may not use a trade, gift, aid payment, construction contract, market order or any other value-moving economic action to achieve what the interaction matrix forbids. The pair check is a single shared call (B-03 CON-002); B-04 does not re-implement IP matching. An economic action that violates the restriction moves nothing and is reported.

**ECN-206 — History is retained and attributable.** *Provisional (REQ-171).* The old nation's economic events remain attributed to the old `nation_id`; they are not re-parented to the account or to the replacement. Public history may remain visible under the old identity; private events remain private. The audit spine is permanent and is not deleted with the nation (D-026/D-042).

**ECN-207 — Starter farming is a review signal, not an automatic punishment.** *Provisional.* A pattern of creating a nation, extracting transferable value and rerolling is reviewable under B-03 RRL-024/RRL-030. The economic evidence is: the standard bundle, the transfer window, the fair-value band (Prompt 07) and the ledger of transfers. No automatic ban follows from a single signal; a shared IP alone is never sufficient (D-018, B-03 NET-039).

**ECN-208 — The fair-value band and transfer window are Prompt 07's.** *Provisional.* B-04 requires that a transfer at a price far outside the reference band is flagged for review, and that the fresh-nation restriction has a defined window. The exact band, window and review threshold are Prompt 07's with Prompt 14's validation; B-04 does not invent them. This is a named dependency, not an unresolved design question that blocks the economy.

---


## 22. Cross-system contracts

**ECN-209 — Prompt 05 (cities, infrastructure, production, research).** *Provisional (REQ-172).* Prompt 05 may add capacity, buildings, slots, upgrades and research modifiers. It must: use the B-04 recipes and coefficients; charge capex at P4 with reservation; add fixed-asset book value; charge maintenance; make new capacity available next turn; declare any yield or cost modifier in the formula register with a cap; and not change a recipe's input list. It owns construction costs, prerequisites, slot limits and warehouse expansion costs; B-04 owns what a batch consumes, produces and costs to run.

**ECN-210 — Prompt 06 (population and domestic politics).** *Provisional (REQ-173).* Prompt 06 owns population size and growth, stability, tax-rate bounds, the stability factor and the political consequences of hunger. It must use B-04's food demand formula and hunger penalty, and may not redefine them. It must supply `population`, `tax_rate_bp` and `stability_factor_bp` as frozen inputs at P3. A stability change takes effect at the next boundary, not retroactively within a turn.

**ECN-211 — Prompt 07 (trade and markets).** *Provisional (REQ-174).* Prompt 07 owns offers, prices, matching, fees and the fair-value band. It must: settle atomically (both legs or neither); use the B-04 reservation and ledger rules; never create or destroy value except an explicit fee; check warehouse space on the buyer; respect D-016 (offers do not reserve) and D-017 (terms are parties-only); and write `TRADE_BUY`/`TRADE_SELL` events with a shared `transfer_id`. A trade settles at P4 and cannot change a P3 production result. The fresh-nation transfer window and fair-value band are Prompt 07's; B-04 requires them to exist.

**ECN-212 — Prompt 08 (diplomacy).** *Provisional (REQ-175).* Prompt 08 may create aid, reparations, embargoes and sanctions. Any crown or resource movement is a transfer with matched ledger events; an embargo blocks a transfer but does not destroy the goods; a sanction may freeze an action but may not create a negative balance. Diplomatic effects on trade are applied at P4. D-030's pending-act visibility applies.

**ECN-213 — Prompt 09 (alliances).** *Provisional (REQ-176).* If Prompt 09 creates an alliance pool, it is a separate audited pool with its own ledger and permissions. A contribution is a transfer out of a nation and into the pool; a draw is a transfer out of the pool. No alliance may mint crowns or resources, and no member may use the pool to bypass a pair restriction (D-035). If Prompt 09 does not create a pool, no B-04 rule changes. The **Alliance Receiving Ledger** defined in ECN-213a is a receipt and accounting record, not that conditional pool: it decides no ownership, custody or capacity and does not bring a general withdrawal pool into existence; its only permitted debit path is the purpose-limited operational funding specified in [B-09 §29.7](16_alliances.md) (`ALL-220`–`ALL-226`, `F-AL-008`), which is currently unavailable because no cost schedule is approved, so received value remains in the ledger.

**ECN-213a — Prompt 09 automatic per-turn production taxation and voluntary donations (`D-140`, with the narrow operational-funding boundary added by `D-141`).** *Binding inherited transfer constraints; ARL receipt/accounting categories and the purpose-limited operational-funding boundary specified under `D-140`/`D-141`; general treasury policy remains Open under `UD-046`.* `D-140` authorizes two value movements from a nation to an alliance. `D-141`, dated 2026-11-02, later adds only the purpose-limited operational-funding boundary; the four categories, the AOP labels, the permission name and the reservation/settlement mechanics are project technical design choices made under `D-014`, not owner selections, and no cost schedule, fee, amount, office or implementation is approved. Tax and donation value is received and accounted for and remains in the ARL; no purpose is currently spendable, so actual expenditure is blocked pending the required approvals. (a) An **alliance tax** is collected automatically each turn from the current-turn production of each active member in the frozen snapshot. (b) A **voluntary donation** is initiated and confirmed by the donating owner. Both are canonical transfers under ECN-212/TR-060: matched `TRANSFER_OUT`/`TRANSFER_IN` ledger events under one `transfer_id`, integer amounts, conservation, no minting, no destruction and no negative balance.

**Taxable base.** Crowns: the gross national tax income computed and credited in P3.1 by ECN-094/ECN-146 for the same turn, before the alliance tax. Resource: the gross output of each supported stored resource produced in P3.3 extraction or P3.5 processing for the same turn, before the alliance tax and before any later P3 consumption. The base excludes opening Crowns, existing stockpiles, earlier production, donations, gifts, aid, reparations, market purchases or sale proceeds, trade receipts, rewards and any other inflow the existing economy does not classify as production for the turn. GU is not stored and not taxable; a future stored resource starts at 0% until configured.

**Rates, brackets and governance.** Each member nation is assigned at most one named, versioned bracket **per Alliance**, and an assignment belongs to exactly one Alliance. A nation in multiple alliances is assigned separately in each; a bracket in one Alliance creates no bracket, rate or assignment in another, and no bracket is borrowed across alliances. Each bracket supplies a separate rate for Crowns and for each taxable resource. A rate is an integer number of basis points from 0 to 10,000 inclusive (0% through 100%); it is not restricted to 10% increments and is never silently rounded to a ladder. Different members and different assets may carry different rates. The alliance's own constitution and role permissions decide who may create, edit or delete brackets, set Crowns rates, set resource rates, assign brackets, view aggregate reports and view member contribution history; this narrow tax-management set is the only `UD-045` authorization and no fixed office exists. An unassigned, deleted or invalid assignment, or an asset with no configured rate, uses the explicit visible 0% fallback. A non-member is never taxed. No per-policy owner consent is required: taxation is an internal alliance economic rule distinct from B-08 national diplomacy.

**Snapshot and effective turn.** One deterministic cutoff before P3 freezes membership, bracket versions, assignments and permissions. A change submitted before the cutoff applies to turn $t$; a change submitted at or after the cutoff applies to turn $t+1$. The snapshot is immutable, its identifier is recorded and shown, no mid-calculation change is possible, and no past turn is recomputed after an edit or deletion.

**Calculation and settlement.** For each asset $a$, production events $j=1,\ldots,m_a$ are ordered by the deterministic P3 sequence with integer gross $g_{a,j}$, cumulative gross $C_{a,j}=\sum_{k\le j}g_{a,k}$, $C_{a,0}=0$, and cumulative tax due $D_{a,j}=\lfloor C_{a,j} \times \text{rate\_bp}_a / 10{,}000 \rfloor$, $D_{a,0}=0$. The tax at event $j$ is $\text{TaxAtEvent}_{a,j}=D_{a,j}-D_{a,j-1}$, and the end-of-turn tax is $\text{tax}_a=D_{a,m_a}=\lfloor \text{gross}_a \times \text{rate\_bp}_a / 10{,}000 \rfloor$, so $\sum_j \text{TaxAtEvent}_{a,j}=\text{tax}_a$; $0 \le \text{TaxAtEvent}_{a,j} \le g_{a,j}$, $0 \le \text{tax}_a \le \text{gross}_a$, and 100% is valid. A single-event asset, including Crowns in P3.1, uses $m_a=1$ and reduces to the per-turn floor. Independent per-event floors are not used because they under-collect when several small events each carry a fractional remainder. The sequence is: (1) freeze the snapshot; (2) obtain the authoritative per-event gross eligible production sequence from the existing P3 calculation; (3) determine the per-asset rate and whether membership-tax attribution is unambiguous; (4) for each event in deterministic order compute $C_{a,j}$, $D_{a,j}$, $\text{TaxAtEvent}_{a,j}$ and the event net $g_{a,j}-\text{TaxAtEvent}_{a,j}$; (5) credit the Alliance Receiving Ledger's `RECEIVED` and `AVAILABLE` categories by the event tax and credit the nation by the event net in one atomic event; (6) let every later same-turn P3 stage consume only the cumulative post-tax net; (7) write the per-event paired ledger events and the immutable receipt/audit record in the same atomic transaction, then reconcile at end of turn that the event taxes sum to $D_{a,m_a}$. Crowns tax settles in P3.1 after `TAX_INCOME` and before P3.2; resource tax settles at the P3.3/P3.5 production event before later P3 consumption. Alliance tax is never collected in P4 and is not an ECN-152 obligation. Later stages may consume the post-tax net plus any already-owned stockpile; an existing stockpile consumed later is not taxed by that consumption, a processing input is not taxed again, and only the newly generated output is taxed once under its own rate. A 100% rate leaves zero of that turn's production available to later same-turn stages and can leave no post-tax Crowns for P3.2 maintenance: ECN-147/ECN-147a then pay only what the unreserved balance can cover, mark unpaid capacity `UNMAINTAINED` and create no negative balance, debt, forced borrowing or confiscation. A high rate is therefore valid but visibly consequential, not a route to charging an opening balance.

**Multiple-membership safeguard (`UD-040` remains Open).** This rule does not decide whether a nation may belong to one alliance or several. It specifies only that one eligible production event is deducted at most once, that the same asset can never lose more than 100% of its gross production, that multiple membership never authorizes multiple deductions and that no alliance is preferred over another. If the applicable alliance or bracket cannot be established unambiguously because of multiple membership or conflicting attribution, the provisional behaviour is an explicit, visible and recorded 0% Alliance-tax fallback for the affected asset and turn: the gross production is credited in full and is not delayed, reduced or destroyed, no alliance is credited, and normal collection resumes at the first later turn with unambiguous attribution. A safeguarded turn is not retroactively re-taxed when attribution is later resolved. The safeguard is reversible and is not an owner approval of any multiple-membership policy.

**Idempotency and failure.** The deterministic key `(settlement_id, nation_id, asset)` prevents double collection across retries, reconnects, duplicate events or resumed phases; a retry returns the original receipt and a conflicting reuse aborts as `ALF-23`. Because the base is current-turn production, no post-tax balance or post-tax inventory is ever re-taxed. A missing, incomplete or inconsistent authoritative production record or frozen snapshot, a failed paired ledger write or a conflicting idempotency-key reuse is `ALF-23`; no opening balance or existing stockpile is charged and no partial collection exists. A technical failure aborts the atomic production+tax transaction and the turn retries from its checkpoint; no generated production or tax is silently rejected, destroyed or lost. The ARL assumes no capacity limit and may not reject, destroy or lose generated tax because no capacity model has been approved. A 0% bracket, the explicit 0% fallback or the multiple-membership safeguard produces no transfer and no failure.

**Alliance Receiving Ledger.** The ARL is the alliance's receipt and accounting record for tax collected under this rule, for voluntary donations and for authorized operational credits. It distinguishes four non-negative categories: `RECEIVED` (all credits), `AVAILABLE` (unreserved and unspent), `RESERVED` (authorized but unsettled) and `EXPENDED` (settled operational expenses), and enforces `AVAILABLE = RECEIVED − RESERVED − EXPENDED` with append-only history. It records the source nation, asset, amount, turn, `transfer_id`, bracket/version/rates used (for tax), snapshot identifier, idempotency key and audit reference. It is not a treasury pool and decides no ownership, custody, capacity, general withdrawal, general spending, unrestricted transfer, distribution or dual approval; those remain Open under `UD-046`. The four categories keep receipt accounting separate from allocation and from approved operational expenditure, and general treasury authority is a distinct concept that this rule does not create. The only permitted debit path is a purpose-limited operational expense in `ALL-220`–`ALL-226` and `F-AL-008`: a closed AOP-01–AOP-04 purpose with an approved cost schedule, exact asset and amount, registered platform cost sink, active `AUTHORIZE_OPERATIONAL_EXPENDITURE` permission, complete authorization record, atomic reservation then settlement, one-time idempotent receipt and `AUD-AL-019` audit. No AOP purpose currently has an approved cost schedule, so every purpose is unavailable, no reservation or expenditure can execute, and all received value remains in the ARL. That is a specification dependency awaiting owner approval, not a spending feature. No role, AI, platform actor or administrator may make a general withdrawal, distribute ARL value to a player, nation, officer or external recipient, or redirect it to a private debt; the operational expense pays only the registered platform sink. The ARL assumes no capacity limit: it may not reject, destroy or lose a valid tax or donation for lack of an approved capacity model. A future general withdrawal mechanism requires an explicit owner decision and a separate specification; this rule does not settle `UD-046`.

**Donations.** A donation is one-time, deliberate, donor-initiated and confirmed, never mandatory, never scheduled, never automatic, never inferred from membership and never treated as production. It transfers crowns or one supported resource through ECN-212/TR-060 into the same ARL, crediting `RECEIVED` and `AVAILABLE`, with a receipt, idempotency key and audit event. No cap, minimum, cooldown, fee or frequency is created. A donation is not an obligation and is not taxed as new production; it creates no general withdrawal authority, and the only debit path from the credited amount is the purpose-limited operational expense in `ALL-220`–`ALL-226`, which is currently unavailable because no cost schedule is approved, so the donated value remains in the ARL.

**Crowns worked examples and reconciliation (illustrative; no default rate).** (1) **0%:** gross Crowns 100,000, tax 0, national post-tax available 100,000, ARL unchanged. (2) **50%:** gross 100,000, tax `floor(100,000 × 5,000 / 10,000) = 50,000`, national post-tax available 50,000, ARL `RECEIVED` and `AVAILABLE` +50,000. (3) **100%:** tax 100,000, national post-tax available 0, ARL +100,000; later same-turn P3 stages can consume only already-owned balances, not the withheld production. (4) **Opening balance:** opening 30,000 plus gross 10,000 at 50% → tax 5,000, post-tax Crowns 5,000, maintenance 8,000, closing 27,000; only the 10,000 gross production is taxed, the 30,000 opening balance is not taxed merely because maintenance later consumes it. (5) **Insufficient post-tax funds:** opening 500 plus gross 100,000 at 100% → tax 100,000, post-tax Crowns 0; maintenance 1,000 pays the 500 available, cancels the remaining 500, marks the unpaid capacity `UNMAINTAINED`, and leaves no negative balance, debt, forced borrowing or confiscation; ARL remains 100,000. (6) **Retry and duplicate:** a retry with the same deterministic key returns the original receipt and collects nothing further; a conflicting reuse aborts as `ALF-23`; the ARL shows 50,000, not 100,000, for a 50% collection of 100,000. (7) **Reconciliation:** every collection satisfies national delta + ARL delta = 0, the ARL receipt names the same asset and turn, and `AVAILABLE = RECEIVED − RESERVED − EXPENDED` holds before and after settlement. A donation follows the same conservation identity but is recorded as a donation, never as tax.

**Multiple same-asset events (illustrative; no default rate).** (1) **Two 1-unit events at 50%:** event 1 cumulative gross 1, cumulative tax due $\lfloor 1 \times 5{,}000/10{,}000 \rfloor=0$, event tax 0; event 2 cumulative gross 2, cumulative tax due 1, event tax 1; turn tax 1, turn net 1, and the ARL receives 1 across two receipts. Independent per-event floors would collect 0. (2) **One 2-unit event at 50%:** cumulative tax due 1 and event tax 1; the same total gross gives the same turn tax. (3) **Four 1-unit events at 3,333 bp:** cumulative tax dues are 0, 0, 0 and 1, so event taxes are 0, 0, 0, 1 and the turn tax is 1; one 4-unit event gives $\lfloor 13{,}332/10{,}000 \rfloor=1$, the same total. (4) **0% and 100%:** three 1-unit events at 0% collect 0, while three 1-unit events at 100% collect 1, 1, 1 and total 3 with 0 net. (5) **Different asset rates:** Iron events at 50% and Steel events at 25% keep separate accumulators and never offset each other. (6) **Retry:** a same-key retry of an event returns its original receipt and does not advance the accumulator; a conflicting reuse is `ALF-23`. (7) **End-of-turn reconciliation:** the sum of event taxes must equal the per-turn floor $\lfloor G_a \times \text{rate\_bp}_a/10{,}000 \rfloor$ and the sum of event nets must equal $G_a-\text{tax}_a$; a mismatch is `ALF-23`, never a second collection.

**Alliance operational funding boundary.** The ARL's four receipt/accounting categories and its single permitted debit path are fully specified in [B-09 §29.7](16_alliances.md) under `D-141`, the later amendment to `D-140`. This economy rule adds only the accounting and settlement constraints: no minting, no destruction, no negative balance, conservation, source withholding, idempotency and reconciliation. No AOP purpose has an approved cost schedule, so no purpose is available and no actual expenditure can occur; received value remains in the ARL pending the required approvals. This is a specification dependency, not a spending feature. It does not decide or imply ownership of the ARL balance, custody, pool capacity, general withdrawal, general spending, distributions to members, grants, loans, aid, refunds, dividends, salaries, prizes, compensation or private debt payments; those remain Open under `UD-046`. No dual-approval rule or fixed office is created. It does not approve any default rate, bracket name, fixed office, ownership, capacity, general withdrawal or distribution rule beyond the specified operational mechanism, and no number in it is calibrated. The full rule set is `ALL-179`–`ALL-226`, with requirements `REQ-618`–`REQ-653`, formulas `F-AL-006`–`F-AL-008` and contracts `AX-27`/`AX-28`.

**ECN-214 — Prompt 10 (warfare).** *Provisional (REQ-177).* Prompt 10 owns the quantities of gasoline, ammunition, steel, aluminum and **Food** consumed by readiness, garrisons and campaigns, the order costs and the consequences of shortage. It must: reserve resources at acceptance and consume at resolution; compute the military Food ration at P3.7 rank 6(a) from the post-P3.6 unreserved stock (F-WR-036); keep the garrison ration distinct from the `OP-09` field ration; write `OBLIGATION_PAID`/`CONSUME` events with the `MILITARY_RATION` component where applicable; never mint value; and leave D-015's Operations Points model untouched. B-04 provides the demand structure and the inventory/ledger contract, not the battle numbers.

**ECN-215 — Prompt 11 (events, objectives, rankings).** *Provisional (REQ-178).* A reward must be one-time, keyed, disclosed and ledgered; it may not be a permanent yield multiplier. A world event may change a price, a population or a resource stock only through a published rule and a ledger event. A ranking may use national wealth, but must label it as an estimate and must not reveal private balances. D-027's k = 5 rule applies to any aggregate.

**ECN-216 — Prompt 12 (fair play, privacy, administration).** *Provisional (REQ-179).* Prompt 12 may read the ledger, the settlement audit and the anomaly signals. An operator correction is an `ADJUSTMENT`/`REVERSAL` with a case reference; no operator may edit a balance or delete an event. Retention follows D-026: class-S digests are hot for 30 days, then monthly summaries for 12 months; the audit spine is permanent. Access is least-privilege and logged.

**ECN-217 — Prompt 13 (interface and journeys).** *Provisional (REQ-180).* Prompt 13 owns screens, layout, accessibility and notification. It must show the six number types separately, the available/reserved/total split, the food forecast, the power supply/demand, the per-chain margin and the reason for every blocked batch. It may not redefine an accounting term; a new number needs a B-04 or register definition first.

**ECN-218 — Prompt 14 (numbers and balance).** *Provisional (REQ-181).* Prompt 14 must validate every formula, rounding rule, cap and reference price in the register; run the simulations in ECN-193; set the balance thresholds; and either confirm or retune the provisional numbers. It may change a number with a recorded decision, but it may not change a recipe's structure without a new B-04 revision. It must publish the measured results, not claim balance from internal consistency.

**ECN-219 — Prompt 15 (Bible assembly).** *Provisional (REQ-182).* Prompt 15 must incorporate B-04, the research report and the register into the Bible, resolve any duplicate formula definition in favour of the register, check both directions of every declared edge, and verify that no later part contradicts ECN-001…ECN-229. It must not silently rewrite a B-04 rule; a change is a new revision with a decision.

**ECN-220 — The subsystem declaration is complete.** *Provisional.* In B-02's fifteen-item subsystem contract, B-04 declares: entities (nation, capacity, inventory, ledger); actions (ECN-131); prerequisites (ECN-133); costs and reservation (ECN-125/126); boundary phase (P3/P4); ordering (ECN-144/149); effects on other systems (this section); failure/cancellation (ECN-137…140); player results (ECN-176…184); visibility (ECN-175); invariants (ECN-111/116/153); edge cases (the examples and §23); requirements/decisions (§23/§24); and validation examples (§20). No item is left to a later prompt without a named owner.

---


## 23. Requirements and test matrix

**ECN-221 — Requirements owned by this document.** *Provisional (REQ-098…REQ-187).* The stable requirement IDs are in [the traceability register](03_requirements_traceability.md). The mapping is: REQ-098…100 the document, units and the roster; REQ-101 Food, REQ-102 Coal, REQ-103 Oil, REQ-104 Uranium, REQ-105 Lead, REQ-106 Bauxite, REQ-107 Iron, REQ-108 Gasoline, REQ-109 Ammunition, REQ-110 Steel and REQ-111 Aluminium — one owning profile each; REQ-112…126 production, power and recipes; REQ-127…130 food and population; REQ-131…140 treasury and finance; REQ-141…144 inventory and reroll disposal; REQ-145…152 actions and settlement; REQ-153…156 ledger; REQ-157…161 reporting and balance; REQ-162…165 conventions and examples; REQ-166…171 account and fairness; REQ-172…182 cross-system contracts; REQ-183…187 the research report (REQ-183), its evidence grading (REQ-184), originality (REQ-185), the formula register (REQ-186) and this consistency check (REQ-187). No requirement is left without an owning section; every ID in REQ-098…REQ-187 appears in this document or in the register it cites.

**ECN-222 — The test matrix.** *Provisional.* Each test is a specification to be run when code exists. **None is executed in Prompt 04.**

| ID | Test | Pass condition |
|---|---|---|
| T04-A01 | Roster completeness | All 11 IDs present, classified, with a lifecycle profile |
| T04-A02 | Resource lifecycle | Every profile has source, sink, storage, trade, shortage and edge case |
| T04-A03 | Recipes | Four recipes match the register; inputs/outputs are integers; no self-loop |
| T04-A04 | Uranium and lead | Uranium has nuclear use; lead has ammunition and shielding use |
| T04-A05 | Units | No fractional resource or crown; every formula has a rounding rule |
| T04-B01 | Tax formula | Standard start yields 150; a 1 bp change changes income by the expected integer |
| T04-B02 | Positive income | Example 2 closes at 1,529 with net operating income 29 |
| T04-B03 | Operating loss | Example 3 closes at 1,247 with net operating income −282 |
| T04-B04 | Capex vs opex | Example 4 charges capex once, adds book value and adds the next-turn maintenance |
| T04-B05 | Reconciliation | Example 5's identity holds to the crown |
| T04-B06 | No negative treasury | A charge that cannot be afforded does not run; balance stays ≥ 0 |
| T04-B07 | Austerity | Example 15 cancels the obligation, creates no debt and stays at 11 |
| T04-B08 | Wealth | Example 2's wealth is 2,207; construction conserves wealth |
| T04-C01 | Food demand | 50,000 people → 50 units; ceil is used |
| T04-C02 | Hunger penalty | 20/50 unmet → 1,200 bp; tax 132 |
| T04-C03 | Hunger recovery | One good turn clears the penalty |
| T04-C04 | Overflow | A batch that does not fit does not run and destroys nothing |
| T04-C05 | Shared storage | All resources consume the same warehouse space |
| T04-D01 | Capacity | `batches_run` never exceeds capacity |
| T04-D02 | Standing policy | Runs without a player action; no reservation at submission |
| T04-D03 | Manual order reserve | Acceptance holds money, inputs, capacity and output space |
| T04-D04 | Manual order atomic | A 2-batch order with 1 batch available fails `F5` and releases all four reservations |
| T04-D05 | Power derating | Example 18 gives 60% and one batch per chain |
| T04-D06 | Fuel fail-closed | A generator without full fuel produces 0 GU and burns nothing |
| T04-D07 | Recipe arithmetic | Examples 7–10 match the register |
| T04-D08 | Cancellation | Cancel while OPEN releases everything; no fee |
| T04-E01 | Settlement order | P3.1…P3.8 run in the published order |
| T04-E02 | Duplicate settlement | Example 14 writes no second event |
| T04-E03 | Recovery | An interrupted settlement resumes from the checkpoint, same turn |
| T04-E04 | Late scheduler | A late trigger does not change the action set |
| T04-E05 | Settlement reconciliation | Balance and inventory identities hold at close |
| T04-E06 | Competing actions | Earlier B1 order runs; later fails `F5`; no double spend |
| T04-F01 | Append-only | No edited or deleted event exists after a correction |
| T04-F02 | Event uniqueness | A duplicate `event_key` is a no-op; a conflicting one aborts |
| T04-F03 | Reversal | A correction links to the original and both are visible |
| T04-F04 | Report reconciliation | Closing = opening + ledger deltas |
| T04-F05 | Visibility | A player cannot read another nation's private events |
| T04-G01 | Starter once | A retry of `NATION_INIT` grants nothing; a reroll grants once to the new ID |
| T04-G02 | No reroll transfer | Example 17 destroys every asset; replacement wealth is 2,100 |
| T04-G03 | Pending disposition | Offers withdrawn, orders cancelled, reservations released, history retained |
| T04-G04 | Sanctions survive | A banned account cannot create; a preservation hold blocks |
| T04-G05 | Shared-network block | A restricted pair's trade moves nothing |
| T04-G06 | History retention | The old ledger remains after retirement |
| T04-H01 | Dashboard | Total/available/reserved, income, expenses, inventory and wealth are separately visible |
| T04-H02 | Forecast label | A forecast is labelled and not shown as a balance |
| T04-H03 | Blocked explanation | Every blocked batch names money/input/power/space |
| T04-H04 | Margin display | Per-chain cost, revenue and margin are shown |
| T04-I01 | Balance targets | The seven targets are stated and testable |
| T04-I02 | Dominance test | The margin/capital table is checked; a dominant chain is flagged |
| T04-I03 | Money creation | A 30-turn simulation checks crown growth vs output |
| T04-J01 | Research report | Exists, with sources, dates, labels and a comparison matrix |
| T04-J02 | Formula register | Every formula has ID, expression, units, bounds, rounding, timing, example and edge cases |
| T04-J03 | Consistency | Outline, requirements, decisions, UD and continuity agree |
| T04-J04 | Validators | The repository validators run and their actual results are recorded |

**ECN-223 — Test status.** *Provisional.* **0 of 54 tests executed.** They are design specifications, not results. A later stage that implements the economy must run them and record the actual output; a document review cannot mark a runtime test as passed.

**ECN-224 — Coverage summary.** *Provisional.* The matrix covers the required resource completeness, formula consistency, settlement/accounting integrity, account-policy consistency and cross-system consistency checks. It does not cover UI accessibility (Prompt 13), market matching (Prompt 07), warfare consumption (Prompt 10) or population politics (Prompt 06); those are named in §22.

---

## 24. Decision register — Prompt 04

**ECN-225 — Decisions recorded.** *Provisional.* The following project decisions are recorded in [DECISIONS.md](../DECISIONS.md) as D-043…D-065 and summarised in [the Stage 2 design register](04_approved_and_provisional_decisions.md) as DD-061…DD-080. This table is the cross-reference; the log is authoritative.

| ID | Decision | Status |
|---|---|---|
| D-043 | Economy philosophy: production first, closed money loop, structural scarcity, absence tolerance | Confirmed (design) |
| D-044 | 11-resource roster and classification; MAT classes become a role taxonomy only | Confirmed (design); roster is an approved constraint |
| D-045 | Integer units, integer crowns, no fractional resources | Confirmed (design) |
| D-046 | Adopted recipes: 10 oil→8 gasoline; 10 iron+6 coal→8 steel; 12 bauxite→8 aluminum; 8 lead+4 coal→10 ammunition | Confirmed (design); numbers Provisional |
| D-047 | Uranium fuels nuclear power; lead also serves as nuclear shielding | Confirmed (design) |
| D-048 | Grid units, three generators, surplus discarded, pro-rata derating | Confirmed (design); numbers Provisional |
| D-049 | Currency named the crown; one pool; no second currency | Confirmed (design) |
| D-050 | No debt, no interest, treasury floors at zero; austerity cancels unpaid obligations | Confirmed (design) |
| D-051 | Capex at P4, book value includes materials, maintenance is a fixed operating expense | Confirmed (design) |
| D-052 | One shared warehouse, no decay, overflow blocks the batch | Confirmed (design); starting size Provisional |
| D-053 | Standing production policy plus optional manual orders; manual orders reserve capacity | Confirmed (design) |
| D-054 | P3 order: tax → maintenance → extraction → power → processing → food → obligations → close | Confirmed (design) |
| D-055 | Append-only ledger, reversal events, reconciliation | Confirmed (design) |
| D-056 | Six number types and provenance in reporting | Confirmed (design) |
| D-057 | Balance targets and simulation metrics | Confirmed (design); thresholds Provisional |
| D-058 | Reference prices are book values, not market prices | Confirmed (design); numbers Provisional |
| D-059 | Reroll destroys all economic assets; replacement gets the standard bundle only | Confirmed (design) |
| D-060 | Cross-system contracts for Prompts 05–15 | Confirmed (design) |
| D-061 | Tax formula and stability interface | Confirmed (design); bounds Prompt 06 |
| D-062 | National wealth = treasury + inventory book value + fixed-asset book value | Confirmed (design) |
| D-063 | Standard starting bundle: 1,500 crowns, 310 units, stated capacity | Confirmed (design); numbers Provisional |
| D-064 | Integer arithmetic with one published rounding rule per formula | Confirmed (design) |
| D-065 | Food contract: 1 unit/1,000 people, 0–30% next-turn tax penalty, Prompt 06 owns population | Confirmed (design) |

---

## 25. Validation, acceptance and next action

**ECN-226 — Acceptance checklist.** *Provisional.*

| Criterion | Status | Evidence |
|---|---|---|
| Research report exists with sources and evidence grades | **Met (document)** | [Research report](research/04_politics_and_war_economy_research.md) |
| The 11 resources are defined and classified | **Met (design)** | §6, §7 |
| Every resource has a complete lifecycle | **Met (design)** | §7.1–7.11 |
| Every manufactured good has a recipe | **Met (design)** | §10 |
| Uranium and lead have explicit purposes | **Met (design)** | ECN-073/074 |
| Treasury, income, opex, capex, cash flow and wealth are distinct | **Met (design)** | §12 |
| Debt/insolvency is decided | **Met (design)** | ECN-103…107 |
| Inventory, storage, reservation and overflow are defined | **Met (design)** | §13 |
| Settlement has an authoritative order and recovery | **Met (design)** | §15 |
| Actions have explicit states and failure behaviour | **Met (design)** | §14 |
| An append-only ledger is specified | **Met (design)** | §16 |
| Reports reconcile with the ledger | **Met (design)** | ECN-116/173 |
| Specialization and strategy are viable | **Met (design)**; unmeasured | §18 |
| Food has a precise contract with Prompt 06 | **Met (design)** | ECN-088 |
| Reroll and starter protections are defined | **Met (design)** | §21 |
| At least 17 worked cases are covered | **Met (document)** | §20, 20 examples |
| Formula register is complete | **Met (document)** | [Register](10_economic_formula_and_balance_register.md) |
| Validators executed and recorded | **See ECN-227** | Actual run below |
| No implementation, migration or deployment | **Met** | Scope confirmation |

**ECN-227 — Validation record.** *Provisional.*

All five checks were run from `docs/` on **2026-10-24**, after the last change to any register or continuity file. Exact results:

| Command | Actual result |
|---|---|
| `python qa_backups/09_validate.py` | **338/338 checks passed** — final line `ALL CHECKS PASSED` |
| `python qa_backups/validate_final.py` | **`VALIDATION: ALL CHECKS PASSED`** — includes the B-04 block: 25 sections, the 11-resource roster, all four recipes stated in both the rulebook and the register, 20 worked examples, complete T04-A…T04-J ID coverage, every REQ-098…REQ-187 cited, and every cited `F-EC-` present in the register |
| `python qa_backups/test_decision_registers.py` | **12 tests, OK** — decision range D-001…D-065, the status block, the UD-status reconciliation and the next action then current ("Prompt 05 is next"; those assertions have since advanced to Prompt 06) |
| `python qa_backups/test_next_action.py` | **15 tests, OK** — no stale next action; the Bible outline, the progress table and the three continuity files agreed that Prompt 04 was complete and Prompt 05 was next on that date (they now assert Prompt 06) |
| `python qa_backups/verify_economy_numbers.py` | **146/146 arithmetic checks passed** — an independent recomputation from the register's constants: the starting bundle (310 units, 600 book, 2,100 wealth, 1,690 free space), Example 2, every Example 3 line, Examples 4–20, and the register's own index and worked examples. It also compares this document's Example 5 with the register's index row, checks that the fee stays labelled hypothetical, and fails if any superseded bundle total, Example 3 total, book value, fee line or version header reappears |

Manual checks run with them:

1. **Arithmetic.** All 20 examples were recomputed from the register's constants (`qa_backups/verify_economy_numbers.py`, added in the correction pass, recomputes the bundle totals and every Example 1–20 figure and fails if the document disagrees). Two correction passes ran on 2026-10-24. The first restated Example 8's break-even thresholds and aligned Examples 7/8 and the register's gasoline sensitivity to the published margin definitions — base margin per F-EC-036 *excludes* power, fully loaded per F-EC-037 *includes* it at ≈3.0 crowns/GU; "+1 per batch" became **+8 per batch** (one crown × eight units). The second, after an independent review, fixed the **standard bundle total (350 → 310)**, **Example 3 in full** (opening 1,360 → 1,560; uranium/bauxite/lead outputs read from costs instead of yields; ammunition run at two batches with capacity one; closing stock 1,673, book value 5,128, wealth 6,375, change **+146**), the free-space figures in ECN-121 and Example 2, and **Example 5's unadopted 2-crown market fee** (closing 1,426 → **1,428**). **No coefficient, recipe or formula changed in either pass.**
2. **Roster.** Exactly 11 resources — 7 raw (Food, Coal, Oil, Uranium, Lead, Bauxite, Iron) and 4 manufactured (Gasoline, Ammunition, Steel, Aluminum) — each with a §7 lifecycle profile.
3. **Requirements.** 187 rows, REQ-001…REQ-187 with no gap; 14 approved / 166 provisional / 5 open / 2 deferred, which is what `validate_final.py` expects.
4. **Decisions.** 65 rows, D-001…D-065; design register DD-001…DD-080; unresolved register unchanged at 17 Resolved / 8 Deferred / 5 Open.
5. **Not run.** No runtime, database, scheduler, market or simulation check. No such code exists, and no test in §23 has been executed (**0 of 54**).

**ECN-228 — Limitations.** *Provisional.* (1) The numbers are provisional and unvalidated by simulation; Prompt 14 must retune or confirm them. (2) No code, database, scheduler or market exists; no runtime test has been run. (3) The food/population interaction is a contract; Prompt 06 may add stability effects that change the player experience. (4) The power derating is deliberately conservative and may need a balance pass. (5) Construction costs and warehouse expansion are Prompt 05's; the examples use placeholders. (6) The market price, fee and fair-value band are Prompt 07's. (7) The military consumption rates are Prompt 10's. (8) The reference prices are accounting estimates, not observed prices. (9) The research is documentary and P&W may have changed. (10) The 54 test specifications are unexecuted. (11) The correction pass corrected arithmetic only; it did not re-derive the provisional coefficients, so an error in a coefficient itself would survive a consistent recalculation.

**ECN-229 — Next action.** *Provisional.* If the acceptance criteria are met, the next scheduled task is **Stage 2, Prompt 05 — Cities, Infrastructure, Production, and Research**. Prompt 05 must use the B-04 recipes, coefficients, reservation model and ledger contract, and must register every building and modifier in the formula register. It must not change a B-04 recipe without a new decision. Prompt 04 is **not** implemented, deployed or runtime-tested.

**ECN-230 — Revision history.** v1.0 (2026-10-24): first issue for Prompt 04. No earlier version exists. The research report is v1.0. **v1.1 (2026-10-24):** numerical correction pass after an independent review — the starting bundle is 310 units, Example 3 is rebuilt from the register's per-batch yields, Example 5 no longer charges an unadopted market fee, and the register's totals and index were corrected; the research report is unchanged at v1.0, the register is v1.1. **No rule, recipe or coefficient changed.** A same-day micro-correction completed v1.1: this document's header now reads v1.1, no figure in the rulebook changed, and the arithmetic checker was extended to compare Example 5 across both documents. **v1.2 (2026-10-25):** the manual-capacity contract is clarified after an independent review — ECN-053 states that a reservation occupies a slot inside capacity, ECN-060 defines `planned_batches = M + A ≤ C`, and Example 12 proves the difference numerically; no rule or coefficient changed. **v1.3 (2026-10-28):** **ECN-147a** publishes the maintenance allocation order and the whole-obligation rule, closing the gap that made Example 41's turn-14 result depend on a test assumption; Example 15's maintenance is corrected from 3 to **6** (`3 + 2 + 1` for its three extraction chains), so its closing treasury is **8** rather than 11. No expense rate, formula or reference price changed. **v1.4 (2026-11-01):** Prompt 09B-I records the owner-authorized alliance taxation and voluntary-donation capability under `D-140` in **ECN-213a**; no national rule changed. **v1.5 (2026-11-01):** Prompt 09B-J clarifies `ECN-213a` to automatic per-turn collection from current-turn production only, with player-created brackets, per-asset rates in basis points, role permissions, a frozen pre-P3 snapshot, no per-policy owner consent and a credit-only Alliance Receiving Ledger; no national tax, transfer, reservation, ledger, conservation, fee or production-ordering rule changed. **v1.6 (2026-11-02):** Prompt 09B-K fixes the seven-step `ECN-213a` settlement sequence, the post-tax same-turn consumption rule, the stockpile/input no-re-tax rule, the once-per-output rule for transformed production, the provisional `UD-040` multiple-membership 0% fallback and the `ALF-21`/`ALF-23`/`ALF-24` alignment; no national rule or coefficient changed. **v1.7 (2026-11-02):** Prompt 09B-L replaces the "credit-only" ARL shorthand with four accounting categories and a single purpose-limited operational debit to a registered platform cost sink, makes bracket assignment per Alliance, and adds the Crowns 0%/50%/100%, opening-balance, maintenance, insufficient-funds, retry and reconciliation examples; no national tax, transfer, reservation, ledger, conservation, fee, production-ordering or coefficient rule changed. **v1.8 (2026-11-02):** Prompt 09B-M records the operational-funding boundary under `D-141`, a later amendment to `D-140`, and states that no AOP purpose has an approved cost schedule or is currently spendable, so tax and donation value remains in the ARL; the four categories are receipt/accounting records, the AOP labels, permission name and settlement mechanics are project design choices, and general treasury authority remains Open under `UD-046`. It also specifies cumulative fractional accrual for multiple same-asset production events, so each event collects the increment of the floored cumulative liability and the event taxes reconcile to the per-turn floor with no independent per-event floor. No national tax, transfer, reservation, ledger, conservation, fee, production-ordering or coefficient rule changed.

<!-- END -->
