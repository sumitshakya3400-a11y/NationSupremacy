# B-12 — Fair-play operational journeys and workflows

**Version:** 1.0 · **Created:** 2026-11-10 · **Stage 2, Prompt 12C**
**Status:** **Operational workflow specification — design only.** Every journey and workflow below is a **specification artefact**. Nothing here is implemented, executed, runtime-tested, staffed or operating. `Definition: COMPLETE` and `Execution: NOT RUN` are the only honest values anywhere in this document.
**Authority.** This document owns the B-12 player and moderator journeys (`FPJ-###`) and the B-12 operational workflow library (`FPW-###`). It owns **no rule, no formula, no parameter, no requirement and no decision**: those remain with the [B-12 rulebook](20_fair_play_and_player_protection.md), the [B-12 formula and parameter register](20_fair_play_and_player_protection_formula_register.md), the [B-12 requirement register](20_fair_play_and_player_protection_requirements.md) and [DECISIONS.md](../DECISIONS.md). Where this document and a register diverge, **the register governs and this document is corrected** (`FP-005`, `GOV-019`).
**Companions.** [B-12 rulebook](20_fair_play_and_player_protection.md) · [B-12 requirements](20_fair_play_and_player_protection_requirements.md) · [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) · [B-12 acceptance](20_fair_play_and_player_protection_acceptance.md) · [12C cross-system integration](20_fair_play_and_player_protection_integration.md) · [12C edge cases and acceptance](20_fair_play_and_player_protection_edge_cases_acceptance.md) · [12A research](research/12A_fair_play_privacy_moderation_administration_research.md) · [12A registers](research/12A_requirements_integration_and_risk_registers.md) · [Prompt 11C companion](19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md) · [decisions](../DECISIONS.md) · [mirrored decisions](04_approved_and_provisional_decisions.md) · [unresolved decisions](05_unresolved_design_decisions.md).

---

## 1. What this document is, and what it never claims

**1.1 Purpose.** Prompt 12B §19 (`GOV-021`) hands Prompt 12C the B-12 rule set and asks 12C to design the workflows, journeys and end-to-end acceptance that operate it. This document performs that translation: for each normative rule family it states what activates it, which system acts, what information moves, what may be decided, what states are permitted, what the player experiences, what is audited, what happens when a dependency is unavailable or the result is ambiguous, and which acceptance test exercises it.

**1.2 It is not an implementation claim.** A workflow in this document exists as a specification. It does not mean a queue, tool, service, record, trigger, screen, job, permission or ledger exists. The project has no gameplay code, no moderation tooling and no audit spine implementation (`EVD-041`, `SEC-030`, `P12B-14`, `P12B-16`).

**1.3 It creates no rules.** `GOV-022` forbids 12C from weakening a rule, closing an owner or legal decision, inventing a number, promoting a provisional parameter or claiming runtime verification from a document check. Concretely, this document:

- allocates no new normative rule identifier and no new `REQ-` row;
- chooses no numeric duration, threshold, tier, window, cap, retention period or penalty;
- uses only the evidence states (`EVD-001`), transaction types (`COR-001`), violation classes (`FP-017`, Annex A), conduct tiers (`MOD-036`), roles (`ADM-003`), privacy classes (`PRV-002`), actor classes (`PRV-005`), actions (`PRV-006`) and failure postures (`FR-001`, Annex D) that B-12 already defines;
- returns `PROVISIONAL_BLOCK` wherever a named formula requires a value the owner or Prompt 14 has not set, exactly as the formula register states.

**1.4 Owner-reserved questions stay open.** `UD-017`, `UD-044`, `UD-046`, `UD-050`, `UD-052`…`UD-060` and every other open row keep their exact status. A workflow that would need one of them answered is written to the boundary of the question and stops there, naming the dependency.

**1.5 Governance.** [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (`D-014`) was read in full before this work began, including §§2–8. Category A constraints are unchanged: browser delivery, original identity, the mapless symbolic world, the two-hour UTC cadence, one account per person, Cloudflare Pages plus Supabase, the free-first target, no paid dependency, and Stage 1/2/3 sequencing (`FP-034`). The decisions recorded by this pass are Category B design decisions listed in §10 of the acceptance companion and mirrored in [DECISIONS.md](../DECISIONS.md); none is presented as owner-approved policy.

---

## 2. Terminology used by every record

| Term | Source | Meaning in this document |
|---|---|---|
| `E0`/`E1`/`E2`/`E3`/`EX` | `EVD-001` | The only five evidence states. No score, no sixth state. |
| `T0`…`T5` | `MOD-036` | The only six conduct tiers. |
| `V-01`…`V-16` | `FP-017`, Annex A | The only sixteen violation classes. |
| `R-MOD`…`R-EMG` | `ADM-003` | The only eight administrative roles. |
| `PUB`…`LEGAL` | `PRV-002` | The only nine access classes. |
| `ORIGINAL`…`ADMIN_ADJUSTMENT` | `COR-001` | The only six corrective transaction types. |
| `FR-01`…`FR-15` | Annex D | The only fifteen failure postures. |
| `NO_ACTION`…`REFERRED` | `EVD-020` | The only six case closure outcomes. |
| `UPHELD`/`REDUCED`/`REVERSED`/`REMANDED` | `MOD-045` | The only four appeal outcomes. |
| turn boundary | `D-015`, `MOD-040` | Every duration, window and expiry in this document is expressed in turn boundaries, never wall-clock. |
| owning subsystem | `FP-012`, `MOD-031` | The subsystem that holds the authoritative value. B-12 never writes it in place. |
| unsegregated | `MOD-005`, `MOD-022`, `MOD-049`, `ADM-013` | The label applied when staffing cannot deliver the separation a rule asks for. A label, never a claim of separation. |

**Case vocabulary.** A *report* is an accusation (`EVD-013`, `MOD-002`). A *case* is the record that a report or a signal opens. A *finding* requires `E3`. A *correction* needs no finding about a person (`FP-016`, `MOD-051`). A *sanction* is a conduct consequence. The words are not interchangeable and a record never uses violation language before `E3` (`FP-020`).

---

## 3. Actor model used by every record

The eight actor classes are `PRV-005`'s and are used verbatim: **PLAYER**, **ALLIANCE personnel**, **MOD** (`R-MOD`), **SMOD** (`R-SMOD`), **APL** (`R-APL`), **INV** (`R-INV`), **SEC/OPS** (`R-SEC`, `R-OPS`), **AUD** (`R-AUD`), plus **EMG** (`R-EMG`) for the emergency actor class. `SYS` denotes a server-side automated path, never a person. A person may hold several roles; every permission in this document is evaluated per action, not per identity (`PRV-005`). A player's own **account** and **nation** are distinct objects (`MA-002`): an enforcement attaches to the account (`INT-002`, `MOD-033`), never to a nation field or a pair state.

---

## 4. Journey record schema and inventory

**4.1 Schema.** Every `FPJ-###` record supplies these twelve fields, in this order. A record missing one is a specification defect and validator check `12C-05` fails it.

| Field | Meaning |
|---|---|
| ID and goal | `FPJ-###` plus what the actor is trying to achieve |
| Actor and role | Which `PRV-005` class acts |
| Entry condition | What must be true for the journey to exist |
| Preconditions | Required prior state, evidence state or permission |
| Main flow | The ordered steps, by `FPW-` reference |
| Alternate flows | Legitimate variations, including the unsegregated path |
| Failure flow | What the actor sees when a step fails, by posture `FR-01`…`FR-15` |
| State transitions | Only states that B-12 already defines |
| Information visible | What this actor may and may not see, by `PRV-008`…`PRV-022` |
| Notifications | Which notice, bounded by `MOD-017`/`MOD-018`/`PRV-019`/`PRV-020` |
| Audit trail | Which `EVD-026` event class the journey produces |
| Requirements and tests | `REQ-` rows covered; `FPA-` rows that verify the journey |

**4.2 Inventory.** Ten journeys, `FPJ-001`…`FPJ-010`, contiguous. They cover the eight families named in the Prompt 12B handoff (`GOV-021`: reporting, investigation, decision, sanction, correction, appeal, emergency action, restoration) plus the two families the requirement register adds: the shared-context declaration (`REQ-779`) and integrity review of the audit spine (`REQ-829`).

| ID | Journey | Actor | Principal requirements |
|---|---|---|---|
| `FPJ-001` | Report a suspected violation and receive a bounded outcome | PLAYER | `REQ-822`, `REQ-823`, `REQ-824`, `REQ-826`, `REQ-803` |
| `FPJ-002` | Be affected by enforcement without learning who reported or what was detected | PLAYER | `REQ-803`, `REQ-804`, `REQ-821`, `REQ-835` |
| `FPJ-003` | Take a report through intake, clustering, triage and a hold decision | MOD | `REQ-822`, `REQ-823`, `REQ-766`, `REQ-790` |
| `FPJ-004` | Investigate a case to a finding or an `EX` closure | INV | `REQ-767`, `REQ-793`, `REQ-794`, `REQ-826`, `REQ-832` |
| `FPJ-005` | Decide, record and notify a sanction within authority | SMOD | `REQ-812`, `REQ-813`, `REQ-816`, `REQ-821` |
| `FPJ-006` | Correct invalid value through the owning ledger without blaming a person | MOD / SYS | `REQ-817`, `REQ-819`, `REQ-845`, `REQ-861` |
| `FPJ-007` | Appeal one account-affecting action and live with its outcome | PLAYER | `REQ-833`, `REQ-834`, `REQ-835`, `REQ-836`, `REQ-837` |
| `FPJ-008` | Invoke, bound, expire and retrospectively review an emergency measure | EMG | `REQ-847`, `REQ-848`, `REQ-849`, `REQ-850` |
| `FPJ-009` | Declare a shared context and control who can see it | PLAYER | `REQ-779`, `REQ-780`, `REQ-778` |
| `FPJ-010` | Verify the audit chain and react to a break | AUD | `REQ-828`, `REQ-829`, `REQ-853`, `REQ-854` |

---

## 5. Journeys

### FPJ-001 — Report a suspected violation and receive a bounded outcome

| Field | Content |
|---|---|
| ID and goal | `FPJ-001` — a player reports conduct they believe violates a published rule, and learns what happened without the process leaking |
| Actor and role | `PLAYER` |
| Entry condition | A published rule and an appeal route exist; the player can identify a subject, a time window and a category |
| Preconditions | Authenticated session; `MOD-002` intake fields available; no enforcement result is implied by submitting |
| Main flow | `FPW-001` intake and acknowledgement → `FPW-002` duplicate clustering → `FPW-005` triage → `FPW-007` evidence-state assignment → (`FPJ-004` investigation) → `FPW-015` closure → bounded outcome notice |
| Alternate flows | Subject is an administrator → `FPW-003` confidential routing. Report is a first honest exploit disclosure → `FPW-033` incident lane, not conduct (`FP-027`). Intake unavailable → retryable failure, nothing silently lost (`FR-06`, `FPW-001`) |
| Failure flow | Unsubstantiated in good faith → no violation against the reporter (`MOD-004`, `REQ-824`); knowingly false → `V-15` case against the reporter. Unreceived report → no action is taken on it (`FR-06`) |
| State transitions | report: `SUBMITTED → ACKNOWLEDGED → CLUSTERED → CLOSED`; case: `OPEN → TRIAGED → (INVESTIGATING) → CLOSED`; a report never transitions directly to a finding (`EVD-013`) |
| Information visible | Own case reference and own report only. Never another player's data (`PRV-009`), never the reported party's restriction or investigation state (`PRV-019`), never a detector, threshold or rule-internal (`MOD-018`) |
| Notifications | Acknowledgement with case reference, stating no finding and no predicted outcome (`MOD-007`); bounded outcome notice on closure (`EVD-008`) |
| Audit trail | `EVD-026` classes: investigation and evidence writes; moderation actions. Reporter identity is never disclosed to the reported party (`INT-017`) |
| Requirements and tests | `REQ-822`, `REQ-823`, `REQ-824`, `REQ-825`, `REQ-826`, `REQ-803`; verified by `FPA-001`…`FPA-014` |

### FPJ-002 — Be affected by enforcement without learning who reported

| Field | Content |
|---|---|
| ID and goal | `FPJ-002` — a player receives, serves and understands a consequence while the process stays confidential |
| Actor and role | `PLAYER` (subject of a case) |
| Entry condition | A sanction record or a correction notice exists for their account |
| Preconditions | Evidence state matches the consequence ceiling (`EVD-002`); tier authority satisfied (`MOD-037`); notice content assembled (`FPW-014`) |
| Main flow | `FPW-016` application through B-03 → notice delivered → `FPW-027` appeal route published → `FPW-017` expiry and extension → restoration |
| Alternate flows | Delayed notice because an active investigation would be compromised → delay and its review recorded (`MOD-030`, `ADM-030`). Reversible hold instead of sanction because evidence is unavailable → `FR-05`, `SEC-023` |
| Failure flow | Notice cannot be delivered → action still recorded, notice enters the in-game digest, delivery failure recorded (`FR-07`, `REQ-850`). Ambiguous association → least-harmful reading, then `FPW-021` correction |
| State transitions | account: `ACTIVE → RESTRICTED(S)` / `SUSPENDED`; never `→ nation field changed` (`INT-002`). Suspension preserves the appeal and data-subject routes (`MOD-015`) |
| Information visible | The `V-` class, the rule element relied on, the evidence class, the tier, the end condition, the appeal route and any correction (`MOD-017`); no method, no threshold, no reporter, no third-party data (`MOD-018`) |
| Notifications | Significant-action notice (`MOD-017`); expiry notice; correction disclosure (`MOD-054`); emergency disclosure (`MOD-027`) |
| Audit trail | moderation and disciplinary actions; appeal outcomes; financial corrections (`EVD-026`) |
| Requirements and tests | `REQ-803`, `REQ-821`, `REQ-818`, `REQ-850`, `REQ-804`; verified by the `FPA-` rows of `FPW-013`, `FPW-014`, `FPW-016` and `FPW-017` in the acceptance companion |

### FPJ-003 — Take a report through intake, clustering, triage and a hold decision

| Field | Content |
|---|---|
| ID and goal | `FPJ-003` — a moderator turns an accusation into a properly triaged case without creating a finding |
| Actor and role | `MOD` (`R-MOD`) |
| Entry condition | A report exists, or an automated signal opened a review object (`FPW-006`) |
| Preconditions | Named capability to view assigned `MOD` records (`ADM-021`); declared interest screened (`FPW-004`); purpose stated for any restricted read (`PRV-004`) |
| Main flow | `FPW-001` → `FPW-002` → `FPW-005` triage (`MOD-008`) → `FPW-007` state assignment → either `FPJ-004`, a reversible hold, or closure |
| Alternate flows | Coordinated report volume → triage signal only, never a tier increase (`MOD-003`, `REQ-823`). Duplicate enforcement already exists against the same account → surfaced to a reviewer, not applied or dropped (`MOD-032`, `FPW-027`) |
| Failure flow | Investigation queue unavailable → holds may continue, no permanent measure (`FR-05`, `FR-07`). Detector down → degrade, record the gap, never block play (`FR-04`, `REQ-863`) |
| State transitions | case: `OPEN → TRIAGED → HOLDED` / `INVESTIGATING` / `CLOSED`; a hold is not a sanction (`MOD-009`) |
| Information visible | Assigned case plus bounded `PLAYER` fields (`ADM-021`); never `SEC` (`ADM-021`), never `AUDIT` (`PRV-015`) |
| Notifications | Internal only; the reporter keeps `FPJ-001`'s acknowledgement; the subject gets nothing until a significant action (`MOD-030`) |
| Audit trail | privileged access with purpose; investigation and evidence reads (`EVD-026`, `ADM-008`) |
| Requirements and tests | `REQ-766`, `REQ-790`, `REQ-822`, `REQ-823`, `REQ-863`, `REQ-864`; verified by the `FPA-` rows of `FPW-001`, `FPW-002`, `FPW-004`, `FPW-005`, `FPW-006` and `FPW-007` |

### FPJ-004 — Investigate a case to a finding or an `EX` closure

| Field | Content |
|---|---|
| ID and goal | `FPJ-004` — an investigator gathers server records, tests the rule elements and reaches a defensible conclusion |
| Actor and role | `INV` (`R-INV`); recommendations only (`ADM-023`) |
| Entry condition | A triaged case with a named `V-` class or a value anomaly the record proves |
| Preconditions | Case purpose stated (`PRV-004`); evidence preserved (`EVD-021`); conflict screened (`EVD-019`); investigate-and-decide separated where staffing permits (`ADM-010`, `REQ-843`) |
| Main flow | `FPW-007` state assignment → `FPW-008` sufficiency → `FPW-010` preservation and custody → `FPW-011` finding recommendation → `FPJ-005` decision |
| Alternate flows | Only behavioural anomaly present → review object, never a finding (`EVD-004`, `REQ-767`). Player-supplied screenshot → pointer, corroborated against server records; if corroboration is impossible → `EX` (`EVD-013`, `REQ-826`). Two server records conflict → recorded and resolved explicitly (`EVD-018`, `FPW-011`) |
| Failure flow | Investigation record corrupt → case becomes inconclusive, never proven (`12A-FR-03` posture restated by `FR-14`: return to last recorded state, never auto-close). Missing required input → `EX` or hold, never a permissive default (`GOV-006`) |
| State transitions | case: `INVESTIGATING → DECISION_PENDING → CLOSED`; evidence lifecycle `identify → collect → preserve → classify → link → assess → disclose → retain → redact → close → review` with every transition recorded (`EVD-035`) |
| Information visible | Case records, `SEC` need-to-know, `AUDIT` case scope (`ADM-023`); every read logged with purpose (`ADM-008`) |
| Notifications | None to the subject during investigation unless a significant action follows (`MOD-030`) |
| Audit trail | investigation and evidence reads/writes; privileged access; integrity-verification results (`EVD-026`) |
| Requirements and tests | `REQ-766`, `REQ-767`, `REQ-791`, `REQ-793`, `REQ-794`, `REQ-795`, `REQ-826`, `REQ-827`, `REQ-828`, `REQ-832`; verified by the `FPA-` rows of `FPW-007`–`FPW-011` |

### FPJ-005 — Decide, record and notify a sanction within authority

| Field | Content |
|---|---|
| ID and goal | `FPJ-005` — a deciding reviewer converts a sufficient finding into a proportionate, comprehensible, appealable consequence |
| Actor and role | `SMOD` for `T3`; `MOD` within `T0`–`T2`; owner-authorized threshold for `T4`/`T5` (`MOD-037`) |
| Entry condition | A recommended finding has reached `DECISION_PENDING` |
| Preconditions | `E3` with at least two independent sources, one non-behavioural (`EVD-010`); a named `V-` class and relied-on element (`FP-021`); demonstrated impact where Annex A requires it (`FP-023`) |
| Main flow | `FPW-011` finding → `FPW-012` severity and repetition → `FPW-013` authority and second review → `FPW-014` record and notice → `FPW-016` application |
| Alternate flows | Correction and conduct both justified → recorded and appealable separately (`FP-031`, `MOD-055`). Mitigation present → may reduce tier, never erases material impact (`FP-026`). Duration value unapproved → `PROVISIONAL_BLOCK` from `F-FP-005`, not a default |
| Failure flow | Notice assembly fails → the action is not committed without its record (`FR-03`, `FR-01`). Audit spine write fails → the transaction fails closed (`FR-01`/`FR-03`) and the reviewer is told nothing was applied |
| State transitions | case: `DECISION_PENDING → CLOSED` with one of six outcomes (`EVD-020`); account: `ACTIVE → RESTRICTED(T2)` / `SUSPENDED(T3–T4)` / `CLOSED(T5)` |
| Information visible | Decision, reason code, tier, end condition, appeal route (`MOD-017`, `MOD-021`); no method (`MOD-018`) |
| Notifications | Significant-action notice; appeal route published (`REQ-803`, `12A-INT-24`) |
| Audit trail | moderation and disciplinary actions; administrative overrides where used; appeal outcomes (`EVD-026`) |
| Requirements and tests | `REQ-811`…`REQ-821`, `REQ-813`, `REQ-816`; verified by the `FPA-` rows of `FPW-011`–`FPW-014` and `FPW-016` |

### FPJ-006 — Correct invalid value through the owning ledger

| Field | Content |
|---|---|
| ID and goal | `FPJ-006` — value the published rules could not produce is restored without a finding about a person |
| Actor and role | `SYS` for the instruction; `MOD`/`INV` for the case; **B-04 or the owning subsystem executes** (`INT-003`, `MOD-052`) |
| Entry condition | The record proves an impossible effect (`EVD-002`, `FP-016`) |
| Preconditions | Original transaction identified (`COR-002`); idempotency key derived from case, original and type (`COR-005`); reason code named (`ADM-012`) |
| Main flow | `FPW-021` instruction → `FPW-022` amount → owning ledger append → `FPW-026` reconciliation → `MOD-054` disclosure → appeal route offered (`COR-008`) |
| Alternate flows | Value moved to another account → `FPW-023` removal follows the flow, subject to `UD-052`. Account cannot cover → floor at zero, record shortfall (`COR-012`). Wrong correction → `FPW-024` appended correction of the correction (`COR-009`) |
| Failure flow | Partial completion prohibited → roll back exactly and retry with the same key (`COR-018`, `FR-09`). Missing lawful counterfactual → `NO_CALCULATION` plus incident, never zero (`F-FP-002` §9) |
| State transitions | ledger: `ORIGINAL → +CORRECTION` / `+ILLICIT_REMOVAL` / `+REVERSAL`; balance never negative (`COR-003`) |
| Information visible | Type, amount or state change, reason, appeal route for the affected account only (`MOD-054`, `COR-015`) |
| Notifications | The affected account is told that a correction occurred, the rule effect reversed, the amount or state change and the dispute route, with no third-party data (`MOD-054`, `COR-015`) |
| Audit trail | financial corrections; every corrective transaction with case and original reference (`COR-016`) |
| Requirements and tests | `REQ-817`, `REQ-819`, `REQ-820`, `REQ-836`, `REQ-845`, `REQ-861`; verified by the `FPA-` rows of `FPW-021`–`FPW-026` |

### FPJ-007 — Appeal one account-affecting action

| Field | Content |
|---|---|
| ID and goal | `FPJ-007` — a player contests one action on stated grounds and receives a written, reasoned outcome |
| Actor and role | `PLAYER` files; `APL` (`R-APL`) decides |
| Entry condition | An account-affecting action at `T1` or above exists (`MOD-042`) |
| Preconditions | Filing window structured by `F-FP-006`; an unapproved `W` returns `PROVISIONAL_BLOCK`, so the window cannot be enforced or claimed until `UD-059` is decided |
| Main flow | `FPW-027` filing → `FPW-028` in force plus optional reversible hold → `FPW-029` decision → `FPW-030` reopening bar → `FPW-024` reversal and restitution where upheld |
| Alternate flows | Service unavailable → action stands, window extended by the recorded outage in turn boundaries, no appeal deemed abandoned (`FR-10`). Reviewer is the original decider → labelled **not independent** and disclosed (`MOD-049`, `REQ-837`). Disagreement with the rule's existence → policy feedback item, not an appeal ground (`MOD-044`) |
| Failure flow | Independence unavailable at current staffing → the label is applied; separation is never claimed (`ADM-013`, `REQ-846`) |
| State transitions | appeal: `FILED → IN_FORCE → DECIDED(UPHELD/REDUCED/REVERSED/REMANDED) → CLOSED`; reopened only on new evidence or procedural defect (`MOD-046`) |
| Information visible | Sufficient to contest, with method, thresholds and third-party data withheld by rule (`MOD-035`, `REQ-835`) |
| Notifications | Filing acknowledgement; the written reasoned decision (`MOD-045`); the reversal and restitution notice where the appeal is upheld (`MOD-047`) |
| Audit trail | appeal outcomes; administrative overrides; evidence reads (`EVD-026`) |
| Requirements and tests | `REQ-833`…`REQ-837`, `REQ-830`-adjacent retention; verified by the `FPA-` rows of `FPW-027`–`FPW-030` and `FPW-024` |

### FPJ-008 — Invoke, bound, expire and review an emergency measure

| Field | Content |
|---|---|
| ID and goal | `FPJ-008` — contain an active incident without acquiring permanent power |
| Actor and role | `EMG` (`R-EMG`); only the named emergency role may invoke (`ADM-015`) |
| Entry condition | An incident class is declared (`SEC-024`) and ordinary authority is too slow |
| Preconditions | Incident, scope, expiry and review owner stated (`ADM-015`); `D_e` from `F-FP-016`; an unapproved `D_e` returns `PROVISIONAL_BLOCK` (`REQ-847`, `UD-056`) |
| Main flow | `FPW-033` incident classification → `FPW-031` invocation → `FPW-032` expiry, extension and retrospective review → `FPW-024` restoration or the ordinary path |
| Alternate flows | Measure must persist → ordinary path with its appeal, never an emergency extension without review (`MOD-025`, `MOD-041`) |
| Failure flow | Cannot be recorded → does not execute (`FR-11`). Threat or third-party data would be disclosed → withheld, generic notice (`MOD-027`) |
| State transitions | measure: `INVOKED → IN_FORCE → EXPIRED` or `EXTENDED(new decision)`; never `→ deleted` / `→ confiscated` / `→ history rewritten` (`MOD-025`, `MOD-048` of `REQ-848`) |
| Information visible | Players are told a temporary measure is in force and when it will be reviewed (`MOD-027`, `REQ-850`) |
| Notifications | The temporary-measure disclosure with its review time and no threat detail (`MOD-027`, `REQ-850`) |
| Audit trail | emergency actions; integrity-verification results (`EVD-026`) |
| Requirements and tests | `REQ-847`, `REQ-848`, `REQ-849`, `REQ-850`, `REQ-856`, `REQ-858`; verified by the `FPA-` rows of `FPW-031`–`FPW-034` and `FPW-024` |

### FPJ-009 — Declare a shared context and control who can see it

| Field | Content |
|---|---|
| ID and goal | `FPJ-009` — a player records which accounts share a device, household, institution or network, without creating an exemption |
| Actor and role | `PLAYER` |
| Entry condition | The player controls or is aware of the association |
| Preconditions | Declaration grants nothing and its absence is never aggravating (`MA-003`) |
| Main flow | `FPW-019` record → visible to author accounts and integrity role only → used as review evidence only (`FPW-007`) → deletable by its author (`FPW-040`) |
| Alternate flows | Declaration contradicts a flow finding → the flow evidence governs (`MA-006`); a declaration is never identity proof (`MA-011`) |
| Failure flow | Storage unavailable → retryable failure; the absence of a declaration is never inferred from the failure |
| State transitions | declaration: `RECORDED → CITED_IN_CASE` / `DELETED` |
| Information visible | Author and integrity role (`MA-004`); never shown to an unrelated player or used as a disclosure channel |
| Notifications | Confirmation of recording or withdrawal to the author only; nothing is sent to a named associated account (`MA-004`) |
| Audit trail | privileged access when the integrity role reads it (`ADM-008`) |
| Requirements and tests | `REQ-778`, `REQ-779`, `REQ-780`, `REQ-781`; verified by the `FPA-` rows of `FPW-019` and `FPW-040` |

### FPJ-010 — Verify the audit chain and react to a break

| Field | Content |
|---|---|
| ID and goal | `FPJ-010` — detect record alteration and treat detection as an incident, not a routine correction |
| Actor and role | `AUD` (`R-AUD`) |
| Entry condition | A spine exists. **It does not today**: no chained digest, no verification job and no protective trigger are implemented (`EVD-041`, `SEC-036`, `SEC-038`, `P12B-14`) |
| Preconditions | Verification interval from `F-FP-013`, provisional (`FP-P08`); readership granted by purpose (`EVD-033`) |
| Main flow | `FPW-045` chain verification run → checkpoint recorded → on break: `FPW-033` incident classification → halt the affected value path (posture per `FR-001` category) → `FPW-046` appended correction only after review |
| Alternate flows | Volume pressure → spine rows are never sampled away; value, pipeline, privileged and enforcement rows retained first (`EVD-034`, `REQ-853`) |
| Failure flow | Enabling verification is not validating it: the run is the evidence (`EVD-032`, `SEC-039`). Missing record → `CHAIN_BREAK`, never a skipped link (`F-FP-012` §9) |
| State transitions | checkpoint: `LAST_VERIFIED → VERIFIED_NEW` or `BREAK_INCIDENT_OPEN`; a spine row is never mutated in place (`EVD-029`) |
| Information visible | Audit role reads the spine and case records; every read logged (`PRV-015`, `EVD-033`) |
| Notifications | Nothing to players unless a break halts publication, in which case the delay is disclosed (`REQ-858`) |
| Audit trail | integrity-verification results (`EVD-026`); audit reads (`REQ-854`) |
| Requirements and tests | `REQ-828`, `REQ-829`, `REQ-851`…`REQ-855`; verified by the `FPA-` rows of `FPW-044`–`FPW-046`. **Blocked at `P12B-14` and `P12B-16` until an implementation and an executed verification run exist** |

---

## 6. Workflow record schema and inventory

**6.1 Schema.** Every `FPW-###` record supplies these twelve fields, in this order, which together carry the seventeen attributes Prompt 12C §6 requires. A record missing one is a specification defect and validator check `12C-04` fails it.

| Field | Meaning |
|---|---|
| ID and purpose | `FPW-###`, name, and the behaviour owned |
| Initiator, permissions and trigger | Who may start it, the `✗` list, and the event or condition that activates it |
| Systems and responsibilities | Acting system, owning subsystem of the authoritative value, participants |
| Required input and access | Logical inputs only — fields, not a physical schema — plus the access class each requires |
| Validation and decision sequence | Checks that must pass before any mutation, in order |
| Normal path | What happens when every check succeeds |
| Alternative paths | Legitimate variations, including the unsegregated and hold branches |
| Failure behaviour | Posture from Annex D, dependency unavailable, ambiguous result |
| Resulting state and player experience | States that B-12 already defines, and what the affected player sees |
| Permitted action and audit evidence | Which administrative action this workflow may produce and which `EVD-026` class it writes |
| Security and privacy constraints | The `SEC-`, `PRV-` and boundary rules that limit it |
| Trace and tests | Rules, `REQ-` rows, `INT-`/`12A-INT-` references, formulas, open decisions, and `FPA-`/`FPE-` rows |

**6.2 No workflow may add a rule.** If a workflow reveals a missing rule, the rule belongs in the B-12 rulebook first (`GOV-019`, and the same discipline `WEP-710` imposes on B-11). Where 12C found a genuinely missing rule or an unavailable control it did **not** write one; it registered a gap in §11 of the acceptance companion and named who decides it.

**6.3 Workflow inventory.** **Fifty-two** records, `FPW-001`…`FPW-052`, contiguous with no unallocated gap; `FPW-053` onward is unallocated. Families: A intake and triage `001`–`005`; B detection and evidence `006`–`010`; C finding, decision and sanction `011`–`015`; D restriction, identity and association `016`–`020`; E correction and recovery `021`–`026`; F appeals `027`–`030`; G emergency and incident `031`–`034`; H privacy and information handling `035`–`038`; I disclosure, export, retention and legal hold `039`–`041`; J administration and separation `042`–`043`; K audit spine and integrity `044`–`046`; L cross-system handoffs `047`–`051`; M governance review `052`.

**6.4 Turn phases referenced.** `TR-040` fixes the phase order as **P0 Prepare · P1 Freeze · P2 Re-validate · P3 Recurring · P4 Orders · P5 Conflict · P6 World · P7 Settle**, with the P6 sub-order `W1`…`W5` owned by B-11 (`WEP-606`). B-12 workflows act in **`W0`**, the out-of-band label this document uses for any moderation, correction, audit or administrative action that is not part of turn resolution, plus at the named boundary where a rule explicitly ties an effect to one (`TR-044`/`TR-045` bands and order key for anything resolved inside a turn; `TR-048` for replay determinism; `FP-014` for the no-order-payoff rule). A B-12 workflow never reorders a closed turn (`COR-007`).

---

## 7. Family A — Intake and triage

### FPW-001 — Report intake, structured capture and acknowledgement

| Field | Content |
|---|---|
| ID and purpose | `FPW-001` — turn a player's submission into one structured report record and a case reference |
| Initiator, permissions, trigger | `PLAYER`, authenticated; `MOD`/`SMOD`/`SYS` ✗ as submitters. Trigger: a player submits a report in any category of Annex A |
| Systems and responsibilities | B-12 owns the report record (`INT-017`); B-02 supplies turn identity and boundary; Prompt 13 owns the surface (`INT-020`); no other system is written |
| Required input and access | Category, subject account or nation reference, time window, reporter account, free-text account, and any separately stored supplied artefact (`MOD-002`). Writes only `MOD`-class state (`PRV-012`) |
| Validation and decision sequence | Session valid (`SEC-001`); subject object authorized separately (`SEC-002`); category ∈ `V-01`…`V-16` or `OTHER-REVIEW` routing label, never a charge (`FP-021`); supplied artefact kept as a pointer, not a finding (`EVD-013`); rate allowance checked as account-plus-resource keyed (`SEC-007`, `F-FP-009`) |
| Normal path | One report row written as an **accusation**; `FPW-002` clustering runs; acknowledgement with case reference issued stating no finding and no predicted outcome (`MOD-007`) |
| Alternative paths | Same conduct, same window → coalesce to the existing case (`MOD-003`). Subject is a privileged actor → `FPW-003`. Reporter discloses their own first-use exploit → `FPW-033` incident lane (`FP-027`) |
| Failure behaviour | Intake unavailable → retryable failure, nothing silently lost, and **no enforcement action on an unreceived report** (`FR-06`, `FPW-001` gate). Audit write unavailable → the report is not committed (`FR-01`/`FR-03` posture for `EVD-026`-class writes). Ambiguous subject → held for triage, never auto-matched by network signal (`MA-005`) |
| Resulting state, player experience | report `SUBMITTED → ACKNOWLEDGED`; case `OPEN`. Reporter sees only their own case reference |
| Permitted action, audit evidence | No consequence is permitted at intake. Writes `EVD-026` investigation and evidence write; record shape `EVD-027` |
| Security and privacy constraints | Reporter identity never exposed to the subject (`INT-017`, `REQ-803`); no credential captured or logged (`SEC-027`); response minimisation on any read-back (`FP-015`) |
| Trace and tests | `MOD-002`, `MOD-007`, `EVD-013`, `FP-021`, `SEC-001`, `SEC-002`, `SEC-007` · `REQ-822`, `REQ-803`, `REQ-775` · `INT-017`, `12A-INT-21` · `F-FP-009` · `FPA-001`–`FPA-006`, `FPE-001`, `FPE-002` |

### FPW-002 — Duplicate clustering and coordinated-volume triage

| Field | Content |
|---|---|
| ID and purpose | `FPW-002` — coalesce reports of one conduct into one case and keep volume out of severity |
| Initiator, permissions, trigger | `SYS`; no human submitter. Trigger: a report is written by `FPW-001` |
| Systems and responsibilities | B-12 owns the cluster key and the case; nothing is written to any gameplay subsystem |
| Required input and access | Subject account `s`, violation class `v`, clustering window `w` in turns, earliest linked event key `e` (`F-FP-008`) |
| Validation and decision sequence | Key `H(s‖v‖w‖e)` computed; different classes never coalesce; reporter identity is **not** part of the key (`F-FP-008` §6); missing subject → held report, not a cluster (§9) |
| Normal path | Cluster count incremented on the existing case; coordinated volume recorded as a triage signal only |
| Alternative paths | A report outside `w` → new cluster. `w` unapproved → `PROVISIONAL_BLOCK` (`FP-P13` provisional): clustering may be performed as a stated-uncertainty grouping, never as an enforced de-duplication rule |
| Failure behaviour | Volume never raises a tier against the reported party (`MOD-003`, `REQ-823`); a failed clustering write records the report unclustered and surfaces it to `FPW-005` — never drops it |
| Resulting state, player experience | case `OPEN` with cluster count; no player-visible change |
| Permitted action, audit evidence | Review-object creation only. Writes `EVD-026` investigation and evidence writes |
| Security and privacy constraints | Cluster records are `MOD` class (`PRV-012`); reporter anonymity preserved inside the cluster (`INT-017`) |
| Trace and tests | `MOD-003`, `F-FP-008`, `REQ-823`, `REQ-822` · `INT-017` · `FP-P13` · `FPA-007`–`FPA-010`, `FPE-003`, `FPE-004` |

### FPW-003 — Confidential routing of a report against a privileged actor

| Field | Content |
|---|---|
| ID and purpose | `FPW-003` — route administrator, moderator and reviewer reports away from the ordinary chain |
| Initiator, permissions, trigger | `SYS` on detection that the subject holds any of `R-MOD`…`R-EMG`; `MOD` ✗ (a moderator never receives their own-subject case, `ADM-009`) |
| Systems and responsibilities | B-12 owns routing; Stage 6 owns the privileged session (`INT-015`); the owner is the escalation destination (`ADM-029`) |
| Required input and access | Report record; subject role membership; declared interests (`FPW-004`) |
| Validation and decision sequence | Subject role present → independent reviewer sought; retaliation pattern screened as its own `V-15` case (`MOD-006`, `REQ-825`); segregation feasibility recorded |
| Normal path | Routed to an independent reviewer where one exists. Where none exists → labelled **unsegregated** and disclosed to the owner (`MOD-005`) |
| Alternative paths | Retaliation against the reporter evidenced → separate case (`MOD-006`); administrative misconduct evidenced → `V-16` plus incident review (`FP-030`, `ADM-020`) |
| Failure behaviour | Routing service unavailable → report remains in `FPW-001` state, flagged, never silently routed to the subject's peers (`FR-06`) |
| Resulting state, player experience | case `OPEN` with confidential routing flag; the reporter sees only an acknowledgement |
| Permitted action, audit evidence | None beyond case creation. Writes `EVD-026` privileged access and moderation action classes |
| Security and privacy constraints | Confidential routing is itself `MOD`/`SEC`-class; no `SEC` field is returned to a moderator (`ADM-021`) |
| Trace and tests | `MOD-005`, `MOD-006`, `FP-030`, `ADM-009`, `ADM-020`, `ADM-029`, `V-15`, `V-16` · `REQ-825` · `12A-INT-22`, `INT-020` · `FPA-011`–`FPA-014`, `FPE-005` |

### FPW-004 — Conflict-of-interest screening and unsegregated labelling

| Field | Content |
|---|---|
| ID and purpose | `FPW-004` — exclude an interested reviewer, or label the case honestly when exclusion is impossible |
| Initiator, permissions, trigger | `SYS` at `FPW-005` triage and again at `FPW-013` decision. Trigger: a reviewer is assigned to or acts on a case |
| Systems and responsibilities | B-12 owns the screen and the label; B-09 supplies membership facts read-only (`INT-008`); the owner's staffing decision is `UD-054` |
| Required input and access | Reviewer role and Alliance membership, declared interests, subject account and Alliance, prior involvement in the case |
| Validation and decision sequence | Reviewer is a party, an Alliance member of the subject, or has a declared interest → excluded (`MOD-021`, `EVD-019`); exclusion impossible → `unsegregated = true` recorded and disclosed to the affected player |
| Normal path | A clean reviewer is assigned; the exclusion decision is stated in the record (`MOD-021`) |
| Alternative paths | Single-operator staffing → label plus disclosure (`ADM-013`, `MOD-049`); appeal reviewer is the original decider → **not independent** label (`FPW-029`) |
| Failure behaviour | Screening data unavailable → the case holds at triage; no decision is taken with an unscreened reviewer (`FR-02` authorization posture) |
| Resulting state, player experience | case `TRIAGED` with screening outcome recorded |
| Permitted action, audit evidence | Assignment and labelling only. Writes `EVD-026` privileged access and moderation action |
| Security and privacy constraints | The label never discloses the reviewer's identity to the player; it discloses the fact of non-segregation (`REQ-795`) |
| Trace and tests | `EVD-019`, `MOD-021`, `MOD-022`, `MOD-049`, `ADM-010`, `ADM-013` · `REQ-795`, `REQ-837`, `REQ-843` · `UD-054` **Open** · `12A-INT-22` · `FPA-015`–`FPA-018`, `FPE-006` |

### FPW-005 — Triage, initial assessment and reversible hold

| Field | Content |
|---|---|
| ID and purpose | `FPW-005` — order the queue by safety and evidence, and decide whether a reversible hold is justified |
| Initiator, permissions, trigger | `MOD` (`R-MOD`, `ADM-021`); `PLAYER` ✗. Trigger: a case is `OPEN` |
| Systems and responsibilities | B-12 owns triage; B-03 owns any applied account restriction (`INT-001`); the owning subsystem keeps its own state authority (`MOD-031`) |
| Required input and access | Report and cluster facts; subject account and nation state; protection, dormancy and eligibility state read from B-03 (`WPC-02` precedent); evidence state so far (`FPW-007`) |
| Validation and decision sequence | Safety, evidence state, subject status and conflict screened **before any action** (`MOD-008`); hold justified only where `E1` or better and reversible (`EVD-002`, `MOD-009`); a hold is never recorded as a sanction (`MOD-009`) |
| Normal path | Case moves to `TRIAGED`, then to `FPW-011` investigation, `FPW-021` correction path, or `FPW-015` closure |
| Alternative paths | Protection or dormancy in force → the eligibility consequence belongs to the owning subsystem, triage does not convert it into a sanction (`WEE-011` precedent, `MOD-031`); queue unavailable → reversible holds continue, no permanent measure (`FR-05`, `FR-07`) |
| Failure behaviour | Ambiguous subject identity → least-harmful reading pending `FPW-020` (`12A` posture 13 restated by `REQ-865`); a failed triage write → nothing is committed (`FR-03`) |
| Resulting state, player experience | case `OPEN → TRIAGED` / `HOLDED` / `CLOSED`; a held player sees a capability limitation and its stated scope, not the reason set (`MOD-027`, `PRV-020`) |
| Permitted action, audit evidence | Reversible hold at `E1` maximum; review priority. Writes `EVD-026` moderation action |
| Security and privacy constraints | No status about another player is disclosed (`PRV-019`); hold content never reveals a detector (`MOD-018`) |
| Trace and tests | `MOD-008`, `MOD-009`, `EVD-002`, `EVD-003`, `MOD-031` · `REQ-766`, `REQ-790`, `REQ-864` · `12A-INT-17` · `FPA-019`–`FPA-026`, `FPE-007`, `FPE-008` |

---

## 8. Family B — Detection and evidence

### FPW-006 — Automated signal to permitted output only

| Field | Content |
|---|---|
| ID and purpose | `FPW-006` — let automation open review, create a reversible hold or request a correction, and nothing else |
| Initiator, permissions, trigger | `SYS`; trigger: a declared detection rule fires |
| Systems and responsibilities | B-12 owns the finding; the signalling subsystem owns its own signal semantics (`INT-006` market `MKT-S`, `INT-010` B-11 flags, `INT-009` B-10 block records) |
| Required input and access | Detector ID, rule version, inputs read, output class, subject reference, turn boundary |
| Validation and decision sequence | Detector declared per `FPW-009`; output ∈ {review object, policy signal, reversible preventive restriction, value correction} (`EVD-003`, `REQ-790`); `E3`, conduct finding, suspension, permanent measure or public statement are prohibited outputs (`EVD-003`) |
| Normal path | A review object opens at `E1` and routes to `FPW-005` |
| Alternative paths | Record proves an impossible effect → `FPW-021` correction without any person-level claim (`FP-016`); detection down → degrade and record, never block play (`FR-04`, `REQ-863`) |
| Failure behaviour | Missing input → no signal is created, and the gap is recorded (`GOV-006`); a duplicate fire coalesces (`SEC-008`) |
| Resulting state, player experience | case `OPEN` (system-created); the subject sees nothing unless a reversible restriction applies with a stated scope (`MOD-027`) |
| Permitted action, audit evidence | Review object, priority, reversible hold, correction instruction. Writes `EVD-026` investigation and evidence writes |
| Security and privacy constraints | Detection internals are `SEC` class and never returned to any player or moderation surface (`PRV-014`); rules are published, detectors are not (`12A-DR-012`, adopted as a design position, not a new rule) |
| Trace and tests | `EVD-002`, `EVD-003`, `EVD-004`, `FP-016`, `FR-04`, `SEC-008` · `REQ-766`, `REQ-790`, `REQ-863` · `12A-INT-09`, `12A-INT-14` · `FPA-027`–`FPA-032`, `FPE-009`, `FPE-010` |

### FPW-007 — Evidence-state assignment

| Field | Content |
|---|---|
| ID and purpose | `FPW-007` — assign exactly one of `E0`, `E1`, `E2`, `E3`, `EX` and cap the consequence by state |
| Initiator, permissions, trigger | `MOD` or `INV`; trigger: a review object, report or signal exists |
| Systems and responsibilities | B-12 owns the state; no other system may set or infer it (`EVD-001`) |
| Required input and access | Source list with producer and independence flags; non-behavioural source presence; rule elements examined |
| Validation and decision sequence | Exactly one state (`EVD-001`, no sixth, no score); independence test applied — two outputs of one detector, or two reports repeating one allegation, are **not** independent (`EVD-011`); behavioural anomaly alone caps at review (`EVD-004`); network attribute is triage only (`EVD-005`, `MA-005`) |
| Normal path | State recorded with its basis; `EVD-002` ceiling becomes the only permitted consequence set |
| Alternative paths | Cannot reach `E2` or `E3` → `EX` and closure with what was examined (`EVD-008`) |
| Failure behaviour | Ambiguous state → the lower state governs, never the higher (`F-FP-007` returns false); a missing source count returns false (`F-FP-007` §9) |
| Resulting state, player experience | case `TRIAGED → INVESTIGATING`; no direct player-visible change |
| Permitted action, audit evidence | State assignment. Writes `EVD-026` investigation and evidence writes |
| Security and privacy constraints | No confidence value, composite or probability is computed or stored anywhere (`EVD-007`, `REQ-793`) |
| Trace and tests | `EVD-001`…`EVD-008`, `EVD-011`, `MA-005`, `F-FP-007` · `REQ-766`, `REQ-767`, `REQ-778`, `REQ-793` · `FPA-033`–`FPA-038`, `FPE-011`, `FPE-012` |

### FPW-008 — Sufficiency assessment against the corroboration matrix

| Field | Content |
|---|---|
| ID and purpose | `FPW-008` — decide whether a claim may proceed, using the matrix and not a score |
| Initiator, permissions, trigger | `INV`; trigger: `FPW-007` produced `E1` or better |
| Systems and responsibilities | B-12 owns sufficiency; the owning subsystem's rule remains authoritative for its own capability (`REQ-815`) |
| Required input and access | Claim type (`correction` or `conduct`), `E`, independent source count `n_i`, non-behavioural flag `b` |
| Validation and decision sequence | `SUFFICIENT = (correction ∧ E ≥ E2) ∨ (conduct ∧ E = E3 ∧ n_i ≥ 2 ∧ b = 1)` (`F-FP-007`); `EX` always false; a reversible preventive hold may proceed at `E1` without this predicate (`EVD-002`) |
| Normal path | Sufficient → `FPW-011` finding or `FPW-021` correction. Insufficient → continue or close `EX` |
| Alternative paths | Player-supplied artefact is the only source → corroborate against server records, else `EX` (`EVD-013`, `REQ-826`) |
| Failure behaviour | Missing source count → false, i.e. no consequence (`F-FP-007` §9); no fallback to a score is permitted (`EVD-007`) |
| Resulting state, player experience | unchanged case state; consequence ceiling enforced downstream |
| Permitted action, audit evidence | Sufficiency determination recorded. Writes `EVD-026` investigation and evidence writes |
| Security and privacy constraints | The matrix is internal; the published text states the prohibited effect, not the sufficiency arithmetic (`FP-033`) |
| Trace and tests | `EVD-010`, `EVD-011`, `EVD-013`, `F-FP-007` · `REQ-767`, `REQ-793`, `REQ-826` · `FPA-039`–`FPA-044`, `FPE-013` |

### FPW-009 — Detector declaration and false-positive catalogue gate

| Field | Content |
|---|---|
| ID and purpose | `FPW-009` — refuse to enable any detection rule whose purpose, sources, false positives and minimum corroboration are not declared |
| Initiator, permissions, trigger | `SEC`/`SMOD` as configuration author; `PLAYER` ✗; trigger: a new or changed detection rule is proposed. Publishing is a separate act (`ADM-011`) |
| Systems and responsibilities | B-12 owns the rule register; the owning subsystem supplies the data the rule reads; Prompt 14 owns any numeric value (`INT-019`) |
| Required input and access | Purpose, data source (must be already inventoried), legitimate triggers, false-positive classes, minimum corroboration, permitted automated output (`EVD-015`) |
| Validation and decision sequence | Data read is already held for gameplay, account-security or legal purposes — no telemetry, client agent, keystroke log, device fingerprint or monitoring SDK (`EVD-016`, `REQ-796`); required-but-refused data → the capability is recorded **not available**, never softened (`EVD-017`, `REQ-797`); catalogue completeness against the named classes (`EVD-014`) |
| Normal path | Declared rule enabled with its output ceiling pinned to `FPW-006` |
| Alternative paths | Author cannot also be sole publisher → separated (`ADM-011`); no second person exists → recorded disclosure plus retrospective review (`REQ-844`, `UD-054` **Open**) |
| Failure behaviour | Undeclared rule → not enabled, and the attempt is recorded (`FR-02`); a rule needing refused data → `not available`, and no proxy is built |
| Resulting state, player experience | detection register version recorded; no player-visible change |
| Permitted action, audit evidence | Configuration authoring only. Writes `EVD-026` configuration publication and permission changes |
| Security and privacy constraints | Rule internals `SEC` class (`PRV-014`); prevention-first alternatives considered before surveillance (`REQ-789`) |
| Trace and tests | `EVD-014`–`EVD-017`, `PRV-014`, `ADM-011` · `REQ-789`, `REQ-791`, `REQ-792`, `REQ-796`, `REQ-797` · `UD-054`, `INT-019` · `FPA-045`–`FPA-048`, `FPE-014`, `FPE-015` |

### FPW-010 — Preservation, chain of custody and conflicting-record resolution

| Field | Content |
|---|---|
| ID and purpose | `FPW-010` — protect the records a case needs, log every handling act, and resolve conflicting server records explicitly |
| Initiator, permissions, trigger | `INV` or `MOD`; trigger: case opening, any evidence access, annotation, correction or export, or a detected record conflict |
| Systems and responsibilities | B-12 owns case records; B-02's spine owns the immutable record (`INT-014`, `TR-090`, `TR-091`); the owning subsystem remains the source of truth |
| Required input and access | Case reference, artefact provenance (producer, source system, timestamp, integrity reference), the conflicting pair of records |
| Validation and decision sequence | Preservation references immutable records and protects them from routine compaction, **without** authorizing indefinite retention (`EVD-021`, retention dependency `UD-055`); every access, annotation, correction and export appends a custody event (`EVD-022`, `REQ-828`); artefacts hashed and digest-referenced — a mismatch is an incident, not a routine correction (`EVD-037`); conflict resolution names which record governs and why (`EVD-018`, `REQ-832`) |
| Normal path | Preservation flag set; custody ledger grows by one event per handling act; case remains reconstructible (`REQ-794`) |
| Alternative paths | Export requested → `FPW-040` (separate permission); retention conflict → conservative branch (`REQ-869`) |
| Failure behaviour | Preservation cannot be applied → the case is labelled and the record's exposure is stated, never silently compacted; spine write failure → no committed act (`FR-03`) |
| Resulting state, player experience | case evidence `PRESERVED`; no player-visible change until a decision |
| Permitted action, audit evidence | Preservation, annotation, correction-by-append, export request. Writes `EVD-026` investigation/evidence reads and writes, privileged access |
| Security and privacy constraints | Evidence is case-scoped and minimised, never copied into logs, analytics or a support tool's default view (`EVD-024`, `REQ-831`); spine rows are never sampled away (`EVD-034`) |
| Trace and tests | `EVD-018`, `EVD-021`–`EVD-024`, `EVD-028`, `EVD-035`–`EVD-037`, `TR-091` · `REQ-794`, `REQ-827`, `REQ-828`, `REQ-831`, `REQ-832`, `REQ-853` · `UD-055` **Open** · `FPA-049`–`FPA-054`, `FPE-016`–`FPE-018` |

---

## 9. Family C — Finding, decision and sanction

### FPW-011 — Investigation to a conduct finding or an inconclusive closure

| Field | Content |
|---|---|
| ID and purpose | `FPW-011` — gather server records, test the named rule elements, and reach `E3` or `EX` |
| Initiator, permissions, trigger | `INV` (`ADM-023`: may open, preserve and recommend; may not sanction or decide an appeal); trigger: `FPW-008` sufficient, or triage directs investigation |
| Systems and responsibilities | B-12 owns the finding; each contributing subsystem owns its own facts (`REQ-815`, `MOD-031`) |
| Required input and access | `V-` class and the eleven elements relied on (`FP-019`, `FP-021`); server records via purpose-bound reads (`FPW-036`); shared-context declarations where they exist (`MA-003`) |
| Validation and decision sequence | Element-by-element test; intent or knowledge required only where Annex A says so (`FP-022`); demonstrated impact where required (`FP-023`); attempt actionable only where named and at `E2` (`FP-024`); manufactured-false-agency test applied before any collusion charge (`CO-001`, `CO-002`); graph or clustering output is queue input only (`CO-004`) |
| Normal path | A recommended finding with evidence references, or an `EX` closure with what was examined (`EVD-008`) |
| Alternative paths | Value-only anomaly → `FPW-021` correction with no person-level claim (`FP-016`); administrative privilege misuse → `V-16` plus incident (`FP-030`) |
| Failure behaviour | Investigation record corrupt → the case becomes inconclusive, never proven (12A posture 3, restated by `FR-14`/`REQ-794`: return to the last recorded state, never auto-close); a subsystem source unavailable → reversible hold, never a permanent measure (`SEC-023`, `REQ-864`) |
| Resulting state, player experience | case `INVESTIGATING → DECISION_PENDING` or `CLOSED(EX)`; the subject sees nothing yet unless a hold is in force (`MOD-030`) |
| Permitted action, audit evidence | Recommendation and record only. Writes `EVD-026` investigation and evidence writes |
| Security and privacy constraints | No violation language before `E3` (`FP-020`); the investigation record is `MOD` confidential and never shown to the reported party (`PRV-012`) |
| Trace and tests | `FP-019`–`FP-024`, `EVD-008`, `EVD-012`, `CO-001`–`CO-004`, `ADM-023` · `REQ-767`, `REQ-784`, `REQ-785`, `REQ-787`, `REQ-794`, `REQ-815` · `FPA-055`–`FPA-062`, `FPE-019`, `FPE-020` |

### FPW-012 — Severity assessment and repetition adjustment

| Field | Content |
|---|---|
| ID and purpose | `FPW-012` — compute the ordinal severity and the single repetition adjustment, with no invented constant |
| Initiator, permissions, trigger | `SMOD` (or `MOD` within `T0`–`T2`); trigger: a recommended `E3` finding |
| Systems and responsibilities | B-12 owns severity; Annex A owns the base band; the owner's `UD-053` and Prompt 14 own the weights |
| Required input and access | Base class severity `S_c`, proven impact `I_p`, intent `K`, mitigation `M`, confirmed prior count `R` within the review window |
| Validation and decision sequence | `SEV = S_c + I_p + K − M`, floored at 0, **no repetition term** (`F-FP-001`); then `SEV_R = SEV + min(R,2) × q` — the only place repetition enters (`F-FP-011`, `FP-025`); only confirmed `E3` priors count; an unconfirmed report, dismissed case or `EX` closure is never an aggravating fact (`FP-025`, `REQ-813`); mitigation may reduce a tier but does not erase material impact (`FP-026`) |
| Normal path | Ordinal severity and tier band recorded as an input to `FPW-013`, subject to authority |
| Alternative paths | Unknown prior history → `R = 0` (`F-FP-011` §9); a successful appeal removes the prior from the count (`F-FP-011` §10) |
| Failure behaviour | A missing proven impact is `I_p = 0` only where Annex A does not require impact, otherwise `INCONCLUSIVE` (`F-FP-001` §9); weights provisional — the band is stated, **no approved numeric penalty is claimed** (`REQ-816`, `UD-053` **Open**) |
| Resulting state, player experience | unchanged case state |
| Permitted action, audit evidence | Assessment. Writes `EVD-026` moderation action with inputs and outcome |
| Security and privacy constraints | Economic correction is never increased by a prior violation (`MOD-039`, `COR-010`) |
| Trace and tests | `FP-025`, `FP-026`, `MOD-039`, `MOD-055`, `F-FP-001`, `F-FP-011`, `FP-P01`–`FP-P03` · `REQ-812`, `REQ-813`, `REQ-816` · `UD-053` **Open** · `FPA-063`–`FPA-068`, `FPE-021` |

### FPW-013 — Tier authority, second review and cross-system capability check

| Field | Content |
|---|---|
| ID and purpose | `FPW-013` — check that the actor may impose the tier, that review exists where required, and that the consequence stays inside B-12's own authority |
| Initiator, permissions, trigger | `MOD`, `SMOD` or the owner-authorized threshold; trigger: `FPW-012` produced a tier band |
| Systems and responsibilities | B-12 decides; **B-03 applies** any account-level consequence (`INT-001`); the owning subsystem's rule remains authoritative for its own capability (`MOD-031`) |
| Required input and access | Proposed tier, actor role, evidence state, staffing availability, affected capabilities |
| Validation and decision sequence | `T0`–`T2` within published moderator scope; `T3` requires a senior moderator or second review where staffing permits; `T4`/`T5` require the owner-authorized threshold and independent review where available (`MOD-037`); tier-to-evidence gate — `T1`/`T2` need at least `E2`, `T3`–`T5` need `E3` plus stated impact, and no tier may be imposed on `E0`, `E1` or `EX` (`MOD-038`); second-person review required above first-tier suspension, permanent measures, emergency actions and appeals against a senior moderator (`MOD-022`); prohibition-list check that the consequence is not a balance, battle, election, standing, snapshot, objective result, treaty or Alliance state change (`ADM-001`); no collective punishment of an Alliance, household or group (`CO-010`) |
| Normal path | Authority satisfied → `FPW-014`. Authority unavailable → hold at decision, labelled `unsegregated`, never silently downgraded past the rule (`MOD-022`) |
| Alternative paths | The capability belongs to another system → B-12 acts on the account only and leaves the subsystem rule intact (`MOD-031`, `INT-006`…`INT-011`) |
| Failure behaviour | Unapproved tier duration → `PROVISIONAL_BLOCK` from `F-FP-005`, never a default length (`FP-P04`, `FP-P05`, `UD-053` **Open**) |
| Resulting state, player experience | case `DECISION_PENDING → DECIDED` |
| Permitted action, audit evidence | Decision and, where required, second-review record. Writes `EVD-026` moderation action and administrative override |
| Security and privacy constraints | A moderator may not edit game state, balance, election, snapshot or history (`MOD-019`); a moderation power may never be used to favour an Alliance, punish a report, win a competition, discourage diplomacy, enforce an in-game agreement or obtain private information (`MOD-024`) |
| Trace and tests | `MOD-019`, `MOD-022`, `MOD-024`, `MOD-031`, `MOD-037`, `MOD-038`, `ADM-001`, `CO-010`, `F-FP-005` · `REQ-812`, `REQ-815`, `REQ-816`, `REQ-861` · `UD-053`, `UD-054` **Open** · `FPA-069`–`FPA-076`, `FPE-022`, `FPE-023` |

### FPW-014 — Sanction record and player notice assembly

| Field | Content |
|---|---|
| ID and purpose | `FPW-014` — build a sanction record a player can understand and contest, with method secrecy enforced by rule |
| Initiator, permissions, trigger | `MOD`/`SMOD`; trigger: `FPW-013` produced a decision |
| Systems and responsibilities | B-12 owns the record and content bounds; B-02 owns notice classes; Prompt 13 owns the surface (`INT-012`) |
| Required input and access | `V-` class, relied-on rule element, evidence class, tier, end condition, appeal route, associated correction if any |
| Validation and decision sequence | Every significant action states all seven in player-usable terms (`MOD-017`, `REQ-821`); detection methods, thresholds, other players' data and investigation detail withheld **by rule, not reviewer discretion** (`MOD-018`, `REQ-835`); where a correction also applies, the notice states that the correction is separate (`FP-031`, `MOD-055`); no enforcement action is invisible to the affected account, and any delay records the delay and its review (`MOD-030`, `ADM-030`) |
| Normal path | Notice committed with the record; delivery to B-02/Prompt 13 for display |
| Alternative paths | Deliberate delay for an active investigation → recorded delay plus review (`MOD-030`) |
| Failure behaviour | Delivery failure does not block the action: the notice enters the in-game digest and the failure is recorded (`FR-07`, `REQ-850`); notice assembly failure → the transaction fails closed, no unrecorded action exists (`FR-03`) |
| Resulting state, player experience | record `COMMITTED`; the player can read the rule relied on and appeal |
| Permitted action, audit evidence | Record and notice. Writes `EVD-026` moderation and disciplinary actions |
| Security and privacy constraints | Never reveals who reported (`INT-017`), another player's restriction state (`PRV-019`), or whether an account exists (`PRV-020`) |
| Trace and tests | `MOD-017`, `MOD-018`, `MOD-030`, `ADM-030`, `FP-031`, `REQ-821` · `INT-012`, `12A-INT-16`, `12A-INT-24` · `FPA-077`–`FPA-084`, `FPE-024` |

### FPW-015 — Case closure and outcome recording

| Field | Content |
|---|---|
| ID and purpose | `FPW-015` — close every case with one of six outcomes, a stated reason and the evidence state |
| Initiator, permissions, trigger | `MOD`, `SMOD` or `APL` for an appeal-driven closure; trigger: a decision, an `EX` determination, or a bar on reopening |
| Systems and responsibilities | B-12 owns the case record; the spine records the fact (`INT-014`) |
| Required input and access | Outcome ∈ {`NO_ACTION`, `INCONCLUSIVE`, `CORRECTION_ONLY`, `CONDUCT_ONLY`, `CORRECTION_AND_CONDUCT`, `REFERRED`} (`EVD-020`); reason; evidence state; reviewer and date (`EVD-012`) |
| Validation and decision sequence | Closure states the reason **and** the evidence state (`EVD-020`); the record reconstructs what was examined (`REQ-794`); a referral names the receiving owner without transferring record ownership (`ADM-029`) |
| Normal path | `CLOSED`; the reporter receives the bounded outcome notice (`EVD-008`); preservation may be released under the retention rule (`FPW-041`) |
| Alternative paths | Referred to another owner (e.g. an Alliance expulsion remains `UD-044`) → `REFERRED` with no B-12 adjudication (`INT-018`) |
| Failure behaviour | Ambiguous outcome → `INCONCLUSIVE`, never the more convenient record (`EVD-018`); a closure write failure leaves the case open (`FR-03`) |
| Resulting state, player experience | case `CLOSED`; reporter sees the bounded outcome |
| Permitted action, audit evidence | Closure. Writes `EVD-026` moderation action and appeal outcome where applicable |
| Security and privacy constraints | The closure summary is bounded; the underlying `MOD` record is not disclosed to the reported party (`PRV-012`) |
| Trace and tests | `EVD-008`, `EVD-012`, `EVD-020` · `REQ-766`, `REQ-794`, `REQ-815` · `UD-044` **Open** · `FPA-085`–`FPA-090`, `FPE-025` |

---

## 10. Family D — Restriction, identity and association

### FPW-016 — Enforcement application through B-03 account state

| Field | Content |
|---|---|
| ID and purpose | `FPW-016` — express every consequence as an account-level action that **only B-03 applies** |
| Initiator, permissions, trigger | `SMOD`/`MOD` within authority requests it; B-03 (`ACC-021` operator actions with a reason and a record) applies it |
| Systems and responsibilities | B-03 owns account state and lifecycle (`INT-001`); B-12 owns the enforcement decision and record (`INT-002`); nation state and pair state are separate objects and are never the vehicle of a sanction (`MA-002`, `REQ-782`-adjacent) |
| Required input and access | Enforcement target account identifier, action class, tier, reason code, end condition, case reference, idempotency key |
| Validation and decision sequence | Target is an account, never a nation field or pair state (`INT-002`); actor authorized for the object separately (`SEC-002`); request audited (`INT-001`); B-12 never re-parents a nation or changes ownership (`REQ-859`, `12A-INT-03`) |
| Normal path | B-03 transitions the account state and confirms; B-12 records the applied action; preservation-order semantics remain B-03's |
| Alternative paths | The consequence is a capability restriction rather than an account state → applied as a scoped limitation with its stated scope and expiry (`MOD-012`); a pair restriction is required → the owning pair rule applies it, B-12 never invents a fourth state object (`MA-002`) |
| Failure behaviour | B-03 unavailable → the action is not applied and the decision remains pending; no partial application exists (`FR-01`, `FR-02`). A duplicate request coalesces to the first committed result (`FP-013`, `SEC-008`) |
| Resulting state, player experience | account `ACTIVE → RESTRICTED`/`SUSPENDED`; the player sees the notice from `FPW-014` and retains appeal plus data-subject routes (`MOD-015`) |
| Permitted action, audit evidence | Account-level enforcement application. Writes `EVD-026` moderation and disciplinary actions |
| Security and privacy constraints | No credential is involved or stored (`SEC-027`); no other player's status is disclosed (`PRV-019`) |
| Trace and tests | `INT-001`, `INT-002`, `MA-002`, `MOD-012`, `MOD-015`, `SEC-002`, `SEC-008`, `ACC-021` · `REQ-777`, `REQ-818`, `REQ-859` · `12A-INT-01`, `12A-INT-02`, `12A-INT-03` · `FPA-091`–`FPA-098`, `FPE-026`, `FPE-027` |

### FPW-017 — Restriction duration, expiry and extension

| Field | Content |
|---|---|
| ID and purpose | `FPW-017` — make every temporary measure turn-counted, self-expiring, and extendable only by a new decision |
| Initiator, permissions, trigger | `SYS` at each turn boundary; `SMOD` may extend |
| Systems and responsibilities | B-12 owns the measure; B-02 supplies the boundary; the owning subsystem's cadence is unchanged (`D-015`, `FP-034`) |
| Required input and access | Tier, base turns `D_base(T)`, extension count `x`, tier maximum `D_max(T)`, start boundary |
| Validation and decision sequence | `D = D_base(T) × (1 + x)` capped at `D_max(T)`, ceiling to the next whole turn (`F-FP-005`); every temporary measure expressed in turn boundaries, never wall-clock, ending at the next boundary if it would fall between them (`MOD-040`); expiry is automatic and extension is a new decision with a new reason and where required a new review (`MOD-041`); `T1` is a warning with no duration |
| Normal path | Measure expires; account state returns to `ACTIVE`; the record states the expiry |
| Alternative paths | `D_base`/`D_max` unapproved → `PROVISIONAL_BLOCK`: the measure may be imposed only with an explicitly recorded, reviewable end condition, and no duration may be presented as an approved value (`FP-P04`, `FP-P05`, `UD-053` **Open**) |
| Failure behaviour | Boundary processing failed → the measure does not silently persist; recovery reconciles to the authoritative state and records the gap (`FR-14`, `REQ-863`) |
| Resulting state, player experience | restriction `IN_FORCE → EXPIRED`; the player sees the end condition from the original notice (`MOD-017`) |
| Permitted action, audit evidence | Expiry and extension. Writes `EVD-026` moderation action |
| Security and privacy constraints | Expiry is not an expungement: the record survives (`MOD-034`) |
| Trace and tests | `MOD-012`, `MOD-040`, `MOD-041`, `F-FP-005`, `FP-P04`, `FP-P05` · `REQ-812`, `REQ-818`, `REQ-821` · `UD-053` **Open** · `FPA-099`–`FPA-104`, `FPE-028` |

### FPW-018 — Sanction survival across reroll, retirement and association change

| Field | Content |
|---|---|
| ID and purpose | `FPW-018` — ensure a reroll is not an amnesty, and an association change is not a laundering route |
| Initiator, permissions, trigger | `SYS` on a reroll or retirement request; B-03 executes (`RRL-016`, `RRL-017`, `ECN-204`) |
| Systems and responsibilities | B-03 owns the reroll and lifecycle; B-04 owns the economic consequences; B-12 owns the enforcement record and its survival (`MOD-033`) |
| Required input and access | Account identity, pending cases, active restrictions and preservation orders, pre-reroll transfer pattern |
| Validation and decision sequence | A correction or restriction attaches to the account and survives a nation reroll (`REQ-818`, `MOD-033`, `RRL-016`); a pending case continues and is not closed by retirement (`RRL-017`); a preservation order blocks the reroll (`RRL-021`, `ECN-204`); pre-reroll divesting to a linked account is a review pattern, not an automatic reversal (`RRL-015`); protection is not re-granted by a reroll (`RRL-018`); an identity-laundering attempt through a reroll is treated as `V-05`/`V-01` evidence, not as a new identity (`WEE-051` precedent) |
| Normal path | New nation state is created; the account's sanctions, cases and history remain attached |
| Alternative paths | Starter-farming pattern → review signal to `FPW-005` (`ECN-207`, `RRL-024`) |
| Failure behaviour | Survival check unavailable → the reroll proceeds only with the enforcement record re-attached at the next reconciliation, and the gap is recorded (`FR-11`-class integrity exposure is an incident, `SEC-026`) |
| Resulting state, player experience | account unchanged in state; nation reset; restriction still in force with the original notice reference |
| Permitted action, audit evidence | Survival verification and preservation-order request. Writes `EVD-026` moderation action, permission-adjacent account events |
| Security and privacy constraints | B-12 never edits an account state directly; B-03 does (`INT-001`) |
| Trace and tests | `MOD-033`, `MA-002`, `V-05`, `RRL-015`–`RRL-021`, `ECN-204` · `REQ-783`, `REQ-818` · `12A-INT-01`, `12A-INT-03` · `FPA-105`–`FPA-110`, `FPE-029`, `FPE-030` |

### FPW-019 — Shared-context declaration record and visibility

| Field | Content |
|---|---|
| ID and purpose | `FPW-019` — let a player attest an association without ever making the attestation an exemption or an identity claim |
| Initiator, permissions, trigger | `PLAYER`, `W0` |
| Systems and responsibilities | B-12 owns the declaration; B-03 owns account identity (`INT-016`) |
| Required input and access | Author account, named associated accounts, shared device/household/institution/network statement |
| Validation and decision sequence | Declaration is review evidence only; it does not clear a pair, permit a transfer, reduce a restriction or make its absence aggravating (`MA-003`); visible only to the author accounts and the integrity role, deletable by the author, never a disclosure channel (`MA-004`, `REQ-780`); never proves identity and never supports more than the lowest preventive tier (`MA-005`, `MA-011`, `NET-039`) |
| Normal path | `RECORDED`, cited by `FPW-007`/`FPW-011` where relevant |
| Alternative paths | Author deletes it → `DELETED` with the deletion recorded as an event, not an edit (`PRV-022`, `EVD-029`); declaration contradicts an evidenced flow → the flow governs (`MA-006`) |
| Failure behaviour | Storage unavailable → retryable failure; absence is never inferred (`FR-06`) |
| Resulting state, player experience | declaration row exists for the author and integrity role only |
| Permitted action, audit evidence | Record and delete. Writes `EVD-026` privileged access when the integrity role reads it (`ADM-008`) |
| Security and privacy constraints | The declaration names third parties: it is `PERSONAL`/`MOD` handling and never `PUB` (`PRV-013`, `REQ-780`) |
| Trace and tests | `MA-003`–`MA-006`, `MA-011`, `NET-039`, `PRV-022` · `REQ-778`, `REQ-779`, `REQ-780`, `REQ-781` · `12A-INT-20` · `FPA-111`–`FPA-116`, `FPE-031` |

### FPW-020 — Wrong-account-association correction and separation

| Field | Content |
|---|---|
| ID and purpose | `FPW-020` — repair a misattribution, which is the most damaging failure mode this system has |
| Initiator, permissions, trigger | `MOD`/`INV` or the affected player's dispute; trigger: evidence that two accounts were treated as one controller |
| Systems and responsibilities | B-03 owns the account objects; B-12 owns the association record and the correction (`REQ-865`) |
| Required input and access | The association claim, its basis, the affected accounts, every consequence that flowed from it |
| Validation and decision sequence | Association error → separate the accounts, lift the restrictions, record the correction and notify (`REQ-865`, `COR-013`); reverse first, investigate second (12A posture 6, operationalised through `MOD-034` and `FPW-024`); never adopt the more convenient record (`EVD-018`) |
| Normal path | Restrictions lifted by appended events referencing the originals; the case is relabelled; each affected player is notified |
| Alternative paths | Association was correct → the dispute closes `NO_ACTION` with a reasoned notice and its appeal route |
| Failure behaviour | Consequences already executed → each is reversed through its own owner's path, not bulk-edited (`INT-003`, `COR-004`) |
| Resulting state, player experience | account states restored; the record keeps the original error as history (`MOD-034`) |
| Permitted action, audit evidence | Correction and notification. Writes `EVD-026` moderation action, financial corrections where value moved |
| Security and privacy constraints | The notification names the correction, not the detector or the other party (`PRV-019`, `PRV-020`) |
| Trace and tests | `MOD-034`, `COR-004`, `COR-013`, `EVD-018`, `MA-011` · `REQ-783`, `REQ-865`, `REQ-832` · `12A-INT-01` · `FPA-117`–`FPA-122`, `FPE-032`, `FPE-033` |

---

## 11. Family E — Correction and recovery

### FPW-021 — Correction instruction to the owning subsystem

| Field | Content |
|---|---|
| ID and purpose | `FPW-021` — correct an impossible effect by instructing the owner's recorded path, never by writing the value |
| Initiator, permissions, trigger | `MOD`/`INV`/`SYS` where `EVD-002` permits; trigger: the record proves an effect the published rules could not produce (`FP-016`, `EVD-010` row 3) |
| Systems and responsibilities | **B-04 executes a ledger correction** (`INT-003`, `ADM-012`); B-05 (`INT-004`, `URB-143`), B-06 (`INT-005`, `DMP-122`), B-07 (`INT-006`), B-09 (`INT-008`), B-10 (`INT-009`), B-11 (`INT-010`, `INT-011`) each execute through their own path; B-12 never writes another subsystem's state (`FP-012`, `MOD-019`) |
| Required input and access | Case reference, original transaction or state reference, correction type from `COR-001`, reason code, idempotency key, computed amount from `FPW-022` |
| Validation and decision sequence | Every corrective transaction references the original — an unreferenced correction is invalid (`COR-002`); a correction needs no finding about a person and is always reversible (`MOD-051`); the actor is not the balance holder (`ADM-012`); reason code exists in the owning registry (`ECN-170`); value, authorization and audit writes fail closed together (`FR-01`–`FR-03`) |
| Normal path | The owning ledger appends `CORRECTION` or `ILLICIT_REMOVAL` with a signed delta, records the operator role, case reference and reason, and notifies the affected account (`MOD-054`, `COR-015`) |
| Alternative paths | A political state or an election result is involved → the correction is an `ADJUSTMENT` that names the original and **may not set `government_id`** (`INT-005`, `DMP-122`, `DMP-267`); a city facility is involved → only by `ADJUSTMENT`/`REVERSAL` referencing the original, never an edit of `capacity`, `housing` or book value (`URB-143`) |
| Failure behaviour | Cannot complete → roll back exactly and retry with the **same** idempotency key; a partial correction is prohibited (`COR-018`, `FR-09`); a missing lawful counterfactual → `NO_CALCULATION` plus incident, never zero (`F-FP-002` §9) |
| Resulting state, player experience | ledger balance restored toward the counterfactual lawful state; the account is told a correction occurred, what changed and how to dispute it |
| Permitted action, audit evidence | Correction instruction only. Writes `EVD-026` financial corrections; spine event with case and original reference (`COR-016`) |
| Security and privacy constraints | No correction mints value, forgives a debt by editing, or creates a negative balance (`SEC-020`, `COR-012`); an administrative adjustment is permitted only under published policy and never simulates gameplay or grants a reward (`SEC-019`) |
| Trace and tests | `FP-012`, `FP-016`, `COR-001`–`COR-006`, `COR-013`–`COR-018`, `MOD-051`–`MOD-055`, `ADM-012`, `SEC-019`, `SEC-020` · `REQ-817`, `REQ-819`, `REQ-820`, `REQ-845`, `REQ-861` · `INT-003`–`INT-005`, `12A-INT-04`, `12A-INT-05`, `12A-INT-07`, `12A-INT-08` · `UD-052` **Open** · `FPA-123`–`FPA-136`, `FPE-034`–`FPE-036` |

### FPW-022 — Correction amount and illicit benefit determination

| Field | Content |
|---|---|
| ID and purpose | `FPW-022` — compute the excess to remove and the benefit ceiling from the record |
| Initiator, permissions, trigger | `SYS` under B-12 instruction, executed with the owning ledger's arithmetic; trigger: `FPW-021` accepted |
| Systems and responsibilities | B-04 owns value units and the lawful counterfactual; B-07 owns market prices at a transaction boundary; B-12 owns the instruction and the cap rule (`MOD-053`) |
| Required input and access | `V_obs`, `V_law`, the linked transaction set `T` with `d_t` and `e_t` |
| Validation and decision sequence | `B_i = Σ max(d_t − e_t, 0)` over proved-linked transactions only; transfers to innocent third parties excluded unless the record proves the flow (`F-FP-003`); `C = min(max(V_obs − V_law, 0), B_i)` — observed minus lawful, never below zero, never above the benefit (`F-FP-002`); a shortfall against the lawful state is a **loss** handled by `FPW-025`, not by this removal (`F-FP-002` §1) |
| Normal path | Amount recorded with its inputs and formula reference; `FPW-021` executes |
| Alternative paths | No linked transactions → `B_i = 0`, no correction; unvaluable leg → `INCONCLUSIVE` for that leg, no fabricated estimate (`F-FP-003` §9) |
| Failure behaviour | An unvaluable or missing input never defaults to a permissive value (`GOV-006`); a market-priced asset uses the owning market's recorded price at the transaction boundary — B-12 defines no price (`F-FP-003` §10) |
| Resulting state, player experience | no visible change until the correction commits |
| Permitted action, audit evidence | Calculation. Writes `EVD-026` financial corrections with inputs |
| Security and privacy constraints | Repetition never increases an economic correction (`F-FP-011` §6, `MOD-039`) |
| Trace and tests | `MOD-053`, `COR-003`, `COR-006`, `F-FP-002`, `F-FP-003`, `F-FP-014` · `REQ-782`, `REQ-817`, `REQ-845` · `UD-052` **Open** · `FPA-137`–`FPA-144`, `FPE-037`, `FPE-038` |

### FPW-023 — Illicit removal, flow reach and insolvency handling

| Field | Content |
|---|---|
| ID and purpose | `FPW-023` — remove a benefit that moved, without inventing a debt mechanic |
| Initiator, permissions, trigger | `MOD`/`SMOD` on an established flow; trigger: value obtained through a violation left the violating account |
| Systems and responsibilities | B-04 owns recovery order and the ledger; B-07 owns market legs; B-09's Alliance container is screened, not treated as a shield (`ALL-159`); B-12 owns the instruction |
| Required input and access | The flow set, each leg's recipient, the proven linkage, each account's held value |
| Validation and decision sequence | Removal follows the flow to the benefiting account even where the account is also sanctioned, and is recorded as a correction, not a fine (`MOD-057`, `COR-011`); where a benefiting account cannot cover the removal, the balance floors at zero and the shortfall is recorded — **no debt mechanic is invented** (`COR-012`); correction against either or both sides of a flow is structurally available (`MA-007`, `CO-009`) but its **reach** is owner-reserved (`REQ-782`, `UD-052` **Open**) — until decided, only the receiving-side leg may be executed |
| Normal path | `ILLICIT_REMOVAL` appended per leg with the original reference; shortfall recorded |
| Alternative paths | Value routed through an Alliance container or tax to lose pairwise attribution → `V-11` case, with Alliance treasury authority untouched (`CO-008`, `UD-046` **Open**) |
| Failure behaviour | Ambiguous reach → reversible hold on the affected leg plus escalation to the owner dependency; never an unauthorised both-sides correction |
| Resulting state, player experience | balances changed on the evidenced legs; each affected account is notified of its own change only |
| Permitted action, audit evidence | Removal and shortfall record. Writes `EVD-026` financial corrections |
| Security and privacy constraints | Third-party data is never disclosed in a correction notice (`MOD-054`) |
| Trace and tests | `MA-007`, `CO-008`, `CO-009`, `COR-011`, `COR-012`, `MOD-057`, `V-11`, `ALL-159` · `REQ-782`, `REQ-817`, `REQ-820` · `UD-052`, `UD-046` **Open** · `FPA-145`–`FPA-152`, `FPE-039`–`FPE-041` |

### FPW-024 — Reversal and restitution through the owning path

| Field | Content |
|---|---|
| ID and purpose | `FPW-024` — undo a specific transaction exactly, and let the owning system restore what moved |
| Initiator, permissions, trigger | `APL` on an upheld appeal; `MOD`/`SMOD` on a wrong-action finding; trigger: a decision to reverse (`MOD-047`) |
| Systems and responsibilities | The owning subsystem executes the reversal in its own ledger (`ECN-166`: `REVERSAL` with the opposite delta and `source_event_id`, then a corrected `ADJUSTMENT`); B-12 instructs and records (`MOD-048`) |
| Required input and access | The referenced original, its remaining unreversed effect, the case reference, the key |
| Validation and decision sequence | A reversal appends the exact opposite of the referenced transaction's **remaining unreversed** effect; a partial reversal is bounded by that remainder; a duplicate reversal coalesces and adds nothing (`F-FP-014` §5, `COR-005`); a reversal with no resolvable original returns `NO_ORIGINAL` and is not applied (`F-FP-014` §9); no administrator calculates or types a compensation amount (`MOD-048`) |
| Normal path | Restriction ends, suspension lifts, value returns; the record states the reversal and its reason (`MOD-047`) |
| Alternative paths | Wrong correction → further appended transaction referencing the wrong correction (`COR-009`); state restoration after a technical failure → `REVERSAL`/`CORRECTION` restoring the authoritative pre-failure state, never the violator's expected gain (`MOD-059`, `COR-013`) |
| Failure behaviour | Partial application prohibited → rollback and same-key retry (`COR-018`); an unreconciled result is an incident (`COR-017`) |
| Resulting state, player experience | prior state restored; the player receives the reversal notice and its reason |
| Permitted action, audit evidence | Reversal and restitution instruction. Writes `EVD-026` financial corrections, appeal outcomes |
| Security and privacy constraints | A reversal is not an expungement — the original stays visible to the audit role (`MOD-034`, `EVD-029`) |
| Trace and tests | `MOD-047`, `MOD-048`, `MOD-059`, `COR-005`, `COR-009`, `COR-013`, `COR-017`, `COR-018`, `F-FP-014`, `ECN-166` · `REQ-836`, `REQ-817`, `REQ-865` · `FPA-153`–`FPA-160`, `FPE-042` |

### FPW-025 — Compensation for a proven project-caused loss

| Field | Content |
|---|---|
| ID and purpose | `FPW-025` — restore a loss the project caused, as an authorized corrective transaction rather than goodwill |
| Initiator, permissions, trigger | `SMOD` with a recorded finding of project error; trigger: a proven loss caused by an enforcement or system error (`MOD-056`) |
| Systems and responsibilities | B-04 executes through the ledger; the owner holds the compensation policy and cap (`REQ-816`-adjacent, `GOV-008`) |
| Required input and access | Proven loss `L_p`, the owner cap `C_max`, the case reference |
| Validation and decision sequence | `P = min(L_p, C_max)` (`F-FP-015`); compensation requires a recorded finding of project error and a stated loss, and is never a discretionary grant (`COR-014`); compensation never exceeds proven loss and never creates a negative balance (`COR-006`); an unapproved `C_max` returns `PROVISIONAL_BLOCK` — no compensation may be paid as if a policy existed (`F-FP-015` §9) |
| Normal path | `COMPENSATION` appended with its reference; the account is notified (`COR-015`) |
| Alternative paths | A systemic incident with a published schedule → still capped, still recorded (`F-FP-015` §10) |
| Failure behaviour | No policy → the loss is recorded as an unresolved exposure with the owner dependency named; the workflow does not improvise a number |
| Resulting state, player experience | balance restored up to the cap; notice states type, amount, reason and appeal route |
| Permitted action, audit evidence | Compensation. Writes `EVD-026` financial corrections |
| Security and privacy constraints | No sanction or compensation creates value for the operator, a reporter or another player (`MOD-058`) |
| Trace and tests | `MOD-056`, `MOD-058`, `COR-006`, `COR-014`, `F-FP-015`, `FP-P09`, `GOV-008` · `REQ-816`, `REQ-817`, `REQ-836` · `UD-053` **Open** · `FPA-161`–`FPA-166`, `FPE-043` |

### FPW-026 — Multiple-correction ordering, reconciliation and rollback

| Field | Content |
|---|---|
| ID and purpose | `FPW-026` — order competing corrections, prove the ledger conserved, and surface conflicts to a reviewer |
| Initiator, permissions, trigger | `SYS` at the owning subsystem's next valid boundary; `MOD` on a surfaced conflict |
| Systems and responsibilities | Each owning subsystem applies and reconciles its own ledger; B-12 owns the case order and the conflict surface (`MOD-032`) |
| Required input and access | Correction records with `case_closed_turn`, case order `n`, type `y`, amount `a`, opening and closing balances |
| Validation and decision sequence | Sort by `(case_closed_turn, n, type_rank)` with `REVERSAL=1, CORRECTION=2, ILLICIT_REMOVAL=3, COMPENSATION=4, ADMIN_ADJUSTMENT=5`; ties use the original transaction ID ascending; no correction reorders a closed turn (`F-FP-004`, `COR-007`); conservation check `Z = O + L + C + R + P + X + A`, `Z ≥ 0`, every term referencing a recorded transaction (`COR-003`, `F-FP-014`); a nonzero residual fails the correction and raises an incident (`COR-017`); duplicate or conflicting enforcement against one account is surfaced, never silently applied or dropped (`MOD-032`, `REQ-820`) |
| Normal path | Ordered application, reconciled totals, residual recorded as zero |
| Alternative paths | Missing case turn → `HOLD`, never a guessed order (`F-FP-004` §9); a legal hold suspends application until released (`F-FP-004` §10) |
| Failure behaviour | Reconciliation failure → incident, and the affected value path stops while the world keeps running (12A posture 11 restated by `FR-01`/`REQ-862`); reversal order for a compound cross-system exploit remains a specification question answered structurally here and registered against `12A-OPEN-013` |
| Resulting state, player experience | balances consistent with the ordered corrections; notifications per affected account |
| Permitted action, audit evidence | Ordering, reconciliation and incident creation. Writes `EVD-026` financial corrections and integrity results |
| Security and privacy constraints | Reconciliation output is `AUDIT`/`OPS` class, never published (`PRV-011`, `PRV-015`) |
| Trace and tests | `MOD-032`, `COR-003`, `COR-007`, `COR-017`, `COR-018`, `F-FP-004`, `F-FP-014` · `REQ-820`, `REQ-817`, `REQ-855` · `12A-OPEN-013` · `FPA-167`–`FPA-176`, `FPE-044`–`FPE-047` |

---

## 12. Family F — Appeals

### FPW-027 — Appeal filing and window computation

| Field | Content |
|---|---|
| ID and purpose | `FPW-027` — accept one appeal per account-affecting action, on stated grounds, inside the structured window |
| Initiator, permissions, trigger | `PLAYER` (subject), `W0`; trigger: a `T1`-or-above action or a correction dispute exists (`MOD-042`, `COR-008`) |
| Systems and responsibilities | B-12 owns the appeal record (`INT-018`); Prompt 13 owns the surface (`INT-020`) |
| Required input and access | Action reference, chosen ground from `MOD-044`, player's statement, new evidence if any |
| Validation and decision sequence | Grounds are exactly the five in `MOD-044`; disagreement with the rule's existence is routed as a policy feedback item, not an appeal; one appeal per action (`REQ-833`); `T0` has no appeal because it imposes no burden, though a factual correction may still be requested (`MOD-042`); window `t_close = t_n + W` (`F-FP-006`) |
| Normal path | appeal `FILED`; `FPW-028` decides the in-force question |
| Alternative paths | Alliance expulsion appeal → not adjudicated by B-12; referred with `UD-044` named (`INT-018`) |
| Failure behaviour | Appeal service unavailable → action stays in force, the filing window extends by the recorded outage in turn boundaries, and no appeal is deemed abandoned (`FR-10`, `F-FP-006` §10); `W` unapproved → `PROVISIONAL_BLOCK` (`FP-P06`, `UD-059` **Open**): the filing route must exist and be usable, and no window may be enforced or advertised as an approved value |
| Resulting state, player experience | appeal `FILED` with acknowledgement; the player sees the outcome options, not the method |
| Permitted action, audit evidence | Filing. Writes `EVD-026` appeal outcomes class at decision time |
| Security and privacy constraints | No method, threshold or third-party data is disclosed in the acknowledgement (`MOD-018`) |
| Trace and tests | `MOD-042`–`MOD-044`, `MOD-050`, `COR-008`, `F-FP-006`, `FP-P06`, `FP-P12` · `REQ-833`, `REQ-835`, `REQ-834` · `UD-059` **Open** · `FPA-177`–`FPA-184`, `FPE-048` |

### FPW-028 — In-force state and reversible hold during an appeal

| Field | Content |
|---|---|
| ID and purpose | `FPW-028` — keep the action in force pending decision, unless a reversible hold is granted |
| Initiator, permissions, trigger | `APL`; trigger: appeal `FILED` |
| Systems and responsibilities | B-12 owns the hold; B-03 applies any account change (`INT-001`) |
| Required input and access | The action, its tier, reversibility, the requested grounds |
| Validation and decision sequence | Default is in force (`MOD-043`); a hold is recorded and **does not decide the appeal** (`MOD-043`); a hold may not be used to pre-empt the decision or to shorten a restriction covertly |
| Normal path | appeal `IN_FORCE`, optionally `HOLDED` |
| Alternative paths | Correction dispute → same structure: in force unless a reversible hold is granted (`COR-008`) |
| Failure behaviour | Hold write failure → the action simply remains in force; no silent relief is granted (`FR-01`) |
| Resulting state, player experience | the restriction continues, or is reversibly paused |
| Permitted action, audit evidence | Hold decision. Writes `EVD-026` appeal outcomes, moderation action |
| Security and privacy constraints | The hold status is never disclosed about another player (`PRV-019`) |
| Trace and tests | `MOD-043`, `COR-008` · `REQ-833`, `REQ-836` · `FPA-185`–`FPA-188`, `FPE-049` |

### FPW-029 — Appeal decision, four outcomes and independence label

| Field | Content |
|---|---|
| ID and purpose | `FPW-029` — decide in writing with one of four outcomes and state the independence actually achieved |
| Initiator, permissions, trigger | `APL` (`ADM-022`: may uphold, reduce, reverse or remand; may not investigate the original case or alter the audit record) |
| Systems and responsibilities | B-12 owns the decision; the owning subsystem executes any resulting correction or restitution (`FPW-024`) |
| Required input and access | Case record, bounded evidence needed to decide, the original decision and its reviewer |
| Validation and decision sequence | Outcome ∈ {`UPHELD`, `REDUCED`, `REVERSED`, `REMANDED`} — exactly four (`MOD-045`); a remand names the procedural defect and the reviewer (`MOD-045`); the explanation is sufficient to contest while withholding method, thresholds and third-party data **by rule** (`REQ-835`, `MOD-018`); the reviewer's independence is stated, and a decision by the original reviewer is labelled **not independent** (`MOD-049`); appeals against a senior moderator require a second reviewer where staffing exists (`MOD-022`) |
| Normal path | Written reasoned decision; upheld → `FPW-024` reversal, appended record correction and owning-subsystem restitution (`REQ-836`) |
| Alternative paths | Independence impossible → label plus disclosure (`REQ-837`, `UD-054` **Open**) |
| Failure behaviour | A reduction never converts a conduct finding into a correction or vice versa (`MOD-055`); a decision cannot be recorded → the appeal remains open (`FR-03`) |
| Resulting state, player experience | appeal `DECIDED`; the account sees the reasoning it is entitled to |
| Permitted action, audit evidence | Decision and any reversal instruction. Writes `EVD-026` appeal outcomes, administrative override |
| Security and privacy constraints | An appeals reviewer may not investigate the original case or edit the original record (`ADM-022`) |
| Trace and tests | `MOD-045`, `MOD-049`, `MOD-022`, `ADM-022`, `ADM-029` · `REQ-833`, `REQ-835`, `REQ-836`, `REQ-837` · `UD-054`, `UD-059` **Open** · `FPA-189`–`FPA-198`, `FPE-050`, `FPE-051` |

### FPW-030 — Reopening bar and repeated appeals

| Field | Content |
|---|---|
| ID and purpose | `FPW-030` — reopen only on new evidence or a procedural defect, and stop appeals becoming a stalling device |
| Initiator, permissions, trigger | `APL`/`SMOD`; trigger: a further submission on an already-decided action |
| Systems and responsibilities | B-12 owns the bar and the closure record |
| Required input and access | The new material, or the named procedural defect, and the prior decision record |
| Validation and decision sequence | Genuinely new evidence or a defect → reopen; otherwise close without re-investigation and record the closure (`MOD-046`, `REQ-834`); reversal of the prior is never automatic on a repeat submission |
| Normal path | appeal `CLOSED` (repeat) with the reason recorded |
| Alternative paths | New evidence arrives later and is genuine → reopen as a new decision with its own record |
| Failure behaviour | Ambiguity about whether the evidence is new → reviewed, and the determination recorded; never dismissed silently |
| Resulting state, player experience | appeal `CLOSED` |
| Permitted action, audit evidence | Closure or reopening. Writes `EVD-026` appeal outcomes |
| Security and privacy constraints | Repeated filings do not raise or lower any tier by themselves (severity comes only from confirmed priors, `FP-025`) |
| Trace and tests | `MOD-046`, `REQ-834` · `12A-DR-027` (capped appeals as a direction, not a rule) · `FPA-199`–`FPA-202`, `FPE-052` |

---

## 13. Family G — Emergency and incident

### FPW-031 — Emergency invocation, scope statement and bounded capability

| Field | Content |
|---|---|
| ID and purpose | `FPW-031` — contain an active incident with the least destructive capability, in a recorded, self-expiring envelope |
| Initiator, permissions, trigger | `EMG` (`R-EMG`) only, and only the named emergency role may invoke (`ADM-015`); trigger: an incident class declared by `FPW-033` |
| Systems and responsibilities | B-12 owns the measure and its bounds; B-02 owns the turn pipeline and whether a halt is needed (`INT-013`, `SEC-026`); the owning subsystems keep their state authority |
| Required input and access | Incident identifier, capability set to freeze, suspend or withhold, affected scope, start boundary, expiry, review owner |
| Validation and decision sequence | Permitted effects are **suspend, freeze, withhold** only; delete, confiscate, transfer and history rewrite are prohibited (`MOD-025`, `REQ-848`, `ADM-014`, `ADM-027`); scope, expiry and review owner stated before execution (`ADM-015`); expiry `t_e = t_s + D_e` (`F-FP-016`); the measure may not include the prohibition list (`ADM-014`) |
| Normal path | Measure recorded and executed, disclosure generated by `FPW-032`/`FPW-039`, review owner assigned |
| Alternative paths | Containment requires halting resolution → halt the affected value path rather than continue resolving on doubtful integrity, and disclose the halt as a delay (`SEC-026`, `REQ-858`) |
| Failure behaviour | **An emergency action that cannot be recorded does not execute; a silent emergency action is prohibited** (`FR-11`, `REQ-849`-adjacent); `D_e` unapproved → `PROVISIONAL_BLOCK`, never an indefinite measure (`F-FP-016` §9, `FP-P10`, `UD-056` **Open**) |
| Resulting state, player experience | measure `INVOKED → IN_FORCE`; players see a temporary measure and its review time, not the threat (`MOD-027`) |
| Permitted action, audit evidence | Freeze, suspend, withhold, preserve. Writes `EVD-026` emergency actions, privileged access |
| Security and privacy constraints | Emergency privilege does not create a superuser (`ADM-002`); no credential or key passes through it (`SEC-027`) |
| Trace and tests | `MOD-025`–`MOD-028`, `ADM-014`, `ADM-015`, `ADM-027`, `SEC-026`, `F-FP-016`, `FP-P10` · `REQ-847`, `REQ-848`, `REQ-850`, `REQ-858` · `UD-056` **Open** · `12A-INT-29` · `FPA-203`–`FPA-210`, `FPE-053` |

### FPW-032 — Emergency expiry, extension and retrospective review

| Field | Content |
|---|---|
| ID and purpose | `FPW-032` — make the measure end by default, and make its continuation a decision someone else reviews |
| Initiator, permissions, trigger | `SYS` at `t_e`; reviewer = someone other than the author where staffing permits (`MOD-028`) |
| Systems and responsibilities | B-12 owns expiry and review; B-02 supplies boundaries |
| Required input and access | Measure record, expiry boundary, whether a new recorded extension exists, the review outcome |
| Validation and decision sequence | At `t_e` the measure expires unless a **new recorded extension** exists (`F-FP-016` §7, `MOD-026`); extension remains bounded and requires a new review (`F-FP-016` §10); every emergency action is reviewed and the outcome recorded **whether or not the action is reversed** (`MOD-028`) |
| Normal path | `IN_FORCE → EXPIRED`, review recorded |
| Alternative paths | Reviewer unavailable → the case is labelled and disclosed as unsegregated rather than left unreviewed (`ADM-013`, `REQ-849`, `UD-054`/`UD-056` **Open**) |
| Failure behaviour | Review not performed by the due boundary → the measure still expires; the missing review becomes an incident record, never a retroactive justification (`FR-15`) |
| Resulting state, player experience | capabilities return; the disclosure states the review happened |
| Permitted action, audit evidence | Expiry, extension, review record. Writes `EVD-026` emergency actions, administrative override |
| Security and privacy constraints | Expired measures are not deleted from the record (`MOD-034`) |
| Trace and tests | `MOD-026`, `MOD-028`, `MOD-041`, `ADM-013`, `F-FP-016` · `REQ-847`, `REQ-849`, `REQ-850` · `UD-054`, `UD-056` **Open** · `FPA-211`–`FPA-216`, `FPE-054` |

### FPW-033 — Incident classification and posture selection

| Field | Content |
|---|---|
| ID and purpose | `FPW-033` — class an incident first, then apply the posture that class already declares |
| Initiator, permissions, trigger | `SEC`/`OPS`/`INV` or `SYS`; trigger: an integrity, privacy, availability or exploitation event |
| Systems and responsibilities | B-12 owns incident class, posture, disclosure owner and preservation step (`SEC-024`); B-02 owns pipeline halts (`INT-013`); Prompt 13 and B-02 own public communication (`12A-INT-29`) |
| Required input and access | Observed effect, affected classes from `SEC-024` (active exploitation, service compromise, data exposure, integrity failure, privacy breach), affected value paths |
| Validation and decision sequence | Class declared before posture (12A posture 10, expressed by `FR-001`); posture is per category and **no global fail-open or fail-closed answer is permitted** (`SEC-022`, `REQ-862`, `FR-001`); a turn-processing integrity failure is an incident, not a conduct case, unless manipulation is evidenced (`INT-013`, `12A-INT-17`); a first honest exploit report is an incident, not a violation (`FP-027`, `REQ-814`) |
| Normal path | Incident record opened; each affected category runs its Annex D posture; preservation applied via `FPW-010` |
| Alternative paths | Duplicate enforcement actions result from the same incident → coalesce to the first committed and flag the conflict (`MOD-032`, `REQ-820`) |
| Failure behaviour | Unknown class → classify, then act; nothing proceeds on an unclassified incident (`FR-001`); a failure that affects integrity, privacy or enforcement is reviewed and recorded whether or not it changed an outcome (`FR-15`) |
| Resulting state, player experience | incident `OPEN → CONTAINED → REVIEWED → CLOSED`; players receive bounded delay or measure notices only |
| Permitted action, audit evidence | Classification, posture application, halt request. Writes `EVD-026` integrity-verification results, emergency actions |
| Security and privacy constraints | Public communication is bounded and discloses no method (`MOD-018`, `12A-INT-29`); a suspected personal-data breach is assessed whether or not reported onward (`FPW-034`) |
| Trace and tests | `FR-001`–`FR-15`, `SEC-022`–`SEC-026`, `FP-027`, `INT-013` · `REQ-856`, `REQ-858`, `REQ-862`, `REQ-863`, `REQ-814` · `12A-INT-17`, `12A-INT-29` · `FPA-217`–`FPA-226`, `FPE-055`–`FPE-058` |

### FPW-034 — Suspected personal-data breach assessment and preservation

| Field | Content |
|---|---|
| ID and purpose | `FPW-034` — produce the assessment artefact, including the reasons for not reporting onward |
| Initiator, permissions, trigger | `SEC`/`INV`; trigger: `FPW-033` classifies a privacy breach or data exposure |
| Systems and responsibilities | B-12 owns the assessment and preservation step; the owner and counsel own the reporting conclusion (`UD-017`); Stage 6 owns credential facts (`INT-015`) |
| Required input and access | Affected classes from `PRV-002`, affected accounts, exposure vector, timestamps, containment state |
| Validation and decision sequence | Assess and document **whether or not** it is reported onward, including reasons for not reporting; the assessment is an artefact, not a legal conclusion (`SEC-025`, `REQ-857`); preserve, assess, document, then decide disclosure (12A posture 8); inter-player data exposure is withheld at publication, not after (12A posture 9, `PRV-018`) |
| Normal path | Assessment artefact recorded in the case, referenced by the spine event |
| Alternative paths | Reporting depends on unresolved jurisdiction → the conservative branch is taken and the dependency named (`REQ-869`, `12A-INT-26`, `UD-017` **Open**) |
| Failure behaviour | Evidence of exposure unavailable → the assessment records the gap; no claim of no-exposure is made (`FP-008`) |
| Resulting state, player experience | artefact `DOCUMENTED`; affected players receive bounded notices only where an obligation and authority exist |
| Permitted action, audit evidence | Assessment, preservation. Writes `EVD-026` privileged access and integrity results |
| Security and privacy constraints | No legal-compliance claim is made anywhere in this workflow (`SEC-025`, `REQ-869`, `P12B-26`) |
| Trace and tests | `SEC-024`, `SEC-025`, `PRV-016`, `PRV-018`, `GOV-009` · `REQ-856`, `REQ-857`, `REQ-869` · `UD-017`, `UD-055` **Open** · `12A-INT-26` · `FPA-227`–`FPA-232`, `FPE-059` |

---

## 14. Family H — Privacy and information handling

### FPW-035 — Field classification and register reconciliation

| Field | Content |
|---|---|
| ID and purpose | `FPW-035` — give every field exactly one value on each of the three axes, reconciling rather than reassigning |
| Initiator, permissions, trigger | `SMOD`/`SEC` as classification owner; trigger: a new field, or a discovered conflict between registers |
| Systems and responsibilities | B-12 owns the model; the **owning register** keeps its assignment and resolves conflicts with a dated decision (`PRV-003`, `REQ-799`) |
| Required input and access | Field identifier, owning register, current assignments on handling class, subject visibility and record purpose |
| Validation and decision sequence | Exactly one value per axis (`PRV-001`, `REQ-798`); nine access classes and no tenth (`PRV-002`); four handling values, eight visibility values, four purpose classes `S`/`P`/`O`/`SPINE`; a classification change is a recorded, versioned decision and never a deployment side effect, and historical records keep the class under which they were created (`PRV-017`) |
| Normal path | Field classified; inventory row completed by `FPW-040` inputs |
| Alternative paths | Registers disagree → reconcile in the owning register with a dated decision; B-12 does not overwrite (`REQ-799`) |
| Failure behaviour | Ambiguous classification → the field is treated at the **more protective** class until reconciled (conservative branch, `REQ-869`) |
| Resulting state, player experience | classification register updated; no visible change |
| Permitted action, audit evidence | Classification decision. Writes `EVD-026` configuration publication |
| Security and privacy constraints | No personal, moderation, security or audit field may be `PUB` (`PRV-008`) |
| Trace and tests | `PRV-001`–`PRV-003`, `PRV-008`, `REQ-798`, `REQ-799`, `REQ-805` · `12A-IC-01`–`12A-IC-11` · `FPA-233`–`FPA-238`, `FPE-060` |

### FPW-036 — Purpose-bound restricted read with audit event

| Field | Content |
|---|---|
| ID and purpose | `FPW-036` — make every restricted read state its purpose and become an auditable event, even when nothing changes |
| Initiator, permissions, trigger | Any privileged actor; trigger: a read of a `MOD`, `OPS`, `PERSONAL`, `SEC`, `AUDIT` or `LEGAL` record |
| Systems and responsibilities | B-12 owns the purpose taxonomy and readership; B-02's spine records the read (`INT-014`); each owning subsystem remains the source of truth |
| Required input and access | Actor, role, session (`FPW-043`), target record, purpose code, authorising requirement |
| Validation and decision sequence | Purpose stated and authorising requirement named — convenience is not a purpose (`PRV-004`, `REQ-800`); permission evaluated for the specific action, and viewing never implies search, export, modify, delete or disclose (`PRV-006`); cross-class flows declared separately from read permission (`PRV-004`, `REQ-801`); a privileged read of a restricted record is an auditable event with actor, purpose, target and time (`ADM-008`, `EVD-025`, `REQ-841`) |
| Normal path | Read granted, audit row appended, data returned minimised by `FPW-038` |
| Alternative paths | Restricted-history diplomacy read → B-12's own class governs and the read is audited (`INT-007`, `DIP-121`); Alliance tax and contribution read → minimised, role-scoped, never leaked through moderation tooling (`INT-008`, `PRV-010`) |
| Failure behaviour | Audit row cannot be written → **the read does not happen** (`FR-02`, `FR-03`); a failed restricted read returns no data and never falls back to a broader cache or an unfiltered response (`FR-14`/`FR-12` read-search posture) |
| Resulting state, player experience | no player-visible change |
| Permitted action, audit evidence | Read. Writes `EVD-026` privileged access |
| Security and privacy constraints | `SEC` content never appears on any player-facing or moderation surface (`PRV-014`); the spine's readership is itself a security control whose absence is a defect, not a documentation gap (`SEC-021`) |
| Trace and tests | `PRV-004`–`PRV-007`, `PRV-011`–`PRV-015`, `ADM-005`, `ADM-008`, `EVD-025`, `SEC-021` · `REQ-800`, `REQ-801`, `REQ-841`, `REQ-854` · `12A-INT-10`, `12A-INT-12` · `FPA-239`–`FPA-246`, `FPE-061`, `FPE-062` |

### FPW-037 — Response minimisation and failure-text construction

| Field | Content |
|---|---|
| ID and purpose | `FPW-037` — build responses and errors that leak nothing: no hidden state, no method, no existence |
| Initiator, permissions, trigger | `SYS` on every read or rejection; trigger: a response is about to be produced |
| Systems and responsibilities | Every read service owns its response shape (`REQ-774`); Prompt 13 owns presentation (`INT-012`) |
| Required input and access | Requester class set, requested fields, the failing condition |
| Validation and decision sequence | Only fields the requester's class entitles them to receive are present — hidden state is never sent and filtered later, and hiding a field in the client is not access control (`FP-015`, `PRV-007`, `SEC-012`); no surface reveals another player's restriction, investigation, verification, appeal or report state, and no badge, ranking note or chronicle entry carries that fact (`PRV-019`, `REQ-803`); failure text identifies the failed condition without revealing a rule, threshold, another player's data or whether an account exists (`PRV-020`, `REQ-804`) |
| Normal path | Minimised response returned |
| Alternative paths | A legitimately containing field is a **design defect, not a player violation** (`FP-029`); reconstruction from response differences is `V-13` (`EX-007`) |
| Failure behaviour | A partial response is never emitted — withhold the figure instead of publishing an incomplete or inferred one (`FR-08`, `REQ-863`) |
| Resulting state, player experience | consistent, non-revealing messages |
| Permitted action, audit evidence | None (read path). Writes `EVD-026` privileged access where restricted fields were in scope |
| Security and privacy constraints | Differencing re-identification below `k` is a registered threat (`12A-RK-022`) addressed by `FPW-038` |
| Trace and tests | `FP-015`, `FP-029`, `PRV-007`, `PRV-019`, `PRV-020`, `SEC-012`, `EX-007` · `REQ-774`, `REQ-803`, `REQ-804` · `FPA-247`–`FPA-252`, `FPE-063` |

### FPW-038 — Aggregate publication, k≥5 and withholding

| Field | Content |
|---|---|
| ID and purpose | `FPW-038` — publish aggregates that cannot single anyone out, and withhold what cannot be published safely |
| Initiator, permissions, trigger | `SYS` at publication; `SMOD` for an exception request |
| Systems and responsibilities | B-11 owns snapshots and publication (`INT-011`); B-07 owns post-gate market statistics; B-12 supplies the disclosure class and the manipulation-evidence shape |
| Required input and access | Candidate aggregate, quasi-identifier list, denominator `k`, merging and suppression plan, inference argument |
| Validation and decision sequence | Name the quasi-identifiers, satisfy `k ≥ 5`, use stable merging and complementary suppression, and state the inference argument (`PRV-018`, `REQ-802`, `TR-022`, `WEP-044`, `WEP-659`); a figure that can single out a nation is withheld or coarsened (`PRV-018`); a nation's own rank is not an aggregate (`WEP-660`); no new threshold or "small group" exception is invented — that would be a Prompt 12 or owner matter (`WEP-649`) |
| Normal path | Aggregate published with its QI list and inference note |
| Alternative paths | Denominator below five → withhold (`WEE-039` precedent in B-11); integrity failure or unverified pipeline → withhold the figure (`FR-08`) |
| Failure behaviour | Publication pipeline failure → withhold, never publish an inferred figure (`FR-08`, `REQ-863`); a composite headline leak is prohibited by `INT-011` |
| Resulting state, player experience | published or withheld aggregate, with no enforcement status carried in any ranking surface (`PRV-019`) |
| Permitted action, audit evidence | Publication decision. Writes `EVD-026` configuration publication and integrity results |
| Security and privacy constraints | A keyed digest is pseudonymous, not anonymous, and carries a written identifiability assessment (`PRV-024`, `REQ-806`) |
| Trace and tests | `PRV-018`, `PRV-024`, `INT-011`, `WEP-044`, `WEP-649`, `WEP-659`, `WEP-660`, `TR-022` · `REQ-802`, `REQ-803`, `REQ-806`, `REQ-868` · `UD-050` **Open** · `FPA-253`–`FPA-260`, `FPE-064`, `FPE-065` |

---

## 15. Family I — Disclosure, export, retention and legal hold

### FPW-039 — Notice content bounding and disclosure decision

| Field | Content |
|---|---|
| ID and purpose | `FPW-039` — decide what a notice may contain, per class, before anything is displayed |
| Initiator, permissions, trigger | `MOD`/`SMOD`/`SYS`; trigger: any notification produced by `FPW-014`, `FPW-021`, `FPW-031`, `FPW-040` or a restore |
| Systems and responsibilities | B-12 bounds content; B-02 owns notice classes; Prompt 13 owns surfaces (`INT-012`, `12A-INT-16`, `12A-INT-24`) |
| Required input and access | Intended audience class, subject, rule element, tier or correction, appeal route |
| Validation and decision sequence | Publish rules, never methods (`FP-033`, `MOD-018`); the reporter's identity and status are never exposed to the reported party (`INT-017`); third-party data never appears (`MOD-054`); every restriction surface must publish its appeal route and must not reveal another account's restriction state (`REQ-803`, `12A-INT-24`) |
| Normal path | Notice emitted within its class bounds; delivery failure routes to `FR-07` |
| Alternative paths | Delayed notice for an active investigation → delay and review recorded (`MOD-030`) |
| Failure behaviour | Content cannot be bounded → withhold the content, not the record of the action (`FR-08` analogy for publication paths; the enforcement record is still committed) |
| Resulting state, player experience | comprehensible, contestable notice |
| Permitted action, audit evidence | Notice. Writes `EVD-026` moderation action |
| Security and privacy constraints | Notification information is never assumed public (`PRV-009`, `PRV-012`) |
| Trace and tests | `FP-033`, `MOD-017`, `MOD-018`, `MOD-030`, `MOD-054`, `PRV-019`, `INT-012` · `REQ-803`, `REQ-804`, `REQ-821`, `REQ-835`, `REQ-850` · `FPA-261`–`FPA-266`, `FPE-066` |

### FPW-040 — Export, delete and disclose as separate permissions

| Field | Content |
|---|---|
| ID and purpose | `FPW-040` — keep the six actions separate, so a view right never becomes an export or deletion right |
| Initiator, permissions, trigger | Actor holding the **specific** named permission (`PRV-006`, `ADM-002`); trigger: an export, deletion or disclosure request |
| Systems and responsibilities | B-12 owns case records; the subject and the legal role own personal-data routes; counsel's authority is `UD-017` |
| Required input and access | Requested artefact set, purpose, authorising permission, destination |
| Validation and decision sequence | Export requires a separate permission, a stated purpose and a recorded event, and a moderator who may view a case may not export it by default (`PRV-021`, `REQ-831`); deletion is a separate permission and a recorded event, and no actor holds export, delete or disclose by default except the audit role for `AUDIT` export (`PRV-022`, Annex B); a data-subject request is served to the subject only (`PRV-013`) |
| Normal path | Export file produced or refusal recorded, each with its event |
| Alternative paths | Legal obligation compels disclosure → recorded authority, minimised content (`PRV-013`, `PRV-016`) |
| Failure behaviour | A failed export produces **no partial file and no unredacted fallback** (`FR-15`/`FR-13` export posture) |
| Resulting state, player experience | artefact delivered or withheld |
| Permitted action, audit evidence | Export, delete, disclose. Writes `EVD-026` investigation and evidence reads/writes, permission changes |
| Security and privacy constraints | An unsegregated reviewer may not export the case they sit on (`ADM-022`, `PRV-021`) |
| Trace and tests | `PRV-006`, `PRV-013`, `PRV-015`, `PRV-021`, `PRV-022`, `ADM-002`, `EVD-024`, `EVD-026` · `REQ-780`, `REQ-805`, `REQ-828`, `REQ-831` · `UD-017`, `UD-055` **Open** · `FPA-267`–`FPA-272`, `FPE-067` |

### FPW-041 — Retention application, redaction, deletion event and legal hold

| Field | Content |
|---|---|
| ID and purpose | `FPW-041` — apply existing retention by class, redact under obligation, and suspend deletion under hold — without inventing a day |
| Initiator, permissions, trigger | `SYS` at the retention boundary; `SMOD`/legal role for redaction; trigger: retention expiry, an obligation, or a hold |
| Systems and responsibilities | B-02 owns history classes and the spine (`TR-090`, `TR-092`); B-03 owns the personal-data inventory (`DAT-001`…`DAT-012`); B-12 owns case-scoped evidence retention and redaction; the owner and counsel own the periods |
| Required input and access | Record class (`S`/`P`/`O`/`SPINE`), case need, existing class periods, obligation or hold authority |
| Validation and decision sequence | Retention is per class with a stated justification and review trigger, and B-12 **adopts no new day-count** — `D-026`, `D-042`, `UD-017`, `UD-055` govern (`PRV-023`, `REQ-808`); evidence is retained only for case need and minimised (`REQ-831`); class-O operational evidence already carries the existing 12-month floor unless an open case requires longer (`TR-090`), and market manipulation evidence is already class O with the same 12-month figure (`MKT-162`) — this document **consumes those values by reference and adds none**; spine rows are permanent and never sampled away (`EVD-034`, `REQ-853`); redaction removes protected content but preserves the fact, authority and remaining reference (`EVD-038`, `PRV-022`); a legal hold suspends routine deletion for named records, and its authority and scope remain `UD-017`/`UD-055` (`EVD-039`) |
| Normal path | Class-appropriate action taken; deletion under obligation recorded as a deletion event with its authority (`EVD-029`, `REQ-855`) |
| Alternative paths | Erasure obligation conflicts with the permanent spine → both obligations recorded and the **conservative branch** taken; the conflict itself is registered, not resolved here (`REQ-809`, `12A-DR-017`, `UD-055` **Open**) |
| Failure behaviour | Period unresolved → the existing class value continues to govern; no new period is invented and no claim of legal sufficiency is made (`REQ-869`) |
| Resulting state, player experience | records retained, redacted or deleted-with-event |
| Permitted action, audit evidence | Retention, redaction, deletion, hold. Writes `EVD-026` permission changes and evidence events |
| Security and privacy constraints | Deletion of a spine row outside the recorded correction path is prohibited (`SEC-037`); a missing protective trigger makes this a **specified obligation with an open defect**, not a satisfied control (`SEC-036`, `P12B-14`, `P12B-16`) |
| Trace and tests | `PRV-016`, `PRV-022`, `PRV-023`, `EVD-029`, `EVD-034`, `EVD-038`, `EVD-039`, `TR-090`, `TR-092`, `MKT-162`, `FP-P11`, `SEC-036`, `SEC-037` · `REQ-808`, `REQ-809`, `REQ-830`, `REQ-831`, `REQ-853`, `REQ-855` · `UD-017`, `UD-055` **Open** · `FPA-273`–`FPA-282`, `FPE-068`–`FPE-071` |

---

## 16. Family J — Administration and separation

### FPW-042 — Capability grant, delegation and revocation

| Field | Content |
|---|---|
| ID and purpose | `FPW-042` — grant named capabilities individually, delegate narrowly, and revoke immediately |
| Initiator, permissions, trigger | Actor holding the specific grant permission; **no superuser exists** (`ADM-002`, `REQ-839`); trigger: a role change, case need or expiry |
| Systems and responsibilities | B-12 owns the permission register (`ADM-018`); Stage 6 owns the session that carries it (`INT-015`); the owner owns staffing (`UD-054`) |
| Required input and access | Capability name, actor, purpose, scope, expiry, delegator |
| Validation and decision sequence | Every capability is named and individually granted and the register is authoritative — a capability not in the register does not exist (`ADM-002`, `ADM-018`, `REQ-839`); a role cannot grant a permission it does not hold (`ADM-006`, `MOD-020`); delegation is permitted only for a named case, purpose and expiry, within the delegator's own permissions, recorded and revocable (`ADM-028`); revocation is immediate and recorded on role end, function change, declared conflict or compromised session (`ADM-016`); read access is narrower than write access and never implies export (`ADM-005`); the prohibition list is enforced on every grant (`ADM-001`) |
| Normal path | Grant, delegation or revocation recorded with purpose and expiry |
| Alternative paths | Emergency privilege → `FPW-031` scope, which still excludes the prohibition list (`ADM-014`) |
| Failure behaviour | A grant request for a prohibited capability → denied and recorded (`FR-02`); self-grant by `R-SEC` is prohibited (`ADM-024`) |
| Resulting state, player experience | role mapping changed; no player-visible change |
| Permitted action, audit evidence | Grant, delegate, revoke. Writes `EVD-026` permission changes |
| Security and privacy constraints | A privileged action outside its named purpose is `V-16` even if otherwise permitted (`ADM-019`); no administrative action may be hidden from the spine (`ADM-020`) |
| Trace and tests | `ADM-001`, `ADM-002`, `ADM-005`, `ADM-006`, `ADM-014`, `ADM-016`, `ADM-018`, `ADM-019`, `ADM-020`, `ADM-024`, `ADM-028`, `MOD-020` · `REQ-838`, `REQ-839`, `REQ-840` · `12A-INT-18` · `FPA-283`–`FPA-290`, `FPE-072` |

### FPW-043 — Step-up session, self-dealing control and separation substitutes

| Field | Content |
|---|---|
| ID and purpose | `FPW-043` — require a distinct privileged session, block or expose self-dealing, and declare the gap where separation is impossible |
| Initiator, permissions, trigger | Stage 6 issues the session; `SYS` evaluates each privileged action; trigger: a privileged action is attempted |
| Systems and responsibilities | Stage 6 owns authentication (`INT-015`); B-12 owns the authorization, purpose and disclosure rules; B-03 owns account state |
| Required input and access | Step-up session identifier, actor's own account/nation/Alliance membership, declared interests, second-approver availability |
| Validation and decision sequence | Privileged action requires an authenticated step-up distinct from ordinary play credentials, in a shorter, separately logged, independently revocable session (`ADM-007`, `REQ-840`); authentication establishes the session and authorization evaluates action, object, role and purpose separately — a valid session is not a permission (`SEC-016`); no administrator exercises a capability against their own account, nation, Alliance or declared interest without second approval where one exists, and where none exists the action is recorded, disclosed on request and retrospectively reviewed (`ADM-009`, `REQ-042`-consistent `REQ-842`); investigate-and-decide are distinct permissions, and one person holding both requires the unsegregated label (`ADM-010`, `REQ-843`); configuration author and publisher are separated, or the substitute disclosure and review are recorded (`ADM-011`, `REQ-844`); where separation is impossible the gap is recorded **with its compensating control and never described as separation of duties** (`ADM-013`, `REQ-846`) |
| Normal path | Action proceeds inside a step-up session with its purpose recorded |
| Alternative paths | Shared operator credential → prohibited; authentication failure denies and never falls back to lower assurance (`FR-12`, `ADM-025`, `12A-RK-025`) |
| Failure behaviour | Step-up unavailable → the action is denied (`FR-02`); a compromised privileged session → halt privileged paths, preserve evidence, keep the world running (12A posture 5, `ADM-016`), and `R-SEC` containment runs within recorded policy (`ADM-024`) |
| Resulting state, player experience | none directly; a self-dealing action may be disclosed on request |
| Permitted action, audit evidence | Session establishment, denial, disclosure, review. Writes `EVD-026` privileged access, administrative override |
| Security and privacy constraints | B-12 never holds, logs, exports or displays a credential, token, key or secret (`SEC-027`, `REQ-807` custodial boundary) |
| Trace and tests | `ADM-007`, `ADM-009`–`ADM-011`, `ADM-013`, `ADM-024`, `ADM-025`, `SEC-016`, `SEC-027` · `REQ-769`, `REQ-840`, `REQ-842`, `REQ-843`, `REQ-844`, `REQ-846` · `UD-054` **Open** · `FPA-291`–`FPA-300`, `FPE-073`–`FPE-075` |

---

## 17. Family K — Audit spine and integrity

### FPW-044 — Audit event emission and record shape

| Field | Content |
|---|---|
| ID and purpose | `FPW-044` — emit the one named event set, in the one shape, with the protected contents |
| Initiator, permissions, trigger | `SYS` at every consequential act; trigger: any of the ten named event classes |
| Systems and responsibilities | B-12 owns the event shape (`EVD-027`) and the readership; **B-02's `TR-090` owns the spine** (`INT-014`) |
| Required input and access | Event type, actor, purpose, target, timestamp, turn or boundary, decision, reason code, evidence reference, outcome |
| Validation and decision sequence | The nine covered domains — privileged access, permission changes, investigation and evidence reads/writes, moderation and disciplinary actions, appeal outcomes, administrative overrides, emergency actions, financial corrections, configuration publication — plus integrity-verification results are all emitted (`EVD-026`, `REQ-851`); rows contain identifiers, decisions and reasons and **never** free-form player content, message bodies, secrets or raw credentials (`EVD-028`, `REQ-852`); no effect is committed without its record (`FR-02`/`FR-03`, `FR-002`) |
| Normal path | One spine row per consequential act, keyed to the case where applicable (`COR-016`) |
| Alternative paths | Quota pressure → spine rows are never sampled away; value-mutation, pipeline, privileged-act and enforcement rows are retained first (`EVD-034`, `REQ-853`) |
| Failure behaviour | Audit write failure → **the transaction fails closed**; nothing is committed that cannot be recorded (`FR-01`, `FR-03`, `SEC-009`). An audit-write failure during `FPW-031` means the emergency action does not execute at all (`FR-11`) |
| Resulting state, player experience | invisible to players by design (`PRV-015`) |
| Permitted action, audit evidence | Emission. The event **is** the evidence |
| Security and privacy constraints | The absence of spine readership control, digest chain, verification job or retention is a **defect, not a documentation gap** (`SEC-021`) |
| Trace and tests | `EVD-026`–`EVD-028`, `EVD-034`, `SEC-009`, `FR-01`–`FR-03`, `TR-090` · `REQ-851`–`REQ-853` · `INT-014`, `12A-INT-18` · `FPA-301`–`FPA-308`, `FPE-076`, `FPE-077` |

### FPW-045 — Digest chain construction and scheduled verification

| Field | Content |
|---|---|
| ID and purpose | `FPW-045` — specify how tamper-evidence would be built and proved, and state plainly that it is not built |
| Initiator, permissions, trigger | `SYS` on each spine append; `AUD` runs verification; trigger: a record is added, or an interval elapses |
| Systems and responsibilities | B-02's spine owns storage; B-12 owns the integrity requirement (`INT-014`, `EVD-030`); Stage 5 owns the implementation |
| Required input and access | Canonical record bytes `r_i`, previous digest `h_{i−1}`, last verified checkpoint, interval `I_v` |
| Validation and decision sequence | `h_i = SHA-256(h_{i−1} ‖ canonical(r_i))` with a published genesis `h_0`; the digest covers every protected field; a missing field invalidates the chain; no secret is stored in the row (`EVD-031`, `F-FP-012`); verification checks from the last verified checkpoint, records the result and escalates a break (`EVD-032`); a correction appends a new record and never recomputes an old digest (`F-FP-012` §10); missing record → `CHAIN_BREAK`, never a skipped link |
| Normal path | Chain extended; verification run recorded with its checkpoint |
| Alternative paths | Interval unresolved (`FP-P08`) → the run is specified and scheduled, but **no interval may be claimed as operating** (`F-FP-013` §9) |
| Failure behaviour | A break halts the next publication until reviewed (`F-FP-013` §10) and opens an integrity-failure incident (`FPW-033`, `SEC-026`); a missed interval raises an incident at the next boundary (`F-FP-013` §7) |
| Resulting state, player experience | none, until a break forces a delay disclosure (`REQ-858`) |
| Permitted action, audit evidence | Chain append, verification record. Writes `EVD-026` integrity-verification results |
| Security and privacy constraints | **Current state: no chained digest, no verification job and no protective `audit` trigger exist; append-only is convention, not enforcement; no document may claim the trail is tamper-proof, immutable in production, monitored or verified** (`EVD-041`, `EVD-042`, `SEC-036`, `SEC-038`, `SEC-039`, `SEC-040`, `P12B-14`) |
| Trace and tests | `EVD-030`–`EVD-034`, `EVD-041`, `EVD-042`, `SEC-021`, `SEC-036`–`SEC-040`, `F-FP-012`, `F-FP-013`, `FP-P08` · `REQ-829`, `REQ-853`, `REQ-855`, `REQ-858` · `12A-INT-18`, `12A-DR-018`, `12A-DR-031` · `FPA-309`–`FPA-318` (**all BLOCKED pending an executed run**), `FPE-078`–`FPE-080` |

### FPW-046 — Readership, read logging, no-sampling and appended correction

| Field | Content |
|---|---|
| ID and purpose | `FPW-046` — control who reads the spine, log every read, and correct only by append |
| Initiator, permissions, trigger | `AUD` or a purpose-bound reviewer; trigger: a spine read, an integrity question, or a wrong record |
| Systems and responsibilities | B-02 owns storage; B-12 owns readership register and integrity requirement (`EVD-033`, `INT-014`) |
| Required input and access | Reader identity and role, purpose, target rows, the original event to be corrected |
| Validation and decision sequence | Readership is a published internal register granted by purpose, every read is logged, and the audit role may verify but not rewrite (`EVD-033`, `PRV-015`, `REQ-854`); an audit record is corrected only by an appended correcting event referencing the original, and deletion under external obligation is recorded as a deletion event with its authority (`EVD-029`, `REQ-855`); production must prevent update and delete of spine rows outside the recorded correction path and protect the spine from the service role's ordinary path where the platform allows (`SEC-037`) |
| Normal path | Read logged; correction appended; original preserved |
| Alternative paths | Audit correction of another system's record → route through that system's correction path (`INT-003`…`INT-011`, `REQ-819`) |
| Failure behaviour | Read without a logged purpose → denied (`FR-02`); the platform's inability to protect the spine from `service_role` is an **open defect to be verified, not a control to be claimed** (`12A-OPEN-015`) |
| Resulting state, player experience | none |
| Permitted action, audit evidence | Read, appended correction, deletion-with-event. Writes `EVD-026` privileged access, integrity results |
| Security and privacy constraints | Readable by all is not evidence and readable by none is not accountability — the register is purpose-bound (`REQ-854`) |
| Trace and tests | `EVD-029`, `EVD-033`, `EVD-034`, `PRV-015`, `SEC-037` · `REQ-854`, `REQ-855` · `UD-055` **Open** · `FPA-319`–`FPA-324`, `FPE-081` |

---

## 18. Family L — Cross-system handoffs

### FPW-047 — Market signal receipt and the G-1 tolerance-band input

| Field | Content |
|---|---|
| ID and purpose | `FPW-047` — receive `MKT-S` signals as review input and supply the structural incident-rate band the Global Trade gate G-1 requires |
| Initiator, permissions, trigger | `SYS` on a signal; `MOD` on receipt; trigger: `MKT-S01`…`MKT-S10` recorded (`MKT-157`) |
| Systems and responsibilities | **B-07 owns market rules, listings, executions, prices and its own signals** (`INT-006`, `MKT-160`); B-04 owns settlement value and conservation (`MKT-217`–`MKT-219`, executed at P4 by B-02); B-12 owns the finding, the case and the account measures; B-12 never resolves a trade, order or price |
| Required input and access | Signal ID, trade or listing ID, parties, turn, measured values (`MKT-157`); the market's declared limits (`MKT-124`, `DD-127`); `SUSPENDED` listing state (`MKT-089`) |
| Validation and decision sequence | A signal **opens a review item** and is never a sanction (`MKT-158`, `MKT-160`, `REQ-859`-consistent); a legitimate unusual trade is not cheating and price alone never proves manipulation (`MKT-155`, `FP-018`); wash and circular patterns are `V-09` where they create an effect the market rules could not produce (`CO-005`, `V-09`); the conservation-pair signal `MKT-S10` is a **defect, not a player act** and pages the operator via `FPW-033`, never a conduct case (`COR-`/`EX-002` distinction); a market ban is achieved only through the account measures B-12 owns (`MKT-218`); no public per-trade feed is used as evidence (`PRV-009`, `INT-006`) |
| Normal path | Review object created at `E1`; `FPW-007` assigns state; `FPW-011` or `FPW-021` proceeds |
| Alternative paths | Repeated matched same-price/same-quantity trading (`MKT-S04`) or a cancelled-and-reposted listing (`MKT-S05`) → indicator, corroborated by a non-behavioural record before any finding (`EVD-004`, `CO-003`); a fresh-nation one-sided receive (`MKT-S03`) → the fresh-nation protection rule remains B-07's (`W-D14`) |
| Failure behaviour | G-1 remains **not met** because no live incident rate exists: this document defines the band **structurally** and the numeric band belongs to Prompt 14 plus an operational measurement (`INT-006`, `MKT-073`, `MKT-074`, `12A-INT-25`, `REQ-789`); a document, test or date is not gate evidence (`MKT-074`) |
| Resulting state, player experience | review item; the market stays dark until its gates pass (`MKT-076`), which is B-07's rule and is unchanged |
| Permitted action, audit evidence | Review object, correction instruction, account measure request. Writes `EVD-026` investigation and evidence writes |
| Security and privacy constraints | Directed terms remain parties-only; completed global trades are not a public per-trade feed (`DD-129`, `PRV-009`) |
| Trace and tests | `MKT-073`, `MKT-074`, `MKT-076`, `MKT-089`, `MKT-124`, `MKT-155`, `MKT-157`–`MKT-162`, `MKT-217`–`MKT-219`, `CO-003`, `CO-005`, `V-09`, `INT-006` · `REQ-786`, `REQ-791`, `REQ-789`, `REQ-803`, `REQ-859` · `12A-INT-09`, `12A-INT-25` · `FPA-325`–`FPA-334`, `FPE-082`–`FPE-085` |

### FPW-048 — Diplomacy restricted-history read and breach-record evidence

| Field | Content |
|---|---|
| ID and purpose | `FPW-048` — read diplomatic history under B-12's own restricted class, audited, without touching treaty state |
| Initiator, permissions, trigger | `INV`/`MOD`; trigger: a coercion, harassment or false-agency allegation involving agreements or statements |
| Systems and responsibilities | **B-08 owns treaty records, breach counts and diplomatic state** (`INT-007`); B-12 owns the case, the read class and the finding |
| Required input and access | Treaty or agreement event records (`DIP-119`), the derived breach count (`DIP-085`), party-published statements (`DIP-078`) |
| Validation and decision sequence | Only an administrator or reviewer under Prompt 12's restricted class may read the full history, and **every privileged read is itself audited** (`DIP-121`, `FPW-036`, `REQ-841`); the breach count is a count of events, not a judgement, not a score and not an input to any other system (`DIP-085`) — B-12 may cite it as evidence but never converts it into a reputation or a sanction; B-08 never reads B-12's enforcement records as a reputation (`DIP-089`); a disputed breach is corrected by a **new event referencing the original**, never an edit (`DIP-119`, `TR-091`, and the `DPE-049` deferral this workflow answers); coercive diplomatic conduct is assessed against `V-15`/`V-03` elements, not against the existence of an embargo (`DIP-037`, `DIP-091`, `FP-018`) |
| Normal path | Audited read; finding or `EX`; any correction routed through B-08's append path |
| Alternative paths | A party wants its own reason published → that is B-08's `DIP-078` right, not a B-12 disclosure (`PRV-019`) |
| Failure behaviour | `DPE-054`'s combined disclosure-plus-privileged-read row stays **PARTIAL** until the read audit exists as an implemented control; 12C supplies the specification and does not close the row (`P11C`/`08C` coverage unchanged by this document) |
| Resulting state, player experience | none directly |
| Permitted action, audit evidence | Restricted read, evidence citation, correction request. Writes `EVD-026` privileged access |
| Security and privacy constraints | Diplomatic-confidential material stays inside its class; no cross-agreement inference (`DIP-111`) |
| Trace and tests | `DIP-037`, `DIP-078`, `DIP-085`, `DIP-086`, `DIP-089`, `DIP-111`, `DIP-119`, `DIP-121`, `TR-091`, `INT-007` · `REQ-781`, `REQ-800`, `REQ-841`, `REQ-860` · `12A-INT-10` · `FPA-335`–`FPA-340`, `FPE-086` |

### FPW-049 — Alliance evidence, finance screening and enforcement boundary

| Field | Content |
|---|---|
| ID and purpose | `FPW-049` — take Alliance-sourced evidence and route finance-evasion cases without giving the Alliance any adjudication role |
| Initiator, permissions, trigger | `MOD`/`INV`; trigger: a contribution, tax, container-transfer or leadership-abuse pattern, or an Alliance-submitted report |
| Systems and responsibilities | **B-09 owns Alliance rules, membership, roles, tax and contribution data** (`INT-008`, `AX-23` security boundary: alliances cannot self-adjudicate TOS violations); B-04 owns every ledger effect (`ALL-191`, `ECN-212`/`ECN-213`); B-12 owns platform enforcement readership and the finding |
| Required input and access | Container transfer records (`ALL-159`), ARL categories `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` (`ALL-187`), tax and donation records (`ALL-179`–`ALL-195`), purpose-registry operational funding (`ALL-220`–`ALL-226`, `AOP-01`–`AOP-04`), Alliance audit rows (`AUD-AL-013`–`AUD-AL-017`) |
| Validation and decision sequence | An officer has **no** power to suspend a player account; Alliance content is subject to the global moderation rules and reports follow the platform evidence-and-appeal path (`ALL-158`); an Alliance container is never a channel for evading a national restriction, and every in/out transfer passes the same Economy and Diplomacy checks (`ALL-159`); routing a restricted flow through the container or tax to lose pairwise attribution is `V-11` (`CO-008`); Alliance-scale behavioural similarity is a documented false-positive class, not evidence (`REQ-788`, `CO-002`); aggregate Alliance data is read only at `k ≥ 5` and honour-only where B-11 publishes it (`DD-160`, `PRV-010`); a leadership dispute that is really an expulsion or member-rights question is **referred, not decided** (`INT-018`, `UD-044` **Open**) |
| Normal path | Case opened on the evidenced accounts only; value corrections routed through B-04/B-09's own paths |
| Alternative paths | Alliance-internal discipline → referred with `UD-044` named; platform enforcement → continues here. No collective punishment (`CO-010`) |
| Failure behaviour | Alliance treasury authority unresolved (`UD-046`) → B-12 requests no financial effect through the container and records the dependency; tax/contribution confidentiality → read only through `FPW-036` with purpose, and never leaked through moderation tooling (roadmap B-09 dependency for Prompt 12) |
| Resulting state, player experience | account-level enforcement; Alliance state untouched |
| Permitted action, audit evidence | Restricted read, evidence receipt, referral, correction request. Writes `EVD-026` privileged access, moderation action |
| Security and privacy constraints | Moderation tooling scoped by B-09 permissions with every read audited (`12A-INT-12`); a member does not acquire another member's private data by joining (`PRV-010`) |
| Trace and tests | `ALL-154`, `ALL-156`–`ALL-159`, `ALL-187`, `ALL-191`–`ALL-195`, `ALL-220`–`ALL-226`, `AUD-AL-013`–`AUD-AL-017`, `CO-008`, `V-11`, `AX-23`, `INT-008`, `ECN-212`, `ECN-213` · `REQ-784`, `REQ-788`, `REQ-800`, `REQ-802`, `REQ-815`, `REQ-861` · `12A-INT-11`, `12A-INT-12` · `UD-044`, `UD-046` **Open** · `FPA-341`–`FPA-350`, `FPE-087`–`FPE-090` |

### FPW-050 — Warfare and objective participation evidence receipt

| Field | Content |
|---|---|
| ID and purpose | `FPW-050` — receive B-10 and B-11 evidence for `V-10` cases without recomputing any battle, campaign or reward |
| Initiator, permissions, trigger | `MOD`/`INV`; trigger: a block record, participation anomaly, manufactured completion or objective reward dispute |
| Systems and responsibilities | **B-10 owns warfare rules, blocks, results and audit rows and supplies the taxonomy and evidence fields; B-12 owns enforcement and penalty policy** (`WAR-155`, `INT-009`); **B-11 owns event, objective and completion state, flags and records, and defers** (`INT-010`, `WEP-655`, `WEP-704`, `WPC-13`/`WEP-632`); B-12 never grants, removes or rerolls a reward |
| Required input and access | `WRA-02` block records, `WRA-04` battle results, `WRA-06` objective progress, `AUD-AL-017` restricted rows (`WAR-153`, `WAR-154`); B-11 evidence ID, inputs, fingerprint and population (`WEP-412`); `WPF-32` evidence-hold code (`19_` §10) |
| Validation and decision sequence | Feeding, slot filling, forged acceptance and manufactured participation are `V-10` **where the warfare or objective rules could not produce the recorded effect** (`CO-007`, `V-10`); B-10 records these as **review signals**, never as sanctions (`WAR-028`, `WRK-06`, `WRK-07`); a defence-band or sandbagging pattern is an indicator requiring a non-behavioural corroboration (`EVD-004`, `WTS-018` precedent); a grant without evidence is invalid, and an evidence hold is applied as `SUSPENDED`/`EXCLUDED` **by B-12's request through B-11's own state machine**, never as a B-11 punishment (`WEP-655`, `WEP-371`); in-place edit of a committed record is rejected — only a recorded reversal is permitted (`WFA-003` precedent, `TR-091`) |
| Normal path | Review object at `E1`; finding at `E3` → sanction through `FPW-013`/`FPW-016`; invalid effect → correction instruction to B-11/B-04 |
| Alternative paths | B-11 asks for a hold on a disputed snapshot → `WPC-13` evidence path with `WPF-32` |
| Failure behaviour | B-10's five unallocated failure codes `WRF-15`–`WRF-19` remain **unusable** by any workflow or test (`D-143` disclosure); B-11's missing "actor not authorised" code remains a registered gap with the `WPF-13` + `WPA-50` reuse disposition, which 12C does not renumber |
| Resulting state, player experience | a reward may be held or invalidated as a status change with its evidence ID; the player sees the affected action, not the warfare internals |
| Permitted action, audit evidence | Evidence receipt, hold request, correction instruction. Writes `EVD-026` investigation and evidence writes, financial corrections |
| Security and privacy constraints | `AUD-AL-017` remains restricted with a redacted actor view; no role exercises B-10's rows as a gameplay lever (`WAR-151`) |
| Trace and tests | `WAR-005`, `WAR-007`, `WAR-028`, `WAR-151`–`WAR-155`, `WRA-02`, `WRA-04`, `WRA-06`, `WRF-15`–`WRF-19`, `WEP-371`, `WEP-412`, `WEP-632`, `WEP-655`, `WEP-704`, `WPF-32`, `CO-007`, `V-10`, `INT-009`, `INT-010` · `REQ-786`, `REQ-860`, `REQ-861`, `REQ-865` · `12A-INT-13`, `12A-INT-14` · `FPA-351`–`FPA-360`, `FPE-091`–`FPE-094` |

### FPW-051 — Ranking, snapshot and progression correction integrity with turn-engine incident routing

| Field | Content |
|---|---|
| ID and purpose | `FPW-051` — correct standing and progression outcomes without silently rewriting history, and route engine faults to the right lane |
| Initiator, permissions, trigger | `MOD`/`INV`/`OPS`; trigger: a disputed result, a post-publication correction, or an integrity failure inside a shared turn |
| Systems and responsibilities | **B-11 owns snapshots, honours, chronicle and publication** (`INT-011`); **B-02 owns phases, the turn ledger and the audit spine** (`INT-013`, `INT-014`); B-12 owns the disclosure class, the enforcement and the correction instruction |
| Required input and access | Sealed snapshot with its fingerprint, denominator, rank order and tie group (`WEP-646`), `corrects_snapshot_id` (`WEP-383`), the P6 `W1`…`W5` boundary, the affected turn identifier |
| Validation and decision sequence | A sealed snapshot is immutable and a correction is a **new snapshot** with `corrects_snapshot_id`, moving `SEALED → PUBLISHED` and marking the original `corrected_by`; a record may become `CORRECTED` or `REDACTED` but **deletion is invalid** (`WEP-383`, `WEP-389`, `WEP-580`, `WEP-583`); a formula change never rewrites a sealed snapshot (`WEP-593`); no player sees a mid-turn rank (`WEP-384`); a correction never reorders a closed turn (`COR-007`); an integrity failure is an **incident**, not a conduct case, unless manipulation is evidenced (`INT-013`, `REQ-856`); where integrity is doubtful, halt resolution rather than continue doubtfully and disclose the delay (`SEC-026`, `REQ-858`) |
| Normal path | New corrected snapshot published at the next boundary with its linkage; incident opened if engine-caused |
| Alternative paths | Artificial pre-snapshot inflation (`WTS-007`, `12A-RK-015`) → `V-04`/`V-09`/`V-10` evidence path, with the snapshot itself corrected through B-11 only |
| Failure behaviour | Historical standings may not be silently rewritten (`P12C` consistency rule 12, `WEP-383`); a replayed or duplicate publication coalesces (`SEC-008`) and the duplicate key `(turn_id, standing_id)` rejects (`WEP-390`) |
| Resulting state, player experience | standings corrected forward; honour-only aggregate visibility preserved (`DD-160`) |
| Permitted action, audit evidence | Correction instruction, incident creation, disclosure class. Writes `EVD-026` financial corrections, integrity results |
| Security and privacy constraints | Enforcement status never appears in a ranking, badge or chronicle entry (`PRV-019`); `k ≥ 5` is kept while correcting (`INT-011`) |
| Trace and tests | `WEP-383`, `WEP-384`, `WEP-389`–`WEP-390`, `WEP-580`, `WEP-583`, `WEP-593`, `WEP-646`, `TR-044`–`TR-046`, `TR-048`, `INT-011`, `INT-013`, `INT-014`, `V-04` · `REQ-803`, `REQ-819`, `REQ-856`, `REQ-858`, `REQ-862` · `12A-INT-15`, `12A-INT-17` · `UD-050` **Open** · `FPA-361`–`FPA-370`, `FPE-095`–`FPE-098` |

---

## 19. Family M — Governance review

### FPW-052 — Enforcement practice review, capacity declaration and transparency structure

| Field | Content |
|---|---|
| ID and purpose | `FPW-052` — close the loop on what the design can actually operate, and prepare the transparency structure without publishing |
| Initiator, permissions, trigger | `SMOD`/`AUD`/owner-facing review; trigger: a stated review period arriving, an incident, or a capacity observation |
| Systems and responsibilities | B-12 owns the review record and the structure; the owner owns publication, staffing and ladder scale (`GOV-008`, `UD-053`, `UD-054`, `UD-058`) |
| Required input and access | Case volumes and cycle times as observations, appeal outcomes, observed false-positive indications, the stated capacity assumption |
| Validation and decision sequence | Enforcement practice is reviewed periodically against a stated capacity assumption and observed false-positive rate, and **the outcome is recorded even when nothing changes** (`MOD-035`, `REQ-867`); the design does not assume a capacity it has not measured, and where staffing cannot meet a review guarantee the gap is declared with its compensating control (`MOD-029`, `ADM-013`); the role-to-permission map is reviewed periodically and after every incident (`ADM-017`); the public transparency **structure** is defined while publication remains an owner decision (`REQ-868`); no overturn rate is presented as measured (`P12B-10` limitation, `12A-RS-152` absence finding) |
| Normal path | Review record appended; gaps and compensating controls restated; the owner's publication decision is requested, not assumed |
| Alternative paths | A mechanism defect rather than misconduct → routed to Prompt 14 as balance work, "balance before blame", not converted into a manipulation charge (`INT-019`, `12A-INT-23`, `REQ-789`) |
| Failure behaviour | No review capacity → the gap is declared; a missed review is recorded as a gap, never back-dated (`FR-15`) |
| Resulting state, player experience | unchanged play; a possible future published transparency report |
| Permitted action, audit evidence | Review record, gap declaration, configuration change request. Writes `EVD-026` configuration publication, permission changes |
| Security and privacy constraints | Nothing published identifies a case, a reporter or a player (`REQ-868`, `PRV-019`) |
| Trace and tests | `MOD-029`, `MOD-035`, `ADM-013`, `ADM-017`, `GOV-008`, `INT-019` · `REQ-789`, `REQ-867`, `REQ-868` · `UD-053`, `UD-054`, `UD-058` **Open** · `FPA-371`–`FPA-378`, `FPE-099`, `FPE-100` |

---

## 20. Journey-to-workflow map

| Journey | Workflows in order | Branch points |
|---|---|---|
| `FPJ-001` | `FPW-001` → `FPW-002` → `FPW-005` → `FPW-007` → `FPW-011` → `FPW-015` | `FPW-003` privileged subject; `FPW-033` incident lane |
| `FPJ-002` | `FPW-013` → `FPW-014` → `FPW-016` → `FPW-017` → `FPW-027` | `FPW-021` correction instead of sanction |
| `FPJ-003` | `FPW-001` → `FPW-002` → `FPW-006` → `FPW-005` → `FPW-007` | `FPW-004` exclusion; `FPW-020` misassociation |
| `FPJ-004` | `FPW-007` → `FPW-008` → `FPW-010` → `FPW-011` | `FPW-036` restricted reads |
| `FPJ-005` | `FPW-011` → `FPW-012` → `FPW-013` → `FPW-014` → `FPW-016` | `FPW-021` parallel correction |
| `FPJ-006` | `FPW-021` → `FPW-022` → `FPW-023` → `FPW-026` | `FPW-024` reversal; `FPW-025` compensation |
| `FPJ-007` | `FPW-027` → `FPW-028` → `FPW-029` → `FPW-030` → `FPW-024` | `FPW-041` retention on closure |
| `FPJ-008` | `FPW-033` → `FPW-031` → `FPW-032` → `FPW-034` | `FPW-051` engine halt routing |
| `FPJ-009` | `FPW-019` → `FPW-007` | `FPW-040` deletion request |
| `FPJ-010` | `FPW-045` → `FPW-046` → `FPW-044` → `FPW-033` | `FPW-051` publication halt |

---

## 21. Non-claims carried by this document

1. No workflow here is implemented. No queue, tool, service, record type, trigger, job, screen or ledger exists because this document specifies one (`EVD-041`, `SEC-030`, `GOV-024`).
2. No detection, moderation, privacy, audit, appeal or correction capability has been executed, measured or verified. Every `FPA-` reference resolves to a **specification** with `Definition: COMPLETE` and `Execution: NOT RUN`.
3. No number is approved. Every duration, window, cap, weight, interval, rate and reach value remains exactly as the formula and parameter register states it, and the `PROVISIONAL_BLOCK` branches above are the honest behaviour until the named authority decides.
4. No owner-reserved or legal question is resolved: `UD-017`, `UD-044`, `UD-046`, `UD-050`, `UD-052`…`UD-060` remain Open, and every workflow that touches one says so in its own row.
5. The three Prompt 12B `PARTIAL` gates (`P12B-14`, `P12B-16`, `P12B-23`) and the seven Prompt 12A `PARTIAL` gates are unchanged by this document, and the outstanding security obligations — the authenticated table-wide `UPDATE` on `feasibility.profiles` including `treasury`, the absent corrective migration, the absent SQL permission tests, the absent protective audit trigger, the absent tamper-evident implementation and the absent verification job — remain outstanding and are carried into `FPW-044`–`FPW-046` and `FPW-021` as explicit dependencies, not as satisfied controls.
6. R7 remains implemented-but-not-independently-accepted with its five residual weaknesses unfixed; R8 remains **DEFERRED BY OWNER**; 12B-C1 remains **NOT CLOSED**. This prompt does not change any of those statuses and opens no Prompt 13, 14 or 15 work.
