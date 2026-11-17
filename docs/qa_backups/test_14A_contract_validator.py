#!/usr/bin/env python3
"""Regression suite for the Prompt 14A controlled numerical contracts.

Run: python docs/qa_backups/test_14A_contract_validator.py

The suite proves, with executed evidence:
* strict schema and semantic rejection of malformed or dangling contracts;
* deterministic projection equivalence and 100 % material coverage;
* the modality truth table (including double negation);
* the six mandatory negative classes with three paraphrases each, rejected for
  the stated semantic reason rather than a structural hash/manifest failure;
* the required positive fixtures (baseline, wording clarification, typed
  Category B, Category C, owner-authorized Category A, B-09 within-turn);
* independent evidence and D-014 authority gates;
* unknown, contradictory, stale, partial and self-authorizing material fails
  closed;
* fingerprints and repeated runs are deterministic.

Documentation QA only. No network, no model, no randomness.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(HERE, "14A_contract_validator.py")
LEGACY_PATH = os.path.join(HERE, "14A_validate_numerical_foundation.py")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cv = load_module("contract_validator", MODULE_PATH)
legacy = load_module("legacy_numerical_validator", LEGACY_PATH)


def all_problems(report):
    out = []
    for gate in ("request_gate", "contract_gate", "evidence_gate",
                 "authority_gate", "comparison_gate"):
        out.extend(report.get(gate, {}).get("problems", []))
    return out


def codes(report):
    return {p["code"] for p in all_problems(report)}


def gate_problems(report, gate):
    return report.get(gate, {}).get("problems", [])


def schema_errors(instance, def_name="contract"):
    artifacts = cv.load_artifacts()
    return cv.validate_schema(instance, {"$ref": "#/$defs/" + def_name},
                              artifacts["schema"], "$")


class RegistryAndSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = cv.load_artifacts()
        cls.schema = cls.artifacts["schema"]
        cls.lexicon = cls.artifacts["lexicon"]
        cls.contracts = cls.artifacts["contracts"]
        cls.mappings = cls.artifacts["mappings"]
        cls.b04 = cv.read(cv.B04)

    def test_schema_uses_only_supported_keywords(self):
        self.assertEqual(cv.schema_meta_problems(self.schema), [])

    def test_registry_files_parse_and_index_matches(self):
        self.assertFalse(self.artifacts["problems"])
        self.assertEqual(len(self.contracts), 2)
        for contract in self.contracts.values():
            self.assertEqual(schema_errors(contract), [])

    def test_unknown_field_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["unexpected"] = "x"
        errors = schema_errors(contract)
        self.assertTrue(errors)
        self.assertTrue(all(e["code"] == "CONTRACT_SCHEMA_INVALID" for e in errors))

    def test_missing_mandatory_field_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        del contract["baseline_source_hash"]
        self.assertTrue(schema_errors(contract))

    def test_invalid_enumeration_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"][0]["modality"] = "SHOULD"
        self.assertTrue(schema_errors(contract))

    def test_duplicate_proposition_ids_are_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"].append(copy.deepcopy(contract["propositions"][0]))
        problems = cv.validate_contract_semantics(
            contract, self.schema, self.lexicon, cv.read(cv.DECISIONS), self.b04)
        self.assertTrue(any("duplicate proposition" in p["message"] for p in problems))

    def test_incompatible_subject_predicate_object_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"][0]["predicate"] = "USES_REPRESENTATION"
        problems = cv.validate_contract_semantics(
            contract, self.schema, self.lexicon, cv.read(cv.DECISIONS), self.b04)
        self.assertTrue(any(p["code"] == "CONTRACT_SCHEMA_INVALID" for p in problems))

    def test_unit_dimension_incompatibility_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"][3]["units"] = {"dimension": "RATE", "unit": "NONE"}
        problems = cv.validate_contract_semantics(
            contract, self.schema, self.lexicon, cv.read(cv.DECISIONS), self.b04)
        self.assertTrue(any("incompatible with object type" in p["message"] for p in problems))

    def test_timing_persistence_mismatch_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        p005 = next(p for p in contract["propositions"] if p["id"].endswith("P-005"))
        p005["timing"]["persistence"] = "WITHIN_TURN"
        problems = cv.validate_contract_semantics(
            contract, self.schema, self.lexicon, cv.read(cv.DECISIONS), self.b04)
        self.assertTrue(any("does not match scope persistence" in p["message"] for p in problems))

    def test_ambiguous_inheritance_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"][0]["scope"]["inheritance"] = "INHERIT"
        errors = schema_errors(contract)
        self.assertTrue(errors)

    def test_duplicate_json_keys_are_rejected(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8", newline="\n") as fh:
            fh.write('{"a": 1, "a": 2}\n')
            path = fh.name
        try:
            with self.assertRaises(ValueError):
                cv.load_json_strict(path)
        finally:
            os.unlink(path)

    def test_dangling_exception_target_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"][0]["exceptions"] = [{
            "exception_id": "X-001", "target_proposition": "NC-F-EC-000b/P-999",
            "effect": "PERMIT",
            "scope": {"systems": ["B-04"], "domain": "FORMULA_ARITHMETIC",
                      "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
            "conditions": [],
            "authority": {"decision": "D-045", "category": "B"},
        }]
        problems = cv.validate_contract_semantics(
            contract, self.schema, self.lexicon, cv.read(cv.DECISIONS), self.b04)
        self.assertTrue(any(p["code"] == "CONTRACT_EXCEPTION_UNSUPPORTED" for p in problems))

    def test_unknown_exception_effect_is_rejected(self):
        contract = copy.deepcopy(self.contracts["F-EC-000b"])
        contract["propositions"][0]["exceptions"] = [{
            "exception_id": "X-001", "target_proposition": "NC-F-EC-000b/P-003",
            "effect": "ALLOW_ANYTHING",
            "scope": {"systems": ["B-04"], "domain": "FORMULA_ARITHMETIC",
                      "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
            "conditions": [],
            "authority": {"decision": "D-045", "category": "B"},
        }]
        self.assertTrue(schema_errors(contract))


class ProjectionAndCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = cv.load_artifacts()
        cls.b04 = cv.read(cv.B04)

    def test_projection_equals_preserved_clauses(self):
        for clause in ("F-EC-000b", "F-EC-000f"):
            contract = self.artifacts["contracts"][clause]
            rendered, problems = cv.render_contract(contract)
            self.assertEqual(problems, [])
            self.assertEqual(cv.norm_text(rendered),
                             cv.norm_text(cv.extract_clause(self.b04, clause)))

    def test_source_hashes_are_preserved(self):
        for clause, expected in cv.BASELINE_HASHES.items():
            clause_text = cv.extract_clause(self.b04, clause)
            self.assertEqual(cv.source_clause_sha256(clause_text), expected)

    def test_material_coverage_is_complete(self):
        expected = {"F-EC-000b": (6, 6), "F-EC-000f": (7, 7)}
        for clause, (segments, covered) in expected.items():
            contract = self.artifacts["contracts"][clause]
            cov = cv.material_coverage(contract, cv.extract_clause(self.b04, clause))
            self.assertEqual((cov["segments"], cov["covered"]), (segments, covered))
            self.assertEqual(cov["ratio"], 1.0)
            self.assertEqual(cov["missing"], [])
            self.assertEqual(cov["leftover"], "")

    def test_unconsumed_trailing_material_is_rejected(self):
        contract = self.artifacts["contracts"]["F-EC-000b"]
        clause = cv.extract_clause(self.b04, "F-EC-000b") + " Additional unmodelled arithmetic material."
        cov = cv.material_coverage(contract, clause)
        self.assertLess(cov["ratio"], 1.0)
        self.assertTrue(cov["leftover"])

    def test_p003_is_unambiguous_negative_representation(self):
        p003 = next(p for p in self.artifacts["contracts"]["F-EC-000b"]["propositions"]
                    if p["id"].endswith("P-003"))
        self.assertEqual(p003["predicate"], "USES_REPRESENTATION")
        self.assertEqual(p003["object"]["value"], "BINARY_FLOATING_POINT")
        self.assertEqual(p003["modality"], "MUST_NOT")
        self.assertEqual(p003["polarity"], "AFFIRM")
        self.assertNotIn("MAY_USE_REPRESENTATION", json.dumps(self.artifacts["contracts"]["F-EC-000b"]))
        self.assertIn("No formula uses binary floating point.",
                      json.dumps(self.artifacts["contracts"]["F-EC-000b"]))

    def test_arithmetic_authority_is_category_b_and_cites_d045_d064(self):
        contract = self.artifacts["contracts"]["F-EC-000b"]
        for prop in contract["propositions"]:
            if prop["kind"] in ("NUMERIC_DOMAIN", "DIVISION_ROUNDING",
                                "ARITHMETIC_REPRESENTATION", "PERCENTAGE_REPRESENTATION"):
                self.assertEqual(prop["authority"]["category"], "B")
                self.assertFalse(prop["authority"]["owner_reserved"])
                self.assertTrue({"D-045", "D-064"}.issubset(
                    set(prop["authority"]["basis_decisions"])))
        authority = self.artifacts["index"]["cross_cutting_authority"]
        self.assertEqual(authority["authority"]["category"], "B")
        self.assertEqual(authority["scope"]["systems"], ["B-04"])
        self.assertEqual(authority["scope"]["inheritance"], "NONE")


class ScopeAndEvidenceStatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = cv.load_artifacts()

    def test_f_ec_000b_scope_is_b04_only(self):
        contract = self.artifacts["contracts"]["F-EC-000b"]
        self.assertEqual(contract["scope"]["systems"], ["B-04"])
        self.assertIn("B-09", contract["scope"]["excluded_systems"])
        self.assertNotIn("B-09", contract["scope"]["systems"])

    def test_cross_turn_and_within_turn_are_distinct(self):
        p005 = next(p for p in self.artifacts["contracts"]["F-EC-000b"]["propositions"]
                    if p["id"].endswith("P-005"))
        self.assertEqual(p005["modality"], "NOT_ESTABLISHED")
        self.assertEqual(p005["polarity"], "NEUTRAL")
        self.assertIn("CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN",
                      p005["scope"]["distinct_from"])
        concepts = {c["concept_id"] for c in self.artifacts["lexicon"]["concepts"]}
        self.assertIn("CROSS_TURN_REMAINDER_PERSISTENCE", concepts)
        self.assertIn("CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN", concepts)
        cross = next(c for c in self.artifacts["lexicon"]["concepts"]
                     if c["concept_id"] == "CROSS_TURN_REMAINDER_PERSISTENCE")
        within = next(c for c in self.artifacts["lexicon"]["concepts"]
                      if c["concept_id"] == "CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN")
        self.assertIn("CUMULATIVE_FLOOR_ACCRUAL_WITHIN_TURN", cross["distinct_from"])
        self.assertIn("CROSS_TURN_REMAINDER_PERSISTENCE", within["distinct_from"])

    def test_production_evidence_is_honestly_unreviewed(self):
        reviewed = [m for m in self.artifacts["mappings"]["mappings"]
                    if m["review"]["review_status"] == "REVIEWED"]
        self.assertEqual(reviewed, [])
        p005 = [m for m in self.artifacts["mappings"]["mappings"]
                if m["proposition_id"].endswith("P-005")
                and m["contract_id"] == "NC-F-EC-000b"]
        self.assertEqual(len(p005), 1)
        self.assertEqual(p005[0]["classification"], "NOT_REVIEWED")
        self.assertEqual(p005[0]["proposed_classification"], "NOT_ESTABLISHED")
        self.assertFalse(cv.has_supports_review("NC-F-EC-000b/P-005",
                                                self.artifacts["mappings"], mode="production"))

    def test_every_proposition_has_a_draft_mapping(self):
        for contract in self.artifacts["contracts"].values():
            mapped = {m["proposition_id"] for m in self.artifacts["mappings"]["mappings"]}
            for prop in contract["propositions"]:
                self.assertIn(prop["id"], mapped)


class ModalityTests(unittest.TestCase):
    def test_truth_table(self):
        table = {
            "Formula calculations may use binary floating point.": "PERMIT",
            "Formula calculations may not use binary floating point.": "PROHIBIT",
            "Binary floating point is not permitted.": "PROHIBIT",
            "Binary floating point is not prohibited.": "PERMIT",
            "Binary floating point is not not permitted.": "PERMIT",
            "No formula uses binary floating point.": "PROHIBIT",
            "No formula may use binary floating point.": "PROHIBIT",
            "Formula calculations must not use binary floating point.": "PROHIBIT",
            "Every division must state its rounding.": "MANDATE",
            "The binary floating-point prohibition applies to every formula calculation.": "PROHIBIT",
            "Residual sub-unit amounts between turns are preserved.": "PERMIT",
            "Neither permitted nor prohibited.": None,
            "It is permitted and also prohibited.": None,
        }
        for text, expected in table.items():
            self.assertEqual(cv.normalize_modality(text), expected, text)

    def test_double_negation_cannot_bypass_the_prohibition(self):
        request = cv.build_negative("D-999", 2)  # "Binary floating point is not prohibited."
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_PROPOSITION_CONFLICT", codes(report))

    def test_permission_prohibition_reversal(self):
        request = cv.build_negative("D-999", 0)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_PROPOSITION_CONFLICT", codes(report))
        messages = " ".join(p["message"] for p in all_problems(report))
        self.assertIn("contradicts", messages)


class MandatoryNegativeTests(unittest.TestCase):
    EXPECTED = {
        "D-998": {"CONTRACT_EVIDENCE_PROPOSITION_MISMATCH"},
        "D-999": {"CONTRACT_PROPOSITION_CONFLICT"},
        "D-990": {"CONTRACT_EXCEPTION_UNSUPPORTED"},
        "D-991": {"CONTRACT_PROPOSITION_CONFLICT", "CONTRACT_UNMAPPED_TERM"},
        "D-992": {"CONTRACT_PROPOSITION_CONFLICT", "CONTRACT_UNMAPPED_TERM"},
        "D-993": {"CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                  "CONTRACT_EVIDENCE_NOT_REVIEWED",
                  "CONTRACT_EVIDENCE_MAPPING_MISSING"},
    }

    def test_three_variants_per_class(self):
        for case, expected in self.EXPECTED.items():
            for variant in range(3):
                with self.subTest(case=case, variant=variant):
                    report = cv.validate_amendment(cv.build_negative(case, variant))
                    self.assertFalse(report["accepted"])
                    found = codes(report)
                    self.assertTrue(found & expected,
                                    f"{case} variant {variant} did not fail for the semantic reason: {sorted(found)}")
                    # The fixture is structurally valid: the rejection is not a
                    # missing hash, malformed manifest or stale fingerprint.
                    self.assertNotIn("CONTRACT_MANIFEST_INVALID", found)
                    self.assertNotIn("CONTRACT_FINGERPRINT_MISMATCH", found)

    def test_novel_radix_wording_is_rejected_as_unmapped(self):
        report = cv.validate_amendment(cv.build_negative("D-991", 2))
        self.assertIn("CONTRACT_UNMAPPED_TERM", codes(report))

    def test_d993_has_no_supporting_evidence(self):
        report = cv.validate_amendment(cv.build_negative("D-993", 0))
        self.assertFalse(report["accepted"])
        self.assertFalse(cv.has_supports_review("NC-F-EC-000b/P-005",
                                                cv.load_artifacts()["mappings"],
                                                mode="production"))
        evidence_codes = {p["code"] for p in gate_problems(report, "evidence_gate")}
        self.assertTrue(evidence_codes & {"CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS",
                                          "CONTRACT_EVIDENCE_NOT_REVIEWED",
                                          "CONTRACT_EVIDENCE_MAPPING_MISSING"})

    def test_d998_with_authorized_locus_but_irrelevant_claim_is_rejected(self):
        request = cv.build_negative("D-998", 1)
        # Replace the fair-play locus with the authorized B-14 §8.2 locus while
        # keeping the unrelated supports-claim.
        request.fixture_context.decisions_text = request.fixture_context.decisions_text.replace(
            'path=docs/stage-2/20_fair_play_and_player_protection.md; section=Fair-play',
            'path=docs/stage-2/22_formulas_and_balance.md; section=8.2')
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH", codes(report))
        messages = " ".join(p["message"] for p in all_problems(report))
        self.assertTrue("not substantiated" in messages or "does not establish" in messages)


class PositiveFixtureTests(unittest.TestCase):
    def test_unchanged_baseline_is_accepted(self):
        request = cv._fixture_request(
            cv._fixture_ctx(),
            amendment_id="TEST-BASELINE",
            target_contract="NC-F-EC-000b",
            candidate_document=cv.read(cv.B04),
            candidate_contract=None,
            evidence_refs=[],
            decision_ref="D-957",
            notes="Unchanged baseline verification.")
        report = cv.validate_amendment(request)
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])

    def test_typed_category_b_with_supporting_evidence_is_accepted(self):
        report = cv.validate_amendment(cv.build_typed_positive())
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])
        self.assertIn("NC-F-EC-000b/P-007", report["diff"]["added"])
        self.assertTrue(report["evidence_gate"]["passed"])
        self.assertTrue(report["authority_gate"]["passed"])
        self.assertEqual(report["authority_gate"]["category"], "B")

    def test_category_c_provisional_change_is_accepted_and_not_promoted(self):
        request = cv.build_typed_provisional()
        report = cv.validate_amendment(request)
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])
        self.assertEqual(request["candidate_contract"]["lifecycle_status"], "ADOPTED_PROVISIONAL")
        self.assertTrue(report["evidence_gate"]["provisional_open"])

    def test_category_c_cannot_be_promoted(self):
        request = cv.build_typed_provisional()
        prop = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-006"))
        prop["authority"]["classification_status"] = "RESOLVED"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_owner_authorized_category_a_test_proposition_is_accepted_in_test_mode(self):
        request = cv.build_owner_authorized()
        report = cv.validate_amendment(request)
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])
        self.assertEqual(report["authority_gate"]["category"], "A")

    def test_owner_authorized_change_without_trusted_authorization_is_rejected(self):
        request = cv.build_owner_authorized()
        request.fixture_context.owner_authorizations = []
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_OWNER_AUTHORIZATION_MISSING", codes(report))

    def test_owner_authorization_placeholder_is_rejected(self):
        request = cv.build_owner_authorized()
        request.fixture_context.owner_authorizations[0]["quoted_instruction"] = (
            "Owner authorization: TEMP-OWNER-01 (temporary fixture, not a real owner instruction)")
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_OWNER_AUTHORIZATION_MISSING", codes(report))

    def test_wording_clarification_is_accepted(self):
        report = cv.validate_amendment(cv.build_wording_positive())
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])
        self.assertEqual(report["ingestion"]["status"], "WORDING_ONLY")

    def test_contract_accepts_clarification_that_the_legacy_gate_rejects(self):
        clause = cv.BASELINE_CLAUSES["F-EC-000b"].replace(
            "No formula uses binary floating point.",
            "The binary floating-point prohibition applies to every formula calculation.")
        self.assertTrue(legacy._semantic_contract_violation("F-EC-000b", clause))
        report = cv.validate_amendment(cv.build_wording_positive())
        self.assertTrue(report["accepted"])

    def test_b09_within_turn_cumulative_accrual_remains_valid(self):
        contract, problems = cv.build_b09_within_turn()
        self.assertEqual(problems, [], [cv.fmt(p) for p in problems])
        self.assertEqual(contract["scope"]["systems"], ["B-09"])
        b04 = cv.load_artifacts()["contracts"]["F-EC-000b"]
        self.assertFalse(set(contract["scope"]["systems"]) & set(b04["scope"]["systems"]))
        b09 = cv.read(cv.B09)
        for needle in ("F-AL-006 — Automatic Per-Turn Production Tax Arithmetic",
                       "cumulative", "10{,}000", "Different assets keep separate accumulators"):
            self.assertIn(needle, b09)


class GateIndependenceTests(unittest.TestCase):
    def test_authority_passes_while_evidence_fails(self):
        report = cv.validate_amendment(cv.build_typed_unsupported_evidence())
        self.assertFalse(report["accepted"])
        self.assertFalse(report["evidence_gate"]["passed"])
        self.assertTrue(report["authority_gate"]["passed"])

    def test_evidence_passes_while_authority_fails(self):
        report = cv.validate_amendment(cv.build_missing_authority())
        self.assertFalse(report["accepted"])
        self.assertTrue(report["evidence_gate"]["passed"])
        self.assertFalse(report["authority_gate"]["passed"])

    def test_missing_decision_is_an_authority_failure_not_an_evidence_failure(self):
        request = cv.build_missing_authority()
        report = cv.validate_amendment(request)
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))
        self.assertNotIn("CONTRACT_EVIDENCE_NOT_REVIEWED",
                         {p["code"] for p in gate_problems(report, "evidence_gate")})


class EvidenceGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = cv.load_artifacts()
        cls.contracts = cls.artifacts["contracts"]

    def _changed(self):
        return [{"contract_id": "NC-F-EC-000b", "proposition_id": "NC-F-EC-000b/P-005",
                 "systems": ["B-04"]}]

    def test_missing_mapping(self):
        empty = {"schema_version": "1.0.0", "mappings": []}
        report = cv.evidence_gate(self._changed(), empty, self.contracts)
        self.assertFalse(report["passed"])
        self.assertEqual(report["problems"][0]["code"], "CONTRACT_EVIDENCE_MAPPING_MISSING")

    def test_not_reviewed_mapping(self):
        report = cv.evidence_gate(self._changed(), self.artifacts["mappings"], self.contracts)
        self.assertFalse(report["passed"])
        self.assertIn(report["problems"][0]["code"],
                      {"CONTRACT_EVIDENCE_NOT_REVIEWED",
                       "CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS"})

    def test_stale_hash(self):
        mappings = copy.deepcopy(self.artifacts["mappings"])
        mappings["mappings"][0]["document_sha256"] = "0" * 64
        problems, _ = cv.evidence_integrity(mappings, self.contracts)
        self.assertIn("CONTRACT_EVIDENCE_INTEGRITY_FAILED",
                      {p["code"] for p in problems})

    def test_fabricated_quote(self):
        mappings = copy.deepcopy(self.artifacts["mappings"])
        mappings["mappings"][0]["excerpt"] = "A fabricated quotation that does not exist."
        problems, _ = cv.evidence_integrity(mappings, self.contracts)
        self.assertIn("CONTRACT_EVIDENCE_INTEGRITY_FAILED",
                      {p["code"] for p in problems})

    def test_contradictory_classification(self):
        mappings = {"schema_version": "1.0.0", "mappings": [
            cv._test_mapping("NC-F-EC-000b/P-005", "NC-F-EC-000b",
                             excerpt="No binary floating point; no fractional carry stated",
                             classification="CONTRADICTS", reviewed=True,
                             document_path="docs/stage-2/22_formulas_and_balance.md",
                             section="8.2")]}
        report = cv.evidence_gate(self._changed(), mappings, self.contracts, mode="test")
        self.assertFalse(report["passed"])
        self.assertEqual(report["problems"][0]["code"],
                         "CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS")

    def test_partial_coverage(self):
        mappings = {"schema_version": "1.0.0", "mappings": [
            cv._test_mapping("NC-F-EC-000b/P-003", "NC-F-EC-000b",
                             excerpt="No formula uses binary floating point.",
                             classification="SUPPORTS", reviewed=True,
                             document_path="docs/stage-2/10_economic_formula_and_balance_register.md",
                             section="F-EC-000b")]}
        changed = [
            {"contract_id": "NC-F-EC-000b", "proposition_id": "NC-F-EC-000b/P-003", "systems": ["B-04"]},
            {"contract_id": "NC-F-EC-000b", "proposition_id": "NC-F-EC-000b/P-005", "systems": ["B-04"]},
        ]
        report = cv.evidence_gate(changed, mappings, self.contracts, mode="test")
        self.assertFalse(report["passed"])
        self.assertTrue(any(p["code"] == "CONTRACT_EVIDENCE_MAPPING_MISSING" for p in report["problems"]))

    def test_narrower_scope(self):
        mapping = cv._test_mapping("NC-F-EC-000b/P-003", "NC-F-EC-000b",
                                   excerpt="No formula uses binary floating point.",
                                   classification="SUPPORTS", reviewed=True,
                                   document_path="docs/stage-2/10_economic_formula_and_balance_register.md",
                                   section="F-EC-000b")
        mapping["scope"]["systems"] = ["B-05"]
        report = cv.evidence_gate(
            [{"contract_id": "NC-F-EC-000b", "proposition_id": "NC-F-EC-000b/P-003",
              "systems": ["B-04"]}],
            {"schema_version": "1.0.0", "mappings": [mapping]},
            self.contracts, mode="test")
        self.assertFalse(report["passed"])
        self.assertIn("CONTRACT_EVIDENCE_PROPOSITION_MISMATCH",
                      {p["code"] for p in report["problems"]})

    def test_amendment_cannot_supply_its_own_evidence(self):
        request = cv.build_typed_positive()
        request["candidate_contract"]["evidence_mappings"] = {"mappings": []}
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCHEMA_INVALID", codes(report))

    def test_request_cannot_supply_evidence_mappings(self):
        request = cv.build_typed_positive()
        attack = dict(request)
        attack["evidence_mappings"] = {"mappings": []}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_authorizing_decision_is_not_a_substitute_for_evidence(self):
        artifacts = cv.load_artifacts()
        mapping = copy.deepcopy(artifacts["mappings"]["mappings"][0])
        mapping["authorizing_decision"] = "D-237"
        errors = cv.validate_schema(mapping, {"$ref": "#/$defs/evidence_mapping"},
                                    artifacts["schema"], "$.mapping")
        self.assertTrue(errors)


class AuthorityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = cv.load_artifacts()
        cls.base = cls.artifacts["contracts"]["F-EC-000b"]
        cls.decisions = cv._fixture_decisions_text()

    def test_pending_rejected_deferred_superseded_are_rejected(self):
        for word in ("Pending", "Rejected", "Deferred", "Superseded"):
            with self.subTest(status=word):
                request = cv.build_typed_positive()
                request.fixture_context.decisions_text = request.fixture_context.decisions_text + "\n" + (
                    f"| D-960 | 2026-11-16 | TEST FIXTURE {word} | "
                    f"Previous contract: NC-F-EC-000b 1.0.0; Replacement contract: NC-F-EC-000b 1.1.0; "
                    f"Alternatives: retain; add; Consequences: fixture; Reopening: reopen. | "
                    f"**{word}** (Category B; TEST FIXTURE) | Evidence: fixture; Rationale: fixture. | "
                    f"docs/stage-2/10_economic_formula_and_balance_register.md | Consequences: fixture; Reopening: reopen. |\n")
                request["decision_ref"] = "D-960"
                request["candidate_contract"]["effective_decision"] = "D-960"
                report = cv.validate_amendment(request)
                self.assertFalse(report["accepted"])
                self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_duplicate_decision_id_is_rejected(self):
        request = cv.build_typed_positive()
        request.fixture_context.decisions_text = request.fixture_context.decisions_text + "\n" + cv._decision_row_text("D-940") + "\n"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_wrong_category_is_rejected(self):
        request = cv.build_typed_positive()
        request.fixture_context.decisions_text = request.fixture_context.decisions_text.replace(
            "**Confirmed** (Category B; TEST FIXTURE) | Evidence: governed evidence mapping EV-TEST-D064",
            "**Owner-approved** (Category A; TEST FIXTURE) | Evidence: governed evidence mapping EV-TEST-D064", 1)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_authority_downgrade_is_rejected(self):
        first = cv.build_owner_authorized()
        base_contract = first["candidate_contract"]  # P-007 is owner-reserved here
        candidate = copy.deepcopy(base_contract)
        candidate["contract_version"] = "1.2.0"
        candidate["effective_decision"] = "D-940"
        prop = next(p for p in candidate["propositions"] if p["id"].endswith("P-007"))
        prop["authority"]["category"] = "B"
        prop["authority"]["owner_reserved"] = False
        prop["authority"]["classification_status"] = "RESOLVED"
        candidate["change_policy"]["propositions"]["NC-F-EC-000b/P-007"]["category"] = "B"
        candidate["change_policy"]["propositions"]["NC-F-EC-000b/P-007"]["owner_reserved"] = False
        candidate_clause, _ = cv.render_contract(candidate)
        document = cv.replace_clause(cv.read(cv.B04), "F-EC-000b", candidate_clause)
        context = copy.copy(first.fixture_context)
        context.contracts = {"F-EC-000b": base_contract}
        context.contracts_by_id = {"NC-F-EC-000b": base_contract}
        context.decisions_text = cv._fixture_decisions_text()
        context.owner_authorizations = []
        request = cv._fixture_request(
            context,
            amendment_id="TEST-DOWNGRADE",
            target_contract="NC-F-EC-000b",
            candidate_document=document,
            candidate_contract=candidate,
            evidence_refs=["EV-TEST-P-007"],
            decision_ref="D-940",
            notes="Category B downgrade of an owner-reserved proposition.")
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_self_authorizing_authority_metadata_is_rejected(self):
        request = cv.build_typed_positive()
        prop = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-007"))
        prop["authority"]["basis_decisions"] = ["D-940"]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_missing_alternatives_is_rejected(self):
        request = cv.build_typed_positive()
        request.fixture_context.decisions_text = request.fixture_context.decisions_text.replace(
            "Alternatives: retain the baseline only; add the derived-calculation restatement; ",
            "", 1)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_missing_reopening_condition_is_rejected(self):
        request = cv.build_typed_positive()
        request.fixture_context.decisions_text = request.fixture_context.decisions_text.replace(
            "Reopening: reopen if D-064 changes.", "", 2)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_wrong_clause_scope_is_rejected(self):
        request = cv.build_typed_positive()
        row = cv._decision_row_text("D-940")
        wrong = row.replace("F-EC-000b", "F-EC-000f").replace("NC-F-EC-000b", "NC-F-EC-000f")
        request.fixture_context.decisions_text = request.fixture_context.decisions_text.replace(row, wrong, 1)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCOPE_MISMATCH", codes(report))


class SemanticAdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = cv.load_artifacts()
        cls.base = cls.artifacts["contracts"]["F-EC-000b"]

    def _candidate(self):
        request = cv.build_typed_positive()
        return request

    def test_scope_leakage_is_rejected(self):
        request = self._candidate()
        prop = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-007"))
        prop["scope"]["systems"] = ["B-09"]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCOPE_MISMATCH", codes(report))

    def test_basis_point_relation_cannot_change(self):
        request = self._candidate()
        contract = request["candidate_contract"]
        p004 = next(p for p in contract["propositions"] if p["id"].endswith("P-004"))
        p004["numeric"]["basis_point_relation"] = "1,000 bp = 100%"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCHEMA_INVALID", codes(report))

    def test_basis_point_object_basis_cannot_change(self):
        request = self._candidate()
        p004 = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-004"))
        p004["object"]["basis"] = 1000
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCHEMA_INVALID", codes(report))

    def test_negative_number_floor_semantics_cannot_change(self):
        request = self._candidate()
        p002 = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-002"))
        p002["object"]["floor_negative"] = "TOWARD_ZERO"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_PROPOSITION_CONFLICT", codes(report))

    def test_exception_on_prohibited_representation_is_rejected(self):
        request = self._candidate()
        contract = request["candidate_contract"]
        p003 = next(p for p in contract["propositions"] if p["id"].endswith("P-003"))
        p003["exceptions"] = [{
            "exception_id": "X-001",
            "target_proposition": "NC-F-EC-000b/P-003",
            "effect": "PERMIT",
            "scope": {"systems": ["B-04"], "domain": "FORMULA_ARITHMETIC",
                      "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
            "conditions": [],
            "authority": {"decision": "D-940", "category": "B"},
        }]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EXCEPTION_UNSUPPORTED", codes(report))

    def test_exception_scope_wider_than_target_is_rejected(self):
        request = self._candidate()
        contract = request["candidate_contract"]
        p003 = next(p for p in contract["propositions"] if p["id"].endswith("P-003"))
        contract["change_policy"]["propositions"]["NC-F-EC-000b/P-003"]["exceptions_allowed"] = True
        p003["exceptions"] = [{
            "exception_id": "X-001",
            "target_proposition": "NC-F-EC-000b/P-003",
            "effect": "QUALIFY",
            "scope": {"systems": ["B-04", "B-09"], "domain": "FORMULA_ARITHMETIC",
                      "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
            "conditions": [],
            "authority": {"decision": "D-940", "category": "B"},
        }]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCOPE_MISMATCH", codes(report))

    def test_conditional_and_multiple_exceptions_fail_closed(self):
        for sentence in (
            "An exception applies only when the treasury subsystem calculates.",
            "The treasury subsystem may use binary representation, and the audit subsystem may use decimal representation.",
            "Numeric calculations may use an alternative representation notwithstanding the prohibition.",
        ):
            with self.subTest(sentence=sentence):
                request = cv.build_negative("D-990", 0)
                clause = cv.BASELINE_CLAUSES["F-EC-000b"] + " " + sentence
                request["candidate_document"] = cv.replace_clause(cv.read(cv.B04), "F-EC-000b", clause)
                report = cv.validate_amendment(request)
                self.assertFalse(report["accepted"])
                self.assertIn("CONTRACT_EXCEPTION_UNSUPPORTED", codes(report))

    def test_unknown_predicate_is_rejected(self):
        request = self._candidate()
        prop = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-007"))
        prop["predicate"] = "MAY_USE_REPRESENTATION"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCHEMA_INVALID", codes(report))

    def test_unknown_exception_effect_is_rejected(self):
        request = self._candidate()
        contract = request["candidate_contract"]
        p003 = next(p for p in contract["propositions"] if p["id"].endswith("P-003"))
        contract["change_policy"]["propositions"]["NC-F-EC-000b/P-003"]["exceptions_allowed"] = True
        p003["exceptions"] = [{
            "exception_id": "X-001", "target_proposition": "NC-F-EC-000b/P-003",
            "effect": "ALLOW",
            "scope": {"systems": ["B-04"], "domain": "FORMULA_ARITHMETIC",
                      "persistence": "WITHIN_TURN", "inheritance": "NONE", "distinct_from": []},
            "conditions": [],
            "authority": {"decision": "D-940", "category": "B"},
        }]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCHEMA_INVALID", codes(report))

    def test_treasury_scope_permission_without_exception_is_rejected(self):
        request = cv.build_negative("D-990", 0)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EXCEPTION_UNSUPPORTED", codes(report))


class FingerprintAndDeterminismTests(unittest.TestCase):
    def test_contract_fingerprint_mutation_is_detected(self):
        artifacts = cv.load_artifacts()
        index = copy.deepcopy(artifacts["index"])
        index["contracts"][0]["contract_sha256"] = "0" * 64
        artifacts["index"] = index
        problems = cv.validate_registry(artifacts, cv.read(cv.DECISIONS))
        self.assertIn("CONTRACT_FINGERPRINT_MISMATCH",
                      {p["code"] for p in problems})

    def test_projection_fingerprint_mutation_is_detected(self):
        artifacts = cv.load_artifacts()
        index = copy.deepcopy(artifacts["index"])
        index["contracts"][0]["projection_sha256"] = "1" * 64
        artifacts["index"] = index
        problems = cv.validate_registry(artifacts, cv.read(cv.DECISIONS))
        self.assertIn("CONTRACT_PROJECTION_MISMATCH",
                      {p["code"] for p in problems})

    def test_wrong_previous_source_hash_is_rejected(self):
        request = cv.build_typed_positive()
        request["candidate_contract"]["baseline_source_hash"] = "2" * 64
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_FINGERPRINT_MISMATCH", codes(report))

    def test_wrong_source_document_is_rejected(self):
        request = cv.build_typed_positive()
        request["candidate_contract"]["source_document"] = (
            "docs/stage-2/20_fair_play_and_player_protection.md")
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_SCOPE_MISMATCH", codes(report))

    def test_semantic_failure_cannot_be_overridden_by_valid_hashes(self):
        request = cv.build_negative("D-999", 0)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_PROPOSITION_CONFLICT", codes(report))
        # The manifest hashes were valid; the rejection is semantic.
        self.assertNotIn("CONTRACT_FINGERPRINT_MISMATCH", codes(report))

    def test_repeated_proposition_serialization_is_identical(self):
        request = cv.build_typed_positive()
        first = cv.validate_amendment(request)
        second = cv.validate_amendment(request)
        self.assertEqual(cv.canonical_json(first), cv.canonical_json(second))

    def test_no_network_or_random_dependency(self):
        source = cv.read(MODULE_PATH)
        for token in ("import socket", "import urllib", "import requests",
                      "import random", "from socket", "from urllib", "from requests"):
            self.assertNotRegex(source, r"(?m)^\s*" + token)


class RegistryProductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = cv.validate_production()

    def test_production_validation_passes(self):
        failures = [cv.fmt(p) for c in self.report["checks"] if not c["passed"] for p in c["problems"]]
        self.assertEqual(self.report["status"], "PASS", failures)

    def test_all_nine_checks_present(self):
        self.assertEqual([c["id"] for c in self.report["checks"]],
                         [f"C-0{i}" for i in range(1, 10)])

    def test_production_evidence_has_no_reviewed_supports(self):
        self.assertEqual(self.report["evidence"]["reviewed"], 0)
        self.assertEqual(self.report["evidence"]["supports"], 0)
        self.assertGreater(self.report["evidence"]["mappings"], 0)

    def test_production_manifest_is_empty(self):
        manifest = json.loads(cv.read(cv.MANIFEST))
        self.assertEqual(manifest.get("amendments"), [])

    def test_preserved_baseline_counts(self):
        baseline = cv.load_artifacts()["index"]["preserved_baseline"]
        self.assertEqual(baseline["active_formulas"], 295)
        self.assertEqual(baseline["parameter_records"], 393)
        self.assertEqual(baseline["b03_carry_ins"], 20)
        self.assertEqual(baseline["registers"], 9)
        self.assertEqual(baseline["retired_formula"], "F-WEP-048")


if __name__ == "__main__":
    unittest.main(verbosity=2)
