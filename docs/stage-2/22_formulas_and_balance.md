# B-14 — Formulas, numerical rules and balance

**Version:** 1.5 (Prompt 14B B-04 economy reconciliation) · **Created:** 2026-11-13 · **Last corrected:** 2026-11-17 · **Stage 2, Prompt 14, Subphase 14B**
**Status:** **PROMPT 14A IS OWNER ACCEPTED (17 November 2026). PROMPT 14B — B-04 economy, resources, income and treasury — IS COMPLETE AT THE DOCUMENTATION, NUMERICAL-ANALYSIS AND DOCUMENT-VALIDATION LEVEL.** No B-04 value was retuned; no formula was added or renumbered; the 295/393/20 counts are preserved. The standard start is not balance-accepted and no runtime exists. Subphases 14C–14K are **NOT AUTHORIZED and NOT STARTED**. No numerical value is approved, calibrated, simulated or implemented by this document.**

> **Scope statement.** B-14 is the numerical architecture of Nation Supremacy: the index, reconciliation and decision-authority layer over the nine authoritative formula registers. **It is not a competing formula register.** Every expression, constant and worked example remains defined by its owning register (B-04…B-12); B-14 links to those definitions, accounts for every active identifier and records who may decide each unresolved value. Prompt 14A established this foundation (owner accepted 2026-11-17). Prompt 14B reconciled the B-04 economy at the documentation and numerical-analysis level (2026-11-17) without retuning a value; the remaining economy, production, research, trade, diplomacy, Alliance, warfare and progression calibration belong to Prompt 14C–14K and require separate owner authorization.

**Governing policy:** [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (D-014).
**Parent instruction:** [Prompt 14A archive](../prompts/prompt_14A_formula_inventory_numerical_architecture_and_baseline_reconciliation.md).

---

## 1. Purpose and scope

### 1.1 What B-14 owns

| B-14 owns | B-14 does **not** own |
|---|---|
| The master index of active and retired formula identifiers | Any formula expression or definition (owned by B-04…B-12) |
| The numerical parameter ownership map | The numerical value of a provisional parameter (owned by the named decision authority) |
| The four-label numerical status vocabulary | A balance target, a tuned value or a playtest result |
| The reconciliation of the 20 B-03 carry-in parameters | The B-03 rule that consumes a parameter |
| The units / precision / rounding convention matrix | A register's own rounding rule (owned by that register) |
| The timing dependency map against B-02's P0–P7 | The phase order itself (owned by B-02) |
| The numerical QA baseline and coverage gaps | Implementation, simulation or gameplay validation |

### 1.2 In scope for 14A

- B-02 (core gameplay loop and turn system) and B-03 (account onboarding, nation creation and progression) as numerical authorities.
- All nine formula registers: B-04, B-05, B-06, B-07, B-08, B-09, B-10, B-11 and B-12.
- The B-14 canonical filename reconciliation required by D-198.
- Existing numerical QA and regression coverage.
- Continuity, roadmap, outline, decision and prompt-archive reconciliation genuinely affected by 14A.

### 1.3 Out of scope for 14A

Formula redesign; changing any starting resource, treasury value, construction cost, production ratio, research cost, tax rate, market price, fee, trade limit, diplomatic cost, Alliance permission, warfare value, Operations Points model, combat coefficient, progression reward, fair-play sanction or anti-abuse threshold; implementing any mechanic; building a playable simulation; modifying frontend, backend, database, SQL, API, migrations, infrastructure, security or deployment; performing Git operations; starting 14B–14K.

### 1.4 Section status legend

Each section states one of: **COMPLETE** (14A work finished and verified), **PROVISIONAL** (content exists but depends on evidence owned elsewhere), **BLOCKED** (cannot complete without an owner-reserved or external decision), **RESERVED** (deliberately left to a later 14 subphase).

---

## 2. Governing constraints and source authority — COMPLETE

### 2.1 Fixed constraints preserved

| Constraint | Authority | Numerical consequence |
|---|---|---|
| Two-hour UTC cadence, 12 turns/day | D-008 / B-02 §10 | 84 turns per 7 days; 360 turns per 30 days; 168 turns per 14 days |
| Mapless symbolic world | D-001 / B-02 §7 | No distance, terrain or geography parameter exists; supply is abstract |
| One account, one active nation | D-032 | No per-account production multiplier; protection is account-scoped |
| Browser delivery, Cloudflare Pages + Supabase | D-008 / D-009 / D-010 | Hosting, deployment, scheduler and platform direction only; no arithmetic convention is derived from these entries |
| Integer arithmetic and whole-unit precision | D-045 / D-064 | Whole integer quantities; integer basis-point percentages; every division states floor or ceil; no binary floating point; no fractional resource or crown balance |
| Free-first ₹0 target | Owner constraint | No paid numerical service; no licensed data feed |
| Stage 1 → Stage 2 → Stage 3 sequencing | D-012 | No numerical value implies implementation |

### 2.2 Source authority order

1. **Fixed constraints** (Category A) above.
2. **Owner decisions** in [DECISIONS.md](../DECISIONS.md) that approve a value explicitly.
3. **The owning formula register** for every expression, constant and formula-level classification.
4. **B-02** for turn timing, phase order, deterministic ordering and inactivity.
5. **B-03** for the 20 carry-in parameters and their owners.
6. **This document** for the index, reconciliation, status vocabulary and ownership map only.

A conflict between sources is recorded in §13 and is never resolved by silently choosing one. In particular, a number is not owner-approved because it appears in a register, because a Category B decision records the rule as Confirmed, or because a validator can recompute it.

### 2.3 Checked source set

[B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [B-03](09_account_onboarding_nation_creation_and_progression.md) · [B-04 register](10_economic_formula_and_balance_register.md) · [B-05 register](11_city_infrastructure_production_and_research_formula_register.md) · [B-06 register](12_population_and_domestic_politics_formula_register.md) · [B-07 register](13_trade_and_markets_formula_register.md) · [B-08 register](15_diplomacy_formula_register.md) · [B-09 register](16_alliances_formula_register.md) · [B-10 register](17_warfare_formula_register.md) · [B-11 register](18_world_events_objectives_rankings_progression_formula_register.md) · [B-12 register](20_fair_play_and_player_protection_formula_register.md) · [DECISIONS.md](../DECISIONS.md) · [UD register](05_unresolved_design_decisions.md) · [AI_CONTEXT.md](../AI_CONTEXT.md).

---

## 3. Formula-register architecture — COMPLETE

| System | Canonical register | Role | Active formulas | Register rules excluded | Retired |
|---|---|---|---:|---:|---:|
| B-04 | [`10_economic_formula_and_balance_register.md`](10_economic_formula_and_balance_register.md) | Economy, resources, treasury, production, maintenance | 47 | 8 | 0 |
| B-05 | [`11_city_infrastructure_production_and_research_formula_register.md`](11_city_infrastructure_production_and_research_formula_register.md) | Cities, infrastructure, construction, research | 41 | 5 | 0 |
| B-06 | [`12_population_and_domestic_politics_formula_register.md`](12_population_and_domestic_politics_formula_register.md) | Population, approval, stability, legitimacy, elections | 44 | 6 | 0 |
| B-07 | [`13_trade_and_markets_formula_register.md`](13_trade_and_markets_formula_register.md) | Directed trade, Global Trade, fair value, fees | 39 | 10 (+2 duplicate headings) | 0 |
| B-08 | [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md) | Proposals, postures, agreements, embargoes, aid | 12 | 0 | 0 |
| B-09 | [`16_alliances_formula_register.md`](16_alliances_formula_register.md) | Alliance treasury, tax, donations, operational funding | 8 | 0 | 0 |
| B-10 | [`17_warfare_formula_register.md`](17_warfare_formula_register.md) | Operations Points, readiness, combat, losses, settlement | 39 | 0 | 0 |
| B-11 | [`18_world_events_objectives_rankings_progression_formula_register.md`](18_world_events_objectives_rankings_progression_formula_register.md) | Events, objectives, rankings, progression, rewards | 49 | 8 | 1 |
| B-12 | [`20_fair_play_and_player_protection_formula_register.md`](20_fair_play_and_player_protection_formula_register.md) | Sanctions, appeals, corrections, audit integrity | 16 | 0 | 0 |
| **Total** | | | **295** | **39 entries (37 unique)** | **1** |

### 3.1 Counting convention

An **active formula** is a numbered `F-<system>-001`-or-higher identifier carrying a computational, analytical or governance entry. The `F-<system>-000` series carries register conventions and is excluded. `F-WEP-048` is retired and excluded. Lettered identifiers that define a separable computation (`F-EC-002a`) count; lettered sub-parts inside one heading (`F-DP-006a`, `F-DP-006b`) do not.

### 3.2 What the registers are — and are not

Every register declares that its numbers are provisional. B-04, B-05 and B-06 state that their constant tables are a versioned provisional calibration. B-07 states the same and defers two fees to gate G-5. B-09 states that **no formula is a rule**; every value is a candidate awaiting owner decisions. B-10 states that every numeric constant is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED** unless its field 17 says Structural. B-11 separates 43 active structural formulas (20 with Prompt 14 parameters, 23 without) from 6 provisional formulas. B-12 registers 14 parameters, none calibrated.

**No register is a balance authority and no register approves its own numbers.**

---

## 4. Master formula inventory — COMPLETE

The complete, individually traceable inventory of all **295 active formulas** is:

- [`22_formula_master_inventory.md`](22_formula_master_inventory.md) — one record per active identifier, with the fields required by Prompt 14A §4.1, the retired-formula register, the excluded register-rule index and the metadata-gap findings.

Summary of the inventory:

| Item | Count | Evidence |
|---|---:|---|
| Active formula identifiers | **295** | Reconciled per register in the companion §2 |
| Unique active identifiers | **295** | No duplicate active ID |
| Retired identifiers | **1** (`F-WEP-048`) | B-11 register, retained for traceability |
| Register-rule entries excluded | **39 entries (37 unique identifiers)** | Inventory §5 |
| Duplicate register-rule identifiers | **2** (`F-TM-000e`, `F-TM-000f`) | Source-register defect, recorded in §13 |
| Unresolved source references | **0** | Every record resolves to a real register line |
| Records with an explicit metadata-gap marker | **Recorded** | Inventory §7 |

**Expected-versus-actual reconciliation:** all nine registers match the expected baseline exactly — 47, 41, 44, 39, 12, 8, 39, 49, 16. No identifier was added, removed, renumbered or recreated to force that result.

---

## 5. Numerical parameter master inventory — COMPLETE FOR INVENTORY, PROVISIONAL FOR VALUES

The ownership map is:

- [`22_numerical_parameter_inventory.md`](22_numerical_parameter_inventory.md) — every constant-table row in B-04/B-05/B-06/B-07, every formula-level provisional value set in B-08/B-09/B-10/B-11, all 14 B-12 registered parameters, all 20 B-03 carry-ins and the B-02 timing constants.

| Layer | Records | Authority |
|---|---:|---|
| B-02 timing constants | 7 | Fixed cadence / B-02 |
| B-03 carry-in parameters | 20 | B-03 named owners |
| B-04 constant-table parameters | 49 rows (multi-value vectors) | Prompt 14 calibration; B-04 structure |
| B-05 constant-table parameters | 73 rows | Prompt 14 calibration; B-05 structure |
| B-06 constant-table parameters | 96 rows | Prompt 14 calibration; B-06 structure |
| B-07 constant-table parameters | 26 | Prompt 14; G-5 for fees |
| B-08 formula-level values | 12 | B-08 rule owner |
| B-09 formula-level values | 8 | Owner (`UD-040`, `UD-043`, `UD-044`, `UD-046`) |
| B-10 formula-level values | 39 | Prompt 14 calibration |
| B-11 formula-level values | 49 | Prompt 14 / B-11 structure |
| B-12 registered parameters | 14 | Owner / Stage 5 / Prompt 14 per row |
| **Total parameter records** | **393** | Mixed — see the ownership map |

**Metadata provenance.** Formula-row units are derived from the source fields (B-08/B-09 `Variables` + `Range`, B-10 `Output`, B-11 `Units` + `Output range`); records with no source unit carry `NOT SPECIFIED IN SOURCE`. The B-03 evidence-class column is a derived analysis label because B-03 §21.2 states no classification. The B-12 evidence column mirrors the source `Review trigger` field. Values, owners and statuses are unchanged by these metadata corrections. `FP-P07` is source-validated to `operations per turn` by `F-FP-009`. Constant-table precision/rounding is validated against the register-level integer/basis-point convention (B-04 `F-EC-000b`, B-05 `F-CI-000c`, B-06 `F-PD-000b`, B-07 `F-TM-000c`), and owner-reserved flags are source-validated for every applicable record.

A row that carries a vector (for example an extraction coefficient row with `Y`, `V`, `M` and `P_ref`) states each value with its own unit inside the value cell. No parameter identifier was invented where the source has none.

---

## 6. B-03 carry-in parameter reconciliation — COMPLETE

All **20** parameters in [B-03 §21.2](09_account_onboarding_nation_creation_and_progression.md) are reproduced exactly in the parameter map §4. The reconciliation:

| # | Parameter | B-03 provisional value | Numeric owner / validator (B-03 exact) | Prompt 14 role |
|---:|---|---|---|---|
| 1 | Network observation window `W_obs` | 24 hours | Prompt 12; Prompt 14 | Validate |
| 2 | Observation life `R_obs` | 180 days | Prompt 12 | None |
| 3 | Large-network threshold `L_large` | >25 accounts / 24h | Prompt 12 | None |
| 4 | Restricted-attempt escalation | Second observation ≥6h apart within 7 days | Prompt 12 | None |
| 5 | Review service target | 7 days, not a guarantee | Prompt 12 | None |
| 6 | Clearance watch | 90 days | Prompt 12 | None |
| 7 | Re-review interval after `MAINTAINED` | 30 days | Prompt 12 | None |
| 8 | Network digest retention | 180 days after last seen | Prompt 12 | None |
| 9 | Pair-record retention | Active + 12 months | Prompt 12 | None (legal `UD-017`) |
| 10 | Newcomer protection `P_prot` | 7 days / 84 turns | Prompt 10; Prompt 14 | Validate |
| 11 | Fresh-nation transfer window | 30 days / 360 turns | Prompt 07; Prompt 14 | Validate |
| 12 | Fair-value band | Unspecified here (B-07 / D-114 fix it at 3,000 bp) | Prompt 07 | None |
| 13 | Display-name change cooldown | 7 days | Prompt 13; Prompt 14 | Validate |
| 14 | Short-name change cooldown | 30 days | Prompt 13; Prompt 14 | Validate |
| 15 | Released-name hold | 30 days | Prompt 12 | None |
| 16 | Reroll review flag | 3 completed rerolls / 30 days | Prompt 12 | Value support (`UD-031`) |
| 17 | Reroll request rate limit | 1 per 60 seconds | Stage 6 | None |
| 18 | Account closure cooling | 7 days | Prompt 12 | None |
| 19 | Unverified-account cleanup | 30 days | Stage 6 | None |
| 20 | Session absolute lifetime | 30 days | Stage 6 | None |

**Ownership conclusion.** Prompt 14 does **not** own all 20. It validates or supports seven (1, 10, 11, 13, 14, 16 and the numeric side of `UD-031`). Prompt 12 owns the shared-network, review, retention and reroll-review rules; Prompt 10 owns newcomer protection; Prompt 07 owns the transfer window and fair-value band; Prompt 13 owns the naming cooldowns; Stage 6 owns the technical rate limit, cleanup and session lifetime.

**Status conclusion.** All 20 remain `PROVISIONAL VALUE` (or `UNSPECIFIED` for the B-03 fair-value row). None is promoted to `OWNER-APPROVED VALUE`. `UD-017`, `UD-031`, `UD-032` and `UD-033` keep their actual current dispositions: `UD-017` Open (owner/legal), `UD-031` Deferred to Prompt 12, `UD-032` Resolved (Prompt 10 Option A) and `UD-033` Resolved (D-128).

---

## 7. Numerical approval and status classifications — COMPLETE

### 7.1 The four statuses

| Status | Definition | Used when | Not used when |
|---|---|---|---|
| **OWNER-APPROVED VALUE** | An explicit owner decision approves this number | A traceable owner decision names the value | The rule is merely Confirmed under Category B; the number is provisional; a validator can recompute it |
| **PROVISIONAL VALUE** | A working value exists but is not confirmed by adequate evidence | The register states provisional, uncalibrated or Prompt 14 calibration required | The value is owner-reserved and undefined; the entry is structural |
| **DESIGN PROPOSAL** | A value or arithmetic model proposed but not adopted | All eight B-09 candidate formulas; future proposals | The source has adopted the rule (then provisional or approved applies) |
| **NEEDS PLAYTESTING** | Only actual player behaviour or sustained operation can settle the value | Parameters whose evidence class is playtest, behavioural or load measurement | Offline arithmetic can settle the value |

`UNSPECIFIED` marks an absent or owner-reserved value and is an absence marker, **not** a fifth status. `RETIRED` is a lifecycle state used only in the retired register.

### 7.2 Safeguards applied in 14A

1. A Category B decision recorded **Confirmed** does not make its number owner-approved. D-063 (starting bundle), D-114 (3,000 bp band) and D-027 (`k = 5`) are confirmed rules whose numbers remain provisional.
2. A Category C decision stays provisional until its named evidence supports a change.
3. An owner-reserved decision cannot be made acceptable by assigning it a provisional value. Six B-12 parameters and eight Alliance formulas remain `UNSPECIFIED`/`DESIGN PROPOSAL` behind open owner decisions.
4. A formula passing an arithmetic validator is **not** a calibrated value. The distinction between specified, arithmetic-checked, validator-passed, simulated, runtime-tested and playtested is preserved in §12.

### 7.3 Current distribution

| Status | Count | Where |
|---|---:|---|
| OWNER-APPROVED VALUE | 0 formula values | No formula value in the nine registers carries explicit owner approval. The B-02 cadence and phase model are owner-approved **rules**, not formula values. |
| PROVISIONAL VALUE | 231 active formula records + most constant rows | B-04…B-12 |
| DESIGN PROPOSAL | 8 | All B-09 formulas |
| NEEDS PLAYTESTING | 1 registered parameter (`FP-P07`); plus named evidence classes for playtest-dependent parameters | B-12; §11 |
| UNSPECIFIED | 56 active formula records + owner-reserved parameters | Structural formulas, governance entries and owner-reserved values |

---

## 8. Units, precision and rounding conventions — COMPLETE (INVENTORY), WITH RECORDED GAPS

### 8.1 Units in use

| Unit | Meaning | Registers |
|---|---|---|
| Crowns | Integer currency | B-04, B-05, B-07, B-09, B-10, B-12 |
| Resource units | Integer raw or manufactured goods | B-04, B-05, B-07 |
| Batches | Integer production batch | B-04, B-05 |
| People | Integer population | B-06 |
| Basis points (bp) | Integer; 10,000 bp = 100% | B-04, B-05, B-06, B-07, B-09, B-10, B-11 |
| Turns | Integer two-hour boundaries | Every register |
| Hours / days | Conversions of turns at 2 h / 12 per day | B-03, B-05, B-06, B-10, B-12 |
| Capacity points (DC) | Integer development capacity | B-05 |
| Research points (RP) | Integer research | B-05 |
| Generation units (GU) | Integer power | B-04, B-05 |
| Operation Points (OP) | Integer military action points | B-10 |
| Members / cities / listings / chains | Integer counts | B-05, B-07, B-09 |
| Probabilities / weights | Integer bp or ordinal points | B-06, B-11, B-12 |

### 8.2 Precision and rounding by register

| Register | Precision | Rounding rule | Fractional accumulation |
|---|---|---|---|
| B-04 | Integer; bp percentages | Per formula: floor, ceil or round_half_up (F-EC-000b) | No binary floating point; no fractional carry stated |
| B-05 | Integer; bp discounts | Per formula floor/ceil; discount `ceil(base × (10,000 − bp) / 10,000)` | No |
| B-06 | Integer; bp rates and stability | `floor` unless the entry says `ceil` | No |
| B-07 | Integer | Each division states floor or ceil; default floor (F-TM-000c) | No |
| B-08 | Integer counts and turns | No fractional arithmetic stated | No |
| B-09 | Integer; bp rates | **Cumulative** floor then subtract collected, per asset and per turn — never floor each event independently (F-AL-006) | Yes — cumulative fractional accrual is explicit |
| B-10 | Integer | Exact integer arithmetic; per-formula rounding (field 7) | No |
| B-11 | Integer / bp | Per formula field 11 | No |
| B-12 | Integer ordinal points / turn counts | Per formula field 8 | No |

### 8.3 Conservation identities that must not be altered

| Identity | Register | Statement |
|---|---|---|
| Treasury conservation | B-04 / B-12 | No formula mints a crown; every transfer has a debit and a credit |
| Resource conservation | B-04 | Production adds only what a recipe states; consumption removes only its input |
| Market settlement | B-07 | Both sides are reserved at acceptance and settle atomically; the conservation identity `F-TM-037` and settlement completeness `F-TM-039` must hold |
| Alliance tax | B-09 | `0 ≤ Tax ≤ gross`; net = gross − tax; the ARL receives exactly the tax; gross is never delayed, reduced or destroyed |
| Alliance donation | B-09 | Donation conservation and idempotency `F-AL-007`; no capacity is invented |
| Military expenditure | B-10 | Resource supply bundles are consumed at P5; losses are bounded and settled atomically, with no debt |
| Fair-play correction | B-12 | `F-FP-014` correction conservation identity; corrections may not create value |
| Reward conservation | B-11 | `F-WEP-049` conservation check; rewards come from an authorised pool or system grant |

### 8.4 Recorded unit/rounding gaps

1. **B-05:** six active formulas (`F-CI-009`, `F-CI-022`, `F-CI-024`, `F-CI-027`, `F-CI-028`, `F-CI-029`) do not state their own rounding rule. The register-level integer convention exists, but the per-formula field is absent.
2. **B-07:** many formulas omit a per-formula rounding and timing field; F-TM-000c/000e supply register-level defaults. `F-TM-000e` cites a non-existent `§4.20`.
3. **B-12:** no formula carries a P0–P7 position. Sanction timing is stated only at rule level.
4. **B-08:** outputs are not separately stated for all 12 formulas; the definition and range supply the result.
5. **B-09:** dependencies are not separately stated for its formulas; source rules and requirements supply traceability.

None of these gaps is repaired in 14A. Each is visible in the inventory's Outstanding-issue column.

---

## 9. Turn timing and numerical execution order — COMPLETE (RECONCILED AGAINST B-02)

### 9.1 Two-hour UTC cadence preserved

`slot(t) = floor(unix_utc_seconds(t) / 7200)`; turn N covers `[7200·N, 7200·(N+1))`; the boundary instant belongs to the later turn; there is no grace period (B-02 TR-024, TR-029, TR-030). Turn identity is the absolute slot; display number is relative to the immutable world epoch (TR-025, TR-026).

| Conversion | Check | Result |
|---|---|---|
| 2 h per turn | B-02 §10 | Preserved |
| 12 turns per day | 24 / 2 | Preserved |
| 84 turns per 7 days | 12 × 7 | Preserved |
| 360 turns per 30 days | 12 × 30 | Preserved |
| 168 turns per 14 days | 12 × 14 | Preserved (D-028 dormancy) |

No numerical document uses a conflicting conversion.

### 9.2 P0–P7 execution order

| Phase | Name | Numerical content | Authority |
|---|---|---|---|
| **P0** | Prepare | No OP mutation, no world-state mutation | B-02 TR-040 |
| **P1** | Freeze | Snapshot only; Alliance founding debit occurs at P1 under the candidate model | B-02; B-09 |
| **P2** | Re-validate | Re-check accepted actions; release failed reservations; proposal counts and expiry checks | B-02; B-08 |
| **P3** | Recurring | Income/production **first**, then maintenance/upkeep; Alliance tax inside P3.1 and P3.3/P3.5; OP regeneration at the P3.7 opening; military Food at P3.7 6(a) | B-02; B-04; B-09; B-10 |
| **P4** | Orders | Construction, research, policy, trade settlement, diplomatic acts | B-04…B-09 |
| **P5** | Conflict | Campaigns, battles, losses, settlement prerequisites | B-10 |
| **P6** | World | Events, objectives, rankings | B-11 |
| **P7** | Settle | Invariants, digest, COMPLETED publication | B-02; B-11 |

### 9.3 Income and upkeep — D-019 preserved

**Production and income are applied first, followed by mandatory upkeep and maintenance.** A shortfall after income invokes the B-04 deficit/austerity rule; obligations never consume another action's reservation. The verified dependency chain is:

`tax income (F-EC-001)` → `maintenance (F-EC-014, P3.2)` → `extraction (F-EC-004)` → `power (F-EC-013)` → `processing (F-EC-006/007/008)` → `food settlement (F-EC-002/003, P3.6)` → `P3.7 obligations (F-WR-003 readiness, F-WR-036 military Food)` → `P7 treasury settlement`.

B-04 F-EC-000e publishes this internal order. D-019 is not altered, reinterpreted or weakened by 14A.

### 9.4 Operations Points — D-015 current authoritative model

| Property | Current position |
|---|---|
| Pool | One **persistent national military-only** pool |
| Transferability | Non-transferable; not purchasable, giftable or tradeable |
| Reservation | Reserved at acceptance |
| Consumption | Consumed at resolution |
| Per-war / shared Alliance pool | **None** |
| Regeneration | **+1 at the opening of P3.7** at each successful turn boundary; never at P0 or P7 |
| Carry | Unused points carry **below** the national cap |
| National cap | **10 (provisional)** |
| Pairing | Cap and regeneration rate are calibrated as a pair (`F-WR-001`) |

The original D-015 wording that unused points do not bank is **superseded by the recorded 10B-C3 amendment** (2026-11-04). B-14 states only the current position and does not calibrate it.

### 9.5 Timing dependency matrix

| Item | Canonical source | Phase | Trigger | Frequency | Dependencies | Status |
|---|---|---|---|---|---|---|
| Turn state machine | B-02 §12 TR-035/036 | — | Boundary clock | Every turn | Locked set required before resolution | Complete (rule) |
| Deterministic ordering | B-02 §14 TR-044/045 | All | Phase entry | Every turn | `(priority, submitted_at, action_id)`; B0–B4 | Complete (rule) |
| Tax income `F-EC-001` | B-04 §4.1 | P3.1 | Boundary | Every turn | Hunger penalty `F-EC-003` | Provisional |
| Maintenance `F-EC-014` | B-04 §4.3 | P3.2 | Boundary | Every turn | B-05 capacity | Provisional |
| Extraction `F-EC-004` | B-04 §4.1 | P3.3 | Boundary | Every turn | Capacity, crowns, space | Provisional |
| Power `F-EC-013` | B-04 §4.2 | P3.4–P3.7 | Boundary | Every turn | Generator fuel | Provisional |
| Processing `F-EC-006/007/008` | B-04 §4.2 | P3.4–P3.5 | Boundary | Every turn | Extraction output, power | Provisional |
| Food settlement `F-EC-002/003` | B-04 §4.1 | P3.6 | Boundary | Every turn | Protected civilian Food; `OP-09` release | Provisional |
| Capacity `F-CI-001` | B-05 §4.1 | Derived | Submission and P4.1 | Continuous read | Infrastructure | Provisional |
| Construction `F-CI-016`–`F-CI-020` | B-05 §4.2 | P4.1 | Accepted order | Per order | Capacity, crowns, materials | Provisional |
| Research `F-CI-021`–`F-CI-025` | B-05 §4.3 | P4.2 | Accepted order | Per order | Institutes, RP, crowns | Provisional |
| Population growth `F-PD-001` | B-06 §4 | P3.8 | Boundary | Every turn | Approval, housing, hunger, crowding | Provisional |
| Approval / stability `F-PD-012`–`F-PD-015` | B-06 §7 | P3.8 | Boundary | Every turn | Services, tax, food, order | Provisional |
| Election cycle `F-PD-026`–`F-PD-044` | B-06 §13 | P3.8 / P4.3 | `campaign_open_turn` + 24 turns | Per 240-turn term | Legitimacy, government | Provisional (cycle fixed by D-107) |
| Trade settlement `F-TM-037`/`F-TM-039` | B-07 §4.9 | P4 | Accepted trade | Per trade | Reservations, prices | Provisional |
| Proposal expiry `F-DP-004` | B-08 §2 | P2 | Boundary | Every turn | Freeze-aware timers | Provisional |
| Posture / agreement timers `F-DP-005`–`F-DP-009` | B-08 §2 | P2 | Boundary | Every turn | Actor freeze | Provisional |
| Alliance tax `F-AL-006` | B-09 §2 | P3.1 (Crowns), P3.3/P3.5 (resources) | Production event | Every turn | Frozen bracket snapshot | Design proposal (model authorised by D-140; no rate approved) |
| OP regeneration `F-WR-001` | B-10 §5 | P3.7 opening | Successful boundary | Every turn | `op_cap` + rate pair | Provisional |
| Readiness upkeep `F-WR-003` | B-10 §5 | P3.7 | Boundary | Every turn | Military stock, Food | Provisional |
| Military Food `F-WR-036` | B-10 §5 | P3.7 6(a) | Boundary | Every turn | Food left after P3.6 | Provisional |
| Battle resolution `F-WR-021`–`F-WR-028` | B-10 §5 | P5 | Campaign order | Per battle | Frozen baseline, seed | Provisional |
| Settlement `F-WR-029`–`F-WR-031` | B-10 §5 | P5 / P7 | Accepted settlement | Per conflict | Bounded losses, atomic transfer | Provisional |
| Events / objectives / rankings `F-WEP-001`–`F-WEP-050` | B-11 §3 | P6 | Boundary | Per event / objective / season | Post-P5 baseline | Provisional / structural |
| Fair-play sanctions `F-FP-001`–`F-FP-016` | B-12 §2 | **Not specified** | Case decision | Per case | Evidence, appeal windows | Metadata gap recorded |

---

## 10. Cross-system numerical dependencies — COMPLETE

| Source system | Dependent system | Formula / parameter IDs | Dependency type | Turn timing | Conservation constraint | Status |
|---|---|---|---|---|---|---|
| B-04 economy | B-05 cities | Y, V, M, P_ref per resource | Value input (B-04 wins) | P3/P4 | Resource conservation | Provisional |
| B-05 cities | B-04 economy | Capacity, maintenance base | Capacity input | P3.2 / P3.3 | DC accounting | Provisional |
| B-06 politics | B-04 economy | Tax rate, stability factor, population | Rate input | P3.1 | No minting | Provisional |
| B-04 economy | B-06 politics | Hunger penalty, food demand | Modifier | P3.6 → next P3.1 | Hunger cap 3,000 bp | Provisional |
| B-05 cities | B-06 politics | Housing, crowding | Modifier | P3.8 | Housing capacity | Provisional |
| B-07 trade | B-04 economy | Reserve/settle transfers, reference prices | Transaction | P4 | `F-TM-037`, `F-TM-039` | Provisional |
| B-04 economy | B-07 trade | `P_ref`, warehouse space, production | Value and availability | P4 | No negative stock | Provisional |
| B-08 diplomacy | B-09 alliances | Treaty effect catalogue | Rule link | P2 / boundary | No value minted by a treaty | Provisional |
| B-09 alliances | B-04 economy | Cumulative tax rates (0–10,000 bp) | Deduction | P3.1 / P3.3 / P3.5 | `0 ≤ Tax ≤ gross` | Design proposal |
| B-09 alliances | B-04/B-05 | ARL credits, operational expense | Transfer | P3 / P4 | ARL categories; no general withdrawal | Design proposal |
| B-10 warfare | B-04 economy | Supply bundle costs, military Food | Consumption | P3.7 / P5 | Resource expenditure | Provisional |
| B-04 economy | B-10 warfare | Food left after P3.6, crown balance | Availability | P3.7 / P5 | No debt | Provisional |
| B-05 cities | B-10 warfare | Infrastructure damage / repair curve | Modifier | P5 | City floor 10, 20-level strike cap, 30% campaign cap | Provisional |
| B-10 warfare | B-06 politics | Political-state constraint | Gate | P5 | No warpac | Provisional |
| B-11 progression | B-04 economy | Reward amounts / caps | Grant | P6 | `F-WEP-046`, `F-WEP-049` | Provisional |
| B-10 warfare | B-11 progression | Military participation / defensive band | Input | P6 | Post-P5 baseline | Provisional |
| B-03 protection | B-10 warfare | `P_prot` 84 turns | Gate | P5 | Hostile-action shield only | Provisional |
| B-03 protection | B-07 trade | Fresh window 360 turns; fair-value band | Gate | P4 | One-sided transfer block | Provisional |
| B-12 fair play | B-04 economy | Correction amount, restitution | Correction | Case | `F-FP-014` conservation | Provisional / owner-reserved |
| B-12 fair play | B-07/B-09/B-11 | Correction reach (account vs nation) | Scope | Case | `UD-052` open | Blocked by owner decision |
| B-02 turn system | Every register | Phase, ordering, seed | Execution frame | Every turn | One outcome per turn | Complete (rule) |
| B-01 account rules | B-03 protection | First-nation eligibility | Gate | Creation | Once-only protection | Complete (rule) |

**Reading rule for calibration.** A value may not be calibrated in isolation. `F-WR-001`'s cap and rate are a pair; `F-EC-001` and `F-EC-003` form a feedback loop through the next turn; `F-AL-006` must consume post-tax gross exactly once; `F-TM-005/006` and `F-WEP-046` share the material-value boundary. Prompt 14B–14K must consult this matrix before changing any value.

---

## 11. Initial balance-parameter inventory — COMPLETE FOR SCOPING, RESERVED FOR CALIBRATION

This section lists the **calibration clusters** that later subphases will address. It contains no proposed tuning.

| Cluster | Parameters | Owner of the decision | Evidence class | Subphase |
|---|---|---|---|---|
| Starting economy | 24 starting-bundle values; B-05 capital grant; B-06 political preset | Prompt 14 calibration | Offline calculation + simulation | 14B |
| Production and maintenance | 7 extraction vectors, 4 recipes, 3 generators, 11 reference prices | Prompt 14 | Simulation | 14B |
| Cities and construction | 18 city constants, 17 building costs, 13 research costs, 4 programmes | Prompt 14 | Simulation | 14C |
| Population and politics | ~97 B-06 constants including the election cycle (fixed at 240 by D-107) | Prompt 14; D-107 for the cycle | Simulation + playtest | 14D |
| Trade and markets | 26 B-07 constants; 3,000 bp band (D-114 rule) | Prompt 14; G-5 for fees | Market simulation | 14E |
| Diplomacy | 12 B-08 formula values | B-08 rule owner | Playtest | 14F |
| Alliances | 8 B-09 candidate values | Owner (`UD-040`, `UD-043`, `UD-044`, `UD-046`) | Owner decision | 14G |
| Warfare | 39 B-10 value sets incl. OP cap/rate pair | Prompt 14 | Simulation + playtest | 14H |
| Progression and rewards | 49 B-11 value sets incl. `UD-050`/`UD-051` | Prompt 14; owner for `UD-051` | Simulation + economy-impact model | 14I |
| Fair play and protection | `FP-P01`–`FP-P14`; `P_prot`; protection thresholds | Owner for `UD-053`/`UD-056`/`UD-059`; Prompt 14 for `FP-P02`/`FP-P08`/`FP-P13`/`FP-P14` | Case data, load test, playtest | 14J |
| Cross-system consolidation | Dependency effects, worked examples, balance report | Prompt 14 | Simulation | 14K |

**Reserved.** No cluster is calibrated here. The subphase allocation in the last column is the 14A proposal under Category B documentation architecture and must be confirmed by the owner's 14B–14K authorizations.

---

## 12. Existing validator and QA baseline — COMPLETE (EXECUTED 2026-11-13)

The full report is [`22_numerical_baseline_qa_report.md`](22_numerical_baseline_qa_report.md). Summary of what was actually executed:

| Script | Scope | Actual result | Classification |
|---|---|---|---|
| `verify_economy_numbers.py` | B-04 arithmetic | **164/164 PASS** | Numerical baseline |
| `verify_city_numbers.py` | B-05 arithmetic | **267/267 PASS** | Numerical baseline |
| `verify_politics_numbers.py` | B-06 arithmetic + continuity guards | **878/879; 1 inherited FAIL** — stale guard demands “Prompt 13C next” in progress-log row 10 | Numerical baseline + stale guard |
| `verify_market_numbers.py` | B-07 arithmetic | **ALL CHECKS PASSED** | Numerical baseline |
| `verify_diplomacy_numbers.py` | B-08 structure and arithmetic | **9 groups, 0 failed** | Numerical baseline |
| `verify_alliance_numbers.py` | B-09 arithmetic | **375 passed, 0 failed** | Numerical baseline |
| `verify_warfare_workflows.py` | B-10 workflows + 4 assertions group | **49/49, 0 failed** | Numerical regression |
| `verify_alliance_workflows.py` | B-09 workflows | **ALL CHECKS PASSED** (49 workflows, 65 cases, 132 tests) | Numerical regression |
| `verify_diplomacy_workflows.py` | B-08 workflows | **17 groups, 0 failed** | Numerical regression |
| `verify_market_workflows.py` | B-07 workflows | **ALL CHECKS PASSED** | Numerical regression |
| `09_validate.py` | B-03 | **371/371 PASS** | Structural baseline |
| `09A_validate_alliance.py` | B-09 | **943 checks; 2 inherited FAIL** (handoff/AI_CONTEXT next-prompt guards) | Stale continuity guards |
| `09B_validate_alliance_semantic.py` | B-09 semantics | **8 inherited FAIL** (C17 DD/D tally frozen at 219/267; C18 next-prompt guard) | Stale continuity guards |
| `10B_validate_warfare.py` | B-10 | **1,036 checks; 0 failures; 73/73 negative fixtures** | Structural/arithmetic |
| `11A_validate_research.py` | 11A research | **29/30; 1 inherited FAIL** — frozen `REQ-703` maximum | Stale guard |
| `11B_validate_b11.py` | B-11 | **PASS; 52 gates PASS** | Structural |
| `11C_validate_b11_workflows.py` | B-11 workflows | **PASS** | Structural |
| `12A_validate_foundations.py` | B-12 research | **45/45 PASS** | Structural |
| `12B_validate_b12.py` | B-12 | **87/87 PASS** | Structural/arithmetic |
| `12C_validate_fair_play_workflows.py` | B-12 workflows | **24/24 PASS** | Structural |
| `13A`/`13B`/`13C`/`13D` | UI families | **34/34, 28/28, 27/27, 75/75 PASS** | Documentation QA |
| `validate_final.py` | Project-wide | **ALL CHECKS PASSED** | Documentation QA |
| `validate_links.py` | Markdown links | **4,386 links; 4,004 local; 382 external; 34 anchors; 0 unresolved** | Documentation QA |
| `test_decision_registers.py` | UD register | **12 tests OK** | Register QA |
| `test_next_action.py` | Continuity | **27 tests OK** | Continuity QA |
| `14A_validate_numerical_foundation.py` | B-14 numerical foundation | **64/64 checks; 150/150 self-tests** (55 legacy checks + 9 controlled-contract checks; 138 legacy self-tests + 12 contract self-tests) | **14A primary** |
| `14A_contract_validator.py` | Controlled numerical contracts | **9/9 production checks; 83/83 regression tests** (see §18) | **Semantic-contract architecture (D-238)** |
| `test_14A_trusted_amendment_security.py` | C2 trusted-input and semantic-gate hardening | **46/46 tests; OK** (see §18.7) | **C2 hardening (D-239)** |
| `test_14A_metadata_diff.py` | C3 contract-level metadata diff | **8/8 tests; OK** (see §18.8) | **C3 reconciliation** |

**Inherited failures.** Two numerical/structure scripts and two historical validators fail on frozen continuity expectations. None is caused by 14A; none was edited to make it pass. They are classified in §13 and in the QA report.

**What the baseline cannot establish.** No script executes a gameplay formula against a scheduler, a database or player data. Every result is documentation/arithmetic quality. There is no playable Nation Supremacy runtime.

---

## 13. Identified inconsistencies and missing definitions — COMPLETE (RECORDED, NOT REPAIRED)

### 13.1 Source-register findings

| # | Finding | Affected | Impact | Owner of the repair |
|---:|---|---|---|---|
| 1 | `F-TM-000e` cites `§4.20`; B-07 has no §4.20 | B-07 timing citation | Ambiguous cross-reference, rule itself clear | B-07 revision (14E) |
| 2 | Duplicate register-rule identifiers `F-TM-000e`, `F-TM-000f` | B-07 §2 and §6 | Duplicate identifier in the 000 series; no active duplicate | B-07 revision |
| 3 | Eleven active B-04 identifiers are non-computational (`F-EC-036`–`F-EC-046`) | B-04 count | Count includes governance entries; reported, not renumbered | B-04 revision |
| 4 | B-12 formulas have no P0–P7 timing field | All 16 `F-FP-` | Sanction timing not numerically anchored | B-12 / 14J |
| 5 | B-03 leaves the fair-value band `UNSPECIFIED`; B-07 fixes 3,000 bp | B-03 row 12; B-07 `B` | Two-source parameter; values are compatible but must be cited together | B-03 / B-07 |
| 6 | Six B-05 formulas lack a rounding field | `F-CI-009`, `022`, `024`, `027`, `028`, `029` | Register-level convention applies; per-formula gap | B-05 / 14C |
| 7 | B-08 does not separately state outputs for all formulas | `F-DP-001`–`012` | Definition supplies the result; metadata gap | B-08 / 14F |
| 8 | B-09 does not separately state dependencies | `F-AL-001`–`008` | Source rules supply traceability; metadata gap | B-09 / 14G |
| 9 | D-015 original wording (“unused points do not bank”) conflicts with the current 10B-C3 carry rule | B-10 `F-WR-001` | **Resolved by the recorded amendment**; B-14 states only the current position | B-02/B-10 records |
| 10 | `F-WEP-037` says “k = 5 is approved”; `UD-050` still tests viability | B-11 | `k = 5` is a confirmed design rule (D-027), not an owner-approved value; the viability question remains Open | 14I / Prompt 12 |

### 13.2 QA and continuity findings

| # | Finding | Evidence | Classification |
|---:|---|---|---|
| 11 | `verify_politics_numbers.py` fails one guard that requires the literal “Prompt 13C next” in progress-log row 10 | Actual run 2026-11-13: 878/879 | Stale documentation guard — inherited |
| 12 | `11A_validate_research.py` fails the guard “max REQ stays REQ-703” | Actual run: 29/30 | Stale guard — inherited |
| 13 | `09A_validate_alliance.py` fails two next-prompt guards | Actual run: 2 problems / 943 checks | Stale continuity guard — inherited |
| 14 | `09B_validate_alliance_semantic.py` fails eight frozen register-tally guards (D-001…D-219, DD-001…DD-267) | Actual run: 8 problems | Stale guard — inherited |
| 15 | An earlier note claimed several scripts exit `0` on FAIL. **Corrected by 14A-C1:** re-executed without a pipeline, `verify_politics_numbers.py`, `11A_validate_research.py`, `09A_validate_alliance.py` and `09B_validate_alliance_semantic.py` each return exit code **1**. | Measured 2026-11-13 | Earlier claim removed; no harness exception remains asserted |
| 16 | The owner confirmed Prompt 13D formal acceptance on 2026-11-13, while the detailed 13D acceptance record and several dated historical blocks still carry the pre-acceptance “PENDING” wording | `23_prompt_13d_owner_acceptance_record.md`; dated status history | **Baseline continuity discrepancy.** The 14A instruction records the acceptance; the current-position status blocks now state it and label the older lines as snapshots. A separate bounded reconciliation of the detailed record is required; 14A does not rewrite Prompt 13 acceptance history. |

### 13.3 What 14A deliberately did not do

It did not repair any finding above. Repairing a register changes a formula, a value or a structure and is outside 14A's authorization. The findings are the input to 14B–14K and to a separate continuity-reconciliation task.

---

## 14. Owner-reserved and externally dependent parameters — BLOCKED WHERE NOTED

| Decision | Numerical boundary | Current status | What is blocked |
|---|---|---|---|
| `UD-017` | Data-protection jurisdiction, lawful basis, age gate, retention | **Open — owner/legal** | `FP-P11`; pair-record retention; any legal retention claim |
| `UD-031` | Reroll-frequency review value | **Deferred to Prompt 12**; Prompt 14 validates | The final reroll flag value |
| `UD-040` | Alliance founding, cost, multiple membership | **Open — owner** | `F-AL-001`, `F-AL-002`, `F-AL-006` attribution |
| `UD-043` | Succession, removal, inactivity | **Open — owner** | `F-AL-003` vacancy window |
| `UD-044` | Member rights, expulsion, rejoin cooldown | **Open — owner** | `F-AL-004` |
| `UD-046` | Treasury ownership, withdrawals, capacity, dual approval | **Open — owner** | `F-AL-001`, `F-AL-005`, `F-AL-008`; no capacity/fee invented |
| `UD-047` | Collective diplomacy and delegation | **Open — owner** | No numerical parameter may be invented |
| `UD-050` | Alliance-standings `k = 5` viability | **Open — evidence** | `F-WEP-037` publication threshold |
| `UD-051` | Material-reward “rare” bound | **Open — Prompt 14** | `F-WEP-046` |
| `UD-053` | Single sanctions ladder and tiers | **Open — owner** | `FP-P01`, `FP-P04`, `FP-P05` |
| `UD-056` | Emergency authority scope and duration | **Open — owner** | `FP-P10` |
| `UD-059` | Appeal count and window | **Open — owner** | `FP-P06`, `FP-P12` |
| `UD-052`, `UD-054`, `UD-055`, `UD-057`, `UD-058`, `UD-060` | Correction reach, moderation staffing, evidence retention, automation, public history, age assurance | **Open — owner** | Fair-play corrections, retention and emergency parameters |
| `UD-041`, `UD-042`, `UD-045`, `UD-048`, `UD-049` | Alliance governance, capabilities, Discord link, announcements/votes | **Open — owner** | Alliance governance parameters |

**Preserved without change:** automatic per-turn production taxation; player-authored 0–100% tax rates; separate Crowns and resource schedules; cumulative fractional rounding per asset and per turn; multiple-Alliance attribution rules; the reversible 0% protective fallback; the prohibition on unauthorised Alliance withdrawal or treasury permission; the absence of invented storage capacity, fees or operational-funding schedules.

### 14.1 Outstanding production-security obligations

The following remain **unresolved** and are not described as completed anywhere in B-14:

1. The Supabase prototype's table-wide `UPDATE` on `feasibility.profiles`, including `treasury`.
2. The missing corrective migration `0005`.
3. The missing SQL permission tests.
4. The missing protective audit trigger.
5. The unverified tamper-evident audit implementation.
6. The unverified audit-digest job.

**Numerical/timing dependencies they impose:** the audit-digest interval (`FP-P13` is a different parameter; the audit-digest chain is `F-FP-012`/`F-FP-013`), the retention periods (`FP-P11`, `UD-017`/`UD-055`) and the treasury-integrity conservation identity (`F-FP-014`). Future owner: Stage 5/6 security work with Prompt 12; 14A neither implements nor repairs them.

---

## 15. Prompt 14A completion and evidence — COMPLETE

### 15.1 Deliverables

| # | Deliverable | Path | Status |
|---:|---|---|---|
| 1 | Canonical B-14 document | `docs/stage-2/22_formulas_and_balance.md` | Complete |
| 2 | Formula master inventory | [`22_formula_master_inventory.md`](22_formula_master_inventory.md) | Complete |
| 3 | Numerical parameter ownership map | [`22_numerical_parameter_inventory.md`](22_numerical_parameter_inventory.md) | Complete |
| 4 | Numerical baseline QA report | [`22_numerical_baseline_qa_report.md`](22_numerical_baseline_qa_report.md) | Complete |
| 5 | Focused validator and regression tests | [`../qa_backups/14A_validate_numerical_foundation.py`](../qa_backups/14A_validate_numerical_foundation.py) | Complete — 55 checks, 138/138 fixtures after the constrained semantic contract |
| 6 | Permanent prompt archive and index | `../prompts/prompt_14A_*.md`; `../prompts/INDEX.md` | Complete |
| 7 | Continuity and governance updates | Roadmap, progress log, handoff, AI_CONTEXT/AI_HANDOFF/PROJECT_PROGRESS as genuinely affected | Complete |
| 8 | Acceptance assessment | §16 of this document and the QA report | Complete |

### 15.2 Acceptance gates

| Gate | Acceptance objective | Required evidence | Validation method | Actual result | Status | Known limitation | Outstanding issue | Next action |
|---|---|---|---|---|---|---|---|---|
| P14A-01 | Complete governance and policy review | Policy and continuity files read | Manual review | All mandatory files read | PASS | None | None | Preserve |
| P14A-02 | B-02 authoritative timing reconciliation | Cadence, P0–P7, conversions | Cross-check against B-02 §10–§14, §22 | 5/5 conversions agree; D-019/D-015 verified | PASS | B-02 itself is provisional in implementation | None | Carry into 14B |
| P14A-03 | B-03 complete review | §8, §9, §12, §18, §21.2, §21.3, §22 | Manual review | Reviewed | PASS | None | None | Preserve |
| P14A-04 | All nine registers inventoried | 295 active records | Automated extraction + manual review | 295 active | PASS | Extraction is index-level, not a re-derivation | None | Maintain |
| P14A-05 | Active formula ID reconciliation | Per-register counts | Independent recount | 47/41/44/39/12/8/39/49/16 | PASS | B-04 includes 11 governance entries | Recorded | 14B–14K |
| P14A-06 | Complete numerical parameter inventory | Parameter records reconciled per system | Table extraction + 393-record source reconciliation | **393 parameter inventory records** (7 B-02 + 20 B-03 + 366 across B-04…B-12); some records are vectors or grouped values | PASS | 393 is the record count, not a scalar-value count | Per-record metadata gaps recorded | 14B–14K |
| P14A-07 | All 20 B-03 carry-ins reconciled | 20 exact rows | Row-by-row comparison | 20/20 | PASS | None | Row 12 two-source | 14E |
| P14A-08 | Parameter ownership and decision authority identified | Authority per row | Source-field comparison | Recorded | PASS | Some rows have no registered authority | Recorded | 14B–14K |
| P14A-09 | Four numerical statuses implemented consistently | Vocabulary audit | Validator + analysis | Four labels + absence marker | PASS | No value is owner-approved | None | Maintain |
| P14A-10 | Units, precision and rounding inventory | Convention matrix | Register review | Matrix complete | PASS | Five register-level gaps | Recorded | 14B–14K |
| P14A-11 | P0–P7 timing and D-019 reconciliation | Timing matrix | Cross-check | Complete | PASS | B-12 has no phase field | Recorded | 14J |
| P14A-12 | D-015 current OP model preserved | Current model statement | Compare with 10B-C3 amendment | Preserved | PASS | Cap remains provisional | None | 14H |
| P14A-13 | Cross-system numerical dependency inventory | Dependency matrix | Register cross-check | 22 rows | PASS | Not a full simulation | None | 14B–14K |
| P14A-14 | Existing validator baseline independently executed | Actual command results | Execution on 2026-11-13 | All scripts run; inherited failures recorded | PASS | Documentation QA only | 4 inherited failing scripts | Separate maintenance |
| P14A-15 | Canonical B-14 filename corrected | Roadmap row 14 uses `22_` | Validator check | Corrected | PASS | Row 15 remains per D-198 boundary | Recorded | None |
| P14A-16 | Canonical B-14 document created | This file, 16 sections | File inspection | Created | PASS | Content is foundation only | None | 14B |
| P14A-17 | Prompt archive and index updated | Archive + byte/SHA-256 | Hash verification | 45,984 bytes; SHA-256 `5441eef4…`; INDEX row matches; 1,410 LF / 0 CRLF | PASS | No external original exists for byte comparison | Provenance caveat recorded | None |
| P14A-18 | Focused numerical foundation validator created | `14A_validate_numerical_foundation.py` | Execution | 55 checks; 138/138 self-tests after the constrained semantic contract | PASS | Documentary only | None | Maintain |
| P14A-19 | Positive and negative regression fixtures pass | Prior 128 + constrained semantic-contract cases | Self-test run | 138/138 passed | PASS | Fixtures test the validator, not the game | None | Maintain |
| P14A-20 | Continuity, historical and owner-reserved decisions preserved | No protected change | Diff review + decision-register tests | Preserved | PARTIAL | Prompt 13D acceptance discrepancy remains un-reconciled by design | Separate reconciliation required | Owner/next continuity pass |
| P14A-21 | Final project QA and documentation links reconciled | `validate_final`, `validate_links` | Execution | `validate_final.py` ALL CHECKS PASSED; 4,386 links, 4,004 local, 0 unresolved | PASS | Inherited failures remain visible | None | None |
| P14A-22 | Prompt 14A handoff and completion assessment | Handoff updated | File inspection | Complete | PASS | Prompt 14 remains incomplete | 14B unauthorized | Await owner |

**Gate tally:** 21 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED. `P14A-20` is PARTIAL because the Prompt 13D acceptance continuity discrepancy is a pre-existing baseline defect that 14A is instructed to record rather than rewrite. No gate was deleted or weakened.

### 15.3 Prompt 14A-C1 correction gates

| Gate | Acceptance objective | Required evidence | Actual result | Status | Known limitation | Outstanding issue | Next action |
|---|---|---|---|---|---|---|---|
| C1-01 | Complete governance and policy review | Policy, 14A archive and current validator read | Read and applied | PASS | None | None | Preserve |
| C1-02 | All 393 parameter records reconciled | Per-record source comparison | 393/393 reconciled (7 + 20 + 366) | PASS | 393 records ≠ 393 scalars | Vector records noted | Maintain |
| C1-03 | B-02–B-12 coverage validated | Source adapters for every system | 11 systems; no register skipped | PASS | Adapters document parsing assumptions | None | Maintain |
| C1-04 | Source values verified | Token-multiset/value comparison | 0 value mismatches | PASS | Textual status values compared by required tokens | None | 14B–14K |
| C1-05 | Units, precision, rounding and timing validated | Per-record metadata check | Units, timing and rounding match source or carry explicit markers | PASS | B-12 states no per-parameter rounding/timing; explicit note added | B-12 metadata gap remains | 14J |
| C1-06 | Ownership and decision authority verified | Source owner fields and UD positions | 0 authority mismatches | PASS | Some sources name no authority; recorded | None | 14B–14K |
| C1-07 | Four status safeguards enforced | Status mapping and owner-approved rule | 0 invalid statuses; 0 false owner-approved | PASS | None | None | Maintain |
| C1-08 | All 20 B-03 carry-ins intact | Exact rows | 20/20 values and owners exact | PASS | None | None | Preserve |
| C1-09 | Four original mutation cases rejected | Fixtures 21–24 | All four rejected | PASS | Fixtures test the validator | None | Maintain |
| C1-10 | Additional cross-system negative fixtures pass | Fixtures 25–32 | All eight rejected | PASS | None | None | Maintain |
| C1-11 | Existing 14A tests intact and passing | Original 20 fixtures | 20/20 preserved; 35/35 at C1; 48/48 at R1; 64/64 at R1-R1; 78/78 at final C1; 94/94 at closure; 118/118 after decision-evidence validation | PASS | None | None | Maintain |
| C1-12 | P14A-06 records 393 | Gate wording and breakdown | 393 records with breakdown | PASS | Vectors noted | None | None |
| C1-13 | Documentation-link totals rerun and reconciled | Actual final output | See QA report and §12 | PASS | Final totals may differ from the 95 baseline | None | None |
| C1-14 | Politics-validator exit evidence corrected | Actual process exit code | Exit **1**, 878/879 | PASS | Inherited guard remains | None | Separate maintenance |
| C1-15 | Other QA assertions supported by execution | Measured exit codes | 11A, 09A and 09B each exit **1**; generic claim removed | PASS | None | None | None |
| C1-16 | Prompt archive and index verified | Archive + byte/SHA | Archived and indexed | PASS | No external original | Provenance caveat | None |
| C1-17 | Historical records and owner-reserved decisions preserved | Diff and UD check | Preserved | PASS | None | None | None |
| C1-18 | No formula or game-balance change | Register diff | 295 identifiers unchanged | PASS | None | None | None |
| C1-19 | Final project and documentation QA complete | Validator suite | See QA report | PASS | Inherited failures remain visible | None | None |
| C1-20 | Final correction report and handoff produced | Progress log §99 and handoff | Produced | PASS | None | None | Owner review |

**C1 gate tally:** 20 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

### 15.4 Prompt 14A-C1-R1 source-validation gates

| Gate | Acceptance objective | Actual result | Status |
|---|---|---|---|
| R1-01 | Complete policy and governance review | Policy and archives read | PASS |
| R1-02 | Nine original mutation cases rejected | 9/9 rejected | PASS |
| R1-03 | All 393 parameter records source-reconciled | 393/393; 0 unparseable | PASS |
| R1-04 | B-02 metadata validated | 7/7 values, units, timing, authority, status | PASS |
| R1-05 | All 20 B-03 carry-ins validated | 20/20 values, units, owners, evidence, classes | PASS |
| R1-06 | B-04 metadata validated | 49/49 | PASS |
| R1-07 | B-05 metadata validated | 73/73 | PASS |
| R1-08 | B-06 metadata validated | 96/96 | PASS |
| R1-09 | B-07 metadata validated | 26/26 | PASS |
| R1-10 | B-08 metadata validated | 12/12 | PASS |
| R1-11 | B-09 metadata validated | 8/8 | PASS |
| R1-12 | B-10 metadata validated | 39/39 | PASS |
| R1-13 | B-11 metadata validated | 49/49 | PASS |
| R1-14 | B-12 metadata validated | 14/14 | PASS |
| R1-15 | Units source-validated | 306 matched / 74 explicit / 13 derived / 0 mismatch | PASS |
| R1-16 | Precision and rounding source-validated | 108 source-matched, 244 convention, 41 explicit | PASS |
| R1-17 | Timing source-validated | 115 source-matched, 244 convention, 34 explicit | PASS |
| R1-18 | Decision authorities source-validated | 393/393 | PASS |
| R1-19 | Four numerical status safeguards enforced | 393/393; 0 false approvals | PASS |
| R1-20 | Evidence requirements and classifications validated | B-03 20/20; B-12 14/14 | PASS |
| R1-21 | Owner-reserved decisions protected | No owner-reserved change | PASS |
| R1-22 | Positive and negative regression suite passes | 48/48 | PASS |
| R1-23 | All earlier 14A/C1 checks preserved | 35 prior checks and 35 prior tests intact | PASS |
| R1-24 | QA and parameter coverage reports reconciled | Matrix in QA report §5.3 | PASS |
| R1-25 | Prompt archive and index verified | 28,984 bytes; SHA-256 `abf6b021…` | PASS |
| R1-26 | No original formula definitions changed | 295/295; registers unmodified | PASS |
| R1-27 | No implementation or Git changes | None | PASS |
| R1-28 | Final project validation completed | See QA report | PASS |
| R1-29 | Handoff and completion assessment prepared | Log §100 and handoff | PASS |

**R1 gate tally:** 29 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

### 15.5 Prompt 14A-C1-R1-R1 final correction gates

| Gate | Acceptance objective | Actual result | Status |
|---|---|---|---|
| R1-R1-01 | Complete policy and governance review | Read and applied | PASS |
| R1-R1-02 | Existing 41 validator checks preserved | 41 prior checks intact; 44 total | PASS |
| R1-R1-03 | Existing 48 self-tests preserved | 48 prior tests intact; 64 total | PASS |
| R1-R1-04 | B-04 Treasury precision/rounding source verified | Register-level integer/bp convention (`F-EC-000b`) | PASS |
| R1-R1-05 | Invalid Treasury precision/rounding mutation rejected | Fixture 49 rejected by `14A-42` | PASS |
| R1-R1-06 | B-04–B-07 precision/rounding metadata coverage verified | 244/244 constants; four source anchors | PASS |
| R1-R1-07 | All 393 owner-reserved flags reconciled | 386 applicable matched; 7 B-02 records have no flag field | PASS |
| R1-R1-08 | False B-04 Treasury owner-reserved flag rejected | Fixture 56 rejected by `14A-43` | PASS |
| R1-R1-09 | Genuine owner-reserved parameter remains accepted | B-09 and B-12 owner-reserved rows pass | PASS |
| R1-R1-10 | False NO/YES owner-reserved mutations rejected | Fixtures 57–61 rejected | PASS |
| R1-R1-11 | Unrelated decision references cannot establish authority | Status/authority compared to source; no bare-D approval path | PASS |
| R1-R1-12 | Ambiguous ownership fails closed | Fixture 62 rejected as ambiguous | PASS |
| R1-R1-13 | New positive and negative regressions pass | 16 new fixtures; 64/64 total | PASS |
| R1-R1-14 | Previous C1/R1 regressions remain intact | 48 prior fixtures preserved | PASS |
| R1-R1-15 | All 393 parameter records remain reconciled | 393/393; 0 unparseable | PASS |
| R1-R1-16 | All 295 formula identifiers remain unchanged | 295/295; registers unmodified | PASS |
| R1-R1-17 | Historical QA evidence preserved | §98–§100 unchanged | PASS |
| R1-R1-18 | C1-R1 verbatim archive reconciled or limitation documented | Provenance removed; 28,525 bytes; SHA-256 `4c282b11…`; no external original | PASS |
| R1-R1-19 | This final correction prompt archived and hashed | 24,815 bytes; SHA-256 `12e03da2…` | PASS |
| R1-R1-20 | Final project validator passes | `validate_final.py` ALL CHECKS PASSED | PASS |
| R1-R1-21 | Documentation links and prompt index pass | **131 files; 4,386 links; 4,004 local; 382 external; 34 anchors; 0 unresolved**; index rows match | PASS |
| R1-R1-22 | Owner-reserved decisions and policy remain protected | No UD/D-015/D-019 change | PASS |
| R1-R1-23 | No implementation or Git operations occurred | None | PASS |
| R1-R1-24 | Final independent handoff is prepared | Log §101 and handoff | PASS |

**R1-R1 gate tally:** 24 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

### 15.6 Prompt 14A-C1-R1-R1-C1 final correction gates

| Gate | Acceptance objective | Actual result | Status |
|---|---|---|---|
| FINAL-C1-01 | Complete governance and policy review | Read and applied | PASS |
| FINAL-C1-02 | F-EC-000b integer rule semantically validated | Contract hash and required phrase | PASS |
| FINAL-C1-03 | F-EC-000b rounding requirements validated | floor/ceil/round_half_up clause | PASS |
| FINAL-C1-04 | F-EC-000b floating-point prohibition protected | Required and forbidden phrases | PASS |
| FINAL-C1-05 | F-EC-000b basis-point relationship protected | Integer bp and 10,000 bp = 100% | PASS |
| FINAL-C1-06 | F-EC-000f calibration-version rule validated | Contract hash and required phrases | PASS |
| FINAL-C1-07 | F-EC-000f provisional classification preserved | v1.0 provisional calibration | PASS |
| FINAL-C1-08 | F-EC-000f F-EC-044 reference preserved | Required phrase | PASS |
| FINAL-C1-09 | F-EC-000f calibration claims remain correct | Not observed prices / not balance claims | PASS |
| FINAL-C1-10 | F-EC-000f register-revision rule protected | Required revision sentence | PASS |
| FINAL-C1-11 | Both original semantic mutations rejected | Fixtures 66 and 73 | PASS |
| FINAL-C1-12 | Additional semantic regression tests pass | Fixtures 65–78; 78/78 total | PASS |
| FINAL-C1-13 | Legitimate baseline source passes | Fixtures 65 and 72 | PASS |
| FINAL-C1-14 | Authorized amendment handling documented | Failure message and QA report §5.8 | PASS |
| FINAL-C1-15 | No original formula definitions changed | 295/295; registers unmodified | PASS |
| FINAL-C1-16 | No numerical parameter values changed | 393 records preserved | PASS |
| FINAL-C1-17 | B-14 §15.5 final link count reconciled | R1-R1-21 updated to actual final output | PASS |
| FINAL-C1-18 | All current QA records show identical final link totals | B-14, QA report, log §102, handoff | PASS |
| FINAL-C1-19 | Documentation-link validator passes | 126 files; 0 unresolved | PASS |
| FINAL-C1-20 | Final project validator passes | `validate_final.py` ALL CHECKS PASSED | PASS |
| FINAL-C1-21 | Existing 44 validator checks preserved | 44 prior checks intact; 47 total | PASS |
| FINAL-C1-22 | Existing 64 self-tests preserved | 64 prior tests intact; 78 total | PASS |
| FINAL-C1-23 | Previous C1/R1/R1-R1 regressions remain passing | 64 prior fixtures pass | PASS |
| FINAL-C1-24 | New correction prompt archived verbatim | 20,967 bytes; SHA-256 `3cd01360…` | PASS |
| FINAL-C1-25 | Prompt index hash and byte count verified | INDEX row matches | PASS |
| FINAL-C1-26 | Owner-reserved decisions preserved | No UD/D-015/D-019 change | PASS |
| FINAL-C1-27 | No implementation or Git operations occur | None | PASS |
| FINAL-C1-28 | Final handoff prepared | Log §102 and handoff | PASS |

**FINAL-C1 gate tally:** 28 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

### 15.7 Prompt 14A-C1-R1-R1-C1-R1 closure gates

| Gate | Acceptance objective | Actual result | Status |
|---|---|---|---|
| FINAL-R1-01 | Complete D-014 review | Policy and decision register inspected | PASS |
| FINAL-R1-02 | Current F-EC-000b source verified | Hash `bb1090cc…`; baseline phrases | PASS |
| FINAL-R1-03 | Current F-EC-000f source verified | Hash `3025cc44…`; baseline phrases | PASS |
| FINAL-R1-04 | Current controlled hashes verified | Python contract and JSON manifest agree | PASS |
| FINAL-R1-05 | Unauthorized source changes rejected | Fixture 82 | PASS |
| FINAL-R1-06 | Hash updates without decisions rejected | Fixtures 83 and 90 | PASS |
| FINAL-R1-07 | Unrelated D-number references rejected | Fixture 84 | PASS |
| FINAL-R1-08 | Wrong-clause decision references rejected | Fixture 85 | PASS |
| FINAL-R1-09 | Pending/rejected/deferred decision references rejected | Fixtures 86–89 | PASS |
| FINAL-R1-10 | Applicable D-014 decision authority verified | Category B Confirmed fixture 80 | PASS |
| FINAL-R1-11 | Owner-reserved amendments require the applicable authorization | Category A fixture 81; negative fixture 93 | PASS |
| FINAL-R1-12 | Proper authorized amendment fixture accepted | Fixtures 80–81 | PASS |
| FINAL-R1-13 | All previous source-semantic protections preserved | Fixtures 65–78 | PASS |
| FINAL-R1-14 | All Treasury precision/rounding safeguards preserved | Fixtures 49–55 | PASS |
| FINAL-R1-15 | All owner-reserved safeguards preserved | Fixtures 56–63 | PASS |
| FINAL-R1-16 | All 47 previous validator checks preserved | 47 prior checks; 49 total | PASS |
| FINAL-R1-17 | All 78 previous regression tests preserved | 78 prior tests; 94 total | PASS |
| FINAL-R1-18 | New amendment mutation suite passes | Fixtures 79–94 | PASS |
| FINAL-R1-19 | 295 formulas unchanged | 295/295; registers unmodified | PASS |
| FINAL-R1-20 | 393 parameter records unchanged | 393/393 | PASS |
| FINAL-R1-21 | Final link totals reconciled | 127 files; 4,354 links; 3,972 local; 0 unresolved | PASS |
| FINAL-R1-22 | Final project validator passes | `validate_final.py` ALL CHECKS PASSED | PASS |
| FINAL-R1-23 | Prompt archive and SHA-256 verified | 19,654 bytes; `5e11f662…` | PASS |
| FINAL-R1-24 | Policy and owner decisions preserved | No change | PASS |
| FINAL-R1-25 | No implementation or Git operations | None | PASS |
| FINAL-R1-26 | Final Prompt 14A handoff prepared | Log §103 and handoff | PASS |

**FINAL-R1 gate tally:** 26 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

### 15.8 Prompt 14A-C1-R1-R1-C1-R1-C1 closure gates

| Gate | Acceptance objective | Actual result | Status |
|---|---|---|---|
| CLOSURE-01 | Complete D-014 policy review | Policy and decisions inspected | PASS |
| CLOSURE-02 | Decision-table schema correctly parsed | 8-column header mapped by name | PASS |
| CLOSURE-03 | Decision ID uniqueness enforced | 0 duplicate rows; duplicates rejected | PASS |
| CLOSURE-04 | Exact source/clause identity validated | Exact filename and clause required | PASS |
| CLOSURE-05 | Previous rule evidence verified | Marker + source comparison | PASS |
| CLOSURE-06 | Replacement rule evidence verified | Marker + source comparison | PASS |
| CLOSURE-07 | Relevant alternatives verified | Required where applicable | PASS |
| CLOSURE-08 | Rationale substantive and clause-specific | Generic text rejected | PASS |
| CLOSURE-09 | Supporting evidence resolves | Repository path checked | PASS |
| CLOSURE-10 | Consequences verified | Consequences field required | PASS |
| CLOSURE-11 | Reopening conditions verified | Reopening marker required | PASS |
| CLOSURE-12 | D-014 authority/category enforced | Category A/B/C/D rules | PASS |
| CLOSURE-13 | Decision/manifest status agree | Cross-checked | PASS |
| CLOSURE-14 | Owner authorization enforced where required | Category A/D/owner-reserved | PASS |
| CLOSURE-15 | False D-998 mutation rejected | Fixture 95 and related | PASS |
| CLOSURE-16 | Additional negative tests rejected | Fixtures 95–117 | PASS |
| CLOSURE-17 | Complete Category B fixture accepted | Fixture 80 | PASS |
| CLOSURE-18 | Category A fixture accepted where permitted | Fixture 81 | PASS |
| CLOSURE-19 | Category C fixture remains Provisional | Fixture 118 | PASS |
| CLOSURE-20 | Previous 49 checks preserved (historical snapshot of the CLOSURE correction) | 49 prior; 51 total | PASS |
| CLOSURE-21 | Previous 94 tests preserved (historical snapshot of the CLOSURE correction) | 94 prior; 118 total | PASS |
| CLOSURE-22 | B-04 source hashes unchanged | `bb1090cc…` / `3025cc44…` | PASS |
| CLOSURE-23 | Production manifest unchanged and empty | `amendments: []` | PASS |
| CLOSURE-24 | 295 formula identifiers preserved | 295/295 | PASS |
| CLOSURE-25 | 393 parameter records preserved | 393/393 | PASS |
| CLOSURE-26 | QA report link totals reconciled | 131/4,386/4,004 | PASS |
| CLOSURE-27 | B-14 and progress log agree | Same totals (131/4,386/4,004) | PASS |
| CLOSURE-28 | Documentation-link validator passes | 0 unresolved | PASS |
| CLOSURE-29 | Final project validator passes | ALL CHECKS PASSED | PASS |
| CLOSURE-30 | Decision-register tests pass | 12/12 | PASS |
| CLOSURE-31 | Next-action tests pass | 27/27 | PASS |
| CLOSURE-32 | Prompt archive and index verified (historical snapshot; C1-R1-R1-C1-R1-C1 archive) | 29,966 bytes; `a377413e…` | PASS |
| CLOSURE-33 | Historical records and owner decisions preserved | No change | PASS |
| CLOSURE-34 | No implementation or Git operations | None | PASS |
| CLOSURE-35 | Final handoff completed (historical snapshot of the CLOSURE correction) | Log §104 and handoff | PASS |

**CLOSURE gate tally:** 35 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

### 15.9 Decision-evidence semantic relevance closure

| Check | Result |
|---|---|
| Authorized evidence loci | F-EC-000b: B-04 F-EC-000b/F-EC-000c, B-14 §8.2, REQ-162; F-EC-000f: B-04 F-EC-000f/F-EC-044, B-14 §5/§7 |
| Evidence format | Structured `path`, `section`, `quote`, `supports` and `Rationale` |
| Content verification | Quote must appear in the cited section of the cited document |
| Relevance verification | Supports-claim must overlap the quoted evidence; unrelated documents are rejected |
| Exact D-998 fair-play attack | **REJECTED** for `evidence locus is not an authorized source for F-EC-000b` |
| Fabricated/misleading/stale excerpts | Rejected for missing quote, wrong section or unsupported claim |
| Positive Category A/B/C fixtures | Accepted under their D-014 paths |
| Baseline | PASS |
| Production manifest | Empty |

The fair-play document is not an authorized evidence locus for a B-04 numerical amendment; a path, filename, generic rationale or matching hash is not sufficient. A future legitimate evidence source must be added to the controlled allowlist with the authorizing decision and regression evidence.

### 15.10 Evidence contradiction detection

| Check | Result |
|---|---|
| Stance vocabulary | `supports` / `contradicts` / `not_established` computed independently; a declared `stance=supports` is not trusted on its own |
| Permission vs prohibition | Floating-point permission in the amendment against a prohibiting passage is rejected |
| Negation reversal | “Observed prices / balance claims” against “not observed prices / not balance claims” is rejected |
| Numerical scope | A changed basis-point relationship is rejected against the cited 10,000-bp passage |
| Coverage | A supports-claim term absent from the quote is rejected as not established |
| Fractional carry | “No fractional carry stated” is not treated as affirmative permission |
| Unauthorized mapping | A manifest field claiming its own allowlist is ignored; the controlled allowlist governs |
| D-999 attack | **REJECTED** — prohibition presented as permission |
| Positive Category A/B/C | Accepted under their D-014 paths |
| Baseline | PASS |

The evidence check is deterministic and source-backed: authorized locus, section resolution, exact quote, independent polarity/stance classification, claim coverage, numeric consistency and rationale. It does not rely on an external model or token overlap alone.

### 15.11 Constrained semantic-contract closure (Prompt 14A-C1-R1-R1-C1-R1-C1-R1-R1-R1)

> **Superseded status (2026-11-16):** The table below is preserved as a historical record. Its 20/20 SEM tally and SEM-07 claim were disproved by the independent reproduction of D-991, D-992 and D-993, each of which passed all 55 lexical checks. The controlled typed-contract implementation and its actual results are recorded in §18. Nothing in this historical table is a current acceptance claim.

This section records the final, uniquely numbered closure of the semantic-validation correction. It supersedes no historical gate; the `SEM-` identifiers are unique to this correction.

| Gate | Acceptance objective | Actual result | Status |
|---|---|---|---|
| SEM-01 | Final correction archive present and indexed | 28,645 bytes; SHA-256 `f8ce85ce…`; INDEX row and validator check `14A-55` | PASS |
| SEM-02 | Deterministic, source-backed semantic contract for both controlled B-04 clauses | `_semantic_contract_violation` implements the documented rule set; no external model at validation runtime | PASS |
| SEM-03 | Exact D-990 exception attack rejected | Fixture 129 — `semantic-contract` | PASS |
| SEM-04 | IEEE-754 and alternative-representation permissions rejected | Fixtures 130, 136, 137 | PASS |
| SEM-05 | binary32, binary64 and single-precision permissions rejected | Fixtures 131–133 | PASS |
| SEM-06 | Treasury/scope exceptions and fractional-carry permissions rejected | Fixtures 134, 135, 138 | PASS |
| SEM-07 | Unknown material arithmetic wording fails closed | Unclassified material clauses and exceptions rejected rather than accepted | PASS |
| SEM-08 | Positive Category A/B/C fixtures preserved | Fixtures 80, 81, 118 | PASS |
| SEM-09 | All 53 prior checks preserved | 53 prior; 55 total | PASS |
| SEM-10 | All 128 prior self-tests preserved | 128 prior; 138 total | PASS |
| SEM-11 | B-04 source hashes unchanged | `bb1090cc…` / `3025cc44…` | PASS |
| SEM-12 | Production amendment manifest unchanged and empty | `amendments: []` | PASS |
| SEM-13 | 295 formulas, 393 parameter records and 20 B-03 carry-ins preserved | 295/295; 393/393; 20/20 | PASS |
| SEM-14 | Status vocabulary and owner-reserved boundaries preserved | No promotion; `UD-017`, `UD-040`–`UD-060` unchanged | PASS |
| SEM-15 | Documentation links and prompt index pass | Final totals recorded in the current QA report and progress log | PASS |
| SEM-16 | Final project validator, decision-register and next-action tests pass | `validate_final.py` ALL CHECKS PASSED; 12/12; 27/27 | PASS |
| SEM-17 | Inherited validator failures remain visible and unchanged | Four scripts exit 1; not edited | PASS |
| SEM-18 | No implementation, balance change or Git operation | None | PASS |
| SEM-19 | Historical records and earlier archives preserved | Dated snapshots retained; only current-position status updated | PASS |
| SEM-20 | Final Prompt 14A handoff prepared | [Log §107](06_stage_2_progress_log.md) and handoff | PASS |

**SEM gate tally:** 20 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED.

**Final status (2026-11-16):**

**PROMPT 14A — OPEN / NOT READY FOR FINAL OWNER ACCEPTANCE UNTIL THE FINAL SEMANTIC-VALIDATION CORRECTION IS INDEPENDENTLY VERIFIED.** *(Status at the start of this correction; superseded by the verified result below.)*

**PROMPT 14A — the final semantic-validation correction is independently verified: 55/55 checks, 138/138 self-tests, 20/20 SEM gates. PROMPT 14A IS READY FOR FINAL OWNER ACCEPTANCE. Owner acceptance has not been granted and is not claimed.**

**PROMPT 14B — NOT AUTHORIZED / NOT STARTED. Only the owner may authorize Prompt 14B.**

**PROMPT 14A-C1 — COMPLETE.**

**PROMPT 14A-C1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1-C1 — COMPLETE.**

**Final status (historical snapshots — preserved, superseded by the 2026-11-16 block above):**

**PROMPT 14A — NUMERICAL FOUNDATION COMPLETE.**

**PROMPT 14A-C1 — COMPLETE.**

**PROMPT 14A-C1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1-C1 — COMPLETE.**

**PROMPT 14A — READY FOR FINAL OWNER ACCEPTANCE.**

**NEXT ACTION: AWAIT EXPLICIT OWNER AUTHORIZATION OF PROMPT 14B.**

**Final status (second historical snapshot — pre-14A-C1-R1 record):**

**PROMPT 14A — DOCUMENTATION AND NUMERICAL FOUNDATION COMPLETE.**

**PROMPT 14A-C1 — COMPLETE.**

**PROMPT 14A-C1-R1 — COMPLETE.**

**PROMPT 14A-C1-R1-R1 — COMPLETE.**

**PROMPT 14A — READY FOR FINAL INDEPENDENT OWNER ACCEPTANCE.**

**NEXT ACTION: AWAIT THE OWNER'S EXPLICIT AUTHORIZATION OF PROMPT 14B.**

---

## 16. Subsequent Prompt 14 subphase ownership — RESERVED

| Subphase | Scope | Preconditions | Status |
|---|---|---|---|
| 14B | Economy, resources, income and treasury | 14A owner accepted; owner authorization 2026-11-17 | **COMPLETE at the documentation/numerical-analysis level (2026-11-17); no balance acceptance** |
| 14C | Cities, infrastructure, production and research | 14B or parallel authorization | **NOT AUTHORIZED** |
| 14D | Population and domestic politics | 14B/14C inputs | **NOT AUTHORIZED** |
| 14E | Trade and markets | 14B reference prices; G-5 for fees | **NOT AUTHORIZED** |
| 14F | Diplomacy | 14A; B-08 values | **NOT AUTHORIZED** |
| 14G | Alliances | Owner decisions `UD-040`/`UD-043`/`UD-044`/`UD-046` | **NOT AUTHORIZED / partially BLOCKED** |
| 14H | Warfare, Operations Points and settlements | 14B economy; `F-WR-001` pair | **NOT AUTHORIZED** |
| 14I | World events, objectives, rankings and progression | 14B; `UD-050`/`UD-051` | **NOT AUTHORIZED** |
| 14J | Fair play, player protection and anti-abuse calibration | Owner decisions `UD-053`/`UD-056`/`UD-059` | **NOT AUTHORIZED / partially BLOCKED** |
| 14K | Consolidated balance, worked examples and balance report | 14B–14J | **NOT AUTHORIZED** |

Each subphase must re-run this validator, update the affected inventory rows and preserve the status vocabulary. No subphase may treat this document as approval of the game's balance.

---

## 17. Revision history

| Version | Date | Change | Evidence |
|---|---|---|---|
| 0.1 | 2026-11-13 | Prompt 14A foundation: canonical B-14 created at the D-198 path; 295 active formulas reconciled; parameter map; 20 B-03 carry-ins; status vocabulary; timing and dependency matrices; QA baseline; 14A validator | [log §98](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.2 | 2026-11-13 | Prompt 14A-C1: per-record source reconciliation of all 393 parameter records; validator extended to 35 checks and 35 self-tests; four audited mutations and eight further mutations rejected; P14A-06 corrected to 393; documentation-link totals and exit-code evidence corrected | [log §99](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.3 | 2026-11-13 | Prompt 14A-C1-R1: unit, authority, status, timing, precision/rounding and evidence metadata source-validated across 393 records; validator 41 checks and 48 self-tests; nine audited mutations plus further cases rejected; coverage matrix added; B-03/FP metadata provenance corrected | [log §100](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.4 | 2026-11-13 | Prompt 14A-C1-R1-R1: constant precision/rounding conventions source-validated for B-04…B-07; owner-reserved flags source-validated across applicable records; validator 44 checks / 64 self-tests; nine R1 mutations and final Treasury mutations rejected; C1-R1 and R1-R1 archives reconciled | [log §101](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.5 | 2026-11-13 | Prompt 14A-C1-R1-R1-C1: F-EC-000b and F-EC-000f semantic source contracts protected; final link totals reconciled; validator 47 checks / 78 self-tests; final prompt archived verbatim | [log §102](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.6 | 2026-11-13 | Prompt 14A-C1-R1-R1-C1-R1: D-014 amendment authorization evidence enforced through a controlled manifest and decision-register chain; validator 49 checks / 94 self-tests; final closure archive added | [log §103](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.7 | 2026-11-13 | Prompt 14A-C1-R1-R1-C1-R1-C1: substantive D-014 decision evidence enforced through structured DECISIONS.md parsing; false D-998 pattern rejected; validator 51 checks / 118 self-tests; final QA link totals reconciled | [log §104](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.8 | 2026-11-13 | Prompt 14A-C1-R1-R1-C1-R1-C1-R1: evidence-content relevance enforced through clause-specific authorized loci, quoted excerpts and supports-claim overlap; the fair-play D-998 attack is rejected; validator 52 checks / 124 self-tests | [log §105](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 0.9 | 2026-11-13 | Prompt 14A-C1-R1-R1-C1-R1-C1-R1-R1: evidence polarity/stance classification added; prohibition-as-permission (D-999), negation reversal, partial coverage and basis-point scope contradictions rejected; validator 53 checks / 128 self-tests | [log §106](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |
| 1.0 | 2026-11-16 | Prompt 14A-C1-R1-R1-C1-R1-C1-R1-R1-R1: deterministic constrained semantic contracts for F-EC-000b and F-EC-000f; exact D-990 exception, IEEE-754/binary32/binary64/single-precision, fractional-carry, alternative-representation and scope exceptions rejected; unknown material wording fails closed; validator 55 checks / 138 self-tests; final archive indexed; §15.11 SEM closure added | [log §107](06_stage_2_progress_log.md); [QA report](22_numerical_baseline_qa_report.md) |

| 1.1 | 2026-11-16 | Prompt 14A controlled semantic-contract implementation: typed contracts `NC-F-EC-000b` and `NC-F-EC-000f` (v1.0.0) adopted by D-238; strict schema, canonical lexicon, deterministic projections, evidence review role, separate evidence and D-014 authority gates, typed proposition diffs and a fail-closed ingest path; the legacy lexical semantic blocklist is retired as an acceptance gate and retained as a diagnostic; numerical validator 64 checks / 150 self-tests; contract validator 9/9 checks and 83/83 regression tests (D-991, D-992 and D-993 rejected with three paraphrases each) | [log §108](06_stage_2_progress_log.md); [implementation report](../qa_backups/14A_SEMANTIC_CONTRACT_IMPLEMENTATION_REPORT.md) |

| 1.2 | 2026-11-16 | Prompt 14A-C2 trusted-input and semantic-gate hardening: strict seven-field amendment request; fixed `TrustedContext`; path and symlink protection; trusted decision and owner-authorization sources; evidence revalidation; complete span coverage and canonical single-sentence rendering; four independent gates; new 46-test security suite; 64/64 checks, 150/150 self-tests, 9/9 contract checks, 83/83 contract tests | [log §109](06_stage_2_progress_log.md); [C2 report](../qa_backups/14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md) |

| 1.3 | 2026-11-17 | Prompt 14A-C3 final QA reconciliation: contract-level metadata diff with previous/proposed values and gate-derived classifications; complete 150/150 numerical self-test executed in 1m00.094s after safe memoization; accurate Git status and complete C3 file inventory; C3 closeout report; no numerical or architectural change | [log §110](06_stage_2_progress_log.md); [C3 report](../qa_backups/14A_FINAL_QA_CLOSEOUT_REPORT.md) |

| 1.4 | 2026-11-17 | Prompt 14A-C4 final Git-status and handoff closeout: handoff banner reconciled to 17 November; live Git counts 17 modified tracked / 38 untracked / 55 individual / 48 display / 0 staged; audit 152/36/188 recorded as an unreproduced audit-environment observation; generated Python cache artifacts separately inventoried; no source or numerical change | [log §111](06_stage_2_progress_log.md); [precommit report](../qa_backups/14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md) |
| 1.5 | 2026-11-17 | Prompt 14B B-04 economy reconciliation: 47 B-04 formulas and 49 parameter records re-verified; B-06 public-service cost and B-05 research modifiers/facility upkeep adopted into B-04 (D-240/D-241); Example 4 reconciled to the B-05 farm and the `net economic result` definition published (D-242); 30-turn reference model and cross-system matrix recorded without retuning any value (D-243); 295/393/20 counts preserved; 14B validator added | [log §113](06_stage_2_progress_log.md); [14B report](25_prompt_14B_b04_economy_completion_report.md); [QA report](22_numerical_baseline_qa_report.md) |

**End of B-14 v1.5 (Prompt 14B B-04 economy reconciliation).**

---

## 18. Superseding semantic-contract implementation status (2026-11-16) — PROMPT 14A OPEN

### 18.1 What the previous record did not establish

The historical §15.11 table reports 55/55 lexical checks and 20/20 SEM gates, including SEM-07 (“unknown material arithmetic wording fails closed”). That count was real, but it was not proof of semantic completeness. An independent reproduction constructed three amendments that kept the literal baseline sentences and appended an alternative numerical vocabulary:

| Case | Attack class | Historical result |
|---|---|---|
| D-991 | Radix-two exponent/significand encoding permission | Accepted by all 55 lexical checks |
| D-992 | Sign, exponent and mantissa representation permission | Accepted by all 55 lexical checks |
| D-993 | Residual sub-unit amounts preserved between turns | Accepted by all 55 lexical checks |

The lexical gate was a blocklist over known surface forms. The three attacks used forms outside the blocklist, so the gate returned “no violation”. The historical SEM-07 claim is therefore **disproved**, not reinterpreted. The original §15.11 table and the original progress-log §107 remain preserved as historical records.

### 18.2 Implemented architecture

The controlled clauses are now represented by typed, machine-readable contracts under [`22_numerical_contracts/`](22_numerical_contracts/index.json):

| Artifact | Role |
|---|---|
| `index.json` | Registry, adoption decision, preserved baseline counts, source-document fingerprints and the cross-cutting arithmetic-authority record |
| `schema.json` | Strict, closed schema; unknown fields, enumerations, references and missing mandatory metadata are rejected |
| `lexicon.json` | Reviewed canonical concepts and surface forms; unknown material terms fail closed |
| `F-EC-000b.contract.json` | Five propositions for integer quantities, division rounding, negative binary-floating-point representation, basis-point percentages and the unresolved cross-turn remainder question |
| `F-EC-000f.contract.json` | Five propositions for provisional calibration, v1.0-to-v1.1 carry, observed-price denial, balance-claim denial and revision authority |
| `evidence_mappings.json` | Draft evidence catalogue with source hashes, sections, excerpts, scope and review state; every production mapping is `NOT_REVIEWED` |
| `projections/` | Deterministic projection templates whose rendered output equals the preserved B-04 clauses after normalization |

The validator [`14A_contract_validator.py`](../qa_backups/14A_contract_validator.py) implements schema validation, typed proposition diffs, deterministic rendering, 100 % material coverage, an evidence gate and a separate D-014 authority gate. The regression suite is [`test_14A_contract_validator.py`](../qa_backups/test_14A_contract_validator.py). Nine new checks (`14A-56`–`14A-64`) integrate the contract results into the numerical foundation validator; checks `14A-01`–`14A-55` and the 138 legacy self-tests are preserved.

### 18.3 Corrected authority classification

B-14 §2.1 previously associated integer arithmetic with D-008/D-009/D-010. The corrected table separates the two matters:

- hosting, deployment, scheduler and platform direction remain under **D-008 / D-009 / D-010**;
- integer arithmetic, whole-unit precision and basis-point percentages are **Category B** design rules under **D-045 / D-064**.

The binary-floating-point prohibition is therefore not owner-reserved Category A. The validator enforces the classification: every F-EC-000b arithmetic proposition must be Category B, not owner-reserved, and must cite D-045 and D-064. A Category B amendment cannot downgrade an owner-reserved proposition, and any authority-classification change requires authentic Category A owner authorization.

### 18.4 Evidence reviewer accountability

The registry defines the **Independent Human Evidence Reviewer** role. A reviewed `SUPPORTS` mapping must record the reviewer identity, role, date, source document and full SHA-256, exact section and excerpt, proposition identifier, covered scope and conditions, classification, rationale and status. The reviewer must be a human who is neither the amendment author nor the implementation actor.

No human reviewer has approved any mapping in this pass. All production mappings remain `NOT_REVIEWED`; their proposed classifications are drafts only. Consequently **no semantic amendment requiring evidence can pass in production**. The validator’s positive evidence path is exercised only with clearly labelled synthetic test fixtures; production mode rejects fixture-only reviews and fixture-only owner authorizations. No owner acceptance or human review is claimed.

### 18.5 Executed results

| Check | Actual result |
|---|---|
| Numerical foundation validator | **64/64 checks; 150/150 self-tests** |
| Controlled-contract validator | **9/9 checks** |
| Contract regression suite | **83/83 tests** |
| D-998 / D-999 / D-990 | Rejected; three paraphrases each |
| D-991 / D-992 / D-993 | Rejected; three paraphrases each; D-993 has no reviewed `SUPPORTS` mapping |
| Positive fixtures | Unchanged baseline, wording clarification, typed Category B, Category C, owner-authorized Category A (test-only proposition) and B-09 F-AL-006 within-turn accrual accepted under their stated conditions |
| B-04 hashes | `bb1090cc…` / `3025cc44…` unchanged |
| Production manifest | `amendments: []` |
| 295 formulas / 393 parameter records / 20 B-03 carry-ins / nine registers | Preserved |
| Prompt 14B | **NOT AUTHORIZED / NOT STARTED** |

The full executed evidence, file list and negative/positive results are in the [implementation report](../qa_backups/14A_SEMANTIC_CONTRACT_IMPLEMENTATION_REPORT.md).

### 18.6 Current status — the five claims are separate

| Claim | Status |
|---|---|
| Implementation complete | **Yes** — contracts, schema, lexicon, renderer, validator, regression suite and integration exist and run |
| Documentation complete | **Yes for this implementation pass** — current status, roadmap, QA report, handoff, context and prompt archive reconciled |
| Validation passed | **Yes at the documentation/tooling level** — the executed totals above; no gameplay, balance, runtime or human semantic judgment is proven |
| Owner acceptance | **PENDING** — not requested by this pass and not granted |
| Prompt 14A | **OPEN** — implementation and validation are complete, but owner acceptance is outstanding |
| Prompt 14B | **NOT AUTHORIZED / NOT STARTED** |

### 18.7 Prompt 14A-C2 — trusted amendment inputs and semantic-gate hardening (2026-11-16)

The Project X (106) audit confirmed the typed-contract architecture and reproduced five remaining defects in the production amendment path. All five are now closed.

| Finding | Root cause | Correction |
|---|---|---|
| Caller-controlled trusted inputs | `validate_amendment()` accepted request-supplied baseline contracts, schema, lexicon, evidence mappings, decision text, owner authorizations and template text | A fixed `TrustedContext` loads every trusted input from canonical repository paths; the public entry point accepts only a strict seven-field request and rejects every override or alias with `CONTRACT_TRUSTED_INPUT_OVERRIDE` |
| Incomplete material coverage | `material_coverage()` located expected fragments but ignored material before, between and after them | Complete span accounting detects gaps, missing pieces, duplicates, overlapping spans and trailing material; canonical rendering is derived only from typed fields |
| Evidence not revalidated on the amendment path | Production validation checked the registry, but amendment acceptance used caller-supplied mappings | Every referenced mapping is revalidated against the actual source bytes, hash, section, excerpt, proposition, scope, classification and review metadata during amendment acceptance |
| Authority substitution | The request could supply decision-register text and owner-authorization data; a fabricated D-940 was accepted | Decision authority and owner authorizations come only from the trusted `DECISIONS.md` and the trusted index; fabricated D-940 is rejected with `CONTRACT_AUTHORITY_MISMATCH`, and register/owner injection with `CONTRACT_TRUSTED_INPUT_OVERRIDE` |
| Inaccurate Git-status reporting | The prior report quoted a collapsed `git status --short` display count as a file count | The C2 report records the live modified/untracked file counts, the display-line count and the read-only snapshot comparison; no Git operation is performed |

The production amendment path now executes four independent gates: contract integrity, evidence integrity, D-014 authority and complete comparison. A failure in one gate is not compensated by another. The renderer is canonical: structural prefixes are restricted to the clause identity, title and numerical status; every material fragment is a single sentence tied to a typed proposition; an arbitrary template cannot be supplied.

**Executed C2 results.** Numerical validator **64/64 checks and 150/150 self-tests**; contract validator **9/9 checks**; original contract suite **83/83**; new trusted-input and semantic-gate suite **46/46**. The exact insertion attack “B-04 binary floating-point calculations are permitted” is rejected at the beginning, middle, between propositions, end and after trailing qualifications; D-991/D-992/D-993 and D-998/D-999/D-990 remain rejected with three paraphrases each; all positive fixtures remain accepted in their documented fixture contexts. The full results, attack table and Git reconciliation are in the [C2 hardening report](../qa_backups/14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md).

**Limitations preserved.** Production evidence mappings remain `NOT_REVIEWED`; no human reviewer identity or attestation is fabricated. The Category A positive fixture uses a clearly labelled synthetic fixture context and is not project owner authorization. The validator can verify the integrity of review metadata but cannot cryptographically prove human semantic judgment. A real reviewer and a real owner authorization require a future governance act. Prompt 14A remains **OPEN** and Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**.

### 18.8 Prompt 14A-C3 — final QA reconciliation and documentation closeout (2026-11-17)

The Project X (107) audit confirmed the C2 fixes and identified four remaining closeout issues. All four are resolved without changing the contract model or numerical rules.

**Contract-level metadata diff.** `diff_contracts()` now emits `metadata_changes` for `contract_version`, `effective_decision` and `lifecycle_status`, each with the previous value, proposed value, whether it changed and a classification of `UNCHANGED`, `AUTHORIZED`, `PROVISIONAL`, `UNAUTHORIZED` or `INVALID`. The classification is derived after the contract, evidence and D-014 authority gates from their actual results; it never makes a metadata change valid. The authority gate now independently rejects a candidate whose `effective_decision` does not equal the request `decision_ref`. The contract, evidence, authority and comparison gates remain separate.

**Numerical self-test reproducibility.** The self-test was re-executed to completion. The baseline run took **2m23.817s**; safe text-hash memoization of immutable parsers and reads reduced the complete run to **1m00.094s** without removing, skipping or weakening any case. All **150/150** numerical self-tests executed and passed; exit status 0; repeated execution is deterministic. The caches are keyed by content hashes, so mutation fixtures still exercise the changed text.

**Git-status reconciliation.** The live repository was inspected read-only with `git status --short --untracked-files=all`. The actual state is **17 modified tracked paths, 36 untracked individual files, 53 individual paths, 46 default display lines and 0 staged changes**. The audit's 152/33/185 figures are not reproduced by `git status --short --untracked-files=all`, `git diff --name-status` or the snapshot `.git` index against the live worktree in this environment. The difference is treated as an audit-environment measurement (line-ending/filter state or a different Git index), not as the live count; no file was staged, reverted or discarded to force agreement. The previous 40/50 figure was a display-line count, not an individual-path count.

**File inventory.** The C3 report contains a complete file-level inventory with previous and final SHA-256 for every C3-created or C3-modified file. Earlier C2 changes remain attributed to C2; no earlier change is reclassified as C3.

**Executed results.** Numerical validator 64/64 checks and 150/150 self-tests; contract validator 9/9; original contract suite 83/83; C2 security suite 46/46; C3 metadata suite 8/8; decision-register tests 12/12; next-action tests 27/27; documentation-link validator 0 unresolved. The 295 formulas, 393 parameter records, 20 B-03 carry-ins, nine registers, both B-04 hashes, the empty production manifest and D-014/D-238/D-239 are preserved. All production evidence mappings remain `NOT_REVIEWED`; no human review or owner authorization is claimed.

**Status.** Prompt 14A remains **OPEN**; owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**. The consolidated closeout evidence is in the [C3 final QA closeout report](../qa_backups/14A_FINAL_QA_CLOSEOUT_REPORT.md).

### 18.9 Prompt 14A-C4 — final Git-status and handoff closeout (2026-11-17)

C4 made no source, formula, parameter, contract or validator change. It reconciles reporting and handoff state before the owner's planned commit.

**Git status.** The exact command `git status --porcelain=v1 --untracked-files=all` was executed read-only on 2026-11-17. The live repository reports:

| Category | Count |
|---|---:|
| Modified tracked paths | **17** |
| Added tracked paths | **0** |
| Deleted tracked paths | **0** |
| Renamed tracked paths | **0** |
| Staged changes | **0** |
| Untracked individual files | **38** |
| Total individual paths | **55** |
| Default `git status --short` display lines | **48** |

The 17 modified tracked paths are the total accumulated tracked changes, not C3/C4-specific changes. C3 changed 14 files and created 3; C4 changes documentation only. The 38 untracked individual files include the 33 pre-existing Prompt 14A artifacts, the 3 C3-created files, the C4 prompt archive and the C4 precommit report.

The Project X (108) audit's **152 modified / 36 untracked / 188 total / 0 staged** is preserved as an audit-environment observation. It is not reproduced by the live Git index or by the Project X (108) snapshot `.git` index against the live worktree in this environment. The audit's 36 untracked count matches the pre-C4 live count; C4 later added two files, so the final untracked count is 38. The 152 modified count does not match. The difference is attributed to the audit environment's Git index, line-ending/filter normalization or a different measurement. The live counts above are the authoritative repository-wide record; no file was staged, reverted or discarded to force agreement.

**Handoff banner.** `docs/AI_HANDOFF.md` now begins with **CURRENT PROJECT POSITION — 17 NOVEMBER 2026**, stating Prompt 13A–13D owner acceptance, the Prompt 14A numerical foundation, the semantic-contract architecture, C2/C3 implementation, C4 closeout, Prompt 14A awaiting formal owner acceptance, and Prompt 14B unauthorized. The November 16 semantic-contract banner is preserved as **SUPERSEDED / HISTORICAL**.

**Generated cache artifacts.** The two Python bytecode cache files modified during the 14A work are `docs/qa_backups/__pycache__/14A_contract_validator.cpython-312.pyc` and `docs/qa_backups/__pycache__/14A_validate_numerical_foundation.cpython-312.pyc`. They are generated artifacts, ignored by `.gitignore` (`__pycache__/`, `*.pyc`), not tracked and not substantive source changes. They were not deleted or manipulated; the tracking policy was not changed.

**Validation.** C4 changed documentation only. The cheap validators were executed: documentation links 0 unresolved; `validate_final.py` ALL CHECKS PASSED; `test_decision_registers.py` 12/12; `test_next_action.py` 27/27; prompt archive/index valid. The expensive suites (150 numerical self-tests, 83 contract tests, 46 C2 tests, 8 C3 tests, 64/9 validators) were last executed to completion in C3 and were not rerun after documentation-only changes; they remain previously independently verified, not newly executed in C4.

**Status.** Prompt 14A remains **OPEN**; independent verification is recorded; formal owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**. The precommit report is [14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md](../qa_backups/14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md).

**Exact next action:** owner review and commit of the accumulated changes, then formal acceptance or rejection of Prompt 14A; Prompt 14B remains subject to separate explicit owner authorization.

---

## 19. Prompt 14B — B-04 economy reconciliation status (2026-11-17)

**Status:** **COMPLETE at the documentation, numerical-analysis and document-validation level.** No B-04 value was retuned; no formula was added, renumbered or retired; the 295 active identifiers, 393 parameter records and 20 B-04 worked examples are preserved. No runtime, database, scheduler or player exists.

### 19.1 What was reconciled

| Area | Result | Evidence |
|---|---|---|
| 47 active B-04 formulas | 36 executable + 11 analytical/governance identifiers reconciled against the register; F-EC-002a published as a full field table; F-EC-004/012/014 consume the B-05 modifiers; F-EC-018's `operating` defined | [14B report §2](25_prompt_14B_b04_economy_completion_report.md) |
| 49 B-04 parameter records | every record retains `PROVISIONAL VALUE`; two metadata defects corrected (generator timing P3.7 → P3.4; unit vectors made explicit); no value promoted | [14B report §2.3](25_prompt_14B_b04_economy_completion_report.md) |
| Starting economy | 1,500 crowns; 310 units; 600 book; 2,100 wealth; 1,690 free; standard full turn closes at **1,499** with a net economic result of **+77** | 14B Example H |
| Four production chains | margins, power, capital and full cost re-derived; refining's actual standard-start margin is **−12**, not 0 | 14B §4.5 |
| 11 resources | conservation identities reproduced in Examples A/G and the 30-turn model | 14B §4.7 |
| Cross-system matrix | 35 dependency-matrix rows: 27 `VERIFIED CONSISTENT`, 4 `VERIFIED WITH DOCUMENTED LIMITATION`, 4 `CONTRADICTION IDENTIFIED`, 0 `NOT YET VERIFIED` (sum 35); separately, the 18-entry contradiction register and the 2 B-06 `OUTSIDE PROMPT 14B AUTHORITY` items are not part of the 35. | 14B §5 |
| 20 + 8 worked examples | 20 recalculated; A–G and H added; all reproducible | 14B §6 |
| 30-turn reference model | gross money creation fails by 24 crowns; net passes; idle fails both | 14B §4.9 |
| Decisions | D-240…D-243 / DD-286…DD-289; no owner-reserved matter resolved | D-014 |

**14B-C1 closeout note (2026-11-17).** The 49 B-04 parameter records now carry explicit D-014 **Category C** metadata in [the parameter inventory §6.1](22_numerical_parameter_inventory.md) (0 A/B/D, 0 unresolved; no value, status or source ID changed). The 35-row dependency matrix was recounted at **27 `VERIFIED CONSISTENT` / 4 `VERIFIED WITH DOCUMENTED LIMITATION` / 4 `CONTRADICTION IDENTIFIED` / 0 `NOT YET VERIFIED`**, with the 18-entry contradiction register and the 2 B-06 `OUTSIDE PROMPT 14B AUTHORITY` items kept separate. The QA report carries the 17-category evidence crosswalk (§8). The C1 corrections changed no numerical value and no formula identity.

### 19.2 What was not established

No balance acceptance, no playtest, no runtime validation and no economic simulation beyond the deterministic reference model. The standard start is cash-neutral (−1 crown/turn), oil is the binding input, power is overbuilt at the start, and refining is the weakest chain; these are recorded as findings, not retuned. The two external B-06 reference defects (`DMP-135` P3.7/P3.8 wording; `DMP-097a` `ECN-081` citation) remain **OUTSIDE PROMPT 14B AUTHORITY**. `UD-040` and `UD-046` remain Open.

### 19.3 Next subphase

Prompt 14C is **NOT AUTHORIZED**. Only the owner may authorize it.
