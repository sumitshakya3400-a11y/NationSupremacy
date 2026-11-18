#!/usr/bin/env python3
"""Prompt 14A — numerical-foundation validator (documentation quality only).

Checks the B-14 numerical foundation against the nine canonical formula
registers, B-03, B-02, the live roadmap, the Bible outline, the final
validator and the prompt archive. It reads the real files; it does not carry
hard-coded copies of their contents.

It is NOT a gameplay engine, a balance test, a simulation or a runtime test.
A passing result proves documentary consistency only.

Usage:
    python 14A_validate_numerical_foundation.py
    python 14A_validate_numerical_foundation.py --self-test

Run from docs/ (the default) or from anywhere; paths resolve from this file.
"""
import hashlib
import importlib.util
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))       # docs/
STAGE2 = os.path.join(BASE, "stage-2")
QA = os.path.join(BASE, "qa_backups")
PROMPTS = os.path.join(BASE, "prompts")
_CONTRACT_MODULE = None
_CONTRACT_REPORT = None


def _contract_module():
    global _CONTRACT_MODULE
    if _CONTRACT_MODULE is None:
        path = os.path.join(QA, "14A_contract_validator.py")
        spec = importlib.util.spec_from_file_location("contract_validator_14a", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _CONTRACT_MODULE = module
    return _CONTRACT_MODULE


def _contract_report():
    global _CONTRACT_REPORT
    if _CONTRACT_REPORT is None:
        _CONTRACT_REPORT = _contract_module().validate_production()
    return _CONTRACT_REPORT

REGISTERS = [
    ("B-04", "10_economic_formula_and_balance_register.md", "F-EC", 47),
    ("B-05", "11_city_infrastructure_production_and_research_formula_register.md", "F-CI", 41),
    ("B-06", "12_population_and_domestic_politics_formula_register.md", "F-PD", 44),
    ("B-07", "13_trade_and_markets_formula_register.md", "F-TM", 39),
    ("B-08", "15_diplomacy_formula_register.md", "F-DP", 12),
    ("B-09", "16_alliances_formula_register.md", "F-AL", 8),
    ("B-10", "17_warfare_formula_register.md", "F-WR", 39),
    ("B-11", "18_world_events_objectives_rankings_progression_formula_register.md", "F-WEP", 49),
    ("B-12", "20_fair_play_and_player_protection_formula_register.md", "F-FP", 16),
]
PREFIXES = [p for _, _, p, _ in REGISTERS]
EXPECTED_TOTAL = sum(n for *_, n in REGISTERS)

FILES = {
    "B-14": os.path.join(STAGE2, "22_formulas_and_balance.md"),
    "MASTER": os.path.join(STAGE2, "22_formula_master_inventory.md"),
    "PARAMS": os.path.join(STAGE2, "22_numerical_parameter_inventory.md"),
    "QA_REPORT": os.path.join(STAGE2, "22_numerical_baseline_qa_report.md"),
    "ROADMAP": os.path.join(STAGE2, "01_stage_2_prompt_roadmap.md"),
    "OUTLINE": os.path.join(STAGE2, "02_master_game_design_bible_outline.md"),
    "B03": os.path.join(STAGE2, "09_account_onboarding_nation_creation_and_progression.md"),
    "B02": os.path.join(STAGE2, "07_core_gameplay_loop_symbolic_world_and_turn_system.md"),
    "UD": os.path.join(STAGE2, "05_unresolved_design_decisions.md"),
    "DECISIONS": os.path.join(BASE, "DECISIONS.md"),
    "B04_AMENDMENTS": os.path.join(QA, "14A_b04_source_contract_amendments.json"),
    "VALIDATE_FINAL": os.path.join(QA, "validate_final.py"),
    "INDEX": os.path.join(PROMPTS, "INDEX.md"),
}
for system, fname, _, _ in REGISTERS:
    FILES["REG_" + system] = os.path.join(STAGE2, fname)

VALID_STATUSES = {"OWNER-APPROVED VALUE", "PROVISIONAL VALUE", "DESIGN PROPOSAL",
                  "NEEDS PLAYTESTING", "UNSPECIFIED", "RETIRED"}
OWNER_RESERVED_UD = ["UD-017", "UD-040", "UD-041", "UD-042", "UD-043", "UD-044", "UD-045",
                     "UD-046", "UD-047", "UD-048", "UD-049", "UD-050", "UD-051", "UD-052",
                     "UD-053", "UD-054", "UD-055", "UD-056", "UD-057", "UD-058", "UD-059", "UD-060"]

CONST_META = {
    "B-04": {
        "3.1": ("Applied at nation creation", "Prompt 14 calibration; B-04 structure owner"),
        "3.2": ("P3.3 extraction", "Prompt 14 calibration; B-04 structure owner"),
        "3.3": ("P3.5 processing", "Prompt 14 calibration; B-04 structure owner"),
        "3.4": ("P3.4 power generation", "Prompt 14 calibration; B-04 structure owner"),
        "3.5": ("Read at settlement; not a per-turn change", "Prompt 14 calibration; B-04 structure owner"),
    },
    "B-05": {
        "3.1": ("Submission and P4.1", "Prompt 14 calibration; B-05 structure owner"),
        "3.2": ("P4.1", "Prompt 14 calibration; B-05 structure owner"),
        "3.3": ("P4.1–P4.2", "Prompt 14 calibration; B-05 structure owner"),
        "3.4": ("Applied at nation creation", "Prompt 14 calibration; B-05 structure owner"),
        "3.5": ("P4.2", "Prompt 14 calibration; B-05 structure owner"),
        "3.6": ("P4.2", "Prompt 14 calibration; B-05 structure owner"),
        "3.7": ("P3.7 / P4.2", "Prompt 14 calibration; B-05 structure owner"),
    },
    "B-06": {
        "3.1": ("P3.8", "Prompt 14 calibration; B-06 structure owner"),
        "3.2": ("P3.8 / P4.3", "Prompt 14 calibration; B-06 structure owner"),
        "3.3": ("P3.8", "DMP-063 structure; Prompt 14 calibration"),
        "3.4": ("P3.8 / P4.3", "Prompt 14 calibration; B-06 structure owner"),
        "3.5": ("Derived on read", "DMP structure; Prompt 14 calibration"),
        "3.6": ("Immediate (policy order); P3.8 (fiscal)", "DMP-095 sets the settings; Prompt 14 calibrates"),
        "3.7": ("P3.8", "Prompt 14 calibration; B-06 structure owner"),
        "3.8": ("P3.8 / P4.3", "D-107 fixes the cycle; Prompt 14 calibrates the constants"),
        "3.9": ("P4.3", "DMP constants; Prompt 14 calibration"),
    },
    "B-07": {
        "3": ("P3/P4 boundary; statistic job off-path", "Prompt 14 calibration; B-07 structure owner; G-5 for fees"),
    },
}

B02_META = {
    "Turn length": ("OWNER-APPROVED VALUE", "Fixed constraint"),
    "Turns per day": ("OWNER-APPROVED VALUE", "Fixed constraint"),
    "Turns per 7 days": ("OWNER-APPROVED VALUE", "Fixed constraint"),
    "Turns per 30 days": ("OWNER-APPROVED VALUE", "Fixed constraint"),
    "Turns per 14 days (dormancy)": ("OWNER-APPROVED VALUE", "Owner decision D-028"),
    "Phase set": ("OWNER-APPROVED VALUE", "Fixed by B-02"),
    "Ordering bands": ("OWNER-APPROVED VALUE", "Fixed by B-02"),
}

B03_CLASS = {
    "Network observation window W_obs": "Playtest data",
    "Observation life R_obs": "Operational measurement",
    "Large-network threshold L_large": "Operational data",
    "Restricted-attempt escalation": "Operational data",
    "Review service target": "Operational measurement",
    "Clearance watch": "Case data",
    "Re-review interval after MAINTAINED": "Case data",
    "Network digest retention": "Operational measurement",
    "Pair-record retention": "Legal review",
    "Newcomer protection P_prot": "Playtest data",
    "Fresh-nation transfer window": "Market data",
    "Fair-value band": "Market data",
    "Display-name change cooldown": "Abuse data",
    "Short-name change cooldown": "Abuse data",
    "Released-name hold": "Abuse data",
    "Reroll review flag": "Playtest data",
    "Reroll request rate limit": "Load measurement",
    "Account closure cooling": "Operational data",
    "Unverified-account cleanup": "Operational data",
    "Session absolute lifetime": "Configuration evidence",
}

UNIT_PATTERNS_R1 = [
    ("basis points", r"(?<![a-z])basis points?(?![a-z])"), ("bp", r"(?<![a-z])bp(?![a-z])"),
    ("resource units", r"(?<![a-z])resource units?(?![:a-z])"), ("crowns", r"(?<![a-z])crowns?(?![a-z])"),
    ("batches", r"(?<![a-z])batches?(?![a-z])"), ("turns", r"(?<![a-z])turns?(?![a-z])"),
    ("people", r"(?<![a-z])people(?![a-z])"), ("levels", r"(?<![a-z])levels?(?![a-z])"),
    ("capacity points", r"(?<![a-z])capacity points?(?![a-z])"), ("DC", r"(?<![a-z])DC(?![a-z])"),
    ("research points", r"(?<![a-z])research points?(?![a-z])"), ("RP", r"(?<![a-z])RP(?![a-z])"),
    ("generation units", r"(?<![a-z])generation units?(?![:a-z])"), ("GU", r"(?<![a-z])GU(?![a-z])"),
    ("operations points", r"(?<![a-z])operations points?(?![a-z])"), ("OP", r"(?<![a-z])OP(?![a-z])"),
    ("operations", r"(?<![a-z])operations?(?![a-z])"), ("actions", r"(?<![a-z])actions?(?![a-z])"),
    ("points", r"(?<![a-z])points?(?![a-z])"), ("units", r"(?<![a-z])units?(?![:a-z])"),
    ("days", r"(?<![a-z])days?(?![a-z])"), ("hours", r"(?<![a-z])hours?(?![a-z])"),
    ("months", r"(?<![a-z])months?(?![a-z])"), ("seconds", r"(?<![a-z])seconds?(?![a-z])"),
    ("members", r"(?<![a-z])members?(?![a-z])"), ("cities", r"(?<![a-z])cities(?![a-z])"),
    ("proposals", r"(?<![a-z])proposals?(?![a-z])"), ("listings", r"(?<![a-z])listings?(?![a-z])"),
    ("offers", r"(?<![a-z])offers?(?![a-z])"), ("chains", r"(?<![a-z])chains?(?![a-z])"),
    ("executions", r"(?<![a-z])executions?(?![a-z])"), ("trades", r"(?<![a-z])trades?(?![a-z])"),
    ("nations", r"(?<![a-z])nations?(?![a-z])"), ("projects", r"(?<![a-z])projects?(?![a-z])"),
    ("boolean", r"(?<![a-z])booleans?(?![a-z])"), ("dimensionless", r"(?<![a-z])dimensionless(?![a-z])"),
    ("ordinal", r"(?<![a-z])ordinal(?![a-z])"), ("multiplier", r"(?<![a-z])multipliers?(?![a-z])"),
    ("appeals", r"(?<![a-z])appeals?(?![a-z])"), ("ledger value", r"(?<![a-z])ledger values?(?![a-z])"),
]


def _unit_tokens_r1(text):
    low = (text or "").lower()
    return {name for name, pat in UNIT_PATTERNS_R1 if re.search(pat, low, re.I)}


def _b03_unit_words(value):
    low = (value or "").lower()
    out = set()
    if "hour" in low or re.search(r"\d\s*h(?![a-z])", low):
        out.add("hours")
    if "day" in low:
        out.add("days")
    if "month" in low:
        out.add("months")
    if "seconds" in low:
        out.add("seconds")
    return out


PRECISION_CONVENTION = {
    "B-04": "Integer / bp per register convention",
    "B-05": "Integer / bp per register convention",
    "B-06": "Integer / bp per register convention",
    "B-07": "Integer / bp per register convention",
}
PRECISION_ANCHORS = {
    "B-04": ("F-EC-000b", "binary floating point"),
    "B-05": ("F-CI-000c", "No formula uses floating point"),
    "B-06": ("F-PD-000b", "No formula uses floating point"),
    "B-07": ("F-TM-000c", "No formula uses binary floating point"),
}
OWNER_RESERVED_UDS = {"UD-017"} | {"UD-%03d" % i for i in list(range(40, 50)) + list(range(52, 61))}
# UD-050 and UD-051 are evidence/Prompt-14 reservations, not owner-reserved numerical values.

B04_CONTRACT = {
    "F-EC-000b": {
        "source_version": "B-04 formula register v1.4",
        "baseline_text": "F-EC-000b - Integer arithmetic. Provisional (REQ-162). All quantities are integers. Every division states its rounding: floor (toward negative infinity for negative values; toward zero for the positive values used here), ceil or round_half_up. No formula uses binary floating point. A percentage is an integer in basis points (bp), where 10,000 bp = 100%.",
        "hash": "bb1090ccae5cd15e0d883a57ab63216a106ff7c4e503e85cf2146e19e02271c6",
        "required": [
            "All quantities are integers.",
            "Every division states its rounding",
            "floor",
            "ceil",
            "round_half_up",
            "No formula uses binary floating point.",
            "A percentage is an integer in basis points",
            "10,000 bp = 100%",
        ],
        "forbidden": [
            "may be decimal fractions",
            "may use binary floating point",
            "floating-point formula calculations are permitted",
        ],
    },
    "F-EC-000f": {
        "source_version": "B-04 formula register v1.4",
        "baseline_text": "F-EC-000f - Constants are versioned. Provisional. The constants below are the v1.0 provisional calibration, carried unchanged into v1.1 (see F-EC-044). They are not observed prices and not balance claims. Prompt 14 may change a value only by a new revision of this register.",
        "hash": "3025cc447ebb91be8d226ff5035da0e403947d2be603e81e535bbd5600bca5ca",
        "required": [
            "v1.0 provisional calibration",
            "carried unchanged into v1.1",
            "F-EC-044",
            "not observed prices",
            "not balance claims",
            "Prompt 14 may change a value only by a new revision of this register.",
        ],
        "forbidden": [
            "Only the project owner may change",
            "are observed prices",
            "are balance claims",
        ],
    },
}

B04_EVIDENCE_ALLOWED = {
    "F-EC-000b": [
        ("docs/stage-2/10_economic_formula_and_balance_register.md", "F-EC-000b"),
        ("docs/stage-2/10_economic_formula_and_balance_register.md", "F-EC-000c"),
        ("docs/stage-2/22_formulas_and_balance.md", "8.2"),
        ("docs/stage-2/03_requirements_traceability.md", "REQ-162"),
    ],
    "F-EC-000f": [
        ("docs/stage-2/10_economic_formula_and_balance_register.md", "F-EC-000f"),
        ("docs/stage-2/10_economic_formula_and_balance_register.md", "F-EC-044"),
        ("docs/stage-2/22_formulas_and_balance.md", "5."),
        ("docs/stage-2/22_formulas_and_balance.md", "7."),
    ],
}

B14_HEADINGS = [
    "Purpose and scope",
    "Governing constraints and source authority",
    "Formula-register architecture",
    "Master formula inventory",
    "Numerical parameter master inventory",
    "B-03 carry-in parameter reconciliation",
    "Numerical approval and status classifications",
    "Units, precision and rounding conventions",
    "Turn timing and numerical execution order",
    "Cross-system numerical dependencies",
    "Initial balance-parameter inventory",
    "Existing validator and QA baseline",
    "Identified inconsistencies and missing definitions",
    "Owner-reserved and externally dependent parameters",
    "Prompt 14A completion and evidence",
    "Subsequent Prompt 14 subphase ownership",
]

HEADING_RE = re.compile(r"^### (" + "|".join(PREFIXES) + r")-(\d{3})([a-z]?)\s*[—-]\s*(.+?)\s*$")
BOLD_RE = re.compile(r"^\*\*(" + "|".join(PREFIXES) + r")-(\d{3})([a-z]?)\s*[—-]\s*(.+?)\.?\*\*\s*(.*)$")


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
_READ_CACHE = {}
_HASH_CACHE = {}
_PARSE_CACHE = {}


def _text_hash(text):
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def _memo_text_parse(func):
    """Memoize a parser by text hash and immutable extra arguments."""
    def wrapper(text, *args):
        key = (func.__name__, _text_hash(text), args)
        if key not in _PARSE_CACHE:
            _PARSE_CACHE[key] = func(text, *args)
        return _PARSE_CACHE[key]
    wrapper.__name__ = func.__name__
    return wrapper


def read(path):
    if path not in _READ_CACHE:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            _READ_CACHE[path] = fh.read()
    return _READ_CACHE[path]


def norm(s):
    return re.sub(r"\s+", " ", (s or "").replace("`", "").replace("**", "")).strip()


def split_row(line):
    """Split a Markdown table row on unescaped pipes."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells, buf, i = [], [], 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            buf.append("|")
            i += 2
            continue
        if s[i] == "|":
            cells.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(s[i])
        i += 1
    cells.append("".join(buf).strip())
    return cells


def is_separator(cells):
    return bool(cells) and all(set(c) <= set("-: ") for c in cells)


def tables_after(text, start_index):
    """Yield (header, rows) for contiguous tables after a position."""
    lines = text[start_index:].splitlines()
    header, rows = None, []
    for line in lines:
        if not line.strip().startswith("|"):
            if header is not None:
                yield header, rows
                header, rows = None, []
            continue
        cells = split_row(line)
        if is_separator(cells):
            continue
        if header is None:
            header = cells
        else:
            rows.append(cells)
    if header is not None:
        yield header, rows


@_memo_text_parse
def parse_register(text, prefix):
    """Return active ids, register-rule ids, retired ids and duplicates."""
    active, rules, retired, seen = [], [], [], []
    for line in text.splitlines():
        m = HEADING_RE.match(line) or BOLD_RE.match(line)
        if not m:
            continue
        fid = m.group(1) + "-" + m.group(2) + m.group(3)
        num = int(m.group(2))
        seen.append(fid)
        if num == 0:
            rules.append(fid)
        elif fid == "F-WEP-048":
            retired.append(fid)
        else:
            active.append(fid)
    dupes = sorted({i for i in active if active.count(i) > 1})
    return active, rules, retired, dupes


@_memo_text_parse
def parse_master(text):
    """Return identity rows and contract rows keyed by formula id."""
    identity, contract = {}, {}
    identity_dupes = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("| Formula ID |"):
            header = split_row(line)
            mode = "identity" if "Formula name" in header else ("contract" if "Input units" in header else None)
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                if is_separator(split_row(lines[i])):
                    i += 1
                    continue
                cells = split_row(lines[i])
                if cells and cells[0].startswith("`") and mode in ("identity", "contract"):
                    fid = cells[0].strip("`")
                    if mode == "identity":
                        if fid in identity:
                            identity_dupes.append(fid)
                        identity[fid] = cells
                    else:
                        contract[fid] = cells
                i += 1
            continue
        i += 1
    return identity, contract, sorted(set(identity_dupes))


def parse_b03_rows(text):
    idx = text.find("### 21.2")
    if idx < 0:
        return []
    rows = []
    for header, data in tables_after(text, idx):
        if header and header[0].lower() == "parameter":
            for r in data:
                rows.append({"name": r[0], "value": r[1], "purpose": r[2],
                             "owner": r[3], "evidence": r[4]})
            break
    return rows


def parse_param_b03(text):
    idx = text.find("## 4. B-03")
    if idx < 0:
        return []
    rows = []
    for header, data in tables_after(text, idx):
        if header and any("Provisional value" in h for h in header):
            for r in data:
                rows.append({"name": r[1], "value": r[2], "unit": r[3], "owner": r[4],
                             "evidence": r[5], "cls": r[6], "reserved": r[7]})
            break
    return rows


def parse_ud_rows(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*\*{0,2}(UD-\d{3})\b", line)
        if m:
            out.setdefault(m.group(1), line)
    return out


def first_cells_in_section3(text):
    """Yield first-cell names from every §3.x table."""
    names = []
    lines = text.splitlines()
    in3 = False
    for line in lines:
        if line.startswith("## "):
            in3 = bool(re.match(r"##\s+3(?:\.|\s|$)", line))
            continue
        if line.startswith("### "):
            in3 = bool(re.match(r"###\s+3(?:\.|\s|$)", line))
            continue
        if not in3 or not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        if not cells or is_separator(cells):
            continue
        name = norm(cells[0])
        if name.lower() in {"item", "resource", "chain", "generator", "id", "class", "constant",
                            "government", "government_id", "setting", "input", "group", "symbol",
                            "parameter", "total", ""}:
            continue
        names.append(name)
    return names


def sha256_file(path):
    if path not in _HASH_CACHE:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        _HASH_CACHE[path] = h.hexdigest()
    return _HASH_CACHE[path]


def _numeric_tokens(text):
    out = []
    for m in re.finditer(r"(?<![A-Za-z0-9_.\-§])(\d{1,3}(?:,\d{3})+|\d+)(?!\d)", text or ""):
        out.append(m.group(1).replace(",", ""))
    return out


def _tok_tuple(text):
    return tuple(sorted(_numeric_tokens(text)))


def _norm_auth(text):
    s = norm(text).lower()
    return re.sub(r"\s*/\s*", "/", s)


def _clean_cell(text):
    s = (text or "").strip()
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("**", "").replace("`", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def _row_split(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells, buf, i = [], [], 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            buf.append("|")
            i += 2
            continue
        if s[i] == "|":
            cells.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(s[i])
        i += 1
    cells.append("".join(buf).strip())
    return cells


def _is_sep(cells):
    return bool(cells) and all(set(c) <= set("-: ") for c in cells)


@_memo_text_parse
def parse_param_inventory(text):
    """Parse the B-14 parameter inventory into schema-specific records."""
    out = {"constants": [], "formulas": [], "fp": [], "b02": [], "b03": []}
    section = ""
    mode = None
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            section = line[3:].strip()
            mode = None
            continue
        if not line.strip().startswith("|"):
            continue
        cells = _row_split(line)
        if _is_sep(cells) or not cells:
            continue
        low = [c.lower() for c in cells]
        if low[:1] == ["id"] and "parameter" in low and len(cells) == 9 and "used by" in low:
            mode = "fp"
            continue
        if low[:1] == ["id"] and "parameter" in low and len(cells) == 14 and "current value" in low:
            mode = "main"
            continue
        if low[:1] == ["parameter"] and "value" in low:
            mode = "b02"
            continue
        if low[:1] == ["#"] and "parameter" in low:
            mode = "b03"
            continue
        if mode == "main" and len(cells) == 14:
            rec = {
                "id": _clean_cell(cells[0]), "name": _clean_cell(cells[1]),
                "value": _clean_cell(cells[2]), "unit": _clean_cell(cells[3]),
                "source": _clean_cell(cells[4]), "used": _clean_cell(cells[5]),
                "prec": _clean_cell(cells[6]), "timing": _clean_cell(cells[7]),
                "auth": _clean_cell(cells[8]), "validator": _clean_cell(cells[9]),
                "status": _clean_cell(cells[10]), "evidence": _clean_cell(cells[11]),
                "deps": _clean_cell(cells[12]), "reserved": _clean_cell(cells[13]),
                "line": lineno, "section": section,
            }
            if rec["id"].startswith("F-"):
                out["formulas"].append(rec)
            elif rec["id"].startswith("FP-P"):
                out["fp"].append(rec)
            else:
                out["constants"].append(rec)
        elif mode == "b02" and len(cells) == 7:
            out["b02"].append({
                "name": _clean_cell(cells[0]), "value": _clean_cell(cells[1]),
                "unit": _clean_cell(cells[2]), "source": _clean_cell(cells[3]),
                "used": _clean_cell(cells[4]), "auth": _clean_cell(cells[5]),
                "status": _clean_cell(cells[6]), "line": lineno, "section": section,
            })
        elif mode == "b03" and len(cells) == 8:
            out["b03"].append({
                "num": _clean_cell(cells[0]), "name": _clean_cell(cells[1]),
                "value": _clean_cell(cells[2]), "unit": _clean_cell(cells[3]),
                "owner": _clean_cell(cells[4]), "evidence": _clean_cell(cells[5]),
                "cls": _clean_cell(cells[6]), "reserved": _clean_cell(cells[7]),
                "line": lineno, "section": section,
            })
        elif mode == "fp" and len(cells) == 9:
            out["fp"].append({
                "id": _clean_cell(cells[0]), "name": _clean_cell(cells[1]),
                "value": _clean_cell(cells[2]), "unit": _clean_cell(cells[3]),
                "used": _clean_cell(cells[4]), "status": _clean_cell(cells[5]),
                "auth": _clean_cell(cells[6]), "evidence": _clean_cell(cells[7]),
                "reserved": _clean_cell(cells[8]), "line": lineno, "section": section,
            })
    return out


def _parse_source_fields(block):
    fields = {}
    for m in re.finditer(r"^\|\s*(?:\d+\s*\|\s*)?\*{0,2}([A-Za-z][A-Za-z0-9 &/()\-\.']*?)\*{0,2}\s*\|\s*(.*?)\s*\|\s*$", block, re.M):
        label = m.group(1).strip().lower()
        if label not in ("field", "---", "#"):
            fields.setdefault(label, m.group(2).strip())
    for m in re.finditer(r"^\d+\.\s+\*\*([A-Za-z][A-Za-z0-9 &/()\-\.']*?)\.\*\*\s*(.*)$", block, re.M):
        fields.setdefault(m.group(1).strip().lower(), m.group(2).strip())
    return fields


def expected_constants(stage2, overrides=None):
    """Build expected constant-table records from B-04…B-07 §3 tables."""
    expected = {}
    files = {
        "B-04": "10_economic_formula_and_balance_register.md",
        "B-05": "11_city_infrastructure_production_and_research_formula_register.md",
        "B-06": "12_population_and_domestic_politics_formula_register.md",
        "B-07": "13_trade_and_markets_formula_register.md",
    }
    overrides = overrides or {}
    sources = {}
    for system, fname in files.items():
        src = overrides.get("REG_" + system)
        if src is None:
            src = read(os.path.join(stage2, fname))
        sources[system] = src
    cache_key = ("expected_constants", tuple((system, _text_hash(sources[system])) for system in files))
    if cache_key in _PARSE_CACHE:
        return _PARSE_CACHE[cache_key]
    for system, fname in files.items():
        src_text = sources[system]
        lines = src_text.splitlines()
        section = None
        header = None
        for line in lines:
            if line.startswith("## "):
                m = re.match(r"##\s+3(?:\.(\d+))?", line)
                section = ("3." + m.group(1)) if m and m.group(1) else ("3" if m else None)
                header = None
                continue
            if line.startswith("### ") and section:
                m = re.match(r"###\s+(\d+(?:\.\d+)*)", line)
                if m:
                    section = m.group(1)
                header = None
                continue
            if not line.strip():
                header = None
                continue
            if section is None or not line.strip().startswith("|"):
                continue
            cells = _row_split(line)
            if _is_sep(cells) or not cells:
                continue
            if header is None:
                header = cells
                continue
            name = _clean_cell(cells[0])
            if not name or name.lower() in {"item", "resource", "chain", "generator", "id", "class", "constant",
                                            "government", "government_id", "setting", "input", "group", "symbol",
                                            "parameter"}:
                continue
            unit = ""
            symbol = ""
            token_cells = []
            for j, h in enumerate(header):
                if j >= len(cells):
                    continue
                if h.lower() in ("unit", "units"):
                    unit = _clean_cell(cells[j])
                    continue
                if h.lower() in ("notes", "note", "rationale"):
                    continue
                if h.lower() in ("symbol", "id"):
                    if j > 0:
                        symbol = _clean_cell(cells[j])
                    continue
                if j > 0:
                    token_cells.append(cells[j])
            if symbol and symbol.lower() != "none":
                name = f"{name} ({symbol})"
            header_tokens = _numeric_tokens(" ".join(header[1:]))
            tokens = tuple(sorted(_numeric_tokens(" ".join(token_cells)) + header_tokens))
            key = (f"{system} §{section}", name)
            expected.setdefault(key, []).append({"tokens": tokens, "unit": unit})
    _PARSE_CACHE[cache_key] = expected
    return expected


def expected_formulas(stage2, overrides=None):
    """Build expected formula-level parameter records from B-08…B-11."""
    files = {
        "B-08": ("15_diplomacy_formula_register.md", "F-DP"),
        "B-09": ("16_alliances_formula_register.md", "F-AL"),
        "B-10": ("17_warfare_formula_register.md", "F-WR"),
        "B-11": ("18_world_events_objectives_rankings_progression_formula_register.md", "F-WEP"),
    }
    WEP_PROMPT14 = {"F-WEP-003", "F-WEP-004", "F-WEP-005", "F-WEP-007", "F-WEP-009", "F-WEP-010",
                    "F-WEP-012", "F-WEP-015", "F-WEP-016", "F-WEP-019", "F-WEP-024", "F-WEP-025",
                    "F-WEP-031", "F-WEP-034", "F-WEP-035", "F-WEP-036", "F-WEP-040", "F-WEP-042",
                    "F-WEP-043", "F-WEP-050"}
    overrides = overrides or {}
    sources = {}
    for system, (fname, prefix) in files.items():
        src = overrides.get("REG_" + system)
        if src is None:
            src = read(os.path.join(stage2, fname))
        sources[system] = src
    cache_key = ("expected_formulas", tuple((system, _text_hash(sources[system])) for system in files))
    if cache_key in _PARSE_CACHE:
        return _PARSE_CACHE[cache_key]
    out = {}
    for system, (fname, prefix) in files.items():
        text = sources[system]
        lines = text.splitlines()
        marks = []
        for i, line in enumerate(lines, 1):
            m = re.match(r"^### (" + prefix + r"-\d{3}[a-z]?)\s*[—-]\s*(.+)$", line)
            if m:
                marks.append((i, m.group(1), m.group(2)))
        for idx, (ln, fid, name) in enumerate(marks):
            if fid == "F-WEP-048":
                continue
            end = marks[idx + 1][0] - 1 if idx + 1 < len(marks) else len(lines)
            fields = _parse_source_fields("\n".join(lines[ln - 1:end]))
            value = fields.get("value", "")
            prov = fields.get("provisional status", "")
            owner = fields.get("calibration owner", "")
            if system == "B-08":
                status = "PROVISIONAL VALUE" if "provisional" in value.lower() else "UNSPECIFIED"
                auth = "B-08 rule owner (no Prompt 14 calibration registered)"
                reserved = "No"
                source_text = value
                rounding = fields.get("rounding", "")
                timing = fields.get("timing", "")
            elif system == "B-09":
                status = "DESIGN PROPOSAL"
                auth = "Owner — UD-040 / UD-043 / UD-044 / UD-046"
                reserved = "Yes — owner-reserved"
                source_text = value or "No platform-set value; player-authored parameters"
                rounding = fields.get("rounding", "")
                timing = fields.get("timing", "")
            elif system == "B-10":
                status = "PROVISIONAL VALUE" if ("provisional" in prov.lower() or "calibration required" in prov.lower()) else "UNSPECIFIED"
                auth = owner or "None"
                reserved = "Yes — owner-reserved" if "UD-" in prov else "No"
                source_text = prov or "Structural; no calibration parameter"
                rounding = fields.get("rounding", "")
                timing = fields.get("phase and trigger", "")
            else:
                status = "PROVISIONAL VALUE" if (("provisional" in prov.lower() or "prompt 14" in prov.lower()) and "no calibration" not in prov.lower()) else "UNSPECIFIED"
                auth = "Prompt 14" if "prompt 14" in prov.lower() else "B-11 structure owner"
                reserved = "No"
                source_text = prov or "Structural; no calibration parameter"
                rounding = fields.get("rounding", "")
                timing = fields.get("phase", "")
            if system == "B-08":
                unit_source = fields.get("variables", "") + " " + fields.get("range", "")
                unit_present = bool(fields.get("variables", "").strip())
            elif system == "B-09":
                unit_source = fields.get("variables & units", fields.get("variables", "")) + " " + fields.get("range", "")
                unit_present = bool((fields.get("variables & units", "") or fields.get("variables", "")).strip())
            elif system == "B-10":
                unit_source = fields.get("output", "")
                unit_present = bool(fields.get("output", "").strip())
            else:
                unit_source = fields.get("units", "") + " " + fields.get("output range", "")
                unit_present = bool(fields.get("units", "").strip())
            if system == "B-09":
                expected_reserved = "Yes — owner-reserved"
            elif system == "B-10":
                expected_reserved = "Yes — owner-reserved" if any(ud in prov for ud in OWNER_RESERVED_UDS) else "No"
            else:
                expected_reserved = "No"
            out[fid] = {
                "system": system, "name": name.strip(), "status": status, "auth": auth,
                "owner_reserved_expected": expected_reserved,
                "reserved": reserved, "tokens": _tok_tuple(source_text[:200]),
                "rounding": _clean_cell(rounding), "timing": _clean_cell(timing),
                "source": f"{system} formula {fid}", "unit_field_present": unit_present,
                "unit_source": unit_source,
            }
    _PARSE_CACHE[cache_key] = out
    return out


def expected_b02():
    return [
        ("Turn length", ("2", "7200"), "hours", "OWNER-APPROVED VALUE", None),
        ("Turns per day", ("12",), "turns", "OWNER-APPROVED VALUE", None),
        ("Turns per 7 days", ("84",), "turns", "OWNER-APPROVED VALUE", None),
        ("Turns per 30 days", ("360",), "turns", "OWNER-APPROVED VALUE", None),
        ("Turns per 14 days (dormancy)", ("168",), "turns", "OWNER-APPROVED VALUE", None),
        ("Phase set", (), "phases", "OWNER-APPROVED VALUE", "P0–P7"),
        ("Ordering bands", (), "bands", "OWNER-APPROVED VALUE", "B0–B4"),
    ]


def expected_fp(stage2, overrides=None):
    overrides = overrides or {}
    text = overrides.get("REG_B-12")
    if text is None:
        text = read(os.path.join(stage2, "20_fair_play_and_player_protection_formula_register.md"))
    cache_key = ("expected_fp", _text_hash(text))
    if cache_key in _PARSE_CACHE:
        return _PARSE_CACHE[cache_key]
    idx = text.find("## 3. Parameter register")
    out = {}
    if idx < 0:
        return out
    lines = text[idx:].splitlines()
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = _row_split(line)
        if len(cells) < 6 or "FP-P" not in cells[0]:
            continue
        m = re.search(r"(FP-P\d{2})`?\s+(.*)", cells[0])
        if not m:
            continue
        pid = m.group(1)
        pname = _clean_cell(m.group(2))
        cls = _clean_cell(cells[3])
        owner = _clean_cell(cells[4])
        status = {"Provisional": "PROVISIONAL VALUE", "Owner decision required": "UNSPECIFIED",
                  "Capacity validation": "NEEDS PLAYTESTING", "Legal review required": "UNSPECIFIED"}.get(cls, "")
        out[pid] = {
            "name": pname, "value": _clean_cell(cells[2]), "unit": "",
            "status": status, "auth": owner,
            "reserved": "Yes — owner-reserved" if "Owner" in owner else "No",
        }
    _PARSE_CACHE[cache_key] = out
    return out


# ----------------------------------------------------------------------------
# checks
# ----------------------------------------------------------------------------
def validate(overrides=None):
    overrides = overrides or {}
    results = []

    def text(key):
        if key in overrides:
            return overrides[key]
        return read(FILES[key])

    def add(cid, desc, problems):
        results.append((cid, desc, problems))

    # 01 — registers exist
    missing = [fname for _, fname, _, _ in REGISTERS if not os.path.isfile(os.path.join(STAGE2, fname))]
    add("14A-01", "All nine formula registers exist", ["missing: " + ", ".join(missing)] if missing else [])

    # 02/03/04 — per-register counts, duplicates, retirement
    all_active, register_data, problems2, problems3, problems4 = [], {}, [], [], []
    for system, fname, prefix, expected in REGISTERS:
        if "REG_" + system in overrides:
            src = overrides["REG_" + system]
        else:
            src = read(os.path.join(STAGE2, fname))
        active, rules, retired, dupes = parse_register(src, prefix)
        register_data[system] = (active, rules, retired)
        all_active.extend(active)
        if len(active) != expected:
            problems2.append(f"{system}: expected {expected} active, found {len(active)}")
        if dupes:
            problems3.append(f"{system}: duplicate active IDs {dupes}")
        if system == "B-11":
            if retired != ["F-WEP-048"]:
                problems4.append(f"B-11 retired set is {retired}, expected ['F-WEP-048']")
            if "F-WEP-048" in active:
                problems4.append("F-WEP-048 is counted as active")
        elif retired:
            problems4.append(f"{system}: unexpected retired IDs {retired}")
    add("14A-02", "Per-register active counts match the 295 baseline", problems2)
    add("14A-03", "No duplicate active formula identifier", problems3)
    add("14A-04", "Retired formulas are excluded from the active set", problems4)

    # 05/06 — master inventory completeness
    master_text = text("MASTER")
    identity, contract, identity_dupes = parse_master(master_text)
    id_ids = set(identity)
    active_set = set(all_active)
    problems5 = []
    duplicate_active = sorted({i for i in all_active if all_active.count(i) > 1})
    if duplicate_active:
        problems5.append("duplicate active IDs across registers: " + ", ".join(duplicate_active))
    if identity_dupes:
        problems5.append("duplicate identity rows in the master inventory: " + ", ".join(identity_dupes))
    if id_ids != active_set:
        missing_ids = sorted(active_set - id_ids)
        extra_ids = sorted(id_ids - active_set)
        if missing_ids:
            problems5.append(f"missing from master inventory: {len(missing_ids)} — {missing_ids[:8]}")
        if extra_ids:
            problems5.append(f"not an active formula: {len(extra_ids)} — {extra_ids[:8]}")
    if len(identity) != len(all_active):
        problems5.append(f"master identity rows {len(identity)} != active formulas {len(all_active)}")
    if set(contract) != active_set:
        problems5.append(f"contract-table ID set differs ({len(contract)} rows)")
    add("14A-05", "Master inventory contains every active ID exactly once", problems5)

    # 06 — required metadata fields
    required_identity = {1: "system", 3: "source document", 4: "source section", 5: "purpose",
                         6: "status", 7: "authority", 8: "validator coverage", 9: "evidence", 10: "outstanding"}
    required_contract = {1: "inputs", 2: "input units", 3: "output", 4: "output units", 5: "precision",
                         6: "rounding", 7: "timing", 8: "turn phase", 9: "dependencies", 10: "invariant"}
    problems6 = []
    for fid, cells in identity.items():
        for idx, label in required_identity.items():
            if idx < len(cells) and not cells[idx].strip():
                problems6.append(f"{fid}: missing {label}")
            if idx >= len(cells):
                problems6.append(f"{fid}: row shorter than the required field set ({label})")
    for fid, cells in contract.items():
        for idx, label in required_contract.items():
            if idx < len(cells) and not cells[idx].strip():
                problems6.append(f"{fid}: missing {label}")
    add("14A-06", "Every record has the required metadata or an explicit gap marker", problems6)

    # 07 — source references resolve
    problems7 = []
    for fid, cells in identity.items():
        if len(cells) < 10:
            continue
        evidence = cells[9]
        m = re.search(r"`?(docs/stage-2/[^`\s]+?\.md)`?\s+line\s+(\d+)", evidence)
        if not m:
            problems7.append(f"{fid}: no resolvable source reference in Evidence")
            continue
        path = os.path.join(os.path.dirname(BASE), m.group(1).replace("/", os.sep))
        if not os.path.isfile(path):
            problems7.append(f"{fid}: source file missing {m.group(1)}")
            continue
        line_no = int(m.group(2))
        if line_no < 1 or line_no > len(read(path).splitlines()):
            problems7.append(f"{fid}: line {line_no} outside {m.group(1)}")
    add("14A-07", "Every inventory record resolves to its canonical source", problems7)

    # 08 — status vocabulary
    problems8 = []
    for fid, cells in identity.items():
        status = norm(cells[6]) if len(cells) > 6 else ""
        if status not in VALID_STATUSES:
            problems8.append(f"{fid}: invalid status {status!r}")
    add("14A-08", "All numerical statuses use the prescribed vocabulary", problems8)

    # 09 — owner-approved safeguard
    problems9 = []
    for fid, cells in identity.items():
        status = norm(cells[6]) if len(cells) > 6 else ""
        if status == "OWNER-APPROVED VALUE":
            blob = " ".join(cells)
            if not re.search(r"D-\d{3}", blob) and "Fixed constraint" not in blob and "Fixed by B-02" not in blob:
                problems9.append(f"{fid}: OWNER-APPROVED without a decision citation")
    for line in master_text.splitlines():
        if "OWNER-APPROVED VALUE" in line and line.strip().startswith("| `F-"):
            if not re.search(r"D-\d{3}", line):
                problems9.append("unattributed OWNER-APPROVED row")
    # B-09 is candidate-only
    for fid, cells in identity.items():
        if fid.startswith("F-AL-") and norm(cells[6]) != "DESIGN PROPOSAL":
            problems9.append(f"{fid}: B-09 must remain a DESIGN PROPOSAL, found {norm(cells[6])}")
    add("14A-09", "No false owner-approved classification", sorted(set(problems9)))

    # 10 — parameter document and B-03 20 rows
    params_text = text("PARAMS")
    source_rows = parse_b03_rows(text("B03"))
    mirror_rows = parse_param_b03(params_text)
    problems10 = []
    if not os.path.isfile(FILES["PARAMS"]):
        problems10.append("parameter inventory missing")
    if len(source_rows) != 20:
        problems10.append(f"B-03 §21.2 has {len(source_rows)} rows, expected 20")
    if len(mirror_rows) != 20:
        problems10.append(f"parameter inventory mirrors {len(mirror_rows)} B-03 rows, expected 20")
    add("14A-10", "All 20 B-03 carry-in parameters are accounted for", problems10)

    # 11 — exact B-03 values and owners
    problems11 = []
    if len(source_rows) == len(mirror_rows) == 20:
        for i, (src, mir) in enumerate(zip(source_rows, mirror_rows), 1):
            if norm(src["name"]) != norm(mir["name"]):
                problems11.append(f"row {i}: name {norm(mir['name'])!r} != source {norm(src['name'])!r}")
            if norm(src["value"]) != norm(mir["value"]):
                problems11.append(f"row {i} ({norm(src['name'])}): value {norm(mir['value'])!r} != source {norm(src['value'])!r}")
            if norm(src["owner"]) != norm(mir["owner"]):
                problems11.append(f"row {i} ({norm(src['name'])}): owner {norm(mir['owner'])!r} != source {norm(src['owner'])!r}")
    add("14A-11", "Every B-03 value and numeric owner matches its canonical source", problems11)

    # 12 — no false promotion in the B-03 table
    problems12 = []
    idx = params_text.find("## 4. B-03")
    if idx >= 0:
        block = params_text[idx:params_text.find("## 5.", idx) if params_text.find("## 5.", idx) > 0 else len(params_text)]
        if re.search(r"\|\s*OWNER-APPROVED VALUE\s*\|", block):
            problems12.append("B-03 carry-in block contains an OWNER-APPROVED classification cell")
    add("14A-12", "No B-03 parameter is falsely promoted to owner-approved", problems12)

    # 13 — FP-P01..FP-P14
    problems13 = [f"missing FP-P{i:02d}" for i in range(1, 15) if f"FP-P{i:02d}" not in params_text]
    add("14A-13", "All 14 registered B-12 parameters are represented", problems13)

    # 14 — parameter coverage of §3 constant tables
    problems14 = []
    param_norm = norm(params_text).lower()
    for system, fname, prefix, _ in REGISTERS[:4]:
        src = overrides.get("REG_" + system, read(os.path.join(STAGE2, fname)))
        for name in first_cells_in_section3(src):
            if name.lower() not in param_norm:
                problems14.append(f"{system} §3 row {name!r} has no parameter record")
    add("14A-14", "Every §3 constant-table row is represented in the parameter map", sorted(set(problems14)))

    # 15 — B-14 headings
    b14 = text("B-14")
    problems15 = []
    for n, title in enumerate(B14_HEADINGS, 1):
        if not re.search(r"^##\s+(?:\d+\.\s*)?" + re.escape(title), b14, re.M):
            problems15.append(f"missing heading {n}: {title}")
    add("14A-15", "The canonical B-14 document has all 16 required headings", problems15)

    # 16 — timing references
    problems16 = []
    for token in ("two-hour UTC", "P0", "P7", "P3.7", "D-019", "D-015"):
        if token.lower() not in b14.lower():
            problems16.append(f"missing reference {token}")
    add("14A-16", "Two-hour cadence, P0–P7, D-019 and D-015 are documented", problems16)

    # 17 — D-019 ordering
    problems17 = []
    required = "Production and income are applied first, followed by mandatory upkeep and maintenance"
    if norm(required) not in norm(b14):
        problems17.append("D-019 ordering sentence missing")
    if re.search(r"upkeep[^.]{0,40}before[^.]{0,40}income", b14, re.I):
        problems17.append("a reversed ordering claim is present")
    add("14A-17", "D-019 income-before-upkeep ordering is preserved", problems17)

    # 18 — D-015 current model, obsolete wording not current
    problems18 = []
    for token in ("+1 at the opening of P3.7", "carry", "cap", "10"):
        if token not in b14:
            problems18.append(f"missing current D-015 element {token!r}")
    for sentence in re.split(r"(?<=[.!?])\s+", norm(b14)):
        if "unused points do not bank" in sentence.lower() and not any(
                w in sentence.lower() for w in ("superseded", "conflict", "original", "obsolete", "historical")):
            problems18.append("obsolete D-015 wording presented as current")
    add("14A-18", "The current D-015 Operations Points model is preserved", problems18)

    # 19 — conversions
    problems19 = [f"missing conversion token {t}" for t in ("12 turns", "84", "360", "168") if t not in b14]
    add("14A-19", "Day/turn conversions are documented", problems19)

    # 20 — conservation
    problems20 = []
    if "conservation" not in b14.lower():
        problems20.append("no conservation requirement documented")
    for token in ("Treasury", "Resource", "Market", "Alliance"):
        if token not in b14:
            problems20.append(f"missing {token} conservation identity")
    add("14A-20", "Conservation requirements are identified", problems20)

    # 21 — B-14 file exists
    problems21 = [] if os.path.isfile(FILES["B-14"]) else ["22_formulas_and_balance.md missing"]
    add("14A-21", "Canonical B-14 file exists at the D-198 path", problems21)

    # 22 — roadmap row 14
    roadmap = text("ROADMAP")
    row14 = ""
    for line in roadmap.splitlines():
        if re.match(r"\|\s*14\s*\|", line):
            row14 = line
            break
    problems22 = []
    if not row14:
        problems22.append("no Prompt 14 roadmap row")
    else:
        if "22_formulas_and_balance.md" not in row14:
            problems22.append("row 14 does not reference 22_formulas_and_balance.md")
        for m in re.finditer(r"21_formulas_and_balance\.md", row14):
            clause = row14[max(0, m.start() - 120):m.end() + 120].lower()
            if not any(w in clause for w in ("superseded", "earlier", "historical", "old ")):
                problems22.append("row 14 presents the stale 21_ filename as current")
    add("14A-22", "The live Prompt 14 roadmap row uses the canonical 22_ filename", problems22)

    # 23 — outline mapping
    outline = text("OUTLINE")
    problems23 = []
    if "22_formulas_and_balance.md" not in outline:
        problems23.append("outline does not map B-14 to 22_formulas_and_balance.md")
    for line in outline.splitlines():
        if "21_formulas_and_balance.md" in line:
            clause = line.lower()
            if not any(w in clause for w in ("planned", "superseded", "historical", "earlier")):
                problems23.append("outline presents 21_formulas_and_balance.md without a historical label")
    add("14A-23", "The Bible outline's B-14 mapping agrees", problems23)

    # 24 — final validator expectation
    vf = text("VALIDATE_FINAL")
    problems24 = []
    if '"B-14": "22_formulas_and_balance.md"' not in vf:
        problems24.append("validate_final.py does not expect the 22_ B-14 filename")
    add("14A-24", "The existing final validator expects the same B-14 path", problems24)

    # 25 — owner-reserved UDs
    ud_rows = parse_ud_rows(text("UD"))
    problems25 = []
    for ud in OWNER_RESERVED_UD:
        row = ud_rows.get(ud)
        if not row:
            problems25.append(f"{ud}: row not found")
            continue
        if "**Resolved**" in row or re.search(r"\|\s*Resolved\s*\|", row):
            problems25.append(f"{ud}: owner-reserved decision appears resolved")
        if ud not in b14:
            problems25.append(f"{ud}: not listed in B-14 §14")
    add("14A-25", "Owner-reserved UDs are not silently resolved", problems25)

    # 26 — acceptance gates
    problems26 = [f"missing gate P14A-{i:02d}" for i in range(1, 23) if f"P14A-{i:02d}" not in b14]
    add("14A-26", "The P14A-01…P14A-22 gate register exists", problems26)

    # 27 — B-14 references companions and validator
    problems27 = []
    for token in ("22_formula_master_inventory.md", "22_numerical_parameter_inventory.md",
                  "22_numerical_baseline_qa_report.md", "14A_validate_numerical_foundation.py"):
        if token not in b14:
            problems27.append(f"missing reference {token}")
    add("14A-27", "B-14 links its companions and its validator", problems27)

    # 28 — prompt archive and index
    problems28 = []
    archives = [f for f in os.listdir(PROMPTS)
                if f.startswith("prompt_14A_") and f.endswith(".md")
                and "14A-C1" not in f
                and f != "prompt_14A_semantic_contract_implementation.md"]
    if len(archives) != 1:
        problems28.append(f"expected one original prompt_14A_*.md archive, found {archives}")
    else:
        archive_path = os.path.join(PROMPTS, archives[0])
        index = text("INDEX")
        if archives[0] not in index:
            problems28.append("archive filename not recorded in INDEX.md")
        digest = sha256_file(archive_path)
        if digest not in index:
            problems28.append("archive SHA-256 not recorded in INDEX.md")
        size = os.path.getsize(archive_path)
        if str(size) not in index and "{:,}".format(size) not in index:
            problems28.append("archive byte count not recorded in INDEX.md")
    add("14A-28", "The permanent prompt archive is present and indexed", problems28)

    # 28b — Prompt 14A-C1 archive and index
    problems28b = []
    c1archives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1_") and f.endswith(".md")]
    if len(c1archives) != 1:
        problems28b.append(f"expected one prompt_14A-C1_*.md archive, found {c1archives}")
    else:
        c1path = os.path.join(PROMPTS, c1archives[0])
        index = text("INDEX")
        if c1archives[0] not in index:
            problems28b.append("C1 archive filename not recorded in INDEX.md")
        c1digest = sha256_file(c1path)
        if c1digest not in index:
            problems28b.append("C1 archive SHA-256 not recorded in INDEX.md")
        c1size = os.path.getsize(c1path)
        if str(c1size) not in index and "{:,}".format(c1size) not in index:
            problems28b.append("C1 archive byte count not recorded in INDEX.md")
    add("14A-35", "The Prompt 14A-C1 correction archive is present and indexed", problems28b)

    # 41 — Prompt 14A-C1-R1 archive and index
    problems41 = []
    r1archives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1_") and f.endswith(".md")]
    if len(r1archives) != 1:
        problems41.append(f"expected one prompt_14A-C1-R1_*.md archive, found {r1archives}")
    else:
        r1path = os.path.join(PROMPTS, r1archives[0])
        index = text("INDEX")
        if r1archives[0] not in index:
            problems41.append("R1 archive filename not recorded in INDEX.md")
        r1digest = sha256_file(r1path)
        if r1digest not in index:
            problems41.append("R1 archive SHA-256 not recorded in INDEX.md")
        r1size = os.path.getsize(r1path)
        if str(r1size) not in index and "{:,}".format(r1size) not in index:
            problems41.append("R1 archive byte count not recorded in INDEX.md")
    add("14A-41", "The Prompt 14A-C1-R1 correction archive is present and indexed", problems41)

    # ------------------------------------------------------------------
    # Per-record parameter reconciliation (14A-C1)
    # ------------------------------------------------------------------
    inv = parse_param_inventory(params_text)
    exp_const = expected_constants(STAGE2, overrides)
    exp_form = expected_formulas(STAGE2, overrides)
    exp_fp = expected_fp(STAGE2, overrides)

    # 29 — record set reconciliation
    problems29 = []
    total_actual = sum(len(v) for v in inv.values())
    total_expected = sum(len(v) for v in exp_const.values()) + len(exp_form) + len(exp_fp) + 7 + 20
    if total_actual != 393:
        problems29.append(f"category=total-records param=<inventory> expected=393 actual={total_actual} source=B-14 parameter map inventory_line=<document>")
    if total_expected != 393:
        problems29.append(f"category=source-records param=<sources> expected=393 actual={total_expected} source=canonical registers inventory_line=<validator>")

    act_groups = {}
    for r in inv["constants"]:
        act_groups.setdefault((r["source"], r["name"]), []).append(r)
    for key, expected_list in exp_const.items():
        actual_list = act_groups.get(key, [])
        if len(actual_list) != len(expected_list):
            where = actual_list[0]["line"] if actual_list else "missing"
            problems29.append(
                f"category=record-count param={key[1]!r} expected={len(expected_list)} "
                f"actual={len(actual_list)} source={key[0]} inventory_line={where}")
    for key, actual_list in act_groups.items():
        if key not in exp_const:
            problems29.append(
                f"category=unexpected-record param={key[1]!r} expected=0 actual={len(actual_list)} "
                f"source={key[0]} inventory_line={actual_list[0]['line']}")

    form_ids = [r["id"] for r in inv["formulas"]]
    dup_form = sorted({i for i in form_ids if form_ids.count(i) > 1})
    for fid in dup_form:
        problems29.append(f"category=duplicate-record param={fid} expected=1 actual={form_ids.count(fid)} source={fid} inventory_line=<multiple>")
    act_form = {r["id"]: r for r in inv["formulas"]}
    for fid in exp_form:
        if fid not in act_form:
            problems29.append(f"category=missing-record param={fid} expected=present actual=missing source={exp_form[fid]['source']} inventory_line=missing")
    for fid in act_form:
        if fid not in exp_form:
            problems29.append(f"category=unexpected-record param={fid} expected=0 actual=1 source={act_form[fid]['source']} inventory_line={act_form[fid]['line']}")

    fp_ids = [r["id"] for r in inv["fp"]]
    for pid in exp_fp:
        if pid not in fp_ids:
            problems29.append(f"category=missing-record param={pid} expected=present actual=missing source=B-12 parameter register inventory_line=missing")
    for pid in fp_ids:
        if pid not in exp_fp:
            problems29.append(f"category=unexpected-record param={pid} expected=0 actual=1 source=B-12 parameter register inventory_line=<fp>")

    b02_names = [r["name"] for r in inv["b02"]]
    for name, _tokens, _unit, _status, _text in expected_b02():
        if name not in b02_names:
            problems29.append(f"category=missing-record param={name!r} expected=present actual=missing source=B-02 §3 inventory_line=missing")
    if len(b02_names) != 7:
        problems29.append(f"category=record-count param=<B-02> expected=7 actual={len(b02_names)} source=B-02 §3 inventory_line=<section>")
    if len(inv["b03"]) != 20:
        problems29.append(f"category=record-count param=<B-03> expected=20 actual={len(inv['b03'])} source=B-03 §21.2 inventory_line=<section>")
    add("14A-29", "Every parameter record reconciles to its canonical source set", problems29)

    # 30 — values
    problems30 = []
    for key, expected_list in exp_const.items():
        actual_list = act_groups.get(key, [])
        if len(actual_list) != len(expected_list):
            continue
        exp_tokens = sorted(x["tokens"] for x in expected_list)
        got_tokens = sorted(_tok_tuple(r["value"]) for r in actual_list)
        if exp_tokens != got_tokens:
            for i, (exp, got) in enumerate(zip(exp_tokens, got_tokens)):
                if exp != got:
                    rec = actual_list[i]
                    problems30.append(
                        f"category=value-mismatch param={key[1]!r} expected={list(exp)} actual={list(got)} "
                        f"source={key[0]} inventory_line={rec['line']}")
                    break
    for fid, exp in exp_form.items():
        rec = act_form.get(fid)
        if not rec:
            continue
        got = _numeric_tokens(rec["value"])
        missing = [t for t in exp["tokens"] if t not in got]
        if missing:
            problems30.append(
                f"category=value-mismatch param={fid} expected_tokens={sorted(exp['tokens'])} "
                f"missing_from_inventory={missing} source={exp['source']} inventory_line={rec['line']}")
    fp_actual = {r["id"]: r for r in inv["fp"]}
    for pid, exp in exp_fp.items():
        rec = fp_actual.get(pid)
        if not rec:
            continue
        if _tok_tuple(exp["value"]) != _tok_tuple(rec["value"]):
            problems30.append(
                f"category=value-mismatch param={pid} expected={exp['value']!r} actual={rec['value']!r} "
                f"source=B-12 parameter register inventory_line={rec['line']}")
    b02_actual = {r["name"]: r for r in inv["b02"]}
    for name, tokens, _unit, _status, _text in expected_b02():
        rec = b02_actual.get(name)
        if rec and tokens and tuple(sorted(tokens)) != _tok_tuple(rec["value"]):
            problems30.append(
                f"category=value-mismatch param={name!r} expected={sorted(tokens)} actual={list(_tok_tuple(rec['value']))} "
                f"source=B-02 §3 inventory_line={rec['line']}")
        if rec and _text and _text not in rec["value"]:
            problems30.append(
                f"category=value-mismatch param={name!r} expected={_text!r} actual={rec['value']!r} "
                f"source=B-02 §3 inventory_line={rec['line']}")
    # B-03 values are checked exactly by 14A-11; include record-level detail here too
    for i, (src, mir) in enumerate(zip(parse_b03_rows(text("B03")), parse_param_b03(params_text)), 1):
        if norm(src["value"]) != norm(mir["value"]):
            problems30.append(
                f"category=value-mismatch param=B-03 row {i} expected={norm(src['value'])!r} actual={norm(mir['value'])!r} "
                f"source=B-03 §21.2 inventory_line=<B-03 table row {i}>")
    add("14A-30", "Every parameter value agrees with its authoritative source", problems30)

    # 31 — units
    problems31 = []
    for key, expected_list in exp_const.items():
        actual_list = act_groups.get(key, [])
        for exp, rec in zip(expected_list, actual_list):
            unit = norm(exp.get("unit", "")).lower()
            if unit and unit not in ("—", "-"):
                actual_unit = norm(rec["unit"]).lower()
                if unit not in actual_unit:
                    problems31.append(
                        f"category=unit-mismatch param={key[1]!r} expected={exp['unit']!r} actual={rec['unit']!r} "
                        f"source={key[0]} inventory_line={rec['line']}")
    b02_actual = {r["name"]: r for r in inv["b02"]}
    for name, _tokens, unit, _status, _text in expected_b02():
        rec = b02_actual.get(name)
        if rec and norm(unit).lower() not in norm(rec["unit"]).lower():
            problems31.append(
                f"category=unit-mismatch param={name!r} expected={unit!r} actual={rec['unit']!r} "
                f"source=B-02 §3 inventory_line={rec['line']}")
    for fid, rec in act_form.items():
        if not rec["unit"]:
            problems31.append(f"category=unit-missing param={fid} expected=explicit unit or marker actual=empty source={rec['source']} inventory_line={rec['line']}")
    for pid, rec in fp_actual.items():
        if not rec["unit"]:
            problems31.append(f"category=unit-missing param={pid} expected=explicit unit or marker actual=empty source=B-12 inventory_line={rec['line']}")
    add("14A-31", "Every parameter unit agrees with its source or carries a marker", problems31)

    # 32 — status, authority and owner-reserved state
    problems32 = []
    for fid, exp in exp_form.items():
        rec = act_form.get(fid)
        if not rec:
            continue
        if rec["status"] != exp["status"]:
            problems32.append(
                f"category=status-mismatch param={fid} expected={exp['status']} actual={rec['status']} "
                f"source={exp['source']} inventory_line={rec['line']}")
        if not _norm_auth(rec["auth"]).startswith(_norm_auth(exp["auth"])[:25]):
            problems32.append(
                f"category=authority-mismatch param={fid} expected={exp['auth'][:80]!r} actual={rec['auth'][:80]!r} "
                f"source={exp['source']} inventory_line={rec['line']}")
        if rec["reserved"] != exp["reserved"]:
            problems32.append(
                f"category=owner-reserved-mismatch param={fid} expected={exp['reserved']!r} actual={rec['reserved']!r} "
                f"source={exp['source']} inventory_line={rec['line']}")
    for pid, exp in exp_fp.items():
        rec = fp_actual.get(pid)
        if not rec:
            continue
        if rec["status"] != exp["status"]:
            problems32.append(
                f"category=status-mismatch param={pid} expected={exp['status']} actual={rec['status']} "
                f"source=B-12 parameter register inventory_line={rec['line']}")
        if not _norm_auth(rec["auth"]).startswith(_norm_auth(exp["auth"])[:20]):
            problems32.append(
                f"category=authority-mismatch param={pid} expected={exp['auth']!r} actual={rec['auth']!r} "
                f"source=B-12 parameter register inventory_line={rec['line']}")
        if rec["reserved"] != exp["reserved"]:
            problems32.append(
                f"category=owner-reserved-mismatch param={pid} expected={exp['reserved']!r} actual={rec['reserved']!r} "
                f"source=B-12 parameter register inventory_line={rec['line']}")
    for rec in inv["formulas"] + inv["fp"] + inv["constants"] + inv["b02"]:
        if rec.get("status", "").startswith("OWNER-APPROVED"):
            blob = " ".join(str(v) for v in rec.values())
            if not re.search(r"D-\d{3}", blob) and "Fixed constraint" not in blob and "Fixed by B-02" not in blob:
                problems32.append(
                    f"category=false-owner-approved param={rec.get('id') or rec.get('name')} expected=decision citation actual=none "
                    f"source={rec.get('source', 'B-02')} inventory_line={rec['line']}")
    add("14A-32", "Status, decision authority and owner-reserved state match the source", problems32)

    # 33 — source references, timing and rounding metadata
    problems33 = []
    for fid, exp in exp_form.items():
        rec = act_form.get(fid)
        if not rec:
            continue
        if norm(rec["source"]) != norm(exp["source"]):
            problems33.append(
                f"category=source-mismatch param={fid} expected={exp['source']!r} actual={rec['source']!r} "
                f"source={exp['source']} inventory_line={rec['line']}")
        if exp["timing"]:
            if not rec["timing"].lower().startswith(exp["timing"][:20].lower()):
                problems33.append(
                    f"category=timing-mismatch param={fid} expected={exp['timing'][:80]!r} actual={rec['timing'][:80]!r} "
                    f"source={exp['source']} inventory_line={rec['line']}")
        elif "Not specified" not in rec["timing"]:
            problems33.append(
                f"category=timing-mismatch param={fid} expected='Not specified' actual={rec['timing'][:60]!r} "
                f"source={exp['source']} inventory_line={rec['line']}")
        if exp["rounding"]:
            if not rec["prec"].lower().startswith(exp["rounding"][:20].lower()):
                problems33.append(
                    f"category=rounding-mismatch param={fid} expected={exp['rounding'][:80]!r} actual={rec['prec'][:80]!r} "
                    f"source={exp['source']} inventory_line={rec['line']}")
        elif "Not specified" not in rec["prec"]:
            problems33.append(
                f"category=rounding-mismatch param={fid} expected='Not specified' actual={rec['prec'][:60]!r} "
                f"source={exp['source']} inventory_line={rec['line']}")
    for rec in inv["constants"]:
        if not rec["prec"] or not rec["timing"] or not rec["source"]:
            problems33.append(
                f"category=metadata-missing param={rec['name']!r} expected=source+precision+timing actual=empty "
                f"source={rec['source'] or '<empty>'} inventory_line={rec['line']}")
    if "B-12 does not state per-parameter rounding or timing" not in params_text:
        problems33.append(
            "category=metadata-marker param=<B-12> expected=explicit missing-data note actual=missing source=B-12 parameter register inventory_line=<section 14>")
    add("14A-33", "Source references, timing and rounding metadata are source-backed", problems33)

    # 34 — evidence, owner-reserved and playtesting visibility
    problems34 = []
    for rec in inv["fp"]:
        if any(w in rec["evidence"].lower() for w in ("satisfied", "approved", "passed")):
            problems34.append(
                f"category=false-evidence param={rec['id']} expected=evidence requirement actual={rec['evidence']!r} "
                f"source=B-12 inventory_line={rec['line']}")
    fp07 = fp_actual.get("FP-P07")
    if fp07 and fp07["status"] != "NEEDS PLAYTESTING":
        problems34.append(
            f"category=playtesting-status param=FP-P07 expected=NEEDS PLAYTESTING actual={fp07['status']} "
            f"source=B-12 inventory_line={fp07['line']}")
    fp11 = fp_actual.get("FP-P11")
    if fp11 and not any(w in fp11["auth"].lower() for w in ("counsel", "legal", "owner")):
        problems34.append(
            f"category=authority-mismatch param=FP-P11 expected=owner/counsel actual={fp11['auth']!r} "
            f"source=B-12 inventory_line={fp11['line']}")
    for i, mir in enumerate(inv["b03"], 1):
        if mir["reserved"].lower().startswith("yes"):
            problems34.append(
                f"category=owner-reserved-mismatch param=B-03 row {i} expected=not owner-reserved actual={mir['reserved']!r} "
                f"source=B-03 §21.2 inventory_line={mir['line']}")
    add("14A-34", "Evidence requirements, owner-reserved state and playtesting needs are visible", problems34)

    # 36 — constant-row metadata (authority, timing, status)
    problems36 = []
    for rec in inv["constants"]:
        m = re.match(r"(B-\d{2})\s*§(\S+)", rec["source"])
        if not m:
            problems36.append(f"category=source-unparseable param={rec['name']!r} expected='B-xx §x' actual={rec['source']!r} source={rec['source']} inventory_line={rec['line']}")
            continue
        system, sec = m.group(1), m.group(2)
        meta = CONST_META.get(system, {}).get(sec)
        if not meta:
            problems36.append(f"category=metadata-uncovered param={rec['name']!r} expected=section metadata actual=none source={rec['source']} inventory_line={rec['line']}")
            continue
        timing, authority = meta
        if not _norm_auth(rec["auth"]).startswith(_norm_auth(authority)[:25]):
            problems36.append(f"category=authority-mismatch param={rec['name']!r} expected={authority!r} actual={rec['auth']!r} source={rec['source']} inventory_line={rec['line']}")
        if not rec["timing"].lower().startswith(timing[:18].lower()):
            problems36.append(f"category=timing-mismatch param={rec['name']!r} expected={timing!r} actual={rec['timing']!r} source={rec['source']} inventory_line={rec['line']}")
        if rec["status"] != "PROVISIONAL VALUE":
            problems36.append(f"category=status-mismatch param={rec['name']!r} expected=PROVISIONAL VALUE actual={rec['status']!r} source={rec['source']} inventory_line={rec['line']}")
    add("14A-36", "Constant-table metadata (authority, timing, status) matches the B-14 convention", problems36)

    # 37 — B-02 turn-model metadata
    problems37 = []
    for rec in inv["b02"]:
        meta = B02_META.get(rec["name"])
        if not meta:
            problems37.append(f"category=metadata-uncovered param={rec['name']!r} expected=B-02 row metadata actual=none source=B-02 inventory_line={rec['line']}")
            continue
        status_prefix, auth_kw = meta
        if not rec["status"].startswith(status_prefix):
            problems37.append(f"category=status-mismatch param={rec['name']!r} expected={status_prefix} actual={rec['status']!r} source=B-02 §3 inventory_line={rec['line']}")
        if auth_kw.lower() not in rec["auth"].lower():
            problems37.append(f"category=authority-mismatch param={rec['name']!r} expected={auth_kw!r} actual={rec['auth']!r} source=B-02 §3 inventory_line={rec['line']}")
    add("14A-37", "B-02 turn-model status and authority are preserved", problems37)

    # 38 — B-03 unit, evidence text and evidence classification
    problems38 = []
    src_rows = parse_b03_rows(text("B03"))
    for i, (src, mir) in enumerate(zip(src_rows, inv["b03"]), 1):
        expected_units = _b03_unit_words(src.get("value", ""))
        actual_units = _b03_unit_words(mir["unit"])
        for u in expected_units:
            if u not in actual_units:
                problems38.append(f"category=unit-mismatch param=B-03 row {i} expected={u!r} actual={mir['unit']!r} source=B-03 §21.2 inventory_line={mir['line']}")
        if norm(src.get("evidence", "")) != norm(mir.get("evidence", "")):
            problems38.append(f"category=evidence-mismatch param=B-03 row {i} expected={norm(src.get('evidence',''))!r} actual={norm(mir.get('evidence',''))!r} source=B-03 §21.2 inventory_line={mir['line']}")
        if any(bad in mir.get("evidence", "").lower() for bad in ("already satisfied", "confirmed", "approved", "passed")):
            problems38.append(f"category=evidence-fabricated param=B-03 row {i} expected=requirement text actual={mir.get('evidence','')!r} source=B-03 §21.2 inventory_line={mir['line']}")
        key = norm(src.get("name", ""))
        expected_cls = B03_CLASS.get(key)
        if expected_cls is None:
            problems38.append(f"category=evidence-class-unmapped param={key!r} expected=derived class actual=none source=B-03 §21.2 inventory_line={mir['line']}")
        elif mir.get("cls", "") != expected_cls:
            problems38.append(f"category=evidence-class-mismatch param={key!r} expected={expected_cls!r} actual={mir.get('cls','')!r} source=B-03 §21.2 inventory_line={mir['line']}")
    add("14A-38", "B-03 units, evidence requirements and derived evidence classes are preserved", problems38)

    # 39 — formula and FP unit source validation
    problems39 = []
    fp_actual = {r["id"]: r for r in inv["fp"]}
    for fid, exp in exp_form.items():
        rec = act_form.get(fid)
        if not rec:
            continue
        if not exp.get("unit_field_present"):
            problems39.append(f"category=source-field-unparseable param={fid} expected=units/output/variables field actual=absent source={exp['source']} inventory_line={rec['line']}")
            continue
        expected_tokens = _unit_tokens_r1(exp.get("unit_source", ""))
        actual_tokens = _unit_tokens_r1(rec["unit"])
        if expected_tokens:
            if expected_tokens != actual_tokens:
                problems39.append(f"category=unit-mismatch param={fid} expected={sorted(expected_tokens)} actual={sorted(actual_tokens)} source={exp['source']} inventory_line={rec['line']}")
        else:
            if "not specified" not in rec["unit"].lower():
                problems39.append(f"category=unit-mismatch param={fid} expected='NOT SPECIFIED IN SOURCE' actual={rec['unit']!r} source={exp['source']} inventory_line={rec['line']}")
    for pid, rec in fp_actual.items():
        actual_tokens = _unit_tokens_r1(rec["unit"])
        if not actual_tokens:
            problems39.append(f"category=unit-mismatch param={pid} expected=source-supported unit actual={rec['unit']!r} source=B-12 parameter register inventory_line={rec['line']}")
        if pid == "FP-P07":
            used = rec["used"].strip("`").split(",")[0].strip()
            exp = exp_form.get(used)
            expected_tokens = _unit_tokens_r1(exp.get("unit_source", "")) if exp else set()
            if expected_tokens and not expected_tokens.issubset(actual_tokens):
                problems39.append(f"category=unit-mismatch param=FP-P07 expected={sorted(expected_tokens)} actual={sorted(actual_tokens)} source={used} inventory_line={rec['line']}")
    add("14A-39", "Formula and B-12 units are source-validated or explicitly marked", problems39)

    # 40 — coverage totals
    problems40 = []
    expected_counts = {"B-02": 7, "B-03": 20, "B-04": 49, "B-05": 73, "B-06": 96, "B-07": 26,
                       "B-08": 12, "B-09": 8, "B-10": 39, "B-11": 49, "B-12": 14}
    actual_counts = {"B-02": len(inv["b02"]), "B-03": len(inv["b03"]), "B-12": len(inv["fp"])}
    for system in ("B-04", "B-05", "B-06", "B-07"):
        actual_counts[system] = sum(1 for r in inv["constants"] if r["source"].startswith(system + " "))
    for system in ("B-08", "B-09", "B-10", "B-11"):
        actual_counts[system] = sum(1 for r in inv["formulas"] if r["source"].startswith(system + " "))
    for system, expected in expected_counts.items():
        if actual_counts.get(system) != expected:
            problems40.append(f"category=coverage-count param={system} expected={expected} actual={actual_counts.get(system)} source=canonical registers inventory_line=<section>")
    if sum(actual_counts.values()) != 393:
        problems40.append(f"category=coverage-count param=<total> expected=393 actual={sum(actual_counts.values())} source=canonical registers inventory_line=<document>")
    add("14A-40", "All 393 records are covered by source-specific adapters", problems40)

    # 42 — constant-table precision/rounding convention
    problems42 = []
    for system, (anchor1, anchor2) in PRECISION_ANCHORS.items():
        src = text("REG_" + system)
        if anchor1 not in src or anchor2 not in src:
            problems42.append(
                f"category=source-convention-unparseable param=<{system} constants> expected={anchor1!r}+{anchor2!r} actual=missing "
                f"source={FILES['REG_' + system]} inventory_line=<register convention>")
    for rec in inv["constants"]:
        system = rec["source"].split()[0]
        expected = PRECISION_CONVENTION.get(system)
        if not expected:
            problems42.append(
                f"category=precision-uncovered param={rec['name']!r} expected=register convention actual=none "
                f"source={rec['source']} inventory_line={rec['line']}")
            continue
        if not rec["prec"]:
            problems42.append(
                f"category=precision-missing param={rec['name']!r} expected={expected!r} actual=<empty> "
                f"source={rec['source']} inventory_line={rec['line']}")
        elif rec["prec"] != expected:
            problems42.append(
                f"category=precision-mismatch param={rec['name']!r} expected={expected!r} actual={rec['prec']!r} "
                f"source={rec['source']} inventory_line={rec['line']}")
    add("14A-42", "B-04…B-07 constant precision/rounding matches the source convention", problems42)

    # 43 — owner-reserved field across applicable records
    problems43 = []
    for rec in inv["constants"]:
        if rec["reserved"] != "No":
            problems43.append(
                f"category=owner-reserved-mismatch param={rec['name']!r} expected='No' actual={rec['reserved']!r} "
                f"source={rec['source']} inventory_line={rec['line']}")
    for fid, exp in exp_form.items():
        rec = act_form.get(fid)
        if not rec:
            continue
        expected = exp.get("owner_reserved_expected", "No")
        if rec["reserved"] != expected:
            problems43.append(
                f"category=owner-reserved-mismatch param={fid} expected={expected!r} actual={rec['reserved']!r} "
                f"source={exp['source']} inventory_line={rec['line']}")
    for pid, rec in fp_actual.items():
        src_exp = exp_fp.get(pid)
        if not src_exp or not src_exp.get("auth"):
            problems43.append(
                f"category=owner-authority-ambiguous param={pid} expected=owner field actual=<empty> "
                f"source=B-12 parameter register inventory_line={rec['line']}")
            continue
        expected = "Yes — owner-reserved" if "Owner" in src_exp["auth"] else "No"
        if rec["reserved"] != expected:
            problems43.append(
                f"category=owner-reserved-mismatch param={pid} expected={expected!r} actual={rec['reserved']!r} "
                f"source=B-12 parameter register inventory_line={rec['line']}")
    for i, rec in enumerate(inv["b03"], 1):
        if not rec["reserved"]:
            problems43.append(
                f"category=owner-authority-ambiguous param=B-03 row {i} expected=No or No-with-dependency actual=<empty> "
                f"source=B-03 §21.2 inventory_line={rec['line']}")
        elif not rec["reserved"].startswith("No"):
            problems43.append(
                f"category=owner-reserved-mismatch param=B-03 row {i} expected=No (legal dependency may be noted) actual={rec['reserved']!r} "
                f"source=B-03 §21.2 inventory_line={rec['line']}")
    add("14A-43", "Owner-reserved flags match source authority for every applicable record", problems43)

    # 44 — Prompt 14A-C1-R1-R1 archive and index
    problems44 = []
    rrarchives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1_") and f.endswith(".md")]
    if len(rrarchives) != 1:
        problems44.append(f"expected one prompt_14A-C1-R1-R1_*.md archive, found {rrarchives}")
    else:
        rrpath = os.path.join(PROMPTS, rrarchives[0])
        index = text("INDEX")
        if rrarchives[0] not in index:
            problems44.append("R1-R1 archive filename not recorded in INDEX.md")
        rrdigest = sha256_file(rrpath)
        if rrdigest not in index:
            problems44.append("R1-R1 archive SHA-256 not recorded in INDEX.md")
        rrsize = os.path.getsize(rrpath)
        if str(rrsize) not in index and "{:,}".format(rrsize) not in index:
            problems44.append("R1-R1 archive byte count not recorded in INDEX.md")
    add("14A-44", "The Prompt 14A-C1-R1-R1 correction archive is present and indexed", problems44)

    # 47 — Prompt 14A-C1-R1-R1-C1 archive and index
    problems47 = []
    farchives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1-C1_") and f.endswith(".md")]
    if len(farchives) != 1:
        problems47.append(f"expected one prompt_14A-C1-R1-R1-C1_*.md archive, found {farchives}")
    else:
        fpath = os.path.join(PROMPTS, farchives[0])
        index = text("INDEX")
        if farchives[0] not in index:
            problems47.append("final C1 archive filename not recorded in INDEX.md")
        fdigest = sha256_file(fpath)
        if fdigest not in index:
            problems47.append("final C1 archive SHA-256 not recorded in INDEX.md")
        fsize = os.path.getsize(fpath)
        if str(fsize) not in index and "{:,}".format(fsize) not in index:
            problems47.append("final C1 archive byte count not recorded in INDEX.md")
    add("14A-47", "The Prompt 14A-C1-R1-R1-C1 archive is present and indexed", problems47)




    # 45/46 — B-04 source semantic contracts and amendment authorization
    b04_text = text("REG_B-04")
    decisions_text = text("DECISIONS")
    manifest_text = text("B04_AMENDMENTS")
    for idx, fid in enumerate(("F-EC-000b", "F-EC-000f"), start=45):
        problems = _validate_source_contract(fid, b04_text, decisions_text, manifest_text)
        add(f"14A-{idx}", f"{fid} normative source contract and amendment authority are preserved", problems)

    # 48 — controlled amendment manifest structure
    problems48 = []
    manifest = _load_manifest(manifest_text)
    if manifest is None:
        problems48.append("category=manifest-unparseable param=<B-04 contracts> expected=valid JSON actual=parse error source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<manifest>")
    else:
        for fid, contract in B04_CONTRACT.items():
            base = manifest.get("baseline", {}).get(fid, {})
            if base.get("hash") != contract["hash"]:
                problems48.append(f"category=manifest-baseline-mismatch param={fid} expected={contract['hash']} actual={base.get('hash')!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<baseline>")
        for i, a in enumerate(manifest.get("amendments", []), 1):
            for field in ("clause", "source_document", "previous_hash", "new_hash", "decision_id", "category", "decision_status", "authorization_evidence", "rationale", "regression_evidence"):
                if not a.get(field):
                    problems48.append(f"category=manifest-entry-incomplete param=amendment {i} expected={field} actual=empty source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
            if a.get("clause") not in B04_CONTRACT:
                problems48.append(f"category=manifest-clause param=amendment {i} expected=F-EC-000b or F-EC-000f actual={a.get('clause')!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
            for hf in ("previous_hash", "new_hash"):
                if a.get(hf) and not re.fullmatch(r"[0-9a-f]{64}", str(a.get(hf))):
                    problems48.append(f"category=manifest-hash-format param=amendment {i} expected=64 hex actual={a.get(hf)!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    add("14A-48", "The controlled B-04 amendment manifest is structurally valid", problems48)

    # 49 — Prompt 14A-C1-R1-R1-C1-R1 archive and index
    problems49 = []
    r1archives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1-C1-R1_") and f.endswith(".md")]
    if len(r1archives) != 1:
        problems49.append(f"expected one prompt_14A-C1-R1-R1-C1-R1_*.md archive, found {r1archives}")
    else:
        r1path = os.path.join(PROMPTS, r1archives[0])
        index = text("INDEX")
        if r1archives[0] not in index:
            problems49.append("closure archive filename not recorded in INDEX.md")
        r1digest = sha256_file(r1path)
        if r1digest not in index:
            problems49.append("closure archive SHA-256 not recorded in INDEX.md")
        r1size = os.path.getsize(r1path)
        if str(r1size) not in index and "{:,}".format(r1size) not in index:
            problems49.append("closure archive byte count not recorded in INDEX.md")
    add("14A-49", "The Prompt 14A-C1-R1-R1-C1-R1 closure archive is present and indexed", problems49)

    # 50 — decision table structural integrity
    problems50 = []
    headers, records, malformed, dupes = _decision_table(text("DECISIONS"))
    if not headers:
        problems50.append("category=decision-table-header param=<DECISIONS> expected=8-column header actual=missing source=DECISIONS.md inventory_line=<header>")
    elif len(headers) != 8:
        problems50.append(f"category=decision-table-header param=<DECISIONS> expected=8 columns actual={len(headers)} source=DECISIONS.md inventory_line=<header>")
    for did, got, want in malformed:
        if got > want:
            problems50.append(f"category=decision-row-overlong param={did} expected={want} cells actual={got} source=DECISIONS.md inventory_line={did}")
        # Short legacy decision rows are not eligible for amendment validation;
        # a target amendment row with fewer than eight cells fails 14A-45/46 as missing.
    for did in dupes:
        problems50.append(f"category=decision-id-duplicate param={did} expected=unique actual=duplicate source=DECISIONS.md inventory_line={did}")
    add("14A-50", "The DECISIONS.md table is structurally valid and IDs are unique", problems50)

    # 51 — Prompt 14A-C1-R1-R1-C1-R1-C1 archive and index
    problems51 = []
    carchives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1-C1-R1-C1_") and f.endswith(".md")]
    if len(carchives) != 1:
        problems51.append(f"expected one prompt_14A-C1-R1-R1-C1-R1-C1_*.md archive, found {carchives}")
    else:
        cpath = os.path.join(PROMPTS, carchives[0])
        index = text("INDEX")
        if carchives[0] not in index:
            problems51.append("decision-evidence archive filename not recorded in INDEX.md")
        cdigest = sha256_file(cpath)
        if cdigest not in index:
            problems51.append("decision-evidence archive SHA-256 not recorded in INDEX.md")
        csize = os.path.getsize(cpath)
        if str(csize) not in index and "{:,}".format(csize) not in index:
            problems51.append("decision-evidence archive byte count not recorded in INDEX.md")
    add("14A-51", "The final decision-evidence correction archive is present and indexed", problems51)

    # 52 — Prompt 14A-C1-R1-R1-C1-R1-C1-R1 archive and index
    problems52 = []
    earchives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1-C1-R1-C1-R1_") and f.endswith(".md")]
    if len(earchives) != 1:
        problems52.append(f"expected one prompt_14A-C1-R1-R1-C1-R1-C1-R1_*.md archive, found {earchives}")
    else:
        epath = os.path.join(PROMPTS, earchives[0])
        index = text("INDEX")
        if earchives[0] not in index:
            problems52.append("evidence-relevance archive filename not recorded in INDEX.md")
        edigest = sha256_file(epath)
        if edigest not in index:
            problems52.append("evidence-relevance archive SHA-256 not recorded in INDEX.md")
        esize = os.path.getsize(epath)
        if str(esize) not in index and "{:,}".format(esize) not in index:
            problems52.append("evidence-relevance archive byte count not recorded in INDEX.md")
    add("14A-52", "The final evidence-relevance correction archive is present and indexed", problems52)

    # 53 — Prompt 14A-C1-R1-R1-C1-R1-C1-R1-R1 archive and index
    problems53 = []
    carchives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1-C1-R1-C1-R1-R1_") and f.endswith(".md")]
    if len(carchives) != 1:
        problems53.append(f"expected one prompt_14A-C1-R1-R1-C1-R1-C1-R1-R1_*.md archive, found {carchives}")
    else:
        cpath = os.path.join(PROMPTS, carchives[0])
        index = text("INDEX")
        if carchives[0] not in index:
            problems53.append("contradiction-correction archive filename not recorded in INDEX.md")
        cdigest = sha256_file(cpath)
        if cdigest not in index:
            problems53.append("contradiction-correction archive SHA-256 not recorded in INDEX.md")
        csize = os.path.getsize(cpath)
        if str(csize) not in index and "{:,}".format(csize) not in index:
            problems53.append("contradiction-correction archive byte count not recorded in INDEX.md")
    add("14A-53", "The final contamination-correction archive is present and indexed", problems53)

    # 54 — controlled B-04 semantic contract coverage
    problems54 = []
    for fid in ("F-EC-000b", "F-EC-000f"):
        clause = _extract_b04_clause(b04_text, fid)
        if not clause:
            problems54.append(f"category=semantic-contract param={fid} expected=clause present actual=missing source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
            continue
        sem = _semantic_contract_violation(fid, clause)
        if sem:
            problems54.append(f"category=semantic-contract param={fid} expected=controlled semantic contract actual={sem} source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
    add("14A-54", "Both controlled B-04 clauses satisfy the complete semantic contract", problems54)

    # 55 — Prompt 14A-C1-R1-R1-C1-R1-C1-R1-R1-R1 archive and index
    problems55 = []
    carchives = [f for f in os.listdir(PROMPTS) if f.startswith("prompt_14A-C1-R1-R1-C1-R1-C1-R1-R1-R1_") and f.endswith(".md")]
    if len(carchives) != 1:
        problems55.append(f"expected one prompt_14A-C1-R1-R1-C1-R1-C1-R1-R1-R1_*.md archive, found {carchives}")
    else:
        cpath = os.path.join(PROMPTS, carchives[0])
        index = text("INDEX")
        if carchives[0] not in index:
            problems55.append("semantic-contract archive filename not recorded in INDEX.md")
        cdigest = sha256_file(cpath)
        if cdigest not in index:
            problems55.append("semantic-contract archive SHA-256 not recorded in INDEX.md")
        csize = os.path.getsize(cpath)
        if str(csize) not in index and "{:,}".format(csize) not in index:
            problems55.append("semantic-contract archive byte count not recorded in INDEX.md")
    add("14A-55", "The final semantic-contract correction archive is present and indexed", problems55)

    # 56–64 — controlled numerical-contract architecture (D-238)
    report = _contract_report()
    contract_mod = _contract_module()
    contract_checks = {c["id"]: c for c in report.get("checks", [])}

    def contract_problems(check_id):
        check = contract_checks.get(check_id)
        if not check:
            return [f"category=contract-missing check={check_id} actual=absent source=docs/stage-2/22_numerical_contracts inventory_line=<contract>"]
        return [f"category=contract-{check_id.lower()} {contract_mod.fmt(p)} source=docs/stage-2/22_numerical_contracts inventory_line=<contract>"
                for p in check.get("problems", [])]

    add("14A-56", "The controlled contract registry, strict schema and closed lexicon validate", contract_problems("C-01"))
    add("14A-57", "Both controlled contracts satisfy the typed proposition schema and semantic rules", contract_problems("C-02"))
    add("14A-58", "B-04 projections match the preserved clauses with 100% material coverage", contract_problems("C-03"))
    add("14A-59", "Contract, projection and source fingerprints are recomputed deterministically", contract_problems("C-04"))
    add("14A-60", "Evidence mappings are source-verified, scoped and honestly unreviewed", contract_problems("C-05"))
    add("14A-61", "D-014 authority, adoption decision and owner-authorization provenance are enforced", contract_problems("C-06"))
    add("14A-62", "Evidence and authority gates operate independently on the mandatory regression matrix", contract_problems("C-07"))
    problems63 = contract_problems("C-08")
    archive_name = "prompt_14A_semantic_contract_implementation.md"
    archive_path = os.path.join(PROMPTS, archive_name)
    archive_index = text("INDEX")
    if not os.path.isfile(archive_path):
        problems63.append(f"category=contract-archive param={archive_name} expected=archive present actual=missing source=docs/prompts inventory_line=<archive>")
    else:
        if archive_name not in archive_index:
            problems63.append(f"category=contract-archive param={archive_name} expected=indexed actual=absent source=docs/prompts/INDEX.md inventory_line=<row>")
        archive_digest = sha256_file(archive_path)
        if archive_digest not in archive_index:
            problems63.append(f"category=contract-archive param={archive_name} expected=SHA-256 {archive_digest} actual=absent source=docs/prompts/INDEX.md inventory_line=<row>")
        archive_size = os.path.getsize(archive_path)
        if str(archive_size) not in archive_index and "{:,}".format(archive_size) not in archive_index:
            problems63.append(f"category=contract-archive param={archive_name} expected={archive_size} bytes actual=absent source=docs/prompts/INDEX.md inventory_line=<row>")
    add("14A-63", "Contract scope is isolated from B-09 and the numerical foundation is preserved", problems63)
    add("14A-64", "Contract validation is deterministic, offline and standard-library only", contract_problems("C-09"))

    return results


# ----------------------------------------------------------------------------
# self-tests
# ----------------------------------------------------------------------------
def _replace_row(text, fid, col, value):
    out = []
    for line in text.splitlines():
        if line.strip().startswith("| `" + fid + "`"):
            cells = split_row(line)
            if col < len(cells):
                cells[col] = value
                out.append("| " + " | ".join(cells) + " |")
                continue
        out.append(line)
    return "\n".join(out)


def _insert_after_row(text, anchor, new_row):
    out = []
    inserted = False
    for line in text.splitlines():
        out.append(line)
        if not inserted and line.strip().startswith("| `" + anchor + "`"):
            out.append(new_row)
            inserted = True
    return "\n".join(out)


def _drop_row(text, fid):
    return "\n".join(l for l in text.splitlines() if not l.strip().startswith("| `" + fid + "`"))


def _checks(results):
    return {cid: problems for cid, _, problems in results}



def _replace_param_named(text, name, col, value, source_prefix=None):
    out = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = split_row(line)
            if (len(cells) == 14 and cells[0] == "None" and cells[1] == name
                    and (source_prefix is None or cells[4].startswith(source_prefix))):
                cells[col] = value
                out.append("| " + " | ".join(cells) + " |")
                continue
        out.append(line)
    return "\n".join(out)


def _clear_formula_rounding(text, fid):
    out = []
    inside = False
    for line in text.splitlines():
        if line.startswith("### "):
            inside = line.startswith("### " + fid)
        if inside and re.match(r"^\|\s*7\s*\|\s*Rounding\s*\|", line):
            out.append("| 7 | Rounding |  |")
            continue
        out.append(line)
    return "\n".join(out)



def _replace_b03_row(text, name, col, value):
    out = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = split_row(line)
            if len(cells) == 8 and cells[1].replace("`", "").strip() == name.replace("`", "").strip():
                cells[col] = value
                out.append("| " + " | ".join(cells) + " |")
                continue
        out.append(line)
    return "\n".join(out)


def _replace_b02_row(text, name, col, value):
    out = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = split_row(line)
            if len(cells) == 7 and cells[0] == name:
                cells[col] = value
                out.append("| " + " | ".join(cells) + " |")
                continue
        out.append(line)
    return "\n".join(out)


def _remove_formula_field(text, fid, fieldnum):
    out = []
    inside = False
    for line in text.splitlines():
        if line.startswith("### "):
            inside = line.startswith("### " + fid)
        if inside and re.match(r"^\|\s*" + str(fieldnum) + r"\s*\|", line):
            continue
        out.append(line)
    return "\n".join(out)



def _remove_line_containing(text, needle):
    return "\n".join(l for l in text.splitlines() if needle not in l)


def _replace_fp_source_owner(text, pid, value):
    out = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = split_row(line)
            if len(cells) >= 6 and pid in cells[0]:
                cells[4] = value
                out.append("| " + " | ".join(cells) + " |")
                continue
        out.append(line)
    return "\n".join(out)



def _extract_b04_clause(text, fid):
    for para in text.split("\n\n"):
        if para.strip().startswith("**" + fid):
            return para.strip()
    return ""


def _norm_contract(text):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", lambda m: m.group(1), text or "")
    s = s.replace("**", "").replace("*", "").replace("`", "")
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()



def _replace_text(text, old, new):
    return text.replace(old, new, 1)


def _load_manifest(text):
    try:
        return json.loads(text)
    except Exception:
        return None


def _decision_row(decisions_text, did):
    for line in decisions_text.splitlines():
        m = re.match(r"^\|\s*(D-[0-9]{3})\s*\|", line)
        if m and m.group(1) == did:
            return line
    return ""


def _decision_authorized(row, category, owner_reserved):
    low = row.lower()
    if any(w in low for w in ("pending", "proposed", "rejected", "deferred", "superseded", "not approved")):
        return False, "decision is pending, proposed, rejected, deferred, superseded or not approved"
    if category == "B":
        if owner_reserved:
            return False, "owner-reserved amendment cannot be authorized by a Category B decision"
        if "confirmed" not in low:
            return False, "Category B decision is not Confirmed"
    elif category in ("A", "D"):
        if not any(w in low for w in ("owner-approved", "owner approved", "owner authorized", "owner accepted")):
            return False, "Category A/D amendment lacks explicit owner authorization"
    elif category == "C":
        if "provisional" not in low:
            return False, "Category C decision is not Provisional"
    else:
        return False, "invalid D-014 category"
    return True, ""


def _validate_source_contract(fid, source_text, decisions_text, manifest_text):
    problems = []
    clause = _extract_b04_clause(source_text, fid)
    contract = B04_CONTRACT[fid]
    if not clause:
        return [f"category=source-contract-missing param={fid} expected=clause present actual=missing "
                f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>"]
    normalized = _norm_contract(clause)
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    contract_mod = _contract_module()
    artifacts = contract_mod.load_artifacts()
    base_contract = artifacts["contracts"].get(fid)
    ingest = contract_mod.ingest_clause(base_contract, clause, artifacts["lexicon"])
    for prob in ingest["problems"]:
        problems.append(f"category=semantic-contract param={fid} expected=controlled typed contract actual={contract_mod.fmt(prob)} "
                        f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
    manifest = _load_manifest(manifest_text)
    if manifest is None:
        return [f"category=manifest-unparseable param={fid} expected=valid JSON actual=parse error "
                f"source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<manifest>"]
    amendments = [a for a in manifest.get("amendments", []) if a.get("clause") == fid]
    if digest == contract["hash"]:
        for a in amendments:
            problems.append(
                f"category=amendment-without-source-change param={fid} expected=no amendment entry actual={a.get('decision_id')!r} "
                f"source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendments>")
        low = normalized.lower()
        for phrase in contract["required"]:
            if phrase.lower() not in low:
                problems.append(f"category=source-semantic-missing param={fid} expected={phrase!r} actual=missing "
                                f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
        for phrase in contract["forbidden"]:
            if phrase.lower() in low:
                problems.append(f"category=source-semantic-forbidden param={fid} expected={phrase!r} absent actual=present "
                                f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
        return problems
    if len(amendments) != 1:
        problems.append(f"category=amendment-unauthorized param={fid} expected=one authorized amendment actual={len(amendments)} "
                        f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
        return problems
    a = amendments[0]
    required = ["source_document", "clause", "previous_hash", "new_hash", "decision_id", "category",
                "decision_status", "authorization_evidence", "rationale", "regression_evidence"]
    for field in required:
        if not a.get(field):
            problems.append(f"category=amendment-evidence-missing param={fid} expected={field} actual=empty "
                            f"source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    if a.get("source_document") != "docs/stage-2/10_economic_formula_and_balance_register.md":
        problems.append(f"category=amendment-source-mismatch param={fid} expected=docs/stage-2/10_economic_formula_and_balance_register.md "
                        f"actual={a.get('source_document')!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    if a.get("previous_hash") != contract["hash"]:
        problems.append(f"category=amendment-previous-hash param={fid} expected={contract['hash']} actual={a.get('previous_hash')!r} "
                        f"source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    if a.get("new_hash") != digest:
        problems.append(f"category=amendment-new-hash param={fid} expected={digest} actual={a.get('new_hash')!r} "
                        f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
    decision_id = a.get("decision_id", "")
    headers, records, malformed, dupes = _decision_table(decisions_text)
    matches = [r for r in records if _decision_cell(r, "id") == decision_id]
    if len(matches) != 1:
        problems.append(f"category=amendment-decision-missing param={fid} expected=one {decision_id!r} row in DECISIONS.md actual={len(matches)} "
                        f"source=DECISIONS.md inventory_line=<decision row>")
    else:
        problems.extend(_validate_decision_record(matches[0], a, fid, contract["baseline_text"], normalized, decisions_text))
    if decision_id in dupes:
        problems.append(f"category=amendment-decision-duplicate param={fid} expected=unique {decision_id} actual=duplicate "
                        f"source=DECISIONS.md inventory_line={decision_id}")
    for phrase in a.get("required_phrases", []):
        if phrase.lower() not in normalized.lower():
            problems.append(f"category=amendment-semantic-missing param={fid} expected={phrase!r} actual=missing "
                            f"source=docs/stage-2/10_economic_formula_and_balance_register.md inventory_line=<source clause>")
    return problems



def _clause_hash(text, fid):
    return hashlib.sha256(_norm_contract(_extract_b04_clause(text, fid)).encode("utf-8")).hexdigest()


def _manifest_json(fid, new_hash, **over):
    base = json.loads(read(FILES["B04_AMENDMENTS"]))
    entry = {
        "clause": fid,
        "source_document": "docs/stage-2/10_economic_formula_and_balance_register.md",
        "previous_hash": B04_CONTRACT[fid]["hash"],
        "new_hash": new_hash,
        "decision_id": "D-900",
        "category": "B",
        "decision_status": "Confirmed",
        "authorization_evidence": "DECISIONS.md D-900 (TEST FIXTURE ONLY)",
        "rationale": "Temporary test fixture; not a project decision",
        "regression_evidence": "Self-test fixture",
        "owner_reserved": False,
    }
    entry.update(over)
    base["amendments"] = [entry]
    return json.dumps(base)


def _decision_fixture(did, clause, status="**Confirmed** (Category B; TEST FIXTURE ONLY)", source="docs/stage-2/10_economic_formula_and_balance_register.md", verb="Amends"):
    return (f"| {did} | 2026-11-13 | TEST FIXTURE ONLY — not a project decision | "
            f"{verb} {clause} in {source}; temporary authorization fixture. | {status} | Test fixture | Test only | Test only |")


DECISION_GENERIC = (
    "approved because confirmed", "n/a", "none", "tbd", "placeholder",
    "generic", "no evidence",
)


@_memo_text_parse
def _decision_table(decisions_text):
    headers = None
    records = []
    malformed = []
    counts = {}
    for line in decisions_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        if headers is None:
            low = [c.lower() for c in cells]
            if low and low[0] == "id" and "date" in low:
                headers = low
            continue
        m = re.match(r"^\|\s*(D-[0-9]{3})\s*\|", line)
        if not m:
            continue
        did = m.group(1)
        if len(cells) != len(headers):
            malformed.append((did, len(cells), len(headers)))
            continue
        records.append(dict(zip(headers, cells)))
        counts[did] = counts.get(did, 0) + 1
    dupes = sorted([d for d, c in counts.items() if c > 1])
    return headers, records, malformed, dupes


def _decision_cell(rec, key_start):
    for key, value in rec.items():
        if key.startswith(key_start):
            return value
    return ""


def _substantive(text, minimum=30):
    low = (text or "").lower().strip()
    if len(low) < minimum:
        return False
    if any(g in low for g in DECISION_GENERIC):
        return False
    if not re.search(r"[a-z]", low):
        return False
    return True


def _marker(text, label, stop_labels):
    pattern = label + r"\s*[:\-]\s*(.*?)(?=" + "|".join(stop_labels) + r"|$)"
    m = re.search(pattern, text or "", re.I | re.S)
    return (m.group(1).strip() if m else "")


def _token_overlap(a, b):
    wa = set(re.findall(r"[a-z0-9]+", (a or "").lower()))
    wb = set(re.findall(r"[a-z0-9]+", (b or "").lower()))
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / float(len(wa | wb))


def _rule_matches(text, source_text):
    a = _norm_contract(text)
    b = _norm_contract(source_text)
    if not a or not b:
        return False
    if a in b or b in a:
        return True
    return _token_overlap(a, b) >= 0.85


def _section_block(doc, section):
    token = (section or "").strip()
    if not token:
        return ""
    lines = doc.splitlines()
    if token.lower().startswith("req-"):
        for line in lines:
            if token.lower() in line.lower():
                return line
        return ""
    pat = re.compile(r"^#{1,6}\s*" + re.escape(token), re.I)
    for i, line in enumerate(lines):
        if pat.match(line) or line.startswith("**" + token):
            return "\n".join(lines[i:i + 80])
    for i, line in enumerate(lines):
        if token.lower() in line.lower():
            return "\n".join(lines[i:i + 80])
    return ""


def _perm(text, subject):
    pat = r"(?:may|can|permitted|allowed|authorized|permits)[^.]{0,60}" + subject
    pat2 = subject + r"[^.]{0,60}(?:permitted|allowed|may|can)"
    return bool(re.search(pat, text) or re.search(pat2, text))


def _proh(text, subject):
    pat = r"(?:no|not|never|prohibit|forbid|may not|must not)[^.]{0,60}" + subject
    pat2 = subject + r"[^.]{0,60}(?:not permitted|not allowed|prohibited|forbidden)"
    return bool(re.search(pat, text) or re.search(pat2, text))


def _classify_stance(fid, replacement, quote, supports):
    low_r = (replacement or "").lower()
    low_q = (quote or "").lower()
    low_s = (supports or "").lower()
    if fid == "F-EC-000b" or "floating point" in low_s:
        subject = r"floating[- ]point"
        if (_perm(low_r, subject) or _perm(low_s, subject)) and _proh(low_q, subject):
            return "contradicts", "the cited passage prohibits binary floating point while the amendment or claim permits it"
        if _proh(low_r, subject) and _perm(low_q, subject):
            return "contradicts", "the cited passage permits binary floating point while the amendment prohibits it"
    if fid == "F-EC-000f":
        if "final calibration" in low_r and "provisional calibration" in low_q:
            return "contradicts", "the cited passage classifies the constants as provisional while the amendment calls them final"
        if re.search(r"(?<!not )observed prices", low_r) and "not observed prices" in low_q:
            return "contradicts", "the cited passage denies observed-price status while the amendment asserts it"
        if re.search(r"(?<!not )balance claims", low_r) and "not balance claims" in low_q:
            return "contradicts", "the cited passage denies balance-claim status while the amendment asserts it"
    terms = (["integer", "basis point", "bp", "rounding", "floating point"] if fid == "F-EC-000b"
             else ["provisional", "calibration", "v1.0", "v1.1", "revision"])
    for term in terms:
        if term in low_s and term not in low_q:
            return "not_established", f"supports claim mentions {term!r} but the quoted evidence does not"
    m_r = re.search(r"(\d[\d,]*)\s*bp\s*=\s*100%", low_r)
    m_q = re.search(r"(\d[\d,]*)\s*bp\s*=\s*100%", low_q)
    if m_r and m_q and m_r.group(1) != m_q.group(1):
        return "contradicts", "the basis-point relationship differs from the cited evidence"
    return "supports", ""


def _evidence_supports(cell, fid, decision_id, replacement=""):
    m = re.search(r"Evidence:\s*(.*?)(?=\bRationale\b|$)", cell or "", re.I | re.S)
    if not m:
        return False, "no structured Evidence block"
    block = m.group(1)
    path_m = re.search(r"path\s*=\s*([^;]+)", block, re.I)
    section_m = re.search(r"section\s*=\s*([^;]+)", block, re.I)
    quote_m = re.search(r"quote\s*=\s*[\"“](.+?)[\"”]", block, re.I | re.S)
    supports_m = re.search(r"supports\s*=\s*([^;]+)", block, re.I)
    stance_m = re.search(r"stance\s*=\s*([a-z_]+)", block, re.I)
    if not (path_m and section_m and quote_m and supports_m and stance_m):
        return False, "Evidence block must state path, section, quote, supports and stance"
    path = path_m.group(1).strip()
    section = section_m.group(1).strip()
    quote = quote_m.group(1).strip()
    supports = supports_m.group(1).strip()
    stance = stance_m.group(1).strip().lower()
    if stance != "supports":
        return False, f"declared evidence stance is {stance!r}, not 'supports'"
    if not _substantive(quote, 20):
        return False, "evidence quote is empty, generic or too short"
    if not _substantive(supports, 15):
        return False, "evidence supports-claim is empty, generic or too short"
    allowed = B04_EVIDENCE_ALLOWED.get(fid, [])
    if not any(path == ap and (as_.lower() in section.lower() or section.lower().startswith(as_.lower()))
               for ap, as_ in allowed):
        return False, f"evidence locus is not an authorized source for {fid}: {path} section {section}"
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full = os.path.join(os.path.dirname(base), path)
    if not os.path.isfile(full):
        return False, "evidence path does not resolve: " + path
    doc = open(full, encoding="utf-8").read()
    sec = _section_block(doc, section)
    if not sec:
        return False, "evidence section does not resolve: " + section
    if _norm_contract(quote) not in _norm_contract(sec):
        return False, "quoted evidence does not appear in the cited section"
    verdict, detail = _classify_stance(fid, replacement, quote, supports)
    if verdict == "contradicts":
        return False, "evidence contradicts the proposed amendment: " + detail
    if verdict != "supports":
        return False, "evidence does not establish the proposed amendment: " + detail
    if _token_overlap(supports, quote) < 0.15 and supports.lower() not in quote.lower() and quote.lower() not in supports.lower():
        return False, "supports-claim is not substantiated by the quoted evidence"
    rationale = re.search(r"Rationale:\s*(.*)$", cell or "", re.I | re.S)
    if not rationale or not _substantive(rationale.group(1), 40):
        return False, "rationale is empty, generic or too short"
    return True, ""


def _semantic_contract_violation(fid, clause):
    low = _norm_contract(clause).lower()
    sentences = [s.strip() for s in re.split(r"(?<=[.;])\s+", low) if s.strip()]
    if fid == "F-EC-000b":
        rep_terms = [
            "ieee-754", "ieee 754", "binary32", "binary64", "binary128",
            "single-precision", "double-precision", "float32", "float64",
            "alternative representation", "binary representation", "decimal representation",
        ]
        for term in rep_terms:
            if term in low:
                return "binary floating-point representation term present: " + term
        controlled = ["floating", "binary", "fractional", "carry", "precision", "representation", "decimal"]
        markers = ["exception", "unless", "except", "provided that", "only when", "subject to", "notwithstanding", "however", "but "]
        for s in sentences:
            if any(m in s for m in markers) and any(c in s for c in controlled):
                return "unsupported exception or condition on controlled arithmetic: " + s[:140]
        if re.search(r"(may|can|permitted|allowed|preserve[sd]?|support[sd]?)[^.]{0,80}fractional carry", low):
            return "fractional carry permission asserted"
        if re.search(r"fractional carry[^.]{0,80}(may|can|permitted|allowed|preserve|support)", low):
            return "fractional carry permission asserted"
        if _perm(low, r"(?:binary[- ])?floating[- ]point") or _perm(low, "binary representation"):
            return "floating-point permission asserted"
        required = [
            "all quantities are integers",
            "every division states its rounding",
            "no formula uses binary floating point",
            "a percentage is an integer in basis points",
            "10,000 bp = 100%",
        ]
        for r in required:
            if r not in low:
                return "required baseline statement missing: " + r
        allowed = (
            "all quantities are integers",
            "every division states its rounding",
            "no formula uses binary floating point",
            "a percentage is an integer in basis points",
        )
        for s in sentences:
            if any(c in s for c in controlled) and not any(s.startswith(p) or p in s for p in allowed):
                return "unknown material clause: " + s[:140]
        return ""
    if fid == "F-EC-000f":
        if "final calibration" in low and "provisional calibration" in low:
            return "final/provisional calibration contradiction"
        if re.search(r"(?<!not )observed prices", low):
            return "affirmative observed-price claim"
        if re.search(r"(?<!not )balance claims", low):
            return "affirmative balance-claim"
        for s in sentences:
            if any(m in s for m in ("unless", "except", "provided that", "notwithstanding", "however")) and any(
                    c in s for c in ("provisional", "calibration", "observed", "balance", "revision", "owner")):
                return "unsupported exception on calibration/revision: " + s[:140]
        required = [
            "v1.0 provisional calibration",
            "carried unchanged into v1.1",
            "f-ec-044",
            "not observed prices",
            "not balance claims",
            "prompt 14 may change a value only by a new revision of this register",
        ]
        for r in required:
            if r not in low:
                return "required baseline statement missing: " + r
        return ""
    return ""


def _validate_decision_record(rec, a, fid, baseline_text, new_text, decisions_text):
    problems = []
    decision_id = a.get("decision_id", "")
    topic = _decision_cell(rec, "topic")
    body = _decision_cell(rec, "decision")
    status_cell = _decision_cell(rec, "status")
    reason = _decision_cell(rec, "reason")
    source_cell = _decision_cell(rec, "source")
    consequences = _decision_cell(rec, "consequences")
    combined = " ".join([topic, body, reason, source_cell, consequences])
    low = combined.lower()
    if fid.lower() not in low:
        problems.append(f"category=decision-clause param={fid} expected=clause named in decision actual=absent source=DECISIONS.md inventory_line={decision_id}")
    if "10_economic_formula_and_balance_register.md" not in low:
        problems.append(f"category=decision-source param={fid} expected=B-04 source named in decision actual=absent source=DECISIONS.md inventory_line={decision_id}")
    if not any(w in low for w in ("amend", "revis", "replac", "chang")):
        problems.append(f"category=decision-verb param={fid} expected=amendment verb in decision actual=absent source=DECISIONS.md inventory_line={decision_id}")
    if not _substantive(topic, 15):
        problems.append(f"category=decision-topic param={fid} expected=specific amendment topic actual={topic!r} source=DECISIONS.md inventory_line={decision_id}")
    # D-014 category and status
    cat_m = re.search(r"category\s*([ABCD])", status_cell, re.I)
    category = cat_m.group(1).upper() if cat_m else ""
    if not category:
        problems.append(f"category=decision-category param={fid} expected=explicit D-014 category actual={status_cell!r} source=DECISIONS.md inventory_line={decision_id}")
    elif category != str(a.get("category", "")).upper():
        problems.append(f"category=decision-category-mismatch param={fid} expected={a.get('category')!r} actual={category!r} source=DECISIONS.md inventory_line={decision_id}")
    if category == "B":
        if "confirmed" not in status_cell.lower():
            problems.append(f"category=decision-status param={fid} expected=Confirmed actual={status_cell!r} source=DECISIONS.md inventory_line={decision_id}")
    elif category in ("A", "D"):
        if not any(w in status_cell.lower() for w in ("owner-approved", "owner approved", "owner authorized", "owner accepted")):
            problems.append(f"category=decision-owner-status param={fid} expected=explicit owner authorization actual={status_cell!r} source=DECISIONS.md inventory_line={decision_id}")
    elif category == "C":
        if "provisional" not in status_cell.lower():
            problems.append(f"category=decision-status param={fid} expected=Provisional actual={status_cell!r} source=DECISIONS.md inventory_line={decision_id}")
    if any(w in status_cell.lower() for w in ("pending", "proposed", "rejected", "deferred", "superseded", "not approved")):
        problems.append(f"category=decision-inactive param={fid} expected=active decision actual={status_cell!r} source=DECISIONS.md inventory_line={decision_id}")
    if a.get("decision_status") and a["decision_status"].lower() not in status_cell.lower():
        problems.append(f"category=decision-status-manifest param={fid} expected={a.get('decision_status')!r} actual={status_cell!r} source=DECISIONS.md inventory_line={decision_id}")
    # Previous and replacement rules in the Decision cell
    previous = _marker(body, r"previous rule", [r"replacement rule", r"alternatives", r"consequences", r"reopening"])
    replacement = _marker(body, r"replacement rule", [r"alternatives", r"consequences", r"reopening"])
    if not _substantive(previous, 40):
        problems.append(f"category=decision-previous-rule param={fid} expected=substantive previous rule actual={previous!r} source=DECISIONS.md inventory_line={decision_id}")
    elif not _rule_matches(previous, baseline_text):
        problems.append(f"category=decision-previous-rule-mismatch param={fid} expected=previous source rule actual={previous!r} source=DECISIONS.md inventory_line={decision_id}")
    if not _substantive(replacement, 40):
        problems.append(f"category=decision-replacement-rule param={fid} expected=substantive replacement rule actual={replacement!r} source=DECISIONS.md inventory_line={decision_id}")
    elif not _rule_matches(replacement, new_text):
        problems.append(f"category=decision-replacement-rule-mismatch param={fid} expected=replacement source rule actual={replacement!r} source=DECISIONS.md inventory_line={decision_id}")
    alternatives = _marker(body, r"alternatives", [r"consequences", r"reopening", r"replacement rule"])
    if not _substantive(alternatives, 20):
        problems.append(f"category=decision-alternatives param={fid} expected=relevant alternatives actual={alternatives!r} source=DECISIONS.md inventory_line={decision_id}")
    replacement = _marker(body, r"replacement rule", [r"alternatives", r"consequences", r"reopening"])
    contract_mod = _contract_module()
    artifacts = contract_mod.load_artifacts()
    base_contract = artifacts["contracts"].get(fid)
    for prob in contract_mod.context_evidence_problems(base_contract, rec, artifacts["lexicon"], artifacts["mappings"]):
        problems.append(f"category=decision-evidence param={fid} actual={contract_mod.fmt(prob)} source=DECISIONS.md inventory_line={decision_id}")
    if not _substantive(consequences, 30):
        problems.append(f"category=decision-consequences param={fid} expected=documented consequences actual={consequences!r} source=DECISIONS.md inventory_line={decision_id}")
    reopen = _marker(body, r"reopening", [r"consequences", r"alternatives"]) or _marker(consequences, r"reopening", [r"$"])
    if not _substantive(reopen, 15):
        problems.append(f"category=decision-reopening param={fid} expected=reopening conditions actual={reopen!r} source=DECISIONS.md inventory_line={decision_id}")
    if a.get("owner_reserved") or category in ("A", "D"):
        auth_text = " ".join([body, reason, status_cell])
        if not re.search(r"owner\s+(?:authorization|instruction)\s*[:\-]", auth_text, re.I):
            problems.append(f"category=decision-owner-authorization param={fid} expected=explicit owner authorization reference actual=absent source=DECISIONS.md inventory_line={decision_id}")
        artifacts = _contract_module().load_artifacts()
        registry = artifacts["index"].get("owner_authorizations", [])
        owner_props = [{"proposition_id": p["id"], "systems": p.get("scope", {}).get("systems", [])}
                       for p in base_contract.get("propositions", [])] or [
            {"proposition_id": fid, "systems": base_contract.get("scope", {}).get("systems", [])}]
        for prob in _contract_module()._owner_authorization_problems(
                decision_id, owner_props, registry, mode="production"):
            problems.append(f"category=decision-owner-authorization param={fid} actual={_contract_module().fmt(prob)} source=DECISIONS.md inventory_line={decision_id}")
    if not _substantive(a.get("authorization_evidence", ""), 20):
        problems.append(f"category=manifest-authorization-evidence param={fid} expected=substantive authorization evidence actual={a.get('authorization_evidence')!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    if not _substantive(a.get("rationale", ""), 20):
        problems.append(f"category=manifest-rationale param={fid} expected=substantive rationale actual={a.get('rationale')!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    if not _substantive(a.get("regression_evidence", ""), 10):
        problems.append(f"category=manifest-regression-evidence param={fid} expected=regression evidence actual={a.get('regression_evidence')!r} source=qa_backups/14A_b04_source_contract_amendments.json inventory_line=<amendment>")
    return problems



def _decision_full(did, clause, previous, replacement, status="**Confirmed** (Category B; TEST FIXTURE)",
                   reason=None, consequences=None,
                   source="docs/stage-2/10_economic_formula_and_balance_register.md",
                   alternatives="retain current wording; adopt decimal fractions (rejected); clarify basis points",
                   topic=None, owner_auth=None):
    body = f"Previous rule: {previous}; Replacement rule: {replacement}; Alternatives: {alternatives}."
    if owner_auth:
        body += f" Owner authorization: {owner_auth}."
    if reason is None:
        if clause == "F-EC-000b":
            reason = ('Evidence: path=docs/stage-2/22_formulas_and_balance.md; section=8.2; '
                      'quote="No binary floating point; no fractional carry stated"; '
                      'supports="the register prohibits binary floating point"; stance=supports; '
                      'Rationale: B-14 section 8.2 records the register floating-point prohibition.')
        else:
            reason = ('Evidence: path=docs/stage-2/10_economic_formula_and_balance_register.md; section=F-EC-044; '
                      'quote="The constants are the v1.0 provisional calibration"; '
                      'supports="v1.0 constants remain provisional calibration"; stance=supports; '
                      'Rationale: F-EC-044 records the v1.0 provisional calibration and its carry into v1.1.')
    consequences = consequences or ("Consequences: B-04 constants remain integer; dependent formulas and maintenance accounting are unchanged. "
                                    "Reopening: reopen if a D-014 decision changes arithmetic policy.")
    topic = topic or f"Amend {clause} (TEST FIXTURE)"
    return f"| {did} | 2026-11-13 | {topic} | {body} | {status} | {reason} | {source} | {consequences} |"


def _manifest_full(fid, new_hash, decision_id="D-900", category="B", decision_status="Confirmed",
                   owner_reserved=False, **over):
    base = json.loads(read(FILES["B04_AMENDMENTS"]))
    entry = {
        "clause": fid,
        "source_document": "docs/stage-2/10_economic_formula_and_balance_register.md",
        "previous_hash": B04_CONTRACT[fid]["hash"],
        "new_hash": new_hash,
        "decision_id": decision_id,
        "category": category,
        "decision_status": decision_status,
        "authorization_evidence": f"DECISIONS.md {decision_id} (TEST FIXTURE ONLY)",
        "rationale": "Clarifies the clause while preserving the register integer-arithmetic policy and its dependent formulas.",
        "regression_evidence": "Fixture 80 (TEST FIXTURE ONLY)",
        "owner_reserved": owner_reserved,
    }
    entry.update(over)
    base["amendments"] = [entry]
    return json.dumps(base)


def self_test():
    base_master = read(FILES["MASTER"])
    base_params = read(FILES["PARAMS"])
    base_roadmap = read(FILES["ROADMAP"])
    base_b14 = read(FILES["B-14"])
    base_ud = read(FILES["UD"])
    cases = []

    def expect_pass(name, cid, overrides=None):
        problems = _checks(validate(overrides))[cid]
        cases.append((name, not problems, problems))

    def expect_fail(name, cid, overrides):
        problems = _checks(validate(overrides))[cid]
        cases.append((name, bool(problems), problems or ["expected a failure, got none"]))

    def expect_fail_with(name, cid, overrides, token):
        problems = _checks(validate(overrides))[cid]
        hit = [p for p in problems if token in p]
        cases.append((name, bool(hit), hit or (problems or ["expected a failure, got none"])))

    # 1 — correct baseline
    results = validate()
    bad = [(cid, p) for cid, _, p in results if p]
    cases.append(("Baseline: all checks pass", not bad, [f"{c}: {p}" for c, p in bad]))

    # 2 — missing active formula
    expect_fail("Missing active formula → FAIL", "14A-05",
                {"MASTER": _drop_row(base_master, "F-EC-001")})

    # 3 — duplicate active formula
    rows = [l for l in base_master.splitlines() if l.strip().startswith("| `F-EC-002`")]
    expect_fail("Duplicate active formula → FAIL", "14A-05",
                {"MASTER": _insert_after_row(base_master, "F-EC-001", rows[0])})

    # 4 — retired counted as active
    retired_row = ("| `F-WEP-048` | B-11 | Contribution allocation | `18_` | x | x | UNSPECIFIED | x | x | x | x |")
    expect_fail("Retired formula counted as active → FAIL", "14A-05",
                {"MASTER": _insert_after_row(base_master, "F-EC-001", retired_row)})

    # 5 — unresolved source reference
    bad_ref = _replace_row(base_master, "F-EC-001", 9, "`docs/stage-2/does_not_exist.md` line 1; test")
    expect_fail("Unresolved formula source reference → FAIL", "14A-07", {"MASTER": bad_ref})

    # 6 — missing unit metadata
    expect_fail("Missing unit metadata without gap marker → FAIL", "14A-06",
                {"MASTER": _replace_row(base_master, "F-EC-001", 2, "")})

    # 7 — missing rounding metadata
    expect_fail("Missing rounding metadata without gap marker → FAIL", "14A-06",
                {"MASTER": _replace_row(base_master, "F-EC-001", 6, "")})

    # 8 — missing timing metadata
    expect_fail("Missing timing metadata without gap marker → FAIL", "14A-06",
                {"MASTER": _replace_row(base_master, "F-EC-001", 7, "")})

    # 9 — missing B-03 carry-in
    first_b03_row = next(l for l in base_params.splitlines() if l.strip().startswith("| 1 |") and "W_obs" in l)
    expect_fail("Missing B-03 carry-in parameter → FAIL", "14A-10",
                {"PARAMS": base_params.replace(first_b03_row + "\n", "")})

    # 10 — altered B-03 value
    altered = base_params.replace("| 24 hours | hours | Prompt 12; Prompt 14 |", "| 25 hours | hours | Prompt 12; Prompt 14 |", 1)
    expect_fail("Altered B-03 provisional value → FAIL", "14A-11", {"PARAMS": altered})

    # 11 — incorrect parameter owner
    altered_owner = base_params.replace("| 24 hours | hours | Prompt 12; Prompt 14 |", "| 24 hours | hours | Prompt 14 |", 1)
    expect_fail("Incorrect parameter owner → FAIL", "14A-11", {"PARAMS": altered_owner})

    # 12 — invalid status
    expect_fail("Invalid numerical status → FAIL", "14A-08",
                {"MASTER": _replace_row(base_master, "F-EC-001", 6, "APPROVED")})

    # 13 — false owner-approved classification
    expect_fail("False owner-approved classification → FAIL", "14A-09",
                {"MASTER": _replace_row(base_master, "F-EC-001", 6, "OWNER-APPROVED VALUE")})

    # 14 — owner-reserved UD silently resolved
    ud_bad = base_ud.replace("| UD-046 |", "| UD-046 |", 1)
    ud_bad = re.sub(r"(\| UD-046 \|[^\n]*)Open", r"\1**Resolved**", ud_bad, count=1)
    expect_fail("Owner-reserved UD silently resolved → FAIL", "14A-25", {"UD": ud_bad})

    # 15 — correct 22_ mapping
    expect_pass("Correct current B-14 22_ mapping → PASS", "14A-22")

    # 16 — live stale 21_ row
    stale_row = "| 14 | Numbers, formulas, balance and worked examples | `21_formulas_and_balance.md` | Pending |"
    roadmap_bad = re.sub(r"^\|\s*14\s*\|.*$", stale_row, base_roadmap, count=1, flags=re.M)
    expect_fail("Live roadmap row using stale 21_ → FAIL", "14A-22", {"ROADMAP": roadmap_bad})

    # 17 — historical 21_ mention properly labelled
    labelled = re.sub(r"^\|\s*14\s*\|.*$",
                      "| 14 | Numbers | `22_formulas_and_balance.md` (the earlier `21_formulas_and_balance.md` name is superseded) | Pending |",
                      base_roadmap, count=1, flags=re.M)
    expect_pass("Historical superseded 21_ mention labelled → PASS", "14A-22", {"ROADMAP": labelled})

    # 18 — D-019 ordering
    expect_pass("D-019 ordering preserved → PASS", "14A-17")

    # 19 — obsolete D-015 current claim
    obsolete = base_b14.replace("The original D-015 wording that unused points do not bank is **superseded by the recorded 10B-C3 amendment** (2026-11-04).",
                                "Unused points do not bank.")
    expect_fail("Obsolete D-015 wording presented as current → FAIL", "14A-18", {"B-14": obsolete})

    # 20 — missing validator reference
    expect_fail("Missing validator reference → FAIL", "14A-06",
                {"MASTER": _replace_row(base_master, "F-EC-001", 8, "")})


    # ---- 14A-C1 parameter mutation matrix ----
    fwr003 = [l for l in base_params.splitlines() if l.strip().startswith("| `F-WR-003`")]
    fwr003_row = fwr003[0]
    expect_fail("C1: Remove B-10 F-WR-001 parameter record → FAIL", "14A-29",
                {"PARAMS": _drop_row(base_params, "F-WR-001")})
    expect_fail("C1: Change B-10 F-WR-003 owner → FAIL", "14A-32",
                {"PARAMS": _replace_row(base_params, "F-WR-003", 8, "Owner (UD-053)")})
    expect_fail("C1: Promote B-10 F-WR-003 without approval evidence → FAIL", "14A-32",
                {"PARAMS": _replace_row(base_params, "F-WR-003", 10, "OWNER-APPROVED VALUE")})
    expect_fail("C1: Change B-04 starting treasury 1,500 → 1,501 → FAIL", "14A-30",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 2, "1,501", "B-04 §3.1")})
    expect_fail("C1: Change a parameter unit → FAIL", "14A-31",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 3, "people", "B-04 §3.1")})
    expect_fail("C1: Change a parameter rounding rule → FAIL", "14A-33",
                {"PARAMS": _replace_row(base_params, "F-WR-003", 6, "Rounded to the nearest hundred")})
    expect_fail("C1: Remove a parameter source reference → FAIL", "14A-33",
                {"PARAMS": _replace_row(base_params, "F-WR-003", 4, "")})
    expect_fail("C1: Duplicate a parameter record → FAIL", "14A-29",
                {"PARAMS": _insert_after_row(base_params, "F-WR-003", fwr003_row)})
    expect_fail("C1: Remove a B-08 parameter record → FAIL", "14A-29",
                {"PARAMS": _drop_row(base_params, "F-DP-001")})
    expect_fail("C1: Remove a B-09 parameter record → FAIL", "14A-29",
                {"PARAMS": _drop_row(base_params, "F-AL-002")})
    expect_fail("C1: Remove a B-11 parameter record → FAIL", "14A-29",
                {"PARAMS": _drop_row(base_params, "F-WEP-003")})
    expect_fail("C1: Mark playtesting-dependent FP-P07 owner-approved → FAIL", "14A-32",
                {"PARAMS": _replace_row(base_params, "FP-P07", 5, "OWNER-APPROVED VALUE")})
    expect_pass("C1: Preserve a correctly documented provisional parameter → PASS", "14A-32")
    expect_pass("C1: Preserve a properly sourced owner-approved parameter → PASS", "14A-32")
    source_no_round = _clear_formula_rounding(read(FILES["REG_B-10"]), "F-WR-024")
    params_no_round = _replace_row(base_params, "F-WR-024", 6, "Not specified")
    expect_pass("C1: Preserve an explicit missing-data marker → PASS", "14A-33",
                {"REG_B-10": source_no_round, "PARAMS": params_no_round})


    # ---- 14A-C1-R1 mandatory mutation matrix ----
    fwr003_row = next(l for l in base_params.splitlines() if l.strip().startswith("| `F-WR-003`"))
    expect_fail("R1: B-10 F-WR-003 unit → bananas", "14A-39",
                {"PARAMS": _replace_row(base_params, "F-WR-003", 3, "bananas")})
    expect_fail("R1: B-04 Treasury decision authority changed", "14A-36",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 8, "Owner (UD-053)", "B-04 §3.1")})
    expect_fail("R1: B-04 Treasury promoted to OWNER-APPROVED", "14A-36",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 10, "OWNER-APPROVED VALUE", "B-04 §3.1")})
    expect_fail("R1: B-04 Treasury timing changed", "14A-36",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 7, "Whenever", "B-04 §3.1")})
    expect_fail("R1: B-03 W_obs unit → bananas", "14A-38",
                {"PARAMS": _replace_b03_row(base_params, "Network observation window `W_obs`", 3, "bananas")})
    expect_fail("R1: B-03 W_obs evidence fabricated", "14A-38",
                {"PARAMS": _replace_b03_row(base_params, "Network observation window `W_obs`", 5, "evidence already satisfied")})
    expect_fail("R1: B-03 W_obs evidence class → Confirmed", "14A-38",
                {"PARAMS": _replace_b03_row(base_params, "Network observation window `W_obs`", 6, "Confirmed")})
    expect_fail("R1: B-02 Turn length status → PROVISIONAL", "14A-37",
                {"PARAMS": _replace_b02_row(base_params, "Turn length", 6, "PROVISIONAL VALUE")})
    expect_fail("R1: B-12 FP-P07 unit → bananas", "14A-39",
                {"PARAMS": _replace_row(base_params, "FP-P07", 3, "bananas")})
    expect_fail("R1: Unparseable source unit field", "14A-39",
                {"REG_B-10": _remove_formula_field(read(FILES["REG_B-10"]), "F-WR-003", 6)})
    expect_fail("R1: F-WR-003 timing changed", "14A-33",
                {"PARAMS": _replace_row(base_params, "F-WR-003", 7, "Any time")})
    expect_fail("R1: F-AL-002 owner-reserved status cleared", "14A-32",
                {"PARAMS": _replace_row(base_params, "F-AL-002", 13, "No")})
    expect_pass("R1: Preserve an approved B-02 turn-length status", "14A-37")


    # ---- 14A-C1-R1-R1 final precision/rounding and owner-reserved fixtures ----
    expect_fail("R1-R1: B-04 Treasury precision/rounding → round to nearest banana", "14A-42",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 6, "round to nearest banana", "B-04 §3.1")})
    expect_pass("R1-R1: Correct B-04 Treasury precision/rounding", "14A-42")
    expect_fail("R1-R1: B-05 constant precision changed", "14A-42",
                {"PARAMS": _replace_param_named(base_params, "Maximum cities per nation", 6, "round to nearest banana", "B-05 §3.1")})
    expect_fail("R1-R1: B-06 constant precision changed", "14A-42",
                {"PARAMS": _replace_param_named(base_params, "Starting population", 6, "round to nearest banana", "B-06 §3.1")})
    expect_fail("R1-R1: B-07 constant precision changed", "14A-42",
                {"PARAMS": _replace_param_named(base_params, "Fair-value band (B)", 6, "round to nearest banana", "B-07 §3")})
    expect_fail("R1-R1: Precision marker removed", "14A-42",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 6, "", "B-04 §3.1")})
    expect_fail("R1-R1: B-04 source convention unparseable", "14A-42",
                {"REG_B-04": _remove_line_containing(read(FILES["REG_B-04"]), "F-EC-000b")})
    expect_fail("R1-R1: B-04 Treasury owner-reserved → Yes without authority", "14A-43",
                {"PARAMS": _replace_param_named(base_params, "Treasury", 13, "Yes — owner-reserved", "B-04 §3.1")})
    expect_fail("R1-R1: B-09 F-AL-002 owner-reserved removed", "14A-43",
                {"PARAMS": _replace_row(base_params, "F-AL-002", 13, "No")})
    expect_fail("R1-R1: B-10 F-WR-001 false owner-reserved addition", "14A-43",
                {"PARAMS": _replace_row(base_params, "F-WR-001", 13, "Yes — owner-reserved")})
    expect_fail("R1-R1: B-12 FP-P07 false owner-reserved addition", "14A-43",
                {"PARAMS": _replace_row(base_params, "FP-P07", 8, "Yes — owner-reserved")})
    expect_fail("R1-R1: B-12 FP-P01 owner-reserved removal", "14A-43",
                {"PARAMS": _replace_row(base_params, "FP-P01", 8, "No")})
    expect_fail("R1-R1: B-03 W_obs false owner-reserved addition", "14A-43",
                {"PARAMS": _replace_b03_row(base_params, "Network observation window `W_obs`", 7, "Yes — owner-reserved")})
    expect_fail("R1-R1: B-12 FP-P07 owner authority ambiguous", "14A-43",
                {"REG_B-12": _replace_fp_source_owner(read(FILES["REG_B-12"]), "FP-P07", "")})
    expect_pass("R1-R1: Genuine B-09 owner-reserved record preserved", "14A-43")
    expect_pass("R1-R1: Non-owner-reserved Treasury preserved", "14A-43")


    # ---- 14A-C1-R1-R1-C1 B-04 semantic source contracts ----
    b04 = read(FILES["REG_B-04"])
    expect_pass("FINAL: F-EC-000b correct integer rule", "14A-45")
    expect_fail("FINAL: F-EC-000b decimal-fraction mutation", "14A-45",
                {"REG_B-04": _replace_text(b04, "All quantities are integers.", "All quantities may be decimal fractions.")})
    expect_fail("FINAL: F-EC-000b floating-point permission", "14A-45",
                {"REG_B-04": _replace_text(b04, "No formula uses binary floating point.", "Formula calculations may use binary floating point.")})
    expect_fail("FINAL: F-EC-000b floating-point prohibition removed", "14A-45",
                {"REG_B-04": _replace_text(b04, "No formula uses binary floating point.", "")})
    expect_fail("FINAL: F-EC-000b rounding requirement removed", "14A-45",
                {"REG_B-04": _replace_text(b04, "Every division states its rounding:", "Every division may round as convenient:")})
    expect_fail("FINAL: F-EC-000b basis-point relationship changed", "14A-45",
                {"REG_B-04": _replace_text(b04, "A percentage is an integer in **basis points** (bp)", "A percentage is a decimal fraction (bp)")})
    expect_fail("FINAL: F-EC-000b 10,000 bp = 100% changed", "14A-45",
                {"REG_B-04": _replace_text(b04, "10,000 bp = 100%", "1,000 bp = 100%")})
    expect_pass("FINAL: F-EC-000f correct provisional-versioning rule", "14A-46")
    expect_fail("FINAL: F-EC-000f owner-only revision authority", "14A-46",
                {"REG_B-04": _replace_text(b04, "Prompt 14 may change a value only by a new revision of this register.", "Only the project owner may change a value by a new revision of this register.")})
    expect_fail("FINAL: F-EC-000f provisional classification removed", "14A-46",
                {"REG_B-04": _replace_text(b04, "v1.0 provisional calibration", "v1.0 final calibration")})
    expect_fail("FINAL: F-EC-000f v1.0/v1.1 relationship changed", "14A-46",
                {"REG_B-04": _replace_text(b04, "carried unchanged into v1.1", "revised into v1.1")})
    expect_fail("FINAL: F-EC-000f F-EC-044 reference removed", "14A-46",
                {"REG_B-04": _replace_text(b04, "(see F-EC-044)", "")})
    expect_fail("FINAL: F-EC-000f observed-price claim", "14A-46",
                {"REG_B-04": _replace_text(b04, "They are not observed prices", "They are observed prices")})
    expect_fail("FINAL: F-EC-000f balance-claim promotion", "14A-46",
                {"REG_B-04": _replace_text(b04, "and not balance claims", "and balance claims")})


    # ---- 14A-C1-R1-R1-C1-R1 amendment authorization chain ----
    b04_base = read(FILES["REG_B-04"])
    decisions_base = read(FILES["DECISIONS"])
    mut_perm = _replace_text(b04_base, "No formula uses binary floating point.", "Binary floating point calculations are permitted.")
    hash_perm = _clause_hash(mut_perm, "F-EC-000b")
    new_perm = _norm_contract(_extract_b04_clause(mut_perm, "F-EC-000b"))
    mut_b = _replace_text(b04_base, "No formula uses binary floating point.", "No formula uses binary floating point, including derived calculations.")
    hash_b = _clause_hash(mut_b, "F-EC-000b")
    new_b = _norm_contract(_extract_b04_clause(mut_b, "F-EC-000b"))
    mut_f_a = _replace_text(b04_base, "Prompt 14 may change a value only by a new revision of this register.", "Prompt 14 may change a value only by a new revision of this register, and the v1.0 constants remain provisional calibration until that revision.")
    hash_f_a = _clause_hash(mut_f_a, "F-EC-000f")
    new_f_a = _norm_contract(_extract_b04_clause(mut_f_a, "F-EC-000f"))
    mut_f_c = _replace_text(b04_base, "The constants below are the **v1.0 provisional calibration**", "The constants below remain the **v1.0 provisional calibration** pending calibration evidence.")
    hash_f_c = _clause_hash(mut_f_c, "F-EC-000f")
    new_f_c = _norm_contract(_extract_b04_clause(mut_f_c, "F-EC-000f"))
    row_b = _decision_full("D-900", "F-EC-000b", B04_CONTRACT["F-EC-000b"]["baseline_text"], new_b)
    # Superseded legacy semantics: the old fixture accepted a placeholder owner
    # authorization. AC-20 now rejects placeholders, so this restatement is
    # validated as an ordinary Category B wording clarification; the Category A
    # positive path is covered by the contract suite with a test-only owner
    # authorization registry entry.
    row_a = _decision_full("D-901", "F-EC-000f", B04_CONTRACT["F-EC-000f"]["baseline_text"], new_f_a,
                           status="**Confirmed** (Category B; TEST FIXTURE)")
    expect_pass("FINAL-R1: restatement accepted as Category B wording clarification (legacy placeholder-A fixture superseded)", "14A-46",
                {"REG_B-04": mut_f_a, "DECISIONS": decisions_base + chr(10) + row_a,
                 "B04_AMENDMENTS": _manifest_full("F-EC-000f", hash_f_a, decision_id="D-901", category="B", decision_status="Confirmed", owner_reserved=False)})
    expect_fail("FINAL-R1: changed source without a decision", "14A-45",
                {"REG_B-04": mut_b})
    expect_fail("FINAL-R1: manifest updated but decision row missing", "14A-45",
                {"REG_B-04": mut_b, "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-902")})
    expect_fail("FINAL-R1: unrelated decision citation", "14A-45",
                {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-903", "F-EC-000b", verb="Records an unrelated matter about"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-903")})
    expect_fail("FINAL-R1: decision covers a different clause", "14A-45",
                {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-904", "F-EC-000f"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-904")})
    for label, status in (("pending", "**Pending**"), ("rejected", "**Rejected**"), ("deferred", "**Deferred**"), ("superseded", "**Superseded**")):
        expect_fail(f"FINAL-R1: {label} decision reference", "14A-45",
                    {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-905", "F-EC-000b", status=status),
                     "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-905")})
    expect_fail("FINAL-R1: manifest missing authorization evidence", "14A-45",
                {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-906", "F-EC-000b"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-906", authorization_evidence="")})
    expect_fail("FINAL-R1: wrong previous fingerprint", "14A-45",
                {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-907", "F-EC-000b"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-907", previous_hash="0" * 64)})
    expect_fail("FINAL-R1: new fingerprint does not match source", "14A-45",
                {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-908", "F-EC-000b"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", "1" * 64, decision_id="D-908")})
    expect_fail("FINAL-R1: owner-reserved change without owner authority", "14A-45",
                {"REG_B-04": mut_b, "DECISIONS": decisions_base + "\n" + _decision_fixture("D-909", "F-EC-000b"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", hash_b, decision_id="D-909", owner_reserved=True)})
    expect_fail("FINAL-R1: amendment entry without source change", "14A-45",
                {"DECISIONS": decisions_base + "\n" + _decision_fixture("D-910", "F-EC-000b"),
                 "B04_AMENDMENTS": _manifest_json("F-EC-000b", B04_CONTRACT["F-EC-000b"]["hash"], decision_id="D-910")})

    # ---- C1-R1-C1: substantive D-014 decision evidence ----
    base_b = B04_CONTRACT["F-EC-000b"]["baseline_text"]
    default_reason = split_row(row_b)[5]
    default_cons = ("Consequences: B-04 constants remain integer; dependent formulas and maintenance accounting are unchanged. "
                    "Reopening: reopen if a D-014 decision changes arithmetic policy.")
    d998 = _decision_full("D-998", "F-EC-000b", base_b, new_b)
    fair = ("Evidence: path=docs/stage-2/20_fair_play_and_player_protection.md; section=Fair-play; quote=\"Fair-play rules apply to all accounts\"; supports=\"integer arithmetic policy\"; stance=supports; Rationale: The fair-play document describes account rules.")
    d998 = d998.replace(split_row(d998)[5], fair, 1)
    m998 = _manifest_full("F-EC-000b", hash_b, decision_id="D-998")
    expect_fail_with("CLOSURE: exact D-998 fair-play evidence attack rejected", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + d998, "B04_AMENDMENTS": m998},
                     "evidence locus")
    d999 = _decision_full("D-999", "F-EC-000b", base_b, new_perm)
    m999 = _manifest_full("F-EC-000b", hash_perm, decision_id="D-999")
    expect_fail_with("CLOSURE-R1: exact D-999 prohibition-as-permission attack rejected", "14A-45",
                     {"REG_B-04": mut_perm, "DECISIONS": decisions_base + chr(10) + d999, "B04_AMENDMENTS": m999},
                     "contradicts")
    expect_fail_with("CLOSURE: previous rule omitted", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(f"Previous rule: {base_b}; ", ""),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-previous-rule")
    expect_fail_with("CLOSURE: replacement rule omitted", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(f"Replacement rule: {new_b}; ", ""),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-replacement-rule")
    expect_fail_with("CLOSURE: previous rule mismatch", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(base_b, "All quantities are decimal fractions and may use floating point."),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-previous-rule-mismatch")
    expect_fail_with("CLOSURE: replacement rule mismatch", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(new_b, "All quantities may be decimal fractions."),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-replacement-rule-mismatch")
    expect_fail_with("CLOSURE: alternatives omitted", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace("Alternatives: retain current wording; adopt decimal fractions (rejected); clarify basis points.", ""),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-alternatives")
    expect_fail_with("CLOSURE: empty rationale", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(default_reason, ""),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-evidence")
    expect_fail_with("CLOSURE: generic rationale", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(default_reason, "Approved because confirmed."),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-evidence")
    expect_fail_with("CLOSURE: generic evidence", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(default_reason, "Test only."),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-evidence")
    expect_fail_with("CLOSURE: evidence path missing", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace("path=docs/stage-2/22_formulas_and_balance.md", "path=docs/stage-2/does_not_exist.md"),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-evidence")
    expect_fail_with("CLOSURE: consequences empty", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace(default_cons, ""),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-consequences")
    expect_fail_with("CLOSURE: reopening condition missing", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b.replace("Reopening: reopen if a D-014 decision changes arithmetic policy.", ""),
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-reopening")
    wrong_source_row = _decision_full("D-900", "F-EC-000b", base_b, new_b,
                                      source="docs/stage-2/22_formulas_and_balance.md",
                                      reason="Evidence: repository review supports the clarification.")
    expect_fail_with("CLOSURE: wrong source document", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + wrong_source_row,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-source")
    wrong_clause_row = _decision_full("D-900", "F-EC-000f", B04_CONTRACT["F-EC-000f"]["baseline_text"], new_f_a,
                                      reason="Evidence: docs/stage-2/10_economic_formula_and_balance_register.md and REQ-162 support the clarification.")
    expect_fail_with("CLOSURE: wrong clause", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + wrong_clause_row,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-clause")
    cat_row = _decision_full("D-900", "F-EC-000b", base_b, new_b,
                             status="**Owner-approved** (Category A; TEST FIXTURE)",
                             owner_auth="TEMP-OWNER-02 (temporary fixture, not a real owner instruction)")
    expect_fail_with("CLOSURE: category mismatch", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + cat_row,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-category-mismatch")
    status_row = _decision_full("D-900", "F-EC-000b", base_b, new_b,
                                status="**Provisional** (Category B; TEST FIXTURE)")
    expect_fail_with("CLOSURE: status mismatch", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + status_row,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-status")
    expect_fail_with("CLOSURE: owner-reserved without owner authority", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b, owner_reserved=True)}, "decision-owner-authorization")
    promoted_c = _decision_full("D-900", "F-EC-000b", base_b, new_b,
                                status="**Confirmed** (Category C; TEST FIXTURE)")
    expect_fail_with("CLOSURE: Category C promoted to Confirmed", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + promoted_c,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b, category="C", decision_status="Provisional")}, "decision-status")
    expect_fail_with("CLOSURE: duplicate D-number", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b + chr(10) + row_b,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "amendment-decision-duplicate")
    malformed_row = "| D-900 | 2026-11-13 | Amend F-EC-000b | only four cells |"
    expect_fail_with("CLOSURE: malformed decision row", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + malformed_row,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "amendment-decision-missing")
    unrelated_row = _decision_full("D-900", "F-EC-000b", base_b, new_b, topic="Record an unrelated documentation matter",
                                   reason="Evidence: docs/stage-2/10_economic_formula_and_balance_register.md and REQ-162 support the clarification.")
    unrelated_row = unrelated_row.replace("Previous rule: " + base_b, "Previous rule: This row records a separate matter").replace("Replacement rule: " + new_b, "Replacement rule: no B-04 change")
    expect_fail_with("CLOSURE: unrelated decision reference", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + unrelated_row,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "decision-clause")
    expect_fail_with("CLOSURE: manifest source mismatch", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b, source_document="docs/stage-2/22_formulas_and_balance.md")}, "amendment-source-mismatch")
    expect_fail_with("CLOSURE: manifest status mismatch", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_b,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b, decision_status="Provisional")}, "decision-status-manifest")
    row_c = _decision_full("D-902", "F-EC-000f", B04_CONTRACT["F-EC-000f"]["baseline_text"], new_f_c,
                           status="**Provisional** (Category C; TEST FIXTURE)")
    row_c = row_c.replace(" | **Provisional**", " Missing evidence: calibrated integer-arithmetic review; Test: fixture; Owner: Prompt 14. | **Provisional**", 1)
    expect_pass("CLOSURE: complete Category C provisional fixture accepted", "14A-46",
                {"REG_B-04": mut_f_c, "DECISIONS": decisions_base + chr(10) + row_c,
                 "B04_AMENDMENTS": _manifest_full("F-EC-000f", hash_f_c, decision_id="D-902", category="C", decision_status="Provisional")})

    row_ctx = row_b.replace("section=8.2", "section=13.1")
    expect_fail_with("CLOSURE: genuine quote cited from wrong section", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_ctx,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "evidence locus is not an authorized source")
    row_fab = row_b.replace('quote="No binary floating point; no fractional carry stated"',
                            'quote="All quantities may be decimal fractions."')
    expect_fail_with("CLOSURE: fabricated supporting excerpt", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_fab,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "quoted evidence does not appear")
    row_stale = row_b.replace("section=8.2", "section=99.9")
    expect_fail_with("CLOSURE: stale evidence location", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_stale,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "evidence locus is not an authorized source")
    row_supp = row_b.replace('supports="the register prohibits binary floating point"',
                             'supports="fair-play appeal window and retention"')
    expect_fail_with("CLOSURE: evidence does not support the claimed proposition", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_supp,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "not substantiated")
    row_partial = row_b.replace('supports="the register prohibits binary floating point"',
                                'supports="integer arithmetic and fair-play appeal window"')
    expect_fail_with("CLOSURE: partial evidence coverage", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_partial,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "does not establish")
    row_changed = row_b.replace('quote="No binary floating point; no fractional carry stated"',
                                'quote="No formula uses binary floating point."')
    expect_fail_with("CLOSURE: materially changed evidence text", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_changed,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "quoted evidence does not appear")

    mut_obs = _replace_text(b04_base, "They are not observed prices and not balance claims.",
                            "They are observed prices and balance claims.")
    hash_obs = _clause_hash(mut_obs, "F-EC-000f")
    new_obs = _norm_contract(_extract_b04_clause(mut_obs, "F-EC-000f"))
    row_obs = _decision_full("D-903", "F-EC-000f", B04_CONTRACT["F-EC-000f"]["baseline_text"], new_obs)
    obs_reason = ('Evidence: path=docs/stage-2/10_economic_formula_and_balance_register.md; section=F-EC-000f; '
                  'quote="They are not observed prices and not balance claims."; '
                  'supports="the constants are observed prices and balance claims"; stance=supports; '
                  'Rationale: The amendment identifies the constants as observed prices and balance claims.')
    row_obs = row_obs.replace(split_row(row_obs)[5], obs_reason, 1)
    expect_fail_with("CLOSURE-R1: evidence negation reversed (permission as prohibition)", "14A-46",
                     {"REG_B-04": mut_obs, "DECISIONS": decisions_base + chr(10) + row_obs,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000f", hash_obs, decision_id="D-903")}, "contradicts")
    row_partial_supp = row_b.replace('supports="the register prohibits binary floating point"',
                                     'supports="integer arithmetic and owner authorization"')
    expect_fail_with("CLOSURE-R1: partial evidence does not establish the claim", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + row_partial_supp,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_b)}, "does not establish")
    m_map = _manifest_full("F-EC-000b", hash_b, decision_id="D-998",
                           evidence_allowlist=["docs/stage-2/20_fair_play_and_player_protection.md"])
    expect_fail_with("CLOSURE-R1: unauthorized evidence mapping cannot authorize itself", "14A-45",
                     {"REG_B-04": mut_b, "DECISIONS": decisions_base + chr(10) + d998, "B04_AMENDMENTS": m_map},
                     "evidence locus")
    mut_bp = _replace_text(b04_base, "10,000 bp = 100%", "1,000 bp = 100%")
    hash_bp = _clause_hash(mut_bp, "F-EC-000b")
    new_bp = _norm_contract(_extract_b04_clause(mut_bp, "F-EC-000b"))
    row_bp = _decision_full("D-905", "F-EC-000b", base_b, new_bp)
    bp_reason = ('Evidence: path=docs/stage-2/10_economic_formula_and_balance_register.md; section=F-EC-000b; '
                 'quote="A percentage is an integer in basis points (bp), where 10,000 bp = 100%."; supports="the basis-point relationship is 1,000 bp = 100%"; stance=supports; '
                 'Rationale: The amendment changes the basis-point relationship.')
    row_bp = row_bp.replace(split_row(row_bp)[5], bp_reason, 1)
    expect_fail_with("CLOSURE-R1: incorrect numerical scope (basis points)", "14A-45",
                     {"REG_B-04": mut_bp, "DECISIONS": decisions_base + chr(10) + row_bp,
                      "B04_AMENDMENTS": _manifest_full("F-EC-000b", hash_bp, decision_id="D-905")}, "contradicts")

    # ---- C1-R1-C1-R1: controlled semantic contract (D-990) ----
    d990_text = ("No formula uses binary floating point. An exception applies only when numeric calculations use an alternative representation "
                 "within the treasury carry subsystem, subject to separate fractional ledger handling; the subsystem may use IEEE-754 "
                 "binary representation and preserve fractional carry.")
    mut_990 = _replace_text(b04_base, "No formula uses binary floating point.", d990_text)
    hash_990 = _clause_hash(mut_990, "F-EC-000b")
    new_990 = _norm_contract(_extract_b04_clause(mut_990, "F-EC-000b"))
    d990 = _decision_full("D-990", "F-EC-000b", base_b, new_990)
    m990 = _manifest_full("F-EC-000b", hash_990, decision_id="D-990")
    expect_fail_with("CLOSURE-FINAL: exact D-990 exception attack rejected", "14A-45",
                     {"REG_B-04": mut_990, "DECISIONS": decisions_base + chr(10) + d990, "B04_AMENDMENTS": m990},
                     "semantic-contract")
    for label, exception in (
        ("IEEE-754 representation", "An exception applies for IEEE-754 representation."),
        ("Binary32 permission", "Binary32 is permitted for numeric calculations."),
        ("Binary64 permission", "Binary64 is allowed for treasury calculations."),
        ("Single-precision permission", "Single-precision binary floating point is permitted."),
        ("Treasury-specific exception", "The treasury carry subsystem may use binary representation."),
        ("Fractional carry permission", "Fractional carry is permitted."),
        ("Conditional alternative representation", "Only when the subsystem uses an alternative representation may it calculate."),
        ("Decimal representation", "Numeric calculations may use decimal representation."),
    ):
        mut = _replace_text(b04_base, "No formula uses binary floating point.",
                            "No formula uses binary floating point. " + exception)
        expect_fail_with(f"CLOSURE-FINAL: {label} rejected", "14A-54", {"REG_B-04": mut}, "semantic-contract")
    long_exception = ("No formula uses binary floating point. " + ("Background text. " * 20) +
                      "Except the treasury subsystem may use binary representation.")
    expect_fail_with("CLOSURE-FINAL: long-distance exception rejected", "14A-54",
                     {"REG_B-04": _replace_text(b04_base, "No formula uses binary floating point.", long_exception)},
                     "semantic-contract")

    # ---- CONTRACT (D-238): typed contracts replace the lexical acceptance gate ----
    contract_mod = _contract_module()
    contract_report = _contract_report()
    bad_contract = [f"{c['id']}: {contract_mod.fmt(p)}" for c in contract_report.get("checks", [])
                    if not c["passed"] for p in c.get("problems", [])]
    cases.append(("CONTRACT: production validation passes", contract_report.get("status") == "PASS", bad_contract))
    for case, expected in (("D-998", "CONTRACT_EVIDENCE_PROPOSITION_MISMATCH"),
                           ("D-999", "CONTRACT_PROPOSITION_CONFLICT"),
                           ("D-990", "CONTRACT_EXCEPTION_UNSUPPORTED"),
                           ("D-991", "CONTRACT_PROPOSITION_CONFLICT"),
                           ("D-992", "CONTRACT_PROPOSITION_CONFLICT"),
                           ("D-993", "CONTRACT_EVIDENCE_NOT_REVIEWED")):
        result = contract_mod.validate_amendment(contract_mod.build_negative(case, 0))
        found = {p["code"] for gate in ("contract_gate", "evidence_gate", "authority_gate")
                 for p in result.get(gate, {}).get("problems", [])}
        cases.append((f"CONTRACT: {case} rejected for its semantic reason", not result["accepted"] and expected in found,
                      sorted(found) or ["accepted"]))
    result = contract_mod.validate_amendment(contract_mod.build_wording_positive())
    cases.append(("CONTRACT: Category B wording clarification accepted",
                  result["accepted"], [contract_mod.fmt(p) for gate in ("contract_gate", "evidence_gate", "authority_gate")
                                       for p in result.get(gate, {}).get("problems", [])] or ["rejected"]))
    result = contract_mod.validate_amendment(contract_mod.build_typed_positive())
    cases.append(("CONTRACT: typed Category B change with reviewed test evidence accepted",
                  result["accepted"], [contract_mod.fmt(p) for gate in ("contract_gate", "evidence_gate", "authority_gate")
                                       for p in result.get(gate, {}).get("problems", [])] or ["rejected"]))
    result = contract_mod.validate_amendment(contract_mod.build_typed_provisional())
    cases.append(("CONTRACT: Category C provisional change accepted and not promoted",
                  result["accepted"] and bool(result["evidence_gate"].get("provisional_open")),
                  [contract_mod.fmt(p) for gate in ("contract_gate", "evidence_gate", "authority_gate")
                   for p in result.get(gate, {}).get("problems", [])] or ["rejected or promoted"]))
    result = contract_mod.validate_amendment(contract_mod.build_owner_authorized())
    cases.append(("CONTRACT: owner-authorized Category A test proposition accepted in test mode",
                  result["accepted"], [contract_mod.fmt(p) for gate in ("contract_gate", "evidence_gate", "authority_gate")
                                       for p in result.get(gate, {}).get("problems", [])] or ["rejected"]))
    _b09_contract, b09_problems = contract_mod.build_b09_within_turn()
    cases.append(("CONTRACT: B-09 F-AL-006 within-turn cumulative accrual remains valid",
                  not b09_problems, [contract_mod.fmt(p) for p in b09_problems] or ["contract invalid"]))
    clarification = ("No formula uses binary floating point. The binary floating-point prohibition applies "
                     "to every formula calculation.")
    legacy_rejects = bool(_semantic_contract_violation("F-EC-000b", clarification))
    typed_accepts = contract_mod.validate_amendment(contract_mod.build_wording_positive())["accepted"]
    cases.append(("CONTRACT: retired lexical gate is diagnostic-only and cannot block a typed-clarification",
                  legacy_rejects and typed_accepts,
                  [f"legacy_rejects={legacy_rejects}", f"typed_accepts={typed_accepts}"]))

    passed = sum(1 for _, ok, _ in cases if ok)
    print("=" * 78)
    print("14A SELF-TESTS")
    print("=" * 78)
    for i, (name, ok, detail) in enumerate(cases, 1):
        print(f"{i:2d}. {'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            for d in detail[:5]:
                print("      " + str(d))
    print(f"\nSELF-TESTS: {passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1



def coverage_data():
    text = read(FILES["PARAMS"])
    inv = parse_param_inventory(text)
    exp_const = expected_constants(STAGE2)
    exp_form = expected_formulas(STAGE2)
    exp_fp = expected_fp(STAGE2)
    orders = ["B-02", "B-03", "B-04", "B-05", "B-06", "B-07", "B-08", "B-09", "B-10", "B-11", "B-12"]
    rows = {}
    for system in orders:
        r = {"records": 0, "values": 0, "units_m": 0, "units_x": 0, "units_d": 0,
             "pr_m": 0, "pr_x": 0, "pr_c": 0, "tim_m": 0, "tim_x": 0, "tim_c": 0,
             "auth": 0, "status": 0, "ev_m": 0, "ev_x": 0, "unparseable": 0}
        rows[system] = r
    for rec in inv["constants"]:
        system = rec["source"].split()[0]
        r = rows[system]
        r["records"] += 1; r["values"] += 1; r["auth"] += 1; r["status"] += 1
        if rec["unit"] in ("", "Not specified", "NOT SPECIFIED IN SOURCE"):
            r["units_x"] += 1
        else:
            r["units_m"] += 1
        r["pr_c"] += 1; r["tim_c"] += 1; r["ev_x"] += 1
    act_form = {x["id"]: x for x in inv["formulas"]}
    for fid, exp in exp_form.items():
        rec = act_form.get(fid)
        if not rec:
            continue
        system = exp["system"]; r = rows[system]
        r["records"] += 1; r["values"] += 1; r["auth"] += 1; r["status"] += 1
        if not exp.get("unit_field_present"):
            r["unparseable"] += 1
        else:
            tokens = _unit_tokens_r1(exp.get("unit_source", ""))
            if tokens:
                r["units_m"] += 1
            else:
                r["units_x"] += 1
        if exp.get("rounding"):
            r["pr_m"] += 1
        else:
            r["pr_x"] += 1
        if exp.get("timing"):
            r["tim_m"] += 1
        else:
            r["tim_x"] += 1
        r["ev_x"] += 1
    fp_actual = {x["id"]: x for x in inv["fp"]}
    for pid, exp in exp_fp.items():
        rec = fp_actual.get(pid)
        if not rec:
            continue
        r = rows["B-12"]
        r["records"] += 1; r["values"] += 1; r["auth"] += 1; r["status"] += 1
        if pid == "FP-P07":
            r["units_m"] += 1
        else:
            r["units_d"] += 1
        r["pr_x"] += 1; r["tim_x"] += 1; r["ev_m"] += 1
    for rec in inv["b02"]:
        r = rows["B-02"]
        r["records"] += 1; r["values"] += 1; r["auth"] += 1; r["status"] += 1
        r["units_m"] += 1; r["tim_m"] += 1; r["pr_x"] += 1; r["ev_x"] += 1
    for rec in inv["b03"]:
        r = rows["B-03"]
        r["records"] += 1; r["values"] += 1; r["auth"] += 1; r["status"] += 1
        r["units_m"] += 1; r["ev_m"] += 1; r["pr_x"] += 1; r["tim_x"] += 1
    return rows


def print_coverage():
    rows = coverage_data()
    print("PARAMETER SOURCE-COVERAGE MATRIX (records; matched/explicit/derived)")
    print("System | Records | Values | Units | Precision+rounding | Timing | Authority | Status | Evidence")
    print("---|---|---|---|---|---|---|---|---")
    total = {k: 0 for k in ("records", "units_m", "units_x", "units_d", "pr_m", "pr_x", "pr_c",
                            "tim_m", "tim_x", "tim_c", "ev_m", "ev_x", "unparseable")}
    for system in ("B-02", "B-03", "B-04", "B-05", "B-06", "B-07", "B-08", "B-09", "B-10", "B-11", "B-12"):
        r = rows[system]
        for k in total:
            total[k] += r.get(k, 0)
        units = f"{r['units_m']}m/{r['units_x']}x/{r['units_d']}d"
        pr = f"{r['pr_m']}m/{r['pr_x']}x/{r['pr_c']}c"
        tim = f"{r['tim_m']}m/{r['tim_x']}x/{r['tim_c']}c"
        ev = f"{r['ev_m']}m/{r['ev_x']}x"
        print(f"{system} | {r['records']} | {r['values']}/{r['records']} | {units} | {pr} | {tim} | {r['auth']}/{r['records']} | {r['status']}/{r['records']} | {ev}")
    print(f"TOTAL | {total['records']} | {total['records']}/{total['records']} | {total['units_m']}m/{total['units_x']}x/{total['units_d']}d | {total['pr_m']}m/{total['pr_x']}x/{total['pr_c']}c | {total['tim_m']}m/{total['tim_x']}x/{total['tim_c']}c | {total['records']}/{total['records']} | {total['records']}/{total['records']} | {total['ev_m']}m/{total['ev_x']}x")
    print(f"Unparseable source unit fields: {total['unparseable']}")


def main():
    if "--self-test" in sys.argv:
        return self_test()
    if "--coverage" in sys.argv:
        print_coverage()
        return 0
    results = validate()
    print("=" * 78)
    print("14A NUMERICAL FOUNDATION VALIDATOR — documentation quality only")
    print("=" * 78)
    failed = 0
    for cid, desc, problems in results:
        print(f"[{'PASS' if not problems else 'FAIL'}] {cid} {desc}")
        if problems:
            failed += 1
            for p in problems[:12]:
                print("      - " + str(p))
            if len(problems) > 12:
                print(f"      - … {len(problems) - 12} more")
    print("-" * 78)
    print(f"CHECKS: {len(results)}  FAILED: {failed}")
    print("RESULT:", "PASS — documentary consistency only." if not failed else "FAIL")
    print("NOT PROVEN: gameplay behaviour, balance, simulation, runtime execution or player experience.")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
