# 09A — Cross-System Integration Matrix (Prompts 01–08C)

**Companion to:** `09A_alliance_research.md`
**Version:** 1.4 — corrected by Prompt 09A-F (2026-10-31)
**Purpose:** Record every Alliance integration with the completed Stage 2 work, using the 20 required fields, without changing any owning system's rules.
**Status:** Research record. No integration in this matrix is implemented, and no candidate requirement is approved by being listed.

---

## 1. How to read this matrix

- `AX-##` is an integration ID, not a requirement or a decision.
- **Owning system** is the canonical owner of the rule. Alliance may consume or expose data; it may not rewrite the rule.
- Fields 1–11 are in §2; the requirement-level semantic audit is in §3; fields 12–20 are in §4.
- §3 is authoritative for the **relationship** between an AX record and each cited requirement. A requirement ID appearing in §2 is not a claim of direct dependency; §3 states the classification and the evidence.
- "Deferred" means the integration is acknowledged but intentionally not specified in 09A/09B's first release.
- Any change to an owning rule requires an owner decision (`D-###`) and must not be smuggled in as an Alliance requirement.
- A row marked **NO EXISTING REQUIREMENT** does not transfer ownership of that behaviour to Alliance. The owner named in §2 remains the owner; Alliance records the interface and the required decision.

### 1.1 Relationship classifications

| Classification | Meaning | Validator rule |
|---|---|---|
| **DIRECT DEPENDENCY** | The existing requirement establishes a rule or capability on which the Alliance integration directly depends. | Must carry specific evidence naming the requirement's actual rule. |
| **RELATED CONSTRAINT** | The requirement establishes a restriction or boundary relevant to the integration but does not define the integration itself. | Must not be described as the source of the integration. |
| **SUPPORTING CONTEXT** | The requirement provides useful background but does not establish a dependency. | Cannot justify a rule on its own. |
| **NO VALID RELATIONSHIP** | The cited requirement does not substantively support the integration. | Must not remain in the canonical matrix. |
| **OWNER DECISION REQUIRED** | The integration needs new behaviour or a change that has not been approved. | Names the `UD-###` or `D-###` route. |

`NO EXISTING REQUIREMENT — NEW ALLIANCE REQUIREMENT OR OWNER DECISION REQUIRED.` is used where no existing requirement supports the integration at all. It is not a fifth relationship class; it is the absence of a relationship plus the required follow-up.

### 1.2 Audit basis

Every cited requirement was read in `03_requirements_traceability.md` with its title, statement, status, source and owning Bible section. Requirement titles are reproduced in §3. A title containing the word "alliance", "nation", "resource" or "diplomacy" was never sufficient; the test was whether the rule's actual subject supports the integration.

**Inspected canonical groups:** Prompt 01 (roadmap/scope), 02 (foundations, turn order, visibility), 03 (nation/identity/dormancy), 04 (economy/ledger), 05 (cities/development/research), 06 (population/approval/elections/crisis), 07A (market research), 07B (market rules), 07C (Global Trade + gates), 08A (diplomacy research), 08B (`15_diplomacy.md` incl. §18), 08C + 08C-C/D/E (`15_diplomacy_workflows_acceptance.md`).

**Semantic review record:** `09A_alliance_reference_review.md`. It records the reviewer, the limits of automated checks, and the per-AX conclusion. It is a self-review by the project author, not an independent review.

---

## 2. Fields 1–11 — integration summary

| ID | Integration title | Alliance capability | Owning system | Prompt / canonical document | Requirements and classifications (detail in §3) | Behaviour already approved? | New proposed functionality? | Owner decision required? | Mandatory / optional / deferred |
|---|---|---|---|---|---|---|---|---|---|
| AX-01 | Alliance founding requires an eligible nation owner | Create alliance; founder becomes first Leader | Nation/identity (B-03) | P03; B-03 account and nation lifecycle | REQ-002 **DIRECT**; REQ-061 **DIRECT**; REQ-076 **RELATED**; no existing founding-eligibility requirement | Identity and ownership only; founding eligibility is not approved | Yes — founding eligibility, cost and cap (`REQ-535`) | Yes — `UD-040` | Mandatory |
| AX-02 | One-player-one-nation and multi-identity limits apply to alliance roles | Assign roles only to eligible nation owners | Nation/identity (B-03) | P03; B-03 §4–§5 | REQ-061 **DIRECT**; REQ-043 **DIRECT**; REQ-004 **DIRECT**; REQ-031 **RELATED** | Identity policy approved; enforcement mechanism open; role model new | Yes — capability model (`REQ-552`–`REQ-561`) | Yes — `UD-045` | Mandatory |
| AX-03 | Dormant or retired founder/leader does not freeze alliance | Trigger a vacancy/succession path on lifecycle events | Nation/lifecycle (B-03) | P03; B-03 §9/§13; D-028 | REQ-091 **DIRECT**; REQ-085 **DIRECT**; REQ-013 **RELATED** | Dormancy and reroll rules approved/provisional | Yes — alliance vacancy path (`REQ-548`) | Yes — `UD-043` | Mandatory |
| AX-04 | Leadership, succession and office vacancy | Define offices, succession and removal | Alliance governance (B-09) + B-03 event | P03 + B-09; D-028; DIP-146 | REQ-013 **DIRECT**; REQ-085 **DIRECT**; REQ-091 **RELATED** | No — `REQ-013` is Open | Yes — office and succession rules (`REQ-542`–`REQ-551`) | Yes — `UD-012`, `UD-043` | Mandatory |
| AX-05 | Permission changes and role grants | Grant, revoke and audit capabilities | Alliance governance (B-09) | B-09; DIP-146 | REQ-013 **DIRECT**; REQ-004 **DIRECT**; REQ-027 **DIRECT** | No — only the obligation in `REQ-013` is canonical | Yes — capability catalogue (`REQ-552`–`REQ-561`) | Yes — `UD-045` | Mandatory |
| AX-06 | Treasury deposits of already-owned resources | Accept a member transfer into a segregated pool | Economy/ledger (B-04) | P04; B-04 §13/§16/§22 | REQ-176 **DIRECT**; REQ-005 **DIRECT**; REQ-154 **DIRECT**; REQ-170 **DIRECT** | Economy conservation and ledger rules exist; pool is not implemented | Yes — treasury deposit (`REQ-571`–`REQ-572`) | Yes — `UD-046` | Mandatory if treasury ships |
| AX-07 | Treasury withdrawals, grants and loans | Authorise and record a pool draw | Economy/ledger (B-04) | P04; B-04 §12–§16 | REQ-013 **DIRECT**; REQ-176 **DIRECT**; REQ-005 **DIRECT**; REQ-153 **DIRECT**; REQ-170 **DIRECT** | No — `REQ-013` is Open; no withdrawal model exists | Yes — propose/approve/execute (`REQ-556`, `REQ-573`–`REQ-575`) | Yes — `UD-046` | Mandatory if treasury ships |
| AX-08 | Alliance resource storage limits | Determine whether a separately approved Alliance Treasury capacity rule is required; national warehouse capacity does not establish Alliance-pool capacity | Economy/warehouse (B-04) | P04; B-04 §13/§22 | REQ-176 **DIRECT**; REQ-141 **RELATED**; REQ-142 **RELATED**; no existing alliance-pool capacity requirement | Storage rules exist for national warehouse; pool capacity and over-capacity deposit behaviour are not approved | Yes, if a separate pool capacity is chosen | Yes — `UD-046` | Optional |
| AX-09 | Applications, acceptance, rejection and withdrawal | Run an authoritative membership application | Alliance membership (B-09) | B-09; no existing canonical rule | REQ-002 **SUPPORTING CONTEXT**; no existing application/membership requirement | No | Yes — application lifecycle (`REQ-562`–`REQ-570`) | Yes — `UD-044` | Mandatory |
| AX-10 | Field-level visibility of profile and applicant data | Classify each profile/applicant field | Foundations/visibility (B-02) | P02; 07 §9; REQ-057 | REQ-057 **DIRECT** | Yes — visibility classes are canonical (Provisional) | Mapping only; no new privacy model | No — `UD-044` may set the applicant-list default | Mandatory |
| AX-11 | City/development support programmes | Transfer already-owned value to a member's development | Cities/development (B-05) + Economy (B-04) | P05; B-05 §23; B-04 §22 | REQ-172 **DIRECT**; REQ-218 **RELATED**; REQ-005 **RELATED** | City costs and pacing are provisional; no alliance programme exists | Yes — support as a transfer (`REQ-575`) | Yes — `UD-046` (grant/loan controls) | Optional |
| AX-12 | Readiness/activity declarations for members | Collect voluntary readiness declarations | Nation/activity (B-03) + future military (B-10) | P03/P06; B-03 §13 | REQ-091 **SUPPORTING CONTEXT**; REQ-023 **RELATED**; no existing readiness requirement | Dormancy and collection limits exist; readiness declarations do not | Yes — `REQ-587` | Yes — `UD-044`/`UD-049` | Optional |
| AX-13 | Population/approval effects of alliance membership | None assumed; possible future input | Population/approval (B-06) | P06A | No existing requirement establishes any alliance effect | No effect is approved | No — deferred, no candidate effect | Yes, if any effect is ever proposed | Deferred |
| AX-14 | Elections/crisis interaction with alliance offices | Alliance office identity must not override nation politics | Nation politics (B-06) | P06B; B-06 Part II | REQ-326 **SUPPORTING CONTEXT**; no existing requirement defines the interaction | B-06 owns elections/crisis; the interaction is undefined | No — deferred | Yes, if an interaction is proposed | Deferred |
| AX-15 | National treaties persist through alliance join/leave/removal | Membership change is not a treaty event | Diplomacy (B-08) | P08B `15_diplomacy.md` §18; DIP-146–149 | REQ-530 **DIRECT**; REQ-523 **DIRECT**; REQ-531 **RELATED**; persistence is `DIP-147`, not a REQ | Yes — `DIP-147` and `REQ-530` are canonical | No new Alliance rule; the integration is a boundary | No | Mandatory (constraint) |
| AX-16 | Alliance diplomatic positions (non-binding) | Publish a position; never bind a nation | Diplomacy (B-08) + B-09 publication | P08B §18; 08A §13 | REQ-530 **DIRECT**; REQ-523 **RELATED**; REQ-531 **RELATED**; no existing position requirement | National authority approved; alliance position is not | Yes — `REQ-579`–`REQ-580` | Yes — `UD-039`, `UD-047` | Optional |
| AX-17 | Embargo and restricted-pair checks on alliance-mediated transfers | Run the same checks as a direct transfer | Diplomacy (B-08) + Economy (B-04) | P08B; B-04 §21–§22 | REQ-529 **DIRECT**; REQ-175 **DIRECT**; REQ-170 **DIRECT** | Yes — embargo and transfer rules are canonical | No new rule; the integration is a constraint (`REQ-576`) | No | Mandatory (constraint) |
| AX-18 | War/coordination information | Publish coordination information; never execute | Military (B-10, future) | P10 (future) | REQ-014 **RELATED**; REQ-518 **RELATED**; no existing coordination requirement | War rules do not exist yet | Yes, but deferred | Yes — Prompt 10 owns the interface | Deferred |
| AX-19 | Static Discord invite link | Store one optional external URL | Alliance profile (B-09) + platform security (B-12) | B-09; D-133; DD-147/DD-148 | REQ-057 **RELATED**; no existing link requirement | `D-133`/`DD-147` approve the exclusion; `DD-148` is Provisional | Yes — `REQ-598`–`REQ-603` | Yes — `UD-048` | Optional |
| AX-20 | Announcements and formal notices | Publish asynchronous alliance notices | Alliance (B-09) | B-09 | REQ-057 **RELATED**; REQ-021 **SUPPORTING CONTEXT**; no existing announcement requirement | No | Yes — `REQ-586`, `REQ-606` | Yes — `UD-049` | Optional |
| AX-21 | Audit and history of alliance actions | Record consequential acts immutably | Alliance (B-09) + platform audit (B-12) | B-09; P02; D-026 | REQ-027 **DIRECT**; REQ-021 **DIRECT**; REQ-153 **DIRECT**; REQ-013 **RELATED** | Audit-spine and append-only rules are canonical (Provisional) | Yes — alliance audit schema (`REQ-609`–`REQ-613`) | No — `D-026` applies | Mandatory |
| AX-22 | Rankings/chronicle aggregates | Supply alliance aggregates to a future rankings system | Rankings (B-11, future) | P11 (future) | REQ-058 **SUPPORTING CONTEXT**; no existing alliance-ranking requirement | Bounded history exists; rankings do not | Yes, but deferred | Yes — Prompt 11 owns the metric | Deferred |
| AX-23 | Fair-play/moderation of alliance conduct | Report evidence; no enforcement power | Moderation (B-12, future) | P12 (future) | REQ-025 **DIRECT**; REQ-026 **DIRECT**; REQ-027 **DIRECT** | Moderation principles are canonical (Provisional); no alliance procedure | Yes, but deferred | Yes — Prompt 12 owns procedure | Deferred |
| AX-24 | Notifications and UI surfaces | Emit alliance event types | Interface (B-13, future) | P13 (future) | REQ-020 **SUPPORTING CONTEXT**; no existing notification-taxonomy requirement | No | Yes, but deferred | Yes — Prompt 13 owns taxonomy | Deferred |
| AX-25 | Formula and balance registration | Register any alliance formula candidate | Formula register (B-14, future) | P14 (future) | REQ-163 **DIRECT**; REQ-098 **RELATED**; REQ-047 **RELATED** | The register is canonical; no alliance formula exists | Yes, but deferred | Yes — Prompt 14 owns balance | Deferred |
| AX-26 | Global Trade interaction | Consume market/trade context; create no channel | Market/Global Trade (B-07) | P07C; D-122; DD-136 | REQ-513 **DIRECT**; REQ-010 **DIRECT**; no existing alliance-trade requirement | Global Trade is approved scope but release-gated; G-1…G-6 unchanged | No new trade channel | No — D-122 decides scope | Mandatory (constraint) |

---

## 3. Requirement-level semantic audit

One row per AX-to-requirement relationship. `—` in the REQ column is the explicit "no existing requirement" marker. Every DIRECT row states what the requirement actually establishes.

| AX | REQ ID | Requirement title (faithful) | Classification | Exact evidence / explanation | Approved behaviour? | Owner decision |
|---|---|---|---|---|---|---|
| AX-01 | REQ-002 | Each nation has exactly one owning account; ownership is checked on every action | **DIRECT DEPENDENCY** | Founding must resolve a real owning account for the founder; `REQ-002` is the canonical ownership check, so the alliance cannot be created for an unowned or spoofed nation. | Provisional | — |
| AX-01 | REQ-061 | Exactly one active nation per account at all times | **DIRECT DEPENDENCY** | The founder is an active nation owner; `REQ-061` establishes the one-active-nation state that eligibility must read. | Provisional | — |
| AX-01 | REQ-076 | The account owns the nation; a nation is never re-parented, claimed or transferred | **RELATED CONSTRAINT** | Prevents founding on behalf of, or transferring a nation into, another account. It does not define founding eligibility. | Provisional | — |
| AX-01 | — | No existing requirement defines founding eligibility, cost or cap | **NO EXISTING REQUIREMENT** | `REQ-535` is a 09A candidate, not an approved rule. `UD-040` must settle eligibility, cost and whether a nation may belong to more than one alliance. | No | `UD-040` |
| AX-02 | REQ-061 | Exactly one active nation per account at all times | **DIRECT DEPENDENCY** | A role is held by one active nation; the one-active-nation rule is the identity basis for a role grant. | Provisional | — |
| AX-02 | REQ-043 | Only one account per person is permitted (policy now; enforcement later) | **DIRECT DEPENDENCY** | The policy is the rule the alliance role model must not undermine; it is approved as policy, with enforcement explicitly open. | Approved (policy) | — |
| AX-02 | REQ-004 | Every valuable verb resolves the actor's nation and role server-side before mutation | **DIRECT DEPENDENCY** | A role grant or capability check is a valuable verb; it must resolve the actor and role server-side. | Provisional | — |
| AX-02 | REQ-031 | Multi-account and collusion policy is declared and behaviourally enforced, with appeals | **RELATED CONSTRAINT** | States that enforcement exists as a requirement but is Open; it neither defines alliance roles nor supplies an enforcement mechanism. | Open | Prompt 12 (mechanism) |
| AX-03 | REQ-091 | Dormant nations remain addressable and ranked per D-028; return needs no new account; the turn clock is unaffected | **DIRECT DEPENDENCY** | The dormancy state and return path are the events the alliance vacancy rule must consume; the alliance cannot invent a second inactivity state. | Provisional | — |
| AX-03 | REQ-085 | Reroll cleanup across warfare, trade, diplomacy, alliances, rankings, operations and notifications is deterministic | **DIRECT DEPENDENCY** | Explicitly names alliances: a rerolled leader's offices must be cleaned deterministically. This is the event-handling dependency, not a succession rule. | Provisional | — |
| AX-03 | REQ-013 | Alliances have explicit roles, audited pool draws and a succession rule before any pool exists | **RELATED CONSTRAINT** | Requires a succession rule to exist; it does not define the dormancy trigger or the vacancy path. | Open | `UD-012`, `UD-043` |
| AX-04 | REQ-013 | Alliances have explicit roles, audited pool draws and a succession rule before any pool exists | **DIRECT DEPENDENCY** | The only canonical requirement that directly obliges alliance roles and succession; it is Open, so the integration cannot be specified without an owner decision. | Open | `UD-012`, `UD-043` |
| AX-04 | REQ-085 | Reroll cleanup across ... alliances ... is deterministic | **DIRECT DEPENDENCY** | A leader's reroll must vacate offices deterministically; founding a succession model without consuming this event would leave stale authority. | Provisional | — |
| AX-04 | REQ-091 | Dormant nations remain addressable ... return needs no new account | **RELATED CONSTRAINT** | Supplies the dormancy/return behaviour the vacancy rule must not contradict; it does not define office succession. | Provisional | — |
| AX-05 | REQ-013 | Alliances have explicit roles, audited pool draws and a succession rule before any pool exists | **DIRECT DEPENDENCY** | Establishes explicit roles and audited draws as an obligation; capability grants are the mechanism that discharges it. | Open | `UD-045` |
| AX-05 | REQ-004 | Every valuable verb resolves the actor's nation and role server-side before mutation | **DIRECT DEPENDENCY** | A permission change must be authorised server-side from the actor's resolved role, not from client state. | Provisional | — |
| AX-05 | REQ-027 | A permanent audit spine records every value mutation, pipeline phase, privileged act and moderation act | **DIRECT DEPENDENCY** | A permission grant is a privileged act; the audit spine is the canonical record, so `REQ-027` supports the audit requirement directly. | Provisional | — |
| AX-06 | REQ-176 | Prompt 09 alliance pools are separate audited pools and may not mint or bypass restrictions | **DIRECT DEPENDENCY** | The only canonical requirement written specifically for the Prompt 09 pool. It establishes separate audited pools, no minting and no bypass — exactly the deposit boundary. | Provisional | — |
| AX-06 | REQ-005 | Treasury conserves under C1–C4; no negative balance; commitments reserve before spend | **DIRECT DEPENDENCY** | A deposit must conserve value and cannot create a negative balance; the pool is not a second mint. | Provisional | — |
| AX-06 | REQ-154 | The ledger records the declared event types for every monetary and resource change | **DIRECT DEPENDENCY** | A deposit that moves value must write a declared ledger event; otherwise the pool balance is not reconstructable. | Provisional | — |
| AX-06 | REQ-170 | Shared-network restrictions apply to every value-moving economic action | **DIRECT DEPENDENCY** | A deposit is a value-moving economic action, so restricted-pair checks apply to it. | Provisional | — |
| AX-07 | REQ-013 | Alliances have explicit roles, audited pool draws and a succession rule before any pool exists | **DIRECT DEPENDENCY** | Explicitly requires audited pool draws; a withdrawal is the draw the requirement governs. | Open | `UD-046` |
| AX-07 | REQ-176 | Prompt 09 alliance pools are separate audited pools and may not mint or bypass restrictions | **DIRECT DEPENDENCY** | A withdrawal must not bypass restrictions and must remain reconstructable from the pool's audit. | Provisional | — |
| AX-07 | REQ-005 | Treasury conserves under C1–C4; no negative balance; commitments reserve before spend | **DIRECT DEPENDENCY** | The pool cannot overdraw; a withdrawal reserves and then moves value under the Economy rules. | Provisional | — |
| AX-07 | REQ-153 | The economic ledger is append-only; completed events are never edited or deleted | **DIRECT DEPENDENCY** | A withdrawal history that can be edited is not auditable; the append-only ledger is the direct dependency. | Provisional | — |
| AX-07 | REQ-170 | Shared-network restrictions apply to every value-moving economic action | **DIRECT DEPENDENCY** | A withdrawal is value-moving; the same restricted-pair checks must run. | Provisional | — |
| AX-08 | REQ-176 | Prompt 09 alliance pools are separate audited pools and may not mint or bypass restrictions | **DIRECT DEPENDENCY** | Establishes that alliance pools are separate audited pools with their own ledger and permissions, and must not mint or bypass restrictions; this directly establishes separate-pool ownership, auditability and resource integrity boundaries, but does not define an unapproved numerical capacity limit. | Provisional | — |
| AX-08 | REQ-141 | One shared warehouse capacity holds all 11 resources; no per-resource cap and no decay by default | **RELATED CONSTRAINT** | Establishes national warehouse storage capacity (ECN-120) for national inventory; national warehouse storage rules may inform future Alliance design but do not establish the Alliance Treasury's own capacity or storage limits. | Provisional | — |
| AX-08 | REQ-142 | Production or purchase that would exceed storage is blocked, and no money, input or output is destroyed | **RELATED CONSTRAINT** | Governs national production and trade purchase overflow blocking (ECN-124); applies to national inventory operations and does not establish deposit restrictions, storage limits or overflow handling for a separate Alliance Treasury pool. | Provisional | — |
| AX-08 | — | No existing requirement defines alliance pool capacity or over-capacity deposit behaviour | **NO EXISTING REQUIREMENT** | Existing national warehouse capacity and production/purchase restrictions do not automatically establish Alliance Treasury storage capacity or deposit behaviour. Alliance pool capacity and over-capacity handling remain unresolved and require an explicit Alliance System design decision, coordinated with the Economy system owner. Existing related rules REQ-141, REQ-142 and REQ-176 do not establish pool limits. | No | `UD-046` |
| AX-09 | REQ-002 | Each nation has exactly one owning account; ownership is checked on every action | **SUPPORTING CONTEXT** | Confirms that an applicant is a real nation owner, but does not establish application states, acceptance or membership. | Provisional | — |
| AX-09 | — | No existing requirement defines membership, applications or acceptance | **NO EXISTING REQUIREMENT** | `REQ-562`–`REQ-570` are candidates only. The matrix cannot cite a trade or diplomacy requirement to fill this gap. | No | `UD-044` |
| AX-10 | REQ-057 | Every field carries one visibility class (public/alliance/private/restricted), and aggregates must not leak private components | **DIRECT DEPENDENCY** | The integration is precisely the mapping of alliance profile and applicant fields onto the canonical visibility classes. | Provisional | — |
| AX-11 | REQ-172 | Prompt 05 must use the B-04 recipes, reservation model, capex and ledger, and register every modifier | **DIRECT DEPENDENCY** | An alliance support programme that pays for a city build must use the same recipes, reservation, capex and ledger; it cannot invent a discount or free build. | Provisional | — |
| AX-11 | REQ-218 | Each city resolves at most one construction-class action per turn; one founding and one programme per nation | **RELATED CONSTRAINT** | A support payment cannot buy an extra construction slot; the pacing rule bounds what support can do. It does not define support. | Provisional | — |
| AX-11 | REQ-005 | Treasury conserves under C1–C4; no negative balance | **RELATED CONSTRAINT** | A transfer must conserve value, but conservation is not a city-support rule. | Provisional | — |
| AX-12 | REQ-091 | Dormant nations remain addressable ... return needs no new account | **SUPPORTING CONTEXT** | Dormancy is relevant to readiness staleness, but the requirement does not define a readiness declaration. | Provisional | — |
| AX-12 | REQ-023 | Collect only the data inventory's categories; no analytics, ads, precise location or content logging | **RELATED CONSTRAINT** | Bounds what an alliance readiness feature may collect; it does not authorise collecting readiness data. | Provisional | — |
| AX-12 | — | No existing requirement defines readiness or activity declarations | **NO EXISTING REQUIREMENT** | `REQ-587` is a candidate. A readiness feature must not infer private play activity. | No | `UD-044`/`UD-049` |
| AX-13 | — | No existing requirement gives alliance membership a population or approval effect | **NO EXISTING REQUIREMENT** | B-06 owns population and approval; 09A proposes no effect. Any effect needs a B-06 change and an owner decision. | No | Owner decision required if proposed |
| AX-14 | REQ-326 | An electoral government holds a contest every 240 shared world turns | **SUPPORTING CONTEXT** | Establishes that elections are nation-level and periodic; it does not define how an alliance office interacts with them. | Provisional | — |
| AX-14 | — | No existing requirement defines alliance-office interaction with elections or crisis | **NO EXISTING REQUIREMENT** | The safe boundary is that B-06 owns the election/crisis state and an alliance office cannot override it. No rule is created here. | No | Owner decision required if an interaction is proposed |
| AX-15 | REQ-530 | The only diplomatic authority is the authenticated owner of the active nation; no delegation to another player, an AI or an alliance office exists | **DIRECT DEPENDENCY** | Directly forbids an alliance office from signing, accepting or terminating for a member. It is the authority basis for treaty persistence through membership change. | Provisional | — |
| AX-15 | REQ-523 | A bilateral agreement exists only after both parties' authenticated owners accept the exact version; silence, expiry, dormancy, a leadership change and an administrative state are never consent | **DIRECT DEPENDENCY** | Membership change is not consent; the same requirement makes the persistence rule coherent. | Provisional | — |
| AX-15 | REQ-531 | The system never accepts, rejects, proposes, declares, sanctions, surrenders, breaks, renews or changes posture for a player | **RELATED CONSTRAINT** | Confirms that no automatic alliance event may create or void a treaty. | Provisional | — |
| AX-16 | REQ-530 | The only diplomatic authority is the authenticated owner of the active nation; no delegation ... exists | **DIRECT DEPENDENCY** | An alliance position may be published, but it cannot become diplomatic authority or consent for a member. `REQ-530` is the direct boundary. | Provisional | `UD-039`, `UD-047` |
| AX-16 | REQ-523 | Bilateral agreement requires both owners' authenticated acceptance | **RELATED CONSTRAINT** | Reinforces that a position cannot substitute for consent; it does not authorise a position record. | Provisional | — |
| AX-16 | REQ-531 | The system never acts diplomatically for a player | **RELATED CONSTRAINT** | A position must not be treated as an automatic diplomatic act. | Provisional | — |
| AX-16 | — | No existing requirement authorises an alliance diplomatic position | **NO EXISTING REQUIREMENT** | `REQ-579`–`REQ-580` are candidates. The position must be non-binding and cannot be represented as a treaty. | No | `UD-039`, `UD-047` |
| AX-17 | REQ-529 | One sanction exists: an embargo requiring HOSTILE posture, lasting 24 turns, public, blocking new directed trades and new aid only, grandfathering accepted transfers, with no fee or price change | **DIRECT DEPENDENCY** | This is the actual embargo rule. An alliance-mediated transfer must run the same embargo check; it may not create a bypass. | Provisional | — |
| AX-17 | REQ-175 | Prompt 08 movements are transfers with matched ledger events; embargoes do not destroy goods | **DIRECT DEPENDENCY** | Establishes that an embargo blocks transfers but does not destroy goods, which is exactly how the treasury check must behave. | Provisional | — |
| AX-17 | REQ-170 | Shared-network restrictions apply to every value-moving economic action | **DIRECT DEPENDENCY** | Treasury transfers are value-moving and therefore subject to the same pair checks. | Provisional | — |
| AX-18 | REQ-014 | Strategic orders exist only with a war rule set, protection states and settlement enforcement | **RELATED CONSTRAINT** | Explains why no alliance military integration can be specified before Prompt 10; it does not authorise coordination features. | Deferred | Prompt 10 |
| AX-18 | REQ-518 | An active NAP prohibits a war declaration between its parties; the prohibition is enforced by Prompt 10 and is inert until Prompt 10 exists | **RELATED CONSTRAINT** | A coordination notice must not be confused with a war declaration; the war rule remains Prompt 10's. | Provisional | Prompt 10 |
| AX-18 | — | No existing requirement defines alliance war coordination | **NO EXISTING REQUIREMENT** | Deferred to Prompt 10. No alliance order may execute a military action. | No | Prompt 10 |
| AX-19 | REQ-057 | Every field carries one visibility class | **RELATED CONSTRAINT** | The Discord link needs a visibility class, but the requirement does not authorise an external link feature. | Provisional | `UD-048` |
| AX-19 | — | No existing requirement defines an external communication link | **NO EXISTING REQUIREMENT** | `REQ-598`–`REQ-603` are candidates; `DD-148` is Provisional. The link is display-only and never fetched. | No | `UD-048` |
| AX-20 | REQ-057 | Every field carries one visibility class | **RELATED CONSTRAINT** | An announcement needs an audience class; the requirement does not authorize announcements. | Provisional | `UD-049` |
| AX-20 | REQ-021 | Player-visible history is append-only; corrections are new disclosed events | **SUPPORTING CONTEXT** | Relevant if announcements are retained as history; it does not establish an announcement feature. | Provisional | — |
| AX-20 | — | No existing requirement defines alliance announcements or notices | **NO EXISTING REQUIREMENT** | `REQ-586` is a candidate; `UD-049` decides scope. Asynchronous only, with no message threads. | No | `UD-049` |
| AX-21 | REQ-027 | A permanent audit spine records every value mutation, pipeline phase, privileged act and moderation act | **DIRECT DEPENDENCY** | Alliance leadership, permission and treasury acts are privileged/value acts; the canonical audit spine is the direct dependency. | Provisional | — |
| AX-21 | REQ-021 | Player-visible history is append-only; corrections are new disclosed events | **DIRECT DEPENDENCY** | Alliance history must follow the same append-only correction model. | Provisional | — |
| AX-21 | REQ-153 | The economic ledger is append-only; completed events are never edited or deleted | **DIRECT DEPENDENCY** | Treasury audit rows that record value movements must follow the append-only ledger rule. | Provisional | — |
| AX-21 | REQ-013 | Alliances have explicit roles, audited pool draws and a succession rule | **RELATED CONSTRAINT** | Requires audited draws; it does not define the general alliance audit schema. | Open | `UD-045` |
| AX-22 | REQ-058 | History is bounded: one digest row per nation-turn, permanent rows only for class-P events | **SUPPORTING CONTEXT** | Bounds what a future alliance aggregate could read; it does not define an alliance ranking. | Provisional | — |
| AX-22 | — | No existing requirement defines alliance rankings or chronicle aggregates | **NO EXISTING REQUIREMENT** | Deferred to Prompt 11. Alliance-controlled transfers must not inflate standings. | No | Prompt 11 |
| AX-23 | REQ-025 | Moderation is evidence-based, logged, proportionate and role-scoped | **DIRECT DEPENDENCY** | Any alliance conduct report must follow the canonical moderation principles. | Provisional | — |
| AX-23 | REQ-026 | Appeals are possible and decided with a reason; overturns are reviewed | **DIRECT DEPENDENCY** | An alliance sanction or report needs the canonical appeal path. | Provisional | — |
| AX-23 | REQ-027 | A permanent audit spine records every ... moderation act | **DIRECT DEPENDENCY** | The permanent audit spine is the canonical record for every moderation act; an alliance report, sanction or enforcement decision must be written there rather than in a separate alliance-only log. | Provisional | — |
| AX-24 | REQ-020 | Every resolved delta is visible with provenance; failures explain and release reservations | **SUPPORTING CONTEXT** | A future notification/UI surface must show provenance; the requirement does not define the taxonomy. | Provisional | — |
| AX-24 | — | No existing requirement defines notification taxonomy for alliances | **NO EXISTING REQUIREMENT** | Deferred to Prompt 13. The surface must not become a chat surface. | No | Prompt 13 |
| AX-25 | REQ-163 | The formula register is the single authoritative definition of every formula | **DIRECT DEPENDENCY** | Any alliance formula candidate must be registered there; 09A invents none. | Provisional | — |
| AX-25 | REQ-098 | The economy has one authoritative specification and one formula register; no competing formula definition exists | **RELATED CONSTRAINT** | Forbids a second treasury/economy formula set inside B-09. | Provisional | — |
| AX-25 | REQ-047 | Approved, provisional and unresolved states stay distinguishable; no document claims implementation, security or balance as proven | **RELATED CONSTRAINT** | Applies to any alliance balance claim; it does not define a formula. | Approved (project rule) | — |
| AX-26 | REQ-513 | Global Trade is required for the intended complete game, distinct from directed trades, and stays on the authoritative roadmap subject to G-1…G-6 | **DIRECT DEPENDENCY** | The Alliance System may consume trade context but must not bypass the gates or create an alternate trade channel. | Approved | — |
| AX-26 | REQ-010 | A listings market exists only after gates G-1…G-6 are met | **DIRECT DEPENDENCY** | An alliance trade feature cannot open a listings market before the gates. | Deferred | — |
| AX-26 | — | No existing requirement defines an alliance-mediated trade channel | **NO EXISTING REQUIREMENT** | None is proposed. Alliance features must not create a trade channel. | No | — |

---

## 4. Fields 12–20

| ID | Authorized actors | Permissions required | Player consent | Resource/economic impact | Failure & recovery | Security/abuse risk | Mandatory / optional / deferred | Open questions | Recommended ownership boundary |
|---|---|---|---|---|---|---|---|---|---|
| AX-01 | Any eligible nation owner | Founding capability (implicit owner) | Yes (own nation) | Possible founding cost (`UD-040`) | Creation is atomic; failure leaves no orphan alliance | Name squatting, impersonation | Mandatory | Cost? cooldown? cap? | B-09 owns creation; B-03 supplies eligibility |
| AX-02 | Founder/Leader | `roles.assign` | Target accepts role | None | Revoke on failure | Alt-role stacking | Mandatory | Should alt checks be per-alliance? | B-03 owns identity; B-09 enforces at assignment |
| AX-03 | System + successor | `succession.trigger` (system) | No (protective) | None | Manual owner override path | Premature takeover | Mandatory | Threshold consistency with D-028 | B-03 emits event; B-09 applies succession |
| AX-04 | Leader, system | `leadership.transfer`, `leadership.remove` | Removal may need council vote (`UD-043`) | None | Freeze sensitive actions during vacancy | Coup, lockout | Mandatory | Who removes a captured Leader? | B-09 owns offices; B-03 owns existence events |
| AX-05 | Holder of `roles.manage` | `roles.manage` + re-auth | No | None | Roll back partial changes; audit | Privilege escalation | Mandatory | Should grants expire? | B-09; platform auth supplies re-auth |
| AX-06 | Any member; finance officer for recorded deposit | `treasury.deposit` | Yes (depositor owns assets) | Moves owned value into pool | Idempotent deposit key; reconcile on retry | Laundering, alt funding | Mandatory (if treasury ships) | Minimum deposit? | Economy moves value; B-09 records intent |
| AX-07 | Finance officer + approver(s) | `treasury.withdraw`, `treasury.approve` | Depositor consent not implied; member consent for grants | Moves pool value out | Two-phase: reserve → commit; reverse on failure | Theft, collusion, evasion | Mandatory (if treasury ships) | Limits? dual approval threshold? | Economy validates; B-09 authorizes; ledger is Economy's |
| AX-08 | System | — | No | Alliance Treasury capacity unestablished; national warehouse capacity cannot be substituted; storage impact subject to UD-046; no capacity formula approved | Over-capacity deposit behaviour is unresolved under UD-046 (do not assume rejection, partial acceptance, queuing, resource loss or any other outcome; Prompt 09B must define policy) | Storage exploit | Optional | Is separate capacity needed? Over-capacity deposit behaviour? Shared vs per-resource? | Economy owns value/storage rules; B-09 owns authorization; UD-046 in 09B |
| AX-09 | Recruitment officer | `members.applications.manage` | Applicant applies voluntarily | None | Withdraw/expire paths | Coercion, bait alliances | Mandatory | Appeal path? reapply cooldown? | B-09 |
| AX-10 | B-09 + viewer | — | Subject's visibility choice where applicable | None | Default to most restrictive on error | Data leak | Mandatory | Default for applicant list? | P02 owns classes; B-09 maps fields |
| AX-11 | Finance/development officer | `treasury.grant` | Recipient accepts | Moves value; no free builds | Cancel before commit | Favoritism, alt farms | Optional | Grants vs loans? | P05 validates cost; Economy moves value; B-09 authorizes |
| AX-12 | Member (self-declaration); officer reads aggregate | `members.readiness.read` | Yes (self-report) | None | Stale declaration expiry | Surveillance, coercion | Optional | Retention? | B-03 owns activity; B-09 stores declaration |
| AX-13 | — | — | — | Potential approval effect | — | Hidden penalties | Deferred | Any effect at all? | P06A; no Alliance rule |
| AX-14 | P06B system | — | Per B-06 | None | — | Office used to dodge crisis | Deferred | Interaction with vacant office | P06B |
| AX-15 | Diplomacy system | — | Per DIP rules | None | Membership change is not a treaty event | Treaty laundering via alliance | Mandatory (constraint) | None | Diplomacy |
| AX-16 | Leader/council per `UD-047` | `diplomacy.position.publish` | No binding effect; member consent needed for anything binding | None | Withdraw position | Misrepresentation | Optional | Is a position record worth it? | Diplomacy owns acts; B-09 publishes text |
| AX-17 | Economy/Diplomacy checks | — | Per owning rules | Blocks transfer | Fail closed | Sanctions evasion | Mandatory (constraint) | None | Diplomacy/Economy |
| AX-18 | Military system; alliance reads | — | Per Military rules | None | — | Unofficial orders | Deferred | Interface shape | Military |
| AX-19 | Holder of `profile.discord.manage` | Dedicated capability | No | None | Clear/replace link; audit | Phishing, impersonation | Optional | Allowlist domains? | B-09 + platform URL policy |
| AX-20 | Announcement capability | `announcements.publish` | No | None | Edit/delete policy; retention | Spam, misinformation | Optional | Initial release? | B-09 |
| AX-21 | System | — | No | Storage | Bounded retention | Log tampering | Mandatory | Retention length? | B-09 domain; platform transport |
| AX-22 | Future system | — | No | None | — | Inflation via transfers | Deferred | Metric set | Future system |
| AX-23 | Future moderation | — | — | None | — | Weaponized reports | Deferred | — | Future system |
| AX-24 | Future UI | — | — | None | — | Notification spam | Deferred | — | Future system |
| AX-25 | P14 | — | — | — | — | — | Deferred | Which formulas? | P14 |
| AX-26 | Market/Global Trade | Per P07C | Per P07C | Trade value | Per P07C | Gate bypass | Mandatory (constraint) | None | Market/Global Trade |

---

## 5. Ownership-boundary conclusions

1. **B-09 owns**: alliance identity, membership state, roles/capabilities, internal governance records, treasury *authorization*, announcements, positions, audit of alliance actions.
2. **B-03 owns**: nation existence, player identity, dormancy, retirement; B-09 only reacts to its events.
3. **B-04 owns**: resource value, ledger postings, transfer validation, storage capacity; B-09 never writes balances.
4. **B-08 owns**: relationship states, proposals, consent, treaties, embargoes; B-09 never creates or modifies a treaty.
5. **B-06 owns**: nation elections, approval, crisis; B-09 never overrides them.
6. **B-07/Global Trade owns**: market rules and release gates; B-09 creates no trade channel.
7. **P02 owns**: turn order, visibility classes, idempotency; B-09 declares its place in that order.
8. **Future B-10 owns**: military execution; B-09 provides coordination information only.
9. **B-05 owns**: city costs, construction pacing, development capacity; B-09 may only authorize a transfer of already-owned value to a member.
10. **B-12 owns**: audit transport, moderation procedure and enforcement; B-09 owns only its domain records.

### 5.1 Required interfaces where no existing requirement exists

| Integration | Alliance may do | Alliance may not do | Owning system and required interface |
|---|---|---|---|
| Treasury | Record a deposit intent, authorise a draw, publish history | Mint, edit balances, bypass restricted-pair/embargo/storage checks | B-04 validates and posts value; B-09 stores authorization and metadata |
| City/development support | Authorise a grant/loan from the pool | Create a discount, free build, extra construction slot or research point | B-05 validates the build and its cost; B-04 moves the value |
| Diplomatic position | Publish non-binding text with an internal approval record | Sign, amend, activate, break or consent to a treaty for a member | B-08 owns diplomatic acts and consent; B-09 stores the text |
| Military coordination | Publish information and readiness declarations | Order, move, attack with or spend for a member's military | B-10 owns military execution; B-09 stores declarations |
| Global Trade | Read the market context allowed by visibility rules | Open a listing market, create an alliance trade channel or bypass G-1…G-6 | B-07 owns the market and gates |

**No existing canonical document was modified by 09A, 09A-C or 09A-D.** The matrix records interfaces and tensions; it does not amend Diplomacy, Market, Economy, City or Military rules.

### 5.2 National warehouse versus Alliance Treasury distinction (Prompt 09A-D)

Existing national warehouse capacity (`ECN-120` / `REQ-141`) and national production/purchase overflow restrictions (`ECN-124` / `REQ-142`) govern national inventory operations. They do not automatically establish Alliance Treasury storage capacity or deposit behaviour. An alliance deposit is a transfer of already-owned resources into a segregated audited pool (`REQ-176`), not a national production or trade purchase operation. Alliance pool capacity, deposit limits, and over-capacity handling remain unresolved and require an explicit Alliance System design decision (`UD-046`), coordinated with the Economy system owner in Prompt 09B.

---

## 6. Correction record — removed and replaced references

This table records every invalid reference found in matrix v1.0. Removal is not a judgement that the requirement is unimportant; it did not support the integration it was cited for.

| AX | Removed reference | Why it did not support the integration | Replacement / outcome |
|---|---|---|---|
| AX-01 | REQ-012 | `REQ-012` governs typed, event-sourced bilateral Diplomacy relationships, not founding eligibility. | REQ-002, REQ-061 direct; REQ-076 related; founding eligibility remains a new requirement (`REQ-535`, `UD-040`). |
| AX-01 | REQ-176 | `REQ-176` governs separate audited alliance pools and no minting, not who may found an alliance. | Moved to AX-06/AX-07/AX-08, where it is direct. |
| AX-02 | REQ-176 | Same pool requirement; it does not establish identity or multi-account limits. | REQ-061, REQ-043, REQ-004 direct; REQ-031 related. |
| AX-03 | REQ-012 | Bilateral relationship typing does not establish leadership succession or dormancy handling. | REQ-091, REQ-085 direct; REQ-013 related. |
| AX-04 | REQ-012 | Same mismatch: a Diplomacy relationship requirement is not an alliance succession rule. | REQ-013, REQ-085 direct; REQ-091 related. |
| AX-06 | REQ-530 | `REQ-530` is the national diplomatic-authority rule; it says nothing about deposits. | REQ-176, REQ-005, REQ-154, REQ-170 direct. |
| AX-08 | REQ-530 | National diplomatic authority does not establish storage limits. | REQ-176 direct; REQ-141 and REQ-142 related; no existing pool capacity requirement (UD-046). |
| AX-08 (09A-D) | REQ-141, REQ-142 (misclassified as DIRECT in v1.1) | REQ-141 (ECN-120) and REQ-142 (ECN-124) govern national inventory warehouse capacity and overflow blocking, not alliance treasury pools. | Reclassified to RELATED CONSTRAINT; REQ-176 retained as DIRECT for separate audited pool/integrity; explicit NO EXISTING REQUIREMENT row added for alliance pool capacity (UD-046). |
| AX-08 (09A-E) | Summary, failure/recovery, and resource impact fields (v1.2) | AX-08 summary previously said "Hold pooled resources within Economy capacity", failure/recovery said "Reject over-capacity deposit cleanly", and resource impact said "Capacity only". | Replaced summary with explicit statement that national warehouse capacity does not establish Alliance-pool capacity; replaced failure/recovery and economic impact with explicit statements that over-capacity deposit behaviour and pool capacity are unresolved under UD-046. |
| AX-08 (09A-F) | Status and matrix changelog (v1.3) | Final project-wide status reconciliation and acceptance closure pass. Confirmed AX-08 national warehouse distinction, unapproved deposit policy under UD-046, and 77 relationship totals; reconciled all project-wide current-status references to Prompt 09A-F closure. | Reconciled all current-status references across project handoffs, roadmaps, and progress records; added Prompt 09A-F closure validation. |
| AX-09 | REQ-012 | Diplomacy relationship typing does not establish recruitment or membership applications. | REQ-002 supporting only; no existing membership requirement; new candidates `REQ-562`–`REQ-570`. |
| AX-11 | REQ-530 | National diplomatic authority does not establish city-development support. | REQ-172 direct; REQ-218, REQ-005 related. |
| AX-16 | REQ-532 | `REQ-532` is the TRANSITION/CRISIS diplomacy freeze and deadline extension; it does not define an alliance diplomatic position. | REQ-530 direct; REQ-523, REQ-531 related; no existing position requirement. |
| AX-17 | REQ-532 | The freeze rule is not the embargo rule. | REQ-529, REQ-175, REQ-170 direct. |
| AX-15 | `DIP-146–149` listed as "related decisions" | These are B-08 **rules**, not decision IDs; the matrix mislabelled them. | Cited as canonical Diplomacy rules (`DIP-147`/`DIP-148`); decision column now names only real decisions. |
| AX-13/14/18/22/23/24 | No REQ cited, but the row implied a future dependency | An empty cell is ambiguous. | Explicit **NO EXISTING REQUIREMENT** rows with the owning prompt or owner decision. |

**Result:** every remaining requirement reference is either a direct dependency, a related constraint or supporting context, and every direct dependency has an evidence sentence naming the rule it depends on.

---

## 7. Change log

| Date | Version | Change | Reason |
|---|---|---|---|
| 2026-10-31 | 1.0 | Initial 26-record matrix, 20 fields, no per-requirement classification. | Prompt 09A research baseline. |
| 2026-10-31 | 1.1 | Full semantic audit of all 26 records; 11 invalid references removed; 9 direct/related replacements added; `DIP-146–149` relabelled from decisions to rules; explicit no-requirement rows added; ownership interfaces added. | Prompt 09A-C Corrections A and G. No owning rule, decision or requirement status changed. |
| 2026-10-31 | 1.2 | Reclassified REQ-141 and REQ-142 to RELATED CONSTRAINT in AX-08; retained REQ-176 as DIRECT; added explicit NO EXISTING REQUIREMENT row for alliance-pool capacity under UD-046. Reconciled relationship totals (39 DIRECT, 19 RELATED, 6 SUPPORTING, 13 NO EXISTING REQUIREMENT, 77 total). | Prompt 09A-D final treasury storage traceability correction pass. |
| 2026-10-31 | 1.3 | Corrected AX-08 summary to explicitly state national warehouse capacity does not establish Alliance Treasury capacity; removed unapproved over-capacity deposit rejection claim in failure/recovery and clarified economic impact under UD-046. Reconciled handoff references and validator checks. | Prompt 09A-E final AX-08 wording corrections, treasury policy status, handoff reconciliation and acceptance closure. |
| 2026-10-31 | 1.4 | Final project-wide current-status reconciliation and acceptance closure pass. Reconciled all current-status statements project-wide to Prompt 09A-F; confirmed AX-08 national warehouse distinction and UD-046 treasury policy status; strengthened validator protection. | Prompt 09A-F final project status reconciliation, handoff validation and acceptance closure. |
