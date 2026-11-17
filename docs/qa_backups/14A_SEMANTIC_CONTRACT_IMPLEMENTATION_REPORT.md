# Prompt 14A — Semantic Contract Implementation and Controlled Validator Cutover

**Report type:** Independent QA implementation report (documentation/tooling level)
**Date:** 2026-11-16
**Starting audit baseline:** Project X (105)
**Governing policy:** D-014 — Autonomous Decision Policy (unmodified)
**Adoption decision:** D-238 — Controlled numerical-contract architecture (Category B, Confirmed)
**Canonical contracts:** `NC-F-EC-000b` and `NC-F-EC-000f`, contract version 1.0.0

> **Non-claims.** This report records executed documentation/tooling evidence. It does not prove gameplay, balance, simulation, runtime behaviour, human semantic judgment or owner acceptance. No human evidence reviewer has approved any mapping. No owner authorization was created. Prompt 14B is not authorized.

---

## 1. Scope and status

The assignment replaced the default-allow lexical semantic gate with typed, machine-readable contracts for the two controlled B-04 numerical clauses. The numerical foundation, all formula and parameter values, both B-04 source clauses and the production amendment manifest were preserved.

| Claim | Status |
|---|---|
| Implementation complete | **Yes** |
| Documentation complete for this pass | **Yes** |
| Validation passed at the documentation/tooling level | **Yes** |
| Owner acceptance | **PENDING — not requested and not granted** |
| Prompt 14A overall | **OPEN** |
| Prompt 14B | **NOT AUTHORIZED / NOT STARTED** |

The five claims are deliberately separate. A passing validator is not owner acceptance.

---

## 2. Files created

| # | Path | Purpose |
|---:|---|---|
| 1 | `docs/stage-2/22_numerical_contracts/index.json` | Contract registry, adoption decision, preserved baseline, source fingerprints, cross-cutting arithmetic authority |
| 2 | `docs/stage-2/22_numerical_contracts/schema.json` | Strict closed JSON schema and typed proposition vocabulary |
| 3 | `docs/stage-2/22_numerical_contracts/lexicon.json` | Canonical concepts, surface forms, modality and exception markers, unknown-term families |
| 4 | `docs/stage-2/22_numerical_contracts/F-EC-000b.contract.json` | Five typed propositions for integer arithmetic, rounding, representation, basis points and the unresolved cross-turn remainder |
| 5 | `docs/stage-2/22_numerical_contracts/F-EC-000f.contract.json` | Five typed propositions for constant classification, carry-forward, observed-price/balance-claim denial and revision authority |
| 6 | `docs/stage-2/22_numerical_contracts/evidence_mappings.json` | Eleven draft evidence mappings with source hashes, sections, excerpts, scope and honest `NOT_REVIEWED` status |
| 7 | `docs/stage-2/22_numerical_contracts/projections/F-EC-000b.md.tpl` | Deterministic projection template |
| 8 | `docs/stage-2/22_numerical_contracts/projections/F-EC-000f.md.tpl` | Deterministic projection template |
| 9 | `docs/qa_backups/14A_contract_validator.py` | Schema/semantic/evidence/authority validator, renderer, diff engine, ingest parser, production checks, seal mode |
| 10 | `docs/qa_backups/test_14A_contract_validator.py` | 83-test regression suite |
| 11 | `docs/qa_backups/14A_contract_fixtures/owner_authorization_TEST_FIXTURE.md` | Clearly labelled synthetic owner-authorization fixture; production mode rejects it |
| 12 | `docs/qa_backups/14A_SEMANTIC_CONTRACT_IMPLEMENTATION_REPORT.md` | This report |
| 13 | `docs/prompts/prompt_14A_semantic_contract_implementation.md` | Verbatim implementation-prompt archive |

---

## 3. Files modified

| # | Path | Change |
|---:|---|---|
| 1 | `docs/qa_backups/14A_validate_numerical_foundation.py` | Added contract integration; checks `14A-56`–`14A-64`; 12 contract self-tests; retired the lexical gate as acceptance; superseded the placeholder-A fixture |
| 2 | `docs/stage-2/22_formulas_and_balance.md` | Corrected §2.1 authority references; updated §12 current totals; marked §15.11 historical; added §18 superseding status and revision v1.1 |
| 3 | `docs/stage-2/22_numerical_baseline_qa_report.md` | Appended §8 superseding controlled-contract implementation record |
| 4 | `docs/stage-2/06_stage_2_progress_log.md` | Appended §108 implementation record |
| 5 | `docs/stage-2/01_stage_2_prompt_roadmap.md` | Updated the Prompt 14 row to OPEN / owner acceptance pending |
| 6 | `docs/DECISIONS.md` | Added D-238 (Category B, Confirmed); all historical rows preserved |
| 7 | `docs/AI_CONTEXT.md` | New current status entry; old completion claim marked historical; STATUS block updated (D-001…D-238) |
| 8 | `docs/AI_HANDOFF.md` | Current state, next action and STATUS block updated |
| 9 | `docs/PROJECT_PROGRESS.md` | Prompt 14 row and STATUS block updated |
| 10 | `docs/prompts/INDEX.md` | Added the implementation-prompt archive row and scope note |
| 11 | `docs/qa_backups/test_next_action.py` | Current-status expectation reconciled: Prompt 14A is OPEN, only Prompt 15 remains a bare Pending row |
| 12 | `docs/qa_backups/validate_final.py` | Added the spelled decision count “two hundred and thirty-eight” for the D-238 row (the file already carried pre-existing changes) |

The following working-tree changes shown by Git **predate this assignment** and were not made by it: `docs/ROADMAP.md`, `docs/qa_backups/09_validate.py`, `12A_validate_foundations.py`, `13A_validate_ui_foundations.py`, `13B_validate_ui_specifications.py`, `validate_final.py`, `docs/stage-2/00_stage_2_handoff.md`, `02_master_game_design_bible_outline.md`, `04_approved_and_provisional_decisions.md`, and the untracked Prompt 14A archives/artifacts created by earlier passes. They are recorded in §13 but are not part of this implementation's diff.

---

## 4. Architecture implemented

The authoritative path for a controlled clause is now:

1. **Typed contract** — the clause is a set of propositions with kind, subject, predicate, object, modality, polarity, scope, conditions, exceptions, units, timing, numeric representation, authority and source anchor.
2. **Deterministic projection** — the human-readable B-04 paragraph is rendered from the template and fragments; normalized output must equal the preserved clause byte-for-byte after normalization.
3. **100 % material coverage** — every structural sentence and every fragment must be consumed in order; missing or trailing material fails.
4. **Typed amendment** — a semantic change requires a candidate contract; the validator computes added, removed, changed and unchanged propositions and field-level paths.
5. **Evidence gate** — every changed proposition needs a governed, independently reviewed `SUPPORTS` mapping that matches the exact proposition, scope, source hash and excerpt.
6. **Authority gate** — every changed proposition needs an active, correctly scoped D-014 decision with the correct category and status; Category A/D additionally needs a traceable owner-instruction source and hash.
7. **Fingerprint gate** — canonical contract, rendered projection, source clause and evidence documents have separate SHA-256 fingerprints. A hash never overrides a semantic failure.
8. **Fail-closed ingestion** — raw prose is accepted only as a restatement of the same propositions; a semantic change must be expressed as a typed patch. Unknown material words fail.

The legacy lexical functions (`_semantic_contract_violation`, `_evidence_supports`) remain in the file as historical diagnostics. `_validate_source_contract` and `_validate_decision_record` no longer call them for acceptance. The positive test `test_contract_accepts_clarification_that_the_legacy_gate_rejects` proves the retired gate cannot block a typed-contract-valid clarification.

---

## 5. Contract schema and proposition model

### 5.1 Identity and lifecycle

Each contract records `schema_version`, `contract_id`, `clause_id`, `title`, `source_document`, `source_version`, `baseline_source_hash`, `contract_version`, `lifecycle_status`, `numerical_status`, `numerical_status_display`, `effective_decision`, `scope`, `propositions`, `change_policy` and `rendering`.

Contract lifecycle states (`SHADOW`, `ADOPTED`, `ADOPTED_PROVISIONAL`, `SUPERSEDED`, `RETIRED`) are separate from the preserved numerical-value vocabulary (`OWNER-APPROVED VALUE`, `PROVISIONAL VALUE`, `DESIGN PROPOSAL`, `NEEDS PLAYTESTING`) and the `UNSPECIFIED` absence marker.

### 5.2 Proposition fields

Every proposition carries a stable namespaced ID, a closed kind, typed subject/predicate/object, modality, polarity, explicit scope, typed conditions and exceptions, units and dimensions, timing and persistence, numeric representation/rounding/precision, authority metadata, a source anchor and status.

| Clause | Proposition | Meaning |
|---|---|---|
| F-EC-000b | P-001 | All quantities are integers (`MUST`) |
| F-EC-000b | P-002 | Every division states floor, ceil or round_half_up; floor is toward negative infinity for negative values |
| F-EC-000b | P-003 | Formula calculations `USES_REPRESENTATION BINARY_FLOATING_POINT` with modality `MUST_NOT` and polarity `AFFIRM` |
| F-EC-000b | P-004 | Percentages are integer basis points with `10,000 bp = 100%` |
| F-EC-000b | P-005 | Cross-turn fractional-remainder persistence is `NOT_ESTABLISHED` / `NEUTRAL`; distinct from within-turn cumulative accrual |
| F-EC-000f | P-001 | The constants are the v1.0 provisional calibration |
| F-EC-000f | P-002 | The v1.0 constants are carried unchanged into v1.1 (F-EC-044) |
| F-EC-000f | P-003 | The constants are not observed prices (`MUST_NOT`) |
| F-EC-000f | P-004 | The constants are not balance claims (`MUST_NOT`) |
| F-EC-000f | P-005 | A value change requires a new revision of the register |

### 5.3 P-003 correction

The proposal's illustrative `MAY_USE_REPRESENTATION` + `MUST_NOT` combination was not implemented. The adopted representation is one unambiguous negative proposition:

```
subject: FORMULA_CALCULATIONS
predicate: USES_REPRESENTATION
object: { type: REPRESENTATION_CLASS, value: BINARY_FLOATING_POINT }
modality: MUST_NOT
polarity: AFFIRM
```

`NEGATE` is rejected for every modality; negative meaning is carried only by `MUST_NOT`. The modality truth table covers `may`, `may not`, `not permitted`, `not prohibited`, `not not permitted`, `no`, `must not`, `must`, `prohibition`, ambiguity and double negation.

### 5.4 Scope

F-EC-000b is scoped to B-04, with B-09 explicitly excluded. The cross-cutting D-045/D-064 integer economic-arithmetic authority is a separate index proposition scoped to B-04 with `inheritance: NONE`; it is not extended to every register. P-005 lists `CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN` in `distinct_from`, and the lexicon keeps the two concepts separate. B-09 F-AL-006 remains valid and unchanged.

---

## 6. How evidence review works

The registry defines the **Independent Human Evidence Reviewer** role. Each mapping records:

- evidence ID, contract ID and proposition ID;
- document path, exact section, full-document SHA-256 and exact excerpt;
- scope and conditions;
- effective classification and proposed classification;
- reviewer identity, role, review date, review rationale and review status;
- implementation actor and `reviewer_independence_required: true`.

A changed proposition passes the evidence gate only when a mapping is `REVIEWED`, its effective classification is `SUPPORTS`, its reviewer is a real non-placeholder human who is not the implementation actor, its source hash/excerpt/section verify, and its scope covers the proposition. `CONTRADICTS`, `QUALIFIES`, `CONTEXT_ONLY`, `NOT_ESTABLISHED`, `INVALID_SOURCE`, `PARSE_FAILURE` and `NOT_REVIEWED` fail. Stale hashes, fabricated excerpts and partial coverage fail. An amendment cannot supply its own evidence mapping.

**Actual status:** 11 active production mappings, **0 REVIEWED**, **0 reviewed SUPPORTS**. All are `NOT_REVIEWED` drafts. No human reviewer identity was invented. Consequently no production amendment requiring evidence can pass. The positive evidence path is exercised only by clearly labelled synthetic test fixtures in test mode; production mode rejects fixture reviewers and fixture-only owner authorizations.

The cross-turn P-005 mapping is proposed `NOT_ESTABLISHED`; it can never count as support for an affirmative cross-turn permission.

---

## 7. How D-014 authority is enforced

The authority gate parses the eight-column `DECISIONS.md` table and checks, for every changed proposition:

- the decision exists exactly once and is not pending, rejected, deferred or superseded;
- the decision names the clause/contract;
- the category is explicit and matches the manifest;
- Category B is Confirmed and cannot change an owner-reserved proposition;
- Category C is Provisional, names the missing evidence or confirming test, keeps the contract `ADOPTED_PROVISIONAL`, and cannot promote a proposition to `RESOLVED`;
- Category A/D has an explicit owner status and a registry entry whose original instruction source exists, whose full SHA-256 matches, whose quoted instruction appears verbatim, and whose scope covers the proposition;
- typed amendments record previous and replacement contract IDs/versions, alternatives, rationale, governed evidence references, consequences and reopening conditions;
- authority-classification changes (including downgrading `owner_reserved`) require Category A;
- a proposition cannot cite the amendment decision as its own authority;
- decision status strings, manifest strings and contract metadata never authorize themselves.

Production has no owner-authorization registry entries, so **every Category A/D production amendment fails** with `CONTRACT_OWNER_AUTHORIZATION_MISSING`. The Category A positive fixture uses a synthetic instruction file marked `fixture_only: true`; production mode rejects it, and the test asserts that rejection. No owner authorization was created.

---

## 8. How unknown and contradictory material is rejected

| Situation | Error |
|---|---|
| Unknown field, enum, reference, missing metadata, incompatible subject/predicate/object, unit/dimension, timing or inheritance | `CONTRACT_SCHEMA_INVALID` |
| Unknown material term outside the lexicon | `CONTRACT_UNMAPPED_TERM` |
| Unconsumed, missing, ambiguous or trailing material | `CONTRACT_UNPARSED_MATERIAL_SEGMENT` |
| Rendered projection differs from the clause or template | `CONTRACT_PROJECTION_MISMATCH` |
| Permission/affirmative statement contradicts `MUST_NOT`, double negation, object change | `CONTRACT_PROPOSITION_CONFLICT` |
| Exception, conditional, subsystem permission or unknown exception effect | `CONTRACT_EXCEPTION_UNSUPPORTED` |
| Scope widening, cross-register leakage or wrong clause | `CONTRACT_SCOPE_MISMATCH` |
| No governed evidence mapping | `CONTRACT_EVIDENCE_MAPPING_MISSING` |
| Mapping not reviewed, placeholder/synthetic reviewer or unreviewed classification | `CONTRACT_EVIDENCE_NOT_REVIEWED` |
| Mapping targets a different proposition or narrower scope | `CONTRACT_EVIDENCE_PROPOSITION_MISMATCH` |
| Reviewed evidence is contradictory or not `SUPPORTS` | `CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS` |
| Stale evidence hash, fabricated quote or missing section | `CONTRACT_EVIDENCE_INTEGRITY_FAILED` |
| Wrong authority, category, status, scope, promotion or downgrade | `CONTRACT_AUTHORITY_MISMATCH` |
| Category A/D without authentic owner provenance | `CONTRACT_OWNER_AUTHORIZATION_MISSING` |
| Manifest supplies evidence/lexicon/allowlist or wrong hashes | `CONTRACT_MANIFEST_INVALID` / `CONTRACT_FINGERPRINT_MISMATCH` |

The prose path can accept a wording-only clarification with the same typed proposition set. Any semantic change requires a typed contract patch; raw prose cannot bypass the evidence and authority gates.

---

## 9. Mandatory negative cases

Each class has three materially different paraphrases. All fixtures use structurally valid manifests and hashes; the table records the primary semantic code. Secondary evidence codes are consequences of the semantic change, not structural rejection reasons.

| Case | Variant wording (abridged) | Accepted | Primary semantic code(s) |
|---|---|---|---|
| D-998 | “including derived calculations”; “including derived calculations and related calculations”; “including derived and downstream calculations” with unrelated fair-play evidence | No | `CONTRACT_EVIDENCE_PROPOSITION_MISMATCH` (all 3) |
| D-999 | “Binary floating point calculations are permitted.”; “Formula calculations may use binary floating-point representation.”; “Binary floating point is not prohibited.” | No | `CONTRACT_PROPOSITION_CONFLICT` (all 3); “contradicts” in the diagnostic |
| D-990 | Exact treasury/IEEE-754 exception; “An exception applies for IEEE-754 representation.”; “Only when the treasury subsystem calculates may it use an alternative representation.” | No | `CONTRACT_EXCEPTION_UNSUPPORTED` (all 3) |
| D-991 | Radix-two exponent/significand encoding; base-2 exponent/significand form; “two-part power-and-coefficient number layout” | No | `CONTRACT_PROPOSITION_CONFLICT` (1, 2); `CONTRACT_UNMAPPED_TERM` (3) |
| D-992 | Sign/exponent/mantissa fields; mantissa/exponent/sign components; three-field sign-mantissa-exponent tuple | No | `CONTRACT_PROPOSITION_CONFLICT` (all 3) |
| D-993 | “Residual sub-unit amounts between turns are preserved.”; “Sub-unit remainders carry across turns.”; “A leftover fraction from one turn is retained into the next turn.” | No | `CONTRACT_EVIDENCE_NOT_REVIEWED` plus `CONTRACT_UNPARSED_MATERIAL_SEGMENT` (typed patch required); no reviewed `SUPPORTS` mapping exists for P-005 |

The D-998 authorized-locus variant (B-14 §8.2 with an unrelated supports claim) is also rejected by `CONTRACT_EVIDENCE_PROPOSITION_MISMATCH` with “not substantiated” / “does not establish”. No variant is rejected by `CONTRACT_MANIFEST_INVALID` or `CONTRACT_FINGERPRINT_MISMATCH`.

---

## 10. Positive fixtures

| Fixture | Result | Conditions |
|---|---|---|
| Unchanged original baseline | **Accepted** | Projection equals the preserved clause; no amendment entry; manifest empty |
| Valid Category B wording clarification | **Accepted** | “The binary floating-point prohibition applies to every formula calculation.” Same proposition set; valid decision; governed context evidence |
| Valid Category B semantic change with genuinely supporting evidence | **Accepted** | Adds a derived-calculations integer proposition; D-064 evidence mapping marked `SUPPORTS` in test mode; Category B decision; contract/projection hashes valid |
| Valid Category C provisional change | **Accepted provisionally** | Adds an unresolved calibration-evidence proposition; decision names missing evidence and test; lifecycle `ADOPTED_PROVISIONAL`; not promoted |
| Valid owner-authorized Category A change | **Accepted in test mode** | Test-only owner-reserved proposition; synthetic authorization source with matching hash/quote; production mode rejects the same request |
| B-09 F-AL-006 within-turn cumulative accrual | **Valid** | Separate B-09 scope; `WITHIN_TURN_CUMULATIVE_ACCRUAL` distinct from cross-turn persistence; F-AL-006 text and integer cumulative-floor model preserved |

The Category A fixture is not a claim of project owner authorization. The test-only proposition is `CATEGORY_A_TEST_PROPOSITION`; P-003 was not reclassified as Category A.

---

## 11. Validator totals

| Validator | Actual result |
|---|---|
| `14A_validate_numerical_foundation.py` | **64/64 checks; FAILED 0; PASS** |
| `14A_validate_numerical_foundation.py --self-test` | **150/150 self-tests passed** (138 legacy + 12 contract) |
| `14A_contract_validator.py` | **9/9 production checks; PASS**; report SHA-256 `de9836c2a9be0d7a35d6674e5d612a0ae96819b855375335197eb53b791be4b0` |
| `test_14A_contract_validator.py` | **83/83 tests; OK** |
| Evidence and authority independence | Valid authority + unsupported evidence: evidence fails, authority passes. Valid evidence + missing authority: evidence passes, authority fails |

`14A-01`–`14A-55` retain their IDs and count. `14A-28`'s archive selector was narrowed to the original Prompt 14A archive so the new implementation archive does not break it; `14A-45`, `14A-46` and `14A-54` now delegate semantic acceptance to the contract gate; `14A-55` remains the final-archive check. No check was removed or renumbered, and the retired lexical logic is diagnostic-only. `14A-56`–`14A-64` are the new contract checks. The 138 legacy self-tests remain; one legacy fixture's expected semantics changed from “accept a placeholder owner authorization” to “Category B wording clarification” because AC-20 now forbids placeholder owner proof. This is recorded, not hidden.

---

## 12. Preservation, hashes and manifest

| Invariant | Actual state |
|---|---|
| Active formula identifiers | 295 unchanged |
| Retired formula | F-WEP-048 remains retired |
| Formula registers | Nine preserved |
| Numerical parameter records | 393 unchanged |
| B-03 carry-in parameters | 20 preserved |
| B-04 F-EC-000b source hash | `bb1090ccae5cd15e0d883a57ab63216a106ff7c4e503e85cf2146e19e02271c6` |
| B-04 F-EC-000f source hash | `3025cc447ebb91be8d226ff5035da0e403947d2be603e81e535bbd5600bca5ca` |
| Production amendment manifest | `amendments: []` |
| D-014 policy | Unmodified; SHA-256 `697dd52d895ff897c498c1acb987535178da42e96bb3458297e762addb8ad479` |
| B-14 full-document hash | `2a3ce894d7de537582941b34cabfa4ba0c48f07067e4bf3ffee798b54afb94dd` |
| DECISIONS.md hash | `d8cced90072a58611f55aa758c8755416cb679f48845bec80741d545bcc9bbb9` |
| B-04 full-document hash | `46950c264dfd3a42979e21fe9ea43e45067bc5ac48ee2a000b5e77420fd30d1c` |

| Contract fingerprint | Value |
|---|---|
| NC-F-EC-000b canonical | `07ce51388c69524d497dafe0c38f7baa7ca4686af29cbc2e00f2e76d2b179d8b` |
| NC-F-EC-000b projection | `9ef02d58e8e0518aad0e0125c78c2a4b720e50be00a24beb2fe05641d1dd1f57` |
| NC-F-EC-000f canonical | `1f81736336c1649cf1bbab770a3f120b4abb7fec4032d27ede1feee810eb44e3` |
| NC-F-EC-000f projection | `682b2c3ea7ef9cbf6bb0546e7fcd13b19a16bd3cbacc8137da71008442e420eb` |
| Material coverage | F-EC-000b 6/6; F-EC-000f 7/7; ratio 1.0 |

No production frontend, backend, SQL, database, migration, API or gameplay file changed. No formula or parameter value changed.

---

## 13. Actual Git status (read-only)

`git status --short` was run; **no Git operation (stage, commit, push, reset, revert, clean) was performed**. The working tree contains 40 entries: 17 modified files and 23 untracked files/directories.

Modified files:

```
 M docs/AI_CONTEXT.md
 M docs/AI_HANDOFF.md
 M docs/DECISIONS.md
 M docs/PROJECT_PROGRESS.md
 M docs/ROADMAP.md
 M docs/prompts/INDEX.md
 M docs/qa_backups/09_validate.py
 M docs/qa_backups/12A_validate_foundations.py
 M docs/qa_backups/13A_validate_ui_foundations.py
 M docs/qa_backups/13B_validate_ui_specifications.py
 M docs/qa_backups/test_next_action.py
 M docs/qa_backups/validate_final.py
 M docs/stage-2/00_stage_2_handoff.md
 M docs/stage-2/01_stage_2_prompt_roadmap.md
 M docs/stage-2/02_master_game_design_bible_outline.md
 M docs/stage-2/04_approved_and_provisional_decisions.md
 M docs/stage-2/06_stage_2_progress_log.md
```

Untracked files/directories include the new contract artifacts, validators, fixtures, report, implementation-prompt archive and the earlier Prompt 14A archives/artifacts. `docs/ROADMAP.md`, the 09/12A/13A/13B validator scripts, `00_stage_2_handoff.md`, `02_master...`, `04_approved...` and the earlier untracked Prompt 14A files were already modified/untracked before this assignment; they were not changed by it. The assignment's own diff is limited to the files listed in §3 plus the new files in §2.

---

## 14. Remaining blockers and provisional decisions

1. **Owner acceptance is outstanding.** Prompt 14A remains OPEN. This is the only blocker to closing 14A.
2. **No human evidence review exists.** All 11 production mappings are `NOT_REVIEWED`. Until an Independent Human Evidence Reviewer records REVIEWED SUPPORTS mappings, no production semantic amendment requiring evidence can pass. This is intentional fail-closed behaviour, not a validator defect.
3. **No owner authorization exists for Category A/D.** The owner-authorization registry is empty. Category A/D amendments fail closed until authentic owner provenance is recorded.
4. **The controlled architecture covers two clauses only.** It is not a general natural-language validator; extending it to other registers is a future governed decision.
5. **Legacy limitations remain.** Four historical validators still fail on frozen guards; 26 historical decision rows have fewer than eight cells. They are preserved, not repaired, in this assignment.
6. **Prompt 14B is not authorized.** Nothing in this report authorizes it.

---

## 15. Acceptance criteria

| ID | Criterion | Result |
|---|---|---|
| AC-01 | 295 formulas unchanged | PASS |
| AC-02 | 393 parameter records unchanged | PASS |
| AC-03 | 20 B-03 carry-ins unchanged | PASS |
| AC-04 | Nine formula registers preserved | PASS |
| AC-05 | Existing 55 numerical checks preserved | PASS (`14A-01`–`14A-55`) |
| AC-06 | Existing 138 self-tests preserved | PASS (138 legacy cases; one superseded expectation documented) |
| AC-07 | Both original B-04 hashes preserved | PASS |
| AC-08 | Production amendment manifest empty | PASS |
| AC-09 | Both contracts pass strict schema validation | PASS |
| AC-10 | B-04 projections match existing clauses | PASS |
| AC-11 | Complete material coverage | PASS (6/6; 7/7) |
| AC-12 | P-003 unambiguous negative representation | PASS |
| AC-13 | D-045/D-064 authority correctly represented | PASS |
| AC-14 | F-AL-006 remains valid | PASS |
| AC-15 | D-991/D-992/D-993 rejected | PASS (3 paraphrases each) |
| AC-16 | D-998/D-999/D-990 rejected | PASS (3 paraphrases each) |
| AC-17 | All required positive fixtures pass | PASS |
| AC-18 | Evidence and authority gates independent | PASS |
| AC-19 | Human evidence-review status genuine and traceable | PASS (role defined; all mappings honestly NOT_REVIEWED) |
| AC-20 | Owner authorization cannot be fabricated or self-authorized | PASS |
| AC-21 | Unknown material fails closed | PASS |
| AC-22 | No unrestricted NLP or external service | PASS |
| AC-23 | Validation deterministic and offline | PASS |
| AC-24 | Legacy gate cannot block a valid adopted amendment | PASS |
| AC-25 | Current documentation and status reconciled | PASS for this pass |
| AC-26 | Historical records preserved | PASS (§15.11 and log §107 retained; old claims marked historical) |
| AC-27 | No production, gameplay or numerical values changed | PASS |
| AC-28 | D-014 unchanged | PASS |
| AC-29 | Prompt 14B remains unauthorized | PASS |
| AC-30 | Actual execution evidence recorded | PASS (this report and executed outputs) |

No criterion is reported as passing without an executed check. AC-19 does not assert that a human reviewed anything; it asserts that the role and honest review states are traceable.

---

## 16. Final Prompt 14A status

**Implementation complete. Documentation complete for this pass. Validation passed at the documentation/tooling level. Owner acceptance PENDING and NOT GRANTED. Therefore PROMPT 14A REMAINS OPEN.**

**PROMPT 14B REMAINS NOT AUTHORIZED / NOT STARTED.**

---

## 17. Exact next action

**Owner review and acceptance or rejection of the Prompt 14A controlled-contract implementation and its executed evidence.** Prompt 14B remains subject to separate explicit owner authorization.

---

## Reproduction

```bash
cd docs
python qa_backups/14A_contract_validator.py
python qa_backups/14A_contract_validator.py --self-test
python qa_backups/test_14A_contract_validator.py
python qa_backups/14A_validate_numerical_foundation.py
python qa_backups/14A_validate_numerical_foundation.py --self-test
```

The contract validator is deterministic, offline and standard-library only. It does not claim human semantic judgment, gameplay validation, balance or owner acceptance.

---

## 18. Prompt 14A-C2 correction — trusted inputs and semantic-gate hardening (2026-11-16)

This section corrects the implementation report for the Project X (106) findings. Sections 1–17 above remain the historical implementation record; this section supersedes their current-status and Git-count statements.

### 18.1 Vulnerabilities closed

| Finding | Correction |
|---|---|
| Caller-controlled trusted inputs | `validate_amendment(request)` now accepts only a strict seven-field request; all trusted inputs load from canonical repository paths through `TrustedContext`. Overrides/aliases fail `CONTRACT_TRUSTED_INPUT_OVERRIDE`; path traversal/symlinks fail path protection. |
| Incomplete material coverage | `material_coverage()` now performs complete span accounting (gaps before/between/after pieces, missing pieces, duplicates, overlapping spans, trailing material). The renderer is derived only from typed fields; prefixes are restricted and fragments are single sentences. |
| Evidence not revalidated | Every applicable mapping and `evidence_refs` entry is revalidated against actual bytes, hash, section, excerpt, proposition, scope, classification and review metadata during amendment acceptance. |
| Authority substitution | Decisions come only from the trusted `DECISIONS.md`; owner authorizations only from the trusted index. Fabricated D-940 is rejected as an override or `CONTRACT_AUTHORITY_MISMATCH`. |
| Git-count discrepancy | Section 13's “40 entries” was a `git status --short` display-line count. The corrected live counts are below. |

The amendment path now executes four independent gates: contract integrity, evidence integrity, D-014 authority and complete comparison. A failure in one gate is not compensated by another.

### 18.2 Updated execution totals

| Suite | Actual result |
|---|---|
| `14A_validate_numerical_foundation.py` | **64/64 checks, 0 failed** |
| `--self-test` | **150/150** |
| `14A_contract_validator.py` | **9/9 checks, PASS** |
| `test_14A_contract_validator.py` | **83/83 tests, OK** |
| `test_14A_trusted_amendment_security.py` | **46/46 tests, OK** |
| `validate_final.py` | **ALL CHECKS PASSED** |
| `test_decision_registers.py` | **12/12 OK** |
| `test_next_action.py` | **27/27 OK** |
| `validate_links.py` | **0 unresolved** |

The 295 formulas, 393 parameter records, 20 B-03 carry-ins, nine registers, both B-04 hashes and the empty production amendment manifest remain unchanged. D-239 records the Category B hardening; D-014 is unmodified.

### 18.3 Corrected Git status

Read-only inspection; no Git operation was performed.

- **17 modified tracked files**
- **33 untracked files** (individual files, including the C2 report and the C2 prompt archive)
- **50 total working-tree files**
- **43 `git status --short` display lines** (Git collapses some untracked directories)
- **0 staged changes**

The prior report's 40 figure was a display-line count, not a file count. The Project X (106) audit's 152/23/175 could not be reproduced from the supplied snapshot in this environment; the snapshot `docs/` files are byte-identical to the pre-C2 live files, and the snapshot `.git` index against the live worktree yields 17 modified tracked and 32 untracked files before the C2 report (42 display lines, 0 staged). The difference is attributed to the audit environment's Git index, line-ending/filter state or untracked-directory counting. The live counts are the authoritative record.

### 18.4 Status

Implementation and documentation are complete for this correction; validation passed at the documentation/tooling level; **human evidence review is NOT complete; owner authorization is NOT obtained; owner acceptance is PENDING and NOT claimed. PROMPT 14A REMAINS OPEN. Prompt 14B remains NOT AUTHORIZED / NOT STARTED.**

The full C2 evidence is in [14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md](14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md).

---

## 19. Prompt 14A-C3 reconciliation (2026-11-17)

This section appends the final closeout corrections to the historical implementation record; it does not rewrite the prior sections.

### 19.1 Metadata diff

`diff_contracts()` now reports `metadata_changes` for `contract_version`, `effective_decision` and `lifecycle_status` with previous value, proposed value, change flag and a classification of `UNCHANGED`, `AUTHORIZED`, `PROVISIONAL`, `UNAUTHORIZED` or `INVALID`. The classification is assigned after the contract, evidence and authority gates from their actual results and never makes a change valid. The authority gate independently rejects an effective-decision mismatch. The C3 metadata suite is **8/8 tests passing**.

### 19.2 Complete numerical self-test

The complete self-test executed **150/150** with exit status 0. Safe text-hash memoization reduced the run from **2m23.817s** to **1m00.094s** without removing, skipping or weakening any case. Repeated execution is deterministic.

### 19.3 Git status correction

The earlier “40 entries” statement was a `git status --short` display-line count, not an individual-file count. The live read-only status with `--untracked-files=all` is:

- **17 modified tracked paths**
- **36 untracked individual files**
- **53 individual paths**
- **46 default display lines**
- **0 staged changes**

The Project X (107) audit's 152/33/185 figures are not reproduced by `git status --short --untracked-files=all`, `git diff --name-status` or the snapshot `.git` index against the live worktree in this environment. The difference is attributed to the audit environment's Git index, line-ending/filter state or a different measurement; no file was staged, reverted or discarded to force agreement.

### 19.4 File inventory

The C3 final closeout report contains the complete C3 file-level inventory with previous and final SHA-256. Earlier C2 changes remain attributed to C2; no earlier change is reclassified as C3.

### 19.5 Status

Prompt 14A remains **OPEN**; owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**. The consolidated evidence is in [14A_FINAL_QA_CLOSEOUT_REPORT.md](14A_FINAL_QA_CLOSEOUT_REPORT.md).


---

## 20. Prompt 14A-C4 reconciliation (2026-11-17)

C4 made no code, contract or numerical change.

- Read-only live status with `git status --porcelain=v1 --untracked-files=all`: **17 modified tracked paths, 38 untracked individual files, 55 individual paths, 48 default display lines, 0 staged.** The 17 modified tracked paths are the accumulated repository total, not C3/C4-specific. C3 changed 14 and created 3; C4 changes documentation only.
- The Project X (108) audit's **152/36/188** is preserved as an audit-environment observation; it is not reproduced by the live Git index or the Project X (108) snapshot `.git` index in this environment. No file was staged, reverted or discarded to force agreement.
- The handoff banner now states **CURRENT PROJECT POSITION — 17 NOVEMBER 2026**; the November 16 semantic-contract banner is **SUPERSEDED / HISTORICAL**.
- Generated cache artifacts separately inventoried: `docs/qa_backups/__pycache__/14A_contract_validator.cpython-312.pyc` and `docs/qa_backups/__pycache__/14A_validate_numerical_foundation.cpython-312.pyc`; ignored by Git, not substantive changes.
- C4 changed documentation only; the expensive suites were not rerun and remain previously independently verified in C3. Prompt 14A remains **OPEN**; formal owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**.

The precommit report is [14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md](14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md).
