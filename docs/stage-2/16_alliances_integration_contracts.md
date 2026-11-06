# B-09 Alliances — Cross-System Integration Contracts

**Version:** 2.8 • **Created:** 2026-10-31 • **Updated:** 2026-11-03 • **Stage 2, Prompt 09B-M** • **Integration Contracts Ledger (Correction Candidate)**
**Status:** **Phase 09B Alliance specification and documentation: ACCEPTED. Accepted at the specification/documentation level (D-142 / DD-165).** Acceptance is not production implementation, live-game integration testing, release or operational readiness, and it authorizes no new capability and resolves no unresolved decision. **Prompt 09C is registered next with canonical deliverable `docs/stage-2/16_alliances_workflows_acceptance.md` but has not started.** **Prompt 09B-M records the operational-funding boundary under `D-141` and states that no AOP purpose is currently spendable because no cost schedule is approved.** The contracts describe candidate interfaces; nothing here is implemented, runtime-tested, balanced, or release-approved.
**Parent task:** Stage 2, **Prompt 09 — Alliances and Coalitions**. This document is the canonical **Integration Contracts Ledger** for **Prompt 09B** (corrected under Prompt 09B-E, authority-audited under Prompt 09B-F, clarified under Prompt 09B-J, completed under Prompt 09B-K, reconciled with operational funding under Prompt 09B-L and re-verified under Prompt 09B-M), reconciling all 30 `AX-` records: `AX-01` through `AX-26` as originally defined in accepted Prompt 09A research, plus `AX-27` through `AX-30` added by Prompt 09B-I under the owner authorization `D-140`.
**Evidence base:** Research integration matrix [`research/09A_alliance_integration_matrix.md`](research/09A_alliance_integration_matrix.md) v1.4, research report [`research/09A_alliance_research.md`](research/09A_alliance_research.md) v1.4, source register [`research/09A_alliance_sources_findings.md`](research/09A_alliance_sources_findings.md) v1.1, and canonical rulebooks B-01 through B-08.
**Traceability:** Every integration contract links explicit external subsystem rules (`TR-`, `ACC-`, `ECN-`, `CIT-`, `DMP-`, `MKT-`, `DIP-`), alliance rules (`ALL-###`), requirement IDs (`REQ-###`), decision records (`D-###`, `DD-###`), and formula IDs (`F-AL-###`).
**Reconciliation Notice:** Under Prompt 09B-E, `UD-039` is recorded as resolved by `D-137` (no national diplomatic delegation for alliances). Under Prompt 09B-I, `D-140` narrowly amends `D-137` by authorizing a **separate** Alliance-to-Alliance treaty object; zero delegation remains binding (`ALL-196`, `ALL-217`). Under Prompt 09B-J, `D-140` is clarified: member tax is automatic per-turn collection from **current-turn production only**, with player-created brackets, separate Crowns and resource rates, role-based permissions and a then-credit-only Alliance Receiving Ledger (superseded by the 09B-L four-category receipt/accounting record with one purpose-limited operational debit); no per-policy owner consent is required. Under Prompt 09B-K, `AX-27` adds the provisional `UD-040` attribution safeguard (at most one deduction per eligible production event, never more than 100% of gross, no Alliance priority, visible recorded 0% fallback on unresolved ambiguous attribution) and the rule that later same-turn stages consume only post-tax net; `AX-28` states the `ALF-24` rejection set without a capacity limit; `REQ-626` names the Alliance Receiving Ledger. Under Prompt 09B-L, `AX-27` extends to the ARL's `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` accounting and the purpose-limited operational expense (`ALL-220`–`ALL-226`, `F-AL-008`, `ALF-27`–`ALF-29`, `AUD-AL-019`); `AX-28` distinguishes donation credit from the only permitted operational debit; and `AX-29` registers `AT-E00` record-only versus `AT-E01` NAP. `UD-045` retains only the narrow tax-management partial authorization; `UD-046` retains ownership, custody, capacity, general withdrawal, general spending, distributions and dual approval. Treaty coverage is a recorded consenting set and a non-consenting nation is admitted as a **non-covered member**, never refused. Only structured effects execute; custom prose never does. Owner decisions `UD-040` through `UD-049` remain **Open** awaiting explicit owner approval; no contract field may convert a candidate into a rule. An `AX` field marked **approved** cites an owner-approved boundary; a field marked **candidate** creates no right, cost, capacity, threshold, office, or workflow. `AX-08` asserts only that national warehouse limits do not establish alliance-pool capacity; it does not assert that a pool or a capacity value exists. The Alliance Receiving Ledger is a receipt record, not an ownership or capacity model; `UD-046` remains Open.

---

## 1. System Integration Principles and Architecture

The Alliance System is an organizational superstructure built on top of the sovereign nation-state model of Nation Supremacy. It does not replace, duplicate, or compromise the integrity of existing subsystems:

1. **Subsystem Authority:** The underlying subsystem (Account, Economy, Cities, Markets, Diplomacy, Military) remains the exclusive authority for its own state mutations.
2. **National Sovereignty:** An alliance leader, officer, or majority vote cannot compel a sovereign nation owner to perform unconsented diplomatic, economic, or military actions (`B-08`, `ALL-004`). Silence never constitutes consent; alliance majorities do not bind sovereign nations.
3. **Resource Conservation (binding inherited constraint, provisional requirement):** Any alliance value-holding mechanism must conserve value, cannot mint resources, and must be audited (`REQ-176`, `ECN-213`). Whether a pool exists, who owns it, and what capacity it has are unresolved under `UD-046`; this document establishes no ownership (`D-136`, `DD-157`).
4. **Treasury Capacity Isolation (boundary only):** National warehouse capacity rules (`REQ-141`, `REQ-142`) do not establish or govern alliance pool capacity (`AX-08`). No dedicated capacity, member bonus, overflow rule, withdrawal workflow, signature requirement, or threshold is approved; each is a candidate under `UD-046`, calibrated only if approved, in Prompt 14.
5. **Market Gate Integrity:** Global Trade operates under the approved release gates (`G-1` through `G-6`, `D-122`, `DD-136`). Alliance systems create no backdoors, fee bypasses, or shadow market channels (`AX-26`).
6. **Turn Lattice Synchronization:** All cross-system transactions resolve at the two-hour turn lattice boundary defined in `TR-024` (slot arithmetic) and `TR-029` (boundary assignment).

---

## 2. AX-01 through AX-30 Reconciliation Matrix

The table below reconciles `AX-01`–`AX-26` against their original Prompt 09A definitions and records `AX-27`–`AX-30` as new Prompt 09B-I contracts, documenting the corrective restoration applied under Prompt 09B-C, re-verified under Prompts 09B-E and 09B-F, and clarified under Prompt 09B-J. **"Reconciled & Restored" in the final column means the contract identity and scope were restored; it is not an approval status.** The status of each contract is stated in §3, where `UD-040`–`UD-049` remain Open and no deferred or candidate contract is binding.

| Contract ID | Original Prompt 09A Definition | Prior Defective 09B Definition | Correction Required & Applied | Final Status |
|---|---|---|---|---|
| **AX-01** | Alliance founding requires an eligible nation owner | Alliance Founding and Nation Owner Eligibility | Restored exact Prompt 09A scope: active nation eligibility and founder contact bootstrap; single-alliance and fee are candidate under `UD-040` | Reconciled & Restored |
| **AX-02** | One-player-one-nation and multi-identity limits apply to alliance roles | Single-Alliance Invariant and Identity Enforcement | Restored Prompt 09A identity: one-player-one-nation applied to roles (REQ-061, REQ-043, REQ-004; UD-045) | Reconciled & Restored |
| **AX-03** | Dormant or retired founder/leader does not freeze alliance | Founder / Leader Dormancy and Succession Integration | Restored Prompt 09A identity: consumes D-028 dormancy (168 turns) and REQ-085 reroll cleanup (UD-043) | Reconciled & Restored |
| **AX-04** | Leadership, succession and office vacancy | Leadership Appointment, Resignation, and Removal | Restored Prompt 09A identity: office vacancy and succession framework; `UD-012` resolved structurally by B-09, policy Open under `UD-043` | Reconciled & Restored |
| **AX-05** | Permission changes and role grants | Permission Modification and Role Escalation Guards | Restored Prompt 09A identity: capability catalogue, anti-escalation controls, least-privilege enforcement (UD-045) | Reconciled & Restored |
| **AX-06** | Treasury deposits of already-owned resources | Alliance Treasury Pool Isolation and Conservation (Shifted) | **CRITICAL FIX:** Restored AX-06 as Treasury deposits of already-owned resources (REQ-176, REQ-005, REQ-154, REQ-170; UD-046) | Reconciled & Restored |
| **AX-07** | Treasury withdrawals, grants and loans | Voluntary Resource Contributions and Deposits (Shifted) | **CRITICAL FIX:** Restored AX-07 as Treasury withdrawals, grants and loans (REQ-013, REQ-176, REQ-005, REQ-153; UD-046) | Reconciled & Restored |
| **AX-08** | Alliance resource storage limits | Alliance Treasury Dedicated Storage Limits and Deposit Policies | **CRITICAL FIX:** Restored AX-08 canonical scope: national warehouse limits (REQ-141/142) do not establish pool capacity; UD-046 governs | Reconciled & Restored |
| **AX-09** | Applications, acceptance, rejection and withdrawal | Treasury Withdrawals, Disbursements, and Multi-Sig (Shifted) | **CRITICAL FIX:** Restored AX-09 as Applications, acceptance, rejection and withdrawal (REQ-002, REQ-562-570; UD-044) | Reconciled & Restored |
| **AX-10** | Field-level visibility of profile and applicant data | Membership Application, Review, and Roster Lifecycle (Shifted) | **CRITICAL FIX:** Restored AX-10 as Field-level visibility of profile and applicant data (REQ-057; UD-044) | Reconciled & Restored |
| **AX-11** | City/development support programmes | Field-Level Privacy and Profile Data Classification (Shifted) | **CRITICAL FIX:** Restored AX-11 as City/development support programmes (REQ-172, REQ-218, REQ-005; UD-046) | Reconciled & Restored |
| **AX-12** | Readiness/activity declarations for members | Non-Repayable Development Grants and Aid Programs (Shifted) | **CRITICAL FIX:** Restored AX-12 as Readiness/activity declarations for members (REQ-091, REQ-023; UD-044/UD-049) | Reconciled & Restored |
| **AX-13** | Population/approval effects of alliance membership | Opt-In Member Readiness and Activity Overview (Shifted) | **CRITICAL FIX:** Restored AX-13 as Population/approval effects of alliance membership (Deferred) | Reconciled & Restored |
| **AX-14** | Elections/crisis interaction with alliance offices | Population and Domestic Approval Non-Interference (Shifted) | **CRITICAL FIX:** Restored AX-14 as Elections/crisis interaction with alliance offices (REQ-326; Deferred) | Reconciled & Restored |
| **AX-15** | National treaties persist through alliance join/leave/removal | Domestic Elections and Crisis Independence (Shifted) | **CRITICAL FIX:** Restored AX-15 as National treaties persist through alliance join/leave/removal (REQ-530, DIP-147) | Reconciled & Restored |
| **AX-16** | Alliance diplomatic positions (non-binding) | Persistence of Bilateral Treaties Across Membership (Shifted) | **CRITICAL FIX:** Restored AX-16 as Alliance diplomatic positions (non-binding) (REQ-579, REQ-580; UD-039 resolved by D-137; positions Open under UD-047) | Reconciled & Restored |
| **AX-17** | Embargo and restricted-pair checks on alliance transfers | Non-Binding Collective Alliance Diplomatic Stances (Shifted) | **CRITICAL FIX:** Restored AX-17 as Embargo and restricted-pair checks on alliance transfers (REQ-529, REQ-175, REQ-576) | Reconciled & Restored |
| **AX-18** | War/coordination information | Bilateral Embargo Enforcement on Treasury Transfers (Shifted) | **CRITICAL FIX:** Restored AX-18 as War/coordination information (REQ-014, REQ-518; Deferred to Prompt 10) | Reconciled & Restored |
| **AX-19** | Static Discord invite link | Military Coordination and Command Sovereignty (Shifted) | **CRITICAL FIX:** Restored AX-19 as Static Discord invite link (D-133, DD-147, DD-148, REQ-057; UD-048) | Reconciled & Restored |
| **AX-20** | Announcements and formal notices | Static External Discord URL Integration (Shifted) | **CRITICAL FIX:** Restored AX-20 as Announcements and formal notices (REQ-057, REQ-021, REQ-586, REQ-606; UD-049) | Reconciled & Restored |
| **AX-21** | Audit and history of alliance actions | Asynchronous Official Bulletins and Notifications (Shifted) | **CRITICAL FIX:** Restored AX-21 as Audit and history of alliance actions (REQ-027, REQ-021, REQ-153, D-026) | Reconciled & Restored |
| **AX-22** | Rankings/chronicle aggregates | Immutable Audit Logging of Alliance Events (Shifted) | **CRITICAL FIX:** Restored AX-22 as Rankings/chronicle aggregates (REQ-058; Deferred to Prompt 11) | Reconciled & Restored |
| **AX-23** | Fair-play/moderation of alliance conduct | Chronicle Aggregates and Future Alliance Rankings (Shifted) | **CRITICAL FIX:** Restored AX-23 as Fair-play/moderation of alliance conduct (REQ-025, REQ-026, REQ-027; Deferred to Prompt 12) | Reconciled & Restored |
| **AX-24** | Notifications and UI surfaces | Fair-Play Reporting and Moderation Boundary (Shifted/Omitted) | **CRITICAL FIX:** Restored AX-24 as Notifications and UI surfaces (REQ-020; Deferred to Prompt 13) | Reconciled & Restored |
| **AX-25** | Formula and balance registration | Alliance Formula Registration and Calibration Authority | Restored exact Prompt 09A scope: authoritative formula registration (REQ-163, D-064; Deferred to Prompt 14) | Reconciled & Restored |
| **AX-26** | Global Trade interaction | Global Trade Independence and Market Gate Preservation | Restored exact Prompt 09A scope: Global Trade independence, gate integrity (D-122, DD-136, REQ-513, G-1..G-6) | Reconciled & Restored |
| **AX-27** | New Prompt 09B-I contract; clarified Prompt 09B-J/09B-K; reconciled Prompt 09B-L | — | Automatic per-turn tax on current-turn production only; player-created versioned **per-Alliance** brackets, separate Crowns and resource rates 0–100%, role permissions, frozen cutoff, 0% fallback, ARL receipt/accounting in four categories; no per-policy owner consent; at most one deduction per eligible production event, never more than 100% of gross, no Alliance priority, visible recorded 0% fallback for ambiguous multiple-membership attribution, later same-turn stages consume only post-tax net; narrow purpose-limited operational expense to a registered platform cost sink with no general withdrawal or player distribution; no cost schedule is approved, so no purpose is currently spendable (D-140/D-141, DD-161, DD-164, REQ-618..625/648..653, ALL-179..187/220..226, F-AL-006/008) | New Contract — Binding Owner-Authorized Constraint |
| **AX-28** | New Prompt 09B-I contract; clarified Prompt 09B-J/09B-K; reconciled Prompt 09B-L | — | Owner-authorized voluntary donations; canonical transfer, ARL `RECEIVED`/`AVAILABLE` credit with no capacity assumption, receipts, idempotency, no general withdrawal authority and no player payment; the ALF-24 rejection set has no destination-capacity limit (D-140, DD-161, REQ-626..632, ALL-188..195, F-AL-007) | New Contract — Binding Owner-Authorized Constraint |
| **AX-29** | New Prompt 09B-I contract; clarified Prompt 09B-J; reconciled Prompt 09B-L | — | Separate Alliance-to-Alliance treaty object with AT-T01..AT-T05 and registered effects AT-E00 record-only / AT-E01 NAP, recorded per-nation consent, non-covered membership, structured effects only; AT-T01 cannot be record-only; no B-08 reuse, no delegation, dissolution ends the bilateral treaty whole (D-140, DD-162, REQ-633..644, ALL-196..208) | New Contract — Binding Owner-Authorized Constraint |
| **AX-30** | New Prompt 09B-I contract; clarified Prompt 09B-J; reconciled Prompt 09B-L | — | Same-Alliance ban and active `AT-E01` NAP checked independently and cumulatively in one server-side attack validator on every entry point; AT-E00 supplies no coverage; mandatory block audit `AUD-AL-017`; Prompt 10 dependency (D-140, DD-163, REQ-642/645..647, ALL-206/209..215) | New Contract — Binding Design Contract |

---

## 3. Master Integration Ledger (AX-01 through AX-30)

### AX-01 — Alliance Founding Requires an Eligible Nation Owner

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-01` |
| **Integration Title** | Alliance Founding Requires an Eligible Nation Owner |
| **Alliance Capability** | Create a new alliance entity; founding nation becomes initial primary administrative contact |
| **Owning Subsystem** | Nation & Account Systems (`B-01` / `B-03`) |
| **Canonical External Rule** | `ACC-001`, `TR-060`, `ECN-212` |
| **Alliance Internal Rule** | `ALL-011`, `ALL-012`, `ALL-015` |
| **Relevant REQ IDs** | `REQ-002` (DIRECT), `REQ-061` (DIRECT), `REQ-076` (RELATED), `REQ-534`, `REQ-535` |
| **Related Decision IDs** | `D-138`, `DD-151`, `UD-040` |
| **Related Formula IDs** | `F-AL-002` (Founding Fee) |
| **Inputs Received** | Founding player account credentials, authenticated nation ID, nation account status, liquid crowns balance |
| **Outputs Provided** | Newly created Alliance Record (`ALLIANCE_ID`, status `ACTIVE`), administrative root contact assignment record |
| **State Ownership** | Account/Nation owns player identity and eligibility; Alliance owns alliance metadata and administrative role assignment |
| **Authorized Actors** | Authenticated sovereign player nation owner |
| **Permission Requirement** | None (public action available to unaffiliated eligible nation owners) |
| **National Player Consent** | Mandatory explicit consent (player signs founding action with credentials/confirmation) |
| **Resource Impact** | Candidate only: if a founding fee is approved under `UD-040`, `F-AL-002` would debit an illustrative 100,000 crowns atomically. No fee, amount or charge is in force |
| **Security Boundary** | Account verification; any anti-sybil founding control, single-alliance restriction and tag uniqueness are candidate under `UD-040` and currently unenforced. Founding creates no authority over another nation and no tax, treasury or operational-funding power; those are separate rules (`ALL-006`, `ALL-179`–`ALL-187`, `ALL-220`–`ALL-226`) |
| **Failure Behaviour** | Rejection if the account is banned or ineligible. If a single-alliance rule is ever approved under `UD-040`, an affiliated nation would be rejected (`REQ-566`); if a fee is approved, insufficient crowns would reject the act (`ALF-05`). Neither rule is in force |
| **Recovery Responsibility** | Alliance System aborts transaction; zero crowns debited; player notified |
| **Unresolved Decision** | `UD-040` (Founding fee policy, eligibility rules, and single-alliance invariant are candidate proposals awaiting explicit owner decision `UD-040`; 100k crowns provisional baseline under Category C / Prompt 14) |
| **Status** | **Candidate Proposal; Open under UD-040 awaiting Owner decision; 100k Crowns Provisional** |

---

### AX-02 — One-Player-One-Nation and Multi-Identity Limits Apply to Alliance Roles

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-02` |
| **Integration Title** | One-Player-One-Nation and Multi-Identity Limits Apply to Alliance Roles |
| **Alliance Capability** | Assign roles, offices, and governance authority only to verified, eligible sovereign nation owners |
| **Owning Subsystem** | Nation & Identity Systems (`B-01` / `B-03`) |
| **Canonical External Rule** | `ACC-001`, `ACC-004`, `REQ-061`, `REQ-043`, `REQ-004`, `REQ-031` |
| **Alliance Internal Rule** | `ALL-059`, `ALL-061`, `ALL-062`, `ALL-080` |
| **Relevant REQ IDs** | `REQ-061` (DIRECT), `REQ-043` (DIRECT), `REQ-004` (DIRECT), `REQ-031` (RELATED), `REQ-552`–`REQ-561` |
| **Related Decision IDs** | `D-138`, `D-139`, `DD-153`, `DD-155`, `UD-045` |
| **Related Formula IDs** | None |
| **Inputs Received** | Actor account ID, nation ID, proposed target member nation ID, role/position assignment payload |
| **Outputs Provided** | Validated role assignment record, audit log entry (`AUD-AL-003`) |
| **State Ownership** | Account owns one-player-one-nation policy; Alliance owns position assignments |
| **Authorized Actors** | Alliance officer holding `MANAGE_ROLES` permission |
| **Permission Requirement** | `MANAGE_ROLES` |
| **National Player Consent** | Implicit via membership acceptance; explicit confirmation for executive transfer |
| **Resource Impact** | None |
| **Security Boundary** | Multi-identity prevention; sybil detection; roles cannot be assigned to bots or secondary accounts |
| **Failure Behaviour** | Rejection if actor or target nation violates single-nation or single-account rules (`ALF-08`) |
| **Recovery Responsibility** | Action rejected cleanly; state unmodified; security audit logged |
| **Unresolved Decision** | `UD-045` (Capability catalogue and role assignment limits awaiting explicit owner decision `UD-045`) |
| **Status** | **Candidate Role Architecture; Open under UD-045 awaiting Owner decision** |

---

### AX-03 — Dormant or Retired Founder/Leader Does Not Freeze Alliance

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-03` |
| **Integration Title** | Dormant or Retired Founder/Leader Does Not Freeze Alliance |
| **Alliance Capability** | Receive nation dormancy, reroll and retirement events and record office status; any vacancy, caretaker or succession action is candidate under `UD-043` and executes only if an approved policy exists |
| **Owning Subsystem** | Nation & Account Lifecycle (`B-03`) |
| **Canonical External Rule** | `B-03` § 9 / § 13, `D-028`, `REQ-091`, `REQ-085` |
| **Alliance Internal Rule** | `ALL-053`, `ALL-054`, `ALL-055`, `ALL-058` |
| **Relevant REQ IDs** | `REQ-091` (DIRECT), `REQ-085` (DIRECT), `REQ-013` (RELATED), `REQ-548` |
| **Related Decision IDs** | `D-028`, `D-138`, `DD-154`, `UD-043` |
| **Related Formula IDs** | `F-AL-003` (Administrative Inactivity Window) |
| **Inputs Received** | Account dormancy notice, nation reroll event, nation retirement/deletion event |
| **Outputs Provided** | Dormancy or lifecycle notice to the alliance and an audit record; no office, authority or seat transfers automatically. A candidate vacancy or succession event exists only if `UD-043` approves one |
| **State Ownership** | Nation owns lifecycle states; Alliance owns office assignments. No lifecycle event transfers alliance authority by itself |
| **Authorized Actors** | System records the event only. Any future automatic vacancy or succession process would require an owner-approved policy under `UD-043` |
| **Permission Requirement** | None while `UD-043` is Open; no system process may vacate an office, appoint a steward or transfer authority |
| **National Player Consent** | Not applicable to event recording. Any future automatic succession requires an owner-approved policy and cannot transfer national sovereignty |
| **Resource Impact** | None |
| **Security Boundary** | Preserves evidence of administrative inactivity and prevents the platform from inventing a succession outcome |
| **Failure Behaviour** | If every member is inactive, no automatic dissolution or abandonment transition occurs; a candidate abandoned-state review remains under `ALL-150` and `UD-043` |
| **Recovery Responsibility** | Event recorded; no fallback stewardship, caretaker appointment or dissolution executes |
| **Unresolved Decision** | `UD-043` (Succession thresholds and vacancy handling awaiting explicit owner decision; D-028 168-turn account dormancy lattice is a confirmed constraint; no automatic authority transfer is in force) |
| **Status** | **Candidate Succession Safeguards; Open under UD-043 awaiting Owner decision; F-AL-003 Provisional** |

---

### AX-04 — Leadership, Succession and Office Vacancy

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-04` |
| **Integration Title** | Leadership, Succession and Office Vacancy |
| **Alliance Capability** | Define offices, voluntary executive transfer and resignation under the alliance's own constitution; any succession or vacancy rule is candidate under `UD-043` |
| **Owning Subsystem** | Alliance Governance (`B-09`) + B-03 Lifecycle Interface |
| **Canonical External Rule** | `REQ-013` (DIRECT), `REQ-085` (DIRECT), `REQ-091` (RELATED), `DIP-146`, `D-028` |
| **Alliance Internal Rule** | `ALL-051`, `ALL-052`, `ALL-053`, `ALL-054`, `ALL-055`, `ALL-056`, `ALL-057`, `ALL-058` |
| **Relevant REQ IDs** | `REQ-013`, `REQ-085`, `REQ-091`, `REQ-542`–`REQ-551` |
| **Related Decision IDs** | `D-135`, `D-138`, `DD-151`, `DD-154`, `UD-012`, `UD-043` |
| **Related Formula IDs** | `F-AL-003` |
| **Inputs Received** | Voluntary resignation action, leadership transfer action, and a constitutional removal or transfer action recorded under the alliance's own procedures (any native ballot is candidate under `UD-042`/`UD-049`) |
| **Outputs Provided** | Updated office assignment registry, administrative root contact transition, audit event (`AUD-AL-002`) |
| **State Ownership** | Alliance owns internal governance roles; external systems read current administrative contact |
| **Authorized Actors** | Incumbent executive officer acting under the alliance's own procedures, or a recorded outcome of the alliance's own constitutional process; the platform prescribes no role or threshold |
| **Permission Requirement** | The alliance's own designated capability for the act. No platform-prescribed executive rank or voting threshold is approved |
| **National Player Consent** | Explicit consent of the transferring officer and explicit acceptance by the receiving member; a native ballot, if any, is candidate under `UD-042` |
| **Resource Impact** | None |
| **Security Boundary** | Prevention of unauthorized leadership takeovers; office holds authority, not personal account |
| **Failure Behaviour** | Rejection if the recipient is inactive, ineligible, or demoted (`ALF-03`; `ALF-04` is reserved for `INVALID_DISCORD_URL`) |
| **Recovery Responsibility** | Transaction aborted; incumbent remains in office; audit logged |
| **Unresolved Decision** | `UD-012` is **Resolved by B-09 §5–§11** as the structural role model; `UD-043` (succession, removal and vacancy policy) remains **Open** awaiting explicit owner decision |
| **Status** | **Candidate Succession Architecture; UD-012 structural model resolved; policy Open under UD-043** |

---

### AX-05 — Permission Changes and Role Grants

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-05` |
| **Integration Title** | Permission Changes and Role Grants |
| **Alliance Capability** | Grant, revoke, and audit granular capabilities with strict anti-escalation enforcement |
| **Owning Subsystem** | Alliance Governance (`B-09`) + Platform Security (`B-12`) |
| **Canonical External Rule** | `REQ-013` (DIRECT), `REQ-004` (DIRECT), `REQ-027` (DIRECT), `DIP-146` |
| **Alliance Internal Rule** | `ALL-059`, `ALL-062`, `ALL-066`–`ALL-078` |
| **Relevant REQ IDs** | `REQ-013`, `REQ-004`, `REQ-027`, `REQ-552`–`REQ-561` |
| **Related Decision IDs** | `D-139`, `DD-155`, `DD-156`, `UD-045` |
| **Related Formula IDs** | None |
| **Inputs Received** | Actor ID, target position ID, target member ID, modified permissions bitmask, actor authorization |
| **Outputs Provided** | Updated position record, member permission cache invalidation, audit log (`AUD-AL-004`) |
| **State Ownership** | Alliance owns position and permission tables; server enforces checks on every mutation |
| **Authorized Actors** | Member holding `MANAGE_ROLES` permission |
| **Permission Requirement** | `MANAGE_ROLES` |
| **National Player Consent** | None (internal alliance administrative action) |
| **Resource Impact** | None |
| **Security Boundary** | Anti-escalation invariant: officer cannot grant permissions they do not possess, nor edit roles beyond their constitutional authority |
| **Failure Behaviour** | Rejection if escalation attempted or actor lacks permission (`ALF-08`, `PRIVILEGE_ESCALATION_BLOCKED`) |
| **Recovery Responsibility** | State unmodified; security violation logged to audit spine |
| **Unresolved Decision** | `UD-045` (Capability catalogue and delegation limits awaiting explicit owner decision `UD-045`) |
| **Status** | **Candidate Capability Model; Open under UD-045 awaiting Owner decision** |

---

### AX-06 — Treasury Deposits of Already-Owned Resources

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-06` |
| **Integration Title** | Treasury Deposits of Already-Owned Resources |
| **Alliance Capability** | Candidate: accept voluntary member transfers from national treasury/warehouse into an alliance pool, if `UD-046` approves a pool |
| **Owning Subsystem** | Economy & Ledger System (`B-04`) |
| **Canonical External Rule** | `B-04` § 13 / § 16 / § 22, `ECN-212`, `TR-060`, `REQ-176`, `REQ-005`, `REQ-154`, `REQ-170` |
| **Alliance Internal Rule** | `ALL-095`, `ALL-096`, `ALL-098`, `ALL-102`, `ALL-103`, `ALL-105`, `ALL-107`, `ALL-108` |
| **Relevant REQ IDs** | `REQ-176` (DIRECT), `REQ-005` (DIRECT), `REQ-154` (DIRECT), `REQ-170` (DIRECT), `REQ-571`, `REQ-572` |
| **Related Decision IDs** | `D-136`, `DD-157`, `UD-046` |
| **Related Formula IDs** | `F-AL-001` (Dedicated Pool Capacity) |
| **Inputs Received** | Depositing nation ID, alliance ID, resource type, deposit quantity, nation unreserved balance |
| **Outputs Provided** | Debited national balance, credited alliance pool balance, audit ledger entry (`AUD-AL-006`) |
| **State Ownership** | Economy owns national inventory. Ownership of any alliance pool — entity, alliance, escrow or none — is unresolved under `UD-046`; this contract establishes no ownership. |
| **Authorized Actors** | Active member nation owner |
| **Permission Requirement** | `ACTIVE_MEMBER` status |
| **National Player Consent** | Mandatory explicit consent (player initiates and signs deposit transaction) |
| **Resource Impact** | Value conservation under `REQ-176`: national inventory decreases by $X$; alliance pool increases by $X$; zero net change |
| **Security Boundary** | Candidate rate limiting; double-spend prevention; non-minting verification |
| **Failure Behaviour** | Rejection if the national balance is insufficient (inherited Economy rule). An over-capacity rejection (`ALF-02`) would exist only if `UD-046` approves both a pool and a capacity model; neither is approved today, so no capacity-rejection rule is in force. |
| **Recovery Responsibility** | Atomic rollback; national balance intact; alliance balance intact |
| **Unresolved Decision** | `UD-046` (Treasury ownership, storage capacity model and over-capacity deposit policy are Open. `REQ-176` value conservation is an inherited binding constraint, not an owner approval of a pool.) |
| **Status** | **Candidate Treasury Architecture; Open under UD-046 awaiting Owner decision; REQ-176 Preserved** |

---

### AX-07 — Treasury Withdrawals, Grants and Loans

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-07` |
| **Integration Title** | Treasury Withdrawals, Grants and Loans |
| **Alliance Capability** | Candidate: authorise, gate and execute disbursements from an approved alliance pool to member nations or foreign aid recipients |
| **Owning Subsystem** | Economy & Ledger System (`B-04`) |
| **Canonical External Rule** | `B-04` § 12–16, `ECN-212`, `REQ-013`, `REQ-176`, `REQ-005`, `REQ-153`, `REQ-170` |
| **Alliance Internal Rule** | `ALL-097`, `ALL-100`, `ALL-109`, `ALL-110`, `ALL-111`, `ALL-112`, `ALL-113`, `ALL-114`, `ALL-115`, `ALL-117`, `ALL-118` |
| **Relevant REQ IDs** | `REQ-013` (DIRECT), `REQ-176` (DIRECT), `REQ-005` (DIRECT), `REQ-153` (DIRECT), `REQ-170` (DIRECT), `REQ-556`, `REQ-573`–`REQ-575` |
| **Related Decision IDs** | `D-136`, `DD-158`, `DD-159`, `UD-046` |
| **Related Formula IDs** | `F-AL-005` (Multi-Signature Dual Authorization Threshold) |
| **Inputs Received** | Proposing officer ID, approving officer ID, recipient nation ID, resource type, quantity, disbursement purpose |
| **Outputs Provided** | Debited alliance pool, credited recipient national warehouse/treasury, immutable audit log (`AUD-AL-007`) |
| **State Ownership** | Ownership of pooled balances is unresolved under `UD-046`; Economy owns recipient national inventory |
| **Authorized Actors** | Candidate: officers holding `PROPOSE_WITHDRAWAL`, `APPROVE_WITHDRAWAL`, `EXECUTE_WITHDRAWAL` |
| **Permission Requirement** | Candidate: distinct officers for proposal and approval above a threshold (`ALL-111`). No capability or separation rule is approved. |
| **National Player Consent** | A recipient nation's owner must explicitly accept a transfer; receipt is never inferred from silence, and accepting resources creates no treaty or diplomatic authority |
| **Resource Impact** | Value conservation under `REQ-176`: alliance pool decreases by $Y$; recipient nation increases by $Y$; zero minting |
| **Security Boundary** | Candidate optional dual authorization above a threshold (`F-AL-005`), candidate self-approval prohibition, recipient validation. None is enforced while `UD-046` is open. |
| **Failure Behaviour** | Rejection for insufficient pool balance or an invalid recipient follows inherited binding Economy rules. Self-approval, threshold and reservation failures would apply only if `UD-046` approves those candidate controls. |
| **Recovery Responsibility** | Reservation released; pool funds restored to available status; zero balance lost |
| **Unresolved Decision** | `UD-046` (Treasury withdrawal authorization, dual approval, and multi-sig thresholds are candidate proposals awaiting owner decision `UD-046`) |
| **Status** | **Candidate Treasury Architecture; Open under UD-046 awaiting Owner decision; Multi-Sig Provisional** |

---

### AX-08 — Alliance Resource Storage Limits

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-08` |
| **Integration Title** | Alliance Resource Storage Limits |
| **Alliance Capability** | Candidate: determine whether and how an alliance pool has storage limits. National warehouse capacity does not establish pool capacity, and neither rule creates a pool. |
| **Owning Subsystem** | Economy & Warehouse Systems (`B-04`) |
| **Canonical External Rule** | `B-04` § 13 / § 22, `REQ-176` (DIRECT), `REQ-141` (RELATED), `REQ-142` (RELATED) |
| **Alliance Internal Rule** | `ALL-096`, `ALL-104`, `ALL-105` |
| **Relevant REQ IDs** | `REQ-176` (DIRECT), `REQ-141` (RELATED), `REQ-142` (RELATED), `REQ-572` |
| **Related Decision IDs** | `D-136`, `DD-157`, `UD-046` |
| **Related Formula IDs** | `F-AL-001` (illustrative candidate capacity) |
| **Inputs Received** | Alliance active member count, resource type, current pool balance, incoming deposit quantity — only if a pool exists |
| **Outputs Provided** | Candidate capacity calculation; candidate acceptance or rejection flag. Neither is authoritative while `UD-046` is open. |
| **State Ownership** | Economy owns warehouse mechanics; ownership of alliance pool storage parameters is unresolved |
| **Authorized Actors** | System calculation engine (`SYS_ENGINE`), if the feature is approved |
| **Permission Requirement** | System internal execution |
| **National Player Consent** | None (candidate capacity evaluation) |
| **Resource Impact** | Candidate anti-hoarding control; no storage bound is enforced today |
| **Security Boundary** | National warehouse limits (`REQ-141`, `REQ-142`) do not define alliance-pool capacity, and an alliance pool never substitutes for a national warehouse. This boundary does not assert that a pool exists. |
| **Failure Behaviour** | If and only if `UD-046` approves a pool and a capacity model, an over-capacity deposit would be rejected (`ALF-02`) with zero debit. While `UD-046` is open, no capacity rejection is in force. |
| **Recovery Responsibility** | Depositor retained in original state; any candidate over-capacity handling is unapproved |
| **Unresolved Decision** | `UD-046` (Treasury pool capacity policy and over-capacity deposit behavior are candidate proposals awaiting owner decision `UD-046`) |
| **Status** | **Candidate Capacity Proposal; Open under UD-046 awaiting Owner decision; F-AL-001 Provisional** |

---

### AX-09 — Applications, Acceptance, Rejection and Withdrawal

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-09` |
| **Integration Title** | Applications, Acceptance, Rejection and Withdrawal |
| **Alliance Capability** | Manage the complete membership application lifecycle, review, admission, rejection, and voluntary exit |
| **Owning Subsystem** | Alliance Membership (`B-09`) + Account/Nation Interface (`B-01` / `B-03`) |
| **Canonical External Rule** | `REQ-002` (SUPPORTING CONTEXT), `ACC-001`, `TR-060` |
| **Alliance Internal Rule** | `ALL-079`, `ALL-080`, `ALL-081`, `ALL-082`, `ALL-083`, `ALL-084`, `ALL-085`, `ALL-086`, `ALL-091`, `ALL-092` |
| **Relevant REQ IDs** | `REQ-002`, `REQ-562`–`REQ-570` |
| **Related Decision IDs** | `D-138`, `DD-153`, `UD-044` |
| **Related Formula IDs** | `F-AL-004` (Rejoin Cooldown) |
| **Inputs Received** | Applicant nation ID, alliance ID, review action (`ACCEPT`, `REJECT`), voluntary departure action |
| **Outputs Provided** | Updated member roster record, membership status transition, audit log (`AUD-AL-001`) |
| **State Ownership** | Alliance owns membership roster; Nation owns national affiliation state |
| **Authorized Actors** | Applicant nation owner; candidate officer capabilities `ACCEPT_APPLICANTS` / `REMOVE_MEMBERS` |
| **Permission Requirement** | Candidate `ACCEPT_APPLICANTS` for admissions and `REMOVE_MEMBERS` for expulsions; none for voluntary departure |
| **National Player Consent** | Mandatory: application is voluntary and revocable; exit is unblockable at the nation owner's discretion (`REQ-567`) |
| **Resource Impact** | None on admission; national wealth remains private and untouched |
| **Security Boundary** | Candidate single-alliance baseline (`REQ-566`); candidate rejoin cooldown (`F-AL-004`). Neither is enforced while `UD-040`/`UD-044` are open. |
| **Failure Behaviour** | Rejection if the applicant is already affiliated would apply only if `UD-040` approves the single-alliance baseline; a cooldown rejection only if `UD-044` approves one. `ALF-06` is a candidate code. |
| **Recovery Responsibility** | Application rejected cleanly; national status unchanged |
| **Unresolved Decision** | `UD-044` (Member rights, expulsion appeals and cooldown are candidate; `UD-040` owns the single-alliance question. Freedom of exit is a binding sovereignty constraint.) |
| **Status** | **Candidate Membership Lifecycle; Open under UD-044 awaiting Owner decision; Cooldown Provisional** |

---

### AX-10 — Field-Level Visibility of Profile and Applicant Data

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-10` |
| **Integration Title** | Field-Level Visibility of Profile and Applicant Data |
| **Alliance Capability** | Classify each profile and applicant field into explicit visibility tiers (Public, Member-Only, Officer-Only) |
| **Owning Subsystem** | Foundations & Visibility (`B-02`) |
| **Canonical External Rule** | `B-02`, Prompt 07 § 9, `REQ-057` (DIRECT) |
| **Alliance Internal Rule** | `ALL-013`, `ALL-079`, `ALL-086` |
| **Relevant REQ IDs** | `REQ-057` (DIRECT), `REQ-538`, `REQ-539`, `REQ-564`, `REQ-604`, `REQ-605` |
| **Related Decision IDs** | `D-017`, `D-138` |
| **Related Formula IDs** | None |
| **Inputs Received** | Viewing actor nation ID, viewer role tier, target alliance ID, requested profile/roster field |
| **Outputs Provided** | Sanitized, redacted data view filtered by authorized visibility tier |
| **State Ownership** | Visibility rules owned by B-02; Alliance owns field values and role classifications |
| **Authorized Actors** | Authenticated players and public visitors |
| **Permission Requirement** | Evaluated dynamically based on actor relationship to alliance |
| **National Player Consent** | Players consent to public display of basic nation identity; private logs protected |
| **Resource Impact** | None |
| **Security Boundary** | Prevention of operational intelligence leaks; applicant identities are not public by default |
| **Failure Behaviour** | Redaction of unauthorized fields; access denied to private rosters |
| **Recovery Responsibility** | Platform returns filtered public view; zero confidential data exposed |
| **Unresolved Decision** | None specific to visibility; defaults follow B-02 and `REQ-057` (Provisional). Member-rights policy remains `UD-044` but does not gate field classification |
| **Status** | **Binding Inherited Privacy Constraint (`REQ-057`, Provisional); field defaults candidate** |

---

### AX-11 — City/Development Support Programmes

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-11` |
| **Integration Title** | City/Development Support Programmes |
| **Alliance Capability** | Candidate: facilitate voluntary development aid transfers from an approved alliance pool to assist member nation growth |
| **Owning Subsystem** | Cities & Infrastructure (`B-05`) + Economy (`B-04`) |
| **Canonical External Rule** | `B-05` § 23, `B-04` § 22, `REQ-172` (DIRECT), `REQ-218` (RELATED), `REQ-005` (RELATED) |
| **Alliance Internal Rule** | `ALL-117`, `ALL-118`, `ALL-120` |
| **Relevant REQ IDs** | `REQ-172`, `REQ-218`, `REQ-005`, `REQ-575` |
| **Related Decision IDs** | `D-136`, `DD-159`, `UD-046` |
| **Related Formula IDs** | None |
| **Inputs Received** | Recipient member nation ID, requested resource/crown grant, authorized grant proposal |
| **Outputs Provided** | Candidate: a grant transfer debited from an approved pool and credited to the recipient nation |
| **State Ownership** | Cities/Economy owns urban construction and capital expenditure; ownership of grant disbursement is unresolved under `UD-046` |
| **Authorized Actors** | Candidate: treasury officers holding grant authorization capabilities |
| **Permission Requirement** | Candidate `APPROVE_WITHDRAWAL` / `EXECUTE_WITHDRAWAL`; no capability is approved |
| **National Player Consent** | The recipient nation's owner must explicitly accept the grant; construction decisions remain sovereign and silence is not consent |
| **Resource Impact** | Value conservation under `REQ-176`; no alliance-level construction discount or free capacity |
| **Security Boundary** | Candidate non-repayable grants (`ALL-117`); no engine-enforced loan or debt garnishment (`ALL-118`, provisional) |
| **Failure Behaviour** | Rejection for insufficient pool balance or full national warehouse follows Economy rules; no grant feature is in force while `UD-046` is open |
| **Recovery Responsibility** | Transaction aborted; no pool reserved |
| **Unresolved Decision** | `UD-046` (Treasury support programme authorization governed by treasury policy under `UD-046`) |
| **Status** | **Candidate Treasury Support Model; Open under UD-046 awaiting Owner decision** |

---

### AX-12 — Readiness/Activity Declarations for Members

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-12` |
| **Integration Title** | Readiness/Activity Declarations for Members |
| **Alliance Capability** | Collect and display voluntary, opt-in member readiness and availability declarations |
| **Owning Subsystem** | Nation Activity (`B-03`) + Future Military (`B-10`) |
| **Canonical External Rule** | `B-03` § 13, `REQ-091` (SUPPORTING CONTEXT), `REQ-023` (RELATED) |
| **Alliance Internal Rule** | `ALL-137`, `ALL-138` |
| **Relevant REQ IDs** | `REQ-091`, `REQ-023`, `REQ-587` |
| **Related Decision IDs** | `D-137`, `UD-044`, `UD-049` |
| **Related Formula IDs** | None |
| **Inputs Received** | Voluntary player status declaration (`ACTIVE`, `DEPLOYED`, `UNAVAILABLE`), turn timestamp |
| **Outputs Provided** | Internal roster readiness indicator visible to authorized defense coordinators |
| **State Ownership** | Nation owns actual activity state; Alliance stores voluntary display declaration |
| **Authorized Actors** | Individual member nation owner |
| **Permission Requirement** | Self-reporting only (players update their own status) |
| **National Player Consent** | Strictly voluntary; no compulsory reporting or automated surveillance |
| **Resource Impact** | None |
| **Security Boundary** | Readiness data is strictly internal to alliance (`ALL-086`); protected from espionage leakage |
| **Failure Behaviour** | Rejection of malformed status codes |
| **Recovery Responsibility** | Status remains at previous declaration |
| **Unresolved Decision** | `UD-049` for any bulletin/notice surface. The voluntary readiness declaration itself is a candidate informational feature, not an approved foundation. |
| **Status** | **Candidate Informational Feature; no owner approval; no mechanical effect on military command** |

---

### AX-13 — Population/Approval Effects of Alliance Membership

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-13` |
| **Integration Title** | Population/Approval Effects of Alliance Membership (Deferred) |
| **Alliance Capability** | None assumed in v1; preserves boundary against unintended domestic demographic impacts |
| **Owning Subsystem** | Population & Domestic Politics (`B-06`) |
| **Canonical External Rule** | `B-06A`, `F-PD-001`–`F-PD-025` |
| **Alliance Internal Rule** | `ALL-006`, `ALL-007` |
| **Relevant REQ IDs** | None (deferred) |
| **Related Decision IDs** | `D-081`–`D-091` |
| **Related Formula IDs** | None |
| **Inputs Received** | Membership join/leave event (monitored only, no mutation triggered) |
| **Outputs Provided** | None (zero mechanical effect on approval, stability, or population growth) |
| **State Ownership** | Population and Domestic Politics owns approval/stability; Alliance has zero authority |
| **Authorized Actors** | None |
| **Permission Requirement** | None |
| **National Player Consent** | Inviolable: alliance membership cannot alter domestic approval or cause unrest |
| **Resource Impact** | Zero |
| **Security Boundary** | Prevents alliances from weaponizing domestic unrest against members |
| **Failure Behaviour** | Any attempted cross-system mutation is rejected at architectural boundary |
| **Recovery Responsibility** | Boundary enforcement; zero state mutation |
| **Unresolved Decision** | Deferred to future balance review if any demographic effect is ever proposed |
| **Status** | **Deferred to Future Prompts; Zero Effect in v1** |

---

### AX-14 — Elections/Crisis Interaction with Alliance Offices

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-14` |
| **Integration Title** | Elections/Crisis Interaction with Alliance Offices (Deferred) |
| **Alliance Capability** | Preserves strict separation between domestic elections/crises and alliance officeholding |
| **Owning Subsystem** | Domestic Politics & Elections (`B-06`) |
| **Canonical External Rule** | `B-06` Part II, `REQ-326` (SUPPORTING CONTEXT) |
| **Alliance Internal Rule** | `ALL-006`, `ALL-007`, `ALL-048` |
| **Relevant REQ IDs** | `REQ-326` |
| **Related Decision IDs** | `D-092`–`D-108` |
| **Related Formula IDs** | None |
| **Inputs Received** | Domestic election result, political crisis event |
| **Outputs Provided** | None (alliance officeholding is unaffected by domestic political transitions) |
| **State Ownership** | Domestic Politics owns national government; Alliance owns alliance positions |
| **Authorized Actors** | None |
| **Permission Requirement** | None |
| **National Player Consent** | Inviolable: domestic crisis cannot strip a player of alliance office |
| **Resource Impact** | None |
| **Security Boundary** | Separation of national leadership from alliance officeholding |
| **Failure Behaviour** | Rejection of any engine coupling |
| **Recovery Responsibility** | Independent execution |
| **Unresolved Decision** | Deferred; no cross-system coupling in v1 |
| **Status** | **Deferred to Future Prompts; Zero Interaction in v1** |

---

### AX-15 — National Treaties Persist Through Alliance Join/Leave/Removal

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-15` |
| **Integration Title** | National Treaties Persist Through Alliance Join/Leave/Removal |
| **Alliance Capability** | Ensure bilateral national treaties remain intact regardless of alliance membership changes |
| **Owning Subsystem** | Diplomacy System (`B-08`) |
| **Canonical External Rule** | `B-08` § 18, `DIP-146`–`DIP-149`, `REQ-530` (DIRECT), `REQ-523` (DIRECT), `REQ-531` (RELATED), `DIP-147` |
| **Alliance Internal Rule** | `ALL-004`, `ALL-006`, `ALL-090`, `ALL-122` |
| **Relevant REQ IDs** | `REQ-530`, `REQ-523`, `REQ-531` |
| **Related Decision IDs** | `D-123`, `D-126`, `D-137`, `D-140`, `DD-160` |
| **Related Formula IDs** | None |
| **Inputs Received** | Member join event, voluntary exit event, member expulsion event |
| **Outputs Provided** | Zero mutation to existing bilateral treaties (`NAP`, `Consultation`, `Aid`) |
| **State Ownership** | Diplomacy (`B-08`) owns bilateral treaties; Alliance has zero authority to alter them |
| **Authorized Actors** | None (membership changes have no treaty authority) |
| **Permission Requirement** | None |
| **National Player Consent** | Sovereign treaties require explicit bilateral agreement; alliance cannot void them |
| **Resource Impact** | None |
| **Security Boundary** | Alliances cannot break or cancel member treaties; prevents alliance-mandated treaty breaches |
| **Failure Behaviour** | Any attempt to cancel national treaties via alliance action is rejected (`ALF-09`) |
| **Recovery Responsibility** | Treaties remain active and binding per B-08 lifecycle rules |
| **Unresolved Decision** | None on national treaty persistence (resolved by `DIP-147`; `REQ-530` and `REQ-523` remain Provisional requirements). `D-137`'s no-alliance-object conclusion is amended only by `D-140` for a separate B-09 treaty object; the B-08 object is never reused, copied or mutated. |
| **Status** | **Binding Inherited Constraint (`B-08`, `D-137`, `DIP-147`); Provisional requirements** |

---

### AX-16 — Alliance Diplomatic Positions (Non-Binding)

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-16` |
| **Integration Title** | Alliance Diplomatic Positions (Non-Binding) |
| **Alliance Capability** | Candidate: publish a non-binding collective diplomatic position regarding a foreign entity. It creates no delegation, treaty or obligation. |
| **Owning Subsystem** | Diplomacy (`B-08`) + Alliance System (`B-09`) |
| **Canonical External Rule** | `B-08` § 18, `08A` § 13, `REQ-530` (DIRECT), `REQ-523` (RELATED), `REQ-531` (RELATED) |
| **Alliance Internal Rule** | `ALL-123`, `ALL-124`, `ALL-127`, `ALL-128` |
| **Relevant REQ IDs** | `REQ-530`, `REQ-523`, `REQ-531`, `REQ-579`, `REQ-580` |
| **Related Decision IDs** | `D-137` (resolves `UD-039`), `D-140` (separate B-09 treaty object), `DD-160`, `UD-047` |
| **Related Formula IDs** | None |
| **Inputs Received** | Target foreign alliance/nation ID, proposed stance (`Friendly`, `Neutral`, `Hostile`, `Boycott`) |
| **Outputs Provided** | Public collective stance record, audit log (`AUD-AL-008`), notification to members |
| **State Ownership** | Alliance owns public stances; Diplomacy owns mechanical treaty states |
| **Authorized Actors** | Candidate: officers holding `MANAGE_FOREIGN_POLICY` |
| **Permission Requirement** | Candidate `MANAGE_FOREIGN_POLICY`; no capability is approved |
| **National Player Consent** | A non-binding position requires no individual consent because it binds nobody; it never forces a treaty, embargo or posture. A member may disassociate from it publicly. |
| **Resource Impact** | None |
| **Security Boundary** | Stances are informational only; they cannot force member embargos, attacks, cancellations, national posture or treaty effects, and they create no delegation. Only the separate `AX-29` treaty object, with a registered `AT-E00` or `AT-E01` effect, can create a treaty mechanic; a collective position is never a treaty |
| **Failure Behaviour** | Rejection if actor lacks permission or target entity does not exist |
| **Recovery Responsibility** | Stance record remains unchanged |
| **Unresolved Decision** | `UD-047` (collective positions are candidate). `UD-039` is resolved by `D-137` for the national system; `D-140` authorizes only a separate B-09 Alliance-to-Alliance treaty object. No collective position is a treaty, and no delegation exists. |
| **Status** | **Candidate Position Feature; Open under UD-047; no delegation (binding `B-08`/`REQ-530` constraint)** |

---

### AX-17 — Embargo and Restricted-Pair Checks on Alliance-Mediated Transfers

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-17` |
| **Integration Title** | Embargo and Restricted-Pair Checks on Alliance-Mediated Transfers |
| **Alliance Capability** | Apply bilateral embargo and restricted-pair checks to any future treasury disbursement or aid transfer; no alliance office can waive a national embargo |
| **Owning Subsystem** | Diplomacy (`B-08`) + Economy (`B-04`) |
| **Canonical External Rule** | `B-08`, `B-04` § 21–22, `REQ-529` (DIRECT), `REQ-175` (DIRECT), `REQ-170` (DIRECT) |
| **Alliance Internal Rule** | `ALL-112`, `ALL-115`, `ALL-160` |
| **Relevant REQ IDs** | `REQ-529`, `REQ-175`, `REQ-170`, `REQ-576` |
| **Related Decision IDs** | `D-126`, `D-136`, `DD-158` |
| **Related Formula IDs** | None |
| **Inputs Received** | Source alliance ID, recipient nation ID, proposed transfer amount, bilateral embargo state |
| **Outputs Provided** | Compliance check result (`PASS` / `BLOCK`), transaction validation record |
| **State Ownership** | Diplomacy owns embargo records; Economy owns restricted-pair rules; Alliance queries both |
| **Authorized Actors** | System transfer execution engine |
| **Permission Requirement** | System validation |
| **National Player Consent** | National embargoes are sovereign; alliance disbursements cannot override active embargoes |
| **Resource Impact** | Prevents illicit resource leakage through alliance pooling |
| **Security Boundary** | Alliance transfers cannot bypass bilateral embargoes or multi-account restrictions |
| **Failure Behaviour** | Rejection of a transfer if an active embargo exists between the disbursing nation and the recipient (`ALF-10`); alliance leadership cannot override it |
| **Recovery Responsibility** | Transfer aborted; any reservation released; audit log recorded |
| **Unresolved Decision** | None on the embargo boundary (`B-08`, `REQ-529`, `REQ-175`, all Provisional requirements); the transfer workflow itself remains under `UD-046` |
| **Status** | **Binding Inherited Constraint (`B-08`, `REQ-529`); Provisional requirement; no alliance override** |

---

### AX-18 — War/Coordination Information

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-18` |
| **Integration Title** | War/Coordination Information (Deferred to Prompt 10) |
| **Alliance Capability** | Candidate: publish informational strategic coordination notices; national military command remains strictly sovereign |
| **Owning Subsystem** | Military System (`B-10`, Future) |
| **Canonical External Rule** | Prompt 10 interface, `REQ-014` (RELATED), `REQ-518` (RELATED) |
| **Alliance Internal Rule** | `ALL-136`, `ALL-138`, `ALL-140`, `ALL-141` |
| **Relevant REQ IDs** | `REQ-014`, `REQ-518`, `REQ-588`–`REQ-597` |
| **Related Decision IDs** | `D-015`, `D-023`, `D-137` |
| **Related Formula IDs** | None |
| **Inputs Received** | Strategic notice payload (target nation ID, coordination theater, suggested deployment) |
| **Outputs Provided** | Published internal coordination bulletin (`AUD-AL-012`) |
| **State Ownership** | Military owns tactical combat and war states; Alliance owns coordination text |
| **Authorized Actors** | Candidate: alliance members holding `COORDINATE_DEFENSE`; the capability is not approved |
| **Permission Requirement** | Candidate `COORDINATE_DEFENSE`; any notice surface also requires `UD-049` |
| **National Player Consent** | Inviolable: military forces belong exclusively to sovereign nations; zero automated war-drag |
| **Resource Impact** | None; operations points and military upkeep remain 100% national |
| **Security Boundary** | Alliances cannot declare wars on behalf of members or command national armies |
| **Failure Behaviour** | Rejection if actor lacks permission; any attempted military execution rejected |
| **Recovery Responsibility** | Bulletin unpublished |
| **Unresolved Decision** | Formal warfare and coalition combat mechanics deferred to Prompt 10 (`REQ-591`); any coordination-notice surface is candidate under `UD-049` |
| **Status** | **Deferred to Prompt 10; candidate coordination notices only; no approved bulletin feature** |

---

### AX-19 — Static Discord Invite Link

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-19` |
| **Integration Title** | Static Discord Invite Link |
| **Alliance Capability** | Store and display one optional external communication URL on the alliance profile |
| **Owning Subsystem** | Alliance Profile (`B-09`) + Platform Security (`B-12`) |
| **Canonical External Rule** | `D-133`, `DD-147`, `DD-148`, `REQ-057` (RELATED) |
| **Alliance Internal Rule** | `ALL-165`, `ALL-166`, `ALL-167`, `ALL-168` |
| **Relevant REQ IDs** | `REQ-057`, `REQ-598`–`REQ-603` |
| **Related Decision IDs** | `D-133`, `DD-147`, `DD-148`, `UD-048` |
| **Related Formula IDs** | None |
| **Inputs Received** | Proposed invite link URL string, editing actor credentials |
| **Outputs Provided** | Candidate: a validated static invite URL for display. The link feature itself is provisional. |
| **State Ownership** | Alliance owns the metadata field if the feature ships; Platform Security would apply a candidate allowlist |
| **Authorized Actors** | Candidate: an officer holding `MANAGE_DISCORD_LINK` |
| **Permission Requirement** | Candidate `MANAGE_DISCORD_LINK`; not approved |
| **National Player Consent** | Visiting the external link is voluntary; Discord is never required for membership or play |
| **Resource Impact** | None |
| **Security Boundary** | Candidate allowlist recommendation (`discord.gg`, `discord.com/invite`); zero API, zero bots, zero auth are binding boundaries (`D-133`, `ALL-167`) |
| **Failure Behaviour** | A candidate validator would reject a non-allowlisted or script-bearing URL with `ALF-11`; no rejection rule is approved under `UD-048` |
| **Recovery Responsibility** | URL discarded; previous link maintained; security audit logged |
| **Unresolved Decision** | `UD-048` (visibility, validation and allowlist policy are Open). `DD-148` is **Provisional**, not an approved security baseline. |
| **Status** | **Provisional Recommendation (`DD-148`); Open under UD-048; zero-API boundary binding (`D-133`)** |

---

### AX-20 — Announcements and Formal Notices

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-20` |
| **Integration Title** | Announcements and Formal Notices |
| **Alliance Capability** | Candidate: publish asynchronous official bulletins and leadership notices to members, if `UD-049` approves the tool |
| **Owning Subsystem** | Alliance System (`B-09`) |
| **Canonical External Rule** | `REQ-057` (RELATED), `REQ-021` (SUPPORTING CONTEXT) |
| **Alliance Internal Rule** | `ALL-161`, `ALL-162`, `ALL-163`, `ALL-164` |
| **Relevant REQ IDs** | `REQ-057`, `REQ-021`, `REQ-586`, `REQ-606` |
| **Related Decision IDs** | `D-133`, `DD-147`, `UD-049` |
| **Related Formula IDs** | None |
| **Inputs Received** | Candidate: notice title, markdown body (length cap unapproved), author ID, priority flag |
| **Outputs Provided** | Candidate: a published bulletin record, member inbox notice and audit log (`AUD-AL-012`) |
| **State Ownership** | Alliance owns bulletin storage and publication history if the feature is approved |
| **Authorized Actors** | Candidate: officers holding `POST_ANNOUNCEMENT` |
| **Permission Requirement** | Candidate `POST_ANNOUNCEMENT`; not approved |
| **National Player Consent** | Players receive asynchronous notices in system inbox; no real-time push interruptions |
| **Resource Impact** | None |
| **Security Boundary** | Content moderation sanitization; no chat, no comments, no typing indicators (`D-133`) |
| **Failure Behaviour** | A candidate validator would reject an over-limit or disallowed payload; no limit or notice tool is in force |
| **Recovery Responsibility** | Bulletin rejected; author prompted with validation error |
| **Unresolved Decision** | `UD-049` (Asynchronous official bulletins are candidate proposals awaiting explicit Owner approval under `UD-049`; zero real-time chat is an owner-approved product constraint (`D-133` / `DD-147`)) |
| **Status** | **Candidate Scope Proposal; Bulletins Open under UD-049 awaiting Owner decision; Zero Chat Owner Constraint (`D-133`)** |

---

### AX-21 — Audit and History of Alliance Actions

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-21` |
| **Integration Title** | Audit and History of Alliance Actions |
| **Alliance Capability** | Record all state-altering governance, membership, treasury, and constitutional acts immutably |
| **Owning Subsystem** | Alliance System (`B-09`) + Platform Audit Spine (`B-12`) |
| **Canonical External Rule** | `B-09`, Prompt 02, `D-026`, `REQ-027` (DIRECT), `REQ-021` (DIRECT), `REQ-153` (DIRECT), `REQ-013` (RELATED) |
| **Alliance Internal Rule** | `ALL-005`, `ALL-043`, `ALL-065`, `ALL-101`, `ALL-128`, `ALL-135`, `ALL-147`, `ALL-153`, `ALL-154` |
| **Relevant REQ IDs** | `REQ-027`, `REQ-021`, `REQ-153`, `REQ-013`, `REQ-609`–`REQ-613` |
| **Related Decision IDs** | `D-026`, `D-136`, `D-138`, `D-139` |
| **Related Formula IDs** | None |
| **Inputs Received** | Event code (`AUD-AL-###`), actor ID, target ID, turn number, timestamp, parameter payload, SHA-256 hash |
| **Outputs Provided** | Immutable, append-only audit row, verifiable event sequence |
| **State Ownership** | Platform Audit Spine owns immutable storage; Alliance generates domain event data |
| **Authorized Actors** | System execution runtime (automated on every state change) |
| **Permission Requirement** | System internal |
| **National Player Consent** | None (mandatory security audit trail) |
| **Resource Impact** | Append-only database storage |
| **Security Boundary** | Rows cannot be deleted, edited, or retroactively modified by players or administrators |
| **Failure Behaviour** | If audit logging fails, the initiating transaction aborts atomically (`FAIL_CLOSED`) |
| **Recovery Responsibility** | Database rollbacks transaction; state remains unmodified |
| **Unresolved Decision** | None; the audit-spine decision `D-026` is inherited. Coverage of new alliance event types is specified here but not implemented. |
| **Status** | **Binding Inherited Audit Infrastructure (`D-026`); `REQ-027` remains planned** |

---

### AX-22 — Rankings/Chronicle Aggregates

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-22` |
| **Integration Title** | Rankings/Chronicle Aggregates (Deferred to Prompt 11) |
| **Alliance Capability** | Supply public historical metadata and aggregate statistics to future rankings system |
| **Owning Subsystem** | Rankings & Chronicle (`B-11`, Future) |
| **Canonical External Rule** | Prompt 11 interface, `REQ-058` (SUPPORTING CONTEXT) |
| **Alliance Internal Rule** | `ALL-022`, `ALL-152` |
| **Relevant REQ IDs** | `REQ-058` |
| **Related Decision IDs** | None |
| **Related Formula IDs** | None |
| **Inputs Received** | Alliance lifecycle events, member count updates, dissolution events |
| **Outputs Provided** | Aggregate statistics payload (peak member count, active turns, founding turn, final status) |
| **State Ownership** | Alliance owns historical metadata; Rankings owns ranking tables and chronicle presentation |
| **Authorized Actors** | System rankings engine |
| **Permission Requirement** | System internal |
| **National Player Consent** | Public aggregate statistics only; private logs excluded |
| **Resource Impact** | None |
| **Security Boundary** | Aggregates are derived from public metadata; zero access to private member data |
| **Failure Behaviour** | None (read-only derivation) |
| **Recovery Responsibility** | Recomputed at next aggregation boundary |
| **Unresolved Decision** | Prompt 11 owns ranking metrics and scoring formulas; `REQ-058` is Provisional and no aggregate schema is approved |
| **Status** | **Deferred to Prompt 11; candidate aggregates; no ranking or chronicle feature is in scope for 09B** |

---

### AX-23 — Fair-Play/Moderation of Alliance Conduct

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-23` |
| **Integration Title** | Fair-Play/Moderation of Alliance Conduct (Deferred to Prompt 12) |
| **Alliance Capability** | Provide evidence reporting channels and enforce platform moderation sanctions |
| **Owning Subsystem** | Moderation & Fair Play (`B-12`, Future) |
| **Canonical External Rule** | Prompt 12 interface, `REQ-025` (DIRECT), `REQ-026` (DIRECT), `REQ-027` (DIRECT) |
| **Alliance Internal Rule** | `ALL-013`, `ALL-142`, `ALL-158` |
| **Relevant REQ IDs** | `REQ-025`, `REQ-026`, `REQ-027` |
| **Related Decision IDs** | `D-018`, `D-025`, `D-031` |
| **Related Formula IDs** | None |
| **Inputs Received** | Abuse report payload, content moderation alert, platform suspension directive |
| **Outputs Provided** | Administrative review packet, forced naming reset or sanction execution record |
| **State Ownership** | Platform Moderation owns sanctions and TOS enforcement; Alliance complies with directives |
| **Authorized Actors** | Platform moderators and system safety automation |
| **Permission Requirement** | Platform administrative authority |
| **National Player Consent** | Platform Terms of Service govern moderation interventions |
| **Resource Impact** | None |
| **Security Boundary** | Alliances cannot self-adjudicate TOS violations; platform moderation acts independently |
| **Failure Behaviour** | Rejection of improper reports; escalated handling of confirmed violations |
| **Recovery Responsibility** | Platform moderation runbooks |
| **Unresolved Decision** | Moderation procedures and automated detection tools deferred to Prompt 12 |
| **Status** | **Deferred to Prompt 12; name moderation is a planned inherited constraint, not implemented** |

---

### AX-24 — Notifications and UI Surfaces

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-24` |
| **Integration Title** | Notifications and UI Surfaces (Deferred to Prompt 13) |
| **Alliance Capability** | Emit structured alliance event notifications to member notification centers and digests |
| **Owning Subsystem** | Interface & Notification Systems (`B-13`, Future) |
| **Canonical External Rule** | Prompt 13 interface, `REQ-020` (SUPPORTING CONTEXT) |
| **Alliance Internal Rule** | `ALL-161`, `ALL-164` |
| **Relevant REQ IDs** | `REQ-020`, `REQ-607`, `REQ-608` |
| **Related Decision IDs** | None |
| **Related Formula IDs** | None |
| **Inputs Received** | Alliance event trigger (admission, expulsion, proposal, withdrawal, ballot closure) |
| **Outputs Provided** | Formatted asynchronous notification payload routed to recipient inboxes |
| **State Ownership** | Alliance generates domain event; Interface manages delivery and display |
| **Authorized Actors** | System event bus |
| **Permission Requirement** | System internal |
| **National Player Consent** | Players configure notification preferences per category |
| **Resource Impact** | None |
| **Security Boundary** | Zero real-time push spam; batched digest delivery at turn boundaries |
| **Failure Behaviour** | Notification dropped or queued; underlying alliance state unaffected |
| **Recovery Responsibility** | Re-emitted from audit log if critical |
| **Unresolved Decision** | Notification delivery taxonomy deferred to Prompt 13; the notice/bulletin feature remains Open under `UD-049` |
| **Status** | **Deferred to Prompt 13; candidate notification taxonomy; zero real-time chat is binding (`D-133`)** |

---

### AX-25 — Formula and Balance Registration

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-25` |
| **Integration Title** | Formula and Balance Registration (Deferred to Prompt 14) |
| **Alliance Capability** | Register all alliance formulas, parameters, and operational thresholds with master balance register |
| **Owning Subsystem** | Formula Register & Balance Systems (`B-14`, Future) |
| **Canonical External Rule** | Prompt 14 interface, `REQ-163` (DIRECT), `REQ-098` (RELATED), `REQ-047` (RELATED), `D-064` |
| **Alliance Internal Rule** | `ALL-174`, [`16_alliances_formula_register.md`](16_alliances_formula_register.md) |
| **Relevant REQ IDs** | `REQ-163`, `REQ-098`, `REQ-047`, `REQ-614` |
| **Related Decision IDs** | `D-064`, Prompt 14 calibration |
| **Related Formula IDs** | `F-AL-001` through `F-AL-007` |
| **Inputs Received** | Draft mathematical specifications, variable types, rounding rules, unit declarations |
| **Outputs Provided** | Candidate formula records and test-harness specifications; nothing is registered as an approved formula |
| **State Ownership** | The formula register owns mathematical definitions; the alliance would implement only formulas that survive Prompt 14 and the owning owner decision |
| **Authorized Actors** | Specification author, not a gameplay actor |
| **Permission Requirement** | Specification authoring |
| **National Player Consent** | None (mathematical architecture) |
| **Resource Impact** | Candidate integer arithmetic; no balance is approved |
| **Security Boundary** | The register prevents uncalibrated formulas from being mistaken for approved balance |
| **Failure Behaviour** | A validator should reject a formula presented as approved without an owner decision; it must **not** reject a specification that omits a particular threshold |
| **Recovery Responsibility** | Candidate formulas carry full metadata and an explicit decision status |
| **Unresolved Decision** | Prompt 14 owns simulations and calibration; `UD-040`, `UD-043`, `UD-044` and `UD-046` own the policy choices |
| **Status** | **Candidate Specifications; none approved; balance deferred to Prompt 14** |

---

### AX-26 — Global Trade Interaction

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-26` |
| **Integration Title** | Global Trade Interaction |
| **Alliance Capability** | Consume market context without intermediating, bypassing, or creating competing trade channels |
| **Owning Subsystem** | Market & Global Trade System (`B-07`) |
| **Canonical External Rule** | `B-07`, Prompt 07C, `D-122`, `DD-136`, `REQ-513` (DIRECT), `REQ-010` (DIRECT), `G-1` through `G-6` |
| **Alliance Internal Rule** | `ALL-009`, `ALL-027` |
| **Relevant REQ IDs** | `REQ-513` (DIRECT), `REQ-010` (DIRECT), `REQ-577` |
| **Related Decision IDs** | `D-122`, `DD-136` |
| **Related Formula IDs** | None |
| **Inputs Received** | Market state queries, published reference prices (read-only) |
| **Outputs Provided** | Zero trade order mutations; zero private trade boards |
| **State Ownership** | Global Trade owns all public boards, order clearing, trading fees, and release gates (`G-1`..`G-6`) |
| **Authorized Actors** | None (alliances possess no market trading actor role) |
| **Permission Requirement** | None |
| **National Player Consent** | Market trades are executed exclusively by sovereign nation owners |
| **Resource Impact** | Alliances cannot collect trading fees, levy internal tariffs, or subsidize market lots |
| **Security Boundary** | **MANDATORY INVARIANT:** Alliances cannot bypass market gates, create private trading networks, or undercut trading fees |
| **Failure Behaviour** | Any attempted market intermediation by an alliance entity is rejected cleanly (`ALF-12`) |
| **Recovery Responsibility** | Architectural boundary enforcement; zero market state mutation |
| **Unresolved Decision** | None (Global Trade scope and gates approved under `D-122` and `DD-136`) |
| **Status** | **Approved Mandatory Constraint (`D-122`, `DD-136`, `REQ-513`)** |

---

### AX-27 — Automatic Per-Turn Member Taxation

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-27` |
| **Integration Title** | Automatic Per-Turn Member Taxation |
| **Alliance Capability** | Collect a player-defined tax automatically each turn from each active member's **current-turn production**, using that member's frozen per-Alliance bracket assignment and separate Crowns and resource rates, and receive and account for credits in the Alliance Receiving Ledger. The separate `D-141` boundary permits a registered platform cost to be paid from `AVAILABLE` ARL value for a registered operational purpose (`ALL-220`–`ALL-226`), but no cost schedule is approved and no purpose is currently spendable |
| **Owning Subsystem** | National Economy and Ledger (`B-04`) for production, balances and transfer; Alliance (`B-09`) for bracket, assignment, rate and permission policy |
| **Canonical External Rule** | `ECN-094`, `ECN-100`, `ECN-143`, `ECN-144`, `ECN-146`, `ECN-148`, `ECN-150`, `ECN-195`, `ECN-212`, `TR-060`, `REQ-176` |
| **Alliance Internal Rule** | `ALL-179`, `ALL-180`, `ALL-181`, `ALL-182`, `ALL-183`, `ALL-184`, `ALL-185`, `ALL-186`, `ALL-187` |
| **Relevant REQ IDs** | `REQ-618`–`REQ-625` (DIRECT); `REQ-648`–`REQ-653` (DIRECT, ARL accounting and operational funding) |
| **Related Decision IDs** | `D-140`, `D-141`, `DD-161`, `DD-164`; `UD-040`, `UD-044`, `UD-046` remain Open; `UD-045` is narrowly authorized only for tax-management permissions |
| **Related Formula IDs** | `F-AL-006` (automatic per-turn production tax arithmetic); `F-AL-008` (purpose-limited operational funding arithmetic) |
| **Inputs Received** | Immutable turn snapshot `(snapshot_id)` of active membership, bracket versions, per-Alliance bracket assignments and role-permission state; the set of active alliances that could assert a tax claim on the member; each member's gross Crowns income from P3.1 (`ECN-094`/`ECN-146`); each member's gross output of each supported stored resource from P3.3 extraction or P3.5 processing; the bracket's per-asset rates in basis points; `turn_id` and settlement identifier. For operational funding: ARL `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` balances per asset; registered purpose `AOP-01`–`AOP-04`; an approved cost schedule and version **where one exists — none is approved today, so no purpose is currently spendable**; the registered platform cost sink; and the authorization record with its idempotency key |
| **Outputs Provided** | Per-asset tax at the production source; Alliance Receiving Ledger credit; net production credited to the nation and available to later same-turn stages; paired `TRANSFER_OUT`/`TRANSFER_IN` ledger events under one `transfer_id`; per-asset receipt naming bracket/version, rates, and for each production event its sequence, gross, cumulative gross, cumulative tax due, tax at the event and tax already collected, plus the end-of-turn gross, total tax and net, ARL credit, attribution status and reason, fallback flag and snapshot ID; `AUD-AL-013` audit event; deterministic idempotency key `(settlement_id, nation_id, alliance_id, asset)`. For operational funding: ARL category balances, allocation, release, a settled platform-cost receipt only when a purpose is available, reconciliation and `AUD-AL-019`; with no approved cost schedule, the normal result is that no purpose is spendable and any actual expense is rejected |
| **State Ownership** | B-04 owns production, national balances and the canonical transfer; B-09 owns the bracket, rate, per-Alliance assignment, permission and operational authorization records; the ARL owns a receipt and accounting record in four categories. No treasury ownership, custody or general pool is decided here |
| **Authorized Actors** | Only an authenticated account holding the alliance's active permission for the specific act: create/edit/delete bracket, set Crowns rate, set resource rate, assign/change member bracket, view aggregate reports, view member contribution history, authorize a registered operational expense. No fixed office is created and no AI, automated agent or unauthorized office may act |
| **Permission Requirement** | The player-authored constitution defines the permissions and who holds them; an unauthorized tax-policy action is rejected with `ALF-21`, and an unauthorized or invalid operational expense is rejected with `ALF-27`; neither enters the version history, the turn snapshot or the ARL |
| **National Player Consent** | Not required per policy version or rate change: taxation is an internal alliance economic rule governed by role permissions. It is distinct from B-08 national diplomacy. A non-member is never taxed, and membership alone assigns no rate |
| **Resource Impact** | For each asset, order its production events $j=1,\ldots,m$ in the deterministic P3 sequence and let $C_j=\sum_{k\le j}g_k$, $D_0=0$ and $D_j=\lfloor C_j \times r / 10{,}000 \rfloor$. The tax at event $j$ is $D_j-D_{j-1}$, and the end-of-turn tax is $D_m=\lfloor G \times r / 10{,}000 \rfloor$ with $0 \le D_m \le G$ and $\sum_j (D_j-D_{j-1})=D_m$. A single-event asset, including Crowns in P3.1, reduces to the per-turn floor; independent per-event floors are not used. The event tax is transferred to the ARL and the event net remains with the nation in one atomic transaction, with the end-of-turn total reconciling to $D_m$. Opening Crowns, existing stockpiles, earlier production, donations, gifts, aid, reparations, market purchases/sale proceeds and other non-production inflows are never in the base. GU is not stored and not taxable. Later same-turn P3 stages may consume only the post-tax net; a 100% rate leaves zero of that turn's production for those stages; an existing stockpile consumed later is not taxed and a processing input is not taxed again. P3.2 maintenance is charged after the Crowns tax from the unreserved post-tax balance including any opening Crowns; that spending is not a tax event. Operational funding, when a purpose and approved cost schedule exist, moves only ARL `AVAILABLE` value to a registered platform cost sink and never debits a nation or pays a player; today no approved schedule exists, so no operational value moves and the assets remain in the ARL |
| **Security Boundary** | **MANDATORY INVARIANT:** collection is automatic only under a valid frozen bracket with an active role-authorized policy; rates are any integer 0–10,000 bp (0–100%), never restricted to 10% increments; an unassigned, deleted or invalid assignment uses the visible recorded 0% fallback; no engine/AI/platform default rate, no mid-turn change, no retroactive recomputation, no double collection, no negative balance, no stockpile charge, no forced sale. Tax at an event is the increment of one floored cumulative liability per asset and turn, not an independent per-event floor, and the sum of event taxes must equal `floor(total gross × rate_bp / 10,000)`, so no fractional remainder is dropped or collected twice. One eligible production event is deducted at most once across all alliances and never loses more than 100% of gross; multiple membership never authorizes multiple deductions and no alliance receives priority. If the applicable alliance or bracket cannot be established unambiguously, the provisional safeguard records and displays a 0% Alliance-tax fallback for the affected asset and turn, leaves gross production intact and never delays, destroys or charges it. The ARL imposes no capacity limit and may not reject, destroy or lose generated tax for lack of an approved capacity model. Receipt accounting, allocation, approved operational expenditure and general treasury authority are distinct. Operational funding may debit only `AVAILABLE`; `RESERVED` and `EXPENDED` are not spendable; the only destination is a registered platform cost sink; no purpose is spendable without an approved cost schedule, and none is approved today; no general withdrawal, distribution, grant, loan, refund, player payment or transfer to a nation, member, officer or alliance exists; every expense is at most once and idempotent |
| **Failure Behaviour** | A member outside the snapshot is not taxed. An invalid assignment or unconfigured asset yields the visible 0% fallback and is shown in the receipt, not a failure. Multiple or ambiguously attributed memberships yield the recorded 0% multiple-membership safeguard, not a failure; gross production posts in full and no alliance is credited. An unauthorized bracket, rate or assignment change is rejected with `ALF-21` and never enters the version history or snapshot. A missing, incomplete or inconsistent authoritative production record or frozen snapshot, a conflicting idempotency-key reuse or a failed paired ledger write rejects the production+tax transaction with `ALF-23`; a cumulative-reconciliation mismatch, an out-of-order or replayed event that would advance the accumulator, or a per-event floor that differs from the required cumulative increment is also `ALF-23`. No existing stockpile or balance is charged, no partial collection occurs and a retry cannot create a second charge. An operational expense with an invalid purpose, schedule, amount, destination, authorization or permission is rejected with `ALF-27`; because no cost schedule is approved today, every actual expense is currently rejected as unavailable; insufficient `AVAILABLE` is `ALF-28`; settlement failure or conflicting key reuse is `ALF-29`; nothing is paid twice or partially and no value is silently dropped |
| **Recovery Responsibility** | B-04 retries the idempotent transaction; B-09 preserves every version, authorization and audit record; the member and authorized roles receive the receipt, rejection or failure record; no value moves twice, no reservation is stranded and no value is lost |
| **Unresolved Decision** | `UD-046` (treasury ownership, custody, capacity, general withdrawal, general spending beyond the `D-141` boundary, distributions, dual approval and treasury offices remain Open; the ARL is a receipt/accounting record and creates no right, and no operational purpose is currently spendable); `UD-040` (multi-Alliance membership remains Open; the at-most-once, no-priority and visible 0% ambiguous-attribution safeguard is a reversible provisional behaviour, not an owner decision on whether multiple membership is permitted); `UD-044` (member rights and appeal remain Open); `UD-045` (only the narrow tax-management permissions are authorized; the wider catalogue and delegation remain Open); `UD-047` (collective positions and delegation remain Open and are untouched by this internal economic rule) |
| **Status** | **Binding Owner-Authorized Constraint (`D-140` taxation and accounting; `D-141` narrow operational-funding boundary); rates, brackets, per-Alliance assignments and permissions player-defined; ARL receipt/accounting; no approved cost schedule, so no operational purpose is currently spendable; general treasury policy Open under `UD-046`** |

---

### AX-28 — Voluntary Donations and Receipts

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-28` |
| **Integration Title** | Voluntary Donations and Receipts |
| **Alliance Capability** | Receive a one-time, donor-confirmed transfer of crowns or a supported resource into the Alliance Receiving Ledger's `RECEIVED` and `AVAILABLE` categories |
| **Owning Subsystem** | National Economy and Ledger (`B-04`) |
| **Canonical External Rule** | `ECN-212`, `ECN-213`, `TR-060`, `REQ-176` |
| **Alliance Internal Rule** | `ALL-188`, `ALL-189`, `ALL-190`, `ALL-191`, `ALL-192`, `ALL-193`, `ALL-194`, `ALL-195` |
| **Relevant REQ IDs** | `REQ-626`–`REQ-632` (DIRECT) |
| **Related Decision IDs** | `D-140`, `DD-161`; `UD-046` remains Open |
| **Related Formula IDs** | `F-AL-007` (donation conservation arithmetic) |
| **Inputs Received** | Donor nation identity, receiving alliance identity, selected asset and integer amount, donor unreserved balance, idempotency key, authenticated confirmation |
| **Outputs Provided** | One canonical transfer under a single `transfer_id`, matched debit/credit ledger events, ARL credit record, immutable donor and alliance receipts, donation history entry, `AUD-AL-014` audit event |
| **State Ownership** | Donor owns the value until settlement; Economy owns the transfer and ledger; the ARL owns a receipt and accounting record in `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` categories, not treasury ownership, custody, capacity or a general withdrawal balance |
| **Authorized Actors** | Authenticated owner of the donating nation; no alliance actor may initiate a donation on a nation's behalf |
| **Permission Requirement** | None beyond authenticated nation ownership and confirmation |
| **National Player Consent** | Mandatory explicit confirmation of donor, receiver, asset, amount and irrevocability; no inferred, scheduled or membership-derived consent |
| **Resource Impact** | Moves the exact donated amount atomically; mints nothing; no fee, cap, minimum or cooldown exists without an explicit owner decision. No capacity limit is assumed and a valid donation is never rejected for lack of an approved capacity model |
| **Security Boundary** | **MANDATORY INVARIANT:** a compulsory deduction may never be recorded as a donation; automatic tax withholding, a voluntary donation and every other ordinary transfer are distinct transaction classes and never substitute for one another; a donation never authorizes a general withdrawal, distribution or player payment; duplicate keys never double-debit; a donation is never treated as new production or taxed as production. The only permitted debit of donated value is a purpose-limited operational platform-cost expense under `AX-27`/`F-AL-008`, never a refund or transfer to a player; because no cost schedule is approved today, donated value remains in the ARL and no actual debit is available |
| **Failure Behaviour** | Insufficient donor value, an unsupported or invalid asset, missing, failed or stale authenticated authorization or confirmation, a duplicate settlement that conflicts with the original receipt, or a technical ARL credit failure rejects the whole donation with `ALF-24` and no movement; an exact replay returns the original receipt; absence of a capacity model is not a failure |
| **Recovery Responsibility** | Economy returns the original receipt for a replayed idempotency key and keeps balances unchanged; Alliance records the failure and notifies the donor; no value is silently dropped |
| **Unresolved Decision** | `UD-046` (treasury ownership, custody, capacity, general withdrawal, general spending, distributions and dual approval remain Open; this contract creates no general withdrawal, distribution or ownership right) |
| **Status** | **Binding Owner-Authorized Constraint (`D-140`); no limits, fees or capacity invented; ARL receives and accounts for the credit; general treasury policy Open under `UD-046`** |

---

### AX-29 — Alliance-to-Alliance Treaties and NAP Consent

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-29` |
| **Integration Title** | Alliance-to-Alliance Treaties and NAP Consent |
| **Alliance Capability** | Propose, approve, activate, amend and terminate a separate Alliance-to-Alliance treaty, including an enforced `AT-T01` non-aggression pact. Coverage is the recorded set of consenting nations; a member that declines is a non-covered member |
| **Owning Subsystem** | Alliance System (`B-09`) as a new object; National Diplomacy (`B-08`) retains exclusive ownership of nation treaties |
| **Canonical External Rule** | `DIP-039`, `DIP-147`, `DIP-150`, `REQ-530`, `D-137` as amended by `D-140` |
| **Alliance Internal Rule** | `ALL-123`, `ALL-196`–`ALL-208`, `ALL-217` |
| **Relevant REQ IDs** | `REQ-633`–`REQ-644` (DIRECT) |
| **Related Decision IDs** | `D-140`, `DD-162`; `D-137` (amended in part); `UD-040`, `UD-042`, `UD-044`, `UD-047` remain Open |
| **Related Formula IDs** | None (no treaty formula is created) |
| **Inputs Received** | Both alliance identities, registered type (`AT-T01`–`AT-T05`), exactly one registered effect (`AT-E00` record-only or `AT-E01` NAP), structured terms version, each alliance's lawful approval, each affected nation's authenticated consent, current membership records, turn number |
| **Outputs Provided** | `alliance_agreement_id`, immutable version record, consent ledger, covered-nation set containing exactly the recorded consenting nations, public treaty record, lifecycle audit events, `AT-E01` NAP coverage set consumed by `AX-30`; non-consenting members remain members and are recorded as non-covered; an `AT-E00` treaty is archived as a record-only diplomatic record and supplies no coverage set |
| **State Ownership** | Alliance System owns the treaty object and its lifecycle; Nation and B-08 own national treaties; neither alliance treaty mutates a national agreement |
| **Authorized Actors** | Constitution-authorized alliance actors for proposal and approval; each affected nation owner for national consent |
| **Permission Requirement** | Constitution-defined treaty authority; no diplomatic delegation is created |
| **National Player Consent** | Mandatory explicit authenticated consent per affected nation and per version for a nation to be **covered**; silence, inactivity, default membership, ballot, office or majority never consents. Declining or withholding consent must not deny admission, remove membership, impose a cooldown, fine or punishment, or make the nation ineligible |
| **Resource Impact** | None for `AT-E01`. `AT-E00` is explicitly record-only and executes nothing; `AT-T02`–`AT-T05` currently select only `AT-E00`, and any future executable effect must be registered separately before it can act. Custom prose is descriptive and never executable. No treaty moves value outside the canonical transfer contract or creates a tariff, fee or market channel |
| **Security Boundary** | **MANDATORY INVARIANT:** no reuse or mutation of a B-08 object; no national diplomatic agency; no silent extension to a joining nation; no automatic coverage from membership; no waiver of an active NAP; free text cannot create an attack ban, financial power, withdrawal right, distribution or delegation; only a registered structured effect can execute, and only `AT-E01` may restrict an attack; dissolution of either party terminates the bilateral treaty as a whole at the dissolution boundary |
| **Failure Behaviour** | A missing alliance approval rejects activation (`ALF-25`). A nation without recorded consent is excluded from the covered set rather than blocked from membership; an attempt to bind it fails closed. An unknown or unregistered type or effect is rejected with `ALF-25`; an explicitly registered `AT-E00` record-only treaty is valid and executes nothing; `AT-T01` cannot be record-only. A joining nation is never automatically added |
| **Recovery Responsibility** | Alliance System keeps the prior version in force, records the failure, and notifies both alliances; no partial activation and no retroactive coverage |
| **Unresolved Decision** | `UD-047` (binding collective diplomatic positions and any delegation model remain Open; no delegation is granted); `UD-042` (native ballot authorization remains Open); `UD-044` (membership rights and expulsion/appeal remain Open); `UD-040` (multi-membership remains Open) |
| **Status** | **Binding Owner-Authorized Constraint (`D-140`, `DD-162`); separate object, registered `AT-E00`/`AT-E01` effects, recorded covered set, non-covered membership allowed, zero delegation; `UD-047` Open** |

---

### AX-30 — Same-Alliance and Alliance-NAP Attack Validation

| Field | Contract Specification |
|---|---|
| **AX ID** | `AX-30` |
| **Integration Title** | Same-Alliance and Alliance-NAP Attack Validation |
| **Alliance Capability** | Supply the canonical server-side attack validator with independent, cumulative shared-membership and active-NAP restrictions for every attack path |
| **Owning Subsystem** | Warfare and Military Systems (`B-10`, future) consuming Alliance membership and treaty state (`B-09`) |
| **Canonical External Rule** | Prompt 10 (Warfare) attack-validation contract; `TR-024`, `TR-029` turn lattice |
| **Alliance Internal Rule** | `ALL-206`, `ALL-209`, `ALL-210`, `ALL-211`, `ALL-212`, `ALL-213`, `ALL-214`, `ALL-215` |
| **Relevant REQ IDs** | `REQ-642`, `REQ-645`, `REQ-646`, `REQ-647` (DIRECT) |
| **Related Decision IDs** | `D-140`, `DD-163`; `UD-040` (multi-membership policy) remains Open |
| **Related Formula IDs** | None |
| **Inputs Received** | Attacker and defender nation IDs, attack type and parameters, current membership records, active `AT-T01` records selecting `AT-E01` and their covered-nation sets, submission turn and execution turn; an `AT-E00` record-only treaty supplies no coverage input |
| **Outputs Provided** | Allow or reject decision from one canonical validator for every attack method, interface, API, handler and service route; block reason naming the shared alliance or active NAP and the covered nation; **mandatory** `AUD-AL-017` block event for every rejected attempt; zero state mutation on rejection |
| **State Ownership** | Alliance System owns membership and treaty coverage; Prompt 10 owns the attack action and its state mutation |
| **Authorized Actors** | B-10 attack submission path only; no player, officer or administrator may override the decision |
| **Permission Requirement** | Prompt 10 attack authority, always subordinate to the validator |
| **National Player Consent** | Not applicable to the same-alliance ban (membership-derived); NAP coverage requires the consents recorded under `AX-29`; non-covered nations are neither protected nor restricted by that NAP |
| **Resource Impact** | A rejected attack consumes no crowns, resources, readiness, Operations Points or units, and applies no damage |
| **Security Boundary** | **MANDATORY INVARIANT:** enforcement is server-side only; every attack method, interface, API, handler and service route calls the one validator; UI hiding or a client check is not enforcement. The same-Alliance check and the NAP check are evaluated **independently and cumulatively**: leaving a shared alliance does not bypass an active NAP, and an expired or non-covering NAP does not permit a same-Alliance attack. Only an active `AT-T01` selecting `AT-E01` supplies NAP coverage; `AT-E00` and any future unregistered effect supply none. Audit logging of a block is mandatory and independent of optional audit settings |
| **Failure Behaviour** | The validator fails closed with `ALF-26`; no partial execution, no retroactive sanction, no confiscation. If membership changed between submission and execution, the execution-time state governs |
| **Recovery Responsibility** | Prompt 10 aborts the attack before execution and returns the plain-language reason; Alliance supplies current state at submission and settlement and writes the mandatory block event |
| **Unresolved Decision** | `UD-040` (multi-membership admission policy remains Open; this contract defines the attack result for every combination without deciding it); `UD-047` (collective position policy remains Open) |
| **Status** | **Binding Design Contract (`D-140`, `DD-163`); Prompt 10 runtime enforcement not implemented; every entry point must call the validator and every block must write `AUD-AL-017`; only `AT-E01` supplies NAP coverage; `UD-040` Open** |
