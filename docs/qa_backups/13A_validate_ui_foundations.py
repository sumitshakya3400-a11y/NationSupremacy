#!/usr/bin/env python3
"""Prompt 13A focused validator — UI research, architecture and design foundations.

Run:  python docs/qa_backups/13A_validate_ui_foundations.py
Self-test (seeded defects):  python docs/qa_backups/13A_validate_ui_foundations.py --self-test

Scope discipline. This validator grades *documentation quality only*: identifier
integrity, register arithmetic, citation resolution, governance synchronization and
hygiene across Prompt 13A's five canonical deliverables. It is not an acceptance
substitute — the `P13A-` gate register in
`docs/stage-2/research/13A_ui_requirements_open_questions_and_acceptance.md` is the
acceptance record, and every gate there is a documentation-level verdict. Nothing
here executes a UI, a test or a migration, and no check may be read as evidence that
any screen, component or framework exists.

Every expectation is *derived from the documents themselves* (row counts, tallies,
identifier sets, status blocks); no register number is hard-coded as truth without a
matching extraction from the file it describes.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
RESEARCH = DOCS / "stage-2" / "research"

DELIVERABLES = {
    "doc1": RESEARCH / "13A_politics_and_war_ui_research.md",
    "doc2": RESEARCH / "13A_ui_design_principles_and_architecture.md",
    "doc3": RESEARCH / "13A_master_screen_inventory.md",
    "doc4": RESEARCH / "13A_responsive_and_design_system_foundations.md",
    "doc5": RESEARCH / "13A_ui_requirements_open_questions_and_acceptance.md",
}
GOVERNANCE = {
    "ai_context": DOCS / "AI_CONTEXT.md",
    "ai_handoff": DOCS / "AI_HANDOFF.md",
    "progress": DOCS / "PROJECT_PROGRESS.md",
    "roadmap": DOCS / "ROADMAP.md",
    "decisions": DOCS / "DECISIONS.md",
    "register04": DOCS / "stage-2" / "04_approved_and_provisional_decisions.md",
    "unresolved": DOCS / "stage-2" / "05_unresolved_design_decisions.md",
    "tracker": DOCS / "stage-2" / "03_requirements_traceability.md",
    "outline": DOCS / "stage-2" / "02_master_game_design_bible_outline.md",
    "prompt_roadmap": DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md",
    "log": DOCS / "stage-2" / "06_stage_2_progress_log.md",
    "handoff_stage2": DOCS / "stage-2" / "00_stage_2_handoff.md",
    "prompt_index": DOCS / "prompts" / "INDEX.md",
}
ARCHIVE = DOCS / "prompts" / "prompt_13A_ui_research_architecture_and_design_foundations.md"

EXPECTED_SRC_TOTAL = 36
EXPECTED_SRC_PRIMARY = 28          # §3 rows 13A-SRC-001..028
EXPECTED_SRC_SUPPLEMENTARY = 2     # §4 rows 029 (Cyber Nations), 030 (eRepublik)
EXPECTED_SRC_NEGATIVE = 1          # §4 row 031 (NationStates, negative access check)
EXPECTED_SRC_BOUNDARY = 5          # §5 rows 032..036
EXPECTED_FND = 40
EXPECTED_BP = 28
EXPECTED_DR = 24
EXPECTED_PR = 16
EXPECTED_STATES = 13
EXPECTED_NAV_SECTIONS = 8
EXPECTED_SCREENS = 100
EXPECTED_OVERLAYS = 8
EXPECTED_DS = 15
EXPECTED_RD = 8
EXPECTED_UR = 48
EXPECTED_OQ = 16
EXPECTED_GATES = 24
TALLY_TEXT = "**Tally: 23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED.**"


def load() -> dict[str, str]:
    texts: dict[str, str] = {}
    for key, path in DELIVERABLES.items():
        texts[key] = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    for key, path in GOVERNANCE.items():
        texts[key] = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    texts["archive"] = ARCHIVE.read_text(encoding="utf-8", errors="replace") if ARCHIVE.exists() else ""
    return texts


def section(text: str, marker: str) -> str:
    """From the heading that starts with `marker` to the next `## ` heading."""
    i = text.find(marker)
    if i < 0:
        return ""
    nxt = text.find("\n## ", i + len(marker))
    return text[i:] if nxt < 0 else text[i:nxt]


def row_ids(text: str, family: str) -> list[int]:
    """Row-leading identifiers of one family, in document order."""
    pat = rf"^\|\s*`?{re.escape(family)}-(\d{{2,3}})`?\s*\|"
    return [int(m.group(1)) for m in re.finditer(pat, text, re.M)]


def row_cells(text: str, family: str) -> list[tuple[int, list[str]]]:
    out = []
    for line in text.splitlines():
        m = re.match(rf"^\|\s*`?{re.escape(family)}-(\d{{2,3}})`?\s*\|", line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append((int(m.group(1)), cells[1:]))
    return out


def contiguous(nums: list[int], start: int, end: int) -> bool:
    return nums == list(range(start, end + 1))


def status_value(text: str, key: str) -> str:
    """The value of one STATUS-block key, read inside the fenced block only."""
    m = re.search(r"<!-- STATUS:BEGIN -->(.*?)<!-- STATUS:END -->", text, re.S)
    if not m:
        return ""
    hit = re.search(rf"^{re.escape(key)}:[ \t]*([^\n]*)$", m.group(1), re.M)
    return hit.group(1).strip() if hit else ""


# ---------------------------------------------------------------------------
# checks — each returns a list of problems (empty == pass)
# ---------------------------------------------------------------------------

def c01_files(T):
    p = []
    for key, path in DELIVERABLES.items():
        if not path.exists():
            p.append(f"missing deliverable: {path.name}")
        elif len(T[key]) < 4000:
            p.append(f"{path.name} is implausibly short ({len(T[key])} chars)")
    return p


def c02_headers(T):
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        head = T[key][:2600]
        if "Prompt 13A" not in head:
            p.append(f"{key}: header does not identify Prompt 13A")
        if "2026-11-11" not in head:
            p.append(f"{key}: header carries no 2026-11-11 creation date")
        if not re.search(r"(?i)(no|not).{0,60}(implement|built|approved as a product commitment)"
                         r"|(approves no rule, screen|no screen is specified in final detail)", head):
            p.append(f"{key}: header states no research-level / no-implementation boundary")
    return p


def c03_src_register(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-SRC")
    p = []
    if not contiguous(nums, 1, EXPECTED_SRC_TOTAL):
        dup = [n for n in set(nums) if nums.count(n) > 1]
        missing = sorted(set(range(1, EXPECTED_SRC_TOTAL + 1)) - set(nums))
        p.append(f"13A-SRC rows are not 001..{EXPECTED_SRC_TOTAL} exactly once "
                 f"(duplicates={dup}, missing={missing}, rows={len(nums)})")
    s3, s4, s5 = (row_ids(section(t, "## 3."), "13A-SRC"),
                  row_ids(section(t, "## 4."), "13A-SRC"),
                  row_ids(section(t, "## 5."), "13A-SRC"))
    if not contiguous(s3, 1, EXPECTED_SRC_PRIMARY):
        p.append(f"§3 source rows are not 001..{EXPECTED_SRC_PRIMARY}: {s3}")
    if not contiguous(s4, 29, 29 + EXPECTED_SRC_SUPPLEMENTARY + EXPECTED_SRC_NEGATIVE - 1):
        p.append(f"§4 supplementary rows are not 029..031: {s4}")
    if not contiguous(s5, 32, 32 + EXPECTED_SRC_BOUNDARY - 1):
        p.append(f"§5 boundary rows are not 032..036: {s5}")
    return p


def c04_src_tokens(T):
    """No malformed or wrong-width identifier survives in the 13A package.

    Three families of defect are rejected: a non-digit inside the numeric part
    (`13A-SRC-03_yield`), a split number (`13A-SRC-02 6`), and a width that does
    not match the family (`13A-SRC-01`, `P13A-001`). `###` placeholders in the
    identifier-convention table are the notation itself and stay legal.
    """
    p = []
    three = ("SRC", "FND", "BP", "DR", "UR", "OQ")
    two = ("PR", "RD", "DS")
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        text = T[key]
        # any 13A-prefixed token whose family letters are followed by a digit is a
        # corrupted identifier (`13A-SR26 C-004`), whatever the rest looks like
        for m in re.finditer(r"13A-[A-Z]{1,4}\d", text):
            p.append(f"{key}: corrupted identifier at {text[max(0, m.start()-8):m.end()+6]!r}")
        for m in re.finditer(r"13A-([A-Z]{2,4})-([\d/,#]{1,60})", text):
            fam, num = m.group(1), m.group(2)
            if num.replace("/", "").replace(",", "").replace("#", "") == "":
                continue  # `13A-SRC-###` notation table
            width = 3 if fam in three else (2 if fam in two else 0)
            if width == 0:
                p.append(f"{key}: unknown 13A family 13A-{fam}-")
                continue
            parts = [x for x in re.split(r"[/,]", num) if x]
            bad = [x for x in parts if not re.fullmatch(rf"#{{3}}|\d{{{width}}}", x)]
            if bad:
                p.append(f"{key}: bad-width 13A-{fam}-{num!r} ({bad[0]!r} is not {width} digits)")
        for m in re.finditer(r"P13A-([\d/,#]{1,30})", text):
            parts = [x for x in re.split(r"[/,]", m.group(1)) if x]
            bad = [x for x in parts if x != "###" and not re.fullmatch(r"\d{2}", x)]
            if bad:
                p.append(f"{key}: bad-width P13A-{m.group(1)!r}")
        for m in re.finditer(r"(?<![\w-])(SCR|OVL)-([\d/,#]{1,80})", text):
            fam, num = m.group(1), m.group(2)
            width = 3 if fam == "SCR" else 2
            parts = [x for x in re.split(r"[/,]", num) if x]
            bad = [x for x in parts if x != "###" and not re.fullmatch(rf"\d{{{width}}}", x)]
            if bad:
                p.append(f"{key}: bad-width {fam}-{num!r} ({bad[0]!r})")
    return p


def c05_evidence_classes(T):
    """The class column is the source of truth; §10.1 must report what it says."""
    t = T["doc1"]
    rows = row_cells(section(t, "## 3."), "13A-SRC")
    if not rows:
        return ["§3 source rows could not be parsed"]
    counts = {"OBSERVED": 0, "DOCUMENTED": 0, "NOT-RETRIEVABLE": 0, "OTHER": 0}
    for _, cells in rows:
        cls = cells[1] if len(cells) > 1 else ""
        if cls.startswith("OBSERVED"):
            counts["OBSERVED"] += 1
        elif cls.startswith("DOCUMENTED"):
            counts["DOCUMENTED"] += 1
        elif cls.startswith("NOT-RETRIEVABLE"):
            counts["NOT-RETRIEVABLE"] += 1
        else:
            counts["OTHER"] += 1
            p = [f"row has no recognised evidence class: {cls[:40]!r}"]
            return p
    if sum(counts.values()) != EXPECTED_SRC_PRIMARY:
        return [f"§3 class rows total {sum(counts.values())}, expected {EXPECTED_SRC_PRIMARY}"]
    dist = section(t, "### 10.1")
    p = []
    for label, n in (("OBSERVED", counts["OBSERVED"]), ("DOCUMENTED", counts["DOCUMENTED"]),
                     ("NOT-RETRIEVABLE", counts["NOT-RETRIEVABLE"])):
        if not re.search(rf"\b{counts and n}\b `?{label}", dist):
            p.append(f"§10.1 does not state {n} {label} rows (computed from the class column)")
    if f"**{EXPECTED_SRC_PRIMARY + EXPECTED_SRC_BOUNDARY} are Politics & War**" not in dist:
        p.append("§10.1 does not report 33 Politics & War rows (28 primary + 5 boundary)")
    for claim in ("Of the 36 numbered source rows", "the two supplementary evidence rows",
                  "the supplementary negative access row"):
        if claim not in dist:
            p.append(f"§10.1 missing distribution claim {claim!r}")
    for cls in ("OBSERVED", "DOCUMENTED", "SECONDARY", "INFERRED", "NOT-RETRIEVABLE"):
        if cls not in section(t, "## 1."):
            p.append(f"§1 does not define the {cls} evidence class")
    # The acceptance register restates the same distribution on gate P13A-02; the
    # two statements must agree with the class column rather than with each other.
    gate02 = next((rest for num, rest in re.findall(
        r"^\|\s*`?P13A-(\d{2})`?\s*\|(.*)\|\s*$", section(T["doc5"], "## 5."), re.M) if num == "02"), "")
    for cls in ("OBSERVED", "DOCUMENTED", "NOT-RETRIEVABLE"):
        n = counts[cls]
        if n and not re.search(rf"\b{n} `?{cls}", gate02):
            p.append(f"P13A-02 does not restate the computed {n} {cls} rows")
    if gate02 and "33 of the 36" not in gate02:
        p.append("P13A-02 does not restate the 33-of-36 P&W distribution")
    return p


def c06_findings(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-FND")
    p = []
    if not contiguous(nums, 1, EXPECTED_FND):
        p.append(f"13A-FND rows are not 001..{EXPECTED_FND} exactly once ({len(nums)} rows)")
    for rid, cells in row_cells(section(t, "## 7."), "13A-FND"):
        if len(cells) != 3:
            p.append(f"13A-FND-{rid:03d} has {len(cells)} cells, expected 3 (finding, evidence, class)")
        elif not re.search(r"13A-SRC-\d{3}|SECONDARY|fixed constraint|boundary|constraint", cells[1]):
            p.append(f"13A-FND-{rid:03d} cites no evidence row")
        elif not re.search(r"(?i)OBSERVED|DOCUMENTED|SECONDARY|INFERRED|NOT-RETRIEVABLE|constraint|boundary",
                           cells[2]):
            p.append(f"13A-FND-{rid:03d} states no evidence class")
    return p


def c07_patterns(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-BP")
    p = []
    if not contiguous(nums, 1, EXPECTED_BP):
        p.append(f"13A-BP rows are not 001..{EXPECTED_BP} exactly once ({len(nums)} rows)")
    dispositions = 0
    for rid, cells in row_cells(section(t, "## 8."), "13A-BP"):
        if len(cells) != 3:
            p.append(f"13A-BP-{rid:03d} has {len(cells)} cells, expected 3")
            continue
        if re.search(r"(?i)\*\*(retain|adapt|reject|defer|provisional)", cells[1]):
            dispositions += 1
        else:
            p.append(f"13A-BP-{rid:03d} states no retain/adapt/reject disposition")
    if dispositions != EXPECTED_BP:
        p.append(f"only {dispositions} of {EXPECTED_BP} patterns carry a disposition")
    return p


def c08_recommendations(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-DR")
    p = []
    if not contiguous(nums, 1, EXPECTED_DR):
        p.append(f"13A-DR rows are not 001..{EXPECTED_DR} exactly once ({len(nums)} rows)")
    for rid, cells in row_cells(section(t, "## 9."), "13A-DR"):
        if len(cells) != 2:
            p.append(f"13A-DR-{rid:03d} has {len(cells)} cells, expected 2")
        elif not re.search(r"13A-SRC|13A-FND|13A-BP|REQ-|D-\d{3}|TR-\d|WEP-|WAR-|fixed", cells[1]):
            p.append(f"13A-DR-{rid:03d} states no basis")
    return p


def c09_benchmark(T):
    t = T["doc1"]
    p = []
    if "https://politicsandwar.com/" not in t:
        p.append("primary benchmark URL absent")
    if not re.search(r"(?i)primary (UI )?benchmark", t):
        p.append("the primary-benchmark role is not stated")
    if "Prohibited categories" not in t:
        p.append("the prohibited-comparator-category paragraph is missing")
    if "approves no rule, screen, component, number or implementation" not in t:
        p.append("the inputs-only boundary sentence is missing")
    if "2026-11-11" not in t:
        p.append("no retrieval date recorded")
    return p


def c10_principles(T):
    t = T["doc2"]
    p = []
    nums = row_ids(t, "13A-PR")
    if not contiguous(nums, 1, EXPECTED_PR):
        p.append(f"13A-PR rows are not 01..{EXPECTED_PR:02d} exactly once ({len(nums)} rows)")
    nav = [l for l in section(t, "## 5.").splitlines() if re.match(r"^\|\s*\d+\s*\|", l)]
    if len(nav) != EXPECTED_NAV_SECTIONS:
        p.append(f"navigation register has {len(nav)} sections, expected {EXPECTED_NAV_SECTIONS}")
    states = [l for l in section(t, "## 6.").splitlines() if re.match(r"^\|\s*\*\*", l)]
    if len(states) != EXPECTED_STATES:
        p.append(f"application-state register has {len(states)} states, expected {EXPECTED_STATES}")
    for term in ("PROVISIONAL_BLOCK", "suppressed"):
        if term not in section(t, "## 6."):
            p.append(f"state register does not name {term}")
    for term in ("mapless", "Network View", "War Operations Board"):
        if term not in t:
            p.append(f"architecture text does not use the fixed term {term!r}")
    if "remain reserved" not in t or "D-203" not in t:
        p.append("brand/visual-identity values are not recorded as owner-reserved (D-203)")
    if "no implementation, no visual asset, no component built" not in t:
        p.append("the no-implementation boundary sentence is missing")
    return p


def _scr_rows(T):
    t = T["doc3"]
    return row_cells(section(t, "## 2."), "SCR")


def c11_screen_ids(T):
    nums = row_ids(T["doc3"], "SCR")
    if not contiguous(nums, 1, EXPECTED_SCREENS):
        dup = [n for n in set(nums) if nums.count(n) > 1]
        missing = sorted(set(range(1, EXPECTED_SCREENS + 1)) - set(nums))
        return [f"SCR rows are not 001..{EXPECTED_SCREENS} exactly once "
                f"(rows={len(nums)}, duplicates={dup}, missing={missing})"]
    bad = [rid for rid, cells in _scr_rows(T) if len(cells) != 5]
    if bad:
        return [f"SCR rows with the wrong cell count (expected 6 columns): {bad[:8]}"]
    return []


def c12_screen_tally(T):
    rows = _scr_rows(T)
    if len(rows) != EXPECTED_SCREENS:
        return [f"screen register parsed {len(rows)} rows, expected {EXPECTED_SCREENS}"]
    tally = {"mandatory": 0, "admin": 0, "conditional": 0, "provisional": 0}
    conditional, provisional = [], []
    for rid, cells in rows:
        cls = cells[3].strip("*").strip()
        if cls == "Mandatory":
            tally["mandatory"] += 1
        elif cls == "Mandatory (admin)":
            tally["admin"] += 1
        elif cls.lower().startswith("conditional"):
            tally["conditional"] += 1
            conditional.append(rid)
        elif cls.lower().startswith("provisional"):
            tally["provisional"] += 1
            provisional.append(rid)
        else:
            return [f"unknown screen class {cls!r} on SCR-{rid:03d}"]
    p = []
    if tally != {"mandatory": 85, "admin": 10, "conditional": 4, "provisional": 1}:
        p.append(f"computed class tally {tally} != the registered 85/10/4/1")
    arith = section(T["doc3"], "## 7.")
    if conditional and "SCR-020/038/039/077" not in arith:
        p.append("§7 does not name the computed Conditional set")
    if sorted(conditional) != [20, 38, 39, 77]:
        p.append(f"Conditional screens are {conditional}, expected [20, 38, 39, 77]")
    if provisional != [68]:
        p.append(f"Provisional screens are {provisional}, expected [68]")
    for claim in ("Player-facing: 90", "Administrative: 10 (Mandatory)", "Total screens **100**",
                  "overlays 8", "sections 8"):
        if claim not in arith:
            p.append(f"§7 arithmetic line missing {claim!r}")
    return p


def c13_admin_family(T):
    rows = _scr_rows(T)
    admin = [rid for rid, cells in rows if cells[1] == "Admin"]
    p = []
    if admin != list(range(91, 101)):
        p.append(f"Parent=Admin rows are {admin[:12]}…, expected SCR-091..100")
    if not re.search(r"SCR-091\u2026SCR-100", T["doc3"]):
        p.append("the administrative family is not registered as SCR-091…SCR-100")
    return p


def c14_hierarchy(T):
    t = T["doc3"]
    p = []
    if "```mermaid" not in t:
        p.append("no Mermaid hierarchy diagram")
    else:
        start = t.index("```mermaid")
        graph = t[start:t.index("```", start + 10)]
        if "graph" not in graph[:120].lower() and "flowchart" not in graph[:120].lower():
            p.append("the Mermaid block declares no graph/flowchart")
        # The diagram addresses screens by their SCR numeric suffix, so the eight
        # section nodes plus the two roots are the checkable structure.
        for label in ("Public shell", "Authenticated shell", "Admin 091-100"):
            if label not in graph:
                p.append(f"hierarchy diagram omits {label!r}")
        for n in range(1, 9):
            if not re.search(rf"{n} (Home|Economy|Cities|Politics|Foreign|War|World|Account)", graph):
                p.append(f"hierarchy diagram omits navigation section {n}")
    nums = row_ids(t, "OVL")
    if not contiguous(nums, 1, EXPECTED_OVERLAYS):
        p.append(f"OVL rows are not 01..{EXPECTED_OVERLAYS} exactly once ({len(nums)} rows)")
    if not re.search(r"(?i)cross-system transition", t):
        p.append("no cross-system transition table")
    if not re.search(r"(?i)navigation-quality audit|seven-risk", t):
        p.append("the navigation-quality audit is missing")
    return p


def c15_responsive_ds(T):
    t = T["doc4"]
    p = []
    ds = row_ids(t, "13A-DS")
    if not contiguous(ds, 1, EXPECTED_DS):
        p.append(f"13A-DS rows are not 01..{EXPECTED_DS} exactly once ({len(ds)} rows)")
    rd_rows = row_ids(t, "13A-RD")
    if not contiguous(rd_rows, 2, EXPECTED_RD):
        p.append(f"13A-RD table rows are not 02..{EXPECTED_RD}: {rd_rows}")
    if "13A-RD-01" not in t:
        p.append("13A-RD-01 is not recorded anywhere in the responsive foundations")
    if "13A-RD-01" in [f"13A-RD-{n:02d}" for n in rd_rows]:
        p.append("13A-RD-01 must be a prose rule, not a duplicated table row")
    coverage = (("token discipline", r"(?i)token"),
                ("WCAG thresholds", r"(?i)WCAG"),
                ("the six-number-type register law", r"(?i)six-number|number-type"),
                ("the component state matrix", r"focus-visible"))
    for term, pat in coverage:
        if not re.search(pat, t):
            p.append(f"design-system foundations do not cover {term!r}")
    return p


def c16_responsive_boundaries(T):
    t = T["doc4"]
    p = []
    if "same game with the same rules" not in t:
        p.append("the same-rules-every-device guarantee is missing")
    if "Not owner-approved numbers" not in t or "Provisional breakpoints" not in t:
        p.append("breakpoints are not labelled provisional, not owner-approved")
    if "no CSS, no framework, no component implementation" not in t:
        p.append("the no-CSS/no-framework boundary is missing")
    if "no compliance claim is made" not in t:
        p.append("the no-accessibility-compliance-claim boundary is missing")
    for oq in ("13A-OQ-001", "13A-OQ-002"):
        if oq not in t:
            p.append(f"owner-reserved brand question {oq} is not referenced")
    return p


def c17_ur_register(T):
    t = T["doc5"]
    hits = re.findall(r"^\|\s*`?UR-(\d{3})`?\s*\|", t, re.M)
    nums = [int(h) for h in hits]
    p = []
    if not contiguous(sorted(set(nums)), 1, EXPECTED_UR):
        p.append(f"UR identifiers are not 001..{EXPECTED_UR} ({len(set(nums))} distinct)")
    for n in range(1, EXPECTED_UR + 1):
        if nums.count(n) != 2:
            p.append(f"UR-{n:03d} appears as a row {nums.count(n)} times, expected 2 "
                     "(candidate register + dependency ledger)")
            break
    return p


def c18_open_questions(T):
    nums = row_ids(section(T["doc5"], "## 4."), "OQ")
    if not contiguous(nums, 1, EXPECTED_OQ):
        return [f"OQ rows are not 001..{EXPECTED_OQ} exactly once ({len(nums)} rows)"]
    buckets = 0
    body = section(T["doc5"], "## 4.")
    for label in ("owner", "technical", "design", "legal", "research", "calibration", "scope"):
        if re.search(rf"(?i){label}", body):
            buckets += 1
    if buckets < 5:
        return [f"the open-question register exposes only {buckets} decision buckets"]
    return []


def _gate_rows(T):
    return re.findall(r"^\|\s*`?P13A-(\d{2})`?\s*\|(.*)\|\s*$", section(T["doc5"], "## 5."), re.M)


def c19_gate_rows(T):
    p = []
    nums = [int(m.group(1)) for m in re.finditer(r"^\|\s*`?P13A-(\d{2})`?\s*\|",
                                                 section(T["doc5"], "## 5."), re.M)]
    if not contiguous(nums, 1, EXPECTED_GATES):
        dup = [n for n in set(nums) if nums.count(n) > 1]
        missing = sorted(set(range(1, EXPECTED_GATES + 1)) - set(nums))
        p.append(f"P13A gates are not 01..{EXPECTED_GATES} exactly once "
                 f"(rows={len(nums)}, duplicates={dup}, missing={missing})")
    for num, rest in _gate_rows(T):
        cells = [c.strip() for c in rest.split("|")]
        results = [c for c in cells if re.fullmatch(
            r"\*\*(PASS|PARTIAL|FAIL|BLOCKED|NOT RUN|NOT APPLICABLE)\*\*", c)]
        if len(results) != 1:
            p.append(f"P13A-{num} has {len(results)} bolded result cells, expected exactly 1")
    return p


def c20_gate_tally(T):
    p = []
    counts = {"PASS": 0, "PARTIAL": 0, "FAIL": 0, "BLOCKED": 0}
    partial_ids = []
    for num, rest in _gate_rows(T):
        cells = [c.strip() for c in rest.split("|")]
        for c in cells:
            m = re.fullmatch(r"\*\*(PASS|PARTIAL|FAIL|BLOCKED)\*\*", c)
            if m:
                counts[m.group(1)] += 1
                if m.group(1) == "PARTIAL":
                    partial_ids.append(num)
    claimed = re.search(r"\*\*Tally: (\d+) PASS / (\d+) PARTIAL / (\d+) FAIL / (\d+) BLOCKED\.\*\*",
                        T["doc5"])
    if not claimed:
        return ["the gate register states no bolded PASS/PARTIAL/FAIL/BLOCKED tally"]
    got = tuple(int(x) for x in claimed.groups())
    want = (counts["PASS"], counts["PARTIAL"], counts["FAIL"], counts["BLOCKED"])
    if got != want:
        p.append(f"stated tally {got} disagrees with the computed gate results {want}")
    if claimed.group(0) != TALLY_TEXT:
        p.append(f"tally sentence is not the canonical {TALLY_TEXT!r}")
    if partial_ids != ["10"]:
        p.append(f"PARTIAL gates are {partial_ids}, expected exactly ['10'] (P13A-10)")
    return p


def c21_identifier_policy(T):
    t = T["doc5"]
    p = []
    if "REQ-870" not in t or "reserved" not in t:
        p.append("REQ-870 is not recorded as reserved for Prompt 13B")
    if not re.search(r"(?i)no global `?REQ-`?|allocated no global", t):
        p.append("the no-global-REQ-allocation policy is not stated")
    if not re.search(r"(?i)no global `?UD-`?|UD-0\d\d`? remain Open", t) \
            and "resolved none" not in t:
        p.append("the UD non-resolution duty is not stated")
    if "none is implemented" not in t:
        p.append("the acceptance register does not say none is implemented")
    return p


def c22_req_citations(T):
    defined = {int(m.group(1)) for m in re.finditer(r"^\|\s*REQ-(\d{3})\s*\|", T["tracker"], re.M)}
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        for line in T[key].splitlines():
            for m in re.finditer(r"REQ-(\d{3})\b", line):
                n = int(m.group(1))
                if n in defined:
                    continue
                if n == 870 and re.search(r"(?i)reserved|frontier", line):
                    continue
                p.append(f"{key}: unresolved REQ-{n:03d} in {line[:70]!r}")
    return p


def c23_decision_citations(T):
    d_ids = {int(m.group(1)) for m in re.finditer(r"^\| D-(\d{3}) \|", T["decisions"], re.M)}
    ud_ids = {int(m.group(1)) for m in re.finditer(r"^\|\s*`?UD-(\d{3})`?\s*\|", T["unresolved"], re.M)}
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        text = T[key]
        for m in re.finditer(r"\bD-(\d{3})\b", text):
            if int(m.group(1)) not in d_ids:
                p.append(f"{key}: cites D-{m.group(1)} which is not in DECISIONS.md")
        for m in re.finditer(r"\bUD-(\d{3})\b", text):
            if int(m.group(1)) not in ud_ids:
                p.append(f"{key}: cites UD-{m.group(1)} which is not in the unresolved register")
    seen = set()
    return [x for x in p if not (x in seen or seen.add(x))]


def c24_family_citations(T):
    """Every 13A-/SCR-/OVL-/P13A- citation resolves to a registered row."""
    defined = {
        "13A-SRC": set(row_ids(T["doc1"], "13A-SRC")),
        "13A-FND": set(row_ids(T["doc1"], "13A-FND")),
        "13A-BP": set(row_ids(T["doc1"], "13A-BP")),
        "13A-DR": set(row_ids(T["doc1"], "13A-DR")),
        "13A-PR": set(row_ids(T["doc2"], "13A-PR")),
        "SCR": set(row_ids(T["doc3"], "SCR")),
        "OVL": set(row_ids(T["doc3"], "OVL")),
        "13A-RD": set(row_ids(T["doc4"], "13A-RD")) | {1},
        "13A-DS": set(row_ids(T["doc4"], "13A-DS")),
        "13A-OQ": set(row_ids(T["doc5"], "OQ")),
        "13A-UR": set(row_ids(T["doc5"], "UR")),
        "P13A": set(row_ids(T["doc5"], "P13A")),
    }
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        for m in re.finditer(r"\b(13A-SRC|13A-FND|13A-BP|13A-DR|13A-PR|SCR|OVL|13A-RD|13A-DS|"
                             r"13A-OQ|13A-UR|P13A)-0*(\d{1,3})\b", T[key]):
            fam, num = m.group(1), int(m.group(2))
            if num not in defined[fam]:
                p.append(f"{key}: dangling citation {m.group(0)} (no registered row)")
    return p


def c25_decision_records(T):
    p = []
    rows = re.findall(r"^\| D-(\d{3}) \| (2026-11-11) \|", T["decisions"], re.M)
    got = sorted(int(n) for n, _ in rows)
    if got != list(range(198, 206)):
        p.append(f"DECISIONS.md rows dated 2026-11-11 are {got}, expected D-198..D-205")
    dd = row_ids(T["register04"], "DD")
    if not contiguous(dd, 1, 253):
        p.append(f"stage-2/04 DD rows are not contiguous to DD-253 (max={max(dd) if dd else None})")
    for n in range(246, 254):
        if f"| DD-{n:03d} |" not in T["register04"]:
            p.append(f"DD-{n:03d} row missing from the mirrored position register")
    return p


def c26_status_blocks(T):
    p = []
    keys = ("ai_context", "ai_handoff", "progress")
    for k in keys:
        if status_value(T[k], "stage_2_next_prompt") != "13B":
            p.append(f"{k}: stage_2_next_prompt is "
                     f"{status_value(T[k], 'stage_2_next_prompt')!r}, expected 13B")
        if status_value(T[k], "decisions_range") != "D-001..D-205":
            p.append(f"{k}: decisions_range is {status_value(T[k], 'decisions_range')!r}")
        if status_value(T[k], "status_updated") != "2026-11-11":
            p.append(f"{k}: status_updated is {status_value(T[k], 'status_updated')!r}")
    ui = [status_value(T[k], "ui_foundations") for k in keys]
    if not all(ui):
        p.append("ui_foundations status key missing from at least one continuity file")
    elif len(set(ui)) != 1:
        p.append("ui_foundations status entries disagree across the three continuity files")
    if "Prompt 13A" not in T["ai_context"][:6000] or "Prompt 13A" not in T["progress"][:6000]:
        p.append("no Prompt 13A current-status block at the head of AI_CONTEXT/PROJECT_PROGRESS")
    return p


def c27_roadmap_registration(T):
    p = []
    if not re.search(r"^## 87\. Prompt 13A", T["log"], re.M):
        p.append("progress log has no §87 for Prompt 13A")
    if "Executed split (2026-11-11; D-198)" not in T["prompt_roadmap"]:
        p.append("the Stage 2 roadmap does not register the executed 13A/13B split")
    if "13A" not in T["prompt_roadmap"] or "13B" not in T["prompt_roadmap"]:
        p.append("the Stage 2 roadmap prompt table does not carry both 13A and 13B")
    b13 = section(T["outline"], "### B-13")
    if "`21_interface_and_player_journeys.md`" not in b13:
        p.append("outline B-13 does not use the D-198 path 21_interface_and_player_journeys.md")
    if "20_interface_and_player_journeys.md" in b13:
        p.append("outline B-13 still presents the superseded 20_ path as current")
    return p


def c28_prompt_archive(T):
    p = []
    if not ARCHIVE.exists():
        return ["the Prompt 13A instruction is not archived under docs/prompts/"]
    head = T["archive"][:2000]
    if "Archival provenance" not in head:
        p.append("the archive carries no provenance paragraph")
    if "# PROMPT 13A" not in T["archive"][:400]:
        p.append("the archive does not preserve the original title line")
    if "prompt_13A_ui_research_architecture_and_design_foundations.md" not in T["prompt_index"]:
        p.append("docs/prompts/INDEX.md has no Prompt 13A row")
    if re.search(r"SHA-256 `[0-9a-f]{64}`", T["prompt_index"]) is None:
        p.append("docs/prompts/INDEX.md records no stored-bytes digest")
    return p


def c29_protected_statuses(T):
    """Prompt 13A may not have quietly advanced any preserved 12A/12B/12C status."""
    joined = "\n".join(T[key] for key in ("ai_context", "ai_handoff", "progress", "roadmap",
                                         "handoff_stage2", "log", "doc5"))
    p = []
    required = (
        "D-014",
        "DEFERRED BY OWNER",
        "NOT CLOSED",
        "P12B-14",
        "P12B-16",
        "P12B-23",
        "16 PASS / 2 PARTIAL / 2 BLOCKED",
        "378",
        "owner acceptance GRANTED",
    )
    for token in required:
        if token not in joined:
            p.append(f"protected-status token absent from the synchronized record: {token!r}")
    if not re.search(r"(?i)(R7|independent acceptance).{0,160}(not accepted|not independently)",
                     joined):
        p.append("R7's outstanding independent acceptance is not preserved")
    if "five residual weaknesses" not in joined and "five further bypass classes" not in joined:
        p.append("the five known R7 residual weaknesses are not preserved")
    for obligation in ("0005", "audit trigger", "tests/sql"):
        if obligation not in joined:
            p.append(f"outstanding security obligation {obligation!r} is not preserved")
    return p


def c30_hygiene(T):
    """Line-anchored conflict markers only.

    Progress log §86 quotes the markers as evidence of the *repaired* baseline
    defect; a quoted token inside a sentence is documentation, while a marker at
    column zero is an unrepaired hunk.
    """
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5", "ai_context", "ai_handoff", "progress",
                "roadmap", "decisions", "register04", "tracker", "outline", "prompt_roadmap",
                "log", "handoff_stage2", "archive"):
        for line in T[key].splitlines():
            if re.match(r"^<<<<<<<[ \n]|^=======$|^>>>>>>>[ \n]", line):
                p.append(f"{key}: unrepaired conflict-marker line {line[:30]!r}")
    return p


def c31_links(T):
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        base = RESEARCH
        for m in re.finditer(r"\]\(([^)\s#]+)(?:#[^)]*)?\)", T[key]):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (base / target).exists():
                p.append(f"{key}: unresolved relative link {target!r}")
    return p


def c32_no_overclaim(T):
    p = []
    banned = (r"(?i)\b(?:ui|frontend|screen|component|framework)\b[^.\n]{0,30}"
              r"\b(?:has been|was|is)\s+implemented",
              r"(?i)deployed the (?:ui|frontend)",
              r"(?i)accessibility conformance (?:verified|achieved|certified)",
              r"(?i)conformance verified",
              r"(?i)breakpoints? (?:are |is )?owner-approved",
              r"(?i)brand identity (?:is|was) decided")
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5", "log"):
        for pat in banned:
            for m in re.finditer(pat, T[key]):
                clause = T[key][max(0, m.start() - 120):m.start()]
                # "No appeal mechanic, migration or UI is implemented" is the boundary
                # sentence itself; only an unqualified assertion is an over-claim.
                if re.search(r"(?i)\b(?:no|not|nothing|never|non)\b[^.\n]{0,110}$", clause):
                    continue
                p.append(f"{key}: over-claim {m.group(0)[:60]!r}")
    if "## 87." not in T["log"]:
        p.append("progress log §87 missing")
    return p


CHECKS = [
    ("13A-01", "the five 13A deliverables exist at canonical paths", c01_files),
    ("13A-02", "every deliverable header records Prompt 13A and its boundary", c02_headers),
    ("13A-03", "source register is 001–036 contiguous with correct section membership", c03_src_register),
    ("13A-04", "no malformed or wrong-width 13A identifier token", c04_src_tokens),
    ("13A-05", "evidence-class distribution is computed and §10.1 reports it", c05_evidence_classes),
    ("13A-06", "findings register 001–040, every row cites evidence", c06_findings),
    ("13A-07", "benchmark-pattern register 001–028 with a disposition each", c07_patterns),
    ("13A-08", "recommendation register 001–024 with a basis each", c08_recommendations),
    ("13A-09", "P&W identity, prohibited categories and inputs-only boundary", c09_benchmark),
    ("13A-10", "16 principles, 8 navigation sections, 13 application states", c10_principles),
    ("13A-11", "screen identifiers are unique and contiguous SCR-001–100", c11_screen_ids),
    ("13A-12", "class tally and §7 arithmetic agree with the register", c12_screen_tally),
    ("13A-13", "administrative family is SCR-091–100 behind the Admin parent", c13_admin_family),
    ("13A-14", "hierarchy diagram, overlay register and navigation audit present", c14_hierarchy),
    ("13A-15", "design-system 01–15 and responsive 01–08 rules registered", c15_responsive_ds),
    ("13A-16", "same-rules guarantee, provisional breakpoints, no-CSS boundary", c16_responsive_boundaries),
    ("13A-17", "UR-001–048 appear in both the register and the ledger", c17_ur_register),
    ("13A-18", "open questions OQ-001–016 with bucket coverage", c18_open_questions),
    ("13A-19", "P13A-01–24 unique, one bolded result per gate", c19_gate_rows),
    ("13A-20", "stated gate tally equals the computed results (23/1/0/0)", c20_gate_tally),
    ("13A-21", "identifier policy: no global REQ/UD, REQ-870 reserved", c21_identifier_policy),
    ("13A-22", "every cited REQ- resolves in the requirements tracker", c22_req_citations),
    ("13A-23", "every cited D-/UD- resolves in the decision registers", c23_decision_citations),
    ("13A-24", "every cited 13A-/SCR-/OVL-/P13A- id resolves in its home register", c24_family_citations),
    ("13A-25", "D-198–205 and DD-246–253 are recorded and mirrored", c25_decision_records),
    ("13A-26", "STATUS blocks agree: 13B, D-001..D-205, ui_foundations identical", c26_status_blocks),
    ("13A-27", "log §87, roadmap split registration and outline B-13 path", c27_roadmap_registration),
    ("13A-28", "Prompt 13A instruction archived and indexed with its digest", c28_prompt_archive),
    ("13A-29", "12A/12B/12C/R7/R8/security statuses preserved unchanged", c29_protected_statuses),
    ("13A-30", "no merge-conflict markers in the touched files", c30_hygiene),
    ("13A-31", "relative links inside the deliverables resolve", c31_links),
    ("13A-32", "no implementation, conformance or owner-approval over-claims", c32_no_overclaim),
]


def run(T):
    results = []
    for cid, name, fn in CHECKS:
        try:
            problems = fn(T)
        except Exception as exc:  # a crashing check is a failure, never a pass
            problems = [f"check raised {type(exc).__name__}: {exc}"]
        results.append((cid, name, problems))
    return results


# ---------------------------------------------------------------------------
# self-test — seeded defects must be caught by the named check
# ---------------------------------------------------------------------------

def fx_dup_scr(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-050`"))
    T["doc3"] = t.replace(line, line.replace("SCR-050", "SCR-049", 1), 1)
    return "13A-11"


def fx_gate_swap(T):
    lines = T["doc5"].splitlines()
    idx = next(i for i, l in enumerate(lines) if re.match(r"^\|\s*`?P13A-05`?\s*\|", l))
    lines[idx] = lines[idx].replace("**PASS**", "**FAIL**", 1)
    T["doc5"] = "\n".join(lines) + "\n"
    return "13A-20"


def fx_class_flip(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-002`"))
    T["doc3"] = t.replace(line, line.replace("| B-03 | Mandatory |", "| B-03 | Conditional |"), 1)
    return "13A-12"


def fx_fake_req(T):
    T["doc2"] = T["doc2"] + "\nDepends on REQ-991 which the tracker does not carry.\n"
    return "13A-22"


def fx_src_removed(T):
    t = T["doc1"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-SRC-014`"))
    T["doc1"] = t.replace(line + "\n", "", 1)
    return "13A-03"


def fx_status_reverted(T):
    T["ai_context"] = T["ai_context"].replace("stage_2_next_prompt: 13B", "stage_2_next_prompt: 12C", 1)
    return "13A-26"


def fx_conflict_marker(T):
    T["doc4"] = T["doc4"] + "\n<<<<<<< HEAD\nlocal edit\n=======\nowner edit\n>>>>>>>> branch\n"
    return "13A-30"


def fx_pr_row_dropped(T):
    t = T["doc2"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-PR-16`") or l.startswith("| 13A-PR-16"))
    T["doc2"] = t.replace(line + "\n", "", 1)
    return "13A-10"


def fx_boundary_removed(T):
    T["doc4"] = T["doc4"].replace("no CSS, no framework, no component implementation",
                                  "CSS and framework are recorded as 13B inputs")
    return "13A-16"


def fx_overclaim(T):
    T["doc4"] = (T["doc4"] + "\nThe UI framework has been implemented and accessibility "
                               "conformance verified against WCAG.\n")
    return "13A-32"


def fx_ui_key_split(T):
    T["progress"] = T["progress"].replace(
        "ui_foundations: Prompt 13A complete", "ui_foundations: Prompt 13B pending", 1)
    return "13A-26"


def fx_broken_link(T):
    T["doc1"] = T["doc1"].replace("(13A_ui_design_principles_and_architecture.md)",
                                  "(13A_ui_design_principles_and_architectur.md)", 1)
    return "13A-31"


def fx_decision_missing(T):
    t = T["decisions"]
    line = next(l for l in t.splitlines() if l.startswith("| D-201 |"))
    T["decisions"] = t.replace(line + "\n", "", 1)
    return "13A-25"


def fx_dangling_family_ref(T):
    T["doc3"] = T["doc3"] + "\nSee `SCR-141` for the omitted surface.\n"
    return "13A-24"


SELF_TEST_FIXTURES = (
    fx_dup_scr, fx_gate_swap, fx_class_flip, fx_fake_req, fx_src_removed, fx_status_reverted,
    fx_conflict_marker, fx_pr_row_dropped, fx_boundary_removed, fx_overclaim, fx_ui_key_split,
    fx_broken_link, fx_decision_missing, fx_dangling_family_ref,
)


def main(argv: list[str]) -> int:
    # Windows consoles default to cp1252; the registers quote French/emoji-free but
    # typographic punctuation (— § ≤), so reporting must never crash on encoding.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    T = load()
    if "--self-test" in argv:
        bad = 0
        by_id = {cid: (name, fn) for cid, name, fn in CHECKS}
        for fx in SELF_TEST_FIXTURES:
            mutated = dict(T)
            expected = fx(mutated)
            results = run(mutated)
            caught = [cid for cid, _, probs in results if probs]
            ok = expected in caught
            detail = next((by_id[cid][1](mutated)[0][:110] for cid in caught if cid == expected), "undetected")
            print(f"SELF-TEST {'PASS' if ok else 'FAIL'}  {fx.__name__} -> "
                  f"expected {expected}: {detail}")
            bad += 0 if ok else 1
        print(f"SELF-TEST: {len(SELF_TEST_FIXTURES) - bad}/{len(SELF_TEST_FIXTURES)} seeded defects detected")
        return 0 if bad == 0 else 1

    results = run(T)
    failed = [(cid, name, probs) for cid, name, probs in results if probs]
    print("13A UI-foundations validator — documentation quality only")
    print(f"CHECKS: {len(results) - len(failed)}/{len(results)} passed; {len(failed)} failed")
    for cid, name, probs in failed:
        print(f"\nFAILED {cid}: {name}")
        for pr in probs[:12]:
            print(f"  - {pr}")
        if len(probs) > 12:
            print(f"  - … {len(probs) - 12} more")
    if not failed:
        print("RESULT: PASS at the documentation level. No screen, component, framework, "
              "migration or implementation exists, and no Prompt 13A gate is evidence of one.")
        return 0
    print("\nRESULT: FAIL — Prompt 13A documentation-quality checks not satisfied")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
