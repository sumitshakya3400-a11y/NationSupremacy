# B-13C — Interaction flows and player experience

**Prompt:** Stage 2 Prompt 13C — complete interaction flows and player-experience specifications (2026-11-13).
**Status:** COMPLETE at the interaction-specification level. **No frontend, route, component, state store, migration, gameplay or runtime behaviour exists.** Every statement below is a specification; none is an implementation, a test result, a WCAG conformance claim or an owner acceptance of a game rule.
**Authority basis:** the owner's Prompt 13C instruction (2026-11-13); [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (D-014); the owner-accepted Prompt 13A package; the completed B-13 screen/component package (Prompt 13B and 13B-C1/13B-C1-R1); the accepted B-02…B-12 rulebooks; decisions **D-198…D-219** and the new **D-220…D-232**.
**Companions (same `22_` serial family; D-220):**
- [`22_player_journey_specifications.md`](22_player_journey_specifications.md) — the thirteen player journeys `JRN-A`…`JRN-M`, the thirty-three interaction flows `FLOW-001`…`FLOW-033` and the twelve tutorials `TUT-01`…`TUT-12`.
- [`22_interaction_states_and_feedback.md`](22_interaction_states_and_feedback.md) — the eighteen interaction states `ST-01`…`ST-18`, loading/empty/success/failure behaviour, the per-component state map (90 `UI-CMP` + 8 `OVL`), validation `VAL-`, confirmation `CFM-`, duplicate-submission `DUP-`, error `ERR-`, recovery `REC-`, accessibility interaction `AXI-`, notification `NTF-`, offline `OFF-` specifications, and Matrix D.

**Reading rule.** This file is the authoritative register for interaction authority, conventions, journey architecture, global state and feedback doctrine, accessibility/onboarding/notification/offline architecture, cross-screen consistency, the `REQ-1090`…`REQ-1203` block and Matrices A–C, E–I. The journey companion owns every `JRN-`, `FLOW-` and `TUT-` body. The state companion owns every `ST-`, `VAL-`, `CFM-`, `DUP-`, `ERR-`, `REC-`, `AXI-`, `NTF-`, `OFF-` body and Matrix D. No register is duplicated.

**Predecessor reconciliation.** Prompt 13B-C1-R1 is complete: B-13 §29 is labelled as the historical 13B impact assessment and B-13 §31 preserves the later correction record. This pass does not reopen Prompt 13B. 13B already reserved the journey boundary at B-13 §30.2; this document fills exactly that boundary and no other.

---

## 1. Document authority and scope

### 1.1 What this document does

It defines how a player moves through the 100 already-specified screens: entry, context, available and unavailable actions, validation, confirmation, success, failure, cancellation, return, feedback, notifications and cross-screen reflection. It defines the interaction conventions that make the screens one application, the state model that every flow uses, the accessibility duties that apply during interaction, the onboarding/tutorial architecture, the notification and offline posture, and the complete requirement and traceability block for Prompt 13C.

### 1.2 What this document does not do

- It does not implement frontend or backend code, create a framework or route table, select a state-management library, define API contracts or touch Supabase, authentication, migrations or gameplay.
- It does not create, change or reinterpret a game rule, formula, parameter, number, requirement status or owner-reserved decision.
- It does not renumber, redesign, add or remove any `SCR-`, `UI-CMP-` or `OVL-` identifier; the 13B inventory is preserved exactly.
- It does not perform Prompt 13D's independent completeness audit, final integration acceptance, acceptance-test execution or closure report.
- It does not claim WCAG 2.2 AA conformance. Accessibility statements are **implementation requirements to be verified on a built UI** (§11.7).
- It does not promise offline gameplay, offline action execution, automatic committing retries or real-time behaviour.

### 1.3 Scope boundary summary

| Boundary | Position in this pass |
|---|---|
| Frontend implementation | NOT AUTHORIZED and NOT PERFORMED |
| Backend/API/database/auth | NOT AUTHORIZED and NOT PERFORMED |
| Game-rule change | None; B-02…B-12 remain authoritative |
| New gameplay action | None; every flow executes only an action an owning rule already defines |
| Prompt 13D | NOT STARTED; §21.4 hands over |
| Prompt 14/15 | NOT STARTED |
| Global Trade (`SCR-038/039`) | G-1…G-6 not met; screens absent; no flow, tutorial or notification implies availability |
| Favorites (`SCR-020`), World Health (`SCR-077`), intelligence (`SCR-068`) | Conditional/Provisional; absent; no flow, tutorial or notification is specified for them |
| Owner-reserved brand values | Preserved open (`13A-OQ-001/002`, D-219) |

---

## 2. Relationship to Prompt 13A and Prompt 13B

### 2.1 Inheritance from 13A

| 13A artefact | How 13C uses it |
|---|---|
| `13A-PR-01`…`13A-PR-16` | Applied as interaction duties: the turn is the heartbeat; state never lives only in the UI; the disabled control explains itself; confirmation-first; deep links; honesty about uncertainty. |
| 13A §6 application states (13 values) | Mapped into the `ST-` interaction taxonomy (§10.2) without renaming the 13B component states. |
| `13A-RD-01`…`13A-RD-08` | Keyboard, focus, reflow and must-not-simplify duties are restated as interaction requirements in §11 and the state companion §12. |
| `13A-DS-07`…`13A-DS-15` | Accessibility, token and localization duties bind every flow. `UR-010` remains an `INDEPENDENT_ACCESSIBILITY_REQUIREMENT`; `13A-DS-07` is unchanged. |
| `13A-UR-001`…`13A-UR-048` | Cited; not re-allocated. `13A-UR-045` (≤3 steps) is checked by Matrix A journey step counts where applicable. |
| `13A-OQ-001`…`13A-OQ-016` | Preserved; `13A-OQ-006` (notification tiers), `13A-OQ-008` (context panel), `13A-OQ-012` (pins), `13A-OQ-014` (mobile mode) remain open/provisional. |

### 2.2 Inheritance from 13B

| 13B artefact | How 13C uses it |
|---|---|
| 100 `SCR-` bodies (A–K) | The authoritative screen content. 13C adds sequencing, state transitions and feedback; it never restates or changes screen content. |
| 90 `UI-CMP-` components + 8 `OVL-` overlays | The authoritative component bodies. 13C maps interaction states to them (state companion §7) and never changes their internals. |
| D-209 navigation model | Canonical parents, route keys, aliases and conditional absence are the navigation basis of every journey. |
| D-214 confirmation-first / disabled-reason / cooldown-on-control | Extended to full sequences: trigger → validation → confirmation → in-flight → authoritative outcome → cross-screen reflection. |
| D-215 overlay page-equivalence and 13B/13C boundary | Every overlay interaction has a page-reachable equivalent; 13C owns sequencing and recovery. |
| D-216 conditional-surface absence | Conditional screens have journeys only where a gate-independent absence duty exists; none has an active flow. |
| `REQ-870`…`REQ-1089` | Preserved unchanged; `REQ-1014` (component state vocabulary) constrains §10. |

### 2.3 Boundary discipline

Prompt 13B §30.2 listed journeys, cross-system sequences, loading/empty/success/failure journeys, validation/error-handling logic, notification/feedback sequences, onboarding/tutorials and cross-screen behavioural audits as Prompt 13C work. Those are delivered here. Nothing in 13B's screen or component content is altered.

---

## 3. Governing design principles

### 3.1 Inherited principles

`13A-PR-01`…`13A-PR-16` remain the design principles. This pass does not replace them.

### 3.2 Interaction principles (new; Category B under D-014)

| ID | Principle | Consequence for interaction design |
|---|---|---|
| `IP-01` | **One action, one intent, one confirmation.** | A committing action originates from one control, names one authoritative effect and is confirmed once. No secondary control may bypass or pre-answer the confirmation. |
| `IP-02` | **The interface never asserts an outcome the server has not produced.** | "Submitted" means a request was accepted; "settled" means the authoritative system confirmed it. A click, animation or toast is never proof. |
| `IP-03` | **Every state is explainable and every blocked action says why.** | No dead end, blank panel or unexplained disabled control; every block names a rule class and, where the rule defines one, the next eligible turn. |
| `IP-04` | **Uncertain is a displayed state, not a guess.** | Lost responses, interrupted turns and unverifiable submissions render as uncertain until the authoritative system resolves them (`TR-075`). |
| `IP-05` | **The player can always leave safely.** | Cancel, back, Escape and navigation never commit; unsent input is preserved where safe; destructive actions never sit adjacent to primary ones. |
| `IP-06` | **One grammar across systems.** | The same confirmation, disabled-reason, pending, error, empty and suppression patterns apply in Economy, Politics, Foreign, War, World and Account. |
| `IP-07` | **Time is in turns and UTC boundaries.** | Countdowns are cosmetic aids; the source of truth is the turn and the boundary. No interaction implies real-time urgency (`13A-PR-01`, D-021, DP-002). |
| `IP-08` | **Identity is stable and shared.** | The same nation, alliance, war, treaty, offer, city or event has one canonical view and one canonical identity everywhere (§15.2). |
| `IP-09` | **Permission is server-authoritative and presentation never grants it.** | A rendered control can still fail; it fails closed with the owning restriction class (`REQ-1088`). |
| `IP-10` | **Accessibility is interaction, not an after-layer.** | Every journey is completable by keyboard and understood by assistive technology; focus, announcement and error association are part of each flow (§11). |
| `IP-11` | **Notification never creates a fact.** | A notification points at an existing event; opening, dismissing or muting never changes the underlying record (`REQ-731`, `UR-029`). |
| `IP-12` | **Re-entry beats attendance.** | Digest-first, inbox-first and "since you last looked" are the returning-player defaults; no streak, punishment or catch-up mechanic is introduced (`13A-PR-06`, D-021). |

---

## 4. Player identity, account and nation context

### 4.1 Three separate contexts

The account, the nation and the account pair are three independent state machines (D-031, D-032, D-034, D-041). Every journey names which context it acts on:

| Context | Meaning | Primary surfaces |
|---|---|---|
| **Account** | Persistent person-level identity (ten ACC states) | `SCR-002`…`SCR-006`, `SCR-011`, `SCR-012`, `SCR-079`, `SCR-080`, `SCR-085` |
| **Nation** | Replaceable object owned 0..1 per account; one active nation | `SCR-007`…`SCR-010`, `SCR-013`…`SCR-090` |
| **Pair** | Shared-network relationship between two accounts (five D-034 states) | `SCR-084`, `SCR-086`; never public (`NET-050`) |

### 4.2 Context rules that bind every interaction

1. **No nation action without an active, eligible nation.** An unverified account sees the verification gate (`SCR-006`) instead of nation surfaces (D-029).
2. **Account-level actions never masquerade as nation actions.** Closure, security and reroll live under Account; the game surfaces show their consequence but do not host the control (`SCR-011`, `SCR-012`, `SCR-090`).
3. **Pair state is never a game state.** A pair restriction is explained in its own surface (`SCR-086`) and never rendered as a political state, a sanction on a nation page or a ranking fact (NET-023/050).
4. **Reroll replaces the nation, not the account.** Tutorial progress and preferences survive; protection does not renew; sanctions survive (D-039, D-040, RRL-005/006/020).
5. **The shell identity strip shows only what the viewer may see.** Public viewers never receive authenticated values; other players receive only public fields (TR-021/022, `REQ-974`).

---

## 5. Interaction architecture

### 5.1 Layers

| Layer | Owner | 13C rule |
|---|---|---|
| **Shell** (`UI-CMP-001`…`UI-CMP-011`) | D-201 / 13B | Never replaced by a full-page spinner; identity, navigation, alert indicator, breadcrumb, context and footer persist through loading and errors (`REQ-970`). |
| **Screen** (100 `SCR-`) | 13B A–K bodies | One primary register; one screen identity; no duplicate route. |
| **Component** (90 `UI-CMP` + 8 `OVL`) | 13B component catalogue | State names come from the 13B eleven-state vocabulary; interaction sequencing comes from 13C. |
| **Flow** (`FLOW-`) | 13C | A reproducible sequence across screens with one authoritative outcome. |
| **Journey** (`JRN-`) | 13C | A player goal spanning flows and screens. |
| **Tutorial** (`TUT-`) | 13C | Optional, safe teaching layered over journeys; never a second game. |

### 5.2 Request → outcome model

Every committing interaction uses one model, whatever the system:

1. **Trigger** — the player activates one control.
2. **Local state** — the interface performs **presentation validation** only (format, required fields, obvious bounds) and displays the confirmation required by the owning rule.
3. **Submission** — after explicit confirmation, the control enters single-flight `pending`; repeated activations are ignored while in flight.
4. **Acceptance** — the authoritative system accepts or rejects. The interface may show **accepted/processing**, never **completed**.
5. **Resolution** — the owning system settles at its defined point (immediate, action-specific, or a boundary phase P0–P7). Only then may the interface show success and the resulting state.
6. **Reflection** — the object, the Inbox, the digest, the alert indicator and the owning screens reflect the new state from the same authoritative record.

### 5.3 What the interface may calculate

The interface may display only values the authoritative system supplies or that are explicitly derived by an owning rule (for example `available = total − reserved`, display formatting, static labels). It may not simulate a trade, predict a combat result, pre-compute a tax, invent a cooldown value or resolve an objective locally (`13A-PR-11`, `REQ-1088`). Forecasts must carry their forecast label and assumptions (`ECN-178`, `REQ-1064`).

---

## 6. Navigation and transition behaviour

### 6.1 Route and return model

1. Every screen has one canonical route key and one canonical parent (D-209; B-13 §7.2).
2. Breadcrumbs appear at depth ≥ 2; every ancestor is a working link (`REQ-973`).
3. Returning from a detail/task screen goes to the canonical parent unless the entry breadcrumb supplies a deeper return; a return never lands on a Conditional, role-denied or absent surface (B-13 §7.2).
4. Back/forward uses the browser history; the application rehydrates the screen from the current authoritative state, not from a cached rendered state.
5. A deep link lands on a titled screen with its own loading, permission and edge states; a deep link to an unavailable object renders the owning unavailable/retired/denied state, never a fabricated object.
6. Route changes update the page title and move focus to the screen heading (§11.4; `REQ-1081`).
7. Conditional screens (`SCR-020/038/039/077`) have **no rendered route** until their gate; Provisional `SCR-068` has no production route or link (B-13 §7.2; D-216).
8. Admin routes live only inside the Admin root and are denied without disclosing case data (`REQ-978`, `REQ-1037`).

### 6.2 Transition states

- **Navigation loading:** shell persists; the destination region shows its skeleton; previously confirmed context stays readable where safe; the destination is announced as loading (§10).
- **Slow response:** after the owning screen's content has not arrived, the loading state must state what is being loaded and keep navigation available; it must not pretend completion.
- **Interrupted navigation:** if the destination cannot load, the screen shows the failure anatomy (§10.7) with retry and a safe return; the previous screen remains reachable.
- **Dirty form navigation:** if the player has unsent input, leaving the task screen presents a leave-confirmation; after a confirmed submission, no leave-confirmation is shown for the submitted data.
- **Context preservation:** search, filters, sort, pagination and saved-view state are preserved on back/return within the same session where the owning screen defines them (B-13 §8.3). The mechanism is a Stage 5 implementation matter; the duty is the requirement.

### 6.3 Overlays and page equivalence

`OVL-01` confirmation, `OVL-02` destructive exact-phrase, `OVL-03` reason, `OVL-04` definition/cause chain, `OVL-05` object peek, `OVL-06` boundary notice, `OVL-07` suppression notice and `OVL-08` claim badge obey 13A §5.3 and D-215. An overlay never becomes the only place a fact, state or action exists. Escape dismisses a non-committing overlay and cancels a confirmation; it never confirms. Focus is trapped while modal and restored on dismissal (§11.4).

---

## 7. Global interaction conventions

| Convention | Rule |
|---|---|
| **One primary action per region** | One filled primary control per action region; secondary controls are visually subordinate; destructive controls are separated (`REQ-1055`). |
| **Committing controls** | Every committing control passes through the owning confirmation (`UI-CMP-088`, `OVL-01`) and shows the exact effect, cost, resource impact, cooldown, turn/phase and consequence (`REQ-1049`, D-214, `CFM-` rules). |
| **Disabled controls** | Never hidden merely to avoid explanation; carry a reason and rule link (`UI-CMP-089`, `OVL-03`, `13A-PR-10`). A permission-denied destination may be hidden where naming it would disclose a protected object; an object action is disabled with its permitted reason class. |
| **Pending** | A submitted but unresolved action shows `pending` with the owning system, what is reserved and where it resolves. It is cancellable only where the owning rule permits (`UI-CMP-070`, `REQ-1047`). |
| **Success** | Only after authoritative confirmation; names what changed and the resulting state; never claims more than the record says (§10.5). |
| **Failure** | Names what happened, whether anything changed, whether the action completed, whether retry is safe and what to do next (§10.7). |
| **Time** | Turn number and UTC boundary; wall-clock is a cosmetic aid only (`REQ-1007`). |
| **Numbers** | Six number types separated; units and as-of turn always present; total/reserved/available together for every balance (`ECN-177`, MKT-053, `REQ-1065`). |
| **Suppression** | Render the named suppressed state; never zero, blank or inferable (`D-027`, `REQ-1066`). |
| **Objects** | Every object identifier links to its canonical route; peeks reveal only already-visible fields (`REQ-995`, `REQ-996`). |
| **Search** | Jump-to-object and jump-to-screen only; no full-text corpus promise (`REQ-994`, `13A-OQ-005/009`). |
| **Focus return** | After any overlay, inline expansion or submission result, focus returns to the invoking control or to the announced result heading (§11.4). |

---

## 8. Player journey architecture

### 8.1 Journey classes

| Class | Purpose | Examples |
|---|---|---|
| **Entry journeys** | Establish or restore access and identity | `JRN-A`, `JRN-B`, `JRN-L` |
| **Routine management** | Check the situation and manage the nation | `JRN-C`, `JRN-D`, `JRN-F`, `JRN-G` |
| **Transactional journeys** | Negotiate and commit an exchange or agreement | `JRN-E`, `JRN-H` |
| **Consequential journeys** | Commit military, destructive or protection-relevant actions | `JRN-I`, `JRN-L` |
| **Progression journeys** | Understand events, objectives, standings and world state | `JRN-J` |
| **Support journeys** | Handle alerts, reports, appeals, restrictions and support | `JRN-K` |
| **Administrative journeys** | Role-scoped work inside the separate Admin root | `JRN-M` |

### 8.2 Journey and flow identifiers

- Journeys are `JRN-A`…`JRN-M`, one per mandatory journey category in the Prompt 13C instruction. They are unique and non-renumberable.
- Flows are `FLOW-001`…`FLOW-033`. A flow is the smallest reproducible interaction unit with one authoritative outcome; a journey is a chain of flows and screen visits.
- Tutorials are `TUT-01`…`TUT-12`; they reference journeys and flows but never replace them.
- A flow appears on the owning screen(s) in Matrix B/C; a journey appears in Matrix A. Every requirement row in §18.2 names its journey and, where it governs a sequence, its flow.

### 8.3 Journey design rules

1. A journey begins and ends at a named surface; the completion state names the next meaningful action.
2. The player is never trapped: every uncommitted step has a cancel/back path; every committed step has a recovery/report path.
3. The journey never requires attendance at a specific wall-clock moment; boundary-dependent results are delivered through the digest and notifications.
4. A journey that changes a balance, commitment or relationship must show the exact consequence before confirmation and the exact resulting state after resolution.
5. A journey that cannot complete must leave the pre-existing state intact and explain the block; partial irreversible application is prohibited.
6. Cross-system effects (for example a trade that changes warehouse space or a war that changes city infrastructure) are reflected on the owning screens after the authoritative settlement, not invented by the interface.

### 8.4 Journey template

Every `JRN-` uses the ten-part template fixed by the instruction: identity; starting conditions; entry point; main sequence; alternative paths; failure paths; completion; recovery; accessibility; requirements and evidence. The template is instantiated in the journey companion.

---

## 9. Cross-system interaction principles

| ID | Principle | Consequence |
|---|---|---|
| `XSP-01` | **One Inbox for every pending act.** | Trade offers, diplomatic proposals, alliance applications/invitations, campaign actions and settlements appear as pending rows and deep-link to their owning screen (`SCR-014`, `REQ-883`, `TR-004`). |
| `XSP-02` | **The boundary is the settlement point.** | Actions resolve at their defined phase; until then the interface shows pending/reserved. The digest is the durable record (`TR-088/089`, `REQ-882`). |
| `XSP-03` | **Reservation is visible but not spendable.** | A reserved crown, resource, capacity slot or OP is shown as reserved and excluded from available; no screen offers it again (`ECN-110`, `REQ-1065`). |
| `XSP-04` | **A rule block is explained in every system.** | Protection, NAP, same-alliance, political state, cooldown, eligibility, permission, rate limit and capacity blocks use the owning vocabulary and a consistent reason presentation (`UI-CMP-053`, `UI-CMP-089`). |
| `XSP-05` | **A settlement explains its cause chain.** | Every consequential change carries a "why" path to its contributing terms and governing rule (`13A-PR-04`, `13A-DR-010`, `REQ-980`). |
| `XSP-06` | **Private data never becomes cross-system glue.** | A trade, alliance, war or support journey never reveals another player's private field to make its UI convenient (`TR-021`, `REQ-1076`). |
| `XSP-07` | **Alliance is coordination, never command.** | No alliance flow links to, delegates or displays another nation's War Operations Board or private war state (`REQ-1073`, `AX-18`, `WAR-148/161`). |
| `XSP-08` | **Support and conduct are separate routes.** | A support request does not become a moderation case; a report is an accusation with its own intake (`MOD-002`, `SCR-081`, `SCR-087`, `REQ-956`). |

---

## 10. Global state and feedback conventions

### 10.1 Interaction-state model

Prompt 13C uses eighteen interaction states `ST-01`…`ST-18` (state companion §2). They describe **screen/action scenarios**; they do not rename the thirteen 13A application states or the eleven 13B component states. Mapping:

| 13A application state | 13C interaction state(s) |
|---|---|
| loading | `ST-02` Loading (initial/navigation) or `ST-03` Refreshing |
| empty (new nation) / empty (no data) | `ST-05` Empty |
| error / failed request | `ST-14` Failed |
| permission-denied | `ST-09` Permission denied |
| blocked-by-rule | `ST-11` Blocked by rule |
| disconnected / stale | `ST-15` Offline or `ST-06` Partial data |
| action success | `ST-07` Success |
| pending action | `ST-06` Partial data + pending treatment |
| confirmation-required | `ST-04` Loaded + `CFM-` confirmation (not a state of the data) |
| time-sensitive | `ST-12` Expired / `ST-04` with turn context |
| suppressed-data | `ST-06` Partial data |
| `PROVISIONAL_BLOCK` | `ST-10` Unavailable |

### 10.2 State doctrine

1. **Transient vs persistent:** `ST-01`…`ST-04`, `ST-07` and `ST-18` are normally transient interaction states; `ST-05`, `ST-06`, `ST-09`…`ST-17` can persist and must remain legible on reload.
2. **A persistent state survives navigation.** Reloading a denied, expired, suppressed, offline or failed screen reproduces the state from the authoritative record, never a stale one-time toast.
3. **No invented state.** If no owning rule defines a state, the interface renders the applicable generic state (`ST-10` Unavailable or `ST-14` Failed) with the rule gap named, never a simulated success.
4. **State is announced.** Loading, success, failure, validation, permission, blocked, expired, conflict, offline, reconnecting, recovering and cancellation each have a text label plus an assistive announcement (§11.3).
5. **State is never colour-only.** Every state pairs tone with glyph and text (`REQ-1014`, `13A-DS-10`).
6. **Not every component supports every state.** The applicable set is recorded per component in the state companion §7; an unsupported state is an exemption with reason, not a silent gap (`REQ-1004`, B-13 §6.3).

### 10.3 Loading doctrine

- The shell and previously confirmed data remain visible; no full-page spinner (`REQ-970`).
- Skeletons are used within the bounds of the component being loaded; they must not imply values.
- Tables, charts and forms announce what is loading; action buttons show an in-flight state.
- Navigation remains available during a section load; a committing request may disable only the controls that would duplicate or contradict it.
- Stale data shown during refresh is labelled with its as-of turn (see §10.8).

### 10.4 Empty-state doctrine

Distinguish: no records exist yet; no matching search/filter result; no pending actions; no notifications; no historical records; no eligible actions; unavailable feature; permission-restricted content. Every empty state names **why** it is empty and, where a legitimate next step exists, links it. A Conditional or Provisional feature never renders as an empty usable feature (`D-216`).

### 10.5 Success doctrine

1. **Genuine confirmed success** means the owning system resolved the action and the interface can read the resulting state. A button click, an HTTP 2xx response that only means "accepted", or an animation is not success.
2. **Four distinct messages:** request accepted; request processing; action completed; action rejected. A fifth, **result pending**, covers boundary-settled actions.
3. **Success content:** what changed, the object and turn, the cost charged, any reservation released, the new state and the next meaningful action.
4. **No premature celebration:** a boundary action never shows a completion toast before P4/P5/P6 settlement (`TR-038`).
5. **Receipt, not confetti:** success is a receipt view or inline state with a durable record, not a transient-only toast.

### 10.6 Failure doctrine

Every failure state answers: **what happened; whether anything changed; whether the action completed; whether retrying is safe; what the player can do next; whether support is necessary.** The exact catalogue is `ERR-01`…`ERR-20`. No stack trace, secret, token, internal identifier beyond a support-safe reference, detection method or another player's data may appear (`REQ-1077`, `PRV-014`).

### 10.7 Error anatomy

| Element | Content |
|---|---|
| Title | Player-language statement of the condition |
| Body | Cause in the owning vocabulary; what was and was not changed |
| Safe-retry | Whether retry is safe; the control to retry; what has been preserved |
| Next step | Correction, alternate route, support or wait-until turn |
| Reference | Optional support-safe reference code; never a raw internal trace |

### 10.8 Stale-data doctrine

A figure or record is stale when the last confirmed authoritative read is older than the stated as-of turn/slot, or when a refresh failed. Stale data may remain visible for read continuity but must be labelled with its as-of turn and the owning screen must not present it as current (`TR-039`, `TR-049`). Writes based on stale state are revalidated by the server; the interface must never assume the stale value still holds.

### 10.9 Cancellation doctrine

Cancellation is a first-class outcome. `ST-18` applies when the player or the rule cancels before commitment. Cancelling never commits, never charges, never reserves, and never leaves a half-state. Cancellation after acceptance is possible only where the owning rule explicitly permits it (trade cancellation before settlement, proposal withdrawal, operation cancellation before freeze, closure cancellation during cooling). Where the rule forbids cancellation, the control is absent and the reason is stated; no "cancel" is offered that cannot be honoured.

---

## 11. Accessibility interaction principles

### 11.1 Standard and evidence boundary

The target is **WCAG 2.2 Level AA as design intent**. No conformance is claimed; no built UI, browser test, screen-reader pass or contrast measurement exists (13A §7; B-13 §10.3). Specification-level acceptance criteria are in the state companion §12.5 and in §18.2 (`REQ-1162`…`REQ-1171`).

### 11.2 Keyboard interaction

- Every essential journey is completable with a keyboard alone (`REQ-1081`).
- Tab order follows visual/reading order; the shell offers a skip-to-content link before the navigation; no positive `tabindex` ordering.
- Enter and Space activate buttons, links and custom controls per platform convention; Space toggles checkboxes and toggles.
- Escape closes a non-committing overlay and cancels a confirmation; Escape never confirms and never dismisses a destructive confirmation without an explicit cancel action.
- Arrow keys move within tablists, radio groups, menus, date/turn selectors and grid-like tables where the pattern defines it; arrows never hijack text inputs or scroll the page unexpectedly.
- Every table is reachable and navigable by keyboard; row actions are reachable without hover; shortcuts are optional and discoverable.
- No keyboard trap exists outside a modal; a modal returns focus on close.

### 11.3 Screen-reader interaction

- Every control has an accessible name; every input has a programmatically associated label (`REQ-1086`).
- Roles and states are exposed (`aria-pressed`, `aria-expanded`, `aria-disabled`, `aria-invalid`, `aria-busy` where applicable) without inventing roles that misrepresent the control.
- Errors are linked by text to the affected field and summarised at the form top; the summary is focusable when validation fails.
- Tables expose header/row/column scope; card fallbacks preserve the same reading order and field labels.
- Numbers are announced with units, basis points and as-of turn; a bare number is not the accessible name (`REQ-1084`).
- Loading, submission, success, failure, suppression, permission and blocking states are announced once at an appropriate politeness; continuous countdown ticks are never announced (`13A-DS-13`).
- Dynamic updates after a boundary or background refresh announce the region and the changed summary, not every cell.
- Important information is never available only through colour, animation or visual position (`13A-DS-10`).

### 11.4 Focus management

| Situation | Focus rule |
|---|---|
| Screen transition | Focus moves to the screen heading (or main landmark) after the route renders; page title updates. |
| Dialog open | Focus enters the dialog at its title or first safe control; focus is trapped. |
| Dialog close | Focus returns to the invoking control; if it no longer exists, focus goes to the nearest logical heading. |
| Validation failure | Focus moves to the error summary (or first invalid field when no summary exists); the field is announced. |
| Submission result | Focus moves to the result heading/toast-equivalent region; the page equivalent remains reachable. |
| Search results | Focus remains in the search field; the result count is announced; results are reachable by Tab. |
| Notification arrival | No focus steal; the alert indicator announces politely. |
| Table update | Focus stays on the same row/control where it still exists; otherwise the table heading is announced. |
| Recoverable failure | Focus moves to the retry/correction control; the failure text is announced. |

### 11.5 Responsive accessibility interaction

- One game, one rule set, one URL per screen (`REQ-1051`, `13A-RD-05`).
- Desktop, tablet and mobile preserve every non-negotiable field, action, reason and confirmation (B-13 §8.2).
- Mobile tables become card lists that preserve the same labels and values; the twelve-city set remains one screen (`REQ-910`).
- The Network View is list-first on mobile; every graph fact is reachable in the list (B-13 §11.2).
- Touch targets meet the WCAG 2.2 AA 24×24 CSS-pixel minimum and the project's DS-14 token; destructive controls are separated (`REQ-1055`, `13A-DS-14`).
- 200% text resize and 200% zoom do not lose content or introduce horizontal page scroll; reflow at 320 CSS px is supported (`13A-RD-05`).
- Both portrait and landscape orientations are usable; no interaction requires device tilt or gesture-only input.
- Reduced motion is respected; no state depends on motion; the countdown remains a polite live region.
- Contrast targets are AA for text and essential graphics (design intent); the owner palette must pass before adoption (`13A-DS-09`, `13A-OQ-001`).
- A hardware/on-screen keyboard can reach, type into and submit every form; no custom text entry is specified.

### 11.6 Alternative presentation

Every chart has a text/table alternative reachable without interacting with the chart (`REQ-1059`). Every cause-chain drawer has its page/detail equivalent. Every overlay state has a page-reachable equivalent (D-215). Suppression and provisional states are announced as states (`REQ-1056`).

### 11.7 Accessibility acceptance criteria

The measurable specification-level criteria are `AX-AC-01`…`AX-AC-12` in the state companion §12.5. They are requirements for a future built UI, not claims of present compliance.

---

## 12. Onboarding and tutorial architecture

### 12.1 What onboarding must teach

The accounts of the turn cadence, the national dashboard, financial reading, political conditions, national management, diplomacy and warfare, objectives/progression, notifications and help (`TUT-01`…`TUT-12`). Teaching is layered, optional and never a gate on play except the mandatory account/nation setup that the owning rules already require.

### 12.2 Five layers

| Layer | Mandatory? | Purpose | Surfaces |
|---|---|---|---|
| **Account setup** | Mandatory where the rule requires (e-mail verification, nation creation) | Establish identity and nation | `SCR-002`…`SCR-007` |
| **Essential first-time guidance** | Strongly offered, skippable | Orient the first session; explain the real shell and the first objectives | `SCR-008`, `SCR-009`, `TUT-01`…`TUT-03` |
| **Optional tutorials** | Optional | Teach a system before or when the player uses it | `TUT-04`…`TUT-12` |
| **Contextual help** | On demand | Explain the current screen, term or rule without leaving it | `OVL-04`, `SCR-078`, governing-rule anchors |
| **Advanced system explanations** | On demand | Deeper cause chains, methodology and edge cases | `SCR-078`, owning detail screens |

### 12.3 Tutorial architecture

- Tutorials run **inside the real shell** with the player's true zero-state or current values (D-040; `REQ-877`). No separate tutorial product, fake dashboard or stub economy.
- Every step is skippable and resumable; skipping records a preference, not a failure (ONB-009).
- Help is reopenable and searchable; help content is versioned with a "this changed" note where rules change (ONB-011/012).
- Each tutorial action is labelled **now** or **at the next turn** (ONB-013); no tutorial implies instant settlement.
- No countdown, streak, attendance reward or pressure device is used (ONB-014, D-021, AP-001).
- Tutorial progress belongs to the account and survives a reroll (D-040).
- A tutorial never performs a gameplay action on the player's behalf, never spends resources, never submits a trade/diplomacy/military action and never overrides a restriction (§12.5).

### 12.4 Entry and resumption

Tutorials can start from `SCR-008` (first-session), from the owning screen's help affordance, from `SCR-078` (guide) or from a contextual prompt where the player first meets a system. A tutorial is interrupted by navigation, session loss or a blocking state; on return the player may resume at the last incomplete step, restart, or dismiss. Completion is recorded once per account and never re-granted; replay is available read-only and marked as replay.

### 12.5 Tutorial safety (binding)

A tutorial must never execute or auto-complete a gameplay action, spend a resource, commit a diplomatic decision, submit a trade, execute a military action, override a restriction or force an irreversible action. Safe demonstrations use read-only previews, annotated real screens, and optional player-performed actions that pass the same confirmation as normal play. No tutorial reward, currency, protection extension or progression advantage exists.

### 12.6 Tutorial template

Every `TUT-` records the eighteen fields mandated by the instruction (identity; name; objective; intended player; prerequisites; entry condition; starting screen; ordered steps; explanation; expected interaction; expected result; validation; failure/recovery; skip; completion condition; re-entry; accessibility; related requirements). Bodies are in the journey companion §5.

---

## 13. Notification and feedback architecture

### 13.1 Notification sources and categories

Notifications are presentation over **existing** events only (`REQ-731`, `UR-029`, `REQ-976`). The categories map to existing sources:

| Category | Existing source family | Primary surfaces |
|---|---|---|
| Account & security | B-03/D-041 notices, session and recovery events | `SCR-011`, `SCR-080`, `SCR-006` |
| Nation management | B-02 digest and boundary events (`TR-088/089`) | `SCR-013`, `SCR-016`, `SCR-019` |
| Economy & finance | B-04 reports, austerity and settlement events | `SCR-029`…`SCR-031` |
| Production | B-04/B-05 chain, maintenance and capacity events | `SCR-032`, `SCR-044` |
| Politics & elections | B-06 state, election and crisis events (`DMP-268`) | `SCR-021`…`SCR-028` |
| Diplomacy | B-08 notification catalogue N1–N9 (`DIP-114/116`) | `SCR-047`…`SCR-052`, `SCR-019` |
| Alliances | B-09 application, tax and treaty events | `SCR-053`…`SCR-058` |
| Warfare | B-10 catalogue, battle reports, settlement events | `SCR-059`…`SCR-067` |
| World events & objectives | B-11 event and objective lifecycle (`WEP-099`, `WEP-232`) | `SCR-069`…`SCR-071` |
| Rankings & progression | B-11 standings, achievements and rewards | `SCR-072`…`SCR-075` |
| Player protection & support | B-12 notice, appeal and support events (`MOD-013/017`) | `SCR-081`…`SCR-087` |

No notification category may generate a trigger the owning system does not define.

### 13.2 Two vocabulary layers

- **Routing tier (13B):** `blocking`, `digest`, `ambient` — how an existing event is presented (`SCR-019`). Default assignment remains provisional (`13A-OQ-006`, D-219).
- **Feedback class (13C):** `informational`, `success`, `warning`, `critical`, `action-required` — the local message's meaning. It is **not** a game-severity label and never upgrades a rule's seriousness.

### 13.3 Notification behaviour

- Arrival on another screen updates the shell indicator count and shows a non-focus-stealing notice; only an `action-required` or security-critical item may surface in the alert bar.
- Arrival while offline appears on the next authenticated load, with its event turn and read state; no push channel is specified.
- Read/unread state is per account and per event; opening the linked object does not silently mark an unrelated item read.
- Opening a notification deep-links to the owning object/screen. If the destination is retired, expired, restricted, role-denied or absent, the notification history retains the event and the destination renders its owning unavailable/retired/denied state; the link never fabricates an object.
- Duplicates are grouped by source event and object; one event never produces two ungrouped notifications. Grouping shows the count and the latest state.
- Muting is available only where the owning rule permits; non-opt-out notices (security, appeal route, statutory disclosure) are marked and cannot be muted (MOD-013, DIP-114/116).
- Dismissal removes the presentation, never the underlying event or its record in `SCR-019`.
- Announcements are polite, concise and deduplicated; a count change alone is not repeatedly announced.

### 13.4 Player feedback classes

Every action result uses exactly one feedback class and the matching presentation:

| Class | Used for | Never used for |
|---|---|---|
| `informational` | settled facts, digest entries, help | implying an action succeeded |
| `success` | authoritative completion with a receipt | a merely accepted request |
| `warning` | degradation, approaching limit, `UNMAINTAINED`, protection ending | an error that blocked the action |
| `critical` | security notice, restriction, failed settlement requiring attention | ordinary validation |
| `action-required` | pending decision due before a boundary, appeal route | decorative urgency |

---

## 14. Offline and reconnection behaviour

### 14.1 Posture

There is **no offline gameplay**: no offline action execution, no queued writes that commit later, no offline settlement, no automatic retry of a committing action. Reads are **read-only**: previously confirmed data may remain visible labelled with its as-of turn, but new reads require connectivity. The two-hour UTC cadence is unchanged by connectivity (D-008, TR-024).

### 14.2 Connection-loss scenarios

| Scenario | Player sees | Actions available | Input preserved | Authoritative result |
|---|---|---|---|---|
| Loss during navigation | Offline banner; destination shows a retry state | Navigation within already-loaded screens; retry | Not applicable | Restored by a successful read |
| Loss during form entry | Inline offline notice; unsent fields remain | Edit locally; cannot submit | Yes, for the open form until the session ends or the player navigates away | Submission only after reconnection and explicit confirmation |
| Loss during submission | Single-flight control in `pending`, then `unknown — retrying` per TR-075 | No duplicate submission; cancel of the pending view only | Submitted intent retained on screen where safe | Reconciled by re-reading the object; never assumed |
| Session expiration | Re-authentication gate; return-to-screen context | Sign in; choose another account | Unsent input preserved only where safe; secrets never retained | Re-read after authentication |
| Browser refresh during submission | On reload, the object is re-read; if still pending, the pending state is shown | Wait; open the Inbox | Form drafts are not promised across reload except where the owning screen defines saved-view state | Pending or resolved per authoritative record |
| Browser closure | Nothing is promised | — | No | On next login, digest/inbox/object state is authoritative |
| Extended absence | Re-entry summary groups missed turns and open decisions (`REQ-022`, TR-084) | Normal play | Not applicable | Current state from authoritative reads |
| Reconnection | Reconnecting state, then refreshed data with as-of turn | Normal play | Unsent input offered for review before submit | Conflicting values are replaced by authoritative values and labelled |

### 14.3 Uncertain outcome

A timed-out or interrupted committing request is **never assumed failed or successful**. The interface shows `unknown — retrying` or an equivalent named state, prevents duplicate submission, and resolves by re-reading the object and its activity before offering a retry. Automatic client retries are permitted only where the owning system defines a safe idempotency key and the retry reuses it; otherwise the player must be shown the state and choose. Backend idempotency is not invented here; `DUP-04`…`DUP-08` record the implementation dependencies.

### 14.4 Boundary and offline interaction

The turn boundary proceeds server-side regardless of the player's connectivity. A player who is offline at the boundary sees the settled result on return through the digest and object state; no local timer may simulate settlement. A `FAILED` or `INTERRUPTED` turn is presented as a delay with the named state, not as a lost turn (TR-080).

---

## 15. Cross-screen consistency

### 15.1 Global consistency rules

| Area | Rule |
|---|---|
| Navigation | One canonical parent, one route key, breadcrumb at depth ≥ 2, active section marked; no duplicate destinations (`REQ-971`…`REQ-973`). |
| Back navigation | Browser back never loses the canonical context; a return never lands on an absent/denied surface. |
| Screen transitions | Shell persists; heading and title update; focus moves to the heading (§6.2, §11.4). |
| Context preservation | Filters, sort, pagination, saved views and the selected turn persist on return where the screen defines them. |
| Search | Jump-to-object and jump-to-screen only; same result semantics everywhere (`REQ-994`). |
| Filters | Same filter row grammar, active-filter disclosure and clear action on every table (`REQ-991`). |
| Pagination | Exact `0–N of M` counts; sort/filter preserved across pages; no false completeness (`REQ-992`). |
| Saved views | Per-user; dirty/invalid state shown; never widens visibility (`REQ-993`). |
| Object references | Same link/peek/retired/denied behaviour everywhere (`REQ-995`). |
| Context panels | Same contextual-fact rules and visibility class; defaults remain provisional (`13A-OQ-008`). |
| Confirmation overlays | Same ten-field consequence discipline and cancel/confirm order (`REQ-1049`, D-214). |
| Error messages | Same anatomy and failure class; owning vocabulary; safe retry. |
| Loading feedback | Same skeleton, announcement and shell persistence. |
| Notifications | Same source event, tier, grouping and deep-link semantics (§13). |
| Permission restrictions | Same reason class and deny presentation; no contradictory availability. |
| Empty states | Same eight-way distinction and next-step rule (§10.4). |
| Responsive interaction | Same data, actions and confirmations on desktop, tablet and mobile (`REQ-1051`). |

### 15.2 Shared-object behaviour

| Object | Canonical view | Identity rule | Status rule | Permission/action rule |
|---|---|---|---|---|
| Nation | `SCR-010` (public), `SCR-015`/`SCR-089` own | `nation_id` stable; retired page remains labelled `retired — rerolled` | Public/own fields per TR-021; protection is a state with an end turn | No private action from a public page; own actions only on owner screens |
| Alliance | `SCR-053` | Name/acronym public; leadership public | Membership/role shown only within disclosure | Management links only with permission; no military authority |
| War | `SCR-063` | War identifier stable | WAR-125 lifecycle state, exact label | Field-filtered by viewer; owner controls only on `SCR-061` |
| Treaty/agreement | `SCR-050` | Exact type `DP-T01`…`DP-T03`/`DP-A01` or `AT-*` | Lifecycle state; no stale active badge | Pending terms parties-only; publication per DIP-108…113 |
| Trade offer | `SCR-037` | Chain/revision identity | `ACTIVE`/`COUNTERED`/`ACCEPTED`/`DECLINED`/`CANCELLED`/`EXPIRED`/`RESOLVED`/`FAILED` | Parties + restricted audit only |
| City | `SCR-042` | `city_id` immutable; name cosmetic | `UNMAINTAINED`, capacity, housing | Owner only; one construction-class action per city per turn |
| Event | `SCR-070` | Registered event ID | WEP-099 lifecycle state | Eligibility per event; no unregistered effect |
| Objective | `SCR-071` | Registered category + objective ID | WEP-232 lifecycle state | Optional; penalty-free dismissal |
| Notification | `SCR-019` | Source event + object | Read/unread + routing tier | Mute only where permitted |

### 15.3 Financial consistency

1. Every crown or resource balance is rendered as total, reserved and available together (`UI-CMP-033`, `REQ-1065`). A total-only presentation is a review defect.
2. Reserved amounts remain in the treasury/warehouse but are unavailable (`ECN-110`, `ECN-125`); no screen may offer a reserved amount for a new commitment.
3. `available = total − reserved` is derived for display only; the authoritative balance is server-side.
4. National wealth is a report statistic, never a spendable balance or credit (`D-051`, `D-062`).
5. Forecasts are visually lighter, labelled and never shown as current balances (`ECN-178`, `REQ-1064`).
6. Completed prices, book values and reference prices are separate labels with units (`MKT-140`).
7. The same object's balance must agree on every screen at the same as-of turn; a disagreement renders the stale label and the authoritative refresh, never two "current" numbers.
8. Alliance receipts are immutable and never imply ownership or a spendable alliance treasury (`ALL-193`, `REQ-1028`).

### 15.4 Permission consistency

1. Availability is server-authoritative; a rendered control without permission fails closed with a named restriction (`REQ-1088`).
2. The same restriction class uses the same explanation on every screen (`UI-CMP-053`, `NET-023`).
3. An action denied on one screen is never presented as available on another for the same viewer and object.
4. A role-restricted destination is hidden where naming it would disclose a protected object; a visible object action is disabled with its permitted reason.
5. Administrative access is separate, role-scoped, purpose-bound and audited; no player screen exposes admin chrome or data (`REQ-1037`, D-042).

### 15.5 Navigation consistency

Canonical parents, route keys and aliases are verified by B-13 §7.2/§7.3 and preserved. Four dual-parent screens use a canonical parent plus cross-section alias: `SCR-010`, `SCR-017`, `SCR-062`, `SCR-088` (D-209). No journey creates a duplicate route, a second object copy or an alias-only screen.

### 15.6 Matrix I — Cross-screen consistency coverage

| Consistency ID | Behaviour | Applicable screens | Shared components | Expected behaviour | Related requirements |
|---|---|---|---|---|---|
| `CON-01` | Shell persistence | All authenticated | `UI-CMP-001`…`UI-CMP-011` | Shell remains through loading/error; identity/nav/alerts/breadcrumb never disappear | `REQ-970`, `REQ-1194` |
| `CON-02` | Canonical parent/route | All 100 | `UI-CMP-002`, `UI-CMP-005` | One parent, one route, alias not a second copy | `REQ-1013`, `REQ-1198` |
| `CON-03` | Breadcrumb return | Depth ≥ 2 | `UI-CMP-005` | Every crumb works; return never to absent/denied | `REQ-973`, `REQ-1194` |
| `CON-04` | Object identity | `SCR-010/042/050/053/063/070` | `UI-CMP-027`, `OVL-05` | Same object, same identity and visibility everywhere | `REQ-995`, `REQ-1195` |
| `CON-05` | Balance triple | Economy/market/alliance | `UI-CMP-015`, `UI-CMP-033` | Total/reserved/available always together | `REQ-1065`, `REQ-1196` |
| `CON-06` | Number type | All data screens | `UI-CMP-012`, `UI-CMP-013` | Six types separate; forecast lighter | `REQ-1063`, `REQ-1196` |
| `CON-07` | As-of turn | All data screens | `UI-CMP-012`, `UI-CMP-020` | Every figure has an as-of turn/slot | `REQ-1062`, `REQ-1196` |
| `CON-08` | Suppression | Aggregate surfaces | `UI-CMP-072`, `OVL-07` | Named suppressed/insufficient state; no zero | `REQ-1066`, `REQ-1196` |
| `CON-09` | Disabled reason | All controls | `UI-CMP-089`, `OVL-03` | Reason before click; rule link | `REQ-1029`, `REQ-1200` |
| `CON-10` | Confirmation content | All committing screens | `UI-CMP-088`, `OVL-01` | Effect, cost, cooldown, phase, consequence | `REQ-1049`, `REQ-1200` |
| `CON-11` | Destructive barrier | `SCR-012/090`, `SCR-094` | `UI-CMP-087`, `UI-CMP-090`, `OVL-02` | Separated, consequence-first, exact phrase where required | `REQ-959`, `REQ-1200` |
| `CON-12` | Failure anatomy | All screens | `UI-CMP-084`, `UI-CMP-019` | What happened/changed/completed/retry/next | `REQ-1154`, `REQ-1201` |
| `CON-13` | Empty-state taxonomy | All lists | `UI-CMP-019`, `UI-CMP-022` | Eight distinctions; next step or honest absence | `REQ-1136`, `REQ-1201` |
| `CON-14` | Pending visibility | `SCR-013/014/019` + owning screens | `UI-CMP-069`, `UI-CMP-070` | Same pending act appears consistently | `REQ-1047`, `REQ-1195` |
| `CON-15` | Permission presentation | All permission-sensitive screens | `UI-CMP-053`, `UI-CMP-089` | Same restriction class, same explanation | `REQ-1029`, `REQ-1197` |
| `CON-16` | Admin separation | `SCR-091`…`SCR-100` | `UI-CMP-010` | No player chrome or admin data crossover | `REQ-1037`, `REQ-1197` |
| `CON-17` | Notification source | `SCR-013/014/019` | `UI-CMP-008`, `UI-CMP-069` | One event → one grouped notification | `REQ-976`, `REQ-1201` |
| `CON-18` | Deep-link failure | All object links | `UI-CMP-027`, `OVL-05` | Retired/expired/denied state, never fabricated | `REQ-995`, `REQ-1198` |
| `CON-19` | Filter/pagination | List screens | `UI-CMP-023`, `UI-CMP-024` | Exact counts; state preserved | `REQ-991`, `REQ-1199` |
| `CON-20` | Search scope | Shell and search screens | `UI-CMP-026`, `UI-CMP-082` | Jump-only; denied/no-result states | `REQ-994`, `REQ-1199` |
| `CON-21` | Time expression | All screens | `UI-CMP-007`, `UI-CMP-041` | Turns + UTC; no wall-clock truth | `REQ-1007`, `REQ-1195` |
| `CON-22` | Responsive parity | All screens | All applicable | Same facts, actions, confirmations on every device | `REQ-1051`, `REQ-1202` |
| `CON-23` | Focus behaviour | All interactive screens | All interactive | Predictable entry/return; no lost focus | `REQ-1081`, `REQ-1194` |
| `CON-24` | Conditional absence | `SCR-020/038/039/068/077` | None | Absent until gate; no teaser, stub or implied availability | `REQ-907`, `REQ-937`, `REQ-946`, `REQ-1198` |

---

## 16. Security, fair-play and permission boundaries

1. **Authentication boundary.** Public screens never render authenticated data; session loss routes to the login gate and back to the same permitted screen (`SCR-003`). Unverified accounts cannot play (D-029).
2. **Authorization.** Every action is checked server-side against the account, nation, role, ownership and state. Presentation never grants it (`REQ-1088`).
3. **Ownership.** Trade offers, proposals, settlements, operation controls, construction and city actions are owner-scoped; alliance and administrative views never merge another owner's private state (`REQ-1039`, `REQ-1073`).
4. **Sensitive data.** `SEC` class never appears on any player or moderation surface; credentials, tokens, keys and detection internals never appear (`PRV-014`, `REQ-1077`).
5. **Privacy.** The nine privacy classes govern every disclosure; a privacy setting never widens another player's visibility (`PRV-002/009`, `REQ-1076`).
6. **Player protection.** Restriction text names kind, scope, end/review turn and appeal route without accusation, another player's data or a detection threshold (`NET-023/050`, `REQ-953`). The appeal route is never blocked (`MOD-013`, `REQ-1078`).
7. **Audit.** Administrative reads and decisions are role-scoped, purpose-bound and themselves audited (`REQ-1080`).
8. **Fair play.** No interaction enables duplicate-action exploitation, resource duplication, reroll farming, unauthorized visibility, administrative overreach or restriction-circumvention. The Inbox, single-flight submission, server revalidation, task caps, cooldowns and protection checks are the interaction-level expressions of rules that already exist; 13C adds no enforcement mechanism.
9. **Untrusted input.** Player-authored names, constitution text, announcement text, report free text and offer terms are rendered as text, never as markup or executable content; validation never echoes raw input into an executable context.
10. **Safe errors.** No stack trace, secret, internal path, detection method, threshold or another player's data. Support references are opaque and safe to share.
11. **Outstanding obligations preserved.** The production security defects recorded by 12A/12B remain outstanding; this pass implements nothing and claims no fix.
12. **Mapless interaction preserved.** No journey, flow, tutorial, notification or state uses geographic coordinates, distance, territory, borders, provinces, fronts or movement; **no geographic** map, territorial view or map-dependent interaction exists. The Network View (`SCR-018`) is the only world-situational surface and is symbolic, relationship-based and list-first on mobile (TR-012/013/014, REQ-041). No map provider, tile service or geocoding dependency is specified anywhere.

---

## 17. Provisional decisions and unresolved dependencies

### 17.1 New Category B decisions

D-220…D-231 are recorded in [DECISIONS.md](../DECISIONS.md) and mirrored as DD-268…DD-279 in [stage-2/04](04_approved_and_provisional_decisions.md). D-232 is the Category C provisional bundle mirrored as DD-280.

| ID | Topic | Status |
|---|---|---|
| D-220 | Prompt 13C three-document interaction architecture and register ownership | Confirmed (Category B) |
| D-221 | Eighteen-state interaction taxonomy layered over 13A/13B states | Confirmed (Category B) |
| D-222 | `JRN-`, `FLOW-` and `TUT-` identifier families and templates | Confirmed (Category B) |
| D-223 | Journey chain and flow decomposition policy | Confirmed (Category B) |
| D-224 | Validation timing and message anatomy | Confirmed (Category B) |
| D-225 | Single-flight confirmation and uncertain-outcome discipline | Confirmed (Category B) |
| D-226 | Focus management and screen-transition behaviour | Confirmed (Category B) |
| D-227 | Notification interaction, grouping and deep-link fallback policy | Confirmed (Category B) / tier defaults Provisional |
| D-228 | Offline read-only posture and reconnection reconciliation | Confirmed (Category B) |
| D-229 | Tutorial safety, skip/resume/replay and no-auto-action rule | Confirmed (Category B) |
| D-230 | Cross-screen object, balance and permission consistency rules | Confirmed (Category B) |
| D-231 | `REQ-1090`…`REQ-1203` allocation, traceability and status policy | Confirmed (Category B) |
| D-232 | Provisional interaction values and owner-reserved preservation | Provisional (Category C) |

### 17.2 Provisional matters (D-232)

| Question | Safe working default | Missing evidence | Named validation test | Condition for replacement |
|---|---|---|---|---|
| Notification routing-tier defaults (`13A-OQ-006`) | Security/appeal items `blocking`; boundary results `digest`; cosmetic records `ambient` | Player comprehension and fatigue testing | Stage 6+ notification playtest panel | A documented tier study or owner decision |
| Announcement timing for loading states | Announce loading after a short delay; immediately announce failures/success | Screen-reader fatigue measurement | Built-UI assistive-technology pass | Test evidence on announcement thresholds |
| Draft preservation scope | Preserve unsent form input for the open session; do not promise reload persistence | Stage 5 storage/security decision | Built-UI interruption test | Approved client-state mechanism |
| Context-panel defaults (`13A-OQ-008`) | Section-specific defaults in 13B; no new data | Design review | Playtest navigation observation | Later design review |
| Mobile user-selectable mode (`13A-OQ-014`) | Same responsive rules; no mode switch | Real-device evidence | Stage 5 device matrix | Owner/Stage 5 decision |
| Notification grouping threshold | Group by source event and object without a numeric threshold | Fatigue testing | Stage 6+ notification study | Evidence-based threshold decision |
| Retry-offer timing after timeout | Offer reconciliation before any retry | Reliability measurement | Built-UI outage simulation | Stage 5 reliability evidence |
| Pins/favorites (`13A-OQ-012`) | Absent | Fair-play review | `SCR-020` gate review | Gate passes and a flow is specified |

Owner-reserved brand values (`13A-OQ-001/002`), dark mode (`13A-OQ-013`), icon set, final breakpoints (`13A-RD-06`), public test server (`13A-OQ-003`), search scope (`13A-OQ-005/009`) and performance budgets (`13A-OQ-016`) remain exactly as D-219 recorded. No interaction in this pass depends on a particular brand value.

### 17.3 External dependencies preserved

| Dependency | Effect on 13C |
|---|---|
| G-1…G-6 Global Trade gates | No trade flow, tutorial or notification references `SCR-038/039` as available |
| B-10 intelligence rule (none) | No flow references `SCR-068` |
| Fair-play review of pins (`13A-OQ-012`) | No `SCR-020` flow |
| Per-figure k=5 evidence | World Health (`SCR-077`) has no flow; suppression states are still specified |
| Stage 5 routing/storage/device work | Route keys are documentation identifiers; draft/stale-cache mechanisms are implementation matters |
| Owner-reserved `UD-017`, `UD-040`…`UD-060` | Alliance/support/report branches remain labelled; no value invented |
| Outstanding production security obligations | Unchanged; no fix claimed |

---

## 18. Requirements and traceability

### 18.1 Allocation and status policy

Prompt 13B's block ends at `REQ-1089`; the verified next free identifier is `REQ-1090`. This pass allocates **`REQ-1090`…`REQ-1203`** (114 requirements) and records the next free identifier as **`REQ-1204`**. No earlier requirement is renumbered, reworded, duplicated or status-changed.

**Status vocabulary:** `SPECIFIED` (fully specified in this documentation pass), `PROVISIONAL` (specified but gated by named evidence or an owner-reserved matter) and `BLOCKED` (the surface/feature must not exist until a named gate exists). No row is `APPROVED`, `IMPLEMENTED`, `VALIDATED` or `RELEASED`; none of those states has been earned.

**Verification intent:** `Structure` (document inspection), `Review` (human semantic review), `Runtime` (future built-UI test — **not performed**), `A11y-test` (future assistive-technology/device test — **not performed**). A future-test intent is a plan, never a result.

### 18.2 Requirement register (REQ-1090…REQ-1203)

| ID | Requirement | Category | Priority | Journey | Flow | Screens | Components | Governing system | Decision | Acceptance evidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `REQ-1090` | The first-time journey shall run landing → registration → verification → nation creation → onboarding → first objectives → digest, and shall not create a nation before e-mail verification. | Journey | P0 | `JRN-A` | `FLOW-001`…`FLOW-004` | `SCR-001`…`SCR-009`, `SCR-013` | `UI-CMP-001`, `UI-CMP-084`, `UI-CMP-088` | B-03; D-029 | D-223 | Structure | SPECIFIED |
| `REQ-1091` | The returning-player journey shall present the digest, open decisions and changed national state without an attendance reward, streak, decay or catch-up mechanic. | Journey | P0 | `JRN-B` | `FLOW-005`, `FLOW-006` | `SCR-013`, `SCR-014`, `SCR-016`, `SCR-019` | `UI-CMP-069`, `UI-CMP-070`, `UI-CMP-007` | B-02; TR-084/089; D-021 | D-223 | Structure | SPECIFIED |
| `REQ-1092` | The national-management journey shall proceed from digest to national overview to turn status to the owning section, and every overview card shall deep-link to its owning screen. | Journey | P0 | `JRN-C` | `FLOW-005` | `SCR-013`, `SCR-015`, `SCR-016`, section roots | `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-007` | B-02; B-04…B-10 | D-223 | Review | SPECIFIED |
| `REQ-1093` | The economy journey shall always distinguish total, reserved, available, forecast and historical values, and no economy interaction shall offer a reserved amount for new spending. | Journey | P0 | `JRN-D` | `FLOW-009`, `FLOW-010` | `SCR-029`…`SCR-034` | `UI-CMP-014`, `UI-CMP-033`, `UI-CMP-035` | B-04; MKT-053; ECN-110/177/178 | D-230 | Structure | SPECIFIED |
| `REQ-1094` | The directed-trade journey shall expose exactly the B-07 chain lifecycle, show both sides before acceptance, reserve nothing at creation, and revalidate both sides at acceptance. | Journey | P0 | `JRN-E` | `FLOW-011`…`FLOW-013` | `SCR-035`…`SCR-037`, `SCR-040` | `UI-CMP-046`, `UI-CMP-047`, `UI-CMP-033` | B-07; MKT-026/027/029/038/039 | D-223 | Review | SPECIFIED |
| `REQ-1095` | The cities/research journey shall enforce one construction-class action per city per turn, the 25% crown-only demolition refund, and one active research project, without inventing a queue object. | Journey | P0 | `JRN-F` | `FLOW-014`…`FLOW-016` | `SCR-041`…`SCR-046` | `UI-CMP-036`, `UI-CMP-037`, `UI-CMP-089` | B-05; URB-064/071/093; D-073/074/076 | D-223 | Structure | SPECIFIED |
| `REQ-1096` | The politics journey shall display the six-state banner on every political surface, apply one policy change per axis per 12-turn cooldown, and never offer a government-change control. | Journey | P0 | `JRN-G` | `FLOW-007`, `FLOW-008` | `SCR-021`…`SCR-028` | `UI-CMP-039`, `UI-CMP-040`, `UI-CMP-042` | B-06; DMP-102/189/268; D-084 | D-223 | Structure | SPECIFIED |
| `REQ-1097` | The diplomacy/alliance journey shall present directional posture, parties-only pending terms, ten-field proposal confirmation, and zero alliance military authority. | Journey | P0 | `JRN-H` | `FLOW-017`…`FLOW-020` | `SCR-047`…`SCR-058` | `UI-CMP-044`, `UI-CMP-047`, `UI-CMP-053` | B-08/B-09; D-030; 08C §12.3; AX-18 | D-223 | Review | SPECIFIED |
| `REQ-1098` | The warfare journey shall be nation-owner-only, show threat only as `LOW`/`MODERATE`/`HIGH`/`SEVERE`, require WAR-152 confirmation, and keep surrender available as the off-ramp. | Journey | P0 | `JRN-I` | `FLOW-021`…`FLOW-024` | `SCR-059`…`SCR-067` | `UI-CMP-057`, `UI-CMP-058`, `UI-CMP-062` | B-10; WAR-086/126/131/152 | D-223 | Review | SPECIFIED |
| `REQ-1099` | The world/progression journey shall show event cause and registered consequence, objectives with penalty-free dismissal, standings with denominator and window, and no composite score. | Journey | P0 | `JRN-J` | `FLOW-005`, `FLOW-025`, `FLOW-026` | `SCR-069`…`SCR-076`, `SCR-018` | `UI-CMP-064`, `UI-CMP-065`, `UI-CMP-068` | B-11; WEP-179/232/324/361 | D-223 | Review | SPECIFIED |
| `REQ-1100` | The notification/protection journey shall deep-link to the owning object, preserve non-opt-out notices, separate support from reporting, and keep the appeal route always reachable. | Journey | P0 | `JRN-K` | `FLOW-027`…`FLOW-029` | `SCR-019`, `SCR-081`…`SCR-087` | `UI-CMP-069`, `UI-CMP-085`, `UI-CMP-053` | B-02/B-12; MOD-002/013/017/018 | D-227 | Review | SPECIFIED |
| `REQ-1101` | The account journey shall disclose the 7-day cooling period and consequence list before closure, permit cancellation during cooling, and never present closure as a shield. | Journey | P0 | `JRN-L` | `FLOW-030`, `FLOW-031` | `SCR-011`, `SCR-012`, `SCR-090` | `UI-CMP-088`, `UI-CMP-090`, `OVL-02` | B-03; D-041; ACC-043; RRL-005/006 | D-223 | Review | SPECIFIED |
| `REQ-1102` | The administrative journey shall execute each action only within the holder's role and tier authority, require the specified second review, and never expose `SEC` data or player chrome. | Journey | P0 | `JRN-M` | `FLOW-032` | `SCR-091`…`SCR-100` | `UI-CMP-010`, `UI-CMP-022`, `OVL-02` | B-12; ADM-003/021/022; D-042 | D-223 | Review | SPECIFIED |
| `REQ-1103` | Registration shall validate e-mail pair, password policy, terms acknowledgement and the multi-account notice, and shall treat repeated submission as one intent. | Flow | P0 | `JRN-A` | `FLOW-001` | `SCR-002` | `UI-CMP-074`, `UI-CMP-083`, `UI-CMP-084` | B-03; D-018; D-029 | D-224 | Structure | SPECIFIED |
| `REQ-1104` | Login shall not disclose whether an e-mail exists, shall preserve the intended destination, and shall route an unverified account to `SCR-006` rather than the game. | Flow | P0 | `JRN-A`/`JRN-B` | `FLOW-002` | `SCR-003`, `SCR-006` | `UI-CMP-074`, `UI-CMP-084` | B-03; ACC-018; D-029 | D-224 | Structure | SPECIFIED |
| `REQ-1105` | Nation creation shall validate name and short name under D-038, show the start-state summary, confirm name/short name/emblem/posture, and create at most one nation. | Flow | P0 | `JRN-A` | `FLOW-003` | `SCR-007` | `UI-CMP-074`, `UI-CMP-084`, `UI-CMP-088` | B-03/B-04; NAT-005/026–030 | D-225 | Review | SPECIFIED |
| `REQ-1106` | The first-session onboarding step shall be skippable, resumable and labelled "now" or "at the next turn"; completing a view shall not complete a gameplay objective. | Flow | P1 | `JRN-A` | `FLOW-004` | `SCR-008`, `SCR-009` | `UI-CMP-016`, `UI-CMP-065` | B-03; ONB-009/013; D-040 | D-229 | Review | SPECIFIED |
| `REQ-1107` | The digest review shall group settled changes, open decisions and due-boundary items, each with cause and deep link, and shall consume only existing events. | Flow | P0 | `JRN-B`/`JRN-C` | `FLOW-005` | `SCR-013` | `UI-CMP-063`, `UI-CMP-069`, `UI-CMP-021` | B-02; TR-088/089; REQ-022 | D-227 | Structure | SPECIFIED |
| `REQ-1108` | Inbox triage shall order rows by due boundary, show owning system and state, and permit only the act/defer/cancel paths the owning rule defines. | Flow | P0 | `JRN-B`/`JRN-K` | `FLOW-006` | `SCR-014` | `UI-CMP-022`, `UI-CMP-070`, `UI-CMP-023` | B-02 + B-07…B-09; TR-004 | D-223 | Structure | SPECIFIED |
| `REQ-1109` | A policy change shall show the proposed setting, effect, cost, 12-turn cooldown and next eligible turn, then confirm once and record at the resolution turn. | Flow | P0 | `JRN-G` | `FLOW-007` | `SCR-024` | `UI-CMP-040`, `UI-CMP-089`, `OVL-01` | B-06; DMP-101/102; D-087 | D-225 | Review | SPECIFIED |
| `REQ-1110` | A campaign action shall offer exactly the three DMP-189 types with cost/effect, charge once at submission, and offer no cancellation or fourth action. | Flow | P0 | `JRN-G` | `FLOW-008` | `SCR-026` | `UI-CMP-042`, `OVL-01`, `UI-CMP-089` | B-06; DMP-189/193; D-094 | D-225 | Review | SPECIFIED |
| `REQ-1111` | A standing production-policy change shall state that it reserves nothing, applies at the defined recurring phase, and is not a manual order. | Flow | P0 | `JRN-D` | `FLOW-009` | `SCR-032` | `UI-CMP-035`, `UI-CMP-080`, `UI-CMP-088` | B-04; ECN-044; D-053 | D-225 | Structure | SPECIFIED |
| `REQ-1112` | A manual production order shall preview money, inputs, capacity and space reservation, reject overbooking, and commit fully or fail atomically. | Flow | P0 | `JRN-D` | `FLOW-010` | `SCR-032`, `SCR-033` | `UI-CMP-075`, `UI-CMP-033`, `UI-CMP-089` | B-04; ECN-045/049/053; F5 | D-225 | Review | SPECIFIED |
| `REQ-1113` | Directed-offer creation shall collect up to five lines per side, show available balances, pledge and imbalance facts, expiry and rate limit, and reserve nothing. | Flow | P0 | `JRN-E` | `FLOW-011` | `SCR-036` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-088` | B-07; MKT-019/022/030/038/059–067 | D-224 | Review | SPECIFIED |
| `REQ-1114` | Trade acceptance shall re-read both sides, confirm the exact terms and the MKT-038 pledge, and report an atomic all-or-nothing settlement or a named failure. | Flow | P0 | `JRN-E` | `FLOW-012` | `SCR-035`, `SCR-037` | `UI-CMP-046`, `UI-CMP-088`, `UI-CMP-021` | B-07; MKT-039/041/046; D-016 | D-225 | Review | SPECIFIED |
| `REQ-1115` | Counter, decline and cancel shall be offered only in the permitted lifecycle states, show the revision/expiry effect, and never present an accepted chain as cancellable. | Flow | P1 | `JRN-E` | `FLOW-013` | `SCR-035`, `SCR-036`, `SCR-037` | `UI-CMP-046`, `UI-CMP-086`, `UI-CMP-089` | B-07; MKT-028/029/047 | D-223 | Review | SPECIFIED |
| `REQ-1116` | A construction order shall show the full URB-148 preview, the single city slot, projected DC, cost after discounts, availability turn and book value before one confirmation. | Flow | P0 | `JRN-F` | `FLOW-014` | `SCR-042`, `SCR-043` | `UI-CMP-036`, `UI-CMP-088`, `UI-CMP-034` | B-05; URB-064/148 | D-225 | Review | SPECIFIED |
| `REQ-1117` | City founding shall show the eligibility checklist, crown and steel cost, expansion slot and new-city starting state, and shall not invent a cooldown. | Flow | P0 | `JRN-F` | `FLOW-015` | `SCR-046` | `UI-CMP-088`, `UI-CMP-084`, `UI-CMP-089` | B-05; URB-032–034; D-068 | D-225 | Review | SPECIFIED |
| `REQ-1118` | Research start shall enforce one active project, show RP/crown cost, prerequisite, effect and completion forecast, and record the project only after confirmation. | Flow | P0 | `JRN-F` | `FLOW-016` | `SCR-045` | `UI-CMP-037`, `UI-CMP-088`, `UI-CMP-016` | B-05; URB-093–097; D-076 | D-225 | Review | SPECIFIED |
| `REQ-1119` | A diplomatic proposal shall present the ten 08C §12.3 confirmation fields in order, never preselect acceptance, and keep pending terms parties-only. | Flow | P0 | `JRN-H` | `FLOW-017` | `SCR-049`, `SCR-050` | `UI-CMP-047`, `UI-CMP-088`, `UI-CMP-046` | B-08; D-030; 08C §12.3 | D-225 | Review | SPECIFIED |
| `REQ-1120` | Diplomatic acceptance shall revalidate the proposal state, record acceptance, and reflect activation/publication at the boundary the rule defines. | Flow | P0 | `JRN-H` | `FLOW-018` | `SCR-049`, `SCR-050`, `SCR-051` | `UI-CMP-045`, `UI-CMP-048`, `UI-CMP-021` | B-08; DIP-052/101/108–113 | D-225 | Review | SPECIFIED |
| `REQ-1121` | Alliance application/invitation responses shall terminate in-product, show applicant status privacy, and never require an external platform. | Flow | P1 | `JRN-H` | `FLOW-019` | `SCR-053`, `SCR-054` | `UI-CMP-049`, `UI-CMP-050`, `UI-CMP-053` | B-09; ALL-080–086; D-133 | D-223 | Review | SPECIFIED |
| `REQ-1122` | Alliance tax changes shall validate integer basis points 0–10,000, show the effective turn and policy version, and preserve the explicit 0% fallback. | Flow | P1 | `JRN-H` | `FLOW-020` | `SCR-056`, `SCR-057` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-052` | B-09; ALL-179–187; UD-040/UD-045 | D-225 | Review | SPECIFIED |
| `REQ-1123` | Military operation submission shall be owner-only, show OP/resource cost, objective, expected effect and block reason, and confirm per WAR-152 before submission. | Flow | P0 | `JRN-I` | `FLOW-021` | `SCR-061` | `UI-CMP-062`, `UI-CMP-057`, `UI-CMP-088` | B-10; WAR-046/152; REQ-589…591 | D-225 | Review | SPECIFIED |
| `REQ-1124` | War declaration shall show the 2 OP, 500 crowns, outgoing-slot and public-record consequences, and shall not be available through any alliance surface. | Flow | P0 | `JRN-I` | `FLOW-022` | `SCR-061`, `SCR-063` | `UI-CMP-062`, `UI-CMP-088`, `OVL-01` | B-10; WAR-152; AX-18 | D-225 | Review | SPECIFIED |
| `REQ-1125` | Settlement proposal and acceptance shall show every term and duration, enforce one live settlement, allow withdrawal before acceptance, and never infer consent from silence. | Flow | P0 | `JRN-I` | `FLOW-023` | `SCR-067` | `UI-CMP-047`, `UI-CMP-088`, `UI-CMP-021` | B-10; WAR-122/126/127 | D-225 | Review | SPECIFIED |
| `REQ-1126` | Surrender shall be available as a nation-owner action, disclose the campaign end and limited-victory consequence, require confirmation, and never be refused. | Flow | P0 | `JRN-I` | `FLOW-024` | `SCR-067` | `UI-CMP-087`, `OVL-02`, `UI-CMP-088` | B-10; WAR-131/132 | D-225 | Review | SPECIFIED |
| `REQ-1127` | Objective accept/dismiss shall be optional and penalty-free, show category and progress, and never require presence, membership, spending or aggression. | Flow | P1 | `JRN-J` | `FLOW-025` | `SCR-009`, `SCR-071` | `UI-CMP-065`, `UI-CMP-016` | B-11; WEP-203–215/232 | D-223 | Review | SPECIFIED |
| `REQ-1128` | A deferred reward claim shall remain visible and claimable where the B-11 flow permits, and shall never be presented as granted before resolution. | Flow | P1 | `JRN-J` | `FLOW-026` | `SCR-073`, `SCR-075` | `UI-CMP-066`, `UI-CMP-073` | B-11; WEP-240/582/705 | D-223 | Review | SPECIFIED |
| `REQ-1129` | Opening an alert shall deep-link to its object; an expired, retired, restricted or absent destination shall render the owning state and retain the history entry. | Flow | P1 | `JRN-K` | `FLOW-027` | `SCR-019`, owning screens | `UI-CMP-069`, `UI-CMP-027`, `OVL-05` | B-02/B-12; REQ-731 | D-227 | Review | SPECIFIED |
| `REQ-1130` | Report submission shall use exactly the MOD-002 fields, state that a report is an accusation, return an acknowledgement and case reference, and preserve nothing silently on failure. | Flow | P0 | `JRN-K` | `FLOW-028` | `SCR-081`, `SCR-082` | `UI-CMP-074`, `UI-CMP-076`, `UI-CMP-084` | B-12; MOD-002/007; FR-001/006 | D-224 | Review | SPECIFIED |
| `REQ-1131` | Appeal submission shall remain reachable under every restriction, show the status ladder and decision reasons, and never expose another player's data or a method. | Flow | P0 | `JRN-K` | `FLOW-029` | `SCR-083`, `SCR-084` | `UI-CMP-085`, `UI-CMP-021`, `UI-CMP-017` | B-12; MOD-013/015/042 | D-223 | Review | SPECIFIED |
| `REQ-1132` | Account closure request shall disclose cooling, retained restrictions, the no-shield rule and retention, then confirm; cancellation during cooling shall restore the account. | Flow | P0 | `JRN-L` | `FLOW-030` | `SCR-012` | `UI-CMP-088`, `OVL-01`, `UI-CMP-086` | B-03; ACC-043; D-041 | D-225 | Review | SPECIFIED |
| `REQ-1133` | Reroll shall require fresh re-authentication, the exact current nation name, the full consequence list and a destructive confirmation; blocked conditions shall be shown before the field. | Flow | P0 | `JRN-L` | `FLOW-031` | `SCR-090` | `UI-CMP-090`, `OVL-02`, `UI-CMP-089` | B-03; RRL-005/006/021; D-039 | D-225 | Review | SPECIFIED |
| `REQ-1134` | An administrative decision shall be permitted only within the holder's role and tier, show the two-person state, and append an audit record without exposing `SEC` data. | Flow | P0 | `JRN-M` | `FLOW-032` | `SCR-093`, `SCR-094`, `SCR-096` | `UI-CMP-010`, `UI-CMP-088`, `OVL-02` | B-12; MOD-022/036/037; ADM-003 | D-225 | Review | SPECIFIED |
| `REQ-1135` | A reconnection shall re-read the affected object, label prior data with its as-of turn, present an uncertain outcome as uncertain, and never auto-repeat a committing action. | Flow | P0 | `JRN-B`/`JRN-K` | `FLOW-033` | Shell; owning screens | `UI-CMP-007`, `UI-CMP-019`, `OVL-06` | B-02; TR-075/080/039 | D-228 | Review | SPECIFIED |
| `REQ-1136` | Every screen shall declare and render its applicable `ST-` states from the eighteen-state taxonomy, or record an exemption with reason. | State | P0 | All | All | All 100 | All applicable | 13A §6; 13B §6.3 | D-221 | Structure | SPECIFIED |
| `REQ-1137` | Initial, loaded and refreshing states shall preserve the shell, the previous confirmed content where safe, and a labelled as-of turn for any stale figure. | State | P0 | All | All | All authenticated | `UI-CMP-001`, `UI-CMP-012` | 13A §6; TR-039 | D-221 | Structure | SPECIFIED |
| `REQ-1138` | Loading shall never hide the whole application behind a full-page spinner; a skeleton or in-place progress shall identify what is loading. | State | P0 | All | All | All 100 | `UI-CMP-001`, `UI-CMP-016` | 13A §6; `REQ-970` | D-221 | Review | SPECIFIED |
| `REQ-1139` | Empty states shall distinguish no records, no matches, no pending acts, no notifications, no history, no eligible actions, unavailable feature and permission-restricted content, and shall explain why. | State | P0 | All | All | List/dashboard screens | `UI-CMP-019`, `UI-CMP-022` | 13A §6; D-216 | D-221 | Review | SPECIFIED |
| `REQ-1140` | Partial-data states shall name the missing, suppressed or provisional part and shall never fabricate a value or present a partial aggregate as complete. | State | P0 | All | All | Data screens | `UI-CMP-072`, `OVL-07` | D-027; ECN-178 | D-221 | Structure | SPECIFIED |
| `REQ-1141` | Success shall be shown only after authoritative resolution, distinguish accepted/processing/completed/rejected/pending, and include the resulting state and charge. | State | P0 | All | All | Committing screens | `UI-CMP-088`, `OVL-01` | B-02 §17; TR-038 | D-221 | Review | SPECIFIED |
| `REQ-1142` | Validation errors shall identify the field, the problem, the reason, the correction and whether input is preserved, in text linked to the field. | State | P0 | All | All | All forms | `UI-CMP-084`, `UI-CMP-083` | 13A-DS-11; `REQ-1086` | D-224 | Review | SPECIFIED |
| `REQ-1143` | Permission-denied states shall name the permitted restriction class and shall never imply the protected object does not exist where that disclosure matters. | State | P0 | All | All | Permission-sensitive screens | `UI-CMP-053`, `UI-CMP-089` | NET-023/050; `REQ-1029` | D-230 | Review | SPECIFIED |
| `REQ-1144` | Unavailable/conditional states shall explain absence honestly and shall never render a stub, teaser, partial control or implied availability. | State | P0 | All | All | `SCR-020`, `SCR-038`, `SCR-039`, `SCR-068`, `SCR-077` | `UI-CMP-019` | D-216; `REQ-907/937/946` | D-221 | Structure | SPECIFIED |
| `REQ-1145` | Blocked-by-rule states shall show the specific block reason, the governing rule and the next eligible turn or condition where one exists. | State | P0 | All | All | All action screens | `UI-CMP-089`, `OVL-03` | 13A-PR-10; 08C §12.7 | D-221 | Review | SPECIFIED |
| `REQ-1146` | Expired, conflict and failed states shall state whether anything changed, whether a retry is safe, and what the player can do next. | State | P0 | All | All | All screens | `UI-CMP-019`, `UI-CMP-084` | 13A §6; `REQ-1088` | D-221 | Review | SPECIFIED |
| `REQ-1147` | Offline, reconnecting and recovering states shall be distinct, persistent across reload where applicable, and shall never simulate settlement or queue a committing action. | State | P0 | All | All | Shell; owning screens | `UI-CMP-007`, `OVL-06` | TR-075/080 | D-228 | Review | SPECIFIED |
| `REQ-1148` | Cancelled states shall confirm that nothing committed, nothing was charged and nothing remains reserved, and shall name the safe return. | State | P0 | All | All | Task screens | `UI-CMP-086`, `UI-CMP-088` | 13A §6; `IP-05` | D-221 | Review | SPECIFIED |
| `REQ-1149` | Every state shall be conveyed by text plus tone and glyph, never colour alone, and shall be announced at the appropriate politeness. | State | P0 | All | All | All screens | All state-bearing | 13A-DS-10/13; `REQ-1014` | D-221 | A11y-test | SPECIFIED |
| `REQ-1150` | A state that persists (denied, expired, suppressed, offline, failed) shall be reconstructed from the authoritative record on reload, not from a one-time client notice. | State | P0 | All | All | All screens | `UI-CMP-019`, `UI-CMP-017` | TR-039; `REQ-1088` | D-221 | Review | SPECIFIED |
| `REQ-1151` | A submitted-but-unsettled action shall remain visibly pending with its owning system, reservations and resolution point until the authoritative settlement. | State | P0 | All | All | `SCR-013/014/016` + owning screens | `UI-CMP-070`, `UI-CMP-016` | TR-004; B-02 §17 | D-221 | Review | SPECIFIED |
| `REQ-1152` | Suppressed and insufficient-sample states shall render as their named state on every device and shall never be represented by zero, blank space or an omitted card. | State | P0 | All | All | Aggregate surfaces | `UI-CMP-072`, `OVL-07` | D-027; `REQ-1066` | D-221 | Structure | SPECIFIED |
| `REQ-1153` | A `PROVISIONAL_BLOCK` or provisional-value state shall be labelled provisional and shall never be presented as an approved value or completed rule. | State | P1 | All | All | Provisional surfaces | `UI-CMP-019`, `UI-CMP-084` | D-194; `UR-037` | D-221 | Review | SPECIFIED |
| `REQ-1154` | Validation shall run on blur for format, on submit for required/cross-field, and always server-side for permission, ownership, state, resources and rules; typing shall not trigger repetitive error messages. | Validation | P0 | All | All | All forms | `UI-CMP-074`…`UI-CMP-084` | 13A-PR-10; `REQ-1086` | D-224 | Review | SPECIFIED |
| `REQ-1155` | Every action-confirmation shall include the exact action, known cost, resource impact, cooldown, turn/phase, consequences, confirm and cancel, with confirm never preselected or remembered. | Validation | P0 | All | All committing | All committing screens | `UI-CMP-088`, `OVL-01` | D-214; RRL-006; WAR-152; 08C §12.3 | D-225 | Structure | SPECIFIED |
| `REQ-1156` | Destructive actions shall use the separated destructive pattern, consequence-first content and the exact-phrase barrier where the owning rule requires it. | Validation | P0 | `JRN-L`/`JRN-M` | `FLOW-031`, `FLOW-032` | `SCR-012`, `SCR-090`, `SCR-094` | `UI-CMP-087`, `UI-CMP-090`, `OVL-02` | RRL-006; `REQ-959` | D-225 | Structure | SPECIFIED |
| `REQ-1157` | A committing control shall be single-flight: repeated activation while in flight is ignored, and the same pointer/keyboard intent never produces two submissions. | Validation | P0 | All | All committing | All committing screens | `UI-CMP-085` | TR-004; SEC-014 discipline | D-225 | Review | SPECIFIED |
| `REQ-1158` | A timed-out or interrupted submission shall be presented as uncertain until reconciled by re-reading the object; retry shall be offered only with a safe idempotency basis or after reconciliation. | Validation | P0 | All | `FLOW-033` | All committing screens | `UI-CMP-019`, `OVL-06` | TR-075; `IP-04` | D-228 | Review | SPECIFIED |
| `REQ-1159` | Duplicate suppression shall never invent a backend idempotency mechanism; where the owning system defines a key, the retry shall reuse it, and the dependency shall be recorded. | Validation | P0 | All | All committing | All committing screens | `UI-CMP-085` | D-225; MKT-041; ALL-193 | D-225 | Review | SPECIFIED |
| `REQ-1160` | A failure message shall state what happened, whether anything changed, whether the action completed, whether retry is safe and the next step, without internal detail. | Validation | P0 | All | All | All screens | `UI-CMP-084`, `UI-CMP-019` | 13A §6; `REQ-1077` | D-224 | Review | SPECIFIED |
| `REQ-1161` | Authentication expiry, authorization failure, conflict, stale state, rule rejection and rate limit shall each map to a distinct named failure treatment, not one generic error. | Validation | P0 | All | All | All screens | `UI-CMP-019` | `ERR-01`…`ERR-20`; owning catalogues | D-224 | Review | SPECIFIED |
| `REQ-1162` | Every essential journey shall be fully keyboard-operable in reading order with visible focus, with no essential function requiring a pointer. | Accessibility | P0 | All | All | All screens | All interactive | 13A-DS-07; `REQ-1081` | D-226 | A11y-test | SPECIFIED |
| `REQ-1163` | Overlays shall trap focus, cancel-first focus order, restore focus to the invoker, and never trap focus outside a modal. | Accessibility | P0 | All | All | Overlay invocations | `OVL-01`…`OVL-08` | D-215; `REQ-1081` | D-226 | A11y-test | SPECIFIED |
| `REQ-1164` | Every screen transition shall update the page title and move focus to the screen heading; asynchronous results shall not steal focus. | Accessibility | P0 | All | All | All screens | `UI-CMP-004` | `REQ-1013`; `UR-044` | D-226 | A11y-test | SPECIFIED |
| `REQ-1165` | Validation errors shall be programmatically associated with their fields and summarised; the summary or first invalid field shall receive focus on failed submission. | Accessibility | P0 | All | All | All forms | `UI-CMP-084`, `UI-CMP-083` | 13A-DS-11; `REQ-1086` | D-226 | A11y-test | SPECIFIED |
| `REQ-1166` | Loading, success, failure, suppression, permission, blocked, expired, conflict, offline, reconnecting and recovery states shall be announced exactly once at an appropriate politeness. | Accessibility | P0 | All | All | All screens | All state-bearing | 13A-DS-13; `REQ-1016` | D-226 | A11y-test | SPECIFIED |
| `REQ-1167` | Tables shall expose semantic headers and scope; card fallbacks shall preserve the same labels and reading order; chart alternatives shall be reachable without interacting with the chart. | Accessibility | P0 | All | All | Table/chart screens | `UI-CMP-022`, `UI-CMP-030` | `REQ-1059`, `REQ-1083` | D-226 | A11y-test | SPECIFIED |
| `REQ-1168` | Text shall reflow at 320 CSS px and survive 200% text resize and 200% zoom without loss of content or horizontal page scroll. | Accessibility | P0 | All | All | All screens | All layouts | 13A-RD-05; `REQ-1051` | D-230 | A11y-test | SPECIFIED |
| `REQ-1169` | Touch targets shall meet the WCAG 2.2 AA 24×24 CSS-px minimum and the DS-14 token; destructive controls shall be separated from primary controls. | Accessibility | P0 | All | All | Task/mobile screens | `UI-CMP-085`, `UI-CMP-087` | `REQ-1055`; 13A-DS-14 | D-230 | A11y-test | SPECIFIED |
| `REQ-1170` | Motion shall respect reduced-motion preferences; no state may depend on motion; countdown announcements shall not fire continuously. | Accessibility | P1 | All | All | All screens | `UI-CMP-007` | 13A-DS-13; `REQ-1085` | D-226 | A11y-test | SPECIFIED |
| `REQ-1171` | Every accessibility interaction requirement shall be verified against a built UI; this specification shall not be reported as conformance evidence. | Accessibility | P0 | All | All | All screens | All | `UR-010`; B-13 §10.3 | D-232 | Review | SPECIFIED |
| `REQ-1172` | Account setup shall remain mandatory only where the owning rule requires it; every other tutorial or guidance layer shall be optional and non-blocking. | Onboarding | P0 | `JRN-A` | `FLOW-004` | `SCR-002`…`SCR-009` | `UI-CMP-016`, `UI-CMP-019` | B-03; ONB-009; D-040 | D-229 | Structure | SPECIFIED |
| `REQ-1173` | A tutorial shall never execute a gameplay action, spend resources, submit a trade/diplomacy/military action, override a restriction or force an irreversible act. | Onboarding | P0 | `JRN-A` | `FLOW-004` | All tutorial screens | `UI-CMP-019` | D-040; `IP-02` | D-229 | Review | SPECIFIED |
| `REQ-1174` | A tutorial shall be skippable, resumable, replayable read-only and dismissible, with completion recorded once per account and never re-granted. | Onboarding | P0 | `JRN-A` | `FLOW-004` | `SCR-008`, `SCR-078` | `UI-CMP-016`, `UI-CMP-065` | D-040; ONB-009 | D-229 | Review | SPECIFIED |
| `REQ-1175` | The orientation tutorials shall explain the fictional premise, the two-hour UTC cadence, the shell and the difference between "now" and "at the next turn". | Onboarding | P1 | `JRN-A` | `FLOW-004` | `SCR-008`, `SCR-013`, `SCR-016` | `UI-CMP-007`, `UI-CMP-019` | `TUT-01`…`TUT-03`; TR-024 | D-229 | Review | SPECIFIED |
| `REQ-1176` | The management tutorials shall explain dashboard reading, financial total/reserved/available, political state and production/construction without demonstrating an outcome the rules do not guarantee. | Onboarding | P1 | `JRN-C`/`JRN-D`/`JRN-F`/`JRN-G` | `FLOW-009`, `FLOW-014` | `SCR-015`, `SCR-029`, `SCR-021`, `SCR-043` | `UI-CMP-033`, `UI-CMP-039`, `UI-CMP-035` | `TUT-04`…`TUT-07`; ECN-177; DMP-268 | D-229 | Review | SPECIFIED |
| `REQ-1177` | The social and warfare tutorials shall explain directed trade, diplomacy, protection and owner-only military action without implying that any alliance grants military authority. | Onboarding | P1 | `JRN-E`/`JRN-H`/`JRN-I` | `FLOW-011`, `FLOW-017`, `FLOW-021` | `SCR-035`, `SCR-049`, `SCR-059`, `SCR-089` | `UI-CMP-043`, `UI-CMP-053`, `UI-CMP-058` | `TUT-08`…`TUT-10`; AX-18 | D-229 | Review | SPECIFIED |
| `REQ-1178` | The progression and support tutorials shall explain objectives, re-entry, notifications, help and the support/report/appeal separation. | Onboarding | P1 | `JRN-J`/`JRN-K` | `FLOW-025`, `FLOW-027`, `FLOW-028` | `SCR-071`, `SCR-078`, `SCR-087` | `UI-CMP-065`, `UI-CMP-069` | `TUT-11`, `TUT-12`; MOD-002 | D-229 | Review | SPECIFIED |
| `REQ-1179` | Contextual help shall be available on every screen and shall link the exact governing rule without leaving the screen's context. | Onboarding | P1 | All | All | All screens | `UI-CMP-011`, `OVL-04` | F-010; DP-004; `REQ-947` | D-229 | Review | SPECIFIED |
| `REQ-1180` | Tutorial interruption, logout, reroll or a blocking state shall leave progress resumable and shall never auto-complete a step or lose a preference silently. | Onboarding | P1 | `JRN-A` | `FLOW-004` | `SCR-008` | `UI-CMP-016` | D-040; ONB-009 | D-229 | Review | SPECIFIED |
| `REQ-1181` | Tutorial content and controls shall meet the same accessibility interaction requirements as normal play, including focus, labels, skip controls and announcements. | Onboarding | P0 | `JRN-A` | `FLOW-004` | All tutorial screens | All interactive | `REQ-1162`…`REQ-1171` | D-229 | A11y-test | SPECIFIED |
| `REQ-1182` | Notifications shall be generated only from existing owning-system events; no interaction may create, mutate, suppress or fabricate an event. | Notification | P0 | All | All | `SCR-013/014/019` | `UI-CMP-008`, `UI-CMP-069` | REQ-731; `REQ-976` | D-227 | Structure | SPECIFIED |
| `REQ-1183` | Notification routing tiers shall be `blocking`, `digest` and `ambient`, with defaults provisional and non-opt-out items preserved. | Notification | P1 | `JRN-K` | `FLOW-027` | `SCR-019` | `UI-CMP-069` | DIP-114/116; `13A-OQ-006` | D-227/D-232 | Review | PROVISIONAL |
| `REQ-1184` | Opening a notification shall deep-link to the owning object or render its retired/expired/restricted/absent state without losing the history record. | Notification | P0 | `JRN-K` | `FLOW-027` | `SCR-019` + owning screens | `UI-CMP-027`, `OVL-05` | `REQ-731`; `REQ-995` | D-227 | Review | SPECIFIED |
| `REQ-1185` | Notifications shall be grouped by source event and object, show read/unread state, and permit mute only where the owning rule allows. | Notification | P1 | `JRN-K` | `FLOW-027` | `SCR-019` | `UI-CMP-069` | `REQ-731`; DIP-114/116 | D-227 | Review | PROVISIONAL |
| `REQ-1186` | Non-opt-out security, appeal and statutory notices shall remain visible and mutable only where the rule permits, and shall never be silently dropped. | Notification | P0 | `JRN-K` | `FLOW-027`, `FLOW-029` | `SCR-019`, `SCR-083`, `SCR-084` | `UI-CMP-069`, `UI-CMP-008` | MOD-013; DIP-114/116 | D-227 | Structure | SPECIFIED |
| `REQ-1187` | Notification arrival and count changes shall not steal focus and shall be announced politely without repeating each count increment. | Notification | P0 | `JRN-K` | `FLOW-027` | Shell; `SCR-019` | `UI-CMP-008`, `UI-CMP-069` | `REQ-1166`; 13A-DS-13 | D-227 | A11y-test | SPECIFIED |
| `REQ-1188` | Offline mode shall be read-only: no offline gameplay, no queued committing action, no offline settlement and no simulated boundary result. | Offline | P0 | All | `FLOW-033` | All authenticated | `UI-CMP-019` | D-008; TR-024 | D-228 | Review | SPECIFIED |
| `REQ-1189` | Previously confirmed data may remain visible offline only when labelled with its as-of turn; no new read shall be presented as current while disconnected. | Offline | P0 | All | `FLOW-033` | All authenticated | `UI-CMP-012` | TR-039/049 | D-228 | Review | SPECIFIED |
| `REQ-1190` | Session expiration shall preserve the intended destination and the safe unsent input, require re-authentication, and never disclose credentials or retain secrets. | Offline | P0 | `JRN-A`/`JRN-L` | `FLOW-002` | `SCR-003`, `SCR-080` | `UI-CMP-074`, `UI-CMP-017` | D-041; ACC-031 | D-228 | Review | SPECIFIED |
| `REQ-1191` | Browser refresh or closure during a committing request shall not assume success or failure; on return the object state shall be re-read and shown. | Offline | P0 | All | `FLOW-033` | All committing screens | `UI-CMP-019` | TR-075 | D-228 | Review | SPECIFIED |
| `REQ-1192` | Reconnection shall refresh the affected data, label replaced values with their new as-of turn, and surface any conflict or stale input before resubmission. | Offline | P0 | All | `FLOW-033` | All authenticated | `UI-CMP-019`, `OVL-06` | TR-039/075/080 | D-228 | Review | SPECIFIED |
| `REQ-1193` | No automatic retry of a committing action shall occur without a safe idempotency basis; a failed or interrupted turn shall be shown as a delay, not a lost turn. | Offline | P0 | All | `FLOW-033` | All committing screens | `UI-CMP-019`, `UI-CMP-007` | TR-080; `IP-04` | D-228 | Review | SPECIFIED |
| `REQ-1194` | Navigation, breadcrumbs, back/forward, title and focus shall behave consistently on every screen and never return to an absent or denied surface. | Consistency | P0 | All | All | All 100 | `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005` | D-209; `REQ-1013` | D-230 | Review | SPECIFIED |
| `REQ-1195` | The same object shall present the same identity, status, ownership, permissions and updated values on every screen at the same as-of turn. | Consistency | P0 | All | All | All object screens | `UI-CMP-027`, `UI-CMP-012` | TR-021; `IP-08` | D-230 | Review | SPECIFIED |
| `REQ-1196` | Financial values shall not contradict across screens: total/reserved/available, forecast and historical registers, units and as-of turns shall agree; reserved shall never appear spendable. | Consistency | P0 | `JRN-D`/`JRN-E` | All financial flows | Economy/market/alliance | `UI-CMP-033`, `UI-CMP-014` | MKT-053; ECN-110/177/178 | D-230 | Structure | SPECIFIED |
| `REQ-1197` | An action available on one screen shall not be unexplained-denied on another; permissions shall present the same restriction class and never widen visibility through a layout hint. | Consistency | P0 | All | All | Permission-sensitive screens | `UI-CMP-053`, `UI-CMP-089` | `REQ-1088`; NET-023/050 | D-230 | Review | SPECIFIED |
| `REQ-1198` | Canonical parents, route keys, aliases and conditional absence shall remain stable; no journey may create a duplicate route, screen copy or teaser for an absent feature. | Consistency | P0 | All | All | All 100 | `UI-CMP-002` | D-209; D-216 | D-230 | Structure | SPECIFIED |
| `REQ-1199` | Search, filters, pagination and saved views shall use the same grammar and semantics on every list screen, with exact counts and preserved state. | Consistency | P1 | All | All | List screens | `UI-CMP-023`…`UI-CMP-026` | `REQ-991`…`REQ-994` | D-230 | Review | SPECIFIED |
| `REQ-1200` | Confirmation, disabled-reason and destructive patterns shall be identical in structure across systems, while carrying the owning rule's exact content. | Consistency | P0 | All | All committing | All committing screens | `UI-CMP-088`, `UI-CMP-089`, `OVL-01/02/03` | D-214; `REQ-1049` | D-230 | Structure | SPECIFIED |
| `REQ-1201` | Feedback shall not duplicate: one action produces one primary result message plus at most one grouped notification, and never contradictory success/failure messages. | Consistency | P0 | All | All | All screens | `UI-CMP-069`, `UI-CMP-084` | `REQ-731`; `IP-01` | D-230 | Review | SPECIFIED |
| `REQ-1202` | Desktop, tablet and mobile shall present the same data, actions and confirmation content; layout simplification may never remove a must-not-simplify field. | Consistency | P0 | All | All | All screens | All applicable | `REQ-1051`, `REQ-1052` | D-230 | Review | SPECIFIED |
| `REQ-1203` | The Prompt 13C registers and matrices shall remain internally traceable: every requirement names a journey and flow; every flow names screens, components and requirements; no undefined identifier is referenced. | Consistency | P0 | All | All | All | All | D-231; `REQ-1089` | D-231 | Structure | SPECIFIED |

**Requirement tally:** 114 rows — **112 SPECIFIED**, **2 PROVISIONAL** (`REQ-1183`, `REQ-1185`), **0 BLOCKED**. The next free identifier is `REQ-1204`.

### 18.3 Matrix A — Journey-to-screen traceability

| Journey | Name | Screens | Flows | Requirements |
|---|---|---|---|---|
| `JRN-A` | Account and first-time player experience | `SCR-001`…`SCR-009`, `SCR-013` | `FLOW-001`…`FLOW-004` | `REQ-1090`, `REQ-1103`…`REQ-1106`, `REQ-1172`…`REQ-1181` |
| `JRN-B` | Returning player experience | `SCR-003`, `SCR-013`…`SCR-019` | `FLOW-002`, `FLOW-005`, `FLOW-006`, `FLOW-033` | `REQ-1091`, `REQ-1107`, `REQ-1108`, `REQ-1135` |
| `JRN-C` | National management | `SCR-013`, `SCR-015`, `SCR-016`, section roots | `FLOW-005`, `FLOW-006` | `REQ-1092`, `REQ-1107` |
| `JRN-D` | Economy and treasury | `SCR-029`…`SCR-034` | `FLOW-009`, `FLOW-010` | `REQ-1093`, `REQ-1111`, `REQ-1112`, `REQ-1196` |
| `JRN-E` | Trade | `SCR-035`…`SCR-037`, `SCR-040` | `FLOW-011`…`FLOW-013` | `REQ-1094`, `REQ-1113`…`REQ-1115` |
| `JRN-F` | Cities, infrastructure and research | `SCR-041`…`SCR-046` | `FLOW-014`…`FLOW-016` | `REQ-1095`, `REQ-1116`…`REQ-1118` |
| `JRN-G` | Politics and domestic governance | `SCR-021`…`SCR-028` | `FLOW-007`, `FLOW-008` | `REQ-1096`, `REQ-1109`, `REQ-1110` |
| `JRN-H` | Diplomacy and alliances | `SCR-047`…`SCR-058` | `FLOW-017`…`FLOW-020` | `REQ-1097`, `REQ-1119`…`REQ-1122` |
| `JRN-I` | Warfare and military | `SCR-059`…`SCR-067` | `FLOW-021`…`FLOW-024` | `REQ-1098`, `REQ-1123`…`REQ-1126` |
| `JRN-J` | World and progression | `SCR-018`, `SCR-069`…`SCR-076` | `FLOW-025`, `FLOW-026` | `REQ-1099`, `REQ-1127`, `REQ-1128` |
| `JRN-K` | Notifications and player protection | `SCR-019`, `SCR-081`…`SCR-087` | `FLOW-027`…`FLOW-029` | `REQ-1100`, `REQ-1129`…`REQ-1131`, `REQ-1182`…`REQ-1187` |
| `JRN-L` | Account management | `SCR-011`, `SCR-012`, `SCR-080`, `SCR-090` | `FLOW-030`, `FLOW-031` | `REQ-1101`, `REQ-1132`, `REQ-1133` |
| `JRN-M` | Administrative | `SCR-091`…`SCR-100` | `FLOW-032` | `REQ-1102`, `REQ-1134` |

### 18.4 Matrix B — Interaction-flow-to-screen traceability

| Flow | Name | Screens | Requirements |
|---|---|---|---|
| `FLOW-001` | Registration and verification | `SCR-002`, `SCR-006` | `REQ-1103` |
| `FLOW-002` | Login and session entry | `SCR-003`, `SCR-013`, `SCR-006` | `REQ-1104` |
| `FLOW-003` | Nation creation | `SCR-007`, `SCR-008` | `REQ-1105` |
| `FLOW-004` | First-session onboarding step | `SCR-008`, `SCR-009`, `SCR-013` | `REQ-1106` |
| `FLOW-005` | Return, digest review and next action | `SCR-013`, `SCR-015`, `SCR-016` | `REQ-1107` |
| `FLOW-006` | Inbox triage and object return | `SCR-014`, owning screens | `REQ-1108` |
| `FLOW-007` | Policy change | `SCR-024`, `SCR-023` | `REQ-1109` |
| `FLOW-008` | Campaign action | `SCR-026`, `SCR-025` | `REQ-1110` |
| `FLOW-009` | Standing production-policy change | `SCR-032`, `SCR-044` | `REQ-1111` |
| `FLOW-010` | Manual production order | `SCR-032`, `SCR-033` | `REQ-1112` |
| `FLOW-011` | Directed trade offer creation | `SCR-036`, `SCR-035` | `REQ-1113` |
| `FLOW-012` | Trade acceptance and settlement | `SCR-035`, `SCR-037` | `REQ-1114` |
| `FLOW-013` | Trade counter, decline and cancel | `SCR-035`…`SCR-037` | `REQ-1115` |
| `FLOW-014` | Construction order | `SCR-042`, `SCR-043` | `REQ-1116` |
| `FLOW-015` | City founding | `SCR-046`, `SCR-041` | `REQ-1117` |
| `FLOW-016` | Research start | `SCR-045` | `REQ-1118` |
| `FLOW-017` | Diplomatic proposal submit/counter/withdraw | `SCR-049`, `SCR-048` | `REQ-1119` |
| `FLOW-018` | Diplomatic acceptance and activation | `SCR-049`, `SCR-050`, `SCR-051` | `REQ-1120` |
| `FLOW-019` | Alliance application/invitation response | `SCR-053`, `SCR-054` | `REQ-1121` |
| `FLOW-020` | Alliance tax bracket change | `SCR-056`, `SCR-057` | `REQ-1122` |
| `FLOW-021` | Military operation submission | `SCR-061`, `SCR-060` | `REQ-1123` |
| `FLOW-022` | War declaration | `SCR-061`, `SCR-063` | `REQ-1124` |
| `FLOW-023` | Settlement proposal and acceptance | `SCR-067`, `SCR-063` | `REQ-1125` |
| `FLOW-024` | Surrender | `SCR-067` | `REQ-1126` |
| `FLOW-025` | Objective accept/dismiss | `SCR-009`, `SCR-071` | `REQ-1127` |
| `FLOW-026` | Deferred reward claim | `SCR-073`, `SCR-075` | `REQ-1128` |
| `FLOW-027` | Alert open and deep link | `SCR-019`, owning screens | `REQ-1129`, `REQ-1184` |
| `FLOW-028` | Report submission | `SCR-081`, `SCR-082` | `REQ-1130` |
| `FLOW-029` | Appeal submission | `SCR-083`, `SCR-084` | `REQ-1131`, `REQ-1186` |
| `FLOW-030` | Account closure request/cancel | `SCR-012`, `SCR-011` | `REQ-1132` |
| `FLOW-031` | Reroll exact-phrase flow | `SCR-090`, `SCR-007` | `REQ-1133`, `REQ-1156` |
| `FLOW-032` | Administrative moderation decision | `SCR-092`…`SCR-096`, `SCR-100` | `REQ-1134` |
| `FLOW-033` | Boundary reconnection and stale-data recovery | Shell, owning screens, `SCR-016` | `REQ-1135`, `REQ-1188`…`REQ-1193` |

### 18.5 Matrix C — Interaction-flow-to-component traceability

| Flow | Components | Governing rule anchors |
|---|---|---|
| `FLOW-001` | `UI-CMP-074`, `UI-CMP-078`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-085`, `OVL-01` | ACC-023/024; D-029 |
| `FLOW-002` | `UI-CMP-074`, `UI-CMP-085`, `UI-CMP-086`, `UI-CMP-017` | ACC-018; D-041 |
| `FLOW-003` | `UI-CMP-074`, `UI-CMP-079`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-088`, `OVL-01` | NAT-005/026–030; D-038/D-063 |
| `FLOW-004` | `UI-CMP-016`, `UI-CMP-019`, `UI-CMP-065` | ONB-009/013; D-040 |
| `FLOW-005` | `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-063`, `UI-CMP-069`, `UI-CMP-021` | TR-088/089; REQ-022 |
| `FLOW-006` | `UI-CMP-022`, `UI-CMP-023`, `UI-CMP-070` | TR-004; D-016/D-030 |
| `FLOW-007` | `UI-CMP-040`, `UI-CMP-089`, `UI-CMP-088`, `OVL-01`, `OVL-03` | DMP-101/102; D-087 |
| `FLOW-008` | `UI-CMP-042`, `UI-CMP-089`, `UI-CMP-088`, `OVL-01` | DMP-189/193; D-094 |
| `FLOW-009` | `UI-CMP-035`, `UI-CMP-080`, `UI-CMP-033`, `UI-CMP-088` | ECN-044; D-053 |
| `FLOW-010` | `UI-CMP-075`, `UI-CMP-033`, `UI-CMP-089`, `UI-CMP-084` | ECN-045/049/053 |
| `FLOW-011` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-083`, `UI-CMP-088`, `OVL-01` | MKT-019/022/038 |
| `FLOW-012` | `UI-CMP-046`, `UI-CMP-088`, `UI-CMP-021`, `UI-CMP-022` | MKT-039/046; D-016 |
| `FLOW-013` | `UI-CMP-046`, `UI-CMP-086`, `UI-CMP-089`, `UI-CMP-076` | MKT-028/029/047 |
| `FLOW-014` | `UI-CMP-036`, `UI-CMP-088`, `UI-CMP-034`, `UI-CMP-089` | URB-064/148; D-073 |
| `FLOW-015` | `UI-CMP-088`, `UI-CMP-084`, `UI-CMP-089`, `UI-CMP-033` | URB-032–034; D-068 |
| `FLOW-016` | `UI-CMP-037`, `UI-CMP-088`, `UI-CMP-016`, `UI-CMP-089` | URB-093–097; D-076 |
| `FLOW-017` | `UI-CMP-047`, `UI-CMP-088`, `UI-CMP-046`, `OVL-01` | 08C §12.3; D-030 |
| `FLOW-018` | `UI-CMP-045`, `UI-CMP-048`, `UI-CMP-088`, `UI-CMP-021` | DIP-052/101/108–113 |
| `FLOW-019` | `UI-CMP-049`, `UI-CMP-050`, `UI-CMP-053`, `OVL-03` | ALL-080–086; D-133 |
| `FLOW-020` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-088`, `UI-CMP-052` | ALL-179–187; UD-040/UD-045 |
| `FLOW-021` | `UI-CMP-062`, `UI-CMP-057`, `UI-CMP-058`, `UI-CMP-088` | WAR-046/152; REQ-589…591 |
| `FLOW-022` | `UI-CMP-062`, `UI-CMP-088`, `OVL-01`, `UI-CMP-058` | WAR-152; AX-18 |
| `FLOW-023` | `UI-CMP-047`, `UI-CMP-088`, `UI-CMP-021`, `OVL-01` | WAR-122/126/127 |
| `FLOW-024` | `UI-CMP-087`, `OVL-02`, `UI-CMP-088` | WAR-131/132 |
| `FLOW-025` | `UI-CMP-065`, `UI-CMP-016`, `UI-CMP-086` | WEP-203–215/232 |
| `FLOW-026` | `UI-CMP-066`, `UI-CMP-073`, `UI-CMP-088` | WEP-240/582/705 |
| `FLOW-027` | `UI-CMP-069`, `UI-CMP-027`, `OVL-05` | REQ-731; DIP-114/116 |
| `FLOW-028` | `UI-CMP-074`, `UI-CMP-076`, `UI-CMP-083`, `UI-CMP-084`, `OVL-01` | MOD-002/007; FR-001/006 |
| `FLOW-029` | `UI-CMP-085`, `UI-CMP-021`, `UI-CMP-017`, `UI-CMP-084` | MOD-013/015/042 |
| `FLOW-030` | `UI-CMP-088`, `OVL-01`, `UI-CMP-086`, `UI-CMP-017` | ACC-043; D-041 |
| `FLOW-031` | `UI-CMP-090`, `OVL-02`, `UI-CMP-089`, `UI-CMP-087` | RRL-005/006/021; D-039 |
| `FLOW-032` | `UI-CMP-010`, `UI-CMP-022`, `UI-CMP-088`, `OVL-02`, `UI-CMP-017` | MOD-022/036/037; ADM-003 |
| `FLOW-033` | `UI-CMP-007`, `UI-CMP-019`, `OVL-06`, `UI-CMP-012` | TR-075/080/039 |

### 18.6 Matrix D — State-to-component coverage

Matrix D is owned by the state companion §16. It maps `ST-01`…`ST-18` to every component family and records, for each of the 90 components and 8 overlays, the applicable states, visible feedback, interaction availability, focus behaviour, transitions, persistence and screen dependencies. The family summary is: shell → all states where the shell persists; display → loading/empty/partial/suppressed/stale/error; economic/political → pending/blocked/forecast/suppressed; diplomacy/alliance → pending/expired/blocked/denied; warfare → pending/blocked/expired/failed; world/notification → empty/pending/expired/suppressed; forms/actions/overlays → initial/validation/loading/success/failure/cancelled.

### 18.7 Matrix E — Accessibility coverage

| Accessibility requirement | Screens | Components | Journeys/flows | Acceptance evidence |
|---|---|---|---|---|
| `REQ-1162` Keyboard operability | All 100 | All interactive | All | `AX-AC-01` |
| `REQ-1163` Overlay focus | Overlay invocations | `OVL-01`…`OVL-08` | All committing flows | `AX-AC-02` |
| `REQ-1164` Transition focus | All 100 | `UI-CMP-004` | All | `AX-AC-03` |
| `REQ-1165` Error association | All forms | `UI-CMP-083`, `UI-CMP-084` | `FLOW-001`, `FLOW-003`, `FLOW-011`, `FLOW-028` | `AX-AC-04` |
| `REQ-1166` State announcements | All 100 | State-bearing | All | `AX-AC-05` |
| `REQ-1167` Table/chart alternatives | Table/chart screens | `UI-CMP-022`, `UI-CMP-030` | `JRN-C`, `JRN-D`, `JRN-J` | `AX-AC-06` |
| `REQ-1168` Reflow/resize | All 100 | All layouts | All | `AX-AC-07` |
| `REQ-1169` Touch/destructive | Task screens | `UI-CMP-085`, `UI-CMP-087` | `JRN-L`, `JRN-M` | `AX-AC-08` |
| `REQ-1170` Motion | All 100 | `UI-CMP-007` | All | `AX-AC-09` |
| `REQ-1171` Evidence boundary | All 100 | All | All | `AX-AC-12` |
| `REQ-1181` Tutorial accessibility | Tutorial screens | All interactive | `JRN-A` | `AX-AC-10` |
| `REQ-1187` Notification announcements | Shell, `SCR-019` | `UI-CMP-008`, `UI-CMP-069` | `JRN-K` | `AX-AC-11` |

### 18.8 Matrix F — Onboarding and tutorial coverage

| Tutorial | Learning objective | Entry | Screens/flows | Requirements |
|---|---|---|---|---|
| `TUT-01` | What Nation Supremacy is and how to enter | `SCR-008`; `SCR-001` excerpt | `SCR-001`, `SCR-008`, `FLOW-004` | `REQ-1175` |
| `TUT-02` | Turn cadence, boundary and "now vs next turn" | `SCR-008`, `SCR-016` | `SCR-016`, `FLOW-005` | `REQ-1175` |
| `TUT-03` | Reading the Command Digest and re-entry | `SCR-008`, `SCR-013` | `SCR-013`, `FLOW-005` | `REQ-1175` |
| `TUT-04` | Treasury and total/reserved/available | `SCR-029` help | `SCR-029`…`SCR-031`, `FLOW-009` | `REQ-1176` |
| `TUT-05` | Political state, approval and stability | `SCR-021` help | `SCR-021`…`SCR-028`, `FLOW-007` | `REQ-1176` |
| `TUT-06` | Production policy and chain management | `SCR-032`/`SCR-044` help | `SCR-032`, `SCR-044`, `FLOW-009` | `REQ-1176` |
| `TUT-07` | City infrastructure and construction | `SCR-041`/`SCR-043` help | `SCR-042`, `SCR-043`, `FLOW-014` | `REQ-1176` |
| `TUT-08` | Directed trade basics | `SCR-035` help | `SCR-035`…`SCR-037`, `FLOW-011` | `REQ-1177` |
| `TUT-09` | Diplomacy and alliance boundaries | `SCR-047`/`SCR-053` help | `SCR-047`…`SCR-058`, `FLOW-017` | `REQ-1177` |
| `TUT-10` | Protection, readiness and owner-only military action | `SCR-059`/`SCR-089` help | `SCR-059`…`SCR-067`, `FLOW-021` | `REQ-1177` |
| `TUT-11` | Objectives and long-term progression | `SCR-071` help | `SCR-071`…`SCR-074`, `FLOW-025` | `REQ-1178` |
| `TUT-12` | Notifications, help, support and reporting | `SCR-019`/`SCR-078` help | `SCR-019`, `SCR-078`, `SCR-087`, `FLOW-027` | `REQ-1178` |

### 18.9 Matrix G — Notification coverage

| Notification scenario | Category | Source | Surfaces | Requirements |
|---|---|---|---|---|
| `NTF-01` Boundary settled | Nation management | TR-088/089 | `SCR-013`, `SCR-019`, `OVL-06` | `REQ-1182` |
| `NTF-02` Turn interrupted/failed | Nation management | TR-075/080 | `SCR-016`, `SCR-019` | `REQ-1182` |
| `NTF-03` Pending act due | Nation management | TR-004 | `SCR-014`, `SCR-019` | `REQ-1184` |
| `NTF-04` Trade offer received/countered/expired | Economy | MKT lifecycle | `SCR-035`, `SCR-037`, `SCR-019` | `REQ-1184` |
| `NTF-05` Trade settled/failed | Economy | MKT-046/047 | `SCR-037`, `SCR-040`, `SCR-019` | `REQ-1184` |
| `NTF-06` Production blocked/`UNMAINTAINED` | Production | ECN-147/147a | `SCR-032`, `SCR-044`, `SCR-019` | `REQ-1185` |
| `NTF-07` Political state change | Politics | DMP-268 | `SCR-021`, `SCR-019` | `REQ-1184` |
| `NTF-08` Election window/result | Politics | DMP-178/184 | `SCR-025`, `SCR-027`, `SCR-019` | `REQ-1184` |
| `NTF-09` Diplomatic proposal/expiry | Diplomacy | DIP-114/116 | `SCR-049`, `SCR-019` | `REQ-1184` |
| `NTF-10` Agreement activation/expiry | Diplomacy | DIP-101/108–113 | `SCR-050`, `SCR-051`, `SCR-019` | `REQ-1184` |
| `NTF-11` Alliance application/tax/treaty | Alliances | ALL-080–086/179–187 | `SCR-054`, `SCR-056`, `SCR-058`, `SCR-019` | `REQ-1185` |
| `NTF-12` War declared/operation/battle | Warfare | WAR catalogue | `SCR-061`, `SCR-063`, `SCR-064`, `SCR-019` | `REQ-1184` |
| `NTF-13` Settlement offered/expired | Warfare | WAR-122/126/127 | `SCR-067`, `SCR-019` | `REQ-1184` |
| `NTF-14` World event announced/active | World events | WEP-099/102/103 | `SCR-069`, `SCR-070`, `SCR-019` | `REQ-1185` |
| `NTF-15` Objective progress/reward | Objectives | WEP-232/582 | `SCR-071`, `SCR-073`, `SCR-019` | `REQ-1185` |
| `NTF-16` Standing published | Rankings | WEP-325/359 | `SCR-072`, `SCR-019` | `REQ-1185` |
| `NTF-17` Security/recovery notice | Account & security | D-041; ACC-031 | `SCR-080`, `SCR-019` | `REQ-1186` |
| `NTF-18` Moderation decision/appeal status | Player protection | MOD-013/017 | `SCR-082`, `SCR-083`, `SCR-019` | `REQ-1186` |

### 18.10 Matrix H — Requirement-to-journey/flow traceability

Every requirement row in §18.2 names its journey and flow columns; the reverse index below confirms bidirectional coverage. Requirement rows whose journey column is `All` are cross-cutting and apply to every journey.

| Journey/flow | Requirement IDs |
|---|---|
| `JRN-A` | `REQ-1090`, `REQ-1103`…`REQ-1106`, `REQ-1172`…`REQ-1181` |
| `JRN-B` | `REQ-1091`, `REQ-1107`, `REQ-1108`, `REQ-1135` |
| `JRN-C` | `REQ-1092`, `REQ-1107` |
| `JRN-D` | `REQ-1093`, `REQ-1111`, `REQ-1112`, `REQ-1196` |
| `JRN-E` | `REQ-1094`, `REQ-1113`…`REQ-1115` |
| `JRN-F` | `REQ-1095`, `REQ-1116`…`REQ-1118` |
| `JRN-G` | `REQ-1096`, `REQ-1109`, `REQ-1110` |
| `JRN-H` | `REQ-1097`, `REQ-1119`…`REQ-1122` |
| `JRN-I` | `REQ-1098`, `REQ-1123`…`REQ-1126` |
| `JRN-J` | `REQ-1099`, `REQ-1127`, `REQ-1128` |
| `JRN-K` | `REQ-1100`, `REQ-1129`…`REQ-1131`, `REQ-1182`…`REQ-1187` |
| `JRN-L` | `REQ-1101`, `REQ-1132`, `REQ-1133` |
| `JRN-M` | `REQ-1102`, `REQ-1134` |
| `FLOW-001`…`FLOW-033` | `REQ-1103`…`REQ-1135` (one row per flow; see §18.2) |
| Cross-cutting (All) | `REQ-1136`…`REQ-1171`, `REQ-1194`…`REQ-1203` |

### 18.11 No-duplication statement

These rows are interaction duties, not restatements of game mechanics. Where a duty derives from an existing rule, the rule is cited as the governing source; the requirement adds only the interaction obligation. No `REQ-870`…`REQ-1089` row is renumbered, reworded or reclassified, and no existing `REQ-001`…`REQ-869` row is duplicated.

---

## 19. Documentation impact register

| Document path | Authority | Inspected | Modification required | Modification performed | Reason | Validation | Notes |
|---|---|---|---|---|---|---|---|
| `docs/AUTONOMOUS_DECISION_POLICY.md` | Canonical | Yes | No | No | D-014 read and applied | Read only | Unchanged |
| `docs/AI_CONTEXT.md` | Canonical status | Yes | Yes | Yes | Prompt 13C status, frontier and next action | 13C validator; `validate_final.py` | Historical snapshots preserved |
| `docs/AI_HANDOFF.md` | Canonical status | Yes | Yes | Yes | Handoff with actual results and next action | 13C validator; `validate_final.py` | Historical entries preserved |
| `docs/PROJECT_PROGRESS.md` | Canonical status | Yes | Yes | Yes | STATUS block remains identical; progress pointer | 13C validator; `validate_final.py` | STATUS blocks must agree |
| `docs/ROADMAP.md` | Canonical | Yes | Yes | Yes | Prompt 13 status and next action | `validate_final.py` | 13D remains unstarted |
| `docs/DECISIONS.md` | Canonical | Yes | Yes | Yes | D-220…D-232 recorded; header updated | 13C validator; register tests | Historical rows untouched |
| `docs/stage-2/00_stage_2_handoff.md` | Canonical status | Yes | Yes | Yes | Current handoff and next action | `validate_final.py` | Historical snapshots preserved |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Canonical | Yes | Yes | Yes | Prompt 13C completion record; Prompt 13D next | `test_next_action.py` | 13D row unchanged in scope |
| `docs/stage-2/02_master_game_design_bible_outline.md` | Canonical | Yes | Yes | Yes | B-13 completed at interaction level; no new Bible part | `validate_final.py` | B-01/B-14/B-15/B-18 remain unwritten |
| `docs/stage-2/03_requirements_traceability.md` | Canonical requirements | Yes | Yes | Yes | Frontier note `REQ-1090`…`REQ-1203`; pointer only, no duplicate rows | 13C validator | `REQ-1204` next free |
| `docs/stage-2/04_approved_and_provisional_decisions.md` | Canonical mirror | Yes | Yes | Yes | DD-268…DD-280 mirrored | 13C validator | Historical rows untouched |
| `docs/stage-2/05_unresolved_design_decisions.md` | Canonical | Yes | No | No | No new UD; owner-reserved rows preserved | Read only | Unchanged |
| `docs/stage-2/06_stage_2_progress_log.md` | Canonical history | Yes | Yes | Yes | New progress-log §92 Prompt 13C entry | 13C validator | §§1–91 preserved |
| `docs/stage-2/21_interface_and_player_journeys.md` | Canonical B-13 | Yes | No | No | Authoritative predecessor; not reopened | Read only | B-13 §29/§31 clarification preserved |
| `docs/stage-2/21_screen_specifications.md` | Canonical B-13 companion | Yes | No | No | Screen bodies authoritative | Read only | Preserved |
| `docs/stage-2/21_component_specifications.md` | Canonical B-13 companion | Yes | No | No | Component bodies authoritative | Read only | Preserved |
| `docs/stage-2/research/13A_*.md` (five files) | Accepted 13A | Yes | No | No | Principles/states/OQ/UR inherited | Read only | Preserved |
| `docs/prompts/INDEX.md` | Canonical index | Yes | Yes | Yes | Added the Prompt 13C archive row and scope-note sentence | `validate_links.py`; 13C validator | 13B archive unchanged |
| `docs/prompts/prompt_13C_interaction_flows_and_player_experience.md` | Historical archive | Created | — | Yes | Verbatim Prompt 13C instruction with the provenance paragraph; stored-bytes SHA-256 recorded in INDEX | Digest computed over stored bytes; link check | New file |
| `docs/qa_backups/13C_validate_interaction_specs.py` | QA tool | Created | — | Yes | Focused 13C validator and self-tests | Executed | New file |
| `docs/qa_backups/13B_validate_ui_specifications.py` | QA tool | Yes | Yes | Yes | Frontier refresh only: D-232/DD-280/13D/REQ-1203 status expectations; no B-13 check weakened | Executed | Documented in §21.2 |
| `docs/qa_backups/13A_validate_ui_foundations.py`, `12A_validate_foundations.py` | QA tools | Yes | Yes | Yes | Frontier/status refresh only; no rule, gate or fixture changed | Executed | Precedent from 13B |
| `docs/qa_backups/validate_final.py`, `test_next_action.py`, `test_decision_registers.py`, `status_rules.py` | QA tools | Yes | Yes | Yes | Current-prompt/frontier refresh only | Executed | Exact commands in §21.2 |
| `docs/stage-2/07_…` … `20_` (B-02…B-12 families) | Canonical rulebooks | Yes (targeted) | No | No | Rule extraction only; no rule change | Read only | Governing authority untouched |
| Pre-existing line-ending-only modifications | Uncertain provenance | Classified only | No | No | Not normalised, restored or discarded | Content-normalised comparison | Preserved |

**Effectiveness note.** Every "Modification required = Yes" row is updated before completion is reported. Historical documents are not rewritten; new dated records are appended. No implementation file is created.

---

## 20. Scope boundaries

### 20.1 What this pass delivered

- The three Prompt 13C documents (this master, the journey companion, the state/feedback companion).
- 13 journeys `JRN-A`…`JRN-M`, 33 flows `FLOW-001`…`FLOW-033`, 12 tutorials `TUT-01`…`TUT-12`.
- 18 interaction states `ST-01`…`ST-18`, validation `VAL-`, confirmation `CFM-`, duplicate `DUP-`, error `ERR-`, recovery `REC-`, accessibility `AXI-`, notification `NTF-`, offline `OFF-` specifications.
- Per-component state mapping for all 90 `UI-CMP` components and 8 overlays (state companion §7).
- Matrices A, B, C, D, E, F, G, H, I.
- `REQ-1090`…`REQ-1203` (114 requirements) and D-220…D-232 / DD-268…DD-280.
- The documentation impact register and the focused 13C validator.

### 20.2 What is explicitly not delivered (13D)

Independent Prompt 13 completeness audit; final cross-system integration acceptance; complete UI-to-backend integration contracts; final Prompt 13 acceptance gates; the final UI acceptance-test suite; final reconciliation and closure report. **13D is NOT STARTED.**

### 20.3 What is explicitly not authorized (14/15 and implementation)

Prompt 14 calibration, Prompt 15 assembly, frontend implementation, backend implementation, database changes, authentication implementation, gameplay implementation, deployment and production security changes are **NOT AUTHORIZED** by this document.

---

## 21. Validation evidence and final handoff

### 21.1 Validator

[`docs/qa_backups/13C_validate_interaction_specs.py`](../qa_backups/13C_validate_interaction_specs.py) performs 27 structural checks plus self-tests: deliverable existence; journey/flow/tutorial/state identifiers; unique IDs; screen/component/requirement/decision references; state-taxonomy coverage; validation/error/accessibility/onboarding/notification/offline/consistency coverage; conditional-feature gates; mapless prohibition; no implementation files; no Prompt 13D deliverable; internal links and section references; requirement/journey/flow traceability. Structural validation is not semantic correctness review.

### 21.2 Actual execution results

| Validator / test | Expected | Actual | Result |
|---|---|---|---|
| `python docs/qa_backups/13C_validate_interaction_specs.py` | 27/27 checks pass | `CHECKS: 27/27 passed; 0 failed; 0 problem(s)` | PASS |
| `python docs/qa_backups/13C_validate_interaction_specs.py --self-test` | All self-tests pass | `SELF-TEST: 18/18 regression cases passed` | PASS |
| `python docs/qa_backups/13B_validate_ui_specifications.py` | 28/28 checks pass after frontier refresh | `CHECKS: 28/28 passed; 0 findings` | PASS |
| `python docs/qa_backups/13B_validate_ui_specifications.py --self-test` | 7/7 self-tests pass | `SELF-TEST: 7/7 cases passed` | PASS |
| `python docs/qa_backups/13A_validate_ui_foundations.py` | 34/34 checks pass after frontier refresh | `CHECKS: 34/34 passed; 0 failed` | PASS |
| `python docs/qa_backups/13A_validate_ui_foundations.py --self-test` | 66/66 self-tests pass | `SELF-TEST: 66/66 regression cases passed` | PASS |
| `python docs/qa_backups/12A_validate_foundations.py` | 45/45 checks pass after frontier refresh | `CHECKS: 45/45 passed; 0 failed` | PASS |
| `python docs/qa_backups/12B_validate_b12.py` | 87/87 checks pass | `CHECKS: 87/87 passed; 0 failed` | PASS |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py` | 24/24 checks pass | `CHECKS: 24/24 passed; 0 failed` | PASS |
| `python docs/qa_backups/validate_links.py` | 0 unresolved links | `Links checked locally: 3803; External links skipped: 382; Anchors checked: 33; Unresolved: 0` | PASS |
| `python docs/qa_backups/validate_final.py` | ALL CHECKS PASSED after current-state refresh | `VALIDATION: ALL CHECKS PASSED` | PASS |
| `python docs/qa_backups/test_next_action.py` | 27 tests pass | `Ran 27 tests … OK` | PASS |
| `python docs/qa_backups/test_decision_registers.py` | 12 tests pass | `Ran 12 tests … OK` | PASS |

The final report records the actual commands, counts and any limitation; no result is claimed before execution.

### 21.3 Acceptance criteria

Result vocabulary: **PASS** (criterion satisfied with cited evidence), **PARTIAL** (partially satisfied with the gap stated), **BLOCKED** (cannot be satisfied for a stated external reason) and **NOT APPLICABLE** (the criterion does not apply, with the reason). No criterion is reported PASS without evidence.

| ID | Criterion | Result | Evidence |
|---|---|---|---|
| 13C-AC-01 | All mandatory predecessor documents inspected | PASS | §2; §19 impact register; progress log §92 |
| 13C-AC-02 | Mandatory governance policy followed | PASS | D-014 applied; D-220…D-232 recorded |
| 13C-AC-03 | Complete player journey specifications exist | PASS | Journey companion §3; 13 journeys |
| 13C-AC-04 | Major existing game-system journeys covered | PASS | Journey companion §3; Matrix A |
| 13C-AC-05 | Detailed interaction sequences exist | PASS | 33 `FLOW-` bodies |
| 13C-AC-06 | Alternative and failure paths documented | PASS | Per-journey E/F; per-flow alternatives/failure |
| 13C-AC-07 | Loading states specified | PASS | State companion §3; `ST-02/03` |
| 13C-AC-08 | Empty states specified | PASS | State companion §4; `ST-05` |
| 13C-AC-09 | Success states specified | PASS | State companion §5; `ST-07` |
| 13C-AC-10 | Failure states specified | PASS | State companion §6; `ST-08`…`ST-17` |
| 13C-AC-11 | Validation rules documented | PASS | State companion §8; `VAL-01`…`VAL-20` |
| 13C-AC-12 | Error handling and recovery documented | PASS | State companion §11; `ERR-01`…`ERR-20`; `REC-01`…`REC-10` |
| 13C-AC-13 | Confirmation and duplicate-submission behaviour documented | PASS | State companion §9–§10; `CFM-`, `DUP-` |
| 13C-AC-14 | Accessibility interaction specifications exist | PASS | §11; state companion §12; `AXI-`, `AX-AC-` |
| 13C-AC-15 | Onboarding and tutorial specifications exist | PASS | §12; journey companion §5; `TUT-01`…`TUT-12` |
| 13C-AC-16 | Notification and feedback specifications exist | PASS | §13; state companion §13; `NTF-01`…`NTF-18` |
| 13C-AC-17 | Offline and reconnection experiences specified | PASS | §14; state companion §14; `OFF-01`…`OFF-12` |
| 13C-AC-18 | Cross-screen behavioural consistency documented | PASS | §15; Matrix I `CON-01`…`CON-24` |
| 13C-AC-19 | Existing game mechanics and restrictions preserved | PASS | Governing citations; no rule change |
| 13C-AC-20 | Conditional feature restrictions preserved | PASS | §1.3, §17.3, `REQ-1144`; no flow for absent screens |
| 13C-AC-21 | Requirements and decisions fully traceable | PASS | §18; D-220…D-232/DD-268…DD-280 |
| 13C-AC-22 | Documentation impact assessment complete | PASS | §19 |
| 13C-AC-23 | Dedicated validator and self-tests have actual results | PASS | §21.2 and §21.6 after execution |
| 13C-AC-24 | Links and references verified | PASS | §21.2 `validate_links.py`; validator checks |
| 13C-AC-25 | Project handoff and roadmap updated accurately | PASS | §21.4; continuity files |
| 13C-AC-26 | No unauthorized implementation or later-phase work occurred | PASS | §1.3, §20; git-status inspection only |

### 21.4 Next action and handoff

**Owner acceptance (2026-11-13).** Prompt 13C is OWNER ACCEPTED (D-233); Prompt 13B is also OWNER ACCEPTED (D-233), and Prompt 13C-C1 is COMPLETE AND INDEPENDENTLY VERIFIED. The next authorized phase after Prompt 13C is **Prompt 13D — integration, acceptance and final reconciliation**, subject to its own authorization and predecessor-status requirements. Prompt 13C does not begin Prompt 13D, and **Prompt 13D is NOT STARTED / NOT AUTHORIZED**. Prompt 14 and Prompt 15 remain unauthorized and unstarted.

### 21.5 Scope confirmation

- No frontend implementation. No backend implementation. No database changes. No SQL migration. No Supabase change. No API implementation. No authentication implementation. No gameplay implementation. No deployment. No production security change.
- No change to any existing game mechanic or formula.
- No Prompt 13D deliverable. No Prompt 14 or 15 work.
- No Git staging, commit, push, reset, revert or discard performed in this pass.

### 21.6 Execution record

Executed on the final 2026-11-13 tree after every edit: `13C_validate_interaction_specs.py` **27/27 checks, 0 problems**; its self-test **18/18**; `13B_validate_ui_specifications.py` **28/28** with **7/7** self-tests; `13A_validate_ui_foundations.py` **34/34** with **66/66** self-tests; `12A_validate_foundations.py` **45/45**; `12B_validate_b12.py` **87/87**; `12C_validate_fair_play_workflows.py` **24/24**; `validate_links.py` **3,803 local links, 382 external, 33 anchors, 0 unresolved**; `validate_final.py` **ALL CHECKS PASSED**; `test_next_action.py` **27 tests OK**; `test_decision_registers.py` **12 tests OK**.

**Validator-frontier refresh (documented).** To keep the existing documentation validators truthful after a legitimate current-state advance, only their current-frontier expectations were refreshed: `13B` checks 13B-17/18 (D-232/DD-280/13D), `13A` checks 13A-25/26 (DD-280/13D/D-232), `12A` status range (D-232), `validate_final` (13D, 280 DD rows, 232 decisions, log row 10), `test_next_action` (13D), `test_decision_registers` (13D) and `status_rules` (`CURRENT_SUBPROMPT=13D`, `13C` completed, `D` sub-prompt suffix). No rule, gate verdict, fixture count, check logic or historical result was weakened or rewritten. The one 13A self-test fixture that simulated a status rollback was retargeted from the now-current 13C to 13D so it still tests detection.

**Limitations.** The validators are deterministic structural/traceability tools, not natural-language reviewers, UI tests or accessibility audits. No runtime UI, keyboard walkthrough, screen-reader pass, contrast measurement, device test or WCAG conformance exists. The 267-test `test_09B_alliance_semantic_validator.py` suite and the 11A validator's known historical check-29 debt were not rerun (no material reason; unrelated to this pass). The pre-existing line-ending-only working-tree differences were not normalised, restored or attributed to this pass.
