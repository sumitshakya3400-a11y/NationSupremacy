# B-13C companion — Player journey specifications

**Parent:** [B-13C](22_interaction_flows_and_player_experience.md) (authority, conventions, requirements, Matrices A–C/E–I).
**Created:** 2026-11-13 (Prompt 13C). **Status:** specification only; no screen, component, route, state store, API or gameplay exists.
**Scope:** the thirteen mandatory player journeys `JRN-A`…`JRN-M`, the thirty-three interaction flows `FLOW-001`…`FLOW-033`, and the twelve tutorials `TUT-01`…`TUT-12`.

**Reading rules.** (1) The parent §18.2 requirement register is authoritative; rows here cite requirements, they do not restate them. (2) Screen content is owned by the 13B screen companion; this document adds sequencing and state, never screen content. (3) A step saying "the server permits" never grants permission; every action remains server-authoritative. (4) Conditional/prohibited screens (`SCR-020/038/039/068/077`) appear in no active journey or flow, and no tutorial implies their availability. (5) Every flow resolves against the owning rule, never against an interface assumption.

---

## 1. Journey template

Every `JRN-` uses the ten-part template fixed by the Prompt 13C instruction:

| Part | Content |
|---|---|
| **A Journey identity** | ID, name, category, priority, related screens, related components, governing system specifications. |
| **B Starting conditions** | Player state, account state, nation state, permissions, preconditions. |
| **C Entry point** | Where the journey starts, what triggers it and how the player arrives. |
| **D Main sequence** | Ordered steps: player action, interface response, information presented, resulting state, next destination. |
| **E Alternative paths** | Optional actions, cancel paths, back navigation, restricted and conditional paths. |
| **F Failure paths** | Validation, permission, expiry, stale data, conflict, network and server failures. |
| **G Completion** | Successful result, confirmation, persistent record, updated screens, notifications, available next actions. |
| **H Recovery** | Retry behaviour, return behaviour, safe navigation and recovery after interruption. |
| **I Accessibility** | Keyboard interaction, screen-reader information, focus behaviour, error announcement and alternative presentation. |
| **J Requirements and evidence** | Related `REQ-`, `D-`, `DD-` identifiers, governing rules and unresolved dependencies. |

---

## 2. Journey index

| ID | Name | Category | Priority | Flows | Tutorials |
|---|---|---|---|---|---|
| `JRN-A` | Account and first-time player experience | Entry | P0 | `FLOW-001`…`FLOW-004` | `TUT-01`…`TUT-03` |
| `JRN-B` | Returning player experience | Entry/re-entry | P0 | `FLOW-002`, `FLOW-005`, `FLOW-006`, `FLOW-033` | `TUT-03`, `TUT-12` |
| `JRN-C` | National management | Routine | P0 | `FLOW-005`, `FLOW-006` | `TUT-02`, `TUT-03` |
| `JRN-D` | Economy and treasury | Routine | P0 | `FLOW-009`, `FLOW-010` | `TUT-04`, `TUT-06` |
| `JRN-E` | Trade | Transactional | P0 | `FLOW-011`…`FLOW-013` | `TUT-08` |
| `JRN-F` | Cities, infrastructure and research | Routine | P0 | `FLOW-014`…`FLOW-016` | `TUT-07` |
| `JRN-G` | Politics and domestic governance | Routine | P0 | `FLOW-007`, `FLOW-008` | `TUT-05` |
| `JRN-H` | Diplomacy and alliances | Transactional | P0 | `FLOW-017`…`FLOW-020` | `TUT-09` |
| `JRN-I` | Warfare and military | Consequential | P0 | `FLOW-021`…`FLOW-024` | `TUT-10` |
| `JRN-J` | World and progression | Progression | P1 | `FLOW-025`, `FLOW-026` | `TUT-11` |
| `JRN-K` | Notifications and player protection | Support | P0 | `FLOW-027`…`FLOW-029` | `TUT-12` |
| `JRN-L` | Account management | Account | P0 | `FLOW-030`, `FLOW-031` | — |
| `JRN-M` | Administrative | Admin | P0 | `FLOW-032` | — |

---

## 3. Player journey specifications

### JRN-A — Account and first-time player experience

**A. Journey identity.** ID `JRN-A`; category Entry; priority P0; screens `SCR-001`…`SCR-009`, `SCR-013`; components `UI-CMP-001`, `UI-CMP-005`, `UI-CMP-074`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-085`, `UI-CMP-088`, `UI-CMP-016`, `UI-CMP-065`; governing B-03, B-04 and B-11 onboarding surfaces.

**B. Starting conditions.** Unauthenticated visitor; no account; no nation; public reduced shell; public fields only. Registration requires a valid e-mail pair, password policy and terms acknowledgement; nation creation additionally requires a verified e-mail and an eligible account (D-029, NAT-001).

**C. Entry point.** Any unauthenticated URL lands on `SCR-001`; the `Start Playing` control opens `SCR-002`; `Login` opens `SCR-003`; a verification link opens `SCR-006`; a verified account with no nation may open `SCR-007`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-001` | Public reduced shell; premise and cadence statement | What the game is; browser-only; fictional world; rules/terms/privacy | Choose register or login |
| 2 | Registers on `SCR-002` (`FLOW-001`) | Inline validation; multi-account and verification notices | E-mail, password, referrer, terms; "verify before creating a nation" | Account `UNVERIFIED`; `SCR-006` |
| 3 | Verifies e-mail on `SCR-006` | Verification state and blocked-capability list | Verification gate; resend limit; change-e-mail route | Verified; `SCR-007` eligible |
| 4 | Creates nation on `SCR-007` (`FLOW-003`) | Name/short-name live feedback; start-state summary; confirmation | Name, short name, emblem, posture; 1,500 crowns, 50,000 people, 310 units; `awaiting first turn` | Nation created; `SCR-008` |
| 5 | Follows onboarding on `SCR-008` (`FLOW-004`) | Real shell with true zero-state; step card; skip | Why this step matters; real values; protection state | Step complete/skipped; `SCR-009` or `SCR-013` |
| 6 | Reviews first objectives on `SCR-009` | Objective entry set; optionality and penalty-free dismissal | Objective categories; progress; no obligation | `SCR-071` or `SCR-013` |
| 7 | Enters the digest on `SCR-013` | Digest, pending summary, turn strip | Since-last-look (empty on creation) and next boundary | First session complete; `JRN-C`/`JRN-B` |

**E. Alternative paths.** Recovery without a password uses `SCR-004` → `SCR-005` (single-use code). A wrong e-mail may be corrected through `SCR-006`/`SCR-080`. Nation creation can be cancelled before confirmation without creating anything. Onboarding can be skipped at any step; skipping never removes protection. A player may open the public guide `SCR-078` at any point.

**F. Failure paths.** Invalid/duplicate e-mail or weak password → `ST-08`, linked field message, input preserved. Terms unchecked → submit disabled with `OVL-03` reason. Unverified creation attempt → `ST-11` with D-029 explanation, not a generic error. Name unavailable/reserved → neutral D-038 message with no reserved-list disclosure. Creation conflict (concurrent request) → `ST-13` and a re-read; no duplicate nation (`AC-03`). Verification link expired → resend flow. Network failure → `ST-15`; nothing is created until a confirmed authoritative success.

**G. Completion.** A verified account owns exactly one active nation; the nation exists in `awaiting first turn` state; onboarding completion is recorded once per account; the digest is the home. Persistent records: account state, nation identity, founding turn, tutorial preference. No notification is generated by nation creation except the account/security record defined by B-03. Available next actions: review `SCR-009`, open `SCR-015`, read `SCR-078`, configure `SCR-080`.

**H. Recovery.** Interruption at registration leaves no account or leaves `UNVERIFIED` (resumable). Interruption after verification leaves the account without a nation; `SCR-007` remains reachable. Interruption during nation creation creates either the nation or nothing (`AC-03`); the player re-reads account home. A lost password uses `SCR-004`/`SCR-005`; a lost e-mail follows `SCR-004`/support without a promised identity-document path.

**I. Accessibility.** The entire first-session path is keyboard-operable; the form error summary receives focus on failed submission; the verification state is announced (`AXI-02`, `AXI-07`); nation name/short name fields have programmatic labels and text-linked errors; the start-state summary is readable before confirmation; the onboarding step heading receives focus after navigation; progress is announced once per step, not per tick.

**J. Requirements and evidence.** `REQ-1090`, `REQ-1103`…`REQ-1106`, `REQ-1172`…`REQ-1181`; D-029, D-038, D-040, D-041, D-063; ONB-004/009/013; ACC-023/024/031; NAT-001/005/026–030. Unresolved: custom SMTP verification is a deployment dependency (D-029); no implementation exists.

---

### JRN-B — Returning player experience

**A. Journey identity.** ID `JRN-B`; category Entry/re-entry; P0; screens `SCR-003`, `SCR-013`…`SCR-019`; components `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-069`, `UI-CMP-070`, `UI-CMP-021`; governing B-02 (TR-084/088/089), B-11 digest content.

**B. Starting conditions.** Verified account with an active nation; any absence length; any turn state (`OPEN`, `LOCKED`, `RESOLVING`, `COMPLETED`, `INTERRUPTED`, `FAILED`).

**C. Entry point.** Login (`SCR-003`) lands on `SCR-013`; a deep link may land on the owning screen and the shell shows the same digest context; the alert indicator opens `SCR-019`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Logs in (`FLOW-002`) | Session established; shell identity, countdown and alerts | Turn, boundary, account/nation state | `SCR-013` |
| 2 | Reads the digest (`FLOW-005`) | Bounded settled-change rows, pending totals, due items | What changed, cause chain, deep links; as-of turn | Choose an item |
| 3 | Reviews open decisions | Inbox summary and due boundary | Pending trade/proposal/invitation/settlement | `SCR-014` (`FLOW-006`) |
| 4 | Reviews national performance | Overview cards and warnings | Treasury triple, stability/approval, readiness, protection, population, power | Section screen |
| 5 | Identifies the next meaningful action | Owning screen shows allowed/blocked actions and reasons | Available actions, costs, confirmations | Act or defer |
| 6 | Returns to the digest | Context and as-of state preserved | Updated state after any confirmed action | Continue |

**E. Alternative paths.** A player may go directly to `SCR-019` for history, `SCR-016` for turn detail, `SCR-017` for chronicle, or any section root. A player may dismiss an ambient notification where permitted; non-opt-out items remain. A player may choose to take no action; the game imposes no attendance penalty.

**F. Failure paths.** Session expired → `ST-12`/re-auth; return to the same screen (`OFF-04`). Digest unavailable → `ST-14` with retry; the turn indicator remains. An object cited by a stale digest is retired/restricted → the owning state renders; the digest record remains (`FLOW-027`). Offline → `ST-15`; already-confirmed data remains labelled; no action can be submitted (`OFF-01`). Boundary `INTERRUPTED`/`FAILED` → named state; no invented outcome; accepted actions remain pending (TR-080).

**G. Completion.** The player has read what changed, seen the open decisions and knows the next action. The digest remains the durable record. Next actions: act on an inbox item, open a section, or leave. No reward is granted for returning; no "welcome back" bonus exists (D-021).

**H. Recovery.** The digest is regenerated from authoritative records on the next load. If the player returns after many turns, the digest groups missed turns and names still-open decisions (TR-084); no per-turn catch-up loop is created. A lost session is recovered without losing the intended destination.

**I. Accessibility.** Digest rows are a headed list with turn, cause and link; the count of changes is announced once; pending counts are not a live-updating ticker; the turn countdown is a polite live region and does not announce every second; the first row's heading receives focus when arriving from login.

**J. Requirements and evidence.** `REQ-1091`, `REQ-1107`, `REQ-1108`, `REQ-1135`, `REQ-1188`…`REQ-1193`; D-021; TR-084/088/089/092; REQ-022. Unresolved: grouped-summary presentation depth is a design-review item, not a rule.

---

### JRN-C — National management journey

**A. Journey identity.** ID `JRN-C`; category Routine; P0; screens `SCR-013`, `SCR-015`, `SCR-016`, section roots; components `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-018`, `UI-CMP-039`, `UI-CMP-007`; governing B-02, B-04, B-05, B-06, B-10.

**B. Starting conditions.** Active nation; authenticated; any political state; any turn state.

**C. Entry point.** Primary navigation Home → `SCR-013`; overview `SCR-015`; turn status `SCR-016`; a warning or banner deep-links to its owning surface.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens the digest | Summary of settled changes | Changes, pending, next boundary | `SCR-015` |
| 2 | Reviews the overview | Six labelled registers plus warnings and political banner | Treasury triple, stability/approval, readiness, protection, population/housing, power | Open a card |
| 3 | Examines turn status | Turn, boundary, phase, queued actions, last settlement | `OPEN`/`LOCKED`/`RESOLVING`/`COMPLETED`/`INTERRUPTED`/`FAILED`; `unknown — retrying` | Owning action |
| 4 | Identifies a warning | Warning panel names condition, consequence, end/review turn and actions | What to fix and by when | Owning screen |
| 5 | Opens the owning screen | Full object/register; allowed/blocked actions | Action details and confirmations | Take or defer action |
| 6 | Takes an available action | Owning flow confirmation and result | Exact effect, cost, phase, resulting state | Return to `SCR-015` |
| 7 | Confirms the reflected state | Overview shows the new state at the new as-of turn | Updated triple/status/warning | Continue or leave |

**E. Alternative paths.** A player may open any section directly; the overview is a convenience, not a gate. Warnings may be deferred where the rule permits; the warning remains. No action may be taken from the overview itself. A player may inspect history before acting (`SCR-017`, `SCR-031`).

**F. Failure paths.** A card's owning screen is denied → `ST-09` with the restriction class. A register is suppressed → `ST-06` with the named suppression state, not zero. Turn status is stale → labelled as-of; refresh offered. A section fails → `ST-14` within that section; the rest of the overview remains. An action becomes blocked between overview and owning screen → owning screen shows `ST-11` with reason and no confirmation.

**G. Completion.** The player understands the national state, has acted where intended, and sees the result reflected consistently on the owning screen and overview. No new notification is generated by viewing. Next actions: another section, digest, or leave.

**H. Recovery.** If an action is interrupted, the owning screen and digest are re-read; the overview never asserts a state the authoritative record does not hold. Safe navigation: return to `SCR-015` or `SCR-013`.

**I. Accessibility.** Overview cards are a headed list; each card's label/value/unit/as-of are announced together; warnings precede supporting data in reading order; no chart is the only representation; state banners are announced once; focus follows the card link into the owning heading.

**J. Requirements and evidence.** `REQ-1092`, `REQ-1107`, `REQ-1136`…`REQ-1153`; ECN-176/177; URB-052; DMP-073/268; TR-035/039. Unresolved: none beyond the inherited provisional values.

---

### JRN-D — Economy and treasury journey

**A. Journey identity.** ID `JRN-D`; category Routine; P0; screens `SCR-029`…`SCR-034`; components `UI-CMP-014`, `UI-CMP-031`, `UI-CMP-032`, `UI-CMP-033`, `UI-CMP-034`, `UI-CMP-035`, `UI-CMP-075`, `UI-CMP-088`; governing B-04, B-05 for capacity and power.

**B. Starting conditions.** Active nation; authenticated; treasury and warehouse records exist (zero values are true values); any turn state.

**C. Entry point.** Primary navigation Economy → `SCR-029`; a digest treasury row or warning deep-links; `SCR-015` treasury card opens `SCR-029`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens Treasury `SCR-029` | Six separated registers; as-of turn | Available, reserved, total; income/expenditure; forecast with assumptions; history | Choose budget/reports/resources/production |
| 2 | Examines budget `SCR-030` | Opex vs capex; wealth as report statistic | Recurring costs; one-time investments; austerity order if triggered; recovery options | Owning screen |
| 3 | Reviews resources `SCR-033` | Per-resource total/reserved/available; warehouse `used/total` | Available stock; capacity; book value | Production or trade |
| 4 | Reviews production `SCR-032`/`SCR-044` | Chain policy, capacity, inputs, blocking reason | `RUN_AT_CAPACITY`/`RUN_TO_TARGET`/`IDLE`; power; maintenance | Set policy or order |
| 5 | Sets standing policy (`FLOW-009`) | Confirmation explains recurring nature and no reservation | Effect at the recurring phase; no immediate charge | Policy recorded |
| 6 | Submits a manual order (`FLOW-010`) | Preview of money/inputs/capacity/space reservation | Exact cost; batch count; availability | Accepted/reserved or rejected |
| 7 | Reviews financial history `SCR-031` | Append-only records with causes and failure factor | Why each material change occurred | Return to `SCR-029` |

**E. Alternative paths.** A player may inspect power `SCR-034` to diagnose derating, or warehouse capacity before ordering. A player may choose `IDLE` or no manual order. A manual order may be cancelled only where ECN-063 permits while `OPEN`. Trade is a separate journey (`JRN-E`); no economy screen initiates a trade except through `SCR-036` with available assets.

**F. Failure paths.** Invalid numeric input → `ST-08` with bounds and preserved input. Insufficient crowns/inputs/space/power → `ST-11` naming the limiting factor (`F5`, `SPACE_BLOCKED`, power shortfall). Capacity overbooking → `ST-11`; nothing reserved. Setup fails at resolution → exact failure factor in `SCR-031`; no partial execution. Treasury at zero → no debt/credit/overdraft; austerity cancels unpaid obligations (ECN-105/106). Stale balance → labelled; action revalidated server-side.

**G. Completion.** The policy or order is recorded with its reservation or recurring effect; the treasury triple reflects the change at the authoritative as-of turn; the digest records the settlement; the next action is visible (`SCR-029`). No new notification is created by viewing; a settlement produces its existing digest event.

**H. Recovery.** A rejected order preserves the form where safe for correction. An interrupted settlement is shown as `INTERRUPTED`/`FAILED` with no invented charge; accepted actions remain pending (TR-080). Retry is safe only where no reservation was created or the owning rule permits; an uncertain order is reconciled by re-reading `SCR-032`/`SCR-031` before resubmission (`DUP-03`).

**I. Accessibility.** Each balance is announced as "total X, reserved Y, available Z, unit, as of turn N"; forecasts are announced as forecasts; capacity bars have text equivalents; numeric inputs have visible labels and errors linked; the six number types are distinguishable without colour; charts have table alternatives.

**J. Requirements and evidence.** `REQ-1093`, `REQ-1111`, `REQ-1112`, `REQ-1196`; ECN-044/045/049/053/105/106/107/110/142/177/178; MKT-053; D-048/D-050/D-051/D-053/D-062. Unresolved: all economic numbers remain provisional (Prompt 14).

---

### JRN-E — Trade journey

**A. Journey identity.** ID `JRN-E`; category Transactional; P0; screens `SCR-035`…`SCR-037`, `SCR-040`; components `UI-CMP-022`, `UI-CMP-033`, `UI-CMP-046`, `UI-CMP-047`, `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-088`; governing B-07 (MKT), D-016/D-017.

**B. Starting conditions.** Active nation; authenticated; a named counterparty or an incoming offer; assets available (creation reserves nothing); no Global Trade requirement. `SCR-038/039` remain absent (G-1…G-6 not met).

**C. Entry point.** Inbox `SCR-014` → `SCR-035`; Economy navigation → `SCR-035`; `SCR-033` `Compose offer` → `SCR-036`; `SCR-019` trade alert → `SCR-037`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-035` | Incoming/outgoing chains; status, terms summary, expiry, balances | Who offered what; expiry turn; rate-limit position; no-reservation notice | Open, counter, accept, decline, cancel |
| 2 | Reviews an offer `SCR-037` | Two-sided record; revision timeline; settlement/failure panel | Both obligations; transfer reference; exact state | Decide |
| 3 | Composes/counters `SCR-036` (`FLOW-011`) | Up to 5 lines per side; available balances; pledge/imbalance; expiry | Both sides; no reserve at create; MKT-038 pledge | Confirm offer |
| 4 | Counterparty accepts (`FLOW-012`) | Revalidation notice; confirmation; pending acceptance | Terms re-checked; atomic all-or-nothing consequence | Accepted → settlement at P4 |
| 5 | Settlement resolves | Record shows `RESOLVED` or `FAILED` with exact reason | What moved; transfer reference; ledger deltas | Review history |
| 6 | Reviews `SCR-040` | Own trade history; pre-gate minimal reference-price state | Completed/pending/failed; no market statistic pre-gate | Return |

**E. Alternative paths.** Decline is private and free with a reason code; counter creates a new revision and resets the 72-turn expiry; the current author may cancel while `ACTIVE`/`COUNTERED`; an accepted chain cannot be player-cancelled. A player may leave the offer untouched until expiry; expiry is a boundary job. `SCR-038/039` are not reachable under any path.

**F. Failure paths.** Missing/invalid resource or amount → `ST-08` with `MKT-E01`…`E12` translated. Resource/warehouse/space/political/restriction block → `ST-11` with the owning `MKT-A0x` reason. Stale revision → `ST-13`; the player re-reads before retrying. Duplicate submission → single-flight and stored-key reuse (`MKT-041` A09). Third failed acceptance → chain `EXPIRED` (`STALE`). Counterparty retired/unavailable → offer remains until expiry; no fabricated acceptance. Atomic settlement failure → nothing moves; both sides revalidated; exact failure recorded. Rate limit → `ST-11` with reset turn.

**G. Completion.** A created chain is `ACTIVE` and reserves nothing; an accepted chain becomes `ACCEPTED` then `RESOLVED`/`FAILED` at settlement; both parties see the same record and ledger. The Inbox row updates; a settlement generates its existing event. Next actions: new offer, history, or return.

**H. Recovery.** An interrupted acceptance is reconciled by re-reading `SCR-037` and the Inbox before retrying; no automatic duplicate acceptance. A cancelled/expired chain is terminal and a new chain is required. If the counterparty page is retired, the record remains readable within retention and the trade flow cannot proceed.

**I. Accessibility.** The offer builder is a labelled fieldset per side; amount fields have units and errors linked; the pledge and imbalance are text, not colour; the confirmation lists both sides in reading order; the settlement state is announced once; tables/cards preserve all terms and the triple.

**J. Requirements and evidence.** `REQ-1094`, `REQ-1113`…`REQ-1115`; D-016, D-017; MKT-019/022/026/027/028/029/030/038/039/041/046/047/053/059–067/105/125/131. Unresolved: Global Trade gate G-1…G-6 remains unmet; no pre-gate market flow exists.

---

### JRN-F — Cities, infrastructure and research journey

**A. Journey identity.** ID `JRN-F`; category Routine; P0; screens `SCR-041`…`SCR-046`; components `UI-CMP-036`, `UI-CMP-037`, `UI-CMP-034`, `UI-CMP-088`, `UI-CMP-089`, `UI-CMP-016`; governing B-05 (URB), D-073/D-074/D-076.

**B. Starting conditions.** Active nation; at least the capital exists; owned cities; one construction slot per city per turn; one active research project nationally.

**C. Entry point.** Primary navigation Cities → `SCR-041`; a city row → `SCR-042`; `Construct` → `SCR-043`; `Research` → `SCR-045`; `Found new city` → `SCR-046`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-041` | All twelve cities/capital; infrastructure, DC, housing, status | Count, total infrastructure, found-city eligibility | Open a city |
| 2 | Reviews `SCR-042` | Infrastructure 10–500; housing formula; `used/total` DC; facilities; slot | Capacity and constraints before paying | Construct/demolish |
| 3 | Previews construction `SCR-043` (`FLOW-014`) | Full URB-148 preview; slot; availability; affordability; refund | Cost after discounts, DC, book value, wealth effect | Confirm |
| 4 | Confirms construction | Pending order with slot claimed at acceptance | Availability turn; cancellation terms | Order accepted |
| 5 | Opens research `SCR-045` | RP pool, generation, active project, twelve-tech tree | Status, cost, prerequisites, effect, one-active limit | Start/fund |
| 6 | Starts research (`FLOW-016`) | Confirmation with cost, effect, completion forecast | Crowns charged immediately; no refund on abandon | Project active |
| 7 | Reviews completion/failure | Project/queue state at the owning turn | Complete, failed or cancelled with reason | Next action |

**E. Alternative paths.** A player may demolish a facility (separate destructive control, 25% crown refund, materials not returned, slot consumed) where URB-071 permits. A player may found a city (`FLOW-015`) when all gates pass. A player may fund a research programme with banked RP only. A player may cancel a construction order only where the rule permits; an accepted order is otherwise resolved at the boundary.

**F. Failure paths.** No slot → `ST-11` with slot reason. DC insufficient → `ST-11` with projected `used/total`. Cost/steel unavailable → `ST-11` with the exact missing amount. Facility limit reached → `ST-11`. Research prerequisite missing → `ST-11`; active project exists → `ST-11`. Founding eligibility fails → `ST-11` with the checklist. Completion failure names the factor; no silent partial. Stale city state → re-read before confirming; the server revalidates.

**G. Completion.** The construction order is accepted with its slot claimed; the research project is active with its cost charged; the city/queue/research state is reflected on `SCR-041`, `SCR-042`, `SCR-045` and the digest; the availability/completion turn is visible. Next actions: another city, another turn's order, research view.

**H. Recovery.** A rejected order preserves the preview for correction. An interrupted settlement is named; no charge beyond the rule's charge point. A cancelled construction/abandoned research loses what the rule says (crown cost/progress) and says so before confirmation. The one-slot rule prevents duplicate orders; a retry after `unknown` reconciles `SCR-042/043` before resubmission.

**I. Accessibility.** The twelve-city list is one screen with headed rows; each row's infrastructure/DC/housing are announced together; the construction preview is an ordered list; projected values are announced as projections; the destructive demolition control is separated and confirmed; focus returns to the city heading after order.

**J. Requirements and evidence.** `REQ-1095`, `REQ-1116`…`REQ-1118`; URB-031/032–034/052/064/071/093–097/148; D-067/D-068/D-073/D-074/D-076. Unresolved: capacity parameters remain provisional.

---

### JRN-G — Politics and domestic governance journey

**A. Journey identity.** ID `JRN-G`; category Routine; P0; screens `SCR-021`…`SCR-028`; components `UI-CMP-038`, `UI-CMP-039`, `UI-CMP-040`, `UI-CMP-041`, `UI-CMP-042`, `UI-CMP-089`; governing B-06 (DMP), D-084/D-085, D-087, D-094.

**B. Starting conditions.** Active nation; authenticated; one of the six `leadership_state` values; government identity permanent; administration/policy separately changeable.

**C. Entry point.** Primary navigation Politics → `SCR-021`; state banner or warning → `SCR-028`; digest election/result row → `SCR-025`/`SCR-027`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-021` | State banner with cause/end turn/what is locked; government and leader/administration | Approval, stability in bp + text label, six supports, pressure | Choose detail |
| 2 | Reviews `SCR-023` | Six supports with weights, terms and contributions; cause-chain drawers | Why approval/stability are what they are | Policy or crisis |
| 3 | Reviews `SCR-024` | Two axes, current settings, effect, cost, cooldown on control | Next eligible turn; effect at T+1 | Change policy |
| 4 | Confirms a policy change (`FLOW-007`) | Confirmation lists effect, cost, cooldown, effective turn | One change per axis per 12 turns | Recorded |
| 5 | Participates in an election | `SCR-025` date ladder anchored on `campaign_open_turn`; ballot; projection | `T−24`/`T−12`/`T−2` on-time labels; turnout; forecast vote | `SCR-026` |
| 6 | Runs a campaign action (`FLOW-008`) | Exactly three action types with cost/effect and once-only state | Points or crowns; charge-once; no cancellation | Charged once |
| 7 | Reviews result/crisis | `SCR-027` outcome and transition; `SCR-028` crisis/recovery | Administration changes, government does not; 800 bp transition; crisis 18 turns/1,500 bp; recovery 12 turns/400 bp | Plan next |

**E. Alternative paths.** A player may only read politics. During `TRANSITION`/`CRISIS`, policy and campaign controls are read-only with reason. A player may dismiss a crisis explanation and return later; recovery remains actionable. There is no government-change, coup, revolution or constitution-change control. A player may decline to campaign; no penalty beyond the election outcome.

**F. Failure paths.** Policy on cooldown → `ST-11` with remaining turns/next eligible turn. Campaign limit reached → `ST-11`; charged-once state visible. State blocks action → `ST-11` with the DMP-268 state and what is locked. Election dates interrupted → delayed state, not missed deadline. Result unavailable → `ST-14`/`ST-12` with the owning record. A campaign retry with the same key returns the stored row and does not charge twice (`DMP-193`).

**G. Completion.** The policy change, campaign action or election outcome is recorded; the political state banner updates; the digest records the outcome; next eligible turn and recovery actions are visible. No new notification type is invented; DMP election/state events are the existing sources.

**H. Recovery.** A policy rejection starts no cooldown (`DMP-102`) and the form can be corrected. A campaign action cannot be cancelled after charge; the record shows the charge. If the political state blocks a return, the banner names the end turn. A re-entry after crisis shows the current state and recovery actions.

**I. Accessibility.** The state banner is announced once with state/cause/end turn; approval/stability are announced as integer basis points plus the text label; the six supports form a headed table/list; policy cooldown is on the control and exposed to assistive technology, not tooltip-only; campaign cost/effect are text; no election urgency countdown.

**J. Requirements and evidence.** `REQ-1096`, `REQ-1109`, `REQ-1110`; D-084, D-085, D-087, D-094; DMP-073/080–083/101/102/128/163/178/184/189/193/225/268. Unresolved: no stability bands may be invented; all political numbers remain provisional.

---

### JRN-H — Diplomacy and alliances journey

**A. Journey identity.** ID `JRN-H`; category Transactional; P0; screens `SCR-047`…`SCR-058`; components `UI-CMP-044`, `UI-CMP-045`, `UI-CMP-046`, `UI-CMP-047`, `UI-CMP-048`, `UI-CMP-049`, `UI-CMP-050`, `UI-CMP-053`, `UI-CMP-088`; governing B-08 (DIP), B-09 (ALL/D-140), 08C §12.3.

**B. Starting conditions.** Active nation; authenticated; a named counterparty for proposals; alliance role/permission for management surfaces; pending terms visible only to parties (D-030).

**C. Entry point.** Primary navigation Foreign → `SCR-047`; nation profile `SCR-010` → pair `SCR-048`; Inbox proposal row → `SCR-049`/`SCR-050`; Network View node → `SCR-010`/`SCR-053`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Discovers another nation | `SCR-010` public fields; `SCR-047` posture register; `SCR-018` symbolic edges | Identity, posture per direction, public agreements, breach count | Open pair |
| 2 | Opens `SCR-048` | Two directional postures; agreements; embargo; pending band; restriction panel | What is between the nations | Propose/view |
| 3 | Creates a proposal `SCR-049` (`FLOW-017`) | Ten-field confirmation; terms, duration, limits, reversibility | What it authorises, affects, costs, lasts, consumes, does not do | Send |
| 4 | Counterparty reviews | Inbox pending row; proposal detail; ten fields | Parties-only terms; no preselected acceptance | Accept/counter/reject/withdraw |
| 5 | Accepts (`FLOW-018`) | Confirmation; then accepted state | Activation/expiry at the boundary; six consent questions where bilateral | Active/record-only |
| 6 | Reviews `SCR-050`/`SCR-051` | Type, lifecycle, obligations, publication state | Private vs public fields; k=5 aggregates | Manage |
| 7 | Alliance surfaces `SCR-053`…`SCR-058` | Public identity; permissioned management; coverage | Roles, tax brackets, ARL categories, treaties; no military command | Act within permission |

**E. Alternative paths.** A proposer may withdraw while `PENDING`; a recipient may reject (private, free, final); a counter replaces the live terms. A pair may impose an embargo only under `HOSTILE` where B-08 permits, with confirmation. An alliance member may apply/invite (`FLOW-019`) where the rules permit, or decline consent to an alliance treaty and remain non-covered. A player may leave an alliance; exit is unblockable. `SCR-038/039` are unrelated and absent.

**F. Failure paths.** Wrong/terminal state → `ST-12`/`ST-13` (`DPF-01`). Duplicate proposal/agreement → `ST-11` (`DPF-04`). Three outgoing proposals → `ST-11` (`DPF-06`). Transition/crisis freeze or missing consultation → `ST-11` (`DPF-07/09`). Cooldown → `ST-11` (`DPF-08/10/14`). Counterparty unavailable/retired → `ST-12` (`DPF-02`); no acceptance. Aid insufficient crowns → `ST-11` (`DPF-05`). Alliance permission/role failure → `ST-09` with the permission class (`ALF-21`, `ALF-08`); no escalation. Tax input outside 0–10,000 bp → `ST-08`. Alliance operational funding → `ST-10` unavailable (`ALF-27`), no cost schedule exists.

**G. Completion.** A proposal is pending (parties only), accepted, rejected, withdrawn or expired; an agreement is active/record-only with its publication state; an alliance action is recorded with receipts/audit; the Inbox and owning screens reflect the state. Notifications are the existing DIP/ALL events only. Next actions: pair history, another proposal, alliance management.

**H. Recovery.** A withdrawn/rejected/expired proposal is final for that object; a new proposal is required and the cap/cooldown is shown. An interrupted acceptance is reconciled by re-reading `SCR-049/050` before retry. An alliance permission change invalidates dependent unexecuted proposals (`ALL-074`); the surface re-reads and explains. A retired counterparty remains a historical record; no new action is possible.

**I. Accessibility.** Directional postures are two labelled groups, not colour; the ten confirmation fields are an ordered list; pending/expiry are announced as turns; permission-denied reasons are text; the alliance role matrix is a table with headers; no control exists only on hover.

**J. Requirements and evidence.** `REQ-1097`, `REQ-1119`…`REQ-1122`; D-030, D-133, D-140; DIP-023/024/042/045/046/047/049/052/101/108–114/130; ALL-080–086/179–187/193/220–226; 08C §12.3. Unresolved: `UD-040`, `UD-044`…`UD-047`, `UD-049` remain Open; no value invented.

---

### JRN-I — Warfare and military journey

**A. Journey identity.** ID `JRN-I`; category Consequential; P0; screens `SCR-059`…`SCR-067`; components `UI-CMP-054`, `UI-CMP-055`, `UI-CMP-056`, `UI-CMP-057`, `UI-CMP-058`, `UI-CMP-062`, `UI-CMP-088`, `UI-CMP-087`, `OVL-02`; governing B-10 (WAR), WAR-152, WAR §12.3.

**B. Starting conditions.** Active nation; authenticated; **nation owner only**; one OP pool with cap/regeneration; protection/NAP/alliance/political-state checks apply; no alliance authority exists.

**C. Entry point.** Primary navigation War → `SCR-059`; `Open operations board` → `SCR-061` (owner only); conflict ledger `SCR-062` → `SCR-063`; battle report `SCR-064`; settlement `SCR-067`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-059` | Own OP balance/cap/regeneration; readiness; active wars; warnings | Own exact state; no opponent exact data | Forces or board |
| 2 | Reviews forces `SCR-060` | Unit roster; military Food; readiness effect; impairment | `RATION_SHORT`; upkeep outcome | Board |
| 3 | Prepares an operation `SCR-061` (`FLOW-021`) | Operation type, OP cost, supply, objective, expected effect; block reasons | Threat only as `LOW`/`MODERATE`/`HIGH`/`SEVERE`; exact own cost | Confirmation |
| 4 | Confirms per WAR-152 | Confirmation names counterparty, OP/resources, objective, effect, irreversible consequence | No preselected or remembered confirmation | Submitted/reserved |
| 5 | Reviews battle/war detail | `SCR-063`/`SCR-064` field-filtered; public summary otherwise | Own detail; public tier/type/loss band | Continue/settle |
| 6 | Proposes/accepts settlement `SCR-067` (`FLOW-023`) | One live settlement; every term/duration; 12-turn expiry | Acceptance never inferred from silence | Accepted/failed |
| 7 | Reviews history `SCR-066`/`SCR-065` | Class-P records; losses; retention | Outcome and settlement | Return |

**E. Alternative paths.** The owner may amend/cancel an accepted reserved operation before freeze; may withdraw a settlement before acceptance; may surrender at any time in `ACTIVE`/`SUSPENDED` (`FLOW-024`). A player may only observe public conflicts. An alliance may not operate, spend OP, delegate war or view private war data; an alliance treaty blocks hostile action where `AT-E01` applies. There is no espionage or intelligence flow (`SCR-068` absent).

**F. Failure paths.** Protection/NAP/same-alliance/political state/OP/supply/readiness block → `ST-11` with the exact `WRF-` class and next condition. Campaign expired → `ST-12` (`WRF-20`). Settlement reservation lost → `WRF-33`; campaign returns `ACTIVE`. Invalid city target/repair → `ST-08`/`ST-11` (`WRF-36/37`). Duplicate submission → single-flight; no double reservation. Thaw/interruption → `ST-14`/`ST-16`; no invented battle result. Non-owner access → `ST-09`; the board is never rendered.

**G. Completion.** The operation is submitted/reserved and resolves at P5; the battle report and losses reflect the authoritative result; the campaign state and settlement are visible; surrender is the guaranteed off-ramp. Existing WAR notifications are generated; no new channel. Next actions: another operation (within limits), review reports, settle.

**H. Recovery.** Before freeze, the owner may cancel an accepted reservation; after freeze, no change. A failed operation releases its reservation per the rule and names the factor. An interrupted settlement remains one-live; a lost reservation returns the campaign to `ACTIVE`. Reconnection never re-submits; the board is re-read.

**I. Accessibility.** OP balance/reservation are announced together; the threat band is text plus glyph; the confirmation lists every required field in order; the destructive surrender control is separated and confirmed; battle tables have headers and text alternatives; no critical fact is hover-only.

**J. Requirements and evidence.** `REQ-1098`, `REQ-1123`…`REQ-1126`; WAR-039/046/085–088/115–117/122/126/127/131/132/148/152/161; AX-18; REQ-589…591. Unresolved: all warfare numbers provisional; UD-032 Option A stands; no espionage rule.

---

### JRN-J — World and progression journey

**A. Journey identity.** ID `JRN-J`; category Progression; P1; screens `SCR-018`, `SCR-069`…`SCR-076`; components `UI-CMP-063`, `UI-CMP-064`, `UI-CMP-065`, `UI-CMP-066`, `UI-CMP-067`, `UI-CMP-068`, `UI-CMP-072`, `UI-CMP-073`; governing B-11 (WEP), B-02 for Network View.

**B. Starting conditions.** Authenticated; event eligibility per event; objectives are optional; standings are published at P7 from the P6 snapshot.

**C. Entry point.** Primary navigation World → `SCR-069`; digest event row → `SCR-070`; `SCR-009` → `SCR-071`; `SCR-018` from World or overview.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Reviews events `SCR-069` | Active/scheduled events with class/state/eligibility | Registered events only | `SCR-070` |
| 2 | Opens event `SCR-070` | Cause/hazard paired with registered consequence; duration; affected quantities | Exact effect source; no hidden modifier | Respond or back |
| 3 | Reviews objectives `SCR-071` | Twelve categories; lifecycle; progress; optionality | Tiered progress; penalty-free dismissal; reward class | Accept/dismiss |
| 4 | Acts on an objective (`FLOW-025`) | Optional accept/dismiss with no penalty | No presence/membership/spending/aggression requirement | Owning screen or back |
| 5 | Reviews standings `SCR-072` | Named lists with denominator, eligibility, window, computation turn | No live rank; no composite score | Compare/profile |
| 6 | Reviews progression `SCR-074`/`SCR-073` | Eight separate layers; achievements; reward classes | No single score | Reward history |
| 7 | Reviews history/rewards `SCR-075` | Deferred, granted, voided, corrected | Deferred stays visible; no premature grant | Return |
| 8 | Reviews Network View `SCR-018` | Symbolic nodes/edges; filters; list-first mobile | Published relations only; no geography | Profile/pair |

**E. Alternative paths.** A player may take no objective and dismiss any optional objective without penalty. A player may view only public events. A reward claim is offered only where the B-11 flow provides one (`FLOW-026`); deferral remains visible. `SCR-077` (World Health) is absent; no figure, axis or placeholder exists pre-gate.

**F. Failure paths.** Event expired → `ST-12`; progress/recognition survives. Objective invalid transition → `ST-11` (`WPF-19`). Reward claim conflict/duplicate → `ST-13`; the first valid grant wins and duplicates are deduplicated. Standing unavailable/suppressed → `ST-06` with the named state; never zero. Network edge to a retired/denied object → denied/retired state. Missing denominator → treated as a specification defect and the display is not rendered as a rank.

**G. Completion.** The player understands what is active, what is optional, where the nation stands in named lists, and what remains deferred. The record is the objective/reward/standing history; no notification type is invented. Next actions: an owning screen, reward history, profile.

**H. Recovery.** Objective progress recomputes from authoritative state; a dismissed objective may return where the flow permits. A failed claim is retryable after reconciliation. A suppressed figure remains suppressed until the sample threshold is met; no manual override.

**I. Accessibility.** Event cause and consequence are separate headed regions; objectives state optionality in text; standings announce denominator/window with the rank; suppression is announced as suppressed; Network View has a list-first equivalent that contains every fact; no chart is the only source.

**J. Requirements and evidence.** `REQ-1099`, `REQ-1127`, `REQ-1128`; WEP-099/179/203–215/232/240/324/325/359/361/582/663/705; D-027; TR-012/013/014; REQ-041. Unresolved: `SCR-077` gate; k=5 evidence; `OBJ-TRADE` remains blocked while trade gates are unmet.

---

### JRN-K — Notifications and player protection journey

**A. Journey identity.** ID `JRN-K`; category Support; P0; screens `SCR-019`, `SCR-081`…`SCR-087`; components `UI-CMP-008`, `UI-CMP-069`, `UI-CMP-027`, `UI-CMP-053`, `UI-CMP-085`, `UI-CMP-021`, `OVL-05`, `OVL-08`; governing B-02/REQ-731, B-12 (MOD/PRV/NET/FR).

**B. Starting conditions.** Authenticated; a notification exists or the player initiates a report/appeal/support request; a restriction may apply but never blocks appeal or security notices.

**C. Entry point.** Shell alert indicator → `SCR-019`; digest alert row; `SCR-010` report action → `SCR-081`; decision notice → `SCR-082`/`SCR-083`; account home → `SCR-084`/`SCR-086`/`SCR-087`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Receives a notification | Indicator count; non-focus-stealing notice | Source event, tier, object, turn | Open or defer |
| 2 | Opens `SCR-019` | Alert history with tier, source, read state, mute state | Non-opt-out marked; duplicates grouped | Open an alert |
| 3 | Opens an alert (`FLOW-027`) | Deep link to owning object; loading state | The event's owning context | Act or back |
| 4 | Reports conduct `SCR-081` (`FLOW-028`) | Exactly MOD-002 fields; accusation notice; evidence store | Category, subject, time window, free text; acknowledgement and case reference | `SCR-082` |
| 5 | Reviews status/decision `SCR-082` | Seven-element notice; claim tier; withheld explanation | Kind, rule element, evidence class, tier, end, appeal, correction | Appeal |
| 6 | Files an appeal `SCR-083` (`FLOW-029`) | Status ladder; never blocked by restriction | Grounds, decisions, next step | Appeal recorded |
| 7 | Reviews restriction/review `SCR-084`/`SCR-086` | Kind, scope, end/review turn; five network states | No accusation; no technical exposure | Appeal/correction |
| 8 | Opens support `SCR-087` | Separate support categories and route | Support ≠ moderation; explicit route change | Request registered |

**E. Alternative paths.** A notification may be deferred or dismissed where permitted; non-opt-out items remain. A player may mute a mutable tier. A player may contact support instead of reporting; the route distinction is explicit. A player may withdraw an appeal only where the rule permits. A player may request data/export/correction via `SCR-085`.

**F. Failure paths.** Intake unavailable → retryable failure; the report is not silently lost (`FR-006`). Missing required field → `ST-08`. A report subject is the reporter or an invalid object → validation with MOD-002 scope. An appeal route must never render unavailable (`MOD-013`); if a surface fails, the account-level route remains. A retired/denied notification destination → owning state. A pair restriction is not a suspension; the wrong vocabulary is a defect. Duplicate report submission → single-flight; one case reference.

**G. Completion.** The notification is read/deferred under its rule; the report has an acknowledgement and case reference; the appeal has a status; the restriction explanation names recourse; the support request is registered separately. MOD-017's seven elements and the EVD-009 claim vocabulary are preserved. No moderation outcome is invented.

**H. Recovery.** A failed report submission preserves the entered intake where safe and offers retry. A lost case reference is recoverable from `SCR-082`. A restriction remains in force during appeal unless a reversible hold applies (`FPW-028`); the UI never implies suspension of a sanction by filing. A wrong shared-network association has the correction path.

**I. Accessibility.** The indicator announces a count change once, politely; the alert list is headed and keyboard navigable; the decision notice's seven elements are an ordered list; claim tiers are text badges, not colour; the appeal route remains focusable under every restriction; errors in report intake are field-linked.

**J. Requirements and evidence.** `REQ-1100`, `REQ-1129`…`REQ-1131`, `REQ-1182`…`REQ-1187`; MOD-002/007/013/015/017/018/022; NET-023/050; PRV-002/009/014/019; EVD-009; D-026/D-033/D-034. Unresolved: `UD-052`…`UD-060` and `UD-017` remain owner/legal reserved; no outcome invented.

---

### JRN-L — Account management journey

**A. Journey identity.** ID `JRN-L`; category Account; P0; screens `SCR-011`, `SCR-012`, `SCR-080`, `SCR-090`; components `UI-CMP-017`, `UI-CMP-088`, `UI-CMP-090`, `UI-CMP-087`, `OVL-01`, `OVL-02`; governing B-03 (ACC/D-041/RRL).

**B. Starting conditions.** Authenticated account holder; a linked nation or none; any account state; closure only from an eligible state; reroll subject to RRL-021 blocks.

**C. Entry point.** Account menu → `SCR-011`; `Security settings` → `SCR-080`; `Close account` → `SCR-012`; `Reroll nation` → `SCR-090`.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-011` | Account state, nation linkage, security summary, restrictions | Sessions, recovery custody, privacy/data links | Choose action |
| 2 | Manages security `SCR-080` | Sessions, recovery codes, e-mail change | Codes shown once; count thereafter; dual confirmation | Updated |
| 3 | Requests closure `SCR-012` (`FLOW-030`) | Consequence list, 7-day cooling, retained records, no-shield rule | Blocked offensive/transfer actions during cooling; still targetable | `CLOSURE_REQUESTED` |
| 4 | Cancels during cooling | Cancellation control; state restored | Cooling end turn; what survives | `ACTIVE` |
| 5 | Starts reroll `SCR-090` (`FLOW-031`) | Re-auth, exact-phrase field, consequence list, block conditions | Permanent reset, losses, sanctions survive, replacement, no renewed protection | Destructive confirmation |
| 6 | Confirms reroll | `OVL-02` exact-phrase match; destructive action | No undo; immediate replacement | `SCR-007` |

**E. Alternative paths.** The player may cancel closure during cooling; may withdraw a reroll before confirmation; may use recovery-code entry `SCR-005` if locked out; may request data/export via `SCR-085`. A blocked reroll names the block (active campaign, settlement, preservation order, suspension) and offers the permitted off-ramp (for war: surrender).

**F. Failure paths.** Wrong password on re-auth → `ST-08`; no destructive action proceeds. Exact phrase mismatch → `ST-08`/`ST-11` with mismatch reason; confirm disabled. Blocked reroll → `ST-11` with block reason and off-ramp. Account already closing → `ST-13`; no duplicate closure. Expired session → re-auth, no loss of context. A recovery code already used → neutral rejection, no disclosure.

**G. Completion.** Closure enters cooling and can be cancelled; after cooling the account closes and the nation retires without replacement; records follow D-026. Reroll produces a retired nation labelled `retired — rerolled` and a replacement `New nation`; sanctions/pair limits persist. Security changes append their history. Next actions: account home, replacement creation, support.

**H. Recovery.** An interrupted closure request is reconciled by re-reading `SCR-011`. A reroll is irreversible after confirmation; there is no recovery. A lost session during closure cooling returns to the state. A lost recovery code is handled by the remaining codes/support path, not by regenerating from an unauthenticated context.

**I. Accessibility.** The destructive consequence list precedes the exact-phrase field in reading order; the match state is announced; cancel is first in focus order and never destructive-styled; the cooling period is expressed in turns/UTC; no action is triggered by keyboard default focus.

**J. Requirements and evidence.** `REQ-1101`, `REQ-1132`, `REQ-1133`, `REQ-1156`; D-039, D-040, D-041; ACC-031/043; RRL-005/006/012/020/021. Unresolved: none new; recovery/legal branches remain owner/legal reserved.

---

### JRN-M — Administrative journey

**A. Journey identity.** ID `JRN-M`; category Admin; P0; screens `SCR-091`…`SCR-100`; components `UI-CMP-010`, `UI-CMP-022`, `UI-CMP-088`, `UI-CMP-089`, `OVL-02`, `OVL-08`; governing B-12 (ADM/MOD/EVD), D-042.

**B. Starting conditions.** Authenticated holder of one or more of the eight ADM roles; step-up where required; a case or operation within the role's scope; the Admin root, never the player shell.

**C. Entry point.** Role-gated admin entry → `SCR-091`; only permitted workspaces render. Player navigation never links to an admin route.

**D. Main sequence.**

| Step | Player action | Interface response | Information presented | Result / next |
|---|---|---|---|---|
| 1 | Opens `SCR-091` | Role card, permitted workspaces, posture, audit notice | What this role may do; step-up/emergency state | Workspace |
| 2 | Reviews queue `SCR-092` | Assigned/triage list; claim tier; age | Permitted cases only; no `SEC` material | Case |
| 3 | Reviews case `SCR-093` | Evidence matrix; V-class; rule element; withheld data | Claim tier; audited read | Decision |
| 4 | Proposes a measure `SCR-094` (`FLOW-032`) | Six-tier ladder; scope; evidence class; end/review; appeal route | Two-person state or `unsegregated` | Second review/apply |
| 5 | Second review applies where required | Separate reviewer; audit record appended | Separation of duties; no self-approval | Applied |
| 6 | Audit/data views `SCR-096`/`SCR-098` | Role-scoped events; retention; preservation | No content bodies/secrets; access itself audited | Return |
| 7 | Announcement/roles `SCR-099`/`SCR-100` | Content limits; role matrix; anti-escalation | Scope, publication, audit | Publish/assign |

**E. Alternative paths.** A holder may view only permitted workspaces; denied routes do not confirm case existence. A reviewer may escalate, request a second review, or record no action. Emergency posture is a recorded state, not unbounded power. Roles may be combined in one person while permissions stay separate.

**F. Failure paths.** Insufficient role/tier → `ST-09` with the permitted class; no case data. Step-up required → `ST-11` with the step-up route. Second reviewer unavailable → `unsegregated` label where ADM-013 permits; never invented as a satisfied review. Destructive data operation without confirmation → blocked. `SEC` access attempt → denied without content. Concurrent decision conflict → `ST-13`; re-read the case. Audit write failure → the action must not be reported as applied.

**G. Completion.** A decision is recorded with its tier, scope, end/review turn, appeal route and audit entry; the player subject sees the MOD-017 notice through the owning player surface; no admin data leaks to players. Next action: next case, audit review, or exit the Admin root.

**H. Recovery.** An interrupted proposal is reconciled from the case record before retry; a lost second review is re-requested. A correction appends, never rewrites. A wrong association has its correction path (`SCR-095`). An expired step-up returns to the gate without losing the selected case reference where safe.

**I. Accessibility.** Admin workspaces are keyboard-operable; the evidence matrix is a semantic table; destructive applies are separated and confirmed; claim tiers and roles are text; focus returns to the case heading after a decision; no content depends on colour or hover.

**J. Requirements and evidence.** `REQ-1102`, `REQ-1134`; ADM-003/005/006/009/010/011/012/013/021/022; MOD-022/036/037/042; EVD-009/026/028; D-042. Unresolved: staffing-dependent two-person availability; `unsegregated` state must be shown honestly.

---

## 4. Interaction flow catalogue (FLOW-001…FLOW-033)

Every flow uses: identity; name; trigger; preconditions; actors; sequence table; alternative paths; failure paths; cancellation; completion; recovery; accessibility; related screens; related components; related requirements; governing specifications. Flow bodies below compress the ten fixed fields into the mandated 15 fields.

### FLOW-001 — Registration and verification

- **Trigger:** `Create account` on `SCR-002`.
- **Preconditions:** No authenticated session; valid e-mail pair, password policy and terms accepted.
- **Actors:** Player; interface; authentication/account system.
- **Sequence:** (1) Player submits → (2) local validation → (3) confirmation (plain, non-destructive) → (4) account created `UNVERIFIED` → (5) `SCR-006` shows verification state and resend limit → (6) verification link confirms → (7) account verified; `SCR-007` eligible.
- **Alternative:** reset (`SCR-004`), recovery (`SCR-005`), change e-mail, support.
- **Failure:** invalid input → `ST-08`; network → `ST-15`; duplicate/concurrent → `ST-13`; e-mail already in use → neutral message that does not enumerate accounts.
- **Cancellation:** before account creation, nothing exists; after creation, the account remains unverified and may be abandoned.
- **Completion:** verified account; creation gate open.
- **Recovery:** re-open `SCR-006`; resend subject to limit; no token disclosure.
- **Accessibility:** labelled fields; error summary focus; state announced; keyboard complete.
- **Screens:** `SCR-002`, `SCR-006`, `SCR-004`, `SCR-005`. **Components:** `UI-CMP-074`, `UI-CMP-078`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-085`, `OVL-01`.
- **Requirements:** `REQ-1103`, `REQ-1090`, `REQ-1142`, `REQ-1165`.
- **Governing:** B-03 ACC-023/024; D-029; D-041.

### FLOW-002 — Login and session entry

- **Trigger:** `Log in` on `SCR-003` or session expiry.
- **Preconditions:** Existing account; credentials; account not closed/banned.
- **Actors:** Player; interface; authentication system.
- **Sequence:** (1) Submit credentials → (2) authenticate → (3) resolve account state → (4a) verified with nation → `SCR-013`; (4b) verified without nation → `SCR-007`; (4c) unverified → `SCR-006`; (4d) restricted/suspended → neutral `ACC-018` state.
- **Alternative:** reset/recovery; keep-session; close.
- **Failure:** wrong credentials → generic message (no account enumeration); locked/recovery-locked → neutral state; network → `ST-15`.
- **Cancellation:** return to landing; no session created.
- **Completion:** session established; intended destination preserved.
- **Recovery:** re-auth and return; recovery codes; support.
- **Accessibility:** labels; password reveal toggle is accessible; status announced; no auto-zoom on mobile.
- **Screens:** `SCR-003`, `SCR-006`, `SCR-007`, `SCR-013`. **Components:** `UI-CMP-001`, `UI-CMP-074`, `UI-CMP-085`, `UI-CMP-086`, `UI-CMP-017`.
- **Requirements:** `REQ-1104`, `REQ-1190`. **Governing:** B-03 ACC-018; D-029; D-041.

### FLOW-003 — Nation creation

- **Trigger:** `Create nation` on `SCR-007`.
- **Preconditions:** Verified account; no active nation; eligible; valid unique name/short name; no creation pause.
- **Actors:** Player; interface; nation system.
- **Sequence:** (1) Enter name/short name/emblem/posture → (2) live D-038 validation → (3) start-state summary → (4) confirmation → (5) server creates exactly one nation atomically → (6) `SCR-008`/`SCR-013`.
- **Alternative:** cancel; choose a different emblem/posture; open guide.
- **Failure:** name/short name invalid/reserved/unavailable → neutral message; account ineligible → named gate; concurrent creation → `ST-13`, no duplicate (`AC-03`); network → uncertain, re-read account home.
- **Cancellation:** no nation is created; return to `SCR-006`/`SCR-011`.
- **Completion:** nation in `awaiting first turn`; founding turn recorded; onboarding available.
- **Recovery:** re-read account home; a created nation is not re-created.
- **Accessibility:** labels; live validation not repetitive; summary readable; confirmation focus; errors linked.
- **Screens:** `SCR-007`, `SCR-008`, `SCR-013`. **Components:** `UI-CMP-074`, `UI-CMP-079`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-088`, `OVL-01`.
- **Requirements:** `REQ-1105`, `REQ-1142`, `REQ-1157`. **Governing:** B-03/B-04; NAT-005/026–030; D-038/D-063.

### FLOW-004 — First-session onboarding step

- **Trigger:** Entry to `SCR-008` or a contextual "learn this" entry.
- **Preconditions:** Authenticated; tutorial available for the account; no tutorial auto-action.
- **Actors:** Player; interface; tutorial layer; owning screen.
- **Sequence:** (1) Step card shows objective and real state → (2) player opens the owning screen → (3) reads a read-only demonstration or performs a normal action → (4) step completion is server-derived or explicitly marked where the rule allows → (5) next step/skip/replay.
- **Alternative:** skip; resume; restart; dismiss; open help; replay read-only.
- **Failure:** owning screen blocked → tutorial explains the block and pauses; no bypass; interruption → resumable; no auto-completion.
- **Cancellation:** skip/dismiss; preference recorded; protection unaffected.
- **Completion:** completion recorded once per account; tutorial preference persists.
- **Recovery:** resume at the last incomplete step; never re-grant completion.
- **Accessibility:** step heading focus; skip reachable; progress announced once; labels; no auto-advance on a timer.
- **Screens:** `SCR-008`, `SCR-009`, `SCR-013`, owning screens. **Components:** `UI-CMP-016`, `UI-CMP-019`, `UI-CMP-065`.
- **Requirements:** `REQ-1106`, `REQ-1172`…`REQ-1181`. **Governing:** B-03; ONB-009/013; D-040.

### FLOW-005 — Return, digest review and next action

- **Trigger:** Login or Home navigation.
- **Preconditions:** Authenticated nation owner.
- **Actors:** Player; interface; digest/notification system.
- **Sequence:** (1) Digest loads within the shell → (2) settled changes with cause/links → (3) pending totals and due items → (4) turn/boundary → (5) player opens an item or a section.
- **Alternative:** dismiss ambient items; open history; take no action.
- **Failure:** digest unavailable → `ST-14` with retry; stale → as-of label; offline → read-only labelled data.
- **Cancellation:** leave; no state change.
- **Completion:** player has read state and next action.
- **Recovery:** regenerate from authoritative records; missed-turn grouping.
- **Accessibility:** row headings; count announced once; countdown polite; links keyboard reachable.
- **Screens:** `SCR-013`, `SCR-015`, `SCR-016`. **Components:** `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-063`, `UI-CMP-069`, `UI-CMP-021`.
- **Requirements:** `REQ-1107`, `REQ-1091`, `REQ-1138`. **Governing:** TR-084/088/089; REQ-022.

### FLOW-006 — Inbox triage and object return

- **Trigger:** `Open Inbox` or an alert row.
- **Preconditions:** Authenticated; rows subject to per-row permissions.
- **Actors:** Player; interface; owning systems.
- **Sequence:** (1) Rows ordered by due boundary → (2) player opens a row → (3) owning screen shows the pending act → (4) player acts/defers/cancels where permitted → (5) returns to the Inbox.
- **Alternative:** filter/saved view; defer; open history; leave.
- **Failure:** row no longer live → `ST-12`; owning screen denied → `ST-09`; stale → re-read; network → retry.
- **Cancellation:** return; no change.
- **Completion:** the row reflects the owning outcome; no duplicate row.
- **Recovery:** re-read the Inbox; pending state remains until settlement.
- **Accessibility:** table headers; row actions keyboard reachable; due boundary announced; exact counts.
- **Screens:** `SCR-014`, owning screens. **Components:** `UI-CMP-022`, `UI-CMP-023`, `UI-CMP-070`.
- **Requirements:** `REQ-1108`, `REQ-1145`. **Governing:** TR-004; D-016/D-030.

### FLOW-007 — Policy change

- **Trigger:** `Confirm change` on `SCR-024`.
- **Preconditions:** Cooldown elapsed for that axis; political state permits; no pending change on that axis.
- **Actors:** Player; interface; politics system.
- **Sequence:** (1) Select setting → (2) effect/cost/cooldown preview → (3) confirmation → (4) accepted → (5) effective T+1 at resolution → (6) cooldown restarts.
- **Alternative:** cancel; inspect history; open approval detail.
- **Failure:** cooldown running → `ST-11` with next eligible turn; state blocks → `ST-11`; invalid request → `ST-08`; concurrent change → `ST-13`.
- **Cancellation:** no change; no cooldown (`DMP-102`).
- **Completion:** one change per axis recorded; cooldown visible.
- **Recovery:** rejected/cancelled requests start no cooldown; re-read.
- **Accessibility:** cooldown on control and described; confirmation ordered; result announced.
- **Screens:** `SCR-024`, `SCR-023`, `SCR-021`. **Components:** `UI-CMP-040`, `UI-CMP-089`, `UI-CMP-088`, `OVL-01`.
- **Requirements:** `REQ-1109`, `REQ-1155`. **Governing:** DMP-101/102; D-087.

### FLOW-008 — Campaign action

- **Trigger:** `Run rally`/`Run advertisement`/`Allocate platform points` on `SCR-026`.
- **Preconditions:** `ELECTORAL`; action not already charged; within the once/twice limits; campaign budget.
- **Actors:** Player; interface; politics system.
- **Sequence:** (1) Choose action → (2) show points/cost/effect → (3) confirmation → (4) charged once at submission → (5) state recorded; no cancellation.
- **Alternative:** choose another action; leave; view result later.
- **Failure:** state blocks → `ST-11`; limit reached → `ST-11`; budget insufficient → `ST-11`; duplicate → stored row, no second charge.
- **Cancellation:** before confirmation only; after charge, none.
- **Completion:** action recorded once; effect in the contest.
- **Recovery:** retry with the same key returns the stored row; re-read.
- **Accessibility:** action cards labelled; cost/effect text; confirmation; charged state announced.
- **Screens:** `SCR-026`, `SCR-025`, `SCR-027`. **Components:** `UI-CMP-042`, `UI-CMP-089`, `UI-CMP-088`, `OVL-01`.
- **Requirements:** `REQ-1110`, `REQ-1157`. **Governing:** DMP-189/193; D-094.

### FLOW-009 — Standing production-policy change

- **Trigger:** `Set policy` on `SCR-032`.
- **Preconditions:** Authenticated owner; chain exists; valid policy; target valid for `RUN_TO_TARGET`.
- **Actors:** Player; interface; economy system.
- **Sequence:** (1) Choose policy/target → (2) explanation of recurring nature and no reservation → (3) confirmation → (4) recorded → (5) applies at the recurring phase.
- **Alternative:** `IDLE`; cancel; open chain detail.
- **Failure:** invalid target → `ST-08`; chain unavailable → `ST-11`; concurrent stale policy → re-read.
- **Cancellation:** no change; nothing reserved.
- **Completion:** policy recorded; next run follows it.
- **Recovery:** re-read `SCR-032`/`SCR-044`; change again at any time (policy is not a cooldown action).
- **Accessibility:** radio/toggle semantics; target input labelled; no-reservation statement text.
- **Screens:** `SCR-032`, `SCR-044`. **Components:** `UI-CMP-035`, `UI-CMP-080`, `UI-CMP-033`, `UI-CMP-088`.
- **Requirements:** `REQ-1111`. **Governing:** ECN-044; D-053.

### FLOW-010 — Manual production order

- **Trigger:** `Submit manual order` on `SCR-032`.
- **Preconditions:** Chain capacity free after manual/standing reservations; inputs/space/power affordable; valid batch count.
- **Actors:** Player; interface; economy system.
- **Sequence:** (1) Enter batches → (2) preview money/inputs/capacity/space → (3) confirmation → (4) reservation created → (5) runs fully or fails atomically.
- **Alternative:** reduce batches; cancel; use standing policy.
- **Failure:** overbooking/insufficient → `ST-11` (`F5`, `SPACE_BLOCKED`); invalid number → `ST-08`; settlement failure → exact factor.
- **Cancellation:** while `OPEN` where ECN-063 permits; otherwise not.
- **Completion:** order accepted and reserved; or failed with nothing consumed.
- **Recovery:** reconcile before retry; no duplicate reservation.
- **Accessibility:** numeric input labels/bounds; preview ordered; error linked; result announced.
- **Screens:** `SCR-032`, `SCR-033`. **Components:** `UI-CMP-075`, `UI-CMP-033`, `UI-CMP-089`, `UI-CMP-084`.
- **Requirements:** `REQ-1112`, `REQ-1158`. **Governing:** ECN-045/049/053; F5.

### FLOW-011 — Directed trade offer creation

- **Trigger:** `Submit offer` on `SCR-036`.
- **Preconditions:** Named counterparty; no existing chain with that pair; under active-chain and rate limits; valid lines (≤5/side; bounds).
- **Actors:** Player; interface; trade system.
- **Sequence:** (1) Build both sides → (2) available balance check → (3) pledge/imbalance/expiry/rate limit → (4) confirmation → (5) chain `ACTIVE` revision 1 → (6) nothing reserved.
- **Alternative:** add/remove line; cancel; save draft only if the screen defines one (none specified).
- **Failure:** invalid line → `ST-08`; missing/invisible counterparty → `ST-11`; self-trade → `ST-11`; limit → `ST-11`; stale → re-read.
- **Cancellation:** no chain created before confirmation; after creation, cancel per MKT-029.
- **Completion:** chain `ACTIVE`, expiry `revised_turn + 72`.
- **Recovery:** re-read `SCR-035`; a created chain is editable only via counter/cancel.
- **Accessibility:** two labelled groups; amount units; confirmation lists both sides; no colour-only imbalance.
- **Screens:** `SCR-036`, `SCR-035`. **Components:** `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-083`, `UI-CMP-088`, `OVL-01`.
- **Requirements:** `REQ-1113`, `REQ-1155`. **Governing:** MKT-019/022/030/038/059–067.

### FLOW-012 — Trade acceptance and settlement

- **Trigger:** `Accept` on `SCR-035` or `SCR-037`.
- **Preconditions:** Chain `ACTIVE`/`COUNTERED`; current revision; actor is recipient; both sides can cover; pair permitted.
- **Actors:** Player; interface; trade system; boundary settlement.
- **Sequence:** (1) Open acceptance → (2) re-read both sides → (3) MKT-038 pledge and confirmation → (4) accepted (reservation) → (5) P4 settlement `RESOLVED`/`FAILED` → (6) record/ledger updated.
- **Alternative:** decline; counter; defer.
- **Failure:** stale revision → `ST-13`; insufficient → `ST-11` (`MKT-A01`…`A10`); third failure → `EXPIRED`; atomic settlement failure → nothing moves.
- **Cancellation:** accepted chain cannot be player-cancelled.
- **Completion:** atomic settlement or named failure; shared `transfer_id`.
- **Recovery:** re-read `SCR-037`/Inbox; an interrupted acceptance is not repeated blindly.
- **Accessibility:** pledge text; confirmation fields; settlement state announced.
- **Screens:** `SCR-035`, `SCR-037`. **Components:** `UI-CMP-046`, `UI-CMP-088`, `UI-CMP-021`, `UI-CMP-022`.
- **Requirements:** `REQ-1114`, `REQ-1158`. **Governing:** MKT-039/041/046; D-016; ECON-054.

### FLOW-013 — Trade counter, decline and cancel

- **Trigger:** `Counter`, `Decline` or `Cancel` on the trade screens.
- **Preconditions:** Lifecycle state permits the actor's chosen path.
- **Actors:** Player; interface; trade system.
- **Sequence:** (1) Choose path → (2) reason/terms → (3) confirmation → (4) new revision/decline/cancel → (5) status reflected.
- **Alternative:** accept instead; leave to expiry.
- **Failure:** terminal state → `ST-12`/`ST-13`; not the current author → control absent; rate limit → `ST-11`.
- **Cancellation:** counter can be withdrawn by a later counter/cancel while permitted; decline/cancel are terminal.
- **Completion:** chain state updated for both parties.
- **Recovery:** a new chain is required after terminal decline/cancel/expiry.
- **Accessibility:** reason select labelled; confirmation; status announced.
- **Screens:** `SCR-035`…`SCR-037`. **Components:** `UI-CMP-046`, `UI-CMP-086`, `UI-CMP-089`, `UI-CMP-076`.
- **Requirements:** `REQ-1115`. **Governing:** MKT-028/029/047.

### FLOW-014 — Construction order

- **Trigger:** `Confirm construction` on `SCR-043`.
- **Preconditions:** One free construction slot for that city; projected DC within limit; crowns/materials available and unreserved; facility limit.
- **Actors:** Player; interface; cities/economy system.
- **Sequence:** (1) Select facility → (2) full preview → (3) slot/DC/affordability checks → (4) confirmation → (5) slot claimed at acceptance; reservation → (6) resolution at P4.
- **Alternative:** preview other facilities; demolish where permitted; cancel.
- **Failure:** no slot/DC/cost → `ST-11` with the exact limit; invalid target → `ST-08`; concurrent order → `ST-13`.
- **Cancellation:** where the rule permits; otherwise slot resolves.
- **Completion:** order accepted; availability/book value visible; or failed with reason.
- **Recovery:** re-read city/queue; no second order for the same city/slot.
- **Accessibility:** preview ordered; projections labelled; destructive demolition separated; focus returns to city heading.
- **Screens:** `SCR-042`, `SCR-043`. **Components:** `UI-CMP-036`, `UI-CMP-088`, `UI-CMP-034`, `UI-CMP-089`.
- **Requirements:** `REQ-1116`, `REQ-1155`. **Governing:** URB-064/148; D-073.

### FLOW-015 — City founding

- **Trigger:** `Found city` on `SCR-046`.
- **Preconditions:** k≤12 and holds k−1 cities; national infrastructure ≥100×(k−1); one expansion slot; crowns and 20 steel unreserved; no other founding this turn.
- **Actors:** Player; interface; cities/economy system.
- **Sequence:** (1) Eligibility checklist → (2) cost/new-city preview → (3) name validation → (4) confirmation → (5) city created → (6) next boundary state.
- **Alternative:** cancel; return to overview.
- **Failure:** any gate → `ST-11` with the checklist item; insufficient steel/crowns → `ST-11`; duplicate founding → `ST-13`.
- **Cancellation:** nothing created before confirmation.
- **Completion:** new city at infrastructure 10/DC 11/housing 46,000; no cooldown.
- **Recovery:** re-read eligibility after a rejection.
- **Accessibility:** checklist as list; cost and starting state text; name errors linked.
- **Screens:** `SCR-046`, `SCR-041`, `SCR-042`. **Components:** `UI-CMP-088`, `UI-CMP-084`, `UI-CMP-089`, `UI-CMP-033`.
- **Requirements:** `REQ-1117`. **Governing:** URB-032–034; D-068.

### FLOW-016 — Research start

- **Trigger:** `Start research` on `SCR-045`.
- **Preconditions:** Institute standing; prerequisite met; not completed/in progress; no other active project; crowns available; slot free.
- **Actors:** Player; interface; cities system.
- **Sequence:** (1) Choose technology → (2) cost/effect/prerequisite/forecast → (3) confirmation → (4) crowns charged immediately → (5) active project at P4.2 progress.
- **Alternative:** fund a programme with banked RP; cancel only where permitted; inspect effects.
- **Failure:** prerequisite missing/active project → `ST-11`; insufficient crowns/RP → `ST-11`; invalid target → `ST-08`.
- **Cancellation:** abandonment loses crown cost and progress; confirmation states this.
- **Completion:** one active project; progress visible.
- **Recovery:** a failed start leaves no project; re-read.
- **Accessibility:** tree/list headers; status text; cost/effect; confirmation.
- **Screens:** `SCR-045`. **Components:** `UI-CMP-037`, `UI-CMP-088`, `UI-CMP-016`, `UI-CMP-089`.
- **Requirements:** `REQ-1118`. **Governing:** URB-093–097; D-076.

### FLOW-017 — Diplomatic proposal submit/counter/withdraw

- **Trigger:** `Send proposal`, `Counter` or `Withdraw` on `SCR-049`.
- **Preconditions:** Named counterparty; proposal type permitted; no duplicate live proposal for that direction/type; under the three-outgoing cap; no freeze.
- **Actors:** Player; interface; diplomacy system.
- **Sequence:** (1) Choose type/terms → (2) ten-field confirmation → (3) submit/counter/withdraw → (4) pending state (parties only) → (5) expiry at `submitted_turn + 36` or acceptance.
- **Alternative:** withdraw; counter; reject; leave.
- **Failure:** cap → `ST-11` (`DPF-06`); duplicate → `ST-11` (`DPF-04`); freeze → `ST-11` (`DPF-07`); cooldown → `ST-11`; aid insufficient → `ST-11` (`DPF-05`).
- **Cancellation:** withdrawal is free, immediate, private, irreversible.
- **Completion:** proposal `PENDING`; counterparty sees it.
- **Recovery:** a final proposal cannot be revived; a new one requires a free slot.
- **Accessibility:** ten fields ordered; confirm never preselected; cancel first.
- **Screens:** `SCR-049`, `SCR-048`, `SCR-014`. **Components:** `UI-CMP-047`, `UI-CMP-088`, `UI-CMP-046`, `OVL-01`.
- **Requirements:** `REQ-1119`. **Governing:** 08C §12.3; D-030; DIP-042/044/045/046/047.

### FLOW-018 — Diplomatic acceptance and activation

- **Trigger:** `Accept` on a pending proposal.
- **Preconditions:** Pending; actor is named counterparty; not expired/withdrawn; state permits.
- **Actors:** Player; interface; diplomacy system; boundary.
- **Sequence:** (1) Review terms → (2) six consent questions where bilateral → (3) confirmation → (4) accepted → (5) active at the defined boundary → (6) publication state per DIP-108…113.
- **Alternative:** reject; counter; defer.
- **Failure:** expired/terminal → `ST-12`; consent incomplete → `ST-11`; concurrent withdrawal/acceptance → first recorded wins (`DIP-130`).
- **Cancellation:** acceptance cannot be undone unilaterally; only mutual termination/break later.
- **Completion:** active/record-only agreement with exact lifecycle and public record.
- **Recovery:** re-read `SCR-049/050`; no duplicate agreement.
- **Accessibility:** consent questions as labelled controls; publication state text; no countdown decision.
- **Screens:** `SCR-049`, `SCR-050`, `SCR-051`. **Components:** `UI-CMP-045`, `UI-CMP-048`, `UI-CMP-088`, `UI-CMP-021`.
- **Requirements:** `REQ-1120`. **Governing:** DIP-052/059–062/082/101/108–113.

### FLOW-019 — Alliance application/invitation response

- **Trigger:** `Apply` on `SCR-053` or `Admit`/`Decline` on `SCR-054`.
- **Preconditions:** Membership flow permits; role permission for administrative decisions; no duplicate application.
- **Actors:** Player applicant; alliance administration; interface; alliance system.
- **Sequence:** (1) Apply/invite → (2) pending application → (3) administration decision → (4) status (admitted/declined/expired/withdrawn) → (5) member/non-member state.
- **Alternative:** withdraw; decline; leave later (unblockable).
- **Failure:** permission denied → `ST-09`; duplicate → `ST-11`; expired → `ST-12`; privacy breach attempt → not rendered.
- **Cancellation:** applicant may withdraw while pending where the flow permits.
- **Completion:** membership state updated in-product; no external hop.
- **Recovery:** re-apply only where the rule permits; expired application is final for that object.
- **Accessibility:** applicant list permissioned; status text; confirmations.
- **Screens:** `SCR-053`, `SCR-054`. **Components:** `UI-CMP-049`, `UI-CMP-050`, `UI-CMP-053`, `OVL-03`.
- **Requirements:** `REQ-1121`. **Governing:** ALL-080–086; D-133; UD-040 Open.

### FLOW-020 — Alliance tax bracket change

- **Trigger:** `Create/edit bracket` or `Assign member` on `SCR-056`.
- **Preconditions:** Tax-management permission; valid name; rates integer 0–10,000 bp; member exists.
- **Actors:** Tax manager; interface; alliance system.
- **Sequence:** (1) Edit bracket/rates → (2) assignment → (3) effective turn and policy version → (4) confirmation → (5) version recorded; effect from the defined snapshot.
- **Alternative:** delete/disable bracket where permitted; 0% fallback shown.
- **Failure:** out-of-range → `ST-08`; permission → `ST-09`; stale policy → `ST-13`; missing tax term → `ST-11` (`ALF-22`).
- **Cancellation:** no version created before confirmation.
- **Completion:** new bracket version effective; receipts follow.
- **Recovery:** re-read version/history; a wrong version is corrected by a new version, not an edit.
- **Accessibility:** bp suffix announced; rates as labelled numeric fields; effective turn on confirm.
- **Screens:** `SCR-056`, `SCR-057`. **Components:** `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-088`, `UI-CMP-052`.
- **Requirements:** `REQ-1122`. **Governing:** ALL-179–187; UD-040/UD-045; D-141.

### FLOW-021 — Military operation submission

- **Trigger:** An offensive operation control on `SCR-061`.
- **Preconditions:** Owner; campaign state permits; OP/supply/readiness; protection/NAP/alliance checks pass; within per-turn limits.
- **Actors:** Nation owner; interface; warfare system; boundary.
- **Sequence:** (1) Choose operation/target → (2) show OP cost, supply, objective, expected effect, block reasons → (3) WAR-152 confirmation → (4) submitted/reserved → (5) resolves at P5 → (6) battle report/losses.
- **Alternative:** amend/cancel before freeze; choose another operation; do nothing.
- **Failure:** any block → `ST-11` with `WRF-` class; campaign expired → `ST-12`; invalid target → `ST-08`; reservation lost → `WRF-33`; duplicate → single-flight.
- **Cancellation:** before freeze per WFW-017; after freeze, none.
- **Completion:** operation resolved; report and losses authoritative.
- **Recovery:** re-read board; no automatic resubmission.
- **Accessibility:** OP/cost/effect text; threat band; confirmation ordered; destructive controls separated.
- **Screens:** `SCR-061`, `SCR-060`, `SCR-064`. **Components:** `UI-CMP-062`, `UI-CMP-057`, `UI-CMP-058`, `UI-CMP-088`.
- **Requirements:** `REQ-1123`, `REQ-1155`. **Governing:** WAR-039/046/073/085–088/152; WAR §12.3.

### FLOW-022 — War declaration

- **Trigger:** `Declare war` on `SCR-061`.
- **Preconditions:** Owner; 2 OP; 500 crowns; one outgoing campaign slot; protection/NAP/same-alliance checks pass; valid counterparty.
- **Actors:** Nation owner; interface; warfare system.
- **Sequence:** (1) Select counterparty/objective set → (2) show costs and public-record consequence → (3) confirmation → (4) `DECLARED_PENDING` → (5) resolves at the boundary.
- **Alternative:** cancel; choose a different operation.
- **Failure:** no slot/OP/crowns → `ST-11`; protection/NAP/alliance → `ST-11`; political state → `ST-11`; duplicate → `ST-13`.
- **Cancellation:** declarer may withdraw before P1 freeze; `VOID`; reservation released once.
- **Completion:** campaign declared; public record at activation.
- **Recovery:** re-read board; a void campaign is not re-declared automatically.
- **Accessibility:** consequence list; confirmation; public-record statement.
- **Screens:** `SCR-061`, `SCR-063`. **Components:** `UI-CMP-062`, `UI-CMP-088`, `OVL-01`, `UI-CMP-058`.
- **Requirements:** `REQ-1124`. **Governing:** WAR-145/152; AX-18.

### FLOW-023 — Settlement proposal and acceptance

- **Trigger:** `Propose settlement` or `Accept settlement` on `SCR-067`.
- **Preconditions:** Participant; campaign `ACTIVE`/`SUSPENDED`; one live settlement at a time; valid terms.
- **Actors:** Participants; interface; warfare system.
- **Sequence:** (1) Compose terms/durations → (2) confirm → (3) propose → (4) counterparty reviews → (5) accept/counter/decline/withdraw → (6) accepted then completed or failed.
- **Alternative:** counter; withdraw before acceptance; surrender.
- **Failure:** one-live conflict → `ST-13`; invalid/prohibited term → `ST-08`; expired → `ST-12`; acceptance failure → campaign `ACTIVE` (`WRF-33`).
- **Cancellation:** proposer may withdraw before acceptance; terms immutable after submission.
- **Completion:** settlement completed with its terms; or failed and returned to active.
- **Recovery:** re-read settlement state; no second live settlement.
- **Accessibility:** terms/durations ordered; no silence-as-consent; confirmation.
- **Screens:** `SCR-067`, `SCR-063`. **Components:** `UI-CMP-047`, `UI-CMP-088`, `UI-CMP-021`, `OVL-01`.
- **Requirements:** `REQ-1125`. **Governing:** WAR-122/125/126/127/138.

### FLOW-024 — Surrender

- **Trigger:** `Surrender` on `SCR-067`.
- **Preconditions:** Nation owner; campaign `ACTIVE`/`SUSPENDED`; surrender always available as off-ramp.
- **Actors:** Nation owner; interface; warfare system.
- **Sequence:** (1) Open surrender panel → (2) consequences (`TERM_CEASEFIRE`; campaign ends `SURRENDER`; opponent limited victory) → (3) destructive confirmation → (4) recorded at P5.3 → (5) campaign ends.
- **Alternative:** continue; propose settlement.
- **Failure:** already ended → `ST-12`; wrong role → `ST-09`.
- **Cancellation:** cannot be withdrawn after P5.3; before confirmation only.
- **Completion:** campaign ended by surrender; no refusal path.
- **Recovery:** none after resolution; history retains the record.
- **Accessibility:** separated destructive control; consequence list; exact confirmation; no default focus on surrender.
- **Screens:** `SCR-067`. **Components:** `UI-CMP-087`, `OVL-02`, `UI-CMP-088`.
- **Requirements:** `REQ-1126`, `REQ-1156`. **Governing:** WAR-131/132/133.

### FLOW-025 — Objective accept/dismiss

- **Trigger:** `Accept` or `Dismiss` on `SCR-009`/`SCR-071`.
- **Preconditions:** Objective in `AVAILABLE` or optional state; no forced participation.
- **Actors:** Player; interface; world/objectives system.
- **Sequence:** (1) Review objective → (2) accept or dismiss → (3) state recorded → (4) progress if accepted.
- **Alternative:** leave; view category; dismiss without penalty.
- **Failure:** invalid transition → `ST-11` (`WPF-19`); expired → `ST-12`.
- **Cancellation:** dismissal is penalty-free; withdrawn objectives retain earned tiers where the rule permits.
- **Completion:** objective state updated; reward class only where defined.
- **Recovery:** a dismissed objective may return where the flow permits; progress recomputes.
- **Accessibility:** optionality text; progress label; dismissal reachable.
- **Screens:** `SCR-009`, `SCR-071`. **Components:** `UI-CMP-065`, `UI-CMP-016`, `UI-CMP-086`.
- **Requirements:** `REQ-1127`. **Governing:** WEP-203–215/232/244/248.

### FLOW-026 — Deferred reward claim

- **Trigger:** A claim control where the B-11 flow provides one.
- **Preconditions:** `ELIGIBLE` or `CLAIM_PENDING`; deferred claim exists; no duplicate claim.
- **Actors:** Player; interface; world/reward system.
- **Sequence:** (1) View reward → (2) claim → (3) confirmation → (4) `CLAIM_PENDING`/`GRANTED` → (5) ledger/record.
- **Alternative:** leave deferred; view history.
- **Failure:** duplicate → deduplicated; invalid state → `ST-11`; claim failure → retry after re-read.
- **Cancellation:** no claim. **Completion:** granted with class/quantity/key; or remains deferred.
- **Recovery:** deferred remains visible; no expiry through absence.
- **Accessibility:** class/quantity/state text; claim keyboard reachable.
- **Screens:** `SCR-073`, `SCR-075`. **Components:** `UI-CMP-066`, `UI-CMP-073`, `UI-CMP-088`.
- **Requirements:** `REQ-1128`. **Governing:** WEP-240/582/705.

### FLOW-027 — Alert open and deep link

- **Trigger:** An alert/notification row.
- **Preconditions:** Authenticated; row exists; destination subject to visibility.
- **Actors:** Player; interface; notification layer; owning system.
- **Sequence:** (1) Open row → (2) resolve destination → (3a) permitted object loads → (3b) denied/retired/expired/absent state renders → (4) history retains the entry.
- **Alternative:** dismiss mutable notice; mark read; filter history; mute where permitted.
- **Failure:** destination failed → `ST-14` with retry; session lost → re-auth; offline → read-only history.
- **Cancellation:** back to `SCR-019`; dismiss where permitted.
- **Completion:** player reaches the object or its owning unavailable state.
- **Recovery:** retry from `SCR-019`; the event is never lost.
- **Accessibility:** count announced once; row link named; destination heading focus; no focus steal.
- **Screens:** `SCR-019`, owning screens. **Components:** `UI-CMP-069`, `UI-CMP-027`, `OVL-05`.
- **Requirements:** `REQ-1129`, `REQ-1184`. **Governing:** REQ-731; DIP-114/116.

### FLOW-028 — Report submission

- **Trigger:** `Submit report` on `SCR-081`.
- **Preconditions:** Authenticated; required MOD-002 fields; intake available.
- **Actors:** Reporter; interface; moderation intake.
- **Sequence:** (1) Complete category/subject/window/text → (2) evidence attached separately → (3) confirmation states "this is an accusation" → (4) acknowledgement and case reference → (5) `SCR-082` status.
- **Alternative:** cancel; contact support (separate route).
- **Failure:** missing field → `ST-08`; intake unavailable → retryable `ST-14`, nothing lost; duplicate → one reference.
- **Cancellation:** no report before confirmation.
- **Completion:** acknowledgement and case reference; no outcome promised.
- **Recovery:** retry preserves intake; case reference recoverable from `SCR-082`.
- **Accessibility:** labels; evidence control accessible; acknowledgement announced.
- **Screens:** `SCR-081`, `SCR-082`. **Components:** `UI-CMP-074`, `UI-CMP-076`, `UI-CMP-083`, `UI-CMP-084`, `OVL-01`.
- **Requirements:** `REQ-1130`. **Governing:** MOD-002/007; FR-001/006.

### FLOW-029 — Appeal submission

- **Trigger:** `Submit appeal` on `SCR-083`.
- **Preconditions:** Tier permits appeal (`T1`+); a decision exists; route never blocked.
- **Actors:** Sanctioned player; interface; moderation system.
- **Sequence:** (1) Eligibility/grounds → (2) submit → (3) confirmation → (4) status `FILED`/`IN_FORCE` → (5) decision outcome.
- **Alternative:** withdraw where permitted; support; view case.
- **Failure:** tier has no appeal (`T0`) → control absent with reason; duplicate → `ST-13`; outage → retry; window extended by outage where the rule says.
- **Cancellation:** before submission only; withdrawal per rule.
- **Completion:** appeal recorded; decision reasons shown later.
- **Recovery:** the appeal route remains reachable under every restriction (`MOD-013/015`).
- **Accessibility:** focus remains on the appeal form despite restriction banners; status ladder text.
- **Screens:** `SCR-083`, `SCR-084`. **Components:** `UI-CMP-085`, `UI-CMP-021`, `UI-CMP-017`, `UI-CMP-084`.
- **Requirements:** `REQ-1131`, `REQ-1186`. **Governing:** MOD-013/015/042.

### FLOW-030 — Account closure request/cancel

- **Trigger:** `Request closure` on `SCR-012`; `Cancel closure` during cooling.
- **Preconditions:** Authenticated; account not already closed; cooling cancel available.
- **Actors:** Account holder; interface; account system.
- **Sequence:** (1) Read consequences → (2) confirmation → (3) `CLOSURE_REQUESTED` + cooling end turn → (4a) cancel → `ACTIVE`; (4b) cooling elapses → `CLOSED`.
- **Alternative:** cancel; support; data request.
- **Failure:** already closing → `ST-13`; session expired → re-auth; network → uncertain, re-read.
- **Cancellation:** cancelling during cooling restores the account.
- **Completion:** closure entered/closed as stated; nation retired at closure.
- **Recovery:** re-read `SCR-011`; no hidden deletion.
- **Accessibility:** consequence list first; safe confirmation; cooling in turns/UTC.
- **Screens:** `SCR-012`, `SCR-011`. **Components:** `UI-CMP-088`, `OVL-01`, `UI-CMP-086`, `UI-CMP-017`.
- **Requirements:** `REQ-1132`. **Governing:** ACC-043; D-041.

### FLOW-031 — Reroll exact-phrase flow

- **Trigger:** `Permanently delete …` on `SCR-090`.
- **Preconditions:** Re-auth within 5 minutes; exact current nation name; no RRL-021 block.
- **Actors:** Nation owner; interface; account/nation system.
- **Sequence:** (1) Re-auth → (2) consequence list → (3) exact phrase → (4) destructive confirmation → (5) nation retired, replacement available → (6) `SCR-007`.
- **Alternative:** cancel; use the surrender off-ramp if blocked by war.
- **Failure:** wrong re-auth/phrase → `ST-08`; block → `ST-11`; concurrent operation → `ST-13`.
- **Cancellation:** before confirmation only; after, irreversible.
- **Completion:** old nation `retired — rerolled`; replacement `New nation`; no protection renewal.
- **Recovery:** none after confirmation; before, cancel restores nothing changed.
- **Accessibility:** phrase instruction linked; match announced; cancel first; no autocomplete.
- **Screens:** `SCR-090`, `SCR-007`. **Components:** `UI-CMP-090`, `OVL-02`, `UI-CMP-089`, `UI-CMP-087`.
- **Requirements:** `REQ-1133`, `REQ-1156`. **Governing:** RRL-005/006/021; D-039.

### FLOW-032 — Administrative moderation decision

- **Trigger:** `Propose measure` / `Apply` on `SCR-094`.
- **Preconditions:** Role and tier authority; evidence class; two-person state where required; step-up if required.
- **Actors:** Reviewer; second reviewer; interface; moderation/audit system.
- **Sequence:** (1) Review case → (2) propose tier/scope → (3) second review where required → (4) confirmation → (5) apply → (6) audit append; subject notice through player surface.
- **Alternative:** escalate; no action; record.
- **Failure:** role/tier → `ST-09`; missing second review → `unsegregated` or blocked; conflict → `ST-13`; audit failure → action not reported applied.
- **Cancellation:** before apply; no state change.
- **Completion:** measure applied with end/review turn and appeal route; audit record.
- **Recovery:** append-only correction; re-read case.
- **Accessibility:** tier/scope text; destructive apply separated; audit notice.
- **Screens:** `SCR-092`…`SCR-096`, `SCR-100`. **Components:** `UI-CMP-010`, `UI-CMP-022`, `UI-CMP-088`, `OVL-02`, `UI-CMP-017`.
- **Requirements:** `REQ-1134`. **Governing:** MOD-022/036/037/042; ADM-003/021/022.

### FLOW-033 — Boundary reconnection and stale-data recovery

- **Trigger:** Reconnection after offline, session expiry, refresh or an uncertain submission.
- **Preconditions:** Previously authenticated; an affected screen/object.
- **Actors:** Player; interface; authoritative systems.
- **Sequence:** (1) Detect reconnect → (2) `ST-16` reconnecting → (3) re-read affected object/turn → (4) replace stale values with authoritative values + as-of → (5) if an uncertain action exists, show its actual state before any retry → (6) resume.
- **Alternative:** stay read-only; sign in again; open the digest.
- **Failure:** refresh fails → `ST-14` with retry; session invalid → re-auth; boundary `INTERRUPTED`/`FAILED` → named state, no lost-turn claim.
- **Cancellation:** leave; no queued action.
- **Completion:** the player sees the authoritative state and knows whether their action completed.
- **Recovery:** never auto-repeat a committing action; retry only after reconciliation or with the owning safe key.
- **Accessibility:** reconnection state announced; refreshed values not announced cell-by-cell; focus preserved.
- **Screens:** Shell, owning screens, `SCR-016`. **Components:** `UI-CMP-007`, `UI-CMP-019`, `OVL-06`, `UI-CMP-012`.
- **Requirements:** `REQ-1135`, `REQ-1188`…`REQ-1193`. **Governing:** TR-039/075/080.

---

## 5. Onboarding and tutorial specifications (TUT-01…TUT-12)

Every tutorial records the eighteen mandated fields. Common rules: safe demonstrations are read-only; the player performs any real action with the normal confirmation; every step is skippable; progress is account-scoped; no reward or advantage is granted; help is reopenable; accessibility matches normal play.

### TUT-01 — First landing orientation

| Field | Content |
|---|---|
| ID / name | `TUT-01` — First landing orientation |
| Learning objective | Understand the fictional premise, browser game and the register/login path |
| Intended player | New visitor / new account |
| Prerequisites | None |
| Entry condition | First visit to `SCR-001` or first entry to `SCR-008` |
| Starting screen | `SCR-001` (public) or `SCR-008` (authenticated) |
| Ordered steps | 1 Premise; 2 what the game is; 3 cadence; 4 entry path; 5 fictional-world and multi-account notices |
| Explanation | Read-only cards using the real public page; no data fabrication |
| Expected interaction | Read, expand sections, choose register/login |
| Expected result | Player can state what the game is and how to enter |
| Validation | No gameplay action; step completion is view/skip only |
| Failure/recovery | None required; re-open from `SCR-078` |
| Skip | Always available; preference recorded |
| Completion condition | Steps viewed or skipped; recorded once |
| Re-entry | Replay read-only; no completion re-grant |
| Accessibility | Keyboard accordion; headings; no auto-advance |
| Related requirements | `REQ-1175`, `REQ-1172`…`REQ-1174` |

### TUT-02 — Turn and boundary

| Field | Content |
|---|---|
| ID / name | `TUT-02` — Turn and boundary |
| Learning objective | Understand the two-hour UTC cadence, phase P0–P7 and "now vs next turn" |
| Intended player | New nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-008` step or `SCR-016` help |
| Starting screen | `SCR-016` with the real turn state |
| Ordered steps | 1 current turn/boundary; 2 phase position; 3 where an action lands; 4 what "pending" means; 5 what happens if a turn is interrupted |
| Explanation | Uses the real `SCR-016`; no simulated settlement |
| Expected interaction | Read; open queued actions; return |
| Expected result | Player understands when an action resolves |
| Validation | Read-only; no action |
| Failure/recovery | Turn state unavailable → tutorial pauses with explanation |
| Skip | Available |
| Completion condition | Viewed/skipped; recorded once |
| Re-entry | Replay read-only |
| Accessibility | Countdown announced as a polite state, not per tick |
| Related requirements | `REQ-1175` |

### TUT-03 — Reading the Command Digest

| Field | Content |
|---|---|
| ID / name | `TUT-03` — Reading the Command Digest |
| Learning objective | Understand re-entry: settled changes, pending acts and next action |
| Intended player | New/returning player |
| Prerequisites | Authenticated |
| Entry condition | `SCR-008` or `SCR-013` help |
| Starting screen | `SCR-013` |
| Ordered steps | 1 digest rows and cause; 2 pending totals; 3 due boundary; 4 opening an item; 5 returning |
| Explanation | Uses the real digest; empty digest explained honestly |
| Expected interaction | Read; open a row; return |
| Expected result | Player can identify the next meaningful action |
| Validation | Read-only |
| Failure/recovery | Digest unavailable → pause; retry |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Row headings; count announced once |
| Related requirements | `REQ-1175`, `REQ-1091` |

### TUT-04 — Treasury and the three balances

| Field | Content |
|---|---|
| ID / name | `TUT-04` — Treasury and the three balances |
| Learning objective | Read total/reserved/available, forecasts and history without treating reserved as spendable |
| Intended player | New nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-029` help |
| Starting screen | `SCR-029` |
| Ordered steps | 1 triple; 2 number types; 3 forecast; 4 reserved meaning; 5 history cause |
| Explanation | Real values (true zero allowed); no simulated spend |
| Expected interaction | Read; open reports/resources |
| Expected result | Player can state available vs reserved |
| Validation | Read-only; no order submitted |
| Failure/recovery | Value unavailable → named state; tutorial continues with the explanation |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Triple announced together with units/as-of |
| Related requirements | `REQ-1176`, `REQ-1093` |

### TUT-05 — Political state, approval and stability

| Field | Content |
|---|---|
| ID / name | `TUT-05` — Political state, approval and stability |
| Learning objective | Read the six-state banner, six supports and stability in basis points |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-021`/`SCR-023` help |
| Starting screen | `SCR-021` |
| Ordered steps | 1 banner and cause; 2 government vs administration; 3 six supports; 4 approval/stability; 5 policy cooldown |
| Explanation | Real political state; no invented bands |
| Expected interaction | Read; open approval detail; return |
| Expected result | Player can explain why approval is what it is |
| Validation | Read-only |
| Failure/recovery | State unavailable → pause |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | bp + text label announced; supports table |
| Related requirements | `REQ-1176`, `REQ-1096` |

### TUT-06 — Production policy and chains

| Field | Content |
|---|---|
| ID / name | `TUT-06` — Production policy and chains |
| Learning objective | Understand standing policy vs manual order, capacity, inputs, power and maintenance |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-032`/`SCR-044` help |
| Starting screen | `SCR-044` |
| Ordered steps | 1 chain state; 2 standing policy; 3 manual order; 4 reservation; 5 `UNMAINTAINED`/blocked |
| Explanation | Uses real chain values; a demonstration preview is read-only |
| Expected interaction | Read; open policy; optional real action with normal confirmation |
| Expected result | Player can choose a policy without overbooking |
| Validation | Any real action uses `FLOW-009`/`FLOW-010` and its confirmation |
| Failure/recovery | No capacity → tutorial explains; no bypass |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Capacity/inputs text; errors linked |
| Related requirements | `REQ-1176` |

### TUT-07 — City infrastructure and construction

| Field | Content |
|---|---|
| ID / name | `TUT-07` — City infrastructure and construction |
| Learning objective | Understand infrastructure, housing, DC, the one-slot rule and the preview |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-041`/`SCR-043` help |
| Starting screen | `SCR-041` |
| Ordered steps | 1 twelve-city view; 2 city detail; 3 DC; 4 preview; 5 one-slot and refund |
| Explanation | Real city values; no simulated construction |
| Expected interaction | Read; open preview; optional real order with confirmation |
| Expected result | Player can read the preview and slot state |
| Validation | Any real order uses `FLOW-014` |
| Failure/recovery | No slot → explanation; no bypass |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | City rows headed; projections labelled |
| Related requirements | `REQ-1176` |

### TUT-08 — Directed trade basics

| Field | Content |
|---|---|
| ID / name | `TUT-08` — Directed trade basics |
| Learning objective | Understand offer, counter, accept, decline, expiry and no-reservation-at-create |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-035` help |
| Starting screen | `SCR-035` |
| Ordered steps | 1 parties-only; 2 chain states; 3 both sides; 4 acceptance re-check; 5 expiry/history |
| Explanation | Uses real inbox; no offer is submitted by the tutorial |
| Expected interaction | Read; open detail; optional real offer with confirmation |
| Expected result | Player can state when reservation occurs |
| Validation | Any real action uses `FLOW-011`…`FLOW-013` |
| Failure/recovery | Inbox empty → explain how offers arrive |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Terms in reading order; status text |
| Related requirements | `REQ-1177` |

### TUT-09 — Diplomacy and alliance boundaries

| Field | Content |
|---|---|
| ID / name | `TUT-09` — Diplomacy and alliance boundaries |
| Learning objective | Understand directional posture, proposal lifecycle, publication and alliance limits |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-047`/`SCR-053` help |
| Starting screen | `SCR-047` |
| Ordered steps | 1 posture per direction; 2 proposal lifecycle; 3 parties-only terms; 4 activation/publication; 5 alliance has no military authority |
| Explanation | Uses real diplomacy screens; no proposal submitted |
| Expected interaction | Read; open pair/alliance; optional real proposal with confirmation |
| Expected result | Player understands consent and publication |
| Validation | Any real action uses `FLOW-017`/`FLOW-018` |
| Failure/recovery | No counterparty → explain how to find one |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Directional groups labelled; ten fields ordered |
| Related requirements | `REQ-1177` |

### TUT-10 — Protection, readiness and owner-only military action

| Field | Content |
|---|---|
| ID / name | `TUT-10` — Protection, readiness and owner-only military action |
| Learning objective | Understand protection as visibility-only, readiness bands and owner-only action |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-059`/`SCR-089` help |
| Starting screen | `SCR-089` |
| Ordered steps | 1 protection state/end turn; 2 what it does not do; 3 readiness bands; 4 owner-only board; 5 surrender off-ramp |
| Explanation | Real state; no operation submitted |
| Expected interaction | Read; open forces/board; optional real action with WAR-152 confirmation |
| Expected result | Player understands protection and command limits |
| Validation | Any real action uses `FLOW-021`…`FLOW-024` |
| Failure/recovery | Protected/blocked → explanation; no bypass |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | State/end turn pinned; threat band text |
| Related requirements | `REQ-1177` |

### TUT-11 — Objectives and progression

| Field | Content |
|---|---|
| ID / name | `TUT-11` — Objectives and progression |
| Learning objective | Understand optional objectives, tiered progress, standings and eight-layer progression |
| Intended player | Nation owner |
| Prerequisites | Nation created |
| Entry condition | `SCR-071` help |
| Starting screen | `SCR-071` |
| Ordered steps | 1 categories; 2 optionality/dismissal; 3 progress; 4 standings denominator/window; 5 eight layers |
| Explanation | Uses the real objective/standing data or honest empty state |
| Expected interaction | Read; optional accept/dismiss |
| Expected result | Player understands no presence or payment is required |
| Validation | Any real action uses `FLOW-025`/`FLOW-026` |
| Failure/recovery | No objectives → honest empty explanation |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Optionality text; denominator announced |
| Related requirements | `REQ-1178` |

### TUT-12 — Notifications, help, support and reporting

| Field | Content |
|---|---|
| ID / name | `TUT-12` — Notifications, help, support and reporting |
| Learning objective | Understand notification tiers, deep links, help, support vs report and the appeal route |
| Intended player | All players |
| Prerequisites | Authenticated |
| Entry condition | `SCR-019`/`SCR-078`/`SCR-087` help |
| Starting screen | `SCR-019` |
| Ordered steps | 1 alert tiers; 2 opening a destination; 3 non-opt-out; 4 help/rule anchors; 5 support vs report; 6 appeal always reachable |
| Explanation | Real alerts/history; no report submitted |
| Expected interaction | Read; open a permitted destination; route to help/support |
| Expected result | Player can find help and the right intake |
| Validation | Any real intake uses `FLOW-028`/`FLOW-029` |
| Failure/recovery | Empty alerts → explain how events arrive |
| Skip | Available |
| Completion condition | Viewed/skipped |
| Re-entry | Replay read-only |
| Accessibility | Count announced once; appeal route focusable under restriction |
| Related requirements | `REQ-1178`, `REQ-1187` |

---

## 6. Journey–flow integrity

1. Every journey names at least one flow and at least one screen; every flow names at least one journey in its requirement rows. See parent Matrix A/B/H.
2. No journey or flow references `SCR-020`, `SCR-038`, `SCR-039`, `SCR-068` or `SCR-077` as an available surface.
3. Administrative flows appear only under `JRN-M` and only inside the Admin root.
4. No flow creates an action, notification, event, reward or permission; each cites its governing rule.
5. Every committing flow uses the same confirmation/single-flight/failure model (`IP-01`, `IP-02`, `DUP-`, `CFM-`).
6. Every tutorial is optional and safe; no tutorial is a gate on play except the account/nation setup the owning rules require.

## 7. Traceability note

Requirement rows are owned by the parent §18.2. This companion supplies the journey, flow and tutorial bodies those rows reference; it does not maintain a second requirement register. Matrices A–C and E–I are in the parent; Matrix D is in the state companion.
