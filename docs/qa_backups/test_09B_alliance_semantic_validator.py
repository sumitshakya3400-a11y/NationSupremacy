#!/usr/bin/env python3
"""
test_09B_alliance_semantic_validator.py - fixtures for the Prompt 09B-I
Alliance semantic validator.

The suite proves three things:

  1. The corrected canonical corpus passes every semantic check.
  2. A corpus with UD-046 still Open passes when every illustrative treasury
     threshold (50,000 crowns, 10%) is removed: no numeric value is required.
  3. Reintroducing any defect class - owner-reserved leakage, delegation,
     treasury approval overclaims, mandatory hierarchy, phantom ids, status
     contradictions, disguised succession/appeal policy, negative-polarity
     entitlements, premature 09C work - makes validation fail.

Fixtures A-H cover the authority regressions: timestamp-decided succession,
a mandatory appeal path, a neutralized rule whose policy moves into a
contract, one unauthorized settlement of each owner-reserved subject, and
the two compound disclaimer-plus-mandate sentences that defeated the earlier
sentence-level negation check. Fixtures I-M cover appeal policy asserted
through negative polarity: expulsion barred without an appeal, deprivation
of an appeal barred, expulsion conditioned on an appeal, appeals prohibited,
and a duty to allow appeals. Fixtures N-P cover denial framed as protection
and entitlements hidden in except-that or unless branches. C24 adds the
equivalent claimant-bypass and succession-denial constructions, with positive
controls that keep neutral recordkeeping, audit evidence and genuine
prohibitions valid.

Prompt 09B-I adds C27-C31: owner-consented taxation, voluntary donations,
the ALL-093 tombstone and its independent safeguards, the separate Alliance
treaty object with NAP consent, and the mandatory server-side same-Alliance
attack ban. Fixtures Q-U exercise each guard and its positive control, and
regression tests keep the withdrawn ALL-093 confiscation clause from
returning. Prompt 09B-K completes C27 with the production-tax failure codes,
the ARL naming in REQ-626, the provisional multiple-membership 0% safeguard
and the production-chain accounting tokens, and adds the final positive
appeal-grant fixtures 177-198. Prompt 09B-L adds the retained, preserved,
reviewable and avenue-of-appeal fixtures (210-225), the C32 ARL/operational
funding guards (226-235), the C33 treaty-effect guards (236-243), the C34
tax-boundary guards (244-249) and the per-Alliance assignment fixtures
(250-252). Prompt 09B-P adds the three final audited C25 cases (262-264) and
their six compact policy, ambiguity and non-normative controls (265).

Run:
    python docs/qa_backups/test_09B_alliance_semantic_validator.py -v
"""

from __future__ import annotations

import importlib.util
import os
import re
import shutil
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "validate_semantic",
    Path(__file__).resolve().parent / "09B_validate_alliance_semantic.py",
)
VAL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VAL)
run_checks = VAL.run_checks
run_checks_with_review = VAL.run_checks_with_review
STATUS_SENTENCE = VAL.STATUS_SENTENCE


def _link_or_copy(src: str, dst: str) -> str:
    """Share the read-only baseline inode; fall back to a real copy off-volume."""
    try:
        os.link(src, dst)
    except OSError:
        return shutil.copy2(src, dst)
    return dst


class AllianceSemanticValidatorTests(unittest.TestCase):
    """Clean fixture, threshold-removal regression and negative defect fixtures."""

    @classmethod
    def setUpClass(cls):
        cls.real_root = Path(__file__).resolve().parent.parent.parent
        cls.pristine = tempfile.TemporaryDirectory()
        cls.pristine_docs = Path(cls.pristine.name) / "docs"
        shutil.copytree(cls.real_root / "docs", cls.pristine_docs, copy_function=shutil.copy2)

    @classmethod
    def tearDownClass(cls):
        cls.pristine.cleanup()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(
            self.pristine_docs,
            self.root / "docs",
            copy_function=_link_or_copy,
        )

    def tearDown(self):
        self.tmp.cleanup()

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    def path(self, relative: str) -> Path:
        return self.root / "docs" / relative

    def read(self, relative: str) -> str:
        return self.path(relative).read_text(encoding="utf-8")

    def write(self, relative: str, content: str) -> None:
        target = self.path(relative)
        target.unlink(missing_ok=True)
        target.write_text(content, encoding="utf-8")

    def modify(self, relative: str, find: str, replace: str, count: int = 1) -> None:
        content = self.read(relative)
        self.assertIn(find, content, f"Fixture setup error: {find!r} not in {relative}")
        if count < 0:
            content = content.replace(find, replace)
        else:
            content = content.replace(find, replace, count)
        self.write(relative, content)

    def append(self, relative: str, sentence: str) -> None:
        content = self.read(relative).rstrip() + "\n\n" + sentence + "\n"
        self.write(relative, content)

    def inject_all079(self, sentence: str) -> None:
        self.modify(
            "stage-2/16_alliances.md",
            "**`ALL-079` (Membership States):** A nation account",
            f"**`ALL-079` (Membership States):** {sentence} A nation account",
        )

    def inject_all057(self, sentence: str) -> None:
        self.modify(
            "stage-2/16_alliances.md",
            "**`ALL-057` (Competing Succession Claims — Audit Evidence Only):** If competing",
            f"**`ALL-057` (Competing Succession Claims — Audit Evidence Only):** {sentence} If competing",
        )

    def section_modify(
        self,
        relative: str,
        start: str,
        find: str,
        replace: str,
        end: str | None = None,
        count: int = 1,
    ) -> None:
        content = self.read(relative)
        begin = content.index(start)
        finish = content.index(end, begin) if end else len(content)
        section = content[begin:finish]
        self.assertIn(find, section, f"Fixture setup error: {find!r} not in section {start!r}")
        if count < 0:
            section = section.replace(find, replace)
        else:
            section = section.replace(find, replace, count)
        self.write(relative, content[:begin] + section + content[finish:])

    def _row_bounds(self, relative: str, row_id: str) -> tuple[list[str], int, int]:
        lines = self.read(relative).splitlines(keepends=True)
        for index, line in enumerate(lines):
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells and cells[0].strip("*` ").strip() == row_id:
                return lines, index, len(cells)
        raise AssertionError(f"Fixture setup error: row {row_id} not found in {relative}")

    def set_row_cell(self, relative: str, row_id: str, cell_index: int, value: str) -> None:
        lines, index, cell_count = self._row_bounds(relative, row_id)
        cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
        cells[cell_index] = f" {value} "
        lines[index] = "| " + " | ".join(cell.strip() for cell in cells) + " |\n"
        self.write(relative, "".join(lines))

    def modify_row_cell(
        self, relative: str, row_id: str, cell_index: int, find: str, replace: str
    ) -> None:
        lines, index, _ = self._row_bounds(relative, row_id)
        cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
        self.assertIn(find, cells[cell_index], f"Fixture setup error: {find!r} not in {row_id}")
        cells[cell_index] = cells[cell_index].replace(find, replace, 1)
        lines[index] = "| " + " | ".join(cell.strip() for cell in cells) + " |\n"
        self.write(relative, "".join(lines))

    def delete_row(self, relative: str, row_id: str) -> None:
        lines, index, _ = self._row_bounds(relative, row_id)
        del lines[index]
        self.write(relative, "".join(lines))

    def assert_failure(self, failures: list[str], code: str, needle: str | None = None) -> None:
        matches = [
            failure
            for failure in failures
            if code in failure and (needle is None or needle.lower() in failure.lower())
        ]
        rendered = " | ".join(failures[:8]).encode("ascii", "replace").decode("ascii")
        self.assertTrue(
            matches,
            f"Expected a {code} failure"
            + (f" containing {needle!r}" if needle else "")
            + f"; got: {rendered}",
        )

    def assert_clean(self) -> None:
        failures, reviews = run_checks_with_review(self.root)
        rendered = " | ".join(failures[:8]).encode("ascii", "replace").decode("ascii")
        self.assertEqual(failures, [], f"Fixture should pass cleanly, got: {rendered}")
        rendered_reviews = " | ".join(reviews[:8]).encode("ascii", "replace").decode("ascii")
        self.assertEqual(
            reviews,
            [],
            f"Fixture should have no review findings, got: {rendered_reviews}",
        )

    # ------------------------------------------------------------------
    # clean fixtures
    # ------------------------------------------------------------------
    def test_00_real_workspace_passes(self):
        """The corrected canonical workspace passes all 34 checks."""
        failures, reviews = run_checks_with_review(self.real_root)
        rendered = " | ".join(failures[:8]).encode("ascii", "replace").decode("ascii")
        self.assertEqual(failures, [], f"Real workspace should pass cleanly, got: {rendered}")
        rendered_reviews = " | ".join(reviews[:8]).encode("ascii", "replace").decode("ascii")
        self.assertEqual(
            reviews,
            [],
            f"Real workspace should have no review findings, got: {rendered_reviews}",
        )

    def test_01_clean_fixture_passes(self):
        """A pristine copy of docs/ passes all checks."""
        self.assert_clean()

    def test_02_threshold_removal_still_passes(self):
        """UD-046 stays Open and the project passes with 50,000 and 10% removed."""
        relative = "stage-2/16_alliances_formula_register.md"
        content = self.read(relative)
        content, removed_crowns = re.subn(r"50,000", "", content)
        content, removed_percent = re.subn(r"10\\?%", "", content)
        self.assertGreater(removed_crowns, 0)
        self.assertGreater(removed_percent, 0)
        self.write(relative, content)
        self.assert_clean()

    # ------------------------------------------------------------------
    # C01 - rulebook completeness and status
    # ------------------------------------------------------------------
    def test_03_duplicate_rule_definition_fails(self):
        relative = "stage-2/16_alliances.md"
        self.modify(
            relative,
            "- **`ALL-001` (Authoritative Document):**",
            "- **`ALL-001` (Duplicate Definition):** duplicate.\n"
            "- **`ALL-001` (Authoritative Document):**",
        )
        self.assert_failure(run_checks(self.root), "[C01]", "ALL-001")

    def test_04_missing_rule_definition_fails(self):
        self.modify(
            "stage-2/16_alliances.md",
            "- **`ALL-226` (`UD-046` Boundary and Non-Implementation Status):**",
            "- **REMOVED-226:**",
        )
        self.assert_failure(run_checks(self.root), "[C01]", "ALL-001..ALL-226")

    def test_05_header_version_regression_fails(self):
        self.modify("stage-2/16_alliances.md", "**Version:** 2.8", "**Version:** 2.7")
        self.assert_failure(run_checks(self.root), "[C01]", "v2.8")

    def test_06_b09_status_sentence_removed_fails(self):
        self.modify("stage-2/16_alliances.md", STATUS_SENTENCE, "Status withheld.", count=-1)
        self.assert_failure(run_checks(self.root), "[C01]", "status sentence")

    # ------------------------------------------------------------------
    # C02 - AX inventory and field completeness
    # ------------------------------------------------------------------
    def test_07_missing_ax_section_fails(self):
        self.modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-16 — Alliance Diplomatic Positions (Non-Binding)",
            "### AX-16 (Removed) — Alliance Diplomatic Positions (Non-Binding)",
        )
        self.assert_failure(run_checks(self.root), "[C02]", "AX-16")

    def test_08_empty_ax_field_fails(self):
        relative = "stage-2/16_alliances_integration_contracts.md"
        content = self.read(relative)
        begin = content.index("### AX-07 —")
        finish = content.index("### AX-08 —", begin)
        section = re.sub(
            r"(\| \*\*Failure Behaviour\*\* \|)[^|\n]*\|",
            r"\1  |",
            content[begin:finish],
            count=1,
        )
        self.assertNotEqual(section, content[begin:finish])
        self.write(relative, content[:begin] + section + content[finish:])
        self.assert_failure(run_checks(self.root), "[C02]", "Failure Behaviour")

    def test_09_ax_id_mismatch_fails(self):
        self.section_modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-05 —",
            "`AX-05`",
            "`AX-06`",
            end="### AX-06 —",
        )
        self.assert_failure(run_checks(self.root), "[C02]", "AX ID")

    def test_10_ax_title_drift_fails(self):
        self.section_modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-08 —",
            "| **Integration Title** | Alliance Resource Storage Limits |",
            "| **Integration Title** | Alliance Warehouse Capacity Rules |",
            end="### AX-09 —",
        )
        self.assert_failure(run_checks(self.root), "[C02]", "AX-08")

    # ------------------------------------------------------------------
    # C03 - AX status authority
    # ------------------------------------------------------------------
    def test_11_candidate_contract_claims_approval_fails(self):
        self.section_modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-07 —",
            "Open under UD-046",
            "Approved",
            end="### AX-08 —",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C03]", "AX-07")

    def test_12_ax19_not_provisional_fails(self):
        self.section_modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-19 —",
            "Provisional",
            "Confirmed",
            end="### AX-20 —",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C05]", "AX-19")

    # ------------------------------------------------------------------
    # C08 - UD-039 reconciliation
    # ------------------------------------------------------------------
    def test_13_ud039_status_regression_fails(self):
        self.set_row_cell("stage-2/05_unresolved_design_decisions.md", "UD-039", -1, "**Deferred**")
        self.assert_failure(run_checks(self.root), "[C08]", "UD-039")

    def test_14_d137_status_regression_fails(self):
        self.set_row_cell("DECISIONS.md", "D-137", 4, "Provisional (diplomatic design)")
        self.assert_failure(run_checks(self.root), "[C08]", "D-137")

    def test_15_b09_ud039_ledger_reopened_fails(self):
        self.set_row_cell("stage-2/16_alliances.md", "UD-039", 3, "**Open**")
        self.assert_failure(run_checks(self.root), "[C08]", "UD-039")

    def test_16_ud039_delegation_claim_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "UD-039 permits an alliance representative to sign treaties on behalf of a member nation.",
        )
        self.assert_failure(run_checks(self.root), "[C08]", "UD-039")

    # ------------------------------------------------------------------
    # C09 - owner-reserved decisions remain Open
    # ------------------------------------------------------------------
    def test_17_ud046_falsely_resolved_fails(self):
        self.set_row_cell(
            "stage-2/05_unresolved_design_decisions.md",
            "UD-046",
            -1,
            "**Resolved** by Prompt 09B.",
        )
        self.assert_failure(run_checks(self.root), "[C09]", "UD-046")

    def test_18_b09_ledger_marks_owner_decision_resolved_fails(self):
        self.set_row_cell("stage-2/16_alliances.md", "UD-045", 3, "**Resolved**")
        self.assert_failure(run_checks(self.root), "[C09]", "UD-045")

    def test_19_dd153_false_approval_fails(self):
        self.set_row_cell(
            "stage-2/04_approved_and_provisional_decisions.md",
            "DD-153",
            2,
            "**Approved** (candidate exit rule)",
        )
        self.assert_failure(run_checks(self.root), "[C09]", "DD-153")

    def test_20_decision_falsely_resolves_owner_question_fails(self):
        self.modify_row_cell(
            "DECISIONS.md",
            "D-138",
            3,
            "In strict accordance with",
            "This resolves UD-044. In strict accordance with",
        )
        self.assert_failure(run_checks(self.root), "[C09]", "UD-044")

    def test_21_prose_false_resolution_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "UD-046 is now resolved by the design team.",
        )
        self.assert_failure(run_checks(self.root), "[C09]", "UD-046")

    # ------------------------------------------------------------------
    # C10 - sensitive rule authority anchors
    # ------------------------------------------------------------------
    def test_22_all176_settled_treasury_claim_fails(self):
        self.modify(
            "stage-2/16_alliances.md",
            "must not be described as settled",
            "is settled",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C10]", "ALL-176")

    def test_23_all125_delegation_anchor_removed_fails(self):
        self.section_modify(
            "stage-2/16_alliances.md",
            "- **`ALL-125`",
            "silence never constitutes consent",
            "silence may constitute consent",
            end="- **`ALL-126`",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C10]", "ALL-125")

    def test_24_all124_owner_reservation_removed_fails(self):
        self.section_modify(
            "stage-2/16_alliances.md",
            "- **`ALL-124`",
            "unapproved",
            "approved",
            end="- **`ALL-125`",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C10]", "ALL-124")

    def test_25_all166_owner_reservation_removed_fails(self):
        self.section_modify(
            "stage-2/16_alliances.md",
            "- **`ALL-166`",
            "UD-048",
            "UD-999",
            end="- **`ALL-167`",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C10]", "ALL-166")

    # ------------------------------------------------------------------
    # C11 - constitutional neutrality
    # ------------------------------------------------------------------
    def test_26_mandatory_leader_office_fails(self):
        self.append("stage-2/16_alliances.md", "The engine requires a mandatory Leader office.")
        self.assert_failure(run_checks(self.root), "[C11]", "leader")

    def test_27_fixed_position_cap_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The game enforces a fixed cap of 20 custom positions.",
        )
        self.assert_failure(run_checks(self.root), "[C11]", "20-position")

    def test_28_constitution_deadline_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "A constitution must be created within 12 turns.",
        )
        self.assert_failure(run_checks(self.root), "[C11]", "deadline")

    def test_29_mandatory_impeachment_threshold_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The rulebook imposes a mandatory 75% impeachment threshold.",
        )
        self.assert_failure(run_checks(self.root), "[C11]", "impeachment")

    def test_30_phantom_rule_citation_fails(self):
        self.append("stage-2/16_alliances.md", "See ALL-282 for the default succession model.")
        self.assert_failure(run_checks(self.root), "[C11]", "ALL-282")

    # ------------------------------------------------------------------
    # C12 - diplomatic sovereignty and zero delegation
    # ------------------------------------------------------------------
    def test_31_alliance_leader_signs_treaty_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "An alliance leader may sign a treaty on behalf of a member nation.",
        )
        self.assert_failure(run_checks(self.root), "[C12]", "delegation")

    def test_32_silence_as_consent_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Silence is treated as consent for alliance treaties.",
        )
        self.assert_failure(run_checks(self.root), "[C12]", "silence")

    def test_33_majority_binds_sovereign_nation_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "A majority vote binds every member nation to the alliance treaty.",
        )
        self.assert_failure(run_checks(self.root), "[C12]", "majority")

    def test_34_delegate_capability_reintroduced_fails(self):
        self.append(
            "stage-2/16_alliances_integration_contracts.md",
            "The alliance capability catalogue includes DELEGATE_DIPLOMACY.",
        )
        self.assert_failure(run_checks(self.root), "[C12]", "DELEGATE_DIPLOMACY")

    def test_35_req530_delegation_ban_removed_fails(self):
        self.modify_row_cell(
            "stage-2/03_requirements_traceability.md",
            "REQ-530",
            1,
            "no delegation",
            "delegation",
        )
        self.assert_failure(run_checks(self.root), "[C12]", "REQ-530")

    # ------------------------------------------------------------------
    # C13 - Discord and chat boundary
    # ------------------------------------------------------------------
    def test_36_mandatory_discord_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Discord is mandatory for alliance membership.",
        )
        self.assert_failure(run_checks(self.root), "[C13]", "Discord")

    def test_37_discord_bot_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The engine integrates a Discord bot for alliance notices.",
        )
        self.assert_failure(run_checks(self.root), "[C13]", "Discord")

    def test_38_static_invite_link_removed_fails(self):
        self.modify("stage-2/16_alliances.md", "discord.gg", "example.com", count=-1)
        self.modify(
            "stage-2/16_alliances.md", "discord.com/invite", "example.com/invite", count=-1
        )
        self.assert_failure(run_checks(self.root), "[C13]", "invite")

    # ------------------------------------------------------------------
    # C14 / C15 / C22 - treasury and formula neutrality
    # ------------------------------------------------------------------
    def test_39_pool_capacity_approved_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Alliance pool capacity is approved and enforced.",
        )
        self.assert_failure(run_checks(self.root), "[C14]", "capacity")

    def test_40_dual_signature_mandatory_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Dual signature authorization is mandatory for every withdrawal.",
        )
        self.assert_failure(run_checks(self.root), "[C14]", "threshold")

    def test_41_unapproved_threshold_presented_as_approved_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The 50,000 crown dual-signature threshold is approved and enforced.",
        )
        self.assert_failure(run_checks(self.root), "[C14]", "threshold")

    def test_42_formula_claims_approval_fails(self):
        self.section_modify(
            "stage-2/16_alliances_formula_register.md",
            "### F-AL-005",
            "**Decision Status** | **Candidate Proposal",
            "**Decision Status** | **Approved",
        )
        self.assert_failure(run_checks(self.root), "[C15]", "F-AL-005")

    def test_43_formula_required_number_fails(self):
        self.append(
            "stage-2/16_alliances_formula_register.md",
            "50,000 crowns is required content.",
        )
        self.assert_failure(run_checks(self.root), "[C22]", "required")

    def test_44_formula_optionality_statement_removed_fails(self):
        self.modify(
            "stage-2/16_alliances_formula_register.md",
            "No number in this register is required content",
            "Numbers are mandatory",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C14]", "required content")

    def test_45_formula_owner_reference_removed_fails(self):
        self.section_modify(
            "stage-2/16_alliances_formula_register.md",
            "### F-AL-001",
            "UD-046",
            "",
            end="### F-AL-002",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C15]", "F-AL-001")

    # ------------------------------------------------------------------
    # C16 - requirements register
    # ------------------------------------------------------------------
    def test_46_owner_reserved_requirement_approved_fails(self):
        self.set_row_cell(
            "stage-2/03_requirements_traceability.md", "REQ-556", 3, "**Approved**"
        )
        self.assert_failure(run_checks(self.root), "[C16]", "status counts")

    def test_47_missing_requirement_fails(self):
        self.delete_row("stage-2/03_requirements_traceability.md", "REQ-617")
        self.assert_failure(run_checks(self.root), "[C16]", "continuity")

    def test_48_req535_founder_office_regression_fails(self):
        self.modify_row_cell(
            "stage-2/03_requirements_traceability.md",
            "REQ-535",
            1,
            'founding creates no office and no "first Leader"',
            'founding creates a "first Leader" office',
        )
        self.assert_failure(run_checks(self.root), "[C16]", "REQ-535")

    def test_49_req591_deferral_removed_fails(self):
        # 2026-11-06 (Prompt 11C-C1): REQ-591 is now Provisional (10B supplied
        # the B-10 rule), so mutating it to "Provisional" was a no-op. The test
        # must move it to a status the C16 rule rejects.
        self.set_row_cell(
            "stage-2/03_requirements_traceability.md", "REQ-591", 3, "**Approved**"
        )
        self.assert_failure(run_checks(self.root), "[C16]", "REQ-591")

    def test_50_global_trade_requirement_weakened_fails(self):
        self.modify_row_cell(
            "stage-2/03_requirements_traceability.md",
            "REQ-513",
            1,
            "Global Trade is required",
            "Global Trade is optional",
        )
        self.assert_failure(run_checks(self.root), "[C16]", "REQ-513")

    def test_51_phantom_requirement_reference_fails(self):
        self.append(
            "stage-2/16_alliances_integration_contracts.md",
            "This contract is governed by REQ-999.",
        )
        self.assert_failure(run_checks(self.root), "[C06]", "REQ-999")

    def test_52_phantom_turn_rule_prefix_fails(self):
        self.append(
            "stage-2/16_alliances_integration_contracts.md",
            "The boundary rule TRN-020 applies.",
        )
        self.assert_failure(run_checks(self.root), "[C06]", "TRN-")

    # ------------------------------------------------------------------
    # C17 - decision registers
    # ------------------------------------------------------------------
    def test_53_d135_status_regression_fails(self):
        self.set_row_cell("DECISIONS.md", "D-135", 4, "Candidate Architecture")
        self.assert_failure(run_checks(self.root), "[C17]", "D-135")

    def test_54_missing_decision_fails(self):
        # 2026-11-06 (Prompt 11C-C1): the register now runs to D-162.
        self.delete_row("DECISIONS.md", "D-138")
        self.assert_failure(run_checks(self.root), "[C17]", "D-001..D-162")

    def test_55_dd_tally_regression_fails(self):
        self.modify(
            "stage-2/04_approved_and_provisional_decisions.md",
            "| Approved | 130 |",
            "| Approved | 129 |",
        )
        self.assert_failure(run_checks(self.root), "[C17]", "tally")

    def test_56_phantom_decision_reference_fails(self):
        self.modify("DECISIONS.md", "DMP-204", "D-204", count=-1)
        self.assert_failure(run_checks(self.root), "[C17]", "D-204")

    # ------------------------------------------------------------------
    # C18 - continuity and status
    # ------------------------------------------------------------------
    def test_57_continuity_status_removed_fails(self):
        self.modify("ROADMAP.md", STATUS_SENTENCE, "Status withheld.", count=-1)
        self.assert_failure(run_checks(self.root), "[C18]", "ROADMAP")

    def test_58_09c_authorized_fails(self):
        self.append("AI_HANDOFF.md", "Prompt 09C is authorized and next.")
        self.assert_failure(run_checks(self.root), "[C18]", "09C")

    def test_58b_09c_complete_without_spec_qualifier_fails(self):
        self.append("AI_HANDOFF.md", "Prompt 09C is complete and implemented.")
        self.assert_failure(run_checks(self.root), "[C18]", "specification-level qualifier")

    def test_59_next_prompt_changed_fails(self):
        # 2026-11-06 (Prompt 11C-C1): the live prompt advanced to 12, so the
        # fixture must mutate the current literal; a stale target silently
        # disables the test (the D-10 hazard).
        self.modify("AI_CONTEXT.md", "stage_2_next_prompt: 12", "stage_2_next_prompt: 09")
        self.assert_failure(run_checks(self.root), "[C18]", "stage_2_next_prompt")

    # ------------------------------------------------------------------
    # C19 - canonical 09C companion, specification boundary, no production code
    # ------------------------------------------------------------------
    def test_60_09c_companion_without_boundary_fails(self):
        self.write(
            "stage-2/16_alliances_workflows_acceptance.md",
            "# Premature 09C deliverable\n",
        )
        self.assert_failure(run_checks(self.root), "[C19]", "09C")

    def test_61_production_code_fails(self):
        source = self.root / "src"
        source.mkdir()
        (source / "alliance.ts").write_text("export const Alliance = {};\n", encoding="utf-8")
        self.assert_failure(run_checks(self.root), "[C19]", "src")

    # ------------------------------------------------------------------
    # C20 / C21 - cross-system anchors and history
    # ------------------------------------------------------------------
    def test_62_turn_rule_removed_fails(self):
        self.modify(
            "stage-2/07_core_gameplay_loop_symbolic_world_and_turn_system.md",
            "TR-024",
            "",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C20]", "TR-024")

    def test_63_global_trade_anchor_removed_fails(self):
        self.modify("stage-2/16_alliances.md", "D-122", "", count=-1)
        self.modify("stage-2/16_alliances_integration_contracts.md", "D-122", "", count=-1)
        self.assert_failure(run_checks(self.root), "[C20]", "D-122")

    def test_64_progress_entry_removed_fails(self):
        self.modify(
            "stage-2/06_stage_2_progress_log.md",
            "Prompt 09B-I correction",
            "Correction",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C21]", "09B-I")

    def test_65_global_trade_scope_weakened_fails(self):
        self.append("stage-2/16_alliances.md", "Global Trade is optional.")
        self.assert_failure(run_checks(self.root), "[C07]", "Global Trade")

    # ------------------------------------------------------------------
    # Fixtures A-F - authority-aware owner-reservation regressions
    # ------------------------------------------------------------------
    def test_66_fixture_A_timestamp_succession_rule_fails(self):
        """A: authoritative timestamp-based succession while UD-043 is Open."""
        self.append(
            "stage-2/16_alliances.md",
            "The earlier recorded timestamp decides which competing succession claim prevails.",
        )
        self.assert_failure(run_checks(self.root), "[C24]", "timestamp")

    def test_67_fixture_B_mandatory_appeal_path_fails(self):
        """B: mandatory appeal path while UD-044 is Open."""
        self.append(
            "stage-2/16_alliances.md",
            "Every expelled member must file an appeal with the alliance council, "
            "and the council shall issue a recorded decision.",
        )
        self.assert_failure(run_checks(self.root), "[C25]", "appeal")

    def test_68_fixture_C_contract_timestamp_succession_fails(self):
        """C: a contract, not the rulebook wording, assigns succession by timestamp."""
        self.section_modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-03 —",
            "No lifecycle event transfers alliance authority by itself",
            "No lifecycle event transfers alliance authority by itself. "
            "The earlier recorded timestamp automatically assigns succession authority "
            "to the first claimant.",
            end="### AX-04 —",
        )
        self.assert_failure(run_checks(self.root), "[C24]", "contracts")

    def test_69_fixture_D_relocated_mandatory_appeal_fails(self):
        """D: REQ-551 is neutralized but a contract introduces a mandatory appeal."""
        self.modify_row_cell(
            "stage-2/03_requirements_traceability.md",
            "REQ-551",
            1,
            "No appeal or dispute-resolution mechanism is required or approved while UD-044 is Open; "
            "if the owner later approves one, it must have a declared path and a recorded decision",
            "Dispute and disciplinary records are retained.",
        )
        self.modify(
            "stage-2/16_alliances_integration_contracts.md",
            "### AX-22 —",
            "Every expelled member must appeal to the alliance council, and the council "
            "shall issue a recorded decision.\n\n### AX-22 —",
        )
        self.assert_failure(run_checks(self.root), "[C25]", "contracts")

    def test_70_fixture_E_ud040_founding_policy_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Alliance founding costs 5,000 crowns, which is approved and enforced.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-040")

    def test_71_fixture_E_ud041_default_office_model_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The default office model is approved and ships with a mandatory Leader.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-041")

    def test_72_fixture_E_ud042_native_ballots_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Native ballots are approved and mandatory for every amendment.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-042")

    def test_73_fixture_E_ud045_permission_catalogue_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The permission catalogue is approved and fixed for launch.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-045")

    def test_74_fixture_E_ud046_treasury_ownership_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Alliance treasury ownership is approved and enforced.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-046")

    def test_75_fixture_E_ud047_collective_diplomacy_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Collective diplomatic positions are binding on every member nation.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-047")

    def test_76_fixture_E_ud048_invite_visibility_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "The Discord invite link is public by default for all alliances.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-048")

    def test_77_fixture_E_ud049_release_scope_fails(self):
        self.append(
            "stage-2/16_alliances.md",
            "Announcements and formal votes are included in the first release.",
        )
        self.assert_failure(run_checks(self.root), "[C26]", "UD-049")

    def test_78_fixture_F_clean_canonical_authority_passes(self):
        """F: clean corpus with every owner reservation and approved boundary intact."""
        failures = run_checks(self.root)
        rendered = " | ".join(failures[:8]).encode("ascii", "replace").decode("ascii")
        self.assertEqual(failures, [], f"Fixture should pass cleanly, got: {rendered}")
        ud_text = self.read("stage-2/05_unresolved_design_decisions.md")
        for number in range(40, 50):
            row = VAL.get_row(ud_text, f"UD-{number:03d}")
            self.assertIsNotNone(row, f"UD-{number:03d} is missing")
            self.assertEqual(VAL.status_word(row[-1]), "Open")
        b09_lower = self.read("stage-2/16_alliances.md").lower()
        self.assertIn("sole diplomatic authority", b09_lower)
        self.assertIn("open-ended", b09_lower)
        self.assertIn("no mandatory", b09_lower)
        self.assertIn("no alliance-level treaty object", self.read("DECISIONS.md").lower())

    # ------------------------------------------------------------------
    # Fixtures G-H - compound disclaimer plus unauthorized mandate
    # ------------------------------------------------------------------
    def test_79_fixture_G_compound_succession_disclaimer_mandate_fails(self):
        """G: a negation in one clause must not hide a succession mandate in another."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-057`",
            "Any rule for resolving competing claims remains owner-reserved under `UD-043` "
            "and is not in force.",
            "Any rule for resolving competing claims remains owner-reserved under `UD-043` "
            "and is not in force. Timestamp ordering is not sufficient by itself, but the "
            "earliest claimant must become the successor.",
            end="**`ALL-058`",
        )
        self.assert_failure(
            run_checks(self.root), "[C24]", "UD-043"
        )
        self.assert_failure(
            run_checks(self.root), "[C24]", "ALL-057"
        )
        self.assert_failure(
            run_checks(self.root), "[C24]", "B-09"
        )
        self.assert_failure(
            run_checks(self.root), "[C24]", "earliest claimant"
        )

    def test_80_fixture_H_compound_appeal_disclaimer_entitlement_fails(self):
        """H: a disclaimer must not hide a mandatory appeal entitlement."""
        self.modify_row_cell(
            "stage-2/03_requirements_traceability.md",
            "REQ-551",
            1,
            "No appeal or dispute-resolution mechanism is required or approved while UD-044 is Open",
            "No appeal or dispute-resolution mechanism is required or approved while UD-044 is Open. "
            "Appeals are generally not required, but members must have the right to appeal every expulsion.",
        )
        self.assert_failure(
            run_checks(self.root), "[C25]", "UD-044"
        )
        self.assert_failure(
            run_checks(self.root), "[C25]", "REQ-551"
        )
        self.assert_failure(
            run_checks(self.root), "[C25]", "right to appeal"
        )

    # ------------------------------------------------------------------
    # Positive authority wording - must remain accepted
    # ------------------------------------------------------------------
    def test_81_positive_direct_succession_prohibition_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "Timestamp ordering must not determine succession.",
        )
        self.assert_clean()

    def test_82_positive_audit_only_timestamp_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "Timestamp ordering is retained only as audit evidence and cannot determine "
            "who becomes the successor.",
        )
        self.assert_clean()

    def test_83_positive_conditional_succession_proposal_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "A succession workflow may be proposed for future owner review, but no "
            "automatic succession rule is currently authorized.",
        )
        self.assert_clean()

    def test_84_positive_no_approved_appeal_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "No appeal mechanism is currently approved under UD-044.",
        )
        self.assert_clean()

    def test_85_positive_conditional_appeal_proposal_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "An appeal procedure could be proposed for future owner review, but it "
            "cannot be enforced before owner approval.",
        )
        self.assert_clean()

    def test_86_positive_neutral_recordkeeping_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "Dispute records are retained for audit and evidence only and create no "
            "appeal right.",
        )
        self.assert_clean()

    def test_87_positive_approved_audit_reference_passes(self):
        self.append(
            "stage-2/16_alliances.md",
            "The audit record of a succession event is retained under the approved "
            "audit spine and decides no succession question.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # Fixtures I-M - negative-polarity appeal policy while UD-044 is Open
    # ------------------------------------------------------------------
    def test_88_fixture_I_cannot_be_expelled_without_appeal_fails(self):
        """I: a negative construction must not hide an appeal entitlement."""
        self.inject_all079(
            "Alliance members cannot be expelled without a right to appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "without a right to appeal")
        self.assert_failure(failures, "[C25]", "condition of expulsion")

    def test_89_fixture_J_must_not_be_deprived_of_appeal_fails(self):
        """J: barring deprivation of an appeal asserts an appeal entitlement."""
        self.inject_all079(
            "Members must not be deprived of a right to appeal an expulsion."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "deprived")
        self.assert_failure(failures, "[C25]", "deprivation")

    def test_90_fixture_K_no_member_expelled_unless_appeal_fails(self):
        """K: an appeal made a precondition of expulsion is an unauthorized policy."""
        self.inject_all079(
            "No member may be expelled unless an appeal opportunity is provided."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "unless an appeal opportunity")
        self.assert_failure(failures, "[C25]", "condition of expulsion")

    def test_91_fixture_L_no_expelled_member_may_appeal_fails(self):
        """L: prohibiting appeals is an unauthorized policy, not neutral wording."""
        self.inject_all079(
            "No expelled member may appeal the expulsion."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "No expelled member may appeal")
        self.assert_failure(failures, "[C25]", "denies an appeal right")

    def test_92_fixture_M_must_be_allowed_to_appeal_fails(self):
        """M: a positive duty to allow an appeal is an unauthorized entitlement."""
        self.inject_all079(
            "Every expelled member must be allowed to challenge the expulsion "
            "through an appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "must be allowed to challenge")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    # ------------------------------------------------------------------
    # 09B-H positive controls - legitimate neutral or prohibitive wording
    # ------------------------------------------------------------------
    def test_93_positive_must_not_create_or_deny_appeal_rights_passes(self):
        self.inject_all079(
            "The platform must not create or deny appeal rights until UD-044 "
            "receives an owner decision."
        )
        self.assert_clean()

    def test_94_positive_no_approved_or_required_appeal_mechanism_passes(self):
        self.inject_all079(
            "No appeal mechanism is currently approved or required."
        )
        self.assert_clean()

    def test_95_positive_expulsion_evidence_without_appeal_decision_passes(self):
        self.inject_all079(
            "The system stores expulsion evidence without deciding appeal rights."
        )
        self.assert_clean()

    def test_96_positive_future_appeal_proposal_not_enforced_passes(self):
        self.inject_all079(
            "A future appeal mechanism may be proposed for owner review, but is "
            "not currently enforced."
        )
        self.assert_clean()

    def test_97_positive_recordkeeping_not_an_entitlement_passes(self):
        self.inject_all079(
            "Technical recordkeeping must not be interpreted as an appeal "
            "entitlement."
        )
        self.assert_clean()

    def test_98_positive_expulsion_record_does_not_establish_appeal_passes(self):
        self.inject_all079(
            "The existence of an expulsion record does not establish an appeal "
            "mechanism."
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C24 negative-polarity succession fixtures and positive controls
    # ------------------------------------------------------------------
    def test_99_c24_claimant_cannot_be_bypassed_fails(self):
        """C24: barring a claimant from being bypassed imposes a succession rule."""
        self.inject_all057(
            "The earliest claimant cannot be bypassed by a later technical "
            "workflow in succession."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C24]", "UD-043")
        self.assert_failure(failures, "[C24]", "ALL-057")
        self.assert_failure(failures, "[C24]", "bypassed")
        self.assert_failure(failures, "[C24]", "displacement")

    def test_100_c24_successor_cannot_be_denied_succession_fails(self):
        """C24: barring denial of succession asserts a succession entitlement."""
        self.inject_all057(
            "A successor cannot be denied succession once the earliest claimant "
            "is recorded."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C24]", "UD-043")
        self.assert_failure(failures, "[C24]", "ALL-057")
        self.assert_failure(failures, "[C24]", "cannot be denied succession")

    def test_101_c24_no_claimant_may_be_displaced_fails(self):
        """C24: protecting a claimant from displacement is a succession policy."""
        self.inject_all057(
            "The earliest claimant cannot be displaced from the succession by a "
            "later technical workflow."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C24]", "UD-043")
        self.assert_failure(failures, "[C24]", "ALL-057")
        self.assert_failure(failures, "[C24]", "cannot be displaced")
        self.assert_failure(failures, "[C24]", "displacement")

    def test_102_c24_positive_neutral_recording_passes(self):
        """Neutral claim recording creates no succession entitlement under C24."""
        self.inject_all057(
            "Competing claims are retained as neutral audit records and create "
            "no succession entitlement."
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # Fixtures N-P - denial and exception/unless branches decide appeal
    # policy even when the main clause reads as neutral
    # ------------------------------------------------------------------
    def test_103_fixture_N_must_not_deny_appeal_rights_fails(self):
        """N: a prohibition on denial asserts an appeal entitlement."""
        self.inject_all079(
            "The platform must not deny appeal rights to any expelled member."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "must not deny appeal rights")
        self.assert_failure(failures, "[C25]", "denial")

    def test_104_fixture_O_except_branch_entitlement_fails(self):
        """O: an except-that branch granting an appeal is a policy decision."""
        self.inject_all079(
            "The platform must not create or deny appeal rights except that "
            "expelled members shall retain a right to appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "except that")
        self.assert_failure(failures, "[C25]", "entitlement")

    def test_105_fixture_P_unless_branch_entitlement_fails(self):
        """P: an unless branch granting an appeal is a policy decision."""
        self.inject_all079(
            "The platform must not create or deny appeal rights unless every "
            "expelled member has a right to appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "unless every expelled member")
        self.assert_failure(failures, "[C25]", "entitlement")

    def test_106_positive_must_not_create_appeal_rights_passes(self):
        """A bare holding statement creates no appeal entitlement."""
        self.inject_all079(
            "The platform must not create appeal rights while UD-044 is Open."
        )
        self.assert_clean()

    def test_107_positive_neutral_create_or_deny_with_reservation_passes(self):
        """A coordinated create-or-deny holding statement stays neutral."""
        self.inject_all079(
            "The platform must not create or deny appeal rights pending an "
            "owner decision under UD-044."
        )
        self.assert_clean()

    def test_108_positive_recordkeeping_confers_no_appeal_right_passes(self):
        """Expulsion recordkeeping is technical evidence, not appeal policy."""
        self.inject_all079(
            "Expulsion records are retained for audit evidence only and confer "
            "no appeal right."
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C27 - Owner-consented taxation (Prompt 09B-I)
    # ------------------------------------------------------------------
    def test_109_c27_default_tax_rate_fails(self):
        """An invented default rate is not player-defined."""
        self.append(
            "stage-2/16_alliances.md",
            "The default tax rate is 12 percent for every alliance.",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "default tax rate")

    def test_110_c27_per_policy_owner_approval_fails(self):
        """Requiring every nation owner to approve each policy version contradicts ALL-179."""
        self.append(
            "stage-2/16_alliances.md",
            "The alliance tax requires every member nation's owner to approve each "
            "policy version before it applies.",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "per-policy owner approval")

    def test_111_c27_requirement_status_regression_fails(self):
        """REQ-618 is an owner-authorized capability and must remain Approved."""
        self.set_row_cell(
            "stage-2/03_requirements_traceability.md", "REQ-618", 3, "Provisional"
        )
        self.assert_failure(run_checks(self.root), "[C27]", "REQ-618")

    def test_112_c27_positive_player_defined_policy_passes(self):
        """An automatic per-turn player-defined policy with an explicit 0% fallback is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "An alliance collects its automatic per-turn production tax from each "
            "member's eligible current-turn Crowns and resource output under "
            "player-created brackets; an unassigned member is taxed at the explicit "
            "0% fallback until an authorized actor assigns a valid bracket.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C28 - Voluntary donations (Prompt 09B-I)
    # ------------------------------------------------------------------
    def test_113_c28_mandatory_or_automatic_donation_fails(self):
        """A donation cannot be mandatory, automatic or relabelled from a levy."""
        self.append(
            "stage-2/16_alliances.md",
            "Donations are mandatory for every member. The alliance automatically "
            "withdraws the donation each turn. A compulsory levy is recorded as a "
            "donation.",
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C28]", "mandatory")
        self.assert_failure(failures, "[C28]", "automatically")
        self.assert_failure(failures, "[C28]", "donation")

    def test_114_c28_donation_as_withdrawal_authority_fails(self):
        """A donation receipt confers no treasury withdrawal authority."""
        self.append(
            "stage-2/16_alliances.md",
            "A donation authorizes the alliance to withdraw from the treasury.",
        )
        self.assert_failure(run_checks(self.root), "[C28]", "withdraw")

    def test_115_c28_requirement_status_regression_fails(self):
        """REQ-626 is an owner-authorized capability and must remain Approved."""
        self.set_row_cell(
            "stage-2/03_requirements_traceability.md", "REQ-626", 3, "Provisional"
        )
        self.assert_failure(run_checks(self.root), "[C28]", "REQ-626")

    def test_116_c28_positive_voluntary_donation_passes(self):
        """A voluntary, authenticated, receipted donation without withdrawal power is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "A donation is voluntary, requires authenticated confirmation, produces "
            "a receipt and creates no withdrawal authority.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C29 - ALL-093 withdrawal and independent safeguards (Prompt 09B-I)
    # ------------------------------------------------------------------
    def test_117_c29_confiscation_clause_reintroduced_fails(self):
        """The withdrawn ALL-093 confiscation protection cannot return."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-093`",
            "Withdrawn by `D-140`",
            "Protection Against Arbitrary Confiscation. Withdrawn by `D-140`",
            end="**`ALL-094`",
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C29]", "confiscation")
        self.assert_failure(failures, "[C29]", "withdrawn confiscation clause")

    def test_118_c29_tombstone_meaning_removed_fails(self):
        """The tombstone must keep stating that it grants no right or power."""
        self.modify(
            "stage-2/16_alliances.md",
            "It grants no right, protection, authority or confiscation power.",
            "It governs exit assets.",
        )
        self.assert_failure(run_checks(self.root), "[C29]", "grants no right")

    def test_119_c29_security_anchor_removed_fails(self):
        """Transaction authentication is an independent safeguard, not part of ALL-093."""
        self.modify(
            "stage-2/16_alliances.md",
            "authentication",
            "identity proof",
            count=-1,
        )
        self.modify(
            "stage-2/16_alliances.md",
            "Authentication",
            "Identity proof",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C29]", "authentication")

    def test_120_c29_positive_security_and_audit_wording_passes(self):
        """Removing the confiscation clause must not remove security or audit rules."""
        self.append(
            "stage-2/16_alliances.md",
            "Authentication, authorization, audit logging and transaction integrity "
            "remain in force for every alliance action.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C30 - Separate Alliance treaty object, NAP consent and other pacts
    # ------------------------------------------------------------------
    def test_121_c30_treaty_reuses_b08_object_fails(self):
        """The Alliance treaty object must remain separate from B-08."""
        self.append(
            "stage-2/16_alliances.md",
            "The alliance treaty reuses the B-08 object.",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "reuses")

    def test_122_c30_leader_consents_for_nation_fails(self):
        """No alliance actor can consent for a sovereign nation."""
        self.append(
            "stage-2/16_alliances.md",
            "An alliance leader consents for a nation to the treaty.",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "consent")

    def test_123_c30_nap_exception_fails(self):
        """An active NAP has no discretionary exception or waiver."""
        self.append(
            "stage-2/16_alliances.md",
            "A NAP exception is available while the treaty is active.",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "exception")

    def test_124_c30_other_pact_effect_invented_fails(self):
        """Mutual defence creates no automatic war entry."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-203`",
            "no automatic war entry",
            "automatic war entry",
            end="**`ALL-204`",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "no automatic war entry")

    def test_125_c30_requirement_status_regression_fails(self):
        """REQ-633 is an owner-authorized treaty capability and must remain Approved."""
        self.set_row_cell(
            "stage-2/03_requirements_traceability.md", "REQ-633", 3, "Provisional"
        )
        self.assert_failure(run_checks(self.root), "[C30]", "REQ-633")

    def test_126_c30_positive_nap_and_other_pact_wording_passes(self):
        """A consented NAP and a declared-effect pact remain valid."""
        self.append(
            "stage-2/16_alliances.md",
            "While an active AT-T01 NAP applies, a cross-Alliance attack must be "
            "rejected before execution by the server-side validator. An AT-T03 "
            "economic pact creates only the effects its adopted text declares.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C31 - Mandatory same-Alliance attack ban (Prompt 09B-I)
    # ------------------------------------------------------------------
    def test_127_c31_optional_same_alliance_ban_fails(self):
        """The same-Alliance ban cannot be optional or opt-out."""
        self.append(
            "stage-2/16_alliances.md",
            "The same-Alliance ban is optional for member nations.",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "optional")

    def test_128_c31_ui_only_enforcement_fails(self):
        """Hiding a button is not server-side enforcement."""
        self.append(
            "stage-2/16_alliances.md",
            "UI-only enforcement prevents same-Alliance attacks.",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "UI-only")

    def test_129_c31_execution_time_check_removed_fails(self):
        """Validation must run again at execution, not only at submission."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-211`",
            "and again at execution or settlement",
            "only at submission",
            end="**`ALL-212`",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "again at execution")

    def test_130_c31_requirement_status_regression_fails(self):
        """REQ-645 is an owner-authorized attack ban and must remain Approved."""
        self.set_row_cell(
            "stage-2/03_requirements_traceability.md", "REQ-645", 3, "Provisional"
        )
        self.assert_failure(run_checks(self.root), "[C31]", "REQ-645")

    def test_131_c31_positive_same_alliance_ban_passes(self):
        """Restating the server-side ban and audit-neutral block language is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "Nations that share an active alliance must not attack each other, and "
            "every attack path calls the same server-side validator at submission "
            "and execution. A blocked attack consumes no resources and creates no "
            "retaliation.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C27-C31 structural coverage: each policy shape and lifecycle term
    # must remain present, not only the representative guard sentences
    # ------------------------------------------------------------------
    def test_132_c27_zero_fallback_term_removed_fails(self):
        """The explicit 0% fallback is a required tax assignment term."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-182`",
            "Assignment and Explicit 0% Fallback",
            "Assignment and Fallback",
            end="**`ALL-183`",
        )
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-182`",
            "The 0% fallback is explicit, visible to the member and recorded",
            "The fallback is visible to the member",
            end="**`ALL-183`",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "0% fallback")

    def test_133_c28_donor_asset_selection_removed_fails(self):
        """The donor, not the alliance, selects the donated asset and amount."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-189`",
            "The donor selects the asset and the amount.",
            "The alliance selects the asset and the amount.",
            end="**`ALL-190`",
        )
        self.assert_failure(
            run_checks(self.root), "[C28]", "the donor selects the asset and the amount"
        )

    def test_134_c28_confirmation_identification_removed_fails(self):
        """Confirmation must identify the donor and receiving alliance."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-190`",
            "the confirmation shows the donor nation",
            "the confirmation shows the totals",
            end="**`ALL-191`",
        )
        self.assert_failure(
            run_checks(self.root), "[C28]", "confirmation shows the donor nation"
        )

    def test_135_c28_insufficient_funds_failure_removed_fails(self):
        """The insufficient-value failure rule is part of donation handling."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-191`",
            "lacks unreserved value",
            "cannot complete the transfer",
            end="**`ALL-192`",
        )
        self.assert_failure(run_checks(self.root), "[C28]", "lacks unreserved value")

    def test_136_c30_nap_player_explanation_removed_fails(self):
        """A blocked NAP attack must give a clear player reason."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-206`",
            "clear reason",
            "response",
            end="**`ALL-207`",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "clear reason")

    def test_137_c30_treaty_approval_record_removed_fails(self):
        """Both alliances' approvals are part of the treaty record."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-200`",
            "each alliance's approval",
            "the proposing alliance's approval",
            end="**`ALL-201`",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "each alliance's approval")

    def test_138_c31_shared_membership_trigger_removed_fails(self):
        """The ban triggers on sharing at least one active alliance."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-209`",
            "share at least one active alliance",
            "are in the same alliance",
            end="**`ALL-210`",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "share at least one active alliance")

    def test_139_c31_canonical_server_side_validator_removed_fails(self):
        """Every attack path must call one canonical server-side function."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-210`",
            "one canonical server-side attack-validation function",
            "a client-side attack-validation function",
            end="**`ALL-211`",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "one canonical server-side")

    def test_140_c31_membership_change_coverage_removed_fails(self):
        """Join, leave and transfer must remain named membership changes."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-212`",
            "Join, leave, transfer, expulsion",
            "Membership changes and expulsion",
            end="**`ALL-213`",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "join")

    def test_141_c30_nap_explicit_consent_term_removed_fails(self):
        """A NAP binds only after the nation owner explicitly consents."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-199`",
            "must explicitly consent to the exact version",
            "may consent to the exact version",
            end="**`ALL-200`",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "explicitly consent")

    # ------------------------------------------------------------------
    # C25-J - plain modal grants, procedural access and clause-scoped
    # evaluation. These are permanent fixtures for the five statements the
    # independent audit found escaping the earlier C25.
    # ------------------------------------------------------------------
    def test_142_c25_members_may_appeal_fails(self):
        """Audit escape 1: a plain permissive modal is a grant, not neutral."""
        self.inject_all079("Members may appeal an expulsion.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_143_c25_expelled_member_can_appeal_fails(self):
        """Audit escape 2: 'can appeal' asserts the same entitlement as 'may'."""
        self.inject_all079("An expelled member can appeal the expulsion decision.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_144_c25_every_expelled_member_may_appeal_fails(self):
        """Audit escape 3: a universal beneficiary still decides appeal policy."""
        self.inject_all079("Every expelled member may appeal.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_145_c25_appeal_may_be_lodged_fails(self):
        """Audit escape 4: procedural access decides appeal rights too."""
        self.inject_all079("An appeal may be lodged within the review window.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "provides an appeal procedure")

    def test_146_c25_has_access_to_appeal_process_fails(self):
        """Audit escape 5: access to a procedure is an entitlement."""
        self.inject_all079("The expelled member has access to an appeal process.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants access to an appeal procedure")

    def test_147_c25_denied_access_to_appeal_fails(self):
        """A fixed denial of procedural access is an unauthorized policy."""
        self.inject_all079(
            "An expelled member is denied access to an appeal process."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "denies an appeal right")

    def test_148_c25_conditional_grant_fails(self):
        """A conditional expression must not exempt a grant in the same clause."""
        self.inject_all079(
            "If a member is expelled, the member may appeal the expulsion."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_149_c25_negation_does_not_hide_grant_in_same_clause_fails(self):
        """A negation earlier in the clause must not skip the remaining grant."""
        self.inject_all079(
            "Notwithstanding that no appeal mechanism is approved, every "
            "expelled member may appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_150_c25_compound_disclaimer_then_grant_fails(self):
        """A neutral disclaimer in one branch cannot immunise another branch."""
        self.inject_all079(
            "No appeal mechanism is approved, but members may appeal an expulsion."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_151_c25_exception_branch_grant_fails(self):
        """An exception branch that grants an appeal is a policy assertion."""
        self.inject_all079(
            "The platform must not create or deny appeal rights except that "
            "expelled members may appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_152_c25_conditional_procedural_duty_fails(self):
        """A conditional duty to provide an appeal is still an appeal policy."""
        self.inject_all079(
            "If an expelled member requests review, the alliance must provide "
            "an appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "mandates an alliance appeal")

    def test_153_c25_subordinate_clause_grant_fails(self):
        """A grant in a subordinate clause must be evaluated on its own."""
        self.inject_all079(
            "Expulsion records are retained for audit evidence, and every "
            "expelled member may appeal the decision."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_154_c25_positive_unresolved_proposal_passes(self):
        """Approved wording that keeps appeal policy unresolved stays valid."""
        self.inject_all079(
            "No appeal mechanism is required or approved while UD-044 is Open; "
            "a future appeal procedure remains a candidate proposal for owner review."
        )
        self.assert_clean()

    def test_155_c25_positive_recordkeeping_passes(self):
        """Neutral audit recordkeeping creates no appeal entitlement."""
        self.inject_all079(
            "Expulsion records are retained as neutral audit evidence and confer "
            "no appeal right."
        )
        self.assert_clean()

    def test_156_c25_positive_no_rejoin_rule_passes(self):
        """Stating that no rejoin rule is in force is a neutral holding."""
        self.inject_all079(
            "No rejoin cooldown, blacklist or rejoin rule is in force while "
            "UD-044 is Open."
        )
        self.assert_clean()

    def test_157_c25_positive_treaty_consent_after_rejoin_passes(self):
        """Treaty coverage consent after rejoin is not a rejoin restriction."""
        self.inject_all079(
            "A rejoining nation requires fresh consent to each Alliance treaty."
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C27 - 09B-J per-turn production-tax semantics
    # ------------------------------------------------------------------
    def test_158_c27_existing_stockpile_taxed_fails(self):
        """The base is current-turn production, never an opening balance."""
        self.append(
            "stage-2/16_alliances.md",
            "The alliance tax applies to each member's existing Crown balance and "
            "stored resource stockpile.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C27]",
            "taxes existing value rather than current-turn production",
        )

    def test_159_c27_rates_restricted_to_ten_percent_fails(self):
        """Rates are any integer basis point, not fixed 10% steps."""
        self.append(
            "stage-2/16_alliances.md",
            "Tax rates are restricted to 10% increments for every alliance bracket.",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "restricts rates to fixed 10% steps")

    def test_160_c27_capacity_rejection_fails(self):
        """No receipt may be rejected because no capacity model is approved."""
        self.append(
            "stage-2/16_alliances.md",
            "A tax receipt is rejected at the capacity limit of the Alliance "
            "Receiving Ledger.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C27]",
            "rejects a receipt on an invented capacity limit",
        )

    def test_161_c27_fixed_office_tax_authority_fails(self):
        """A fixed office cannot hold automatic tax authority."""
        self.append(
            "stage-2/16_alliances.md",
            "The Treasurer automatically sets the tax rate for every member.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C27]",
            "hard-codes tax authority to a fixed office",
        )

    def test_162_c27_unauthorized_actor_changes_policy_fails(self):
        """Tax changes require the active role permission, not mere office."""
        self.append(
            "stage-2/16_alliances.md",
            "Any officer may change a tax bracket regardless of permission.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C27]",
            "lets an unauthorized actor change tax policy",
        )

    def test_163_c27_positive_non_ten_rates_and_brackets_passes(self):
        """37/55/73/100 rates, separate assets and an explicit 0% fallback are valid."""
        self.append(
            "stage-2/16_alliances.md",
            "One frozen bracket may set a 37% Crowns rate and a 55% iron rate, "
            "while another member's bracket sets 73% for oil and 100% for food; "
            "an unassigned member stays at the explicit 0% fallback.",
        )
        self.assert_clean()

    def test_164_c27_fixed_office_prohibition_removed_fails(self):
        """ALL-183 must keep the explicit no-fixed-office constraint."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-183`",
            "No fixed office",
            "No permanent office",
            end="**`ALL-184`",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "no fixed office")

    def test_165_c27_post_tax_double_deduction_guard_removed_fails(self):
        """ALL-180 must keep the ban on applying tax to the post-tax balance."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-180`",
            "The tax is never applied to the post-tax balance or to inventory a second time.",
            "The tax is applied once per settlement.",
            end="**`ALL-181`",
        )
        self.assert_failure(
            run_checks(self.root), "[C27]", "never applied to the post-tax balance"
        )

    def test_166_c27_ledger_ownership_boundary_removed_fails(self):
        """ALL-187 must keep the no-ownership-interest boundary of the ARL."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-187`",
            "It creates no ownership interest",
            "It creates no title claim",
            end="**`ALL-188`",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "no ownership interest")

    def test_167_c27_positive_role_permission_and_freeze_passes(self):
        """Role-gated assignment with a freeze-boundary effect is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "Only an authenticated account holding the active tax-assignment "
            "permission may assign a bracket; every change is versioned and takes "
            "effect at the next freeze boundary.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C30 - 09B-J NAP membership, custom text and whole-treaty termination
    # ------------------------------------------------------------------
    def test_168_c30_admission_refused_for_declined_nap_fails(self):
        """Declining NAP consent cannot cost admission."""
        self.append(
            "stage-2/16_alliances.md",
            "A nation is barred from admission when its owner declines NAP participation.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C30]",
            "refuses admission for withheld treaty consent",
        )

    def test_169_c30_automatic_joiner_coverage_fails(self):
        """A new member is never added to a NAP's covered set automatically."""
        self.append(
            "stage-2/16_alliances.md",
            "A joining nation is automatically covered by the alliance NAP.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C30]",
            "extends NAP coverage automatically to a joiner",
        )

    def test_170_c30_custom_prose_executable_fails(self):
        """Player prose cannot become an executable attack restriction."""
        self.append(
            "stage-2/16_alliances.md",
            "Custom treaty prose is parsed into an executable attack ban.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C30]",
            "makes custom treaty prose executable",
        )

    def test_171_c30_whole_treaty_termination_term_removed_fails(self):
        """ALL-205 must keep the dissolution-ends-the-whole-treaty rule."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-205`",
            "terminates the bilateral treaty **as a whole** at the defined dissolution boundary",
            "terminates the bilateral treaty at the defined dissolution boundary",
            end="**`ALL-206`",
        )
        self.assert_failure(run_checks(self.root), "[C30]", "as a whole")

    def test_172_c30_nap_bidirectional_clause_removed_fails(self):
        """The NAP must prohibit attacks in both directions."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-206`",
            ", and no covered member of B may attack any covered member of A",
            "",
            end="**`ALL-207`",
        )
        self.assert_failure(
            run_checks(self.root), "[C30]", "no covered member of b may attack"
        )

    def test_173_c30_positive_non_covered_membership_passes(self):
        """Declining consent leaves a member non-covered, not punished."""
        self.append(
            "stage-2/16_alliances.md",
            "A member that declines NAP consent remains a non-covered member, and "
            "the active NAP neither protects nor restricts that nation.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C31 - 09B-J mandatory audit and independent cumulative checks
    # ------------------------------------------------------------------
    def test_174_c31_mandatory_audit_term_removed_fails(self):
        """ALL-214 must keep the unconditional blocked-attack audit."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-214`",
            "writes a mandatory audit event",
            "may write an audit event",
            end="**`ALL-215`",
        )
        self.assert_failure(run_checks(self.root), "[C31]", "mandatory audit event")

    def test_175_c31_nap_bypass_after_leaving_anchor_removed_fails(self):
        """Leaving a shared alliance cannot switch off an active NAP check."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-213`",
            "leaving a shared alliance does not bypass a still-active NAP",
            "leaving a shared alliance ends every treaty check",
            end="**`ALL-214`",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C31]",
            "leaving a shared alliance does not bypass",
        )

    def test_176_c31_positive_multiple_shared_memberships_passes(self):
        """Any shared active membership triggers the server-side ban."""
        self.append(
            "stage-2/16_alliances.md",
            "If two nations share any one of several active alliances, the "
            "server-side validator blocks the attack; a nation in multiple "
            "alliances is covered for every shared membership.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C25 - 09B-K appeal-entitlement semantics
    # ------------------------------------------------------------------
    def test_177_c25_receives_opportunity_to_appeal_fails(self):
        """A received opportunity decides the appeal right as surely as 'may'."""
        self.inject_all079(
            "Every expelled member receives an opportunity to appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_178_c25_right_to_appeal_established_fails(self):
        """A right declared established is a positive entitlement."""
        self.inject_all079("The member's right to appeal is established.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_179_c25_afforded_an_appeal_fails(self):
        """'Are afforded' is a passive grant, not a neutral description."""
        self.inject_all079("Expelled members are afforded an appeal.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_180_c25_appeals_available_to_expelled_members_fails(self):
        """Availability to a beneficiary is an entitlement statement."""
        self.inject_all079("Appeals are available to expelled members.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_181_c25_expelled_member_may_file_appeal_fails(self):
        """'May file' is a permissive grant of an appeal procedure."""
        self.inject_all079("An expelled member may file an appeal.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_182_c25_every_member_permitted_to_appeal_fails(self):
        """A universal permission is still an appeal-policy decision."""
        self.inject_all079("Every member is permitted to appeal.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_183_c25_platform_guarantees_appeal_opportunity_fails(self):
        """A guarantee asserts that the opportunity exists."""
        self.inject_all079("The platform guarantees an appeal opportunity.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_184_c25_appeal_right_exists_fails(self):
        """Existence of an appeal right is a positive entitlement."""
        self.inject_all079("An appeal right exists for expelled members.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_185_c25_access_to_appeal_procedure_fails(self):
        """Access to a procedure is an entitlement even without 'right'."""
        self.inject_all079(
            "Expelled members have access to an appeal procedure."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants access to an appeal procedure")

    def test_186_c25_no_appeal_available_fails(self):
        """A fixed denial is an appeal-policy decision, not a neutral holding."""
        self.inject_all079("No appeal is available to an expelled member.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "denies an appeal right")

    def test_187_c25_must_not_grant_any_appeal_right_fails(self):
        """A prohibition on granting an appeal decides the negative policy."""
        self.inject_all079("The platform must not grant any appeal right.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "denies an appeal right")

    def test_188_c25_disclaimer_then_entitlement_fails(self):
        """A disclaimer cannot immunise an entitlement in the next branch."""
        self.inject_all079(
            "No appeal mechanism is approved, but every expelled member "
            "receives an opportunity to appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_189_c25_entitlement_then_disclaimer_fails(self):
        """A later disclaimer cannot erase an earlier active entitlement."""
        self.inject_all079(
            "Every expelled member receives an opportunity to appeal; "
            "however, no appeal mechanism is approved."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_190_c25_subordinate_entitlement_fails(self):
        """An entitlement in a subordinate clause is evaluated on its own."""
        self.inject_all079(
            "Expulsion records are retained for audit evidence, and expelled "
            "members are afforded an appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_191_c25_compound_entitlement_fails(self):
        """A coordinated compound cannot hide the grant in its second limb."""
        self.inject_all079(
            "The alliance must record the expulsion and afford every expelled "
            "member an appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_192_c25_historical_mention_passes(self):
        """A historical note about a rejected draft is not a policy decision."""
        self.inject_all079(
            "Historical note: an earlier draft gave every expelled member an "
            "appeal, but the owner rejected that proposal."
        )
        self.assert_clean()

    def test_193_c25_rejected_proposal_passes(self):
        """A rejected proposal describes what was not adopted."""
        self.inject_all079(
            "A rejected proposal would have given every expelled member an "
            "appeal; the owner never adopted it."
        )
        self.assert_clean()

    def test_194_c25_illustrative_fixture_passes(self):
        """An illustrative fixture is descriptive, not an operative rule."""
        self.inject_all079(
            "The illustrative fixture reads: expelled members are afforded an "
            "appeal, but it is not part of this design."
        )
        self.assert_clean()

    def test_195_c25_negated_historical_framing_fails(self):
        """Denying that a statement is historical leaves the present grant."""
        self.inject_all079(
            "This is not a historical example: every expelled member receives "
            "an opportunity to appeal."
        )
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "grants an appeal entitlement")

    def test_196_c25_only_expelled_members_may_appeal_fails(self):
        """A restriction of who may appeal decides the appeal policy."""
        self.inject_all079("Only expelled members may appeal.")
        failures = run_checks(self.root)
        self.assert_failure(failures, "[C25]", "UD-044")
        self.assert_failure(failures, "[C25]", "ALL-079")
        self.assert_failure(failures, "[C25]", "restricts an appeal entitlement")

    def test_197_c25_must_not_create_or_deny_passes(self):
        """The owner-reservation disclaimer is neutral, not a negative policy."""
        self.inject_all079(
            "The platform must not create or deny appeal rights while UD-044 "
            "remains Open."
        )
        self.assert_clean()

    def test_198_c25_no_approved_appeal_right_passes(self):
        """Stating that no appeal right is approved preserves the reservation."""
        self.inject_all079(
            "No appeal right is approved while UD-044 remains Open."
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C27 - Prompt 09B-K failure-code, ARL and production-chain checks
    # ------------------------------------------------------------------
    def test_199_c27_alf21_owner_consent_regression_fails(self):
        """ALF-21 is an active-permission failure, never per-policy owner consent."""
        self.modify_row_cell(
            "stage-2/16_alliances.md",
            "ALF-21",
            1,
            "required active alliance permission",
            "member nation owner consent",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "ALF-21")

    def test_200_c27_alf23_stockpile_regression_fails(self):
        """ALF-23 must not revert to an insufficient-unreserved-value/stockpile failure."""
        self.modify_row_cell(
            "stage-2/16_alliances.md",
            "ALF-23",
            1,
            "authoritative gross record or frozen turn snapshot",
            "insufficient unreserved value",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "ALF-23")

    def test_201_c27_alf24_capacity_limit_regression_fails(self):
        """ALF-24 must not invent a destination-capacity rejection."""
        self.modify_row_cell(
            "stage-2/16_alliances.md",
            "ALF-24",
            1,
            "no destination-capacity limit exists",
            "the destination capacity limit blocks the donation",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "ALF-24")

    def test_202_c27_req626_treasury_regression_fails(self):
        """REQ-626 must name the ARL, not an alliance treasury."""
        self.modify_row_cell(
            "stage-2/03_requirements_traceability.md",
            "REQ-626",
            1,
            "Alliance Receiving Ledger",
            "alliance treasury",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "REQ-626")

    def test_203_c27_at_most_once_regression_fails(self):
        """Removing the at-most-once safeguard must fail C27."""
        self.modify(
            "stage-2/16_alliances.md",
            "one eligible production event is deducted at most once",
            "one eligible production event may be deducted more than once",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "deducted at most once")

    def test_204_c27_ambiguous_attribution_regression_fails(self):
        """The ambiguous fallback must leave no alliance credited."""
        self.modify(
            "stage-2/16_alliances.md",
            "no alliance is credited",
            "each alliance is credited",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "no alliance is credited")

    def test_205_c27_chain_example_regression_fails(self):
        """The production-chain example D must remain arithmetically stated."""
        self.modify(
            "stage-2/16_alliances_formula_register.md",
            "total alliance tax is 107",
            "total alliance tax is 170",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "total alliance tax is 107")

    def test_206_c27_ax27_post_tax_consumption_regression_fails(self):
        """AX-27 must keep the post-tax same-turn consumption rule."""
        self.modify(
            "stage-2/16_alliances_integration_contracts.md",
            "post-tax net",
            "net production",
            count=-1,
        )
        self.assert_failure(run_checks(self.root), "[C27]", "post-tax net")

    def test_207_c27_ecn213a_safeguard_regression_fails(self):
        """ECN-213a must keep the provisional UD-040 membership safeguard."""
        self.modify(
            "stage-2/10_economy_resources_treasury_and_finances.md",
            "Multiple-membership safeguard (`UD-040` remains Open)",
            "Multiple-membership policy (resolved)",
        )
        self.assert_failure(run_checks(self.root), "[C27]", "membership safeguard")

    def test_208_c27_multiple_membership_safeguard_passes(self):
        """A visible 0% safeguard that preserves gross and UD-040 is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "When multiple memberships make attribution ambiguous, the affected "
            "asset and turn use the visible recorded 0% Alliance-tax safeguard; "
            "gross production is credited in full, no alliance is credited, and "
            "UD-040 remains Open.",
        )
        self.assert_clean()

    def test_209_c27_production_chain_consumption_passes(self):
        """Post-tax same-turn consumption and untaxed stockpiles are valid."""
        self.append(
            "stage-2/16_alliances.md",
            "Later same-turn P3 stages consume only the post-tax net; a 100% rate "
            "leaves zero for later consumption, and an existing stockpile consumed "
            "later is not taxed.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C25 - 09B-L retained, reviewable and avenue-of-appeal semantics
    # ------------------------------------------------------------------
    def test_210_c25_retained_ability_to_appeal_fails(self):
        """A retained procedural ability asserts an appeal policy under UD-044."""
        self.inject_all079("Members retain the ability to submit an appeal.")
        self.assert_failure(
            run_checks(self.root), "[C25]", "preserves an appeal entitlement"
        )

    def test_211_c25_reviewable_on_appeal_fails(self):
        """Reviewability of expulsion is an appeal policy."""
        self.inject_all079("Expulsion decisions are reviewable on appeal.")
        self.assert_failure(
            run_checks(self.root), "[C25]", "makes expulsion reviewable on appeal"
        )

    def test_212_c25_rules_provide_appeal_avenue_fails(self):
        """Providing an avenue of appeal grants procedural access."""
        self.inject_all079(
            "The rules provide an avenue of appeal to every expelled member."
        )
        self.assert_failure(run_checks(self.root), "[C25]", "provides an appeal avenue")

    def test_213_c25_appeal_rights_preserved_fails(self):
        """Preserved appeal rights are a positive entitlement."""
        self.inject_all079("Appeal rights are preserved for expelled members.")
        self.assert_failure(
            run_checks(self.root), "[C25]", "preserves an appeal entitlement"
        )

    def test_214_c25_remains_available_equivalent_fails(self):
        """Availability of an appeal right is the same policy in another shape."""
        self.inject_all079(
            "An appeal right remains available to an expelled member."
        )
        self.assert_failure(
            run_checks(self.root), "[C25]", "grants an appeal entitlement"
        )

    def test_215_c25_able_to_request_review_equivalent_fails(self):
        """Being able to request a review grants an appeal opportunity."""
        self.inject_all079("An expelled member is able to request a review.")
        self.assert_failure(
            run_checks(self.root), "[C25]", "grants an appeal opportunity"
        )

    def test_216_c25_preserve_access_to_mechanism_fails(self):
        """Preserved access to an appeal mechanism is an entitlement."""
        self.inject_all079("The rules preserve access to an appeal mechanism.")
        self.assert_failure(
            run_checks(self.root), "[C25]", "preserves an appeal entitlement"
        )

    def test_217_c25_may_seek_appellate_review_fails(self):
        """A permissive modal plus appellate review grants an opportunity."""
        self.inject_all079("Every expelled member may seek appellate review.")
        self.assert_failure(
            run_checks(self.root), "[C25]", "grants an appeal opportunity"
        )

    def test_218_c25_no_avenue_of_appeal_fails(self):
        """Denying every avenue of appeal is also an unauthorized policy."""
        self.inject_all079("No avenue of appeal exists for expelled members.")
        self.assert_failure(run_checks(self.root), "[C25]", "denies an appeal right")

    def test_219_c25_platform_must_not_allow_appeal_fails(self):
        """A platform prohibition settles the appeal question negatively."""
        self.inject_all079("The platform must not allow an appeal.")
        self.assert_failure(run_checks(self.root), "[C25]", "denies an appeal right")

    def test_220_c25_historical_debate_passes(self):
        """A rejected historical proposal is not active policy."""
        self.inject_all079(
            "This section records the historical debate: the earlier draft "
            "proposed an appeal, which was rejected and is not in force."
        )
        self.assert_clean()

    def test_221_c25_meta_fixture_passes(self):
        """A labelled non-normative fixture is not a rule."""
        self.inject_all079(
            "This is a non-normative illustrative fixture in which a hypothetical "
            "expelled member appeals; it is not a rule."
        )
        self.assert_clean()

    def test_222_c25_no_approved_mechanism_passes(self):
        """A genuine absence statement does not approve an appeal policy."""
        self.inject_all079("No appeal mechanism is currently approved.")
        self.assert_clean()

    def test_223_c25_owner_reserved_question_passes(self):
        """A named UD-044 reservation does not decide the policy."""
        self.inject_all079(
            "Whether expelled members should have an appeal remains "
            "owner-reserved under UD-044."
        )
        self.assert_clean()

    def test_224_c25_audit_creates_no_right_passes(self):
        """A record-keeping disclaimer with no grant is non-policy."""
        self.inject_all079("The audit record creates no appeal right.")
        self.assert_clean()

    def test_225_c25_platform_does_not_decide_passes(self):
        """Recording an outcome without deciding an appeal is neutral."""
        self.inject_all079(
            "The platform records the expulsion outcome but does not decide any appeal."
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C32 - ARL accounting, operational funding and UD-045/UD-046 bounds
    # ------------------------------------------------------------------
    def test_226_c32_missing_all226_fails(self):
        """ALL-226 carries the binding UD-046 boundary."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-226`",
            "**`ALL-226` (`UD-046` Boundary and Non-Implementation Status):**",
            "**REMOVED-226:**",
        )
        self.assert_failure(
            run_checks(self.root), "[C32]", "ALL-226 is missing"
        )

    def test_227_c32_fal008_ownership_token_removed_fails(self):
        """F-AL-008 must state that it creates no ownership."""
        self.section_modify(
            "stage-2/16_alliances_formula_register.md",
            "### F-AL-008",
            "ownership",
            "title",
            count=-1,
        )
        self.assert_failure(
            run_checks(self.root), "[C32]", "lost the accounting token 'no ownership'"
        )

    def test_228_c32_ax28_operational_token_removed_fails(self):
        """AX-28 must name the operational debit path, not a generic expense."""
        self.modify(
            "stage-2/16_alliances_integration_contracts.md",
            "purpose-limited operational platform-cost expense",
            "purpose-limited platform-cost expense",
        )
        self.assert_failure(
            run_checks(self.root), "[C32]", "lost the ARL/donation token 'operational'"
        )

    def test_229_c32_ud046_not_open_fails(self):
        """UD-046 is a reserved owner decision and must remain Open."""
        self.set_row_cell("stage-2/16_alliances.md", "UD-046", 3, "Deferred")
        self.assert_failure(
            run_checks(self.root), "[C32]", "UD-046 is no longer recorded Open"
        )

    def test_230_c32_ud045_not_open_fails(self):
        """UD-045 keeps only its narrow tax-management authorization and stays Open."""
        self.set_row_cell("stage-2/16_alliances.md", "UD-045", 3, "Resolved")
        self.assert_failure(
            run_checks(self.root), "[C32]", "UD-045 is no longer recorded Open"
        )

    def test_231_c32_operational_as_general_withdrawal_fails(self):
        """Operational funding is not a general withdrawal."""
        self.append(
            "stage-2/16_alliances.md",
            "Operational funding is a general withdrawal from the ARL.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C32]",
            "collapses operational funding into a general withdrawal",
        )

    def test_232_c32_player_payment_fails(self):
        """Operational funding cannot pay a member or player."""
        self.append(
            "stage-2/16_alliances.md",
            "The alliance may pay a member from the operational allocation.",
        )
        self.assert_failure(
            run_checks(self.root), "[C32]", "authorizes a player payment"
        )

    def test_233_c32_invented_capacity_fails(self):
        """No capacity limit may be invented for operational funding."""
        self.append(
            "stage-2/16_alliances.md",
            "Operational funding respects an invented capacity limit.",
        )
        self.assert_failure(
            run_checks(self.root), "[C32]", "reintroduces an invented capacity limit"
        )

    def test_234_c32_approved_general_withdrawal_fails(self):
        """General withdrawal remains owner-reserved, never approved."""
        self.append(
            "stage-2/16_alliances.md",
            "General withdrawal is authorized for every member.",
        )
        self.assert_failure(
            run_checks(self.root), "[C32]", "claims an approved general withdrawal"
        )

    def test_235_c32_positive_operational_boundary_passes(self):
        """A sink-only operational debit with no player payment is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "Operational funding pays only a registered platform cost sink from "
            "AVAILABLE value; it never pays a member and is not a general withdrawal.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C33 - Registered record-only and NAP treaty effects
    # ------------------------------------------------------------------
    def test_236_c33_all197_record_only_token_removed_fails(self):
        """ALL-197 must keep the explicit record-only effect category."""
        relative = "stage-2/16_alliances.md"
        content = self.read(relative)
        begin = content.index("**`ALL-197`")
        finish = content.index("**`ALL-198`", begin)
        section = re.sub(
            r"record-only", "descriptive", content[begin:finish], flags=re.I
        )
        self.write(relative, content[:begin] + section + content[finish:])
        self.assert_failure(
            run_checks(self.root), "[C33]", "lost the structured-effect token 'record-only'"
        )

    def test_237_c33_all203_execute_no_mechanic_removed_fails(self):
        """ALL-203 must state that non-NAP effects execute no mechanic."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-203`",
            "execute no mechanic",
            "have no registered effect",
            end="**`ALL-204`",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C33]",
            "lost the effect-scope token 'execute no mechanic'",
        )

    def test_238_c33_record_only_rejected_contradiction_fails(self):
        """A record-only treaty cannot be described as rejected or unsupported."""
        self.append(
            "stage-2/16_alliances.md",
            "A record-only treaty is rejected as unsupported.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C33]",
            "contradicts the record-only catalogue",
        )

    def test_239_c33_non_nap_attack_restriction_fails(self):
        """AT-T02 cannot block attacks without a separately approved effect."""
        self.append(
            "stage-2/16_alliances.md",
            "An AT-T02 treaty blocks every attack between the parties.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C33]",
            "makes a non-NAP treaty restrict attacks",
        )

    def test_240_c33_custom_wording_executable_fails(self):
        """Player-authored wording can never become an executable rule."""
        self.append(
            "stage-2/16_alliances.md",
            "Custom wording is parsed into an executable attack restriction.",
        )
        self.assert_failure(
            run_checks(self.root), "[C33]", "makes treaty prose executable"
        )

    def test_241_c33_positive_record_only_treaty_passes(self):
        """A record-only AT-T05 treaty is a valid diplomatic record."""
        self.append(
            "stage-2/16_alliances.md",
            "A record-only AT-T05 treaty is a valid diplomatic record that "
            "executes no mechanic.",
        )
        self.assert_clean()

    def test_242_c33_positive_only_nap_effect_passes(self):
        """Only AT-T01 selecting AT-E01 blocks attacks."""
        self.append(
            "stage-2/16_alliances.md",
            "Only AT-T01 selecting AT-E01 blocks an attack between covered members.",
        )
        self.assert_clean()

    def test_243_c33_positive_non_executable_prose_passes(self):
        """Free text is descriptive and never parsed or executed."""
        self.append(
            "stage-2/16_alliances.md",
            "Free text is descriptive only and is never parsed into an executable rule.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C34 - National/municipal settings and the three transfer classes
    # ------------------------------------------------------------------
    def test_244_c34_all006_municipal_token_removed_fails(self):
        """ALL-006 must distinguish national and municipal rates from Alliance tax."""
        self.section_modify(
            "stage-2/16_alliances.md",
            "**`ALL-006`",
            "municipal",
            "local",
            end="**`ALL-007`",
            count=-1,
        )
        self.assert_failure(
            run_checks(self.root), "[C34]", "ALL-006 lost the tax-boundary token 'municipal'"
        )

    def test_245_c34_all007_authorized_withholding_removed_fails(self):
        """ALL-007 must preserve the authorized automatic withholding."""
        self.modify(
            "stage-2/16_alliances.md",
            "The authorized automatic withholding of the Alliance's tax",
            "The withholding of the Alliance's tax",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C34]",
            "ALL-007 lost the non-interference token 'authorized automatic withholding'",
        )

    def test_246_c34_all008_voluntary_donations_removed_fails(self):
        """ALL-008 must keep donations as a distinct voluntary class."""
        self.modify(
            "stage-2/16_alliances.md",
            "Voluntary donations are player-initiated and confirmed under",
            "Donations are player-initiated and confirmed under",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C34]",
            "ALL-008 lost the transfer-class token 'voluntary donations'",
        )

    def test_247_c34_alliance_sets_national_tax_fails(self):
        """An Alliance cannot set national or municipal tax rates."""
        self.append(
            "stage-2/16_alliances.md",
            "The alliance may set national tax rates for its members.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C34]",
            "lets an alliance set or change national or municipal tax rates",
        )

    def test_248_c34_automatic_tax_as_donation_fails(self):
        """Automatic withholding is a tax, never a donation."""
        self.append(
            "stage-2/16_alliances.md",
            "Automatic tax is a donation.",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C34]",
            "misclassifies automatic tax as a voluntary donation",
        )

    def test_249_c34_positive_tax_boundary_passes(self):
        """A negative statement of the same boundaries is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "The Alliance cannot alter national or municipal tax rates, and its "
            "automatic withholding is not confiscation of existing wealth.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # Per-Alliance assignment and narrow UD-045 scope
    # ------------------------------------------------------------------
    def test_250_c27_per_alliance_assignment_token_removed_fails(self):
        """ALL-182 must keep bracket assignment scoped to one Alliance."""
        self.modify(
            "stage-2/16_alliances.md",
            "per member nation **per Alliance**",
            "per member nation across Alliances",
        )
        self.assert_failure(
            run_checks(self.root), "[C27]", "lost 'per alliance'"
        )

    def test_251_c32_ud045_narrow_tax_scope_removed_fails(self):
        """UD-045 must keep its narrow tax-management authorization visible."""
        self.modify_row_cell(
            "stage-2/16_alliances.md",
            "UD-045",
            4,
            "bracket creation, editing and deletion",
            "bracket policy",
        )
        self.assert_failure(
            run_checks(self.root),
            "[C32]",
            "UD-045 lost its narrow authorization token 'bracket creation'",
        )

    def test_252_positive_per_alliance_assignment_passes(self):
        """A per-Alliance assignment with no cross-Alliance effect is valid."""
        self.append(
            "stage-2/16_alliances.md",
            "A nation has at most one active bracket assignment per Alliance, and "
            "a bracket in one Alliance is not a bracket in another.",
        )
        self.assert_clean()

    # ------------------------------------------------------------------
    # C25-M - fail / review / safe classification
    # ------------------------------------------------------------------
    def _append_policy_lines(self, lines: list[str]) -> None:
        self.append("stage-2/16_alliances.md", "\n\n".join(lines))

    def _rendered(self, findings: list[str]) -> str:
        return " | ".join(findings).lower()

    def test_253_appeal_policy_variants_fail(self):
        """Every confirmed active appeal/review assertion is a failure."""
        cases = {
            "ZZ-F1": "Members retain appeal rights after expulsion.",
            "ZZ-F2": "Every expelled nation is eligible for appellate review.",
            "ZZ-F3": "An expelled member has a right of reconsideration.",
            "ZZ-F4": "A member may challenge expulsion by review.",
            "ZZ-F5": "The alliance provides procedural access to an appeal process.",
            "ZZ-F6": "Each member has the opportunity to seek review.",
            "ZZ-F7": "Expulsion decisions are reviewable.",
            "ZZ-F8": "Only council members may appeal.",
            "ZZ-F9": "This is illustrative only, but members may appeal expulsion.",
        }
        self._append_policy_lines(
            [
                f"{sentence.rstrip('.')} ({code})."
                for code, sentence in cases.items()
            ]
        )
        failures, reviews = run_checks_with_review(self.root)
        failure_text = self._rendered(failures)
        review_text = self._rendered(reviews)
        for code in cases:
            self.assertIn(
                code.lower(),
                failure_text,
                f"Expected {code} to be a confirmed C25 failure; got: {failure_text[:900]}",
            )
            self.assertNotIn(
                code.lower(),
                review_text,
                f"{code} was confirmed and must not be downgraded to a review finding",
            )

    def test_254_appeal_uncertain_wording_requires_review(self):
        """Uncertain active wording is surfaced, not silently passed."""
        cases = {
            "ZZ-R1": "The alliance will consider whether to establish an appeal procedure.",
            "ZZ-R2": "Appeal eligibility is under consideration.",
            "ZZ-R3": "The alliance could establish an appeal procedure.",
            "ZZ-R4": "Members perhaps could seek review.",
            "ZZ-R5": "A member may be eligible for review.",
        }
        self._append_policy_lines(
            [
                f"{sentence.rstrip('.')} ({code})."
                for code, sentence in cases.items()
            ]
        )
        failures, reviews = run_checks_with_review(self.root)
        failure_text = self._rendered(failures)
        review_text = self._rendered(reviews)
        for code in cases:
            self.assertIn(
                code.lower(),
                review_text,
                f"Expected {code} to require manual review; got: {review_text[:900]}",
            )
            self.assertNotIn(
                code.lower(),
                failure_text,
                f"{code} is uncertain wording and must not be a confirmed failure",
            )

    def test_255_appeal_history_and_non_normative_text_is_safe(self):
        """Historical, rejected, illustrative and external text is allowed."""
        cases = {
            "ZZ-S1": "Historically, members could appeal expulsion under an earlier rule.",
            "ZZ-S2": "A withdrawn proposal would have allowed members to appeal.",
            "ZZ-S3": (
                "This non-normative note records that no appeal procedure is in force."
            ),
            "ZZ-S4": "No appeal mechanism is approved while UD-044 is open.",
            "ZZ-S5": "A rejected proposal to create appeal rights is not adopted.",
            "ZZ-S6": (
                "An illustrative fixture shows a hypothetical appeal that is not "
                "part of this design."
            ),
            "ZZ-S7": "Platform account moderation may review a sanction under NET-01.",
        }
        self._append_policy_lines(
            [f"{code}: {sentence}" for code, sentence in cases.items()]
        )
        failures, reviews = run_checks_with_review(self.root)
        failure_text = self._rendered(failures)
        review_text = self._rendered(reviews)
        for code in cases:
            self.assertNotIn(
                code.lower(),
                failure_text,
                f"{code} is non-normative and must not fail; got: {failure_text[:900]}",
            )
            self.assertNotIn(
                code.lower(),
                review_text,
                f"{code} is non-normative and must not require review; got: {review_text[:900]}",
            )

    def test_256_review_findings_are_not_a_silent_pass(self):
        """A review finding blocks the validator's pass status."""
        self._append_policy_lines(
            ["The alliance will consider whether to establish an appeal procedure."]
        )
        failures, reviews = run_checks_with_review(self.root)
        self.assertEqual(failures, [], f"Unexpected confirmed failure: {failures[:3]}")
        self.assertTrue(reviews, "Uncertain active wording must produce a review finding")

    # ------------------------------------------------------------------
    # C25-N - conservative review detection (Prompt 09B-N)
    # ------------------------------------------------------------------
    def _c25_outcomes(self, cases: dict[str, str]) -> dict[str, str]:
        """Return the exact C25 outcome for each coded sentence."""
        self._append_policy_lines(
            [f"{sentence} ({code})." for code, sentence in cases.items()]
        )
        failures, reviews = run_checks_with_review(self.root)
        failure_text = self._rendered(failures)
        review_text = self._rendered(reviews)
        outcomes: dict[str, str] = {}
        for code in cases:
            if code.lower() in failure_text:
                outcomes[code] = "FAIL"
            elif code.lower() in review_text:
                outcomes[code] = "REVIEW"
            else:
                outcomes[code] = "SAFE"
        return outcomes

    def test_257_recourse_and_former_member_challenge_fail(self):
        """The two audited false negatives are confirmed policy failures."""
        cases = {
            "ZZ-N1": "Members have recourse to appellate review",
            "ZZ-N2": "Former members may challenge their expulsion by review",
            "ZZ-N3": "Former members may not appeal their expulsion",
        }
        self.assertEqual(
            self._c25_outcomes(cases),
            {code: "FAIL" for code in cases},
            "Recourse to review, a former member's challenge and its denial "
            "are all confirmed appeal policy",
        )

    def test_258_redress_wording_requires_manual_review(self):
        """Redress and remedy wording is plausible but not a confident failure."""
        cases = {
            "ZZ-N4": "A former member is entitled to seek redress",
            "ZZ-N5": "A former member is entitled to pursue a remedy",
            "ZZ-N6": "Former members may seek redress",
        }
        self.assertEqual(
            self._c25_outcomes(cases),
            {code: "REVIEW" for code in cases},
            "Redress wording must be surfaced for manual review, not failed or passed",
        )

    def test_259_former_people_label_and_compound_sentences(self):
        """A people label does not immunise policy; historical notes stay safe."""
        cases = {
            "ZZ-N7": "Former rules allowed members to appeal expulsion",
            "ZZ-N8": "Former members historically could appeal under an old rule",
            "ZZ-N9": "Whether former members may appeal remains open under UD-044",
            "ZZ-N10": "This historical note is not operative, but members may appeal expulsion",
            "ZZ-N11": "The record is historical; former members may appeal expulsion",
        }
        self.assertEqual(
            self._c25_outcomes(cases),
            {
                "ZZ-N7": "SAFE",
                "ZZ-N8": "SAFE",
                "ZZ-N9": "SAFE",
                "ZZ-N10": "FAIL",
                "ZZ-N11": "FAIL",
            },
            "Historical framing stays safe, but a separate active entitlement "
            "in the same compound sentence must fail",
        )

    def test_260_eight_audited_false_negatives(self):
        """The eight 09B-O audited procedural statements classify correctly."""
        cases = {
            "ZZ-O1": "A member may petition for reconsideration of expulsion",
            "ZZ-O2": "Expelled members are permitted to seek a review",
            "ZZ-O3": "The council must hear appeals from expelled members",
            "ZZ-O4": "Expulsion decisions are subject to reconsideration",
            "ZZ-O5": "A former member has the right to challenge removal",
            "ZZ-O6": "Members may request review of expulsion decisions",
            "ZZ-O7": "All expulsion decisions are final and cannot be reviewed",
            "ZZ-O8": "Expelled members may petition the council for redress",
        }
        self.assertEqual(
            self._c25_outcomes(cases),
            {
                "ZZ-O1": "FAIL",
                "ZZ-O2": "FAIL",
                "ZZ-O3": "FAIL",
                "ZZ-O4": "FAIL",
                "ZZ-O5": "FAIL",
                "ZZ-O6": "FAIL",
                "ZZ-O7": "FAIL",
                "ZZ-O8": "REVIEW",
            },
            "Confirmed grants and denials fail; uncertain redress access is reviewed",
        )

    def test_261_procedural_domain_controls(self):
        """Positive, negative, ambiguous, historical and unrelated controls."""
        cases = {
            "ZZ-C1": "A member may appeal an expulsion decision",
            "ZZ-C2": "Expelled members may not appeal an expulsion decision",
            "ZZ-C3": "An expelled member may seek a remedy",
            "ZZ-C4": "The rejected proposal would have let members appeal expulsion",
            "ZZ-C5": "UD-044 remains owner-reserved and no appeal policy is approved",
            "ZZ-C6": "UD-044 remains open, but expelled members may appeal expulsion",
            "ZZ-C7": "Expelled members may appeal, unless the council decides otherwise",
            "ZZ-C8": "This note is historical, but former members may appeal expulsion",
            "ZZ-C9": "The council reviews the annual budget every turn",
            "ZZ-C10": "The alliance faces a strategic challenge in the north",
        }
        self.assertEqual(
            self._c25_outcomes(cases),
            {
                "ZZ-C1": "FAIL",
                "ZZ-C2": "FAIL",
                "ZZ-C3": "REVIEW",
                "ZZ-C4": "SAFE",
                "ZZ-C5": "SAFE",
                "ZZ-C6": "FAIL",
                "ZZ-C7": "FAIL",
                "ZZ-C8": "FAIL",
                "ZZ-C9": "SAFE",
                "ZZ-C10": "SAFE",
            },
            "Active grants and denials fail, ambiguous remedies are reviewed, "
            "and historical, reserved or unrelated wording stays safe",
        )

    # ------------------------------------------------------------------
    # C25-P - three final audited false negatives (Prompt 09B-P)
    # ------------------------------------------------------------------
    def test_262_challenge_to_dismissal_requires_review(self):
        """A challenge to an ambiguous "dismissal" is surfaced, not passed."""
        cases = {"ZZ-P1": "A former member may challenge dismissal"}
        self.assertEqual(
            self._c25_outcomes(cases),
            {"ZZ-P1": "REVIEW"},
            "Dismissal may mean expulsion, but the context is not explicit",
        )

    def test_263_available_grievance_process_requires_review(self):
        """An unspecified grievance route is a potential formal remedy."""
        cases = {"ZZ-P2": "A grievance process is available for expelled members"}
        self.assertEqual(
            self._c25_outcomes(cases),
            {"ZZ-P2": "REVIEW"},
            "A passive grievance process is plausible but not a confirmed policy",
        )

    def test_264_explicit_redress_entitlement_fails(self):
        """An express procedural entitlement concerning expulsion is confirmed."""
        cases = {"ZZ-P3": "There is a right to seek redress for an expulsion"}
        self.assertEqual(
            self._c25_outcomes(cases),
            {"ZZ-P3": "FAIL"},
            "An explicit right to seek redress for expulsion must fail validation",
        )

    def test_265_final_c25_compact_controls(self):
        """Six controls keep policy, ambiguity and non-normative text distinct."""
        cases = {
            "ZZ-Q1": (
                "Historically, a rejected proposal would have allowed members "
                "to challenge dismissal by review"
            ),
            "ZZ-Q2": (
                "UD-044 remains unresolved and no appeal or grievance policy "
                "has been approved"
            ),
            "ZZ-Q3": (
                "The alliance guarantees a grievance mechanism to expelled members"
            ),
            "ZZ-Q4": (
                "UD-044 remains unresolved, but the alliance guarantees a "
                "grievance process to expelled members"
            ),
            "ZZ-Q5": "A former member may challenge dismissal",
            "ZZ-Q6": (
                "An expelled member has the right to seek redress for an expulsion"
            ),
        }
        self.assertEqual(
            self._c25_outcomes(cases),
            {
                "ZZ-Q1": "SAFE",
                "ZZ-Q2": "SAFE",
                "ZZ-Q3": "FAIL",
                "ZZ-Q4": "FAIL",
                "ZZ-Q5": "REVIEW",
                "ZZ-Q6": "FAIL",
            },
            "Historical and reserved text stays safe, a current guarantee and a "
            "compound disclaimer-plus-entitlement fail, ambiguous dismissal is "
            "reviewed, and explicit redress fails",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
