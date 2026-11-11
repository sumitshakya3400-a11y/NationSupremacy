# B-12 — Fair-play cross-system integration specification

**Version:** 1.0 · **Created:** 2026-11-10 · **Stage 2, Prompt 12C**
**Status:** **Integration specification — design only.** Every row is a policy interface mapped to a workflow. `Definition: COMPLETE` and `Execution: NOT RUN` are the only honest values in this document: no integration has been executed, nothing is implemented, verified, runtime-tested or operating.
**Authority.** This document owns the B-12 **integration matrix** (`INT-001`…`INT-020` expanded to operational fields) and the cross-system consistency findings. It owns **no rule** (the [B-12 rulebook](20_fair_play_and_player_protection.md) does), **no contract identifier** (`INT-` is allocated by `FP-004`/§16 of the rulebook), **no gameplay rule** (each owning subsystem does), and **no decision**. Where this document and an owning subsystem's rule disagree, **the owning subsystem wins** and this document is corrected (`GOV-019`, `REQ-815`, `REQ-860`).
**Companions.** [B-12 rulebook](20_fair_play_and_player_protection.md) · [B-12 requirements](20_fair_play_and_player_protection_requirements.md) · [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) · [B-12 acceptance](20_fair_play_and_player_protection_acceptance.md) · [12C journeys and workflows](20_fair_play_and_player_protection_workflows.md) · [12C edge cases and acceptance](20_fair_play_and_player_protection_edge_cases_acceptance.md) · [12A integration and risk registers](research/12A_requirements_integration_and_risk_registers.md) · [B-02 turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [B-03 accounts](09_account_onboarding_nation_creation_and_progression.md) · [B-04 economy](10_economy_resources_treasury_and_finances.md) · [B-05 cities](11_cities_infrastructure_production_and_research.md) · [B-06 politics](12_population_and_domestic_politics.md) · [B-07 markets](13_trade_and_markets.md) · [B-08 diplomacy](15_diplomacy.md) · [B-09 alliances](16_alliances.md) · [B-10 warfare](17_warfare_and_settlements.md) · [B-11 world events](18_world_events_objectives_rankings_progression.md) · [Prompt 11C companion](19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md).

---

## 1. Scope and method

**1.1 No new contract identifier is created.** Prompt 12B §16 allocates exactly twenty cross-system contracts, `INT-001`…`INT-020`, and §16.1 states seven normative dependency fields per contract. This document **reuses all twenty with their existing identifiers**, expands them to the fifteen operational fields Prompt 12C §7 requires, and creates **no** `INT-021`, no parallel contract namespace and no competing source of truth. The identifier policy is recorded as `D-190`.

**1.2 Method.** For each affected subsystem: (a) find the genuine fair-play integration points in its own published rules; (b) state what B-12 may and may not do there; (c) bind each point to a workflow, a contract row and an acceptance block; (d) test the twelve consistency rules of §6; (e) record any contradiction with its authority, impact and the decision required, without choosing a winner.

**1.3 What is not claimed.** No integration has been executed. No interface, API, endpoint, schema, column, queue or job is defined here (`P12B-18` limitation: "contracts are policy interfaces, not API definitions"). Where a technical detail is undecided, this document states the required behaviour and marks the implementation decision unresolved.

---

## 2. Integration matrix, part 1 — boundaries and data

| Contract | Source → destination | Trigger | Required data (minimum necessary) | Data authority | Processing responsibility | Permissions |
|---|---|---|---|---|---|---|
| `INT-001` | B-12 ↔ B-03 accounts | A sanction, suspension, restoration or lift is decided (`FPW-013`–`FPW-016`) | Account identifier, action class, tier, reason code, end condition, case reference, idempotency key | **B-03** owns account state and lifecycle (`ACC-017`, `ACC-020`, `ACC-021`) | B-12 decides and requests; **only B-03 applies** (`MOD-031`) | `R-MOD`/`R-SMOD` within `MOD-037`; requester ≠ applier is not required, but the applier code path is B-03's |
| `INT-002` | B-12 → enforcement/action record | Any conduct consequence is committed | Target account id, `V-` class, tier, evidence class, end condition, appeal route | **B-12** | B-12 writes its own record only | No nation field, no pair state (`MA-002`, `REQ-859`) |
| `INT-003` | B-12 → B-04 economy | A value effect must be restored (`FPW-021`–`FPW-026`) | Case ref, original transaction ref, `COR-001` type, signed delta, reason code, key | **B-04** owns every balance and conservation (`ECN-163`, `ECN-167`) | B-12 instructs; **B-04 computes and appends** (`ECN-166`, `ADM-012`) | No administrator types a balance (`MOD-052`, `SEC-019`) |
| `INT-004` | B-12 ↔ B-05 cities/research | A facility, capacity, book-value or research state is implicated | Action records, ledger events, capacity checks, book-value changes, case ref | **B-05** | Correction only through B-05's `ADJUSTMENT`/`REVERSAL` path (`URB-143`); no direct edit of `capacity`, `housing`, `fixed_asset_book_value` (`URB-143`, `URB-159`) | Purpose-bound read, audited |
| `INT-005` | B-12 ↔ B-06 politics | A ballot, contest or political state is implicated | Contest record, campaign-action rows, state events | **B-06** | Correction is an `ADJUSTMENT` naming the original; **may not set `government_id`** (`DMP-122`, `DMP-267`) | Restricted read, audited; a political state is never a sanction |
| `INT-006` | B-12 ↔ B-07 markets | An `MKT-S01`…`S10` signal is recorded (`MKT-157`) | Signal id, trade/listing id, parties, turn, measured values | **B-07** owns market rules and signals; **B-04** owns settlement value; **B-02** executes at P4 (`MKT-217`–`MKT-219`) | A signal opens review; **B-12 owns the finding** (`MKT-160`); B-12 never resolves a trade, order or price | No public per-trade feed used as evidence (`PRV-009`) |
| `INT-007` | B-12 → B-08 diplomacy | Coercion, false agency or disputed breach is alleged | Treaty/agreement event records, derived breach count, party-published statements | **B-08** owns treaty records and breach counts | Read-only under B-12's class (`DIP-121`); a disputed breach is a **new event**, never an edit (`DIP-119`, `TR-091`) | Audited privileged read; B-08 never reads B-12 records as reputation (`DIP-089`) |
| `INT-008` | B-12 ↔ B-09 alliances | A container transfer, tax/contribution pattern or leadership abuse is implicated | `ALL-159` transfer screening records, ARL categories, tax/donation records, `AUD-AL-013`–`AUD-AL-017` | **B-09** owns Alliance rules, membership, tax and contribution data | Alliance cannot self-adjudicate TOS violations (`AX-23` boundary) and an officer cannot suspend an account (`ALL-158`); platform enforcement is separate | Moderation readership scoped by B-09 permissions, every read audited; aggregate-safe `k ≥ 5` reads only |
| `INT-009` | B-12 → B-10 warfare | A block, result or participation anomaly is used as evidence | `WRA-02` blocked actions, `WRA-04` results, `WRA-06` objective progress, `AUD-AL-017` | **B-10** owns warfare rules, blocks, results and audit rows | B-10 supplies taxonomy and evidence; **B-12 owns enforcement and penalty policy**; no result is recomputed (`WAR-155`) | Redacted-actor view; `AUD-AL-017` restricted (`WAR-154`) |
| `INT-010` | B-12 ↔ B-11 events/objectives | A flag, invalid status or disputed completion arrives (`WEP-632`, `WPC-13`) | Evidence id, inputs, fingerprint, population, requested status | **B-11** owns event, objective and completion state | B-11 flags, records and defers (`WEP-655`, `WEP-704`); B-12 owns enforcement, appeals and retention; a hold is applied as B-11 state with an evidence id, never as a B-11 punishment | `MOD` requests, `SYS` enacts, before the affected grant |
| `INT-011` | B-12 ↔ B-11 rankings/progression | Standing manipulation, snapshot dispute or correction | Sealed snapshot, fingerprint, denominator, rank order, tie group, `corrects_snapshot_id` | **B-11** owns snapshots, honours and publication | B-12 enforces standing manipulation and supplies the disclosure class; **no snapshot is rewritten** — a correction is a new sealed snapshot (`WEP-383`, `WEP-389`, `WEP-580`) | `k ≥ 5` kept; no composite headline leak |
| `INT-012` | B-12 → B-02 notices / Prompt 13 | Any notice, digest entry or surface presentation | Notice class, bounded content, appeal route | **B-02** owns notice classes; **Prompt 13** owns surfaces | B-12 bounds content (`MOD-017`, `MOD-018`); no surface reveals a third party's status (`PRV-019`) | Prompt 13 must publish the appeal route and must not reveal restriction state |
| `INT-013` | B-12 ↔ B-02 turn engine | A turn, phase or ledger integrity event is suspected or confirmed | Turn id, phase, boundary length, affected value path, integrity observation | **B-02** owns phases, the turn ledger and the spine | An integrity failure is an **incident**, not a conduct case, unless manipulation is evidenced (`REQ-856`); a halt is disclosed as a delay (`SEC-026`) | No silent re-derivation; no cadence change (`D-015`, `FP-034`) |
| `INT-014` | B-12 → B-02 audit spine | Every consequential act | Event shape fields per `EVD-027`; case and original references | **B-02 `TR-090`** owns the spine; **B-12** owns event shape, readership and integrity requirement | Append-only with chained digests and scheduled verification (`EVD-030`) | **Specified and unimplemented**: no digest chain, no verification job, no protective trigger exists (`EVD-041`, `SEC-036`, `SEC-038`) |
| `INT-015` | B-12 ↔ Stage 6 authentication | Privileged action, session failure, security event | Step-up session id, security events, revocation request | **Stage 6** owns credentials and sessions | B-12 consumes events and never holds a credential (`SEC-027`, `REQ-840`) | Step-up; separate, independently revocable session |
| `INT-016` | B-12 ↔ B-03 network signal | Triage or pair review | Keyed digest of the network attribute | **B-03** owns the digest | Triage and pair review **only**, inside `NET-039`; never an IP-keyed sanction (`EVD-005`, `MA-010`) | Custody of the keying secret is outside the database (`PRV-024`) |
| `INT-017` | B-12 reporting tooling | A report is submitted or clustered | Report fields, cluster key, supplied artefact pointer | **B-12** | Intake, clustering, duplicate handling (`FPW-001`, `FPW-002`) | Reporter identity never exposed to the reported party |
| `INT-018` | B-12 appeals | An appeal is filed, decided or reopened | Appeal record, grounds, outcome, independence label | **B-12** | One appeal, four outcomes, independence labelled (`FPW-027`–`FPW-030`) | An Alliance expulsion appeal stays with `UD-044` and is not decided here |
| `INT-019` | B-12 ↔ Prompt 14 | A mechanism defect or a value need | Provisional values, observed defect, candidate remedy | **Prompt 14** owns numeric values | B-12 routes defects and chooses no number ("balance before blame") (`REQ-789`) | No calibrated claim may be presented |
| `INT-020` | B-12 ↔ Prompt 13 / owner | A surface, ladder scale, staffing or publication question | Structure, options, dependencies | **Prompt 13** owns screens; **the owner** owns ladder scale, staffing, legal posture and publication | B-12 supplies structure only (`GOV-008`) | Owner-reserved decisions stay Open |

---

## 3. Integration matrix, part 2 — effects, failure, evidence and traceability

| Contract | State effects | Failure behaviour | Audit requirement | B-12 requirements | Existing specifications reused | Workflows | Acceptance block |
|---|---|---|---|---|---|---|---|
| `INT-001` | Account state only; nation and pair states untouched | `FR-02` deny; nothing applied on failure | Privileged access + moderation action | `REQ-777`, `REQ-818`, `REQ-859` | `ACC-017`/`ACC-020`/`ACC-021`, `RRL-016`, `RRL-017`, `ECN-204`; `12A-INT-01`–`12A-INT-03` | `FPW-016`–`FPW-020` | `FPA-091`–`FPA-122` |
| `INT-002` | One enforcement record appended | `FR-03` no commit without record | Moderation action | `REQ-818`, `REQ-819` | `WEP-655` boundary; `19_` §13 `WPC-13` | `FPW-014`, `FPW-016` | `FPA-077`–`FPA-090` |
| `INT-003` | Ledger gains one signed, referenced delta | `COR-018` rollback plus same-key retry; `FR-09` | Financial correction with case and original refs | `REQ-817`, `REQ-836`, `REQ-845` | `ECN-163`, `ECN-165`, `ECN-166`, `ECN-170`; `F-FP-002`, `F-FP-003`, `F-FP-014`; `12A-INT-04`, `12A-INT-05` | `FPW-021`–`FPW-026` | `FPA-123`–`FPA-176` |
| `INT-004` | B-05 state corrected by appended event | Deny non-owner path; incident on break | Privileged read + correction | `REQ-819`, `REQ-860` | `URB-143`, `URB-159`; `12A-INT-06` | `FPW-021`, `FPW-036` | `FPA-123`–`FPA-136`, `FPA-239`–`FPA-246` |
| `INT-005` | Political values adjusted; `government_id` never set | Deny; label and disclose if unscreened | Restricted read + adjustment reason | `REQ-860`, `REQ-861` | `DMP-122`, `DMP-153`, `DMP-267`; `12A-INT-07`, `12A-INT-08` | `FPW-021`, `FPW-036` | `FPA-123`–`FPA-136`, `FPE-035` |
| `INT-006` | Review object; account measure if found; **no market state change** | Signal loss degrades detection only (`FR-04`) | Investigation and evidence write | `REQ-786`, `REQ-791`, `REQ-789` | `MKT-155`–`MKT-162`, `MKT-073`–`MKT-076`, `MKT-217`–`MKT-219`, `W-D08`–`W-D14`; `12A-INT-09`, `12A-INT-25` | `FPW-047` | `FPA-325`–`FPA-334` |
| `INT-007` | None to diplomatic state; evidence cited | Restricted read denied if unauditable (`FR-14`) | Privileged read with purpose | `REQ-781`, `REQ-841`, `REQ-860` | `DIP-085`, `DIP-089`, `DIP-119`, `DIP-121`; `DPE-049`, `DPE-054` (stay PARTIAL); `12A-INT-10` | `FPW-048` | `FPA-335`–`FPA-340` |
| `INT-008` | None to Alliance membership or treasury | Referral instead of adjudication | Privileged access, `k ≥ 5` aggregate reads logged | `REQ-784`, `REQ-788`, `REQ-815` | `ALL-154`–`ALL-159`, `ALL-187`, `ALL-191`–`ALL-195`, `ALL-220`–`ALL-226`, `AX-23`, `AUD-AL-013`–`017`; `12A-INT-11`, `12A-INT-12` | `FPW-049` | `FPA-341`–`FPA-350` |
| `INT-009` | None to battle or campaign results | Missing evidence → hold, not sanction (`SEC-023`) | Evidence write; `AUD-AL-017` restricted | `REQ-860`, `REQ-861`, `REQ-864` | `WAR-005`, `WAR-007`, `WAR-028`, `WAR-151`–`WAR-155`, `WRA-02`, `WRA-04`, `WRA-06`, `WRF-15`–`WRF-19` (unallocated, unusable); `12A-INT-13` | `FPW-050` | `FPA-351`–`FPA-360` |
| `INT-010` | B-11 hold/exclusion status with evidence id | Duplicate completion coalesces; no double grant | Investigation write + status event | `REQ-786`, `REQ-860`, `REQ-861` | `WEP-371`, `WEP-412`, `WEP-632`, `WEP-655`, `WEP-704`, `WPF-32`, `WWF-045`, `WPC-13`; `12A-INT-14` | `FPW-050` | `FPA-351`–`FPA-360` |
| `INT-011` | New sealed snapshot correcting the old; nothing deleted | Withhold publication; incident on residual | Configuration publication + integrity result | `REQ-803`, `REQ-868` | `WEP-383`–`WEP-390`, `WEP-580`, `WEP-583`, `WEP-593`, `WEP-646`, `WEE-034`, `WTS-007`; `12A-INT-15` | `FPW-051` | `FPA-361`–`FPA-370` |
| `INT-012` | Notice queued or digested | `FR-07` fail open into digest, failure recorded | Moderation action | `REQ-803`, `REQ-804`, `REQ-850` | `TR-021`, `TR-023`, `WEE-050` digest privacy, `WPC-14`; `12A-INT-16`, `12A-INT-24`, `12A-INT-29` | `FPW-039` | `FPA-261`–`FPA-266` |
| `INT-013` | Incident opened; affected value path may halt | Never re-execute a committed action; forward-only or last committed (`SEC-010`) | Integrity result + turn record | `REQ-856`, `REQ-858`, `REQ-770`, `REQ-771` | `TR-044`–`TR-046`, `TR-048`, `ECN-171`, `WRF-34`, `WEG-02` (conflicting admin corrections, assigned to Prompt 12/owner); `12A-INT-17` | `FPW-051`, `FPW-033` | `FPA-361`–`FPA-370`, `FPA-217`–`FPA-226` |
| `INT-014` | Spine row appended; chain extended | `FR-01`/`FR-03` fail closed with the transaction | The event **is** the evidence | `REQ-828`, `REQ-829`, `REQ-851`–`REQ-855` | `TR-090`, `TR-091`, `EVD-041`, `SEC-036`–`SEC-040`, `P12B-14`, `WEG-04` (privileged-read auditing, assigned to Prompt 12) | `FPW-044`–`FPW-046` | `FPA-301`–`FPA-324` — **BLOCKED pending an executed run** |
| `INT-015` | Session established or denied | `FR-12` deny, no fallback, no shared operator credential | Privileged access | `REQ-769`, `REQ-840` | `SEC-016`, `SEC-027`, `12A-RK-025`, `12A-OPEN-004` | `FPW-043` | `FPA-291`–`FPA-300` |
| `INT-016` | Queue ordering only | Digest unavailable → triage degrades, play unaffected | Privileged access | `REQ-775`, `REQ-778` | `NET-039`, `NET-014`–`NET-043`, `12A-OPEN-002`, `12A-INT-20` | `FPW-019`, `FPW-007` | `FPA-111`–`FPA-116` |
| `INT-017` | Report and cluster rows | `FR-06` retryable, never silently lost | Moderation action + evidence write | `REQ-822`–`REQ-824` | `MKT-157` signal analogue for volume, `WTS-021`; `12A-RK-029` brigading | `FPW-001`–`FPW-003` | `FPA-001`–`FPA-014` |
| `INT-018` | Appeal record and outcome | `FR-10` window extended by outage, never abandoned | Appeal outcome | `REQ-833`–`REQ-837` | `NET-045`, `WEP-655` boundary, `UD-044`; `12A-INT-22`, `12A-OPEN-012` | `FPW-027`–`FPW-030` | `FPA-177`–`FPA-202` |
| `INT-019` | None (handoff only) | Value unresolved → `PROVISIONAL_BLOCK` | Configuration publication | `REQ-789`, `REQ-867` | `FP-P01`–`FP-P14` classifications, `WEP-649`, `DD-127`; `12A-INT-23` | `FPW-052` | `FPA-371`–`FPA-378` |
| `INT-020` | None (structure only) | Owner dependency named, work continues elsewhere | Governance record | `REQ-868`, `REQ-869` | `GOV-008`, `GOV-009`, `UD-052`–`UD-060`; `12A-INT-26`, `12A-INT-30` | `FPW-052` | `FPA-371`–`FPA-378` |

---

## 4. System-by-system consistency assessment

### 4.1 Market (B-07)

**Integration points.** `MKT-S01`–`MKT-S10` (`MKT-157`); the fair-value band and fresh-nation rules (`MKT-128`, `DD-127`, `W-D14`); the no-self-trade and no-wash/circular rules (`MKT-097`, `MKT-098`); the explicit statement that a signal is triage, not breach (`MKT-158`) and that review, not punishment, happens at the market layer (`MKT-160`); the reversal standard that a market signal alone is not sufficient reason for a reversal (`MKT-161`); and `MKT-218`, which states that a market ban is achieved only through the account measures B-12 owns.
**Preserved unchanged.** The two trading systems, the G-1…G-6 release gates, taker-selected posted-price execution, partial fills, the directed chain and revision model, every declared limit, the `TRADE_BUY`/`TRADE_SELL` pair with one `transfer_id`, the zero-fee contract, the reference prices, the post-gate statistic rule requiring five distinct nations, and the market's own privacy classes. **B-12 changes none of them** (`REQ-861`, `INT-006`).
**Fair-play mapping.** `V-08` economic manipulation and `V-09` market manipulation are B-12 classes; `MKT-S10` (a completed trade whose ledger pair fails conservation) is a **defect, not a player act** and routes to `FPW-033`, never to a conduct case — consistent with `EX-002` and `COR-011`.
**Unresolved.** G-1 needs the incident-rate tolerance band that `12A-INT-25` says B-12 must supply **structurally**. This document supplies its shape (§7 gap `FPG-03`) and chooses no number; G-1 stays **not met**, and `MKT-074` continues to apply: a document is not gate evidence.

### 4.2 Diplomacy (B-08)

**Integration points.** Harassment, coercion and abusive communication are assessed against `V-03`, `V-15` and the diplomatic record; `DIP-078` gives each party the right to publish **its own** reason, which is a party act and not a B-12 disclosure; `DIP-089` forbids B-08 from reading B-12's records as reputation; `DIP-121` is the privileged-read hook this document operates; `DIP-085`/`DIP-086` keep the breach count as a count, not a judgement.
**Preserved unchanged.** The three-layer relationship model, the three-agreement catalogue plus exactly one coercive act (`DP-A01`), player sovereignty over every diplomatic decision, publication at activation, the no-cross-agreement-inference rule and the reroll cleanup.
**Deferrals answered at specification level only.** `DPE-049` (operator correction path for a disputed breach) is answered by `FPW-048` and `FPW-021` as an **append, never an edit** (`DIP-119`, `TR-091`); `DPE-054` (unauthorised history read, restricted-field access, notification leak) is answered by `FPW-036` and `FPW-039`. **Both rows remain PARTIAL** and this document does not restate, renumber or close them: their stated outcome includes an implemented privileged-read audit, which does not exist.

### 4.3 Alliances (B-09)

**Integration points.** `ALL-158` (no officer suspension power; Alliance content subject to global moderation), `ALL-159` (container transfers pass the same Economy and Diplomacy checks; the pool is never an evasion channel), `ALL-187`–`ALL-195` (ARL categories, donation conservation and the no-withdrawal-authority rule), `ALL-220`–`ALL-226` with `AOP-01`–`AOP-04` (purpose-limited operational funding), `ALL-154`–`ALL-157` (immutable spine rows, privacy, throttle, anti-sybil) and `AUD-AL-013`–`AUD-AL-017`.
**Preserved unchanged.** Alliance membership and role permissions, the automatic per-turn production tax with player-authored brackets, the credit-only ARL, the closed purpose registry with no player recipient, the separate Alliance treaty object and NAP coverage, the same-Alliance attack ban, and honour-only aggregate recognition at `k ≥ 5`.
**Boundary held.** `CO-010` no collective punishment; `AX-23`'s security boundary that alliances cannot self-adjudicate TOS violations; `UD-044` (member rights, expulsion and appeal) and `UD-046` (treasury authority) stay Open, and `FPW-049` refers rather than decides.
**Privacy obligation carried.** Moderation tooling must not leak tax or contribution data — enforced as a purpose-bound read (`FPW-036`), minimisation (`PRV-010`) and readership scoping (`12A-INT-12`). This is the roadmap's registered B-09 dependency for Prompt 12.

### 4.4 Warfare (B-10)

**Integration points.** `WAR-155` gives B-10 the taxonomy, evidence fields and block records and gives B-12 enforcement and penalty policy; `WAR-153`/`WAR-154` supply `WRA-02`…`WRA-14` with `AUD-AL-017` restricted; `WAR-009a`–`WAR-009g` is the twelve-check cumulative hostile-effect validator whose block reasons are evidence, not sanctions; `WAR-028` records a blocked reroll as a review signal; `WAR-007` and `WRK-06`/`WRK-07` describe the slot and shield-war patterns.
**Preserved unchanged.** Every combat formula, the campaign lifecycle, operations-point economics, protection limits, settlement term registry, and the fact that **B-10 defines no feeding or deliberate-loss prohibition of its own** — `WCR-33` and `GAP-13` were explicitly transferred to Prompt 12, and `V-10` is where the prohibition lives.
**Nothing invented.** `WRF-15`–`WRF-19` remain unallocated and unusable (`D-143`); no new warfare failure code, event or block type is created here.

### 4.5 World events and objectives (B-11)

**Integration points.** `WEP-655` and `WEP-704` (B-11 flags, records and defers), `WEP-400` (controls, not punishments), `WEP-632`/`WPC-13` (the evidence handoff), `WEP-412` (inputs, fingerprint and population recorded so a disputed result can be reconstructed), `WEP-371` (an evidence hold appears as `EXCLUDED` presentation and loses nothing), `WPF-32` (the existing hold/failure code) and `WWF-045` (B-11 enacts a status change **requested** by Prompt 12).
**Preserved unchanged.** Event classes, triggers, occurrence keys, eligibility, reward classes and caps, the P6 `W1`…`W5` order, objective state machines, and `WEP-710`'s rule that a missing rule is added to B-11 first, not in a workflow.
**No duplicate version.** 12C does not restate `WWF-045` as a B-12 workflow; `FPW-050` is the B-12 side of the same handoff and cites it.

### 4.6 Objectives, rankings and progression (B-11)

**Integration points.** Pre-snapshot inflation (`WTS-007`, `12A-RK-015`), circular-trade volume inflation (`WTS-008`), cross-account funneling (`WTS-009`), manufactured participation (`WTS-017`), scripted grind (`WTS-020`), prestige and season-reset abuse (`WTS-023`, `WTS-029`), identity laundering through a reroll (`WTS-026`) and dormant-account leaderboard freeze (`WTS-030`).
**Preserved unchanged.** Snapshot immutability and the `corrects_snapshot_id` correction pattern, the seal coverage (`WEP-646`), the "no mid-turn rank" rule, the rule that a formula change never rewrites a sealed snapshot, honour-only Alliance recognition, and the ten standings plus WSE separation.
**Historical integrity.** `FPW-051` corrects forward only; deletion of a class-P record is invalid (`WEP-583`). Ranking formulas and scoring are untouched (`REQ-861`), which is why the acceptance block for this row tests linkage and non-rewrite, never a value change.

### 4.7 Accounts, authentication and shared infrastructure

**Integration points.** `ACC-017`/`ACC-020`/`ACC-021` (suspension, ban, removal and preservation are operator actions with a reason and a record), `NET-039` (the IP-only ceiling), `NET-045` (a different reviewer where possible, with the record saying so when not), `RRL-015`–`RRL-021` (reroll laundering review, enforcement survival, blocking conditions), `ECN-204` (a reroll is not an amnesty) and Stage 6's future ownership of credentials (`INT-015`).
**Preserved unchanged.** One account per person (`D-018`, `D-032`, `REQ-777`), the ten account states, the separation of account, nation and pair state, and the two-hour cadence.
**Open defect carried.** `SEC-031` — the feasibility prototype grants `authenticated` a table-wide `UPDATE` on `feasibility.profiles` including `treasury`, with only a row-scoped policy. It is carried into `FPW-021` (no B-12 path may rely on it), `FPW-043` (step-up does not fix a column grant) and the `FPA-301`–`FPA-324` security block, which is **BLOCKED** until column-level privilege correction and SQL permission tests exist (`SEC-033`, `SEC-034`, `P12B-16`).

### 4.8 Turn processing, administration, moderation, reporting, notifications, audit, retention and recovery

`TR-040` phases, `TR-044`–`TR-046` ordering and `TR-048` replay determinism are unchanged; corrections apply at the next valid boundary (`COR-007`). Administration is bound by `ADM-001`'s prohibition list and `ADM-002`'s no-superuser rule, so no 12C workflow grants a new capability. Reporting keeps `INT-017`'s reporter protection. Notifications keep class bounds and `FR-07` digest fallback. Audit keeps `TR-090`/`TR-091` append semantics. Retention uses only existing class values (`PRV-023`, `D-026`, `TR-092`, `MKT-162`) and names `UD-055` where a period is undecided. Recovery and appeals run through `FPW-024`, `FPW-027`–`FPW-030` and `INT-018` without bypassing any owner boundary.

---

## 5. Dependency preservation

All thirty Prompt 12A integration dependencies are reused with their identifiers and none is renumbered. Mapping to this document:

| `12A-INT` | Consumed by | `12A-INT` | Consumed by |
|---|---|---|---|
| `01`, `02`, `03` | `INT-001`, `INT-002`, `FPW-016`–`FPW-020` | `17` | `INT-013`, `FPW-033`, `FPW-051` |
| `04`, `05` | `INT-003`, `FPW-021`–`FPW-026` | `18` | `INT-014`, `FPW-044`–`FPW-046` |
| `06` | `INT-004`, `FPW-021` | `19` | `INT-015`, `FPW-043` |
| `07`, `08` | `INT-005`, `FPW-021` | `20` | `INT-016`, `FPW-019` |
| `09` | `INT-006`, `FPW-047` | `21` | `INT-017`, `FPW-001`–`FPW-003` |
| `10` | `INT-007`, `FPW-048` | `22` | `INT-018`, `FPW-003`, `FPW-004`, `FPW-029` |
| `11`, `12` | `INT-008`, `FPW-049` | `23` | `INT-019`, `FPW-052` |
| `13` | `INT-009`, `FPW-050` | `24` | `INT-020`, `FPW-039`, `FPW-052` |
| `14`, `15` | `INT-010`, `INT-011`, `FPW-050`, `FPW-051` | `25` | `FPW-047`, `FPG-03` |
| `16` | `INT-012`, `FPW-039` | `26` | `FPW-034`, `FPW-041`, `FPG-06` |
| — | — | `27` | `FPW-041`, `FPG-06` |
| — | — | `28` | `FPG-08` (prototype shortcut must not inherit into production) |
| — | — | `29` | `FPW-033`, `FPW-039` |
| — | — | `30` | `FPW-004`, `FPW-013`, `FPW-029`, `FPW-052` |

No new `12A-INT-31` or later identifier is created by Prompt 12C; `12A-INT-30` remains the frontier of that register.

---

## 6. Consistency verification against the twelve rules

| # | Rule | Result | Evidence |
|---|---|---|---|
| 1 | No contradictory rule exists in another system | **Two registered, zero unresolved** | C-01 and C-02 in §7; both keep their authority and both are owner-reserved |
| 2 | No system receives authority it does not possess | **Pass at specification level** | Every row names the owning subsystem; B-12 requests, never applies (`INT-001`–`INT-011`, `MOD-031`) |
| 3 | No duplicate source of truth is created | **Pass** | No new contract id, no new rule id, no new register; §5 reuses 12A ids |
| 4 | Existing resource and currency definitions preserved | **Pass** | No resource, unit, price or `transfer_id` semantics restated |
| 5 | Turn timing and processing order preserved | **Pass** | `TR-040`/`TR-044`–`TR-046`/`TR-048` cited unchanged; corrections apply at the next valid boundary (`COR-007`) |
| 6 | Existing permissions and ownership preserved | **Pass** | `ADM-001` prohibition list enforced in `FPW-042`; no new capability granted |
| 7 | Fair-play restrictions do not break normal play | **Pass** | `FR-04` detection degrades without blocking play; `REQ-863`; no workflow halts the world for a missing detector |
| 8 | Administrative privileges not expanded implicitly | **Pass** | `ADM-002` no superuser, `ADM-018` register is authoritative, `ADM-006` no escalation by grant |
| 9 | Privacy boundaries maintained | **Pass** | `FPW-035`–`FPW-041`; `PRV-019` status never disclosed; `k ≥ 5` in `FPW-038` |
| 10 | Failure handling consistent across systems | **Pass** | Annex D postures reused verbatim; no universal fail-open/fail-closed statement appears anywhere in 12C (`SEC-022`) |
| 11 | Appeals and corrections do not bypass authority | **Pass** | `FPW-024` and `FPW-029` route execution to the owner's path; `ADM-022` bars an appeals reviewer from editing the original |
| 12 | Historical records and rankings not silently rewritten | **Pass** | Append-only everywhere (`TR-091`, `EVD-029`, `WEP-383`, `WEP-583`, `MOD-034`) |

**Citation-accuracy observation, not a conflict.** B-12 `FP-014` and `REQ-772` cite `TR-048` for the no-order-payoff rule, while `TR-048` states replay determinism and `TR-044`–`TR-046` state the ordering bands and total-order key. The rules agree in substance — arrival order buys nothing and a replay reproduces identical ordering — so 12C records the citation as it stands, uses the precise identifiers alongside it, and leaves the rulebook text for its owner document to revise if it chooses. No count, status or rule is changed here.

---

## 7. Conflict and gap register

| ID | What conflicts or is missing | Authority | Impact | Who decides | 12C treatment |
|---|---|---|---|---|---|
| `C-01` | Two incompatible consequence ladders remain in the corpus: B-11's reversal model (`WEP-655`, `WEP-400`) and the permanence carried by B-03/B-06 (`ACC-021`, `NET-038` history). `MOD-036` declares exactly six tiers | `MOD-036` states the target design; `REQ-812` is **Open** | A workflow cannot state an approved duration or authority split | **Owner** (`UD-053`) | `FPW-012`–`FPW-014`, `FPW-017` stop at `PROVISIONAL_BLOCK`; nothing is resolved |
| `C-02` | Correction **reach**: whether value may be recovered from both legs of a flow (`MA-007`, `CO-009`) versus only the receiving account | `REQ-782` is **Open**; `UD-052` | `FPW-023` may execute only the receiving leg today | **Owner** (`UD-052`) | Reach is specified as a decision point with the conservative branch taken |
| `FPG-01` | No `MOD-014` content surface exists, yet `ALL-158` subjects Alliance names, descriptions and bulletins to global moderation | `MOD-014`: B-12 does not create a content surface | Content removal cannot be operated until a surface exists | Prompt 13 owns surfaces; owner owns scope | Registered; `FPW-039` states the bound, none is invented |
| `FPG-02` | B-10 defines **no** feeding or deliberate-loss prohibition; the taxonomy was transferred (`WCR-33`, `GAP-13`) | `V-10`, `CO-007` own the class | `FPW-050` can only enforce against `V-10` elements, not a warfare rule | B-12 owns the class; B-10 owns evidence fields | Recorded as satisfied at class level; no warfare rule invented |
| `FPG-03` | G-1's incident-rate tolerance band has no value | `MKT-073`, `12A-INT-25` | G-1 stays not met; Global Trade stays release-gated | Prompt 14 plus an operational measurement | Shape supplied structurally; no number chosen |
| `FPG-04` | No spine implementation, digest chain, verification job or protective trigger | `EVD-041`, `SEC-036`, `SEC-038`, `P12B-14` | `FPA-301`–`FPA-324` are **BLOCKED**; no tamper-evidence may be claimed | Stage 5 implementation plus an executed verification run | Dependency stated in every affected row; gate untouched |
| `FPG-05` | Authenticated table-wide `UPDATE` on `feasibility.profiles` including `treasury`; no `0005` migration; no SQL permission tests | `SEC-031`–`SEC-035`, `P12B-16` | Single-writer enforcement is unproven in the prototype | Stage 5 column-level privilege work | Carried as an open defect; no RLS-as-column-security assumption anywhere |
| `FPG-06` | Erasure versus the permanent spine, and every retention period, is legally unresolved | `REQ-809`, `REQ-855`, `UD-017`, `UD-055` | `FPW-041` runs the conservative branch only | Owner and counsel | Existing class values consumed by reference; no day invented |
| `FPG-07` | Reviewer independence and staffing cannot be demonstrated | `MOD-005`, `MOD-022`, `MOD-049`, `ADM-013`, `UD-054` | Every segregation claim becomes an `unsegregated` label | **Owner** (`UD-054`) | Labels specified; no separation claimed |
| `FPG-08` | Prototype findings must not inherit into production as if they were design | `SEC-029`, `12A-INT-28`, `WTS-027` | A production grant could repeat the defect | Stage 5 architecture | `FPW-021`, `FPW-043` state the required property, not the prototype's |
| `FPG-09` | Appeal window, decision target and budget are undefined | `MOD-050`, `F-FP-006`, `FP-P06`, `FP-P12`, `UD-059` | `FPW-027` may not enforce an invented window | **Owner** (`UD-059`) | `PROVISIONAL_BLOCK` specified |
| `FPG-10` | The `WPF-` namespace has no "actor not authorised" code and the span is closed | `WEP-667`, `WEP-674`, `19_` §26 gap | No new failure code may be minted | B-11 owns its codes | `FPW-050` reuses `WPF-32`/`WPF-13` semantics as disposed; nothing renumbered |

---

## 8. Non-claims

1. This document specifies interfaces. It defines no API, endpoint, table, column, schema, queue, job or credential.
2. No integration described here has been executed against any implementation; no subsystem currently enforces any of it.
3. No `INT-` identifier is added, removed, renumbered or re-scoped; `INT-001`…`INT-020` and the thirty `12A-INT-` dependencies remain the whole of their namespaces.
4. No existing subsystem rule is edited, and no PARTIAL gate or acceptance status in 11C, 12A or 12B is changed by this document.
5. The two conflicts and ten gaps above are the honest state of cross-system consistency at the specification level. They are not closed by being listed, and none is presented as resolved.
