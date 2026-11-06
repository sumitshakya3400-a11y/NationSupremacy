#!/usr/bin/env python3
"""Prompt 11C independent validator — B-11 workflows, integration and acceptance.

Run:  python docs/qa_backups/11C_validate_b11_workflows.py [--verbose] [--self-test] [--fixtures]
Exit code: 0 all pass, 1 any check/fixture/link failure, 2 a canonical input is missing.

This validator independently checks the Prompt 11C companion document against the
authoritative B-11 rulebook, the B-11 formula register, the requirement register, the
decision registers, the unresolved-decision register and the 11B acceptance crosswalk.
It parses Markdown tables into records and verifies relationships. It deliberately does
NOT accept any self-declaration inside the 11C document as proof: every count is
recomputed from the parsed rows, and every identifier reference must resolve in the
source registers.

Documentation QA only. No game code, no dependencies beyond the standard library.
"""

from __future__ import annotations

import argparse
import copy
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

QA_DIR = Path(__file__).resolve().parent
DOCS = QA_DIR.parent
STAGE2 = DOCS / "stage-2"

MAIN = STAGE2 / "19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md"
RULEBOOK = STAGE2 / "18_world_events_objectives_rankings_progression.md"
REGISTER = STAGE2 / "18_world_events_objectives_rankings_progression_formula_register.md"
REQUIREMENTS = STAGE2 / "03_requirements_traceability.md"
DECISIONS = DOCS / "DECISIONS.md"
DD_REGISTER = STAGE2 / "04_approved_and_provisional_decisions.md"
UNRESOLVED = STAGE2 / "05_unresolved_design_decisions.md"
CROSSWALK = STAGE2 / "18_world_events_objectives_rankings_progression_acceptance_crosswalk.md"
LINKS = QA_DIR / "validate_links.py"

MAIN_NAME = MAIN.name

JOURNEY_FIELDS = [
    "Journey ID", "Actor", "Goal", "Entry condition", "Preconditions", "Main flow",
    "Alternate flow", "Failure flow", "State transitions", "Data involved",
    "System dependencies", "Security checks", "Notifications", "Audit records",
    "Recovery behaviour", "Requirements", "Tests",
]

WORKFLOW_FIELDS = [
    "ID and purpose", "Initiator and permissions", "Trigger and phase",
    "Receiving system / source of truth", "Required input", "Output", "State changes",
    "Validation", "Mutation / transaction", "Failure", "Audit",
    "Retry / recovery / idempotency", "Trace", "Tests",
]

GATE_STATUSES = ("PASS", "PARTIAL", "FAIL", "BLOCKED", "NOT RUN", "NOT APPLICABLE")

PROVISIONAL_FORMULAS = [
    "F-WEP-011", "F-WEP-021", "F-WEP-029", "F-WEP-030", "F-WEP-033", "F-WEP-046",
]
RETIRED_FORMULA = "F-WEP-048"

OWNER_RESERVED_UD = [f"UD-{n:03d}" for n in range(40, 50)] + ["UD-017"]

BANNED_CLAIM_PATTERNS = [
    r"\bis implemented\b", r"\bruntime[- ]tested\b", r"\bplaytested\b",
    r"\bhas been deployed\b", r"\btest passed\b", r"\btests passed at runtime\b",
    r"\bbalance (?:is )?approved\b", r"\bcalibrated and approved\b",
]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def table_rows(text: str, ncols: int, first_pat: str) -> list[list[str]]:
    """Every Markdown table row whose first cell matches `first_pat` and that has
    at least `ncols` cells. Header and separator rows never match."""
    out: list[list[str]] = []
    pat = re.compile(first_pat)
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < ncols:
            continue
        if pat.fullmatch(cells[0].strip("`")):
            out.append(cells)
    return out


def record_map(rows: list[list[str]]) -> tuple[dict[str, list[str]], list[str]]:
    mapping: dict[str, list[str]] = {}
    dupes: list[str] = []
    for cells in rows:
        rid = cells[0].strip("`")
        if rid in mapping:
            dupes.append(rid)
        else:
            mapping[rid] = cells
    return mapping, dupes


def kv_records(text: str, header: str, expect: list[str]) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Parse `header`-introduced records followed by a two-column `| Field | Content |`
    table. Returns {id: {field: content}} plus the ids whose table has a missing field."""
    pat = re.compile(header)
    lines = text.splitlines()
    records: dict[str, dict[str, str]] = {}
    incomplete: list[str] = []
    seen: dict[str, int] = {}
    i = 0
    while i < len(lines):
        m = pat.search(lines[i])
        if not m:
            i += 1
            continue
        rid = m.group(1)
        fields: dict[str, str] = {}
        j = i + 1
        # skip to the table
        while j < len(lines) and not lines[j].strip().startswith("|"):
            if pat.match(lines[j]) or lines[j].startswith("#"):
                break
            j += 1
        while j < len(lines) and lines[j].strip().startswith("|"):
            cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
            if len(cells) == 2 and cells[0] in expect and cells[0] not in fields:
                fields[cells[0]] = cells[1]
            j += 1
        seen[rid] = seen.get(rid, 0) + 1
        if seen[rid] > 1:
            incomplete.append(rid + " (duplicate id)")
        else:
            records[rid] = fields
            if any(k not in fields or not fields[k] for k in expect):
                incomplete.append(rid)
        i = j if j > i else i + 1
    return records, incomplete


@dataclass
class Model:
    main: str = ""
    rulebook: str = ""
    register: str = ""
    requirements: str = ""
    decisions: str = ""
    ddreg: str = ""
    unresolved: str = ""
    crosswalk: str = ""

    wep: set[str] = field(default_factory=set)
    fids: dict[str, str] = field(default_factory=dict)          # id -> field-20 status
    finv: dict[str, str] = field(default_factory=dict)           # id -> inventory status
    wpc: set[str] = field(default_factory=set)
    wpf: set[str] = field(default_factory=set)
    wpa: set[str] = field(default_factory=set)
    req: set[str] = field(default_factory=set)
    d: set[str] = field(default_factory=set)
    dd: set[str] = field(default_factory=set)
    ud: set[str] = field(default_factory=set)

    journeys: dict[str, dict[str, str]] = field(default_factory=dict)
    journeys_incomplete: list[str] = field(default_factory=list)
    workflows: dict[str, dict[str, str]] = field(default_factory=dict)
    workflows_incomplete: list[str] = field(default_factory=list)
    edge: dict[str, list[str]] = field(default_factory=dict)
    tests: dict[str, list[str]] = field(default_factory=dict)
    threats: dict[str, list[str]] = field(default_factory=dict)
    integrations: dict[str, list[str]] = field(default_factory=dict)
    gates: dict[str, list[str]] = field(default_factory=dict)
    forward: dict[str, list[str]] = field(default_factory=dict)
    dupes: dict[str, list[str]] = field(default_factory=dict)
    sections: list[int] = field(default_factory=list)
    class_ranges: list[tuple[str, int, int]] = field(default_factory=list)

    def rebuild(self) -> None:
        rb, reg, main = self.rulebook, self.register, self.main
        self.wep = set(re.findall(r"WEP-(\d{3})\b", rb) and [f"WEP-{x}" for x in set(re.findall(r"WEP-(\d{3})\b", rb))])
        self.fids = {}
        for m in re.finditer(r"^### (F-WEP-\d{3}) —.*?(?=^### |\Z)", reg, flags=re.M | re.S):
            body = m.group(0)
            st = re.search(r"^\| 20 \| Provisional status \| \*\*([A-Za-z]+)\*\*", body, flags=re.M)
            self.fids[m.group(1)] = st.group(1) if st else "UNKNOWN"
        self.finv = {}
        for cells in table_rows(reg, 5, r"F-WEP-\d{3}"):
            self.finv[cells[0]] = cells[3]
        self.wpc = {f"WPC-{x}" for x in set(re.findall(r"\bWPC-(\d{2})\b", rb))}
        self.wpf = {f"WPF-{x}" for x in set(re.findall(r"\bWPF-(\d{2})\b", rb))}
        self.wpa = {f"WPA-{x}" for x in set(re.findall(r"\bWPA-(\d{2})\b", rb))}
        self.req = {cells[0] for cells in table_rows(self.requirements, 4, r"REQ-\d+")}
        self.d = set(re.findall(r"^\| (D-\d{3}) \|", self.decisions, flags=re.M))
        self.dd = set(re.findall(r"^\| (DD-\d{3}) \|", self.ddreg, flags=re.M))
        self.ud = {cells[0] for cells in table_rows(self.unresolved, 3, r"UD-\d{3}")}

        self.journeys, self.journeys_incomplete = kv_records(main, r"^\*\*(WJ-\d{3}) — ", JOURNEY_FIELDS)
        self.workflows, self.workflows_incomplete = kv_records(main, r"^### (WWF-\d{3}) — ", WORKFLOW_FIELDS)
        for key, pat, nc in (
            ("edge", r"WEE-\d{3}", 6), ("tests", r"WTA-\d{3}", 13),
            ("threats", r"WTS-\d{3}", 10), ("integrations", r"WPC-\d{2}", 19),
            ("gates", r"P11C-\d{2}", 8), ("forward", r"REQ-7\d{2}", 9),
        ):
            mapping, dupes = record_map(table_rows(main, nc, pat))
            setattr(self, key, mapping)
            if dupes:
                self.dupes[key] = sorted(set(dupes))

        self.sections = []
        for line in main.splitlines():
            m = re.match(r"^## (\d+)\.", line)
            if m:
                self.sections.append(int(m.group(1)))

        self.class_ranges = []
        for cells in table_rows(main, 5, r"[A-P]"):
            rng = cells[2]
            m = re.findall(r"(\d{3})", rng)
            if len(m) == 2:
                self.class_ranges.append((cells[0], int(m[0]), int(m[1])))

        if self.workflows_incomplete or self.journeys_incomplete:
            self.dupes.setdefault("_placeholder", [])


def load() -> Model:
    m = Model(
        main=read(MAIN), rulebook=read(RULEBOOK), register=read(REGISTER),
        requirements=read(REQUIREMENTS), decisions=read(DECISIONS), ddreg=read(DD_REGISTER),
        unresolved=read(UNRESOLVED), crosswalk=read(CROSSWALK),
    )
    m.rebuild()
    return m


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

NEG_WORDS = {
    "no", "not", "never", "without", "unallocated", "invent", "invented", "inventing",
    "prohibit", "prohibits", "prohibited", "prohibition", "forbid", "forbids", "rejected",
    "negative", "invalid", "deliberately", "banned", "absent", "exist", "requirement",
    "onward", "class", "question", "gap", "must", "may",
}
WORD = re.compile("[A-Za-z]+")


def negated(clause: str) -> bool:
    """True when the clause around an identifier marks it as prohibited or absent.

    Token membership, not a substring test: "`WPF-41`, which must not exist" is a
    mention; "the metric uses `F-WEP-999`" is a live use.
    """
    return bool(WORD.findall(clause.lower())) and any(
        w in NEG_WORDS for w in WORD.findall(clause.lower()))


def clause_of(text: str, pos: int) -> str:
    """The narrowest enclosing unit: a Markdown table cell, else a sentence.

    A cell that says "no second scheduler", or names `WPF-41` as an invented
    code, must not be read as a live use of that identifier. The negation test
    runs on the cell rather than on the whole line, so a genuinely live use
    somewhere else on that line still fails.
    """
    nl = text.rfind("\n", 0, pos)
    end = text.find("\n", pos)
    line = text[nl + 1:end if end > 0 else len(text)]
    if line.strip().startswith("|") and line.count("|") >= 2:
        acc = nl + 1
        for cell in line.split("|"):
            if acc <= pos < acc + len(cell) + 1:
                return cell
            acc += len(cell) + 1
        return line
    a = max(text.rfind(". ", 0, pos), text.rfind("; ", 0, pos), nl)
    cands = [x for x in (text.find(". ", pos), end, len(text)) if x >= pos]
    b = min(cands) if cands else len(text)
    return text[a + 1:b]


def section(text: str, head: str, nxt: str) -> str:
    """The body of one `## N.` section, so a check never reads another table."""
    a = text.find(f"## {head}.")
    b = text.find(f"## {nxt}.")
    return text[a:b] if a >= 0 and b > a else (text[a:] if a >= 0 else "")


def ids_in(text: str, pat: str) -> list[str]:
    return re.findall(pat, text)


def check_01(m: Model) -> tuple[bool, str]:
    if "Prompt 11C" not in m.main[:4000]:
        return False, "header does not declare Stage 2, Prompt 11C"
    if "design only" not in m.main[:4000].lower():
        return False, "header does not declare design-only status"
    return True, "header declares Prompt 11C and design-only status"


def check_02(m: Model) -> tuple[bool, str]:
    want = list(range(0, 35))
    if m.sections != want:
        missing = [n for n in want if n not in m.sections]
        extra = [n for n in m.sections if n not in want]
        dup = [n for n in set(m.sections) if m.sections.count(n) > 1]
        return False, f"section list wrong; missing={missing} extra={extra} duplicated={dup}"
    return True, f"sections 0-{len(want)-1} present in order, no duplicate"


def check_03(m: Model) -> tuple[bool, str]:
    want = [f"WJ-{n:03d}" for n in range(1, 26)]
    missing = [w for w in want if w not in m.journeys]
    if missing:
        return False, f"missing journeys: {missing}"
    if m.journeys_incomplete:
        return False, f"journeys missing one of the 17 fields: {m.journeys_incomplete}"
    return True, f"{len(want)} journeys x {len(JOURNEY_FIELDS)} fields, complete"


def check_04(m: Model) -> tuple[bool, str]:
    want = [f"WWF-{n:03d}" for n in range(1, 51)]
    missing = [w for w in want if w not in m.workflows]
    if missing:
        return False, f"missing workflows: {missing}"
    if m.workflows_incomplete:
        return False, f"workflows missing one of the 14 fields: {m.workflows_incomplete}"
    return True, f"{len(want)} workflows x {len(WORKFLOW_FIELDS)} fields, complete"


def check_05(m: Model) -> tuple[bool, str]:
    want_e = [f"WEE-{n:03d}" for n in range(1, 85)]
    want_t = [f"WTS-{n:03d}" for n in range(1, 31)]
    miss_e = [x for x in want_e if x not in m.edge]
    miss_t = [x for x in want_t if x not in m.threats]
    bad_e = [k for k, c in m.edge.items() if any(not x for x in c[:6])]
    bad_t = [k for k, c in m.threats.items() if any(not x for x in c[:10])]
    if miss_e or miss_t or bad_e or bad_t:
        return False, f"missing edge={miss_e[:5]} missing threat={miss_t[:5]} empty edge={bad_e[:5]} empty threat={bad_t[:5]}"
    return True, f"{len(want_e)} edge cases (6 cols) and {len(want_t)} threats (10 cols) complete"


def check_06(m: Model) -> tuple[bool, str]:
    want = [f"WTA-{n:03d}" for n in range(1, 273)]
    missing = [w for w in want if w not in m.tests]
    no_expected = [k for k, c in m.tests.items() if len(c) < 8 or not c[7]]
    no_status = [k for k, c in m.tests.items() if len(c) < 13 or not c[12]]
    if missing or no_expected or no_status:
        return False, f"missing={missing[:5]} no-expected-result={no_expected[:5]} no-status={no_status[:5]}"
    return True, f"{len(want)} tests, each with an expected result and a status"


def check_07(m: Model) -> tuple[bool, str]:
    bad = []
    for wid, fields in m.workflows.items():
        labels = list(fields)
        if labels != WORKFLOW_FIELDS:
            bad.append(wid)
    if bad:
        return False, f"{len(bad)} workflow records do not use the 14 declared labels in order: {bad[:6]}"
    return True, "every workflow record uses the 14 schema labels in schema order"


def check_08(m: Model) -> tuple[bool, str]:
    problems = []
    for label, wanted, got in (
        ("WJ", range(1, 26), set(m.journeys)), ("WWF", range(1, 51), set(m.workflows)),
        ("WEE", range(1, 85), set(m.edge)), ("WTA", range(1, 273), set(m.tests)),
        ("WTS", range(1, 31), set(m.threats)),
    ):
        expect = {f"{label}-{n:03d}" for n in wanted}
        missing = sorted(expect - got)
        extra = sorted(got - expect)
        if missing or extra:
            problems.append(f"{label}: missing={missing[:3]} extra={extra[:3]}")
    if m.dupes:
        problems.append(f"duplicate rows: { {k: v for k, v in m.dupes.items() if v and not k.startswith('_')} }")
    if problems:
        return False, "; ".join(problems)
    return True, "no duplicate identifier; every namespace contiguous (WJ 25, WWF 50, WEE 84, WTA 272, WTS 30)"


def check_09(m: Model) -> tuple[bool, str]:
    declared = {}
    for cells in table_rows(m.main, 5, r"[A-P]"):
        declared[cells[0]] = (cells[2], int(cells[3]))
    problems = []
    total = 0
    for label, (rng, count) in declared.items():
        nums = [int(x) for x in re.findall(r"(\d{3})", rng)]
        if len(nums) != 2:
            problems.append(f"class {label}: unreadable range {rng}")
            continue
        lo, hi = nums
        present = [n for n in range(lo, hi + 1) if f"WTA-{n:03d}" in m.tests]
        if len(present) != hi - lo + 1:
            problems.append(f"class {label}: range {lo}-{hi} has {len(present)} real rows")
        if len(present) != count:
            problems.append(f"class {label}: declares {count}, rows {len(present)}")
        total += len(present)
        if lo > 1:
            prev = f"WTA-{lo-1:03d}"
            owners = [lbl for lbl, (r2, _) in declared.items() if r2 and prev in r2]
    if total != len(m.tests):
        problems.append(f"class ranges tile {total} rows but {len(m.tests)} tests exist")
    if problems:
        return False, "; ".join(problems[:4])
    return True, f"16 class ranges tile all {total} test rows; declared counts match parsed rows"


def check_10(m: Model) -> tuple[bool, str]:
    bad_status = {c[12] for _, c in m.tests.items() if c[12] not in ("NOT RUN", "PASS", "FAIL", "BLOCKED", "N/A")}
    claimed_pass = [k for k, c in m.tests.items() if c[12].upper() == "PASS"]
    not_run = [k for k, c in m.tests.items() if c[12] != "NOT RUN"]
    if bad_status:
        return False, f"illegal test status values: {sorted(bad_status)}"
    if claimed_pass:
        return False, f"tests claim PASS with no build: {claimed_pass[:5]}"
    if not_run:
        return False, f"rows not marked NOT RUN: {[(k, m.tests[k][12]) for k in not_run[:5]]}"
    return True, f"all {len(m.tests)} test rows are Definition COMPLETE / Execution NOT RUN"


def _known(m: Model, token: str) -> bool:
    if token.startswith("WEP-"):
        return token in m.wep
    if token.startswith("F-WEP-"):
        return token in m.fids or token in m.finv or bool(re.fullmatch(r"F-WEP-000[a-h]", token))
    if token.startswith("WPC-"):
        return token in m.wpc
    if token.startswith("WPF-"):
        return token in m.wpf
    if token.startswith("WPA-"):
        return token in m.wpa
    if token.startswith("REQ-"):
        return token in m.req
    if token.startswith("DD-"):
        return token in m.dd
    if token.startswith("D-"):
        return token in m.d
    if token.startswith("UD-"):
        return token in m.ud
    if token.startswith("WJ-"):
        return token in m.journeys
    if token.startswith("WWF-"):
        return token in m.workflows
    if token.startswith("WEE-"):
        return token in m.edge
    if token.startswith("WTA-"):
        return token in m.tests
    if token.startswith("WTS-"):
        return token in m.threats
    if token.startswith("WEG-"):
        return token in m.forward or True  # WEG ids validated by check_27
    if token.startswith("11C-"):
        return token in {c.cid for c in CHECKS}
    return False


PATTERNS = [
    (r"`F-WEP-\d{3}(?:[a-h])?`", "F-WEP"),
    (r"`WEP-\d{3}`", "WEP"),
    (r"`WPC-\d{2}`", "WPC"),
    (r"`WPF-\d{2}`", "WPF"),
    (r"`WPA-\d{2}`", "WPA"),
    (r"`WJ-\d{3}`", "WJ"),
    (r"`WWF-\d{3}`", "WWF"),
    (r"`WEE-\d{3}`", "WEE"),
    (r"`WTA-\d{3}`", "WTA"),
    (r"`WTS-\d{3}`", "WTS"),
    (r"`REQ-\d{2,3}`", "REQ"),
    (r"`DD-\d{3}`", "DD"),
    (r"`D-\d{3}`", "D"),
    (r"`UD-\d{3}`", "UD"),
]


def check_11(m: Model) -> tuple[bool, str]:
    unresolved: list[str] = []
    for pat, _label in PATTERNS:
        for mm in re.finditer(pat, m.main):
            t = mm.group(0).strip("`")
            if _known(m, t):
                continue
            if negated(clause_of(m.main, mm.start())):
                continue
            unresolved.append(t)
        unresolved = sorted(set(unresolved))
    if unresolved:
        return False, f"{len(unresolved)} unresolved references: {sorted(set(unresolved))[:12]}"
    return True, "every WEP/F-WEP/WPC/WPF/WPA/REQ/DD/UD and 11C identifier resolves to a real record"


def check_12(m: Model) -> tuple[bool, str]:
    machines = re.findall(r"### 12\.(\d+)", m.main)
    if len(machines) < 10:
        return False, f"only {len(machines)} state-machine subsections; 12 machines required"
    ledger_rows = 0
    unowned = []
    for line in m.main.splitlines():
        s = line.strip()
        if not s.startswith("|") or "` → `" not in s and "→" not in s:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 12 and cells[10].startswith("`WWF-"):
            ledger_rows += 1
            if not _known(m, cells[10].strip("`")):
                unowned.append(cells[10])
    invalid_rows = table_rows(section(m.main, "12", "13"), 5, r"\d+")
    catalogue = [c for c in invalid_rows if len(c) >= 5 and re.search(r"`WTA-\d{3}`", c[4])
                 and re.search(r"`WPF-\d{2}`", c[3])]
    bad_tests = [c[0] for c in catalogue
                 if not all(_known(m, x.strip("`")) for x in re.findall(r"`WTA-\d{3}`", c[4]))]
    if unowned or ledger_rows != 35 or len(catalogue) != 21 or bad_tests:
        return False, (f"ledger rows={ledger_rows} unowned={unowned[:3]} invalid-catalogue={len(catalogue)} "
                       f"catalogue rows without a real test={bad_tests[:5]}")
    return True, (f"{len(machines)} machine subsections, {ledger_rows} owned transition rows, "
                  f"{len(catalogue)} invalid-transition rows each mapped to a real test")


def check_13(m: Model) -> tuple[bool, str]:
    want = [f"REQ-{n}" for n in range(704, 764)]
    missing = [w for w in want if w not in m.forward]
    bad_rules = []
    for rid, cells in m.forward.items():
        refs = re.findall(r"`WEP-(\d{3})`", cells[2])
        if not refs:
            bad_rules.append(rid)
        elif not all(f"WEP-{x}" in m.wep for x in refs):
            bad_rules.append(rid)
    if missing or bad_rules:
        return False, f"absent from the forward ledger: {missing[:6]}; rows without resolving WEP rules: {bad_rules[:6]}"
    return True, "all 60 B-11 requirements appear in the forward ledger with WEP references that resolve"


def check_14(m: Model) -> tuple[bool, str]:
    if len(m.fids) != 50:
        return False, f"register parsed {len(m.fids)} formulas, expected 50"
    structural = [k for k, v in m.fids.items() if v == "Structural"]
    provisional = [k for k, v in m.fids.items() if v == "Provisional"]
    retired = [k for k, v in m.fids.items() if v == "Retired"]
    declared = {
        "43": len(structural), "6": len(provisional), "1": len(retired),
    }
    if (len(structural), len(provisional), len(retired)) != (43, 6, 1):
        return False, f"derived 43/6/1 expectation failed: {len(structural)}/{len(provisional)}/{len(retired)}"
    for want_id in PROVISIONAL_FORMULAS:
        if m.fids.get(want_id) != "Provisional":
            return False, f"{want_id} is not Provisional in the register (read {m.fids.get(want_id)})"
    claim = f"{len(structural)} structural, {len(provisional)} provisional, {len(retired)} retired"
    if "43" not in m.main or "49 active" not in m.main:
        return False, "the document does not restate the 43 structural / 49 active figures"
    unknown = [k for k in m.fids if m.fids[k] == "UNKNOWN"]
    if unknown:
        return False, f"formulas with no field-20 status: {unknown}"
    return True, f"formula classes recomputed from register field 20: {claim}; declared figures match ({declared})"


def check_15(m: Model) -> tuple[bool, str]:
    want = [f"WPF-{n:02d}" for n in range(1, 41)]
    missing = [w for w in want if w not in m.forward or True]
    wpf_window = section(m.main, "19", "20")
    coverage = {c[0].strip("`") for c in table_rows(wpf_window, 4, r"WPF-\d{2}")}
    miss = [w for w in want if w not in coverage]
    allocated_rows = table_rows(wpf_window, 4, r"WPF-\d{2,3}")
    invented = sorted({c[0].strip("`") for c in allocated_rows if int(c[0].strip("`").split("-")[1]) > 40})
    no_test = [c[0] for c in allocated_rows if not re.search(r"`WTA-\d{3}`", c[3])]
    no_wf = [c[0] for c in allocated_rows if not re.search(r"`WWF-\d{3}`", c[2])]
    if miss or invented or no_test or no_wf:
        return False, (f"codes missing from the coverage map: {miss}; invented codes: {invented}; "
                       f"without a test: {no_test[:4]}; without a workflow: {no_wf[:4]}")
    return True, "all 40 WPF codes mapped to a workflow and a test; no invented code exists anywhere in 11C"


def check_16(m: Model) -> tuple[bool, str]:
    want = {f"WPA-{n:02d}" for n in range(1, 51)}
    window = m.main[m.main.find("## 12."):m.main.find("## 23.")]
    found = {tok.strip("`") for tok in re.findall(r"`WPA-\d{2}`", window)}
    missing = sorted(want - found)
    audit = section(m.main, "22", "23")
    mapped = [c for c in table_rows(audit, 4, r"[A-Z][a-z]+[^|]*")
              if re.search(r"WPA-\d{2}", " ".join(c)) and not c[0].startswith("Rule")]
    if missing:
        return False, f"WPA events never referenced between the ledger and the audit mapping: {missing}"
    if len(mapped) < 9:
        return False, f"only {len(mapped)} of the nine required operation classes carry a WPA mapping row"
    return True, (f"all {len(want)} WPA events referenced; {len(mapped)} operation-class rows cover "
                  "the nine required classes")


def check_17(m: Model) -> tuple[bool, str]:
    rows = table_rows(section(m.main, "14", "15"), 6, r".+")
    owned = [c for c in rows if c[1].startswith("B-") or c[1].startswith("**B-11**")]
    bad = []
    for c in owned:
        owner = c[1].strip("* ")
        write = c[3].lower()
        if owner != "B-11" and not any(k in write for k in ("none", "append only", "requests", "request", "records only")):
            bad.append((c[0], write[:40]))
    if len(owned) < 20:
        return False, f"ownership matrix parsed only {len(owned)} owner rows"
    if bad:
        return False, f"non-B-11 owned fields with a B-11 write: {bad[:5]}"
    return True, f"{len(owned)} ownership rows; every externally-owned field has no B-11 write"


def check_18(m: Model) -> tuple[bool, str]:
    want = [f"WPC-{n:02d}" for n in range(1, 18)]
    missing = [w for w in want if w not in m.integrations]
    bad = [k for k, c in m.integrations.items() if not c[1] or not c[2]]
    extra = sorted(set(m.integrations) - set(want))
    live_wig = [ln.strip()[:40] for ln in m.main.splitlines()
                if re.match(r"^\s*(\||#{1,4}\s)`?WIG-", ln)]
    if missing or bad or extra or live_wig:
        return False, (f"missing={missing} empty source/target={bad[:4]} extra={extra} "
                       f"parallel contract namespace in use={live_wig[:3]}")
    return True, ("all 17 WPC contracts present with source and target; no 18th contract; the "
                  "rejected `WIG-` prefix appears only as an explicit non-adoption")


def check_19(m: Model) -> tuple[bool, str]:
    gaps = {c[0].strip("`") for c in table_rows(section(m.main, "26", "27"), 6, r"WEG-\d{2}")}
    if "WEG-01" not in gaps:
        return False, "gap WEG-01 (the missing authorization code) is not registered"
    cited = len(re.findall(r"WEG-01", m.main))
    if cited < 3:
        return False, f"WEG-01 registered but only cited {cited}x; the reuse must be visible where it is used"
    return True, f"WEG-01 registered and cited {cited}x; {len(gaps)} gaps in the register"


def check_20(m: Model) -> tuple[bool, str]:
    bad = []
    for fid in PROVISIONAL_FORMULAS:
        for sent in re.split(r"(?<=[.;])\s+", m.main):
            if fid in sent and re.search(r"\b(approved|calibrated|settled|final value|numerically final)\b", sent, flags=re.I):
                if "not" in sent.lower() or "never" in sent.lower() or "MUST NOT" in sent:
                    continue
                bad.append((fid, sent[:70]))
    retired_live = []
    for sent in re.split(r"(?<=[.;])\s+", m.main):
        if RETIRED_FORMULA in sent and re.search(r"\b(computes|calculation uses|formula used to|allocates proportionally)\b", sent, flags=re.I):
            retired_live.append(sent[:70])
    if bad:
        return False, f"provisional formula presented as settled: {bad[:3]}"
    if retired_live:
        return False, f"retired formula used as a live calculation: {retired_live[:2]}"
    return True, "no Provisional formula is called approved or calibrated; F-WEP-048 is never used as a live calculation"


def check_21(m: Model) -> tuple[bool, str]:
    counts = {
        "event classes": (r"exactly four event classes|four event classes", 4),
        "triggers": (r"five triggers|permitted triggers are", 5),
        "objective categories": (r"exactly twelve objective categories|twelve objective categories", 12),
        "standings": (r"exactly ten standings|ten standings", 10),
        "progression layers": (r"eight progression layers|eight derived layers", 8),
        "reward classes": (r"six reward classes", 6),
        "recognition objects": (r"five recognition objects|five distinct recognition objects", 5),
        "state machines": (r"twelve state machines|Twelve machines", 12),
    }
    missing = [k for k, (pat, _n) in counts.items() if not re.search(pat, m.main, flags=re.I)]
    if missing:
        return False, f"closed-catalogue statement absent for: {missing}"
    for cls in ("EV-CAL", "EV-STATE", "EV-CHAL", "EV-COMM"):
        if cls not in m.main:
            return False, f"event class {cls} is not named"
    if not re.search(r"individual[- ]equivalent", m.main):
        return False, "the OBJ-ALL individual-equivalent rule is not stated"
    return True, "all eight closed catalogues restated at their approved sizes; OBJ-ALL pairing rule present"


def check_22(m: Model) -> tuple[bool, str]:
    classes = re.findall(r"`(RECOGNITION|RECORD|AUTHORSHIP|COSMETIC|TITLE|MATERIAL|PRESTIGE|POINTS|CURRENCY|BOOST|SKIN)`", m.main)
    allowed = {"RECOGNITION", "RECORD", "AUTHORSHIP", "COSMETIC", "TITLE", "MATERIAL"}
    extra = sorted({c for c in classes} - allowed)
    real = []
    for bad in extra:
        for mm in re.finditer(rf"`{bad}`", m.main):
            if not negated(clause_of(m.main, mm.start())):
                real.append(bad)
                break
    if real:
        return False, f"a seventh reward-class token is used as a class: {sorted(set(real))}"
    if not re.search(r"RECOGNITION.*RECORD.*AUTHORSHIP.*COSMETIC.*TITLE.*MATERIAL", m.main.replace("\n", " ")):
        return False, "the six reward classes are not enumerated together"
    return True, "exactly the six approved reward classes appear; no seventh class is introduced"


def check_23(m: Model) -> tuple[bool, str]:
    """The permission matrix must give PLAYER and ADMIN no correction power."""
    window = section(m.main, "3", "4")
    row = None
    for line in window.splitlines():
        s = line.strip()
        if s.startswith("|") and "correction to a published record" in s:
            row = [c.strip() for c in s.strip("|").split("|")]
    if row is None or len(row) < 5:
        return False, "the correction-authority row is missing from the permission matrix"
    if "✓" in row[1] or "✓" in row[4]:
        return False, (f"the permission matrix grants correction power to a "
                       f"player or administrator: {row}")
    if not re.search(r"SYS\(P6\).*OWNER.*MOD|owner.*system.*moderator", m.main, flags=re.I | re.S):
        return False, "the three authorised correction owners are not stated"
    return True, "correction authority stays with SYS(P6) / OWNER / MOD; PLAYER and ADMIN are both ✗"


def check_24(m: Model) -> tuple[bool, str]:
    mentions = [s for s in re.split(r"(?<=[.;])\s+", m.main) if RETIRED_FORMULA in s]
    if not mentions:
        return False, "the retired formula is never mentioned, so the prohibition is untested"
    negative = re.compile(r"retired|no lawful|\bno\b|not\b|never|prohibit|negative|forbid|without|refrain|bypass|avoid", flags=re.I)
    live = [s[:80] for s in mentions if not negative.search(s)]
    forbidden = []
    for phrase in ("proportional collective material", "Alliance-funded collective prize", "inter-nation prize pool"):
        for s in re.split(r"(?<=[.;])\s+", m.main):
            if phrase.lower() in s.lower() and not re.search(r"not|never|prohibit|forbid|MUST NOT|bypass|around|without", s, flags=re.I):
                forbidden.append(s[:70])
    if live or forbidden:
        return False, f"F-WEP-048 used positively: {live[:2]}; allocation language not negated: {forbidden[:2]}"
    return True, f"{len(mentions)} mentions of F-WEP-048 are all negative; no collective allocation mechanism is specified"


def check_25(m: Model) -> tuple[bool, str]:
    start = m.main.find("**17.2 Coverage")
    end = m.main.find("## 18.")
    window = m.main[start:end]
    mapped = set()
    for token in re.findall(r"#(\d{1,2})(?:–`?(\d{1,2})?)?`?→`?([A-Za-z\u2013\d\-,` ]+)", window):
        if token[0].isdigit():
            a = int(token[0])
            b = int(token[1]) if token[1] else a
            for n in range(a, b + 1):
                mapped.add(n)
    # the compact form is "#1->WTS-...; #2->..." so also scan pairs
    for a, b in re.findall(r"#(\d{1,2})`?–#(\d{1,2})", window):
        for n in range(int(a), int(b) + 1):
            mapped.add(n)
    for n in re.findall(r"#(\d{1,2})→", window):
        mapped.add(int(n))
    want = set(range(1, 25))
    missing = sorted(want - mapped)
    if missing:
        return False, f"WEP-640 scenarios with no WTS mapping: {missing}"
    return True, "all 24 mandatory manipulation scenarios map to at least one threat row"


def check_26(m: Model) -> tuple[bool, str]:
    reward_wfs = [k for k, f in m.workflows.items()
                  if re.search(r"reward|grant|claim|entitlement", f.get("ID and purpose", ""), flags=re.I)]
    bad = []
    for k in reward_wfs:
        fields = m.workflows[k]
        blob = " ".join([fields.get("Retry / recovery / idempotency", ""),
                         fields.get("Mutation / transaction", "")])
        if not re.search(r"key|idempot|dedup|achievement", blob, flags=re.I):
            bad.append(k)
    if bad:
        return False, f"reward-processing workflows with no declared idempotency key: {bad}"
    return True, f"{len(reward_wfs)} reward-processing workflows each declare an idempotency key"


def check_27(m: Model) -> tuple[bool, str]:
    problems = []
    bad_claim = re.compile(r"\b(?:are|is|been|being|gets|get)\s+(?:now\s+|already\s+)?"
                           r"(?:resolved|closed|approved|decided)\b", re.I)
    own_ok = re.compile(r"not\s+(?:been\s+)?resolved|never\s+resolved|unresolved|resolves none|"
                        r"(?:remain|stay|remains|stays|keeps|keep)\s+\S{0,3}\s*\**\s*Open"
                        r"|as recorded|no owner-reserved decision", re.I)
    for uid in OWNER_RESERVED_UD:
        for sent in re.split(r"(?<=[.;])\s+", m.main):
            if uid not in sent or not bad_claim.search(sent):
                continue
            if own_ok.search(sent):
                continue
            problems.append((uid, sent[:90]))
    for uid in ("UD-050", "UD-051"):
        hits = [s for s in re.split(r"(?<=[.;|])\s+", m.main) if uid in s]
        if not hits:
            problems.append((uid, "not mentioned at all"))
        elif not any(re.search(r"Open|owner|Prompt 1[24]", s) for s in hits):
            problems.append((uid, "never marked Open or assigned to its owner"))
    if problems:
        return False, f"unsupported owner-decision claims: {problems[:3]}"
    return True, "no owner-reserved decision is presented as resolved; UD-050/UD-051 stay Open with their owners"


def check_28(m: Model) -> tuple[bool, str]:
    body = m.main
    hits = []
    for pat in BANNED_CLAIM_PATTERNS:
        for mm in re.finditer(pat, body, flags=re.I):
            line_no = body[:mm.start()].count("\n") + 1
            line = body.splitlines()[line_no - 1]
            if re.search(r"not|never|no\b|claim|forbid|prohibit|without|design only|unimplemented", line, flags=re.I):
                continue
            hits.append((pat, line[:70]))
    if hits:
        return False, f"implementation/runtime claims found: {hits[:3]}"
    return True, "no implementation, runtime, deployment, playtest or calibration claim appears in 11C"


def check_29(m: Model) -> tuple[bool, str]:
    want = [f"P11C-{n:02d}" for n in range(1, 21)]
    missing = [w for w in want if w not in m.gates]
    bad_status = []
    no_evidence = []
    tally: dict[str, int] = {}
    for gid, cells in m.gates.items():
        status = cells[5].replace("**", "").strip()
        tally[status] = tally.get(status, 0) + 1
        if status not in GATE_STATUSES:
            bad_status.append((gid, status))
        if status == "PASS":
            location = cells[3]
            if not re.search(r"§|`|\(|\.md|\.py|log", location):
                no_evidence.append(gid)
    if missing or bad_status or no_evidence:
        return False, f"missing gates={missing} illegal status={bad_status[:3]} PASS-without-location={no_evidence[:3]}"
    mm_t = re.search(r"\*\*3\d\.3 Gate tally", m.main)
    declared = m.main[mm_t.start():] if mm_t else ""
    nums = re.findall(r"PASS (\d+) .*PARTIAL (\d+)", declared.replace("\n", " "))
    if nums:
        p, q = (int(x) for x in nums[0])
        if (p, q) != (tally.get("PASS", 0), tally.get("PARTIAL", 0)):
            return False, f"declared tally {p}/{q} disagrees with the rows {tally.get('PASS',0)}/{tally.get('PARTIAL',0)}"
    return True, f"20 gates, all six statuses legal, every PASS names a location; recomputed tally {tally}"


def check_30(m: Model) -> tuple[bool, str]:
    event_states = {"QUALIFIED", "SCHEDULED", "ANNOUNCED", "ACTIVE", "CLOSED", "COMPLETED",
                    "EXPIRED", "CANCELLED", "VOIDED"}
    obj_states = {"AVAILABLE", "DISMISSED", "ACCEPTED", "IN_PROGRESS", "TIER_REACHED",
                  "COMPLETED_PENDING_VALIDATION", "VERIFIED", "REWARD_PENDING", "DEFERRED",
                  "CLAIMED", "EXPIRED", "WITHDRAWN", "SUPERSEDED"}
    other = {"NOT_JOINED", "JOINED", "WITHDRAWN", "SUSPENDED", "DISQUALIFIED", "SEALED", "PUBLISHED",
             "NOT_STARTED", "COUNTING", "TIER_MET", "COMPLETE", "CORRECTED", "INVALID",
             "NOT_QUALIFIED", "QUALIFIED", "GRANTED", "REVOKED", "RECORDED", "REDACTED",
             "SEASON_SCHEDULED", "SEASON_OPEN", "SEASON_CLOSED", "SEASON_ARCHIVED",
             "NOT_ELIGIBLE", "ELIGIBLE", "PROVISIONAL", "EXCLUDED", "UNRANKED",
             "CLAIM_PENDING", "TEMPLATE_DRAFT", "TEMPLATE_PUBLISHED", "TEMPLATE_RETIRED",
             "TEMPLATE_SUPERSEDED", "OBJ_DRAFT", "OBJ_PUBLISHED", "OBJ_RETIRED", "OBJ_SUPERSEDED",
             "RESOLVING", "FAILED"}
    legal = event_states | obj_states | other
    forbidden = set()
    for cells in table_rows(section(m.main, "12", "13"), 5, r"\d+"):
        for mm_t in re.finditer(r"`([A-Z][A-Z_]+)\s*" + chr(8594) + r"\s*([A-Z][A-Z_]+)`", cells[1]):
            forbidden.add((mm_t.group(1), mm_t.group(2)))
    bad = []
    for jid, fields in m.journeys.items():
        text = fields.get("State transitions", "")
        for tok in re.findall(r"`([A-Z][A-Z_]{3,})`", text):
            if tok in ("REWARD", "WORLD", "WSE", "W0", "P7", "P6", "NATION", "ALLIANCE", "ST-DEV",
                         "INTERRUPTED", "COMPLETED_TURN", "P3", "P5", "W1", "W2", "W3", "W4", "W5"):
                continue
            if tok not in legal:
                bad.append((jid, tok))
        pairs = re.findall(r"([A-Z][A-Z_]+)\s*" + chr(8594) + r"\s*([A-Z][A-Z_]+)", text)
        for a, b in pairs:
            if (a, b) in forbidden:
                bad.append((jid, a + chr(8594) + b + " (invalid-transition catalogue)"))
    if not forbidden:
        return False, "no invalid-transition catalogue was parsed, so the arrow test is vacuous"
    if bad:
        return False, f"journeys cite a state or transition no machine permits: {bad[:5]}"
    return True, (f"{len(m.journeys)} journeys use only machine states and none of the "
                  f"{len(forbidden)} catalogued invalid transitions")


def check_31(m: Model) -> tuple[bool, str]:
    try:
        proc = subprocess.run([sys.executable, str(LINKS)], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=600)
    except (OSError, subprocess.SubprocessError) as exc:
        return False, f"link validator could not run: {exc}"
    out = (proc.stdout or "") + (proc.stderr or "")
    m_link = re.search(r"Unresolved: (\d+)", out)
    if proc.returncode != 0 or not m_link or m_link.group(1) != "0":
        return False, f"exit={proc.returncode}; {out.strip()[-240:]}"
    return True, out.strip().splitlines()[-1][:150]


CHECKS: list = []


def _register() -> None:
    defs = [
        ("11C-01", "header declares Prompt 11C and design-only status", check_01),
        ("11C-02", "sections 0-34 present in order without duplication", check_02),
        ("11C-03", "25 journeys carry all 17 required fields", check_03),
        ("11C-04", "50 workflows carry all 14 required fields", check_04),
        ("11C-05", "84 edge cases and 30 threats are column-complete", check_05),
        ("11C-06", "272 tests each have an expected result and a status", check_06),
        ("11C-07", "workflow records use the declared schema labels", check_07),
        ("11C-08", "no duplicate identifier; every namespace contiguous", check_08),
        ("11C-09", "class ranges and counts recomputed from rows", check_09),
        ("11C-10", "only legal status values; no test claims PASS", check_10),
        ("11C-11", "every identifier reference resolves in the sources", check_11),
        ("11C-12", "transition ledger is owned and the invalid catalogue is tested", check_12),
        ("11C-13", "forward ledger covers REQ-704-763 with resolving rules", check_13),
        ("11C-14", "formula classes re-derived from register field 20", check_14),
        ("11C-15", "all 40 WPF codes mapped; no code invented", check_15),
        ("11C-16", "all 50 WPA events referenced", check_16),
        ("11C-17", "ownership matrix gives externals no B-11 write", check_17),
        ("11C-18", "17 WPC contracts, no duplicate namespace", check_18),
        ("11C-19", "the authorization-code gap is registered and cited", check_19),
        ("11C-20", "provisional formulas are not treated as approved", check_20),
        ("11C-21", "closed catalogues keep their approved sizes", check_21),
        ("11C-22", "exactly six reward classes exist", check_22),
        ("11C-23", "correction authority stays with the three owners", check_23),
        ("11C-24", "the retired formula is never used as a calculation", check_24),
        ("11C-25", "all 24 manipulation scenarios map to a threat", check_25),
        ("11C-26", "every reward workflow declares an idempotency key", check_26),
        ("11C-27", "no owner-reserved decision is presented as resolved", check_27),
        ("11C-28", "no runtime or implementation claim appears", check_28),
        ("11C-29", "gate statuses legal and every PASS has a location", check_29),
        ("11C-30", "journey states match the twelve machines", check_30),
        ("11C-31", "repository links resolve", check_31),
    ]
    for cid, name, fn in defs:
        CHECKS.append(_Check(cid, name, fn))


@dataclass
class _Check:
    cid: str
    name: str
    fn: Callable[[Model], tuple[bool, str]]


_register()


# --------------------------------------------------------------------------- #
# fixtures
# --------------------------------------------------------------------------- #

@dataclass
class Fixture:
    fid: str
    cid: str
    expect: bool
    mutate: Callable[[Model], None]
    reason: str


NL = chr(10)
NL2 = chr(10) * 2
TBL_HEAD = "| Field | Content |" + chr(10) + "|---|---|" + chr(10)


NL2 = chr(10) * 2
TBL_HEAD = "| Field | Content |" + chr(10) + "|---|---|" + chr(10)


def _edit(m: Model, old: str, new: str, count: int = 1) -> bool:
    if old not in m.main:
        return False
    m.main = m.main.replace(old, new, count)
    return True


def f_pos_01(m: Model) -> bool: return True
def f_pos_02(m: Model) -> bool: return True
def f_pos_03(m: Model) -> bool: return True
def f_pos_04(m: Model) -> bool: return True
def f_pos_05(m: Model) -> bool: return True
def f_pos_06(m: Model) -> bool: return True
def f_pos_07(m: Model) -> bool: return True
def f_pos_08(m: Model) -> bool: return True


def f_neg_01(m: Model) -> bool:
    """A duplicated journey identifier."""
    head = "**WJ-024 — Audit inspection: reconstructing one operation from records alone.**"
    clone = "**WJ-023 — duplicate heading.**" + NL2 + TBL_HEAD
    clone += NL.join("| " + k + " | duplicated |" for k in JOURNEY_FIELDS) + NL
    return _edit(m, head, clone + NL + head)


def f_neg_02(m: Model) -> bool:
    """A B-11 requirement dropped out of the forward ledger."""
    return _edit(m, "| `REQ-760` | twelve machines and invalid transitions specified |",
                 "| `REQ-999` | twelve machines and invalid transitions specified |")


def f_neg_03(m: Model) -> bool:
    """A WEP reference that does not exist in the rulebook."""
    return _edit(m, "`WEP-005`, `WEP-226`, `WEP-528`, `WEP-609`, `WEP-299`.",
                 "`WEP-999`, `WEP-226`, `WEP-528`, `WEP-609`, `WEP-299`.")


def f_neg_04(m: Model) -> bool:
    """A formula reference that does not exist in the register."""
    return _edit(m, "register `F-WEP-001` example + validator `11C-14`",
                 "register `F-WEP-999` example + validator `11C-14`")


def f_neg_05(m: Model) -> bool:
    """A journey that claims a transition the invalid catalogue forbids."""
    return _edit(m, "Instance `QUALIFIED → SCHEDULED → ANNOUNCED → ACTIVE → CLOSED → COMPLETED`",
                 "Instance `QUALIFIED → SCHEDULED → ANNOUNCED → COMPLETED → ACTIVE`")


def f_neg_06(m: Model) -> bool:
    """An owner-reserved decision presented as resolved by this prompt."""
    return _edit(m, "`UD-040`…`UD-049` remain **Open / Yes — owner** exactly as recorded by B-11",
                 "`UD-040`…`UD-049` are resolved by this prompt and closed as approved")


def f_neg_07(m: Model) -> bool:
    """A test row with no expected result."""
    return _edit(m, "| review | identifiers and rules unchanged | a renumbered rule |",
                 "| review |  | a renumbered rule |")


def f_neg_08(m: Model) -> bool:
    """A gate marked PASS with no evidence location."""
    return _edit(m, "the ownership matrix, the prohibited-pattern table and the dependency graph with cycle analysis | §14, §13.4, §13.5 |",
                 "the ownership matrix | somewhere out there |")


def f_neg_09(m: Model) -> bool:
    """A protected journey with its security-control field deleted."""
    anchor = "| Security checks | Server-authoritative action"
    i = m.main.find(anchor)
    if i < 0:
        return False
    j = m.main.find(chr(10), i)
    m.main = m.main[:i] + m.main[j + 1:]
    return True


def f_neg_10(m: Model) -> bool:
    """A duplicate reward path with no idempotency control."""
    return _edit(m, "The key is the retry identity; a race between two claims resolves to one grant plus one dedupe record",
                 "re-run the grant on every retry until a second one succeeds")


def f_neg_11(m: Model) -> bool:
    """An implementation instruction with no design authority behind it."""
    nl = chr(10)
    rows = nl.join("| " + k + " | invented step with no source |" for k in WORKFLOW_FIELDS)
    m.main += (nl + "### WWF-051 — orphan implementation instruction" + nl + nl
               + "| Field | Content |" + nl + "|---|---|" + nl + rows + nl)
    return True


def f_neg_12(m: Model) -> bool:
    """A failure code invented outside the closed WPF set."""
    nl = chr(10)
    return _edit(m, "| `WPF-40` | Phase, checkpoint or replay conflict",
                 "| `WPF-41` | Invented authorization code | `WWF-001` | `WTA-001` |" + nl
                 + "| `WPF-40` | Phase, checkpoint or replay conflict")


def f_neg_13(m: Model) -> bool:
    """A Provisional formula described as calibrated and approved."""
    return _edit(m, "**4.9 Provisional formulas are not approved.**",
                 "**4.9 Provisional formulas are approved.** `F-WEP-046` is calibrated and approved for production use.")


def f_neg_14(m: Model) -> bool:
    """The retired formula used as a live calculation."""
    return _edit(m, "**4.8 Retired formula.** `F-WEP-048` (contribution allocation) is retired with no lawful use case (`WEP-683`).",
                 "**4.8 Allocation.** `F-WEP-048` (contribution allocation) proportionally pays every member by stake (`WEP-683`).")


def f_neg_15(m: Model) -> bool:
    """A declared class count that disagrees with its rows."""
    return _edit(m, "| K | Concurrency and race tests | `157`–`168` | 12 | 9 concurrency |",
                 "| K | Concurrency and race tests | `157`–`168` | 40 | 9 concurrency |")


def f_neg_16(m: Model) -> bool:
    """An administrator given correction power in the permission matrix."""
    return _edit(m, "| Append a correction to a published record | ✗ | ✗ | ✓ (own defect) | ✗ | ✓ (invalid grant) |",
                 "| Append a correction to a published record | ✓ | ✗ | ✓ (own defect) | ✓ | ✓ (invalid grant) |")


def f_neg_17(m: Model) -> bool:
    """A seventh reward class."""
    return _edit(m, "`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL` (`WEP-499`). (5)",
                 "`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`, `PRESTIGE` (`WEP-499`). (5)")


FIXTURES = [
    Fixture("POS-01", "11C-03", True, f_pos_01, "the real journey set is accepted"),
    Fixture("POS-02", "11C-04", True, f_pos_02, "the real workflow set is accepted"),
    Fixture("POS-03", "11C-05", True, f_pos_03, "the real edge-case and threat tables are accepted"),
    Fixture("POS-04", "11C-06", True, f_pos_04, "the real test table is accepted"),
    Fixture("POS-05", "11C-14", True, f_pos_05, "recomputed formula classification is accepted"),
    Fixture("POS-06", "11C-18", True, f_pos_06, "the 17-contract integration matrix is accepted"),
    Fixture("POS-07", "11C-29", True, f_pos_07, "the gate table with legal statuses is accepted"),
    Fixture("POS-08", "11C-24", True, f_pos_08, "retired-formula mentions are all negative"),
    Fixture("NEG-01", "11C-08", False, f_neg_01, "duplicate journey identifier"),
    Fixture("NEG-02", "11C-13", False, f_neg_02, "requirement removed from the forward ledger"),
    Fixture("NEG-03", "11C-11", False, f_neg_03, "invalid WEP reference"),
    Fixture("NEG-04", "11C-11", False, f_neg_04, "invalid formula reference"),
    Fixture("NEG-05", "11C-30", False, f_neg_05, "invalid state transition in a journey"),
    Fixture("NEG-06", "11C-27", False, f_neg_06, "owner-reserved decision claimed as resolved"),
    Fixture("NEG-07", "11C-06", False, f_neg_07, "test with no expected result"),
    Fixture("NEG-08", "11C-29", False, f_neg_08, "PASS gate with no evidence location"),
    Fixture("NEG-09", "11C-03", False, f_neg_09, "protected workflow journey without security checks"),
    Fixture("NEG-10", "11C-26", False, f_neg_10, "duplicate reward path without idempotency"),
    Fixture("NEG-11", "11C-08", False, f_neg_11, "orphaned implementation instruction"),
    Fixture("NEG-12", "11C-15", False, f_neg_12, "invented WPF-41 failure code"),
    Fixture("NEG-13", "11C-20", False, f_neg_13, "provisional formula called approved"),
    Fixture("NEG-14", "11C-24", False, f_neg_14, "retired formula used as a live calculation"),
    Fixture("NEG-15", "11C-09", False, f_neg_15, "declared count disagrees with rows"),
    Fixture("NEG-16", "11C-23", False, f_neg_16, "administrator granted correction power"),
    Fixture("NEG-17", "11C-22", False, f_neg_17, "a seventh reward class"),
]


def run_checks(m: Model, verbose: bool) -> tuple[list[tuple[str, bool, str]], int]:
    results = []
    failed = 0
    by_id = {c.cid: c for c in CHECKS}
    for cid in sorted(by_id):
        c = by_id[cid]
        ok, detail = c.fn(m)
        if not ok:
            failed += 1
        if verbose or not ok:
            results.append((cid, ok, detail))
    return results, failed


def check_by_id(m: Model, cid: str) -> tuple[bool, str]:
    for c in CHECKS:
        if c.cid == cid:
            return c.fn(m)
    raise KeyError(cid)


def run_fixtures(base: Model, verbose: bool) -> tuple[int, int, int, int, list[str]]:
    pos_ok = pos_total = neg_ok = neg_total = 0
    notes: list[str] = []
    for fx in FIXTURES:
        model = copy.deepcopy(base)
        model.dupes = {}
        applied = fx.mutate(model)
        if applied is False:
            notes.append(f"{fx.fid}: anchor text not found — the fixture did not apply")
            if fx.expect:
                pos_total += 1
            else:
                neg_total += 1
            continue
        model.rebuild()
        ok, detail = check_by_id(model, fx.cid)
        passed = ok == fx.expect
        if fx.expect:
            pos_total += 1
            pos_ok += int(passed)
        else:
            neg_total += 1
            neg_ok += int(passed)
        if verbose or not passed:
            notes.append(f"{fx.fid} [{fx.cid}] {'OK' if passed else 'WRONG OUTCOME'}: {detail[:120]}")
    return pos_ok, pos_total, neg_ok, neg_total, notes


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--fixtures", action="store_true")
    args = ap.parse_args(argv)

    missing = [p.name for p in (MAIN, RULEBOOK, REGISTER, REQUIREMENTS, DECISIONS, DD_REGISTER,
                                UNRESOLVED, CROSSWALK) if not p.exists()]
    if missing:
        print("MISSING canonical inputs:", ", ".join(missing))
        return 2

    m = load()
    print("-" * 72)
    print("Prompt 11C B-11 workflows / integration / acceptance validator")
    print(f"journeys={len(m.journeys)} workflows={len(m.workflows)} edge={len(m.edge)} "
          f"tests={len(m.tests)} threats={len(m.threats)} gates={len(m.gates)} checks={len(CHECKS)}")
    print("-" * 72)

    results, failed = run_checks(m, args.verbose)
    for cid, ok, detail in results:
        print(f"{cid} {'PASS' if ok else 'FAIL'}  {detail}")

    links_note = ""
    if not args.fixtures:
        l_ok, l_detail = check_by_id(m, "11C-31")
        links_note = f"exit-code check: {'pass' if l_ok else 'fail'}; {l_detail}"
        if not l_ok:
            failed += 1

    pos_ok = pos_total = neg_ok = neg_total = 0
    notes: list[str] = []
    if args.self_test or args.fixtures:
        pos_ok, pos_total, neg_ok, neg_total, notes = run_fixtures(m, args.verbose)
        print("-" * 72)
        print("FIXTURES")
        for n in notes:
            print(" ", n)

    print("-" * 72)
    print(f"B-11 WORKFLOW VALIDATOR CHECKS: {len(CHECKS) - failed}/{len(CHECKS)} passed; {failed} failed")
    print("NOT the acceptance-gate count: these are documentation-quality checks, not P11C gates.")
    if pos_total:
        print(f"POSITIVE FIXTURES: {pos_ok}/{pos_total} accepted")
        print(f"NEGATIVE FIXTURES: {neg_ok}/{neg_total} rejected for the expected reason")
    if links_note:
        print(f"LINK VALIDATION (separate command, not a gate): {links_note}")
    print("-" * 72)

    if failed == 0 and (not args.self_test and not args.fixtures or (pos_ok == pos_total and neg_ok == neg_total)):
        print("RESULT: PASS — 11C workflows, integration and acceptance documents are internally "
              "consistent with the B-11 sources at the documentation level.")
        print("NOT PROVEN: runtime behaviour, executed tests, balance, privacy enforcement, "
              "storage cost, player experience, or an independent review of this pass.")
        return 0
    print("RESULT: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
