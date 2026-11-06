# B-11 world events, objectives, rankings and progression — formula register

**Version:** 1.0 · **Created:** 2026-11-05 · **Stage 2, Prompt 11B** · **11B-C2 correction; C3 acceptance 2026-11-05**
**Status:** **Specification complete at the documentation level. Unimplemented, uncalibrated and untested.**
**Authority.** This register is the authoritative statement of every B-11 calculation. The [B-11 rulebook](18_world_events_objectives_rankings_progression.md) defines the rules; where it describes arithmetic in prose, this register's expression governs. If the two diverge, this register wins and the rulebook is corrected.
**Companions.** [B-11 rulebook](18_world_events_objectives_rankings_progression.md) · [acceptance crosswalk](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md) · [acceptance source artifact](18_world_events_objectives_rankings_progression_acceptance_source.md) · [11A research](research/11A_world_events_objectives_rankings_progression_research.md) · [requirements](03_requirements_traceability.md) · [decisions](04_approved_and_provisional_decisions.md).

**Status of values.** B-11 structural formulas and inherited approved constants retain their documented classifications and approval status. All unapproved numerical calibration parameters remain provisional and require Prompt 14 review. Structural formulas containing provisional parameters are structurally specified but are not numerically finalized. A structural formula may contain a provisional constant; the structure is fixed, the constant is not. No value in this register is a balance decision. Field 20 is authoritative for each formula; the derived counts are stated in §1 and are checked against field 20 by `B11-53`.

---

## 1. Formula inventory

| ID | Name | Domain | Status | Main rule |
|---|---|---|---|---|
| `F-WEP-001` | Event occurrence key | Event | Structural | WEP-087 |
| `F-WEP-002` | Event eligibility predicate | Event | Structural | WEP-132 |
| `F-WEP-003` | Event relative-band membership | Event | Structural + provisional bounds | WEP-133, WEP-155 |
| `F-WEP-004` | Participation cap check | Event | Structural + provisional cap | WEP-148 |
| `F-WEP-005` | Event progress | Event | Structural | WEP-159 |
| `F-WEP-006` | Event completion predicate | Event | Structural | WEP-181 |
| `F-WEP-007` | Event contribution share | Event | Structural | WEP-160 |
| `F-WEP-008` | Event reward qualification | Event | Structural | WEP-163 |
| `F-WEP-009` | Occurrence cap | Event | Structural + provisional cap | WEP-123 |
| `F-WEP-010` | Teardown boundaries | Event | Structural + provisional lag | WEP-185 |
| `F-WEP-011` | Event effect magnitude | Event | Provisional | WEP-169 |
| `F-WEP-012` | Participation freeze boundary | Event | Structural | WEP-155 |
| `F-WEP-013` | Event result order | Event | Structural | WEP-160 |
| `F-WEP-014` | Event notability flag | Event | Structural | WEP-193 |
| `F-WEP-015` | Objective offer eligibility | Objective | Structural | WEP-254 |
| `F-WEP-016` | Outstanding-objective count | Objective | Structural + provisional cap | WEP-254 |
| `F-WEP-017` | Objective progress | Objective | Structural | WEP-265 |
| `F-WEP-018` | Objective progress percentage | Objective | Structural | WEP-283 |
| `F-WEP-019` | Tier completion | Objective | Structural | WEP-237 |
| `F-WEP-020` | Objective completion predicate | Objective | Structural | WEP-225 |
| `F-WEP-021` | Seasonal objective points | Objective | Provisional weights | WEP-214 |
| `F-WEP-022` | Difficulty class lookup | Objective | Structural | WEP-291 |
| `F-WEP-023` | Objective reward eligibility | Objective | Structural | WEP-520 |
| `F-WEP-024` | Repeat cooldown | Objective | Structural + provisional interval | WEP-298 |
| `F-WEP-025` | Objective expiry boundary | Objective | Structural + provisional limit | WEP-226 |
| `F-WEP-026` | Individual-equivalence check | Objective | Structural | WEP-261 |
| `F-WEP-027` | Ranking percentile | Standing | Structural | WEP-324 |
| `F-WEP-028` | WSE state | Standing | Structural | WEP-367 |
| `F-WEP-029` | Development index | Standing | Provisional weights | WEP-327 |
| `F-WEP-030` | Economic output index | Standing | Structural + provisional weights | WEP-328 |
| `F-WEP-031` | Resilience index | Standing | Structural + provisional window | WEP-329 |
| `F-WEP-032` | Housing sufficiency | Standing | Structural | WEP-330 |
| `F-WEP-033` | Institutional continuity | Standing | Structural + provisional weights | WEP-331 |
| `F-WEP-034` | Diplomatic activity | Standing | Structural | WEP-332 |
| `F-WEP-035` | Military participation | Standing | Structural | WEP-333 |
| `F-WEP-036` | Defensive performance band | Standing | Structural + provisional bands | WEP-334 |
| `F-WEP-037` | Alliance collective aggregate | Standing | Structural + `k` | WEP-335 |
| `F-WEP-038` | Rank assignment and tie groups | Standing | Structural | WEP-392 |
| `F-WEP-039` | Achievement qualification | Progression | Structural | WEP-433 |
| `F-WEP-040` | Milestone geometric threshold | Progression | Structural + provisional constants | WEP-449 |
| `F-WEP-041` | Milestone level | Progression | Structural | WEP-449 |
| `F-WEP-042` | Honour closure check | Progression | Structural | WEP-464 |
| `F-WEP-043` | Season window and reset scope | Progression | Structural + provisional length | WEP-465 |
| `F-WEP-044` | Scope classification | Progression | Structural | WEP-031 |
| `F-WEP-045` | Reward qualification predicate | Reward | Structural | WEP-515 |
| `F-WEP-046` | Reward amount and cap | Reward | Provisional | WEP-542 |
| `F-WEP-047` | Reward dedupe key | Reward | Structural | WEP-510 |
| `F-WEP-048` | Contribution allocation — **RETIRED** (no lawful use case) | Reward | Retired | — |
| `F-WEP-049` | Conservation check | Reward | Structural | WEP-539 |
| `F-WEP-050` | Chronicle notability flag | History | Structural | WEP-681 |

**Counts (derived from field 20, not from prose).** 50 formula IDs: **49 active + 1 retired** (`F-WEP-048`). Active categories: 14 event, 12 objective, 12 standing, 6 progression, 4 reward, 1 history. **Structural (active): 43. Provisional: 6** — `F-WEP-011`, `F-WEP-021`, `F-WEP-029`, `F-WEP-030`, `F-WEP-033`, `F-WEP-046`. Of the 43 active structural formulas, **20 contain a Prompt 14 parameter** (`F-WEP-003`, `004`, `005`, `007`, `009`, `010`, `012`, `015`, `016`, `019`, `024`, `025`, `031`, `034`, `035`, `036`, `040`, `042`, `043`, `050`) and **23 contain no calibration parameter**. The 11B-C2 correction retired `F-WEP-048` after finding no authorized use case; it did not reclassify any other formula. Undefined variables: 0. Duplicate identifiers: 0.

---

## 2. The 20 mandatory fields

| # | Field | Meaning |
|---|---|---|
| 1 | **Identifier** | Stable `F-WEP-###` code, never reused |
| 2 | **Name** | Short human name |
| 3 | **Domain** | Event, objective, standing, progression, reward or history |
| 4 | **Purpose** | What decision the calculation supports |
| 5 | **Expression** | Exact arithmetic or logical expression |
| 6 | **Variables** | Every variable, type and valid range |
| 7 | **Input source** | Authoritative subsystem and field |
| 8 | **Units** | Integer, basis points, turns, count, boolean or enum |
| 9 | **Valid range** | Input bounds |
| 10 | **Output range** | Result bounds |
| 11 | **Rounding** | Floor, ceiling or largest remainder |
| 12 | **Caps** | Upper bounds applied |
| 13 | **Floors** | Lower bounds applied |
| 14 | **Phase** | P6 step |
| 15 | **Snapshot** | Frozen baseline or archived snapshot |
| 16 | **Missing data** | Behaviour on absence |
| 17 | **Invalid input** | Fail-closed behaviour and code |
| 18 | **Example** | One worked case |
| 19 | **Boundary case** | Minimum, maximum or equality |
| 20 | **Provisional status / calibration owner** | Structural, provisional, Prompt 14 |
| — | **Main rule reference** | The `WEP-` rule(s) |

The register also records the **audit event** and **privacy** where they are not obvious; a formula inherits the rule's audit and privacy unless its entry says otherwise.

---

## 3. Global conventions

**F-WEP-000a — Integer arithmetic.** All quantities are integers. Percentages and shares are basis points (`bp`, 10,000 = 100%). There is no floating-point step; a displayed decimal is a rendering of an integer.

**F-WEP-000b — Division.** Integer division floors toward zero unless the expression says `ceil`. Every formula with a denominator defines its zero-denominator branch.

**F-WEP-000c — Clamping order.** Clamp after the final arithmetic step unless the entry states an intermediate clamp. A clamped value is never fed back into the same formula in the same evaluation.

**F-WEP-000d — Determinism.** Every formula is a pure function of its declared inputs and, where stated, the frozen turn seed. No formula reads wall-clock time, login state, latency, request order or environment entropy.

**F-WEP-000e — Seed.** The only seed is B-02's frozen turn seed. A selection is `seeded_integer(seed, allocation_id, low, high)`, inclusive, stable for the same pair.

**F-WEP-000f — Fail closed.** A missing, out-of-range or inconsistent input produces the stated `WPF-` code and no partial value. A formula never guesses.

**F-WEP-000g — Snapshot.** A formula evaluated at W3 reads the sealed W3 baseline. A formula evaluated at W1/W2 reads the frozen post-P5 baseline. A formula never reads a later W-step result.

**F-WEP-000h — No hidden constant.** Every constant is named in field 6 or field 12/13 and classified in field 20.

---

## 4. Event formulas

### F-WEP-001 — Event occurrence key

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-001` |
| 2 | Name | Event occurrence key |
| 3 | Domain | Event |
| 4 | Purpose | Give one event occurrence a unique, reproducible identity so a duplicate cannot be generated |
| 5 | Expression | `occurrence_key = H(definition_id ‖ definition_version ‖ discriminator)` where `H` is the project's stable string hash and `‖` is an unambiguous separator |
| 6 | Variables | `definition_id` (string, non-empty); `definition_version` (integer ≥ 1); `discriminator` (string: boundary slot, threshold-crossing ID, nation ID + threshold ID, or challenge ID) |
| 7 | Input source | B-11 event definition table; B-02 turn slot; B-11 challenge table |
| 8 | Units | String |
| 9 | Valid range | All components non-empty; version ≥ 1 |
| 10 | Output range | Fixed-length hexadecimal string |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | Fail `WPF-03`; no instance |
| 17 | Invalid input | Empty component or version < 1 → `WPF-03` |
| 18 | Example | `definition_id="EV-STATE-CAPSTONE-01"`, version `3`, discriminator `"slot:248901:nation:1042"` → a stable 32-hex key; a second call with identical inputs returns the same key |
| 19 | Boundary case | A repeated discriminator at a different version produces a **different** key; the same version and discriminator produces the same key |
| 20 | Provisional status | **Structural**; no calibration |
| — | Main rule | WEP-087, WEP-115 |
| — | Audit / privacy | `WPA-04`; internal |

### F-WEP-002 — Event eligibility predicate

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-002` |
| 2 | Name | Event eligibility predicate |
| 3 | Domain | Event |
| 4 | Purpose | Decide whether a nation may join, be targeted by, or receive an instance |
| 5 | Expression | `eligible = exists(nation) ∧ ¬retired ∧ (hostile ⇒ (¬protected ∧ ¬dormant)) ∧ (competitive ⇒ first_boundary_complete) ∧ definition_conditions` |
| 6 | Variables | `exists` (boolean); `retired` (boolean); `protected` (boolean); `dormant` (boolean); `hostile` (boolean, definition); `competitive` (boolean, definition); `first_boundary_complete` (boolean); `definition_conditions` (boolean) |
| 7 | Input source | B-03 nation state, protection, dormancy, retirement; B-11 definition |
| 8 | Units | Boolean |
| 9 | Valid range | All booleans |
| 10 | Output range | `TRUE` or `FALSE` |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | Fail closed: `FALSE` plus `WPF-08` |
| 17 | Invalid input | A non-boolean state → `WPF-08` |
| 18 | Example | Active unprotected nation with a completed first boundary, non-hostile event → `TRUE`; protected nation, hostile event → `FALSE` |
| 19 | Boundary case | Dormant nation, non-hostile informational event → `TRUE` but excluded from public participant lists (WEP-136) |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-132…WEP-144 |
| — | Audit / privacy | `WPA-41`; per definition |

### F-WEP-003 — Event relative-band membership

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-003` |
| 2 | Name | Relative-band membership |
| 3 | Domain | Event |
| 4 | Purpose | Select eligible nations within a published band of the current world maximum without an absolute constant |
| 5 | Expression | `band_min = max(1, ceil(max_world_value × lo_bp / 10,000))`; `band_max = max(band_min, ceil(max_world_value × hi_bp / 10,000))`; `in_band = value ≥ band_min ∧ value ≤ band_max` |
| 6 | Variables | `value` (integer ≥ 0); `max_world_value` (integer ≥ 0); `lo_bp`, `hi_bp` (0…10,000; `lo_bp ≤ hi_bp`) |
| 7 | Input source | B-11 standing/event input; B-03; world snapshot |
| 8 | Units | Count or integer value; band bounds in bp |
| 9 | Valid range | `0 ≤ value ≤ max_world_value`; `0 ≤ lo_bp ≤ hi_bp ≤ 10,000` |
| 10 | Output range | Boolean |
| 11 | Rounding | `ceil` at each bound |
| 12 | Caps | `hi_bp ≤ 10,000` |
| 13 | Floors | `band_min ≥ 1` |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | No band → event withheld, `WPF-29` |
| 17 | Invalid input | `max_world_value = 0` → no eligible nation, not a division; `lo_bp > hi_bp` → `WPF-03` |
| 18 | Example | `max_world_value=100`, `lo_bp=1,500`, `hi_bp=6,500` → `band_min=15`, `band_max=65`; value 40 → `TRUE`; value 70 → `FALSE` |
| 19 | Boundary case | `max_world_value=0` → empty band; `value=ceil(max×lo)` is inside (inclusive); `value=band_max+1` is outside |
| 20 | Provisional status | **Structural**; `lo_bp`/`hi_bp` are **Prompt 14** parameters |
| — | Main rule | WEP-133, WEP-155 |
| — | Audit / privacy | `WPA-41`; published band |

### F-WEP-004 — Participation cap check

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-004` |
| 2 | Name | Participation cap check |
| 3 | Domain | Event |
| 4 | Purpose | Bound simultaneous and per-window participation |
| 5 | Expression | `allowed = (active_count < max_active) ∧ (window_count < max_window)` |
| 6 | Variables | `active_count` (integer ≥ 0); `window_count` (integer ≥ 0); `max_active`, `max_window` (integer ≥ 1) |
| 7 | Input source | B-11 participation records; definition |
| 8 | Units | Count |
| 9 | Valid range | Counts ≥ 0; caps ≥ 1 |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | Caps are the published values |
| 13 | Floors | 0 |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Current instance records at W1 |
| 16 | Missing data | Fail closed; no participation |
| 17 | Invalid input | Negative count → `WPF-14` |
| 18 | Example | `active_count=2`, `max_active=3`, `window_count=4`, `max_window=5` → `TRUE` |
| 19 | Boundary case | `active_count=max_active` → `FALSE` (the next join is refused) |
| 20 | Provisional status | **Structural**; caps are **Prompt 14** |
| — | Main rule | WEP-148, WEP-156 |
| — | Audit / privacy | `WPA-14`; owner |

### F-WEP-005 — Event progress

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-005` |
| 2 | Name | Event progress |
| 3 | Domain | Event |
| 4 | Purpose | Sum verified contributions to an event's completion condition |
| 5 | Expression | `progress = floor(Σ contribution_i)`; each `contribution_i` is recorded once per `(instance, participant, source_key)` |
| 6 | Variables | `contribution_i` (integer ≥ 0); `n` participants/events |
| 7 | Input source | B-11 effect records; owning subsystem source |
| 8 | Units | Definition's unit |
| 9 | Valid range | Each contribution ≥ 0 |
| 10 | Output range | 0…`target` (or unbounded for a score event) |
| 11 | Rounding | Floor |
| 12 | Caps | Event cap (field 12 of the definition) |
| 13 | Floors | 0 |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | Do not add; `PROVISIONAL` progress, `WPF-23` if completion is attempted |
| 17 | Invalid input | Negative contribution → reject, `WPF-16` |
| 18 | Example | Three verified contributions 10, 25, 15 → `progress = 50`; target 100 → not complete |
| 19 | Boundary case | A duplicate source key contributes once; progress 0 is valid and not an error |
| 20 | Provisional status | **Structural**; target is **Prompt 14** |
| — | Main rule | WEP-159 |
| — | Audit / privacy | `WPA-09`; per event scope |

### F-WEP-006 — Event completion predicate

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-006` |
| 2 | Name | Event completion predicate |
| 3 | Domain | Event |
| 4 | Purpose | Decide whether an event instance has satisfied its completion condition |
| 5 | Expression | `complete = (state = CLOSED) ∧ verified ∧ (progress ≥ target ∨ predicate = TRUE) ∧ ¬voided` |
| 6 | Variables | `state` (enum); `verified` (boolean); `progress` (integer ≥ 0); `target` (integer ≥ 0); `predicate` (boolean); `voided` (boolean) |
| 7 | Input source | B-11 instance; source verification |
| 8 | Units | Boolean |
| 9 | Valid range | Target ≥ 0 |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W1 after W1 close |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | `FALSE`; stay `CLOSED`; `WPF-18` |
| 17 | Invalid input | State not `CLOSED` → `WPF-13` |
| 18 | Example | `progress=100`, `target=100`, `verified=TRUE`, state `CLOSED` → `TRUE` |
| 19 | Boundary case | `progress=target−1` → `FALSE`; `target=0` → complete on verification (explicit zero-target rule) |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-181…WEP-192 |
| — | Audit / privacy | `WPA-10`; public after P7 |

### F-WEP-007 — Event contribution share

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-007` |
| 2 | Name | Event contribution share |
| 3 | Domain | Event |
| 4 | Purpose | Allocate a pooled result among participants without order dependence |
| 5 | Expression | `share_i = floor(pool × contribution_i / total_contribution)`; distribute the remainder by descending contribution then ascending `nation_id` (deterministic) |
| 6 | Variables | `pool` (integer ≥ 0); `contribution_i` (integer ≥ 0); `total_contribution` (integer ≥ 0) |
| 7 | Input source | B-11 event effects; B-04 value |
| 8 | Units | Pool unit |
| 9 | Valid range | `pool ≥ 0`; `total_contribution ≥ 0` |
| 10 | Output range | 0…pool |
| 11 | Rounding | Floor, then a declared remainder rule |
| 12 | Caps | 100% of pool |
| 13 | Floors | 0 |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | No allocation; `WPF-29` |
| 17 | Invalid input | `total_contribution=0` → no allocation, no division |
| 18 | Example | Pool 1,000; contributions 60, 30, 10 → shares 600, 300, 100 |
| 19 | Boundary case | Pool 100; three equal contributions → 33, 33, 34 by the declared remainder rule; never 34, 34, 34 |
| 20 | Provisional status | **Structural**; pool size is **Prompt 14** |
| — | Main rule | WEP-160 |
| — | Audit / privacy | `WPA-09`; public at `k≥5` |

### F-WEP-008 — Event reward qualification

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-008` |
| 2 | Name | Event reward qualification |
| 3 | Domain | Event |
| 4 | Purpose | Decide whether a participant qualifies for a declared event reward |
| 5 | Expression | `qualified = complete ∧ eligible_at_grant ∧ ¬deduped ∧ reward_declared ∧ cap_not_reached` |
| 6 | Variables | `complete` (boolean); `eligible_at_grant` (boolean); `deduped` (boolean); `reward_declared` (boolean); `cap_not_reached` (boolean) |
| 7 | Input source | B-11 instance, reward table, B-03 state |
| 8 | Units | Boolean |
| 9 | Valid range | Booleans |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | Reward cap (F-WEP-046) |
| 13 | Floors | None |
| 14 | Phase | P6 W1/W4 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; defer, `WPF-30` |
| 17 | Invalid input | Undeclared reward → `WPF-31` |
| 18 | Example | Complete, eligible, key unused, reward declared, cap 5 not reached → `TRUE` |
| 19 | Boundary case | A duplicate key → `FALSE`, existing grant returned |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-163 |
| — | Audit / privacy | `WPA-16`; owner |

### F-WEP-009 — Occurrence cap

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-009` |
| 2 | Name | Occurrence cap |
| 3 | Domain | Event |
| 4 | Purpose | Stop repeated generation of one definition in a window |
| 5 | Expression | `may_generate = occurrence_count(window) < max_occurrences(window)` |
| 6 | Variables | `occurrence_count` (integer ≥ 0); `max_occurrences` (integer ≥ 0) |
| 7 | Input source | B-11 generation records |
| 8 | Units | Count |
| 9 | Valid range | Both ≥ 0 |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | `max_occurrences` |
| 13 | Floors | 0 |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Current window records |
| 16 | Missing data | Fail closed; no generation |
| 17 | Invalid input | Negative count → `WPF-05` |
| 18 | Example | `occurrence_count=2`, `max_occurrences=3` → `TRUE`; next turn `3 < 3` → `FALSE` |
| 19 | Boundary case | `max_occurrences=0` means the definition never generates; it is a valid disabled row |
| 20 | Provisional status | **Structural**; cap is **Prompt 14** |
| — | Main rule | WEP-123, WEP-129 |
| — | Audit / privacy | `WPA-26`; published skip |

### F-WEP-010 — Teardown boundaries

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-010` |
| 2 | Name | Teardown boundaries |
| 3 | Domain | Event |
| 4 | Purpose | Fix the closing and cleanup boundaries so an event cannot end in two clocks |
| 5 | Expression | `close_boundary = end_boundary`; `teardown_boundary = close_boundary + teardown_lag`; require `teardown_boundary > close_boundary` |
| 6 | Variables | `end_boundary` (turn/boundary); `teardown_lag` (integer ≥ 1 turn) |
| 7 | Input source | Definition; B-02 slot arithmetic |
| 8 | Units | Turns |
| 9 | Valid range | `teardown_lag ≥ 1` |
| 10 | Output range | Two boundaries |
| 11 | Rounding | None |
| 12 | Caps | `teardown_lag ≤ 12` (provisional) |
| 13 | Floors | 1 |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `WPF-06`; no schedule |
| 17 | Invalid input | `teardown_boundary ≤ close_boundary` → `WPF-06` |
| 18 | Example | End at slot 248,900; lag 1 → close 248,900, teardown 248,901 |
| 19 | Boundary case | Lag 1 is the minimum; a multi-turn lag is allowed within the cap |
| 20 | Provisional status | **Structural**; lag is **Prompt 14** |
| — | Main rule | WEP-185 |
| — | Audit / privacy | `WPA-08`; public |

### F-WEP-011 — Event effect magnitude

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-011` |
| 2 | Name | Event effect magnitude |
| 3 | Domain | Event |
| 4 | Purpose | Bound a non-material effect so it cannot become a hidden bonus or penalty |
| 5 | Expression | `effect = clamp(floor(base × scale_bp / 10,000), effect_min, effect_max)` |
| 6 | Variables | `base` (integer ≥ 0); `scale_bp` (0…10,000); `effect_min` (integer); `effect_max` (integer) |
| 7 | Input source | Definition; owning subsystem baseline |
| 8 | Units | Owning subsystem unit |
| 9 | Valid range | `effect_min ≤ effect_max`; `base ≥ 0` |
| 10 | Output range | `[effect_min, effect_max]` |
| 11 | Rounding | Floor |
| 12 | Caps | `effect_max` |
| 13 | Floors | `effect_min` |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | No effect; `WPF-16` |
| 17 | Invalid input | `effect_min > effect_max` → `WPF-03` |
| 18 | Example | base 200, scale 1,000 bp (10%), min 0, max 50 → `20` |
| 19 | Boundary case | base 0 → 0; scale 10,000 with base 1,000 and max 50 → 50 (cap) |
| 20 | Provisional status | **Provisional**; `scale_bp`, min and max are **Prompt 14** |
| — | Main rule | WEP-169, WEP-176 |
| — | Audit / privacy | `WPA-09`; per effect |

### F-WEP-012 — Participation freeze boundary

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-012` |
| 2 | Name | Participation freeze boundary |
| 3 | Domain | Event |
| 4 | Purpose | Close participation one turn before a deciding snapshot or selection |
| 5 | Expression | `freeze_boundary = decide_boundary − freeze_turns`; `accept_allowed = current_turn < freeze_boundary` |
| 6 | Variables | `decide_boundary` (turn); `freeze_turns` (integer ≥ 1); `current_turn` (turn) |
| 7 | Input source | Definition; B-02 turn |
| 8 | Units | Turns |
| 9 | Valid range | `freeze_turns ≥ 1` |
| 10 | Output range | Boundary; boolean |
| 11 | Rounding | None |
| 12 | Caps | `freeze_turns ≤ decide_boundary − start_boundary` |
| 13 | Floors | 1 |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | No acceptance; `WPF-15` |
| 17 | Invalid input | Freeze before start → `WPF-06` |
| 18 | Example | Decide at turn 100; freeze 1 → freeze boundary 99; an action at 98 is accepted, at 99 rejected |
| 19 | Boundary case | An action exactly at the freeze boundary is rejected (half-open rule) |
| 20 | Provisional status | **Structural**; freeze length is **Prompt 14** |
| — | Main rule | WEP-155 |
| — | Audit / privacy | `WPA-15`; public |

### F-WEP-013 — Event result order

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-013` |
| 2 | Name | Event result order |
| 3 | Domain | Event |
| 4 | Purpose | Produce a deterministic result order when a single winner or a ranked result is required |
| 5 | Expression | Sort by `(score DESC, completion_turn ASC, nation_id ASC)`, then apply F-WEP-038 tie groups |
| 6 | Variables | `score` (integer); `completion_turn` (turn); `nation_id` (integer) |
| 7 | Input source | B-11 instance results; B-03 nation ID |
| 8 | Units | Order |
| 9 | Valid range | Score ≥ 0 |
| 10 | Output range | Ordered list |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W1 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | Participant excluded, not zero |
| 17 | Invalid input | Duplicate nation ID → `WPF-14` |
| 18 | Example | Scores 10 (turn 90), 10 (turn 91), 12 → order: 12 first, then the turn-90 10, then the turn-91 10 |
| 19 | Boundary case | Equal score and equal completion turn → shared rank unless one winner is required; then seeded selection |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-160, WEP-394 |
| — | Audit / privacy | `WPA-10`; public after P7 |

### F-WEP-014 — Event notability flag

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-014` |
| 2 | Name | Event notability flag |
| 3 | Domain | Event / history |
| 4 | Purpose | Decide whether an event instance writes a chronicle entry |
| 5 | Expression | `notable = class ∈ {EV-COMM} ∨ scope = WORLD ∨ completed_with_honour ∨ voided_or_corrected` |
| 6 | Variables | `class` (enum); `scope` (enum); `completed_with_honour` (boolean); `voided_or_corrected` (boolean) |
| 7 | Input source | B-11 instance |
| 8 | Units | Boolean |
| 9 | Valid range | Enums |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W4 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE` (no chronicle entry) |
| 17 | Invalid input | Unknown class → `WPF-02` |
| 18 | Example | A world-scope calendar event → `TRUE`; a nation-scope informational event with no honour → `FALSE` |
| 19 | Boundary case | A voided world event → `TRUE` (correction entry) |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-193, WEP-681 |
| — | Audit / privacy | `WPA-48`; public/redacted |

## 5. Objective formulas

### F-WEP-015 — Objective offer eligibility

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-015` |
| 2 | Name | Objective offer eligibility |
| 3 | Domain | Objective |
| 4 | Purpose | Decide whether a definition may be offered to a nation |
| 5 | Expression | `offer = published ∧ eligible ∧ ¬on_cooldown ∧ outstanding < cap ∧ ¬(one_time ∧ already_completed)` |
| 6 | Variables | `published` (boolean); `eligible` (boolean); `on_cooldown` (boolean); `outstanding` (integer ≥ 0); `cap` (integer ≥ 0); `one_time`, `already_completed` (boolean) |
| 7 | Input source | B-11 definitions/instances; B-03 state |
| 8 | Units | Boolean |
| 9 | Valid range | Counts ≥ 0 |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | `outstanding < cap` |
| 13 | Floors | 0 |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | No offer; `WPF-19` |
| 17 | Invalid input | Negative count → `WPF-19` |
| 18 | Example | Published, eligible, no cooldown, 2 outstanding, cap 5, not completed → `TRUE` |
| 19 | Boundary case | `outstanding = cap` → `FALSE`; a completed one-time objective → `FALSE` |
| 20 | Provisional status | **Structural**; cap is **Prompt 14** |
| — | Main rule | WEP-254 |

### F-WEP-016 — Outstanding-objective count

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-016` |
| 2 | Name | Outstanding-objective count |
| 3 | Domain | Objective |
| 4 | Purpose | Count the objectives a nation currently holds, for the offer cap |
| 5 | Expression | `outstanding = count(instances where state ∈ {ACCEPTED, IN_PROGRESS, TIER_REACHED, COMPLETED_PENDING_VALIDATION, VERIFIED, REWARD_PENDING, DEFERRED})` |
| 6 | Variables | `instances` (set); `state` (enum) |
| 7 | Input source | B-11 objective instances |
| 8 | Units | Count |
| 9 | Valid range | 0…cap |
| 10 | Output range | Integer ≥ 0 |
| 11 | Rounding | None |
| 12 | Caps | Count returns the true count; the cap is applied by F-WEP-015 |
| 13 | Floors | 0 |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Current W2 records |
| 16 | Missing data | Treat as 0 only if the nation has no instances; otherwise `WPF-23` |
| 17 | Invalid input | Negative count → `WPF-19` |
| 18 | Example | 2 accepted, 1 tier reached, 4 dismissed → `outstanding = 3` |
| 19 | Boundary case | `DISMISSED` and `EXPIRED` do not count; `DEFERRED` does |
| 20 | Provisional status | **Structural**; cap is **Prompt 14** |
| — | Main rule | WEP-254, WEP-260 |

### F-WEP-017 — Objective progress

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-017` |
| 2 | Name | Objective progress |
| 3 | Domain | Objective |
| 4 | Purpose | Compute the current progress value from keyed source records |
| 5 | Expression | Incremental: `progress = floor(Σ delta_j)`; aggregate: `progress = max(0, current_owned_value − baseline_value)`; threshold: `progress = current_owned_value` |
| 6 | Variables | `delta_j` (integer, may be negative only for a correction); `current_owned_value` (integer); `baseline_value` (integer) |
| 7 | Input source | B-04, B-05, B-06, B-07, B-08, B-09, B-10, B-11 source records |
| 8 | Units | Definition's unit |
| 9 | Valid range | Progress ≥ 0 after clamping |
| 10 | Output range | 0…event/objective cap |
| 11 | Rounding | Floor |
| 12 | Caps | Definition cap |
| 13 | Floors | 0 |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | Do not advance; `WPF-23` |
| 17 | Invalid input | Missing source key → `WPF-22`; negative without a correction record → `WPF-21` |
| 18 | Example | Deltas 10, 25, 15 → 50; target 100 → 50% |
| 19 | Boundary case | A correction of −5 after 50 → 45, with the reversal record preserved |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-265…WEP-280 |

### F-WEP-018 — Objective progress percentage

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-018` |
| 2 | Name | Objective progress percentage |
| 3 | Domain | Objective |
| 4 | Purpose | Display progress without changing the authoritative integer |
| 5 | Expression | `pct_bp = min(10,000, floor(progress × 10,000 / target))` |
| 6 | Variables | `progress` (integer ≥ 0); `target` (integer ≥ 1) |
| 7 | Input source | B-11 progress; definition |
| 8 | Units | Basis points |
| 9 | Valid range | `progress ≥ 0`; `target ≥ 1` |
| 10 | Output range | 0…10,000 |
| 11 | Rounding | Floor |
| 12 | Caps | 10,000 |
| 13 | Floors | 0 |
| 14 | Phase | P6 W2 (display) |
| 15 | Snapshot | Current progress |
| 16 | Missing data | Display "unknown"; no completion |
| 17 | Invalid input | `target = 0` → `WPF-03`; the definition is invalid |
| 18 | Example | progress 50, target 100 → 5,000 bp = 50% |
| 19 | Boundary case | progress ≥ target → 10,000 bp; progress 0 → 0 bp |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-283 |

### F-WEP-019 — Tier completion

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-019` |
| 2 | Name | Tier completion |
| 3 | Domain | Objective |
| 4 | Purpose | Decide whether a tier threshold is reached and not already awarded |
| 5 | Expression | `tier_met = (progress ≥ tier_threshold) ∧ ¬awarded(tier_key)` |
| 6 | Variables | `progress` (integer ≥ 0); `tier_threshold` (integer ≥ 0); `awarded` (boolean) |
| 7 | Input source | B-11 progress and tier records |
| 8 | Units | Boolean |
| 9 | Valid range | Threshold ≥ 0 |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; `WPF-23` if progress is unknown |
| 17 | Invalid input | Negative threshold → `WPF-03` |
| 18 | Example | progress 60, thresholds 25/50/100 → tiers 1 and 2 met; tier 3 not |
| 19 | Boundary case | progress exactly 50 meets the 50 tier (inclusive) |
| 20 | Provisional status | **Structural**; thresholds are **Prompt 14** |
| — | Main rule | WEP-237, WEP-298 |

### F-WEP-020 — Objective completion predicate

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-020` |
| 2 | Name | Objective completion predicate |
| 3 | Domain | Objective |
| 4 | Purpose | Decide whether the objective is complete and ready for verification |
| 5 | Expression | `complete = (target_predicate = TRUE) ∧ all_required_conditions ∧ ¬already_verified` |
| 6 | Variables | `target_predicate` (boolean); `all_required_conditions` (boolean); `already_verified` (boolean) |
| 7 | Input source | B-11 instance; definition |
| 8 | Units | Boolean |
| 9 | Valid range | Booleans |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; stay `IN_PROGRESS` |
| 17 | Invalid input | Unknown condition → `WPF-22` |
| 18 | Example | Target reached, both required conditions true, not verified → `TRUE` |
| 19 | Boundary case | A threshold equality counts as reached |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-225, WEP-284 |

### F-WEP-021 — Seasonal objective points

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-021` |
| 2 | Name | Seasonal objective points |
| 3 | Domain | Objective |
| 4 | Purpose | Combine tier completions into a seasonal standing input |
| 5 | Expression | `points = floor(Σ (tier_points_k × class_weight_bp_k) / 10,000)` |
| 6 | Variables | `tier_points_k` (integer ≥ 0); `class_weight_bp_k` (0…10,000) |
| 7 | Input source | B-11 seasonal records |
| 8 | Units | Points |
| 9 | Valid range | Points ≥ 0; weights within range |
| 10 | Output range | 0…seasonal cap |
| 11 | Rounding | Floor |
| 12 | Caps | Seasonal cap (provisional) |
| 13 | Floors | 0 |
| 14 | Phase | P6 W2/W3 |
| 15 | Snapshot | Season-scoped records |
| 16 | Missing data | No points for that tier; `WPF-23` |
| 17 | Invalid input | Weight > 10,000 → `WPF-03` |
| 18 | Example | Tier points 40 at 10,000 bp + 25 at 5,000 bp → 40 + 12 = 52 |
| 19 | Boundary case | No tiers → 0; a weight of 0 makes the tier recognition-only |
| 20 | Provisional status | **Provisional**; weights and cap are **Prompt 14** |
| — | Main rule | WEP-214, WEP-336 |

### F-WEP-022 — Difficulty class lookup

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-022` |
| 2 | Name | Difficulty class lookup |
| 3 | Domain | Objective |
| 4 | Purpose | Assign a descriptive difficulty label from declared properties, not from time spent |
| 5 | Expression | `class = lookup(scale, condition_count, horizon)` per the published table; no arithmetic weighting |
| 6 | Variables | `scale` (enum: small/medium/large); `condition_count` (1…5); `horizon` (enum: short/medium/long/permanent) |
| 7 | Input source | Definition |
| 8 | Units | Enum |
| 9 | Valid range | Enumerated |
| 10 | Output range | `INTRODUCTORY`, `STANDARD`, `ADVANCED`, `LONG_TERM`, `COMPETITIVE`, `SEASONAL` |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | Definition publication |
| 15 | Snapshot | None |
| 16 | Missing data | Definition rejected |
| 17 | Invalid input | Out-of-range property → `WPF-01` |
| 18 | Example | small/short/1 condition → `INTRODUCTORY`; large/long/4 conditions → `LONG_TERM` |
| 19 | Boundary case | A competitive condition overrides the horizon to `COMPETITIVE` |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-291…WEP-296 |

### F-WEP-023 — Objective reward eligibility

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-023` |
| 2 | Name | Objective reward eligibility |
| 3 | Domain | Objective |
| 4 | Purpose | Decide whether a verified objective may grant its reward |
| 5 | Expression | `reward_ok = verified ∧ reward_declared ∧ eligible_at_grant ∧ ¬deduped ∧ cap_ok` |
| 6 | Variables | `verified` (boolean); `reward_declared` (boolean); `eligible_at_grant` (boolean); `deduped` (boolean); `cap_ok` (boolean) |
| 7 | Input source | B-11 instance/reward; B-03; B-04 cap |
| 8 | Units | Boolean |
| 9 | Valid range | Booleans |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | Reward cap |
| 13 | Floors | None |
| 14 | Phase | P6 W4/W5 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; `DEFERRED` |
| 17 | Invalid input | Undeclared reward → `WPF-31` |
| 18 | Example | Verified, declared, eligible, key unused, cap available → `TRUE` |
| 19 | Boundary case | Cap reached → `FALSE`; recognition may still be granted |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-520, WEP-527 |

### F-WEP-024 — Repeat cooldown

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-024` |
| 2 | Name | Repeat cooldown |
| 3 | Domain | Objective |
| 4 | Purpose | Prevent immediate repeated completion of a repeatable objective |
| 5 | Expression | `available = (current_turn − last_completion_turn) ≥ cooldown_turns` |
| 6 | Variables | `current_turn` (turn); `last_completion_turn` (turn or null); `cooldown_turns` (integer ≥ 0) |
| 7 | Input source | B-11 instance |
| 8 | Units | Turns |
| 9 | Valid range | `cooldown_turns ≥ 0` |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | Cooldown cap (provisional) |
| 13 | Floors | 0 |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Current records |
| 16 | Missing data | No prior completion → `TRUE` |
| 17 | Invalid input | Negative cooldown → `WPF-03` |
| 18 | Example | Last completed turn 80, cooldown 12, current 92 → `TRUE`; current 91 → `FALSE` |
| 19 | Boundary case | Cooldown 0 → available immediately; this is permitted only for a non-economic repeatable recognition |
| 20 | Provisional status | **Structural**; cooldown is **Prompt 14** |
| — | Main rule | WEP-298, WEP-303 |

### F-WEP-025 — Objective expiry boundary

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-025` |
| 2 | Name | Objective expiry boundary |
| 3 | Domain | Objective |
| 4 | Purpose | Fix when an accepted objective ends |
| 5 | Expression | `expiry = acceptance_turn + limit_turns`; `expired = current_turn ≥ expiry ∧ state ∉ {VERIFIED, REWARD_PENDING, DEFERRED, CLAIMED}` |
| 6 | Variables | `acceptance_turn` (turn); `limit_turns` (integer ≥ 1); `current_turn` (turn); `state` (enum) |
| 7 | Input source | B-11 instance; definition |
| 8 | Units | Turns |
| 9 | Valid range | `limit_turns ≥ 1` |
| 10 | Output range | Boundary; boolean |
| 11 | Rounding | None |
| 12 | Caps | Limit cap (provisional) |
| 13 | Floors | 1 |
| 14 | Phase | P6 W2 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | No expiry if the definition has none |
| 17 | Invalid input | `limit_turns ≤ 0` → `WPF-03` |
| 18 | Example | Accepted turn 100, limit 12 → expiry 112; at 112 it expires |
| 19 | Boundary case | A verified or deferred instance never expires; a completed-but-unclaimed reward never expires |
| 20 | Provisional status | **Structural**; limit is **Prompt 14** |
| — | Main rule | WEP-226, WEP-243 |

### F-WEP-026 — Individual-equivalence check

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-026` |
| 2 | Name | Individual-equivalence check |
| 3 | Domain | Objective |
| 4 | Purpose | Enforce that every collective objective has an individual path |
| 5 | Expression | `valid = (category ≠ OBJ-ALL) ∨ exists(equivalent_id where not_requires_membership ∧ same_recognition_class)` |
| 6 | Variables | `category` (enum); `equivalent_id` (reference); `not_requires_membership` (boolean); `same_recognition_class` (boolean) |
| 7 | Input source | B-11 definitions |
| 8 | Units | Boolean |
| 9 | Valid range | Enumerated |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | Definition publication |
| 15 | Snapshot | None |
| 16 | Missing data | `FALSE`; definition rejected |
| 17 | Invalid input | Dangling reference → `WPF-01` |
| 18 | Example | An `OBJ-ALL` "collective capstone" with an individual "complete one capstone" equivalent → `TRUE` |
| 19 | Boundary case | A collective objective with no equivalent → `FALSE`, `WPF-01` |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-261 |

---

## 6. Standing formulas

### F-WEP-027 — Ranking percentile

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-027` |
| 2 | Name | Ranking percentile |
| 3 | Domain | Standing |
| 4 | Purpose | Express a rank as a share of the eligible population |
| 5 | Expression | `percentile_bp = floor(10,000 × (N − rank + 1) / N)` |
| 6 | Variables | `N` (eligible population ≥ 1); `rank` (1…N) |
| 7 | Input source | Sealed snapshot |
| 8 | Units | Basis points |
| 9 | Valid range | `N ≥ 1`; `1 ≤ rank ≤ N` |
| 10 | Output range | 100…10,000 |
| 11 | Rounding | Floor |
| 12 | Caps | 10,000 |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | Withhold the percentile |
| 17 | Invalid input | `N = 0` → no standing, `WPF-29` |
| 18 | Example | N=100, rank=1 → 10,000; rank=100 → 100 |
| 19 | Boundary case | Tied ranks share the same percentile; the denominator is the eligible set, stated publicly |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-324, WEP-359 |

### F-WEP-028 — WSE state

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-028` |
| 2 | Name | World Standing Eligibility state |
| 3 | Domain | Standing |
| 4 | Purpose | Publish whether a nation may appear in a competitive standing, without creating a rank |
| 5 | Expression | `if ¬exists ∨ retired ∨ archived → EXCLUDED`; `else if ¬first_boundary_complete → UNRANKED`; `else if dormant ∨ evidence_hold → EXCLUDED`; `else if incomplete_data ∨ correction_pending → PROVISIONAL`; `else ELIGIBLE` |
| 6 | Variables | `exists`, `retired`, `archived`, `first_boundary_complete`, `dormant`, `evidence_hold`, `incomplete_data`, `correction_pending` (booleans) |
| 7 | Input source | B-03; B-11 data completeness |
| 8 | Units | Enum |
| 9 | Valid range | Booleans |
| 10 | Output range | `UNRANKED`, `ELIGIBLE`, `PROVISIONAL`, `EXCLUDED` |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | Frozen post-P5 baseline |
| 16 | Missing data | `PROVISIONAL` |
| 17 | Invalid input | Contradictory source states → `EXCLUDED` plus `WPF-34` |
| 18 | Example | Active, first boundary complete, complete data → `ELIGIBLE` |
| 19 | Boundary case | Dormant and data-complete → `EXCLUDED`; a new nation → `UNRANKED` |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-367…WEP-380 |

### F-WEP-029 — Development index

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-029` |
| 2 | Name | Development index |
| 3 | Domain | Standing |
| 4 | Purpose | Combine durable B-05 development into one comparative metric |
| 5 | Expression | `D = w_city × C + w_infra × I + w_fac × F + w_res × R + w_cap × K`; then normalise per F-WEP-027 |
| 6 | Variables | `C` cities (0…12); `I` total infrastructure (0…6,000); `F` weighted facility points (≥0); `R` completed technologies (0…12); `K` completed capstones (0…4); `w_*` provisional weights (≥0) |
| 7 | Input source | B-05 |
| 8 | Units | Index |
| 9 | Valid range | `C ≤ 12`, `I ≤ 6,000`, `R ≤ 12`, `K ≤ 4` |
| 10 | Output range | 0…index cap |
| 11 | Rounding | Floor |
| 12 | Caps | Per-component caps as listed |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | Nation `PROVISIONAL`, excluded from the order |
| 17 | Invalid input | Out-of-range component → `WPF-29` |
| 18 | Example | C=3, I=300, F=40, R=5, K=1, weights 100/10/50/200/1,000 → 300+3,000+2,000+1,000+1,000 = 7,300 |
| 19 | Boundary case | A new city with I=0 contributes through `C` only; a maxed nation is capped, not unbounded |
| 20 | Provisional status | **Provisional**; all weights are **Prompt 14** |
| — | Main rule | WEP-327 |

### F-WEP-030 — Economic output index

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-030` |
| 2 | Name | Economic output index |
| 3 | Domain | Standing |
| 4 | Purpose | Recognise produced output, not stored wealth |
| 5 | Expression | `EO = floor(Σ (qty_i × ref_price_i) / 100)` over the window; no `national_wealth` term |
| 6 | Variables | `qty_i` (integer ≥ 0); `ref_price_i` (integer ≥ 0) |
| 7 | Input source | B-04 published production records and reference prices |
| 8 | Units | Crown-equivalent minor units |
| 9 | Valid range | Non-negative |
| 10 | Output range | 0…cap |
| 11 | Rounding | Floor |
| 12 | Caps | Per-nation cap (provisional) |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline, window records |
| 16 | Missing data | `PROVISIONAL`, excluded from order |
| 17 | Invalid input | Missing reference price → `WPF-29` |
| 18 | Example | 100 units at 50 + 40 units at 25 → (5,000 + 1,000)/100 = 60 |
| 19 | Boundary case | Zero output is a valid zero, not a missing value; a nation with no production record is missing, not zero |
| 20 | Provisional status | **Provisional**; cap and window are **Prompt 14** |
| — | Main rule | WEP-328 |

### F-WEP-031 — Resilience index

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-031` |
| 2 | Name | Resilience index |
| 3 | Domain | Standing |
| 4 | Purpose | Recognise stability and recovery rather than size |
| 5 | Expression | `res = clamp(floor(10,000 × (W − S) / W), 0, 10,000)` where `S = shortfall_turns + austerity_turns` in the window |
| 6 | Variables | `W` window turns (≥1); `S` adverse turns (0…W) |
| 7 | Input source | B-04 shortfall/austerity records |
| 8 | Units | Basis points |
| 9 | Valid range | `W ≥ 1`; `0 ≤ S ≤ W` |
| 10 | Output range | 0…10,000 |
| 11 | Rounding | Floor |
| 12 | Caps | 10,000 |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline, window |
| 16 | Missing data | `PROVISIONAL` |
| 17 | Invalid input | `W = 0` → `WPF-29`; `S > W` → clamp with a `WPF-34` |
| 18 | Example | W=12, S=3 → floor(10,000 × 9 / 12) = 7,500 |
| 19 | Boundary case | S=0 → 10,000; S=W → 0 |
| 20 | Provisional status | **Structural**; window is **Prompt 14** |
| — | Main rule | WEP-329 |

### F-WEP-032 — Housing sufficiency

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-032` |
| 2 | Name | Housing sufficiency |
| 3 | Domain | Standing |
| 4 | Purpose | Compare population with effective housing without a headcount race |
| 5 | Expression | `hs_bp = if population = 0 then 10,000 else min(20,000, floor(10,000 × effective_housing / population))` |
| 6 | Variables | `population` (integer ≥ 0); `effective_housing` (integer ≥ 0) |
| 7 | Input source | B-05 housing; B-06 population |
| 8 | Units | Basis points |
| 9 | Valid range | Non-negative |
| 10 | Output range | 0…20,000 |
| 11 | Rounding | Floor |
| 12 | Caps | 20,000 |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | `PROVISIONAL` |
| 17 | Invalid input | Negative value → `WPF-29` |
| 18 | Example | population 10,000, housing 12,000 → 12,000 bp = 120% |
| 19 | Boundary case | population 0 → 10,000 (neutral); housing 0 with population > 0 → 0 |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-330 |

### F-WEP-033 — Institutional continuity

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-033` |
| 2 | Name | Institutional continuity |
| 3 | Domain | Standing |
| 4 | Purpose | Recognise political continuity without ranking approval or welfare |
| 5 | Expression | `IC = w_term × terms_completed + w_crisis × crises_survived + w_policy × policy_lines_held + w_inst × institutional_steps` |
| 6 | Variables | Counts (≥0); `w_*` provisional weights |
| 7 | Input source | B-06 election, crisis and institutional records |
| 8 | Units | Index |
| 9 | Valid range | Counts non-negative |
| 10 | Output range | 0…cap |
| 11 | Rounding | Floor |
| 12 | Caps | Per-component caps |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | `PROVISIONAL` |
| 17 | Invalid input | Approval or welfare input present → `WPF-34`; the metric is invalid |
| 18 | Example | 2 terms, 1 crisis, 1 policy line, 3 steps; weights 500/300/200/100 → 1,000+300+200+300 = 1,800 |
| 19 | Boundary case | A nation with no election yet scores 0, not a penalty |
| 20 | Provisional status | **Provisional**; weights are **Prompt 14** |
| — | Main rule | WEP-331 |

### F-WEP-034 — Diplomatic activity

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-034` |
| 2 | Name | Diplomatic activity |
| 3 | Domain | Standing |
| 4 | Purpose | Count published diplomatic facts without creating a reputation score |
| 5 | Expression | `DA = distinct_partners + agreements_concluded + consultations_honoured + peaceful_settlements` over the window |
| 6 | Variables | Counts (≥0) |
| 7 | Input source | B-08 published facts |
| 8 | Units | Count |
| 9 | Valid range | Non-negative |
| 10 | Output range | 0…cap |
| 11 | Rounding | None |
| 12 | Caps | Per-component cap (provisional) |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | `PROVISIONAL` |
| 17 | Invalid input | A "reputation" input → `WPF-34`; it is not available |
| 18 | Example | 3 partners + 2 agreements + 1 consultation + 1 settlement = 7 |
| 19 | Boundary case | No diplomacy → 0, not "unknown" |
| 20 | Provisional status | **Structural**; cap and window are **Prompt 14** |
| — | Main rule | WEP-332 |

### F-WEP-035 — Military participation

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-035` |
| 2 | Name | Military participation |
| 3 | Domain | Standing |
| 4 | Purpose | Recognise participation and service without exposing force values |
| 5 | Expression | `MP = campaigns_participated + operations_executed + defensive_engagements`; published only as counts/bands |
| 6 | Variables | Counts (≥0) |
| 7 | Input source | B-10 permanent campaign record |
| 8 | Units | Count |
| 9 | Valid range | Non-negative |
| 10 | Output range | 0…cap |
| 11 | Rounding | None |
| 12 | Caps | Per-component cap |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | Treat as 0 only if B-10 confirms no participation; otherwise `PROVISIONAL` |
| 17 | Invalid input | Any exact readiness/force/inventory field → `WPF-37`; the standing is withheld |
| 18 | Example | 2 campaigns, 5 operations, 1 defensive engagement = 8 |
| 19 | Boundary case | A nation with no campaign → 0 |
| 20 | Provisional status | **Structural**; cap is **Prompt 14** |
| — | Main rule | WEP-333, WEP-636 |

### F-WEP-036 — Defensive performance band

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-036` |
| 2 | Name | Defensive performance band |
| 3 | Domain | Standing |
| 4 | Purpose | Express defensive outcomes in a published band, never an exact value |
| 5 | Expression | `r_bp = if defensive_engagements = 0 then null else floor(10,000 × repelled / defensive_engagements)`; `band = lookup(r_bp)` |
| 6 | Variables | `repelled` (0…engagements); `defensive_engagements` (≥0); band table |
| 7 | Input source | B-10 campaign record |
| 8 | Units | Basis points → band enum |
| 9 | Valid range | `0 ≤ repelled ≤ defensive_engagements` |
| 10 | Output range | `NONE`, `LOW`, `MID`, `HIGH` (published thresholds) |
| 11 | Rounding | Floor |
| 12 | Caps | 10,000 |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | `NONE` if no engagements; `PROVISIONAL` if unknown |
| 17 | Invalid input | `repelled > engagements` → `WPF-37` |
| 18 | Example | 3 repelled / 4 engagements = 7,500 bp → `HIGH` under the published table |
| 19 | Boundary case | 0 engagements → `NONE`, not 0% (which would imply failure) |
| 20 | Provisional status | **Structural**; band thresholds are **Prompt 14** |
| — | Main rule | WEP-334 |

### F-WEP-037 — Alliance collective aggregate

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-037` |
| 2 | Name | Alliance collective aggregate |
| 3 | Domain | Standing |
| 4 | Purpose | Publish a group measure without exposing a member value |
| 5 | Expression | `agg = if member_count < 5 then WITHHELD else floor(Σ member_metric / member_count)` |
| 6 | Variables | `member_metric` (integer ≥ 0); `member_count` (≥0) |
| 7 | Input source | B-09 membership; B-11 member metrics |
| 8 | Units | Metric unit |
| 9 | Valid range | `member_count ≥ 0` |
| 10 | Output range | 0…cap or `WITHHELD` |
| 11 | Rounding | Floor |
| 12 | Caps | Metric cap |
| 13 | Floors | 0 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | `WITHHELD` |
| 17 | Invalid input | Any member-level publication → `WPF-36` |
| 18 | Example | 6 members with metrics 100, 80, 60, 40, 20, 0 → floor(300/6) = 50 |
| 19 | Boundary case | 4 members → `WITHHELD` even if all values are public |
| 20 | Provisional status | **Structural**; `k = 5` is approved; `UD-050` tests viability |
| — | Main rule | WEP-335, WEP-379 |

### F-WEP-038 — Rank assignment and tie groups

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-038` |
| 2 | Name | Rank assignment and tie groups |
| 3 | Domain | Standing |
| 4 | Purpose | Assign competition ranks with shared positions and deterministic tie groups |
| 5 | Expression | Sort descending by metric; `rank_1 = 1`; `rank_i = rank_{i−1}` if `metric_i = metric_{i−1}` else `rank_i = i`; all equal values form one tie group |
| 6 | Variables | `metric_i` (integer or stated order) |
| 7 | Input source | Sealed snapshot inputs |
| 8 | Units | Ordinal |
| 9 | Valid range | Non-negative metric |
| 10 | Output range | Rank 1…N; tie group ID |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | 1 |
| 14 | Phase | P6 W3 |
| 15 | Snapshot | W3 baseline |
| 16 | Missing data | Excluded entity does not consume a rank |
| 17 | Invalid input | Duplicate entity → `WPF-34` |
| 18 | Example | Metrics 100, 90, 90, 80 → ranks 1, 2, 2, 4; tie group {2,3} |
| 19 | Boundary case | All equal → everyone rank 1; no arbitrary ordinal is invented |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-392…WEP-399 |

## 7. Progression formulas

### F-WEP-039 — Achievement qualification

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-039` |
| 2 | Name | Achievement qualification |
| 3 | Domain | Progression |
| 4 | Purpose | Decide whether a nation qualifies for a keyed achievement |
| 5 | Expression | `qualified = condition_true ∧ evidence_exists ∧ ¬granted(achievement_key) ∧ eligibility_closure_ok` |
| 6 | Variables | `condition_true` (boolean); `evidence_exists` (boolean); `granted` (boolean); `eligibility_closure_ok` (boolean) |
| 7 | Input source | B-11 condition and evidence; B-03/B-04/B-05/B-06/B-08/B-10 |
| 8 | Units | Boolean |
| 9 | Valid range | Booleans |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W4 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; `WPF-27` |
| 17 | Invalid input | Missing evidence → `WPF-22` |
| 18 | Example | Condition true, evidence ID present, key unused, closure open → `TRUE` |
| 19 | Boundary case | A closed honour after the closure boundary → `FALSE` (not eligible), even if the condition is true |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-433…WEP-446 |

### F-WEP-040 — Milestone geometric threshold

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-040` |
| 2 | Name | Milestone geometric threshold |
| 3 | Domain | Progression |
| 4 | Purpose | Generate an open-ended threshold series without inventing new tiers |
| 5 | Expression | `T_n = ceil(T_0 × r^n)` for `n = 0, 1, 2, …`, with `r > 1` |
| 6 | Variables | `T_0` (integer ≥ 1); `r` (rational > 1, expressed in bp); `n` (integer ≥ 0) |
| 7 | Input source | B-11 milestone definition; owning state |
| 8 | Units | State unit |
| 9 | Valid range | `T_0 ≥ 1`; `r_bp > 10,000` |
| 10 | Output range | Increasing integer series |
| 11 | Rounding | Ceiling |
| 12 | Caps | Display tier cap; the series itself is open |
| 13 | Floors | `T_0` |
| 14 | Phase | Definition publication; crossing at P6 W4 |
| 15 | Snapshot | Published series version |
| 16 | Missing data | Definition rejected |
| 17 | Invalid input | `r_bp ≤ 10,000` → `WPF-03`; `T_0 < 1` → `WPF-03` |
| 18 | Example | `T_0=10`, `r=1.5`, n=0..3 → 10, 15, 23, 34 |
| 19 | Boundary case | n=0 → `T_0`; a very large n overflows the display cap but remains a valid next threshold |
| 20 | Provisional status | **Structural**; `T_0` and `r` are **Prompt 14** |
| — | Main rule | WEP-449 |

### F-WEP-041 — Milestone level

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-041` |
| 2 | Name | Milestone level |
| 3 | Domain | Progression |
| 4 | Purpose | Determine the highest milestone level a current value has reached |
| 5 | Expression | `level = max{ n : value ≥ T_n }`, or `NONE` if `value < T_0` |
| 6 | Variables | `value` (integer ≥ 0); `T_n` (series) |
| 7 | Input source | Owning subsystem state; definition |
| 8 | Units | Ordinal |
| 9 | Valid range | `value ≥ 0` |
| 10 | Output range | `NONE` or `0…n` |
| 11 | Rounding | None |
| 12 | Caps | Display cap |
| 13 | Floors | None |
| 14 | Phase | P6 W4 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | No level; `WPF-23` |
| 17 | Invalid input | Negative value → `WPF-23` |
| 18 | Example | value 30, series 10/15/23/34 → level 2 (23 reached, 34 not) |
| 19 | Boundary case | value exactly 23 → level 2; value 9 → `NONE` |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-449, WEP-455 |

### F-WEP-042 — Honour closure check

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-042` |
| 2 | Name | Honour closure check |
| 3 | Domain | Progression |
| 4 | Purpose | Decide whether an honour is still eligible to be granted |
| 5 | Expression | `open = (closure = WORLD_STATE) ∨ (closure = WINDOW ∧ current_turn ≤ window_end) ∨ (closure = FIRST_N ∧ granted_count < N ∧ current_turn ≤ disclosure_end)` |
| 6 | Variables | `closure` (enum); `current_turn` (turn); `window_end` (turn); `granted_count` (≥0); `N` (≥1); `disclosure_end` (turn) |
| 7 | Input source | B-11 honour definition and grant records |
| 8 | Units | Boolean |
| 9 | Valid range | Counts ≥ 0; N ≥ 1 |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | `granted_count < N` |
| 13 | Floors | None |
| 14 | Phase | P6 W4 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; no grant |
| 17 | Invalid input | FIRST_N without disclosure_end → definition invalid, `WPF-01` |
| 18 | Example | FIRST_N, N=10, 4 granted, within disclosure → `TRUE`; 10 granted → `FALSE` |
| 19 | Boundary case | A world-state honour remains open in principle forever; a window honour closes exactly at `window_end + 1` |
| 20 | Provisional status | **Structural**; N and windows are **Prompt 14** |
| — | Main rule | WEP-464, WEP-481 |

### F-WEP-043 — Season window and reset scope

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-043` |
| 2 | Name | Season window and reset scope |
| 3 | Domain | Progression |
| 4 | Purpose | Define the season boundaries and exactly what a rollover resets |
| 5 | Expression | `open_turn = season_start`; `close_turn = season_start + season_length`; reset set = `{seasonal standings, seasonal objective progress, seasonal achievement progress}`; preserved set = `{national state, records, honours, chronicle, snapshots}` |
| 6 | Variables | `season_start` (turn); `season_length` (integer ≥ 1) |
| 7 | Input source | B-02 world clock; B-11 season table |
| 8 | Units | Turns; set |
| 9 | Valid range | `season_length ≥ 1` |
| 10 | Output range | Boundaries; two sets |
| 11 | Rounding | None |
| 12 | Caps | Length cap (provisional) |
| 13 | Floors | 1 |
| 14 | Phase | P6 W4/P7 |
| 15 | Snapshot | Segment boundaries |
| 16 | Missing data | No season; `WPF-03` |
| 17 | Invalid input | `season_length ≤ 0` → `WPF-03`; overlap with an existing season → `WPF-34` |
| 18 | Example | start 10,000, length 1,080 → close 11,080; seasonal standings and progress reset; records preserved |
| 19 | Boundary case | The close turn is the first turn of the next season; the last snapshot of the old season is archived |
| 20 | Provisional status | **Structural**; length is **Prompt 14** |
| — | Main rule | WEP-465…WEP-476 |

### F-WEP-044 — Scope classification

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-044` |
| 2 | Name | Scope classification |
| 3 | Domain | Progression |
| 4 | Purpose | Enforce nation/account scope and survival rules |
| 5 | Expression | `survives_reroll = (scope = ACCOUNT) ∧ non_transferable ∧ ¬re_earnable`; otherwise `FALSE` |
| 6 | Variables | `scope` (enum); `non_transferable` (boolean); `re_earnable` (boolean) |
| 7 | Input source | B-11 object definition; B-03 reroll rules |
| 8 | Units | Boolean |
| 9 | Valid range | Enumerated |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | Definition publication; applied at reroll |
| 15 | Snapshot | Reroll event |
| 16 | Missing data | Default nation scope |
| 17 | Invalid input | Account scope with transferable value → `WPF-01` |
| 18 | Example | A nation-scope "first campaign" honour → `FALSE` (forfeited); an account-scope tutorial record → `TRUE` |
| 19 | Boundary case | An account-scope object that is re-earnable is invalid, not merely non-surviving |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-031, WEP-443, WEP-452 |

---

## 8. Reward and history formulas

### F-WEP-045 — Reward qualification predicate

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-045` |
| 2 | Name | Reward qualification predicate |
| 3 | Domain | Reward |
| 4 | Purpose | Decide whether a defined reward may be granted to a recipient |
| 5 | Expression | `reward = source_complete ∧ eligible ∧ disclosed ∧ ¬deduped ∧ cap_ok ∧ class_allowed` |
| 6 | Variables | `source_complete`, `eligible`, `disclosed`, `deduped`, `cap_ok`, `class_allowed` (booleans) |
| 7 | Input source | B-11 source object; B-03; B-04 |
| 8 | Units | Boolean |
| 9 | Valid range | Booleans |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | Reward cap |
| 13 | Floors | None |
| 14 | Phase | P6 W4/W5 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `FALSE`; `DEFERRED` |
| 17 | Invalid input | A material class not allowed by D-159 → `WPF-31` |
| 18 | Example | Complete, eligible, disclosed, key unused, cap available, class allowed → `TRUE` |
| 19 | Boundary case | A recognition reward may pass with no cap; a material reward always requires the cap check |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-506…WEP-514 |

### F-WEP-046 — Reward amount and cap

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-046` |
| 2 | Name | Reward amount and cap |
| 3 | Domain | Reward |
| 4 | Purpose | Compute a material grant within published per-recipient, per-window and world-share caps |
| 5 | Expression | `amount = clamp(base_amount, 0, min(per_recipient_cap, per_window_remaining, world_share_remaining))` |
| 6 | Variables | `base_amount` (integer ≥ 0); caps and remaining values (≥0) |
| 7 | Input source | B-11 reward definition; B-04 supply |
| 8 | Units | Crown or resource unit |
| 9 | Valid range | Non-negative |
| 10 | Output range | 0…smallest cap |
| 11 | Rounding | Floor |
| 12 | Caps | Min of the three caps |
| 13 | Floors | 0 |
| 14 | Phase | P6 W4/W5 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | `DEFERRED`, `WPF-30` |
| 17 | Invalid input | Negative base → `WPF-30`; no cap defined → definition invalid, `WPF-01` |
| 18 | Example | base 100; per-recipient 200; window remaining 60; world-share remaining 500 → 60 |
| 19 | Boundary case | A remaining cap of 0 → amount 0; the reward is `DEFERRED`, not silently granted |
| 20 | Provisional status | **Provisional**; all caps and base amounts are **Prompt 14** |
| — | Main rule | WEP-542 |

### F-WEP-047 — Reward dedupe key

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-047` |
| 2 | Name | Reward dedupe key |
| 3 | Domain | Reward |
| 4 | Purpose | Guarantee at most one grant per achievement key |
| 5 | Expression | `reward_key = H(nation_id ‖ achievement_id ‖ achievement_version ‖ scope_key ‖ tier_id)`; `deduped = exists(reward_key)` |
| 6 | Variables | Components (non-empty); `tier_id` (0 if none) |
| 7 | Input source | B-11 grant records |
| 8 | Units | String; boolean |
| 9 | Valid range | Non-empty |
| 10 | Output range | Fixed-length key; boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W4/W5 |
| 15 | Snapshot | Frozen baseline |
| 16 | Missing data | Fail `WPF-30` |
| 17 | Invalid input | Empty component → `WPF-30` |
| 18 | Example | nation 42, achievement ACH-7, version 1, scope "season:2026-Q4", tier 2 → one stable key; a second claim returns the existing grant |
| 19 | Boundary case | A different season produces a different key and a different grant; the same season and tier never grants twice |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-510, WEP-548 |

### F-WEP-048 — Contribution allocation (RETIRED)

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-048` |
| 2 | Name | Contribution allocation — retired |
| 3 | Domain | Reward |
| 4 | Purpose | **RETIRED in the 11B-C2 correction.** No authorized collective material-reward use case exists. The ID is retained for traceability; this is not an active formula. |
| 5 | Expression | None — retired. No active calculation. |
| 6 | Variables | None — retired. |
| 7 | Input source | None — retired. |
| 8 | Units | None. |
| 9 | Valid range | Not applicable. |
| 10 | Output range | Not applicable. |
| 11 | Rounding | Not applicable. |
| 12 | Caps | Not applicable. |
| 13 | Floors | Not applicable. |
| 14 | Phase | Not applicable. |
| 15 | Snapshot | Not applicable. |
| 16 | Missing data | Not applicable. |
| 17 | Invalid input | Any use of this formula is invalid. |
| 18 | Example | None — see the retirement note below. |
| 19 | Boundary case | None — see the retirement note below. |
| 20 | Provisional status | **Retired** — no lawful use case; WEP-515, WEP-519, WEP-540 and WEP-541 exclude the only plausible material path. |
| — | Main rule | None — retired. See WEP-540, WEP-541 and progress log §70. |

**Why it is retired.** The formula allocated a numeric total among contributors. No B-11 rule authorizes a collective material-reward pool: WEP-515 makes the recipient the nation that satisfied the condition, WEP-519 requires each event reward to have a recorded participant and verified completion, WEP-540 allows only a system-generated grant or a transfer from an existing authorized pool, and WEP-541 prohibits alliance-funded rewards and nation-to-nation prizes. WEP-079, WEP-212 and WEP-335 make alliance recognition honour-only, and WEP-500 makes non-material recognition a non-quantity label, so it cannot be divided. WEP-548 and WEP-555, the former references, govern stacking and audit, not allocation. Retiring the formula is therefore the only lawful resolution; authorizing a system-funded collective pool would require a new decision and a new rule, which this correction does not make.

### F-WEP-049 — Conservation check

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-049` |
| 2 | Name | Conservation check |
| 3 | Domain | Reward |
| 4 | Purpose | Prove that a material grant enters the B-04 conservation identity exactly once |
| 5 | Expression | `ok = (opening_balances + production + one_time_rewards + transfers_in − consumption − transfers_out = closing_balances)` and `Σ grants_by_key = Σ ledger_rewards_by_key` |
| 6 | Variables | B-04 identity terms (integers); grant and ledger sets |
| 7 | Input source | B-04 `ECN-111`/`ECN-101`; B-11 reward records |
| 8 | Units | Crown/resource units |
| 9 | Valid range | Integers |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P7 |
| 15 | Snapshot | Turn close |
| 16 | Missing data | `FALSE`; invariant failure |
| 17 | Invalid input | A mismatch → `WPF-40`; the turn's B-11 invariant fails |
| 18 | Example | Grants {A:100, B:50} and ledger {A:100, B:50}; identity holds → `TRUE` |
| 19 | Boundary case | Zero rewards → the identity still holds; a record without a ledger entry → `FALSE` |
| 20 | Provisional status | **Structural** |
| — | Main rule | WEP-539, WEP-617 |

### F-WEP-050 — Chronicle notability flag

| # | Field | Content |
|---|---|---|
| 1 | Identifier | `F-WEP-050` |
| 2 | Name | Chronicle notability flag |
| 3 | Domain | History |
| 4 | Purpose | Apply the UD-024 quality bar deterministically |
| 5 | Expression | `notable = permanent_event ∨ rank1_change ∨ top10_entry_or_exit ∨ honour_granted ∨ season_open_close_champion ∨ correction_or_redaction` |
| 6 | Variables | Booleans; `rank`, `top10` set |
| 7 | Input source | B-11 records; sealed snapshots |
| 8 | Units | Boolean |
| 9 | Valid range | Booleans |
| 10 | Output range | Boolean |
| 11 | Rounding | None |
| 12 | Caps | None |
| 13 | Floors | None |
| 14 | Phase | P6 W4 |
| 15 | Snapshot | W3 sealed snapshot for rank changes |
| 16 | Missing data | `FALSE`; no entry |
| 17 | Invalid input | Unknown category → `WPF-34` |
| 18 | Example | A nation moves from rank 11 to rank 10 → `TRUE`; a nation stays at rank 40 → `FALSE` |
| 19 | Boundary case | A tie group entering the top 10 counts as an entry for every tied nation in it |
| 20 | Provisional status | **Structural** (the bar is D-158; the top-10 size is **Prompt 14**) |
| — | Main rule | WEP-681 |

---

## 9. Validation summary

**Counts.** **50 formula IDs** (`F-WEP-001`…`F-WEP-050`): 49 active + 1 retired (`F-WEP-048`). Active categories: 14 event, 12 objective, 12 standing, 6 progression, 4 reward and 1 history; the retired ID is in the reward category.
**Active:** 49 + **retired:** 1 (`F-WEP-048`). **Structural (active):** 43. **Provisional:** 6 — `F-WEP-011`, `F-WEP-021`, `F-WEP-029`, `F-WEP-030`, `F-WEP-033`, `F-WEP-046`. Of the 43 active structural formulas, **20 contain a Prompt 14 parameter** (`F-WEP-003`, `004`, `005`, `007`, `009`, `010`, `012`, `015`, `016`, `019`, `024`, `025`, `031`, `034`, `035`, `036`, `040`, `042`, `043`, `050`) and **23 contain no calibration parameter**. These counts are derived from field 20; the 11B-C2 correction retired `F-WEP-048` and changed no other classification.
**Undefined variables:** 0. **Missing mandatory fields:** 0. **Duplicate formula IDs:** 0. **Unresolved references:** 0.
**Calibration owner:** Prompt 14 for every provisional parameter; structural constants are fixed by this register; no owner-reserved value is present.

**Global invariants checked by the validator (not by runtime):**

1. Every `F-WEP-` ID in the rulebook exists here.
2. Every formula has all 20 fields and a main-rule reference.
3. Every variable is declared in field 6 and has a source in field 7.
4. Every division has a zero-denominator branch.
5. Every formula states rounding, cap or floor where the operation requires it.
6. Every provisional formula names Prompt 14.
7. No formula reads wall-clock time, login state or request order.
8. No formula creates a balance, currency or resource.
9. No formula reads a private value into a public standing.
10. No formula uses a hidden constant.

**What this register does not prove.** It does not prove that any value is balanced, that any event fired, that any standing was computed or that any reward was granted. Every example is synthetic. Prompt 14 calibrates; Prompt 11C tests; Stage 3 measures.

*End of B-11 formula register.*


