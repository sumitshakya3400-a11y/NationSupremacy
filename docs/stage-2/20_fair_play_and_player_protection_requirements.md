# B-12 — Fair play, privacy, moderation and administration: requirement register

**Version:** 1.0 · **Created:** 2026-11-07 · **Stage 2, Prompt 12B**
**Status:** **Global requirement records `REQ-764`…`REQ-869`. Design status only; none is implemented, tested or released.**
**Authority.** This register owns the B-12 requirement records and the `12A-CR` → `REQ` disposition. The [B-12 rulebook](20_fair_play_and_player_protection.md) owns the rules; the [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) owns the calculations. The canonical ledger [03_requirements_traceability.md](03_requirements_traceability.md) carries the same identifiers and one-line summaries.
**Companions.** [B-12 rulebook](20_fair_play_and_player_protection.md) · [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) · [B-12 acceptance](20_fair_play_and_player_protection_acceptance.md) · [12A requirement candidates](research/12A_requirements_integration_and_risk_registers.md) · [decisions](../DECISIONS.md) · [unresolved decisions](05_unresolved_design_decisions.md).

**Allocation.** `REQ-764`…`REQ-869` are allocated one-to-one from `12A-CR-001`…`12A-CR-106`: `REQ = 763 + CR`. No identifier is skipped, duplicated or renumbered. `REQ-763` remains the previous frontier. No identifier beyond `REQ-869` is allocated or reserved by this pass.

**Status.** **86 Provisional** design requirements and **20 Open** requirements whose owner or legal dependency is unresolved. None is Approved: D-014 permits a design decision, not an owner policy approval. The 20 Open rows are `REQ-782`, `795`, `808`, `809`, `812`, `816`, `817`, `830`, `831`, `837`, `842`, `843`, `844`, `846`, `849`, `855`, `857`, `867`, `868`, `869`.

**Preserved.** `D-163`…`D-177`, `DD-211`…`DD-225`, `UD-017`, `UD-052`…`UD-060` and every existing requirement are unchanged. The 14 pre-existing Prompt-12-owned rows (`REQ-004`, `019`, `023`–`031`, `037`, `043`, `748`) are extended by reference, not renumbered.

---

## 1. Disposition of the 106 candidates

Every candidate is **adopted** with adapted normative wording. None is rejected or merged because the 12A review already consolidated overlap; the exact one-to-one mapping preserves auditability. A candidate that restated approved policy remains a new design requirement, not a new approval.

| 12A candidate | Global | Disposition | Status |
|---|---|---|---|
| `12A-CR-001`…`12A-CR-106` | `REQ-764`…`REQ-869` | Adopted one-to-one, wording converted to normative requirement form | 86 Provisional / 20 Open |

---

## 2. Requirement records, part 1 — identity and authority

| ID | Statement | Type | Pri | Status | Authority or decision basis | Rationale |
|---|---|---|---|---|---|---|
| REQ-764 | Every value the game acts on is computed server-side from authoritative state; a client value is intent only | Security | A | Provisional | FP-011; SEC-010; D-032; 12A-CR-001 | Removes whole cheat classes rather than detecting them |
| REQ-765 | Each protected value has exactly one owning subsystem and no other writer path | Security | A | Provisional | FP-012; D-064; 12A-CR-002 | Closes the single-writer defect class |
| REQ-766 | A finding uses exactly one of five evidence states; below established violation only reversible prevention is permitted | Operations | B | Provisional | EVD-001; EVD-002; D-167; 12A-CR-003 | Prevents a signal being treated as a finding |
| REQ-767 | A behavioural anomaly alone is never a violation and needs one independent non-behavioural source | Operations | A | Provisional | EVD-004; D-018; 12A-CR-004 | Anomaly detection is evadable and unfair alone |
| REQ-768 | The corpus and player text distinguish suspicion, policy violation, confirmed exploitation, deliberate cheating, unintentional breach and legitimate unusual behaviour | Governance | B | Provisional | FP-018; FP-019; 12A-CR-005 | One vocabulary prevents disproportionate language |
| REQ-769 | Every write validates the acting session and authorizes each referenced object separately | Security | A | Provisional | SEC-001; SEC-002; D-032; 12A-CR-006 | Object and function authorization failures are common |
| REQ-770 | Every value-changing operation is atomic, idempotency-keyed and revalidated at effect | Security | A | Provisional | FP-013; SEC-003; SEC-004; 12A-CR-007 | Duplicate settlement is the highest-value mechanical risk |
| REQ-771 | Idempotency-key retention is expressed in turns and covers the longest legitimate retry path | Security | A | Provisional | SEC-003; F-FP-010; 12A-CR-008 | A short window converts a retry into a new action |
| REQ-772 | No outcome depends on submission order; the published deterministic catalogue governs | Security | A | Provisional | FP-014; SEC-018; TR-048; 12A-CR-009 | A hard close produces timing competition |
| REQ-773 | A value-protecting limit is enforced in the write transaction, not only in the browser, edge or RLS | Security | A | Provisional | SEC-004; SEC-012; 12A-CR-010 | Edge limits are approximate and RLS can be bypassed |
| REQ-774 | A response contains only fields the requester's class entitles them to receive | Privacy | A | Provisional | FP-015; PRV-007; TR-021; 12A-CR-011 | Information cheats are server-created leaks |
| REQ-775 | Abuse counters key to the account and protected resource; a network attribute affects triage only | Security | A | Provisional | EVD-005; SEC-007; NET-039; D-168; 12A-CR-012 | IP-keyed control over-punishes CGNAT and mobile users |
| REQ-776 | Every control declares its failure direction; value, authorization and audit writes fail closed | Reliability | A | Provisional | SEC-009; FR-001; FR-002; 12A-CR-013 | One global posture is wrong for some class |
| REQ-777 | One person holds one account; multiple controlled accounts are prohibited; no identity-proof claim is made | Policy | A | Provisional | MA-001; D-018; D-032; REQ-043; 12A-CR-014 | Restates approved policy without overclaiming |
| REQ-778 | Network association alone never supports more than the lowest preventive tier or a permanent measure | Policy | A | Provisional | EVD-005; MA-005; NET-039; 12A-CR-015 | Independent operators reached the same ceiling |
| REQ-779 | A player may record a shared-context declaration naming associated accounts | Policy | B | Provisional | MA-003; D-169; D-033; 12A-CR-016 | Converts an unknowable fact into attested evidence |
| REQ-780 | A shared-context declaration is visible only to its author and the integrity role and is deletable | Privacy | B | Provisional | MA-004; PRV-021; DAT-009; 12A-CR-017 | A declaration names third parties and must not leak |
| REQ-781 | Multi-account offences are drafted as flow and outcome offences, not as proof of common control | Policy | B | Provisional | MA-006; CO-001; D-172; 12A-CR-018 | The project cannot prove identity |
| REQ-782 | Value may be corrected against either or both sides of an established beneficial flow | Policy | B | **Open** | MA-007; COR-003; D-165; UD-052; 12A-CR-019 | Correction reach is owner-reserved |
| REQ-783 | Ban evasion is a named violation with its own evidence requirement and is not inferred from a shared network | Policy | B | Provisional | MA-008; V-05; 12A-CR-020 | Without it the ladder has an obvious hole |
| REQ-784 | Cooperation is not collusion; listed legitimate behaviours are never indicators by themselves | Policy | A | Provisional | FP-018; CO-002; D-170; 12A-CR-021 | Collusion rules that punish cooperation destroy play |
| REQ-785 | The collusion boundary is manufactured false agency, stated as one player-testable rule | Policy | A | Provisional | CO-001; D-170; 12A-CR-022 | One sentence beats a list players cannot self-assess |
| REQ-786 | Collusion indicators are structural and outcome-shaped and use only data already written for gameplay | Operations | B | Provisional | CO-003; EVD-016; 12A-CR-023 | No new collection is needed |
| REQ-787 | Graph or clustering output is queue input only and never raises a tier by itself | Operations | A | Provisional | CO-004; 12A-CR-024 | Friends and rings look structurally alike |
| REQ-788 | Alliance-scale similarity is a documented false-positive class, not evidence | Operations | B | Provisional | CO-002; EVD-014; 12A-CR-025 | Large coordination is an emergent property |
| REQ-789 | Where a rule, cap or mechanism change can meet the purpose, it is chosen before surveillance | Policy | B | Provisional | FP-016; D-177; 12A-CR-026 | Prevention is cheaper and fairer than detection |
| REQ-790 | Automated rules may create only a review object, reversible hold or value correction | Operations | A | Provisional | EVD-003; D-167; 12A-CR-027 | No automated path from signal to conduct finding |
| REQ-791 | Every detection rule declares its false-positive classes and minimum corroboration before enabling | Operations | B | Provisional | EVD-015; EVD-014; 12A-CR-028 | A rule without declared FPs is unauditable |
| REQ-792 | The false-positive catalogue covers shared households, institutions, public and mobile networks, CGNAT, VPN, travel, families, schedules, alliances and mechanics | Operations | B | Provisional | EVD-014; 12A-CR-029 | Every listed class is common in a browser game |
| REQ-793 | No universal confidence score exists; sufficiency is a stated corroboration matrix and human review | Operations | A | Provisional | EVD-007; EVD-010; 12A-CR-030 | A score without a validated method is false precision |
| REQ-794 | A case record names evidence, rules, reviewer, decision, date and outcome including inconclusive | Operations | B | Provisional | EVD-012; EVD-020; 12A-CR-031 | A closed case must be reconstructible |
| REQ-795 | A reviewer with a declared interest is excluded; an unsegregated case is labelled and disclosed | Operations | B | **Open** | EVD-019; MOD-021; UD-054; 12A-CR-032 | Staffing and independence are owner-reserved |
| REQ-796 | Detection reads only existing gameplay, security or legally required data; no new surveillance is introduced | Privacy | A | Provisional | EVD-016; PRV-025; D-042; 12A-CR-033 | The privacy posture is the principal defence |
| REQ-797 | A capability requiring refused data is recorded as unavailable, not softened into a weaker claim | Governance | A | Provisional | EVD-017; FP-008; 12A-CR-034 | Softened claims become false promises |
| REQ-798 | One three-axis classification model assigns every field exactly one value on each axis | Privacy | A | Provisional | PRV-001; PRV-003; D-171; 12A-CR-035 | Three registers already classify fields differently |
| REQ-799 | Existing class assignments are reconciled in the owning register, not silently reassigned | Privacy | A | Provisional | PRV-003; D-171; 12A-CR-036 | Reassignment without a decision is a quiet edit |
| REQ-800 | Each restricted read states its purpose and the requirement that authorises it | Privacy | A | Provisional | PRV-004; PRV-005; DAT-004; 12A-CR-037 | Convenience causes over-broad access |
| REQ-801 | Cross-class information flows are declared separately from read permissions | Privacy | B | Provisional | PRV-004; PRV-006; D-017; D-030; 12A-CR-038 | Read permission and flow control are different |
| REQ-802 | Every published aggregate names its quasi-identifiers and inference argument and satisfies k at least 5 | Privacy | A | Provisional | PRV-018; D-027; 12A-CR-039 | Dropping QIs can raise apparent k falsely |
| REQ-803 | No surface reveals another player's restriction, investigation, verification or appeal state | Privacy | B | Provisional | PRV-019; MOD-018; D-042; 12A-CR-040 | Disclosure is a privacy harm and harassment vector |
| REQ-804 | Failure messages identify the failed condition without revealing a rule, threshold, another player's data or account existence | Privacy | A | Provisional | PRV-020; 12A-CR-041 | Error text is an information channel |
| REQ-805 | A single data inventory states owner, purpose, use, access role, three-axis class, retention, erasure limit, deletability and one-account need | Privacy | A | Provisional | PRV-023; PRV-024; DAT-001; 12A-CR-042 | The inventory exists but its columns are incomplete |
| REQ-806 | Derived identifiers are labelled pseudonymous with a written identifiability assessment | Privacy | A | Provisional | PRV-024; D-036; 12A-CR-043 | A keyed digest over a small space is still personal data |
| REQ-807 | The pseudonymisation secret is held outside the database, owned, rotated and excluded from repository, logs and backups | Privacy | A | Provisional | PRV-024; D-036; 12A-CR-044 | Key custody separates minimisation from reversal |
| REQ-808 | Retention is per class with a justification and review trigger; no new day-count is adopted | Privacy | A | **Open** | PRV-023; D-026; UD-017; UD-055; 12A-CR-045 | Legal review owns the periods |
| REQ-809 | The conflict between erasure and the permanent audit spine is recorded with both obligations and a conservative branch | Privacy | B | **Open** | PRV-022; PRV-023; UD-055; 12A-CR-046 | Two genuine obligations collide |
| REQ-810 | Missing managed backups and the sensitivity of the owner-run export are recorded as open exposures | Operations | B | Provisional | FR-014; CF-02; D-025; 12A-CR-047 | Missing backups are an availability risk |
| REQ-811 | Prohibited conduct is classified once in the sixteen-class `V-01`…`V-16` taxonomy | Operations | B | Provisional | FP-017; Annex A; 12A-CR-048 | Enforcement cannot be proportionate without classification |
| REQ-812 | Exactly one six-tier ladder exists, with one numbering, authority, evidence, notice and appeal per tier | Operations | B | **Open** | MOD-036; MOD-037; UD-053; 12A-CR-049 | Two incompatible ladders exist and the scale is owner-reserved |
| REQ-813 | Severity uses stated factors and never counts an unconfirmed accusation as a prior | Operations | B | Provisional | MOD-039; FP-025; 12A-CR-050 | Proportionality requires explicit factors |
| REQ-814 | Exploit and incident handling runs separately from conduct; a first honest report is an incident | Operations | B | Provisional | FP-027; MOD-001; 12A-CR-051 | Punishing reporters loses intelligence |
| REQ-815 | The owning subsystem's rule and evidence remain authoritative for its capability | Governance | A | Provisional | FP-004; MOD-031; 12A-CR-052 | Prevents double jeopardy and authority overlap |
| REQ-816 | No penalty type, amount or duration is approved merely because a category exists | Operations | B | **Open** | MOD-037; MOD-038; UD-053; 12A-CR-053 | A category is not a penalty |
| REQ-817 | Value and standing correction is a distinct class from restriction and suspension | Operations | B | **Open** | MOD-051; D-165; UD-052; 12A-CR-054 | Correction is cheaper and fairer than culpability |
| REQ-818 | A correction or restriction attaches to the account and survives a nation reroll | Operations | A | Provisional | MOD-033; D-039; 12A-CR-055 | Otherwise reroll resets a sanction |
| REQ-819 | Enforcement touching another subsystem uses that subsystem's appended correction path | Security | A | Provisional | FP-012; COR-004; TR-091; 12A-CR-056 | Direct state editing is the insider mechanism |
| REQ-820 | Duplicate or conflicting enforcement is surfaced to a reviewer rather than silently applied or dropped | Operations | B | Provisional | MOD-032; COR-007; 12A-CR-057 | Concurrent corrections are unhandled today |
| REQ-821 | A sanction record states the rule, evidence class, tier, end condition and appeal route in usable terms | Operations | B | Provisional | MOD-017; MOD-018; 12A-CR-058 | An incomprehensible sanction is not defensible |
| REQ-822 | Report intake captures structured fields and stores the report as an accusation | Operations | B | Provisional | MOD-002; EVD-013; 12A-CR-059 | Structured intake is affordable at this staffing |
| REQ-823 | Duplicate reports cluster; coordinated volume affects reporter trust, never the reported party's tier | Operations | B | Provisional | MOD-003; F-FP-008; 12A-CR-060 | Brigading must not convert volume into severity |
| REQ-824 | A knowingly false report is a violation; a good-faith unsubstantiated report is not | Operations | B | Provisional | MOD-004; V-15; 12A-CR-061 | Reporting must not become a harassment weapon |
| REQ-825 | A report against an administrator is routed confidentially; retaliation is a named violation | Operations | B | Provisional | MOD-005; MOD-006; 12A-CR-062 | The ordinary path fails for administrator cases |
| REQ-826 | Player-supplied evidence is a pointer corroborated against server records; if impossible, the case is inconclusive | Operations | A | Provisional | EVD-013; EVD-023; 12A-CR-063 | Screenshots alone are insufficient |
| REQ-827 | Evidence used in a finding is identified by provenance, producer, time and integrity reference | Security | B | Provisional | EVD-023; EVD-036; 12A-CR-064 | A finding must be reconstructible |
| REQ-828 | Every access, annotation, correction and export of evidence is itself an audit event | Security | B | Provisional | EVD-022; EVD-026; 12A-CR-065 | Chain of custody defends against tampering claims |
| REQ-829 | Audit and case records are tamper-evident: chained digests, scheduled verification and incident on failure | Security | B | Provisional | EVD-030; EVD-031; F-FP-012; 12A-CR-066 | Append-only by convention is not evidence |
| REQ-830 | Deletion required by law closes a case with a recorded redaction and preserves the fact of removal | Privacy | B | **Open** | EVD-038; PRV-022; UD-055; 12A-CR-067 | Deletion and integrity obligations collide |
| REQ-831 | Evidence is retained only for case need, minimised, and absent from logs, analytics and default views | Privacy | B | **Open** | EVD-024; PRV-021; UD-055; 12A-CR-068 | Evidence retention is the largest privacy expansion |
| REQ-832 | Conflicting server records are recorded and resolved explicitly, never silently adopted | Operations | B | Provisional | EVD-018; 12A-CR-069 | Conflicting records are inevitable |
| REQ-833 | Every account-affecting action is appealable once, stays in force pending decision and receives a reasoned outcome | Operations | B | Provisional | MOD-042; MOD-043; MOD-045; 12A-CR-070 | The appeal minimum is approved policy |
| REQ-834 | Reopening requires new evidence or a procedural defect; a repeat appeal is closed and recorded | Operations | B | Provisional | MOD-046; 12A-CR-071 | Without a bar appeals become stalling |
| REQ-835 | The appeal explanation is sufficient to contest and withholds method, thresholds and third-party data by rule | Operations | B | Provisional | MOD-018; MOD-045; 12A-CR-072 | Disclosure tension is explicit |
| REQ-836 | An upheld appeal triggers reversal, appended record correction and owning-subsystem restitution | Operations | B | Provisional | MOD-047; MOD-048; 12A-CR-073 | A hollow reversal makes appeal meaningless |
| REQ-837 | The design states which independence guarantees exist and labels an unsegregated appeal | Operations | B | **Open** | MOD-049; UD-054; 12A-CR-074 | Independence is a staffing fact |
| REQ-838 | Administrative roles are defined by a prohibition list as much as by permitted actions | Governance | A | Provisional | ADM-001; D-173; 12A-CR-075 | The prohibition list is the control |
| REQ-839 | Every administrative capability is named and individually granted; there is no superuser | Governance | A | Provisional | ADM-002; ADM-005; 12A-CR-076 | A superuser is the standard shortcut |
| REQ-840 | Privileged action requires a step-up session, separately logged and independently revocable | Security | B | Provisional | ADM-007; 12A-CR-077 | Operator credentials are the highest-value target |
| REQ-841 | A privileged read of a restricted record is an auditable event with purpose, target and actor | Security | A | Provisional | ADM-008; EVD-026; 12A-CR-078 | Four registers demand this and none implements it |
| REQ-842 | No administrator acts against their own account, nation or Alliance without second approval or recorded disclosure | Governance | B | **Open** | ADM-009; UD-054; 12A-CR-079 | Self-dealing is the insider pattern |
| REQ-843 | Investigation and final conduct decision are distinct permissions | Governance | B | **Open** | ADM-010; UD-054; 12A-CR-080 | Investigator-decides is the default at one-person staffing |
| REQ-844 | Configuration author and publisher are separated, or the substitute disclosure and review are recorded | Governance | B | **Open** | ADM-011; UD-054; 12A-CR-081 | Configuration-to-publication is one step today |
| REQ-845 | Financial correction is executed by the ledger under a reason code, never by an administrator typing a balance | Governance | A | Provisional | ADM-012; COR-002; 12A-CR-082 | Treasury correction is where favouritism pays |
| REQ-846 | Where separation is impossible, the gap is declared with its compensating control | Governance | A | **Open** | ADM-013; UD-054; 12A-CR-083 | Claiming an unavailable control is worse than naming the gap |
| REQ-847 | Emergency powers are enumerated, time-bounded and self-expiring | Governance | B | Provisional | MOD-025; MOD-026; F-FP-016; 12A-CR-084 | Unlimited emergency authority becomes permanent |
| REQ-848 | Emergency measures may suspend, freeze or withhold but not delete, confiscate, transfer or rewrite history | Governance | B | Provisional | MOD-025; 12A-CR-085 | The irreversible action must not be the easy one |
| REQ-849 | Every emergency action is retrospectively reviewed and the outcome recorded | Governance | B | **Open** | MOD-028; UD-054; 12A-CR-086 | Review is the affordable substitute for pre-approval |
| REQ-850 | Players are told a temporary measure is in force and when it will be reviewed | Operations | B | Provisional | MOD-027; 12A-CR-087 | Silent intervention destroys trust |
| REQ-851 | A single named audit event set covers privileged access, permissions, evidence, enforcement, appeals, overrides, emergency, corrections and configuration | Security | A | Provisional | EVD-026; EVD-027; 12A-CR-088 | The audit requirement is spread across nine documents |
| REQ-852 | Audit records contain identifiers, decisions and reasons, never content bodies, secrets or raw credentials | Security | A | Provisional | EVD-028; 12A-CR-089 | The log's omissions are protective |
| REQ-853 | Spine rows are never sampled away; value, pipeline, privileged and enforcement rows are retained first | Security | A | Provisional | EVD-034; 12A-CR-090 | Quota pressure is how integrity logging disappears |
| REQ-854 | Audit access is restricted, purpose-bound, registered and logged | Security | B | Provisional | EVD-033; PRV-015; 12A-CR-091 | Readable by all is not evidence; readable by none is not accountability |
| REQ-855 | Audit correction is an appended event; obligation deletion is recorded with its authority | Security | A | **Open** | EVD-029; EVD-038; UD-055; 12A-CR-092 | Correction and deletion must remain distinguishable |
| REQ-856 | Incident classes are separated and each declares posture, authority, disclosure owner and preservation step | Security | B | Provisional | SEC-024; FR-001; 12A-CR-093 | One blended class fails every posture |
| REQ-857 | A suspected personal-data breach is assessed and documented whether or not it is reported onward | Privacy | B | **Open** | SEC-025; UD-017; 12A-CR-094 | Documenting a non-report is a regulator expectation |
| REQ-858 | A suspected integrity failure halts resolution rather than continuing doubtfully, and is disclosed as a delay | Reliability | A | Provisional | SEC-026; D-025; 12A-CR-095 | Continuing multiplies damage |
| REQ-859 | B-12 owns policy, evidence, access, audit shape and enforcement, and no gameplay mechanic or outcome | Governance | A | Provisional | FP-004; INT-001; 12A-CR-096 | Prevents a universal controller |
| REQ-860 | Existing subsystem integrity obligations are consumed by reference, not restated | Governance | A | Provisional | INT-003; INT-009; 12A-CR-097 | Duplication guarantees divergence |
| REQ-861 | No B-12 rule creates a new entitlement, protection, reward, capacity, treasury right or diplomatic effect | Governance | A | Provisional | FP-004; INT-008; 12A-CR-098 | Enforcement must not mint entitlements |
| REQ-862 | Failure posture is per category, never global | Reliability | A | Provisional | FR-001; D-175; 12A-CR-099 | Opposite answers are correct for different classes |
| REQ-863 | Detection downtime does not block play, silently remove protection or lose reconstructible records | Reliability | B | Provisional | FR-003; FR-004; 12A-CR-100 | Detection is not value authority |
| REQ-864 | Unavailable enforcement evidence yields a reversible hold, never a permanent measure | Reliability | B | Provisional | SEC-023; FR-005; 12A-CR-101 | The reversible action is the only defensible one |
| REQ-865 | Wrong account association has a correction path that separates accounts, lifts restrictions, records and notifies | Reliability | B | Provisional | EVD-018; COR-013; 12A-CR-102 | Misattribution is the most damaging failure |
| REQ-866 | The corpus states what it does not claim: no identity proof, guaranteed detection, surveillance, executed test or implemented control | Governance | A | Provisional | FP-008; GOV-024; 12A-CR-103 | Overclaiming is the recorded failure mode |
| REQ-867 | Enforcement practice is reviewed periodically against capacity and observed false-positive rate | Governance | C | **Open** | MOD-035; UD-054; 12A-CR-104 | Policy without a review loop is a guess kept forever |
| REQ-868 | A public transparency structure is defined; publication remains an owner decision | Governance | C | **Open** | PRV-018; UD-058; 12A-CR-105 | Publishing counts builds trust; publishing cases destroys privacy |
| REQ-869 | A legal dependency is named with its owner and the design takes the conservative branch | Governance | A | **Open** | GOV-009; GOV-016; UD-017; 12A-CR-106 | Deciding law by default creates unintended obligations |

---

## 3. Requirement records, part 2 — constraints, behaviour and verification

| ID | Preconditions and constraints | Expected system behaviour | Responsible subsystem | Dependencies and related decisions | Verification and acceptance criteria | Owner or legal dependency | Intended delivery stage |
|---|---|---|---|---|---|---|---|
| REQ-764 | Authenticated session; server state available | Compute value server-side and reject client outcome assertions | B-02/B-04 owning services | D-032, SEC-010, FP-011 | Negative client-value test design | None | Stage 5 |
| REQ-765 | Owning map declared | Reject a write from any non-owner path; record attempt | Owning subsystem | D-064, FP-012, `12A-RK-007` | Schema and grant enumeration | Stage 5 | Stage 5 |
| REQ-766 | Evidence state recorded | Select consequence from state; block above-state action | B-12 | D-167, EVD-002 | Case-table fixture | None | Stage 5 |
| REQ-767 | One behavioural source | Open review only; require independent source | B-12 | D-018, EVD-004 | Corroboration matrix fixture | None | Stage 5 |
| REQ-768 | Player-facing text exists | Use the six terms consistently; never call suspicion a finding | B-12/Prompt 13 | FP-019 | Text review | Prompt 13 | Stage 5/13 |
| REQ-769 | Object reference supplied | Authorize actor, object and function separately | B-02/Stage 6 | D-032, SEC-002 | Endpoint matrix | Stage 5/6 | Stage 5 |
| REQ-770 | Value action submitted | One atomic transaction; duplicate coalesces | Owning service | SEC-003, SEC-004 | Concurrency test design | Stage 5 | Stage 5 |
| REQ-771 | Retry path declared | Retain key for `P_r + 1` turns at minimum | B-02/owning service | F-FP-010, SEC-003 | Boundary replay design | None | Stage 5 |
| REQ-772 | Turn window closes | Resolve by catalogue, not arrival | B-02 | TR-048, SEC-018 | Ordering review | None | Stage 5 |
| REQ-773 | Value write occurs | Enforce limit in same transaction | Owning service | SEC-004, SEC-012 | Direct denial test design | Stage 5 | Stage 5 |
| REQ-774 | Requester class known | Build response from allowed fields only | Every read service | PRV-007, TR-021 | Response-shape review | Stage 5 | Stage 5/13 |
| REQ-775 | Counter incremented | Key to account and resource; IP only triage | B-03/B-12 | NET-039, D-168 | Counter-key review | None | Stage 5 |
| REQ-776 | Control can fail | Apply declared direction; no silent re-derivation | Every service | SEC-009, FR-001 | Failure-injection design | Stage 5 | Stage 5 |
| REQ-777 | Account created | Enforce one active nation; no identity claim | B-03 | D-018, D-032, REQ-043 | Lifecycle test design | None | Stage 5 |
| REQ-778 | Network signal present | Cap at lowest preventive tier; never permanent | B-12 | NET-039, EVD-005 | Ladder review | None | Stage 5 |
| REQ-779 | Player records declaration | Store as review evidence; grant nothing | B-12 | D-169, D-033 | Journey design | None | Stage 5/12C |
| REQ-780 | Declaration exists | Restrict to author and integrity role; allow deletion | B-12 | PRV-021, DAT-009 | Access matrix review | None | Stage 5 |
| REQ-781 | Flow evidenced | Charge the flow, not assumed identity | B-12/B-04 | D-172, MA-006 | Flow-offence review | None | Stage 5 |
| REQ-782 | Beneficial flow established | Correct either or both sides under the owner's reach decision | B-04/B-12 | UD-052, D-165 | Ledger simulation | Owner (`UD-052`) | Blocked until owner |
| REQ-783 | Restriction and evading use evidenced | Open `V-05`; never infer from IP alone | B-12/B-03 | D-041, MA-008 | Case-type review | None | Stage 5 |
| REQ-784 | Cooperative act alleged | Apply manufactured-false-agency test; dismiss if absent | B-12 | D-170, CO-002 | Negative fixture list | None | Stage 5 |
| REQ-785 | Collusion alleged | State the one-sentence boundary in the notice | B-12 | D-170, CO-001 | Text review | None | Stage 5 |
| REQ-786 | Data already recorded | Compute structural indicators only | B-12 | CO-003, EVD-016 | Data-flow review | None | Stage 5 |
| REQ-787 | Graph output exists | Queue only; no tier increase | B-12 | CO-004 | Queue design review | None | Stage 5 |
| REQ-788 | Alliance-scale pattern observed | Record as false-positive class | B-12 | CO-002, EVD-014 | Catalogue entry | None | Stage 5 |
| REQ-789 | Abuse class identified | Record cheaper control or the gap | B-12/Prompt 14 | D-177, CO-002 | Alternative review | Prompt 14 | Stage 5/14 |
| REQ-790 | Automated rule fires | Emit permitted output only | B-12 | D-167, EVD-003 | Pipeline fixture | None | Stage 5 |
| REQ-791 | Rule proposed | Require FP classes and corroboration declaration | B-12 | EVD-015 | Rule-register check | None | Stage 5 |
| REQ-792 | Catalogue maintained | Include all named classes | B-12 | EVD-014 | Completeness check | None | Stage 5 |
| REQ-793 | Finding proposed | Apply matrix; no universal score | B-12 | EVD-007, EVD-010 | Matrix fixture | None | Stage 5 |
| REQ-794 | Case closed | Record evidence, rules, reviewer, date and outcome | B-12 | EVD-012, EVD-020 | Case-schema review | None | Stage 5 |
| REQ-795 | Conflict exists | Exclude or label unsegregated and disclose | B-12 | UD-054, MOD-021 | Case audit | Owner (`UD-054`) | Blocked until owner |
| REQ-796 | Detection reads data | Use only inventoried existing data | B-12 | D-042, EVD-016 | Inventory review | None | Stage 5 |
| REQ-797 | Capability needs refused data | Record unavailable; no proxy | B-12 | FP-008, EVD-017 | Claim scan | None | Stage 5 |
| REQ-798 | Field inventoried | Assign one value on each axis | B-12/all systems | D-171, PRV-001 | Field audit | None | Stage 5 |
| REQ-799 | Conflict found | Resolve in owning register with dated decision | Owning register | PRV-003 | Diff review | None | Stage 5 |
| REQ-800 | Restricted read occurs | State purpose and authorising requirement | Every role | PRV-004 | Permission-purpose map | None | Stage 5 |
| REQ-801 | Cross-class flow occurs | Declare flow separately and validate | B-12/all systems | PRV-004, PRV-006 | Flow-table review | None | Stage 5 |
| REQ-802 | Aggregate published | Name QIs, show inference, enforce k | B-11/B-12 | D-027, PRV-018 | Aggregate audit | None | Stage 5 |
| REQ-803 | Surface renders | Omit other-party status | Prompt 13 | D-042, PRV-019 | Surface enumeration | Prompt 13 | Stage 13 |
| REQ-804 | Failure rendered | State condition only | Every service | PRV-020 | Message catalogue | None | Stage 5 |
| REQ-805 | Field inventoried | Populate all columns; state retention | B-12 | DAT-001, PRV-023 | Column completeness | Legal for periods | Stage 5 / legal |
| REQ-806 | Derived identifier created | Label pseudonymous; write assessment | B-03/B-12 | D-036, PRV-024 | Labelling check | None | Stage 5 |
| REQ-807 | Secret exists | Separate custody; rotate; exclude from logs | Stage 5/6 | D-036, PRV-024 | Custody review | Stage 5/6 | Stage 5/6 |
| REQ-808 | Class retention stated | Use existing periods only; name review trigger | B-12 | D-026, UD-017, UD-055 | Retention table review | Legal (`UD-017`,`UD-055`) | Blocked until legal |
| REQ-809 | Erasure request conflicts | Preserve both obligations; take conservative branch | B-12 | UD-055, PRV-022 | Register review | Legal and owner (`UD-055`) | Blocked |
| REQ-810 | Backup posture stated | Disclose no managed backup and export sensitivity | Operations | CF-02, D-025 | Status statement | Owner (CF-02) | Stage 3 |
| REQ-811 | Conduct classified | Use `V-01`…`V-16` only | B-12 | FP-017, Annex A | Taxonomy completeness | None | Stage 5 |
| REQ-812 | Sanction considered | Use one ladder with one authority and evidence per tier | B-12 | UD-053, MOD-036 | Ladder review | Owner (`UD-053`) | Blocked until owner |
| REQ-813 | Severity assessed | Apply factors; exclude unconfirmed priors | B-12 | MOD-039, FP-025 | Case audit | None | Stage 5 |
| REQ-814 | Exploit reported | Treat first honest report as incident; separate lanes | B-12 | FP-027, MOD-001 | Policy review | None | Stage 5 |
| REQ-815 | Capability affected | Defer to owning rule and evidence | Owning subsystem | MOD-031, FP-004 | Boundary review | None | Stage 5 |
| REQ-816 | Penalty proposed | Propose rationale; do not claim approval | B-12 | UD-053, MOD-037 | Ladder review | Owner (`UD-053`) | Blocked until owner |
| REQ-817 | Correction considered | Record separately from sanction | B-12/B-04 | UD-052, D-165 | Ledger path review | Owner (`UD-052`) | Blocked until owner |
| REQ-818 | Account sanctioned | Attach to account; survive reroll | B-03/B-12 | D-039, MOD-033 | Lifecycle review | None | Stage 5 |
| REQ-819 | Other state affected | Append through owner's correction path | Owning subsystem | TR-091, COR-004 | Permission enumeration | None | Stage 5 |
| REQ-820 | Duplicate action detected | Surface to reviewer | B-12 | MOD-032, COR-007 | Conflict fixture | None | Stage 5 |
| REQ-821 | Sanction recorded | State rule, evidence, tier, end and appeal | B-12 | MOD-017 | Schema review | None | Stage 5 |
| REQ-822 | Report submitted | Capture structure; store as accusation | B-12 | MOD-002, EVD-013 | Form review | None | Stage 5/13 |
| REQ-823 | Duplicate reports arrive | Cluster; no tier increase from volume | B-12 | F-FP-008 | Cluster fixture | None | Stage 5 |
| REQ-824 | Report false or unsubstantiated | Distinguish intent; no penalty for good faith | B-12 | MOD-004, V-15 | Policy text review | None | Stage 5 |
| REQ-825 | Subject is administrator | Route confidentially; treat retaliation as violation | B-12 | MOD-005, MOD-006 | Routing fixture | None | Stage 5 |
| REQ-826 | Player evidence supplied | Corroborate server records; inconclusive if impossible | B-12 | EVD-013, EVD-023 | Corroboration fixture | None | Stage 5 |
| REQ-827 | Artefact used | Record provenance, producer, time, digest | B-12 | EVD-023, EVD-036 | Reference check | None | Stage 5 |
| REQ-828 | Evidence accessed | Append audit event | B-12/B-02 | EVD-022, EVD-026 | Custody event check | None | Stage 5 |
| REQ-829 | Spine specified | Chain digests; schedule verification; escalate break | B-02/B-12 | EVD-030, F-FP-012 | Design review; no runtime | Stage 5 | Stage 5 |
| REQ-830 | Deletion obligation exists | Record redaction and authority | B-12 | UD-055, EVD-038 | Redaction fixture | Legal (`UD-055`) | Blocked |
| REQ-831 | Evidence retained | Minimise, case-scope, exclude from defaults | B-12 | UD-055, EVD-024 | Copy-path review | Owner (`UD-055`) | Blocked |
| REQ-832 | Records conflict | Record and resolve explicitly | B-12 | EVD-018 | Conflict fixture | None | Stage 5 |
| REQ-833 | Action imposed | Offer one appeal; keep in force; reason | B-12 | MOD-042, MOD-043, MOD-045 | Appeal-record review | None | Stage 5 |
| REQ-834 | Appeal repeats | Require new evidence or defect; record closure | B-12 | MOD-046 | Repeat fixture | None | Stage 5 |
| REQ-835 | Appeal explained | Sufficient to contest; withhold by rule | B-12 | MOD-018, MOD-045 | Notice review | None | Stage 5 |
| REQ-836 | Appeal upheld | Reverse, append correction, restitute | B-12/owner | MOD-047, MOD-048 | Restitution path | None | Stage 5 |
| REQ-837 | Appeal assigned | State independence; label unsegregated | B-12 | UD-054, MOD-049 | Record field check | Owner (`UD-054`) | Blocked |
| REQ-838 | Role defined | Enforce prohibition list | B-12 | D-173, ADM-001 | Permission matrix | None | Stage 5 |
| REQ-839 | Permission granted | Named grant only; no superuser | B-12/Stage 6 | ADM-002, ADM-006 | Role-graph review | Stage 5/6 | Stage 5 |
| REQ-840 | Privileged login | Require step-up; separate session | Stage 6 | ADM-007, SEC-027 | Session review | Stage 6 | Stage 6 |
| REQ-841 | Restricted read by role | Append audit row with purpose | B-12/B-02 | ADM-008, EVD-026 | Read-path check | None | Stage 5 |
| REQ-842 | Self-targeting action | Block or require approval; disclose | B-12 | UD-054, ADM-009 | Conflict fixture | Owner (`UD-054`) | Blocked |
| REQ-843 | Case decision | Separate investigate and decide | B-12 | UD-054, ADM-010 | Role assignment | Owner (`UD-054`) | Blocked |
| REQ-844 | Config published | Separate author and publisher or disclose | B-12 | UD-054, ADM-011 | Change trace | Owner (`UD-054`) | Blocked |
| REQ-845 | Financial correction | Ledger path with reason code | B-04/B-12 | ADM-012, COR-002 | Ledger review | None | Stage 5 |
| REQ-846 | Separation impossible | Declare gap and compensating control | B-12 | UD-054, ADM-013 | Control register | Owner (`UD-054`) | Blocked |
| REQ-847 | Emergency invoked | State scope, expiry, review | B-12 | MOD-025, F-FP-016 | Measure register | Owner (`UD-056`) | Stage 5 |
| REQ-848 | Emergency used | Suspend/freeze/withhold only | B-12 | MOD-025, ADM-014 | Capability matrix | None | Stage 5 |
| REQ-849 | Emergency action taken | Retrospective review recorded | B-12 | UD-054, MOD-028 | Review record | Owner (`UD-054`) | Blocked |
| REQ-850 | Temporary measure active | Notify scope and review date | B-12/13 | MOD-027 | Message catalogue | Prompt 13 | Stage 13 |
| REQ-851 | Audit event occurs | Emit the named event shape | B-02/B-12 | EVD-026, EVD-027 | Event-set check | None | Stage 5 |
| REQ-852 | Audit row written | Identifiers and reasons only | B-02/B-12 | EVD-028 | Field review | None | Stage 5 |
| REQ-853 | Volume pressure | Never sample spine rows; retain priority classes | B-02 | EVD-034 | Tiering review | None | Stage 5 |
| REQ-854 | Audit read | Purpose-bound, registered, logged | B-12 | EVD-033 | Readership matrix | None | Stage 5 |
| REQ-855 | Audit correction/deletion | Append event; record authority | B-02/B-12 | UD-055, EVD-029 | Event review | Legal (`UD-055`) | Blocked |
| REQ-856 | Incident declared | Apply class posture and authority | B-12 | SEC-024, FR-001 | Class matrix | None | Stage 5 |
| REQ-857 | Breach suspected | Document assessment either way | B-12 | UD-017, SEC-025 | Artefact check | Legal (`UD-017`) | Blocked |
| REQ-858 | Integrity doubtful | Halt and disclose delay | B-02 | SEC-026, D-025 | Halt-path review | None | Stage 5 |
| REQ-859 | B-12 rule proposed | Verify no mechanic or outcome ownership | B-12 | FP-004, INT-001 | Boundary audit | None | Stage 5 |
| REQ-860 | Subsystem obligation exists | Link by reference | B-12 | INT-003, INT-009 | Reference check | None | Stage 5 |
| REQ-861 | B-12 rule proposed | Verify no new entitlement or reward | B-12 | FP-004, INT-008 | Prohibition fixture | None | Stage 5 |
| REQ-862 | Failure policy proposed | Declare per category | B-12 | FR-001, D-175 | Posture matrix | None | Stage 5 |
| REQ-863 | Detection unavailable | Keep play and value; record gap | B-12 | FR-003, FR-004 | Degradation review | None | Stage 5 |
| REQ-864 | Evidence unavailable | Hold; no permanent measure | B-12 | SEC-023, FR-005 | Failure fixture | None | Stage 5 |
| REQ-865 | Association error found | Separate, lift, record, notify | B-12 | EVD-018, COR-013 | Correction path | None | Stage 5 |
| REQ-866 | Claim written | State non-claims explicitly | B-12 | FP-008, GOV-024 | Claim scan | None | Stage 5 |
| REQ-867 | Review period arrives | Review capacity and FP rate; record | B-12 | MOD-035, UD-054 | Review record | Owner (`UD-054`) | Blocked |
| REQ-868 | Transparency proposed | Define structure; owner decides publication | B-12 | PRV-018, UD-058 | Structure review | Owner (`UD-058`) | Blocked |
| REQ-869 | Legal dependency exists | Name owner; take conservative branch | B-12 | GOV-009, UD-017 | Dependency register | Legal (`UD-017`) | Blocked until legal |

---

## 4. Totals, duplicate and traceability audit

| Metric | Value |
|---|---|
| Allocated requirements | **106** (`REQ-764`…`REQ-869`) |
| Provisional | **86** |
| Open (owner or legal) | **20** |
| Approved | **0** |
| Deferred | **0** |
| Duplicate identifiers | **0** |
| Missing statements | **0** |
| Missing verification cells | **0** |
| Requirements with a rule reference | **106** |
| Requirements whose own row cites a formula identifier | **4** (`REQ-771`, `REQ-823`, `REQ-829`, `REQ-847`) |
| Requirements named in a formula's affected-requirement field | **27** |
| Requirements with an owner/legal dependency | **20** |
| Downstream-only dependencies | **5** (`REQ-773`, `REQ-789`, `REQ-807`, `REQ-810`, `REQ-829`) |
| Untraced requirements | **0** |

**Open rows.** `REQ-782`, `795`, `808`, `809`, `812`, `816`, `817`, `830`, `831`, `837`, `842`, `843`, `844`, `846`, `849`, `855`, `857`, `867`, `868`, `869`. Each maps to `UD-017`, `UD-052`, `UD-053`, `UD-054`, `UD-055`, `UD-056` or `UD-058`; none is closed here.

**Formula linkage.** Only four requirement rows name a formula in their authority cell, because a requirement states an obligation while the [formula register](20_fair_play_and_player_protection_formula_register.md) states the calculation that satisfies it. The formula register's `Affected requirements` field names 27 requirements across the 16 formulas; both directions are checked by the `12B-` validator.

**Traceability rule.** A link is planned coverage, never proof of implementation or runtime behaviour. The acceptance companion maps each requirement family to a gate and a verification method; Prompt 12C will map the workflows and executed acceptance tests.