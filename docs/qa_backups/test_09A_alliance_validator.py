#!/usr/bin/env python3
"""Self-tests for 09A_validate_alliance.py.

The clean fixture is the current accepted documentation tree, copied to a
temporary directory. Each negative fixture applies one declared mutation to a
fresh copy and asserts that the validator fails. A mutation that passes is a
validator gap, not a document success.

Run: python docs/qa_backups/test_09A_alliance_validator.py
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "alliance_validator", HERE / "09A_validate_alliance.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.unlink(missing_ok=True)
    path.write_text(text, encoding="utf-8")


def _link_or_copy(src: str, dst: str) -> str:
    """Share the clean fixture inode; fall back to a real copy off-volume."""
    try:
        os.link(src, dst)
    except OSError:
        return shutil.copy2(src, dst)
    return dst


def edit(path: Path, old: str, new: str) -> None:
    text = read(path)
    if old not in text:
        raise AssertionError(f"fixture target not found in {path}: {old[:80]!r}")
    write(path, text.replace(old, new, 1))


def matrix_path(root: Path) -> Path:
    return root / "stage-2" / "research" / "09A_alliance_integration_matrix.md"


def append_audit_row(root: Path, row: str) -> None:
    path = matrix_path(root)
    text = read(path)
    marker = "\n\n---\n\n## 4. Fields 12–20"
    if marker not in text:
        raise AssertionError("audit section end marker not found")
    write(path, text.replace(marker, "\n" + row + marker, 1))


def edit_audit_row(root: Path, ax: str, req: str, column: int, value: str) -> None:
    path = matrix_path(root)
    lines = read(path).splitlines()
    prefix = f"| {ax} | {req} |"
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 7:
                raise AssertionError(f"unexpected audit width for {ax}/{req}: {len(cells)}")
            cells[column] = value
            lines[i] = "| " + " | ".join(cells) + " |"
            write(path, "\n".join(lines) + "\n")
            return
    raise AssertionError(f"audit row {ax}/{req} not found")


def edit_summary_owner(root: Path, ax: str, value: str) -> None:
    path = matrix_path(root)
    lines = read(path).splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {ax} |"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 10:
                continue
            cells[3] = value
            lines[i] = "| " + " | ".join(cells) + " |"
            write(path, "\n".join(lines) + "\n")
            return
    raise AssertionError(f"summary row {ax} not found")


def edit_source_row(root: Path, sid: str, column: int, value: str) -> None:
    path = root / "stage-2" / "research" / "09A_alliance_sources_findings.md"
    lines = read(path).splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {sid} |"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 9:
                raise AssertionError(f"unexpected source width for {sid}: {len(cells)}")
            cells[column] = value
            lines[i] = "| " + " | ".join(cells) + " |"
            write(path, "\n".join(lines) + "\n")
            return
    raise AssertionError(f"source row {sid} not found")


class AllianceValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory(prefix="09a-alliance-")
        cls.clean = Path(cls._tmp.name) / "clean"
        shutil.copytree(DOCS, cls.clean)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def work(self, name: str) -> Path:
        path = Path(self._tmp.name) / name
        if path.exists():
            shutil.rmtree(path)
        shutil.copytree(self.clean, path, copy_function=_link_or_copy)
        return path

    def assert_fails(self, name: str, mutate) -> None:
        root = self.work(name)
        mutate(root)
        problems, checks = VALIDATOR.validate(root)
        self.assertGreater(checks, 0, f"{name}: validator ran no checks")
        self.assertTrue(problems, f"{name}: mutation passed the validator: {checks} checks, 0 problems")

    def test_clean_fixture_passes(self) -> None:
        problems, checks = VALIDATOR.validate(self.clean)
        self.assertEqual([], problems, f"clean fixture failed with {checks} checks")

    def test_01_ax01_req012_direct_founding(self) -> None:
        self.assert_fails(
            "neg01",
            lambda root: append_audit_row(
                root,
                "| AX-01 | REQ-012 | Bilateral relationships are typed | **DIRECT DEPENDENCY** | "
                "Bilateral relationship typing is treated as founding eligibility evidence. | Provisional | — |",
            ),
        )

    def test_02_ax06_req530_direct_deposit(self) -> None:
        self.assert_fails(
            "neg02",
            lambda root: append_audit_row(
                root,
                "| AX-06 | REQ-530 | The only diplomatic authority is the nation owner | **DIRECT DEPENDENCY** | "
                "National diplomatic authority is treated as a treasury-deposit requirement. | Provisional | — |",
            ),
        )

    def test_03_ax09_req012_direct_membership(self) -> None:
        self.assert_fails(
            "neg03",
            lambda root: append_audit_row(
                root,
                "| AX-09 | REQ-012 | Bilateral relationships are typed | **DIRECT DEPENDENCY** | "
                "Bilateral relationship typing is treated as membership-application support. | Provisional | — |",
            ),
        )

    def test_04_ax16_req532_direct_position(self) -> None:
        self.assert_fails(
            "neg04",
            lambda root: append_audit_row(
                root,
                "| AX-16 | REQ-532 | Diplomacy is read-only in TRANSITION or CRISIS | **DIRECT DEPENDENCY** | "
                "The transition freeze is treated as the alliance-position requirement. | Provisional | — |",
            ),
        )

    def test_05_nonexistent_requirement(self) -> None:
        self.assert_fails(
            "neg05",
            lambda root: append_audit_row(
                root,
                "| AX-05 | REQ-999 | Nonexistent requirement | **RELATED CONSTRAINT** | "
                "This identifier does not exist in the register and must be rejected. | No | — |",
            ),
        )

    def test_06_supporting_relabelled_direct(self) -> None:
        self.assert_fails(
            "neg06",
            lambda root: edit_audit_row(root, "AX-19", "REQ-057", 3, "**DIRECT DEPENDENCY**"),
        )

    def test_07_direct_without_explanation(self) -> None:
        self.assert_fails(
            "neg07",
            lambda root: edit_audit_row(root, "AX-10", "REQ-057", 4, "—"),
        )

    def test_08_economy_assigned_to_alliance(self) -> None:
        self.assert_fails(
            "neg08",
            lambda root: edit_summary_owner(root, "AX-06", "Alliance"),
        )

    def test_09_alliance_leader_binds_diplomacy(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            text = read(path)
            text += "\nThe Alliance Leader consents to national treaties on behalf of members.\n"
            write(path, text)

        self.assert_fails("neg09", mutate)

    def test_10_discord_bot_approved(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_research.md"
            text = read(path)
            text += "\nDiscord bot integration is approved for the first release.\n"
            write(path, text)

        self.assert_fails("neg10", mutate)

    def test_11_real_time_chat_reintroduced(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_research.md"
            text = read(path)
            text += "\nReal-time alliance chat rooms are included in the first release.\n"
            write(path, text)

        self.assert_fails("neg11", mutate)

    def test_12_two_next_prompts(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "01_stage_2_prompt_roadmap.md"
            text = read(path)
            marker = "Prompt 09C — Alliance workflows, edge cases, acceptance matrix and release-gate evidence"
            if marker not in text:
                raise AssertionError("roadmap 09C registration heading not found")
            write(path, text + "\nPrompt 09B is the next task and has started.\n")

        self.assert_fails("neg12", mutate)

    def test_13_permission_without_source(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_research.md"
            text = read(path)
            text = text.replace("15 possible permissions", "16 possible permissions", 1)
            marker = "| 15 | Promote Self to Leader |"
            if marker not in text:
                raise AssertionError("permission table end not found")
            extra = "| 16 | Teleport Bank | “moves the bank” | Move value | Leader |\n"
            write(path, text.replace(marker, extra + marker, 1))

        self.assert_fails("neg13", mutate)

    def test_14_forum_root_marked_primary(self) -> None:
        def mutate(root: Path) -> None:
            edit_source_row(
                root,
                "ALS-016",
                3,
                "https://forum.politicsandwar.com/",
            )
            edit_source_row(root, "ALS-016", 4, "PRIMARY/OFFICIAL")

        self.assert_fails("neg14", mutate)

    def test_15_ud039_no_object_mislabelled_option_a(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_research.md"
            text = read(path)
            old = "This is **not option (a)**: option (a) still creates alliance-level treaties under the B-08 object."
            if old not in text:
                raise AssertionError("UD-039 recommendation wording not found")
            write(path, text.replace(old, "This is **option (a)**: no alliance-level treaty object.", 1))

        self.assert_fails("neg15", mutate)

    def test_16_ax08_req141_direct(self) -> None:
        self.assert_fails(
            "neg16",
            lambda root: edit_audit_row(root, "AX-08", "REQ-141", 3, "**DIRECT DEPENDENCY**"),
        )

    def test_17_ax08_req142_direct(self) -> None:
        self.assert_fails(
            "neg17",
            lambda root: edit_audit_row(root, "AX-08", "REQ-142", 3, "**DIRECT DEPENDENCY**"),
        )

    def test_18_ax08_req176_numerical_capacity(self) -> None:
        self.assert_fails(
            "neg18",
            lambda root: edit_audit_row(
                root,
                "AX-08",
                "REQ-176",
                4,
                "Establishes a numerical capacity limit of 10,000 units for the separate audited pool.",
            ),
        )

    def test_19_ax08_missing_no_existing_req(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            text = read(path)
            prefix = "| AX-08 | — |"
            lines = [l for l in text.splitlines() if not l.startswith(prefix)]
            write(path, "\n".join(lines) + "\n")

        self.assert_fails("neg19", mutate)

    def test_20_ax08_omits_ud046(self) -> None:
        self.assert_fails(
            "neg20",
            lambda root: edit_audit_row(root, "AX-08", "—", 6, "—"),
        )

    def test_21_ud046_marked_resolved(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "05_unresolved_design_decisions.md"
            text = read(path)
            marker = "| UD-046 | Who owns the treasury"
            lines = text.splitlines()
            for i, l in enumerate(lines):
                if l.startswith(marker):
                    lines[i] = l.replace("| Open —", "| Resolved —")
                    write(path, "\n".join(lines) + "\n")
                    return
            raise AssertionError("UD-046 register row not found")

        self.assert_fails("neg21", mutate)

    def test_22_national_warehouse_substituted_for_pool(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            text = read(path)
            write(path, text + "\nNational warehouse capacity automatically establishes alliance treasury capacity.\n")

        self.assert_fails("neg22", mutate)

    def test_23_alliance_deposit_described_as_purchase(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            text = read(path)
            write(path, text + "\nAn alliance deposit is treated as a national purchase operation.\n")

        self.assert_fails("neg23", mutate)

    def test_24_stale_relationship_totals(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_reference_review.md"
            text = read(path)
            write(path, text.replace("| Requirement relationships reviewed | 77 |", "| Requirement relationships reviewed | 76 |", 1))

        self.assert_fails("neg24", mutate)

    def test_25_research_matrix_inconsistent(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_reference_review.md"
            text = read(path)
            write(path, text.replace("REQ-176 DIRECT; REQ-141/142 RELATED", "REQ-176/141/142 DIRECT", 1))

        self.assert_fails("neg25", mutate)

    def test_26_unapproved_capacity_req_approved(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "03_requirements_traceability.md"
            text = read(path)
            extra = "\n| REQ-648 | Alliance pool storage capacity is fixed at 10,000 units | Alliance | Approved | [09A §8](research/09A_alliance_research.md) | B-09 | 09B | REQ-176 | Document review |\n"
            write(path, text + extra)

        self.assert_fails("neg26", mutate)


    def test_27_ax08_summary_economy_capacity(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            lines = read(path).splitlines()
            for i, line in enumerate(lines):
                if line.startswith("| AX-08 |"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) == 10:
                        cells[2] = "Hold pooled resources within Economy capacity"
                        lines[i] = "| " + " | ".join(cells) + " |"
                        write(path, "\n".join(lines) + "\n")
                        return
            raise AssertionError("AX-08 summary row not found")

        self.assert_fails("neg27", mutate)

    def test_28_ax08_failure_reject_overcapacity(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            lines = read(path).splitlines()
            for i, line in enumerate(lines):
                if line.startswith("| AX-08 | System |"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) == 10:
                        cells[5] = "Reject over-capacity deposit cleanly"
                        lines[i] = "| " + " | ".join(cells) + " |"
                        write(path, "\n".join(lines) + "\n")
                        return
            raise AssertionError("AX-08 fields row not found")

        self.assert_fails("neg28", mutate)

    def test_29_ax08_resource_impact_capacity_only(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            lines = read(path).splitlines()
            for i, line in enumerate(lines):
                if line.startswith("| AX-08 | System |"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) == 10:
                        cells[4] = "Capacity only"
                        lines[i] = "| " + " | ".join(cells) + " |"
                        write(path, "\n".join(lines) + "\n")
                        return
            raise AssertionError("AX-08 fields row not found")

        self.assert_fails("neg29", mutate)

    def test_30_stale_handoff_09ac_status(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "00_stage_2_handoff.md"
            text = read(path)
            write(path, text.replace("accepted after the final 09A-F closure pass", "accepted after 09A-C", 1))

        self.assert_fails("neg30", mutate)

    def test_31_stale_outline_09ac_status(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "02_master_game_design_bible_outline.md"
            text = read(path)
            write(path, text.replace("accepted after Prompt 09A-F", "accepted after 09A-C", 1))

        self.assert_fails("neg31", mutate)

    def test_32_stale_validator_count_829(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "00_stage_2_handoff.md"
            text = read(path)
            write(path, text + "\nTargeted validator reports 829 checks.\n")

        self.assert_fails("neg32", mutate)


    def test_33_current_status_stale_09ad(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "AI_CONTEXT.md"
            text = read(path)
            write(path, text.replace("Prompt 09A accepted after 09A-F", "Prompt 09A accepted after 09A-D", 1))

        self.assert_fails("neg33", mutate)

    def test_34_current_status_stale_09ae(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "AI_HANDOFF.md"
            text = read(path)
            write(path, text.replace("Prompt 09A accepted after 09A-F", "Prompt 09A accepted after 09A-E", 1))

        self.assert_fails("neg34", mutate)

    def test_35_current_status_stale_09ac(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "PROJECT_PROGRESS.md"
            text = read(path)
            write(path, text.replace("Prompt 09A accepted after 09A-F", "Prompt 09A accepted after 09A-C", 1))

        self.assert_fails("neg35", mutate)

    def test_36_omission_of_09af_in_status_document(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "PROJECT_PROGRESS.md"
            text = read(path)
            write(path, text.replace("09A-F", "09A"))

        self.assert_fails("neg36", mutate)

    def test_37_missing_section_36_in_progress_log(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "06_stage_2_progress_log.md"
            text = read(path)
            write(path, text.replace("## 36. Prompt 09A-F", "## 36. Omitted Section", 1))

        self.assert_fails("neg37", mutate)

    def test_38_missing_section_26_in_research(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "stage-2" / "research" / "09A_alliance_research.md"
            text = read(path)
            write(path, text.replace("## 26. Prompt 09A-F correction record", "## 26. Omitted Section", 1))

        self.assert_fails("neg38", mutate)

    def test_39_missing_09af_in_matrix_changelog(self) -> None:
        def mutate(root: Path) -> None:
            path = matrix_path(root)
            text = read(path)
            write(path, text.replace("| AX-08 (09A-F) |", "| AX-08 (omitted) |", 1))

        self.assert_fails("neg39", mutate)

    def test_40_disagreement_on_next_prompt(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "AI_CONTEXT.md"
            text = read(path)
            # 2026-11-04: 10C is complete and Prompt 11 is the registered next
            # prompt, so disagreement is a STATUS block pointing elsewhere.
            write(path, text.replace("stage_2_next_prompt: 11", "stage_2_next_prompt: 09C"))

        self.assert_fails("neg40", mutate)

    def test_41_stale_progress_log_reference(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "ROADMAP.md"
            text = read(path)
            write(path, text.replace("[§36](stage-2/06_stage_2_progress_log.md)", "[§35](stage-2/06_stage_2_progress_log.md)"))

        self.assert_fails("neg41", mutate)

    def test_42_false_positive_historical_entries_intact(self) -> None:
        root = self.work("fp42")
        path = root / "stage-2" / "06_stage_2_progress_log.md"
        text = read(path)
        marker = "## 34. Prompt 09A-D"
        extra_history = "\nHistorical note: Prompt 09A-C was accepted here (§33) and Prompt 09A-D was accepted here (§34).\n"
        write(path, text.replace(marker, extra_history + marker, 1))

        problems, checks = VALIDATOR.validate(root)
        self.assertEqual([], problems, f"historical entries triggered false positive: {problems}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
