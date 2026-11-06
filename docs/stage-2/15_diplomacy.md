# B-08 — Diplomacy: foundations, player authority, relationships and agreements

**Version:** 1.3 · **Created:** 2026-10-30 · **Revised:** 2026-11-01 · **Stage 2, Prompt 08B** · **Corrected 2026-10-30 (Prompt 08B-C):** complete posture matrix (12 transitions), one five-step boundary order, ordered proposals vs unordered agreements, freeze-aware cooldowns, DIP-061 cross-reference and the rolling-window example. **Corrected 2026-10-30 (Prompt 08B-D):** DIP-027, DIP-039a, DIP-073 and DIP-093 now state the freeze extension their cooldowns already had in DIP-105/DIP-106, and DIP-044/DIP-106 say per **direction** rather than per pair. No value, treaty type, permission or player-authority rule changed. · **Status erratum 2026-11-01 (Prompt 09B-F):** the 08C status sentence was corrected; no rule changed. · **Prompt 09B-I amendment note (2026-11-01):** `D-140` authorizes a **separate** B-09 Alliance-to-Alliance treaty object (`AT-T01`–`AT-T05`). No B-08 rule, object, party rule, term, value or delegation boundary changes; B-08 remains the exclusive owner of nation treaties and zero diplomatic delegation remains binding. · **Boundary clarification (2026-11-04, Prompt 10B-C3):** the §1.3 scope row names a **restricted Alliance management interface** rather than an "Alliance war room"; the war surface is B-10's nation-level, owner-only War Operations Board, and no Alliance military command or shared OP follows. No B-08 rule changed. · **Design and documentation only**
**Status:** **Designed at the foundations level; not implemented, not runtime-tested, not release-approved.** Every numeric value in this document is **Provisional** and belongs to Prompt 14. Prompt 08C — workflows, edge cases and acceptance — is **complete** at [v1.4](15_diplomacy_workflows_acceptance.md); this status was corrected under Prompt 09B-F after the 08C deliverable was verified, and v1.4 carries only the Prompt 09B-J boundary clarification with no B-08 rule change.
**Parent task:** Stage 2, **Prompt 08 — diplomacy between nations**. This document is the **B-08** deliverable of **08B**; it is not the whole of Prompt 08. Prompt 08C has its own deliverable and does not amend a B-08 rule.
**Evidence base:** [`research/08A_diplomacy_research.md`](research/08A_diplomacy_research.md) v1.0 — 19 sources (`DPS-001`…`DPS-019`), 54 findings (`DPR-001`…`DPR-054`), six conflicts (`DPX-01`…`DPX-06`), twelve candidate recommendations (`DCR-01`…`DCR-12`) and sixteen questions (`DQ-01`…`DQ-16`). The research **proposes**; this document **decides**, and every decision is recorded in [`DECISIONS.md`](../DECISIONS.md).
**Formulas:** every calculation is in [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md) (`F-DP-001`…`F-DP-012`). This document states the rule; the register states the arithmetic.
**Identifier spaces:** rules **`DIP-001…DIP-157`** (`DIP-001`…`DIP-151` and `DIP-152`…`DIP-157` are rule paragraphs or §16.1 entries; `DIP-039a` is a sub-lettered rule); failure codes **`DPF-01…DPF-15`**; formulas **`F-DP-001…F-DP-012`**; agreement types **`DP-T01…DP-T03`**; act **`DP-A01`**; decisions **`D-123…D-132`**; requirements **`REQ-514…REQ-533`**. None reuses an existing `TR-`, `RRL-`, `ECN-`, `URB-`, `DMP-`, `MKT-`, `F-TM-` or `F-PD-` identifier.

---

## 1. Purpose, scope and how to read this document

### 1.1 Purpose

B-08 defines how two **nations** may hold and change a diplomatic relationship, propose and conclude a written agreement, carry out the few diplomatic acts the first playable supports, and live with the public record of what they did. It exists to answer five questions for every diplomatic action:

1. **Who decides?** — always a player, never the system (D-123/D-126).
2. **What exactly is being agreed?** — a posture, an agreement with terms, or a coercive act (D-123/D-124).
3. **When does it take effect, and when does it end?** — at a boundary, under B-02's clock (D-131).
4. **What can the other system do with it?** — a named contract row, owned by one document (D-132).
5. **What happens when it goes wrong?** — a named failure code and a permanent record (D-127/D-131).

### 1.2 In scope

- The directional **posture** between two nations.
- Three bilateral **agreements**: non-aggression (`DP-T01`), consultation (`DP-T02`) and aid (`DP-T03`).
- The **proposal** lifecycle: submit, withdraw, reject, expire, accept.
- **Amendment, renewal, mutual termination and unilateral breach** of an active agreement.
- One coercive diplomatic **act**: the embargo (`DP-A01`).
- Nation-level **authority**, confirmation, and the prohibition on autonomous diplomacy.
- **Timing, visibility, notifications, history, failure and integrity** rules for the above.
- The **contracts** B-08 owes B-02…B-07, Prompt 09 and Prompts 10–14.
- **Twelve worked examples** and the **08C handoff**.

### 1.3 Out of scope — deliberately not designed here

| Excluded | Owner | Why it is excluded |
|---|---|---|
| War declaration, campaigns, ceasefires, peace terms, protection states | **Prompt 10** | D-023 keeps warfare out of the first playable; B-08 may define a *permission* a NAP blocks, never a campaign |
| Alliance founding, constitution, leadership, ranks, membership, pool, voting, restricted Alliance management interface (not a war room; no military command, member OP spending or shared pool), alliance diplomacy | **Prompt 09** | Registered Prompt 09 scope; B-08 publishes the object and the interface only (§18) |
| Market structure, fees, prices, listings, statistics, Global Trade release | **B-07 / 07C** | D-122, MKT-185, MKT-217/218/220; B-08 adds no fee, tax or price rule |
| Aid as a resource transfer, treasury mechanics, ledger rows | **B-04** | B-08 chooses **crowns only** and delegates the movement to ECN-212 |
| Construction, research, policy or approval effects of a sanction | **B-05 / B-06** | The one sanction adopted (§11) does not touch those systems; URB-155/DMP-138 bound what any future one may do |
| Reputation as a numeric score, trust value or hidden account record | **Not adopted** | D-128; UD-033 resolved as "no score" |
| Delegation of diplomatic authority to another player, an AI or an alliance office | **Prompt 09 / a later decision** | No approved delegation model exists; D-126 refuses to invent one |
| Counterproposals, formal mediation, ultimatums, trade treaties, mutual-defence pacts | **Deferred** | No evidence or approved scope requires them; recorded in §19 |
| Any code, schema, migration, API, screen, job, deployment | **Forbidden in Stage 2** | D-012; no implementation is authorised by this document |

### 1.4 How to read a rule

- **`DIP-nnn` is a rule.** It is binding on later prompts until a superseding `D-` entry changes it.
- **"Provisional"** on a rule or value means the *structure* is decided and the *number* is not validated. Prompt 14 owns every number.
- **"Player"** means the authenticated owner of the active nation (D-032). **"Nation"** is the object that holds the posture and the agreement.
- **"Boundary"** means the two-hour UTC turn boundary in B-02 §10. Nothing in B-08 resolves off a boundary except a player's own submission.
- **"Silence"** is never consent. No rule in this document treats an unanswered proposal as accepted.
- **"Automatic"** is used in exactly three senses — activation, expiry and cleanup — and never means "the game chose for the player" (§3.3).

### 1.5 Status vocabulary used for each rule

| Label | Meaning |
|---|---|
| **Rule** | A binding design position, decided under D-014 and recorded in `DECISIONS.md` |
| **Approved constraint** | An existing approved rule B-08 consumes and may not change |
| **Provisional value** | A number or threshold that Prompt 14 must tune; the structure is fixed |
| **Deferred** | Assigned to a named future prompt; not decided here |
| **Not adopted** | Considered and excluded, with the reason stated |

---

## 2. Design principles

**DIP-001 — Player sovereignty is the first rule.** Every diplomatic decision that belongs to a nation is made by that nation's player. The system validates, records, enforces an existing promise and explains; it never chooses a policy, a counterparty or a response. D-126 makes this binding and §3 applies it action by action.

**DIP-002 — Three layers, never one field.** A **posture** (directional attitude), an **agreement** (mutual written terms) and an **effect** (what another system will now permit or do) are separate objects. The posture does not contain the agreement; the agreement does not contain the effect; the effect is listed in the catalogue. This follows B-02 **TR-019** and the comparative finding `DPR-013`/`DPR-014`.

**DIP-003 — Consent is explicit and bilateral.** A proposal creates no obligation. An agreement exists only after both parties' authorized players accept it. An amendment needs both parties again. Silence, expiry, dormancy and a leadership change never substitute for consent (D-125).

**DIP-004 — The smallest catalogue that has real effects.** B-08 adopts three agreements and one act. Each has a stated effect or a stated "record only" status; none is included because a comparator lists it. P&W's ten treaty labels are evidence that labels can outrun mechanics (`DPR-001`), not a template.

**DIP-005 — Enforcement, not decision.** The game may block an action that contradicts an active promise, expire a deadline the parties agreed to, or apply a consequence the rules define. It may not decide that a nation should accept, reject, break or sanction (D-126).

**DIP-006 — One authoritative record per pair and type.** Two nations cannot hold two live proposals of the same type in the **same direction** (a reciprocal proposal is a separate object — DIP-044), or two active agreements of the same type, or two embargoes in the same direction. A reciprocal act is a second, explicitly different act, not a second copy of the same one (DIP-050; `DPR-054`).

**DIP-007 — Publish the outcome, protect the negotiation.** A pending proposal's terms are visible to its named counterparty only. An agreement becomes public when it activates. Rejection and withdrawal are private unless a party publishes them. This is D-030, implemented rather than re-decided (`DPX-01` resolved in §13).

**DIP-008 — Every action has a declared, visible limit.** D-024 forbids a hidden throttle. B-08 declares proposal, agreement, posture, breach and embargo limits in §12 and publishes them before confirmation (D-130).

**DIP-009 — No new currency, no OP, no invented fee.** Crowns are the only value that moves, and only through B-04's ledger. Operations Points are military-only (D-015). A sanction is not a market fee (MKT-185). An agreement costs nothing unless its own terms say so.

**DIP-010 — No geography.** A posture, an agreement or an embargo has no distance, border, province or front. `REQ-041`/`DD-013`.

**DIP-011 — The record is permanent, the interface is honest.** Signature, activation, termination and breach are class-P events. The record says what happened, who did it, on which turn, and under which rule. No history is rewritten (D-026, TR-090/TR-091).

**DIP-012 — Know the boundary of the system.** A rule that needs another system's behaviour names that system as the owner and states the contract. B-08 does not grow a war rule, a market rule, an alliance rule or an approval modifier to make diplomacy look complete.

---

## 3. Player sovereignty and decision authority

### 3.1 The authority rule

**DIP-013 — Sole authority.** The only player who may act for a nation in B-08 is the authenticated owner of that nation's **active** account (D-032). Authority is resolved from the session on every action; a submitted `nation_id` is an object reference to authorize, never an identity claim.

**DIP-014 — No authority by relationship.** A treaty, a posture, a shared alliance (Prompt 09) or a negotiation gives a player **no** authority over the other nation's decisions. The counterparty's acceptance is always its own.

**DIP-015 — No delegation in B-08.** B-08 defines no ministers, officers, proxies or AI agents. If a later prompt adds delegation, it must state the scope, the revocation rule, the audit event and the re-validation the delegated act must pass; until then, a delegated diplomatic act is `DPF-03 UNAUTHORIZED`. **Resolved for the Alliance scope by Prompt 09 under D-137:** no delegation model is adopted; zero diplomatic delegation remains binding (see also DIP-148).

**DIP-016 — Confirmation before consequence.** Every consequential action shows, before the player confirms: the counterparty, the agreement type and version, the terms, the activation turn, the expiry or completion condition, the cost or reservation, what the action does **not** do, and the consequence of breaking it. A one-click irreversible action with hidden terms is a specification defect.

**DIP-017 — The player may always refuse.** No rule obliges a player to accept a proposal, to respond to one, to renew, to terminate, or to lift an embargo. The cost of refusal is the lost opportunity and the public record, never an automatic penalty.

**DIP-018 — The player may break their own promise, visibly.** A party may unilaterally **break** an active agreement. The game ends the effect immediately, writes a permanent public breach event and applies the breach cooldown. It does not fine, freeze, ban or auto-retaliate. The choice is the player's; the record is everyone's (§8.5).

**DIP-019 — The system never accepts, rejects, declares, sanctions, surrenders or signs.** The following are prohibited regardless of convenience: auto-accepting an incoming proposal; auto-rejecting one before its deadline; declaring war or an embargo for a player; entering an alliance commitment; accepting peace; breaking or renewing an agreement; spending crowns on a diplomatic action without confirmation; changing a posture automatically.

**DIP-020 — Automatic acts are a closed list.** The system may perform only:
1. **activation** of a proposal both parties accepted, at the boundary (DIP-048);
2. **expiry** of a proposal or agreement whose agreed deadline passed (DIP-052, DIP-053);
3. **cleanup** required by an account event — reroll, dormancy, retirement — defined in DIP-127…DIP-130.
Nothing else is automatic. An "automatic" act never chooses a new counterparty, term or response.

### 3.2 The mandatory authority test

Every action in §9 answers these eight questions. An action that cannot answer all eight is not specified.

| # | Question | Where answered |
|---|---|---|
| 1 | Who chooses to initiate it? | §9 permission matrix; §3.1 |
| 2 | Who chooses to accept it? | §8.1–§8.3 |
| 3 | Whose nation is affected? | §6 terms; §9 |
| 4 | Whose resources are affected? | §6.3 (aid); §11 (no cost) |
| 5 | Who must authorize it? | DIP-013; §9 |
| 6 | Can the game perform it automatically? | DIP-020; §12 |
| 7 | Can the affected player cancel or revoke an authorization? | DIP-017; §8.4–§8.5 |
| 8 | What happens if a participant does nothing? | DIP-052 (expiry); DIP-017 (no penalty) |

### 3.3 What "automatic" may and may not mean

| Situation | May the system act? | Why |
|---|---|---|
| Both players accepted; the activation boundary arrives | **Yes — activate** | The players already decided; the system executes their decision |
| A proposal's 36-turn deadline passes unanswered | **Yes — expire** | The deadline is part of the rule the proposer chose; expiry is not a rejection by the system |
| An agreement's term ends | **Yes — expire** | Same |
| A nation rerolls | **Yes — terminate and record** | B-03 RRL-019 already decides the outcome |
| A nation becomes dormant | **Yes — cancel its open proposals** | The player cannot respond, and holding the slots would spam the counterparty; active agreements persist |
| A player is in `TRANSITION`/`CRISIS` | **Yes — freeze** | B-06 DMP-263 suspends authority; freezing protects the player from losing a deadline they cannot meet |
| An incoming proposal is unattractive | **No** | The player rejects or ignores it |
| A counterparty is hostile | **No** | The player decides |
| A treaty could be renewed | **No** | Renewal is a new proposal requiring consent |
| An embargo could be lifted | **No** | Only the imposer may lift it |
| A breach could be punished | **No** | The record is the consequence; enforcement belongs to the rules, not to retaliation |

**DIP-021 — Expiry is not rejection.** An expired proposal is recorded as `EXPIRED`, not `REJECTED`, and the counterparty is told the deadline passed. The proposer may submit a new proposal subject to the limits in §12.

**DIP-022 — Freeze beats expiry.** While a party is in `TRANSITION` or `CRISIS`, its proposals do not expire, its agreements do not terminate for lapse, and its deadlines are extended by the frozen turns (DIP-105). The player is not punished for a state the rules imposed.

---

## 4. The relationship model — posture

### 4.1 What a posture is

**DIP-023 — Posture is directional and declarative.** Each nation holds one posture toward each other nation: `FRIENDLY`, `NEUTRAL`, `TENSE` or `HOSTILE`. A's posture toward B is independent of B's toward A. The default is `NEUTRAL`.

**DIP-024 — A posture is not an agreement and creates no obligation.** It is the nation's published attitude. It does not bind the other nation, does not create a treaty, and does not by itself change any eligibility except the one gate in DIP-026. It is not a promise, so breaking it is not a breach.

**DIP-025 — Posture changes are the player's, immediate and public.** The owner may change their nation's posture at any time subject to the cooldown (DIP-027). The new posture is a **declared public act**: it is visible immediately, recorded as a class-I event, and the counterparty is notified. It never changes the other nation's posture.

**DIP-026 — The only gate: an embargo needs `HOSTILE`.** A nation may declare an embargo (§11) only on a nation toward which it currently holds `HOSTILE` posture. No other action in B-08 is gated by posture. Proposing, accepting, renewing and terminating are available at any posture; a player may sign a NAP with a nation it distrusts.

**DIP-027 — Posture cooldown.** After a nation changes its posture toward a given nation, it may not change it toward that nation again for **12 turns** (one day), extended by that nation's own frozen turns — the cooldown is **12 unfrozen boundaries** from the change (DIP-105(b), F-DP-005). The cooldown is visible on the pair screen with the exact eligible turn, including any added turns. A change that would violate the cooldown fails with `DPF-08 POSTURE_COOLDOWN`. The cooldown is per direction and per pair; it never blocks the counterparty, and the counterparty's freeze never lengthens it.

**DIP-028 — No automatic posture change, no decay.** A posture never changes because of time, absence, an agreement, an embargo, a breach or a reroll. A rerolled nation's replacement starts `NEUTRAL` toward everyone (RRL-019), which is a cleanup event, not a drift. There is no "relations decay" mechanic and no hidden modifier.

**DIP-029 — Hostile posture is not war.** `HOSTILE` is an attitude; it does not declare war (Prompt 10 owns that), does not permit an attack, and does not itself block trade. Its only mechanical consequence is the embargo gate. This separation is deliberate: D-023 keeps war out of the first playable, and a posture must not smuggle it in.

**DIP-030 — Posture visibility.** A nation's posture toward another is **public** while both nations exist. The pair screen shows both directions side by side, so a player cannot mistake their own attitude for the counterparty's. A retired nation's historical postures remain on its public page; a dormant nation's posture remains readable.

### 4.2 Posture transition table

Every one of the twelve source-destination pairs is listed, so no reader has to infer whether an omitted row is allowed. Every transition is initiated by the owning player, requires no counterparty consent, and is immediate. "Cooldown" is DIP-027. No transition is prohibited between postures: an attitude is the player's own, and a rule that forbade, say, `HOSTILE` → `FRIENDLY` would let the system hold a player's declared attitude against their later choice.

| # | From | To | Preconditions | Confirmation | Result | Failure | Record | Notification |
|---|---|---|---|---|---|---|---|---|
| T1 | `NEUTRAL` | `FRIENDLY` | Cooldown clear; counterparty exists and is not retired | Shows the declaration is public | Posture changes; class-I event | `DPF-08`; `DPF-02` | `POSTURE_SET` | Counterparty |
| T2 | `NEUTRAL` | `TENSE` | Cooldown clear; counterparty exists | Same | Same | Same | `POSTURE_SET` | Counterparty |
| T3 | `NEUTRAL` | `HOSTILE` | Cooldown clear; counterparty exists; **if a `DP-T02` is active, a valid notice exists** (DIP-039a) | Shows the notice state and the embargo gate | Posture changes; embargo becomes available | `DPF-08`; `DPF-02`; `DPF-09` | `POSTURE_SET` | Counterparty |
| T4 | `FRIENDLY` | `NEUTRAL` | Cooldown clear | Same | Same | `DPF-08` | `POSTURE_SET` | Counterparty |
| T5 | `FRIENDLY` | `TENSE` | Cooldown clear | Same | Same | `DPF-08` | `POSTURE_SET` | Counterparty |
| T6 | `FRIENDLY` | `HOSTILE` | Cooldown clear; **if a `DP-T02` is active, a valid notice exists** | Shows the notice state | Posture changes; embargo becomes available | `DPF-08`; `DPF-09` | `POSTURE_SET` | Counterparty |
| T7 | `TENSE` | `NEUTRAL` | Cooldown clear | Same | Same | `DPF-08` | `POSTURE_SET` | Counterparty |
| T8 | `TENSE` | `FRIENDLY` | Cooldown clear | Same | Same | `DPF-08` | `POSTURE_SET` | Counterparty |
| T9 | `TENSE` | `HOSTILE` | Cooldown clear; **if a `DP-T02` is active, a valid notice exists** | Shows the notice state | Posture changes; embargo becomes available | `DPF-08`; `DPF-09` | `POSTURE_SET` | Counterparty |
| T10 | `HOSTILE` | `NEUTRAL` | Cooldown clear | Same | Posture changes; an active embargo **continues** to its term (DIP-099) | `DPF-08` | `POSTURE_SET` | Counterparty |
| T11 | `HOSTILE` | `TENSE` | Cooldown clear | Same | Posture changes; an active embargo continues | `DPF-08` | `POSTURE_SET` | Counterparty |
| T12 | `HOSTILE` | `FRIENDLY` | Cooldown clear | Same | Posture changes; an active embargo continues | `DPF-08` | `POSTURE_SET` | Counterparty |
| T13 | any | any | Counterparty is `retired` | — | **Rejected** | `DPF-02 NATION_UNAVAILABLE` | — | — |
| T14 | any | any | Actor's nation is in `TRANSITION`/`CRISIS` | — | **Rejected** | `DPF-07 AUTHORITY_SUSPENDED` | — | — |
| T15 | any | same | — | — | **No-op, not an error** | — | No event | None |

**DIP-031 — Every transition *to* `HOSTILE` carries the notice precondition.** T3, T6 and T9 are the only rows with an extra precondition, and it applies whenever a `DP-T02` consultation pact is active with that counterparty — not only when the starting posture is `TENSE`. A `CONSULT` pact does not freeze posture; it requires the player to give notice before declaring hostility, from whatever posture. The failure names the notice requirement and links to the notice action; it never offers to send the notice automatically.

**Leaving `HOSTILE` does not lift an embargo or end a notice.** Posture and embargo are separate objects (DIP-036, DIP-099): an embargo imposed while `HOSTILE` continues to its 24-turn term if the imposer softens its posture; the imposer may lift it early (A12) and the target still cannot (DIP-098). No transition creates, renews or cancels a treaty, and no transition changes the counterparty's posture.

**DIP-032 — A failed posture change changes nothing.** The cooldown is not consumed, no event is written, and the counterparty is not notified. A rejected action is not a "near miss" record.

---

## 5. State machines

### 5.1 Proposal states

```
PENDING ──accept──▶ ACCEPTED ──boundary──▶ (effect applied; proposal stays ACCEPTED as history)
   │
   ├──reject──────▶ REJECTED
   ├──withdraw────▶ WITHDRAWN
   └──deadline────▶ EXPIRED
```

| State | Meaning | Who can move it | Terminal? |
|---|---|---|---|
| `PENDING` | Submitted, awaiting the named counterparty | Counterparty accepts/rejects; proposer withdraws; boundary expires | No |
| `ACCEPTED` | Both players consented; effect applies at the next boundary | Boundary applies it at step 3; a freeze extends the deadline rather than pausing an applied effect (DIP-105) | Yes as a decision; effect pending |
| `REJECTED` | Counterparty declined | — | Yes |
| `WITHDRAWN` | Proposer withdrew before acceptance | — | Yes |
| `EXPIRED` | Deadline passed unanswered | — | Yes |

**DIP-033 — There is no `DRAFT` state.** A proposal is created when the player submits it. A local unsent form is interface state, not a game object, and writes nothing.

**DIP-034 — There is no `COUNTERED` state.** B-08 does not adopt counterproposals (`DQ-05` option (a)). A rejection is free and final; either party may submit a new proposal. This keeps one live proposal per direction and type and avoids a negotiation tree the project has no evidence for.

**DIP-035 — An `ACCEPTED` proposal is still not public.** Acceptance is a decision; activation is the effect. Between them the terms remain parties-only (§13). The agreement object is created in `ACCEPTED` and becomes `ACTIVE` at the boundary.

### 5.2 Agreement states

```
ACCEPTED ──boundary──▶ ACTIVE ──term──▶ EXPIRED
                         │  ├──mutual──▶ TERMINATED
                         │  ├──break───▶ BREACHED
                         │  └──delivery▶ COMPLETED   (aid only)
                         └──amend──────▶ ACTIVE (version + 1; prior version SUPERSEDED)
```

| State | Meaning | Terminal? | Effect live? |
|---|---|---|---|
| `ACCEPTED` | Both accepted; activation at next boundary | No | No |
| `ACTIVE` | In force from its activation turn | No | Yes |
| `EXPIRED` | Term ended at its agreed expiry | Yes | No |
| `TERMINATED` | Ended by mutual consent | Yes | No |
| `BREACHED` | Ended by a party's unilateral break | Yes | No |
| `COMPLETED` | A one-shot obligation was performed (aid) | Yes | No |

**Versions.** An agreement has an integer `version` starting at 1. An amendment creates a **new proposal** referencing the agreement and the proposed version. On activation, the agreement's terms become version *n+1* and the prior version is labelled `SUPERSEDED` in the version history. The agreement does not pass through a "pending amendment" state: the old terms remain fully in force until the amendment activates. This is DIP-064.

### 5.3 Embargo states

```
ACTIVE ──term──▶ EXPIRED
   └──lift────▶ LIFTED
```

**DIP-036 — An embargo is an act, not an agreement.** It has an imposer and a target, no target consent, one effect list and a fixed term. It is never "signed", never amended, and never converted into a treaty. The target cannot accept, reject or lift it; it may respond diplomatically, and the record shows the response only if the target publishes one.

### 5.4 Transition ownership

| Transition | Actor | Consent | Automatic? |
|---|---|---|---|
| Posture change | Owning player | None (own attitude) | No |
| Proposal submit | Proposing player | Counterparty later | No |
| Proposal withdraw | Proposing player | None | No |
| Proposal reject | Counterparty | Its own | No |
| Proposal expire | Boundary | Pre-agreed deadline | **Yes** |
| Proposal accept | Counterparty | Its own | No |
| Agreement activate | Boundary | Both already consented | **Yes** |
| Agreement expire | Boundary | Pre-agreed term | **Yes** |
| Agreement terminate | Both players | Both | No |
| Agreement break | Either player | Its own, with record | No |
| Agreement complete | Boundary (aid delivery) | Pre-agreed | **Yes** |
| Amendment activate | Boundary | Both accepted the amendment | **Yes** |
| Embargo declare | Imposing player | None (coercive) | No |
| Embargo expire | Boundary | Pre-agreed term | **Yes** |
| Embargo lift | Imposing player | Its own | No |

---

## 6. The agreement catalogue

### 6.0 Catalogue rules

**DIP-037 — Three agreements, one act.** B-08 adopts `DP-T01` non-aggression, `DP-T02` consultation and `DP-T03` aid. It adopts one coercive act, `DP-A01` embargo. No other type exists at first playable. A type not in this table cannot be proposed, stored or displayed as a treaty.

**DIP-038 — Every type states its effect.** A type's row says exactly which system changes behaviour and when; "record only" is permitted but must be written. A label with no effect is not a treaty type in B-08.

**DIP-039 — Treaty parties are nations, not alliances.** `DP-T01`…`DP-T03` are signed by two nations. An alliance is never a party by implication, and alliance membership never makes an alliance liable for a member's agreement (§18). **09B-I note:** the separate B-09 `AT-T01`–`AT-T05` object authorized by `D-140` is not a B-08 treaty, has no B-08 party and creates no B-08 effect; this rule governs every B-08 instrument without exception.

### 6.1 `DP-T01` — Non-aggression pact (NAP)

| Field | Rule |
|---|---|
| **Purpose** | A public promise that neither party will declare war on the other for the term. It is the one agreement whose effect is a hard permission block. |
| **Parties** | Exactly two nations, both active and not a restricted pair. |
| **Proposal authority** | Either party's owner (DIP-013). |
| **Acceptance authority** | The other party's owner. No third party, no alliance, no office. |
| **Consent** | Both. Silence never accepts. |
| **Preconditions** | Neither party is retired, removed or unavailable; the pair is not restricted (DIP-074); neither party has an active `DP-T01` with the other; neither party is at its active-agreement cap (DIP-106); the proposer has no live `DP-T01` proposal to the same counterparty. |
| **Activation** | At the first boundary after acceptance (DIP-048). |
| **Term** | **360 turns** (30 days) from activation. **Provisional** (Prompt 14). |
| **Expiry** | Automatic at `activation_turn + 360`. A renewal accepted before expiry extends the term; an expired NAP is not retroactive. |
| **Renewal** | A `RENEW` proposal (§8.4) accepted and activated **before** the expiry boundary. The new expiry is `old_expiry_turn + 360`. No silent renewal. |
| **Amendment** | A versioned amendment (§8.3). The term may be extended, shortened or the text clarified; shortening requires both parties. |
| **Withdrawal before activation** | The proposer may withdraw while `PENDING`. After acceptance, only mutual termination or break — acceptance is a decision and cannot be undone unilaterally. |
| **Termination** | Mutual `TERMINATE` (§8.4) or unilateral `BREAK` (§8.5). Expiry is automatic. |
| **Breach condition** | A party declares war on the other while the NAP is `ACTIVE`. Until Prompt 10 exists, the block is **inert** and no first-playable action can breach a NAP. If Prompt 10 ever permits the declaration, it must call the NAP check and record `BREACHED`; B-08 does not define the war rule. |
| **Effect** | `WAR_DECLARATION` between the parties is **not permitted** while the NAP is `ACTIVE`. The block is enforced by Prompt 10's declaration validator, which reads this agreement. The NAP does not block trade, aid, an embargo, a posture or a proposal. |
| **Visibility** | Pending: parties only. Active: public (type, parties, activation, expiry, version). Private notes are not part of the object. |
| **History** | `PROPOSED`, `ACCEPTED`, `ACTIVATED`, `RENEWED`, `AMENDED`, `TERMINATED`/`EXPIRED`/`BREACHED` are class-P events. |
| **Cross-system** | Prompt 10 (declaration validator); B-02 (timing); B-13 (display). No cost. |
| **Status** | **Designed; effect inert until Prompt 10.** |

### 6.2 `DP-T02` — Consultation pact

| Field | Rule |
|---|---|
| **Purpose** | A public promise to give warning before escalating to hostility or imposing an embargo. It is the "soft" agreement in the catalogue: it constrains the parties' own future acts, not a third system. |
| **Parties** | Exactly two nations. |
| **Proposal / acceptance** | Either owner; the other owner accepts. Both consent. |
| **Preconditions** | As `DP-T01`, with `DP-T02` in place of the type; no duplicate live proposal or active agreement of this type. |
| **Activation / term / expiry** | Next boundary; **360 turns**; automatic expiry. **Provisional.** |
| **Renewal / amendment / withdrawal** | As `DP-T01`. |
| **Effect** | While active, a party may not (a) set its posture toward the other to `HOSTILE`, or (b) declare an embargo on the other, unless it has sent a **consultation notice** to the other at least **12 turns** earlier and no more than **36 turns** earlier, that end extended by either party's freeze (DIP-039a, DIP-105(a)). The action fails with `DPF-09` if the notice is missing or stale. |
| **Breach condition** | There is none reachable while the gate works: the prohibited act is blocked. If a later system permits the act without the check, that system records `BREACHED`; B-08 does not create a second enforcement path. |
| **Visibility** | Pending: parties only. Active: public. A consultation notice is visible to the **counterparty only**; third parties see the resulting posture or embargo, not the warning. |
| **History** | `PROPOSED`, `ACCEPTED`, `ACTIVATED`, `NOTICE_SENT`, `AMENDED`, terminal states — class-P except the notice, which is class-S (it is an intent, not an obligation performed). |
| **Cross-system** | B-08 only (posture and embargo gates); B-13 shows the notice and the eligible window. No cost. |
| **Status** | **Designed.** |

**DIP-039a — Consultation notice.** The notice is a player action (`SEND_CONSULT_NOTICE`) available only while a `DP-T02` is active with the named counterparty. It records the turn, is visible to the counterparty, and is valid for the window `[notice_turn + 12, notice_turn + 36 + pair freeze]`: the 12-turn minimum is fixed, while the end moves by the boundaries on which **either** party was frozen (DIP-105(a), F-DP-006a). It does not commit the sender to act, and it does not reveal the intended act. A notice may be sent once per **12 unfrozen turns** per pair, extended by the sender's own frozen turns (DIP-105(b), F-DP-006b); a second notice inside that window fails with `DPF-10 NOTICE_COOLDOWN`.

### 6.3 `DP-T03` — Aid agreement

| Field | Rule |
|---|---|
| **Purpose** | A one-off, consented transfer of **crowns** from one nation to another, recorded as a treaty rather than a market trade. |
| **Parties** | Two nations: a payer and a recipient. The payer is the proposer. |
| **Proposal / acceptance** | Payer proposes; recipient accepts. Both consent. |
| **Terms** | An integer crown amount `A`, fixed at proposal time. **Crowns only** — no resources, capacity, DC, housing, research points, approval or population (URB-155, DMP-138). |
| **Preconditions** | Payer has at least `A` crowns **available** (not reserved elsewhere) at submission; the pair is not restricted; neither party is at the active-agreement cap; no live `DP-T03` proposal or active `DP-T03` between the pair. |
| **Reservation** | At acceptance, the payer's `A` crowns are **reserved** under B-02 §19. The recipient's acceptance re-validates the payer's balance and the pair. If reservation fails, acceptance fails with `DPF-05 INSUFFICIENT_CROWNS` and nothing moves. |
| **Activation / delivery** | At the first boundary after acceptance, in **P4**, the reserved crowns move as one B-04 transfer with matched ledger events and one `transfer_id`. The agreement becomes `COMPLETED` in the same boundary. |
| **Term** | None. A one-shot obligation, not a standing treaty. It does not expire and cannot be renewed; a second aid agreement is a new proposal. |
| **Amendment** | Not permitted. An aid agreement's amount is fixed; to change it, break or terminate before activation and propose again. |
| **Withdrawal / termination** | The payer may withdraw while `PENDING`. After acceptance, either party may **break** before delivery (the reservation is released, a breach is recorded) or agree to **terminate** (the reservation is released, no breach). |
| **Breach condition** | A break before delivery. Failure of the transfer caused by an operator-voided turn is **not** a breach; the agreement returns to `ACCEPTED` and retries at the next successful boundary (DIP-129). |
| **Visibility** | Pending: parties only. Completed: public (payer, recipient, amount, turn). The payer's treasury detail remains private; the public record shows the amount, because the transfer is the treaty's purpose. |
| **History** | `PROPOSED`, `ACCEPTED`, `RESERVED`, `SETTLED`, `BREACHED`/`TERMINATED` — class-P. |
| **Cross-system** | B-04 (reservation, transfer, ledger, no debt, zero floor); B-02 (P4); B-03 (pair check); B-13 (display). |
| **Status** | **Designed; no value is balance-tested.** |

**DIP-040 — Aid is not a gift mechanic and not a market route.** It exists to make a diplomatic promise of support real. It uses B-04's transfer contract, never a parallel balance. A payer cannot promise crowns it does not hold: the submission check and the acceptance reservation both fail closed. There is no credit, no future delivery and no instalment plan.

**DIP-041 — Aid cannot be used to bypass a pair restriction.** The pair check runs at submission, at acceptance and at P4. A restricted pair cannot sign, reserve or settle, and an alliance pool or a third nation cannot be interposed (B-03 §5.5; D-035).

### 6.4 `DP-A01` — Embargo (a coercive act, not an agreement)

The full rule is §11. The catalogue records only that it is **not** a treaty: no consent, no signature, no amendment, no renewal, and one direction per pair.

### 6.5 Types deliberately not adopted

| Candidate | Why not adopted | Owner if revisited |
|---|---|---|
| Mutual-defence pact / automatic war entry | Requires Prompt 10's war rules; would bind 08 to a system that does not exist (D-023, `DQ-04`) | Prompt 10 + a new decision |
| Trade treaty / tariff / market-access pact | B-07 owns market rules; a trade term is not a treaty, and a tariff is forbidden by MKT-185 | B-07 + a new decision |
| Protectorate / guarantee | Implies obligations over a third nation's foreign policy; no approved delegation model | Prompt 09/10 |
| Peace treaty / ceasefire | Prompt 10 owns war termination | Prompt 10 |
| Alliance-level treaty | No **B-08** object and no reuse of the B-08 object; `D-137` resolves zero delegation. `D-140` authorizes a **separate** B-09 `AT-T01`–`AT-T05` object with explicit per-nation consent (§18) | Resolved by `D-137`, amended in part by `D-140` |
| Research / cultural / migration pact | No existing system effect; would be a label with no mechanic (DIP-004) | Not planned |
| Non-binding "declaration of friendship" | Posture already expresses it; a second record would duplicate the layer (DIP-002) | Not planned |

---

## 7. Proposal and agreement lifecycles

### 7.1 Proposal object

**DIP-042 — One object, five outcomes.** A proposal has: `proposal_id`, `type` (`DP-T01`/`DP-T02`/`DP-T03`/`AMEND`/`RENEW`/`TERMINATE`), `from_nation`, `to_nation`, `terms` (type-specific, immutable after submission), `submitted_turn`, `expiry_turn`, `status`, `responded_turn`, `applied_turn`, and the `agreement_id` it references for the four agreement-related types. It has no free-text public field.

**DIP-043 — Terms are immutable.** Editing a submitted proposal is not an action. The proposer withdraws and submits a new one, subject to the limits. This prevents a counterparty from accepting terms it did not see.

**DIP-044 — One live proposal per direction and type.** For any ordered pair and any type, at most one proposal may be `PENDING`. A second submission in the **same direction** fails with `DPF-04 DUPLICATE_PROPOSAL`. A reciprocal proposal is not a duplicate: if B has also proposed `DP-T01` to A, the two are separate objects and either may be accepted; accepting one makes the other fail at its next validation with `DPF-04` (DIP-050, DIP-124).

**DIP-045 — Proposal caps.** A nation may hold at most **3** proposals it has sent that are still `PENDING` across all counterparties. A fourth fails with `DPF-06 PROPOSAL_CAP`. There is no cap on incoming proposals, but the interface groups them and the notification is one per proposal, not one per turn. **Provisional value.**

**DIP-046 — Expiry.** A proposal expires at `submitted_turn + 36` (three days), extended by frozen turns under DIP-105. At the expiry boundary it becomes `EXPIRED`, both parties are notified once, and no effect occurs. **Provisional value.**

**DIP-047 — Withdrawal.** The proposer may withdraw a `PENDING` proposal at any time before acceptance. Withdrawal is free, immediate and private (D-030). It cannot be undone; a new proposal is a new object.

**DIP-048 — Acceptance is a decision, activation is the effect.** The counterparty accepts in the interface; the acceptance is validated at submission and again at P2 (DIP-101). If valid, the proposal becomes `ACCEPTED` and the agreement object is created in `ACCEPTED`. At the boundary, in P4, the agreement becomes `ACTIVE` and its public record is written. If P2 fails, the acceptance fails with the named code, the proposal stays `PENDING` until its deadline, and nothing moves.

**DIP-049 — Rejection.** The counterparty may reject at any time before acceptance. Rejection is immediate, free, private and final for that proposal. It does not consume the proposer's cap once recorded, and it does not trigger a cooldown.

**DIP-050 — Reciprocal proposals resolve deterministically.** If both nations propose the same type to each other, the first acceptance at a boundary wins; the other proposal fails at P2 with `DPF-04 DUPLICATE_PROPOSAL` and is recorded `EXPIRED` with the reason "a reciprocal agreement activated". No duplicate agreement is created. The loser's player is told which agreement superseded it.

**DIP-051 — A proposal never reserves value.** Only an accepted `DP-T03` reserves crowns (DIP-040). A `DP-T01`/`DP-T02` proposal reserves nothing because it costs nothing. A `RENEW` reserves nothing. A `TERMINATE` reserves nothing.

### 7.2 Agreement object

**DIP-052 — One active agreement per pair and type.** Two nations may hold at most one `ACTIVE`/`ACCEPTED` agreement of each type. A second is impossible by the proposal rule; if data ever shows two, the later activation fails at P2 with `DPF-04` and the earlier remains authoritative.

**DIP-053 — The agreement carries its versions.** The object stores the current version's terms, the version number, and an append-only list of prior versions with their `SUPERSEDED` label, activation turn and reason. It does not store a "pending" draft.

**DIP-054 — Agreement caps.** A nation may hold at most **8** agreements in `ACCEPTED` or `ACTIVE` across all types and counterparties. A ninth acceptance fails with `DPF-11 AGREEMENT_CAP`; a ninth proposal may still be submitted only if it would not exceed the cap on activation, otherwise submission warns and acceptance fails closed. **Provisional value.**

**DIP-055 — Terminal states are final.** An agreement that is `EXPIRED`, `TERMINATED`, `BREACHED` or `COMPLETED` cannot be reactivated by editing it. Renewal creates a renewal proposal; a new agreement creates a new object. History is append-only.

### 7.3 The four agreement-related proposal types

| Type | References | Acceptance effect at the boundary | Consent | Notes |
|---|---|---|---|---|
| `AMEND` | An `ACTIVE` agreement | Terms become version *n+1*; prior version `SUPERSEDED`; expiry may change only as the amendment states | Both | Old terms stay in force until activation |
| `RENEW` | An `ACTIVE` agreement that has not expired | Expiry becomes `old_expiry + 360`; version unchanged; `RENEWED` event | Both | Must activate before expiry |
| `TERMINATE` | An `ACTIVE`/`ACCEPTED` agreement | Agreement becomes `TERMINATED`; effect ends; no breach | Both | Mutual exit |
| `BREAK` | An `ACTIVE`/`ACCEPTED` agreement | Agreement becomes `BREACHED`; effect ends; breach event; cooldown | **One** | Unilateral, DIP-018; not a proposal, an action |

**DIP-056 — `BREAK` is not a proposal.** It is a single-player action with confirmation and a public consequence. It needs no counterparty response and cannot be rejected. This is the one place where a player may end a bilateral obligation alone, and the record says so.

**DIP-057 — A `TERMINATE` proposal needs both players.** The initiator proposes; the counterparty accepts or rejects. If it expires unanswered, the agreement continues to its normal expiry. Withdrawal by the initiator leaves the agreement active. No silence ends a treaty.

**DIP-058 — A `RENEW` proposal that activates after expiry is void.** At P2, if `current_turn >= expiry_turn`, the renewal fails with `DPF-12 AGREEMENT_EXPIRED`; the agreement is already `EXPIRED`. A new agreement is the only route. This prevents a retroactive renewal.
---

## 8. Consent, amendment, renewal, termination and breach

### 8.1 Consent

**DIP-059 — Consent is per version.** Each party's acceptance applies to the exact terms it was shown: the type, the version, the amount, the term, the activation and the expiry. A material change after acceptance is impossible because terms are immutable (DIP-043); a change requires a new proposal or an amendment.

**DIP-060 — Who may consent.** Only the authenticated owner of the active nation (DIP-013). An alliance leader, an officer, a third nation or an AI cannot consent for a nation. A restricted pair cannot consent to an agreement with each other (DIP-074).

**DIP-061 — Consent cannot be inherited.** A new owner of the same nation (a leadership change under B-06) inherits the nation's existing agreements; it does not inherit a *pending acceptance* by the previous player. A proposal accepted before the change remains accepted if it was valid when accepted; a proposal merely pending is unaffected and can be accepted or ignored by the new player. A reroll is different: the nation is retired and every agreement terminates (DIP-127).

**DIP-062 — Consent is not silence.** No deadline, dormancy, absence, transition or administrative state is consent. The only consent is an authenticated acceptance by the owner, recorded with the turn and the version.

### 8.2 Approval of material terms

**DIP-063 — What counts as material.** A change to any of these is material and needs fresh consent: the type; the parties; the crown amount of an aid; the term or expiry; the consultation notice window; the effect list; the breach consequence. A change to a non-material label (a private note, a display name) is not a treaty term and is not stored on the object.

**DIP-064 — Amendment procedure.** An `AMEND` proposal carries the full proposed terms and the version it would create. Both parties accept. At the boundary, the agreement's terms become the new version and the old version is `SUPERSEDED`. Until that boundary, the old terms are fully in force: the parties must still comply with the old NAP, the old notice window or the old aid amount. There is no "amendment pending" grace period and no automatic extension.

**DIP-065 — An amendment cannot be used to smuggle a new type.** Changing `DP-T01` into `DP-T02` is not an amendment; it is a termination plus a new proposal. An amendment that names a different type fails validation with `DPF-13 INVALID_TERMS`.

**DIP-066 — A rejected amendment changes nothing.** The agreement stays at its current version and term. The rejection is private. The proposer may submit another amendment subject to the one-live-proposal rule.

### 8.3 Renewal and extension

**DIP-067 — Renewal is prospective.** A `RENEW` accepted before expiry extends the expiry by one term from the **old expiry**, not from the acceptance turn. A renewal accepted after expiry is void (DIP-058). There is no automatic renewal, no "evergreen" clause and no negative-option consent.

**DIP-068 — Extension is the same action.** B-08 does not distinguish "renewal" from "extension": both are a `RENEW` proposal that moves the expiry. A shorter extension is not a renewal; it is an amendment to the term, and it needs both parties.

### 8.4 Termination

**DIP-069 — Mutual termination is free and private.** Either party proposes `TERMINATE`; the other accepts. At the boundary the agreement becomes `TERMINATED`, the effect ends, and no breach is recorded. The fact of termination is public (the agreement's public record changes); the reason is private unless a party publishes it.

**DIP-070 — Termination does not undo the past.** An aid already delivered is not clawed back. A NAP's protection ends at the termination boundary; a war declaration submitted before that boundary but resolving after it is governed by Prompt 10's ordering, not by B-08. B-08 states only that the NAP is not active at the later boundary.

**DIP-071 — Termination of an `ACCEPTED` agreement releases the reservation.** If an aid agreement is terminated before delivery, the payer's reserved crowns are released at the same boundary and no transfer occurs.

### 8.5 Breach

**DIP-072 — Breach is a player's unilateral break, or a prohibited act another system permits.** The two breach conditions are:
1. **B-1 — Unilateral break.** A party uses `BREAK` on an `ACTIVE`/`ACCEPTED` agreement. This is always available, always the player's choice, and always recorded.
2. **B-2 — Externally permitted violation.** A system that owns an effect (today only Prompt 10 for a NAP's war block) permits the prohibited act without calling the check. That system must write `BREACHED` with the act's event ID. B-08 does not create a second detector.

**DIP-073 — What a break does.** At the break boundary: the agreement becomes `BREACHED`; its effect ends; a **public class-P** event records the breaker, the counterparty, the type, the version, the turn and the rule; the counterparty is notified; the breaker's derived breach count increases (§10); the breaker may not propose the same type to the same counterparty for **36 turns** — 36 unfrozen boundaries from the break, extended by the breaker's own frozen turns (DIP-105(b), F-DP-007) — failing `DPF-14 BREACH_COOLDOWN`. Nothing is confiscated, frozen or transferred. The breaker keeps its nation, its treasury and its other agreements.

**DIP-074 — A restricted pair cannot conclude or keep a restricted agreement.** The B-03 §5.5 pair check runs at submission, acceptance and P4. A restricted pair may not sign `DP-T01`, `DP-T02` or `DP-T03`, and may not route the same effect through an alliance, a third nation, an aid transfer or a market trade (D-035). An agreement that becomes restricted after activation is **suspended**, not breached: its effect pauses, the parties are told the pair state, and it resumes if the restriction clears. Suspension is not a penalty and does not create a breach event.

**DIP-075 — Breach cannot be caused by the system.** A failed turn, a voided turn, an operator recovery, a dormancy, a transition/crisis, a reroll or a delayed settlement never creates a breach. The aid rule in DIP-129 is the concrete case: a voided turn re-queues the transfer, it does not fail the payer.

**DIP-076 — No duplicate breach.** A break is recorded once per agreement. A second `BREAK` on a terminal agreement fails with `DPF-01 AGREEMENT_NOT_ACTIVE`. If two players break simultaneously, the first applied at the boundary wins and the second fails at P2; only one breach event exists. Idempotency is by `agreement_id + BREAK` (DIP-102).

**DIP-077 — Breach consequences are direct rules, not hidden scores.** The consequences are exactly: the effect ends; the public record exists; the derived count rises; the 36-turn same-type cooldown applies. No approval, stability, tax, market, production or alliance penalty follows. Any future consequence needs a named term and a new decision (DMP-138's discipline).

---

## 9. Permissions and the action matrix

### 9.1 The action set

B-08 has **fourteen** player actions. Every one is executed by the authenticated owner of the acting nation and is recorded with a turn and an idempotency key. There is no "diplomatic budget", no click allowance and no OP cost.

| # | Action | Initiator | Consent | Affects | Cost / reservation | Reversible? | Confirmation | Record class |
|---|---|---|---|---|---|---|---|---|
| A1 | `SET_POSTURE` | Owner | None (own attitude) | Own posture | None | Yes, after the 12-turn cooldown | Public declaration | I |
| A2 | `SEND_CONSULT_NOTICE` | Owner of a party to an active `DP-T02` | None | Counterparty's information | None | No (a new notice needs the cooldown) | Shows the valid window | S |
| A3 | `PROPOSE_AGREEMENT` | Owner | Counterparty later | Both nations' records | `DP-T03`: crowns available, not reserved | Withdraw before acceptance | Full terms and consequences | P on acceptance |
| A4 | `PROPOSE_AMENDMENT` | Owner of a party | Both | The agreement | None | Withdraw before acceptance | Old vs new terms | P |
| A5 | `PROPOSE_RENEWAL` | Owner of a party | Both | The agreement's expiry | None | Withdraw before acceptance | New expiry | P |
| A6 | `PROPOSE_TERMINATION` | Owner of a party | Both | The agreement | None | Withdraw before acceptance | What ends, what remains | P |
| A7 | `ACCEPT_PROPOSAL` | Counterparty owner | Its own | Both | `DP-T03`: reserves crowns | No; break/terminate after activation | Full terms again | P |
| A8 | `REJECT_PROPOSAL` | Counterparty owner | Its own | The proposal | None | No (a new proposal is new) | One click, private | S |
| A9 | `WITHDRAW_PROPOSAL` | Proposer | Its own | The proposal | None | No | One click, private | S |
| A10 | `BREAK_AGREEMENT` | Either party | One | Both | None | No | Names the public breach and the 36-turn cooldown | P |
| A11 | `DECLARE_EMBARGO` | Owner, `HOSTILE` posture | None (coercive) | Target and imposer | None | Only by lifting | Names every blocked route | P |
| A12 | `LIFT_EMBARGO` | Imposer | Its own | Both | None | No | One click, public | P |
| A13 | `VIEW_DIPLOMACY` | Any authenticated user | — | Read only | None | — | — | — |
| A14 | `PUBLISH_REASON` | Either party | Its own | Public record | None | No (append-only) | Shows what becomes public | P |

**DIP-078 — A14 exists because D-030 allows publication.** A rejection, withdrawal or termination reason is private by default. Either party may publish **its own** reason as a free-text statement attached to the event; it cannot publish the counterparty's reason, and the counterparty is notified. The statement is class-P and append-only; a correction is a new statement. It is not a treaty term and creates no obligation.

### 9.2 Permission matrix by action

| Action | Proposing party | Counterparty | Third nation | Alliance officer | Administrator |
|---|---|---|---|---|---|
| `SET_POSTURE` | Own only | No | No | No (Prompt 09 may add a display, never a control) | No (Prompt 12 may restrict an account, not set a posture) |
| `SEND_CONSULT_NOTICE` | Own only | No | No | No | No |
| `PROPOSE_AGREEMENT` | Own only | No | No | No | No |
| `PROPOSE_AMENDMENT` | Party only | Party only | No | No | No |
| `PROPOSE_RENEWAL` | Party only | Party only | No | No | No |
| `PROPOSE_TERMINATION` | Party only | Party only | No | No | No |
| `ACCEPT_PROPOSAL` | No | Named counterparty only | No | No | No |
| `REJECT_PROPOSAL` | No | Named counterparty only | No | No | No |
| `WITHDRAW_PROPOSAL` | Proposer only | No | No | No | No |
| `BREAK_AGREEMENT` | Either party | Either party | No | No | No |
| `DECLARE_EMBARGO` | Own only | No | No | No | No |
| `LIFT_EMBARGO` | Imposer only | No | No | No | No |
| `VIEW_DIPLOMACY` | Own view | Own view | Public fields only | Per §18 | Restricted audit only |

**DIP-079 — No administrator may sign, break or sanction for a player.** An administrator may suspend an account, restrict a pair or remove content under Prompt 12. That is an **account** measure, not a diplomatic act: it produces no treaty, no posture and no breach attributed to the nation. D-031's three state machines are preserved.

**DIP-080 — Read access follows visibility, not relationship.** Being a treaty party does not grant access to the counterparty's treasury, other treaties or private reasons. Being an alliance member does not grant access to a member's pending terms (§18).

### 9.3 Mandatory confirmation content

**DIP-081 — The confirmation panel must show, before submission:** the action; the named counterparty; the agreement type and version; every term; the activation boundary; the expiry or completion condition; the cost or reservation (aid); the public/private status now and after activation; the breach consequence and the 36-turn cooldown; and the exact limits the action consumes. For `BREAK_AGREEMENT`, it must show that the record is permanent and public and that no retaliation follows automatically.

**DIP-082 — No dark pattern.** A confirmation may not preselect acceptance, hide a term behind a tooltip, count down to an automatic acceptance, or offer "accept all". Declining is always available and free. This is a player-sovereignty rule, not a UX preference.

**DIP-083 — A failed action explains itself in the player's terms.** Each `DPF` code maps to one sentence naming the cause and the next eligible turn where one exists (`"You changed posture toward this nation 4 turns ago; you can change it again on turn 1,240."`). It never discloses the counterparty's private state (TR-023).
---

## 10. Reputation and diplomatic consequences

### 10.1 The decision

**DIP-084 — There is no diplomatic reputation score.** B-08 adopts **no** stored honour, trust, prestige, standing or "diplomatic points" value. No formula in this document produces a score, and no other system may read a diplomatic reputation from B-08 because none exists. This follows the evidence in `DPR-033`…`DPR-040`: the comparators offer trust, opinion, player labels or no register, and none supports a single global number. It also follows D-049/DD-067 (one currency, no prestige) and DMP-138 (no unnamed diplomatic modifier).

**DIP-085 — What exists instead is a factual record and one derived count.** Every agreement event is a permanent class-P record (§14). From those records B-08 derives exactly one public number per nation: the **breach count** — the number of `BREACHED` events attributed to that nation in the trailing **4,380 turns** (365 days). It is a count of events, not a judgement, not a score, and not an input to any other system.

**DIP-086 — The breach count is nation-scoped and dies with the nation.** The count is attached to the nation identity that committed the breach. A reroll retires that nation; its historical page keeps the record and the count as history. The replacement nation starts at **zero** and inherits no diplomatic consequence. This is UD-033 option **(a)**, adopted explicitly.

**DIP-087 — Why (a), and what it costs.** Nation-scoping matches RRL-019 ("the replacement starts neutral with no treaties"), keeps one owner for the record (D-031), avoids a hidden account penalty and avoids making a new nation answerable for an old one. The cost is real and is not hidden: **a player can shed the count by rerolling.** B-03 already constrains the escape — a reroll is blocked during an active campaign or settlement and enforcement sanctions survive (RRL-021, RRL-017) — but the diplomatic count itself does not follow the account. B-08 accepts that limitation because the alternative (an account-level diplomatic record) would be a covert account sanction and would need a policy decision this prompt is not authorized to make. The public retirement page is the mitigation: the old nation's breaches remain visible and attributed, and the replacement is visibly new.

**DIP-088 — The count has no mechanical effect.** It does not change approval, stability, tax, production, market access, war eligibility, proposal eligibility or the outcome of any action. It is displayed on the public nation page and in the treaty history. A player may use it; the game does not. This keeps "factual history" and "calculated reputation" separate, as the 08A brief requires.

**DIP-089 — No hidden account record.** B-08 creates no restricted "diplomatic integrity" record. Prompt 12's enforcement records are separate, are governed by D-018/D-042, and are never read by B-08 as a reputation. A player cannot be silently penalised by a record it cannot see.

**DIP-090 — No decay, no recovery, no purchase.** The count is a rolling 365-day window; an old breach leaves the window by time, not by a "repair" action. There is no way to buy, trade or grind the count down. There is no positive counterpart ("honour"), because a positive score would need a purpose and a formula this design does not have.

### 10.2 UD-033 disposition

| Field | Disposition |
|---|---|
| **Registered question** | "Is in-game diplomatic/treaty reputation account-scoped or nation-scoped after a reroll?" |
| **Decision** | **Nation-scoped — option (a).** There is no separate reputation register; the only derived value is the public breach count, attached to the nation. |
| **Recorded in** | **D-128**; this section; the UD register row is marked **Resolved** with the authoritative section. |
| **What the replacement inherits** | Nothing diplomatic. Neutral posture, no agreements, breach count 0. |
| **What survives** | The retired nation's public page, its class-P treaty events and its historical breach count. Enforcement sanctions survive under B-03, separately. |
| **Owner approval** | **Not required.** This is a Category B design decision under D-014: it creates no account-level restriction and no new sanction. Had it created one, it would have needed a policy decision and would not have been made here. |
| **Reopening condition** | Evidence that reroll-laundering is a material abuse, or a decision to introduce an account-level integrity record. Either reopens UD-033 with a new `D-` entry; it does not silently change this one. |

---

## 11. Sanctions — the embargo

### 11.1 Scope decision

**DIP-091 — One sanction, and it is an embargo.** B-08 adopts `DP-A01` embargo as its only coercive act. It does **not** adopt asset freezes, construction bans, research bans, policy freezes, travel bans, reputation penalties or collective alliance sanctions. Those remain unadopted; B-04 ECN-212, B-05 URB-155 and B-06 DMP-138 bound what any future sanction may do, but they do not require one.

**DIP-092 — Why an embargo.** It is the best-evidenced sanction in the research (`DPR-041`, `DPR-042`), it has a clear, bounded effect that B-07 already anticipates (MKT-218: "if B-08 later adds an embargo, the market reads it"), and it needs no new currency, no hidden modifier and no war rule. It is the smallest act that makes "sanctions" in the B-08 scope real.

### 11.2 The embargo rule

**DIP-093 — Declaration.** The owner of a nation may declare an embargo on any other nation toward which it holds `HOSTILE` posture, provided:
1. the target exists and is not retired;
2. the imposer is not in `TRANSITION`/`CRISIS`;
3. there is no active embargo by the imposer on the same target;
4. the imposer's last embargo on that target ended at least **12 turns** ago — 12 unfrozen boundaries from that end or lift, extended by the imposer's own frozen turns (DIP-105(b), F-DP-008);
5. if a `DP-T02` consultation pact is active between the pair, a valid consultation notice exists (DIP-039a).

**DIP-094 — Term.** An embargo lasts **24 turns** (two days) from declaration and expires automatically at the boundary. The term is **not** extended by either party's freeze: it is a fixed sanction duration, not a deadline owed by the target (DIP-105, exception 1). **Provisional value.** It cannot be renewed; the imposer may declare a new one after the 12-turn cooldown. The imposer may lift it early.

**DIP-095 — Effect: new transfers only.** While active, the pair may not create:
- a new **directed-trade offer** or accept an existing one (B-07 reads the embargo; no fee, no price change);
- a new **aid agreement** or a new aid transfer (B-04 reads the embargo as a blocked transfer).

Already-accepted directed trades **settle** at P4. An already-active aid agreement **delivers** at its activation boundary (grandfathering). Existing listings are not deleted; a new execution between the pair fails with a market-side reason that names the embargo. The embargo destroys nothing, confiscates nothing and changes no price.

**DIP-096 — What the embargo does not do.** It does not block diplomacy other than the transfers above: the pair may still propose, accept, renew, terminate or break agreements, and may still change posture. It does not block third-party trade. It does not declare war, blockade, or affect construction, research, policy, approval, stability or population. It is not a market fee and may not be implemented as one (MKT-185).

**DIP-097 — Visibility and record.** The **fact** of the embargo is public: imposer, target, declared turn, expiry turn. The imposer's stated reason is optional and, if given, public (it is a coercive public act, not a private negotiation). The target may publish a response through A14. Declaration, early lift and expiry are class-P events; the target is notified once at each.

**DIP-098 — The target cannot lift it; the imposer can.** There is no negotiation, no counter-offer and no consent. The target's remedies are diplomatic: persuade, retaliate with its own embargo (a separate act, not a reciprocal duplicate), or escalate in a system that owns escalation (Prompt 10, when it exists). B-08 does not auto-retaliate.

**DIP-099 — One direction per pair.** A's embargo on B and B's embargo on A are two distinct acts with two records. B-08 does not collapse them into a "mutual embargo" state, because the imposers, reasons and end turns can differ (`DPR-054`'s duplicate-record warning is about duplicating **the same** act, not about two real ones).

### 11.3 Abuse and integrity

| Risk | Rule |
|---|---|
| Embargo as a hidden tariff | Forbidden: the market reads a permission block, not a price or fee (MKT-185/MKT-218) |
| Embargo spam | One active per pair, 24-turn term, 12-turn re-imposition cooldown (DIP-093/094) |
| Embargo to dodge a pair restriction | The pair check runs on every blocked transfer; an embargo cannot be used to route value around D-035 |
| Embargo as a war substitute | It has no war effect; a blockade or campaign is Prompt 10's and may not be inferred from B-08 |
| Collective/alliance embargo | **Not adopted.** An alliance cannot impose an embargo through B-08; Prompt 09 would need its own authority rule and a new decision |
| Sanction against a dormant nation | **Blocked** at declaration (`DPF-02`); dormancy is protective (D-028) |
| Sanction to evade a breach cooldown | No interaction: the breach cooldown is type-and-pair specific; an embargo is a different act and cannot restore proposal eligibility |

---

## 12. Timing, expiry and declared limits

### 12.1 The clock

**DIP-100 — Everything resolves at a boundary.** B-08 uses B-02's UTC slot arithmetic and P0–P7 phases. A submission between boundaries is recorded immediately but its effect resolves at the next boundary. There is no live or off-boundary resolution.

**DIP-101 — Where B-08 acts in the boundary.**

| Phase | B-08 behaviour |
|---|---|
| **P2 — re-validation** | Re-check authority, pair state, caps, duplicate, expiry, posture/notice, reservation, and agreement state for every accepted proposal and every embargo transition. A failure cancels the action with its `DPF` code and writes no effect. |
| **P3 — recurring** | Not used by B-08. No diplomatic income, upkeep or decay. |
| **P4 — application** | Apply the five ordered steps of DIP-103: (1) expiry and termination, (2) breach, (3) activation, (4) scheduled obligation/aid delivery, (5) embargo declaration, lift and expiry. Each step reads the state committed by the step before it. The public record is written once, after all five steps succeed. |
| **P6 — publication** | The treaty/embargo public record and notifications are published after P4 succeeds, never before. |
| **P7 — invariants** | Verify: no duplicate active agreement per pair+type; no duplicate live proposal; every active effect has an active agreement/embargo; every class-P event has one outcome; no reservation without a live `ACCEPTED` aid. |

**DIP-102 — One outcome per action.** Each action carries an idempotency key. A retry of the same key returns the recorded outcome and writes nothing new. A break is keyed `agreement_id + BREAK`; an acceptance is keyed `proposal_id + ACCEPT`; an embargo declaration is keyed `imposer + target + declared_turn`.

**DIP-103 — One priority band, five ordered steps.** Within P2 and P4, B-08 orders by `(declared priority, submitted_at, action_id)` under B-02's deterministic rule, and it declares **one** priority band with five steps, applied in this order at every boundary:

| Step | Priority | What runs | Why it sits here |
|---|---|---|---|
| 1 | `EXPIRY_AND_TERMINATION` | Agreement and proposal expiry, and mutual termination that activates this boundary | An expired or terminated agreement must not be activated, renewed, amended or delivered against later in the same boundary |
| 2 | `BREACH` | Breaks that resolve this boundary | A break is an exit the player chose. It must take effect before any new commitment or scheduled transfer, so a player cannot take a delivery and then break in the same boundary (DIP-131) |
| 3 | `ACTIVATION` | New agreements becoming `ACTIVE`, amendments becoming version *n+1*, renewals extending the expiry | Activation applies only to objects still live after steps 1–2; a renewal of an agreement broken at step 2 fails rather than reviving it |
| 4 | `SCHEDULED_OBLIGATION` | Aid delivery due this boundary, and its matched ledger events | Delivery follows activation so that an agreement activated at this boundary can deliver only if its own terms say the same boundary, and a step-2 break has already cancelled it |
| 5 | `EMBARGO` | Embargo declaration, early lift and term expiry | The embargo is a permission change read by another system at settlement; applying it last means a trade accepted before the declaration is grandfathering, not a retroactive block (DIP-095) |

**How a boundary actually runs.** P2 re-validates every submitted action once against the state at the start of the boundary and cancels the invalid ones with their `DPF` code. The band then applies the surviving actions step by step, and **each step re-reads the state committed by the previous step**. An action whose object no longer exists in the required state at its own step fails there with `DPF-01 AGREEMENT_NOT_ACTIVE`, writes no effect and notifies only its actor; it does not roll back an earlier step. Consequences follow the events: the derived breach count (§10), the public record and the notifications are computed after the band from the events actually committed, so a break at step 2 is counted even if a later step at the same boundary fails. One boundary therefore has one committed outcome per object, and no object can be both `EXPIRED` and `ACTIVE`.

**The same-turn cases are fixed by that order.** An agreement expiring and a renewal activating at the same boundary: expiry wins, the renewal fails `DPF-12` (F-DP-009). A termination and a break at the same boundary: termination wins, no breach is recorded. A break and an aid delivery due at the same boundary: the break wins, the delivery is cancelled and the reservation released, and the breach is recorded (DIP-131). A break and an amendment or renewal activating at the same boundary: the break wins and the activation fails `DPF-01`. An embargo declared and a directed trade accepted at the same boundary: a trade **accepted before** the declaration settles; an offer accepted **after** it fails, because the embargo is live from the end of step 5 and the market reads it from the next validation.

**DIP-104 — Publication is after success, and one action is atomic.** A failed action writes no public treaty event, no notification of success and no breach. It writes the failure code to the acting player and leaves that object's previous state intact. Because the five steps of DIP-103 apply to different objects, a failure at step 3 does **not** roll back an expiry or termination already committed at step 1 — those are separate outcomes, each atomic for its own object. A partial write **within one object** is a defect, not a state; a half-applied boundary is never visible.

### 12.2 Declared limits

**DIP-105 — Freeze arithmetic, and exactly which timers it touches.** A nation in `TRANSITION` or `CRISIS` cannot act (DMP-263, DIP-022), so the boundaries it spends there are restored to the timers that protect it — and to nothing else. There are two scopes, and a timer belongs to exactly one:

**(a) Pair-scoped timers** extend by the number of boundaries in the interval on which **either** party was frozen, **each boundary counted once**. When both parties are frozen on the same boundary the extension is **+1**, not +2, because only one boundary of time was lost. These are: a proposal's `expiry_turn`; an agreement's `expiry_turn`; and the **end** of a consultation-notice validity window.

**(b) Actor-scoped timers** extend by the number of boundaries the **acting nation** was frozen. These are: the posture cooldown, the consultation-notice cooldown, the breach cooldown and the embargo re-imposition cooldown. A counterparty's freeze never lengthens the actor's wait, because the actor had the time.

**Not extended, deliberately:**

1. **An embargo's 24-turn term.** It is a fixed sanction duration, not a deadline the target owes. Lengthening a coercive act because the target was politically paralysed would punish a player who could not answer, and the freeze already protects the target from losing anything else.
2. **The 12-turn minimum before a consultation notice becomes usable.** A minimum wait is not a deadline; freezing neither shortens nor lengthens it. Only the window's **end** moves.
3. **The “strictly before expiry” test for a renewal.** It is evaluated against the already-extended `expiry_turn`; extending it twice would double-count the same frozen boundary.
4. **Dormancy.** A dormant nation is not frozen (DIP-128); dormancy expires proposals and preserves agreements without moving any timer.

The freeze begins at the boundary the political state begins and ends at the boundary it ends; a boundary on which the state is in force counts. The interface shows the added turns and the resulting eligible turn. This is the concrete implementation of DMP-263's read-only rule and resolves `DPX-05`; the arithmetic is in the formula register (F-DP-004, F-DP-005, F-DP-006, F-DP-007, F-DP-008, F-DP-009).

**DIP-106 — The limits table.** D-024 requires a visible limit for every action. These are the limits; all values are **Provisional** and belong to Prompt 14.

| Limit | Value | Applies to | Failure |
|---|---|---|---|
| Open outgoing proposals | **3** per nation | A3–A6 | `DPF-06` |
| Live proposals per direction and type | **1** | A3–A6 | `DPF-04` |
| Active agreements | **8** per nation | A7 (activation) | `DPF-11` |
| Proposal response window | **36 turns** | A7/A8/inactivity | `EXPIRED` |
| Posture cooldown | **12 turns** per pair, per direction **+ actor freeze** | A1 | `DPF-08` |
| Consultation notice window | valid **12–36 turns** after sending, **end + pair freeze** | A2, A11 | `DPF-09` |
| Consultation notice cooldown | **12 turns** per pair **+ actor freeze** | A2 | `DPF-10` |
| Breach cooldown | **36 turns** per pair and type **+ actor freeze** | A3 | `DPF-14` |
| Embargo term | **24 turns**, **never freeze-extended** | A11 | `EXPIRED` |
| Embargo re-imposition cooldown | **12 turns** per pair **+ imposer freeze** | A11 | `DPF-08` |
| Agreement term | **360 turns** (`DP-T01`/`DP-T02`) | A3/A5 | `EXPIRED` |
| Aid amount | integer ≥ 1, ≤ payer's available crowns | A3/A7 | `DPF-05` |
| Breach-count window | **4,380 turns** (365 days) | §10 | — |

**DIP-107 — Limits are published, not enforced silently.** The interface shows the current count and the next eligible turn before the action. A hidden throttle, a shadow cooldown or a server-side rejection without a code is a specification defect. Changing a limit is a new `D-` entry, not a tuning edit.
---

## 13. Visibility and notifications

### 13.1 The publication moment (resolves DPX-01)

**DIP-108 — An agreement becomes public when it activates, not when it is accepted.** The sequence is: `PENDING` (parties only) → `ACCEPTED` (parties only) → **`ACTIVE` at the boundary (public)**. Acceptance is a decision between the parties; activation is the effect. This reads B-02 TR-021's "treaty texts once signed" together with D-030's "until it takes effect at a boundary" and adopts the narrowest moment that satisfies both: **both signatures complete and the activation boundary reached**. A one-sided signature is never public.

**DIP-109 — The public treaty record contains:** the type, both nation names, the version, the activation turn, the expiry or completion turn, the current status and the terminal event if any. It does **not** contain private notes, rejection reasons, withdrawal reasons, the negotiation history, the counterparties' other agreements or the terms of an aid agreement's payer treasury. The aid **amount** is public because it is the performed obligation.

**DIP-110 — An embargo is public at declaration.** There is no pending state: a coercive act is declared, and the declaration is the event. The reason is optional and, if given, public.

### 13.2 Visibility matrix

| Field | Actor | Counterparty | Treaty party (other type) | Alliance member | Public | Administrator |
|---|---|---|---|---|---|---|
| Own posture toward X | Yes | Yes | No | No | **Yes** | Restricted audit |
| X's posture toward actor | Yes (it is public) | Yes | No | No | **Yes** | Restricted audit |
| Pending proposal: existence | Yes | Yes | No | No | No | Restricted audit |
| Pending proposal: terms | Yes | Yes | No | No | **No** | Restricted audit |
| Accepted, not active: terms | Yes | Yes | No | No | **No** | Restricted audit |
| Active agreement: record | Yes | Yes | No | Per §18 | **Yes** | Restricted audit |
| Active agreement: private note | Yes | Yes | No | No | No | Restricted audit |
| Rejection / withdrawal reason | Yes | Yes | No | No | **No** (unless A14) | Restricted audit |
| Breach event | Yes | Yes | No | Per §18 | **Yes** | Restricted audit |
| Consultation notice | Yes | Yes | No | No | **No** | Restricted audit |
| Embargo fact and reason | Yes | Yes | No | No | **Yes** | Restricted audit |
| Breach count | Yes | Yes | No | Per §18 | **Yes** | Restricted audit |

**DIP-111 — A treaty party to one agreement learns nothing about the others.** The matrix is per object, not per nation. A NAP counterparty cannot see the aid agreements, postures or proposals of the other party. This prevents a "diplomatic profile" leak by implication.

**DIP-112 — Alliance visibility is not granted here.** B-08 assigns **public** to active treaty records and **private** to pending terms. Prompt 09 may not widen the private class; it may display the public class to its members. Any alliance-only field would need a Prompt 09 decision plus a B-08 amendment, because B-02 TR-021 requires one class per field. `DQ-13` remains Prompt 09's.

**DIP-113 — Aggregates respect k = 5.** If a later interface publishes a diplomatic statistic (for example, "treaties signed this month"), D-027 applies: at least five contributors, stable merging, complementary suppression, no differencing. B-08 itself publishes no aggregate; it publishes named records.

### 13.3 Notifications

**DIP-114 — Nine notification events, one per event, idempotent.** Each is delivered to the named recipient set once, grouped by turn; a retry does not duplicate it. The taxonomy belongs to Prompt 13 (UD-022), but the event set is B-08's.

| # | Event | Recipients | Timing | Content |
|---|---|---|---|---|
| N1 | Proposal received | Counterparty | At submission | Type, proposer, deadline, no terms in the subject line |
| N2 | Proposal expiring soon | Both parties | 12 turns before expiry | The expiry turn and the action still available |
| N3 | Proposal accepted | Proposer | At acceptance | The activation boundary |
| N4 | Proposal rejected | Proposer | At rejection | No reason unless the rejecter publishes one |
| N5 | Proposal withdrawn | Counterparty | At withdrawal | No reason unless the withdrawer publishes one |
| N6 | Agreement activated | Both parties; public record | At P6 | Type, version, expiry |
| N7 | Agreement expiring soon | Both parties | 24 turns before expiry | The expiry turn and the renewal route |
| N8 | Agreement terminated / breached / expired | Both parties; public record for breach/expiry | At P6 | Which terminal state, who acted (break only) |
| N9 | Embargo declared / lifted / expired | Both parties; public record | At P6 | Scope summary and end turn |

**DIP-115 — No notification contains a private term of another pair.** N1/N2/N3 show the recipient its own proposal only. N7 shows the parties their own expiry. A public record notification (N6/N8/N9) names the parties and type, never a private note or a third party's terms.

**DIP-116 — A player may not opt out of a consequence notification.** N8 and N9 (breach, termination, embargo) always reach the affected player, because they change what the game will permit. Digest preferences may group them, but not suppress them. N1/N3/N6 may be grouped; N2/N7 (deadline warnings) may not be suppressed while the player has an open decision.

---

## 14. Event history and audit

**DIP-117 — Class-P events.** The following are permanent, append-only and public unless marked private: `AGREEMENT_PROPOSED` (private), `AGREEMENT_ACCEPTED` (private), `AGREEMENT_ACTIVATED` (public), `AGREEMENT_AMENDED` (public record; old version retained), `AGREEMENT_RENEWED`, `AGREEMENT_TERMINATED` (public fact, private reason), `AGREEMENT_EXPIRED`, `AGREEMENT_BREACHED` (public, with breaker), `AID_SETTLED` (public amount), `EMBARGO_DECLARED`, `EMBARGO_LIFTED`, `EMBARGO_EXPIRED`, `POSTURE_SET` (public), `REASON_PUBLISHED`.

**DIP-118 — Class-S events.** `PROPOSAL_REJECTED`, `PROPOSAL_WITHDRAWN`, `PROPOSAL_EXPIRED`, `CONSULT_NOTICE_SENT`, `POSTURE_COOLDOWN_STARTED`. These are retained under D-026's summarised class; they are not permanent. A rejection or withdrawal that the parties want preserved can be published through A14, which is class-P.

**DIP-119 — One event per outcome, with provenance.** Every event records: event ID, agreement/proposal/embargo ID, actor nation, counterparty, turn, rule ID (`DIP-…`), version (where applicable), and the idempotency key. An event with no rule ID is a defect. A correction is a new event referencing the original (TR-091), never an edit.

**DIP-120 — The retired nation keeps its record.** A reroll does not delete treaty events or the breach count. The old nation's page shows them; the replacement's page does not. This is RRL-019/RRL-020 applied to B-08.

**DIP-121 — Audit access is restricted and logged.** An administrator may read the full history only under Prompt 12's restricted class. Every privileged read is itself audited (D-042). B-08 publishes no "admin view" to players.

---

## 15. Failure, integrity and race rules

### 15.1 Failure codes

| Code | Name | Meaning | Player next step |
|---|---|---|---|
| `DPF-01` | `AGREEMENT_NOT_ACTIVE` | The agreement is not in `ACTIVE`/`ACCEPTED`, or the action needs a state it does not have | Refresh; the agreement may have expired or ended |
| `DPF-02` | `NATION_UNAVAILABLE` | The counterparty is retired, removed, dormant or otherwise unavailable | Choose another counterparty; dormancy is protective |
| `DPF-03` | `UNAUTHORIZED` | The actor does not own the nation, or a delegated act has no approved scope | Act from the owning account |
| `DPF-04` | `DUPLICATE_PROPOSAL` | A live proposal or active agreement already exists for the pair and type, including a reciprocal winner | Withdraw, wait, or use the existing object |
| `DPF-05` | `INSUFFICIENT_CROWNS` | The payer cannot reserve the aid amount | Lower the amount or wait |
| `DPF-06` | `PROPOSAL_CAP` | Three outgoing proposals are already pending | Withdraw one or wait for an expiry |
| `DPF-07` | `AUTHORITY_SUSPENDED` | The nation is in `TRANSITION`/`CRISIS`; diplomacy is read-only | Wait for the state to end; deadlines are frozen |
| `DPF-08` | `COOLDOWN` | The posture or embargo cooldown is running | The message names the eligible turn |
| `DPF-09` | `CONSULT_NOTICE_REQUIRED` | A `DP-T02` requires a valid notice before this hostile act | Send a notice; wait 12 turns |
| `DPF-10` | `NOTICE_COOLDOWN` | A notice was sent to this pair less than 12 turns ago | Wait for the eligible turn |
| `DPF-11` | `AGREEMENT_CAP` | Eight active agreements are already held | Terminate or wait for expiry |
| `DPF-12` | `AGREEMENT_EXPIRED` | The agreement expired before the renewal could activate | Propose a new agreement |
| `DPF-13` | `INVALID_TERMS` | The terms are malformed, a type change disguised as an amendment, or an amount below 1 | Correct the proposal |
| `DPF-14` | `BREACH_COOLDOWN` | The same type to the same counterparty is blocked for 36 turns after a break | Wait, or use another type |
| `DPF-15` | `POSTURE_REQUIRED` | The embargo requires the imposer to hold `HOSTILE` posture toward the target | Change posture (subject to the 12-turn cooldown), then declare |

**DIP-122 — A failure is not a partial success.** If validation fails at any point, nothing changes: no event, no notification, no reservation, no cooldown consumed (except the action's own submission attempt, which writes only the failure line to the actor). A failed acceptance leaves the proposal `PENDING`; a failed activation leaves the agreement `ACCEPTED` and retries at the next boundary **only if the cause is transient** (a failed turn), otherwise it fails closed and notifies both parties.

### 15.2 Integrity rules

**DIP-123 — No self-dealing.** A nation may not propose to itself, embargo itself, or hold two parties to one agreement. The validator rejects `from == to`.

**DIP-124 — No duplicate object, and the three keys are not the same shape.** A proposal is **directed**, so its key is ordered: `(from_nation, to_nation, type, PENDING)`. An agreement is **mutual**, so its key is unordered: `({nation_a, nation_b}, type, ACCEPTED|ACTIVE)`. An embargo is **directed coerced**, so its key is ordered: `(imposer, target, ACTIVE)`. This distinction is the reason A→B and B→A proposals can both be `PENDING` while only one agreement of that type can exist afterwards (DIP-044, DIP-050, DIP-052). A database-level uniqueness constraint is recommended at Stage 5; B-08 states the rule now.

**DIP-125 — No stale authorization.** Authority, pair state, caps, reservation and the political state are re-checked at submission, at P2 and (for an aid) at P4. A change between submission and resolution fails the action with the code for the new state; it never resolves under the old authority.

**DIP-126 — No resurrection.** A terminal agreement cannot be returned to `ACTIVE` by a late boundary, a retry or a recovery. A retry of the activating action returns the recorded outcome; it does not re-activate.

**DIP-127 — Reroll cleanup.** On a reroll, at the transaction boundary: every `PENDING` proposal to or from the old nation is `WITHDRAWN` with reason `NATION_RETIRED` (no breach, no notification beyond the counterparty); every `ACCEPTED`/`ACTIVE` agreement becomes `TERMINATED` with reason `NATION_RETIRED` and a class-P event attributed to the **old** nation; every reservation is released; every embargo imposed by or on the old nation becomes `LIFTED` with reason `NATION_RETIRED`; the replacement starts `NEUTRAL` toward everyone with no agreements and breach count 0. This implements RRL-019 and DIP-086.

**DIP-128 — Dormancy cleanup.** A nation becoming dormant: its open outgoing and incoming proposals become `EXPIRED` with reason `COUNTERPARTY_DORMANT` (no breach, one notification); its active agreements **persist** and their effects continue (a NAP still blocks a declaration; an aid still delivers); its embargoes persist to their term. A dormant nation cannot be the target of a **new** proposal or embargo (`DPF-02`); it cannot initiate anything. This applies D-028 and does not add a penalty.

**DIP-129 — Aid and a voided turn.** If the boundary that would deliver an aid is voided by an operator decision (D-025), the agreement returns to `ACCEPTED` with its reservation intact and retries at the next successful boundary. If the reservation was released by the void, the payer is asked to re-confirm; if it does not confirm within 12 turns, the agreement becomes `TERMINATED` with reason `TRANSFER_VOIDED`, **not** `BREACHED`. The recipient is told the transfer did not occur. No player is punished for an operator event.

**DIP-130 — Simultaneous actions.** Every pair of actions at the same boundary is resolved by DIP-103's order. The table below is the authoritative outcome matrix for the races B-08 creates.

| Race | Outcome |
|---|---|
| A accepts; B withdraws at the same boundary | Both are recorded changes, not boundary events: the **first recorded** submission wins. If the withdrawal was recorded first, the proposal is already `WITHDRAWN` and the acceptance fails at submission with `DPF-01`; if the acceptance was recorded first, the withdrawal fails. P2 never revives a state that a recorded action already changed (DIP-047, DIP-048). |
| A and B accept reciprocal proposals | The lower `(submitted_at, action_id)` acceptance wins; the other fails `DPF-04`. |
| A renews; the agreement expires at the same boundary | Expiry is ordered before activation; the renewal fails `DPF-12`. A new agreement is needed. |
| A terminates; B breaks at the same boundary | Termination is ordered before breach; the agreement is `TERMINATED`, no breach event. |
| A breaks; B breaks at the same boundary | The first break wins; the second fails `DPF-01`; one breach event. |
| A declares an embargo; B accepts a directed trade at the same boundary | The embargo is ordered before the trade's settlement **only for offers accepted after the declaration**; an already-accepted trade at that boundary settles (grandfathering). The market records the outcome. |
| A sets `HOSTILE`; B declares an embargo on A at the same boundary | The two are independent: A's posture is its own; B's eligibility depends on **B's** posture toward A, not A's toward B. No conflict. |
| A's nation enters `TRANSITION`; a proposal expires at the same boundary | The freeze applies from the boundary the state begins; if the state is already in force at P2, expiry is suspended (DIP-105). The proposal survives. |
| A rerolls; a proposal is accepted at the same boundary | The reroll transaction is outside the boundary; if it completes first, the proposal fails `DPF-02`; if the acceptance resolves first, the agreement terminates at the reroll. One outcome only. |
| A breaks; an aid delivery is due at the same boundary | Breach is step 2 and delivery is step 4, so the break cancels the delivery and releases the reservation; the breach is recorded (DIP-131). This prevents a player from taking the value and breaking in the same boundary. |
| A breaks; an amendment or renewal is due to activate at the same boundary | Breach (step 2) precedes activation (step 3); the agreement is `BREACHED` and the amendment/renewal fails `DPF-01` (or `DPF-12` for a renewal whose expiry has also passed). Nothing revives a broken agreement in the same boundary. |
| A's embargo term expires; A re-declares at the same boundary | Expiry runs at step 5 and sets `end_turn`; the re-imposition cooldown is `end_turn + 12` (F-DP-008), so a same-boundary re-declaration fails `DPF-08`. A declaration **submitted** at the boundary is not a duplicate of the expiring one (DIP-124). |

**DIP-131 — The break-before-delivery rule is deliberate.** Step 2 (`BREACH`) precedes step 4 (`SCHEDULED_OBLIGATION`), so a payer who breaks before or at the delivery boundary does not deliver. This is the one place where an ordering choice favours the breaker, and it is justified: the reservation is the payer's value, the recipient has not yet received it, and allowing a same-boundary delivery-then-break would let the payer appear generous while recording a breach. The recipient is notified that the delivery was cancelled by the break, and the break still costs the breaker the public record, the derived count and the 36-turn cooldown (DIP-073). Breaking an `ACCEPTED` aid before it activates is a break of that agreement: it cancels the activation and the delivery in the same step, and the agreement becomes `BREACHED`, not `TERMINATED` (DIP-056).

**DIP-132 — No double reservation.** An aid's crowns are reserved once at acceptance. A second acceptance of the same proposal (a duplicate click) returns the recorded outcome; it does not reserve twice. A retry after a failed P2 does not reserve until the retry succeeds.

**DIP-133 — No silent failure.** Every rejected action writes a failure line to the actor with the code and the rule ID. A rejection that the player cannot see is a defect. `DPF` codes are stable; changing one needs a documentation correction, not a silent rename.

**DIP-134 — Invariants checkable at P7.** (1) No **ordered** pair+type has two `PENDING` proposals in the same direction. (2) No **unordered** pair+type has two `ACCEPTED`/`ACTIVE` agreements. (3) No pair has two `ACTIVE` embargoes in the same direction. (4) Every `ACTIVE` effect has an `ACTIVE` object. (5) Every reservation belongs to an `ACCEPTED` aid or none. (6) Every public record has exactly one terminal event. (7) The breach count equals the number of `BREACHED` events in the window. (8) No retired nation has an `ACTIVE` agreement or embargo. (9) Every class-P event has a rule ID and a turn. A failed invariant is a defect to investigate, never a value to "fix" in place.

---

## 16. Formulas

**DIP-135 — The formula register is authoritative.** Every calculation in B-08 is in [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md): the twelve formulas `F-DP-001`…`F-DP-012` cover caps, expiry, cooldown, notice windows, embargo term, breach count, transfer conservation, version increment and the freeze extension. Each has a unit, a range, a rounding rule, a timing, an example and a validation expectation. No formula is duplicated here.

**DIP-136 — Every value is provisional.** The numbers in §6, §10 and §12 are structural defaults chosen for testability, not balance claims. Prompt 14 owns them. No value may be described as balanced, tested or final. A later tuning change edits the register and the rule's value together; it does not create a second formula.

**DIP-137 — No formula without a purpose.** B-08 does not add a prestige curve, a trust decay, a relation score or a "war exhaustion" term. The absence is deliberate: every formula in the register corresponds to a rule a player can see and a test can check. A future formula needs a named purpose and a decision.

### 16.1 Register discipline

Six rules govern the register itself rather than a calculation. They are numbered `DIP-152`…`DIP-157` — after the rules they govern — and their **full text is stated once**, in §10 of [`15_diplomacy_formula_register.md`](15_diplomacy_formula_register.md). They are binding rules, not register notes:

| Rule | One-line statement |
|---|---|
| **DIP-152** | Values live in one place: a value appears in the rule as a named parameter and in the register as its definition; a third copy is a defect. |
| **DIP-153** | Arithmetic checks are **document checks**; 08C/14 recompute examples, and no runtime claim follows from a match. |
| **DIP-154** | Every formula is validated at its bound, one below and one above, plus the freeze case and the retired-nation case. |
| **DIP-155** | Every surface that shows a limit or term labels it **provisional** until Prompt 14; no player-facing claim that a value is balanced is permitted. |
| **DIP-156** | **One authority:** B-08 wins on *what* happens, the register on *how it is calculated*; a second formula for one value is a defect. |
| **DIP-157** | **No numeric reputation:** the register has no trust, honour, standing, prestige or score formula. `F-DP-010` counts events and feeds nothing. A score requires a new decision and the reversal of DIP-084. |

---

## 17. Cross-system integration

### 17.1 The contract rule

**DIP-138 — One rule, one owner, one read.** For every interface, exactly one document owns the rule and the other reads it. A second copy of the rule is a defect even if it agrees today. B-08 may **consume** an earlier rule; it may not restate it with a different number, and it may not change it to make diplomacy easier.

**DIP-139 — Every B-08 action declares its phase and its event class.** A3–A6 submit immediately (class S/I for the proposal record) and resolve at P4; A7 reserves at acceptance and activates at P2/P4; A10 breaks at P2/P4; A11 declares at P2/P4. The event class per action is in §9.

### 17.2 Integration matrix

| Source | Rule / decision | Status | What B-08 does with it | Relationship | Follow-up |
|---|---|---|---|---|---|
| **B-02 §9** | TR-019 posture directional; Agreement mutual; alliance 09; conflict 10 | Provisional | Adopts the three layers; posture catalogue is §4; agreement object is §7 | **Compatible** | None; 08C tests |
| **B-02 §9** | TR-020 / D-030 pending-act visibility | D-030 Confirmed | Implements: pending terms parties-only; public at activation; private rejection; A14 publication | **Dependency** | 08C tests the sequence |
| **B-02 §9** | TR-021 / TR-022 / D-027 classes and k = 5 | Provisional/Confirmed | One class per field (§13); no aggregate; no leakage | **Dependency** | 08C/13 display; 12 audit |
| **B-02 §13–§19** | P0–P7; class Q/S; P2 re-validation; P4 application; reservation; `F` codes; idempotency | Provisional | DIP-100…DIP-104, DIP-119, DIP-122, DIP-130 | **Dependency** | 08C writes failure paths |
| **B-02 §24** | TR-093 15 declarations; D-024 visible limit | Confirmed | §12 limits table; §9 phases; §14 events; §15 invariants | **Dependency** | 08C verifies the 15 |
| **B-02 TR-096** | Prompt 08 inherits relationship types, consent, visibility, D-030; returns treaty effects, breach, publication timing | Provisional | Returns: three agreements + one act; breach via break; publication at activation (§13) | **Dependency discharged** | 08C tests; 15 consolidates |
| **B-03 §5.5, §18** | Restricted pair cannot treaty; no indirect route | Provisional | DIP-074; pair check at submission/acceptance/P4; suspension rule | **Dependency** | 08C tests the block |
| **B-03 RRL-019** | Reroll terminates treaties; class-P event; replacement neutral | Provisional | DIP-127 implements it; breach count nation-scoped (DIP-086) | **Dependency** | 08C tests cleanup |
| **B-03 RRL-021** | Reroll blocked in campaign/settlement/hold | Provisional | Not modified; the escape limitation is disclosed in DIP-087 | **Compatible** | Prompt 10/12 |
| **B-03 ACC/NET** | Three state machines; one account/one nation | Confirmed | DIP-013, DIP-079 | **Approved constraint** | None |
| **B-04 ECN-212** | Aid/reparation/embargo/sanction envelope; transfers with matched ledger; embargo destroys nothing; no negative balance; P4; D-030 | Provisional | Adopts crowns-only aid and transfer-based embargo; no parallel balance | **Dependency** | 08C settlement path; 04 ledger |
| **B-04 ECN-087/092; D-049/050/055** | Aid route; one currency; no debt; append-only ledger | Provisional/Confirmed | DIP-040, DIP-071, DIP-132 | **Approved constraint** | 08C conservation test |
| **B-05 URB-155** | Sanction may freeze construction/research; may not delete; aid moves crowns only | Provisional | The adopted embargo does not touch construction/research; aid is crowns-only | **Compatible / stricter** | None; future sanction needs 05 |
| **B-06 DMP-138** | No approval/population modifier without a named 08 term; sanction may freeze policy | Provisional | B-08 adds no modifier; embargo does not touch policy | **Compatible / stricter** | None |
| **B-06 DMP-263** | Treaties persist through `TRANSITION`/`CRISIS`; read-only; leadership change does not void | Provisional | DIP-022, DIP-062, DIP-105 implement freeze and persistence | **Dependency** | 08C tests |
| **B-06 REQ-360/361/387** | Persistence; no confiscation | Provisional | DIP-070, DIP-127 | **Compatible** | None |
| **B-07 MKT-185** | Diplomacy/war restriction is separate; not a market fee | **Approved constraint** | DIP-096, DIP-098; embargo is a permission block, no fee | **Dependency** | 08C market interface test |
| **B-07 MKT-217/218/220** | One rule one owner; market reads a B-08 embargo; political interface one-way | Provisional | B-08 owns the embargo object; B-07 reads it; no market edit | **Dependency / interface** | 08C records the row |
| **B-07 D-016/D-017/D-110…D-122** | Directed trade, visibility, listing, Global Trade gates | Confirmed/Provisional | Not reopened; an embargo blocks new offers/acceptances only | **Compatible** | Preserve |
| **07C §6/§15** | "Nothing at launch"; 08 inherits market; may not add fee/tariff without a decision; must add restriction to B-08 and record interface | Accepted | D-129 is that decision; the interface row is §17.3; no `MKT-` rule edited | **Dependency discharged** | 08C tests |
| **Prompt 09** | Alliance founding/governance/membership/diplomacy | Registered | B-08 publishes the object and the interface only (§18); no alliance rule | **Boundary** | 09 |
| **Prompt 10** | War declaration, campaign, peace | Registered | NAP is a permission block, inert until 10; no campaign rule | **Dependency** | 10 |
| **Prompt 11** | Chronicle/rankings | Planned | Class-P public records are chronicle inputs; no ranking score | **Dependency** | 11 |
| **Prompt 12** | Enforcement, appeals, audit | Planned | Administrator may restrict account/pair, never sign/break; restricted audit | **Dependency** | 12 |
| **Prompt 13** | Screens, notifications | Planned | Nine events and visibility matrix; taxonomy is 13's | **Dependency** | 13 |
| **Prompt 14** | Numbers and balance | Planned | Every value Provisional; formula register | **Dependency** | 14 |

### 17.3 The contract table

| System | B-08 needs | B-08 returns | Owner of the rule |
|---|---|---|---|
| **B-02 turn engine** | P2/P4/P6/P7 phases; class Q/S; reservation; idempotency; `F` codes; visibility classes | Action list, phases, priority band, event classes, limits | B-02 |
| **B-03 accounts/nations** | Ownership from session; pair check; reroll cleanup; dormancy; data classes | Treaty termination event, neutral restart, pair-block reason | B-03 |
| **B-04 economy** | Reservation, transfer, ledger, no debt, zero floor | Aid intent (`A` crowns, payer, recipient, `transfer_id`), no mint/burn | B-04 |
| **B-05 cities/research** | None for the adopted catalogue | No sanction that touches capacity/DC/RP | B-05 |
| **B-06 politics** | `TRANSITION`/`CRISIS` flag and freeze duration | Treaty persistence, freeze extension, no approval modifier | B-06 |
| **B-07 market** | Reads `EMBARGO_ACTIVE(pair)` for new directed offers/acceptances | Embargo object with imposer, target, start/end, reason | **B-08** |
| **Prompt 09 alliances** | Membership event on join/leave/removal/reroll; role model later | Treaty object contract, authority contract, visibility, public record | **B-08** for nation-level; no B-08 alliance object (`D-137`); separate B-09 `AT-` object authorized by `D-140` |
| **Prompt 10 warfare** | `WAR_DECLARATION` checks an active NAP; a violation writes `BREACHED` | NAP check and breach event | **B-08** for the permission; 10 for the war |
| **Prompt 11 chronicle** | Public class-P events with provenance | Event list and visibility | B-08 emits; 11 displays |
| **Prompt 12 fair play** | Restricted audit; account/pair measures | No reputation register; no hidden record | B-03/12 |
| **Prompt 13 interface** | States, labels, deadlines, failure sentences, nine notifications | Visibility matrix, `DPF` sentences, confirmation content | B-08 |
| **Prompt 14 formulas** | Values, units, bounds, rounding, examples | `F-DP-001`…`F-DP-012` | B-08 register; 14 tunes |

**DIP-140 — The embargo hook is one-way.** B-07 reads a boolean/object from B-08; B-08 never reads a market price, fee or statistic. This preserves MKT-220's one-way political interface. If B-07 cannot read the hook without a change to a `MKT-` rule, that is a separate correction owned by the market document, not a B-08 edit.

**DIP-141 — The NAP hook is a permission, not a war rule.** B-08 states that a war declaration between NAP parties is not permitted; Prompt 10 owns the declaration, its costs and its consequences. Until Prompt 10 exists, the hook is **declared and inert**; the NAP is still a public record and still a promise. This is the honest status, not a claim that a war block is enforced today.

**DIP-142 — No B-08 rule depends on a system that does not exist.** The only forward dependency is the NAP's enforcement by Prompt 10. Every other B-08 action is fully specified within B-02/B-03/B-04/B-06/B-07 as they stand. If a later system changes a consumed rule, B-08 is re-read against it; it does not pre-empt it.

### 17.4 Protections preserved

**DIP-143 — Global Trade is untouched.** B-08 does not change D-122, DD-136, REQ-513, any `MKT-` rule, any `F-TM-` formula or G-1…G-6. The embargo blocks **directed** offers/acceptances and aid; it does not create a listing rule, a tariff or a release gate. Global Trade remains approved mandatory scope and release-gated.

**DIP-144 — The market's accounting is untouched.** No B-08 action moves value except the aid transfer, which uses B-04's matched ledger events. An embargo moves nothing. A break moves nothing. No hidden fee exists.

**DIP-145 — The political and city contracts are untouched.** The adopted catalogue has no construction, research, policy, approval, stability, population or capacity effect. URB-155 and DMP-138 are respected by not using the envelope they bound.

---

## 18. The Prompt 09 interface contract

### 18.1 Boundary

**DIP-146 — Prompt 09 owns the Alliance System.** Founding, constitution, leadership, ranks, internal permissions, membership, shared resources, collective decisions, alliance diplomacy and operations are Prompt 09's. B-08 does **not** define any of them. This section is a contract, not an alliance design.

**DIP-147 — B-08 owns nation-level diplomacy.** A treaty between two nations is a B-08 object even if both nations belong to alliances. Membership does not make an alliance a party, a guarantor or a decision-maker. `UD-039` is resolved by `D-137`: there is no **B-08** alliance-level treaty object and no reuse of the B-08 object. `D-140` (Prompt 09B-I) amends only the separate-object component by authorizing a **B-09** `AT-T01`–`AT-T05` object; it creates no B-08 party, no B-08 term and no delegation. An alliance cannot be a B-08 treaty party; only the owning nation can sign a B-08 treaty.

**DIP-148 — No delegation is granted by B-08.** An alliance leader cannot sign, accept, break or terminate for a member. Prompt 09 may propose a delegation model, but it must state the scope, revocation, audit and re-validation; until a `D-` entry adopts it, a delegated act is `DPF-03`. **Resolved by Prompt 09 under D-137:** no delegation model is adopted; zero diplomatic delegation remains binding.

### 18.2 Contract rows

| # | Interaction | Owner | What crosses the boundary | Constraint | Open question |
|---|---|---|---|---|---|
| **A-01** | A nation treaty where both parties are in alliances | **B-08** | Nation IDs, agreement ID, status | The alliance is not a party; membership creates no obligation | `DQ-11` |
| **A-02** | An alliance-to-alliance treaty | **Separate B-09 object** (`D-140`); never B-08 | B-09 agreement ID, type and covered-nation consents | No B-08 object exists or is reusable for an alliance; `D-137` zero delegation remains; B-09 requires per-nation consent | Resolved by `D-137`, amended in part by `D-140` |
| **A-03** | An alliance acting for a member | **No delegation** (`D-137`) | — | Zero diplomatic delegation; only the authenticated nation owner may act | Resolved by `D-137` |
| **A-04** | A member joins/leaves/is removed during a treaty | **Joint** | Membership event, agreement IDs | B-08: the nation treaty **persists**; membership changes nothing. 09 must emit the event | `DQ-11` |
| **A-05** | A restricted pair in the same alliance | **B-03** (restriction) / **B-08** (block) | Pair state | 09 may not create an alliance route; B-08 rejects | Closed: DIP-074 |
| **A-06** | An alliance-wide embargo or sanction | **Prompt 09** | Sanction object, authorizing role | B-08 has **no** collective sanction; 09 would need its own act and a new decision | `DQ-13` |
| **A-07** | Visibility of a nation treaty to alliance members | **B-08** assigns; **09** displays | Class per field | 09 may display only the public class; pending terms stay private | `DQ-13` |
| **A-08** | Notifications to an alliance about a member's treaty | **B-08** emits; **13** renders | Event IDs, recipient set | No third-party disclosure of pending terms | `DQ-13` |
| **A-09** | A war involving an alliance or member | **Prompt 10** | War ID, sides | B-08 has no war rule; a NAP is only a declaration permission | `DQ-14` |
| **A-10** | Alliance standing / reputation | **Prompt 09** if it exists | — | 09 must not read a B-08 reputation (none exists) or invent a parallel national one | `DQ-13` |
| **A-11** | A shared pool funding aid | **Prompt 09 / B-04 / B-08** | Pool ID, transfer ID, amount | B-08 knows only a nation payer; a pool is not a B-08 party | `DQ-15` |
| **A-12** | A reroll while in an alliance and a treaty | **B-03 / 09 / B-08** | Nation ID, membership, agreement IDs | B-08 terminates and records; 09 ends membership and vacates roles; neither transfers assets | `DQ-11` |

### 18.3 What Prompt 09 must be told

1. **The object contract:** `agreement_id`, two nation parties, type (`DP-T01`…`DP-T03`), version, status, activation/expiry, visibility class, event classes.
2. **The authority contract:** only the authenticated nation owner; no inherited consent; no delegation; a leadership change does not void a treaty.
3. **The membership rule:** a nation treaty **persists** through join/leave/removal; the alliance is not a party and is not liable. A reroll terminates the treaty and ends membership.
4. **The pair contract:** the B-03 check and its reason code; suspension on a later restriction; no alliance route.
5. **The embargo contract:** only a nation may impose one; an alliance cannot; a shared pool cannot fund one.
6. **The visibility contract:** public active record; private pending terms; no alliance-only field without a B-08 amendment.
7. **The notification contract:** N1–N9; 09 may distribute the public ones to its members, never the private ones.
8. **Acceptance scenarios** for after both designs exist (§18.4).

### 18.4 Cross-system scenarios for later verification

These are **not executed tests**. They are the cases Prompt 08C/09 must check together.

1. Two allied nations sign a NAP; the alliance is not a party; members see only the public record.
2. A nation leaves its alliance mid-NAP; the NAP persists and the alliance receives the membership event, not a treaty change.
3. A restricted pair in one alliance attempts a NAP; blocked with the B-03 reason; no bank route.
4. A member rerolls; membership ends, roles vacate, the treaty terminates and the old nation's page keeps the record.
5. An alliance attempts to sign a B-08 alliance-level treaty; `D-137` and `D-140` confirm B-08 has no such object and B-08 refuses the act. A separate B-09 `AT-` treaty is a different object and requires per-nation consent.
6. A collective embargo is proposed; it has no B-08 path, so 09 must define its own authority or decline.
7. A member in `TRANSITION` cannot sign; the treaty persists; its deadlines freeze.
8. A dormant member's treaty remains readable and its NAP effect persists; no new proposal targets it.
9. A pool funds an aid; B-04 has matched ledger events and B-08 sees a nation payer, not a pool.
10. A public record exposes no private term; no alliance view widens it.

**DIP-149 — Prompt 09 may not silently override a B-08 rule.** If 09 needs a different membership effect, it must state the conflict, name B-08's rule and propose a coordinated amendment. B-08 may not silently override 09 either. A conflict is resolved by a joint `D-` entry, not by one document editing the other.

---

## 19. Open decisions and dependencies

### 19.1 Resolved by this document

| ID | Question | Resolution |
|---|---|---|
| **UD-013** | What does a treaty do beyond a non-aggression analogue? | **Resolved** by D-124: NAP = war-declaration block; consultation = notice gate; aid = crown transfer. No other effect exists. |
| **UD-033** | Is diplomatic/treaty reputation account- or nation-scoped after a reroll? | **Resolved** by D-128: no score; nation-scoped breach count; replacement starts at zero; limitation disclosed. |
| **DPX-01** | When does a signed treaty become public? | **Resolved** by DIP-108: at activation, not at one-sided signature or acceptance. |
| **DPX-02** | Is the relationship model symmetric? | **Resolved** by DIP-023: posture directional, agreement mutual. |
| **DPX-03** | Reroll vs account reputation | **Resolved** by DIP-086/DIP-127: nation-scoped, no account record. |
| **DPX-04** | Diplomacy–market embargo ownership | **Resolved** by DIP-095/140: B-08 owns the embargo; B-07 reads it; no fee. |
| **DPX-05** | Read-only diplomacy vs pending proposals | **Resolved** by DIP-022/DIP-105: freeze, extend deadlines. |
| **DPX-06** | Alliance treaty ownership | **Resolved by `D-137`, amended in part by `D-140`:** no B-08 alliance-level object and zero delegation; a separate B-09 `AT-` object now exists. B-08's refusal remains correct. |

### 19.2 Open and deferred

| ID | Question | Owner | Status |
|---|---|---|---|
| **UD-039** | Do alliance-level treaties reuse the B-08 object, and may an alliance delegate diplomacy for a member? | **Prompt 09** | **Resolved by D-137 (Prompt 09B), amended in part by D-140 (Prompt 09B-I)** — no B-08 alliance-level treaty object and zero diplomatic delegation; B-08's refusal remains correct, while a separate B-09 `AT-T01`–`AT-T05` object exists outside B-08 |
| **DQ-04** | May a treaty ever drag a nation into war automatically? | **Prompt 10** | **Deferred** — no MDP in B-08; revisit only with the war rules. |
| **DQ-14** | Is a diplomatic declaration a precondition for war? | **Prompt 10** | **Deferred** — B-08 defines only the NAP permission. |
| **DQ-15** | May an alliance pool fund aid? | **Prompt 09 / B-04** | **Deferred** — B-08 has no pool party. |
| **DQ-13** | What may an alliance see of a member's diplomacy? | **Prompt 09 / 13** | **Deferred** — B-08 fixes public vs private; 09 may not widen private. |
| **UD-037/UD-038** | Market calibration | **Prompt 14 / Stage 3** | Unchanged; B-08 does not touch them. |
| **Every number in §6/§10/§12** | Values | **Prompt 14** | **Provisional** — see the formula register. |

### 19.3 Known limitations

1. **The NAP's effect is inert until Prompt 10.** The record and the promise exist; the war block cannot be exercised because no war declaration exists. This is honest, not a hidden gap.
2. **The reroll escape is real.** A player can shed a breach count by rerolling. DIP-087 discloses it; the mitigation is the public retired page and B-03's separate enforcement.
3. **No player research.** The confirmation, notification and visibility choices are design analysis, not verified usability. Prompt 13 must test them.
4. **No counterproposal or mediation.** A rejection is free and final; negotiation happens outside the object. This is a deliberate simplification, not an oversight.
5. **No alliance diplomacy.** A whole class of treaty is deferred to Prompt 09; B-08 cannot claim the diplomacy system is complete without it.
6. **No runtime evidence.** Nothing here has been implemented, so no timing, concurrency, load or security property is tested.
7. **The break-before-delivery ordering is a judgement.** It favours the breaker in one boundary; DIP-131 states why and 08C must test the alternative.
---

## 20. Worked examples

All turn numbers are **illustrative test assumptions**, not balance claims. Names are fictional. The examples use the rules as written; an example never introduces a mechanic the specification does not contain.

### E1 — A proposes a non-aggression pact

- **Initial state:** Arcadia (player A) and Bravia (player B) are `NEUTRAL` toward each other, no agreements. Turn 1000.
- **Initiating player:** A.
- **Available choices:** propose `DP-T01`, propose `DP-T02`, propose `DP-T03`, change posture, do nothing.
- **Decision:** A proposes `DP-T01`, term 360 turns. The confirmation shows: activation at the next boundary after acceptance, expiry 360 turns later, no cost, breach = public record + 36-turn same-type cooldown, no automatic renewal.
- **Other participant:** none yet.
- **Validations:** A owns Arcadia; B is active, not dormant, not retired; pair not restricted; no live `DP-T01` between them; A has 0/3 outgoing proposals; A holds 0/8 agreements.
- **Result:** proposal `PENDING`, `submitted_turn 1000`, `expiry_turn 1036`. No agreement exists. B sees the terms; third parties see nothing.
- **Costs:** none.
- **History:** `AGREEMENT_PROPOSED` (private), class P on acceptance only; the proposal itself is class S.
- **Notifications:** N1 to B at submission; N2 to both at 1024.
- **Why authority is preserved:** A chose to propose; B has not been committed to anything; A may withdraw until B accepts.

**Reciprocal variant (same turns).** B proposes `DP-T01` to A at turn 1002, before answering A's proposal. Both are `PENDING`: a proposal's identity is the **ordered** key `(from, to, type)` (DIP-044, DIP-124), so B's proposal is not a duplicate of A's. B accepts A's proposal at turn 1003. At P2 of the next boundary A's proposal becomes `ACCEPTED`, and B's own outgoing proposal fails with `DPF-04` because the pair now holds an `ACCEPTED` agreement with the **unordered** key `{A,B}` + `DP-T01` (DIP-050). A never accepted B's proposal, so no second agreement exists and no term is inherited from the losing record; had both accepted in the same boundary, the lower `(submitted_at, action_id)` acceptance would win and the other would fail the same way.

### E2 — B rejects the proposal

- **Initial state:** E1's proposal is `PENDING` at turn 1004.
- **Initiating player:** B.
- **Available choices:** accept, reject, ignore, propose a different type.
- **Decision:** B rejects.
- **Other participant:** A receives N4.
- **Validations:** B owns Bravia; the proposal is addressed to B and is `PENDING`; the version matches.
- **Result:** `REJECTED`, `responded_turn 1004`. No agreement. No cooldown. A's outgoing cap is released. The rejection reason is private and not recorded unless B uses A14.
- **Costs:** none.
- **History:** `PROPOSAL_REJECTED` (class S, private).
- **Notifications:** N4 to A, without a reason.
- **Why authority is preserved:** B's refusal is final and free; the system did not auto-reject on B's behalf, and A cannot force acceptance.

### E3 — B accepts; the pact activates

- **Initial state:** A re-proposes at 1010 (the rejection did not create a cooldown). B accepts at 1010, before the boundary.
- **Initiating player:** B (acceptance).
- **Available choices:** accept, reject, ignore.
- **Decision:** B accepts.
- **Other participant:** A.
- **Validations:** submission check passes; at P2 on 1011: authority, pair state, no duplicate, caps, expiry (1011 < 1046), version, no political freeze.
- **Result:** proposal `ACCEPTED`; agreement created `ACCEPTED`; at P4 on 1011 it becomes `ACTIVE`, `activation_turn 1011`, `expiry_turn 1371`. Public record written at P6. No reservation (NAP is free).
- **Costs:** none.
- **History:** `AGREEMENT_ACCEPTED` (private at 1010), `AGREEMENT_ACTIVATED` (public at 1011).
- **Notifications:** N3 to A at acceptance; N6 to both at activation.
- **Why authority is preserved:** both players consented to the exact version; activation is the system executing their decision, not making one.

### E4 — A withdraws before acceptance

- **Initial state:** A proposed `DP-T02` to B at 1100; B has not responded.
- **Initiating player:** A.
- **Available choices:** wait, withdraw.
- **Decision:** A withdraws at 1105.
- **Other participant:** B receives N5, no reason.
- **Validations:** A is the proposer; the proposal is `PENDING`; no acceptance recorded.
- **Result:** `WITHDRAWN`. No agreement, no cooldown, no cost. A's cap is released.
- **Costs:** none.
- **History:** `PROPOSAL_WITHDRAWN` (class S, private).
- **Notifications:** N5 to B.
- **Why authority is preserved:** A's own proposal remains A's to withdraw until B accepts; B is not bound by a proposal it did not answer.

### E5 — An amendment needs fresh consent

- **Initial state:** The NAP from E3 is `ACTIVE`, version 1, expiry 1371. At 1200 A wants to extend it by 360 turns.
- **Initiating player:** A.
- **Available choices:** propose `RENEW` (moves expiry, same version), propose `AMEND` (changes terms and creates a version), do nothing.
- **Decision:** A proposes `AMEND` version 2, term 720 turns from activation, expiry 1731. B accepts at 1204.
- **Other participant:** B.
- **Validations:** A is a party; the agreement is `ACTIVE`; no live `AMEND` for the pair; the proposed type is unchanged (`DP-T01`); the new expiry is later than the current one; both accept the exact version-2 terms.
- **Result:** at P4 on 1205 the agreement is version 2; version 1 is `SUPERSEDED`; expiry 1731. Between 1200 and 1205 the version-1 term (expiry 1371) is fully in force — if the parties did nothing, the NAP would still expire at 1371.
- **Costs:** none.
- **History:** `AGREEMENT_AMENDED` (public), version 1 retained with its activation and supersession turn.
- **Notifications:** N6 to both.
- **Why authority is preserved:** B was not bound by A's proposed version until B accepted; the old terms were never silently replaced.

### E6 — The pact reaches its agreed expiry

- **Initial state:** The amended NAP is `ACTIVE`, expiry 1731. No renewal was proposed.
- **Initiating player:** none. This is an automatic boundary event.
- **Available choices (before expiry):** renew; terminate; break; do nothing.
- **Decision:** both parties do nothing.
- **Validations:** P2 confirms the agreement is `ACTIVE`, the expiry turn is 1731, no accepted renewal exists, no freeze.
- **Result:** at P4 the agreement becomes `EXPIRED`; the war-declaration permission block ends; the record is public.
- **Costs:** none.
- **History:** `AGREEMENT_EXPIRED` (public).
- **Notifications:** N7 at 1707 (24 turns before); N8 at expiry.
- **Why authority is preserved:** the parties agreed to the term; expiry executes that agreement. The system did **not** renew, extend or reinterpret the silence as consent.

### E7 — A player terminates an aid agreement before delivery

- **Initial state:** Arcadia (payer) and Cyrene (recipient) have an `ACCEPTED` `DP-T03` for 5,000 crowns, accepted at 1300, delivery due at 1301. The 5,000 are reserved.
- **Initiating player:** the recipient, Cyrene, changes its mind; the payer agrees to a mutual termination at 1300 before the boundary.
- **Available choices:** let it deliver; terminate by mutual proposal; break (breach).
- **Decision:** Cyrene proposes `TERMINATE`; Arcadia accepts at 1300.
- **Other participant:** Arcadia.
- **Validations:** both are parties; the agreement is `ACCEPTED`; the termination acceptance is valid at P2; no delivery has occurred.
- **Result:** at P4 the agreement is `TERMINATED`; the 5,000 reservation is released to Arcadia; no transfer, no ledger movement, no breach.
- **Costs:** none.
- **History:** `AGREEMENT_TERMINATED` (public fact, private reason).
- **Notifications:** N8 to both.
- **Why authority is preserved:** both players chose to stop; neither was forced to deliver or to accept a breach record. The recipient did not receive value it had not yet been given.

### E8 — A break, and its consequences

- **Initial state:** A NAP between Arcadia and Doria is `ACTIVE`, activated 1400, expiry 1760. At 1500 Arcadia decides the pact no longer serves it.
- **Initiating player:** Arcadia.
- **Available choices:** keep the pact; propose mutual termination (Doria may refuse); break.
- **Decision:** Arcadia confirms `BREAK`. The confirmation states: the record is public and permanent; the war block ends; a 36-turn same-type cooldown applies; no fine, freeze or automatic retaliation.
- **Other participant:** Doria is notified; it did not consent and cannot reject the break.
- **Validations:** Arcadia is a party; the agreement is `ACTIVE`; no terminal event exists; the idempotency key is new.
- **Result:** at P4 the agreement is `BREACHED`; the effect ends; the public event names Arcadia as breaker; Arcadia's breach count rises by 1; Arcadia cannot propose `DP-T01` to Doria until 1536. No value moves.
- **Costs:** none. The cost is the record, the lost pact and the cooldown.
- **History:** `AGREEMENT_BREACHED` (public, class P).
- **Notifications:** N8 to both.
- **Why authority is preserved:** Arcadia chose to break its own promise; Doria was not asked to consent to being released, and the system did not punish Arcadia beyond the published consequence.

### E9 — A diplomatic action rejected for lack of permission

- **Initial state:** An alliance leader (Prompt 09's future role) tries to accept a `DP-T01` addressed to a member nation. B-08 has no delegation.
- **Initiating player:** the alliance leader, not the member's owner.
- **Available choices:** none for the leader in B-08; the member's owner may accept.
- **Decision:** the leader submits acceptance.
- **Other participant:** the member and the proposer are not notified of a valid acceptance.
- **Validations:** session ownership ≠ the addressed nation; no approved delegation scope exists.
- **Result:** `DPF-03 UNAUTHORIZED`; nothing changes; the proposal stays `PENDING`.
- **Costs:** none.
- **History:** failure line to the actor only.
- **Notifications:** none.
- **Why authority is preserved:** the member's player, not its alliance, owns the decision. Prompt 09 may later propose a delegation model, but it cannot be assumed here.

### E10 — An action blocked because eligibility is not met

- **Initial state:** Arcadia wants to embargo Etruria at 1600. Arcadia's posture toward Etruria is `TENSE`; there is no consultation pact.
- **Initiating player:** Arcadia.
- **Available choices:** change posture to `HOSTILE` (if the 12-turn cooldown is clear), wait, abandon the embargo.
- **Decision:** Arcadia first tries `DECLARE_EMBARGO`.
- **Validations:** the embargo requires `HOSTILE` posture (DIP-093); Arcadia is `TENSE`.
- **Result:** `DPF-15 POSTURE_REQUIRED`; no embargo; no event; no cooldown consumed.
- **Follow-up:** Arcadia sets `HOSTILE` (allowed if the cooldown is clear), then declares the embargo at the next boundary. If a `DP-T02` had been active, the posture change would first require a valid consultation notice (`DPF-09`).
- **Costs:** none.
- **History:** failure line only; the posture change, once made, is a public `POSTURE_SET`.
- **Notifications:** the posture change notifies Etruria; the failed embargo notifies no one.
- **Why authority is preserved:** the game did not decide to embargo or to escalate; it enforced the eligibility rule and told the player the path.

### E11 — Simultaneous termination and break

- **Initial state:** A NAP between Arcadia and Faunia is `ACTIVE`. At the same boundary, Arcadia submits `BREAK` and Faunia's `TERMINATE` acceptance (proposed earlier) is also pending.
- **Initiating players:** Arcadia (break), Faunia (termination acceptance).
- **Available choices:** both are already submitted.
- **Decision:** both resolve at the boundary.
- **Validations:** P2 validates both; DIP-103 orders `EXPIRY_AND_TERMINATION` before `BREACH`; the termination wins.
- **Result:** the agreement is `TERMINATED`; no breach event; no breach count; no 36-turn cooldown. Arcadia's break fails with `DPF-01` because the agreement is no longer active. One outcome, one public record.
- **Costs:** none.
- **History:** `AGREEMENT_TERMINATED` only.
- **Notifications:** N8 once, not twice.
- **Why authority is preserved:** both players' decisions were considered; the published order resolved the conflict without the system choosing a winner by preference.

### E12 — A treaty that depends on a Prompt 09 rule

- **Initial state:** Two nations in the same alliance sign a `DP-T01`. Later, one leaves the alliance.
- **Initiating players:** the two nation owners (for the NAP); the leaver (for membership).
- **Available choices:** keep the NAP; terminate it; break it; leave the alliance.
- **Decision:** the nation leaves the alliance; neither party touches the NAP.
- **Validations:** B-08 checks only the two nations and the pair; alliance membership is not a B-08 field; Prompt 09 emits the membership event.
- **Result:** the NAP **persists**; the alliance is not a party and receives no treaty obligation; the leaving nation's diplomatic record is unchanged. If the leaver later rerolls, DIP-127 terminates the NAP and Prompt 09 ends membership separately.
- **Costs:** none in B-08. Any alliance-side consequence (role loss, pool access) is Prompt 09's and is not specified here.
- **History:** `AGREEMENT_ACTIVATED` remains; the membership event is 09's record.
- **Notifications:** the NAP parties receive no treaty notification for a membership change; 09 notifies the alliance.
- **Why authority is preserved:** the nation's treaty is its own; the alliance cannot sign, veto or inherit it. `UD-039` is resolved by `D-137`: no delegation is allowed and no B-08 alliance object exists, so the design preserves that refusal; `D-140` adds only a separate B-09 `AT-` object outside B-08.

---

## 21. Prompt 08C handoff

**Status note (Prompt 09B-F, 2026-11-01).** This handoff was fulfilled by [Prompt 08C v1.3](15_diplomacy_workflows_acceptance.md). The brief below is retained as the historical design handoff; it is not a current authorization or an open task. No rule in B-08 was changed by recording this status.

### 21.1 What 08C must produce

Prompt 08C owns **workflows, edge cases, safeguards, failure paths, worked examples and the acceptance matrix**. B-08 supplies the rules; 08C must make every rule traceable to a test and every workflow traceable to a rule. It must not add a mechanic B-08 does not contain; if it finds a gap, it records the gap and the owner rather than inventing a rule.

| Area | 08C must specify | Rules to trace |
|---|---|---|
| Proposal journey | Create → submit → notify → view → accept/reject/withdraw/expire, with every screen state and deadline | DIP-042…DIP-051; §13 |
| Acceptance and rejection | Validation at submission and P2; failure paths; reciprocal proposals; stale terms | DIP-048…DIP-050; DIP-125 |
| Withdrawal | Before acceptance only; private; cap release; no undo | DIP-047 |
| Amendment | Version display; old vs new terms; consent; activation; rejection; invalid type change | DIP-063…DIP-066 |
| Renewal | Window; prospective expiry; late renewal void; no auto-renew | DIP-067, DIP-068, DIP-058 |
| Expiration | Proposal and agreement expiry; warnings; no silence acceptance | DIP-046, DIP-021, N2/N7 |
| Termination | Mutual only; reservation release; no breach; private reason | DIP-069…DIP-071 |
| Breach | Break confirmation; public record; count; cooldown; no automatic penalty; simultaneous break | DIP-072…DIP-077; DIP-130 |
| Reputation | Breach count display; window; reroll; no score | DIP-084…DIP-090 |
| Embargo | Eligibility; declaration; blocked routes; grandfathering; lift/expiry; market row | DIP-091…DIP-099; §17.3 |
| Permissions | Owner-only; no delegation; administrator limits; read access | DIP-013…DIP-019; DIP-078…DIP-080 |
| Authorization failures | Every `DPF` code, its sentence and the next eligible turn | §15.1; DIP-083 |
| Simultaneous actions | The full race matrix, including break vs delivery, terminate vs break, reciprocal accepts | DIP-130, DIP-131 |
| Restricted/inactive participants | Pair restriction; dormancy; transition/crisis; reroll; retirement | DIP-074, DIP-105, DIP-127…DIP-129 |
| Notifications | Nine events; recipients; duplicates; deadline warnings; no suppression of consequences | DIP-114…DIP-116 |
| Visibility | Every field in the matrix; public vs private; publication moment; A14 | DIP-108…DIP-113 |
| History | Class P vs S; provenance; corrections; retired page | DIP-117…DIP-121 |
| Cross-system | B-02 phases; B-03 pair/reroll; B-04 aid; B-06 freeze; B-07 embargo hook; 10 NAP hook; 09 boundary | §17, §18 |
| Player authority | The eight-question test for every action; the "no automatic decision" list; confirmation content | §3; DIP-081, DIP-082 |
| Prompt 09 scenarios | The ten cross-system scenarios as acceptance cases after both designs exist | §18.4 |

### 21.2 The acceptance matrix 08C must build

The matrix must have one row per **rule**, not one per screen. A rule with no test is an unmapped rule and fails the matrix. The minimum columns are: rule ID; workflow; actor; precondition; action; expected state; expected record; expected notification; failure code; visibility; cross-system dependency; test ID.

**DIP-150 — The matrix must cover, at minimum:** every `DIP-` rule; every `DPF` code; every state transition in §5; every limit in §12; every field in §13.2; every event in §14; every invariant in DIP-134; every race in DIP-130; every example in §20; every cross-system row in §17.2; and the ten 09 scenarios.

**DIP-151 — Tests are specified, not executed.** 08C writes test specifications and may add document-level checks; it must not claim a runtime, load, security or integration test. There is no implementation to test. The acceptance matrix is a design artefact.

### 21.3 What 08C must not do

- Add a treaty type, sanction, reputation score or delegation rule.
- Change a value in §6/§10/§12 without a `D-` entry (Prompt 14 owns tuning).
- Change a `MKT-`, `ECN-`, `URB-`, `DMP-` or `TR-` rule.
- Mark Global Trade released or a gate passed.
- Design Prompt 09's alliance system or Prompt 10's war.
- Treat a B-08 example as a balance proof.
- Claim Prompt 08 complete before 08C's own deliverables and checks exist.

### 21.4 Handoff questions 08C must answer

1. What is the exact screen sequence for a proposal, and where does the counterparty see the deadline?
2. How is a version displayed when an amendment is pending, and how does the player compare versions?
3. What does the breach confirmation say, word for word, and what is the cancel path?
4. How is the breach count shown so it is a fact, not a score?
5. How is an embargo's blocked route explained to a trader who hits it?
6. What does the recipient see when an aid is terminated or voided?
7. How are N2/N7 warnings delivered when a player has notifications grouped?
8. What happens on a stale tab that submits an acceptance after expiry?
9. How does the interface show a frozen deadline during `TRANSITION`?
10. How does a player see that an alliance cannot sign for it?
11. What is the empty state for a nation with no diplomacy?
12. How is a retired nation's treaty history reached from the replacement's page without implying inheritance?

---

## 22. Acceptance checklist and validation evidence

**Corrected 2026-10-30 (Prompt 08B-C).** Seven confirmed defects were repaired without changing a value, a treaty type, a permission or a player-authority rule: the Prompt 09 filename, the same-turn order, the proposal/agreement key shapes, the freeze omissions, the rolling-window example, the posture matrix and the DIP-061 cross-reference. §22.2 and §22.3 record the checks that were re-run afterwards.

### 22.1 The 08B acceptance checklist

Every criterion in the Prompt 08B acceptance list, with the artefact that satisfies it. "Satisfied" means the criterion is met **at the design and documentation level**; it never means implemented, runtime-tested or release-approved.

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | The complete 08A handoff was used | **Satisfied** | The evidence base is cited in the header; the six `DPX-` conflicts are disposed in §19.1; `DQ-` and `DCR-` items are answered or deferred in §19.2 |
| 2 | The specification is complete at foundations/design level | **Satisfied** | §1–§22; 22 sections; **157 `DIP-` IDs** (`DIP-001`…`DIP-157`) plus `DIP-039a`; 12 formulas |
| 3 | Player sovereignty is explicit and applied consistently | **Satisfied** | DIP-001, DIP-013…DIP-019; §3; every §5 transition names the choosing actor; §20 E1–E12 |
| 4 | No discretionary diplomatic action is autonomous | **Satisfied** | DIP-019's prohibition list and DIP-020's closed automatic list (activation, expiry, cleanup); §3.3; no rule accepts, rejects, breaks, renews or sanctions for a player |
| 5 | Bilateral agreements require participant consent | **Satisfied** | DIP-003, DIP-045, DIP-047, DIP-049, DIP-063; §8.1; silence never consents |
| 6 | Every relationship and treaty state has a defined transition | **Satisfied** | §4 posture table; §5.1–§5.3 matrices; forbidden transitions listed with `DPF` codes |
| 7 | Permissions and authorization are explicit | **Satisfied** | §9 action matrix (14 actions, A1–A14) and its visibility table; DIP-078…DIP-083; no delegation (DIP-015) |
| 8 | Reputation and UD-033 have an accurate disposition | **Satisfied** | D-128; §10; UD-033 resolved as "no score"; the reroll limitation is disclosed (DIP-087) |
| 9 | Sanctions are within approved scope | **Satisfied** | One act only, `DP-A01` (§11); no collective, asset-freezing or technology sanction; D-129 |
| 10 | Timing, expiration, visibility and history are specified | **Satisfied** | §12 limits and boundaries; §13 visibility matrix; §14 nine events and class P/S |
| 11 | Failure and integrity cases are addressed | **Satisfied** | §15: 15 `DPF` codes, nine invariants (DIP-134), twelve race rows (DIP-130) |
| 12 | Stage 2 Prompts 01–07C remain integrated | **Satisfied** | §17.2 26-row matrix; no `TR-`, `ECN-`, `URB-`, `DMP-`, `MKT-` or `F-TM-` rule edited |
| 13 | Prompt 09 Alliance System ownership is preserved | **Satisfied** | §18; DIP-146…DIP-149; nothing in §18 defines founding, governance, ranks, membership or pool |
| 14 | Cross-system contracts and dependencies are documented | **Satisfied** | §17.2–§17.4; §19.2 owners; `D-137` resolved the interface (no B-08 alliance object, zero delegation), amended in part by `D-140`'s separate B-09 `AT-` object |
| 15 | Formula and decision registers are accurate | **Satisfied** | 12 `F-DP-` entries with units, bounds, rounding, timing, edge cases, example and validation; D-123…D-132; DD-137…DD-146; REQ-514…REQ-533 |
| 16 | Worked examples demonstrate player authority | **Satisfied** | §20 E1–E12, each stating who chose, what the system validated, and what silence did |
| 17 | Prompt 08C has a clear handoff | **Satisfied** | §21.1–§21.4; DIP-150/DIP-151 |
| 18 | Canonical filenames and references are consistent | **Satisfied** | D-132; `15_diplomacy.md` and `15_diplomacy_formula_register.md`; `14_` untouched; Prompt 09 → `16_alliances.md` |
| 19 | All applicable continuity files are updated | **Satisfied** | §22.3 records each file and its purpose |
| 20 | All applicable validators have been run and reported | **Satisfied** | §22.3: exact commands and actual outcomes |
| 21 | No implementation has been performed | **Satisfied** | No code, schema, migration, API, screen, job or deployment was created; the only non-Markdown edits are document-QA scripts |

**Criterion 20's limit.** A validator passing proves the documents agree; it does not prove the diplomacy design is balanced, usable or complete. See DIP-151.

### 22.2 Internal consistency checks actually run

These were executed against the saved files, not asserted from memory. All results are as reported.

| Check | Method | Result |
|---|---|---|
| Rule identifiers | Regex over every `**DIP-nnn —` rule paragraph, and a second pass over every `DIP-nnn` mention | **151 rule paragraphs, `DIP-001`…`DIP-151`, no gap**, plus one sub-lettered rule `DIP-039a`; `DIP-152`…`DIP-157` are the six register-discipline rules stated in §16.1 and in full in the register, so the ID range `DIP-001`…`DIP-157` is contiguous |
| Duplicate rule IDs | `sort | uniq -c` on the definition prefix | One apparent duplicate was `DIP-039` / `DIP-039a`, i.e. the sub-lettered pair, not a re-use |
| Failure codes | Regex `DPF-\d\d` | `DPF-01`…`DPF-15`, all 15 referenced by §15.1 and by at least one rule |
| Formulas | Regex `F-DP-\d{3}` in both files | B-08 cites `F-DP-001`…`F-DP-012`; the register defines the same twelve, none extra |
| Sections | Heading scan | §1–§22 continuous, no gap |
| Worked examples | Heading scan | E1–E12, twelve, matching §20's claim |
| Cross-system matrix | Row count of §17.2 | 26 rows against B-02…B-07, 07C and Prompts 09–14 |
| Posture transitions | Every ordered pair of the four postures in the §4.2 table | **12 of 12** present (`T1`–`T12`), plus three guard rows; every transition to `HOSTILE` carries the notice precondition |
| Same-turn order | One band named in DIP-101 and DIP-103, cross-checked against DIP-130/DIP-131 | Five steps in one order: expiry/termination → breach → activation → scheduled delivery → embargo; no text says activation precedes breach |
| Key shapes | DIP-124, DIP-134 and F-DP-002 | Proposals **ordered** by `from → to`; agreements **unordered** by pair; embargoes ordered by imposer → target |
| Freeze scopes | DIP-105 against F-DP-004, 005, 006, 007, 008 and 009 | Pair-scoped timers use `frozen_pair` (a shared frozen boundary counts once); actor-scoped timers use `frozen_turns(actor, start, t)` over an explicit interval, so each cooldown counts unfrozen boundaries; the embargo term is explicitly not extended |
| Rolling window | F-DP-010 example recomputation | At turn 4480 the bound is 100: a breach at 100 is excluded, at 200 included, at 5000 excluded |
| Prompt 09 filename | Read of the Stage 2 register, outline and D-132 | Row 09 names `16_alliances.md`; no register cell names `15_alliances.md` |
| Register tallies | Count of `D-`, `DD-`, `REQ-`, `UD-` rows in the authoritative registers | D-123…D-132 (10), DD-137…DD-146 (10), REQ-514…REQ-533 (20), UD-039 (1 new; UD-013/UD-033 resolved) |
| Identifier collisions | Search for `DIP-`, `F-DP-`, `DP-T`, `DP-A`, `DPF-` outside B-08 | No earlier document uses any of the five families |
| Frozen rules | Re-ran the market, economy, city and politics checkers with their assertions unchanged | No `MKT-`, `F-TM-`, `ECN-`, `URB-` or `DMP-` assertion was edited or broken; every checker reports its earlier counts (237 rules and 237 matrix rows, 95/95, 164/164, 267/267, 879/879) |
| Global Trade status | Read of D-122, DD-136, REQ-513 and G-1…G-6 | Unchanged: mandatory scope, **not** released; G-4 partial, the other five not met |

**What these checks do not show.** They are structural and textual. No rule has been executed, no state machine has been exercised, and no player has used the interface. The consistency of a document is not evidence that its design is fun, balanced or correct.

### 22.3 Document validators and their actual results

Run from `docs/qa_backups/` on 2026-10-30, after the continuity updates in §20 of this prompt. Every line is the command's own output, not an expectation.

| Command | Actual result |
|---|---|
| `python3 validate_final.py` | **VALIDATION: ALL CHECKS PASSED** (exit 0) |
| `python3 validate_final.py --self-test` | **7/7 guards detect their defect** (exit 0) |
| `python3 test_next_action.py` | **23 tests, OK** (exit 0) |
| `python3 test_decision_registers.py` | **12 tests, OK** (exit 0) |
| `python3 09_validate.py` | **347/347 — ALL CHECKS PASSED** (exit 0) |
| `python3 verify_politics_numbers.py` | **879/879** (exit 0) |
| `python3 verify_politics_numbers.py --self-test` | **18/18 guards; 879/879 document checks** (exit 0) |
| `python3 verify_market_workflows.py` | **14 checks, 0 failed; 237 `MKT-` rules / 237 matrix rows / 83 tests — ALL CHECKS PASSED** (exit 0) |
| `python3 verify_market_workflows.py --self-test` | **8/8 guards detected their defect** (exit 0) |
| `python3 verify_market_numbers.py` | **95 passed, 0 failed — ALL CHECKS PASSED** (exit 0) |
| `python3 verify_economy_numbers.py` | **164/164** (exit 0) |
| `python3 verify_city_numbers.py` | **267/267** (exit 0) |
| `python3 verify_diplomacy_numbers.py` | **8 groups checked, 0 failed** (exit 0) |
| `python3 verify_diplomacy_numbers.py --self-test` | **7/7 guards detected their defect** (exit 0) |

**What the validators were changed to expect, and why that is not a weakened check.** Several assertions encoded the pre-08B state — the register totals (REQ-001…REQ-513, DD-001…DD-136, D-001…D-122, 19/487/5/2), the unresolved register (UD-001…UD-038, UD-013/UD-033 deferred, 22/8/8), the progress-log row (`08A complete`, `08B next`) and the handoff count ("one hundred and twenty-two"). Each was advanced to the value the files now carry: **REQ-001…REQ-533**, **DD-001…DD-146**, **D-001…D-132**, **19/507/5/2**, **UD-001…UD-039**, UD-013/UD-033 resolved, **24/7/8**, `08A`/`08B` complete with `08C` next, **132**. Two guards were added — `08B` in the completed sub-prompt set (with a self-test fixture) and `15_diplomacy.md` in the outline's gameplay-rule derivation — because the documents grew a section and a rulebook. **No check was deleted, no threshold was loosened to make a failure disappear, and every earlier assertion about market, economy, city and politics content still passes unchanged.**

**The 08B-C checker.** `verify_diplomacy_numbers.py` exists because the general validators could not see the seven defects: they check registers, status and continuity, not diplomacy semantics. It asserts the section and identifier structure, the `16_alliances.md` filename, the five-step order, the ordered-proposal/unordered-agreement keys, the freeze scopes, the rolling-window boundary, all twelve posture transitions, the DIP-061 reference and the player-authority rules — and its `--self-test` mutates a copy of each in memory to prove it fails on the defect it was written for.

**What was not run.** There is no server, database, browser, scheduler or game runtime to exercise: no implementation of B-08 exists (D-012). Accessibility of the 08A sources was established on 2026-10-29, not re-tested here. No load, concurrency, security or usability test exists, and none is implied by a green validator.
