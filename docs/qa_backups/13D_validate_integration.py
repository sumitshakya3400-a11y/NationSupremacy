#!/usr/bin/env python3
"""Prompt 13D focused validator — documentary quality only.

Verifies structural, semantic and cross-document integrity of the four B-13D
integration deliverables. It is not a UI test, not an accessibility audit, not
an independent review and not evidence of implementation.

Run:  python docs/qa_backups/13D_validate_integration.py
      python docs/qa_backups/13D_validate_integration.py --self-test
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from copy import deepcopy
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
D1 = DOCS / "stage-2" / "23_ui_system_integration_and_traceability.md"
D2 = DOCS / "stage-2" / "23_ui_integration_contracts.md"
D3 = DOCS / "stage-2" / "23_ui_acceptance_test_catalog.md"
D4 = DOCS / "stage-2" / "23_prompt_13_final_reconciliation_and_acceptance.md"
DECISIONS = DOCS / "DECISIONS.md"
DD = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
SCREENS = DOCS / "stage-2" / "21_screen_specifications.md"
COMPONENTS = DOCS / "stage-2" / "21_component_specifications.md"
INTERACTIONS = DOCS / "stage-2" / "22_interaction_flows_and_player_experience.md"
JOURNEYS = DOCS / "stage-2" / "22_player_journey_specifications.md"
B13_PARENT = DOCS / "stage-2" / "21_interface_and_player_journeys.md"
AI_CONTEXT = DOCS / "AI_CONTEXT.md"
AI_HANDOFF = DOCS / "AI_HANDOFF.md"
PROJECT_PROGRESS = DOCS / "PROJECT_PROGRESS.md"
ROADMAP = DOCS / "ROADMAP.md"
LOG = DOCS / "stage-2" / "06_stage_2_progress_log.md"
STAGE2_ROADMAP = DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md"

SCREEN_IDS = [f"SCR-{i:03d}" for i in range(1, 101)]
COMPONENT_IDS = [f"UI-CMP-{i:03d}" for i in range(1, 91)]
OVERLAY_IDS = [f"OVL-{i:02d}" for i in range(1, 9)]
JOURNEY_IDS = [f"JRN-{c}" for c in "ABCDEFGHIJKLM"]
FLOW_IDS = [f"FLOW-{i:03d}" for i in range(1, 34)]
STATE_IDS = [f"ST-{i:02d}" for i in range(1, 19)]
REQ_13B = [f"REQ-{i}" for i in range(870, 1090)]
REQ_13C = [f"REQ-{i}" for i in range(1090, 1204)]
UIX_DEFINED = ([f"UIX-{i:02d}" for i in range(1, 31)]
               + ["UIX-B01", "UIX-B02", "UIX-P01", "UIX-P02"])
GATE_IDS = [f"P13D-{i:02d}" for i in range(1, 29)]
SCENARIO_COUNTS = {"F": 26, "I": 16, "X": 12, "P": 12, "E": 14,
                   "A": 10, "R": 8, "C": 10, "J": 8}
CONTRACT_GROUPS = [
    "Identity and purpose", "Parties and authority", "Trigger and preconditions",
    "Authentication and authorization", "Request/command", "Response and result",
    "Failure conditions", "Idempotency and concurrency",
    "Retry, timeout, offline, recovery", "Audit, privacy, notification",
    "Traceability and dependencies",
]
GAP_STATUSES = {"FIXED IN 13D", "OPEN", "DEFERRED", "OWNER-RESERVED",
                "OPEN (BY GATE)", "OPEN (PROVISIONAL)", "OPEN (EXPECTED)",
                "OPEN (BY RULE)"}
GATE_STATUSES = {"PASS", "PARTIAL", "FAIL", "BLOCKED"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def section(text: str, start: str, end: str) -> str:
    a = text.find(start)
    if a < 0:
        return ""
    b = text.find(end, a + len(start))
    return text[a:] if b < 0 else text[a:b]


def check(problems: list[str], ok: bool, message: str) -> None:
    if not ok:
        problems.append(message)


def rows(text: str, pattern: str) -> list[list[str]]:
    out = []
    for line in text.splitlines():
        if re.match(pattern, line):
            out.append([c.strip() for c in line.strip().strip("|").split("|")])
    return out


def clean(cell: str) -> str:
    return cell.strip().strip("`* ").strip()


def load() -> dict[str, str]:
    return {
        "d1": read(D1) if D1.exists() else "",
        "d2": read(D2) if D2.exists() else "",
        "d3": read(D3) if D3.exists() else "",
        "d4": read(D4) if D4.exists() else "",
        "decisions": read(DECISIONS) if DECISIONS.exists() else "",
        "dd": read(DD) if DD.exists() else "",
        "screens": read(SCREENS) if SCREENS.exists() else "",
        "components": read(COMPONENTS) if COMPONENTS.exists() else "",
        "interactions": read(INTERACTIONS) if INTERACTIONS.exists() else "",
        "journeys": read(JOURNEYS) if JOURNEYS.exists() else "",
        "b13_parent": read(B13_PARENT) if B13_PARENT.exists() else "",
        "ai_context": read(AI_CONTEXT) if AI_CONTEXT.exists() else "",
        "ai_handoff": read(AI_HANDOFF) if AI_HANDOFF.exists() else "",
        "project_progress": read(PROJECT_PROGRESS) if PROJECT_PROGRESS.exists() else "",
        "roadmap": read(ROADMAP) if ROADMAP.exists() else "",
        "log": read(LOG) if LOG.exists() else "",
        "stage2_roadmap": read(STAGE2_ROADMAP) if STAGE2_ROADMAP.exists() else "",
    }


def expand_req_ranges(text: str) -> set[str]:
    found = {int(n) for n in re.findall(r"REQ-(\d{4})", text)}
    for a, b in re.findall(r"REQ-(\d{4})\s*(?:`?…`?|–|-)\s*`?REQ-(\d{4})", text):
        lo, hi = int(a), int(b)
        if lo <= hi and hi - lo < 500:
            found.update(range(lo, hi + 1))
    return {f"REQ-{n}" for n in found}


def uix_tokens(text: str) -> set[str]:
    out: set[str] = set()
    for m in re.finditer(r"UIX-((?:B|P)?\d{2})(?:/(\d{2}))?", text):
        out.add(f"UIX-{m.group(1)}")
        if m.group(2):
            out.add(f"UIX-{m.group(2)}")
    return out


def test_ids(text: str) -> set[str]:
    return set(re.findall(r"UAT-(?:SCR-\d{3}|(?:F|I|X|P|E|A|R|C|J)-\d{3})", text))


def scenario_rows(text: str) -> list[list[str]]:
    return rows(text, r"^\| `UAT-(?:F|I|X|P|E|A|R|C|J)-\d{3}` \|")


def screen_test_rows(text: str) -> list[list[str]]:
    return rows(text, r"^\| `UAT-SCR-\d{3}` \|")


def uix_blocks(text: str) -> dict[str, str]:
    parts = re.split(r"^### (UIX-(?:B|P)?\d{2}) — .*$", text, flags=re.M)
    out: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        body = re.split(r"^### ", parts[i + 1], maxsplit=1, flags=re.M)[0]
        out[parts[i]] = body
    return out


MATRIX_B_CLASSES = ("Complete", "Partial", "Blocked", "Open-Owner", "Candidate")
GAP_CLASSES = ("FIXED IN 13D", "OPEN", "DEFERRED", "OWNER-RESERVED")
GAP_STATUS_GROUPS = {
    "Fixed": ("FIXED IN 13D",),
    "Open": ("OPEN", "OPEN (BY GATE)", "OPEN (PROVISIONAL)", "OPEN (EXPECTED)", "OPEN (BY RULE)"),
    "Deferred": ("DEFERRED",),
    "Owner-reserved": ("OWNER-RESERVED",),
}


def matrix_b_counts(text: str) -> tuple[Counter, int]:
    sec = section(text, "## 9. Matrix B", "**Reverse-mapping conclusion")
    counts: Counter = Counter()
    for line in sec.splitlines():
        m = re.match(r"^\| [A-Za-z]", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) > 3 and cells[3] in MATRIX_B_CLASSES:
            counts[cells[3]] += 1
    return counts, sum(counts.values())


def b13_matrix_a_counts(text: str) -> tuple[Counter, Counter, int]:
    sec = section(text, "## 24. Matrix A", "## 25. Matrix B")
    status: Counter = Counter()
    klass: Counter = Counter()
    n = 0
    for line in sec.splitlines():
        if not re.match(r"^\| `SCR-\d{3}` \|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 10:
            continue
        n += 1
        status[clean(cells[9])] += 1
        klass[clean(cells[2])] += 1
    return status, klass, n


def gate_cells(text: str, gid: str) -> list[str]:
    for line in text.splitlines():
        if line.startswith(f"| `{gid}` |"):
            return [c.strip() for c in line.strip().strip("|").split("|")]
    return []


def gap_rows_in(text: str) -> list[list[str]]:
    sec = section(text, "## 17. Gap register", "**Gap tally:**")
    return rows(sec, r"^\| `GAP-13D-\d{2}` \|")


def gap_summary_line(text: str) -> str:
    for line in text.splitlines():
        if "16 gaps" in line and ("3 fixed" in line or "8 open" in line or "5 open" in line):
            return line
    return ""


def prompt13_roadmap_row(text: str) -> str:
    return next((ln for ln in text.splitlines()
                 if ln.startswith("| 13 | Interface, screens and player journeys")), "")


def gap_summary_problems(text: str, label: str) -> list[str]:
    p: list[str] = []
    line = gap_summary_line(text)
    if not line:
        p.append(f"{label}: no 16-gap summary line")
        return p
    for token in ("8 open", "3 deferred", "2 owner-reserved"):
        check(p, token in line, f"{label}: gap summary missing {token!r}")
    for bad in ("5 open", "4 provisional/gated"):
        check(p, bad not in line, f"{label}: stale gap phrase {bad!r}")
    return p


# ---------------------------------------------------------------- checks

def validate(t: dict[str, str]) -> list[tuple[str, str, list[str]]]:
    results: list[tuple[str, str, list[str]]] = []

    def add(cid: str, name: str, probs: list[str]) -> None:
        results.append((cid, name, probs))

    # 01 deliverables
    p: list[str] = []
    for path, key in ((D1, "d1"), (D2, "d2"), (D3, "d3"), (D4, "d4")):
        check(p, bool(t[key]), f"missing deliverable: {path.name}")
        check(p, "<<<<<<<" not in t[key] and ">>>>>>>" not in t[key],
              f"merge-conflict marker in {path.name}")
    add("13D-01", "Deliverables exist and are conflict-free", p)

    # 02-05 required sections
    required = {
        "13D-02": ("d1", "D1", [
            "## 1. Scope, inputs and boundaries", "## 2. Method and status vocabulary",
            "## 3. Source-authority matrix", "## 4. Stage 1 cross-system consistency audit",
            "## 5. Stage 2 cross-system consistency audit", "## 6. Requirement and decision integrity checks",
            "## 7. Conflict register and resolutions", "## 8. Matrix A", "## 9. Matrix B",
            "## 10. Matrix L", "## 11. Matrix E", "## 12. Matrix F", "## 13. Matrix G",
            "## 14. Interaction-state consistency", "## 15. Requirement traceability",
            "## 16. Matrix J", "## 17. Gap register", "## 18. Matrix index and integrity statement"]),
        "13D-03": ("d2", "D2", [
            "## 1. Purpose and rules", "## 2. Contract field template", "## 3. Existing-contract reuse map",
            "## 4. Read/write boundary register", "## 5. Contract catalogue",
            "## 6. Failure taxonomy and UI treatment", "## 7. Idempotency, duplicate and concurrency register",
            "## 8. Retry, timeout, offline and recovery matrix",
            "## 9. Audit, privacy and notification requirements",
            "## 10. Provisional, blocked and dependency contracts",
            "## 11. Contract coverage matrix (Matrix H)", "## 12. Contract integrity statement"]),
        "13D-04": ("d3", "D3", [
            "## 1. Test design method", "## 2. Category A", "## 3. Category B", "## 4. Category C",
            "## 5. Category D", "## 6. Category E", "## 7. Category F", "## 8. Category G",
            "## 9. Category H", "## 10. Category I", "## 11. Category J",
            "## 12. Bidirectional traceability", "## 13. Execution-status register",
            "## 14. Acceptance evidence references"]),
        "13D-05": ("d4", "D4", [
            "## 1. Final status", "## 2. Owner-acceptance history", "## 3. What Prompt 13D completed",
            "## 4. Overall UI completeness assessment", "## 5. Cross-stage audit summary",
            "### 5.1 Matrix K", "## 6. Registers", "## 7. Prompt 13D acceptance-gate register",
            "## 8. Overall acceptance conclusion", "## 9. Validation results",
            "## 10. Known limitations", "## 11. Implementation dependencies",
            "## 12. Independent-audit readiness", "## 13. Final next action"]),
    }
    for cid, (key, label, heads) in required.items():
        probs = [f"{label} missing section: {h}" for h in heads if h not in t[key]]
        add(cid, f"{label} required sections", probs)

    # 06 Matrix A screens complete
    p = []
    ma = section(t["d1"], "## 8. Matrix A", "### 8.1")
    screen_rows = rows(ma, r"^\| `SCR-\d{3}` \|")
    ids = [r[0].strip("`") for r in screen_rows]
    check(p, ids == SCREEN_IDS, f"Matrix A screens are not SCR-001..SCR-100 ({len(ids)} rows)")
    check(p, len(set(ids)) == len(ids), "duplicate screen row in Matrix A")
    for r in screen_rows:
        check(p, len(r) == 14, f"{r[0]} Matrix A row has {len(r)} cells, expected 14")
        req = f"`REQ-{869 + int(r[0].strip('`')[-3:])}`"
        check(p, req in r[8], f"{r[0]} cites {r[8]} not {req}")
        check(p, bool(re.search(r"UAT-SCR-\d{3}", r[11])), f"{r[0]} has no screen test")
    add("13D-06", "Matrix A completeness (100 screens, 14 fields)", p)

    # 07 screen tests complete
    p = []
    st = screen_test_rows(t["d3"])
    sids = [r[0].strip("`") for r in st]
    check(p, sids == [f"UAT-SCR-{i:03d}" for i in range(1, 101)],
          f"screen tests are not UAT-SCR-001..100 ({len(sids)} rows)")
    for i, r in enumerate(st, 1):
        check(p, len(r) == 12, f"UAT-SCR-{i:03d} has {len(r)} cells, expected 12")
        check(p, f"`REQ-{869 + i}`" in r[7], f"UAT-SCR-{i:03d} does not cite REQ-{869 + i}")
        check(p, r[10] == "SPECIFIED", f"UAT-SCR-{i:03d} status is {r[10]!r}")
        check(p, r[1].startswith(f"`SCR-{i:03d}`"), f"UAT-SCR-{i:03d} does not test SCR-{i:03d}")
    add("13D-07", "Screen acceptance tests match screens and requirements", p)

    # 08 components/overlays
    p = []
    mg = section(t["d1"], "## 13. Matrix G", "**Component verdict")
    comp = rows(mg, r"^\| `(?:UI-CMP-\d{3}|OVL-\d{2})` \|")
    cids = [r[0].strip("`") for r in comp]
    check(p, cids == COMPONENT_IDS + OVERLAY_IDS,
          f"component matrix is not UI-CMP-001..090 + OVL-01..08 ({len(cids)} rows)")
    for r in comp:
        check(p, len(r) == 9, f"{r[0]} component row has {len(r)} cells, expected 9")
        check(p, bool(re.search(r"UAT-[A-Z-]*\d{3}", r[7])), f"{r[0]} has no test")
    add("13D-08", "Component and overlay coverage (90 + 8)", p)

    # 09 journeys
    p = []
    me = section(t["d1"], "## 11. Matrix E", "**Journey verdict")
    jr = rows(me, r"^\| `JRN-[A-M]` \|")
    jids = [r[0].strip("`") for r in jr]
    check(p, jids == JOURNEY_IDS, f"journeys are not JRN-A..JRN-M ({jids})")
    for r in jr:
        check(p, len(r) == 9, f"{r[0]} journey row has {len(r)} cells, expected 9")
        check(p, bool(re.search(r"UAT-[A-Z-]*\d{3}", r[6])), f"{r[0]} has no test")
    add("13D-09", "Journey integration coverage (13)", p)

    # 10 flows
    p = []
    mf = section(t["d1"], "## 12. Matrix F", "**Flow verdict")
    fr = rows(mf, r"^\| `FLOW-\d{3}` \|")
    fids = [r[0].strip("`") for r in fr]
    check(p, fids == FLOW_IDS, f"flows are not FLOW-001..033 ({len(fids)} rows)")
    for r in fr:
        check(p, len(r) == 9, f"{r[0]} flow row has {len(r)} cells, expected 9")
        check(p, bool(re.search(r"UAT-[A-Z-]*\d{3}", r[8])), f"{r[0]} has no test")
    add("13D-10", "Flow-to-system coverage (33)", p)

    # 11 states
    p = []
    ms = section(t["d1"], "## 14. Interaction-state consistency", "**Missing transitions")
    sr = rows(ms, r"^\| `ST-\d{2}` \|")
    stids = [r[0].strip("`") for r in sr]
    check(p, stids == STATE_IDS, f"states are not ST-01..ST-18 ({len(stids)} rows)")
    for r in sr:
        check(p, len(r) == 7, f"{r[0]} state row has {len(r)} cells, expected 7")
    add("13D-11", "Interaction-state reconciliation (18)", p)

    # 12 navigation
    p = []
    ml = section(t["d1"], "## 10. Matrix L", "**Reachability verdict")
    nr = rows(ml, r"^\| `SCR-\d{3}` \|")
    nids = [r[0].strip("`") for r in nr]
    check(p, nids == SCREEN_IDS, f"navigation rows are not 100 screens ({len(nids)})")
    routes = [r[2] for r in nr]
    check(p, len(set(routes)) == len(routes), "duplicate route key in Matrix L")
    for r in nr:
        check(p, len(r) == 7, f"{r[0]} navigation row has {len(r)} cells, expected 7")
        check(p, bool(r[6]), f"{r[0]} has no reachability verdict")
    add("13D-12", "Navigation reachability matrix (100 routes)", p)

    # 13 cross-cutting requirement ledger
    p = []
    mcii = section(t["d1"], "### 15.2 Matrix C (ii)", "**Tally:**")
    cr = rows(mcii, r"^\| `REQ-\d{3,4}` \|")
    crate = [r[0].strip("`") for r in cr]
    check(p, crate == [f"REQ-{i}" for i in range(970, 1090)],
          f"cross-cutting ledger is not REQ-970..1089 ({len(crate)} rows)")
    add("13D-13", "Cross-cutting requirement ledger (120 rows)", p)

    # 14 interaction requirement coverage
    p = []
    mciii = section(t["d1"], "### 15.3 Matrix C (iii)", "**Tally:**")
    covered = expand_req_ranges(mciii)
    missing = [r for r in REQ_13C if r not in covered]
    check(p, not missing, f"interaction requirements not dispositioned: {missing[:10]}")
    check(p, "114/114" in mciii or "114/114" in t["d1"], "D1 does not state 114/114 interaction coverage")
    add("13D-14", "Interaction requirement coverage (114)", p)

    # 15 requirement block integrity
    p = []
    check(p, "334/334" in t["d3"] or "334 / 334" in t["d3"], "D3 does not state 334/334 coverage")
    check(p, "REQ-1204" in t["d4"], "D4 does not record the REQ-1204 frontier")
    for key, label in (("d1", "D1"), ("d2", "D2"), ("d3", "D3"), ("d4", "D4")):
        bad = [n for n in re.findall(r"REQ-(\d{4})", t[key]) if int(n) > 1204]
        check(p, not bad, f"{label} references impossible requirement(s): {bad[:5]}")
    add("13D-15", "Requirement frontier and identifier sanity", p)

    # 16 UIX definitions unique and complete
    p = []
    blocks = uix_blocks(t["d2"])
    check(p, list(blocks) == UIX_DEFINED, f"UIX definitions are not the expected 34 ({list(blocks)})")
    check(p, len(blocks) == len(UIX_DEFINED), "duplicate UIX heading")
    for uid, body in blocks.items():
        for group in CONTRACT_GROUPS:
            check(p, f"| {group}" in body, f"{uid} missing group row: {group}")
        status_ok = any(s in body for s in ("SPECIFIED", "PROVISIONAL", "BLOCKED"))
        check(p, status_ok, f"{uid} has no status token")
    add("13D-16", "UIX contract structure (34 x 11 groups)", p)

    # 17 contract references resolve
    p = []
    refs = uix_tokens(t["d1"]) | uix_tokens(t["d3"]) | uix_tokens(t["d4"])
    unknown = sorted(refs - set(UIX_DEFINED))
    check(p, not unknown, f"undefined UIX reference(s): {unknown}")
    for uid in UIX_DEFINED:
        check(p, uid in t["d1"], f"{uid} is defined but never used in D1")
    add("13D-17", "UIX reference integrity and usage", p)

    # 18 Matrix H coverage
    p = []
    mh = section(t["d2"], "## 11. Contract coverage matrix (Matrix H)", "**Coverage tally:**")
    hr = rows(mh, r"^\| `UIX-(?:B|P)?\d{2}` \|")
    hids = [r[0].strip("`") for r in hr]
    check(p, hids == UIX_DEFINED, f"Matrix H rows are not the 34 contracts ({len(hids)})")
    for r in hr:
        check(p, len(r) == 7, f"{r[0]} Matrix H row has {len(r)} cells, expected 7")
        check(p, bool(re.search(r"UAT-I-\d{3}", r[5])), f"{r[0]} has no contract test")
    add("13D-18", "Matrix H contract coverage (34)", p)

    # 19 scenario test counts by category
    p = []
    sc = scenario_rows(t["d3"])
    counts = {k: 0 for k in SCENARIO_COUNTS}
    for r in sc:
        m = re.match(r"`UAT-([FIXPEARCJ])-\d{3}`", r[0])
        if m and m.group(1) in counts:
            counts[m.group(1)] += 1
    check(p, counts == SCENARIO_COUNTS, f"scenario counts are {counts}, expected {SCENARIO_COUNTS}")
    check(p, len(sc) == 116, f"scenario test rows are {len(sc)}, expected 116")
    add("13D-19", "Scenario test counts (116 across 9 categories)", p)

    # 20 scenario rows 16 fields and status
    p = []
    statuses = {"SPECIFIED": 0, "BLOCKED": 0}
    for r in sc:
        check(p, len(r) == 16, f"{r[0]} has {len(r)} cells, expected 16")
        status = clean(r[14])
        check(p, status in statuses, f"{r[0]} status is {status!r}")
        if status in statuses:
            statuses[status] += 1
        for idx, label in ((4, "preconditions"), (11, "expected"), (12, "failure"),
                           (13, "acceptance"), (15, "evidence")):
            check(p, bool(r[idx]), f"{r[0]} empty {label} field")
    add("13D-20", "Scenario test field completeness and status", p)

    # 21 test totals and status tally
    p = []
    check(p, statuses["SPECIFIED"] + len(st) == 215, f"SPECIFIED count is {statuses['SPECIFIED']} scenario + {len(st)} screen, expected 215")
    check(p, statuses["BLOCKED"] == 1, f"BLOCKED count is {statuses['BLOCKED']}, expected 1")
    check(p, "| **Total** | **216** |" in t["d3"], "D3 does not state the 216 total")
    check(p, "215" in t["d4"] and "1 BLOCKED" in t["d4"], "D4 does not state 215 SPECIFIED / 1 BLOCKED")
    add("13D-21", "Test totals and status tally", p)

    # 22 duplicate UAT identifiers
    p = []
    all_rows = screen_test_rows(t["d3"]) + sc
    ids = [r[0].strip("`") for r in all_rows]
    check(p, len(set(ids)) == len(ids), "duplicate UAT identifier")
    add("13D-22", "UAT identifier uniqueness", p)

    # 23 D1 test references resolve
    p = []
    referenced = test_ids(t["d1"])
    defined = set(ids)
    unknown = sorted(referenced - defined)
    check(p, not unknown, f"D1 references undefined test(s): {unknown}")
    add("13D-23", "Test references in D1 resolve", p)

    # 24 gap register integrity
    p = []
    mg = section(t["d1"], "## 17. Gap register", "**Gap tally:**")
    gr = rows(mg, r"^\| `GAP-13D-\d{2}` \|")
    gids = [r[0].strip("`") for r in gr]
    check(p, len(gids) == 16 and len(set(gids)) == 16, f"gap rows are {len(gids)} (expected 16 unique)")
    for r in gr:
        check(p, len(r) == 16, f"{r[0]} gap row has {len(r)} cells, expected 16")
        check(p, any(clean(r[8]).startswith(x) for x in ("High", "Medium", "Low", "Informational")), f"{r[0]} severity {r[8]!r}")
        check(p, clean(r[15]) in GAP_STATUSES, f"{r[0]} status {r[15]!r}")
        check(p, bool(r[14]), f"{r[0]} has no acceptance condition")
    add("13D-24", "Gap register integrity (16 rows, fields, statuses)", p)

    # 25 gap disposition references
    p = []
    check(p, "FIXED IN 13D" in t["d1"], "D1 records no fixed gap")
    for ref in ("GAP-13D-06", "GAP-13D-07"):
        check(p, ref in t["d4"], f"D4 does not carry {ref}")
    add("13D-25", "High-severity gaps carried into reconciliation", p)

    # 26 acceptance gates complete
    p = []
    mg4 = section(t["d4"], "## 7. Prompt 13D acceptance-gate register", "## 8.")
    gate_rows = rows(mg4, r"^\| `P13D-\d{2}` \|")
    gate_ids = [r[0].strip("`") for r in gate_rows]
    check(p, gate_ids == GATE_IDS, f"gates are not P13D-01..28 ({len(gate_ids)})")
    for r in gate_rows:
        check(p, len(r) == 9, f"{r[0]} gate row has {len(r)} cells, expected 9")
        check(p, clean(r[6]) in GATE_STATUSES, f"{r[0]} status {clean(r[6])!r}")
        for idx, label in ((2, "required evidence"), (5, "actual result"),
                           (7, "outstanding limitation"), (8, "next action")):
            check(p, bool(r[idx]), f"{r[0]} empty {label}")
    add("13D-26", "Acceptance-gate register completeness (28 gates)", p)

    # 27 gate tally consistency
    p = []
    tally = {"PASS": 0, "PARTIAL": 0, "FAIL": 0, "BLOCKED": 0}
    for r in gate_rows:
        status = clean(r[6])
        if status in tally:
            tally[status] += 1
    m = re.search(r"Gate tally:\*\*\s*\*\*(\d+) PASS / (\d+) PARTIAL / (\d+) FAIL / (\d+) BLOCKED", t["d4"])
    check(p, bool(m), "D4 gate tally line missing")
    if m:
        expected = tuple(int(x) for x in m.groups())
        actual = (tally["PASS"], tally["PARTIAL"], tally["FAIL"], tally["BLOCKED"])
        check(p, expected == actual, f"gate tally {expected} disagrees with rows {actual}")
    add("13D-27", "Gate tally arithmetic", p)

    # 28 overall conclusion and owner boundary
    p = []
    check(p, "COMPLETE WITH DOCUMENTED LIMITATIONS" in t["d4"], "overall conclusion missing")
    check(p, "OWNER ACCEPTANCE PENDING" in t["d4"], "D4 does not mark 13D acceptance pending")
    check(p, "does not record owner acceptance of Prompt 13D" in t["d4"],
          "D4 does not disclaim owner acceptance")
    check(p, "Prompt 14" in t["d4"] and "NOT AUTHORIZED" in t["d4"],
          "D4 does not leave Prompt 14 unauthorized")
    add("13D-28", "Overall conclusion and owner boundary", p)

    # 29 historical positions preserved
    p = []
    for token in ("R7 implementation", "R8", "12B-C1", "P12B-14", "2537606", "94f5ec4"):
        check(p, token in t["d4"], f"D4 does not preserve historical position: {token}")
    add("13D-29", "Historical decisions and authorized commits preserved", p)

    # 30 no false acceptance claims
    p = []
    check(p, "Prompt 13D is OWNER ACCEPTED" not in t["d4"], "D4 claims owner acceptance of 13D")
    check(p, "13D is OWNER ACCEPTED" not in t["d1"] + t["d2"] + t["d3"], "companion claims owner acceptance of 13D")
    add("13D-30", "No false owner-acceptance claim", p)

    # 31 source-authority matrix size
    p = []
    sa = section(t["d1"], "## 3. Source-authority matrix", "### 2.4")
    srows = rows(sa, r"^\| \d+ \|")
    check(p, len(srows) >= 20, f"source-authority matrix has {len(srows)} rows, expected >= 20")
    add("13D-31", "Source-authority matrix coverage", p)

    # 32 conflict register
    p = []
    confs = re.findall(r"`CONF-13D-(\d{2})`", t["d1"])
    check(p, len(confs) >= 10, f"conflict register has {len(confs)} rows, expected >= 10")
    check(p, len(set(confs)) == len(confs), "duplicate CONF identifier")
    add("13D-32", "Conflict register completeness", p)

    # 33 Matrix index lists A-L
    p = []
    mi = section(t["d1"], "## 18. Matrix index", "**Integrity statement")
    for letter in "ABCDEFGHIJKL":
        check(p, re.search(rf"\| {letter} \|", mi) is not None, f"Matrix index missing {letter}")
    add("13D-33", "All master matrices A-L indexed", p)

    # 34 screen references valid
    p = []
    for key, label in (("d1", "D1"), ("d3", "D3"), ("d4", "D4")):
        refs = set(re.findall(r"SCR-(\d{3})", t[key]))
        bad = sorted(n for n in refs if int(n) > 100 or int(n) < 1)
        check(p, not bad, f"{label} references invalid screen(s): {bad}")
    add("13D-34", "Screen identifiers valid", p)

    # 35 component/journey/flow references valid
    p = []
    for key, label in (("d1", "D1"), ("d2", "D2"), ("d3", "D3")):
        for n in re.findall(r"UI-CMP-(\d{3})", t[key]):
            check(p, 1 <= int(n) <= 90, f"{label} invalid component UI-CMP-{n}")
        for n in re.findall(r"OVL-(\d{2})", t[key]):
            check(p, 1 <= int(n) <= 8, f"{label} invalid overlay OVL-{n}")
        for n in re.findall(r"FLOW-(\d{3})", t[key]):
            check(p, 1 <= int(n) <= 33, f"{label} invalid flow FLOW-{n}")
        for c in re.findall(r"JRN-([A-M])", t[key]):
            check(p, f"JRN-{c}" in JOURNEY_IDS, f"{label} invalid journey JRN-{c}")
    add("13D-35", "Component, overlay, flow and journey identifiers valid", p)

    # 36 core source files contain the referenced IDs
    p = []
    for sid in SCREEN_IDS:
        check(p, f"### {sid} —" in t["screens"], f"{sid} not specified in 21_screen_specifications.md")
    for cid in COMPONENT_IDS:
        check(p, f"### {cid} —" in t["components"], f"{cid} not specified in 21_component_specifications.md")
    for oid in OVERLAY_IDS:
        check(p, f"### {oid} —" in t["components"], f"{oid} not specified in 21_component_specifications.md")
    for jid in JOURNEY_IDS:
        check(p, f"### {jid} —" in t["journeys"], f"{jid} not specified in journey document")
    add("13D-36", "Referenced source identifiers exist in canonical sources", p)

    # 37 contract group count statement
    p = []
    check(p, "35" in t["d2"] and "field numbers" in t["d2"], "D2 does not map the 35 contract fields")
    check(p, "34" in t["d2"], "D2 does not state the 34 contract entries")
    add("13D-37", "Contract field and count statement", p)

    # 38 failure taxonomy coverage
    p = []
    errs = set(re.findall(r"ERR-(\d{2})", t["d2"]))
    check(p, len({e for e in errs if 1 <= int(e) <= 20}) >= 18, "D2 failure taxonomy covers fewer than 18 ERR rows")
    add("13D-38", "Failure taxonomy coverage", p)

    # 39 error/recovery references in D3
    p = []
    for token in ("ERR-01", "ERR-20", "DUP-01", "OFF-01", "ST-17"):
        check(p, token in t["d3"] or token in t["d1"], f"missing failure/recovery token {token}")
    add("13D-39", "Error, duplicate, offline and recovery coverage", p)

    # 40 accessibility evidence boundary
    p = []
    check(p, "No WCAG conformance is claimed" in t["d3"] or "no WCAG conformance" in t["d3"].lower(),
          "D3 does not bound WCAG claims")
    check(p, "WCAG 2.2" in t["d1"], "D1 does not record the accessibility standard")
    add("13D-40", "Accessibility evidence boundary", p)

    # 41 responsive duties
    p = []
    for token in ("must-not-simplify", "320", "Tablet", "Mobile"):
        check(p, token.lower() in (t["d1"] + t["d3"]).lower(), f"responsive duty missing: {token}")
    add("13D-41", "Responsive coverage", p)

    # 42 eight-section architecture
    p = []
    for section_name in ("Home", "Economy", "Cities", "Politics", "Foreign", "War", "World", "Account"):
        check(p, f"| {section_name} |" in t["d1"] or section_name in t["d1"],
              f"architecture section missing: {section_name}")
    check(p, "mapless" in t["d1"].lower(), "mapless world statement missing")
    check(p, "Network View" in t["d1"], "Network View statement missing")
    add("13D-42", "Prompt 13A architecture preservation", p)

    # 43 13B counts
    p = []
    for token in ("100", "90", "8", "220", "`REQ-870`", "`REQ-1089`", "D-206", "D-219"):
        check(p, token in t["d1"], f"D1 misses B-13 baseline token: {token}")
    add("13D-43", "Prompt 13B baseline preservation", p)

    # 44 13C counts
    p = []
    for token in ("13", "33", "18", "`REQ-1090`", "`REQ-1203`", "D-220", "D-232"):
        check(p, token in t["d1"], f"D1 misses B-13C baseline token: {token}")
    add("13D-44", "Prompt 13C baseline preservation", p)

    # 45 decisions recorded
    p = []
    for did in ("D-234", "D-235", "D-236"):
        check(p, did in t["d4"], f"D4 does not record {did}")
        check(p, re.search(rf"^\| {did} \|", t["decisions"], re.M) is not None, f"DECISIONS.md does not record {did}")
    for ddid in ("DD-282", "DD-283", "DD-284"):
        check(p, ddid in t["d4"], f"D4 does not record {ddid}")
    add("13D-45", "Prompt 13D decisions and mirrors", p)

    # 46 no new requirement allocated
    p = []
    check(p, "next free identifier remains **`REQ-1204`**" in t["d4"].replace("the ", ""),
          "D4 does not confirm the REQ-1204 frontier")
    check(p, "no new `REQ-` row was created" in t["d4"].lower()
          or "No new `REQ-` row was created" in t["d4"],
          "D4 does not state that no requirement was created")
    add("13D-46", "Requirement frontier unchanged", p)

    # 47 open issues register
    p = []
    for token in ("UNR-13D-01", "UNR-13D-12", "MF-13D-01", "MF-13D-09"):
        check(p, token in t["d4"], f"D4 missing register row {token}")
    add("13D-47", "Unresolved and missing-functionality registers", p)

    # 48 validation evidence present
    p = []
    for token in ("13D_validate_integration.py", "--self-test", "validate_links.py",
                  "validate_final.py", "test_next_action.py", "test_decision_registers.py"):
        check(p, token in t["d4"], f"D4 validation record missing {token}")
    add("13D-48", "Validation evidence recorded", p)

    # 49 contract no-endpoint rule
    p = []
    check(p, "does not define HTTP endpoints" in t["d2"] or "does not define HTTP" in t["d2"],
          "D2 does not disclaim endpoint definition")
    for bad in ("https://", "CREATE TABLE", "ALTER TABLE"):
        check(p, bad not in t["d2"], f"D2 invents implementation detail: {bad}")
    add("13D-49", "No invented endpoints, tables or services", p)

    # 50 contract statuses valid
    p = []
    for uid, body in blocks.items():
        for status in re.findall(r"Status:\s*`?([A-Z-]+)`?", body):
            check(p, status in {"SPECIFIED", "PROVISIONAL", "BLOCKED", "IMPLEMENTATION-DEPENDENCY"},
                  f"{uid} has invalid status {status!r}")
    add("13D-50", "Contract status vocabulary", p)

    # 51 cross-stage matrix
    p = []
    mj = section(t["d1"], "## 16. Matrix J", "**Matrix J verdict")
    mjrows = rows(mj, r"^\| [^|]+ \|")
    check(p, len(mjrows) >= 30, f"Matrix J has {len(mjrows)} rows, expected >= 30")
    add("13D-51", "Cross-stage consistency matrix (>=30)", p)

    # 52 gaps referenced from D4
    p = []
    for gid in ("GAP-13D-03", "GAP-13D-04", "GAP-13D-05"):
        check(p, gid in t["d4"], f"D4 does not reference {gid}")
    add("13D-52", "Deferred/owner gap references carried", p)

    # 53 no implementation claim
    p = []
    for key, label in (("d1", "D1"), ("d2", "D2"), ("d3", "D3"), ("d4", "D4")):
        check(p, "No frontend" not in t[key] or True, "")  # no-op, kept for clarity
    check(p, "implements no screen" in t["d1"] or "It implements no screen" in t["d1"],
          "D1 does not disclaim implementation")
    check(p, "No built UI exists" in t["d3"] or "no built UI exists" in t["d3"].lower(),
          "D3 does not state the implementation absence")
    add("13D-53", "Implementation absence stated", p)

    # 54 markdown links resolve
    p = []
    for path, key in ((D1, "d1"), (D2, "d2"), (D3, "d3"), (D4, "d4")):
        for target in re.findall(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)", t[key]):
            if target.startswith(("http://", "https://")):
                continue
            resolved = (path.parent / target).resolve()
            check(p, resolved.exists(), f"broken link in {path.name}: {target}")
    add("13D-54", "Markdown links resolve", p)

    # 55 maturity boundary: execution outcomes are vocabulary only
    p = []
    check(p, t["d3"].count("never used in 13D") >= 3,
          "D3 status vocabulary does not mark execution states unused")
    for r in sc:
        check(p, clean(r[14]) in {"SPECIFIED", "BLOCKED"},
              f"{r[0]} has execution status {r[14]!r}")
    add("13D-55", "No execution claims in test tables", p)

    # 56 contract tests exist for every UIX
    p = []
    for uid in UIX_DEFINED:
        check(p, uid in mh, f"{uid} missing from Matrix H coverage")
    check(p, "0 orphan contracts" in t["d2"], "D2 does not state 0 orphan contracts")
    add("13D-56", "Contract-to-test coverage statement", p)

    # 57 journey/flow reachability not broken by conditional screens
    p = []
    for cid in ("SCR-020", "SCR-038", "SCR-039", "SCR-068", "SCR-077"):
        check(p, cid in t["d1"], f"conditional screen {cid} not addressed")
        check(p, cid not in section(t["d1"], "## 11. Matrix E", "**Journey verdict"),
              f"conditional screen {cid} appears in an active journey")
    add("13D-57", "Conditional/provisional screens remain outside active journeys", p)

    # 58 counts agree across documents
    p = []
    for doc, key, label in ((t["d2"], "d2", "D2"), (t["d3"], "d3", "D3"), (t["d4"], "d4", "D4")):
        check(p, "216" in doc if label == "D3" else True, "")
    check(p, "216" in t["d3"] and "216" in t["d4"], "test total 216 disagrees across D3/D4")
    check(p, "34" in t["d2"] and "34" in t["d4"], "contract total 34 disagrees across D2/D4")
    check(p, "100" in t["d1"] and "100" in t["d4"], "screen total 100 disagrees across D1/D4")
    add("13D-58", "Cross-document totals agree", p)

    # 59 no duplicate structural identifiers across 13D
    p = []
    for family, regex in (("UAT", r"`(UAT-[A-Z-]*\d{3})`"), ("UIX", r"`(UIX-(?:B|P)?\d{2})`"),
                          ("GAP", r"`(GAP-13D-\d{2})`"), ("P13D", r"`(P13D-\d{2})`")):
        found = re.findall(regex, t["d1"] + t["d2"] + t["d3"] + t["d4"])
        # A reference may repeat legitimately; duplicates are checked on definition rows above.
        check(p, len(found) > 0, f"no {family} identifiers found")
    add("13D-59", "Identifier families present and non-empty", p)

    # 60. Matrix B actual row count and status totals
    p = []
    mb_counts, mb_total = matrix_b_counts(t["d1"])
    expected_mb = Counter({"Complete": 74, "Partial": 8, "Blocked": 5,
                           "Open-Owner": 2, "Candidate": 1})
    check(p, mb_total == 90, f"Matrix B has {mb_total} capability rows, expected 90")
    check(p, mb_counts == expected_mb, f"Matrix B totals are {dict(mb_counts)}, expected {dict(expected_mb)}")
    add("13D-60", "Matrix B capability rows and five status totals", p)

    # 61. P13D-11 agrees with Matrix B
    p = []
    g11 = gate_cells(t["d4"], "P13D-11")
    joined11 = " ".join(g11)
    check(p, bool(g11), "P13D-11 gate row missing")
    check(p, "90 capabilities" in joined11, "P13D-11 does not state 90 capabilities")
    for token in ("74 Complete", "8 Partial", "5 Blocked", "2 Open-Owner", "1 Candidate"):
        check(p, token in joined11, f"P13D-11 does not state {token!r}")
    for bad in ("63 capabilities", "6 Blocked", "4 open-owner", "4 Open-Owner"):
        check(p, bad not in joined11, f"P13D-11 retains stale claim {bad!r}")
    add("13D-61", "P13D-11 agrees with Matrix B status distribution", p)

    # 62. Matrix A (13B source) specification-status and class totals
    p = []
    a_status, a_class, a_total = b13_matrix_a_counts(t["b13_parent"])
    expected_status = Counter({"SPECIFIED": 95, "PROVISIONAL": 2, "BLOCKED": 3})
    expected_class = Counter({"Mandatory": 85, "Conditional": 4,
                              "Provisional": 1, "Mandatory (admin)": 10})
    check(p, a_total == 100, f"13B Matrix A has {a_total} screens, expected 100")
    check(p, a_status == expected_status, f"13B Matrix A statuses are {dict(a_status)}, expected {dict(expected_status)}")
    check(p, a_class == expected_class, f"13B Matrix A classes are {dict(a_class)}, expected {dict(expected_class)}")
    add("13D-62", "Matrix A specification-status and class totals", p)

    # 63. D4 completeness table agrees with screen totals
    p = []
    sec4 = section(t["d4"], "## 4. Overall UI completeness assessment", "## 5. Cross-stage audit summary")
    integrated_line = next((ln for ln in sec4.splitlines() if ln.startswith("| Screens integrated |")), "")
    reachable_line = next((ln for ln in sec4.splitlines() if ln.startswith("| Screens reachable |")), "")
    check(p, "95 / 100" in integrated_line, "D4 'Screens integrated' does not state 95 / 100")
    check(p, "5" in integrated_line and "Conditional" in integrated_line and "Provisional" in integrated_line,
          "D4 'Screens integrated' does not explain the five unavailable screens")
    for bad in ("96 / 100", "4 blocked"):
        check(p, bad not in integrated_line, f"D4 'Screens integrated' retains stale claim {bad!r}")
    check(p, "95 / 100" in reachable_line and "5" in reachable_line,
          "D4 'Screens reachable' does not state 95 / 100 with 5 unavailable")
    add("13D-63", "D4 completeness table agrees with Matrix A/L", p)

    # 64. P13D-05 and P13D-13 identify all five unavailable screens
    p = []
    g05 = " ".join(gate_cells(t["d4"], "P13D-05"))
    g13 = " ".join(gate_cells(t["d4"], "P13D-13"))
    for gid, row in (("P13D-05", g05), ("P13D-13", g13)):
        for token in ("95", "5 unavailable", "SCR-020", "SCR-038", "SCR-039", "SCR-077", "SCR-068"):
            check(p, token in row, f"{gid} does not state {token!r}")
        check(p, "4 conditional/provisional screens" not in row, f"{gid} retains the four-screen claim")
    check(p, "95 `INTEGRATED`" in t["d1"] and "2 `INTEGRATED-PROVISIONAL`" in t["d1"]
          and "3 `INTEGRATED-BLOCKED`" in t["d1"], "D1 §8.1 integration-status tally is not 95/2/3")
    add("13D-64", "Screen availability agrees with P13D-05/P13D-13", p)

    # 65. Gap-register counts and classifications
    p = []
    gr = gap_rows_in(t["d1"])
    gstatus = Counter(clean(r[15]) for r in gr if len(r) > 15)
    grouped = {name: sum(gstatus[s] for s in statuses) for name, statuses in GAP_STATUS_GROUPS.items()}
    check(p, len(gr) == 16, f"gap register has {len(gr)} rows, expected 16")
    check(p, grouped["Fixed"] == 3, f"fixed gaps are {grouped['Fixed']}, expected 3")
    check(p, grouped["Open"] == 8, f"open gaps are {grouped['Open']}, expected 8")
    check(p, grouped["Deferred"] == 3, f"deferred gaps are {grouped['Deferred']}, expected 3")
    check(p, grouped["Owner-reserved"] == 2, f"owner-reserved gaps are {grouped['Owner-reserved']}, expected 2")
    open_parts = Counter({s: gstatus[s] for s in GAP_STATUS_GROUPS["Open"]})
    expected_open = Counter({"OPEN": 2, "OPEN (PROVISIONAL)": 3, "OPEN (BY GATE)": 1,
                             "OPEN (BY RULE)": 1, "OPEN (EXPECTED)": 1})
    check(p, open_parts == expected_open, f"open-gap composition is {dict(open_parts)}, expected {dict(expected_open)}")
    add("13D-65", "Gap-register totals and open-gap composition", p)

    # 66. Gap summaries agree across canonical records
    p = []
    sources: list[tuple[str, str]] = []
    sources.append(("D1", gap_summary_line(t["d1"])))
    d4_gap_line = next((ln for ln in t["d4"].splitlines() if ln.startswith("12. **Gap register**")), "")
    sources.append(("D4 §3", d4_gap_line))
    sources.append(("D4 P13D-21", " ".join(gate_cells(t["d4"], "P13D-21"))))
    sources.append(("D-236", next((ln for ln in t["decisions"].splitlines() if ln.startswith("| D-236 |")), "")))
    sources.append(("DD-284", next((ln for ln in t["dd"].splitlines() if ln.startswith("| DD-284 |")), "")))
    for name, key in (("AI_CONTEXT", "ai_context"), ("AI_HANDOFF", "ai_handoff"),
                      ("PROJECT_PROGRESS", "project_progress"), ("ROADMAP", "roadmap")):
        sources.append((name, gap_summary_line(t.get(key, ""))))
    log_gap = next((ln for ln in t.get("log", "").splitlines() if ln.startswith("- **Gaps:** 16")), "")
    sources.append(("log §94", log_gap))
    for label, line in sources:
        if not line:
            p.append(f"{label}: gap summary line missing")
            continue
        for token in ("8 open", "3 deferred", "2 owner-reserved"):
            check(p, token in line, f"{label}: gap summary missing {token!r}")
        for bad in ("5 open", "4 provisional/gated"):
            check(p, bad not in line, f"{label}: stale gap phrase {bad!r}")
    add("13D-66", "Gap summaries agree across D1/D4/registers/continuity", p)

    # 67. Working-tree audit-trail correction (§95) present, §94 preserved
    p = []
    log = t.get("log", "")
    check(p, "## 95. Prompt 13D-C1" in log, "progress log §95 correction record missing")
    check(p, "## 94. Prompt 13D" in log, "historical §94 record was removed or renumbered")
    check(p, "working tree was clean at start" in log, "historical §94 clean-tree statement was silently rewritten")
    for token in ("6 new files", "24 substantively modified existing files", "0 removed files",
                  "150", "154", "no application or prototype implementation content",
                  "Autonomous Decision Policy content remained unchanged"):
        check(p, token.lower() in log.lower(), f"§95 does not record audit-trail fact {token!r}")
    add("13D-67", "Working-tree audit trail corrected in §95 with §94 preserved", p)

    # 68. Integration-status agreement across D1 and D4
    p = []
    check(p, "95 `INTEGRATED`" in t["d1"] and "2 `INTEGRATED-PROVISIONAL`" in t["d1"]
          and "3 `INTEGRATED-BLOCKED`" in t["d1"], "D1 integration-status tally is not 95/2/3")
    joined05 = " ".join(gate_cells(t["d4"], "P13D-05"))
    check(p, "95 INTEGRATED" in joined05 and "2 INTEGRATED-PROVISIONAL" in joined05
          and "3 INTEGRATED-BLOCKED" in joined05, "P13D-05 integration-status tally is not 95/2/3")
    check(p, "92 `INTEGRATED`" not in t["d1"] and "96 / 100" not in t["d4"],
          "stale screen-integration tally remains")
    add("13D-68", "Integration-status tally agrees across D1 and D4", p)

    # 69. Stage 2 roadmap current Prompt 13 row reports 90 capabilities
    p = []
    row13 = prompt13_roadmap_row(t["stage2_roadmap"])
    check(p, bool(row13), "Stage 2 roadmap Prompt 13 row missing")
    check(p, "90 capabilities" in row13, "Stage 2 roadmap Prompt 13 row does not report 90 capabilities")
    for token in ("74 Complete", "8 Partial", "5 Blocked", "2 Open-Owner", "1 Candidate"):
        check(p, token in row13, f"Stage 2 roadmap Prompt 13 row omits Matrix B total {token!r}")
    add("13D-69", "Stage 2 roadmap reports 90 Matrix B capabilities", p)

    # 70. Stage 2 roadmap Matrix B totals agree with canonical D1 Matrix B
    p = []
    mb_counts2, mb_total2 = matrix_b_counts(t["d1"])
    check(p, bool(row13), "Stage 2 roadmap Prompt 13 row missing")
    for name in ("Complete", "Partial", "Blocked", "Open-Owner", "Candidate"):
        token = f"{mb_counts2[name]} {name}"
        check(p, token in row13, f"Stage 2 roadmap Matrix B total disagrees with D1: missing {token!r}")
    add("13D-70", "Stage 2 roadmap Matrix B totals agree with D1", p)

    # 71. Stage 2 roadmap screen totals agree with D1 and D4
    p = []
    for token in ("95 fully integrated", "2 INTEGRATED-PROVISIONAL", "3 INTEGRATED-BLOCKED",
                  "95 reachable", "5 unavailable", "4 Conditional-class", "1 Provisional-class"):
        check(p, token in row13, f"Stage 2 roadmap screen total missing {token!r}")
    check(p, "96 / 100" not in row13 and "4 blocked" not in row13,
          "Stage 2 roadmap retains a stale screen-integration total")
    add("13D-71", "Stage 2 roadmap screen totals agree with D1 and D4", p)

    # 72. Stage 2 roadmap gap totals agree with the canonical gap register
    p = []
    gr2 = gap_rows_in(t["d1"])
    g2 = Counter(clean(r[15]) for r in gr2 if len(r) > 15)
    grouped2 = {name: sum(g2[s] for s in statuses) for name, statuses in GAP_STATUS_GROUPS.items()}
    check(p, "16 gaps" in row13, "Stage 2 roadmap does not state 16 gaps")
    check(p, f"{grouped2['Fixed']} fixed" in row13, "Stage 2 roadmap fixed-gap total disagrees with D1")
    check(p, f"{grouped2['Open']} open" in row13, "Stage 2 roadmap open-gap total disagrees with D1")
    check(p, f"{grouped2['Deferred']} deferred" in row13, "Stage 2 roadmap deferred-gap total disagrees with D1")
    check(p, f"{grouped2['Owner-reserved']} owner-reserved" in row13,
          "Stage 2 roadmap owner-reserved gap total disagrees with D1")
    for bad in ("5 open", "4 provisional/gated"):
        check(p, bad not in row13, f"Stage 2 roadmap retains stale gap phrase {bad!r}")
    add("13D-72", "Stage 2 roadmap gap totals agree with D1", p)

    # 73. Stale 63-capability statement cannot remain in the current row
    p = []
    for bad in ("63-capability", "63 capabilities", "63-capability Matrix B"):
        check(p, bad not in row13, f"Stage 2 roadmap current row retains stale claim {bad!r}")
    add("13D-73", "Stage 2 roadmap current row has no stale 63-capability claim", p)

    # 74. Stage 2 roadmap cites the completion and correction records
    p = []
    check(p, "§94" in row13, "Stage 2 roadmap does not cite the Prompt 13D completion record §94")
    check(p, "§95" in row13, "Stage 2 roadmap does not cite the 13D-C1 correction record §95")
    add("13D-74", "Stage 2 roadmap cites §94 and §95", p)

    # 75. Historical/current distinction for superseded roadmap figures
    p = []
    for line in t["stage2_roadmap"].splitlines():
        if "63-capability" not in line and "63 capabilities" not in line:
            continue
        if line == row13:
            continue  # check 73 owns the current row
        low = line.lower()
        check(p, any(marker in low for marker in ("historical", "superseded", "earlier summary")),
              "Stage 2 roadmap contains an unlabelled superseded 63-capability reference")
    add("13D-75", "Superseded roadmap figures are labelled historical", p)

    return results


# ---------------------------------------------------------------- self-tests

def expect(mutated: dict[str, str], substring: str, case: str) -> bool:
    results = validate(mutated)
    joined = "\n".join(pb for _, _, probs in results for pb in probs)
    ok = substring in joined
    if not ok:
        print(f"[SELF-TEST FAIL] {case}: expected {substring!r} in problems")
    return ok


def validate_with_texts(t: dict[str, str]):
    results = validate(t)
    return results


def self_test() -> int:
    base = load()
    passed = 0
    total = 0

    def case(name: str, fn) -> None:
        nonlocal passed, total
        total += 1
        try:
            ok = fn()
        except Exception as exc:  # pragma: no cover - diagnostic path
            print(f"[SELF-TEST FAIL] {name}: crashed {exc!r}")
            ok = False
        if ok:
            passed += 1
            print(f"[SELF-TEST PASS] {name}")

    def missing_screen():
        m = deepcopy(base)
        m["d1"] = m["d1"].replace("| `SCR-050` | Agreement/treaty detail", "| `SCR-050x` | Agreement detail", 1)
        return expect(m, "Matrix A screens are not SCR-001..SCR-100", "missing screen row")
    case("missing screen row fails", missing_screen)

    def duplicate_screen():
        m = deepcopy(base)
        m["d1"] = m["d1"].replace("| `SCR-001` | Landing | Public | Mandatory | Public | SHELL |",
                                  "| `SCR-050` | Landing | Public | Mandatory | Public | SHELL |", 1)
        return expect(m, "Matrix A screens are not SCR-001..SCR-100", "duplicate screen row")
    case("duplicate screen row fails", duplicate_screen)

    def bad_screen_test():
        m = deepcopy(base)
        m["d3"] = m["d3"].replace("| `UAT-SCR-100` | `SCR-100` Admin roles", "| `UAT-SCR-101` | `SCR-100` Admin roles", 1)
        return expect(m, "screen tests are not UAT-SCR-001..100", "bad screen test id")
    case("invalid screen test id fails", bad_screen_test)

    def duplicate_uat():
        m = deepcopy(base)
        m["d3"] = m["d3"].replace("| `UAT-F-002` | Login routes", "| `UAT-F-001` | Login routes", 1)
        return expect(m, "duplicate UAT identifier", "duplicate UAT")
    case("duplicate UAT identifier fails", duplicate_uat)

    def unknown_uix():
        m = deepcopy(base)
        m["d1"] = m["d1"] + "\nSee `UIX-99`.\n"
        return expect(m, "undefined UIX reference", "undefined UIX")
    case("undefined UIX reference fails", unknown_uix)

    def missing_group():
        m = deepcopy(base)
        m["d2"] = m["d2"].replace("| Identity and purpose | `UIX-01`; Session and identity; establishes who is acting and which nation is active, for every authenticated surface. |", "", 1)
        return expect(m, "missing group row: Identity and purpose", "missing contract group")
    case("missing contract group row fails", missing_group)

    def bad_gate_status():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("| `P13D-01` | Governing policy and project baseline integrity |", "| `P13D-01` | Governing policy and project baseline integrity |", 1)
        m["d4"] = m["d4"].replace("| **PASS** | 10B defect pre-existed", "| **BOGUS** | 10B defect pre-existed", 1)
        return expect(m, "status 'BOGUS'", "invalid gate status")
    case("invalid gate status fails", bad_gate_status)

    def missing_gate():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("| `P13D-28` | Final Prompt 13 documentation-package readiness", "| `P13D-29` | Final readiness", 1)
        return expect(m, "gates are not P13D-01..28", "missing gate")
    case("missing gate row fails", missing_gate)

    def bad_gap_severity():
        m = deepcopy(base)
        m["d1"] = m["d1"].replace("| `GAP-13D-03` | Admin workspaces", "| `GAP-13D-03` | Admin workspaces", 1)
        m["d1"] = m["d1"].replace("| Low | Admin efficiency only", "| CRITICAL | Admin efficiency only", 1)
        return expect(m, "severity 'CRITICAL'", "invalid gap severity")
    case("invalid gap severity fails", bad_gap_severity)

    def missing_matrix_heading():
        m = deepcopy(base)
        m["d1"] = m["d1"].replace("## 9. Matrix B", "## 9. Reverse map", 1)
        return expect(m, "D1 missing section: ## 9. Matrix B", "missing matrix heading")
    case("missing matrix heading fails", missing_matrix_heading)

    def impossible_requirement():
        m = deepcopy(base)
        m["d1"] = m["d1"] + "\nSee `REQ-1300`.\n"
        return expect(m, "impossible requirement", "impossible REQ")
    case("out-of-range requirement fails", impossible_requirement)

    def invalid_screen_ref():
        m = deepcopy(base)
        m["d3"] = m["d3"] + "\nSee `SCR-101`.\n"
        return expect(m, "invalid screen(s): ['101']", "invalid screen reference")
    case("invalid screen reference fails", invalid_screen_ref)

    def executed_status():
        m = deepcopy(base)
        m["d3"] = m["d3"].replace("| `UAT-F-001` | First-time path: register, verify, create, onboard, digest | Functional | P0 |", "| `UAT-F-001` | First-time path: register, verify, create, onboard, digest | Functional | P0 |", 1)
        m["d3"] = m["d3"].replace("| SPECIFIED | 13C JRN-A |", "| PASSED | 13C JRN-A |", 1)
        return expect(m, "status is 'PASSED'", "executed status cell")
    case("executed test status fails", executed_status)

    def missing_pending():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("OWNER ACCEPTANCE PENDING", "OWNER ACCEPTED", 1)
        return expect(m, "does not mark 13D acceptance pending", "false acceptance")
    case("missing acceptance-pending marker fails", missing_pending)

    def false_acceptance():
        m = deepcopy(base)
        m["d4"] = m["d4"] + "\nPrompt 13D is OWNER ACCEPTED.\n"
        return expect(m, "claims owner acceptance of 13D", "false acceptance claim")
    case("false acceptance claim fails", false_acceptance)

    def broken_link():
        m = deepcopy(base)
        m["d1"] = m["d1"] + "\n[broken](does_not_exist_13d.md)\n"
        return expect(m, "broken link", "broken markdown link")
    case("broken markdown link fails", broken_link)

    def bad_total():
        m = deepcopy(base)
        m["d3"] = m["d3"].replace("| **Total** | **216** | 100 screen + 116 scenario |", "| **Total** | **217** | 100 screen + 116 scenario |", 1)
        return expect(m, "D3 does not state the 216 total", "test total mismatch")
    case("test total mismatch fails", bad_total)

    def duplicate_contract():
        m = deepcopy(base)
        m["d2"] = m["d2"].replace("### UIX-02 — Registration, verification and recovery", "### UIX-01 — Registration and recovery", 1)
        return expect(m, "not the expected 34", "duplicate UIX heading")
    case("duplicate contract heading fails", duplicate_contract)

    def missing_matrix_k():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("### 5.1 Matrix K", "### 5.1 Coverage", 1)
        return expect(m, "D4 missing section: ### 5.1 Matrix K", "missing Matrix K")
    case("missing Matrix K fails", missing_matrix_k)

    def bad_gate_tally():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("**27 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED**", "**28 PASS / 0 PARTIAL / 0 FAIL / 0 BLOCKED**", 1)
        return expect(m, "gate tally", "gate tally mismatch")
    case("gate tally mismatch fails", bad_gate_tally)

    def missing_decision():
        m = deepcopy(base)
        m["decisions"] = m["decisions"].replace("| D-234 |", "| D-934 |", 1)
        return expect(m, "DECISIONS.md does not record D-234", "missing decision")
    case("missing decision row fails", missing_decision)

    # Positive controls
    def positive_baseline():
        results = validate(base)
        problems = sum(len(probs) for _, _, probs in results)
        if problems:
            print(f"[SELF-TEST FAIL] positive baseline: {problems} problems on the corrected tree")
        return problems == 0
    case("positive baseline passes", positive_baseline)

    def positive_matrix_b():
        counts, total = matrix_b_counts(base["d1"])
        expected = Counter({"Complete": 74, "Partial": 8, "Blocked": 5,
                            "Open-Owner": 2, "Candidate": 1})
        ok = total == 90 and counts == expected
        if not ok:
            print(f"[SELF-TEST FAIL] positive Matrix B: {total}, {dict(counts)}")
        return ok
    case("positive Matrix B totals accepted", positive_matrix_b)

    # Negative controls for the 13D-C1 checks
    def bad_matrix_b_count():
        m = deepcopy(base)
        m["d1"] = m["d1"].replace(
            "| Registration and e-mail verification | B-03 ACC-023/024 | `SCR-002`, `SCR-006` | Complete |",
            "| Registration and e-mail verification | B-03 ACC-023/024 | `SCR-002`, `SCR-006` | Partial |", 1)
        return expect(m, "Matrix B totals", "Matrix B count corruption")
    case("Matrix B count corruption fails", bad_matrix_b_count)

    def bad_gate_11():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("90 capabilities; 0 silent absences", "63 capabilities; 0 silent absences", 1)
        return expect(m, "P13D-11", "P13D-11 stale capability claim")
    case("P13D-11 stale capability claim fails", bad_gate_11)

    def bad_matrix_a_status():
        m = deepcopy(base)
        m["b13_parent"] = m["b13_parent"].replace(
            "| `SCR-001` | Landing / public introduction | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-007; brand `13A-OQ-001/002`; k=5 | SPECIFIED |",
            "| `SCR-001` | Landing / public introduction | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-007; brand `13A-OQ-001/002`; k=5 | PROVISIONAL |", 1)
        return expect(m, "13B Matrix A statuses", "Matrix A status corruption")
    case("Matrix A status corruption fails", bad_matrix_a_status)

    def bad_screen_total():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("95 / 100 fully integrated", "96 / 100 fully integrated", 1)
        return expect(m, "Screens integrated", "D4 screen-total corruption")
    case("D4 screen-total corruption fails", bad_screen_total)

    def bad_gate_05():
        m = deepcopy(base)
        m["d4"] = m["d4"].replace("5 unavailable: 4 Conditional-class", "4 conditional/provisional screens", 1)
        return expect(m, "P13D-05", "P13D-05 four-screen claim")
    case("P13D-05 unavailable-screen corruption fails", bad_gate_05)

    def bad_gap_status():
        m = deepcopy(base)
        m["d1"] = m["d1"].replace("| **OPEN (BY RULE)** |", "| **DEFERRED** |", 1)
        return expect(m, "open gaps are", "gap-status corruption")
    case("gap-status corruption fails", bad_gap_status)

    def bad_d236():
        m = deepcopy(base)
        m["decisions"] = m["decisions"].replace("**8 open**", "**5 open**", 1)
        return expect(m, "D-236", "D-236 stale gap total")
    case("D-236 stale gap total fails", bad_d236)

    def bad_ai_context():
        m = deepcopy(base)
        m["ai_context"] = m["ai_context"].replace("8 open — 2 high-severity", "5 open — 2 high-severity", 1)
        return expect(m, "AI_CONTEXT", "AI_CONTEXT stale gap total")
    case("AI_CONTEXT stale gap total fails", bad_ai_context)

    def bad_audit_trail():
        m = deepcopy(base)
        m["log"] = m["log"].replace("24 substantively modified existing files", "22 substantively modified existing files", 1)
        return expect(m, "§95", "§95 audit-trail corruption")
    case("§95 audit-trail corruption fails", bad_audit_trail)

    # Stage 2 roadmap synchronization controls
    def positive_roadmap():
        row = prompt13_roadmap_row(base["stage2_roadmap"])
        ok = ("90 capabilities" in row and "8 open" in row and "§94" in row and "§95" in row)
        if not ok:
            print(f"[SELF-TEST FAIL] positive roadmap: {row[:200]}")
        return ok
    case("positive Stage 2 roadmap row accepted", positive_roadmap)

    def bad_roadmap_63():
        m = deepcopy(base)
        m["stage2_roadmap"] = m["stage2_roadmap"].replace("Matrix B 90 capabilities", "63-capability Matrix B", 1)
        return expect(m, "63-capability", "roadmap 63-corruption")
    case("roadmap 63-capability corruption fails", bad_roadmap_63)

    def bad_roadmap_missing_95():
        m = deepcopy(base)
        m["stage2_roadmap"] = m["stage2_roadmap"].replace("[§95](06_stage_2_progress_log.md)", "[§94](06_stage_2_progress_log.md)", 1)
        return expect(m, "§95", "roadmap missing §95")
    case("roadmap missing §95 fails", bad_roadmap_missing_95)

    def bad_roadmap_gap():
        m = deepcopy(base)
        m["stage2_roadmap"] = m["stage2_roadmap"].replace("16 gaps (3 fixed, 8 open", "16 gaps (3 fixed, 5 open", 1)
        return expect(m, "open-gap total", "roadmap gap-total corruption")
    case("roadmap gap-total corruption fails", bad_roadmap_gap)

    def historical_63_allowed():
        m = deepcopy(base)
        m["stage2_roadmap"] = m["stage2_roadmap"] + "\n> **Historical (superseded):** an earlier summary said 63-capability Matrix B.\n"
        results = validate(m)
        problems = sum(len(probs) for _, _, probs in results)
        if problems:
            print(f"[SELF-TEST FAIL] historical 63 allowed: {problems} problems")
        return problems == 0
    case("labelled historical 63-capability reference allowed", historical_63_allowed)

    def unlabelled_historical_63():
        m = deepcopy(base)
        m["stage2_roadmap"] = m["stage2_roadmap"] + "\nA current summary says 63-capability Matrix B.\n"
        return expect(m, "unlabelled superseded 63-capability reference", "unlabelled 63 reference")
    case("unlabelled superseded 63-capability reference fails", unlabelled_historical_63)

    print(f"\nSELF-TEST: {passed}/{total} regression cases passed")
    return 0 if passed == total else 1


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    t = load()
    results = validate(t)
    problems = sum(len(probs) for _, _, probs in results)
    for cid, name, probs in results:
        if probs:
            print(f"[FAIL] {cid} {name}")
            for pb in probs[:8]:
                print(f"       - {pb}")
            if len(probs) > 8:
                print(f"       ... {len(probs) - 8} more")
        else:
            print(f"[PASS] {cid} {name}")
    print(f"\nCHECKS: {len(results) - sum(1 for _, _, p in results if p)}/{len(results)} passed; "
          f"{sum(1 for _, _, p in results if p)} failed; {problems} problem(s)")
    print("RESULT: documentation quality only. No screen, component, route, API, database object or runtime UI exists; no test has executed.")
    return 0 if problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
