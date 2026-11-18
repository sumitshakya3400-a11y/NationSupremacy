"""Prompt 14B-C1-R1-R1 — end-to-end adversarial mutation tests.

Each case:
  1. starts from a temporary copy of the real `docs` repository;
  2. runs the production validator and requires exit 0;
  3. applies one mutation to a real document in the fixture;
  4. runs the same production validator and requires a nonzero exit with the
     intended diagnostic;
  5. restores the clean fixture and requires exit 0 again.

Run from `docs/`:

    python qa_backups/14B_R1_R1_mutation_tests.py
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOCS = Path(__file__).resolve().parent.parent
VALIDATOR_REL = Path("qa_backups") / "14B_C1_validate_closeout.py"
QA_REL = Path("stage-2") / "22_numerical_baseline_qa_report.md"
INV_REL = Path("stage-2") / "22_numerical_parameter_inventory.md"
R1_REL = Path("stage-2") / "27_prompt_14B-C1-R1_closeout_report.md"

# (id, file, original, mutated, expected diagnostic substrings, mode)
CASES = [
    ("M01", QA_REL, "`ECN-214`", "`ECN-999`", ("X5", "ECN-999"), "replace"),
    ("M02", QA_REL, "`F-EC-001`", "`F-EC-999`", ("X5", "F-EC-999"), "replace"),
    ("M03", QA_REL, "`F-WR-036`", "`F-WR-999`", ("X5", "F-WR-999"), "replace"),
    ("M04", INV_REL, "| D-063 | D-063 confirms the bundle structure",
     "| D-999 | D-063 confirms the bundle structure", ("A19", "D-999"), "replace"),
    ("M05", R1_REL, "[22_numerical_baseline_qa_report.md](22_numerical_baseline_qa_report.md)",
     "[22_numerical_baseline_qa_report.md](22_nonexistent_qa.md)", ("22_nonexistent_qa.md",), "replace"),
    ("M06", QA_REL, "14B §4.1", "14B §99.9", ("X4", "§99.9"), "replace"),
    ("M07", QA_REL, "`14B_verify_b04_economy.py`", "`14B_nonexistent_economy.py`",
     ("14B_nonexistent_economy.py",), "replace"),
    ("M08", INV_REL, "| D-063 | D-063 confirms the bundle structure",
     "| D-004 | D-063 confirms the bundle structure", ("A20", "D-004"), "replace"),
    ("M09", INV_REL, "| D-046 (recipe structure) |", "|  |", ("A14", "§3.3"), "replace"),
    ("M10", INV_REL, "| Prompt 14 calibration; B-04 structure owner | D-063 |",
     "| Prompt 14 calibration; B-04 structure owner; owner-approved constraint | D-063 |",
     ("A21", "owner-approved"), "replace"),
    ("M11", QA_REL,
     "Standard 150; 100,000 people 300; 600 bp hunger 282; full starvation 105",
     "playtest completed", ("X11", "playtest completed"), "replace"),
    ("M12", INV_REL, "| **C** |", "| **E** |", ("A11", "category is valid"), "replace"),
    ("M13", INV_REL, "| **C** |", "| PROVISIONAL VALUE |", ("A12",), "replace"),
    ("M14", INV_REL, "| B-04 §3.1 · Treasury |", "| B-04 §3.1 · NP-EC-001 Treasury |", ("A8", "NP-EC-001"), "replace"),
    ("M15", QA_REL, "| 1 | Tax and income | B-04 rulebook; B-04 register |", "", ("C2",), "duplicate"),
]


def run_validator(fixture: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(fixture / VALIDATOR_REL)],
        cwd=str(fixture),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def diagnostic(out: str) -> str:
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    for line in lines:
        if line.startswith("- "):
            return line[2:]
    return lines[-1] if lines else ""


def apply_case(fixture: Path, rel: Path, original: str, mutated: str, mode: str):
    path = fixture / rel
    text = path.read_text(encoding="utf-8")
    if original not in text:
        raise RuntimeError(f"mutation target not found in {rel}: {original[:60]!r}")
    if mode == "duplicate":
        idx = text.find(original)
        end = text.find("\n", idx)
        line = text[idx:end]
        new_text = text[:end + 1] + line + "\n" + text[end + 1:]
    else:
        new_text = text.replace(original, mutated, 1)
    path.write_text(new_text, encoding="utf-8")


def restore(fixture: Path, rel: Path, original_text: str):
    (fixture / rel).write_text(original_text, encoding="utf-8")


def resolver_positive_controls(validator_path: Path) -> list[tuple[str, bool]]:
    spec = importlib.util.spec_from_file_location("c1_validator", validator_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    decisions = (DOCS / "DECISIONS.md").read_text(encoding="utf-8")
    spec_text = (DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md").read_text(encoding="utf-8")
    reg_text = (DOCS / "stage-2" / "10_economic_formula_and_balance_register.md").read_text(encoding="utf-8")
    report_text = (DOCS / "stage-2" / "25_prompt_14B_b04_economy_completion_report.md").read_text(encoding="utf-8")
    return [
        ("valid decision D-063 resolves", mod.decision_exists("D-063", decisions)),
        ("invalid decision D-999 rejected", not mod.decision_exists("D-999", decisions)),
        ("D-004 is superseded", mod.decision_is_superseded("D-004", decisions)),
        ("D-063 is not superseded", not mod.decision_is_superseded("D-063", decisions)),
        ("valid B-04 section resolves", mod.has_section(spec_text, "13")),
        ("invalid B-04 section rejected", not mod.has_section(spec_text, "99")),
        ("valid register section resolves", mod.has_section(reg_text, "3.2")),
        ("invalid register section rejected", not mod.has_section(reg_text, "99.9")),
        ("valid report section resolves", mod.has_section(report_text, "4.1")),
        ("invalid report section rejected", not mod.has_section(report_text, "99.9")),
        ("ECN range expands", mod.expand_ids("ECN-119–ECN-121", "ECN") == {"ECN-119", "ECN-120", "ECN-121"}),
        ("delegated Category B wording accepted",
         mod.authority_wording_ok("Category B confirmed under delegated D-014 authority; not owner approval")),
        ("owner-approved wording rejected", not mod.authority_wording_ok("owner-approved constraint")),
        ("planned playtest wording accepted", mod.evidence_wording_ok("value confirmation requires the playtest")),
        ("completed playtest wording rejected", not mod.evidence_wording_ok("playtest completed")),
        ("category C is distinct from a status", mod.category_distinct("C", "PROVISIONAL VALUE")),
        ("status copied into category rejected", not mod.category_distinct("PROVISIONAL VALUE", "PROVISIONAL VALUE")),
        ("valid local link resolves", mod.check_local_link("22_numerical_baseline_qa_report.md")),
        ("missing local link rejected", not mod.check_local_link("22_nonexistent_qa.md")),
        ("superseded reference labelled historical is acceptable",
         mod.decision_is_superseded("D-004", decisions) and bool(__import__("re").search(r"SUPERSEDED", "D-004 (SUPERSEDED)"))),
    ]


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="ns_14B_R1_R1_mutation_"))
    fixture = tmp / "docs"
    shutil.copytree(DOCS, fixture)
    results = []
    try:
        baseline_code, baseline_out = run_validator(fixture)
        print(f"BASELINE: exit={baseline_code} | {diagnostic(baseline_out) or 'no output'}")
        if baseline_code != 0:
            print("FAIL: the clean fixture does not pass; mutation results would be meaningless")
            return 1

        for cid, rel, original, mutated, expected, mode in CASES:
            original_text = (fixture / rel).read_text(encoding="utf-8")
            apply_case(fixture, rel, original, mutated, mode)
            code, out = run_validator(fixture)
            diag = diagnostic(out)
            ok = code != 0 and all(token in out for token in expected)
            restore(fixture, rel, original_text)
            restore_code, restore_out = run_validator(fixture)
            restore_ok = restore_code == 0
            results.append((cid, rel.as_posix(), original, mutated, code, diag, ok and restore_ok, restore_ok))
            print(f"{cid} exit={code} reject={'PASS' if ok else 'FAIL'} restore={'PASS' if restore_ok else 'FAIL'} | {diag[:160]}")

        controls = resolver_positive_controls(DOCS / VALIDATOR_REL)
        control_pass = all(ok for _label, ok in controls)
        for label, ok in controls:
            print(f"CTRL {'PASS' if ok else 'FAIL'} | {label}")

        rejected = sum(1 for r in results if r[6])
        print(f"SUMMARY: {rejected}/{len(results)} mutations rejected and restored; "
              f"{sum(1 for r in results if r[7])}/{len(results)} restores passed; "
              f"resolver controls {'PASS' if control_pass else 'FAIL'}")
        return 0 if rejected == len(results) and control_pass else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
