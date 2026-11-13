# B-13D — UI system integration and traceability

**Version:** 1.0 · **Created:** 2026-11-13 · **Stage 2, Prompt 13D** · **Status:** specification and integration analysis only.
**Authority:** Prompt 13D instruction, executed 2026-11-13. Owning documents remain the B-02…B-12 rulebooks, the B-13 screen/component family, the B-13C interaction family and the fair-play family. This document owns the **integration mapping, navigation audit, integration traceability and gap ledger**; it owns no game rule, no formula, no screen content and no implementation.
**Companions:** [`23_ui_integration_contracts.md`](23_ui_integration_contracts.md) · [`23_ui_acceptance_test_catalog.md`](23_ui_acceptance_test_catalog.md) · [`23_prompt_13_final_reconciliation_and_acceptance.md`](23_prompt_13_final_reconciliation_and_acceptance.md).
**Governing policy:** [`AUTONOMOUS_DECISION_POLICY.md`](../AUTONOMOUS_DECISION_POLICY.md) (D-014).

**Status boundary.** This is a documentation deliverable. It implements no screen, component, route, state store, API, database object, migration, gameplay rule or deployment. Every `UAT-` test here is **SPECIFIED — designed, not implemented, not executed**. No WCAG conformance is claimed. No owner-reserved decision is resolved.

---

## 1. Scope, inputs and boundaries

### 1.1 What this document does

1. Establishes the source-authority matrix for the Prompt 13 integration exercise (§3).
2. Records the Stage 1 and Stage 2 cross-system consistency findings and their resolutions (§4–§7).
3. Maps every one of the 100 screens to its systems, rules, requirements, flows, contracts, tests, read/write posture and limitations (Matrix A, §8).
4. Maps every relevant game-system capability back to a UI representation (Matrix B, §9).
5. Verifies navigation reachability (Matrix L, §10).
6. Maps the 13 journeys, 33 flows and 98 components/overlays (§11–§13).
7. Reconciles the 18 interaction states with screens, components and systems (§14).
8. Gives every Prompt 13 requirement an explicit traceability disposition (Matrix C) and every UI capability a requirement/decision source (Matrix D) (§15).
9. Records cross-stage consistency (Matrix J, §16).
10. Records every discovered gap with severity, classification, disposition and acceptance condition (§17).

### 1.2 What this document does not do

- It does not re-specify screens (owned by `21_screen_specifications.md`), component bodies (`21_component_specifications.md`), journeys/flows (`22_player_journey_specifications.md`) or states (`22_interaction_states_and_feedback.md`).
- It does not define an endpoint, table, queue, job or runtime service. Where an implementation detail is undefined, the abstraction boundary is named and classified as a Stage 5/6 obligation.
- It does not change a rule, requirement status, gate verdict, provisional value or owner-reserved decision.
- It does not claim that any test was executed against a built interface.

### 1.3 Field-ownership rule

The 24 screen fields required by the Prompt 13D instruction are satisfied in two layers:

- **A–K content** (purpose, hierarchy, layout, data presentation, controls, validation, errors, notifications, responsive and restrictions) is owned by the screen body in `21_screen_specifications.md` §1–§10. Matrix A cites the body rather than duplicating it; every screen body carries all eleven fields.
- **Integration fields** (systems, rules/formulas, requirement, flows, contract, test, read/write posture, limitation) are owned by this document and shown in Matrix A. Where a field is genuinely not applicable, the cell says why (`none — public read only`, `none — no rule exists`, `BLK-…`, `PROV-…`).

---

## 2. Method and status vocabulary

### 2.1 Authority levels used in §3

| Level | Meaning |
|---|---|
| **A — Fixed constraint** | Owner-only; may not be overridden (D-014, AI_CONTEXT §2) |
| **B — Confirmed/approved design** | Binding design position recorded in DECISIONS.md or the owning rulebook |
| **C — Provisional** | Safe working default with a named missing evidence or owner decision |
| **D — Research input** | Evidence and recommendations; never an approved product rule (D-003) |
| **E — Historical** | Dated snapshot; read as history, never as current instruction |
| **F — QA evidence** | Validator/test output; documentation quality only |

### 2.2 Integration status vocabulary

| Status | Meaning in this document |
|---|---|
| `INTEGRATED` | Screen, system, requirement, contract and test are all identified; no unresolved dependency beyond global obligations |
| `INTEGRATED-PROVISIONAL` | Integrated, but a named provisional value/question can change presentation |
| `INTEGRATED-BLOCKED` | Integrated as an **absence**: the screen/feature must not be available until a gate passes |
| `GAP` | A mapping, flow, contract or test is missing and is registered in §17 |
| `N/A` | The field does not apply; the reason is written in the cell |

### 2.3 Test status vocabulary

`SPECIFIED` · `IMPLEMENTED` · `EXECUTED` · `PASSED` · `FAILED` · `BLOCKED`. Only `SPECIFIED` and `BLOCKED` occur in Prompt 13D. A specification is not a pass.

---

## 3. Source-authority matrix

| # | Source | Section/identifier | Governs | Authority | Current status | UI surfaces | Integration implication | Unresolved conflict |
|---|---|---|---|---|---|---|---|---|
| 1 | `AI_CONTEXT.md` | §2, STATUS block | Fixed constraints, current position | A/B | Confirmed | All | Cadence, mapless world, browser, account and architecture bind every screen | None |
| 2 | `AUTONOMOUS_DECISION_POLICY.md` | D-014 | Decision procedure | A/B | Confirmed | — | Every 13D disposition is Category B unless owner/evidence-reserved | None |
| 3 | `DECISIONS.md` | D-001…D-233 | Project decisions | B | Confirmed/superseded per row | All | D-015 OP, D-016/D-017 trade, D-030 diplomacy, D-039 reroll, D-042 admin, D-122 Global Trade, D-233 acceptance | D-233 acceptance scope clarified in §7 |
| 4 | Stage 1 Reports 01–13 | As cited per screen | Research and identity evidence | D/E | Inputs-only (D-003) | Cross-cutting | Informs but never overrides a B-rule | None |
| 5 | B-02 core loop | `07_core_gameplay_loop_symbolic_world_and_turn_system.md` | Turn, phases, digest, notifications | B/C | Approved model; values provisional | All authenticated | Two-hour UTC cadence is the only cadence any screen may show | None |
| 6 | B-03 accounts | `09_account_onboarding_nation_creation_and_progression.md` | Identity, registration, nation, protection, reroll | B/B-C | Confirmed design; numbers provisional | `SCR-001`…`SCR-012`, `SCR-080`, `SCR-089`, `SCR-090` | UI availability never grants account permission | None |
| 7 | B-04 economy | `10_economy_resources_treasury_and_finances.md` + formula register | Treasury, production, resources, reports | B/C | Confirmed design; values provisional | `SCR-029`…`SCR-034`, `SCR-044` | Six number types; total/reserved/available; no invented formula | None |
| 8 | B-05 cities | `11_cities_infrastructure_production_and_research.md` + formula register | Cities, construction, research | B/C | Confirmed design; values provisional | `SCR-041`…`SCR-046` | One city slot; one research project; DC capacity semantics | None |
| 9 | B-06 politics | `12_population_and_domestic_politics.md` + formula register | Population, approval, stability, elections, crisis | B/C | Confirmed design; values provisional | `SCR-021`…`SCR-028`, `SCR-015` | Six-state banner; election anchors; no government-change control | None |
| 10 | B-07 markets | `13_trade_and_markets.md` + formula register; `14_market_workflows_and_acceptance.md` | Directed trades, Global Trade gate | B/C | Directed specified; Global Trade blocked | `SCR-035`…`SCR-040` | Directed lifecycle only; Global Trade absent until G-1…G-6 | Global Trade gate correctly blocks `SCR-038/039` |
| 11 | B-08 diplomacy | `15_diplomacy.md` + formula register; `15_diplomacy_workflows_acceptance.md` | Posture, agreements, embargo, publication | B/C | Confirmed design; values provisional | `SCR-047`…`SCR-052` | Directional posture; parties-only pending; no delegation | None |
| 12 | B-09 alliances | `16_alliances.md` + formula register + `16_alliances_integration_contracts.md`; `16_alliances_workflows_acceptance.md` | Membership, roles, tax, ARL, treaties | B/C | Accepted at specification level; owner-reserved rows Open | `SCR-053`…`SCR-058` | No military command; 0% fallback while UD-040 open; no spendable ARL purpose | UD-040/044–049 remain Open |
| 13 | B-10 warfare | `17_warfare_and_settlements.md` + formula register; `17_warfare_workflows_acceptance.md` | Operations, campaigns, settlements | B/C | Confirmed design; values provisional | `SCR-059`…`SCR-068` | Nation-owner-only; four readiness bands; surrender off-ramp; no espionage | None |
| 14 | B-11 world | `18_world_events_objectives_rankings_progression.md` + formula register; `19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md` | Events, objectives, standings, rewards | B/C | Confirmed design; values provisional; 17 WPC contracts | `SCR-069`…`SCR-078`, `SCR-018` | Denominator/window; no composite headline; k=5 suppression | None |
| 15 | B-12 fair play | `20_fair_play_and_player_protection.md` + formula register + requirements + acceptance; 12C workflows/integration/edge cases | Privacy, reports, moderation, sanctions, audit | B/C | 23 PASS / 3 PARTIAL; owner accepted 12C | `SCR-079`…`SCR-087`, `SCR-091`…`SCR-100` | Nine privacy classes; appeal always reachable; two-person rule; audit obligations outstanding | Production security obligations outstanding |
| 16 | 13A research | `research/13A_*.md` (five files) | Benchmark, principles, inventory, responsive/design system, requirements | D (principles adopted B) | Owner accepted | All | 16 principles, eight sections, 100-screen inventory, 13 state names | None |
| 17 | B-13 screens/components | `21_interface_and_player_journeys.md`, `21_screen_specifications.md`, `21_component_specifications.md` | Screen and component content | B | Owner accepted (D-233) | All | A–K template, navigation register, `UI-CMP-001`…`090`, `OVL-01`…`08` | None |
| 18 | B-13C interaction | `22_interaction_flows_and_player_experience.md`, `22_player_journey_specifications.md`, `22_interaction_states_and_feedback.md` | Journeys, flows, tutorials, states, feedback | B | Owner accepted (D-233) | All | 13 JRN, 33 FLOW, 12 TUT, 18 ST, validation/duplicate/error/offline rules | None |
| 19 | Workflow companions | 07C, 08C, 09C, 10C, 11C, 12C | Operational rules and acceptance | B/C | Complete at specification level | System screens | Supply validation, failure and acceptance references | None |
| 20 | Requirements register | `03_requirements_traceability.md` | `REQ-001`…`REQ-869` | B/C | REQ-869 frontier; later blocks pointed to owners | All | `REQ-870`…`REQ-1203` are owned by the B-13/B-13C registers | None |
| 21 | Decision register | `04_approved_and_provisional_decisions.md` | `DD-001`…`DD-281` | B/C | Mirrors D-rows | All | Every new 13D decision must be mirrored | §6 tallies were stale; corrected in 13D (§7) |
| 22 | Unresolved register | `05_unresolved_design_decisions.md` | `UD-001`…`UD-060` | C/A | 28 Resolved / 3 Deferred / 29 Open | Alliance, privacy, enforcement | No UI design may resolve one | None |
| 23 | Progress log | `06_stage_2_progress_log.md` §§1–93 | Chronology | E | Historical through §93 | — | New records append; old entries not rewritten | Prompt 13D status appended (§94) |
| 24 | Prompt archive | `docs/prompts/` + INDEX | Verbatim instructions | E | Preserved | — | Provenance for this pass | None |
| 25 | QA validators | `docs/qa_backups/*.py` | Structural/document checks | F | See §2.4 and Deliverable 4 | — | Evidence of documentation quality only | 10B stale constant corrected (§7) |

### 2.4 Baseline verification performed before integration

| Check | Result |
|---|---|
| Working tree at start | Clean; no tracked or untracked modifications; one pre-existing unrelated stash on `review/12A` preserved |
| Branch | `main` at `07027fb` |
| 13A validator | 34/34 checks |
| 13B validator | 28/28 checks |
| 13C validator | 27/27 checks |
| 12A validator | 45/45 checks |
| 12C validator | 24/24 checks |
| 10B validator | **1036 checks, 1 failure** — stale `CURRENT_SUBPROMPT` expectation (pre-existing; see §7 CONF-13D-02) |
| Documentation links | 4,185 found; 3,803 local; 382 external; 33 anchors; 0 unresolved |
| `validate_final.py` | ALL CHECKS PASSED (pre-13D frontier) |
| `test_next_action.py` | 27 tests OK (pre-13D frontier) |
| `test_decision_registers.py` | 12 tests OK |

---

## 4. Stage 1 cross-system consistency audit

Stage 1 is **CLOSED** (D-011). Its conclusions bind the UI as product identity and constraints, not as screen designs.

| # | Stage 1 source | Finding that binds the UI | UI evidence | Consistency |
|---|---|---|---|---|
| S1-01 | Report 05 identity; D-007 | Original name **Nation Supremacy**, browser game, fictional mapless world | `SCR-001`, `SCR-018`, `SCR-088`; no map component anywhere | Consistent |
| S1-02 | AI_CONTEXT §2; D-012 | Two-hour UTC cadence, 12 turns/day, server-resolved | `SCR-013`, `SCR-016`, `SCR-097`, `REQ-975` | Consistent; no screen implies another cadence |
| S1-03 | Report 08; D-032/D-034 | One account per person; pair restrictions; shared-network review | `SCR-002`, `SCR-086`, `SCR-095` | Consistent |
| S1-04 | Report 07; B-04 | Treasury conservation and six number types | `SCR-029`…`SCR-034`; `REQ-1062`/`REQ-1063` | Consistent |
| S1-05 | Report 07; B-07/D-122 | Global Trade is product scope but release-gated | `SCR-038/039` absent; `SCR-040` pre-gate minimal | Consistent |
| S1-06 | Report 08; B-12 | Fair-play, privacy, appeals and audit | `SCR-079`…`SCR-087`, admin family | Consistent at specification level; production obligations outstanding |
| S1-07 | Report 09 GATE-13/16/18 | Free-first and capacity limits remain conditional/evidence-owned | No screen promises capacity or scale | Consistent; UI must not assert measured capacity |
| S1-08 | Report 10–12 prototypes | `feasibility` schema is not game code; client-writable treasury is a known defect | All write contracts are server-authoritative in intent | Consistent; `UIX-08`/`UIX-09` carry the dependency |
| S1-09 | Report 04 personas | Re-entry, absence tolerance, mobile expectations | Digest, Inbox, responsive duties | Consistent |
| S1-10 | Report 06 systems catalogue | Every system needs a visible consequence | Matrix B coverage; `13A-PR-15` | Consistent; gaps recorded in §17 |
| S1-11 | Report 03 feature comparison | No mandatory paid dependency; no client download | Shell, public entry, no install surface | Consistent |
| S1-12 | Report 02 frustrations | Knowledge spill-off, opacity, hidden state | In-context help, cause chains, suppression states | Consistent |
| S1-13 | Stage 1 closure | Stage 2 authorized; Stage 3+ not started | No implementation deliverable exists | Consistent |
| S1-14 | D-011/D-012 | Stage sequencing is fixed | Prompt 13D does not start Prompt 14 | Consistent |

**Conclusion.** No Stage 1 product identity, constraint or conclusion is contradicted by any Prompt 13 screen, component, flow or state. Two Stage 1-derived obligations remain visible as dependencies rather than resolved facts: free-tier capacity evidence (CF-01…CF-09) and the prototype's security posture.

---

## 5. Stage 2 cross-system consistency audit

| # | Stage 2 source | Binding fact | UI evidence | Consistency |
|---|---|---|---|---|
| S2-01 | B-02 | Turn phases P0–P7 and one global boundary | Turn indicator, pending model, admin monitor | Consistent |
| S2-02 | B-02 TR-004/TR-089 | Inbox is the single pending-action aggregation; digest is bounded | `SCR-014`, `SCR-013` | Consistent |
| S2-03 | B-03 D-029/D-038/D-040/D-041 | Verification gate; neutral naming; one-time protection; closure/recovery | `SCR-002`…`SCR-009`, `SCR-012`, `SCR-089`, `SCR-090` | Consistent |
| S2-04 | B-03 D-039 reroll | Immediate replacement, no renewed protection, exact-phrase confirmation | `SCR-090`, `FLOW-031` | Consistent |
| S2-05 | B-04 ECN-176/177/178 | Six number types; total/reserved/available; labelled forecast | `SCR-029`…`SCR-034`; `REQ-1062`…`REQ-1065` | Consistent |
| S2-06 | B-04 D-053/ECN-044/045 | Standing policy versus manual order; capacity and space reservation | `SCR-032`, `FLOW-009/010` | Consistent |
| S2-07 | B-05 URB-031/D-067 | Twelve cities on one screen; no pagination into separate screens | `SCR-041`; `REQ-910` | Consistent |
| S2-08 | B-05 URB-064/148/D-073/D-074 | One construction-class action per city per turn; 25% crown-only demolition refund | `SCR-043`, `FLOW-014` | Consistent |
| S2-09 | B-05 D-076/URB-093–097 | One active research project; RP pool separate from programme spend | `SCR-045`, `FLOW-016` | Consistent |
| S2-10 | B-06 DMP-268 | Six political states; banner on every political surface | `SCR-021`…`SCR-028`; `REQ-1010` | Consistent |
| S2-11 | B-06 D-087/D-106/D-107/D-094 | Policy cooldown 12 turns; election anchor; three campaign actions; charge once | `SCR-024`…`SCR-027`; `FLOW-007/008` | Consistent |
| S2-12 | B-06 DMP-163/205/229 | Crisis 18 turns stability-only; transition 12 turns; 800 bp penalty disclosure | `SCR-027`, `SCR-028` | Consistent |
| S2-13 | B-07 MKT-053/D-016/D-017 | Three balances; directed offers reserve nothing; atomic settlement; revisions | `SCR-035`…`SCR-037`; `FLOW-011`…`013` | Consistent |
| S2-14 | B-07 D-110/D-111/D-117/D-122; G-1…G-6 | Global Trade reserves at posting, taker-selected, no statistic pre-gate, release-gated | `SCR-038/039` blocked; `SCR-040` minimal; `UIX-B01` | Consistent |
| S2-15 | B-08 DIP-023/024/D-030/DIP-108–113 | Directional posture; parties-only pending; publication at activation; k=5 aggregates | `SCR-047`…`SCR-052`; `FLOW-017/018` | Consistent |
| S2-16 | B-08 D-030/no-delegation | Sole diplomatic authority is the nation owner; no delegation | No alliance or admin diplomatic submit control | Consistent |
| S2-17 | B-09 D-135/D-140/D-141/AT-E00/E01 | Player-authored constitution; separate alliance treaty object; record-only vs NAP effect; ARL four categories | `SCR-053`…`SCR-058`; `FLOW-019/020` | Consistent |
| S2-18 | B-09 AX-18/WAR-148/161 | No alliance military command, member OP spending, delegated operations or private war visibility | `SCR-058`, `SCR-061`; `REQ-1039/1073` | Consistent |
| S2-19 | B-09 UD-040/045/046 | 0% fallback while attribution open; only narrow tax management authorized; no spendable ARL purpose | `SCR-056`, `SCR-057`; `REQ-925/926/1027` | Consistent; owner-reserved |
| S2-20 | B-10 D-015/10B-C3/WAR-039 | One persistent national OP pool; +1 at P3.7; cap 10 provisional; carry below cap | `SCR-059`, `SCR-061`, `UIX-21` | Consistent |
| S2-21 | B-10 WAR-086/088/148/150 | Four readiness bands only; field visibility; nation-owner-only board | `SCR-061`…`SCR-065`; `REQ-1034/1074/1075` | Consistent |
| S2-22 | B-10 WAR-126/131/132/UD-032 | One live settlement; surrender guaranteed; reroll block retained | `SCR-067`, `FLOW-023/024` | Consistent |
| S2-23 | B-10 espionage exclusion | No intelligence rule exists | `SCR-068` provisional and not built; `UIX-B02` | Consistent |
| S2-24 | B-11 WEP-324/325/361/362 | Denominator and window; no live tick; no composite headline | `SCR-072`, `SCR-074`; `REQ-1045/1069/1070` | Consistent |
| S2-25 | B-11 WEP-179/619/WPC-14 | Cause paired with registered consequence; six required surfaces | `SCR-069`…`SCR-076`; `UIX-24` | Consistent |
| S2-26 | B-11 D-027/WEP-663 | k=5 suppression is a named state | `SCR-072`, `SCR-077`, `SCR-040`; `REQ-1056/1066` | Consistent |
| S2-27 | B-12 PRV-002/009/014 | Nine privacy classes; `SEC` never rendered | `SCR-079`, `SCR-085`, `SCR-096`; `REQ-1076/1077` | Consistent |
| S2-28 | B-12 MOD-002/013/017/022 | Exact report intake; appeal never blocked; seven notice elements; two-person rule | `SCR-081`…`SCR-084`, `SCR-094`; `FLOW-028/029/032` | Consistent |
| S2-29 | B-12 D-042/ADM-003 | Separate Admin root; least privilege; no superuser | `SCR-091`…`SCR-100`; `UIX-28/29` | Consistent |
| S2-30 | B-12 audit spine (SEC-036…040/EVD-030) | Tamper-evident chain and verification job **specified, not implemented** | `SCR-096`; `UIX-29`; `GAP-13D-06` | Consistent; blocked dependency |
| S2-31 | D-233 owner acceptance | 13B/13C accepted at specification level only | All status blocks preserve limitations | Consistent; §7 clarifies 13A wording |
| S2-32 | 13C REQ-1183/1185 | Notification tiers/grouping provisional | `SCR-019`; `UIX-06` | Consistent; provisional preserved |

**Conclusion.** All Prompt 13 screens are derivable from the B-system rules and no screen invents a mechanic. The only cross-system contradictions found were documentation/register artefacts, not game-design conflicts; they are logged and resolved in §7.

---

## 6. Requirement and decision integrity checks

| Check | Result |
|---|---|
| Screen requirement formula `REQ-(869+n)` for `SCR-001`…`SCR-100` | Verified; 100/100 rows resolve |
| B-13 requirement block | 220 rows: 213 SPECIFIED / 4 PROVISIONAL / 3 BLOCKED |
| B-13C requirement block | 114 rows: 112 SPECIFIED / 2 PROVISIONAL / 0 BLOCKED |
| Next free requirement | `REQ-1204`; **no new requirement was justified by 13D** |
| Decision frontier before 13D | D-233 / DD-281; 13D adds D-234…D-236 / DD-282…DD-284 |
| Owner-reserved register | 28 Resolved / 3 Deferred / 29 Open; unchanged by 13D |
| Duplicate screen/component/flow/journey identifiers | None found |
| Orphan screen references in 13D | None (validator-enforced) |

---

## 7. Conflict register and resolutions

| ID | Conflicting statements | Authoritative source | Resolution | Reopens? |
|---|---|---|---|---|
| `CONF-13D-01` | `04_approved_and_provisional_decisions.md` header records DD-281 / D-233, but its §6 tallies still say 267 DD rows, 219 D rows and maxima D-219/DD-267/REQ-1089 | DECISIONS.md D-233 + the register's own header | §6 tallies reconciled in 13D to the actual frontier; historical tally text kept as history | No |
| `CONF-13D-02` | `status_rules.py` sets `CURRENT_SUBPROMPT = "13D"` while `10B_validate_warfare.py` still expects `"13C"` | status_rules.py (current frontier) | 10B validator's single continuity expectation refreshed to the current frontier; no check logic weakened | No |
| `CONF-13D-03` | Some records say Prompt 13A owner acceptance "PENDING"; the Prompt 13B instruction and the 13D instruction record 13A as OWNER ACCEPTED | Owner instructions; D-233 for 13B/13C | Current status records 13A accepted; pending-era sentences are preserved as labelled history | No |
| `CONF-13D-04` | 13B uses "class" (Mandatory/Conditional/Provisional/Admin) while Matrix A uses "Status" (SPECIFIED/PROVISIONAL/BLOCKED) | 13B §4.3 | Two orthogonal axes; 13D never converts one into the other | No |
| `CONF-13D-05` | `SCR-020` is Conditional class yet PROVISIONAL status; a reader could call it "a Provisional screen" | 13B §4.3 and Matrix A | Clarified: class is product availability; status is specification/gate state | No |
| `CONF-13D-06` | 13C `JRN-J` includes `SCR-018` while 13B lists it under World; an older 13A line grouped it under Home | 13B §3.2 canonical parent (World) | 13C is consistent with 13B; 13A text is historical inventory language | No |
| `CONF-13D-07` | `04` §6 says "current maxima are REQ-1089, D-219, DD-267"; 13C added REQ-1203 and D-232/DD-280; D-233 added DD-281 | 13C registers + D-233 | Frontier reconciled in `04` and in every STATUS block during 13D | No |
| `CONF-13D-08` | `AI_CONTEXT` `ui_foundations` field began with "OWNER ACCEPTED 2026-11-13 (D-233)" although D-233 accepts 13B/13C and 13A was accepted in the 13B instruction | Owner instructions; D-233 | 13D rewrites the field to name both acceptance bases precisely | No |
| `CONF-13D-09` | Roadmap/status blocks say "Prompt 13D NOT STARTED / NOT AUTHORIZED" after this execution | This prompt's owner authorization | Status blocks reconciled to "13D complete at documentation level; owner acceptance PENDING; Prompt 14 NOT AUTHORIZED" | No |
| `CONF-13D-10` | 13B screen Matrix A tally "95 SPECIFIED" includes admin screens, while a reader might expect 85 player screens | 13B Matrix A | Clarified: 85 Mandatory player + 10 admin = 95 SPECIFIED; 2 PROVISIONAL + 3 BLOCKED | No |
| `CONF-13D-11` | 12C gate tally says 16 PASS / 2 PARTIAL / 2 BLOCKED; some summaries compress it to "owner accepted" | 12C acceptance companion | Both are true: owner accepted the phase; gates retain their verdicts | No |
| `CONF-13D-12` | The Prompt 13D instruction baseline table says 220 B-13 requirements and 114 new 13C requirements | 13B Matrix C / 13C §18.2 | Verified exact: 220 and 114 | No |

No underlying game-system conflict was found that required changing a rule. No accepted gameplay decision was rewritten to make the UI appear consistent.

---

## 8. Matrix A — Screen-to-System traceability

**Reading rule.** `System` codes: `ACC` account/identity, `TURN` core loop, `ECON` economy, `CITY` cities, `POL` politics, `MKT` markets, `DIP` diplomacy, `ALL` alliances, `WAR` warfare, `WORLD` world/progression, `FP` fair play, `ADMIN` administration, `SHELL` presentation shell. `R/W`: `R` read-only; `W` submits or modifies; `R/W` both; `none` absent by gate. Every row's A–K content is in the cited screen body (`21_screen_specifications.md`); every row's test is the matching `UAT-SCR-` case in Deliverable 3. Limitation codes are defined in §8.2.

| SCR | Name | Section | Class | Access | System | Secondary | Governing rules | REQ | Flows | UIX | Test | R/W | Limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCR-001` | Landing | Public | Mandatory | Public | SHELL | — | B-03; D-007; TR-022 | `REQ-870` | — | `UIX-01` | `UAT-SCR-001` | R | `BRAND` |
| `SCR-002` | Registration | Public | Mandatory | Public | ACC | — | B-03 ACC; D-029/D-032 | `REQ-871` | `FLOW-001` | `UIX-02` | `UAT-SCR-002` | W | — |
| `SCR-003` | Login | Public | Mandatory | Public | ACC | TURN | B-03 ACC-018; D-041 | `REQ-872` | `FLOW-002` | `UIX-01` | `UAT-SCR-003` | W | — |
| `SCR-004` | Password reset | Public | Mandatory | Public | ACC | — | B-03; D-041 | `REQ-873` | `FLOW-001` alt | `UIX-02` | `UAT-SCR-004` | W | — |
| `SCR-005` | Recovery code | Public | Mandatory | Public | ACC | — | B-03 ACC-031 | `REQ-874` | `FLOW-002` alt | `UIX-02` | `UAT-SCR-005` | W | — |
| `SCR-006` | E-mail verification | Public | Mandatory | Public | ACC | — | B-03; D-029; ACC-024 | `REQ-875` | `FLOW-001` | `UIX-02` | `UAT-SCR-006` | W | — |
| `SCR-007` | Nation creation | Public | Mandatory | Verified | ACC | ECON | NAT; D-038/D-063 | `REQ-876` | `FLOW-003` | `UIX-03` | `UAT-SCR-007` | W | — |
| `SCR-008` | Onboarding | Home | Mandatory | Auth | ACC | SHELL | ONB; D-040 | `REQ-877` | `FLOW-004` | `UIX-04` | `UAT-SCR-008` | W | — |
| `SCR-009` | First-turn objectives | Home | Mandatory | Auth | WORLD | ACC | ONB; WEP-203–215 | `REQ-878` | `FLOW-004/025` | `UIX-04/24` | `UAT-SCR-009` | R | — |
| `SCR-010` | Public nation profile | Public | Mandatory | Public | ACC | POL/WAR/WORLD | NAT-015; TR-021/022 | `REQ-879` | `FLOW-027` | `UIX-07` | `UAT-SCR-010` | R | `PRV` |
| `SCR-011` | Account home | Account | Mandatory | Auth | ACC | FP | ACC-017/018; D-041 | `REQ-880` | `FLOW-030` | `UIX-27` | `UAT-SCR-011` | R | — |
| `SCR-012` | Account closure | Account | Mandatory | Auth | ACC | FP | ACC-043; D-026 | `REQ-881` | `FLOW-030` | `UIX-27` | `UAT-SCR-012` | W | `RET` |
| `SCR-013` | Command Digest | Home | Mandatory | Auth | TURN | WORLD/ECON/POL/WAR | TR-088/089/092; REQ-022 | `REQ-882` | `FLOW-005` | `UIX-05/06` | `UAT-SCR-013` | R | — |
| `SCR-014` | Inbox | Home | Mandatory | Auth | TURN | MKT/DIP/ALL/WAR | TR-004; D-016/D-030 | `REQ-883` | `FLOW-006` | `UIX-06` | `UAT-SCR-014` | R | — |
| `SCR-015` | National Overview | Home | Mandatory | Auth | ECON | CITY/POL/WAR | ECN-176/177; URB-052; DMP-073 | `REQ-884` | `FLOW-005` | `UIX-07` | `UAT-SCR-015` | R | — |
| `SCR-016` | Turn & settlement status | Home | Mandatory | Auth | TURN | — | TR-027/030/033/035/036/039/075/080 | `REQ-885` | `FLOW-005/033` | `UIX-05` | `UAT-SCR-016` | R | — |
| `SCR-017` | National Chronicle | Home | Mandatory | Auth | WORLD | TURN | D-026; TR-049 | `REQ-886` | `FLOW-027` | `UIX-07/24` | `UAT-SCR-017` | R | `RET` |
| `SCR-018` | Network View | World | Mandatory | Auth | DIP | ALL/WAR | TR-012/013/014; REQ-041 | `REQ-887` | — | `UIX-07` | `UAT-SCR-018` | R | — |
| `SCR-019` | Alerts & notification history | Home | Mandatory | Auth | TURN | all | REQ-731; DIP-114/116 | `REQ-888` | `FLOW-027` | `UIX-06` | `UAT-SCR-019` | R/W | `PROV-1183` |
| `SCR-020` | Pinned objects | Home | Conditional | Auth | SHELL | all | `13A-OQ-012` | `REQ-889` | — | `UIX-P01` | `UAT-SCR-020` | W | `PROV-OQ012` |
| `SCR-021` | Political Panel | Politics | Mandatory | Auth | POL | TURN | DMP-256/268 | `REQ-890` | `FLOW-005` | `UIX-14` | `UAT-SCR-021` | R | — |
| `SCR-022` | Government structure | Politics | Mandatory | Auth | POL | — | D-084/D-085; DMP-079–083 | `REQ-891` | — | `UIX-14` | `UAT-SCR-022` | R | — |
| `SCR-023` | Approval & stability | Politics | Mandatory | Auth | POL | — | DMP-073; F-PD-004–009 | `REQ-892` | — | `UIX-14` | `UAT-SCR-023` | R | — |
| `SCR-024` | Policy axes | Politics | Mandatory | Auth | POL | — | D-087; DMP-101/102 | `REQ-893` | `FLOW-007` | `UIX-14` | `UAT-SCR-024` | W | — |
| `SCR-025` | Election dashboard | Politics | Mandatory | Auth | POL | — | D-106/D-107; DMP-178/184 | `REQ-894` | `FLOW-008` | `UIX-14` | `UAT-SCR-025` | R | — |
| `SCR-026` | Campaign actions | Politics | Mandatory | Auth | POL | ECON | D-094; DMP-189/193 | `REQ-895` | `FLOW-008` | `UIX-14` | `UAT-SCR-026` | W | — |
| `SCR-027` | Election result | Politics | Mandatory | Auth | POL | — | DMP-184/205/210 | `REQ-896` | — | `UIX-14` | `UAT-SCR-027` | R | — |
| `SCR-028` | Crisis & recovery | Politics | Mandatory | Auth | POL | ECON | DMP-163/225/229/248 | `REQ-897` | `FLOW-007` alt | `UIX-14` | `UAT-SCR-028` | R/W | — |
| `SCR-029` | Treasury | Economy | Mandatory | Auth | ECON | MKT/ALL | ECN-176/177/178; D-050 | `REQ-898` | `FLOW-005` | `UIX-08` | `UAT-SCR-029` | R | — |
| `SCR-030` | Budget & national wealth | Economy | Mandatory | Auth | ECON | CITY | D-051/D-062; ECN-105/107 | `REQ-899` | — | `UIX-08` | `UAT-SCR-030` | R | — |
| `SCR-031` | Economic reports | Economy | Mandatory | Auth | ECON | — | ECN-142; D-026 | `REQ-900` | — | `UIX-08` | `UAT-SCR-031` | R | `RET` |
| `SCR-032` | Production policy | Economy | Mandatory | Auth | ECON | CITY | D-053; ECN-044/045/053/139 | `REQ-901` | `FLOW-009/010` | `UIX-09` | `UAT-SCR-032` | W | — |
| `SCR-033` | Resources & warehouse | Economy | Mandatory | Auth | ECON | MKT/CITY | MKT-053; ECN-120; URB-066 | `REQ-902` | `FLOW-010` | `UIX-10` | `UAT-SCR-033` | R | — |
| `SCR-034` | Power grid | Economy | Mandatory | Auth | ECON | CITY | D-048; ECN-056/059/060/061/064 | `REQ-903` | — | `UIX-10` | `UAT-SCR-034` | R | — |
| `SCR-035` | Directed-trade inbox | Economy | Mandatory | Auth | MKT | ECON | MKT-105/125; D-016 | `REQ-904` | `FLOW-011`…`013` | `UIX-15` | `UAT-SCR-035` | R/W | — |
| `SCR-036` | Compose/counter offer | Economy | Mandatory | Auth | MKT | ECON | MKT-019/022/037/038/061 | `REQ-905` | `FLOW-011/013` | `UIX-15` | `UAT-SCR-036` | W | — |
| `SCR-037` | Offer detail | Economy | Mandatory | Parties | MKT | ECON | MKT-056/131; ECON-054 | `REQ-906` | `FLOW-012/013` | `UIX-15` | `UAT-SCR-037` | R/W | — |
| `SCR-038` | Global Trade board | Economy | Conditional | — | MKT | ECON | D-117/D-122; G-1…G-6 | `REQ-907` | — | `UIX-B01` | `UAT-SCR-038` | none | `BLK-GT` |
| `SCR-039` | Listing detail | Economy | Conditional | — | MKT | ECON | D-111; MKT-106–108 | `REQ-908` | — | `UIX-B01` | `UAT-SCR-039` | none | `BLK-GT` |
| `SCR-040` | Trade history | Economy | Mandatory | Auth | MKT | WORLD | D-117; MKT-140; D-026 | `REQ-909` | — | `UIX-16` | `UAT-SCR-040` | R | `BLK-GT` (statistic) |
| `SCR-041` | Cities overview | Cities | Mandatory | Auth | CITY | ECON | URB-031; D-067 | `REQ-910` | `FLOW-014/015` | `UIX-11` | `UAT-SCR-041` | R | — |
| `SCR-042` | City detail | Cities | Mandatory | Auth | CITY | ECON | URB-052/124–127 | `REQ-911` | `FLOW-014` | `UIX-11` | `UAT-SCR-042` | R/W | — |
| `SCR-043` | Construction queue | Cities | Mandatory | Auth | CITY | ECON | URB-064/148; D-073/D-074 | `REQ-912` | `FLOW-014` | `UIX-11` | `UAT-SCR-043` | W | — |
| `SCR-044` | Production chains | Cities | Mandatory | Auth | CITY | ECON | URB-149; ECN-147/147a | `REQ-913` | `FLOW-009` | `UIX-09/10` | `UAT-SCR-044` | R | — |
| `SCR-045` | Research | Cities | Mandatory | Auth | CITY | ECON | URB-102/150/095; D-076–078 | `REQ-914` | `FLOW-016` | `UIX-13` | `UAT-SCR-045` | W | — |
| `SCR-046` | Found new city | Cities | Mandatory | Auth | CITY | ECON | URB-032–034; D-068 | `REQ-915` | `FLOW-015` | `UIX-12` | `UAT-SCR-046` | W | — |
| `SCR-047` | Diplomatic overview | Foreign | Mandatory | Auth | DIP | ALL | 08C §12.2; DIP-023/024 | `REQ-916` | `FLOW-017/018` | `UIX-17` | `UAT-SCR-047` | R | — |
| `SCR-048` | Pair screen | Foreign | Mandatory | Auth | DIP | ALL/FP | DIP-023/024/086/088; NET-023 | `REQ-917` | `FLOW-017` | `UIX-17` | `UAT-SCR-048` | R | `PRV` |
| `SCR-049` | Proposal & negotiation | Foreign | Mandatory | Auth | DIP | — | D-030; 08C §12.3 | `REQ-918` | `FLOW-017` | `UIX-17` | `UAT-SCR-049` | W | — |
| `SCR-050` | Agreement/treaty detail | Foreign | Mandatory | Auth | DIP | — | DP-T01–T03; DP-A01; DIP-108–113 | `REQ-919` | `FLOW-018` | `UIX-17` | `UAT-SCR-050` | R | — |
| `SCR-051` | Publication state | Foreign | Mandatory | Auth | DIP | — | DIP-108–113; D-030 | `REQ-920` | — | `UIX-17` | `UAT-SCR-051` | R | `K5` |
| `SCR-052` | Relations history | Foreign | Mandatory | Auth | DIP | WORLD | 08C §12.6; D-026 | `REQ-921` | — | `UIX-17` | `UAT-SCR-052` | R | `RET` |
| `SCR-053` | Alliance home | Foreign | Mandatory | Public/Auth | ALL | DIP/WAR | ALL-086 | `REQ-922` | `FLOW-019` | `UIX-18` | `UAT-SCR-053` | R | `UD-048` |
| `SCR-054` | Membership & applicants | Foreign | Mandatory | Member | ALL | FP | ALL-080–086; D-133 | `REQ-923` | `FLOW-019` | `UIX-18` | `UAT-SCR-054` | W | `UD-040/044` |
| `SCR-055` | Governance & roles | Foreign | Mandatory | Role | ALL | — | D-135; AN matrix; REQ-553 | `REQ-924` | — | `UIX-18` | `UAT-SCR-055` | W | `UD-045` |
| `SCR-056` | Tax brackets | Foreign | Mandatory | Role | ALL | ECON | ALL-179–187; UD-040/045 | `REQ-925` | `FLOW-020` | `UIX-19` | `UAT-SCR-056` | W | `UD-040` |
| `SCR-057` | Alliance finances | Foreign | Mandatory | Member | ALL | ECON/FP | ALL-187/193/220–226; D-141; UD-046 | `REQ-926` | `FLOW-020` | `UIX-19` | `UAT-SCR-057` | R | `UD-046` |
| `SCR-058` | Alliance diplomacy | Foreign | Mandatory | Role | ALL | DIP/WAR | D-140; AT-E00/E01; WAR-149; UD-047 | `REQ-927` | — | `UIX-20` | `UAT-SCR-058` | W | `UD-047` |
| `SCR-059` | Military overview | War | Mandatory | Auth | WAR | ECON | D-015 (10B-C3); WAR-039 | `REQ-928` | `FLOW-005` | `UIX-23` | `UAT-SCR-059` | R | — |
| `SCR-060` | Forces & upkeep | War | Mandatory | Auth | WAR | ECON | WAR-049–053; WAR-109f–m | `REQ-929` | — | `UIX-23` | `UAT-SCR-060` | R | — |
| `SCR-061` | War Operations Board | War | Mandatory | Owner | WAR | — | WAR-148/161; REQ-589–591; AX-18 | `REQ-930` | `FLOW-021/022` | `UIX-21` | `UAT-SCR-061` | W | — |
| `SCR-062` | Conflicts ledger | War | Mandatory | Auth/Public | WAR | WORLD | WAR-085–088 | `REQ-931` | — | `UIX-23` | `UAT-SCR-062` | R | — |
| `SCR-063` | War detail | War | Mandatory | Auth | WAR | DIP | WAR-085–088/150 | `REQ-932` | `FLOW-023` | `UIX-23` | `UAT-SCR-063` | R | — |
| `SCR-064` | Battle report | War | Mandatory | Participant | WAR | — | WAR-088/109k | `REQ-933` | — | `UIX-23` | `UAT-SCR-064` | R | — |
| `SCR-065` | War reports & losses | War | Mandatory | Owner | WAR | — | WAR-109f–m | `REQ-934` | — | `UIX-23` | `UAT-SCR-065` | R | — |
| `SCR-066` | Military history | War | Mandatory | Auth | WAR | WORLD | D-026 | `REQ-935` | — | `UIX-23` | `UAT-SCR-066` | R | `RET` |
| `SCR-067` | Settlement & peace | War | Mandatory | Parties | WAR | DIP | WAR-126–129/131/132; UD-032 | `REQ-936` | `FLOW-023/024` | `UIX-22` | `UAT-SCR-067` | W | `UD-032(A)` |
| `SCR-068` | Strategic intelligence | War | Provisional | — | WAR | — | no rule; espionage excluded | `REQ-937` | — | `UIX-B02` | `UAT-SCR-068` | none | `BLK-INTEL` |
| `SCR-069` | Events Centre | World | Mandatory | Auth | WORLD | TURN | WEP-633/713; WPC-14 | `REQ-938` | `FLOW-005` | `UIX-24` | `UAT-SCR-069` | R | — |
| `SCR-070` | Event detail | World | Mandatory | Auth | WORLD | ECON/POL/WAR | WEP-179/619 | `REQ-939` | — | `UIX-24` | `UAT-SCR-070` | R | — |
| `SCR-071` | Objectives & Challenges | World | Mandatory | Auth | WORLD | — | WEP-203–215 | `REQ-940` | `FLOW-025` | `UIX-24` | `UAT-SCR-071` | R/W | — |
| `SCR-072` | Standings | World | Mandatory | Auth/Public | WORLD | — | WEP-324/325/359/361/362 | `REQ-941` | — | `UIX-24` | `UAT-SCR-072` | R | `K5` |
| `SCR-073` | Achievements & rewards | World | Mandatory | Auth | WORLD | — | WEP-499/663 | `REQ-942` | `FLOW-026` | `UIX-25` | `UAT-SCR-073` | R | — |
| `SCR-074` | National Progress | World | Mandatory | Auth | WORLD | — | WEP-423 | `REQ-943` | — | `UIX-24` | `UAT-SCR-074` | R | — |
| `SCR-075` | Reward History | World | Mandatory | Auth | WORLD | — | WEP-633/663/705 | `REQ-944` | `FLOW-026` | `UIX-25` | `UAT-SCR-075` | R/W | — |
| `SCR-076` | World Chronicle | World | Mandatory | Auth/Public | WORLD | — | D-026; TR-049 | `REQ-945` | — | `UIX-24` | `UAT-SCR-076` | R | `RET` |
| `SCR-077` | World Health | World | Conditional | Auth | WORLD | — | D-027; WEP-663 | `REQ-946` | — | `UIX-P02` | `UAT-SCR-077` | R | `PROV-K5` |
| `SCR-078` | World Guide | World | Mandatory | Public | WORLD | — | F-010; DP-004 | `REQ-947` | `FLOW-004` | `UIX-07` | `UAT-SCR-078` | R | — |
| `SCR-079` | Privacy centre | Account | Mandatory | Auth | FP | — | PRV-002/009/014 | `REQ-948` | — | `UIX-27` | `UAT-SCR-079` | W | `UD-017/055` |
| `SCR-080` | Security settings | Account | Mandatory | Auth | ACC | FP | D-029/D-041; ACC-031 | `REQ-949` | — | `UIX-27` | `UAT-SCR-080` | W | — |
| `SCR-081` | Report creation | Account | Mandatory | Auth | FP | — | MOD-002/007; FR-001/006 | `REQ-950` | `FLOW-028` | `UIX-26` | `UAT-SCR-081` | W | — |
| `SCR-082` | Report status | Account | Mandatory | Reporter | FP | — | MOD-017/018; EVD-009 | `REQ-951` | `FLOW-028` | `UIX-26` | `UAT-SCR-082` | R | — |
| `SCR-083` | Appeal | Account | Mandatory | Auth | FP | — | MOD-013/015 | `REQ-952` | `FLOW-029` | `UIX-26` | `UAT-SCR-083` | W | `UD-059` |
| `SCR-084` | Restrictions & sanctions | Account | Mandatory | Auth | FP | ACC | NET-023/050; PRV-019; MOD-027 | `REQ-953` | `FLOW-027` | `UIX-26` | `UAT-SCR-084` | R | `UD-053` |
| `SCR-085` | My data | Account | Mandatory | Auth | FP | ACC | D-026; DAT-001; PRV-001 | `REQ-954` | — | `UIX-27` | `UAT-SCR-085` | W | `UD-055` |
| `SCR-086` | Review explanation | Account | Mandatory | Auth | FP | ACC | D-033/D-034; NET-023 | `REQ-955` | — | `UIX-26` | `UAT-SCR-086` | R | — |
| `SCR-087` | Support centre | Account | Mandatory | Auth | FP | — | intake taxonomy; FR-001 | `REQ-956` | — | `UIX-26` | `UAT-SCR-087` | W | — |
| `SCR-088` | Change disclosures | World | Mandatory | Public | WORLD | FP | TR-049; MOD-017/018 | `REQ-957` | — | `UIX-30` | `UAT-SCR-088` | R | — |
| `SCR-089` | Protection state | Home | Mandatory | Auth | ACC | FP/WAR | ONB-020/022; D-040; WAR-115–117 | `REQ-958` | `FLOW-027` | `UIX-26` | `UAT-SCR-089` | R | — |
| `SCR-090` | Reroll confirmation | Account | Mandatory | Auth | ACC | ECON/WORLD | RRL-005/006/012/021; D-039 | `REQ-959` | `FLOW-031` | `UIX-03` | `UAT-SCR-090` | W | `RRL` |
| `SCR-091` | Admin console | Admin | Admin | Role | ADMIN | — | ADM-003/021/022; D-042 | `REQ-960` | — | `UIX-28` | `UAT-SCR-091` | R | — |
| `SCR-092` | Moderation queue | Admin | Admin | Role | ADMIN | FP | ADM-021/022 | `REQ-961` | `FLOW-032` | `UIX-28` | `UAT-SCR-092` | R/W | — |
| `SCR-093` | Case & evidence | Admin | Admin | Role | ADMIN | FP | EVD classes; V-01–V-16 | `REQ-962` | `FLOW-032` | `UIX-28` | `UAT-SCR-093` | R/W | `SEC-OBL` |
| `SCR-094` | Sanctions administration | Admin | Admin | Role | ADMIN | ACC/FP | MOD-036/037/042; MOD-022 | `REQ-963` | `FLOW-032` | `UIX-28` | `UAT-SCR-094` | W | `UD-053` |
| `SCR-095` | Shared-network review | Admin | Admin | Role | ADMIN | ACC | D-033/D-034 | `REQ-964` | `FLOW-032` | `UIX-28` | `UAT-SCR-095` | R/W | — |
| `SCR-096` | Audit ledger viewer | Admin | Admin | Role | ADMIN | FP | SEC-021/036–040; EVD-026 | `REQ-965` | — | `UIX-29` | `UAT-SCR-096` | R | `SEC-OBL` |
| `SCR-097` | Turn-engine monitor | Admin | Admin | Role | TURN | ADMIN | TR-035/036/043/075/080 | `REQ-966` | — | `UIX-29` | `UAT-SCR-097` | R/W | — |
| `SCR-098` | Data operations | Admin | Admin | Role | ADMIN | FP | D-026; PRV-023; COR | `REQ-967` | — | `UIX-29` | `UAT-SCR-098` | W | `SEC-OBL` |
| `SCR-099` | Announcement composer | Admin | Admin | Role | ADMIN | FP | MOD-017/018; ALL-164 | `REQ-968` | — | `UIX-30` | `UAT-SCR-099` | W | — |
| `SCR-100` | Admin roles | Admin | Admin | Role | ADMIN | — | ADM-003; D-042; FR postures | `REQ-969` | — | `UIX-29` | `UAT-SCR-100` | W | — |

### 8.1 Matrix A tallies

- **100 screens** accounted for: 85 Mandatory player, 4 Conditional player (`SCR-020/038/039/077`), 1 Provisional player (`SCR-068`), 10 Mandatory administrative (`SCR-091`…`SCR-100`).
- **Status:** 95 SPECIFIED, 2 PROVISIONAL (`SCR-020`, `SCR-077`), 3 BLOCKED (`SCR-038`, `SCR-039`, `SCR-068`).
- **R/W posture:** 52 read-only, 45 write/both (34 write-only + 11 read/write), 3 absent.
- **Integration status:** 95 `INTEGRATED`, 2 `INTEGRATED-PROVISIONAL` (`SCR-020`, `SCR-077`), 3 `INTEGRATED-BLOCKED` as absence (`SCR-038`, `SCR-039`, `SCR-068`), 0 unexplained gaps.

### 8.2 Limitation codes

| Code | Meaning |
|---|---|
| `BRAND` | Brand values (`13A-OQ-001/002`) remain owner-reserved |
| `PRV` | Field visibility is class-filtered (B-12/TR-021) |
| `RET` | Retention class applies; hot records may compact |
| `PROV-OQ012` | Pins absent until fair-play review |
| `PROV-1183` | Notification routing-tier defaults are provisional |
| `PROV-K5` | Per-figure k=5 suppression |
| `K5` | k=5 aggregate suppression |
| `BLK-GT` | Global Trade gate G-1…G-6 not met |
| `BLK-INTEL` | No intelligence rule exists; espionage excluded |
| `UD-040` | Alliance founding/cost/multi-membership owner-reserved |
| `UD-044` | Membership rights/rejoin owner-reserved |
| `UD-045` | Capability/delegation owner-reserved outside the narrow tax set |
| `UD-046` | Treasury ownership/spending owner-reserved; no spendable purpose |
| `UD-047` | Collective diplomacy owner-reserved |
| `UD-048` | Discord-link policy owner-reserved |
| `UD-053` | Sanction ladder scale/authority owner-reserved |
| `UD-055` | Retention/erasure-vs-spine owner/legal-reserved |
| `UD-059` | Appeal count/window owner-reserved |
| `UD-017` | Applicable law owner/legal-reserved |
| `SEC-OBL` | Production security obligations outstanding (treasury UPDATE, 0005, SQL tests, audit trigger, digest job) |
| `RRL` | Reroll block conditions and exact-phrase rule |

---

## 9. Matrix B — Reverse system-to-screen traceability

**Coverage classes:** `Complete` (every specified capability has a legitimate surface), `Partial` (surface exists; a named limitation remains), `Blocked` (specified as absent by a gate/rule), `Candidate` (no product obligation yet), `Open-Owner` (surface cannot exist until an owner decision).

| Capability | Source | Screens | Coverage | Note / gap |
|---|---|---|---|---|
| **A. Account and player identity** | | | | |
| Registration and e-mail verification | B-03 ACC-023/024 | `SCR-002`, `SCR-006` | Complete | `UIX-02` |
| Login, session expiry and recovery | B-03 ACC-018/031; D-041 | `SCR-003`…`SCR-005`, `SCR-080` | Complete | `UIX-01/27` |
| Nation creation and ownership | B-03 NAT; D-038 | `SCR-007`, `SCR-010`, `SCR-011` | Complete | `UIX-03` |
| Onboarding and first objectives | B-03 ONB; D-040 | `SCR-008`, `SCR-009` | Complete | `UIX-04` |
| Account settings, closure and data rights | B-03; B-12 PRV/DAT; D-026 | `SCR-011`, `SCR-012`, `SCR-079`, `SCR-080`, `SCR-085` | Complete | Data-export mechanism is Stage 5/6 |
| Protection and dormancy states | B-03 ONB-020/022; D-028/D-040 | `SCR-089`, `SCR-084` | Partial | Dormancy is shown as account/nation state; no separate dormancy screen (`GAP-13D-13`, informational) |
| Reroll | B-03 RRL-005/006; D-039 | `SCR-090`, `SCR-007` | Complete | Exact-phrase barrier required |
| One account per person / shared-network review | B-03 D-032/D-033/D-034 | `SCR-086`, `SCR-095` | Complete | Review mechanism not disclosed |
| **B. Core loop and turn system** | | | | |
| Two-hour UTC boundaries and phase position | B-02 TR-024/027/030/033 | Shell, `SCR-013`, `SCR-016`, `SCR-097` | Complete | `UIX-05` |
| Turn progress and settlement state | B-02 TR-035/036/039 | `SCR-016`, `SCR-097` | Complete | `INTERRUPTED`/`FAILED` named |
| Digest of settled changes | B-02 TR-088/089/092; REQ-022 | `SCR-013`, `SCR-017` | Complete | `UIX-06` |
| Pending actions aggregation | B-02 TR-004 | `SCR-014`, owning screens | Complete | `UIX-06` |
| Notifications and alerts | REQ-731; DIP-114/116 | `SCR-019`, `SCR-013`, `SCR-069` | Complete | Tier defaults provisional |
| Scheduled processing and recovery | B-02 TR-075/080 | `SCR-016`, `SCR-097` | Complete | Operator recovery surface admin-only |
| **C. Economy and national finances** | | | | |
| Treasury triple and position | B-04 ECN-176/177; D-050 | `SCR-029`, `SCR-033`, `SCR-015`, `SCR-057` | Complete | `UIX-08` |
| Income, expenditure and budget | B-04 D-051; ECN-093/097/098 | `SCR-029`…`SCR-031` | Complete | `UIX-08` |
| Taxes and production policy | B-04 D-053; ECN-044/045 | `SCR-032`, `SCR-044` | Complete | `UIX-09` |
| Resources, warehouse and power | B-04/B-05 MKT-053; D-048 | `SCR-033`, `SCR-034` | Complete | `UIX-10` |
| Economic reports and history | B-04 ECN-142; D-026 | `SCR-031`, `SCR-040` | Complete | Retention applies |
| Financial validation and failure | B-04 failure families | All economic screens | Complete | `ERR-08`…`ERR-17` |
| Financial correction path | B-12 COR/INT-003 | `SCR-093`, `SCR-098` | Partial | Correction is admin-only; no player-facing correction |
| **D. Cities, infrastructure and production** | | | | |
| Cities overview and detail | B-05 URB-031/052 | `SCR-041`, `SCR-042` | Complete | `UIX-11` |
| Buildings and infrastructure | B-05 URB-124–127 | `SCR-042`, `SCR-043` | Complete | `UIX-11` |
| Construction queue and slot | B-05 URB-064/148; D-073 | `SCR-043` | Complete | One slot per city |
| Production chains and maintenance | B-05 URB-149; ECN-147/147a | `SCR-044`, `SCR-032` | Complete | `UNMAINTAINED` state |
| Research | B-05 URB-093–097/150; D-076 | `SCR-045` | Complete | One active project |
| City founding | B-05 URB-032–034; D-068 | `SCR-046` | Complete | No cooldown invented |
| Demolition/refund | B-05 URB-071; D-074 | `SCR-042`, `SCR-043` | Complete | 25% crown-only |
| Development capacity | B-05 URB-052 | `SCR-041`, `SCR-042` | Complete | `used / total` |
| **E. Population and domestic politics** | | | | |
| Population and housing | B-06; B-05 URB-052 | `SCR-015`, `SCR-042` | Complete | `UIX-07/11` |
| Approval and stability | B-06 DMP-073; F-PD-004–009 | `SCR-021`, `SCR-023` | Complete | Six supports; no invented bands |
| Elections and campaigns | B-06 D-106/D-107; DMP-189 | `SCR-025`…`SCR-027` | Complete | Anchor `campaign_open_turn` |
| Government and policies | B-06 D-084/D-087 | `SCR-022`, `SCR-024` | Complete | Six permanent governments |
| Crisis and recovery | B-06 DMP-163/225/229/248 | `SCR-028` | Complete | 18-turn stability-only |
| Leadership and transition | B-06 DMP-184/205/210 | `SCR-021`, `SCR-027` | Complete | Administration changes; government does not |
| **F. Trade and markets** | | | | |
| Directed trade lifecycle | B-07 MKT-105/125; D-016/D-017 | `SCR-035`…`SCR-037` | Complete | `UIX-15` |
| Order management and revisions | B-07 MKT-019–061 | `SCR-035`, `SCR-036` | Complete | 10 revisions, 72-turn expiry |
| Global Trade listings/execution | B-07 D-110/D-111/D-122 | `SCR-038`, `SCR-039` | Blocked | G-1…G-6 not met |
| Trade history and reference prices | B-07 D-117; MKT-140 | `SCR-040` | Partial | Pre-gate minimal; no statistic |
| Treasury integration | B-07/B-04 MKT-053; ECON-054 | `SCR-029`, `SCR-037` | Complete | Atomic settlement |
| Trade restrictions and failures | B-07 MKT-038/041; B-12 D-034 | `SCR-035`, `SCR-037`, `SCR-086` | Complete | Fresh-nation band |
| Market statistics | B-07 D-117 | `SCR-040` | Blocked | `INSUFFICIENT_SAMPLE` until gate |
| **G. Diplomacy** | | | | |
| Posture and relationships | B-08 DIP-023/024 | `SCR-047`, `SCR-048`, `SCR-052` | Complete | `UIX-17` |
| Agreements (NAP, consultation, aid) | B-08 DP-T01–T03 | `SCR-049`…`SCR-051` | Complete | Parties-only pending |
| Embargo | B-08 DP-A01 | `SCR-047`, `SCR-050` | Complete | Distinct from treaty |
| Publication and visibility | B-08 DIP-108–113; D-030 | `SCR-050`, `SCR-051` | Complete | k=5 aggregates |
| Proposal lifecycle | B-08 DIP-044/052 | `SCR-049` | Complete | One live proposal per direction |
| Expiry and termination | B-08 DIP-101/103/130 | `SCR-050`, `SCR-052` | Complete | Freeze-aware |
| **H. Alliances** | | | | |
| Founding and membership | B-09 ALL-080–086 | `SCR-053`, `SCR-054` | Complete | UD-040/044 Open |
| Roles and governance | B-09 D-135; AX-05 | `SCR-055` | Complete | UD-045 Open |
| Automatic taxation | B-09 ALL-179–187; AX-27 | `SCR-056`, `SCR-057` | Complete | 0% fallback while UD-040 Open |
| ARL and donations | B-09 AX-28; D-141 | `SCR-057` | Complete | Four categories; no withdrawal |
| Operational funding | B-09 D-141; UD-046 | `SCR-057` | Partial | No approved cost schedule; unavailable state |
| Alliance treaties and NAP | B-09 AX-29/AX-30; D-140 | `SCR-058` | Complete | UD-047 Open |
| Member readiness declarations | B-09 AX-12 | none | Candidate | Candidate informational feature; no product obligation (`GAP-13D-04`) |
| Alliance diplomatic positions | B-09 AX-16 | `SCR-058` (record-only) | Open-Owner | UD-047; no binding position object |
| Static Discord invite | B-09 AX-19 | `SCR-053` (disclosure-controlled) | Open-Owner | UD-048; host policy unresolved |
| Grievances and redress | B-09 UD-044; B-12 MOD-013 | `SCR-054`, `SCR-083` | Partial | Expulsion appeal stays UD-044 |
| Alliance audit/history | B-09 AX-21; D-026 | `SCR-053`, `SCR-057` | Partial | No dedicated alliance history screen; records reachable from surfaces (`GAP-13D-05`, Low) |
| No alliance military authority | B-09 AX-18; WAR-148/161 | `SCR-058`, `SCR-061` | Complete | Permanent prohibition |
| **I. Warfare and settlements** | | | | |
| Military overview and readiness | B-10 WAR-039/049–053 | `SCR-059`, `SCR-060` | Complete | `UIX-21/23` |
| Operations and OP | B-10 D-015/10B-C3; WAR-152 | `SCR-061`, `SCR-059` | Complete | One national pool |
| Campaigns and war records | B-10 WAR-085–088/150 | `SCR-062`, `SCR-063` | Complete | Field-filtered |
| Battle reports | B-10 WAR-088/109k | `SCR-064`, `SCR-065` | Complete | Participant vs public |
| Settlements and peace | B-10 WAR-126–129 | `SCR-067` | Complete | One live settlement |
| Surrender | B-10 WAR-131/132 | `SCR-067` | Complete | Always available |
| Protection recheck | B-10 WAR-115–117 | `SCR-061`, `SCR-063`, `SCR-089` | Complete | Visibility-only |
| Espionage/intelligence | B-10 exclusion; 13A-OQ-010 | `SCR-068` | Blocked | No rule; no build authority |
| Military history | B-10/B-11 D-026 | `SCR-066` | Complete | Retention |
| **J. World events, objectives and progression** | | | | |
| Events and consequences | B-11 WEP-179/619/633 | `SCR-069`, `SCR-070` | Complete | `UIX-24` |
| Objectives | B-11 WEP-203–215 | `SCR-009`, `SCR-071` | Complete | Penalty-free dismissal |
| Standings | B-11 WEP-324/325/359 | `SCR-072` | Complete | Denominator/window |
| Achievements | B-11 WEP-499/663 | `SCR-073` | Complete | Six reward classes |
| Progression layers | B-11 WEP-423 | `SCR-074` | Complete | Eight layers; no composite |
| Rewards and deferred claims | B-11 WEP-633/705 | `SCR-075` | Complete | Deferred visible |
| World chronicle | B-11 D-026/TR-049 | `SCR-076` | Complete | Public/disclosed |
| World health aggregates | B-11 D-027; WEP-663 | `SCR-077` | Blocked | k=5 per figure |
| **K. Fair play, security and administration** | | | | |
| Reporting | B-12 MOD-002/007 | `SCR-081`, `SCR-082` | Complete | `UIX-26` |
| Moderation and cases | B-12 ADM-021/022; EVD | `SCR-092`, `SCR-093` | Complete | Every read audited |
| Sanctions ladder | B-12 MOD-036/037; UD-053 | `SCR-094` | Partial | Tier authority owner-reserved |
| Appeals | B-12 MOD-013/015 | `SCR-083`, `SCR-084` | Complete | Never blocked |
| Restrictions | B-12 NET-023/050; PRV-019 | `SCR-084`, `SCR-086` | Complete | Reason class only |
| Shared-network review | B-03/B-12 D-033/D-034 | `SCR-095` | Complete | Mechanism not exposed |
| Audit ledger | B-12 SEC-036–040; EVD-026/030 | `SCR-096` | Blocked | Verification job absent (`SEC-OBL`) |
| Turn operations | B-02 TR-035/075/080 | `SCR-097` | Complete | Operator recovery |
| Data operations/retention | B-12 D-026; PRV-023 | `SCR-098`, `SCR-085` | Partial | Legal/retention owner-reserved |
| Announcements and change disclosure | B-12 MOD-017/018; TR-049 | `SCR-099`, `SCR-088` | Complete | `UIX-30` |
| Admin roles and permissions | B-12 ADM-003; D-042 | `SCR-091`, `SCR-100` | Complete | Least privilege |
| Privacy classes | B-12 PRV-002/009/014 | `SCR-079`, `SCR-085` | Complete | `SEC` never rendered |
| Security notices | B-03/B-12; TR-049 | `SCR-019`, `SCR-088` | Complete | Non-opt-out preserved |

**Reverse-mapping conclusion.** 90 capabilities assessed: 74 Complete, 8 Partial, 5 Blocked, 2 Open-Owner and 1 Candidate. No capability is silently absent; every non-complete row is registered in §17 or classified as an intentional gate.

---

## 10. Matrix L — Navigation reachability

**Derived from** the 13B master navigation register (§7.2), which remains authoritative for direct entries, related destinations and restrictions. This matrix adds the journey association and a reachability verdict. `Entry` gives the shortest legitimate path; `Return` is the canonical parent unless a breadcrumb supplies deeper return. Conditional screens have no route until their gate.

| SCR | Parent | Route key | Entry | Return | Journeys | Reachability |
|---|---|---|---|---|---|---|
| `SCR-001` | Public | `public.landing` | Any unauthenticated URL | — | `JRN-A` | Reachable |
| `SCR-002` | Public | `public.register` | Landing CTA | `SCR-001` | `JRN-A` | Reachable |
| `SCR-003` | Public | `public.login` | Landing; session expiry | `SCR-001` | `JRN-A/B` | Reachable |
| `SCR-004` | Public | `public.reset` | Login link | `SCR-003` | `JRN-A` | Reachable |
| `SCR-005` | Public | `public.recovery` | Reset; security settings | `SCR-003` | `JRN-A` | Reachable |
| `SCR-006` | Public | `public.verify` | Registration; unverified login | `SCR-003` | `JRN-A` | Reachable |
| `SCR-007` | Public | `public.create-nation` | Verified account | `SCR-006` | `JRN-A` | Reachable |
| `SCR-008` | Home | `home.onboarding` | First nation creation | `SCR-013` | `JRN-A` | Reachable |
| `SCR-009` | Home | `home.objectives-entry` | Onboarding; objectives | `SCR-013` | `JRN-A` | Reachable |
| `SCR-010` | Public | `public.nation` | Object link; search | Prior page | `JRN-J` (support) | Reachable |
| `SCR-011` | Account | `account.home` | Account menu | Prior page | `JRN-L` | Reachable |
| `SCR-012` | Account | `account.closure` | Account home | `SCR-011` | `JRN-L` | Reachable |
| `SCR-013` | Home | `home.digest` | Primary nav; post-login | — | `JRN-A/B/C` | Reachable |
| `SCR-014` | Home | `home.inbox` | Shell alert; digest | `SCR-013` | `JRN-B/K` | Reachable |
| `SCR-015` | Home | `home.overview` | Primary nav; digest | `SCR-013` | `JRN-B/C` | Reachable |
| `SCR-016` | Home | `home.turn` | Shell countdown | `SCR-013` | `JRN-B/C` | Reachable |
| `SCR-017` | Home | `home.chronicle` | Overview; digest | `SCR-015` | `JRN-B` (support) | Reachable |
| `SCR-018` | World | `world.network` | World nav; overview | `SCR-069` | `JRN-J` | Reachable |
| `SCR-019` | Home | `home.alerts` | Shell alert count | `SCR-013` | `JRN-B/K` | Reachable |
| `SCR-020` | Home | `home.pins` | — (gate) | — | — | **Absent** (`PROV-OQ012`) |
| `SCR-021` | Politics | `politics.panel` | Primary nav | — | `JRN-G` | Reachable |
| `SCR-022` | Politics | `politics.government` | Panel | `SCR-021` | `JRN-G` | Reachable |
| `SCR-023` | Politics | `politics.approval` | Panel | `SCR-021` | `JRN-G` | Reachable |
| `SCR-024` | Politics | `politics.axes` | Panel | `SCR-021` | `JRN-G` | Reachable |
| `SCR-025` | Politics | `politics.elections` | Panel | `SCR-021` | `JRN-G` | Reachable (ELECTORAL) |
| `SCR-026` | Politics | `politics.campaign` | Election dashboard | `SCR-025` | `JRN-G` | Reachable (ELECTORAL) |
| `SCR-027` | Politics | `politics.result` | Resolution alert | `SCR-021` | `JRN-G` | Reachable (post-result) |
| `SCR-028` | Politics | `politics.crisis` | Banner; warning | `SCR-021` | `JRN-G` | Reachable (CRISIS/RECOVERY) |
| `SCR-029` | Economy | `economy.treasury` | Primary nav | — | `JRN-D` | Reachable |
| `SCR-030` | Economy | `economy.budget` | Treasury | `SCR-029` | `JRN-D` | Reachable |
| `SCR-031` | Economy | `economy.reports` | Treasury | `SCR-029` | `JRN-D` | Reachable |
| `SCR-032` | Economy | `economy.production` | Economy nav | `SCR-029` | `JRN-D` | Reachable |
| `SCR-033` | Economy | `economy.resources` | Treasury; production | `SCR-029` | `JRN-D` | Reachable |
| `SCR-034` | Economy | `economy.power` | Economy nav | `SCR-029` | `JRN-D` | Reachable |
| `SCR-035` | Economy | `economy.offers` | Economy nav; inbox | `SCR-029` | `JRN-E` | Reachable |
| `SCR-036` | Economy | `economy.offer-compose` | Directed inbox | `SCR-035` | `JRN-E` | Reachable |
| `SCR-037` | Economy | `economy.offer-detail` | Inbox; history | `SCR-035` | `JRN-E` | Reachable (parties) |
| `SCR-038` | Economy | `economy.trade-board` | — (gate) | — | — | **Absent** (`BLK-GT`) |
| `SCR-039` | Economy | `economy.listing` | — (gate) | — | — | **Absent** (`BLK-GT`) |
| `SCR-040` | Economy | `economy.trade-history` | Economy nav | `SCR-029` | `JRN-E` | Reachable |
| `SCR-041` | Cities | `cities.overview` | Primary nav | — | `JRN-F` | Reachable |
| `SCR-042` | Cities | `cities.city` | Overview row | `SCR-041` | `JRN-F` | Reachable (ownership) |
| `SCR-043` | Cities | `cities.construction` | City detail | `SCR-042` | `JRN-F` | Reachable |
| `SCR-044` | Cities | `cities.chains` | Cities nav | `SCR-041` | `JRN-F` | Reachable |
| `SCR-045` | Cities | `cities.research` | Cities nav | `SCR-041` | `JRN-F` | Reachable |
| `SCR-046` | Cities | `cities.found` | Overview CTA | `SCR-041` | `JRN-F` | Reachable (gate) |
| `SCR-047` | Foreign | `foreign.diplomacy` | Primary nav | — | `JRN-H` | Reachable |
| `SCR-048` | Foreign | `foreign.pair` | Overview; profile | `SCR-047` | `JRN-H` | Reachable |
| `SCR-049` | Foreign | `foreign.proposal` | Pair screen | `SCR-048` | `JRN-H` | Reachable |
| `SCR-050` | Foreign | `foreign.agreement` | Overview; history | `SCR-047` | `JRN-H` | Reachable |
| `SCR-051` | Foreign | `foreign.publication` | Agreement detail | `SCR-050` | `JRN-H` | Reachable |
| `SCR-052` | Foreign | `foreign.history` | Pair/agreement | `SCR-048` | `JRN-H` | Reachable |
| `SCR-053` | Foreign | `foreign.alliance` | Overview; network | `SCR-047` | `JRN-H` | Reachable |
| `SCR-054` | Foreign | `foreign.alliance-members` | Alliance home | `SCR-053` | `JRN-H` | Reachable (member) |
| `SCR-055` | Foreign | `foreign.alliance-governance` | Alliance home | `SCR-053` | `JRN-H` | Reachable (role) |
| `SCR-056` | Foreign | `foreign.alliance-tax` | Governance | `SCR-055` | `JRN-H` | Reachable (tax role) |
| `SCR-057` | Foreign | `foreign.alliance-finance` | Alliance home | `SCR-053` | `JRN-H` | Reachable (member) |
| `SCR-058` | Foreign | `foreign.alliance-diplomacy` | Alliance home | `SCR-053` | `JRN-H` | Reachable (role) |
| `SCR-059` | War | `war.overview` | Primary nav | — | `JRN-I` | Reachable |
| `SCR-060` | War | `war.forces` | Overview | `SCR-059` | `JRN-I` | Reachable |
| `SCR-061` | War | `war.board` | Overview | `SCR-059` | `JRN-I` | Reachable (owner only) |
| `SCR-062` | War | `war.conflicts` | Overview; World alias | `SCR-059` | `JRN-I` (public) | Reachable |
| `SCR-063` | War | `war.detail` | Conflicts ledger | `SCR-062` | `JRN-I` | Reachable |
| `SCR-064` | War | `war.battle` | Board; war detail | `SCR-063` | `JRN-I` | Reachable (participant) |
| `SCR-065` | War | `war.reports` | Board; war detail | `SCR-061` | `JRN-I` | Reachable (owner) |
| `SCR-066` | War | `war.archive` | Overview | `SCR-059` | `JRN-I` (support) | Reachable |
| `SCR-067` | War | `war.settlement` | War detail; board | `SCR-063` | `JRN-I` | Reachable (parties) |
| `SCR-068` | War | `war.intelligence` | — (no route) | — | — | **Absent** (`BLK-INTEL`) |
| `SCR-069` | World | `world.events` | Primary nav | — | `JRN-J` | Reachable |
| `SCR-070` | World | `world.event` | Events list | `SCR-069` | `JRN-J` | Reachable |
| `SCR-071` | World | `world.objectives` | World nav | `SCR-069` | `JRN-J` | Reachable |
| `SCR-072` | World | `world.standings` | World nav | `SCR-069` | `JRN-J` | Reachable |
| `SCR-073` | World | `world.achievements` | World nav | `SCR-069` | `JRN-J` | Reachable |
| `SCR-074` | World | `world.progress` | World nav | `SCR-069` | `JRN-J` | Reachable |
| `SCR-075` | World | `world.rewards` | World nav | `SCR-069` | `JRN-J` | Reachable |
| `SCR-076` | World | `world.chronicle` | World nav | `SCR-069` | `JRN-J` | Reachable |
| `SCR-077` | World | `world.health` | — (gate) | — | — | **Absent** (`PROV-K5`) |
| `SCR-078` | World | `world.guide` | Footer; help | Prior page | — (support) | Reachable |
| `SCR-079` | Account | `account.privacy` | Account home | `SCR-011` | `JRN-L` | Reachable |
| `SCR-080` | Account | `account.security` | Account home | `SCR-011` | `JRN-L` | Reachable |
| `SCR-081` | Account | `account.report` | Footer; profile | Prior page | `JRN-K` | Reachable |
| `SCR-082` | Account | `account.report-status` | Report receipt | `SCR-081` | `JRN-K` | Reachable (reporter) |
| `SCR-083` | Account | `account.appeal` | Decision notice | `SCR-084` | `JRN-K` | Reachable (always) |
| `SCR-084` | Account | `account.restrictions` | Account home; notice | `SCR-011` | `JRN-K` | Reachable |
| `SCR-085` | Account | `account.data` | Privacy centre | `SCR-079` | `JRN-L` | Reachable |
| `SCR-086` | Account | `account.review` | Restriction notice | `SCR-084` | `JRN-K` | Reachable |
| `SCR-087` | Account | `account.support` | Footer | Prior page | `JRN-K` | Reachable |
| `SCR-088` | World | `world.changes` | Footer; Home alias | Prior page | — (support) | Reachable |
| `SCR-089` | Home | `home.protection` | Shell badge; block moments | `SCR-013` | `JRN-K` | Reachable |
| `SCR-090` | Account | `account.reroll` | Account home | `SCR-011` | `JRN-L` | Reachable (block conditions) |
| `SCR-091` | Admin | `admin.console` | Role-gated entry | — | `JRN-M` | Reachable (ADM) |
| `SCR-092` | Admin | `admin.moderation` | Console | `SCR-091` | `JRN-M` | Reachable (role) |
| `SCR-093` | Admin | `admin.case` | Queue | `SCR-092` | `JRN-M` | Reachable (assigned) |
| `SCR-094` | Admin | `admin.sanctions` | Case | `SCR-093` | `JRN-M` | Reachable (two-person) |
| `SCR-095` | Admin | `admin.network` | Console | `SCR-091` | `JRN-M` | Reachable (role) |
| `SCR-096` | Admin | `admin.audit` | Console | `SCR-091` | `JRN-M` | Reachable (scoped) |
| `SCR-097` | Admin | `admin.turns` | Console | `SCR-091` | `JRN-M` | Reachable (R-OPS) |
| `SCR-098` | Admin | `admin.data` | Console | `SCR-091` | `JRN-M` | Reachable (role) |
| `SCR-099` | Admin | `admin.announce` | Console | `SCR-091` | `JRN-M` | Reachable (authorized) |
| `SCR-100` | Admin | `admin.roles` | Console | `SCR-091` | `JRN-M` | Reachable (R-SEC) |

**Reachability verdict.** 95 screens reachable by a legitimate path; 4 conditional/provisional screens correctly absent (`SCR-020`, `SCR-038`, `SCR-039`, `SCR-077`); `SCR-068` provisional and unlinked. No accidental dead end exists: every reachable screen has a return path, and every task screen has a cancel/return path specified in its flow. No screen is reachable only through an overlay. The four dual-parent aliases (`SCR-010/017/062/088`) share one route each; no duplicate copy exists.

---

## 11. Matrix E — Journey-to-integration traceability

| JRN | Name | Screens | Flows | Systems | Contracts | Tests | Completion condition | Status |
|---|---|---|---|---|---|---|---|---|
| `JRN-A` | First-time player | `SCR-001`…`SCR-009`, `SCR-013` | `FLOW-001`…`004` | ACC, TURN | `UIX-01`…`04` | `UAT-F-001`, `UAT-E-001` | Verified account owns exactly one nation; onboarding recorded once; digest home | Complete spec |
| `JRN-B` | Returning player | `SCR-003`, `SCR-013`…`019` | `FLOW-002`, `005`, `006`, `033` | TURN, WORLD | `UIX-05`, `UIX-06` | `UAT-F-002/003/026` | Player sees what changed, open decisions and next action; no attendance reward | Complete spec |
| `JRN-C` | National management | `SCR-013`, `SCR-015`, `SCR-016`, section roots | `FLOW-005`, `006` | TURN, ECON | `UIX-05`…`07` | `UAT-F-003` | Overview reflects new state at new as-of turn | Complete spec |
| `JRN-D` | Economy and treasury | `SCR-029`…`034` | `FLOW-009`, `010` | ECON | `UIX-08`…`10` | `UAT-F-006/007` | Policy/order committed with exact cost and phase; balances agree | Complete spec |
| `JRN-E` | Trade | `SCR-035`…`037`, `040` | `FLOW-011`…`013` | MKT, ECON | `UIX-15`, `UIX-16` | `UAT-F-008`…`010` | Offer/acceptance settles atomically or fails with named factor | Complete spec |
| `JRN-F` | Cities and research | `SCR-041`…`046` | `FLOW-014`…`016` | CITY, ECON | `UIX-11`…`13` | `UAT-F-011`…`013` | Order/research recorded against one slot/project; preview accurate | Complete spec |
| `JRN-G` | Politics | `SCR-021`…`028` | `FLOW-007`, `008` | POL, ECON | `UIX-14` | `UAT-F-004/005` | Policy or campaign action recorded once with cooldown/charge shown | Complete spec |
| `JRN-H` | Diplomacy and alliances | `SCR-047`…`058` | `FLOW-017`…`020` | DIP, ALL, ECON | `UIX-17`…`20` | `UAT-F-014`…`017` | Proposal accepted/activated or alliance change recorded; no delegation | Complete spec |
| `JRN-I` | Warfare | `SCR-059`…`067` | `FLOW-021`…`024` | WAR, ECON | `UIX-21`…`23` | `UAT-F-018`…`021` | Operation/declaration/settlement/surrender recorded with OP and phase | Complete spec |
| `JRN-J` | World and progression | `SCR-018`, `SCR-069`…`076` | `FLOW-025`, `026` | WORLD | `UIX-24`, `UIX-25` | `UAT-F-022` | Objective dismiss/claim recorded; standings show denominator/window | Complete spec |
| `JRN-K` | Notifications and protection | `SCR-019`, `SCR-081`…`087` | `FLOW-027`…`029` | FP, TURN | `UIX-06`, `UIX-26` | `UAT-F-023` | Report acknowledged with case reference; appeal reachable | Complete spec |
| `JRN-L` | Account management | `SCR-011`, `012`, `080`, `090` | `FLOW-030`, `031` | ACC | `UIX-27`, `UIX-03` | `UAT-F-024` | Closure cooling/reroll recorded exactly; no shield | Complete spec |
| `JRN-M` | Administrative | `SCR-091`…`100` | `FLOW-032` | ADMIN, FP, TURN | `UIX-28`, `UIX-29` | `UAT-F-025` | Decision within role/tier; audit row appended; no SEC leak | Complete spec |

**Journey verdict.** All 13 journeys have a start condition, entry screen, sequence, permission checks, failure handling, completion state, recovery and accessibility (13C template A–J). No journey depends on an absent screen. `SCR-020/038/039/068/077` appear in no active journey.

---

## 12. Matrix F — Flow-to-system/contract traceability

| FLOW | Initiating UI action | System operation | Validation | Permission | Contract | Failure reference | Idempotency | Test |
|---|---|---|---|---|---|---|---|---|
| `FLOW-001` | Submit registration | Create `UNVERIFIED` account; verify e-mail | Pair, policy, terms, verification | Public | `UIX-02` | `ERR-08/09/05`; `ST-08/11/13` | One intent per submit (`DUP-01`) | `UAT-F-001` |
| `FLOW-002` | Submit login | Authenticate; establish session; route by state | Credentials, account state | Public | `UIX-01` | `ERR-04/05`; neutral message | Single-flight | `UAT-F-002` |
| `FLOW-003` | Confirm nation creation | Create exactly one nation at founding turn | Name/short name, eligibility, creation pause | Verified account | `UIX-03` | `ERR-08/11/13`; `AC-03` | One nation per account | `UAT-F-001` |
| `FLOW-004` | Open/complete onboarding step | Record tutorial completion once | Tutorial availability | Auth | `UIX-04` | `ST-11`; no bypass | Completion recorded once | `UAT-E-001` |
| `FLOW-005` | Open digest | Read settled events, pending totals, due boundary | Read permission | Auth | `UIX-06` | `ERR-03/18` | Read-only | `UAT-F-003` |
| `FLOW-006` | Open inbox row | Read pending object; deep link | Row permission | Auth | `UIX-06` | `ERR-06/07/12` | Read-only | `UAT-F-003` |
| `FLOW-007` | Confirm policy change | Record policy at resolution turn | Effect, cost, cooldown | Auth | `UIX-14` | `ERR-13/14`; `ST-11` | One per axis per 12 turns | `UAT-F-004` |
| `FLOW-008` | Submit campaign action | Charge once; record action | Type, cost, limit | Auth (ELECTORAL) | `UIX-14` | `ERR-13/14/16` | Charge once; no cancel | `UAT-F-005` |
| `FLOW-009` | Save standing policy | Set recurring production policy | Affordability/capacity preview | Auth | `UIX-09` | `ERR-08/13/14` | Last-write-wins setting | `UAT-F-006` |
| `FLOW-010` | Submit manual order | Reserve money/inputs/capacity; execute atomically | Overbooking, stock, power | Auth | `UIX-09` | `ERR-14/17` | Reservation until settlement | `UAT-F-007` |
| `FLOW-011` | Submit directed offer | Create chain/revision; reserve nothing | Lines, balances, expiry, rate limit | Auth | `UIX-15` | `ERR-08/14/15/16` | One live revision per pair | `UAT-F-008` |
| `FLOW-012` | Accept offer | Re-read both sides; reserve; settle atomically at P4 | Both-side validation | Party | `UIX-15` | `ERR-11/14/17` | One settlement per revision | `UAT-F-009` |
| `FLOW-013` | Counter/decline/cancel | Create revision or terminate | Lifecycle state | Party | `UIX-15` | `ERR-11/12/16` | Revision count limit | `UAT-F-010` |
| `FLOW-014` | Confirm construction | Claim city slot; schedule build | Preview, DC, cost, one slot | Auth | `UIX-11` | `ERR-13/14/16` | One action per city per turn | `UAT-F-011` |
| `FLOW-015` | Confirm city founding | Create city; charge crowns/steel | Eligibility, expansion slot | Auth | `UIX-12` | `ERR-13/14` | One city per confirmation | `UAT-F-012` |
| `FLOW-016` | Confirm research start | Start one active project | RP/crown cost, prerequisite | Auth | `UIX-13` | `ERR-13/14/16` | One active project | `UAT-F-013` |
| `FLOW-017` | Submit/counter/withdraw proposal | Record ordered proposal | Ten confirmation fields, parties-only | Auth | `UIX-17` | `ERR-08/11/12` | One live proposal per direction | `UAT-F-014` |
| `FLOW-018` | Accept proposal | Record acceptance; activate at boundary | State, counterparty, terms | Party | `UIX-17` | `ERR-11/12` | One acceptance | `UAT-F-015` |
| `FLOW-019` | Respond to application | Admit/decline/withdraw | Role permission, status | Member/Role | `UIX-18` | `ERR-06/11` | One outcome per application | `UAT-F-016` |
| `FLOW-020` | Save tax bracket | Record bracket/rates/policy version | Integer bp 0–10,000; role | Tax role | `UIX-19` | `ERR-08/06/13` | Versioned policy; effective turn | `UAT-F-017` |
| `FLOW-021` | Submit military operation | Reserve OP; queue operation | Owner, OP, resources, block | Owner | `UIX-21` | `ERR-13/14`; `WRF` | Reservation at acceptance | `UAT-F-018` |
| `FLOW-022` | Declare war | Create campaign; publish record | 2 OP, 500 crowns, slots, NAP/Alliance checks | Owner | `UIX-21` | `ERR-13/14`; `WRF` | One campaign object | `UAT-F-019` |
| `FLOW-023` | Propose/accept settlement | Record one live settlement | Terms, duration, one-live | Party | `UIX-22` | `ERR-11/12/16` | One live settlement | `UAT-F-020` |
| `FLOW-024` | Confirm surrender | End campaign as limited victory | Owner; confirm | Owner | `UIX-22` | `ERR-04/11` | One surrender | `UAT-F-021` |
| `FLOW-025` | Accept/dismiss objective | Record optional acceptance/dismissal | No penalty; no presence requirement | Auth | `UIX-24` | `ERR-11/12` | One state per objective | `UAT-F-022` |
| `FLOW-026` | Claim deferred reward | Read/claim where permitted | Claim state | Auth | `UIX-25` | `ERR-11/12/16` | One claim per grant | `UAT-F-022` |
| `FLOW-027` | Open alert | Deep-link to object; render absent/denied state | Visibility | Auth | `UIX-06` | `ERR-06/07/12` | Read-only | `UAT-F-003` |
| `FLOW-028` | Submit report | Create report and case reference | MOD-002 fields | Auth | `UIX-26` | `ERR-03/08`; retryable | One case per submission | `UAT-F-023` |
| `FLOW-029` | Submit appeal | Create appeal; preserve route | Grounds, eligibility | Auth | `UIX-26` | `ERR-03/13` | One appeal per action | `UAT-F-023` |
| `FLOW-030` | Request/cancel closure | Start cooling; cancel during cooling | Cooling, retention | Auth | `UIX-27` | `ERR-11/13` | One closure request | `UAT-F-024` |
| `FLOW-031` | Reroll exact phrase | Reset nation; replace immediately | Re-auth, exact name/phrase, blocks | Auth | `UIX-03` | `ERR-06/08/13` | One reroll per confirmation | `UAT-F-024` |
| `FLOW-032` | Decide moderation action | Append decision; apply within tier | Role, tier, two-person | Role | `UIX-28` | `ERR-06/13`; `FR` codes | One decision per case step | `UAT-F-025` |
| `FLOW-033` | Reconnect/re-read | Reconcile stale/uncertain state | As-of, conflict | Auth | `UIX-05/06` | `ERR-01/02/18/19` | No auto-repeat | `UAT-F-026` |

**Flow verdict.** Every flow names a real system operation, a validation basis, a permission, a contract, a failure reference and a duplicate/uncertainty rule. No flow promises an outcome the system does not permit. No `FLOW-` entry exists for Global Trade, correctly: the board and listing screens are blocked and have no interaction flow.

---

## 13. Matrix G — Component and overlay traceability

**States** follow the 13C component state map; `interaction` names the primary interactive rule. Every row names at least one owning screen and one acceptance test. `Global` components serve all authenticated screens; the screen column names distinctive owners.

| ID | Name | Family | Owning screens | States | Interaction | REQ | Test | Status |
|---|---|---|---|---|---|---|---|---|
| `UI-CMP-001` | Global shell | Shell | All | default/loading/error/stale/denied | persistent shell; never full-page spinner | `REQ-970` | `UAT-I-001` | SPECIFIED |
| `UI-CMP-002` | Primary nav | Shell | All authenticated | default/hover/focus/active/disabled/overflow | eight sections; no admin entry | `REQ-971` | `UAT-F-001` | SPECIFIED |
| `UI-CMP-003` | Secondary nav | Shell | Section screens | default/active/disabled | same-object tabs only | `REQ-972` | `UAT-A-001` | SPECIFIED |
| `UI-CMP-004` | Page heading | Shell | All | default | title + focus target | `REQ-1013/1164` | `UAT-A-002` | SPECIFIED |
| `UI-CMP-005` | Breadcrumb | Shell | Depth ≥ 2 | default/denied | every crumb links; no denied return | `REQ-973` | `UAT-F-003` | SPECIFIED |
| `UI-CMP-006` | Account/nation context | Shell | All authenticated | default/stale | identity strip; visibility-filtered | `REQ-974` | `UAT-P-001` | SPECIFIED |
| `UI-CMP-007` | Turn indicator | Shell | All authenticated | default/pending/offline/interrupted | turn + UTC boundary; polite live region | `REQ-975/1007` | `UAT-I-002` | SPECIFIED |
| `UI-CMP-008` | Notification indicator | Shell | All authenticated | default/unread/non-opt-out | counts from existing events only | `REQ-976` | `UAT-E-008` | SPECIFIED |
| `UI-CMP-009` | Contextual navigation | Shell | Object/detail/task | default/denied/hidden | related-object links | `REQ-977` | `UAT-F-003` | SPECIFIED |
| `UI-CMP-010` | Admin entry/nav | Shell | `SCR-091`…`100` | default/denied | separate Admin root only | `REQ-978/1037` | `UAT-P-002` | SPECIFIED |
| `UI-CMP-011` | Footer/help | Shell | All | default | help, support, report, terms, changes | `REQ-979` | `UAT-E-009` | SPECIFIED |
| `UI-CMP-012` | Statistic card | Info | Dashboards | default/loading/partial/error | number type + unit + as-of | `REQ-980/1062` | `UAT-E-003` | SPECIFIED |
| `UI-CMP-013` | Metric group | Info | `SCR-013/015/029/041/059/072` | default/partial | equal treatment; no merged types | `REQ-981` | `UAT-E-003` | SPECIFIED |
| `UI-CMP-014` | Financial summary | Info | `SCR-029/030/031/037/057` | default/forecast/error | opening→closing; capex/opex | `REQ-982` | `UAT-X-001` | SPECIFIED |
| `UI-CMP-015` | Resource balance | Info | Balance surfaces | default/reserved/empty | single-resource triple | `REQ-983` | `UAT-X-001` | SPECIFIED |
| `UI-CMP-016` | Progress indicator | Info | `SCR-016/025/043/045/074` | pending/success/warning/error/indeterminate | names what progresses | `REQ-984` | `UAT-E-004` | SPECIFIED |
| `UI-CMP-017` | Status banner | Info | Political/state screens | six states + warning/error | tone+glyph+text; cause/end turn | `REQ-985` | `UAT-E-005` | SPECIFIED |
| `UI-CMP-018` | Warning panel | Info | Warning surfaces | default/critical | condition/consequence/end/actions | `REQ-986` | `UAT-E-005` | SPECIFIED |
| `UI-CMP-019` | Information panel | Info | All read surfaces | default/provisional/forecast/suppressed | rule anchor | `REQ-987` | `UAT-E-006` | SPECIFIED |
| `UI-CMP-020` | Historical record | Info | History surfaces | default/retained/restricted | as-of + retention + class | `REQ-988/1008` | `UAT-E-010` | SPECIFIED |
| `UI-CMP-021` | Timeline | Info | Timeline surfaces | pending/completed | turn order; no implied outcome | `REQ-989` | `UAT-F-014` | SPECIFIED |
| `UI-CMP-022` | Data table | Info | Table screens | default/loading/empty/error | semantic headers; exact pagination | `REQ-990/1083` | `UAT-A-003` | SPECIFIED |
| `UI-CMP-023` | Filter row | Info | Table screens | default/active/invalid | active filters disclosed | `REQ-991` | `UAT-A-003` | SPECIFIED |
| `UI-CMP-024` | Pagination | Info | Paginated lists | default/end | exact bounds; preserve sort | `REQ-992` | `UAT-A-003` | SPECIFIED |
| `UI-CMP-025` | Saved view | Info | List screens | default/dirty/invalid | per-user; never widens visibility | `REQ-993` | `UAT-E-011` | SPECIFIED |
| `UI-CMP-026` | Search/jump | Info | Shell; object screens | default/loading/no-result/denied | jump-to-object/screen only | `REQ-994` | `UAT-E-011` | SPECIFIED |
| `UI-CMP-027` | Object link | Info | All object citations | default/retired/denied | canonical route | `REQ-995` | `UAT-F-003` | SPECIFIED |
| `UI-CMP-028` | Object peek | Info | Lists everywhere | default/denied/suppressed | visible fields only | `REQ-996` | `UAT-P-003` | SPECIFIED |
| `UI-CMP-029` | Detail section | Info | Object pages | default/collapsed | page-reachable equivalent | `REQ-997` | `UAT-A-004` | SPECIFIED |
| `UI-CMP-030` | Comparison panel | Info | `SCR-015/022/023/042/063/072` | default/suppressed | legal inputs; facts not verdicts | `REQ-998` | `UAT-X-002` | SPECIFIED |
| `UI-CMP-031` | Treasury summary | Econ | `SCR-029/030/031/057` | default/pending | available/reserved/position | `REQ-999` | `UAT-X-001` | SPECIFIED |
| `UI-CMP-032` | Income/expenditure | Econ | `SCR-029/030/031` | default/forecast | recurring vs one-time | `REQ-1000` | `UAT-X-001` | SPECIFIED |
| `UI-CMP-033` | Total/reserved/available | Econ | All balance screens | default/pending/error | three figures together | `REQ-1001/1065` | `UAT-X-001` | SPECIFIED |
| `UI-CMP-034` | Capacity bar | Econ | Capacity screens | default/full/derated/unmaintained | capacity ≠ resource | `REQ-1002` | `UAT-X-003` | SPECIFIED |
| `UI-CMP-035` | Production chain | Econ | `SCR-032/044` | default/blocked/unmaintained | inputs/output/cost/maintenance/power | `REQ-1004` | `UAT-X-003` | SPECIFIED |
| `UI-CMP-036` | Construction item | Econ | `SCR-042/043` | default/pending/cancelled | slot/cost/availability | `REQ-1005` | `UAT-F-011` | SPECIFIED |
| `UI-CMP-037` | Research card | Econ | `SCR-045` | locked/available/in-progress/complete | one active project | `REQ-1006` | `UAT-F-013` | SPECIFIED |
| `UI-CMP-038` | Approval/stability | Political | `SCR-021/023/028` | default/cause-chain | six supports; no invented bands | `REQ-1009` | `UAT-X-004` | SPECIFIED |
| `UI-CMP-039` | Political banner | Political | `SCR-021`…`028`, block surfaces | six states | cause/end/locked/not locked | `REQ-1010` | `UAT-E-005` | SPECIFIED |
| `UI-CMP-040` | Policy control | Political | `SCR-024` | default/disabled/cooldown | effect/cost/cooldown on control | `REQ-1011` | `UAT-F-004` | SPECIFIED |
| `UI-CMP-041` | Election date | Political | `SCR-025/027/028` | on-time/delayed/interrupted | anchor `campaign_open_turn` | `REQ-1012` | `UAT-F-005` | SPECIFIED |
| `UI-CMP-042` | Campaign control | Political | `SCR-026` | default/disabled/charged | exactly three types; charge once | `REQ-1018` | `UAT-F-005` | SPECIFIED |
| `UI-CMP-043` | Relationship indicator | Dip | Diplomacy surfaces | four postures + blocked | glyph+text; no score | `REQ-1019` | `UAT-F-014` | SPECIFIED |
| `UI-CMP-044` | Directional presentation | Dip | `SCR-047/048` | per-direction | both sides; embargo distinct | `REQ-1020/1067` | `UAT-F-014` | SPECIFIED |
| `UI-CMP-045` | Treaty status | Dip | `SCR-047/050/051/052/058` | pending/active/expired/terminated | exact type and lifecycle | `REQ-1021` | `UAT-F-015` | SPECIFIED |
| `UI-CMP-046` | Proposal summary | Dip | `SCR-014/047/049/050` | pending/accepted/withdrawn | parties-only pending | `REQ-1022` | `UAT-F-014` | SPECIFIED |
| `UI-CMP-047` | Negotiation panel | Dip | `SCR-049/067` | default/confirming | ten fields; cancel non-destructive | `REQ-1023` | `UAT-F-015` | SPECIFIED |
| `UI-CMP-048` | Publication status | Dip | `SCR-050/051/058` | private/public/record-only | no pending terms to third party | `REQ-1024/1068` | `UAT-F-015` | SPECIFIED |
| `UI-CMP-049` | Alliance membership row | Alliance | `SCR-053/054/055` | member/applicant/non-covered | role only within disclosure | `REQ-1025` | `UAT-F-016` | SPECIFIED |
| `UI-CMP-050` | Applicant status | Alliance | `SCR-054` | pending/admitted/declined/expired/withdrawn | admin-only; in-product | `REQ-1026` | `UAT-F-016` | SPECIFIED |
| `UI-CMP-051` | Alliance financial summary | Alliance | `SCR-056/057` | four ARL categories | `AVAILABLE = RECEIVED − RESERVED − EXPENDED` | `REQ-1027` | `UAT-X-005` | SPECIFIED |
| `UI-CMP-052` | Alliance receipt | Alliance | `SCR-056/057` | immutable | donor/source/asset/turn/ref | `REQ-1028` | `UAT-X-005` | SPECIFIED |
| `UI-CMP-053` | Restriction explanation | Alliance/FP | `SCR-048/055/058/084/086` | reason classes | no accusation/threshold/data | `REQ-1029` | `UAT-P-004` | SPECIFIED |
| `UI-CMP-054` | War summary | War | `SCR-059/061/062/063` | campaign states | public facts only | `REQ-1030` | `UAT-F-018` | SPECIFIED |
| `UI-CMP-055` | War status strip | War | `SCR-061/063` | lifecycle/protection/settlement | WAR-125 vocabulary | `REQ-1031` | `UAT-F-018` | SPECIFIED |
| `UI-CMP-056` | Operations summary | War | `SCR-061` | reservation/execution/released/failed | exact failure factor | `REQ-1032` | `UAT-F-018` | SPECIFIED |
| `UI-CMP-057` | OP balance/reservation | War | `SCR-059/061` | default/reserved/capped | one national pool only | `REQ-1033` | `UAT-F-018` | SPECIFIED |
| `UI-CMP-058` | Threat/odds band | War | `SCR-061/063` | four bands | band only; no ratio | `REQ-1034` | `UAT-P-005` | SPECIFIED |
| `UI-CMP-059` | Battle record | War | `SCR-061/064/065` | participant/public | WAR-088 fields; filtered | `REQ-1035` | `UAT-P-006` | SPECIFIED |
| `UI-CMP-060` | Battle outcome | War | `SCR-064/065` | win/loss/stalemate/interrupted/voided | no unproduced result | `REQ-1036` | `UAT-F-020` | SPECIFIED |
| `UI-CMP-061` | Military history | War | `SCR-066` | retained/restricted | class-P; filters | `REQ-1038` | `UAT-E-010` | SPECIFIED |
| `UI-CMP-062` | Nation-owner controls | War | `SCR-061` | default/disabled/blocked | OP cost/reservation/confirmation | `REQ-1039` | `UAT-P-007` | SPECIFIED |
| `UI-CMP-063` | Event card | World | `SCR-013/069/070` | registered states | no invented event | `REQ-1040` | `UAT-F-022` | SPECIFIED |
| `UI-CMP-064` | Event consequence | World | `SCR-070` | cause/effect | registered effect only | `REQ-1041/1071` | `UAT-F-022` | SPECIFIED |
| `UI-CMP-065` | Objective card | World | `SCR-009/071` | categories/progress | optional; penalty-free | `REQ-1042` | `UAT-F-022` | SPECIFIED |
| `UI-CMP-066` | Achievement card | World | `SCR-073/075` | earned/locked/deferred | six classes | `REQ-1043` | `UAT-F-022` | SPECIFIED |
| `UI-CMP-067` | Ranking row | World | `SCR-072/010` | eligible/ineligible/suppressed | denominator stated | `REQ-1044` | `UAT-X-006` | SPECIFIED |
| `UI-CMP-068` | Ranking summary | World | `SCR-072` | computed/published | denominator/window/turns | `REQ-1045/1069` | `UAT-X-006` | SPECIFIED |
| `UI-CMP-069` | Notification item | World | `SCR-013/019/014` | read/unread/mutable | source event; no paraphrase | `REQ-1046/1182` | `UAT-E-008` | SPECIFIED |
| `UI-CMP-070` | Pending-action item | World | `SCR-014` | pending/due/deferred | act/defer/cancel per rule | `REQ-1047` | `UAT-F-003` | SPECIFIED |
| `UI-CMP-071` | Chronicle record | World | `SCR-017/070/075/076` | public/restricted | turn/class/retention | `REQ-1048` | `UAT-E-010` | SPECIFIED |
| `UI-CMP-072` | Suppression indicator | World | Aggregate surfaces | suppressed/insufficient | named state, never zero | `REQ-1056/1066/1152` | `UAT-E-012` | SPECIFIED |
| `UI-CMP-073` | Historical reward record | World | `SCR-075` | granted/deferred/voided/corrected | deferred never granted | `REQ-1072` | `UAT-F-022` | SPECIFIED |
| `UI-CMP-074` | Text input | Form | Forms | default/focus/error/disabled | label + text error | `REQ-1086` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-075` | Numeric input | Form | Forms | default/focus/error | units and bounds | `REQ-1086` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-076` | Select | Form | Forms | default/error | programmatic label | `REQ-1086` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-077` | Multi-select | Form | Forms | default/error | line limits | `REQ-1086` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-078` | Checkbox | Form | Forms | checked/unchecked/error | terms and consent | `REQ-1086` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-079` | Radio | Form | Forms | selected/error | posture/emblems | `REQ-1086` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-080` | Toggle | Form | Settings | on/off/disabled | setting only, never permission | `REQ-1088` | `UAT-P-008` | SPECIFIED |
| `UI-CMP-081` | Date/turn selector | Form | Forms | default/error | turns and UTC | `REQ-1007` | `UAT-E-013` | SPECIFIED |
| `UI-CMP-082` | Search field | Form | Search surfaces | loading/no-result/denied | scope announced | `REQ-1003` | `UAT-E-011` | SPECIFIED |
| `UI-CMP-083` | Form field group | Form | Forms | default/error | grouped semantics | `REQ-1049` | `UAT-A-005` | SPECIFIED |
| `UI-CMP-084` | Validation message | Form | Forms | error/summary | field-linked text | `REQ-1142/1165` | `UAT-A-006` | SPECIFIED |
| `UI-CMP-085` | Primary action | Form | Committing screens | default/loading/disabled | single-flight | `REQ-1157` | `UAT-C-001` | SPECIFIED |
| `UI-CMP-086` | Secondary action | Form | Task screens | default/disabled | non-destructive cancel | `REQ-1148` | `UAT-E-014` | SPECIFIED |
| `UI-CMP-087` | Destructive action | Form | Destructive screens | default/disabled | separated; exact phrase | `REQ-1156` | `UAT-P-009` | SPECIFIED |
| `UI-CMP-088` | Confirmation panel | Form | Committing screens | default/confirming/expired | exact effect; confirm not preselected | `REQ-1155/1200` | `UAT-E-007` | SPECIFIED |
| `UI-CMP-089` | Disabled action | Form | All action screens | disabled+reason | reason before click | `REQ-1145` | `UAT-E-006` | SPECIFIED |
| `UI-CMP-090` | Exact-phrase field | Form | `SCR-090` | empty/match/error | never remembered | `REQ-959/1156` | `UAT-P-009` | SPECIFIED |
| `OVL-01` | Confirmation dialog | Overlay | All committing | open/cancelled/expired | focus trap; cancel-first | `REQ-1049/1163` | `UAT-A-007` | SPECIFIED |
| `OVL-02` | Destructive dialog | Overlay | `SCR-012/090/094/098` | open/cancelled | exact phrase; no bypass | `REQ-1156/1163` | `UAT-A-007` | SPECIFIED |
| `OVL-03` | Reason popover | Overlay | Disabled/denied | open/closed | reason class only | `REQ-1029/1145` | `UAT-E-006` | SPECIFIED |
| `OVL-04` | Definition/cause drawer | Overlay | Read surfaces | open/closed | page equivalent exists | `REQ-997` | `UAT-A-004` | SPECIFIED |
| `OVL-05` | Object peek card | Overlay | Object links | open/denied/retired | visible fields only | `REQ-996` | `UAT-P-003` | SPECIFIED |
| `OVL-06` | Boundary-effect notice | Overlay | Boundary/pending | open/closed | phase and effect | `REQ-1135/1192` | `UAT-C-008` | SPECIFIED |
| `OVL-07` | Suppression notice | Overlay | Aggregate surfaces | open/closed | explains suppression | `REQ-1056/1066` | `UAT-E-012` | SPECIFIED |
| `OVL-08` | Claim-vocabulary badge | Overlay | `SCR-082/093` | tiered | EVD-009 tiers only | `REQ-951/962` | `UAT-J-003` | SPECIFIED |

**Component verdict.** 98/98 identifiers mapped. No duplicate component specification was created. The two similar balance components (`UI-CMP-015` single-resource and `UI-CMP-033` composite triple) remain intentionally separate; screen usage follows the 13B rule.

---

## 14. Interaction-state consistency

| ST | State | 13B presentation | 13C interaction | Screen coverage | Component coverage | System consistency verdict |
|---|---|---|---|---|---|---|
| `ST-01` | Initial | Shell + empty region | no request completed | All | Shell, headings | Consistent |
| `ST-02` | Loading | skeleton + label | in-flight reads | All | 001, 012, 022 | Consistent |
| `ST-03` | Refreshing | as-of retained | newer read in flight | All data screens | 012, 019, 020 | Consistent |
| `ST-04` | Loaded | full screen | all permitted actions | All | all | Consistent |
| `ST-05` | Empty | explained absence | next step | Lists/dashboards | 019, 022 | Consistent |
| `ST-06` | Partial data | named missing part | unaffected sections usable | Data screens | 072, OVL-07 | Consistent |
| `ST-07` | Success | receipt | authoritative confirmation only | Committing | 088 | Consistent |
| `ST-08` | Validation error | field-linked text | blur/submit timing | Forms | 083/084 | Consistent |
| `ST-09` | Permission denied | reason class | no protected disclosure | Restricted | 053/089 | Consistent |
| `ST-10` | Unavailable | honest absence | no stub/teaser | Conditional/provisional | 019 | Consistent |
| `ST-11` | Blocked by rule | specific reason + rule | next eligible condition | Action screens | 089, OVL-03 | Consistent |
| `ST-12` | Expired | what survives | new request route | Expiry surfaces | 019/021 | Consistent |
| `ST-13` | Conflict | changed since load | re-read before resubmit | Committing/objects | 019 | Consistent |
| `ST-14` | Failed | failure anatomy | retry/support | All | 019/084 | Consistent |
| `ST-15` | Offline | read-only banner | writes disabled | All authenticated | 019, OVL-06 | Consistent |
| `ST-16` | Reconnecting | re-establishing | no duplicate action | Shell | 007 | Consistent |
| `ST-17` | Recovering | known/pending | no invented outcome | Boundary screens | 019, OVL-06 | Consistent |
| `ST-18` | Cancelled | nothing committed | safe return | Task screens | 086/088 | Consistent |

**Missing transitions.** None found beyond those the 13C transition diagram already covers. Accessibility interaction targets **WCAG 2.2 Level AA as design intent**; no conformance is claimed and no assistive-technology test has been run. Two consistency rulings are recorded for implementation: (1) `ST-03` must not blank a figure that `ST-06` will later label; the partial state supersedes refreshing only for the affected section (`REQ-1140`). (2) `ST-16` never auto-repeats a committing action (`REQ-1193`).

---

## 15. Requirement traceability

### 15.1 Matrix C (i) — Screen-level requirements (`REQ-870`…`REQ-969`)

The block is **totally mapped by construction**: `REQ-(869+n)` is the presentation requirement of `SCR-n`, its screen body carries fields A–K, and its acceptance test is `UAT-SCR-n`. The mapping is verified mechanically (validator check `13D-06`) and needs no duplicate rows. The 9 non-SPECIFIED rows retain their status: `REQ-889` PROVISIONAL, `REQ-946` PROVISIONAL, `REQ-907/908/937` BLOCKED. No screen is without a requirement or test.

### 15.2 Matrix C (ii) — Cross-cutting requirements (`REQ-970`…`REQ-1089`)

| REQ | UI owner | Primary test | Disposition |
|---|---|---|---|
| `REQ-970` | `UI-CMP-001` | `UAT-I-001` | Integrated |
| `REQ-971` | `UI-CMP-002` | `UAT-F-001` | Integrated |
| `REQ-972` | `UI-CMP-003` | `UAT-A-001` | Integrated |
| `REQ-973` | `UI-CMP-005` | `UAT-F-003` | Integrated |
| `REQ-974` | `UI-CMP-006` | `UAT-P-001` | Integrated |
| `REQ-975` | `UI-CMP-007` | `UAT-I-002` | Integrated |
| `REQ-976` | `UI-CMP-008` | `UAT-E-008` | Integrated |
| `REQ-977` | `UI-CMP-009` | `UAT-F-003` | Integrated |
| `REQ-978` | `UI-CMP-010` | `UAT-P-002` | Integrated |
| `REQ-979` | `UI-CMP-011` | `UAT-E-009` | Integrated |
| `REQ-980` | `UI-CMP-012` | `UAT-E-003` | Integrated |
| `REQ-981` | `UI-CMP-013` | `UAT-E-003` | Integrated |
| `REQ-982` | `UI-CMP-014` | `UAT-X-001` | Integrated |
| `REQ-983` | `UI-CMP-015` | `UAT-X-001` | Integrated |
| `REQ-984` | `UI-CMP-016` | `UAT-E-004` | Integrated |
| `REQ-985` | `UI-CMP-017` | `UAT-E-005` | Integrated |
| `REQ-986` | `UI-CMP-018` | `UAT-E-005` | Integrated |
| `REQ-987` | `UI-CMP-019` | `UAT-E-006` | Integrated |
| `REQ-988` | `UI-CMP-020` | `UAT-E-010` | Integrated |
| `REQ-989` | `UI-CMP-021` | `UAT-F-014` | Integrated |
| `REQ-990` | `UI-CMP-022` | `UAT-A-003` | Integrated |
| `REQ-991` | `UI-CMP-023` | `UAT-A-003` | Integrated |
| `REQ-992` | `UI-CMP-024` | `UAT-A-003` | Integrated |
| `REQ-993` | `UI-CMP-025` | `UAT-E-011` | Integrated |
| `REQ-994` | `UI-CMP-026` | `UAT-E-011` | Integrated; PROVISIONAL search scope preserved |
| `REQ-995` | `UI-CMP-027` | `UAT-F-003` | Integrated |
| `REQ-996` | `UI-CMP-028` | `UAT-P-003` | Integrated |
| `REQ-997` | `UI-CMP-029` | `UAT-A-004` | Integrated |
| `REQ-998` | `UI-CMP-030` | `UAT-X-002` | Integrated |
| `REQ-999` | `UI-CMP-031` | `UAT-X-001` | Integrated |
| `REQ-1000` | `UI-CMP-032` | `UAT-X-001` | Integrated |
| `REQ-1001` | `UI-CMP-033` | `UAT-X-001` | Integrated |
| `REQ-1002` | `UI-CMP-034` | `UAT-X-003` | Integrated |
| `REQ-1003` | `UI-CMP-082` | `UAT-E-011` | Integrated |
| `REQ-1004` | `UI-CMP-035` | `UAT-X-003` | Integrated |
| `REQ-1005` | `UI-CMP-036` | `UAT-F-011` | Integrated |
| `REQ-1006` | `UI-CMP-037` | `UAT-F-013` | Integrated |
| `REQ-1007` | `UI-CMP-007/041` | `UAT-E-013` | Integrated |
| `REQ-1008` | `UI-CMP-020` | `UAT-E-010` | Integrated |
| `REQ-1009` | `UI-CMP-038` | `UAT-X-004` | Integrated |
| `REQ-1010` | `UI-CMP-039` | `UAT-E-005` | Integrated |
| `REQ-1011` | `UI-CMP-040` | `UAT-F-004` | Integrated |
| `REQ-1012` | `UI-CMP-041` | `UAT-F-005` | Integrated |
| `REQ-1013` | `UI-CMP-002/004` | `UAT-A-002` | Integrated |
| `REQ-1014` | All components | `UAT-A-008` | Integrated |
| `REQ-1015` | All components | `UAT-R-001` | Integrated |
| `REQ-1016` | All components | `UAT-A-009` | Integrated |
| `REQ-1017` | All components | `UAT-A-010` | Integrated |
| `REQ-1018` | `UI-CMP-042` | `UAT-F-005` | Integrated |
| `REQ-1019` | `UI-CMP-043` | `UAT-F-014` | Integrated |
| `REQ-1020` | `UI-CMP-044` | `UAT-F-014` | Integrated |
| `REQ-1021` | `UI-CMP-045` | `UAT-F-015` | Integrated |
| `REQ-1022` | `UI-CMP-046` | `UAT-F-014` | Integrated |
| `REQ-1023` | `UI-CMP-047` | `UAT-F-015` | Integrated |
| `REQ-1024` | `UI-CMP-048` | `UAT-F-015` | Integrated |
| `REQ-1025` | `UI-CMP-049` | `UAT-F-016` | Integrated |
| `REQ-1026` | `UI-CMP-050` | `UAT-F-016` | Integrated |
| `REQ-1027` | `UI-CMP-051` | `UAT-X-005` | Integrated |
| `REQ-1028` | `UI-CMP-052` | `UAT-X-005` | Integrated |
| `REQ-1029` | `UI-CMP-053` | `UAT-P-004` | Integrated |
| `REQ-1030` | `UI-CMP-054` | `UAT-F-018` | Integrated |
| `REQ-1031` | `UI-CMP-055` | `UAT-F-018` | Integrated |
| `REQ-1032` | `UI-CMP-056` | `UAT-F-018` | Integrated |
| `REQ-1033` | `UI-CMP-057` | `UAT-F-018` | Integrated |
| `REQ-1034` | `UI-CMP-058` | `UAT-P-005` | Integrated |
| `REQ-1035` | `UI-CMP-059` | `UAT-P-006` | Integrated |
| `REQ-1036` | `UI-CMP-060` | `UAT-F-020` | Integrated |
| `REQ-1037` | `UI-CMP-010` | `UAT-P-002` | Integrated |
| `REQ-1038` | `UI-CMP-061` | `UAT-E-010` | Integrated |
| `REQ-1039` | `UI-CMP-062` | `UAT-P-007` | Integrated |
| `REQ-1040` | `UI-CMP-063` | `UAT-F-022` | Integrated |
| `REQ-1041` | `UI-CMP-064` | `UAT-F-022` | Integrated |
| `REQ-1042` | `UI-CMP-065` | `UAT-F-022` | Integrated |
| `REQ-1043` | `UI-CMP-066/073` | `UAT-F-022` | Integrated |
| `REQ-1044` | `UI-CMP-067` | `UAT-X-006` | Integrated |
| `REQ-1045` | `UI-CMP-068` | `UAT-X-006` | Integrated |
| `REQ-1046` | `UI-CMP-069` | `UAT-E-008` | Integrated |
| `REQ-1047` | `UI-CMP-070` | `UAT-F-003` | Integrated |
| `REQ-1048` | `UI-CMP-071` | `UAT-E-010` | Integrated |
| `REQ-1049` | Forms/overlays | `UAT-E-007` | Integrated |
| `REQ-1050` | All screens | `UAT-A-001` | Integrated |
| `REQ-1051` | All screens | `UAT-R-001` | Integrated |
| `REQ-1052` | All screens | `UAT-R-002` | Integrated |
| `REQ-1053` | `UI-CMP-022/033` | `UAT-R-003` | Integrated |
| `REQ-1054` | `UI-CMP-002/003` | `UAT-R-004` | Integrated |
| `REQ-1055` | Task screens | `UAT-R-005` | Integrated |
| `REQ-1056` | `UI-CMP-072`, `OVL-07` | `UAT-E-012` | Integrated |
| `REQ-1057` | All screens | `UAT-R-006` | Integrated; PROVISIONAL breakpoints preserved |
| `REQ-1058` | `UI-CMP-030/019` | `UAT-A-010` | Integrated |
| `REQ-1059` | `UI-CMP-030` | `UAT-A-010` | Integrated |
| `REQ-1060` | `UI-CMP-030` | `UAT-A-010` | Integrated |
| `REQ-1061` | `UI-CMP-072` | `UAT-E-012` | Integrated |
| `REQ-1062` | `UI-CMP-012` | `UAT-E-003` | Integrated |
| `REQ-1063` | `UI-CMP-012/013` | `UAT-E-003` | Integrated |
| `REQ-1064` | `UI-CMP-012/018` | `UAT-E-003` | Integrated |
| `REQ-1065` | `UI-CMP-033` | `UAT-X-001` | Integrated |
| `REQ-1066` | `UI-CMP-072`, `OVL-07` | `UAT-E-012` | Integrated |
| `REQ-1067` | `UI-CMP-044` | `UAT-F-014` | Integrated |
| `REQ-1068` | `UI-CMP-048/045` | `UAT-F-015` | Integrated |
| `REQ-1069` | `UI-CMP-068` | `UAT-X-006` | Integrated |
| `REQ-1070` | `UI-CMP-068/067` | `UAT-X-006` | Integrated |
| `REQ-1071` | `UI-CMP-064` | `UAT-F-022` | Integrated |
| `REQ-1072` | `UI-CMP-073` | `UAT-F-022` | Integrated |
| `REQ-1073` | `SCR-053`…`058`, `SCR-061` | `UAT-P-010` | Integrated |
| `REQ-1074` | `UI-CMP-058/059` | `UAT-P-005` | Integrated |
| `REQ-1075` | `UI-CMP-059/030` | `UAT-P-006` | Integrated |
| `REQ-1076` | Privacy surfaces | `UAT-P-011` | Integrated |
| `REQ-1077` | All player screens | `UAT-P-011` | Integrated |
| `REQ-1078` | `SCR-083/084` | `UAT-J-001` | Integrated |
| `REQ-1079` | `SCR-081` | `UAT-J-002` | Integrated |
| `REQ-1080` | Admin screens | `UAT-J-004` | Integrated |
| `REQ-1081` | All screens | `UAT-A-001` | Integrated |
| `REQ-1082` | All screens | `UAT-A-002` | Integrated |
| `REQ-1083` | `UI-CMP-022` | `UAT-A-003` | Integrated |
| `REQ-1084` | `UI-CMP-012/058` | `UAT-A-009` | Integrated |
| `REQ-1085` | Animated surfaces | `UAT-A-008` | Integrated |
| `REQ-1086` | Form components | `UAT-A-005` | Integrated |
| `REQ-1087` | All text-bearing | `UAT-A-010` | Integrated |
| `REQ-1088` | All action surfaces | `UAT-P-008` | Integrated |
| `REQ-1089` | 13D traceability | `UAT-I-016` | Integrated |

**Tally:** 120/120 cross-cutting requirements dispositioned; 0 orphans. Three PROVISIONAL conditions (`REQ-994`, `REQ-1057`, plus the 13C notification rows below) remain recorded, not upgraded.

### 15.3 Matrix C (iii) — Interaction requirements (`REQ-1090`…`REQ-1203`)

| REQ | UI owner | Primary test | Disposition |
|---|---|---|---|
| `REQ-1090`…`REQ-1102` (13 journey rows) | `JRN-A`…`JRN-M` | `UAT-F-001`…`UAT-F-025` | Integrated; each journey has a completion test |
| `REQ-1103` | `FLOW-001` | `UAT-F-001` | Integrated |
| `REQ-1104` | `FLOW-002` | `UAT-F-002` | Integrated |
| `REQ-1105` | `FLOW-003` | `UAT-F-001` | Integrated |
| `REQ-1106` | `FLOW-004` | `UAT-E-001` | Integrated |
| `REQ-1107` | `FLOW-005` | `UAT-F-003` | Integrated |
| `REQ-1108` | `FLOW-006` | `UAT-F-003` | Integrated |
| `REQ-1109` | `FLOW-007` | `UAT-F-004` | Integrated |
| `REQ-1110` | `FLOW-008` | `UAT-F-005` | Integrated |
| `REQ-1111` | `FLOW-009` | `UAT-F-006` | Integrated |
| `REQ-1112` | `FLOW-010` | `UAT-F-007` | Integrated |
| `REQ-1113` | `FLOW-011` | `UAT-F-008` | Integrated |
| `REQ-1114` | `FLOW-012` | `UAT-F-009` | Integrated |
| `REQ-1115` | `FLOW-013` | `UAT-F-010` | Integrated |
| `REQ-1116` | `FLOW-014` | `UAT-F-011` | Integrated |
| `REQ-1117` | `FLOW-015` | `UAT-F-012` | Integrated |
| `REQ-1118` | `FLOW-016` | `UAT-F-013` | Integrated |
| `REQ-1119` | `FLOW-017` | `UAT-F-014` | Integrated |
| `REQ-1120` | `FLOW-018` | `UAT-F-015` | Integrated |
| `REQ-1121` | `FLOW-019` | `UAT-F-016` | Integrated |
| `REQ-1122` | `FLOW-020` | `UAT-F-017` | Integrated |
| `REQ-1123` | `FLOW-021` | `UAT-F-018` | Integrated |
| `REQ-1124` | `FLOW-022` | `UAT-F-019` | Integrated |
| `REQ-1125` | `FLOW-023` | `UAT-F-020` | Integrated |
| `REQ-1126` | `FLOW-024` | `UAT-F-021` | Integrated |
| `REQ-1127` | `FLOW-025` | `UAT-F-022` | Integrated |
| `REQ-1128` | `FLOW-026` | `UAT-F-022` | Integrated |
| `REQ-1129` | `FLOW-027` | `UAT-F-003` | Integrated |
| `REQ-1130` | `FLOW-028` | `UAT-F-023` | Integrated |
| `REQ-1131` | `FLOW-029` | `UAT-F-023` | Integrated |
| `REQ-1132` | `FLOW-030` | `UAT-F-024` | Integrated |
| `REQ-1133` | `FLOW-031` | `UAT-F-024` | Integrated |
| `REQ-1134` | `FLOW-032` | `UAT-F-025` | Integrated |
| `REQ-1135` | `FLOW-033` | `UAT-F-026` | Integrated |
| `REQ-1136`…`REQ-1148` (state rows) | Screens/components | `UAT-E-001`…`UAT-E-014` | Integrated |
| `REQ-1149`/`REQ-1150` | State announcements/persistence | `UAT-A-001`/`UAT-E-012` | Integrated |
| `REQ-1151`…`REQ-1153` | Pending/provisional states | `UAT-E-010`/`UAT-E-012` | Integrated |
| `REQ-1154` | Validation timing | `UAT-E-006` | Integrated |
| `REQ-1155` | Confirmation content | `UAT-E-007` | Integrated |
| `REQ-1156` | Destructive pattern | `UAT-P-009` | Integrated |
| `REQ-1157` | Single-flight | `UAT-C-001` | Integrated |
| `REQ-1158` | Uncertain outcome | `UAT-C-002` | Integrated |
| `REQ-1159` | Duplicate/idempotency dependency | `UAT-C-003` | Integrated; backend key remains an implementation dependency |
| `REQ-1160` | Failure message anatomy | `UAT-C-004` | Integrated |
| `REQ-1161` | Named failure treatments | `UAT-C-005` | Integrated |
| `REQ-1162` | Keyboard operability | `UAT-A-001` | Integrated |
| `REQ-1163` | Overlay focus | `UAT-A-007` | Integrated |
| `REQ-1164` | Transition focus/title | `UAT-A-002` | Integrated |
| `REQ-1165` | Error association/summary | `UAT-A-006` | Integrated |
| `REQ-1166` | State announcements | `UAT-A-009` | Integrated |
| `REQ-1167` | Table/chart semantics | `UAT-A-003`/`UAT-A-010` | Integrated |
| `REQ-1168` | 320 px/200% | `UAT-R-007` | Integrated |
| `REQ-1169` | Touch targets | `UAT-R-005` | Integrated |
| `REQ-1170` | Reduced motion | `UAT-A-008` | Integrated |
| `REQ-1171` | A11y evidence boundary | `UAT-A-009` | Integrated; no conformance claimed |
| `REQ-1172`…`REQ-1181` (onboarding) | Tutorials | `UAT-E-001`…`UAT-E-004` | Integrated |
| `REQ-1182` | Event-only notifications | `UAT-E-008` | Integrated |
| `REQ-1183` | Routing tiers | `UAT-E-008` | **PROVISIONAL** preserved; test is specification-level |
| `REQ-1184` | Deep-link fallback | `UAT-F-003` | Integrated |
| `REQ-1185` | Notification grouping | `UAT-E-008` | **PROVISIONAL** preserved |
| `REQ-1186` | Non-opt-out notices | `UAT-J-006` | Integrated |
| `REQ-1187` | Notification focus/announcement | `UAT-A-009` | Integrated |
| `REQ-1188` | Offline read-only | `UAT-C-006` | Integrated |
| `REQ-1189` | Offline as-of | `UAT-C-007` | Integrated |
| `REQ-1190` | Session expiry/destination | `UAT-C-009` | Integrated |
| `REQ-1191` | Refresh during commit | `UAT-C-003` | Integrated |
| `REQ-1192` | Reconnection refresh | `UAT-C-008` | Integrated |
| `REQ-1193` | No automatic retry | `UAT-C-010` | Integrated |
| `REQ-1194` | Navigation consistency | `UAT-X-007` | Integrated |
| `REQ-1195` | Object consistency | `UAT-X-008` | Integrated |
| `REQ-1196` | Financial consistency | `UAT-X-001` | Integrated |
| `REQ-1197` | Permission consistency | `UAT-P-012` | Integrated |
| `REQ-1198` | Route/alias stability | `UAT-X-009` | Integrated |
| `REQ-1199` | List grammar | `UAT-A-003` | Integrated |
| `REQ-1200` | Confirmation consistency | `UAT-E-007` | Integrated |
| `REQ-1201` | No duplicate feedback | `UAT-X-010` | Integrated |
| `REQ-1202` | Cross-device consistency | `UAT-R-002` | Integrated |
| `REQ-1203` | Internal traceability | `UAT-I-016` | Integrated |

**Tally:** 114/114 interaction requirements dispositioned; 0 orphans. `REQ-1183` and `REQ-1185` remain PROVISIONAL; no status changed.

### 15.4 Matrix D — UI capability to requirement/decision

| UI capability | Evidence | Requirement | Decision/rule source |
|---|---|---|---|
| Persistent shell and section navigation | `UI-CMP-001`…`003` | `REQ-970`…`972` | D-201/D-209 |
| Turn heartbeat and boundary display | `UI-CMP-007` | `REQ-975` | TR-024/039; `13A-PR-01` |
| Six number types and as-of labels | `UI-CMP-012/013` | `REQ-980/1062/1063` | ECN-177; D-056 |
| Triple balance law | `UI-CMP-033` | `REQ-1001/1065` | MKT-053; D-208 |
| Bounded digest and pending inbox | `SCR-013/014` | `REQ-882/883` | TR-004/088; D-223 |
| Political six-state banner | `UI-CMP-039` | `REQ-1010` | DMP-268 |
| Policy cooldown control | `UI-CMP-040` | `REQ-1011` | D-087 |
| Election anchor display | `UI-CMP-041` | `REQ-1012` | D-106/D-107 |
| Construction one-slot preview | `UI-CMP-036` | `REQ-1005` | URB-064/148; D-073 |
| Research one-project card | `UI-CMP-037` | `REQ-1006` | D-076 |
| Directed-trade two-sided record | `UI-CMP-046/047` | `REQ-1022/1023` | D-016/D-017 |
| Global Trade absence | `UIX-B01` | `REQ-907/908` | D-122; G-1…G-6 |
| Directional posture | `UI-CMP-044` | `REQ-1020/1067` | DIP-023/024 |
| Treaty lifecycle/publication | `UI-CMP-045/048` | `REQ-1021/1024` | DIP-108–113; D-030 |
| Alliance ARL and 0% fallback | `UI-CMP-051/052` | `REQ-1027/1028` | D-141; ALL-187 |
| No alliance military authority | `SCR-058/061` | `REQ-1039/1073` | AX-18; WAR-148/161 |
| OP pool and reservation | `UI-CMP-057` | `REQ-1033` | D-015 (10B-C3) |
| Threat band only | `UI-CMP-058` | `REQ-1034` | WAR-086 |
| Surrender off-ramp | `SCR-067` | `REQ-1126` | WAR-131/132; UD-032 |
| Cause/consequence event pairing | `UI-CMP-064` | `REQ-1041/1071` | WEP-179/619 |
| Denominator/window standings | `UI-CMP-068` | `REQ-1045/1069` | WEP-324/325 |
| k=5 suppression state | `UI-CMP-072` | `REQ-1056/1066` | D-027; WEP-663 |
| Privacy classes and SEC exclusion | `SCR-079/085` | `REQ-1076/1077` | PRV-002/009/014 |
| Report intake and appeal route | `SCR-081/083` | `REQ-950/952/1078` | MOD-002/013 |
| Two-person sanctions | `SCR-094` | `REQ-963` | MOD-022 |
| Admin root and least privilege | `SCR-091`…`100` | `REQ-960/978/1080` | D-042; ADM-003 |
| Confirmation/destructive patterns | `UI-CMP-088/090`, `OVL-01/02` | `REQ-1155/1156` | D-214; RRL-006 |
| Single-flight and uncertainty | `UI-CMP-085` | `REQ-1157/1158` | D-225 |
| Offline read-only | `SCR-016`/shell | `REQ-1188`…`1193` | D-228 |
| Responsive must-not-simplify | All layouts | `REQ-1052/1202` | D-202/D-211 |
| Keyboard/focus/announcements | All interactive | `REQ-1081/1163/1166` | `13A-DS-07`…`13` |
| Provisional honesty | `UI-CMP-019/072` | `REQ-1153` | `13A-PR-16`; D-194 |
| No off-screen consequences | Digest/events/chronicle | `REQ-882/1040/1048` | `13A-PR-15` |

**Matrix D verdict.** Every distinctive UI capability traces to either a confirmed requirement/rule or a recorded decision. No capability exists "because it looked good"; no requirement exists without a capability owner.

---

## 16. Matrix J — Cross-stage consistency

| Stage 1/2 source | Decision/rule | UI architecture element | Consistency finding |
|---|---|---|---|
| Report 05; D-007 | Nation Supremacy identity | Shell, landing, guide | Consistent |
| AI_CONTEXT §2; D-008/D-015 | Browser, Cloudflare + Supabase, UTC cadence | No client download; turn indicator | Consistent |
| Report 06 systems; B-02 | Every consequence visible | Digest, inbox, chronicle | Consistent |
| Report 07; B-04 | Conservation, six number types | Treasury family | Consistent |
| Report 07; B-05 | Cities, DC, production | City family | Consistent |
| Report 06; B-06 | Politics and stability | Political family | Consistent |
| Report 07; B-07 | Two market systems | Directed family; Global Trade absent | Consistent |
| Report 08; B-08 | Player sovereignty | No delegation control | Consistent |
| Report 09; B-09 | Alliances as coordination, not command | Alliance family | Consistent |
| Report 10; B-10 | Abstract warfare, OP | War family | Consistent |
| Report 11; B-11 | Progression without composite score | World family | Consistent |
| Report 08; B-12 | Fair play and privacy | Protection family | Consistent |
| D-014 | AI decision policy | 13D decisions D-234…236 | Consistent |
| D-021 | No attendance rewards | Digest wording | Consistent |
| D-026 | Retention classes | History labels | Consistent |
| D-027 | k=5 suppression | Named suppressed state | Consistent |
| D-030 | Parties-only pending | Proposal visibility | Consistent |
| D-032/D-034 | One account; pair restrictions | Registration, shared-network review | Consistent |
| D-036 | Public profile limits | `SCR-010` | Consistent |
| D-038 | Neutral naming | Creation feedback | Consistent |
| D-039 | Immediate reroll | `SCR-090` | Consistent |
| D-040 | One-time protection | `SCR-008/089` | Consistent |
| D-042 | Admin roles/least privilege | Admin root | Consistent |
| D-048 | Power is derived, not stored | Power grid | Consistent |
| D-056 | Six number types | Data components | Consistent |
| D-067 | Twelve-city screen | Cities overview | Consistent |
| D-073/D-074 | One slot; demolition refund | Construction | Consistent |
| D-076 | One research project | Research | Consistent |
| D-087 | Policy cooldown | Policy control | Consistent |
| D-094 | Three campaign actions | Campaign centre | Consistent |
| D-106/D-107 | Election anchor/window | Election dashboard | Consistent |
| D-117/D-122 | No pre-gate statistics; Global Trade gated | Trade history/board | Consistent |
| D-140/D-141 | Alliance treaties; ARL boundary | Alliance family | Consistent |
| D-198…D-205 | UI foundations | Shell, inventory, design system | Consistent |
| D-206…D-219 | Screen/component positions | B-13 | Consistent |
| D-220…D-232 | Interaction positions | B-13C | Consistent |
| D-233 | Owner acceptance of 13B/13C | Scope boundary | Consistent; 13D does not reopen |
| UD-017/040–060 | Owner-reserved matters | Labelled limitations | Preserved |

**Matrix J verdict.** No Stage 1 or Stage 2 decision is contradicted. The UI architecture is a faithful consumer of the accepted systems, not a parallel design.

---

## 17. Gap register

Every gap records the required fields. Severity is assigned against the project's own risk order (security/fair play first, then gameplay coherence, then documentation). Statuses: `OPEN`, `FIXED IN 13D`, `DEFERRED`, `OWNER-RESERVED`, `IMPLEMENTATION-DEPENDENCY`.

| Gap | Description | Category | Evidence | Affected screens/components | Journey/flow | System | Requirements/decisions | Severity | Player impact | Security/fair-play impact | Dependency | Disposition | Future phase | Acceptance condition | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `GAP-13D-01` | Decision-register §6 tallies were stale (267/219; maxima D-219/DD-267/REQ-1089) while the header recorded D-233/DD-281 | Documentation inconsistency (confirmed) | `04` §6 vs header | None | — | Register | D-233; DD-281 | Medium | None directly; misleading count | None | None | Reconcile tallies and maxima in 13D | 13D | Tallies equal actual rows | **FIXED IN 13D** |
| `GAP-13D-02` | `10B_validate_warfare.py` expected `CURRENT_SUBPROMPT = "13C"` while `status_rules.py` is `13D`; 1 failing check | Confirmed defect (validator) | 10B run: 1036 checks, 1 failure | None | — | QA | — | Medium | None | None | None | Refresh expectation to current frontier | 13D | 10B validator passes with no logic weakened | **FIXED IN 13D** |
| `GAP-13D-03` | Admin workspaces `SCR-096`…`SCR-100` and `SCR-091/095` have no dedicated `FLOW-` entries beyond `FLOW-032` | Missing interaction flow | 13C flow catalogue | `SCR-091`…`SCR-100` | `FLOW-032` only | ADMIN | `REQ-960`…`969`, `REQ-1134` | Low | Admin efficiency only | Audit completeness depends on admin flows | None for documentation | Screen controls + admin UATs cover the interactions; dedicated flows may be added in implementation design | Implementation phase (design) | Every admin control has a tested interaction path | **DEFERRED** |
| `GAP-13D-04` | Alliance readiness/activity declarations (`AX-12`) have no UI surface | Missing specification (candidate capability) | AX-12 status = candidate informational feature | None | — | ALL | AX-12; UD-044/049 | Low | No product obligation yet | None | Owner/UD-049 | Not built; no screen invented | Later alliance scope | A rule/decision creates the capability | **OWNER-RESERVED** |
| `GAP-13D-05` | No dedicated alliance history/audit surface; records reachable from `SCR-053/057` only | Missing specification (low) | B-09 AX-21; 13B inventory | `SCR-053`, `SCR-057` | — | ALL | AX-21; D-026 | Low | History discoverability | Audit visibility is partial | None | Accept surface-level history; no new screen | Later alliance scope | A history view is specified if required | **DEFERRED** |
| `GAP-13D-06` | Audit ledger's tamper-evidence cannot be accepted: no digest chain, no verification job, no protective trigger | Blocked integration | SEC-036–040; EVD-030/041; 12C BLOCKED tests | `SCR-096`, `SCR-093`, `SCR-098` | `FLOW-032` | ADMIN/FP | `REQ-965/1080`; `INT-014` | **High** | Admin may see an unverified spine | Audit integrity unproven | Production security work (0005, trigger, job) | UI shows data only; no tamper-evidence claim | Authorized security implementation | An executed verification run and trigger exist | **OPEN** |
| `GAP-13D-07` | Supabase `profiles` table-wide `UPDATE` including `treasury` remains in the feasibility prototype | Blocked integration | 12A/12B/12C records; AI_CONTEXT | All write surfaces | All committing flows | ECON/Platform | REQ-005; SEC-012; `INT-003` | **High** | Client write path could bypass server rules | Treasury integrity at risk | Corrective migration 0005; SQL tests | No UI contract assumes client authority; all writes server-authoritative | Authorized implementation | Column-level grants and SQL tests pass | **OPEN** |
| `GAP-13D-08` | Continuity/roadmap status blocks still said "13D NOT STARTED / NOT AUTHORIZED" during execution | Documentation inconsistency (temporal) | AI_CONTEXT/ROADMAP/HANDOFF | None | — | Register | — | Low | Misleading current status | None | None | Reconcile after execution | 13D | All current-status records agree | **FIXED IN 13D** |
| `GAP-13D-09` | Global Trade has no executable UI test; absence duty only | Blocked integration | G-1…G-6 not met | `SCR-038/039` | — | MKT | `REQ-907/908`; D-122 | Medium | Feature unavailable by design | Prevented price/stat manipulation pre-gate | G-1…G-6 | Absence tests only | Post-gate authorized phase | Gate passes and flows/tests are authored | **OPEN (BY GATE)** |
| `GAP-13D-10` | Notification routing tiers and grouping threshold remain provisional | Provisional dependency | `REQ-1183/1185`; D-232 | `SCR-019` | `FLOW-027` | TURN | `REQ-1183/1185` | Medium | Some notices may route differently after evidence | Non-opt-out preservation is fixed | Playtest/notification study | Tests are specification-level; safe defaults recorded | Post-playtest | A tier study or owner decision | **OPEN (PROVISIONAL)** |
| `GAP-13D-11` | No built UI exists, so every acceptance test remains unexecuted | Implementation absence | Whole package | All | All | All | All | **High** (programme) | No feature exists yet | None | Full implementation | Status is `SPECIFIED`, never `PASSED` | Authorized implementation | Tests are implemented and executed | **OPEN (EXPECTED)** |
| `GAP-13D-12` | World Health per-figure k=5 evidence does not exist; `SCR-077` is provisional | Provisional dependency | D-027; WEP-663 | `SCR-077` | — | WORLD | `REQ-946` | Low | Aggregate view unavailable | Prevents small-group disclosure | Population data | Absence state specified | Post-launch evidence | k=5 passes for each figure | **OPEN (PROVISIONAL)** |
| `GAP-13D-13` | Dormancy is represented within account/protection surfaces but has no dedicated view | Missing specification (informational) | B-03 D-028; 13B inventory | `SCR-084`, `SCR-089` | — | ACC | D-028 | Informational | A dormant player's state is discoverable indirectly | None | None | No new screen; account state suffices | Later UX review | UX review finds a need | **DEFERRED** |
| `GAP-13D-14` | `SCR-020` pins have no flow and remain absent pending fair-play review | Provisional dependency | `13A-OQ-012`; `REQ-889` | `SCR-020` | — | SHELL | `REQ-889`; D-232 | Low | Feature unavailable | Pin list could leak visibility | Fair-play review | Absence specified | Post-review | Review closes and a flow is authored | **OPEN (PROVISIONAL)** |
| `GAP-13D-15` | `SCR-068` intelligence has no rule; placeholder only | Blocked integration | B-10 espionage exclusion; 13A-OQ-010 | `SCR-068` | — | WAR | `REQ-937` | Low | Feature unavailable | Prevents invented intelligence | Future owner-authorized B-10 rule | Absence specified; not linked | Future B-10 scope | A rule exists and is authorized | **OPEN (BY RULE)** |
| `GAP-13D-16` | Alliance operational funding has no approved cost schedule, so the ARL has no spendable purpose | Owner-reserved / blocked feature | D-141; UD-046 | `SCR-057` | `FLOW-020` | ALL/ECON | `REQ-926`; `REQ-1027` | Medium | Alliance funds are receipt-only | Prevents unaudited spending | Owner decision on cost schedule | UI shows `AVAILABLE`/`RESERVED`/`EXPENDED` with no spend control | Owner | A cost schedule and purpose are approved | **OWNER-RESERVED** |

**Gap tally:** 16 gaps — 3 fixed in 13D, 8 open (including 2 high-severity production-security dependencies, 3 provisional, 1 gated, 1 by-rule and 1 expected implementation absence), 3 deferred and 2 owner-reserved. No critical-severity UI-specification defect was found. The two high-severity open items are production/security obligations, not UI design omissions; they are carried forward unchanged.

---

## 18. Matrix index and integrity statement

| Matrix | Title | Location | Rows | Primary authority |
|---|---|---|---|---|
| A | Screen-to-system | §8 | 100 | 13B screen bodies + this document |
| B | System-to-screen | §9 | 90 capability rows | B-02…B-12 |
| C | Requirement-to-UI | §15.1–§15.3 | 100 formulaic + 120 + 114 | 13B/13C requirement registers |
| D | UI-to-requirement | §15.4 | 32 capability rows | Requirements + decisions |
| E | Journey-to-integration | §11 | 13 | 13C journeys |
| F | Flow-to-contract | §12 | 33 | 13C flows + this document |
| G | Component/overlay | §13 | 98 | 13B components |
| H | Integration-contract coverage | `23_ui_integration_contracts.md` §5 | 34 | This document + systems |
| I | Gap-to-acceptance | §17 | 16 | This document |
| J | Cross-stage consistency | §16 | 37 | Stage 1/2 sources |
| K | Prompt 13 acceptance coverage | `23_prompt_13_final_reconciliation_and_acceptance.md` §7 | 28 gates + 5 evidence blocks | This document + D4 |
| L | Navigation reachability | §10 | 100 | 13B navigation register |

**Integrity statement.** All matrices use stable identifiers. No matrix contradicts another: every screen in A appears in L; every journey in E uses only screens in A/L; every flow in F uses only screens in A; every component in G is owned by a screen in A; every contract in H is used by a flow in F; every gap in I names a screen/contract/requirement that exists or a documented absence.

---

*End of B-13D integration and traceability deliverable.*
