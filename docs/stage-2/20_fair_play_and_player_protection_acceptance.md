# B-12 acceptance framework, ten-area coverage and verification plan

**Version:** 1.0 · **Created:** 2026-11-07 · **Stage 2, Prompt 12B**
**Status:** **Acceptance framework complete at the documentation level. No gate here is runtime evidence, and no gate is upgraded by the existence of a document.**
**Authority.** This document grades the B-12 specification set: the [B-12 rulebook](20_fair_play_and_player_protection.md), the [B-12 formula and parameter register](20_fair_play_and_player_protection_formula_register.md) and the [B-12 requirement register](20_fair_play_and_player_protection_requirements.md). It owns the gate definitions and the coverage matrices. It does not own a rule, a formula, a requirement or a decision.
**Companions.** [B-12 rulebook](20_fair_play_and_player_protection.md) · [B-12 formula register](20_fair_play_and_player_protection_formula_register.md) · [B-12 requirements](20_fair_play_and_player_protection_requirements.md) · [12A research](research/12A_fair_play_privacy_moderation_administration_research.md) · [12A source and benchmark register](research/12A_sources_and_benchmarks_register.md) · [12A requirements, integration and risk registers](research/12A_requirements_integration_and_risk_registers.md) · [requirements](03_requirements_traceability.md) · [decisions](../DECISIONS.md) · [mirrored decisions](04_approved_and_provisional_decisions.md) · [unresolved decisions](05_unresolved_design_decisions.md) · [Stage 2 handoff](00_stage_2_handoff.md) · [roadmap](01_stage_2_prompt_roadmap.md) · [progress log](06_stage_2_progress_log.md) · [`12B_validate_b12.py`](../qa_backups/12B_validate_b12.py).

**What this document is not.** It is not a security test, privacy audit, legal opinion, penetration test, fault-injection run, moderation drill, appeal-overturn measurement, database test or implementation review. A `PASS` below means the documentary criterion is satisfied by an artefact that exists and resolves. It does not mean a control works, a threshold is calibrated, a duty is discharged, a player is protected or a system is compliant. **Documentation validation is not runtime verification.**

---

## 1. Grading rules

### 1.1 Statuses

The six statuses are the ones the brief allows.

| Status | Meaning |
|---|---|
| `PASS` | The documentary evidence exists, resolves, and demonstrates the stated criterion. |
| `PARTIAL` | Part of the evidence exists; the missing element and its owner are named in the same row. |
| `FAIL` | The criterion is contradicted by the artefacts. |
| `BLOCKED` | The criterion cannot be assessed without an owner, legal or downstream action. |
| `NOT RUN` | The method exists and has not been executed. |
| `NOT APPLICABLE` | The criterion does not apply to a documentation-stage deliverable. |

No gate is graded on intention, on a rule's existence elsewhere in the corpus, or on the validator passing. A gate is never raised because a later prompt is expected to satisfy it.

### 1.2 What counts as evidence

Acceptable evidence is one of: a normative rule with a resolvable identifier; a formula record with all twenty mandatory fields; a requirement row with a status, a verification method and a dependency; a named decision with an ID; a register audit whose counts reconcile; or a validator check that parses the artefact rather than searching for a heading. Prose that asserts a control exists is not evidence of the control.

### 1.3 Prohibited grading shortcuts

The following never raise a gate:

- a document saying a control is "planned", "designed", "specified" or "required";
- the same claim repeated in two documents;
- a `MUST` without an owner, a verification method or a dependency;
- a validator check that only confirms a heading is present;
- a prototype file existing without a passing test;
- a later prompt being expected to implement the item.

---

## 2. Gate register

**Tally: 23 `PASS` · 3 `PARTIAL` · 0 `FAIL` · 0 `BLOCKED` · 0 `NOT RUN` · 0 `NOT APPLICABLE`.**

The three `PARTIAL` rows are `P12B-14` (no audit implementation exists to verify), `P12B-16` (prototype privilege and audit defects remain open) and `P12B-23` (project-wide synchronization is completed in this pass but includes the pre-existing `D-1` legacy validator debt). Each names its missing evidence and owner. No row is `BLOCKED` because the documentation-stage deliverable did not require an owner ruling to be written; the twenty owner/legal-dependent requirements are recorded as **Open** inside the register rather than hidden behind a blocked gate.

| Gate | Acceptance criterion | Evidence | Exact file and section | Verification method | Result | Remaining limitation | Required action |
|---|---|---|---|---|---|---|---|
| `P12B-01` | Authority, scope and non-claims are stated and preserved decisions are unchanged | Header authority block; `FP-001`–`FP-010`; preserved-authority paragraph | rulebook header, §1; §18–§19 | validator `12B-01`, `12B-02`, `12B-28`; D/DD cross-check | **PASS** | The statement is documentary; it cannot prevent a later prompt from over-claiming | 12C inherits the non-claim list and must not delete it |
| `P12B-02` | All ten Prompt 12B areas have normative rules, an owning section and a requirement path | 344 rules across thirteen prefixes; ten-area matrix §3; 106 requirement rows | rulebook §§2–19, Annex E; requirements §§2–3; this document §3 | validator `12B-03`, `12B-04`, `12B-05`, `12B-24` | **PASS** | Coverage is coverage of text; no rule is implemented | Stage 5 implements; 12C maps workflows |
| `P12B-03` | One violation taxonomy exists with all required elements and no catch-all | 16 `V-` classes × 11 elements; `FP-017`–`FP-035`; non-examples and legitimate alternatives present | rulebook §3, Annex A | validator `12B-06`, `12B-07`, `12B-09` | **PASS** | Severity bands are ordinal design choices, not calibrated measurements | Prompt 14 calibrates; owner confirms `UD-053` |
| `P12B-04` | Evidence states and consequence ceilings are explicit, and no score or automated finding exists | `EVD-001`–`EVD-009`; corroboration matrix `EVD-010`–`EVD-018`; `F-FP-007` | rulebook §2, §6; formula register `F-FP-007` | validator `12B-10`, `12B-11`, `12B-12` | **PASS** | The matrix is a design rule; no case has been run through it | 12C writes case fixtures; Stage 5 implements the gate |
| `P12B-05` | Multi-account and collusion policy separates evidence, legitimate cooperation and the accepted identity residual | `MA-001`–`MA-012`, `CO-001`–`CO-010`; `FP-018`; `EVD-006`; `REQ-777`–`REQ-789` | rulebook §4; requirements rows | validator `12B-13`, `12B-14` | **PASS** | Identity-layer multi-accounting remains undetectable and the residual is not a control | Owner must accept the residual in writing before a launch claim (`UD-052`, `UD-053`) |
| `P12B-06` | Exploitation, automation and forbidden assistance are defined without inventing detection capability | `EX-001`–`EX-012`; `V-12`; `FP-028`; rate and idempotency boundaries | rulebook §5; §13 | validator `12B-15` | **PASS** | No detector exists; the rules describe offences and evidence paths only | Stage 5 detection work; 12C test design |
| `P12B-07` | Privacy classification, actor permissions and disclosure limits are specified on the three axes | `PRV-001`–`PRV-025`; Annex B nine classes and eight actors; `REQ-798`–`REQ-810` | rulebook §7, Annex B; requirements rows | validator `12B-16`, `12B-17`, `12B-18` | **PASS** | Retention periods remain unset because `UD-055` and `UD-017` are open | Legal/owner ruling; `FP-P11` stays unset |
| `P12B-08` | Moderation powers are enumerated, bounded and reversible where the evidence state permits | `MOD-001`–`MOD-035`; `EVD-002`; emergency limits `MOD-025`–`MOD-028` | rulebook §8 | validator `12B-19`, `12B-20` | **PASS** | Powers are specified; no tool, queue or staffing model exists | 12C workflow and Prompt 13 surface; owner staffing plan (`UD-054`) |
| `P12B-09` | One conduct ladder exists with authority and evidence per tier, and the subsystem-rule boundary is stated | `MOD-036`–`MOD-041`; `FP-025`, `FP-031`, `FP-032`; `REQ-812`, `REQ-813` | rulebook §9; formula `F-FP-001`, `F-FP-011` | validator `12B-21`, `12B-22` | **PASS** | No tier duration or penalty amount is approved; the B-11 interplay is stated, not tested | Owner decision `UD-053`; Prompt 14 calibration |
| `P12B-10` | Appeal architecture is complete and no deadline or budget is invented | `MOD-042`–`MOD-050`; `F-FP-006`; `REQ-833`–`REQ-837` | rulebook §9; formula register | validator `12B-23`, `12B-24` | **PASS** | Filing window, decision target and budget are undefined under `UD-059` | Owner decides `UD-059`; no queue estimate may be presented as measured |
| `P12B-11` | Administrative roles, prohibition list and separation of duties are specified | Eight roles × eleven fields; `ADM-001`–`ADM-030`; Annex C; `REQ-838`–`REQ-846` | rulebook §10, Annex C | validator `12B-25`, `12B-26` | **PASS** | A single-operator service cannot prove segregation; the substitute is disclosure | Owner staffing decision `UD-054`; 12C labels unsegregated cases |
| `P12B-12` | Corrections, reversals, compensation and recovery are separated from sanctions | `COR-001`–`COR-018`; `MOD-051`–`MOD-060`; six transaction types; conservation identity | rulebook §12; formulas `F-FP-002`–`F-FP-004`, `F-FP-014`, `F-FP-015` | validator `12B-27`, `12B-29` | **PASS** | No ledger has been tested against `F-FP-014`; caps and valuation are provisional | Stage 5 ledger tests; owner policy for compensation |
| `P12B-13` | Evidence handling, provenance, custody and retention are specified | `EVD-019`–`EVD-042`; chain-of-custody rules; evidence retention and redaction | rulebook §11 | validator `12B-30`, `12B-31` | **PASS** | The rules describe records and custody events; no evidence store exists | Stage 5 schema; 12C case fixtures |
| `P12B-14` | Audit spine and tamper-evidence obligations are specified | `EVD-030`–`EVD-034`, `SEC-038`; `F-FP-012`, `F-FP-013`; `REQ-828`, `REQ-829` | rulebook §11, §14; formula register | validator `12B-32`, `12B-33` | **PARTIAL** | Nothing is implemented or verified: no chained digest, no verification job, no protective `audit` trigger and no executed verification run. The candidate design is not a control | Stage 5 implementation plus an executed verification run; 12C grades only against that run |
| `P12B-15` | Anti-exploit controls and security/accounting boundaries are stated without claiming Supabase enforcement | `SEC-001`–`SEC-030`; `FP-011`–`FP-016`; `REQ-764`–`REQ-776`, `REQ-859`–`REQ-865` | rulebook §13, §16 | validator `12B-34`, `12B-35` | **PASS** | Server authority and single-writer rules are design obligations; the prototype does not satisfy them | Stage 5 schema and transaction review |
| `P12B-16` | Supabase and audit obligations, including known prototype defects, are recorded honestly | `SEC-031`–`SEC-040`; §14 defect statement; `REQ-805`, `REQ-829` | rulebook §14; 12A report §4.1, §19 | validator `12B-36`, `12B-37` | **PARTIAL** | The prototype still grants table-wide authenticated `UPDATE` on `feasibility.profiles` including `treasury`; no `0005` profile-permission migration, no `tests/sql/` permission tests, no protective `audit` trigger and no executed tamper-evidence job exist. None of this is fixed by 12B | Stage 5 column-level privilege correction, SQL permission tests, audit-spine verification; no claim of fix is permitted before that run |
| `P12B-17` | Failure and recovery postures are per category with no universal fail-open or fail-closed rule | `FR-001`–`FR-015`; Annex D; `REQ-862`–`REQ-865` | rulebook §15, Annex D | validator `12B-38`, `12B-39` | **PASS** | Postures are designs; none has been exercised under fault injection | Stage 5 fault injection; 12C recovery tests |
| `P12B-18` | Cross-system contracts exist for every affected subsystem | `INT-001`–`INT-020`; ownership and non-ownership statements; `REQ-859`–`REQ-861` | rulebook §16 | validator `12B-40`, `12B-41` | **PASS** | Contracts are policy interfaces, not API definitions | Prompt 13 and Stage 5 translate them into surfaces and schemas |
| `P12B-19` | Formula and parameter governance is complete, with twenty fields per formula and six value classes | 16 formula records × 20 fields; `FP-P01`–`FP-P14`; six classes stated in the register header | formula register §§1–4 | validator `12B-42`–`12B-45`, `12B-67`–`12B-68`, `12B-75` | **PASS** | No value is calibrated or approved; seven formulas carry provisional parameters | Prompt 14 calibration; owner decisions `UD-053`, `UD-056`, `UD-059` |
| `P12B-20` | Every requirement is traceable, dispositioned and free of duplicate IDs | 106 rows from 106 candidates; 86 Provisional, 20 Open; zero duplicates, zero untraced | requirements §§1–4 | validator `12B-46`–`12B-50` | **PASS** | All 106 are text obligations; none is implemented or tested | Stage 5 implementation; 12C acceptance tests |
| `P12B-21` | Owner-reserved and legal dependencies remain unresolved and correctly referenced | 20 Open requirement rows; `UD-017`, `UD-052`–`UD-060` preserved; no owner decision invented | requirements §4; rulebook preserved-authority paragraph | validator `12B-51`, `12B-52` | **PASS** | Twenty requirements cannot close until external rulings exist | Owner and counsel; re-check before any launch claim |
| `P12B-22` | Ten B-12 decisions are recorded with alternatives, evidence and consequences and mirrored in the DD register | `D-178`–`D-187`; `DD-226`–`DD-235`; tally 235 | `DECISIONS.md`; `04` §6 | validator `12B-53`, `12B-54`; `test_decision_registers` | **PASS** | They are Category B design decisions, not owner-approved policy and not implementation | None for 12B; 12C consumes them |
| `P12B-23` | Project-wide documentation is synchronized to the B-12 frontier | Status files, roadmap, progress log §75, handoff, outline, traceability, AI context | `PROJECT_PROGRESS.md`, `ROADMAP.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `00`–`06`, `01` | validator `12B-55`, `12B-56`; link gate; `09_validate.py`; unit tests | **PARTIAL** | All live status surfaces are updated in this pass, but the project retains pre-existing validator debt `D-1` (11A check 29 expects `REQ-703`) and the broken Stage-1 sweep tools recorded under `D-10`; neither is B-12 evidence | A frontier-refresh pass owns `D-1` and `D-10`; 12B does not disguise them |
| `P12B-24` | The independent validator and its fixtures pass against the delivered corpus | `12B_validate_b12.py` with structural, referential, governance and honesty checks; positive and negative fixtures | `qa_backups/12B_validate_b12.py`; this document §9 | run the validator, `--self-test`, `--verbose`, `--fixtures` | **PASS** | It is a document checker; it proves nothing about a control's behaviour and does not replace the project's regression suite | 12C extends it; it is never a security test |
| `P12B-25` | The Prompt 12C boundary is respected: no journeys, workflow library or 12C acceptance package is written | `GOV-021`–`GOV-025`; §19 handoff; this document §8 | rulebook §19 | validator `12B-57`, `12B-58` | **PASS** | 12C remains unwritten and unauthorized; this gate checks absence, not readiness | Prompt 12C needs separate owner authorization |
| `P12B-26` | No implementation, deployment, migration, test-execution or legal-compliance claim is made | Non-claim blocks in all four documents; `FP-008`, `REQ-866`; validator honesty scan | all four B-12 documents | validator `12B-59`, `12B-60` | **PASS** | The corpus can still be misread by a later session; the repeated non-claims are the mitigation | Every later prompt re-checks the honesty scan |

---

### 2.1 Prompt 12B-C1 reassessment (2026-11-07)

The independent audit identified formula, parameter and integration-mapping defects. Each affected gate was reassessed against the corrected artefacts. No gate was upgraded because a document improved; the classifications below rest on the corrected specification and the new validator checks. The three existing PARTIAL gates are unchanged because their missing evidence is implementation or external ruling, not documentation.

| Gate | Original | Corrected | Evidence | Remaining limitation | Prompt 12C verification | Implementation testing |
|---|---|---|---|---|---|---|
| `P12B-12` | PASS | PASS | `F-FP-002` direction and examples corrected; `F-FP-014` signed convention and `ADMIN_ADJUSTMENT` term added; `COR-003` aligned | No ledger has been executed | Correction/reversal case fixtures | Stage 5 ledger reconciliation against `F-FP-014` |
| `P12B-18` | PASS | PASS | Acceptance §5 mapping corrected to canonical B-system/INT associations; rulebook §16.1 states all seven dependency fields | Contracts are policy interfaces, not APIs | Workflow-to-contract traceability | Stage 5 interface tests |
| `P12B-19` | PASS | PASS | `F-FP-001`/`F-FP-011` repetition counted once; `FP-P13`/`FP-P14` registered; formula-to-parameter mapping complete | No value calibrated; `w` and `f` undefined | Parameter-handoff fixtures | Prompt 14 calibration; Stage 5 load test |
| `P12B-20` | PASS | PASS | Requirement identities preserved; formula and integration references updated without renumbering | All 106 remain text obligations | Requirement-to-workflow ledger | Stage 5 implementation tests |
| `P12B-14` | PARTIAL | PARTIAL | Audit spine still unimplemented | No chained digest, verification job or protective trigger exists | Grade only against an executed run | Stage 5 implementation + verification run |
| `P12B-16` | PARTIAL | PARTIAL | Prototype defects still disclosed, not fixed | `profiles` grant, `0005`, SQL tests, audit trigger absent | Grade only against SQL permission tests | Stage 5 privilege correction and tests |
| `P12B-23` | PARTIAL | PARTIAL | Synchronization completed; legacy `D-1`/`D-10` debt remains | 11A check 29 and Stage-1 sweep tools unfixed | Not a 12C gate | Frontier-refresh pass |

The tally remains **23 PASS / 3 PARTIAL / 0 FAIL / 0 BLOCKED / 0 NOT RUN / 0 NOT APPLICABLE**, recomputed from the gate records by the validator.

---

## 3. Ten-area coverage matrix

Every area named in Prompt 12B §7 has normative rules, at least one formula or structural calculation where a calculation is needed, a requirement path and a cross-system contract. "Rules" counts parsed `**PREFIX-nnn — Title.**` definitions, not prose mentions.

| # | Prompt 12B area | Owning rules | Count | Calculation | Requirement range/path | Contract | Gate |
|---|---|---|---|---|---|---|---|
| 1 | Fair-play rules and violation classification | `FP-011`–`FP-035`; Annex A `V-01`–`V-16` | 25 + 16 classes | `F-FP-001`, `F-FP-011` | `REQ-777`–`REQ-798`, `REQ-811`–`REQ-814` | `INT-001`, `INT-002` | `P12B-03` |
| 2 | Abuse detection, investigation and enforcement | `EVD-010`–`EVD-025`; `EX-001`–`EX-012` | 16 + 12 | `F-FP-007`, `F-FP-008` | `REQ-767`, `REQ-790`–`REQ-797`, `REQ-822`–`REQ-829` | `INT-002`, `INT-006`, `INT-017` | `P12B-04`, `P12B-06` |
| 3 | Privacy permissions and data visibility | `PRV-001`–`PRV-025`; Annex B | 25 + 9 classes / 8 actors | — (classification, not a formula) | `REQ-774`, `REQ-798`–`REQ-810` | `INT-011`, `INT-012`, `INT-020` | `P12B-07` |
| 4 | Moderation powers and restrictions | `MOD-001`–`MOD-035` | 35 | `F-FP-016` (emergency expiry) | `REQ-811`–`REQ-821`, `REQ-847`–`REQ-850` | `INT-001`, `INT-002` | `P12B-08` |
| 5 | Administrative roles and permissions | `ADM-001`–`ADM-030`; Annex C | 30 + 8 roles | — (permission matrix) | `REQ-838`–`REQ-846` | `INT-014`, `INT-015`, `INT-020` | `P12B-11` |
| 6 | Disciplinary actions and appeals | `MOD-036`–`MOD-060` | 25 | `F-FP-001`, `F-FP-005`, `F-FP-006`, `F-FP-011` | `REQ-812`–`REQ-813`, `REQ-833`–`REQ-837` | `INT-003`, `INT-018` | `P12B-09`, `P12B-10` |
| 7 | Evidence handling and audit | `EVD-019`–`EVD-042`; `SEC-031`–`SEC-040` | 24 + 10 | `F-FP-012`, `F-FP-013` | `REQ-826`–`REQ-832`, `REQ-851`–`REQ-858` | `INT-014`, `INT-017` | `P12B-13`, `P12B-14` |
| 8 | Penalties, reversals and recovery | `COR-001`–`COR-018`; `MOD-051`–`MOD-060` | 18 + 10 | `F-FP-002`–`F-FP-004`, `F-FP-014`, `F-FP-015` | `REQ-817`–`REQ-820`, `REQ-836`, `REQ-845` | `INT-003`, `INT-004` | `P12B-12` |
| 9 | Anti-exploit controls | `SEC-001`–`SEC-030`; `FP-011`–`FP-016` | 30 + 6 | `F-FP-009`, `F-FP-010` | `REQ-764`–`REQ-776` | `INT-006`, `INT-013`, `INT-015`, `INT-016` | `P12B-15` |
| 10 | Security/accounting boundaries with Supabase and audit integrity | `SEC-031`–`SEC-040`; `INT-001`–`INT-020` | 10 + 20 | `F-FP-012`, `F-FP-013` | `REQ-805`, `REQ-828`–`REQ-831`, `REQ-859`–`REQ-865` | `INT-003`, `INT-014`, `INT-015` | `P12B-16`, `P12B-18` |

**Counts reconcile with Annex E.** The rule total is 344: `FP` 35, `EVD` 42, `MA` 12, `CO` 10, `EX` 12, `PRV` 25, `MOD` 60, `ADM` 30, `COR` 18, `SEC` 40, `INT` 20, `FR` 15, `GOV` 25. The ten-area matrix intentionally reuses prefixes across areas; the counts in this table are the area's owning subset, not a second rule inventory.

---

## 4. Requirement coverage

### 4.1 By type and priority

All 106 rows come from the 106 `12A-CR` candidates in candidate order: `REQ = 763 + CR`. No candidate is dropped, duplicated or renumbered.

| Dimension | Values |
|---|---|
| Total | **106** (`REQ-764`…`REQ-869`) |
| Type | Operations 33 · Security 20 · Governance 20 · Privacy 18 · Policy 9 · Reliability 6 |
| Priority | A 49 · B 55 · C 2 |
| Status | Provisional 86 · **Open** 20 · Approved 0 · Deferred 0 · Proposed 0 |
| Rule reference | 106 of 106 name at least one structural rule |
| Direct formula reference | 4 rows (`REQ-771`, `REQ-823`, `REQ-829`, `REQ-847`) |
| Named by a formula | 27 rows across the 16 formulas |
| Owner/legal dependency | 20 rows |
| Downstream-only dependency | 5 rows (`REQ-773`, `REQ-789`, `REQ-807`, `REQ-810`, `REQ-829`) |
| Untraced | 0 |
| Duplicate IDs | 0 |

### 4.2 Open rows and their owners

No row in this table is closed by Prompt 12B. Each remains an owner or legal question with a named dependency.

| Requirement | Dependency | What remains unanswered |
|---|---|---|
| `REQ-782` | `UD-052` | Whether value may be corrected against either or both sides of a beneficial flow |
| `REQ-795` | `UD-054` | Whether a reviewer with a declared interest can be replaced at current staffing |
| `REQ-808` | `UD-055` | Final retention periods per class |
| `REQ-809` | `UD-017`, `UD-055` | How erasure and the permanent audit spine reconcile |
| `REQ-812` | `UD-053` | Final tier definitions and durations |
| `REQ-816` | `UD-053` | Whether any penalty amount or duration is approved |
| `REQ-817` | `UD-052` | The boundary between correction and sanction in the owner's policy |
| `REQ-830` | `UD-055` | Legal-deletion handling for case evidence |
| `REQ-831` | `UD-055` | Evidence minimisation and retention limits |
| `REQ-837` | `UD-054` | Which independence guarantees exist at the current staffing level |
| `REQ-842` | `UD-054` | Second-approval availability for self-dealing |
| `REQ-843` | `UD-054` | Whether investigation and decision can be separated |
| `REQ-844` | `UD-054` | Whether configuration author and publisher can be separated |
| `REQ-846` | `UD-054` | The compensating control where separation is impossible |
| `REQ-849` | `UD-056` | Retrospective review authority for emergency actions |
| `REQ-855` | `UD-017`, `UD-055` | Audit correction and obligation-deletion authority |
| `REQ-857` | `UD-017` | Breach-assessment and notification obligations |
| `REQ-867` | `UD-053` | Review cadence for enforcement capacity and false-positive rates |
| `REQ-868` | `UD-058` | Whether a public transparency report is published |
| `REQ-869` | `UD-017` | Which legal dependencies bind the design |

### 4.3 Disposition audit

| Disposition | Count | Meaning |
|---|---|---|
| Adopted | 106 | Converted one-to-one into a normative `REQ-` row |
| Adapted | 0 | No candidate required rewording beyond normative form |
| Merged | 0 | No two candidates addressed the same obligation |
| Rejected | 0 | No candidate was outside B-12 scope |
| Deferred | 0 | Deferral would hide an obligation; owner-dependent rows are **Open**, not deferred |

The 12A rejection log already records 22 candidates rejected *during research*. Those are not part of the 106; no second rejection is invented here.

---

## 5. Cross-system dependency coverage

### 5.1 Canonical system-to-contract mapping

Verified against the rulebook §16 contracts and the canonical B-system definitions. The earlier 12B table mis-assigned several systems; this is the corrected mapping.

| System | Canonical owner | Integration contracts | What B-12 does not do |
|---|---|---|---|
| B-02 turn engine and audit spine | B-02 | `INT-013`, `INT-014`, `INT-012` | Does not alter phases, cadence or the spine implementation |
| B-03 accounts and lifecycle | B-03 | `INT-001`, `INT-016` | Does not re-parent a nation or apply a restriction itself |
| B-04 economy and treasury | B-04 | `INT-003` | Does not write a balance or mint compensation |
| B-05 cities and research | B-05 | `INT-004` | Does not edit infrastructure, capacity or research state |
| B-06 politics | B-06 | `INT-005` | Does not set a political state or overturn an election |
| B-07 markets | B-07 | `INT-006` | Does not resolve a trade, order or price |
| B-08 diplomacy | B-08 | `INT-007` | Does not alter treaties or pair state |
| B-09 alliances | B-09 | `INT-008` | Does not appoint officers, edit membership or self-adjudicate |
| B-10 warfare | B-10 | `INT-009` | Does not recompute a battle, campaign or standing |
| B-11 world events and objectives | B-11 | `INT-010` | Does not grant, remove or reroll an objective reward |
| B-11 rankings and progression | B-11 | `INT-011` | Does not change a snapshot, honour or chronicle entry |
| Enforcement target record | B-12 | `INT-002` | Does not express a sanction as a nation or pair field |
| Stage 6 authentication | Stage 6 | `INT-015` | Holds no credential and implements no auth flow |
| Reporting tooling | B-12 | `INT-017` | Does not expose reporter identity |
| Appeals | B-12 | `INT-018` | Does not decide an Alliance expulsion appeal (`UD-044`) |
| Prompt 14 balance | Prompt 14 | `INT-019` | Chooses no numeric value |
| Prompt 13 interface and owner governance | Prompt 13 / owner | `INT-020`, `INT-012` | Designs no screen and closes no owner decision |

### 5.2 Consolidated dependency traceability

The seven normative fields (boundary, data/authority, invariant, security, ownership, Prompt 12C work, implementation dependency) are stated per contract in rulebook §16.1. This table adds the requirement, decision and status linkage. Every row is specification-level; none is an executed integration.

| Contract | Source → target | Requirements | Decisions | Data / authority | Invariant | Security | Owner | 12C work | Implementation | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `INT-001` | B-12 → B-03 | `REQ-777`, `779`, `780`, `818` | `D-018`, `D-031`, `D-169` | Restriction request | Only B-03 applies it | Audited request | B-03 | Request/response mapping | Stage 5 schema | Specified |
| `INT-002` | B-12 → action record | `REQ-818`, `819` | `D-165` | Enforcement target | Account-level only | No cross-object write | B-12 | Record shape | Stage 5 record | Specified |
| `INT-003` | B-12 → B-04 | `REQ-817`, `836`, `845` | `D-184`, `D-064` | Correction instruction | Ledger appends | Reason code; idempotency | B-04 | Correction/reversal workflow | Stage 5 ledger | Specified |
| `INT-004` | B-12 → B-05 | `REQ-819`, `860` | `D-064` | City/research state | Owner-path correction | Purpose-bound read | B-05 | Evidence/correction mapping | Stage 5 schema | Specified |
| `INT-005` | B-12 → B-06 | `REQ-860`, `861` | `DMP-267` | Political state | Never a sanction | Restricted read | B-06 | Read-boundary mapping | Stage 5 schema | Specified |
| `INT-006` | B-12 → B-07 | `REQ-786`, `791` | `D-170` | Settlements; `MKT-S` | Signal opens review | No public trade feed | B-07 | Signal-to-review handoff | Stage 5; Prompt 14 | Specified |
| `INT-007` | B-12 → B-08 | `REQ-781`, `860` | `D-172` | Treaty records | Read-only | Audited read | B-08 | Restricted-history mapping | Stage 5 schema | Specified |
| `INT-008` | B-12 → B-09 | `REQ-784`, `788` | `D-170` | Alliance data | No self-adjudication | Platform readership | B-09 | Evidence/enforcement boundary | Stage 5; `UD-046` | Specified |
| `INT-009` | B-12 → B-10 | `REQ-860` | `D-161` | Warfare records | No recomputation | Evidence only | B-10 | Evidence receipt mapping | Stage 5 records | Specified |
| `INT-010` | B-12 → B-11 | `REQ-860`, `861` | `D-154` | Event/objective state | B-11 flags only | No reward grant | B-11 | Flag-to-case handoff | Stage 5 records | Specified |
| `INT-011` | B-12 → B-11 | `REQ-803`, `868` | `D-027` | Snapshots/honours | `k ≥ 5` kept | No composite leak | B-11 | Manipulation-evidence mapping | Stage 5; `UD-050` | Specified |
| `INT-012` | B-12 → B-02/Prompt 13 | `REQ-803`, `850` | `D-017` | Notice content | Class-bounded disclosure | No third-party state | B-02/Prompt 13 | Content-to-surface mapping | Prompt 13 | Specified |
| `INT-013` | B-12 → B-02 | `REQ-770`, `771`, `858` | `D-025` | Turn ledger | Incident unless evidenced | No silent re-derivation | B-02 | Incident/delay mapping | Stage 5 engine | Specified |
| `INT-014` | B-12 → B-02 spine | `REQ-828`, `829`, `851` | `D-174` | Event shape; chain | Append-only + verification | Restricted readership | B-02/B-12 | Verification-failure path | Stage 5 + executed run | Specified; unimplemented |
| `INT-015` | B-12 → Stage 6 | `REQ-769`, `840` | `D-032` | Sessions; events | No credential held | Step-up | Stage 6 | Step-up/failure mapping | Stage 6 | Specified |
| `INT-016` | B-12 → B-03 | `REQ-775`, `778` | `D-168` | Keyed digest | Triage only | No IP sanction | B-03 | Triage consumption mapping | Stage 5 custody | Specified |
| `INT-017` | B-12 reporting | `REQ-822`, `823`, `824` | `D-178` | Report records | Reporter hidden | Purpose-bound | B-12 | Intake/cluster mapping | Stage 5; `FP-P13` | Specified |
| `INT-018` | B-12 appeals | `REQ-833`–`837` | `D-185` | Appeal record | One appeal; four outcomes | No method disclosure | B-12 | Appeal/remand workflow | Stage 5; `UD-059` | Specified |
| `INT-019` | B-12 → Prompt 14 | `REQ-789`, `867` | `D-177` | Provisional values | No number chosen | No calibrated claim | Prompt 14 | Calibration handoff | Prompt 14 | Specified |
| `INT-020` | B-12 → Prompt 13/owner | `REQ-868`, `869` | `D-178` | Screens; governance | Structure only | Owner decisions open | Prompt 13/owner | Surface/governance mapping | Prompt 13; owner | Specified |

Every row is a policy interface. None is an API contract, and none is evidence that the interface exists. `INT-014` remains unimplemented and unverified; its gate is `P12B-14`.

---

## 6. Formula and parameter coverage

| Check | Result |
|---|---|
| Formula IDs | 16, active, unique, `F-FP-001`…`F-FP-016` |
| Mandatory fields per formula | 20 (purpose, inputs, units, expression, variables, constraints, boundary, rounding, null, exceptional, dependencies, worked example, verification, parameter status, owner, affected rules, affected requirements, revision, review trigger, approval) |
| Value classes | 6: Structural · Structural + provisional parameter · Provisional · Owner decision required · Legal review required · Capacity validation required |
| Structural, no unapproved constant | 5 (`F-FP-004`, `007`, `010`, `012`, `014`) |
| Structural + provisional parameter | 7 (`F-FP-001`, `002`, `003`, `008`, `009`, `011`, `016`) |
| Provisional | 3 (`F-FP-005`, `013`, `015`) |
| Owner decision required | 1 (`F-FP-006`) |
| Parameters registered | 14 (`FP-P01`…`FP-P14`), none calibrated |
| Undefined variables | 0 |
| Worked example present | 16 of 16 |
| Executed calculation | 0 — no formula has been run against data |

No formula is approved for implementation. A structural formula is a fixed algebraic form, not a validated model.

---

## 7. Evidence required at later stages

| Evidence | Stage/owner | Gates it would move | Why 12B cannot supply it |
|---|---|---|---|
| Column-level Supabase privileges and SQL permission tests | Stage 5 | `P12B-14`, `P12B-16` | 12B is forbidden to write migrations, RLS policies or grants |
| Chained-digest implementation and executed verification job | Stage 5 | `P12B-14` | No audit spine exists to verify |
| Protective trigger and append-only behaviour on the audit table | Stage 5 | `P12B-14`, `P12B-16` | Requires schema work outside 12B scope |
| Ledger conservation test against `F-FP-014` | Stage 5 | `P12B-12` | No ledger test harness exists |
| Case-record and evidence-store schema | Stage 5 | `P12B-13` | Schema is out of scope |
| Moderation, appeal and emergency workflows | Prompt 12C | `P12B-08`, `P12B-10` | At the 12B baseline 12C was unauthorized and its deliverables were prohibited in 12B's own documents; the owner subsequently authorized Prompt 12C and its documentation deliverables are complete (§8 and [`20_fair_play_and_player_protection_workflows.md`](20_fair_play_and_player_protection_workflows.md), [`…_integration.md`](20_fair_play_and_player_protection_integration.md), [`…_edge_cases_acceptance.md`](20_fair_play_and_player_protection_edge_cases_acceptance.md)), which still supplies no 12B evidence: specified acceptance tests are not executed production tests, and 12C owner acceptance remains pending |
| Disclosure-safe screens and response shapes | Prompt 13 | `P12B-07`, `P12B-18` | Interface design belongs to Prompt 13 |
| Calibrated weights, durations and caps | Prompt 14 / owner | `P12B-03`, `P12B-09`, `P12B-19` | 12B must not invent numbers |
| Legal and owner rulings on the 20 Open rows | Owner/counsel | `P12B-05`, `P12B-10`, `P12B-21` | 12B may not close owner-reserved decisions |

---

## 8. Prompt 12C handoff

*(Recorded at the 12B baseline, 2026-11-07: at that date Prompt 12C was **not started and not authorized**, and this section stated what it would have to add if ever authorized. That boundary statement is preserved and still means that no 12B document authorizes any later prompt.)* **Current state (2026-11-11):** the owner subsequently authorized Prompt 12C and its documentation work is complete — [`20_fair_play_and_player_protection_workflows.md`](20_fair_play_and_player_protection_workflows.md) (10 `FPJ-` journeys, 52 `FPW-` workflows), [`20_fair_play_and_player_protection_integration.md`](20_fair_play_and_player_protection_integration.md) (the twenty `INT-` contracts reused with none added, the thirty `12A-INT-` dependencies mapped, `C-01`/`C-02` and 10 `FPG-` gaps) and [`20_fair_play_and_player_protection_edge_cases_acceptance.md`](20_fair_play_and_player_protection_edge_cases_acceptance.md) (100 `FPE-` edge cases, 378 `FPA-` specifications, the 106-row `REQ-764`…`REQ-869` ledger with 0 orphans, 20 `P12C-` gates at 16 `PASS` / 2 `PARTIAL` / 2 `BLOCKED`) — so the six obligations below are now answered by specified documents, **not** by implemented or executed software, and owner acceptance of the 12C specification set remains pending. As specified, 12C had to add:

1. Player and moderator journeys for reporting, investigation, decision, sanction, correction, appeal, emergency action and restoration — with entry conditions, states, failure paths and exit conditions.
2. A workflow library for each moderation, administrative, correction and audit operation, including authority, evidence state, idempotency and audit event.
3. Operational sequence diagrams across B-02…B-11 and the Supabase boundary, at the level of policy interactions rather than API calls.
4. A full edge-case catalogue with an invariant per case, including conflicting corrections, duplicate reports, expired emergency powers, concurrent administrators and unsegregated appeals.
5. A 12C acceptance package with executed-test requirements — still not executed by 12C unless a build exists.
6. Traceability from every 12C workflow to the `REQ-` rows and `F-FP-` formulas it implements.

12C must not: create a second rule, invent a threshold, close an Open requirement, convert a `PARTIAL` gate to `PASS` without the named evidence, or claim that a workflow exists because it is specified.

---

## 9. Validator specification

`docs/qa_backups/12B_validate_b12.py` is a stdlib-only document validator in the house style (parsed tables, per-check results, fixtures, exit codes 0/1/2). It grades text and cross-references, not behaviour.

### 9.1 Check groups

| Group | Checks | What is measured |
|---|---|---|
| Corpus presence and header | `12B-01`–`12B-02` | Four documents exist; version, date, status and authority blocks are present; the non-claim sentence is present |
| Rule integrity | `12B-03`–`12B-09` | 344 definitions, contiguous per prefix, no duplicate, every rule has a title and body; 16 `V-` classes with 11 elements each; no seventeenth class |
| Evidence and ceilings | `12B-10`–`12B-15` | Five evidence states only; no sixth state; automated ceiling present; behavioural and network limits present; no confidence score |
| Privacy and roles | `12B-16`–`12B-26` | Nine privacy classes; eight actors; six actions; eight roles; prohibition list; no superuser; separation statements |
| Sanctions, appeals, corrections | `12B-21`–`12B-29` | Six tiers only; authority and evidence per tier; four appeal outcomes; six correction types; conservation identity |
| Audit and evidence lifecycle | `12B-30`–`12B-37` | Custody events; retention; redaction; digest construction; verification interval; prototype-defect disclosure; no tamper-evidence claim |
| Security and contracts | `12B-34`–`12B-41` | Server authority; single writer; rate and idempotency; 20 `INT-` contracts; ownership boundary |
| Formulas | `12B-42`–`12B-45`, `12B-67`–`12B-68`, `12B-75` | 16 formulas; 20 fields each; six value classes; 14 parameters (`FP-P01`–`FP-P14`); no undefined variable; no executed-calculation claim |
| Requirements | `12B-46`–`12B-52` | 106 rows; candidate pairing one-to-one; 86 Provisional / 20 Open; 20 `UD-` links; no Approved; no duplicate |
| Governance and honesty | `12B-53`–`12B-60` | `D-178`–`D-187` and `DD-226`–`DD-235` present; ten-row mirror; continuity names 12B and 12C; progress log §75; 12C boundary; no implementation, migration, test-execution or legal-compliance claim |
| Gate integrity | `12B-61`–`12B-62` | 26 gates with legal statuses only; the declared tally equals the parsed result column |
| Formula arithmetic and accounting | `12B-63`–`12B-66` | F-FP-002 direction and example arithmetic; F-FP-001 repetition-free; F-FP-011 sole repetition adjustment; F-FP-014 signed convention aligned with COR-003 |
| Parameter completeness | `12B-67`–`12B-68`, `12B-75` | FP-P13/P14 registered and referenced; unique parameter IDs; formula-to-parameter mapping covers all 16 formulas |
| Integration mapping and traceability | `12B-69`–`12B-71` | Canonical B-system/INT associations; seven dependency fields per contract; consolidated requirement/decision traceability |
| Archival and governance | `12B-72`–`12B-74` | Prompt archive exists, is indexed and referenced; truthful policy attestation; 12B-C1 gate reassessment preserves the three PARTIAL gates |
| Canonical integrity and structural validation | `12B-76`–`12B-78` | Canonical register defines a unique, well-formed, contiguous, ascending set discovered from every block kind; exactly one P12B-19 gate with complete occurrence scanning and no stale current-state claim; the **complete** current B-12 AI_CONTEXT entry (status record, continuation lines, inventory rows, attached paragraphs and sentences) is parsed and validated |
| Occurrence accounting | `12B-79`–`12B-83` | Policy-attestation line count; R1 manifest completeness; preserved historical records; **every** parameter-identifier occurrence in the acceptance document and the AI_CONTEXT B-12 entry keeps its file, section, line, span, original token, normalised identifier, statement, context, classification, order and outcome, and no namespace marker is unaccounted for |
| Definition discovery | `12B-84` | Every canonical definition candidate in the parameter-register region is discovered in tables, headings, list items and prose; a candidate count that differs from the accepted definition count, a definition record outside the region boundary, or an undeterminable boundary fails |
| Ambiguity and classification audit | `12B-85`–`12B-86` | No authoritative parameter-bearing record is left ambiguous (fail closed with a line-level diagnostic); every historical or superseded exemption is backed by a date, a past-tense predicate or an explicit supersession, never by a keyword alone |
| Representation equality | `12B-87` | Every authoritative current-state enumeration in the acceptance document and the AI_CONTEXT B-12 entry equals the single source-derived canonical collection, so no second hidden expectation can drift |

### 9.2 Fixtures

Positive fixtures assert that the checks pass on the unmutated corpus. Negative fixtures seed one corruption each and are accepted only when the named check fails for the expected reason. Since 12B-C1-R7 **every fixture runs the complete check registry** over an isolated corpus copy: a positive fixture must pass all checks with no exception, and a negative fixture must be rejected by the named check, for the named reason, by a validation decision rather than a crash. The suite ships **59 positive** and **153 negative** fixtures (**87 checks** total after 12B-C1-R7), including:

- a deleted rule (gap in a prefix sequence);
- a duplicated rule identifier;
- a seventeenth violation class;
- a sixth evidence state;
- a numeric confidence score;
- a behaviour-only finding;
- a network-only sanction above `T1`;
- a missing privacy class or actor;
- a ninth administrative role or a superuser claim;
- a seventh sanction tier;
- a fifth appeal outcome;
- a seventh correction type;
- a formula missing one of the twenty fields;
- a formula with an undefined variable;
- an owner-dependent requirement marked Approved;
- a duplicate requirement ID;
- a candidate dropped without disposition;
- `D-178`–`D-187` missing or a mirror row mismatched;
- an implementation or migration claim;
- a 12C workflow or journey present;
- a duplicated, missing, unexpected, reordered or malformed parameter identifier in any authoritative representation;
- a canonical definition duplicated in a heading, in prose, or across a table and a paragraph;
- a definition record outside the parameter-register boundary, an empty extraction, a missing register and an undeterminable region boundary;
- an AI_CONTEXT entry paragraph, continuation line or extra inventory row that states a conflicting or incomplete collection;
- an identifier split across a wrapped line, contaminated by a leading letter, or followed by punctuation;
- historical wording that disguises a present-state assertion, and an ambiguous colon enumeration with no completeness signal;
- legitimate dated historical records, explicitly superseded collections, historical comparisons, explanatory single-parameter references and canonical formatting variations, which must all still pass.

`python 12B_validate_b12.py --mutation-audit` reproduces the adversarial evidence the way an independent auditor does it: it copies every input file the validator reads into an isolated tree, applies one mutation to the file on disk, and runs the production validator as a subprocess, reporting the exit code and the rejecting check for each of the 23 audited mutations.

### 9.3 What the validator does not prove

It does not test RLS, grants, authentication, audit triggers, tamper-evidence, detection, moderation capacity, appeal execution, ledger conservation or legal compliance. It does not execute any formula. It does not certify that a reviewer read the corpus. Its `PASS` is a statement about document consistency, nothing more.

---

## 10. Limitations and residual risk

1. **No control exists.** Every rule in B-12 is a specification. The prototype demonstrates at least one privilege defect and no audit protection.
2. **No value is calibrated.** Six formulas are fully structural; the other ten contain at least one provisional, owner-required or legal element.
3. **Twenty requirements are Open.** They cannot be closed by documentation and must not be presented as resolved.
4. **Identity residual accepted, not solved.** `EVD-006` records an accepted critical residual; it is not a detection capability.
5. **Separations are disclosed, not proven.** A single-operator service cannot demonstrate segregation of duties; `MOD-049` and `REQ-837` require the label instead of the claim.
6. **No window or budget is invented.** `UD-059` remains open; no appeal queue estimate may be treated as measured.
7. **Legacy validator debt remains.** `D-1` (11A check 29) and `D-10` (broken Stage-1 sweep tools) predate B-12 and are not fixed here.
8. **Prompt 12B completion is documentary.** It does not authorize Prompt 12C, Stage 5 implementation, deployment or release.

---

## 11. Acceptance statement

At the documentation level, the B-12 specification set is internally consistent, traceable and honest about what it does not contain. It defines ten areas, 344 rules, 16 formulas, 14 uncalibrated parameters (`FP-P01`–`FP-P14`), 106 requirements and 26 gates. It records three `PARTIAL` gates whose missing evidence is implementation or external ruling. It does not claim that any fair-play control, privacy rule, moderation power, audit protection or Supabase permission is implemented, tested, running or legally sufficient.

**Specified ≠ implemented ≠ independently verified ≠ operating ≠ compliant.**