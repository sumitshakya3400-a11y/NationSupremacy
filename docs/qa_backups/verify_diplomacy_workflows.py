#!/usr/bin/env python3
"""Document checks for the Prompt 08C diplomacy workflows and acceptance matrix.

Why this exists (2026-10-30): B-08 v1.2 states 157 rules, but a rulebook is not
an operating specification. Prompt 08C adds 30 workflows (DPW-), 54 edge cases
(DPE-) and 88 acceptance tests (DPA-), plus traceability to REQ-012 and
REQ-514..REQ-533, the twelve formulas, the fifteen DPF codes and the nine
notifications.

The 08C-C audit found that the first version of this checker accepted a
semantically wrong DPE-to-DPA mapping because both identifiers existed. This
version therefore checks the *coverage matrix* in §7.10 as well as identifier
presence: every COVERED row must name a real test and a concrete assertion,
every PARTIAL row must explain its gap, and the totals must reconcile. It also
checks that each §14 subsection heading lists exactly the tests in its table,
and that the two corrected DPW references still point at the right sections.

The 08C-D pass adds targeted semantic guards: an acceptance-replay test, a
notification-privacy test, three separated DPE-054 scenarios, the five repaired
requirement rows, reverse traceability for each primary coverage link, and
bare-range expansion so `DPA-080`…`DPA-082` cannot lose its interior.

This remains a documentation checker. There is no game code to run (D-012), so
nothing here is a runtime, load, concurrency, security or playability test.

Usage:
    python3 verify_diplomacy_workflows.py [--self-test]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
WORK = DOCS / "stage-2" / "15_diplomacy_workflows_acceptance.md"
B08 = DOCS / "stage-2" / "15_diplomacy.md"
LOG = DOCS / "stage-2" / "06_stage_2_progress_log.md"

checks: list[tuple[bool, str, str]] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append((bool(ok), label, detail))


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def section(text: str, start: str, end: str) -> str:
    """Text between two markers; empty when a marker is missing."""
    try:
        i = text.index(start)
        j = text.index(end, i + len(start))
        return text[i:j]
    except ValueError:
        return ""


def dip_ids(b08: str) -> set[str]:
    defined = set(re.findall(r"^\*\*DIP-(\d{3}[a-z]?)", b08, re.M))
    defined |= set(re.findall(r"^\| \*\*DIP-(\d{3}[a-z]?)\*\*", b08, re.M))
    return defined


def workflow_blocks(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    starts = list(re.finditer(r"^### DPW-(\d{3}) — ", text, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        blocks[m.group(1)] = text[m.start():end]
    return blocks


def expand_dpa(refs: str) -> set[str]:
    """Expand `DPA-001`…`DPA-026` (backticked or bare) and collect standalone IDs."""
    found: set[str] = set()
    # The traceability cells write ranges both as `DPA-080`…`DPA-082` and as
    # DPA-080…DPA-082. Match both, otherwise the interior of a bare range is
    # silently treated as missing and a complete row is reported as incomplete.
    for pattern in (r"`DPA-(\d{3})`…`DPA-(\d{3})`", r"DPA-(\d{3})…DPA-(\d{3})"):
        for a, b in re.findall(pattern, refs):
            found |= {f"{n:03d}" for n in range(int(a), int(b) + 1)}
    for n in re.findall(r"DPA-(\d{3})", refs):
        found.add(n)
    return found


def test_sections(text: str) -> dict[str, tuple[set[str], set[str]]]:
    """Map each §14 subsection title to (heading IDs, table IDs)."""
    out: dict[str, tuple[set[str], set[str]]] = {}
    starts = list(re.finditer(r"^### 14\.(\d+) ([^\n]+)$", text, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.find("## 15.", m.end())
        block = text[m.start():end if end > 0 else len(text)]
        heading = expand_dpa(m.group(2))
        rows = set(re.findall(r"^\| `DPA-(\d{3})` \|", block, re.M))
        out[f"14.{m.group(1)}"] = (heading, rows)
    return out


def problems(text: str, b08: str) -> list[str]:
    out: list[str] = []

    # 1. Required sections 1..19.
    headings = [int(n) for n in re.findall(r"^## (\d+)\. ", text, re.M)]
    if headings != list(range(1, 20)):
        out.append(f"section headings are not 1..19: {headings}")

    # 2. Workflows: 30 sequential, each with all 23 fields.
    blocks = workflow_blocks(text)
    ids = sorted(blocks)
    if ids != [f"{n:03d}" for n in range(1, 31)]:
        out.append(f"DPW workflow IDs are not 001..030: {ids[:5]}…{ids[-3:]}")
    for wid in ids:
        fields = {int(n) for n in re.findall(r"^\| (\d{1,2}) \| \*\*", blocks[wid], re.M)}
        if fields != set(range(1, 24)):
            out.append(f"DPW-{wid} is missing fields {sorted(set(range(1, 24)) - fields)}")

    # 3. Edge cases: exactly 54 catalogue rows, sequential.
    catalogue = section(text, "## 7. Edge-case catalogue", "**7.9 Coverage check.")
    dpes = re.findall(r"^\| `DPE-(\d{3})` \|", catalogue, re.M)
    if dpes != [f"{n:03d}" for n in range(1, 55)]:
        out.append(f"DPE IDs are not 001..054 (count {len(dpes)})")

    # 4. Tests: 88 sequential, every reference resolving.
    matrix = section(text, "## 14. Acceptance-test matrix", "## 15. Requirements traceability")
    tests = re.findall(r"^\| `DPA-(\d{3})` \|", matrix, re.M)
    # IDs stay stable; the 08C-C additions sit at the end of their subject
    # section, so the document order is 001..026, 073, 027..072, 074...088.
    if sorted(tests) != [f"{n:03d}" for n in range(1, 89)] or len(set(tests)) != len(tests):
        out.append(f"DPA IDs are not exactly 001..088 once each (count {len(tests)})")

    for line in catalogue.splitlines():
        if not re.match(r"^\| `DPE-\d{3}` \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) >= 8:
            for d in re.findall(r"DPA-(\d{3})", cells[7]):
                if d not in tests:
                    out.append(f"a DPE catalogue row maps to nonexistent DPA-{d}")

    defined_dip = dip_ids(b08)
    valid_req = {"012"} | {str(n) for n in range(514, 534)}
    used_wf: set[str] = set()
    used_dpe: set[str] = set()
    dpa_dpe: dict[str, str] = {}
    test_reqs: dict[str, set[str]] = {}
    for line in matrix.splitlines():
        m = re.match(r"\| `DPA-(\d{3})` \|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) != 12:
            out.append(f"DPA-{m.group(1)} has {len(cells) - 2} columns, expected 10")
            continue
        tid, wcell, dcell, rcell, qcell = m.group(1), cells[2], cells[3], cells[4], cells[5]
        dpa_dpe[tid] = dcell
        if wcell not in ids:
            out.append(f"DPA-{tid} cites undefined workflow {wcell!r}")
        else:
            used_wf.add(wcell)
        if dcell != "—":
            for d in re.findall(r"(\d{3})", dcell):
                if d not in dpes:
                    out.append(f"DPA-{tid} cites undefined edge case DPE-{d}")
                else:
                    used_dpe.add(d)
        for d in re.findall(r"DIP-(\d{3}[a-z]?)", rcell):
            if d not in defined_dip:
                out.append(f"DPA-{tid} cites undefined rule DIP-{d}")
        reqs = re.findall(r"REQ-(\d{3})", qcell)
        if not reqs:
            out.append(f"DPA-{tid} has no requirement reference")
        test_reqs[tid] = set(reqs)
        for q in reqs:
            if q not in valid_req:
                out.append(f"DPA-{tid} cites unknown requirement REQ-{q}")
        # The expected and pass columns must not grant authority to the system,
        # an alliance or an administrator, and must never turn silence into consent.
        evidence = (cells[8] + " " + cells[10]).lower()
        if re.search(r"\b(?:system|game) (?:may |will |can )?accepts?\b", evidence):
            out.append(f"DPA-{tid} contains a sovereignty contradiction: the system accepts for a player")
        if re.search(r"\bsilence\b[^.]{0,30}\b(?:consent|accept)", evidence):
            out.append(f"DPA-{tid} treats silence as consent")
        if re.search(r"automatically (?:accept|reject|declare|break|renew|sign|sanction)", evidence):
            out.append(f"DPA-{tid} introduces an unapproved automatic diplomatic action")

    for wid in ids:
        if wid not in used_wf:
            out.append(f"DPW-{wid} is not exercised by any DPA test")
    for did in dpes:
        if did not in used_dpe:
            out.append(f"DPE-{did} is not covered by any DPA test")

    # 4b. Each §14 heading must list exactly the tests in its own table.
    sections = test_sections(text)
    if len(sections) != 7:
        out.append(f"expected seven §14 test subsections, found {len(sections)}")
    for title, (heading_ids, row_ids) in sections.items():
        if heading_ids != row_ids:
            out.append(f"§{title} heading IDs do not match its table: "
                       f"missing {sorted(heading_ids - row_ids)[:4]}, "
                       f"extra {sorted(row_ids - heading_ids)[:4]}")

    # 4c. Section counts and the §14.9 summary must agree.
    counts = [len(v[1]) for _, v in sorted(sections.items(), key=lambda kv: int(kv[0].split(".")[1]))]
    summary = section(text, "**14.9 Coverage.**", "## 15. Requirements traceability")
    bold = [int(n) for n in re.findall(r"\*\*(\d+)\*\*", summary)]
    stated = bold[:7]
    if stated != counts:
        out.append(f"§14.9 category counts {stated} do not match section rows {counts}")
    if sum(counts) != 88:
        out.append(f"§14 test sections sum to {sum(counts)}, expected 88")
    if "27+15+10+7+11+11+7 = 88" not in summary:
        out.append("§14.9 arithmetic line is not 27+15+10+7+11+11+7 = 88")

    # 4d. Coverage matrix: one row per edge case, status and evidence mandatory.
    cover = section(text, "**7.10 Edge-case coverage matrix", "**7.11 Coverage totals.")
    rows = [ln for ln in cover.splitlines() if re.match(r"^\| `DPE-\d{3}` \|", ln)]
    seen: list[str] = []
    statuses: dict[str, int] = {"COVERED": 0, "PARTIAL": 0, "NOT COVERED": 0, "NOT APPLICABLE": 0}
    dpe_status: dict[str, str] = {}
    dpe_primary: dict[str, str] = {}
    dpe_all: dict[str, str] = {}
    dpe_follow: dict[str, str] = {}
    for ln in rows:
        cells = [c.strip() for c in ln.split("|")]
        if len(cells) != 10:
            out.append("a coverage row does not have 8 columns")
            continue
        did = re.search(r"DPE-(\d{3})", cells[1]).group(1)
        seen.append(did)
        primary, assertion = cells[4], cells[6]
        status = cells[7].replace("*", "").strip()
        follow = cells[8]
        dpe_status[did] = status
        dpe_primary[did] = cells[4]
        dpe_all[did] = cells[4] + " " + cells[5]
        dpe_follow[did] = follow
        if status not in statuses:
            out.append(f"DPE-{did} has unknown coverage status {status!r}")
            continue
        statuses[status] += 1
        if status == "COVERED":
            if not re.search(r"DPA-\d{3}", primary):
                out.append(f"DPE-{did} is COVERED but names no test")
            if not assertion:
                out.append(f"DPE-{did} has an empty coverage assertion")
        if status == "PARTIAL" and (not follow or follow == "—"):
            out.append(f"DPE-{did} is PARTIAL without an explanation")
        if status == "NOT COVERED" and (not follow or follow == "—"):
            out.append(f"DPE-{did} is NOT COVERED without a required action")
        if assertion and len(assertion) < 20:
            out.append(f"DPE-{did} has a non-specific coverage assertion")
        for cell in (primary, cells[5]):
            for d in re.findall(r"DPA-(\d{3})", cell):
                if d not in tests:
                    out.append(f"DPE-{did} maps to nonexistent DPA-{d}")
    if seen != [f"{n:03d}" for n in range(1, 55)]:
        out.append(f"coverage matrix IDs are not 001..054 (count {len(seen)})")
    if re.search(r"\bNOT COVERED\b", cover):
        pass  # phrase is allowed in a status cell; totals are checked below.
    totals = section(text, "**7.11 Coverage totals.**", "---")
    for label, n in statuses.items():
        if f"**{n} {label}**" not in totals and f"{n} {label}" not in totals:
            out.append(f"§7.11 total for {label} is not {n}")
    if sum(statuses.values()) != 54:
        out.append(f"coverage statuses sum to {sum(statuses.values())}, expected 54")

    # 4d-2. Targeted semantic guards for the 08C-D corrections. Identifiers
    # alone are not coverage: the row must name the test that proves the case.
    if "DPA-088" not in dpe_primary.get("051", ""):
        out.append("DPE-051 is not linked to the acceptance-replay test DPA-088")
    if dpe_status.get("054") != "PARTIAL":
        out.append("DPE-054 must be PARTIAL while the privileged-read audit is deferred")
    if "DPA-087" not in dpe_all.get("054", ""):
        out.append("DPE-054 does not link the notification-privacy test DPA-087")
    if "Prompt 12" not in dpe_follow.get("054", "") and "privileged" not in dpe_follow.get("054", "").lower():
        out.append("DPE-054 PARTIAL does not name its privileged-read dependency")

    # 4d-3. Reverse traceability for every primary coverage link: the named
    # test must itself carry the edge case, or the relationship is one-way and
    # a future edit can remove the evidence while the matrix still claims it.
    for did, primary in dpe_primary.items():
        if dpe_status.get(did) not in ("COVERED", "PARTIAL"):
            continue
        for tid in re.findall(r"DPA-(\d{3})", primary):
            if tid in dpa_dpe and did not in dpa_dpe[tid]:
                out.append(f"DPE-{did} primary test DPA-{tid} does not cite it")

    # 4e. The two audit-corrected workflow references.
    if "§12.5" not in blocks.get("001", ""):
        out.append("DPW-001 does not cite §12.5 for the empty state")
    if "§12.7" in blocks.get("001", ""):
        out.append("DPW-001 still cites §12.7")
    if "§12.2" not in blocks.get("002", "") or "B-08 §13.2" not in blocks.get("002", ""):
        out.append("DPW-002 does not cite §12.2 and B-08 §13.2")
    if "§12.4" in blocks.get("002", ""):
        out.append("DPW-002 still cites §12.4")

    # 4f. Every local § reference must resolve to a heading or bold subsection.
    nums = set(re.findall(r"^#{2,3} (\d+(?:\.\d+)?)", text, re.M))
    nums |= set(re.findall(r"^\*\*(\d+(?:\.\d+)?) ", text, re.M))
    for m in re.finditer(r"§(\d+(?:\.\d+)?)", text):
        line = text[text.rfind("\n", 0, m.start()) + 1:text.find("\n", m.start())]
        if any(tag in line for tag in ("B-02", "B-03", "B-04", "B-05", "B-06", "B-07", "B-08")):
            continue  # cross-document reference; the owning document resolves it
        if m.group(1) not in nums:
            out.append(f"unresolved internal reference §{m.group(1)}: {line[:70]}")

    # 5. Traceability table: REQ-012 and REQ-514..533, each with a test.
    trace = section(text, "## 15. Requirements traceability", "## 16. Release-gate evidence")
    rows = re.findall(r"^\| `REQ-(\d{3})` \|", trace, re.M)
    if sorted(rows) != sorted(valid_req):
        out.append(f"traceability rows are not REQ-012 + 514..533 (count {len(rows)})")
    req_rows: dict[str, list[str]] = {}
    for line in trace.splitlines():
        if not re.match(r"^\| `REQ-\d{3}` \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) != 12:
            out.append("a traceability row does not have 10 columns")
            continue
        rid = re.search(r"REQ-(\d{3})", cells[1]).group(1)
        if rid in req_rows:
            out.append(f"duplicate traceability row REQ-{rid}")
        req_rows[rid] = cells
        if "DPA-" not in line:
            # A requirement may be honestly deferred when the owning system does
            # not exist yet. It must name that owner and must not claim coverage.
            if not (rid == "518" and "Deferred" in cells[10] and "Prompt 10" in line):
                out.append(f"REQ-{rid} has no acceptance test and is not a named deferred dependency")
        if len(cells[9]) < 8 or not re.search(r"Direct|Document|Arithmetic|Deferred|Partial", cells[9]):
            out.append(f"REQ-{rid} has no verification rationale")
        for d in re.findall(r"DPA-(\d{3})", cells[8]):
            if d not in tests:
                out.append(f"REQ-{rid} cites nonexistent DPA-{d}")

    # 4b-2. The five requirement links repaired by 08C-D.
    req514 = req_rows.get("514", [])
    if req514 and "DPE-054" in req514[7]:
        out.append("REQ-514 still cites the privacy case DPE-054")
    req515 = req_rows.get("515", [])
    if req515 and "DPE-001" in req515[7]:
        out.append("REQ-515 still cites the logout case DPE-001")
    for rid, needed in (("519", ("076",)), ("532", ("076", "077", "083")),
                        ("533", ("080", "081", "082", "084"))):
        row = req_rows.get(rid)
        if row:
            linked = expand_dpa(row[8])
            for d in needed:
                if d not in linked:
                    out.append(f"REQ-{rid} omits supporting DPA-{d}")

    # 5b. Exhaustive bidirectional ledger (§15.5).
    ledger_text = section(text, "**15.5 Exhaustive bidirectional relationship matrix", "**15.6")
    ledger_types: dict[tuple[str, str], str] = {}
    ledger_groups: dict[str, tuple[int, int, int]] = {}
    ledger_deferred: set[str] = set()
    current: str | None = None
    for line in ledger_text.splitlines():
        gm = re.match(r"^\*\*REQ-(\d{3}) — .+?\*\* (\d+) direct, (\d+) supporting, (\d+) deferred\.$", line)
        if gm:
            current = gm.group(1)
            if current in ledger_groups:
                out.append(f"duplicate ledger group REQ-{current}")
            ledger_groups[current] = (int(gm.group(2)), int(gm.group(3)), int(gm.group(4)))
            continue
        if current is None or not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) != 10:
            if "**DIRECT**" in line or "**SUPPORTING**" in line or "**DEFERRED**" in line:
                out.append(f"ledger row under REQ-{current} does not have 8 columns")
            continue
        test, rtype, scenario, evidence, dpe_cell, rule, dependency, status = cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7], cells[8]
        if test in ("Test", "---") or rtype in ("Type", "---"):
            continue  # the repeated table header and separator
        if rtype == "**DEFERRED**":
            if test != "—" or current != "518" or "Prompt 10" not in dependency:
                out.append(f"ledger deferred row under REQ-{current} is not the named Prompt 10 dependency")
            ledger_deferred.add(current)
            continue
        tm = re.fullmatch(r"`DPA-(\d{3})`", test)
        if not tm or rtype not in ("**DIRECT**", "**SUPPORTING**"):
            out.append(f"ledger row under REQ-{current} has an invalid test or relationship type")
            continue
        tid = tm.group(1)
        if tid not in tests:
            out.append(f"ledger cites nonexistent DPA-{tid}")
        key = (tid, current)
        if key in ledger_types:
            out.append(f"duplicate ledger relationship DPA-{tid}/REQ-{current}")
        ledger_types[key] = "DIRECT" if rtype == "**DIRECT**" else "SUPPORTING"
        if not scenario or not evidence or evidence == "—":
            out.append(f"ledger DPA-{tid}/REQ-{current} lacks scenario-specific evidence")
        if rtype == "**SUPPORTING**" and "does not establish" not in evidence:
            out.append(f"supporting ledger DPA-{tid}/REQ-{current} does not state what it omits")
        if dpe_cell != "—":
            for d in re.findall(r"DPE-(\d{3})", dpe_cell):
                if d not in dpes:
                    out.append(f"ledger DPA-{tid} cites undefined DPE-{d}")
        for d in re.findall(r"DIP-(\d{3}[a-z]?)", rule):
            if d not in defined_dip:
                out.append(f"ledger DPA-{tid} cites undefined DIP-{d}")

    direct = {k for k, v in ledger_types.items() if v == "DIRECT"}
    supporting = {k for k, v in ledger_types.items() if v == "SUPPORTING"}
    if len(ledger_types) != 117 or len(direct) != 101 or len(supporting) != 16:
        out.append(f"ledger totals are not 117/101/16 ({len(ledger_types)}/{len(direct)}/{len(supporting)})")
    if ledger_deferred != {"518"}:
        out.append(f"ledger deferred rows are not exactly REQ-518: {sorted(ledger_deferred)}")
    if set(ledger_groups) != valid_req:
        out.append(f"ledger groups are not all 21 requirements: {sorted(set(ledger_groups) ^ valid_req)}")

    # Every test-side claim must be classified, and every ledger row must be
    # claimed by the test row. A missing pair is a one-way reference.
    for tid, reqs in test_reqs.items():
        for rid in reqs:
            if (tid, rid) not in ledger_types:
                out.append(f"DPA-{tid} claims REQ-{rid} but the ledger omits it")
    for (tid, rid), rtype in ledger_types.items():
        if rid not in test_reqs.get(tid, set()):
            out.append(f"ledger {rtype} DPA-{tid}/REQ-{rid} is absent from the test row")
        if rid not in req_rows:
            out.append(f"ledger cites unregistered requirement REQ-{rid}")
            continue
        req_direct = expand_dpa(req_rows[rid][8])
        if rtype == "DIRECT" and tid not in req_direct:
            out.append(f"direct ledger DPA-{tid}/REQ-{rid} is absent from the requirement row")
        if rtype == "SUPPORTING" and tid in req_direct:
            out.append(f"supporting ledger DPA-{tid}/REQ-{rid} is counted as direct")

    # The requirement summary and the ledger must describe the same direct set.
    for rid, row in req_rows.items():
        req_direct = expand_dpa(row[8])
        ledger_direct = {tid for (tid, r) in direct if r == rid}
        if req_direct != ledger_direct:
            out.append(f"REQ-{rid} direct tests disagree with the ledger")
        if rid == "518":
            if req_direct or row[10].find("Deferred") < 0:
                out.append("REQ-518 is not the single deferred, test-free requirement")
        elif "Deferred" in row[10]:
            out.append(f"REQ-{rid} is marked Deferred but has direct tests")
    for rid, (dc, sc, df) in ledger_groups.items():
        calc_d = sum(1 for (tid, r) in direct if r == rid)
        calc_s = sum(1 for (tid, r) in supporting if r == rid)
        calc_f = 1 if rid in ledger_deferred else 0
        if (dc, sc, df) != (calc_d, calc_s, calc_f):
            out.append(f"REQ-{rid} ledger group counts disagree with its rows")
    if sum(1 for rid in req_rows if rid != "518" and not expand_dpa(req_rows[rid][8])) > 0:
        out.append("a non-deferred requirement has no direct test")

    # 6. Formula traceability: all twelve, each with a workflow and a test.
    ftrace = section(text, "**15.3 Formula traceability.**", "**15.4 Decisions")
    fids = sorted({m.group(1) for m in re.finditer(r"^\\| `F-DP-(\d{3})", ftrace, re.M)})
    if fids != [f"{n:03d}" for n in range(1, 13)]:
        out.append(f"formula traceability is not F-DP-001..012: {fids}")
    for line in ftrace.splitlines():
        if re.match(r"^\| `F-DP-\d{3}` \|", line):
            if "DPW-" not in line or "DPA-" not in line:
                out.append("a formula row lacks a workflow or a test")

    # 7. Nine notification events, no tenth.
    notif = section(text, "**11.1 The nine events are closed.**", "**11.2")
    nids = re.findall(r"^\| `N(\d)` \|", notif, re.M)
    if nids != [str(n) for n in range(1, 10)]:
        out.append(f"notification table is not N1..N9: {nids}")
    if re.search(r"^\| `N(?:1[0-9]|[2-9][0-9])` \|", text, re.M):
        out.append("a notification ID beyond N9 was introduced")

    # 8. Failure codes: exactly the fifteen B-08 codes, no sixteenth.
    dpf = sorted({int(n) for n in re.findall(r"DPF-(\d{2})", text)})
    if dpf != list(range(1, 16)):
        out.append(f"DPF codes are not 01..15: {dpf}")

    # 9. No re-introduced proposal state.
    for state in ("COUNTERED", "INVALIDATED", "DRAFT"):
        for line in text.splitlines():
            if f"`{state}`" in line and "Not " not in line:
                out.append(f"{state} appears outside a 'Not adopted' row: {line[:80]}")
                break

    # 10. Authority, consent, silence and the Prompt 09 boundary.
    low = text.lower()
    for phrase in ("silence is never consent", "never makes a discretionary",
                   "no delegation", "dpf-03", "ud-039", "prompt 09"):
        if phrase not in low:
            out.append(f"required authority/boundary phrase missing: {phrase}")
    if re.search(r"silence (?:may|can|does) (?:be|count as) consent", low):
        out.append("a silence-as-consent contradiction was introduced")
    for m in re.finditer(r"automatically (?:accept|reject|declare|break|renew|sign|sanction)", low):
        line = low[low.rfind("\n", 0, m.start()) + 1:low.find("\n", m.start())]
        if not any(neg in line for neg in ("never", "must not", "does not", "cannot", "no ")):
            out.append(f"unapproved automatic diplomatic action: {line[:80]}")
            break

    # 11. Global Trade gates preserved, not marked passed.
    gates = section(text, "**16.1 The six approved gates", "**16.2")
    rows = re.findall(r"^\| \*\*G-(\d)\*\* \| [^|]+ \| \*\*([A-Z ]+)\*\* \|", gates, re.M)
    status = {n: s.strip() for n, s in rows}
    if sorted(status) != [str(n) for n in range(1, 7)]:
        out.append(f"gate rows are not G-1..G-6: {sorted(status)}")
    if list(status.values()).count("NOT MET") != 5 or list(status.values()).count("PARTIAL") != 1:
        out.append("gate statuses no longer read five NOT MET and one PARTIAL")

    # 12. Claimed counts match the document.
    if "30 workflows, 54 edge cases, 88 acceptance tests" not in text:
        out.append("§1.6 counts do not state 30/54/88")
    spans = section(text, "**1.5 Identifier spaces", "**1.6")
    for span in ("`DPW-001`…`DPW-030`", "`DPE-001`…`DPE-054`", "`DPA-001`…`DPA-088`"):
        if span not in spans:
            out.append(f"§1.5 identifier space does not state {span}")

    return out


def log_problems(text: str) -> list[str]:
    """The 08C-C entry must count the findings it actually lists."""
    out: list[str] = []
    m = re.search(r"found (five|seven|eight|nine) more", text)
    if not m:
        out.append("progress log has no 08C-C finding count")
        return out
    start = text.rfind("\n", 0, m.start()) + 1
    end = text.find("\n\n", m.end())
    paragraph = text[start:end if end > 0 else len(text)]
    paragraph = paragraph.split("Several tests")[0]
    listed = sorted(set(re.findall(r"DPE-(\d{3})", paragraph)))
    words = {"five": 5, "seven": 7, "eight": 8, "nine": 9}
    if words[m.group(1)] != len(listed):
        out.append(f"progress log says {m.group(1)} findings but lists {len(listed)}")
    return out


def edit_ledger(text: str, old: str, new: str, occurrence: int = 1) -> str:
    """Apply a mutation only inside the §15.5 ledger."""
    i = text.index("**15.5 Exhaustive bidirectional relationship matrix")
    j = text.index("**15.6", i)
    block = text[i:j]
    k = -1
    for _ in range(occurrence):
        k = block.index(old, k + 1)
    return text[:i] + block[:k] + block[k:].replace(old, new, 1) + text[j:]


def run_self_test() -> int:
    text = rd(WORK)
    b08 = rd(B08)
    cases = [
        ("DPE points at a nonexistent test",
         lambda t: t.replace("| `DPE-001` | Player logs out with a proposal pending | Disconnect must not change consent state | `DPA-073` |",
                             "| `DPE-001` | Player logs out with a proposal pending | Disconnect must not change consent state | `DPA-999` |", 1),
         "maps to nonexistent DPA-999"),
        ("test points at a nonexistent edge case",
         lambda t: t.replace("| `DPA-001` | 003 | — |", "| `DPA-001` | 003 | 099 |", 1),
         "undefined edge case DPE-099"),
        ("COVERED row without a test",
         lambda t: t.replace("| `DPE-002` | Nation ownership changes | Pending consent is not inherited; active treaties persist | `DPA-002` |",
                             "| `DPE-002` | Nation ownership changes | Pending consent is not inherited; active treaties persist | — |", 1),
         "is COVERED but names no test"),
        ("empty coverage assertion",
         lambda t: t.replace("Pre-existing `DP-T02` remains `ACTIVE`; the old session is refused; only the new owner's acceptance is recorded",
                             "", 1),
         "empty coverage assertion"),
        ("wrong section heading range",
         lambda t: t.replace("(`DPA-001`…`DPA-026`, `DPA-073`)", "(`DPA-001`…`DPA-012`)", 1),
         "heading IDs do not match"),
        ("summary count mismatch",
         lambda t: t.replace("27+15+10+7+11+11+7 = 88", "27+15+10+7+11+11+7 = 87", 1),
         "arithmetic line is not"),
        ("DPW-001 cites the wrong empty-state section",
         lambda t: t.replace("an error (§12.5)", "an error (§12.7)", 1),
         "DPW-001"),
        ("DPW-002 cites the wrong visibility section",
         lambda t: t.replace("(§12.2; B-08 §13.2)", "(§12.4; B-08 §13.2)", 1),
         "DPW-002"),
        ("sovereignty contradiction in a test",
         lambda t: t.replace("A→B `HOSTILE`; B→A `NEUTRAL`; one directional change",
                             "A→B `HOSTILE`; the system accepts for the player", 1),
         "sovereignty contradiction"),
        ("silence treated as consent in a test",
         lambda t: t.replace("| Advance to 1036 | `EXPIRED` at step 1; both notified once |",
                             "| Advance to 1036 | `EXPIRED`; silence counts as acceptance |", 1),
         "treats silence as consent"),
        ("introduction loses the authority rule",
         lambda t: t.replace("it never makes a discretionary diplomatic decision for a player",
                             "it may make a discretionary diplomatic decision for a player", 1),
         "authority/boundary phrase"),
        ("unapproved automatic diplomacy",
         lambda t: t.replace("**7.11 Coverage totals.**",
                             "**7.11 Coverage totals.** The system automatically accepts any pending proposal.", 1),
         "automatic diplomatic action"),
        ("Global Trade gate changed",
         lambda t: t.replace("| **G-1** | Identity and anti-multi integrity implemented | **NOT MET** |",
                             "| **G-1** | Identity and anti-multi integrity implemented | **MET** |", 1),
         "gate statuses no longer read"),
        ("stale identifier range",
         lambda t: t.replace("`DPA-001`…`DPA-088`", "`DPA-001`…`DPA-072`", 1),
         "§1.5 identifier space does not state"),
        ("coverage total mismatch",
         lambda t: t.replace("**52 COVERED** and **2 PARTIAL**", "**54 COVERED** and **0 PARTIAL**", 1),
         "§7.11 total"),
        ("stale 53/1 coverage summary",
         lambda t: t.replace("**52 COVERED** and **2 PARTIAL**", "**53 COVERED** and **1 PARTIAL**", 1),
         "§7.11 total for COVERED is not 52"),
        ("DPE-054 COVERED while its audit dependency is deferred",
         lambda t: t.replace("| **PARTIAL** | The privileged-read audit is Prompt 12's under DIP-121; no B-08 test can assert it. |",
                             "| **COVERED** | The privileged-read audit is Prompt 12's under DIP-121; no B-08 test can assert it. |", 1),
         "must be PARTIAL"),
        ("DPE-054 loses the notification-privacy test",
         lambda t: t.replace("| `DPE-054` | Unauthorized history or notification leak | Visibility matrix holds | `DPA-065` | `DPA-068`, `DPA-087` |",
                             "| `DPE-054` | Unauthorized history or notification leak | Visibility matrix holds | `DPA-065` | `DPA-068` |", 1),
         "does not link the notification-privacy test"),
        ("DPE-051 linked only to generic idempotency",
         lambda t: t.replace("| `DPE-051` | Replayed acceptance | Idempotent decision | `DPA-088` | `DPA-004` |",
                             "| `DPE-051` | Replayed acceptance | Idempotent decision | `DPA-004` | — |", 1),
         "acceptance-replay test DPA-088"),
        ("REQ-514 linked to the privacy edge case",
         lambda t: t.replace("| `REQ-514` | Three layers: directional posture, mutual agreement, separate effect | D-123 | DIP-002 | — | DPW-001, DPW-002 | — |",
                             "| `REQ-514` | Three layers: directional posture, mutual agreement, separate effect | D-123 | DIP-002 | — | DPW-001, DPW-002 | DPE-054 |", 1),
         "REQ-514 still cites"),
        ("REQ-515 linked to the logout edge case",
         lambda t: t.replace("| `REQ-515` | One directional public posture per pair; default `NEUTRAL` | D-123 | DIP-023, DIP-030 | — | DPW-003 | — |",
                             "| `REQ-515` | One directional public posture per pair; default `NEUTRAL` | D-123 | DIP-023, DIP-030 | — | DPW-003 | DPE-001 |", 1),
         "REQ-515 still cites"),
        ("requirement omits a supporting test",
         lambda t: t.replace("| DPA-003, DPA-004, DPA-021, DPA-025, DPA-032, DPA-035, DPA-041, DPA-043, DPA-070, DPA-080, DPA-081, DPA-082, DPA-084, DPA-088 |",
                             "| DPA-003, DPA-004, DPA-021, DPA-025, DPA-032, DPA-035, DPA-041, DPA-043, DPA-070, DPA-080, DPA-082, DPA-084, DPA-088 |", 1),
         "REQ-533 omits supporting DPA-081"),
        ("primary coverage link is not mirrored in the test",
         lambda t: t.replace("| `DPA-065` | 002 | 054 |", "| `DPA-065` | 002 | — |", 1),
         "primary test DPA-065 does not cite it"),
        ("test claims a requirement the ledger omits",
         lambda t: edit_ledger(t, "| `DPA-041` | **DIRECT** | Proposal submitted 1000; pair frozen",
                              "| `DPA-999` | **DIRECT** | Proposal submitted 1000; pair frozen", 2),
         "claims REQ-532 but the ledger omits it"),
        ("supporting ledger row counted as direct",
         lambda t: edit_ledger(t, "| `DPA-065` | **DIRECT**", "| `DPA-065` | **SUPPORTING**"),
         "counted as direct"),
        ("ledger group count disagrees with its rows",
         lambda t: edit_ledger(t, "4 direct, 0 supporting, 0 deferred.", "3 direct, 0 supporting, 0 deferred."),
         "REQ-012 ledger group counts"),
        ("requirement summary counts a supporting test as direct",
         lambda t: t.replace("| DPA-003, DPA-004, DPA-021, DPA-025, DPA-032, DPA-035, DPA-041, DPA-043, DPA-070, DPA-080, DPA-081, DPA-082, DPA-084, DPA-088 | Direct: boundary order",
                             "| DPA-003, DPA-004, DPA-021, DPA-025, DPA-032, DPA-035, DPA-041, DPA-043, DPA-070, DPA-080, DPA-081, DPA-082, DPA-084, DPA-087, DPA-088 | Direct: boundary order", 1),
         "REQ-533 direct tests disagree with the ledger"),
        ("duplicate ledger relationship",
         lambda t: edit_ledger(t, "| `DPA-068` | **SUPPORTING**", "| `DPA-066` | **SUPPORTING**"),
         "duplicate ledger relationship"),
    ]
    failures = 0
    for name, mutate, expected in cases:
        mutated = mutate(text)
        found = problems(mutated, b08)
        hit = any(expected in p for p in found)
        print(f"SELFTEST {'PASS' if hit else 'FAIL'}  {name} -> {(found or ['undetected'])[0][:110]}")
        failures += 0 if hit else 1
    clean = problems(text, b08)
    print(f"SELFTEST {'PASS' if not clean else 'FAIL'}  corrected files -> {(clean or ['no problems'])[0][:110]}")
    failures += 0 if not clean else 1
    log = rd(LOG)
    stale_log = log.replace("found seven more", "found five more", 1)
    found_log = log_problems(stale_log)
    log_hit = any("says five findings but lists" in p for p in found_log)
    print(f"SELFTEST {'PASS' if log_hit else 'FAIL'}  progress-log count -> {(found_log or ['undetected'])[0][:110]}")
    failures += 0 if log_hit else 1
    clean_log = log_problems(log)
    print(f"SELFTEST {'PASS' if not clean_log else 'FAIL'}  corrected progress log -> {(clean_log or ['no problems'])[0][:110]}")
    failures += 0 if not clean_log else 1
    total = len(cases) + 3
    if failures:
        print(f"SELFTEST: {failures} of {total} checks failed")
        return 2
    print(f"SELFTEST: {total}/{total} checks pass ({len(cases)} defect guards + clean docs + progress-log guard + clean log)")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return run_self_test()
    if not WORK.exists():
        print(f"MISSING: {WORK}")
        return 1
    found = problems(rd(WORK), rd(B08)) + log_problems(rd(LOG))
    if found:
        print("\nDIPLOMACY WORKFLOW FAILURES:")
        for p in found:
            print("  -", p)
        return 1
    print("\nDIPLOMACY WORKFLOWS: 17 groups checked (sections, 30 workflows x 23 fields, "
          "54 edge cases, 88 tests, section ranges, 54-row coverage matrix, targeted "
          "references, traceability, formulas, notifications, failure codes, states, "
          "authority, gates, counts), 0 failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
