#!/usr/bin/env python3
"""Focused regression tests for the decision registers (stdlib unittest).

Run: `python docs/qa_backups/test_decision_registers.py`

These tests guard the 2026-10-23 micro-correction defects and the state
advanced by Stage 2 Prompt 03 (2026-10-24):
  * a current decision range that stops before the last recorded decision;
  * prompt-owned UD rows misclassified as generic Open;
  * totals that do not reconcile with the UD status cells;
  * a backup policy that treats one default `db dump` as roles+schema+data;
  * a continuity set that still names an earlier prompt once the next one is current.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]

CURRENT_FILES = [
    DOCS / "AI_CONTEXT.md",
    DOCS / "AI_HANDOFF.md",
    DOCS / "PROJECT_PROGRESS.md",
    DOCS / "stage-2" / "00_stage_2_handoff.md",
    DOCS / "stage-2" / "05_unresolved_design_decisions.md",
    DOCS / "stage-2" / "08_final_decision_closure_audit.md",
]

RESOLVED = {
    "UD-001", "UD-002", "UD-003", "UD-004", "UD-008", "UD-010", "UD-011",
    "UD-014", "UD-015", "UD-016", "UD-018", "UD-019", "UD-020", "UD-021",
    "UD-025", "UD-027", "UD-028", "UD-029", "UD-030", "UD-009",
    "UD-034", "UD-035", "UD-013", "UD-033", "UD-012", "UD-039", "UD-032",
}
DEFERRED = {
    "UD-022": "13",
    "UD-023": "13", "UD-031": "12",
}
OPEN = {"UD-005", "UD-006", "UD-007", "UD-017", "UD-026", "UD-036",
        "UD-037", "UD-038", "UD-040", "UD-041", "UD-042", "UD-043", "UD-044", "UD-045", "UD-046", "UD-047", "UD-048", "UD-049",
        "UD-050", "UD-051",
        "UD-052", "UD-053", "UD-054", "UD-055", "UD-056", "UD-057", "UD-058", "UD-059", "UD-060",}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def decision_ids() -> list[str]:
    return re.findall(r"^\|\s*(D-\d{3})\s*\|", read(DOCS / "DECISIONS.md"), re.M)


def ud_rows() -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for line in read(DOCS / "stage-2" / "05_unresolved_design_decisions.md").splitlines():
        m = re.match(r"\|\s*(UD-\d{3})\s*\|", line)
        if m:
            rows[m.group(1)] = [c.strip() for c in line.strip().strip("|").split("|")]
    return rows


class DecisionRangeTests(unittest.TestCase):
    def test_log_end_is_derived_and_contiguous(self) -> None:
        ids = decision_ids()
        self.assertTrue(ids)
        last = int(ids[-1][2:])
        self.assertEqual(ids, [f"D-{i:03d}" for i in range(1, last + 1)])

    def test_status_range_matches_the_log(self) -> None:
        ids = decision_ids()
        expected = f"D-001..{ids[-1]}"
        for path in (DOCS / "AI_CONTEXT.md", DOCS / "AI_HANDOFF.md", DOCS / "PROJECT_PROGRESS.md"):
            text = read(path)
            m = re.search(r"^decisions_range:\s*(\S+)\s*$", text, re.M)
            self.assertIsNotNone(m, path.name)
            self.assertEqual(m.group(1), expected, path.name)

    def test_no_current_range_stops_at_d029(self) -> None:
        for path in CURRENT_FILES:
            text = read(path)
            self.assertNotIn("D-001…D-029", text, path.name)
            self.assertNotIn("D-001..D-029", text, path.name)

    def test_no_stale_decision_count_summaries(self) -> None:
        for path in CURRENT_FILES:
            low = read(path).lower()
            with self.subTest(file=path.name):
                self.assertNotIn("fifteen design decisions", low)
                self.assertNotIn("sixteen pending", low)
                self.assertNotIn("twenty-nine entries", low)


class UnresolvedStatusTests(unittest.TestCase):
    def test_every_row_has_one_exclusive_status(self) -> None:
        rows = ud_rows()
        self.assertEqual(sorted(rows), [f"UD-{i:03d}" for i in range(1, 61)])
        counts = {"Resolved": 0, "Deferred": 0, "Open": 0}
        for cells in rows.values():
            self.assertGreaterEqual(len(cells), 9)
            status = cells[8]
            if status.startswith("**Resolved"):
                counts["Resolved"] += 1
            elif status.startswith("**Deferred"):
                counts["Deferred"] += 1
            elif status.startswith("Open"):
                counts["Open"] += 1
            else:
                self.fail(f"unclassified status: {status!r}")
        self.assertEqual(counts, {"Resolved": 28, "Deferred": 3, "Open": 29})
        self.assertEqual(sum(counts.values()), 60)

    def test_deferred_rows_name_their_owning_prompt(self) -> None:
        rows = ud_rows()
        for uid, prompt in DEFERRED.items():
            cells = rows[uid]
            self.assertTrue(cells[8].startswith(f"**Deferred to Prompt {prompt}**"), uid)
            self.assertEqual(cells[7], prompt, uid)

    def test_open_rows_are_the_open_evidence_items(self) -> None:
        rows = ud_rows()
        for uid in OPEN:
            self.assertTrue(rows[uid][8].startswith("Open"), uid)
        for uid in RESOLVED:
            self.assertTrue(rows[uid][8].startswith("**Resolved"), uid)

    def test_section_6_matches_non_resolved_rows(self) -> None:
        text = read(DOCS / "stage-2" / "05_unresolved_design_decisions.md")
        section = text[text.index("## 6."):]
        ids = re.findall(r"^\|\s*`?(UD-\d{3})`?\s*\|", section, re.M)
        self.assertEqual(ids, sorted(list(DEFERRED) + list(OPEN)))


class BackupPolicyTests(unittest.TestCase):
    def _policy_texts(self) -> dict[str, str]:
        dec = read(DOCS / "DECISIONS.md")
        dd = read(DOCS / "stage-2" / "04_approved_and_provisional_decisions.md")
        audit = read(DOCS / "stage-2" / "08_final_decision_closure_audit.md")
        d025 = next(ln for ln in dec.splitlines() if ln.startswith("| D-025 |"))
        dd043 = next(ln for ln in dd.splitlines() if ln.startswith("| DD-043 |"))
        return {"D-025": d025, "DD-043": dd043, "audit": audit}

    def test_three_exports_are_distinguished(self) -> None:
        for label, text in self._policy_texts().items():
            low = text.lower()
            with self.subTest(document=label):
                self.assertIn("--role-only", low)
                self.assertIn("--data-only", low)
                self.assertIn("custom roles", low)
                self.assertTrue("no table data" in low or "no data" in low)

    def test_no_single_command_is_called_a_full_backup(self) -> None:
        for label, text in self._policy_texts().items():
            with self.subTest(document=label):
                self.assertNotIn("`supabase db dump` — roles, schema, data", text)

    def test_testing_remains_unexecuted(self) -> None:
        dec = read(DOCS / "DECISIONS.md")
        d025 = next(ln for ln in dec.splitlines() if ln.startswith("| D-025 |"))
        self.assertIn("Awaiting validation", d025)
        self.assertIn("no drill has run", d025)


class HandoffTests(unittest.TestCase):
    def test_prompt_08_is_complete_and_09b_is_accepted(self) -> None:
        # 07C closed the trade workstream on 2026-10-29 and 08C closed
        # diplomacy on 2026-10-30; Phase 09B is accepted at the
        # specification/documentation level, 09C is complete at the same
        # level, 10A research, the 10B specification and the 10C
        # workflow/acceptance companion are complete, and Prompt 11 split into
        # 11A/11B/11C with 11A research complete on 2026-11-05, so the live
        # sub-prompt recorded in every STATUS block is 11C.
        # 2026-11-06 (Prompt 11C): the 11C workflow/acceptance companion closed the
        # Prompt 11 family at the design level, so every STATUS block now records 12.
        for path in (DOCS / "AI_CONTEXT.md", DOCS / "AI_HANDOFF.md", DOCS / "PROJECT_PROGRESS.md"):
            self.assertRegex(read(path), r"stage_2_next_prompt:\s*12\b", path.name)
        progress = read(DOCS / "PROJECT_PROGRESS.md")
        self.assertRegex(progress, r"\| 04 \| Economy[^\n]*\| \*\*Complete\*\*")
        self.assertRegex(progress, r"\| 05 \| Cities[^\n]*\| \*\*Complete\*\*")
        self.assertRegex(progress, r"\| 06 \| Population[^\n]*\| \*\*Complete\*\*")
        self.assertRegex(progress, r"\| 07 \| Trade[^\n]*\| \*\*Complete\*\*")
        # 2026-10-30: all three diplomacy sub-prompts are complete. The
        # completion is specification-level only and must say so.
        row08 = next((ln for ln in progress.splitlines() if ln.startswith("| 08 |")), "")
        self.assertIn("**08A complete**", row08)
        self.assertIn("**08B complete**", row08)
        self.assertIn("**08C complete**", row08)
        self.assertIn("**Prompt 08 complete**", row08)
        self.assertIn("designed, **not implemented**", row08)
        self.assertIn("Prompt 08 — diplomacy — is complete", progress)
        row09 = next((ln for ln in progress.splitlines() if ln.startswith("| 09 |")), "")
        self.assertIn("**ACCEPTED", row09)
        self.assertIn("Prompt 09C: complete at the specification/documentation level", row09)
        self.assertIn("Prompt 10A: complete", row09)
        self.assertIn("Prompt 10B: complete at the specification/documentation level", row09)
        # PROJECT_PROGRESS also carries a Stage 1 report row numbered 10, so
        # select the Stage 2 warfare row by its table title, not by number.
        row10 = next((ln for ln in progress.splitlines()
                      if ln.startswith("| 10 | Warfare, campaigns and postwar settlements |")), "")
        self.assertTrue(row10, "PROJECT_PROGRESS has no Stage 2 Prompt 10 row")
        self.assertIn("10B specification complete", row10)
        self.assertIn("Prompt 10C complete", row10)
        # 2026-11-06 (Prompt 11C): Prompt 11 closed, so row 10 must name Prompt 12.
        self.assertIn("Prompt 12 is next", row10)
        # 2026-11-05: the Stage 2 Prompt 11 row records 11A's research closure
        # and names 11B as live, without claiming a B-11 rulebook.
        row11 = next((ln for ln in progress.splitlines()
                      if ln.startswith("| 11 | World events, objectives, rankings and long-term progression")), "")
        self.assertTrue(row11, "PROJECT_PROGRESS has no Stage 2 Prompt 11 row")
        self.assertIn("11A COMPLETE at the research/design-foundations level", row11)
        # 2026-11-06 (Prompt 11C): 11C is complete, not "next and not started".
        self.assertIn("11C complete at the specification/documentation level", row11)
        self.assertIn("Prompt 12 next and not started", row11)
        self.assertIn("B-11 rulebook at the specification level", row11)


if __name__ == "__main__":
    unittest.main(verbosity=2)
