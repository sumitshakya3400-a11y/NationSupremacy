#!/usr/bin/env python3
"""Current cross-file validator for the Project X Stage 1 document set.

History: this started as a point-in-time checker written at the end of the
Prompt 8 correction pass. Its original assertions expected Prompt 9 to be
"not started" and no 09 report to exist, so it reported four stale failures
once the owner authorized and executed Prompt 9. On 2026-10-23 it was
re-purposed: the stale expectations were replaced with the actual nine-prompt
executed-sequence state, and the valid checks were retained unchanged.

It validates documents only. It is not a game test, not a security test, and
not evidence that any proposed control works.

Scope note (2026-10-23, Prompt 10): the "no production code" assertion used to
mean "no code exists anywhere in the project". Prompt 10 authorises a bounded,
labelled feasibility spike, so the assertion now means what it was for: no code
in the research deliverables or at the project root. Only
`prototypes/` (with its dependencies and build output) is exempt, and the
prototype contains no gameplay code.

Run from anywhere: paths resolve relative to this file.
"""

from __future__ import annotations

import glob
import os
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
ROOT = DOCS.parent

fail: list[str] = []


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


ctx = rd(DOCS / "AI_CONTEXT.md")
hnd = rd(DOCS / "AI_HANDOFF.md")
prog = rd(DOCS / "PROJECT_PROGRESS.md")
r8 = rd(DOCS / "stage-1" / "08_security_privacy_fair_play_and_trust.md")
r9 = rd(DOCS / "stage-1" / "09_integrated_design_synthesis_and_readiness_audit.md")
dec = rd(DOCS / "DECISIONS.md")

# 1. Headers updated ---------------------------------------------------------
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)]:
    head = "\n".join(text.splitlines()[:4])
    if "2026-10-23" not in head:
        fail.append(f"{name}: header not dated 2026-10-23")

# 2. Current status language -------------------------------------------------
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)]:
    required = [
        (r"Prompt 9", "prompt-9 mention"),
        (r"Prompt 9[^.\n]{0,120}(complete|executed|delivered)", "prompt-9 completed"),
        (r"Stage 1 is[^.]{0,10}not complete|Stage 1 is incomplete|Stage 1 NOT complete", "stage-1-incomplete"),
        (r"nine[- ]prompt|9 prompts|Prompt 9", "nine-prompt sequence"),
        (r"Prompt 8", "prompt-8 mention"),
        (r"correction|corrected|passed", "prompt-8 correction wording"),
        (r"Prompt 7[^.\n]{0,40}accepted|Prompt 7[^.\n]{0,220}micro-correction|final micro-correction", "prompt-7 micro-correction"),
        (r"conditionally ready", "readiness verdict"),
    ]
    for pattern, label in required:
        if not re.search(pattern, text, re.I):
            fail.append(f"{name}: missing {label}")
    if re.search(r"Prompt 9[^.\n]{0,80}(not started|awaits|awaiting authorization)", text, re.I):
        fail.append(f'{name}: stale "Prompt 9 not started" wording')
    if re.search(r"Prompt 8[^.\n]{0,60}(not started|not begun)", text, re.I):
        fail.append(f'{name}: stale "Prompt 8 not started" wording')

# 2b. QA-vs-production distinction ------------------------------------------
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd)]:
    if re.search(r"no code exists|consists entirely of research", text, re.I):
        fail.append(f"{name}: broad no-code wording remains")
    if not re.search(r"document-QA tooling|QA tooling|document QA", text, re.I):
        fail.append(f"{name}: QA-tooling wording missing")
    if not re.search(r"Production game implementation has not started|implementation has not started", text, re.I):
        fail.append(f"{name}: production-not-started wording missing")

# 3. Prompt 8 correction markers (DEF-004/005/010) ---------------------------
if not re.search(r"\*\*Version:\*\* v1\.1", r8):
    fail.append("08: version header is not v1.1")
r8_154 = r8[r8.index("### 15.4 Which protections"):r8.index("## 16. Security requirements")]
if "16 requirements on stage A" in r8_154:
    fail.append('08 §15.4: stale "16 requirements on stage A" still present as a live claim')
if not re.search(r"\*\*Twelve requirements\*\* are assigned to stage A", r8):
    fail.append("08 §15.4: twelve-requirement correction missing")
if not re.search(r"12 full requirements \(SEC-010/011", r8):
    fail.append("08 §17.1: exact stage-A count note missing")
if not re.search(r"subset of SEC-031", r8):
    fail.append("08 A8: SEC-031 subset wording missing")
if not re.search(r"PL \(money/pipeline spine rows required at A8", r8):
    fail.append("08 §16.2: SEC-031 stage cell not clarified")
if not re.search(r"\*\*Stage-A prevention:\*\*", r8):
    fail.append("08 TH-011: Stage-A prevention wording missing")
if not re.search(r"Residual \(accepted\)", r8):
    fail.append("08 TH-011: accepted residual wording missing")
if not re.search(r"superseded", r8):
    fail.append("08 §26.9: superseded Prompt 9 handoff wording missing")

# 3b. Prompt 8 §25/§26 markers retained from the first pass -------------------
r8sec = r8[r8.index("## 25. Quality assurance record"):r8.index("## 26. Handoff")]
for label in [
    "SEC-009",
    "Correction-pass addendum",
    "validate_final.py",
    "DECISIONS.md was NOT changed",
    "production game implementation has not started",
]:
    if not re.search(re.escape(label), r8sec, re.I):
        fail.append(f"08 §25: missing {label}")

row9 = re.search(r"SEC-009 \|", r8)
if row9:
    blk = r8[row9.start():row9.start() + 700]
    if not any(x in blk for x in ["reserve, not a usage", "deliberately unassigned", "placeholder row"]):
        fail.append("SEC-009 row not labelled as reserve")

# 4. Prompt 9 state ----------------------------------------------------------
if not re.search(r"## Section 20 — Stage 1 readiness gates", r9):
    fail.append("09: readiness-gate section missing")
for gate in ("GATE-13", "GATE-16", "GATE-18"):
    if gate not in r9:
        fail.append(f"09: {gate} missing")
if not re.search(r"\| \*\*Pass\*\* \| \*\*17\*\*", r9):
    fail.append("09: gate tally is not 17 pass")
if not re.search(r"\| \*\*Conditional\*\* \| \*\*3\*\*", r9):
    fail.append("09: gate tally is not 3 conditional")
if "**Fixed 2026-10-23**" not in r9:
    fail.append("09: corrected DEF rows not marked Fixed")
if not re.search(r"DEF-010[^\n]*\*\*Fixed 2026-10-23\*\*", r9):
    fail.append("09: DEF-010 not marked Fixed")
if not re.search(r"GATE-03[^\n]*\| \*\*Pass\*\*", r9):
    fail.append("09: GATE-03 is not marked Pass")
if not re.search(r"conditionally ready", r9, re.I):
    fail.append("09: readiness verdict missing")

# 5. ID registers ------------------------------------------------------------
def ids(text: str, prefix: str) -> set[str]:
    return {v for v in re.findall(prefix + r"-(.{3})", text) if v.isdigit()}


sec, th, st, osq = ids(r8, "SEC"), sorted(ids(r8, "TH")), sorted(ids(r8, "ST")), sorted(ids(r8, "OSQ"))
if not all(("%03d" % i) in sec for i in list(range(1, 9)) + list(range(10, 34))):
    fail.append("SEC register incomplete: " + ",".join(
        x for x in [("%03d" % i) for i in range(1, 34)] if x not in sec))
for label, (got, want) in {
    "TH-001..TH-025": (th, ["%03d" % i for i in range(1, 26)]),
    "ST-001..ST-020": (st, ["%03d" % i for i in range(1, 21)]),
    "OSQ-001..OSQ-012": (osq, ["%03d" % i for i in range(1, 13)]),
}.items():
    if got != want:
        fail.append(f"{label}: mismatch")

w = sorted(set(re.findall(r"W-18-([A-R])", r8)))
if w != [chr(c) for c in range(65, 83)]:
    fail.append('W-18-A..R register: got "' + "".join(w) + '"')

# 6. Relative links resolve --------------------------------------------------
def links(text: str) -> list[str]:
    out = []
    for m in re.finditer(r"\]\(([^)\s#]+)", text):
        link = m.group(1)
        if link.startswith(("http", "#", "mailto")):
            continue
        out.append(link)
    return out


missing = []
for text, base in [(ctx, DOCS), (hnd, DOCS), (prog, DOCS), (r8, DOCS / "stage-1"), (r9, DOCS / "stage-1")]:
    for link in set(links(text)):
        if not (base / link).resolve().exists():
            missing.append(f"{base.name}: {link}")
if missing:
    fail.append("dead relative links: " + "; ".join(missing[:10]))

# 7. DECISIONS.md integrity --------------------------------------------------
# Updated 2026-10-23 for Prompt 10.1. The original table asserted that D-005
# stayed Provisional and that no D-007 existed — a guard written while nothing
# was owner-approved. Two decisions now are (D-007, D-008) and D-005 is
# superseded, so the expectation had to follow the documents. D-004 is still
# Provisional and is asserted as such.
want_status = {
    "D-001": "Confirmed", "D-002": "Confirmed", "D-003": "Confirmed",
    "D-004": "Provisional", "D-005": "Superseded by D-008", "D-006": "Provisional",
    "D-007": "Confirmed", "D-008": "Confirmed",
}
for did, expected in want_status.items():
    rows = [ln for ln in dec.splitlines() if re.match(r"\|\s*" + re.escape(did) + r"\s*\|", ln)]
    if not rows:
        fail.append(f"DECISIONS: no row for {did}")
        continue
    cells = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    status = cells[4] if len(cells) > 4 else "(missing)"
    if not status.replace("*", "").strip().startswith(expected):
        fail.append(f"DECISIONS: {did} status is {status!r}, expected {expected}")
if "Nation Supremacy" not in dec:
    fail.append("DECISIONS: D-007 does not name Nation Supremacy")
if "Supabase" not in dec:
    fail.append("DECISIONS: D-008 does not record the Supabase direction")
if 'Keep "Operations Points" as a provisional' not in dec:
    fail.append("DECISIONS: D-004 decision text altered")
if "Treat Cloudflare Workers + D1 as initial candidates only" not in dec:
    fail.append("DECISIONS: D-005 decision text altered")

# 8. No production code outside the authorised prototype --------------------
# Prompt 10 permits exactly one isolated spike directory. Code anywhere else
# (docs/, project root, future game directories) still fails this check.
EXEMPT_PARTS = {"prototypes", "node_modules", "dist", ".git", ".wrangler"}
files = [p for p in glob.glob(str(ROOT / "**" / "*"), recursive=True) if ".git" not in Path(p).parts and Path(p).is_file()]
prodlike = [
    f
    for f in files
    if f.lower().endswith((".ts", ".js", ".tsx", ".jsx", ".cs", ".go", ".rb", ".php", ".java", ".c", ".cpp"))
    and not (set(Path(f).parts) & EXEMPT_PARTS)
]
if prodlike:
    fail.append("production-code-like files present: " + "; ".join(prodlike[:10]))
py_out = [f for f in files if f.endswith(".py") and "qa_backups" not in Path(f).parts]
if py_out:
    fail.append(".py files outside qa_backups: " + "; ".join(py_out))

# 9. Required documents exist ------------------------------------------------
for required in [
    DOCS / "stage-1" / "01_competitor_research.md",
    DOCS / "stage-1" / "02_strengths_weaknesses_player_frustrations.md",
    DOCS / "stage-1" / "03_feature_comparison_opportunity_analysis.md",
    DOCS / "stage-1" / "04_target_audience_and_player_experience.md",
    DOCS / "stage-1" / "05_core_game_concept_and_design_pillars.md",
    DOCS / "stage-1" / "06_core_gameplay_systems_and_interactions.md",
    DOCS / "stage-1" / "07_economy_design_and_market_structure.md",
    DOCS / "stage-1" / "08_security_privacy_fair_play_and_trust.md",
    DOCS / "stage-1" / "09_integrated_design_synthesis_and_readiness_audit.md",
]:
    if not required.exists():
        fail.append(f"missing required document: {required}")

print("VALIDATION:", "ALL CHECKS PASSED" if not fail else "FAILURES:")
for item in fail:
    print("  -", item)
sys.exit(1 if fail else 0)
