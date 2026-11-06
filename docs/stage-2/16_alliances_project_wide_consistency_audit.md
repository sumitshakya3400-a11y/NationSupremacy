# Project-Wide Consistency and Preservation Audit — Prompts 01–09A

**Version:** 1.8 • **Created:** 2026-11-01 • **Stage 2, Prompt 09B-F; validator amended by Prompt 09B-G, Prompt 09B-I, Prompt 09B-J, Prompt 09B-K, Prompt 09B-L, Prompt 09B-M, Prompt 09B-N, Prompt 09B-O and Prompt 09B-P (2026-11-02); v1.5 adds §13, the 09B-K verification record; v1.6 adds §14, the 09B-L consolidated correction record; v1.7 adds §15, the 09B-M/09B-N acceptance-closeout record; v1.8 adds §16, the 09B-O/09B-P corrections and the Phase 09B acceptance record (2026-11-03)** • **Audit Record, Not an Approval**
**Status:** **Phase 09B Alliance specification and documentation: ACCEPTED.** Accepted at the specification/documentation level (D-142 / DD-165, 2026-11-03). Production implementation, live-game integration testing and release remain pending; `UD-040`–`UD-049` remain Open/Deferred; Prompt 09C is registered next and not started. This report records what was inspected, what was found, what was corrected and what remains owner-reserved. It is not independent acceptance, not a release approval and not a claim that the Alliance design is balanced or complete. §12 and §13 are historical audit verdicts as of 2026-11-01/02; the current status is §16.
**Scope:** Alliance-system consistency against Stage 2 Prompts 01–09A, with emphasis on the owner-reserved decisions `UD-040`–`UD-049`. Prompt 09B-F corrected the authority defects in `ALL-057` and `REQ-551`, audited every other indirect route to those reserved decisions, and checked the earlier subsystems the Alliance System depends on. Prompt 09B-G closed two validator false negatives in `C24`/`C25`, added compound-sentence regression fixtures G and H and seven positive controls, and re-ran the audited boundary checks. No canonical rule, requirement, contract, formula or decision changed in 09B-G. Prompt 09B-I adds `D-140` and the rules, contracts, formulas and requirements for owner-authorized taxation, voluntary donations, a separate Alliance-to-Alliance treaty object, NAP enforcement, the same-Alliance attack ban and the withdrawal of ALL-093's former confiscation clause; this section records that delta without claiming acceptance. **Prompt 09B-J** corrects the taxation model to automatic per-turn source withholding from current-turn production, adds player-authored brackets with any integer 0–100% rates and role-governed policy freeze, confines receipts to a credit-only Alliance Receiving Ledger under an Open UD-046, corrects NAP membership so a non-consenting nation is admitted as a non-covered member, and closes the remaining C25 plain-modal appeal escapes. **Prompt 09B-K** closes the remaining positive appeal-grant semantic gaps, replaces ALF-21/23/24's national-owner-consent, stockpile and destination-capacity implications, names the credit-only ARL in REQ-626, adds the reversible ambiguous-multiple-membership 0% fallback under Open UD-040 and specifies post-tax production-chain accounting; this record is extended, not replaced. **Prompt 09B-L** reconciles automatic taxation with `ALL-006`–`ALL-008`, `ALL-087`–`ALL-088` and §14; replaces the credit-only ledger with a four-category receipt/accounting record and one purpose-limited operational debit; narrows `UD-045` and leaves `UD-046` Open; makes bracket assignment per-Alliance; replaces the record-only treaty contradiction with the registered `AT-E00`/`AT-E01` catalogue; and widens `C25` to retained, preserved, reviewable and avenue-of-appeal formulations. **Prompt 09B-M** consolidates the closeout: it restores the three-outcome `C25` gate (fail, manual review, safe), keeps the historical `D-140` (2026-11-01) and the dated successor `D-141` (2026-11-02), separates ARL receipt accounting from spendable availability, and specifies cumulative fractional tax accrual across multiple same-asset events. **Prompt 09B-N** closes the two `C25` false negatives identified by the independent 09B-M audit — members' recourse to appellate review and a former member's challenge to expulsion — routes uncertain redress/remedy wording to manual review, and synchronizes the current-state documents. **Prompt 09B-N is the current revision; the earlier 09B-J, 09B-K and 09B-L descriptions are retained as history.** **Prompt 09B-O** closes eight remaining procedural `C25` false negatives and **Prompt 09B-P** closes the three dismissal/grievance/redress cases; both are recorded in §16 together with the **Phase 09B acceptance at the specification/documentation level (D-142 / DD-165, 2026-11-03)**. The earlier descriptions are retained unchanged as history.
**Companion evidence:** [`16_alliances.md`](16_alliances.md) (rules), [`16_alliances_integration_contracts.md`](16_alliances_integration_contracts.md) (30 `AX` contracts), [`16_alliances_formula_register.md`](16_alliances_formula_register.md) (candidate formulas), [`03_requirements_traceability.md`](03_requirements_traceability.md), [`04_approved_and_provisional_decisions.md`](04_approved_and_provisional_decisions.md), [`05_unresolved_design_decisions.md`](05_unresolved_design_decisions.md), [`DECISIONS.md`](../DECISIONS.md), and `docs/qa_backups/09B_validate_alliance_semantic.py` with its isolated test suite.

---

## 1. Executive result

1. **`ALL-057` no longer decides succession.** Competing claims are recorded as immutable audit evidence. Timestamp order, transaction order and workflow completion are expressly evidence only; they do not recognise a successor or steward, assign or transfer an office, or establish political authority. Any rule for resolving competing claims remains owner-reserved under `UD-043` and is not in force.
2. **`REQ-551` no longer mandates an appeal.** Dispute and disciplinary records are retained and the game never adjudicates the merits. No appeal or dispute-resolution mechanism is required or approved while `UD-044` is Open. Any future path is conditional on explicit owner approval.
3. **No other inspected requirement, rule, contract, formula, decision, example or acceptance criterion imposes an owner-reserved choice.** Every `UD-040`–`UD-049` row remains `Open` / `Yes — owner`. The remaining references are either binding inherited constraints, expressly labelled candidates, or negations that preserve the reservation.
4. **All audited cross-system boundaries remain intact.** National diplomatic authority has zero delegation (`D-137`, `REQ-530`); treasury conservation is binding while pool ownership/capacity/withdrawal policy stays Open under `UD-046`; Global Trade remains mandatory product scope (`D-122`, `DD-136`, `REQ-513`) behind unchanged gates `G-1`–`G-6` (G-1, G-2, G-3, G-5, G-6 **NOT MET**; G-4 **PARTIAL**).
5. **The strengthened validator detects the corrected defects without rejecting legitimate records.** 34 semantic checks now include authority-aware checks `C24`–`C26`, the five 09B-I guards `C27`–`C31`, the 09B-K grant-family hardening inside `C25`, the 09B-L ARL/operational-funding and treaty-effect guards `C32`–`C33`, and the tax-boundary guard `C34`; **260 isolated tests** cover negative fixtures A–P, the five 09B-J plain-modal appeal fixtures, the 09B-K positive-grant and control fixtures (tests 177–198), the 09B-L retained/preserved/reviewable/avenue fixtures (210–225), the `C32`–`C34` guard fixtures (226–252), the 09B-M fail/review/safe and regression fixtures (253–256), the 09B-N recourse/appellate/redress acceptance fixtures (257–259), every 09B-I, 09B-J, 09B-K and 09B-L policy shape and lifecycle term, the per-turn tax semantics, the ALF/ARL corrections, the multiple-membership safeguard and the production-chain examples, and their positive controls. Passing the validator proves documentary agreement, not design quality or independent acceptance.
6. **Two validator false negatives were found and closed in 09B-G.** `C24` and `C25` previously skipped an entire sentence when any negation or conditional wording appeared, so a disclaimer followed by a mandate passed. Both checks now split compound sentences into clauses and evaluate each clause independently; the exact disclaimer-plus-mandate sentences now fail for the intended reasons. This was a validator defect, not a new authority defect in the canonical corpus. **Prompt 09B-I closed the remaining C25 N/O/P class**: a denial prohibition, an `except that` entitlement and an `unless` entitlement now fail even when the main clause reads as neutral, while honest holding statements and neutral recordkeeping still pass.
7. **The five owner-authorized 09B-I capabilities are specified with their reservations intact.** Member taxation and voluntary donations are binding owner-authorized capabilities under `D-140`/`DD-161`, with taxation corrected by 09B-J to automatic per-turn production withholding; the separate Alliance-to-Alliance treaty object and NAP consent are binding under `DD-162`; the same-Alliance attack ban is a binding design contract on Prompt 10 under `DD-163`. `UD-046` and `UD-047` remain Open outside those exact capabilities, `UD-043` and `UD-044` are untouched, and `ALL-093` is a tombstone that grants no confiscation power.

---

## 2. Method, authority rules and evidence limits

### 2.1 What this audit treats as authoritative

| Question | Authority used |
|---|---|
| Is a rule binding? | The owning subsystem rulebook plus an owner-approved `D-` entry in [`DECISIONS.md`](../DECISIONS.md). A Provisional requirement does not become binding merely because an Alliance document repeats it |
| Is an Alliance policy approved? | The unresolved-decision register [`05_unresolved_design_decisions.md`](05_unresolved_design_decisions.md) and the decision register [`04_approved_and_provisional_decisions.md`](04_approved_and_provisional_decisions.md). `UD-040`–`UD-049` are `Open` / `Yes — owner`; only the owner may change that |
| Is a proposal a decision? | No. Candidate formulas, candidate contracts, examples and recommendations are non-authoritative until the named owner decision is recorded, followed by a status update in the owning document |
| May an Alliance document override a national rule? | No. The owning subsystem governs at its interface (`ALL-171`); an Alliance document may not silently amend `TR-`, `ACC-`, `ECN-`, `URB-`, `DMP-`, `MKT-` or `DIP-` rules |

### 2.2 Inspection method

- **Full reads** were made of `16_alliances.md`, `16_alliances_integration_contracts.md`, `16_alliances_formula_register.md`, the requirements register header and the cited Alliance rows, both decision registers' headers/tallies, `DECISIONS.md` header and the cited rows, and the continuity files named in §10.
- **Targeted section reads** were made of the earlier rulebooks and reports cited in §4. The specific rule or section is named in each record so the claim can be re-checked; this audit does not claim that every line of every earlier document was re-read in this pass.
- **Search-based checks** were run across the corpus for indirect succession, vacancy, stewardship, fallback-leader, appeal, expulsion, rejoin, treasury-ownership and diplomatic-delegation language. Findings were then read in context; a keyword alone was never treated as a defect.
- **No production code, schema, migration, API, screen, job or deployment** was created by Prompt 09B, 09B-F or 09B-G. Sanctioned feasibility prototypes exist under `prototypes/` from earlier Stage 1/Stage 3 work and are outside the production-scope prohibition; the validator excludes that directory explicitly.

### 2.3 What this audit does not prove

- It does not prove that the Alliance design is balanced, fun, secure in implementation, or complete.
- It does not prove that any requirement is implemented or runtime-tested. No such claim is made anywhere in Stage 2.
- It does not independently accept Prompt 09B. That decision belongs to the owner and the independent reviewer.
- It does not convert any `UD-040`–`UD-049` question into an approved answer, and it does not reclassify any decision.

---

## 3. Documents and prompt stages actually inspected

| Stage / prompt | Deliverable inspected | What was checked | Result |
|---|---|---|---|
| Stage 1, Reports 09, 11, 12 | Integrated design synthesis; free-tier feasibility results; deployment/resource separation | Architecture direction (`D-008`–`D-013`), free-tier limits, verified deployment facts, explicit non-proofs | Consistent with Stage 2's documentation-only mission |
| Stage 2, Prompt 01 | [`01_stage_2_prompt_roadmap.md`](01_stage_2_prompt_roadmap.md), [`02_master_game_design_bible_outline.md`](02_master_game_design_bible_outline.md), [`03_requirements_traceability.md`](03_requirements_traceability.md), [`04_approved_and_provisional_decisions.md`](04_approved_and_provisional_decisions.md), [`05_unresolved_design_decisions.md`](05_unresolved_design_decisions.md) | Roadmap ownership, Bible part mapping, requirement vocabulary/counts, decision precedence, owner-reserved rows | One stale Prompt 09 instruction found and corrected (§7) |
| Stage 2, Prompt 02 | [`07_core_gameplay_loop_symbolic_world_and_turn_system.md`](07_core_gameplay_loop_symbolic_world_and_turn_system.md) (B-02) | `TR-024` slot arithmetic, `TR-029` boundary assignment, `TR-060` resolution validation, visibility and consent rules, `TR-021` alliance-visibility row | Consistent; `TR-021` already conditional on a native ballot under `UD-042`/`UD-049` |
| Stage 2, Prompt 03 | [`09_account_onboarding_nation_creation_and_progression.md`](09_account_onboarding_nation_creation_and_progression.md) (B-03) | `ACC-001`, `ACC-008`, `ONB-048`, `D-028` dormancy, reroll/role handling, account and nation ownership | Consistent; reroll row labels office succession/vacancy candidate under `UD-043` |
| Stage 2, Prompt 04 | [`10_economy_resources_treasury_and_finances.md`](10_economy_resources_treasury_and_finances.md) (B-04) and [`10_economic_formula_and_balance_register.md`](10_economic_formula_and_balance_register.md) | `ECN-092`, `ECN-103`, `ECN-152`, `ECN-176`, `ECN-212`, `ECN-213`; conservation, no debt, no alliance currency, transfer contract | Consistent; `ECN-152` now names maintenance and any approved voluntary contribution, not "dues" |
| Stage 2, Prompt 05 | [`11_cities_infrastructure_production_and_research.md`](11_cities_infrastructure_production_and_research.md) (B-05) and formula register | `URB-156` (no alliance-held cities, facilities, DC/housing or research-for-member), build and research ownership | Consistent; no Alliance rule creates city or research authority |
| Stage 2, Prompt 06 | [`12_population_and_domestic_politics.md`](12_population_and_domestic_politics.md) (B-06) and formula register | `DMP-139` non-interference, `DMP-264` caretaker limits, election/crisis ownership | Consistent; AX-13/AX-14 are deferred with zero first-release effect |
| Stage 2, Prompt 07 | [`13_trade_and_markets.md`](13_trade_and_markets.md) (B-07), [`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md) and formula register | `MKT-008`, `MKT-100`, `MKT-218`, `MKT-072`–`MKT-077`, `G-1`–`G-6`, Global Trade scope | Consistent; gates unchanged and still unmet except G-4 partial |
| Stage 2, Prompt 08 | [`15_diplomacy.md`](15_diplomacy.md) (B-08), [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md) (08C), formula register | `DIP-146`–`DIP-149`, `DIP-015`, `D-137`, `REQ-530`, treaty persistence, embargo and delegation boundary, 08C's 117-pair ledger | One stale B-08 header status sentence found and corrected (§7); active 08C sections already `D-137`-correct |
| Stage 2, Prompt 09A | `research/09A_alliance_research.md`, `09A_alliance_integration_matrix.md`, `09A_alliance_sources_findings.md`, `09A_alliance_reference_review.md` | Four-document evidence base, 26 `AX` identities, requirement relationships, 17 enrichment areas | Accepted work preserved; no research finding promoted to a rule |
| Stage 2, Prompt 09B / 09B-F | B-09, contracts, formula register, requirements, decision registers, progress log, continuity set | Rule authority, contract status, requirement counts, `UD` statuses, status sentence, 09C gate | Corrected and synchronized; details in §7 and §10 |
| Continuity | [`DECISIONS.md`](../DECISIONS.md), [`AI_CONTEXT.md`](../AI_CONTEXT.md), [`AI_HANDOFF.md`](../AI_HANDOFF.md), [`PROJECT_PROGRESS.md`](../PROJECT_PROGRESS.md), [`ROADMAP.md`](../ROADMAP.md), [`00_stage_2_handoff.md`](00_stage_2_handoff.md), [`06_stage_2_progress_log.md`](06_stage_2_progress_log.md) | Mandated status sentence, 09C blocked, historical entries preserved | Synchronized under 09B-F |

---

## 4. Integration audit — required eight fields per system

Legend for field (6): **Consistent** — no correction required in this pass; **Corrected** — a targeted correction was recorded in §7; **Deferred** — the interface is owned by a later prompt and is not exercised in the first release; **Binding inherited** — the external subsystem governs and the Alliance side only consumes it.

### 4.1 Accounts, authentication and identity

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-03 [`09_account_onboarding_nation_creation_and_progression.md`](09_account_onboarding_nation_creation_and_progression.md): `ACC-001`, `ACC-003`, `ACC-008`, `D-018`, `D-029`; requirements `REQ-043`, `REQ-061`; B-02 `TR-060` for execution-time validation |
| **(2) Alliance interaction** | `AX-01` (eligible owner founds), `AX-02` (one-player-one-nation applied to roles), `AX-09` (applicant/account checks), `AX-10` (field-level visibility) |
| **(3) Inputs / outputs** | Inputs: authenticated account ID, verified e-mail status, nation ID, account state, role payload. Outputs: validated role or membership record, audit event, visibility projection |
| **(4) Ownership / permissions** | Account system owns identity, one-account policy and verification. Alliance owns only position/roster records. An alliance officer cannot create, recover, merge or transfer an account or nation |
| **(5) Restrictions / failure behaviour** | One account per person and one active nation (`ACC-001`); no sale, gift, inheritance or transfer (`ACC-008`); bots and secondary accounts cannot hold roles; rejection is atomic with a stable failure code. Identity enforcement is policy plus planned controls, not a perfect technical proof |
| **(6) Consistency** | **Binding inherited.** `AX-02`, `AX-09`, `AX-10` preserve the account boundary; `AX-01` eligibility is candidate only under `UD-040` |
| **(7) Correction made** | None required in 09B-F. Earlier 09B-E text already labels founding eligibility and the single-alliance rule candidate |
| **(8) Verification evidence** | Read `ACC-001` (line 177 region), `ACC-008` (line 199 region), `ONB-048` (line 1166 region); validator `C06`, `C16`; negative fixtures do not touch account policy |

### 4.2 Nation creation, ownership and management

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-03: `NAT-013`, `NAT-015`, `NAT-017`, `NAT-032`, `NAT-037`, `NAT-045`, `NAT-052`, `ONB-010`, `ONB-023`, `ONB-025`, `ONB-034`, `ONB-043`, `ONB-048`; `D-028` (168-turn dormancy); `REQ-085`, `REQ-091` |
| **(2) Alliance interaction** | `AX-01` founding, `AX-03` dormancy/reroll/retirement events, `AX-04` office vacancy; membership never changes nation ownership |
| **(3) Inputs / outputs** | Inputs: nation lifecycle event, dormancy state, reroll event, retirement/deletion. Outputs: alliance notice and audit record; a dormant nation remains a member but cannot vote, accept a role, authorise a bank transfer or join a new operation |
| **(4) Ownership / permissions** | The player owns the nation. The Alliance holds only membership and office metadata. No alliance action changes nation ownership or national assets |
| **(5) Restrictions / failure behaviour** | Reroll ends membership and vacates roles but transfers no assets; dormancy triggers `D-028` effects; no lifecycle event transfers diplomatic or military authority. If every member is inactive, no automatic dissolution occurs |
| **(6) Consistency** | **Binding inherited.** The reroll row correctly says succession/vacancy is candidate under `UD-043` and is not applied automatically |
| **(7) Correction made** | Earlier 09B-F pass corrected the B-03 reroll row to remove automatic succession language. No new change in this report |
| **(8) Verification evidence** | Read B-03 reroll row and `ONB-048`; `AX-03` contains "no office, authority or seat transfers automatically" and "no fallback stewardship, caretaker appointment or dissolution executes"; validator `C24` |

### 4.3 Nation permissions and authority

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-02 `TR-060` (resolution validation); B-03 `REQ-004`, `REQ-027`; approved owner model `ACC-001`; B-09 `ALL-066`–`ALL-078` candidate capability architecture |
| **(2) Alliance interaction** | `AX-05` permission changes and role grants; `AX-21` audit of privileged actions; `AX-02` role eligibility |
| **(3) Inputs / outputs** | Inputs: actor, target, capability, alliance configuration, constitutional authority reference. Outputs: granted/revoked capability record, audit event, execution-time check |
| **(4) Ownership / permissions** | National authority derives from the sovereign owner; alliance permissions are internal technical capabilities only. They never grant authority over a nation's diplomacy, military, treasury or domestic government |
| **(5) Restrictions / failure behaviour** | Least privilege, independence of capabilities, anti-escalation, execution-time verification, no cached UI grant. Unauthorised acts fail closed with an audit record |
| **(6) Consistency** | **Consistent.** Capability catalogue content and delegation limits remain `Open` under `UD-045`; no rank or role grants national authority |
| **(7) Correction made** | None in 09B-F. Existing B-09 text already distinguishes technical capability from political title (`ALL-048`) |
| **(8) Verification evidence** | Read B-09 §11 and `AX-05`; `AX-05` status is candidate/Open under `UD-045`; validator `C26` for `UD-045` |

### 4.4 Economy, currency, resources and treasury

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-04: `ECN-092` (no alliance currency), `ECN-103` (no debt/loans), `ECN-152` (maintenance and voluntary contribution), `ECN-176`, `ECN-212` (canonical transfer), `ECN-213` (alliance pool separate/audited); `REQ-176`; `D-060` |
| **(2) Alliance interaction** | `AX-06` deposits, `AX-07` withdrawals/grants/loans, `AX-08` storage boundary, `AX-11` city/development support |
| **(3) Inputs / outputs** | Inputs: nation, resource, quantity, source/destination, authorisation, ledger references. Outputs: conserved transfer, ledger entries, audit record, rejection code. No resource is created by an alliance |
| **(4) Ownership / permissions** | National wealth is inviolable (`ALL-087`, `ALL-142`, `ALL-145`); `ALL-093` is withdrawn by `D-140` and grants no confiscation power. Only the nation owner authorises a legal transfer out; the two authorized value movements are an automatic per-turn production tax under the alliance's lawful policy and a voluntary donation (`ALL-179`–`ALL-195`). Whether a pool exists, who owns it, its capacity, withdrawal rules and signatures are owner-reserved under `UD-046`; the Alliance Receiving Ledger is a four-category receipt/accounting record and creates no ownership or withdrawal right, its only debit being the purpose-limited operational expense |
| **(5) Restrictions / failure behaviour** | No minting, no bypass of storage or embargo checks, no loans as a core engine mechanic, no alliance currency, no trading fees. Over-capacity rejection, dual signatures and thresholds are candidates only; no value is in force. A generated tax or valid donation may never be rejected, destroyed or lost because of an unapproved capacity assumption (`ALL-187`; `UD-046` Open) |
| **(6) Consistency** | **Binding inherited conservation; candidate architecture.** `AX-08` correctly states only that national warehouse limits do not establish pool capacity |
| **(7) Correction made** | Earlier pass changed `ECN-152`'s "alliance dues" to "maintenance and any approved voluntary alliance contribution"; 09B-E removed approval claims from `F-AL-001`/`F-AL-005` and `AX-06`–`AX-08`; 09B-J replaced the per-policy consent tax description with automatic per-turn source withholding and the credit-only ARL |
| **(8) Verification evidence** | Read `ECN-212`/`ECN-213`; `AX-08` text; `F-AL-001` "Candidate Proposal"; validator `C14`, `C22`, `C26` for `UD-046` |

### 4.5 Domestic politics and government

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-06 [`12_population_and_domestic_politics.md`](12_population_and_domestic_politics.md): `DMP-002`, `DMP-139`, `DMP-175`, `DMP-176`, `DMP-231`, `DMP-264`; decisions `D-081`–`D-108`; `REQ-307`, `REQ-326`, `REQ-365` |
| **(2) Alliance interaction** | `AX-13` population/approval effects and `AX-14` election/crisis interaction are both **Deferred** with zero first-release effect. `AX-04` office vacancy must not touch national government |
| **(3) Inputs / outputs** | No first-release input or output. If later authorised, an alliance could read a member's public political state; it could never set policy, choose a government or transfer approval, stability, legitimacy or population |
| **(4) Ownership / permissions** | National government, policies, elections, approval, stability, legitimacy and population remain exclusively national. An alliance caretaker cannot change permissions, spend a pool, accept an application or leave an alliance |
| **(5) Restrictions / failure behaviour** | `DMP-139` forbids alliance control of political state and use of a pool for political effect; `DMP-264` limits caretakers; any interaction is deferred and cannot be inferred from Alliance texts |
| **(6) Consistency** | **Deferred / consistent.** No Alliance rule claims political effect |
| **(7) Correction made** | None required in 09B-F |
| **(8) Verification evidence** | Read `DMP-139`, `DMP-264`; `AX-13`/`AX-14` statuses "Deferred … Zero Effect/Interaction"; validator `C26` covers `UD-041` office template without political authority |

### 4.6 Diplomacy and treaties

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-08 [`15_diplomacy.md`](15_diplomacy.md): `DIP-012`, `DIP-014`, `DIP-015`, `DIP-019`, `DIP-039`, `DIP-041`, `DIP-060`, `DIP-074`, `DIP-077`, `DIP-080`, `DIP-091`, `DIP-112`, `DIP-146`–`DIP-149`; `D-137`; `REQ-530`; 08C [`15_diplomacy_workflows_acceptance.md`](15_diplomacy_workflows_acceptance.md) |
| **(2) Alliance interaction** | `AX-15` national treaties persist through join/leave/removal; `AX-16` candidate non-binding collective positions; `AX-17` embargo and restricted-pair checks. No B-08 alliance treaty object; `D-140` creates a separate B-09 object; no delegation |
| **(3) Inputs / outputs** | Inputs: treaty/relationship records, member roster changes, embargo state, proposed non-binding position. Outputs: unchanged bilateral treaty state, optional published position with no obligation, rejection of any alliance-mediated diplomatic act |
| **(4) Ownership / permissions** | Only the authenticated owner of an active nation holds diplomatic authority. No leader, officer, majority, AI, administrator or alliance body may sign, accept, break or terminate for a nation. Silent consent is never inferred |
| **(5) Restrictions / failure behaviour** | No B-08 alliance-level treaty object; `D-140` creates a separate B-09 object; no delegation; membership does not make an alliance a party, guarantor or decision-maker; an alliance cannot be a diplomatic shortcut around consent. Collective positions are candidate under `UD-047` and bind nobody |
| **(6) Consistency** | **Binding inherited.** `D-137` resolves `UD-039`; `AX-16` remains Open under `UD-047` for the non-binding-position question only |
| **(7) Correction made** | Earlier 09B-F pass propagated `D-137` through B-08 active sections and 08C and corrected B-08's stale header sentence; 09B-J corrects `ALL-204`/`REQ-641` so a nation whose owner declines NAP coverage remains a non-covered member and is never refused admission. No B-08 rule changed |
| **(8) Verification evidence** | Read `DIP-146`–`DIP-149`, `DIP-015`, B-08 header, 08C authority line; `AX-15`/`AX-16`; validator `C08`, `C12`, `C20`, `C24`; negative fixture C proves a contract cannot assign succession authority by timestamp |

### 4.7 Warfare and military

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | Prompt 10 owns warfare (design pending). Existing boundaries: B-02 resolution rules `TR-024`/`TR-029`/`TR-060`; B-03 §18 restricted-pair campaign rule; B-09 `ALL-136` national military sovereignty; `REQ-014`, `REQ-518` |
| **(2) Alliance interaction** | `AX-12` readiness/activity declarations (informational only); `AX-18` war/coordination information **Deferred to Prompt 10**; `AX-29` AT-T01 NAP coverage and `AX-30` same-Alliance/NAP attack validator are binding design contracts on Prompt 10 |
| **(3) Inputs / outputs** | Inputs: member-declared readiness or activity signal. Outputs: informational record; no order, no obligation, no automatic action, no command transfer. War records remain national |
| **(4) Ownership / permissions** | Military forces, command and war decisions belong exclusively to sovereign nations. An alliance owns no unit, cannot deploy a member's force and cannot declare war for a nation. The same-Alliance ban and an active AT-T01 NAP restrict attacks between covered nations, but they transfer no command and create no alliance war authority |
| **(5) Restrictions / failure behaviour** | No alliance military object; no automatic mobilisation; no alliance-level war authority. Coordination notices are candidate only and create no mechanical effect. Every supported attack entry point must call the canonical server-side same-Alliance and applicable NAP checks before execution, fail closed before consuming resources or damage, and write a mandatory `AUD-AL-017` event independent of optional audit settings (`ALL-209`–`ALL-215`, `REQ-645`–`REQ-647`); no UI-only check is enforcement |
| **(6) Consistency** | **Deferred for war mechanics; binding for attack restrictions.** No first-release alliance war mechanic is claimed. The same-Alliance ban and active-NAP restriction are owner-authorized design contracts whose runtime enforcement belongs to Prompt 10 |
| **(7) Correction made** | 09B-I added `AX-29`/`AX-30` and `ALL-206`–`ALL-215`; 09B-J makes the blocked-attempt audit mandatory, corrects NAP non-covered membership and keeps the two checks independent and cumulative |
| **(8) Verification evidence** | Read `AX-12`, `AX-18`, `AX-29`, `AX-30` status fields; `ALL-136`, `ALL-206`–`ALL-215`; B-09 §20 and §29.3–§29.4; `REQ-642`, `REQ-645`–`REQ-647`; no `TRN-` identifiers or invented turn rules exist |

### 4.8 Global Trade

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-07 [`13_trade_and_markets.md`](13_trade_and_markets.md): `MKT-008`, `MKT-068`, `MKT-072`, `MKT-074`, `MKT-075`, `MKT-076`, `MKT-077`, `MKT-100`, `MKT-185`, `MKT-195`, `MKT-218`; `D-122`; `DD-136`; `REQ-513`; gates `G-1`–`G-6`; 07C [`14_market_workflows_and_acceptance.md`](14_market_workflows_and_acceptance.md) |
| **(2) Alliance interaction** | `AX-26` consumes market context read-only. An alliance creates no market, no scrip, no private board, no trading fee, no tariff and no fee bypass |
| **(3) Inputs / outputs** | Inputs: market state queries and published reference prices, read-only. Outputs: zero order mutations, zero private boards, zero alliance fee revenue |
| **(4) Ownership / permissions** | Global Trade owns boards, order clearing, fees and release gates. Alliances possess no market actor role; only sovereign nation owners trade |
| **(5) Restrictions / failure behaviour** | Any attempted alliance intermediation is rejected (`ALF-12`). The market stays dark until every gate passes. No document may call it ready, live or released while a gate is unmet |
| **(6) Consistency** | **Approved mandatory constraint; gates unchanged.** Products scope is approved but release is gated; this is not a contradiction |
| **(7) Correction made** | None. `D-122`, `DD-136`, `REQ-513` and `G-1`–`G-6` deliberately preserved |
| **(8) Verification evidence** | Read B-07 gate table (`G-1`/`G-2`/`G-3`/`G-5`/`G-6` NOT MET, `G-4` PARTIAL); `AX-26` status "Approved Mandatory Constraint"; validator `C07`, `C20`; test `test_65_global_trade_scope_weakened_fails` |

### 4.9 Progression

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-03 onboarding/progression rules and `D-028`; B-05 research and city progression (`URB-156` prohibits alliance research for a member); requirements `REQ-085`, `REQ-091`; no alliance-level progression currency or research tree exists |
| **(2) Alliance interaction** | Membership is organizational only. `AX-13`/`AX-14` are deferred with zero first-release effect. An alliance cannot grant technology, research, development points or population |
| **(3) Inputs / outputs** | Inputs: none for progression. Outputs: none; alliance membership does not accelerate, decelerate or redirect a nation's progression |
| **(4) Ownership / permissions** | Each nation owns its own progression. An alliance officer has no capability to grant or remove national progression |
| **(5) Restrictions / failure behaviour** | `URB-156` forbids researching for a member; no alliance research institute, shared technology tree or progression pool is defined. Any future effect requires an explicit decision |
| **(6) Consistency** | **Consistent.** No Alliance rule claims progression authority |
| **(7) Correction made** | None required in 09B-F |
| **(8) Verification evidence** | Read `URB-156`; `AX-13`/`AX-14` deferred statuses; B-09 §2 ownership table; validator `C26` does not find a progression claim |

### 4.10 Security, privacy, moderation and audit

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | B-02 visibility and audit rules; platform audit spine `D-026`, `REQ-021`, `REQ-027`, `REQ-153`; moderation `REQ-025`, `REQ-026`; B-09 `ALL-005`, `ALL-154`–`ALL-160`; `D-133`; `DD-147` |
| **(2) Alliance interaction** | `AX-10` field-level visibility; `AX-19` static Discord link; `AX-21` immutable audit; `AX-23` fair-play moderation deferred; `AX-24` notifications deferred |
| **(3) Inputs / outputs** | Inputs: privileged alliance act, report, visibility field, link submission. Outputs: append-only audit event, filtered projection, moderation record; no account suspension by an alliance officer |
| **(4) Ownership / permissions** | Platform owns audit, moderation, account enforcement and privacy defaults. The Alliance owns only its domain records; an officer cannot suspend an account, read private national data beyond the declared visibility rule, or appeal platform moderation on behalf of another player |
| **(5) Restrictions / failure behaviour** | Immutable append-only audit is binding; sensitive acts require confirmation; no real-time chat, Discord bot, API, OAuth, webhook or account linking. A platform moderation appeal remains a platform path and does not create an alliance appeal right |
| **(6) Consistency** | **Binding inherited audit; candidate confirmation mechanics.** `ALL-158`'s platform evidence-and-appeal path is legitimate and is excluded from the `UD-044` membership-appeal check by context |
| **(7) Correction made** | Earlier 09B-E corrected `ALL-057` audit wording and preserved the platform moderation boundary; 09B-F calibrated the validator so it does not flag platform moderation |
| **(8) Verification evidence** | Read `ALL-154`–`ALL-160`, `AX-21`; validator `C13`, `C21`, `C25`; negative fixture B/D prove an alliance-member appeal mandate fails |

### 4.11 UI/UX and player journeys

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | Bible outline B-13 (Prompt 13, Planned); B-02 visibility; B-09 `ALL-160`, `ALL-175`; `REQ-614`–`REQ-617`; `AX-24`; `D-133`; 09A UX findings |
| **(2) Alliance interaction** | `AX-24` notifications/UI surfaces is **Deferred to Prompt 13**. The Alliance rulebook fixes only constraints: plain language, destructive-action confirmation, neutral office vocabulary, no mandatory Discord and no second account |
| **(3) Inputs / outputs** | Inputs: alliance domain events, configuration, user role. Outputs (future): notification payload, confirmation prompt, visibility-filtered screen. No screen is specified in 09B |
| **(4) Ownership / permissions** | Prompt 13 owns the interface specification. The Alliance owns domain events; the interface owns delivery and display. UI render state never grants permission |
| **(5) Restrictions / failure behaviour** | No real-time chat; batched digest delivery; a dropped notification cannot alter alliance state; a stale tab cannot execute an unauthorised or expired act. Accessibility and screen sequence remain future work |
| **(6) Consistency** | **Deferred / consistent.** 09B explicitly defers interface specification to 09C/13 and does not invent screens |
| **(7) Correction made** | None in 09B-F. The audit report records the deferral as a limitation, not a defect |
| **(8) Verification evidence** | Read `AX-24`, `ALL-175` item 3, `REQ-614`–`REQ-617`; no UI component exists in production scope |

### 4.12 Technical architecture and data ownership

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | [`DECISIONS.md`](../DECISIONS.md) `D-008` (Cloudflare + Supabase; Supabase Cron sole scheduler), `D-009` (Pages URL), `D-010` (dedicated Supabase project), `D-012` (Stage 2 design only; architecture is Stage 5), `D-013` (legacy resources deleted); Stage 1 Report 11 §§15–19 and Report 12 §§2–3; B-09 §2 ownership boundaries and every `AX` "State Ownership" field |
| **(2) Alliance interaction** | All 26 `AX` contracts declare inputs, outputs, state ownership, authorised actors, failure behaviour and recovery responsibility. Alliance state is domain state, not a second source of truth for national state |
| **(3) Inputs / outputs** | Inputs: authenticated commands, canonical subsystem records, turn-boundary events. Outputs: alliance metadata, audit events, projections; mutations of national state only through the owning subsystem |
| **(4) Ownership / permissions** | Each subsystem owns its state (`ALL-170`). The Alliance cannot mutate account, nation, economy, city, politics, market or diplomacy state directly; it invokes the owning contract |
| **(5) Restrictions / failure behaviour** | Server-side execution-time checks, atomic rejection, idempotency, audit, no cached UI authority. Free-tier limits are measured but not proven for production; no backup/restore drill, no auth flow and no load test exist for the eventual game |
| **(6) Consistency** | **Consistent, with explicit evidence limits.** Stage 2 does not claim that the free-tier architecture is production-proven |
| **(7) Correction made** | None in 09B-F. This report does not change `D-008`–`D-013` |
| **(8) Verification evidence** | Read Report 11 §15.8 ("what this does not prove") and Report 12 §2.1 (Pages Function limitation); read `AX` state-ownership fields; the validator excludes sanctioned `prototypes/` and finds no production source |

### 4.13 Requirements, formulas, decisions and release gates

| Field | Finding |
|---|---|
| **(1) Authoritative source and ID** | [`03_requirements_traceability.md`](03_requirements_traceability.md); [`04_approved_and_provisional_decisions.md`](04_approved_and_provisional_decisions.md); [`05_unresolved_design_decisions.md`](05_unresolved_design_decisions.md); [`DECISIONS.md`](../DECISIONS.md); alliance formula register; B-07 `MKT-072`–`MKT-077`; 08C §15.5 |
| **(2) Alliance interaction** | 114 Alliance requirements `REQ-534`–`REQ-647`; 7 formulas (`F-AL-001`–`F-AL-005` candidate, `F-AL-006`/`F-AL-007` arithmetic models under `D-140`); decisions `D-135`–`D-140`, `DD-151`–`DD-163`; `UD-040`–`UD-049` |
| **(3) Inputs / outputs** | Inputs: rule text, candidate parameters, owner decisions, test plans. Outputs: requirement status, formula status, decision record, gate status. None is an implementation result |
| **(4) Ownership / permissions** | The requirement register owns text/status; the decision register owns approved design positions; `DECISIONS.md` is the only approval log; the owner owns every `UD-040`–`UD-049` question |
| **(5) Restrictions / failure behaviour** | The 30 `D-140`-authorised Alliance rows are Approved for design; the other 84 keep their prior Provisional/Open/Deferred status. No formula is enforced, balanced or calibrated; a passing validator does not approve a rule; Global Trade remains gated. `REQ-591` stays Deferred to Prompt 10 |
| **(6) Consistency** | **Consistent after correction.** Counts: 647 requirements = 49 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed; Alliance 114 = 30 Approved / 71 Provisional / 12 Open / 1 Deferred; 49 `UD` rows = 26 Resolved / 5 Deferred / 18 Open; 163 `DD` rows = 128 Approved / 26 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred |
| **(7) Correction made** | 09B-F corrected `REQ-551`, `REQ-568`, `REQ-569` and the related rulebook/contract/formula language; 09B-I added `REQ-618`–`REQ-647` and `D-140`; 09B-J clarified the 30 authorised rows and `DD-161`–`DD-163` without adding, removing, renumbering or status-changing a row. No owner-reserved row was resolved |
| **(8) Verification evidence** | Register headers and tallies read; validator `C14`–`C17`, `C22`, `C25`, `C27`–`C31`; tests `test_46`–`test_59`, fixtures A–P and tests `test_142`–`test_176`; `verify_alliance_numbers.py` (217 checks, 22/22 self-test) |

---

## 5. AX contract reconciliation — all 30 records

The status column reproduces the contract's own field. "Candidate/Open" means the contract is a proposal whose policy depends on the named owner decision; it is not an approved interface. `AX-27`–`AX-30` are the Prompt 09B-I additions under `D-140`; **Prompt 09B-J clarifies `AX-27`–`AX-30` without changing any identity or status**.

| AX | Owning subsystem | Contract status | Reserved decision / authority |
|---|---|---|---|
| AX-01 | Nation & Account (`B-01`/`B-03`) | Candidate Proposal; Open | `UD-040` |
| AX-02 | Nation & Identity (`B-01`/`B-03`) | Candidate Role Architecture; Open | `UD-045` |
| AX-03 | Nation & Account Lifecycle (`B-03`) | Candidate Succession Safeguards; Open | `UD-043`; `F-AL-003` candidate |
| AX-04 | Alliance Governance + B-03 | Candidate Succession Architecture; Open | `UD-043`; `UD-012` structural only |
| AX-05 | Alliance Governance + Platform Security | Candidate Capability Model; Open | `UD-045` |
| AX-06 | Economy & Ledger (`B-04`) | Candidate Treasury Architecture; Open | `UD-046`; `REQ-176` preserved |
| AX-07 | Economy & Ledger (`B-04`) | Candidate Treasury Architecture; Open | `UD-046` |
| AX-08 | Economy & Warehouse (`B-04`) | Candidate Capacity Proposal; Open | `UD-046`; `F-AL-001` candidate |
| AX-09 | Alliance Membership + Account/Nation | Candidate Membership Lifecycle; Open | `UD-044` |
| AX-10 | Foundations & Visibility (`B-02`) | **Binding Inherited** privacy constraint | `REQ-057` Provisional; field defaults candidate |
| AX-11 | Cities (`B-05`) + Economy (`B-04`) | Candidate Treasury Support Model; Open | `UD-046` |
| AX-12 | Nation Activity (`B-03`) + Future Military | Candidate Informational Feature | No owner approval; no military effect |
| AX-13 | Population & Domestic Politics (`B-06`) | **Deferred**; zero effect in v1 | Future prompt |
| AX-14 | Domestic Politics & Elections (`B-06`) | **Deferred**; zero interaction in v1 | Future prompt |
| AX-15 | Diplomacy (`B-08`) | **Binding Inherited** constraint | `D-137`, `DIP-147`; requirements Provisional |
| AX-16 | Diplomacy (`B-08`) + Alliance | Candidate Position Feature; Open | `UD-047`; no delegation |
| AX-17 | Diplomacy (`B-08`) + Economy (`B-04`) | **Binding Inherited** constraint | `REQ-529`; no alliance override |
| AX-18 | Military (`B-10`, Future) | **Deferred** to Prompt 10 | Prompt 10 |
| AX-19 | Alliance Profile + Platform Security | Provisional Recommendation; Open | `UD-048`; zero-API boundary `D-133` |
| AX-20 | Alliance System (`B-09`) | Candidate Scope Proposal; Open | `UD-049`; zero chat `D-133` |
| AX-21 | Alliance + Platform Audit Spine | **Binding Inherited** audit infrastructure | `D-026`; `REQ-027` planned |
| AX-22 | Rankings & Chronicle (`B-11`, Future) | **Deferred** to Prompt 11 | Prompt 11 |
| AX-23 | Moderation & Fair Play (`B-12`, Future) | **Deferred** to Prompt 12 | Prompt 12 |
| AX-24 | Interface & Notifications (`B-13`, Future) | **Deferred** to Prompt 13 | Prompt 13; `UD-049` notice tool |
| AX-25 | Formula Register & Balance (`B-14`, Future) | Candidate Specifications; none approved | `UD-040`, `UD-043`, `UD-044`, `UD-046`; Prompt 14 |
| AX-26 | Market & Global Trade (`B-07`) | **Approved Mandatory Constraint** | `D-122`, `DD-136`, `REQ-513`, `G-1`–`G-6` |
| AX-27 | Economy & Treasury (`B-04`) + Alliance (`B-09`) | **Binding Owner-Authorized Constraint** | `D-140`, `DD-161`; `UD-046` untouched |
| AX-28 | Economy & Treasury (`B-04`) + Alliance (`B-09`) | **Binding Owner-Authorized Constraint** | `D-140`, `DD-161`; no withdrawal authority; `UD-046` untouched |
| AX-29 | Diplomacy (`B-08`) + Alliance (`B-09`) | **Binding Owner-Authorized Constraint** | `D-140`, `DD-162`; separate object; no delegation; `UD-047` untouched |
| AX-30 | Military (`B-10`, Future) + Alliance (`B-09`) | **Binding Design Contract** | `D-140`, `DD-163`; Prompt 10 implementation dependency |

**Reconciliation result.** After Prompt 09B-I there are 30 contracts: 1 approved (`AX-26`), 4 binding-inherited (`AX-10`, `AX-15`, `AX-17`, `AX-21`), 6 deferred (`AX-13`, `AX-14`, `AX-18`, `AX-22`, `AX-23`, `AX-24`), 3 binding owner-authorized additions (`AX-27`–`AX-29`), 1 binding design contract (`AX-30`) and 15 candidate/Open contracts. No earlier contract status was promoted or demoted, and the four additions do not decide anything outside `D-140`'s five authorized capabilities.

---

## 6. Accepted earlier-stage work preserved

| Work | Evidence of preservation |
|---|---|
| 09A four-document research base | All four documents remain referenced at their recorded versions; no finding was promoted to a rule; `UD-039` is recorded as resolved by `D-137` for B-08, not by research, and `D-140` separately authorizes the B-09 object |
| 26 `AX` identities from 09A | Contracts retain the original identities; 09B-C restored shifted contracts and 09B-E verified them; 09B-F did not renumber or delete any; 09B-I adds `AX-27`–`AX-30` without changing `AX-01`–`AX-26` |
| Prompt 09B-I owner authorization | `D-140` is confined to member taxation, voluntary donations, the separate Alliance-to-Alliance treaty object, NAP enforcement and the same-Alliance attack ban; `ALL-093` is a tombstone and `ALL-087`/`ALL-142`/`ALL-145` retain independent protections; `UD-040`/`UD-043`/`UD-044`/`UD-046`/`UD-047` remain Open |
| 08C diplomacy workflows and acceptance | 117-pair ledger, 54 edge cases, `DPA` matrix and 08C-E evidence remain; the `D-137` correction is confined to active diplomacy sections; historical records are preserved |
| B-02–B-08 rule identifiers | No `TR-`, `ACC-`, `ECN-`, `URB-`, `DMP-`, `MKT-` or `DIP-` rule was renumbered or deleted by 09B/09B-F |
| `D-135` / `DD-151` open-ended constitution | Still owner-approved; no mandatory Leader, Heir, council, rank tier, government model, succession model or amendment procedure |
| `UD-039` resolution | Still `D-137` for B-08: no B-08 alliance-level treaty object, zero diplomatic delegation; `D-140` adds the separate B-09 object without transferring national authority |
| 114 Alliance requirements | All 114 rows retained: the original 84 (71 Provisional / 12 Open / 1 Deferred) plus 30 Approved owner-authorized rows (30 Approved / 71 Provisional / 12 Open / 1 Deferred in total) |
| 30 AX contracts | The original 26 are retained with 21 fields each; `AX-27`–`AX-30` are appended by 09B-I with the same field structure; statuses are recorded in §5 |
| Global Trade decisions | `D-122`, `DD-136`, `REQ-513` and `G-1`–`G-6` remain unchanged and visible |
| `D-133` zero-chat / zero-Discord-API constraint | Preserved in `ALL-167`, `AX-19`, `AX-20`, `AX-24` |
| Historical progress-log sections | Sections §37–§45 and earlier historical claims remain; new entries are appended, not substituted |
| 09A research evaluation | The seventeen-area ledger remains at B-09 §28.1; 09B-F adds no retroactive approval |

---

## 7. Inconsistencies found and corrections made

### 7.1 The two principal authority defects

| Defect | Why it was a defect | Correction | Supporting authority | Verification |
|---|---|---|---|---|
| `ALL-057` recorded the earlier timestamp/workflow as deciding a succession claim | It resolved a competing claim and recognised a successor while `UD-043` is owner-reserved | Rewritten as "Competing Succession Claims — Audit Evidence Only": evidence is recorded; timestamp/transaction/workflow order decides nothing; no office or authority transfers; no adjudication; any resolution rule remains owner-reserved under `UD-043` | `UD-043` remains Open / Yes — owner; `D-028` only supplies account dormancy | Rule text read; validator `C24`; fixture A (timestamp succession rule) and fixture C (contract assigns authority by timestamp) fail |
| `REQ-551` required a declared appeal path ending in a recorded decision | It mandated an appeal mechanism while `UD-044` is owner-reserved | Rewritten: records retained; game never adjudicates merits; no appeal or dispute-resolution mechanism is required or approved while `UD-044` is Open; any future path requires owner approval | `UD-044` remains Open / Yes — owner | Requirement row read; validator `C25`; fixture B (mandatory appeal) and fixture D (appeal relocated to a contract) fail |

### 7.2 Other corrections made in the 09B-F cycle

| Document | Issue found | Correction | Authority / reason |
|---|---|---|---|
| `16_alliances.md` (`ALL-055`, `ALL-079`, `ALL-130`, `ALL-133`, `ALL-142`, `ALL-143`, `ALL-145`, `ALL-150`, `ALL-158`) | Candidate succession, member rights, ballots, discipline and abandonment language could be read as settled; `ALL-158`'s platform moderation appeal needed to remain legitimate | Candidate wording made explicit; member rights owner-reserved under `UD-044`; no automatic dissolution; platform moderation path kept | `UD-042`–`UD-044` Open; platform moderation is an inherited boundary |
| `03_requirements_traceability.md` (`REQ-013`, `REQ-551`, `REQ-568`, `REQ-569`) | Platform-imposed succession and mandatory appeal/expulsion/rejoin policy were implied | No platform succession model; no appeal/expulsion/rejoin mechanism in force; future policy conditional | `UD-043`, `UD-044` Open |
| `16_alliances_integration_contracts.md` (`AX-03`, `AX-04`, `AX-09`) | Dormancy, vacancy, succession and cooldown wording could transfer authority or enforce a candidate | "No office, authority or seat transfers automatically"; "none while `UD-043` is Open"; no fallback stewardship/caretaker/dissolution; membership rules not enforced while `UD-040`/`UD-044` open | `UD-043`, `UD-044` Open; `D-028` only |
| `16_alliances_formula_register.md` (`F-AL-003`) | The candidate vacancy formula could be read as an operative succession rule | Purpose conditional; "No declaration or consequence is in force"; no automatic dissolution or authority transfer; example transfers nothing | `UD-043` Open; candidate status |
| B-02 `TR-021` | Alliance visibility row implied native ballots | Conditional on candidate ballot scope under `UD-042`/`UD-049` | Owner-reserved scope |
| B-03 reroll row | Implied automatic office succession/vacancy | Records succession/vacancy as candidate under `UD-043`, not applied automatically | `UD-043` Open |
| B-04 `ECN-152` | Named "alliance dues" as if approved | "maintenance and any approved voluntary alliance contribution" | No dues policy approved |
| B-08 header | Stated "Prompt 08C … has not started" after 08C was completed | Status sentence corrected; 08C completion and its v1.3 authority recorded; no rule changed | 08C deliverable exists at v1.3 |
| `01_stage_2_prompt_roadmap.md` | Told Prompt 09 to "decide reuse, delegation or a separate object with a new D- entry" after `D-137` had resolved it | Replaced with the recorded `D-137` outcome: no B-08 alliance treaty object, zero delegation, `UD-039` Resolved; `D-140` later authorizes a separate B-09 object | `D-137`; `UD-039` register row |

No correction changed an approved security, sovereignty or audit constraint. No correction changed an owner-reserved status.

### 7.3 Validator false negatives found and corrected in Prompt 09B-G

The independent review identified that `C24` and `C25` could skip an entire sentence whenever a negation or conditional token appeared anywhere in it. A sentence such as "Timestamp ordering is not sufficient by itself, but the earliest claimant must become the successor" therefore passed while `UD-043` was Open. Prompt 09B-G corrected the validator, not the canonical documents:

| Aspect | Before 09B-G | After 09B-G | Verification |
|---|---|---|---|
| Unit of evaluation | Whole sentence; any `NEGATION`/`CONDITIONAL` match skipped it | `clauses()` splits contrastive/coordinated compounds (`but`, `however`, `yet`, `nevertheless`, `nonetheless`, `whereas`, `although`, `though`, `and`); only the clause containing the negation/conditional is skipped | Fixture G (succession disclaimer + mandate) fails `C24` and names `UD-043` and the earliest-claimant outcome |
| Succession order vocabulary | Timestamp, transaction order, chronological order, first claim | Adds `earliest claimant`, earlier recorded timestamp/claimant and time-of-record variants | Fixture G |
| Appeal/expulsion/rejoin mandate | Same sentence-level skip | Each clause evaluated; `C25` names `UD-044` and the offending entitlement | Fixture H (appeal disclaimer + entitlement) fails `C25` and names the right to appeal every expulsion |
| Positive controls | Negations and labelled proposals accepted implicitly | Seven explicit positives: direct prohibition; audit-only timestamp; labelled succession proposal; no approved appeal; conditional non-enforced appeal proposal; neutral recordkeeping; approved audit reference | Tests 81–87 pass without any `C24`/`C25` failure |
| Diagnostics | Check name and sentence | Check name, source document, owner-reserved decision and offending clause (truncated to 180 characters) | Failure messages observed in fixtures G and H |

The correction does not reject every mention of succession or appeals, does not treat every conditional as approved, and does not rely on a single keyword. Its limits are recorded in §11: the splitter is a deterministic heuristic, not a semantic parser.

---

## 8. Decisions and requirements deliberately unchanged

| Item | Why unchanged |
|---|---|
| `UD-040`–`UD-049` | Owner-reserved; only the owner may decide. 09B-F and 09B-G audited them, did not resolve or reclassify them |
| `D-135` / `DD-151` | Owner-approved open-ended constitution; no mandatory political model |
| `D-137` / `UD-039` | Resolved interface; no B-08 alliance treaty object and zero delegation; `D-140` adds a separate B-09 object |
| `D-122` / `DD-136` / `REQ-513` | Global Trade is approved mandatory product scope; release remains gated |
| `G-1`–`G-6` | Gate definitions and statuses unchanged; G-4 remains partial, the others not met |
| `REQ-176` / `ECN-213` | Binding inherited conservation and audit; requirement remains Provisional |
| `D-028` / 168 turns | Confirmed account-dormancy lattice; not an alliance office rule |
| `D-133` / `DD-147` | No real-time chat, Discord bot, API, OAuth, webhook or account linking |
| 114 Alliance requirements | Text corrected where defective; the 30 `D-140`-authorised rows are Approved, the other 84 keep their prior status; `REQ-591` stays Deferred to Prompt 10 |
| 26 `AX` contracts | Statuses preserved; no contract promoted |
| 09C authorization | Remains blocked pending independent acceptance; no 09C deliverable was created |

---

## 9. Unresolved owner-only decisions relevant to this audit

| Decision | Subject | Current status | Effect of the reservation |
|---|---|---|---|
| `UD-040` | Founding eligibility, fee, single-alliance rule | Open; Yes — owner | No fee, eligibility rule, anti-sybil control or one-alliance enforcement is in force |
| `UD-041` | Default government model and office set | Open; Yes — owner | No mandatory Leader, Heir, council or template; Primary Administrative Contact is technical |
| `UD-042` | Charter and native voting | Open; Yes — owner | Charter storage is allowed; native ballots are not first-release scope |
| `UD-043` | Succession, resignation, removal, inactivity | Open; Yes — owner | No fallback leader, default heir, automatic stewardship, vacancy resolution or threshold is in force |
| `UD-044` | Member rights, expulsion, appeal, rejoin | Open; Yes — owner | No expulsion mechanism, appeal procedure, rejoin cooldown or blacklist is in force |
| `UD-045` | Capability catalogue granularity and delegation limits | Open; Yes — owner | The 23-capability catalogue is candidate; no rank-based caps or temporary delegation is approved |
| `UD-046` | Treasury ownership, capacity, withdrawals, dual approval | Open; Yes — owner | No pool, ownership, capacity, threshold, withdrawal workflow or dual signature is in force |
| `UD-047` | Collective diplomatic positions | Open; Yes — owner | Non-binding positions are candidate; no delegation or collective treaty authority |
| `UD-048` | Discord invite visibility and validation | Open; Yes — owner | No link field, default visibility, allowlist or validation policy is approved |
| `UD-049` | Announcements and formal votes in first release | Open; Yes — owner | No bulletin, notice, native vote or announcement feature is committed |

---

## 10. Cross-document synchronization and verification evidence

**Historical 09B-J snapshot.** The table below records what was verified at the Prompt 09B-J pass and is retained unchanged as history. Prompt 09B-K re-verified the same boundaries and its evidence is recorded in §13; where a count or version in this table differs from §13, §13 is current.

| Check | Result |
|---|---|
| B-09, contracts and formula register headers | Synchronized to Prompt 09B-J: B-09 v2.5, contracts v2.5 (`AX-01`–`AX-30`), formula register v2.5 (`F-AL-001`–`F-AL-007`); mandated status sentence present; no owner-reserved status changed |
| Requirements register | v1.26 revision note records the Prompt 09B-J clarifications; counts unchanged at 647 = 49 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed; the Alliance block is 114 = 30 Approved / 71 Provisional / 12 Open / 1 Deferred |
| Decision registers | 140 project decisions and 163 design positions; UD counts unchanged at 26 Resolved / 5 Deferred / 18 Open; UD-039 remains resolved by D-137 and amended in part by D-140; UD-040–UD-049 remain Open, with UD-046/UD-047 only partially authorized |
| `DECISIONS.md` | `D-140` added as Confirmed; it records the five owner-authorized capabilities, the `D-137` partial amendment, the ALL-093 withdrawal and the untouched reservations |
| Continuity and handoffs | Mandated status sentence retained; 09C remains blocked; progress log gains §45 (09B-J); prior sections preserved |
| Global Trade preservation | `D-122`, `DD-136`, `REQ-513`, `G-1`–`G-6` present and unchanged; no "ready/live/released" claim |
| Production-code prohibition | No production source, schema, migration, API, screen or deployment created; sanctioned `prototypes/` remain outside scope |
| Semantic validator | `python docs/qa_backups/09B_validate_alliance_semantic.py` — exit 0; **31/31 checks passed**. `C25` now evaluates the complete policy assertion (main clause, exceptions, unless/except branches, polarity and plain permissive/procedural/access modals); `C27`–`C31` cover taxation, donations, the ALL-093 tombstone, Alliance treaties/NAP consent and the same-Alliance attack ban |
| Isolated tests | `python docs/qa_backups/test_09B_alliance_semantic_validator.py` — **Ran 177 tests in 1194.447 s; OK; exit 0** in the complete suite run. Earlier targeted runs: tests 142–157 (C25) passed in 97.133 s; tests 158–176 (09B-J tax, treaty, NAP and attack hardening) passed together with the revised 05/110/112/132 fixtures in 146.569 s plus a 5.882 s re-run for 164. Fixtures A–P fail for the intended reasons; structural tests 132–141 and 164–166, 171–172 and 174–175 remove a required tax, donation, treaty, whole-dissolution, bidirectional-NAP or mandatory-audit term; tests 142–157 add the five audited C25 escapes and their controls; tests 158–163 and 167–170, 173 and 176 exercise current-turn-only base, fixed-10% restriction, capacity rejection, fixed-office and unauthorized-role guards, executable-prose and automatic-joiner-coverage guards, and positive controls; all fixtures copy the corpus to temporary directories and never modify the real documents |
| 09B-I fixtures N–P | N (`must not deny appeal rights`), O (`must not create or deny … except that`) and P (`must not create or deny … unless`) each fail `C25` with `UD-044` and the asserting clause; the bare holding statement and neutral recordkeeping controls pass |
| 09B-J C25 fixtures | The five audited escapes ("Members may appeal an expulsion", "An expelled member can appeal the expulsion decision", "Every expelled member may appeal", "An appeal may be lodged within the review window", "The expelled member has access to an appeal process") each fail `C25` with `UD-044`; denial, conditional, negation-in-clause, compound disclaimer-plus-grant, `except`, procedural-duty and subordinate-clause controls also fail; the unresolved-proposal, recordkeeping, no-rejoin-rule and treaty-consent-after-rejoin positives pass |
| 09B-I reservation re-audit | `UD-040`–`UD-049` remain `Yes — owner` / `Open`; the B-09 §27 ledger rows remain Open; 114 Alliance requirements = 30 Approved / 71 Provisional / 12 Open / 1 Deferred; `REQ-551` anchors intact; `UD-039` still resolved by `D-137`, amended only by `D-140`; `ALL-093` grants no right or power |
| 09A validator/tests | `python docs/qa_backups/09A_validate_alliance.py` — exit 0; **911 checks passed**. `python docs/qa_backups/test_09A_alliance_validator.py` — exit 0; **Ran 43 tests in 31.351 s; OK** |
| Stage 2/global validator | `python docs/qa_backups/09_validate.py` — exit 0; **358/358 checks passed**. `python docs/qa_backups/validate_final.py` — exit 0; all checks passed. `python docs/qa_backups/validate_final.py --self-test` — exit 0; **10/10 guards detect their defect** |
| Decision-register tests | `python docs/qa_backups/test_decision_registers.py` — exit 0; **Ran 12 tests in 0.041 s; OK** |
| Next-action tests | `python docs/qa_backups/test_next_action.py` — exit 0; **Ran 23 tests in 0.121 s; OK** |
| Alliance arithmetic verifier | `python docs/qa_backups/verify_alliance_numbers.py` — exit 0; **217 checked, 0 failed**; `--self-test` — exit 0; **22/22 guards detected their defect**. It recomputes F-AL-006 (rate sweep, non-10 rates, separate asset rates, different brackets, floor, 100%, 0% fallback, conservation, ARL-once, retry, conflicting key) and F-AL-007 (conservation, replay, two equal donations, insufficient/unsupported, no capacity term), then checks the B-09/REQ/D-140/DD-161/AX/UD-046 anchors. These are documentation checks, not runtime ledger tests |
| Subsystem numeric/workflow checks | Politics 879/879; market arithmetic all passed; 07C workflows all passed; diplomacy numbers 9 groups / 0 failed; diplomacy workflows 17 groups / 0 failed; economy 164/164; cities 267/267 — all exit 0. No skipped tests and no warnings were reported by these scripts. |

---

## 11. Limitations, risks and remaining work

1. **Documentary agreement is not design quality.** The validator and this audit can show that the documents do not contradict each other or the owner's reservations. They cannot show that the alliance experience is balanced, understandable or complete.
2. **No runtime evidence exists.** Every requirement remains unimplemented and untested. Planned validation is not execution.
3. **UI/UX is deferred.** Prompt 09C and Prompt 13 own screens, workflows, accessibility and asynchronous interaction flows. No interface specification exists yet.
4. **Warfare, rankings, moderation and formula calibration are deferred** to Prompts 10–14. Their Alliance contracts are placeholders with declared owners, not implemented behaviour.
5. **Free-tier architecture is measured, not proven.** No true concurrency, backup/restore drill, auth flow, 24-hour run or load test exists for the eventual game (Report 11 §15.8; Report 12 §2.1).
6. **The owner still owns ten policy questions.** The design can proceed around them, but no implementation should treat a candidate as settled.
7. **Independent acceptance is still pending.** This report is evidence for that review, not a substitute for it.
8. **The clause splitter and policy classifier are heuristics, not a semantic parser.** `C24`/`C25` split on a fixed set of contrastive and coordinating markers. `C25` evaluates each clause segment independently, does not skip a clause merely because it contains a negation or conditional, and checks the main clause, exceptions and unless/except branches for a positive entitlement, a denial, an appeal-as-expulsion-condition, a passive appeal procedure or access to one. An adversarial sentence that states a mandate in a separate sentence with no negation token, or hides it behind unusual punctuation or an unlisted conjunction, may still evade the check. The validator is a regression guard for the documented defect class, not a proof that no contradictory policy can ever be worded.
9. **The five 09B-I capabilities are specified, not implemented.** Taxation, donations, Alliance treaties, NAP enforcement and the same-Alliance attack ban exist only as rules and contracts. 09B-J corrects taxation to automatic per-turn production withholding and confines receipts to credit-only accounting under an Open UD-046; 09B-K aligns the three contaminated failure codes, adds the ambiguous-membership 0% safeguard and fixes post-tax production-chain accounting. No database, API, attack validator, UI or runtime test exists, and Prompt 10 must implement and test the attack checks before any enforcement claim can be made.

---

## 12. Audit conclusion

The corrected Alliance documents now distinguish **technical evidence** from **political authority**, and **record-keeping** from **adjudication**. `ALL-057` records competing claims without deciding them; `REQ-551` retains records without mandating an appeal. Every other inspected reference to `UD-040`–`UD-049` is either a binding inherited constraint, a clearly labelled candidate, or a conditional/negated statement that preserves the owner's reservation. The earlier-stage work, the 30 contracts, the 114 Alliance requirements, the Global Trade decisions and gates, and the open-ended constitution remain preserved. Prompt 09B-I adds the five owner-authorized capabilities under `D-140`; Prompt 09B-J corrects the taxation model to automatic per-turn production withholding, adds player-authored brackets and role-governed freeze, confines receipts to a credit-only ledger, corrects NAP non-covered membership and closes the remaining C25 plain-modal escapes; both leave `UD-040`, `UD-043`, `UD-044`, `UD-046` and `UD-047` Open and change no earlier-stage rule.

**Verdict for this audit:** the documentary conditions within the primary writer's authority are satisfied. Prompt 09B-G removed the two demonstrated validator false negatives, and the exact disclaimer-plus-mandate sentences now fail with diagnostics naming `UD-043`/`UD-044`; seven positive controls confirm that legitimate prohibitions, audit records and labelled proposals still pass. Prompt 09B-I closes the N/O/P exception and unless-branch false negatives and adds the five owner-authorized Alliance capabilities with permanent fixtures and positive controls. Prompt 09B-J closes the remaining plain-modal, passive-procedure and access-to-appeal escapes, corrects the taxation model to automatic per-turn production withholding and the NAP non-covered-membership rule, and preserves every owner reservation. Prompt 09B-K closes the five positive appeal-grant escapes through semantic grant-family detection, rewrites the three contaminated failure codes, names the credit-only ARL in `REQ-626`, adds the reversible ambiguous-membership 0% safeguard while `UD-040` stays Open, and fixes post-tax production-chain accounting without changing any national economy rule. **Prompt 09B is not independently accepted and Prompt 09C remains blocked.** The owner and independent reviewer decide acceptance.

---

## 13. Prompt 09B-K verification evidence (current)

**Current-state note.** This section is the 09B-K evidence record and supersedes §10 where a version, count or result differs; §10 remains the historical 09B-J snapshot. Prompt 09B-K changed no rule, requirement, formula, decision, contract or test identifier. It corrected the `C25` classifier, three failure-code meanings, one requirement destination term, the provisional multiple-membership tax safeguard and the production-chain accounting, then re-ran the checks in §13.3.

### 13.1 Corrections verified

1. **`C25` positive appeal grants.** The five audited statements (`Every expelled member receives an opportunity to appeal.`, `The member's right to appeal is established.`, `Expelled members are afforded an appeal.`, `Appeals are available to expelled members.`, `An expelled member may file an appeal.`) all grant an appeal entitlement without `must` or `shall`. The prior classifier evaluated imperative wording and a narrow denial/procedure vocabulary, could return safe on a sentence-level neutral holding, and skipped a clause containing a negation or conditional marker. `C25` now splits the policy assertion into main, subordinate and exception branches; evaluates each branch for positive grant families (receipt/benefit, establishment/existence, availability/access, opportunity/ability, bare-verb provision and bare permissive modal) and for denial/restriction families (prohibition, no-right, unavailability, denial of opportunity, restriction); treats institutional duty (`must provide an appeal`) as a grant while `must not grant` remains a denial; and exempts only text explicitly marked historical, explanatory, disclaimer, reserved, illustrative, fixture, rejected-proposal or non-enforced proposal. The validator contains no five-sentence special-case list; the audited sentences exist only as test fixtures.
2. **Permanent `C25` fixtures.** Tests 177–198 (22 tests) cover the five statements plus `Every member is permitted to appeal.`, `The platform guarantees an appeal opportunity.`, `An appeal right exists for expelled members.`, `Expelled members have access to an appeal procedure.`, `No appeal is available to an expelled member.` and `The platform must not grant any appeal right.`; they also cover disclaimer→entitlement, entitlement→disclaimer, subordinate entitlement, compound entitlement, historical mention, rejected proposal, illustrative fixture, negated historical framing, an `only` restriction and create-or-deny controls. Each fixture asserts the exact validator outcome. The earlier `C25` fixtures, `C24` and the positive controls remain unchanged and pass.
3. **`ALF-21`.** The failure is a rejected bracket, rate or assignment change because the authenticated actor lacks the required active alliance tax permission, or because authorization or version validation failed; nothing was collected. Individual national-owner consent is not required, and authenticated role authorization is not weakened.
4. **`ALF-23`.** The failure is a missing, incomplete or inconsistent authoritative gross figure, frozen turn snapshot or production record, or a failed atomic paired-ledger commit. No existing stockpile or balance is charged, no partial collection exists and a retry cannot create a second charge.
5. **`ALF-24`.** A donation is rejected for an unsupported or invalid asset, insufficient donor unreserved value, missing/failed/stale authorization or confirmation, a conflicting duplicate settlement, or an atomic Alliance Receiving Ledger credit failure. An exact replay returns the original receipt. No destination-capacity limit exists or is assumed.
6. **`REQ-626` and the ARL.** The donation destination is the **Alliance Receiving Ledger**; 09B-L supersedes the earlier credit-only wording with the four-category receipt/accounting record and its single purpose-limited operational debit. Tax and donation text, `F-AL-007`, `AX-28` and this audit use that term. The ARL implies no ownership or custody, and `UD-046` remains **Open**.
7. **Multiple membership.** `ALL-179`, `ALL-185`, `ALL-186`, `F-AL-006`, `AX-27`, `ECN-213a`, `REQ-624` and `REQ-625` state: one eligible production event is deducted at most once; no asset loses more than 100% of gross; multiple membership never authorizes multiple deductions; no Alliance receives priority; unresolved or unestablishable attribution produces a visible, recorded 0% Alliance-tax fallback for the affected asset and turn, with gross credited in full, no Alliance credited, the reason visible to the member and authorized Alliance roles, normal collection at the first later unambiguous turn, and no retroactive re-tax of a safeguarded turn. The safeguard is reversible and does not resolve `UD-040`. Ten scenarios exercise it: single alliance collection, two memberships no stacking, different rates no priority, repeated settlement once, leaving one alliance with history preserved, boundary-only membership change, non-retroactive joining, visible 0% fallback, later unambiguous collection, and no combination above 100% of gross.
8. **Production chain.** The required sequence is (1) capture the frozen snapshot, (2) establish authoritative gross current-turn production, (3) apply the per-asset rate and attribution, (4) credit the ARL exactly once, (5) credit net national available, (6) let later same-turn P3 stages consume only the post-tax net, and (7) write atomic paired events, receipt and audit. Existing B-04 economy figures are used; no parallel engine exists. `F-AL-006` examples A–G show: 0% leaves 100 available; 50% leaves 50; 100% leaves 0; a production chain totals 107; an existing stockpile of 500 plus 100 current production at 50% pays 50 and leaves 550; a transformed processing input is not re-taxed; a retry leaves the total ARL credit at 50, never 100. Rates remain any integer 0–10,000 bp; no universal ceiling below 100% is invented; stockpiled resources consumed later are not taxed and a newly generated different output is taxed once at its own rate.

### 13.2 Current identifier state

| Check | Current result |
|---|---|
| B-09 | v2.6, 29 sections, `ALL-001`–`ALL-219`; `F-AL-001`–`F-AL-007`; `ALF-01`–`ALF-26`; `AX-01`–`AX-30` |
| Requirements register | v1.27; **647 = 49 Approved / 578 Provisional / 17 Open / 3 Deferred / 0 Proposed**; Alliance block **114 = 30 Approved / 71 Provisional / 12 Open / 1 Deferred** |
| Decision registers | 140 `DECISIONS.md` rows; DD register v3.8 with 163 rows (128 Approved / 26 Provisional / 3 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred); UD register v1.22 with 26 Resolved / 5 Deferred / 18 Open |
| `D-140` | Confirmed owner-authorized capability; 09B-K re-verifies without broadening it; `D-137` amended only in its no-object component; zero diplomatic delegation remains |
| Reserved questions | `UD-040`, `UD-044`, `UD-046` and `UD-047` remain **Open / Yes — owner**; no candidate is promoted by repetition |
| Production code | None created; no schema, migration, API, screen, deployment or runtime test exists |

### 13.3 Executed verification

All commands below were run from the repository root with the project Python environment; each reported exit code 0. No test was skipped, no timeout is reported as a pass, and the isolated suite result is the complete 210-test run, not a selected subset. The complete suite was executed after every rule, formula, contract, requirement, decision, economy and continuity document was final; only the result rows in this audit and in the progress log were written afterward, and neither file is read by any validator. The suite's reported elapsed time includes a host sleep/suspend during the run, so it measures wall-clock time rather than test execution time.

| Command | Actual result |
|---|---|
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | exit 0; **31/31 checks passed** |
| `python docs/qa_backups/verify_alliance_numbers.py` | exit 0; **269 checked, 0 failed** — includes the ten membership scenarios and chain examples A–G |
| `python docs/qa_backups/verify_alliance_numbers.py --self-test` | exit 0; **31/31 guards detected their defect** |
| `python docs/qa_backups/test_09B_alliance_semantic_validator.py` | exit 0; **Ran 210 tests in 27,210.874 s; OK** — complete suite; the elapsed time includes a host sleep, so it is not a measure of test execution time |
| `python docs/qa_backups/09A_validate_alliance.py` | exit 0; **911 checks passed** |
| `python docs/qa_backups/test_09A_alliance_validator.py` | exit 0; **Ran 43 tests in 28.708 s; OK** |
| `python docs/qa_backups/09_validate.py` | exit 0; **358/358 checks passed** |
| `python docs/qa_backups/validate_final.py` | exit 0; all checks passed |
| `python docs/qa_backups/validate_final.py --self-test` | exit 0; **10/10 guards detect their defect** |
| `python docs/qa_backups/test_decision_registers.py` | exit 0; **Ran 12 tests in 0.041 s; OK** |
| `python docs/qa_backups/test_next_action.py` | exit 0; **Ran 23 tests in 0.124 s; OK** |
| `python docs/qa_backups/verify_politics_numbers.py` | exit 0; **879/879 arithmetic checks**; `--self-test` **18/18** |
| `python docs/qa_backups/verify_market_numbers.py` | exit 0; **95/95 checks passed** |
| `python docs/qa_backups/verify_market_workflows.py` | exit 0; **14/14 checks passed** |
| `python docs/qa_backups/verify_diplomacy_numbers.py` | exit 0; **9 groups / 0 failed** |
| `python docs/qa_backups/verify_diplomacy_workflows.py` | exit 0; **17 groups / 0 failed** |
| `python docs/qa_backups/verify_economy_numbers.py` | exit 0; **164/164** |
| `python docs/qa_backups/verify_city_numbers.py` | exit 0; **267/267** |

**Isolated-suite content.** The 210 tests comprise the earlier 177-test suite plus tests 177–198 (`C25` grants and controls) and 199–209 (`ALF-21`, `ALF-23`, `ALF-24`, `REQ-626`/ARL, at-most-once deduction, ambiguous-attribution fallback, chain total 107, `AX-27` post-tax consumption, `ECN-213a` safeguard and two positive controls). Fixtures copy `docs/` to a temporary directory and never modify the real corpus.

### 13.4 Limits

1. These are documentary and arithmetic checks. They do not prove the Alliance design is balanced, complete or usable, and they are not independent acceptance.
2. `C25` remains a heuristic classifier. An adversarial sentence that hides a grant behind unusual punctuation, an unlisted conjunction or a non-policy framing may still evade it; the tests are a regression guard for the documented defect class, not a semantic proof.
3. The 210-test suite and the arithmetic verifier are specification fixtures, not runtime ledger, API or UI tests. No production implementation exists.
4. Prompt 09C remains blocked pending independent acceptance of Prompt 09B. The owner and independent reviewer decide acceptance.

---

## 14. Prompt 09B-L consolidated correction record (2026-11-02)

**Status:** correction completed by the primary writing agent; independent acceptance review pending. This section is an audit record, not an approval.

1. **Automatic Alliance taxation reconciled.** `ALL-006` separates national and municipal tax settings from the Alliance's automatic per-turn production tax and states that an Alliance cannot change either; `ALL-007` preserves the authorized source withholding while retaining the bans on confiscation, stockpile access, unauthorized withdrawals or spending, transfers and national financial-policy changes; `ALL-008` distinguishes automatic tax withholding, voluntary donations and every other ordinary transfer. `ALL-087`/`ALL-088` and the §14 treasury introduction carry the same boundary. No per-policy owner consent was reintroduced.
2. **ARL and operational funding.** The ARL is a receipt/accounting record in `RECEIVED`/`AVAILABLE`/`RESERVED`/`EXPENDED` categories, not a treasury ownership decision. `ALL-220`–`ALL-226`, `REQ-648`–`REQ-653`, `F-AL-008`, `AX-27` and `ALF-27`–`ALF-29` specify one purpose-limited operational debit to a registered platform cost sink under the closed `AOP-01`–`AOP-04` registry, with authorization, permission, schedule, idempotency, receipt, reconciliation and duplicate-payment protection. No member distribution, player payment, general withdrawal, debt or negative balance exists.
3. **Owner reservations preserved.** `UD-045` records only the narrow role-based tax-management permission set and remains Open for the wider catalogue, delegation and governance. `UD-046` records automatic tax receipt, ARL accounting and the narrow operational mandate and remains Open for ownership, custody, capacity, general withdrawal, general spending beyond the mechanism, distributions, unrestricted transfers and dual approval. Neither is closed or reclassified; `UD-040`, `UD-044` and `UD-047` remain Open.
4. **Semantic validator and treaty effects.** `C25` now detects retained, preserved, reviewable, avenue-based, opportunity-based and negative-polarity appeal assertions across active, passive, subordinate, conditional and compound formulations while preserving genuine historical, disclaimer, fixture and `UD-044`-reserved text. `C32` guards the ARL/operational-funding boundary and the narrow `UD-045` scope; `C33` guards the `AT-E00` record-only and `AT-E01` NAP effect catalogue; `C34` guards the national/municipal tax boundary and the authorized-withholding distinction. The validator now runs 34 checks against B-09 v2.7, 653 requirements and 164 decision rows.
5. **Verification.** `09B_validate_alliance_semantic.py` passes 34/34; `verify_alliance_numbers.py` passes 318/318 with self-test 31/31; the 09B suite retains tests 0–209 and adds 210–252 (253 tests) and completed on 2026-11-02 with `python docs/qa_backups/test_09B_alliance_semantic_validator.py -v` → **Ran 253 tests in 1,658.410 s, OK, exit 0**. An earlier complete run exposed a stale fixture in `test_55_dd_tally_regression_fails` that still expected the pre-09B-L `128` tally; the fixture now mutates the current `129` tally to `128` and requires rejection, and the suite was rerun in full. The exact commands and results are recorded in progress log §47 item 14 and the Prompt 09B-L report; a timeout is never reported as a pass.
6. **Limits.** These are documentary/arithmetic checks against a specification. No tax engine, ARL, treaty service or attack-enforcement code exists; no runtime or integration test demonstrates those mechanics. `C25` remains a heuristic with a conservative review gate, not a universal semantic proof.

---

## 15. Prompt 09B-M/09B-N acceptance-closeout record (2026-11-02)

**Status:** correction completed by the primary writing agent; independent acceptance review pending. This section is an audit record, not an approval. It records the final two corrections identified by the independent 09B-M audit and the status synchronization they required; it changes no owner-approved rule.

1. **The two audited `C25` false negatives are closed.** In `09B_validate_alliance_semantic.py`, `APPEAL_VIOLATION_PATTERNS` gained recourse formulations: `has/have/had/gains/gets/obtains/is given/are given recourse to (appellate) review|appeal|reconsideration`, and `right|entitlement of|to recourse to …`. `appeal_subject()` now treats redress/remedy wording as appeal-adjacent only when a member, nation, player, applicant or expulsion/removal subject is present. `non_policy_context()` now scrubs people labels (`former members`, `rejected applicants`, `previous nations`, and similar) before applying the historical/disclaimer exemption, so a label about people cannot immunise a live-sounding entitlement. `appeal_policy_issue()` still evaluates each policy segment and each colon/dash-introduced clause, and `appeal_review_issue()` evaluates the same segments for uncertain wording. The banner now names Prompt 09B-N; no check identifier, rule, contract, formula, requirement or decision was renumbered.
2. **Uncertain redress wording routes to manual review.** `APPEAL_REVIEW_PATTERNS` gained four redress/remedy patterns covering `entitled/eligible to seek|request|pursue|obtain|apply for redress|a remedy|remedies`, modal `may/can/might/could seek …`, `right/entitlement/opportunity/avenue/route/access/recourse … to|of|for redress|remedy|remedies`, and `has/have/retains/preserves/maintains … redress|remedy|remedies`. A match produces `[C25][REVIEW]` in `review_findings`; it is not a failure and not a pass. `main()` returns exit 1 when either `failures` or `review_findings` is non-empty, so an unreviewed match cannot be reported as clean.
3. **The three outcomes are preserved.** A confirmed policy assertion is **FAIL** (`[C25]` in `failures`); plausible but uncertain appeal/review/redress wording is **MANUAL REVIEW** (`[C25][REVIEW]` in `review_findings`); genuine historical, explanatory, rejected-proposal, non-operative fixture and `UD-044`-reserved text is **SAFE** (no entry). The conservative gate is deliberate: the detector matches meaning-bearing patterns and context, not an exhaustive phrase list, and its limitations are documented rather than presented as universal natural-language understanding.
4. **Permanent acceptance tests 257–259.** `test_257_recourse_and_former_member_challenge_fail` expects and obtains **FAIL** for `ZZ-N1` “Members have recourse to appellate review”, `ZZ-N2` “Former members may challenge their expulsion by review” and `ZZ-N3` “Former members may not appeal their expulsion”. `test_258_redress_wording_requires_manual_review` expects and obtains **MANUAL REVIEW** for `ZZ-N4` “A former member is entitled to seek redress”, `ZZ-N5` “… pursue a remedy” and `ZZ-N6` “Former members may seek redress”. `test_259_former_people_label_and_compound_sentences` expects and obtains **SAFE** for `ZZ-N7` “Former rules allowed members to appeal expulsion”, `ZZ-N8` “Former members historically could appeal under an old rule” and `ZZ-N9` “Whether former members may appeal remains open under UD-044”, and **FAIL** for `ZZ-N10` “This historical note is not operative, but members may appeal expulsion” and `ZZ-N11` “The record is historical; former members may appeal expulsion”. The suite is now **260 tests**; no earlier test was removed, weakened or skipped.
5. **History and authority are unchanged.** `D-140` (2026-11-01) remains the historical five-capability authorization and `D-141` (2026-11-02) its dated successor for the narrow purpose-limited operational-funding boundary; neither was merged, backdated or reworded. `UD-040`–`UD-049` remain Open / Yes — owner, with only the documented partial authorizations: `UD-045` keeps the narrow role-based tax-management permission set, `UD-046` keeps only automatic tax receipt, ARL accounting and the narrow operational mandate, and the separate B-09 Alliance-to-Alliance treaty/NAP framework is authorized by `D-140` without delegation while `UD-047` remains Open for collective positions and any delegation model. No owner-reserved decision was closed. `ALL-006`–`ALL-008`, the four-category ARL, the 0–10,000 bp tax rates, the `AOP-01`–`AOP-04` registry, the `AT-E00`/`AT-E01` catalogue, B-08 national treaty sovereignty and `REQ-530` are unchanged.
6. **Inventory after the patch.** 653 requirements = 55 Approved / 578 Provisional / 17 Open / 3 Deferred, of which 120 Alliance requirements = 36 / 71 / 12 / 1; 164 design-decision rows (129 Approved); UD register v1.23 = 49 rows = 26 Resolved / 5 Deferred / 18 Open; 30 `AX-01`–`AX-30` integration contracts; `F-AL-001`–`F-AL-008`; `ALF-01`–`ALF-29`; 34 semantic checks `C01`–`C34`.
7. **Testing evidence actually obtained by this patch.** The 34/34 semantic validator run, the three new tests and the documentation checks below were executed on 2026-11-02 after the final edits:
   - `python docs/qa_backups/09B_validate_alliance_semantic.py` → `[PASS] All 34 semantic checks passed with no review findings.`, exit 0, 7.342 s.
   - `python docs/qa_backups/test_09B_alliance_semantic_validator.py -k test_257_` → Ran 1 test in 7.620 s, OK, exit 0.
   - `python docs/qa_backups/test_09B_alliance_semantic_validator.py -k test_258_` → Ran 1 test in 7.363 s, OK, exit 0.
   - `python docs/qa_backups/test_09B_alliance_semantic_validator.py -k test_259_` → Ran 1 test in 7.509 s, OK, exit 0.
   - A temporary selection runner outside the repository, selecting test names in the C24/C25/appeal families and the 09B-M/09B-N acceptance range, reported `SELECTED 83 TESTS`, `Ran 83 tests in 618.901 s`, `OK`, `RESULT run=83 failures=0 errors=0 skipped=0`, exit 0.
   - `python docs/qa_backups/validate_final.py` → `VALIDATION: ALL CHECKS PASSED`, exit 0, 1.110 s.
   - `python docs/qa_backups/09_validate.py` → `358/358 checks passed`, exit 0, 0.914 s.
   - `python docs/qa_backups/verify_politics_numbers.py` → `879/879 checks passed`, exit 0, 0.419 s.
   - `python docs/qa_backups/verify_alliance_numbers.py` → `375 passed, 0 failed`, exit 0, 0.450 s.
   - **Historical, not rerun by this patch:** the earlier complete suite `python docs/qa_backups/test_09B_alliance_semantic_validator.py -v` ran **257 tests in 1,833.109 s: OK, exit 0** on 2026-11-02 before the 09B-N fixtures existed. It is retained as historical evidence with its original command, result and date; it is not presented as a 09B-N execution. The full 260-test suite was not rerun for this documentation-only acceptance patch.
8. **Maturity distinction.** The Alliance design and the two C25 corrections are **specified** and **designed**; the semantic and documentation checks above are **documentation tests executed and passed**. There is **no implementation**: no tax engine, ARL, treaty service, permission service, attack enforcement, migration, API or UI exists, and no runtime or integration test demonstrates these mechanics. Phase 09B is **ready for independent acceptance**, not independently accepted, and Prompt 09C remains **blocked** until that acceptance completes.

## 16. Prompt 09B-O/09B-P corrections and the Phase 09B acceptance record (2026-11-03)

**Status:** **Phase 09B Alliance specification and documentation: ACCEPTED.** Accepted at the specification/documentation level (D-142 / DD-165). This section is an audit record, **not an approval**: the acceptance is recorded by D-142/DD-165 on the owner-directed alignment pass, and the audit evidence below is cited by that record. The `§15` statement that 09B was then “ready for independent acceptance, not independently accepted” remains accurate **as of 2026-11-02**; acceptance was recorded afterwards and does not rewrite that history.

1. **09B-O closed eight procedural C25 false negatives.** The bounded person/action/normative-force gate classifies petition for reconsideration, permitted review, mandatory hearing, subject-to-reconsideration, right to challenge removal, request for review, fixed denial of review and petition for redress. `test_260` encodes seven **FAIL** fixtures (`ZZ-O1`–`ZZ-O7`) and one **MANUAL REVIEW** fixture (`ZZ-O8`); `test_261` adds ten controls (active grants/denials **FAIL**, ambiguous remedy **REVIEW**, rejected-proposal, `UD-044`-reserved, unrelated-budget and unrelated-strategy text **SAFE**). The repository preserves no separate 09B-O execution log, so **no 09B-O run beyond the permanent fixture definitions is claimed**.
2. **09B-P closed the three remaining audited false negatives.** `test_262` (`ZZ-P1`, ambiguous challenge to dismissal) and `test_263` (`ZZ-P2`, unspecified grievance process) expect **MANUAL REVIEW**; `test_264` (`ZZ-P3`, express right to seek redress for an expulsion) expects **FAIL**; `test_265` adds six compact controls. Only Python compilation, those four tests, the affected C25 group and relevant C24 controls were executed — **not the complete suite**. The isolated suite now contains **266 tests**; no earlier test was removed, weakened or skipped.
3. **Acceptance scope.** Acceptance covers the canonical B-09 rulebook (`16_alliances.md` v2.8), its formula register and integration contracts, requirements `REQ-534`–`REQ-653`, the `ALL-*`, `AX-01`–`AX-30`, `AT-*`, `ALF-*`, `AUD-AL-*` and `F-AL-*` identifiers as specified, and the independent review findings already applied by 09B-N, 09B-O and 09B-P. It is **not** production implementation, live-game integration testing, release or operational readiness; it is **not** a new owner authorization; and it resolves or closes **no** unresolved decision.
4. **Owner decisions unchanged.** `D-140` and `D-141` retain their historical and dated scopes. `UD-040`–`UD-049` remain **Open / Yes — owner**; the partial authorizations are unchanged — `UD-045` keeps only the narrow role-based tax-management permission set, `UD-046` only automatic tax receipt, ARL accounting and the narrow operational mandate, and `D-140` the separate B-09 Alliance-to-Alliance treaty/NAP framework without delegation while `UD-047` remains Open for collective positions and any delegation model. `UD-044` (expulsion and appeal) is not decided by acceptance. `D-014` was not used to override an owner reservation.
5. **Inventory after the acceptance record.** 653 requirements = 55 Approved / 578 Provisional / 17 Open / 3 Deferred, of which 120 Alliance requirements = 36 / 71 / 12 / 1; design-decision register `D-001`–`D-142` with **165** DD rows (130 Approved); UD register v1.24 = 49 rows = 26 Resolved / 5 Deferred / 18 Open; 30 `AX-01`–`AX-30` contracts; `F-AL-001`–`F-AL-008`; `ALF-01`–`ALF-29`; 34 semantic checks `C01`–`C34`.
6. **Prompt 09C is registered, not executed.** The roadmap registers **Prompt 09C — Alliance workflows, edge cases, acceptance matrix and release-gate evidence** with canonical deliverable `docs/stage-2/16_alliances_workflows_acceptance.md`. That file **does not exist** and was not created by this pass; no 09C workflow or test was executed, and no new 09B redesign or research is authorized. The `C19` guard continues to reject premature 09C deliverables.
7. **Maturity distinction preserved.** The Alliance design is **specified, documented and accepted at that level**; the semantic and documentation checks are **documentation tests executed and passed**. There is still **no implementation**: no tax engine, Alliance Receiving Ledger service, treaty service, NAP check, attack validator, permission service, migration, API or UI exists. Prompt 09C, Prompts 10–15, assembly, production implementation, live-game integration testing and release all remain pending.
