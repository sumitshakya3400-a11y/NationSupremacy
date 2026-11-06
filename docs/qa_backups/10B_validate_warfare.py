#!/usr/bin/env python3
"""Targeted documentation QA for the Prompt 10B warfare specification.

This validator exists because the general validators check presence and
continuity, not whether the B-10 rulebook is internally consistent. It checks:

  1. The 30 required H2 sections exist in order with the expected topic.
  2. WAR-001..WAR-188 are defined exactly once and all references resolve.
  3. B10-AD-01..B10-AD-25 and B10-C01..B10-C34 are registered once.
  4. Every 10A identifier family is dispositioned in its own §27 table with
     the exact row count and contiguous IDs.
  5. The §27.1 summary rows agree with the verdicts in §27.2-§27.9.
  6. The formula register has 39 formulas, each with all 20 mandatory fields,
     and the rulebook index agrees with it.
  7. REQ-654..REQ-703 and DD-166..DD-190 exist as Provisional rows; DD-185
     resolves UD-032; UD-032 is Resolved.
  8. The binding constraints survive: mapless, D-015, Alliance sovereignty,
     no facility/city damage, no nuclear, no espionage, conventional missiles.
  9. Prompt 10C was not pre-empted: no workflow companion exists and the
     handoff and completion statements keep 10C as the next task.
 10. Seventy-three mandatory negative fixtures, two clean fixtures and
     twenty structured semantic evidence records (thirteen area summaries
     plus seven full ten-field records for the Prompt 10B-C2 defects) cover
     the Food, infrastructure-damage, OP-lifecycle, validator, political-state,
     timing, housing and modifier corrections. CF-01 is hand arithmetic over
     F-WR-036/F-WR-037/F-WR-038/F-WR-039; CF-02 is hand arithmetic over the
     Prompt 10B-C3 OP regeneration, reservation, release, retry and cap
     sequence. Both are separately traced to the canonical sentence behind
     every required bullet; no runtime is executed.

Run:  python docs/qa_backups/10B_validate_warfare.py [docs-root]
Exit 0 = all checks pass. Exit 1 = at least one failure.

Documentation QA only; stdlib only; no network access.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# The status model is a sibling helper; importing it makes the 11C completion
# check a membership test instead of a substring search over its source text.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_rules import COMPLETED_SUBPROMPTS  # noqa: E402


def section(text: str, start: str, end: str | None) -> str:
    """Text between two markers, or to the end when no end marker is given."""
    i = text.index(start)
    if end is None:
        return text[i:]
    j = text.index(end, i + len(start))
    return text[i:j]


def cells(line: str) -> list[str]:
    """Cells of a Markdown table row, stripped."""
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_rows(block: str, prefix: str) -> list[list[str]]:
    """Table rows whose first cell starts with the prefix."""
    rows = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        row = cells(line)
        if row and row[0].strip("`").startswith(prefix):
            rows.append(row)
    return rows


def contiguous(prefix: str, count: int, width: int = 2) -> list[str]:
    """IDs of the form PREFIX-01..count, zero-padded."""
    return [f"{prefix}-{i:0{width}d}" for i in range(1, count + 1)]


def contiguous_flat(prefix: str, count: int, width: int = 2) -> list[str]:
    """IDs of the form PREFIX01..count, zero-padded."""
    return [f"{prefix}{i:0{width}d}" for i in range(1, count + 1)]


def handoff_ids() -> list[str]:
    """The 36 WFH handoff identifiers, A1..F6."""
    return [f"WFH-{letter}{n}" for letter in "ABCDEF" for n in range(1, 7)]


SECTIONS = [
    (1, "executive summary"),
    (2, "purpose, scope and non-goals"),
    (3, "authority and binding decisions"),
    (4, "warfare entities and terminology"),
    (5, "declaration and eligibility"),
    (6, "campaign architecture and state machine"),
    (7, "objectives and victory"),
    (8, "operations points"),
    (9, "military readiness"),
    (10, "military units, recruitment and development"),
    (11, "resources and upkeep"),
    (12, "supply and logistics"),
    (13, "complete operation catalogue"),
    (14, "battle-resolution model"),
    (15, "simultaneous combat and deterministic ordering"),
    (16, "losses and damage"),
    (17, "recovery and repair"),
    (18, "protection and counterplay"),
    (19, "ceasefires and peace"),
    (20, "surrender and negotiated settlement"),
    (21, "settlement enforcement and reparations"),
    (22, "postwar consequences"),
    (23, "visibility and permissions"),
    (24, "audit events and failure codes"),
    (25, "cross-system integration contracts"),
    (26, "decision and conflict-resolution register"),
    (27, "10a research disposition matrix"),
    (28, "formula register references"),
    (29, "prompt 10c handoff"),
    (30, "completion and limitation statement"),
]

FAMILIES = [
    ("WCR", "### 27.2", "### 27.3", contiguous("WCR", 44)),
    ("WQN", "### 27.3", "### 27.4", contiguous("WQN", 20)),
    ("WFQ", "### 27.4", "### 27.5", contiguous("WFQ", 22)),
    ("WRK", "### 27.5", "### 27.6", contiguous("WRK", 15)),
    ("WFX", "### 27.6", "### 27.7", contiguous("WFX", 12)),
    ("WFC", "### 27.7", "### 27.8", contiguous("WFC", 26)),
    ("GAP", "### 27.8", "### 27.9", contiguous("GAP", 16)),
    ("WFH", "### 27.9", "## 28.", handoff_ids()),
]

OPS = [
    "RAID",
    "ASSAULT",
    "AIR_STRIKE",
    "BLOCKADE",
    "MISSILE_STRIKE",
    "INTERCEPT",
    "FORTIFY",
    "BREAK_BLOCKADE",
    "RESUPPLY",
]

OBJECTIVES = [
    "OBJ-ATTRITION",
    "OBJ-INTERDICTION",
    "OBJ-BLOCKADE",
    "OBJ-AIR",
    "OBJ-DEFENCE",
    "OBJ-STRIKE",
]

OWNER_RESERVED = [f"UD-{n:03d}" for n in range(40, 50)]


def validate(docs: Path) -> tuple[list[str], int]:
    """Run the structural checks and return the problems and check count."""
    problems: list[str] = []
    checks = 0

    def check(ok: bool, category: str, message: str) -> None:
        """Record one check, appending the message when it fails."""
        nonlocal checks
        checks += 1
        if not ok:
            problems.append(f"[{category}] {message}")

    rulebook_path = docs / "stage-2" / "17_warfare_and_settlements.md"
    register_path = docs / "stage-2" / "17_warfare_formula_register.md"
    req_path = docs / "stage-2" / "03_requirements_traceability.md"
    dd_path = docs / "stage-2" / "04_approved_and_provisional_decisions.md"
    ud_path = docs / "stage-2" / "05_unresolved_design_decisions.md"
    log_path = docs / "stage-2" / "06_stage_2_progress_log.md"
    b04_path = docs / "stage-2" / "10_economy_resources_treasury_and_finances.md"
    b05_path = docs / "stage-2" / "11_cities_infrastructure_production_and_research.md"
    b06_path = docs / "stage-2" / "12_population_and_domestic_politics.md"
    handoff_path = docs / "stage-2" / "00_stage_2_handoff.md"

    for path in (rulebook_path, register_path, req_path, dd_path, ud_path, log_path,
                 b04_path, b05_path, b06_path, handoff_path):
        check(path.exists(), "0-files", f"missing required file: {path}")
    if problems:
        return problems, checks

    rulebook = rulebook_path.read_text(encoding="utf-8")
    register = register_path.read_text(encoding="utf-8")
    req = req_path.read_text(encoding="utf-8")
    dd = dd_path.read_text(encoding="utf-8")
    ud = ud_path.read_text(encoding="utf-8")
    log = log_path.read_text(encoding="utf-8")
    bodies = {
        "rulebook": rulebook,
        "register": register,
        "b04": b04_path.read_text(encoding="utf-8"),
        "b05": b05_path.read_text(encoding="utf-8"),
        "b06": b06_path.read_text(encoding="utf-8"),
        "handoff": handoff_path.read_text(encoding="utf-8"),
    }

    # --- 1. Section structure ----------------------------------------------
    headings = re.findall(r"(?m)^## (\d{1,2})\. (.+)$", rulebook)
    check(len(headings) == 30, "1-structure", f"rulebook has {len(headings)} numbered H2 sections, expected 30")
    check([int(n) for n, _ in headings] == list(range(1, 31)), "1-structure", "H2 section numbers are not 1..30 in order")
    for number, keyword in SECTIONS:
        match = next((title for n, title in headings if int(n) == number), "")
        check(keyword in match.lower(), "1-structure", f"section {number} title does not cover {keyword!r}: {match!r}")

    # --- 2. WAR identifiers -------------------------------------------------
    definitions = re.findall(r"(?m)^\*{0,2}`(WAR-\d{3})`", rulebook)
    check(len(definitions) == 188, "2-rules", f"rulebook defines {len(definitions)} WAR rules, expected 188")
    check(len(set(definitions)) == len(definitions), "2-rules", "a WAR rule is defined more than once")
    for number in range(1, 189):
        check(f"WAR-{number:03d}" in definitions, "2-rules", f"WAR-{number:03d} is not defined")
    referenced = set(re.findall(r"WAR-\d{3}", rulebook))
    check(referenced == set(definitions), "2-rules", f"unresolved WAR references: {sorted(referenced - set(definitions))}")
    check("WAR-168" in rulebook and "out of scope" in section(rulebook, "**`WAR-168`**", "\n").lower(), "2-rules", "WAR-168 mapless terminology contract is missing or not binding")

    # --- 3. Architecture decisions and conflicts ----------------------------
    ad_rows = table_rows(section(rulebook, "### 26.1", "### 26.2"), "B10-AD-")
    check(len(ad_rows) == 25, "3-registers", f"§26.1 has {len(ad_rows)} architecture-decision rows, expected 25")
    check([r[0].strip("`") for r in ad_rows] == contiguous_flat("B10-AD-", 25), "3-registers", "B10-AD IDs are not contiguous 01..25")
    conflict_rows = table_rows(section(rulebook, "### 26.2", "## 27."), "B10-C")
    check(len(conflict_rows) == 34, "3-registers", f"§26.2 has {len(conflict_rows)} conflict rows, expected 34")
    check([r[0].strip("`") for r in conflict_rows] == contiguous_flat("B10-C", 34), "3-registers", "B10-C IDs are not contiguous 01..34")

    # --- 4. 10A disposition families ---------------------------------------
    family_rows: dict[str, list[list[str]]] = {}
    for prefix, start, end, expected_ids in FAMILIES:
        rows = table_rows(section(rulebook, start, end), prefix + "-")
        family_rows[prefix] = rows
        ids = [r[0].strip("`") for r in rows]
        check(len(rows) == len(expected_ids), "4-dispositions", f"{prefix} table has {len(rows)} rows, expected {len(expected_ids)}")
        check(ids == expected_ids, "4-dispositions", f"{prefix} IDs are not the expected contiguous set")
    total_rows = sum(len(rows) for rows in family_rows.values())
    check(total_rows == 191, "4-dispositions", f"disposition tables contain {total_rows} rows, expected 191")

    # --- 5. §27.1 summary agreement ----------------------------------------
    summary = section(rulebook, "### 27.1", "### 27.2")

    def summary_row(family: str) -> str:
        """The summary-table row for a family's first member."""
        return next((l for l in summary.splitlines() if l.startswith(f"| `{family}-01`")), "")

    wcr = family_rows["WCR"]
    wcr_adopt = sum(1 for r in wcr if r[2].startswith("**Adopt**"))
    wcr_amend = sum(1 for r in wcr if r[2].startswith("**Amend**"))
    wcr_transfer = sum(1 for r in wcr if r[2].startswith("**Transfer"))
    check((wcr_adopt, wcr_amend, wcr_transfer) == (33, 10, 1), "5-summary", f"WCR verdicts are {wcr_adopt}/{wcr_amend}/{wcr_transfer}, expected 33/10/1")
    check("33 adopted, 10 amended, 1 transferred" in summary_row("WCR"), "5-summary", "§27.1 WCR summary disagrees with §27.2 verdicts")

    wqn = family_rows["WQN"]
    wqn_provisional = sum(1 for r in wqn if "Provisional" in r[4])
    wqn_structural = sum(1 for r in wqn if "Structural" in r[4])
    wqn_rejected = sum(1 for r in wqn if "Rejected" in r[4])
    wqn_other = sum(1 for r in wqn if "Resolved by alignment" in r[4] or "Closed by exclusion" in r[4])
    check((wqn_provisional + wqn_structural, wqn_rejected, wqn_other) == (17, 1, 2), "5-summary", f"WQN verdicts are {wqn_provisional + wqn_structural}/{wqn_rejected}/{wqn_other}, expected 17/1/2")
    check("17 architecture decisions" in summary_row("WQN") and "1 rejected" in summary_row("WQN") and "2 closed by exclusion or B-03 alignment" in summary_row("WQN"), "5-summary", "§27.1 WQN summary disagrees with §27.3 statuses")

    wfq = family_rows["WFQ"]
    wfq_resolved = sum(1 for r in wfq if r[2].startswith("**Resolved**"))
    wfq_design = sum(1 for r in wfq if r[2].startswith("**Resolved by design**"))
    wfq_na = sum(1 for r in wfq if r[2].startswith("**Not applicable**"))
    check((wfq_resolved, wfq_design, wfq_na) == (14, 1, 7), "5-summary", f"WFQ verdicts are {wfq_resolved}/{wfq_design}/{wfq_na}, expected 14/1/7")
    check("15 resolved by a B-10 rule (14 resolved, 1 resolved by design); 7 not applicable" in summary_row("WFQ"), "5-summary", "§27.1 WFQ summary disagrees with §27.4 verdicts")
    check("Seven questions are marked **not applicable**" in rulebook, "5-summary", "WAR-170 does not state the correct not-applicable count")

    wfx = family_rows["WFX"]
    wfx_counts = {
        "carried": sum(1 for r in wfx if r[3].startswith("**Carried**")),
        "context": sum(1 for r in wfx if r[3].startswith("**Adopted as context**")),
        "irrelevant": sum(1 for r in wfx if r[3].startswith("**Closed as irrelevant**")),
        "design": sum(1 for r in wfx if r[3].startswith("**Closed by design**")),
        "applied": sum(1 for r in wfx if r[3].startswith("**Applied**")),
        "open": sum(1 for r in wfx if r[3].startswith("**Open")),
    }
    check(wfx_counts == {"carried": 4, "context": 1, "irrelevant": 2, "design": 3, "applied": 1, "open": 1}, "5-summary", f"WFX verdicts differ from the expected set: {wfx_counts}")
    for phrase in ("4 carried as P&W evidence status", "1 adopted as context", "2 closed as irrelevant", "3 closed by design", "1 evidence-method conflict applied", "1 open external evidence gap"):
        check(phrase in summary_row("WFX"), "5-summary", f"§27.1 WFX summary lacks {phrase!r}")

    wfc = family_rows["WFC"]
    wfc_counts = (
        sum(1 for r in wfc if r[2].startswith("**Adopted")),
        sum(1 for r in wfc if r[2].startswith("**Adapted")),
        sum(1 for r in wfc if r[2].startswith("**Rejected")),
        sum(1 for r in wfc if r[2].startswith("**Not applicable")),
        sum(1 for r in wfc if r[2].startswith("**Replaced")),
        sum(1 for r in wfc if r[2].startswith("**Transferred")),
    )
    check(wfc_counts == (3, 14, 5, 2, 1, 1), "5-summary", f"WFC verdicts are {wfc_counts}, expected 3/14/5/2/1/1")
    check("3 adopted in substance, 14 adapted, 5 rejected, 2 not applicable, 1 replaced by a first-principles design, 1 transferred to Prompt 12" in summary_row("WFC"), "5-summary", "§27.1 WFC summary disagrees with §27.7 verdicts")
    check("**3 adopted in substance**" in section(rulebook, "`WAR-173`", "\n"), "5-summary", "WAR-173 classification counts are missing")

    gap = family_rows["GAP"]
    gap_counts = (
        sum(1 for r in gap if r[2].startswith("**Closed by design**")),
        sum(1 for r in gap if r[2].startswith("**Closed as irrelevant**")),
        sum(1 for r in gap if r[2].startswith("**Transferred")),
        sum(1 for r in gap if r[2].startswith("**Open")),
    )
    check(gap_counts == (8, 3, 1, 4), "5-summary", f"GAP verdicts are {gap_counts}, expected 8/3/1/4")
    check("8 closed by design decision, 3 closed as irrelevant, 1 transferred to a named owner, 4 remain open evidence gaps" in summary_row("GAP"), "5-summary", "§27.1 GAP summary disagrees with §27.8 verdicts")

    wrk_open = [r[0].strip("`") for r in family_rows["WRK"] if "Prompt 10B" in r[6]]
    check(not wrk_open, "5-summary", f"risks left with Prompt 10B as owner: {wrk_open}")

    # --- 6. Formula register -----------------------------------------------
    formula_sections = re.findall(r"(?m)^### (F-WR-\d{3}) \u2014 (.+)$", register)
    check(len(formula_sections) == 39, "6-formulas", f"register has {len(formula_sections)} formula sections, expected 39")
    check([fid for fid, _ in formula_sections] == contiguous("F-WR", 39, 3), "6-formulas", "formula IDs are not contiguous F-WR-001..F-WR-039")

    for index, (fid, name) in enumerate(formula_sections):
        start_marker = f"### {fid} \u2014 {name}"
        start = register.index(start_marker)
        next_heading = register.find("\n### ", start + len(start_marker))
        next_h2 = register.find("\n## ", start + len(start_marker))
        ends = [pos for pos in (next_heading, next_h2) if pos != -1]
        body = register[start:min(ends)] if ends else register[start:]
        numbers = [int(n) for n in re.findall(r"(?m)^\| (\d{1,2}) \| ", body)]
        check(numbers == list(range(1, 21)), "6-formulas", f"{fid} has fields {numbers}, expected 1..20")
        check(re.search(r"^\| 1 \| Identifier \| `" + re.escape(fid) + r"` \|", body, re.M) is not None, "6-formulas", f"{fid} field 1 does not name the formula")
        field17 = re.search(r"(?m)^\| 17 \| ([^|]+) \| ([^|]+) \|$", body)
        check(field17 is not None and len(field17.group(2).strip()) >= 6 and ("Structural" in field17.group(2) or "PROVISIONAL" in field17.group(2)), "6-formulas", f"{fid} has no substantive provisional-status field")
        source = re.search(r"(?m)^\| 19 \| ([^|]+) \| ([^|]+) \|$", body)
        check(source is not None and len(source.group(2).strip()) >= 5, "6-formulas", f"{fid} has no source rule")

    index_ids = re.findall(r"(?m)^\| `(F-WR-\d{3})` \|", section(register, "## 4.", "## 5."))
    check(index_ids == contiguous("F-WR", 39, 3), "6-formulas", "register index does not list F-WR-001..F-WR-039 in order")
    rulebook_ids = re.findall(r"(?m)^\| `(F-WR-\d{3})` \|", section(rulebook, "## 28.", "## 29."))
    check(rulebook_ids == contiguous("F-WR", 39, 3), "6-formulas", "rulebook §28 index does not list F-WR-001..F-WR-039 in order")
    check(set(re.findall(r"F-WR-\d{3}", rulebook)) == set(index_ids), "6-formulas", "a formula referenced in the rulebook is missing from the register")
    check("20 mandatory fields" in rulebook and "20 mandatory fields" in register, "6-formulas", "the 20-field contract is not stated in both documents")
    check("F-WR-035" in section(rulebook, "## 28.", "## 29.") and "contains every provisional value" in section(rulebook, "## 28.", "## 29."), "6-formulas", "the calibration envelope is not identified as the owner of every provisional value")

    # --- 7. Requirements, decisions and UD-032 -----------------------------
    req_rows = {}
    for line in req.splitlines():
        match = re.match(r"^\| REQ-(\d{3}) \|", line)
        if match:
            req_rows[int(match.group(1))] = line
    for number in range(654, 704):
        check(number in req_rows, "7-registers", f"REQ-{number:03d} is missing")
        check("| Provisional |" in req_rows.get(number, ""), "7-registers", f"REQ-{number:03d} is not Provisional")
    check("| Provisional |" in req_rows.get(14, ""), "7-registers", "REQ-014 was not reclassified from Deferred to Provisional")
    check("| Provisional |" in req_rows.get(591, ""), "7-registers", "REQ-591 was not reclassified from Deferred to Provisional")
    check(req.count("**55 Approved / 688 Provisional / 19 Open / 1 Deferred / 0 Proposed = 763 total**") >= 1, "7-registers", "requirements counts are not stated as 55/688/19/1/763")
    check("| Requirements tracked | **763** |" in req, "7-registers", "the requirements tally does not record 763 rows")

    dd_rows = {}
    for line in dd.splitlines():
        match = re.match(r"^\| DD-(\d{3}) \|", line)
        if match:
            dd_rows[int(match.group(1))] = line
    for number in range(166, 191):
        check(number in dd_rows, "7-registers", f"DD-{number:03d} is missing")
        check("Provisional" in dd_rows.get(number, ""), "7-registers", f"DD-{number:03d} is not Provisional")
    check("UD-032" in dd_rows.get(185, "") and "Option A" in dd_rows.get(185, ""), "7-registers", "DD-185 does not resolve UD-032 as Option A")
    check("130 Approved / 51 Provisional / 22 Confirmed / 2 Binding inherited / 2 Candidate-Open / 1 Superseded / 1 Deferred" in dd, "7-registers", "decision-log counts are not the expected 130/51/22/2/2/1/1")

    ud_row = next((line for line in ud.splitlines() if line.startswith("| UD-032 |")), "")
    check("**Resolved**" in ud_row and "Option (a)" in ud_row, "7-registers", "UD-032 is not recorded as Resolved Option A")
    check("**28 Resolved**, **3 Deferred to a future prompt**, **20 Open**" in ud, "7-registers", "unresolved-decision counts are not 28/3/20")
    for number in range(40, 50):
        row = next((line for line in ud.splitlines() if line.startswith(f"| UD-{number:03d} |")), "")
        check("| Open |" in row or "Open" in row, "7-registers", f"UD-{number:03d} is no longer Open")

    # --- 8. Binding constraints --------------------------------------------
    non_goals = section(rulebook, "### 2.3", "## 3.")
    check("- No geography of any kind." in non_goals, "8-constraints", "the mapless non-goal is missing")
    check("No city capture, city deletion or city ownership transfer; no facility damage or facility destruction." in non_goals, "8-constraints", "the no-city/facility-damage non-goal is missing")
    check("No nuclear weapons, no radiation mechanic, no uranium consumption." in non_goals, "8-constraints", "the no-nuclear non-goal is missing")
    check("No espionage or covert-operation system." in non_goals, "8-constraints", "the no-espionage non-goal is missing")
    check("No Alliance military coordination, command, delegation, shared OP or military treasury." in non_goals, "8-constraints", "the Alliance military non-goal is missing")
    check("No loot, no forced wealth seizure, no debt, no negative balance, no future-income garnishment." in non_goals, "8-constraints", "the no-loot/no-debt non-goal is missing")
    check("No calibrated numeric balance; Prompt 14 owns every calibration." in non_goals, "8-constraints", "the calibration boundary is missing")

    op_table = section(rulebook, "### 13.1", "### 13.2")
    for number, name in enumerate(OPS, 1):
        check(f"| `OP-{number:02d}` | `{name}` |" in op_table, "8-constraints", f"operation OP-{number:02d} {name} is missing from the closed catalogue")
    check(op_table.count("| `OP-") == 9, "8-constraints", "the operation catalogue is not closed at nine operations")
    check("no nuclear variant" in section(rulebook, "#### `OP-05 MISSILE_STRIKE`", "#### `OP-06"), "8-constraints", "OP-05 does not exclude a nuclear variant")
    check("Conventional missile strike only; no nuclear, no radiation, no uranium" in rulebook, "8-constraints", "B10-AD-23 does not limit missiles to conventional warheads")
    check("| Nuclear weapons | **Rejected** |" in rulebook, "8-constraints", "nuclear weapons are not explicitly rejected")

    objective_table = section(rulebook, "### 7.1", "### 7.2")
    for objective in OBJECTIVES:
        check(f"`{objective}`" in objective_table, "8-constraints", f"objective {objective} is missing")
    check(objective_table.count("| `OBJ-") == 6, "8-constraints", "the objective catalogue is not closed at six objectives")

    op_pool = section(rulebook, "### 8.1", "### 8.2")
    check("exactly one Operations Points pool" in op_pool, "8-constraints", "§8.1 does not state the single national OP pool")
    check("military-only, non-transferable, non-purchasable and never shared" in op_pool, "8-constraints", "§8.1 does not state the D-015 pool properties")
    check("There is no per-war pool, no per-campaign pool and no Alliance pool" in op_pool, "8-constraints", "§8.1 does not prohibit per-war, per-campaign and shared pools")
    check("This is D-015 as amended on 2026-11-04" in op_pool, "8-constraints", "§8.1 does not record the D-015 amendment")
    check("the amendment changes only the regeneration rate and the carry below the cap; every other property is unchanged" in op_pool, "8-constraints", "§8.1 does not delimit the D-015 amendment")
    check("| **D-015** | One national OP pool, military-only, non-transferable, reserved at acceptance, consumed at resolution; no per-war/campaign/shared pool; no MAP import. **Amended 2026-11-04 (Prompt 10B-C3):** one OP regenerated at each boundary, cap-enforced, with carry below the cap" in rulebook, "8-constraints", "the D-015 authority row is not preserved with its amendment")
    check("`op_balance = min(op_cap, op_balance + 1)`" in op_pool, "8-constraints", "§8.1 does not state the regeneration formula")
    check("`available = max(0, op_balance − reserved)`" in op_pool, "8-constraints", "§8.1 does not state the availability formula")
    check("P7 performs **no** regeneration" in op_pool and "P7 writes no `REGENERATED` item" in op_pool, "8-constraints", "§8.1 does not forbid regeneration at P7")
    check("one `REGENERATED` item per nation per turn, including a recorded `0` at the cap" in op_pool, "8-constraints", "§8.1 does not require the idempotent zero item at the cap")
    check("no reservation or point can be transferred to another nation, campaign, Alliance or action" in op_pool, "8-constraints", "WAR-043b does not forbid OP transfer")
    check("No global currency" not in rulebook, "8-constraints", "unexpected global-currency wording")

    check("No Alliance role can read a member's private military state, spend a member's OP or resources, submit a member's operation or declare for a member." in rulebook, "8-constraints", "WAR-161 Alliance authority invariant is missing")
    check("The Alliance Receiving Ledger remains a credit-only receipt boundary. It is not a military treasury" in rulebook, "8-constraints", "WAR-186 does not exclude the ARL as a military treasury")
    check("City infrastructure is the **only** B-05 attribute a strike may reduce" in rulebook, "8-constraints", "WAR-102 damage boundary is missing")
    check("`URB-157` is amended for infrastructure damage only; every other protection in it is preserved." in rulebook, "8-constraints", "URB-157 is not preserved explicitly")
    for ud_id in OWNER_RESERVED:
        check(ud_id in section(rulebook, "`WAR-185`", "\n"), "8-constraints", f"{ud_id} is not listed in the owner-reserved boundary")

    # --- 8b. Mandatory negative fixtures -----------------------------------
    # Each fixture is a documentation-level rejection case: an invalid input
    # that the rulebook must explicitly reject. The probe is the exact rule
    # text that supplies the rejection; the fixture fails if that text is
    # missing or weakened.
    fixtures = [
        ("NF-01", "Food", "strength point treated as one soldier", "rulebook", "Strength points are **abstract combat weight**, not soldiers"),
        ("NF-02", "Food", "military demand added to civilian food_demand", "rulebook", "are computed before and without the military ration"),
        ("NF-03", "Food", "civilian Food diverted to feed the garrison", "rulebook", "P3.6 civilian Food resolves first and is never reduced to feed the military"),
        ("NF-04", "Food", "ration paid partially", "rulebook", "the whole obligation is **cancelled**"),
        ("NF-05", "Food", "short ration with no readiness or flag consequence", "rulebook", "applies `readiness = max(0, readiness − 100)`, and sets `RATION_SHORT`"),
        ("NF-06", "Food", "OP-09 field ration counted as garrison ration", "rulebook", "It is an operational ration, not the garrison ration"),
        ("NF-07", "City", "non-OP-05 operation carries a city target", "rulebook", "Only `OP-05 MISSILE_STRIKE` may carry a city target."),
        ("NF-08", "City", "city target skips the national validator", "rulebook", "A city target is not a shortcut."),
        ("NF-09", "City", "damage pushes infrastructure below 10", "rulebook", "Infrastructure cannot fall below 10."),
        ("NF-10", "City", "damage exceeds the per-city campaign cap", "rulebook", "cumulative infrastructure damage cannot exceed"),
        ("NF-11", "City", "facility deleted by infrastructure damage", "rulebook", "No facility is deleted, moved, disabled or transferred."),
        ("NF-12", "City", "damage creates a population casualty", "rulebook", "No strike kills, moves or evicts people"),
        ("NF-13", "City", "repair retroactively heals a past strike", "rulebook", "P5 damage never retroactively undoes a P4.1 completion"),
        ("NF-14", "OP", "OP mutated at P0", "rulebook", "P0 only confirms the turn identity and writes the run record; it performs **no** OP mutation"),
        ("NF-15", "OP", "OP regenerated at P3 outside the P3.7 opening", "rulebook", "P3 performs **no** OP mutation except the single regeneration at the opening of P3.7"),
        ("NF-16", "OP", "reservation taken at P5 instead of acceptance", "rulebook", "Reservation | At acceptance, while the turn is OPEN, before P1 freeze"),
        ("NF-17", "OP", "failed P2 action keeps its reservation", "rulebook", "The reservation is released exactly once under `WAR-002`"),
        ("NF-18", "OP", "two terminal ledger items for one action", "register", "No state permits two terminal items for one `action_id`"),
        ("NF-19", "Validator", "DP-T01 blocks an operation inside an active war", "rulebook", "`DP-T01` is **absent from checks 6–12**"),
        ("NF-20", "Validator", "same-Alliance check satisfied by an Alliance NAP pass", "rulebook", "Checks 5, 6 and 7 are **separate and cumulative**"),
        ("NF-21", "Validator", "client-side hiding treated as enforcement", "rulebook", "Hiding an attack button, filtering a list or checking on the client is **not** enforcement."),
        ("NF-22", "Validator", "blocked action consumes OP or applies damage", "rulebook", "A blocked action is **not executed at all**"),
        ("NF-23", "Validator", "AUD-AL-017 written for a non-B-09 block", "rulebook", "`AUD-AL-017` is written **only** when checks 6 or 7 fail"),
        ("NF-24", "Validator", "P2 protection snapshot reused at P5", "rulebook", "The **execution-time state governs**"),
        ("NF-25", "Political", "war pauses during TRANSITION or CRISIS", "rulebook", "There is no `PAUSED` state."),
        ("NF-26", "Political", "accepted offensive operation resolves under TRANSITION", "rulebook", "Fails at the first validation run after the state begins"),
        ("NF-27", "Political", "accepted defensive operation blocked by TRANSITION", "rulebook", "An operation accepted while the political state was normal resolves at P5"),
        ("NF-28", "Modifier", "denial and blockade multiplied to +56.25%", "rulebook", "When both are active the surcharge is **+50%**, not +56.25%."),
        ("NF-29", "Modifier", "supply denial stacks with itself", "rulebook", "Denial lasts one turn, does not stack with itself"),
        ("NF-30", "Scope", "espionage assigned to Prompt 12 or 10C", "rulebook", "**No owner is identified and nothing is transferred**"),
        ("NF-31", "Scope", "city ownership transfers on victory", "rulebook", "City destruction, deletion, capture, transfer"),
        ("NF-32", "Scope", "facility destruction auto-adopted", "rulebook", "Facility destruction, deletion, disablement or transfer is prohibited"),
        ("NF-33", "Scope", "city targeted outside an active campaign", "rulebook", "A city cannot be targeted outside an active campaign."),
        ("NF-34", "Scope", "repair raises infrastructure above 500", "rulebook", "add infrastructure above 500"),
        # --- Prompt 10B-C2: 24 mandatory semantic-closure fixtures -------------
        ("NF-35", "Food", "OP-09 reserves Food needed by protected civilians", "rulebook",
         "It is never partially funded and never takes Food that the protected civilian requirement needs."),
        ("NF-36", "Food", "availability deducts OP-09 before the protected requirement", "rulebook",
         "available_if_held  = food_after_other − op09_held_total"),
        ("NF-37", "Food", "military ration charged before civilian demand", "rulebook",
         "P3.7 may consume only Food that remains unreserved after P3.6"),
        ("NF-38", "Food", "recurring and operational rations double-counted", "rulebook",
         "no path derives one from the other or charges the same Food twice"),
        ("NF-39", "Timing", "nonexistent P3.0 used as an authority", "rulebook",
         "There is no P3.0 and no second force baseline."),
        ("NF-40", "Timing", "Food and readiness use different force snapshots", "rulebook",
         "neither may recompute a different force"),
        ("NF-41", "Political", "valid accepted defensive commitment rejected by the political state", "rulebook",
         "`WAR-009g` supplies the narrow row-8 exemption and lists the seven conditions"),
        ("NF-42", "Political", "new offensive bypasses the political-state restriction", "rulebook",
         "Submission has no exception."),
        ("NF-43", "Political", "defensive exemption bypasses B-03/B-09", "rulebook",
         "The exemption changes **only** row 8."),
        ("NF-44", "Asset", "impairment uses total city book value", "b05",
         "Facility book value is **excluded** from infrastructure impairment"),
        ("NF-45", "Asset", "facility value impaired without authorization", "b05",
         "never touched by infrastructure impairment"),
        ("NF-46", "Asset", "initial infrastructure asset basis undefined", "b05",
         "are an opening lot with **zero capitalised cost**"),
        ("NF-47", "Repair", "repair cost contradicts B-05", "rulebook",
         "no material charge and no second discount"),
        ("NF-48", "Repair", "repair capitalization duplicated", "b05",
         "keyed on the repair `order_id`; replaying it applies nothing"),
        ("NF-49", "Timing", "damage measured against a stale opening snapshot", "rulebook",
         "`I_before` is `I_combat` from `WAR-109m`"),
        ("NF-50", "Timing", "capacity and housing use inconsistent boundaries", "rulebook",
         "= 10 + floor(I_post_P5(T) / 10)"),
        ("NF-51", "Housing", "housing shortfall bypasses B-06 crowding", "b06",
         "`DMP-031` applies the ordinary crowding decline"),
        ("NF-52", "Housing", "population directly deleted by infrastructure damage", "rulebook",
         "No strike kills, moves or evicts people"),
        ("NF-53", "Housing", "crowding described only as paused growth", "rulebook",
         "never through a warfare casualty rule"),
        ("NF-54", "Register", "B10-C17 keeps a stale priority", "rulebook",
         "sub-order **(a) military Food**, (b) readiness, (c) settlement, (d) other military obligation"),
        ("NF-55", "Register", "B10-C21 conflates military recovery with infrastructure repair", "rulebook",
         "**Two distinct paths, never one pool.**"),
        ("NF-56", "Scope", "B10-C30 claims espionage transferred without an owner", "rulebook",
         "**EXCLUDED FROM CURRENT B-10 SCOPE — UNASSIGNED FUTURE-SCOPE CANDIDATE**"),
        ("NF-57", "Scope", "WAR-166 repeats the stale espionage classification", "rulebook",
         "excluded from the current B-10 scope by decision"),
        ("NF-58", "Handoff", "project handoff says no city or infrastructure damage exists", "handoff",
         "**city targeting with bounded, recoverable infrastructure damage**"),
        # --- Prompt 10B-C3: 15 mandatory OP-lifecycle fixtures ------------------
        ("NF-59", "OP", "double regeneration at one boundary", "rulebook",
         "a second attempt for the same boundary returns the original receipt and writes nothing"),
        ("NF-60", "OP", "balance stored above the national cap", "rulebook",
         "A stored balance above `op_cap`, a negative balance, a reservation above the balance, or a second regeneration for one turn is an integrity failure (`WRF-34`), not a rule"),
        ("NF-61", "OP", "full refill to cap instead of an incremental rate", "rulebook",
         'the original "refill to cap / unused points do not bank" rate is superseded'),
        ("NF-62", "OP", "reserved OP spent as if available", "rulebook",
         "A player who wants the full pool reads `available + reserved`; a player who wants spendable OP reads `available` without subtracting anything mentally"),
        ("NF-63", "OP", "reservation dropped at the P3.7 boundary", "rulebook",
         "The reservation survives the regeneration and is neither refunded nor double-counted"),
        ("NF-64", "OP", "one action consumed twice", "rulebook",
         "A second `CONSUMED` for A is `WRF-34` and debits nothing"),
        ("NF-65", "OP", "one reservation released twice", "rulebook",
         "An action writes exactly one `HELD` and at most one terminal item (`CONSUMED` or `RELEASED`), all keyed by `action_id`"),
        ("NF-66", "OP", "P3.7 and the P7 close both regenerate", "rulebook",
         "P7 writes no `REGENERATED` item"),
        ("NF-67", "OP", "B-02 and B-10 define different regeneration boundaries", "rulebook",
         "P3.7 single `REGENERATED` (+1, capped)"),
        ("NF-68", "OP", "failed transaction silently loses OP without a ledger item", "rulebook",
         "The retry reads the terminal `CONSUMED` item, writes nothing and leaves balance 4"),
        ("NF-69", "OP", "retry regenerates a second time", "rulebook",
         "No second regeneration occurs because `R(T)` already exists"),
        ("NF-70", "OP", "OP transferred to another nation", "rulebook",
         "no reservation or point can be transferred to another nation, campaign, Alliance or action"),
        ("NF-71", "OP", "Alliance reads or spends a member's OP", "rulebook",
         "No Alliance role can read a member's private military state, spend a member's OP or resources, submit a member's operation or declare for a member"),
        ("NF-72", "OP", "per-war or per-campaign OP pool", "rulebook",
         "There is no per-war pool, no per-campaign pool and no Alliance pool"),
        ("NF-73", "OP", "regeneration bypasses dormancy or protection", "rulebook",
         "Dormancy blocks the submissions it already blocks; the increased balance grants no action and bypasses no protection"),
    ]
    fixture_ids = [f[0] for f in fixtures]
    check(len(fixtures) == 73, "8b-fixtures", f"fixture count is {len(fixtures)}, expected 73")
    check(len(set(fixture_ids)) == 73, "8b-fixtures", "fixture IDs are not unique")
    check(fixture_ids == [f"NF-{i:02d}" for i in range(1, 74)], "8b-fixtures", "fixture IDs are not contiguous NF-01..NF-73")
    rejected = 0
    for fid, area, invalid, doc, probe in fixtures:
        body = bodies.get(doc, "")
        ok = probe in body
        if ok:
            rejected += 1
        check(ok, "8b-fixtures", f"{fid} ({area}) does not reject: {invalid!r} (missing probe {probe!r} in {doc})")
    check(rejected == 73, "8b-fixtures", f"{rejected}/73 negative fixtures rejected")

    # --- 8c. Clean fixture --------------------------------------------------
    # CF-01 is one fully valid turn, checked by hand against F-WR-036,
    # F-WR-037, F-WR-038 and F-WR-039. All values are integers and no
    # runtime is executed. The city has purchased infrastructure (gross
    # 10,000) and one facility (5,000); the nation is fed, the garrison is
    # paid and one OP-09 field ration is reserved from eligible surplus.
    base_bundle = 5
    civic = 1
    facility_value = 5_000
    gross = 10_000
    accumulated = 0

    # Civilian Food and the conditional OP-09 reservation (WAR-053l).
    opening_food = 70
    food_produced = 0
    other_food_reservations = 0
    food_demand = 50
    protected_civilian_food = food_demand
    eligible_op09_surplus = opening_food + food_produced - other_food_reservations - protected_civilian_food
    op09_request = 4
    op09_held = op09_request if eligible_op09_surplus >= op09_request else 0
    food_after_other = opening_food + food_produced - other_food_reservations
    available_if_held = food_after_other - op09_held
    op09_released = 0 if available_if_held >= protected_civilian_food else op09_held
    civilians_fed = min(food_after_other - (op09_held - op09_released), food_demand)
    # One canonical P3.7 force snapshot feeds both Food and readiness (WAR-053m).
    ration_equivalents = 10 * 1_000 + 4 * 500  # 1,000 INF + 500 ARM
    military_food_demand = -(-ration_equivalents // 1_000)
    unreserved_for_garrison = food_after_other - civilians_fed - (op09_held - op09_released)
    garrison_paid = military_food_demand if unreserved_for_garrison >= military_food_demand else 0

    # City strike, impairment and repair (WAR-109a..WAR-109m).
    city_i = 120
    campaign_headroom = (city_i * 3_000) // 10_000
    removed = min(-(-(city_i * 500) // 10_000), 20, campaign_headroom, city_i - 10)
    i_after = city_i - removed
    capacity_construction = 10 + city_i // 10          # I_open(T)
    capacity_effective = 10 + i_after // 10            # I_post_P5(T)
    housing_population = 45_000 + 100 * city_i + 25_000 * civic
    housing_effective = 45_000 + 100 * i_after + 25_000 * civic
    carrying_before = gross - accumulated
    impaired = min(carrying_before, (carrying_before * removed) // city_i)
    carrying_after = carrying_before - impaired
    fixed_assets_after = carrying_after + facility_value
    repair_levels = removed
    base_repair_cost = sum(8 + j // 10 for j in range(i_after, i_after + repair_levels))
    repair_cost = base_repair_cost
    civil_survey_cost = -(-(base_repair_cost * 9_000) // 10_000)
    gross_repaired = gross + repair_cost
    carrying_repaired = gross_repaired - (accumulated + impaired)
    fixed_assets_repaired = carrying_repaired + facility_value
    # B-06 crowding at the next P3.8, with the ordinary growth comparison.
    population = 82_000
    growth_bp = 50
    natural = population + (population * growth_bp) // 10_000
    excess = max(0, population - housing_effective)
    decline = max(-(-excess // 10), max(0, population - natural))
    population_next = max(1_000, population - decline)
    bundle_after = -(-(base_bundle * 12_500) // 10_000)

    clean = (
        op09_held, civilians_fed, garrison_paid, military_food_demand,
        removed, i_after, capacity_construction, capacity_effective,
        housing_population, housing_effective, impaired, carrying_after,
        fixed_assets_after, repair_cost, civil_survey_cost, carrying_repaired,
        fixed_assets_repaired, decline, population_next, bundle_after,
    )
    expected_clean = (
        4, 50, 12, 12,
        6, 114, 22, 21,
        82_000, 81_400, 500, 9_500,
        14_500, 114, 103, 9_614,
        14_614, 60, 81_940, 7,
    )
    check(clean == expected_clean, "8c-clean", f"clean fixture arithmetic is {clean}, expected {expected_clean}")
    check(
        "infrastructure_carrying_value(city) = gross − accumulated" in register
        and "impaired = min(carrying_before, floor(carrying_before × removed / I_combat))" in register
        and "base_repair_cost = Σ_{j=I}^{I+n−1} (8 + floor(j / 10))" in register
        and "bundle'_r = ceil(bundle_r × (10,000 + surcharge_bp) / 10,000)" in register,
        "8c-clean",
        "clean fixture cannot be traced to the register expressions",
    )
    check(
        "`= 10 + floor(I_open(T) / 10)`" in rulebook
        and "`= 10 + floor(I_post_P5(T) / 10)`" in rulebook
        and "`= 45,000 + 100 × I_post_P5(T) + 25,000 × civic_centres`" in rulebook,
        "8c-clean",
        "clean fixture cannot be traced to the WAR-109m snapshot boundaries",
    )
    check(facility_value == 5_000 and fixed_assets_after - carrying_after == facility_value and fixed_assets_repaired - carrying_repaired == facility_value, "8c-clean", "clean fixture changes the facility value")
    check(population_next == 81_940 and 0 < decline < population - 1_000, "8c-clean", "clean fixture does not demonstrate a crowding decline above the floor")
    check(45_000 + 100 * city_i + 25_000 * civic == 82_000 and 81_940 < 82_000, "8c-clean", "clean fixture does not demonstrate recovery once repair restores housing")

    # Every §13.2 bullet is also traced to the canonical sentence that carries
    # it, so the clean case is documentation evidence and not only arithmetic.
    clean_claims = [
        ("civilian Food priority", "rulebook", "P3.6 civilian Food resolves first and is never reduced to feed the military"),
        ("valid OP-09 reservation from eligible surplus", "b04", "eligible_op09_surplus = opening_food + projected_food_production"),
        ("insufficient surplus prevents an unsafe reservation", "b04", "otherwise the whole action fails `WRF-25`"),
        ("regular soldier Food upkeep", "rulebook", "military_food_demand = ceil(ration_equivalents / 1000)"),
        ("operational rations without double counting", "rulebook", "no path derives one from the other or charges the same Food twice"),
        ("one consistent force snapshot", "rulebook", "neither may recompute a different force"),
        ("correct recruitment timing", "rulebook", "adds the strength points at the **opening of the completion turn's P3.7**"),
        ("valid accepted defensive commitment across TRANSITION/CRISIS", "rulebook", "`WAR-009g` supplies the narrow row-8 exemption and lists the seven conditions"),
        ("new offensive action blocked in the prohibited state", "rulebook", "Submission has no exception."),
        ("independent B-03/B-09 security checks still enforced", "rulebook", "The exemption changes **only** row 8."),
        ("infrastructure-only impairment basis", "b05", "Facility book value is **excluded** from infrastructure impairment"),
        ("facility value unchanged", "b05", "never touched by infrastructure impairment"),
        ("repair cost consistent with B-05", "rulebook", "no material charge and no second discount"),
        ("repair and P5 damage use the defined turn ordering", "rulebook", "P5 damage never retroactively undoes a P4.1 completion"),
        ("reduced housing capacity", "rulebook", "= 45,000 + 100 × I_post_P5(T) + 25,000 × civic_centres"),
        ("B-06 crowding and demographic calculation", "b06", "`DMP-031` applies the ordinary crowding decline"),
        ("recovery after infrastructure repair", "b06", "crowding stops once housing covers the population again"),
        ("correct conflict register statement", "rulebook", "**Two distinct paths, never one pool.**"),
        ("correct project handoff statement", "handoff", "**city targeting with bounded, recoverable infrastructure damage**"),
    ]
    for label, doc, probe in clean_claims:
        check(probe in bodies.get(doc, ""), "8c-clean", f"clean fixture claim {label!r} is not supported by {doc}: {probe!r}")

    # --- 8c-b. CF-02: OP regeneration and reservation clean fixture ---------
    # Hand arithmetic over §8.1. One national pool opens at 8 with cap 10.
    # The sequence exercises simultaneous acceptance, cancellation, a P2
    # failure, one P3.7 regeneration, a duplicate boundary retry, P5
    # consumption, the P7 close and the next boundary. Nothing is executed
    # against a live store; the fixture is documentation arithmetic.
    op_cap = 10
    op_balance = 8
    reserved = 0
    regenerated: dict[str, int] = {}
    ledger: list[tuple[str, str, int]] = []

    def op_accept(action_id: str, cost: int) -> None:
        """Reserve an operation's cost and record the hold."""
        nonlocal reserved
        reserved += cost
        ledger.append(("HELD", action_id, cost))

    def op_release(action_id: str, cost: int) -> None:
        """Release a reserved operation cost."""
        nonlocal reserved
        reserved -= cost
        ledger.append(("RELEASED", action_id, cost))

    def op_consume(action_id: str, cost: int) -> None:
        """Consume a reserved cost from the held and available balance."""
        nonlocal reserved, op_balance
        reserved -= cost
        op_balance -= cost
        ledger.append(("CONSUMED", action_id, cost))

    def op_regenerate(turn_id: str) -> int:
        """Grant one point up to the cap once per turn."""
        nonlocal op_balance
        if turn_id in regenerated:
            return regenerated[turn_id]
        granted = min(op_cap, op_balance + 1) - op_balance
        op_balance += granted
        regenerated[turn_id] = granted
        ledger.append(("REGENERATED", turn_id, granted))
        return granted

    op_accept("A", 2)
    op_accept("B", 3)
    op_accept("C", 1)
    reserved_after_accept = reserved                      # 6
    available_after_accept = op_balance - reserved        # 2
    op_release("C", 1)                                    # cancelled while OPEN
    reserved_after_cancel = reserved                      # 5
    op_release("B", 3)                                    # P2 failure
    reserved_after_p2 = reserved                          # 2
    first_grant = op_regenerate("T")                      # +1
    balance_after_regen = op_balance                      # 9
    available_after_regen = op_balance - reserved         # 7
    duplicate_grant = op_regenerate("T")                  # same receipt, writes nothing
    events_after_retry = len(ledger)                      # 6
    op_consume("A", 2)                                    # P5
    final_balance = op_balance                            # 7
    final_reserved = reserved                             # 0
    final_available = op_balance - reserved               # 7
    regenerated_items = sum(1 for kind, _, _ in ledger if kind == "REGENERATED")  # 1
    next_grant = min(op_cap, op_balance + 1) - op_balance  # 1
    cap_balance = 10
    cap_grant = min(op_cap, cap_balance + 1) - cap_balance  # 0
    alliance_can_spend = False                            # WAR-039 / WAR-161

    clean_op = (
        reserved_after_accept, available_after_accept, reserved_after_cancel,
        reserved_after_p2, first_grant, balance_after_regen,
        available_after_regen, duplicate_grant, events_after_retry,
        final_balance, final_reserved, final_available, regenerated_items,
        next_grant, cap_grant, alliance_can_spend,
    )
    expected_op = (
        6, 2, 5,
        2, 1, 9,
        7, 1, 6,
        7, 0, 7, 1,
        1, 0, False,
    )
    check(clean_op == expected_op, "8c-clean", f"OP clean fixture arithmetic is {clean_op}, expected {expected_op}")
    check(sum(1 for kind, _, _ in ledger if kind == "HELD") == 3, "8c-clean", "OP clean fixture does not hold three simultaneous actions")
    check(ledger[:5] == [("HELD", "A", 2), ("HELD", "B", 3), ("HELD", "C", 1), ("RELEASED", "C", 1), ("RELEASED", "B", 3)], "8c-clean", "OP clean fixture ledger order is wrong")
    check(ledger[-2:] == [("REGENERATED", "T", 1), ("CONSUMED", "A", 2)], "8c-clean", "OP clean fixture ledger does not end with one regeneration and one consumption")
    check(0 <= final_available <= final_balance <= op_cap and final_reserved <= final_balance, "8c-clean", "OP clean fixture violates the WAR-041 invariants")

    clean_op_claims = [
        ("one OP regenerated at the P3.7 opening", "rulebook", "the only OP regeneration is at P3.7, and P0 and the P7 close never regenerate"),
        ("regeneration is capped by the national cap", "rulebook", "`op_balance = min(op_cap, op_balance + 1)`"),
        ("reservation occurs at acceptance", "rulebook", "At acceptance, while the turn is OPEN, before P1 freeze"),
        ("consumption occurs at P5", "rulebook", "At P5 resolution"),
        ("release restores availability without refunding the balance", "rulebook", "A `RELEASED` item leaves `op_balance` unchanged because the amount was only reserved, never debited"),
        ("duplicate boundary processing is idempotent", "rulebook", "A retry of the same idempotency key returns the original receipt and writes nothing"),
        ("action limits are not a general budget", "rulebook", "These are B-10's declared limits under D-024; they are not a general action budget."),
        ("the pool is one national pool with no Alliance authority", "rulebook", "No Alliance role can read a member's private military state, spend a member's OP or resources"),
        ("the P7 close releases unresolved actions and forces reserved to zero", "rulebook", "The close then verifies `reserved = 0`"),
    ]
    for label, doc, probe in clean_op_claims:
        check(probe in bodies.get(doc, ""), "8c-clean", f"OP clean fixture claim {label!r} is not supported by {doc}: {probe!r}")

    # --- 8d. Structured semantic evidence ----------------------------------
    # One summary record per corrected area. Each names the claim, the rule
    # anchors that carry it, the fixtures that attempt to violate it, and the
    # method. A record is evidence of documentation consistency only.
    evidence = [
        {"claim": "Military Food demand uses soldier-equivalents and is separate from civilian demand", "anchors": ("WAR-053a", "WAR-053b", "WAR-053c"), "fixtures": ("NF-01", "NF-02"), "method": "semantic"},
        {"claim": "Civilian Food has priority and the garrison sees only unreserved Food", "anchors": ("WAR-053c",), "fixtures": ("NF-03", "NF-35", "NF-54"), "method": "semantic"},
        {"claim": "A short ration cancels in full, costs 100 readiness and sets RATION_SHORT", "anchors": ("WAR-053d", "WAR-053e", "WRF-35"), "fixtures": ("NF-04", "NF-05"), "method": "semantic"},
        {"claim": "The OP-09 field ration is distinct and never double-counted", "anchors": ("WAR-053f", "WAR-053g"), "fixtures": ("NF-06", "NF-36", "NF-38"), "method": "semantic"},
        {"claim": "Only OP-05 may target a city and it never bypasses a national check", "anchors": ("WAR-009b", "WAR-109a", "WAR-109b"), "fixtures": ("NF-07", "NF-08", "NF-33"), "method": "semantic"},
        {"claim": "Infrastructure damage is bounded, preserves facilities and creates no casualty", "anchors": ("WAR-109d", "WAR-109e", "WAR-109f", "WAR-109j"), "fixtures": ("NF-09", "NF-10", "NF-11", "NF-12"), "method": "semantic"},
        {"claim": "Repair is bounded and P4.1 precedes P5 with no retroactive undo", "anchors": ("WAR-109h", "WAR-109i"), "fixtures": ("NF-13", "NF-34"), "method": "semantic"},
        {"claim": "OP is a persistent national ledger regenerated once at the P3.7 opening and never at P0 or P7, with carry below the cap", "anchors": ("WAR-039", "WAR-040", "WAR-043a", "WAR-043b"), "fixtures": ("NF-14", "NF-15", "NF-16", "NF-17", "NF-18", "NF-59", "NF-61", "NF-63", "NF-66", "NF-67", "NF-73"), "method": "semantic"},
        {"claim": "Every OP movement is one recorded ledger item; reservations, releases and consumptions are single and idempotent and the pool is never transferable or shared", "anchors": ("WAR-041", "WAR-042", "WAR-043", "WAR-043b"), "fixtures": ("NF-60", "NF-62", "NF-64", "NF-65", "NF-68", "NF-69", "NF-70", "NF-71", "NF-72"), "method": "semantic"},
        {"claim": "One canonical validator runs independently and cumulatively and moves nothing on failure", "anchors": ("WAR-009", "WAR-009a", "WAR-009e", "WAR-009f"), "fixtures": ("NF-19", "NF-20", "NF-21", "NF-22", "NF-23", "NF-24"), "method": "semantic"},
        {"claim": "Political states block new orders without pausing war or changing accepted defensive commitments", "anchors": ("WAR-053j", "WAR-053k"), "fixtures": ("NF-25", "NF-26", "NF-27"), "method": "semantic"},
        {"claim": "Denial and blockade combine once, additively and under a cap", "anchors": ("WAR-071", "WAR-071a", "WAR-072"), "fixtures": ("NF-28", "NF-29"), "method": "semantic"},
        {"claim": "City destruction, transfer, facility loss and espionage ownership remain prohibited or unassigned", "anchors": ("WAR-102", "WAR-109j", "B10-C30"), "fixtures": ("NF-30", "NF-31", "NF-32", "NF-56", "NF-57"), "method": "semantic"},
    ]

    # The seven Prompt 10B-C2 defects carry a full ten-field record. Each
    # `expected` value is hand-derived from the named formula; each `actual`
    # value is the outcome the canonical text states. Equality is the check:
    # the API/ID surface alone is not accepted as semantic evidence.
    semantic_records = [
        {
            "id": "SR-01",
            "defect": "OP-09 could reserve Food needed by protected civilians",
            "contradiction": "`available_if_held` deducted `op09_held_total` before civilian demand was met, and `WAR-053f` accepted a 4-Food field ration without a protected-requirement test, so an accepted OP-09 could leave civilians below `food_demand`.",
            "authority": "B-04 ECN-080/ECN-082 (civilian demand is canonical and computed first) and ECN-105 rank 6(a); B-10 §9.3.",
            "corrected_b10": "`WAR-053l` defines `protected_civilian_food = food_demand`, accepts an OP-09 reservation only from `eligible_op09_surplus` above that requirement, and releases reservations in reverse acceptance order at P3.6; `WAR-053c`/`WAR-053f` forbid taking protected Food and fail the whole action with `WRF-25`.",
            "companion": "B-04 ECN-081 (OP-09 is reserved only above the protected requirement), ECN-082 (release test and `unmet_food`), ECN-108 (no wealth path).",
            "formula": "`eligible_op09_surplus = opening_food + projected_food_production − other_food_reservations − protected_civilian_food`; `available_if_held = food_after_other − op09_held_total`; `food_consumed = min(food_after_other − op09_held_after_release, food_demand)`; `unmet_food = max(0, food_demand − (food_after_other − op09_held_after_release))`.",
            "scenario": "Opening 20, planned and actual production 40, another action holds 6, demand 50, one OP-09 requests 4. Acceptance: `eligible = 20 + 40 − 6 − 50 = 4`, so 4 are reserved. P3.6: `available_if_held = 54 − 4 = 50`, the reservation stands and civilians consume 50. With actual production 35: `available_if_held = 45`, the 4 are released, the action fails `WRF-25`, `food_for_civilians = 49` and `unmet_food = 1`.",
            "expected": "Reservation stands only while `available_if_held >= 50`; on the 35-production path all 4 are released, civilians receive 49, unmet is 1, no protected Food is spent and no debt is created.",
            "actual": "Reservation stands only while `available_if_held >= 50`; on the 35-production path all 4 are released, civilians receive 49, unmet is 1, no protected Food is spent and no debt is created.",
            "reviewer": "Document comparison of ECN-082 against WAR-053l and the F-EC-003/`WAR-053l` worked examples, with the arithmetic re-derived by hand.",
            "limitation": "Proves that the published formulas and examples agree; it does not prove that any inventory implementation matches them, because no runtime exists.",
            "anchors": ("WAR-053l", "WAR-053c", "WAR-053f", "ECN-082", "ECN-081"),
            "fixtures": ("NF-35", "NF-36", "NF-37", "NF-38", "NF-54"),
            "method": "semantic + hand arithmetic",
        },
        {
            "id": "SR-02",
            "defect": "Undefined P3.0 recruitment arrival and inconsistent force snapshots",
            "contradiction": "Recruitment arrival was written at `P3.0`, which B-02 does not define, and `WAR-050` (readiness) and `WAR-053b` (Food) each described the force independently, so one turn could charge rations against one population and roll readiness against another.",
            "authority": "B-02 P0–P7 sequence and TR-040 (a subsystem owns its internal ordering; no phase may be invented).",
            "corrected_b10": "`WAR-053m` removes P3.0, declares one step at the opening of P3.7 inside the authorized P3.7 subphase, stores one immutable snapshot read by both `F-WR-036` and `F-WR-003`, and lists the excluded categories; `WAR-058` places recruitment arrival in the same step.",
            "companion": "B-02 TR-040; B-04 ECN-105 rank 6(b) readiness obligation reads the same snapshot.",
            "formula": "`ration_equivalents = 10 × INF + 4 × ARM + 2 × AIR + 20 × NAV`; `military_food_demand = ceil(ration_equivalents / 1000)`; both `F-WR-036` and `F-WR-003` read `snapshot_P3_7`.",
            "scenario": "Opening force 9,000 INF. An infantry order placed at P4 of turn 100 completes at turn 101 and enters turn 101's snapshot: 10,000 INF = 100,000 equivalents = 100 Food. An armour order placed at P4 of 100 completes at 102 and is excluded from 101. A P4 disband in 101 changes the P5 force only; current-turn P4 recruitment, pending, cancelled and P5-lost strength are excluded.",
            "expected": "Turn 101 demand is 100 Food from 10,000 INF; Food and readiness read identical stored values; no P3.0 reference survives.",
            "actual": "Turn 101 demand is 100 Food from 10,000 INF; Food and readiness read identical stored values; no P3.0 reference survives.",
            "reviewer": "Rule-by-rule comparison of WAR-050, WAR-053b, WAR-053m and WAR-058 against the B-02 phase table, with the training-turn arithmetic re-derived.",
            "limitation": "The snapshot excludes voluntary P4 disbanding for the P5 baseline by rule; this is a stated, justified difference, not a proven implementation behaviour.",
            "anchors": ("WAR-053m", "WAR-058", "WAR-050", "F-WR-036", "F-WR-003"),
            "fixtures": ("NF-39", "NF-40"),
            "method": "semantic + hand arithmetic",
        },
        {
            "id": "SR-03",
            "defect": "A valid accepted defensive commitment could be rejected by the political-state check",
            "contradiction": "`WAR-009` row 8 denied every action in `TRANSITION`/`CRISIS`, including an operation accepted while the state was normal, so the validator could reject the defensive commitment B-06 `DMP-265` requires to resolve; the text also read as if the whole validator were relaxed.",
            "authority": "B-06 DMP-265 (war does not pause and an existing defensive commitment resolves); B-09 treaty/NAP checks; B-03 protection.",
            "corrected_b10": "`WAR-009c`/`WAR-009g` exempt a qualifying accepted defensive commitment from row 8 only at P2 and pre-P5, list seven conditions, keep submission without exception, and keep checks 1–7 and 9–12 independent and cumulative; `WAR-053k` states the same boundary.",
            "companion": "B-06 DMP-265; B-09 NAP/treaty validation; B-03 protection layers.",
            "formula": "No new formula. The exemption predicate requires: accepted before `state_began`, a recorded `action_id`, still held at execution, `defensive = TRUE`, resources still reserved, not expired, and a still-valid target.",
            "scenario": "Nation A accepts `FORTIFY` in turn 100 while `NORMAL` and enters `CRISIS` in 101. At P2 of 101 row 8 passes only because all seven conditions hold; a B-09 NAP over the target still blocks the same commitment, and a new `RAID` submitted in 101 fails at submission. An accepted offensive operation fails at P2/pre-P5 and releases.",
            "expected": "The qualifying defensive commitment resolves; the new offensive order is rejected `WRF-09`; an independent B-09 block still rejects the commitment.",
            "actual": "The qualifying defensive commitment resolves; the new offensive order is rejected `WRF-09`; an independent B-09 block still rejects the commitment.",
            "reviewer": "Eight-scenario row-by-row review of the `B10-C26` table against the twelve validator checks and DMP-265.",
            "limitation": "Document-level only; the eight scenarios are specification cases and no combat engine was executed.",
            "anchors": ("WAR-009c", "WAR-009g", "WAR-053k", "B10-C26", "DMP-265"),
            "fixtures": ("NF-41", "NF-42", "NF-43"),
            "method": "semantic case review",
        },
        {
            "id": "SR-04",
            "defect": "Infrastructure impairment used an undefined total city book value",
            "contradiction": "`F-WR-038` impaired `city_book_value_before`, an undefined total that included facilities and had no initial basis, so a strike could impair facility value and the first strike's arithmetic depended on an unstated opening number.",
            "authority": "B-04 ECN-108 fixed-asset book value; B-05 URB-047 (granted facilities carry 0) and URB-043/URB-044.",
            "corrected_b10": "`WAR-109g`/`WAR-109m` define an infrastructure-only subledger: gross capitalised upgrade lots, accumulated impairment and carrying value; the 50/10 opening lot has zero capitalised cost; facilities are excluded and never impaired; impairment is capped at carrying value and idempotent on `damage_event_id`.",
            "companion": "B-05 URB-118a/URB-118b; B-04 ECN-108; F-CI-019 aggregates carrying values instead of a second city-book number.",
            "formula": "`gross = Σ completed UPGRADE_INFRASTRUCTURE capitalized lots`; `carrying = gross − accumulated`; `impaired = min(carrying_before, floor(carrying_before × removed / I_combat))`; `fixed_asset_book_value = Σ carrying + Σ other recognised assets`.",
            "scenario": "`I = 50` at zero-cost basis; buy 50→60 for 130; a facility is worth 5,000, so national fixed assets are 5,130. A strike removes 3: `impaired = min(130, floor(130 × 3/60)) = 6`; carrying 124; national assets 5,124; the facility remains 5,000. A second strike of 3 impairs `floor(163 × 3/60) = 8` after the repair that raised carrying to 163.",
            "expected": "Carrying 124 after the first strike, facility still 5,000, national assets 5,124, accumulated 6 never above gross; a city at its zero-cost opening lot records impairment 0 and still records the level loss.",
            "actual": "Carrying 124 after the first strike, facility still 5,000, national assets 5,124, accumulated 6 never above gross; a city at its zero-cost opening lot records impairment 0 and still records the level loss.",
            "reviewer": "Cross-read of ECN-108, F-CI-019, URB-118a/URB-118b and F-WR-038, with every crown value recomputed by hand.",
            "limitation": "The subledger is a specification contract; no ledger, migration or reconciliation job exists to be tested.",
            "anchors": ("WAR-109g", "WAR-109m", "URB-118a", "URB-118b", "ECN-108"),
            "fixtures": ("NF-44", "NF-45", "NF-46", "NF-58"),
            "method": "semantic + hand arithmetic",
        },
        {
            "id": "SR-05",
            "defect": "Repair cost contradicted B-05 and could capitalise twice",
            "contradiction": "The draft added a materials surcharge and a second discount to repair, contradicting B-05's `URB-043`/`URB-044`, and capitalised the repair more than once; `B10-C21` also merged military recovery with city infrastructure repair.",
            "authority": "B-05 URB-043 (stepped marginal cost) and URB-044 (Civil Survey ceiling); URB-118a lot capitalisation.",
            "corrected_b10": "`WAR-109h` uses exactly `Σ(8 + floor(j/10))`, applies the Civil Survey at most once, adds no materials, reserves crowns at acceptance, charges capex at P4.1, capitalises one new lot, never reverses impairment, is idempotent on `order_id`, and `B10-C21` separates the two recovery paths.",
            "companion": "B-05 URB-043/URB-044/URB-118a/URB-157 item 6; B-04 ECN-108.",
            "formula": "`base_repair_cost = Σ_{j=I}^{I+n−1} (8 + floor(j / 10))`; `repair_cost = ceil(base × 9,000 / 10,000)` only with Civil Survey, else `base`; `gross += repair_cost`; `accumulated` unchanged; `carrying += repair_cost`.",
            "scenario": "`I = 57`, repair 3 levels: `3 × (8 + floor(57/10)) = 3 × 13 = 39`; without Civil Survey the cost is 39, carrying moves 124→163 and accumulated stays 6. With Civil Survey the cost is `ceil(39 × 0.9) = 36`. Replaying the same `order_id` adds nothing.",
            "expected": "39 crowns (36 with Civil Survey), one capitalised lot, carrying 163, accumulated 6, no materials, no second discount and no second capitalisation on retry.",
            "actual": "39 crowns (36 with Civil Survey), one capitalised lot, carrying 163, accumulated 6, no materials, no second discount and no second capitalisation on retry.",
            "reviewer": "Term-by-term comparison of WAR-109h and F-WR-038 with URB-043/URB-044, plus a replay check of the `order_id` idempotency statement.",
            "limitation": "Idempotency is asserted by the specification; no transaction or retry harness was run.",
            "anchors": ("WAR-109h", "URB-043", "URB-044", "URB-118a", "B10-C21"),
            "fixtures": ("NF-47", "NF-48", "NF-55"),
            "method": "semantic + hand arithmetic",
        },
        {
            "id": "SR-06",
            "defect": "Repair and damage used inconsistent timing snapshots",
            "contradiction": "`URB-046` said repaired capacity and housing were available 'next turn' while `WAR-109i` said a P4.1 repair is present for the same turn's P5 strike, and the damage formula read an unnamed 'current level'; the statements could not both hold.",
            "authority": "B-02's P4.1/P5 ordering; B-05 URB-046 and URB-051a capacity-overdraw check.",
            "corrected_b10": "`WAR-109m` names every snapshot — `I_open`, `I_pre`, `I_post_P4_1`, `I_combat`, `I_post_P5`, `capacity_construction(T)`, `capacity_effective(T+1)`, `housing_population(T)`, `housing_effective(T+1)`, `BV_post_P4_1`, `BV_post_P5` — and states that P5 combat reads the physical `I_combat` while capacity and housing read their own effective boundaries.",
            "companion": "B-05 URB-046 (exact boundaries) and URB-051a; B-04 ECN-108 at a P3.8 reads the prior turn's written book value.",
            "formula": "`I_combat = I_post_P4_1`; `I_post_P5 = I_combat − removed` (floor 10); `capacity_construction(T) = 10 + floor(I_open(T)/10)`; `capacity_effective(T+1) = 10 + floor(I_post_P5(T)/10)`; `housing_population(T) = 45,000 + 100 × I_open(T) + 25,000 × civic`; `housing_effective(T+1) = 45,000 + 100 × I_post_P5(T) + 25,000 × civic`.",
            "scenario": "`I_open = 57`; repair 3 → `I_combat = 60`; a strike removes 3 → `I_post_P5 = 57`. `capacity_construction(T) = 15` and `housing_population(T) = 50,700`; T+1 capacity is 15 and housing 50,700. A facility order needing 14 + 2 DC is rejected in T even with the repair ordered, and becomes acceptable in T+2 when `capacity_effective = 16`.",
            "expected": "The same-turn strike measures 60; T's construction capacity is 15; T+1 capacity is 15 after the damage; no rule reads an unnamed 'current level'.",
            "actual": "The same-turn strike measures 60; T's construction capacity is 15; T+1 capacity is 15 after the damage; no rule reads an unnamed 'current level'.",
            "reviewer": "Table-by-table review of WAR-109i/WAR-109m against URB-046, with all seven timing examples recomputed.",
            "limitation": "Specification consistency only; the turn engine does not exist to observe the boundaries at runtime.",
            "anchors": ("WAR-109m", "WAR-109i", "URB-046", "URB-051a", "ECN-108"),
            "fixtures": ("NF-49", "NF-50"),
            "method": "semantic + hand arithmetic",
        },
        {
            "id": "SR-07",
            "defect": "Housing loss was described as paused growth instead of B-06 crowding",
            "contradiction": "B-10 described the housing effect of damage as 'paused growth', while B-06 `DMP-031` already applies a crowding decline of `ceil(excess/10)` with a natural-decline comparison and a 1,000 floor; the two descriptions produced different populations for the same shortfall.",
            "authority": "B-06 DMP-028 (growth), DMP-031 (crowding), DMP-034 (one P3.8 settlement), DMP-037 (housing).",
            "corrected_b10": "`WAR-109f`/`WAR-109m` and B-06 `DMP-031a` make infrastructure damage a housing-source change: no casualty, eviction or transfer at P5; the reduced housing is read at the next P3.8 and the ordinary `DMP-031` crowding rule applies; repair restores housing at the same boundary.",
            "companion": "B-05 URB-042/URB-046 and URB-157 item 3; B-06 DMP-031a.",
            "formula": "`housing_effective(T+1) = 45,000 + 100 × I_post_P5(T) + 25,000 × civic`; `excess = max(0, population − housing)`; `decline = max(ceil(excess/10), max(0, population − natural))`; `population_next = max(1,000, population − decline)`.",
            "scenario": "Population 50,000, `I = 50`, no civic centre, housing 50,000. A strike removes 10 → `I_post_P5 = 40`, housing 49,000, no P5 casualty. P3.8 of T+1 with `growth_bp = 50`: `natural = 50,250`, excess 1,000, `decline = max(100, 0) = 100`, population 49,900. Repair to 50 at P4.1 gives housing 50,000; at the next P3.8 excess is 0 and no crowding applies. With natural 49,500 the decline is `max(100, 500) = 500`.",
            "expected": "Population 49,900 after one settlement at the illustrated growth; no casualty at P5; the natural decline dominates when it is larger; crowding stops once housing covers population.",
            "actual": "Population 49,900 after one settlement at the illustrated growth; no casualty at P5; the natural decline dominates when it is larger; crowding stops once housing covers population.",
            "reviewer": "Recomputation of the WAR-109 housing example against DMP-031/F-PD-011, including the natural-decline branch.",
            "limitation": "`growth_bp = 50` is a provisional illustration, not a calibrated value; Prompt 14 calibration remains required.",
            "anchors": ("WAR-109f", "WAR-109m", "DMP-031", "DMP-031a", "DMP-034"),
            "fixtures": ("NF-51", "NF-52", "NF-53"),
            "method": "semantic + hand arithmetic",
        },
    ]

    check(len(evidence) == 13, "8d-evidence", f"semantic evidence record count is {len(evidence)}, expected 13")
    check(len(semantic_records) == 7, "8d-evidence", f"full semantic record count is {len(semantic_records)}, expected 7")
    all_bodies = "\n".join(bodies.values())
    required_fields = (
        "defect", "contradiction", "authority", "corrected_b10", "companion",
        "formula", "scenario", "expected", "actual", "reviewer", "limitation",
    )
    coverage = set()
    for record in evidence:
        for anchor in record["anchors"]:
            check(anchor in all_bodies, "8d-evidence", f"evidence anchor {anchor} does not resolve")
        for fid in record["fixtures"]:
            check(fid in fixture_ids, "8d-evidence", f"evidence record names unknown fixture {fid}")
            coverage.add(fid)
    for record in semantic_records:
        for field in required_fields:
            value = record.get(field)
            check(isinstance(value, str) and bool(value.strip()), "8d-evidence", f"{record.get('id', '?')} field {field!r} is missing or empty")
        check(record["expected"] == record["actual"], "8d-evidence", f"{record['id']} expected result differs from the documented actual result")
        for anchor in record["anchors"]:
            check(anchor in all_bodies, "8d-evidence", f"{record['id']} anchor {anchor} does not resolve")
        for fid in record["fixtures"]:
            check(fid in fixture_ids, "8d-evidence", f"{record['id']} names unknown fixture {fid}")
            coverage.add(fid)
    check(coverage == set(fixture_ids), "8d-evidence", f"fixtures without a semantic record: {sorted(set(fixture_ids) - coverage)}")
    check(len(set(r["id"] for r in semantic_records)) == 7, "8d-evidence", "semantic record IDs are not unique")
    check(len(set(r["defect"] for r in semantic_records)) == 7, "8d-evidence", "semantic records do not name seven distinct defects")

    # --- 9. Prompt 10C boundary --------------------------------------------
    # 2026-11-04 (Prompt 10C): these two checks asserted that Prompt 10C had not
    # started. 10C is now complete at the specification/documentation level, so
    # the companion must exist; the checks are inverted, not removed, and the
    # 10B boundary they protected is still enforced by the handoff and §30 checks
    # below (10C may not invent B-10 content).
    workflow_path = docs / "stage-2" / "17_warfare_workflows_acceptance.md"
    check(workflow_path.exists(), "9-boundary", "the Prompt 10C workflow/acceptance companion is missing")
    check(bool(workflow_path.exists() and workflow_path.read_text(encoding="utf-8").strip()),
          "9-boundary", "the Prompt 10C workflow/acceptance companion is empty")

    handoff = section(rulebook, "## 29.", "## 30.")
    check("Prompt 10C owns workflows, acceptance cases and traceability." in handoff, "9-boundary", "§29 does not assign workflows and acceptance to Prompt 10C")
    check("**must not invent** campaign architecture, OP economics, battle formulas, operation costs, settlement logic or permissions" in handoff, "9-boundary", "§29 does not forbid 10C from inventing B-10 content")
    check(handoff.count("| ") >= 18, "9-boundary", "§29.1 handoff table is incomplete")
    for prompt in ("Prompt 11", "Prompt 12", "Prompt 13", "Prompt 14", "Prompt 15"):
        check(prompt in handoff, "9-boundary", f"§29.3 does not hand off to {prompt}")

    completion = section(rulebook, "## 30.", None)
    check("No implementation." in completion, "9-boundary", "§30.2 does not disclaim implementation")
    check("No gameplay or integration test." in completion, "9-boundary", "§30.2 does not disclaim runtime testing")
    check("No 10C acceptance suite." in completion, "9-boundary", "§30.2 does not leave the acceptance suite to Prompt 10C")
    check("No P&W value imported as an NS value." in completion, "9-boundary", "§30.2 does not disclaim imported P&W values")
    check("The next task is **Prompt 10C" in completion, "9-boundary", "§30.6 does not name Prompt 10C as the next task")
    check("not implemented, not balanced, not playtested and not released" in completion, "9-boundary", "§30.6 overclaims completion")

    # --- 10. Continuity -----------------------------------------------------
    check("## 58." in log, "10-continuity", "progress log has no §58 for Prompt 10B")
    log_58 = section(log, "## 58.", None)
    check("prompt 10b is complete" in log_58.lower(), "10-continuity", "§58 does not record 10B complete")
    check("Prompt 10C" in log_58, "10-continuity", "§58 does not name Prompt 10C as next")
    status_rules = (docs / "qa_backups" / "status_rules.py").read_text(encoding="utf-8")
    # 2026-11-04 (Prompt 10C): the live prompt advanced to 11 when 10C closed.
    # 2026-11-04 (Prompt 11A): Prompt 11 then split, and 11A research closed, so
    # the live sub-prompt is 11B. The 10-family completion facts are unchanged.
    # 2026-11-06 (Prompt 11C-C1): 11C closed the Prompt 11 family, so the live
    # prompt is 12. The value is advanced here rather than in a duplicated
    # constant, so the two surfaces cannot drift apart.
    check('CURRENT_SUBPROMPT = "12"' in status_rules, "10-continuity", "status_rules.py does not set 12 as the current prompt")
    check("11C" in COMPLETED_SUBPROMPTS, "10-continuity", "status_rules.py does not list 11C as completed")
    check('"10B"' in status_rules, "10-continuity", "status_rules.py does not list 10B as completed")
    check('"10C"' in status_rules, "10-continuity", "status_rules.py does not list 10C as completed")

    return problems, checks


def main(argv: list[str]) -> int:
    """Run the validator and return the exit code."""
    docs = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parents[1]
    problems, checks = validate(docs)
    print(f"10B Warfare validator - {docs}")
    print(f"Checks run: {checks}")
    if problems:
        print(f"FAIL: {len(problems)} problem(s)")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("Negative fixtures: 73/73 rejected; clean fixtures CF-01 and CF-02 PASS; semantic evidence records: 13 summaries + 7 full")
    print("PASS: all B-10 structure, disposition, formula, register and boundary checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
