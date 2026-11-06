# Core gameplay loop, symbolic world and turn system

**Version:** 1.6 · **Created:** 2026-10-23 · **Stage 2, Prompt 02** · **Revised:** 2026-11-04 (v1.1 D-015 Operations Points model; D-019 P3 order · v1.2 reference block and boundary wording reconciled with the supersession of D-004 · v1.3 UD-030 marked resolved wherever this document still listed it as open · v1.4 decision-closure audit — D-025…D-029 applied to TR-022, TR-080, TR-092 and TR-096 · v1.5 UD-029 resolved by D-030 in TR-020/TR-096 · v1.6 Prompt 10B-C3 adopts one OP regenerated at each boundary inside P3.7, replacing the full refill-to-cap wording as amended in D-015; the §24 Alliance contract no longer uses the ambiguous "war-room" scope and the B-10 contract records the amended OP model. No phase, rule ID or numeric value added)
**Status:** **Draft** — the authoritative document for Bible part **B-02**. It contains design rules, not implementation. No rule here is implemented, tested in production, or balanced by live play.
**Rule status vocabulary:** **Approved** (established by an owner constraint or a confirmed decision) · **Provisional** (a design that binds later prompts but is not owner-approved) · **Proposed** (a candidate a later prompt may adopt or discard) · **Deferred** (belongs to a later stage). A rule ID is stable; rules are superseded, never deleted.

**Companions:** [Bible outline](02_master_game_design_bible_outline.md) · [requirements](03_requirements_traceability.md) · [design decisions](04_approved_and_provisional_decisions.md) · [unresolved questions](05_unresolved_design_decisions.md) · [progress log](06_stage_2_progress_log.md)

---

## 1. Purpose and scope

This document defines the foundation every other Nation Supremacy system must build on:

1. what a player repeatedly does, from the first visit to the long-term arc;
2. what the *world* is, given that it has no map;
3. how one shared two-hour UTC turn is identified, closed, resolved and reported;
4. how player actions move through submission, validation, reservation and resolution;
5. how simultaneous players, competing orders and interruptions are handled without double spending or duplicate rewards;
6. what every later subsystem must declare so its rules fit this framework;
7. which of these rules are approved, which are provisional, and which are still open.

**In scope:** the player loop, the world model, the clock, the turn lifecycle, the resolution phase order, the action lifecycle, reservation and idempotency principles, recovery requirements, inactivity and fairness principles, reporting, the subsystem contract, worked examples, traceability.

**Out of scope (and not silently decided here):**

| Not decided here | Owner prompt |
|---|---|
| Prices, yields, upkeep rates, thresholds, any balance number | Prompt 04 / Prompt 14 |
| Nation creation flow, starting grants, progression milestones | Prompt 03 |
| Production, construction and research rules | Prompt 04, Prompt 05 |
| Trade mechanics beyond settlement timing | Prompt 07 |
| Treaty types, alliance governance, war rules and the action-resource model | Prompts 08–10 |
| Screen layouts, components, journeys | Prompt 13 |
| Schema, functions, scheduler code, API shape | Stage 5+ |
| Whether a second world/shard may ever exist | UD-026 (not decided) |

**How to read the rules.** Each numbered rule carries a status label and, where it exists, the requirement or decision it serves. A rule marked *Provisional* is binding on later Stage 2 prompts — they may change it only by editing this document and recording why (outline §3).

---

## 2. Source documents and design authority

| Source | What it contributes | Authority |
|---|---|---|
| [AI_CONTEXT](../AI_CONTEXT.md) §2 | Browser delivery, mapless world, 2-hour UTC cadence, free-first and architecture constraints, one account per person | Owner-stated constraints |
| [DECISIONS.md](../DECISIONS.md) | D-001…D-030 (D-004 superseded by D-015; D-005 superseded by D-008; D-008 provider direction; D-012 roadmap; D-014 decision policy; D-024–D-030 action economy, recovery, retention, aggregates, dormancy, e-mail and pending diplomacy) | The only approval record |
| [Report 06 §17](../stage-1/06_core_gameplay_systems_and_interactions.md) | Three-class timing contract; no attendance rewards; deterministic ordering requirement (SDQ-018); pending-state visibility; boundary re-validation | Stage 1 evidence, provisional |
| [Report 07 §14/§15](../stage-1/07_economy_design_and_market_structure.md) | Timing classification of economic actions, reservation display, provenance reporting | Stage 1 evidence, provisional |
| [Report 08 §5–§7, §13](../stage-1/08_security_privacy_fair_play_and_trust.md) | Server-authoritative values, idempotency, exactly-once resolution, audit spine, failure disclosure | Stage 1 evidence, provisional |
| [Report 09 §12](../stage-1/09_integrated_design_synthesis_and_readiness_audit.md) | REQ-001…REQ-039 inherited text | Stage 1 evidence |
| [Prompt 01 registers](03_requirements_traceability.md) | REQ-040…REQ-047, DD-001…DD-020, UD-001…UD-024 | Stage 2 working registers |

**Precedence on conflict:** confirmed decision → Stage 2 design register → this document → Stage 1 report → proposal. A later prompt that finds a conflict edits the owning document and records the change; it never leaves two competing rules.

**What this document does *not* inherit.** Stage 1's D1/Workers measurements are comparative evidence only (D-005 superseded). The Supabase figures (≈264–291 B/nation-turn, 35–59 ms per 1,000-nation slot) are single-boundary observations, not proof that twelve consecutive boundaries work (CF-03). Nothing in this document claims otherwise.

---

## 3. Established requirements and constraints

| ID | Constraint | Status |
|---|---|---|
| REQ-015 | The world resolves **12 turns/day at fixed UTC boundaries**, server-side; no live resolution windows | **Approved** (cadence) |
| REQ-045 | One authoritative scheduler (`pg_cron`); no second Cloudflare Cron job | **Approved** (D-008) |
| REQ-041 / DD-013 | Fictional, **mapless** world — symbolic network, never a geographic map | **Approved** (owner constraint) |
| REQ-043 / DD-016 | One account per person (policy); enforcement mechanism later | **Approved** (policy) |
| REQ-044 / DD-015 | Cloudflare Pages + Supabase direction respected in design | **Approved** (direction) |
| REQ-016 | Turn resolution is exactly-once and forward-only under retry or abort | Provisional (design) |
| REQ-017 | Boundary ordering is deterministic and published | **Open in Prompt 01 — resolved by this document** (§14; see §27) |
| REQ-018 | Duplicate submissions are safe | Provisional (design) |
| REQ-020 | Every resolved delta is explainable; failures explain and release | Provisional (design) |
| DP-002 / DD-017 | No attendance requirement, no streak reward, absence is respected | Provisional (design pillar) |
| D-004 → D-015 | Operations Points: **model approved** (military-only, non-transferable; **amended 2026-11-04**: one OP regenerated per boundary up to the cap, with carry below the cap); cap and costs **Provisional** | **Approved model / provisional values** |

**Hard boundaries this document must not cross:** no geographic positioning, no player-private turn schedule, no payment-dependent mechanic, no second scheduler, no unapproved promotion of an Operations Points *value*, and no claim that "exactly-once" has been implemented (only that it is required and was demonstrated once in a synthetic prototype).

---

## 4. The player core gameplay loop

**TR-001 — Core loop.** *Approved as a design requirement (REQ-001), design provisional.*

The repeated loop has six steps. A player may perform them in any order; the sequence below is the default path.

| Step | What the player does | What the game must provide |
|---|---|---|
| **1. Observe** | Opens the nation view; sees state, standing obligations, open decisions | Current state, distinct from forecasts and from other players' state |
| **2. Understand change** | Reads the digest of completed turns since the last visit | Per-turn deltas with provenance (what, how much, why) |
| **3. Decide** | Chooses between competing uses of limited means | Visible costs, prerequisites, consequences and opportunity costs |
| **4. Commit** | Submits orders and acts that require no boundary | Confirmation of acceptance, or a specific rejection reason |
| **5. Boundary** | Does nothing — or keeps planning, negotiating, or logging off | Resolution without presence; no action lost because a browser closed |
| **6. Revise** | Reads results, adjusts plans, schedules the next commitment | Digest within one turn of completion; no surprises without a cause chain |

The reviewed surface is deliberately plural: **treasury and resources, population and political condition, diplomatic status, alliance activity, active conflicts and objectives, and the queue of decisions that need an answer**. Each is owned by a later prompt; the loop requires only that the player can see its current state without hunting.

**TR-002 — Session shape.** *Provisional (REQ-001; Report 04's audience direction).* The design targets **1–3 sessions per day of roughly 5–15 minutes**, with no session mandatory. A session must be completable in that window in the steady state; longer sessions are allowed but never required by a mechanic.

**TR-003 — First session to steady state.** *Provisional.*
1. **First visit:** the player can found a nation and take one meaningful decision without leaving the game for help (REQ-038; Prompt 03 owns the flow).
2. **First turn:** the player submits at least one order, sees it accepted, and sees it resolved in the first digest.
3. **Steady state:** the player reviews the digest, adjusts one or two standing commitments, optionally interacts with another nation, and leaves. A player who only reads the digest loses nothing structural.

**TR-004 — Three time scales.** *Provisional (DD-010; Report 06 §17).* Every player-facing action is classified as exactly one of:

| Class | Meaning | Examples (subsystem-owned) | Player-visible state |
|---|---|---|---|
| **I — immediate with record** | Takes effect when accepted; recorded for history | Profile/posture edits, marking a digest read, withdrawing an unaccepted offer | Applied + recorded |
| **Q — queued until boundary** | Accepted now, resolved at the next boundary | Construction orders, policy changes, directed-trade acceptance, treaty signature consequences | Pending with a stated resolution turn |
| **S — boundary-scheduled** | A commitment that spans several boundaries | Multi-turn development targets, programme schedules, campaign arcs | Scheduled with progress and cancellation terms |

A subsystem may not invent a fourth class. If an action genuinely fits none, it is split into an immediate record plus a queued effect. Class membership is declared once per action type in the owning subsystem document.

**TR-005 — Action limits.** *Provisional.* This framework introduces **no global action-point currency, no universal action cap and no per-turn "click budget"**. Limits are **domain-declared** by each subsystem (for example a construction-slot limit), must be visible before submission, and must not reward being online at the boundary.

**Operations Points (military only).** Under [D-015](../DECISIONS.md), Operations Points are the **single military action resource** and nothing else:

1. one pool per nation, with a cap set by the war rules (Prompt 10);
2. regenerated by **one OP** at the opening of P3.7 at every successful boundary, capped at the national cap — points below the cap persist across turns, no point above the cap ever exists, and a dormant or absent player cannot mint power faster than the cap allows;
3. spent only on military orders; never on construction, research, trade, diplomacy or politics;
4. **not purchasable, tradeable, giftable or transferable**, so they cannot be funnelled between accounts;
5. reserved at acceptance and consumed at resolution under §19, like every other cost-bearing action;
6. visible to the owner; opponents see only what the war rules make public.

The accounting is explicit. At any read, `available = max(0, op_balance − op_reserved)`. Acceptance writes one `HELD` item and increases `op_reserved`; resolution writes one `CONSUMED` item, decreases `op_reserved` and debits `op_balance`; failure, cancellation or expiry writes one `RELEASED` item and leaves `op_balance` unchanged. The P3.7 regeneration writes exactly one `REGENERATED` item per nation per turn and applies `op_balance = min(op_cap, op_balance + 1)`, including a recorded `0` when the pool is already at the cap. A unique boundary key prevents a second regeneration for the same turn. The regenerated OP becomes spendable to the player only when the next OPEN window begins at P7 publication: the window for the current turn closed at P1, so P3.7 never makes an order affordable retroactively. Dormancy, protection and political-state rules are unchanged and continue to be evaluated at submission; regeneration never bypasses them.

The **model** is approved (D-015, amended 2026-11-04 as to the regeneration rate and carry below the cap); the cap, per-order costs and any readiness scaling are **Provisional** and belong to Prompt 10 and Prompt 14. Operations Points must never be described as the game-wide action currency.

---

## 5. Immediate, boundary and long-term activity

**TR-006 — How the scales interact.** *Provisional.*

1. Immediate actions never mutate boundary-resolved values directly; they write records, set intentions, or withdraw things that have not been committed.
2. Nothing that costs a resource is "immediate": cost-bearing actions are class Q or S, so their cost is settled at a boundary under the reservation rules (§19).
3. Long-term plans are expressed as class-S commitments with explicit review points; they are not hidden timers. Every commitment states its next observable effect.
4. A player may prepare the next turn's orders at any time, including immediately after a boundary. The queue is not emptied by logging out.
5. No system may require a player to act *during* resolution. Anything that would need a live response is redesigned.

**TR-007 — Waiting is a valid move.** *Provisional (DP-002).* Doing nothing for a turn has no penalty beyond the natural consequence of unchanged commitments. There is no decay applied merely for absence, no streak, and no bonus for acting every turn.

---

## 6. Player feedback loop

**TR-008 — Feedback contract.** *Provisional (REQ-020; DP-004).* For every action the player must be able to answer, without guessing:

| Question | Required answer |
|---|---|
| What will this cost? | The full cost, split into reserved-now and charged-at-resolution, in the same units the balance uses |
| Can I do it? | Eligible, or the specific unmet prerequisite |
| Did it go through? | One of the action states in §17, shown immediately |
| When does it take effect? | The turn number and its UTC time |
| Why did it fail? | A failure code from §17.4 plus a human sentence naming the cause |
| What changed? | The digest line for that action, with before/after values |
| What needs attention? | A bounded list of decisions whose window is closing, not an infinite feed |

**TR-009 — Server time is the only clock.** *Provisional (REQ-019).* The interface displays the server's authoritative time and the current turn's closing time. A client clock is never used to decide whether an action is in time. If the client's estimate differs, the client shows the server's value and the accepted turn, not its own countdown.

**TR-010 — No silent success, no silent failure.** *Provisional.* A submission that receives no response is *unknown*, and the interface must say so with a retry that is safe (§20). It may never be displayed as accepted, and an unknown action must not be assumed to have failed.

---

## 7. The symbolic world

**TR-011 — One shared world.** *Provisional (REQ-060; UD-026 open).* Nation Supremacy runs **one world** at a time. Every nation, alliance, relationship, campaign and ranking exists inside that world. There are no parallel worlds, shards, servers or player-private timelines in the initial design. A second world is a capacity question (UD-026, Stage 3), not an approved feature.

**TR-012 — The world is a relationship graph, not a map.** *Approved (constraint), model provisional (REQ-041, DD-013).* The world is represented as a **network of entities and relationships** with no coordinates, distances, borders, provinces or fronts. Nothing in the design may derive an outcome from physical proximity, and no future visualisation may imply real geography.

**TR-013 — World entities.** *Provisional.* The world model recognises these entity classes. The list is a design vocabulary, **not a schema** (Stage 5 owns tables).

| Entity | Meaning | Established? |
|---|---|---|
| **World** | The single shared instance: its epoch, current turn, configuration | Provisional (this document) |
| **Nation** | A player-governed political entity; the unit of ownership and state | Approved as a concept (REQ-002) |
| **Account** | The authenticated human identity that owns exactly one nation | Approved policy (REQ-043), model provisional |
| **Alliance** | A player-created collective with membership and permissions | Provisional (Report 06 SYS-010) |
| **Relationship** | A typed, directional or mutual state between two nations | Provisional (REQ-012) |
| **Agreement** | A treaty, trade or other recorded commitment between parties | Provisional (Prompts 07–08) |
| **Trade** | A transfer of resources between nations, atomic or rejected | Provisional (REQ-009) |
| **Campaign** | A bounded conflict object with objectives and a settlement stage | Deferred (REQ-014; Prompt 10) |
| **Objective** | A world-level goal that nations or alliances may pursue | Provisional (Prompt 11) |
| **World event** | A system-generated occurrence affecting the world | Provisional (Prompt 11) |
| **Ranking / record** | A published comparative measure or historical entry | Provisional (Prompt 11) |
| **Digest** | The per-nation, per-turn record of what changed and why | Provisional (this document, §23) |

**TR-014 — Edges carry the meaning.** *Provisional.* An entity is not interesting alone: relationships, memberships, agreements and conflicts are **edges** between nodes, and each edge declares its type, direction, visibility class and owning subsystem. A later visualisation renders the edge set; it does not invent a second model.

---

## 8. World membership and identity

**TR-015 — Membership is by nation, ownership is by account.** *Approved as policy (REQ-002/043), mechanics provisional.* One account owns exactly one nation. A nation belongs to the world from creation until it is retired under rules Prompt 03 defines. No account owns two nations, and no nation has two owners.

**TR-016 — Identity persists through absence.** *Provisional (REQ-022, DD-017).* A nation's identity — name, emblem, founding turn, history — remains in the world while it exists. Inactivity changes what the nation *does*, not whether it is real. What counts as abandonment, and what happens then, belongs to Prompt 03 (UD-025); this document requires only that no rule quietly deletes a nation because a player missed turns.

**TR-017 — No silent recreation.** *Provisional.* A retired or removed nation's name remains in the historical record with its status marked. Re-using the exact identity is a Prompt 03/12 decision, not an automatic behaviour. A player whose nation is gone must be able to see why.

**TR-018 — Alliances are optional.** *Provisional (DD-018; AP-004).* No mechanic may require alliance membership; alliance-scoped information and tools exist only for members and are never the sole route to a core action.

---

## 9. Relationships, direction and visibility

**TR-019 — Relationship types.** *Provisional (REQ-012, REQ-057).* The foundation recognises these relationship families. Detailed states, transitions and effects belong to the owning prompt.

| Family | Direction | Can change | Owning prompt | Boundary effect |
|---|---|---|---|---|
| Posture (friendly / neutral / tense / hostile) | Directional (A's posture toward B ≠ B's toward A) | Yes, recorded immediately | 08 | May gate actions; changes are class-I records with visible consequences |
| Agreement (treaty, pact, trade term) | Mutual | Signed, amended, exited | 08 | Consequences at boundary (class Q/S) |
| Alliance membership | Mutual, role-scoped | Join, leave, remove | 09 | Boundary effects for shared actions; role edits immediate-with-audit |
| Trade relationship | Mutual, per transaction | Per trade | 07 | Atomic settlement at boundary |
| Conflict / campaign | Mutual, adversarial | Declared, resolved | 10 | Campaign phases at boundaries |
| Competition (same objective or limited resource) | Implicit, not a stored state | Emergent | 11 | Evaluated at boundary |

**TR-020 — Relations transparent, intent opaque.** *Provisional (DP-004; D-030).* A nation's *standing relationships and public acts* are visible to those entitled to see them; its *plans, pending unannounced orders and private reasoning* are not. Declared acts (a treaty signature, a war declaration, a public posture statement) become visible when declared — that is their purpose.

**Pending diplomatic proposals.** A proposal that requires acceptance is visible to its **named counterparty** while it is open — acceptance requires seeing it. Third parties see nothing until both parties declare it, it takes effect at a boundary, or a party publishes it. A rejection or withdrawal is private to the two parties unless the withdrawing/rejecting party publishes it. The terms of a pending act never enter a published aggregate (D-027). Detailed exceptions belong to Prompt 08 (D-030).

**TR-021 — Visibility classes.** *Provisional (REQ-057).* Every piece of state is assigned exactly one class:

| Class | Who sees it | Examples |
|---|---|---|
| **Public** | Everyone | World chronicle events, rankings, declared postures, treaty texts once signed, war declarations |
| **Alliance** | Members of the alliance only | Membership list, roles, shared-pool balances, internal votes (if a native ballot is adopted under `UD-042`/`UD-049`) |
| **Private** | The owning nation/account only | Treasury detail, pending orders, reserves, unannounced plans, digest lines |
| **Restricted** | Authorised operators only (Prompt 12) | Audit and moderation records, abuse evidence |

**TR-022 — Aggregates must not leak.** *Provisional (D-027).* A published aggregate (ranking total, world statistic, market summary) may not allow a reader to recover a private component. The minimum contributing group is **k = 5**; a smaller group is merged into a stable "other" group only when the merged group is still ≥5, otherwise the value is withheld or coarsened into a band. **Complementary suppression** applies: if a total plus all but one component would reveal the last component, at least one further component is suppressed too. No differencing across turns or related tables may recover a suppressed component. An individual nation's public ranking is not an aggregate. k = 5 is a design constant (D-027), not a legal-compliance claim.

**TR-023 — Failure explanations respect the same classes.** *Provisional.* An error message may say *why your action failed* without disclosing another nation's private state. "Insufficient funds" never becomes "your opponent has 40 more".

---

## 10. The shared UTC clock and turn numbering

**TR-024 — Slot arithmetic.** *Provisional (REQ-015; D-008).* The world turn is identified by the two-hour UTC slot:

```
slot(t) = floor(unix_utc_seconds(t) / 7200)
turn N covers  [7200·N, 7200·(N + 1))   — half-open, UTC
```

*Examples (all UTC):* 08:00–09:59:59.999 is one turn; 10:00–11:59:59.999 is the next. The boundary instant belongs to the **later** turn.

**TR-025 — Turn identity vs display number.** *Provisional.* The **turn ID** is the absolute slot integer — stable, monotonic, and independent of when the world opened. The **display number** is relative: `display = slot − world_epoch_slot + 1`, so the first turn a world ever resolves is "Turn 1". Both appear in records; players see the display number with the UTC window.

**TR-026 — The world epoch.** *Provisional.* When a world opens, its epoch slot is fixed and recorded. It never changes. Changing the epoch would renumber history, so it is treated as immutable once the first turn completes.

**TR-027 — Current, next, previous.** *Provisional.*

| Term | Meaning |
|---|---|
| **Current turn** | The open turn a submission would join *if accepted now* |
| **Next turn** | The first turn that has not yet opened (the current turn's successor) |
| **Previous turn** | The most recently **completed** turn; its results are what the digest reports |
| **Resolving turn** | A turn whose submission window is closed and whose resolution has not yet been published |

A player can always tell which turn an action belongs to: the confirmation states the turn ID/display number and its UTC window, and the digest groups results by that same identifier.

---

## 11. Cutoff and boundary semantics

**TR-028 — Authoritative receipt.** *Provisional (REQ-019; Report 08 SEC-014).* An action belongs to the turn that was **open at the moment the server accepted the request**, using the server's authoritative timestamp — never the browser clock, never a value supplied by the client.

**TR-029 — Boundary assignment.** *Provisional (REQ-049).* Let `t` be the authoritative acceptance time.

| Situation | Rule | Assigned to |
|---|---|---|
| `t` comfortably before the boundary; turn N open | Accepted normally | Turn N |
| `t` exactly at the boundary instant (`t = 7200·(N+1)`) | The boundary instant belongs to the later turn | Turn N+1 |
| `t` after the boundary but before turn N+1's resolution | Turn N is no longer open | Turn N+1 |
| `t` during resolution of turn N (its window has closed) | Submissions never join a resolving turn | Turn N+1 |
| Request arrives after its target's own window closed (e.g. accepting an offer that expired at the boundary) | Cannot be retargeted silently | **Rejected** with reason |
| Duplicate of an already accepted action | Idempotent replay, no second action | Same turn as the original |

**TR-030 — No grace period.** *Provisional.* There is no hidden grace window at the boundary. A one-second-late request is next turn's action, and the interface says so. This is deliberately strict: a grace window would make the cutoff a guess and reward connection luck.

**TR-031 — Delayed or misconfigured clients.** *Provisional.* The client displays server time and warns inside the last minute of the window. If a request arrives late, the confirmation states the turn it actually joined. A wrong device clock cannot change the assignment. A player who believes an action was lost can inspect the action's state and turn; the record is authoritative.

**TR-032 — Submissions during resolution.** *Provisional (REQ-050).* While a turn is `RESOLVING`, the interface accepts orders **for the next open turn** and labels them so. It never queues an order into the turn already being resolved.

**TR-033 — A turn that overruns.** *Provisional.* If resolution has not completed when the next boundary arrives, the *published* result is still one outcome per turn: the later turn waits for the earlier turn to complete (serial resolution). Players see "turn N resolving; turn N+1 opens for orders". The framework never resolves two turns concurrently, because that would make ordering and cost settlement depend on machine speed.

**TR-034 — Implementation details deferred.** *Deferred.* Timestamp precision, request signing, retry transport, and how "accepted" is persisted are architecture concerns (Stage 5/8). The design requirements are: server receipt decides, half-open windows, no grace, no concurrent resolution.

---

## 12. Turn lifecycle

**TR-035 — States.** *Provisional (REQ-050, REQ-059).* Every turn is in exactly one state.

| State | Meaning | New actions accepted? | Accepted actions changeable? | Effects applied? | Player sees |
|---|---|---|---|---|---|
| **SCHEDULED** | Known future turn; nothing open | No | — | No | Countdown / next window |
| **OPEN** | Submission window; current turn | Yes | Yes (withdraw/amend) | No | "Orders open until hh:00Z" |
| **LOCKED** | Cutoff passed; accepted set frozen; resolution not started | No | No | No | "Closed; resolving shortly" |
| **RESOLVING** | Phases running; results not published | For the *next* turn only | No | In progress, unpublished | "Resolving turn N" |
| **COMPLETED** | Result published; digest available | For the next turn | No (already resolved) | Yes | Results, digest |
| **INTERRUPTED** | Resolution stopped mid-way; recoverable | For the next turn only | No | Partially, unpublished | "Recovering turn N" |
| **FAILED** | Resolution cannot produce a valid outcome for this attempt | For the next turn only | No | Nothing is published as final | "Turn N did not complete" + next step |

**TR-036 — Permitted transitions.** *Provisional.*

```
SCHEDULED → OPEN → LOCKED → RESOLVING → COMPLETED
                                   ↘ INTERRUPTED → RESOLVING (resume, same turn)
                                   ↘ FAILED → RESOLVING (retry, same turn)
COMPLETED is terminal for a turn; a completed turn never reopens.
```

No transition may skip `LOCKED`: resolution always begins from a frozen set. No transition may return a turn to `OPEN`.

**TR-037 — Freeze means freeze.** *Provisional (REQ-050, REQ-055).* At `LOCKED` the accepted action set, the world baseline and the configuration version are captured. Nothing submitted afterwards joins that turn. This is the single rule that makes deterministic resolution possible.

**TR-038 — One outcome per turn.** *Provisional (REQ-016, REQ-059).* A turn may be resolved more than once **internally** during recovery, but it has exactly one published outcome. A re-run must produce the same result for the same frozen input; a result that differs indicates a non-deterministic rule, which is a defect to fix, not a variant to publish.

**TR-039 — Players are told the state.** *Provisional.* The current turn state is always visible where actions are submitted, with the closing time. The interface disables submission for a resolving turn and enables it for the next one.

---

## 13. Turn resolution phases

**TR-040 — Fixed phase order.** *Provisional (REQ-051; UD-003 resolved).* Resolution always runs these phases in this order:

| Phase | Name | Purpose | Consumes | May change | Must remain invariant | Detailed rules owned by |
|---|---|---|---|---|---|---|
| **P0** | Prepare | Identify the turn, confirm it is due, refuse a duplicate run | Turn ID, world epoch, config version | Run record only | Turn identity | This document |
| **P1** | Freeze | Close the window; snapshot baseline and accepted set | Accepted actions, world state | Snapshot only | No mutation of world state | This document |
| **P2** | Re-validate | Re-check every accepted action against the frozen state; release reservations for failures | Snapshot | Reservations, failure records | No production, no rewards | This document + subsystems |
| **P3** | Recurring | Apply scheduled production/income, then mandatory obligations (upkeep, maintenance), then recurring political/event ticks | Snapshot + subsystem rules | Resource stocks, treasury, baseline condition, national OP balance (B-10 regeneration at P3.7) | Conservation identity; no discretionary orders | 04, 05, 06, 11 |
| **P4** | Orders | Resolve accepted player orders: construction, research, policy, trade settlement, diplomatic acts | Post-P3 state + frozen intents | Committed state and records | Reservation accounting; no double spend | 04–09 |
| **P5** | Conflict | Resolve campaigns and adversarial interactions | Post-P4 state | Conflict state, losses, settlement prerequisites | Bounded losses; off-ramp exists | 10 |
| **P6** | World | Evaluate objectives, rankings, systemic events | Post-P5 state | Rankings, events, objectives | No retroactive change to earlier phases | 11 |
| **P7** | Settle | Enforce invariants, write digest/events, mark COMPLETED, publish | All phase outputs | Records, turn status | One outcome; published only now | This document + 11 |

**TR-041 — Why this order.** *Provisional, except the income-before-upkeep point, which **D-019 confirms** (2026-10-23).* Income before obligations lets a nation pay this turn's upkeep from this turn's income; obligations before discretionary orders prevents orders from spending money already owed; conflict after economy means war costs are settled against a real balance; world evaluation last means rankings describe the turn that happened. Each of these is a design choice, not a law of nature.

**TR-042 — Ordering questions deliberately left open.** *Provisional, assigned.*

| Question | Why it is open | Owner |
|---|---|---|
| ~~Should production arrive before or after upkeep?~~ | **Decided (D-019, 2026-10-23):** production/income first, then mandatory upkeep; a shortfall invokes Prompt 04's deficit rule, and obligations never consume another action's reservation. UD-030 is resolved; the row stays as history | Prompt 04 defines the deficit rule only |
| Do trade settlements precede production that consumes the traded goods? | Decides whether a trade can rescue a turn's production | Prompt 07 (with 04) |
| Do campaign costs draw on pre- or post-P3 balances? | Affects readiness planning | Prompt 10 |
| Are world events generated before or after objective evaluation? | Changes whether an event can affect this turn's ranking | Prompt 11 |

Until the owning prompt decides, the phase *position* above stands; the *internal* order inside a phase is the subsystem's to specify and publish.

**TR-043 — Phase failure.** *Provisional.* A failure inside P0–P2 leaves no state change. A failure inside P3–P7 makes the turn `INTERRUPTED`; recovery resumes from the last completed phase checkpoint, not from P0. The turn is never left half-published.

---

## 14. Deterministic ordering and tiebreaks

**TR-044 — The ordering catalogue is published.** *Provisional (REQ-017/052; resolves UD-003).* The following is the **published ordering catalogue**. It is complete for the foundation; subsystems add their own entries inside these bands, and must declare them.

| Band | Contents | Ordering rule |
|---|---|---|
| **B0** | Mandatory system effects (upkeep, maintenance, expiry, scheduled obligations) | System-defined, deterministic; not player-ordered |
| **B1** | Accepted player orders with no contested target | Ascending `(submitted_at, action_id)` |
| **B2** | Contested allocations (a limited resource, slot or objective with more claimants than capacity) | **Order-independent**: proportional for divisible pools; seeded lottery for indivisible lots |
| **B3** | Adversarial interactions (campaigns, counters) | Subsystem-declared priority, then B1 key |
| **B4** | World evaluation (events, objectives, rankings) | Fixed evaluation order declared by Prompt 11 |

**TR-045 — The total order key.** *Provisional.* Within B1 and B3, actions are ordered by:
1. subsystem-declared priority class (if any, published);
2. `submitted_at` (server receipt, ascending);
3. `action_id` (server-assigned, monotonic) as the final tiebreak.

No rule may use a hidden identifier (database row order, hash order, client-supplied sequence) as an ordering key.

**TR-046 — Contested resources are order-independent.** *Provisional (REQ-052).* If an outcome would depend on *who was processed first*, the subsystem must convert it to an allocation:

- **Divisible** (funds, material quantities in a pool): pro-rata at a published ratio; every claimant gets a share, and the report states the ratio.
- **Indivisible** (one lot, one seat, one objective claim): a **seeded lottery**. The seed is derived deterministically from `(turn_id, allocation_id)` so it can be re-derived and audited; every entrant sees the same odds, and entrants are not advantaged by submitting earlier.
- **Time-critical by design** (a declared race the subsystem explicitly wants, such as first-to-declare): allowed only if the subsystem publishes the rule and explains why time priority is the intended mechanic. None exists at the foundation.

**TR-047 — Determinism requirements.** *Provisional (REQ-016).* During resolution, rules may read: the frozen snapshot, the turn ID, the configuration version, and subsystem state. They may not read wall-clock time, request arrival order beyond the frozen key, environment randomness, or live external data. Any pseudo-randomness uses the published seed derivation.

**TR-048 — The same inputs give the same result.** *Provisional.* A replay of a frozen turn must produce identical numbers and identical ordering. If it does not, the subsystem is non-deterministic and is corrected before it ships. This is what makes recovery, audit and player trust possible.

**TR-049 — Published means player-readable.** *Provisional.* The catalogue's *effect* must be explainable in the digest: which band applied, what the ordering key was where it mattered, and why a claim succeeded or failed. Publishing an internal rule nobody can read is not compliance.

---

## 15. Simultaneous-player semantics

**TR-050 — Simultaneity means "same frozen turn", not "same instant".** *Provisional.* Players act at different times during the window; all accepted actions are evaluated against the **frozen baseline** at `LOCKED`, then applied in the catalogue order. A player's acceptance does not immediately change what another pending action sees.

**TR-051 — Eligibility is checked at P2, not only at submission.** *Provisional (REQ-053; Report 06 §17).* An action accepted on Tuesday may be invalid at the boundary: funds spent elsewhere, a prerequisite revoked, a target retired. P2 re-validates against the frozen state and fails the action with a reason. Acceptance is not a guarantee of effect; it is a guarantee that the action entered the queue under the rules then in force.

**TR-052 — Dependent actions.** *Provisional.* A subsystem may declare that action X depends on action Y resolving first. It must declare the dependency as an ordering edge and specify what happens if Y fails (does X fail, or proceed with the old state?). The default is **fail with a reason**, not "proceed silently". No circular dependency is permitted; if two rules would form a cycle, the subsystem must break it by phase or band.

**TR-053 — Targeting a changing entity.** *Provisional.* If a target becomes inactive, leaves an alliance, or changes the state the action requires, the action fails at P2 with the specific cause. It does not retarget, and it does not consume the resource.

**TR-054 — Two actions on one relationship.** *Provisional.* Mutually exclusive relationship changes in the same turn (A offers, B exits) are resolved in B1 order; the later action is re-evaluated against the earlier outcome and fails if incompatible. The digest explains which act applied first. Prompt 08 may replace this with a dedicated consent model, and must say so here if it does.

---

## 16. Conflict handling

**TR-055 — Generic conflict classes.** *Provisional (REQ-052).* These are the foundation's answers. Subsystems extend them; they may not contradict them.

| Conflict | Generic rule | Still required from |
|---|---|---|
| Two accepted orders need the same uncommitted funds | Reservation makes this impossible at acceptance; if P3 changes the balance, P4 applies B1 order and the later order fails with `F1` | Prompt 04 (austerity interaction) |
| Two orders claim one indivisible lot | B2 seeded lottery; loser fails with `F4` | Prompt 07 (market) |
| An order's prerequisite is consumed by an earlier order | Later order fails at P4 with `F2`; no partial effect | Owning subsystem |
| Two relationship changes conflict | B1 order; later fails with `F7` | Prompt 08 |
| An action targets a nation that retired | Fails at P2 with `F3` | Prompt 03/10 |
| A trade's counterparty cannot deliver at settlement | Whole trade fails atomically (`F1`/`F3`); neither leg applies | Prompt 07 |
| Rewards for the same achievement | First in B4 order is granted; later claims are deduplicated by achievement key | Prompt 11 |
| Duplicate submission of one intent | Idempotent replay; one action | This document |

**TR-056 — Failure is cheaper than corruption.** *Provisional.* When two rules genuinely cannot be reconciled, the framework prefers a **clean failure with an explanation** over a partial or ambiguous outcome. Silent partial application is prohibited except where a subsystem explicitly defines a safe partial outcome (for example a campaign armistice), and then it must be labelled and reported as such.

---

## 17. Generic action lifecycle

**TR-057 — States.** *Provisional.* Every player action is in exactly one state.

| State | Meaning | Terminal? | Resources |
|---|---|---|---|
| **DRAFT** | Being configured in the client; not authoritative | No | None |
| **SUBMITTED** | Received; validation running | No | None |
| **ACCEPTED** | Valid; queued for its turn; reservation taken if it costs | No | Reserved |
| **REJECTED** | Refused at submission with a reason | Yes | None |
| **RESOLVED** | Applied at the boundary; effects and record exist | Yes | Charged |
| **FAILED** | Accepted but could not apply at resolution | Yes | Released |
| **CANCELLED** | Withdrawn by the player while still changeable | Yes | Released |
| **EXPIRED** | A time-bounded offer or claim lapsed | Yes | Released |

`PENDING` is a **display label** for `ACCEPTED`, not a separate state. A subsystem that defines a safe partial outcome (TR-056) reports it as `RESOLVED` with an explicit *partial* marker and the applied/not-applied split in the digest; it does not invent an extra state.

**TR-058 — Legal transitions.** *Provisional.*

```
DRAFT → SUBMITTED → ACCEPTED → RESOLVED
                  ↘ REJECTED     ↘ FAILED
ACCEPTED → CANCELLED
ACCEPTED → EXPIRED
```

No state returns to an earlier one. `RESOLVED` and `FAILED` are final for that action; a player who wants a different outcome submits a new action.

**TR-059 — Submission validation.** *Provisional (REQ-053).* At submission the server checks, at minimum: the actor owns the nation; the action type exists and is enabled; the turn is open; required parameters are within bounds; the player meets prerequisites; the cost is affordable **including existing reservations**; the target is visible and valid; no duplicate idempotency key conflicts. Failure produces `REJECTED` with a code.

**TR-060 — Resolution validation.** *Provisional.* At P2 the server re-checks the same conditions against the frozen state, plus dependencies and contested capacity. Failure produces `FAILED` with a code and a released reservation. The digest explains both the original acceptance and the later failure.

**TR-061 — Why accepted-then-failed is legitimate.** *Provisional.* Two actions can each be affordable alone but not together; a prerequisite can be revoked; a target can leave. Pretending acceptance guarantees effect would require either blocking all other actions or lying. The design therefore separates *entry* from *effect* and reports both.

**TR-062 — Failure codes.** *Provisional.* Codes are stable and player-visible:

| Code | Meaning |
|---|---|
| `F1` | Insufficient uncommitted resource at resolution |
| `F2` | Prerequisite no longer satisfied |
| `F3` | Target invalid, inactive or no longer visible |
| `F4` | Contested allocation lost |
| `F5` | Domain limit or capacity reached |
| `F6` | Offer or claim expired |
| `F7` | Invalidated by an earlier action's outcome |
| `F8` | Turn-level interruption; action retried with the turn |
| `F9` | Duplicate or conflicting idempotency key |
| `F10` | Rule disallows the action in the current world state |

`F8` is the only code that is not final: the action remains `ACCEPTED` and is retried when its turn resumes.

---

## 18. Modification, cancellation and expiry

**TR-063 — The window is the permission.** *Provisional (REQ-055).* An accepted action may be amended or cancelled **only while its turn is OPEN**. At `LOCKED` the set is frozen; after `RESOLVED` the action is history.

| When | Amend | Cancel | Effect on reservation |
|---|---|---|---|
| DRAFT | Yes | Yes | None |
| SUBMITTED | No (transient) | No | None |
| ACCEPTED, turn OPEN | Yes — new version, new idempotency key; supersedes the old version | Yes | Released on cancel; re-reserved on amend |
| ACCEPTED, turn LOCKED | No | No | Held; resolved or failed at P2 |
| RESOLVING | No | No | Held until P2 or P7 |
| RESOLVED / FAILED / CANCELLED / EXPIRED | No | No | Final |

**TR-064 — Amendment is replacement, not mutation.** *Provisional.* An amended action is a new version with the same logical identity; the previous version is recorded as superseded, and the amendment is submitted under a **new idempotency key**. Reusing the creation key with a different payload is `F9` (§20), not an amendment. History shows both versions, so "I changed my mind at 09:59" is auditable.

**TR-065 — No universal cancellation penalty.** *Provisional.* The framework imposes no fee for cancelling before the cutoff. A subsystem may charge one (for example a committed construction programme), and must state it at submission and in the digest. Free cancellation before the cutoff is the default because penalising a change of mind in an absence-tolerant game punishes exactly the behaviour the design supports.

**TR-066 — Offers expire.** *Provisional (REQ-009 context).* Time-bounded offers (trade, treaty, invitation) carry an explicit expiry turn. Expiry is automatic, costs nothing, and is reported to both sides. The expiry length is the owning subsystem's decision.

---

## 19. Costs, reservation and resource safety

**TR-067 — Reserve at acceptance, charge at resolution.** *Provisional (REQ-005/054; Report 07 ECON-001).*

1. **Submission:** the cost is checked against the **uncommitted** balance (total minus all reservations).
2. **Acceptance:** the cost is **reserved** — it remains in the account but is unavailable to any other order.
3. **Resolution:** at P3/P4 the reserved amount is **deducted** as the action applies.
4. **Failure/cancellation/expiry:** the reservation is **released** in the same step that records the outcome.

**TR-068 — Reservations are exclusive.** *Provisional.* The sum of reservations may never exceed the balance. This is the mechanism that makes "two orders spend the same money" impossible at acceptance rather than merely unlikely.

**TR-069 — The display is honest.** *Provisional (REQ-020).* Balances are shown as three distinct figures: **total**, **reserved**, **available**. A forecast is never displayed at the same weight as a current value. A player must not have to subtract reservations mentally to know what they can spend.

**TR-070 — Income does not retroactively authorise spending; obligations do not consume reservations.** *Provisional.* A reservation is judged against the balance at acceptance. Income arriving at P3 may fund obligations and orders, but an order that was unaffordable at submission is `REJECTED`, not queued in hope of income.

Mandatory obligations (upkeep, maintenance) draw only on **unreserved** funds. If P3 cannot cover them, the economy's declared deficit rule (Prompt 04) applies — another action's reservation is never silently spent. If a later phase still cannot honour a reservation, that action fails with `F1` and is released; the invariant is that the *cause* is explicit, not that failure is impossible.

**TR-071 — Caps and overflow.** *Provisional.* A reward that would exceed a storage cap is handled by the owning subsystem's declared rule (cap and lose, convert, or refuse). The foundation requires only that the rule is declared, applied deterministically, and reported; silent loss is prohibited.

**TR-072 — The client is never the balance.** *Provisional (REQ-019).* Numbers rendered in the browser are a view of server state. No design rule may depend on the client knowing the true balance before submission; the server's check is the decision.

---

## 20. State-consistency and idempotency guarantees

**TR-073 — The ten guarantees.** *Provisional (REQ-016/018/059; DD-011).* These are **design guarantees**; the mechanism column names the class of enforcement, not an implemented feature.

| # | Guarantee | Enforcement class (later stage) |
|---|---|---|
| G1 | No resource is spent twice for one action | Reservation + transactional settlement |
| G2 | No reward is granted twice for one resolution | Deterministic resolution + unique achievement keys |
| G3 | A failed action leaves no partial effect | Phase checkpoints + rollback of the action's own writes |
| G4 | A turn has exactly one published outcome | Single resolution record per turn |
| G5 | A completed turn never accepts ordinary submissions | State machine + server check |
| G6 | A duplicate submission does not create a second action | Idempotency key |
| G7 | Displayed balances equal the authoritative state at read time | Server-rendered values |
| G8 | An accepted action is not intentionally resolved twice | Frozen set + per-action application marker |
| G9 | Cross-system changes leave the world in a valid state | Invariant checks at P7 |
| G10 | The report matches the outcome | Digest generated from the same transaction as the state change |

**TR-074 — Idempotency key.** *Provisional (REQ-018).* Every mutating submission carries a client-generated key, scoped to `(account, action type, turn)`. The first request with a key creates the action; repeats return the original result. The same key with a **different payload** is rejected (`F9`) and creates nothing — it is treated as a client bug, not as an amendment (amendment uses the action's own identity, §18).

**TR-075 — Unknown is a state.** *Provisional.* A request whose response was lost may be retried safely with the same key. The client shows "unknown — retrying" rather than inventing success or failure. This is the only correct behaviour under an absence-tolerant design.

**TR-076 — Server-assigned identity.** *Provisional.* Action IDs, ordering keys and timestamps are assigned by the server. A client-supplied ID may be used only as the idempotency key, never as an ordering or identity authority.

---

## 21. Interrupted resolution and recovery

**TR-077 — One coherent outcome.** *Provisional (REQ-059; Report 08 SEC-019–021).* If resolution stops partway, the turn must still end with exactly one published outcome. Recovery may repeat internal work; it may not publish a second, different result, and it may not double-apply an effect.

**TR-078 — Forward-only resume.** *Provisional.* Recovery resumes from the last completed **phase checkpoint** for the same turn. Completed phases are not re-executed against changed input, because the input is frozen (P1). The turn remains the same turn; the display number does not change.

**TR-079 — Visibility waits for completion.** *Provisional.* No phase's effects are published before `COMPLETED`. A player therefore never sees a half-resolved world, and an interrupted turn that later completes is indistinguishable (to the player) from a slow one.

**TR-080 — Repeated interruption.** *Provisional (D-025).* If a turn cannot complete after a bounded retry budget, it is marked `FAILED` and the operator path is declared (Prompt 12 / Stage 8). Until it completes, the next turn waits (§11 TR-033) — the world does not skip a number, because a skipped turn would break the 12/day guarantee and the turn identity.

*Player-facing rule.* A `FAILED` turn shows as a **delay**, not a lost turn. Accepted actions stay pending and are never silently dropped, and no cost is charged unless the turn completes. If the turn later completes, the normal digest appears with its completion time. If the operator cannot recover it, the incident is disclosed and only an operator decision recorded in the incident log may **void** the turn: every reservation is released, no cost is charged, and the digest states that the turn did not resolve. A void is a disclosed outage, never a silent skip. A **disaster restore** that loses turns is the sole exception to the no-skip rule: unreconstructable slots are not replayed, the gap is disclosed, and the world resumes at the next boundary (D-025).

**TR-081 — Late start.** *Provisional.* If the scheduler fires late, the turn still uses its own frozen window: actions accepted before the boundary belong to it; actions after the boundary belong to the next turn. A late trigger changes *when* the result appears, not *which* actions it contains.

**TR-082 — Service unavailability.** *Provisional.* If the service is down across a boundary, the turn is resolved on recovery with the same window and input. Players see the delay and the eventual result; no action is dropped because the service was unavailable.

**TR-083 — Deferred technical requirements.** *Deferred.* Idempotent scheduler invocation, phase checkpoints, per-nation application markers, dead-letter handling, alerting and runbooks are Stage 5/8 obligations. Their design requirement is G4/G8 plus TR-077–TR-082. The synthetic Supabase prototype demonstrated exactly-once and full rollback **once**, at one boundary; that is evidence of feasibility, not proof of production behaviour (CF-03/CF-06).

---

## 22. Inactivity, absence and fair play

**TR-084 — The world does not wait for anyone.** *Provisional (REQ-022; DP-002).* Every turn resolves whether or not any player is present. Recurring effects, accepted orders and incoming actions proceed normally.

| Situation | Behaviour |
|---|---|
| Misses one turn | Nothing special; the digest reports what happened |
| Misses several turns | Digests accumulate; nothing decays merely for absence |
| Has accepted orders pending | They resolve at their boundary under §19 |
| Has recurring production/upkeep | Applied every turn (Prompt 04 defines the numbers) |
| In an alliance with active plans | Membership persists; alliance rules (Prompt 09) decide participation duties — none may require presence at the boundary |
| Is targeted by another player | The action resolves against the frozen state; protection rules are Prompt 10/12 |
| Returns after a long absence | A re-entry summary groups the missed turns and names the decisions that are still open (Prompt 03/13 own the presentation) |

**TR-085 — No attendance mechanic.** *Provisional (DP-002/AP-001).* There is no login streak, no presence bonus, no "act within X minutes" reward, and no penalty for not logging in. Any future proposal that rewards presence must change this rule explicitly, and the anti-pillar makes that unlikely.

**TR-086 — Fairness principles.** *Provisional (REQ-015/052).*

| # | Principle |
|---|---|
| F1 | All players share the same UTC boundaries; no local schedules |
| F2 | Acceptance is decided by the server, not the browser |
| F3 | No action requires the browser to stay open |
| F4 | The cutoff is published, exact and grace-free |
| F5 | Accepted and rejected actions are always reported |
| F6 | No undocumented processing order decides an outcome |
| F7 | Contested resources are allocated by published, order-independent rules |
| F8 | Duplicate submissions and recovery never duplicate effects |
| F9 | Disconnection changes nothing about an accepted action's fate |
| F10 | Rules and outcomes are visible enough to audit one's own turn |

**TR-087 — Enforcement is not claimed.** *Deferred.* Multi-account detection, botting policy, sanctions and appeals belong to Prompt 12 and later security work. The turn system only provides the properties they will need: server authority, idempotency, one outcome per turn, and an auditable record.

---

## 23. Turn reports and history

**TR-088 — Minimum report content.** *Provisional (REQ-020/056).* A completed turn's report contains, for the nation:

1. turn ID and display number; UTC window; completion time;
2. state deltas per resource, with before/after and the rule that caused them;
3. every action: identity, state (`RESOLVED`/`FAILED`), cost charged or released, effect, failure code and sentence;
4. recurring effects (production, upkeep, obligations);
5. diplomatic, alliance and conflict changes that involve the nation;
6. world events visible to it;
7. warnings and decisions whose window is closing;
8. ranking/objective movement, where published;
9. nothing about another nation's private state.

**TR-089 — Digest first.** *Provisional.* The per-turn digest is the primary record: **one bounded digest row per nation per turn**, containing the lines above. Routine actions do not each get their own history row. This is the volume decision required by UD-004 (§28) and the reason the design can claim a bounded write budget per nation-turn.

**TR-090 — History classes.** *Provisional (REQ-021/058).*

| Class | Content | Retention posture |
|---|---|---|
| **P — permanent record** | Treaties signed/exited, wars declared/settled, alliance founding/dissolution, leadership changes, sanctions, major world events, milestones | Append-only chronicle; corrections are new disclosed events |
| **S — summarised** | Routine turn results, action lines, market activity | Digest row per nation-turn; compacted after a bounded window |
| **O — operational** | Moderation and abuse evidence (Prompt 12) | Restricted class; 12-month floor unless an open case requires longer |
| **Audit spine** | Value mutations, pipeline phases, privileged acts (REQ-027) | **Permanent**, restricted and append-only; not deleted with class-O evidence |

Permanent does not mean "public": class-P entries still carry a visibility class (§9).

**TR-091 — Corrections are visible.** *Provisional (REQ-021).* A wrong record is corrected by appending a correction event that references the original. Editing history in place is prohibited, because it destroys the audit trail the fairness rules depend on.

**TR-092 — Retention limits.** *Provisional (D-026).* Class-S digests stay hot for **30 days**, then compact to **one monthly summary per nation** (totals and notable events, no per-action lines) kept for **12 months**, then deleted. Class-P records are **permanent**. Class-O moderation/abuse records keep a **12-month floor** unless an open case requires longer; Prompt 12 sets the operational value. The permanent audit spine required by REQ-027 is **not** subject to that floor. Compaction is an **idempotent daily maintenance job**, not a turn phase, never deletes class P, and is itself recorded. If Stage 3 measures the 1,000-nation footprint above **350 MB**, the hot window drops to **14 days** and summaries to **6 months** before launch. The stated sizes are a policy target, not a measured guarantee.

---

## 24. The subsystem contract

**TR-093 — What every later prompt must declare.** *Provisional (REQ-053).* A subsystem document is not complete until it states all fifteen items. The foundation supplies the defaults; a deviation must be argued.

| # | Declaration | Foundation default |
|---|---|---|
| 1 | State and entities | Graph entities (§7); no coordinates |
| 2 | Player actions | Each mapped to a timing class I/Q/S (§4) |
| 3 | Prerequisites | Checked at submission and again at P2 |
| 4 | Submission validation | §17.3 rules plus subsystem-specific bounds |
| 5 | Costs and reservation | Reserve at acceptance, charge at resolution (§19) |
| 6 | Boundary behaviour | Declares its phase (P3–P6) and internal order |
| 7 | Ordering | Declares its band and any priority class; contested resources use B2 |
| 8 | Effects on other systems | Registered as edges for B-15 |
| 9 | Failure and cancellation | Uses `F1`–`F10`; declares any partial outcome explicitly |
| 10 | Player-facing results | Digest lines with provenance (§23) |
| 11 | Visibility | One class per field; aggregates respect TR-022 |
| 12 | Invariants | Named, checkable at P7 |
| 13 | Edge cases and exploits | At least the ones its rules create |
| 14 | Requirements and decisions | REQ/DD/UD citations, with status |
| 15 | Validation examples | At least one worked boundary |

**TR-094 — Declared edges feed the Bible.** *Provisional (REQ-046).* Each subsystem registers its interactions for B-15 (cross-system matrix assembled in Prompt 15). An edge declared by only one side is incomplete; Prompt 15 checks both directions.

**TR-095 — Deviations are recorded, not hidden.** *Provisional.* A subsystem that needs a different reservation model, a fourth timing class, or a live resolution window must amend this document first, with the reason and the affected requirements. "Local exception" is not a permitted category.

---

## 25. Cross-system dependencies

**TR-096 — What each later prompt inherits.** *Provisional.*

| Prompt | Inherits from this document | Must decide / return |
|---|---|---|
| **03** Nation creation | World membership, identity persistence, inactivity continuity, the decided dormancy policy (D-028) and the verified-e-mail gate (D-029) | Starting state, creation flow, progression milestones, re-entry presentation hooks; it applies D-028 rather than re-deciding dormancy |
| **04** Economy | Reservation model, phase P3 placement, conservation invariants, failure codes | The deficit/austerity rule that follows D-019's income-before-upkeep order; austerity at P3; all numeric values |
| **05** Cities/production/research | Q/S classes, construction reservation, phase P4 ordering | Slot limits, prerequisites, production modifiers |
| **06** Politics | Recurring political effects at P3, policy changes at P4, stability invariants | Policy axes, stability effects, cooldowns |
| **07** Trade | Atomic settlement, offer expiry, contested B2 allocation, visibility classes | Settlement position vs production; offer reservation is settled by D-016 and visibility by D-017 — the prompt implements them (D-016 is **awaiting validation**, not proven) |
| **08** Diplomacy | Relationship types, consent semantics, visibility, ordering edges, and the pending-act visibility rule (D-030) | Treaty effects, breach consequences, public-declaration timing; implements D-030 rather than re-deciding it |
| **09** Alliances | Membership edge, role permissions, boundary effects, audit requirements | Governance, pool rules, succession, coordination-notice scope under `AX-18`/`UD-049`; no military command or war room |
| **10** Warfare | Campaign edge, P5 placement, bounded outcomes, no geography | Action-resource model is settled by D-015, amended 2026-11-04: one OP regenerated at each boundary inside P3.7 and carried below the cap; the prompt owns order costs, protection states and settlement rules |
| **11** World events | P6 placement, ranking aggregation, permanent-record class, the k = 5 aggregate rule (D-027) | Event generation, objective evaluation, ranking criteria |
| **12** Fair play | Policy hooks, restricted class, audit spine, failure disclosure, the recovery/retention policies (D-025/D-026) | Multi-account mechanics, appeals, the recovery disclosure and restore runbook; it implements D-025/D-026 rather than re-deciding them |
| **13** Interface | States, turn semantics, feedback contract, digest content | Screens, journeys, accessibility, notification taxonomy |
| **14** Formulas | Units, timing, ordering, labels | Every numeric value, rounding, caps, worked turn calculations |
| **15** Bible | This document as B-02 authority | Consistency review; B-15 matrix |

**TR-097 — Re-entry point for later conflicts.** *Provisional.* If a later subsystem cannot fit the framework, it amends §13/§14/§19 here and records the change in the progress log. Forking a private turn rule is the failure mode this document exists to prevent.

---

## 26. Worked examples

All numbers below are **illustrative test assumptions**, clearly fictional, and not balance decisions. Turn IDs use the real slot arithmetic; the display numbers are invented for readability. Assume the world epoch is display turn 1 at slot 248,900 (illustrative), so display = slot − 248,899.

### Example A — Ordinary turn

**Setup:** Turn 248,993 (display 94) opens at 10:00Z and closes at 12:00Z. At 10:20Z nation *Aurelia* submits "raise a granary" costing 40 units (illustrative), with 120 available.

1. Submission validates: owns the nation, turn open, affordable after reservations, prerequisites met.
2. Action becomes `ACCEPTED`; 40 becomes **reserved**; available shows 80.
3. The confirmation says "resolves at Turn 94 close (12:00Z)".
4. At 12:00Z the turn is `LOCKED`; the action is in the frozen set.
5. P2 re-validates: still affordable, prerequisite still valid.
6. P4 applies it: 40 is deducted; the granary becomes active.
7. P7 writes the digest line: "Granary raised — 40 units charged; production effect applies from Turn 95."
8. The player, offline since 11:00Z, sees the digest at 13:00Z. Nothing was required of them.

### Example B — Boundary submission

Same window: Turn 94 opens 10:00Z, closes 12:00Z; Turn 95 opens at 12:00Z.

| Server receipt (UTC) | Assigned to | Why |
|---|---|---|
| 11:59:30 | Turn 94 | Turn 94 is open; receipt is before the boundary |
| 11:59:59.900 | Turn 94 | Still before the boundary |
| **12:00:00.000** | **Turn 95** | The boundary instant belongs to the later turn |
| 12:00:00.400 | Turn 95 | Turn 94 is locked |
| 12:00:03 (during resolution) | Turn 95 | Submissions never join a resolving turn |
| 11:59:58 sent, arrives 12:00:02 | Turn 95 | Arrival is authoritative, not the send time |

The interface states the assigned turn on every confirmation, so a late order is visible as a next-turn action rather than silently lost.

### Example C — Insufficient resources

*Borealis* has 100 available, no reservations. At 10:10Z it submits order X costing 60 → `ACCEPTED`, 60 reserved, 40 available. At 10:15Z it submits order Y costing 60 → **`REJECTED` (`F1`)** because 60 > 40 available. No reservation is taken for Y.

If instead both orders were submitted and each cost 50, the same rule rejects the second; the framework never queues an order that cannot reserve its full cost. At resolution, X's 50 is deducted.

Suppose P3 applies an upkeep of 70 while 40 remains unreserved and 60 is reserved for X. Total commitments (130) now exceed the balance (100), so something must give, and it may not be a silent choice. The obligation may not spend X's reservation (TR-070). Prompt 04's deficit rule decides between the two coherent outcomes: obligations take priority and X fails with `F1` (its reservation released), or the unpaid part of the upkeep is deferred and X resolves. Either way the digest names both the shortfall and the order's fate. This prompt does not choose between them, because the choice is the economy's.

### Example D — Conflicting actions

Two nations claim the last seat on a world objective (one indivisible lot) in the same turn. B2 applies: a seeded lottery from `(turn_id, objective_id)` selects one; the other receives `FAILED` with `F4`, its reservation released, and a digest line naming the allocation rule. Neither is advantaged by submitting at 10:01 instead of 11:58.

If the contested item were divisible (for example a pooled material allocation of 100 units with claims of 60 and 60), B2 applies pro-rata: 50 each, stated in both digests.

### Example E — Disconnection

*Cyrene* submits a treaty acceptance at 11:40Z, receives the acceptance confirmation, and closes the laptop. At 12:00Z the turn resolves without any client connection: the treaty's consequences apply at P4, the digest is written at P7, and Cyrene sees it on return. The browser's absence is irrelevant because acceptance, reservation and resolution all happen server-side.

### Example F — Inactive player

*Delphi* stops logging in after Turn 94 but has a standing upkeep and a queued construction order.

| Turn | What happens |
|---|---|
| 95 | Upkeep applied; construction completes if its boundary arrived; digest written |
| 96–99 | Same pattern; nothing decays for absence; no streak lost (none exists) |
| 100 | Another nation's action targets Delphi; it resolves against the frozen state; Delphi's protection status is Prompt 10/12's rule |
| Return | Digest groups turns 95–100; open decisions are listed; no penalty is applied |

Dormancy and abandonment are **fixed by D-028**: dormant after 14 days/168 turns, no offensive targeting or initiation, no resource/progression loss, excluded from rankings as a presentation rule (not a penalty), reversible archival at 12 months. Prompt 03 applies the creation/re-entry presentation; Prompt 10 owns protection states and Prompt 12 deletion/notice. This document guarantees that absence does not stop the world and does not itself punish.

### Example G — Interrupted resolution

Turn 94 begins resolving at 12:00Z. P1–P3 complete; P4 fails after applying 300 of 1,000 nations' orders.

1. The turn becomes `INTERRUPTED`; nothing is published.
2. Recovery restarts at the P4 checkpoint with the same frozen snapshot.
3. Nations already applied are skipped by their application markers; the rest are processed.
4. P5–P7 run; the turn becomes `COMPLETED` once.
5. Players see one normal digest. The delay is visible as a later completion time, not as a second result.

If recovery cannot complete, the turn stays unpublished and the operator path (Prompt 12/Stage 8) decides. It is never published twice, and the next turn's number is not skipped.

### Example H — Duplicate request

A client sends "build granary" with key `k-7f3a` at 10:20Z, the response is lost, and the client retries at 10:20:04 with the same key and payload.

1. The retry matches the stored key; the server returns the original `ACCEPTED` response and the same action ID.
2. No second action exists, no second reservation is taken.
3. If the retry had a different cost or target with the same key, it is rejected `F9`; the client must amend the original action instead.

### Example I — Target changes state

*Elysium* submits a trade acceptance at 10:30Z. At 11:50Z the counterparty leaves the alliance whose members get a fee waiver, so the accepted terms no longer apply. At P2 the action fails with `F2`, the reservation is released, and the digest says "terms no longer valid — prerequisite lost". It does not silently charge the higher fee, and it does not retarget another seller.

### Example J — Turn report (illustrative)

> **Turn 94 · 10:00–12:00Z · completed 12:00:07Z**
> **Treasury:** 120 → 60 (−60). Reserved: 0. **Materials:** construction 30 → 42 (+12).
> **Resolved:** Raise granary (40 charged) — production +2 from Turn 95. Trade with *Borealis*: 12 construction received, 18 treasury paid.
> **Failed:** Accept offer #221 — `F6` expired at Turn 94 close; nothing charged.
> **Recurring:** Upkeep −2; granary maintenance not yet active. *(40 + 18 + 2 = 60 charged.)*
> **World:** Borealis and Cyrene signed a non-aggression pact (public).
> **Attention:** your construction queue is empty; one objective closes at Turn 96.
> *Values are illustrative and not balance decisions.*

---

## 27. Requirements traceability

### 27.1 Requirements this document covers

| REQ | How B-02 covers it | Status after this prompt |
|---|---|---|
| REQ-001 | §4 loop, §5 scales, §6 feedback | Provisional — coverage complete for the loop |
| REQ-015 | §10 slot arithmetic, §12 lifecycle | Approved (cadence); design now specified |
| REQ-016 | §20 guarantees, §21 recovery, §14 determinism | Provisional — design specified; **awaiting validation**; not implemented |
| REQ-017 | **§14 published ordering catalogue and tiebreaks** | **Open → Provisional** (UD-003 resolved) |
| REQ-018 | §20 idempotency key and replay | Provisional — design specified; **awaiting validation** |
| REQ-020 | §6 feedback, §19 display, §23 report | Provisional — design specified |
| REQ-035 | §10/§13 preserve the free-scheduler shape; no live resolution | **Open** — capacity unmeasured (UD-028 / CF-03: empirical load test still required) |
| REQ-041 | §7 mapless graph | Approved constraint, model specified |
| REQ-045 | One scheduler; §21 forbids concurrent resolution | Approved |
| REQ-049–REQ-060 | New foundation requirements (below) | Provisional |

### 27.2 New requirements added here

| ID | Requirement | Status | Source |
|---|---|---|---|
| REQ-048 | A turn is identified by its 2-hour UTC slot; its window is half-open and its display number is relative to the world epoch | Provisional | This document §10 |
| REQ-049 | An action belongs to the turn open at the server's receipt instant; the boundary instant belongs to the later turn; no grace window | Provisional | §11 |
| REQ-050 | Turn states and transitions are fixed; the accepted set is frozen at LOCKED and never reopened | Provisional | §12 |
| REQ-051 | Boundary phases run in the published P0–P7 order, each with declared inputs, permitted changes and invariants | Provisional | §13 |
| REQ-052 | Ordering is deterministic and published; contested resources are allocated order-independently, never by hidden processing order | Provisional | §14–§15 |
| REQ-053 | Every action is validated at submission **and** re-validated at resolution; acceptance never implies effect | Provisional | §17 |
| REQ-054 | Costs are reserved exclusively at acceptance, charged at resolution, released on failure/cancel/expiry; reservations never exceed the balance | Provisional | §19 |
| REQ-055 | Accepted actions may be amended or cancelled only while their turn is OPEN; the frozen set cannot change | Provisional | §18 |
| REQ-056 | Every completed turn produces a digest with per-resource deltas and per-action provenance, using stable failure codes | Provisional | §17.4, §23 |
| REQ-057 | Every field carries one visibility class (public/alliance/private/restricted), and aggregates must not leak private components | Provisional | §9 |
| REQ-058 | History is bounded: one digest row per nation-turn, permanent rows only for class-P events | Provisional | §23 |
| REQ-059 | An interrupted turn has one outcome; recovery is forward-only from phase checkpoints and never publishes twice | Provisional | §21 |
| REQ-060 | One shared world; no shards, realms or player-private timelines in the initial design | Provisional | §7 |

No inherited ID was renumbered. REQ-017's text is unchanged; only its status and coverage moved.

### 27.3 Coverage summary

60 requirements: **12 Approved**, **39 Provisional**, **7 Open**, **2 Deferred**. Executed validations: **0** — nothing in this document has been run against an implementation.

---

## 28. Approved, provisional and proposed rules

| Rule group | IDs | Status | Basis |
|---|---|---|---|
| Mapless symbolic world | TR-012, TR-013 | **Approved** constraint; model provisional | REQ-041, DD-013 |
| One shared world | TR-011 | Provisional | UD-026 open |
| Core loop and session shape | TR-001…TR-007 | Provisional | REQ-001, DP-002 |
| Feedback contract | TR-008…TR-010 | Provisional | REQ-020, DP-004 |
| Relationship and visibility model | TR-019…TR-023 | Provisional; aggregate threshold **decided** by D-027 and pending-act visibility by D-030 | REQ-012/057, SDQ-004 |
| Clock, identity, boundary | TR-024…TR-034 | Provisional; cadence **Approved** | REQ-015/048/049 |
| Lifecycle and phases | TR-035…TR-043 | Provisional | REQ-050/051 |
| Ordering and simultaneity | TR-044…TR-056 | Provisional | REQ-017/052; UD-003 resolved |
| Action lifecycle and failure codes | TR-057…TR-066 | Provisional | REQ-053/055 |
| Reservation and consistency | TR-067…TR-076 | Provisional | REQ-005/018/054; DD-011 |
| Recovery | TR-077…TR-083 | Provisional; policy **decided** by D-025, technical parts Deferred | REQ-059 |
| Inactivity and fairness | TR-084…TR-087 | Provisional; dormancy **decided** by D-028, enforcement Deferred | REQ-022, DP-002 |
| Reporting and history | TR-088…TR-092 | Provisional; retention **decided** by D-026 | REQ-020/021/058 |
| Subsystem contract | TR-093…TR-097 | Provisional | REQ-046/053 |

**No numeric balance value was decided by this document.** Operations Points are an approved military-only model (D-015) with provisional values; no general action currency was introduced. The other rules here remain provisional design positions, not owner approvals.

---

## 29. Unresolved questions

Resolved here, with the resolution recorded in the [unresolved register](05_unresolved_design_decisions.md):

| ID | Resolution |
|---|---|
| **UD-003** | **Resolved.** The ordering catalogue is §14 TR-044…TR-049: fixed P0–P7 phases, B0–B4 bands, `(priority, submitted_at, action_id)` key, order-independent allocation for contested resources, published seed derivation. |
| **UD-004** | **Resolved.** The volume shape is one bounded digest row per nation-turn plus class-P event rows (§23 TR-089); retention is 30 days hot → 12 monthly summaries → deleted, class-P permanent (D-026, TR-092). The byte budget is now a Stage 3 measurement, not an open design question. |
| **UD-018** | **Resolved by D-015** (not by this document). The military action model is a single Operations Points pool, defined in TR-005. Prompt 10 owns the order costs and war rules. |
| **UD-025** | **Resolved by D-028** (not by this document). Dormancy begins after 14 days/168 turns without an authenticated session; dormant nations cannot initiate or be targeted by offensive actions, suffer no decay, and are excluded from rankings; archival at 12 months is reversible. Prompt 03 applies it. |
| **UD-027** | **Resolved by D-027.** Published aggregates require at least 5 contributors, stable merging and complementary suppression (TR-022). |
| **UD-028** | **Resolved by D-025.** A FAILED turn delays the world; accepted actions stay pending, no cost is charged unless it completes, and only an operator-recorded void releases reservations with disclosure (TR-080). |
| **UD-029** | **Resolved by D-030.** A pending diplomatic proposal is visible to its named counterparty while open, not to third parties until declared, effective or published; rejection/withdrawal is private unless published (TR-020). |
| **UD-030** | **Resolved by D-019.** Within P3, production/income is applied before mandatory upkeep; a shortfall after income invokes Prompt 04's deficit rule and never consumes a reservation. |

Raised by this prompt and recorded as new register entries:

| ID | Question | Class | Status |
|---|---|---|---|
| UD-026 | May the world ever be split into shards/worlds, and on what capacity evidence? | E | **Open** — needs Stage 3 capacity evidence |

---

## 30. Validation and acceptance criteria

**What was checked for this document (2026-10-23):**

| Check | Method | Result |
|---|---|---|
| Required sections present and ordered | validator over this file | PASS — §1–§31 with the required 29 areas |
| 2-hour UTC cadence and 12/day preserved | rule scan + validator | PASS — TR-024/TR-025; no alternative cadence |
| Mapless world preserved | rule scan + validator | PASS — TR-012; no coordinates, distances or fronts |
| Boundary rule unambiguous | worked examples B/D vs TR-029 | PASS — one rule, one table, no exception |
| Action states and transitions coherent | §17 table vs diagram | PASS — eight states, five terminal paths, one transient |
| Reservation model has no double-spend path | §19 vs §20 G1 | PASS by construction; implementation unproven |
| Duplicate and recovery behaviour specified | §20/§21 + examples H/G | PASS |
| Ordering is deterministic and published | §14 + example D | PASS — UD-003 resolved |
| No presence requirement | TR-084/TR-085 + example F | PASS |
| No private data in reports or aggregates | TR-021/TR-022/TR-023 | PASS as a rule; enforcement deferred |
| Cross-document consistency | validators + manual read | PASS after the register updates recorded in the progress log |
| Any implemented claim | scan | PASS — none made; CF-03/CF-06 remain open |

**Acceptance criteria for this prompt** (all met by the document plus the register updates):

1. A reader can state what happens between 10:00 and 12:00 UTC and in what order.
2. Every action has exactly one timing class and one lifecycle state.
3. Every later subsystem has an explicit contract and an owner for each open ordering question.
4. No rule requires presence, introduces geography, changes the cadence, or presents a provisional Operations Points value as approved.
5. The registers and continuity files agree, and the validators pass.

**What this does not demonstrate.** No turn has been resolved under these rules, no scheduler change was made, and no capacity claim follows from them. The ordering catalogue is a design commitment to be tested in Stage 3/5, not evidence that it works.

---

## 31. Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-23 | Created for Stage 2, Prompt 02. Resolves UD-003 and UD-004's volume half. Adds REQ-048…REQ-060, DD-021…DD-032, UD-025…UD-030. No implementation, migration or hosting change. |
| 1.1 | 2026-10-23 | TR-005 extended with the approved Operations Points model (D-015); P3 income-before-upkeep confirmed (D-019); status notes aligned with D-004's supersession. No rule renumbered; no numeric value added. |
| 1.3 | 2026-10-23 | Consistency pass after the autonomous decision pass: TR-041 marks the income-before-upkeep point confirmed (D-019), TR-042's first row is recorded as decided rather than open, the later-prompt inheritance table no longer asks Prompt 04/07/10 to re-decide settled questions, and §29 lists UD-030 as resolved instead of raised. No rule text, number or example changed. |
| 1.2 | 2026-10-23 | Reference block updated to D-001…D-023 and the boundary wording changed from "no promotion of D-004" to "no unapproved promotion of an Operations Points value" (D-014/D-015). No rule, example or requirement changed. |
| 1.3 | 2026-10-23 | UD-030 marked resolved in TR-041/TR-042, §28 and §29 so the document no longer asks Prompt 04 to re-decide the P3 order. No rule changed. |
| 1.4 | 2026-10-23 | Decision-closure audit: TR-022 gains the k = 5 threshold and complementary suppression (D-027); TR-080 gains the player-facing FAILED-turn treatment (D-025); TR-092 replaces open retention with the 30-day/12-month policy (D-026); TR-096 hands Prompt 03 the decided dormancy policy (D-028) and verified-e-mail gate (D-029). No rule renumbered. |
| 1.5 | 2026-10-23 | UD-029 resolved by D-030: TR-020 gains the pending-proposal visibility rule; TR-096 hands the implementation to Prompt 08. No rule renumbered. |
| 1.6 | 2026-11-04 | Prompt 10B-C3: TR-005 adopts one OP regenerated at the opening of P3.7, cap-enforced, with carry below the cap and explicit `HELD`/`CONSUMED`/`RELEASED`/`REGENERATED` accounting; the P3 phase table records the OP balance change; §24 replaces the ambiguous Alliance "war-room scope" with the `AX-18`/`UD-049` coordination-notice boundary and records the amended B-10 contract. No phase, rule ID or value added. |
