#!/usr/bin/env python3
"""Prompt 07C checks: workflows, traceability, gates and continuity.

What this proves
----------------
* Every MKT rule in B-07 appears exactly once in the 07C acceptance matrix,
  and every test the matrix cites is defined in the catalogue.
* The three corrected B-07 semantics are present: E1's single crown payment,
  the one space predicate (reservations never added back) and the asymmetric
  ratio band (never described as a symmetric +/-30% interval).
* D-122 / DD-136 / REQ-513 record Global Trade as mandatory product scope,
  while G-1..G-6 keep their statuses and no summary calls the market released.
* The current-status files agree that 07C is complete and Prompt 09 is next.

What this does NOT prove
------------------------
No runtime market exists. These are document and traceability checks; the
matrix is a test design, not executed evidence. No gate is passed here.

Usage
-----
    python qa_backups/verify_market_workflows.py
    python qa_backups/verify_market_workflows.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
B07 = DOCS / "stage-2" / "13_trade_and_markets.md"
COMPANION = DOCS / "stage-2" / "14_market_workflows_and_acceptance.md"
DEC = DOCS / "DECISIONS.md"
DD = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
REQ = DOCS / "stage-2" / "03_requirements_traceability.md"
ROADMAP = DOCS / "ROADMAP.md"
HANDOFF = DOCS / "AI_HANDOFF.md"
CONTEXT = DOCS / "AI_CONTEXT.md"
PROGRESS = DOCS / "PROJECT_PROGRESS.md"
S2_HANDOFF = DOCS / "stage-2" / "00_stage_2_handoff.md"
S2_REGISTER = DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md"
LOG = DOCS / "stage-2" / "06_stage_2_progress_log.md"

sys.path.insert(0, str(DOCS / "qa_backups"))
from status_rules import subprompt_status_problems  # noqa: E402

PASS: list[str] = []
FAIL: list[str] = []


def check(name: str, condition: bool, detail: object = "") -> bool:
    if condition:
        PASS.append(name)
    else:
        FAIL.append(f"{name} :: {detail}")
    return bool(condition)


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rule_ids(text: str) -> list[str]:
    return re.findall(r"^\*\*(MKT-\d{3}[a-z]*) —", text, re.M)


def matrix_rows(text: str) -> list[tuple[str, list[str]]]:
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\| `(MKT-\d{3}[a-z]*)` \|(.*)\|$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        tests = re.findall(r"\bT-[DGSXPOF]\d{2}\b", cells[2] if len(cells) >= 3 else "")
        rows.append((m.group(1), tests))
    return rows


def catalogue_ids(text: str) -> set[str]:
    return set(re.findall(r"^\| (T-[DGSXPOF]\d{2}) \|", text, re.M))


def matrix_problems(rules: list[str], rows: list[tuple[str, list[str]]],
                    defined: set[str]) -> list[str]:
    problems = []
    seen = [r[0] for r in rows]
    if len(seen) != len(set(seen)):
        problems.append("duplicate rule rows")
    missing = [r for r in rules if r not in set(seen)]
    if missing:
        problems.append(f"unmapped rules: {missing[:4]}")
    unknown = [r for r in seen if r not in set(rules)]
    if unknown:
        problems.append(f"unknown rules: {unknown[:4]}")
    bad_tests = [t for _, ts in rows for t in ts if t not in defined]
    if bad_tests:
        problems.append(f"undefined tests: {sorted(set(bad_tests))[:4]}")
    used = {t for _, ts in rows for t in ts}
    unused = sorted(defined - used)
    if unused:
        problems.append(f"unused tests: {unused[:4]}")
    if any(not ts for _, ts in rows):
        problems.append("row with no test")
    return problems


def e1_problems(text: str) -> list[str]:
    rows = [
        "| Aurelia | `TRADE_SELL` | `0` | `−100 food` |",
        "| Aurelia | `TRADE_BUY` | `−200` | `+50 steel` |",
        "| Borealis | `TRADE_SELL` | `+200` | `−50 steel` |",
        "| Borealis | `TRADE_BUY` | `0` | `+100 food` |",
    ]
    problems = [f"missing {r}" for r in rows if r not in text]
    if "| Aurelia | `TRADE_SELL` | `+200` |" in text:
        problems.append("the double-counted +200 Aurelia sale is back")
    if "A single payment must never be entered with both signs" not in text:
        problems.append("missing the single-payment rule")
    return problems


def space_problems(text: str) -> list[str]:
    problems = []
    for phrase in ("free space plus", "free warehouse space plus",
                   "free space plus its existing", "plus existing space reservations"):
        if phrase in text:
            problems.append(f"adds reservations back: {phrase!r}")
    if "W − total_inventory − space_reserved" not in text:
        problems.append("canonical predicate missing")
    if "No rule may add `space_reserved` back" not in text:
        problems.append("missing the no-add-back warning")
    return problems


def band_problems(text: str) -> list[str]:
    problems = []
    if "symmetric ratio" in text:
        problems.append("'symmetric ratio' still present")
    if "not symmetric in percentage terms" not in text:
        problems.append("asymmetry statement missing")
    if "| 70 | 100 | 91 |" not in text:
        problems.append("discount boundary missing")
    if "within ±30%" not in text:
        problems.append("explicit prohibition of 'within ±30%' missing")
    return problems


def gate_problems(b07: str, companion: str) -> list[str]:
    rows = re.findall(r"^\| \*\*G-(\d)\*\* \|(.*)\|\s*$", b07, re.M)
    problems = []
    if len(rows) != 6:
        problems.append(f"expected 6 gates, found {len(rows)}")
    statuses = [r[1] for r in rows]
    if sum("NOT MET" in s for s in statuses) != 5:
        problems.append("not five NOT MET gates")
    if sum("PARTIAL" in s for s in statuses) != 1:
        problems.append("not one PARTIAL gate")
    for n in range(1, 7):
        if f"**G-{n}**" not in companion and f"### G-{n} —" not in companion:
            problems.append(f"companion does not plan G-{n}")
    return problems


def approval_problems(dec: str, dd: str, req: str, companion: str) -> list[str]:
    problems = []
    if "| D-122 |" not in dec:
        problems.append("D-122 missing")
    elif "mandatory" not in dec.lower():
        problems.append("D-122 does not say mandatory")
    if "| DD-136 |" not in dd:
        problems.append("DD-136 missing")
    if "| REQ-513 |" not in req:
        problems.append("REQ-513 missing")
    if "feature approval, not release approval" not in companion:
        problems.append("companion does not separate approval from release")
    return problems


def continuity_problems(texts: dict[str, str]) -> list[str]:
    problems = []
    for name in ("ROADMAP", "AI_HANDOFF", "AI_CONTEXT", "PROJECT_PROGRESS", "stage-2/00"):
        text = texts[name]
        if "Prompt 09" not in text:
            problems.append(f"{name}: Prompt 09 is not named as next")
        if "07C" not in text:
            problems.append(f"{name}: 07C not recorded")
        for snippet in subprompt_status_problems(text):
            problems.append(f"{name}: completed sub-prompt still live :: {snippet}")
    if ("Prompts 01–08 complete" not in texts["ROADMAP"]
            and "Prompt 08 complete" not in texts["ROADMAP"]
            and "Prompt 08 is complete" not in texts["ROADMAP"]):
        problems.append("ROADMAP does not record Prompt 08 complete")
    if "PASS — ACCEPTED" not in texts["companion"]:
        problems.append("companion does not record the acceptance verdict")
    return problems


def self_test() -> int:
    rules = ["MKT-001", "MKT-002"]
    rows = [("MKT-001", ["T-S01"]), ("MKT-002", ["T-S01"])]
    defined = {"T-S01"}
    guards = [
        ("matrix accepts a complete mapping", lambda: matrix_problems(rules, rows, defined) == []),
        ("matrix catches a missing rule", lambda: matrix_problems(rules, rows[:1], defined) != []),
        ("matrix catches a duplicate rule", lambda: matrix_problems(rules, rows + [rows[0]], defined) != []),
        ("matrix catches an undefined test", lambda: matrix_problems(rules, [("MKT-001", ["T-Z99"]), rows[1]], defined) != []),
        ("matrix catches an unused test", lambda: matrix_problems(rules, rows, defined | {"T-Z98"}) != []),
        ("E1 catches the old double-counted sale", lambda: e1_problems("| Aurelia | `TRADE_SELL` | `+200` | `−100 food` |\nA single payment must never be entered with both signs") != []),
        ("space catches 'free space plus'", lambda: space_problems("checks free space plus existing reservations") != []),
        ("band catches 'symmetric ratio'", lambda: band_problems("A symmetric ratio; | 70 | 100 | 91 |; not symmetric in percentage terms; within ±30%") != []),
    ]
    failed = 0
    for name, guard in guards:
        try:
            ok = bool(guard())
        except Exception as exc:  # noqa: BLE001
            ok = False
            name = f"{name} (raised {exc})"
        print(f"SELFTEST {'PASS' if ok else 'FAIL'}  {name}")
        failed += 0 if ok else 1
    print(f"\nSELFTEST: {len(guards) - failed}/{len(guards)} guards detected their defect")
    return 0 if failed == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    for path in (B07, COMPANION, DEC, DD, REQ, ROADMAP, HANDOFF, CONTEXT, PROGRESS):
        if not path.exists():
            FAIL.append(f"missing {path}")
    if FAIL:
        for item in FAIL:
            print("FAIL ", item)
        return 1

    b07 = rd(B07)
    companion = rd(COMPANION)
    rules = rule_ids(b07)
    rows = matrix_rows(companion)
    defined = catalogue_ids(companion)

    check("B-07 has 237 unique MKT rules", len(rules) == 237 and len(set(rules)) == 237, len(rules))
    check("acceptance matrix has 237 rows", len(rows) == 237, len(rows))
    for problem in matrix_problems(rules, rows, defined):
        check("matrix consistency", False, problem)
    if not matrix_problems(rules, rows, defined):
        check("matrix consistency", True)
    check("catalogue defines 83 tests", len(defined) == 83, len(defined))

    for problem in e1_problems(b07):
        check("E1 ledger", False, problem)
    if not e1_problems(b07):
        check("E1 ledger", True)
    for problem in space_problems(b07):
        check("space predicate", False, problem)
    if not space_problems(b07):
        check("space predicate", True)
    for problem in band_problems(b07):
        check("fair-value wording", False, problem)
    if not band_problems(b07):
        check("fair-value wording", True)
    for problem in gate_problems(b07, companion):
        check("release gates", False, problem)
    if not gate_problems(b07, companion):
        check("release gates", True)
    for problem in approval_problems(rd(DEC), rd(DD), rd(REQ), companion):
        check("product approval", False, problem)
    if not approval_problems(rd(DEC), rd(DD), rd(REQ), companion):
        check("product approval", True)

    texts = {
        "ROADMAP": rd(ROADMAP),
        "AI_HANDOFF": rd(HANDOFF),
        "AI_CONTEXT": rd(CONTEXT),
        "PROJECT_PROGRESS": rd(PROGRESS),
        "stage-2/00": rd(S2_HANDOFF),
        "companion": companion,
    }
    for problem in continuity_problems(texts):
        check("continuity", False, problem)
    if not continuity_problems(texts):
        check("continuity", True)

    check("companion is registered in the Stage 2 roadmap", "14_market_workflows" in rd(S2_REGISTER))
    check("B-07 links the companion", "14_market_workflows_and_acceptance.md" in b07)
    check("progress log names 07C", "07C" in rd(LOG))
    check("no market release claim", "Global Trade is implemented" not in companion
          and "Global Trade is released" not in companion
          and "Global Trade is live" not in companion)

    print(f"Prompt 07C workflow/traceability checks: {len(PASS)} passed, {len(FAIL)} failed")
    for item in FAIL:
        print("FAIL ", item)
    if FAIL:
        print("\n07C VALIDATION: FAILED")
        return 1
    for item in PASS:
        print("PASS ", item)
    print("\n07C VALIDATION: ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
