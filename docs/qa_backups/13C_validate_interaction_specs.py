#!/usr/bin/env python3
"""Prompt 13C focused validator — documentary quality only.

Verifies structural and traceability integrity of the B-13C interaction
specifications. It is not a natural-language reviewer, not a UI test, not an
accessibility audit and not evidence of implementation.

Run:  python docs/qa_backups/13C_validate_interaction_specs.py
      python docs/qa_backups/13C_validate_interaction_specs.py --self-test
"""

from __future__ import annotations

import re
import sys
from copy import deepcopy
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
MASTER = DOCS / "stage-2" / "22_interaction_flows_and_player_experience.md"
JOURNEYS = DOCS / "stage-2" / "22_player_journey_specifications.md"
STATES = DOCS / "stage-2" / "22_interaction_states_and_feedback.md"
DECISIONS = DOCS / "DECISIONS.md"
DD = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
TRACE = DOCS / "stage-2" / "03_requirements_traceability.md"

JOURNEY_IDS = [f"JRN-{c}" for c in "ABCDEFGHIJKLM"]
FLOW_IDS = [f"FLOW-{i:03d}" for i in range(1, 34)]
TUT_IDS = [f"TUT-{i:02d}" for i in range(1, 13)]
STATE_IDS = [f"ST-{i:02d}" for i in range(1, 19)]
REQ_IDS = [f"REQ-{i}" for i in range(1090, 1204)]
D_NEW = [f"D-{i:03d}" for i in range(220, 233)]
DD_NEW = [f"DD-{i:03d}" for i in range(268, 281)]
CONDITIONAL = {"SCR-020", "SCR-038", "SCR-039", "SCR-068", "SCR-077"}

STATE_NAMES = {
    "ST-01": "Initial", "ST-02": "Loading", "ST-03": "Refreshing",
    "ST-04": "Loaded", "ST-05": "Empty", "ST-06": "Partial data",
    "ST-07": "Success", "ST-08": "Validation error",
    "ST-09": "Permission denied", "ST-10": "Unavailable",
    "ST-11": "Blocked by rule", "ST-12": "Expired", "ST-13": "Conflict",
    "ST-14": "Failed", "ST-15": "Offline", "ST-16": "Reconnecting",
    "ST-17": "Recovering", "ST-18": "Cancelled",
}


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


def ids_in(text: str, pattern: str) -> list[str]:
    return re.findall(pattern, text, re.M)


def load() -> dict[str, str]:
    return {
        "master": read(MASTER),
        "journeys": read(JOURNEYS),
        "states": read(STATES),
        "decisions": read(DECISIONS),
        "dd": read(DD),
        "trace": read(TRACE),
    }


# ---------------------------------------------------------------- checks

def c01_files(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for path in (MASTER, JOURNEYS, STATES):
        check(p, path.exists() and path.stat().st_size > 5000,
              f"missing or too-small deliverable: {path.name}")
        if path.exists():
            text = read(path)
            check(p, "<<<<<<<" not in text and ">>>>>>>" not in text and "\n=======\n" not in text,
                  f"merge-conflict marker in {path.name}")
    return p


def c02_journeys(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    found = ids_in(t["journeys"], r"^### (JRN-[A-M]) — ")
    check(p, found == JOURNEY_IDS, f"journeys are not JRN-A..JRN-M: {found}")
    check(p, len(set(found)) == len(found), "duplicate journey identifier")
    for jid in found:
        block = section(t["journeys"], f"### {jid} — ", "### ")
        for part in "ABCDEFGHIJ":
            # block ends at next heading; search only within
            pass
    # template parts per journey
    blocks = re.split(r"^### (JRN-[A-M]) — .*$", t["journeys"], flags=re.M)[1:]
    for i in range(0, len(blocks), 2):
        jid, body = blocks[i], blocks[i + 1]
        body = re.split(r"^### ", body, maxsplit=1, flags=re.M)[0]
        for part in "ABCDEFGHIJ":
            check(p, f"**{part}." in body, f"{jid} missing template part {part}")
    return p


def c03_flows(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    found = ids_in(t["journeys"], r"^### (FLOW-\d{3}) — ")
    check(p, found == FLOW_IDS, f"flows are not FLOW-001..FLOW-033: {found}")
    check(p, len(set(found)) == len(found), "duplicate flow identifier")
    blocks = re.split(r"^### (FLOW-\d{3}) — .*$", t["journeys"], flags=re.M)[1:]
    labels = ("Trigger", "Preconditions", "Actors", "Sequence", "Alternative",
              "Failure", "Cancellation", "Completion", "Recovery",
              "Accessibility", "Screens", "Components", "Requirements", "Governing")
    for i in range(0, len(blocks), 2):
        fid, body = blocks[i], blocks[i + 1]
        body = re.split(r"^### ", body, maxsplit=1, flags=re.M)[0]
        miss = [l for l in labels if f"**{l}:**" not in body]
        check(p, not miss, f"{fid} missing flow fields {miss}")
    return p


def c04_tutorials(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    found = ids_in(t["journeys"], r"^### (TUT-\d{2}) — ")
    check(p, found == TUT_IDS, f"tutorials are not TUT-01..TUT-12: {found}")
    check(p, len(set(found)) == len(found), "duplicate tutorial identifier")
    labels = ("Learning objective", "Intended player", "Prerequisites",
              "Entry condition", "Starting screen", "Ordered steps",
              "Explanation", "Expected interaction", "Expected result",
              "Validation", "Failure/recovery", "Skip", "Completion condition",
              "Re-entry", "Accessibility", "Related requirements")
    blocks = re.split(r"^### (TUT-\d{2}) — .*$", t["journeys"], flags=re.M)[1:]
    for i in range(0, len(blocks), 2):
        tid, body = blocks[i], blocks[i + 1]
        body = re.split(r"^### |^## ", body, maxsplit=1, flags=re.M)[0]
        miss = [l for l in labels if f"| {l} |" not in body]
        check(p, not miss, f"{tid} missing tutorial fields {miss}")
        check(p, "| ID / name |" in body, f"{tid} missing combined identity/name field")
    return p


def c05_states(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    catalogue = section(t["states"], "## 2. State catalogue", "## 3. Loading states")
    for sid, name in STATE_NAMES.items():
        check(p, f"`{sid}`" in catalogue, f"state {sid} missing from catalogue")
        check(p, name.lower() in catalogue.lower(), f"state {sid} name {name!r} missing")
    found = ids_in(catalogue, r"^\| `(ST-\d{2})` \|")
    check(p, found == STATE_IDS, f"state catalogue is not ST-01..ST-18: {found}")
    check(p, len(set(found)) == len(found), "duplicate state identifier")
    # every state must be reachable in the transition diagram or described
    for sid in STATE_IDS:
        check(p, f"{sid}" in t["states"], f"state {sid} not used anywhere in state document")
    return p


def c06_component_map(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    body = section(t["states"], "## 7. Component state mapping", "## 8. Validation")
    check(p, bool(body), "component state mapping section missing")
    comps = ids_in(body, r"^\| `(UI-CMP-\d{3})` \|")
    ovls = ids_in(body, r"^\| `(OVL-\d{2})` \|")
    check(p, comps == [f"UI-CMP-{i:03d}" for i in range(1, 91)],
          f"component state map is not UI-CMP-001..090 ({len(comps)})")
    check(p, ovls == [f"OVL-{i:02d}" for i in range(1, 9)],
          f"overlay state map is not OVL-01..08 ({ovls})")
    check(p, "Screen dependency" in body, "component map lacks a screen-dependency column")
    check(p, "Applicable ST" in body, "component map lacks an applicable-ST column")
    return p


def c07_screen_refs(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for name, text in (("master", t["master"]), ("journeys", t["journeys"]), ("states", t["states"])):
        for sid in re.findall(r"SCR-\d{3}", text):
            n = int(sid.split("-")[1])
            check(p, 1 <= n <= 100, f"{name}: undefined screen {sid}")
    return p


def c08_component_refs(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for name, text in (("master", t["master"]), ("journeys", t["journeys"]), ("states", t["states"])):
        for cid in re.findall(r"UI-CMP-\d{3}", text):
            n = int(cid.split("-")[2])
            check(p, 1 <= n <= 90, f"{name}: undefined component {cid}")
        for oid in re.findall(r"OVL-\d{2}", text):
            n = int(oid.split("-")[1])
            check(p, 1 <= n <= 8, f"{name}: undefined overlay {oid}")
    return p


def c09_requirements(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    reg = section(t["master"], "### 18.2 Requirement register", "**Requirement tally")
    rows = ids_in(reg, r"^\| `(REQ-\d{3,4})` \|")
    check(p, rows == REQ_IDS, f"13C requirement register is not REQ-1090..REQ-1203 ({len(rows)})")
    check(p, len(set(rows)) == len(rows), "duplicate 13C requirement identifier")
    check(p, "REQ-1204" in t["master"], "next free identifier REQ-1204 not recorded")
    # status vocabulary and tally
    statuses = re.findall(r"\| (SPECIFIED|PROVISIONAL|BLOCKED) \|$", reg, re.M)
    check(p, set(statuses) <= {"SPECIFIED", "PROVISIONAL", "BLOCKED"}, "invalid requirement status")
    check(p, statuses.count("PROVISIONAL") == 2,
          f"expected 2 PROVISIONAL rows, found {statuses.count('PROVISIONAL')}")
    # every requirement reference in all docs resolves
    known = set(rows)
    for name, text in (("master", t["master"]), ("journeys", t["journeys"]), ("states", t["states"])):
        for rid in re.findall(r"REQ-(\d{3,4})", text):
            num = int(rid)
            if 1090 <= num <= 1203:
                check(p, f"REQ-{num}" in known, f"{name}: undefined 13C requirement REQ-{num}")
    # no earlier requirement row is renumbered into the 03 register table
    trace_ids = [int(x.split("-")[1]) for x in re.findall(r"^\| (REQ-\d{3,4}) \|", t["trace"], re.M)]
    check(p, trace_ids and max(trace_ids) == 869,
          f"03 requirements register table moved past REQ-869 (max={max(trace_ids) if trace_ids else None})")
    return p


def c10_decisions(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    d_rows = ids_in(t["decisions"], r"^\| (D-\d{3}) \|")
    for did in D_NEW:
        check(p, did in d_rows, f"missing DECISIONS row {did}")
    dd_rows = ids_in(t["dd"], r"^\| (DD-\d{3}) \|")
    for did in DD_NEW:
        check(p, did in dd_rows, f"missing mirrored decision {did}")
    # every D reference used in 13C exists (D-001..D-232)
    for name, text in (("master", t["master"]), ("journeys", t["journeys"]), ("states", t["states"])):
        for did in re.findall(r"(?<!D)D-(\d{3})", text):
            check(p, f"D-{did}" in d_rows, f"{name}: undefined decision D-{did}")
    return p


def c11_matrices(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for matrix in "ABCDEFGHI":
        found = (f"Matrix {matrix} —" in t["master"]) or (f"Matrix {matrix}" in t["states"])
        check(p, found, f"Matrix {matrix} missing")
    ma = section(t["master"], "### 18.3 Matrix A", "### 18.4 Matrix B")
    for jid in JOURNEY_IDS:
        check(p, f"`{jid}`" in ma, f"Matrix A missing journey {jid}")
    mb = section(t["master"], "### 18.4 Matrix B", "### 18.5 Matrix C")
    for fid in FLOW_IDS:
        check(p, f"`{fid}`" in mb, f"Matrix B missing flow {fid}")
    mc = section(t["master"], "### 18.5 Matrix C", "### 18.6 Matrix D")
    for fid in FLOW_IDS:
        check(p, f"`{fid}`" in mc, f"Matrix C missing flow {fid}")
    mf = section(t["master"], "### 18.8 Matrix F", "### 18.9 Matrix G")
    for tid in TUT_IDS:
        check(p, f"`{tid}`" in mf, f"Matrix F missing tutorial {tid}")
    mg = section(t["master"], "### 18.9 Matrix G", "### 18.10 Matrix H")
    for n in range(1, 19):
        check(p, f"`NTF-{n:02d}`" in mg, f"Matrix G missing NTF-{n:02d}")
    mi = section(t["master"], "### 15.6 Matrix I", "## 16.")
    for n in range(1, 25):
        check(p, f"`CON-{n:02d}`" in mi, f"Matrix I missing CON-{n:02d}")
    mh = section(t["master"], "### 18.10 Matrix H", "### 18.11")
    for jid in JOURNEY_IDS:
        check(p, f"`{jid}`" in mh, f"Matrix H missing journey {jid}")
    return p


def c12_state_coverage(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for label, count in (("VAL", 20), ("CFM", 10), ("DUP", 8), ("ERR", 20),
                         ("REC", 10), ("AXI", 18), ("AX-AC", 12),
                         ("NTF", 18), ("OFF", 12), ("CON", 24)):
        for n in range(1, count + 1):
            ident = f"{label}-{n:02d}"
            hay = t["master"] + t["states"]
            check(p, ident in hay, f"missing {ident}")
    return p


def c13_validation_errors(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    sv = section(t["states"], "## 8. Validation", "## 9. Confirmation")
    check(p, "VAL-01" in sv and "VAL-20" in sv, "validation register incomplete")
    for needle in ("field", "problem", "why", "correction", "preserved"):
        check(p, needle in sv.lower(), f"validation message anatomy lacks {needle}")
    se = section(t["states"], "## 11. Error handling", "## 12. Accessibility")
    for needle in ("what happened", "whether anything changed", "completed",
                   "retrying is safe", "next", "support"):
        check(p, needle in se.lower(), f"failure anatomy lacks {needle}")
    return p


def c14_accessibility(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    sx = section(t["states"], "## 12. Accessibility", "## 13. Notification")
    for needle in ("WCAG 2.2", "keyboard", "focus", "screen reader", "announced",
                   "200%", "320", "reduced motion", "colour"):
        check(p, needle.lower() in sx.lower(), f"accessibility interaction section lacks {needle}")
    check(p, "AX-AC-12" in sx and "AX-AC-01" in sx, "accessibility acceptance criteria incomplete")
    check(p, "No WCAG conformance is claimed" in t["states"], "accessibility evidence boundary missing")
    return p


def c15_onboarding(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    so = section(t["master"], "## 12. Onboarding", "## 13. Notification")
    for needle in ("Mandatory", "Optional", "Contextual help", "skippable", "resumable",
                   "never performs a gameplay action", "no tutorial reward"):
        check(p, needle.lower() in so.lower(), f"onboarding architecture lacks {needle}")
    check(p, "TUT-01" in t["journeys"] and "TUT-12" in t["journeys"], "tutorial bodies incomplete")
    return p


def c16_notifications(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    sn = section(t["master"], "## 13. Notification", "## 14. Offline")
    for needle in ("blocking", "digest", "ambient", "informational", "success",
                   "warning", "critical", "action-required", "non-opt-out", "deep-link"):
        check(p, needle in sn, f"notification architecture lacks {needle}")
    check(p, "No notification category may generate a trigger" in sn,
          "notification no-invention rule missing")
    return p


def c17_offline(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    so = section(t["master"], "## 14. Offline", "## 15. Cross-screen")
    for needle in ("no offline gameplay", "unknown — retrying", "no automatic retry",
                   "two-hour UTC", "read-only", "as-of turn"):
        check(p, needle.lower() in so.lower(), f"offline posture lacks {needle}")
    ss = section(t["states"], "## 14. Offline", "## 15. Cross-screen")
    check(p, "OFF-12" in ss and "OFF-01" in ss, "offline scenario register incomplete")
    return p


def c18_consistency(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    sc = section(t["master"], "## 15. Cross-screen", "## 16. Security")
    for needle in ("Canonical parent", "total, reserved and available", "server-authoritative",
                   "Canonical parents"):
        check(p, needle.lower() in sc.lower(), f"cross-screen consistency lacks {needle}")
    check(p, "CON-24" in sc, "consistency matrix incomplete")
    return p


def c19_conditional(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    # Matrix B flow rows must not reference conditional screens
    mb = section(t["master"], "### 18.4 Matrix B", "### 18.5 Matrix C")
    flow_rows = [l for l in mb.splitlines() if re.match(r"^\| `FLOW-", l)]
    for row in flow_rows:
        for sid in re.findall(r"SCR-\d{3}", row):
            check(p, sid not in CONDITIONAL, f"flow matrix references conditional screen {sid} as a flow screen")
    # tutorial starting screens must not be conditional
    tut_blocks = re.split(r"^### (TUT-\d{2}) — .*$", t["journeys"], flags=re.M)[1:]
    for i in range(0, len(tut_blocks), 2):
        tid, body = tut_blocks[i], tut_blocks[i + 1]
        body = re.split(r"^### |^## ", body, maxsplit=1, flags=re.M)[0]
        m = re.search(r"\| Starting screen \| (.*?) \|", body)
        if m:
            for sid in re.findall(r"SCR-\d{3}", m.group(1)):
                check(p, sid not in CONDITIONAL, f"{tid} starts on conditional screen {sid}")
    # absence statements present in the master
    for sid in sorted(CONDITIONAL):
        check(p, f"`{sid}`" in t["master"], f"conditional screen {sid} lacks an absence statement in the master")
    for needle in ("absent", "no flow"):
        check(p, needle in t["master"].lower(), f"conditional absence wording lacks {needle}")
    return p


def c20_mapless(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    text = t["master"] + t["journeys"] + t["states"]
    check(p, "Mapless interaction preserved" in t["master"], "mapless interaction guard missing")
    check(p, "no geographic" in text.lower(), "no-geographic prohibition missing")
    check(p, "TR-012" in t["master"] and "REQ-041" in t["master"], "mapless rule anchors missing")
    check(p, "SCR-018" in t["master"], "Network View reference missing")
    for bad in ("tile provider", "basemap", "map projection", "geocoding"):
        # allowed only inside a prohibition sentence; ensure not presented as a feature
        for m in re.finditer(bad, text, re.I):
            ctx = text[max(0, m.start() - 60):m.end() + 40].lower()
            if "no " not in ctx and "not " not in ctx and "forbid" not in ctx:
                p.append(f"possible geographic feature reference ({bad}) without prohibition context")
    return p


def c21_no_implementation(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    code_ext = {".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte", ".sql", ".css", ".scss"}
    for path in (DOCS / "stage-2").rglob("*"):
        if path.is_file() and path.suffix.lower() in code_ext:
            p.append(f"implementation-looking file exists under stage-2: {path.name}")
    check(p, "No frontend implementation" in t["master"], "scope confirmation missing")
    for forbidden in ("CREATE TABLE", "import React", "from supabase", "ALTER TABLE"):
        check(p, forbidden not in t["master"] + t["journeys"] + t["states"],
              f"implementation token found: {forbidden}")
    return p


def c22_no_13d(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    # Frontier refresh (Prompt 13D): the four 13D deliverables now exist by owner
    # authorization. The 13C boundary that matters is retained: 13C itself
    # created no implementation and recorded the 13D boundary.
    for name in ("23_ui_system_integration_and_traceability.md", "23_ui_integration_contracts.md",
                 "23_ui_acceptance_test_catalog.md", "23_prompt_13_final_reconciliation_and_acceptance.md"):
        check(p, (DOCS / "stage-2" / name).exists(), f"Prompt 13D deliverable missing: {name}")
    check(p, "Prompt 13D" in t["master"], "Prompt 13D boundary missing")
    check(p, "No frontend implementation" in t["master"], "13C scope confirmation missing")
    return p


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch in " -_")
    return text.replace(" ", "-")


def c23_links(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for path, key in ((MASTER, "master"), (JOURNEYS, "journeys"), (STATES, "states")):
        text = t[key]
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            target = m.group(1)
            if target.lower().startswith(("http:", "https:", "mailto:", "tel:", "data:")):
                continue
            target_path, _, fragment = target.partition("#")
            if target_path:
                resolved = (path.parent / target_path).resolve()
                check(p, resolved.exists(), f"{path.name}: broken link {target}")
            if fragment:
                if target_path:
                    tpath = (path.parent / target_path).resolve()
                else:
                    tpath = path
                if tpath.exists() and tpath.suffix.lower() == ".md":
                    anchors = set()
                    for line in read(tpath).splitlines():
                        hm = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
                        if hm:
                            anchors.add(slugify(hm.group(1)))
                    check(p, fragment.lower() in anchors,
                          f"{path.name}: missing anchor #{fragment} in {tpath.name}")
    return p


HEADING_RE = re.compile(r"^#{2,4}\s+(\d+(?:\.\d+)?)\.?\s+")
EXTERNAL_PREFIXES = ("13A", "13B", "Prompt 13B", "B-13", "B-13C", "08C", "07C", "WAR",
                     "B-02", "B-10", "Report 07", "progress-log", "progress log")


def heading_numbers(text: str) -> set[str]:
    out: set[str] = set()
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            out.add(m.group(1))
    return out


def c24_sections(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    own = {
        "master": heading_numbers(t["master"]),
        "journeys": heading_numbers(t["journeys"]),
        "states": heading_numbers(t["states"]),
    }
    targets = {
        "parent": own["master"],
        "state companion": own["states"],
        "journey companion": own["journeys"],
    }
    for name, text in (("master", t["master"]), ("journeys", t["journeys"]), ("states", t["states"])):
        prev_external = False
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in re.finditer(r"§(\d+(?:\.\d+)?)", line):
                num = m.group(1)
                before = line[max(0, m.start() - 60):m.start()]
                pref = None
                stripped = before.rstrip()
                for candidate in ("state companion", "journey companion", "parent"):
                    if stripped.endswith(candidate):
                        pref = candidate
                        break
                if pref is None:
                    if any(stripped.endswith(ext) for ext in EXTERNAL_PREFIXES):
                        pref = "external"
                if pref == "external" or before.rstrip().endswith("§"):
                    prev_external = True
                    continue
                if pref is None and prev_external and re.search(r"[/–-]\s*$", before):
                    continue
                target = targets.get(pref, own[name])
                if num not in target:
                    p.append(f"{name} line {lineno}: §{num} does not resolve (prefix={pref})")
                prev_external = False
    return p


def c25_traceability(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    # every journey/flow has a requirement row referencing it
    reg = section(t["master"], "### 18.2 Requirement register", "**Requirement tally")
    rows = [l for l in reg.splitlines() if re.match(r"^\| `REQ-", l)]
    for jid in JOURNEY_IDS:
        check(p, any(f"`{jid}`" in r for r in rows), f"no requirement references journey {jid}")
    for fid in FLOW_IDS:
        check(p, any(f"`{fid}`" in r for r in rows), f"no requirement references flow {fid}")
    # every requirement row has a D-22x/23x decision reference
    for row in rows:
        rid = re.match(r"^\| `(REQ-\d+)`", row).group(1)
        check(p, re.search(r"D-2[23]\d", row) is not None, f"{rid} has no 13C decision reference")
    # Matrix B and C flow sets equal
    mb = section(t["master"], "### 18.4 Matrix B", "### 18.5 Matrix C")
    mc = section(t["master"], "### 18.5 Matrix C", "### 18.6 Matrix D")
    b = ids_in(mb, r"^\| `(FLOW-\d{3})`")
    c = ids_in(mc, r"^\| `(FLOW-\d{3})`")
    check(p, b == FLOW_IDS and c == FLOW_IDS, "Matrix B/C flow sets are not 33 contiguous flows")
    # every flow must cite an owning rule/system, never invent a mechanic
    governing = re.compile(r"(B-0[2-9]|B-1[0-2]|08C|DIP|ALL|WAR|ECN|URB|DMP|WEP|MKT|MOD|RRL|ACC|NAT|ONB|TR-|REQ-|D-\d{3})")
    blocks = re.split(r"^### (FLOW-\d{3}) — .*$", t["journeys"], flags=re.M)[1:]
    for i in range(0, len(blocks), 2):
        fid, body = blocks[i], blocks[i + 1]
        body = re.split(r"^### ", body, maxsplit=1, flags=re.M)[0]
        m = re.search(r"\*\*Governing:\*\* (.*)", body)
        check(p, m is not None and governing.search(m.group(1)) is not None,
              f"{fid} has no recognisable governing rule/system citation")
    # every requirement row must name a governing system
    for row in rows:
        cells = [x.strip() for x in row.strip().strip("|").split("|")]
        if len(cells) >= 12:
            check(p, bool(cells[8]) and cells[8] != "None",
                  f"{cells[0]} has no governing system")
    return p


def c26_unique_ids(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    alltext = t["master"] + t["journeys"] + t["states"]
    for prefix, expected in (("JRN", 13), ("FLOW", 33), ("TUT", 12), ("ST", 18)):
        # occurrence count is not uniqueness; check heading/definition uniqueness
        if prefix == "JRN":
            ids = re.findall(r"^### (JRN-[A-M]) — ", t["journeys"], re.M)
        elif prefix == "FLOW":
            ids = re.findall(r"^### (FLOW-\d{3}) — ", t["journeys"], re.M)
        elif prefix == "TUT":
            ids = re.findall(r"^### (TUT-\d{2}) — ", t["journeys"], re.M)
        else:
            ids = re.findall(r"^\| `(ST-\d{2})` \|", t["states"], re.M)
        check(p, len(ids) == expected, f"{prefix} definition count is {len(ids)}, expected {expected}")
        check(p, len(set(ids)) == len(ids), f"duplicate {prefix} identifier")
    return p


def c27_acceptance(t: dict[str, str]) -> list[str]:
    p: list[str] = []
    for n in range(1, 27):
        cid = f"13C-AC-{n:02d}"
        check(p, cid in t["master"], f"acceptance criterion {cid} missing")
    for needle in ("PASS", "PARTIAL", "BLOCKED", "NOT APPLICABLE"):
        check(p, needle in t["master"], f"acceptance vocabulary lacks {needle}")
    return p


CHECKS = [
    ("13C-01", "Mandatory deliverables exist and are conflict-free", c01_files),
    ("13C-02", "Journeys JRN-A..M with ten template parts", c02_journeys),
    ("13C-03", "Flows FLOW-001..033 with fifteen fields", c03_flows),
    ("13C-04", "Tutorials TUT-01..12 with the tutorial template", c04_tutorials),
    ("13C-05", "Eighteen-state taxonomy and catalogue", c05_states),
    ("13C-06", "Component state map for 90 components and 8 overlays", c06_component_map),
    ("13C-07", "All screen references exist", c07_screen_refs),
    ("13C-08", "All component/overlay references exist", c08_component_refs),
    ("13C-09", "Requirement register REQ-1090..REQ-1203 and frontier", c09_requirements),
    ("13C-10", "Decision D-220..D-232 and DD-268..DD-280 exist", c10_decisions),
    ("13C-11", "Matrices A..I exist and cover their identifiers", c11_matrices),
    ("13C-12", "State/validation/error/accessibility/notification/offline/consistency coverage", c12_state_coverage),
    ("13C-13", "Validation and error anatomy coverage", c13_validation_errors),
    ("13C-14", "Accessibility interaction coverage and evidence boundary", c14_accessibility),
    ("13C-15", "Onboarding architecture and tutorial safety", c15_onboarding),
    ("13C-16", "Notification architecture and no-invention rule", c16_notifications),
    ("13C-17", "Offline and reconnection coverage", c17_offline),
    ("13C-18", "Cross-screen consistency coverage", c18_consistency),
    ("13C-19", "Conditional features respect gates", c19_conditional),
    ("13C-20", "Mapless architecture preserved", c20_mapless),
    ("13C-21", "No implementation artifacts", c21_no_implementation),
    ("13C-22", "Prompt 13D boundary recorded; 13D deliverables present", c22_no_13d),
    ("13C-23", "Internal Markdown links and anchors resolve", c23_links),
    ("13C-24", "Section references resolve", c24_sections),
    ("13C-25", "Requirement/journey/flow traceability consistent", c25_traceability),
    ("13C-26", "Journey/flow/tutorial/state identifiers unique", c26_unique_ids),
    ("13C-27", "Acceptance criteria 13C-AC-01..26 present", c27_acceptance),
]


def validate(t: dict[str, str]) -> tuple[int, list[tuple[str, str, list[str]]]]:
    results = []
    problems = 0
    for cid, name, fn in CHECKS:
        try:
            probs = fn(t)
        except Exception as exc:  # a parser failure is a failed check, never a pass
            probs = [f"check crashed: {exc!r}"]
        results.append((cid, name, probs))
        problems += len(probs)
    return problems, results


def main() -> int:
    t = load()
    problems, results = validate(t)
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
    return 0 if problems == 0 else 1


# ---------------------------------------------------------------- self-tests

def expect(mutated: dict[str, str], substring: str, case: str) -> bool:
    _, results = validate(mutated)
    joined = "\n".join(pb for _, _, probs in results for pb in probs)
    ok = substring in joined
    if not ok:
        print(f"[SELF-TEST FAIL] {case}: expected {substring!r} in problems")
    return ok


def self_test() -> int:
    base = load()
    cases: list[tuple[str, callable]] = []
    passed = 0

    def case(name: str, fn):
        nonlocal passed
        try:
            ok = fn()
        except Exception as exc:
            print(f"[SELF-TEST FAIL] {name}: crashed {exc!r}")
            ok = False
        cases.append((name, fn))
        if ok:
            passed += 1
            print(f"[SELF-TEST PASS] {name}")

    def missing_journey():
        m = deepcopy(base)
        m["journeys"] = m["journeys"].replace("### JRN-C — National management journey", "### JRN-C: National management", 1)
        return expect(m, "journeys are not JRN-A..JRN-M", "missing journey heading")

    def missing_template_part():
        m = deepcopy(base)
        m["journeys"] = m["journeys"].replace("**F. Failure paths.**", "Failure paths.", 1)
        return expect(m, "missing template part F", "missing journey template part")

    def duplicate_flow():
        m = deepcopy(base)
        m["journeys"] = m["journeys"].replace("### FLOW-002 — Login and session entry",
                                              "### FLOW-001 — Login and session entry", 1)
        return expect(m, "flows are not FLOW-001..FLOW-033", "duplicate flow id")

    def missing_flow_field():
        m = deepcopy(base)
        m["journeys"] = m["journeys"].replace("**Cancellation:**", "**Cancel path:**", 1)
        return expect(m, "missing flow fields", "missing flow field")

    def missing_tutorial():
        m = deepcopy(base)
        m["journeys"] = m["journeys"].replace("### TUT-12 — Notifications, help, support and reporting",
                                              "### TUT-12: Notifications", 1)
        return expect(m, "tutorials are not TUT-01..TUT-12", "missing tutorial heading")

    def bad_screen():
        m = deepcopy(base)
        m["master"] = m["master"] + "\nSee `SCR-101`.\n"
        return expect(m, "undefined screen SCR-101", "invalid screen reference")

    def bad_component():
        m = deepcopy(base)
        m["journeys"] = m["journeys"] + "\nUse `UI-CMP-091`.\n"
        return expect(m, "undefined component UI-CMP-091", "invalid component reference")

    def missing_requirement():
        m = deepcopy(base)
        m["master"] = m["master"].replace("| `REQ-1183` |", "| `REQ-1283` |", 1)
        return expect(m, "not REQ-1090..REQ-1203", "broken requirement sequence")

    def missing_decision():
        m = deepcopy(base)
        m["decisions"] = m["decisions"].replace("| D-225 |", "| D-925 |", 1)
        return expect(m, "missing DECISIONS row D-225", "missing decision row")

    def missing_matrix():
        m = deepcopy(base)
        m["master"] = m["master"].replace("### 18.7 Matrix E", "### 18.7 Accessibility coverage", 1)
        return expect(m, "Matrix E missing", "missing matrix heading")

    def conditional_flow():
        m = deepcopy(base)
        m["master"] = m["master"].replace(
            "| `FLOW-001` | Registration and verification | `SCR-002`, `SCR-006` |",
            "| `FLOW-001` | Registration and verification | `SCR-002`, `SCR-006`, `SCR-038` |", 1)
        return expect(m, "conditional screen SCR-038", "conditional screen in flow matrix")

    def broken_link():
        m = deepcopy(base)
        m["master"] = m["master"] + "\n[broken](does_not_exist.md)\n"
        return expect(m, "broken link", "broken markdown link")

    def broken_section_ref():
        m = deepcopy(base)
        m["states"] = m["states"] + "\nSee §99.9.\n"
        return expect(m, "§99.9 does not resolve", "broken section reference")

    def missing_state():
        m = deepcopy(base)
        m["states"] = m["states"].replace("| `ST-18` |", "| `ST-19` |", 1)
        return expect(m, "state catalogue is not ST-01..ST-18", "missing state")

    def missing_component_map_row():
        m = deepcopy(base)
        m["states"] = m["states"].replace("| `UI-CMP-090` | Exact-phrase", "| `UI-CMP-091` | Exact-phrase", 1)
        return expect(m, "component state map is not UI-CMP-001..090", "missing component map row")

    def missing_acceptance():
        m = deepcopy(base)
        m["master"] = m["master"].replace("| 13C-AC-26 |", "| 13C-AC-27 |", 1)
        return expect(m, "acceptance criterion 13C-AC-26 missing", "missing acceptance criterion")

    def mapless_guard():
        m = deepcopy(base)
        m["master"] = m["master"].replace("Mapless interaction preserved", "World interaction", 1)
        return expect(m, "mapless interaction guard missing", "mapless guard removed")

    def implementation_token():
        m = deepcopy(base)
        m["states"] = m["states"] + "\n```sql\nCREATE TABLE players (id int);\n```\n"
        return expect(m, "implementation token found: CREATE TABLE", "implementation token")

    case("missing journey heading", missing_journey)
    case("missing journey template part", missing_template_part)
    case("duplicate flow identifier", duplicate_flow)
    case("missing flow field", missing_flow_field)
    case("missing tutorial heading", missing_tutorial)
    case("invalid screen reference", bad_screen)
    case("invalid component reference", bad_component)
    case("broken requirement sequence", missing_requirement)
    case("missing decision row", missing_decision)
    case("missing matrix heading", missing_matrix)
    case("conditional screen in flow matrix", conditional_flow)
    case("broken markdown link", broken_link)
    case("broken section reference", broken_section_ref)
    case("missing state", missing_state)
    case("missing component map row", missing_component_map_row)
    case("missing acceptance criterion", missing_acceptance)
    case("mapless guard removed", mapless_guard)
    case("implementation token inserted", implementation_token)

    print(f"\nSELF-TEST: {passed}/{len(cases)} regression cases passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
