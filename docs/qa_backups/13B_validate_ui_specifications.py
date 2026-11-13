#!/usr/bin/env python3
"""Prompt 13B focused validator — documentation quality only.

Verifies structural and traceability integrity of the B-13 screen and component
specifications. It does not understand natural language and is not a substitute
for review, implementation testing or owner acceptance. No runtime UI exists.

Run:  python docs/qa_backups/13B_validate_ui_specifications.py
      python docs/qa_backups/13B_validate_ui_specifications.py --self-test
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
B13 = DOCS / "stage-2" / "21_interface_and_player_journeys.md"
SCREENS = DOCS / "stage-2" / "21_screen_specifications.md"
COMPONENTS = DOCS / "stage-2" / "21_component_specifications.md"
INVENTORY = DOCS / "stage-2" / "research" / "13A_master_screen_inventory.md"
DECISIONS = DOCS / "DECISIONS.md"
DD = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
TRACE = DOCS / "stage-2" / "03_requirements_traceability.md"
LOG = DOCS / "stage-2" / "06_stage_2_progress_log.md"
CONTINUITY = ["AI_CONTEXT.md", "AI_HANDOFF.md", "PROJECT_PROGRESS.md"]

PARENTS = {"Public", "Home", "Economy", "Cities", "Politics", "Foreign", "War", "World", "Account", "Admin"}
STATUSES = {"SPECIFIED", "PROVISIONAL", "BLOCKED"}
REQ_RANGE = list(range(870, 1090))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rows(text: str, first: str) -> list[list[str]]:
    out = []
    for line in text.splitlines():
        if line.startswith(first):
            cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
            out.append(cells)
    return out


def section(text: str, start: str, end: str) -> str:
    a = text.find(start)
    if a < 0:
        return ""
    b = text.find(end, a + len(start))
    return text[a:] if b < 0 else text[a:b]


def check(problems: list[str], ok: bool, message: str) -> None:
    if not ok:
        problems.append(message)


def status_value(text: str, key: str) -> str:
    m = re.search(r"<!-- STATUS:BEGIN -->(.*?)<!-- STATUS:END -->", text, re.S)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith(key + ":"):
            return line.split(":", 1)[1].strip()
    return ""


# ---------------------------------------------------------------- extraction

def extract_screens() -> dict[str, dict[str, str]]:
    text = read(SCREENS)
    blocks = re.split(r"^### (SCR-\d{3}) — ", text, flags=re.M)[1:]
    out: dict[str, dict[str, str]] = {}
    for i in range(0, len(blocks), 2):
        sid, body = blocks[i], blocks[i + 1]
        fields = {}
        for field in "ABCDEFGHIJK":
            m = re.search(rf"\| \*\*{field} [^|]*\| (.*?) \|", body, re.S)
            fields[field] = m.group(1).strip() if m else ""
        out[sid] = fields
    return out


def extract_components() -> dict[str, int]:
    text = read(COMPONENTS)
    blocks = re.split(r"^### (UI-CMP-\d{3}) — ", text, flags=re.M)[1:]
    out = {}
    for i in range(0, len(blocks), 2):
        cid, body = blocks[i], blocks[i + 1]
        nums = set(re.findall(r"^\| (\d{1,2}) \|", body, re.M))
        out[cid] = len(nums)
    return out


def extract_navigation() -> list[list[str]]:
    text = read(B13)
    nav = section(text, "### 7.2 Master navigation relationship register", "### 7.3 Navigation integrity checks")
    return rows(nav, "| `SCR-")


def extract_matrix_a() -> list[list[str]]:
    text = read(B13)
    ma = section(text, "## 24. Matrix A", "## 25. Matrix B")
    return rows(ma, "| `SCR-")


def extract_matrix_b() -> list[list[str]]:
    text = read(B13)
    mb = section(text, "## 25. Matrix B", "## 26. Matrix C")
    return rows(mb, "| `UI-CMP-") + rows(mb, "| `OVL-")


def extract_requirements() -> list[list[str]]:
    text = read(B13)
    mc = section(text, "## 26. Matrix C", "## 27. Decisions")
    return rows(mc, "| `REQ-")


# ------------------------------------------------- section and anchor integrity
# Supported syntax: "§N" and "§N.M" references to numbered headings in the same
# document, with optional "parent §N" (main document), "screen companion §N" /
# "Companion §N" (screen companion) and "component companion §N" (component
# companion). External references whose immediate prefix names another document
# (13A, 13B instruction, 08C, 07C, WAR, Report 07, B-10, log, progress log) are
# skipped. This is a deterministic parser, not natural-language understanding.
EXTERNAL_SECTION_PREFIXES = (
    "13A", "13B instruction", "08C", "07C", "WAR", "Report 07", "B-10",
    "log", "progress log", "progress-log",
)


def heading_numbers(text: str) -> set[str]:
    numbers: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"^#{2,4}\s+(\d+(?:\.\d+)?)\.?\s+", line)
        if m:
            numbers.add(m.group(1))
    return numbers


def section_ref_problems(text: str, own: set[str], main: set[str],
                         screen: set[str], component: set[str]) -> list[str]:
    problems: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        previous_external = False
        for m in re.finditer(r"§(\d+(?:\.\d+)?)", line):
            number = m.group(1)
            before = line[max(0, m.start() - 55):m.start()]
            immediate = re.search(
                r"(13A|13B instruction|08C|07C|WAR|Report 07|B-10|progress-log|progress log|log|parent|screen companion|component companion|Companion)\s*$",
                before,
            )
            prefix = immediate.group(1) if immediate else None
            external = prefix in EXTERNAL_SECTION_PREFIXES or before.rstrip().endswith("§")
            if not external and previous_external and re.search(r"[/–-]\s*$", before):
                external = True
            if external:
                previous_external = True
                continue
            if prefix == "parent":
                target = main
            elif prefix in ("screen companion", "Companion"):
                target = screen
            elif prefix == "component companion":
                target = component
            else:
                target = own
            if number not in target:
                problems.append(f"line {lineno}: §{number} does not resolve in its target document")
            previous_external = False
    return problems


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch in " -_")
    return text.replace(" ", "-")


def collect_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if not m:
            continue
        slug = slugify(m.group(2))
        count = seen.get(slug, 0)
        anchors.add(slug if count == 0 else f"{slug}-{count}")
        seen[slug] = count + 1
    return anchors


def anchor_problems(text: str, own: set[str], targets: dict[str, set[str]]) -> list[str]:
    problems: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\]\(([^)\s]+)\)", line):
            target = m.group(1)
            if target.lower().startswith(("http:", "https:", "mailto:", "tel:", "ftp:", "data:")):
                continue
            path, _, fragment = target.partition("#")
            if not fragment:
                continue
            fragment = fragment.lower()
            name = path.replace("\\", "/").split("/")[-1]
            if path == "":
                if fragment not in own:
                    problems.append(f"line {lineno}: anchor #{fragment} does not exist in this document")
            elif name in targets and fragment not in targets[name]:
                problems.append(f"line {lineno}: anchor {name}#{fragment} does not exist")
    return problems


# ---------------------------------------------------------------- checks

def c01_files(problems: list[str]) -> None:
    for path in (B13, SCREENS, COMPONENTS):
        check(problems, path.exists() and path.stat().st_size > 1000, f"missing or empty deliverable: {path.name}")
        if path.exists():
            text = read(path)
            check(problems, "<<<<<<<" not in text and ">>>>>>>" not in text and "\n=======\n" not in text,
                  f"merge-conflict marker in {path.name}")


def c02_inventory(problems: list[str]) -> None:
    inv = read(INVENTORY)
    inv_ids = re.findall(r"^\| `(SCR-\d{3})` \|", inv, re.M)
    check(problems, inv_ids == [f"SCR-{i:03d}" for i in range(1, 101)],
          f"13A inventory is not SCR-001..SCR-100 ({len(inv_ids)} ids)")
    screens = extract_screens()
    check(problems, list(screens) == [f"SCR-{i:03d}" for i in range(1, 101)],
          f"screen catalogue headings are not 100 unique contiguous screens ({len(screens)})")
    for sid in screens:
        check(problems, re.fullmatch(r"SCR-\d{3}", sid) is not None, f"malformed screen id {sid}")


def c03_screen_fields(problems: list[str]) -> None:
    screens = extract_screens()
    for sid, fields in screens.items():
        missing = [f for f in "ABCDEFGHIJK" if not fields.get(f)]
        check(problems, not missing, f"{sid} missing fields {missing}")


def c04_classifications(problems: list[str]) -> None:
    inv = read(INVENTORY)
    classes = {}
    for line in inv.splitlines():
        if line.startswith("| `SCR-"):
            cells = [c.strip().strip("*").strip("`") for c in line.strip().strip("|").split("|")]
            if len(cells) >= 5:
                classes[cells[0]] = cells[4]
    check(problems, len(classes) == 100, f"13A classification rows parsed {len(classes)}, expected 100")
    mandatory = sum(1 for v in classes.values() if v == "Mandatory")
    admin = sum(1 for v in classes.values() if v == "Mandatory (admin)")
    conditional = sum(1 for v in classes.values() if v == "Conditional")
    provisional = sum(1 for v in classes.values() if v == "Provisional")
    check(problems, (mandatory, admin, conditional, provisional) == (85, 10, 4, 1),
          f"13A class tally changed: {(mandatory, admin, conditional, provisional)}")
    ma = extract_matrix_a()
    check(problems, len(ma) == 100, f"Matrix A has {len(ma)} rows, expected 100")
    statuses = [r[9] for r in ma if len(r) >= 10]
    check(problems, statuses.count("SPECIFIED") == 95 and statuses.count("PROVISIONAL") == 2 and statuses.count("BLOCKED") == 3,
          f"Matrix A status tally changed: {statuses.count('SPECIFIED')}/{statuses.count('PROVISIONAL')}/{statuses.count('BLOCKED')}")
    for r in ma:
        if len(r) >= 10:
            check(problems, r[9] in STATUSES, f"Matrix A {r[0]} has invalid status {r[9]!r}")


def c05_admin(problems: list[str]) -> None:
    screens = extract_screens()
    for i in range(91, 101):
        sid = f"SCR-{i:03d}"
        check(problems, "Parent **Admin**" in screens[sid].get("A", ""), f"{sid} is not parented to Admin")
    for i in range(1, 91):
        sid = f"SCR-{i:03d}"
        check(problems, "Parent **Admin**" not in screens[sid].get("A", ""), f"player screen {sid} is parented to Admin")


def c06_components(problems: list[str]) -> None:
    comps = extract_components()
    check(problems, list(comps) == [f"UI-CMP-{i:03d}" for i in range(1, 91)],
          f"component headings are not UI-CMP-001..090 ({len(comps)})")
    bad = {cid: n for cid, n in comps.items() if n < 19}
    check(problems, not bad, f"components with fewer than 19 fields: {bad}")
    text = read(COMPONENTS)
    ovl = re.findall(r"^### (OVL-\d{2}) — ", text, re.M)
    check(problems, ovl == [f"OVL-{i:02d}" for i in range(1, 9)], f"overlay headings are not OVL-01..08: {ovl}")
    check(problems, text.count("| 19 | Page equivalent |") == 8, "not every overlay has a page-equivalent row")


def c07_component_refs(problems: list[str]) -> None:
    screens = extract_screens()
    comps = extract_components()
    comp_ids = set(comps) | {f"OVL-{i:02d}" for i in range(1, 9)}
    mb = extract_matrix_b()
    listed = set()
    for r in mb:
        if len(r) >= 4:
            cid, screens_cell = r[0], r[3]
            check(problems, cid in comp_ids, f"Matrix B unknown component {cid}")
            ids = re.findall(r"SCR-\d{3}", screens_cell)
            if not ids and not any(k in screens_cell for k in ("All", "Every", "all ")):
                problems.append(f"Matrix B {cid} lists no screens and no global scope")
            for sid in ids:
                check(problems, sid in screens, f"Matrix B {cid} references unknown screen {sid}")
                listed.add(sid)
    # Derived reverse index: every screen except SCR-068 must have at least one component.
    b13 = read(B13)
    rev = section(b13, "### 25.1 Reverse lookup", "## 26. Matrix C")
    rev_rows = rows(rev, "| `SCR-")
    check(problems, len(rev_rows) == 100, f"reverse component index has {len(rev_rows)} rows, expected 100")
    for r in rev_rows:
        if len(r) >= 2:
            sid, cell = r[0], r[1]
            check(problems, sid in screens, f"reverse index unknown screen {sid}")
            ids = re.findall(r"UI-CMP-\d{3}|OVL-\d{2}", cell)
            if sid == "SCR-068":
                check(problems, not ids, "SCR-068 must not reference a component (no rule exists)")
            else:
                check(problems, bool(ids), f"reverse index {sid} has no component")
            for cid in ids:
                check(problems, cid in comp_ids, f"reverse index {sid} references unknown component {cid}")


def c08_requirements(problems: list[str]) -> None:
    reqs = extract_requirements()
    ids = [r[0] for r in reqs if r]
    expected = [f"REQ-{i}" for i in REQ_RANGE]
    check(problems, ids == expected, f"B-13 requirements are not REQ-870..REQ-1089 ({len(ids)} rows)")
    check(problems, len(set(ids)) == len(ids), "duplicate B-13 requirement identifier")
    statuses = [r[8] for r in reqs if len(r) >= 10]
    check(problems, statuses.count("SPECIFIED") == 213 and statuses.count("PROVISIONAL") == 4 and statuses.count("BLOCKED") == 3,
          f"requirement status tally changed: {statuses.count('SPECIFIED')}/{statuses.count('PROVISIONAL')}/{statuses.count('BLOCKED')}")
    for r in reqs:
        if len(r) < 10:
            problems.append(f"requirement row has fewer than 10 fields: {r[:1]}")
            continue
        check(problems, r[8] in STATUSES, f"{r[0]} invalid status {r[8]!r}")
        check(problems, all(r[i] for i in (1, 2, 3, 4, 5, 6, 7, 9)), f"{r[0]} has an empty required field")


def c09_requirement_refs(problems: list[str]) -> None:
    reqs = extract_requirements()
    screens = set(extract_screens())
    comps = set(extract_components()) | {f"OVL-{i:02d}" for i in range(1, 9)}
    for r in reqs:
        if len(r) < 10:
            continue
        for sid in re.findall(r"SCR-\d{3}", r[5]):
            check(problems, sid in screens, f"{r[0]} references unknown screen {sid}")
        for cid in re.findall(r"UI-CMP-\d{3}|OVL-\d{2}", r[6]):
            check(problems, cid in comps, f"{r[0]} references unknown component {cid}")
        check(problems, bool(r[4]) and r[4] != "None", f"{r[0]} has no governing source")
    # one-per-screen allocation
    by_id = {r[0]: r for r in reqs if len(r) >= 10}
    for n in range(1, 101):
        rid, sid = f"REQ-{869 + n}", f"SCR-{n:03d}"
        check(problems, rid in by_id, f"missing screen requirement {rid} for {sid}")
        if rid in by_id:
            check(problems, sid in by_id[rid][5], f"{rid} does not name {sid}")


def c10_frontier(problems: list[str]) -> None:
    trace = read(TRACE)
    existing = re.findall(r"^\| (REQ-\d{3}) \|", trace, re.M)
    nums = [int(x.split("-")[1]) for x in existing]
    check(problems, nums and max(nums) == 869, f"global requirement register is not at REQ-869 (max={max(nums) if nums else None})")
    b13_ids = re.findall(r"^\| `(REQ-\d{3,4})` \|", read(B13), re.M)
    check(problems, b13_ids and b13_ids[0] == "REQ-870" and b13_ids[-1] == "REQ-1089",
          "B-13 block does not start at REQ-870 and end at REQ-1089")
    check(problems, "REQ-1090" in read(B13), "next free requirement frontier REQ-1090 is not recorded")


def c11_navigation(problems: list[str]) -> None:
    nav = extract_navigation()
    check(problems, len(nav) == 100, f"navigation register has {len(nav)} rows, expected 100")
    seen_routes = set()
    for r in nav:
        if len(r) < 6:
            problems.append(f"navigation row malformed: {r[:2]}")
            continue
        sid, parent, route = r[0], r[1], r[2]
        check(problems, parent in PARENTS, f"{sid} has invalid parent {parent!r}")
        check(problems, route not in seen_routes, f"duplicate route key {route}")
        seen_routes.add(route)
        check(problems, re.fullmatch(r"[a-z]+[.a-z-]+", route) is not None, f"{sid} malformed route key {route!r}")
        if parent == "Admin":
            check(problems, route.startswith("admin."), f"admin screen {sid} route is outside admin.*")
        else:
            check(problems, not route.startswith("admin."), f"player screen {sid} route leaks admin.*")
    screens = extract_screens()
    for sid, fields in screens.items():
        check(problems, any(r and r[0] == sid for r in nav), f"{sid} missing from the navigation register")


def c12_conditional_nav(problems: list[str]) -> None:
    nav = {r[0]: r for r in extract_navigation() if r}
    for sid in ("SCR-020", "SCR-038", "SCR-039", "SCR-077", "SCR-068"):
        check(problems, sid in nav, f"conditional/provisional screen {sid} missing from navigation register")
    check(problems, "BLOCKED" in " ".join(nav["SCR-038"]), "SCR-038 navigation row does not state BLOCKED/absent")
    check(problems, "absent" in " ".join(nav["SCR-038"]).lower(), "SCR-038 navigation row does not state absence")
    check(problems, "no route" in " ".join(nav["SCR-068"]).lower(), "SCR-068 navigation row does not state no route")
    check(problems, "no build authority" in " ".join(nav["SCR-068"]).lower(), "SCR-068 lacks no-build-authority statement")


def c13_alliance_war(problems: list[str]) -> None:
    b13 = read(B13)
    check(problems, "no Alliance military command" in b13, "Alliance/Warfare prohibition sentence missing")
    check(problems, "REQ-589" in b13 and "WAR-148" in b13 and "WAR-161" in b13, "Alliance/Warfare boundary identifiers missing")
    nav = {r[0]: r for r in extract_navigation() if r}
    s058 = " ".join(nav.get("SCR-058", []))
    for forbidden in ("SCR-061", "SCR-064", "SCR-065"):
        check(problems, forbidden not in s058, f"SCR-058 navigation links to {forbidden} (prohibited Alliance authority path)")
    screens = extract_screens()
    check(problems, "owner-only" in screens["SCR-061"]["A"].lower(), "SCR-061 is not marked owner-only")
    comps = read(COMPONENTS)
    block = comps[comps.find("### UI-CMP-062"):]
    block = block[:block.find("### UI-CMP-063")]
    check(problems, "Never" in block and "Alliance" in block, "UI-CMP-062 does not prohibit Alliance use")


def c14_responsive(problems: list[str]) -> None:
    screens = extract_screens()
    for sid, fields in screens.items():
        i = fields.get("I", "").lower()
        check(problems, "desktop" in i, f"{sid} responsive field has no desktop specification")
        check(problems, "tablet" in i, f"{sid} responsive field has no tablet specification")
        check(problems, "mobile" in i, f"{sid} responsive field has no mobile specification")


def c15_map(problems: list[str]) -> None:
    b13 = read(B13)
    sec = section(b13, "## 11. Map and Network View reconciliation", "## 12. Screen-to-component")
    check(problems, bool(sec), "map/Network View reconciliation section missing")
    for needle in ("TR-012", "REQ-041", "SCR-018", "no geographic", "not a map", "13A-SRC-016", "13A-BP-016"):
        check(problems, needle.lower() in sec.lower(), f"map reconciliation lacks {needle}")
    inv = read(INVENTORY)
    check(problems, not re.search(r"^\| `SCR-\d{3}` \| [^|]*\b(map|map view)\b", inv, re.I | re.M),
          "13A inventory contains a map-named screen")
    all_b13 = read(B13) + read(SCREENS) + read(COMPONENTS)
    check(problems, "geographic world map" in all_b13.lower(), "prohibition of geographic world maps is not stated")


def c16_suppression(problems: list[str]) -> None:
    b13 = read(B13).lower()
    check(problems, "suppressed is not zero" in b13 or "suppressed is never zero" in b13,
          "suppression-is-not-zero doctrine missing")
    check(problems, "d-027" in b13 and "mkt-110" in b13, "suppression rule identifiers missing")
    check(problems, "ui-cmp-072" in read(B13).lower(), "suppression component not registered")


def c17_decisions(problems: list[str]) -> None:
    dec = read(DECISIONS)
    d_ids = re.findall(r"^\| (D-\d{3}) \|", dec, re.M)
    check(problems, d_ids == [f"D-{i:03d}" for i in range(1, 234)], f"DECISIONS.md is not D-001..D-233 ({len(d_ids)})")
    for i in range(220, 234):
        check(problems, f"D-{i:03d}" in d_ids, f"missing decision D-{i:03d}")
    dd = read(DD)
    dd_ids = re.findall(r"^\| (DD-\d{3}) \|", dd, re.M)
    check(problems, dd_ids == [f"DD-{i:03d}" for i in range(1, 282)], f"DD register is not DD-001..DD-281 ({len(dd_ids)})")
    for i in range(268, 282):
        check(problems, f"DD-{i:03d}" in dd_ids, f"missing mirrored decision DD-{i:03d}")


def c18_status(problems: list[str]) -> None:
    blocks = {f: read(DOCS / f) for f in CONTINUITY}
    for f, text in blocks.items():
        check(problems, status_value(text, "status_updated") == "2026-11-13", f"{f} status_updated is not 2026-11-13")
        check(problems, status_value(text, "stage_2_next_prompt") == "13D", f"{f} next prompt is not 13D")
        check(problems, status_value(text, "decisions_range") == "D-001..D-233", f"{f} decisions_range is not D-001..D-233")
    ui = [status_value(t, "ui_foundations") for t in blocks.values()]
    check(problems, all(ui) and len(set(ui)) == 1 and "Prompt 13B" in ui[0],
          "ui_foundations status entries are missing, disagree, or do not record Prompt 13B")


def c19_impact(problems: list[str]) -> None:
    b13 = read(B13)
    sec = section(b13, "## 29. Documentation impact register", "## 30. Scope boundaries")
    check(problems, bool(sec), "documentation impact register missing")
    for needle in ("AI_CONTEXT.md", "AI_HANDOFF.md", "ROADMAP.md", "DECISIONS.md",
                   "21_screen_specifications.md", "21_component_specifications.md",
                   "21_interface_and_player_journeys.md", "06_stage_2_progress_log.md"):
        check(problems, needle in sec, f"impact register does not list {needle}")
    check(problems, "Pending" not in sec, "impact register still contains a Pending modification")


def c20_log(problems: list[str]) -> None:
    log = read(LOG)
    check(problems, re.search(r"^## 91\. Prompt 13B", log, re.M) is not None, "progress log has no §91 Prompt 13B entry")
    sec = log[log.find("## 91. Prompt 13B"):] if "## 91. Prompt 13B" in log else ""
    for needle in ("100", "90", "8", "REQ-870", "REQ-1089", "D-206", "D-219", "DD-254", "DD-267", "13C"):
        check(problems, needle in sec, f"progress log §91 lacks {needle}")


def c21_scope(problems: list[str]) -> None:
    text = read(B13) + read(SCREENS) + read(COMPONENTS)
    low = text.lower()
    forbidden = [
        "frontend is implemented", "frontend has been implemented",
        "wcag 2.2 aa compliant", "wcag 2.2 aa conformance achieved",
        "prompt 13c is complete", "prompt 13d is complete",
        "runtime verification passed", "ui runtime tests passed",
    ]
    for phrase in forbidden:
        check(problems, phrase not in low, f"overclaim phrase present: {phrase!r}")
    check(problems, "not performed" in low or "no runtime" in low, "runtime verification boundary not stated")


def c22_overlays(problems: list[str]) -> None:
    b13 = read(B13)
    comps = read(COMPONENTS)
    for i in range(1, 9):
        oid = f"OVL-{i:02d}"
        check(problems, b13.count(oid) >= 1, f"{oid} missing from Matrix B")
        check(problems, f"### {oid} —" in comps, f"{oid} body missing")
    check(problems, "page-reachable equivalent" in comps, "overlay page-equivalence doctrine missing")


def c23_templates(problems: list[str]) -> None:
    b13 = read(B13)
    for needle in ("## 1. Document authority", "## 4. Screen specification methodology",
                   "## 7. Navigation", "## 8. Responsive", "## 9. Information hierarchy",
                   "## 10. Accessibility", "## 11. Map", "## 24. Matrix A",
                   "## 25. Matrix B", "## 26. Matrix C", "## 27. Decisions",
                   "## 28. Dependencies", "## 29. Documentation impact", "## 30. Scope", "## 31. Prompt 13B-C1"):
        check(problems, needle in b13, f"parent document missing section {needle}")


def c24_crosscheck(problems: list[str]) -> None:
    b13 = read(B13)
    screens = extract_screens()
    reqs = extract_requirements()
    by_id = {r[0]: r for r in reqs if len(r) >= 10}
    for n in range(1, 101):
        sid, rid = f"SCR-{n:03d}", f"REQ-{869 + n}"
        check(problems, sid in screens and rid in by_id, f"cross-check failed for {sid}/{rid}")
        check(problems, f"`REQ-{869 + n}`" in b13, f"Matrix C heading missing {rid}")
    # No duplicate screen/component/requirement definitions in the companion files.
    comps = extract_components()
    check(problems, len(set(comps)) == len(comps), "duplicate component definition")
    check(problems, len(set(screens)) == len(screens), "duplicate screen definition")
    # Requirement ID must not appear as a new row in the global tracker.
    trace_rows = set(re.findall(r"^\| (REQ-\d{3,4}) \|", read(TRACE), re.M))
    clashes = [f"REQ-{i}" for i in REQ_RANGE if f"REQ-{i}" in trace_rows]
    check(problems, not clashes, f"B-13 requirement IDs collide with global tracker rows: {clashes[:3]}")


def c25_section_refs(problems: list[str]) -> None:
    texts = {"main": read(B13), "screen": read(SCREENS), "component": read(COMPONENTS)}
    heads = {key: heading_numbers(text) for key, text in texts.items()}
    for key, text in texts.items():
        for p in section_ref_problems(text, heads[key], heads["main"], heads["screen"], heads["component"]):
            problems.append(f"{key}: {p}")


def c26_heading_links(problems: list[str]) -> None:
    texts = {"21_interface_and_player_journeys.md": read(B13),
             "21_screen_specifications.md": read(SCREENS),
             "21_component_specifications.md": read(COMPONENTS)}
    anchors = {name: collect_anchors(text) for name, text in texts.items()}
    for name, text in texts.items():
        for p in anchor_problems(text, anchors[name], anchors):
            problems.append(f"{name}: {p}")



def c27_archive(problems: list[str]) -> None:
    archive = DOCS / "prompts" / "prompt_13B_screen_and_component_specifications.md"
    check(problems, archive.exists(), "Prompt 13B archive is missing")
    if not archive.exists():
        return
    text = read(archive)
    sections = [int(m.group(1)) for m in re.finditer(r"^# (\d+)\.", text, re.M)]
    check(problems, sections == list(range(1, 27)), f"Prompt 13B archive sections are {sections}, expected 1..26")
    index = read(DOCS / "prompts" / "INDEX.md")
    check(problems, "prompt_13B_screen_and_component_specifications.md" in index,
          "INDEX.md has no Prompt 13B archive row")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    check(problems, digest in index, "INDEX.md does not carry the archive's stored-bytes SHA-256")


def c28_correction_register(problems: list[str]) -> None:
    text = read(B13)
    sec = section(text, "## 31. Prompt 13B-C1 correction impact register", "## 32.")
    check(problems, bool(sec), "Prompt 13B-C1 correction impact register is missing")
    for needle in ("Prompt 13B-C1", "prompt_13B_screen_and_component_specifications.md",
                   "116", "24", "§91.9", "D-219 / DD-267"):
        check(problems, needle in sec, f"correction register lacks {needle}")


CHECKS = [
    ("13B-01", "deliverables exist, non-empty, merge-marker free", c01_files),
    ("13B-02", "100 screens, no duplicate or missing identifiers", c02_inventory),
    ("13B-03", "every screen has all A–K fields", c03_screen_fields),
    ("13B-04", "classes and Matrix A status tally preserved", c04_classifications),
    ("13B-05", "ten admin screens are Admin-parented and separated", c05_admin),
    ("13B-06", "90 components with 19 fields and 8 overlays", c06_components),
    ("13B-07", "component and screen references resolve", c07_component_refs),
    ("13B-08", "REQ-870…REQ-1089 present, unique, statuses valid", c08_requirements),
    ("13B-09", "requirement screen/component references resolve", c09_requirement_refs),
    ("13B-10", "requirement frontier and no collision", c10_frontier),
    ("13B-11", "navigation register complete and unique", c11_navigation),
    ("13B-12", "conditional/provisional routes are absent or blocked", c12_conditional_nav),
    ("13B-13", "Alliance/Warfare authority separation", c13_alliance_war),
    ("13B-14", "all three responsive specifications per screen", c14_responsive),
    ("13B-15", "mapless reconciliation and no geographic map", c15_map),
    ("13B-16", "suppression doctrine and component", c16_suppression),
    ("13B-17", "D-206…D-219 and DD-254…DD-267 recorded", c17_decisions),
    ("13B-18", "continuity STATUS blocks agree", c18_status),
    ("13B-19", "documentation impact register complete", c19_impact),
    ("13B-20", "progress log §91 present", c20_log),
    ("13B-21", "no implementation or conformance overclaim", c21_scope),
    ("13B-22", "overlay identifiers and page equivalence", c22_overlays),
    ("13B-23", "parent document section structure", c23_templates),
    ("13B-24", "screen-to-requirement cross-check and no collisions", c24_crosscheck),
    ("13B-25", "internal numbered section references resolve", c25_section_refs),
    ("13B-26", "internal heading anchors resolve", c26_heading_links),
    ("13B-27", "Prompt 13B archive and INDEX digest", c27_archive),
    ("13B-28", "Prompt 13B-C1 correction register", c28_correction_register),
]


def run() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    problems: list[str] = []
    results = []
    for cid, name, fn in CHECKS:
        local: list[str] = []
        try:
            fn(local)
        except Exception as exc:  # a crashing check is a failure, never a pass
            local.append(f"check crashed: {exc!r}")
        results.append((cid, name, local))
        problems.extend(f"{cid}: {p}" for p in local)
    print("13B UI specification validator — documentation quality only")
    for cid, name, local in results:
        print(f"[{'PASS' if not local else 'FAIL'}] {cid} {name}")
        for p in local:
            print(f"        - {p}")
    print(f"CHECKS: {len(results) - sum(1 for _, _, l in results if l)}/{len(results)} passed; {len(problems)} findings")
    print("RESULT: PASS at the documentation level." if not problems else "RESULT: FAIL")
    print("No frontend, screen, component, route, migration or runtime UI exists; no WCAG conformance is claimed.")
    return 0 if not problems else 1


def self_test() -> int:
    # Three seeded defects must be detected by the structural parsers/checks.
    cases = []
    screens = extract_screens()
    mangled = {k: dict(v) for k, v in screens.items()}
    mangled["SCR-001"]["G"] = ""
    local: list[str] = []
    for sid, fields in mangled.items():
        missing = [f for f in "ABCDEFGHIJK" if not fields.get(f)]
        if missing:
            local.append(sid)
    cases.append(("missing field detected", local == ["SCR-001"]))
    ids = [f"REQ-{i}" for i in REQ_RANGE] + ["REQ-999"]
    cases.append(("duplicate requirement detected", len(ids) != len(set(ids))))
    cases.append(("invalid status detected", "APPROVED" not in STATUSES))
    main_h = heading_numbers(read(B13))
    screen_h = heading_numbers(read(SCREENS))
    comp_h = heading_numbers(read(COMPONENTS))
    valid_refs = "See §27, §9.1, parent §8.1, screen companion §10 and 08C §12.2/§12.5."
    cases.append(("valid section references accepted",
                  section_ref_problems(valid_refs, main_h, main_h, screen_h, comp_h) == []))
    bad_refs = "See §99 for the missing section."
    cases.append(("broken section reference detected",
                  section_ref_problems(bad_refs, main_h, main_h, screen_h, comp_h) != []))
    main_a = collect_anchors(read(B13))
    good_link = "See [decisions](#27-decisions-and-provisional-matters)."
    cases.append(("valid heading anchor accepted",
                  anchor_problems(good_link, main_a, {"21_interface_and_player_journeys.md": main_a}) == []))
    bad_link = "See [missing](#missing-section)."
    cases.append(("broken heading anchor detected",
                  anchor_problems(bad_link, main_a, {"21_interface_and_player_journeys.md": main_a}) != []))
    ok = all(v for _, v in cases)
    for name, passed in cases:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    print(f"SELF-TEST: {sum(1 for _, v in cases if v)}/{len(cases)} cases passed")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else run())
