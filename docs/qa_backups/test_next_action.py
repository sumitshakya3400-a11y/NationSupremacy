#!/usr/bin/env python3
"""Regression tests for the stale-next-action detector (stdlib `unittest`).

Run: `python docs/qa_backups/test_next_action.py`

Demonstrates the behaviours the validators rely on:
  * a *current* next-action field pointing at an earlier prompt is rejected;
  * the current prompt number is read from the STATUS block when present;
  * a labelled *historical* mention of an earlier prompt is accepted.

The last test applies the detector to the real continuity set, so a future
stale sentence fails here as well as in the two validators.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True  # keep the repo free of __pycache__
sys.path.insert(0, str(Path(__file__).resolve().parent))

from status_rules import (  # noqa: E402
    CURRENT_PROMPT,
    PROMPT_ACCEPTANCE,
    COMPLETED_SUBPROMPTS,
    NEXT_PROMPT,
    continuity_problems,
    status_next_prompt,
    stale_next_actions,
    subprompt_status_problems,
)

DOCS = Path(__file__).resolve().parents[1]


class StaleNextActionTests(unittest.TestCase):
    def test_current_field_naming_prompt_01_is_rejected(self) -> None:
        text = "**Next action:** Stage 2, Prompt 01 — structure and traceability.\n"
        self.assertEqual(len(stale_next_actions(text)), 1)

    def test_current_field_naming_prompt_03_is_rejected_after_04(self) -> None:
        text = "**Next action:** Stage 2, Prompt 03 — onboarding and progression.\n"
        self.assertEqual(len(stale_next_actions(text)), 1)

    def test_current_field_naming_prompt_04_is_accepted(self) -> None:
        text = "**Next action:** Stage 2, Prompt 04 — economy and treasury.\n"
        self.assertEqual(stale_next_actions(text), [])

    def test_status_block_overrides_the_default(self) -> None:
        text = (
            "<!-- STATUS:BEGIN -->\nstage_2_next_prompt: 04\n<!-- STATUS:END -->\n\n"
            "**Next action:** Stage 2, Prompt 03.\n"
        )
        self.assertEqual(len(stale_next_actions(text, current_prompt=1)), 1)

    def test_historical_mention_is_accepted(self) -> None:
        text = (
            "*Historical:* at the time of that closure the next activity was "
            "Stage 2, Prompt 01; that prompt is complete and the current next "
            "action is Stage 2, Prompt 04.\n"
        )
        self.assertEqual(stale_next_actions(text), [])

    def test_historical_marker_without_new_action_is_accepted(self) -> None:
        text = "The report's next action was Prompt 01; it has since been superseded.\n"
        self.assertEqual(stale_next_actions(text), [])

    def test_prose_without_a_next_action_marker_is_ignored(self) -> None:
        text = "Prompt 01 delivered the Bible frame, the tracker and both registers.\n"
        self.assertEqual(stale_next_actions(text), [])

    def test_higher_numbered_prompt_is_not_mistaken_for_an_old_one(self) -> None:
        text = "**Next action:** run the checks added by Prompt 10.\n"
        self.assertEqual(stale_next_actions(text), [])

    def test_status_block_value_is_read(self) -> None:
        text = "<!-- STATUS:BEGIN -->\nstage_2_next_prompt: 04\n<!-- STATUS:END -->\n"
        self.assertEqual(status_next_prompt(text), "04")

    def test_real_continuity_set_has_no_stale_next_action(self) -> None:
        files = [
            DOCS / "AI_CONTEXT.md",
            DOCS / "AI_HANDOFF.md",
            DOCS / "PROJECT_PROGRESS.md",
            DOCS / "stage-2" / "00_stage_2_handoff.md",
            DOCS / "stage-2" / "06_stage_2_progress_log.md",
        ]
        status_files = {files[0].name, files[1].name, files[2].name}
        for path in files:
            text = path.read_text(encoding="utf-8", errors="replace")
            with self.subTest(file=path.name):
                self.assertEqual(stale_next_actions(text), [])
                if path.name in status_files:
                    # 2026-11-04 (Prompt 10C): 10C closed, so the live prompt was 11.
                    # 2026-11-04 (Prompt 11A): Prompt 11 split and 11A research
                    # closed, so the live sub-prompt is 11B.
                    # 2026-11-06 (Prompt 11C): the 11C companion closed the whole
                    # Prompt 11 family at the design level, so the live prompt is 12.
                    self.assertEqual(status_next_prompt(text), "12")


class CurrentStateConsistencyTests(unittest.TestCase):
    """Regressions for the 2026-10-24 finalization audit.

    These check *current-state* tables and instructions, not historical prose.
    A labelled history may name an earlier prompt; an unlabelled current table
    may not, and a finished prompt may not be presented as the next task.
    """

    def read(self, *parts: str) -> str:
        return (DOCS.joinpath(*parts)).read_text(encoding="utf-8", errors="replace")

    def current_prompt(self, context: str) -> int:
        value = status_next_prompt(context)
        self.assertIsNotNone(value, "AI_CONTEXT.md has no stage_2_next_prompt value")
        # Prompt 10 is the registered next prompt; the outline's next-prompt
        # row is keyed on the numeric prompt, so compare the leading digits.
        digits = re.match(r"\d{1,2}", value)
        self.assertIsNotNone(digits, f"unparseable stage_2_next_prompt: {value!r}")
        return int(digits.group(0))

    def outline_rows(self) -> dict[str, str]:
        outline = self.read("stage-2", "02_master_game_design_bible_outline.md")
        section = outline[outline.index("## 5. Current state") :]
        rows: dict[str, str] = {}
        for line in section.splitlines():
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] not in {"Item", "---"} and not cells[0].startswith("---"):
                rows[cells[0]] = cells[1]
        return rows

    def test_outline_current_state_matches_the_authoritative_prompts(self) -> None:
        """The outline's §5 table must describe the completed prompts and the next one."""
        context = self.read("AI_CONTEXT.md")
        rows = self.outline_rows()
        current = self.current_prompt(context)

        self.assertIn(
            "09_account_onboarding_nation_creation_and_progression.md",
            rows.get("Authoritative Prompt 03 specification", ""),
        )
        self.assertIn(
            "10_economy_resources_treasury_and_finances.md",
            rows.get("Authoritative Prompt 04 specification", ""),
        )
        self.assertIn(
            "11_cities_infrastructure_production_and_research.md",
            rows.get("Authoritative Prompt 05 specification", ""),
        )
        self.assertIn(f"Prompt {current:02d}", rows.get("Next prompt", ""))
        self.assertRegex(rows.get("Prompts executed", ""), r"01[–-]0?7.*09C")
        self.assertNotIn(f"Prompt {current - 1:02d} —", rows.get("Next prompt", ""))

    def test_outline_section_counts_are_derived_from_the_outline(self) -> None:
        """Planned/drafted/gameplay counts must agree with the actual B-sections."""
        outline = self.read("stage-2", "02_master_game_design_bible_outline.md")
        rows = self.outline_rows()

        planned = len(re.findall(r"^### B-\d{2} ", outline, re.M))
        # 2026-11-03: B-09 is ACCEPTED at the specification/documentation
        # level, so it is still a drafted section but no longer a Draft row.
        drafted = len(
            re.findall(r"^\| Status \| \*\*(?:Draft|ACCEPTED)", outline, re.M)
        )
        blocks = re.split(r"(?=^### B-\d{2} )", outline, flags=re.M)
        gameplay = 0
        for block in blocks:
            doc = re.search(r"^\| Authoritative document \| (.+)$", block, re.M)
            if (
                doc
                and ("**Draft**" in block or "**ACCEPTED" in block)
                and any(
                    name in doc.group(1)
                    for name in ("07_core_gameplay_loop", "09_account_onboarding", "10_economy_resources", "11_cities_infrastructure", "12_population", "15_diplomacy", "16_alliances")
                )
            ):
                gameplay += 1

        self.assertEqual(int(re.search(r"\d+", rows["Sections planned"]).group()), planned)
        self.assertEqual(int(re.search(r"\d+", rows["Sections drafted"]).group()), drafted)
        self.assertEqual(
            int(re.search(r"\d+", rows["Sections with gameplay rules"]).group()), gameplay
        )

    def test_progress_table_records_09b_acceptance_and_completed_09c(self) -> None:
        """Prompt 09 is accepted; 09C is complete at the specification level and Prompt 10A is complete."""
        text = self.read("PROJECT_PROGRESS.md")
        start = text.index("## Stage 2 —")
        header = text.index("| # | Prompt | Status |", start)
        table = text[header : text.index("\n\n", header)]
        rows = re.findall(r"^\| (\d{2}) \| (.+?) \| (.+?) \|$", table, re.M)

        numbers = [number for number, _, _ in rows]
        self.assertEqual(numbers, [f"{i:02d}" for i in range(1, 16)])

        # 2026-11-04: Phase 09B is accepted at the specification/documentation
        # level (D-142 / DD-165); Prompt 09C is complete at the same level,
        # Prompt 10A research is complete, Prompt 10B specification is complete,
        # Prompt 10C is complete at the same level and Prompt 11 is next.
        awaiting = [row for row in rows if "pending independent acceptance" in row[2].lower()]
        self.assertEqual(awaiting, [], "09B has independent acceptance recorded")

        accepted = [row for row in rows if "**accepted" in row[2].lower()]
        self.assertEqual(len(accepted), 1, f"expected one accepted row, got {accepted}")
        self.assertEqual(accepted[0][0], "09")
        self.assertIn("specification/documentation level", accepted[0][2])
        self.assertIn("Prompt 09C: complete at the specification/documentation level", accepted[0][2])
        self.assertIn("Prompt 10A: complete", accepted[0][2])
        self.assertIn("Prompt 10B: complete at the specification/documentation level", accepted[0][2])

        # Completion is documentation-only: no row may present 09C as an
        # implemented, functioning or released system. 2026-11-05 (Prompt 11A):
        # row 11 stops being a bare Pending row because 11A closed at the
        # research/design-foundations level, so only Prompts 12-15 stay Pending.
        self.assertNotRegex(
            "\n".join(row[2] for row in rows).lower(),
            r"prompt 09c[^.\n]{0,80}(?:implemented|functioning|released|deployed)",
        )
        # 2026-11-06 (Prompt 12A): row 12 stops being a bare Pending row because
        # 12A closed at the research/design-foundations level, so only 13-15 stay
        # Pending.
        pending = [row[0] for row in rows if row[2].strip() == "Pending"]
        self.assertEqual(pending, [f"{i:02d}" for i in range(13, 16)])
        row12 = next(row for row in rows if row[0] == "12")
        self.assertIn("12A COMPLETE at the research and design-foundations level", row12[2])
        self.assertIn("Prompt 12B is next, has not started", row12[2])

        row10 = next(row for row in rows if row[0] == "10")
        self.assertIn("10B specification complete", row10[2])
        self.assertIn("Prompt 10C complete", row10[2])
        # 2026-11-06 (Prompt 12A): 12A closed at the research level, so row 10
        # must name 12B as the live sub-prompt instead of presenting 12 as next.
        self.assertIn("Prompt 12B is next", row10[2])

        row11 = next(row for row in rows if row[0] == "11")
        self.assertIn("11A COMPLETE at the research/design-foundations level", row11[2])
        self.assertIn("11C complete at the specification/documentation level", row11[2])
        self.assertIn("Prompt 12B next and not started", row11[2])
        # A research pass must never be described as a written rulebook.
        self.assertIn("b-11 rulebook at the specification level", row11[2].lower())
        self.assertNotRegex(
            row11[2].lower(),
            r"prompt 11a[^.\n]{0,80}(?:implemented|functioning|released|deployed|tested)",
        )

    def test_handoff_keeps_prompt_03_instructions_as_labelled_history(self) -> None:
        """No unlabelled instruction may tell the next AI to begin Prompt 03."""
        handoff = self.read("AI_HANDOFF.md")
        marker = "Historical snapshot — the Prompt 03 brief"
        self.assertIn(marker, handoff)

        current = handoff[: handoff.index(marker)]
        self.assertIn("Prompts 01–06 are complete", current)
        self.assertIn("Prompt 06 is complete", current)
        self.assertIn("09_account_onboarding_nation_creation_and_progression.md", current)
        self.assertIn("10_economy_resources_treasury_and_finances.md", current)
        self.assertIn("11_cities_infrastructure_production_and_research.md", current)
        self.assertNotIn("Before writing it, read:", current)
        self.assertNotIn("Prompt 03 **applies**", current)

        historical = handoff[handoff.index(marker) :]
        self.assertIn("do not execute", historical.lower())
        self.assertIn("Before writing it, read:", historical)
        self.assertIn("Historical snapshot — the Prompt 04 brief", handoff)
        self.assertIn("H.5 Prompt 06B carry-in", handoff)

    def test_market_summary_agrees_with_the_decision_register(self) -> None:
        """An unqualified 'none decided' market claim conflicts with D-016/D-017."""
        decisions = self.read("DECISIONS.md")
        d017 = next((line for line in decisions.splitlines() if line.startswith("| D-017 |")), "")
        self.assertTrue(d017, "DECISIONS.md no longer records D-017")
        d017_confirmed = "Confirmed" in d017 and "Superseded" not in d017

        handoff = self.read("AI_HANDOFF.md")
        market_lines = [line for line in handoff.splitlines() if "Market design questions" in line]
        self.assertTrue(market_lines, "handoff no longer carries the market-question summary")
        summary = "\n".join(market_lines)

        if d017_confirmed:
            self.assertNotRegex(summary.lower(), r"none decided\.?$")
            self.assertIn("D-017", summary)
            self.assertIn("D-016", summary)
            self.assertIn("Still genuinely open", summary)
        else:
            self.assertIn("historical", summary.lower())

        for line in handoff.splitlines():
            if "market" in line.lower() and "none decided" in line.lower():
                self.assertIn("historical", line.lower())




class SubPromptStatusTests(unittest.TestCase):
    """Regressions for the 2026-10-29 status reconciliation.

    Prompt 07 is split into 07A/07B/07C, so the prompt-number detector cannot
    tell 07B from 07C. These tests cover the sub-prompt rule directly and then
    the real continuity set.
    """

    def read(self, *parts: str) -> str:
        return (DOCS.joinpath(*parts)).read_text(encoding="utf-8", errors="replace")

    def test_completed_subprompt_cannot_be_the_next_task(self) -> None:
        text = "**Prompt 07B - market foundations is the next intended task** and has not started."
        found = subprompt_status_problems(text)
        self.assertEqual(len(found), 1, found)
        self.assertIn("07B", found[0])

    def test_next_outstanding_task_prefix_is_caught(self) -> None:
        # The 2026-10-29 handoff said "its next outstanding task is **Prompt
        # 07C ..." — the identifier follows the word "Prompt", which the old
        # prefix pattern did not allow, so the clause escaped every check.
        text = ("For Stage 2 work, its next outstanding task is **Prompt 07C "
                "— market workflows and acceptance** (07A research and 07B "
                "market foundations are complete).")
        found = subprompt_status_problems(text)
        self.assertEqual(len(found), 1, found)
        self.assertIn("07C", found[0])

    def test_next_outstanding_task_prefix_accepts_prompt_08(self) -> None:
        text = "Stage 2's next outstanding task is **Prompt 08 — Diplomacy between nations**."
        self.assertEqual(subprompt_status_problems(text), [])

    def test_completed_subprompt_cannot_be_reported_not_started(self) -> None:
        text = "Prompt 07A research has not started."
        self.assertEqual(len(subprompt_status_problems(text)), 1)

    def test_done_and_successor_next_is_accepted(self) -> None:
        text = ("**Prompt 07C - workflows and acceptance is complete; "
                "Prompt 08 - diplomacy is the next intended task.**")
        self.assertEqual(subprompt_status_problems(text), [])

    def test_labelled_history_is_accepted(self) -> None:
        text = ("*Historical:* at the time, Prompt 07B was the next intended task "
                "and had not started; it is now complete and 07C is next.")
        self.assertEqual(subprompt_status_problems(text), [])

    def test_completed_08a_cannot_be_the_next_task_but_08b_may_be(self) -> None:
        # Prompt 08 is split too: 08A is complete, so naming it as the live next
        # task is the same defect the 07B/07C guard was added for.
        stale = "**Prompt 08A - diplomacy research is the next intended task** and has not started."
        found = subprompt_status_problems(stale)
        self.assertEqual(len(found), 1, found)
        self.assertIn("08A", found[0])
        live_b = ("**Prompt 08A - diplomacy research is complete; "
                  "Prompt 08B - diplomacy foundations is complete; "
                  "Prompt 08C - diplomacy workflows and acceptance is complete; "
                  "Prompt 09 - alliances is the next intended task.**")
        self.assertEqual(subprompt_status_problems(live_b), [])
        # 2026-10-30: 08B is now complete too, so the same rule applies to it.
        stale_b = "**Prompt 08B - diplomacy foundations is the next intended task** and has not started."
        found_b = subprompt_status_problems(stale_b)
        self.assertEqual(len(found_b), 1, found_b)
        self.assertIn("08B", found_b[0])
        live_c = ("**Prompt 08B - diplomacy foundations is complete; "
                  "Prompt 08C - diplomacy workflows and acceptance is complete; "
                  "Prompt 09 - alliances is the next intended task.**")
        self.assertEqual(subprompt_status_problems(live_c), [])
        # 2026-10-30: 08C is now complete too, so naming it as next is stale.
        stale_c = "**Prompt 08C - workflows and acceptance is the next intended task** and has not started."
        found_c = subprompt_status_problems(stale_c)
        self.assertEqual(len(found_c), 1, found_c)
        self.assertIn("08C", found_c[0])

    def test_real_continuity_set_names_08c_complete_and_09_next(self) -> None:
        for name in ("AI_CONTEXT.md", "AI_HANDOFF.md", "PROJECT_PROGRESS.md"):
            text = self.read(name)
            with self.subTest(file=name):
                self.assertIn("08C", text)
                self.assertIn("Prompt 09", text)
                self.assertEqual(subprompt_status_problems(text), [])
        roadmap = self.read("ROADMAP.md")
        self.assertIn("Prompt 09", roadmap)
        self.assertEqual(subprompt_status_problems(roadmap), [])

    def test_completed_10_family_cannot_be_the_next_task_once_10c_closes(self) -> None:
        # 2026-11-03: Prompt 10 is split into 10A research, 10B foundations and
        # 10C workflows; 10A and 10B are complete, so naming either as the live
        # next task is the same defect the 07B/07C and 08A/08B guards cover.
        # 2026-11-04: 10C closed too, so 10C joins the completed set and the
        # same sentence that used to be live must now be flagged; the live case
        # moves to Prompt 11, which the 07–10 sub-prompt rule does not track.
        stale = "**Prompt 10A - warfare research is the next intended task** and has not started."
        found = subprompt_status_problems(stale)
        self.assertEqual(len(found), 1, found)
        self.assertIn("10A", found[0])
        stale_pending = "Prompt 10A research remains pending."
        self.assertEqual(len(subprompt_status_problems(stale_pending)), 1)
        stale_b = ("**Prompt 10A - warfare research is complete; "
                   "Prompt 10B - warfare foundations is the next intended task** "
                   "and has not started.")
        found_b = subprompt_status_problems(stale_b)
        self.assertEqual(len(found_b), 1, found_b)
        self.assertIn("10B", found_b[0])
        stale_b_done = "Prompt 10B is the next intended task."
        self.assertEqual(len(subprompt_status_problems(stale_b_done)), 1)
        closed_c = ("**Prompt 10B - warfare foundations is complete; "
                    "Prompt 10C - warfare workflows and acceptance is the next intended task** "
                    "and has not started.")
        found_c = subprompt_status_problems(closed_c)
        self.assertEqual(len(found_c), 1, found_c)
        self.assertIn("10C", found_c[0])
        live_11 = ("**Prompt 10C - warfare workflows and acceptance is complete; "
                   "Prompt 11 - world events, objectives and rankings is the next intended task** "
                   "and has not started.")
        self.assertEqual(subprompt_status_problems(live_11), [])

    def test_regex_recognises_the_10_family(self) -> None:
        from status_rules import SUBPROMPT
        self.assertEqual(SUBPROMPT.findall("10A 10B 10C 09C 08B 07A"), ["10A", "10B", "10C", "09C", "08B", "07A"])

    def test_regex_recognises_the_11_family(self) -> None:
        # 2026-11-05 (Prompt 11A): Prompt 11 is split into 11A/11B/11C like the
        # 10 family, and the detector's `1[01]` alternative now covers it. Without
        # this, a document could keep calling a closed 11A the live task and no
        # check would notice — the exact defect the 07-10 guards were built for.
        from status_rules import SUBPROMPT
        self.assertEqual(SUBPROMPT.findall("11A 11B 11C 10C 09A"), ["11A", "11B", "11C", "10C", "09A"])

    def test_completed_11a_cannot_be_the_next_task_once_11a_closes(self) -> None:
        # 2026-11-05 (Prompt 11A): 11A research closed at the research/design-
        # foundations level, so 11A joins the completed set and the sentence that
        # was live on 2026-11-04 must now be flagged. The live case is 11B, which
        # is not completed and must pass.
        stale = ("**Prompt 10C - warfare workflows and acceptance is complete; "
                 "Prompt 11A - world events research is the next intended task** "
                 "and has not started.")
        found = subprompt_status_problems(stale)
        self.assertEqual(len(found), 1, found)
        self.assertIn("11A", found[0])
        self.assertEqual(len(subprompt_status_problems("Prompt 11A research remains pending.")), 1)
        self.assertEqual(len(subprompt_status_problems("Prompt 11A is the next intended task.")), 1)
        stale_11b = ("**Prompt 11A - world events, objectives and rankings research is complete; "
                     "Prompt 11B - B-11 foundations is the next intended task** "
                     "and has not started.")
        self.assertEqual(len(subprompt_status_problems(stale_11b)), 1)
        live = ("**Prompt 11B - the B-11 specification is complete; "
                "Prompt 11C - B-11 workflows and acceptance is the next intended task** "
                "and has not started.")
        # 2026-11-06 (Prompt 12A): 11C closed on 2026-11-06 and Prompt 12A closed
        # the same day, so the sentence that was live on 2026-11-05 is now a stale
        # claim and must be flagged, while the genuinely live sub-prompt 12B must
        # not be. The 12 family also had to join the sub-prompt pattern first:
        # before it, "12A" was not a recognised sub-prompt token at all.
        self.assertEqual(len(subprompt_status_problems(live)), 1)
        self.assertEqual(subprompt_status_problems("Prompt 12B is the next intended task."), [])
        self.assertEqual(len(subprompt_status_problems("Prompt 12A is the next intended task.")), 1)
        self.assertEqual(len(subprompt_status_problems("Prompt 11C is the next intended task.")), 1)
        # The current true statement must pass, and the prompt-level "next" claim
        # in the same sentence must not be attributed back to 11C.
        current = ("**Prompt 11C is complete at the specification/documentation level "
                   "and its acceptance verdict is PARTIAL; Prompt 12A is complete; Prompt 12B is next and has not started.**")
        self.assertEqual(subprompt_status_problems(current), [])

class ContinuityAgreementTests(unittest.TestCase):
    """Prompt 11C-C1: status documents must not contradict each other.

    The 11C audit found a roadmap that still said 11C had not started after the
    status blocks said it was complete, and a status model that still named the
    finished prompt as current. These tests pin both directions: a consistent
    record passes, and each contradiction is rejected for its own reason.
    """

    def status_block(self, prompt: str) -> str:
        return (
            "<!-- STATUS:BEGIN -->\n"
            f"stage_2_next_prompt: {prompt}\n"
            "<!-- STATUS:END -->\n"
        )

    def test_11c_is_recorded_complete_and_specification_only(self) -> None:
        self.assertIn("11C", COMPLETED_SUBPROMPTS)
        self.assertIn("11B", COMPLETED_SUBPROMPTS)
        self.assertIn("10C", COMPLETED_SUBPROMPTS)
        record = ("**Prompt 11C is complete at the specification/documentation level; "
                  "its acceptance verdict is PARTIAL; Prompt 12A is complete; Prompt 12B is next and has not started.**")
        self.assertEqual(continuity_problems({"record": record}), [])

    def test_11c_acceptance_is_tracked_separately_from_completion(self) -> None:
        self.assertEqual(PROMPT_ACCEPTANCE.get("11C"), "PARTIAL")
        self.assertEqual(PROMPT_ACCEPTANCE.get("11B"), None)
        # Completion and acceptance are different facts: the record that says
        # "complete at the specification level" must not be rewritten into an
        # acceptance claim, and the acceptance map must still say PARTIAL.
        complete_only = ("**Prompt 11C is complete at the specification/documentation level; "
                         "its acceptance verdict is PARTIAL.**")
        self.assertEqual(continuity_problems({"record": complete_only}), [])
        self.assertNotEqual(PROMPT_ACCEPTANCE["11C"], "ACCEPTED")

    def test_next_scheduled_prompt_is_12b(self) -> None:
        self.assertEqual(NEXT_PROMPT, "12B")
        self.assertEqual(CURRENT_PROMPT, "12B")
        docs = {
            "AI_CONTEXT.md": self.status_block("12B"),
            "AI_HANDOFF.md": self.status_block("12B"),
            "PROJECT_PROGRESS.md": self.status_block("12B"),
        }
        self.assertEqual(continuity_problems(docs), [])

    def test_prompt_14_remains_unstarted(self) -> None:
        started = "Prompt 14 is complete."
        self.assertEqual(len(continuity_problems({"roadmap": started})), 1)
        negated = "Prompt 14 has not started; numerical calibration remains outstanding."
        self.assertEqual(continuity_problems({"roadmap": negated}), [])

    def test_roadmap_cannot_say_11c_has_not_started(self) -> None:
        docs = {
            "stage-2/01_stage_2_prompt_roadmap.md": "Prompt 11C has not started.",
            "PROJECT_PROGRESS.md": "Prompt 11C is complete at the specification/documentation level.",
        }
        problems = continuity_problems(docs)
        self.assertTrue(any("01_stage_2_prompt_roadmap" in p for p in problems), problems)
        self.assertFalse(any(p.startswith("PROJECT_PROGRESS") for p in problems), problems)

    def test_two_status_files_cannot_disagree_on_the_live_prompt(self) -> None:
        docs = {
            "AI_CONTEXT.md": self.status_block("11C"),
            "PROJECT_PROGRESS.md": self.status_block("12B"),
        }
        problems = continuity_problems(docs)
        self.assertTrue(any("11C" in p and "expected '12B'" in p for p in problems), problems)
        self.assertTrue(any("disagree" in p for p in problems), problems)

    def test_specification_complete_is_not_runtime_implemented(self) -> None:
        docs = {"PROJECT_PROGRESS.md": "The B-11 workflow layer is fully implemented and released."}
        problems = continuity_problems(docs)
        self.assertTrue(any("implementation" in p for p in problems), problems)
        honest = ("The B-11 workflow layer is specified at the specification/documentation "
                  "level and is not implemented.")
        self.assertEqual(continuity_problems({"PROJECT_PROGRESS.md": honest}), [])

    def test_negation_only_exempts_the_claim_it_governs(self) -> None:
        negative = "No B-11 control is implemented."
        self.assertEqual(continuity_problems({"PROJECT_PROGRESS.md": negative}), [])
        mixed = "No B-11 control is implemented, but the event layer is implemented."
        problems = continuity_problems({"PROJECT_PROGRESS.md": mixed})
        self.assertTrue(any("implementation" in p for p in problems), problems)

    def test_history_marker_only_exempts_its_own_clause(self) -> None:
        line = "The old plan is superseded. Prompt 11C has not started."
        problems = continuity_problems({"roadmap.md": line})
        self.assertTrue(any("11C" in p for p in problems), problems)
        bracketed = ("(Historical, superseded: Prompt 11B was next.) "
                     "Prompt 11C has not started.")
        problems = continuity_problems({"roadmap.md": bracketed})
        self.assertTrue(any("11C" in p for p in problems), problems)

    def test_owner_reserved_decision_cannot_be_reported_as_approved(self) -> None:
        docs = {"AI_HANDOFF.md": "UD-040 is approved and closed by this pass."}
        problems = continuity_problems(docs)
        self.assertTrue(any("owner-reserved" in p for p in problems), problems)
        still_open = "UD-040, UD-050 and UD-051 remain Open and owner-reserved."
        self.assertEqual(continuity_problems({"AI_HANDOFF.md": still_open}), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
