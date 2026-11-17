#!/usr/bin/env python3
"""Prompt 14A-C2 trusted-input and semantic-gate security regression suite.

Run: python docs/qa_backups/test_14A_trusted_amendment_security.py

Every attack uses the public production amendment entry point where the attack
is a request-level override. Fixture-context tests exercise the same validation
code with an explicitly constructed trusted fixture context; they are labelled
and never used by production callers.

Documentation QA only. Deterministic and offline.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(HERE, "14A_contract_validator.py")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cv = load_module("contract_validator_c2", MODULE_PATH)


def all_problems(report):
    out = []
    for gate in ("request_gate", "contract_gate", "evidence_gate",
                 "authority_gate", "comparison_gate"):
        out.extend(report.get(gate, {}).get("problems", []))
    return out


def codes(report):
    return {p["code"] for p in all_problems(report)}


def gate_codes(report, gate):
    return {p["code"] for p in report.get(gate, {}).get("problems", [])}


def plain_request(request):
    """Strip a FixtureRequest down to its JSON request fields."""
    return dict(request)


def insert_text(request, text, position="end"):
    clause = cv.extract_clause(request["candidate_document"], "F-EC-000b")
    if position == "beginning":
        clause = clause.replace(
            "*Provisional (REQ-162).*",
            "*Provisional (REQ-162).* " + text, 1)
    elif position == "between":
        clause = clause.replace(
            "All quantities are integers.",
            "All quantities are integers. " + text, 1)
    elif position == "middle":
        clause = clause.replace(
            "Every division states its rounding:",
            "Every division states its rounding: " + text + ";", 1)
    else:
        clause = clause + " " + text
    request["candidate_document"] = cv.replace_clause(cv.read(cv.B04), "F-EC-000b", clause)
    return request


class TrustedInputBoundaryTests(unittest.TestCase):
    def _base_attack(self):
        return plain_request(cv.build_typed_positive())

    def test_baseline_contract_override_is_rejected(self):
        attack = self._base_attack()
        attack["base_contract"] = {}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_schema_override_is_rejected(self):
        attack = self._base_attack()
        attack["schema"] = {}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_lexicon_override_is_rejected(self):
        attack = self._base_attack()
        attack["lexicon"] = {"concepts": []}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_evidence_mapping_override_is_rejected(self):
        attack = self._base_attack()
        attack["evidence_mappings"] = {"mappings": []}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_decision_register_override_is_rejected(self):
        attack = self._base_attack()
        attack["decisions_text"] = "| D-940 | fabricated |"
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_owner_authorization_override_is_rejected(self):
        attack = self._base_attack()
        attack["owner_authorizations"] = [{"authorization_id": "OA-FAKE"}]
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_projection_template_override_is_rejected(self):
        attack = self._base_attack()
        attack["candidate_template_text"] = "literal injected text"
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_manifest_override_is_rejected(self):
        attack = self._base_attack()
        attack["manifest"] = {"amendments": []}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_alias_overrides_are_rejected(self):
        for key, value in (
            ("baseline_contract", {}),
            ("evidence_registry", {}),
            ("decision_text", "fabricated"),
            ("template", "literal"),
            ("contracts_dir", "/tmp"),
            ("mode", "test"),
            ("context", {}),
        ):
            with self.subTest(key=key):
                attack = self._base_attack()
                attack[key] = value
                report = cv.validate_amendment(attack)
                self.assertFalse(report["accepted"])
                self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_unknown_request_field_is_rejected(self):
        attack = self._base_attack()
        attack["unexpected_note"] = "x"
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_REQUEST_SCHEMA_INVALID", codes(report))

    def test_candidate_contract_cannot_embed_trusted_inputs(self):
        attack = self._base_attack()
        attack["candidate_contract"] = copy.deepcopy(attack["candidate_contract"])
        attack["candidate_contract"]["evidence_mappings"] = {"mappings": []}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_path_traversal_is_rejected(self):
        attack = self._base_attack()
        attack["candidate_contract"] = copy.deepcopy(attack["candidate_contract"])
        attack["candidate_contract"]["source_document"] = "../outside.md"
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertTrue(codes(report) & {"CONTRACT_UNAUTHORIZED_PATH", "CONTRACT_SCOPE_MISMATCH"})

    def test_symlink_redirection_is_rejected(self):
        context = cv.get_trusted_context()
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, "target.md")
            with open(target, "w", encoding="utf-8") as fh:
                fh.write("target")
            link = os.path.join(tmp, "link.md")
            try:
                os.symlink(target, link)
            except OSError:
                # Windows may require elevated privileges to create a symlink;
                # simulate the guard deterministically so the path-protection
                # branch is still exercised.
                original = os.path.islink
                os.path.islink = lambda candidate: candidate.endswith("link.md")
                try:
                    with self.assertRaises(cv.TrustedPathError):
                        context.resolve("link.md", root=tmp)
                finally:
                    os.path.islink = original
            else:
                with self.assertRaises(cv.TrustedPathError):
                    context.resolve("link.md", root=tmp)

    def test_fabricated_d940_without_override_is_authority_failure(self):
        attack = self._base_attack()
        attack["decision_ref"] = "D-940"
        attack["candidate_contract"] = copy.deepcopy(attack["candidate_contract"])
        attack["candidate_contract"]["effective_decision"] = "D-940"
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))
        self.assertNotIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_fabricated_d940_with_register_injection_is_override(self):
        attack = self._base_attack()
        attack["decision_ref"] = "D-940"
        attack["decisions_text"] = (
            "| D-940 | 2026-11-16 | fabricated | Previous contract: NC-F-EC-000b 1.0.0; "
            "Replacement contract: NC-F-EC-000b 1.1.0 | **Confirmed** (Category B) | evidence | source | consequences |")
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))


class EvidenceRevalidationTests(unittest.TestCase):
    def _with_mapping(self, mapping):
        request = cv.build_typed_positive()
        context = request.fixture_context
        mappings = context.mappings
        mappings["mappings"] = [m for m in mappings["mappings"]
                                if m.get("evidence_id") != "EV-TEST-P-007"]
        mappings["mappings"].append(mapping)
        return cv.validate_amendment(request)

    def _mapping(self):
        request = cv.build_typed_positive()
        return copy.deepcopy(next(
            m for m in request.fixture_context.mappings["mappings"]
            if m.get("evidence_id") == "EV-TEST-P-007"))

    def test_fabricated_source_path_is_rejected(self):
        mapping = self._mapping()
        mapping["document_path"] = "docs/stage-2/does_not_exist.md"
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertTrue(gate_codes(report, "evidence_gate") &
                        {"CONTRACT_EVIDENCE_INTEGRITY_FAILED", "CONTRACT_UNAUTHORIZED_PATH"})

    def test_nonexistent_section_is_rejected(self):
        mapping = self._mapping()
        mapping["section"] = "99.9"
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_INTEGRITY_FAILED", codes(report))

    def test_invented_quotation_is_rejected(self):
        mapping = self._mapping()
        mapping["excerpt"] = "An invented quotation that never existed in the source."
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_INTEGRITY_FAILED", codes(report))

    def test_zero_hash_is_rejected(self):
        mapping = self._mapping()
        mapping["document_sha256"] = "0" * 64
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_INTEGRITY_FAILED", codes(report))

    def test_stale_hash_is_rejected(self):
        mapping = self._mapping()
        mapping["document_sha256"] = "a" * 64
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_INTEGRITY_FAILED", codes(report))

    def test_placeholder_reviewer_is_rejected(self):
        mapping = self._mapping()
        mapping["review"]["reviewed_by"] = "TBD"
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_NOT_REVIEWED", codes(report))

    def test_implementation_actor_as_reviewer_is_rejected(self):
        mapping = self._mapping()
        mapping["review"]["reviewed_by"] = mapping["implementation_actor"]
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_NOT_REVIEWED", codes(report))

    def test_unsupported_supports_without_review_is_rejected(self):
        mapping = self._mapping()
        mapping["review"]["review_status"] = "NOT_REVIEWED"
        mapping["classification"] = "NOT_REVIEWED"
        mapping["proposed_classification"] = "SUPPORTS"
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_NOT_REVIEWED", codes(report))

    def test_contradictory_evidence_is_rejected(self):
        mapping = self._mapping()
        mapping["classification"] = "CONTRADICTS"
        report = self._with_mapping(mapping)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS", codes(report))

    def test_partial_coverage_is_rejected(self):
        request = cv.build_typed_positive()
        candidate = copy.deepcopy(request["candidate_contract"])
        prop = copy.deepcopy(next(p for p in candidate["propositions"]
                                  if p["id"].endswith("P-007")))
        prop["id"] = "NC-F-EC-000b/P-008"
        prop["subject"] = "ALL_QUANTITIES"
        candidate["propositions"].append(prop)
        candidate["change_policy"]["propositions"]["NC-F-EC-000b/P-008"] = {
            "category": "B", "owner_reserved": False,
            "evidence_required_on_change": True, "baseline_unresolved": False,
            "exceptions_allowed": False}
        candidate["rendering"]["fragments"].append({
            "proposition_id": "NC-F-EC-000b/P-008",
            "template": "A second added proposition is present."})
        rendered, _ = cv.render_contract(candidate)
        request["candidate_contract"] = candidate
        request["candidate_document"] = cv.replace_clause(
            cv.read(cv.B04), "F-EC-000b", rendered)
        request["evidence_refs"] = ["EV-TEST-P-007"]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertTrue(gate_codes(report, "evidence_gate") &
                        {"CONTRACT_EVIDENCE_MAPPING_MISSING",
                         "CONTRACT_EVIDENCE_NOT_REVIEWED"})

    def test_request_created_mapping_is_rejected(self):
        attack = plain_request(cv.build_typed_positive())
        attack["evidence_mappings"] = {"mappings": [self._mapping()]}
        report = cv.validate_amendment(attack)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_TRUSTED_INPUT_OVERRIDE", codes(report))

    def test_synthetic_review_cannot_pass_production_context(self):
        mapping = self._mapping()
        self.assertIn("SYNTHETIC", mapping["review"]["reviewed_by"])
        # The production registry contains no reviewed mappings at all.
        production = cv.get_trusted_context()
        self.assertEqual([m for m in production.mappings["mappings"]
                          if m["review"]["review_status"] == "REVIEWED"], [])
        self.assertFalse(cv.has_supports_review("NC-F-EC-000b/P-005",
                                                production.mappings,
                                                mode="production"))


class MaterialCoverageTests(unittest.TestCase):
    INSERTIONS = {
        "beginning": "B-04 binary floating-point calculations are permitted.",
        "between": "B-04 binary floating-point calculations are permitted.",
        "middle": "B-04 binary floating-point calculations are permitted",
        "end": "B-04 binary floating-point calculations are permitted.",
        "alternative": "B-04 calculations may use radix-two exponent and significand encoding.",
    }

    def test_insertions_are_detected_by_complete_span_accounting(self):
        for position, text in self.INSERTIONS.items():
            with self.subTest(position=position):
                request = cv.build_typed_positive()
                insert_text(request, text, position if position in
                            ("beginning", "between", "middle") else "end")
                coverage = cv.material_coverage(
                    request["candidate_contract"],
                    cv.extract_clause(request["candidate_document"], "F-EC-000b"))
                self.assertFalse(coverage["exact"])
                self.assertTrue(coverage["uncovered_material"])
                self.assertLess(coverage["ratio"], 1.0)

    def test_insertions_are_rejected_through_the_amendment_path(self):
        for position, text in self.INSERTIONS.items():
            with self.subTest(position=position):
                request = cv.build_typed_positive()
                insert_text(request, text, position if position in
                            ("beginning", "between", "middle") else "end")
                report = cv.validate_amendment(request)
                self.assertFalse(report["accepted"])
                self.assertTrue(codes(report) & {
                    "CONTRACT_PROJECTION_MISMATCH", "CONTRACT_COVERAGE_GAP",
                    "CONTRACT_PROPOSITION_CONFLICT"})
                self.assertNotIn("CONTRACT_EVIDENCE_MISSING", codes(report))

    def test_duplicate_sentence_is_detected(self):
        request = cv.build_typed_positive()
        clause = cv.extract_clause(request["candidate_document"], "F-EC-000b")
        duplicated = clause + " All quantities are integers."
        request["candidate_document"] = cv.replace_clause(cv.read(cv.B04), "F-EC-000b", duplicated)
        coverage = cv.material_coverage(request["candidate_contract"], duplicated)
        self.assertTrue(coverage["duplicates"])
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertTrue(codes(report) & {"CONTRACT_COVERAGE_GAP", "CONTRACT_PROPOSITION_CONFLICT"})

    def test_unknown_proposition_in_prose_is_rejected(self):
        request = cv.build_wording_positive()
        clause = cv.extract_clause(request["candidate_document"], "F-EC-000b")
        request["candidate_document"] = cv.replace_clause(
            cv.read(cv.B04), "F-EC-000b",
            clause + " The treasury may apply a discretionary surcharge.")
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertTrue(codes(report) & {
            "CONTRACT_UNPARSED_MATERIAL_SEGMENT", "CONTRACT_UNMAPPED_TERM"})

    def test_trailing_qualification_is_rejected(self):
        request = cv.build_wording_positive()
        clause = cv.extract_clause(request["candidate_document"], "F-EC-000b")
        request["candidate_document"] = cv.replace_clause(
            cv.read(cv.B04), "F-EC-000b",
            clause + " unless a later register revision says otherwise.")
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertTrue(codes(report) & {
            "CONTRACT_EXCEPTION_UNSUPPORTED", "CONTRACT_UNPARSED_MATERIAL_SEGMENT"})

    def test_scope_timing_and_unit_insertions_are_rejected(self):
        for sentence in (
            "The global register may use decimal fractions.",
            "Residual sub-unit amounts are carried into the next turn.",
            "A percentage is a decimal fraction of the whole.",
        ):
            with self.subTest(sentence=sentence):
                request = cv.build_wording_positive()
                clause = cv.extract_clause(request["candidate_document"], "F-EC-000b")
                request["candidate_document"] = cv.replace_clause(
                    cv.read(cv.B04), "F-EC-000b", clause + " " + sentence)
                report = cv.validate_amendment(request)
                self.assertFalse(report["accepted"])
                self.assertTrue(codes(report) & {
                    "CONTRACT_PROPOSITION_CONFLICT",
                    "CONTRACT_UNPARSED_MATERIAL_SEGMENT",
                    "CONTRACT_UNMAPPED_TERM",
                    "CONTRACT_EVIDENCE_NOT_REVIEWED",
                    "CONTRACT_EVIDENCE_CLASSIFICATION_NOT_SUPPORTS"})

    def test_typed_rendering_only_contradiction_is_rejected(self):
        request = cv.build_typed_positive()
        candidate = copy.deepcopy(cv.get_trusted_context().contracts["F-EC-000b"])
        candidate["contract_version"] = "1.1.0"
        candidate["effective_decision"] = "D-940"
        for frag in candidate["rendering"]["fragments"]:
            if frag["proposition_id"].endswith("P-003"):
                frag["template"] = "Binary floating-point calculations are permitted."
        rendered, _ = cv.render_contract(candidate)
        request["candidate_contract"] = candidate
        request["candidate_document"] = cv.replace_clause(
            cv.read(cv.B04), "F-EC-000b", rendered)
        request["evidence_refs"] = []
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertTrue(codes(report) & {
            "CONTRACT_PROPOSITION_CONFLICT", "CONTRACT_COVERAGE_GAP",
            "CONTRACT_PROJECTION_MISMATCH"})

    def test_prefix_injection_is_rejected(self):
        request = cv.build_typed_positive()
        candidate = copy.deepcopy(cv.get_trusted_context().contracts["F-EC-000b"])
        candidate["contract_version"] = "1.1.0"
        candidate["effective_decision"] = "D-940"
        candidate["rendering"]["structural_prefix"] = (
            candidate["rendering"]["structural_prefix"]
            + " B-04 binary floating-point calculations are permitted.")
        rendered, render_problems = cv.render_contract(candidate)
        self.assertTrue(render_problems)
        request["candidate_contract"] = candidate
        request["candidate_document"] = cv.replace_clause(
            cv.read(cv.B04), "F-EC-000b", rendered)
        request["evidence_refs"] = []
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_PROJECTION_MISMATCH", codes(report))

    def test_multi_sentence_fragment_is_rejected(self):
        request = cv.build_typed_positive()
        candidate = request["candidate_contract"]
        for frag in candidate["rendering"]["fragments"]:
            if frag["proposition_id"].endswith("P-007"):
                frag["template"] = ("Derived calculations are included. "
                                    "B-04 binary-floating-point calculations are permitted.")
        rendered, render_problems = cv.render_contract(candidate)
        self.assertTrue(any(p["code"] == "CONTRACT_UNPARSED_MATERIAL_SEGMENT"
                            for p in render_problems))
        request["candidate_document"] = cv.replace_clause(
            cv.read(cv.B04), "F-EC-000b", rendered)
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])


class ContractDiffTests(unittest.TestCase):
    def _base(self):
        return cv.build_typed_positive()

    def test_floor_semantics_change_is_visible_in_the_diff(self):
        request = self._base()
        p002 = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-002"))
        p002["object"]["floor_negative"] = "TOWARD_ZERO"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        fields = [f for c in report["diff"]["changed"] for f in c["fields"]]
        self.assertTrue(any("floor_negative" in f for f in fields))

    def test_contract_scope_change_is_a_material_contract_change(self):
        request = self._base()
        request["candidate_contract"]["scope"]["systems"] = ["B-04", "B-09"]
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_CONTRACT_FIELD_CHANGE", codes(report))
        self.assertFalse(report["comparison_gate"]["passed"])

    def test_change_policy_weakening_is_a_material_contract_change(self):
        request = self._base()
        request["candidate_contract"]["change_policy"]["propositions"][
            "NC-F-EC-000b/P-003"]["evidence_required_on_change"] = False
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_CONTRACT_FIELD_CHANGE", codes(report))

    def test_numerical_status_change_is_a_material_contract_change(self):
        request = self._base()
        request["candidate_contract"]["numerical_status"] = "OWNER-APPROVED VALUE"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("CONTRACT_CONTRACT_FIELD_CHANGE", codes(report))

    def test_units_timing_and_authority_changes_are_gated(self):
        request = self._base()
        p003 = next(p for p in request["candidate_contract"]["propositions"]
                    if p["id"].endswith("P-003"))
        p003["units"] = {"dimension": "RATE", "unit": "BASIS_POINT"}
        p003["timing"]["persistence"] = "ACROSS_TURNS"
        p003["authority"]["category"] = "A"
        p003["authority"]["owner_reserved"] = True
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertTrue(codes(report) & {
            "CONTRACT_SCHEMA_INVALID", "CONTRACT_AUTHORITY_MISMATCH",
            "CONTRACT_CONTRACT_FIELD_CHANGE"})
        fields = [f for c in report["diff"]["changed"] for f in c["fields"]]
        self.assertTrue(any(".units" in f for f in fields))
        self.assertTrue(any(".timing" in f for f in fields))
        self.assertTrue(any(".authority" in f for f in fields))


class PositiveRegressionTests(unittest.TestCase):
    def test_baseline_wording_typed_b_provisional_and_owner_a_pass(self):
        fixtures = (
            ("baseline", cv._fixture_request(
                cv._fixture_ctx(), amendment_id="TEST-BASELINE",
                target_contract="NC-F-EC-000b",
                candidate_document=cv.read(cv.B04),
                candidate_contract=None, evidence_refs=[],
                decision_ref="D-957")),
            ("wording", cv.build_wording_positive()),
            ("typed-B", cv.build_typed_positive()),
            ("typed-C", cv.build_typed_provisional()),
            ("owner-A", cv.build_owner_authorized()),
        )
        for label, request in fixtures:
            with self.subTest(label=label):
                report = cv.validate_amendment(request)
                self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])

    def test_b09_within_turn_cumulative_accrual_remains_valid(self):
        contract, problems = cv.build_b09_within_turn()
        self.assertEqual(problems, [])
        self.assertEqual(contract["scope"]["systems"], ["B-09"])
        b09 = cv.read(cv.B09)
        for needle in ("F-AL-006", "cumulative", "10{,}000",
                       "Different assets keep separate accumulators"):
            self.assertIn(needle, b09)

    def test_gate_independence_is_preserved(self):
        unsupported = cv.validate_amendment(cv.build_typed_unsupported_evidence())
        self.assertFalse(unsupported["accepted"])
        self.assertFalse(unsupported["evidence_gate"]["passed"])
        self.assertTrue(unsupported["authority_gate"]["passed"])
        missing = cv.validate_amendment(cv.build_missing_authority())
        self.assertFalse(missing["accepted"])
        self.assertTrue(missing["evidence_gate"]["passed"])
        self.assertFalse(missing["authority_gate"]["passed"])


class DeterminismTests(unittest.TestCase):
    def test_repeated_attack_reports_are_identical(self):
        attack = plain_request(cv.build_typed_positive())
        attack["schema"] = {}
        first = cv.validate_amendment(attack)
        second = cv.validate_amendment(attack)
        self.assertEqual(cv.canonical_json(first), cv.canonical_json(second))

    def test_no_network_or_random_dependency(self):
        source = cv.read(MODULE_PATH)
        for token in ("import socket", "import urllib", "import requests",
                      "import random", "from socket", "from urllib", "from requests"):
            self.assertNotRegex(source, r"(?m)^\s*" + token)


if __name__ == "__main__":
    unittest.main(verbosity=2)
