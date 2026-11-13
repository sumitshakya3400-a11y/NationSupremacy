# B-13D — UI acceptance test catalogue

**Version:** 1.0 · **Created:** 2026-11-13 · **Stage 2, Prompt 13D** · **Status:** designed acceptance tests only.
**Companion to:** [`23_ui_system_integration_and_traceability.md`](23_ui_system_integration_and_traceability.md) · [`23_ui_integration_contracts.md`](23_ui_integration_contracts.md) · [`23_prompt_13_final_reconciliation_and_acceptance.md`](23_prompt_13_final_reconciliation_and_acceptance.md).

**Evidence boundary.** No test in this catalogue has been implemented, executed, passed or failed against a running interface. **No built UI exists**, so every `UAT-` row is **SPECIFIED** — a designed scenario with an observable expected result — except where a production dependency genuinely prevents even a future pass (`BLOCKED`). A documentation validator is not a UI test; a specification is not a pass.

---

## 1. Test design method

### 1.1 Sources

- Screen content and A–K fields: `21_screen_specifications.md`.
- Component content and states: `21_component_specifications.md`, `22_interaction_states_and_feedback.md`.
- Journeys, flows and tutorials: `22_player_journey_specifications.md`.
- Rules, formulas, permissions and failure codes: B-02…B-12 and their workflow companions.
- Contracts: `23_ui_integration_contracts.md`.
- Integration mapping: `23_ui_system_integration_and_traceability.md` (Matrix A).

### 1.2 Required fields

Every scenario test has: test ID, name, category, priority, preconditions, related screen(s), related flow, related requirement(s), related system(s), contract, ordered steps, expected result, failure expectation, acceptance condition, status and evidence. Screen tests use a compact form of the same fields; their steps and expected results are fixed by the shared rule below and their per-screen evidence is the A–K body.

### 1.3 Status vocabulary

| Status | Meaning |
|---|---|
| `SPECIFIED` | Designed, not implemented, not executed |
| `BLOCKED` | Cannot be passed until a named production dependency is resolved |
| `IMPLEMENTED` | A built test exists (never used in 13D) |
| `EXECUTED` | A built test has run (never used in 13D) |
| `PASSED` / `FAILED` | Execution outcomes (never used in 13D) |

### 1.4 Common fixture vocabulary

- `AN` — active nation owned by the viewer; `AN2` — a second active nation owned by another account.
- `ADM` — a holder of the stated admin role; `R-MOD`, `R-SMOD`, `R-AUD`, `R-OPS`, `R-SEC`, `R-INV` as defined by B-12.
- `T-n` — a turn/slot reference; `P0`…`P7` phases; UTC boundaries.
- `G-1…G-6` — Global Trade release gates (not met).
- `BLK` — the screen/feature is absent by gate and must not render.

### 1.5 Screen-test common rule

**Steps:** open the screen with the stated access; compare the rendered content against fields A–K; exercise every applicable `ST-` state declared in the body; attempt every control and verify permission/precondition enforcement. **Expected:** every A–K field, non-negotiable field and declared state is present; no control exists without a governing rule; no field exceeds the viewer's visibility class. **Failure expectation:** any missing A–K field, invented value/control, missing state, or unauthorized disclosure fails the test. **Acceptance:** zero deviations from the screen body and its Matrix A row.

---

## 2. Category A — Screen completeness (`UAT-SCR-001`…`UAT-SCR-100`)

| Test ID | Screen | Steps | Expected | Failure expectation | Acceptance condition | Screens | Requirement | System | Contract | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-SCR-001` | `SCR-001` Landing | Common rule | Premise, public entry paths, no live counts below k=5 | Any authenticated data or count | Zero deviations | `SCR-001` | `REQ-870` | SHELL | `UIX-01` | SPECIFIED | 13B §1 |
| `UAT-SCR-002` | `SCR-002` Registration | Common rule | E-mail pair, referrer, terms, multi-account notice | Nation creation before verification | Zero deviations | `SCR-002` | `REQ-871` | ACC | `UIX-02` | SPECIFIED | 13B §1 |
| `UAT-SCR-003` | `SCR-003` Login | Common rule | Credentials, keep-session, reset, public shell only | Another account's data | Zero deviations | `SCR-003` | `REQ-872` | ACC | `UIX-01` | SPECIFIED | 13B §1 |
| `UAT-SCR-004` | `SCR-004` Password reset | Common rule | Reset route; no account enumeration; no creation | Existence disclosure | Zero deviations | `SCR-004` | `REQ-873` | ACC | `UIX-02` | SPECIFIED | 13B §1 |
| `UAT-SCR-005` | `SCR-005` Recovery code | Common rule | Single-use code, consumption state, custody rules | Bypass of D-041 | Zero deviations | `SCR-005` | `REQ-874` | ACC | `UIX-02` | SPECIFIED | 13B §1 |
| `UAT-SCR-006` | `SCR-006` Verification | Common rule | Pending state, resend limit, verified transition, no token | Token exposure | Zero deviations | `SCR-006` | `REQ-875` | ACC | `UIX-02` | SPECIFIED | 13B §1 |
| `UAT-SCR-007` | `SCR-007` Nation creation | Common rule | Name/short name/emblem/posture; start state; awaiting first turn | Creation before verification | Zero deviations | `SCR-007` | `REQ-876` | ACC | `UIX-03` | SPECIFIED | 13B §1 |
| `UAT-SCR-008` | `SCR-008` Onboarding | Common rule | Real shell, true zero-state, one-time completion | Re-granted completion | Zero deviations | `SCR-008` | `REQ-877` | ACC | `UIX-04` | SPECIFIED | 13B §1 |
| `UAT-SCR-009` | `SCR-009` First objectives | Common rule | Objective categories, optionality, no award on view | Objective awarded by viewing | Zero deviations | `SCR-009` | `REQ-878` | WORLD | `UIX-04/24` | SPECIFIED | 13B §1 |
| `UAT-SCR-010` | `SCR-010` Public profile | Common rule | Twelve-section public object; awaiting/retired states | E-mail/account/IP/enforcement | Zero deviations | `SCR-010` | `REQ-879` | ACC | `UIX-07` | SPECIFIED | 13B §1 |
| `UAT-SCR-011` | `SCR-011` Account home | Common rule | Account state, nation linkage, sessions, closure, support | Restricted-state accusation | Zero deviations | `SCR-011` | `REQ-880` | ACC | `UIX-27` | SPECIFIED | 13B §1 |
| `UAT-SCR-012` | `SCR-012` Account closure | Common rule | Cooling, retained restrictions, no shield, retention | Closure as shield | Zero deviations | `SCR-012` | `REQ-881` | ACC | `UIX-27` | SPECIFIED | 13B §1 |
| `UAT-SCR-013` | `SCR-013` Digest | Common rule | Bounded settled changes, pending, due items, cause/deep link | New event type or open board | Zero deviations | `SCR-013` | `REQ-882` | TURN | `UIX-05/06` | SPECIFIED | 13B §2 |
| `UAT-SCR-014` | `SCR-014` Inbox | Common rule | All pending kinds, due order, owning system, deep links | Missing pending kind | Zero deviations | `SCR-014` | `REQ-883` | TURN | `UIX-06` | SPECIFIED | 13B §2 |
| `UAT-SCR-015` | `SCR-015` Overview | Common rule | Six labelled registers, six number types, section links | Merged/unnamed figures | Zero deviations | `SCR-015` | `REQ-884` | ECON | `UIX-07` | SPECIFIED | 13B §2 |
| `UAT-SCR-016` | `SCR-016` Turn status | Common rule | Turn, boundary, phase, queued actions, settlement states | Invented success | Zero deviations | `SCR-016` | `REQ-885` | TURN | `UIX-05` | SPECIFIED | 13B §2 |
| `UAT-SCR-017` | `SCR-017` Chronicle | Common rule | Class-P history, filters, as-of, retention, restricted split | Restricted fact via counts | Zero deviations | `SCR-017` | `REQ-886` | WORLD | `UIX-07/24` | SPECIFIED | 13B §2 |
| `UAT-SCR-018` | `SCR-018` Network View | Common rule | Symbolic nodes/edges, filters, legend, peeks; no coordinates | Geographic map or distance | Zero deviations | `SCR-018` | `REQ-887` | DIP | `UIX-07` | SPECIFIED | 13B §2 |
| `UAT-SCR-019` | `SCR-019` Alerts | Common rule | Existing events, three tiers, non-opt-out locked | Fabricated/mutated event | Zero deviations | `SCR-019` | `REQ-888` | TURN | `UIX-06` | SPECIFIED | 13B §2 |
| `UAT-SCR-020` | `SCR-020` Pins | Common rule | Absent until fair-play review | Stub/teaser | Zero deviations | `SCR-020` | `REQ-889` | SHELL | `UIX-P01` | SPECIFIED | 13B §2 |
| `UAT-SCR-021` | `SCR-021` Political Panel | Common rule | Six-state banner, identity, leader split, six supports | State shown as penalty | Zero deviations | `SCR-021` | `REQ-890` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-022` | `SCR-022` Government | Common rule | Permanent government, five channels, equal disadvantages | Advantages only | Zero deviations | `SCR-022` | `REQ-891` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-023` | `SCR-023` Approval/stability | Common rule | Six supports with weights/terms; integers; no invented bands | Invented band names | Zero deviations | `SCR-023` | `REQ-892` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-024` | `SCR-024` Policy axes | Common rule | Both axes, effect/cost, 12-turn cooldown, next eligible | Second change inside cooldown | Zero deviations | `SCR-024` | `REQ-893` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-025` | `SCR-025` Election dashboard | Common rule | Anchor dates, turnout weights, challengers, no live countdown | Wall-clock countdown as truth | Zero deviations | `SCR-025` | `REQ-894` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-026` | `SCR-026` Campaign actions | Common rule | Exactly three types, cost/effect, charge once, no cancel | Fourth type or refund | Zero deviations | `SCR-026` | `REQ-895` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-027` | `SCR-027` Election result | Common rule | Outcome banner, 12-turn transition, 800 bp disclosure | Administration/government confusion | Zero deviations | `SCR-027` | `REQ-896` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-028` | `SCR-028` Crisis | Common rule | Crisis state, end turn, 18-turn effect, recovery actions | Ban/penalty framing | Zero deviations | `SCR-028` | `REQ-897` | POL | `UIX-14` | SPECIFIED | 13B §3 |
| `UAT-SCR-029` | `SCR-029` Treasury | Common rule | Six separated registers, as-of, triple | Total-only balance | Zero deviations | `SCR-029` | `REQ-898` | ECON | `UIX-08` | SPECIFIED | 13B §4 |
| `UAT-SCR-030` | `SCR-030` Budget | Common rule | Opex/capex split, wealth as statistic, austerity/recovery | Wealth shown as spendable | Zero deviations | `SCR-030` | `REQ-899` | ECON | `UIX-08` | SPECIFIED | 13B §4 |
| `UAT-SCR-031` | `SCR-031` Reports | Common rule | Append-only records, per-turn aggregates, causes, exports | Editable history | Zero deviations | `SCR-031` | `REQ-900` | ECON | `UIX-08` | SPECIFIED | 13B §4 |
| `UAT-SCR-032` | `SCR-032` Production policy | Common rule | Policy/manual modes, reservation preview, three modes | Order without preview | Zero deviations | `SCR-032` | `REQ-901` | ECON | `UIX-09` | SPECIFIED | 13B §4 |
| `UAT-SCR-033` | `SCR-033` Resources | Common rule | Triple per resource/space, capacity vs holdings, book values | Total-only presentation | Zero deviations | `SCR-033` | `REQ-902` | ECON | `UIX-10` | SPECIFIED | 13B §4 |
| `UAT-SCR-034` | `SCR-034` Power | Common rule | Supply, demand, surplus/shortfall, `power_pct`, derated | Stored power balance | Zero deviations | `SCR-034` | `REQ-903` | ECON | `UIX-10` | SPECIFIED | 13B §4 |
| `UAT-SCR-035` | `SCR-035` Trade inbox | Common rule | In/out chains, terms, revision, expiry, triple, no reservation | Reservation at creation | Zero deviations | `SCR-035` | `REQ-904` | MKT | `UIX-15` | SPECIFIED | 13B §4 |
| `UAT-SCR-036` | `SCR-036` Compose offer | Common rule | Five lines/side, pledge/imbalance, window, rate limit, confirm | More than five lines | Zero deviations | `SCR-036` | `REQ-905` | MKT | `UIX-15` | SPECIFIED | 13B §4 |
| `UAT-SCR-037` | `SCR-037` Offer detail | Common rule | Two-sided record, obligations, atomic state, shared reference | Third-party view | Zero deviations | `SCR-037` | `REQ-906` | MKT | `UIX-15` | SPECIFIED | 13B §4 |
| `UAT-SCR-038` | `SCR-038` Global Trade board | Common rule | Absent; no preview/stub/statistic | Any board rendering | Zero deviations | `SCR-038` | `REQ-907` | MKT | `UIX-B01` | SPECIFIED | 13B §4 |
| `UAT-SCR-039` | `SCR-039` Listing detail | Common rule | Absent with `SCR-038` | Partial listing | Zero deviations | `SCR-039` | `REQ-908` | MKT | `UIX-B01` | SPECIFIED | 13B §4 |
| `UAT-SCR-040` | `SCR-040` Trade history | Common rule | Pre-gate own history, labelled statistics, `INSUFFICIENT_SAMPLE` | Zero in place of suppressed | Zero deviations | `SCR-040` | `REQ-909` | MKT | `UIX-16` | SPECIFIED | 13B §4 |
| `UAT-SCR-041` | `SCR-041` Cities overview | Common rule | Twelve cities + capital on one screen; no pagination | Paginated city set | Zero deviations | `SCR-041` | `REQ-910` | CITY | `UIX-11` | SPECIFIED | 13B §5 |
| `UAT-SCR-042` | `SCR-042` City detail | Common rule | Infrastructure range, housing, `used / total` DC, projection | DC as resource | Zero deviations | `SCR-042` | `REQ-911` | CITY | `UIX-11` | SPECIFIED | 13B §5 |
| `UAT-SCR-043` | `SCR-043` Construction | Common rule | One slot, URB-148 preview, refund, cancel state | Multi-item queue | Zero deviations | `SCR-043` | `REQ-912` | CITY | `UIX-11` | SPECIFIED | 13B §5 |
| `UAT-SCR-044` | `SCR-044` Chains | Common rule | Batches, inputs, output, cost, maintenance, power, `UNMAINTAINED` | Hidden blocking reason | Zero deviations | `SCR-044` | `REQ-913` | CITY | `UIX-09/10` | SPECIFIED | 13B §5 |
| `UAT-SCR-045` | `SCR-045` Research | Common rule | Tree, costs, prerequisites, four states, one project, RP split | Two active projects | Zero deviations | `SCR-045` | `REQ-914` | CITY | `UIX-13` | SPECIFIED | 13B §5 |
| `UAT-SCR-046` | `SCR-046` Found city | Common rule | Cost gate, threshold, expansion slot, no cooldown, start state | Invented cooldown | Zero deviations | `SCR-046` | `REQ-915` | CITY | `UIX-12` | SPECIFIED | 13B §5 |
| `UAT-SCR-047` | `SCR-047` Diplomatic overview | Common rule | Six views, directional posture, agreements/embargo lifecycle | Fake statistics | Zero deviations | `SCR-047` | `REQ-916` | DIP | `UIX-17` | SPECIFIED | 13B §6 |
| `UAT-SCR-048` | `SCR-048` Pair screen | Common rule | Both postures, bilateral agreements, breach fact, restriction | Other pair's pending terms | Zero deviations | `SCR-048` | `REQ-917` | DIP | `UIX-17` | SPECIFIED | 13B §6 |
| `UAT-SCR-049` | `SCR-049` Proposal | Common rule | Named counterparty, ten-field confirmation, withdraw/counter | Delegation implied | Zero deviations | `SCR-049` | `REQ-918` | DIP | `UIX-17` | SPECIFIED | 13B §6 |
| `UAT-SCR-050` | `SCR-050` Agreement | Common rule | Exact type/lifecycle/parties/obligations/duration | Active badge when pending | Zero deviations | `SCR-050` | `REQ-919` | DIP | `UIX-17` | SPECIFIED | 13B §6 |
| `UAT-SCR-051` | `SCR-051` Publication | Common rule | Pending-private→accepted-private→active-public; k=5 | Public pending terms | Zero deviations | `SCR-051` | `REQ-920` | DIP | `UIX-17` | SPECIFIED | 13B §6 |
| `UAT-SCR-052` | `SCR-052` Relations history | Common rule | Private/public split, retention, retired label | Merged history | Zero deviations | `SCR-052` | `REQ-921` | DIP | `UIX-17` | SPECIFIED | 13B §6 |
| `UAT-SCR-053` | `SCR-053` Alliance home | Common rule | Public identity, roles, member count, treaties/wars | Member internals | Zero deviations | `SCR-053` | `REQ-922` | ALL | `UIX-18` | SPECIFIED | 13B §6 |
| `UAT-SCR-054` | `SCR-054` Membership | Common rule | Applicants admin-only, member states, non-covered, in-product | Applicant exposed | Zero deviations | `SCR-054` | `REQ-923` | ALL | `UIX-18` | SPECIFIED | 13B §6 |
| `UAT-SCR-055` | `SCR-055` Governance | Common rule | Constitution, role matrix, permission-denied states | Render implies permission | Zero deviations | `SCR-055` | `REQ-924` | ALL | `UIX-18` | SPECIFIED | 13B §6 |
| `UAT-SCR-056` | `SCR-056` Tax brackets | Common rule | Named bracket, separate rates 0–10,000 bp, effective turn, 0% fallback | >100% or hidden fallback | Zero deviations | `SCR-056` | `REQ-925` | ALL | `UIX-19` | SPECIFIED | 13B §6 |
| `UAT-SCR-057` | `SCR-057` Alliance finances | Common rule | Four ARL categories, immutable receipts, no withdrawal | Withdraw/distribute control | Zero deviations | `SCR-057` | `REQ-926` | ALL | `UIX-19` | SPECIFIED | 13B §6 |
| `UAT-SCR-058` | `SCR-058` Alliance diplomacy | Common rule | Treaty objects, record-only/NAP, coverage, no military authority | Collective command control | Zero deviations | `SCR-058` | `REQ-927` | ALL | `UIX-20` | SPECIFIED | 13B §6 |
| `UAT-SCR-059` | `SCR-059` Military overview | Common rule | Own OP, cap, regeneration, readiness, owner entry | Another nation's data | Zero deviations | `SCR-059` | `REQ-928` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-060` | `SCR-060` Forces | Common rule | Roster, Food demand, paid/short, impairment, `RATION_SHORT` | Exact other stock | Zero deviations | `SCR-060` | `REQ-929` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-061` | `SCR-061` War board | Common rule | Owner-only, own OP/reservations/operations/losses | Alliance merged data | Zero deviations | `SCR-061` | `REQ-930` | WAR | `UIX-21` | SPECIFIED | 13B §7 |
| `UAT-SCR-062` | `SCR-062` Conflicts | Common rule | Public declared facts, thin list, no hidden-detail implication | Implied private detail | Zero deviations | `SCR-062` | `REQ-931` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-063` | `SCR-063` War detail | Common rule | Field-filtered, four bands, public city damage | Exact force/inventory | Zero deviations | `SCR-063` | `REQ-932` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-064` | `SCR-064` Battle report | Common rule | WAR-088 to participants; public summary elsewhere | Exact strength public | Zero deviations | `SCR-064` | `REQ-933` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-065` | `SCR-065` War reports | Common rule | Conservation-visible losses, impairment basis, campaign figures | Leaked restricted values | Zero deviations | `SCR-065` | `REQ-934` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-066` | `SCR-066` Military history | Common rule | Class-P records, filters, retention, participant split | Restricted via ordering | Zero deviations | `SCR-066` | `REQ-935` | WAR | `UIX-23` | SPECIFIED | 13B §7 |
| `UAT-SCR-067` | `SCR-067` Settlement | Common rule | Every term, one live, expiry, surrender off-ramp | Silence as consent | Zero deviations | `SCR-067` | `REQ-936` | WAR | `UIX-22` | SPECIFIED | 13B §7 |
| `UAT-SCR-068` | `SCR-068` Intelligence | Common rule | Placeholder only; no data/route/action | Any intelligence surface | Zero deviations | `SCR-068` | `REQ-937` | WAR | `UIX-B02` | SPECIFIED | 13B §7 |
| `UAT-SCR-069` | `SCR-069` Events | Common rule | Closed catalogue, states, eligibility, detail links | Live/unregistered event | Zero deviations | `SCR-069` | `REQ-938` | WORLD | `UIX-24` | SPECIFIED | 13B §8 |
| `UAT-SCR-070` | `SCR-070` Event detail | Common rule | Cause/hazard with registered consequence; exact source | Unregistered modifier | Zero deviations | `SCR-070` | `REQ-939` | WORLD | `UIX-24` | SPECIFIED | 13B §8 |
| `UAT-SCR-071` | `SCR-071` Objectives | Common rule | Twelve categories, lifecycle, optional, penalty-free | Presence/spend requirement | Zero deviations | `SCR-071` | `REQ-940` | WORLD | `UIX-24` | SPECIFIED | 13B §8 |
| `UAT-SCR-072` | `SCR-072` Standings | Common rule | Named lists, denominator, window, P6/P7, no live tick | Rank without denominator | Zero deviations | `SCR-072` | `REQ-941` | WORLD | `UIX-24` | SPECIFIED | 13B §8 |
| `UAT-SCR-073` | `SCR-073` Achievements | Common rule | Six classes, earned/locked, material notice | Other nation's reward | Zero deviations | `SCR-073` | `REQ-942` | WORLD | `UIX-25` | SPECIFIED | 13B §8 |
| `UAT-SCR-074` | `SCR-074` Progress | Common rule | Eight separate layers, own state/history | Composite score | Zero deviations | `SCR-074` | `REQ-943` | WORLD | `UIX-24` | SPECIFIED | 13B §8 |
| `UAT-SCR-075` | `SCR-075` Reward history | Common rule | Granted/deferred/voided/corrected, claim state | Deferred as granted | Zero deviations | `SCR-075` | `REQ-944` | WORLD | `UIX-25` | SPECIFIED | 13B §8 |
| `UAT-SCR-076` | `SCR-076` World chronicle | Common rule | Dated public record, filters, retention | Private/fabricated entry | Zero deviations | `SCR-076` | `REQ-945` | WORLD | `UIX-24` | SPECIFIED | 13B §8 |
| `UAT-SCR-077` | `SCR-077` World Health | Common rule | Per-figure k=5 or suppressed; no pre-gate chart | Placeholder axis/inferred total | Zero deviations | `SCR-077` | `REQ-946` | WORLD | `UIX-P02` | SPECIFIED | 13B §8 |
| `UAT-SCR-078` | `SCR-078` World Guide | Common rule | Section vocabulary, definitions, rule links, no image-only text | Gameplay only in image | Zero deviations | `SCR-078` | `REQ-947` | WORLD | `UIX-07` | SPECIFIED | 13B §8 |
| `UAT-SCR-079` | `SCR-079` Privacy centre | Common rule | Nine classes in player language, no SEC | SEC class rendered | Zero deviations | `SCR-079` | `REQ-948` | FP | `UIX-27` | SPECIFIED | 13B §9 |
| `UAT-SCR-080` | `SCR-080` Security settings | Common rule | Sessions, recovery custody, e-mail change, no credential | Token/key displayed | Zero deviations | `SCR-080` | `REQ-949` | ACC | `UIX-27` | SPECIFIED | 13B §9 |
| `UAT-SCR-081` | `SCR-081` Report creation | Common rule | Exact MOD-002 fields, evidence separate, retryable | Extra mandatory field | Zero deviations | `SCR-081` | `REQ-950` | FP | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-082` | `SCR-082` Report status | Common rule | Seven elements, EVD-009 tiers, no methods/thresholds | Silent tier upgrade | Zero deviations | `SCR-082` | `REQ-951` | FP | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-083` | `SCR-083` Appeal | Common rule | Route, status ladder, reasons, always reachable | Appeal blocked | Zero deviations | `SCR-083` | `REQ-952` | FP | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-084` | `SCR-084` Restrictions | Common rule | Kind/scope/end/review/appeal, no accusation | Another player's data | Zero deviations | `SCR-084` | `REQ-953` | FP | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-085` | `SCR-085` My data | Common rule | Categories, access/export states, retention, erasure vs spine | Promised deletion of spine | Zero deviations | `SCR-085` | `REQ-954` | FP | `UIX-27` | SPECIFIED | 13B §9 |
| `UAT-SCR-086` | `SCR-086` Review explanation | Common rule | Shared-network state names, clearance, review route | Matching mechanism | Zero deviations | `SCR-086` | `REQ-955` | FP | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-087` | `SCR-087` Support | Common rule | Support separate from conduct report; degraded state | Silent conversion to case | Zero deviations | `SCR-087` | `REQ-956` | FP | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-088` | `SCR-088` Changes | Common rule | Dated player-readable changes; no private case | Private case/method | Zero deviations | `SCR-088` | `REQ-957` | WORLD | `UIX-30` | SPECIFIED | 13B §9 |
| `UAT-SCR-089` | `SCR-089` Protection | Common rule | Protected until turn, visibility-only, no countdown/bonus | Bonus/countdown framing | Zero deviations | `SCR-089` | `REQ-958` | ACC | `UIX-26` | SPECIFIED | 13B §9 |
| `UAT-SCR-090` | `SCR-090` Reroll | Common rule | Re-auth, exact name/phrase, consequence list, blocks | Phrase remembered or skipped | Zero deviations | `SCR-090` | `REQ-959` | ACC | `UIX-03` | SPECIFIED | 13B §9 |
| `UAT-SCR-091` | `SCR-091` Admin console | Common rule | Only held workspaces; player nav absent | Case data to non-holder | Zero deviations | `SCR-091` | `REQ-960` | ADMIN | `UIX-28` | SPECIFIED | 13B §10 |
| `UAT-SCR-092` | `SCR-092` Moderation queue | Common rule | Assigned cases, triage, reviewer-scoped actions | SEC material exposed | Zero deviations | `SCR-092` | `REQ-961` | ADMIN | `UIX-28` | SPECIFIED | 13B §10 |
| `UAT-SCR-093` | `SCR-093` Case workspace | Common rule | Evidence matrix, 16 classes, claim tier, audited reads | Unscoped access | Zero deviations | `SCR-093` | `REQ-962` | ADMIN | `UIX-28` | SPECIFIED | 13B §10 |
| `UAT-SCR-094` | `SCR-094` Sanctions | Common rule | Six tiers, two-person, separation of duties | Single reviewer above tier | Zero deviations | `SCR-094` | `REQ-963` | ADMIN | `UIX-28` | SPECIFIED | 13B §10 |
| `UAT-SCR-095` | `SCR-095` Network review | Common rule | Five states, separate review, observation window | Matching mechanism | Zero deviations | `SCR-095` | `REQ-964` | ADMIN | `UIX-28` | SPECIFIED | 13B §10 |
| `UAT-SCR-096` | `SCR-096` Audit viewer | Common rule | Spine/preservation state, no bodies/secrets, access audited | Content/secret exposure | Zero deviations | `SCR-096` | `REQ-965` | ADMIN | `UIX-29` | SPECIFIED | 13B §10 |
| `UAT-SCR-097` | `SCR-097` Turn monitor | Common rule | Slot history, checkpoints, interrupted/failed, recovery | Invented success state | Zero deviations | `SCR-097` | `REQ-966` | TURN | `UIX-29` | SPECIFIED | 13B §10 |
| `UAT-SCR-098` | `SCR-098` Data operations | Common rule | Retention/compaction/preservation, audit consequence, confirmation | Reversible claim when not | Zero deviations | `SCR-098` | `REQ-967` | ADMIN | `UIX-29` | SPECIFIED | 13B §10 |
| `UAT-SCR-099` | `SCR-099` Announcements | Common rule | Content limits, scope, preview, no private data | Private case data | Zero deviations | `SCR-099` | `REQ-968` | ADMIN | `UIX-30` | SPECIFIED | 13B §10 |
| `UAT-SCR-100` | `SCR-100` Admin roles | Common rule | Eight roles, least privilege, step-up, no grant beyond self | Escalation | Zero deviations | `SCR-100` | `REQ-969` | ADMIN | `UIX-29` | SPECIFIED | 13B §10 |

**Screen-test tally:** 100 tests — 100 SPECIFIED, 0 BLOCKED (absence screens are tested as absence).

---

## 3. Category B — Functional interaction (`UAT-F-001`…`UAT-F-026`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-F-001` | First-time path: register, verify, create, onboard, digest | Functional | P0 | No account; valid e-mail | `SCR-001`…`009`, `013` | `FLOW-001`…`004` | `REQ-1090/1103/1105/1106` | ACC/TURN | `UIX-01`…`04` | Register → verify → create → follow/skip onboarding → open objectives → digest | Verified account owns exactly one nation; onboarding recorded once; digest is home | Nation exists unverified or onboarding re-granted | All completions observable and unique | SPECIFIED | 13C JRN-A |
| `UAT-F-002` | Login routes by account state and preserves destination | Functional | P0 | Existing accounts in four states | `SCR-003/006/007/013` | `FLOW-002` | `REQ-1104/1190` | ACC | `UIX-01` | Attempt login as verified/no-nation, unverified, restricted, valid | Each routes to the specified destination; no enumeration | Generic success/error or lost destination | Four/four routes correct | SPECIFIED | 13C JRN-A/B |
| `UAT-F-003` | Digest/inbox triage deep-links to owning action | Functional | P0 | `AN` with pending offer, proposal, application | `SCR-013/014/019` | `FLOW-005/006/027` | `REQ-1107/1108/1129` | TURN | `UIX-06` | Open digest → inbox → open each row → return | Rows ordered by due boundary; each opens its owning screen; return restores as-of | Row opens wrong/denied screen with no state | 3/3 rows correct | SPECIFIED | 13C JRN-B |
| `UAT-F-004` | Policy change enforces cooldown and confirmation | Functional | P0 | `AN`; axis change available | `SCR-024` | `FLOW-007` | `REQ-1109` | POL | `UIX-14` | Change axis → inspect effect/cost/cooldown → confirm → retry inside cooldown | Recorded once; second change disabled with next turn | Second change accepted | One change, one block | SPECIFIED | 13C FLOW-007 |
| `UAT-F-005` | Campaign action charges once and offers three types | Functional | P0 | `AN` in `ELECTORAL` | `SCR-025/026` | `FLOW-008` | `REQ-1110` | POL | `UIX-14` | Open campaign → inspect types → submit one → attempt cancel/fourth | Charge once; no cancel; exactly three types | Refund or fourth action | 3 types, 1 charge | SPECIFIED | 13C FLOW-008 |
| `UAT-F-006` | Standing production policy reserves nothing | Functional | P0 | `AN`; production available | `SCR-032` | `FLOW-009` | `REQ-1111` | ECON | `UIX-09` | Open policy → set mode/target → save | Policy applies at recurring phase; treasury unchanged now | Immediate charge | No immediate charge; policy active | SPECIFIED | 13C FLOW-009 |
| `UAT-F-007` | Manual production order reserves and settles atomically | Functional | P0 | `AN` with inputs/capacity | `SCR-032/033` | `FLOW-010` | `REQ-1112` | ECON | `UIX-09` | Preview → overbook attempt → valid submit | Overbooking rejected; valid order reserves and settles or fails atomically | Partial settlement | Atomic all-or-nothing | SPECIFIED | 13C FLOW-010 |
| `UAT-F-008` | Directed offer creation reserves nothing | Functional | P0 | `AN` with resources; `AN2` | `SCR-035/036` | `FLOW-011` | `REQ-1113` | MKT | `UIX-15` | Compose five lines → submit | Chain created; balances unchanged; expiry/rate limit shown | Reservation at creation | No reservation; chain visible | SPECIFIED | 13C FLOW-011 |
| `UAT-F-009` | Trade acceptance revalidates and settles atomically | Functional | P0 | Live chain with both sides funded | `SCR-035/037` | `FLOW-012` | `REQ-1114` | MKT/ECON | `UIX-15` | Open offer → accept → confirm | Both sides re-read; reserve; P4 settlement with one reference | Partial leg or false success | Both legs exact; one ref | SPECIFIED | 13C FLOW-012 |
| `UAT-F-010` | Counter, decline and cancel respect lifecycle | Functional | P1 | Live chain | `SCR-035`…`037` | `FLOW-013` | `REQ-1115` | MKT | `UIX-15` | Counter → decline → cancel in valid/invalid states | Revision created; terminal states block cancel | Accepted chain cancellable | Lifecycle correct | SPECIFIED | 13C FLOW-013 |
| `UAT-F-011` | Construction uses the single city slot and full preview | Functional | P0 | `AN`; empty slot; affordable | `SCR-042/043` | `FLOW-014` | `REQ-1116` | CITY | `UIX-11` | Open city → preview → confirm → attempt second | Slot claimed; preview fields exact; second blocked | Two simultaneous orders | One slot; preview matches | SPECIFIED | 13C FLOW-014 |
| `UAT-F-012` | City founding enforces its gates | Functional | P0 | `AN` eligible; resources | `SCR-041/046` | `FLOW-015` | `REQ-1117` | CITY | `UIX-12` | Inspect checklist → confirm → attempt below threshold | City created; deductions exact; no cooldown invented | Creation below threshold | Gates enforced | SPECIFIED | 13C FLOW-015 |
| `UAT-F-013` | Research enforces one active project | Functional | P0 | `AN`; no active project | `SCR-045` | `FLOW-016` | `REQ-1118` | CITY | `UIX-13` | Inspect tree → start project → attempt second | One active; cost/RP shown; second disabled | Two active projects | One active | SPECIFIED | 13C FLOW-016 |
| `UAT-F-014` | Diplomatic proposal shows ten confirmation fields | Functional | P0 | `AN`; `AN2` | `SCR-048/049` | `FLOW-017` | `REQ-1119` | DIP | `UIX-17` | Compose proposal → inspect ten fields → submit → withdraw | Proposal parties-only; fields exact; withdraw safe | Missing field; third-party visibility | 10/10 fields | SPECIFIED | 13C FLOW-017 |
| `UAT-F-015` | Proposal acceptance activates at the boundary | Functional | P0 | Pending proposal | `SCR-049`…`051` | `FLOW-018` | `REQ-1120` | DIP | `UIX-17` | Accept → inspect state → re-open publication | Acceptance recorded; activation/publication at defined boundary | Immediate false active state | State sequence exact | SPECIFIED | 13C FLOW-018 |
| `UAT-F-016` | Alliance application terminates in-product | Functional | P1 | `AN`; open alliance | `SCR-053/054` | `FLOW-019` | `REQ-1121` | ALL | `UIX-18` | Apply → respond as admin → inspect applicant privacy | Outcome recorded; applicant admin-only | External hop required | In-product outcome | SPECIFIED | 13C FLOW-019 |
| `UAT-F-017` | Alliance tax bracket accepts only valid basis points | Functional | P1 | Role with tax management | `SCR-056/057` | `FLOW-020` | `REQ-1122` | ALL | `UIX-19` | Enter 0, 10,000, 10,001, negative, decimals → save valid | Valid saved with effective turn; invalid rejected | Out-of-range accepted | Boundary values exact | SPECIFIED | 13C FLOW-020 |
| `UAT-F-018` | Military operation is owner-only and OP-reserved | Functional | P0 | `AN` owner with OP | `SCR-061` | `FLOW-021` | `REQ-1123` | WAR | `UIX-21` | Open board → select operation → inspect cost/block → confirm | Owner-only; OP reserved; exact cost/effect | Alliance path or second pool | Owner-only, one pool | SPECIFIED | 13C FLOW-021 |
| `UAT-F-019` | War declaration checks protection, NAP and Alliance | Functional | P0 | Eligible target; one blocked target | `SCR-061/063` | `FLOW-022` | `REQ-1124` | WAR | `UIX-21` | Declare on eligible → attempt blocked target → inspect audit | Eligible campaign created; blocked target refused with reason | UI bypass of block | Blocks enforced | SPECIFIED | 13C FLOW-022 |
| `UAT-F-020` | Settlement shows every term and one-live rule | Functional | P0 | Active campaign | `SCR-067` | `FLOW-023` | `REQ-1125` | WAR | `UIX-22` | Propose → inspect terms → withdraw → propose → accept | One live; withdrawal safe; no silence consent | Second live settlement | One live | SPECIFIED | 13C FLOW-023 |
| `UAT-F-021` | Surrender is always available and confirmed | Functional | P0 | Active campaign; losing state | `SCR-067` | `FLOW-024` | `REQ-1126` | WAR | `UIX-22` | Attempt surrender under all states → confirm | Surrender available; campaign ends; limited-victory disclosed | Refusal or unconfirmed end | Always available | SPECIFIED | 13C FLOW-024 |
| `UAT-F-022` | Objectives and deferred rewards never obligate | Functional | P1 | `AN` with objective and deferred reward | `SCR-009/071/073/075` | `FLOW-025/026` | `REQ-1127/1128` | WORLD | `UIX-24/25` | Dismiss objective → view deferred → claim | Dismissal penalty-free; deferred labelled; one claim | Deferred shown granted | Optional and idempotent | SPECIFIED | 13C FLOW-025/026 |
| `UAT-F-023` | Report and appeal preserve separation and route | Functional | P0 | `AN`; intake available; restricted account | `SCR-081`…`084` | `FLOW-028/029` | `REQ-1130/1131` | FP | `UIX-26` | Submit report → inspect acknowledgement → appeal under restriction | Case ref returned; appeal reachable; reasons shown | Appeal blocked or data exposed | Intake + appeal both pass | SPECIFIED | 13C FLOW-028/029 |
| `UAT-F-024` | Closure cooling and reroll exact phrase | Functional | P0 | `AN`; no reroll block | `SCR-011/012/090` | `FLOW-030/031` | `REQ-1132/1133` | ACC | `UIX-27/03` | Request closure → cancel → reopen reroll → wrong phrase → correct phrase | Cooling disclosed and cancellable; wrong phrase refused; correct reroll executes | Phrase bypass | Exact phrase enforced | SPECIFIED | 13C FLOW-030/031 |
| `UAT-F-025` | Admin decision respects role, tier and two-person rule | Functional | P0 | `ADM` with role; assigned case | `SCR-092`…`096/100` | `FLOW-032` | `REQ-1134` | ADMIN/FP | `UIX-28` | Review case → attempt above-tier → request second review → decide | Decision within tier; second review enforced; audit row appended | Single reviewer above tier | Role/tier/two-person all hold | SPECIFIED | 13C FLOW-032 |
| `UAT-F-026` | Reconnection reconciles and never repeats an action | Functional | P0 | `AN`; simulated disconnect during submit | Shell, `SCR-016` | `FLOW-033` | `REQ-1135` | TURN | `UIX-05/06` | Submit → drop connection → reconnect → re-read | Uncertain shown; no auto-repeat; conflict surfaced | False success or duplicate | Reconciliation exact | SPECIFIED | 13C FLOW-033 |

**Functional tally:** 26 tests, 26 SPECIFIED.

---

## 4. Category C — System integration (`UAT-I-001`…`UAT-I-016`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-I-001` | Session/identity contract conformance | Integration | P0 | Accounts in all states | Shell, `SCR-003/011` | `FLOW-002` | `REQ-872/1104` | ACC | `UIX-01` | Read identity; login; expire; resume; logout | Correct identity/nation scope; neutral failures; no credential exposure | Credential in UI; wrong nation scope | All contract rows hold | SPECIFIED | D2 UIX-01 |
| `UAT-I-002` | Registration/verification contract conformance | Integration | P0 | No account | `SCR-002`…`006` | `FLOW-001` | `REQ-871/873`…`875` | ACC | `UIX-02` | Register; verify; reset; recover; resend beyond limit | States and limits exact; no enumeration | Token/state leak | All rows hold | SPECIFIED | D2 UIX-02 |
| `UAT-I-003` | Nation creation/reroll and tutorial state contracts | Integration | P0 | Verified account; eligible | `SCR-007/008/090` | `FLOW-003/004/031` | `REQ-876/877/1105/1106` | ACC | `UIX-03/04` | Create; onboard; skip; reroll | One nation; one-time onboarding; exact reroll | Duplicate nation/re-grant | All rows hold | SPECIFIED | D2 UIX-03/04 |
| `UAT-I-004` | Turn state and digest/notification contracts | Integration | P0 | `AN`; pending items | Shell, `SCR-013/014/016/019` | `FLOW-005/006` | `REQ-885/882/883` | TURN | `UIX-05/06` | Read turn; open digest; acknowledge; mute permitted | As-of, states and grouping exact; non-opt-out preserved | Fabricated event | All rows hold | SPECIFIED | D2 UIX-05/06 |
| `UAT-I-005` | Object/overview and treasury read contracts | Integration | P0 | `AN`; public `AN2` | `SCR-010/015/029`…`031` | `FLOW-005` | `REQ-879/884/898`…`900` | ECON/ACC | `UIX-07/08` | Read own and other objects; inspect visibility and number types | Fields filtered; six registers; as-of | Field above class | All rows hold | SPECIFIED | D2 UIX-07/08 |
| `UAT-I-006` | Production and resource contracts | Integration | P0 | `AN`; inputs/capacity | `SCR-032`…`034/044` | `FLOW-009/010` | `REQ-901/902/1111/1112` | ECON | `UIX-09/10` | Save policy; place order; inspect resource/power | No policy charge; order atomic; capacity derived | Capacity as resource | All rows hold | SPECIFIED | D2 UIX-09/10 |
| `UAT-I-007` | Construction and founding contracts | Integration | P0 | `AN`; slot/resources/eligibility | `SCR-041`…`043/046` | `FLOW-014/015` | `REQ-911/912/915` | CITY | `UIX-11/12` | Build; demolish; found | Slot/refund/founding exact | Multi-slot or double founding | All rows hold | SPECIFIED | D2 UIX-11/12 |
| `UAT-I-008` | Research and politics contracts | Integration | P0 | `AN`; no project; electoral state | `SCR-024`…`028/045` | `FLOW-007/008/016` | `REQ-893/895/914` | CITY/POL | `UIX-13/14` | Start research; change policy; campaign | One project; cooldown; charge once | Two projects or refund | All rows hold | SPECIFIED | D2 UIX-13/14 |
| `UAT-I-009` | Directed trade and history contracts | Integration | P0 | Live chain | `SCR-035`…`037/040` | `FLOW-011`…`013` | `REQ-904`…`906` | MKT/ECON | `UIX-15/16` | Create/counter/accept/cancel; read history | Atomic settlement; no reservation at creation; pre-gate history minimal | Partial settlement | All rows hold | SPECIFIED | D2 UIX-15/16 |
| `UAT-I-010` | Diplomacy contract conformance | Integration | P0 | `AN`; `AN2` | `SCR-047`…`052` | `FLOW-017/018` | `REQ-916`…`921` | DIP | `UIX-17` | Propose; accept; inspect publication; terminate | Parties-only pending; activation boundary; k=5 | Third-party terms | All rows hold | SPECIFIED | D2 UIX-17 |
| `UAT-I-011` | Alliance membership/tax/treaty contracts | Integration | P0 | Alliance; roles; members | `SCR-053`…`058` | `FLOW-019/020` | `REQ-922`…`927` | ALL | `UIX-18`…`20` | Apply; change role; save tax; inspect ARL; propose treaty | Role bounds; rates; four categories; consent | Escalation or spend control | All rows hold | SPECIFIED | D2 UIX-18…20 |
| `UAT-I-012` | Warfare/settlement contracts | Integration | P0 | Campaign; OP | `SCR-059`…`067` | `FLOW-021`…`024` | `REQ-928`…`936` | WAR | `UIX-21`…`23` | Operate; declare; settle; surrender; read battle | Owner-only; OP single pool; one live; bands only | Alliance command path | All rows hold | SPECIFIED | D2 UIX-21…23 |
| `UAT-I-013` | World/reward contracts | Integration | P1 | `AN`; events/objectives/rewards | `SCR-069`…`076` | `FLOW-025/026` | `REQ-938`…`945` | WORLD | `UIX-24/25` | Read event/objective/standing; claim reward | Cause/effect; denominator; one claim | Composite score or double grant | All rows hold | SPECIFIED | D2 UIX-24/25 |
| `UAT-I-014` | Protection and account contracts | Integration | P0 | `AN`; open case; restricted `AN2` | `SCR-011/012/079`…`085` | `FLOW-028`…`031` | `REQ-950`…`959` | FP/ACC | `UIX-26/27` | Report; appeal; change settings; close | Exact intake; appeal reachable; cooling; no SEC | Appeal blocked | All rows hold | SPECIFIED | D2 UIX-26/27 |
| `UAT-I-015` | Admin contracts | Integration | P0 | `ADM` roles; case | `SCR-091`…`098/100` | `FLOW-032` | `REQ-960`…`969` | ADMIN | `UIX-28/29` | Review case; apply tier; read audit; recover turn | Role/tier/two-person; audit read scoped; recovery named | Unscoped audit | All rows hold subject to audit dependency | SPECIFIED | D2 UIX-28/29 |
| `UAT-I-016` | Announcement and absence contracts | Integration | P1 | Authorized role; public user | `SCR-088/099/020/038/039/068/077` | — | `REQ-957/968/889/907/908/937/946` | ADMIN/WORLD | `UIX-30/B01/B02/P01/P02` | Publish; read changes; request each absent route | Notice bounded; every absent surface renders honest absence | Any stub/teaser | Absence exact | SPECIFIED | D2 UIX-30/B01/B02/P01/P02 |

**Integration tally:** 16 tests, 16 SPECIFIED.

---

## 5. Category D — Cross-system transactions (`UAT-X-001`…`UAT-X-012`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-X-001` | Trade settlement updates treasury and resource triples consistently | Cross-system | P0 | Live chain; both funded | `SCR-029/033/035/037` | `FLOW-012` | `REQ-1196` | MKT/ECON | `UIX-15/08` | Accept trade → re-read treasury, resources, offer | Both sides' triples agree; one reference; no double count | Any screen contradicts | Three-screen agreement | SPECIFIED | D1 X-summary |
| `UAT-X-002` | Construction preview matches settlement | Cross-system | P0 | Affordable build | `SCR-042/043/029/033` | `FLOW-014` | `REQ-1116/1196` | CITY/ECON | `UIX-11/08` | Preview → confirm → wait for boundary → compare | Cost, DC, availability, book value exact | Preview differs | Exact match | SPECIFIED | D1 Matrix E |
| `UAT-X-003` | Production order appears in economic reporting at the right turn | Cross-system | P0 | Manual order executes | `SCR-032/031/033` | `FLOW-010` | `REQ-1112/900` | ECON | `UIX-09/08` | Order → settle → open reports | Report row at correct turn; cause and factor exact | Missing/duplicated row | One row, correct turn | SPECIFIED | 13C FLOW-010 |
| `UAT-X-004` | Election outcome changes administration, not government | Cross-system | P0 | Election resolves | `SCR-021/023/027/028` | `FLOW-008` | `REQ-896/1096` | POL | `UIX-14` | Resolve election → inspect banner/transition/stability | Administration changes; government persists; 12-turn transition; 800 bp disclosure | Government changed | All four facts hold | SPECIFIED | 13B SCR-027 |
| `UAT-X-005` | Alliance tax receipt and ARL identity agree | Cross-system | P0 | Taxing alliance; production | `SCR-056/057` | `FLOW-020` | `REQ-1027/1122` | ALL/ECON | `UIX-19` | Produce → collect → open ARL | `AVAILABLE = RECEIVED − RESERVED − EXPENDED`; no double deduction | Broken identity | Identity holds | SPECIFIED | B-09 ALL-187 |
| `UAT-X-006` | Settlement ends the campaign with consistent losses | Cross-system | P0 | Active campaign | `SCR-063/065/067` | `FLOW-023` | `REQ-1125/1035` | WAR | `UIX-22/23` | Settle → inspect war detail and losses | Terms, end state, losses agree; OP not restored | Contradictory records | Records agree | SPECIFIED | B-10 WAR-126 |
| `UAT-X-007` | Event consequence appears once in progression and reward | Cross-system | P1 | Registered event with reward | `SCR-069/070/074/075` | — | `REQ-1041/1128` | WORLD | `UIX-24/25` | Trigger event → open progress/reward | One consequence; one reward record; cause linked | Double grant | Single effect | SPECIFIED | B-11 WEP-619 |
| `UAT-X-008` | Fair-play restriction is consistent across gameplay surfaces | Cross-system | P0 | Restricted `AN2` | `SCR-013/019/063/084` | `FLOW-027` | `REQ-1197/953` | FP/TURN/WAR | `UIX-26/06/23` | Attempt action → inspect restriction on three surfaces | Same restriction class; same end/review; appeal reachable | Surface says allowed | Consistent restriction | SPECIFIED | B-12/NET-023 |
| `UAT-X-009` | Alliance NAP and same-alliance ban block attacks with audit | Cross-system | P0 | Alliance NAP; same alliance | `SCR-058/061/063` | `FLOW-022` | `REQ-927/1124` | ALL/WAR | `UIX-20/21` | Attempt attack via every UI path | Every path blocked with reason; audit row written | Any unblocked path | All paths blocked | SPECIFIED | AX-30 |
| `UAT-X-010` | Directed terms remain parties-only everywhere | Cross-system | P0 | Active chain; third party | `SCR-035/037/048/019` | `FLOW-011` | `REQ-906/1022` | MKT/DIP | `UIX-15` | Inspect as third party via alerts, links, peeks | No terms visible; only permitted metadata | Leak on any surface | No leak | SPECIFIED | D-030/MKT |
| `UAT-X-011` | Budget and construction separate capex from opex | Cross-system | P1 | Build with capex | `SCR-030/031/043` | `FLOW-014` | `REQ-899/1000` | ECON/CITY | `UIX-08/11` | Build → open budget/report | Capex classified separately; forecast labelled; warning if negative | Capex as opex | Classification exact | SPECIFIED | B-04 D-051 |
| `UAT-X-012` | Material reward is granted once and reflected consistently | Cross-system | P1 | Eligible reward | `SCR-073/075/033` | `FLOW-026` | `REQ-1043/1128` | WORLD/ECON | `UIX-25` | Claim → inspect reward history and resources | One grant; claim state resolved; inventory increase once | Double grant | One grant | SPECIFIED | B-11 WEP-705 |

**Cross-system tally:** 12 tests, 12 SPECIFIED.

---

## 6. Category E — Permission and security (`UAT-P-001`…`UAT-P-012`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-P-001` | Identity strip never exceeds viewer class | Permission | P0 | `AN`; public viewer; privileged viewer | Shell | — | `REQ-974/1195` | ACC | `UIX-01/07` | Inspect strip in three roles | Values filtered per class; as-of shown | Any excess field | Class exact | SPECIFIED | TR-021 |
| `UAT-P-002` | Admin root and player navigation are mutually exclusive | Permission | P0 | Player; `ADM` | `SCR-091`…`100`, shell | — | `REQ-978/1037` | ADMIN | `UIX-28` | Open as each role; attempt denied route | Admin only in Admin root; player nav absent; denial no case data | Cross-render | Mutual exclusion | SPECIFIED | D-042 |
| `UAT-P-003` | Object peek filters fields by class | Permission | P0 | Objects with field classes | All object links | — | `REQ-996` | ACC | `UIX-07` | Peek each object as each class | Only visible fields; denied state | Hidden field leaked | No leak | SPECIFIED | TR-021/022 |
| `UAT-P-004` | Restriction explanations use reason classes only | Permission | P0 | Restricted case | `SCR-048/055/058/084/086` | `FLOW-027` | `REQ-1029/1143` | FP | `UIX-26` | Inspect each restriction surface | Kind/scope/end/appeal; no accusation/threshold | Method/data leaked | Class-only text | SPECIFIED | NET-023 |
| `UAT-P-005` | Opponent strength is band-only | Permission | P0 | Active campaign | `SCR-061/063` | — | `REQ-1034/1074` | WAR | `UIX-23` | Inspect war surfaces as owner/non-owner | Four bands only; band meaning once | Exact ratio/statistic | Band-only | SPECIFIED | WAR-086 |
| `UAT-P-006` | Battle report field filtering | Permission | P0 | Battle record | `SCR-064/065` | — | `REQ-1035/1075` | WAR | `UIX-23` | Inspect as participant/third party | Participant fields vs public summary | Exact value public | Filter exact | SPECIFIED | WAR-088 |
| `UAT-P-007` | War board is nation-owner-only; alliance has no command path | Permission | P0 | `AN` owner; alliance officer | `SCR-058/061` | `FLOW-021` | `REQ-1039/1073` | WAR/ALL | `UIX-21` | Open as owner; open as officer; inspect links | Owner controls only; no alliance link/command | Any alliance control | No path | SPECIFIED | AX-18 |
| `UAT-P-008` | Render never grants permission; forged control fails closed | Permission | P0 | `AN2` attempting owner action | `SCR-061/090` | — | `REQ-1088` | All | All writes | Invoke a control not permitted by server | Server refuses with named restriction; no state change | State change | Fail closed | SPECIFIED | `13A-PR-11` |
| `UAT-P-009` | Destructive actions require exact phrase and separation | Permission | P0 | `AN`; reroll/closure/sanction | `SCR-090/094` | `FLOW-031/032` | `REQ-1156` | ACC/ADMIN | `UIX-03/28` | Attempt destructive with wrong phrase/adjacent tap | Refused; separated controls; phrase not remembered | Bypass | Refused | SPECIFIED | RRL-006 |
| `UAT-P-010` | Alliance military authority prohibitions remain permanent | Permission | P0 | Alliance officer | `SCR-053`…`058` | — | `REQ-1073` | ALL | `UIX-18`…`20` | Search every alliance surface for military actions | None exists; only permitted public links | Any command/OP path | Zero paths | SPECIFIED | AX-18 |
| `UAT-P-011` | SEC class and credentials never render | Permission | P0 | Admin and player sessions | `SCR-079/085/096` | — | `REQ-1076/1077` | FP | `UIX-26/29` | Inspect privacy/admin surfaces for SEC/tokens | None rendered; only labels/classes | Secret/token visible | Zero exposure | SPECIFIED | PRV-014 |
| `UAT-P-012` | Permission consistency across screens | Permission | P0 | Same action on two screens | `SCR-019/048/084` | — | `REQ-1197` | FP | `UIX-26` | Attempt same action from two surfaces | Same class/reason/denial | Contradictory permission | Consistent | SPECIFIED | D-230 |

**Permission tally:** 12 tests, 12 SPECIFIED.

---

## 7. Category F — Player experience (`UAT-E-001`…`UAT-E-014`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-E-001` | Tutorial safety, skip, resume and no auto-action | Experience | P0 | New account | `SCR-008/009/078` | `FLOW-004` | `REQ-1172`…`1180` | ACC | `UIX-04` | Run, skip, interrupt, resume, replay | No gameplay action; resumable; completion once | Tutorial spends/acts | Zero auto-actions | SPECIFIED | 13C TUT |
| `UAT-E-002` | Loading keeps shell and never uses a full-page spinner | Experience | P0 | Slow network | All | — | `REQ-1137/1138` | SHELL | `UIX-07` | Throttle; navigate; open detail | Shell persists; skeleton; failure with retry | Blank page | Shell persists | SPECIFIED | 13C §3 |
| `UAT-E-003` | Number types, forecast weight and as-of labels | Experience | P0 | Data screens | `SCR-015/029` | — | `REQ-980/1062`…`1064` | ECON | `UIX-08` | Inspect every figure | Six types labelled; forecast lighter; as-of everywhere | Unlabelled/merged | 100% labels | SPECIFIED | ECN-177 |
| `UAT-E-004` | Empty states distinguish their causes | Experience | P1 | New nation; filtered lists; no alerts | Lists/dashboards | — | `REQ-1139` | All | `UIX-07` | Open each empty surface | Cause + next step + honest absence | Fake zero/disabled control | 8 kinds correct | SPECIFIED | 13C §4 |
| `UAT-E-005` | Political and warning banners state cause and end | Experience | P0 | CRISIS; warning condition | `SCR-021/028` | — | `REQ-985/986` | POL | `UIX-14` | Trigger states; inspect banners | Cause, end/review, actions, locked/not locked | State as penalty | Content complete | SPECIFIED | DMP-268 |
| `UAT-E-006` | Validation and disabled reasons appear before the click | Experience | P0 | Invalid inputs; blocked controls | Forms | — | `REQ-1142/1145` | All | All writes | Submit invalid; hover/focus disabled | Field-linked errors; reason + rule + next condition | Error only after click | Reasons visible | SPECIFIED | 13A-PR-10 |
| `UAT-E-007` | Confirmation content, focus and no preselection | Experience | P0 | Any committing action | All committing | — | `REQ-1155` | All | All writes | Open confirmation; inspect focus/content/Escape | Cancel-first focus; exact effect/cost/turn; Escape cancels | Confirm preselected | All rules hold | SPECIFIED | D-214 |
| `UAT-E-008` | Notification tiers, grouping and non-opt-out preservation | Experience | P1 | Security notice; boundary result; cosmetic | `SCR-019` | `FLOW-027` | `REQ-1182`…`1187` | TURN | `UIX-06` | Inspect three tiers; mute permitted; attempt non-opt-out mute | Correct grouping; non-opt-out locked; no event mutation | Non-opt-out dropped | Tier behaviour correct | SPECIFIED | D-227 |
| `UAT-E-009` | Help, support and report remain separate | Experience | P1 | Footer access | `SCR-078/081/087` | — | `REQ-956/979` | FP | `UIX-26` | Open each entry; submit support | Separate routes; no silent conversion | Support becomes case | Separation holds | SPECIFIED | MOD-002 |
| `UAT-E-010` | Partial, suppressed and historical states are named | Experience | P0 | k=5 data; retained record | `SCR-040/072/077` | — | `REQ-988/1140/1152` | WORLD | `UIX-24` | Inspect partial/suppressed/retained | Named states; unaffected sections usable; retention label | Zero/blank in place | Named states | SPECIFIED | D-027 |
| `UAT-E-011` | Search, filters, pagination and saved views agree | Experience | P1 | Large lists | List screens | — | `REQ-991`…`994/1199` | All | `UIX-07` | Filter/search/page/save | Exact counts; preserved state; no visibility widening | Silent exclusion | Exact counts | SPECIFIED | MKT-065 |
| `UAT-E-012` | Suppression is not zero or an omitted card | Experience | P0 | Aggregate below threshold | `SCR-040/072/077` | — | `REQ-1056/1066` | WORLD | `UIX-P02` | Inspect below-threshold aggregate | Suppressed/insufficient state visible on every device | Zero/blank/absence | Named state | SPECIFIED | WEP-663 |
| `UAT-E-013` | Time is shown in turns and UTC, not wall-clock truth | Experience | P0 | All time-sensitive surfaces | All | — | `REQ-1007` | TURN | `UIX-05` | Inspect countdown/dates | Turn + UTC; wall clock cosmetic; no live urgency | Wall clock is truth | Turn/UTC exact | SPECIFIED | TR-024 |
| `UAT-E-014` | Cancelled state confirms nothing changed | Experience | P0 | Any task | Task screens | — | `REQ-1148` | All | `UIX-07` | Cancel each task/overlay | Nothing charged/reserved; safe return | Lingering charge | Zero change | SPECIFIED | 13C §6 |

**Experience tally:** 14 tests, 14 SPECIFIED.

---

## 8. Category G — Accessibility (`UAT-A-001`…`UAT-A-010`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-A-001` | Keyboard operability and reading order | Accessibility | P0 | Any authenticated surface | All | — | `REQ-1081/1162` | All | All | Tab through primary tasks without pointer | Reading order; skip link; no trap outside modal | Pointer-only function | Full task keyboard-complete | SPECIFIED | AXI-01–05 |
| `UAT-A-002` | Focus visibility, title and heading on transition | Accessibility | P0 | Navigation between screens | All | — | `REQ-1082/1164` | All | All | Navigate; inspect focus/title | Visible tokenized focus; title updated; focus on heading | Focus lost/unchanged | Focus+title correct | SPECIFIED | AXI-11–14 |
| `UAT-A-003` | Table semantics and card fallback | Accessibility | P0 | Table screens; mobile width | `SCR-014/019/040/072` | — | `REQ-990/1083/1167` | All | `UIX-07` | Inspect desktop table and mobile cards | Header/scope semantics; card preserves labels/order | Lost label/order | Semantics preserved | SPECIFIED | 13A-DS-12 |
| `UAT-A-004` | Drawers and accordions have page equivalents | Accessibility | P1 | Detail sections | `SCR-023/078` | — | `REQ-997` | All | `UIX-07` | Open every drawer; reach content without interaction | Page-reachable equivalent exists | Content only in drawer | Equivalent exists | SPECIFIED | D-215 |
| `UAT-A-005` | Form labels, errors and disabled reasons | Accessibility | P0 | All forms | Forms | — | `REQ-1086/1016` | All | All writes | Inspect labels; submit invalid | Programmatic labels; text-linked errors; reasons | Placeholder-only label | All labelled | SPECIFIED | 13A-DS-11 |
| `UAT-A-006` | Error summary focus and announcement | Accessibility | P0 | Invalid submission | Forms | — | `REQ-1165/1142` | All | All writes | Submit invalid; observe focus/live region | Summary or first invalid field focused; announced once | Silent error | Focus+announcement | SPECIFIED | AXI-06–10 |
| `UAT-A-007` | Overlay focus trap, cancel-first and restore | Accessibility | P0 | All overlays | All overlays | — | `REQ-1163` | All | All writes | Open/close each overlay by keyboard | Trap inside; cancel first; focus restored | Focus escape/restore failure | Trap/restore correct | SPECIFIED | D-215 |
| `UAT-A-008` | Reduced motion and non-motion-only states | Accessibility | P1 | OS reduced motion | Animated surfaces | — | `REQ-1085/1170` | All | All | Enable reduced motion; trigger states | Motion non-essential; text/glyph conveys state | Motion-only state | Non-essential motion | SPECIFIED | 13A-DS-13 |
| `UAT-A-009` | State announcements are single and polite | Accessibility | P0 | Loading/success/failure/suppression | All | — | `REQ-1149/1166/1187` | All | All | Trigger each state; monitor announcements | Announced once at correct politeness; counts not repeated | Announcement storm | Single announcements | SPECIFIED | AXI-06–10 |
| `UAT-A-010` | Chart alternatives, no dual axis, no conformance claim | Accessibility | P1 | Chart surfaces | `SCR-029/072/074` | — | `REQ-1058`…`1060/1087` | WORLD/ECON | `UIX-24` | Inspect charts and alternatives | Text/table alternative reachable; no dual axis; no WCAG claim in UI | Dual axis; image-only data | Alternatives present | SPECIFIED | 13A-DS-12 |

**Accessibility tally:** 10 tests, 10 SPECIFIED. No WCAG conformance is claimed by any row (`REQ-1171`).

---

## 9. Category H — Responsive (`UAT-R-001`…`UAT-R-008`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-R-001` | Same data, actions and rules on every device | Responsive | P0 | Desktop/tablet/mobile | All | — | `REQ-1051/1202` | All | All | Compare three devices for each section root | Identical data/actions/visibility/cadence | Device-specific mechanic | Identical | SPECIFIED | D-202 |
| `UAT-R-002` | Must-not-simplify list survives every layout | Responsive | P0 | Three devices | All | — | `REQ-1052` | All | All | Inspect countdown, pending, banner, protection, suppression, confirmation, reasons, appeal | Every item present | Any item removed | All 9+ present | SPECIFIED | 13A-RD-07 |
| `UAT-R-003` | Table-to-card preserves triples and units | Responsive | P0 | Mobile; financial table | `SCR-029/033/057` | — | `REQ-1053` | ECON | `UIX-08/10` | Convert table to cards | Triple, units, as-of preserved | Lost triple/unit | Preserved | SPECIFIED | MKT-053 |
| `UAT-R-004` | Navigation adapts with one-step section access | Responsive | P1 | Three devices | All | — | `REQ-1054` | All | `UIX-07` | Navigate to every section | One-step access; no hidden destination | Multi-step-only access | One-step | SPECIFIED | D-211 |
| `UAT-R-005` | Touch targets and destructive separation on mobile | Responsive | P0 | Mobile | Task screens | — | `REQ-1055/1169` | All | All writes | Inspect targets; attempt adjacent mis-tap | ≥24×24 CSS px; destructive separated; confirmation not skipped | Adjacent mis-tap commits | Targets+separation | SPECIFIED | 13A-DS-14 |
| `UAT-R-006` | Provisional breakpoints are labelled, not approved | Responsive | P1 | Design review | All | — | `REQ-1057` | All | — | Inspect design notes | Breakpoints labelled Category C/provisional | Claimed final | Labelled | SPECIFIED | D-232 |
| `UAT-R-007` | 320 px and 200% text/zoom reflow | Responsive | P0 | 320 px; 200% zoom | All | — | `REQ-1168` | All | All | Resize/zoom; inspect | No content loss; no horizontal page scroll | Clipping/scroll | Reflow clean | SPECIFIED | 13A-RD-05 |
| `UAT-R-008` | Complex dashboards and war/finance layouts survive mobile | Responsive | P1 | Mobile | `SCR-015/021/029/059/061` | — | `REQ-1053/1054` | All | All | Open each complex screen | Hierarchy, actions and warnings preserved | Meaning removed | All preserved | SPECIFIED | D-211 |

**Responsive tally:** 8 tests, 8 SPECIFIED.

---

## 10. Category I — Recovery and reliability (`UAT-C-001`…`UAT-C-010`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-C-001` | Single-flight double submission | Recovery | P0 | Any committing action | All committing | — | `REQ-1157` | All | All writes | Double-click/hold Enter | One intent; control in-flight; no second submit | Duplicate created | One submission | SPECIFIED | DUP-01/02 |
| `UAT-C-002` | Timeout shows uncertain, never success | Recovery | P0 | Simulated timeout | All committing | `FLOW-033` | `REQ-1158` | All | All writes | Submit; drop response | `ST-17`; no success; reconcile before retry | False success | Uncertain shown | SPECIFIED | DUP-05 |
| `UAT-C-003` | Refresh during commit re-reads without resubmit | Recovery | P0 | Submit; refresh | All committing | `FLOW-033` | `REQ-1191` | All | All writes | Refresh mid-flight | Object state re-read; no auto-resubmit | Duplicate | No resubmit | SPECIFIED | DUP-03 |
| `UAT-C-004` | Failure anatomy is complete | Recovery | P0 | Each failure family | All | — | `REQ-1160` | All | All | Trigger `ERR-01`…`ERR-20` | Happened/changed/completed/retry/next/support | Missing element | All six elements | SPECIFIED | 13C §11 |
| `UAT-C-005` | Named failure treatments are distinct | Recovery | P0 | Auth, authz, conflict, stale, rule, rate | All | — | `REQ-1161` | All | All | Trigger each | Distinct state/message; no generic error | Generic collapse | Distinct | SPECIFIED | ERR catalogue |
| `UAT-C-006` | Offline mode is read-only | Recovery | P0 | Network off | All authenticated | `FLOW-033` | `REQ-1188` | All | `UIX-05` | Disconnect; attempt every write | Writes disabled; no queue; reads last confirmed | Offline write accepted | Read-only | SPECIFIED | OFF-01 |
| `UAT-C-007` | Offline data carries as-of | Recovery | P0 | Disconnect after load | All data | — | `REQ-1189` | All | `UIX-07` | Inspect figures offline | As-of label on all | Presented current | As-of shown | SPECIFIED | OFF |
| `UAT-C-008` | Reconnection refreshes and surfaces conflict | Recovery | P0 | Reconnect after stale | Shell, owning | `FLOW-033` | `REQ-1192` | TURN | `UIX-05/06` | Reconnect; inspect values/conflict | New as-of; conflict before resubmit | Stale submitted | Refresh+conflict | SPECIFIED | OFF-04 |
| `UAT-C-009` | Session expiry preserves destination | Recovery | P0 | Expire mid-task | `SCR-003/080` | `FLOW-002` | `REQ-1190` | ACC | `UIX-01` | Expire; re-auth | Return to intended screen; safe input handling | Lost destination/secret | Destination preserved | SPECIFIED | ACC-031 |
| `UAT-C-010` | No automatic retry; delay not lost turn | Recovery | P0 | Boundary `INTERRUPTED` | `SCR-016/097` | `FLOW-033` | `REQ-1193` | TURN | `UIX-05` | Trigger interrupted boundary | No auto commit retry; delay named; pending remains | Lost turn/auto retry | Delay only | SPECIFIED | TR-080 |

**Recovery tally:** 10 tests, 10 SPECIFIED.

---

## 11. Category J — Player protection (`UAT-J-001`…`UAT-J-008`)

| Test ID | Test name | Category | Priority | Preconditions | Screens | Flow | Requirement | System | Contract | Steps | Expected result | Failure expectation | Acceptance condition | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UAT-J-001` | Appeal route always reachable | Player protection | P0 | Restricted/suspended/limited account | `SCR-083/084` | `FLOW-029` | `REQ-1078/1131` | FP | `UIX-26` | Attempt appeal under every restriction | Route reachable; status/reasons shown | Appeal blocked | Reachable in all states | SPECIFIED | MOD-013 |
| `UAT-J-002` | Report intake exact and evidence separate | Player protection | P0 | Intake available | `SCR-081` | `FLOW-028` | `REQ-1079/1130` | FP | `UIX-26` | Submit with/without evidence | Exact MOD-002 fields; separate evidence; case ref | Extra mandatory field | Fields exact | SPECIFIED | MOD-002 |
| `UAT-J-003` | Decision notice elements and claim tiers | Player protection | P0 | Decided case | `SCR-082` | — | `REQ-951` | FP | `UIX-26` | Open decision | Seven elements; EVD-009 tiers; no method/threshold | Missing element/tier upgrade | Complete | SPECIFIED | MOD-017 |
| `UAT-J-004` | Audit access is scoped and tamper-evidence verified | Player protection | P0 | `R-AUD`; audit data | `SCR-096` | — | `REQ-965/1080` | ADMIN | `UIX-29` | Open audit; attempt out-of-scope; verify chain/job | Scoped access; every access audited; chain verified | Unverified chain claimed | **BLOCKED** until trigger/digest/job exist | `BLOCKED` | SEC-036–040 |
| `UAT-J-005` | Newcomer/return protection is visibility-only | Player protection | P0 | Protected nation | `SCR-089/063` | — | `REQ-958` | ACC/WAR | `UIX-26/23` | Inspect protection across surfaces | End turn shown; no bonus/countdown; blocks consistent | Bonus framing | Visibility-only | SPECIFIED | D-040 |
| `UAT-J-006` | Non-opt-out security and appeal notices persist | Player protection | P0 | Security notice | `SCR-019/084` | `FLOW-027` | `REQ-1186` | TURN/FP | `UIX-06/26` | Attempt mute; reload | Notice remains; cannot be silently dropped | Notice removed | Persist | SPECIFIED | DIP-114 |
| `UAT-J-007` | Sanctions two-person rule and separation | Player protection | P0 | Case needing top tier | `SCR-094` | `FLOW-032` | `REQ-963` | ADMIN | `UIX-28` | Single-reviewer attempt; second review | Blocked until second; duties separated; audit | Single approval | Two-person enforced | SPECIFIED | MOD-022 |
| `UAT-J-008` | Restriction text, redress and sensitive data | Player protection | P0 | Restricted case; subject data | `SCR-082`…`084/086` | — | `REQ-953/955` | FP | `UIX-26` | Inspect every protection surface | Kind/scope/end/appeal; no accusation/method/third-party data | Data/method leak | Text compliant | SPECIFIED | NET-050 |

**Protection tally:** 8 tests — 7 SPECIFIED, 1 BLOCKED (`UAT-J-004`, audit tamper-evidence dependency).

---

## 12. Bidirectional traceability

### 12.1 Requirement → test

| Requirement block | Requirement → test rule | Coverage |
|---|---|---|
| `REQ-870`…`REQ-969` | `REQ-(869+n)` → `UAT-SCR-n` | 100/100 |
| `REQ-970`…`REQ-1089` | Row-level mapping in D1 §15.2 → primary test named per row | 120/120 |
| `REQ-1090`…`REQ-1203` | Row-level mapping in D1 §15.3 → primary test named per group/row | 114/114 |
| `REQ-1204` frontier | No row allocated | N/A |

### 12.2 Test → requirement/system/screen

Every scenario row above names its requirement(s), system(s), screen(s), flow and contract. The reverse index is the table itself; no test exists without a legitimate requirement or a documented rationale (the four absence tests in `UAT-I-016` cite `REQ-889/907/908/937/946` and contract absence clauses).

### 12.3 Orphan analysis

| Population | Count | Orphans | Disposition |
|---|---|---|---|
| Screens | 100 | 0 | Every screen has `UAT-SCR-n` |
| Components | 90 | 0 | Every component mapped to at least one test in D1 §13 |
| Overlays | 8 | 0 | Every overlay mapped to at least one test in D1 §13 |
| Journeys | 13 | 0 | Every journey has a completion test (`UAT-F-001`…`025`) |
| Flows | 33 | 0 | Every flow has a functional test |
| Requirements (Prompt 13) | 334 | 0 | All dispositioned; none upgraded |
| Contracts | 34 | 0 | Every contract has a `UAT-I` test |
| Tests without requirement | 0 | 0 | Every test cites a requirement or absence clause |

### 12.4 Coverage summary

| Dimension | Covered | Total | Percentage |
|---|---|---|---|
| Screens | 100 | 100 | 100% |
| Journeys | 13 | 13 | 100% |
| Flows | 33 | 33 | 100% |
| Components/overlays | 98 | 98 | 100% |
| Contracts | 34 | 34 | 100% |
| Requirements (13A/13B/13C) | 334 | 334 | 100% |

**Coverage is planned, not proven.** No test has run. Aggregate requirement coverage across the Prompt 13 blocks is **334/334** (100 screen + 120 cross-cutting + 114 interaction requirements dispositioned).

---

## 13. Execution-status register

| Status | Count | Notes |
|---|---|---|
| SPECIFIED | 215 | Designed scenarios; no implementation exists |
| BLOCKED | 1 | `UAT-J-004` — tamper-evident audit chain, trigger and verification job absent |
| IMPLEMENTED | 0 | No test code exists |
| EXECUTED | 0 | No test has run |
| PASSED | 0 | None |
| FAILED | 0 | None |
| **Total** | **216** | 100 screen + 116 scenario |

**Breakdown of the 116 scenario tests:** F 26 + I 16 + X 12 + P 12 + E 14 + A 10 + R 8 + C 10 + J 8 = 116.

### 13.1 Tests that cannot be executed without a built application

All 216. A specification-level test cannot be executed against documentation. The distinction is recorded so no reader mistakes this catalogue for evidence that the interface works.

### 13.2 Tests with a production-security dependency beyond the built UI

`UAT-J-004` additionally requires the audit trigger, digest chain and scheduled verification job (currently absent). `UAT-I-015` can test the UI's role-scoped read behaviour, but cannot certify tamper-evidence. No test in this catalogue can be satisfied by a documentation validator.

---

## 14. Acceptance evidence references

| Evidence | Location |
|---|---|
| Screen bodies (A–K) | `21_screen_specifications.md` §1–§10 |
| Component bodies and states | `21_component_specifications.md` §1–§9 |
| Journeys/flows/tutorials | `22_player_journey_specifications.md` §2–§5 |
| States/validation/errors/offline | `22_interaction_states_and_feedback.md` §1–§15 |
| Contracts | `23_ui_integration_contracts.md` §5 |
| Screen/system/contract/test mapping | `23_ui_system_integration_and_traceability.md` §8–§15 |
| Gates and overall verdict | `23_prompt_13_final_reconciliation_and_acceptance.md` |

---

*End of B-13D acceptance-test catalogue.*
