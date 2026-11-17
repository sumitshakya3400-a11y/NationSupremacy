# Prompt 14A — Semantic Validation Architecture Proposal

**Status:** INVESTIGATION AND PROPOSAL ONLY — NOT IMPLEMENTED, NOT APPROVED, NOT A CORRECTION.
**Prepared:** 2026-11-16 · **Scope:** Prompt 14A numerical-foundation validation, Project X (104) audit context.
**Governing policy:** [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (D-014), read in full; not modified.
**Owning validator:** [14A_validate_numerical_foundation.py](14A_validate_numerical_foundation.py)
**Related canonical artifacts:** [B-04 formula register](../stage-2/10_economic_formula_and_balance_register.md), [B-14](../stage-2/22_formulas_and_balance.md), [numerical QA report](../stage-2/22_numerical_baseline_qa_report.md), [DECISIONS.md](../DECISIONS.md), [amendment manifest](14A_b04_source_contract_amendments.json), [prompt archive](../prompts/INDEX.md).

> **Non-claims.** This document does not fix the validator, does not close Prompt 14A, does not authorize Prompt 14B, and does not change any formula, parameter, decision, source hash or production amendment manifest. It records a read-only investigation and a proposal. Any adoption requires a separate D-014 decision and owner-visible implementation work.

---

## 1. Root-cause analysis

### 1.1 What was tested and how

The repository's numerical validator was imported as a module and exercised with **in-memory overrides only**. No fixture, source document, manifest or validator code was modified. The reproduction reused the validator's own fixture constructors (`_decision_full`, `_manifest_full`, `_clause_hash`, `_extract_b04_clause`, `_norm_contract`) so that every non-semantic requirement — decision row structure, Category B status, previous/replacement rule, alternatives, rationale, consequences, reopening condition, manifest fields, previous/new fingerprints, authorized evidence path and genuine B-14 §8.2 quotation — was structurally valid.

The exact D-991–D-993 fixture texts are not archived in the repository. The three attack **classes** named in the assignment were reconstructed from their descriptions:

| Case | Attack class | Representative added clause (after the unchanged literal prohibition sentence) |
|---|---|---|
| D-991 | Radix-two exponent/significand encoding | `A radix-two encoding with a separate exponent and significand is permitted for numeric calculations.` |
| D-992 | Sign, exponent and mantissa fields | `Numeric values may be stored as sign, exponent and mantissa fields.` |
| D-993 | Residual sub-unit amounts between turns | `Residual sub-unit amounts between turns are preserved.` |

Each attack used the genuine B-14 §8.2 quotation (`No binary floating point; no fractional carry stated`) and a valid, authorized evidence locus. Each was accompanied by a complete Category B decision and a matching amendment manifest.

**Actual result:** each attack passed **all 55 checks**, including `14A-45` (F-EC-000b source contract and amendment authority) and `14A-54` (complete semantic contract). Nine paraphrase variants across the three classes were also accepted 55/55. This is a class-level bypass, not one wording.

The repository does contain the *previous* attacks, and those were executed exactly as encoded in `self_test()`:

| Case | Actual rejection reason |
|---|---|
| D-998 — unrelated fair-play evidence | `category=decision-evidence … actual=evidence locus is not an authorized source for F-EC-000b: docs/stage-2/20_fair_play_and_player_protection.md section Fair-play` |
| D-999 — prohibition as permission | `semantic-contract … floating-point permission asserted` and `decision-evidence … the cited passage prohibits binary floating point while the amendment or claim permits it` |
| D-990 — IEEE-754 exception attack | `semantic-contract … binary floating-point representation term present: ieee-754` |

The difference between the accepted and rejected cases is **lexical**, not structural. Replacing one word changes the outcome:

| Clause wording | Result | Rejection reason |
|---|---|---|
| `A radix-two representation with a separate exponent and significand is permitted …` | REJECT | `unknown material clause` — because the sentence contains the substring `representation` |
| `A radix-two encoding with a separate exponent and significand is permitted …` | **ACCEPT (55/55)** | No controlled substring is present |
| `Residual fractional carry amounts between turns are preserved.` | REJECT | `fractional carry permission asserted` |
| `Fractional remainders between turns are preserved.` | REJECT | `unknown material clause` — the substring `fractional` is present |
| `Residual sub-unit amounts between turns are preserved.` | **ACCEPT (55/55)** | No controlled substring is present |

### 1.2 Exact code path that accepts D-991, D-992 and D-993

The validation path for a changed B-04 clause is `_validate_source_contract` ([lines 1926–1994](14A_validate_numerical_foundation.py#L1926)). The semantic decision is delegated to `_semantic_contract_violation` ([lines 2213–2279](14A_validate_numerical_foundation.py#L2213)). For F-EC-000b that function implements a **blocklist**, not a complete parse:

1. **Literal representation blocklist** ([lines 2217–2224](14A_validate_numerical_foundation.py#L2217)): it rejects only the exact strings `ieee-754`, `ieee 754`, `binary32`, `binary64`, `binary128`, `single-precision`, `double-precision`, `float32`, `float64`, `alternative representation`, `binary representation`, `decimal representation`. None of `radix-two`, `exponent`, `significand`, `mantissa`, `encoding`, `fields`, `sub-unit`, `remainder` or `fraction` is in the list.
2. **Controlled-term gate** ([lines 2225–2229](14A_validate_numerical_foundation.py#L2225)): exception/condition wording is rejected only when the same sentence also contains one of seven substrings: `floating`, `binary`, `fractional`, `carry`, `precision`, `representation`, `decimal`. The D-991–D-993 sentences contain none of them. The test is a substring test, so `sub-unit` does not match `units`, and `radix-two` does not match `binary`.
3. **Fractional-carry regex** ([lines 2230–2233](14A_validate_numerical_foundation.py#L2230)): it matches only wording built around the literal phrase `fractional carry`. `residual sub-unit amounts`, `sub-unit remainders` and `leftover fractions` do not match.
4. **Floating-point permission regex** ([line 2234](14A_validate_numerical_foundation.py#L2234)): `_perm` only checks the subjects `(?:binary[- ])?floating[- ]point` and `binary representation`. It never checks whether an unrecognized arithmetic representation is being **permitted**.
5. **Required baseline statements** ([lines 2236–2245](14A_validate_numerical_foundation.py#L2236)): the original five statements are still present because the attack appends a sentence and leaves the prohibition anchor untouched. All five checks pass.
6. **Unknown-material clause check** ([lines 2246–2254](14A_validate_numerical_foundation.py#L2246)): this is the only catch-all, but it only examines sentences that already contain one of the seven controlled substrings. A sentence outside that vocabulary is invisible. The function then returns `""` — no violation — which every caller treats as compliance.

The same function is called twice, by `14A-45` and `14A-54` ([lines 1601–1607](14A_validate_numerical_foundation.py#L1601), [1718–1728](14A_validate_numerical_foundation.py#L1718)). They are not independent checks; the second repeats the first. `14A-42` includes an anchor check that verifies only that the literal strings `F-EC-000b` and `binary floating point` are present in the register ([lines 1497–1521](14A_validate_numerical_foundation.py#L1497)); the attacks preserve both, so that check passes. `14A-48` validates the manifest's structure ([lines 1609–1628](14A_validate_numerical_foundation.py#L1609)); the attacks supply a structurally valid manifest, so it passes as well.

### 1.3 Why the evidence gate does not catch the attacks

`_evidence_supports` ([lines 2163–2210](14A_validate_numerical_foundation.py#L2163)) verifies a **free-text `supports` claim**, not the amendment's material propositions:

- It parses `path`, `section`, `quote`, `supports` and `stance`.
- It requires an authorized locus ([lines 2186–2189](14A_validate_numerical_foundation.py#L2186)); B-14 §8.2 is authorized for F-EC-000b, so D-991–D-993 pass this gate.
- It verifies that the quote appears in the cited section ([lines 2194–2199](14A_validate_numerical_foundation.py#L2194)). The genuine quote does.
- It calls `_classify_stance` ([lines 2134–2160](14A_validate_numerical_foundation.py#L2134)), which knows only a narrow set of F-EC-000b terms and **returns `supports` by default**. It never learns that the replacement clause added a radix-two representation, mantissa fields or residual sub-unit amounts.
- It checks token overlap between the `supports` claim and the quote ([lines 2205–2206](14A_validate_numerical_foundation.py#L2205)). A claim such as “the register prohibits binary floating point” overlaps the quote and passes, even though it says nothing about the new proposition.

Consequently, the attack's evidence block can be **true but irrelevant** to the material change. The validator never requires the evidence to cover every changed proposition. This is the same class of defect as D-998, except that D-998 was caught only because its path was outside the allowlist; an irrelevant claim at an authorized path passes.

### 1.4 Why the decision gate does not catch the attacks

`_validate_decision_record` ([lines 2282–2354](14A_validate_numerical_foundation.py#L2282)) checks that a replacement rule is present and that it matches the **new source text** via `_rule_matches` ([lines 2092–2099](14A_validate_numerical_foundation.py#L2092)). `_rule_matches` returns true on substring containment or Jaccard token overlap ≥ 0.85. The decision is allowed to copy the mutated clause, so the comparison is effectively self-referential: the source text and the decision replacement rule can be made identical without any independent semantic relation to the contract or the evidence.

The Category/status logic ([lines 2302–2320](14A_validate_numerical_foundation.py#L2302)) is a string test over the status cell. It does not know which **proposition** the decision is changing. There is no per-proposition authority check, so a Category B decision can authorize a change to a rule that may be an A-derived fixed constraint.

### 1.5 Why D-998, D-999 and the original D-990 are rejected — and why that is not reassurance

| Case | Rejection hook | What would evade it |
|---|---|---|
| D-998 | The fair-play document is not in `B04_EVIDENCE_ALLOWED` ([lines 238–251](14A_validate_numerical_foundation.py#L238)) | Use an authorized locus (B-14 §8.2) with an irrelevant but genuine quote — as D-991–D-993 do |
| D-999 | The literal phrase `floating point` appears in a permission construction; `_perm` and `_classify_stance` recognize it | Express the same permission as `radix-two exponent/significand encoding`; the permission is no longer recognized |
| D-990 | The literal token `ieee-754` is in the representation blocklist | Express the same representation as `radix-two encoding`, `sign/exponent/mantissa fields` or another synonym; the blocklist does not match |

The rejections therefore prove **attack-specific recognition**, not **rule-general enforcement**. Each correction has moved the boundary of the blocklist; the next audit has moved the wording around it.

### 1.6 Root-cause taxonomy

| ID | Root cause | Evidence in the current implementation |
|---|---|---|
| R1 | **Default-allow/open-world semantics.** Unrecognized material is accepted unless it matches a known bad pattern. | `_semantic_contract_violation` returns `""`; `_classify_stance` returns `supports` ([lines 2160](14A_validate_numerical_foundation.py#L2160), [2255](14A_validate_numerical_foundation.py#L2255)). |
| R2 | **Enumeration instead of an ontology.** Semantic classes are ad-hoc strings, not typed concepts with a closed vocabulary. | `rep_terms` and `controlled` lists ([2217–2226](14A_validate_numerical_foundation.py#L2217)); no canonical `BINARY_FLOATING_POINT` class. |
| R3 | **No completeness requirement.** There is no proof that every material segment of a clause was interpreted. | The unknown-clause loop only runs for seven substrings ([2252–2254](14A_validate_numerical_foundation.py#L2252)); unparsed sentences are silently ignored. |
| R4 | **Evidence is text-matching, not proposition entailment.** The `supports` claim is not tied to the propositions being changed. | `_evidence_supports` never receives a proposition set; it receives `replacement` only for narrow term checks ([2163–2210](14A_validate_numerical_foundation.py#L2163), [2282–2338](14A_validate_numerical_foundation.py#L2282)). |
| R5 | **Authority, evidence and fingerprints are commingled.** A valid hash, a Confirmed decision and a genuine quote can collectively look like semantic validation. | `_validate_source_contract` treats hash + manifest + decision + quote as a chain ([1926–1994](14A_validate_numerical_foundation.py#L1926)); none of them proves the proposition. |
| R6 | **The contract lives in code.** Semantic rules are Python literals, not governed data. Changing a rule requires a code patch and a new validator release, while the human-readable register is edited separately. | `B04_CONTRACT` ([197–236](14A_validate_numerical_foundation.py#L197)); `B04_EVIDENCE_ALLOWED` ([238–251](14A_validate_numerical_foundation.py#L238)). |
| R7 | **Test corpus is attack-shaped.** Each correction adds fixtures for the named attack, not a coverage model over the rule's dimensions. The baseline grew from 28 checks/20 self-tests at D-237 to 55/138 today, with nine correction archives after the baseline, without closing the class. | B-14 revision history v0.1–v1.0 ([B-14](../stage-2/22_formulas_and_balance.md), lines 899–912); self-test cases 129–138 ([validator](14A_validate_numerical_foundation.py), lines 2404–2905). |
| R8 | **Documentation claims exceed implementation.** The QA report states “Unknown material wording — Fails closed”, but the catch-all only covers seven substrings. | [QA report](../stage-2/22_numerical_baseline_qa_report.md), line 329; reproduction above. |

**Conclusion of the root-cause analysis.** The failures are not caused by an incomplete synonym list that one more patch can complete. They are caused by the **decision procedure**: the validator accepts unless it recognizes a prohibited token, and it validates evidence by textual proximity rather than by a proposition-level relation. A reliable fix must change that procedure, not extend the list.

### 1.7 Two governance defects exposed by the investigation

These are not code defects; they are questions the current architecture forces into code without an explicit decision:

1. **Scope of F-EC-000b.** The clause says “All quantities are integers” and “No formula uses binary floating point” without stating whether its scope is B-04 only or all nine registers. B-14 §8.2 applies the B-04 integer convention to B-04, while B-09 has an explicit cumulative fractional-accrual rule ([B-14](../stage-2/22_formulas_and_balance.md), lines 240–245; [B-09 F-AL-006](../stage-2/16_alliances_formula_register.md), line 133). D-993's “between turns” wording sits exactly on this ambiguity. The contract schema must carry an explicit scope; **the scope decision itself is not made by this proposal.**
2. **Authority classification of integer arithmetic.** B-14 §2.1 connects integer arithmetic to the fixed constraints D-008/D-009/D-010 ([B-14](../stage-2/22_formulas_and_balance.md), lines 47–56). D-014's Category A includes the fixed architecture. Whether a change to F-EC-000b's arithmetic representation is Category B (ordinary formula/documentation design) or Category A (fixed-constraint reinterpretation) is a governance question. The current validator assumes Category B can authorize it. **This proposal does not resolve that question; it makes the classification explicit and configurable.**

---

## 2. Existing validation architecture

### 2.1 Artifact map

| Artifact | Role in the current architecture | Authority |
|---|---|---|
| [B-04 formula register](../stage-2/10_economic_formula_and_balance_register.md) | Human-readable source of F-EC-000b/F-EC-000f; the text that is hashed and amended | Canonical source text |
| [B-14](../stage-2/22_formulas_and_balance.md) | Index/reconciliation layer; §8.2 contains the authorized evidence quotation | Canonical reconciliation document |
| [DECISIONS.md](../DECISIONS.md) | D-014 decision log; 237 rows; the authority record | Canonical authority |
| [14A_b04_source_contract_amendments.json](14A_b04_source_contract_amendments.json) | Baseline hashes and the amendment ledger; currently `amendments: []` | Controlled QA ledger |
| [14A_validate_numerical_foundation.py](14A_validate_numerical_foundation.py) | 55 documentary checks and 138 self-tests; hard-codes the B-04 contract and evidence allowlist | Tooling, not authority |
| [22_numerical_baseline_qa_report.md](../stage-2/22_numerical_baseline_qa_report.md) | Records the executed baseline and claimed controls | Report/snapshot |
| [22_formula_master_inventory.md](../stage-2/22_formula_master_inventory.md) | Identity/metadata inventory of 295 active formulas | Companion inventory |
| [22_numerical_parameter_inventory.md](../stage-2/22_numerical_parameter_inventory.md) | 393 parameter records, including 20 B-03 carry-ins | Companion inventory |
| Formula registers B-04…B-12 | Nine canonical registers; 295 active formulas | Canonical formula definitions |
| [Prompt archive](../prompts/INDEX.md) | Ten Prompt 14A archives (baseline plus nine corrections) | Historical record |

### 2.2 The amendment-validation pipeline as implemented

The end-to-end path for a proposed B-04 source change is:

1. **Clause extraction.** `_extract_b04_clause` selects the paragraph beginning `**F-EC-000b` or `**F-EC-000f` ([lines 1872–1876](14A_validate_numerical_foundation.py#L1872)).
2. **Normalization and fingerprint.** `_norm_contract` strips Markdown formatting; SHA-256 is computed over the normalized text ([lines 1879–1883](14A_validate_numerical_foundation.py#L1879), [1933–1934](14A_validate_numerical_foundation.py#L1933)).
3. **Semantic gate.** `_semantic_contract_violation` applies the blocklist described in §1.2.
4. **Manifest lookup.** The manifest must parse; amendments are filtered by clause ([1939–1943](14A_validate_numerical_foundation.py#L1939)).
5. **Baseline branch.** If the digest equals the baseline hash, required/forbidden phrase checks run ([1944–1958](14A_validate_numerical_foundation.py#L1944)).
6. **Amendment branch.** If the digest differs, exactly one amendment is required; its fields, source document and previous/new hashes are checked ([1959–1978](14A_validate_numerical_foundation.py#L1959)).
7. **Decision lookup.** The decision row is parsed from DECISIONS.md and must appear exactly once ([1980–1989](14A_validate_numerical_foundation.py#L1980)).
8. **Decision record validation.** Clause, source, verb, topic, D-014 category/status, previous/replacement rules, alternatives, evidence, consequences, reopening condition, owner authorization and manifest evidence fields are checked ([2282–2354](14A_validate_numerical_foundation.py#L2282)).
9. **Evidence validation.** The structured evidence block is checked for an authorized locus, section resolution, exact quote, stance, token overlap and rationale ([2163–2210](14A_validate_numerical_foundation.py#L2163)).
10. **Manifest structure.** `14A-48` validates field completeness, clause membership and hash format ([1609–1628](14A_validate_numerical_foundation.py#L1609)).
11. **Semantic duplication.** `14A-54` calls the same semantic function again ([1718–1728](14A_validate_numerical_foundation.py#L1718)).
12. **Human approval.** A passing validator is documentary consistency only; no owner acceptance is granted by the tool.

### 2.3 What the pipeline proves and what it assumes

| Claim | Mechanism | Actually proven? |
|---|---|---|
| The clause exists and is byte-identical to a fingerprint | SHA-256 over normalized text | **Yes** |
| The source document did not change without a manifest entry | Previous/new hash | **Yes** |
| The decision row exists, is unique and names the clause/source | Table parse and string checks | **Yes, structurally** |
| The D-014 category/status is the required string | Status-cell regex | **Yes, as text; not per proposition** |
| The decision's replacement rule matches the new source | `_rule_matches` containment/Jaccard | **No independent semantics** |
| The cited evidence exists at an authorized locus | Allowlist and section resolution | **Yes, as a locus** |
| The evidence supports the amendment | `supports` claim + token overlap + `_classify_stance` | **No; irrelevant claims can pass** |
| Every material part of the amended clause is understood | No completeness requirement | **No** |
| The decision has authority over the changed proposition | No proposition-level authority | **No** |
| The source still implements the same numerical rule | Only the blocklist | **No** |

### 2.4 Why this architecture produced repeated corrections

Each audit found a new surface form of the same defect. The correction pattern was: add the surface form to a list, add a fixture, increase the check/test count, and re-run. The count history in B-14 §17 is the signature:

| Correction | Checks | Self-tests |
|---|---:|---:|
| Prompt 14A baseline (D-237 snapshot) | 28 | 20 |
| 14A-C1 | 35 | 35 |
| 14A-C1-R1 | 41 | 48 |
| 14A-C1-R1-R1 | 44 | 64 |
| 14A-C1-R1-R1-C1 | 47 | 78 |
| 14A-C1-R1-R1-C1-R1 | 49 | 94 |
| 14A-C1-R1-R1-C1-R1-C1 | 51 | 118 |
| 14A-C1-R1-R1-C1-R1-C1-R1 | 52 | 124 |
| 14A-C1-R1-R1-C1-R1-C1-R1-R1 | 53 | 128 |
| 14A-C1-R1-R1-C1-R1-C1-R1-R1-R1 | 55 | 138 |

Twenty-seven checks and 118 self-tests were added without eliminating the acceptance class. That is evidence that the problem is the **decision procedure**, not the size of the corpus.

---

## 3. Comparison of three approaches

### A. Extend the existing regex and keyword validator

- **Reliability:** Low. Correctness depends on enumerating every bad surface form; the space is open-ended. The current investigation demonstrates a one-word bypass.
- **False acceptance risk:** High. Unrecognized material is accepted by default; evidence need not cover the amendment.
- **False rejection risk:** Low at first, but rises unpredictably as the blocklist grows and catches legitimate wording.
- **Maintainability:** Poor. Every new synonym requires a code patch, new fixtures, a new archive and a new check ID. Nine correction cycles have not closed the class.
- **Compatibility:** Perfect; no migration.
- **Migration effort:** None.
- **Testability:** Adversarial whack-a-mole; coverage is measured by known attacks, not by a rule model.
- **Preservation:** All identifiers and documents preserved.
- **Verdict:** Rejected. It reproduces the failure mode that the assignment asks to stop.

### B. Controlled-language parser with complete coverage

- **Reliability:** Medium to high for a bounded grammar. A complete parse can reject unknown material and represent negation, modality, scope, conditions and exceptions explicitly.
- **False acceptance risk:** Medium. If the parser's grammar or lexicon misclassifies a known construction, a false acceptance is still possible; if the grammar is incomplete, the usual failure is rejection, which is safer.
- **False rejection risk:** High for legitimate prose outside the grammar; authors must learn the controlled language.
- **Maintainability:** Medium. Grammar and lexicon are data; the parser is code. Versioning is manageable.
- **Compatibility:** Good; implementable in Python stdlib. The human-readable document remains the authority, so drift and malformed exceptions remain possible unless the parser is run on every amendment.
- **Migration effort:** High. A parser, grammar, lexicon, error taxonomy and authoring guidance must be built.
- **Testability:** Good. Grammar coverage, parse-failure tests and proposition-level assertions are possible.
- **Preservation:** All identifiers and documents can be preserved.
- **Verdict:** Necessary as a migration/ingestion mechanism, but insufficient alone. It leaves the human text as the sole authority and still lacks a proposition-level evidence and authority model.

### C. Canonical machine-readable numerical contracts, with generated or strictly validated human-readable specifications

- **Reliability:** High. The authority is a typed proposition set; the validator compares propositions, not surface strings. Unknown material cannot be silently ignored because every material segment must be mapped, and every proposed change must be expressed as a proposition diff.
- **False acceptance risk:** Low. A change must identify the proposition it alters; an added permission or exception is a typed conflict, not a phrase to be recognized. Evidence and authority are independent gates.
- **False rejection risk:** Medium at authoring time, because proposals outside the controlled schema are rejected. This is a safe failure and can be reduced with templates and clear diagnostics.
- **Maintainability:** Good. Contracts, lexicon and evidence mappings are versioned data; the validator is a small deterministic engine. Rule changes are governed data changes, not hidden code edits.
- **Compatibility:** Good. JSON + Python stdlib; no paid or external runtime dependency. The existing Markdown documents can remain as projections.
- **Migration effort:** Medium. Two controlled clauses, one schema, one lexicon, one evidence index and a renderer/equivalence check are needed. The 295 active formulas and 393 parameter records do not need to be converted for Prompt 14A.
- **Testability:** Best. Typed error codes, proposition-level fixtures, property-based synonym tests, evidence/authority separation tests and mutation coverage are all straightforward.
- **Preservation:** All formula, parameter, decision and evidence identifiers remain; new proposition IDs are namespaced and never substitute for a `D-`, `F-`, `REQ-` or `UD-` identifier.
- **Verdict:** **Recommended.**

### Comparison matrix

| Dimension | A: Extend regex | B: Controlled parser only | C: Canonical contracts |
|---|---|---|---|
| Reliability | Low | Medium–high | **High** |
| False acceptance | High | Medium | **Low** |
| False rejection | Low now, unpredictable later | High outside grammar | Medium at authoring; low at validation |
| Maintainability | Poor (code patch per synonym) | Medium | **Good (data + small engine)** |
| Existing-architecture compatibility | Perfect | Good | **Good** |
| Migration effort | None | High | **Medium** |
| Testability | Poor | Good | **Best** |
| Preservation of existing IDs/decisions | Perfect | Perfect | **Perfect** |
| Eliminates the D-991–D-993 class | No | Probably, if parse coverage is complete | **Yes, by construction** |

**Recommendation:** Adopt **C**, with **B as the migration and ingestion front-end** for existing prose. C is the only option that changes the default from “accept unless recognized as bad” to “accept only what is fully represented, authorized and evidenced.” B is not discarded: its parser is how legacy text is converted into the initial contracts and how any future prose proposal is either parsed or rejected.

---

## 4. Recommended architecture

### 4.1 Design principles

1. **One authoritative representation per controlled rule.** For the two controlled B-04 numerical-convention clauses, the machine-readable contract is authoritative. The human-readable clause is either generated from it or proven equivalent on every validation run. There is no independent third copy.
2. **Typed propositions, not keyword tests.** A rule is a set of propositions with subject, predicate, object, modality, polarity, scope, conditions, exceptions, units, timing and authority.
3. **Fail closed.** Missing, unknown, ambiguous or unparsed material is a rejection with a machine-readable reason. There is no default `supports` and no default compliance.
4. **Evidence and authority are independent gates.** A decision can authorize a change but cannot make evidence support it. Evidence can support a proposition but cannot authorize a change.
5. **Fingerprints are provenance, not semantics.** A hash proves which bytes were reviewed; it never proves what they mean.
6. **Deterministic and offline.** Python standard library only; no network, no model inference, no randomness, canonical ordering.
7. **Additive migration.** The existing 55 checks and 138 self-tests remain; new checks are added under new IDs. No Prompt 14A rebuild.

### 4.2 Artifact set

Proposed layout (names are illustrative; adoption would be a separate decision):

```
docs/stage-2/22_numerical_contracts/
  index.json                     # contract registry + schema/version references
  lexicon.json                   # canonical concepts + reviewed surface forms
  F-EC-000b.contract.json        # F-EC-000b propositions and change policy
  F-EC-000f.contract.json        # F-EC-000f propositions and change policy
  evidence_mappings.json         # reviewed proposition→evidence mappings
  projections/
    F-EC-000b.md.tpl             # renderer template for the controlled clause
    F-EC-000f.md.tpl
docs/qa_backups/
  14A_contract_validator.py      # deterministic loader, parser, diff, gates, reporter
  test_14A_contract_validator.py # fixtures, property tests, mutation tests
```

The contract files are **not a new formula register and not a new decision register**. They contain no independent numerical values and no independent decisions. Every proposition maps to an existing clause identifier and, where applicable, to an existing `D-` decision. Proposition IDs are namespaced (`NC-F-EC-000b/P-003`) and never replace project identifiers.

### 4.3 Schema (normative shape)

A contract has:

- **Identity:** `schema_version`, `contract_id`, `clause_id`, `title`, `source_document`, `source_version`, `status` (reuse the B-14 status vocabulary), `supersedes`, `effective_decision`.
- **Scope:** explicit systems/registers (`B-04`), turn phases (`P3`, `P4`, `ALL`), numeric domain, and whether the rule is within-turn or across-turn. **Scope is mandatory**; an unstated scope is a schema error.
- **Propositions:** an array of typed objects:
  - `id` — stable, never reused;
  - `kind` — one of a closed enum (`NUMERIC_DOMAIN`, `ARITHMETIC_REPRESENTATION`, `DIVISION_ROUNDING`, `PERCENTAGE_REPRESENTATION`, `FRACTIONAL_ACCUMULATION`, `UNIT_DIMENSION`, `TIMING_BOUNDARY`, `ORDERING`, `CONSERVATION`, `CONSTANT_VERSIONING`, `PRICE_STATUS`, `BALANCE_STATUS`, `REVISION_AUTHORITY`, ...);
  - `subject`, `predicate`, `object` — typed values, not free text;
  - `modality` — `MUST`, `MUST_NOT`, `MAY`, `MAY_NOT`, `NOT_ESTABLISHED`;
  - `polarity` — `AFFIRM`, `NEGATE`, `NEUTRAL`;
  - `scope` — explicit, inheriting only where the schema says so;
  - `conditions` — typed logical expressions over other propositions;
  - `exceptions` — typed objects with `target_proposition`, `effect` (`PERMIT`, `NEGATE`, `QUALIFY`), `scope`, `conditions` and `authority`;
  - `units` — dimension + unit (`CURRENCY/CROWNS`, `RATE/BASIS_POINT`, `TIME/TURN`, `COUNT`, `DIMENSIONLESS`);
  - `timing` — boundary (`TWO_HOUR_UTC`), phase (`P0`–`P7`), persistence (`NONE`, `WITHIN_TURN`, `ACROSS_TURNS`);
  - `numeric` — representation (`INTEGER`, `BINARY_FLOATING_POINT`, `DECIMAL_FRACTION`, `RATIONAL`), radix, format fields, rounding modes, basis (`10,000 bp = 100%`);
  - `authority` — required D-014 category, `owner_reserved`, basis;
  - `source_anchor` — document, section, exact excerpt, line;
  - `status` — `ACTIVE`, `RETIRED`, `PROPOSED`, with `successor` for retirement.
- **Lexicon:** canonical concepts with reviewed surface forms. Initially:
  - `BINARY_FLOATING_POINT`: `binary floating point`, `IEEE-754`, `binary32/64/128`, `single/double precision`, `float32/64`, `radix-two exponent/significand encoding`, `sign-exponent-mantissa fields`, `base-2 exponent/significand form`.
  - `FRACTIONAL_ACCUMULATION`: `fractional carry`, `residual sub-unit amounts`, `sub-unit remainder`, `leftover fraction`, with a required persistence qualifier (`WITHIN_TURN` or `ACROSS_TURNS`).
  - **Unknown surface forms are not guessed. They produce `CONTRACT_UNMAPPED_TERM` and a rejection.** This is the safety property: the lexicon does not need to be omniscient; it needs to be the only door through which a material term can enter.
- **Change policy:** per proposition, which D-014 categories may change it, whether an exception may be added, and whether evidence is mandatory. The default is `B` only for propositions not marked `owner_reserved`; arithmetic-representation propositions carry the unresolved authority classification described in §1.7 until the owner decides.
- **Renderer:** a template and renderer version that produces the controlled clause from the propositions. The renderer is deterministic and its output is hashed.

### 4.4 Deterministic validation pipeline

1. **Load and schema-validate** the index, lexicon, contracts and evidence mappings. Unknown fields, duplicate IDs, dangling references, unknown enums and missing mandatory fields fail.
2. **Verify baseline integrity:** the rendered projection hash equals the recorded contract projection hash; the current B-04 source text hash equals the manifest baseline (or an authorized amendment); the contract semantic hash equals its recorded value.
3. **Accept an amendment in one of two forms:**
   - a **typed contract patch** (preferred), validated against the schema; or
   - a **prose proposal**, tokenized and parsed by the controlled grammar. Any material token or segment not consumed by the grammar produces `CONTRACT_UNPARSED_MATERIAL_SEGMENT`.
4. **Compute the proposition diff:** added, removed, changed and unchanged propositions, with proposition IDs and JSON paths.
5. **Validate internal consistency:** negation/polarity, modality conflicts, scope narrowing/widening, unit compatibility, timing compatibility, rounding completeness, exception targeting and condition satisfiability. A permission that contradicts a `MUST_NOT` proposition without a declared, authorized exception fails with `CONTRACT_PROPOSITION_CONFLICT`.
6. **Evidence gate:** every added/changed proposition requires a reviewed evidence mapping with classification `SUPPORTS`, a scope that covers the proposition, conditions that do not exceed the proposition's conditions, and a document hash matching the actual bytes. `CONTRADICTS`, `QUALIFIES`, `CONTEXT_ONLY`, `NOT_ESTABLISHED`, `INVALID_SOURCE` and `PARSE_FAILURE` fail with distinct codes. Partial coverage fails.
7. **Authority gate:** every changed proposition requires its policy category. Parse the DECISIONS.md row; verify clause/proposition scope, category, status and owner authorization. A Category B decision cannot change an owner-reserved/A-derived proposition; a Category C decision cannot be Confirmed; a missing, duplicate, pending, rejected, deferred or superseded decision fails. This gate is independent of the evidence gate and reports separately.
8. **Fingerprint gate:** the manifest's previous hash must be the current authorized contract version; the new hash must match the candidate; the semantic contract hash must match the candidate; source projection hash must match the rendered candidate. No amendment may carry its own evidence allowlist or contract definition.
9. **Render and compare:** generate the human-readable controlled clause and compare it byte-for-byte (or normalized, during migration) with the proposed text. Any mismatch is `CONTRACT_PROJECTION_MISMATCH`.
10. **Emit a machine-readable report:** every result has a reason code, contract ID, proposition ID, JSON path, source locus and a human-readable explanation. Exit non-zero on any rejection. No default acceptance path exists.

### 4.5 Fail-closed invariants

The architecture is only credible if these invariants are enforced by construction, not by tests:

- **No unparsed material:** every material segment of a controlled clause must map to a proposition or an approved structural token. The validator reports a coverage count; 100% is required.
- **No default stance:** absence of a contradiction is not support. An evidence mapping must be reviewed and classified; missing classification is `NOT_ESTABLISHED`.
- **No self-authorization:** an amendment manifest cannot define or modify an evidence mapping or the lexicon.
- **No semantic default-allow:** an unknown proposition kind, object value, surface form, unit, scope or timing value is a rejection, never “other.”
- **No silent scope widening:** an exception's scope must be a subset of the proposition's scope, and a change that widens a rule's scope is itself a proposition change requiring authority and evidence.

### 4.6 Human-readable documentation

- **Generated for controlled clauses:** F-EC-000b/F-EC-000f paragraphs and the B-14 §8.2 row fragments are rendered from the contract. The renderer is the only writer of those fragments once the architecture is adopted.
- **Not generated for rationale, evidence prose or decisions.** These remain human-authored and are validated for structure, not generated.
- **Equivalence gate before adoption:** during migration, the renderer output must equal the existing clause (normalized) before the contract can be treated as authoritative. If it cannot, the contract extraction is wrong; the architecture does not silently rewrite the rule.
- **Diff visibility:** every renderer change produces a textual diff of the human-readable clause, making the semantic change reviewable by a human.

---

## 5. Example machine-readable contract

The following is illustrative JSON, not a production artifact. It shows the shape needed to make D-990–D-993 impossible to accept. Values are transcribed from the current B-04 clause; the `scope` and `authority` entries deliberately mark the unresolved questions from §1.7.

```json
{
  "schema_version": "1.0.0",
  "contract_id": "NC-F-EC-000b",
  "clause_id": "F-EC-000b",
  "title": "Integer arithmetic",
  "source_document": "docs/stage-2/10_economic_formula_and_balance_register.md",
  "source_version": "B-04 formula register v1.4",
  "baseline_source_hash": "bb1090ccae5cd15e0d883a57ab63216a106ff7c4e503e85cf2146e19e02271c6",
  "status": "PROVISIONAL VALUE",
  "scope": {
    "systems": ["B-04"],
    "turn_phases": ["P3", "P4"],
    "persistence": "WITHIN_TURN",
    "scope_status": "PROPOSED_PENDING_GOVERNANCE_CONFIRMATION"
  },
  "propositions": [
    {
      "id": "NC-F-EC-000b/P-001",
      "kind": "NUMERIC_DOMAIN",
      "subject": "ALL_QUANTITIES",
      "predicate": "HAS_TYPE",
      "object": {"type": "INTEGER"},
      "modality": "MUST",
      "polarity": "AFFIRM",
      "scope": "FORMULA_ARITHMETIC",
      "conditions": [],
      "exceptions": [],
      "units": {"dimension": "DIMENSIONLESS"},
      "timing": {"persistence": "WITHIN_TURN"},
      "authority": {"category": "B", "owner_reserved": false, "basis": "D-014; D-237"},
      "source_anchor": {"text": "All quantities are integers.", "line": 26},
      "status": "ACTIVE"
    },
    {
      "id": "NC-F-EC-000b/P-002",
      "kind": "DIVISION_ROUNDING",
      "subject": "EVERY_DIVISION",
      "predicate": "STATES_ROUNDING",
      "object": {
        "allowed": ["FLOOR", "CEIL", "ROUND_HALF_UP"],
        "floor_negative": "TOWARD_NEGATIVE_INFINITY",
        "floor_positive": "TOWARD_ZERO"
      },
      "modality": "MUST",
      "polarity": "AFFIRM",
      "scope": "FORMULA_ARITHMETIC",
      "conditions": [],
      "exceptions": [],
      "units": {"dimension": "DIMENSIONLESS"},
      "timing": {"persistence": "WITHIN_TURN"},
      "authority": {"category": "B", "owner_reserved": false, "basis": "D-014; D-237"},
      "source_anchor": {"text": "Every division states its rounding: floor ... ceil or round_half_up.", "line": 26},
      "status": "ACTIVE"
    },
    {
      "id": "NC-F-EC-000b/P-003",
      "kind": "ARITHMETIC_REPRESENTATION",
      "subject": "FORMULA_CALCULATIONS",
      "predicate": "MAY_USE_REPRESENTATION",
      "object": {"representation_class": "BINARY_FLOATING_POINT"},
      "modality": "MUST_NOT",
      "polarity": "AFFIRM",
      "scope": "FORMULA_ARITHMETIC",
      "conditions": [],
      "exceptions": [],
      "units": {"dimension": "DIMENSIONLESS"},
      "timing": {"persistence": "WITHIN_TURN"},
      "authority": {
        "category": "A",
        "category_basis": "DERIVED_FROM_FIXED_CONSTRAINTS",
        "classification_status": "PENDING_OWNER_CLARIFICATION",
        "owner_reserved": true,
        "basis": "B-14 §2.1 links integer arithmetic to D-008/D-009/D-010"
      },
      "source_anchor": {"text": "No formula uses binary floating point.", "line": 26},
      "status": "ACTIVE"
    },
    {
      "id": "NC-F-EC-000b/P-004",
      "kind": "PERCENTAGE_REPRESENTATION",
      "subject": "PERCENTAGE",
      "predicate": "IS_REPRESENTED_AS",
      "object": {"unit": "BASIS_POINT", "basis": 10000},
      "modality": "MUST",
      "polarity": "AFFIRM",
      "scope": "FORMULA_ARITHMETIC",
      "conditions": [],
      "exceptions": [],
      "units": {"dimension": "RATE", "unit": "BASIS_POINT"},
      "timing": {"persistence": "WITHIN_TURN"},
      "numeric": {"basis_point_relation": "10000 bp = 100%"},
      "authority": {"category": "B", "owner_reserved": false, "basis": "D-014; D-237"},
      "source_anchor": {"text": "A percentage is an integer in basis points (bp), where 10,000 bp = 100%.", "line": 26},
      "status": "ACTIVE"
    },
    {
      "id": "NC-F-EC-000b/P-005",
      "kind": "FRACTIONAL_ACCUMULATION",
      "subject": "FRACTIONAL_CARRY",
      "predicate": "PERSISTS_BETWEEN_TURNS",
      "object": {"status": "NOT_ESTABLISHED"},
      "modality": "NOT_ESTABLISHED",
      "polarity": "NEUTRAL",
      "scope": "FORMULA_ARITHMETIC",
      "conditions": [],
      "exceptions": [],
      "units": {"dimension": "DIMENSIONLESS"},
      "timing": {"persistence": "ACROSS_TURNS"},
      "authority": {"category": "B", "owner_reserved": false, "basis": "D-014; evidence does not establish permission"},
      "source_anchor": {
        "document": "docs/stage-2/22_formulas_and_balance.md",
        "section": "8.2",
        "text": "No binary floating point; no fractional carry stated"
      },
      "status": "ACTIVE"
    }
  ],
  "change_policy": {
    "default_category": "B",
    "owner_reserved_propositions": ["NC-F-EC-000b/P-003"],
    "propositions_requiring_evidence": [
      "NC-F-EC-000b/P-001",
      "NC-F-EC-000b/P-002",
      "NC-F-EC-000b/P-003",
      "NC-F-EC-000b/P-004",
      "NC-F-EC-000b/P-005"
    ]
  },
  "renderer": {
    "template_id": "B04-F-EC-000b",
    "version": "1.0.0",
    "deterministic": true
  }
}
```

A corresponding evidence mapping:

```json
{
  "schema_version": "1.0.0",
  "mappings": [
    {
      "evidence_id": "EV-B04-F-EC-000b-001",
      "contract_id": "NC-F-EC-000b",
      "proposition_id": "NC-F-EC-000b/P-003",
      "document_path": "docs/stage-2/10_economic_formula_and_balance_register.md",
      "section": "2. Numerical conventions",
      "document_sha256": "<actual full-document hash recorded at review>",
      "excerpt": "No formula uses binary floating point.",
      "classification": "SUPPORTS",
      "scope": {"systems": ["B-04"], "turn_phases": ["P3", "P4"], "persistence": "WITHIN_TURN"},
      "conditions": [],
      "review": {
        "reviewed_by": "<role>",
        "authorizing_decision": "D-237",
        "reviewed_at": "2026-11-16",
        "review_note": "The clause directly states the prohibition."
      },
      "status": "ACTIVE"
    },
    {
      "evidence_id": "EV-B14-8.2-001",
      "contract_id": "NC-F-EC-000b",
      "proposition_id": "NC-F-EC-000b/P-005",
      "document_path": "docs/stage-2/22_formulas_and_balance.md",
      "section": "8.2",
      "document_sha256": "<actual full-document hash recorded at review>",
      "excerpt": "No binary floating point; no fractional carry stated",
      "classification": "NOT_ESTABLISHED",
      "scope": {"systems": ["B-04"], "turn_phases": ["P3", "P4"], "persistence": "ACROSS_TURNS"},
      "conditions": [],
      "review": {
        "reviewed_by": "<role>",
        "authorizing_decision": "D-237",
        "reviewed_at": "2026-11-16",
        "review_note": "The evidence says no fractional-carry rule is stated; it neither permits nor prohibits one."
      },
      "status": "ACTIVE"
    }
  ]
}
```

### 5.1 How the mandatory attacks fail against this model

| Attack | Contract representation | Required result |
|---|---|---|
| D-991 | `radix-two encoding with exponent and significand` maps to `BINARY_FLOATING_POINT`; the patch adds a permission for P-003 | `CONTRACT_PROPOSITION_CONFLICT`: P-003 is `MUST_NOT`; no authorized exception exists. |
| D-992 | `sign, exponent and mantissa fields` maps to `BINARY_FLOATING_POINT`; same conflict | `CONTRACT_PROPOSITION_CONFLICT`. |
| D-993 | `residual sub-unit amounts between turns` maps to `FRACTIONAL_ACCUMULATION` with `persistence: ACROSS_TURNS`; P-005 is `NOT_ESTABLISHED` | `EVIDENCE_CLASSIFICATION_NOT_SUPPORTS`: B-14 §8.2 is `NOT_ESTABLISHED`; no permission is established. |
| D-990 | Exception targets P-003 with `PERMIT` and scope “treasury carry subsystem” | `CONTRACT_EXCEPTION_UNSUPPORTED`: no allowed exception; scope is not authorized. |
| D-999 | Direct permission for `BINARY_FLOATING_POINT` | `CONTRACT_PROPOSITION_CONFLICT` plus evidence `CONTRADICTS` if it cites the prohibition. |
| D-998 | Evidence maps to a fair-play proposition, not P-003; the document has no P-003 mapping | `EVIDENCE_PROPOSITION_MISMATCH` / `EVIDENCE_MAPPING_MISSING`; the manifest cannot add the mapping. |

The rejection reasons are properties of the **proposition model**, not of the attack wording. A new synonym that the lexicon does not recognize is rejected as unmapped; a synonym that maps to `BINARY_FLOATING_POINT` is rejected as a conflict; a scope that is not authorized is rejected as an exception; evidence that does not establish the proposition is rejected as not established.

---

## 6. Evidence and authority separation

### 6.1 Two independent gates

| Gate | Question | Inputs | Cannot be satisfied by |
|---|---|---|---|
| **Evidence** | Does the cited source establish this exact proposition, under these scope/conditions? | Contract propositions, evidence mappings, source document bytes, excerpts | A decision, a manifest field, a hash, a filename, a generic rationale, token overlap, or the amendment's own `supports` text |
| **Authority** | Does a valid D-014 decision authorize this change to this proposition? | DECISIONS.md, contract change policy, proposition authority metadata, manifest | An evidence quote, a source document, a contract file, or a test fixture |

Both gates must pass for every changed proposition. The validator reports them separately so a failure cannot be misattributed.

### 6.2 Evidence classifications

Use the classifications required by the 14A instruction, with strict meanings:

| Classification | Meaning | Effect on amendment |
|---|---|---|
| `SUPPORTS` | The source establishes the exact proposition, scope and conditions | May pass, if all other checks pass |
| `CONTRADICTS` | The source conflicts with the proposition | Reject |
| `QUALIFIES` | The source supports only under conditions not present in the proposition | Reject unless the proposition is changed to include those conditions |
| `CONTEXT_ONLY` | Background only; no proof | Reject as insufficient |
| `NOT_ESTABLISHED` | The evidence neither establishes nor contradicts the proposition | Reject |
| `INVALID_SOURCE` | Path, section, excerpt or document hash cannot be verified | Reject |
| `PARSE_FAILURE` | The evidence content cannot be interpreted by the controlled grammar | Reject |

A hash proves which bytes were referenced. It does not prove that the bytes support the proposition. The classification is a reviewed human judgment recorded in data; it is not inferred by keyword overlap, and it is not inferred by an AI at validation time.

### 6.3 Reviewed evidence mappings

- The mapping file is independent of the amendment manifest.
- Each mapping has a unique `evidence_id`, a `proposition_id`, a document path, an exact locator, a full-document SHA-256, an exact excerpt, classification, scope, conditions, review metadata and status.
- Mapping changes require a D-014 decision and regression evidence; an amendment cannot add, remove or modify a mapping.
- The validator recomputes the document hash and verifies the excerpt at the locator. A changed source invalidates the mapping until it is re-reviewed.
- Mapping coverage is proposition-based: every active proposition in a controlled contract that requires evidence must have at least one active `SUPPORTS` mapping. A mapping for a different proposition does not count.

### 6.4 D-014 authority validation

- The decision register remains the sole authority record. The contract does not duplicate decisions; it references decision IDs.
- The validator parses the decision row and checks: unique ID; date; clause and proposition scope; category (`A`/`B`/`C`/`D`); status (`Confirmed` for B, `Provisional` for C, explicit owner authorization for A/D); previous/new contract versions; owner authorization reference where required; not pending/rejected/deferred/superseded.
- Per-proposition policy:
  - Category B may change ordinary propositions only.
  - Category A or D may change owner-reserved/A-derived propositions only with explicit owner authorization.
  - Category C may record a provisional change with a named missing evidence/test; it cannot be promoted to Confirmed and cannot change an owner-reserved proposition.
- The unresolved classification from §1.7 is represented as data (`category: A`, `category_basis: DERIVED_FROM_FIXED_CONSTRAINTS`, `classification_status: PENDING_OWNER_CLARIFICATION`), not assumed in code. Until the owner decides, a change to P-003 requires Category A; a wording clarification that leaves the proposition set unchanged can remain a Category B documentary edit.

### 6.5 Fingerprints, manifests and approvals

- The **contract hash** covers the canonical JSON (sorted keys, UTF-8, LF, fixed indentation).
- The **projection hash** covers the rendered human-readable clause.
- The **source hash** covers the actual B-04 Markdown.
- The **manifest** records previous/new source and contract hashes and the decision ID. It cannot contain policy, lexicon, evidence or contract content.
- The **approval** remains a human/owner act. The validator reports documentary consistency and never claims owner acceptance, gameplay validation, implementation or balance.

---

## 7. Migration plan

### 7.1 Guardrails

- No production source, formula, parameter, decision, hash or manifest changes during Phases 0–2.
- Existing check IDs `14A-01`…`14A-55` and self-tests 1–138 are not modified, deleted, weakened or renumbered.
- New checks use `14A-56`, `14A-57`, …; new self-tests use 139, 140, ….
- The contract system is additive and can be removed without touching existing documents.
- The production amendment manifest remains `amendments: []` throughout Phases 0–2.
- Any Phase 3 adoption is a separate D-014 decision and must be owner-visible.

### 7.2 Phases

**Phase 0 — Freeze the baseline (read-only).**
Record the executed baseline: 55/55 checks, 138/138 self-tests, the two source hashes, the empty manifest, 295 active formulas, 393 parameter records, 20 B-03 carry-ins, nine registers, D-014 unmodified. Capture the exact outputs in a dated snapshot. This is the reference against which the new system is proven equivalent.

**Phase 1 — Contract extraction and equivalence proof (no source changes).**
- Define the schema, lexicon and initial contracts for F-EC-000b and F-EC-000f by transcribing the current clauses into typed propositions.
- Build the renderer and prove that its output equals the current clause after normalization; investigate every difference and correct the extraction, not the source.
- Record a **material coverage report**: every material segment of the controlled clause maps to a proposition or an approved structural token; 100% is required.
- Build the evidence mappings for the active propositions from the authorized loci. Classify the B-14 §8.2 fractional-carry statement as `NOT_ESTABLISHED`, not as support or prohibition.
- Nothing is authoritative yet. If the contract and the source disagree, the source wins and the extraction is wrong.

**Phase 2 — Parallel validation (additive checks).**
- Add `14A-56` (`contract-integrity`: schema, coverage, projection equivalence, evidence mapping integrity) and `14A-57` (`contract-amendment-gates`: evidence and authority separation) to the existing validator, without changing checks 01–55.
- Add self-tests 139+ covering the six mandatory negatives, positives, adversarial dimensions and the contract/evidence/authority failure modes.
- Run the new checks on the unchanged baseline; they must pass. Run the negative fixtures; they must fail with the specified codes. Run the full legacy suite; it must remain 55/55 and 138/138.
- The new checks are advisory for production until Phase 3, but they are mandatory in the test suite.

**Phase 3 — Governance adoption (separate authorization).**
- A new Category B D-entry records the contract as the authoritative representation of the two controlled clauses, the projection-equivalence gate and the reviewed evidence mappings.
- If the rendered clause is byte-identical to the current text, the source hash does not change and the manifest remains empty. If it differs, the source text is updated through the normal amendment process: decision, manifest, previous/new hash and regression evidence.
- The existing semantic blocklist may remain as a defensive legacy check, but it is no longer the authoritative semantic gate. It is not deleted in the same change; a later cleanup may retire it after the new gate has an independent audit history.

**Phase 4 — Extension (future 14 subphases).**
Add contracts only for rules that need semantic amendment validation, for example the B-02 fixed cadence, the B-14 status/rounding matrix or other register-level conventions. Do not convert all 295 formulas. Formula values and expressions remain owned by their registers and covered by the existing inventory/arithmetic checks.

### 7.3 What must change and what remains untouched

| Component | Phase 0–2 | Phase 3 (if authorized) |
|---|---|---|
| Nine formula registers | **Untouched** | Untouched except the two controlled clause texts, and only if the projection differs |
| 295 active formulas | **Untouched** | Untouched |
| 393 parameter records | **Untouched** | Untouched |
| 20 B-03 carry-ins | **Untouched** | Untouched |
| Existing 55 checks | **Untouched; all preserved** | Preserved; new checks added |
| Existing 138 self-tests | **Untouched; all preserved** | Preserved; new tests added |
| B-04 source contracts | **Untouched; shadow contract only** | Contract becomes authoritative; projection equivalence enforced |
| B-14 | **Untouched** | Add a documentation section describing the contract system, if decided |
| Decision register | **Untouched; historical rows preserved** | Add one D-entry for adoption; no historical rewrite |
| Evidence mappings | **New file; reviewed; non-authoritative** | Becomes controlled evidence data |
| Production amendment manifest | **Remains empty** | Updated only if the source text changes |
| QA report | **Untouched** | Add a new correction section; preserve historical snapshots |
| D-014 policy | **Untouched** | Untouched |
| Prompt 14A archive | **Untouched** | Add a new archive for the adoption prompt |

### 7.4 Rollback

Because Phases 0–2 are additive, rollback is trivial: remove the new contract files, new checks and new tests; the existing validator and all canonical documents are unchanged. Phase 3 rollback requires a new D-014 decision and the normal amendment process; it is not a code-only rollback.

### 7.5 Why this does not rebuild Prompt 14A

The 14A foundation — 295 identifiers, 393 parameter records, 20 B-03 carry-ins, nine registers, the B-14 index, the status vocabulary, the existing QA baseline and the 55/138 regression suite — is preserved. The new system adds a semantic layer over two clauses that already exist. No inventory is repeated, no formula is redesigned, no numerical value changes, and no prior correction is discarded.

---

## 8. Regression-test strategy

### 8.1 Mandatory negative cases

Each case must be rejected for the **stated semantic reason**, not for a missing decision, malformed manifest, hash mismatch or unrelated structural failure.

| ID | Attack | Expected reason code | Must not pass because of |
|---|---|---|---|
| D-998 | Unrelated fair-play evidence | `EVIDENCE_PROPOSITION_MISMATCH` or `EVIDENCE_MAPPING_MISSING` | Locus allowlist alone; the test must exercise an authorized-locus variant too |
| D-999 | Prohibition presented as permission | `CONTRACT_PROPOSITION_CONFLICT` and/or `EVIDENCE_CLASSIFICATION_CONTRADICTS` | The literal phrase `floating point` |
| D-990 | Exception for IEEE-754 representation | `CONTRACT_EXCEPTION_UNSUPPORTED` | The literal token `ieee-754` |
| D-991 | Radix-two exponent/significand encoding | `CONTRACT_PROPOSITION_CONFLICT` (mapped `BINARY_FLOATING_POINT`) or `CONTRACT_UNMAPPED_TERM` | The word `encoding` |
| D-992 | Sign, exponent and mantissa fields | `CONTRACT_PROPOSITION_CONFLICT` (mapped `BINARY_FLOATING_POINT`) or `CONTRACT_UNMAPPED_TERM` | The words `fields` or `mantissa` |
| D-993 | Residual sub-unit amounts between turns | `EVIDENCE_CLASSIFICATION_NOT_SUPPORTS` and/or `CONTRACT_FRACTIONAL_ACCUMULATION_NOT_ESTABLISHED` | The absence of the phrase `fractional carry` |

The D-991–D-993 tests must not be satisfied by recognizing only the representative wording. Each class must include at least three paraphrase variants, including one that uses a novel surface form and is rejected as `CONTRACT_UNMAPPED_TERM`. This proves the fail-closed behavior rather than vocabulary coverage.

### 8.2 Positive cases

| Case | Expected |
|---|---|
| Unchanged production baseline | PASS, 55/55 legacy checks and 138/138 legacy tests; contract checks pass |
| Valid Category B wording clarification (e.g., “including derived calculations”) | ACCEPT when the proposition set is unchanged; decision + manifest required; no evidence contradiction |
| Valid Category B semantic change with genuinely supporting evidence | ACCEPT only when every changed proposition has `SUPPORTS` evidence and B authority |
| Valid Category A owner-authorized change to an owner-reserved proposition | ACCEPT only with explicit owner authorization; the owner-reserved status must be in the contract and the decision |
| Valid Category C provisional change | ACCEPT as Provisional; remains Provisional; no promotion |
| Legitimate B-09 intra-turn cumulative fractional accrual | Not affected by F-EC-000b if the contract scope is B-04; if a global scope is chosen, a B-09 exception must be explicitly modeled and authorized |

### 8.3 Adversarial dimensions

| Dimension | Tests |
|---|---|
| **Negation** | Double negation; “not prohibited”; “no … except”; “neither … nor”; negation scoped to one subsystem; a negated proposition re-used as a positive evidence claim |
| **Exceptions** | `unless`, `except`, `only when`, `where`, `provided that`, `notwithstanding`, `however`, `but`; long-distance exceptions; multiple sentences on the same subject; an exception after a semicolon; an exception targeting one subsystem |
| **Scope** | Global vs B-04 vs subsystem; exception scope wider than the proposition; a change that silently widens scope; cross-register leakage (B-09 accrual vs B-04 carry) |
| **Units** | bp vs percent; 10,000 bp vs 1,000 bp; crowns vs resource units; per-turn vs per-event; dimension mismatch |
| **Timing** | P0–P7; two-hour UTC boundary; within-turn vs across-turn; “residual between turns” vs “cumulative within the turn” |
| **Fractional carry** | Explicit permission; implicit permission via “preserve”, “retain”, “residual”, “remainder”; denial-only evidence; cumulative accrual that is authorized in B-09 but not in B-04 |
| **Equivalent numerical representations** | 1% = 100 bp; 10,000 bp = 100%; integer 5 vs 500 bp; floor vs truncate for negative values; radix-two encoding vs IEEE-754; sign/mantissa vs significand |
| **Unknown propositions** | New noun, verb, object, unit, scope or timing value; unknown surface form; unknown proposition kind; unknown exception effect |
| **Partial evidence support** | Evidence supports one of three changed propositions; evidence supports a weaker scope; evidence supports a condition that the amendment omits; evidence supports the old rule but not the new one |
| **Unauthorized decision changes** | Category B changing an owner-reserved proposition; Category C promoted to Confirmed; pending/rejected/deferred/superseded; duplicate ID; wrong clause/proposition scope; owner authorization missing; a decision that cites itself or its own manifest as authority |
| **Self-authorization** | Manifest supplies its own evidence mapping, lexicon or allowlist; amendment adds a new evidence path without a reviewed mapping; mapping update without a decision |
| **Fingerprint/drift** | Correct old hash but wrong new hash; correct hashes but changed evidence document; contract projection drift; source text changed without manifest; manifest changed without source change |
| **Parser completeness** | A material clause outside the grammar; a recognized sentence with an unrecognized trailing qualifier; an ambiguous modal; a sentence that parses in two ways (must be rejected, not resolved arbitrarily) |

### 8.4 How legitimate amendments continue to work

- **Wording-only clarification:** the patch produces an empty proposition diff; the renderer changes the text; the decision and manifest record the source hash change; a Category B decision is sufficient. This preserves the existing positive fixture where “including derived calculations” is accepted.
- **Semantic clarification with evidence:** the patch changes or adds a proposition; the evidence mapping supplies `SUPPORTS` for that exact proposition; the authority gate supplies the correct D-014 category. The renderer produces the new clause; the manifest records the new hashes. The change is accepted and auditable.
- **Owner-authorized change:** a Category A/D decision with explicit owner authorization changes an owner-reserved proposition; the evidence gate still applies; the contract records the new version and the decision. The owner can change the rule; the validator cannot invent the authority.
- **Provisional change:** a Category C decision records a provisional proposition and names the missing evidence/test; the contract status stays Provisional. It is not promoted by the validator.
- **New evidence:** a reviewed mapping is added by a separate D-014 decision, with a document hash and regression evidence. It does not retroactively authorize an amendment that previously failed.
- **Unchanged baseline:** no proposal, no problem; the baseline passes as before.

### 8.5 Test mechanics

- Fixtures are JSON (typed patches, evidence mappings, decisions, manifests) plus a small number of prose inputs for the parser. Production files are never modified; the test harness uses temporary directories or in-memory overrides.
- Property-based tests: generate random synonym substitutions from the lexicon, random scope/condition combinations, random unit/timing values and random well-formed proposals. All ill-formed variants must fail with a specific code; all well-formed variants must pass. Use a fixed seed for reproducibility.
- Mutation testing: mutate each contract proposition, evidence classification, authority field and renderer output; assert that every mutation is caught by at least one test. Report a proposition-coverage matrix.
- Golden reports: exact reason codes and JSON paths are snapshot-tested, so a future change cannot silently weaken a rejection.
- Determinism test: run each fixture twice; outputs and hashes must be identical. Run with networking disabled; no code path may import a network or model library.

---

## 9. Acceptance criteria

A future implementation may be considered ready for owner review only when all of the following are demonstrated with executed evidence:

1. **AC-01 — Baseline preservation.** The unchanged repository passes 55/55 numerical checks and 138/138 self-tests; all nine registers, 295 active formulas, 393 parameter records and 20 B-03 carry-ins are unchanged.
2. **AC-02 — Schema integrity.** Every contract, lexicon and evidence mapping validates against the declared schema; unknown fields, enums, IDs, references and missing mandatory fields are rejected.
3. **AC-03 — Projection equivalence.** The rendered F-EC-000b and F-EC-000f clauses equal the current clauses after the agreed normalization; any difference is investigated and resolved before the contract is treated as authoritative.
4. **AC-04 — Material completeness.** The controlled clauses have 100% material-segment coverage; no unparsed material segment remains; the coverage report is attached.
5. **AC-05 — Mandatory negatives.** D-998, D-999, D-990, D-991, D-992 and D-993 are rejected with the specified semantic reason codes; each class has at least three paraphrase variants; none is rejected for an unrelated structural reason.
6. **AC-06 — Positives.** The unchanged baseline, a valid Category B wording clarification, a valid evidence-backed Category B change, a valid owner-authorized Category A change and a valid Category C provisional change are accepted under their proper conditions.
7. **AC-07 — Evidence gate independence.** A fixture with valid authority but unsupported/contradictory evidence fails the evidence gate; a fixture with valid evidence but missing/unauthorized authority fails the authority gate. The two failures are reported separately.
8. **AC-08 — No self-authorization.** A manifest that tries to add an evidence mapping, lexicon entry or allowlist is rejected; a mapping change without a D-014 decision is rejected.
9. **AC-09 — Fail-closed behavior.** Unknown proposition kinds, objects, surface forms, units, scopes, timing values and exception effects are rejected with `CONTRACT_UNMAPPED_TERM` or `CONTRACT_SCHEMA_INVALID`; there is no generic “other” or default acceptance.
10. **AC-10 — Fingerprint integrity.** Previous/new contract hashes, projection hashes, source hashes and document hashes are recomputed; a correct hash never overrides a semantic failure.
11. **AC-11 — Determinism and offline execution.** Two runs over the same inputs produce identical outputs and hashes; no network, external model, paid service or randomness is used.
12. **AC-12 — Preservation of identifiers and decisions.** No `D-`, `F-`, `REQ-`, `UD-` or `DD-` identifier is created, removed or reinterpreted by the contract layer; proposition IDs are namespaced and local.
13. **AC-13 — Documentation truthfulness.** Current operational documents describe the contract system as implemented only after the corresponding phase is executed; historical snapshots are preserved and labelled.
14. **AC-14 — No production mutation.** During Phases 0–2, the production amendment manifest remains empty, both B-04 baseline hashes remain unchanged, and no numerical value changes.
15. **AC-15 — Explicit authority questions.** The unresolved scope and authority questions from §1.7 are recorded as decisions required, not silently resolved by the implementation.

---

## 10. Risks and limitations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Controlled vocabulary misses legitimate terminology** | Medium | Legitimate amendments are rejected | Fail closed with a precise diagnostic; maintain a reviewed lexicon; provide authoring templates; make vocabulary changes a low-friction but governed data update |
| **Vocabulary expansion reopens the bypass** | Medium | A new synonym could be mapped incorrectly | Every lexicon change needs a reviewed justification and negative tests; the completeness gate rejects unmapped terms; the mapping is data, auditable and versioned |
| **Ambiguous scope (B-04 vs global)** | High until decided | A rule could be applied to the wrong registers; D-993 sits on this boundary | Make scope mandatory in the schema; record the open question; do not let code default to global or B-04; require an owner/governance decision |
| **Authority classification (B vs A-derived) unresolved** | High until decided | A Category B decision may be treated as sufficient for a fixed-constraint change | Encode the classification in the contract; default unknown authority to owner-reserved; require an explicit owner decision |
| **Contract/human text drift** | Medium | Two competing sources of truth, the exact failure this proposal is meant to end | Generate controlled clauses where feasible; otherwise require projection equivalence on every validation run; a mismatch is a hard failure |
| **Evidence classification is a human judgment** | Certain | The system can be wrong if reviewers are careless | Record reviewer, decision, date and rationale; require document hashes and exact excerpts; separate the evidence gate from authority; audit samples |
| **Migration effort is underestimated** | Medium | Delays or a half-finished parallel layer | Limit Phase 1 to two clauses; time-box the parser; keep the existing validator as the fallback; do not convert the 295 formulas |
| **Overfitting the new tests to D-990–D-993** | Medium | False confidence | Use property-based paraphrases, mutation testing, unknown-term tests and independent review; require a coverage matrix over proposition kinds |
| **Schema complexity becomes bureaucratic** | Medium | Authors avoid the process or work around it | Keep the schema minimal for two clauses; generate forms/templates; reject only what is necessary to preserve the rule |
| **False sense of semantic proof** | High if overstated | Stakeholders may believe the system understands English or proves gameplay | State explicitly: the system proves a bounded, reviewed proposition model, not general natural-language understanding, not runtime behavior and not balance |
| **Existing validator remains as a second semantic gate** | Medium during transition | Conflicting verdicts or duplicated authority | Keep the blocklist only as a legacy defensive check; make the contract gate authoritative in Phase 3; retire the legacy gate only after an audit history |
| **No owner bandwidth for the unresolved decisions** | Medium | Phases 3–4 stall | Proceed with Phases 0–2, which are read-only/additive; leave the unresolved questions recorded and block only the rules that depend on them |

### 10.1 Limitations that no architecture can remove

- **This is documentation-level validation.** It does not execute formulas, simulate turns, prove balance, test gameplay or authorize implementation.
- **No general natural-language understanding.** The controlled language covers the propositions that have been modeled. Prose outside it is rejected, not understood.
- **No automatic entailment.** Evidence classifications are reviewed judgments. The validator can prove that the mapping is complete, current and scoped; it cannot prove that a human reviewer's classification is correct.
- **No proof of source intent.** A clause can be internally consistent and still be the wrong game rule. The architecture makes the rule explicit and reviewable; it does not choose the rule.
- **No substitute for owner authority.** Category A/D questions and unresolved design decisions remain owner/governance matters.

### 10.2 Decisions required before adoption

These are recorded as open questions; this proposal does not resolve them:

1. **F-EC-000b scope:** B-04 only, or all nine registers? If all, how is B-09's explicit cumulative fractional accrual represented as an authorized exception?
2. **Arithmetic-representation authority:** Is the integer/binary-floating-point prohibition a Category B design rule or an A-derived fixed constraint? The contract schema supports either, but the classification must be decided.
3. **Authority of the contract artifact:** Which D-014 category and decision will adopt the contract as the authoritative representation of the two clauses?
4. **Generated projections:** Will the controlled clauses be generated from contracts (preferred) or validated by equivalence? Generation is the stronger single-source guarantee but changes the authoring workflow.
5. **Ownership and location:** Who reviews and owns `lexicon.json`, the evidence mappings and contract versions? The proposal recommends treating them as controlled specification artifacts, not test fixtures.
6. **Extension policy:** Which future 14 subphases may add contracts, and under what review? The default should be “only when a rule needs semantic amendment validation,” not “convert everything.”

---

## Appendix A — Investigation record

**Executed commands and observations (2026-11-16):**

- Baseline validator: `python 14A_validate_numerical_foundation.py` → `CHECKS: 55  FAILED: 0`; `RESULT: PASS — documentary consistency only.`
- Self-tests: `python 14A_validate_numerical_foundation.py --self-test` → `SELF-TESTS: 138/138 passed`.
- In-memory reproductions: nine D-991–D-993 paraphrases → each `ACCEPTED (55/55)`; D-998/D-999/D-990 exact fixtures → rejected with the reasons in §1.1; lexical-boundary probes → `radix-two representation` rejected, `radix-two encoding` accepted; `fractional carry` rejected, `sub-unit amounts` accepted.
- Documentation-link validation after adding this proposal: `Markdown files scanned: 132`; `Links found: 4462`; `Links checked locally: 4080`; `External links skipped: 382`; `Anchors checked: 34`; `Unresolved: 0`. The current operational documents still record the pre-proposal totals (131 files / 4,386 links); they were **not** modified under this assignment's documentation boundary, so those recorded totals are now stale and require reconciliation in a future authorized pass.
- Repository state: no project source, formula, parameter, decision, manifest or validator file was modified by this investigation. The only file created is this proposal.

**Files inspected:**

- [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) — read in full; D-014 categories, procedure, priority order, approval semantics, change control.
- [14A_validate_numerical_foundation.py](14A_validate_numerical_foundation.py) — full relevant code path: configuration, `validate`, `_validate_source_contract`, `_decision_authorized`, `_validate_decision_record`, `_classify_stance`, `_evidence_supports`, `_semantic_contract_violation`, `_rule_matches`, `self_test`, archive checks.
- [B-04 formula register](../stage-2/10_economic_formula_and_balance_register.md) — F-EC-000a–F-EC-000f, constants, numerical conventions.
- [B-14](../stage-2/22_formulas_and_balance.md) — purpose, scope, inventory, statuses, units/precision, timing, validators, correction history, closure gates, §15.11.
- [Numerical QA report](../stage-2/22_numerical_baseline_qa_report.md) — executed baseline, §5.15–§5.19, link totals, historical snapshots.
- [DECISIONS.md](../DECISIONS.md) — header, 237 decision rows, D-014, D-198, D-237 row structure.
- [Amendment manifest](14A_b04_source_contract_amendments.json) — baseline hashes, empty `amendments`.
- [Prompt archive index](../prompts/INDEX.md) and the ten Prompt 14A archives — objective, scope and correction history.
- [Final validator](validate_final.py), [decision-register tests](test_decision_registers.py) — role and coverage boundaries.
- [Link validator](validate_links.py) — anchor and local-link rules used to verify this proposal's links.
- B-09 [Alliance formula register](../stage-2/16_alliances_formula_register.md) — F-AL-006 cumulative accrual, the legitimate fractional-accrual case relevant to scope.
- Existing tests and mutation fixtures — `self_test()` cases 1–138, including D-998, D-999 and D-990.

**What was not done:** no implementation, no validator patch, no fixture change, no source or manifest change, no decision change, no Git operation, no Prompt 14B authorization, no owner acceptance claim.

---

**End of proposal.**
