#!/usr/bin/env python3
"""Prompt 14A-C3 focused metadata-diff regression tests.

Run: python docs/qa_backups/test_14A_metadata_diff.py

These tests prove that contract-level metadata changes are explicitly reported
with previous/proposed values and a classification derived from the actual
contract, evidence and D-014 authority gates. A metadata change is never made
valid merely by appearing in the diff.
"""

from __future__ import annotations

import copy
import importlib.util
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(HERE, "14A_contract_validator.py")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cv = load_module("contract_validator_c3", MODULE_PATH)


def all_problems(report):
    out = []
    for gate in ("request_gate", "contract_gate", "evidence_gate",
                 "authority_gate", "comparison_gate"):
        out.extend(report.get(gate, {}).get("problems", []))
    return out


def codes(report):
    return {p["code"] for p in all_problems(report)}


def metadata(report, field):
    return next(item for item in report["diff"]["metadata_changes"]
                if item["field"] == field)


class MetadataDiffTests(unittest.TestCase):
    def test_unchanged_contract_has_no_metadata_or_proposition_change(self):
        base = cv.get_trusted_context().contracts["F-EC-000b"]
        diff = cv.diff_contracts(base, copy.deepcopy(base))
        self.assertEqual(diff["all_changed"], [])
        self.assertEqual(diff["contract_changes"], [])
        self.assertEqual({m["field"]: m["classification"] for m in diff["metadata_changes"]},
                         {"contract_version": "UNCHANGED",
                          "effective_decision": "UNCHANGED",
                          "lifecycle_status": "UNCHANGED"})

    def test_authorized_contract_version_change_is_reported(self):
        report = cv.validate_amendment(cv.build_typed_positive())
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])
        item = metadata(report, "contract_version")
        self.assertTrue(item["changed"])
        self.assertEqual(item["previous"], "1.0.0")
        self.assertEqual(item["proposed"], "1.1.0")
        self.assertEqual(item["classification"], "AUTHORIZED")

    def test_unauthorized_effective_decision_change_is_reported_and_rejected(self):
        request = cv.build_typed_positive()
        request["candidate_contract"]["effective_decision"] = "D-957"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        item = metadata(report, "effective_decision")
        self.assertTrue(item["changed"])
        self.assertEqual(item["previous"], "D-238")
        self.assertEqual(item["proposed"], "D-957")
        self.assertEqual(item["classification"], "UNAUTHORIZED")
        self.assertFalse(report["authority_gate"]["passed"])
        self.assertIn("CONTRACT_AUTHORITY_MISMATCH", codes(report))

    def test_unauthorized_lifecycle_change_is_reported_and_rejected(self):
        request = cv.build_typed_positive()
        request["candidate_contract"]["lifecycle_status"] = "RETIRED"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        item = metadata(report, "lifecycle_status")
        self.assertTrue(item["changed"])
        self.assertEqual(item["previous"], "ADOPTED")
        self.assertEqual(item["proposed"], "RETIRED")
        self.assertEqual(item["classification"], "UNAUTHORIZED")
        self.assertFalse(report["authority_gate"]["passed"])

    def test_valid_metadata_change_is_not_a_proposition_change(self):
        report = cv.validate_amendment(cv.build_typed_positive())
        changed_fields = [f for c in report["diff"]["changed"] for f in c["fields"]]
        self.assertFalse(any("contract_version" in f for f in changed_fields))
        self.assertFalse(any("effective_decision" in f for f in changed_fields))
        self.assertFalse(any("lifecycle_status" in f for f in changed_fields))
        self.assertEqual(report["diff"]["added"], ["NC-F-EC-000b/P-007"])
        self.assertTrue(metadata(report, "contract_version")["changed"])
        self.assertTrue(metadata(report, "effective_decision")["changed"])

    def test_combined_proposition_and_metadata_change_reports_both(self):
        report = cv.validate_amendment(cv.build_typed_positive())
        self.assertIn("NC-F-EC-000b/P-007", report["diff"]["added"])
        self.assertTrue(metadata(report, "contract_version")["changed"])
        self.assertTrue(metadata(report, "effective_decision")["changed"])
        self.assertEqual(metadata(report, "contract_version")["classification"],
                         "AUTHORIZED")

    def test_rejected_metadata_change_cannot_be_hidden_by_a_valid_proposition(self):
        request = cv.build_typed_positive()
        request["candidate_contract"]["effective_decision"] = "D-957"
        report = cv.validate_amendment(request)
        self.assertFalse(report["accepted"])
        self.assertIn("NC-F-EC-000b/P-007", report["diff"]["added"])
        self.assertEqual(metadata(report, "effective_decision")["classification"],
                         "UNAUTHORIZED")
        self.assertFalse(report["authority_gate"]["passed"])
        self.assertTrue(report["evidence_gate"]["passed"])

    def test_category_c_metadata_changes_are_classified_provisional(self):
        report = cv.validate_amendment(cv.build_typed_provisional())
        self.assertTrue(report["accepted"], [cv.fmt(p) for p in all_problems(report)])
        version = metadata(report, "contract_version")
        decision = metadata(report, "effective_decision")
        lifecycle = metadata(report, "lifecycle_status")
        self.assertEqual(version["classification"], "PROVISIONAL")
        self.assertEqual(decision["classification"], "PROVISIONAL")
        self.assertEqual(lifecycle["classification"], "PROVISIONAL")
        self.assertEqual(lifecycle["proposed"], "ADOPTED_PROVISIONAL")


if __name__ == "__main__":
    unittest.main(verbosity=2)
