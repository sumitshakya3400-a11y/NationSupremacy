#!/usr/bin/env python3
"""Read-only QA validator for the Prompt 9 synthesis report.

Checks (document QA only, no game code):
  1. Report exists at the required path; Sections 1-23 present and ordered.
  2. No leftover append sentinel; no duplicate new-family IDs.
  3. New-family counts: REQ 39, ZD 14, GATE 20, DEF 18, OD 12, PV 15, TQ 17.
     (DEF was 15 when Prompt 9 was first written; the report's defect register
     grew to 18 with DEF-016/017/018, which the report and this script both
     assert. Corrected 2026-10-23 — the assertion already expected 18.)
  4. Inherited register counts observed in the owning reports.
  5. Local Markdown links resolve.
  6. DECISIONS.md still holds D-001..D-006 with D-004/D-005 Provisional.
  7. No production code outside docs/qa_backups and the authorised spike
     directory prototypes/ (document-QA scripts allowed). Scoped 2026-10-23
     when Prompt 10 introduced the feasibility prototype; the intent (no game
     or production code in the project) is unchanged.
  8. Continuity files agree on Prompt 9 / Stage 1 / zero-cost / readiness.
  9. Correction-pass assertions: P8 §15.4 says twelve stage-A requirements,
     A8 states the SEC-031 subset, TH-011 separates prevention from residual,
     P8 §26.9 is marked superseded, P7 keeps its 2026-10-23 fixes, and P9
     marks DEF-004/005/010 Fixed with GATE-03 passing (17 pass / 3 conditional).

Counts are asserted against the saved report, not against this docstring: if a
register grows, both the report and the expectation here must change together.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
ROOT = DOCS.parent
REPORT = DOCS / "stage-1" / "09_integrated_design_synthesis_and_readiness_audit.md"

failures: list[str] = []
checks = 0


def check(condition: bool, label: str, detail: str = "") -> None:
    global checks
    checks += 1
    if condition:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}{(' :: ' + detail) if detail else ''}")
        failures.append(label)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def uniq(pattern: str, text: str) -> set[str]:
    return set(re.findall(pattern, text, flags=re.IGNORECASE))


report = read(REPORT)

# 1. Section continuity -------------------------------------------------------
sections = [int(n) for n in re.findall(r"^## Section (\d+) — ", report, flags=re.MULTILINE)]
check(sections == list(range(1, 24)), "Sections 1-23 present and ordered", str(sections))
check("<!--P9-APPEND-->" not in report, "No append sentinel left in report")

# 2/3. New families ----------------------------------------------------------
families = {
    "REQ": (r"\bREQ-\d{3}\b", 39),
    "ZD": (r"\bZD-\d{2}\b", 14),
    "GATE": (r"\bGATE-\d{2}\b", 20),
    "DEF": (r"\bDEF-\d{3}\b", 18),
    "OD": (r"\bOD-\d{2}\b", 12),
    "PV": (r"\bPV-\d{2}\b", 15),
    "TQ": (r"\bTQ-\d{2}\b", 17),
}
for prefix, (pattern, expected) in families.items():
    ids = uniq(pattern, report)
    check(len(ids) == expected, f"{prefix} family has {expected} unique IDs", f"found {len(ids)}: {sorted(ids)}")
    # contiguity
    numbers = sorted(int(re.search(r"\d+", i).group()) for i in ids)  # type: ignore[union-attr]
    check(
        numbers == list(range(1, expected + 1)),
        f"{prefix} IDs are contiguous 1..{expected}",
        str(numbers),
    )

# Every REQ in the §12.2 matrix is unique (the §11.3 feature table also cites REQ-039)
matrix_start = report.index("### 12.2 The matrix")
matrix_end = report.index("### 12.3 Traceability status")
req_rows = re.findall(r"^\| (REQ-\d{3}) \|", report[matrix_start:matrix_end], flags=re.MULTILINE)
check(len(req_rows) == 39 and len(set(req_rows)) == 39, "39 REQ matrix rows, unique", str(len(req_rows)))

# 4. Inherited registers -----------------------------------------------------
p8 = read(DOCS / "stage-1" / "08_security_privacy_fair_play_and_trust.md")
p7 = read(DOCS / "stage-1" / "07_economy_design_and_market_structure.md")
p6 = read(DOCS / "stage-1" / "06_core_gameplay_systems_and_interactions.md")
p5 = read(DOCS / "stage-1" / "05_core_game_concept_and_design_pillars.md")
p4 = read(DOCS / "stage-1" / "04_target_audience_and_player_experience.md")
p3 = read(DOCS / "stage-1" / "03_feature_comparison_opportunity_analysis.md")
p2 = read(DOCS / "stage-1" / "02_strengths_weaknesses_player_frustrations.md")

th = uniq(r"\bTH-\d{3}\b", p8)
sec = uniq(r"\bSEC-\d{3}\b", p8)
st = uniq(r"\bST-\d{3}\b", p8)
osq = uniq(r"\bOSQ-\d{3}\b", p8)
walk = uniq(r"\bW-18-([A-R])\b", p8)
sys_ids = {s.upper() for s in uniq(r"\bSYS-\d{3}\b", p6)}  # P6 §9D has one lowercase 'sys-010'
int_ids = uniq(r"\bINT-\d{3}\b", p6)
sdq = uniq(r"\bSDQ-\d{3}\b", p6)
econ = uniq(r"\bECON-\d{3}\b", p7)
ecv = uniq(r"\bECV-\d{3}\b", p7)
r_ids = uniq(r"\bR-\d{2}\b", p6) | uniq(r"\bR-\d{2}\b", p7)
fo = uniq(r"\bFO-\d{3}\b", p3)
v_ids = uniq(r"\bV-\d{1,2}\b", p4)
cv = uniq(r"\bCV-\d{3}\b", p5)
d_ids = uniq(r"\bD-\d{3}\b", read(DOCS / "DECISIONS.md"))
# F register rows only (the §9 table), not prose mentions: the register note added
# on 2026-10-23 names the unassigned numbers deliberately.
f_ids = {m for m in re.findall(r"^\| (F-\d{3}b?) \|", p2, flags=re.MULTILINE)}
o_ids = uniq(r"\bO-\d{1,2}\b", p2)

sec_defined = {s for s in sec if re.fullmatch(r"SEC-00[1-9]|SEC-0[12]\d|SEC-03[0-3]", s)} - {"SEC-009"}
econ_retired = {"ECON-003", "ECON-004", "ECON-005", "ECON-007", "ECON-008"}
econ_active = econ - econ_retired

check(len(th) == 25, "TH-001..025 (25)", str(len(th)))
check(len(sec_defined) == 32 and "SEC-009" in sec and "SEC-034" not in sec - {"SEC-034"},
      "SEC 32 defined with SEC-009 reserved", f"defined={len(sec_defined)}")
check(len(st) == 20, "ST-001..020 (20)", str(len(st)))
check(len(osq) == 12, "OSQ-001..012 (12)", str(len(osq)))
check(len(walk) == 18, "W-18-A..R (18)", str(len(walk)))
check(len(sys_ids) == 18, "SYS-001..018 (18)", str(len(sys_ids)))
check(len(int_ids) == 14, "INT-001..014 (14)", str(len(int_ids)))
check(len(sdq) == 18, "SDQ-001..018 (18)", str(len(sdq)))
check(len(econ_active) == 18, "ECON 18 active (5 retired)", f"{len(econ_active)} -> {sorted(econ_active)}")
check(all(f"ECV-00{i}" in ecv for i in range(1, 6)), "ECV-001..005 defined (5)", str(sorted(ecv)))
check(len(r_ids) == 21, "R-01..R-21 (21)", str(len(r_ids)))
check(len(fo) == 27, "FO-001..027 (27)", str(len(fo)))
check(len(v_ids) == 10, "V-1..V-10 (10)", str(len(v_ids)))
check(len(cv) == 6, "CV-001..006 (6)", str(len(cv)))
check(len(d_ids) == 6, "D-001..D-006 (6)", str(len(d_ids)))
check(
    len(f_ids) == 28 and "F-007" not in f_ids and "F-028" not in f_ids and "F-003b" in f_ids,
    "F register 28 rows; F-007/F-028 unassigned; F-003b present",
    f"{len(f_ids)} -> {sorted(f_ids)}",
)
check(len(o_ids) == 12, "O register 12 entries (O-1..O-12)", str(len(o_ids)))

# 5. Local links -------------------------------------------------------------
missing = []
for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", report):
    if target.startswith(("http://", "https://", "mailto:", "#")):
        continue
    clean = target.split("#", 1)[0]
    if not clean:
        continue
    if not (REPORT.parent / clean).resolve().exists():
        missing.append(target)
check(not missing, "All local Markdown links resolve", str(missing[:8]))

# 6. Decision log ------------------------------------------------------------
decisions = read(DOCS / "DECISIONS.md")
check("| D-004 |" in decisions and "Provisional" in decisions, "D-004 present and Provisional")
check("| D-005 |" in decisions and "Provisional" in decisions, "D-005 present and Provisional")
check("Operations Points" in decisions and "Cloudflare Workers + D1" in decisions,
      "D-004/D-005 decision text intact")
check("| D-007 |" not in decisions, "No unapproved decision was added")

# 7. No production code outside the document set and authorised prototype -----
allowed_suffixes = {".py"}
code_suffixes = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".go", ".rs", ".java", ".cs", ".php", ".rb"}
EXEMPT_PARTS = {"prototypes", "node_modules", "dist", ".wrangler"}
offenders = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if set(path.parts) & EXEMPT_PARTS:
        continue
    if path.suffix.lower() in code_suffixes:
        offenders.append(str(path.relative_to(ROOT)))
    if path.suffix.lower() in allowed_suffixes and "qa_backups" not in path.parts:
        offenders.append(str(path.relative_to(ROOT)))
check(not offenders, "No production code outside docs/qa_backups and prototypes/", str(offenders))

# 8. Continuity agreement ----------------------------------------------------
ctx = read(DOCS / "AI_CONTEXT.md")
hand = read(DOCS / "AI_HANDOFF.md")
prog = read(DOCS / "PROJECT_PROGRESS.md")
continuity_blob = "\n".join([ctx, hand, prog])
check("Prompt 9" in ctx and "complete" in ctx.lower(), "AI_CONTEXT mentions Prompt 9 completion")
check("Prompt 9" in hand, "AI_HANDOFF mentions Prompt 9")
check("| 9 |" in prog and "Prompt 9" in prog, "PROJECT_PROGRESS has a row 9")
check("conditionally ready" in report.lower() and "conditionally ready" in continuity_blob.lower(),
      "Readiness verdict repeated in continuity files")
check("not complete" in report.lower() and "not complete" in continuity_blob.lower(),
      "Stage 1 not complete stated in report and continuity")
check("₹0" in report and "₹0" in ctx, "Zero-cost objective present in report and AI_CONTEXT")
check("D-004" in hand and "Provisional" in hand, "AI_HANDOFF preserves D-004 status")

# 9. Correction-pass assertions (2026-10-23) ---------------------------------
check(re.search(r"\*\*Version:\*\* v1\.1", p8) is not None, "P8 header is v1.1")
p8_154 = p8[p8.index("### 15.4 Which protections"):p8.index("## 16. Security requirements")]
check("16 requirements on stage A" not in p8_154 and "Twelve requirements" in p8_154, "P8 §15.4 has no live 16-count claim")
check("**Twelve requirements**" in p8, "P8 §15.4 states twelve stage-A requirements")
check("12 full requirements (SEC-010/011" in p8, "P8 §17.1 states the exact stage-A count")
check("subset of SEC-031" in p8, "P8 A8 states the SEC-031 subset")
check("PL (money/pipeline spine rows required at A8" in p8, "P8 §16.2 SEC-031 stage cell clarified")
check("**Stage-A prevention:**" in p8 and "Residual (accepted)" in p8, "P8 TH-011 prevention/residual explicit")
check("superseded" in p8, "P8 §26.9 handoff marked superseded")
check(len(re.findall(r"\*\*Fixed 2026-10-23\*\*", report)) >= 3, "P9 marks DEF-004/005/010 Fixed")
check(re.search(r"\| \*\*Pass\*\* \| \*\*17\*\*", report) is not None, "P9 gate tally is 17 pass")
check(re.search(r"\| \*\*Conditional\*\* \| \*\*3\*\*", report) is not None, "P9 gate tally is 3 conditional")
check(re.search(r"GATE-03[^\n]*\| \*\*Pass\*\*", report) is not None, "P9 GATE-03 is Pass")
check("validate_final.py" in report and "re-purposed" in report.lower(), "P9 records the legacy validator's re-purposing")
check("Version:** 1.2" in p7 and "2026-10-23" in p7, "P7 header is v1.2 with the correction date")
p7_15 = p7[p7.index("## 15. The finance interface"):p7.index("## 16. Storage")]
check("interest on reserve" not in p7_15, "P7 §15 has no reserve-interest label")
check("DEF-018" in p7 and "Open conflict" in p7, "P7 records the offer-reservation conflict")
check("**18**" in report and "| **DEF** | 18 |" in report, "P9 DEF register is 18")
check("| **Total** | **135** |" in report, "P9 appendix total is 135")

# 10. Report-level hygiene ---------------------------------------------------
check(re.search(r"no production (game )?code", report, re.IGNORECASE) is not None,
      "Report states no production code")
check("not a guarantee" in report.lower() or "no guarantee" in report.lower(),
      "Report avoids an unlimited-free guarantee")
check(report.count("Conditionally ready") >= 1, "Report states the readiness verdict")

print()
print(f"{checks - len(failures)}/{checks} checks passed")
if failures:
    print("FAILURES:")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("ALL CHECKS PASSED")
