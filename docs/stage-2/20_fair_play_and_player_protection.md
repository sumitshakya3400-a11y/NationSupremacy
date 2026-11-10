# B-12 — Fair Play, Privacy, Moderation and Administration

**Version:** 1.0 · **Created:** 2026-11-07 · **Stage 2, Prompt 12B**
**Status:** **Specification complete at the documentation level. Unimplemented, unverified and untested.**
**Authority:** This document is the authoritative statement of the B-12 rule family. It defines the policy, evidence, access, audit-shape and enforcement rules. The [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) defines every calculation. The [B-12 requirement register](20_fair_play_and_player_protection_requirements.md) owns the `REQ-764`…`REQ-869` records. Where prose and register diverge, the register governs and this document is corrected.
**Companions:** [12A research](research/12A_fair_play_privacy_moderation_administration_research.md) · [12A source and benchmark register](research/12A_sources_and_benchmarks_register.md) · [12A requirements, integration and risk registers](research/12A_requirements_integration_and_risk_registers.md) · [B-12 requirements](20_fair_play_and_player_protection_requirements.md) · [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) · [B-12 acceptance](20_fair_play_and_player_protection_acceptance.md) · [requirements](03_requirements_traceability.md) · [decisions](../DECISIONS.md) · [mirrored decisions](04_approved_and_provisional_decisions.md) · [unresolved decisions](05_unresolved_design_decisions.md) · [Stage 2 handoff](00_stage_2_handoff.md) · [roadmap](01_stage_2_prompt_roadmap.md) · [progress log](06_stage_2_progress_log.md).

**What this document is not.** It is not an implementation, database schema, API, screen design, moderation staffing plan, legal opinion, retention schedule, calibrated penalty scale or proof of anti-cheat effectiveness. It does not authorize code, migrations, deployment, live data or a release. **Specified ≠ implemented ≠ independently verified ≠ operating.** No claim in this document may be read as evidence that a control exists, runs, is tamper-proof, detects cheating or satisfies a legal obligation.

**Preserved authority.** `D-163`…`D-177` and `DD-211`…`DD-225` are unchanged. `UD-017` and `UD-052`…`UD-060` remain unresolved. `UD-040`…`UD-051` and all other owner/legal dependencies keep their existing status. No B-12 rule resolves, narrows or assumes an answer to an owner-reserved or legal question. Where a rule cannot be completed without such an answer, it states the structure and names the dependency.

---

## 1. Purpose, scope and acceptance target

**FP-001 — Purpose.** *Confirmed design (D-178).* B-12 specifies how Nation Supremacy defines fair play, collects and handles evidence, classifies information, controls moderation and administration, corrects invalid value, protects audit records and maintains security and accounting boundaries across the existing systems.

**FP-002 — Scope.** *Confirmed (D-178).* In scope: violation definitions; evidence states and sufficiency; multi-account and collusion policy; privacy classification and permission; moderation powers; sanctions and appeals; administrative roles and separation of duties; correction and recovery; anti-exploit controls; security and accounting boundaries; cross-system contracts; failure postures; requirement and decision traceability. Out of scope: gameplay mechanics owned by B-02…B-11, numerical balance, screens, schema, migrations, implementation and Prompt 12C workflows.

**FP-003 — Acceptance target.** *Confirmed.* Prompt 12B is complete at the specification level when all ten areas in Prompt 12B §7 have normative rules, every rule resolves to an owning section and requirement, every calculation resolves to the formula register, every affected system has a contract, the owner/legal dependencies are preserved, and the independent validator passes. Acceptance is documentary only.

**FP-004 — No universal controller.** *Confirmed (D-173).* B-12 owns policy, evidence, access, audit shape and enforcement. It owns no gameplay value, resolves no match, market, election, objective, event, campaign or diplomatic outcome, and never writes another subsystem's authoritative state in place.

**FP-005 — Source hierarchy.** *Confirmed (D-014).* Order: (1) owner-fixed constraints and owner-reserved decisions; (2) `AUTONOMOUS_DECISION_POLICY.md`; (3) accepted B-02…B-11 rules and security/privacy architecture; (4) approved decisions and requirements; (5) 12A research and candidates; (6) provisional recommendations; (7) implementation evidence; (8) new reasoning. A lower source never overrides a higher one.

**FP-006 — Research is not a rule.** *Confirmed.* The 106 `12A-CR` candidates are inputs. Their disposition is recorded in the [requirement register](20_fair_play_and_player_protection_requirements.md); only this document's rules and the global `REQ-764`…`REQ-869` rows are binding B-12 requirements. A candidate not adopted here has a recorded reject, merge or defer reason.

**FP-007 — Protected decisions are read, not rewritten.** *Confirmed.* `D-165` (two enforcement classes), `D-167` (five evidence states), `D-168` (network evidence demotion), `D-169` (shared-context declaration), `D-170` (manufactured false agency), `D-171` (three-axis classification), `D-172` (flow and outcome offences), `D-173` (prohibition-list administration), `D-174` (tamper-evident spine), `D-175` (per-category failure), `D-176` (accepted identity residual) and `D-177` (prevention-heavy posture) are consumed exactly as recorded.

**FP-008 — Minimum honest claim.** *Confirmed (D-176, D-177).* This corpus MUST NOT claim perfect identity verification, reliable common-ownership detection, guaranteed detection, complete prevention, surveillance capability, moderation capacity, legal compliance, implemented security or runtime verification.

**FP-009 — One rule family.** *Confirmed (D-178).* Fair play, privacy, moderation, administration, evidence, correction and security boundaries are one rule family because each enforcement decision depends on the same evidence states, classification axes, audit spine and correction model. Splitting them would create competing definitions of evidence and authority.

**FP-010 — Normative language.** *Confirmed.* **MUST/MUST NOT** is mandatory; a violation is a specification defect. **SHOULD/SHOULD NOT** is the expected design and requires a recorded reason to deviate. **MAY** is permitted and creates no obligation. A MAY never becomes a requirement by repetition elsewhere.

---

## 2. Evidence states, terminology and non-claims

**EVD-001 — Five evidence states.** *Confirmed (D-167).* Exactly five states exist: **Suspicion indicator (`E0`)**, **Policy signal (`E1`)**, **Corroborated evidence (`E2`)**, **Established violation (`E3`)** and **Inconclusive (`EX`)**. No sixth state, numeric confidence score or composite risk score may be introduced.

**EVD-002 — Maximum consequence per state.** *Confirmed (D-167).* `E0` and `E1` may produce a review object, a queue priority or a reversible preventive restriction only. `E2` may support a reversible restriction and a value correction where the record proves an impossible effect. Only `E3` may support a conduct sanction above the lowest preventive tier, a suspension or a permanent measure. `EX` produces no adverse action and closes the case with that outcome.

**EVD-003 — Automated ceiling.** *Confirmed (D-167).* Automated rules may create a review object, a policy signal, a reversible preventive restriction or a value correction. They MUST NOT create `E3`, a conduct finding, a suspension, a permanent measure or a public statement.

**EVD-004 — Behaviour alone is insufficient.** *Confirmed (D-018).* A behavioural, statistical, network, timing or clustering anomaly MUST NOT be treated as a violation. It may open a review and may support a finding only with at least one independent non-behavioural source.

**EVD-005 — Network evidence ceiling.** *Confirmed (NET-039, D-168).* A network attribute is triage evidence only. It may never support a sanction above the lowest preventive tier, a permanent measure, a conduct finding or an inference that two accounts have one controller. Counters are keyed to the authenticated account and the protected resource, never to an IP address.

**EVD-006 — Identity residual.** *Confirmed (D-176).* Identity-layer multi-accounting cannot be reliably detected under the current fixed constraints. This is an accepted critical residual, not a control. The limit concerns proving common identity; it does not prevent the use of behavioural, transactional and outcome evidence against a named, evidenced violation.

**EVD-007 — No universal confidence formula.** *Confirmed.* No weighted signal score, probability of guilt or universal confidence number may be used. Sufficiency is decided by the corroboration matrix (`EVD-010`…`EVD-018`) and human review.

**EVD-008 — Inconclusive is a valid closure.** *Confirmed.* Where the available evidence cannot reach `E2` or `E3`, the case closes `EX`. The subject is not sanctioned, the record states what was examined, and the reporter receives a bounded outcome notice.

**EVD-009 — Claim boundary.** *Confirmed.* Every player-facing and internal text MUST distinguish **suspected**, **under review**, **confirmed** and **inconclusive**. Internal codes do not substitute for this distinction.

---

## 3. Fair-play foundations and violation taxonomy

**FP-011 — Server authority.** *Confirmed (SEC-010, D-032).* Every value the game acts on — balance, quantity, result, eligibility, timestamp, ordering and progress — is computed server-side from authoritative state. A client-supplied value is a declaration of intent only.

**FP-012 — Single writer.** *Confirmed (D-064).* Each protected value has exactly one owning subsystem. No other subsystem, tool, moderator or administrator may write it in place. A correction is an appended event through the owner's recorded path.

**FP-013 — Transactional invariants.** *Confirmed.* Every value-changing action is atomic, idempotency-keyed and revalidated at the point of effect. A duplicate submission coalesces to the first committed result. A failed action writes no partial value.

**FP-014 — No order payoff.** *Confirmed (TR-048, SEC-018).* No outcome depends on arrival order inside a turn window. The published deterministic order governs; timing affects only queue position where the owning subsystem explicitly says so.

**FP-015 — Response minimisation.** *Confirmed (TR-021, D-017, D-030).* A response contains only fields the requester's class is entitled to receive. Hidden state is not sent and filtered later. Hiding a field in the client is not access control.

**FP-016 — Enforcement classes are separate.** *Confirmed (D-165).* **Value and standing correction** reverses an effect the published rules could not have produced and requires no finding about a person. **Conduct sanction** addresses behaviour. They have separate evidence thresholds, authority, records, reversibility, calculation and appeal treatment. Neither implies the other.

**FP-017 — One violation taxonomy.** *Confirmed (D-179).* Exactly sixteen violation classes exist, `V-01`…`V-16`, each with the eleven elements in `FP-019`. A rule may not create a seventeenth class without a new decision and a register update.

**FP-018 — Ordinary cooperation is not a violation.** *Confirmed (D-170).* Alliance operations, joint diplomacy, treaties, coordinated defence, negotiated peace, permitted shared objectives, competitive market conduct and strategic voting are legitimate. They become a violation only when an element of a defined class is independently evidenced.

**FP-019 — Every class carries eleven elements.** *Confirmed.* Each class MUST state: (1) definition; (2) required elements; (3) examples; (4) non-examples; (5) evidence indicators; (6) legitimate alternative explanations; (7) severity class; (8) intent/knowledge requirement; (9) demonstrated-impact requirement; (10) enforcement eligibility; (11) reversal/recovery consideration. The class table in Annex A is normative.

**FP-020 — Suspicion is not a finding.** *Confirmed.* A technical anomaly, an unproven allegation, a player report or a detection queue item is not a violation. The case record must state the evidence state and may not use violation language before `E3`.

**FP-021 — No vague catch-all.** *Confirmed.* "Abuse", "cheating", "toxic behaviour" or "exploitation" alone is not a charge. Every notice names the `V-` class and the rule element relied on.

**FP-022 — Intent.** *Confirmed.* Intent or knowledge is required only where Annex A says so. For flow-and-outcome classes, demonstrated effect may establish the offence without proving who controlled the account; for conduct classes, knowledge of the prohibited nature is required unless the class states strict liability.

**FP-023 — Impact.** *Confirmed.* Where Annex A requires demonstrated impact, the finding states the effect on value, eligibility, outcome, another player or system integrity. A merely possible impact is insufficient.

**FP-024 — Attempt.** *Confirmed.* An attempt is actionable only where Annex A names an attempt element and the evidence reaches `E2`. A failed attempt is not retroactively upgraded by an unrelated later event.

**FP-025 — Repetition.** *Confirmed (D-184).* Repetition counts only **confirmed** prior violations (`E3`) within the stated review window. An unconfirmed report, dismissed case or `EX` closure is never an aggravating fact.

**FP-026 — Mitigation.** *Confirmed.* Self-reporting before discovery, full cooperation, immediate cessation, restoration of value and a first honest exploit report are mitigating factors. They may reduce tier but do not erase a finding where impact is material.

**FP-027 — First honest exploit report.** *Confirmed.* A player who reports an exploit before using it for material gain is treated as an incident reporter, not as a violator. Continued use after a fix, or concealment for gain, is a conduct matter.

**FP-028 — Bug exploitation.** *Confirmed.* Using a defect to obtain value, eligibility or outcome the rules do not permit is `V-12`. A good-faith report is not exploitation. The defect is fixed and its effects corrected under `COR-` rules.

**FP-029 — Unauthorized information.** *Confirmed.* Reading or inferring restricted state the actor is not entitled to is `V-13`. A server response that legitimately contains the field is a design defect, not a player violation.

**FP-030 — Administrative abuse.** *Confirmed.* Any privileged act outside the granted purpose, scope or procedure is `V-16`, regardless of whether it changed a value. Self-dealing and evidence tampering are aggravated forms.

**FP-031 — No double jeopardy.** *Confirmed.* One act may produce both a correction and a conduct sanction only when each is independently justified, recorded and appealable. The sanction notice states that the correction is separate.

**FP-032 — Reversal is not forgiveness.** *Confirmed.* Correcting value restores the rules' outcome. It does not by itself reduce, expunge or preclude a conduct finding, and a conduct finding does not by itself determine the correction amount.

**FP-033 — Player-facing boundary.** *Confirmed.* Rules are published in player-usable language, but enforcement thresholds, detection methods, investigation records and other players' data are not disclosed. The published text states the prohibited effect and the appeal route.

**FP-034 — Fixed constraints.** *Confirmed.* No B-12 rule may change the browser delivery, mapless world, two-hour UTC cadence, one-account policy, Cloudflare/Supabase architecture, free-first target or Stage sequencing.

**FP-035 — No retroactive rule.** *Confirmed.* A new violation class or higher tier applies only to conduct after its publication date. A correction may reverse value obtained under an earlier defect because the effect never conformed to the published rules.

---

## 4. Multi-account, shared context and collusion

**MA-001 — One account per person.** *Confirmed (D-018, D-032).* One person holds at most one account. Multiple accounts controlled by one person are prohibited. The project makes no claim that it can prove how many people stand behind an account.

**MA-002 — Account, nation and pair states are separate.** *Confirmed (D-031).* A pair restriction is not an account suspension; a nation may be dormant while its account is active. No fourth state object may be invented.

**MA-003 — Shared-context declaration.** *Confirmed (D-169).* A player may record that named accounts share a device, household, institution or network. The declaration is evidence for review only. It does not clear a pair, permit a transfer, reduce a restriction or make its absence aggravating.

**MA-004 — Declaration access.** *Confirmed.* A declaration is visible only to its author accounts and the integrity role, is deletable by its author, and is never shown to an unrelated player or used as a disclosure channel.

**MA-005 — Network association ceiling.** *Confirmed (EVD-005).* Shared network evidence never proves common control and never supports more than the lowest preventive tier.

**MA-006 — Beneficial flow test.** *Confirmed (D-172).* A multi-account offence may be established from a beneficial flow between accounts that could not occur between independent controllers, without proving common identity.

**MA-007 — Both sides of a flow.** *Confirmed.* Where a flow is established, value may be corrected against either or both sides, recorded against the flow rather than an assumed controller. The correction follows the ledger and preserves the audit trail.

**MA-008 — Ban evasion.** *Confirmed.* Creating or using another account to evade a restriction is `V-05`. It requires evidence of the restriction and the evading account's use; it is never inferred from a shared network alone.

**MA-009 — Shared household legitimacy.** *Confirmed.* Family members, roommates, students and coworkers may each hold an account. Their legitimate interaction is not a violation. A shared address alone is not a basis for restriction.

**MA-010 — Counter keying.** *Confirmed (D-168).* Abuse and rate counters key to the authenticated account and the protected resource. Network attributes may order the review queue only.

**MA-011 — Identity claim prohibited.** *Confirmed (D-176).* No rule, notice, report or public statement may claim identity verification, device uniqueness, household uniqueness or reliable common-ownership detection.

**MA-012 — Residual disclosure.** *Confirmed.* The accepted residual `D-176` / `DD-224` must be disclosed to the owner before any launch claim and must remain visible in the B-12 corpus.

**CO-001 — Manufactured false agency.** *Confirmed (D-170).* Collusion is presenting a non-independent decision-maker as independent: a second account, nation, offer, vote, claim or participant that purports to be independent when it is controlled by, or coordinated for, another participant.

**CO-002 — One test.** *Confirmed.* Scale, similarity, alliance size, shared objectives, coordinated timing that the rules permit and behavioural resemblance are not collusion by themselves. They may support a review only when the false-agency element is independently evidenced.

**CO-003 — Flow patterns.** *Confirmed (D-172).* Repeated one-directional flow, matched opposite-side flows, circular sets and coordinated capture of a shared reward pool are indicators, not findings. Each requires a corroborating non-behavioural record.

**CO-004 — Graph output is a queue input.** *Confirmed.* No topology, clustering or graph score may raise an enforcement tier, create `E3` or impose a sanction by itself.

**CO-005 — Market manipulation.** *Confirmed.* Wash trading, matched self-contra flows, layered inducement and price-signal capture are `V-09` where they create an effect the market rules could not produce. The market's own signals and rules remain authoritative.

**CO-006 — Voting and elections.** *Confirmed.* Coordinated voting is legitimate. Ballot manipulation requires false agency or a breach of the franchise rule, not agreement or persuasion.

**CO-007 — Warfare and objectives.** *Confirmed.* Feeding, slot filling, forged acceptance and manufactured participation are `V-10` where the warfare or objective rules could not produce the recorded effect.

**CO-008 — Alliance finance.** *Confirmed.* Routing a restricted transfer through an Alliance bank or tax to lose pairwise attribution is `V-11`. Alliance treasury authority remains `UD-046`.

**CO-009 — Both legs accountable.** *Confirmed.* Where both sides of a manufactured-false-agency flow are evidenced, both may be accountable, subject to the same evidence and proportionality rules and to `UD-052`.

**CO-010 — No collective punishment.** *Confirmed.* An Alliance, household or group is not sanctioned as a body. Enforcement attaches to evidenced accounts and nations. Alliance-internal discipline remains `UD-044`.

---

## 5. Exploitation, automation and forbidden assistance

**EX-001 — Exploit definition.** *Confirmed.* An exploit is a use of a defect, ambiguity or unintended interaction to obtain value, eligibility, standing or outcome the published rules do not permit.

**EX-002 — Duplicate value.** *Confirmed.* Duplicate rewards, replayed settlement, double spend and refund duplication are `V-12`. The ledger's own correction path reverses the duplicate; the conduct finding is separate.

**EX-003 — Race and replay.** *Confirmed.* Exploiting a race condition, non-atomic check-then-act or expired idempotency window is `V-12`. Every value path must be atomic and replay-resistant in the same transaction.

**EX-004 — Automation.** *Confirmed.* Unauthorized automation that substitutes for human play to obtain value, eligibility or competitive standing is `V-06`. Simple accessibility tools, screen readers and permitted client behaviour are not automation abuse.

**EX-005 — Bot distinction.** *Confirmed.* A bot is an automated process acting in play. A script that merely formats a legal action for human confirmation is not a bot unless it decides or submits without human intent.

**EX-006 — Client modification.** *Confirmed.* Modifying the delivered client, intercepting or altering responses, or injecting state to obtain restricted information or value is `V-07`.

**EX-007 — Information extraction.** *Confirmed.* Scraping restricted state, enumerating hidden identifiers or reconstructing hidden values from response differences is `V-13`. Public aggregate publication at `k ≥ 5` is permitted.

**EX-008 — Rate and quota abuse.** *Confirmed.* Circumventing a declared rate, quota, slot or cooldown is `V-14`. The limit's owning subsystem defines the legal allowance; B-12 supplies the enforcement response.

**EX-009 — Restriction circumvention.** *Confirmed.* Acting through another account, Alliance, market route or proxy to evade an account, pair or market restriction is `V-05`.

**EX-010 — Reversal abuse.** *Confirmed.* Manufacturing a correction, false appeal or fabricated evidence to obtain compensation, restore illicit value or harm another party is `V-15` and may be an aggravated administrative matter.

**EX-011 — Failure exploitation.** *Confirmed.* Using an outage, failed turn, partial settlement or recovery state to obtain value or avoid a consequence is `V-12`. Recovery must reconcile to the authoritative pre-failure state.

**EX-012 — No client-only control.** *Confirmed.* A limit, permission or invariant that protects value MUST be enforced server-side in the transaction that writes the value. Browser validation and RLS alone are insufficient.

---

## 6. Detection, investigation and evidence sufficiency

**EVD-010 — Corroboration matrix.** *Confirmed (D-180).* Evidence sufficiency is determined by source count and independence, not by a score. The minimum matrix is normative:

| Claim type | Minimum evidence | May produce |
|---|---|---|
| Suspicious pattern | one `E0` source | review object only |
| Policy signal | one `E1` source plus a stated rule | priority and reversible hold |
| Value correction | record proves an impossible effect (`E2`) | correction, no conduct finding |
| Conduct finding | `E3`: at least two independent sources, one non-behavioural | sanction within the tier |
| Identity/common control | not establishable | must not be claimed |

**EVD-011 — Independence.** *Confirmed.* Two outputs of the same detector, two reports repeating the same allegation and two records derived from one underlying event are not independent sources.

**EVD-012 — Investigation record.** *Confirmed.* Every case names the evidence examined, the rule elements, the reviewer, the decision, the date and the outcome, including `EX`.

**EVD-013 — Report is an accusation.** *Confirmed.* A player report is stored as an accusation, never as a finding. Player-supplied evidence is a pointer to be corroborated against server records.

**EVD-014 — False-positive catalogue.** *Confirmed.* The maintained catalogue MUST include shared households and devices, universities and workplaces, public and mobile networks, CGNAT, VPN use, travel, families, similar schedules, legitimate alliance strategy and mechanics-induced behaviour.

**EVD-015 — Detection rule declaration.** *Confirmed.* Every detection rule states its purpose, data source, legitimate triggers, false-positive classes, minimum corroboration and permitted automated output before it is enabled.

**EVD-016 — No undisclosed collection.** *Confirmed (DAT-007, D-042).* Detection reads only data already held for gameplay, account-security or legal purposes. No behavioural telemetry, client agent, keystroke log, device fingerprint or monitoring SDK is introduced.

**EVD-017 — Unavailable capability.** *Confirmed.* Where a capability would require refused data, it is recorded as **not available**, not softened into a weaker claim or an undisclosed proxy.

**EVD-018 — Conflict of records.** *Confirmed.* Where two server-record sources conflict, the conflict is recorded and resolved explicitly. A case may not adopt the more convenient record without stating why.

**EVD-019 — Case assignment.** *Confirmed.* A reviewer who is a party or has a declared interest is excluded. Where staffing cannot exclude them, the record is labelled **unsegregated** and the outcome is disclosed to the affected player.

**EVD-020 — Case outcomes.** *Confirmed.* A case closes as `NO_ACTION`, `INCONCLUSIVE`, `CORRECTION_ONLY`, `CONDUCT_ONLY`, `CORRECTION_AND_CONDUCT` or `REFERRED`. Every closure states the reason and the evidence state.

**EVD-021 — Evidence preservation.** *Confirmed.* On case opening, the relevant immutable records are referenced and protected from routine compaction. Preservation does not authorize indefinite retention; the retention dependency is `UD-055`.

**EVD-022 — Chain of custody.** *Confirmed.* Every access, annotation, correction and export of case evidence is itself an audit event. Corrections append a new disclosed event referencing the original; nothing is edited in place.

**EVD-023 — Evidence quality.** *Confirmed.* A finding must identify each artefact's provenance, producer, timestamp and integrity reference. An unattributed screenshot, memory or verbal report is insufficient.

**EVD-024 — Evidence minimisation.** *Confirmed.* Evidence is case-scoped, minimised, and never copied into operational logs, analytics or a support tool's default view.

**EVD-025 — Case access.** *Confirmed.* Case access is purpose-bound and logged. A privileged read of a restricted case is auditable even when no state changes.

---

## 7. Privacy classification and permissions

**PRV-001 — Three axes.** *Confirmed (D-171).* Every field maps to exactly one value on three orthogonal axes: **handling class** (`Public`, `Private`, `Restricted`, `Secret`), **subject visibility** (`Public`, `Participant`, `Alliance`, `Private`, `Operational`, `Moderation`, `Security`, `Audit`) and **record purpose class** (`S` state, `P` public history, `O` operational, `SPINE` audit).

**PRV-002 — Nine operational classes.** *Confirmed (D-183).* For access decisions the following nine classes are normative: `PUB`, `PLAYER`, `ALLIANCE`, `OPS`, `MOD`, `PERSONAL`, `SEC`, `AUDIT`, `LEGAL`. Annex B maps them to the three axes.

**PRV-003 — Reconciliation duty.** *Confirmed.* Where an owning register already assigns a class, B-12 reconciles rather than reassigns. A conflict is resolved in the owning register with a dated decision.

**PRV-004 — Purpose before permission.** *Confirmed.* Each restricted read names the purpose it serves and the requirement that authorises it. Convenience is not a purpose.

**PRV-005 — Eight actor classes.** *Confirmed.* Exactly eight actor classes are recognised: **Player**, **Alliance personnel**, **Moderator**, **Appeals reviewer**, **Investigator**, **Administrator**, **Operator/emergency privileged** and **Audit reviewer**. A person may hold several roles; the permission is evaluated per action, not per identity.

**PRV-006 — Six actions.** *Confirmed.* Permissions are granted separately for **view**, **search**, **export**, **modify**, **delete** and **disclose**. Viewing never implies search, export, modify, delete or disclosure.

**PRV-007 — API minimisation.** *Confirmed.* A response MUST omit every field the requester's classes exclude. A hidden UI component is not a control.

**PRV-008 — Public.** *Confirmed.* `PUB` is visible to anyone, including unauthenticated readers, and may be cached or indexed. No personal, moderation, security or audit field may be `PUB`.

**PRV-009 — Player-visible.** *Confirmed.* `PLAYER` is visible to the subject and to other players only where the owning subsystem publishes it. It never includes private notices, pair state, investigation state or another player's account data.

**PRV-010 — Alliance-restricted.** *Confirmed.* `ALLIANCE` is visible to current members under the Alliance's own permission rules. Tax, contribution and treasury detail are minimised; a member does not acquire another member's private data by joining.

**PRV-011 — Operationally restricted.** *Confirmed.* `OPS` is visible to operators for a named operational purpose. It is logged and is not exportable by default.

**PRV-012 — Moderation-confidential.** *Confirmed.* `MOD` is visible to assigned moderators, the appeals reviewer and the audit reviewer. It is never visible to the reported party except as the bounded decision summary.

**PRV-013 — Sensitive personal.** *Confirmed.* `PERSONAL` includes account identifiers, contact data and any derived identifier that remains personal data. It is purpose-bound, access-logged and not exportable except to the subject or under a recorded legal obligation.

**PRV-014 — Security-sensitive.** *Confirmed.* `SEC` includes credentials, session tokens, keys, detection internals and privileged configuration. No player-facing or moderation surface may return it.

**PRV-015 — Audit.** *Confirmed.* `AUDIT` is the spine and case record. It is readable only by the audit role and by a purpose-bound reviewer; every read is logged.

**PRV-016 — Legal/retention-dependent.** *Confirmed.* `LEGAL` is a legal-hold or retention-dependent class. Its duration and disclosure rules depend on `UD-017` / `UD-055`; B-12 states the structure and does not invent a period.

**PRV-017 — Classification change.** *Confirmed.* A class change is a recorded decision, versioned with the field, and never a side effect of a deployment. Historical records retain the class under which they were created.

**PRV-018 — Aggregates.** *Confirmed (D-027).* A published aggregate names its quasi-identifiers, satisfies `k ≥ 5`, uses stable merging and complementary suppression, and states its inference argument. A figure that can single out a nation is withheld or coarsened.

**PRV-019 — No status disclosure.** *Confirmed.* No player-facing surface reveals another player's restriction, investigation, verification, appeal or report state. No badge, ranking note or chronicle entry carries that fact.

**PRV-020 — Failure text.** *Confirmed.* An error or rejection identifies the failed condition in usable terms without revealing a detection rule, threshold, another player's data or whether an account exists.

**PRV-021 — Export.** *Confirmed.* Export requires a separate permission, a stated purpose and a recorded event. A moderator who may view a case may not export it by default.

**PRV-022 — Deletion.** *Confirmed.* Deletion is a separate permission and a recorded event. Where an external obligation requires deletion, the case records a redaction and the surviving record states what was removed and under what authority.

**PRV-023 — Retention.** *Confirmed.* Retention is per class with a stated justification and review trigger. B-12 adopts no new day-count; `D-026`, `D-042`, `UD-017` and `UD-055` govern.

**PRV-024 — Pseudonymous is not anonymous.** *Confirmed.* A keyed digest or derived identifier is labelled pseudonymous and carries a written identifiability assessment. The key is held outside the database, excluded from the repository, logs and backups, and has a rotation plan.

**PRV-025 — No profiling decision.** *Confirmed.* No automated profile, score or inferred attribute may decide a sanction. The refusal to profile is both a design choice and a compliance asset.

---

## 8. Moderation powers and restrictions

**MOD-001 — Separation of lanes.** *Confirmed.* Value correction, conduct moderation, security investigation and system administration are four separate lanes. A person acting in one lane does not acquire the authority of another.

**MOD-002 — Report intake.** *Confirmed.* Intake captures category, subject, time window, reporter account and a free-text account, and separately stores any supplied evidence. A report is an accusation.

**MOD-003 — Duplicate clustering.** *Confirmed.* Duplicate reports of the same conduct cluster to one case. Coordinated report volume is a triage signal and never raises a tier against the reported party.

**MOD-004 — False reporting.** *Confirmed.* A knowingly false report is `V-15`. A good-faith report that is not substantiated is not a violation.

**MOD-005 — Confidential routing.** *Confirmed.* A report against an administrator, moderator or reviewer is routed confidentially to an independent reviewer where one exists; otherwise it is labelled unsegregated and disclosed to the owner.

**MOD-006 — Retaliation.** *Confirmed.* Retaliation against a reporter is `V-15` with its own evidence path.

**MOD-007 — Intake acknowledgement.** *Confirmed.* Every report receives an acknowledgement and a case reference. The acknowledgement does not state a finding or a predicted outcome.

**MOD-008 — Triage.** *Confirmed.* Every case is triaged for safety, evidence state, subject status and conflict of interest before any action.

**MOD-009 — Initial assessment.** *Confirmed.* The first assessment records whether the report is actionable, what evidence exists and whether a reversible hold is justified. A hold is not a sanction.

**MOD-010 — Investigation.** *Confirmed.* An investigation gathers server records, examines the rule elements, records the evidence state and either reaches a finding or closes `EX`.

**MOD-011 — Warning.** *Confirmed.* A warning is a recorded notice attached to the account. It is not a restriction and may be appealed once.

**MOD-012 — Temporary restriction.** *Confirmed.* A temporary restriction limits a named capability for a turn-counted period. It requires at least `E2`, a stated scope, an expiry and a review.

**MOD-013 — Communication restriction.** *Confirmed.* A communication restriction limits named channels only. It never blocks access to the appeal route or to account-security notices.

**MOD-014 — Content removal.** *Confirmed.* Where a content surface exists, removal requires a stated rule, a preserved copy for the case record and a notice. B-12 does not create a content surface.

**MOD-015 — Suspension.** *Confirmed.* A suspension disables play for an account while preserving access to the appeal and data-subject routes. It requires `E3`, a tier within authority and a written reason.

**MOD-016 — Permanent measure.** *Confirmed.* A permanent suspension or closure requires the highest evidence, the owner-authorized tier and independent review where staffing permits. It is never automated and never based on `E0` or `E1`.

**MOD-017 — Notice content.** *Confirmed.* Every significant action states the `V-` class, the rule element, the evidence class, the tier, the end condition, the appeal route and the correction (if any) in player-usable terms.

**MOD-018 — Method secrecy.** *Confirmed.* The notice withholds detection methods, thresholds, other players' data and investigation detail by rule, not by reviewer discretion.

**MOD-019 — Moderation is not administration.** *Confirmed.* A moderator may act on an account; a moderator may not edit game state, set a balance, change an election, alter a snapshot or rewrite history.

**MOD-020 — Least privilege.** *Confirmed.* Each power is a named permission with a purpose, scope and evidence threshold. A role cannot grant a permission it does not hold.

**MOD-021 — Conflict of interest.** *Confirmed.* A moderator who is a party, an Alliance member of the subject or has a declared interest is excluded from the decision. The record states the exclusion.

**MOD-022 — Two-person review.** *Confirmed.* Suspensions above the first tier, permanent measures, emergency actions and appeals against a senior moderator require a second reviewer where staffing exists. Where it does not, the case is labelled unsegregated.

**MOD-023 — Moderator accountability.** *Confirmed.* Every moderation action is recorded with actor, purpose, target, evidence reference and outcome, and is reviewable by the audit role.

**MOD-024 — Prohibited moderation uses.** *Confirmed.* A moderation power MUST NOT be used to favour an Alliance, punish a report, win a competition, discourage diplomacy, enforce an in-game agreement or obtain private information.

**MOD-025 — Emergency boundary.** *Confirmed.* An emergency power may suspend, freeze or withhold; it may not delete, confiscate, transfer or rewrite history. Permanent effect requires the ordinary path and its appeal.

**MOD-026 — Emergency expiry.** *Confirmed.* Every emergency measure states its scope, a turn-counted expiry and the review required before extension. It self-expires.

**MOD-027 — Emergency disclosure.** *Confirmed.* Players are told that a temporary measure is in force and when it will be reviewed, without disclosing the threat or another party's data.

**MOD-028 — Retrospective review.** *Confirmed.* Every emergency action is reviewed by someone other than its author where staffing permits, and the outcome is recorded whether or not the action is reversed.

**MOD-029 — Moderation capacity.** *Confirmed.* The design does not assume a capacity it has not measured. Where staffing cannot meet a review guarantee, the gap is declared with its compensating control.

**MOD-030 — No silent action.** *Confirmed.* No enforcement action is invisible to the affected account. A delayed notice is permitted only where an active investigation would be compromised, and the delay and its review are recorded.

**MOD-031 — Cross-system authority.** *Confirmed.* Where the affected capability belongs to a market, Alliance, diplomacy, warfare or progression system, the owning subsystem's rule and evidence remain authoritative. Moderation acts only through its own recorded action on the account.

**MOD-032 — Duplicate enforcement.** *Confirmed.* Duplicate or conflicting actions against one account or nation are surfaced to a reviewer, not silently applied or dropped.

**MOD-033 — Sanction survival.** *Confirmed.* A sanction attaches to the account and survives a nation reroll. A pair restriction survives closure where the owning rule says so.

**MOD-034 — Record correction.** *Confirmed.* A wrong sanction is corrected by an appended event referencing the original. The original is never deleted.

**MOD-035 — Review loop.** *Confirmed.* Enforcement practice is reviewed periodically against a stated capacity assumption and observed false-positive rate. The outcome is recorded even when nothing changes.

---

## 9. Sanctions, corrections and appeals

**MOD-036 — One ladder.** *Confirmed (D-181).* Exactly six conduct tiers exist: `T0` no action, `T1` warning, `T2` temporary capability restriction, `T3` suspension, `T4` extended suspension, `T5` permanent measure. No parallel ladder, letter grade or level numbering may be introduced.

**MOD-037 — Tier authority.** *Confirmed.* `T0`–`T2` may be imposed by a moderator within the published scope; `T3` requires a senior moderator or second review where staffing permits; `T4` and `T5` require the owner-authorized threshold and independent review where available. Numeric durations and the authority split are `UD-053`.

**MOD-038 — Evidence per tier.** *Confirmed.* `T0` requires no finding. `T1`–`T2` require at least `E2`. `T3`–`T5` require `E3` and a stated impact. No tier may be imposed on `E0`, `E1` or `EX`.

**MOD-039 — Proportionality factors.** *Confirmed.* Severity is assessed from intent, proven impact, frequency, repetition, deliberateness, harm, evidence confidence, confirmed priors and mitigation. The structural severity index is `F-FP-001`; weights are provisional. Repetition is applied exactly once, through `F-FP-011`; `F-FP-001` contains no repetition term, and economic correction is never increased by a prior violation.

**MOD-040 — Duration form.** *Confirmed.* Every temporary measure is expressed in turn boundaries, not wall-clock minutes. A measure that would end outside a boundary ends at the next boundary.

**MOD-041 — Expiry.** *Confirmed.* A temporary measure expires automatically. Extension is a new decision with a new reason and, where required, a new review.

**MOD-042 — Appeal eligibility.** *Confirmed (D-185).* Every account-affecting action from `T1` upward is appealable once on stated grounds. `T0` has no appeal because it imposes no burden; a factual correction may still be requested.

**MOD-043 — Appeal in force.** *Confirmed.* The action stays in force pending the appeal unless the reviewer grants a reversible hold. A hold is recorded and does not decide the appeal.

**MOD-044 — Appeal grounds.** *Confirmed.* Grounds are: the rule was not breached; the evidence is wrong or insufficient; the tier is disproportionate; the procedure was defective; new evidence exists. A disagreement with the rule's existence is a policy feedback item, not an appeal ground.

**MOD-045 — Appeal decision.** *Confirmed.* The decision is written, reasoned and states the outcome: `UPHELD`, `REDUCED`, `REVERSED` or `REMANDED`. A remand names the procedural defect and the reviewer.

**MOD-046 — Reopening.** *Confirmed.* A case reopens only on genuinely new evidence or a procedural defect. A repeat appeal on the same grounds is closed without re-investigation and the closure is recorded.

**MOD-047 — Reversal.** *Confirmed.* A reversed action is removed by an appended event; a restriction ends; a suspension is lifted; the record states the reversal and its reason.

**MOD-048 — Restitution.** *Confirmed.* Where value moved, reversal triggers the owning subsystem's restitution under its own rules. An administrator does not calculate or type a compensation amount.

**MOD-049 — Independence disclosure.** *Confirmed.* An appeal decided by the original reviewer is labelled **not independent**. The design states which independence guarantees exist at current staffing and does not claim more.

**MOD-050 — Appeal deadlines.** *Confirmed.* Filing windows, decision targets and appeal budgets are structured but numerically provisional under `UD-059`. No invented number is binding.

**MOD-051 — Correction definition.** *Confirmed (D-165).* A correction reverses an effect the published rules could not produce, established from the record, without needing to identify a person. It is always reversible.

**MOD-052 — Correction authority.** *Confirmed.* A correction is executed by the owning subsystem's recorded path with a reason code and a reference to the original. No administrator writes a balance in place.

**MOD-053 — Correction amount.** *Confirmed.* The correction restores the counterfactual lawful state, capped at the illicit benefit actually obtained. The structural calculation is `F-FP-002`; valuation inputs are provisional.

**MOD-054 — Correction disclosure.** *Confirmed.* The affected account is told that a correction occurred, the rule effect reversed, the amount or state change and the appeal route. Third-party data is not disclosed.

**MOD-055 — Correction and sanction separation.** *Confirmed.* A correction does not imply a conduct finding. A conduct finding does not determine the correction amount. Each is recorded and appealable separately.

**MOD-056 — Compensation.** *Confirmed.* Compensation for a proven loss caused by an enforcement or system error is an authorized corrective transaction, not a discretionary grant. The structural cap is `F-FP-015`; the policy is provisional.

**MOD-057 — Illicit benefit removal.** *Confirmed.* Value obtained through a violation is removed through the owning ledger even where the account is also sanctioned. The removal is recorded as a correction, not as a fine.

**MOD-058 — No punitive minting.** *Confirmed.* A sanction never creates value for the operator, a reporter or another player. Correction conserves total value except where the owning system's own rules create or destroy it.

**MOD-059 — Restoration.** *Confirmed.* A state restoration after a technical failure returns the authoritative pre-failure state or the state the rules would have produced. It is not a discretionary reward.

**MOD-060 — Error correction.** *Confirmed.* Every enforcement or correction error has a named correction path, a record, a notice and, where value moved, restitution.

---

## 10. Administrative roles, permissions and separation of duties

**ADM-001 — Prohibition list.** *Confirmed (D-173).* No administrative role may: set a treasury or resource balance; alter a battle, campaign or election outcome; change a standing or snapshot; change an objective result; grant material reward outside a registered path; alter diplomatic, Alliance or pair state; or delete or edit an audit record.

**ADM-002 — No superuser.** *Confirmed.* There is no "see everything", "do everything" or default-inherited administrator role. Every capability is named and individually granted.

**ADM-003 — Role catalogue.** *Confirmed (D-182).* Exactly eight roles are recognised: `R-MOD` moderator, `R-SMOD` senior moderator, `R-APL` appeals reviewer, `R-INV` security investigator, `R-SEC` security administrator, `R-OPS` technical operator, `R-AUD` audit/compliance reviewer, `R-EMG` emergency privileged operator. A role may be combined in one person; the permissions remain separate.

**ADM-004 — Role responsibilities.** *Confirmed.* Annex C defines each role's responsibilities, permitted actions, prohibited actions, read/write scope, approval requirements, separation duties, audit duties, delegation limits, escalation authority and revocation conditions.

**ADM-005 — Least privilege.** *Confirmed.* A role receives only the permissions its purpose requires. Read access is narrower than write access and does not imply export.

**ADM-006 — No escalation by grant.** *Confirmed.* A role cannot grant a permission it does not hold. Delegation is time-bounded, purpose-bound and recorded.

**ADM-007 — Step-up authentication.** *Confirmed.* Privileged action requires an authenticated step-up distinct from ordinary play credentials. A privileged session is shorter, separately logged and revocable independently.

**ADM-008 — Privileged read audit.** *Confirmed.* A privileged read of a restricted record is an auditable event with actor, purpose, target and time, even when no state changes.

**ADM-009 — Self-dealing.** *Confirmed.* No administrator may exercise a capability against their own account, nation, Alliance or declared interest without a second approval where one exists. Where none exists, the action is recorded, disclosed on request and retrospectively reviewed.

**ADM-010 — Investigate versus decide.** *Confirmed.* The permission to investigate and the permission to make the final conduct decision are distinct. A single person may hold both only where the case is labelled unsegregated and reviewed.

**ADM-011 — Author versus publisher.** *Confirmed.* The person who authors an enforcement-affecting configuration change may not also be the sole publisher. Where no second person exists, publication requires a recorded disclosure and retrospective review.

**ADM-012 — Financial separation.** *Confirmed.* A financial correction is executed by the economy ledger under a reason code. The account holder, the moderator and the administrator do not type a balance.

**ADM-013 — Declared control gap.** *Confirmed.* Where separation is impossible at current staffing, the gap is recorded with its compensating control and is never described as separation of duties.

**ADM-014 — Emergency privilege scope.** *Confirmed.* Emergency privilege is purpose-limited, time-limited, scoped to the incident, recorded and retrospectively reviewed. It does not include the prohibition list.

**ADM-015 — Emergency authority.** *Confirmed.* Only the named emergency role may invoke emergency powers. The invocation states the incident, the scope, the expiry and the review owner. The authority source remains `UD-056`.

**ADM-016 — Revocation.** *Confirmed.* A role is revoked when its purpose ends, the person changes function, a conflict is declared or a session is compromised. Revocation is immediate and recorded.

**ADM-017 — Access review.** *Confirmed.* The role-to-permission mapping is reviewed periodically and after every incident. The review outcome is recorded.

**ADM-018 — Permission register.** *Confirmed.* The permission register is the authoritative list of capabilities. A capability not in the register does not exist.

**ADM-019 — Purpose binding.** *Confirmed.* A privileged action outside its named purpose is `V-16`, even if the action would otherwise be permitted.

**ADM-020 — No covert action.** *Confirmed.* No administrative action may be hidden from the audit spine. Concealment is itself a violation and an incident.

**ADM-021 — Moderator scope.** *Confirmed.* A moderator may view `MOD` records for assigned cases, issue `T0`–`T2` within scope and request escalation. A moderator may not read `SEC`, export evidence, change a balance or alter a snapshot.

**ADM-022 — Appeals reviewer scope.** *Confirmed.* An appeals reviewer may view the case record and the bounded evidence needed to decide, may uphold, reduce, reverse or remand, and may not investigate the original case or alter the audit record.

**ADM-023 — Investigator scope.** *Confirmed.* An investigator may open a case, preserve evidence and recommend a finding. An investigator may not impose a sanction or decide the appeal.

**ADM-024 — Security administrator scope.** *Confirmed.* A security administrator may manage sessions, keys, permission mappings and incident containment within the recorded policy. It may not edit game value or audit history.

**ADM-025 — Technical operator scope.** *Confirmed.* A technical operator may run the turn, deploy the service and manage infrastructure. It may not use production access to inspect player private data outside an incident purpose.

**ADM-026 — Audit reviewer scope.** *Confirmed.* The audit reviewer may read the spine and case records, verify integrity and report findings. It may not alter the spine, decide a case or grant a permission.

**ADM-027 — Emergency operator scope.** *Confirmed.* The emergency operator may freeze a capability, suspend a service or preserve evidence to contain an incident. It may not perform a permanent action or bypass the appeal route.

**ADM-028 — Delegation.** *Confirmed.* Delegation is permitted only for a named case, purpose and expiry, and only within the delegator's own permissions. A delegation is recorded and revocable.

**ADM-029 — Escalation.** *Confirmed.* A moderator escalates a case beyond their tier authority; an investigator escalates a sanction decision; an operator escalates a policy question. Escalation does not transfer the record's ownership.

**ADM-030 — Administrative notice.** *Confirmed.* A player affected by an administrative action receives a bounded notice unless an active investigation requires delay; the delay and its review are recorded.

---

## 11. Audit, evidence lifecycle and integrity

**EVD-026 — Audit event set.** *Confirmed.* The spine records: privileged access; permission changes; investigation and evidence reads/writes; moderation and disciplinary actions; appeal outcomes; administrative overrides; emergency actions; financial corrections; configuration publication; and integrity-verification results.

**EVD-027 — Record shape.** *Confirmed.* Each event class has a defined shape: event type, actor, purpose, target, timestamp, turn or boundary, decision, reason code, evidence reference and outcome. The shape is owned here and consumed by B-02's spine.

**EVD-028 — Contents.** *Confirmed.* Audit rows contain identifiers, decisions and reasons. They never contain free-form player content, message bodies, secrets or raw credentials.

**EVD-029 — Append-only correction.** *Confirmed.* An audit record is corrected only by an appended correcting event referencing the original. A deletion under external obligation is recorded as a deletion event with its authority.

**EVD-030 — Protection.** *Confirmed (D-174).* The spine MUST carry chained digests over its records, restricted readership and a scheduled verification job whose failure raises an incident. Append-only by convention is not tamper-evidence.

**EVD-031 — Chain construction.** *Confirmed.* Each record's digest covers the record's canonical fields and the previous record's digest. The structural construction is `F-FP-012`; the algorithm and canonicalisation are fixed there; no secret is stored in the row.

**EVD-032 — Verification.** *Confirmed.* The verification job checks the chain from the last verified checkpoint, records the result and escalates a break. Enabling verification does not validate; the run is the evidence. The interval is provisional (`F-FP-013`).

**EVD-033 — Readership.** *Confirmed.* Spine readership is a published internal register, granted by purpose. Every read is logged. The audit role may verify but not rewrite.

**EVD-034 — No sampling.** *Confirmed.* Spine rows are never sampled away for quota. Where volume forces tiering, value-mutation, pipeline, privileged-act and enforcement rows are retained first.

**EVD-035 — Evidence lifecycle.** *Confirmed.* The lifecycle is: identify → collect → preserve → classify → link → assess → disclose (bounded) → retain → redact/delete under obligation → close → review. Every transition is recorded.

**EVD-036 — Provenance.** *Confirmed.* Each artefact names its producer, source system, timestamp and integrity reference. A copied artefact retains its original reference.

**EVD-037 — Integrity.** *Confirmed.* Case artefacts are hashed and referenced by digest. A mismatch is an incident, not a routine correction.

**EVD-038 — Redaction.** *Confirmed.* Redaction removes the protected content but preserves a record that redaction occurred, its authority and the remaining reference. It is never a silent deletion.

**EVD-039 — Legal hold.** *Confirmed.* A legal hold suspends routine deletion for the named records. The hold's authority and scope remain `UD-017` / `UD-055`; B-12 does not invent a period.

**EVD-040 — Review history.** *Confirmed.* Every case review, annotation, escalation and outcome is appended to the case history and is visible to the appeal reviewer.

**EVD-041 — Implementation status.** *Confirmed.* The chained-digest spine and verification job are a **documented candidate design and specified requirement**. They are not implemented, not running and not independently verified. The prototype `audit` table has no protective trigger.

**EVD-042 — No tamper-proof claim.** *Confirmed.* No document may state that the audit trail is tamper-proof, immutable in production, monitored or verified. Hashing is specified; operation is not.

---

## 12. Correction, reversal and recovery accounting

**COR-001 — Six transaction types.** *Confirmed (D-184).* Corrections and reversals distinguish exactly six transaction types: `ORIGINAL` (the transaction under review), `CORRECTION` (restores a lawful effect), `REVERSAL` (undoes a specific transaction), `COMPENSATION` (authorized restoration for a proven loss), `ILLICIT_REMOVAL` (removes a benefit obtained through violation) and `ADMIN_ADJUSTMENT` (a recorded administrative change permitted by policy). No seventh type without a decision.

**COR-002 — Reference to original.** *Confirmed.* Every corrective transaction references the original transaction or state it corrects. An unreferenced correction is invalid.

**COR-003 — Conservation.** *Confirmed.* Every transaction carries a signed ledger delta (credit positive, debit negative). For every correction, `closing = opening + Σ signed deltas of ORIGINAL, CORRECTION, REVERSAL, COMPENSATION, ILLICIT_REMOVAL and ADMIN_ADJUSTMENT`, and no balance is negative. A reversal appends the exact opposite of the referenced transaction's remaining unreversed effect; a partial reversal is bounded by that remainder; a duplicate reversal coalesces under `COR-005`. The identity is `F-FP-014`.

**COR-004 — No in-place edit.** *Confirmed.* A balance, quantity or state is never edited in place. The owning ledger appends.

**COR-005 — Idempotency.** *Confirmed.* A corrective transaction carries an idempotency key derived from the case, original and type. A duplicate submission coalesces.

**COR-006 — Caps.** *Confirmed.* A correction never exceeds the illicit benefit actually obtained. Compensation never exceeds the proven loss and the provisional cap `F-FP-015`.

**COR-007 — Ordering.** *Confirmed.* Where multiple corrections affect one balance, they apply in the recorded case order at the owning subsystem's next valid boundary. No correction reorders a closed turn.

**COR-008 — Dispute.** *Confirmed.* A correction may be disputed once through the appeal route. The correction stays in force pending the decision unless a reversible hold is granted.

**COR-009 — Correction of correction.** *Confirmed.* A wrong correction is corrected by a further appended transaction referencing the wrong correction. The chain is never rewritten.

**COR-010 — Sanction independence.** *Confirmed.* A correction is valid without a conduct finding and is appealable without contesting conduct.

**COR-011 — Illicit removal.** *Confirmed.* Removal follows the flow to the benefiting account. Where value has moved on, the owning ledger applies its own recovery order and records the shortfall; it does not create a negative balance.

**COR-012 — Insolvency.** *Confirmed.* Where a benefiting account cannot cover removal, the balance floors at zero and the shortfall is recorded. B-12 does not invent a debt mechanic.

**COR-013 — State restoration.** *Confirmed.* A state restoration is a `REVERSAL` or `CORRECTION` through the owner's path, not a fresh grant. It restores the lawful state, not the violator's expected gain.

**COR-014 — Compensation authority.** *Confirmed.* Compensation requires a recorded finding of project error, a stated loss and the owner-authorized policy. It is not a discretionary goodwill grant.

**COR-015 — Notification.** *Confirmed.* The affected account is notified of the type, amount or state change, reason and appeal route.

**COR-016 — Audit.** *Confirmed.* Every corrective transaction is a spine event with the case reference, original reference and authority.

**COR-017 — Reconciliation.** *Confirmed.* After a batch of corrections, the owning ledger reconciles opening and closing totals and records any residual. An unreconciled correction is an incident.

**COR-018 — Failure recovery.** *Confirmed.* A failure during correction rolls back the transaction or completes it exactly once on retry. A partial correction is prohibited.

---

## 13. Anti-exploit and security-accounting boundaries

**SEC-001 — Server validation.** *Confirmed.* Every consequential action validates actor, object, quantity, timing and entitlement server-side at execution.

**SEC-002 — Object authorization.** *Confirmed.* Each referenced object is authorized separately. A request body, query or path never establishes identity.

**SEC-003 — Idempotency.** *Confirmed.* Every value-changing operation is idempotency-keyed. The retention window is at least the longest legitimate retry path, expressed in turn boundaries (`F-FP-010`).

**SEC-004 — Atomicity.** *Confirmed.* A transaction writes all of its effects or none. A partial write is a defect.

**SEC-005 — Consistency.** *Confirmed.* The owning ledger's invariants are checked in the same transaction. A post-hoc reconciliation alone is insufficient.

**SEC-006 — Replay resistance.** *Confirmed.* A replayed request after the key window is rejected by state or entitlement, not merely by the key's absence.

**SEC-007 — Rate limits.** *Confirmed.* Limits key to the authenticated account and protected resource. The structural allowance is `F-FP-009`; numeric values are provisional.

**SEC-008 — Duplicate operation.** *Confirmed.* A duplicate submission coalesces to the first committed result and produces one record.

**SEC-009 — Failure handling.** *Confirmed.* Value-moving, authorizing and audit-writing controls fail closed with the transaction. Informational controls degrade without silent re-derivation.

**SEC-010 — Recovery.** *Confirmed.* Recovery is forward-only or restores the last committed state. It never re-executes a committed action.

**SEC-011 — Boundary: client/server.** *Confirmed.* The client sends intent; the server computes outcome. No client-supplied value is trusted for balance, result, eligibility or ordering.

**SEC-012 — Boundary: public/private.** *Confirmed.* Public responses contain only `PUB` and published aggregate data. Restricted fields are never sent and hidden later.

**SEC-013 — Boundary: gameplay/economic.** *Confirmed.* Gameplay services request economic effects through the economy's ledger; they never write a balance. The economy owns conservation.

**SEC-014 — Boundary: moderation/administration.** *Confirmed.* Moderation acts on accounts. Administration acts on the platform. Neither writes gameplay state in place.

**SEC-015 — Boundary: evidence/audit.** *Confirmed.* Evidence lives in case records and references spine events. The audit spine records the fact of access and action; it is not a copy of the evidence.

**SEC-016 — Boundary: authentication/authorization.** *Confirmed.* Authentication establishes the session. Authorization evaluates the action, object, role and purpose separately. A valid session is not a permission.

**SEC-017 — Boundary: external integration.** *Confirmed.* An external service receives only the fields its purpose requires. No external service becomes authoritative for a game value, a sanction or an audit record.

**SEC-018 — Accounting identities.** *Confirmed.* The economy's conservation identity remains authoritative. B-12 corrections supply referenced transactions; they do not define a second balance model.

**SEC-019 — Administrative adjustment.** *Confirmed.* An `ADMIN_ADJUSTMENT` is permitted only where a published policy authorizes it, is recorded with a reason and is never used to simulate gameplay or grant a reward.

**SEC-020 — Correction limits.** *Confirmed.* A correction cannot mint value, forgive a debt by editing, or create a negative balance. It restores the lawful state or records a shortfall.

**SEC-021 — Audit protection.** *Confirmed.* The spine's readership, digest chain, verification job and retention are security controls. Their absence is a defect, not a documentation gap.

**SEC-022 — Failure posture per category.** *Confirmed (D-175).* The fifteen postures in §15 govern. No global fail-open or fail-closed answer is permitted.

**SEC-023 — Least destructive action.** *Confirmed.* Where enforcement data is unavailable, the system takes a reversible hold rather than a sanction and never proceeds to a permanent measure on unavailable evidence.

**SEC-024 — Incident classes.** *Confirmed.* Incident classes are active exploitation, service compromise, data exposure, integrity failure and privacy breach. Each declares posture, containment authority, disclosure owner and preservation step.

**SEC-025 — Breach assessment.** *Confirmed.* A suspected personal-data breach is assessed and documented whether or not it is reported onward, including the reasons for not reporting. The assessment is an artefact, not a legal conclusion.

**SEC-026 — Halt over doubtful continuation.** *Confirmed.* Containment that halts the turn pipeline is preferred over continuing to resolve while integrity is doubtful. The halt is disclosed as a delay.

**SEC-027 — No credentials in scope.** *Confirmed.* B-12 never holds, logs, exports or displays a credential, session token, key or secret. Authentication remains Stage 6's.

**SEC-028 — No production access in specification.** *Confirmed.* This prompt inspects implementation files only to identify obligations. It does not change a grant, policy, trigger, migration or runtime permission.

**SEC-029 — Prototype evidence.** *Confirmed.* The Supabase feasibility prototype is evidence of a defect, not a specification. Its observed permissions never authorize a B-12 rule.

**SEC-030 — Security non-claim.** *Confirmed.* No specification statement is evidence that a security control works. Implementation and independent verification remain outstanding.

---

## 14. Supabase and audit-log obligations

**SEC-031 — Profile treasury.** *Confirmed as an open defect.* The feasibility prototype grants `authenticated` a table-wide `UPDATE` on `feasibility.profiles` including `treasury`, with only a row-scoped policy. This is not fixed by this document.

**SEC-032 — Required property.** *Confirmed.* The production design MUST prevent an authenticated player from modifying a server-owned sensitive field, including `treasury`, through any column-, row- or function-level path. The property is column-scoped privilege or a server-mediated write, not a client restriction.

**SEC-033 — Migration obligation.** *Confirmed.* A corrective migration (`0005` equivalent) MUST remove the table-wide update, restrict the writable column set and preserve the legitimate self-service fields. No such migration exists on disk today.

**SEC-034 — SQL permission tests.** *Confirmed.* The production design MUST include SQL permission tests that attempt the prohibited update as the player role, as another player and as the owner row, and assert denial. No `tests/sql/` directory or test source exists today.

**SEC-035 — RLS is not sufficient alone.** *Confirmed.* Row-level security does not constrain a table-wide column grant. The design MUST combine column privilege, policy and transaction-level validation where the platform requires it.

**SEC-036 — Audit trigger absent.** *Confirmed.* The prototype `audit` table has no protective trigger and no delete revocation outside the player role. Append-only is convention, not enforcement.

**SEC-037 — Audit protection requirement.** *Confirmed.* Production MUST prevent update and delete of spine rows outside the recorded correction path; protect the spine from the service role's ordinary path where the platform allows; and record every attempted violation.

**SEC-038 — Tamper-evidence.** *Confirmed.* Production MUST implement the chained digest (`F-FP-012`) and the scheduled verification job (`F-FP-013`). No implementation or executed verification exists.

**SEC-039 — Verification evidence.** *Confirmed.* A gate may claim audit integrity only against an executed verification run, a recorded chain checkpoint and an incident path for failure. A design document is not that evidence.

**SEC-040 — Status disclosure.** *Confirmed.* The corpus MUST keep the profile-permission and audit-protection defects visible in the status surfaces until an implementation and an independent verification close them.

---

## 15. Failure and recovery postures

**FR-001 — Per-category posture.** *Confirmed (D-175).* The fifteen postures are: value write; authorization; audit write; detection service; investigation queue; report intake; notification; aggregate publication; correction; appeal; emergency action; authentication; rate limiter; search/read; export. Each declares its direction in Annex D.

**FR-002 — Fail closed with the transaction.** *Confirmed.* Value writes, authorization decisions, audit writes and correction transactions fail closed. No effect is committed without its record.

**FR-003 — Degrade without blocking play.** *Confirmed.* Detection-service failure degrades detection and never blocks legitimate play. The gap is recorded and backfilled where records survive.

**FR-004 — Withhold publication.** *Confirmed.* Aggregate and informational publication fails closed by withholding the figure, not by publishing an incomplete or inferred one.

**FR-005 — Notification fail-open into digest.** *Confirmed.* Notification delivery failure does not block the action; the notice enters the in-game digest and the delivery failure is recorded.

**FR-006 — Report intake degradation.** *Confirmed.* If intake is unavailable, the player receives a retryable failure and the report is not silently lost. No enforcement action is taken on an unreceived report.

**FR-007 — Investigation degradation.** *Confirmed.* If the investigation queue is unavailable, reversible holds may continue and no permanent measure may be imposed.

**FR-008 — Appeal degradation.** *Confirmed.* If the appeal service is unavailable, the action remains in force, the filing window is extended by the recorded outage in turn boundaries, and no appeal is deemed abandoned.

**FR-009 — Emergency failure.** *Confirmed.* An emergency action that cannot be recorded does not execute. A silent emergency action is prohibited.

**FR-010 — Authentication failure.** *Confirmed.* Authentication failure denies the action. It never falls back to a lower-assurance identity or a shared operator credential.

**FR-011 — Rate-limiter failure.** *Confirmed.* A failed limiter fails closed for value-moving actions and degrades for read-only actions, with the condition recorded.

**FR-012 — Read/search failure.** *Confirmed.* A failed restricted read returns no data. It never falls back to a broader cache or an unfiltered response.

**FR-013 — Export failure.** *Confirmed.* A failed export produces no partial file and no unredacted fallback.

**FR-014 — Correction failure.** *Confirmed.* A correction that cannot complete rolls back exactly and is retried with the same idempotency key.

**FR-015 — Incident review.** *Confirmed.* Every failure that affects integrity, privacy or enforcement is reviewed and recorded, whether or not it changed an outcome.

---

## 16. Cross-system contracts

**INT-001 — Accounts.** *Confirmed.* B-03 owns account state and the lifecycle. B-12 may request a restriction; only B-03 applies it. B-12 never re-parents a nation or changes ownership.

**INT-002 — Enforcement target.** *Confirmed.* Enforcement writes an account-level action. It never expresses a sanction as a nation field or a pair state.

**INT-003 — Economy.** *Confirmed.* B-04 owns every balance. B-12 triggers a correction; the ledger computes and appends it. No administrator writes a balance.

**INT-004 — Cities and research.** *Confirmed.* B-05 owns infrastructure, capacity and research state. B-12 reads for evidence and corrects only through B-05's path.

**INT-005 — Politics.** *Confirmed.* B-06 owns campaign, ballot and political state. A political state is never a sanction (`DMP-267`). An administrative adjustment names the original and may not set `government_id`.

**INT-006 — Markets.** *Confirmed.* B-07 owns market rules and `MKT-S` signals. A signal opens a review; B-12 owns the finding. Gate G-1 requires the incident-rate band B-12 defines structurally.

**INT-007 — Diplomacy.** *Confirmed.* B-08 owns treaty records and breach counts. B-12 may read restricted history under its class; the read is audited.

**INT-008 — Alliances.** *Confirmed.* B-09 owns Alliance rules, tax and contribution data. B-12 owns platform enforcement readership. An officer cannot suspend an account; an Alliance cannot self-adjudicate.

**INT-009 — Warfare.** *Confirmed.* B-10 owns warfare rules, blocks and audit rows. B-12 owns enforcement and penalty policy; B-10 supplies taxonomy and evidence.

**INT-010 — World events and objectives.** *Confirmed.* B-11 owns event, objective and completion state. B-11 flags and records; B-12 owns enforcement, appeals and evidence retention.

**INT-011 — Rankings and progression.** *Confirmed.* B-11 owns snapshots, honours and publication. B-12 enforces standing manipulation and supplies the disclosure class; B-11 keeps `k ≥ 5`.

**INT-012 — Notifications.** *Confirmed.* B-02 owns notice classes and Prompt 13 owns surfaces. B-12 bounds disclosure content.

**INT-013 — Turn engine.** *Confirmed.* B-02 owns phases and the turn ledger. An integrity failure is an incident unless manipulation is evidenced.

**INT-014 — Audit spine.** *Confirmed.* B-02's `TR-090` owns the spine. B-12 owns the event shape, readership and integrity requirement.

**INT-015 — Authentication.** *Confirmed.* Stage 6 owns credentials and sessions. B-12 consumes security events and never holds a credential.

**INT-016 — Network signal.** *Confirmed.* B-03 owns the keyed digest. B-12 uses it for triage and pair review only, within `NET-039`.

**INT-017 — Reporting tooling.** *Confirmed.* B-12 owns report records. Reporter identity is never exposed to the reported party.

**INT-018 — Appeals.** *Confirmed.* B-12 owns the appeal record. An Alliance expulsion appeal stays with `UD-044`.

**INT-019 — Balance and calibration.** *Confirmed.* Prompt 14 owns numeric values. B-12 routes mechanism defects to Prompt 14 and does not call a faucet-sink defect manipulation.

**INT-020 — Interface and owner governance.** *Confirmed.* Prompt 13 owns screens; the owner owns ladder scale, staffing, legal posture and publication. B-12 supplies structure only.

### 16.1 Integration dependency fields

Each contract below states the seven fields Prompt 12B §13 requires. The table is normative; the rule sentences above remain the authority for ownership. No row authorizes implementation.

| Contract | System boundary | Data or authority dependency | Invariant | Security requirement | Ownership | Prompt 12C integration work | Implementation dependency |
|---|---|---|---|---|---|---|---|
| `INT-001` | B-12 ↔ B-03 accounts | Restriction request; account lifecycle state | Only B-03 applies an account restriction | Authenticated actor; audited request | B-03 | Map restriction request/response and failure paths | Stage 5 account-state schema |
| `INT-002` | B-12 ↔ account action record | Enforcement target identifier | A sanction is account-level, never a nation or pair field | No cross-object write | B-12 | Specify the enforcement record shape | Stage 5 enforcement record |
| `INT-003` | B-12 ↔ B-04 economy | Correction instruction; ledger deltas | Ledger computes and appends; no balance typed by an administrator | Reason code; original reference; idempotency | B-04 | Map correction and reversal workflows | Stage 5 ledger and `F-FP-014` test |
| `INT-004` | B-12 ↔ B-05 cities/research | Infrastructure, capacity, research state | Correction only through B-05's path | Purpose-bound read; audit | B-05 | Map evidence read and correction path | Stage 5 B-05 schema |
| `INT-005` | B-12 ↔ B-06 politics | Campaign, ballot, political state | A political state is never a sanction; no `government_id` write | Restricted read; audit | B-06 | Map evidence read boundaries | Stage 5 B-06 schema |
| `INT-006` | B-12 ↔ B-07 markets | Settlement records; `MKT-S` signals | A signal opens review; B-12 owns the finding | No public per-trade feed | B-07 | Map signal-to-review handoff and G-1 band | Stage 5 market records; Prompt 14 band |
| `INT-007` | B-12 ↔ B-08 diplomacy | Treaty records; breach counts | Read-only under class; no treaty edit | Audited restricted read | B-08 | Map restricted-history read | Stage 5 B-08 schema |
| `INT-008` | B-12 ↔ B-09 alliances | Membership, roles, tax/contribution data | An Alliance cannot self-adjudicate or suspend an account | Platform enforcement readership only | B-09 | Map alliance evidence and enforcement boundary | Stage 5 B-09 schema; `UD-046` |
| `INT-009` | B-12 ↔ B-10 warfare | Blocks, results, audit rows | B-10 supplies taxonomy/evidence; B-12 owns penalty policy | No result recomputation | B-10 | Map evidence receipt and enforcement | Stage 5 B-10 records |
| `INT-010` | B-12 ↔ B-11 events/objectives | Event, objective, completion state | B-11 flags; B-12 owns enforcement/appeals/retention | No reward grant by B-12 | B-11 | Map flag-to-case handoff | Stage 5 B-11 records |
| `INT-011` | B-12 ↔ B-11 rankings/progression | Snapshots, honours, publication | B-11 keeps `k ≥ 5`; B-12 supplies disclosure class | No composite headline leak | B-11 | Map standing-manipulation evidence | Stage 5 B-11 snapshots; `UD-050` |
| `INT-012` | B-12 ↔ B-02 notices / Prompt 13 | Notice classes and content bounds | Disclosure content is bounded by class | No third-party enforcement state | B-02 / Prompt 13 | Map notice content rules to surfaces | Prompt 13 surfaces |
| `INT-013` | B-12 ↔ B-02 turn engine | Phases; turn ledger; boundary length | Integrity failure is an incident unless manipulation is evidenced | No silent re-derivation | B-02 | Map incident and delay disclosure | Stage 5 turn engine |
| `INT-014` | B-12 ↔ B-02 audit spine | Event shape; readership; digest chain | Append-only with chained digests and scheduled verification | Restricted readership; read log | B-02 spine / B-12 requirement | Map verification-failure incident path | Stage 5 spine implementation and executed verification |
| `INT-015` | B-12 ↔ Stage 6 authentication | Sessions; security events; step-up | B-12 consumes events, never holds a credential | Step-up; separate revocation | Stage 6 | Map step-up and session-failure paths | Stage 6 auth |
| `INT-016` | B-12 ↔ B-03 network signal | Keyed digest | Triage and pair review only, within `NET-039` | No IP-keyed sanction | B-03 | Map triage-only consumption | Stage 5 digest custody |
| `INT-017` | B-12 reporting tooling | Report records; cluster key | Reporter identity never exposed to reported party | Purpose-bound access | B-12 | Map intake, clustering and duplicate handling | Stage 5 report store; `FP-P13` |
| `INT-018` | B-12 appeals | Appeal record; outcome | One appeal; four outcomes; independence labelled | No method/threshold disclosure | B-12 | Map appeal workflow and remand | Stage 5 appeal record; `UD-059` |
| `INT-019` | B-12 ↔ Prompt 14 balance | Provisional values; mechanism defects | B-12 routes defects; chooses no number | No calibrated claim | Prompt 14 | Map calibration handoff | Prompt 14 |
| `INT-020` | B-12 ↔ Prompt 13 / owner | Screens; ladder scale; staffing; publication | B-12 supplies structure only | Owner-reserved decisions stay open | Prompt 13 / owner | Map surface and governance dependencies | Prompt 13; owner rulings |

---

## 17. Formula and parameter governance

**GOV-001 — Six classifications.** *Confirmed.* Every value is one of: approved authoritative; structurally specified with provisional parameter; research-derived recommendation; owner decision required; legal review required; capacity/implementation validation required.

**GOV-002 — Formula fields.** *Confirmed.* Every formula in the register carries twenty mandatory fields: ID, purpose, inputs, units, expression, variable definitions, constraints, boundary behaviour, rounding, null behaviour, exceptional conditions, dependencies, worked example, verification, parameter status, owner, affected rules, affected requirements, revision, and review trigger.

**GOV-003 — Structure versus value.** *Confirmed.* A complete structural formula does not approve its constants. A provisional constant remains provisional until the named authority approves it.

**GOV-004 — No duplicate formula.** *Confirmed.* A calculation is defined once in the formula register and referenced elsewhere. A second expression is a defect.

**GOV-005 — Rounding.** *Confirmed.* Every formula states rounding, unit and boundary behaviour. Silent truncation is prohibited.

**GOV-006 — Null and missing inputs.** *Confirmed.* A missing required input fails closed or returns an explicit `EX`/hold; it never defaults to zero intent or a permissive value.

**GOV-007 — Parameter register.** *Confirmed.* Each parameter states its current value, classification, source, owner, review trigger and the rule that consumes it.

**GOV-008 — Owner authority.** *Confirmed.* Ladder durations, appeal windows, compensation caps, staffing assumptions and transparency publication are owner-reserved. B-12 structures them and does not choose them.

**GOV-009 — Legal authority.** *Confirmed.* Retention, deletion, age assurance, transfer and breach-reporting conclusions remain `UD-017`, `UD-055` and `UD-060`. B-12 takes the conservative branch.

**GOV-010 — Revision.** *Confirmed.* A formula or parameter change is versioned, dated, justified and propagated to every consumer.

**GOV-011 — No invented number.** *Confirmed.* No numeric value may be presented as approved unless a decision records it. A placeholder is marked provisional and cannot be used as a launch threshold.

**GOV-012 — Calibration.** *Confirmed.* Prompt 14 owns balance calibration. B-12's formulas are structural and its numeric parameters are provisional.

---

## 18. Requirement disposition and decisions

**GOV-013 — Requirement allocation.** *Confirmed (D-186).* The 106 `12A-CR` candidates map one-to-one to `REQ-764`…`REQ-869`. Each is adopted, adapted or merged with a recorded reason; no candidate is silently dropped. Twenty owner/legal-dependent rows are **Open**; eighty-six are **Provisional**.

**GOV-014 — Requirement fields.** *Confirmed.* Every requirement carries the fourteen fields required by Prompt 12B §6. A requirement missing a field is invalid.

**GOV-015 — Decision records.** *Confirmed (D-178…D-187).* Ten B-12 design decisions are recorded in `DECISIONS.md` and mirrored in `04`. Each states issue, alternatives, evidence, rationale, consequences, affected requirements and approval authority. None is owner-approved policy except where it restates an existing owner decision.

**GOV-016 — Unresolved preservation.** *Confirmed.* `UD-017`, `UD-052`…`UD-060`, `UD-040`…`UD-051` and every other open row keep their exact status. B-12 opens no new owner row and closes none.

**GOV-017 — No silent promotion.** *Confirmed.* A provisional recommendation is not an approved rule because it appears in a specification. The status vocabulary remains visible in the requirement register.

**GOV-018 — Traceability.** *Confirmed.* Every rule maps to at least one requirement or to a named decision/inherited rule; every requirement maps to a rule, a formula and an acceptance criterion. The traceability audit is in the requirements register and the acceptance companion.

**GOV-019 — Conflict resolution.** *Confirmed.* A conflict between B-12 and an owning subsystem is resolved in favour of the owning subsystem; B-12 records the conflict and corrects its text. A conflict between two owner decisions is escalated.

**GOV-020 — Prompt 12C boundary.** *Confirmed.* B-12 identifies workflow implications but does not produce journeys, workflow libraries, operational sequences, full edge-case catalogues or 12C acceptance deliverables.

---

## 19. Prompt 12C handoff and non-claims

**GOV-021 — What 12C receives.** *Confirmed.* B-12 supplies the rule set, evidence matrix, role and permission catalogue, privacy classes, sanction ladder, correction model, audit requirements, cross-system contracts, failure postures, formulas and acceptance structure. 12C designs the workflows, journeys and end-to-end acceptance tests.

**GOV-022 — What 12C must not change.** *Confirmed.* 12C may not weaken a rule, close an owner/legal decision, invent a number, promote a provisional parameter or claim runtime verification from a document check.

**GOV-023 — Implementation readiness.** *Confirmed.* B-12 is sufficient to begin 12C workflow design. It is not sufficient for production implementation until the owner/legal dependencies, Stage 5 security work and the audit implementation exist.

**GOV-024 — No runtime claim.** *Confirmed.* No rule, gate or validator in this package proves cheat detection, privacy enforcement, RLS behaviour, moderation capacity, appeal execution, audit integrity or legal compliance.

**GOV-025 — Acceptance status.** *Confirmed.* B-12's acceptance is documentary. The gate register in the acceptance companion states PASS/PARTIAL per criterion and never treats a validator pass as runtime evidence. Prompt 12C is not started and not authorized; this handoff describes what 12C would receive and does not authorize it.

---

## Annex A — Violation classes `V-01`…`V-16`

| ID | Class | Definition | Required elements | Examples | Non-examples | Evidence indicators | Legitimate alternatives | Base severity | Intent | Impact | Enforcement eligibility | Reversal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `V-01` | Multi-account abuse | One person controls more than one account, or uses another account to obtain an advantage | Prohibited account relationship; an advantage or evasion; the accounts are not independent | Sockpuppet voting; alt treasury transfer; alt slot filling | Family members with separate accounts; cooperative allies | Beneficial flow; matched actions; shared declared context; recovery pattern | Shared household; institution; genuine separate players | `T2`–`T3` | Knowledge of the prohibition | Advantage or evasion required | `E2` for restriction; `E3` for suspension | Correct value; close/restrict the account; preserve appeal |
| `V-02` | Account sharing or sale | Giving, selling or transferring control of an account to another person | Transfer of control; benefit or consideration; the account remains active | Selling a nation; sharing credentials for turn coverage | Household assistance under the declared-context rule | Login pattern change; credential change; payment or message evidence | Legitimate recovery; accessibility assistance | `T2`–`T3` | Knowledge | Control transfer required | `E2`–`E3` | Restore owner control; correct transferred value |
| `V-03` | Collusion / manufactured false agency | Presenting a non-independent participant as independent | False agency; coordination; an effect the rules could not produce | Fake participant in a vote; controlled counterparty in a market | Alliance strategy; joint diplomacy; permitted coordination | Matched flows; circular sets; linked timing; shared reward capture | Friends; allies; public coordination | `T2`–`T4` | Knowledge or reckless disregard | Effect on outcome or value | `E3` | Reverse effect; correct value; appeal |
| `V-04` | Match and outcome manipulation | Arranging a result outside the rules | Agreement or control; outcome effect; intended result | Surrender farming; staged war result | Negotiated peace; legitimate surrender under rules | Abnormal outcome sequence; paired actions; communication evidence | Strategic loss; legitimate concession | `T3`–`T4` | Knowledge | Outcome effect required | `E3` | Restore standing/record; correct value |
| `V-05` | Restriction or ban evasion | Acting through another account or route to evade a restriction | Existing restriction; evading act; same controller or coordinated route | New account after suspension; Alliance-bank routing | Legitimate separate account of another person | Restriction record; linked behaviour; route analysis | Shared network without control evidence | `T3`–`T5` | Knowledge | Evasion required | `E3` | Extend restriction; correct value; no automatic permanent measure |
| `V-06` | Unauthorized automation | Automated play obtaining value, eligibility or standing without human intent | Automated process; consequential action; absence of human intent | Scripted turn bot; auto-farming | Accessibility tools; manual macro that only formats | Timing regularity; volume; no human variation | Accessibility; permitted automation | `T2`–`T3` | Knowledge | Material effect or repeated conduct | `E2`–`E3` | Stop automation; correct value; appeal |
| `V-07` | Client or protocol manipulation | Modifying the client, response or protocol to obtain value or information | Modification; effect; unauthorized capability | Injected state; altered response; forged request | Browser zoom; permitted UI extension | Integrity mismatch; impossible request; modified asset | Network latency; legitimate retry | `T3`–`T4` | Knowledge | Security or value effect | `E3` | Invalidate effect; preserve evidence; appeal |
| `V-08` | Economic manipulation | Creating, duplicating or moving value outside the economic rules | Invalid transaction; value effect; no entitlement | Duplicate settlement; wash trade; ledger mismatch | Legitimate arbitrage; negotiated trade | Ledger break; duplicate key; matched flow | Price movement; market strategy | `T2`–`T4` | Knowledge or negligence | Value effect required | `E2` for correction; `E3` for conduct | Correct value; restore ledger; appeal |
| `V-09` | Market manipulation | Distorting a market signal or price to mislead or gain | Artificial signal; intent or effect; market impact | Wash trading; layered orders; false depth | Genuine large order; legitimate exit | `MKT-S` signal; matched flow; order pattern | Legitimate strategy; liquidity provision | `T2`–`T4` | Knowledge | Market or value effect | `E3` | Remove signal effect; correct value; appeal |
| `V-10` | Warfare or objective manipulation | Manufacturing participation or results outside the rules | Invalid participation; effect; coordination or control | Feeding; slot filling; forged acceptance | Legitimate alliance war; coordinated defence | Block records; paired results; participation anomalies | Strategy; permitted coordination | `T2`–`T4` | Knowledge | Outcome or reward effect | `E3` | Reverse record; correct reward; appeal |
| `V-11` | Alliance-finance abuse | Using an Alliance pool or tax to evade a restriction or conceal a flow | Restricted flow; Alliance route; concealment or evasion | Bank-routed transfer; tax laundering | Legitimate Alliance finance under `UD-046` | Contribution/tax records; flow graph | Authorized treasury use | `T2`–`T4` | Knowledge | Value or evasion effect | `E3` | Correct value; preserve audit; appeal |
| `V-12` | Exploit or bug abuse | Using a defect to obtain an impermissible effect | Defect; use; effect | Duplicate reward; race exploit; failure exploit | Honest report; accidental trigger disclosed | Impossible state; duplicate; error log | Legitimate use of a published rule | `T1`–`T4` | Knowledge or reckless disregard | Effect required | `E2` correction; `E3` conduct | Fix defect; correct value; appeal |
| `V-13` | Unauthorized information access | Obtaining restricted state without entitlement | Restricted field; access or inference; absence of entitlement | Scraping; response reconstruction; hidden-state read | Public aggregate; permitted shared view | Read anomalies; response diff; enumeration | Legitimate public data | `T2`–`T4` | Knowledge | Privacy or competitive effect | `E2`–`E3` | Stop access; notify; preserve evidence |
| `V-14` | Rate, quota or limit circumvention | Exceeding a declared allowance through a prohibited route | Declared limit; circumventing route; excess use | Multi-session flood; data-centre rotation | Legitimate retry; permitted concurrency | Counter spread; timing; account set | Network retry; normal burst | `T1`–`T3` | Knowledge | Resource or fairness effect | `E2`–`E3` | Rate limit; no value correction unless value moved |
| `V-15` | False report, retaliation or reversal abuse | Knowingly false report, retaliation, or fabricated evidence/correction | Falsehood or retaliation; intent; effect | Brigading; revenge report; forged correction | Good-faith unsubstantiated report | Report pattern; relationship; contradictory evidence | Honest mistake; genuine concern | `T1`–`T4` | Knowledge | Harm or procedural effect | `E3` | Withdraw false record; restore wrongly affected state |
| `V-16` | Administrative or evidence misconduct | Privileged act outside purpose, or tampering with evidence/audit | Privileged capability; prohibited purpose or tampering; effect | Self-dealing; audit edit; evidence deletion | Recorded correction under authority | Audit gap; permission mismatch; changed record | Authorized emergency action | `T4`–`T5` | Knowledge | Trust, value or privacy effect | `E3` plus independent review | Reverse action; preserve evidence; incident review |

---

## Annex B — Privacy classes and actor permissions

| Class | Handling | Subject visibility | Purpose | Authorised viewers | Authorised modifiers | Export | Retention dependency | Security requirement |
|---|---|---|---|---|---|---|---|---|
| `PUB` | Public | Public | Published game facts | Anyone | Owning subsystem | Permitted | Public history | Integrity only |
| `PLAYER` | Private | Participant/Private | Player's own and published player state | Subject; permitted players | Subject through gameplay | Subject request | `D-026` | Authentication |
| `ALLIANCE` | Restricted | Alliance | Alliance operations | Alliance members under B-09 | Alliance roles under B-09 | Alliance officer, purpose-bound | `D-026` / `UD-046` | Role check; audit |
| `OPS` | Restricted | Operational | Operations and turn health | Operators | Operators under change control | Purpose-bound | Operational window | Audit; least privilege |
| `MOD` | Restricted | Moderation | Cases, reports, decisions | Assigned moderator; appeals; audit | Case append only | Appeals reviewer only | `UD-055` | Audit; segregation |
| `PERSONAL` | Restricted/Secret | Private | Account and contact data | Subject; Stage 6 auth; legal role | Subject; Stage 6 | Subject request; legal obligation | `UD-017` | Encryption; access log |
| `SEC` | Secret | Security | Credentials, keys, detection internals | Security administrator; audit | Security administrator | Prohibited | Security window | Secret custody; no log |
| `AUDIT` | Restricted | Audit | Spine and case integrity | Audit role; purpose-bound reviewer | Append-only | Audit only | Permanent / `D-026` | Chain; read log |
| `LEGAL` | Restricted | Legal | Holds, obligations, assessments | Owner; counsel; audit | Counsel only | Legal only | `UD-017` / `UD-055` | Segregated access |

**Actor/action matrix.** `V` view, `S` search, `X` export, `M` modify, `D` delete, `Dc` disclose.

| Actor | PUB | PLAYER | ALLIANCE | OPS | MOD | PERSONAL | SEC | AUDIT | LEGAL |
|---|---|---|---|---|---|---|---|---|---|
| Player | V | V own | V member | — | — | V own | — | — | — |
| Alliance personnel | V | V published | V/S | — | — | V own | — | — | — |
| Moderator | V | V case | V case | — | V/S | V bounded | — | — | — |
| Appeals reviewer | V | V case | V case | — | V | V bounded | — | V case | — |
| Investigator | V | V case | V case | V | V/S | V bounded | — | V case | — |
| Administrator | V | V purpose | V purpose | V/S | V purpose | V purpose | — | V purpose | — |
| Operator/emergency | V | V purpose | V purpose | V/S/M | V purpose | V purpose | V/M | V purpose | — |
| Audit reviewer | V | V audit | V audit | V audit | V audit | V audit | V audit | V/S/X | V audit |

No actor holds `X`, `D` or `Dc` by default except the audit role for `AUDIT` export; every exception is a separate permission, purpose-bound and logged.

---

## Annex C — Role catalogue

| Role | Responsibilities | Permitted | Prohibited | Read | Write | Approval | Separation | Audit | Delegation | Escalation | Revocation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `R-MOD` | Intake, triage, `T0`–`T2`, case notes | View assigned `MOD`; warn; restrict ≤ `T2` | Sanction `T3`+; export; edit state; self-case | `MOD`, bounded `PLAYER` | Case append | None below `T2` | Cannot decide own case | Every action | Case-scoped only | To `R-SMOD` | On role end/conflict |
| `R-SMOD` | `T3`, review, moderator oversight | `T3`; approve `T2` extension; review | `T4`/`T5`; audit edit; state edit | `MOD` | Case append; restriction | Second review where possible | Cannot appeal own case | Every action | Case-scoped | To owner/`R-APL` | On role end |
| `R-APL` | Appeals | Uphold/reduce/reverse/remand | Investigate; new sanction; edit original | Case + bounded evidence | Appeal record | Independent where possible | Cannot review own decision | Every action | None | To owner | After appeal |
| `R-INV` | Investigation | Open case; preserve; recommend | Decide sanction/appeal; edit state | `MOD`, `SEC` need-to-know | Case append | Recommendation only | Cannot decide | Every action | Case-scoped | To `R-SMOD` | On case close |
| `R-SEC` | Security admin | Sessions, keys, permission map, containment | Game value; audit edit; sanction | `SEC`, `OPS`, `AUDIT` | Security config | Change record | Cannot self-grant | Every action | Incident-scoped | To owner | On incident end |
| `R-OPS` | Technical operations | Run turn; deploy; infra | Private player data outside incident; audit edit | `OPS` | Infra config | Change control | Cannot publish alone | Every action | Incident-scoped | To `R-SEC` | On shift end |
| `R-AUD` | Integrity review | Read/verify spine; report | Alter spine; decide case; grant | `AUDIT`, `MOD`, `SEC` summary | Verification record | None | Independent | Every action | None | To owner | On role end |
| `R-EMG` | Emergency containment | Freeze/suspend/preserve | Permanent action; delete; transfer; audit edit | Incident scope | Emergency record | Review after | Cannot review own action | Every action | Incident-only | To owner | On expiry |

---

## Annex D — Fifteen failure postures

| ID | Category | Posture |
|---|---|---|
| `FR-01` | Value write | Fail closed with transaction |
| `FR-02` | Authorization | Fail closed; deny |
| `FR-03` | Audit write | Fail closed with transaction |
| `FR-04` | Detection service | Degrade; record gap; no play block |
| `FR-05` | Investigation queue | Holds allowed; no permanent measure |
| `FR-06` | Report intake | Retryable failure; no silent loss |
| `FR-07` | Notification | Fail open into digest; record |
| `FR-08` | Aggregate publication | Withhold figure |
| `FR-09` | Correction | Roll back; retry same key |
| `FR-10` | Appeal | Action stands; window extended by outage |
| `FR-11` | Emergency action | No record, no action |
| `FR-12` | Authentication | Deny; no fallback |
| `FR-13` | Rate limiter | Fail closed for value; degrade reads |
| `FR-14` | Restricted read/search | Return no data |
| `FR-15` | Export | No partial or unredacted file |

---

## Annex E — Rule inventory and source map

| Prefix | Range | Rules | Section | Subject |
|---|---|---|---|---|
| `FP-` | 001–035 | 35 | §1–§3 | Purpose, evidence terminology, fair-play foundations and the violation taxonomy |
| `EVD-` | 001–042 | 42 | §2, §6, §11 | Evidence states, investigation, sufficiency and evidence lifecycle |
| `MA-` | 001–012 | 12 | §4 | Accounts, shared context and multi-account policy |
| `CO-` | 001–010 | 10 | §4 | Collusion and coordination |
| `EX-` | 001–012 | 12 | §5 | Exploitation and automation |
| `PRV-` | 001–025 | 25 | §7 | Privacy classification, permission and disclosure |
| `MOD-` | 001–060 | 60 | §8–§9 | Moderation powers, sanctions, corrections and appeals |
| `ADM-` | 001–030 | 30 | §10 | Administrative roles, permissions and separation of duties |
| `COR-` | 001–018 | 18 | §12 | Correction, reversal, compensation and recovery |
| `SEC-` | 001–040 | 40 | §13–§14 | Anti-exploit controls, security and accounting boundaries, Supabase and audit obligations |
| `INT-` | 001–020 | 20 | §16 | Cross-system contracts and ownership boundaries |
| `FR-` | 001–015 | 15 | §15 | Failure and recovery postures |
| `GOV-` | 001–025 | 25 | §17–§19 | Formula governance, requirement disposition, Prompt 12C handoff |

**Requirement linkage.** There is no prefix-to-`REQ-` range mapping. Global requirement identifiers follow the order of the 106 `12A-CR` candidates, and each requirement names the structural rules it depends on; a single rule is therefore cited by several requirements and a single requirement cites rules from more than one prefix. The authoritative rule-to-requirement and requirement-to-rule links are held in the [B-12 requirement register](20_fair_play_and_player_protection_requirements.md) §2–§3.

**Counts.** 344 normative rules across thirteen prefixes (`FP` 35, `EVD` 42, `MA` 12, `CO` 10, `EX` 12, `PRV` 25, `MOD` 60, `ADM` 30, `COR` 18, `SEC` 40, `INT` 20, `FR` 15, `GOV` 25). Annex A defines 16 violation classes. Annex B defines 9 privacy classes, 8 actor classes and 6 actions. Annex C defines 8 administrative roles. Annex D defines 15 failure postures. No rule in this document is implemented, tested or independently verified.