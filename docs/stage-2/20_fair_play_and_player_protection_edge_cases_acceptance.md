# B-12 — Fair-play edge cases, acceptance specifications and traceability

**Version:** 1.0 · **Created:** 2026-11-10 · **Stage 2, Prompt 12C**
**Status:** **Edge-case and acceptance specification — design only.** `Definition: COMPLETE` and `Execution: NOT RUN` are the only honest values in this document except where a row is explicitly **BLOCKED** by a named outstanding obligation. **No specification below was executed, and none is evidence of an implementation, a control, a measurement or a runtime behaviour.**
**Authority.** This document owns the B-12 fair-play edge cases (`FPE-###`), the 12C acceptance-test specifications (`FPA-###`), the 12C gate register (`P12C-##`), the 12C gap register (`FPG-##`, whose rows are stated in the [integration document](20_fair_play_and_player_protection_integration.md) §7 and consumed here) and the 12C traceability ledger. It owns **no rule** (`FP-`…), **no formula or parameter**, **no requirement row**, **no `INT-` contract identifier**, **no gameplay rule** and **no owner decision**.
**Companions.** [B-12 rulebook](20_fair_play_and_player_protection.md) · [B-12 requirements](20_fair_play_and_player_protection_requirements.md) · [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) · [B-12 acceptance](20_fair_play_and_player_protection_acceptance.md) · [12C journeys and workflows](20_fair_play_and_player_protection_workflows.md) · [12C cross-system integration](20_fair_play_and_player_protection_integration.md) · [12A research](research/12A_fair_play_privacy_moderation_administration_research.md) · [12A registers](research/12A_requirements_integration_and_risk_registers.md) · [11C companion](19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md) · [requirements ledger](03_requirements_traceability.md) · [decisions](../DECISIONS.md) · [unresolved decisions](05_unresolved_design_decisions.md) · [`12C_validate_fair_play_workflows.py`](../qa_backups/12C_validate_fair_play_workflows.py).

---

## 1. Status vocabulary, stated once and never relaxed

| Status | Meaning in 12C |
|---|---|
| `SPECIFIED` | A documentation artefact exists, resolves and is internally consistent. **This is the only status any 12C row may hold by default.** |
| `IMPLEMENTED` | Code, schema, grant, trigger, job, tool or surface exists and performs it. **No 12C row holds this status.** |
| `EXECUTED` | A method was actually run against an available implementation, with an inspected result. **No 12C row holds this status.** |
| `PASS` | A documentary criterion is satisfied by an artefact that exists and resolves. Used only for 12C **gates**, never for a test. |
| `FAIL` | The criterion is contradicted by the artefacts. |
| `BLOCKED` | The criterion cannot be assessed without a named external action — an implementation, a Stage 5 privilege correction, an executed verification run, an owner ruling or a legal answer. |
| `NOT APPLICABLE` | The criterion does not apply to a documentation-stage deliverable. |

A specification is never described as a passing test. Where a row is `BLOCKED`, the blocking obligation is named in the same row. Documentation validation is not runtime verification (`P12B` grading rules; `WTA` precedent in 11C §24).

**Test classifications.** `POS` positive · `NEG` negative · `BND` boundary · `SEC` security · `INT` integration · `REC` recovery · `PRV` privacy · `OWN` owner-decision-dependent. Each `FPA-` row carries exactly one primary class.

---

## 2. Edge-case register

**2.1 Schema.** Each `FPE-###` row supplies: identifier · scenario category · scenario · triggering condition · affected systems · owning workflow · expected system behaviour · expected player experience · security and privacy implication · recovery or escalation · audit requirement · test rows · and whether the case needs an owner or legal resolution.

**2.2 Deduplication against Prompt 11C.** The 84 existing `WEE-001`…`WEE-084` rows stay exactly as they are and are **not** restated, renumbered or duplicated. Every B-12 case below is either (a) a situation `WEE-` has no row for — reporting, moderation queues, conduct ladders, sanctions, appeals, collusion determination, account compromise, evidence handling, retention and erasure — or (b) a `WEE-` or `WTS-` situation whose **B-12 side** needs a fair-play behaviour that 11C explicitly deferred (`WEE-027` material recovery "only through Prompt 12", `WEE-023`, `WEE-011`, `WEE-051`, `WEE-039`, `WEG-02`, `WEG-04`, `WEG-05`, `WEG-06`). In case (b) the row cites the existing identifier and specifies only the B-12 half. Where 11C already fully owns the behaviour, 12C adds nothing.

**2.3 Threat reuse.** No new threat namespace is created. Cases cite the 32 `12A-RK-001`…`12A-RK-032` threats and, where the exposure is B-11's, the 30 `WTS-###` threats, unchanged. Nothing here is reported as a confirmed project incident: `12A-RK-007`, `12A-RK-012`, `12A-RK-024`, `12A-RK-026` and `12A-RK-031` are the only confirmed items in the corpus and they keep that classification exactly.

**2.4 Counts.** 100 rows, `FPE-001`…`FPE-100`, contiguous; `FPE-101` onward is unallocated. Category coverage, counted from the register: **C1 player behaviour 6** · **C2 economic and gameplay manipulation 24** · **C3 account and identity 7** · **C4 moderation and enforcement 25** · **C5 technical and operational failure 19** · **C6 privacy and information handling 19** = 100. Every scenario named in Prompt 12C §8 is mapped in §2.6.

### 2.6 Required-scenario coverage map

| Prompt 12C §8 scenario | Row(s) | | Prompt 12C §8 scenario | Row(s) |
|---|---|---|---|---|
| False reports | `FPE-004`, `FPE-045` | | Partial workflow execution | `FPE-036` |
| Malicious reports | `FPE-004`, `FPE-005` | | Duplicate event delivery | `FPE-056` |
| Repeated reports | `FPE-003`, `FPE-052` | | Retry behaviour | `FPE-027`, `FPE-036` |
| Coordinated reporting | `FPE-004` | | Timeout and service unavailability | `FPE-002`, `FPE-009`, `FPE-048` |
| Harassment | `FPE-089`, `FPE-066` | | Inconsistent database state | `FPE-018`, `FPE-046` |
| Impersonation | `FPE-031`, `FPE-033` | | Failure during a shared turn | `FPE-055`, `FPE-098` |
| Abusive communications | `FPE-089`, `FPE-024` | | Concurrent actions | `FPE-057`, `FPE-044` |
| Retaliation | `FPE-005` | | Stale data | `FPE-058`, `FPE-093` |
| Coordinated market manipulation | `FPE-082`–`FPE-085` | | Audit-write failure | `FPE-076` |
| Artificial resource generation | `FPE-034`, `FPE-094` | | Recovery after interruption | `FPE-055`, `FPE-032` |
| Exploit chains | `FPE-047` | | Unauthorised disclosure | `FPE-066`, `FPE-090` |
| Abusive trade patterns | `FPE-085`, `FPE-041` | | Excessive data collection | `FPE-015` |
| Unfair reward claims | `FPE-019`, `FPE-092` | | Unauthorised administrative access | `FPE-073`–`FPE-075`, `FPE-081` |
| Ranking manipulation | `FPE-095`–`FPE-097` | | Retention conflicts | `FPE-068`, `FPE-069` |
| Objective exploitation | `FPE-093`, `FPE-094` | | Deletion requests | `FPE-071` |
| Account compromise | `FPE-033` | | Legal holds | `FPE-068`, `FPE-044` |
| Shared-account indicators | `FPE-012`, `FPE-031` | | Evidence access restrictions | `FPE-016`, `FPE-067`, `FPE-070` |
| Account recovery | `FPE-033` | | Good-faith versus knowing report | `FPE-004`, `FPE-020` |
| Identity ambiguity | `FPE-032`, `FPE-030` | | | |
| Unauthorised access | `FPE-061`, `FPE-062` | | | |
| Conflicting account states | `FPE-029`, `FPE-057` | | | |
| Incorrect sanctions | `FPE-042`, `FPE-080` | | | |
| Inconsistent enforcement | `FPE-044`, `FPE-057` | | | |
| Delayed review | `FPE-054`, `FPE-099` | | | |
| Evidence insufficiency | `FPE-011`, `FPE-020` | | | |
| Appeals | `FPE-048`–`FPE-052` | | | |
| Repeated violations | `FPE-021` | | | |
| Administrative abuse | `FPE-073`, `FPE-080` | | | |
| Conflicting moderation outcomes | `FPE-045`, `FPE-047` | | | |

### 2.5 Register

A case's category follows the **failing mechanism**, not the actor: a player-behaviour scenario whose interest is how enforcement responds is recorded under C4, and one whose interest is the value or outcome effect is recorded under C2. §2.6 proves that every scenario named in Prompt 12C §8 is covered regardless of which category holds it.

| ID | Cat | Scenario | Trigger | Systems | FPW | Expected behaviour | Player experience | Security and privacy | Recovery or escalation | Audit | Tests | Dependency |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `FPE-001` | C1 | Report submitted with a missing subject or category | Structured intake validation fails | B-12 | `FPW-001` | Rejected with the failed condition only; no report row created | Retryable, non-revealing error | No existence or rule disclosure (`PRV-020`) | Resubmit | Nothing written (`FR-06`) | `FPA-001`, `FPA-002` | none |
| `FPE-002` | C1 | Report submitted while intake is unavailable | Intake service down | B-12 | `FPW-001` | Retryable failure; nothing silently lost; **no action on an unreceived report** | Told to retry | No enforcement implied by absence | Retry after boundary | Failure recorded | `FPA-003`, `FPA-004` | none |
| `FPE-003` | C1 | Ten duplicate reports of one conduct in one window | `F-FP-008` key collision | B-12 | `FPW-002` | Coalesce to one case; cluster count grows | None | Reporter never identified to subject | Normal triage | Evidence write | `FPA-007`, `FPA-008` | `FP-P13` provisional |
| `FPE-004` | C1 | Coordinated report brigading against one nation | Volume spike, same window | B-12, B-03 | `FPW-002` | Volume is a triage signal; **tier never raised by volume**; reporter trust may be affected instead | None | No inference about the target | Review | Triage record | `FPA-009`, `FPA-010` | cites `12A-RK-029` |
| `FPE-005` | C1 | Report names an administrator as the subject | Subject role check | B-12, Stage 6 | `FPW-003` | Confidential routing; ordinary chain excluded | Acknowledgement only | Peer reviewers excluded | Owner escalation where no independent reviewer exists | Privileged access | `FPA-011`–`FPA-014` | `UD-054` |
| `FPE-006` | C4 | Assigned reviewer is in the subject's Alliance | COI screen at assignment | B-12, B-09 | `FPW-004` | Reviewer excluded and exclusion recorded; if impossible, labelled `unsegregated` and disclosed | Disclosure of the label, not the reviewer id | No identity leak | Reassign or label | Decision record | `FPA-015`–`FPA-018` | `UD-054` |
| `FPE-007` | C4 | Triage would act before safety and evidence are assessed | Queue shortcut attempt | B-12 | `FPW-005` | Blocked: triage order enforced (`MOD-008`) | None | No premature sanction | Complete triage | Attempt recorded | `FPA-019`, `FPA-020` | none |
| `FPE-008` | C4 | Reversible hold requested on an `E0` suspicion only | Ceiling check | B-12 | `FPW-005`, `FPW-007` | `E0` permits a review object only; no hold | None | Prevention only, never punishment | Raise to `E1` with a stated rule | State assignment | `FPA-021`–`FPA-024` | none |
| `FPE-009` | C5 | Detection service unavailable during a turn | Detector outage | B-12, B-02 | `FPW-006` | Detection degrades; play continues; gap recorded and backfilled where records survive | Unaffected | No silent removal of protection | Backfill | Gap record | `FPA-027`, `FPA-028` | cites `12A-RK-012` |
| `FPE-010` | C2 | Automated rule attempts to write a conduct finding | Output-class violation | B-12 | `FPW-006` | Refused: automation cannot create `E3`, a suspension, a permanent measure or a public statement | None | No automated culpability | Route to human review | Rejection recorded | `FPA-029`–`FPA-032` | none |
| `FPE-011` | C1 | One behavioural anomaly and nothing else | Independence test | B-12 | `FPW-007`, `FPW-008` | Review object only; needs one independent non-behavioural source | None | Anomaly is not a violation | Await corroboration | State assignment | `FPA-033`, `FPA-034` | none |
| `FPE-012` | C3 | Shared CGNAT or household network observed | Network signal | B-03, B-12 | `FPW-007`, `FPW-019` | Triage ordering only; never a control inference; ceiling at lowest preventive tier | None | Named false-positive class (`EVD-014`) | Independent evidence required | Triage record | `FPA-035`, `FPA-036` | cites `12A-RK-028` |
| `FPE-013` | C2 | Two reports repeating one allegation counted as independent | Independence misuse | B-12 | `FPW-008` | Not independent (`EVD-011`); sufficiency predicate false | None | No score, no shortcut | Correct source accounting | Determination recorded | `FPA-039`, `FPA-040` | none |
| `FPE-014` | C5 | Detection rule enabled without declared false positives | Configuration publication | B-12 | `FPW-009` | Not enabled; attempt recorded | None | Unauditable rule is refused | Declare then enable | Configuration publication | `FPA-045`, `FPA-046` | none |
| `FPE-015` | C6 | Detector would require data the project refuses to collect | Capability gap | B-12 | `FPW-009` | Recorded **not available**; no proxy, no softened claim | None | No new surveillance (`EVD-016`) | Owner may change collection policy | Decision record | `FPA-047`, `FPA-048` | none |
| `FPE-016` | C6 | Evidence artefact opened by a reviewer with no stated purpose | Restricted read | B-12, B-02 | `FPW-036` | Read denied until a purpose and authorising requirement are stated | None | Purpose before permission | State purpose, then read | Privileged access event | `FPA-049`–`FPA-052` | `WEG-04` |
| `FPE-017` | C5 | Routine compaction reaches a preserved record | Retention boundary | B-02, B-12 | `FPW-010`, `FPW-041` | Protected from compaction for case need; preservation is not indefinite retention | None | `UD-055` dependency stated | Release preservation at closure | Retention event | `FPA-053`, `FPA-054` | `UD-055` |
| `FPE-018` | C2 | Two server records contradict each other | Conflict detection | B-12, B-04 | `FPW-010`, `FPW-011` | Conflict recorded and resolved explicitly with a reason; never silently adopted | None | Record integrity | Named governing record | Resolution recorded | `FPA-055` (also `FPA-049`) | none |
| `FPE-019` | C2 | A "grant without evidence" completion claim | B-11 flag to B-12 | B-11, B-12 | `FPW-050` | Invalidated as `EXCLUDED`/`SUSPENDED` **by B-11 enacting a B-12 request**, never as a B-11 punishment | Reward held with a reason and a route | No B-12 reward grant | Appeal then restitution path | Status event | `FPA-351`–`FPA-356` | cites `WEE-081` |
| `FPE-020` | C4 | Screenshot supplied as the only evidence | Corroboration | B-12 | `FPW-011` | Pointer corroborated against server records; if impossible, `EX` | Bounded outcome | Artefact alone insufficient (`EVD-023`) | Close `EX` | Evidence assessment | `FPA-057`, `FPA-058` | none |
| `FPE-021` | C4 | Unconfirmed prior used to aggravate severity | Repetition input | B-12 | `FPW-012` | Refused: only confirmed `E3` priors count, applied exactly once via `F-FP-011` | None | Proportionality | Correct the input | Severity inputs recorded | `FPA-063`, `FPA-064` | none |
| `FPE-022` | C4 | Moderator attempts `T3` without senior or second review | Authority check | B-12 | `FPW-013` | Denied or escalated; where staffing permits no review, labelled and stopped | None | No implicit privilege | Escalate to `R-SMOD` | Override attempt recorded | `FPA-069`–`FPA-072` | `UD-053`, `UD-054` |
| `FPE-023` | C4 | Sanction would edit a market, election, snapshot or balance | Prohibition-list check | B-12, all owners | `FPW-013` | Blocked: B-12 acts on the account only; the owning rule stays authoritative | None | No universal controller | Route via `FPW-021` correction | Decision recorded | `FPA-073`–`FPA-076` | none |
| `FPE-024` | C6 | Notice text would reveal a threshold or the reporter | Notice assembly | B-12 | `FPW-014` | Content withheld **by rule**, not by reviewer choice | Understandable but bounded | Method secrecy (`MOD-018`) | Rebuild notice | Notice event | `FPA-077`–`FPA-080` | none |
| `FPE-025` | C4 | Case closed without stating what was examined | Closure validation | B-12 | `FPW-015` | Closure invalid until reason and evidence state are recorded | Incomplete notice blocked | Reconstructibility | Complete then close | Closure event | `FPA-085`, `FPA-086` | none |
| `FPE-026` | C3 | Enforcement expressed as a nation field or pair state | Record shape | B-12, B-03 | `FPW-016` | Rejected: a sanction is account-level (`INT-002`, `MA-002`) | None | No fourth state object | Correct the target | Rejection recorded | `FPA-091`, `FPA-092` | none |
| `FPE-027` | C5 | Duplicate enforcement request after a retry | Idempotency | B-12, B-03 | `FPW-016` | Coalesces to the first committed result; one record | One notice | No double application | None needed | Single event | `FPA-093`–`FPA-096` | none |
| `FPE-028` | C4 | Restriction expires between two turn boundaries | Boundary arithmetic | B-12, B-02 | `FPW-017` | Ends at the next boundary; ceiling rounding only; never wall-clock | Ends at a predictable point | No order payoff | Automatic | Expiry event | `FPA-099`–`FPA-102` | `FP-P04`, `FP-P05` |
| `FPE-029` | C3 | Reroll attempted while a case is pending | Survival check | B-03, B-12 | `FPW-018` | Reroll proceeds or is blocked by a preservation order; the case **continues** and is not closed by retirement | Told the restriction survives | A reroll is not an amnesty | Case continues | Survival event | `FPA-105`, `FPA-106` | cites `RRL-017`, `ECN-204` |
| `FPE-030` | C3 | Assets divested to a linked account immediately before a reroll | Pattern detection | B-04, B-12 | `FPW-018`, `FPW-023` | Reviewable pattern, **not automatically reversed merely because a reroll followed** | None | No identity claim | Reach decision then correction | Review record | `FPA-107`–`FPA-110` | `UD-052` |
| `FPE-031` | C3 | Shared-context declaration submitted for accounts the author does not control | Declaration validation | B-12 | `FPW-019` | Stored as an attestation by its author only; grants nothing; absence never aggravating | Confirmed to the author | Author and integrity role only | Delete to withdraw | Access event on read | `FPA-111`–`FPA-114` | none |
| `FPE-032` | C3 | Accounts wrongly associated and both restricted | Misassociation discovery | B-03, B-12 | `FPW-020` | Separate, lift, record and notify; reverse first, investigate second | Restrictions lifted | Least-harmful reading while unresolved | Correction path | Correction event | `FPA-117`, `FPA-118` | none |
| `FPE-033` | C3 | Account compromise reported, then play continued under it | Recovery state | B-03, Stage 6, B-12 | `FPW-020`, `FPW-033` | Recovery is B-03 and Stage 6's; B-12 treats conduct during compromise on the evidence, never on the compromise alone | Recovery route preserved, appeal intact | No credential held by B-12 | Recovery then assessment | Both lanes recorded | `FPA-119`–`FPA-122` | cites `12A-RK-001` |
| `FPE-034` | C2 | Ledger pair fails its conservation identity (`MKT-S10`) | Signal receipt | B-04, B-07, B-02 | `FPW-047`, `FPW-033` | Treated as a **defect, not a player act**; operator paged; no conduct case | None | No accusation without a person-level finding | Reconciliation | Integrity result | `FPA-325`–`FPA-328` | cites `12A-RK-007` |
| `FPE-035` | C2 | Value correction needed inside a political or Alliance object | Owner-path correction | B-06, B-09, B-12 | `FPW-021` | Appended adjustment naming the original; `government_id` never set; no self-adjudication | Named in the notice | Political state is never a sanction | Owner path executes | Correction event | `FPA-123`–`FPA-128` | `UD-046` |
| `FPE-036` | C5 | Correction transaction fails partway | Rollback | B-04, B-12 | `FPW-021`, `FPW-026` | Rolls back exactly; retried with the same key; partial correction prohibited | None | No partial value exists | Retry | Failure event | `FPA-129`–`FPA-132` | none |
| `FPE-037` | C2 | `V_obs` lower than `V_law` — a loss, not an excess | Amount sign test | B-04, B-12 | `FPW-022` | `C = 0`; the shortfall is compensation territory, never a removal | None | No negative balance created | `FPW-025` | Calculation recorded | `FPA-137`, `FPA-138` | none |
| `FPE-038` | C2 | Lawful counterfactual cannot be computed | Null behaviour | B-12, owner system | `FPW-022` | `NO_CALCULATION` plus incident; never zero | None | No fabricated value | Reconstruct or escalate | Incident | `FPA-139`, `FPA-140` | none |
| `FPE-039` | C2 | Benefit moved on through three further accounts | Flow tracing | B-04, B-07, B-12 | `FPW-023` | Removal follows proved links only; unproven legs excluded | Only their own change disclosed | No collective punishment | Recovery order plus shortfall record | Per-leg events | `FPA-145`–`FPA-148` | `UD-052` |
| `FPE-040` | C2 | Benefiting account has less than the removal amount | Insolvency | B-04 | `FPW-023` | Floors at zero and records the shortfall; **no debt mechanic invented** | Balance not negative | No new currency | Shortfall stays on record | Removal event | `FPA-149`, `FPA-150` | none |
| `FPE-041` | C2 | Restricted transfer routed through an Alliance container | `V-11` evidence | B-09, B-04, B-12 | `FPW-049`, `FPW-023` | Same Economy and Diplomacy checks apply; container is never an evasion channel | None | No Alliance adjudication | Platform enforcement only | `AUD-AL` plus correction | `FPA-341`–`FPA-346` | `UD-046` |
| `FPE-042` | C4 | Reversal references a transaction that no longer resolves | Original reference | B-04 | `FPW-024` | `NO_ORIGINAL`; nothing appended | None | No orphan reversal | Fix the reference | Rejection recorded | `FPA-153`, `FPA-154` | none |
| `FPE-043` | C4 | Compensation requested with no owner cap set | Parameter status | B-12, owner | `FPW-025` | `PROVISIONAL_BLOCK`; the loss is recorded as an exposure, not paid as if approved | Told a decision is outstanding | No invented number | Owner decision | Decision request | `FPA-161`–`FPA-164` | `UD-053` |
| `FPE-044` | C5 | Two corrections claim one balance at one boundary | Ordering | B-04, B-12 | `FPW-026` | Deterministic order by `(case_closed_turn, n, type_rank)`; ties by original id | None | No race in correction | Both apply at next boundary | Ordered events | `FPA-167`–`FPA-170` | none |
| `FPE-045` | C5 | A correction is submitted twice with different keys | Duplicate handling | B-12, B-04 | `FPW-026` | Key derived from case, original and type coalesces the second | One change | No double removal | None | Second coalesced | `FPA-171`, `FPA-172` | none |
| `FPE-046` | C5 | Reconciliation residual is non-zero after a batch | Conservation | B-04 | `FPW-026` | Correction fails and raises an incident; affected value path stops, world continues | Unaffected | `Z = O + L + C + R + P + X + A` enforced | Incident then correction | Incident plus result | `FPA-173`–`FPA-176` | cites `12A-RK-007`, `12A-RK-031` |
| `FPE-047` | C5 | Compound cross-system exploit spans economy, market, alliance, event and ranking | Multi-owner reversal | all owners, B-12 | `FPW-026`, `FPW-021` | Reversal order is **structural**: each owner appends in the recorded case order at its next valid boundary; nothing is reordered in a closed turn | One notice per affected action | No single system rewrites another | Per-owner paths | Per-owner events | `FPA-167`–`FPA-176` | answers `12A-OPEN-013` structurally; reach stays `UD-052` |
| `FPE-048` | C4 | Appeal filed after the window because the service was down | Outage arithmetic | B-12 | `FPW-027` | Window extended by the recorded outage in turns; **no appeal deemed abandoned** | Filing accepted | No silent forfeiture | File normally | Filing event | `FPA-177`–`FPA-180` | `UD-059` |
| `FPE-049` | C4 | Appeal granted a reversible hold | Hold semantics | B-12, B-03 | `FPW-028` | Hold recorded; the appeal is not decided by it | Relief limited | No covert remission | Decision later | Hold event | `FPA-185`, `FPA-186` | none |
| `FPE-050` | C4 | Appeal decided by the original reviewer | Independence | B-12 | `FPW-029` | Labelled **not independent** and disclosed; the design states what it does not guarantee | Told the fact | No separation claimed | Reassign if staffing permits | Label recorded | `FPA-189`–`FPA-192` | `UD-054` |
| `FPE-051` | C4 | Appeal remanded for a procedural defect | Remand | B-12 | `FPW-029` | Remand names the defect and the reviewer; the original is not edited | Told what was wrong | No silent re-decision | Reworked decision | Remand event | `FPA-193`, `FPA-194` | none |
| `FPE-052` | C4 | Third appeal on identical grounds | Reopening bar | B-12 | `FPW-030` | Closed without re-investigation, recorded | Reasoned closure | Appeals cannot become stalling | New evidence reopens | Closure event | `FPA-199`–`FPA-202` | `UD-059` |
| `FPE-053` | C4 | Emergency measure requested with no recording path | Record-first rule | B-12, B-02 | `FPW-031` | **Does not execute**; a silent emergency action is prohibited | None | No covert action | Restore recording first | None (refused) | `FPA-203`, `FPA-204` | none |
| `FPE-054` | C4 | Emergency measure reaches its expiry with no extension record | Self-expiry | B-12, B-02 | `FPW-032` | Expires automatically; extension is a new decision with review | Capability returns | No indefinite emergency | Ordinary path if needed | Expiry event | `FPA-211`–`FPA-214` | `UD-056` |
| `FPE-055` | C5 | Failure during a shared turn produces partial settlement | Turn integrity | B-02, B-04, B-12 | `FPW-033`, `FPW-051` | Integrity failure is an **incident**, not a conduct case, unless manipulation is evidenced; recovery never re-executes a committed action | Disclosed as a delay | Forward-only or last-committed recovery | Reconcile then review | Incident event | `FPA-217`–`FPA-222` | cites `12A-RK-008` |
| `FPE-056` | C5 | Duplicate event delivery opens the same case twice | Delivery semantics | B-12 | `FPW-006`, `FPW-002` | Coalesces to one case by key; no double queue entry | None | No double jeopardy from a retry | None | One event | `FPA-223`, `FPA-224` | none |
| `FPE-057` | C5 | Concurrent administrators act on one account | Concurrency | B-12, B-03 | `FPW-013`, `FPW-016` | One commits; the other is surfaced as a conflict, never silently applied or dropped | One notice | No last-write-wins | Reviewer resolves | Both recorded | `FPA-225`, `FPA-226` | answers `WEG-02` |
| `FPE-058` | C5 | Stale data used for a decision after a boundary | Staleness | B-02, B-12 | `FPW-013` | Re-validated at effect; a stale fingerprint re-runs the check | None | No order payoff | Recompute | Rejection recorded | `FPA-361`–`FPA-364` | cites `WEE-047` |
| `FPE-059` | C6 | Suspected personal-data breach with no reporting obligation met | Assessment duty | B-12, owner, counsel | `FPW-034` | Assessed and documented **with the reasons for not reporting**; artefact, not a legal conclusion | Bounded notice only where authority exists | No compliance claim | Legal decision remains | Assessment event | `FPA-227`–`FPA-232` | `UD-017` |
| `FPE-060` | C6 | Two registers classify the same field differently | Reconciliation | B-12, owning register | `FPW-035` | Reconciled in the owning register with a dated decision; no silent reassignment | None | More protective class governs meanwhile | Dated reconciliation | Configuration event | `FPA-233`, `FPA-234` | none |
| `FPE-061` | C6 | Privileged read performed for convenience | Purpose check | B-12 | `FPW-036` | Denied until a purpose and authorising requirement exist | None | Convenience is not a purpose | State purpose | Attempt recorded | `FPA-239`–`FPA-242` | `WEG-04` |
| `FPE-062` | C6 | Restricted read fails and falls back to a broader cache | Posture | B-12 | `FPW-036` | Returns **no data**; no unfiltered fallback | None | Fail-closed read | Retry with purpose | Failure recorded | `FPA-243`, `FPA-244` | none |
| `FPE-063` | C6 | Response legitimately contains a field the requester cannot see | Server leak | B-12, owner service | `FPW-037` | Treated as a **design defect**, not a player violation; the leak is fixed and its effects corrected | None | Hiding in the client is not control | Defect then correction | Defect incident | `FPA-247`–`FPA-250` | cites `12A-RK-021` |
| `FPE-064` | C6 | Aggregate denominator drops below five after a withdrawal | Suppression | B-11, B-12 | `FPW-038` | Withheld or coarsened; no exception invented | Unaffected | No differencing leak | Recompute denominator | Publication decision | `FPA-253`, `FPA-254` | cites `WEE-039` |
| `FPE-065` | C6 | Differencing two published aggregates singles out a nation | Inference | B-11, B-12 | `FPW-038` | Complementary suppression and stable merging applied; figure withheld | None | Re-identification risk | Coarsen | Inference argument recorded | `FPA-255`–`FPA-258` | cites `12A-RK-022` |
| `FPE-066` | C6 | Notice would reveal that another account is under restriction | Disclosure bound | B-12, Prompt 13 | `FPW-039` | Withheld; no badge, ranking note or chronicle entry carries it | Only their own state | Status privacy preserved | Bounded text | Notice event | `FPA-261`–`FPA-264` | none |
| `FPE-067` | C6 | Moderator with view rights attempts an export | Permission separation | B-12 | `FPW-040` | Denied: viewing never implies export; a failed export leaves **no partial or unredacted file** | None | Least privilege | Grant separately if justified | Attempt and result recorded | `FPA-267`, `FPA-268` | none |
| `FPE-068` | C6 | Legal deletion obligation meets the permanent spine | Obligation clash | B-12, B-02, counsel | `FPW-041` | Both obligations recorded; conservative branch taken; the fact of removal survives as an event | Subject informed of removal authority | No period invented | Owner and counsel decision | Deletion-with-authority event | `FPA-273`–`FPA-278` | `UD-017`, `UD-055` |
| `FPE-069` | C6 | Retention quota pressure on spine rows | No sampling | B-02, B-12 | `FPW-041`, `FPW-044` | Spine rows never sampled away; value, pipeline, privileged and enforcement rows retained first | None | Integrity is not a quota variable | Tier the non-spine classes | Tiering decision | `FPA-279`, `FPA-280` | none |
| `FPE-070` | C6 | Case evidence copied into a support tool default view | Minimisation | B-12 | `FPW-040`, `FPW-010` | Prohibited: evidence is case-scoped and excluded from logs and default views | None | Minimisation | Remove copy path | Custody event | `FPA-281`, `FPA-282` | `UD-055` |
| `FPE-071` | C6 | Data-subject access or erasure request arrives | Dual lane | B-03, B-12, counsel | `FPW-040`, `FPW-041` | Served to the subject only; case-evidence limits recorded; nothing disclosed to a third party | Subject receives their own data | No third-party leak | Legal decision remains | Request and outcome events | `FPA-269`, `FPA-270` | `UD-017`, `UD-055` |
| `FPE-072` | C4 | Role granted without a named capability, or a superuser shortcut | Register check | B-12 | `FPW-042` | Denied: a capability not in the register does not exist | None | No superuser | Name then grant | Permission change | `FPA-283`–`FPA-286` | none |
| `FPE-073` | C4 | Operator acts against their own nation | Self-dealing | B-12, B-03 | `FPW-043` | Blocked where second approval exists; otherwise recorded, disclosed on request and retrospectively reviewed | May learn of it on request | Insider pattern named (`12A-RK-023`) | Second approval or review | Override and review events | `FPA-291`–`FPA-294` | `UD-054` |
| `FPE-074` | C4 | Ordinary play credential used for a privileged action | Step-up | Stage 6, B-12 | `FPW-043` | Denied; no fallback identity and no shared operator credential | None | Session separation | Step up then retry | Denial recorded | `FPA-295`, `FPA-296` | cites `12A-RK-025` |
| `FPE-075` | C4 | Privileged session suspected compromised | Containment | Stage 6, `R-SEC` | `FPW-043`, `FPW-033` | Halt privileged paths, preserve evidence, **keep the world running** | Unaffected play | No audit suppression | Rotate and revoke | Containment events | `FPA-297`, `FPA-298` | cites `12A-RK-026` |
| `FPE-076` | C5 | Consequential act has no audit row available | Fail closed | B-12, B-02 | `FPW-044` | Nothing commits: no effect without its record | None | Absence is a defect, not a gap in text | Restore spine then retry | None (refused) | `FPA-301`, `FPA-302` | `P12B-14` |
| `FPE-077` | C6 | Audit row would contain a message body or a secret | Content rule | B-12 | `FPW-044` | Field refused: identifiers, decisions and reasons only | None | Log omissions are protective | Reference, never body | Shape validation | `FPA-303`–`FPA-306` | none |
| `FPE-078` | C5 | Chain link missing or a digest mismatch | Tamper evidence | B-02, B-12 | `FPW-045` | `CHAIN_BREAK`, never a skipped link; publication halted pending review | Delay disclosed | **No claim that this is operating** | Incident then appended correction | Verification result | `FPA-309`–`FPA-312` | `P12B-14` **BLOCKED** |
| `FPE-079` | C5 | Verification interval missed | Cadence | B-02 | `FPW-045` | Incident raised at the next boundary; interval value stays provisional | None | Missing job is a defect | Run verification | Miss recorded | `FPA-313`, `FPA-314` | `UD-058`, `FP-P08` |
| `FPE-080` | C4 | Someone edits an audit row in place | Append-only | B-02, B-12 | `FPW-046`, `FPW-033` | Prohibited; corrected only by an appended event referencing the original; the act itself is `V-16` | None | Concealment is itself a violation | Appended correction | Both events | `FPA-319`–`FPA-322` | `P12B-14`, `P12B-16` |
| `FPE-081` | C6 | Audit read performed without a registered purpose | Readership | B-12, B-02 | `FPW-046` | Denied; readership is granted by purpose from a published register | None | Readable by none is not accountability either | Register a purpose | Read log | `FPA-323`, `FPA-324` | none |
| `FPE-082` | C2 | Matched opposite-side orders creating artificial depth | `MKT-S07`, `MKT-S04` | B-07, B-12 | `FPW-047` | Indicator opens review; finding requires a non-behavioural record; price alone proves nothing (`MKT-155`) | None | No public accusation | Corroborate | Signal receipt event | `FPA-329`, `FPA-330` | none |
| `FPE-083` | C2 | Listing cancelled and reposted at the same price | `MKT-S05` | B-07, B-12 | `FPW-047` | Review object; the market's own `SUSPENDED` listing power stays B-07's | Neutral confirmation, no flag | No market-side trust score (`MKT-182`) | Market handles the listing; B-12 the conduct | Signal event | `FPA-331`, `FPA-332` | none |
| `FPE-084` | C2 | One nation exceeds half of a resource's 12-turn volume | `MKT-S08` | B-07, B-12 | `FPW-047` | Review input only; scale and share are never violations by themselves (`FP-018`, `CO-002`) | None | Legitimate dominance is legal | Corroboration | Signal event | `FPA-333`, `FPA-334` | none |
| `FPE-085` | C2 | Trade repeated at the same price and quantity between a fixed pair | `MKT-S04`, `V-09` | B-07, B-04, B-12 | `FPW-047`, `FPW-022` | If the effect could not occur between independent controllers, the **flow** is charged, not identity | Corrected value | No identity claim | Correction plus optional conduct case | Both events | `FPA-325`–`FPA-334` | cites `12A-RK-013` |
| `FPE-086` | C2 | Breach record disputed as incorrect | `DPE-049` | B-08, B-12 | `FPW-048`, `FPW-021` | New event referencing the original through B-08; **never an edit**; no dispute state is invented in B-08 | Their own published reason remains available | Append-only history | Correction path | Correction event | `FPA-335`–`FPA-340` | `DPE-049` stays PARTIAL |
| `FPE-087` | C2 | Officer attempts to suspend a member's account | Power boundary | B-09, B-03, B-12 | `FPW-049` | No such power; platform moderation only (`ALL-158`) | Told the platform path exists | No self-adjudication (`AX-23`) | Report through `FPW-001` | Refusal recorded | `FPA-341`, `FPA-342` | `UD-044` |
| `FPE-088` | C2 | Alliance-scale behavioural similarity presented as collusion | False-positive class | B-09, B-12 | `FPW-049`, `FPW-007` | Recorded as a documented false-positive class, not evidence (`REQ-788`) | None | Cooperation is not collusion | False-agency test | Catalogue entry | `FPA-343`, `FPA-344` | none |
| `FPE-089` | C2 | Leadership abuse: coercion of members for platform benefit | Conduct class | B-09, B-12 | `FPW-011`, `FPW-013` | Assessed on evidenced accounts; the Alliance is not sanctioned as a body | Members see no collective effect | No collective punishment (`CO-010`) | Account-level action | Decision event | `FPA-345`, `FPA-346` | `UD-044` |
| `FPE-090` | C6 | Tax or contribution detail leaking through moderation tooling | Readership | B-09, B-12 | `FPW-036`, `FPW-049` | Scoped by B-09 permissions, minimised, every read audited (`12A-INT-12`) | None | Confidential finance data | Fix the read path | Read events | `FPA-347`, `FPA-348` | none |
| `FPE-091` | C2 | Slot filling or deliberate feeding in a campaign | `WRK-06`, `V-10` | B-10, B-12 | `FPW-050` | B-10 records the block and reason as a **review signal**; B-12 owns the finding and the measure; no result is recomputed | Blocked action explained | No warfare prohibition invented | Evidence then decision | `WRA-02` cited | `FPA-351`–`FPA-356` | cites `WTS-017` |
| `FPE-092` | C2 | Manufactured participation recorded as an event completion | `WEP-655` | B-11, B-12 | `FPW-050` | B-11 flags and records; B-12 decides; the grant is held or invalidated with an evidence id | Held reward with a route | B-12 grants nothing | Hold then appeal | Status event | `FPA-357`–`FPA-360` | cites `WEE-081` |
| `FPE-093` | C2 | Objective completed through an obsolete or stale route | Staleness | B-11, B-02 | `FPW-050`, `FPW-013` | Uncredited where the state was stale; correction restores the lawful effect | No credit | No retroactive rule (`FP-035`) | Correction | Completion event | `FPA-359`, `FPA-360` | cites `WEE-024` |
| `FPE-094` | C2 | Replay of an activity record re-grants a reward | Replay resistance | B-11, B-04, B-12 | `FPW-050`, `FPW-024` | Rejected by state or entitlement, not merely by a missing key; a replay cannot re-grant | One grant | No duplicate value | Reverse any duplicate | Rejection event | `FPA-361`–`FPA-364` | cites `WEE-049`, `12A-RK-005` |
| `FPE-095` | C2 | Pre-snapshot spike inflates a standing | Timing abuse | B-11, B-12 | `FPW-051`, `FPW-047` | Snapshot-boundary manipulation is evidence for `V-04`/`V-10`; the seal is not moved | Rank as published | No mid-turn rank visible | Correct forward | Seal integrity record | `FPA-365`, `FPA-366` | cites `WTS-007`, `12A-RK-015` |
| `FPE-096` | C5 | Historical standing proven wrong | Correction | B-11, B-12 | `FPW-051` | A **new sealed snapshot** with `corrects_snapshot_id`; the original becomes `corrected_by`; deletion invalid | Changed rank, explained | History never silently rewritten | New snapshot | Publication event | `FPA-367`, `FPA-368` | cites `WEE-034` |
| `FPE-097` | C5 | Formula change would alter a sealed result | Immutability | B-11 | `FPW-051` | Sealed snapshots are never rewritten by a formula change; the correction is prospective | None | Reproducibility | Recompute forward | Change record | `FPA-369`, `FPA-370` | cites `WEP-593` |
| `FPE-098` | C5 | Integrity doubt during resolution of a shared turn | Halt decision | B-02, B-12 | `FPW-033`, `FPW-051` | Halt resolution rather than continue doubtfully; disclose the delay | Told there is a delay | `REQ-858` | Reconcile then resume | Halt event | `FPA-371`–`FPA-374` | cites `12A-RK-012` |
| `FPE-099` | C4 | Enforcement practice review finds no capacity to meet a guarantee | Capacity honesty | B-12, owner | `FPW-052` | Gap declared with its compensating control; never described as met | None | No assumed capacity | Owner staffing decision | Review record | `FPA-375`, `FPA-376` | `UD-054` |
| `FPE-100` | C4 | Transparency report proposed with case-level detail | Publication scope | B-12, owner | `FPW-052` | Structure defined; publication withheld; no overturn rate presented as measured | None | Publishing counts builds trust, publishing cases destroys privacy | Owner decision | Configuration event | `FPA-377`, `FPA-378` | `UD-058` |

---

## 3. Acceptance-test specifications

**3.1 Record schema.** Every `FPA-###` row supplies: objective · requirement rows · normative rule references (via the workflow) · workflow · integration contract · edge cases · **Given** (preconditions and required test data) · **When** (action sequence) · **Then** (expected result, expected state transition, player-visible outcome, permission outcome and expected audit evidence, each observable) · **Fail** (the condition that fails the test) · classification · execution requirement (`auto` single-component document or logic check · `integration` cross-subsystem check · `manual` requires a human reviewer or operator) · status.

**3.2 Shared defaults, applied once.** Unless a row says otherwise: precondition = an authenticated session, a case or signal in the stated state, and the relevant register values at their recorded status; required data = the logical fields named by the workflow's `Required input`, never a physical schema; expected audit evidence = one `EVD-026`-class event in the shape of `EVD-027` containing identifiers, decisions and reasons and no content bodies (`EVD-028`); expected permission outcome = the action is granted only to the actor class named in `Annex C` for that workflow, and denied to every class marked `✗`; player-visible outcome = within `MOD-017`/`MOD-018`/`PRV-019`/`PRV-020`. **A row whose expectation would require a number the corpus has not approved asserts `PROVISIONAL_BLOCK` instead, and is classified `OWN`.**

**3.3 Counts and classification split.** 378 specifications, `FPA-001`…`FPA-378`, contiguous; `FPA-379` onward is unallocated. Classes, counted from the register: `SEC` 77 · `NEG` 48 · `POS` 48 · `REC` 44 · `BND` 43 · `OWN` 35 · `PRV` 36 · `INT` 47 = 378. Execution requirement: `auto` 169 · `integration` 114 · `manual` 95. Status: **`SPECIFIED` 368 · `BLOCKED` 10 · `IMPLEMENTED` 0 · `EXECUTED` 0 · `PASS` 0**. Nothing has been executed: **there is no implementation to run these against** (`GOV-023`, `P12B-26`).

**3.4 Blocked rows.** Exactly ten rows are `BLOCKED` — `FPA-309`–`FPA-314`, `FPA-316`, `FPA-318`, `FPA-319` and `FPA-320`. Each asserts a behaviour that can only be graded against the outstanding security obligations named in `FPG-04` and `FPG-05`: an implemented chained digest, an executed verification run, a protective audit trigger, and protection of the spine from the service role's ordinary path. `FPA-315` and `FPA-317` in the same block stay `SPECIFIED` because they assert a blocking branch and a corpus-wide non-claim, both of which are checkable today. These rows stay `BLOCKED` and **do not** close, downgrade or reinterpret `P12B-14`, `P12B-16` or `P12B-23`.

### 3.5 Register — Family A, intake and triage (`FPW-001`–`FPW-005`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-001` | A complete report creates exactly one accusation row | `REQ-822` | `FPW-001`/`INT-017` | POS | valid session; all `MOD-002` fields | submit | case `OPEN`; state word is "accusation", never "violation"; `EVD-026` evidence-write row | any violation language, or a second row | `auto` | SPECIFIED |
| `FPA-002` | A report missing subject or category is refused without creating state | `REQ-822` | `FPW-001` | NEG | valid session; subject omitted | submit | rejection names the failed condition only (`PRV-020`); no report row; no spine row | any partial row written | `auto` | SPECIFIED |
| `FPA-003` | Intake outage never silently loses a report | `REQ-822`, `REQ-863` | `FPW-001`/`FR-06` | REC | intake unavailable | submit | retryable failure surfaced to the player; nothing queued half-written | silent drop or a generic success message | `integration` | SPECIFIED |
| `FPA-004` | No enforcement may follow an unreceived report | `REQ-822` | `FPW-001`/`INT-017` | SEC | report never reached intake | reviewer attempts an action | action denied; case does not exist | any consequence applied | `auto` | SPECIFIED |
| `FPA-005` | Reporter identity is never disclosed to the reported party | `REQ-803` | `FPW-001`/`INT-017` | PRV | one report and one case | subject queries the case | response contains no reporter field at any level | any field implying origin | `integration` | SPECIFIED |
| `FPA-006` | Supplied artefacts are stored separately as pointers | `REQ-826` | `FPW-001` | POS | artefact attached | submit | artefact referenced by provenance, not treated as a finding | artefact auto-escalates the state | `auto` | SPECIFIED |
| `FPA-007` | Duplicate reports coalesce to one case | `REQ-823` | `FPW-002`/`F-FP-008` | POS | same `s`,`v`,`e` inside `w` | ten submissions | one case, cluster count 10 | two cases | `auto` | SPECIFIED |
| `FPA-008` | Different violation classes never coalesce | `REQ-823` | `FPW-002` | BND | same subject, classes `V-06` and `V-09` | two submissions | two distinct cases | coalescing across classes | `auto` | SPECIFIED |
| `FPA-009` | Coordinated volume raises no tier | `REQ-823` | `FPW-002`/`MOD-003` | NEG | 200 reports, one subject | triage | severity inputs unchanged; volume recorded as triage only | any tier movement | `auto` | SPECIFIED |
| `FPA-010` | A missing subject yields a held report, not a cluster | `REQ-822` | `FPW-002` | BND | subject empty | cluster step | held; no key computed | a cluster formed on a null subject | `auto` | SPECIFIED |
| `FPA-011` | A report naming an administrator bypasses the ordinary chain | `REQ-825` | `FPW-003`/`INT-015` | SEC | subject holds `R-MOD` | submit | routed confidentially; the subject's peers cannot see the case | ordinary queue placement | `integration` | SPECIFIED |
| `FPA-012` | Absence of an independent reviewer is labelled and disclosed | `REQ-825` | `FPW-003` | NEG | single-operator staffing | route | `unsegregated` label set and disclosed to the owner | a claimed independent review | `manual` | SPECIFIED |
| `FPA-013` | Retaliation against a reporter opens its own case | `REQ-825` | `FPW-003`/`MOD-006` | POS | pattern after a report | submit | separate `V-15` case, own evidence path | merging into the original | `integration` | SPECIFIED |
| `FPA-014` | A moderator never sees a case where they are the subject | `REQ-825` | `FPW-003`/`ADM-009` | SEC | actor is the subject | assignment | denied | self-assignment possible | `auto` | SPECIFIED |
| `FPA-015` | A reviewer in the subject's Alliance is excluded | `REQ-795` | `FPW-004`/`INT-008` | SEC | shared Alliance membership | assign | excluded and the exclusion recorded | assignment succeeds | `integration` | SPECIFIED |
| `FPA-016` | A declared interest excludes the reviewer | `REQ-795` | `FPW-004` | NEG | interest declared | assign | excluded | ignored interest | `auto` | SPECIFIED |
| `FPA-017` | Exclusion impossibility produces the label, never a silent pass | `REQ-795` | `FPW-004` | OWN | no alternate reviewer | assign | `unsegregated` recorded and disclosed to the affected player | proceeding without the label | `manual` | SPECIFIED |
| `FPA-018` | Screening data outage stops the decision | `REQ-795` | `FPW-004`/`FR-02` | REC | membership data unavailable | assign | case holds at triage | decision on unscreened reviewer | `integration` | SPECIFIED |
| `FPA-019` | Triage order enforces safety, state, status then conflict | `REQ-766` | `FPW-005`/`MOD-008` | POS | fresh case | triage | all four assessed before any action; sequence recorded | any action before assessment | `auto` | SPECIFIED |
| `FPA-020` | A hold is never recorded as a sanction | `REQ-864` | `FPW-005`/`MOD-009` | NEG | `E1`, reversible hold granted | triage | record class is "hold"; no tier assigned | tier or ladder rung written | `auto` | SPECIFIED |
| `FPA-021` | `E0` alone cannot produce a hold | `REQ-766` | `FPW-005`/`EVD-002` | BND | only an `E0` indicator | request hold | refused; review object only | hold created | `auto` | SPECIFIED |
| `FPA-022` | `EX` produces no adverse action and closes the case | `REQ-766` | `FPW-005`/`EVD-008` | POS | state `EX` | close | `INCONCLUSIVE`; subject unsanctioned; bounded notice to the reporter | any adverse consequence | `auto` | SPECIFIED |
| `FPA-023` | Detection downtime never blocks legitimate play | `REQ-863` | `FPW-005`/`FR-04` | REC | detector unavailable | play continues | turn resolves; gap recorded and backfilled | play blocked by detection state | `integration` | SPECIFIED |
| `FPA-024` | A missing protection never silently disappears | `REQ-863` | `FPW-005` | NEG | detection degraded | boundary | recorded gap with a reconstructible record | unrecorded absence | `auto` | SPECIFIED |
| `FPA-025` | Ambiguous identity resolves to the least-harmful reading | `REQ-865` | `FPW-005`/`FPW-020` | REC | two candidate subjects | triage | no restriction applied pending resolution | restricting both by default | `manual` | SPECIFIED |
| `FPA-026` | A protection or dormancy state is not converted into a sanction | `REQ-815` | `FPW-005`/`MOD-031` | NEG | subject is protected | triage | owning eligibility rule governs; B-12 does not punish the state | sanction arising from dormancy | `integration` | SPECIFIED |

### 3.6 Register — Family B, detection and evidence (`FPW-006`–`FPW-010`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-027` | Automation output is limited to the four permitted classes | `REQ-790` | `FPW-006`/`EVD-003` | SEC | rule fires | emit | review object, signal, reversible restriction or correction instruction only | any `E3`, suspension, permanent measure or public statement | `auto` | SPECIFIED |
| `FPA-028` | A detector may never publish a finding | `REQ-790` | `FPW-006` | NEG | automated path | attempt a public statement | refused and recorded | statement issued | `auto` | SPECIFIED |
| `FPA-029` | A signal cannot become a conduct finding without a human | `REQ-766` | `FPW-006`/`FPW-011` | NEG | `E1` signal | attempt `E3` | state stays `E1` | automatic escalation | `auto` | SPECIFIED |
| `FPA-030` | Missing detector input creates no signal | `REQ-766` | `FPW-006`/`GOV-006` | BND | required input absent | run | no object; gap recorded | a default-value signal | `auto` | SPECIFIED |
| `FPA-031` | Duplicate detector fires coalesce to one object | `REQ-770` | `FPW-006`/`SEC-008` | POS | same key twice | run | one review object | two objects | `auto` | SPECIFIED |
| `FPA-032` | Detection internals never leave the `SEC` class | `REQ-796` | `FPW-006`/`PRV-014` | PRV | any surface | request | no method, threshold or rule internal returned | any internal disclosed | `integration` | SPECIFIED |
| `FPA-033` | Exactly one of five states is assignable | `REQ-766` | `FPW-007`/`EVD-001` | POS | any case | assign | one state; no sixth, no score field | two states or a numeric confidence | `auto` | SPECIFIED |
| `FPA-034` | A behavioural anomaly alone never exceeds review | `REQ-767` | `FPW-007`/`EVD-004` | NEG | anomaly only | assign | capped at `E1` review object | `E2` or higher | `auto` | SPECIFIED |
| `FPA-035` | A network attribute never supports a tier above `T1` | `REQ-778` | `FPW-007`/`NET-039` | BND | shared `/64` only | propose `T2` | refused; ceiling enforced | tier above the ceiling | `auto` | SPECIFIED |
| `FPA-036` | No inference of common control from a network signal | `REQ-778` | `FPW-007`/`MA-005` | NEG | network match | write a finding | refused; triage ordering only | any control claim | `auto` | SPECIFIED |
| `FPA-037` | Counters key to account and resource, never to IP | `REQ-775` | `FPW-007`/`MA-010` | SEC | counter increment | inspect key | key = account + protected resource | any IP-keyed counter | `integration` | SPECIFIED |
| `FPA-038` | Identity-layer multi-accounting is stated as undetectable | `REQ-797` | `FPW-007`/`EVD-006` | PRV | claim attempted | record | text reads "not establishable" | any verification claim | `manual` | SPECIFIED |
| `FPA-039` | The sufficiency predicate matches the matrix exactly | `REQ-793` | `FPW-008`/`F-FP-007` | POS | `E3`, 2 independent, 1 non-behavioural | evaluate | true for conduct | false | `auto` | SPECIFIED |
| `FPA-040` | Two outputs of one detector are not independent | `REQ-767` | `FPW-008`/`EVD-011` | NEG | same detector | evaluate | `n_i` counts one | counted two | `auto` | SPECIFIED |
| `FPA-041` | A missing source count evaluates false | `REQ-793` | `FPW-008` | BND | `n_i` absent | evaluate | false, i.e. no consequence | permissive default | `auto` | SPECIFIED |
| `FPA-042` | `EX` always evaluates insufficient | `REQ-766` | `FPW-008` | BND | state `EX` | evaluate | false | true | `auto` | SPECIFIED |
| `FPA-043` | A reversible hold at `E1` bypasses the predicate legitimately | `REQ-766` | `FPW-008`/`EVD-002` | BND | `E1` | hold request | permitted; predicate not required | refusal of the only permitted action | `auto` | SPECIFIED |
| `FPA-044` | No universal confidence score exists anywhere | `REQ-793` | `FPW-008`/`EVD-007` | SEC | any record | inspect | no score field in any specification artefact | a score introduced | `auto` | SPECIFIED |
| `FPA-045` | An undeclared detector is never enabled | `REQ-791` | `FPW-009` | NEG | declaration incomplete | publish | refused; attempt recorded | enabled | `auto` | SPECIFIED |
| `FPA-046` | Every declared FP class from `EVD-014` is present | `REQ-792` | `FPW-009` | POS | catalogue | audit | all named classes covered | any class missing | `manual` | SPECIFIED |
| `FPA-047` | A capability needing refused data is recorded unavailable | `REQ-797` | `FPW-009` | NEG | data prohibited | propose | `not available`; no proxy | a softened claim | `manual` | SPECIFIED |
| `FPA-048` | Detection uses only inventoried existing data | `REQ-796` | `FPW-009`/`PRV-014` | PRV | proposed source | review | source is already held for gameplay, security or legal purpose | new telemetry, fingerprint or SDK | `integration` | SPECIFIED |
| `FPA-049` | Preservation protects referenced records from compaction | `REQ-829` | `FPW-010`/`EVD-021` | REC | case open | compaction run | preserved rows survive | any preserved row compacted | `integration` | SPECIFIED |
| `FPA-050` | Preservation is never indefinite retention | `REQ-831` | `FPW-010`/`UD-055` | OWN | closure | release | preservation released under the class rule | permanent hold without a case | `manual` | SPECIFIED |
| `FPA-051` | Every access, annotation, correction and export writes a custody event | `REQ-828` | `FPW-010`/`EVD-022` | SEC | four handling acts | perform | four appended events, no in-place edit | a silent act | `integration` | SPECIFIED |
| `FPA-052` | An artefact digest mismatch raises an incident, not a correction | `REQ-827` | `FPW-010`/`EVD-037` | SEC | digest differs | verify | incident opened | routine overwrite | `auto` | SPECIFIED |
| `FPA-053` | Conflicting server records are resolved with a stated reason | `REQ-832` | `FPW-010`/`EVD-018` | NEG | two conflicting records | resolve | conflict and governing reason recorded | the convenient record adopted | `manual` | SPECIFIED |
| `FPA-054` | Evidence never appears in logs, analytics or default views | `REQ-831` | `FPW-010`/`EVD-024` | PRV | case open | inspect views | evidence absent from every default surface | any copy path present | `integration` | SPECIFIED |

### 3.7 Register — Family C, finding, decision and sanction (`FPW-011`–`FPW-015`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-055` | A finding names the class and the relied-on element | `REQ-811` | `FPW-011`/`FP-021` | POS | `E3` reached | recommend | `V-` id plus element cited; no generic "abuse" | catch-all wording | `auto` | SPECIFIED |
| `FPA-056` | No violation wording appears before `E3` | `REQ-768` | `FPW-011`/`FP-020` | NEG | state `E1` | draft text | suspicion or review wording only | "confirmed" language | `auto` | SPECIFIED |
| `FPA-057` | An uncorroborable screenshot closes the case `EX` | `REQ-826` | `FPW-011`/`EVD-013` | REC | server record absent | assess | `EX` with what was examined | a finding on the artefact alone | `manual` | SPECIFIED |
| `FPA-058` | Attempt is actionable only where Annex A names it, at `E2` | `REQ-767` | `FPW-011`/`FP-024` | BND | attempt, no effect | assess | permitted only for attempt-bearing classes | retroactive upgrade of an unrelated event | `auto` | SPECIFIED |
| `FPA-059` | Impact must be demonstrated where the class requires it | `REQ-813` | `FPW-011`/`FP-023` | NEG | possible-only impact | assess | insufficient | finding on possibility | `auto` | SPECIFIED |
| `FPA-060` | Cooperation without false agency is dismissed | `REQ-784` | `FPW-011`/`CO-001` | POS | allied coordination | assess | dismissed; legitimate behaviour recorded | collusion charge | `manual` | SPECIFIED |
| `FPA-061` | Graph output never raises a tier | `REQ-787` | `FPW-011`/`CO-004` | NEG | cluster score high | decide | queue input only | tier movement from topology | `auto` | SPECIFIED |
| `FPA-062` | Investigation corruption yields inconclusive, never proven | `REQ-794` | `FPW-011`/`FR-14` | REC | record damaged | resume | returns to last recorded state; case stays open or `EX` | auto-close as proven | `integration` | SPECIFIED |
| `FPA-063` | Severity excludes any repetition term | `REQ-813` | `FPW-012`/`F-FP-001` | POS | one confirmed prior | compute | `SEV = S_c + I_p + K − M`, unchanged by the prior | double counting | `auto` | SPECIFIED |
| `FPA-064` | Repetition is applied exactly once, by `F-FP-011` | `REQ-812` | `FPW-012`/`FP-025` | BND | priors 0,1,2,3 | compute | `min(R,2)` cap; `R>2` adds nothing | linear escalation | `auto` | SPECIFIED |
| `FPA-065` | An unconfirmed prior never enters severity | `REQ-813` | `FPW-012` | NEG | dismissed case on file | compute | `R` excludes it | prior counted | `auto` | SPECIFIED |
| `FPA-066` | Mitigation may reduce a tier but not erase material impact | `REQ-813` | `FPW-012`/`FP-026` | POS | self-report, restoration | compute | tier may drop; finding stands | finding expunged | `manual` | SPECIFIED |
| `FPA-067` | A successful appeal removes the prior from the count | `REQ-836` | `FPW-012`/`F-FP-011` | REC | prior reversed | recompute | prior excluded | stale prior counted | `auto` | SPECIFIED |
| `FPA-068` | Economic correction is never increased by a prior | `REQ-817` | `FPW-012`/`COR-010` | BND | two confirmed priors | compute `C` | `C` identical to a first offence | severity inflating value | `auto` | SPECIFIED |
| `FPA-069` | Tier-to-evidence gate is enforced | `REQ-816` | `FPW-013`/`MOD-038` | BND | `E2` and `T3` proposed | decide | refused: `T3` needs `E3` plus impact | `T3` on `E2` | `auto` | SPECIFIED |
| `FPA-070` | No tier may be imposed on `E0`, `E1` or `EX` | `REQ-766` | `FPW-013` | NEG | low state | decide | refused | any tier | `auto` | SPECIFIED |
| `FPA-071` | `T4` and `T5` require the owner-authorized threshold | `REQ-816` | `FPW-013`/`MOD-037` | OWN | high severity | decide | blocked pending the owner's authority split | automatic top tier | `manual` | SPECIFIED |
| `FPA-072` | Second review is required above the first suspension tier | `REQ-795` | `FPW-013`/`MOD-022` | SEC | single reviewer available | decide | held pending review, or labelled unsegregated | unilateral `T3` | `manual` | SPECIFIED |
| `FPA-073` | A sanction never writes another subsystem's state | `REQ-859`, `REQ-861` | `FPW-013`/`ADM-001` | SEC | balance, election, snapshot target | decide | blocked by the prohibition list | any in-place edit | `integration` | SPECIFIED |
| `FPA-074` | No collective punishment of an Alliance or household | `REQ-784` | `FPW-013`/`CO-010` | NEG | group-level request | decide | refused; only evidenced accounts act | group sanction | `auto` | SPECIFIED |
| `FPA-075` | Moderation may not favour, punish reporting, or enforce in-game deals | `REQ-815` | `FPW-013`/`MOD-024` | SEC | any prohibited purpose | act | denied and recorded | purpose accepted | `manual` | SPECIFIED |
| `FPA-076` | An unapproved duration returns `PROVISIONAL_BLOCK` | `REQ-816` | `FPW-013`/`F-FP-005` | OWN | `FP-P04` undefined | set duration | blocked; no default length | a number invented | `auto` | SPECIFIED |
| `FPA-077` | The notice states all seven required elements | `REQ-821` | `FPW-014`/`MOD-017` | POS | tier decided | render | class, element, evidence class, tier, end, appeal route, correction flag | any element missing | `manual` | SPECIFIED |
| `FPA-078` | Method and thresholds are withheld by rule | `REQ-804` | `FPW-014`/`MOD-018` | PRV | notice drafted | render | no detection detail | internal disclosed | `manual` | SPECIFIED |
| `FPA-079` | A correction is stated as separate from the sanction | `REQ-817` | `FPW-014`/`FP-031` | POS | both applied | render | notice distinguishes them; two appeal tracks | merged consequence | `auto` | SPECIFIED |
| `FPA-080` | No action is invisible to the affected account | `REQ-821` | `FPW-014`/`MOD-030` | NEG | action committed | inspect | notice exists, or a recorded delay with review | silent action | `auto` | SPECIFIED |
| `FPA-081` | Delayed notice records the delay and its review | `REQ-821` | `FPW-014`/`ADM-030` | REC | active investigation | defer | delay and review written | indefinite silence | `manual` | SPECIFIED |
| `FPA-082` | Notice delivery failure digests and records | `REQ-850` | `FPW-014`/`FR-07` | REC | delivery error | deliver | action stands; entry in digest; failure recorded | action reverted or hidden | `integration` | SPECIFIED |
| `FPA-083` | A notice revealing a reporter or third party is rejected at assembly | `REQ-803` | `FPW-014`/`PRV-019` | PRV | content contains either | assemble | blocked before commit | content shipped | `auto` | SPECIFIED |
| `FPA-084` | Notice assembly failure leaves nothing committed | `REQ-776` | `FPW-014`/`FR-03` | SEC | spine unavailable | commit | whole transaction fails closed | action without a record | `integration` | SPECIFIED |
| `FPA-085` | Every closure uses one of six outcomes | `REQ-794` | `FPW-015`/`EVD-020` | POS | decision made | close | one of the six, with reason and state | any seventh outcome | `auto` | SPECIFIED |
| `FPA-086` | A closure without reconstruction is invalid | `REQ-794` | `FPW-015` | NEG | evidence list empty | close | rejected | closure accepted | `auto` | SPECIFIED |
| `FPA-087` | A referral does not transfer record ownership | `REQ-815` | `FPW-015`/`ADM-029` | INT | referred to another owner | close | B-12 record retained; `REFERRED` stated | ownership moved | `manual` | SPECIFIED |
| `FPA-088` | An Alliance expulsion appeal is referred, not decided | `REQ-815` | `FPW-015`/`INT-018` | INT | expulsion dispute | close | `REFERRED` citing `UD-044` unresolved | B-12 adjudicating | `manual` | SPECIFIED |
| `FPA-089` | Every review, annotation and escalation is appended and visible to the appeal reviewer | `REQ-794` | `FPW-015`/`EVD-040` | SEC | three review passes | close | three appended history entries; reviewer sees all | overwritten history | `auto` | SPECIFIED |
| `FPA-090` | The reporter receives a bounded outcome notice | `REQ-803` | `FPW-015`/`EVD-008` | POS | `EX` closure | close | bounded notice, no finding language | no notice at all | `manual` | SPECIFIED |

### 3.8 Register — Family D, restriction, identity and association (`FPW-016`–`FPW-020`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-091` | Enforcement is expressed only as an account-level action | `REQ-818` | `FPW-016`/`INT-002` | SEC | tier decided | apply | account state changed; no nation or pair field touched | a nation field written | `integration` | SPECIFIED |
| `FPA-092` | Only B-03 applies the restriction | `REQ-859` | `FPW-016`/`INT-001` | INT | B-12 request | apply | B-03 executes and confirms; B-12 records the request | B-12 applying directly | `integration` | SPECIFIED |
| `FPA-093` | A duplicate enforcement request coalesces | `REQ-770` | `FPW-016`/`SEC-008` | BND | same key twice | apply twice | one application, one record | two applications | `auto` | SPECIFIED |
| `FPA-094` | A replay after the key window is rejected by state | `REQ-771` | `FPW-016`/`F-FP-010` | BND | retry path `P_r` | replay beyond `K` | rejected by entitlement, not missing key | replay accepted | `integration` | SPECIFIED |
| `FPA-095` | Suspension preserves the appeal and data-subject routes | `REQ-833` | `FPW-016`/`MOD-015` | POS | `T3` active | attempt appeal | route available | route blocked | `manual` | SPECIFIED |
| `FPA-096` | A communication restriction never blocks the appeal route | `REQ-803` | `FPW-016`/`MOD-013` | BND | restriction active | appeal | accepted | blocked | `integration` | SPECIFIED |
| `FPA-097` | B-12 never re-parents a nation | `REQ-859` | `FPW-016`/`12A-INT-03` | SEC | ownership query | any action | ownership unchanged | ownership changed | `auto` | SPECIFIED |
| `FPA-098` | A B-03 outage leaves the decision pending, never partial | `REQ-776` | `FPW-016`/`FR-02` | REC | applier unavailable | apply | nothing applied; decision pending | partial application | `integration` | SPECIFIED |
| `FPA-099` | Every temporary measure is turn-counted, never wall-clock | `REQ-812` | `FPW-017`/`MOD-040` | BND | any tier | set duration | value expressed in boundaries; ends at the next one | a minute-based value | `auto` | SPECIFIED |
| `FPA-100` | `D = D_base × (1 + x)` respects `D_max` | `REQ-812` | `FPW-017`/`F-FP-005` | BND | extension count rising | extend repeatedly | capped at the tier maximum | unbounded extension | `auto` | SPECIFIED |
| `FPA-101` | Expiry is automatic with no operator act | `REQ-812` | `FPW-017`/`MOD-041` | REC | boundary passes `t_e` | resume play | capability returns | persistence without decision | `integration` | SPECIFIED |
| `FPA-102` | `T1` carries no duration | `REQ-812` | `FPW-017` | BND | warning issued | commit | no expiry object created | a timed warning | `auto` | SPECIFIED |
| `FPA-103` | Unapproved base turns produce `PROVISIONAL_BLOCK` | `REQ-816` | `FPW-017`/`FP-P04` | OWN | `FP-P04` undefined | set duration | blocked with the dependency named | a default number used | `auto` | SPECIFIED |
| `FPA-104` | A boundary processing failure records the gap | `REQ-863` | `FPW-017`/`FR-14` | REC | turn failed | resume | measure reconciled at next boundary; gap recorded | silent persistence | `integration` | SPECIFIED |
| `FPA-105` | A sanction survives a nation reroll | `REQ-818` | `FPW-018`/`MOD-033` | INT | `T2` active | reroll | restriction remains attached to the account | amnesty by reroll | `integration` | SPECIFIED |
| `FPA-106` | A pending case is not closed by retirement | `REQ-818` | `FPW-018`/`RRL-017` | INT | case open | retire | case continues | auto-closure | `integration` | SPECIFIED |
| `FPA-107` | A preservation order blocks the reroll | `REQ-783` | `FPW-018`/`ECN-204` | INT | order active | reroll request | refused with a stated reason | reroll allowed | `integration` | SPECIFIED |
| `FPA-108` | Pre-reroll divesting is reviewed, never auto-reversed | `REQ-782` | `FPW-018`/`RRL-015` | INT | transfer then reroll | assess | review opened; no automatic reversal | automatic reversal as a rule | `manual` | SPECIFIED |
| `FPA-109` | Protection is not re-granted by a reroll | `REQ-777` | `FPW-018`/`RRL-018` | INT | restricted account | reroll | no fresh protection from the enforcement | protection reset | `integration` | SPECIFIED |
| `FPA-110` | Enforcement survival is checked without inventing a state | `REQ-818` | `FPW-018`/`MA-002` | SEC | any survival case | apply | account, nation and pair states remain three objects | a fourth state created | `auto` | SPECIFIED |
| `FPA-111` | A shared-context declaration grants no exemption | `REQ-779` | `FPW-019`/`MA-003` | NEG | declaration on file | evaluate a pair | outcome unchanged by the declaration | exemption applied | `auto` | SPECIFIED |
| `FPA-112` | Absence of a declaration is never aggravating | `REQ-779` | `FPW-019` | NEG | no declaration | assess severity | no input from absence | absence counted | `auto` | SPECIFIED |
| `FPA-113` | Only the author and the integrity role can read a declaration | `REQ-780` | `FPW-019`/`MA-004` | PRV | third-party player | request | omitted entirely | any leak | `integration` | SPECIFIED |
| `FPA-114` | The author can delete the declaration by event, not edit | `REQ-780` | `FPW-019`/`PRV-022` | REC | declaration exists | delete | deletion recorded as an event | silent removal | `auto` | SPECIFIED |
| `FPA-115` | A declaration never proves common control | `REQ-781` | `FPW-019`/`MA-011` | NEG | declaration names two accounts | charge `V-01` | charge rests on flow evidence only | identity claimed | `auto` | SPECIFIED |
| `FPA-116` | A declaration contradicted by a proven flow yields to the flow | `REQ-781` | `FPW-019`/`MA-006` | INT | declaration says "separate" | flow proven | flow governs | declaration overriding evidence | `manual` | SPECIFIED |
| `FPA-117` | A wrong association separates, lifts, records and notifies | `REQ-865` | `FPW-020`/`COR-013` | REC | two accounts merged | dispute upheld | both restrictions lifted by append; each notified | lifting without a record | `integration` | SPECIFIED |
| `FPA-118` | Misattribution reverses first and investigates second | `REQ-865` | `FPW-020` | REC | suspicion of error | detect | relief applied before the finding | investigation before relief | `manual` | SPECIFIED |
| `FPA-119` | Account compromise does not by itself excuse or aggravate | `REQ-767` | `FPW-020`/`REQ-794` | INT | compromise reported | assess conduct | conduct judged on its own evidence; compromise handled by B-03/Stage 6 | blanket amnesty or blanket blame | `manual` | SPECIFIED |
| `FPA-120` | B-12 holds no credential during recovery | `REQ-840` | `FPW-020`/`SEC-027` | SEC | recovery in progress | any step | no credential stored, logged or displayed | any credential surface | `integration` | SPECIFIED |
| `FPA-121` | A recovery state never becomes a sanction state | `REQ-815` | `FPW-020`/`ACC-017` | NEG | `RECOVERY_LOCKED` | decide | enforcement not imposed for being in recovery | recovery read as guilt | `auto` | SPECIFIED |
| `FPA-122` | Conflicting account states surface to a reviewer | `REQ-820` | `FPW-020`/`MOD-032` | INT | two states disagree | any action | surfaced, not resolved silently | silent adoption | `manual` | SPECIFIED |

### 3.9 Register — Family E, correction and recovery (`FPW-021`–`FPW-026`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-123` | A correction instruction never writes a balance directly | `REQ-845` | `FPW-021`/`INT-003` | SEC | excess identified | instruct | B-04 computes and appends; B-12 writes no balance | direct write | `integration` | SPECIFIED |
| `FPA-124` | An unreferenced correction is invalid | `REQ-817` | `FPW-021`/`COR-002` | NEG | original omitted | submit | rejected | accepted | `auto` | SPECIFIED |
| `FPA-125` | A correction needs no finding about a person | `REQ-817` | `FPW-021`/`MOD-051` | POS | record proves impossible effect | correct | applied; case outcome may be `CORRECTION_ONLY` | a conduct finding required | `auto` | SPECIFIED |
| `FPA-126` | A reason code and case reference accompany every correction | `REQ-821` | `FPW-021`/`COR-016` | POS | correction | commit | both present in the spine event | either absent | `auto` | SPECIFIED |
| `FPA-127` | Political corrections never set `government_id` | `REQ-860` | `FPW-021`/`DMP-122` | INT | election effect | correct | adjustment names the original; `government_id` unchanged | government altered | `integration` | SPECIFIED |
| `FPA-128` | City corrections never edit capacity, housing or book value | `REQ-819` | `FPW-021`/`URB-143` | INT | facility state wrong | correct | appended `ADJUSTMENT`/`REVERSAL` only | in-place edit | `integration` | SPECIFIED |
| `FPA-129` | A failed correction rolls back exactly | `REQ-770` | `FPW-021`/`COR-018` | REC | mid-write fault | commit | no partial value remains | partial commit | `integration` | SPECIFIED |
| `FPA-130` | Retry uses the same idempotency key | `REQ-771` | `FPW-021`/`FR-09` | REC | failure occurred | retry | same key; one effect | a new key creating two effects | `auto` | SPECIFIED |
| `FPA-131` | A correction cannot mint value | `REQ-861` | `FPW-021`/`SEC-020` | SEC | any correction | commit | total value conserved or decreased | net creation | `auto` | SPECIFIED |
| `FPA-132` | A correction cannot create a negative balance | `REQ-817` | `FPW-021`/`COR-012` | BND | balance below zero implied | commit | floors at zero with a shortfall record | negative balance | `auto` | SPECIFIED |
| `FPA-133` | No correction reorders a closed turn | `REQ-772` | `FPW-021`/`COR-007` | INT | turn sealed | apply | applied at the next valid boundary | closed turn rewritten | `integration` | SPECIFIED |
| `FPA-134` | A correction is disclosed to the affected account only | `REQ-803` | `FPW-021`/`MOD-054` | PRV | two parties linked | notify | each sees its own change only | third-party data disclosed | `integration` | SPECIFIED |
| `FPA-135` | A correction is disputable once through the appeal route | `REQ-833` | `FPW-021`/`COR-008` | POS | correction applied | dispute | one appeal accepted | no route offered | `manual` | SPECIFIED |
| `FPA-136` | An administrative adjustment requires published policy | `REQ-845` | `FPW-021`/`SEC-019` | SEC | no published policy | adjust | refused | discretionary adjustment | `auto` | SPECIFIED |
| `FPA-137` | No excess produces zero correction | `REQ-817` | `FPW-022`/`F-FP-002` | BND | `V_obs = V_law` | compute | `C = 0` | any removal | `auto` | SPECIFIED |
| `FPA-138` | A loss is never handled as a removal | `REQ-817` | `FPW-022` | BND | `V_obs < V_law` | compute | `C = 0`; routed to compensation | negative removal | `auto` | SPECIFIED |
| `FPA-139` | The cap binds at the illicit benefit | `REQ-817` | `FPW-022`/`COR-006` | BND | `V_obs − V_law > B_i` | compute | `C = B_i` | removal above benefit | `auto` | SPECIFIED |
| `FPA-140` | A missing lawful counterfactual yields `NO_CALCULATION` | `REQ-776` | `FPW-022` | NEG | `V_law` absent | compute | `NO_CALCULATION` plus incident | zero assumed | `auto` | SPECIFIED |
| `FPA-141` | Only proved-linked transactions enter the benefit sum | `REQ-786` | `FPW-022`/`F-FP-003` | SEC | mixed proven and unproven legs | compute `B_i` | unproven excluded | all legs included | `integration` | SPECIFIED |
| `FPA-142` | An unvaluable leg returns `INCONCLUSIVE`, never an estimate | `REQ-826` | `FPW-022` | REC | leg unpriceable | compute | leg excluded and flagged | a fabricated value | `manual` | SPECIFIED |
| `FPA-143` | Market-priced assets use the owner's recorded price | `REQ-860` | `FPW-022`/`B-07` | INT | asset priced at boundary | compute | owning market's value used | B-12 defining a price | `integration` | SPECIFIED |
| `FPA-144` | Rounding follows the ledger's minor unit | `REQ-771` | `FPW-022` | BND | fractional result | compute | minor-unit rounding, no fraction | fractional unit written | `auto` | SPECIFIED |
| `FPA-145` | Removal follows the flow to the benefiting account | `REQ-782` | `FPW-023`/`COR-011` | INT | benefit moved one hop | remove | second account charged | only the first charged | `integration` | SPECIFIED |
| `FPA-146` | Insolvency floors at zero and records the shortfall | `REQ-817` | `FPW-023`/`COR-012` | BND | held < owed | remove | zero floor plus shortfall record | negative balance or a debt object | `auto` | SPECIFIED |
| `FPA-147` | No debt mechanic is invented | `REQ-861` | `FPW-023` | SEC | shortfall exists | inspect | no new currency, obligation or claim type | a debt introduced | `auto` | SPECIFIED |
| `FPA-148` | Both legs are charged only within the owner's reach decision | `REQ-782` | `FPW-023`/`UD-052` | OWN | flow established | charge both | blocked pending `UD-052`; receiving leg only | both sides assumed | `manual` | SPECIFIED |
| `FPA-149` | A removal is recorded as a correction, never a fine | `REQ-817` | `FPW-023`/`MOD-057` | POS | violation confirmed | remove | `ILLICIT_REMOVAL` type | type `COMPENSATION` or a fine | `auto` | SPECIFIED |
| `FPA-150` | A sanction and a removal can coexist and stay separable | `REQ-817` | `FPW-023`/`FP-031` | INT | both justified | commit both | two records, two appeal tracks | merged consequence | `auto` | SPECIFIED |
| `FPA-151` | Value moving through an Alliance container is not shielded | `REQ-786` | `FPW-023`/`ALL-159` | INT | container leg | trace | same checks apply; attribution preserved | attribution lost | `integration` | SPECIFIED |
| `FPA-152` | An innocent third-party transfer is excluded unless proved | `REQ-786` | `FPW-023` | NEG | unproven recipient | compute | excluded | included by association | `auto` | SPECIFIED |
| `FPA-153` | A reversal appends the exact opposite of the remainder | `REQ-836` | `FPW-024`/`F-FP-014` | POS | partial correction | reverse | opposite of remaining unreversed effect | full opposite on a partial | `auto` | SPECIFIED |
| `FPA-154` | A reversal with no resolvable original is not applied | `REQ-836` | `FPW-024` | NEG | dangling reference | reverse | `NO_ORIGINAL`; nothing appended | phantom reversal | `auto` | SPECIFIED |
| `FPA-155` | A duplicate reversal coalesces and adds nothing | `REQ-770` | `FPW-024`/`COR-005` | BND | same reversal twice | submit twice | net effect once | double credit | `auto` | SPECIFIED |
| `FPA-156` | Restitution is computed by the owning subsystem | `REQ-836` | `FPW-024`/`MOD-048` | INT | appeal upheld | restore | owner's rule executes; no typed amount | administrator sets the figure | `integration` | SPECIFIED |
| `FPA-157` | A reversal ends the restriction and lifts the suspension | `REQ-836` | `FPW-024`/`MOD-047` | REC | `T3` reversed | commit | play resumes; record states the reversal | restriction persists | `integration` | SPECIFIED |
| `FPA-158` | A wrong correction is fixed by a further appended event | `REQ-820` | `FPW-024`/`COR-009` | REC | wrong `C` | correct again | chain references the wrong correction | chain rewritten | `auto` | SPECIFIED |
| `FPA-159` | A reversal never deletes the original record | `REQ-855` | `FPW-024`/`MOD-034` | SEC | reversal applied | inspect spine | original remains readable | deletion | `auto` | SPECIFIED |
| `FPA-160` | A state restoration is not a fresh grant | `REQ-861` | `FPW-024`/`COR-013` | NEG | post-failure restore | restore | `REVERSAL`/`CORRECTION` type | type `ORIGINAL` or `REWARD` | `auto` | SPECIFIED |
| `FPA-161` | Compensation requires a recorded finding of project error | `REQ-817` | `FPW-025`/`COR-014` | NEG | no finding | request | refused | discretionary goodwill payment | `manual` | SPECIFIED |
| `FPA-162` | Compensation never exceeds the proven loss | `REQ-817` | `FPW-025`/`F-FP-015` | BND | loss 50, cap 100 | compute | 50 | amount above loss | `auto` | SPECIFIED |
| `FPA-163` | An unapproved cap yields `PROVISIONAL_BLOCK` | `REQ-816` | `FPW-025`/`FP-P09` | OWN | `C_max` undefined | compute | blocked | a number invented | `auto` | SPECIFIED |
| `FPA-164` | Compensation never creates a negative balance | `REQ-817` | `FPW-025` | BND | cap above holdings | commit | floored and recorded | negative value | `auto` | SPECIFIED |
| `FPA-165` | A systemic schedule remains capped and recorded | `REQ-817` | `FPW-025` | INT | published schedule | batch pay | each payment capped | uncapped batch | `integration` | SPECIFIED |
| `FPA-166` | No sanction or compensation enriches the operator | `REQ-861` | `FPW-025`/`MOD-058` | SEC | any removal | commit | no value accrues to the project or a reporter | value retained | `auto` | SPECIFIED |
| `FPA-167` | Corrections apply in the recorded deterministic order | `REQ-820` | `FPW-026`/`F-FP-004` | INT | cases A and B | apply | A before B by `(turn, n, type_rank)` | arbitrary order | `auto` | SPECIFIED |
| `FPA-168` | A missing case turn holds rather than guesses | `REQ-820` | `FPW-026` | BND | `case_closed_turn` absent | order | `HOLD` | a guessed position | `auto` | SPECIFIED |
| `FPA-169` | Ties break on the original transaction id | `REQ-820` | `FPW-026` | BND | identical keys | order | deterministic tie-break | nondeterministic order | `auto` | SPECIFIED |
| `FPA-170` | A legal hold suspends application | `REQ-830` | `FPW-026`/`EVD-039` | OWN | hold in force | apply | suspended until released | applied under hold | `manual` | SPECIFIED |
| `FPA-171` | The conservation identity holds across all six types | `REQ-817` | `FPW-026`/`F-FP-014` | INT | mixed batch | reconcile | `Z = O + L + C + R + P + X + A` | any term omitted | `auto` | SPECIFIED |
| `FPA-172` | `ADMIN_ADJUSTMENT` is never hidden inside another term | `REQ-845` | `FPW-026`/`COR-001` | SEC | admin adjustment present | reconcile | appears as `A` | folded into `C` | `auto` | SPECIFIED |
| `FPA-173` | A non-zero residual fails the batch and raises an incident | `REQ-820` | `FPW-026`/`COR-017` | REC | residual ≠ 0 | reconcile | batch fails; incident opened | residual ignored | `integration` | SPECIFIED |
| `FPA-174` | Duplicate or conflicting corrections surface to a reviewer | `REQ-820` | `FPW-026`/`MOD-032` | INT | two overlapping | detect | surfaced, neither silently dropped | silent drop | `manual` | SPECIFIED |
| `FPA-175` | A compound cross-system reversal runs per owner at each boundary | `REQ-819` | `FPW-026`/`12A-OPEN-013` | INT | economy→market→alliance→event→ranking | reverse | each owner appends in recorded order; no closed turn reordered | one system rewriting all | `integration` | SPECIFIED |
| `FPA-176` | The reach of a compound reversal remains an owner question | `REQ-782` | `FPW-026`/`UD-052` | OWN | both-legs claim | execute | blocked branch executed | both sides applied | `manual` | SPECIFIED |

### 3.10 Register — Family F, appeals (`FPW-027`–`FPW-030`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-177` | Every action from `T1` upward is appealable once | `REQ-833` | `FPW-027`/`MOD-042` | POS | `T1` warning | file | accepted; second filing on same grounds barred | appeal refused | `auto` | SPECIFIED |
| `FPA-178` | `T0` has no appeal but accepts a factual correction request | `REQ-833` | `FPW-027` | BND | `T0` closure | request | correction route open; no appeal created | an appeal invented | `auto` | SPECIFIED |
| `FPA-179` | Grounds are limited to the five stated | `REQ-835` | `FPW-027`/`MOD-044` | NEG | "the rule is wrong" | file | routed as policy feedback, not an appeal | accepted as a ground | `manual` | SPECIFIED |
| `FPA-180` | The window is computed in turn boundaries | `REQ-833` | `FPW-027`/`F-FP-006` | BND | notice at 200, `W` set | compute | `t_close = 200 + W` | a date-based window | `auto` | SPECIFIED |
| `FPA-181` | An unapproved window yields `PROVISIONAL_BLOCK` | `REQ-816` | `FPW-027`/`FP-P06` | OWN | `W` undefined | enforce | blocked; the route still exists and is usable | an enforced invented window | `auto` | SPECIFIED |
| `FPA-182` | An outage extends the window by its turn count | `REQ-833` | `FPW-027`/`FR-10` | REC | outage of 3 turns | file late | accepted; no abandonment | filing rejected | `integration` | SPECIFIED |
| `FPA-183` | A correction dispute uses the same appeal track | `REQ-833` | `FPW-027`/`COR-008` | INT | correction applied | dispute | accepted once | no route for corrections | `auto` | SPECIFIED |
| `FPA-184` | An Alliance expulsion appeal is out of scope | `REQ-815` | `FPW-027`/`UD-044` | OWN | expulsion | file | referred with the dependency named | B-12 deciding | `manual` | SPECIFIED |
| `FPA-185` | The action stays in force pending decision | `REQ-833` | `FPW-028`/`MOD-043` | POS | appeal filed | inspect | still in force | automatic suspension of the action | `auto` | SPECIFIED |
| `FPA-186` | A granted hold does not decide the appeal | `REQ-833` | `FPW-028` | NEG | hold granted | inspect | case remains undecided | decision implied by relief | `auto` | SPECIFIED |
| `FPA-187` | A hold failure leaves the action in force | `REQ-776` | `FPW-028`/`FR-03` | REC | hold write error | retry | action stands; nothing partially relieved | silent relief | `integration` | SPECIFIED |
| `FPA-188` | Reversible hold is available only where reversible | `REQ-864` | `FPW-028` | BND | permanent measure | request hold | refused: permanence is not held away | irreversible pause | `auto` | SPECIFIED |
| `FPA-189` | Outcomes are exactly four | `REQ-833` | `FPW-029`/`MOD-045` | POS | any appeal | decide | one of the four, written and reasoned | a fifth outcome | `auto` | SPECIFIED |
| `FPA-190` | A remand names the defect and the reviewer | `REQ-833` | `FPW-029` | NEG | procedural defect | decide | both named | generic remand | `manual` | SPECIFIED |
| `FPA-191` | Independence is stated, and its absence is labelled | `REQ-837` | `FPW-029`/`MOD-049` | OWN | original reviewer decides | decide | "not independent" recorded and disclosed | a claim of independence | `manual` | SPECIFIED |
| `FPA-192` | An appeals reviewer never investigates the original case | `REQ-837` | `FPW-029`/`ADM-022` | SEC | reviewer tries to gather | act | denied | investigation permitted | `auto` | SPECIFIED |
| `FPA-193` | The appeal explanation is sufficient to contest | `REQ-835` | `FPW-029` | POS | decision issued | read | grounds answered without method detail | unusable reasoning | `manual` | SPECIFIED |
| `FPA-194` | Method, thresholds and third-party data are withheld | `REQ-835` | `FPW-029`/`MOD-018` | PRV | decision issued | read | none present | any leak | `auto` | SPECIFIED |
| `FPA-195` | An upheld appeal triggers reversal, correction and restitution | `REQ-836` | `FPW-029`/`FPW-024` | REC | `REVERSED` | commit | all three follow, each recorded | reversal without restitution | `integration` | SPECIFIED |
| `FPA-196` | A reduction does not merge conduct and correction | `REQ-817` | `FPW-029`/`MOD-055` | NEG | `REDUCED` | commit | two tracks remain separate | merged record | `auto` | SPECIFIED |
| `FPA-197` | An appeal against a senior moderator gets a second reviewer | `REQ-795` | `FPW-029`/`MOD-022` | SEC | senior moderator decided | file | routed away from that reviewer | same reviewer deciding | `manual` | SPECIFIED |
| `FPA-198` | The independence guarantee that exists is stated | `REQ-837` | `FPW-029`/`ADM-013` | OWN | single operator | inspect design | the label and substitute, never a claim | a promised guarantee | `manual` | SPECIFIED |
| `FPA-199` | Reopening requires new evidence or a defect | `REQ-834` | `FPW-030`/`MOD-046` | NEG | same grounds | resubmit | closed without re-investigation | reopened | `auto` | SPECIFIED |
| `FPA-200` | Genuinely new evidence reopens with its own record | `REQ-834` | `FPW-030` | REC | new server record | resubmit | reopened as a new decision | ignored evidence | `manual` | SPECIFIED |
| `FPA-201` | A repeat appeal never changes any tier by itself | `REQ-834` | `FPW-030` | BND | three filings | inspect | tier unchanged | escalation by persistence | `auto` | SPECIFIED |
| `FPA-202` | Every closure of a repeat appeal is recorded | `REQ-834` | `FPW-030` | POS | closure | commit | event written | silent closure | `auto` | SPECIFIED |

### 3.11 Register — Family G, emergency and incident (`FPW-031`–`FPW-034`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-203` | Emergency power may only suspend, freeze or withhold | `REQ-848` | `FPW-031`/`MOD-025` | SEC | incident open | attempt a delete or transfer | refused | any irreversible effect | `auto` | SPECIFIED |
| `FPA-204` | An emergency action with no recording path does not execute | `REQ-847` | `FPW-031`/`FR-11` | REC | spine unavailable | invoke | nothing happens | silent action | `integration` | SPECIFIED |
| `FPA-205` | Only the named emergency role may invoke | `REQ-847` | `FPW-031`/`ADM-015` | SEC | `R-MOD` attempts | invoke | denied | any role invoking | `auto` | SPECIFIED |
| `FPA-206` | Invocation states incident, scope, expiry and review owner | `REQ-847` | `FPW-031` | POS | invoking | record | all four present | any missing | `auto` | SPECIFIED |
| `FPA-207` | Emergency privilege excludes the prohibition list | `REQ-848` | `FPW-031`/`ADM-014` | SEC | emergency active | attempt a balance edit | refused | privilege expanding scope | `auto` | SPECIFIED |
| `FPA-208` | An unapproved emergency duration blocks, not continues | `REQ-847` | `FPW-031`/`F-FP-016` | OWN | `D_e` undefined | invoke | `PROVISIONAL_BLOCK` | an indefinite measure | `auto` | SPECIFIED |
| `FPA-209` | Players are told a measure is in force and when it is reviewed | `REQ-850` | `FPW-031`/`MOD-027` | PRV | measure active | boundary | generic notice with review time, no threat detail | silent restriction | `manual` | SPECIFIED |
| `FPA-210` | No emergency action may bypass the appeal route | `REQ-848` | `FPW-031`/`ADM-027` | POS | measure applied | appeal | route available | route blocked | `auto` | SPECIFIED |
| `FPA-211` | Measures expire automatically at their boundary | `REQ-847` | `FPW-032`/`F-FP-016` | BND | expiry reached | resume | expired without an operator act | persistence | `integration` | SPECIFIED |
| `FPA-212` | Extension is a new bounded decision | `REQ-847` | `FPW-032`/`MOD-026` | POS | extension sought | decide | new reason, new review, new bound | rolling without decision | `manual` | SPECIFIED |
| `FPA-213` | Every emergency action gets a retrospective review | `REQ-849` | `FPW-032`/`MOD-028` | OWN | action taken | review window | review recorded whether or not reversed | unreviewed action | `manual` | SPECIFIED |
| `FPA-214` | The reviewer is not the author where staffing permits | `REQ-849` | `FPW-032` | SEC | author only available | review | labelled and disclosed | claimed independence | `manual` | SPECIFIED |
| `FPA-215` | An expired measure is not deleted from the record | `REQ-855` | `FPW-032`/`MOD-034` | SEC | measure expired | inspect | record remains | erasure | `auto` | SPECIFIED |
| `FPA-216` | A missed review becomes an incident record | `REQ-862` | `FPW-032`/`FR-15` | REC | review not done | boundary | incident opened | back-dated review | `auto` | SPECIFIED |
| `FPA-217` | Incidents are classified before a posture is chosen | `REQ-856` | `FPW-033`/`SEC-024` | POS | event observed | classify | one of five classes with posture, authority, disclosure owner, preservation | posture before class | `manual` | SPECIFIED |
| `FPA-218` | No global fail-open or fail-closed rule appears | `REQ-862` | `FPW-033`/`SEC-022` | SEC | any design claim | inspect corpus | per-category postures only | a universal statement | `auto` | SPECIFIED |
| `FPA-219` | An integrity failure is an incident, not a conduct case | `REQ-856` | `FPW-033`/`INT-013` | INT | turn fault | classify | incident opened; no person charged | conduct case opened | `integration` | SPECIFIED |
| `FPA-220` | Manipulation evidenced during a fault converts the lane | `REQ-856` | `FPW-033` | INT | fault plus false agency | classify | both lanes run, recorded separately | one lane swallowing the other | `manual` | SPECIFIED |
| `FPA-221` | A suspected integrity failure halts and discloses a delay | `REQ-858` | `FPW-033`/`SEC-026` | REC | integrity doubtful | resolve | halted; players see a delay | continuing doubtfully | `integration` | SPECIFIED |
| `FPA-222` | Recovery never re-executes a committed action | `REQ-770` | `FPW-033`/`SEC-010` | REC | restore | replay | forward-only or last committed | re-execution | `integration` | SPECIFIED |
| `FPA-223` | A first honest exploit report is an incident, not a violation | `REQ-814` | `FPW-033`/`FP-027` | POS | reporter discloses before gain | triage | incident lane; no conduct record | reporter charged | `manual` | SPECIFIED |
| `FPA-224` | Continued use after a fix is a conduct matter | `REQ-814` | `FPW-033`/`FP-027` | NEG | use after fix | triage | conduct lane opens | immunity from the first report | `manual` | SPECIFIED |
| `FPA-225` | Duplicate enforcement from one incident coalesces | `REQ-820` | `FPW-033`/`MOD-032` | INT | two actions issued | commit | first committed stands; conflict flagged | two effects | `integration` | SPECIFIED |
| `FPA-226` | Every failure affecting integrity, privacy or enforcement is reviewed | `REQ-862` | `FPW-033`/`FR-15` | REC | no outcome change | review | review still recorded | unreviewed failure | `auto` | SPECIFIED |
| `FPA-227` | A suspected data breach is assessed whether or not reported | `REQ-857` | `FPW-034`/`SEC-025` | PRV | exposure suspected | assess | documented assessment including non-reporting reasons | undocumented | `manual` | SPECIFIED |
| `FPA-228` | The assessment is an artefact, not a legal conclusion | `REQ-869` | `FPW-034` | OWN | assessment | read | no compliance claim present | a legal claim | `manual` | SPECIFIED |
| `FPA-229` | Exposure is preserved, assessed and documented before disclosure | `REQ-857` | `FPW-034`/`EVD-021` | REC | breach found | sequence | that order, each recorded | disclosure before assessment | `manual` | SPECIFIED |
| `FPA-230` | Inter-player exposure is withheld at publication, not after | `REQ-802` | `FPW-034`/`PRV-018` | PRV | leak candidate | publish step | withheld at the gate | published then retracted | `integration` | SPECIFIED |
| `FPA-231` | The legal dependency is named with its owner | `REQ-869` | `FPW-034`/`UD-017` | OWN | obligation unclear | assess | dependency and conservative branch stated | an assumed jurisdiction answer | `manual` | SPECIFIED |
| `FPA-232` | No credential or secret enters the assessment | `REQ-774` | `FPW-034`/`SEC-027` | SEC | artefacts gathered | assess | identifiers and references only | any secret present | `auto` | SPECIFIED |

### 3.12 Register — Family H, privacy and information handling (`FPW-035`–`FPW-038`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-233` | Every field has exactly one value on each of three axes | `REQ-798` | `FPW-035`/`PRV-001` | POS | inventoried field | classify | one handling, one visibility, one purpose value | two values on one axis | `manual` | SPECIFIED |
| `FPA-234` | Existing class assignments are reconciled, not reassigned | `REQ-799` | `FPW-035`/`PRV-003` | INT | owning register differs | reconcile | change lands in the owning register with a dated decision | silent overwrite here | `manual` | SPECIFIED |
| `FPA-235` | Exactly nine access classes exist | `REQ-798` | `FPW-035`/`PRV-002` | BND | any field | classify | value from the nine | a tenth class | `auto` | SPECIFIED |
| `FPA-236` | No personal, moderation, security or audit field is public | `REQ-774` | `FPW-035`/`PRV-008` | PRV | candidate field | classify | `PUB` refused | any such field public | `auto` | SPECIFIED |
| `FPA-237` | A class change is versioned with the field | `REQ-799` | `FPW-035`/`PRV-017` | POS | class changed | deploy | dated decision recorded; history keeps its class | change as a deployment side effect | `manual` | SPECIFIED |
| `FPA-238` | Historical records keep the class they were created under | `REQ-855` | `FPW-035`/`PRV-017` | REC | class reissued | read history | prior class applies | retroactive reclassification | `auto` | SPECIFIED |
| `FPA-239` | A restricted read without a stated purpose is denied | `REQ-800` | `FPW-036`/`PRV-004` | SEC | purpose absent | read | denied | read granted | `auto` | SPECIFIED |
| `FPA-240` | Every privileged read writes an audit event with actor, purpose, target, time | `REQ-841` | `FPW-036`/`ADM-008` | SEC | restricted record read | complete | event exists even though nothing changed | silent read | `integration` | SPECIFIED |
| `FPA-241` | Viewing implies neither search, export, modify, delete nor disclose | `REQ-801` | `FPW-036`/`PRV-006` | SEC | view-only role | attempt each action | only view succeeds | implication leaks | `integration` | SPECIFIED |
| `FPA-242` | Cross-class flows are declared separately from read permission | `REQ-801` | `FPW-036`/`PRV-004` | INT | flow not declared | attempt | blocked | flow inferred from permission | `auto` | SPECIFIED |
| `FPA-243` | A failed restricted read returns no data | `REQ-776` | `FPW-036`/`FR-14` | REC | read path fails | attempt | empty, never a broader cache | unfiltered fallback | `integration` | SPECIFIED |
| `FPA-244` | A diplomatic full-history read is audited and class-bound | `REQ-841` | `FPW-036`/`INT-007` | INT | `DIP-121` read | perform | event with purpose | unaudited read | `integration` | SPECIFIED |
| `FPA-245` | Alliance finance reads are scoped, minimised and logged | `REQ-802` | `FPW-036`/`INT-008` | PRV | tax or contribution read | perform | minimised fields, purpose, event | leak through tooling | `integration` | SPECIFIED |
| `FPA-246` | An authorisation outage never falls back to a lower assurance | `REQ-769` | `FPW-036`/`FR-02` | SEC | authorization unavailable | attempt | denied | permissive default | `integration` | SPECIFIED |
| `FPA-247` | A response contains only entitled fields | `REQ-774` | `FPW-037`/`FP-015` | PRV | mixed-class payload | render | non-entitled fields absent from the wire | sent then filtered | `integration` | SPECIFIED |
| `FPA-248` | Hiding a field in the client is never treated as control | `REQ-774` | `FPW-037`/`SEC-012` | SEC | client-side hide | test wire | value absent server-side | value present, hidden | `auto` | SPECIFIED |
| `FPA-249` | A failure message names the condition and nothing else | `REQ-804` | `FPW-037`/`PRV-020` | PRV | any rejection | render | no rule, threshold, third-party data or existence disclosure | leakage in error text | `manual` | SPECIFIED |
| `FPA-250` | A server-created leak is a defect, not a player violation | `REQ-815` | `FPW-037`/`FP-029` | NEG | field wrongly sent | assess | defect opened; no `V-13` charge | player charged | `manual` | SPECIFIED |
| `FPA-251` | Reconstruction from response differences is `V-13` | `REQ-796` | `FPW-037`/`EX-007` | SEC | differencing observed | assess | charge available with evidence | no route | `integration` | SPECIFIED |
| `FPA-252` | Public aggregate at `k ≥ 5` is not a violation | `REQ-802` | `FPW-037`/`EX-007` | NEG | aggregate read | assess | no charge | charge on public data | `auto` | SPECIFIED |
| `FPA-253` | Every published aggregate names its quasi-identifiers | `REQ-802` | `FPW-038`/`PRV-018` | POS | aggregate candidate | publish | QI list, inference argument, k value present | bare figure | `manual` | SPECIFIED |
| `FPA-254` | Denominators below five are withheld, never released | `REQ-802` | `FPW-038` | BND | k = 4 | publish | withheld or coarsened | released | `integration` | SPECIFIED |
| `FPA-255` | A figure that singles out a nation is withheld | `REQ-802` | `FPW-038` | PRV | identifiable output | publish | withheld | published | `auto` | SPECIFIED |
| `FPA-256` | Stable merging and complementary suppression are applied | `REQ-802` | `FPW-038`/`WEP-659` | INT | two adjacent cells | publish | suppression prevents re-identification | differencing possible | `integration` | SPECIFIED |
| `FPA-257` | No small-group or sensitive exception is invented | `REQ-802` | `FPW-038`/`WEP-649` | SEC | exception proposed | publish | refused; escalated as an owner or Prompt 12 question | exception adopted | `auto` | SPECIFIED |
| `FPA-258` | A nation's own rank is not treated as an aggregate | `REQ-802` | `FPW-038`/`WEP-660` | BND | own-rank view | render | visible to the owner | suppressed own data | `auto` | SPECIFIED |
| `FPA-259` | Publication withholds on pipeline failure rather than guessing | `REQ-863` | `FPW-038`/`FR-08` | REC | pipeline incomplete | publish | figure withheld | partial figure | `integration` | SPECIFIED |
| `FPA-260` | A derived identifier is labelled pseudonymous with an assessment | `REQ-806` | `FPW-038`/`PRV-024` | PRV | keyed digest created | label | label plus identifiability note | "anonymous" wording | `manual` | SPECIFIED |
| `FPA-261` | Notice content is bounded before it reaches a surface | `REQ-803` | `FPW-039`/`INT-012` | PRV | any notice | render | no third-party enforcement state | state leaked | `integration` | SPECIFIED |
| `FPA-262` | Every restriction surface publishes its appeal route | `REQ-803` | `FPW-039`/`12A-INT-24` | POS | restriction shown | render | route present | route absent | `manual` | SPECIFIED |
| `FPA-263` | No badge, ranking note or chronicle entry carries enforcement status | `REQ-803` | `FPW-039`/`PRV-019` | PRV | standings rendered | inspect | nothing indicating a case | status shown | `integration` | SPECIFIED |
| `FPA-264` | Notification delivery is never assumed to be public information | `REQ-803` | `FPW-039`/`PRV-012` | PRV | notice queued | deliver | class bounds respected | over-disclosure | `auto` | SPECIFIED |
| `FPA-265` | Public rules and hidden detectors coexist without contradiction | `REQ-791` | `FPW-039`/`FP-033` | POS | published text | review | prohibited effect and appeal route published; methods absent | method published | `manual` | SPECIFIED |
| `FPA-266` | Delayed disclosure always records the delay and its review | `REQ-821` | `FPW-039`/`MOD-030` | REC | delay applied | inspect | both recorded | unrecorded delay | `auto` | SPECIFIED |
| `FPA-267` | Export needs a separate permission and a recorded purpose | `REQ-831` | `FPW-040`/`PRV-021` | PRV | view-only moderator | export | denied | export allowed | `integration` | SPECIFIED |
| `FPA-268` | A failed export produces no partial or unredacted file | `REQ-776` | `FPW-040`/`FR-15` | REC | export fails | retry | no artefact on disk | partial file | `integration` | SPECIFIED |
| `FPA-269` | A data-subject request is served only to the subject | `REQ-780` | `FPW-040`/`PRV-013` | PRV | request authenticated | serve | own data only | third-party data | `manual` | SPECIFIED |
| `FPA-270` | Disclosure under legal obligation records its authority | `REQ-830` | `FPW-040`/`PRV-016` | OWN | obligation asserted | disclose | authority, scope and event recorded | undisclosed disclosure | `manual` | SPECIFIED |
| `FPA-271` | Deletion is a separate permission and a recorded event | `REQ-830` | `FPW-040`/`PRV-022` | SEC | delete attempted | act | permission plus event | silent removal | `auto` | SPECIFIED |
| `FPA-272` | No actor holds export, delete or disclose by default | `REQ-846` | `FPW-040`/`Annex B` | SEC | any role | inspect matrix | only the audit role for `AUDIT` export | a default right | `auto` | SPECIFIED |
| `FPA-273` | Retention is stated per class with a justification | `REQ-808` | `FPW-041`/`PRV-023` | OWN | any class | inspect | justification plus review trigger | bare number | `manual` | SPECIFIED |
| `FPA-274` | No new day-count is introduced by 12C | `REQ-808` | `FPW-041` | OWN | corpus scan | audit | only existing values (`TR-092`, `MKT-162`) appear | a new period | `auto` | SPECIFIED |
| `FPA-275` | The erasure-versus-spine conflict is recorded with both duties | `REQ-809` | `FPW-041`/`UD-055` | OWN | clash detected | register | both obligations plus the conservative branch | one duty dropped | `manual` | SPECIFIED |
| `FPA-276` | Redaction preserves the fact, the authority and a reference | `REQ-830` | `FPW-041`/`EVD-038` | PRV | obligation met | redact | all three present | silent redaction | `auto` | SPECIFIED |
| `FPA-277` | A legal hold suspends deletion for named records only | `REQ-831` | `FPW-041`/`EVD-039` | OWN | hold issued | retention run | named records exempt; others proceed | blanket suspension | `integration` | SPECIFIED |
| `FPA-278` | Hold authority and scope are never invented | `REQ-869` | `FPW-041` | OWN | hold proposed | record | `UD-017`/`UD-055` named | a period asserted | `manual` | SPECIFIED |
| `FPA-279` | Spine rows are never sampled away | `REQ-853` | `FPW-041`/`EVD-034` | SEC | quota pressure | tier | spine rows retained; priority classes first | any spine row dropped | `auto` | SPECIFIED |
| `FPA-280` | Class-O evidence cannot be deleted for a live case | `REQ-831` | `FPW-041`/`TR-090` | INT | case open | retention run | preserved while needed | premature deletion | `integration` | SPECIFIED |
| `FPA-281` | Evidence never appears in operational analytics | `REQ-831` | `FPW-041`/`EVD-024` | PRV | analytics build | inspect | no evidence copy path | copy present | `integration` | SPECIFIED |
| `FPA-282` | A deletion event keeps its authority visible to the audit role | `REQ-855` | `FPW-041`/`EVD-029` | SEC | deletion done | audit read | authority and surviving reference visible | untraceable removal | `auto` | SPECIFIED |
| `FPA-283` | Only named capabilities can be granted | `REQ-839` | `FPW-042`/`ADM-018` | SEC | unnamed capability | grant | refused | a wildcard grant | `auto` | SPECIFIED |
| `FPA-284` | No role inherits a permission it does not hold | `REQ-838` | `FPW-042`/`ADM-006` | SEC | escalation attempt | delegate | refused | escalation by grant | `auto` | SPECIFIED |
| `FPA-285` | Delegation is case-, purpose- and time-bounded | `REQ-846` | `FPW-042`/`ADM-028` | BND | delegation issued | inspect | all three bounds recorded | open-ended delegation | `auto` | SPECIFIED |
| `FPA-286` | Revocation is immediate and recorded | `REQ-840` | `FPW-042`/`ADM-016` | REC | conflict declared | revoke | effective immediately with an event | delayed revocation | `integration` | SPECIFIED |
| `FPA-287` | Read access is narrower than write and never implies export | `REQ-838` | `FPW-042`/`ADM-005` | PRV | any role | inspect | no implied export | implied breadth | `auto` | SPECIFIED |
| `FPA-288` | The prohibition list is enforced at grant time | `REQ-838` | `FPW-042`/`ADM-001` | SEC | treasury-edit capability | grant | refused | grant allowed | `auto` | SPECIFIED |
| `FPA-289` | A purpose-outside-scope action is `V-16` | `REQ-846` | `FPW-042`/`ADM-019` | SEC | permitted act, wrong purpose | act | chargeable as `V-16` | treated as harmless | `manual` | SPECIFIED |
| `FPA-290` | No administrative action escapes the spine | `REQ-829` | `FPW-042`/`ADM-020` | SEC | any act | commit | event exists | covert act | `auto` | SPECIFIED |
| `FPA-291` | Privileged action requires a distinct step-up session | `REQ-840` | `FPW-043`/`ADM-007` | SEC | ordinary session | privileged act | denied until step-up | allowed on play credentials | `integration` | SPECIFIED |
| `FPA-292` | A privileged session is shorter, separately logged, independently revocable | `REQ-840` | `FPW-043` | SEC | session open | inspect | three properties present | shared long session | `integration` | SPECIFIED |
| `FPA-293` | Self-dealing is blocked or disclosed with review | `REQ-842` | `FPW-043`/`ADM-009` | SEC | actor targets own nation | act | blocked where approval exists; otherwise recorded, disclosed, reviewed | silent self-action | `manual` | SPECIFIED |
| `FPA-294` | Investigation and decision are separate permissions | `REQ-843` | `FPW-043`/`ADM-010` | OWN | one person holds both | decide | `unsegregated` label plus review | unlabelled fusion | `manual` | SPECIFIED |
| `FPA-295` | Author and publisher of enforcement configuration are separated | `REQ-844` | `FPW-043`/`ADM-011` | OWN | one person authors | publish | second publisher or recorded disclosure and review | sole silent publication | `manual` | SPECIFIED |
| `FPA-296` | An impossible separation is declared with its substitute | `REQ-846` | `FPW-043`/`ADM-013` | OWN | single operator | inspect | gap plus compensating control | described as separated | `manual` | SPECIFIED |
| `FPA-297` | A compromised privileged session halts privileged paths | `REQ-862` | `FPW-043`/`FPW-033` | REC | compromise suspected | contain | privileged paths halted; world continues | global outage or no action | `integration` | SPECIFIED |
| `FPA-298` | Authentication failure never falls back to a shared operator credential | `REQ-776` | `FPW-043`/`FR-12` | SEC | auth error | retry | denied; no fallback identity | fallback used | `integration` | SPECIFIED |
| `FPA-299` | Financial correction is executed by the ledger, not typed | `REQ-845` | `FPW-043`/`ADM-012` | SEC | admin tries a balance | act | refused; routed to `FPW-021` | balance accepted | `integration` | SPECIFIED |
| `FPA-300` | A security administrator never edits game value or audit history | `REQ-846` | `FPW-043`/`ADM-024` | SEC | `R-SEC` acts | attempt | refused for value and history | either permitted | `auto` | SPECIFIED |
| `FPA-301` | The audit event set covers all named domains | `REQ-851` | `FPW-044`/`EVD-026` | POS | ten domains | enumerate | each maps to an event class | any domain uncovered | `auto` | SPECIFIED |
| `FPA-302` | Each event class has the full defined shape | `REQ-852` | `FPW-044`/`EVD-027` | POS | event emitted | inspect | ten fields present, owned by B-12 and consumed by B-02 | missing field | `auto` | SPECIFIED |
| `FPA-303` | No audit row contains content bodies, secrets or credentials | `REQ-852` | `FPW-044`/`EVD-028` | SEC | any event | inspect | identifiers, decisions, reasons only | a body or secret | `auto` | SPECIFIED |
| `FPA-304` | An audit write failure fails the whole transaction | `REQ-776` | `FPW-044`/`FR-03` | REC | spine unavailable | commit | nothing committed | effect without record | `integration` | SPECIFIED |
| `FPA-305` | Corrections reference the original event | `REQ-855` | `FPW-044`/`EVD-029` | POS | correction appended | inspect | reference present | orphan correction | `auto` | SPECIFIED |
| `FPA-306` | Spine readership is a published, purpose-granted register | `REQ-854` | `FPW-044`/`EVD-033` | PRV | reader request | grant | purpose recorded | unregistered reader | `manual` | SPECIFIED |
| `FPA-307` | The audit role may verify but never rewrite | `REQ-854` | `FPW-044`/`ADM-026` | SEC | `R-AUD` acts | attempt edit | refused | any rewrite permitted | `auto` | SPECIFIED |
| `FPA-308` | Volume tiering keeps enforcement rows first | `REQ-853` | `FPW-044`/`EVD-034` | BND | quota pressure | tier | value, pipeline, privileged and enforcement retained | enforcement sampled | `auto` | SPECIFIED |
| `FPA-309` | Each digest covers the record fields and the previous digest | `REQ-829` | `FPW-045`/`F-FP-012` | SEC | chain built | verify | construction matches `F-FP-012` | fields uncovered | `integration` | **BLOCKED** — no implementation exists |
| `FPA-310` | No secret is stored inside a spine row | `REQ-829` | `FPW-045`/`EVD-031` | SEC | row written | inspect | no key material | secret in row | `integration` | **BLOCKED** |
| `FPA-311` | A missing record produces `CHAIN_BREAK` | `REQ-829` | `FPW-045` | NEG | link absent | verify | break reported, never skipped | silent skip | `integration` | **BLOCKED** |
| `FPA-312` | Verification runs from the last verified checkpoint | `REQ-829` | `FPW-045`/`EVD-032` | REC | checkpoint exists | run | resumes correctly | full rescan assumed | `integration` | **BLOCKED** |
| `FPA-313` | A break escalates as an incident | `REQ-858` | `FPW-045`/`EVD-032` | REC | mismatch found | run | incident opened, publication halted | routine note | `integration` | **BLOCKED** |
| `FPA-314` | A missed interval raises an incident at the next boundary | `REQ-862` | `FPW-045`/`F-FP-013` | BND | `I_v` passed | boundary | incident opened | interval unnoticed | `integration` | **BLOCKED** |
| `FPA-315` | An unapproved interval blocks rather than defaults | `REQ-816` | `FPW-045`/`FP-P08` | OWN | `I_v` undefined | schedule | `PROVISIONAL_BLOCK` | a default cadence | `auto` | SPECIFIED |
| `FPA-316` | A correction appends and never recomputes an old digest | `REQ-855` | `FPW-045`/`EVD-029` | SEC | correction added | verify | earlier digests unchanged | recomputation | `integration` | **BLOCKED** |
| `FPA-317` | No document claims the trail is tamper-proof or verified | `REQ-866` | `FPW-045`/`EVD-042` | PRV | corpus | scan | the claim is absent everywhere | any such claim | `auto` | SPECIFIED |
| `FPA-318` | A gate may claim audit integrity only from an executed run | `REQ-829` | `FPW-045`/`SEC-039` | SEC | run exists | grade | gate may move only then | document-based claim | `manual` | **BLOCKED** |
| `FPA-319` | Spine update and delete are prevented outside the correction path | `REQ-855` | `FPW-046`/`SEC-037` | SEC | update attempt | act | refused and recorded | any silent update | `integration` | **BLOCKED** — no protective trigger exists |
| `FPA-320` | The spine is protected from the service role's ordinary path where possible | `REQ-829` | `FPW-046`/`SEC-037` | SEC | service-role write | act | refused or the platform limit is disclosed | unexamined bypass | `integration` | **BLOCKED** — `12A-OPEN-015` unresolved |
| `FPA-321` | Every attempted spine violation is recorded | `REQ-828` | `FPW-046`/`SEC-037` | SEC | denied act | inspect | attempt recorded | attempt lost | `auto` | SPECIFIED |
| `FPA-322` | An audit correction is an appended event, never an edit | `REQ-855` | `FPW-046`/`EVD-029` | POS | wrong row | correct | appended, original retained | in-place edit | `auto` | SPECIFIED |
| `FPA-323` | Audit reads are purpose-bound, registered and logged | `REQ-854` | `FPW-046`/`PRV-015` | PRV | any read | perform | all three hold | unlogged read | `integration` | SPECIFIED |
| `FPA-324` | Obligation deletion records its authority | `REQ-855` | `FPW-046`/`EVD-029` | OWN | deletion under duty | perform | event plus authority recorded | unattributed deletion | `manual` | SPECIFIED |

### 3.13 Register — Family L, cross-system handoffs (`FPW-047`–`FPW-051`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-325` | A market signal opens review and never a sanction | `REQ-786` | `FPW-047`/`INT-006` | INT | any `MKT-S` | receive | review object; no market state change | signal treated as a finding | `integration` | SPECIFIED |
| `FPA-326` | `MKT-S10` conservation failure is treated as a defect | `REQ-819` | `FPW-047`/`FPW-033` | REC | pair fails identity | receive | incident, not a conduct case | player charged | `integration` | SPECIFIED |
| `FPA-327` | A market ban is expressed as an account measure | `REQ-859` | `FPW-047`/`MKT-218` | INT | ban proposed | decide | applied through `FPW-016`, not a market edit | market state rewritten | `integration` | SPECIFIED |
| `FPA-328` | No market-side trust score or fourth status is created | `REQ-861` | `FPW-047`/`MKT-182` | SEC | score suggested | design review | absent from every 12C artefact | a score introduced | `auto` | SPECIFIED |
| `FPA-329` | Price alone never proves manipulation | `REQ-784` | `FPW-047`/`MKT-155` | NEG | out-of-band trade | assess | review only; neutral confirmation | immediate sanction | `manual` | SPECIFIED |
| `FPA-330` | Matched opposite-side flows need a second source | `REQ-767` | `FPW-047`/`CO-003` | NEG | pattern observed | assess | `E1` until corroborated | `E3` on pattern | `auto` | SPECIFIED |
| `FPA-331` | Listing suspension stays B-07's own power | `REQ-815` | `FPW-047`/`MKT-089` | INT | reposting pattern | act | B-07 suspends the listing; B-12 the account | B-12 suspending a listing | `integration` | SPECIFIED |
| `FPA-332` | Volume dominance is not a violation | `REQ-784` | `FPW-047`/`CO-002` | BND | `MKT-S08` fired | assess | review object; no charge by itself | share treated as offence | `manual` | SPECIFIED |
| `FPA-333` | The G-1 band is supplied structurally with no number | `REQ-789` | `FPW-047`/`INT-006` | OWN | gate assessment | propose | shape plus owner plus Prompt 14 dependency | a value asserted as met | `manual` | SPECIFIED |
| `FPA-334` | A document is never treated as gate evidence for G-1 | `REQ-866` | `FPW-047`/`MKT-074` | SEC | gate review | grade | G-1 stays not met | gate marked met | `manual` | SPECIFIED |
| `FPA-335` | A disputed breach produces a new event, never an edit | `REQ-819` | `FPW-048`/`INT-007` | INT | dispute upheld | correct | append referencing the original | in-place edit | `integration` | SPECIFIED |
| `FPA-336` | A full diplomatic-history read is audited | `REQ-841` | `FPW-048`/`DIP-121` | SEC | reviewer reads | perform | purpose and event recorded | unaudited read | `integration` | SPECIFIED |
| `FPA-337` | A breach count is cited as evidence, never as reputation | `REQ-860` | `FPW-048`/`DIP-085` | NEG | count used | decide | judgement language absent | count treated as a score | `manual` | SPECIFIED |
| `FPA-338` | B-08 never reads B-12 records as a reputation input | `REQ-861` | `FPW-048`/`DIP-089` | SEC | enforcement record | integrate | no read path defined | record consumed | `auto` | SPECIFIED |
| `FPA-339` | Each party's own published reason stays a party act | `REQ-803` | `FPW-048`/`DIP-078` | PRV | statement published | render | B-12 discloses nothing further | status inferred from text | `auto` | SPECIFIED |
| `FPA-340` | The `DPE-049` and `DPE-054` rows remain PARTIAL | `REQ-866` | `FPW-048`/`11C` | OWN | specification complete | grade | no 08C row is marked closed | claiming closure | `manual` | SPECIFIED |
| `FPA-341` | An officer cannot suspend an account | `REQ-815` | `FPW-049`/`ALL-158` | INT | officer attempts | act | refused; platform path explained | officer power granted | `integration` | SPECIFIED |
| `FPA-342` | Alliance conduct reports follow the platform evidence path | `REQ-822` | `FPW-049`/`ALL-158` | INT | content report | submit | one case in B-12 | parallel alliance queue | `integration` | SPECIFIED |
| `FPA-343` | Alliance-scale similarity is a false-positive class | `REQ-788` | `FPW-049`/`CO-002` | NEG | pattern observed | assess | recorded as FP class | evidence treated | `manual` | SPECIFIED |
| `FPA-344` | Cooperation between members is not collusion | `REQ-784` | `FPW-049`/`CO-002` | POS | coordinated defence | assess | dismissed absent false agency | charge raised | `manual` | SPECIFIED |
| `FPA-345` | A container transfer passes the same economy checks | `REQ-786` | `FPW-049`/`ALL-159` | INT | transfer in/out | screen | attribution preserved | attribution lost | `integration` | SPECIFIED |
| `FPA-346` | A restricted flow through tax is charged as `V-11` | `REQ-781` | `FPW-049`/`CO-008` | POS | routed transfer | assess | class named with evidence | unclassified charge | `manual` | SPECIFIED |
| `FPA-347` | Alliance treasury authority is not assumed | `REQ-861` | `FPW-049`/`UD-046` | OWN | financial effect sought | decide | no effect through the container | an assumed capability | `auto` | SPECIFIED |
| `FPA-348` | Expulsion disputes are referred, not adjudicated | `REQ-815` | `FPW-049`/`UD-044` | OWN | expulsion appeal | receive | referred with the dependency | B-12 deciding | `manual` | SPECIFIED |
| `FPA-349` | Aggregate Alliance reads satisfy `k ≥ 5` | `REQ-802` | `FPW-049`/`INT-008` | PRV | counts requested | read | aggregate-safe only | member-level leak | `integration` | SPECIFIED |
| `FPA-350` | No Alliance is sanctioned as a body | `REQ-784` | `FPW-049`/`CO-010` | NEG | group misconduct alleged | decide | only evidenced accounts act | collective sanction | `auto` | SPECIFIED |
| `FPA-351` | A block record is evidence, never a sanction | `REQ-766` | `FPW-050`/`WAR-028` | INT | `WRA-02` written | receive | review object only | block read as penalty | `integration` | SPECIFIED |
| `FPA-352` | No battle or campaign result is recomputed | `REQ-815` | `FPW-050`/`INT-009` | SEC | disputed result | assess | taxonomy consumed; result stands | recomputation | `integration` | SPECIFIED |
| `FPA-353` | An in-place edit of a committed battle record is rejected | `REQ-819` | `FPW-050`/`TR-091` | SEC | edit attempted | commit | refused; recorded reversal only | edit accepted | `integration` | SPECIFIED |
| `FPA-354` | Slot-filling patterns are charged under `V-10` | `REQ-781` | `FPW-050`/`CO-007` | POS | filled slots | assess | class named with the effect test | no route to a charge | `manual` | SPECIFIED |
| `FPA-355` | `AUD-AL-017` stays restricted with a redacted view | `REQ-803` | `FPW-050`/`WAR-154` | PRV | reviewer reads | perform | redacted actor fields | full disclosure | `integration` | SPECIFIED |
| `FPA-356` | No warfare failure code is invented | `REQ-860` | `FPW-050`/`D-143` | SEC | code needed | design | only defined codes referenced | `WRF-15`–`19` used | `auto` | SPECIFIED |
| `FPA-357` | An evidence hold is enacted by B-11 on B-12's request | `REQ-815` | `FPW-050`/`WEP-655` | INT | manipulation flagged | hold | `SUSPENDED`/`EXCLUDED` with evidence id | B-11 punishing | `integration` | SPECIFIED |
| `FPA-358` | A held grant loses nothing permanently | `REQ-861` | `FPW-050`/`WEP-371` | POS | hold applied | inspect standings | presentation only; no loss | silent loss | `integration` | SPECIFIED |
| `FPA-359` | A grant without supporting evidence is invalid | `REQ-786` | `FPW-050`/`WEE-081` | NEG | no evidence | grant attempt | refused and corrected | grant stands | `auto` | SPECIFIED |
| `FPA-360` | No reward is granted or removed by B-12 | `REQ-861` | `FPW-050`/`INT-010` | SEC | reward dispute | act | B-11 executes under its rule | B-12 granting | `auto` | SPECIFIED |
| `FPA-361` | A corrected standing is a new sealed snapshot | `REQ-803` | `FPW-051`/`WEP-383` | INT | error proven | correct | `corrects_snapshot_id` links the pair | original rewritten | `integration` | SPECIFIED |
| `FPA-362` | Deletion of a historical standing is invalid | `REQ-855` | `FPW-051`/`WEP-583` | SEC | deletion requested | act | refused; `REDACTED` route only | deletion | `auto` | SPECIFIED |
| `FPA-363` | A formula change never rewrites a sealed snapshot | `REQ-772` | `FPW-051`/`WEP-593` | BND | formula updated | recompute | sealed values unchanged | retroactive rewrite | `integration` | SPECIFIED |
| `FPA-364` | No player sees a mid-turn rank | `REQ-774` | `FPW-051`/`WEP-384` | PRV | turn in progress | render | publication boundary respected | mid-turn value | `integration` | SPECIFIED |
| `FPA-365` | Pre-snapshot inflation is charged, the seal is not moved | `REQ-786` | `FPW-051`/`INT-011` | INT | spike detected | assess | evidence for `V-04`/`V-10`; snapshot intact | seal altered | `manual` | SPECIFIED |
| `FPA-366` | A duplicate publication key is rejected | `REQ-770` | `FPW-051`/`WEP-390` | BND | same turn and standing | publish | duplicate key refused | second value | `auto` | SPECIFIED |
| `FPA-367` | Integrity doubt halts resolution as an incident | `REQ-858` | `FPW-051`/`SEC-026` | REC | doubt raised | resolve | halted, disclosed as a delay | continued resolving | `integration` | SPECIFIED |
| `FPA-368` | An engine fault is not converted into a conduct case | `REQ-856` | `FPW-051`/`INT-013` | INT | fault observed | classify | incident lane | conduct charged | `manual` | SPECIFIED |
| `FPA-369` | `k ≥ 5` is preserved while correcting | `REQ-802` | `FPW-051`/`INT-011` | PRV | correction published | render | suppression maintained | composite leak | `integration` | SPECIFIED |
| `FPA-370` | Enforcement status never enters a ranking surface | `REQ-803` | `FPW-051`/`PRV-019` | PRV | standings rendered | render | no status field | status visible | `integration` | SPECIFIED |

### 3.14 Register — Family M, governance review (`FPW-052`)

| ID | Objective | Req | FPW / INT | Cls | Given | When | Then | Fail | Exec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `FPA-371` | Enforcement practice is reviewed against a stated capacity | `REQ-867` | `FPW-052`/`MOD-035` | OWN | review due | review | capacity assumption stated and observed | an assumed capacity | `manual` | SPECIFIED |
| `FPA-372` | The review outcome is recorded even when nothing changes | `REQ-867` | `FPW-052`/`MOD-035` | POS | no change | close | record exists | no record | `manual` | SPECIFIED |
| `FPA-373` | Observed false-positive indications reach the review | `REQ-792` | `FPW-052`/`EVD-014` | INT | indications exist | review | catalogue updated by reference | findings dropped | `manual` | SPECIFIED |
| `FPA-374` | A capacity gap is declared with its compensating control | `REQ-846` | `FPW-052`/`MOD-029` | OWN | guarantee unmeetable | review | gap plus substitute recorded | gap concealed | `manual` | SPECIFIED |
| `FPA-375` | A mechanism defect is routed to Prompt 14, not to enforcement | `REQ-789` | `FPW-052`/`INT-019` | INT | faucet-like pattern | review | routed as balance work | manipulation charged | `manual` | SPECIFIED |
| `FPA-376` | No calibrated value is presented from this loop | `REQ-816` | `FPW-052`/`GOV-011` | SEC | review output | publish | all values remain provisional | a value claimed | `auto` | SPECIFIED |
| `FPA-377` | The transparency structure is defined without publishing | `REQ-868` | `FPW-052`/`UD-058` | OWN | structure drafted | review | fields and cadence defined; publication withheld | publication assumed | `manual` | SPECIFIED |
| `FPA-378` | No appeal-overturn rate is presented as measured | `REQ-866` | `FPW-052`/`P12B-10` | SEC | transparency draft | review | no statistic without data | a fabricated rate | `manual` | SPECIFIED |

---

## 4. Traceability ledger

**4.1 Backward chain.** `12A-CR-nnn` → `REQ-(763+n)` is exact and one-to-one (`GOV-013`, `D-186`). Every requirement names its normative rules in its own authority cell, and every 12C workflow names the rules and requirements it operates. The research layer therefore reaches each workflow in four hops: **12A source rows and benchmarks → `12A-CR` candidate → `REQ-` row → B-12 rules → `FPW-` workflow → `FPA-` specification.** No link in that chain was created by 12C; each was verified by reading the registers.

**4.2 Reading the ledger.** `NA` means the requirement is not a workflow-shaped obligation: the reason column states who owns it instead. **No requirement is dropped.** A `OWN` dependency means the workflow reaches the boundary of an owner or legal question and stops.

| REQ | Focus | Workflows | Contracts | Key rules | Edge cases | Tests | Not-applicable reason or owner dependency |
|---|---|---|---|---|---|---|---|
| `REQ-764` | server-side value | `FPW-021`, `FPW-037`, `FPW-047` | `INT-003`, `INT-006` | `FP-011` | `FPE-034` | `FPA-123`, `FPA-247`, `FPA-327` | none |
| `REQ-765` | one owning writer | `FPW-016`, `FPW-021`, `FPW-043` | `INT-003`–`INT-011` | `FP-012` | `FPE-023` | `FPA-123`, `FPA-127`, `FPA-299` | enforcement of the writer path is Stage 5 (`FPG-05`) |
| `REQ-766` | five states, capped consequence | `FPW-005`, `FPW-007`, `FPW-008` | `INT-002` | `EVD-001`, `EVD-002` | `FPE-008` | `FPA-033`, `FPA-042`, `FPA-043`, `FPA-070` | none |
| `REQ-767` | behaviour needs a second source | `FPW-007`, `FPW-008`, `FPW-011` | `INT-006` | `EVD-004`, `EVD-011` | `FPE-011` | `FPA-034`, `FPA-039`, `FPA-040` | none |
| `REQ-768` | six-term vocabulary | `FPW-011`, `FPW-014` | `INT-012` | `FP-018`, `FP-019` | `FPE-024` | `FPA-056`, `FPA-077` | surface text is Prompt 13 |
| `REQ-769` | session plus per-object authz | `FPW-036`, `FPW-043` | `INT-015` | `SEC-001`, `SEC-002` | `FPE-061` | `FPA-239`, `FPA-246`, `FPA-291` | none |
| `REQ-770` | atomic, keyed, revalidated | `FPW-016`, `FPW-021`, `FPW-024` | `INT-003` | `FP-013`, `SEC-003` | `FPE-027` | `FPA-093`, `FPA-155`, `FPA-366` | transaction code is Stage 5 |
| `REQ-771` | key retention in turns | `FPW-016` | `INT-003` | `SEC-003`, `F-FP-010` | `FPE-094` | `FPA-094`, `FPA-144` | none |
| `REQ-772` | no order payoff | `FPW-017`, `FPW-021`, `FPW-051` | `INT-013` | `FP-014`, `TR-044`–`TR-046` | `FPE-058` | `FPA-099`, `FPA-133`, `FPA-363` | none |
| `REQ-773` | limit inside the write transaction | — | — | `SEC-012`, `EX-012` | `FPE-010` | `FPA-288` | **NA**: a transaction-internal enforcement duty owned by Stage 5; 12C states the instruction boundary only |
| `REQ-774` | response minimisation | `FPW-037` | `INT-012` | `FP-015`, `PRV-007` | `FPE-063` | `FPA-247`, `FPA-248`, `FPA-252` | none |
| `REQ-775` | account-and-resource counters | `FPW-007` | `INT-016` | `MA-010`, `SEC-007` | `FPE-012` | `FPA-037` | none |
| `REQ-776` | declared failure direction | `FPW-033`, `FPW-016` | `INT-013` | `FR-001`, `SEC-009` | `FPE-076` | `FPA-218`, `FPA-243` | none |
| `REQ-777` | one account per person | `FPW-018`, `FPW-019` | `INT-001` | `MA-001` | `FPE-031` | `FPA-109`, `FPA-111` | restates `D-018`/`D-032`; no identity claim |
| `REQ-778` | network ceiling | `FPW-007`, `FPW-019` | `INT-016` | `MA-005`, `NET-039` | `FPE-012` | `FPA-035`, `FPA-036` | none |
| `REQ-779` | declaration recordable | `FPW-019` | `INT-001` | `MA-003` | `FPE-031` | `FPA-111`, `FPA-112` | none |
| `REQ-780` | declaration visibility and deletion | `FPW-019`, `FPW-040` | `INT-017` | `MA-004`, `PRV-021` | `FPE-031` | `FPA-113`, `FPA-114` | none |
| `REQ-781` | flow offences | `FPW-011`, `FPW-019`, `FPW-047` | `INT-006` | `MA-006`, `CO-001` | `FPE-085` | `FPA-115`, `FPA-116`, `FPA-346` | none |
| `REQ-782` | both-sides reach | `FPW-023`, `FPW-026` | `INT-003` | `MA-007`, `CO-009` | `FPE-039` | `FPA-148`, `FPA-176` | **owner** `UD-052` Open |
| `REQ-783` | ban evasion named | `FPW-018` | `INT-001` | `MA-008`, `V-05` | `FPE-029` | `FPA-107` | none |
| `REQ-784` | cooperation is not collusion | `FPW-011`, `FPW-049` | `INT-008` | `CO-002`, `FP-018` | `FPE-088` | `FPA-060`, `FPA-344`, `FPA-350` | none |
| `REQ-785` | one-sentence boundary | `FPW-011`, `FPW-014` | `INT-012` | `CO-001`, `FP-021` | `FPE-088` | `FPA-055`, `FPA-077` | none |
| `REQ-786` | structural indicators only | `FPW-011`, `FPW-047`, `FPW-049` | `INT-006` | `CO-003`, `EVD-016` | `FPE-082` | `FPA-141`, `FPA-145`, `FPA-325` | none |
| `REQ-787` | graph is queue input | `FPW-011` | `INT-006` | `CO-004` | `FPE-088` | `FPA-061` | none |
| `REQ-788` | alliance-scale FP class | `FPW-049` | `INT-008` | `CO-002`, `EVD-014` | `FPE-088` | `FPA-088`, `FPA-343` | none |
| `REQ-789` | prevention before surveillance | `FPW-009`, `FPW-047`, `FPW-052` | `INT-019` | `FP-016`, `D-177` | `FPE-084` | `FPA-046`, `FPA-333`, `FPA-375` | Prompt 14 owns the value |
| `REQ-790` | automated ceiling | `FPW-006` | `INT-002` | `EVD-003` | `FPE-010` | `FPA-027`–`FPA-030` | none |
| `REQ-791` | detector declaration | `FPW-009` | `INT-006` | `EVD-015` | `FPE-014` | `FPA-045`, `FPA-265` | none |
| `REQ-792` | false-positive catalogue | `FPW-009`, `FPW-052` | `INT-020` | `EVD-014` | `FPE-012` | `FPA-046`, `FPA-373` | none |
| `REQ-793` | no universal score | `FPW-008` | `INT-002` | `EVD-007`, `EVD-010` | `FPE-013` | `FPA-041`, `FPA-044` | none |
| `REQ-794` | reconstructible case record | `FPW-015` | `INT-014` | `EVD-012`, `EVD-020` | `FPE-025` | `FPA-085`, `FPA-086`, `FPA-089` | none |
| `REQ-795` | reviewer exclusion | `FPW-004`, `FPW-029` | `INT-008` | `EVD-019`, `MOD-021` | `FPE-006` | `FPA-015`–`FPA-018`, `FPA-197` | **owner** `UD-054` Open |
| `REQ-796` | no undisclosed collection | `FPW-009`, `FPW-037` | `INT-006` | `EVD-016`, `PRV-025` | `FPE-015` | `FPA-048`, `FPA-251` | none |
| `REQ-797` | unavailable capability stated | `FPW-007`, `FPW-009` | `INT-020` | `EVD-017`, `FP-008` | `FPE-015` | `FPA-038`, `FPA-047` | none |
| `REQ-798` | three-axis assignment | `FPW-035` | `INT-011` | `PRV-001`, `PRV-003` | `FPE-060` | `FPA-233`, `FPA-235` | none |
| `REQ-799` | reconcile in the owning register | `FPW-035` | `INT-011` | `PRV-003`, `PRV-017` | `FPE-060` | `FPA-234`, `FPA-237`, `FPA-238` | none |
| `REQ-800` | purpose before permission | `FPW-036` | `INT-007` | `PRV-004` | `FPE-016` | `FPA-239`, `FPA-240` | none |
| `REQ-801` | flows declared separately | `FPW-036` | `INT-007` | `PRV-004`, `PRV-006` | `FPE-061` | `FPA-241`, `FPA-242` | none |
| `REQ-802` | aggregate `k ≥ 5` | `FPW-038`, `FPW-049`, `FPW-051` | `INT-011` | `PRV-018`, `TR-022` | `FPE-064` | `FPA-253`–`FPA-258`, `FPA-349` | none |
| `REQ-803` | no status disclosure | `FPW-039`, `FPW-014`, `FPW-051` | `INT-012` | `PRV-019`, `MOD-018` | `FPE-066` | `FPA-005`, `FPA-261`–`FPA-264`, `FPA-370` | none |
| `REQ-804` | failure text | `FPW-037` | `INT-012` | `PRV-020` | `FPE-001` | `FPA-002`, `FPA-249` | none |
| `REQ-805` | data inventory columns | `FPW-035`, `FPW-041` | `INT-011` | `PRV-023`, `DAT-001` | `FPE-060` | `FPA-233`, `FPA-273` | **NA for population**: the inventory itself is a Stage 5 artefact; 12C specifies consumption and required columns only |
| `REQ-806` | pseudonymous labelling | `FPW-038` | `INT-016` | `PRV-024` | `FPE-065` | `FPA-260` | none |
| `REQ-807` | pseudonymisation key custody | — | `INT-016` | `PRV-024` | `FPE-015` | `FPA-120` | **NA**: secret custody, rotation and exclusion from backups are Stage 5/6 controls, not workflows |
| `REQ-808` | retention per class | `FPW-041` | `INT-014` | `PRV-023` | `FPE-068` | `FPA-273`, `FPA-274` | **legal** `UD-017`/`UD-055` Open |
| `REQ-809` | erasure versus spine conflict | `FPW-041` | `INT-014` | `PRV-022`, `EVD-038` | `FPE-068` | `FPA-275` | **legal and owner** `UD-055` Open |
| `REQ-810` | backup exposure disclosed | `FPW-052` | `INT-020` | `FR-014`, `CF-02` | `FPE-055` | `FPA-374` | owner item `CF-02`; disclosure duty only |
| `REQ-811` | one taxonomy | `FPW-011` | `INT-002` | `FP-017`, `FP-021` | `FPE-020` | `FPA-055` | none |
| `REQ-812` | one six-tier ladder | `FPW-012`, `FPW-013`, `FPW-017` | `INT-002` | `MOD-036`–`MOD-041` | `FPE-028` | `FPA-069`, `FPA-099`, `FPA-103` | **owner** `UD-053` Open |
| `REQ-813` | severity factors | `FPW-012` | `INT-002` | `MOD-039`, `FP-025` | `FPE-021` | `FPA-063`–`FPA-068` | none |
| `REQ-814` | exploit and incident lanes | `FPW-033` | `INT-013` | `FP-027`, `MOD-001` | `FPE-055` | `FPA-223`, `FPA-224` | none |
| `REQ-815` | owning subsystem stays authoritative | `FPW-013`, `FPW-021`, `FPW-047`–`FPW-051` | `INT-004`–`INT-011` | `FP-004`, `MOD-031` | `FPE-026` | `FPA-073`, `FPA-327`, `FPA-331`, `FPA-341` | none |
| `REQ-816` | no penalty approved by category | `FPW-013`, `FPW-017`, `FPW-025`, `FPW-027` | `INT-019` | `MOD-037`, `MOD-038` | `FPE-043` | `FPA-071`, `FPA-076`, `FPA-163`, `FPA-181` | **owner** `UD-053`, `UD-059` Open |
| `REQ-817` | correction is a separate class | `FPW-021`, `FPW-022`, `FPW-025` | `INT-003` | `MOD-051`–`MOD-057`, `COR-010` | `FPE-037` | `FPA-125`, `FPA-137`, `FPA-138`, `FPA-161` | **owner** `UD-052` Open |
| `REQ-818` | attaches to account, survives reroll | `FPW-016`, `FPW-018` | `INT-001`, `INT-002` | `MOD-033` | `FPE-029` | `FPA-091`, `FPA-105`, `FPA-110` | none |
| `REQ-819` | owner's appended correction path | `FPW-021`, `FPW-050`, `FPW-051` | `INT-003`–`INT-011` | `FP-012`, `COR-004` | `FPE-035` | `FPA-124`, `FPA-128`, `FPA-335`, `FPA-353` | none |
| `REQ-820` | conflicts surfaced | `FPW-020`, `FPW-026`, `FPW-033` | `INT-003` | `MOD-032`, `COR-007` | `FPE-044` | `FPA-118`, `FPA-167`–`FPA-174`, `FPA-225` | none |
| `REQ-821` | comprehensible sanction record | `FPW-014` | `INT-012` | `MOD-017`, `MOD-018` | `FPE-024` | `FPA-077`, `FPA-080`, `FPA-081`, `FPA-126` | none |
| `REQ-822` | structured intake as accusation | `FPW-001` | `INT-017` | `MOD-002`, `EVD-013` | `FPE-001` | `FPA-001`, `FPA-002`, `FPA-006`, `FPA-342` | none |
| `REQ-823` | clustering, volume never severity | `FPW-002` | `INT-017` | `MOD-003`, `F-FP-008` | `FPE-003` | `FPA-007`–`FPA-010` | none |
| `REQ-824` | false versus good-faith report | `FPW-002`, `FPW-011` | `INT-017` | `MOD-004`, `V-15` | `FPE-004` | `FPA-004`, `FPA-009`, `FPA-090` | none |
| `REQ-825` | confidential routing and retaliation | `FPW-003` | `INT-015` | `MOD-005`, `MOD-006` | `FPE-005` | `FPA-011`–`FPA-014` | none |
| `REQ-826` | player evidence is a pointer | `FPW-008`, `FPW-011` | `INT-006` | `EVD-013`, `EVD-023` | `FPE-020` | `FPA-057`, `FPA-142` | none |
| `REQ-827` | artefact provenance | `FPW-010` | `INT-014` | `EVD-023`, `EVD-036` | `FPE-018` | `FPA-052` | none |
| `REQ-828` | custody events | `FPW-010`, `FPW-046` | `INT-014` | `EVD-022`, `EVD-026` | `FPE-016` | `FPA-051`, `FPA-321` | none |
| `REQ-829` | tamper-evident chain and verification | `FPW-045` | `INT-014` | `EVD-030`–`EVD-032`, `F-FP-012` | `FPE-078` | `FPA-309`–`FPA-316`, `FPA-318` | **BLOCKED** `P12B-14`: no implementation or executed run |
| `REQ-830` | legal deletion with redaction | `FPW-040`, `FPW-041` | `INT-014` | `EVD-038`, `PRV-022` | `FPE-068` | `FPA-270`, `FPA-276`, `FPA-324` | **legal** `UD-055` Open |
| `REQ-831` | evidence minimisation | `FPW-010`, `FPW-040` | `INT-014` | `EVD-024`, `PRV-021` | `FPE-070` | `FPA-054`, `FPA-267`, `FPA-281` | **legal** `UD-055` Open |
| `REQ-832` | conflicting records recorded | `FPW-010` | `INT-003` | `EVD-018` | `FPE-018` | `FPA-053` | none |
| `REQ-833` | one appeal, in force, reasoned | `FPW-027`, `FPW-028` | `INT-018` | `MOD-042`–`MOD-045` | `FPE-048` | `FPA-177`, `FPA-180`, `FPA-185` | none |
| `REQ-834` | reopening bar | `FPW-030` | `INT-018` | `MOD-046` | `FPE-052` | `FPA-199`–`FPA-202` | none |
| `REQ-835` | sufficient explanation, method withheld | `FPW-029` | `INT-018` | `MOD-018`, `MOD-045` | `FPE-050` | `FPA-193`, `FPA-194` | none |
| `REQ-836` | upheld appeal effects | `FPW-024`, `FPW-029` | `INT-003`, `INT-018` | `MOD-047`, `MOD-048` | `FPE-042` | `FPA-153`–`FPA-157`, `FPA-195` | none |
| `REQ-837` | independence guarantees stated | `FPW-029` | `INT-018` | `MOD-049` | `FPE-050` | `FPA-191`, `FPA-198` | **owner** `UD-054` Open |
| `REQ-838` | roles defined by prohibition list | `FPW-042` | `INT-020` | `ADM-001`–`ADM-005` | `FPE-072` | `FPA-287`, `FPA-288` | none |
| `REQ-839` | named capabilities, no superuser | `FPW-042` | `INT-015` | `ADM-002`, `ADM-018` | `FPE-072` | `FPA-283`, `FPA-284` | Stage 5/6 grant mechanism |
| `REQ-840` | step-up session | `FPW-043` | `INT-015` | `ADM-007` | `FPE-074` | `FPA-291`, `FPA-292`, `FPA-286` | Stage 6 mechanism |
| `REQ-841` | privileged read auditable | `FPW-036` | `INT-014` | `ADM-008`, `EVD-025` | `FPE-061` | `FPA-240`, `FPA-244`, `FPA-245` | none |
| `REQ-842` | no self-dealing | `FPW-043` | `INT-015` | `ADM-009` | `FPE-073` | `FPA-293` | **owner** `UD-054` Open |
| `REQ-843` | investigate versus decide | `FPW-043` | `INT-020` | `ADM-010` | `FPE-073` | `FPA-294` | **owner** `UD-054` Open |
| `REQ-844` | author versus publisher | `FPW-009`, `FPW-043` | `INT-020` | `ADM-011` | `FPE-014` | `FPA-045`, `FPA-295` | **owner** `UD-054` Open |
| `REQ-845` | ledger executes financial correction | `FPW-021`, `FPW-026` | `INT-003` | `ADM-012`, `COR-002` | `FPE-034` | `FPA-123`, `FPA-172`, `FPA-299` | none |
| `REQ-846` | declared gap with substitute | `FPW-042`, `FPW-043`, `FPW-052` | `INT-020` | `ADM-013` | `FPE-073` | `FPA-272`, `FPA-296`, `FPA-374` | **owner** `UD-054` Open |
| `REQ-847` | emergency powers bounded and self-expiring | `FPW-031`, `FPW-032` | `INT-013` | `MOD-025`, `MOD-026`, `F-FP-016` | `FPE-053` | `FPA-203`–`FPA-212` | **owner** `UD-056` for `D_e` |
| `REQ-848` | suspend, freeze, withhold only | `FPW-031` | `INT-013` | `MOD-025`, `ADM-014`, `ADM-027` | `FPE-053` | `FPA-203`, `FPA-207`, `FPA-210` | none |
| `REQ-849` | retrospective review of emergencies | `FPW-032` | `INT-020` | `MOD-028` | `FPE-054` | `FPA-213`, `FPA-214`, `FPA-216` | **owner** `UD-054`/`UD-056` Open |
| `REQ-850` | temporary measures disclosed | `FPW-031`, `FPW-039` | `INT-012` | `MOD-027` | `FPE-054` | `FPA-209`, `FPA-266`, `FPA-082` | none |
| `REQ-851` | one named audit event set | `FPW-044` | `INT-014` | `EVD-026`, `EVD-027` | `FPE-076` | `FPA-301`, `FPA-302` | none |
| `REQ-852` | identifiers, decisions, reasons only | `FPW-044` | `INT-014` | `EVD-028` | `FPE-077` | `FPA-303` | none |
| `REQ-853` | spine rows never sampled | `FPW-041`, `FPW-044` | `INT-014` | `EVD-034` | `FPE-069` | `FPA-279`, `FPA-308` | none |
| `REQ-854` | audit access purpose-bound | `FPW-046` | `INT-014` | `EVD-033`, `PRV-015` | `FPE-081` | `FPA-306`, `FPA-307`, `FPA-323` | none |
| `REQ-855` | appended correction; deletion authority | `FPW-041`, `FPW-046` | `INT-014` | `EVD-029`, `EVD-038` | `FPE-080` | `FPA-305`, `FPA-316`, `FPA-322`, `FPA-324` | **legal** `UD-055` Open |
| `REQ-856` | incident classes with posture and owner | `FPW-033` | `INT-013` | `SEC-024`, `FR-001` | `FPE-055` | `FPA-217`, `FPA-219`, `FPA-368` | none |
| `REQ-857` | breach assessed either way | `FPW-034` | `INT-015` | `SEC-025` | `FPE-059` | `FPA-227`–`FPA-232` | **legal** `UD-017` Open |
| `REQ-858` | halt over doubtful continuation | `FPW-033`, `FPW-045`, `FPW-051` | `INT-013` | `SEC-026` | `FPE-098` | `FPA-221`, `FPA-313`, `FPA-367` | none |
| `REQ-859` | B-12 owns no mechanic | `FPW-013`, `FPW-016` | `INT-001`, `INT-002` | `FP-004` | `FPE-023` | `FPA-073`, `FPA-097`, `FPA-327` | none |
| `REQ-860` | consume obligations by reference | `FPW-021`, `FPW-047`–`FPW-051` | `INT-006`–`INT-011` | `INT-003`, `INT-009` | `FPE-086` | `FPA-127`, `FPA-143`, `FPA-337`, `FPA-356` | none |
| `REQ-861` | no new entitlement or reward | `FPW-013`, `FPA-` owners, `FPW-023`, `FPW-025` | `INT-010`, `INT-011` | `FP-004`, `MOD-058` | `FPE-030` | `FPA-131`, `FPA-147`, `FPA-160`, `FPA-166`, `FPA-328` | none |
| `REQ-862` | posture per category, never global | `FPW-033` | `INT-013` | `FR-001`, `SEC-022` | `FPE-055` | `FPA-218`, `FPA-314` | none |
| `REQ-863` | downtime keeps play and records | `FPW-005`, `FPW-006`, `FPW-038` | `INT-013` | `FR-003`, `FR-004` | `FPE-009` | `FPA-023`, `FPA-024`, `FPA-083`, `FPA-104`, `FPA-259` | none |
| `REQ-864` | unavailable evidence yields a hold | `FPW-005`, `FPW-028` | `INT-013` | `SEC-023`, `FR-005` | `FPE-008` | `FPA-020`, `FPA-021`, `FPA-188` | none |
| `REQ-865` | association correction path | `FPW-020`, `FPW-024` | `INT-001` | `COR-013`, `EVD-018` | `FPE-032` | `FPA-117`, `FPA-118` | none |
| `REQ-866` | the corpus states its non-claims | `FPW-009`, `FPW-045`, `FPW-052` | `INT-020` | `FP-008`, `GOV-024` | `FPE-078` | `FPA-038`, `FPA-317`, `FPA-334`, `FPA-340`, `FPA-376`, `FPA-378` | none |
| `REQ-867` | periodic enforcement-practice review | `FPW-052` | `INT-019` | `MOD-035` | `FPE-099` | `FPA-371`–`FPA-374` | **owner** `UD-053`/`UD-054` Open |
| `REQ-868` | transparency structure; publication withheld | `FPW-052` | `INT-020` | `PRV-018` | `FPE-100` | `FPA-377`, `FPA-378` | **owner** `UD-058` Open |
| `REQ-869` | legal dependency named, conservative branch | `FPW-034`, `FPW-041` | `INT-020` | `GOV-009` | `FPE-059` | `FPA-228`, `FPA-231`, `FPA-278`, `FPA-324` | **legal** `UD-017` Open |

**4.3 Ledger totals.** 106 requirements; **106 mapped**; **3 mapped with an explicit non-workflow reason** (`REQ-773`, `REQ-805` population duty, `REQ-807` key custody); **103 fully workflow-mapped**; **0 orphan requirements**; **20 rows carrying an owner or legal dependency**, all of which remain Open and unchanged. Ten acceptance rows are `BLOCKED` (`FPA-309`–`FPA-316`, `FPA-318`–`FPA-320`), which is why `REQ-829` and the audit-facing part of `REQ-855` cannot be graded from documentation alone.

---

## 5. Gate register

**5.1 Grading rules.** The six statuses and the prohibited grading shortcuts are exactly those of the 12B acceptance framework §1, and they are reused, not restated. **No 12C gate may raise, lower or reinterpret `P12B-14`, `P12B-16`, `P12B-23`, any of the seven 12A PARTIAL gates, or any of the eight 11C PARTIAL gates.** `P12B-25` graded the 12C boundary as the *absence* of 12C material; from this pass forward that gate's premise is historical and its recorded result is left exactly as 12B wrote it — 12C does not re-grade another prompt's gate.

**5.2 Tally: 16 `PASS` · 2 `PARTIAL` · 2 `BLOCKED` · 0 `FAIL` · 0 `NOT RUN` · 0 `NOT APPLICABLE` = 20** — reassessed on 2026-11-10 by the separately authorized Prompt 12C-FINAL-C1 pass, which recomputed the tally from the gate rows below rather than declaring it.

| Gate | Acceptance criterion | Evidence | Location | Verification | Result | Remaining limitation | Required action |
|---|---|---|---|---|---|---|---|
| `P12C-01` | Source inventory, authority order and non-claims are stated and no upstream document is rewritten | header; §1.3; §9 | this document §§ header, 1, 9; workflows §1 | `12C-01`, `12C-02`, `12C-20` | **PASS** | Statements cannot prevent a later session over-claiming | every later prompt re-runs the honesty scan |
| `P12C-02` | Journeys cover all eight families in the 12B handoff plus the two the requirement register adds | `FPJ-001`…`FPJ-010` | workflows §4, §5 | `12C-03` | **PASS** | Journeys are specifications, not operated paths | Prompt 13 turns them into surfaces |
| `P12C-03` | The workflow library adds no rule, no number, no identifier in another namespace | 52 records; workflows §1.3, §6.2 | workflows §6–§19 | `12C-04`, `12C-21` | **PASS** | A workflow can reveal a missing rule without being allowed to write one | gaps go to `FPG-##`, rules go to their owner |
| `P12C-04` | Every workflow record supplies all twelve fields | 52 × 12 rows | workflows §7–§19 | `12C-04` | **PASS** | Field presence is not behavioural proof | Stage 5 implements |
| `P12C-05` | Edge cases cover all six required scenario categories | 100 rows; §2.4 counts | this document §2.5 | `12C-05`, `12C-06` | **PASS** | A catalogue is not a test run | execution when a build exists |
| `P12C-06` | No 11C edge case is duplicated, renumbered or re-status-changed | §2.2 dedup rule; `WEE-` references | this document §2.2; 11C §18 | `12C-07` | **PASS** | Shared situations are cited, not copied | none |
| `P12C-07` | All twenty `INT-` contracts are reused with their identifiers and expanded to the fifteen operational fields | matrix parts 1 and 2 | integration §2, §3 | `12C-08`, `12C-09` | **PASS** | Policy interfaces, not APIs | Stage 5 and Prompt 13 translate |
| `P12C-08` | No system receives authority it does not possess; no duplicate source of truth | consistency rules 2 and 3 | integration §6 | `12C-10` | **PASS** | Specification-level only | Stage 5 privilege verification |
| `P12C-09` | Market, diplomacy, alliance, warfare, event, objective, ranking and progression rules are uncontradicted | §4.1–§4.6; conflict register C-01, C-02 | integration §4, §7 | `12C-11` | **PARTIAL** | Two registered conflicts remain owner-reserved (`UD-053`, `UD-052`); 12C may not choose | owner decisions |
| `P12C-10` | Accounts, turn processing, administration, moderation, reporting, notifications, audit, retention and recovery are consistent | §4.7, §4.8; `FPG-04`, `FPG-05` | integration §4, §7 | `12C-11` | **PARTIAL** | The prototype privilege and audit-protection defects are unresolved, so consistency is asserted at specification level only | Stage 5 security work |
| `P12C-11` | Every contract row states ownership, permissions, inputs, outputs, failure, audit and dependency | 20 × 15 fields | integration §2, §3 | `12C-09` | **PASS** | No implementation guarantee is implied | none |
| `P12C-12` | Acceptance specifications cover the fourteen mandatory areas | 378 rows across §3.5–§3.14 | this document §3 | `12C-12` | **PASS** | Coverage of designs, not of behaviour | execution when a build exists |
| `P12C-13` | Negative, boundary, security, privacy and recovery cases are present in real proportion | class split §3.3 | this document §3 | `12C-13` | **PASS** | Proportions describe the register, not the running system | none |
| `P12C-14` | Every 12B requirement is mapped or carries a stated non-applicability reason | 106 rows; §4.3 | this document §4.2 | `12C-14` | **PASS** | A link is planned coverage, never proof | Stage 5 and Prompt 14 consume |
| `P12C-15` | No orphan workflow, contract, edge case, test or gate; no artificial link | §6.2 | this document §6.2 | `12C-15`, `12C-16` | **PASS** | Emptiness of a column is checked, its truth is not | none |
| `P12C-16` | D-014 observed: no owner decision closed, no recommendation promoted, R7/R8/12B-C1 unchanged | §6, §7; workflows §21.6 | this document §6, §7 | `12C-17`, `12C-18`, `12C-19` | **PASS** | The policy binds the record, not the future | owner rulings when issued |
| `P12C-17` | Audit-spine and tamper-evidence acceptance can be graded only against an executed verification run | `FPA-309`–`FPA-316`, `FPA-318` | this document §3.12 | run the block | **BLOCKED** | No chained digest, verification job or protective trigger exists (`EVD-041`, `SEC-036`, `SEC-038`) | Stage 5 implementation plus an executed run; `P12B-14` stays PARTIAL |
| `P12C-18` | Supabase privilege acceptance can be graded only against SQL permission tests | `FPA-123`, `FPA-288`, `FPA-299`, `FPA-319`, `FPA-320` | this document §3.11, §3.12 | run the block | **BLOCKED** | Table-wide `UPDATE` on `feasibility.profiles` including `treasury` persists; no `0005`-equivalent migration; no `tests/sql/` | Stage 5 column-privilege work; `P12B-16` stays PARTIAL |
| `P12C-19` | The independent 12C validator and its fixtures pass against the delivered corpus | `12C_validate_fair_play_workflows.py` | §8 | run the validator | **PASS** | It is a document checker; it proves nothing about behaviour | re-run after every edit |
| `P12C-20` | Project status surfaces are synchronized without changing any R7, R8 or 12B-C1 clause | [reconciliation inventory](../qa_backups/12C_FINAL_C1_conflict_reconciliation.md) §4–§6, [log §86](06_stage_2_progress_log.md) | `AI_CONTEXT`, `AI_HANDOFF`, `PROJECT_PROGRESS`, `ROADMAP`, `00`–`06` | `12C-22`, `12B_validate_b12.py` | **PASS** | The markers that made this gate PARTIAL were classified file by file and resolved to the verified main-line side by the separately authorized 12C-FINAL-C1 pass; each status surface now carries one non-contradictory current B-12 declaration, all 11 affected QA scripts parse, and `12B_validate_b12.py` reports 87/87 with its code unmodified | reassessment moves no R7, R8, 12B-C1 or implementation claim |

---

## 6. Decisions, orphans and reverse traceability

**6.1 New decisions.** Ten Category B design decisions are recorded, `D-188`…`D-197`, mirrored as `DD-236`…`DD-245`. Each is a documentation-architecture or specification choice within `D-014`; **none approves a rule, a number, a permission, a penalty, a retention period, an implementation or an owner-reserved position.** They are written into [DECISIONS.md](../DECISIONS.md) and [04](04_approved_and_provisional_decisions.md) and are not restated here as a second register.

| ID | Subject | What it decides | What it does not decide |
|---|---|---|---|
| `D-188` | 12C canonical document set | three companions under the reserved `20_fair_play_and_player_protection*` family | the 12B files' content or status |
| `D-189` | 12C identifier namespaces | `FPJ-`, `FPW-`, `FPE-`, `FPA-`, `FPG-`, `P12C-`, validator checks `12C-` | any new rule, requirement or contract id |
| `D-190` | contracts are reused | all twenty `INT-` rows expanded, none added | contract ownership |
| `D-191` | record schemas | twelve-field workflow and journey records carrying the seventeen required attributes | the attributes themselves, which come from the prompt |
| `D-192` | edge-case organisation | category by failing mechanism; cite `WEE-` instead of copying | 11C's register |
| `D-193` | status discipline | `SPECIFIED` is the only default; `BLOCKED` requires a named obligation | any gate movement |
| `D-194` | undecided-value behaviour | `PROVISIONAL_BLOCK` is the specified result wherever the formula register lacks its authority | the value |
| `D-195` | gate separation | 12C gates grade 12C artefacts and never move another prompt's gate | `P12B-14/16/23` and the 12A and 11C PARTIAL gates |
| `D-196` | validation approach | one focused stdlib 12C validator over 12C's own artefacts | extending R7 validator hardening, which is deferred |
| `D-197` | baseline-defect handling | the pre-existing conflict markers are recorded as a limitation and left untouched | their resolution |

**6.2 Orphan analysis.**

| Object type | Count | Orphans | Note |
|---|---|---|---|
| Workflows `FPW-` | 52 | **0** | every record names at least one rule group, one `REQ-` row and one `FPA-` block |
| Journeys `FPJ-` | 10 | **0** | each maps to workflows in §20 of the workflows document |
| Contracts `INT-` | 20 | **0** | each appears in both matrix parts and in at least one workflow trace row |
| Edge cases `FPE-` | 100 | **0** | each names a workflow and at least one `FPA-` row |
| Acceptance specs `FPA-` | 378 | **0** | each names a requirement, a workflow or contract, a class and a status |
| Gates `P12C-` | 20 | **0** | each names evidence, a location and a verification method |
| Gaps `FPG-` | 10 | **0** | each names who decides and the 12C treatment |
| Requirements `REQ-764`…`REQ-869` | 106 | **0** | see §4.3 |
| Circular dependencies | — | **none found** | `FPW-033` depends on `FPW-031` for effect and on `FPW-044` for evidence; neither routes back into the other's decision |
| Missing integration links | — | **3 recorded** | `REQ-773`, `REQ-805` population and `REQ-807` custody are Stage 5 duties, stated rather than forced into a workflow |

**6.3 Reverse traceability.** Every rule prefix in B-12 is operated by at least one workflow: `FP` (`FPW-006`, `FPW-011`–`FPW-014`, `FPW-037`), `EVD` (`FPW-007`–`FPW-010`, `FPW-044`–`FPW-046`), `MA` (`FPW-016`–`FPW-020`), `CO` (`FPW-011`, `FPW-013`, `FPW-023`, `FPW-047`–`FPW-049`), `EX` (`FPW-006`, `FPW-024`, `FPW-047`), `PRV` (`FPW-035`–`FPW-041`), `MOD` (`FPW-001`–`FPW-033`), `ADM` (`FPW-036`, `FPW-042`, `FPW-043`), `COR` (`FPW-021`–`FPW-026`), `SEC` (`FPW-006`, `FPW-033`, `FPW-043`–`FPW-046`), `INT` (all of Family L plus every matrix row), `FR` (`FPW-033` and the failure field of every record), `GOV` (§1.3, §5.1, §6, §9). No B-12 rule prefix is unrepresented, and no representation claim implies execution.

**6.4 12A open-question disposition.** The 12A register rows and their statuses are **not edited by 12C**; this table records only what the 12C specification can already answer from existing rules.

| `12A-OPEN` | Position after 12C | Basis |
|---|---|---|
| `001` class vocabulary | answered: `V-01`…`V-16` is the only taxonomy; `FPW-011` enforces it | `FP-017` |
| `002` is a keyed `/64` an identifier | **remains open**; `FPW-038` requires the identifiability assessment without deciding it | `PRV-024` |
| `003` idempotency-key lifetime | answered: `K = P_r + 1` turns, per owner declaration | `F-FP-010`, `FPW-016` |
| `004` privileged auth strength | **remains Stage 6's**; `FPW-043` states the required properties | `ADM-007` |
| `005` operator incident throughput | **remains owner**; declared as a capacity gap | `MOD-029`, `UD-054` |
| `006` who may read tax and consent records | partially specified: purpose-bound, minimised, audited; the reader list is `UD-046`/`UD-044` | `FPW-036`, `FPW-049` |
| `007` do published counts arm evaders | **remains open**; `FPW-038` withholds rather than decides | `PRV-018` |
| `008` defensible affordable retention | **remains legal**; only existing class values are consumed | `FPW-041`, `UD-055` |
| `009` audit-verification cadence | **remains provisional**; `I_v` unset | `F-FP-013`, `FP-P08` |
| `010` age gate without refused documents | **untouched by 12C**; no workflow needs it | `UD-060` |
| `011` ordering conflicting corrections | answered structurally by `FPW-026` and `F-FP-004` | `COR-007` |
| `012` does a correction carry an appeal right | answered: yes, once, through the appeal route | `COR-008`, `FPW-027` |
| `013` reversal order for a compound cross-system exploit | **owned by 12C and answered structurally**: per-owner append in recorded case order at each owner's next valid boundary, with reach still `UD-052` | `FPW-026`, `FPA-175`, `FPE-047` |
| `014` is action causation meaningful at 2-hour granularity | **remains research**; 12C never infers causation from timing alone | `EVD-004`, `CO-003` |
| `015` does `service_role` bypass invalidate RLS claims | **remains Stage 5 verification**; `FPA-320` is `BLOCKED` on exactly this question | `SEC-035`, `SEC-037` |

---

## 7. Unresolved issues register

| Issue | Type | Systems | Related | Why resolution is needed | Options supported by the corpus | Consequence of each | Can 12C continue without it | Who decides |
|---|---|---|---|---|---|---|---|---|
| `C-01` two consequence ladders | owner | B-03, B-06, B-11, B-12 | `REQ-812`, `REQ-816`, `UD-053` | one ladder must replace two incompatible models before any duration or authority split can be stated | adopt `MOD-036` as the single ladder, or retain the subsystem reversal model | adopting without the owner would invent an approved penalty scale; retaining both leaves enforcement unimplementable | **yes** — every affected row stops at `PROVISIONAL_BLOCK` | **Owner** |
| `C-02` correction reach | owner | B-04, B-07, B-09, B-12 | `REQ-782`, `UD-052` | both-legs recovery is a fairness commitment the project cannot ground in identity proof | receiving-leg only, or both legs | receiving-leg only under-recovers; both legs without a decision asserts an authority the design has not been granted | **yes** — `FPW-023` executes the conservative branch | **Owner** |
| `FPG-01` no content surface | design | B-09, B-12, Prompt 13 | `MOD-014` | `ALL-158` presumes moderation of names and bulletins that have no surface | build a surface in Prompt 13, or narrow the Alliance claim | specifying removal powers now would create a mechanism that does not exist | **yes** | Prompt 13, owner for scope |
| `FPG-04` audit spine unimplemented | security | B-02, B-12 | `REQ-829`, `P12B-14` | tamper-evidence cannot be claimed, so `P12C-17` cannot close | implement, then run verification | claiming integrity from a document would be the recorded failure mode | **yes** — `FPA-309`–`FPA-324` stay `BLOCKED` | Stage 5 |
| `FPG-05` profile treasury grant | security | B-03, B-04 | `REQ-765`, `P12B-16` | an authenticated player could still write a server-owned field | column privileges plus SQL tests, or server-mediated writes | either way the single-writer rule is unproven until tested | **yes** | Stage 5 |
| `FPG-06` retention and erasure | legal | B-02, B-03, B-12 | `REQ-808`, `REQ-809`, `UD-017`, `UD-055` | period and duty conflict | conservative branch until counsel answers | inventing a period creates an obligation the project may not satisfy | **yes** | Owner and counsel |
| `FPG-07` segregation at current staffing | owner | B-12 | `REQ-795`, `REQ-843`, `REQ-846`, `UD-054` | independence claims must be labels, not guarantees | hire, or accept the label plus disclosure | a claimed guarantee that cannot be demonstrated is worse than the label | **yes** | **Owner** |
| `FPG-09` appeal window and budget | owner | B-12 | `REQ-833`, `UD-059` | a window that is enforced, published or measured must be chosen | any owner-chosen turn count | enforcing an invented window converts a placeholder into policy | **yes** — `FPA-181` | **Owner** |
| `FPG-10` `WPF-` unauthorised-actor code | design | B-11, B-12 | `WEP-667`, `WEP-674` | the namespace is closed, so no new code may be minted | reuse `WPF-13` with `WPA-50` as 11C disposed | renumbering would break 11C's ledger | **yes** | B-11 owner document |

---

## 8. Validator

`docs/qa_backups/12C_validate_fair_play_workflows.py` is a stdlib-only document validator in the house style: parsed tables, per-check results, positive and negative fixtures, exit codes 0/1/2. It checks 12C's own artefacts and the continuity clauses this prompt requires preserved. It is deliberately **not** an extension of the R7 hardening effort (`D-196`): it does not attempt canonical-extraction rework, and it does not modify `12B_validate_b12.py`.

| Check | What it measures |
|---|---|
| `12C-01` | the three 12C files exist with version, date, status, authority and non-claim blocks |
| `12C-02` | no 12C file contains an implementation, deployment, migration, test-execution or legal-compliance claim |
| `12C-03` | `FPJ-001`…`FPJ-010` contiguous; each journey carries its twelve fields |
| `12C-04` | `FPW-001`…`FPW-052` contiguous; each carries all twelve fields; `FPW-053` unallocated |
| `12C-05` | every required edge-case category is represented and the declared counts equal the parsed rows |
| `12C-06` | `FPE-001`…`FPE-100` contiguous, unique, each with a workflow and at least one test |
| `12C-07` | no `WEE-` identifier is redefined or renumbered in 12C; `WEE-` may only be cited |
| `12C-08` | the integration matrix contains exactly the twenty `INT-` identifiers, no `INT-021` |
| `12C-09` | every matrix row fills both parts (fifteen fields) and names a workflow and a test block |
| `12C-10` | no matrix row gives a system an authority the rulebook does not grant |
| `12C-11` | every named conflict or gap has an owner column and a 12C treatment |
| `12C-12` | `FPA-001`…`FPA-378` contiguous and unique |
| `12C-13` | every test row carries one of the eight classes and a legal status; class and execution tallies reconcile |
| `12C-14` | the traceability ledger covers `REQ-764`…`REQ-869` with no gap, no duplicate and no orphan |
| `12C-15` | every `FPA-`, `FPE-`, `FPW-` and `INT-` identifier referenced anywhere in 12C resolves inside 12C or in an existing register |
| `12C-16` | no `REQ-` row is restated as a new requirement; requirement text is never duplicated as a rule |
| `12C-17` | the three 12B PARTIAL gates, the seven 12A PARTIAL gates and R7/R8/12B-C1 wording appear preserved |
| `12C-18` | no owner-reserved `UD-` row is described as resolved, closed or assumed |
| `12C-19` | no provisional parameter is presented as approved; `PROVISIONAL_BLOCK` remains the specified branch |
| `12C-20` | no universal fail-open or fail-closed statement appears in any 12C artefact |
| `12C-21` | no 12C file allocates a rule identifier in a B-12 prefix namespace |
| `12C-22` | status surfaces name Prompt 12C and keep the deferral and non-closure clauses intact |

---

## 9. Non-claims and residual risk

1. **Nothing is implemented.** 52 workflows, 10 journeys, 100 edge cases and 378 acceptance specifications exist as documents. No queue, tool, record type, trigger, job, permission, screen or ledger exists because of them (`EVD-041`, `SEC-030`, `GOV-024`).
2. **Nothing has been executed.** No `FPA-` row holds `EXECUTED` or `PASS`; `PASS` appears only in the gate register and only about documentary criteria.
3. **No number is approved.** Every duration, window, cap, weight, interval, rate and reach remains as the formula and parameter register states it.
4. **Twenty requirements remain Open** and their owner or legal questions are unaddressed by 12C, by design.
5. **The identity residual is unchanged**: `EVD-006` and `D-176` record an accepted critical residual, and 12C states it in `FPW-007` rather than dissolving it.
6. **Separation of duties is disclosed, not demonstrated** (`ADM-013`, `REQ-846`); every affected row uses the `unsegregated` label.
7. **The outstanding security obligations are still outstanding**, and `P12C-17` and `P12C-18` are `BLOCKED` precisely so that no workflow text can be read as their closure.
8. **The repository baseline defect this pass recorded has since been repaired under separate authority.** At the 12C close the tree carried committed merge-conflict markers in 25 files (14 documents, 11 QA scripts, 117 hunks); `12B_validate_b12.py` reported 86 of 87 checks with `12B-78` failing and those eleven scripts could not parse. Prompt 12C §17 forbade touching them, so 12C recorded the condition. The bounded Prompt 12C-FINAL-C1 pass (2026-11-10) then classified every occurrence, resolved each hunk to the evidence-verified main-line side and restored the scripts: the suite now reports **87/87 with the validator file byte-unchanged**, all 11 scripts parse, and the per-file evidence sits in [the reconciliation inventory](../qa_backups/12C_FINAL_C1_conflict_reconciliation.md). Nothing here claims an implementation, a runtime behaviour or a security control: the repair changed document and script text only. `D-197` stands as the record of what Prompt 12C was authorized to touch, and the audit trail for the repair is the inventory, not this sentence.
9. **12C does not authorize Prompt 13, 14 or 15**, does not close 12B-C1, and does not reopen R8.
