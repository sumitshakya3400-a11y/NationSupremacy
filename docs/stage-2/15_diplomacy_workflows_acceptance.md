# B-08 diplomacy — workflows and acceptance

**Version:** 1.4 · **Created:** 2026-10-30 · **Corrected:** 2026-11-01 (08C-C, 08C-D, 08C-E, then the Prompt 09B-J boundary clarification) · **Stage 2, Prompt 08C**
**Status:** **Acceptance specification — design only.** It specifies what a future implementation must do and how that behaviour is to be tested. No diplomacy code, database, endpoint, screen, scheduler or deployment exists (D-012). **No test below has been executed as a runtime test**, and nothing here is release-approved. **v1.1** was the 08C-C correction: 54 edge-case mappings audited, 14 tests added, §14 headings and the DPW-001/002 references fixed, coverage matrix added. **v1.2** was the 08C-D correction: `DPA-087` proves notification privacy, `DPA-088` proves a replayed acceptance, the five requirement rows are reconciled, `DPE-054` is separated into its three scenarios and described accurately as PARTIAL, and the checker expands bare `DPA` ranges. **v1.3** is the 08C-E closure: §15.1.1 states the exhaustive bidirectional methodology, §15.5 is the authoritative 117-pair relationship ledger plus the `REQ-518` deferred row, and the validator now enforces both directions, group counts, duplicate relationships and supporting-vs-direct classification. **v1.4** is the Prompt 09B-J boundary clarification: the historical `D-137` no-object finding is qualified to B-08, the separate B-09 `AT-T01`–`AT-T05` object authorized by `D-140` is distinguished throughout, and no B-08 rule or test changes.
**Authority:** [B-08](15_diplomacy.md) **v1.3** owns the diplomacy rules (v1.3 carries only a 09B-I boundary note; no rule changed from v1.2); [the formula register](15_diplomacy_formula_register.md) **v1.2** owns the arithmetic; [the 08A research report](research/08A_diplomacy_research.md) is evidence, not a rule source. **This document** owns the workflows (`DPW-`), the player journeys, the edge-case catalogue (`DPE-`), the failure/recovery behaviour, the acceptance matrix (`DPA-`) and the evidence register. It adds **no** mechanic of its own; where a workflow and a rule disagree, B-08 wins and this document is corrected.
**Player-authority rule (D-126, DIP-001…DIP-020):** the human player has authority over the diplomatic decisions of their own nation. The game validates, informs, records and enforces authorized decisions; it never makes a discretionary diplomatic decision for a player, never infers consent from silence, and never lets an alliance or an administrator act for a nation.
**Companions:** [B-08](15_diplomacy.md) · [formula register](15_diplomacy_formula_register.md) · [08A research](research/08A_diplomacy_research.md) · [requirements](03_requirements_traceability.md) · [decisions](04_approved_and_provisional_decisions.md) · [unresolved](05_unresolved_design_decisions.md) · [Stage 2 handoff](00_stage_2_handoff.md) · [progress log](06_stage_2_progress_log.md)

---

## 1. Scope and reading order

**1.1 What this document is for.** Prompt 08B decided the diplomacy model: a directional posture, three bilateral agreements (`DP-T01` NAP, `DP-T02` consultation, `DP-T03` crown aid), one coercive act (`DP-A01` embargo), fourteen player actions (`A1`–`A14`), a proposal/agreement lifecycle, declared limits, freeze-aware timing, visibility classes, nine notifications and fifteen failure codes. Prompt 08C must show that the model can be **operated**: who acts, in what order, what the player sees before confirming, what the server validates and persists, which boundary step resolves it, which record is written, which failure is returned and which acceptance test would prove it.

**1.2 What it is not.** It is not a second rulebook and it does not redefine a state, a value, a permission or a limit. It does not implement a screen: a view description is a specification input, not an application. It does not turn a specification-level scenario into a passed test. It does not resolve an owner decision, and it does not design Prompt 09's alliance system or Prompt 10's war rules.

**1.3 Reading order for a new session.** Read [B-08](15_diplomacy.md) first (at least §2–§15, §17–§21), then the [formula register](15_diplomacy_formula_register.md) §1–§4, then this document §2–§4 for the canonical semantics, then the workflow for the task at hand, then the matrix row for every rule being implemented. Use the [08A report](research/08A_diplomacy_research.md) to understand a player-experience risk, never to import a mechanic.

**1.4 Status vocabulary.** **Specified** means the behaviour is written down and traceable; **test-designed** means a scenario exists but has not run; **document-checked** means a consistency or arithmetic check in `qa_backups/` ran and passed; **runtime-tested** and **playtested** mean what they say and are **not claimed anywhere in this document**.

**1.5 Identifier spaces introduced here.** Workflows **`DPW-001`…`DPW-030`**; edge cases **`DPE-001`…`DPE-054`**; acceptance tests **`DPA-001`…`DPA-088`**; evidence dependencies **`DP-RD-01`…`DP-RD-10`**. None of these is a game rule: a `DPW`/`DPE`/`DPA` row is a specification artefact, and every rule it exercises carries its own `DIP-`/`DPF-`/`F-DP-` identifier from B-08.

**1.6 Counts in this document (verified by `qa_backups/verify_diplomacy_workflows.py`).** 30 workflows, 54 edge cases, 88 acceptance tests, 21 traced requirements (`REQ-012`, `REQ-514`…`REQ-533`), 12 traced formulas, 15 failure codes, 9 notifications, 8 player journeys, 6 views, 18 abuse scenarios and 12 answered B-08 handoff questions. `DPA-073`…`DPA-086` came from the 08C-C traceability audit; `DPA-087` and `DPA-088` close the notification-privacy and acceptance-replay gaps found by 08C-D; 08C-E adds no test. §15.5 records **118 requirement/test relationships**: **101 DIRECT**, **16 SUPPORTING** and **1 DEFERRED** (`REQ-518`, Prompt 10). Twenty requirements have direct acceptance coverage; `REQ-518` has none by design. **Two edge cases are PARTIAL**: `DPE-049` (operator correction is Prompt 12's) and `DPE-054` (privileged-read audit is Prompt 12's); all other 52 are covered.

---

## 2. Canonical semantics used by every workflow

### 2.1 Actors and objects

| Term | Meaning | Owner |
|---|---|---|
| **Player** | The authenticated owner of the nation's active account (D-032, DIP-013). The only diplomatic authority. | B-03 |
| **Nation** | The object that holds the posture and the agreements; `active`, dormant, retired (rerolled) or removed. | B-03 |
| **Posture** | A nation's directional, public, declarative attitude: `FRIENDLY`, `NEUTRAL`, `TENSE`, `HOSTILE` (DIP-023). Creates no obligation. | B-08 |
| **Proposal** | A directed object: `PENDING` until accepted, rejected, withdrawn or expired (§5.1). Terms are immutable (DIP-043). | B-08 |
| **Agreement** | A mutual object created in `ACCEPTED` and `ACTIVE` from the boundary; carries versions (DIP-042, DIP-052). | B-08 |
| **Effect** | The named behaviour another system changes (NAP declaration block; notice gate; aid transfer; embargo permission block). Never a treaty field. | B-08 / owner system |
| **Embargo** | A directed coercive act with no consent and no target control (DIP-036, DIP-093…DIP-099). | B-08 |
| **Pair** | Two nations; the B-03 §5.5 restriction check runs at submission, acceptance and P4 (DIP-074). | B-03 |
| **Boundary** | The two-hour UTC turn boundary (B-02 §10, DIP-100). Nothing in diplomacy resolves off a boundary except a player's own submission. | B-02 |
| **Freeze** | `TRANSITION`/`CRISIS`: diplomacy is read-only and specific timers are extended (DIP-022, DIP-105). | B-06 |
| **Dormancy** | Protective, not a penalty: open proposals expire, active agreements persist (DIP-128, D-028). | B-03 |
| **Retirement** | A reroll: every agreement terminates, every embargo lifts, the replacement starts `NEUTRAL` with count 0 (DIP-127). | B-03 |

### 2.2 The three layers are never collapsed

A posture is not an agreement; an agreement is not an effect. Every workflow below names the layer it touches, so a screen can never render "friendly + NAP" as one status. The one posture gate in the game is that an embargo requires the **imposer's** `HOSTILE` posture (DIP-026, DIP-093). Being a treaty party grants the counterparty no authority and no extra read access beyond the matrix in B-08 §13.2 (DIP-080, DIP-111).

### 2.3 The five-step boundary (DIP-101, DIP-103, DIP-130)

Every boundary applies, in this order: **1 `EXPIRY_AND_TERMINATION` → 2 `BREACH` → 3 `ACTIVATION` → 4 `SCHEDULED_OBLIGATION` → 5 `EMBARGO`**; each step re-reads the state the previous step committed. Consequences — the derived breach count, the public record, notifications — are computed after the band from the events actually committed. This document never introduces a second order: every timing workflow and every race case cites one of the five steps by name.

### 2.4 Freeze arithmetic (DIP-105)

| Scope | Function | Timers |
|---|---|---|
| **Pair-scoped** | `frozen_pair(a, t)` — boundaries in `(a, t]` on which **either** party was frozen, each counted once | Proposal expiry, agreement expiry, notice-window **end** |
| **Actor-scoped** | `frozen_turns(n, a, t)` — boundaries in `(a, t]` on which **nation n** was frozen | Posture cooldown, notice cooldown, breach cooldown, embargo re-imposition cooldown |
| **Never extended** | — | The embargo's 24-turn term; the 12-turn notice minimum; the renewal's "strictly before expiry" test; dormancy |

A cooldown is therefore a count of **unfrozen** boundaries, and a frozen player never loses a deadline. This document states every eligible turn the interface must show (§12).

### 2.5 What is automatic, and what is never automatic (DIP-020)

| Automatic — an already-authorized outcome | Never automatic — a discretionary decision |
|---|---|
| Activation of a proposal both players accepted (step 3) | Accepting or rejecting a proposal |
| Expiry of a proposal or agreement at its agreed deadline (step 1) | Deciding that a nation should accept, renew or terminate |
| Aid delivery under an accepted agreement (step 4) | Declaring an embargo, a posture change or a break |
| Embargo term expiry (step 5) | Lifting an embargo, punishing a breach or renewing silently |
| Reroll/dormancy/political-freeze cleanup (DIP-127…DIP-129) | Choosing a counterparty, a term or a response |

**Every workflow below that ends in an automatic step states what was originally authorized, who authorized it and over what scope.** A workflow that cannot answer those three questions is not specified and fails review.

### 2.6 The six consent questions (DIP-059…DIP-062, DIP-081)

Before any bilateral action is finalized the player sees: **(1)** the counterparty; **(2)** the type and version; **(3)** every term; **(4)** the activation boundary; **(5)** the expiry or completion condition; **(6)** the cost or reservation, the public/private status now and after activation, and the breach consequence with its 36-turn cooldown. A confirmation that preselects acceptance, hides a term, counts down to an automatic decision or offers "accept all" is a specification defect (DIP-082).

### 2.7 Failure semantics (DIP-122, DIP-133)

A failed action changes nothing except the failure line written to its actor: no event, no notification, no reservation, no cooldown consumed. A failed action **never** counts as a rejection by the counterparty and **never** counts as consent. Every failure returns one `DPF-` code (or a B-02 `F` code where the cause is the turn engine) with a sentence in the player's terms and the next eligible turn where one exists (DIP-083).

---

## 3. Workflow catalogue

**3.1 How to read a workflow.** Each workflow carries the same 23 fields, numbered as in the Prompt 08C brief. `Steps` are player-facing; `System` is what the server does; `Failure` names the codes; `Tests` names the `DPA-` cases that would prove the workflow. `Automatic processing` states the authorization that permits it, or "none — player decision".

### DPW-001 — Open the diplomatic overview

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-001` — Open the diplomatic overview |
| 2 | **Purpose** | Give the player one place to see their nation's diplomatic state and every decision waiting on them |
| 3 | **Initiating actor** | Any authenticated user with a nation (`A13` read action; DIP-080) |
| 4 | **Permissions** | Read own nation: owner; read public fields: any authenticated user (B-08 §13.2) |
| 5 | **Preconditions** | An active nation exists; the account is not in a state that hides the nation |
| 6 | **Inputs** | None (a read) |
| 7 | **Validation** | None; a read never changes state and is never rate-limited into failure |
| 8 | **Player-visible information** | Own posture toward each nation; each counterparty's posture; active agreements with expiry; incoming proposals awaiting a decision; outgoing proposals with deadline; upcoming deadlines; running cooldowns with eligible turns; active embargoes in both directions; breach count if any; recent class-P events |
| 9 | **Decision points** | Which item to open; nothing is decided on this screen |
| 10 | **Consent requirements** | None |
| 11 | **System processing** | Reads the committed state; never recomputes an outcome, never shows a projection as a fact |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | None; the overview shows the record, it does not re-notify |
| 15 | **Audit/history** | Ordinary read; not a privileged audit read (DIP-121) |
| 16 | **Failure** | None; an empty state is data, not an error (§12.5) |
| 17 | **Cancellation/withdrawal** | Not applicable |
| 18 | **Recovery** | If a sub-object was withdrawn or expired between render and open, the detail view shows its terminal state, not a stale promise |
| 19 | **Acceptance criteria** | Every item above is reachable from the overview; a deadline shows its exact turn; a frozen timer shows the extension |
| 20 | **B-08 rules** | DIP-080, DIP-106, DIP-107, DIP-108, DIP-114, D-024 |
| 21 | **Requirements** | REQ-533 |
| 22 | **Formulas** | F-DP-001…F-DP-012 are displayed only as their resulting values (count, eligible turn) |
| 23 | **Tests** | DPA-066, DPA-067 |

### DPW-002 — Read a nation's public diplomatic profile

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-002` — Read a nation's public diplomatic profile |
| 2 | **Purpose** | Let any player see a nation's public diplomatic record without exposing a negotiation |
| 3 | **Initiating actor** | Any authenticated user |
| 4 | **Permissions** | Public fields only; the owner additionally sees its own pending terms |
| 5 | **Preconditions** | The nation exists; a retired nation's page remains readable as history (DIP-030, DIP-120) |
| 6 | **Inputs** | Nation identifier |
| 7 | **Validation** | A retired/dormant nation returns its historical page, not an error (DIP-030, DIP-128) |
| 8 | **Player-visible information** | Public posture directions; active public agreements (type, parties, version, activation, expiry); declarations and published reasons; breach record; **never** pending terms, private notes or rejection reasons (DIP-109, DIP-111) |
| 9 | **Decision points** | None; reading is not consent and not a signal to the counterparty |
| 10 | **Consent requirements** | None |
| 11 | **System processing** | Reads the class-P record; applies the visibility matrix in B-08 §13.2 |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | None; a view generates no notification and cannot be used to pressure a counterparty |
| 15 | **Audit/history** | Ordinary read |
| 16 | **Failure** | None for a public read; a restricted field is absent rather than masked |
| 17 | **Cancellation/withdrawal** | Not applicable |
| 18 | **Recovery** | None required |
| 19 | **Acceptance criteria** | A third party can learn that an agreement exists and never its pending terms; A viewing B cannot see B's agreements with C (§12.2; B-08 §13.2) |
| 20 | **B-08 rules** | DIP-030, DIP-108…DIP-113 |
| 21 | **Requirements** | REQ-514, REQ-528 |
| 22 | **Formulas** | F-DP-010 (breach count display only) |
| 23 | **Tests** | DPA-065, DPA-068, DPA-069 |

### DPW-003 — Change own posture

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-003` — Change own posture (`A1 SET_POSTURE`) |
| 2 | **Purpose** | Publish the player's own attitude toward another nation |
| 3 | **Initiating actor** | The owner of the acting nation |
| 4 | **Permissions** | Own nation only; no counterparty consent; no administrator, alliance or third party may do it (DIP-079) |
| 5 | **Preconditions** | Counterparty exists and is not retired; the actor is not in `TRANSITION`/`CRISIS`; the 12-turn cooldown is clear; if a `DP-T02` is active with that counterparty and the target posture is `HOSTILE`, a valid consultation notice exists (DIP-031, DIP-039a) |
| 6 | **Inputs** | Counterparty identifier; target posture |
| 7 | **Validation** | Ownership from the session; target availability (`DPF-02`); cooldown (`DPF-08`); political freeze (`DPF-07`); notice window (`DPF-09`); a no-op to the same posture is accepted as a no-op, not an error (T15) |
| 8 | **Player-visible information** | Current posture both directions; the exact eligible turn the cooldown permits; that the declaration is public and the counterparty is notified; that leaving `HOSTILE` does not lift an active embargo (DIP-036) |
| 9 | **Decision points** | Whether to change; which posture; whether to send a notice first when required |
| 10 | **Consent requirements** | None — an attitude is the player's own (DIP-023) |
| 11 | **System processing** | Writes `POSTURE_SET` (class I), notifies the counterparty, starts the cooldown clock |
| 12 | **State transitions** | Any `T1`–`T12` in B-08 §4.2; a rejected change writes nothing (DIP-032) |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | Counterparty notified once; no notification on a failed change |
| 15 | **Audit/history** | `POSTURE_SET` public; `POSTURE_COOLDOWN_STARTED` class S (DIP-117, DIP-118) |
| 16 | **Failure** | `DPF-07`, `DPF-08`, `DPF-09`, `DPF-02` |
| 17 | **Cancellation/withdrawal** | Before confirmation, cancelling changes nothing; after submission the declaration is immediate and cannot be undone except by a later change after the cooldown |
| 18 | **Recovery** | A failed change does not consume the cooldown; the player may act at the eligible turn |
| 19 | **Acceptance criteria** | A change at `+11` fails `DPF-08` and at `+12` passes; a counterparty freeze never lengthens the actor's cooldown; a no-op writes no event |
| 20 | **B-08 rules** | DIP-023…DIP-032, DIP-105(b), DIP-039a |
| 21 | **Requirements** | REQ-515, REQ-516 |
| 22 | **Formulas** | F-DP-005, F-DP-006a |
| 23 | **Tests** | DPA-037, DPA-038, DPA-039, DPA-053 |

### DPW-004 — Send a consultation notice

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-004` — Send a consultation notice (`A2 SEND_CONSULT_NOTICE`) |
| 2 | **Purpose** | Satisfy a `DP-T02` promise to warn before escalating to hostility or an embargo |
| 3 | **Initiating actor** | The owner of either party to an active `DP-T02` |
| 4 | **Permissions** | Party only; no counterparty consent required; never an alliance or officer |
| 5 | **Preconditions** | A `DP-T02` with the named counterparty is `ACTIVE`; the actor is not frozen; the notice cooldown is clear |
| 6 | **Inputs** | Counterparty identifier |
| 7 | **Validation** | Active pact; ownership; notice cooldown (`DPF-10`); freeze (`DPF-07`) |
| 8 | **Player-visible information** | The valid window the notice will create (`notice_turn + 12` to `notice_turn + 36 + pair freeze`); that the notice **does not** commit the sender to act and **does not** reveal the intended act; the next notice-eligible turn |
| 9 | **Decision points** | Whether to warn at all; the notice is optional until the player wants a hostile act |
| 10 | **Consent requirements** | None; the notice is the sender's own act under an agreed pact |
| 11 | **System processing** | Records `CONSULT_NOTICE_SENT` (class S), visible to the counterparty only |
| 12 | **State transitions** | None; the notice is an intent record, not a treaty state |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | The counterparty sees the notice; third parties see only a later posture or embargo |
| 15 | **Audit/history** | Class S (DIP-118); not permanent by default |
| 16 | **Failure** | `DPF-10`, `DPF-07`, `DPF-01` (no active pact) |
| 17 | **Cancellation/withdrawal** | Cannot be recalled; a new notice needs the 12-unfrozen-turn cooldown |
| 18 | **Recovery** | A failed notice does not consume the cooldown |
| 19 | **Acceptance criteria** | A `HOSTILE` change or embargo at `notice + 11` fails `DPF-09`; at `notice + 12` it passes; the window's end moves with pair freeze while the minimum does not |
| 20 | **B-08 rules** | DIP-039a, DIP-031, DIP-105(a)(b) |
| 21 | **Requirements** | REQ-519 |
| 22 | **Formulas** | F-DP-006a, F-DP-006b |
| 23 | **Tests** | DPA-040, DPA-041, DPA-054 |

### DPW-005 — Review the pair's diplomatic record

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-005` — Review the pair's diplomatic record |
| 2 | **Purpose** | Let either party see its shared history: what was proposed, agreed, amended, renewed, ended or broken |
| 3 | **Initiating actor** | Either party; a third party sees only the public class |
| 4 | **Permissions** | Parties see terms and private reasons they are entitled to; a third party sees the public record only (DIP-109, DIP-111) |
| 5 | **Preconditions** | The pair has at least one record, or the view shows an empty state |
| 6 | **Inputs** | Counterparty identifier |
| 7 | **Validation** | Access follows visibility, not relationship (DIP-080) |
| 8 | **Player-visible information** | Each event with its turn, type, version and terminal state; the current posture both ways; the breach count of each side; the eligible turns of running cooldowns |
| 9 | **Decision points** | None on the history view; links to the eligible actions |
| 10 | **Consent requirements** | None |
| 11 | **System processing** | Reads class-P and retained class-S events (DIP-117, DIP-118) |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | None |
| 15 | **Audit/history** | Ordinary read; no privileged access (DIP-121) |
| 16 | **Failure** | None; a correction is shown as a new event referencing the original, never as an edit (DIP-119) |
| 17 | **Cancellation/withdrawal** | Not applicable |
| 18 | **Recovery** | A historical rejection or withdrawal that the parties chose to publish through `A14` appears as its own class-P statement (DIP-078) |
| 19 | **Acceptance criteria** | The record names the actor and the rule for every event; no history is rewritten; a third party's view contains no pending terms |
| 20 | **B-08 rules** | DIP-078, DIP-108…DIP-121 |
| 21 | **Requirements** | REQ-521 |
| 22 | **Formulas** | F-DP-010 |
| 23 | **Tests** | DPA-070 |

### DPW-006 — Create and submit an agreement proposal

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-006` — Create and submit an agreement proposal (`A3 PROPOSE_AGREEMENT`) |
| 2 | **Purpose** | Offer another nation a written agreement whose terms are fixed when it is sent |
| 3 | **Initiating actor** | The owner of the proposing nation |
| 4 | **Permissions** | Own nation only; the counterparty's consent comes later; no delegation (DIP-015) |
| 5 | **Preconditions** | Actor and counterparty active (no dormant/retired target, `DPF-02`); actor not frozen; pair not restricted (DIP-074); no live proposal of the same type in the same direction (DIP-044); actor under the outgoing-proposal cap (DIP-045); for `DP-T03`, the payer holds at least `A` available crowns (DIP-040); for `DP-T03` nowhere should an active embargo block the transfer (DIP-095); neither party would exceed the agreement cap on activation (submission warns, acceptance fails closed, DIP-054) |
| 6 | **Inputs** | Counterparty; agreement type; type-specific terms (`DP-T01`/`DP-T02`: term default 360; `DP-T03`: integer amount `A ≥ 1`) |
| 7 | **Validation** | Ownership, target availability, pair, duplicate direction+type, caps, crown availability, freeze, embargo block for aid, self-dealing (`from == to` rejected, DIP-123) |
| 8 | **Player-visible information** | Every term; that the proposal reserves nothing (`DP-T03` reserves only at acceptance, DIP-051); the response window (36 turns + pair freeze, F-DP-004); that the counterparty may reject, ignore or let it expire; the breach consequence of a later break; the exact limits the action consumes |
| 9 | **Decision points** | Whether to propose; to which nation; which type; which amount |
| 10 | **Consent requirements** | None yet; the counterparty's acceptance is required before any obligation exists (DIP-003) |
| 11 | **System processing** | Creates the proposal `PENDING` with `submitted_turn`, `expiry_turn`, immutable terms and an idempotency key; counts it against the cap; notifies the counterparty once |
| 12 | **State transitions** | None → `PENDING` (DIP-042) |
| 13 | **Resource consequences** | None; no reservation is created at submission (DIP-051) |
| 14 | **Notifications** | `N1` to the counterparty at submission; `N2` to both 12 turns before expiry |
| 15 | **Audit/history** | `AGREEMENT_PROPOSED` private; the proposal itself is class S until acceptance (DIP-117, DIP-118) |
| 16 | **Failure** | `DPF-02`, `DPF-03`, `DPF-04`, `DPF-05`, `DPF-06`, `DPF-07`, `DPF-13` |
| 17 | **Cancellation/withdrawal** | The proposer may withdraw while `PENDING` (`A9`, DIP-047) |
| 18 | **Recovery** | After a rejection the player may propose again at any time (rejection creates no cooldown, DIP-049); after a withdrawal the proposal is gone and a new one is a new object |
| 19 | **Acceptance criteria** | A valid proposal is `PENDING` with the correct `expiry_turn`; a fourth outgoing proposal fails `DPF-06`; a duplicate same-direction proposal fails `DPF-04`; a reciprocal proposal is allowed (DIP-044) |
| 20 | **B-08 rules** | DIP-042…DIP-051, DIP-063, DIP-074, DIP-123 |
| 21 | **Requirements** | REQ-517, REQ-521, REQ-522 |
| 22 | **Formulas** | F-DP-001, F-DP-002, F-DP-004, F-DP-011 |
| 23 | **Tests** | DPA-002…DPA-004, DPA-013…DPA-016, DPA-018, DPA-021, DPA-026, DPA-028, DPA-046, DPA-063, DPA-073 |

### DPW-007 — View and decide an incoming proposal

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-007` — View and decide an incoming proposal |
| 2 | **Purpose** | Show the named counterparty exactly what it is being asked to accept, and nothing more |
| 3 | **Initiating actor** | The named counterparty's owner |
| 4 | **Permissions** | Named counterparty only; the terms are parties-only (DIP-108) |
| 5 | **Preconditions** | The proposal is `PENDING`, addressed to the viewer's nation, and not past its deadline |
| 6 | **Inputs** | Proposal identifier (from the overview or the `N1` notification) |
| 7 | **Validation** | Ownership; the proposal is addressed to the viewer; the version shown equals the version proposed (terms are immutable, DIP-043) |
| 8 | **Player-visible information** | Proposer; type and version; every term; submission and expiry turn; what activating would do; what declining does; that **viewing is not accepting and not silence-consent** (DIP-062); the available actions |
| 9 | **Decision points** | Accept (`DPW-008`), reject (`DPW-009`), do nothing and let it expire (`DPW-011`), or act on a different proposal |
| 10 | **Consent requirements** | The counterparty's own explicit acceptance; silence is never consent (DIP-003, DIP-062) |
| 11 | **System processing** | Read only; no state change, no notification to the proposer merely for viewing |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | For `DP-T03`, the view states the payer's reservation at acceptance and the delivery boundary |
| 14 | **Notifications** | None on view; the decision triggers `N3`/`N4` |
| 15 | **Audit/history** | Ordinary read; a view is not an event |
| 16 | **Failure** | `DPF-01` if the proposal already reached a terminal state; `DPF-03` if the viewer is not the owner |
| 17 | **Cancellation/withdrawal** | Closing the view decides nothing |
| 18 | **Recovery** | A view that races an expiry shows the terminal state and no accept button |
| 19 | **Acceptance criteria** | Viewing a proposal alone changes nothing and notifies no one; the expiry turn is shown; a stale tab cannot accept after expiry (§8.4) |
| 20 | **B-08 rules** | DIP-043, DIP-046, DIP-059, DIP-062, DIP-108 |
| 21 | **Requirements** | REQ-521, REQ-523 |
| 22 | **Formulas** | F-DP-004 |
| 23 | **Tests** | DPA-016, DPA-019 |

### DPW-008 — Accept a proposal

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-008` — Accept a proposal (`A7 ACCEPT_PROPOSAL`) |
| 2 | **Purpose** | Give the counterparty's explicit consent to the exact terms shown |
| 3 | **Initiating actor** | The named counterparty's owner |
| 4 | **Permissions** | Named counterparty only; no authorized third party exists in B-08 (DIP-015) |
| 5 | **Preconditions** | Proposal `PENDING` and unexpired; viewer is the addressee; pair still clear; neither party in freeze; neither party at the agreement cap; for `DP-T03`, the payer can still reserve `A` available crowns (DIP-040) |
| 6 | **Inputs** | Proposal identifier; explicit confirmation |
| 7 | **Validation** | Submission check, then **re-validation at P2** of the next boundary: ownership, pair, caps, duplicate, expiry, freeze, reservation, agreement state (DIP-048, DIP-101, DIP-125) |
| 8 | **Player-visible information** | The full terms again at confirmation; the activation boundary; the expiry; for `DP-T03` the amount to be reserved and the delivery boundary; that acceptance is a decision and activation is the effect (DIP-048) |
| 9 | **Decision points** | Accept or not; accepting one of two reciprocal proposals is a real choice (DPW-012) |
| 10 | **Consent requirements** | The accepting player's own; the proposer's consent was given at submission but a **material change** would require fresh consent (DIP-063) |
| 11 | **System processing** | Records the acceptance; at P2 re-validates; creates the agreement in `ACCEPTED`; for `DP-T03` reserves the crowns; at P4 step 3 the agreement becomes `ACTIVE` |
| 12 | **State transitions** | `PENDING` → `ACCEPTED`; then `ACCEPTED` → `ACTIVE` at step 3 |
| 13 | **Resource consequences** | `DP-T01`/`DP-T02`: none. `DP-T03`: `A` crowns reserved from available balance at acceptance (F-DP-011) |
| 14 | **Notifications** | `N3` to the proposer at acceptance; `N6` to both at activation (P6) |
| 15 | **Audit/history** | `AGREEMENT_ACCEPTED` private; `AGREEMENT_ACTIVATED` public at P6 (DIP-108) |
| 16 | **Failure** | `DPF-01` (already terminal), `DPF-04` (reciprocal winner exists), `DPF-05`, `DPF-07`, `DPF-11`, `DPF-12` (for renewal), `DPF-13` |
| 17 | **Cancellation/withdrawal** | Acceptance cannot be undone unilaterally; after activation only mutual `TERMINATE` or a `BREAK` |
| 18 | **Recovery** | A P2 failure leaves the proposal `PENDING` until its deadline and moves nothing; a transient turn failure retries only where B-08 says so (DIP-129) |
| 19 | **Acceptance criteria** | A valid acceptance creates the agreement in `ACCEPTED` and reserves aid exactly once; a duplicate click returns the recorded outcome and does not reserve twice (DIP-132); an acceptance at the expiry boundary fails as expired |
| 20 | **B-08 rules** | DIP-048, DIP-050, DIP-059, DIP-101, DIP-125, DIP-132 |
| 21 | **Requirements** | REQ-520, REQ-521, REQ-523 |
| 22 | **Formulas** | F-DP-003, F-DP-004, F-DP-011 |
| 23 | **Tests** | DPA-020, DPA-021, DPA-045, DPA-046 |

### DPW-009 — Reject a proposal

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-009` — Reject a proposal (`A8 REJECT_PROPOSAL`) |
| 2 | **Purpose** | Decline a proposal freely and finally, with no penalty and no explanation demanded |
| 3 | **Initiating actor** | The named counterparty's owner |
| 4 | **Permissions** | Named counterparty only |
| 5 | **Preconditions** | Proposal `PENDING`; actor is the addressee |
| 6 | **Inputs** | Proposal identifier; optional private reason (not stored unless published through `A14`) |
| 7 | **Validation** | Ownership; proposal state and version |
| 8 | **Player-visible information** | That the rejection is private by default, immediate, final for that proposal, creates no cooldown and costs nothing; that the proposer may propose again |
| 9 | **Decision points** | Reject, or ignore and let it expire (both are free) |
| 10 | **Consent requirements** | The rejecting player's own; the system never rejects on a player's behalf before the deadline (DIP-019) |
| 11 | **System processing** | Writes `REJECTED` with `responded_turn`; releases the proposer's open-proposal slot |
| 12 | **State transitions** | `PENDING` → `REJECTED` (terminal) |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N4` to the proposer without a reason unless the rejecter publishes one (DIP-078) |
| 15 | **Audit/history** | `PROPOSAL_REJECTED` class S, private (DIP-118) |
| 16 | **Failure** | `DPF-01`, `DPF-03` |
| 17 | **Cancellation/withdrawal** | A rejection cannot be undone; the proposer may submit a new proposal |
| 18 | **Recovery** | None needed |
| 19 | **Acceptance criteria** | The proposal is `REJECTED`; no agreement exists; no cooldown; the proposer's cap is released; the reason stays private unless published |
| 20 | **B-08 rules** | DIP-049, DIP-078 |
| 21 | **Requirements** | REQ-521 |
| 22 | **Formulas** | F-DP-001 |
| 23 | **Tests** | DPA-017, DPA-022 |

### DPW-010 — Withdraw a proposal

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-010` — Withdraw a proposal (`A9 WITHDRAW_PROPOSAL`) |
| 2 | **Purpose** | Let the proposer take back its own offer before anyone accepts it |
| 3 | **Initiating actor** | The proposer |
| 4 | **Permissions** | Proposer only; the counterparty cannot block it |
| 5 | **Preconditions** | Proposal `PENDING`; no acceptance recorded |
| 6 | **Inputs** | Proposal identifier; optional private reason |
| 7 | **Validation** | Ownership; proposal state; if an acceptance was recorded first, the withdrawal fails (DIP-130) |
| 8 | **Player-visible information** | That withdrawal is free, immediate and private; it cannot be undone; the counterparty receives no reason unless the proposer publishes one |
| 9 | **Decision points** | Withdraw or wait |
| 10 | **Consent requirements** | none needed while `PENDING` |
| 11 | **System processing** | Writes `WITHDRAWN`; releases the proposer's open-proposal slot |
| 12 | **State transitions** | `PENDING` → `WITHDRAWN` (terminal) |
| 13 | **Resource consequences** | None; nothing was reserved |
| 14 | **Notifications** | `N5` to the counterparty |
| 15 | **Audit/history** | `PROPOSAL_WITHDRAWN` class S, private |
| 16 | **Failure** | `DPF-01` (already accepted or terminal), `DPF-03` |
| 17 | **Cancellation/withdrawal** | The withdrawal itself is final; a new proposal is a new object |
| 18 | **Recovery** | A race with an acceptance resolves first-recorded-wins (DIP-130) |
| 19 | **Acceptance criteria** | After acceptance, withdrawal fails and only mutual termination or break can end the agreement; before acceptance, the withdrawal leaves no obligation and no cooldown |
| 20 | **B-08 rules** | DIP-047, DIP-130 |
| 21 | **Requirements** | REQ-521 |
| 22 | **Formulas** | F-DP-001 |
| 23 | **Tests** | DPA-023, DPA-024 |
### DPW-011 — Proposal expiry

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-011` — Proposal expiry |
| 2 | **Purpose** | End an unanswered proposal at its agreed deadline without pretending the counterparty rejected it |
| 3 | **Initiating actor** | None; the boundary engine |
| 4 | **Permissions** | System processing only; no player action |
| 5 | **Preconditions** | The proposal is `PENDING` and `current_turn ≥ expiry_turn` |
| 6 | **Inputs** | Proposal record; pair freeze history |
| 7 | **Validation** | Expiry is re-computed from `submitted_turn + 36 + frozen_pair` (F-DP-004); a freeze suspends it (DIP-022) |
| 8 | **Player-visible information** | `N2` 12 turns before; the expiry notice at the boundary; that expiry is **not** a rejection and creates no cooldown |
| 9 | **Decision points** | The players could have accepted, rejected or withdrawn earlier; at expiry there is no decision left |
| 10 | **Consent requirements** | None; the deadline was part of the proposer's own submission |
| 11 | **System processing** | At P4 step 1 (`EXPIRY_AND_TERMINATION`) sets `EXPIRED`, notifies both once, releases the proposer's slot; idempotent |
| 12 | **State transitions** | `PENDING` → `EXPIRED` (terminal) |
| 13 | **Resource consequences** | None; no reservation existed |
| 14 | **Notifications** | `N2` before; one expiry notice to both at the boundary (DIP-114) |
| 15 | **Audit/history** | `PROPOSAL_EXPIRED` class S; retained under D-026's summarised class (DIP-118) |
| 16 | **Failure** | None for expiry itself; a duplicate job run returns the recorded outcome (DIP-102) |
| 17 | **Cancellation/withdrawal** | Expiry cannot be undone; a new proposal is a new object |
| 18 | **Recovery** | An acceptance recorded before expiry but validated at the expiry boundary fails `DPF-01`, because step 1 runs before step 3 (DIP-103) |
| 19 | **Acceptance criteria** | No freeze: expiry at `+36`. Actor freeze: extended. Both parties frozen on one boundary: `+1` only, never `+2`. At the exact expiry turn the proposal is `EXPIRED` |
| 20 | **B-08 rules** | DIP-021, DIP-046, DIP-105(a), DIP-130 |
| 21 | **Requirements** | REQ-522, REQ-532 |
| 22 | **Formulas** | F-DP-004 |
| 23 | **Tests** | DPA-025, DPA-041, DPA-042 |

### DPW-012 — Reciprocal proposals

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-012` — Reciprocal proposals |
| 2 | **Purpose** | Resolve two nations proposing the same type to each other without creating two agreements |
| 3 | **Initiating actor** | Either or both owners |
| 4 | **Permissions** | Each owner acts only for its own nation |
| 5 | **Preconditions** | A→B and B→A proposals of the same type are both `PENDING` |
| 6 | **Inputs** | Two proposal identifiers |
| 7 | **Validation** | Each is a separate **ordered** key (DIP-044, DIP-124); only one **unordered** agreement may exist (DIP-052) |
| 8 | **Player-visible information** | Both proposals are live and either may be accepted; the first acceptance wins and the other fails `DPF-04` with the reciprocal reason; no term is inherited from the loser |
| 9 | **Decision points** | Which proposal (if any) to accept |
| 10 | **Consent requirements** | Both parties for whichever proposal activates; the losing proposal never activates |
| 11 | **System processing** | At P2 the first accepted proposal creates the agreement in `ACCEPTED`; the other fails `DPF-04` and is recorded `EXPIRED` with reason “a reciprocal agreement activated”; at P4 the winner activates |
| 12 | **State transitions** | Winner `PENDING` → `ACCEPTED` → `ACTIVE`; loser `PENDING` → `EXPIRED` |
| 13 | **Resource consequences** | For `DP-T03`, only the winner's amount is reserved; a loser's acceptance never reserves |
| 14 | **Notifications** | `N3` to the winner's proposer; the loser's player is told which agreement superseded it |
| 15 | **Audit/history** | Both records exist; only one agreement event sequence |
| 16 | **Failure** | `DPF-04`, `DPF-01` |
| 17 | **Cancellation/withdrawal** | Either proposer may withdraw before acceptance; withdrawing the winner after acceptance needs termination or break |
| 18 | **Recovery** | A loser may propose again only after the winner is terminal |
| 19 | **Acceptance criteria** | Both `PENDING` proposals coexist; the first accepted at a boundary wins; the second fails and no duplicate agreement exists |
| 20 | **B-08 rules** | DIP-044, DIP-050, DIP-124, DIP-134(1)(2) |
| 21 | **Requirements** | REQ-522 |
| 22 | **Formulas** | F-DP-002, F-DP-003 |
| 23 | **Tests** | DPA-018, DPA-026 |

### DPW-013 — A submission is refused

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-013` — A submission is refused (permission, eligibility, duplicate, cap or freeze) |
| 2 | **Purpose** | Tell the player exactly why an action cannot proceed, without partial state or a misleading success |
| 3 | **Initiating actor** | The player attempting the action |
| 4 | **Permissions** | Depends on the action; a refusal never grants authority |
| 5 | **Preconditions** | A submitted or attempted action fails at submission or at P2 |
| 6 | **Inputs** | The attempted action and its payload |
| 7 | **Validation** | Authority from session; pair; caps; duplicate; expiry; posture/notice; reservation; freeze; idempotency key |
| 8 | **Player-visible information** | One sentence naming the cause and the next eligible turn where one exists (DIP-083); no counterparty private state |
| 9 | **Decision points** | Correct the input, wait for the eligible turn, choose another counterparty, or abandon |
| 10 | **Consent requirements** | None; a refusal is not a decision by the counterparty |
| 11 | **System processing** | Writes only the failure line to the actor; no event, no notification, no reservation, no cooldown consumed (DIP-122) |
| 12 | **State transitions** | None; the object keeps its previous state |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | None to the counterparty; the failure line goes to the actor only (DIP-133) |
| 15 | **Audit/history** | Failure line; not a class-P event |
| 16 | **Failure** | `DPF-01`…`DPF-15`; B-02 `F1`/`F2`/`F3`/`F8`/`F9` where the cause belongs to the turn engine |
| 17 | **Cancellation/withdrawal** | Not applicable; a refused submission does not exist |
| 18 | **Recovery** | The player may resubmit with the same idempotency key after a transient `F8`, or with a corrected payload under a **new** key after `F9` |
| 19 | **Acceptance criteria** | Each code maps to one stable sentence; a failed action changes nothing; a rejected action is never recorded as a rejection by the counterparty |
| 20 | **B-08 rules** | DIP-083, DIP-122, DIP-125, DIP-133 |
| 21 | **Requirements** | REQ-523, REQ-531 |
| 22 | **Formulas** | All limit formulas report the value the refusal cites |
| 23 | **Tests** | DPA-005…DPA-012, DPA-061, DPA-079 |

### DPW-014 — Propose an amendment

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-014` — Propose an amendment (`A4 PROPOSE_AMENDMENT`) |
| 2 | **Purpose** | Change an active agreement's terms through a new, explicitly consented version |
| 3 | **Initiating actor** | Either party's owner |
| 4 | **Permissions** | Party only |
| 5 | **Preconditions** | The agreement is `ACTIVE`; no live `AMEND` for it; the proposed type is unchanged; the new expiry is valid; the actor is not frozen |
| 6 | **Inputs** | Agreement identifier; full proposed terms; the version it would create |
| 7 | **Validation** | Party membership; agreement state; type unchanged (`DPF-13`, DIP-065); material-term completeness (DIP-063); one live amendment |
| 8 | **Player-visible information** | Old terms beside new terms; that the **old terms remain fully in force** until the amendment activates (DIP-064); that the counterparty must accept again; the response window; that no grace period exists |
| 9 | **Decision points** | Propose, withdraw, or leave the agreement unchanged |
| 10 | **Consent requirements** | Both parties for the new version; the proposer's submission is not the counterparty's consent |
| 11 | **System processing** | Creates an `AMEND` proposal referencing the agreement and target version; the agreement keeps its current version and term |
| 12 | **State transitions** | None until activation; on activation `version + 1` and the prior version `SUPERSEDED` (F-DP-012) |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N1` to the counterparty; `N3` on acceptance; `N6` on activation |
| 15 | **Audit/history** | `AGREEMENT_AMENDED` public at activation; prior version retained (DIP-117) |
| 16 | **Failure** | `DPF-01`, `DPF-03`, `DPF-04`, `DPF-07`, `DPF-13` |
| 17 | **Cancellation/withdrawal** | Withdrawable while `PENDING`; after acceptance it cannot be undone unilaterally |
| 18 | **Recovery** | A rejected or expired amendment changes nothing; a new amendment is a new object |
| 19 | **Acceptance criteria** | A type change disguised as an amendment fails `DPF-13`; between proposal and activation the old notice window/term remains in force; activation increments the version exactly once |
| 20 | **B-08 rules** | DIP-063…DIP-066, DIP-053 |
| 21 | **Requirements** | REQ-524 |
| 22 | **Formulas** | F-DP-012 |
| 23 | **Tests** | DPA-027, DPA-028, DPA-029 |

### DPW-015 — Propose a renewal

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-015` — Propose a renewal (`A5 PROPOSE_RENEWAL`) |
| 2 | **Purpose** | Extend an agreement's expiry prospectively, with fresh consent |
| 3 | **Initiating actor** | Either party's owner |
| 4 | **Permissions** | Party only |
| 5 | **Preconditions** | The agreement is `ACTIVE` and not yet expired; no live `RENEW`; the actor is not frozen |
| 6 | **Inputs** | Agreement identifier |
| 7 | **Validation** | Party; state; expiry strictly in the future at activation (DIP-058, F-DP-009); one live renewal |
| 8 | **Player-visible information** | The new expiry `old_expiry + 360`; that the renewal must activate **strictly before** the old expiry; that there is no automatic renewal and no negative-option consent |
| 9 | **Decision points** | Renew, amend the term instead, or let it expire |
| 10 | **Consent requirements** | Both parties |
| 11 | **System processing** | Creates a `RENEW` proposal; on activation sets the expiry forward by one term and keeps the version |
| 12 | **State transitions** | Agreement stays `ACTIVE`; expiry moves |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N1`, `N3`, `N7` (expiring soon), `N6` on renewal |
| 15 | **Audit/history** | `AGREEMENT_RENEWED` public |
| 16 | **Failure** | `DPF-01`, `DPF-04`, `DPF-07`, `DPF-12` |
| 17 | **Cancellation/withdrawal** | Withdrawable while `PENDING` |
| 18 | **Recovery** | A renewal that activates at or after expiry is void (`DPF-12`); a new agreement is required |
| 19 | **Acceptance criteria** | Renewal at `expiry − 1` succeeds and moves expiry by 360; at `expiry` it fails; no renewal is inferred from silence |
| 20 | **B-08 rules** | DIP-058, DIP-067, DIP-068, DIP-105 exception 3 |
| 21 | **Requirements** | REQ-525 |
| 22 | **Formulas** | F-DP-009 |
| 23 | **Tests** | DPA-030, DPA-031 |

### DPW-016 — Propose a mutual termination

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-016` — Propose a mutual termination (`A6 PROPOSE_TERMINATION`) |
| 2 | **Purpose** | Let both parties end an agreement without a breach record |
| 3 | **Initiating actor** | Either party's owner |
| 4 | **Permissions** | Party only |
| 5 | **Preconditions** | The agreement is `ACTIVE` or `ACCEPTED`; the actor is not frozen |
| 6 | **Inputs** | Agreement identifier; optional private reason |
| 7 | **Validation** | Party; state; no duplicate `TERMINATE`; acceptance by the other party at P2 |
| 8 | **Player-visible information** | The termination boundary; that the effect ends with no breach, no count increase and no cooldown; that an `ACCEPTED` aid releases its reservation (DIP-071); that the fact becomes public while the reason stays private |
| 9 | **Decision points** | Propose or not; the counterparty accepts or rejects |
| 10 | **Consent requirements** | Both parties (DIP-057) |
| 11 | **System processing** | Creates `TERMINATE`; at P4 step 1 sets `TERMINATED`, ends the effect and releases any reservation |
| 12 | **State transitions** | `ACTIVE`/`ACCEPTED` → `TERMINATED` (terminal) |
| 13 | **Resource consequences** | Aid reservation released; no transfer |
| 14 | **Notifications** | `N8` to both |
| 15 | **Audit/history** | `AGREEMENT_TERMINATED` public fact, private reason |
| 16 | **Failure** | `DPF-01`, `DPF-03`, `DPF-04`, `DPF-07` |
| 17 | **Cancellation/withdrawal** | Withdrawable while `PENDING`; withdrawal leaves the agreement active |
| 18 | **Recovery** | An expired termination proposal leaves the agreement to its normal expiry; silence ends nothing |
| 19 | **Acceptance criteria** | Mutual termination records no breach; a termination and a break at the same boundary resolve termination first (step 1 before 2) |
| 20 | **B-08 rules** | DIP-057, DIP-069…DIP-071, DIP-130 |
| 21 | **Requirements** | REQ-526 |
| 22 | **Formulas** | F-DP-003 |
| 23 | **Tests** | DPA-032, DPA-033 |

### DPW-017 — Agreement activation

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-017` — Agreement activation |
| 2 | **Purpose** | Turn a consented agreement into a live effect at the boundary |
| 3 | **Initiating actor** | None; the boundary engine executes both players' decision |
| 4 | **Permissions** | System processing; authorization is the two recorded acceptances |
| 5 | **Preconditions** | Agreement `ACCEPTED`; both acceptances valid; pair clear; caps; no freeze; for aid, reservation intact |
| 6 | **Inputs** | Agreement record; accepted proposal; version terms |
| 7 | **Validation** | P2 re-checks everything; at P4 step 3 activation requires the object still live after steps 1–2 |
| 8 | **Player-visible information** | `N3` at acceptance; `N6` at activation with type, version and expiry; the public record appears at P6 |
| 9 | **Decision points** | None at the boundary; the players decided earlier |
| 10 | **Consent requirements** | Both players, per exact version (DIP-059) |
| 11 | **System processing** | At step 3 sets `ACTIVE`, `activation_turn`, computes expiry (F-DP-009); writes the public record after all five steps succeed |
| 12 | **State transitions** | `ACCEPTED` → `ACTIVE` |
| 13 | **Resource consequences** | None for NAP/consultation; aid reservation already exists and delivers at step 4 |
| 14 | **Notifications** | `N6` to both at P6 |
| 15 | **Audit/history** | `AGREEMENT_ACTIVATED` public, class P |
| 16 | **Failure** | A failure at step 3 leaves the agreement `ACCEPTED`; a transient turn failure retries at the next boundary; no partial public event (DIP-104) |
| 17 | **Cancellation/withdrawal** | A break submitted and resolving at the same boundary wins (step 2 before 3), cancelling activation |
| 18 | **Recovery** | A failed activation does not publish; a retry returns the recorded outcome if the same key was used |
| 19 | **Acceptance criteria** | One activation per agreement; the expiry respects freeze; no duplicate public record; a break at the same boundary prevents activation |
| 20 | **B-08 rules** | DIP-048, DIP-101, DIP-103, DIP-104 |
| 21 | **Requirements** | REQ-521, REQ-533 |
| 22 | **Formulas** | F-DP-009, F-DP-012 |
| 23 | **Tests** | DPA-021, DPA-034 |

### DPW-018 — Amendment activation and version change

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-018` — Amendment activation and version change |
| 2 | **Purpose** | Apply the consented new version exactly once and retain the old one as history |
| 3 | **Initiating actor** | None; boundary engine |
| 4 | **Permissions** | System processing under both acceptances |
| 5 | **Preconditions** | Agreement `ACTIVE`; `AMEND` accepted; no break/termination earlier in the band |
| 6 | **Inputs** | Amendment proposal; agreement; target version |
| 7 | **Validation** | `version' == version + 1` (F-DP-012); type unchanged; terms complete |
| 8 | **Player-visible information** | Version number and the superseded version with its activation/supersession turns; the currently binding term |
| 9 | **Decision points** | None at activation; the parties decided at acceptance |
| 10 | **Consent requirements** | Both parties for the new version |
| 11 | **System processing** | At step 3 applies the new terms, increments the version, labels the old `SUPERSEDED` |
| 12 | **State transitions** | Agreement stays `ACTIVE`; version `n` → `n+1` |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N6` to both |
| 15 | **Audit/history** | `AGREEMENT_AMENDED`; append-only version list |
| 16 | **Failure** | A step-2 break or step-1 termination makes activation fail `DPF-01` |
| 17 | **Cancellation/withdrawal** | Cannot be undone after activation; a further amendment is a new version |
| 18 | **Recovery** | A duplicate activation returns the recorded outcome; a version is never applied twice |
| 19 | **Acceptance criteria** | Exactly one increment; the old terms were in force until this boundary; two amendments racing produce one winner (`DPF-04` for the loser) |
| 20 | **B-08 rules** | DIP-053, DIP-064, DIP-065; F-DP-012 |
| 21 | **Requirements** | REQ-524 |
| 22 | **Formulas** | F-DP-012 |
| 23 | **Tests** | DPA-029, DPA-035 |

### DPW-019 — Renewal activation

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-019` — Renewal activation |
| 2 | **Purpose** | Move the expiry forward only when the renewal activates strictly before the old expiry |
| 3 | **Initiating actor** | None; boundary engine |
| 4 | **Permissions** | System processing under both acceptances |
| 5 | **Preconditions** | Agreement `ACTIVE`; `RENEW` accepted; `current_turn < expiry_turn` at the activation boundary |
| 6 | **Inputs** | Renewal proposal; agreement |
| 7 | **Validation** | Strictly-before test against the **already-extended** expiry (DIP-105 exception 3); no expiry event earlier in the band |
| 8 | **Player-visible information** | The new expiry and the boundary that produced it |
| 9 | **Decision points** | None at activation |
| 10 | **Consent requirements** | Both parties |
| 11 | **System processing** | At step 3 sets `expiry_turn = old_expiry + 360`, keeps version, writes `RENEWED` |
| 12 | **State transitions** | `ACTIVE` unchanged; expiry moves |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N6` to both |
| 15 | **Audit/history** | `AGREEMENT_RENEWED` public |
| 16 | **Failure** | `DPF-12` if expiry ran first at step 1 |
| 17 | **Cancellation/withdrawal** | Cannot be undone after activation |
| 18 | **Recovery** | A renewal that fails because expiry won requires a new agreement |
| 19 | **Acceptance criteria** | Renewal at the expiry boundary fails; renewal one boundary earlier succeeds; no double extension from freeze |
| 20 | **B-08 rules** | DIP-058, DIP-067, DIP-103, DIP-105 |
| 21 | **Requirements** | REQ-525, REQ-533 |
| 22 | **Formulas** | F-DP-009 |
| 23 | **Tests** | DPA-031, DPA-036 |

### DPW-020 — View a treaty's terms, obligations and history

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-020` — View a treaty's terms, obligations and history |
| 2 | **Purpose** | Let a party (and the public, for the public fields) inspect exactly what is binding |
| 3 | **Initiating actor** | A party, or any user for the public fields |
| 4 | **Permissions** | Parties see full terms; the public sees the public record only |
| 5 | **Preconditions** | The agreement exists in any state |
| 6 | **Inputs** | Agreement identifier |
| 7 | **Validation** | Visibility check; no access to the counterparty's treasury or other agreements |
| 8 | **Player-visible information** | Parties; type; current state; version and superseded history; activation; expiry/completion; every obligation; the breach consequence; the terminal event if any; the aid amount (public) but not the payer's treasury detail |
| 9 | **Decision points** | Links to the eligible actions (amend, renew, terminate, break) according to state and role |
| 10 | **Consent requirements** | None to view |
| 11 | **System processing** | Read only |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | Displays reserved crowns for an `ACCEPTED` aid |
| 14 | **Notifications** | None |
| 15 | **Audit/history** | Ordinary read |
| 16 | **Failure** | `DPF-01` only where a detail route requires a live object; a terminal object still displays its record |
| 17 | **Cancellation/withdrawal** | Not applicable |
| 18 | **Recovery** | A version superseded while the page was open shows the new version with its activation turn |
| 19 | **Acceptance criteria** | No hidden obligation: every binding term is visible to both parties; the public record contains no private note |
| 20 | **B-08 rules** | DIP-053, DIP-109, DIP-111 |
| 21 | **Requirements** | REQ-521 |
| 22 | **Formulas** | F-DP-009, F-DP-012 |
| 23 | **Tests** | DPA-070, DPA-036 |
### DPW-021 — Break an agreement

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-021` — Break an agreement (`A10 BREAK_AGREEMENT`) |
| 2 | **Purpose** | Let a player end their own promise visibly and bear the published consequence |
| 3 | **Initiating actor** | Either party's owner |
| 4 | **Permissions** | Party only; unilateral; no counterparty consent and no counterparty veto |
| 5 | **Preconditions** | Agreement `ACTIVE` or `ACCEPTED`; no terminal event yet; actor not frozen |
| 6 | **Inputs** | Agreement identifier; explicit confirmation; optional public reason |
| 7 | **Validation** | Party; state; idempotency key `agreement_id + BREAK`; no duplicate breach (DIP-076) |
| 8 | **Player-visible information** | Before confirmation: the record is **public and permanent**; the effect ends; the breach count rises; a 36-turn same-pair same-type cooldown applies; nothing is confiscated, frozen or auto-retaliated; the counterparty is notified and cannot reject the break |
| 9 | **Decision points** | Break, propose mutual termination instead, or keep the agreement |
| 10 | **Consent requirements** | Only the breaker's own; this is the one unilateral exit (DIP-056) |
| 11 | **System processing** | At P4 step 2 (`BREACH`) sets `BREACHED`, ends the effect, writes the public event, releases any aid reservation, starts the cooldown |
| 12 | **State transitions** | `ACTIVE`/`ACCEPTED` → `BREACHED` (terminal) |
| 13 | **Resource consequences** | An aid reservation is released; no transfer, no fine |
| 14 | **Notifications** | `N8` to both; the public record names the breaker |
| 15 | **Audit/history** | `AGREEMENT_BREACHED` public class P with actor, counterparty, type, version, turn and rule |
| 16 | **Failure** | `DPF-01` (not active/terminal), `DPF-03`, `DPF-07`; `DPF-14` governs the later proposal, not the break |
| 17 | **Cancellation/withdrawal** | Irreversible after submission; no undo |
| 18 | **Recovery** | A step-1 termination at the same boundary wins and the break fails with `DPF-01`; a duplicate returns the recorded outcome |
| 19 | **Acceptance criteria** | One breach event; count +1; cooldown from the break turn; a break at the delivery boundary cancels delivery (step 2 before 4); a break cannot be caused by a voided turn |
| 20 | **B-08 rules** | DIP-018, DIP-056, DIP-072…DIP-077, DIP-131 |
| 21 | **Requirements** | REQ-526, REQ-527 |
| 22 | **Formulas** | F-DP-007, F-DP-010 |
| 23 | **Tests** | DPA-034, DPA-043, DPA-047, DPA-051 |

### DPW-022 — Agreement expiry

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-022` — Agreement expiry |
| 2 | **Purpose** | End a term agreement at its agreed expiry without renewal or reinterpretation |
| 3 | **Initiating actor** | None; boundary engine |
| 4 | **Permissions** | System processing |
| 5 | **Preconditions** | Agreement `ACTIVE`; `current_turn ≥ expiry_turn`; no renewal activated earlier |
| 6 | **Inputs** | Agreement record; freeze history |
| 7 | **Validation** | Expiry computed with `frozen_pair` (F-DP-009); step 1 runs first |
| 8 | **Player-visible information** | `N7` 24 turns before; `N8` at expiry; the effect has ended |
| 9 | **Decision points** | Renew or terminate earlier; at expiry none remains |
| 10 | **Consent requirements** | None; the term was agreed |
| 11 | **System processing** | At step 1 sets `EXPIRED`, ends the effect, publishes |
| 12 | **State transitions** | `ACTIVE` → `EXPIRED` (terminal) |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N7`, `N8` |
| 15 | **Audit/history** | `AGREEMENT_EXPIRED` public |
| 16 | **Failure** | A renewal that loses the race fails `DPF-12`; no resurrection |
| 17 | **Cancellation/withdrawal** | Irreversible |
| 18 | **Recovery** | A new agreement is the only route |
| 19 | **Acceptance criteria** | Expiry at `activation + 360 + pair freeze`; the NAP war block ends; no automatic renewal |
| 20 | **B-08 rules** | DIP-067, DIP-101, DIP-105(a), DIP-130 |
| 21 | **Requirements** | REQ-521, REQ-533 |
| 22 | **Formulas** | F-DP-009 |
| 23 | **Tests** | DPA-030, DPA-036 |

### DPW-023 — Aid delivery and scheduled obligation

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-023` — Aid delivery and scheduled obligation |
| 2 | **Purpose** | Perform the one transfer an accepted aid promised, exactly once |
| 3 | **Initiating actor** | None; boundary engine |
| 4 | **Permissions** | System processing under the recipient's acceptance and the payer's proposal |
| 5 | **Preconditions** | Agreement `ACCEPTED` with `A` reserved; delivery boundary reached; no break/termination earlier in the band |
| 6 | **Inputs** | Agreement; reservation; payer/recipient balances |
| 7 | **Validation** | Reservation intact; pair clear; an aid accepted before an embargo declaration still delivers (grandfathering, DIP-095) |
| 8 | **Player-visible information** | The amount; the delivery turn; on success “paid”; on failure “not paid” with the cause and no accusation |
| 9 | **Decision points** | None at delivery; the players decided at proposal/acceptance |
| 10 | **Consent requirements** | Both parties, already recorded |
| 11 | **System processing** | At step 4 moves the reserved crowns as one B-04 transfer with matched ledger events and one `transfer_id`; sets `COMPLETED` |
| 12 | **State transitions** | `ACCEPTED` → `COMPLETED` (terminal) |
| 13 | **Resource consequences** | Payer `−A`, recipient `+A`, world total unchanged (F-DP-011) |
| 14 | **Notifications** | `N8` to both; the settled amount is public |
| 15 | **Audit/history** | `AID_SETTLED` public class P |
| 16 | **Failure** | A voided turn returns the agreement to `ACCEPTED` and retries (DIP-129); a lost reservation asks the payer to re-confirm within 12 turns, else `TERMINATED` `TRANSFER_VOIDED`, never `BREACHED` |
| 17 | **Cancellation/withdrawal** | A step-2 break cancels delivery; mutual termination at step 1 releases the reservation |
| 18 | **Recovery** | Retry is idempotent by agreement and boundary; no double transfer (DIP-132) |
| 19 | **Acceptance criteria** | Exactly one ledger pair; conservation; no negative balance; a break at the same boundary prevents delivery; a voided turn creates no breach |
| 20 | **B-08 rules** | DIP-040, DIP-095, DIP-129, DIP-131, DIP-132 |
| 21 | **Requirements** | REQ-520, REQ-533 |
| 22 | **Formulas** | F-DP-011 |
| 23 | **Tests** | DPA-045, DPA-046, DPA-048 |

### DPW-024 — Publish a reason

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-024` — Publish a reason (`A14 PUBLISH_REASON`) |
| 2 | **Purpose** | Let a party put its own explanation on the public record without exposing the counterparty's |
| 3 | **Initiating actor** | Either party |
| 4 | **Permissions** | Party only; own reason only |
| 5 | **Preconditions** | The event exists (rejection, withdrawal, termination, breach, embargo) |
| 6 | **Inputs** | Event identifier; free-text statement |
| 7 | **Validation** | Actor is a party to the event; the statement is attributed to the actor; no editing of the original event |
| 8 | **Player-visible information** | Exactly what becomes public and that it is append-only; the counterparty is notified |
| 9 | **Decision points** | Publish or keep private |
| 10 | **Consent requirements** | Only the publisher's own; it cannot publish the counterparty's reason |
| 11 | **System processing** | Appends a `REASON_PUBLISHED` class-P event referencing the original |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | The counterparty is notified |
| 15 | **Audit/history** | Class P; a correction is a new statement, never an edit |
| 16 | **Failure** | `DPF-03` if the actor is not a party; `DPF-01` if the event does not exist |
| 17 | **Cancellation/withdrawal** | Cannot be deleted; a correction is another statement |
| 18 | **Recovery** | None needed |
| 19 | **Acceptance criteria** | The counterparty's private reason is never disclosed; the statement cannot alter the event's facts |
| 20 | **B-08 rules** | DIP-078, DIP-117, DIP-119 |
| 21 | **Requirements** | REQ-521 |
| 22 | **Formulas** | None |
| 23 | **Tests** | DPA-062, DPA-070 |

### DPW-025 — Declare an embargo

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-025` — Declare an embargo (`A11 DECLARE_EMBARGO`) |
| 2 | **Purpose** | Exercise the one coercive act: block new transfers between the pair for a fixed term |
| 3 | **Initiating actor** | The owner of the imposing nation |
| 4 | **Permissions** | Own nation only; no consent; no alliance, officer or administrator |
| 5 | **Preconditions** | Target exists and is not retired/dormant; imposer holds `HOSTILE` posture toward it; imposer not frozen; no active embargo on the same target; re-imposition cooldown clear; if a `DP-T02` is active, a valid notice exists |
| 6 | **Inputs** | Target identifier; optional public reason |
| 7 | **Validation** | DIP-093's five preconditions in order; self-embargo rejected (DIP-123) |
| 8 | **Player-visible information** | Exactly what the embargo blocks (new directed offers/acceptances, new aid agreements/transfers) and what it does **not** block (T01/T02 diplomacy, third-party trade, existing settlements/deliveries); the 24-turn term; the cooldown; that the target cannot lift it |
| 9 | **Decision points** | Declare, change posture first, or abandon |
| 10 | **Consent requirements** | None; a coercive act (DIP-036) |
| 11 | **System processing** | At P4 step 5 creates the embargo `ACTIVE`, publishes the fact, notifies the target |
| 12 | **State transitions** | None → `ACTIVE` |
| 13 | **Resource consequences** | None; moves no value and charges no fee (DIP-096) |
| 14 | **Notifications** | `N9` to both at P6 |
| 15 | **Audit/history** | `EMBARGO_DECLARED` public class P |
| 16 | **Failure** | `DPF-15` (posture), `DPF-08` (cooldown), `DPF-09` (notice), `DPF-02`, `DPF-07` |
| 17 | **Cancellation/withdrawal** | The imposer may lift it early (`A12`); it cannot be withdrawn as a proposal because it is not one |
| 18 | **Recovery** | A failed declaration consumes no cooldown |
| 19 | **Acceptance criteria** | Only `HOSTILE` satisfies the gate; the target's posture is irrelevant; the term is 24 turns and is not freeze-extended; the declaration is public at P6 |
| 20 | **B-08 rules** | DIP-026, DIP-091…DIP-099, DIP-105 exception 1 |
| 21 | **Requirements** | REQ-529, REQ-531 |
| 22 | **Formulas** | F-DP-008 |
| 23 | **Tests** | DPA-052, DPA-053, DPA-055 |

### DPW-026 — Lift an embargo

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-026` — Lift an embargo (`A12 LIFT_EMBARGO`) |
| 2 | **Purpose** | Let the imposer end its own sanction early |
| 3 | **Initiating actor** | The imposer's owner |
| 4 | **Permissions** | Imposer only; the target has no lift route (DIP-098) |
| 5 | **Preconditions** | The embargo is `ACTIVE`; actor is the imposer |
| 6 | **Inputs** | Embargo identifier |
| 7 | **Validation** | Ownership; state |
| 8 | **Player-visible information** | That the lift is public and starts the 12-turn re-imposition cooldown from the lift boundary; that the target is notified |
| 9 | **Decision points** | Lift or continue to term |
| 10 | **Consent requirements** | Imposer's own only |
| 11 | **System processing** | At step 5 sets `LIFTED`, `end_turn = lift_turn`; starts the cooldown |
| 12 | **State transitions** | `ACTIVE` → `LIFTED` (terminal) |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N9` to both |
| 15 | **Audit/history** | `EMBARGO_LIFTED` public |
| 16 | **Failure** | `DPF-01`, `DPF-03` |
| 17 | **Cancellation/withdrawal** | Irreversible; a new embargo needs the cooldown |
| 18 | **Recovery** | None |
| 19 | **Acceptance criteria** | The target cannot lift; the cooldown is measured from the lift, not the declaration |
| 20 | **B-08 rules** | DIP-098, DIP-105(b), F-DP-008 |
| 21 | **Requirements** | REQ-529 |
| 22 | **Formulas** | F-DP-008 |
| 23 | **Tests** | DPA-056 |

### DPW-027 — Embargo term expiry and re-imposition

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-027` — Embargo term expiry and re-imposition |
| 2 | **Purpose** | End the sanction automatically at its term and allow a lawful re-declaration only after the cooldown |
| 3 | **Initiating actor** | Boundary for expiry; imposer for re-imposition |
| 4 | **Permissions** | System for expiry; imposer for the new declaration |
| 5 | **Preconditions** | Expiry: `current_turn ≥ end_turn`. Re-imposition: the full posture/cooldown/notice set and `current_turn ≥ end_turn + 12 + imposer freeze` |
| 6 | **Inputs** | Embargo record; imposer freeze history; new declaration |
| 7 | **Validation** | Expiry is not freeze-extended (DIP-105 exception 1); cooldown is actor-scoped (F-DP-008); same-boundary re-declaration fails |
| 8 | **Player-visible information** | `N9` at expiry; the next eligible declaration turn; why a same-boundary attempt fails |
| 9 | **Decision points** | The imposer decides whether to re-declare after the cooldown; expiry itself is automatic |
| 10 | **Consent requirements** | None |
| 11 | **System processing** | Step 5 sets `EXPIRED`; a later submission is validated against the cooldown |
| 12 | **State transitions** | `ACTIVE` → `EXPIRED`; a new act creates a new `ACTIVE` embargo |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | `N9` at expiry; `N9` on a new declaration |
| 15 | **Audit/history** | `EMBARGO_EXPIRED`; a new `EMBARGO_DECLARED` as a separate object |
| 16 | **Failure** | `DPF-08` for a too-early re-declaration; `DPF-15`/`DPF-09` as applicable |
| 17 | **Cancellation/withdrawal** | Not applicable to expiry |
| 18 | **Recovery** | The player waits for the eligible turn; the interface names it |
| 19 | **Acceptance criteria** | Expiry at exactly `declared + 24` even when either party is frozen; re-imposition at `end + 11` fails and at `end + 12` passes; imposer freeze extends, target freeze does not |
| 20 | **B-08 rules** | DIP-094, DIP-099, DIP-105, F-DP-008 |
| 21 | **Requirements** | REQ-529 |
| 22 | **Formulas** | F-DP-008 |
| 23 | **Tests** | DPA-055, DPA-057 |

### DPW-028 — View a nation's breach record

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-028` — View a nation's breach record |
| 2 | **Purpose** | Show the one derived diplomatic number as a fact, not a score |
| 3 | **Initiating actor** | Any authenticated user |
| 4 | **Permissions** | Public field (DIP-088) |
| 5 | **Preconditions** | The nation exists or is retired |
| 6 | **Inputs** | Nation identifier |
| 7 | **Validation** | Window `t − 4380 < e.turn ≤ t` (F-DP-010); nation-scoped |
| 8 | **Player-visible information** | “N breaches in the last 4,380 turns”; each event with type, counterparty and turn; that it has **no mechanical effect**; that a retired nation's history stays on its page and the replacement starts at 0 |
| 9 | **Decision points** | None; display only |
| 10 | **Consent requirements** | None |
| 11 | **System processing** | Counts `AGREEMENT_BREACHED` events in the window |
| 12 | **State transitions** | None |
| 13 | **Resource consequences** | None |
| 14 | **Notifications** | None |
| 15 | **Audit/history** | Read only |
| 16 | **Failure** | None |
| 17 | **Cancellation/withdrawal** | Not applicable |
| 18 | **Recovery** | None |
| 19 | **Acceptance criteria** | The count excludes a breach exactly at `t − 4380`; includes one at `t`; the retired page keeps its history; the replacement shows 0 |
| 20 | **B-08 rules** | DIP-084…DIP-090, DIP-120 |
| 21 | **Requirements** | REQ-528 |
| 22 | **Formulas** | F-DP-010 |
| 23 | **Tests** | DPA-049, DPA-050, DPA-069 |

### DPW-029 — Political freeze

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-029` — Political freeze (`TRANSITION`/`CRISIS` read-only diplomacy) |
| 2 | **Purpose** | Protect a player who cannot act from losing a deadline or a treaty |
| 3 | **Initiating actor** | None; B-06's political state sets the flag |
| 4 | **Permissions** | The system suspends writes; reads remain available |
| 5 | **Preconditions** | The nation is in `TRANSITION` or `CRISIS` at the boundary |
| 6 | **Inputs** | B-06 state flag with start and end boundaries |
| 7 | **Validation** | A write fails `DPF-07`; a timer extension uses the correct scope (pair vs actor) |
| 8 | **Player-visible information** | “Diplomacy is paused while your government is in transition; your deadlines are extended”; the added turns and resulting eligible turns |
| 9 | **Decision points** | None during the freeze; an incoming proposal can still be read but not accepted |
| 10 | **Consent requirements** | A frozen player cannot consent; the freeze never counts as consent |
| 11 | **System processing** | Blocks player writes; does not expire the frozen party's proposals or agreements; extends pair timers and the actor's own cooldowns |
| 12 | **State transitions** | No treaty state changes from the freeze itself; only deadlines move |
| 13 | **Resource consequences** | An aid delivery due while the payer is frozen waits under DIP-105; no breach |
| 14 | **Notifications** | Deadline shifts are shown in the interface; no punitive notification |
| 15 | **Audit/history** | The political state is B-06's record; diplomacy writes no treaty event for a freeze |
| 16 | **Failure** | `DPF-07` for a write; a freeze never causes `DPF-12` by itself |
| 17 | **Cancellation/withdrawal** | A frozen player cannot withdraw; the freeze extends the deadline instead |
| 18 | **Recovery** | On the boundary the state ends, normal validation resumes with the extended deadlines |
| 19 | **Acceptance criteria** | A proposal does not expire on a frozen boundary; the pair timer counts a shared frozen boundary once; the actor cooldown counts only the actor's own frozen boundaries |
| 20 | **B-08 rules** | DIP-022, DIP-062, DIP-105 |
| 21 | **Requirements** | REQ-532, REQ-533 |
| 22 | **Formulas** | F-DP-004…F-DP-009 |
| 23 | **Tests** | DPA-040, DPA-042, DPA-058 |

### DPW-030 — Account-event cleanup: dormancy and retirement

| # | Field | Definition |
|---|---|---|
| 1 | **ID / name** | `DPW-030` — Account-event cleanup: dormancy and retirement |
| 2 | **Purpose** | Apply B-03's account events to diplomacy without inventing a penalty |
| 3 | **Initiating actor** | None; the account transaction |
| 4 | **Permissions** | System processing under B-03 RRL-019 and D-028 |
| 5 | **Preconditions** | A nation becomes dormant, or a reroll retires it |
| 6 | **Inputs** | Nation identifier; account event; open proposals, agreements, embargoes, reservations |
| 7 | **Validation** | Dormancy: open proposals expire, agreements persist, embargoes persist, new proposals/embargoes targeting it fail `DPF-02`. Retirement: every proposal withdrawn, every agreement terminated, every reservation released, every embargo lifted, replacement neutral with count 0 |
| 8 | **Player-visible information** | Counterparties are told the objective reason (`COUNTERPARTY_DORMANT`, `NATION_RETIRED`); no accusation, no breach |
| 9 | **Decision points** | None for the counterparty; the dormant player cannot act |
| 10 | **Consent requirements** | None; cleanup implements an account rule, not a diplomatic decision |
| 11 | **System processing** | Writes the cleanup events with reason codes; releases reservations once; records a class-P event attributed to the old nation on retirement |
| 12 | **State transitions** | Proposals → `EXPIRED`/`WITHDRAWN`; agreements → `TERMINATED`; embargoes → `LIFTED` |
| 13 | **Resource consequences** | Reservations released; no transfer; no confiscation |
| 14 | **Notifications** | One notification per affected counterparty |
| 15 | **Audit/history** | Class-P termination/lift events; the retired nation keeps its page and count |
| 16 | **Failure** | Idempotent by account event; a retry does not double-terminate or double-release |
| 17 | **Cancellation/withdrawal** | Cannot be undone; a replacement starts fresh |
| 18 | **Recovery** | A late boundary does not resurrect a terminated agreement (DIP-126) |
| 19 | **Acceptance criteria** | Dormancy creates no breach and keeps agreement effects; retirement terminates all, lifts embargoes and starts the replacement at 0; no reservation survives |
| 20 | **B-08 rules** | DIP-120, DIP-126, DIP-127, DIP-128 |
| 21 | **Requirements** | REQ-531, REQ-533 |
| 22 | **Formulas** | F-DP-010 |
| 23 | **Tests** | DPA-059, DPA-060 |
---

## 4. Player journeys

**4.1 How to read a journey.** A journey is the player-facing sequence behind a workflow. It names what the player sees, what they may choose, the exact confirmation, the server's answer and why the player's authority is preserved. Turn numbers are illustrative test assumptions, not balance claims. These journeys add no rule; they sequence the rules in §3 and B-08 §20.

### J1 — Propose, wait and receive a rejection (`DPW-006`, `DPW-007`, `DPW-009`)

1. **Open diplomacy.** The overview lists Arcadia's active agreements, one incoming proposal and a running posture cooldown with its eligible turn.
2. **Choose "Propose agreement".** The recipient picker excludes Arcadia itself, retired nations and any nation already holding a live proposal of the chosen type from Arcadia; a dormant nation is shown as unavailable rather than silently omitted.
3. **Choose `DP-T01`.** The form states the default term (360 turns, provisional), that the agreement blocks a war declaration between the parties, and that it costs nothing.
4. **Review.** The confirmation shows: recipient Bravia; type and version 1; no cost; activation at the first boundary after acceptance; expiry 360 turns later; the breach consequence (public record, count +1, 36-turn same-type cooldown); that Arcadia may withdraw until Bravia accepts.
5. **Confirm.** The server re-validates ownership, target availability, pair, duplicate, cap, freeze and self-dealing. It writes the proposal `PENDING` with `submitted_turn 1000` and `expiry_turn 1036`.
6. **Result.** “Proposal sent. It reserves nothing and creates no obligation.” `AGREEMENT_PROPOSED` is private; Bravia receives `N1` without the terms in its subject line.
7. **Bravia's view.** Bravia opens `DPW-007`, sees every term, the expiry turn and three choices: accept, reject, or ignore. Merely opening the proposal writes nothing and notifies no one.
8. **Bravia rejects.** `DPW-009` asks for confirmation; the rejection is immediate and private, records `responded_turn 1004`, releases Arcadia's open-proposal slot and creates no cooldown.
9. **Arcadia's view.** “Bravia declined. No reason was published.” `N4` carries no reason. Arcadia may propose again immediately.
10. **Why authority is preserved.** Arcadia chose to offer; Bravia chose to refuse; the system neither accepted nor rejected for either; silence was never treated as consent.

### J2 — Accept, activate and inspect (`DPW-008`, `DPW-017`, `DPW-020`)

1. **Incoming proposal.** Bravia opens the proposal at turn 1010 and sees the terms unchanged from submission (terms are immutable).
2. **Confirm accept.** The confirmation repeats the full terms, the activation boundary, the expiry, the public/private switch and the breach consequence; there is no preselected button and no countdown.
3. **Server validation.** Submission succeeds; at P2 on 1011 the server re-validates ownership, pair, caps, duplicate, expiry and freeze. Nothing has activated yet.
4. **Private acceptance.** The agreement exists in `ACCEPTED`; Arcadia receives `N3`. The terms are still parties-only.
5. **Activation.** At P4 step 3 the agreement becomes `ACTIVE`, `activation_turn 1011`, `expiry_turn 1371`. The public record is written after the five steps succeed.
6. **Public record.** At P6, `N6` reaches both parties and the public record shows type, parties, version, activation and expiry — no private note and no negotiation history.
7. **Inspect.** `DPW-020` shows the binding term, the version history and the terminal-event slot. The public sees the same record minus private fields.
8. **Why authority is preserved.** Both players consented to the exact version; activation executed their decision; the system did not choose the counterparty, the term or the response.

### J3 — Withdraw before acceptance (`DPW-010`)

1. **Sender's second thoughts.** Arcadia proposed `DP-T02` at 1100; Bravia has not answered.
2. **Withdraw.** The confirmation states: free, immediate, private, cannot be undone, and Bravia receives no reason unless Arcadia publishes one.
3. **Result.** The proposal is `WITHDRAWN`; Arcadia's cap slot is released; Bravia receives `N5`.
4. **Race.** If Bravia's acceptance had been recorded first at the same boundary, the withdrawal fails with `DPF-01` and the acceptance stands; the reverse records a withdrawal and the acceptance fails at submission (DIP-130).
5. **Why authority is preserved.** Arcadia's own offer remained Arcadia's to withdraw until the moment Bravia accepted; no obligation existed before that acceptance.

### J4 — Amend a live treaty (`DPW-014`, `DPW-018`)

1. **Current state.** The NAP is `ACTIVE`, version 1, expiry 1371. Arcadia wants a longer term.
2. **Choose `AMEND`.** The form shows old terms beside proposed terms; Arcadia selects expiry 1731 and version 2.
3. **Warning.** “Version 1 remains fully in force until version 2 activates. If Bravia does not accept, nothing changes.” No grace period exists.
4. **Submit.** The `AMEND` proposal is `PENDING`; Bravia receives `N1`; the old NAP still blocks a war declaration and still expires at 1371.
5. **Bravia accepts.** At P2 the amendment is validated; at P4 step 3 version 2 activates, version 1 is labelled `SUPERSEDED` with its activation and supersession turns, and expiry becomes 1731.
6. **Rejection path.** Had Bravia rejected, the agreement would still be version 1 at expiry 1371; the rejection is private and creates no cooldown.
7. **Invalid path.** An amendment that names `DP-T02` instead of `DP-T01` fails `DPF-13`; a type change is a termination plus a new proposal (DIP-065).
8. **Why authority is preserved.** Bravia was not bound by the new version until it accepted; the old obligations were never silently replaced.

### J5 — Break a treaty (`DPW-021`)

1. **Decision.** The NAP no longer serves Arcadia. The interface offers two exits: propose mutual termination (Bravia may refuse) or break (unilateral).
2. **Break confirmation.** The panel states, in this order: the record is public and permanent; the war block ends at the boundary; the breach count rises by 1; Arcadia may not propose the same type to the same nation for 36 turns (extended by Arcadia's own freeze); nothing is confiscated, frozen or auto-retaliated; Bravia cannot reject the break.
3. **Cancel path.** “Keep the agreement” is the default and is always available; the button is not preselected.
4. **Confirm.** At P4 step 2 the agreement becomes `BREACHED`, the effect ends, the public event names Arcadia as breaker, and Bravia receives `N8`.
5. **Consequences.** The count rises; the cooldown is measured from the break turn; the next eligible proposal turn is shown. No value moves.
6. **Race.** If Bravia's mutual termination resolves at the same boundary, termination wins at step 1 and the break fails with `DPF-01`; no breach event exists.
7. **Why authority is preserved.** Arcadia chose to break its own promise; Bravia was not asked to consent to being released; the system applied the published consequence and did not invent a punishment.

### J6 — An expired proposal and an expired treaty (`DPW-011`, `DPW-022`)

1. **Warning.** At 1024 both parties receive `N2` for a proposal expiring at 1036; at `expiry − 24` they receive `N7` for an agreement.
2. **Nothing happens unless a player acts.** No acceptance is inferred; no renewal is inferred; no “last chance” button accepts anything.
3. **Proposal expiry.** At P4 step 1 the proposal becomes `EXPIRED`, both are notified once, and the proposer's slot is released. The record says “deadline passed”, not “rejected”.
4. **Agreement expiry.** At step 1 the agreement becomes `EXPIRED`, the NAP block ends, and the public record changes. A renewal that activated at the same boundary loses and fails `DPF-12`.
5. **Why authority is preserved.** Expiry executes the deadline the proposer chose or the term both parties agreed; it never interprets silence as a new commitment.

### J7 — A refused action (`DPW-013`)

1. **Attempt.** An alliance officer opens a member's incoming NAP and tries to accept it.
2. **Refusal.** The server resolves authority from the session, finds the officer does not own the addressed nation and returns `DPF-03 UNAUTHORIZED`. B-08 has no delegation (DIP-015), so no scope can be checked.
3. **What the officer sees.** “Only the owner of this nation can accept. An alliance role does not grant diplomatic authority.”
4. **What the member sees.** Nothing; there is no valid acceptance to notify.
5. **State.** The proposal stays `PENDING`; no event, no reservation, no cooldown.
6. **Why authority is preserved.** The member's player, not its alliance, owns the decision; a failed attempt cannot be mistaken for a response.

### J8 — An embargo declared and lifted (`DPW-025`, `DPW-026`, `DPW-027`)

1. **Eligibility.** Arcadia holds `HOSTILE` toward Etruria and no consultation pact is active. The declaration panel is enabled only when the posture gate is met.
2. **Confirmation.** The panel lists the blocked routes (new directed offers/acceptances; new aid agreements/transfers) and the routes that stay open (T01/T02 diplomacy, third-party trade, already-accepted settlements and active aid deliveries). It states the 24-turn term, that the target cannot lift it, and that no fee or price changes.
3. **Declare.** At P4 step 5 the embargo becomes `ACTIVE`; at P6 the fact is public and Etruria receives `N9`.
4. **During the term.** Arcadia changes posture to `TENSE`: the embargo continues to its term. Etruria tries to lift it: the action is not offered, and a crafted request fails `DPF-03`.
5. **Lift early.** Arcadia lifts at 1610; the embargo becomes `LIFTED`, `end_turn = 1610`, and the 12-turn re-imposition cooldown starts from the lift.
6. **Re-impose.** A declaration at 1621 fails `DPF-08`; at 1622 it succeeds if the posture and notice gates are still met. Arcadia's own freeze extends the cooldown; Etruria's does not.
7. **Why authority is preserved.** Arcadia chose to sanction and to lift; Etruria was not asked to consent to a coercive act it cannot control, and the system did not auto-retaliate or auto-renew.

---

## 5. Proposal and consent state machines

### 5.1 The canonical proposal lifecycle

B-08 defines exactly five proposal states. This document adds none; the prompt's candidate states are reconciled here so an implementation cannot invent a sixth.

| Candidate state | Disposition | Reason |
|---|---|---|
| `DRAFT` | **Not a state** | A local unsent form is interface state and writes nothing (DIP-033) |
| `PENDING` | **Canonical** | Submitted and awaiting the named counterparty |
| `ACCEPTED` | **Canonical** | Both consented; the effect applies at step 3 |
| `REJECTED` | **Canonical, terminal** | The counterparty declined |
| `WITHDRAWN` | **Canonical, terminal** | The proposer withdrew before acceptance |
| `EXPIRED` | **Canonical, terminal** | The deadline passed unanswered |
| `COUNTERED` | **Not adopted** | No counterproposals (DIP-034) |
| `INVALIDATED` | **Not adopted** | A failed validation writes nothing and the proposal keeps its prior state (DIP-122) |
| `ACTIVATED` | **Not a proposal state** | The proposal stays `ACCEPTED` as history; the **agreement** becomes `ACTIVE` (DIP-035) |

### 5.2 Proposal transitions

| # | From | Trigger | Authorized actor | Permission | Preconditions | Validation | To | Notification | Audit | Failure |
|---|---|---|---|---|---|---|---|---|---|---|
| PT-01 | — | Submit | Proposing owner | `A3`–`A6` | §3 `DPW-006` | Ownership, target, pair, duplicate, cap, freeze, terms | `PENDING` | `N1` | `AGREEMENT_PROPOSED` (private) | `DPF-02/03/04/05/06/07/13` |
| PT-02 | `PENDING` | Accept | Named counterparty owner | `A7` | Proposal live, unexpired | Submission + P2 re-validation | `ACCEPTED` | `N3` | `AGREEMENT_ACCEPTED` (private) | `DPF-01/04/05/07/11/13` |
| PT-03 | `PENDING` | Reject | Named counterparty owner | `A8` | Proposal live | State + version | `REJECTED` | `N4` | `PROPOSAL_REJECTED` (class S) | `DPF-01/03` |
| PT-04 | `PENDING` | Withdraw | Proposer | `A9` | No acceptance recorded | State | `WITHDRAWN` | `N5` | `PROPOSAL_WITHDRAWN` (class S) | `DPF-01/03` |
| PT-05 | `PENDING` | Deadline | Boundary | System | `current_turn ≥ expiry_turn` | Freeze-aware expiry | `EXPIRED` | Expiry notice | `PROPOSAL_EXPIRED` (class S) | — |
| PT-06 | `ACCEPTED` | Boundary, step 3 | Boundary | System | Both acceptances valid | Steps 1–2 did not kill the object | (`ACCEPTED` retained; agreement → `ACTIVE`) | `N6` | `AGREEMENT_ACTIVATED` (public) | `DPF-01` |
| PT-07 | `ACCEPTED` | Break, step 2 | Either party | `A10` | Agreement not terminal | Idempotency, state | (`ACCEPTED` retained; agreement → `BREACHED`) | `N8` | `AGREEMENT_BREACHED` | `DPF-01/03` |
| PT-08 | `ACCEPTED` | Mutual termination, step 1 | Both parties | `A6` | Both accepted | State | (`ACCEPTED` retained; agreement → `TERMINATED`) | `N8` | `AGREEMENT_TERMINATED` | `DPF-01/03` |

**Consent is per transition, not per object.** PT-02 consumes the counterparty's consent for that exact version; PT-08 requires a **new** acceptance from both parties even though they already accepted the original agreement. No transition is triggered by a view, a notification, a logout or a turn boundary alone except PT-05 and PT-06, whose authorization was the players' earlier submission or acceptance.

### 5.3 Agreement states and transitions

| # | From | Trigger | Actor | To | Consent | Effect | Record | Failure |
|---|---|---|---|---|---|---|---|---|
| AT-01 | — | Accepted proposal | Both players | `ACCEPTED` | Both | None yet | `AGREEMENT_ACCEPTED` | — |
| AT-02 | `ACCEPTED` | Boundary, step 3 | System | `ACTIVE` | Already given | Effect live | `AGREEMENT_ACTIVATED` | `DPF-01/02/04/07/11` |
| AT-03 | `ACTIVE` | Amendment activates, step 3 | System | `ACTIVE` (version + 1) | Both on the new version | New terms | `AGREEMENT_AMENDED` | `DPF-01/04/13` |
| AT-04 | `ACTIVE` | Renewal activates, step 3 | System | `ACTIVE` (expiry moved) | Both | Term extended | `AGREEMENT_RENEWED` | `DPF-01/12` |
| AT-05 | `ACTIVE` | Term end, step 1 | System | `EXPIRED` | Pre-agreed | Effect ends | `AGREEMENT_EXPIRED` | — |
| AT-06 | `ACTIVE`/`ACCEPTED` | Mutual termination, step 1 | Both players | `TERMINATED` | Both | Effect ends; reservation released | `AGREEMENT_TERMINATED` | `DPF-01` |
| AT-07 | `ACTIVE`/`ACCEPTED` | Break, step 2 | One player | `BREACHED` | One, with record | Effect ends; count +1; cooldown | `AGREEMENT_BREACHED` | `DPF-01` |
| AT-08 | `ACCEPTED` | Aid delivery, step 4 | System | `COMPLETED` | Pre-agreed | Transfer | `AID_SETTLED` | B-02 `F1`/`F3`/`F8` |
| AT-09 | `ACCEPTED`/`ACTIVE` | Reroll | System | `TERMINATED` | Account rule | Cleanup | `AGREEMENT_TERMINATED` (`NATION_RETIRED`) | — |
| AT-10 | any terminal | Any attempt to reactivate | — | **Refused** | — | None | None | `DPF-01` (DIP-126) |

**Version history is not a state.** A superseded version is a labelled row, not a live agreement; only one version binds at a time.

### 5.4 Embargo transitions

| # | From | Trigger | Actor | To | Consent | Record | Failure |
|---|---|---|---|---|---|---|---|
| ET-01 | — | Declare | Imposer | `ACTIVE` | None | `EMBARGO_DECLARED` | `DPF-02/07/08/09/15` |
| ET-02 | `ACTIVE` | Term end, step 5 | System | `EXPIRED` | Pre-agreed | `EMBARGO_EXPIRED` | — |
| ET-03 | `ACTIVE` | Lift, step 5 | Imposer | `LIFTED` | Imposer's own | `EMBARGO_LIFTED` | `DPF-01/03` |
| ET-04 | `EXPIRED`/`LIFTED` | Re-declare after cooldown | Imposer | new `ACTIVE` | None | new `EMBARGO_DECLARED` | `DPF-08/15/09` |
| ET-05 | `ACTIVE` | Target attempts lift | Target | **Refused** | — | None | `DPF-03` |

---

## 6. Treaty lifecycle matrix

**6.1 The catalogue is closed.** B-08 has exactly three agreement types and one act. No row below adds a type; a fourth type cannot be proposed, stored or displayed as a treaty (DIP-037).

| Field | `DP-T01` NAP | `DP-T02` consultation | `DP-T03` aid | `DP-A01` embargo |
|---|---|---|---|---|
| **Purpose** | Block war declaration between the parties for the term | Require a warning before hostility or an embargo | One consented crown transfer | Coercive transfer block for a fixed term |
| **Parties** | Two nations | Two nations | Payer + recipient | Imposer + target |
| **Eligible participants** | Both active, pair clear | Both active, pair clear | Payer proposer, recipient accepts; pair clear | Imposer active, target active, imposer `HOSTILE` |
| **Proposal authority** | Either owner | Either owner | Payer owner | Imposer only (not a proposal) |
| **Consent** | Both, explicit | Both, explicit | Both, explicit; recipient's acceptance reserves | **None** |
| **Activation** | Step 3 after acceptance | Step 3 | Step 3; delivery step 4 | Step 5, immediate at boundary |
| **Duration** | 360 turns + pair freeze | 360 turns + pair freeze | One-shot; no expiry | 24 turns, never freeze-extended |
| **Obligations** | Do not declare war | Notice at least 12 and at most 36+freeze turns before the hostile act | Transfer `A` crowns | Block new directed offers/acceptances and new aid transfers |
| **Scheduled processing** | Expiry, renewal | Expiry, renewal | Reservation, delivery, completion | Term expiry |
| **Amendment** | Versioned, both consent | Versioned, both consent | **Not permitted** (DIP-040) | **Not permitted** |
| **Renewal** | `RENEW`, prospective, before expiry | Same | None; a new aid is a new proposal | New declaration after cooldown |
| **Termination** | Mutual or break | Mutual or break | Mutual or break before delivery | Imposer lift only; target cannot |
| **Breach** | War declaration if Prompt 10 permits it; otherwise inert | Only if a later system permits the gated act; blocked today | Break before delivery | **Not a treaty; no breach state** |
| **Consequences** | Effect ends; public record; count; cooldown | Same | Reservation released; public record; count; cooldown | Term ends; no breach count |
| **Visibility** | Pending private; active public | Pending private; notice private; active public | Pending private; completed amount public | Public at declaration |
| **Notifications** | `N1`–`N8` | `N1`, `N3`, `N6`, `N8`; notice visible to counterparty only | `N1`–`N8` | `N9` |
| **Failure cases** | `DPF-02/04/07/11/13` | Same + `DPF-09/10` on the gated act | `DPF-05` on reservation | `DPF-08/09/15` |
| **Formulas** | F-DP-002/003/004/009 | F-DP-002/003/004/006/009 | F-DP-003/004/011 | F-DP-008 |
| **Requirements** | REQ-518, REQ-520, REQ-521, REQ-526 | REQ-519, REQ-521 | REQ-524, REQ-525 | REQ-529 |

**6.2 Five categories that must not be conflated.**

| Category | Example | Who decides | Can the system do it alone? | Where recorded |
|---|---|---|---|---|
| **Agreement recording intent** | A `DP-T02` notice | The sender | No — a player action (`A2`) | Class S notice |
| **Binding in-game obligation** | An `ACTIVE` NAP | Both parties at submission/acceptance | No — the boundary only activates what both accepted | Class P agreement |
| **Automatic gameplay effect** | NAP war block; embargo permission block | The owning system reads the active object | The read is automatic; **creating** the object is not | Owning system plus B-08 record |
| **Action another system must perform** | Aid transfer through B-04; war-declaration check by Prompt 10 | B-08 states the contract; B-04/Prompt 10 execute | The transfer executes from prior consent; the war check reads the NAP | B-04 ledger; Prompt 10 event |
| **Unilateral national declaration** | Posture; embargo; break | The acting owner | No | Class I/P |

**6.3 The treaty-specific acceptance requirements (B-08 §21.1).**

1. No agreement becomes active without every required participant's valid consent.
2. An amendment cannot change an obligation without the required renewed consent.
3. Expiry follows the agreed terms, extended only by the approved freeze rule.
4. A breach is based on an approved, verifiable condition: a unilateral break, or an external system's permitted violation (DIP-072).
5. A player can inspect every obligation their nation has accepted (`DPW-020`).
6. The system creates no hidden obligation, no negative-option renewal and no inferred consent.

**6.4 The one inert effect.** The NAP's war-declaration block is a permission B-08 publishes and Prompt 10 must enforce; until Prompt 10 exists it cannot be exercised (DIP-141). This is disclosed, not hidden: the agreement is still a public promise with a record, and no first-playable action can breach it.
---

## 7. Edge-case catalogue

**7.1 How to read an edge case.** Each row states the trigger, the **expected** behaviour, the **prohibited** behaviour, the state/notification/audit outcome, the governing rule, the test that would prove it and whether an owner decision is needed. "No" in the last column means the case is resolved by B-08 and this document; "Prompt 09" or "Prompt 10" means the case cannot be closed until that system exists. No row invents a rule.

### 7.2 Player, ownership and account cases (`DPE-001`…`DPE-010`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-001` | Player logs out while a proposal is pending | Proposal stays `PENDING` to its deadline; the counterparty sees nothing about the logout | Expiring or withdrawing it because the sender disconnected | No change · no notice · no event | DIP-046, DIP-100 | DPA-073 | No |
| `DPE-002` | Nation leadership/ownership changes (B-06) | Existing agreements persist; a merely pending acceptance is **not** inherited; the new owner may accept or ignore it | Treating the old player's pending click as the new owner's consent | Agreement unchanged · no notice beyond normal · no event | DIP-061 | DPA-002 | No |
| `DPE-003` | Nation becomes dormant or has no active owner | Open proposals `EXPIRED` with `COUNTERPARTY_DORMANT`; active agreements persist; new proposals/embargoes targeting it fail `DPF-02` | Terminating active treaties or recording a breach | Proposals terminal · one notice · class S | DIP-128, D-028 | DPA-059 | No |
| `DPE-004` | Reroll retires the nation | All proposals withdrawn (`NATION_RETIRED`), agreements terminated, embargoes lifted, reservations released; replacement neutral, count 0; old page keeps history | Transferring treaties or the breach count to the replacement | All terminal · one notice per counterparty · class P | DIP-086, DIP-127 | DPA-060 | No |
| `DPE-005` | Two sessions submit the same action | The first recorded wins; the second returns the same outcome or `DPF-01` if the state moved | Applying the action twice | One object · one notice · one event | DIP-102, DIP-130 | DPA-003 | No |
| `DPE-006` | Same action submitted twice with one idempotency key | The retry returns the recorded outcome and writes nothing | Creating a second proposal/breach/reservation | One object · one notice · one event | DIP-102, DIP-134 | DPA-004 | No |
| `DPE-007` | An unauthorized player attempts a diplomatic action | `DPF-03 UNAUTHORIZED`; no state change | Granting authority from proximity, alliance or treaty | No change · no notice · failure line only | DIP-013, DIP-015 | DPA-005 | No |
| `DPE-008` | A stale session submits after ownership was lost | `DPF-03`; the action is discarded | Resolving under the old authority | No change · no notice · failure line | DIP-013, DIP-125 | DPA-006 | No |
| `DPE-009` | Permission/eligibility changes between opening the form and submitting | The server re-validates and refuses with the current code; nothing is reserved | Accepting under the state at page load | No change · no notice · failure line | DIP-125 | DPA-007 | No |
| `DPE-010` | A crafted request supplies another nation's `nation_id` | The id is an object reference to authorize, never an identity claim; `DPF-03` | Acting as the other nation | No change · no notice · failure line | DIP-013 | DPA-008 | No |

### 7.3 Consent cases (`DPE-011`…`DPE-021`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-011` | Recipient never responds | Proposal expires at its deadline; no agreement, no penalty | Treating silence as acceptance or as rejection | `EXPIRED` · expiry notice · class S | DIP-021, DIP-046, DIP-062 | DPA-019 | No |
| `DPE-012` | Recipient views the proposal but takes no action | Nothing changes; the proposer is not told | Notifying the proposer of a view or treating it as intent | No change · no notice · no event | DIP-062, DIP-080 | DPA-020 | No |
| `DPE-013` | Recipient rejects | `REJECTED`; free, private, final for that proposal; no cooldown | Recording a breach, a penalty or a public rejection | `REJECTED` · `N4` no reason · class S | DIP-049 | DPA-017 | No |
| `DPE-014` | Proposer withdraws before acceptance | `WITHDRAWN`; cap slot released; counterparty told | Keeping the proposal live or reserving value | `WITHDRAWN` · `N5` · class S | DIP-047 | DPA-023 | No |
| `DPE-015` | Proposer tries to withdraw after acceptance | `DPF-01`; only mutual termination or break can end it | Unilateral withdrawal of an accepted commitment | No change · no notice · failure line | DIP-048, DIP-056 | DPA-024 | No |
| `DPE-016` | Both nations propose the same type reciprocally | Both `PENDING`; first acceptance wins; loser fails `DPF-04` and is `EXPIRED` | Creating two agreements or silently merging them | Winner active; loser terminal · winner `N3` · class P | DIP-044, DIP-050, DIP-124 | DPA-018, DPA-026 | No |
| `DPE-017` | One accepts while the other rejects/withdraws at the same boundary | First recorded submission wins; the later one fails against the changed state | P2 reviving a state a recorded action already changed | One outcome · one notice · one event | DIP-130 | DPA-025 | No |
| `DPE-018` | One participant's authorization becomes invalid during an amendment | The amendment fails at P2; the old version remains in force | Binding the new version without both valid consents | Old version active · failure notice to actor · no amendment event | DIP-064, DIP-125 | DPA-028 | No |
| `DPE-019` | A material amendment is proposed | Both must accept the new version; the old terms remain in force until activation | Inferring consent from the original acceptance | Old version live · `N1`/`N3`/`N6` · class P on activation | DIP-063, DIP-064 | DPA-029 | No |
| `DPE-020` | A treaty is terminated while a scheduled obligation is pending | Step 1 termination releases the reservation and cancels delivery; no breach | Delivering after termination or recording a breach | `TERMINATED` · `N8` · class P | DIP-071, DIP-103 | DPA-033 | No |
| `DPE-021` | A renewal is unanswered or accepted too late | No renewal; expiry stands; a late renewal fails `DPF-12` | Auto-renewing or interpreting the deadline as consent | `EXPIRED` · `N7`/`N8` · class P | DIP-058, DIP-067 | DPA-030, DPA-074 | No |

### 7.4 Timing and processing cases (`DPE-022`…`DPE-033`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-022` | Acceptance and expiry at the same boundary | Step 1 expiry wins; acceptance fails `DPF-01`; no agreement | Activating an expired proposal | `EXPIRED` · expiry notice · class S | DIP-103, DIP-130 | DPA-080 | No |
| `DPE-023` | Amendment activation and expiry at the same boundary | Expiry wins; amendment fails `DPF-01`; no new version | Applying a version to an expired agreement | `EXPIRED` · `N8` · class P | DIP-103, F-DP-012 | DPA-081 | No |
| `DPE-024` | Activation and mutual termination at the same boundary | Step 1 termination wins; activation fails; agreement `TERMINATED` | Publishing an activation and a termination for one object | `TERMINATED` · `N8` · class P | DIP-103 | DPA-082 | No |
| `DPE-025` | Aid delivery due and a break at the same boundary | Step 2 break wins; delivery cancelled; reservation released; breach recorded | Delivering then recording the breach | `BREACHED` · `N8` · class P | DIP-103, DIP-131 | DPA-043 | No |
| `DPE-026` | Embargo declaration and a directed trade accepted at the same boundary | An offer accepted **before** the declaration settles; one accepted **after** it fails on the market side | Retroactively blocking a settled trade or charging a fee | Trade settles/declines · market notice · market record | DIP-095, DIP-103 | DPA-075 | No |
| `DPE-027` | A nation enters `TRANSITION` during a posture cooldown | The cooldown counts only unfrozen boundaries; the eligible turn moves later by the actor's frozen boundaries | Expiring the cooldown early or extending by the counterparty's freeze | Cooldown unchanged except extension · interface shows new turn · no event | DIP-105(b), F-DP-005 | DPA-038 | No |
| `DPE-028` | A nation enters `CRISIS` during a consultation-notice window | The window's **end** extends by pair freeze; the 12-turn minimum does not | Extending the minimum or shortening the end | Notice stays valid longer · no notice · no event | DIP-105(a), F-DP-006a | DPA-076 | No |
| `DPE-029` | A timer spans several frozen blocks | The extension is the union of frozen boundaries, each counted once per scope | Double-counting overlapping freezes or adding wall-clock days | New eligible turn shown · no event | DIP-105 | DPA-077 | No |
| `DPE-030` | Both parties are frozen on the same boundary | A pair-scoped timer gains **+1**, not +2; an actor-scoped timer gains +1 for the actor only | Counting the same lost boundary twice | Eligible turn moved once · no event | DIP-105 | DPA-042 | No |
| `DPE-031` | An action arrives exactly on its eligible turn | It is allowed; the bound is inclusive (`≥`) | Rejecting at the exact bound or requiring +1 | Action applies · normal notice · normal event | F-DP-005/006b/007/008 | DPA-037, DPA-040, DPA-053, DPA-086 | No |
| `DPE-032` | A duplicate boundary-processing event is received | The second run returns the recorded outcome; no second breach/delivery/activation | Writing a second public event or second reservation | One outcome · one notice · one event | DIP-102, DIP-104 | DPA-035 | No |
| `DPE-033` | A scheduled event is retried after a failure | A transient `F8` retries once the turn resumes; a permanent failure leaves the object `ACCEPTED` and notifies both | Half-applying the boundary or silently dropping it | Object state explicit · failure notice · failure line | DIP-104, DIP-129 | DPA-048 | No |

### 7.5 Resource and economy cases (`DPE-034`…`DPE-040`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-034` | Payer has insufficient available crowns | Submission fails `DPF-05`; acceptance reservation fails `DPF-05`; nothing moves | Negative balance, credit or a partial reservation | No agreement/reservation · failure line · no event | DIP-040, F-DP-011 | DPA-046 | No |
| `DPE-035` | A scheduled aid obligation cannot be fulfilled at P4 | The transfer fails atomically; reservation released; agreement returns to `ACCEPTED` only for a transient cause, else terminates `TRANSFER_VOIDED` | Recording delivery without the crowns or creating debt | No transfer · both notified · failure line | DIP-129, DIP-132 | DPA-047 | No |
| `DPE-036` | The payer's balance changes between proposal and activation | The reservation is taken at acceptance and re-validated at P4; if it cannot be honoured the aid fails, not overdrafts | Reserving twice or spending reserved crowns elsewhere | Reservation consistent · both notified · ledger none | DIP-040, DIP-132 | DPA-047 | No |
| `DPE-037` | Payer enters crisis before an authorized transfer | Delivery waits under the freeze rule; no breach; no expiry of the agreement | Confiscating the reservation or failing the payer | Agreement `ACCEPTED` · deadline notice · no event | DIP-105, DIP-129 | DPA-083 | No |
| `DPE-038` | A duplicate resource-transfer event is received | Idempotent by agreement + boundary; one ledger pair, one `transfer_id` | Two transfers or two completion events | One completion · one notice · class P | DIP-102, DIP-132 | DPA-084 | No |
| `DPE-039` | The transfer succeeds but the notification fails | The transfer stands; the notification is retried; no rollback of value | Undoing a successful transfer to make notification consistent | Transfer stays · retry notice · delivery event remains | DIP-104, DIP-114 | DPA-078 | No |
| `DPE-040` | The transfer fails after the authorization was recorded | Nothing is marked delivered; the reservation is released; the failure is visible to both | A “success” record without value movement | No delivery · both notified · failure line | DIP-122, DIP-129 | DPA-047 | No |

### 7.6 Treaty-integrity cases (`DPE-041`…`DPE-045`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-041` | A duplicate agreement would be created | The second activation fails `DPF-04`; the earlier agreement stays authoritative | Two `ACTIVE` agreements of one type for one pair | One active · failure notice · no second event | DIP-052, DIP-134 | DPA-035 | No |
| `DPE-042` | An expired or terminated agreement is presented as active | The interface shows the terminal state and the terminal event; no action is offered | Resurrecting it or showing a stale “active” badge | Terminal · no notice · record unchanged | DIP-055, DIP-126 | DPA-036 | No |
| `DPE-043` | Historical record is altered, or a termination is processed twice | A correction is a new event referencing the original; a duplicate returns the recorded outcome | Editing or deleting an event; two terminal events | Append-only · no new notice · correction event | DIP-119, DIP-134 | DPA-070 | No |
| `DPE-044` | A player tries to evade an obligation by withdrawing after acceptance | `DPF-01`; only termination or break can end it; break records a breach | Treating withdrawal as a loophole | No change · failure line · no event | DIP-048, DIP-056 | DPA-024 | No |
| `DPE-045` | An invalid participant (self, retired, removed) is named | `DPF-02`/`DPF-13`; nothing is created | Creating a treaty with a non-existent or self party | No object · failure line · no event | DIP-037, DIP-074, DIP-123 | DPA-014 | No |

### 7.7 Breach and reputation cases (`DPE-046`…`DPE-049`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-046` | A player attempts to report a breach that did not occur | **No breach-report action exists**; the only inputs are `A10` and the owning system's B-2 event; the request fails `DPF-03`/`DPF-01` | Inventing a report-and-review mechanic or punishing on accusation | No change · failure line · no event | DIP-072, DIP-056 | DPA-051 | No |
| `DPE-047` | A duplicate breach report or a second break on a terminal agreement | `DPF-01`; the recorded breach stands; count unchanged | Raising the count twice | No change · failure line · one event | DIP-076 | DPA-050 | No |
| `DPE-048` | Multiple breaches on the same turn, or an attempt to manipulate the count | Each agreement contributes one event; the count is computed from committed events only | Editing the count or deleting a breach | Count factual · no notice · class P | DIP-085, DIP-134 | DPA-085 | No |
| `DPE-049` | A breach is disputed or claimed to be incorrect | **No dispute state exists.** A party may publish its own reason (`A14`); an operator correction is a new event under Prompt 12, never an edit | Creating a “disputed” status or reversing a count without a decision | Record unchanged; optional published statement · counterparty notified · class P | DIP-078, DIP-089, DIP-119 | DPA-062 | Prompt 12 for any reversal |

### 7.8 Security and multiplayer-integrity cases (`DPE-050`…`DPE-054`)

| ID | Scenario / trigger | Expected | Prohibited | State · notification · audit | Rule | Test | Owner? |
|---|---|---|---|---|---|---|---|
| `DPE-050` | Tampered request or client-side bypass of authorization | The server re-derives authority and eligibility from trusted state and rejects with `DPF-03`/`DPF-13` | Trusting a client flag, a hidden field or an `isAdmin` claim | No change · failure line · audit attempt | DIP-013, DIP-079 | DPA-079 | Stage 5 implementation |
| `DPE-051` | Replayed acceptance or duplicate transaction | Idempotency key returns the original receipt; no second agreement or applicable side effect | Applying the same decision twice | One object · one notice · one event | DIP-102, DIP-132 | DPA-088 | Stage 5 |
| `DPE-052` | Nation-ID substitution in a URL or payload | The object is authorized against the session; mismatch is `DPF-03` | Object-level authorization by ID alone | No change · failure line · audit | DIP-013 | DPA-008 | Stage 5 |
| `DPE-053` | Acceptance races expiry; a transfer races termination | The five-step order resolves both; the loser fails with `DPF-01`/`DPF-12` | Ordering by arrival time off the boundary | One outcome · normal notices · one event | DIP-103, DIP-130 | DPA-080, DPA-082, DPA-033 | Stage 5 concurrency test |
| `DPE-054` | Unauthorized history read, restricted-field access or a notification leak | Visibility follows B-08 §13.2; a privileged read is itself audited; a notification never contains another pair's private term | Exposing pending terms to an alliance, an administrator UI or a notification subject | Field absent · no notice · privileged read audited | DIP-111, DIP-112, DIP-121 | DPA-065, DPA-068, DPA-087 | Prompt 12 for privileged-read audit |

**7.9 Coverage check.** The 54 rows cover every scenario group named in the Prompt 08C brief: player/ownership (10), consent (11), timing (12), resources (7), treaty integrity (5), breach/reputation (4) and security/multiplayer (5). Where the brief names a scenario B-08 does not implement (breach reporting, dispute states, partial aid), the row says so explicitly rather than inventing a mechanic. §7.10 is the audited mapping from each edge case to the test that actually asserts it; an identifier appearing in a test row is not accepted as coverage on its own.

**7.10 Edge-case coverage matrix (audited 2026-10-30).** `COVERED` means the named test establishes the case's preconditions, executes its trigger and asserts its expected postcondition; it does **not** mean the test has run. `PARTIAL` means at least one promised outcome is outside B-08's ownership or cannot be asserted yet. Every row records the concrete assertion, not just a test number. The matrix is checked by `verify_diplomacy_workflows.py` (status vocabulary, valid test IDs, mandatory explanation, and count reconciliation).

| DPE | Title | Risk tested | Primary DPA | Additional | Assertion that proves coverage | Status | Explanation / required follow-up |
|---|---|---|---|---|---|---|---|
| `DPE-001` | Player logs out with a proposal pending | Disconnect must not change consent state | `DPA-073` | — | Proposal is still `PENDING` at 1010 and reaches its 1036 expiry; no logout event or notice exists | **COVERED** | — |
| `DPE-002` | Nation ownership changes | Pending consent is not inherited; active treaties persist | `DPA-002` | — | Pre-existing `DP-T02` remains `ACTIVE`; the old session is refused; only the new owner's acceptance is recorded | **COVERED** | — |
| `DPE-003` | Nation dormant / no active owner | Open proposals expire; treaties persist; new acts fail closed | `DPA-059` | — | Open proposals become `EXPIRED`; NAP stays `ACTIVE`; new proposal returns `DPF-02`; no breach or termination | **COVERED** | — |
| `DPE-004` | Reroll retires the nation | No treaty or breach inheritance | `DPA-060` | `DPA-069` | All objects terminal; reservation released; replacement count 0; old page keeps its own history | **COVERED** | — |
| `DPE-005` | Two sessions submit the same action | Exactly one object | `DPA-003` | — | First recorded submission wins; the second gets the recorded outcome; one `PENDING` proposal exists | **COVERED** | — |
| `DPE-006` | Same action with one idempotency key | Retry must not duplicate | `DPA-004` | — | Same receipt returned; exactly one object and one event | **COVERED** | — |
| `DPE-007` | Unauthorized player attempts an act | No authority from proximity, treaty or alliance | `DPA-005` | `DPA-009`, `DPA-010`, `DPA-011`, `DPA-012` | `DPF-03`; proposal remains `PENDING`; no notice to the counterparty | **COVERED** | — |
| `DPE-008` | Stale session submits after ownership loss | Old authority cannot resolve | `DPA-006` | — | `DPF-03`; no acceptance recorded | **COVERED** | — |
| `DPE-009` | Eligibility changes before submission | Server re-validates, not the form's snapshot | `DPA-007` | — | Refused with the current code; no agreement and no reservation | **COVERED** | — |
| `DPE-010` | Crafted request names another nation | Nation id is an object, not an identity | `DPA-008` | — | `DPF-03`; no state change | **COVERED** | — |
| `DPE-011` | Recipient never responds | Silence is not acceptance or rejection | `DPA-019` | — | `EXPIRED` at step 1; both notified once; no agreement | **COVERED** | — |
| `DPE-012` | Recipient views but does nothing | A view is not intent | `DPA-020` | — | No state or notification change | **COVERED** | — |
| `DPE-013` | Recipient rejects | Rejection is free, private and final for that proposal | `DPA-017` | — | `REJECTED`; `N4` without a reason; no breach or cooldown | **COVERED** | — |
| `DPE-014` | Proposer withdraws before acceptance | Withdrawal releases the cap slot | `DPA-023` | — | `WITHDRAWN`; `N5`; no obligation | **COVERED** | — |
| `DPE-015` | Withdrawal attempted after acceptance | Accepted commitment cannot be withdrawn | `DPA-024` | — | `DPF-01`; agreement remains live | **COVERED** | — |
| `DPE-016` | Reciprocal proposals | First acceptance wins; no second agreement | `DPA-018` | `DPA-026` | One agreement; loser fails `DPF-04`; same-boundary case resolves by `(submitted_at, action_id)` | **COVERED** | — |
| `DPE-017` | Accept races reject/withdraw | First recorded submission wins | `DPA-025` | — | `ACCEPTED` stands; later rejection/withdrawal fails `DPF-01` | **COVERED** | — |
| `DPE-018` | Authority invalid during amendment | No version binds without both valid consents | `DPA-028` | — | Amendment fails at P2; v1 remains in force | **COVERED** | — |
| `DPE-019` | Material amendment | Fresh consent for the exact new version | `DPA-029` | `DPA-027` | Only the accepted version applies after activation; v1 stays live until then | **COVERED** | — |
| `DPE-020` | Termination with an obligation pending | Termination cancels delivery, not a breach | `DPA-033` | — | Reservation released; balance unchanged; no transfer | **COVERED** | — |
| `DPE-021` | Renewal unanswered or too late | No auto-renewal; deadline is not consent | `DPA-074` | `DPA-030` | Unanswered renewal expires with the agreement; late activation fails `DPF-12` | **COVERED** | — |
| `DPE-022` | Acceptance and expiry at one boundary | Expiry step runs first | `DPA-080` | — | `EXPIRED`; acceptance `DPF-01`; no agreement | **COVERED** | — |
| `DPE-023` | Amendment activation and expiry | No version applies to an expired agreement | `DPA-081` | — | v1 `EXPIRED`; amendment `DPF-01`; no v2 | **COVERED** | — |
| `DPE-024` | Activation and mutual termination | One terminal outcome | `DPA-082` | — | `TERMINATED`; no activation event | **COVERED** | — |
| `DPE-025` | Aid delivery due on a break boundary | Break wins; no delivery | `DPA-043` | — | Delivery cancelled; reservation released; one breach; no transfer | **COVERED** | — |
| `DPE-026` | Embargo declared against a trade boundary | No retroactive block or fee | `DPA-075` | — | Accepted-before offer settles; accepted-after offer declines; no post-settlement adjustment | **COVERED** | — |
| `DPE-027` | Transition during a posture cooldown | Only the actor's freeze extends it | `DPA-038` | `DPA-039` | 1514 `DPF-08`; 1515 accepted; counterparty's freeze does not move 1512 | **COVERED** | — |
| `DPE-028` | Crisis during a consultation window | End extends; minimum does not | `DPA-076` | — | Minimum 2012 unchanged; end 2041; 2042 `DPF-09` | **COVERED** | — |
| `DPE-029` | Timer spans several frozen blocks | Union counted once | `DPA-077` | — | 5+3 boundaries yield expiry 1044, not 1047 or a wall-clock extension | **COVERED** | — |
| `DPE-030` | Both parties frozen on one boundary | Pair +1, never +2 | `DPA-042` | — | Pair-scoped +1; actor-scoped +1 for that actor only | **COVERED** | — |
| `DPE-031` | Action on the exact eligible turn | Inclusive lower bound | `DPA-037` | `DPA-040`, `DPA-053`, `DPA-086` | 1512 allowed; notice bounds; embargo 1636; breach cooldown 2036 | **COVERED** | — |
| `DPE-032` | Duplicate boundary event | Recorded outcome is returned | `DPA-035` | — | One activation; no second reservation, notice or event | **COVERED** | — |
| `DPE-033` | Scheduled event retried after failure | Transient retry; permanent failure is explicit | `DPA-048` | — | Agreement returns to `ACCEPTED`; one `AID_SETTLED` on retry | **COVERED** | — |
| `DPE-034` | Insufficient available crowns | No negative balance or credit | `DPA-046` | — | `DPF-05` at submission/acceptance; nothing reserved | **COVERED** | — |
| `DPE-035` | Obligation cannot be fulfilled at P4 | Atomic failure, no delivery record | `DPA-047` | — | Reservation released; no debt; no delivery; both notified | **COVERED** | — |
| `DPE-036` | Balance changes between proposal and P4 | Re-validate, never overdraw | `DPA-047` | — | P4 fails atomically against the reserved balance; one reservation only | **COVERED** | — |
| `DPE-037` | Payer enters crisis before delivery | Delivery waits; no breach | `DPA-083` | — | Agreement stays `ACCEPTED`; deadline extended; reservation held; one delivery | **COVERED** | — |
| `DPE-038` | Duplicate transfer event | Idempotent transfer | `DPA-084` | — | One ledger pair and one completion for the same `transfer_id` | **COVERED** | — |
| `DPE-039` | Notification fails after transfer | Value is not rolled back for a message failure | `DPA-078` | — | Transfer and delivery event stand; notification retried; no second transfer | **COVERED** | — |
| `DPE-040` | Transfer fails after authorization | No success record without value | `DPA-047` | — | No delivery; reservation released; failure visible to both | **COVERED** | — |
| `DPE-041` | Duplicate agreement | One `ACTIVE` agreement per type and pair | `DPA-035` | — | Second activation `DPF-04`; one active record | **COVERED** | — |
| `DPE-042` | Terminal agreement shown as active | No resurrection, no stale badge | `DPA-036` | — | Expired and terminated objects both show the terminal state and refuse renewal | **COVERED** | — |
| `DPE-043` | History altered or termination processed twice | Append-only, one terminal event | `DPA-070` | — | Correction appends; duplicate termination returns the recorded outcome; one terminal event | **COVERED** | — |
| `DPE-044` | Withdraw after acceptance to evade | No withdrawal loophole | `DPA-024` | — | `DPF-01`; only termination or break ends the agreement | **COVERED** | — |
| `DPE-045` | Invalid participant (self, retired, removed) | No object with an ineligible party | `DPA-014` | — | `DPF-13` for self/type; `DPF-02` for retired/removed; nothing created | **COVERED** | — |
| `DPE-046` | False breach report | No accusation-driven penalty | `DPA-051` | — | No report action exists; request fails; no event | **COVERED** | — |
| `DPE-047` | Duplicate breach | One event per agreement | `DPA-050` | — | `DPF-01`; count unchanged at 1 | **COVERED** | — |
| `DPE-048` | Multiple breaches same turn / count manipulation | Derived count, one event per agreement | `DPA-085` | — | Two agreements yield count 2; edit and replay change nothing | **COVERED** | — |
| `DPE-049` | Disputed or corrected breach | No dispute state; corrections append | `DPA-062` | — | Party publish creates a class-P statement; edit is refused; original unchanged | **PARTIAL** | Operator correction is Prompt 12's; no B-08 test can assert that path. `DPA-062` covers the diplomacy-side behavior. |
| `DPE-050` | Tampered request / client-side bypass | Server derives authority from trusted state | `DPA-079` | — | `isAdmin` and `actor_nation_id` ignored; `DPF-03`; zero state change; attempt audited | **COVERED** | Stage 5 implementation evidence still required. |
| `DPE-051` | Replayed acceptance | Idempotent decision | `DPA-088` | `DPA-004` | Same receipt after an actual acceptance; one agreement and one consent event; no second activation or side effect (the NAP has no reservation) | **COVERED** | — |
| `DPE-052` | Nation-ID substitution | Object authorization, not id trust | `DPA-008` | — | `DPF-03`; no state change | **COVERED** | — |
| `DPE-053` | Acceptance/expiry and transfer/termination races | Boundary order decides, not arrival time | `DPA-080` | `DPA-082`, `DPA-033` | Acceptance loses to expiry; activation loses to termination; termination cancels delivery | **COVERED** | Stage 5 concurrency test still required. |
| `DPE-054` | Unauthorized history or notification leak | Visibility matrix holds | `DPA-065` | `DPA-068`, `DPA-087` | `DPA-065` denies pending terms and private history to a third party/alliance member; `DPA-087` denies private terms in a non-party notification; `DPA-068` keeps pending terms out of the public profile | **PARTIAL** | The privileged-read audit is Prompt 12's under DIP-121; no B-08 test can assert it. |

**7.10a `DPE-054` scenario-level resolution (08C-D).** `DPE-054` combines three disclosure scenarios. They are recorded separately here so the combined row's PARTIAL status is not mistaken for an untested privacy case and the deferred part is not mistaken for covered work.

| Scenario | Actor and attempted access | Verifying test | Observable result asserted | Status | Owner / dependency |
|---|---|---|---|---|---|
| **A — unauthorized history read** | C, a third party and an alliance member, queries the A/B pair's private event history | `DPA-065` | No private history entry is returned; only the public active record is visible | **Covered** | B-08 DIP-111; B-03 session authority |
| **B — restricted pending terms** | C reads the terms of A/B's pending aid proposal and the public profile | `DPA-065`, `DPA-068` | The pending amount and terms are absent; the active public agreement is visible and the pending one is not | **Covered** | B-08 DIP-108, DIP-113 |
| **C — notification leak** | C is allied to B but is not a party to A→B's pending proposal; C's feed is queried and delivery retried | `DPA-087` | C receives no `N1` and no private field, amount or rejection reason; the retry creates no second notice and no state change; the proposal stays `PENDING` | **Covered** | B-08 DIP-111, DIP-114; Prompt 09 may display public fields only |
| **Audit of a privileged read** | An administrator reads the full history under the restricted class | None in B-08 | A privileged read is itself audited (DIP-121) | **Deferred** | **Prompt 12** owns the restricted class and its audit path; D-042 sets the audit principle. No B-08 test can assert an unimplemented privileged-read route |

The three disclosure scenarios are asserted by existing tests; the combined `DPE-054` row stays **PARTIAL** because its stated outcome also includes "a privileged read is itself audited", which belongs to Prompt 12. This is an external dependency, not a missing privacy test. The matrix is not claiming that the audit exists or has run.

**7.11 Coverage totals.** 54 rows: **52 COVERED** and **2 PARTIAL** (`DPE-049`, `DPE-054`); 0 NOT COVERED and 0 NOT APPLICABLE. Every test named in the matrix exists in §14, and every `DPE-001`…`DPE-054` appears exactly once as a row. The matrix is the authority for coverage; §14.9's counts reconcile to it. `DPE-054`'s three disclosure scenarios are individually covered per §7.10a; only its privileged-read audit is deferred to Prompt 12.

---

## 8. Failure codes and recovery

### 8.1 The fifteen codes (B-08 §15.1)

No new `DPF` code is created by 08C. Where a cause belongs to the turn engine, the B-02 `F` code is returned instead; a diplomatic code is never invented to duplicate one.

| Code | Player-facing sentence (pattern) | Internal cause | Retriable? | New player action? | State unchanged? | Resources | Audit | Notification | Recovery condition |
|---|---|---|---|---|---|---|---|---|---|
| `DPF-01` | “This agreement is no longer in the state that action needs.” | Object terminal or wrong state | No | Yes, choose a valid object | Yes | None | Failure line | Actor only | A live object of the required state exists |
| `DPF-02` | “That nation is not available for diplomacy.” | Retired, removed or dormant target | No | Choose another counterparty | Yes | None | Failure line | Actor only | Target becomes available; dormancy is protective |
| `DPF-03` | “Only the owner of this nation can do that.” | Session ownership mismatch; no delegation | No | Act from the owning account | Yes | None | Failure line | Actor only | The owner acts; a future delegation needs a decision |
| `DPF-04` | “A live proposal or agreement of this type already exists for this pair and direction.” | Duplicate ordered proposal or unordered agreement | No | Use the existing object, withdraw, or wait | Yes | None | Failure line | Actor only | The existing object ends |
| `DPF-05` | “You do not have enough available crowns for this aid.” | Insufficient available balance at submission or reservation | Yes, with a lower amount | Lower `A` or wait | Yes | None reserved | Failure line | Actor only | Balance ≥ `A` available |
| `DPF-06` | “You already have three proposals awaiting a response.” | Outgoing proposal cap | No | Withdraw one or wait for expiry | Yes | None | Failure line | Actor only | `open_out < 3` |
| `DPF-07` | “Diplomacy is paused while your government is in transition.” | `TRANSITION`/`CRISIS` freeze | Yes, after the state ends | Wait | Yes | None | Failure line | Actor only | The political state ends; deadlines were extended |
| `DPF-08` | “This cooldown is still running; you can act again on turn N.” | Posture or embargo cooldown | Yes, at the named turn | Wait | Yes | None | Failure line | Actor only | `current_turn ≥ eligible_turn` |
| `DPF-09` | “Your consultation pact requires a warning before this act.” | Missing or stale `DP-T02` notice | Yes, after notice + 12 turns | Send a notice, wait | Yes | None | Failure line | Actor only | A notice in the valid window exists |
| `DPF-10` | “You sent a notice to this nation too recently; the next is available on turn N.” | Notice cooldown | Yes | Wait | Yes | None | Failure line | Actor only | `current_turn ≥ notice_eligible` |
| `DPF-11` | “You already hold eight active agreements.” | Agreement cap | No | Terminate one or wait for expiry | Yes | None | Failure line | Actor only | `active(n) < 8` |
| `DPF-12` | “This agreement expired before the renewal could take effect.” | Renewal at/after expiry | No | Propose a new agreement | Yes (agreement already `EXPIRED`) | None | Failure line | Actor only | A new agreement object |
| `DPF-13` | “These terms are not valid for this agreement type.” | Malformed terms, type change, `A < 1` | No | Correct the proposal | Yes | None | Failure line | Actor only | Valid terms under the same type |
| `DPF-14` | “You broke this type of agreement with this nation recently; a new proposal is possible on turn N.” | Breach cooldown | Yes, at the named turn | Wait or use another type | Yes | None | Failure line | Actor only | `current_turn ≥ breach_eligible` |
| `DPF-15` | “An embargo requires hostile posture toward the target.” | Posture gate | Yes, after a posture change | Change posture (subject to `DPF-08`), then declare | Yes | None | Failure line | Actor only | Imposer holds `HOSTILE` |

### 8.2 B-02 codes used without duplication

| Code | Use in diplomacy | Why not a `DPF` code |
|---|---|---|
| `F1` | A scheduled aid cannot draw the reserved value at P4 | It is the engine's insufficient-resource code, not a diplomatic rule |
| `F2` | A prerequisite (pair clearance, active pact) disappeared between submission and P2 | The engine already owns prerequisite re-validation |
| `F3` | The target retired or became invisible before P2 | The engine already owns target validity |
| `F8` | The boundary was interrupted; the action retries with the turn | The only non-final code; B-08 §DIP-129 uses it for aid |
| `F9` | Same idempotency key with a different payload | A client bug; a new action needs a new key |

### 8.3 Transaction integrity rules

1. **One object, one outcome.** An action either commits its whole effect on its object or writes nothing but the failure line (DIP-104). A half-applied boundary is never visible.
2. **No partial delivery.** An aid either transfers `A` with matched ledger events or transfers nothing; there is no partial fill and no debt (DIP-040, F-DP-011).
3. **No activation without consent.** An agreement cannot reach `ACTIVE` unless both acceptances were recorded and valid at P2 (DIP-048).
4. **No duplicate consequence.** A retry returns the recorded outcome; a breach, a reservation and a public event are each written once (DIP-102, DIP-132).
5. **Publication follows success.** No public treaty event or success notification is written before the five steps commit (DIP-104).
6. **Failure is visible.** Every refusal writes one line to the actor with its code and rule; a silent rejection is a defect (DIP-133).
7. **Steps do not roll each other back.** A failure at step 3 does not undo an expiry committed at step 1 for a different object; each object's outcome is atomic (DIP-104).
8. **No resurrection.** A terminal object is never returned to `ACTIVE` by a retry, a late boundary or a recovery (DIP-126).

### 8.4 Recovery patterns

| Situation | Recovery | What must not happen |
|---|---|---|
| Transient `F8` turn interruption | The action stays accepted and retries when the turn resumes; one outcome | A second transfer or a second activation |
| P2 validation failure | The action is cancelled with its code; the object keeps its prior state; the player is told the cause | A partial reservation or a phantom notification |
| Notification delivery failure | The transaction stands; the notification retries; the record is not rolled back | Undoing a transfer to “fix” a message |
| Lost reservation before P4 | The payer is asked to re-confirm within 12 turns; otherwise `TERMINATED` `TRANSFER_VOIDED`, never `BREACHED` | Treating an operator event as a player breach |
| Duplicate submission | Same key returns the receipt; a new key is a new action | Silently applying it twice |
| Stale tab | The server rejects against current state; the UI refreshes to the terminal state | Client-side acceptance after expiry |
---

## 9. Authority and permission matrix

**9.1 The five authority sources, kept separate.**

| # | Source | What it authorizes | What it never authorizes |
|---|---|---|---|
| 1 | **The nation's owner** | Every diplomatic action for that nation (DIP-013) | Another nation's decision |
| 2 | **Another nation's owner** | Only its own nation's decisions | Anything for the first nation, even under a treaty |
| 3 | **System enforcement** | Activation, expiry, delivery, cleanup, validation (DIP-020) | Choosing a policy, a counterparty or a response |
| 4 | **Administrative authority** | Account suspension, pair restriction, content removal, restricted audit (DIP-079) | Signing, breaking, sanctioning or setting a posture for a nation |
| 5 | **Alliance authority** | **Nothing in B-08.** Prompt 09 owns alliance governance; `D-137` resolves zero delegation and no B-08 alliance-level treaty object; `D-140` authorizes a separate B-09 object (DIP-146…DIP-148) | Overriding a member's national diplomacy |

**9.2 The action-permission matrix.**

| Action | Nation owner | Delegated representative | Alliance leader | Alliance officer | Other alliance member | Other nation | System | Administrator |
|---|---|---|---|---|---|---|---|---|
| `A1 SET_POSTURE` | Own only | **None exists** | No | No | No | No | Never | No |
| `A2 SEND_CONSULT_NOTICE` | Own only | None | No | No | No | No | Never | No |
| `A3 PROPOSE_AGREEMENT` | Own only | None | No | No | No | No | Never | No |
| `A4 PROPOSE_AMENDMENT` | Party only | None | No | No | No | No | Never | No |
| `A5 PROPOSE_RENEWAL` | Party only | None | No | No | No | No | Never | No |
| `A6 PROPOSE_TERMINATION` | Party only | None | No | No | No | No | Never | No |
| `A7 ACCEPT_PROPOSAL` | Named addressee only | None | No | No | No | No | Never | No |
| `A8 REJECT_PROPOSAL` | Named addressee only | None | No | No | No | No | Never | No |
| `A9 WITHDRAW_PROPOSAL` | Proposer only | None | No | No | No | No | Never | No |
| `A10 BREAK_AGREEMENT` | Either party | None | No | No | No | No | Never | No |
| `A11 DECLARE_EMBARGO` | Own only, `HOSTILE` | None | No | No | No | No | Never | No |
| `A12 LIFT_EMBARGO` | Imposer only | None | No | No | No | No | Never | No |
| `A13 VIEW_DIPLOMACY` | Own view | None | Public fields only | Public fields only | Public fields only | Public fields only | Reads for processing | Restricted audit only |
| `A14 PUBLISH_REASON` | Party only, own reason | None | No | No | No | No | Never | No |

**9.3 Audit requirements by action.**

| Action | Audit class | Mandatory record |
|---|---|---|
| `A1` | I (public declaration) | `POSTURE_SET` with actor, target, from/to posture, turn |
| `A2` | S | `CONSULT_NOTICE_SENT` with sender, recipient, turn |
| `A3`–`A6` | S while pending; P on acceptance | Proposal identity, terms, version, expiry; acceptance event |
| `A7`/`A8` | P / S | Acceptance or rejection with turn and version |
| `A9` | S | Withdrawal with turn |
| `A10` | P | Breach with breaker, counterparty, type, version, rule |
| `A11`/`A12` | P | Embargo declaration/lift with imposer, target, term |
| `A13` | Ordinary read; privileged read audited | No player-visible record |
| `A14` | P | Published statement referencing the original event |

**9.4 Delegation is absent, not implied.** B-08 defines no ministers, officers, proxies or AI agents (DIP-015). A delegated act is `DPF-03`. `UD-039` is resolved by `D-137`: no delegation model is adopted, and B-08's refusal remains correct.

**9.5 What an alliance can and cannot do.**

| Situation | B-08 answer | Owner |
|---|---|---|
| Two allied nations sign a NAP | A normal nation-to-nation treaty; the alliance is not a party | B-08 |
| An alliance leader wants to accept for a member | Refused `DPF-03` | B-08 |
| An alliance wants its own treaty | No B-08 route; `D-137` confirms there is no B-08 alliance-level treaty object, and `D-140` authorizes a separate B-09 object | B-08 / `D-137` |
| A member leaves the alliance mid-treaty | The treaty persists; membership is not a B-08 field | B-08 / Prompt 09 |
| An alliance wants a collective embargo | No B-08 route; Prompt 09 would need its own act and a new decision | Prompt 09 |
| An alliance wants to see a member's pending terms | Refused; visibility is B-08's public/private split | B-08 / Prompt 09 |

---

## 10. Reputation and the breach record

**10.1 There is no score.** B-08 adopts no honour, trust, prestige, standing or "diplomatic points" value (DIP-084, DIP-157). This document does not add one and does not display a proxy for one. The only derived diplomatic number is the **breach count**.

**10.2 The one derived value.**

| Field | Rule |
|---|---|
| **Definition** | `breach_count(n, t)` = number of `AGREEMENT_BREACHED` events attributed to nation `n` with `t − 4380 < e.turn ≤ t` (F-DP-010) |
| **Purpose** | A factual public record of how many promises the nation broke in the last 365 days |
| **Scope** | Nation-scoped; dies with the nation on reroll; replacement starts at 0 (DIP-086) |
| **Events that affect it** | A `BREAK` only. Expiry, termination, rejection, dormancy, a voided turn and an operator recovery never increase it (DIP-075) |
| **Direction** | Only non-negative increments; no positive counterpart, no repair action, no purchase, no decay other than leaving the window |
| **Limits** | Non-negative integer; bounded in practice by the number of breaches in the window; no clamp is needed |
| **Duplicate prevention** | One breach event per agreement; the count is computed from events, never incremented by a client or a retry (DIP-076) |
| **Visibility** | Public on the nation page and in the treaty history; the retired nation's page keeps it (DIP-088, DIP-120) |
| **Mechanical effect** | **None.** It does not change approval, stability, tax, production, market access, war eligibility, proposal eligibility or any outcome (DIP-088) |
| **What it is not** | Not an input to any formula; not a reputation register; not an account record; not an enforcement sanction (DIP-089) |

**10.3 What the interface must say.** “Breaches in the last 4,380 turns: N.” Each event lists type, counterparty and turn. The page must not use the words score, rating, trust or standing, must not colour it as a moral judgement, and must not imply that a high count changes the rules. A retired nation's page says “retired” and keeps the record; the replacement's page says “new nation — no breaches”.

**10.4 UD-033 remains resolved as adopted.** The register records UD-033 as resolved by D-128 (no score; nation-scoped count; replacement at zero; limitation disclosed). This document does not reopen it and does not propose an account-level record. If evidence later shows reroll-laundering is material, that is a new decision, not a silent change (DIP-087).

**10.5 UD-039 is resolved by D-137.** There is no B-08 alliance-level treaty object and no delegation of a nation's diplomatic authority; `D-140` authorizes a separate B-09 object and transfers no national authority. B-08's refusal remains correct. A-02/A-03/A-06/A-10 in B-08 §18.2 remain the interface rows, now marked resolved.

---

## 11. Notifications and events

**11.1 The nine events are closed.** B-08 §13.3 defines `N1`–`N9`; this document adds none. Every workflow event maps to one of the nine, and an event with no notification is stated as such (for example, a view or a failed action).

| ID | Event | Trigger | Recipients | Timing | Required content | Confidentiality | Mandatory? | Failure blocks the transaction? | History |
|---|---|---|---|---|---|---|---|---|---|
| `N1` | Proposal received | `A3`–`A6` submission | Named counterparty | At submission | Type, proposer, deadline; **no terms in the subject line** | Parties only | Yes | No | Proposal record (class S) |
| `N2` | Proposal expiring soon | 12 turns before `expiry_turn` | Both parties | At the boundary | Expiry turn and the action still available | Parties only | Yes while a decision is open | No | Class S |
| `N3` | Proposal accepted | `A7` | Proposer | At acceptance | Activation boundary | Parties only | Yes | No | Private acceptance record |
| `N4` | Proposal rejected | `A8` | Proposer | At rejection | No reason unless the rejecter publishes one | Parties only | Yes | No | Class S |
| `N5` | Proposal withdrawn | `A9` | Counterparty | At withdrawal | No reason unless the withdrawer publishes one | Parties only | Yes | No | Class S |
| `N6` | Agreement activated / amended / renewed | Step 3 | Both parties; public record | P6 | Type, version, expiry | Public fields only | Yes | No | Class P |
| `N7` | Agreement expiring soon | 24 turns before expiry | Both parties | At the boundary | Expiry turn and the renewal route | Parties only | Yes while a decision is open | No | Class P |
| `N8` | Agreement terminated / breached / expired; aid settled / cancelled | Steps 1, 2, 4 | Both parties; public record for breach/expiry/settlement | P6 | Terminal state; who acted (break only); amount for aid | Public fields; private reason excluded | **Yes — cannot be suppressed** | No | Class P |
| `N9` | Embargo declared / lifted / expired | Step 5 | Both parties; public record | P6 | Scope summary and end turn | Public | **Yes — cannot be suppressed** | No | Class P |

**11.2 Mapping the prompt's event list to the nine.** "Amendment proposed" and "renewal requested" are `N1` (they are proposals); "amendment accepted" and "renewal accepted" are `N3`; "amendment activated" and "renewal activated" are `N6`; "obligation due" is not a separate notification — the agreement's activation `N6` already stated the delivery boundary, and `N8`/`AID_SETTLED` reports the outcome; "breach detected" has no separate detection event because the only breach is a player's `A10` or the owning system's B-2 event, both of which write the class-P breach and `N8`; "authorization revoked" is not a B-08 event (there is no delegation); "cooldown or eligibility failure" is a failure line to the actor, **not** a notification. Stating these absences is the point: an implementation must not invent `N10`–`N15`.

**11.3 Notification rules.**

1. **A notification is never consent.** Receiving, opening or ignoring `N1` changes nothing (DIP-062).
2. **A failed notification never changes treaty state.** The transaction stands or fails on its own validation; `N8`/`N9` retry (DIP-104).
3. **No private term crosses a notification boundary.** `N1`/`N2`/`N3` show only the recipient's own proposal; `N6`/`N8`/`N9` name parties and type, never a private note or another pair's terms (DIP-115).
4. **Consequences cannot be suppressed.** `N8`/`N9` always reach the affected player; digest preferences may group them, not hide them (DIP-116).
5. **One event, one notification.** A retry does not duplicate; a boundary groups by turn (DIP-114).
6. **Deadline warnings persist while a decision is open.** `N2`/`N7` may not be suppressed while the player has an unanswered proposal or an approaching expiry (DIP-116).

**11.4 Notification failure and retry.** A message that cannot be delivered is queued and retried; the record is written once. If delivery never succeeds, the in-game record and the overview remain authoritative, and the player sees the item on next login. A notification failure is never grounds to roll back an activation, a transfer or a breach.

---

## 12. Player experience and information design

**12.1 What this section is.** It specifies required content and behaviour, not a visual design. Prompt 13 owns the screens and the notification taxonomy (`UD-022`); this section tells Prompt 13 what must be true for diplomacy to be operable.

### 12.2 The six required views

| View | Required content | Must not show |
|---|---|---|
| **Diplomatic overview** | Own posture and each counterparty's; active agreements with expiry; incoming proposals awaiting a decision; outgoing proposals with deadline; upcoming deadlines; running cooldowns with exact eligible turns; active embargoes in both directions; breach count; recent class-P events | A projected outcome as fact; another pair's pending terms; a “score” |
| **Nation diplomatic profile** | Public posture both directions; public agreements; public history; published reasons; breach record; retired/new marker | Pending terms; private notes; another nation's treasury |
| **Treaty detail** | Parties; type; state; version and superseded history; activation; expiry/completion; obligations; scheduled actions; terminal event; the eligible actions | Hidden obligations; a stale “active” badge |
| **Proposal detail** | Sender; recipient; type; exact terms; expiry; required decision; consequences; current state; available actions | A preselected accept; a countdown that decides; terms that changed after submission |
| **Diplomatic history** | Each event with actor, type, turn, rule; public vs parties-only marker; corrections as new events; retired-page separation | An edited event; a deleted breach; a private reason without `A14` |
| **Confirmation panel** | Action; counterparty; type/version; every term; activation; expiry/completion; cost/reservation; public/private switch; breach consequence and cooldown; limits consumed; cancel path | Preselection; hidden term; “accept all”; dark pattern (DIP-082) |

### 12.3 The confirmation panel, field by field

Before a consequential action the panel shows, in this order: **(1)** what the player is authorizing; **(2)** which nation acts and which is affected; **(3)** any other nation affected; **(4)** resource consequences (aid amount and reservation); **(5)** obligations created; **(6)** duration/activation/expiry; **(7)** reversibility (withdraw before acceptance? break after?); **(8)** whether the counterparty's consent is required; **(9)** the exact limit the action consumes and the next eligible turn; **(10)** what the action does **not** do. The cancel path is always present, never styled as the destructive option, and the confirm button is never preselected.

### 12.4 The twelve B-08 handoff questions, answered

| # | Question (B-08 §21.4) | Answer in this document |
|---|---|---|
| 1 | Exact screen sequence for a proposal; where the deadline appears | §4 J1 steps 1–9; the deadline is on the review panel, the proposal detail and every `N1`/`N2` |
| 2 | How a pending version is displayed and compared | §4 J4; old and new terms side by side, the old version explicitly “still in force”, version number on both |
| 3 | What the break confirmation says, word for word | §4 J5 step 2; the permanent public record, the effect ending, count +1, 36-turn cooldown, no confiscation, no auto-retaliation |
| 4 | How the breach count is shown as a fact, not a score | §10.3; a sentence with a window and a number, no colour judgement, no “rating” |
| 5 | How an embargo's blocked route is explained to a trader | §4 J8 step 2 and §12.2; the market returns a neutral “blocked by an embargo between your nations” reason, no fee, no price change |
| 6 | What the recipient sees when an aid is terminated or voided | `N8` with “transfer did not occur — agreement terminated/voided”; no accusation, no breach for a voided turn |
| 7 | How `N2`/`N7` arrive when notifications are grouped | A persistent decision item in the overview; grouping may collapse the message but not the item (§11.3(6)) |
| 8 | A stale tab submitting after expiry | §8.4; server rejects `DPF-01`, UI refreshes to `EXPIRED`, no acceptance recorded |
| 9 | How a frozen deadline is shown | §2.4; “extended by N frozen turns, now turn X”, with the base and the extension separated |
| 10 | How a player sees an alliance cannot sign for it | §4 J7 and §9.5; the action is owner-only, an alliance role shows a read-only view, an attempt returns `DPF-03` |
| 11 | Empty state for a nation with no diplomacy | §12.5 |
| 12 | How a retired nation's history is reached without implying inheritance | §12.6 |

### 12.5 Empty and near-empty states

- **No agreements, no proposals:** “You have no diplomatic agreements. You can propose a non-aggression pact, a consultation pact or an aid agreement.” No fake statistics, no “trend”, no invented recommendation.
- **No incoming proposals:** “Nothing is waiting on you.” The outgoing section still shows deadlines.
- **No breach record:** “No breaches in the last 4,380 turns.” Not “perfect reputation” or a score.
- **A nation with one counterparty and no history:** the profile shows the public posture and an empty history, not a placeholder treaty.

### 12.6 Retired nations and replacements

A retired nation's page is reachable from the public history and is labelled **Retired**. It keeps its agreements' terminal records and its breach count. The replacement's page is a separate identity and says **New nation**; it does not link the old treaties as its own and does not inherit the count. A player who rerolls sees both pages, with the old one explicitly historical. This is the mitigation for the disclosed reroll escape (DIP-087), not a claim that the escape is closed.

### 12.7 Accessibility and error tone

Every failure sentence names the cause and the next eligible turn, never the counterparty's private state (DIP-083). Deadline and cooldown text must be readable without colour alone. A disabled action must say why it is disabled before the player clicks, not only after. A confirmation must not rely on a hover tooltip to disclose a term (DIP-081, DIP-082).

---

## 13. Abuse prevention and multiplayer integrity

**13.1 Classification.** Each row is **E** (existing approved safeguard), **P** (proposed here as a specification requirement, not yet approved gameplay), or **O** (open owner decision). No row invents a numeric limit: every numeric safeguard cites the B-08 limit it already has.

| # | Threat | Capability / exploit path | Prevention | Validation point | Audit | Recovery | Test | Class |
|---|---|---|---|---|---|---|---|---|
| 1 | Proposal spam | Send many proposals to many nations | Cap 3 outgoing (DIP-045); one per direction+type (DIP-044) | Submission and P2 | Proposal records | Withdraw/expire; no penalty | DPA-015, DPA-016 | E |
| 2 | Duplicate-proposal flooding | Re-submit the same proposal | Ordered key + idempotency key (DIP-102, DIP-124) | Submission | Failure line | Returns receipt | DPA-004, DPA-016 | E |
| 3 | Harassment by repeated requests | Re-propose after every rejection | Rejection is free but the cap and the 36-turn expiry bound volume; a player can ignore; no notification on view | Submission | Proposal records | Block/mute is a Prompt 12/13 question | DPA-017 | E / O |
| 4 | Reciprocal-proposal abuse | Both sides propose to create ambiguity | Ordered keys; first acceptance wins; loser `DPF-04` | P2 | Both records, one agreement | Loser may retry after terminal | DPA-018, DPA-026 | E |
| 5 | Acceptance replay | Replay a captured acceptance | Session authority + idempotency key; a duplicate returns the recorded receipt and writes nothing | Submission/P2 | One event | One agreement or applicable reservation | DPA-088, DPA-004 | E |
| 6 | Nation impersonation | Substitute a `nation_id` | Session ownership; object authorized, never identity | Every action | Failure line | None | DPA-008 | E |
| 7 | Unauthorized amendment | Craft an amendment to another's treaty | Party-only; P2 re-validation | Submission/P2 | Failure line | None | DPA-028 | E |
| 8 | Termination/cancellation manipulation | Break then claim mutual termination | Order: termination (step 1) beats break (step 2); one outcome | P4 | One terminal event | Loser `DPF-01` | DPA-032 | E |
| 9 | Expiry-race exploitation | Submit acceptance at the expiry boundary | Step 1 expiry wins; `DPF-01` | P2/P4 | `EXPIRED` only | New proposal | DPA-041 | E |
| 10 | Resource duplication | Duplicate aid acceptance/transfer | Reservation once; idempotency; one ledger pair (F-DP-011) | Acceptance/P4 | One completion | Reconcile by events | DPA-045, DPA-046 | E |
| 11 | Transfer replay | Retry a delivery after a voided turn | Idempotent by agreement+boundary; re-queue once | P4 | One `AID_SETTLED` | Retry or terminate `TRANSFER_VOIDED` | DPA-048 | E |
| 12 | Breach-count manipulation | Trigger/fake breaches to inflate another's count | Only `A10` or the owning system's B-2 writes a breach; one per agreement; count from events | Break/P4 | Class P breach | Correction is a new event; no silent decrement | DPA-049, DPA-051 | E |
| 13 | Reputation manipulation | Buy/grind a “score” | **No score exists**; count is factual and windowed | Display | — | — | DPA-050 | E |
| 14 | Embargo-cooldown circumvention | Lift and immediately re-declare | 12-turn cooldown from lift/expiry + imposer freeze (F-DP-008); same-boundary re-declare fails | Submission/P2 | Embargo records | Wait for eligible turn | DPA-055, DPA-057 | E |
| 15 | Alliance-authority abuse | Leader accepts/signs for a member | No delegation; `DPF-03`; `D-137` confirms zero delegation | Every action | Failure line | None | DPA-009, DPA-011 | E |
| 16 | Restricted-information disclosure | Alliance or admin view widens pending terms | One visibility class per field; parties-only pending terms (DIP-111, DIP-112) | Every read | Privileged read audited | Field absent | DPA-065, DPA-068, DPA-087 | E |
| 17 | Historical-record tampering | Edit/delete an event to hide a breach | Append-only; correction is a new event (DIP-119); privileged writes audited | Write path | Audit trail | New correction event | DPA-070 | E |
| 18 | Notification abuse | Flood a player with messages or leak a term in a subject | One event per action; nine fixed events; no private term in any; consequence notifications mandatory but bounded | Emission | Notification log | Retry/dedupe | DPA-061 | E |

**13.2 Numeric safeguards are not invented.** The only numbers in this chapter are B-08's: 3 outgoing proposals, 1 per direction+type, 8 active agreements, 36-turn response window, 12-turn posture cooldown, 12–36 notice window, 12-turn notice cooldown, 36-turn breach cooldown, 24-turn embargo, 12-turn re-imposition, 360-turn term, 4,380-turn breach window. None is described as balanced or final; all are Provisional for Prompt 14 (DIP-136).

**13.3 What remains an owner decision.** A block/mute feature for repeated diplomatic requests (row 3) is **not** in B-08 and would be a new mechanic; a rate limit beyond the declared caps would violate D-024's no-hidden-throttle rule; an account-level integrity record would reopen UD-033. These are recorded in §17, not assumed.
---

## 14. Acceptance-test matrix

**14.1 How to read a test.** Type **S** = specification scenario a later implementation must satisfy; **A** = arithmetic or document check that can run today; **R** = future runtime test requiring code and a test environment; **P** = future controlled playtest. **No R or P test has run.** Each row folds the prompt's seventeen fields into ten columns: `Preconditions · actor · input` covers preconditions/initial state/actor/input; `Steps` is the action; `Expected` covers resulting state, resource effect, notification and audit; `Prohibited` is the negative assertion; `Pass` is the objective pass condition. `DPW` and `DPE` name the workflow and edge case.

### 14.2 A — Authority and consent (`DPA-001`…`DPA-026`, `DPA-073`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-001` | 003 | — | DIP-013, DIP-025, DIP-023 | REQ-515, REQ-516 | Two active nations; A and B both default `NEUTRAL` | A sets `HOSTILE` | `POSTURE_SET`; exactly A→B becomes `HOSTILE`; B→A stays `NEUTRAL`; B notified; cooldown starts | A second posture record; B's posture changing | A→B `HOSTILE`; B→A `NEUTRAL`; one directional change |
| `DPA-002` | 006 | 002 | DIP-061 | REQ-521, REQ-523 | NAP pending and a `DP-T02` active; A's nation changes owner | Old session tries to accept; new owner accepts | `T02` persists unchanged; the pending NAP is not inherited; new owner's acceptance is valid | Treating the old owner's session as valid; transferring pending consent | `T02` still `ACTIVE`; only the new owner's acceptance recorded |
| `DPA-003` | 006 | 005 | DIP-102, DIP-130 | REQ-533 | Two sessions, same proposal submission | Both submit at once | One proposal; second returns the recorded outcome | Two proposals | One `PENDING` proposal exists |
| `DPA-004` | 006 | 006 | DIP-102, DIP-132 | REQ-533 | A submitted with key K | Resubmit same payload/key | Same receipt; no second object | A second reservation/event | Exactly one object and one event |
| `DPA-005` | 013 | 007 | DIP-013 | REQ-530 | C has no role in A or B | C tries to accept A→B | `DPF-03`; nothing changes | Any state change or notice to B | Proposal remains `PENDING` |
| `DPA-006` | 013 | 008 | DIP-013, DIP-125 | REQ-530 | Session lost ownership before submit | Submit acceptance | `DPF-03`; no acceptance | Resolving under old authority | No acceptance recorded |
| `DPA-007` | 013 | 009 | DIP-125 | REQ-530 | Confirmation open; the pair becomes restricted | Submit | Refused with the current code; nothing reserved | Accepting under stale state | No agreement, no reservation |
| `DPA-008` | 013 | 010, 052 | DIP-013 | REQ-530 | A crafts a request naming B's nation | Submit | `DPF-03` | Acting as B | No state change |
| `DPA-009` | 008 | 007 | DIP-015, DIP-148 | REQ-530 | Alliance leader, member has an incoming NAP | Leader accepts | `DPF-03`; member's owner may accept | Any alliance authority | Proposal stays `PENDING` |
| `DPA-010` | 013 | 007 | DIP-015 | REQ-530 | Any would-be delegate | Delegate accepts | `DPF-03` | An invented delegation model | Refused |
| `DPA-011` | 008 | 007 | DIP-146…DIP-148 | REQ-530 | Alliance leader/officer | Attempt every `A1`–`A12` for a member | All refused `DPF-03` | Any alliance override | Zero successful acts |
| `DPA-012` | 013 | 007 | DIP-019, DIP-079 | REQ-530 | Administrator session | Attempt to sign/break/embargo | Refused; an account measure only | A diplomatic act by an admin | No treaty/posture change |
| `DPA-013` | 006 | 011 | DIP-044, DIP-045 | REQ-517, REQ-521 | A owns Arcadia; B available; no live T01 | Propose `DP-T01` | `PENDING`, expiry `+36+freeze`; `N1` to B | Any reservation or obligation | Proposal exists; no agreement |
| `DPA-014` | 006 | 045 | DIP-037, DIP-123 | REQ-517 | A tries `from == to`, a fourth type, a retired target, or a removed target | Submit each | `DPF-13` for self/type; `DPF-02` for retired/removed | Any object | Refused, nothing created |
| `DPA-015` | 006 | 011 | DIP-045 | REQ-522 | A has 3 outgoing `PENDING` | Submit a fourth | `DPF-06`; no new proposal | A fourth object | Count stays 3 |
| `DPA-016` | 006 | 011 | DIP-044 | REQ-522 | A→B `DP-T01` pending | Submit A→B `DP-T01` again | `DPF-04` | A duplicate; a second agreement | One `PENDING` in that direction |
| `DPA-017` | 009 | 013 | DIP-049 | REQ-521 | A→B pending | B rejects | `REJECTED`; `N4`; cap released; no cooldown | Breach, penalty, public reason | `REJECTED`, no agreement |
| `DPA-018` | 012 | 016 | DIP-044, DIP-050 | REQ-522 | A→B and B→A `DP-T01` pending | B accepts A's | A's proposal `ACCEPTED`; B's fails `DPF-04` | Two agreements | One agreement, one loser |
| `DPA-019` | 011 | 011 | DIP-021, DIP-046 | REQ-522, REQ-523 | A→B pending at 1000; no answer | Advance to 1036 | `EXPIRED` at step 1; both notified once | Treating it as rejection/acceptance | `EXPIRED`, no agreement |
| `DPA-020` | 007 | 012 | DIP-062, DIP-080 | REQ-523 | B views A's proposal | View and close | Nothing changes; A not notified | A view being consent or a notice | No state/notification change |
| `DPA-021` | 008 | 011 | DIP-048, DIP-059 | REQ-521, REQ-523, REQ-533 | A→B pending; both valid | B accepts | `ACCEPTED`; at next boundary `ACTIVE`; `N3`/`N6` | Activation before the boundary | `ACCEPTED` then `ACTIVE`; expiry correct |
| `DPA-022` | 009 | 013 | DIP-049, DIP-132 | REQ-521, REQ-523 | B double-clicks reject | Second reject | `DPF-01`; one rejection event | Two rejection events | One terminal event |
| `DPA-023` | 010 | 014 | DIP-047 | REQ-521, REQ-523 | A→B pending | A withdraws | `WITHDRAWN`; `N5`; cap released | Obligation or cooldown | `WITHDRAWN`, no agreement |
| `DPA-024` | 010 | 015, 044 | DIP-048, DIP-056 | REQ-521, REQ-523 | A→B accepted | A tries to withdraw | `DPF-01`; agreement stands | Withdrawal after acceptance | Refused; agreement live |
| `DPA-025` | 011 | 017 | DIP-103, DIP-130 | REQ-523, REQ-533 | Acceptance recorded, then a rejection or withdrawal submitted for the same proposal at the boundary | Run P2/P4 | First recorded wins; the later rejection/withdrawal fails `DPF-01` | Two outcomes or a revived proposal | Exactly one outcome: `ACCEPTED` |
| `DPA-026` | 012 | 016 | DIP-050 | REQ-522 | Reciprocal proposals; both accepted in one boundary | Run P2 | Lower `(submitted_at, action_id)` wins; other `DPF-04` | Two agreements | One winner, one `EXPIRED` loser |
| `DPA-073` | 006 | 001 | DIP-046, DIP-100 | REQ-521, REQ-523 | A→B `DP-T01` `PENDING` at 1000; A logs out at 1005 | A takes no action; B opens at 1010; advance to expiry | Proposal stays `PENDING` to 1036; no logout marker is shown to B; the disconnect writes nothing | Expiring or withdrawing on disconnect; a presence notice to B | Proposal `EXPIRED` only at step 1 of 1036; no logout event |

### 14.3 B — Proposal and treaty lifecycle (`DPA-027`…`DPA-036`, `DPA-074`, `DPA-075`, `DPA-080`…`DPA-082`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-027` | 014 | 019 | DIP-063…DIP-066 | REQ-524 | NAP `ACTIVE` v1 | A proposes `AMEND` v2; B accepts | At step 3 v2 active, v1 `SUPERSEDED` | A silent replacement before activation | v1 in force until 1205, then v2 |
| `DPA-028` | 014 | 018 | DIP-063, DIP-125 | REQ-524 | `AMEND` pending; B's authority becomes invalid | P2 | Amendment fails; v1 remains | Binding v2 without consent | v1 still active |
| `DPA-029` | 018 | 019 | DIP-063, DIP-064 | REQ-524 | `AMEND` changes the term | B accepts | Only the accepted version applies | A material change without fresh consent | New version matches the shown terms |
| `DPA-030` | 015 | 021 | DIP-058, DIP-067 | REQ-525 | NAP expiry 1371; renewal accepted at 1370 | P4 at 1371 | Expiry step 1 wins; renewal `DPF-12` | Retroactive renewal | `EXPIRED`, not renewed |
| `DPA-031` | 019 | — | DIP-058, F-DP-009 | REQ-525 | Renewal accepted at 1350 | P4 at 1351 | Expiry becomes 1731; version unchanged | Version increment | `expiry 1731`, v1 |
| `DPA-032` | 016 | — | DIP-103, DIP-130 | REQ-526, REQ-533 | Termination accepted and break submitted for one boundary | P4 | `TERMINATED`; break `DPF-01`; no breach | A termination and a breach for one object | One terminal event |
| `DPA-033` | 016 | 020 | DIP-071 | REQ-526 | `ACCEPTED` aid with reservation; mutual termination | P4 | `TERMINATED`; reservation released; no transfer | Delivery or breach | Balance unchanged |
| `DPA-034` | 021 | — | DIP-072…DIP-077 | REQ-527 | NAP `ACTIVE` | A breaks before B's delivery boundary | `BREACHED`; public event; count +1; cooldown | Fine/confiscation/retaliation | One breach event; no value moved |
| `DPA-035` | 017 | 032, 041 | DIP-052, DIP-102 | REQ-533 | Agreement already active; duplicate activation event | Replay | Recorded outcome; no second activation | Two `ACTIVE` records | One active agreement |
| `DPA-036` | 022 | 042 | DIP-055, DIP-126 | REQ-521 | Agreement expired, and separately terminated | Attempt renewal/reopen on each | `DPF-12`/`DPF-01`; terminal state shown | Resurrection or an “active” badge | Terminal state unchanged for both |
| `DPA-074` | 015 | 021 | DIP-058, DIP-067 | REQ-525 | NAP `ACTIVE`, expiry 1371; renewal proposed at 1330 | B never responds; P4 at 1371 | Renewal request expires unanswered; agreement `EXPIRED` at 1371; no successor object | Auto-renewal or silence treated as consent | `EXPIRED`; no renewal |
| `DPA-075` | 025 | 026 | DIP-095, DIP-103 | REQ-529 | A declares an embargo at 1600 while directed trade offers A→B are open | One offer accepted at 1599, one at 1600; run P2/P4 | 1599 offer settles; 1600 offer fails on the market side; no retrofit and no fee | Blocking a settled trade or charging an embargo fee | One settled, one declined; no post-settlement balance change |
| `DPA-080` | 011 | 022, 053 | DIP-103, DIP-130 | REQ-522, REQ-533 | Proposal expires at 1036; acceptance submitted for the 1036 boundary | Run P2/P4 | Step 1 expiry wins; acceptance fails `DPF-01`; no agreement | Activating the expired proposal | `EXPIRED`; no agreement |
| `DPA-081` | 018 | 023 | DIP-103, F-DP-012 | REQ-524, REQ-533 | NAP v1 expiry 1205; amendment accepted for activation at 1205 | Run P4 | Expiry wins; amendment fails `DPF-01`; v1 `EXPIRED`; no v2 | Applying a version to an expired agreement | v1 `EXPIRED`; no version increment |
| `DPA-082` | 016 | 024, 053 | DIP-103, DIP-130 | REQ-526, REQ-533 | Mutual termination accepted for a boundary on which activation is also due | Run P4 | Step 1 termination wins; activation fails; `TERMINATED`; no activation event | Publishing activation and termination for one object | One terminal event |

### 14.4 C — Timing and freeze (`DPA-037`…`DPA-044`, `DPA-076`, `DPA-077`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-037` | 003 | 031 | DIP-027, F-DP-005 | REQ-516 | Posture changed at 1500 | Try at 1511, then 1512 | 1511 `DPF-08`; 1512 accepted | Off-by-one rejection | 1512 allowed |
| `DPA-038` | 003 | 027 | F-DP-005 | REQ-516, REQ-532 | Actor frozen 1504–1506 | Try 1514, then 1515 | 1514 `DPF-08`; 1515 accepted | Counterparty freeze extending it | 1515 allowed |
| `DPA-039` | 003 | 027 | F-DP-005 | REQ-516 | Counterparty frozen 1504–1506 | Try 1512 | Allowed | Extension from the other side's freeze | Eligible turn stays 1512 |
| `DPA-040` | 004 | — | F-DP-006a/6b | REQ-519 | Notice at 2000; no freeze | Try hostile act at 2011/2012/2036/2037 | 2011 `DPF-09`; 2012 pass; 2036 pass; 2037 `DPF-09` | Treating the minimum as extendable | Boundaries as listed |
| `DPA-041` | 011 | — | F-DP-004, DIP-105(a) | REQ-522, REQ-532, REQ-533 | Proposal submitted 1000; pair frozen 1010–1018 | Advance to expiry | Expiry 1045; 1044 not expired; 1045 `EXPIRED` | Counting overlapping freeze twice | 1045 |
| `DPA-042` | 011 | 030 | DIP-105(a) | REQ-532 | Both parties frozen on the same boundary, with one pair-scoped and one actor-scoped timer | Compute each extension | Pair +1; actor-scoped +1 for that actor only | +2 on either scope | Pair +1 and actor +1 |
| `DPA-043` | 021 | 025 | DIP-103, DIP-131 | REQ-527, REQ-533 | Aid due at the same boundary as a break | P4 | Break wins; delivery cancelled; reservation released; breach recorded | Delivery-then-breach | No transfer; one breach |
| `DPA-044` | 027 | — | DIP-094 | REQ-529 | Embargo declared 1600; either party frozen | Advance to 1624 | Term ends at 1624 | Freeze-extended term | Exactly 24 turns |
| `DPA-076` | 004 | 028 | F-DP-006a/6b, DIP-105(a) | REQ-519, REQ-532 | Notice at 2000; pair frozen 2010–2014; window 2012–2036 | Try a hostile act at 2012, 2036, 2041, 2042 | Minimum still 2012; end extends by 5 to 2041; 2012/2036/2041 valid; 2042 `DPF-09` | Extending the 12-turn minimum or shortening the end | 2012 minimum; 2041 end |
| `DPA-077` | 011 | 029 | DIP-105, F-DP-004 | REQ-532 | Proposal submitted 1000; pair frozen 1005–1009 and 1020–1022 | Compute expiry; advance to 1043/1044 | Union is 5+3=8 boundaries, counted once → expiry 1044; 1043 not expired; 1044 `EXPIRED` | Double-counting a boundary or adding wall-clock days | 1044 |

### 14.5 D — Resources and economy (`DPA-045`…`DPA-048`, `DPA-078`, `DPA-083`, `DPA-084`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-045` | 023 | — | F-DP-011 | REQ-520 | Payer 12,000 available; recipient 3,000; `A=5,000` | Accept, then deliver | Payer 7,000; recipient 8,000; one `transfer_id`; total 15,000 | Double transfer or fee | Conservation holds |
| `DPA-046` | 006 | 034 | DIP-040, F-DP-011 | REQ-520 | Payer has 4,999 available; `A=5,000` | Submit/accept | `DPF-05`; nothing reserved | Negative balance or credit | No agreement/reservation |
| `DPA-047` | 008 | 035/036/040 | DIP-132 | REQ-520 | Aid accepted and reserved; payer's available drops at P4 | P4 | Delivery fails atomically; reservation released; no debt; both notified; no delivery record | Partial delivery or a success record without value | No transfer; no negative balance; both notified |
| `DPA-048` | 023 | 033 | DIP-129, DIP-132 | REQ-520 | Delivery boundary voided (`F8`) | Retry at next boundary | Agreement returns to `ACCEPTED`; one delivery on retry | Two transfers or a breach | One `AID_SETTLED` |
| `DPA-078` | 023 | 039 | DIP-104, DIP-114 | REQ-520 | Aid due at P4; the transfer commits; the notification write fails | P4, then retry the notification | Transfer stands once; notification retried; no rollback; delivery event retained | Reversing a committed transfer to make notification consistent | One transfer; one delivery event; notification delivered |
| `DPA-083` | 023 | 037 | DIP-105, DIP-129 | REQ-520, REQ-532 | Aid `ACCEPTED` with reservation; payer enters `CRISIS` at 1500; delivery due 1505 | Advance through the freeze to 1510 | Delivery waits; deadline extended; no breach; reservation held; delivery at the first unfrozen boundary | Confiscating the reservation or failing the payer | Reservation intact; one delivery |
| `DPA-084` | 023 | 038 | DIP-102, DIP-132 | REQ-520, REQ-533 | Aid delivered at 1400 with `transfer_id` T | Replay the same transfer event | Idempotent by agreement + boundary; one ledger pair; one completion | Two transfers or two completion events | One transfer; total conserved |

### 14.6 E — Reputation and sanctions (`DPA-049`…`DPA-057`, `DPA-085`, `DPA-086`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-049` | 028 | — | F-DP-010 | REQ-528 | Breaches at 100, 200, 5000; current 4480 | Compute count | Lower bound 100 exclusive; count 1 | Counting 100 or 5000 | Count = 1 |
| `DPA-050` | 028 | 047 | DIP-076 | REQ-527, REQ-528 | One breach recorded | Replay break/report | `DPF-01`; count unchanged | Count +2 | Count = 1 |
| `DPA-051` | 021 | 046 | DIP-072, DIP-056 | REQ-527 | No breach occurred | Attempt a “report breach” route | No such action; `DPF-03`/`DPF-01` | Punishing on accusation | No event |
| `DPA-052` | 025 | — | DIP-026, DIP-093 | REQ-529 | A is `TENSE` toward E | Declare embargo | `DPF-15`; no act | Auto-changing posture | Refused |
| `DPA-053` | 025 | — | DIP-093(4), F-DP-008 | REQ-529 | Embargo ended at 1624 | Declare at 1635, then 1636 | 1635 `DPF-08`; 1636 accepted | Same-boundary re-declare | 1636 allowed |
| `DPA-054` | 025 | — | DIP-039a, DIP-031 | REQ-519, REQ-529 | `DP-T02` active; no notice | Set `HOSTILE` or declare | `DPF-09`; no hostile act | Auto-sending the notice | Refused |
| `DPA-055` | 027 | — | DIP-094, DIP-105 | REQ-529 | Embargo active at its term boundary | P4 | `EXPIRED` at step 5; `N9` | Freeze extension | Term ends exactly |
| `DPA-056` | 026 | — | DIP-098 | REQ-529 | Target of an embargo | Target attempts lift | `DPF-03`; embargo lives | Any target lift route | Refused; active |
| `DPA-057` | 027 | — | F-DP-008 | REQ-529 | Imposer frozen 1626–1627 | Declare at 1636/1637/1638 | 1636/1637 `DPF-08`; 1638 pass | Target freeze extending it | 1638 only |
| `DPA-085` | 028 | 048 | DIP-085, DIP-134 | REQ-528 | Two active agreements broken at 4480; current count 0 | Run the boundary; attempt a direct count edit and a replay | Each agreement contributes one event; count 2; the count is derived; edit/replay changes nothing | Counting one break twice or storing a hand-edited count | Count = 2; two events |
| `DPA-086` | 021 | 031 | F-DP-007, DIP-075 | REQ-527 | A breaks `DP-T01` at 2000; breach cooldown 36 turns | Propose a new `DP-T01` at 2035, then 2036 | 2035 `DPF-14`; 2036 accepted; the bound is inclusive | Off-by-one rejection at 2036 | 2036 allowed |

### 14.7 F — Security and multiplayer (`DPA-058`…`DPA-065`, `DPA-079`, `DPA-087`, `DPA-088`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-058` | 029 | — | DIP-022, DIP-105 | REQ-532 | Nation frozen | Try every `A1`–`A12` | All `DPF-07`; reads work; deadlines extended | Expiring its proposals | Read-only; no lost deadline |
| `DPA-059` | 030 | 003 | DIP-128 | REQ-531 | Nation becomes dormant or loses its active owner mid-NAP | Run cleanup | Open proposals expire; NAP persists; new proposals fail `DPF-02` | Breach or treaty termination | NAP still active; no active owner required |
| `DPA-060` | 030 | 004 | DIP-127 | REQ-531 | Nation rerolls | Run cleanup | All terminate/lift; reservation released; replacement neutral, count 0 | Transfer/inheritance | Clean state |
| `DPA-061` | 013 | — | DIP-083, DIP-133 | REQ-533 | Any failure | Trigger each `DPF` | One stable sentence with rule and next turn | Silent failure or private-state leak | Every code explained |
| `DPA-062` | 024 | 049 | DIP-078, DIP-119 | REQ-533 | A party publishes its reason | Publish; attempt edit | New class-P statement; original unchanged | Editing/deleting | Append-only |
| `DPA-063` | 006 | — | DIP-074 | REQ-517 | Pair `RESTRICTED` | Propose/accept | `DPF-02`/`DPF-13`; neutral reason | Any route around the restriction | Refused |
| `DPA-064` | 021 | — | DIP-074 | REQ-517 | Pair becomes restricted after activation | Run P2 | Agreement suspended, not breached; effect pauses | Breach event | Suspended, no breach |
| `DPA-065` | 002 | 054 | DIP-111, DIP-112 | REQ-012 | A/B have a pending aid proposal and a private history event; C is a third party and an alliance member | Read pending terms; query the pair's event history; query the public profile | Pending terms and the private history event are absent; only public active terms and public events are returned | Any private term or private history entry | Zero private fields or history entries; public fields only |
| `DPA-079` | 013 | 050 | DIP-013, DIP-079 | REQ-530 | A's owner is signed in; a crafted request sets `actor_nation_id=B` and `isAdmin=true` | Submit acceptance for B's proposal | Server re-derives authority from the session; `DPF-03`; no state change; the attempt is audited | Trusting the client flag; acting as B | Proposal `PENDING`; zero state change |
| `DPA-087` | 020 | 054 | DIP-111, DIP-114 | REQ-012, REQ-533 | A→B `DP-T03` pending with `A=5,000`; C is allied to B but is not a party | Emit `N1`; query C's notification feed; retry delivery | C receives no `N1` for A→B and no private field, amount, rejection reason or P2 data; the retry duplicates neither the notice nor the state; B's own notice is unchanged | Any private term or amount in C's payload; treating the notice as consent | C's payload has zero private fields; one notice per recipient; proposal still `PENDING` |
| `DPA-088` | 008 | 051 | DIP-059, DIP-102, DIP-134 | REQ-523, REQ-533 | A→B `DP-T01` `PENDING`; B is authorized; acceptance submitted with key K | B accepts with K; activate; replay the identical acceptance | First acceptance creates `ACCEPTED`, then exactly one `ACTIVE` agreement; replay returns the recorded receipt and writes nothing new | A second agreement, activation, event or consent record | One agreement, one acceptance event, one active record; the NAP has no reservation or transfer to duplicate |

### 14.8 G — Cross-system and governance (`DPA-066`…`DPA-072`)

| ID | DPW | DPE | B-08 rules | REQ | Preconditions · actor · input | Steps | Expected | Prohibited | Pass |
|---|---|---|---|---|---|---|---|---|---|
| `DPA-066` | 001 | — | DIP-106, D-024, DIP-002 | REQ-514, REQ-533 | A is `HOSTILE` toward B, holds an active NAP with B, and has an embargo on B | Open the overview; change posture; end the embargo | Posture, agreement and embargo appear as three independent records; changing posture does not alter the NAP; ending the embargo does not change the NAP; cooldowns show eligible turns | Collapsing the three into one status; a change to one silently changing another | All three records remain distinct; nine overview items present |
| `DPA-067` | 001 | — | DIP-107 | REQ-533 | A nation with no diplomacy | Open the overview | Empty state copy; no fake statistic | Invented recommendation | Empty state correct |
| `DPA-068` | 002 | 054 | DIP-108, DIP-113 | REQ-012, REQ-514 | One active agreement, one pending | Public view | Active public; pending absent | Pending terms public | Correct split |
| `DPA-069` | 028 | 004 | DIP-086, DIP-120 | REQ-528 | A retired nation and its replacement | View both pages | History retained on the old page; replacement 0 | Implied inheritance | Separate pages |
| `DPA-070` | 005 | 043 | DIP-117…DIP-119 | REQ-012, REQ-533 | Any event sequence, including one termination | Reconstruct; replay a duplicate termination; attempt an edit | One terminal event per object; every event has actor, turn, rule; corrections append | Edited/deleted event; two terminal events | Audit reconstruction succeeds; one termination |
| `DPA-071` | 020 | — | DIP-147, A-04 | REQ-517 | Two allied nations sign a NAP; one leaves | Membership change | NAP persists; alliance not a party | Treaty termination by membership | NAP unchanged |
| `DPA-072` | 001 | — | DIP-146…DIP-149 | REQ-530 | Alliance wants an alliance-level treaty or delegation | Attempt via B-08 | No route; `D-137` confirms no delegation and no alliance object | A B-08 alliance treaty or delegation | Refused/absent |

**14.9 Coverage.** 88 tests: **27** authority, consent and ownership (`DPA-001`…`DPA-026` plus `DPA-073`); **15** proposal and treaty lifecycle (`DPA-027`…`DPA-036` plus `DPA-074`, `DPA-075`, `DPA-080`…`DPA-082`); **10** timing and freeze (`DPA-037`…`DPA-044` plus `DPA-076`, `DPA-077`); **7** resources and economy (`DPA-045`…`DPA-048` plus `DPA-078`, `DPA-083`, `DPA-084`); **11** reputation and sanctions (`DPA-049`…`DPA-057` plus `DPA-085`, `DPA-086`); **11** security and multiplayer (`DPA-058`…`DPA-065` plus `DPA-079`, `DPA-087`, `DPA-088`); and **7** cross-system and governance (`DPA-066`…`DPA-072`). 27+15+10+7+11+11+7 = 88. Every `DPW-001`…`DPW-030` appears in at least one test; every `DPE-001`…`DPE-054` has an explicit row in §7.10; every `DPF-01`…`DPF-15` is exercised by at least one row. The tests are **designed, not executed** (DIP-151); the only executed evidence in this prompt is §19's document checks. **Two cases are PARTIAL**: `DPE-049` (the diplomacy-side publish/append-only behavior is asserted by `DPA-062`; operator correction is Prompt 12's) and `DPE-054` (restricted-field and notification paths are asserted by `DPA-065`, `DPA-068` and `DPA-087`; privileged-read audit is Prompt 12's under DIP-121).
---

## 15. Requirements traceability

**15.1 Scope.** B-08 created twenty diplomacy requirements, `REQ-514`…`REQ-533`, and the pre-existing `REQ-012` (typed, event-sourced, visibility-scoped bilateral relationships) is the earlier requirement diplomacy now fully specifies. This table accounts for all twenty-one. No requirement was added, renumbered or reopened by 08C; the counts stay **533** (**19 Approved / 507 Provisional / 5 Open / 2 Deferred**) and `REQ-012` stays **Provisional** (it names the shape, not the states; the states are now in B-08).

**15.1.1 Canonical traceability methodology (08C-E).** The project uses **exhaustive bidirectional traceability**, not a representative test list. `§15.1` is the requirement summary and `§15.5` is the authoritative exhaustive relationship ledger; the requirement text remains owned by the [requirements register](03_requirements_traceability.md), the test scenario and assertion remain owned by `§14`, and this document is authoritative for the Diplomacy-to-test links. Every relationship is one of:

- **DIRECT VERIFICATION** — the test scenario executes the requirement's named behaviour and its expected result would fail if that behaviour were absent. It is counted in the `§15.1` `Test` cell and in the direct totals.
- **SUPPORTING VERIFICATION** — the test exercises an adjacent rule and gives useful evidence, but does not by itself establish the whole requirement. It is listed in `§15.5` with an explicit statement of what it does **not** prove and is never counted as direct coverage.
- **DEFERRED** — the behaviour depends on a separately owned system or an unresolved approval. The dependency and next action are named; it is not counted as covered. `REQ-518` is the one deferred requirement (Prompt 10 owns war declarations).
- **NOT COVERED** — no qualifying test exists and no owner/dependency has been assigned. There are none in this catalogue; if one appears, it must be recorded with a required action rather than silently omitted.

A test may be direct for one requirement and supporting for another (for example `DPA-087` is direct for `REQ-012` and supporting for `REQ-533`). The `§15.1` `Test` cell lists **direct tests only**; supporting relationships exist solely in `§15.5`. Both directions are checked: every `DPA` requirement reference must appear in the ledger, every direct ledger row must appear in the requirement's `Test` cell, and the classifications must agree. An absent `DPE` row means a positive-path or boundary test with no distinct edge case; it is not an omission.

| REQ | Requirement (short) | Source | B-08 rule | Formula | Workflow | Edge case | Test | Verification | Status |
|---|---|---|---|---|---|---|---|---|---|
| `REQ-012` | Bilateral relationships are typed, event-sourced and visibility-scoped | P6 SYS-008; D-030 | DIP-002, DIP-023, DIP-108…DIP-119 | — | DPW-001, DPW-005 | DPE-054 | DPA-065, DPA-068, DPA-070, DPA-087 | Direct: private history and pending terms denied in `DPA-065`; public/private split in `DPA-068`; event provenance in `DPA-070`; non-party notification privacy in `DPA-087` | **Covered** (Provisional) |
| `REQ-514` | Three layers: directional posture, mutual agreement, separate effect | D-123 | DIP-002 | — | DPW-001, DPW-002 | — | DPA-066 | Direct: `DPA-066` shows posture, agreement and embargo as three independent records and changing one does not change another. `DPA-068` is supporting only (agreement/proposal visibility). | **Covered** |
| `REQ-515` | One directional public posture per pair; default `NEUTRAL` | D-123 | DIP-023, DIP-030 | — | DPW-003 | — | DPA-001 | Direct: both default `NEUTRAL`; A's change leaves B's posture untouched; exactly one directional record changes | **Covered** |
| `REQ-516` | Posture changes only by the owner; 12-turn cooldown; failure consumes none | D-123, DIP-027 | DIP-025…DIP-032 | F-DP-005 | DPW-003 | DPE-027 | DPA-037…DPA-039 | Document + arithmetic | **Covered** |
| `REQ-517` | Closed catalogue: `DP-T01`, `DP-T02`, `DP-T03`, `DP-A01` only | D-124 | DIP-037, DIP-038 | — | DPW-006, DPW-025 | DPE-045 | DPA-013, DPA-014 | Document + test design | **Covered** |
| `REQ-518` | An active NAP blocks a war declaration; enforced by Prompt 10, inert until then | D-124, D-023 | DIP-063, DIP-141 | — | DPW-020 | — | — | **Deferred:** B-08 publishes the permission hook and `DIP-141` declares it inert; no B-08 acceptance test can execute a war declaration. Prompt 10 owns enforcement and must call `DIP-063`/`DIP-141`. | **Deferred (Prompt 10)** |
| `REQ-519` | A consultation pact requires a 12–36-turn notice before hostility/embargo; 12-turn notice cooldown | D-124 | DIP-039a, DIP-031 | F-DP-006a/6b | DPW-004, DPW-025 | DPE-028 | DPA-040, DPA-054, DPA-076 | Direct: fixed-window boundaries in `DPA-040`; freeze-extended end and unchanged minimum in `DPA-076` | **Covered** |
| `REQ-520` | Aid is a one-off crown-only transfer, reserved at acceptance, delivered at P4 | D-124 | DIP-040, DIP-095, DIP-129 | F-DP-011 | DPW-006, DPW-008, DPW-023 | DPE-034…DPE-040 | DPA-045…DPA-048, DPA-078, DPA-083, DPA-084 | Document + arithmetic | **Covered** |
| `REQ-521` | Proposal lifecycle without draft/counter; immutable terms; accepted creates `ACCEPTED` agreement | D-125 | DIP-033…DIP-035, DIP-042…DIP-044 | F-DP-002/004 | DPW-006…DPW-011 | DPE-011, DPE-013…DPE-015, DPE-042, DPE-001 | DPA-013, DPA-017, DPA-021, DPA-022, DPA-023, DPA-024, DPA-036, DPA-073 | Direct: proposal creation, rejection, acceptance, withdrawal, terminal state and logout non-effect. Other proposal tests are supporting in §15.5. | **Covered** |
| `REQ-522` | One live proposal per direction+type; 3 outgoing; 36-turn expiry; reciprocal resolves by first acceptance | D-125, DIP-044 | DIP-044…DIP-046, DIP-050 | F-DP-001/002/004 | DPW-006, DPW-011, DPW-012 | DPE-011, DPE-016, DPE-022 | DPA-015, DPA-016, DPA-018, DPA-019, DPA-026, DPA-041, DPA-080 | Direct: cap, duplicate, reciprocal race, expiry, freeze extension and expiry boundary. | **Covered** |
| `REQ-523` | Both authenticated owners must accept the exact version; silence/expiry/dormancy/administration never consent | D-125, DIP-062 | DIP-059…DIP-062 | — | DPW-007, DPW-008, DPW-009 | DPE-002, DPE-011, DPE-012, DPE-001, DPE-051 | DPA-002, DPA-019, DPA-020, DPA-021, DPA-073, DPA-088 | Direct: ownership transfer, silence/expiry, view-only, explicit acceptance, logout and replayed acceptance. The other consent-adjacent tests are supporting in §15.5. | **Covered** |
| `REQ-524` | An amendment creates a version needing both parties; old terms remain until activation; type change is not an amendment | D-125 | DIP-063…DIP-066 | F-DP-012 | DPW-014, DPW-018 | DPE-018, DPE-019 | DPA-027…DPA-029, DPA-081 | Document + test design | **Covered** |
| `REQ-525` | Renewal is prospective from the old expiry and must activate before expiry; no automatic renewal | D-125 | DIP-058, DIP-067, DIP-068 | F-DP-009 | DPW-015, DPW-019 | DPE-021 | DPA-030, DPA-031, DPA-074 | Document + arithmetic | **Covered** |
| `REQ-526` | Mutual termination needs both and creates no breach; a party may instead break unilaterally | D-127 | DIP-056, DIP-057, DIP-069…DIP-071 | — | DPW-016, DPW-021 | DPE-020, DPE-024 | DPA-032, DPA-033, DPA-082 | Document + test design | **Covered** |
| `REQ-527` | A break writes a public breach, raises the count and applies a 36-turn cooldown; no confiscation or auto-retaliation | D-127 | DIP-072…DIP-077, DIP-131 | F-DP-007/010 | DPW-021, DPW-028 | DPE-025, DPE-047, DPE-031 | DPA-034, DPA-043, DPA-050, DPA-086 | Direct: public breach, break-before-delivery, duplicate prevention and inclusive cooldown boundary. `DPA-051` is supporting only (no false-report route). | **Covered** |
| `REQ-528` | No reputation score; only a nation-scoped public breach count over 4,380 turns, no mechanical effect, replacement at zero | D-128 | DIP-084…DIP-090 | F-DP-010 | DPW-028 | DPE-048, DPE-047, DPE-004 | DPA-049, DPA-050, DPA-069, DPA-085 | Direct: rolling-window count, duplicate prevention, replacement at zero and derived-count integrity. | **Covered** |
| `REQ-529` | One embargo: `HOSTILE` gate, 24 turns, public, blocks new directed trades and aid only, grandfathers accepted transfers, no fee | D-129 | DIP-091…DIP-099 | F-DP-008 | DPW-025…DPW-027 | DPE-026 | DPA-044, DPA-052…DPA-057, DPA-075 | Direct: gate, term, public record, market/aid block, grandfathering, lift and freeze rule. | **Covered** |
| `REQ-530` | Sole authority is the authenticated nation owner; no delegation; no administrator sign/break | D-126 | DIP-013…DIP-017, DIP-079 | — | DPW-003, DPW-021 | DPE-007…DPE-010 | DPA-005…DPA-012, DPA-072, DPA-079 | Direct: unauthorized actors, delegates, alliance leaders, administrators and a crafted request are refused; `DPA-072` proves there is no B-08 alliance delegation route (`D-137`). | **Covered** |
| `REQ-531` | No autonomous accept/reject/propose/declare/sanction/break/renew/posture; automatic acts are the closed list | D-126 | DIP-019, DIP-020, DIP-127…DIP-129 | — | DPW-011, DPW-017, DPW-022, DPW-023, DPW-030 | DPE-003, DPE-004 | DPA-059, DPA-060 | Direct: dormancy and reroll cleanup are the closed automatic acts; `DPA-058` is read-only freeze and belongs to `REQ-532`. | **Covered** |
| `REQ-532` | `TRANSITION`/`CRISIS` makes diplomacy read-only and extends deadlines rather than expiring them | D-126, DIP-105 | DIP-022, DIP-105 | F-DP-004…F-DP-009 | DPW-029 | DPE-027…DPE-030 | DPA-038, DPA-041, DPA-042, DPA-058, DPA-076, DPA-077, DPA-083 | Direct: read-only `DPA-058`; cooldown/window expiry extension in `DPA-038`, `DPA-041`, `DPA-076`; multi-block union in `DPA-077`; delivery deferral in `DPA-083` | **Covered** |
| `REQ-533` | Boundary resolution: P2 re-validation, P4 five-step band, P6 publication, P7 invariants, idempotency | D-131 | DIP-100…DIP-104, DIP-130…DIP-134 | — | DPW-011, DPW-017, DPW-022, DPW-023 | DPE-022…DPE-025, DPE-032, DPE-033, DPE-051 | DPA-003, DPA-004, DPA-021, DPA-025, DPA-032, DPA-035, DPA-041, DPA-043, DPA-070, DPA-080, DPA-081, DPA-082, DPA-084, DPA-088 | Direct: boundary order, re-validation, idempotency, activation, termination, publication and replay. Failure-message, append-only, overview and notification tests are supporting in §15.5. | **Covered** |

**15.2 Status counts.** 20 requirements **Covered** at the specification level; **1 Deferred** (`REQ-518`, because the NAP war-declaration effect cannot be enforced until Prompt 10); **0 partially covered, 0 not covered, 0 blocked by an owner decision**. "Covered" means a rule exists and at least one direct test is designed; it never means a runtime test passed. `REQ-012` is counted as the twenty-first row and remains Provisional. Of the 21 rows, **20 have direct acceptance coverage and 1 has none by design**; `REQ-518` is the deferred exception, not a silent gap.

**15.3 Formula traceability.**

| Formula | Purpose | Workflows | Tests | Current evidence |
|---|---|---|---|---|
| `F-DP-001` | Outgoing proposal count | DPW-006, DPW-009, DPW-010 | DPA-015 | Arithmetic in register §2; document check |
| `F-DP-002` | One live proposal per direction+type | DPW-006, DPW-012 | DPA-016, DPA-018 | Register example; document check |
| `F-DP-003` | Active agreement count | DPW-008, DPW-016 | DPA-021, DPA-033 | Register example; document check |
| `F-DP-004` | Proposal expiry with pair freeze | DPW-007, DPW-011 | DPA-019, DPA-041, DPA-042, DPA-077 | Worked example; boundary check |
| `F-DP-005` | Posture cooldown with actor freeze | DPW-003, DPW-029 | DPA-037…DPA-039 | Boundary + freeze check |
| `F-DP-006a/6b` | Notice validity and cooldown | DPW-004, DPW-025 | DPA-040, DPA-054, DPA-076 | Boundary check |
| `F-DP-007` | Breach cooldown with actor freeze | DPW-021 | DPA-034, DPA-086 | Boundary check |
| `F-DP-008` | Embargo term and re-imposition | DPW-025…DPW-027 | DPA-053…DPA-057 | Boundary check |
| `F-DP-009` | Agreement expiry and renewal | DPW-015, DPW-019, DPW-022 | DPA-030, DPA-031, DPA-036 | Boundary check |
| `F-DP-010` | Derived breach count | DPW-028 | DPA-049, DPA-050, DPA-069, DPA-085 | Rolling-window example |
| `F-DP-011` | Aid conservation | DPW-008, DPW-023 | DPA-045…DPA-048, DPA-078, DPA-083, DPA-084 | Conservation example |
| `F-DP-012` | Version increment | DPW-014, DPW-018 | DPA-027…DPA-029, DPA-035 | Example |

**15.4 Decisions and unresolved questions.**

| Record | Disposition in 08C |
|---|---|
| `D-123`…`D-132` | Applied; none reopened or reinterpreted |
| `DD-137`…`DD-146` | Applied; no design position changed |
| `UD-039` | **Resolved by D-137 (Prompt 09B)** — no B-08 alliance-level object and zero diplomatic delegation; `D-140` authorizes a separate B-09 object; 08C's refusal in DPA-072 remains correct |
| `UD-013`, `UD-033` | **Resolved** (D-124, D-128); not reopened; UD-033's nation-scoped count is displayed as a fact |
| `UD-022` | **Deferred, Prompt 13** — notification taxonomy; 08C fixes only the nine B-08 events |
| `UD-031` | **Deferred, Prompt 12/14** — reroll-review threshold; untouched |
| `DQ-04`, `DQ-13`, `DQ-14`, `DQ-15` | Research questions; no new answer claimed; owners remain Prompt 09/10/13 |
| Every numeric value | **Provisional, Prompt 14** — no value is balanced or final |

**15.5 Exhaustive bidirectional relationship matrix (08C-E).** This is the authoritative relationship ledger for Diplomacy acceptance traceability. The bold line above each table supplies the **Requirement ID and title**; each row supplies the acceptance test, relationship type, scenario, assertion evidence, edge case, B-08 rule and dependency. A row marked **DIRECT** counts as requirement coverage; a **SUPPORTING** row is evidence only and is never counted as verified coverage. A test may be direct for one requirement and supporting for another. **Totals:** 21 requirements, 88 tests, **117 test-pair rows** (101 DIRECT and 16 SUPPORTING), plus **one DEFERRED row** for `REQ-518` = 118 relationship rows. Twenty requirements have direct coverage; `REQ-518` has none by design.

**REQ-012 — Bilateral relationships are typed, event-sourced and visibility-scoped.** 4 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-065` | **DIRECT** | A/B have a pending aid proposal and a private history event; C is a third party and an alliance member → Read pending terms; query the pair's ev… | Pending terms and the private history event are absent; only public active terms and public events are returned | DPE-054 | DIP-111, DIP-112 | — | Designed |
| `DPA-068` | **DIRECT** | One active agreement, one pending → Public view | Active public; pending absent | DPE-054 | DIP-108, DIP-113 | — | Designed |
| `DPA-070` | **DIRECT** | Any event sequence, including one termination → Reconstruct; replay a duplicate termination; attempt an edit | One terminal event per object; every event has actor, turn, rule; corrections append | DPE-043 | DIP-117…DIP-119 | — | Designed |
| `DPA-087` | **DIRECT** | A→B `DP-T03` pending with `A=5,000`; C is allied to B but is not a party → Emit `N1`; query C's notification feed; retry delivery | C receives no `N1` for A→B and no private field, amount, rejection reason or P2 data; the retry duplicates neither the notice nor the state; B's own notice is unchanged | DPE-054 | DIP-111, DIP-114 | — | Designed |

**REQ-514 — Three layers: directional posture, mutual agreement, separate effect.** 1 direct, 1 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-066` | **DIRECT** | A is `HOSTILE` toward B, holds an active NAP with B, and has an embargo on B → Open the overview; change posture; end the embargo | Posture, agreement and embargo appear as three independent records; changing posture does not alter the NAP; ending the embargo does not change the NAP; cooldowns show eligible turns | — | DIP-106, D-024, DIP-002 | — | Designed |
| `DPA-068` | **SUPPORTING** | One active agreement, one pending → Public view | Active public; pending absent — **does not establish the whole requirement:** Confirms the agreement/proposal visibility split; it does not show posture, agreement and effect as three independent records. | DPE-054 | DIP-108, DIP-113 | — | Supporting only |

**REQ-515 — One directional public posture per pair; default `NEUTRAL`.** 1 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-001` | **DIRECT** | Two active nations; A and B both default `NEUTRAL` → A sets `HOSTILE` | `POSTURE_SET`; exactly A→B becomes `HOSTILE`; B→A stays `NEUTRAL`; B notified; cooldown starts | — | DIP-013, DIP-025, DIP-023 | — | Designed |

**REQ-516 — Posture changes only by the owner; 12-turn cooldown; failure consumes none.** 3 direct, 1 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-037` | **DIRECT** | Posture changed at 1500 → Try at 1511, then 1512 | 1511 `DPF-08`; 1512 accepted | DPE-031 | DIP-027, F-DP-005 | — | Designed |
| `DPA-038` | **DIRECT** | Actor frozen 1504–1506 → Try 1514, then 1515 | 1514 `DPF-08`; 1515 accepted | DPE-027 | F-DP-005 | — | Designed |
| `DPA-039` | **DIRECT** | Counterparty frozen 1504–1506 → Try 1512 | Allowed | DPE-027 | F-DP-005 | — | Designed |
| `DPA-001` | **SUPPORTING** | Two active nations; A and B both default `NEUTRAL` → A sets `HOSTILE` | `POSTURE_SET`; exactly A→B becomes `HOSTILE`; B→A stays `NEUTRAL`; B notified; cooldown starts — **does not establish the whole requirement:** Confirms an explicit, directional posture change; it does not test the 12-turn cooldown or that a failed change consumes none. | — | DIP-013, DIP-025, DIP-023 | — | Supporting only |

**REQ-517 — Closed catalogue: `DP-T01`, `DP-T02`, `DP-T03`, `DP-A01` only.** 2 direct, 3 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-013` | **DIRECT** | A owns Arcadia; B available; no live T01 → Propose `DP-T01` | `PENDING`, expiry `+36+freeze`; `N1` to B | DPE-011 | DIP-044, DIP-045 | — | Designed |
| `DPA-014` | **DIRECT** | A tries `from == to`, a fourth type, a retired target, or a removed target → Submit each | `DPF-13` for self/type; `DPF-02` for retired/removed | DPE-045 | DIP-037, DIP-123 | — | Designed |
| `DPA-063` | **SUPPORTING** | Pair `RESTRICTED` → Propose/accept | `DPF-02`/`DPF-13`; neutral reason — **does not establish the whole requirement:** Confirms a restricted pair has no route around the rule; it does not enumerate the closed treaty catalogue. | — | DIP-074 | — | Supporting only |
| `DPA-064` | **SUPPORTING** | Pair becomes restricted after activation → Run P2 | Agreement suspended, not breached; effect pauses — **does not establish the whole requirement:** Confirms a restriction suspends rather than breaches; it does not enumerate the closed treaty catalogue. | — | DIP-074 | — | Supporting only |
| `DPA-071` | **SUPPORTING** | Two allied nations sign a NAP; one leaves → Membership change | NAP persists; alliance not a party — **does not establish the whole requirement:** Confirms alliance membership does not make the alliance a treaty party; it does not enumerate the closed catalogue. | — | DIP-147, A-04 | — | Supporting only |

**REQ-518 — An active NAP blocks a war declaration; enforced by Prompt 10, inert until then.** 0 direct, 0 supporting, 1 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| — | **DEFERRED** | NAP permission hook is declared but inert until a war system exists | B-08/DIP-141 declares that a war declaration between NAP parties is not permitted; no B-08 acceptance test can execute a declaration. Prompt 10 must call the NAP check and record `BREACHED`. | — | DIP-063, DIP-141 | **Prompt 10 — warfare** | Deferred |

**REQ-519 — A consultation pact requires a 12–36-turn notice before hostility/embargo; 12-turn notice cooldown.** 3 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-040` | **DIRECT** | Notice at 2000; no freeze → Try hostile act at 2011/2012/2036/2037 | 2011 `DPF-09`; 2012 pass; 2036 pass; 2037 `DPF-09` | — | F-DP-006a/6b | — | Designed |
| `DPA-054` | **DIRECT** | `DP-T02` active; no notice → Set `HOSTILE` or declare | `DPF-09`; no hostile act | — | DIP-039a, DIP-031 | — | Designed |
| `DPA-076` | **DIRECT** | Notice at 2000; pair frozen 2010–2014; window 2012–2036 → Try a hostile act at 2012, 2036, 2041, 2042 | Minimum still 2012; end extends by 5 to 2041; 2012/2036/2041 valid; 2042 `DPF-09` | DPE-028 | F-DP-006a/6b, DIP-105(a) | — | Designed |

**REQ-520 — Aid is a one-off crown-only transfer, reserved at acceptance, delivered at P4.** 7 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-045` | **DIRECT** | Payer 12,000 available; recipient 3,000; `A=5,000` → Accept, then deliver | Payer 7,000; recipient 8,000; one `transfer_id`; total 15,000 | — | F-DP-011 | — | Designed |
| `DPA-046` | **DIRECT** | Payer has 4,999 available; `A=5,000` → Submit/accept | `DPF-05`; nothing reserved | DPE-034 | DIP-040, F-DP-011 | — | Designed |
| `DPA-047` | **DIRECT** | Aid accepted and reserved; payer's available drops at P4 → P4 | Delivery fails atomically; reservation released; no debt; both notified; no delivery record | DPE-035, DPE-036, DPE-040 | DIP-132 | — | Designed |
| `DPA-048` | **DIRECT** | Delivery boundary voided (`F8`) → Retry at next boundary | Agreement returns to `ACCEPTED`; one delivery on retry | DPE-033 | DIP-129, DIP-132 | — | Designed |
| `DPA-078` | **DIRECT** | Aid due at P4; the transfer commits; the notification write fails → P4, then retry the notification | Transfer stands once; notification retried; no rollback; delivery event retained | DPE-039 | DIP-104, DIP-114 | — | Designed |
| `DPA-083` | **DIRECT** | Aid `ACCEPTED` with reservation; payer enters `CRISIS` at 1500; delivery due 1505 → Advance through the freeze to 1510 | Delivery waits; deadline extended; no breach; reservation held; delivery at the first unfrozen boundary | DPE-037 | DIP-105, DIP-129 | — | Designed |
| `DPA-084` | **DIRECT** | Aid delivered at 1400 with `transfer_id` T → Replay the same transfer event | Idempotent by agreement + boundary; one ledger pair; one completion | DPE-038 | DIP-102, DIP-132 | — | Designed |

**REQ-521 — Proposal lifecycle without draft/counter; immutable terms; accepted creates `ACCEPTED` agreement.** 8 direct, 1 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-013` | **DIRECT** | A owns Arcadia; B available; no live T01 → Propose `DP-T01` | `PENDING`, expiry `+36+freeze`; `N1` to B | DPE-011 | DIP-044, DIP-045 | — | Designed |
| `DPA-017` | **DIRECT** | A→B pending → B rejects | `REJECTED`; `N4`; cap released; no cooldown | DPE-013 | DIP-049 | — | Designed |
| `DPA-021` | **DIRECT** | A→B pending; both valid → B accepts | `ACCEPTED`; at next boundary `ACTIVE`; `N3`/`N6` | DPE-011 | DIP-048, DIP-059 | — | Designed |
| `DPA-022` | **DIRECT** | B double-clicks reject → Second reject | `DPF-01`; one rejection event | DPE-013 | DIP-049, DIP-132 | — | Designed |
| `DPA-023` | **DIRECT** | A→B pending → A withdraws | `WITHDRAWN`; `N5`; cap released | DPE-014 | DIP-047 | — | Designed |
| `DPA-024` | **DIRECT** | A→B accepted → A tries to withdraw | `DPF-01`; agreement stands | DPE-015, DPE-044 | DIP-048, DIP-056 | — | Designed |
| `DPA-036` | **DIRECT** | Agreement expired, and separately terminated → Attempt renewal/reopen on each | `DPF-12`/`DPF-01`; terminal state shown | DPE-042 | DIP-055, DIP-126 | — | Designed |
| `DPA-073` | **DIRECT** | A→B `DP-T01` `PENDING` at 1000; A logs out at 1005 → A takes no action; B opens at 1010; advance to expiry | Proposal stays `PENDING` to 1036; no logout marker is shown to B; the disconnect writes nothing | DPE-001 | DIP-046, DIP-100 | — | Designed |
| `DPA-002` | **SUPPORTING** | NAP pending and a `DP-T02` active; A's nation changes owner → Old session tries to accept; new owner accepts | `T02` persists unchanged; the pending NAP is not inherited; new owner's acceptance is valid — **does not establish the whole requirement:** Confirms pending consent is not inherited on ownership change; it does not establish the full proposal state machine. | DPE-002 | DIP-061 | — | Supporting only |

**REQ-522 — One live proposal per direction+type; 3 outgoing; 36-turn expiry; reciprocal resolves by first acceptance.** 7 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-015` | **DIRECT** | A has 3 outgoing `PENDING` → Submit a fourth | `DPF-06`; no new proposal | DPE-011 | DIP-045 | — | Designed |
| `DPA-016` | **DIRECT** | A→B `DP-T01` pending → Submit A→B `DP-T01` again | `DPF-04` | DPE-011 | DIP-044 | — | Designed |
| `DPA-018` | **DIRECT** | A→B and B→A `DP-T01` pending → B accepts A's | A's proposal `ACCEPTED`; B's fails `DPF-04` | DPE-016 | DIP-044, DIP-050 | — | Designed |
| `DPA-019` | **DIRECT** | A→B pending at 1000; no answer → Advance to 1036 | `EXPIRED` at step 1; both notified once | DPE-011 | DIP-021, DIP-046 | — | Designed |
| `DPA-026` | **DIRECT** | Reciprocal proposals; both accepted in one boundary → Run P2 | Lower `(submitted_at, action_id)` wins; other `DPF-04` | DPE-016 | DIP-050 | — | Designed |
| `DPA-041` | **DIRECT** | Proposal submitted 1000; pair frozen 1010–1018 → Advance to expiry | Expiry 1045; 1044 not expired; 1045 `EXPIRED` | — | F-DP-004, DIP-105(a) | — | Designed |
| `DPA-080` | **DIRECT** | Proposal expires at 1036; acceptance submitted for the 1036 boundary → Run P2/P4 | Step 1 expiry wins; acceptance fails `DPF-01`; no agreement | DPE-022, DPE-053 | DIP-103, DIP-130 | — | Designed |

**REQ-523 — Both authenticated owners must accept the exact version; silence/expiry/dormancy/administration never consent.** 6 direct, 4 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-002` | **DIRECT** | NAP pending and a `DP-T02` active; A's nation changes owner → Old session tries to accept; new owner accepts | `T02` persists unchanged; the pending NAP is not inherited; new owner's acceptance is valid | DPE-002 | DIP-061 | — | Designed |
| `DPA-019` | **DIRECT** | A→B pending at 1000; no answer → Advance to 1036 | `EXPIRED` at step 1; both notified once | DPE-011 | DIP-021, DIP-046 | — | Designed |
| `DPA-020` | **DIRECT** | B views A's proposal → View and close | Nothing changes; A not notified | DPE-012 | DIP-062, DIP-080 | — | Designed |
| `DPA-021` | **DIRECT** | A→B pending; both valid → B accepts | `ACCEPTED`; at next boundary `ACTIVE`; `N3`/`N6` | DPE-011 | DIP-048, DIP-059 | — | Designed |
| `DPA-073` | **DIRECT** | A→B `DP-T01` `PENDING` at 1000; A logs out at 1005 → A takes no action; B opens at 1010; advance to expiry | Proposal stays `PENDING` to 1036; no logout marker is shown to B; the disconnect writes nothing | DPE-001 | DIP-046, DIP-100 | — | Designed |
| `DPA-088` | **DIRECT** | A→B `DP-T01` `PENDING`; B is authorized; acceptance submitted with key K → B accepts with K; activate; replay the identical acceptance | First acceptance creates `ACCEPTED`, then exactly one `ACTIVE` agreement; replay returns the recorded receipt and writes nothing new | DPE-051 | DIP-059, DIP-102, DIP-134 | — | Designed |
| `DPA-022` | **SUPPORTING** | B double-clicks reject → Second reject | `DPF-01`; one rejection event — **does not establish the whole requirement:** Confirms idempotent rejection; it does not establish acceptance, silence or exact-version consent. | DPE-013 | DIP-049, DIP-132 | — | Supporting only |
| `DPA-023` | **SUPPORTING** | A→B pending → A withdraws | `WITHDRAWN`; `N5`; cap released — **does not establish the whole requirement:** Confirms withdrawal before acceptance releases the cap; it is not evidence of consent formation. | DPE-014 | DIP-047 | — | Supporting only |
| `DPA-024` | **SUPPORTING** | A→B accepted → A tries to withdraw | `DPF-01`; agreement stands — **does not establish the whole requirement:** Confirms an accepted commitment cannot be withdrawn; it does not establish how consent was formed. | DPE-015, DPE-044 | DIP-048, DIP-056 | — | Supporting only |
| `DPA-025` | **SUPPORTING** | Acceptance recorded, then a rejection or withdrawal submitted for the same proposal at the boundary → Run P2/P4 | First recorded wins; the later rejection/withdrawal fails `DPF-01` — **does not establish the whole requirement:** Confirms the first recorded outcome wins; it does not assert both owners accepted the exact version. | DPE-017 | DIP-103, DIP-130 | — | Supporting only |

**REQ-524 — An amendment creates a version needing both parties; old terms remain until activation; type change is not an amendment.** 4 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-027` | **DIRECT** | NAP `ACTIVE` v1 → A proposes `AMEND` v2; B accepts | At step 3 v2 active, v1 `SUPERSEDED` | DPE-019 | DIP-063…DIP-066 | — | Designed |
| `DPA-028` | **DIRECT** | `AMEND` pending; B's authority becomes invalid → P2 | Amendment fails; v1 remains | DPE-018 | DIP-063, DIP-125 | — | Designed |
| `DPA-029` | **DIRECT** | `AMEND` changes the term → B accepts | Only the accepted version applies | DPE-019 | DIP-063, DIP-064 | — | Designed |
| `DPA-081` | **DIRECT** | NAP v1 expiry 1205; amendment accepted for activation at 1205 → Run P4 | Expiry wins; amendment fails `DPF-01`; v1 `EXPIRED`; no v2 | DPE-023 | DIP-103, F-DP-012 | — | Designed |

**REQ-525 — Renewal is prospective from the old expiry and must activate before expiry; no automatic renewal.** 3 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-030` | **DIRECT** | NAP expiry 1371; renewal accepted at 1370 → P4 at 1371 | Expiry step 1 wins; renewal `DPF-12` | DPE-021 | DIP-058, DIP-067 | — | Designed |
| `DPA-031` | **DIRECT** | Renewal accepted at 1350 → P4 at 1351 | Expiry becomes 1731; version unchanged | — | DIP-058, F-DP-009 | — | Designed |
| `DPA-074` | **DIRECT** | NAP `ACTIVE`, expiry 1371; renewal proposed at 1330 → B never responds; P4 at 1371 | Renewal request expires unanswered; agreement `EXPIRED` at 1371; no successor object | DPE-021 | DIP-058, DIP-067 | — | Designed |

**REQ-526 — Mutual termination needs both and creates no breach; a party may instead break unilaterally.** 3 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-032` | **DIRECT** | Termination accepted and break submitted for one boundary → P4 | `TERMINATED`; break `DPF-01`; no breach | — | DIP-103, DIP-130 | — | Designed |
| `DPA-033` | **DIRECT** | `ACCEPTED` aid with reservation; mutual termination → P4 | `TERMINATED`; reservation released; no transfer | DPE-020 | DIP-071 | — | Designed |
| `DPA-082` | **DIRECT** | Mutual termination accepted for a boundary on which activation is also due → Run P4 | Step 1 termination wins; activation fails; `TERMINATED`; no activation event | DPE-024, DPE-053 | DIP-103, DIP-130 | — | Designed |

**REQ-527 — A break writes a public breach, raises the count and applies a 36-turn cooldown; no confiscation or auto-retaliation.** 4 direct, 1 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-034` | **DIRECT** | NAP `ACTIVE` → A breaks before B's delivery boundary | `BREACHED`; public event; count +1; cooldown | — | DIP-072…DIP-077 | — | Designed |
| `DPA-043` | **DIRECT** | Aid due at the same boundary as a break → P4 | Break wins; delivery cancelled; reservation released; breach recorded | DPE-025 | DIP-103, DIP-131 | — | Designed |
| `DPA-050` | **DIRECT** | One breach recorded → Replay break/report | `DPF-01`; count unchanged | DPE-047 | DIP-076 | — | Designed |
| `DPA-086` | **DIRECT** | A breaks `DP-T01` at 2000; breach cooldown 36 turns → Propose a new `DP-T01` at 2035, then 2036 | 2035 `DPF-14`; 2036 accepted; the bound is inclusive | DPE-031 | F-DP-007, DIP-075 | — | Designed |
| `DPA-051` | **SUPPORTING** | No breach occurred → Attempt a “report breach” route | No such action; `DPF-03`/`DPF-01` — **does not establish the whole requirement:** Confirms no false-breach report route exists; it does not test a real break, public breach or cooldown. | DPE-046 | DIP-072, DIP-056 | — | Supporting only |

**REQ-528 — No reputation score; only a nation-scoped public breach count over 4,380 turns, no mechanical effect, replacement at zero.** 4 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-049` | **DIRECT** | Breaches at 100, 200, 5000; current 4480 → Compute count | Lower bound 100 exclusive; count 1 | — | F-DP-010 | — | Designed |
| `DPA-050` | **DIRECT** | One breach recorded → Replay break/report | `DPF-01`; count unchanged | DPE-047 | DIP-076 | — | Designed |
| `DPA-069` | **DIRECT** | A retired nation and its replacement → View both pages | History retained on the old page; replacement 0 | DPE-004 | DIP-086, DIP-120 | — | Designed |
| `DPA-085` | **DIRECT** | Two active agreements broken at 4480; current count 0 → Run the boundary; attempt a direct count edit and a replay | Each agreement contributes one event; count 2; the count is derived; edit/replay changes nothing | DPE-048 | DIP-085, DIP-134 | — | Designed |

**REQ-529 — One embargo: `HOSTILE` gate, 24 turns, public, blocks new directed trades and aid only, grandfathers accepted transfers, no fee.** 8 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-044` | **DIRECT** | Embargo declared 1600; either party frozen → Advance to 1624 | Term ends at 1624 | — | DIP-094 | — | Designed |
| `DPA-052` | **DIRECT** | A is `TENSE` toward E → Declare embargo | `DPF-15`; no act | — | DIP-026, DIP-093 | — | Designed |
| `DPA-053` | **DIRECT** | Embargo ended at 1624 → Declare at 1635, then 1636 | 1635 `DPF-08`; 1636 accepted | — | DIP-093(4), F-DP-008 | — | Designed |
| `DPA-054` | **DIRECT** | `DP-T02` active; no notice → Set `HOSTILE` or declare | `DPF-09`; no hostile act | — | DIP-039a, DIP-031 | — | Designed |
| `DPA-055` | **DIRECT** | Embargo active at its term boundary → P4 | `EXPIRED` at step 5; `N9` | — | DIP-094, DIP-105 | — | Designed |
| `DPA-056` | **DIRECT** | Target of an embargo → Target attempts lift | `DPF-03`; embargo lives | — | DIP-098 | — | Designed |
| `DPA-057` | **DIRECT** | Imposer frozen 1626–1627 → Declare at 1636/1637/1638 | 1636/1637 `DPF-08`; 1638 pass | — | F-DP-008 | — | Designed |
| `DPA-075` | **DIRECT** | A declares an embargo at 1600 while directed trade offers A→B are open → One offer accepted at 1599, one at 1600; run P2/P4 | 1599 offer settles; 1600 offer fails on the market side; no retrofit and no fee | DPE-026 | DIP-095, DIP-103 | — | Designed |

**REQ-530 — Sole authority is the authenticated nation owner; no delegation; no administrator sign/break.** 10 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-005` | **DIRECT** | C has no role in A or B → C tries to accept A→B | `DPF-03`; nothing changes | DPE-007 | DIP-013 | — | Designed |
| `DPA-006` | **DIRECT** | Session lost ownership before submit → Submit acceptance | `DPF-03`; no acceptance | DPE-008 | DIP-013, DIP-125 | — | Designed |
| `DPA-007` | **DIRECT** | Confirmation open; the pair becomes restricted → Submit | Refused with the current code; nothing reserved | DPE-009 | DIP-125 | — | Designed |
| `DPA-008` | **DIRECT** | A crafts a request naming B's nation → Submit | `DPF-03` | DPE-010, DPE-052 | DIP-013 | — | Designed |
| `DPA-009` | **DIRECT** | Alliance leader, member has an incoming NAP → Leader accepts | `DPF-03`; member's owner may accept | DPE-007 | DIP-015, DIP-148 | — | Designed |
| `DPA-010` | **DIRECT** | Any would-be delegate → Delegate accepts | `DPF-03` | DPE-007 | DIP-015 | — | Designed |
| `DPA-011` | **DIRECT** | Alliance leader/officer → Attempt every `A1`–`A12` for a member | All refused `DPF-03` | DPE-007 | DIP-146…DIP-148 | — | Designed |
| `DPA-012` | **DIRECT** | Administrator session → Attempt to sign/break/embargo | Refused; an account measure only | DPE-007 | DIP-019, DIP-079 | — | Designed |
| `DPA-072` | **DIRECT** | Alliance wants an alliance-level treaty or delegation → Attempt via B-08 | No route; `D-137` confirms no delegation | — | DIP-146…DIP-149 | — | Designed |
| `DPA-079` | **DIRECT** | A's owner is signed in; a crafted request sets `actor_nation_id=B` and `isAdmin=true` → Submit acceptance for B's proposal | Server re-derives authority from the session; `DPF-03`; no state change; the attempt is audited | DPE-050 | DIP-013, DIP-079 | — | Designed |

**REQ-531 — No autonomous accept/reject/propose/declare/sanction/break/renew/posture; automatic acts are the closed list.** 2 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-059` | **DIRECT** | Nation becomes dormant or loses its active owner mid-NAP → Run cleanup | Open proposals expire; NAP persists; new proposals fail `DPF-02` | DPE-003 | DIP-128 | — | Designed |
| `DPA-060` | **DIRECT** | Nation rerolls → Run cleanup | All terminate/lift; reservation released; replacement neutral, count 0 | DPE-004 | DIP-127 | — | Designed |

**REQ-532 — `TRANSITION`/`CRISIS` makes diplomacy read-only and extends deadlines rather than expiring them.** 7 direct, 0 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-038` | **DIRECT** | Actor frozen 1504–1506 → Try 1514, then 1515 | 1514 `DPF-08`; 1515 accepted | DPE-027 | F-DP-005 | — | Designed |
| `DPA-041` | **DIRECT** | Proposal submitted 1000; pair frozen 1010–1018 → Advance to expiry | Expiry 1045; 1044 not expired; 1045 `EXPIRED` | — | F-DP-004, DIP-105(a) | — | Designed |
| `DPA-042` | **DIRECT** | Both parties frozen on the same boundary, with one pair-scoped and one actor-scoped timer → Compute each extension | Pair +1; actor-scoped +1 for that actor only | DPE-030 | DIP-105(a) | — | Designed |
| `DPA-058` | **DIRECT** | Nation frozen → Try every `A1`–`A12` | All `DPF-07`; reads work; deadlines extended | — | DIP-022, DIP-105 | — | Designed |
| `DPA-076` | **DIRECT** | Notice at 2000; pair frozen 2010–2014; window 2012–2036 → Try a hostile act at 2012, 2036, 2041, 2042 | Minimum still 2012; end extends by 5 to 2041; 2012/2036/2041 valid; 2042 `DPF-09` | DPE-028 | F-DP-006a/6b, DIP-105(a) | — | Designed |
| `DPA-077` | **DIRECT** | Proposal submitted 1000; pair frozen 1005–1009 and 1020–1022 → Compute expiry; advance to 1043/1044 | Union is 5+3=8 boundaries, counted once → expiry 1044; 1043 not expired; 1044 `EXPIRED` | DPE-029 | DIP-105, F-DP-004 | — | Designed |
| `DPA-083` | **DIRECT** | Aid `ACCEPTED` with reservation; payer enters `CRISIS` at 1500; delivery due 1505 → Advance through the freeze to 1510 | Delivery waits; deadline extended; no breach; reservation held; delivery at the first unfrozen boundary | DPE-037 | DIP-105, DIP-129 | — | Designed |

**REQ-533 — Boundary resolution: P2 re-validation, P4 five-step band, P6 publication, P7 invariants, idempotency.** 14 direct, 5 supporting, 0 deferred.

| Test | Type | Scenario | Assertion evidence | Edge case | B-08 rule | Dependency | Status |
|---|---|---|---|---|---|---|---|
| `DPA-003` | **DIRECT** | Two sessions, same proposal submission → Both submit at once | One proposal; second returns the recorded outcome | DPE-005 | DIP-102, DIP-130 | — | Designed |
| `DPA-004` | **DIRECT** | A submitted with key K → Resubmit same payload/key | Same receipt; no second object | DPE-006 | DIP-102, DIP-132 | — | Designed |
| `DPA-021` | **DIRECT** | A→B pending; both valid → B accepts | `ACCEPTED`; at next boundary `ACTIVE`; `N3`/`N6` | DPE-011 | DIP-048, DIP-059 | — | Designed |
| `DPA-025` | **DIRECT** | Acceptance recorded, then a rejection or withdrawal submitted for the same proposal at the boundary → Run P2/P4 | First recorded wins; the later rejection/withdrawal fails `DPF-01` | DPE-017 | DIP-103, DIP-130 | — | Designed |
| `DPA-032` | **DIRECT** | Termination accepted and break submitted for one boundary → P4 | `TERMINATED`; break `DPF-01`; no breach | — | DIP-103, DIP-130 | — | Designed |
| `DPA-035` | **DIRECT** | Agreement already active; duplicate activation event → Replay | Recorded outcome; no second activation | DPE-032, DPE-041 | DIP-052, DIP-102 | — | Designed |
| `DPA-041` | **DIRECT** | Proposal submitted 1000; pair frozen 1010–1018 → Advance to expiry | Expiry 1045; 1044 not expired; 1045 `EXPIRED` | — | F-DP-004, DIP-105(a) | — | Designed |
| `DPA-043` | **DIRECT** | Aid due at the same boundary as a break → P4 | Break wins; delivery cancelled; reservation released; breach recorded | DPE-025 | DIP-103, DIP-131 | — | Designed |
| `DPA-070` | **DIRECT** | Any event sequence, including one termination → Reconstruct; replay a duplicate termination; attempt an edit | One terminal event per object; every event has actor, turn, rule; corrections append | DPE-043 | DIP-117…DIP-119 | — | Designed |
| `DPA-080` | **DIRECT** | Proposal expires at 1036; acceptance submitted for the 1036 boundary → Run P2/P4 | Step 1 expiry wins; acceptance fails `DPF-01`; no agreement | DPE-022, DPE-053 | DIP-103, DIP-130 | — | Designed |
| `DPA-081` | **DIRECT** | NAP v1 expiry 1205; amendment accepted for activation at 1205 → Run P4 | Expiry wins; amendment fails `DPF-01`; v1 `EXPIRED`; no v2 | DPE-023 | DIP-103, F-DP-012 | — | Designed |
| `DPA-082` | **DIRECT** | Mutual termination accepted for a boundary on which activation is also due → Run P4 | Step 1 termination wins; activation fails; `TERMINATED`; no activation event | DPE-024, DPE-053 | DIP-103, DIP-130 | — | Designed |
| `DPA-084` | **DIRECT** | Aid delivered at 1400 with `transfer_id` T → Replay the same transfer event | Idempotent by agreement + boundary; one ledger pair; one completion | DPE-038 | DIP-102, DIP-132 | — | Designed |
| `DPA-088` | **DIRECT** | A→B `DP-T01` `PENDING`; B is authorized; acceptance submitted with key K → B accepts with K; activate; replay the identical acceptance | First acceptance creates `ACCEPTED`, then exactly one `ACTIVE` agreement; replay returns the recorded receipt and writes nothing new | DPE-051 | DIP-059, DIP-102, DIP-134 | — | Designed |
| `DPA-061` | **SUPPORTING** | Any failure → Trigger each `DPF` | One stable sentence with rule and next turn — **does not establish the whole requirement:** Confirms stable failure sentences; it does not test P4 boundary order or P6 publication. | — | DIP-083, DIP-133 | — | Supporting only |
| `DPA-062` | **SUPPORTING** | A party publishes its reason → Publish; attempt edit | New class-P statement; original unchanged — **does not establish the whole requirement:** Confirms an append-only statement; it does not test boundary resolution or the five-step band. | DPE-049 | DIP-078, DIP-119 | — | Supporting only |
| `DPA-066` | **SUPPORTING** | A is `HOSTILE` toward B, holds an active NAP with B, and has an embargo on B → Open the overview; change posture; end the embargo | Posture, agreement and embargo appear as three independent records; changing posture does not alter the NAP; ending the… — **does not establish the whole requirement:** Confirms three independent records; it does not test boundary timing, idempotency or publication. | — | DIP-106, D-024, DIP-002 | — | Supporting only |
| `DPA-067` | **SUPPORTING** | A nation with no diplomacy → Open the overview | Empty state copy; no fake statistic — **does not establish the whole requirement:** Confirms the empty overview; it does not test boundary resolution. | — | DIP-107 | — | Supporting only |
| `DPA-087` | **SUPPORTING** | A→B `DP-T03` pending with `A=5,000`; C is allied to B but is not a party → Emit `N1`; query C's notification feed; retry delivery | C receives no `N1` for A→B and no private field, amount, rejection reason or P2 data; the retry duplicates neither the … — **does not establish the whole requirement:** Confirms notification privacy and idempotent retry; it does not establish the full boundary band or P6 publication. | DPE-054 | DIP-111, DIP-114 | — | Supporting only |

**15.6 No new requirement and no new decision.** 08C opens no `D-`, `DD-`, `REQ-` or `UD-` row. The workflows and tests are traceability artefacts; a future mechanic they cannot express must be recorded as a gap, not smuggled in as a test assumption.

---

## 16. Release-gate evidence

**16.1 The six approved gates are unchanged.** Global Trade's G-1…G-6 (D-122, DD-136, REQ-513) are market release gates; 08C does not touch them, does not mark any passed and does not reinterpret them as diplomacy gates. The current status is exactly as 07C left it: **G-1, G-2, G-3, G-5 and G-6 NOT MET; G-4 PARTIAL** (B-07 §9; 07C §10).

| Gate | Requirement | Current status | What diplomacy would need to demonstrate | 08C change |
|---|---|---|---|---|
| **G-1** | Identity and anti-multi integrity implemented | **NOT MET** | A restricted pair cannot treaty; a crafted account cannot act for another nation | None; DPA-005/008/063 are design cases, not evidence |
| **G-2** | Write-budget evidence | **NOT MET** | Measured rows per diplomatic action and per boundary | None; no implementation exists |
| **G-3** | Demonstrated interest and liquidity | **NOT MET** | Not a diplomacy gate; no inference from treaty counts | None |
| **G-4** | Reference-price readiness | **PARTIAL** | Not a diplomacy gate; an embargo must never alter a price (DIP-096) | None |
| **G-5** | Fee policy | **NOT MET** | Diplomacy charges no fee (DIP-009, DIP-096) | None |
| **G-6** | Operational feasibility | **NOT MET** | Dispute/abuse volume from treaties and embargoes | None |

**16.2 Evidence classes, stated separately.** This is where 08C can and cannot claim anything.

| Class | What it means | Current status for diplomacy |
|---|---|---|
| **Specification completeness** | Rules, workflows, states, permissions, failures and tests are written and cross-referenced | **Established by this document and B-08 v1.2**, subject to the checks in §19 |
| **Implementation completeness** | Code, schema, endpoints, jobs exist | **None.** D-012 forbids implementation in Stage 2 |
| **Automated test evidence** | Executable tests pass against code | **None for gameplay.** Only document validators run (§19) |
| **Manual acceptance evidence** | A person has executed a scenario against a build | **None** |
| **Security and abuse testing** | Adversarial tests against a deployed system | **None.** DPE-050…DPE-054 are designs |
| **Multiplayer and concurrency testing** | Two clients, races, reconnect, load | **None** |
| **Production readiness** | Deployment, operations, monitoring, support | **None**; no release date or commitment exists |
| **Playtest evidence** | Players understood consent, deadlines and consequences | **None.** Every UX statement in §12 is design analysis, not observed usability |

**16.3 Diplomacy release dependencies.** These are evidence dependencies, **not** decisions, dates or gates. `DP-RD-xx` identifiers are internal to this register.

| ID | Dependency | Owner | Blocks what | Evidence needed |
|---|---|---|---|---|
| `DP-RD-01` | Implementation of B-08's fourteen actions and five-step band | Stage 5/7 | Any runtime test | Code, schema, a deployed test environment |
| `DP-RD-02` | Prompt 10's war-declaration validator reads an active NAP | Prompt 10 | The NAP effect's only real consequence | A declaration blocked and a breach recorded when the check is bypassed |
| `DP-RD-03` | Prompt 09's alliance object and delegation decision | Prompt 09 | Any alliance-level treaty or delegated act — none exists after `D-137` | `D-137` resolution recorded; refusal tested by DPA-072 |
| `DP-RD-04` | Prompt 12's restricted audit and account measures | Prompt 12 | Administrator visibility, corrections, abuse handling | Audited privileged reads; a correction procedure |
| `DP-RD-05` | Prompt 13's screens and notification taxonomy | Prompt 13 | Player-facing confirmation, deadline display, digests | Screen specs implemented and usability-tested |
| `DP-RD-06` | Prompt 14's calibration | Prompt 14 | Any claim that a term or cooldown is balanced | Simulation and tuning evidence |
| `DP-RD-07` | Stage 3's measured write budget | Stage 3 | G-2-style operational evidence | Rows per action and per boundary at target scale |
| `DP-RD-08` | Security and abuse test harness | Stage 5/8 | Any security claim | Replay, tampering, race and leak tests against a build |
| `DP-RD-09` | Two-account and two-client concurrency test | Stage 7/8 | Any concurrency claim | Both clients act at one boundary; one outcome |
| `DP-RD-10` | Playtest of consent and deadline comprehension | Stage 8+ | Any usability claim | Observed players; no leading questions |

**16.4 What 08C cannot say.** It cannot say diplomacy is implemented, tested, balanced, secure, usable or ready to release. It cannot say a release gate passed. It cannot say Prompt 08 is complete in the sense of "built"; it is complete **as a specification** only if the acceptance gate in §19 passes.

---

## 17. Open owner decisions and unresolved questions

**17.1 No new owner decision is opened by 08C.** The following remain open, with their existing owners. None blocks the specification's acceptance; all block a later claim that the affected behaviour is final.

| ID / question | Why it matters | Current approved behaviour | Options | Impact on workflows/tests | Blocks implementation? | Recommendation |
|---|---|---|---|---|---|---|
| **UD-039 — resolved by `D-137`** | A whole class of treaty and any delegated act is undefined | B-08 publishes the nation object and refuses delegation; `D-137` confirms no B-08 alliance-level treaty object and zero delegation, while `D-140` authorizes a separate B-09 object | Resolved for B-08: no B-08 alliance object; no delegation; separate B-09 object under `D-140` | `DPW-001`/`DPW-008`/`DPW-021` have no alliance path; DPA-072 asserts the absence | No | `D-137`; not reopened |
| **UD-022** — notification/event-feed taxonomy | The nine events need a delivery taxonomy and grouping rules | B-08 fixes `N1`–`N9`; Prompt 13 owns the taxonomy | Candidate taxonomies in B-13 | `DPW-001` and §11 display the nine; grouping is unspecified | No (screens can use a provisional taxonomy) | Prompt 13 decides; 08C does not |
| **DQ-04 / DQ-14** — may a treaty drag a nation into war; is a declaration precondition? | Would create an MDP or a war gate B-08 does not have | No MDP; NAP is a permission block only | New decision with Prompt 10 | None of the 88 tests assumes an MDP | Yes, for any MDP | Prompt 10 decides; no inference |
| **DQ-13** — what may an alliance see of a member's diplomacy? | A visibility widening would need a B-08 amendment | Public active record; pending terms private | Alliance display of public fields only vs widening | DPA-065/068 assert the current split | No, unless widening is approved | Keep the split; Prompt 09 may display public only |
| **DQ-15** — may an alliance pool fund aid? | Would make a pool a party B-08 does not recognise | No; only a nation payer | Reuse the B-04 transfer with a nation payer, or a new pool object | DPA-045 uses a nation payer only | Yes, for pool-funded aid | Prompt 09/B-04 decide |
| **Repeated-request harassment** — is a block/mute needed? | Repeated proposals can annoy; B-08 has caps but no mute | Cap 3 outgoing, 36-turn expiry, free rejection; no mute | (a) no mute; (b) a Prompt 13 mute of notifications; (c) a block list with a new decision | No test assumes a mute; `DPE-003`/`DPA-017` bound volume | No | Prompt 12/13 consider; **not a B-08 mechanic** |
| **Every number** — terms, cooldowns, caps | Balance and player experience are unvalidated | Provisional structural defaults | Prompt 14 tuning | All boundary tests use the current values | No, but a value change edits rules + tests together | Prompt 14 |

**17.2 Research questions are not decisions.** `DQ-01`…`DQ-16` remain 08A's questions; 08B answered some and deferred others. 08C does not convert a `DQ-` item into a rule. `DCR-` items remain candidate recommendations, not requirements.

**17.3 What would reopen an accepted decision.** A new `D-` entry naming the decision, with evidence and owner authorization. A workflow inconvenience, a test failure caused by a missing system, or an implementation preference is **not** grounds to reopen D-123…D-132.

**17.4 What is explicitly not an open question.** Whether the player controls their own nation's diplomacy; whether silence is consent; whether an alliance can sign for a member; whether an administrator can break a treaty; whether a breach can be invented by a report. B-08 decides all five, and 08C's tests assert them. They are not candidates for trade-off.
---

## 18. Implementation handoff

**18.1 The authoritative sources, by question.**

| The implementation question | Authoritative source | This document's role |
|---|---|---|
| What is the rule? | [B-08](15_diplomacy.md) v1.2, `DIP-001`…`DIP-157` | Cites the rule; never restates a different one |
| How is it calculated? | [Formula register](15_diplomacy_formula_register.md) v1.2, `F-DP-001`…`F-DP-012` | Supplies the boundary tests; does not change a value |
| Who acts, in what order, and what does the player see? | **This document**, §3–§4 and §12 | Owns the workflow layer |
| Which authority and consent apply? | B-08 §3 and §9; this document §9 | Owns the operational matrix |
| Which states and transitions exist? | B-08 §5 and §4.2; this document §5 | Reconciles the prompt's candidate states; adds none |
| Which notifications and records? | B-08 §13–§14; this document §11 | Maps every workflow event to `N1`–`N9` |
| Which failures and recoveries? | B-08 §15; this document §8 | Adds recovery behaviour, no new code |
| What must a test assert? | **This document** §14 | Owns the acceptance matrix |
| What must another system provide? | B-08 §17–§18; this document §16 | Names the dependency and its owner |

**18.2 What a future implementation may build.**

- The fourteen actions (`A1`–`A14`) with their authority, validation, confirmation and idempotency.
- The proposal, agreement and embargo objects with the states and transitions in §5.
- The five-step boundary band, P2 re-validation, P6 publication and P7 invariants.
- The nine notifications, the visibility matrix and the class-P/S records.
- The breach count as a computed display value.
- The screens' content requirements in §12, within Prompt 13's design.

**18.3 What it must not invent.**

1. A delegation model, minister, officer or AI diplomat (DIP-015, `D-137`).
2. A reputation score, trust value, prestige or "diplomatic points" (DIP-084, DIP-157).
3. A counterproposal, draft state, mediation, ultimatum or trade treaty (DIP-033, DIP-034, DIP-037).
4. An automatic accept, reject, renewal, break, sanction or posture change (DIP-019, DIP-020).
5. A new failure code for an existing cause; use `DPF-01`…`DPF-15` or the B-02 `F` code.
6. A new notification event beyond `N1`–`N9`; Prompt 13 owns the taxonomy (UD-022).
7. A war rule, a market fee, a tariff, a price change or an asset freeze (DIP-096, DIP-141, D-129).
8. An alliance-level treaty object or collective sanction inside B-08 (DIP-146…DIP-149).
9. A partial aid delivery, debt, credit or instalment plan (DIP-040).
10. A block/mute/rate limit beyond the declared caps without a new decision (D-024).

**18.4 Recommended implementation sequence.** This is a dependency-aware recommendation for a later authorized phase, **not** permission to implement any of it now.

| Step | Build | Why it must come here | Exit test |
|---|---|---|---|
| 1 | Identity, nation ownership and pair-state reads (B-03) | Every action authorizes from the session and checks the pair | DPA-005, DPA-008, DPA-063 |
| 2 | Posture object and `SET_POSTURE` with cooldown | The simplest state machine; proves authority and freeze reads | DPA-001, DPA-037…DPA-039 |
| 3 | Proposal object and `A3`–`A9` | The lifecycle everything else references | DPA-013…DPA-026 |
| 4 | P2/P4 boundary band and idempotency | A wrong band corrupts every later step | DPA-025, DPA-032, DPA-035, DPA-041 |
| 5 | Agreement activation, expiry, amendment and renewal | The core treaty effect | DPA-021, DPA-027…DPA-036 |
| 6 | Aid reservation and delivery with B-04 | The only value movement; conservation is non-negotiable | DPA-045…DPA-048 |
| 7 | Break, breach record and breach count | The unilateral exit and its consequence | DPA-034, DPA-049, DPA-050 |
| 8 | Consultation notice gate and embargo | The two coercive/constraint mechanisms | DPA-040, DPA-052…DPA-057 |
| 9 | Notifications and visibility | Players cannot act safely without deadlines and consequences | DPA-061, DPA-065, DPA-068 |
| 10 | History, corrections and retired pages | Auditability and the reroll disclosure | DPA-069, DPA-070 |
| 11 | Freeze, dormancy and reroll cleanup | Cross-system account events; must not corrupt treaties | DPA-058…DPA-060 |
| 12 | Alliance interface and Prompt 10 hook | Only after both owners publish their rules | DPA-071, DPA-072 |

**18.5 Definition of done for any slice.** A slice is done only when: (a) its rules are cited; (b) its tests in §14 exist as executable tests; (c) every failure path asserts the unchanged state; (d) the record proves actor, turn and rule; (e) the confirmation shows every consequence; (f) no new mechanic appears without a decision. A green unit test that asserts only the happy path does not satisfy (c).

**18.6 The one-sentence handoff.** **Implement B-08's rules through this document's workflows and tests; when a question is not answered by those two sources, stop and record it as a gap rather than inventing a diplomatic rule.**

**18.7 What the implementation must never do to pass a test.** Weaken an assertion, suppress a failure code, treat a timeout as success, delete a public event, skip the P2 re-validation, or make the confirmation auto-accept "for convenience". A test suite that passes by removing the consent step is evidence of a defect, not of completion.
---

## 19. Acceptance, validation and handoff

### 19.1 Prompt 08C acceptance checklist

Every criterion in the Prompt 08C acceptance gate, with the artefact that satisfies it. "Satisfied" means met **at the specification and documentation level**; it never means implemented, runtime-tested or release-approved.

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | All major Diplomacy workflows are specified | **Satisfied** | `DPW-001`…`DPW-030`, each with 23 fields |
| 2 | Player journeys are complete enough to follow without inventing behaviour | **Satisfied** | §4 J1–J8; §3 fields 8–11 |
| 3 | Proposal and consent state transitions are explicit | **Satisfied** | §5.1–§5.4; `PT-01`…`PT-08`, `AT-01`…`AT-10`, `ET-01`…`ET-05` |
| 4 | Every approved treaty type has a lifecycle and workflow definition | **Satisfied** | §6 matrix; `DPW-014`…`DPW-027` |
| 5 | Player authority is preserved throughout | **Satisfied** | §2.5–§2.6, §9; every journey states why; DPA-001…DPA-012, DPA-079 |
| 6 | Bilateral consent is explicit and cannot be inferred from silence | **Satisfied** | §2.6, §5, §11.3; DPE-011/012; DPA-019/020 |
| 7 | The authority and permission matrix is complete | **Satisfied** | §9.2–§9.3; 8 actor columns, `A1`–`A14` |
| 8 | The edge-case catalogue covers the required scenarios | **Satisfied with two documented external dependencies** | `DPE-001`…`DPE-054`; audited matrix §7.10 (52 covered, 2 partial); `DPE-054`'s three disclosure scenarios are covered by `DPA-065`/`DPA-068`/`DPA-087`, with only its privileged-read audit deferred to Prompt 12 (§7.10a) |
| 9 | Failure and recovery behaviour is specified | **Satisfied** | §8.1–§8.4; `DPF-01`…`DPF-15` plus B-02 `F` codes |
| 10 | Notification and event requirements are complete | **Satisfied** | §11.1–§11.4; `N1`–`N9`, no tenth event |
| 11 | Cross-system interfaces are documented | **Satisfied** | §3, §16.3; B-08 §17–§18 preserved |
| 12 | Alliance governance remains owned by Prompt 09 | **Satisfied** | §9.5, §17.1; DPA-072; `D-137` records no alliance object and zero delegation |
| 13 | Abuse prevention requirements are documented | **Satisfied** | §13.1 (18 scenarios) |
| 14 | Acceptance tests cover positive and negative behaviour | **Satisfied** | §14, `DPA-001`…`DPA-088`, each with a prohibited result |
| 15 | Requirements traceability is complete or exceptions documented | **Satisfied** | §15; 20 directly covered, 1 deferred (`REQ-518`), 0 unmapped; exhaustive ledger §15.5 (101 DIRECT / 16 SUPPORTING / 1 DEFERRED) |
| 16 | Release-gate evidence is accurately classified | **Satisfied** | §16; G-1…G-6 unchanged; eight evidence classes |
| 17 | Unresolved owner decisions are not silently assumed | **Satisfied** | §17; `D-137` (UD-039 resolved), `UD-022`, `DQ-04`, `DQ-13`…`DQ-15` |
| 18 | Implementation handoff is complete | **Satisfied** | §18.1–§18.7 |
| 19 | Documentation validators and relevant regression checks pass | **Verified below** | §19.3 |
| 20 | Earlier Stage 2 work and Global Trade scope remain intact | **Satisfied** | §15.4, §16.1; no `MKT-`/`ECN-`/`URB-`/`DMP-`/`TR-` rule edited |

**Acceptance treatment of the two PARTIAL rows.** `DPE-049` and `DPE-054` are not counted as covered. Their diplomacy-side behaviour is tested (`DPA-062` for the append-only/public statement; `DPA-065`, `DPA-068` and `DPA-087` for the three disclosure scenarios), while the remaining operator-correction and privileged-read-audit paths are explicitly assigned to Prompt 12 by `DIP-121`/D-042. They are therefore **documented external dependencies**, not unhandled mandatory gaps; the acceptance standard is not relaxed, and the combined `DPE-054` row stays PARTIAL precisely because one promised outcome is outside B-08. No human reviewer or runtime test is claimed.

**Verdict: PASS at the specification level, with two documented external dependencies.** The diplomacy system is now specified from the player's perspective and the system's operational perspective. `DPE-049` (operator correction) and the privileged-read audit inside `DPE-054` remain Prompt 12's; neither is claimed as covered or implemented. The system is **not implemented, not runtime-tested, not balanced and not release-approved**.

### 19.2 What this prompt deliberately did not do

- No diplomacy code, database, migration, endpoint, screen, scheduler or deployment (D-012).
- No new treaty type, sanction, reputation score, delegation model or failure code.
- No change to a B-08 rule, value or decision; `D-123`…`D-132` and `DD-137`…`DD-146` stand.
- No reopening of `UD-013`/`UD-033`; `D-137` subsequently resolved `UD-039`, and this historical scope statement is not reopened.
- No change to D-122, DD-136, REQ-513, any `MKT-` rule or G-1…G-6.
- No execution of any `R` or `P` test in §14; only the document checks in §19.3 ran.

### 19.3 Validation record

**Commands run from `docs/qa_backups/` on 2026-10-30, after the final edit.** These are document, structural and arithmetic checks. No game server, database, scheduler, browser or runtime exists, so no runtime, load, concurrency, security, accessibility or play test has run.

| Command | Actual result |
|---|---|
| `python verify_diplomacy_workflows.py` | **17 groups checked, 0 failed** — sections, 30 workflows × 23 fields, 54 edge cases, 88 tests, §14 heading ranges, 54-row coverage matrix, targeted `DPE-051`/`DPE-054` and `REQ` guards, internal references, §15.5 bidirectional traceability (21 groups; 117 pairs + 1 deferred; direct/supporting/group totals and duplicate detection), formulas, notifications, failure codes, states, authority, gates, counts |
| `python verify_diplomacy_workflows.py --self-test` | **31/31** — 28 defect guards each detected their injected defect, the clean-document fixture, the five/seven progress-log guard, the clean-log fixture and the clean ledger. The guards include DPE-054 marked COVERED while its audit is deferred, loss of its notification test, a primary DPE→DPA link not mirrored in the test row, DPE-051 falling back to generic idempotency, the REQ-514/REQ-515 mismatches, an omitted supporting test, a missing ledger row, a supporting row wrongly counted as direct, a wrong group count, a requirement summary that counts a supporting test as direct, and a duplicate relationship |
| `python verify_diplomacy_numbers.py` | **9 groups checked, 0 failed** — B-08 structure, filenames, band, keys, freeze arithmetic, rolling window, posture matrix, references, cooldowns |
| `python verify_diplomacy_numbers.py --self-test` | **15/15** — 14 defect guards plus the clean fixture |
| `python validate_final.py` | **ALL CHECKS PASSED** |
| `python validate_final.py --self-test` | **10/10** guards detect their defect |
| `python test_next_action.py` | **23 tests OK** |
| `python test_decision_registers.py` | **12 tests OK** |
| `python 09_validate.py` | **348/348** |
| `python verify_politics_numbers.py` | **879/879** |
| `python verify_politics_numbers.py --self-test` | **18/18** guards detect their defect |
| `python verify_market_workflows.py` | **14 checks, 0 failed** — 237 rules, 237 matrix rows, 83 tests |
| `python verify_market_workflows.py --self-test` | **8/8** |
| `python verify_market_numbers.py` | **ALL CHECKS PASSED** (95/95); `--self-test` **14/14** |
| `python verify_economy_numbers.py` | **164/164** |
| `python verify_city_numbers.py` | **267/267** |

**What the checks prove.** The workflow validator proves that the document contains 30 workflows with all 23 fields, 54 edge cases, 88 tests whose every workflow/edge-case/rule/requirement reference resolves, §14 headings that list exactly the rows beneath them, a 54-row coverage matrix with a valid status and a concrete assertion per row, 21 requirement rows whose direct-test links match the §15.5 ledger (including bare `DPA-080…DPA-082` ranges) and whose verification cells state a rationale, all twelve formula rows, exactly nine notifications, exactly fifteen failure codes, no re-introduced proposal state, the authority/silence/Prompt 09 statements and five `NOT MET` plus one `PARTIAL` gate. The ledger check also proves the reverse direction: every test-side `REQ-` claim appears in the ledger, every ledger pair appears in its test row, and every direct/supporting classification agrees with the requirement summary. It also proves that `DPE-051` names `DPA-088`, that `DPE-054` names `DPA-087` and remains PARTIAL while naming Prompt 12, and that the five 08C-D requirement rows carry their supporting tests. The B-08 validator proves the rulebook it cites is still v1.2-correct. The continuity validators prove the registers, roadmap, handoff and progress log agree.

**Semantic coverage review.** The 08C-C audit did not treat identifier presence as coverage. Each `DPE` row in §7.10 was compared by the agent (AI) against the preconditions, trigger and expected result of the named `DPA` row, and the assertion column records the comparison. The 08C-D pass re-read `DPE-051` and all three `DPE-054` scenarios separately (§7.10a). The 08C-E pass re-read all 88 test-side `REQ-` cells against the 21 requirement rows, classified every relationship, and built §15.5 from the test rows rather than from the summary. `DPA-041` is DIRECT for `REQ-532`; `DPA-087` is DIRECT for `REQ-012` and SUPPORTING for `REQ-533`; `DPA-088` is DIRECT for both `REQ-523` and `REQ-533`. This is a document review, **not** an independent human sign-off and **not** an execution of the test. `DPE-049` is recorded as PARTIAL because its operator-correction path belongs to Prompt 12; `DPE-054` is PARTIAL because the privileged-read audit also belongs to Prompt 12. No B-08 test can assert either deferred path.

**What they do not prove.** No transaction, concurrency, race, load, security, penetration, usability, balance or player-experience result. A green document check is not a passed game test (DIP-151).

### 19.4 Scope confirmation

**No implementation occurred.** The only files created or changed are Markdown specifications and the Python document-QA scripts that check them. No application code, database schema, migration, API, screen, job, hosting change or deployment exists. No owner decision was made, no requirement renumbered and no gate passed.

### 19.5 Next authorized task

**Stage 2, Prompt 09 — Alliance system and alliance management** (`16_alliances.md`), as recorded in the Stage 2 register and the roadmap. Prompt 09 owns alliance founding, constitution, leadership, ranks, membership, shared resources, alliance diplomacy and collective decisions, and must apply the `D-137` resolution for the national system: no alliance-level treaty object in B-08 and zero diplomatic delegation. It must not treat a B-08 nation treaty as an alliance treaty, must not assume a delegation model, and must not reopen Prompt 08's rules. `D-140` later authorizes only a separate B-09 Alliance-to-Alliance object; zero delegation remains binding.

**Handoff instruction.** Read, in order: [ROADMAP.md](../ROADMAP.md) and [stage-2/01](01_stage_2_prompt_roadmap.md) for the sequence; [AI_HANDOFF.md](../AI_HANDOFF.md) §H and the 2026-10-30 record; [B-08](15_diplomacy.md) v1.2 §2–§15 and §17–§21; [this document](15_diplomacy_workflows_acceptance.md) §2–§5 for the canonical semantics and states, §9 for authority, §14 for the tests and §18 for the implementation boundary; [the formula register](15_diplomacy_formula_register.md) for every constant. Do not restart Prompt 08B. Do not treat the test catalogue as executed. Do not begin Prompt 10.

**End of document.**
