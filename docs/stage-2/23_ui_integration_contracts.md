# B-13D — UI integration contracts

**Version:** 1.0 · **Created:** 2026-11-13 · **Stage 2, Prompt 13D** · **Status:** specification only.
**Companion to:** [`23_ui_system_integration_and_traceability.md`](23_ui_system_integration_and_traceability.md) (Matrix H owner index) and [`23_ui_acceptance_test_catalog.md`](23_ui_acceptance_test_catalog.md).
**Authority boundary.** This document defines **design-level exchange contracts between the UI and the existing game systems**. It does not define HTTP endpoints, database tables, RPC functions, queues, jobs or runtime services. Where a mechanism is not yet designed, the abstraction boundary is named and classified as a Stage 5/6 implementation obligation. No contract changes a rule, formula, permission or failure code.

---

## 1. Purpose and rules

1. **One contract per UI/system exchange cluster.** A contract states what the UI reads or submits, which system owns the result, and what the UI must never assume.
2. **Reuse before invention.** Existing `INT-`, `AX-` and `WPC-` contracts are authoritative for their system semantics. A `UIX-` contract references them; it never restates or overrides them (D-234).
3. **Server authority is absolute.** A rendered control is not a permission (`REQ-1088`). Every write contract requires server-side validation of ownership, role, state, resources and rules.
4. **No false success.** A success state is shown only after authoritative confirmation (`REQ-1141`). An unconfirmed result is uncertain, never successful (`REQ-1158`).
5. **Idempotency is borrowed, never invented.** Where an owning system defines a key, the UI reuses it. Where none exists, the UI reconciles before retry (`REQ-1159`, DUP-05/06).
6. **Absence is a contract too.** Blocked/provisional surfaces have an explicit absence contract: no data, no stub, no teaser.

---

## 2. Contract field template

Every contract uses the same eleven grouped rows, covering the 35 required fields (field numbers in brackets):

| Group | Fields covered |
|---|---|
| Identity and purpose | [1] identifier, [2] name, [3] purpose |
| Parties and authority | [4] provider, [5] consumer, [33] source authority, [34] status |
| Trigger and preconditions | [6] trigger, [7] preconditions |
| Authentication and authorization | [8] authentication, [9] authorization, [10] permissions |
| Request/command | [11] structure, [12] required fields, [13] types and constraints |
| Response and result | [14] response, [15] result states, [16] validation |
| Failure conditions and identifiers | [17] failure conditions and existing failure families |
| Idempotency and concurrency | [18] idempotency, [19] duplicate protection, [20] concurrency, [21] freshness/staleness |
| Retry, timeout, offline, recovery | [22] retry, [23] timeout, [24] offline, [25] recovery |
| Audit, privacy, notification | [26] audit, [27] privacy, [28] notification |
| Traceability and dependencies | [29] screens, [30] flows, [31] requirements, [32] acceptance tests, [35] dependencies |

**Status values:** `SPECIFIED` (design complete), `PROVISIONAL` (a named value/question can change it), `BLOCKED` (no exchange until a gate/rule), `IMPLEMENTATION-DEPENDENCY` (shape fixed; mechanism is Stage 5/6).

---

## 3. Existing-contract reuse map

| UIX | Reuses (authoritative semantics) | Reuse note |
|---|---|---|
| `UIX-01` | B-03 ACC-017/018; `INT-015` (Stage 6 sessions) | Session identity; no credential held by UI |
| `UIX-02` | B-03 ACC-023/024/031; D-029/D-041 | Verification and recovery |
| `UIX-03` | B-03 NAT-001–030; RRL-005/006; D-038/D-039 | Creation and reroll |
| `UIX-04` | B-03 ONB-009–038; D-040 | Tutorial state, no auto-action |
| `UIX-05` | B-02 TR-024–080; `WPC-01` | Turn/boundary read model |
| `UIX-06` | B-02 TR-004/088/089/092; `INT-012`; REQ-731 | Digest/notices |
| `UIX-07` | B-02 TR-021/022; B-03/B-06/B-10/B-11 read rules | Object read; visibility filter |
| `UIX-08` | B-04 ECN-093–178; `INT-003`; B-02 P4 | Treasury read; correction is not UI |
| `UIX-09` | B-04 ECN-044–139; B-02 P3.3–P4 | Production policy/orders |
| `UIX-10` | B-04 ECN-042/120; B-05 URB-052/066 | Warehouse/power read |
| `UIX-11` | B-05 URB-064/071/148; D-073/D-074 | Construction/demolition |
| `UIX-12` | B-05 URB-032–034; D-068 | City founding |
| `UIX-13` | B-05 URB-093–097; D-076 | Research |
| `UIX-14` | B-06 DMP-073/087/101/102/163/189/268; D-106/D-107 | Politics |
| `UIX-15` | B-07 MKT-019–131; D-016/D-017; `INT-006` | Directed trade |
| `UIX-16` | B-07 MKT-110/140; D-117 | Pre-gate history |
| `UIX-17` | B-08 DIP-023–132; `INT-007` | Diplomacy |
| `UIX-18` | B-09 ALL-080–086; AX-01–05/09/10; `INT-008` | Membership/governance |
| `UIX-19` | B-09 ALL-179–193/220–226; AX-27/AX-28; D-141; `INT-003` | Tax/ARL |
| `UIX-20` | B-09 AX-29/AX-30; D-140; `INT-007` | Alliance treaties |
| `UIX-21` | B-10 WAR-039–053/148–152; D-015 (10B-C3); `INT-009` | Operations/declaration |
| `UIX-22` | B-10 WAR-122–132; UD-032 | Settlement/surrender |
| `UIX-23` | B-10 WAR-085–088/109k/150 | War/battle read |
| `UIX-24` | B-11 WEP-179/203–215/324–362/619–633; `WPC-01`–`WPC-10` | World read |
| `UIX-25` | B-11 WEP-240/499/582/663/705; `WPC-03` | Rewards |
| `UIX-26` | B-12 MOD-002/013/017/018/022/036; `INT-001`/`INT-002`/`INT-017`/`INT-018` | Protection |
| `UIX-27` | B-03 ACC-031/043; B-12 PRV/DAT; D-026/D-041 | Account/data |
| `UIX-28` | B-12 ADM-003/012/021/022; MOD-022/036/037; `INT-001`–`INT-014` | Admin moderation |
| `UIX-29` | B-02 TR-035/043/075/080/090; B-12 EVD-026/030; D-042 | Admin operations/audit |
| `UIX-30` | B-12 MOD-017/018; B-09 ALL-164; TR-049 | Announcements/changes |
| `UIX-B01` | B-07 D-110/D-111/D-117/D-122; G-1…G-6 | **Absence**: no exchange exists |
| `UIX-B02` | B-10 espionage exclusion; `13A-OQ-010` | **Absence**: no rule exists |
| `UIX-P01` | `13A-OQ-012`; `REQ-889` | **Absence**: review pending |
| `UIX-P02` | B-11 D-027/WEP-663 | **Provisional**: k=5 per figure |

**No duplicate contract namespace is created for system semantics.** No `INT-`, `AX-` or `WPC-` identifier is renumbered or reassigned. `UIX-` is a UI-consumer boundary identifier only (D-234).

---

## 4. Read/write boundary register

| UIX | Read | Submit command | Update setting | Request approval | Trigger existing operation | Async result | Receive event |
|---|---|---|---|---|---|---|---|
| `UIX-01` | Session/identity | Login/logout | Keep-session | — | — | — | Session expiry |
| `UIX-02` | Verification state | Register, verify, reset | — | — | — | Verification | — |
| `UIX-03` | Eligibility | Create nation, reroll | Emblem/posture at creation | — | — | Creation result | — |
| `UIX-04` | Tutorial state | Complete/skip step | Tutorial preference | — | — | — | — |
| `UIX-05` | Turn/phase/settlement | — | — | — | — | Boundary result | Turn events |
| `UIX-06` | Digest/alerts | Acknowledge/mute permitted items | Mute allowed classes | — | — | — | Notification |
| `UIX-07` | Objects/dashboards | — | — | — | — | — | — |
| `UIX-08` | Treasury/budget/reports | — | — | — | — | — | Settlement |
| `UIX-09` | Policy/chains | Manual order | Standing policy | — | Yes (production at P3) | Reservation/result | — |
| `UIX-10` | Resources/power | — | — | — | — | — | — |
| `UIX-11` | City/queue | Construct/demolish | — | — | — | Slot result | — |
| `UIX-12` | Eligibility | Found city | — | — | — | Creation result | — |
| `UIX-13` | Tree/progress | Start research | — | — | — | Project result | — |
| `UIX-14` | State/approval/elections | Campaign action | Policy axis | — | Yes (P6 resolution) | Charge/result | Election/crisis |
| `UIX-15` | Chains/offers | Create/counter/accept/decline/cancel | — | — | Yes (P4 settlement) | Settlement | — |
| `UIX-16` | Own history/prices | — | — | — | — | — | — |
| `UIX-17` | Posture/agreements | Propose/counter/withdraw/accept/terminate | — | — | Yes (activation/expiry) | Activation | Treaty events |
| `UIX-18` | Alliance/roles/applicants | Apply/admit/decline/withdraw/role change | Role settings | Two-party where rule requires | — | Membership result | — |
| `UIX-19` | Brackets/ARL | Change bracket (role) | Tax policy version | — | Yes (per-turn collection) | Receipt | Tax receipt |
| `UIX-20` | Treaties/coverage | Propose/accept alliance treaty | — | Recorded per-nation consent | Yes (NAP checks) | Treaty result | — |
| `UIX-21` | OP/readiness | Submit operation, declare war | — | — | Yes (P3.7/P4) | Reservation/result | War events |
| `UIX-22` | Settlement state | Propose/accept/withdraw/surrender | — | — | Yes (campaign end) | Settlement result | — |
| `UIX-23` | Wars/battles/losses | — | — | — | — | — | Battle events |
| `UIX-24` | Events/objectives/standings | — | — | — | — | — | Event/standing |
| `UIX-25` | Rewards/claims | Claim deferred reward | — | — | Yes (claim release) | Claim result | Reward event |
| `UIX-26` | Restriction/appeal | Report, appeal | Consent/privacy where allowed | Appeal review | — | Case status | Decision notice |
| `UIX-27` | Account/data | Close/cancel closure, export request | Privacy/session settings | — | — | Closure/export state | — |
| `UIX-28` | Case/queue | Moderation decision, sanction step | Case assignment | Two-person rule | Yes (B-03 applies sanction) | Decision result | — |
| `UIX-29` | Audit/turn/data/roles | Recovery action, data operation, role grant | Role scope | Step-up where required | Yes (recovery/preservation) | Operation result | — |
| `UIX-30` | Changes/notices | Publish announcement | — | Role authority | — | Publication result | Global notice |
| `UIX-B01` | — | — | — | — | — | — | — |
| `UIX-B02` | — | — | — | — | — | — | — |
| `UIX-P01` | — | — | — | — | — | — | — |
| `UIX-P02` | Aggregates (gated) | — | — | — | — | — | — |

**Rule.** A read contract never confers a write path. An approval request is not an approval until the owning system records it. An asynchronous result is never presented as a completed action before settlement (`REQ-1151`).

---

## 5. Contract catalogue

### UIX-01 — Session and identity

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-01`; Session and identity; establishes who is acting and which nation is active, for every authenticated surface. |
| Parties and authority | Provider: B-03 accounts + Stage 6 authentication (`INT-015`). Consumer: shell and all screens. Source authority: B-03 ACC-017/018; D-041. Status: `SPECIFIED`. |
| Trigger and preconditions | Any authenticated navigation; login; session resume. Preconditions: existing account; credentials; account not closed. |
| Authentication and authorization | Authentication: credential/session mechanism owned by Stage 6. Authorization: session validity and account state. Permissions: none beyond identity. |
| Request/command | Read identity; submit credentials; request logout. Fields: account identifier, nation identifier, session state. Types/constraints: opaque identifiers; no credential in UI storage. |
| Response and result | Account state (`UNVERIFIED`, `VERIFIED`, restricted, suspended, closed), nation linkage, session state. Result states: authenticated, unverified, denied, expired. Validation: server-side. |
| Failure conditions | Invalid credentials, locked/recovery-locked, expired session, suspended account. UI maps to `ERR-04`/`ERR-05`/`ERR-06`; neutral wording; no account enumeration. |
| Idempotency and concurrency | Login is a new session intent; repeated submission ignored while in flight. Logout is idempotent. Freshness: session state re-read on focus/resume. |
| Retry, timeout, offline, recovery | Retry after auth failure only by user action; timeout → `ST-17`; offline → `ST-15`; recovery via re-auth, destination preserved (`REQ-1190`). |
| Audit, privacy, notification | Audit: authentication events owned by B-03/Stage 6. Privacy: no credential/token exposure (`REQ-1077`). Notification: security notices non-opt-out. |
| Traceability and dependencies | Screens: `SCR-003`, `SCR-011`, shell. Flows: `FLOW-002`. Requirements: `REQ-872`, `REQ-1104`, `REQ-1190`. Test: `UAT-I-001`. Dependency: Stage 6 session mechanism; production security obligations. |

### UIX-02 — Registration, verification and recovery

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-02`; Registration, verification and recovery; creates an unverified account and proves e-mail control before nation creation. |
| Parties and authority | Provider: B-03 accounts. Consumer: `SCR-002`, `SCR-004`, `SCR-005`, `SCR-006`. Authority: ACC-023/024/031; D-029/D-041. Status: `SPECIFIED`. |
| Trigger and preconditions | Submit registration; open verification link; request reset; enter recovery code. Preconditions: no authenticated session; valid e-mail pair; password policy; terms. |
| Authentication and authorization | Authentication: none for registration; single-use recovery code for recovery. Authorization: account existence and verification state. Permissions: none. |
| Request/command | E-mail pair, password, optional referrer, terms acknowledgement, verification request, recovery code. Constraints: password policy; e-mail format; terms required; code single-use. |
| Response and result | Account created `UNVERIFIED`; verification pending/verified/expired; reset accepted (no account enumeration); recovery outcome. Validation: server-side plus presentation validation. |
| Failure conditions | Duplicate e-mail (neutral), weak password, terms unchecked, expired link, invalid/consumed code, rate limit. UI: `ERR-08`/`ERR-09`/`ERR-12`/`ERR-15`; `ST-08`/`ST-12`/`ST-11`. |
| Idempotency and concurrency | Repeated submit is one intent (`DUP-01`); resend subject to limit; verification link single-use. Freshness: state re-read on return. |
| Retry, timeout, offline, recovery | Resend after limit; reset route; offline → `ST-15`; recovery never bypasses custody (`REQ-874`). |
| Audit, privacy, notification | Audit: account/security events. Privacy: no account enumeration; token never shown. Notification: verification and security notices. |
| Traceability and dependencies | Screens: `SCR-002`, `SCR-004`…`SCR-006`. Flows: `FLOW-001`, `FLOW-002` alt. Requirements: `REQ-871`, `REQ-873`…`REQ-875`, `REQ-1103`. Test: `UAT-I-002`. Dependency: custom SMTP verification (D-029). |

### UIX-03 — Nation creation and reroll

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-03`; Nation creation and reroll; creates exactly one active nation and resets it under exact-phrase control. |
| Parties and authority | Provider: B-03 nation lifecycle + B-04 starting state. Consumer: `SCR-007`, `SCR-090`. Authority: NAT-001–030; RRL-005/006/021; D-038/D-039. Status: `SPECIFIED`. |
| Trigger and preconditions | Confirm creation; confirm reroll. Preconditions: verified eligible account with no nation; reroll re-authentication and no block condition. |
| Authentication and authorization | Authentication: verified account; fresh re-auth for reroll. Authorization: ownership; eligibility; D-039 block list. Permissions: owner only. |
| Request/command | Name, short name, emblem from game set, starting posture; reroll exact nation name and exact phrase. Constraints: D-038 naming; unique; no reserved names; phrase match. |
| Response and result | Nation created in `awaiting first turn` with starting state; reroll replaces immediately with no renewed protection. Result states: created, rejected, blocked, conflict. Validation: server-side. |
| Failure conditions | Invalid/reserved/unavailable name, ineligible account, concurrent creation, reroll blocked. UI: `ERR-08`/`ERR-11`/`ERR-13`; neutral naming; `AC-03`. |
| Idempotency and concurrency | At most one nation per account; reroll one per confirmation; concurrent create resolves to one nation. Freshness: account home re-read after uncertainty. |
| Retry, timeout, offline, recovery | On uncertain create, re-read account home; never re-create blindly. Offline → writes disabled. Recovery via account home. |
| Audit, privacy, notification | Audit: nation creation and reroll records. Privacy: no reserved-list disclosure. Notification: account/security record only; no reward. |
| Traceability and dependencies | Screens: `SCR-007`, `SCR-090`, `SCR-010`. Flows: `FLOW-003`, `FLOW-031`. Requirements: `REQ-876`, `REQ-959`, `REQ-1105`, `REQ-1133`. Test: `UAT-I-003`. Dependency: reroll review signal (D-039). |

### UIX-04 — Onboarding and tutorial state

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-04`; Onboarding and tutorial; records completion/preference and teaches without acting. |
| Parties and authority | Provider: B-03 onboarding. Consumer: `SCR-008`, `SCR-009`, `SCR-078`. Authority: ONB-009–038; D-040; D-229. Status: `SPECIFIED`. |
| Trigger and preconditions | First session; open/skip/resume/replay a tutorial step. Preconditions: authenticated; tutorial available. |
| Authentication and authorization | Authentication: account session. Authorization: account-scoped completion. Permissions: none beyond own account. |
| Request/command | Step completion/skip/preference; read-only replay request. Constraints: completion once per account; no gameplay action. |
| Response and result | Completion state, resumable position, preference. Result states: completed/skipped/paused. Validation: server-derived where required. |
| Failure conditions | Owning screen blocked → tutorial pauses; interruption → resumable. UI: `ST-11`; no bypass. |
| Idempotency and concurrency | Completion is once-only; replay never re-grants. Freshness: state re-read on entry. |
| Retry, timeout, offline, recovery | Resumable after logout/reroll/block; offline reading only. Recovery: resume from `SCR-008`. |
| Audit, privacy, notification | Audit: completion record. Privacy: no behavioural tracking beyond preference. Notification: none. |
| Traceability and dependencies | Screens: `SCR-008`, `SCR-009`, `SCR-078`, `SCR-013`. Flows: `FLOW-004`. Requirements: `REQ-877`, `REQ-1106`, `REQ-1172`…`REQ-1181`. Test: `UAT-I-003`. Dependency: tutorial content ownership. |

### UIX-05 — Turn and boundary state

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-05`; Turn and boundary state; exposes the authoritative two-hour UTC cadence, phase and settlement state. |
| Parties and authority | Provider: B-02 turn engine. Consumer: shell, `SCR-013`, `SCR-016`, `SCR-097`. Authority: TR-024–080; `WPC-01`. Status: `SPECIFIED`. |
| Trigger and preconditions | Every authenticated load; boundary check; manual refresh. Preconditions: authenticated session. |
| Authentication and authorization | Authentication: session. Authorization: standard player read; operator detail only for `SCR-097`. Permissions: read-only for players. |
| Request/command | Read turn id, boundary time, phase P0–P7, settlement state, queued actions. Constraints: UTC; turns not wall-clock. |
| Response and result | `OPEN`/`LOCKED`/`RESOLVING`/`COMPLETED`/`INTERRUPTED`/`FAILED`; last settlement; next boundary. Validation: server-side. |
| Failure conditions | Boundary interrupted/failed; dependency failure. UI: `ERR-18`/`ERR-03`; `ST-17`/`ST-14`; never invent an outcome. |
| Idempotency and concurrency | Read-only; concurrent reads safe. Freshness: as-of turn mandatory; stale labelled. |
| Retry, timeout, offline, recovery | Retry read; offline shows last confirmed with as-of; recovery `ST-17`; no auto-repeat of actions. |
| Audit, privacy, notification | Audit: turn ledger owned by B-02. Privacy: public turn facts only. Notification: boundary results via digest. |
| Traceability and dependencies | Screens: shell, `SCR-013`, `SCR-016`, `SCR-097`. Flows: `FLOW-005`, `FLOW-033`. Requirements: `REQ-885`, `REQ-975`, `REQ-1135`, `REQ-1193`. Test: `UAT-I-004`. Dependency: `pg_cron` sole scheduler. |

### UIX-06 — Digest, notifications and acknowledgement

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-06`; Digest/notification read and permitted acknowledgement; presents existing events only. |
| Parties and authority | Provider: B-02 notices; B-11 event records. Consumer: `SCR-013`, `SCR-014`, `SCR-019`. Authority: TR-004/088/089; REQ-731; `INT-012`; D-227. Status: `SPECIFIED`; tier defaults `PROVISIONAL`. |
| Trigger and preconditions | Open digest/alerts/inbox; notification arrival; acknowledge/mute. Preconditions: authenticated. |
| Authentication and authorization | Authentication: session. Authorization: object visibility per row. Permissions: read; mute only where rule allows. |
| Request/command | Read digest/alerts; acknowledge; mute permitted class. Fields: event id, tier, object link, read state. Constraints: no event creation/mutation. |
| Response and result | Bounded digest rows with cause chain and deep link; pending totals; read/unread; non-opt-out flags. Validation: server-side. |
| Failure conditions | Event unavailable; destination retired/denied; digest failure. UI: `ERR-03`/`ERR-07`/`ERR-12`; `ST-14`/`ST-09`/`ST-12`; history retained. |
| Idempotency and concurrency | Acknowledge idempotent; mute idempotent. Freshness: counts from last read; no per-second tick. |
| Retry, timeout, offline, recovery | Read retry; offline last confirmed; reconnection refresh (`REQ-1192`). |
| Audit, privacy, notification | Audit: notice records. Privacy: third-party status never disclosed (`PRV-019`). Notification: grouped by source event/object; no fabricated event. |
| Traceability and dependencies | Screens: `SCR-013`, `SCR-014`, `SCR-019`, `SCR-069`. Flows: `FLOW-005`, `FLOW-006`, `FLOW-027`. Requirements: `REQ-882/883/888`, `REQ-1107/1108/1129`, `REQ-1182`…`REQ-1187`. Test: `UAT-I-004`. Dependency: `REQ-1183/1185` provisional tiers/grouping. |

### UIX-07 — Object and overview read

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-07`; Object/overview read; serves dashboards, profiles, chronicle, network and guide with visibility-filtered data. |
| Parties and authority | Provider: B-02…B-11 read models. Consumer: `SCR-010`, `SCR-015`, `SCR-017`, `SCR-018`, `SCR-078`. Authority: TR-021/022; D-026. Status: `SPECIFIED`. |
| Trigger and preconditions | Open a screen or object link; apply filter; open peek. Preconditions: authenticated or public as applicable. |
| Authentication and authorization | Authentication: session or public. Authorization: field-level visibility class. Permissions: none. |
| Request/command | Read object/aggregate with identity, status, values, as-of turn, class. Constraints: no field above viewer class. |
| Response and result | Loaded, partial, empty, suppressed, denied, retired. Validation: server-side. |
| Failure conditions | Missing object, denied field, stale data. UI: `ERR-03`/`ERR-06`/`ERR-11`; `ST-14`/`ST-09`/`ST-03`. |
| Idempotency and concurrency | Read-only; concurrent reads safe. Freshness: as-of label on every figure. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed; recovery by refresh. |
| Audit, privacy, notification | Audit: privileged reads only where rule requires. Privacy: class-filtered; suppressed ≠ zero. Notification: none. |
| Traceability and dependencies | Screens: `SCR-010`, `SCR-015`, `SCR-017`, `SCR-018`, `SCR-078`. Flows: `FLOW-005`, `FLOW-027`. Requirements: `REQ-879/884/886/887/947`, `REQ-1195`. Test: `UAT-I-005`. Dependency: Stage 5 read model design. |

### UIX-08 — Treasury, budget and reports

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-08`; Treasury/budget/report read; presents separated number types, balances and history. |
| Parties and authority | Provider: B-04 economy (ledger); B-02 P4 settlement. Consumer: `SCR-029`, `SCR-030`, `SCR-031`. Authority: ECN-093–178; D-050/D-051; `INT-003`. Status: `SPECIFIED`. |
| Trigger and preconditions | Open treasury/budget/report; refresh after settlement. Preconditions: authenticated. |
| Authentication and authorization | Authentication: session. Authorization: own nation only; privileged views scoped. Permissions: read-only. |
| Request/command | Read opening/income/expenditure/net/closing, total/reserved/available, forecasts, history. Constraints: six number types; as-of. |
| Response and result | Labelled registers; forecast lighter; uncomputable → `unknown`. Validation: server-side. |
| Failure conditions | Ledger unavailable, partial section, stale. UI: `ERR-03`/`ERR-11`; `ST-14`/`ST-06`. |
| Idempotency and concurrency | Read-only. Freshness: as-of turn; no optimistic totals. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed; recovery refresh. |
| Audit, privacy, notification | Audit: none for own read; privileged read audited. Privacy: own balances only; alliance aggregates k=5. Notification: settlement digest. |
| Traceability and dependencies | Screens: `SCR-029`…`SCR-031`, `SCR-057`. Flows: `FLOW-005`. Requirements: `REQ-898`…`REQ-900`, `REQ-982/999/1000`. Test: `UAT-I-005`. Dependency: production security obligation (treasury write defect) does not affect this read contract but blocks any future write path. |

### UIX-09 — Production policy and manual orders

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-09`; Production policy/manual order; changes standing policy or submits a one-shot production order. |
| Parties and authority | Provider: B-04 economy; B-02 P3.3–P4. Consumer: `SCR-032`, `SCR-044`. Authority: ECN-044/045/049/053/139; D-053. Status: `SPECIFIED`. |
| Trigger and preconditions | Save policy; submit manual order. Preconditions: authenticated; nation active; political state permits. |
| Authentication and authorization | Authentication: session. Authorization: owner. Permissions: none shared. |
| Request/command | Policy mode `RUN_AT_CAPACITY`/`RUN_TO_TARGET`/`IDLE`; batch selection; quantities. Constraints: affordability, capacity, space, power; whole-batch. |
| Response and result | Policy effective at recurring phase; order reserved and executed atomically; named failure factor. Validation: preview at submit. |
| Failure conditions | Insufficient funds/inputs/capacity, overbooking, blocked by state. UI: `ERR-14`/`ERR-17`/`ERR-13`; `ST-11`/`ST-14`. |
| Idempotency and concurrency | One order per confirmation; policy last-write-wins; no double reservation. Freshness: re-read before retry. |
| Retry, timeout, offline, recovery | Retry after reconciliation; offline writes disabled; recovery via `SCR-032`. |
| Audit, privacy, notification | Audit: order/policy records. Privacy: own nation. Notification: result in digest; failure inline. |
| Traceability and dependencies | Screens: `SCR-032`, `SCR-033`, `SCR-044`. Flows: `FLOW-009`, `FLOW-010`. Requirements: `REQ-901`, `REQ-1111/1112`. Test: `UAT-I-006`. Dependency: server-authoritative production path (Stage 5/6). |

### UIX-10 — Resources, warehouse and power

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-10`; Resource/warehouse/power read; shows triple balances, capacity and derived power. |
| Parties and authority | Provider: B-04/B-05. Consumer: `SCR-033`, `SCR-034`, `SCR-044`. Authority: MKT-053; ECN-120/147; URB-052/066; D-048. Status: `SPECIFIED`. |
| Trigger and preconditions | Open resources/power; open chain. Preconditions: authenticated. |
| Authentication and authorization | Authentication: session. Authorization: owner; alliance aggregate k=5 if ever shown. Permissions: read-only. |
| Request/command | Read every resource triple, warehouse capacity/holdings/value, power supply/demand/`power_pct`. Constraints: capacity not a resource; power not stored. |
| Response and result | Triple, capacity bar, derated/unmaintained state, empty/new-nation state. Validation: server-side. |
| Failure conditions | Partial, suppressed aggregate, unavailable section. UI: `ERR-03`; `ST-06`/`ST-14`. |
| Idempotency and concurrency | Read-only. Freshness: as-of. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed. |
| Audit, privacy, notification | Audit: none. Privacy: own data; alliance aggregate suppressed below k=5. Notification: none. |
| Traceability and dependencies | Screens: `SCR-033`, `SCR-034`, `SCR-044`. Flows: `FLOW-010`. Requirements: `REQ-902/903`, `REQ-1002`. Test: `UAT-I-006`. Dependency: capacity semantics fixed by D-048. |

### UIX-11 — City construction and demolition

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-11`; City construction/demolition; claims the single city slot with a full preview. |
| Parties and authority | Provider: B-05 cities. Consumer: `SCR-041`…`SCR-043`. Authority: URB-064/071/148; D-073/D-074. Status: `SPECIFIED`. |
| Trigger and preconditions | Confirm construction/demolition. Preconditions: city ownership; slot free; cost affordable. |
| Authentication and authorization | Authentication: session. Authorization: owner. Permissions: owner only. |
| Request/command | Building/upgrade/demolition selection, target city. Constraints: one construction-class action per city per turn; 25% crown-only refund; DC limits. |
| Response and result | Slot claimed at acceptance; preview (cost after discounts, DC, availability, book value, wealth effect); demolition refund. Validation: server-side. |
| Failure conditions | Slot occupied, cost/DC invalid, rule block. UI: `ERR-13`/`ERR-14`/`ERR-16`; `ST-11`. |
| Idempotency and concurrency | One slot per city; concurrent orders yield one acceptance and one `ST-13`. Freshness: re-read city before retry. |
| Retry, timeout, offline, recovery | Retry after re-read; offline disabled; recovery via city detail. |
| Audit, privacy, notification | Audit: city action records. Privacy: own city. Notification: completion at boundary. |
| Traceability and dependencies | Screens: `SCR-042`, `SCR-043`. Flows: `FLOW-014`. Requirements: `REQ-911/912`, `REQ-1116`. Test: `UAT-I-007`. Dependency: none beyond B-05. |

### UIX-12 — City founding

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-12`; City founding; creates a new city under cost, infrastructure and expansion-slot gates. |
| Parties and authority | Provider: B-05. Consumer: `SCR-046`. Authority: URB-032–034; D-068. Status: `SPECIFIED`. |
| Trigger and preconditions | Confirm founding. Preconditions: national infrastructure threshold; crowns and 20 steel; expansion slot; 12-city bound. |
| Authentication and authorization | Authentication: session. Authorization: owner. Permissions: owner only. |
| Request/command | City name/identity and confirmation. Constraints: no cooldown invented; cost/steel/space gates. |
| Response and result | New city in starting state; resources deducted; slot consumed. Validation: server-side. |
| Failure conditions | Gate unmet, insufficient resources, bound reached. UI: `ERR-13`/`ERR-14`; `ST-11`. |
| Idempotency and concurrency | One city per confirmation; concurrent founding yields one city. Freshness: overview re-read. |
| Retry, timeout, offline, recovery | Uncertain outcome → re-read overview; never double-create. |
| Audit, privacy, notification | Audit: founding record. Privacy: own nation. Notification: boundary result. |
| Traceability and dependencies | Screens: `SCR-041`, `SCR-046`. Flows: `FLOW-015`. Requirements: `REQ-915`, `REQ-1117`. Test: `UAT-I-007`. Dependency: none. |

### UIX-13 — Research

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-13`; Research; reads the tree and starts one active project. |
| Parties and authority | Provider: B-05. Consumer: `SCR-045`. Authority: URB-093–097/102/150; D-076/D-077/D-078. Status: `SPECIFIED`. |
| Trigger and preconditions | Confirm research start. Preconditions: no active project; RP/crowns; prerequisite. |
| Authentication and authorization | Authentication: session. Authorization: owner. Permissions: owner only. |
| Request/command | Project selection. Constraints: one active project; banked RP vs programme spend; cost. |
| Response and result | Project started; progress at boundaries; completion. Validation: server-side. |
| Failure conditions | Active project, prerequisite, insufficient RP/crowns. UI: `ERR-13`/`ERR-14`/`ERR-16`; `ST-11`. |
| Idempotency and concurrency | One active project; concurrent starts yield one. Freshness: re-read tree. |
| Retry, timeout, offline, recovery | Retry after re-read; offline read-only. |
| Audit, privacy, notification | Audit: research records. Privacy: own nation. Notification: completion at boundary. |
| Traceability and dependencies | Screens: `SCR-045`. Flows: `FLOW-016`. Requirements: `REQ-914`, `REQ-1118`. Test: `UAT-I-008`. Dependency: none. |

### UIX-14 — Politics: policy, campaign and elections

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-14`; Politics; changes policy, submits campaign actions and reads election/crisis state. |
| Parties and authority | Provider: B-06 politics. Consumer: `SCR-021`…`SCR-028`. Authority: DMP-073/087/101/102/163/189/268; D-106/D-107/D-094. Status: `SPECIFIED`. |
| Trigger and preconditions | Change policy; submit campaign action; open state/result/crisis. Preconditions: authenticated; political state permits; cooldown/limit. |
| Authentication and authorization | Authentication: session. Authorization: owner. Permissions: owner only; no government-change control. |
| Request/command | Policy axis/value; campaign action type; recovery action. Constraints: one policy change per axis per 12 turns; three campaign types; charge once. |
| Response and result | Effect at resolution turn; campaign charge recorded; state/banner updates. Validation: server-side. |
| Failure conditions | Cooldown, insufficient charge, state block. UI: `ERR-13`/`ERR-14`/`ERR-16`; `ST-11`. |
| Idempotency and concurrency | Policy one per axis per cooldown; campaign charge once; concurrent submits one acceptance. Freshness: re-read panel. |
| Retry, timeout, offline, recovery | Retry after re-read; offline read-only; recovery via panel. |
| Audit, privacy, notification | Audit: policy/campaign records. Privacy: own politics; public outcome. Notification: election result alert. |
| Traceability and dependencies | Screens: `SCR-021`…`SCR-028`. Flows: `FLOW-007`, `FLOW-008`. Requirements: `REQ-890`…`REQ-897`, `REQ-1109/1110`. Test: `UAT-I-008`. Dependency: D-107 anchor. |

### UIX-15 — Directed trade lifecycle

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-15`; Directed-trade lifecycle; creates revisions, accepts, counters, declines and cancels directed offers. |
| Parties and authority | Provider: B-07 markets + B-04 settlement + B-02 P4. Consumer: `SCR-035`…`SCR-037`. Authority: MKT-019–131; D-016/D-017; `INT-006`. Status: `SPECIFIED`. |
| Trigger and preconditions | Submit offer/counter/acceptance/decline/cancel. Preconditions: authenticated; named counterparty; lifecycle state permits. |
| Authentication and authorization | Authentication: session. Authorization: party to the chain; fresh-nation band checks. Permissions: parties only. |
| Request/command | Up to five resource/crown lines per side; counterparty; revision; acceptance. Constraints: no reservation at creation; 10 revisions; 72-turn expiry; one live per pair; rate limits. |
| Response and result | Chain/revision created; acceptance revalidates both sides; reserves crowns/resources/space; settles atomically at P4 with one `transfer_id`. Validation: server-side. |
| Failure conditions | Invalid terms, insufficient balance/space, stale revision, expired, one-live, band block. UI: `ERR-08`/`ERR-14`/`ERR-11`/`ERR-12`/`ERR-16`/`ERR-13`. |
| Idempotency and concurrency | One settlement per revision; one live offer per pair; duplicate acceptance returns original. Freshness: re-read both sides before confirm. |
| Retry, timeout, offline, recovery | Uncertain settlement → re-read offer; never auto-repeat; offline read-only. |
| Audit, privacy, notification | Audit: trade records and signals. Privacy: terms parties-only; no public per-trade feed. Notification: pending/expiry/settlement. |
| Traceability and dependencies | Screens: `SCR-035`…`SCR-037`, `SCR-040`. Flows: `FLOW-011`…`FLOW-013`. Requirements: `REQ-904`…`REQ-906`, `REQ-1113`…`REQ-1115`. Test: `UAT-I-009`. Dependency: idempotency key owned by B-07. |

### UIX-16 — Trade history and reference prices

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-16`; Trade history/reference read; pre-gate minimal own history only. |
| Parties and authority | Provider: B-07. Consumer: `SCR-040`. Authority: MKT-110/140; D-117; D-026. Status: `SPECIFIED` (pre-gate subset). |
| Trigger and preconditions | Open trade history. Preconditions: authenticated. |
| Authentication and authorization | Authentication: session. Authorization: own history; privileged views scoped. Permissions: read-only. |
| Request/command | Read own completed/cancelled/expired trades; post-gate statistics only if gate passed. Constraints: no statistic pre-gate; sample count required. |
| Response and result | Own history; `INSUFFICIENT_SAMPLE` named; retention labels. Validation: server-side. |
| Failure conditions | None beyond read failure. UI: `ERR-03`; `ST-14`. |
| Idempotency and concurrency | Read-only. Freshness: as-of. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed. |
| Audit, privacy, notification | Audit: none. Privacy: no public per-trade feed; own history only. Notification: none. |
| Traceability and dependencies | Screens: `SCR-040`. Flows: —. Requirements: `REQ-909`. Test: `UAT-I-009`. Dependency: D-117 gate. |

### UIX-17 — Diplomacy: proposal, agreement and publication

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-17`; Diplomacy; submits proposals, records acceptance/termination and exposes publication state. |
| Parties and authority | Provider: B-08 diplomacy. Consumer: `SCR-047`…`SCR-052`. Authority: DIP-023…132; D-030; `INT-007`. Status: `SPECIFIED`. |
| Trigger and preconditions | Submit/counter/withdraw proposal; accept; terminate; open publication. Preconditions: authenticated; named counterparty; state permits; notice precondition for hostile posture. |
| Authentication and authorization | Authentication: session. Authorization: nation owner only; no delegation. Permissions: parties only. |
| Request/command | Counterparty, type (`DP-T01`…`DP-T03`), terms, duration; acceptance; withdrawal; termination. Constraints: terms immutable; one live per direction; parties-only pending. |
| Response and result | Proposal recorded; acceptance recorded; activation/publication at boundary; expiry/termination. Validation: server-side. |
| Failure conditions | Invalid type, missing consent, stale state, duplicate, expiry, freeze. UI: `ERR-08`/`ERR-11`/`ERR-12`/`ERR-16`; `ST-11`. |
| Idempotency and concurrency | One live proposal per direction; one acceptance; replayed acceptance returns original. Freshness: re-read pair before confirm. |
| Retry, timeout, offline, recovery | Reconcile before retry; offline read-only; activation delayed not lost. |
| Audit, privacy, notification | Audit: diplomatic records. Privacy: pending terms parties-only; k=5 aggregates. Notification: proposal/activation/expiry. |
| Traceability and dependencies | Screens: `SCR-047`…`SCR-052`. Flows: `FLOW-017`, `FLOW-018`. Requirements: `REQ-916`…`REQ-921`, `REQ-1119/1120`. Test: `UAT-I-010`. Dependency: none. |

### UIX-18 — Alliance membership and governance

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-18`; Alliance membership/governance; applies, admits, changes roles and reads governance. |
| Parties and authority | Provider: B-09 alliances. Consumer: `SCR-053`…`SCR-055`. Authority: ALL-080–086; AX-01–05/09/10; D-133/D-135. Status: `SPECIFIED`; UD-040/044/045 open. |
| Trigger and preconditions | Apply/respond; change role/permission; read roster. Preconditions: authenticated; alliance exists; role permits. |
| Authentication and authorization | Authentication: session. Authorization: role matrix; applicant privacy. Permissions: role-scoped; officer cannot exceed grant authority. |
| Request/command | Application/invitation response; role assignment; constitution/role settings. Constraints: no permission escalation beyond own; one membership; applicant visible only to administration. |
| Response and result | Membership state; role set; application outcome terminating in-product. Validation: server-side. |
| Failure conditions | Role denied, one-alliance limit, application state, owner-reserved policy. UI: `ERR-06`/`ERR-11`/`ERR-13`; `ST-11`. |
| Idempotency and concurrency | One outcome per application; role change versioned; concurrent changes last-write wins with conflict warning. Freshness: re-read roster. |
| Retry, timeout, offline, recovery | Retry after re-read; offline read-only; recovery via alliance home. |
| Audit, privacy, notification | Audit: membership/role records. Privacy: applicant identities admin-only; aggregates k=5. Notification: application/role notice. |
| Traceability and dependencies | Screens: `SCR-053`…`SCR-055`. Flows: `FLOW-019`. Requirements: `REQ-922`…`REQ-924`, `REQ-1121`. Test: `UAT-I-011`. Dependencies: UD-040/044/045 remain owner-reserved. |

### UIX-19 — Alliance tax brackets and ARL

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-19`; Alliance tax/ARL; changes versioned brackets and reads receipts/available/reserved/expended. |
| Parties and authority | Provider: B-09 + B-04; B-02 P3. Consumer: `SCR-056`, `SCR-057`. Authority: ALL-179–193/220–226; AX-27/AX-28; D-141; `INT-003`. Status: `SPECIFIED`; UD-040/046 open. |
| Trigger and preconditions | Save bracket; open finances. Preconditions: tax-management permission; integer rates; member reading. |
| Authentication and authorization | Authentication: session. Authorization: role-based tax management; ARL read by member/officer. Permissions: no general withdrawal. |
| Request/command | Bracket name, Crowns/resource rates in integer basis points 0–10,000, member assignment, effective turn. Constraints: ≤100%; per-asset; versioned policy. |
| Response and result | New policy version; effective turn; per-turn receipts; four ARL categories; visible 0% fallback while UD-040 open. Validation: server-side. |
| Failure conditions | Invalid bp, role denied, attribution ambiguity (0% fallback), missing cost schedule. UI: `ERR-08`/`ERR-06`/`ERR-13`; `ST-11`. |
| Idempotency and concurrency | Versioned policy; one effective version per turn; per-turn tax effective once. Freshness: re-read before change. |
| Retry, timeout, offline, recovery | Retry after re-read; offline read-only; receipts immutable. |
| Audit, privacy, notification | Audit: tax and ARL records. Privacy: member values not shown; aggregates k=5. Notification: receipt at boundary. |
| Traceability and dependencies | Screens: `SCR-056`, `SCR-057`. Flows: `FLOW-020`. Requirements: `REQ-925`…`REQ-927`, `REQ-1027/1028`, `REQ-1122`. Test: `UAT-I-011`. Dependencies: UD-040/045/046; no spendable purpose. |

### UIX-20 — Alliance treaty objects

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-20`; Alliance-to-alliance treaties; creates record-only or NAP-effect objects with recorded per-nation consent. |
| Parties and authority | Provider: B-09. Consumer: `SCR-058`. Authority: AX-29/AX-30; D-140; AT-E00/E01. Status: `SPECIFIED`; UD-047 open. |
| Trigger and preconditions | Propose/accept/terminate alliance treaty. Preconditions: role authority; counterparty alliance; recorded consent set. |
| Authentication and authorization | Authentication: session. Authorization: alliance role; no delegation of national sovereignty. Permissions: role-scoped; no collective military command. |
| Request/command | Treaty type `AT-T01`…`AT-T05`; effect class `AT-E00`/`AT-E01`; counterparty; coverage consents. Constraints: AT-T01 cannot be record-only; custom prose never executes. |
| Response and result | Treaty object; coverage set; non-covered members marked; NAP block effect where applicable. Validation: server-side. |
| Failure conditions | Unregistered type, missing consent, role denied, UD-047 policy. UI: `ERR-08`/`ERR-06`/`ERR-13`. |
| Idempotency and concurrency | One live treaty per pair/type; dissolution ends whole; versioned terms. Freshness: re-read. |
| Retry, timeout, offline, recovery | Retry after re-read; offline read-only. |
| Audit, privacy, notification | Audit: treaty and consent records. Privacy: private terms not exposed. Notification: proposal/activation. |
| Traceability and dependencies | Screens: `SCR-058`. Flows: —. Requirements: `REQ-927`. Test: `UAT-I-011`. Dependency: UD-047. |

### UIX-21 — Military operations and war declaration

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-21`; Military operations/declaration; submits owner-only operations and declares war with OP/resource cost. |
| Parties and authority | Provider: B-10 warfare. Consumer: `SCR-061`. Authority: WAR-039–053/148–152; D-015 (10B-C3); `INT-009`. Status: `SPECIFIED`. |
| Trigger and preconditions | Submit operation; declare war. Preconditions: nation owner; OP/readiness/resources; valid target; no NAP/protection/Alliance block. |
| Authentication and authorization | Authentication: session. Authorization: nation owner only; no alliance path. Permissions: owner only. |
| Request/command | Operation type, target, objective; declaration. Constraints: OP cost/reservation; 2 OP + 500 crowns for declaration; outgoing slot; WAR-152 confirmation. |
| Response and result | Operation queued/reserved; declaration campaign created/public record. Validation: twelve-check WAR validator at submission, P2, pre-P5 where applicable. |
| Failure conditions | OP/readiness insufficient, block (protection/NAP/Alliance/political), slot, cost. UI: `ERR-13`/`ERR-14`; `WRF` family. |
| Idempotency and concurrency | Reservation at acceptance; one operation per confirmation; one live campaign. Freshness: re-read board. |
| Retry, timeout, offline, recovery | Uncertain outcome → re-read board; never auto-repeat; offline disabled. |
| Audit, privacy, notification | Audit: `WRA` events. Privacy: owner-only exact values. Notification: operation result/war event. |
| Traceability and dependencies | Screens: `SCR-061`, `SCR-059`, `SCR-063`. Flows: `FLOW-021`, `FLOW-022`. Requirements: `REQ-930/1032/1033/1039`, `REQ-1123/1124`. Test: `UAT-I-012`. Dependencies: OP cap provisional (Prompt 14). |

### UIX-22 — Settlement and surrender

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-22`; Settlement/surrender; records one live settlement or ends a campaign by surrender. |
| Parties and authority | Provider: B-10. Consumer: `SCR-067`. Authority: WAR-122–132; UD-032 Option A. Status: `SPECIFIED`. |
| Trigger and preconditions | Propose/accept/withdraw settlement; confirm surrender. Preconditions: party; campaign state; owner for surrender. |
| Authentication and authorization | Authentication: session. Authorization: party/owner. Permissions: parties; surrender owner-only. |
| Request/command | Settlement terms, duration, acceptance/withdrawal; surrender confirmation. Constraints: one live settlement; silence is not consent; surrender always available. |
| Response and result | Settlement recorded; campaign end; limited-victory consequence; terms visible. Validation: server-side. |
| Failure conditions | Stale settlement, already accepted, expired, campaign ended. UI: `ERR-11`/`ERR-12`/`ERR-16`. |
| Idempotency and concurrency | One live settlement; one acceptance; one surrender. Freshness: re-read war detail. |
| Retry, timeout, offline, recovery | Retry after re-read; offline disabled; recovery via war detail. |
| Audit, privacy, notification | Audit: `WRA` settlement events. Privacy: terms parties-only until publication. Notification: settlement/surrender. |
| Traceability and dependencies | Screens: `SCR-067`, `SCR-063`. Flows: `FLOW-023`, `FLOW-024`. Requirements: `REQ-936`, `REQ-1125/1126`. Test: `UAT-I-012`. Dependency: UD-032 resolved model. |

### UIX-23 — War, battle and visibility read

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-23`; War/battle read; serves campaigns, reports, losses and history filtered by viewer class. |
| Parties and authority | Provider: B-10; B-11 history. Consumer: `SCR-059`…`SCR-066`. Authority: WAR-085–088/109k/150; D-026. Status: `SPECIFIED`. |
| Trigger and preconditions | Open military surfaces; open battle/war detail. Preconditions: authenticated/public as applicable. |
| Authentication and authorization | Authentication: session or public. Authorization: field-level visibility; owner/participant scopes. Permissions: read-only. |
| Request/command | Read wars, operations, battles, losses, readiness bands. Constraints: four bands only; exact values owner-only. |
| Response and result | Public summary or participant record; band; loss groups; retention. Validation: server-side. |
| Failure conditions | Denied field, restricted record, stale. UI: `ERR-06`/`ERR-11`; `ST-09`/`ST-03`. |
| Idempotency and concurrency | Read-only. Freshness: as-of turn. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed. |
| Audit, privacy, notification | Audit: privileged reads where required. Privacy: no exact strength to non-owner; no private operation. Notification: battle events. |
| Traceability and dependencies | Screens: `SCR-059`…`SCR-066`. Flows: `FLOW-023` (read). Requirements: `REQ-928/929/931`…`REQ-935`, `REQ-1034/1035/1074/1075`. Test: `UAT-I-012`. Dependency: none. |

### UIX-24 — World events, objectives and standings

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-24`; World read; serves events, objectives, standings and progress with cause/consequence and denominators. |
| Parties and authority | Provider: B-11. Consumer: `SCR-069`…`SCR-076`, `SCR-018`. Authority: WEP-179/203–215/324–362/619–633; `WPC-01`–`WPC-10`. Status: `SPECIFIED`. |
| Trigger and preconditions | Open world surfaces; open event/objective. Preconditions: authenticated/public as applicable. |
| Authentication and authorization | Authentication: session or public. Authorization: publication rules; k=5. Permissions: read-only. |
| Request/command | Read events, objectives, standings, progress, chronicle. Constraints: registered effects only; denominator/window; no live tick. |
| Response and result | Event with cause/effect; objective state; standing with denominator; progress layers. Validation: server-side. |
| Failure conditions | Suppressed, unavailable, stale. UI: `ERR-03`; `ST-06`/`ST-14`. |
| Idempotency and concurrency | Read-only. Freshness: computed/publish turn. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed. |
| Audit, privacy, notification | Audit: event records. Privacy: k=5; no restricted fact through counts. Notification: event/standing. |
| Traceability and dependencies | Screens: `SCR-069`…`SCR-076`, `SCR-018`. Flows: `FLOW-005`. Requirements: `REQ-938`…`REQ-945`, `REQ-1040`…`REQ-1045`, `REQ-1099`. Test: `UAT-I-013`. Dependency: k=5 evidence for `SCR-077`. |

### UIX-25 — Reward and achievement claims

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-25`; Reward claim; reads earned/deferred rewards and submits a permitted claim. |
| Parties and authority | Provider: B-11. Consumer: `SCR-073`, `SCR-075`. Authority: WEP-240/499/582/663/705; `WPC-03`. Status: `SPECIFIED`. |
| Trigger and preconditions | Claim deferred reward. Preconditions: authenticated; claim eligible and visible. |
| Authentication and authorization | Authentication: session. Authorization: account/nation eligibility. Permissions: own claims only. |
| Request/command | Claim request. Constraints: one claim per grant; effective once. |
| Response and result | Claim state; granted/deferred/voided; material notice with class/quantity/owner key. Validation: server-side. |
| Failure conditions | Expired, already claimed, not eligible. UI: `ERR-11`/`ERR-12`/`ERR-16`. |
| Idempotency and concurrency | One claim per grant; duplicate returns original. Freshness: re-read reward list. |
| Retry, timeout, offline, recovery | Retry after re-read; offline read-only. |
| Audit, privacy, notification | Audit: reward records. Privacy: no other nation's reward. Notification: grant notice. |
| Traceability and dependencies | Screens: `SCR-073`, `SCR-075`. Flows: `FLOW-026`. Requirements: `REQ-942/944`, `REQ-1128`. Test: `UAT-I-013`. Dependency: Prompt 14 calibration for "rare" bound. |

### UIX-26 — Player protection: report, appeal, restriction

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-26`; Protection; renders exact report intake, case status, appeal and own restriction state. |
| Parties and authority | Provider: B-12; B-03 state. Consumer: `SCR-081`…`SCR-084`, `SCR-086`, `SCR-087`, `SCR-089`. Authority: MOD-002/013/015/017/018/027; NET-023/050; PRV-019; `INT-001`/`INT-002`/`INT-017`/`INT-018`. Status: `SPECIFIED`. |
| Trigger and preconditions | Submit report/appeal; open status/restriction/support. Preconditions: authenticated; report intake available; appeal route always available. |
| Authentication and authorization | Authentication: session. Authorization: reporter only; own restriction state; appeal route never blocked. Permissions: own case read. |
| Request/command | Report fields (category, subject, time window, reporter account, free text, supplied evidence); appeal grounds. Constraints: exact MOD-002 fields; no additional mandatory field. |
| Response and result | Acknowledgement with case reference; status ladder; decision notice with seven elements; restriction kind/scope/end/review. Validation: server-side. |
| Failure conditions | Intake unavailable (retryable), invalid field, case not found/denied, appeal window. UI: `ERR-03`/`ERR-08`/`ERR-07`/`ERR-12`; `ST-14`/`ST-08`/`ST-09`. |
| Idempotency and concurrency | One case per submission; one appeal per action; duplicate returns original. Freshness: re-read case. |
| Retry, timeout, offline, recovery | Retryable intake; offline read-only; appeal branch preserved during restriction. |
| Audit, privacy, notification | Audit: case and appeal records. Privacy: no third-party data, method or threshold. Notification: non-opt-out decision notice. |
| Traceability and dependencies | Screens: `SCR-081`…`SCR-084`, `SCR-086`, `SCR-087`, `SCR-089`. Flows: `FLOW-028`, `FLOW-029`. Requirements: `REQ-950`…`REQ-956`, `REQ-953/958`, `REQ-1130/1131`. Test: `UAT-I-014`. Dependencies: UD-053/059; staffing/legal posture. |

### UIX-27 — Account settings, closure and data

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-27`; Account settings; changes privacy/security settings, requests closure or export, and shows retention. |
| Parties and authority | Provider: B-03/B-12. Consumer: `SCR-011`, `SCR-012`, `SCR-079`, `SCR-080`, `SCR-085`. Authority: ACC-031/043; PRV-001/002/009/014/023; D-026/D-041. Status: `SPECIFIED`. |
| Trigger and preconditions | Save settings; request/cancel closure; request export. Preconditions: authenticated; cooling/retention rules. |
| Authentication and authorization | Authentication: session; step-up for sensitive changes. Authorization: own account. Permissions: own data only. |
| Request/command | Privacy toggles, session revocation, e-mail change, closure request/cancel, export request. Constraints: no SEC class exposure; closure cooling 7 days; no shield. |
| Response and result | Setting saved; closure cooling/restored; export request state; retention disclosure. Validation: server-side. |
| Failure conditions | Re-auth required, cooling not cancellable, export unavailable. UI: `ERR-04`/`ERR-13`/`ERR-03`. |
| Idempotency and concurrency | One closure request; cancel idempotent; setting last-write-wins. Freshness: re-read account home. |
| Retry, timeout, offline, recovery | Retry; offline read-only; recovery via account home. |
| Audit, privacy, notification | Audit: account/security events. Privacy: nine classes; SEC never rendered. Notification: closure/export notices. |
| Traceability and dependencies | Screens: `SCR-011`, `SCR-012`, `SCR-079`, `SCR-080`, `SCR-085`. Flows: `FLOW-030`. Requirements: `REQ-880/881/948/949/954`, `REQ-1132`, `REQ-1076/1077`. Test: `UAT-I-014`. Dependencies: UD-017/055; Stage 5 storage. |

### UIX-28 — Admin moderation, case and sanctions

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-28`; Admin moderation; queues cases, records evidence and applies sanctions within role/tier. |
| Parties and authority | Provider: B-12 + B-03 outcome. Consumer: `SCR-091`…`SCR-095`. Authority: ADM-003/012/021/022; MOD-022/036/037/042; EVD; `INT-001`–`INT-014`. Status: `SPECIFIED`. |
| Trigger and preconditions | Open queue/case; record decision; apply sanction step. Preconditions: ADM role; assigned case; two-person where required. |
| Authentication and authorization | Authentication: session + step-up where required. Authorization: role/tier; separation of duties. Permissions: least privilege; no superuser. |
| Request/command | Case assignment, finding, evidence reference, sanction tier/step, notice. Constraints: no balance typing; no direct nation mutation; two-person rule. |
| Response and result | Decision record; B-03 applies account state; correction via `INT-003`; audit row. Validation: server-side. |
| Failure conditions | Role denied, tier exceeded, second review missing, stale case. UI: `ERR-06`/`ERR-13`/`ERR-11`; `FR` postures. |
| Idempotency and concurrency | One decision per case step; two-person approval idempotent; conflict on concurrent review. Freshness: re-read case. |
| Retry, timeout, offline, recovery | Retry after re-read; offline disabled; recovery via queue. |
| Audit, privacy, notification | Audit: mandatory spine; every privileged read audited. Privacy: SEC scoped; no third-party exposure. Notification: notice queued/digested. |
| Traceability and dependencies | Screens: `SCR-091`…`SCR-095`, `SCR-100`. Flows: `FLOW-032`. Requirements: `REQ-960`…`REQ-964`, `REQ-1102/1134`, `REQ-1080`. Test: `UAT-I-015`. Dependencies: audit spine implementation (`GAP-13D-06`); UD-053/056. |

### UIX-29 — Admin audit, turn operations, data and roles

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-29`; Admin operations; exposes audit ledger, turn recovery, data operations and role management. |
| Parties and authority | Provider: B-02 + B-12. Consumer: `SCR-096`…`SCR-098`, `SCR-100`. Authority: TR-035/043/075/080/090; EVD-026/030; D-026/D-042; ADM-003. Status: `SPECIFIED`; audit verification `BLOCKED`. |
| Trigger and preconditions | Open audit/turn/data/roles; recovery action; preservation operation; role grant. Preconditions: specific role; purpose; step-up. |
| Authentication and authorization | Authentication: session + step-up. Authorization: `R-AUD`/`R-OPS`/`R-SEC`; least privilege. Permissions: no role grant beyond own. |
| Request/command | Audit query, recovery action, retention/preservation operation, role assignment. Constraints: no content bodies/secrets; destructive action confirmed; no irreversible claim when not reversible. |
| Response and result | Audit rows; recovery state; operation record; role set. Validation: server-side. |
| Failure conditions | Denied scope, audit unavailable, operation unsafe, role escalation. UI: `ERR-06`/`ERR-03`/`ERR-13`. |
| Idempotency and concurrency | Recovery one per boundary; preservation idempotent; role change versioned. Freshness: re-read. |
| Retry, timeout, offline, recovery | Retry after re-read; offline disabled; operator recovery path. |
| Audit, privacy, notification | Audit: every access recorded. Privacy: no secrets; retention classes. Notification: operational notices. |
| Traceability and dependencies | Screens: `SCR-096`…`SCR-098`, `SCR-100`. Flows: — (admin flows deferred; see `GAP-13D-03`). Requirements: `REQ-965`…`REQ-967`, `REQ-969`, `REQ-1080`. Test: `UAT-I-015`. Dependencies: audit digest/trigger/verification job; 0005 migration; SQL tests. |

### UIX-30 — Announcements and change disclosure

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-30`; Announcements/changes; publishes authorized global notices and dated rule/security changes. |
| Parties and authority | Provider: B-12; B-11 chronicle. Consumer: `SCR-088`, `SCR-099`. Authority: MOD-017/018; ALL-164; TR-049. Status: `SPECIFIED`. |
| Trigger and preconditions | Publish announcement; open changes. Preconditions: authorized role; content limits. |
| Authentication and authorization | Authentication: session. Authorization: announcement role; public read. Permissions: publish only within role. |
| Request/command | Notice scope, bounded content, effective date. Constraints: no private case data, detection method or another player; content limits. |
| Response and result | Publication record; dated change entry; global notice. Validation: server-side. |
| Failure conditions | Role denied, content invalid. UI: `ERR-06`/`ERR-08`. |
| Idempotency and concurrency | One publication per confirmation; duplicate suppressed. Freshness: re-read. |
| Retry, timeout, offline, recovery | Retry; offline read-only. |
| Audit, privacy, notification | Audit: publication record. Privacy: bounded content. Notification: global notice where authorized. |
| Traceability and dependencies | Screens: `SCR-088`, `SCR-099`. Flows: —. Requirements: `REQ-957/968`. Test: `UAT-I-016`. Dependency: UD-049 (announcement scope) remains owner-reserved. |

### UIX-B01 — Global Trade board and execution (absence contract)

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-B01`; Global Trade absence; guarantees that no board, listing, preview or statistic exists before G-1…G-6 all pass. |
| Parties and authority | Provider: none until gate. Consumer: `SCR-038`, `SCR-039`. Authority: D-117/D-122; MKT-073–077; G-1…G-6. Status: **`BLOCKED`**. |
| Trigger and preconditions | A user reaches the route or an old link. Preconditions: none; gate unmet. |
| Authentication and authorization | Authentication: n/a. Authorization: none. Permissions: none. |
| Request/command | No request; no command; no data. Constraints: no stub, teaser, beta board, partial listing or leaked statistic. |
| Response and result | Honest absence (`MKT-G01` explanation) and return path. Validation: route absent, not partially rendered. |
| Failure conditions | None; absence is the specified behaviour. UI: `ST-10`. |
| Idempotency and concurrency | N/A. Freshness: N/A. |
| Retry, timeout, offline, recovery | Return/leave. |
| Audit, privacy, notification | No audit event; no data. |
| Traceability and dependencies | Screens: `SCR-038`, `SCR-039`. Flows: none. Requirements: `REQ-907/908`. Test: `UAT-I-016`. Dependency: G-1…G-6. |

### UIX-B02 — Strategic intelligence (absence contract)

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-B02`; Intelligence absence; guarantees no intelligence surface, simulated report or espionage action exists without a rule. |
| Parties and authority | Provider: none. Consumer: `SCR-068` (placeholder only). Authority: B-10 espionage exclusion; `13A-OQ-010`. Status: **`BLOCKED`**. |
| Trigger and preconditions | None; route is not linked. |
| Authentication and authorization | N/A. |
| Request/command | No request; no command; no data. Constraints: no placeholder data, simulation or action. |
| Response and result | No route; no content; documentation placeholder only. |
| Failure conditions | N/A. |
| Idempotency and concurrency | N/A. |
| Retry, timeout, offline, recovery | N/A. |
| Audit, privacy, notification | None. |
| Traceability and dependencies | Screens: `SCR-068`. Flows: none. Requirements: `REQ-937`. Test: `UAT-I-016`. Dependency: future owner-authorized B-10 rule. |

### UIX-P01 — Pinned objects/favorites (provisional absence)

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-P01`; Favorites absence; no pin list until the fair-play review closes. |
| Parties and authority | Provider: none. Consumer: `SCR-020`. Authority: `13A-OQ-012`; `REQ-889`. Status: **`PROVISIONAL`** (absent). |
| Trigger and preconditions | None; screen and route absent. |
| Authentication and authorization | N/A. |
| Request/command | No request; no command; no stored pins. |
| Response and result | Absence; no visibility leakage. |
| Failure conditions | N/A. |
| Idempotency and concurrency | N/A. |
| Retry, timeout, offline, recovery | N/A. |
| Audit, privacy, notification | None. |
| Traceability and dependencies | Screens: `SCR-020`. Flows: none. Requirements: `REQ-889`. Test: `UAT-I-016`. Dependency: `13A-OQ-012`. |

### UIX-P02 — World Health aggregates (provisional read)

| Group | Specification |
|---|---|
| Identity and purpose | `UIX-P02`; World Health; per-figure k=5 aggregates only. |
| Parties and authority | Provider: B-11. Consumer: `SCR-077`. Authority: D-027; WEP-663. Status: **`PROVISIONAL`**. |
| Trigger and preconditions | Open world health where the gate passes. Preconditions: each figure passes k=5. |
| Authentication and authorization | Authentication: session. Authorization: public/aggregate rules. Permissions: read-only. |
| Request/command | Read figures and suppression states. Constraints: no pre-gate chart, placeholder axis or inferred total. |
| Response and result | Figure or suppressed state with complementary suppression. Validation: server-side. |
| Failure conditions | Insufficient sample → named state. UI: `ST-06`; `ERR-03`. |
| Idempotency and concurrency | Read-only. Freshness: as-of. |
| Retry, timeout, offline, recovery | Retry; offline last confirmed. |
| Audit, privacy, notification | Privacy: k=5. Audit: none. Notification: none. |
| Traceability and dependencies | Screens: `SCR-077`. Flows: none. Requirements: `REQ-946`. Test: `UAT-I-016`. Dependency: population evidence. |

---

## 6. Failure taxonomy and UI treatment

| Failure family | Contract examples | UI state | Message obligation |
|---|---|---|---|
| Session/auth (`ERR-04`, `ERR-05`) | `UIX-01`, `UIX-02` | `ST-12`/`ST-11` | Re-auth or verify; destination preserved |
| Authorization/ownership (`ERR-06`, `ERR-07`, `ERR-20`) | All role surfaces | `ST-09` | Restriction class; allowed route; no protected disclosure |
| Validation (`ERR-08`, `ERR-09`, `ERR-14`) | All writes | `ST-08`/`ST-11` | Field-linked correction or exact limiting factor |
| Stale/conflict (`ERR-11`, `ERR-13`, `ERR-16`) | Trade, politics, diplomacy, war, alliances | `ST-13`/`ST-11` | Changed since load / specific block / existing live object |
| Expiry (`ERR-12`) | Offers, proposals, settlements, objectives, verification | `ST-12` | What survives; new request route |
| Duplicate (`ERR-10`) | All committing | `ST-13`/`ST-07` | Already recorded; view original |
| Capacity/resource (`ERR-14`, `ERR-15`, `ERR-17`) | Production, construction, trade, military | `ST-11`/`ST-14` | Exact limiting factor; reservation release |
| Network/timeout (`ERR-01`, `ERR-02`, `ERR-18`) | All | `ST-15`/`ST-17` | Read-only/unknown; reconcile; no auto-retry |
| Server/unexpected (`ERR-03`, `ERR-19`) | All | `ST-14` | Nothing published; support reference |
| Rule block (`ERR-13`) | Protection, NAP, Alliance, political, cooldown | `ST-11` | Rule class and next eligible condition |
| Turn interrupted (`ERR-18`) | `UIX-05`, `UIX-09`, `UIX-14`, `UIX-21` | `ST-17` | Delay, not lost turn |
| Privacy/visibility (`ERR-20`) | Object reads, admin | `ST-09` | Same restriction class across screens |

**Unknown response rule.** An unparseable response is never treated as success or as a clean failure. It renders `ERR-19` with “cannot confirm”, records no success, and offers support (`REQ-1160`).

---

## 7. Idempotency, duplicate and concurrency register

| Contract | Owning idempotency basis | Duplicate behaviour | Concurrency outcome |
|---|---|---|---|
| `UIX-02` | Verification token single-use; resend window | One account per submission | Concurrent registration → one account or neutral duplicate |
| `UIX-03` | Account/nation uniqueness; reroll confirmation | One nation; one reroll | Concurrent creation → one nation (`AC-03`) |
| `UIX-09` | Order confirmation; reservation | One order per confirmation | Second order sees capacity/reservation state |
| `UIX-11` | City slot | One construction-class action per city per turn | Second order → `ST-13`/one slot |
| `UIX-12` | Founding confirmation | One city per confirm | Concurrent founding → one city |
| `UIX-13` | One active project | Second start blocked | Concurrent start → one project |
| `UIX-14` | Policy cooldown; campaign charge-once | One policy per axis per 12 turns; one campaign action charge | Second submit → block/charge state |
| `UIX-15` | `transfer_id`; revision | One settlement per revision; one live pair offer | Stale revision → `ST-13` |
| `UIX-17` | One live proposal per direction | Replayed acceptance returns original | Concurrent accept → one activation |
| `UIX-18` | Application identity; role version | One outcome per application | Concurrent role change → conflict warning |
| `UIX-19` | Policy version; effective turn | One effective version per turn | Concurrent bracket save → last-write with conflict warning |
| `UIX-20` | Treaty pair/type | One live treaty per pair/type | Concurrent proposal → one live |
| `UIX-21` | OP reservation at acceptance | One operation per confirmation | Concurrent submit → one reservation |
| `UIX-22` | One live settlement | One acceptance | Concurrent accept → one settlement |
| `UIX-25` | Grant id | One claim per grant | Duplicate claim returns original |
| `UIX-26` | Case reference; appeal record | One case per submission; one appeal per action | Duplicate report coalesces |
| `UIX-28` | Case step; two-person approval | One decision per step | Concurrent review → conflict |
| `UIX-29` | Boundary recovery record; role version | One recovery per boundary | Concurrent role grant → version conflict |

**Backend dependency.** Where no key exists, the UI must reconcile before retry. This document does not invent a key, table or service (`REQ-1159`).

---

## 8. Retry, timeout, offline and recovery matrix

| Situation | Read contract | Write contract |
|---|---|---|
| Timeout | Retry safe; label stale | `ST-17` uncertain; re-read object; retry only after reconcile |
| Network loss | `ST-15`; last confirmed with as-of | Writes disabled; no queue |
| Session expiry | Re-auth; return to destination | Re-auth; unsaved safe input preserved only per D-232 default; revalidate terms |
| Boundary interrupted | `ST-17`; no invented settlement | Pending remains; operator recovery only |
| Partial system result | `ST-06`; named missing part | Not shown as success; reconcile |
| Conflicting update | `ST-13`; re-read | Re-read, then reapply if intended |
| Duplicate submission | N/A | Single-flight; duplicate returns original |
| Unknown response | `ST-14`/`ERR-19` | No success; support; no auto-retry |
| Reconnection | Refresh affected data; new as-of | Re-read object; surface conflict before resubmit |

**Offline doctrine.** Offline is read-only. No offline gameplay, no queued committing action, no simulated boundary (`REQ-1188`). Previously confirmed data remains visible only with its as-of turn (`REQ-1189`).

---

## 9. Audit, privacy and notification requirements

| Contract group | Audit obligation | Privacy obligation | Notification obligation |
|---|---|---|---|
| Identity/account (`UIX-01`…`UIX-04`, `UIX-27`) | Authentication, verification, creation, reroll, closure | No credential/token; nine privacy classes; SEC excluded | Security notices non-opt-out |
| Turn/system (`UIX-05`, `UIX-29`) | Turn ledger, recovery, privileged reads | Public turn facts only; no secrets | Boundary results via digest |
| Economy/cities (`UIX-08`…`UIX-13`) | Ledger, orders, construction, research | Own values; alliance aggregates k=5 | Settlement and completion |
| Politics (`UIX-14`) | Policy, campaign, election records | Own politics; public outcome | Result/crisis notices |
| Markets (`UIX-15`, `UIX-16`) | Trade records and signals | Terms parties-only; no public per-trade feed | Pending/expiry/settlement |
| Diplomacy (`UIX-17`) | Proposals, agreements, breach facts | Pending terms private; publication rules | Proposal/activation/expiry |
| Alliances (`UIX-18`…`UIX-20`) | Membership, role, tax, ARL, treaties | Member values protected; k=5 | Receipts, applications, treaties |
| Warfare (`UIX-21`…`UIX-23`) | `WRA` events, blocked actions | Exact values owner-only; four bands | Operations, battles, settlements |
| World (`UIX-24`, `UIX-25`) | Event and reward records | k=5; no composite leak | Events, standing, rewards |
| Fair play (`UIX-26`, `UIX-28`…`UIX-30`) | Mandatory audit spine; privileged reads | No third-party data, method, threshold or secret | Decision notices; appeal route always |
| Absence (`UIX-B01`, `UIX-B02`, `UIX-P01`, `UIX-P02`) | None | No data leak through absence | None |

**Production honesty.** The audit spine, digest chain, protective trigger and verification job are **specified but unimplemented** (`GAP-13D-06`). No contract in this document claims that they exist. `UIX-28`/`UIX-29` surface audit data only; they do not create tamper-evidence.

---

## 10. Provisional, blocked and dependency contracts

| Contract | Classification | Blocking condition | What is still specified |
|---|---|---|---|
| `UIX-06` | `SPECIFIED`; tier defaults `PROVISIONAL` | Player fatigue/comprehension study (`REQ-1183/1185`) | Event-only generation, non-opt-out preservation, deep links |
| `UIX-19` | `SPECIFIED`; owner-reserved policy | UD-040/045/046 | 0% fallback, four ARL categories, versioned rates |
| `UIX-26` | `SPECIFIED`; owner/legal dependencies | UD-053/055/059 | Intake fields, appeal route, notice elements |
| `UIX-B01` | **`BLOCKED`** | G-1…G-6 not met | Absence duty, explanation route |
| `UIX-B02` | **`BLOCKED`** | No intelligence rule | Absence duty, no placeholder |
| `UIX-P01` | **`PROVISIONAL`** (absent) | `13A-OQ-012` | Absence duty |
| `UIX-P02` | **`PROVISIONAL`** | Per-figure k=5 evidence | Suppression state |
| `UIX-03` | `SPECIFIED` | Reroll review signal frequency (D-039) | Exact-phrase confirmation, block list |
| `UIX-09`/`UIX-11`/`UIX-21` | `SPECIFIED` | Prompt 14 calibration of values | Structure, reservation, validation |
| `UIX-28`/`UIX-29` | `SPECIFIED`; audit `BLOCKED` | Audit trigger/digest/verification; 0005; SQL tests | Role scoping, two-person rule, audit readership |

---

## 11. Contract coverage matrix (Matrix H)

| UIX | Provider | Consumer surfaces | Permission | Key data | Test | Status |
|---|---|---|---|---|---|---|
| `UIX-01` | B-03/Stage 6 | Shell, `SCR-003`, `SCR-011` | Session | identity/session | `UAT-I-001` | SPECIFIED |
| `UIX-02` | B-03 | `SCR-002/004/005/006` | Public | account/verification | `UAT-I-002` | SPECIFIED |
| `UIX-03` | B-03/B-04 | `SCR-007/090` | Verified owner | nation/starting state | `UAT-I-003` | SPECIFIED |
| `UIX-04` | B-03 | `SCR-008/009/078` | Own account | tutorial state | `UAT-I-003` | SPECIFIED |
| `UIX-05` | B-02 | Shell/`SCR-013/016/097` | Session | turn/phase | `UAT-I-004` | SPECIFIED |
| `UIX-06` | B-02/B-11 | `SCR-013/014/019` | Session | events/notices | `UAT-I-004` | SPECIFIED |
| `UIX-07` | B-02…B-11 | `SCR-010/015/017/018/078` | Visibility class | object/aggregate | `UAT-I-005` | SPECIFIED |
| `UIX-08` | B-04/B-02 | `SCR-029/030/031/057` | Own nation | financial registers | `UAT-I-005` | SPECIFIED |
| `UIX-09` | B-04/B-02 | `SCR-032/044` | Owner | policy/order | `UAT-I-006` | SPECIFIED |
| `UIX-10` | B-04/B-05 | `SCR-033/034/044` | Owner | resources/power | `UAT-I-006` | SPECIFIED |
| `UIX-11` | B-05 | `SCR-041/042/043` | Owner | city/slot | `UAT-I-007` | SPECIFIED |
| `UIX-12` | B-05 | `SCR-046` | Owner | founding | `UAT-I-007` | SPECIFIED |
| `UIX-13` | B-05 | `SCR-045` | Owner | research | `UAT-I-008` | SPECIFIED |
| `UIX-14` | B-06 | `SCR-021`…`028` | Owner | politics | `UAT-I-008` | SPECIFIED |
| `UIX-15` | B-07/B-04/B-02 | `SCR-035/036/037` | Party | offer/settlement | `UAT-I-009` | SPECIFIED |
| `UIX-16` | B-07 | `SCR-040` | Own history | trade history | `UAT-I-009` | SPECIFIED |
| `UIX-17` | B-08 | `SCR-047`…`052` | Owner/party | proposal/agreement | `UAT-I-010` | SPECIFIED |
| `UIX-18` | B-09 | `SCR-053/054/055` | Role/member | membership/roles | `UAT-I-011` | SPECIFIED |
| `UIX-19` | B-09/B-04 | `SCR-056/057` | Tax role/member | bracket/ARL | `UAT-I-011` | SPECIFIED |
| `UIX-20` | B-09 | `SCR-058` | Role | alliance treaty | `UAT-I-011` | SPECIFIED |
| `UIX-21` | B-10 | `SCR-061` | Owner | OP/operation | `UAT-I-012` | SPECIFIED |
| `UIX-22` | B-10 | `SCR-067` | Party/owner | settlement/surrender | `UAT-I-012` | SPECIFIED |
| `UIX-23` | B-10/B-11 | `SCR-059`…`066` | Visibility | war/battle | `UAT-I-012` | SPECIFIED |
| `UIX-24` | B-11 | `SCR-069`…`076` | Visibility | events/standings | `UAT-I-013` | SPECIFIED |
| `UIX-25` | B-11 | `SCR-073/075` | Own claim | reward | `UAT-I-013` | SPECIFIED |
| `UIX-26` | B-12/B-03 | `SCR-081`…`089` | Reporter/own | report/appeal/status | `UAT-I-014` | SPECIFIED |
| `UIX-27` | B-03/B-12 | `SCR-011/012/079/080/085` | Own account | settings/closure/data | `UAT-I-014` | SPECIFIED |
| `UIX-28` | B-12/B-03 | `SCR-091`…`095/100` | Role/tier | case/sanction | `UAT-I-015` | SPECIFIED |
| `UIX-29` | B-02/B-12 | `SCR-096`…`098/100` | Scoped role | audit/turn/data/roles | `UAT-I-015` | SPECIFIED |
| `UIX-30` | B-12/B-11 | `SCR-088/099` | Authorized role | notice/change | `UAT-I-016` | SPECIFIED |
| `UIX-B01` | none | `SCR-038/039` | none | none | `UAT-I-016` | BLOCKED |
| `UIX-B02` | none | `SCR-068` | none | none | `UAT-I-016` | BLOCKED |
| `UIX-P01` | none | `SCR-020` | none | none | `UAT-I-016` | PROVISIONAL |
| `UIX-P02` | B-11 | `SCR-077` | Session | aggregates | `UAT-I-016` | PROVISIONAL |

**Coverage tally:** 34 contract entries — 29 SPECIFIED active, 2 BLOCKED absence, 2 PROVISIONAL, 1 SPECIFIED/PROVISIONAL mixed (`UIX-06`). Every contract has a provider/consumer declaration, a permission statement, a data statement and a corresponding acceptance test. 0 orphan contracts. 0 contracts without a screen.

---

## 12. Contract integrity statement

- No production endpoint, table, queue, job or schema is invented or named.
- No existing `INT-`, `AX-` or `WPC-` contract was duplicated, renumbered or semantically changed.
- Every write contract is server-authoritative; no UI render grants permission.
- Every committing contract names its duplicate/uncertainty basis or explicitly states that the owning system must supply one.
- Every contract preserves the nine privacy classes, the fair-play restrictions and the owner-reserved decisions.
- Statuses are design statuses: no contract is implemented, executed, tested at runtime or released.

---

*End of B-13D integration-contracts deliverable.*
