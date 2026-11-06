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
  5. Local Markdown links resolve.   6. DECISIONS.md holds D-001..D-030 contiguously:
      D-004 keeps its original text and is Superseded by D-015, D-005
      Superseded by D-008, D-007/D-008 the owner-approved name and provider
      direction, D-009/D-010 the Pages address and the dedicated project,
      D-014 the autonomous decision policy.
      (Updated 2026-10-23 for Prompt 10.1: the old guard asserted that no D-007
      existed, which was correct only while nothing was approved. Updated again
      for Prompt 10.2 when two more owner instructions were recorded. Updated
      once more after the 2026-10-23 decision pass: the guard now asserts the
      supersession instead of the superseded "D-004 still Provisional" state,
      so it keeps detecting silent edits to D-004's text. The decision-closure
      audit added D-024..D-029; the range and the count assertions moved with
      them.)
  7. No production code outside docs/qa_backups and the authorised spike
     directory prototypes/ (document-QA scripts allowed). Scoped 2026-10-23
     when Prompt 10 introduced the feasibility prototype; the intent (no game
     or production code in the project) is unchanged.
  8. Continuity files agree on Prompt 9 / Stage 1 / zero-cost / readiness.
  9. Correction-pass assertions: P8 §15.4 says twelve stage-A requirements,
     A8 states the SEC-031 subset, TH-011 separates prevention from residual,
     P8 §26.9 is marked superseded, P7 keeps its 2026-10-23 fixes, and P9
     marks DEF-004/005/010 Fixed with GATE-03 passing (17 pass / 3 conditional).
 10. Stage 2's current next action: the STATUS blocks say 05, the index row,
     the handoff §H/§10 and the progress-log header name Prompt 05, and no
     current-action sentence still directs the reader to an earlier prompt.
     The bounded rule lives in `status_rules.py`; its regression tests are in
     `test_next_action.py`. Labelled history stays legal.
 11. Stage 2 Prompt 02's B-02 specification: 31 sections in order, TR-001..097
     contiguous, the mapless world and 2-hour lattice present, the P0-P7 phases
     published, D-004 superseded by D-015 (the model approved, values
     provisional), and the outline links it as Draft.
 12. The decision-closure audit (stage-2/08): six new decisions D-024..D-029,
     the resolved UD-004/015/016/025/027/028, the separated policy/proof status,
     and the absence of any claim that CF-02/CF-04 or the Stage 3 measurement
     has passed.

Counts are asserted against the saved report, not against this docstring: if a
register grows, both the report and the expectation here must change together.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # keep the repo free of __pycache__
# A failing check may quote a label containing "₹" or another non-ASCII glyph.
# Without this, Windows' legacy console encoding aborts the validator instead of
# printing the failure, which is exactly when a readable result matters most.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_rules import stale_next_actions  # noqa: E402  (document-QA helper)

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
# Row-start extraction, not every mention: decision text cites other decisions
# ("Superseded by D-015"), so a mention scan would both duplicate and reorder
# the IDs. The log is a table; its rows define the range.
d_ids = re.findall(r"^\| (D-\d{3}) ", read(DOCS / "DECISIONS.md"), re.M)
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
d_last = int(d_ids[-1][2:]) if d_ids else 0
check(d_ids == [f"D-{i:03d}" for i in range(1, d_last + 1)],
      f"D-001..D-{d_last:03d} contiguous, no gap or duplicate", str(len(d_ids)))
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
d004_row = next((ln for ln in decisions.splitlines() if ln.startswith("| D-004 |")), "")
# D-004 keeps its original text (history) and points to the superseding entry.
check("| D-004 |" in decisions and 'Keep "Operations Points" as a provisional' in d004_row,
      "D-004 present with its original decision text intact")
check("Superseded by D-015" in d004_row, "D-004 is marked superseded by D-015, not deleted")
d015_row = next((ln for ln in decisions.splitlines() if ln.startswith("| D-015 |")), "")
check("Operations Points" in d015_row and "Confirmed" in d015_row,
      "D-015 approves the Operations Points model")
check("cap" in d015_row.lower() and "provisional" in d015_row.lower(),
      "D-015 keeps the Operations Points values provisional")
check("| D-005 |" in decisions and "Superseded by D-008" in decisions,
      "D-005 present and marked superseded, not deleted")
check("Operations Points" in decisions and "Cloudflare Workers + D1" in decisions,
      "D-004/D-005 decision text intact")
d007_row = next((ln for ln in decisions.splitlines() if ln.startswith("| D-007 |")), "")
d008_row = next((ln for ln in decisions.splitlines() if ln.startswith("| D-008 |")), "")
check("Nation Supremacy" in d007_row and "Confirmed" in d007_row,
      "D-007 records Nation Supremacy as the confirmed public name")
check("Supabase" in d008_row and "Cloudflare" in d008_row and "Confirmed" in d008_row,
      "D-008 records the Cloudflare + Supabase direction as confirmed")

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
check("Superseded by D-015" in hand and "D-015" in hand,
      "AI_HANDOFF records D-004's supersession by D-015")

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

# 11. Prompt 10.1 state ------------------------------------------------------
r11 = read(DOCS / "stage-1" / "11_free_tier_feasibility_results.md")
check("Nation Supremacy" in r11 and "nation-supremacy.nationsphere.workers.dev" in r11,
      "Report 11 records the official name and the deployed URL")
check("## 14. Corrections to v1.0" in r11 and "## 15. Supabase" in r11,
      "Report 11 carries the correction register and the Supabase results")
check("10:00:00Z" in r11 and "pg_cron" in r11,
      "Report 11 records the product pg_cron boundary firing")
check("Superseded by D-008" in decisions, "D-005 supersession is recorded")
check("Nation Supremacy" in ctx and "Supabase" in ctx,
      "AI_CONTEXT carries the official name and the selected backend")

# 12. Prompt 10.2 state ------------------------------------------------------
r12 = read(DOCS / "stage-1" / "12_nation_supremacy_deployment_and_resource_separation.md")
check("https://nation-supremacy.pages.dev" in r12, "Report 12 records the live Pages address")
check("lqdzchtfxrbtwsrpkrzo" in r12, "Report 12 records the dedicated project reference")
check("paused" in r12.lower() and "not deleted" in r12.lower(),
      "Report 12 states the legacy project is paused, not deleted")
check("| D-009 |" in decisions and "| D-010 |" in decisions,
      "D-009/D-010 recorded in the decision log")
for label, blob in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog)):
    check("nation-supremacy.pages.dev" in blob, f"{label} carries the current Pages address")

# 13. Stage 1 closure (final Prompt, 2026-10-23) ------------------------------
# The historical verdicts above stay asserted in Report 9; the continuity files
# must now carry the closed state and the Stage 2 authorization.
r13 = read(DOCS / "stage-1" / "13_stage_1_final_closure_and_stage_2_handoff.md")
s2 = read(DOCS / "stage-2" / "00_stage_2_handoff.md")
check("STAGE 1 CLOSED" in r13, "Report 13 records the closure decision")
check("CF-01" in r13 and "CF-09" in r13, "Report 13 records the carry-forward backlog")
check("owner-confirmed" in r13.lower(), "Report 13 records the deletions as owner-confirmed")
check("Stage 2" in s2 and "OD-02" in s2, "Stage 2 handoff names the first task")
check("| D-011 |" in decisions and "CLOSED" in decisions,
      "D-011 records the closure in the decision log")
for label, blob in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog)):
    check("Stage 2" in blob, f"{label} records the Stage 2 authorization")

# 14. Roadmap alignment and the Stage 2 register (2026-10-23, D-012) -------
# The owner restored the original stage numbering: Stage 2 is the Master Game
# Design Bible. Historical reports keep their own work-package numbers; these
# checks only guard the current-state files against drifting back.
roadmap = read(DOCS / "ROADMAP.md")
reg = read(DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md")
check("Master Game Design Bible" in roadmap, "ROADMAP names Stage 2 as the Master Game Design Bible")
for stage in range(0, 8):
    check(re.search(r"\| \*\*" + str(stage) + r"\*\* \|", roadmap) is not None,
          f"ROADMAP lists official stage {stage}")
check("pre-evidenced" in roadmap and ("Re-running the completed experiments" in roadmap or "not repeated" in roadmap),
      "ROADMAP states Stage 3 reuses the existing hosting evidence")
check("Stage 5" in roadmap and "Application architecture and database" in roadmap,
      "ROADMAP assigns the architecture/schema work to Stage 5")

headings = re.findall(r"### Prompt (\d{2}[AB]?) —", reg)
nums = sorted({h[:2] for h in headings})
check(nums == [f"{i:02d}" for i in range(1, 16)] and "06A" in headings and "06B" in headings,
      "Stage 2 register carries all 15 prompts in order, with Prompt 06 split into 06A/06B", str(headings))
check("Bounded completion rule" in reg and "must not do" in reg.lower(),
      "Stage 2 register states its boundaries and completion rule")
check("Prompt 06" in s2 and "Master Game Design Bible" in s2,
      "Stage 2 handoff names Prompt 06 and the Bible mission")
check("official Stage 5" in s2 or "official stage" in s2.lower(),
      "Stage 2 handoff re-points the architecture work to a later official stage")
for label, blob in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog)):
    check("Master Game Design Bible" in blob, f"{label} records Stage 2 as the Master Game Design Bible")
    check("Prompt 06" in blob, f"{label} names Stage 2 Prompt 06 as the next activity")
    check(not re.search(r"Stage 1 (is|remains) (still )?(incomplete|not complete)", blob),
          f"{label} carries no stale open Stage 1 status")
check("ROADMAP.md" in decisions and "| D-012 |" in decisions,
      "D-012 records the official roadmap alignment")
check("Revision 1.1" in r13 and "roadmap alignment" in r13,
      "Report 13 carries the roadmap-alignment revision note")
check("Stage 2" in r13 and "Master Game Design Bible" in r13,
      "Report 13 describes Stage 2 as the Master Game Design Bible")

# 15. Structured current status (2026-10-23 micro-correction) -----------------
# Phrase presence is not enough: three files can each contain the right words
# and still contradict each other. Each continuity file carries one STATUS block
# between these markers, and the values must agree.
STATUS_KEYS = [
    "status_updated", "stage_1", "stage_2", "stage_2_next_prompt", "roadmap",
    "legacy_worker", "legacy_supabase_project", "operations_points", "decisions_range",
]


def status_block(text: str, name: str) -> dict[str, str]:
    blocks = re.findall(r"<!-- STATUS:BEGIN -->(.*?)<!-- STATUS:END -->", text, re.S)
    if len(blocks) != 1:
        failures.append(f"{name}: expected exactly one STATUS block, found {len(blocks)}")
        checks_ref[0] += 1
        return {}
    out = {}
    for line in blocks[0].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    checks_ref[0] += 1
    if all(k in out for k in STATUS_KEYS):
        print(f"PASS  {name} carries a complete STATUS block")
    for k in STATUS_KEYS:
        if k not in out:
            failures.append(f"{name}: STATUS block missing '{k}'")
            checks_ref[0] += 1
    return out


checks_ref = [0]
status = {n: status_block(t, n) for n, t in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog))}
blocks = [b for b in status.values() if b]
if blocks:
    for key in STATUS_KEYS:
        vals = {b.get(key) for b in blocks}
        checks_ref[0] += 1
        if len(vals) == 1:
            print(f"PASS  STATUS '{key}' agrees across the three files")
        else:
            failures.append(f"STATUS '{key}' disagrees across files: {sorted(x for x in vals if x)}")
    one = blocks[0]
    checks_ref[0] += 1
    if one.get("stage_1") == "CLOSED":
        print("PASS  STATUS: Stage 1 CLOSED")
    else:
        failures.append(f"STATUS: stage_1 is {one.get('stage_1')!r}, expected CLOSED")
    checks_ref[0] += 1
    if one.get("stage_2") == "IN PROGRESS" and one.get("stage_2_next_prompt") == "12B":
        print("PASS  STATUS: Stage 2 IN PROGRESS, next prompt 12B")
    else:
        failures.append(f"STATUS: Stage 2 state is {one.get('stage_2')!r} / prompt {one.get('stage_2_next_prompt')!r}")
    if "deleted" in (one.get("legacy_worker", "") + one.get("legacy_supabase_project", "")) and \
            "owner-confirmed" in (one.get("legacy_worker", "") + one.get("legacy_supabase_project", "")):
        checks_ref[0] += 1
        print("PASS  STATUS: legacy resources recorded as deleted (owner-confirmed)")
    else:
        checks_ref[0] += 1
        failures.append("STATUS: legacy deletions not recorded as owner-confirmed")
    checks_ref[0] += 1
    op = one.get("operations_points", "")
    if op.startswith("Approved") and "provisional" in op.lower() and "D-015" in op:
        print("PASS  STATUS: Operations Points model approved (D-015), values provisional")
    else:
        failures.append(f"STATUS: Operations Points state is {op!r}")
    # decisions_range must match the log itself.
    m = re.search(r"D-(\d{3})\.\.D-(\d{3})", one.get("decisions_range", ""))
    checks_ref[0] += 1
    if m and m.group(2) == f"{d_last:03d}" and m.group(1) == "001":
        print(f"PASS  STATUS: decisions_range matches the {len(d_ids)} logged decisions")
    else:
        failures.append(f"STATUS: decisions_range {one.get('decisions_range')!r} vs {len(d_ids)} decision IDs")

checks += checks_ref[0]

# 15b. The decision log keeps history and points forward ---------------------
d013 = next((ln for ln in decisions.splitlines() if ln.startswith("| D-013 |")), "")
check(bool(d013) and "owner-confirmed" in d013.lower() and "not" in d013.lower(),
      "D-013 records the deletion as owner-confirmed, not independently verified")
d010 = next((ln for ln in decisions.splitlines() if ln.startswith("| D-010 |")), "")
check("paused now" in d010 and "Superseded by D-013" in d010,
      "D-010 keeps its historical wording and points to D-013")
check("| D-011 |" in decisions and "CLOSED" in decisions, "D-011 remains the closure record")
check("| D-012 |" in decisions and "Master Game Design Bible" in decisions,
      "D-012 remains the roadmap decision")

# 15c. Stale current-state wording must not return ---------------------------
stale = {
    "Stage 1 (research stage)": "AI_CONTEXT still opens on the old stage label",
    "paused pending manual deletion": "a continuity file still says the legacy project awaits deletion",
    "remain the outstanding Stage 1 work": "a continuity file still calls the gates outstanding Stage 1 work",
    "currently holds six entries": "AI_HANDOFF still reports six decisions",
    "paused rather than deleted": "AI_HANDOFF still says the legacy project is merely paused",
    "Deleting the old project is still outstanding": "a continuity file still lists the deletion as pending",
}
for phrase, why in stale.items():
    for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog)):
        check(phrase.lower() not in text.lower(), f"{name}: stale current-status wording absent", phrase)

# 15c-2. The handoff's decision count must match the log ---------------------
WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}
WORDS["twenty-one"] = 21
WORDS["twenty-two"] = 22
WORDS["twenty-three"] = 23
WORDS["twenty-nine"] = 29
WORDS["thirty"] = 30
WORDS["forty-two"] = 42
WORDS["fifty-one"] = 51
WORDS["sixty-five"] = 65
WORDS["eighty"] = 80
WORDS["ninety"] = 90
WORDS["ninety-one"] = 91
WORDS["one hundred and five"] = 105
WORDS["one hundred and eight"] = 108
WORDS["one hundred and twenty-one"] = 121
WORDS["one hundred and twenty-two"] = 122
WORDS["one hundred and thirty-two"] = 132
WORDS["one hundred and thirty-four"] = 134
WORDS["one hundred and thirty-nine"] = 139
WORDS["one hundred and forty"] = 140
WORDS["one hundred and forty-one"] = 141
WORDS["one hundred and forty-two"] = 142
WORDS["one hundred and forty-three"] = 143
WORDS["one hundred and fifty-one"] = 151
WORDS["one hundred and sixty-one"] = 161
WORDS["one hundred and sixty-two"] = 162
WORDS["one hundred and seventy-seven"] = 177
m = re.search(r"holds \*\*([\w -]+?)\*\* entries", hand)
check(bool(m) and WORDS.get(m.group(1).lower()) == len(d_ids),
      "AI_HANDOFF decision count matches the log",
      f"said {(m.group(1) if m else 'nothing')!r}, log has {len(d_ids)}")

# 15e. Prompt 01 deliverables (2026-10-23) ------------------------------------
# Stage 2's structural frame: outline, 60 requirements, 41 design decisions,
# 24 unresolved questions, progress log. Presence alone is not enough — the
# registers must be internally consistent enough to be usable.
outline = read(DOCS / "stage-2" / "02_master_game_design_bible_outline.md")
trace = read(DOCS / "stage-2" / "03_requirements_traceability.md")
dd = read(DOCS / "stage-2" / "04_approved_and_provisional_decisions.md")
ud = read(DOCS / "stage-2" / "05_unresolved_design_decisions.md")
log = read(DOCS / "stage-2" / "06_stage_2_progress_log.md")

b_ids = re.findall(r"^### (B-\d{2}) — ", outline, re.M)
check(b_ids == [f"B-{i:02d}" for i in range(1, 20)], "Bible outline carries B-01..B-19 in order", str(b_ids))
check("22_master_game_design_bible.md" in outline, "outline names the planned Bible entry point")
check("no gameplay rules" in outline.lower() or "No gameplay rules" in outline,
      "outline states it contains no gameplay rules")

req_ids = re.findall(r"^\| (REQ-\d{3}) ", trace, re.M)
check(req_ids == [f"REQ-{i:03d}" for i in range(1, 764)], "tracker carries REQ-001..REQ-763 in order", str(len(req_ids)))
req_rows = [ln for ln in trace.splitlines() if re.match(r"\| REQ-\d{3} \|", ln)]
unprompted = [ln[:10] for ln in req_rows if not re.search(r"\| (?:0[2-9]|1[0-5])[ABC]? \||\| all \|", ln)]
check(not unprompted, "every requirement is assigned to a Stage 2 prompt", "; ".join(unprompted[:5]))
check("mapless" in trace.lower() and "one account per person" in trace.lower(),
      "tracker carries the mapless-world and one-account requirements")
check("with an **executed** validation | **0**" in trace or "executed** validation | **0**" in trace,
      "tracker states that zero validations have been executed")

dd_rows = re.findall(r"^\| (DD-\d{3}) \|", dd, re.M)
check(dd_rows == [f"DD-{i:03d}" for i in range(1, 226)], "design register carries DD-001..DD-225", str(len(dd_rows)))
dd019 = next((ln for ln in dd.splitlines() if ln.startswith("| DD-019 |")), "")
dd033 = next((ln for ln in dd.splitlines() if ln.startswith("| DD-033 |")), "")
check("Superseded by DD-033" in dd019 and "Approved" in dd033 and "values Provisional" in dd033,
      "Operations Points model approved by DD-033 with provisional values; DD-019 kept as history")
check("D-004" in dd and "| D-013 |" in dd, "design register reconciles D-004 and D-013")

ud_ids = re.findall(r"^\| (UD-\d{3}) \|", ud, re.M)
check(ud_ids == [f"UD-{i:03d}" for i in range(1, 61)], "unresolved register carries UD-001..UD-060", str(len(ud_ids)))
ud_rows = [ln for ln in ud.splitlines() if ln.startswith("| UD-")]
unclassed = [ln[:10] for ln in ud_rows if not re.search(r"\| [ABCDE][^|]*\|", ln)]
check(not unclassed, "every unresolved item has a blocking class", "; ".join(unclassed[:5]))
check("UD-002" in ud and "DEF-018" in ud, "the request-reservation conflict is carried as UD-002")

check("| 01 |" in log and "**Complete**" in log, "progress log marks Prompt 01 complete")
def log_status(prompt):
    """The status cell of one row in the Stage 2 prompt table."""
    for line in log.splitlines():
        if line.startswith(f"| {prompt} |"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            return cells[3] if len(cells) >= 4 else ""
    return ""


# The 2026-10-28 micro-correction completed 06B. The old assertion accepted the
# stale table (06B "next") because it only required the two labels to appear;
# these checks read the status cell, so a summary that disagrees with its own
# table now fails here.
check("**Complete**" in log_status("06A"), "progress log marks Prompt 06A complete", log_status("06A"))
check("**Complete**" in log_status("06B"), "progress log marks Prompt 06B complete", log_status("06B"))
check("**Complete**" in log_status("07"), "progress log marks Prompt 07 complete", log_status("07"))
# 2026-11-03: Prompt 08 is complete; 09 is accepted through 09C; 10A research
# is complete. 2026-11-05 (Prompt 11A): 11A research closes at the
# research/design-foundations level, so row 11 is no longer a bare Pending row
# and only 12–15 stay pending.
# 2026-11-06 (Prompt 12A): row 12 is no longer a bare Pending row, so only
# 13–15 stay pending.
check(log.count("| Pending |") == 3, "progress log keeps Prompts 13-15 pending", str(log.count("| Pending |")))
check(all(k in next((ln for ln in log.splitlines() if ln.startswith("| 08 |")), "")
          for k in ("**08A complete**", "**08B complete**", "**08C complete**")),
      "progress log row 08 records 08A, 08B and 08C complete", "row 08")
check("**ACCEPTED" in log_status("09")
      and "Prompt 09C: complete at the specification/documentation level" in log_status("09")
      and "Prompt 10A: complete" in log_status("09")
      and "Prompt 10B: complete at the specification/documentation level" in log_status("09"),
      "progress log row 09 records Phase 09B accepted, 09C complete, 10A complete and 10B complete", log_status("09"))
check("10B specification complete" in log_status("10")
      and "Prompt 10C complete" in log_status("10")
      and "Prompt 12B next" in log_status("10"),
      "progress log row 10 records 10B complete, 10C complete and Prompt 12B next", log_status("10"))
# 2026-11-07 (Prompt 12A review remediation): read row 12 itself, not just the
# pending count, so a row that silently regresses to "Pending" or to 12A-live
# fails here even though the count of bare Pending rows is unchanged. The
# status cell must *begin* with the 12A completion text, so a cell that names
# some other state first cannot borrow 12A's completion from later in the cell.
status12 = log_status("12").replace("**", "")
check(status12.startswith("12A complete at the research/design-foundations level")
      and "12B next and not started" in status12,
      "progress log row 12 records 12A complete and 12B next", log_status("12"))

# 15f. The *current* next action (2026-10-23 micro-correction) ----------------
# Section 14 proves Prompt 02 is mentioned somewhere. This section proves no
# current-action sentence still sends the reader to Prompt 01; labelled history
# is allowed (see qa_backups/status_rules.py for the bounded rule).
for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog),
                   ("stage-2/00", s2), ("stage-2/06", log)):
    stale = stale_next_actions(text)
    check(not stale, f"{name}: no current next-action statement points to an earlier prompt",
          " | ".join(stale))

ctx_handoff_row = next((ln for ln in ctx.splitlines() if "stage-2/00_stage_2_handoff.md" in ln), "")
check("Prompt 06" in ctx_handoff_row and "next action = Prompt 05" not in ctx_handoff_row,
      "AI_CONTEXT index row describes the Stage 2 handoff's current next action")

hand_h = hand[hand.index("## H. Next authorized task"):hand.index("## I. Instructions")]
check("Prompt 10C" in hand_h and not stale_next_actions(hand_h),
      "AI_HANDOFF §H names Prompt 10C as the next task")
s2_next = s2[s2.index("## 10. Next action"):s2.index("## 11. House rules")]
check("Prompt 10C" in s2_next and not stale_next_actions(s2_next),
      "Stage 2 handoff §10 names Prompt 10C as the next action")
log_next = log[:log.index("## 1.")] if "## 1." in log else log[:1200]
check("Prompt 10C" in log_next, "Stage 2 progress log header names Prompt 10C")

# 15g. Prompt 02 specification (2026-10-23) ----------------------------------
spec = read(DOCS / "stage-2" / "07_core_gameplay_loop_symbolic_world_and_turn_system.md")
spec_sections = [int(n) for n in re.findall(r"^## (\d+)\. ", spec, re.M)]
check(spec_sections == list(range(1, 32)), "B-02 carries 31 sections in order", str(spec_sections))
tr_ids = sorted({int(n) for n in re.findall(r"\bTR-(\d{3})\b", spec)})
check(tr_ids == list(range(1, 98)), "B-02 rules TR-001..TR-097 are contiguous", f"{len(tr_ids)} ids")
check("7200" in spec and "two-hour utc" in spec.lower(), "B-02 keeps the two-hour UTC lattice")
check("mapless" in spec.lower() and "no coordinates" in spec.lower(),
      "B-02 keeps the mapless, coordinate-free world")
check(all(f"P{i}" in spec for i in range(8)) and "published ordering catalogue" in spec.lower(),
      "B-02 publishes the P0-P7 phases and the ordering catalogue")
check("no attendance mechanic" in spec.lower() and "absence" in spec.lower(),
      "B-02 keeps the no-presence rule")
check("D-015" in spec and "model approved" in spec.lower() and "no global action-point currency" in spec,
      "B-02 carries the approved Operations Points model and invents no general action currency")
check("D-004 → D-015" in spec and "Superseded by D-015" in decisions,
      "B-02 and DECISIONS agree on the D-004 supersession")
check("UD-003" in spec and "Resolved" in spec, "B-02 records the UD-003 resolution")
# 2026-10-23 follow-up: D-019 settled the P3 order, but B-02 still asked Prompt 04
# to decide it. These two checks keep a decided question from reading as open.
check("UD-030" in spec and "Resolved by D-019" in spec,
      "B-02 records the UD-030 resolution (income before upkeep)")
check("Whether production precedes upkeep (UD-030)" not in spec,
      "B-02 no longer asks Prompt 04 to re-decide UD-030")
b02 = outline[outline.index("### B-02"):outline.index("### B-03")]
check("07_core_gameplay_loop_symbolic_world_and_turn_system.md" in b02 and "**Draft**" in b02,
      "outline links B-02 to its specification as Draft")
check("| DD-021 |" in dd and "| DD-032 |" in dd, "design register carries the Prompt 02 positions")
ud003 = next((ln for ln in ud.splitlines() if ln.startswith("| UD-003 |")), "")
check("Resolved" in ud003, "UD-003 is marked resolved")
ud004 = next((ln for ln in ud.splitlines() if ln.startswith("| UD-004 |")), "")
check("Resolved" in ud004 and "D-026" in ud004,
      "UD-004 records the retention decision (D-026)")

# 15h. Decision-closure audit (2026-10-23) -------------------------------------
# Seven new decisions and seven resolved UD rows, plus the policy/proof separation.
for did, token in (("D-024", "No shared general action budget"),
                   ("D-025", "no provider-managed backups"),
                   ("D-026", "hot for 30 days"),
                   ("D-027", "at least 5 contributing members"),
                   ("D-028", "dormant after 14 consecutive days"),
                   ("D-029", "verified e-mail before nation creation"),
                   ("D-030", "visible to its **named counterparty**")):
    check(f"| {did} |" in decisions and token.lower() in decisions.lower(),
          f"{did} is recorded with its selected rule")
for uid, did in (("UD-004", "D-026"), ("UD-015", "D-029"), ("UD-016", "D-025"),
                 ("UD-025", "D-028"), ("UD-027", "D-027"), ("UD-028", "D-025"),
                 ("UD-029", "D-030")):
    row = next((ln for ln in ud.splitlines() if ln.startswith(f"| {uid} |")), "")
    check("Resolved" in row and did in row, f"{uid} is resolved and cites {did}", row[:120])
ud016 = next((ln for ln in ud.splitlines() if ln.startswith("| UD-016 |")), "")
check("CF-02" in ud016 and ("Awaiting validation" in ud016 or "drill" in ud016),
      "UD-016 separates the decided policy from the unexecuted CF-02 drill")

# The audit record must exist, carry its required sections, and never claim the
# unexecuted proofs. These checks guard the exact failure the audit found: a
# policy decision being reported as a passed test.
audit = read(DOCS / "stage-2" / "08_final_decision_closure_audit.md")
for heading in ("## 1. Audit scope and method", "## 2. Complete inventory",
                "## 3. Decisions resolved", "## 4. Every unresolved ID",
                "## 5. Remaining provisional and open items", "## 6. Future-stage work",
                "## 7. Contradictions corrected", "## 8. Accepted risks",
                "## 9. Research record", "## 10. Validation record", "## 11. Readiness"):
    check(heading in audit, f"audit carries '{heading[3:]}'")
check("CF-02" in audit and "not executed" in audit.lower(),
      "audit records CF-02 as unexecuted")
check("CF-04" in audit and "no smtp provider" in audit.lower(),
      "audit records the e-mail flow as unexecuted")
check("No Prompt 03 deliverable exists yet" in audit
      and "Dated note (2026-10-24, after this audit)" in audit
      and "09_account_onboarding_nation_creation_and_progression.md" in audit,
      "audit keeps its 2026-10-23 snapshot and carries a dated note that Prompt 03 was written later")

# 15i. FO-018 / D-021 agreement -----------------------------------------------
# The Stage 1 reports keep their historical "FO-018 open" wording; the current
# continuity files may not call the launch decision owner-held.
for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog)):
    check("FO-018 (catch-up) stays owner-held" not in text,
          f"{name}: FO-018 is not described as owner-held")
    check("FO-018 catch-up decision itself remains owner-held" not in text,
          f"{name}: the old FO-018 handoff sentence is absent")
check("D-021" in decisions and "No catch-up acceleration at launch" in decisions,
      "D-021 remains the record of the launch posture")
check("FO-018 is no longer owner-held" in hand or "D-021" in hand,
      "AI_HANDOFF points FO-018 at D-021")

# 15j. Register counts asserted from the files, not prose ----------------------
req_status = {}
for ln in req_rows:
    cell = ln.split("|")[4].strip() if len(ln.split("|")) > 4 else ""
    key = "Approved" if "Approved" in cell else ("Provisional" if "Provisional" in cell else ("Proposed" if "Proposed" in cell else ("Open" if "Open" in cell else ("Deferred" if "Deferred" in cell else "?"))))
    req_status[key] = req_status.get(key, 0) + 1
check(req_status.get("Approved") == 55 and req_status.get("Provisional") == 688 and req_status.get("Proposed", 0) == 0
      and req_status.get("Open") == 19 and req_status.get("Deferred") == 1,
      "requirements are 55 approved / 688 provisional / 19 open / 1 deferred / 0 proposed", str(req_status))
check("executed** validation | **0**" in trace,
      "requirements register still states zero executed validations")

# 15k. Cross-register status and architecture guards -------------------------
# 1/3. A resolved UD must not reappear as an active row in §6. UD-016 was the
# exact conflict: its row said Open while §6 said the policy was decided.
ud6 = ud[ud.index("## 6."):] if "## 6." in ud else ""
for uid in ("UD-004", "UD-015", "UD-016", "UD-025", "UD-027", "UD-028", "UD-029"):
    check(f"| `{uid}` |" not in ud6 and f"| {uid} |" not in ud6,
          f"{uid} is not still listed as an active item in §6")
# 4. D-004 must stay superseded in both registers, with its history intact.
d004 = next((ln for ln in dd.splitlines() if ln.startswith("| D-004 |")), "")
check("Superseded by D-015" in d004,
      "the design register keeps D-004 superseded by D-015")
for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand), ("PROJECT_PROGRESS", prog)):
    check("D-004 remains Provisional" not in text and "D-004 is Provisional" not in text,
          f"{name}: no current text says D-004 is provisional")

# 6. The AI_CONTEXT index must describe the current registers, not a past one.
ctx_04 = next((ln for ln in ctx.splitlines() if "stage-2/04_approved" in ln), "")
ctx_03 = next((ln for ln in ctx.splitlines() if "stage-2/03_requirements" in ln), "")
ctx_07 = next((ln for ln in ctx.splitlines() if "stage-2/07_core" in ln), "")
check(("DD-001" in ctx_04 and "DD-209" in ctx_04) and ("D-001" in ctx_04 and "D-161" in ctx_04),
      "AI_CONTEXT row 04 describes the current 151 decisions / 199 positions")
check("688 provisional" in ctx_03 and "19 open" in ctx_03 and "55 approved" in ctx_03 and "1 deferred" in ctx_03,
      "AI_CONTEXT row 03 describes the current requirement counts")
check("97 rules" in ctx_07 and "v1.5" in ctx_07,
      "AI_CONTEXT row 07 describes the current B-02 version")
check("not yet written" not in ctx_07.lower() and "unwritten" not in ctx_07.lower(),
      "AI_CONTEXT does not call the completed B-02 specification unwritten")

# 9. The fixed architecture may not drift provider in the current documents.
for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand),
                   ("stage-2/00", s2), ("B-02", spec)):
    low = text.lower()
    check("cloudflare" in low and "supabase" in low, f"{name}: names Cloudflare and Supabase")
    check("vercel" not in low and "netlify" not in low and "firebase" not in low,
          f"{name}: does not name a replacement provider")

# 10. A design decision is not an executed test. No current file may claim the
# backup drill or the auth flow passed because D-025/D-029 decided the policy.
for name, text in (("audit", audit), ("AI_HANDOFF", hand), ("stage-2/06", log)):
    low = text.lower()
    check(not re.search(r"cf-0[24][^\n]{0,30}\b(passed|complete)\b", low),
          f"{name}: does not claim CF-02/CF-04 passed")
    check("no backup exists" in low or "not executed" in low or "unexecuted" in low,
          f"{name}: records the unexecuted drill/auth proof")
check("No backup has been taken" in audit and "No SMTP provider has been selected" in audit,
      "audit states plainly that no backup was taken and no SMTP provider was selected")
check("historical — superseded by §5.1d" in log and "at Prompt 02" in log,
      "progress log labels its superseded register counts as historical")

# 15l. Status consistency across the decision registers ----------------------
# Failure class 1/3/8: a decision resolved in one authoritative file must not
# remain active in another, and no ID may be duplicated or renumbered. The UD
# register is checked both row-by-row and against its own §6 active inventory.
ud_rows = {}
for ln in ud.splitlines():
    m = re.match(r"\| (UD-\d{3}) \|", ln)
    if m:
        ud_rows[m.group(1)] = ln
resolved_ud = [
    "UD-001", "UD-002", "UD-003", "UD-004", "UD-008", "UD-010", "UD-011",
    "UD-014", "UD-015", "UD-016", "UD-018", "UD-019", "UD-020", "UD-021",
    "UD-025", "UD-027", "UD-028", "UD-029", "UD-030",
    "UD-009", "UD-034", "UD-035", "UD-013", "UD-033",
    "UD-012", "UD-039", "UD-032", "UD-024",
]
deferred_ud = {"UD-022": "13", "UD-023": "13",
               "UD-031": "12"}
open_ud = ["UD-005", "UD-006", "UD-007", "UD-017", "UD-026", "UD-036",
           "UD-037", "UD-038", "UD-040", "UD-041", "UD-042", "UD-043", "UD-044", "UD-045", "UD-046", "UD-047", "UD-048", "UD-049", "UD-050", "UD-051",
           "UD-052", "UD-053", "UD-054", "UD-055", "UD-056", "UD-057", "UD-058", "UD-059", "UD-060"]
non_resolved_ud = sorted(list(deferred_ud) + open_ud)
check(sorted(ud_rows) == [f"UD-{i:03d}" for i in range(1, 61)],
      "unresolved rows are UD-001..UD-060 with no duplicate", str(len(ud_rows)))
def ud_status(row: str) -> str:
    """Return the Status cell only; 'Resolved by D-019' elsewhere is history."""
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    return cells[8] if len(cells) >= 9 else ""

for uid in resolved_ud:
    check(ud_status(ud_rows.get(uid, "")).startswith("**Resolved"),
          f"{uid} is marked Resolved in its Status cell")
for uid, prompt in deferred_ud.items():
    status = ud_status(ud_rows.get(uid, ""))
    check(status.startswith(f"**Deferred to Prompt {prompt}**"),
          f"{uid} is deferred to Prompt {prompt} in its Status cell")
for uid in open_ud:
    status = ud_status(ud_rows.get(uid, ""))
    check(status.startswith("Open") and "Resolved" not in status,
          f"{uid} is genuinely Open in its Status cell")
ud6_rows = re.findall(r"^\| `?(UD-\d{3})`? \|", ud6, re.M)
check(ud6_rows == non_resolved_ud,
      "§6 inventory matches the 4 deferred + 18 open rows exactly", str(ud6_rows))
check("**28 Resolved**" in ud and "**3 Deferred to a future prompt**" in ud
      and "**29 Open**" in ud,
      "the UD register states the reconciling 28/3/29 counts")

# Every D-024..D-030 row must be Confirmed in DECISIONS and present in 04;
# the superseded pair must keep pointing at its successor in both registers.
for did in [f"D-{i:03d}" for i in range(24, 31)]:
    drow = next((ln for ln in decisions.splitlines() if ln.startswith(f"| {did} |")), "")
    ddrow = next((ln for ln in dd.splitlines() if ln.startswith(f"| {did} |")), "")
    check("Confirmed" in drow and ddrow, f"{did} is Confirmed and summarised in the design register")
for did, successor in (("D-004", "D-015"), ("D-005", "D-008")):
    drow = next((ln for ln in decisions.splitlines() if ln.startswith(f"| {did} |")), "")
    ddrow = next((ln for ln in dd.splitlines() if ln.startswith(f"| {did} |")), "")
    check(f"Superseded by {successor}" in drow and successor in ddrow,
          f"{did} keeps its {successor} supersession in both registers")
check("D-030" in audit and "Seven decisions" in audit
      and "D-001…D-030" in audit and "DD-001…DD-048" in audit,
      "audit inventory reflects the seven decisions and 30/48 register sizes")

# Current decision-range statements must not stop at D-029. A dated historical
# snapshot is allowed to describe the earlier range; current state pages are not.
for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hand),
                   ("PROJECT_PROGRESS", prog), ("stage-2/00", s2),
                   ("stage-2/05", ud), ("stage-2/08", audit)):
    check("D-001…D-029" not in text and "D-001..D-029" not in text,
          f"{name}: no current decision range stops at D-029")
    low = text.lower()
    check("fifteen design decisions" not in low and "sixteen pending" not in low
          and "twenty-nine entries" not in low,
          f"{name}: no stale 15/16/29 decision-count summary")
# Backup policy must describe the official three-part export, not a single
# default dump that the CLI reference says omits data and custom roles.
for name, text in (("DECISIONS", decisions), ("audit", audit), ("stage-2/04", dd)):
    low = text.lower()
    check("--role-only" in low and "--data-only" in low,
          f"{name}: backup policy names the role-only and data-only exports")
    check(("no data" in low or "no table data" in low) and "custom roles" in low,
          f"{name}: backup policy records the default dump's omissions")
check("`supabase db dump` — roles, schema, data" not in decisions
      and "`supabase db dump` — roles, schema, data" not in audit,
      "no current document describes one dump as roles+schema+data")

status_counts = {"Resolved": 0, "Deferred": 0, "Open": 0}
for row in ud_rows.values():
    cell = ud_status(row)
    if cell.startswith("**Resolved"):
        status_counts["Resolved"] += 1
    elif cell.startswith("**Deferred"):
        status_counts["Deferred"] += 1
    elif cell.startswith("Open"):
        status_counts["Open"] += 1
check(status_counts == {"Resolved": 28, "Deferred": 3, "Open": 29},
      "UD status cells reconcile 28 Resolved / 3 Deferred / 29 Open", str(status_counts))


# 15d. Historical records stay historical, not "corrected" -------------------
# Report 9 is a pre-closure snapshot; its verdict must survive for the record.
check("Stage 1 is not complete" in report, "Report 9 keeps its historical pre-closure verdict")
check("Historical snapshot" in report, "Report 9 is labelled as a historical snapshot")
check("STAGE 1 CLOSED" in r13.upper(), "Report 13 keeps the closure decision")

print()
print(f"{checks - len(failures)}/{checks} checks passed")
if failures:
    print("FAILURES:")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("ALL CHECKS PASSED")
