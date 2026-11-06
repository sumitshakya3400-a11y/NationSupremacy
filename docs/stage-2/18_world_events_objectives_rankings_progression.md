# B-11 — World Events, Objectives, Rankings and Long-Term National Progression

**Version:** 1.0 · **Created:** 2026-11-05 · **Stage 2, Prompt 11B** · **11B-C2 correction; C3 acceptance 2026-11-05**
**Status:** **Specification complete at the documentation level. Unimplemented, uncalibrated and untested.** Acceptance is recorded in the [52-gate crosswalk](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md), with the original criteria preserved in the [acceptance source artifact](18_world_events_objectives_rankings_progression_acceptance_source.md).
**Authority:** This document is the authoritative statement of the B-11 rule family. It defines the rules; the [B-11 formula register](18_world_events_objectives_rankings_progression_formula_register.md) defines every calculation. Where prose and register diverge, the register governs and this document is corrected. No other document may restate a B-11 rule; other documents link here.
**Companions:** [11A research](research/11A_world_events_objectives_rankings_progression_research.md) · [11A comparator register](research/11A_comparator_sources_and_benchmarks.md) · [11A integration and risk registers](research/11A_integration_and_risk_registers.md) · [requirements](03_requirements_traceability.md) · [decisions](04_approved_and_provisional_decisions.md) · [unresolved decisions](05_unresolved_design_decisions.md) · [acceptance crosswalk](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md) · [roadmap](01_stage_2_prompt_roadmap.md).

**What this document is not.** It is not an implementation, a migration, a screen design, a moderation policy or a balance proof. It does not authorize code, deployment, live data or a release. "Specified" ≠ "implemented" ≠ "runtime tested" ≠ "balanced" ≠ "released". B-11 structural formulas and inherited approved constants retain their documented classifications and approval status. All unapproved numerical calibration parameters remain provisional and require Prompt 14 review. Structural formulas containing provisional parameters are structurally specified but are not numerically finalized.

---

## 1. Purpose, scope and acceptance target

**WEP-001 — Purpose.** *Approved (D-146…D-151).* B-11 specifies four connected systems for one persistent, mapless, shared world: world events (Domain A), national objectives and challenges (Domain B), standings and competitive recognition (Domain C), and long-term national progression (Domain D). The four domains share one terminology, one data-ownership model and one P6 evaluation order, while retaining distinct responsibilities.

**WEP-002 — Why the four systems are one rule family.** *Approved (D-148, D-149).* A single completion may emit a record, an honour and a standing entry at once (`11A-DR-014`). Splitting the four domains into four disconnected specifications would duplicate the deduplication key, the eligibility check and the historical record, and would create competing sources of truth. B-11 therefore specifies one architecture with four domains.

**WEP-003 — Scope.** *Approved.* In scope: event definitions and instances; objective definitions and instances; progress records; standings and snapshots; achievements, milestones, honours and authorship unlocks; reward definitions and reward records; eligibility; state machines; failure codes; audit events; privacy; cross-system contracts; and the Prompt 11C handoff. Out of scope: gameplay code, database schema, API, screens, moderation enforcement, calibrated numbers, and any change to B-02…B-10.

**WEP-004 — Acceptance target.** *Approved.* Prompt 11B is complete at the system-specification level when the four domains have normative rules, every calculation resolves to the formula register, every rule traces to a source, every affected subsystem contract exists, and the validator in [`docs/qa_backups/11B_validate_b11.py`](../qa_backups/11B_validate_b11.py) passes. Acceptance is **not** implementation, runtime proof or balance.

**WEP-005 — No second scheduler.** *Approved (TR-040, TR-042, D-150).* All B-11 evaluation occurs inside B-02's existing phases. B-11 creates no cron job, no timer service, no second turn loop and no real-time window. A rule expressed in minutes is invalid; every window is a turn count or a named boundary (`11A-CR-026`).

---

## 2. Authority, source hierarchy and normative language

**WEP-006 — Source hierarchy.** *Approved (D-014).* Where sources conflict, the order is: (1) owner-fixed Category A constraints and owner-reserved decisions; (2) accepted B-02…B-10 rules; (3) approved B-11 decisions D-144…D-161 and DD-192…DD-209; (4) verified authoritative research; (5) verified secondary research; (6) classified inference; (7) Category C provisional assumptions. A lower source never overrides a higher one.

**WEP-007 — Inherited rules are read, not restated.** *Approved.* B-11 cites B-02…B-10 identifiers and never rewrites their text. If a B-11 rule appears to contradict an owning subsystem, the owning subsystem governs and the conflict is recorded in §24; B-11 may not be used to amend another subsystem.

**WEP-008 — Research is not a rule.** *Approved (D-145).* The 34 `11A-DR` recommendations are evidence-linked inputs. Only D-144…D-151 are binding design directions; only this document's `WEP-` rules are binding B-11 rules. A recommendation not adopted here has the disposition recorded in §23.

**WEP-009 — MUST.** *Approved.* "MUST" and "MUST NOT" state a mandatory rule. A violation is a specification defect; the validator fails and the implementation may not ship.

**WEP-010 — SHOULD.** *Approved.* "SHOULD" and "SHOULD NOT" state the expected design. A deviation requires a recorded reason in §24 and a decision entry; the validator checks that a deviation has that record.

**WEP-011 — MAY.** *Approved.* "MAY" states a permitted option that carries no obligation. A "MAY" is never read as a requirement, and a player's failure to use a permitted option is never a failure to comply.

**WEP-012 — Normative consistency.** *Approved.* A rule described as mandatory in one section MUST NOT be described as optional in another. The rule inventory in §22 is generated from the identifiers, not from prose, so a duplicate or contradictory statement is a defect.

**WEP-013 — Terminology is binding.** *Approved.* The terms in §3 are the only permitted meanings in B-11. A synonym that changes meaning — in particular "objective" used for a B-10 campaign objective — is a defect. `11A-INT-32` is resolved by WEP-020.

**WEP-014 — No consent by silence.** *Approved (D-014 §5.6, REQ-523, `11A-CR-027`).* The game MUST NOT accept an objective, join an event, choose a reward, accept a treaty, spend treasury, or take any discretionary national action on a player's behalf because a notification was delivered or a timer elapsed. Silence is never consent. System bookkeeping that an accepted rule authorizes is not a discretionary choice.

---

## 3. Terminology

**WEP-015 — Event definition.** *Approved.* A reusable, versioned **template** (a parameter row) from which event instances are generated. It has a stable definition ID and an immutable published version.

**WEP-016 — Event instance.** *Approved.* One occurrence generated from one published definition version. It has its own instance ID, occurrence key, state and historical record. Changing a definition never rewrites a completed instance.

**WEP-017 — World event.** *Approved.* An event whose scope is `WORLD` or `ALLIANCE` and whose trigger is a published rule. A player may create a **challenge** object; a player never creates a world event.

**WEP-018 — National objective.** *Approved (D-153).* A goal offered to one nation by B-11. The only correct short form in B-11 is "national objective" or "strategic objective". The unqualified word "objective" is reserved for B-10's **campaign objective**.

**WEP-019 — Campaign objective.** *Approved (D-153).* B-10's primary or secondary war aim (`WAR-006`). It is owned by B-10 and is never a B-11 object. B-11 MUST NOT re-emit `WRA-06 OBJECTIVE_PROGRESS` for a national objective.

**WEP-020 — Objective instance.** *Approved.* One nation's accepted or auto-tracked occurrence of a published national-objective definition, with its own state and progress records.

**WEP-021 — Standing.** *Approved (D-148).* A published comparative ranking of eligible nations or alliances. A standing is one of the five recognition objects in WEP-025 and is not a score that gates events, rewards or basic play.

**WEP-022 — Eligibility measure.** *Approved (D-148, `11A-DR-010`).* The separate, published **World Standing Eligibility (WSE)** status defined in §8.6. It answers "may this nation appear in a competitive standing?" and is never a rank, a score or a reward key.

**WEP-023 — Snapshot.** *Approved.* The immutable per-turn record of a standing's inputs, result and rank order, sealed in P6 and published in P7. Weekly, monthly and seasonal standings are derived from snapshots, not recalculated from live state.

**WEP-024 — Season.** *Approved (D-149, `11A-DR-018`).* An in-place named window with a season identifier. A season resets seasonal standings and seasonal progress only; it never resets national state, permanent records or honours.

**WEP-025 — Five recognition objects.** *Approved (`11A-DR-013`).* B-11 distinguishes exactly five objects: **achievement** (keyed binary grant), **milestone** (state-derived threshold record), **seasonal award** (season-scoped recognition), **historical honour** (permanent world-state or event recognition) and **standing** (comparative snapshot). Each declares persistence, eligibility closure and reassignment. Collapsing two objects is a defect.

**WEP-026 — Honour class.** *Approved.* A categorical label on a permanent honour. It is not a currency, balance or spendable value. There is no prestige currency (`ECN-092`).

**WEP-027 — Reward.** *Approved (D-151).* A defined consequence of a completion, in one of six classes: recognition, record, authorship, cosmetic, title, or material. A reward is not an event or objective; it is the output of one.

**WEP-028 — Material reward.** *Approved (D-151, `ECN-113`).* A reward that changes a B-04 balance (Crowns or resources). It is rare, disclosed before grant, keyed, ledgered through the existing `REWARD` event type, non-transferable in effect and never a permanent yield multiplier.

**WEP-029 — Chronicle.** *Approved (UD-024 resolved by D-158).* The append-only class-P permanent record of notable world facts. It is not a narrative feed and not a second history store; B-02 owns the history class, B-11 owns notability.

**WEP-030 — Derived progression.** *Approved (D-149).* The permanent progression layer is computed from owning-subsystem state plus the chronicle. It is not a stored numeric resource and introduces no new balance.

**WEP-031 — Nation scope and account scope.** *Approved (`11A-DR-024`).* A nation-scope object is forfeited on reroll and retained as history. An account-scope object survives a reroll only when it is non-transferable and not re-earnable. Every B-11 object declares its scope.

**WEP-032 — Occurrence key.** *Approved.* The canonical idempotency identity of an event instance or objective activation, formed from the definition ID, definition version and occurrence discriminator (WEP-033). One occurrence key produces at most one instance.

**WEP-033 — Achievement key.** *Approved (TR-055, TR-073 G2, `ECN-155`).* The canonical idempotency identity of a grant: `(nation_id, achievement_id, achievement_version, scope_key, tier_id)`. One key grants at most one record and at most one material reward.

**WEP-034 — Fingerprint.** *Approved.* The frozen hash of the authoritative input set used by a calculation, recorded with every snapshot, progress record and grant. A replay with the same inputs and the same fingerprint must produce the same result.

**WEP-035 — Deterministic.** *Approved (TR-047, TR-048).* A calculation is deterministic when it is a pure function of its declared inputs and the frozen turn seed. No B-11 calculation reads wall-clock time, player activity, login state, latency or environment entropy.

**WEP-036 — Withheld.** *Approved (D-027).* A published figure is withheld when publishing it would identify fewer than `k = 5` contributing entities. Withholding is stated, never silent.

**WEP-037 — Coarsened.** *Approved (D-027).* A figure is coarsened when it is replaced by a published band wide enough that no individual value can be recovered, including by complementary suppression and differencing.

**WEP-038 — Correction.** *Approved (TR-091).* A correction is a new appended record that references the original. Editing or deleting a published historical record in place is prohibited.

---

## 4. Architecture overview

**WEP-039 — One model, four domains.** *Approved (D-144…D-151).* Domain A owns event definitions, instances and event history. Domain B owns objective definitions, instances, progress and objective history. Domain C owns standing definitions, snapshots and ranking history. Domain D owns achievements, milestones, honours, authorship unlocks, seasons and the chronicle's notability. §15 is the complete ownership matrix.

**WEP-040 — Shared identifiers.** *Approved.* Every B-11 object has a stable identifier in one of these spaces: `WEP-` (rule), `F-WEP-` (formula), `WPC-` (cross-system contract), `WPA-` (audit event), `WPF-` (failure code), plus the object IDs in §4.3. An identifier is never reused for a different meaning.

**WEP-041 — Shared eligibility.** *Approved.* Event eligibility (§6.5), objective eligibility (§7.4) and standing eligibility (§8.6) all read B-03's authoritative protection, dormancy, retirement and pair states. B-11 defines no parallel protection model and no new privacy threshold.

**WEP-042 — Shared reward identity.** *Approved.* Every reward is resolved by its achievement key (WEP-033). The first valid grant in the published P6 order wins; every later claim for the same key is deduplicated and recorded, not silently dropped (`TR-055`).

**WEP-043 — Shared record discipline.** *Approved.* Every permanent B-11 outcome is an append-only class-P record written inside the transaction that causes it. Corrections append a new record. Nothing in B-11 may compact, overwrite or re-parent a class-P record.

**WEP-044 — Shared privacy model.** *Approved (D-027).* B-11 adds no privacy threshold and no visibility class. It uses B-02's existing classes and applies `k = 5` to every aggregate, including alliance, military and event-participation figures.

**WEP-045 — No competing source of truth.** *Approved.* B-11 MUST NOT store a copy of a B-04 balance, B-05 infrastructure, B-06 political state, B-07 trade, B-08 agreement, B-09 membership or B-10 campaign value. It stores the **reference** and the **derived result**, and it re-reads the owner at every validation boundary.

**WEP-046 — No new resource.** *Approved.* B-11 creates no currency, resource, points balance, prestige pool, level or XP. A standing is a published comparison; a milestone is a record; an honour is a label; a reward is a ledgered transfer from an authorized source.

**WEP-047 — No retroactive mutation.** *Approved (TR-040, TR-041).* A P6 rule may not change an earlier phase's outcome. A ranking describes the turn that happened. An event may not rewrite a prior turn's production, combat or settlement.

**WEP-048 — Fail closed.** *Approved (TR-056).* If an input is missing, stale, ambiguous or inconsistent with the frozen baseline, the B-11 operation fails with a `WPF-` code, releases any reservation, writes no partial record and changes no state.

**WEP-049 — Idempotent by construction.** *Approved.* Every B-11 write is keyed and idempotent. Replaying the same key at the same turn produces one record, one grant and one audit event. A duplicate request returns the original outcome.

**WEP-050 — Published order.** *Approved (D-150, TR-044 B4, TR-049).* The intra-P6 order is fixed and player-readable: **W1 event resolution → W2 objective evaluation → W3 standing snapshot → W4 record writes → W5 deferred-claim release**, with publication in P7. This closes the `TR-042` question "Are world events generated before or after objective evaluation?" — events come first.

**WEP-051 — Architecture of the event machinery.** *Approved (D-146).* One shared parameterised machinery serves four event classes. Adding an event means adding a published definition row, not authoring a feature. No event requires a human author at runtime.

**WEP-052 — Architecture of the objective machinery.** *Approved (D-147).* One objective container serves all categories. Adding an objective means adding a published definition row and, where the category requires it, a catalogue entry. The B-03 onboarding journey is extended, never re-opened.

**WEP-053 — Architecture of the standing machinery.** *Approved (D-148).* Every standing declares inputs, window, snapshot point, tie rule, eligibility set and exclusion rule. No standing is defined only in prose; every metric resolves to a formula in §22.

**WEP-054 — Architecture of the progression machinery.** *Approved (D-149).* Progression is derived, honour-based and non-compounding. There is no level, no XP and no permanent capability. Authorship is the highest-value reward class.

---

## 5. Fixed constraints (Category A)

**WEP-055 — B-02 owns the turn.** *Approved (TR-040).* P6 is "World — evaluate objectives, rankings, systemic events". B-11 owns the contents of P6 and nothing about the phase structure. P7 publication is B-02's.

**WEP-056 — No presence mechanic.** *Approved (TR-006, TR-007, TR-085, AP-001).* No event, objective, standing or reward may require a player to be online at a particular moment, act every turn, maintain a streak, or log in to avoid a loss. Waiting is a valid strategy.

**WEP-057 — No decay and no loss through absence.** *Approved (D-028).* Dormancy excludes a nation from public standings as a presentation rule and causes no loss of resource, progress, honour, ownership or title. A deferred claim never expires because of absence.

**WEP-058 — Protection is respected.** *Approved (ONB-023…ONB-025).* A protected nation MAY appear in non-hostile standings and MAY take part in non-offensive events. It MUST NOT be made a hostile-event target or a hostile-objective target. No objective or event may bypass protection.

**WEP-059 — Player sovereignty.** *Approved (D-014 §5.6).* B-11 never starts a war, accepts a treaty, joins an alliance, spends treasury, chooses a policy, accepts a settlement or claims a discretionary reward on a player's behalf. A system may record a fact it already owns; it may not exercise a choice.

**WEP-060 — One account, one active nation.** *Approved (D-032, D-034, D-039).* B-11 rejects any participation, progress or award that depends on a second active nation on the same account. Pair restrictions are read from B-03, never re-derived.

**WEP-061 — No age or purchase differential.** *Approved (NAT-045, INV-025).* No standing, event, objective or honour may read account age, nation age (as merit), reroll count, referral, purchase, alliance membership or time of day as an eligibility or weighting input. Tenure MAY be displayed and commemorated, never ranked.

**WEP-062 — No market statistic before the gate.** *Approved (D-122, DD-136, REQ-513, MKT-072…MKT-076).* A trade-derived standing or objective MAY be specified, but its publication MUST remain blocked while any Global Trade gate G-1…G-6 is unmet. G-1, G-2, G-3, G-5 and G-6 are not met and G-4 is partial; no B-11 rule changes that state.

**WEP-063 — No political state control.** *Approved (DMP-141, DMP-266).* An event or reward may move a named support term, a stability term, food or approval through the normal formula and cap. It MUST NOT set `approval` or `leadership_state` directly, resolve a contest, remove a leader, grant a campaign bonus, or grant population, a policy, a government or legitimacy.

**WEP-064 — No city damage through events.** *Approved (URB-035, URB-040, URB-045).* No event or objective may damage, destroy, capture, transfer or delete a city or facility, or take infrastructure below its floor. B-10's bounded `OP-05` exception is B-10's alone and is not available to B-11.

**WEP-065 — No military value exposure.** *Approved (WAR-162).* No exact readiness, force, inventory or OP value may appear in a B-11 standing, event record or chronicle entry. Military recognition is by participation, defensive outcome and published band only.

**WEP-066 — No alliance military power.** *Approved (AX-18, ALL-134, ALL-224, UD-047, UD-049).* B-11 MUST NOT create Alliance military command, a shared OP pool, an Alliance military treasury, a member-funded prize or a binding military order. Alliance recognition is honour-only and aggregate-only at `k ≥ 5`.

**WEP-067 — No OP reward.** *Approved (TR-005, D-015, WAR-040).* Operations Points have exactly one lawful increase: the P3.7 regeneration. No event, objective, achievement or standing may grant, refund, convert or transfer OP.

**WEP-068 — No purchasable recognition.** *Approved (`11A-DR-012`).* No achievement, honour, standing, eligibility status, skip, boost or reward may be bought, promoted, gifted or granted for real money or an external benefit. This includes any "supporter" variant.

**WEP-069 — No second privacy threshold.** *Approved (D-027).* `k = 5`, complementary suppression and the ban on cross-turn and cross-table differencing are reused verbatim. B-11 invents no other threshold and no other suppression rule.

**WEP-070 — No implementation claim.** *Approved (D-012).* This document may not be cited as evidence that any event fired, any ranking was computed, any reward was granted or any player saw a screen. It is a specification.

---

## 6. Domain A — World Events

### 6.1 Event taxonomy

**WEP-071 — Four classes.** *Approved (D-146, `11A-DR-001`).* B-11 recognizes exactly four event classes: `EV-CAL` **calendar**, `EV-STATE` **state**, `EV-CHAL` **challenge**, and `EV-COMM` **commemorative**. A fifth class requires a new decision and a register row.

**WEP-072 — Scope, not class.** *Approved.* "Global" and "national" are **scopes**, not classes: `WORLD`, `NATION` or `ALLIANCE`. Milestone-triggered, system-triggered and seasonal occurrences are **triggers** on a class, not separate classes. This resolves the nine candidate categories in the Prompt 11B brief into one coherent taxonomy.

**WEP-073 — `EV-CAL` calendar events.** *Approved.* Deterministic occurrences fixed by a published schedule derived from the world clock or a world aggregate. Examples: a weekly recognition window, a monthly season rollover, a scheduled world-state publication. Purpose: predictable rhythm without authored content. They MUST be derivable in advance from published rules.

**WEP-074 — `EV-STATE` state events.** *Approved.* Occurrences generated when published thresholds over owning-subsystem state are met. Examples: a nation completes a capstone; the world first passes a development threshold; a nation's stability enters or leaves a named state. Purpose: recognition and information tied to actual play. They MUST read owning state, never a UI route or incidental implementation.

**WEP-075 — `EV-CHAL` challenge events.** *Approved (D-146, `11A-DR-007`).* Player-initiated, reservation-backed, expiring and counterparty-independent contest objects. Purpose: player-generated content with bounded capital risk. They MUST NOT be a route around the trade gate, protection, pair restrictions or the attack-prevention layers. A challenge is never a world event and never binds a third party who did not accept it.

**WEP-076 — `EV-COMM` commemorative events.** *Approved.* One-time world-state anchors that create a permanent honour or chronicle entry, such as "the first nation to reach a published development milestone". Purpose: durable recognition at zero recurring cost. They MUST use a world-state trigger, not a first-mover race, except where WEP-079 permits a disclosed closed-eligibility honour.

**WEP-077 — `WORLD` scope.** *Approved.* The occurrence is visible to every nation and its eligibility set may include every eligible nation. A world-scope event may publish a shared parameter change only through a named term and a ledger event where material.

**WEP-078 — `NATION` scope.** *Approved.* The occurrence concerns one nation. It is recorded on that nation's history and visible under the nation's visibility class. A nation-scope event never creates a public comparison by itself.

**WEP-079 — `ALLIANCE` scope.** *Approved (D-027, ALL-156, ALL-224).* The occurrence concerns an Alliance. Its public record is an aggregate at `k ≥ 5`; no member-level value is exposed; no prize is funded from Alliance value. If the eligible group is below `k`, the public form is withheld and only the members' private records remain.

**WEP-080 — Trigger catalogue.** *Approved.* The permitted triggers are `SCHEDULED_INSTANT` (a named boundary or turn interval), `WORLD_STATE` (a published world threshold), `NATION_STATE` (a published national threshold), `PLAYER_INITIATED` (a created challenge), and `WORLD_ANCHOR` (a one-time world-state anchor). No other trigger exists.

**WEP-081 — Class–trigger matrix.** *Approved.* `EV-CAL` uses `SCHEDULED_INSTANT`; `EV-STATE` uses `WORLD_STATE` or `NATION_STATE`; `EV-CHAL` uses `PLAYER_INITIATED`; `EV-COMM` uses `WORLD_ANCHOR`. A class with a trigger outside its row is invalid and fails `WPF-02`.

**WEP-082 — Seasonal events are calendar events.** *Approved (D-149).* A seasonal event is an `EV-CAL` occurrence carrying a `season_id`. The season is an in-place window; it does not create a world instance, a second world or a reset of national state.

### 6.2 Event definition and event instance

**WEP-083 — Definition fields.** *Approved.* Every event definition MUST declare: definition ID; version; class; scope; trigger; parameter set; eligibility rule reference; start condition; end condition; effect list; reward list; visibility; recurrence policy; occurrence cap; teardown policy; notability class; audit requirements; and an inertness statement (what the event does **not** grant).

**WEP-084 — Published version is immutable.** *Approved.* A published definition version is immutable. A change creates a new version with a new `definition_version` and a `supersedes` reference. Instances already generated keep their original version and outcome.

**WEP-085 — Definition states.** *Approved.* A definition is `TEMPLATE_DRAFT` → `TEMPLATE_PUBLISHED` → `TEMPLATE_RETIRED`; a published version becomes `TEMPLATE_SUPERSEDED` when a later version is published. Only `TEMPLATE_PUBLISHED` may generate instances.

**WEP-086 — Instance fields.** *Approved.* Every instance MUST record: instance ID; definition ID and version; occurrence key; class; scope; trigger record; eligibility set fingerprint; start and end boundaries; state; participant set; progress and result records; reward records; teardown boundary; historical record ID; audit IDs.

**WEP-087 — Occurrence key.** *Approved.* `occurrence_key = hash(definition_id, definition_version, occurrence_discriminator)`, where the discriminator is the scheduled boundary, the world-state threshold crossing, the nation-state threshold crossing or the challenge ID. The same key MUST NOT generate a second instance (`WPF-05`).

**WEP-088 — Version pinning.** *Approved.* An instance is evaluated against the definition version pinned at qualification. A later version does not change an active instance's rules; it applies only to future instances. This prevents a mid-event rule change from altering a player's expected outcome.

**WEP-089 — Definition retirement.** *Approved.* Retiring a definition stops new instances. It does not cancel active instances, delete history or invalidate honours. Active instances continue under their pinned version.

**WEP-090 — Instance fields are append-only after `ACTIVE`.** *Approved.* After activation, the definition fields cannot change. Only state, participant records, progress records, result records and audit records may be appended.

**WEP-091 — Challenge definition.** *Approved (D-146, `11A-CR-008`).* A challenge definition is created by the initiating player and MUST declare: the target condition, the counterparty, the reserved stake, the expiry boundary, the independence proof requirement, the no-self-claim rule and the release rule. The creator cannot be the claimant or a restricted pair of the claimant.

**WEP-092 — Challenge reservation.** *Approved (TR-067).* The stake is reserved at creation through the owning subsystem's reservation mechanism. It is released on expiry, cancellation or completion; it is never forfeited silently.

**WEP-093 — Challenge expiry.** *Approved.* A challenge has a stated expiry in turns or a named boundary. At expiry the reservation is released and the challenge is recorded as `EXPIRED`; the creator may not extend it retroactively.

**WEP-094 — Challenge independence.** *Approved (Prompt 12 owns enforcement).* Before a claim is credited, B-11 MUST record the pair-state check and the declared-relationship check. A claim by a restricted pair or a colluding counterparty is rejected with `WPF-10`; suspected collusion is flagged for Prompt 12, not punished by B-11.

**WEP-095 — Challenge is not a transfer channel.** *Approved (ECN-113, REQ-073).* A challenge stake and payout MUST NOT be used to circumvent trade limits, embargoes, the Global Trade gate or pair restrictions. A challenge that would move value between restricted parties is invalid.

**WEP-096 — No duplicate active challenge.** *Approved.* One creator–counterparty–condition triple may have at most one active challenge at a time. A second identical active challenge fails with `WPF-11`.

**WEP-097 — Commemorative anchor definition.** *Approved.* A commemorative definition declares the world-state predicate, the once-only anchor, the honour class and the closed-eligibility policy. It MUST record whether the honour is world-state-triggered or disclosed first-N.

**WEP-098 — Closed-eligibility disclosure.** *Approved (`11A-DR-016`).* A first-N honour is permitted only where the closure (the N, the window and the start boundary) is published before the first grant. A closed honour that becomes unobtainable without prior disclosure is invalid.

### 6.3 Event lifecycle and state transitions

**WEP-099 — Instance states.** *Approved.* An event instance is in exactly one state: `QUALIFIED`, `SCHEDULED`, `ANNOUNCED`, `ACTIVE`, `CLOSED`, `COMPLETED`, `EXPIRED`, `CANCELLED` or `VOIDED`. `COMPLETED`, `EXPIRED`, `CANCELLED` and `VOIDED` are terminal.

**WEP-100 — `QUALIFIED`.** *Approved.* The trigger has fired and the instance key is unique. Entry requires a published definition, a valid trigger record and a passing eligibility pre-check. No player sees a qualified instance.

**WEP-101 — `SCHEDULED`.** *Approved.* Start and end boundaries are fixed in turns or named boundaries. Entry requires the boundary arithmetic to be valid and the teardown boundary to be later than the end boundary.

**WEP-102 — `ANNOUNCED`.** *Approved.* The instance is published in the bounded digest before activation. Entry requires the announcement boundary to be reached and the visibility class to permit the audience. Announcement is information, not consent.

**WEP-103 — `ACTIVE`.** *Approved.* Participation is open. Entry requires the start boundary, a final eligibility check and a clean P2-style validation of the participant set. Effects are not yet final.

**WEP-104 — `CLOSED`.** *Approved (D-146, `11A-DR-004`).* Participation has stopped at the closing boundary and teardown stage 1 has begun. No new participant may join. In-flight legitimate actions that were accepted before the boundary MAY still resolve within the declared teardown window; no new stake may be taken.

**WEP-105 — `COMPLETED`.** *Approved.* The completion condition is verified, results and non-material rewards are final, and the historical record is written. Entry requires `CLOSED`, a satisfied completion rule and a passing reward-eligibility check.

**WEP-106 — `EXPIRED`.** *Approved.* The end boundary was reached without a completion. Expiry is not a penalty: progress records remain, earned recognition remains, deferred claims remain valid and no resource is confiscated.

**WEP-107 — `CANCELLED`.** *Approved.* An instance is cancelled before activation because a precondition failed, a duplicate was discovered or a system-side invalidity occurred. No participation existed; no reward is due; a correction record is appended.

**WEP-108 — `VOIDED`.** *Approved.* An active or closed instance is found invalid after activation. `VOIDED` stops new grants and appends a disclosed correction. Grants already made remain valid unless Prompt 12 invalidates them with evidence; B-11 never claws back a valid grant on its own.

**WEP-109 — `RESOLVING` is not a state.** *Approved.* The resolving interval is `CLOSED` plus the declared teardown window. A separate `RESOLVING` state would duplicate teardown and invite a second clock; it is rejected.

**WEP-110 — Transition table is exhaustive.** *Approved.* The permitted transitions are exactly those in §13.1. Any other transition fails with `WPF-13` and changes no state.

**WEP-111 — Transition initiator.** *Approved.* Only the P6 world-evaluation step initiates a system transition. A player may initiate a challenge creation or a withdrawal, never a system transition. Prompt 12 may request a suspension through the registered evidence path; it does not mutate event state directly.

**WEP-112 — Transition validation.** *Approved.* Every transition re-validates the frozen baseline, the occurrence key, the definition version, the eligibility set and the teardown boundary. A transition that cannot validate fails closed.

**WEP-113 — Transition mutation.** *Approved.* A transition writes exactly one state change, one audit event and, where applicable, one result or correction record, inside one transaction. Partial transitions are prohibited.

**WEP-114 — Invalid transitions.** *Approved.* `ANNOUNCED → COMPLETED`, `ACTIVE → EXPIRED` without an end boundary, `COMPLETED → ACTIVE`, `CANCELLED → ACTIVE`, `VOIDED → COMPLETED` and any terminal-to-non-terminal transition are invalid.

**WEP-115 — Duplicate instance prevention.** *Approved.* The occurrence key is unique across all instances. A repeated generation attempt returns the existing instance and writes `WPA-25`; it does not create a second instance, reset progress or re-grant a reward.

**WEP-116 — Replay protection.** *Approved.* A replayed turn re-evaluates the same frozen inputs and the same keys. If a record already exists for a key, the replay is a no-op with an idempotency audit record. A replay MUST NOT create a new grant, progress increment or snapshot.

### 6.4 Generation, scheduling and recurrence

**WEP-117 — Generation at P6.** *Approved (D-150).* Event qualification and generation occur in P6 step W1, before objective evaluation. P3 may compute a scheduled anchor but may not generate a B-11 instance.

**WEP-118 — Deterministic generation.** *Approved (TR-047, TR-048).* Generation is a pure function of the frozen post-P5 baseline, the published definition rows, the turn ID and the frozen seed. No generation depends on request arrival, wall-clock time or operator action.

**WEP-119 — Condition-based generation.** *Approved.* A `WORLD_STATE` or `NATION_STATE` trigger fires when the published predicate transitions from false to true against the frozen baseline. It does not re-fire while the predicate remains true.

**WEP-120 — Edge-triggered, not level-triggered.** *Approved (`11A-RK-012`).* A threshold crossing fires once per crossing. An oscillating condition that re-crosses in a later turn may fire again only within the declared occurrence cap, and the cap is published.

**WEP-121 — Scheduled generation.** *Approved.* A `SCHEDULED_INSTANT` trigger fires at the named turn interval or boundary derived from the world clock. The schedule is published and derivable in advance.

**WEP-122 — Recurrence.** *Approved.* A definition MAY declare a recurrence interval and a maximum occurrence count per window. A non-recurring definition fires once per definition version and then retires the occurrence key.

**WEP-123 — Occurrence cap.** *Approved (`11A-DR-005`).* The occurrence cap is per definition, per window and per scope. A cap is enforced before generation, is published, and produces a recorded skip (`WPA-26`) rather than a silent omission (`TR-071`).

**WEP-124 — Duplicate generation protection.** *Approved.* The occurrence key plus a per-definition active-instance check prevents two active instances from the same definition and scope when the definition declares `single_active`. A duplicate attempt fails with `WPF-05`.

**WEP-125 — Template version selection.** *Approved.* Generation uses the latest `TEMPLATE_PUBLISHED` version at the qualification boundary. A version published after the frozen baseline is not used until the next turn.

**WEP-126 — Randomness.** *Approved (TR-044 B2, TR-047).* B-11 permits randomness only for selecting among equal, eligible candidates when a single winner is structurally required. The draw is a seeded lottery keyed on `(turn_id, allocation_id)`; odds are published; the seed is the B-02 frozen seed. No random reward magnitude, random eligibility or hidden random weighting exists.

**WEP-127 — Random selection must not advantage manipulation.** *Approved.* A randomized selection MUST NOT read player-supplied ordering, submission time, account identity or any value the player can influence. Equal candidates have equal published odds.

**WEP-128 — Trigger invalidation.** *Approved.* If the trigger becomes invalid before activation, the instance is `CANCELLED` with a reason. If it becomes invalid after activation, WEP-108 applies. No player is penalized for a system-side cancellation; progress earned to that point remains a record.

**WEP-129 — Frequency limits.** *Approved.* The published generation frequency, recurrence and occurrence caps bound the number of instances. A player cannot raise the frequency by repeated actions; a challenge is the only player-initiated class and is capped by WEP-096.

**WEP-130 — Seed handling.** *Approved.* The seed is the frozen turn seed already used by B-02's seeded lottery. B-11 stores the seed reference, not a new seed. A replay with the same turn ID reproduces the same selection.

**WEP-131 — No content pressure on the player.** *Approved (TR-085, `11A-DR-005`).* Generation frequency is not a participation obligation. The bounded outstanding set, penalty-free dismissal and the player's cadence setting determine what the player sees; missing an event loses nothing that was already earned.

### 6.5 Event eligibility

**WEP-132 — Eligibility is a set, not a score.** *Approved.* Eligibility is evaluated as a boolean set membership against the frozen baseline. There is no "eligibility points" value that can be farmed.

**WEP-133 — New nations.** *Approved (NAT-016).* A nation is unranked until its first completed boundary and MUST NOT enter a competitive event standing before that boundary. It MAY receive informational or non-hostile onboarding events immediately, but no competitive award is granted before its first boundary.

**WEP-134 — Protected nations.** *Approved (ONB-025).* A protected nation is included in non-hostile events and standings and excluded from every hostile event effect and hostile event target set. Protection is read from B-03 at qualification, activation and reward validation.

**WEP-135 — Active nations.** *Approved.* A nation that is neither protected, dormant nor retired is eligible subject to the definition's own conditions.

**WEP-136 — Dormant nations.** *Approved (D-028).* A dormant nation is excluded from public standings and public event participation lists as a presentation rule. It loses no event progress, honour or deferred claim; on reactivation it re-enters the next evaluation under the normal rules.

**WEP-137 — Retired nations.** *Approved (RRL-013, RRL-019).* A retired nation is removed from current event participation and current standings. Its historical event records remain attributed to it. The replacement nation starts with no event credit, no objective credit and no nation-scope honour.

**WEP-138 — Nation owners.** *Approved.* Eligibility attaches to the nation, not the account. An account-scope object is permitted only where WEP-031 allows it and the object is non-transferable and not re-earnable.

**WEP-139 — Alliances.** *Approved (D-027, ALL-156).* An Alliance is eligible for a group event only when the event's scope is `ALLIANCE`, the Alliance is active, and the public form can satisfy `k ≥ 5`. Otherwise the group form is withheld.

**WEP-140 — Seasonal participants.** *Approved.* A nation is a seasonal participant when it is eligible at the season's opening boundary and has not been excluded by WEP-136 or WEP-137. Joining a season is automatic for eligible nations; no acceptance is required because the season is a standing window, not a discretionary commitment.

**WEP-141 — Existing participants.** *Approved.* A nation already participating in an instance is not removed because a later eligibility review would exclude it, except for dormancy (public-list presentation only), retirement (record retained) or a Prompt 12 suspension. Its earned progress is not confiscated.

**WEP-142 — Revalidation boundaries.** *Approved (TR-051).* Eligibility is revalidated at qualification, announcement, activation, participation acceptance, completion verification and reward grant. A cached eligibility result is never authoritative across a boundary.

**WEP-143 — No unfair punishment for system changes.** *Approved (TR-056, D-028).* A system-side cancellation, a definition retirement or an eligibility change caused by B-03 does not forfeit earned progress, an earned honour or a valid deferred claim. The player is told what changed and why.

**WEP-144 — Eligibility failure code.** *Approved.* An ineligible participant fails with `WPF-08`. The failure changes no state and releases any reservation.

### 6.6 Event participation

**WEP-145 — Automatic versus explicit participation.** *Approved (D-014, `11A-DR-009`).* An informational or recognition-only event may include an eligible nation automatically. Any event that requires a discretionary commitment, a stake, a target or a claim requires **explicit player action**. Silence never joins, accepts or claims.

**WEP-146 — Optional participation.** *Approved.* A player MAY decline or ignore any event without penalty. An ignored event expires normally and grants nothing; it does not deduct, forfeit or reduce standing.

**WEP-147 — Opt-in record.** *Approved.* An explicit participation record MUST identify the player action, the turn, the instance, the accepted terms and the acceptance key. The record is immutable.

**WEP-148 — Participation limits.** *Approved (D-146, `11A-DR-005`).* A player MAY participate in several instances concurrently, subject to the definition's `single_active` rule, the outstanding-set cap and the challenge cap. No rule requires participation in any event.

**WEP-149 — Withdrawal.** *Approved.* A player MAY withdraw before the participation freeze. Withdrawal releases any uncommitted stake, preserves progress already verified as a record, and forfeits only a prize that the definition explicitly makes conditional on continued participation. A withdrawal is not a failure.

**WEP-150 — Re-entry.** *Approved.* Re-entry after withdrawal is permitted only if the definition declares it and the freeze has not passed. Re-entry uses a new participation record and the same occurrence key; it does not reset or duplicate progress.

**WEP-151 — Simultaneous participation.** *Approved.* A nation may hold one participation record per instance. Two participation attempts on one instance fail with `WPF-14`.

**WEP-152 — Duplicate participation.** *Approved.* A duplicate participation request returns the existing record and writes `WPA-27`. It does not double progress or reward.

**WEP-153 — Nation eligibility changes.** *Approved.* If a participant becomes protected mid-event, hostile involvement is blocked and non-hostile participation continues; progress is preserved. If it becomes dormant, it is hidden from public lists but keeps its record. If it retires, the record remains history and the replacement starts clean.

**WEP-154 — Player-controlled confirmation.** *Approved.* A confirmation prompt, a notification or a digest line is information. It does not constitute acceptance. The accepting action must be an explicit, recorded player command.

**WEP-155 — Participation freeze.** *Approved (D-146, `11A-DR-006`).* For any event with a deciding snapshot or single-winner selection, participation closes one turn before that decision. The freeze boundary is published with the event. Actions after the freeze are rejected with `WPF-15` and move nothing.

**WEP-156 — Freeze is not a presence requirement.** *Approved.* The freeze limits when an action may be accepted; it never requires a player to be online at the boundary. A player who acts earlier is unaffected.

### 6.7 Event effects

**WEP-157 — Effect classes.** *Approved.* The permitted event effects are `E-INFO` (information), `E-OBJ` (objective-progress credit), `E-RANK` (standing input), `E-ACH` (achievement or honour eligibility), `E-HIST` (historical record), `E-ECON` (authorized material reward), and `E-POL` (named political term through the normal formula and cap). No other effect class exists.

**WEP-158 — Informational effects.** *Approved.* `E-INFO` writes a digest line and, if notable, a chronicle entry. It changes no balance, standing input or political value.

**WEP-159 — Objective-progress effects.** *Approved.* `E-OBJ` credits a national objective only through §7.5's keyed progress record. The event is a source event; it is never itself the progress value.

**WEP-160 — Standing-input effects.** *Approved.* `E-RANK` may make the event outcome an input to a standing only if the standing's definition declares that event class as an input and the result is snapshotted under §8.7.

**WEP-161 — Achievement eligibility effects.** *Approved.* `E-ACH` may make a participant eligible for a declared achievement or honour. The grant still requires WEP-343's keyed award and the eligibility closure rule.

**WEP-162 — Historical effects.** *Approved.* `E-HIST` writes a class-P chronicle entry with the event instance, definition version, participants drawn from public data, result and turn.

**WEP-163 — Economic effects.** *Approved (ECN-113, ECN-013(c), D-151).* `E-ECON` is permitted only as a **rare, disclosed, keyed, ledgered** material reward, in the declared reward class, through B-04's `REWARD` event type. B-11 does not create resources; it requests a grant the owning subsystem can lawfully make.

**WEP-164 — Political effects.** *Approved (DMP-141, DMP-266).* `E-POL` may move a named support term, a stability term, food or approval through the normal formula and cap. It MUST NOT set `approval` or `leadership_state`, resolve a contest, remove a leader, grant a campaign bonus or grant a policy, government or legitimacy.

**WEP-165 — Mutation owner.** *Approved.* The owning subsystem mutates its own field. B-11 supplies the validated effect request and records the result. B-04 writes the ledger, B-05 writes infrastructure, B-06 writes political terms, and B-10 writes campaign records.

**WEP-166 — Processing phase.** *Approved.* Event effects that are not P3 inputs are applied in P6 W1 after the event state is resolved. A P3 input change is published as a parameter for the **next** P3 and is not applied retroactively to the current turn.

**WEP-167 — Validation before effect.** *Approved.* Every effect re-validates eligibility, protection, caps, ownership and the frozen baseline. A failing effect fails the whole instance effect transaction with `WPF-16`; no partial effect is written.

**WEP-168 — Accounting.** *Approved.* A material effect is one atomic B-04 ledger transaction with the achievement key. B-11 stores the reward record and the ledger reference; it does not store a balance.

**WEP-169 — Caps.** *Approved.* Every effect class declares a cap per instance, per nation and per window. A cap is published and enforced before the effect; an over-cap request is rejected, not truncated silently.

**WEP-170 — Duration.** *Approved.* An effect that lasts beyond the instance declares its duration in turns or named boundaries and its expiry. A permanent effect is a reward or an honour, not an event effect.

**WEP-171 — Stacking.** *Approved.* Two effects of the same class on the same object do not stack unless the definition publishes a stacking rule and a combined cap. One achievement key produces at most one grant.

**WEP-172 — Reversal.** *Approved.* A material effect is reversed only by B-04's correction path with an appended ledger event and a disclosed reason. B-11 never silently reverses a grant. A non-material record is corrected under WEP-038.

**WEP-173 — Expiry of effects.** *Approved.* A timed effect expires at its declared boundary. Expiry restores the prior published input; it does not delete the historical record that the effect occurred.

**WEP-174 — Audit.** *Approved.* Every effect writes `WPA-09` `EVENT_EFFECT_APPLIED` with the instance, class, target, before/after reference, cap and reward key.

**WEP-175 — Privacy.** *Approved.* An effect record exposes only the target's public or owner-visible fields. Aggregate effects obey `k = 5`. No effect record exposes a private balance or an exact military value.

**WEP-176 — No hidden permanent bonus.** *Approved (ECN-113, URB-101).* No event may grant a permanent yield multiplier, compounding percentage, permanent capacity, free city, free facility, free technology or permanent military modifier. Such an effect is invalid regardless of how it is labelled.

**WEP-177 — No destructive effect.** *Approved (URB-035, URB-040).* No event may damage, destroy, capture, transfer or delete a city, facility or population, reduce infrastructure below its floor, or cause a casualty. B-10's `OP-05` is not reusable by B-11.

**WEP-178 — No protection or treaty bypass.** *Approved (REQ-063, NET-025…NET-029, DP-T01, ALL-206/ALL-209).* An event effect that targets another nation MUST pass the same cumulative attack-prevention and consent checks as a direct action. A blocked effect moves nothing.

**WEP-179 — Effect catalogue is closed.** *Approved.* The effect catalogue is exactly §6.7 plus the registered reward classes in §11. A new effect class requires a new decision and a register row.

**WEP-180 — Inertness statement.** *Approved (`11A-DR-033`).* Every definition MUST state what it does **not** grant. A definition without an inertness statement is incomplete and fails `WPF-17`.

### 6.8 Completion, expiry and teardown

**WEP-181 — Completion condition.** *Approved.* A completion condition is a deterministic predicate over authoritative state and instance records. It MUST be evaluable at the completion boundary without player input.

**WEP-182 — Completion verification.** *Approved.* At `CLOSED`, B-11 re-reads the authoritative source, checks the fingerprint, applies the duplicate key and verifies the condition. A completion without a verified source fails with `WPF-18` and returns to `CLOSED` pending correction; it is not marked complete.

**WEP-183 — Partial completion.** *Approved (`11A-BM-062`).* A definition MAY define tiers with partial credit. A tier award is keyed separately and does not block a later tier. Partial credit is recorded, not rounded up to completion.

**WEP-184 — Success and failure.** *Approved.* Success is the verified completion condition. Failure is expiry without completion. Failure is not a penalty and grants no negative effect.

**WEP-185 — Two-stage teardown.** *Approved (D-146, `11A-DR-004`).* Stage 1 is the closing boundary (`ACTIVE → CLOSED`). Stage 2 is the cleanup boundary, later than stage 1 and published. Between them, accepted in-flight actions may resolve; no new participation is accepted. At stage 2 the instance becomes `COMPLETED` or `EXPIRED` and the residual artefacts are cleaned.

**WEP-186 — Teardown preserves earned value.** *Approved.* Teardown removes open offers, unclaimed non-entitlement artefacts and temporary locks. It does not remove a verified progress record, an earned honour, a granted reward or a deferred claim.

**WEP-187 — Event interruption.** *Approved (TR-043).* If a turn is interrupted during W1, recovery resumes from the last completed W-step checkpoint. Completed instance transitions are not repeated; an interrupted transition is re-evaluated idempotently.

**WEP-188 — Duplicate completion.** *Approved.* A second completion attempt on the same instance and key returns the existing result and writes `WPA-28`. It does not re-grant.

**WEP-189 — Voiding.** *Approved.* An instance may be `VOIDED` only with a recorded reason and a correction record. Already-granted valid rewards stand; future grants stop. A voided instance is not replayed as a new occurrence with the same key.

**WEP-190 — Cancellation before start.** *Approved.* A cancelled instance never activated. It writes a cancellation record and no participant record. A repeated cancellation request is idempotent.

**WEP-191 — Unavailable reward.** *Approved.* If a reward cannot be granted at completion (for example, a B-04 rejection), the instance is `COMPLETED` with a **deferred reward** record; the entitlement is held under §11.4. The event is never re-run to obtain the reward.

**WEP-192 — Expiry is not forfeiture.** *Approved (D-028).* Expiry ends participation and grants nothing further. A deferred claim created before expiry remains valid and claimable.

### 6.9 Historical event records

**WEP-193 — Event history is class P.** *Approved (TR-090).* Every event instance that reached `ANNOUNCED` or later writes a permanent, append-only class-P record. Pre-announcement cancellations write an operational audit record only.

**WEP-194 — Record content.** *Approved.* The record contains: instance ID; definition ID and version; class, scope and trigger; occurrence key; start, closing and teardown boundaries; participant set (public or aggregate); result; winners or qualifiers (public data only); awards; the turn's seed reference; and the chronicle reference.

**WEP-195 — Winner and award attribution.** *Approved.* A winner or award holder is recorded by nation ID and public name at the time of grant. A later rename does not rewrite the record; the current name may be displayed through B-03's identity rules.

**WEP-196 — Definition version is preserved.** *Approved.* The record states the pinned definition version. A later version does not alter the recorded outcome.

**WEP-197 — Corrections.** *Approved (TR-091).* A correction appends a new record referencing the original, states the reason and the correcting authority, and preserves the original. The original is marked `corrected_by`, never deleted.

**WEP-198 — Redaction.** *Approved (D-027, Prompt 12).* A record may be redacted only for a privacy or legal reason, only by the authorized path, and only with a disclosed redaction record. Redaction does not change the underlying grant or standing at the time.

**WEP-199 — Privacy of history.** *Approved.* A public event record exposes only public fields. A private participant detail remains owner-visible. An Alliance record aggregates at `k ≥ 5`.

**WEP-200 — No silent rewrite.** *Approved (REQ-093).* No administrator, player, alliance officer or automated job may rewrite, re-rank or delete a published event result. A correction is always a new record.

**WEP-201 — Event history survives seasons.** *Approved (D-149).* A season rollover never deletes an event record. Seasonal standings reset; the event record does not.

**WEP-202 — Event history survives reroll.** *Approved (RRL-019).* A reroll removes the retired nation from current participation; the historical record remains attributed to the retired identity and is not transferred to the replacement.

## 7. Domain B — Objectives and Challenges

### 7.1 Objective categories

**WEP-203 — Category catalogue is closed.** *Approved (D-147).* B-11 defines exactly twelve objective categories. A thirteenth requires a new decision and a register row. Categories are labels on definitions; they are not difficulty tiers and not scores.

**WEP-204 — `OBJ-FOLLOW` onboarding follow-up.** *Approved (D-147).* Optional goals offered after B-03's ten-step journey. They MUST NOT gate the journey, replace it, require alliance membership or grant a first-time economic reward. B-03 owns the journey; B-11 extends it.

**WEP-205 — `OBJ-ECON` economic.** *Approved.* Goals over B-04 state: sustained output, production-mix balance, reserve depth, recovery from a shortfall, treasury discipline. The objective reads published B-04 facts. It MUST NOT reward wealth accumulation as a purchased score and MUST NOT reveal private balances.

**WEP-206 — `OBJ-DEV` development.** *Approved.* Goals over B-05 state: cities founded, infrastructure levels, facility types, technology completions, capstone programmes. This is the strongest lawful class because the state is permanent and the condition is unambiguous.

**WEP-207 — `OBJ-CIV` civic and political.** *Approved (DMP-051, DMP-042).* Goals over **institutional continuity**, not approval: holding an election to term, completing a crisis cycle, maintaining a policy line for a declared period, completing an institutional step. Approval, welfare and legitimacy are never objective targets.

**WEP-208 — `OBJ-POP` population and housing.** *Approved.* Goals over housing sufficiency and capacity, not a headcount race. A "grow population" wording is invalid; a "house the current population" wording is valid. No objective may require eviction or a population loss.

**WEP-209 — `OBJ-TRADE` trade.** *Approved with a publication block.* Goals over trade relationships and settlement behaviour MAY be specified. Any publication, standing input or statistic derived from them MUST remain blocked while a Global Trade gate is unmet (WEP-062). The objective's state may still be tracked privately for the owner's own progress; no public leaderboard, no world comparison, no volume target.

**WEP-210 — `OBJ-DIP` diplomatic.** *Approved, positive-only.* Goals over published diplomatic facts: an agreement concluded, a consultation notice issued, a mediation completed, a peaceful settlement concluded. A condition that requires breach, violation, embargo or aggression is invalid.

**WEP-211 — `OBJ-DEF` defensive.** *Approved (`11A-DR-015`).* Goals over defensive outcomes, readiness maintenance through published bands, and repelled actions. A goal MUST NOT reward suffering losses, being attacked, or refusing to defend. Where readiness cannot be evidenced without exposing a value, the objective is expressed as a band or a count, never an exact force value.

**WEP-212 — `OBJ-ALL` alliance.** *Approved, honour-only.* Goals over collective, aggregated activity at `k ≥ 5`. Every `OBJ-ALL` objective MUST have an individual equivalent (WEP-215). It MUST NOT require membership, expose a member's private value, create a command role or fund a prize.

**WEP-213 — `OBJ-EVENT` world-event.** *Approved.* Goals tied to a specific event class or instance: participation, completion, tier reach, defensive contribution. The objective expires with its event or at the declared teardown boundary. An event objective is not a second event.

**WEP-214 — `OBJ-SEASON` seasonal.** *Approved.* Goals whose progress is scoped to one season. Progress resets at the season boundary by design; the record of completion persists. A seasonal objective MUST declare its season ID and its reset rule.

**WEP-215 — `OBJ-LONG` long-term national.** *Approved.* Multi-step, chain-shaped goals with no short deadline, typically a capstone or a multi-city development path. They are the peaceful long game. They MUST be completable by one nation without a group.

**WEP-216 — Rejected categories.** *Approved (`11A §13.1`).* B-11 rejects (a) offensive military action as an objective, (b) community participation requiring chat, upload or an external channel, (c) historical achievement expressed as a task, and (d) any objective that requires alliance membership. Rejection is recorded in §23.

**WEP-217 — Category does not imply difficulty.** *Approved.* A category states subject-matter, not difficulty. A civic objective may be introductory or long-term; a development objective may be either. Difficulty is a separate label (WEP-273).

**WEP-218 — Peaceful paths remain meaningful.** *Approved (AP-004, AP-005).* Every category MUST be completable without warfare, without a group, without spending real money and without being online at a particular time. The validator checks that each category has at least one individual, non-hostile definition.

**WEP-219 — No category dominance by construction.** *Approved (AP-005).* No category may have a reward class that another category cannot reach, and no category may be an entry gate for another. A cross-category entry fee is invalid. The balance audit belongs to Prompt 14.

### 7.2 Objective definition

**WEP-220 — Definition fields.** *Approved.* Every national-objective definition MUST declare: objective ID; version; category; title; player-facing description; purpose; eligibility conditions; activation conditions; progress source; measurement method; target condition; completion rule; time limit (if any); tier set (if any); repeat policy; reward set; expiry policy; cancellation policy; historical handling; visibility; scope (nation or account); difficulty label; inertness statement; and a mechanic-reference ID.

**WEP-221 — Stable identity.** *Approved.* A definition ID is stable across versions. A new version supersedes the old for future instances; it does not rewrite an instance already accepted. An instance pins its definition version.

**WEP-222 — Progress source must be owned state.** *Approved (`11A-CR-010`).* The progress source MUST be a named field or record owned by B-03…B-10 or by B-11. It MUST NOT be a screen path, a client event, a free-text claim or an inferred behaviour. The definition states the exact source ID.

**WEP-223 — Measurement method.** *Approved.* The method is a formula reference (`F-WEP-…`) or a declared deterministic lookup. It states the window, the aggregation, the unit and the rounding.

**WEP-224 — Target condition.** *Approved.* The target is a boolean predicate over the measured value, a threshold, or a set of conditions joined by a published operator. It MUST be evaluable from the declared source alone.

**WEP-225 — Completion rule.** *Approved.* Completion is once per instance key, subject to the tier and repeat rules. The rule states whether completion requires a player claim or is auto-verified. A discretionary reward still requires a claim (WEP-370).

**WEP-226 — Time limit.** *Approved.* A time limit is expressed in turns or a named boundary. A definition with a wall-clock deadline is invalid. The limit starts at the acceptance boundary, not at the definition's publication.

**WEP-227 — Historical handling.** *Approved.* The definition states whether completion writes a milestone, an achievement, a chronicle entry, a standing input or none. A definition may emit several recognition objects from one completion, each with its own key (`11A-DR-014`).

**WEP-228 — Visibility.** *Approved.* The definition states the visibility of the offer, the progress and the completion: owner-only, participants, alliance, or public. A private objective's progress is never exposed in a public standing.

**WEP-229 — Inertness statement.** *Approved.* The definition states what completion does **not** grant. It MUST state that no OP, permanent yield, city, facility, technology, political state, protection or ranking weight is granted unless the definition cites a separately authorized rule.

**WEP-230 — Definition states.** *Approved.* A definition is `OBJ_DRAFT` → `OBJ_PUBLISHED` → `OBJ_RETIRED`; a published version becomes `OBJ_SUPERSEDED` when a later version is published. Only `OBJ_PUBLISHED` may be offered.

**WEP-231 — Mechanic-change review.** *Approved (`11A-RK-024`).* Every definition carries the ID of the mechanic it references. When that mechanic changes, the definition MUST be reviewed and either re-validated, re-versioned or retired. A stale definition that references a removed field is `SUPERSEDED`, not silently kept.

### 7.3 Objective lifecycle

**WEP-232 — Instance states.** *Approved.* An objective instance is in exactly one state: `AVAILABLE`, `DISMISSED`, `ACCEPTED`, `IN_PROGRESS`, `TIER_REACHED`, `COMPLETED_PENDING_VALIDATION`, `VERIFIED`, `REWARD_PENDING`, `DEFERRED`, `CLAIMED`, `EXPIRED`, `WITHDRAWN` or `SUPERSEDED`.

**WEP-233 — `AVAILABLE`.** *Approved.* The definition is published, the nation is eligible and the outstanding-set cap is not exceeded. The offer is visible; no commitment exists.

**WEP-234 — `DISMISSED`.** *Approved (`11A-DR-009`).* The player declined the offer. Dismissal is not failure, forfeits nothing, does not lower a standing and does not consume the outstanding cap permanently. A dismissed definition MAY be re-offered after a published interval.

**WEP-235 — `ACCEPTED`.** *Approved.* The player explicitly accepted. The acceptance record states the turn, definition version and terms. The time limit and progress clock start here.

**WEP-236 — `IN_PROGRESS`.** *Approved.* Progress is being recorded from the authoritative source. A definition with no progress source stays `ACCEPTED` until its first qualifying event.

**WEP-237 — `TIER_REACHED`.** *Approved (`11A-BM-062`).* A partial tier is satisfied. The tier award is keyed and recorded; the instance may continue toward a higher tier. `TIER_REACHED` returns to `IN_PROGRESS` when further progress is possible.

**WEP-238 — `COMPLETED_PENDING_VALIDATION`.** *Approved.* The target predicate is true but verification has not finished. No reward is granted and no standing input is published in this state.

**WEP-239 — `VERIFIED`.** *Approved.* The source, key, window and duplicate checks passed. The completion and its recognition objects are final.

**WEP-240 — `REWARD_PENDING`.** *Approved.* A reward is due but the claim or the grant has not completed. A material reward remains in this state until claimed; it never expires through absence.

**WEP-241 — `DEFERRED`.** *Approved (`11A-RK-028`).* The entitlement exists but a state blocks collection (for example, a temporary hold or a B-04 correction). Deferral preserves the entitlement, grants nothing early and re-checks at every boundary.

**WEP-242 — `CLAIMED`.** *Approved.* The reward was granted and ledgered. A non-material objective may move directly from `VERIFIED` to `CLAIMED` (or to an archived terminal record) without a reward.

**WEP-243 — `EXPIRED`.** *Approved.* The declared window ended before completion. Progress records remain as history; no penalty is applied; a completed-but-deferred reward is never expired.

**WEP-244 — `WITHDRAWN`.** *Approved.* The system cancelled the objective because the source was retired, the definition was superseded, an event was cancelled, or an invalidity was found. A withdrawal is recorded with a reason; earned tiers remain records; a material reward already earned remains claimable.

**WEP-245 — `SUPERSEDED`.** *Approved (`11A-RK-024`).* The referenced mechanic changed and the definition was replaced. The instance ends with a record; it is not silently continued under old semantics. A player may be offered the replacement.

**WEP-246 — `FAILED` is not a state.** *Approved.* Failure is either expiry, withdrawal or an invalid verification that returns the instance to `IN_PROGRESS`. A separate `FAILED` state would imply a penalty that B-11 does not impose.

**WEP-247 — No state returns to an earlier state.** *Approved.* Except `TIER_REACHED → IN_PROGRESS`, `DEFERRED → REWARD_PENDING`, and `DISMISSED → AVAILABLE` under a new offer, no transition returns to an earlier state. A terminal state never reopens.

**WEP-248 — Transition initiator.** *Approved.* The player initiates acceptance, dismissal, withdrawal-before-freeze and claim. The system initiates progress, tier, verification, deferral, expiry, withdrawal and supersession. A system transition is never a player consent.

**WEP-249 — Transition validation.** *Approved.* Every transition re-checks eligibility, the definition version, the outstanding cap, the time limit and the duplicate key. A failed transition changes no state.

**WEP-250 — Transition record.** *Approved.* Every transition writes one `WPA-` event inside the transaction, with the from-state, to-state, reason and key.

**WEP-251 — Invalid transitions.** *Approved.* `AVAILABLE → IN_PROGRESS`, `DISMISSED → ACCEPTED`, `EXPIRED → ACCEPTED`, `CLAIMED → IN_PROGRESS`, `WITHDRAWN → ACCEPTED` and `SUPERSEDED → IN_PROGRESS` are invalid and fail with `WPF-19`.

**WEP-252 — Concurrent transitions.** *Approved (TR-050).* A player acceptance and a system expiry in the same turn are ordered by the published P6 order: the system expiry is evaluated at W2 before the next acceptance window opens. The later acceptance fails with `WPF-20` and the player is told the objective closed.

**WEP-253 — Acknowledgement is not acceptance.** *Approved.* Viewing an offer, receiving a digest line or opening a notification does not transition `AVAILABLE`. Only an explicit acceptance action does.

### 7.4 Assignment, acceptance and auto-tracking

**WEP-254 — Offer sets.** *Approved.* The eligible definitions are offered as a bounded set. The outstanding set cap is published and enforced before offering. The player chooses which to accept; the system does not choose for the player.

**WEP-255 — Optional by default.** *Approved (D-147).* Except for B-03's onboarding journey, no objective is mandatory. Ignoring an offer is a valid play; it never blocks another objective or a basic action.

**WEP-256 — Explicit acceptance.** *Approved (`11A-DR-009`).* A discretionary objective requires an explicit acceptance. The acceptance terms include the time limit, the reward class and the cancellation rule.

**WEP-257 — Auto-tracked recognition.** *Approved.* A **recognition-only** objective (a milestone or achievement whose completion writes a record and grants nothing discretionary) MAY be tracked automatically from owning state. Auto-tracking is not auto-acceptance: it creates no commitment, spends nothing and requires no action. If the recognition carries a material reward, the reward is claimed explicitly.

**WEP-258 — Auto-tracked eligibility.** *Approved.* An auto-tracked recognition MAY start accounting from the nation's first completed boundary or from the definition's publication boundary, whichever is later. It MUST NOT count pre-nation or pre-publication activity.

**WEP-259 — Time-limited event objectives.** *Approved.* An event-linked objective is available only during its event and expires at the teardown boundary. The event's cancellation withdraws the objective without penalty (WEP-244).

**WEP-260 — Long-term goals.** *Approved.* A long-term objective may remain open indefinitely. It has no expiry unless the definition declares one. A season does not expire a non-seasonal long-term objective.

**WEP-261 — Collective objectives need an individual equivalent.** *Approved (AP-004, `11A-CR-009`).* Every `OBJ-ALL` definition MUST declare an individual equivalent with the same recognition class. The equivalent MUST NOT require membership. The validator checks the pairing.

**WEP-262 — Membership is never a requirement.** *Approved.* No objective may require joining an alliance, a group, a region or any player-created association. A collective objective is an optional layer over individual progress.

**WEP-263 — Acceptance cannot be inferred.** *Approved.* A default, a silence, a timeout, a digest delivery or a prior participation never accepts an objective. A claim of acceptance requires the recorded player action.

**WEP-264 — Re-offer policy.** *Approved.* A dismissed or expired objective may be re-offered after a published interval if the definition permits it. Re-offer does not restore old progress; a new instance with a new key starts.

### 7.5 Objective progress

**WEP-265 — Progress record.** *Approved.* Progress is stored as an append-only record keyed by `(objective_instance_id, tier_id, source_event_key)`. Each record states the source subsystem, source event ID, delta or value, turn, fingerprint and contributing quantity.

**WEP-266 — Authoritative source event.** *Approved.* A progress increment requires an authoritative source event from the owning subsystem — a B-04 ledger event, a B-05 completion record, a B-06 settlement record, a B-08 agreement record, a B-10 campaign record, or a B-11 event completion record. A user-submitted value is never authoritative.

**WEP-267 — Incremental progress.** *Approved.* An incremental measure adds the delta of each qualifying source event. The definition declares whether a delta is a quantity, a count or a boolean.

**WEP-268 — Aggregate progress.** *Approved.* An aggregate measure recomputes from the owning subsystem's current value plus the accepted baseline. It MUST NOT double-count an incremental event already counted.

**WEP-269 — Threshold progress.** *Approved.* A threshold measure compares a current owned value with a target. Crossing the threshold once records completion; re-crossing does not re-complete.

**WEP-270 — Multi-condition progress.** *Approved.* A multi-condition objective records each condition separately and completes only when all are satisfied under the published operator. A partial tier may be awarded for a subset if the definition declares it.

**WEP-271 — Multiple qualifying events.** *Approved.* Several source events may contribute to one instance. Each has its own key; the instance total is the sum or the published aggregation. The definition states the cap on contributing events.

**WEP-272 — Duplicate events.** *Approved.* The source event key is unique per instance. A duplicate source event is rejected with `WPF-21` and adds nothing.

**WEP-273 — Replayed events.** *Approved.* A replay of a turn re-reads the same source keys. Existing progress is not incremented again; the replay writes an idempotency record.

**WEP-274 — Reversed transactions.** *Approved.* If a source transaction is reversed before verification, its contribution is removed by an appended negative progress record; the original record is preserved. If it is reversed after verification, the completion and record stand, and a correction record is appended; a material reward is recovered only through Prompt 12's invalid-grant path.

**WEP-275 — Corrected source data.** *Approved.* A source correction appends an adjustment record referencing the original. It never edits the progress record in place. A correction that changes a verified completion is recorded as a correction, not a silent recalculation.

**WEP-276 — Objective expiry during progress.** *Approved.* Progress already recorded remains history. A late source event that arrives after expiry does not reopen the instance; it is recorded as unapplied.

**WEP-277 — Concurrent progress events.** *Approved.* Multiple source events in one turn are processed in the published P6 order and by source event key. There is no last-writer-wins; each key contributes once.

**WEP-278 — No progress before acceptance.** *Approved.* A player-accepted objective counts only source events at or after the acceptance boundary. An auto-tracked recognition counts from WEP-258's start boundary. Retrofitting pre-acceptance activity is prohibited.

**WEP-279 — Progress is monotonic within a tier.** *Approved.* Except for a recorded source reversal (WEP-274), progress does not decrease. A displayed decrease must cite a reversal record.

**WEP-280 — Private progress.** *Approved.* An owner-only objective's progress is visible only to the nation owner. A public representative may show completion, never a private intermediate value, unless the definition declares the progress public.

### 7.6 Progress verification

**WEP-281 — Verification timing.** *Approved.* Verification runs in P6 W2 after progress recording and before the standing snapshot. A completion discovered after W3 is verified in the next turn's W2; the completion turn is the turn of verification, not the turn of the underlying event.

**WEP-282 — Evidence source.** *Approved.* The evidence is the authoritative source record plus the fingerprint. B-11 does not accept a screenshot, a player statement, a client-side event or an external log.

**WEP-283 — Duplicate prevention.** *Approved.* The instance key, the source event key and the achievement key are all checked. Any collision returns the original result.

**WEP-284 — Transaction consistency.** *Approved.* The progress record, the completion record and the recognition record are written in one transaction. A failure leaves none of them.

**WEP-285 — Invalid completion.** *Approved.* If verification fails, the instance returns to `IN_PROGRESS`; no reward is granted; a `WPF-22` record explains why. The player is not penalized for a system-side invalidity.

**WEP-286 — Retroactive progress.** *Approved (D-021).* No catch-up acceleration and no retroactive credit for a period before acceptance or publication. A correction may adjust a counted event, but it may not add a period the definition did not cover.

**WEP-287 — Historical correction.** *Approved.* A correction to a historical completion appends a correction record and preserves the original. It does not re-run the reward unless Prompt 12 invalidates the grant.

**WEP-288 — Fraudulent progress.** *Approved (Prompt 12 owns enforcement).* B-11 may set `DEFERRED` or withhold a reward pending review when the registered evidence path identifies a suspected invalid source. B-11 does not ban, suspend or penalize; Prompt 12 does.

**WEP-289 — Replay prevention.** *Approved.* A replayed verification with the same key is a no-op. A replayed completion cannot mint a second achievement or reward.

**WEP-290 — Verification owner.** *Approved.* B-11 owns objective verification. The source subsystem owns the fact being verified. A disagreement resolves in favour of the source fact and is recorded as a conflict.

### 7.7 Objective difficulty

**WEP-291 — Difficulty labels.** *Approved.* The labels are `INTRODUCTORY`, `STANDARD`, `ADVANCED`, `LONG_TERM`, `COMPETITIVE` and `SEASONAL`. They are descriptive categories, not numeric tiers and not a score.

**WEP-292 — Difficulty reflects effort, not attendance.** *Approved (`11A-DR-029`).* Difficulty is assessed from the scale of state change, the number of independent conditions and the length of the horizon. Time spent online, login count and action frequency are not difficulty inputs.

**WEP-293 — Military difficulty is not general difficulty.** *Approved.* A military-flavoured condition does not make an objective "advanced" by itself. A peaceful long-term objective may be `LONG_TERM` or `ADVANCED`.

**WEP-294 — Difficulty does not change reward eligibility.** *Approved.* A higher difficulty may carry a different recognition class, but it never gates a basic reward, another objective or a standing. Difficulty is not a multiplier unless a formula in §22 declares it and Prompt 14 calibrates the coefficient.

**WEP-295 — Difficulty is published.** *Approved.* The label is visible on the offer so a player can choose. A hidden difficulty label is a defect.

**WEP-296 — No difficulty inflation.** *Approved.* A definition's difficulty label may change only with a new version. Relabelling an existing instance is prohibited.

### 7.8 Repeatable and non-repeatable objectives

**WEP-297 — One-time default.** *Approved.* An objective is one-time unless the definition explicitly declares a repeat policy. One instance, one completion key, one reward key.

**WEP-298 — Repeatable objectives.** *Approved.* A repeatable definition declares the repeat interval, the maximum completions per window, whether progress carries over and whether the reward repeats. The default for all three is "no".

**WEP-299 — Time-gated objectives.** *Approved.* A time gate is a turn interval or a named boundary. A daily reset is permitted only if it creates no obligation and no loss; a missed day grants nothing and forfeits nothing.

**WEP-300 — Seasonal objectives.** *Approved.* A seasonal objective's progress resets at the season boundary. The completion record persists. The reward may repeat per season only if the definition declares it and the material class is separately authorized.

**WEP-301 — Progress carryover.** *Approved.* Progress does not carry from one instance to another. A re-offered or re-created instance starts at zero. A source event counted in an earlier instance is not counted again.

**WEP-302 — Duplicate awards.** *Approved.* A repeatable objective uses a per-completion key that includes the completion ordinal. Two completions may produce two recognised awards only if the definition declares a repeatable recognition class. A material reward repeats only under WEP-404.

**WEP-303 — Repeat-completion limits.** *Approved.* The repeat cap is published per window. An over-cap completion is not credited and is not silently converted into another reward.

**WEP-304 — Recreated transaction is not repeatability.** *Approved.* A player who repeats the underlying transaction after a one-time objective is complete gains nothing. The objective key is exhausted; the transaction is ordinary play.

**WEP-305 — Template version changes.** *Approved.* A new definition version may change the repeat policy for future instances only. It does not reopen completed instances or reset a player's exhausted one-time key.

### 7.9 Failure, cancellation and correction

**WEP-306 — Expiry.** *Approved.* Expiry is the end of the declared window. It is recorded, never punished. Progress remains history.

**WEP-307 — Voluntary abandonment.** *Approved.* A player may abandon an accepted objective before completion. Abandonment is recorded as a withdrawal by the player, not a failure; it forfeits no existing record and no earned tier.

**WEP-308 — Ineligibility.** *Approved.* If the nation becomes ineligible (for example, dormancy or a Prompt 12 hold), the objective is suspended or deferred, not failed. On restoration the instance resumes under the current definition version; if the definition was superseded, WEP-245 applies.

**WEP-309 — Source-system correction.** *Approved.* A correction to a source value adjusts progress through an appended record. A verified completion is corrected, not erased.

**WEP-310 — Event cancellation.** *Approved.* Cancelling the linked event withdraws the objective with a reason. Earned tiers and verified completions remain. A material reward already earned remains claimable.

**WEP-311 — Technical interruption.** *Approved (TR-043).* An interrupted turn resumes from the last W2 checkpoint. A progress record written before the interruption is not repeated.

**WEP-312 — Invalid source data.** *Approved.* If the source is missing, stale or inconsistent, the objective fails closed for that turn: no progress, no completion, a `WPF-23` record. The player is told the system could not verify, not that the player failed.

**WEP-313 — Duplicate completion.** *Approved.* A duplicate completion returns the original result and writes `WPA-28`. It does not re-award.

**WEP-314 — Exploit invalidation.** *Approved (Prompt 12).* A completion obtained through a prohibited behaviour may be invalidated by Prompt 12 with evidence. B-11 records the invalidation and appends a correction; it does not impose a punishment.

**WEP-315 — No punishment for system failure.** *Approved (TR-056, D-028).* A system-side cancellation, a technical failure or an owning-subsystem correction must not reduce a player's honour, standing or record. The remedy is a correction or a re-offer, never a penalty.

**WEP-316 — Failure visibility.** *Approved (REQ-094).* A failure message states what happened, which rule applied, what did not change and what the player may do next. It contains no private data and no enumeration risk.

---

## 8. Domain C — Rankings and Competitive Recognition

### 8.1 Four separated layers

**WEP-317 — Layer model.** *Approved (D-148).* Domain C has four separated layers: (1) plural windowed **domain standings**; (2) one separate published **World Standing Eligibility (WSE)**; (3) a **descriptive median-relative national profile** that rewards nothing; and (4) the permanent **record-and-honour layer** owned jointly with Domain D. No layer may absorb another.

**WEP-318 — Layer 1 — domain standings.** *Approved.* Each standing is a published comparison over a declared window, with its own inputs, snapshot and tie rule. A nation may be notable in several.

**WEP-319 — Layer 2 — WSE.** *Approved.* WSE answers whether a nation may appear in a competitive standing. It is a status, not a rank, and it grants no reward. It is defined in §8.6.

**WEP-320 — Layer 3 — descriptive profile.** *Approved (`11A-DR-027`).* The descriptive profile compares a nation with the world distribution — median-relative, no rank, no reward, no eligibility consequence. It is built only from already-public values.

**WEP-321 — Layer 4 — record and honour.** *Approved.* Achievements, milestones, honours and the chronicle are permanent and non-comparative. They are specified in Domain D and are never inputs to a standing unless the standing's definition explicitly cites a public count.

**WEP-322 — No single dominant ladder.** *Approved (AP-005, `11A-CR-014`).* No single measure may simultaneously be a rank, an eligibility gate and a reward key. A measure used in one role MUST NOT be reused in another without a new decision.

**WEP-323 — Separation is structural.** *Approved.* A balance change to one standing's inputs cannot change WSE, another standing's inputs or a permanent honour. This is the failure Politics & War demonstrated when one score coupled balance to fairness (`11A-BM-001`).

**WEP-324 — Standings are published as comparisons.** *Approved.* A standing displays a rank, a percentile and the denominator population and window. A display without a denominator is a defect (`11A-CR-015`).

**WEP-325 — No live standing.** *Approved (TR-041).* A standing is computed at the P6 snapshot and published at P7. A live-updating public rank is prohibited because it maximises manipulation surface and cost.

### 8.2 Standing categories

**WEP-326 — Standing catalogue is closed.** *Approved (D-156).* B-11 defines exactly ten standings: `ST-DEV`, `ST-ECO`, `ST-RES`, `ST-HOU`, `ST-CIV`, `ST-DIP`, `ST-MIL`, `ST-DEF`, `ST-ALL` and `ST-SEA`. A new standing requires a decision and a register row.

**WEP-327 — `ST-DEV` national development.** *Approved.* Competitive. Inputs: city count, total infrastructure, facility count and class, completed technologies, completed capstones. Purpose: recognise durable national construction. It is the strongest lawful competitive standing.

**WEP-328 — `ST-ECO` economic output.** *Approved.* Competitive. Inputs: published production output valued at B-04 reference prices over the window; capacity utilisation. National wealth MAY be displayed as a labelled estimate but MUST NOT be the metric. Private balances are never exposed.

**WEP-329 — `ST-RES` economic resilience.** *Approved.* Competitive. Inputs: the count of shortfall, austerity or unfilled-obligation turns in the window, and reserve depth expressed as a band. Purpose: recognise stability, not size.

**WEP-330 — `ST-HOU` housing and population.** *Approved.* Statistical standing. Inputs: population, effective housing, housing sufficiency, capacity utilisation, all as public statistics. It is displayed as a comparison but carries no seasonal award and no material reward.

**WEP-331 — `ST-CIV` institutional continuity.** *Approved (D-156, resolves `11A-OPEN-007`).* Competitive. Inputs: elections completed to term, crisis cycles survived, policy lines held for the declared period, institutional steps completed. It MUST NOT use approval, welfare, legitimacy or any "governance quality" score. The measure counts published institutional facts.

**WEP-332 — `ST-DIP` diplomatic activity.** *Approved (D-156, DIP-084, DIP-088).* Recognition standing. Inputs: counts of published facts — agreements concluded, consultations honoured, peaceful settlements concluded, distinct active partners. It is not a reputation score and has no mechanical effect.

**WEP-333 — `ST-MIL` military participation.** *Approved (D-156, WAR-162).* Recognition standing. Inputs: campaigns participated, operations executed, defensive engagements, all as counts or published bands. No exact readiness, force, inventory, casualty or destruction value may appear.

**WEP-334 — `ST-DEF` defensive performance.** *Approved (`11A-DR-015`).* Recognition standing. Inputs: repelled defensive engagements and defensive outcomes, expressed in bands. It MUST NOT reward suffered losses, non-defence or manufactured victimhood.

**WEP-335 — `ST-ALL` Alliance collective.** *Approved (D-160, D-027, ALL-156, ALL-224).* Honour-only aggregate standing. Inputs: aggregated member development and participation counts, published only at `k ≥ 5`. It never lists a member value, never funds a prize and never creates a command role.

**WEP-336 — `ST-SEA` seasonal aggregate.** *Approved.* Competitive seasonal standing. Inputs: seasonal objective points and seasonal event completions, scoped to the season ID. It resets at the season boundary.

**WEP-337 — No duplicate metric standings.** *Approved.* Two standings MUST NOT use the same metric with different labels. If a new purpose is genuinely different, it must declare a different input set and a different decision use.

**WEP-338 — Trade standing is specified but blocked.** *Approved.* A trade-derived standing shape MAY exist in the register. Its publication, snapshot and display MUST remain disabled while any Global Trade gate is unmet. It is not one of the ten active standings until the gate passes.

**WEP-339 — Political standing is not approval.** *Approved.* `ST-CIV` is the only political standing. Approval, welfare and legitimacy are never ranked, displayed as a score, used as an achievement currency or made purchasable.

### 8.3 Standing definitions

**WEP-340 — Definition fields.** *Approved.* Every standing MUST declare: standing ID; name; purpose; scope (nation or alliance); eligible entities; metric; authoritative source IDs; formula reference; measurement window; aggregation; normalisation; weighting (if any); exclusions; caps; missing-data rule; rounding; tie rule; snapshot point; update frequency; inactive treatment; protection treatment; privacy treatment; retention and archive behaviour; and an inertness statement.

**WEP-341 — Metric and source.** *Approved.* The metric is a named formula over named owned inputs. A standing may not read a value that the owning subsystem does not publish to B-11's visibility class.

**WEP-342 — Measurement window.** *Approved.* Every competitive standing declares a window in turns. A cumulative all-time total is not a competitive standing; it is a record. The window is the primary anti-incumbency device (`11A-DR-019`).

**WEP-343 — Aggregation.** *Approved.* The aggregation is sum, mean, rate, ratio, maximum or percentile, named explicitly. A rate or ratio states its numerator, denominator and zero-denominator branch.

**WEP-344 — Normalisation.** *Approved.* A standing is normalised against the current eligible population or the current world maximum, as its formula declares. An absolute constant threshold is prohibited for eligibility-critical normalisation.

**WEP-345 — Weights.** *Approved (Prompt 14).* A standing may use weights only when the formula names them as provisional coefficients. No weight is approved by this document. A hidden weight is a defect.

**WEP-346 — Exclusions.** *Approved.* The definition names every exclusion: dormant, retired, protected-from-hostile-only, incomplete-data, manipulation-hold, below-minimum-participation. An exclusion not named is not applied.

**WEP-347 — Caps.** *Approved.* A per-nation cap prevents one extreme value from dominating. A cap is published and applied before normalisation.

**WEP-348 — Missing data.** *Approved.* A nation with incomplete data is `PROVISIONAL` in WSE, not silently zero. A zero would be a false statement about performance.

**WEP-349 — Rounding.** *Approved.* Every standing declares its rounding and display precision. Integer arithmetic is used internally; display precision is a presentation rule and does not change the stored result.

**WEP-350 — Inertness statement.** *Approved.* The definition states what the standing does not grant: no reward, no eligibility, no protection, no event access, no material grant. A standing that gates something is a defect unless the gating is separately authorized.

**WEP-351 — Definition versions.** *Approved.* A standing definition is versioned. A metric change creates a new version and a new snapshot series; the historical series keeps its original definition. A silent metric change is prohibited.

### 8.4 Ranking calculations

**WEP-352 — Every calculation resolves to the register.** *Approved.* Each standing's metric, normalisation, rank assignment and tie resolution MUST cite an `F-WEP-` formula. A standing described only in prose is incomplete and fails the validator.

**WEP-353 — Inputs and units.** *Approved.* Every input declares its unit, valid range and owning subsystem. A unitless or unbounded input is a defect.

**WEP-354 — Source version.** *Approved.* A snapshot records the source version and fingerprint. A later source correction does not alter a sealed snapshot; it creates a correction snapshot.

**WEP-355 — Calculation phase.** *Approved.* All standing calculations run in P6 W3 after W2, against the post-P5 frozen state and the W2 results. No standing reads a value written later in P6.

**WEP-356 — Snapshot timing.** *Approved.* Exactly one authoritative snapshot per standing per turn. A standing that needs a weekly or monthly view derives it from the archived turn snapshots; it does not run a second calculation against live state.

**WEP-357 — Determinism.** *Approved.* The same frozen inputs and seed produce the same order. A tie that depends on insertion order is a defect.

**WEP-358 — No recalculation of published history.** *Approved.* A published snapshot is immutable. Recalculation is a correction with a new snapshot ID and a reference to the original.

**WEP-359 — Denominator disclosure.** *Approved (`11A-CR-015`).* A published percentile states the population, the eligibility set and the window. Two different denominators in one game must not be presented as one figure.

**WEP-360 — Threshold semantics.** *Approved.* A threshold expressed as a share of the normalised pool states the pool and the rounding. A threshold expressed as a count states the count. Mixing them in one standing is prohibited.

**WEP-361 — Composite calculations are prohibited as a headline.** *Approved (WEP-365).* No formula may combine several standings into one published "best nation" number. A descriptive index MAY exist only as a labelled, non-eligibility, non-reward profile under WEP-366.

### 8.5 Composite ranking

**WEP-362 — No overall composite standing.** *Approved (D-148, D-156).* B-11 does **not** publish a single overall national score, "best nation" ladder or composite rank. The design reason is AP-005, the outline's no-single-dominant-ladder rule and the demonstrated P&W coupling failure. Multiple independent standings better serve the twelve player profiles.

**WEP-363 — No composite eligibility gate.** *Approved.* Even if a descriptive composite is displayed, it MUST NOT gate an event, an objective, a reward, protection, diplomacy or a basic action.

**WEP-364 — No hidden composite.** *Approved.* An internal composite used to sort a display is prohibited unless it is published with its components and weights. A "relevance" or "power" sort that ranks nations is a composite by another name.

**WEP-365 — Descriptive profile is not a composite standing.** *Approved.* The median-relative descriptive profile compares individual published values with the world distribution. It has no rank order across nations, no reward and no eligibility consequence. It is a presentation of facts, not a score.

**WEP-366 — Reopening condition.** *Approved.* A composite standing may be reconsidered only with a new decision that states the components, normalisation, missing-data rule, double-counting analysis, transparency and non-eligibility guarantee, and only after Prompt 14 simulates its dominance behaviour.

### 8.6 Ranking eligibility and WSE

**WEP-367 — WSE states.** *Approved (D-156).* World Standing Eligibility has exactly four states: `UNRANKED`, `ELIGIBLE`, `PROVISIONAL`, `EXCLUDED`.

**WEP-368 — `UNRANKED`.** *Approved (NAT-016).* A nation is `UNRANKED` before its first completed boundary. It may play, build and receive informational events; it does not appear in a competitive standing.

**WEP-369 — `ELIGIBLE`.** *Approved.* The nation has completed a boundary, is not dormant, not retired and not under an evidence hold. It appears in every standing for which its data is complete.

**WEP-370 — `PROVISIONAL`.** *Approved.* The nation is eligible but its data is incomplete, a source correction is pending, or a review is open. It appears in a marked provisional form; its position is not used for a competitive award until resolved.

**WEP-371 — `EXCLUDED`.** *Approved.* The nation is dormant, retired, archived, or under a Prompt 12 evidence hold. It is removed from current public standings as a presentation rule and loses nothing. On restoration it returns at the next snapshot.

**WEP-372 — WSE is not a reward key.** *Approved.* WSE never determines a reward, an honour, an event invitation or a material grant. It determines only appearance in a competitive standing.

**WEP-373 — No protection bypass.** *Approved.* A protected nation is `ELIGIBLE` for non-hostile standings. Protection is never a reason to exclude it and never a reason to exempt it from the same rules as others.

**WEP-374 — New-nation treatment.** *Approved.* A new nation is `UNRANKED` until its first boundary, then `ELIGIBLE` if data is complete. It is not given a provisional rank, a handicap or a catch-up (`D-021`).

**WEP-375 — Incomplete data.** *Approved.* A missing input makes the nation `PROVISIONAL` for that standing only. It is not zero-filled and not silently dropped.

**WEP-376 — Status changes.** *Approved.* A nation moving between states is recorded with the reason and the turn. A return from dormancy is immediate at the next snapshot; no decay is applied.

**WEP-377 — Minimum participation.** *Approved (`11A-DR-021`).* A competitive standing may require a minimum participation floor (for example, a completed boundary and a declared window of activity). The floor is published; a nation below it is `UNRANKED` for that standing, not penalized.

**WEP-378 — Entry closure.** *Approved (`11A-DR-021`).* A competitive award may close new entry before the competition closes, provided the closure is published in advance. A silent closure is prohibited.

**WEP-379 — Alliance eligibility.** *Approved.* An Alliance appears in `ST-ALL` only when the aggregate can satisfy `k ≥ 5`. A smaller Alliance is withheld, not zero-ranked.

**WEP-380 — Archived nations.** *Approved (ONB-046, D-028).* An archived nation is removed from current standings. Its historical snapshots remain.

### 8.7 Snapshots

**WEP-381 — One snapshot per standing per turn.** *Approved.* A snapshot is keyed `(turn_id, standing_id)` and is unique. A duplicate snapshot attempt returns the original and writes `WPA-29`.

**WEP-382 — Snapshot content.** *Approved.* A snapshot records: snapshot ID; standing ID and definition version; turn ID; frozen baseline fingerprint; input values by source; computed metric; normalisation denominator; rank order; tie group; excluded set with reasons; rounding; seed reference; and creation audit ID.

**WEP-383 — Snapshot immutability.** *Approved.* Once sealed, a snapshot's inputs and result are immutable. A correction creates a new snapshot with `corrects_snapshot_id` and leaves the original published.

**WEP-384 — Seal and publish.** *Approved.* A snapshot is `SEALED` in P6 W3 and `PUBLISHED` in P7. A sealed but unpublished snapshot is visible only to the system; no player sees a mid-turn rank.

**WEP-385 — Snapshot schedule.** *Approved.* The per-turn snapshot is the source of truth. Weekly, monthly and seasonal views are derived rollups over the archived turn snapshots; they do not read live state.

**WEP-386 — Rollup rules.** *Approved.* A rollup names its window, its aggregation (for example, the last snapshot in the window or the mean percentile), its treatment of missing turns and its rounding. A rollup that changes the underlying order without a published rule is a defect.

**WEP-387 — Data consistency.** *Approved.* All inputs are read from the same frozen baseline. A snapshot that mixes pre-P5 and post-P5 values is invalid.

**WEP-388 — Historical archive.** *Approved (TR-090, TR-092).* Snapshot headers and top-order results are class-P permanent anchors. Full per-turn detail MAY be compacted into monthly summaries under B-02's retention rule; the anchor and the correction record are never deleted.

**WEP-389 — Correction process.** *Approved.* A correction states the faulty input, the corrected input, the reason, the authority and the new result. The original remains visible as corrected. A correction does not rewrite the historical award that was already granted.

**WEP-390 — Duplicate prevention.** *Approved.* The `(turn_id, standing_id)` key prevents a second snapshot. A replay returns the sealed snapshot and writes an idempotency record.

**WEP-391 — Cost boundary.** *Approved (TR-092).* Snapshot and rollup computation is bounded by the archived-snapshot model. No B-11 job may scan full operational history during a turn; compaction is B-02's idempotent daily job.

### 8.8 Tie-breaking

**WEP-392 — Shared rank by default.** *Approved (`11A-DR-025`, `11A-RK-025`).* Equal values receive the same rank. The next rank is the next ordinal (for example, 1, 2, 2, 4), and the tie group is published. A tie is information, not an error.

**WEP-393 — Secondary metric.** *Approved.* Where a standing declares a secondary published metric, it breaks the tie before any other device. The secondary metric is part of the standing definition and is visible.

**WEP-394 — Earlier sustained position.** *Approved.* If a single winner is structurally required and a secondary metric does not resolve it, the nation that first reached the tied value in a **published snapshot** wins. The archive makes this auditable.

**WEP-395 — Seeded selection.** *Approved (TR-044 B2).* If a single winner is still required, a seeded lottery keyed on `(turn_id, allocation_id)` selects one. The odds and the seed reference are published.

**WEP-396 — Prohibited tie-breaks.** *Approved.* Operator identity, account age, insertion order, database row order, hash order, client-supplied order, alliance membership, nation age as merit and any undisclosed value are prohibited.

**WEP-397 — Tie-break is published.** *Approved (TR-049).* The hierarchy is visible in the standing definition and in the player-facing explanation. A player can reproduce why a tie resolved as it did.

**WEP-398 — Award ties.** *Approved.* A seasonal or event award that requires exactly one holder uses WEP-393…WEP-395 in that order. A shared honour is preferred wherever the honour class permits it.

**WEP-399 — No retroactive tie rewrite.** *Approved.* A later tie-break rule does not change a published result. A correction requires a correction record and a stated reason.

### 8.9 Abuse prevention

**WEP-400 — Design controls, not punishments.** *Approved (Prompt 12 boundary).* B-11 defines preventive and evidentiary controls. It does not define suspensions, bans, penalties, appeals or enforcement thresholds; Prompt 12 owns those.

**WEP-401 — Artificial score inflation.** *Approved.* A standing uses windowed rates and published inputs; a last-turn spike followed by a reversal does not create a sustained position. The window and the snapshot point are the primary controls.

**WEP-402 — Trade manipulation.** *Approved.* A trade-derived measure is blocked before the gate. After the gate, a round-trip or circular trade MUST yield zero net progress; the measure is net-of-friction and relationship-based, not raw volume.

**WEP-403 — Circular transfers.** *Approved.* A standing input that can be inflated by moving value between colluding nations is invalid. The definition must name the anti-circular property or the standing is not published.

**WEP-404 — Repeated activity farming.** *Approved.* Cheap repeatable actions are excluded from scored sources. A count-based standing declares which action classes count and caps repeats. Automation cannot earn a reward because no presence reward exists (WEP-056).

**WEP-405 — Multi-account manipulation.** *Approved (D-032, REQ-061, REQ-066).* B-11 reads B-03's one-account and pair states. It never treats co-residence or a shared network as proof; Prompt 12 owns the evidence and the consequence.

**WEP-406 — Alliance collusion.** *Approved.* `ST-ALL` aggregates at `k ≥ 5`, uses no member values and funds no prize. Collusion detection is Prompt 12's; B-11 records the aggregate and the population.

**WEP-407 — Intentional losses.** *Approved.* No standing reads raw losses, casualties or destruction. Defensive recognition reads repelled actions and defensive outcomes, not suffered damage (`11A-RK-006`, `11A-RK-017`).

**WEP-408 — Duplicate events.** *Approved.* A source event counts once per standing window. The source key is deduplicated before aggregation.

**WEP-409 — Fake transactions.** *Approved.* A transaction that is reversed, invalid or self-dealing does not enter a standing. The owning subsystem's validity flag is authoritative.

**WEP-410 — Snapshot-edge play.** *Approved.* A participation freeze applies to any decision a standing determines (WEP-155). A last-turn change that cannot be frozen is not an input.

**WEP-411 — Strategic abandonment.** *Approved (D-028).* A dormant nation is excluded from public standings and loses nothing. Abandonment cannot freeze an unbeatable position in a windowed standing because the nation is not displayed and its window contribution ages out.

**WEP-412 — Evidence handoff.** *Approved.* B-11 records the inputs, fingerprint and population for every snapshot so Prompt 12 can reconstruct a disputed result. It does not itself decide that manipulation occurred.

### 8.10 Historical and seasonal standings

**WEP-413 — Four historical views.** *Approved.* B-11 distinguishes: current standings; monthly rollups; seasonal standings; and all-time records. The first three are comparisons; the fourth is a record, not a competitive rank.

**WEP-414 — Seasonal standing.** *Approved.* A seasonal standing has a season ID, an opening and closing boundary, and a reset scope. It is derived from snapshots within the season.

**WEP-415 — Season reset scope.** *Approved (D-149, `11A-DR-018`).* A season resets seasonal standings and seasonal objective progress only. It never resets national state, permanent records, achievements, honours, the chronicle or attributed history.

**WEP-416 — Archived champion.** *Approved.* The winner of a seasonal standing is recorded as a permanent honour with the season ID, the standing, the date and the final result. The standing resets; the honour does not.

**WEP-417 — Monthly rollup.** *Approved.* A monthly view derives from the turn snapshots in that month. It is a display product, not a new competition, unless a standing definition declares a monthly award; that award follows WEP-398.

**WEP-418 — All-time records.** *Approved.* An all-time record is a permanent record of a published fact (for example, the highest value ever observed). It is not a competitive standing and grants no recurring reward.

**WEP-419 — Retired standing.** *Approved.* A retired standing keeps its historical snapshots and honours. It stops producing new snapshots. It is not deleted and its past results are not re-ranked.

**WEP-420 — No seasonal erasure.** *Approved.* A season boundary never deletes a chronicle entry, an event record, an achievement or a milestone. A rule that would erase them is invalid.

**WEP-421 — No seasonal state reset.** *Approved (FO-024 rejected).* No season resets cities, infrastructure, population, treasury, research, diplomacy, alliance membership or military state.

**WEP-422 — Cross-season comparison.** *Approved.* A cross-season comparison is labelled as a record comparison, not a standing. Different seasons may have different definitions; the definition version is displayed with each archived result.

## 9. Domain D — Long-Term National Progression

### 9.1 Progression layers

**WEP-423 — Layer catalogue.** *Approved (D-149).* B-11 defines eight progression layers: (1) permanent achievements; (2) national milestones; (3) historical records and the chronicle; (4) seasonal achievements; (5) temporary competitive recognition; (6) honour classes; (7) authorship unlocks; and (8) cosmetic recognition. Each has a distinct purpose and persistence.

**WEP-424 — Layer 1 — permanent achievements.** *Approved.* A keyed, binary, dated, nation-scope record of a completed condition. It grants no power. It is the deliberately small optional layer.

**WEP-425 — Layer 2 — national milestones.** *Approved.* A state-derived threshold record. It is not a task and not a reward. It answers "where has this nation reached?".

**WEP-426 — Layer 3 — historical records.** *Approved.* The chronicle and the permanent event, campaign, agreement and standing anchors. This is the spine of long-term identity.

**WEP-427 — Layer 4 — seasonal achievements.** *Approved.* Recognition scoped to a season. The seasonal progress resets; the achievement record persists.

**WEP-428 — Layer 5 — temporary competitive recognition.** *Approved.* A standing held for a window. It is comparative and transient; the record of having held it is permanent.

**WEP-429 — Layer 6 — honour classes.** *Approved.* Categorical labels for permanent recognition. They are not points and not a currency. There is no prestige balance (`ECN-092`).

**WEP-430 — Layer 7 — authorship unlocks.** *Approved (`11A-DR-032`).* Per-session or permanent rights to name, describe or present one's own nation through B-03's existing identity fields. Authorship grants no economic, military or political capability.

**WEP-431 — Layer 8 — cosmetic recognition.** *Approved.* A display-only token with an explicit inertness statement. It grants nothing and is never purchasable.

**WEP-432 — No layer duplication.** *Approved.* A completion may emit several layers at once (`11A-DR-014`), but each layer has one key and one record. The same fact is not stored twice under two layers without a stated purpose.

### 9.2 Permanent achievements

**WEP-433 — Achievement identity.** *Approved (`11A-DR-008`).* An achievement has a definition ID, version, title, description, category, condition reference, evidence source, tier set (if any), scope, honour class (if any), display class and inertness statement.

**WEP-434 — Binary keyed grant.** *Approved.* An achievement is granted once per achievement key. There is no partial achievement; a tiered achievement has one key per tier.

**WEP-435 — Qualification condition.** *Approved.* The condition is a deterministic predicate over authoritative state or a verified event/objective completion. It is not a player claim, a vote, a purchase or an attendance record.

**WEP-436 — Evidence source.** *Approved.* The grant records the source record ID, the fingerprint and the turn. A grant without evidence is invalid.

**WEP-437 — Completion verification.** *Approved.* Verification runs in P6 W4 after the W2 objective results and the W3 snapshot. A grant discovered earlier may be staged; it is not published before P7.

**WEP-438 — One-time or repeatable.** *Approved.* The default is one-time. A repeatable achievement declares a per-window key and a cap. A repeatable achievement never grants a repeatable material reward unless WEP-509 permits it.

**WEP-439 — Display status.** *Approved.* An achievement displays its title, date, scope, tier and completion percentage where the population denominator is published. A hidden achievement exists only while its condition is secret; its grant is still recorded.

**WEP-440 — Historical retention.** *Approved.* A granted achievement is class-P permanent. It survives seasons, dormancy, retirement and reroll as attributed history.

**WEP-441 — Revocation and correction.** *Approved.* A valid grant is corrected or revoked only by Prompt 12's evidence path or by a source correction. The original grant remains in history with `revoked_by` or `corrected_by`. B-11 never deletes it.

**WEP-442 — Privacy.** *Approved.* A public achievement exposes only public fields. A private achievement is owner-visible. An aggregate completion percentage obeys `k = 5`.

**WEP-443 — Scope.** *Approved (WEP-031).* An achievement declares nation or account scope. A nation-scope achievement is forfeited on reroll and retained as history. An account-scope achievement survives only if non-transferable and not re-earnable.

**WEP-444 — No purchasable achievement.** *Approved (WEP-068).* An achievement may not be bought, promoted, gifted or granted for an external benefit. A supporter-only achievement is invalid.

**WEP-445 — Achievement layer size.** *Approved (D-149, `11A-DR-034`).* The achievement set is deliberately small and optional. Long-term motivation is carried primarily by records, standings, honours and authorship. There is no obligation to fill a checklist.

**WEP-446 — Achievement catalogue review.** *Approved.* Each achievement references the mechanic it measures. A mechanic change triggers the same review as WEP-231. An achievement whose condition can no longer be met is retired, not left broken.

### 9.3 National milestones

**WEP-447 — Milestone identity.** *Approved (NAT-052).* A milestone is a state-derived record with a stable ID, a threshold series, a source field, a scope and a display class. It is not a task, not an achievement and not a reward.

**WEP-448 — Milestone areas.** *Approved.* The permitted areas are: national establishment and continuity; economic development; city foundation and development; infrastructure; population and housing; political and institutional continuity; diplomatic records; trade relationships (publication-blocked where applicable); military history; international recognition; Alliance contribution; and event participation.

**WEP-449 — Geometric thresholds with an open tail.** *Approved (`11A-DR-031`).* A milestone series uses a geometric progression `T_n = T_0 × r^n` with an open tail. The structure is fixed; `T_0`, `r` and the display tiers are Prompt 14 parameters. A series never needs a new tier invented to avoid saturation.

**WEP-450 — State-derived only.** *Approved.* A milestone is computed from the owning subsystem's published state. It cannot be claimed, purchased or awarded by a player action that does not change the state.

**WEP-451 — No ranking weight.** *Approved (NAT-052).* A milestone grants no ranking weight, no reward, no resource, no yield, no military capability and no protection. It is a record.

**WEP-452 — Scope.** *Approved.* A milestone declares nation or account scope. A nation-scope milestone is forfeited on reroll; the historical record remains.

**WEP-453 — Milestone publication.** *Approved.* A milestone is published when crossed, in the digest and, if notable, in the chronicle. It is not re-published every turn while the state remains above the threshold.

**WEP-454 — Milestone versioning.** *Approved.* A threshold change creates a new series version. Existing records keep the version at which they were crossed; a later version does not retroactively create or erase a milestone.

**WEP-455 — No milestone farming.** *Approved.* A milestone is edge-triggered. Oscillating above and below a threshold does not re-award the same milestone; a higher tier requires a higher threshold.

**WEP-456 — Descriptive life phases.** *Approved (URB-128).* The four descriptive phases "Settlement / Specialisation / Industrialisation / Maturity" MAY be used as milestone labels. They remain descriptive and do not create a second state machine or a progression gate.

**WEP-457 — Capstone recognition.** *Approved (`11A-DR-030`).* A B-05 capstone programme completion may emit a milestone and a historical honour. It does not create a new wonder mechanic, a new infrastructure type or a permanent yield.

**WEP-458 — Account-continuity milestone.** *Approved (D-040).* A tutorial or account milestone is account-scope and survives a reroll. It MUST be non-transferable and not re-earnable. It grants no value to the replacement nation.

### 9.4 Prestige and recognition

**WEP-459 — No prestige currency.** *Approved (ECN-092, D-149).* B-11 creates no prestige points, influence balance, honour currency, spendable status or account rank. A "prestige" label on a numeric balance is invalid.

**WEP-460 — Honour classes are categorical.** *Approved.* An honour class states the kind of achievement (world-first, season champion, event, defensive, diplomatic, development, long service). It is not ordered into a ladder and carries no numeric value.

**WEP-461 — Recognition is representational.** *Approved (D-151).* Recognition communicates achievement and national identity. It does not grant economic output, military power, political control, protection or eligibility.

**WEP-462 — No power-affecting prestige at launch.** *Approved.* A power-affecting recognition mechanic is not adopted. Any future proposal needs explicit evidence, a compatibility analysis, a decision entry and a provisional designation until calibrated and approved.

**WEP-463 — Honour display.** *Approved.* An honour displays its class, the condition, the date, the scope and its inertness statement. It does not display a point total.

**WEP-464 — Honour closure.** *Approved (`11A-DR-016`).* An honour declares its eligibility closure: world-state (always attainable in principle), window-scoped, or disclosed first-N. A closed honour without prior disclosure is invalid. Fossilisation is limited by preferring world-state and window-scoped triggers.

### 9.5 Permanent versus seasonal progression

**WEP-465 — Permanent national progression.** *Approved.* Achievements, milestones, honours, chronicle entries, event records and standings anchors are permanent. They survive seasons.

**WEP-466 — Temporary season progress.** *Approved.* Seasonal objective points, seasonal standings and seasonal awards are scoped to a season. They reset at the boundary.

**WEP-467 — Seasonal rewards.** *Approved.* A seasonal reward is granted under §11 and recorded permanently. The entitlement does not evaporate at the season boundary.

**WEP-468 — Seasonal ranking.** *Approved.* A seasonal standing is derived from snapshots inside the season. It does not read across seasons unless the definition explicitly declares a cross-season record view.

**WEP-469 — Seasonal achievements.** *Approved.* A seasonal achievement is scoped to its season ID. The same achievement in a later season uses a new key and a new season-scoped record.

**WEP-470 — Historical archives.** *Approved.* The season archive stores the final standing, the champion, the definition version and the participating population. Full per-turn detail follows B-02 retention.

**WEP-471 — Reset timing.** *Approved.* A season opens and closes at named boundaries. The close is a single atomic transition; a partially closed season is invalid.

**WEP-472 — Carryover.** *Approved.* No seasonal progress carries into the next season unless the definition explicitly declares a carryover and a cap. The default is zero carryover.

**WEP-473 — Non-resettable records.** *Approved.* The chronicle, event history, campaign records, agreement history, achievement records, honour records and standing archives are never reset by a season.

**WEP-474 — Season identifier.** *Approved (P-06).* A season is stored as an identifier plus opening and closing boundaries. It creates no world instance, no separate population and no parallel national state.

**WEP-475 — Season failure.** *Approved.* If the season transition fails, it resumes from the last checkpoint. It never half-resets: either the whole seasonal scope resets or none of it does.

**WEP-476 — No seasonal state reset.** *Approved (WEP-421).* A season never resets a nation's cities, infrastructure, population, treasury, research, diplomacy, alliance or military state.

### 9.6 Inflation and runaway leaders

**WEP-477 — No compounding advantage.** *Approved (ECN-113, URB-101).* No B-11 reward, honour or milestone may increase a yield, a production rate, a capacity or a military modifier permanently. A reward that compounds is invalid.

**WEP-478 — No unbounded accumulation.** *Approved.* Honours are keyed and closed or windowed. A renewable honour source declares a cap. There is no infinite prestige farm because there is no prestige balance.

**WEP-479 — No reward snowball.** *Approved.* A reward never increases the rate at which further rewards are earned. The recognition layer is non-compounding by construction.

**WEP-480 — Old-nation fairness.** *Approved (NAT-045, D-021).* Competitive standings use windows and rates. A long-established nation is not given a handicap and is not given an advantage by age. Its permanent record is commemorated, not converted into power.

**WEP-481 — New-player opportunity.** *Approved (AP-004).* Every permanent honour class has a world-state or window-scoped variant that a new nation can still attain, except a disclosed first-N honour. Every competitive standing can be won on a windowed basis by a new nation.

**WEP-482 — Dormancy is not punished.** *Approved (D-028).* A returning nation loses no honour, record or progress. Its standing re-enters at the next snapshot. It is not decayed, taxed or demoted.

**WEP-483 — No arbitrary punishment of success.** *Approved.* A successful long-term nation keeps its records and honours. The design limits power by keeping recognition inert, not by confiscating achievement.

**WEP-484 — Reward share monitoring.** *Approved (Prompt 14).* The share of material reward value held by the top cohort is a Prompt 14 calibration check. B-11 defines the structural guard; Prompt 14 proves the bound.

**WEP-485 — Historical record cannot be bought.** *Approved.* No purchase, promotion or external benefit may create, alter or accelerate a permanent record.

**WEP-486 — Progression audit.** *Approved.* A yearly (or declared) audit verifies that no honour series is unbounded, no reward is a multiplier and no standing is a de facto overall score. The audit is a documentation check, not a runtime feature.

---

## 10. Achievements and Milestones — consolidated object model

**WEP-487 — Recognition object table.** *Approved.* The five recognition objects have these mandatory properties:

| Object | Key | Persistence | Scope default | Grants power? | Reassignable? |
|---|---|---|---|---|---|
| Achievement | `achievement_key` | Permanent | Nation | No | No |
| Milestone | `milestone_key` | Permanent | Nation | No | No |
| Seasonal award | `season_id + award_key` | Record permanent; season progress resets | Nation or Alliance | No | No |
| Historical honour | `honour_key` | Permanent | Nation or Alliance | No | No |
| Standing | `(turn_id, standing_id)` snapshot | Snapshot permanent; rank transient | Nation or Alliance | No | No |

**WEP-488 — One condition, several objects.** *Approved (`11A-DR-014`).* A single verified completion may emit several objects. Each has its own key; the material reward, if any, is granted once under WEP-502.

**WEP-489 — Object precedence.** *Approved.* A milestone is derived from state and needs no claim. An achievement is a keyed grant. A seasonal award is scoped to a season. A historical honour is permanent world-state or event recognition. A standing is a snapshot. An object never changes type.

**WEP-490 — No double-counting.** *Approved.* The same fact may be referenced by several objects but is stored once in the owning subsystem and referenced by ID. B-11 does not create a second copy of a B-05 infrastructure value to make a milestone.

**WEP-491 — Completion percentage.** *Approved (`11A-DR-008`).* A public achievement displays a completion percentage only when the denominator (eligible nations at the snapshot) is published and at least `k = 5`. A percentage without a denominator is a defect.

**WEP-492 — Dated attribution.** *Approved.* Every recognition object records the turn and UTC time of the grant or crossing. A later reconstruction uses the record, not the current state.

**WEP-493 — Inertness field.** *Approved (`11A-DR-033`).* Every recognition object definition states what it does not grant. The statement is player-visible.

**WEP-494 — Correction authority.** *Approved.* A correction is appended by B-11 for a B-11 defect, by the owning subsystem for a source defect, or by Prompt 12 for an invalid grant. No other authority may alter a recognition record.

**WEP-495 — Deletion is prohibited.** *Approved.* A recognition record is never deleted. A revoked record remains with its revocation reference. A privacy redaction is a disclosed overlay, not a deletion.

**WEP-496 — Account-scope caution.** *Approved.* An account-scope object must be non-transferable and not re-earnable. It cannot carry a material reward that a replacement nation could use.

**WEP-497 — Honour class catalogue.** *Approved.* The classes are `WORLD_FIRST` (disclosed closed-eligibility), `SEASON_CHAMPION`, `EVENT_HONOUR`, `DEFENSIVE_HONOUR`, `DIPLOMATIC_HONOUR`, `DEVELOPMENT_HONOUR` and `CONTINUITY_HONOUR` (commemorative tenure, no merit). A new class requires a decision.

**WEP-498 — Recognition does not gate play.** *Approved.* No achievement, milestone, seasonal award or honour may be required to build, trade, fight, sign, join, vote or participate. Recognition is an output of play, never an entry ticket.

---

## 11. Rewards, recognition and reward accounting

### 11.1 Reward classification

**WEP-499 — Six reward classes.** *Approved (D-151).* The classes are `RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE` and `MATERIAL`. The default hierarchy is recognition → record → authorship → rare material.

**WEP-500 — Recognition reward.** *Approved.* A badge, honour label, achievement display or standing mention. It grants no value and no eligibility.

**WEP-501 — Record reward.** *Approved.* A chronicle entry, a milestone record or a historical anchor. It is permanent and non-comparative.

**WEP-502 — Authorship reward.** *Approved.* A right to name or describe one's own nation within B-03's existing identity rules. It never grants a policy, a government, a capability or a mechanical advantage.

**WEP-503 — Cosmetic and title rewards.** *Approved.* Display-only tokens and labels with an inertness statement. They are never purchasable and never tradeable.

**WEP-504 — Material reward.** *Approved (ECN-113, ECN-013(c)).* A Crown or resource grant through B-04's `REWARD` ledger type. It is rare, disclosed, keyed, non-repeatable and never a yield multiplier.

**WEP-505 — No mixing by accident.** *Approved.* A definition states each reward class separately. A material reward is never bundled invisibly with a recognition reward; the player sees the full grant before claiming.

### 11.2 Reward definition

**WEP-506 — Reward fields.** *Approved.* Every reward MUST declare: reward ID; source (event, objective, achievement, milestone, season or standing); reward class; trigger; eligibility; grant timing; quantity or value where applicable; ledger owner; expiry or claim window; repetition rule; duplication protection key; reversal or correction authority; visibility; audit requirement; and an inertness statement.

**WEP-507 — Reward source.** *Approved.* A reward is emitted by exactly one source object. A source may emit several reward classes, each with its own reward ID and key. A reward without a source is invalid.

**WEP-508 — Quantity and units.** *Approved.* A material quantity is an integer with a unit from B-04's resource roster or the Crown. A non-material reward has no quantity. A floating-point quantity is invalid.

**WEP-509 — Repetition.** *Approved.* A reward is one-time by default. A repeatable reward declares the repeat window, the per-window cap and whether the material class repeats. A material reward may repeat only under an approved decision and a Prompt 14 cap (WEP-504).

**WEP-510 — Duplication protection.** *Approved.* Every reward uses the achievement key. The first valid grant in the published P6 order wins; later claims deduplicate (`TR-055`, `TR-073 G2`).

**WEP-511 — Disclosed before grant.** *Approved (ECN-113(b)).* The player sees the reward class, the quantity and the conditions before the grant or claim. A hidden material reward is invalid.

**WEP-512 — No conversion.** *Approved (ECN-113(e)).* A reward is not convertible into a repeatable transfer, a tradeable claim, a second currency or an external benefit.

**WEP-513 — No yield multiplier.** *Approved (ECN-113).* A reward may not multiply production, income, capacity, research or military output permanently. A temporary effect is an event effect, not a reward, and follows §6.7.

**WEP-514 — Reward record.** *Approved.* B-11 stores the reward record: reward ID, source, key, recipient, class, quantity, ledger reference, turn, visibility and audit ID. B-04 stores the balance.

### 11.3 Reward eligibility

**WEP-515 — Eligible nation.** *Approved.* The recipient is the nation that satisfied the condition. A reward is not paid to an account, a player, an alliance officer or a third party.

**WEP-516 — Eligible owner.** *Approved.* The owner receives the record. An account-scope reward is permitted only where WEP-031 allows it and the reward is non-transferable.

**WEP-517 — Active status.** *Approved.* A dormant nation remains eligible for a deferred claim and for recognition. A retired nation is not eligible for a new reward; its historical rewards remain.

**WEP-518 — Protection status.** *Approved.* Protection never blocks a non-hostile reward. It blocks a hostile reward that would require an attack or a protected target.

**WEP-519 — Event participation.** *Approved.* An event reward requires a recorded participant and a verified completion. A spectator is not a participant.

**WEP-520 — Objective verification.** *Approved.* An objective reward requires `VERIFIED`. A `COMPLETED_PENDING_VALIDATION` instance is not eligible.

**WEP-521 — Standing qualification.** *Approved.* A standing award requires a published snapshot and a resolved tie. A provisional WSE does not disqualify a display but does disqualify a competitive award until resolved.

**WEP-522 — Seasonal eligibility.** *Approved.* A seasonal reward requires participation in the season and a final seasonal result. A nation that joins after the season closes is not eligible.

**WEP-523 — Disqualification.** *Approved (Prompt 12).* A Prompt 12 invalidation removes eligibility for a future reward. An already-granted reward is corrected by the evidence path; B-11 does not impose a penalty.

**WEP-524 — Duplicate claims.** *Approved.* A duplicate claim returns the original grant and writes `WPA-30`. It never grants twice.

**WEP-525 — Reward expiry.** *Approved (D-028).* A reward entitlement never expires through absence. A claim window may control *when* a choice is made, but the entitlement persists; if a choice is required and not made, the default is "no choice", not forfeiture.

**WEP-526 — Incomplete claims.** *Approved.* A claim missing a required selection is `DEFERRED`, not rejected. The player may complete it later without loss.

### 11.4 Reward distribution

**WEP-527 — Automatic versus claimed.** *Approved.* A recognition or record reward may be automatic. A material reward and any reward requiring a choice are claimed explicitly. A discretionary reward is never accepted through silence.

**WEP-528 — Claim window.** *Approved.* A claim window is expressed in turns or a named boundary. It does not create a forfeiture; it only bounds when the player may make a selection. The entitlement remains.

**WEP-529 — Grant transaction.** *Approved.* A material grant is one atomic transaction: B-11 writes the reward record, B-04 writes the `REWARD` ledger event and the balance change, and the audit event is written in the same transaction.

**WEP-530 — Atomicity.** *Approved.* If any part of the grant fails, none of it applies. B-11 records `DEFERRED` with the failure code; it does not leave a record without a ledger entry or a ledger entry without a record.

**WEP-531 — Idempotency.** *Approved.* The achievement key is the idempotency key. A retry returns the original result. A duplicate key never creates a second ledger event.

**WEP-532 — Ledger integration.** *Approved (ECN-165).* The only material path is the existing `REWARD` event type. B-11 creates no ledger type, no parallel treasury and no off-ledger grant.

**WEP-533 — Historical record.** *Approved.* A grant writes a permanent reward record. A later correction appends; it does not erase the original.

**WEP-534 — Failed grant recovery.** *Approved.* A failed grant is retried at the next W5 with the same key. If it fails repeatedly, the entitlement stays `DEFERRED` and is reported to the player and to the operator console; it is never silently discarded.

**WEP-535 — Duplicate prevention.** *Approved.* The key check runs before the grant and again inside the ledger transaction. A race between two claims resolves to one grant and one deduplication record.

**WEP-536 — No discretionary auto-claim.** *Approved.* A material reward, a title and an authorship unlock are discretionary. B-11 must not claim them on a player's behalf, even when the condition is satisfied. The player receives a claimable entitlement.

### 11.5 Economic reward restrictions

**WEP-537 — Authoritative subsystem.** *Approved (ECN-113, ECN-215).* Every Crown or resource reward is created, valued and recorded by B-04. B-11 never writes a balance and never invents a resource.

**WEP-538 — Source of value.** *Approved (ECN-013(c)).* A new-Crown reward is a rare, disclosed, system-generated event adjustment approved by B-11's rules. It is not tax, production, trade or a transfer.

**WEP-539 — Accounting entry.** *Approved (ECN-111).* The grant enters the world money-conservation identity as a `one_time_rewards` term. The closing-balance identity and the conservation identity must both hold.

**WEP-540 — Value conservation.** *Approved.* A material reward is either a system-generated grant with a declared source or a transfer from an existing authorized pool. It is never created from nothing without a ledger entry.

**WEP-541 — Creates or transfers.** *Approved.* The definition states whether the reward creates value or transfers it. An alliance-funded reward is prohibited (ALL-224). A nation-to-nation prize is prohibited.

**WEP-542 — Caps.** *Approved (Prompt 14).* Every material class declares a per-recipient, per-window and world-share cap. The cap is published. An over-cap grant is rejected, not truncated.

**WEP-543 — Duplicate grant protection.** *Approved.* The achievement key and the B-04 event key both prevent a duplicate. A replay returns the original ledger reference.

**WEP-544 — Failure behaviour.** *Approved.* A rejected ledger transaction leaves the reward `DEFERRED`, no balance change and a `WPF-30` record. The event or objective remains complete; only the grant is deferred.

**WEP-545 — Audit event.** *Approved.* Every material grant writes `WPA-16` `REWARD_GRANTED` with the reward ID, key, recipient, quantity, ledger reference, turn and conservation check result.

**WEP-546 — No debt or alternative treasury.** *Approved (ECN-*).* B-11 creates no debt, credit, loan, bond, escrow account or second treasury. A challenge reservation uses the owning subsystem's existing reservation, not a B-11 balance.

**WEP-547 — No paid progression.** *Approved (WEP-068).* There is no paid reward, paid skip, paid reroll, paid boost or paid recognition. The ₹0/free-first product constraint is respected.

### 11.6 Reward stacking and interaction

**WEP-548 — One key, one grant.** *Approved.* Stacking is permitted only across different reward classes with different keys. The same achievement key cannot produce two material grants.

**WEP-549 — Layered emission.** *Approved (`11A-DR-014`).* One completion may emit a record, an honour and a standing entry. Each has its own key. The material reward, if any, is one of them and is granted once.

**WEP-550 — No duplicate achievement claims.** *Approved.* A duplicate claim is deduplicated by key, recorded and returned. It is not treated as a new completion.

**WEP-551 — No replay grants.** *Approved.* A replayed turn cannot re-grant. The W4 and W5 steps are idempotent.

**WEP-552 — Unintended stacking.** *Approved.* A definition declares its maximum simultaneous reward set. A combination not declared is rejected with `WPF-31`.

**WEP-553 — Unbounded accumulation.** *Approved.* A repeatable reward declares a cap. An uncapped repeatable material reward is invalid.

**WEP-554 — Seasonal and permanent duplication.** *Approved.* A seasonal award and a permanent achievement for the same fact use different keys and different classes. Only one material grant may be attached to the fact; the other is recognition.

**WEP-555 — Stacking audit.** *Approved.* Every multi-object emission writes one audit record listing the keys and the single material grant, so a later audit can prove no double payment.

**WEP-556 — No reward for the same fact twice.** *Approved.* A source fact is referenced by one material reward key. A second object may recognise the fact, but it may not pay for it again.

## 12. Eligibility — consolidated rules

**WEP-557 — One eligibility model.** *Approved.* Event, objective and standing eligibility are three consumers of one model. The model reads B-03's authoritative states: nation existence, protection, dormancy, retirement, pair restriction, account status and first-boundary completion.

**WEP-558 — Eligibility is evaluated, not cached.** *Approved (TR-051).* The consumer re-evaluates at every boundary named in WEP-142. A cached result is valid only inside one phase of one turn.

**WEP-559 — Eligible set fingerprint.** *Approved.* Every event instance, objective instance and standing snapshot records the eligible-set fingerprint. A later dispute can reconstruct exactly who was eligible.

**WEP-560 — Protection.** *Approved.* Protected nations are eligible for non-hostile participation and standings, ineligible for hostile targets and hostile effects. The check is server-side and uses the same cumulative validator set as a direct action.

**WEP-561 — Dormancy.** *Approved.* Dormant nations are excluded from public standings and public participant lists as a presentation rule, remain eligible for deferred claims and recognition, and lose nothing.

**WEP-562 — Retirement.** *Approved.* Retired nations are removed from current standings and current participation; historical records remain attributed; the replacement starts with no nation-scope credit.

**WEP-563 — New nations.** *Approved.* `UNRANKED` until the first completed boundary; informational and non-hostile onboarding events may occur earlier; no competitive award before the first boundary.

**WEP-564 — Incomplete data.** *Approved.* A missing input produces `PROVISIONAL`, never zero. A standing with an incomplete population is published with a provisional marker or withheld under `k = 5`.

**WEP-565 — Status-change record.** *Approved.* Every eligibility change writes a record with the old state, new state, reason, turn and source rule. A silent exclusion is a defect.

**WEP-566 — No parallel protection.** *Approved.* B-11 must not define a protection-like state, a cooldown, an immunity or a "safe" flag. Protection is B-03's alone.

---

## 13. State machines and transition integrity

**WEP-567 — Twelve machines.** *Approved.* B-11 defines twelve state machines: event definition, event instance, event participation, objective definition, objective instance, objective progress, achievement qualification, achievement award, ranking snapshot, seasonal progression, reward claim and historical record correction. The tables in this section are normative.

**WEP-568 — Common transition fields.** *Approved.* Every transition row states the from-state, to-state, initiator, precondition, validation, P6 step, mutation, audit event, failure code, recovery and visibility. A row missing a field is a defect.

**WEP-569 — Common failure rule.** *Approved.* A failed transition changes no state, releases no reservation unless the failure code says so, and writes one failure record. A transition is never partially applied.

**WEP-570 — Common recovery rule.** *Approved (TR-043).* Recovery resumes from the last completed W-step checkpoint. A completed transition is not repeated; an interrupted one is re-evaluated idempotently.

**WEP-571 — Common visibility rule.** *Approved.* A transition that produces a public record is visible only after P7. A pre-P7 state is visible to the system and, where the definition permits, to the owner.

**WEP-572 — Invalid transition catalogue.** *Approved.* The invalid transitions named in each machine and in WEP-114, WEP-251 and WEP-608 are exhaustive for their machine. An unlisted transition is also invalid; the tables permit only what they list.

**WEP-573 — Event definition machine.** *Approved.*

| From | To | Initiator | Precondition | Validation | Step | Mutation | Audit | Failure | Recovery | Visibility |
|---|---|---|---|---|---|---|---|---|---|---|
| TEMPLATE_DRAFT | TEMPLATE_PUBLISHED | System/authority | All fields present; inertness stated; formula resolves | Field and formula check | W0 (outside turn) | Version sealed | WPA-01 | WPF-01 | Correct fields | Published |
| TEMPLATE_PUBLISHED | TEMPLATE_SUPERSEDED | System | A later version published | Version ordering | W0 | Supersede link | WPA-02 | WPF-01 | Keep old version | Published |
| TEMPLATE_PUBLISHED | TEMPLATE_RETIRED | System | No active instance requires it; or a retirement date reached | Active-instance check | W0 | Retirement record | WPA-03 | WPF-02 | Keep active instances | Published |

**WEP-574 — Event instance machine.** *Approved.*

| From | To | Initiator | Precondition | Validation | Step | Mutation | Audit | Failure | Recovery | Visibility |
|---|---|---|---|---|---|---|---|---|---|---|
| — | QUALIFIED | System | Trigger fired; key unique | Key + definition check | W1 | Instance record | WPA-04 | WPF-05 | None | System |
| QUALIFIED | SCHEDULED | System | Boundaries valid; teardown later than close | Boundary check | W1 | Schedule fields | WPA-05 | WPF-06 | None | System |
| SCHEDULED | ANNOUNCED | System | Announcement boundary reached | Visibility check | W1 | Announcement record | WPA-06 | WPF-07 | Retry next turn | Participants |
| ANNOUNCED | ACTIVE | System | Start boundary; eligibility final | Eligibility + baseline | W1 | Activation record | WPA-07 | WPF-08 | Cancel | Public |
| ACTIVE | CLOSED | System | Closing boundary reached | Freeze + participant check | W1 | Close record | WPA-08 | WPF-09 | Resume checkpoint | Public |
| CLOSED | COMPLETED | System | Completion verified | Source + key + reward check | W1/W4 | Result + reward record | WPA-10 | WPF-18 | Stay CLOSED | Public after P7 |
| CLOSED | EXPIRED | System | Teardown boundary reached without completion | Teardown check | W1 | Expiry record | WPA-11 | WPF-12 | Resume checkpoint | Public after P7 |
| QUALIFIED/SCHEDULED/ANNOUNCED | CANCELLED | System | Precondition invalid or duplicate | Reason check | W1 | Cancellation record | WPA-12 | WPF-07 | Idempotent | Public after P7 |
| ACTIVE/CLOSED | VOIDED | System | Invalidity found | Evidence + reason | W1 | Correction record | WPA-13 | WPF-13 | Preserve grants | Public after P7 |

**WEP-575 — Event participation machine.** *Approved.*

| From | To | Initiator | Precondition | Validation | Step | Mutation | Audit | Failure | Recovery | Visibility |
|---|---|---|---|---|---|---|---|---|---|---|
| NOT_JOINED | JOINED | Player | Instance ACTIVE; before freeze; explicit action | Eligibility + terms | W1 | Participation record | WPA-14 | WPF-14 | None | Owner |
| JOINED | WITHDRAWN | Player | Before freeze | Freeze + stake check | W1 | Withdrawal record | WPA-15 | WPF-15 | None | Owner |
| JOINED | COMPLETED | System | Verified completion | Source + key | W1/W4 | Completion record | WPA-10 | WPF-18 | Stay JOINED | Public after P7 |
| JOINED | SUSPENDED | System | Prompt 12 evidence path | Evidence ID | W1 | Hold record | WPA-31 | WPF-32 | Review | Owner + moderator |
| SUSPENDED | JOINED | System | Hold lifted | Review result | W1 | Release record | WPA-32 | WPF-32 | Keep hold | Owner |
| SUSPENDED | DISQUALIFIED | System | Prompt 12 invalidation | Evidence | W1 | Correction record | WPA-33 | WPF-33 | None | Owner + moderator |

**WEP-576 — Objective definition machine.** *Approved.* `OBJ_DRAFT → OBJ_PUBLISHED → OBJ_RETIRED`; `OBJ_PUBLISHED → OBJ_SUPERSEDED` on a later version. Validation is the field set, formula resolution, category legality and the individual-equivalent check for `OBJ-ALL`. Failure `WPF-34`; recovery is field correction.

**WEP-577 — Objective instance machine.** *Approved.*

| From | To | Initiator | Precondition | Validation | Step | Mutation | Audit | Failure | Recovery | Visibility |
|---|---|---|---|---|---|---|---|---|---|---|
| — | AVAILABLE | System | Definition published; eligible; under cap | Eligibility + cap | W2 | Offer record | WPA-17 | WPF-19 | Skip offer | Owner |
| AVAILABLE | DISMISSED | Player | Offer open | Explicit action | W2 | Dismissal record | WPA-18 | WPF-19 | None | Owner |
| DISMISSED | AVAILABLE | System | Re-offer interval; cap | Interval check | W2 | New offer | WPA-17 | WPF-19 | Wait | Owner |
| AVAILABLE | ACCEPTED | Player | Offer open; explicit action | Eligibility + terms | W2 | Acceptance record | WPA-19 | WPF-20 | None | Owner |
| ACCEPTED | IN_PROGRESS | System | First source event or acceptance boundary | Source check | W2 | Progress baseline | WPA-20 | WPF-23 | Stay ACCEPTED | Owner |
| IN_PROGRESS | TIER_REACHED | System | Tier predicate true | Source + key | W2 | Tier record | WPA-21 | WPF-21 | Stay IN_PROGRESS | Owner |
| TIER_REACHED | IN_PROGRESS | System | Higher tier possible | Progress check | W2 | Continue | WPA-20 | WPF-21 | Stay | Owner |
| IN_PROGRESS/TIER_REACHED | COMPLETED_PENDING_VALIDATION | System | Completion predicate true | Source + key | W2 | Pending record | WPA-22 | WPF-22 | Return IN_PROGRESS | Owner |
| COMPLETED_PENDING_VALIDATION | VERIFIED | System | Source + key + window pass | Full verification | W2 | Completion record | WPA-23 | WPF-22 | Return IN_PROGRESS | Owner |
| VERIFIED | REWARD_PENDING | System | Reward exists | Reward eligibility | W4 | Entitlement record | WPA-24 | WPF-30 | Stay VERIFIED | Owner |
| VERIFIED | CLAIMED | System | No reward or auto recognition | Key check | W4 | Completion record | WPA-23 | WPF-22 | Stay | Public if public |
| REWARD_PENDING | CLAIMED | Player/system | Explicit claim or automatic recognition | Key + state | W5 | Grant record | WPA-16 | WPF-30 | Stay pending | Owner |
| REWARD_PENDING | DEFERRED | System | Claim blocked | State check | W5 | Deferral record | WPA-34 | WPF-30 | Retry W5 | Owner |
| DEFERRED | REWARD_PENDING | System | Block cleared | State check | W5 | Recheck record | WPA-34 | WPF-30 | Stay deferred | Owner |
| AVAILABLE/ACCEPTED/IN_PROGRESS/TIER_REACHED | EXPIRED | System | Window ended | Boundary check | W2 | Expiry record | WPA-25 | WPF-24 | None | Owner |
| any non-terminal except CLAIMED | WITHDRAWN | System | Source retired, event cancelled or invalidity | Reason check | W2 | Withdrawal record | WPA-26 | WPF-25 | None | Owner |
| any non-terminal | SUPERSEDED | System | Mechanic change or new version | Review record | W2 | Supersede record | WPA-27 | WPF-26 | Offer replacement | Owner |

**WEP-578 — Objective progress machine.** *Approved.* A progress record is `NOT_STARTED → COUNTING → TIER_MET → COMPLETE`; a correction moves `COMPLETE → CORRECTED` or `COUNTING → INVALID`. A record is never deleted. The source key is unique per instance and tier. Invalid transitions: `COMPLETE → COUNTING` (except through a correction), `INVALID → COMPLETE` without a new source proof.

**WEP-579 — Achievement qualification and award machines.** *Approved.* Qualification: `NOT_QUALIFIED → QUALIFIED → GRANTED`; award: `GRANTED → CORRECTED` or `GRANTED → REVOKED` (Prompt 12 only). A revoked award remains visible. Invalid: `REVOKED → GRANTED` on the same key; a regrant requires a new key and a new condition proof.

**WEP-580 — Ranking snapshot machine.** *Approved.* `SEALED → PUBLISHED`; a correction creates a new snapshot `SEALED → PUBLISHED` with `corrects_snapshot_id`, and the original becomes `corrected_by`. A published snapshot never returns to `SEALED`. Invalid: `PUBLISHED → SEALED`; `SEALED → SEALED` for the same `(turn, standing)`.

**WEP-581 — Seasonal progression machine.** *Approved.* `SEASON_SCHEDULED → SEASON_OPEN → SEASON_CLOSED → SEASON_ARCHIVED`. The close is atomic. An interrupted close resumes from the checkpoint. Invalid: `SEASON_CLOSED → SEASON_OPEN` for the same season ID; a new season needs a new ID.

**WEP-582 — Reward claim machine.** *Approved.* `NOT_ELIGIBLE → ELIGIBLE → CLAIM_PENDING → GRANTED`; `ELIGIBLE/CLAIM_PENDING → DEFERRED → CLAIM_PENDING`; `GRANTED → CORRECTED` (evidence path only). No `EXPIRED_UNCLAIMED`; absence never forfeits.

**WEP-583 — Historical record correction machine.** *Approved.* `RECORDED → CORRECTED` or `RECORDED → REDACTED`; the original remains. `REDACTED` records the authority and reason. Invalid: deletion; `CORRECTED → RECORDED`; editing the original in place.

**WEP-584 — Machine interaction.** *Approved.* A single P6 step may advance several machines for one object (for example, an event instance closes, completes and writes a reward). The order inside the step is event → objective → snapshot → record → claim. A machine may not advance another machine out of that order.

---

## 14. Rules, calculations and the formula register

**WEP-585 — Every calculation has one home.** *Approved.* B-11 arithmetic exists only in the [formula register](18_world_events_objectives_rankings_progression_formula_register.md). This document states the rule and cites the formula; it never states a conflicting expression.

**WEP-586 — Formula identifiers.** *Approved (D-152).* B-11 formulas use `F-WEP-###`. The namespace is new, checked free and never reuses an `F-` identifier from B-02…B-10.

**WEP-587 — Mandatory formula fields.** *Approved.* Every formula has the twenty fields in the register's §2: identifier, name, domain, purpose, expression, variables, input source, units, valid range, output range, rounding, caps, floors, phase, snapshot, missing data, invalid input, worked example, boundary case, provisional status, calibration owner and main rule references.

**WEP-588 — Provisional numbers.** *Approved.* A number is one of: an existing approved value; a structural constant; a provisional design assumption; a Prompt 14 calibration parameter; or an owner-reserved value. A number is never described as calibrated unless Prompt 14 has calibrated it.

**WEP-589 — No arbitrary weights.** *Approved.* A weight exists only where the structure requires it and is labelled provisional. A hidden or unexplained constant is a formula defect.

**WEP-590 — Integer arithmetic.** *Approved.* B-11 uses integer arithmetic and basis points (`bp`, 10,000 = 100%). Rounding is floor, ceiling or largest remainder, stated in the formula. No floating-point step is authoritative.

**WEP-591 — Zero-denominator branch.** *Approved.* Every division states its zero-denominator behaviour. A division by zero never produces a rank, a reward or a snapshot.

**WEP-592 — Missing data.** *Approved.* Every formula states its missing-data behaviour: fail closed, `PROVISIONAL`, or omit the entity. It never silently substitutes zero.

**WEP-593 — Formula change control.** *Approved.* A formula change creates a new version and a new snapshot series. It does not rewrite a sealed snapshot, a completed objective or a granted reward.

**WEP-594 — Worked examples.** *Approved.* Every formula has a normal example, a boundary example and an invalid-input behaviour. The examples are synthetic and are not balance evidence.

---

## 15. Data ownership and system of record

**WEP-595 — Ownership matrix.** *Approved.* The following matrix is authoritative. B-11 is the owner only of the B-11 rows.

| Data item | Authoritative owner | B-11 access | B-11 mutation | Audit owner | Privacy |
|---|---|---|---|---|---|
| Resource balances, ledger | B-04 | Read published/reference values | None; requests `REWARD` | B-04 | Owner; aggregates `k≥5` |
| City, infrastructure, facilities | B-05 | Read published state | None | B-05 | Public/owner per B-05 |
| Population, approval, stability, political state | B-06 | Read public statistics and named terms | None; `E-POL` request only | B-06 | Public statistic / owner |
| Trade transactions | B-07 | Read only after gate | None | B-07 | Parties / `k≥5` |
| Diplomatic agreements and counts | B-08 | Read published facts | None | B-08 | Public per B-08 |
| Alliance membership, roles, aggregates | B-09 | Read membership + aggregate | None | B-09 | `k≥5`; roles per B-09 |
| Campaign records, outcomes | B-10 | Read permanent record | None | B-10 | B-10 bands |
| Turn, phase, digest, history class | B-02 | Read/write its own P6 records | Writes B-11 records only | B-02 | Per class |
| Event definitions and instances | **B-11** | Own | Own | B-11 | Definition public; instance per scope |
| Objective definitions and instances | **B-11** | Own | Own | B-11 | Offer/progress per definition |
| Progress records | **B-11** | Own | Append only | B-11 | Owner/public per definition |
| Standing definitions and snapshots | **B-11** | Own | Append only | B-11 | Public snapshot; `k≥5` |
| Achievement, milestone, honour records | **B-11** | Own | Append only | B-11 | Public/private per object |
| Reward records (not balances) | **B-11** | Own | Append only | B-11 | Owner/public per reward |
| Chronicle notability decisions | **B-11** | Own | Append only | B-11 | Public/private per event |
| Audit events `WPA-` | **B-11** | Own | Append only | B-11 | Restricted |
| Privacy suppression decisions | B-02 (`D-027`) | Read | None | B-02 | Restricted |

**WEP-596 — No shadow copy.** *Approved.* B-11 stores a reference ID and a derived value, never a second authoritative copy. A cached input is invalid across a boundary.

**WEP-597 — Write boundary.** *Approved.* B-11 writes only its own tables and its own audit events. It requests an owning subsystem's mutation through the contract in §17. A direct write to a B-04…B-10 table is a defect.

**WEP-598 — Reward record versus balance.** *Approved.* The B-11 reward record proves intent and key; the B-04 ledger proves value. A reconciliation must find one of each per key. A record without a ledger entry is `DEFERRED`; a ledger entry without a record is an invariant break.

**WEP-599 — Ranking input provenance.** *Approved.* Every snapshot input names its owning subsystem and source field. An input without provenance is invalid and the standing is withheld.

**WEP-600 — Historical ownership.** *Approved.* B-11 owns the history of its own objects. B-02 owns the history class and retention; B-03 owns nation identity history; B-04 owns value history; B-10 owns campaign history.

**WEP-601 — Privacy ownership.** *Approved.* D-027 and B-02 own the suppression rules. B-11 applies them; it does not reinterpret them. A B-11 field classified public by its definition is still subject to `k ≥ 5` when aggregated.

**WEP-602 — Audit ownership.** *Approved.* The B-11 audit stream is append-only and restricted. B-02's audit spine remains the cross-system record. A B-11 audit event references the B-02 turn and phase.

**WEP-603 — No ownership by implication.** *Approved.* A B-11 field that looks like a copy of an owned value is not authoritative and must be removed or reclassified. The ownership matrix is the only test.

**WEP-604 — Deletion.** *Approved.* B-11 never deletes a class-P record, a snapshot anchor, a grant or a correction. It may compact class-S detail under B-02's job, never its own permanent records.

---

## 16. Turn-processing integration

**WEP-605 — P6 ownership.** *Approved (TR-040).* B-11 owns the content of P6 and the B4 evaluation order. B-02 owns the phase boundary, the freeze, the failure model and P7 publication.

**WEP-606 — P6 step order.** *Approved (D-150).* The order is fixed:

| Step | Name | What happens | Owner | Output |
|---|---|---|---|---|
| W1 | Event resolution and generation | Close, complete, expire, cancel, void, generate and activate instances; apply non-material and authorized effects | B-11 | Event states, effect records |
| W2 | Objective evaluation | Record progress, reach tiers, verify completion, expire/withdraw/supersede | B-11 | Progress and completion records |
| W3 | Standing snapshot | Read frozen inputs, compute, normalise, rank, tie-resolve, seal | B-11 | Sealed snapshots |
| W4 | Record writes | Achievements, milestones, honours, chronicle entries, reward entitlements | B-11 | Permanent records, entitlements |
| W5 | Deferred-claim release | Re-check blocked entitlements, grant or keep deferred | B-11 | Grants / deferrals |
| P7 | Publication | Publish digest, standings, records, notices | B-02 | Player-visible outcome |

**WEP-607 — Why events precede objectives.** *Approved (D-150).* An event is a source fact for objective progress and a possible standing input. Evaluating objectives before events would let an objective miss a same-turn event or count a stale one. The order is published and closes the `TR-042` row.

**WEP-608 — No later phase may be read early.** *Approved.* W1 must not read W2 results; W2 must not read W3 ranks; W3 must not read W4 grants; W4 must not read W5 releases. A rule that needs a later result defers to the next turn.

**WEP-609 — P3 boundary.** *Approved.* B-11 does not run in P3. A calendar event's effect on a P3 input is published as a parameter for the next P3; it is not applied to the current turn. This preserves the "no retroactive change" rule.

**WEP-610 — P7 publication.** *Approved (TR-038, TR-077…TR-080).* A B-11 result is visible only after the turn is `COMPLETED` and P7 publishes. A snapshot is not a live rank. A record is not visible before its write is committed.

**WEP-611 — Digest integration.** *Approved (TR-088, TR-089, `11A-CR-028`).* Event, objective, standing and reward movement appears in the existing bounded digest: world events visible to the nation; ranking and objective movement where published; reward claim notices. B-11 creates no second notification channel.

**WEP-612 — Deferred claims at W5.** *Approved.* W5 is the only place a deferred entitlement is released. It re-checks eligibility, the source state, the key and the ledger availability. A release is idempotent.

**WEP-613 — Failure and interruption.** *Approved (TR-043).* A failure in W1–W5 makes the turn `INTERRUPTED`; recovery resumes from the last completed W-step checkpoint. A checkpoint is written after each W-step's transaction commits.

**WEP-614 — Replay.** *Approved (TR-048).* A replay of a completed turn produces the same records and no new grants. A replay of an interrupted turn resumes, not restarts.

**WEP-615 — Recovery authority.** *Approved.* The recovery job is B-02's. B-11 supplies idempotent steps; it does not create a recovery scheduler.

**WEP-616 — Concurrency.** *Approved.* Within a turn, a nation's event, objective and snapshot records are processed in one deterministic order. Across nations, order is irrelevant because allocation is order-independent (TR-046) or keyed.

**WEP-617 — Resource accounting.** *Approved.* B-11's material effects are reconciled at P7 against B-04's `ECN-111` identity. A mismatch fails the turn's B-11 invariant check and is reported; it is never silently corrected.

**WEP-618 — Invariants at P7.** *Approved.* P7 checks: one grant per key; one snapshot per `(turn, standing)`; every permanent record has an audit event; every material grant has a ledger reference; no record has a lower turn than its source; no class-P record was modified in place.

---

## 17. Cross-system integration contracts

**WEP-619 — Contract format.** *Approved.* Every contract states: contract ID; source subsystem and rule; consuming B-11 rule; data consumed; trigger; phase; validation owner; mutation owner; event/objective consequence; ranking consequence; progression consequence; accounting impact; transaction boundary; privacy; failure behaviour; audit; recovery; and related formulas.

**WEP-620 — `WPC-01` B-02 turn lifecycle.** *Approved.* Consumes the frozen post-P5 baseline, the turn ID, the seed and the phase checkpoints. B-11 supplies P6 W1–W5 outputs and P7 publication content. B-02 owns the phase, freeze, failure and recovery. Failure `WPF-40`; recovery from checkpoint; audit `WPA-40`. Related: all `F-WEP-` phase fields.

**WEP-621 — `WPC-02` B-03 protection and eligibility.** *Approved.* Consumes nation state, protection, dormancy, retirement, pair restriction, account status and first-boundary completion. B-03 owns the states; B-11 applies them at every boundary. Failure `WPF-08`; no mutation of B-03; audit `WPA-41`.

**WEP-622 — `WPC-03` B-04 economy and resources.** *Approved.* Consumes published production, reference prices, shortfall/austerity records and the `REWARD` ledger path. B-04 owns balances and conservation. B-11 writes only reward records; B-04 writes the ledger. Failure `WPF-30`; recovery at W5; audit `WPA-16`.

**WEP-623 — `WPC-04` B-05 cities and infrastructure.** *Approved.* Consumes city count, infrastructure, facility classes, technologies and capstones. B-05 owns the values and the floor. B-11 reads and never mutates. Failure `WPF-23`; audit `WPA-42`.

**WEP-624 — `WPC-05` B-06 population and domestic politics.** *Approved.* Consumes population, housing, stability, approval as a statistic, election and crisis records. `E-POL` uses only named terms through the normal formula and cap. B-06 owns the political state. Failure `WPF-23`; audit `WPA-43`.

**WEP-625 — `WPC-06` B-07 trade and markets.** *Approved.* Consumes only post-gate published trade facts. Before the gate, no trade standing, statistic or volume objective is published. B-07 owns the gate and the transactions. Failure `WPF-35`; audit `WPA-44`.

**WEP-626 — `WPC-07` B-08 diplomacy.** *Approved.* Consumes published agreement facts and counts. There is no reputation value. Positive-only objective conditions. B-08 owns agreement state and consent. Failure `WPF-23`; audit `WPA-45`.

**WEP-627 — `WPC-08` B-09 alliances.** *Approved.* Consumes membership, roles and aggregate-safe counts. `ST-ALL` and `OBJ-ALL` publish only at `k ≥ 5`; no member value, no prize, no command. B-09 owns membership and permissions. Failure `WPF-36`; audit `WPA-46`.

**WEP-628 — `WPC-09` B-10 warfare.** *Approved.* Consumes the permanent campaign record under `WAR-147` and published bands only. B-11 writes the receipt rule WEP-634. No exact force, readiness, inventory, casualty or destruction value. B-10 owns the record. Failure `WPF-37`; audit `WPA-47`.

**WEP-629 — `WPC-10` B-02 history and retention.** *Approved.* B-11 writes class-P records and class-S digest lines under `TR-090`/`TR-092`. B-02 owns compaction. Failure `WPF-38`; audit `WPA-48`.

**WEP-630 — `WPC-11` B-03 reroll and retirement.** *Approved.* B-11 removes current participation and current standing, preserves historical snapshots, forfeits nation-scope objects, preserves account-scope objects that qualify, and writes a public retirement event. B-03 owns the reroll. Failure `WPF-39`; audit `WPA-49`.

**WEP-631 — `WPC-12` B-10 protection and attack prevention.** *Approved.* Every hostile event effect or objective condition passes the same cumulative validator set as a direct action (B-03 pair, B-08 NAP, B-09 Alliance NAP, B-09 same-Alliance ban). A blocked attempt moves nothing. Failure `WPF-33`; audit `WPA-50`.

**WEP-632 — `WPC-13` Prompt 12 moderation.** *Approved.* B-11 supplies evidence, invalid-status records, suspected-manipulation flags, audit references, provisional WSE status and reward hold/correction conditions. Prompt 12 owns enforcement, penalties, appeals and privacy of enforcement. B-11 invents no suspension, ban or penalty.

**WEP-633 — `WPC-14` Prompt 13 interface.** *Approved.* B-11 supplies the concepts and required content for the Events Centre, Objectives and Challenges, Standings, Achievements, National Progress and Reward History. Prompt 13 owns components, layouts, accessibility and navigation. B-11 makes no screen design.

**WEP-634 — `WPC-15` Prompt 14 calibration.** *Approved.* Every threshold, weight, window, cap, interval, payout and band is a calibration parameter owned by Prompt 14. B-11 supplies the structure and the provisional label. Prompt 14 must not change a rule, only a value within its declared range.

**WEP-635 — `WPC-16` Prompt 15 Bible assembly.** *Approved.* B-11 supplies §1–§29, the formula register and the decision/requirement mappings. Prompt 15 assembles; it does not re-specify or renumber B-11.

**WEP-636 — `WPC-17` B-10 receipt rule.** *Approved (WAR-147).* A campaign outcome is received at P6 W1 as a source fact: participation count, defensive outcome band, campaign result and the permanent record ID. It feeds `ST-MIL`, `ST-DEF`, an `OBJ-DEF` or an `EV-COMM`/`E-HIST` record. It never exposes an exact value and never creates a material reward on its own. Formula `F-WEP-027`/`F-WEP-028`; audit `WPA-47`.

**WEP-637 — Contract failure isolation.** *Approved.* A failure in one contract does not corrupt another. Each contract has its own transaction boundary and failure code. A contract failure that prevents a snapshot withholds that standing for the turn; it does not publish a partial rank.

**WEP-638 — Contract privacy.** *Approved.* Each contract states its visibility class. A contract that would expose a private value is rejected at design time; it is not "fixed" by suppression after publication.

## 18. Security, anti-manipulation and fair-play rules

**WEP-639 — Controls, not punishments.** *Approved.* This section defines preventive controls and the evidence B-11 must record. It does not define a penalty. Prompt 12 owns enforcement, investigation, appeals and sanctions.

**WEP-640 — Manipulation register.** *Approved.* The following scenarios are the mandatory design targets. Each row states the control and the evidence owner.

| # | Scenario | B-11 control | Evidence / owner |
|---|---|---|---|
| 1 | Repeated objective farming | One key per instance; repeat cap; no presence reward | Progress keys; Prompt 12 |
| 2 | Achievement farming | Keyed binary grant; closed eligibility; cap | Achievement key; Prompt 12 |
| 3 | Duplicate event participation | One record per `(instance, nation)`; `WPF-14` | Participation key |
| 4 | Duplicate reward claims | Achievement key; first-in-order; dedupe record | Reward key; B-04 ledger |
| 5 | Circular trading | Trade metric blocked pre-gate; net-of-friction post-gate | B-07 gate; Prompt 12 |
| 6 | Artificial trading volume | Relationship/ratio metric; no raw volume | Standing definition; Prompt 12 |
| 7 | Alliance collusion | `k ≥ 5`; no member values; no prize | Aggregate population; Prompt 12 |
| 8 | Multi-account manipulation | B-03 one-account and pair states; no proof by IP alone | B-03; Prompt 12 |
| 9 | Fake contribution | Source fact must be independently owned; no self-report | Source subsystem |
| 10 | Manipulated snapshots | Frozen inputs; sealed snapshot; correction record | Fingerprint; snapshot audit |
| 11 | Score inflation before cut-off | Freeze; windowed rate; published snapshot point | Freeze record; Prompt 12 |
| 12 | Historical-record tampering | Append-only; correction record; no delete | Audit trail |
| 13 | Replay attacks | Keyed idempotency; replay no-op | Idempotency record |
| 14 | Duplicate event generation | Occurrence key; `single_active`; `WPF-05` | Generation audit |
| 15 | Duplicate objective progress | Source event key; `WPF-21` | Progress key |
| 16 | Stale input data | Fingerprint + fail closed; `PROVISIONAL` | Input provenance |
| 17 | Event-trigger manipulation | Edge-triggered; no player-supplied ordering; cap | Trigger record |
| 18 | Repeated season-reset exploitation | No state reset; seasonal scope only; records persist | Season record |
| 19 | Inactive-account leaderboard abuse | Dormancy exclusion is presentation only; window ages out | WSE record; `D-028` |
| 20 | Artificial activity | No presence or action-count reward; state-triggered conditions | Rule design |
| 21 | Reward stacking exploitation | One key per grant; declared max set; `WPF-31` | Reward set audit |
| 22 | Time-window manipulation | Turn/boundary only; no wall-clock; freeze | Timing rule |
| 23 | Deliberate transaction reversal | Reversal before verification removes contribution; after verification is a correction | Reversal record |
| 24 | Invalid or fabricated progress | Authoritative source only; verify at W2; `WPF-22` | Source proof |

**WEP-641 — Idempotency keys.** *Approved.* Every authoritative write has a key and a uniqueness scope:

| Write | Key | Scope | Duplicate behaviour |
|---|---|---|---|
| Event instance | `occurrence_key` | Definition version + discriminator | Return existing; `WPA-25` |
| Participation | `(instance_id, nation_id)` | Instance | Return existing; `WPA-27` |
| Objective instance | `(definition_id, version, nation_id, offer_ordinal)` | Nation + definition | Return existing |
| Progress | `(instance_id, tier_id, source_event_key)` | Instance + tier | Reject; `WPF-21` |
| Completion | `(instance_id, completion_ordinal)` | Instance | Return existing; `WPA-28` |
| Achievement grant | `achievement_key` | Nation + object | Return existing; `WPA-28` |
| Standing snapshot | `(turn_id, standing_id)` | Turn + standing | Return sealed; `WPA-29` |
| Reward | `achievement_key` + `reward_id` | Nation + object | Return existing; `WPA-30` |
| Season transition | `(season_id, transition)` | Season | Return existing |
| Correction | `(corrects_record_id, correction_seq)` | Record | Return existing |

**WEP-642 — Duplicate request behaviour.** *Approved.* A duplicate returns the original outcome, not an error to the player, unless the duplicate is an invalid attempt (for example, a second participation while one is active). The audit distinguishes an idempotent replay from an invalid duplicate.

**WEP-643 — Atomicity.** *Approved.* These operations are one transaction: objective completion + recognition; achievement grant + reward entitlement; reward grant + ledger event; snapshot seal + rank order; event completion + result + reward record; season close + reset + archive; correction + reference. A partial write is prohibited.

**WEP-644 — Snapshot protection.** *Approved.* A snapshot is sealed before publication. A published snapshot cannot be recalculated in place. A correction is a new snapshot with the original preserved. The input cutoff is the P6 W3 baseline.

**WEP-645 — Snapshot version.** *Approved.* Each snapshot records the standing definition version and the source version. A definition change starts a new series; it does not reinterpret old snapshots.

**WEP-646 — Seal integrity.** *Approved.* The seal covers the input values, the fingerprint, the denominator, the rank order and the tie group. A mismatch on reopen is an integrity failure; the snapshot is withheld and investigated.

**WEP-647 — Privacy levels.** *Approved.* B-11 uses B-02's classes: `PUBLIC`, `NATION_OWNER`, `PARTICIPANT`, `ALLIANCE_MEMBER`, `ALLIANCE_OFFICER`, `MODERATOR`, `ADMIN`, `INTERNAL`. A field has exactly one class. An aggregate uses `k ≥ 5`.

**WEP-648 — Visibility matrix.** *Approved.*

| Object | Owner | Participant | Other nation | Alliance member | Alliance officer | Public | Moderator | Admin |
|---|---|---|---|---|---|---|---|---|
| Event definition | Yes | Yes | Yes | Yes | Yes | Published fields | Yes | Yes |
| Event participation | Yes | Yes (own) | Aggregate only | Aggregate only | Aggregate only | Aggregate at `k≥5` | Yes | Yes |
| Objective offer | Yes | — | No | No | No | No | Yes | Yes |
| Objective progress | Yes | — | No | No | No | Only if definition public | Yes | Yes |
| Standing snapshot | Yes | Yes | Public | Public | Public | Yes | Yes | Yes |
| Private achievement | Yes | — | No | No | No | No | Yes | Yes |
| Material reward | Yes | — | No | No | No | Disclosed class only | Yes | Yes |
| Audit event | — | — | No | No | No | No | Yes | Yes |

**WEP-649 — No new threshold.** *Approved.* A B-11 aggregate uses `k = 5`. A "small group" or "sensitive" exception is not invented; it is a Prompt 12 or owner matter.

**WEP-650 — Differencing.** *Approved.* B-11 must not publish two figures whose difference isolates a nation below `k`. Complementary suppression is applied to the published set, not only to the individual figure.

**WEP-651 — Military privacy.** *Approved.* `ST-MIL` and `ST-DEF` publish bands and counts only. An exact force value is never a B-11 field, even internally for display. The owning B-10 value is read only to compute a band.

**WEP-652 — Wealth privacy.** *Approved.* A wealth estimate may be displayed only as a labelled estimate with no private balance. The `ST-ECO` metric is output-based, not wealth-based.

**WEP-653 — Diplomatic privacy.** *Approved.* `ST-DIP` uses published acts and counts. It does not reveal a private proposal, a pending act or a private message.

**WEP-654 — Alliance privacy.** *Approved.* `ST-ALL` publishes only the aggregate and the population. It never lists a member contribution. A member's own contribution is visible to that member and to an authorized officer under B-09's permissions.

**WEP-655 — Moderation boundary.** *Approved.* B-11 flags, records and defers. It does not suspend, ban, mute, confiscate or publicly shame. A Prompt 12 hold is recorded as `SUSPENDED` or `EXCLUDED` with an evidence ID, not as a B-11 punishment.

**WEP-656 — Access control.** *Approved.* A B-11 write is authorized by the acting system step and the object's owner. A player may write only an acceptance, a dismissal, a withdrawal, a claim or a challenge creation for their own nation. An administrator may not write a grant or a snapshot; corrections use the correction path.

**WEP-657 — Auditability.** *Approved.* Every security-relevant decision (eligibility exclusion, freeze rejection, duplicate rejection, deferral, suspension, correction) writes a `WPA-` event with the rule ID and the evidence reference.

**WEP-658 — No hidden advantage.** *Approved.* No B-11 control may grant a hidden advantage to a cohort, an alliance, an operator or a developer. A control that cannot be published is invalid.

---

## 19. Privacy

**WEP-659 — D-027 is the only threshold.** *Approved.* `k = 5`, complementary suppression and the no-differencing rule apply to every B-11 aggregate. B-11 adds no threshold and no exception.

**WEP-660 — Individual ranking is not an aggregate.** *Approved (TR-020).* A nation's own public rank is a statement about that nation, not a group statistic. It may be published without `k`, provided the underlying value is already public under its owning subsystem's class.

**WEP-661 — Private by default for offers.** *Approved.* An objective offer and its progress are owner-visible by default. A public objective must declare its public fields explicitly.

**WEP-662 — Event participant lists.** *Approved.* A public event may publish participant names only if participation is public by definition. A challenge participant list is parties-only. An Alliance event publishes an aggregate at `k ≥ 5`.

**WEP-663 — Reward disclosure.** *Approved.* A material reward notice states the class, quantity and key to the owner. It never states another nation's reward. A public "recent rewards" list uses only disclosed public rewards and respects `k`.

**WEP-664 — Historical privacy.** *Approved.* A historical record retains the visibility class it had at publication. A later privacy change is applied by a disclosed redaction overlay, not by rewriting the record.

**WEP-665 — Moderation data.** *Approved.* A B-11 evidence record is restricted to `MODERATOR`/`ADMIN`. It is not part of a public profile. Prompt 12 owns the retention of enforcement evidence.

**WEP-666 — No enumeration.** *Approved (REQ-094).* A B-11 message must not let a player enumerate another nation's private state through error text, counts or timing.

---

## 20. Error and exception model

**WEP-667 — Code namespace.** *Approved.* B-11 failure codes use `WPF-01`…`WPF-40`. The namespace is new and does not reuse `WRF-`, `ALF-`, `DPF-` or any other subsystem code. The `WRF-15`–`WRF-19` gaps remain unfilled.

**WEP-668 — Code fields.** *Approved.* Each code states: identifier; condition; trigger; validation owner; state impact; no-mutation guarantee; reservation outcome; audit event; retry eligibility; recovery; player-facing meaning; administrative visibility.

**WEP-669 — Failure catalogue.** *Approved.*

| Code | Condition | State impact | Reservation | Retry | Player meaning |
|---|---|---|---|---|---|
| `WPF-01` | Invalid or incomplete definition | Definition not published | None | After correction | "This event/objective is not available." |
| `WPF-02` | Class–trigger mismatch or invalid class | Instance not created | None | No | "This event could not be generated." |
| `WPF-03` | Invalid parameter or out of range | Instance not created | None | After correction | "The event rules are incomplete." |
| `WPF-04` | Definition retired or superseded | No new instance | None | No | "This event is no longer offered." |
| `WPF-05` | Duplicate occurrence key | Existing instance returned | None | Idempotent | "This event already exists." |
| `WPF-06` | Invalid boundary arithmetic | Not scheduled | None | After correction | "The timing could not be set." |
| `WPF-07` | Announcement/visibility failure | Not announced | None | Next turn | "This event could not be announced." |
| `WPF-08` | Ineligible participant or target | No participation | Released | After state change | "You are not eligible for this event." |
| `WPF-09` | Closing boundary invalid | Stays ACTIVE | None | Next turn | "The event could not close yet." |
| `WPF-10` | Challenge independence failure | No claim | Released | No | "This challenge cannot be claimed by you." |
| `WPF-11` | Duplicate active challenge | No second challenge | Released | After expiry | "An identical challenge is already open." |
| `WPF-12` | Teardown boundary invalid | Stays CLOSED | None | Next turn | "The event is still being closed." |
| `WPF-13` | Invalid state transition | No change | None | No | "That action is not possible now." |
| `WPF-14` | Duplicate participation | Existing record returned | None | Idempotent | "You are already taking part." |
| `WPF-15` | Action after participation freeze | No change | Released | No | "This event is closed for new actions." |
| `WPF-16` | Effect validation failure | No effect | Released | After correction | "The event effect could not be applied." |
| `WPF-17` | Missing inertness statement | Definition incomplete | None | After correction | "This event is not fully specified." |
| `WPF-18` | Completion verification failure | Stays CLOSED | None | After correction | "The result could not be verified yet." |
| `WPF-19` | Objective unavailable or invalid transition | No change | None | No | "This objective is not available." |
| `WPF-20` | Objective ineligible / late acceptance | No acceptance | None | No | "This objective closed before you accepted." |
| `WPF-21` | Duplicate progress source | No increment | None | Idempotent | "This progress was already counted." |
| `WPF-22` | Invalid completion evidence | Returns IN_PROGRESS | None | After correction | "We could not verify this completion." |
| `WPF-23` | Source unavailable, stale or inconsistent | No progress this turn | None | Next turn | "The system could not check this yet." |
| `WPF-24` | Objective expired | EXPIRED | Released | No | "This objective has ended." |
| `WPF-25` | Objective withdrawn | WITHDRAWN | Released | No | "This objective was withdrawn; your record is kept." |
| `WPF-26` | Objective superseded by a mechanic change | SUPERSEDED | Released | New offer | "This objective was replaced." |
| `WPF-27` | Achievement condition not met | No grant | None | Later | "This achievement is not yet complete." |
| `WPF-28` | Achievement already granted | Existing grant returned | None | Idempotent | "You already have this achievement." |
| `WPF-29` | Standing input invalid | Standing withheld | None | Next turn | "This ranking is not available this turn." |
| `WPF-30` | Reward unavailable or grant failed | DEFERRED | Preserved | W5 | "Your reward is held and will be retried." |
| `WPF-31` | Undeclared reward stacking | No grant | Preserved | After correction | "This reward combination is not allowed." |
| `WPF-32` | Evidence hold or suspension | SUSPENDED/EXCLUDED | Preserved | Review | "This is under review; nothing is lost." |
| `WPF-33` | Protection or attack-prevention block | No effect | Released | No | "This action is not allowed against that nation." |
| `WPF-34` | Score/definition version conflict | No snapshot | None | After correction | "This ranking could not be calculated." |
| `WPF-35` | Global Trade gate unmet | No publication | None | No (gate) | "Trade rankings are not available." |
| `WPF-36` | Aggregate below `k = 5` | Withheld | None | No | "This group is too small to publish." |
| `WPF-37` | Military/privacy value exposure | Withheld/coarsened | None | No | "This figure cannot be shown." |
| `WPF-38` | Record retention conflict | Record stays permanent | None | No | "This record is permanent." |
| `WPF-39` | Reroll/retirement cleanup conflict | No partial cleanup | None | Recovery | "Your nation history is being finalised." |
| `WPF-40` | Phase, checkpoint or replay conflict | Turn INTERRUPTED | Released | Recovery | "The turn was interrupted; it will resume." |

**WEP-670 — Retry semantics.** *Approved.* A retry uses the same key and the same frozen inputs. A retry after a state change revalidates from the beginning; it does not resume mid-transition.

**WEP-671 — Recovery semantics.** *Approved.* A `WPF-40` failure resumes from the last W-step checkpoint. A `WPF-30` deferral is retried at W5. A `WPF-22` returns the objective to `IN_PROGRESS` and never marks it complete.

**WEP-672 — Player-facing meaning.** *Approved.* A player message states the outcome, the rule and the next step. It does not expose a private value or an internal identifier that enables enumeration.

**WEP-673 — Administrative visibility.** *Approved.* An operator console may see the code, object ID, turn, key and evidence reference. It may not see a private balance or an exact military value that B-11 itself may not store.

**WEP-674 — No fabricated code.** *Approved.* `WPF-01`…`WPF-40` are the complete B-11 set. A new code requires a decision and a register row. A code is never reused.

---

## 21. Audit events and history

**WEP-675 — Audit namespace.** *Approved.* B-11 audit events use `WPA-01`…`WPA-50`. They are append-only, immutable and write inside the transaction that causes them.

**WEP-676 — Audit catalogue.** *Approved.*

| ID | Event | ID | Event |
|---|---|---|---|
| `WPA-01` | DEFINITION_PUBLISHED | `WPA-26` | OBJECTIVE_WITHDRAWN |
| `WPA-02` | DEFINITION_SUPERSEDED | `WPA-27` | OBJECTIVE_SUPERSEDED |
| `WPA-03` | DEFINITION_RETIRED | `WPA-28` | DUPLICATE_COMPLETION_REJECTED |
| `WPA-04` | EVENT_QUALIFIED | `WPA-29` | SNAPSHOT_DUPLICATE_RETURNED |
| `WPA-05` | EVENT_SCHEDULED | `WPA-30` | DUPLICATE_CLAIM_REJECTED |
| `WPA-06` | EVENT_ANNOUNCED | `WPA-31` | PARTICIPATION_SUSPENDED |
| `WPA-07` | EVENT_ACTIVATED | `WPA-32` | PARTICIPATION_RELEASED |
| `WPA-08` | EVENT_CLOSED | `WPA-33` | PARTICIPATION_DISQUALIFIED |
| `WPA-09` | EVENT_EFFECT_APPLIED | `WPA-34` | REWARD_DEFERRED |
| `WPA-10` | EVENT_COMPLETED | `WPA-35` | REWARD_RECHECKED |
| `WPA-11` | EVENT_EXPIRED | `WPA-36` | SNAPSHOT_CORRECTED |
| `WPA-12` | EVENT_CANCELLED | `WPA-37` | RECORD_CORRECTED |
| `WPA-13` | EVENT_VOIDED | `WPA-38` | RECORD_REDACTED |
| `WPA-14` | PARTICIPATION_JOINED | `WPA-39` | SEASON_OPENED |
| `WPA-15` | PARTICIPATION_WITHDRAWN | `WPA-40` | PHASE_CHECKPOINT |
| `WPA-16` | REWARD_GRANTED | `WPA-41` | ELIGIBILITY_EVALUATED |
| `WPA-17` | OBJECTIVE_OFFERED | `WPA-42` | DEVELOPMENT_INPUT_READ |
| `WPA-18` | OBJECTIVE_DISMISSED | `WPA-43` | POLITICAL_TERM_READ |
| `WPA-19` | OBJECTIVE_ACCEPTED | `WPA-44` | TRADE_INPUT_BLOCKED |
| `WPA-20` | OBJECTIVE_PROGRESS | `WPA-45` | DIPLOMATIC_FACT_READ |
| `WPA-21` | OBJECTIVE_TIER_REACHED | `WPA-46` | ALLIANCE_AGGREGATE_PUBLISHED |
| `WPA-22` | OBJECTIVE_PENDING_VALIDATION | `WPA-47` | WAR_RECEIPT_RECORDED |
| `WPA-23` | OBJECTIVE_VERIFIED | `WPA-48` | HISTORY_RECORD_WRITTEN |
| `WPA-24` | OBJECTIVE_REWARD_PENDING | `WPA-49` | RETIREMENT_CLEANUP |
| `WPA-25` | OBJECTIVE_EXPIRED | `WPA-50` | SECURITY_BLOCK_RECORDED |

**WEP-677 — Audit content.** *Approved.* An audit event records the event ID, turn, phase, object ID, object type, key, rule ID, actor (system/player/operator), before/after reference, reason code and visibility.

**WEP-678 — Audit immutability.** *Approved.* An audit event is never edited or deleted. A correction references it.

**WEP-679 — Audit privacy.** *Approved.* The audit stream is `MODERATOR`/`ADMIN` only. A player sees the player-facing message and, where applicable, the public record, not the audit row.

**WEP-680 — History class.** *Approved (TR-090).* Event, objective, standing, achievement and honour records are class P. Routine progress lines are class S and compact under B-02's retention. Audit is the permanent spine.

**WEP-681 — Chronicle notability.** *Approved (D-158, resolves UD-024).* The chronicle records a fact when it is (a) a permanent event, campaign, agreement or alliance record already class P; (b) a change of rank 1 or of published top-10 membership in a competitive standing; (c) a granted honour or world-first; (d) a season opening, closing or champion; (e) a correction or redaction of a permanent record; or (f) a published world-state anchor. Each entry states what, who (public identity), when (turn and UTC), the rule ID and the source record. One sentence, no speculation, no narrative beyond the record.

**WEP-682 — Chronicle corrections.** *Approved.* A chronicle correction appends a new entry referencing the original. The original remains. A redaction is a disclosed overlay, never a deletion.

---

## 22. Formula register references

**WEP-683 — Formula families.** *Approved.* The register defines formulas in five families: event (`F-WEP-001`…`F-WEP-014`), objective (`F-WEP-015`…`F-WEP-026`), standing (`F-WEP-027`…`F-WEP-038`), progression (`F-WEP-039`…`F-WEP-044`) and reward/history (`F-WEP-045`…`F-WEP-050`). The exact inventory is the register's §1. `F-WEP-048` is a retired ID in that family: it has no active calculation and no active rule reference (11B-C2; progress log §70).

**WEP-684 — Every reference resolves.** *Approved.* A `F-WEP-` reference in this document must exist in the register. A formula in the register must be referenced by at least one rule or by its family declaration. An orphan is a validator failure.

**WEP-685 — No conflicting expression.** *Approved.* This document never states a second expression for a formula. If prose and register differ, the register governs.

**WEP-686 — Calibration ownership.** *Approved.* Every formula's field 20 names Prompt 14 as calibration owner unless the value is structural or owner-reserved. No B-11 number is presented as balanced.

---

## 23. Requirements and traceability

**WEP-687 — Requirement allocation.** *Approved.* B-11 adopts the thirty `11A-CR` candidate requirements as `REQ-704`…`REQ-733`, with the modifications stated in the table below, and adds thirty specification requirements `REQ-734`…`REQ-763` for contracts, security, privacy, failure and record integrity. `REQ-704` onward is the only new global range; no earlier requirement is renumbered.

**WEP-688 — Candidate-requirement disposition.** *Approved.*

| Candidate | Disposition | Requirement | Note |
|---|---|---|---|
| `11A-CR-001` | DIRECT SPECIFICATION | `REQ-704` | Systemic P6 generation |
| `11A-CR-002` | DIRECT SPECIFICATION | `REQ-705` | Parameter-row definition |
| `11A-CR-003` | DIRECT SPECIFICATION | `REQ-706` | Protected/dormant/new-nation event eligibility |
| `11A-CR-004` | ADAPTED | `REQ-707` | Relative band is a structure; bounds are Prompt 14, not a fixed constant |
| `11A-CR-005` | DIRECT SPECIFICATION | `REQ-708` | Named published-input effect |
| `11A-CR-006` | DIRECT SPECIFICATION | `REQ-709` | Effect prohibitions |
| `11A-CR-007` | DIRECT SPECIFICATION | `REQ-710` | Two-stage teardown |
| `11A-CR-008` | DIRECT SPECIFICATION | `REQ-711` | Challenge reservation and independence |
| `11A-CR-009` | DIRECT SPECIFICATION | `REQ-712` | Optional objectives and prohibitions |
| `11A-CR-010` | DIRECT SPECIFICATION | `REQ-713` | State-referenced conditions |
| `11A-CR-011` | DIRECT SPECIFICATION | `REQ-714` | Declared, terminal lifecycle |
| `11A-CR-012` | DIRECT SPECIFICATION | `REQ-715` | Material-reward conditions |
| `11A-CR-013` | DIRECT SPECIFICATION | `REQ-716` | Milestones are records |
| `11A-CR-014` | DIRECT SPECIFICATION | `REQ-717` | Plural standings, no dominant ladder |
| `11A-CR-015` | DIRECT SPECIFICATION | `REQ-718` | Standing declaration fields |
| `11A-CR-016` | DIRECT SPECIFICATION | `REQ-719` | Dormancy presentation exclusion |
| `11A-CR-017` | DIRECT SPECIFICATION | `REQ-720` | `k = 5` aggregation |
| `11A-CR-018` | DIRECT SPECIFICATION | `REQ-721` | No exact military value |
| `11A-CR-019` | DIRECT SPECIFICATION | `REQ-722` | Approval and welfare are statistics only |
| `11A-CR-020` | DIRECT SPECIFICATION | `REQ-723` | Diplomatic counts, no reputation |
| `11A-CR-021` | DIRECT SPECIFICATION | `REQ-724` | Trade publication blocked before gate |
| `11A-CR-022` | DIRECT SPECIFICATION | `REQ-725` | Season resets ladders only |
| `11A-CR-023` | DIRECT SPECIFICATION | `REQ-726` | Derived, non-compounding progression |
| `11A-CR-024` | DIRECT SPECIFICATION | `REQ-727` | Nation/account scope |
| `11A-CR-025` | DIRECT SPECIFICATION | `REQ-728` | Tenure commemorated, not ranked |
| `11A-CR-026` | DIRECT SPECIFICATION | `REQ-729` | Turns and named boundaries |
| `11A-CR-027` | DIRECT SPECIFICATION | `REQ-730` | Explicit player sovereignty |
| `11A-CR-028` | DIRECT SPECIFICATION | `REQ-731` | Existing bounded digest |
| `11A-CR-029` | DIRECT SPECIFICATION | `REQ-732` | Append-only chronicle |
| `11A-CR-030` | DIRECT SPECIFICATION | `REQ-733` | Parameter classification |

**WEP-689 — Additional specification requirements.** *Approved.*

| Requirement | Meaning |
|---|---|
| `REQ-734` | Event taxonomy is exactly four classes and five triggers (WEP-071…WEP-082) |
| `REQ-735` | Event definition and instance fields are mandatory and version-pinned (WEP-083…WEP-098) |
| `REQ-736` | Event lifecycle is the nine-state machine with two-stage teardown (WEP-099…WEP-116) |
| `REQ-737` | Event generation is deterministic, keyed and occurrence-capped (WEP-117…WEP-131) |
| `REQ-738` | Event eligibility is revalidated at six boundaries (WEP-132…WEP-144) |
| `REQ-739` | Explicit participation, withdrawal and freeze rules (WEP-145…WEP-156) |
| `REQ-740` | Effect catalogue is closed and owned by the mutating subsystem (WEP-157…WEP-180) |
| `REQ-741` | Completion, expiry, voiding and history are append-only (WEP-181…WEP-202) |
| `REQ-742` | Objective categories are exactly twelve, with rejected categories recorded (WEP-203…WEP-219) |
| `REQ-743` | Objective definitions declare source, window and inertness (WEP-220…WEP-231) |
| `REQ-744` | Objective lifecycle is the thirteen-state machine; `FAILED` is not a state (WEP-232…WEP-253) |
| `REQ-745` | Acceptance is explicit; auto-tracking is recognition-only (WEP-254…WEP-264) |
| `REQ-746` | Progress is keyed, authoritative and non-retroactive (WEP-265…WEP-280) |
| `REQ-747` | Verification, correction and replay rules (WEP-281…WEP-290) |
| `REQ-748` | Alliance standing and collective-objective publication is withheld pending UD-050 (WEP-335, WEP-379) — **Open** |
| `REQ-749` | Standing catalogue is exactly ten, with no overall composite (WEP-326…WEP-339, WEP-362…WEP-366) |
| `REQ-750` | Snapshot is one per standing per turn, sealed and immutable (WEP-381…WEP-391) |
| `REQ-751` | Tie-break hierarchy is shared rank → secondary → earlier sustained → seeded (WEP-392…WEP-399) |
| `REQ-752` | Material reward rarity bound is defined by Prompt 14 under UD-051 (WEP-504, WEP-542) — **Open** |
| `REQ-753` | Progression layers are eight and non-compounding (WEP-423…WEP-486) |
| `REQ-754` | Achievement, milestone and honour object model is fixed (WEP-487…WEP-498) |
| `REQ-755` | Reward classes are six and material grants are ledgered (WEP-499…WEP-514) |
| `REQ-756` | Reward eligibility and claim/deferral rules preserve entitlement (WEP-515…WEP-536) |
| `REQ-757` | Reward conservation, caps and no-second-treasury rules (WEP-537…WEP-547) |
| `REQ-758` | Reward stacking is keyed and bound (WEP-548…WEP-556) |
| `REQ-759` | Eligibility model is shared and reads B-03 (WEP-557…WEP-566) |
| `REQ-760` | Twelve state machines and their invalid transitions are specified (WEP-567…WEP-584) |
| `REQ-761` | P6 W1–W5 order and P7 publication are mandatory (WEP-605…WEP-618) |
| `REQ-762` | Contracts WPC-01…WPC-17 exist for B-02…B-10 and Prompts 12–15 (WEP-619…WEP-638) |
| `REQ-763` | Failure codes, audit events and privacy matrix are complete (WEP-639…WEP-682) |

**WEP-690 — Bidirectional traceability.** *Approved.* Every new `WEP-` rule points to a decision, a requirement, a source research row or a documented Category B rationale in §24. Every `REQ-704`…`REQ-763` row points to at least one `WEP-` rule. Every `11A-CR` and `11A-OPEN` row has a disposition. An unexplained orphan is a validator failure.

**WEP-691 — Research-question disposition.** *Approved.*

| Open question | Disposition | Where |
|---|---|---|
| `11A-OPEN-001` | NOT APPLICABLE (research gap; no B-11 rule depends on it) | §23 |
| `11A-OPEN-002` | NOT APPLICABLE (research gap) | §23 |
| `11A-OPEN-003` | DEFERRED — Prompt 14 | `F-WEP-031` calibration |
| `11A-OPEN-004` | DEFERRED — Prompt 12/14, `UD-050` | WEP-379 |
| `11A-OPEN-005` | RESOLVED — in-place seasons | WEP-465…WEP-476 |
| `11A-OPEN-006` | DEFERRED — Prompt 14 | `F-WEP-028` |
| `11A-OPEN-007` | RESOLVED — `ST-CIV` institutional continuity | WEP-331 |
| `11A-OPEN-008` | DEFERRED — Prompt 13 | §27 |
| `11A-OPEN-009` | RESOLVED — disclosed closure preferred; world-state preferred | WEP-464, WEP-481 |
| `11A-OPEN-010` | RESOLVED — no `WRA-` reuse | WEP-019 |
| `11A-OPEN-011` | DEFERRED — Prompt 12/14, `UD-050` | WEP-379 |
| `11A-OPEN-012` | DEFERRED — Prompt 14, `UD-051` | WEP-542 |
| `11A-OPEN-013` | RESOLVED — chronicle bar | WEP-681 |
| `11A-OPEN-014` | RESOLVED — band-only defensive recognition | WEP-211, WEP-334 |
| `11A-OPEN-015` | DEFERRED — Prompt 12/13 | §27 |
| `11A-OPEN-016` | DEFERRED — Prompt 13 | §27 |

**WEP-692 — Existing requirements.** *Approved.* B-11 accounts for the inherited requirements named in §23.2 of the research baseline and does not duplicate them. A requirement already owned by B-02…B-10 is cited, not re-created.

### 23.1 11A recommendation disposition

**11A recommendation disposition.** Every one of the 34 `11A-DR` recommendations has a recorded disposition. `ADOPTED` means the named rules carry the direction; `REJECTED` means the direction is excluded by a named rule or decision; `NOT APPLICABLE` means the owning subsystem already supplies the authority and B-11 must not restate it.

| Recommendation | Disposition | Where |
|---|---|---|
| `11A-DR-001` | ADOPTED — systemic parameter-row generation | WEP-071…WEP-098 |
| `11A-DR-002` | ADOPTED — fixed intra-P6 order | WEP-050 |
| `11A-DR-003` | ADOPTED — relative-band eligibility | WEP-132…WEP-145 |
| `11A-DR-004` | ADOPTED — two-stage teardown | WEP-185 |
| `11A-DR-005` | ADOPTED — bounded queue and cadence, no content pressure | WEP-123, WEP-131, WEP-148 |
| `11A-DR-006` | ADOPTED — frozen snapshot and draw integrity | WEP-034, WEP-035, WEP-155 |
| `11A-DR-007` | ADOPTED — reservation, expiry and independence | WEP-075, WEP-091…WEP-096 |
| `11A-DR-008` | ADOPTED — keyed achievement register | WEP-433…WEP-445 |
| `11A-DR-009` | ADOPTED — explicit acceptance and penalty-free dismissal | WEP-234, WEP-256 |
| `11A-DR-010` | ADOPTED — plural standings plus separate eligibility | WEP-317…WEP-335 |
| `11A-DR-011` | ADOPTED — honour-only alliance aggregates | WEP-335, WEP-379, WEP-627 |
| `11A-DR-012` | ADOPTED — purchased recognition banned | WEP-068 |
| `11A-DR-013` | ADOPTED — five distinct recognition objects | WEP-025 |
| `11A-DR-014` | ADOPTED — one completion, several keyed objects | WEP-432, WEP-488 |
| `11A-DR-015` | ADOPTED — participation and defensive bands only | WEP-211, WEP-334 |
| `11A-DR-016` | ADOPTED — disclosed closure preferred; world-state anchors | WEP-098, WEP-464 |
| `11A-DR-017` | ADOPTED — derived records, no level or currency | WEP-423…WEP-432 |
| `11A-DR-018` | ADOPTED — season resets seasonal standings only | WEP-415 |
| `11A-DR-019` | ADOPTED — windowed rates and published inputs | WEP-342, WEP-401 |
| `11A-DR-020` | ADOPTED — earlier sustained position as a published tie-break | WEP-394, WEP-401 |
| `11A-DR-021` | ADOPTED — published eligibility floors and entry closure | WEP-377, WEP-378 |
| `11A-DR-022` | REJECTED — no contested-objective class; offensive categories are excluded | D-155, WEP-203 |
| `11A-DR-023` | ADOPTED — factual counts, no reputation score | WEP-331, WEP-332 |
| `11A-DR-024` | ADOPTED — free parallel paths and explicit choice | WEP-031, WEP-256 |
| `11A-DR-025` | ADOPTED — several published inputs, no single damage counter | WEP-334, WEP-448 |
| `11A-DR-026` | ADOPTED — reuse the existing calendar, invent no second one | WEP-073, WEP-082 |
| `11A-DR-027` | ADOPTED — separate descriptive and competitive layers | WEP-320 |
| `11A-DR-028` | NOT APPLICABLE — B-06 owns office authority; B-11 restates no B-06 power | WEP-007 |
| `11A-DR-029` | ADOPTED — one parameterised objective container | WEP-052, WEP-203 |
| `11A-DR-030` | ADOPTED — capstone recognition, no new wonder mechanic | WEP-457 |
| `11A-DR-031` | ADOPTED — geometric thresholds with an open tail | WEP-449 |
| `11A-DR-032` | ADOPTED — authorship as the highest reward class | WEP-054, WEP-430 |
| `11A-DR-033` | ADOPTED — inertness disclosure in every definition | WEP-180, WEP-493 |
| `11A-DR-034` | ADOPTED — small optional achievement layer | WEP-445 |

**WEP-692a — Rule-family traceability matrix.** *Approved.* Every rule belongs to exactly one family below. The family supplies the six traceability links; a rule paragraph also names a specific decision or requirement where one exists. This is the reverse map used by the validator; a range gap or an empty cell is an orphan.

| Rule range | Family | Research / decision | Requirement | Formula | Owning subsystem | Contract | Failure / control |
|---|---|---|---|---|---|---|---|
| `WEP-001`–`014` | Purpose and authority | D-014, D-152 | `REQ-730` | `F-WEP-000a` | B-11 | `WPC-01` | `WPF-40` |
| `WEP-015`–`038` | Terminology and architecture | D-153, D-144 | `REQ-734` | `F-WEP-001` | B-11 | `WPC-01` | `WPF-13` |
| `WEP-039`–`054` | Architecture and shared rules | D-146…D-151 | `REQ-717` | `F-WEP-027` | B-11 | `WPC-10` | `WPF-29` |
| `WEP-055`–`070` | Fixed constraints | D-014, D-027, D-122 | `REQ-720`, `REQ-724` | `F-WEP-049` | B-02…B-10 | `WPC-02` | `WPF-33`, `WPF-35` |
| `WEP-071`–`202` | Domain A — world events | D-146, D-154 | `REQ-704`–`741` | `F-WEP-001`–`014` | B-11, B-02, B-03 | `WPC-01` | `WPF-05`, `WPF-15` |
| `WEP-203`–`316` | Domain B — objectives | D-147, D-155 | `REQ-742`–`747` | `F-WEP-015`–`026` | B-11, B-04…B-10 | `WPC-03` | `WPF-19`, `WPF-22` |
| `WEP-317`–`422` | Domain C — standings | D-148, D-156 | `REQ-717`–`721`, `REQ-749` | `F-WEP-027`–`038` | B-11, B-02, B-04…B-10 | `WPC-09` | `WPF-29`, `WPF-36` |
| `WEP-423`–`486` | Domain D — progression | D-149, D-157 | `REQ-726`–`728`, `REQ-753` | `F-WEP-039`–`044` | B-11, B-03, B-05 | `WPC-11` | `WPF-27` |
| `WEP-487`–`498` | Recognition object model | D-149, D-158 | `REQ-716`, `REQ-754` | `F-WEP-039`–`042` | B-11 | `WPC-10` | `WPF-27` |
| `WEP-499`–`556` | Rewards | D-151, D-159 | `REQ-715`, `REQ-755`–`758` | `F-WEP-045`–`047`, `F-WEP-049` | B-04, B-09, B-11 | `WPC-03` | `WPF-30`, `WPF-31` |
| `WEP-557`–`584` | Eligibility and state machines | D-014, D-027 | `REQ-759`, `REQ-760` | `F-WEP-002`, `F-WEP-028` | B-03, B-11 | `WPC-02` | `WPF-13`, `WPF-14` |
| `WEP-585`–`618` | Calculation and turn processing | D-150, D-152 | `REQ-761` | `F-WEP-050` | B-02, B-11 | `WPC-01` | `WPF-40` |
| `WEP-619`–`638` | Cross-system contracts | D-144, D-150 | `REQ-762` | all `F-WEP-` | B-02…B-10, Prompts 12–15 | `WPC-01`–`17` | `WPF-40` |
| `WEP-639`–`682` | Security, privacy and audit | D-027, D-151 | `REQ-720`, `REQ-763` | `F-WEP-049` | B-02, B-11, Prompt 12 | `WPC-13` | `WPF-32`, `WPF-33` |
| `WEP-683`–`723` | Registers and acceptance | D-144…D-161, DD-192…DD-209 | `REQ-704`–`763` | all `F-WEP-` | B-11, Prompts 11C–15 | `WPC-16` | `WPF-40` |

---

## 24. Decision register and conflicts

**WEP-693 — Decision handling.** *Approved.* D-144…D-151 are approved design directions; 11B implements them as rules and records the additional Category B decisions D-152…D-161. No 11A direction is reversed. DD-192, DD-193, DD-194, DD-195, DD-196, DD-197, DD-198 and DD-199 are mirrored as DD-200…DD-209 for the new decisions.

**WEP-694 — New Category B decisions.** *Approved.*

| ID | Title | Problem | Selected option | Alternatives rejected | Rationale / evidence | Dependencies | Consequences | Confidence | Reopening condition |
|---|---|---|---|---|---|---|---|---|---|
| `D-152` | Canonical path and B-11 identifier namespace | D-144 left the path to be confirmed; no B-11 IDs existed | Canonical path `18_world_events_objectives_rankings_progression.md`; identifiers `WEP-`, `F-WEP-`, `WPC-`, `WPA-`, `WPF-` | `18_world_events_and_progression.md`; reusing `WAR-`/`F-WR-` | Descriptive name matches the four domains and the 11A title; namespaces checked free | D-144, D-145 | All later links and validators use these IDs | High | A repository convention change |
| `D-153` | Terminology: national objective | B-10 already uses "objective" for a campaign objective; `WRA-06` collides | B-11 uses "national objective"/"strategic objective"; campaign objective stays B-10; no `WRA-06` reuse | Unqualified "objective"; a second event taxonomy | `11A-INT-32`, `WAR-006` | WEP-018…WEP-020 | Removes the vocabulary collision | High | None foreseen |
| `D-154` | Event system | Nine candidate classes and a fifteen-stage lifecycle needed a coherent cut | Four classes (`EV-CAL`, `EV-STATE`, `EV-CHAL`, `EV-COMM`), five triggers, nine states, two-stage teardown, P6 W1 | Global-only; seasonal-only; bespoke content | D-146; `AP-003`; `11A-DR-001`…`007` | WEP-071…WEP-202 | One machinery, bounded content | High on structure; Low on values | New evidence on challenge-class abuse |
| `D-155` | Objective system | Forced sequences harm players; the sixteen categories needed legality verdicts | Twelve categories; optional by default; thirteen states; explicit acceptance; state-triggered progress; rejection of offensive and community categories | Sequential mandatory chain; daily obligations; one long track | D-147; `11A §13`; `NAT-051`/`NAT-052` | WEP-203…WEP-316 | Playable plurality, no chores | High on structure; Low on difficulty | New player-behaviour evidence |
| `D-156` | Standing system | One score couples balance and fairness; approval/welfare cannot be ranked | Ten standings; separate WSE; no overall composite; `ST-CIV` institutional continuity; tie hierarchy | One score; weighted composite headline; wealth rank | D-148; `11A-BM-001`; `DMP-051` | WEP-317…WEP-422 | Plural, non-gating recognition | High on separation; Low on weights | Prompt 14 simulation |
| `D-157` | Progression system | Levels and prestige currencies create runaway leaders | Eight derived layers; small achievement set; no prestige currency; records as spine; authorship top reward | RPG level; prestige currency; maximal checklist | D-149; `ECN-092`; `FO-024` | WEP-423…WEP-498 | Durable identity without power | High on structure; Medium on authorship | A new reward-class proposal |
| `D-158` | Chronicle quality bar (resolves UD-024) | UD-024 was deferred to Prompt 11 with no stated bar | WEP-681 notability list; one-sentence entries; source, turn, rule; append-only | Full narrative feed; per-action history; silent editorial selection | 11A §12.3, §14.6; `11A-OPEN-013`; `TR-090` | UD-024, WEP-681 | A testable, low-cost chronicle | High | Prompt 13 retention evidence |
| `D-159` | Reward catalogue and material guard | Material rewards risk inflation and pay-to-win | Six classes; recognition → record → authorship → rare material; keyed; `REWARD` ledger; caps | Material-first; presence rewards; production bonuses | D-151; `ECN-113`; `ECN-013(c)`; `ALL-224` | WEP-499…WEP-556 | Bounded, disclosed value | High on structure; Low on amounts | Prompt 14 currency-impact model |
| `D-160` | Alliance recognition | Alliance data is private and no prize is lawful | Honour-only aggregate at `k ≥ 5`; no member values; no command; no funding | Alliance ladder with prizes; member contribution list | `ALL-156`, `ALL-224`, `D-027`, `11A-DR-011` | WEP-335, WEP-379, WEP-627 | Small alliances protected | High | Alliance-size evidence (`UD-050`) |
| `D-161` | Warfare receipt rule | `WAR-147` places a positive obligation on B-11 | Receive participation, defensive bands and campaign record at P6 W1; feed `ST-MIL`/`ST-DEF`/`OBJ-DEF`; no exact value; no automatic material reward | Casualty or destruction totals; exact-force ranking | `WAR-147`, `WAR-162`, `11A-DR-015` | WEP-333, WEP-334, WEP-636 | Satisfies B-10 without a privacy breach | High | A B-10 privacy-rule change |

**WEP-695 — Inherited decisions preserved.** *Approved.* D-014, D-015, D-021, D-027, D-028, D-032…D-034, D-039…D-042, D-122, DD-136 and REQ-513 are unchanged. `UD-040`–`UD-049` remain Open and owner-reserved.

**WEP-696 — Conflicts recorded, not hidden.** *Approved.* The only inherited tension is B-10's use of "objective". It is resolved by D-153. No other conflict with B-02…B-10 is open. A future conflict is recorded here with the owning rule and the resolution path.

**WEP-697 — No owner-reserved resolution.** *Approved.* B-11 resolves only UD-024, which was delegated to Prompt 11. It does not resolve, narrow or assume an answer to UD-040…UD-049, UD-017 or any other owner question. It opens UD-050 and UD-051 for evidence genuinely owned elsewhere.

**WEP-698 — Decision traceability.** *Approved.* Every new decision maps to at least one `WEP-` rule and at least one `REQ-` row. Every direction in D-144…D-151 is applied in the sections named in §25.

---

## 25. Provisional parameters and calibration ownership

**WEP-699 — Every value is classified.** *Approved.* A value is Existing approved, Structural constant, Provisional design assumption, Prompt 14 calibration parameter or Owner-reserved. No value is unclassified.

**WEP-700 — Prompt 14 owns calibration.** *Approved.* The following families are provisional and owned by Prompt 14: event frequency and duration; band bounds; occurrence caps; teardown lag; freeze length; objective outstanding cap, tier thresholds, expiry and grace; standing windows, weights, caps and top-N; seasonal length; milestone `T_0` and `r`; reward amounts and caps; band widths for military recognition; `k`-application detail. Each is listed in the formula register with its formula ID.

**WEP-701 — Structural versus provisional.** *Approved.* A structural formula may contain a provisional constant; the structure is fixed and the constant is not. The register's field 20 distinguishes them.

**WEP-702 — No fake precision.** *Approved.* A provisional value is never presented as measured, simulated or approved. A worked example uses synthetic numbers and says so.

---

## 26. Deferred matters

**WEP-703 — Deferred to Prompt 11C.** *Approved.* Player journeys, trigger-to-completion workflows, edge-case execution, concurrency and recovery workflows, the full acceptance matrix, and workflow-level bidirectional traceability are Prompt 11C's.

**WEP-704 — Deferred to Prompt 12.** *Approved.* Enforcement, investigation, suspensions, bans, appeals, penalty thresholds, enforcement evidence retention and multi-account policy are Prompt 12's. B-11 supplies evidence and status codes only.

**WEP-705 — Deferred to Prompt 13.** *Approved.* Screens, layouts, navigation, accessibility, notification presentation, chronicle browsing/export and the re-entry surface are Prompt 13's.

**WEP-706 — Deferred to Prompt 14.** *Approved.* Every numeric calibration parameter and the balance validation of the standing set, reward bound, band widths and season length are Prompt 14's.

**WEP-707 — Deferred to Prompt 15.** *Approved.* Bible assembly, cross-document consolidation and the final consistency review are Prompt 15's. B-11 is a source document, not the assembled Bible.

---

## 27. Prompt 11C handoff

**WEP-708 — What 11C receives.** *Approved.* 11C receives: the four domain rules; the twelve state machines and their invalid transitions; the event taxonomy and effect catalogue; the objective categories and lifecycle; the ten standings and WSE; the eight progression layers; the reward catalogue; the P6 W1–W5 order; the contracts; the failure codes; the audit events; the privacy matrix; the formula IDs; the provisional parameter list; and the open decisions UD-050/UD-051.

**WEP-709 — What 11C must produce.** *Approved.* End-to-end event workflows per class (including protection onset, dormancy, reroll and interruption); objective accept-to-claim workflows (including tier, defer and supersede); snapshot/rollup/publication/correction workflows; reward conservation and duplicate-claim workflows; an edge-case catalogue; a numbered acceptance matrix (Designed, not executed); a bidirectional requirement ledger for REQ-704…REQ-763; a failure-code test set; a B-11 workflow validator with negative fixtures; and the free-tier evidence plan.

**WEP-710 — What 11C must not invent.** *Approved.* 11C may not invent a mechanic, a value, a punishment, a screen or a change to B-02…B-10. If a workflow reveals a missing rule, the rule is added here first and the workflow follows.

**WEP-711 — 11C acceptance.** *Approved.* 11C must show, for every rule and formula, a workflow or a test that exercises it, and must report the status honestly. A test is Designed until a build executes it.

---

## 28. Prompt 12–15 dependencies

**WEP-712 — Prompt 12.** *Approved.* Enforcement of multi-account, collusion, fake contribution and invalid grants; appeal and evidence retention; the operational `k`-application review for alliances (`UD-050`); privacy of enforcement records. B-11 supplies `WPA-` evidence, `WPF-32`/`WPF-33`, `SUSPENDED`/`EXCLUDED` and correction hooks.

**WEP-713 — Prompt 13.** *Approved.* Events Centre, Objectives and Challenges, Standings, Achievements, National Progress, Reward History and the re-entry surface. B-11 supplies required content and concepts; Prompt 13 owns the interface. `AP-006` and `ONB-036` make legibility a design requirement.

**WEP-714 — Prompt 14.** *Approved.* Calibration of every provisional parameter; simulation of the standing set for dominance; the material-reward rarity bound (`UD-051`); band-width privacy testing; season-length and cadence testing; the `URB-119` wealth-anchoring question (`11A-OPEN-006`).

**WEP-715 — Prompt 15.** *Approved.* Consolidation of B-11 into the Bible, including the formula register reference and the decision/requirement maps. Prompt 15 does not renumber B-11 or change a rule.

**WEP-716 — No prompt may lift a gate.** *Approved.* No downstream prompt may mark a Global Trade gate met, resolve an owner-reserved decision, or promote a provisional value to approved without the owning authority. `D-122`, `DD-136` and `REQ-513` remain in force.

**WEP-717 — Boundary statement.** *Approved.* Prompt 11B is a specification. Prompt 11C is workflow and acceptance. Prompt 12 is moderation. Prompt 13 is interface. Prompt 14 is calibration. Prompt 15 is assembly. No prompt may perform another's work under this document.

---

## 29. Final specification acceptance and limitations

**WEP-718 — Acceptance statement.** *Approved.* B-11 is **complete at the system-specification level** when: the four domains have normative rules; the formula register resolves every calculation; the twelve state machines are complete; all contracts WPC-01…WPC-17 exist; the failure and audit catalogues are complete; D-144…D-161 and DD-192…DD-209 are handled; UD-024 is resolved and UD-040…UD-049 remain open; every `11A-CR` and `11A-OPEN` row is dispositioned; and the validator passes.

**WEP-719 — What is proven.** *Approved.* Only that this document, the register and the registers are internally consistent and complete at the documentation level. No event fired, no objective progressed, no standing was computed, no reward was granted, no screen exists, no migration exists and no deployment occurred.

**WEP-720 — What is not proven.** *Approved.* Balance, fairness in a live population, abuse resistance in practice, free-tier storage cost, player comprehension, and the numerical viability of `k = 5` for alliance standings are not proven. They belong to Prompt 14, Prompt 12, Prompt 13 and Stage 3.

**WEP-721 — Calibration status.** *Approved.* Every numeric value not marked Approved or Structural is **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**. No value is described as calibrated.

**WEP-722 — Implementation status.** *Approved.* **No gameplay implementation is authorized by this document.** No code, database migration, API, production configuration, deployment, live gameplay change, final UI, moderation enforcement or calibrated balance exists.

**WEP-723 — Next action.** *Approved.* The next approved task is **Prompt 11C — World Events, Objectives, Rankings and Long-Term National Progression: Complete Workflows, Cross-System Integration and Acceptance.** Prompt 11C has not started.

---

**Acceptance record (11B-C3).** The original Prompt 11B gates `P11B-01`…`P11B-52` are preserved in the [acceptance source artifact](18_world_events_objectives_rankings_progression_acceptance_source.md) and crosswalked in the [acceptance crosswalk](18_world_events_objectives_rankings_progression_acceptance_crosswalk.md). All 52 gate rows are `PASS` on documentary evidence; the source record was independently authenticated on 2026-11-05, and the C2 change scope was verified against `Project X (61).zip` and `Project X (62).zip`. The crosswalk separates the gates from the 61 `B11-` validator checks. **11B-C2 final closeout: FULL PASS — independently accepted on 2026-11-05.**

*End of B-11 specification.*




