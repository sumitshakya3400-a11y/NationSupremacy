#!/usr/bin/env python3
"""Document checks for the Prompt 09C Alliance workflows and acceptance matrix.

What this proves
----------------
* `docs/stage-2/16_alliances_workflows_acceptance.md` has sections 1..19 and
  is the only canonical 09C companion.
* The workflow catalogue is exactly `ALW-001`..`ALW-049`, each block carrying
  all 18 fields, with a test name in field 18.
* The edge-case register is `ALE-001`..`ALE-065`; every row cites a real rule
  (`ALL-001`..`ALL-226`) and a real acceptance test.
* The acceptance matrix is `AAT-001`..`AAT-132`; the eight summary subsection
  headings match their tables exactly, and every test/workflow/edge reference
  resolves. Each test also has a §14.9 execution record with all 26 mandatory
  fields and a prescribed evidence status.
* The classified registers in §15.14–§15.16 cover every source and companion
  identifier with DIRECT, SUPPORTING, DEFERRED or NOT APPLICABLE, an
  authorisation state and a downstream owner where deferred. Every deferred
  row names an owner and every `NOT APPLICABLE` row carries a reason.
* Eight document-level acceptance checks (`AAT-125`–`AAT-132`) audit
  requirement, contract, formula, audit-event, reference, deferral and orphan
  coverage, and are `DOCUMENT-VALIDATED` only when this validator passes.
* The document does not claim `COMPLETE` while any `09C-AC` or `C-09C` item is
  not met.
* Succession/contact authority and the owner-reserved permission boundary keep
  their required negations, and §15.12 uses the official B-section titles.
* Notifications `AN-01`..`AN-16` are defined once and used; the security matrix
  has 25 rows; failure codes 01..29 are accounted for and no workflow emits
  the undefined `ALF-13`..`ALF-20`.
* The traceability ledgers expand to `ALL-001`..`ALL-226`,
  `REQ-534`..`REQ-653`, `AX-01`..`AX-30`, `F-AL-001`..`F-AL-008`,
  `AUD-AL-001`..`AUD-AL-019`, `D-135`..`D-142`, `DD-151`..`DD-165`,
  `UD-040`..`UD-049`, `ALW-001`..`ALW-049` and `AAT-001`..`AAT-132`, with no
  duplicate range membership.
* `UD-040`..`UD-049` are still Open in the unresolved register; the companion
  claims no resolution.
* Succession, contact and general-permission workflows do not present an
  owner-reserved policy as executable; only the narrow tax-management set is
  treated as authorized. Global Trade `G-1`..`G-6` and the twelve internal
  release dependencies remain NOT MET.
* All 30 `09C-AC-*` acceptance criteria are recorded with a status.

What this does NOT prove
-----------------------
No game code, migration, endpoint, scheduler, ledger, treaty service, attack
validator, notification or UI exists. These are documentation checks against a
specification. They do not establish runtime enforcement, concurrency safety,
security or playability, and they settle no owner-reserved decision (D-012).

Usage
-----
    python verify_alliance_workflows.py
    python verify_alliance_workflows.py --self-test
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
WORK = DOCS / "stage-2" / "16_alliances_workflows_acceptance.md"
UD = DOCS / "stage-2" / "05_unresolved_design_decisions.md"

checks: list[tuple[bool, str, str]] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append((bool(ok), label, detail))


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def section(text: str, start: str, end: str) -> str:
    try:
        i = text.index(start)
        j = text.index(end, i + len(start))
        return text[i:j]
    except ValueError:
        return ""


def sub_block(text: str, start: str, end: str) -> str:
    """Slice from `start` to the next `end`; return the tail when `end` is absent."""
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(end, i + len(start))
    return text[i:j] if j >= 0 else text[i:]


def expand(refs: str, prefix: str) -> set[str]:
    """Expand `PREFIX-001`…`PREFIX-026` and collect standalone IDs."""
    found: set[str] = set()
    for pattern in (
        rf"`{prefix}-(\d+)`\s*[–…-]\s*`{prefix}-(\d+)`",
        rf"{prefix}-(\d+)\s*[–…-]\s*{prefix}-(\d+)",
    ):
        for a, b in re.findall(pattern, refs):
            found |= {f"{n:03d}" for n in range(int(a), int(b) + 1)}
    for n in re.findall(rf"{prefix}-(\d+)", refs):
        found.add(f"{int(n):03d}")
    return found


def workflow_blocks(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    starts = list(re.finditer(r"^#### ALW-(\d{3}) — ", text, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.find("## 6.", m.end())
        blocks[m.group(1)] = text[m.start():end if end > 0 else len(text)]
    return blocks


def test_sections(text: str) -> dict[str, tuple[set[str], set[str]]]:
    out: dict[str, tuple[set[str], set[str]]] = {}
    starts = list(re.finditer(r"^### 14\.(\d+) ([^\n]+)$", text, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.find("## 15.", m.end())
        block = text[m.start():end if end > 0 else len(text)]
        heading = expand(m.group(2), "AAT")
        rows = set(re.findall(r"^\| `AAT-(\d{3})` \|", block, re.M))
        out[f"14.{m.group(1)}"] = (heading, rows)
    return out


def test_blocks(text: str) -> dict[str, str]:
    """Return the full 26-field detail block for each `#### `AAT-nnn`` heading."""
    blocks: dict[str, str] = {}
    starts = list(re.finditer(r"^#### `AAT-(\d{3})` — ", text, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.find("## 15.", m.end())
        blocks[m.group(1)] = text[m.start():end if end > 0 else len(text)]
    return blocks


def problems(text: str, ud: str) -> list[str]:
    out: list[str] = []

    # 1. Required sections 1..19, in order, with the expected subject matter.
    headings = [int(n) for n in re.findall(r"^## (\d+)\. ", text, re.M)]
    if headings != list(range(1, 20)):
        out.append(f"section headings are not 1..19: {headings}")
    expected = {
        1: "Scope", 2: "Canonical", 3: "Actors", 4: "Lifecycle",
        5: "Workflow", 6: "transition", 7: "Cross-lifecycle",
        8: "Player journeys", 9: "Edge-case", 10: "Failure",
        11: "Concurrency", 12: "Notification", 13: "Threat",
        14: "Acceptance-test", 15: "traceability", 16: "handoff",
        17: "Release-gate", 18: "Implementation", 19: "Acceptance",
    }
    for n, word in expected.items():
        m = re.search(rf"^## {n}\. ([^\n]+)$", text, re.M)
        if not m or word.lower() not in m.group(1).lower():
            out.append(f"§{n} heading does not mention {word!r}")

    # 2. No placeholder or continuation sentinel survives.
    for bad in ("<!-- 09C-CONTINUE -->", "TODO", "TBD", "PLACEHOLDER", "lorem ipsum"):
        if bad.lower() in text.lower():
            out.append(f"document still contains placeholder {bad!r}")

    # 3. Workflows: 49 sequential, each with all 18 fields and a test citation.
    blocks = workflow_blocks(text)
    ids = sorted(blocks)
    if ids != [f"{n:03d}" for n in range(1, 50)]:
        out.append(f"ALW IDs are not 001..049: {ids[:5]}…{ids[-3:]}")
    for wid in ids:
        fields = {int(n) for n in re.findall(r"^\| (\d{1,2}) \| \*\*", blocks[wid], re.M)}
        if fields != set(range(1, 19)):
            out.append(f"ALW-{wid} is missing fields {sorted(set(range(1, 19)) - fields)}")
        f18 = re.search(r"^\| 18 \| \*\*Rules[^\n]+$", blocks[wid], re.M)
        if not f18 or not re.search(r"AAT-\d{3}", f18.group(0)):
            out.append(f"ALW-{wid} field 18 names no acceptance test")
        # 18 fields exactly once: a duplicated row would hide a missing one.
        rows = re.findall(r"^\| (\d{1,2}) \| \*\*", blocks[wid], re.M)
        if len(rows) != len(set(rows)):
            out.append(f"ALW-{wid} repeats a field number")
        for code in re.findall(r"ALF-(\d{2})", blocks[wid]):
            if 13 <= int(code) <= 20:
                out.append(f"ALW-{wid} emits undefined failure code ALF-{code}")

    # 4. Edge cases: 65 sequential; every row cites a real rule and test.
    catalogue = section(text, "## 9. Edge-case register", "## 10. Failure")
    ale_rows = [ln for ln in catalogue.splitlines() if re.match(r"^\| `ALE-\d{3}` \|", ln)]
    ale_ids = [re.search(r"ALE-(\d{3})", ln).group(1) for ln in ale_rows]
    if sorted(ale_ids) != [f"{n:03d}" for n in range(1, 66)] or len(set(ale_ids)) != len(ale_ids):
        out.append(f"ALE IDs are not 001..065 once each (count {len(ale_ids)})")
    ale_rules: dict[str, set[str]] = {}
    ale_tests: dict[str, set[str]] = {}
    for ln in ale_rows:
        cells = [c.strip() for c in ln.split("|")]
        if len(cells) != 10:
            out.append("an ALE row does not have 8 columns")
            continue
        aid = re.search(r"ALE-(\d{3})", cells[1]).group(1)
        ale_rules[aid] = {f"{int(n):03d}" for n in re.findall(r"ALL-(\d{3})", cells[6])}
        ale_tests[aid] = {f"{int(n):03d}" for n in re.findall(r"AAT-(\d{3})", cells[7])}
        if not ale_rules[aid]:
            out.append(f"ALE-{aid} cites no rule")
        if not ale_tests[aid]:
            out.append(f"ALE-{aid} cites no acceptance test")
        for n in ale_rules[aid]:
            if not 1 <= int(n) <= 226:
                out.append(f"ALE-{aid} cites out-of-range ALL-{n}")
        owner = cells[8]
        for u in re.findall(r"UD-(\d{3})", owner):
            if not 40 <= int(u) <= 49:
                out.append(f"ALE-{aid} attributes ownership to unexpected UD-{u}")
        if "Yes" in owner and not re.search(r"(?:UD-0(?:4\d)|D-14\d)", owner):
            out.append(f"ALE-{aid} is owner-dependent but names no UD")

    # 5. Tests: 132 sequential and every reference resolves.
    matrix = section(text, "## 14. Acceptance-test matrix", "## 15. traceability")
    if not matrix:
        matrix = section(text, "## 14. Acceptance-test matrix", "## 15.")
    test_rows = [ln for ln in matrix.splitlines() if re.match(r"^\| `AAT-\d{3}` \|", ln)]
    test_ids = [re.search(r"AAT-(\d{3})", ln).group(1) for ln in test_rows]
    if sorted(test_ids) != [f"{n:03d}" for n in range(1, 133)] or len(set(test_ids)) != len(test_ids):
        out.append(f"AAT IDs are not 001..132 once each (count {len(test_ids)})")
    tests = set(test_ids)
    used_wf: set[str] = set()
    for ln in test_rows:
        cells = [c.strip() for c in ln.split("|")]
        if len(cells) < 9:
            out.append("an AAT row does not have 7 columns")
            continue
        tid, area = re.search(r"AAT-(\d{3})", cells[1]).group(1), cells[2]
        for w in re.findall(r"ALW-(\d{3})", area):
            if w not in ids:
                out.append(f"AAT-{tid} cites undefined ALW-{w}")
            else:
                used_wf.add(w)
        if not cells[5] or not cells[7]:
            out.append(f"AAT-{tid} lacks an expected or pass condition")
        evidence = (cells[5] + " " + cells[7]).lower()
        if re.search(r"\b(?:system|game) (?:may |will |can )?accepts?\b", evidence):
            out.append(f"AAT-{tid} lets the system accept for a player")
        if re.search(r"\bsilence\b[^.]{0,30}\b(?:consent|accept)", evidence):
            out.append(f"AAT-{tid} treats silence as consent")
        if re.search(r"automatically (?:accept|reject|declare|break|renew|sign|sanction)", evidence):
            out.append(f"AAT-{tid} invents an automatic action")

    # 5b. Each §14 summary heading lists exactly the tests in its own table.
    sections = {k: v for k, v in test_sections(text).items() if k != "14.9"}
    if len(sections) != 8:
        out.append(f"expected eight §14 summary subsections, found {len(sections)}")
    for title, (heading_ids, row_ids) in sorted(sections.items()):
        if heading_ids != row_ids:
            out.append(
                f"§{title} heading IDs do not match its table: "
                f"missing {sorted(heading_ids - row_ids)[:4]}, "
                f"extra {sorted(row_ids - heading_ids)[:4]}"
            )
    union = set().union(*(v[1] for v in sections.values())) if sections else set()
    if union != tests:
        out.append(f"§14 subsection tables do not union to AAT-001..132 "
                   f"(missing {sorted(tests - union)[:4]})")

    # 5b2. §14.9: every test has a 26-field execution record.
    detail = section(text, "### 14.9 Detailed acceptance-test records", "## 15. ")
    field_names = [
        "ID", "Name", "Objective", "Category", "Workflow",
        "Edge case or justified N/A", "Actor identities",
        "Permissions / authentication", "Preconditions", "Test data",
        "Numbered actions", "Expected visible result", "Outcome",
        "State transition", "Unchanged state", "Audit or N/A",
        "Notification or N/A", "Failure code or N/A", "Security assertion",
        "ALL", "REQ", "AX or N/A", "F-AL or N/A", "D / DD / UD",
        "Evidence required", "Evidence status",
    ]
    evidence_statuses = {
        "SPECIFICATION-DEFINED", "DOCUMENT-VALIDATED", "IMPLEMENTATION-PENDING",
        "RUNTIME-TEST-PENDING", "MANUAL-ACCEPTANCE-PENDING", "BLOCKED",
        "MANUALLY-VERIFIED",
    }
    detail_heads = re.findall(r"^#### `AAT-(\d{3})` — ", detail, re.M)
    if detail_heads != [f"{n:03d}" for n in range(1, 133)]:
        out.append(f"§14.9 detail records are not AAT-001..132 once each (count {len(detail_heads)})")
    starts = list(re.finditer(r"^#### `AAT-(\d{3})` — ", detail, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(detail)
        block = detail[m.start():end]
        rows = re.findall(r"^\| \*\*(\d+)\. ([^*]+)\*\* \| (.*?) \|$", block, re.M)
        names = [r[1].strip() for r in rows]
        nums = [int(r[0]) for r in rows]
        if nums != list(range(1, 27)) or names != field_names:
            out.append(f"AAT-{m.group(1)} detail fields are not 1..26 in order")
        if any(not r[2].strip() for r in rows):
            out.append(f"AAT-{m.group(1)} detail record has a blank field")
        status = dict((int(n), v.strip()) for n, _, v in rows).get(26, "")
        if status not in evidence_statuses:
            out.append(f"AAT-{m.group(1)} evidence status {status!r} is not prescribed")

    # 5c. Every workflow has at least one test, and every AAT/ALW/ALE
    # elsewhere in the document resolves.
    for wid in ids:
        f18 = re.search(r"^\| 18 \| \*\*Rules[^\n]+$", blocks[wid], re.M)
        if f18:
            for t in re.findall(r"AAT-(\d{3})", f18.group(0)):
                if t not in tests:
                    out.append(f"ALW-{wid} cites nonexistent AAT-{t}")
    for t in re.findall(r"AAT-(\d{3})", text):
        if t not in tests:
            out.append(f"document cites nonexistent AAT-{t}")
    for e in re.findall(r"ALE-(\d{3})", text):
        if e not in set(ale_ids):
            out.append(f"document cites nonexistent ALE-{e}")
    for w in re.findall(r"ALW-(\d{3})", text):
        if w not in ids:
            out.append(f"document cites nonexistent ALW-{w}")
    for a in set(re.findall(r"ALF-(\d{2})", text)):
        if not 1 <= int(a) <= 29:
            out.append(f"document cites out-of-range ALF-{a}")
    for aid, ts in ale_tests.items():
        for t in ts:
            if t not in tests:
                out.append(f"ALE-{aid} cites nonexistent AAT-{t}")

    # 6. Notifications: 16 defined, all used, no reference outside 01..16.
    notif = section(text, "## 12. Notification matrix", "## 13. Threat")
    an_ids = re.findall(r"^\| `AN-(\d{2})` \|", notif, re.M)
    if an_ids != [f"{n:02d}" for n in range(1, 17)]:
        out.append(f"AN IDs are not 01..16 (count {len(an_ids)})")
    for n in set(re.findall(r"AN-(\d{2})", text)):
        if not 1 <= int(n) <= 16:
            out.append(f"document cites undefined notification AN-{n}")
    for n in an_ids:
        if len(re.findall(rf"AN-{n}\b", text)) < 2:
            out.append(f"AN-{n} is defined but never used by a workflow")

    # 7. Security matrix: 25 numbered rows.
    security = section(text, "## 13. Threat-to-control", "## 14. Acceptance-test")
    sec_rows = re.findall(r"^\| (\d+) \| ", security, re.M)
    if [int(n) for n in sec_rows] != list(range(1, 26)):
        out.append(f"security matrix rows are not 1..25: {sec_rows}")
    if "`R-AL-01`–`R-AL-21`" not in security:
        out.append("security matrix does not claim rows 1..21 are R-AL-01..21")

    # 8. Failure codes: 01..12 named, 13..20 reserved, 21..29 defined.
    failures = section(text, "## 10. Failure codes", "## 11. Concurrency")
    for n in range(1, 30):
        if n <= 20 and f"`ALF-{n:02d}`" not in failures and not (13 <= n <= 20):
            out.append(f"failure table omits ALF-{n:02d}")
        if n >= 21 and f"`ALF-{n:02d}`" not in failures:
            out.append(f"failure table omits ALF-{n:02d}")
    if "`ALF-13`–`ALF-20`" not in failures:
        out.append("failure table does not mark ALF-13..20 as reserved/undefined")

    # 9. Traceability ledgers: exact, once-only coverage.
    def ledger(start: str, end: str) -> list[str]:
        return [ln for ln in section(text, start, end).splitlines()
                if ln.startswith("| `")]

    all_rows = ledger("### 15.2 Rule ledger", "### 15.3 Requirement ledger")
    covered: dict[str, int] = {}
    for ln in all_rows:
        first = ln.split("|")[1]
        for n in expand(first, "ALL"):
            covered[n] = covered.get(n, 0) + 1
    if set(covered) != {f"{n:03d}" for n in range(1, 227)}:
        missing = sorted({f"{n:03d}" for n in range(1, 227)} - set(covered))
        out.append(f"ALL ledger does not cover 001..226; missing {missing[:8]}")
    dup = sorted(n for n, c in covered.items() if c > 1)
    if dup:
        out.append(f"ALL ledger overlaps on {dup[:8]}")

    req_rows = ledger("### 15.3 Requirement ledger", "### 15.4 Integration-contract")
    req_covered: dict[str, int] = {}
    for ln in req_rows:
        for n in expand(ln.split("|")[1], "REQ"):
            req_covered[n] = req_covered.get(n, 0) + 1
    if set(req_covered) != {f"{n:03d}" for n in range(534, 654)}:
        missing = sorted({f"{n:03d}" for n in range(534, 654)} - set(req_covered))
        out.append(f"REQ ledger does not cover 534..653; missing {missing[:8]}")
    req_dup = sorted(n for n, c in req_covered.items() if c > 1)
    if req_dup:
        out.append(f"REQ ledger overlaps on {req_dup[:8]}")
    ax_rows = ledger("### 15.4 Integration-contract", "### 15.5 Formula")
    ax_ids = [re.search(r"AX-(\d{2})", ln).group(1) for ln in ax_rows]
    if ax_ids != [f"{n:02d}" for n in range(1, 31)]:
        out.append(f"AX ledger is not AX-01..30 (count {len(ax_ids)})")

    f_rows = ledger("### 15.5 Formula", "### 15.6 Decision")
    f_ids = [re.search(r"F-AL-(\d{3})", ln).group(1) for ln in f_rows]
    if f_ids != [f"{n:03d}" for n in range(1, 9)]:
        out.append(f"formula ledger is not F-AL-001..008 (count {len(f_ids)})")

    d_rows = ledger("### 15.6 Decision", "### 15.7 Unresolved-decision")
    d_ids = [re.match(r"\| `D-(\d{3})`", ln).group(1) for ln in d_rows if re.match(r"\| `D-", ln)]
    dd_ids = [re.match(r"\| `DD-(\d{3})`", ln).group(1) for ln in d_rows if re.match(r"\| `DD-", ln)]
    if d_ids != [f"{n:03d}" for n in range(135, 143)]:
        out.append(f"decision ledger D rows are not D-135..D-142: {d_ids}")
    if dd_ids != [f"{n:03d}" for n in range(151, 166)]:
        out.append(f"decision ledger DD rows are not DD-151..DD-165 (count {len(dd_ids)})")

    ud_rows = ledger("### 15.7 Unresolved-decision", "### 15.8 Registry")
    ud_ids = [re.search(r"UD-(\d{3})", ln).group(1) for ln in ud_rows]
    if ud_ids != [f"{n:03d}" for n in range(40, 50)]:
        out.append(f"UD preservation ledger is not UD-040..049: {ud_ids}")
    register: dict[str, str] = {}
    for ln in ud.splitlines():
        m = re.match(r"\| (UD-0(?:4\d)) \|", ln)
        if m:
            register[m.group(1)] = ln
    for n in range(40, 50):
        uid = f"UD-{n:03d}"
        row = register.get(uid, "")
        if not row:
            out.append(f"{uid} missing from the unresolved register")
        elif "**Open**" not in row and "Open" not in row:
            out.append(f"{uid} is no longer Open in the unresolved register")
        if uid not in text:
            out.append(f"{uid} is not preserved in the companion")

    aud_rows = ledger("### 15.9 Audit-event", "### 15.10 Workflow reverse")
    aud_ids = [re.search(r"AUD-AL-(\d{3})", ln).group(1) for ln in aud_rows]
    if aud_ids != [f"{n:03d}" for n in range(1, 20)]:
        out.append(f"AUD-AL ledger is not 001..019 (count {len(aud_ids)})")

    wf_block = section(text, "### 15.10 Workflow reverse", "### 15.11 Edge-case")
    wf_rows = [ln for ln in wf_block.splitlines() if re.match(r"^\| [A-J] ", ln)]
    wf_covered: dict[str, int] = {}
    for ln in wf_rows:
        cells = ln.split("|")
        if len(cells) >= 3:
            for n in expand(cells[2], "ALW"):
                wf_covered[n] = wf_covered.get(n, 0) + 1
    if set(wf_covered) != {f"{n:03d}" for n in range(1, 50)}:
        out.append("§15.10 group rows do not cover ALW-001..049")
    if any(c > 1 for c in wf_covered.values()):
        out.append("§15.10 group rows overlap")

    test_rows_map = ledger("### 15.11 Edge-case", "### 15.12 Downstream")
    test_covered: dict[str, int] = {}
    for ln in test_rows_map:
        for n in expand(ln.split("|")[1], "AAT"):
            test_covered[n] = test_covered.get(n, 0) + 1
    if set(test_covered) != {f"{n:03d}" for n in range(1, 133)}:
        out.append("§15.11 rows do not cover AAT-001..132")
    if any(c > 1 for c in test_covered.values()):
        out.append("§15.11 rows overlap")

    # 9b. Classified forward register (§15.14): every source ID once, a valid
    # classification, an authorisation state and a prescribed evidence status.
    forward = section(text, "### 15.14 Classified forward register",
                      "### 15.15 Classified reverse register")
    if not forward:
        out.append("§15.14 classified forward register is missing")
    fwd_specs = [
        ("15.14.1", "ALL", 226), ("15.14.2", "REQ", 120), ("15.14.3", "AX", 30),
        ("15.14.4", "F-AL", 8), ("15.14.5", "ALF", 29), ("15.14.6", "AUD-AL", 19),
        ("15.14.7", "D/DD", 23), ("15.14.8", "UD", 10),
    ]
    classes = {"DIRECT", "SUPPORTING", "DEFERRED", "NOT APPLICABLE"}
    auths = {"approved", "narrowly authorized", "provisional", "blocked"}
    fwd_sub = forward
    for idx, (num, prefix, expected) in enumerate(fwd_specs):
        start = f"#### {num} "
        nxt = f"#### {fwd_specs[idx + 1][0]} " if idx + 1 < len(fwd_specs) else "### 15.15 "
        sub = sub_block(fwd_sub, start, nxt)
        rows = [ln for ln in sub.splitlines()
                if ln.startswith("| `") and not ln.startswith("| `ID")]
        if len(rows) != expected:
            out.append(f"§{num} has {len(rows)} rows, expected {expected}")
        seen: set[str] = set()
        for ln in rows:
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) != 12:
                out.append(f"§{num} row does not have 12 columns: {ln[:60]}")
                continue
            rid = cells[0].strip("`")
            if rid in seen:
                out.append(f"§{num} repeats {rid}")
            seen.add(rid)
            cls = cells[3].strip("* ")
            if cls not in classes:
                out.append(f"§{num} {rid} has invalid class {cls!r}")
            if cells[4] not in auths:
                out.append(f"§{num} {rid} has invalid authorisation {cells[4]!r}")
            if cells[10] not in evidence_statuses:
                out.append(f"§{num} {rid} has invalid evidence status {cells[10]!r}")
            if cls == "DEFERRED" and cells[9].strip(" `") in {"", "-", "—"}:
                out.append(f"§{num} {rid} is DEFERRED without a named owner")
            if cls == "NOT APPLICABLE" and not re.search(
                r"withdrawn|reserved|outside|not applicable|no behaviour", cells[11], re.I
            ):
                out.append(f"§{num} {rid} is NOT APPLICABLE without an explicit justification")

    # 9c. Classified reverse register (§15.15): every companion ID once.
    reverse = section(text, "### 15.15 Classified reverse register", "### 15.16 ")
    for num, prefix, expected in (
        ("15.15.1", "ALW", 49), ("15.15.2", "ALE", 65), ("15.15.3", "AAT", 132),
    ):
        start = f"#### {num} "
        if num == "15.15.1":
            nxt = "#### 15.15.2 "
        elif num == "15.15.2":
            nxt = "#### 15.15.3 "
        else:
            nxt = "### 15.16 "
        sub = sub_block(reverse, start, nxt)
        rows = [ln for ln in sub.splitlines()
                if ln.startswith(f"| `{prefix}-") and not ln.startswith("| `ID")]
        if len(rows) != expected:
            out.append(f"§{num} has {len(rows)} rows, expected {expected}")
        ids = [ln.split("|")[1].strip().strip("`") for ln in rows]
        if len(ids) != len(set(ids)):
            out.append(f"§{num} repeats a companion identifier")
        for ln in rows:
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) != 6:
                out.append(f"§{num} row does not have 6 columns: {ln[:60]}")
            elif cells[4] not in auths:
                out.append(f"§{num} {cells[0]} has invalid authorisation {cells[4]!r}")
            elif not cells[5]:
                out.append(f"§{num} {cells[0]} has no downstream-owner field")
            elif "DEFERRED" in cells[2] and cells[5].strip(" `") in {"-", "—"}:
                out.append(f"§{num} {cells[0]} is DEFERRED without a named owner")

    # 9d. §15.16 totals must add up, with no estimated count.
    totals = section(text, "### 15.16 ", "## 16. ")
    for ln in totals.splitlines():
        m = re.match(r"^\| ([A-Z0-9\-\u2013, ]+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", ln)
        if m:
            n, d, s, f, na = (int(m.group(i)) for i in range(2, 7))
            if d + s + f + na != n:
                out.append(f"§15.16 totals do not add up for {m.group(1).strip()}")
    if "132 tests" not in totals or "3,432" not in totals:
        out.append("§15.16 does not state 132 tests and 26 fields = 3,432")

    # 9d2. Every test record cites exact authoritative refs in fields 20–24,
    # and the eight traceability checks exist with document evidence.
    for n in range(125, 133):
        if f"#### `AAT-{n:03d}` — " not in detail:
            out.append(f"AAT-{n:03d} traceability check is missing from §14.9")
    if detail:
        starts = list(re.finditer(r"^#### `AAT-(\d{3})` — ", detail, re.M))
        for i, m in enumerate(starts):
            end = starts[i + 1].start() if i + 1 < len(starts) else len(detail)
            block = detail[m.start():end]
            vals = dict((int(n), v.strip()) for n, _, v in
                        re.findall(r"^\| \*\*(\d+)\. ([^*]+)\*\* \| (.*?) \|$", block, re.M))
            all_v, req_v = vals.get(20, ""), vals.get(21, "")
            ax_v, fal_v, dec_v = vals.get(22, ""), vals.get(23, ""), vals.get(24, "")
            if not re.search(r"ALL-\d{3}", all_v):
                out.append(f"AAT-{m.group(1)} field 20 cites no ALL rule")
            if not re.search(r"REQ-\d{3}", req_v):
                out.append(f"AAT-{m.group(1)} field 21 cites no REQ requirement")
            for label, value, pat in (
                ("22 AX", ax_v, r"(?:AX-\d{2}|N/A)"),
                ("23 F-AL", fal_v, r"(?:F-AL-\d{3}|N/A)"),
                ("24 D/DD/UD", dec_v, r"(?:D-\d{3}|DD-\d{3}|UD-\d{3}|N/A)"),
            ):
                if not re.search(pat, value):
                    out.append(f"AAT-{m.group(1)} field {label} is not a reference or N/A")

    # 9d3. A title or prose clause never counts as executable permission.
    for phrase in ("a role title is never accepted as evidence of permission",):
        if phrase not in section(text, "### 3.5 ", "### 3.6 "):
            out.append(f"§3.5 is missing the title boundary {phrase!r}")
    if "confers nothing" not in blocks.get("010", ""):
        out.append("ALW-010 does not deny that a position confers permission")

    # 9d4. Status honesty: COMPLETE requires every AC and every correction
    # criterion to be met. A blocking defect cannot sit behind a COMPLETE label.
    status_line = next((ln for ln in text.splitlines() if ln.startswith("**Status:**")), "")
    ac_block = section(text, "### 19.1 Acceptance criteria", "### 19.2 ")
    ac_statuses = re.findall(r"^\| `09C-AC-\d{3}` \|[^\n]*\| (MET|PARTIAL|NOT MET|BLOCKED) \|$",
                             ac_block, re.M)
    corr_block = section(text, "### 19.5 Correction acceptance checklist", "\x00")
    if not corr_block:
        corr_block = text[text.find("### 19.5 Correction acceptance checklist"):]
    corr_rows = [ln for ln in corr_block.splitlines() if re.match(r"^\| `C-09C-\d{3}` \|", ln)]
    corr_ids = [re.search(r"C-09C-(\d{3})", ln).group(1) for ln in corr_rows]
    if corr_ids != [f"{n:03d}" for n in range(1, 28)]:
        out.append(f"C-09C checklist is not 001..027 once each (count {len(corr_ids)})")
    corr_statuses = [re.search(r"\| (PASS|FAIL|PARTIAL|BLOCKED) \|$", ln) for ln in corr_rows]
    if any(m is None for m in corr_statuses):
        out.append("a C-09C criterion has no explicit PASS/FAIL/PARTIAL/BLOCKED status")
    if "COMPLETE" in status_line:
        if len(ac_statuses) != 30 or any(s != "MET" for s in ac_statuses):
            out.append("status claims COMPLETE while a 09C-AC criterion is not MET")
        if len(corr_ids) != 27 or any(m is None or m.group(1) != "PASS" for m in corr_statuses):
            out.append("status claims COMPLETE while a C-09C correction criterion is not PASS")

    # 9e. Succession/contact authority stays record-only.
    s411 = section(text, "### 4.11 ", "### 4.12 ")
    for phrase in ("record-only", "A recorded claim is **not** a decision",
                   "**does not** assign or transfer", "`UD-043`"):
        if phrase not in s411:
            out.append(f"§4.11 is missing the succession boundary phrase {phrase!r}")
    s412 = section(text, "### 4.12 ", "## 5. ")
    for phrase in ("No implied succession", "Contact is not office"):
        if phrase not in s412:
            out.append(f"§4.12 is missing the invariant {phrase!r}")
    alw012 = blocks.get("012", "")
    for phrase in ("No contact-transfer capability is approved", "No transfer branch exists",
                   "record-only"):
        if phrase not in alw012:
            out.append(f"ALW-012 is missing {phrase!r}")
    for bad in ("atomically change the contact pointer", "A → B", "permitted record change"):
        if bad in alw012:
            out.append(f"ALW-012 still describes an executable transfer: {bad!r}")
    alw013 = blocks.get("013", "")
    for phrase in ("perform **no** appointment", "no** transition to a filled office"):
        if phrase not in alw013:
            out.append(f"ALW-013 is missing {phrase!r}")

    # 9f. General permissions remain blocked; only the narrow tax set executes.
    s35 = section(text, "### 3.5 ", "### 3.6 ")
    for phrase in ("limited to the narrow tax-management set",
                   "Every other general permission assignment",
                   "blocked or unavailable", "`UD-045`"):
        if phrase not in s35:
            out.append(f"§3.5 is missing the permission boundary {phrase!r}")
    for wid in ("008", "009", "010", "011"):
        block = blocks.get(wid, "")
        if "`UD-045`" not in block:
            out.append(f"ALW-{wid} does not preserve the UD-045 permission boundary")
    for wid, phrase in (
        ("008", "authorizes no execution"),
        ("009", "without authorizing an actor"),
        ("010", "no general role or office authority is executable"),
        ("010", "confers nothing"),
    ):
        if phrase not in blocks.get(wid, ""):
            out.append(f"ALW-{wid} is missing the boundary phrase {phrase!r}")
    alw011 = blocks.get("011", "")
    for phrase in ("Executable assignment/revocation is limited to the narrow tax-management set",
                   "every other capability assignment or revocation is blocked"):
        if phrase not in alw011:
            out.append(f"ALW-011 is missing {phrase!r}")

    # 9g. Downstream B-section ownership uses the official outline titles.
    s1512 = section(text, "### 15.12 ", "### 15.13 ")
    for title in (
        "B-03 — Accounts, nation creation and progression",
        "B-08 — Diplomacy",
        "B-09 — Alliances and alliance management",
        "B-10 — Warfare, campaigns and postwar settlements",
        "B-12 — Fair play, player protection, privacy and administration",
        "B-13 — Interface and player journeys",
        "B-14 — Formulas, numerical rules and balance",
        "B-15 — Cross-system interactions (Bible assembly",
    ):
        if title not in s1512:
            out.append(f"§15.12 is missing the official title {title!r}")
    if "Moderation is **not** a B-14 responsibility" not in s1512:
        out.append("§15.12 does not deny B-14 moderation ownership")
    rd06 = [ln for ln in section(text, "### 17.2 Alliance release dependencies", "### 17.3").splitlines()
            if ln.startswith("| `AL-RD-06`")]
    if not rd06 or "B-12 moderation separation" not in rd06[0] or "B-14 owns no moderation" not in rd06[0]:
        out.append("AL-RD-06 does not assign moderation to B-12 rather than B-14")

    # 9h. Position and constitution management stay descriptive-only and blocked.
    alw008 = blocks.get("008", "")
    alw009 = blocks.get("009", "")
    alw010 = blocks.get("010", "")
    for wid, phrase in (
        ("008", "structured publication is blocked"),
        ("008", "Do not publish, supersede or activate"),
        ("008", "no version, permission or office write"),
        ("009", "structured amendment is blocked"),
        ("009", "Do not amend, publish, supersede or activate"),
        ("009", "no version, approval, permission or office write"),
        ("010", "descriptive content only"),
        ("010", "do not execute `MANAGE_ROLES`"),
        ("010", "no position record and no proposed-or-active permission set exists"),
        ("011", "no structured position, role or permission state transition"),
    ):
        if phrase not in blocks.get(wid, ""):
            out.append(f"ALW-{wid} is missing the descriptive-only boundary {phrase!r}")
    for bad in (
        "Create, modify or delete a position record",
        "Create/modify/delete the position record",
        "Position record created / modified / deleted",
        "textual publication itself is the approved behaviour",
        "publish; mark prior version",
        "Draft, publish, hash, diff and T+1 behaviour are executed",
        "Amendment, supersession and non-retroactivity are executed",
        "Positions are configured; only the narrow tax-management capability set is executable",
        "Obtain lawful authority through the constitution",
        "the member sees the published constitution",
    ):
        if bad in text:
            out.append(f"document still implies an executable capability: {bad!r}")
    s32 = section(text, "### 3.2 ", "### 3.3 ")
    for phrase in (
        "**Candidate; descriptive authoring only**; structured drafting or version creation is not executable under `UD-045`",
        "**Candidate; structured publication is not executable under `UD-045`**",
        "**Candidate; descriptive authoring only**; structured position create/modify/delete/assign is not executable under `UD-045`",
    ):
        if phrase not in s32:
            out.append(f"§3.2 capability matrix lost the non-executable boundary {phrase!r}")
    s43 = section(text, "### 4.3 ", "### 4.4 ")
    for phrase in ("Authority status", "unreachable while `UD-045` is Open"):
        if phrase not in s43:
            out.append(f"§4.3 constitution states are not marked future conditional: {phrase!r}")
    trace_rows = [ln for ln in text.splitlines()
                  if re.match(r"^\| `ALL-0(?:3[1-9]|4[0-3])` \|", ln)]
    if len(trace_rows) != 13:
        out.append(f"constitution rule traceability rows are not 13 (count {len(trace_rows)})")
    for ln in trace_rows:
        if "future conditional and blocked under `UD-045`" not in ln:
            rid = re.search(r"ALL-\d{3}", ln).group(0)
            out.append(f"forward traceability for {rid} does not classify constitution behaviour as blocked")
    details = test_blocks(text)
    for n in range(21, 27):
        block = details.get(f"{n:03d}", "")
        for phrase in ("`ALF-08`", "`UD-045`"):
            if phrase not in block:
                out.append(f"AAT-{n:03d} does not assert the blocked constitution path ({phrase})")
        if "refus" not in block.lower():
            out.append(f"AAT-{n:03d} does not expect a refusal")
    for n, state_phrase in (
        (27, "No position record is created or modified"),
        (28, "No position record is deleted or modified"),
        (29, "No position or rank is created, promoted, demoted, modified or deleted"),
    ):
        block = details.get(f"{n:03d}", "")
        for phrase in ("`ALF-08`", "`UD-045`", "`AUD-AL-004` rejection", "state is unchanged", state_phrase):
            if phrase not in block:
                out.append(f"AAT-{n:03d} does not prove the blocked position path ({phrase})")
    for n, phrase in (
        (119, "no engine permission"),
        (120, "Title grants nothing"),
        (121, "blocked under `UD-045`"),
        (122, "refused"),
        (123, "`ALF-08`"),
        (124, "`ALF-08`"),
    ):
        if phrase not in details.get(f"{n:03d}", ""):
            out.append(f"AAT-{n:03d} lost the authority-boundary assertion {phrase!r}")

    # 10. Release gates: G-1..G-6 and AL-RD-01..12 all still NOT MET.
    gates = section(text, "### 17.1 Preserved Global Trade gates", "### 17.2")
    g_text = "`G-1`–`G-6`" in gates or all(f"`G-{n}`" in gates for n in range(1, 7))
    if not g_text:
        out.append("§17.1 does not preserve G-1..G-6")
    if "NOT MET" not in gates:
        out.append("§17.1 no longer records NOT MET gates")
    deps = section(text, "### 17.2 Alliance release dependencies", "### 17.3")
    rd_rows = [ln for ln in deps.splitlines() if re.match(r"^\| `AL-RD-\d{2}` \|", ln)]
    rd_ids = [re.search(r"AL-RD-(\d{2})", ln).group(1) for ln in rd_rows]
    if rd_ids != [f"{n:02d}" for n in range(1, 13)]:
        out.append(f"AL-RD rows are not 01..12 (count {len(rd_ids)})")
    for ln in rd_rows:
        if "NOT MET" not in ln:
            out.append("an AL-RD dependency is not marked NOT MET")

    # 11. Acceptance checklist: 30 criteria with honest statuses.
    accept = section(text, "## 19. Acceptance", "\x00") or text[text.find("## 19."):]
    ac_rows = [ln for ln in accept.splitlines() if re.match(r"^\| `09C-AC-\d{3}` \|", ln)]
    ac_ids = [re.search(r"09C-AC-(\d{3})", ln).group(1) for ln in ac_rows]
    if ac_ids != [f"{n:03d}" for n in range(1, 31)]:
        out.append(f"09C-AC IDs are not 001..030 (count {len(ac_ids)})")
    for ln in ac_rows:
        cid = re.search(r"09C-AC-(\d{3})", ln).group(1)
        if not re.search(r"\b(MET|PARTIAL|NOT MET|BLOCKED)\b", ln):
            out.append(f"09C-AC-{cid} has no explicit status")
        if re.search(r"\|\s*(?:MET|PARTIAL|NOT MET|BLOCKED)\s*\|", ln) is None and \
           not re.search(r"\*\*(MET|PARTIAL|NOT MET|BLOCKED)\*\*", ln):
            out.append(f"09C-AC-{cid} status column is ambiguous")

    # 12. The document keeps the specification/implementation boundary.
    if "not a functioning" not in text.lower() and "no runtime evidence" not in text.lower():
        out.append("document does not state the specification/implementation boundary")
    if "Prompt 10" not in section(text, "## 16. Cross-prompt", "## 17. Release-gate"):
        out.append("§16 does not hand off to Prompt 10")

    return out


def self_test() -> int:
    """Mutate the document in memory and prove the guards fire."""
    text = rd(WORK)
    cases = [
        ("missing §19", lambda t: t.replace("## 19. Acceptance", "## 19. Appendix")),
        ("sentinel", lambda t: t + "\n<!-- 09C-CONTINUE -->\n"),
        ("ALF-13 emission", lambda t: t.replace(
            "`ALF-01` name/tag collision", "`ALF-13` invented</br>`ALF-01` name/tag collision", 1)),
        ("silence consent", lambda t: t.replace(
            "Entity created exactly once", "silence is consent", 1)),
        ("bad test heading", lambda t: t.replace(
            "### 14.1 Founding, membership and lifecycle (`AAT-001`–`AAT-020`)",
            "### 14.1 Founding, membership and lifecycle (`AAT-001`–`AAT-019`)", 1)),
        ("claim becomes succession", lambda t: t.replace(
            "A recorded claim is **not** a decision.",
            "A recorded claim becomes the successor.", 1)),
        ("ALW-012 transfer procedure", lambda t: t.replace(
            "No transfer branch exists", "The contact pointer changes from A to B.", 1)),
        ("traceability class removed", lambda t: t.replace(
            "rule `ALL-051` | **DIRECT** | blocked |",
            "rule `ALL-051` | related | blocked |", 1)),
        ("detail field removed", lambda t: t.replace(
            "| **26. Evidence status** | IMPLEMENTATION-PENDING |\n", "", 1)),
        ("B-14 ownership wrong", lambda t: t.replace(
            "B-14 — Formulas, numerical rules and balance",
            "B-14 — Moderation and audit", 1)),
        ("permission boundary removed", lambda t: t.replace(
            "no general role or office authority is executable", "general role authority is executable", 1)),
        ("deferred owner removed", lambda t: t.replace(
            "`AX-06`, `AX-17`, `AX-28` | UD-046 |", "`AX-06`, `AX-17`, `AX-28` | — |", 1)),
        ("NOT APPLICABLE justification removed", lambda t: t.replace(
            "Withdrawn by `D-140`; retains continuity only and grants no right, protection or power.",
            "No further detail.", 1)),
        ("test reference removed", lambda t: t.replace(
            "| **20. ALL** | `ALL-011`–`ALL-017` |", "| **20. ALL** | N/A |", 1)),
        ("status overclaims completion", lambda t: t.replace(
            "| `C-09C-023` | Focused validators and seeded-defect tests pass | §19.3 commands 1–3 and 7; 24/24 seeded defects | PASS |",
            "| `C-09C-023` | Focused validators and seeded-defect tests pass | §19.3 commands 1–3 and 7; 24/24 seeded defects | FAIL |", 1)),
        ("invented test reference", lambda t: t.replace("`AAT-132`", "`AAT-133`", 1)),
        ("title accepted as permission", lambda t: t.replace(
            "a role title is never accepted as evidence of permission",
            "a role title is accepted as evidence of permission", 1)),
        ("ALW-010 executes MANAGE_ROLES", lambda t: t.replace(
            "do not execute `MANAGE_ROLES`", "execute `MANAGE_ROLES` to create the position", 1)),
        ("ALW-010 structured record exists", lambda t: t.replace(
            "no position record and no proposed-or-active permission set exists",
            "the position record and proposed permission set exist", 1)),
        ("ALW-008 publication restored", lambda t: t.replace(
            "Do not publish, supersede or activate any version",
            "Publish the version and mark the prior version superseded", 1)),
        ("AAT-027 state change", lambda t: t.replace(
            "No position record is created or modified;",
            "The position record is created and modified;", 1)),
        ("AAT-028 deletion succeeds", lambda t: t.replace(
            "No position record is deleted or modified;",
            "The position record is deleted and modified;", 1)),
        ("traceability execution restored", lambda t: t.replace(
            "future conditional and blocked under `UD-045`.",
            "executed by `ALW-008`.", 1)),
        ("permission matrix marked approved", lambda t: t.replace(
            "**Candidate; descriptive authoring only**; structured position create/modify/delete/assign is not executable under `UD-045`",
            "**Approved**; structured position create/modify/delete/assign is executable", 1)),
    ]
    failures = 0
    for label, mutate in cases:
        mutated = mutate(text)
        if mutated == text:
            print(f"SELF-TEST INVALID: mutation {label!r} changed nothing")
            failures += 1
            continue
        issues = problems(mutated, rd(UD))
        if not issues:
            print(f"SELF-TEST FAILED: {label!r} was not detected")
            failures += 1
        else:
            print(f"self-test ok: {label} -> {issues[0]}")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    text = rd(WORK)
    issues = problems(text, rd(UD))
    blocks = workflow_blocks(text)
    ale = set(re.findall(r"^\| `ALE-(\d{3})`", section(text, "## 9.", "## 10."), re.M))
    aat = set(re.findall(r"^\| `AAT-(\d{3})`", section(text, "## 14.", "## 15."), re.M))
    print(f"09C companion: {len(blocks)} workflows, {len(ale)} edge cases, {len(aat)} tests")
    if issues:
        print(f"FAIL — {len(issues)} problem(s):")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
