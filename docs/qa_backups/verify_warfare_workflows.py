#!/usr/bin/env python3
"""Hardened documentation validator for docs/stage-2/17_warfare_workflows_acceptance.md.

Verifies four things independently:

1. Document structure, the two-table WFA schema and every internal reference.
2. Traceability against the authoritative sources (requirements, B-10 rules,
   formula register, decision registers, failure codes, audit events).
3. D-014 / owner-reserved consistency and the fixed constraints.
4. Its own integrity: unique check IDs, a mutator per check, every declared
   check executed, and no check passing without evaluating an assertion.

Usage:
    python verify_warfare_workflows.py
    python verify_warfare_workflows.py --self-test

Exit codes: 0 = all checks passed, 1 = one or more checks failed,
2 = a required input file is missing.
"""

from __future__ import annotations

import difflib
import hashlib
import inspect
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
STAGE2 = ROOT / "docs" / "stage-2"
DOC_PATH = STAGE2 / "17_warfare_workflows_acceptance.md"
B10_PATH = STAGE2 / "17_warfare_and_settlements.md"
FORMULA_PATH = STAGE2 / "17_warfare_formula_register.md"
REQ_PATH = STAGE2 / "03_requirements_traceability.md"
DECISIONS_PATH = STAGE2 / "04_approved_and_provisional_decisions.md"
UNRESOLVED_PATH = STAGE2 / "05_unresolved_design_decisions.md"
PROGRESS_PATH = STAGE2 / "06_stage_2_progress_log.md"
AUTONOMY_PATH = ROOT / "docs" / "AUTONOMOUS_DECISION_POLICY.md"
DECISIONS_MD_PATH = ROOT / "docs" / "DECISIONS.md"
CATALOGUE_PATH = Path(__file__).resolve().parent / "warfare_fixture_catalogue.md"
REGISTRY_PATH = Path(__file__).resolve().parent / "warfare_fixture_registry.json"

B02_PATH = STAGE2 / "07_core_gameplay_loop_symbolic_world_and_turn_system.md"
SUBSYSTEM_DOCS = {
    2: STAGE2 / "09_account_onboarding_nation_creation_and_progression.md",
    3: STAGE2 / "10_economy_resources_treasury_and_finances.md",
    4: STAGE2 / "11_cities_infrastructure_production_and_research.md",
    5: STAGE2 / "12_population_and_domestic_politics.md",
    6: STAGE2 / "13_trade_and_markets.md",
    7: STAGE2 / "15_diplomacy.md",
    8: STAGE2 / "16_alliances.md",
}
CURRENT_STATUS_DOCS = [
    ROOT / "docs" / "AI_CONTEXT.md",
    ROOT / "docs" / "AI_HANDOFF.md",
    ROOT / "docs" / "PROJECT_PROGRESS.md",
    ROOT / "docs" / "ROADMAP.md",
    STAGE2 / "00_stage_2_handoff.md",
    STAGE2 / "01_stage_2_prompt_roadmap.md",
    STAGE2 / "02_master_game_design_bible_outline.md",
    STAGE2 / "03_requirements_traceability.md",
]

INPUTS = [
    DOC_PATH,
    B10_PATH,
    FORMULA_PATH,
    REQ_PATH,
    DECISIONS_PATH,
    UNRESOLVED_PATH,
    PROGRESS_PATH,
    AUTONOMY_PATH,
    DECISIONS_MD_PATH,
    B02_PATH,
    *SUBSYSTEM_DOCS.values(),
    CATALOGUE_PATH,
    REGISTRY_PATH,
    *CURRENT_STATUS_DOCS,
]

WFA_TOTAL = 124
WFE_TOTAL = 60
WFW_TOTAL = 40
CLASS_SIZES = {**{c: 8 for c in "ABCDEFGHIJKLMNO"}, "P": 4}
PHASES = {"OPEN", "P2", "P3.7", "P4.1", "P5", "P7"}
DEFINED_WRF = set(range(1, 15)) | set(range(20, 38))  # 32 codes
WRF_GAPS = {15, 16, 17, 18, 19}
OPERATION_WORKFLOWS = {
    "OP-01 RAID": ["WFW-007"],
    "OP-02 ASSAULT": ["WFW-008"],
    "OP-03 AIR_STRIKE": ["WFW-009"],
    "OP-04 BLOCKADE": ["WFW-010"],
    "OP-05 MISSILE_STRIKE": ["WFW-011", "WFW-012"],
    "OP-06 INTERCEPT": ["WFW-013"],
    "OP-07 FORTIFY": ["WFW-014"],
    "OP-08 BREAK_BLOCKADE": ["WFW-015"],
    "OP-09 RESUPPLY": ["WFW-016"],
}
EXTERNAL_RULE_PREFIX = ("MKT-", "TR-", "URB-", "DMP-", "ECN-", "AUD-AL-")

WORKFLOW_FIELDS = [
    "ID and name",
    "Purpose",
    "Initiating actor",
    "Permissions",
    "Preconditions",
    "Inputs",
    "Validation",
    "Player-visible information",
    "Decision points",
    "Consent",
    "System processing",
    "State transitions",
    "Resource consequences",
    "Notifications",
    "Audit and history",
    "Failure",
    "Cancellation and withdrawal",
    "Recovery",
    "Acceptance criteria",
    "B-10 rules",
    "Requirements",
    "Formulas",
    "Tests",
]

FORBIDDEN_PHRASES = [
    "province_id",
    "tile_id",
    "movement points",
    "adjacency bonus",
    "front line",
    "territory capture",
    "capture the city",
    "destroy the city",
    "facility_damage",
    "espionage operation",
    "nuclear strike",
    "population_casualty",
]


# --------------------------------------------------------------------------
# parsing helpers
# --------------------------------------------------------------------------


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def slice_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    i += len(start)
    j = text.find(end, i)
    return text[i:] if j < 0 else text[i:j]


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_rows(section: str):
    for line in section.splitlines():
        if line.startswith("|"):
            yield cells(line)


def expand(text: str, prefix: str, width: int = 3) -> list[int]:
    """Expand every `PREFIX-nnn`, `PREFIX-nnn–mmm` or `PREFIX-nnn–PREFIX-mmm`."""
    text = text.replace("`", "")
    out: list[int] = []
    pat = re.compile(
        prefix + r"-(\d{" + str(width) + r"})(?:[–-](?:" + prefix + r"-)?(\d{" + str(width) + r"}))?"
    )
    for m in pat.finditer(text):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        if b < a:
            continue
        out.extend(range(a, b + 1))
    return out


def ranges_cover(numbers: list[int], total: int) -> bool:
    return numbers == list(range(1, total + 1))


def unique(listing):
    return sorted(set(listing))


def parse_doc(doc: str) -> dict:
    ident: dict[str, dict] = {}
    beh: dict[str, dict] = {}
    wfe: dict[str, dict] = {}
    for line in doc.splitlines():
        if re.match(r"^\| `WFA-\d{3}` \|", line):
            c = cells(line)
            if len(c) == 10:
                ident[c[0].strip("`")] = {
                    "name": c[1], "class": c[2], "req": c[3], "wfw": c[4],
                    "wfe": c[5], "rules": c[6], "formula": c[7],
                    "definition": c[8], "execution": c[9], "raw": line,
                }
            elif len(c) == 13:
                beh[c[0].strip("`")] = {
                    "initial": c[1], "input": c[2], "phase": c[3], "validation": c[4],
                    "output": c[5], "mutation": c[6], "no_mutation": c[7],
                    "ledger": c[8], "audit": c[9], "failure": c[10],
                    "privacy": c[11], "evidence": c[12], "raw": line,
                }
        elif re.match(r"^\| `WFE-\d{3}` \|", line):
            c = cells(line)
            if len(c) == 6:
                wfe[c[0].strip("`")] = {
                    "class": c[1], "scenario": c[2], "expected": c[3],
                    "wfw": c[4], "test": c[5].strip("`"),
                }
    return {"wfa_ident": ident, "wfa_beh": beh, "wfe": wfe}


def workflow_blocks(doc: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    lines = doc.splitlines()
    starts = [i for i, l in enumerate(lines) if l.startswith("#### WFW-")]
    for idx, s in enumerate(starts):
        wid = lines[s][5:12]
        e = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        fields: dict[str, str] = {}
        for line in lines[s:e]:
            if line.startswith("|"):
                c = cells(line)
                if c:
                    fields[c[0].replace("**", "").strip()] = c[1] if len(c) > 1 else ""
        out[wid] = fields
    return out


class Ctx:
    def __init__(self, doc: str, docs: dict[str, str]):
        self.docs = docs
        self.parsed = parse_doc(doc)
        self.workflows = workflow_blocks(doc)
        self.counts: dict[str, int] = {}
        self.registry: list = []
        self.registry_override = None

    def need(self, cid: str, cond, msg: str, errs: list[str]) -> bool:
        self.counts[cid] = self.counts.get(cid, 0) + 1
        if not cond:
            errs.append(msg)
        return bool(cond)


# --------------------------------------------------------------------------
# authoritative inventories
# --------------------------------------------------------------------------


def b10_definitions(b10: str) -> tuple[dict[str, str], list[str]]:
    """Extract one definition per WAR identifier from B-10.

    A definition is a line that begins with the identifier in backticks,
    optionally wrapped in bold (WAR-168 is the one such line in v1.3).
    Occurrences elsewhere in the document are references, not definitions.
    """
    defs: dict[str, str] = {}
    dups: list[str] = []
    pat = re.compile(r"^(?:\*\*)?`(WAR-\d{3}[a-z]?)`(?:\*\*)?\s+(.*)$")
    for line in b10.splitlines():
        m = pat.match(line)
        if not m:
            continue
        rid = m.group(1)
        if rid in defs:
            dups.append(rid)
        else:
            defs[rid] = m.group(2).strip()
    return defs, dups


def b10_numbered(b10: str) -> set[int]:
    return {int(rid[4:]) for rid in b10_definitions(b10)[0] if len(rid) == 7}


def b10_lettered(b10: str) -> set[str]:
    return {rid for rid in b10_definitions(b10)[0] if len(rid) == 8}


def register_formulas(reg: str) -> set[int]:
    return {int(m) for m in re.findall(r"^### F-WR-(\d{3}) — ", reg, re.M)}


def authoritative_requirements(reqs: str) -> set[int]:
    return {int(m) for m in re.findall(r"^\| REQ-(\d{3}) \|", reqs, re.M)}


def unresolved_status(ud: str, ident: str) -> str | None:
    m = re.search(r"^\| `" + re.escape(ident) + r"` \| ([^|]+) \|", ud, re.M)
    return m.group(1).strip() if m else None


IDENT_RE = re.compile(
    r"\b(?:WAR-\d{3}[a-z]?|WRF-\d{2}|WRA-\d{2}|F-WR-\d{3}|WFW-\d{3}|WFE-\d{3}|"
    r"WFA-\d{3}|REQ-\d{3}|B10-AD-\d{2}|B10-C\d{2}|AUD-AL-\d{3}|AT-E\d{2}|"
    r"[A-Z]{2,4}-[A-Z]?\d{2,3}[a-z]?)\b"
)
NA_IDENT_RE = re.compile(r"\b(?:" + IDENT_RE.pattern + r"|D-\d{3}|DD-\d{3})\b")
BARE_NONE = {"n/a", "n/a.", "none", "none.", "—", "-", "--", "n.a.", "n.a"}
NA_PLACEHOLDERS = {
    "n/a", "na", "n.a.", "none", "no", "reason", "no reason", "because",
    "not applicable", "not relevant", "irrelevant", "no details", "no detail",
    "tbd", "todo", "placeholder", "unknown", "nothing",
}

# Vocabulary observed in the canonical 124-record corpus.  A mandatory cell that
# says N/A or none must explain why the field does not apply, using language that
# belongs to that field rather than a bare placeholder.
FIELD_JUSTIFICATION = {
    "formula": (
        "formula", "arithmetic", "calculation", "calculat", "computation",
        "equation", "numeric", "threshold", "catalogue", "enumeration", "check",
        "rule", "operation", "set",
    ),
    "audit": (
        "event", "record", "writ", "log", "audit", "reject", "read", "query",
        "duty", "confirmation", "repair", "ledger", "trade", "visibility",
    ),
    "ledger": (
        "ledger", "reservation", "reserve", "value", "item", "transfer",
        "balance", "movement", "move", "op", "resource", "crown", "accounting",
        "reparation", "settle", "debit", "credit", "record", "confirmation",
        "resolution", "reject",
    ),
    "failure": (
        "failure", "fail", "wrf", "code", "lawful", "outcome", "positive",
        "terminal", "invariant", "replay", "ignor", "bound", "band", "label",
        "structural", "refus", "reject", "suppress", "retention", "determinism",
        "property",
    ),
    "wfe": (
        "boundary", "rule", "path", "window", "deadline", "operation",
        "restricted", "variant", "scenario", "accounting", "visibility",
        "determinism", "priority", "cap", "tier", "no §9", "expiry", "city",
        "protection", "leak", "access", "administrative",
    ),
}


def _resolve_any_ident(tok: str, docs: dict[str, str]) -> bool:
    """True when an identifier is defined in the authoritative project sources."""
    if tok.startswith("D-") or tok.startswith("DD-"):
        return tok in docs.get("decisions_md", "") or tok in docs.get("decisions", "")
    if tok.startswith("UD-"):
        return (unresolved_status(docs.get("unresolved", ""), tok) is not None
                or tok in docs.get("decisions_md", ""))
    if tok.startswith("OP-"):
        return re.fullmatch(r"OP-0[1-9]", tok) is not None
    if tok.startswith("B10-AD-"):
        n = int(tok[8:])
        return 1 <= n <= 25 and tok in docs.get("b10", "")
    if tok.startswith("B10-C"):
        n = int(tok[5:])
        return 1 <= n <= 34 and tok in docs.get("b10", "")
    if tok.startswith("WRF-"):
        return int(tok[4:]) in DEFINED_WRF
    return _resolve_ident(tok, docs, "*")


def _na_reason(value: str) -> tuple[bool, str]:
    """Split an N/A, NONE or em-dash expression from its stated reason."""
    m = re.match(r"^(N/A|N\.A\.?|NA|NONE)\b\s*(?:[—–:;\-]\s*)?(.*)$", value, re.I)
    if m:
        return True, m.group(2).strip()
    if value[:1] in ("—", "–"):
        return True, value[1:].lstrip("—–:;- ").strip()
    if re.match(r"^-{1,2}\s", value) or value in ("-", "--"):
        return True, ""
    return False, ""


def _field_justification(field: str, reason: str, ids: list[str]) -> bool:
    low = reason.lower()
    keywords = FIELD_JUSTIFICATION[field]
    if field == "wfe":
        return bool(ids) or bool(re.search(r"§\d", reason)) or any(k in low for k in keywords)
    if field == "audit":
        return bool(ids) or any(k in low for k in keywords)
    return any(k in low for k in keywords)


def _validate_na_reason(reason: str, field: str | None, ctx) -> tuple[bool, str]:
    reason = reason.strip()
    if not reason:
        return False, "N/A or none has no reason"
    stripped = reason.lower().strip(" .:;,-—–")
    if stripped in NA_PLACEHOLDERS:
        return False, "N/A or none uses a placeholder reason"
    if re.fullmatch(r"(?i)reason\s*[:.]?", reason.strip(" .")):
        return False, "N/A or none uses a placeholder reason"
    if len(re.findall(r"[A-Za-z]", reason)) < 5:
        return False, "N/A or none has no meaningful reason"
    ids = NA_IDENT_RE.findall(reason)
    if ctx is not None:
        for tok in ids:
            if not _resolve_any_ident(tok, ctx.docs):
                return False, f"N/A or none cites unresolved identifier {tok}"
    words = re.findall(r"[A-Za-z]{2,}", reason)
    if (len(words) < 2 and not ids and not re.search(r"§\d", reason)
            and not (len(words) == 1 and len(words[0]) >= 8)):
        return False, "N/A or none has no meaningful reason"
    if field in FIELD_JUSTIFICATION and not _field_justification(field, reason, ids):
        return False, f"N/A or none explanation is not specific to {field}"
    return True, ""


def justified_value(cell: str, field: str | None = None, ctx=None) -> tuple[bool, str]:
    """Validate a mandatory value without letting an identifier bypass N/A rules.

    Processing order: empty and bare-placeholder rejection; N/A/NONE extraction;
    reason meaning; every identifier inside the explanation; field applicability;
    then ordinary values with every named identifier resolved.  An N/A expression
    is never accepted merely because its explanation contains a token that looks
    like an identifier.
    """
    s = (cell or "").strip()
    if not s:
        return False, "empty mandatory field"
    if not any(ch.isalnum() for ch in s):
        return False, "punctuation-only mandatory value"
    if s.lower() in BARE_NONE:
        return False, "bare N/A or none without a reason"
    is_na, reason = _na_reason(s)
    if is_na:
        return _validate_na_reason(reason, field, ctx)
    if ctx is not None:
        for tok in NA_IDENT_RE.findall(s):
            if not _resolve_any_ident(tok, ctx.docs):
                return False, f"unresolved identifier {tok}"
    return True, ""


def parse_war_ranges(doc: str) -> list[dict]:
    sec = slice_between(doc, "### 14.3 Every numbered WAR rule", "**14.3.1")
    rows: list[dict] = []
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 4 or not re.match(r"`WAR-\d{3}`", c[0]):
            continue
        rows.append({
            "ids": expand(c[0], "WAR"),
            "subject": c[1],
            "wfws": expand(c[2], "WFW"),
            "tests": expand(c[3], "WFA"),
            "raw": line,
        })
    return rows


def war_dispositions(ctx, doc: str) -> dict[str, dict]:
    """Derive one disposition record for every numbered and lettered rule."""
    ident = ctx.parsed["wfa_ident"]
    exact: dict[str, set[str]] = {}
    for wid, v in ident.items():
        for n in expand(v["rules"], "WAR"):
            exact.setdefault(f"WAR-{n:03d}", set()).add(wid)
        for lr in re.findall(r"WAR-\d{3}[a-z]", v["rules"]):
            exact.setdefault(lr, set()).add(wid)
    defs, _dups = b10_definitions(ctx.docs["b10"])
    rows = parse_war_ranges(doc)
    by_number = {n: row for row in rows for n in row["ids"]}
    out: dict[str, dict] = {}
    for n in sorted(b10_numbered(ctx.docs["b10"])):
        rid = f"WAR-{n:03d}"
        row = by_number.get(n)
        if rid in exact:
            tests = sorted(exact[rid])
            out[rid] = {"kind": "DIRECT", "workflows": sorted({
                f"WFW-{w:03d}" for t in tests for w in expand(ident[t]["wfw"], "WFW")}),
                "tests": tests, "formula": ident[tests[0]]["formula"],
                "source": "§14.3.3 / §14.3.5", "row": row}
        elif row and row["wfws"] and row["tests"]:
            known = [f"WFA-{t:03d}" for t in row["tests"] if f"WFA-{t:03d}" in ident]
            if not known:
                out[rid] = {"kind": "NOT COVERED", "workflows": [], "tests": [],
                            "formula": "", "source": "", "row": row}
                continue
            out[rid] = {"kind": "SUPPORTING",
                        "workflows": [f"WFW-{w:03d}" for w in row["wfws"]],
                        "tests": [f"WFA-{t:03d}" for t in row["tests"]],
                        "formula": ident[known[0]]["formula"],
                        "source": f"§14.3 range {row['ids'][0]:03d}–{row['ids'][-1]:03d}",
                        "row": row}
        else:
            out[rid] = {"kind": "NOT COVERED", "workflows": [], "tests": [],
                        "formula": "", "source": "", "row": row}
    lettered_sec = slice_between(doc, "**14.3.1 The 42 lettered sub-rules.**", "**14.3.2")
    lrows = {}
    for line in lettered_sec.splitlines():
        c = cells(line) if line.startswith("|") else []
        if c and re.match(r"`WAR-\d{3}[a-z]`", c[0]):
            lrows[c[0].strip("`")] = c
    for rid in sorted(b10_lettered(ctx.docs["b10"])):
        c = lrows.get(rid)
        tests = sorted(exact.get(rid, set()))
        if c and len(c) >= 4:
            listed_test = re.search(r"WFA-\d{3}", c[3])
            listed_wfws = expand(c[2], "WFW")
            if not tests and listed_test and listed_test.group(0) in ident:
                tests = [listed_test.group(0)]
            kind = "DIRECT" if exact.get(rid) else (
                "SUPPORTING" if tests and listed_wfws else "NOT COVERED")
            out[rid] = {"kind": kind,
                        "workflows": [f"WFW-{w:03d}" for w in listed_wfws],
                        "tests": tests,
                        "formula": ident[tests[0]]["formula"] if tests else "",
                        "source": "§14.3.1", "row": None}
        else:
            out[rid] = {"kind": "NOT COVERED", "workflows": [], "tests": [],
                        "formula": "", "source": "", "row": None}
    return out


# --------------------------------------------------------------------------
# checks 01-08 — structure
# --------------------------------------------------------------------------


def check_01(doc, ctx, cid):
    errs = []
    for needle in (
        "**Version:** 1.0",
        "Stage 2, Prompt 10C",
        "Acceptance specification",
        "**Status:** **Acceptance specification — design only.**",
    ):
        ctx.need(cid, needle in doc, f"header missing {needle!r}", errs)
    return errs


def check_02(doc, ctx, cid):
    sec = slice_between(doc, "**1.7 Fixed constraints", "---")
    errs = []
    ctx.need(cid, len(re.findall(r"^\d+\. \*\*", sec, re.M)) == 8,
             "expected 8 fixed constraints", errs)
    for needle in (
        "**Documentation only.**",
        "**Mapless.**",
        "`OP-08` is `BREAK_BLOCKADE`",
        "**Espionage is not authorized**",
        "**No city or facility destruction.**",
        "**Operations Points unchanged.**",
        "`available = max(0, op_balance − reserved)`",
        "including a recorded 0 at the cap",
        "**No provisional promotion.**",
        "**Owner-reserved decisions untouched.**",
        "`UD-040`–`UD-049` remain **Open**",
        "**Protected decisions preserved.**",
        "D-014, D-015, D-027, D-122, DD-136, `REQ-513`",
        "Global Trade gates G-1–G-6",
    ):
        ctx.need(cid, needle in sec, f"constraint text missing {needle!r}", errs)
    return errs


def check_03(doc, ctx, cid):
    errs = []
    for label in OPERATION_WORKFLOWS:
        ctx.need(cid, f"`{label}`" in doc, f"operation catalogue missing {label}", errs)
    ctx.need(cid, not re.search(r"\bOP-(1[0-9]|[2-9][0-9])\b", doc),
             "an operation beyond OP-09 is referenced", errs)
    return errs


def check_04(doc, ctx, cid):
    sec = slice_between(doc, "### 2.4 The complete 25-step campaign lifecycle", "**2.4.1**")
    nums = [int(c[0]) for c in table_rows(sec) if c and c[0].isdigit()]
    errs = []
    ctx.need(cid, nums == list(range(1, 26)), f"lifecycle steps must be 1..25, found {nums}", errs)
    return errs


def check_05(doc, ctx, cid):
    ids = [int(n) for n in re.findall(r"^#### WFW-(\d{3}) — ", doc, re.M)]
    errs = []
    ctx.need(cid, ids == list(range(1, WFW_TOTAL + 1)),
             f"workflow headings must be WFW-001..040 in order, found {ids}", errs)
    ctx.need(cid, len(set(ids)) == len(ids), "duplicate WFW heading", errs)
    return errs


def check_06(doc, ctx, cid):
    errs = []
    for wid, fields in sorted(ctx.workflows.items()):
        found = [f for f in fields if f in WORKFLOW_FIELDS]
        ctx.need(cid, found == WORKFLOW_FIELDS,
                 f"{wid}: fields differ (found {len(found)} of {len(WORKFLOW_FIELDS)})", errs)
    ctx.need(cid, len(ctx.workflows) == WFW_TOTAL,
             f"expected 40 workflow blocks, found {len(ctx.workflows)}", errs)
    return errs


def check_07(doc, ctx, cid):
    ids = [int(n) for n in re.findall(r"^\*\*J(\d+) — ", doc, re.M)]
    errs = []
    ctx.need(cid, ids == list(range(1, 18)), f"journeys must be J1..J17, found {ids}", errs)
    return errs


def check_08(doc, ctx, cid):
    wfe = ctx.parsed["wfe"]
    errs = []
    ctx.need(cid, len(wfe) == WFE_TOTAL, f"expected 60 edge cases, found {len(wfe)}", errs)
    ctx.need(cid, sorted(wfe) == [f"WFE-{i:03d}" for i in range(1, WFE_TOTAL + 1)],
             "edge-case IDs are not WFE-001..060", errs)
    return errs


# --------------------------------------------------------------------------
# checks 09-20 — WFA schema and reverse coverage
# --------------------------------------------------------------------------


def check_09(doc, ctx, cid):
    ident, beh = ctx.parsed["wfa_ident"], ctx.parsed["wfa_beh"]
    errs = []
    ctx.need(cid, len(ident) == WFA_TOTAL, f"expected 124 identification rows, found {len(ident)}", errs)
    ctx.need(cid, len(beh) == WFA_TOTAL, f"expected 124 behaviour rows, found {len(beh)}", errs)
    ctx.need(cid, set(ident) == set(beh),
             f"identification and behaviour sets differ: {sorted(set(ident) ^ set(beh))}", errs)
    ctx.need(cid, sorted(ident) == [f"WFA-{i:03d}" for i in range(1, WFA_TOTAL + 1)],
             "test IDs are not WFA-001..124", errs)
    return errs


def check_10(doc, ctx, cid):
    errs = []
    ident = ctx.parsed["wfa_ident"]
    auth = authoritative_requirements(ctx.docs["reqs"])
    for wid, v in sorted(ident.items()):
        for field in ("name", "class", "req", "wfw", "wfe", "rules", "formula"):
            ctx.need(cid, bool(v[field]), f"{wid}: empty {field}", errs)
        ctx.need(cid, v["class"] in CLASS_SIZES, f"{wid}: invalid class {v['class']!r}", errs)
        ctx.need(cid, v["definition"] == "COMPLETE", f"{wid}: Definition is {v['definition']!r}", errs)
        ctx.need(cid, v["execution"] == "NOT RUN", f"{wid}: Execution is {v['execution']!r}", errs)
        reqs = expand(v["req"], "REQ")
        ctx.need(cid, bool(reqs), f"{wid}: no requirement reference", errs)
        for r in reqs:
            ctx.need(cid, r in auth, f"{wid}: REQ-{r} is not in the authoritative requirement register", errs)
        ctx.need(cid, v["formula"].startswith("`F-WR-") or v["formula"].startswith("N/A")
                 or v["formula"].startswith("all "),
                 f"{wid}: formula cell is neither F-WR- nor N/A", errs)
    return errs


def check_11(doc, ctx, cid):
    errs = []
    for wid, v in sorted(ctx.parsed["wfa_beh"].items()):
        for field in ("initial", "input", "phase", "validation", "output", "mutation",
                      "no_mutation", "ledger", "audit", "failure", "privacy", "evidence"):
            ctx.need(cid, bool(v[field]), f"{wid}: empty behaviour field {field}", errs)
        ctx.need(cid, v["phase"] in PHASES, f"{wid}: invalid phase {v['phase']!r}", errs)
        ctx.need(cid, ("WRF-" in v["failure"]) or v["failure"].startswith("N/A"),
                 f"{wid}: failure cell names no WRF and no N/A reason", errs)
        ctx.need(cid, ("WRA-" in v["audit"]) or v["audit"].startswith("none") or "no " in v["audit"],
                 f"{wid}: audit cell names no WRA and no none reason", errs)
        ctx.need(cid, any(k in v["ledger"] for k in ("none", "HELD", "CONSUMED", "RELEASED", "REGENERATED", "recorded", "WRA-")),
                 f"{wid}: ledger cell names no ledger state", errs)
    return errs


def check_12(doc, ctx, cid):
    counts: dict[str, int] = {}
    for v in ctx.parsed["wfa_ident"].values():
        counts[v["class"]] = counts.get(v["class"], 0) + 1
    errs = []
    ctx.need(cid, counts == CLASS_SIZES, f"class distribution {counts} != {CLASS_SIZES}", errs)
    return errs


def check_13(doc, ctx, cid):
    errs = []
    ident = ctx.parsed["wfa_ident"]
    for eid, v in sorted(ctx.parsed["wfe"].items()):
        ctx.need(cid, v["test"] in ident, f"{eid}: primary test {v['test']} does not exist", errs)
        if v["test"] in ident:
            ctx.need(cid, ident[v["test"]]["class"] == v["class"],
                     f"{eid}: class {v['class']} disagrees with {v['test']} class {ident[v['test']]['class']}", errs)
    return errs


def check_14(doc, ctx, cid):
    errs = []
    known = set(ctx.parsed["wfe"])
    for wid, v in sorted(ctx.parsed["wfa_ident"].items()):
        refs = re.findall(r"WFE-\d{3}", v["wfe"])
        ctx.need(cid, bool(refs) or v["wfe"].startswith("—"),
                 f"{wid}: unreadable edge-case cell {v['wfe']!r}", errs)
        for r in refs:
            ctx.need(cid, r in known, f"{wid}: unknown {r}", errs)
    return errs


def check_15(doc, ctx, cid):
    errs = []
    for wid, v in sorted(ctx.parsed["wfa_ident"].items()):
        refs = expand(v["wfw"], "WFW")
        ctx.need(cid, bool(refs), f"{wid}: no workflow reference", errs)
        for r in refs:
            ctx.need(cid, 1 <= r <= WFW_TOTAL, f"{wid}: unknown WFW-{r:03d}", errs)
    return errs


def check_16(doc, ctx, cid):
    errs = []
    auth = authoritative_requirements(ctx.docs["reqs"])
    for wid, v in sorted(ctx.parsed["wfa_ident"].items()):
        refs = expand(v["req"], "REQ")
        ctx.need(cid, bool(refs), f"{wid}: no requirement reference", errs)
        for r in refs:
            ctx.need(cid, 654 <= r <= 703, f"{wid}: REQ-{r} outside REQ-654–REQ-703", errs)
            ctx.need(cid, r in auth, f"{wid}: REQ-{r} absent from the authoritative register", errs)
    return errs


def check_17(doc, ctx, cid):
    errs = []
    numbered = b10_numbered(ctx.docs["b10"])
    lettered = b10_lettered(ctx.docs["b10"])
    for wid, v in sorted(ctx.parsed["wfa_ident"].items()):
        cell = v["rules"]
        recognized = (
            "WAR-" in cell or "WRF-" in cell or "all B-10 rules" in cell
            or any(p in cell for p in EXTERNAL_RULE_PREFIX)
        )
        ctx.need(cid, recognized, f"{wid}: rules cell names no recognized rule source", errs)
        for n in expand(cell, "WAR"):
            ctx.need(cid, n in numbered, f"{wid}: WAR-{n:03d} is not in the B-10 inventory", errs)
        for lr in re.findall(r"WAR-\d{3}[a-z]", cell):
            ctx.need(cid, lr in lettered, f"{wid}: {lr} is not a B-10 lettered sub-rule", errs)
        for g in re.findall(r"WRF-(\d{2})", cell):
            ctx.need(cid, int(g) not in WRF_GAPS, f"{wid}: cites unallocated WRF-{g}", errs)
            ctx.need(cid, int(g) in DEFINED_WRF, f"{wid}: cites undefined WRF-{g}", errs)
        for a in re.findall(r"WRA-(\d{2})", cell):
            ctx.need(cid, 1 <= int(a) <= 14, f"{wid}: unknown WRA-{a}", errs)
        for f in re.findall(r"F-WR-(\d{3})", cell):
            ctx.need(cid, 1 <= int(f) <= 39, f"{wid}: unknown F-WR-{f}", errs)
    return errs


def check_18(doc, ctx, cid):
    errs = []
    ident = ctx.parsed["wfa_ident"]
    for n in range(1, WFW_TOTAL + 1):
        wfw = f"WFW-{n:03d}"
        tests = [wid for wid, v in ident.items()
                 if wfw in [f"WFW-{x:03d}" for x in expand(v["wfw"], "WFW")] and wid != "WFA-120"]
        ctx.need(cid, bool(tests), f"{wfw}: no dedicated test outside the end-to-end scenario", errs)
    return errs


def check_19(doc, ctx, cid):
    errs = []
    ident = ctx.parsed["wfa_ident"]
    for eid, v in sorted(ctx.parsed["wfe"].items()):
        test = v["test"]
        cited = test in ident and eid in re.findall(r"WFE-\d{3}", ident[test]["wfe"])
        ctx.need(cid, cited, f"{eid}: its primary test {test} does not cite it", errs)
    return errs


def check_20(doc, ctx, cid):
    errs = []
    ident = ctx.parsed["wfa_ident"]
    for label, wfws in OPERATION_WORKFLOWS.items():
        for wfw in wfws:
            tests = [wid for wid, v in ident.items()
                     if wfw in [f"WFW-{x:03d}" for x in expand(v["wfw"], "WFW")] and wid != "WFA-120"]
            ctx.need(cid, bool(tests), f"{label} ({wfw}) has no dedicated test", errs)
    return errs


# --------------------------------------------------------------------------
# checks 21-30 — forward traceability
# --------------------------------------------------------------------------


def check_21(doc, ctx, cid):
    sec = slice_between(doc, "### 14.2 Requirements REQ-654–REQ-703", "### 14.3")
    ids = [int(c[0].split("-")[1]) for c in table_rows(sec)
           if c and re.fullmatch(r"REQ-\d{3}", c[0])]
    errs = []
    ctx.need(cid, ids == list(range(654, 704)), f"requirement rows must be 654..703, found {len(ids)}", errs)
    return errs


def check_22(doc, ctx, cid):
    sec = slice_between(doc, "### 14.2 Requirements REQ-654–REQ-703", "### 14.3")
    counts = {"direct": 0, "supporting": 0, "deferred": 0, "uncovered": 0}
    for c in table_rows(sec):
        if not (c and re.fullmatch(r"REQ-\d{3}", c[0])):
            continue
        if c[2].startswith("DIRECT VERIFICATION"):
            counts["direct"] += 1
        elif c[2].startswith("**SUPPORTING VERIFICATION**"):
            counts["supporting"] += 1
        elif c[2].startswith("**DEFERRED**"):
            counts["deferred"] += 1
        elif c[2].startswith("NOT COVERED"):
            counts["uncovered"] += 1
    errs = []
    ctx.need(cid, (counts["direct"], counts["supporting"], counts["deferred"], counts["uncovered"])
             == (44, 1, 5, 0), f"classification totals {counts} != (44, 1, 5, 0)", errs)
    for phrase in ("44 DIRECT VERIFICATION", "1 SUPPORTING VERIFICATION", "5 DEFERRED", "0 NOT COVERED"):
        ctx.need(cid, phrase in doc, f"totals statement missing {phrase!r}", errs)
    return errs


def check_23(doc, ctx, cid):
    sec = slice_between(doc, "### 14.2 Requirements REQ-654–REQ-703", "### 14.3")
    ident = ctx.parsed["wfa_ident"]
    errs = []
    for c in table_rows(sec):
        if not (c and re.fullmatch(r"REQ-\d{3}", c[0])) or len(c) < 5:
            continue
        req = c[0]
        wfws = expand(c[3], "WFW")
        ctx.need(cid, bool(wfws) or c[3].strip() == "all", f"{req}: no workflow reference", errs)
        for w in wfws:
            ctx.need(cid, 1 <= w <= WFW_TOTAL, f"{req}: unknown WFW-{w:03d}", errs)
        tests = re.findall(r"WFA-\d{3}", c[4])
        ctx.need(cid, bool(tests) or c[4].strip() == "all", f"{req}: no test reference", errs)
        for t in tests:
            ctx.need(cid, t in ident, f"{req}: unknown {t}", errs)
    return errs


def check_24(doc, ctx, cid):
    sec = slice_between(doc, "### 14.4 All 39 formulas", "### 14.5")
    ids = [int(m) for m in re.findall(r"^\| `F-WR-(\d{3})` \|", sec, re.M)]
    reg = register_formulas(ctx.docs["register"])
    errs = []
    ctx.need(cid, ids == list(range(1, 40)), f"formula rows must be 001..039, found {ids}", errs)
    ctx.need(cid, set(ids) == reg, f"formula set differs from the register: {sorted(set(ids) ^ reg)}", errs)
    return errs


def check_25(doc, ctx, cid):
    sec = slice_between(doc, "### 14.4 All 39 formulas", "### 14.5")
    ident = ctx.parsed["wfa_ident"]
    errs = []
    for c in table_rows(sec):
        if not (c and re.fullmatch(r"`F-WR-\d{3}`", c[0])):
            continue
        fid = c[0].strip("`")
        if len(c) < 4:
            ctx.need(cid, False, f"{fid}: row has fewer than four cells", errs)
            continue
        wfws = expand(c[2], "WFW")
        ctx.need(cid, bool(wfws) or c[2].strip() == "all", f"{fid}: no workflow reference", errs)
        for w in wfws:
            ctx.need(cid, 1 <= w <= WFW_TOTAL, f"{fid}: unknown WFW-{w:03d}", errs)
        tests = re.findall(r"WFA-\d{3}", c[3])
        ctx.need(cid, bool(tests), f"{fid}: no test reference", errs)
        for t in tests:
            ctx.need(cid, t in ident, f"{fid}: unknown {t}", errs)
    ctx.need(cid, "DEFERRED to Prompt 14" in sec, "F-WR-035 calibration deferral is not stated", errs)
    return errs


def check_26(doc, ctx, cid):
    sec = slice_between(doc, "### 14.5 The fourteen audit events", "### 14.6")
    ident = ctx.parsed["wfa_ident"]
    rows = [c for c in table_rows(sec) if c and re.match(r"`WRA-\d{2}`", c[0])]
    errs = []
    ctx.need(cid, len(rows) == 14, f"expected 14 audit rows, found {len(rows)}", errs)
    for c in rows:
        eid = re.search(r"WRA-\d{2}", c[0]).group(0)
        if len(c) != 7:
            ctx.need(cid, False, f"{eid}: expected 7 columns, found {len(c)}", errs)
            continue
        for idx, field in ((2, "timing"), (3, "actor/visibility"), (6, "replay")):
            ctx.need(cid, bool(c[idx]), f"{eid}: empty {field}", errs)
        ctx.need(cid, bool(expand(c[4], "WFW")), f"{eid}: no workflow use", errs)
        for w in expand(c[4], "WFW"):
            ctx.need(cid, 1 <= w <= WFW_TOTAL, f"{eid}: unknown WFW-{w:03d}", errs)
        tests = re.findall(r"WFA-\d{3}", c[5])
        ctx.need(cid, bool(tests), f"{eid}: no test reference", errs)
        for t in tests:
            ctx.need(cid, t in ident, f"{eid}: unknown {t}", errs)
    return errs


def check_27(doc, ctx, cid):
    sec = slice_between(doc, "**10.2 Identifier span and defined codes.**", "**10.3")
    ids = sorted({int(m) for m in re.findall(r"^\| `WRF-(\d{2})` \|", sec, re.M)})
    ident, beh = ctx.parsed["wfa_ident"], ctx.parsed["wfa_beh"]
    errs = []
    ctx.need(cid, set(ids) == DEFINED_WRF, f"defined WRF codes differ from the 32-code set: {ids}", errs)
    for gap in sorted(WRF_GAPS):
        ctx.need(cid, not re.search(rf"\| `WRF-{gap:02d}` \|", sec),
                 f"WRF-{gap:02d} is unallocated but appears as a defined row", errs)
    ctx.need(cid, "unallocated" in sec, "gap disclosure text missing", errs)
    cited: set[int] = set()
    for v in ident.values():
        cited |= {int(x) for x in re.findall(r"WRF-(\d{2})", v["rules"])}
    for v in beh.values():
        cited |= {int(x) for x in re.findall(r"WRF-(\d{2})", v["failure"])}
    for code in sorted(DEFINED_WRF):
        ctx.need(cid, code in cited, f"WRF-{code:02d} is defined but no test cites it", errs)
    for gap in sorted(WRF_GAPS):
        ctx.need(cid, gap not in cited, f"a test cites unallocated WRF-{gap:02d}", errs)
    return errs


def check_28(doc, ctx, cid):
    sec = slice_between(doc, "**14.7.1 `B10-AD-01`–`B10-AD-25`.**", "**14.7.2")
    ids = [int(m) for m in re.findall(r"^\| `B10-AD-(\d{2})` \|", sec, re.M)]
    b10_ad = {int(m) for m in re.findall(r"B10-AD-(\d{2})", ctx.docs["b10"])}
    ident = ctx.parsed["wfa_ident"]
    errs = []
    ctx.need(cid, ids == list(range(1, 26)), f"B10-AD rows must be 01..25, found {ids}", errs)
    ctx.need(cid, b10_ad == set(range(1, 26)), f"B-10 AD set is {sorted(b10_ad)}", errs)
    for c in table_rows(sec):
        if not (c and re.match(r"`B10-AD-\d{2}`", c[0])):
            continue
        if len(c) < 4:
            ctx.need(cid, False, f"{c[0]}: row is incomplete", errs)
            continue
        tests = re.findall(r"WFA-\d{3}", c[3])
        ctx.need(cid, bool(tests), f"{c[0]}: no test disposition", errs)
        for t in tests:
            ctx.need(cid, t in ident, f"{c[0]}: unknown {t}", errs)
    return errs


def check_29(doc, ctx, cid):
    sec = slice_between(doc, "**14.7.2 `B10-C01`–`B10-C34`.**", "### 14.8")
    ids = [int(m) for m in re.findall(r"^\| `B10-C(\d{2})` \|", sec, re.M)]
    b10_c = {int(m) for m in re.findall(r"B10-C(\d{2})", ctx.docs["b10"])}
    errs = []
    ctx.need(cid, ids == list(range(1, 35)), f"B10-C rows must be 01..34, found {ids}", errs)
    ctx.need(cid, b10_c == set(range(1, 35)), f"B-10 conflict set is {sorted(b10_c)}", errs)
    for c in table_rows(sec):
        if c and re.match(r"`B10-C\d{2}`", c[0]):
            ctx.need(cid, len(c) >= 3 and all(x for x in c[:3]), f"{c[0]}: incomplete disposition", errs)
    return errs


def check_30(doc, ctx, cid):
    sec = slice_between(doc, "### 14.9 Subsystem and prompt integration rows", "### 14.10")
    rows = [c for c in table_rows(sec) if c and c[0].isdigit()]
    ident = ctx.parsed["wfa_ident"]
    wfe = set(ctx.parsed["wfe"])
    errs = []
    ctx.need(cid, len(rows) == 13, f"expected 13 integration rows, found {len(rows)}", errs)
    for c in rows:
        tag = f"integration row {c[0]}"
        if len(c) != 14:
            ctx.need(cid, False, f"{tag}: expected 14 columns, found {len(c)}", errs)
            continue
        for idx, field in enumerate(
            ("subsystem", "source rule", "workflow", "edge case", "test", "validation owner",
             "mutation owner", "trigger/phase", "ordering", "transaction/accounting",
             "failure/recovery", "audit", "privacy"), start=1
        ):
            ctx.need(cid, bool(c[idx]), f"{tag}: empty {field}", errs)
        for w in expand(c[3], "WFW"):
            ctx.need(cid, 1 <= w <= WFW_TOTAL, f"{tag}: unknown WFW-{w:03d}", errs)
        for e in re.findall(r"WFE-\d{3}", c[4]):
            ctx.need(cid, e in wfe, f"{tag}: unknown {e}", errs)
        for t in re.findall(r"WFA-\d{3}", c[5]):
            ctx.need(cid, t in ident, f"{tag}: unknown {t}", errs)
    return errs


# --------------------------------------------------------------------------
# checks 31-35 — rule inventories, orphan totals, D-014, invariants
# --------------------------------------------------------------------------


def check_31(doc, ctx, cid):
    sec = slice_between(doc, "### 14.3 Every numbered WAR rule", "**14.3.1")
    covered: list[int] = []
    for c in table_rows(sec):
        if c and re.match(r"`WAR-\d{3}`", c[0]):
            covered.extend(expand(c[0], "WAR"))
    errs = []
    ctx.need(cid, ranges_cover(covered, 188),
             f"WAR ranges are incomplete or overlapping (rows={len(covered)})", errs)
    ctx.need(cid, set(covered) == b10_numbered(ctx.docs["b10"]),
             "WAR range coverage differs from the B-10 numbered inventory", errs)
    return errs


def check_32(doc, ctx, cid):
    sec = slice_between(doc, "**14.3.1 The 42 lettered sub-rules.**", "**14.3.2")
    listed = set(re.findall(r"^\| `(WAR-\d{3}[a-z])` \|", sec, re.M))
    expected = b10_lettered(ctx.docs["b10"])
    errs = []
    ctx.need(cid, len(listed) == 42, f"lettered table has {len(listed)} rows, expected 42", errs)
    ctx.need(cid, listed == expected,
             f"lettered set differs from B-10 (doc-only={sorted(listed - expected)}, "
             f"b10-only={sorted(expected - listed)})", errs)
    return errs


def check_33(doc, ctx, cid):
    errs = []
    ident, beh = ctx.parsed["wfa_ident"], ctx.parsed["wfa_beh"]
    wfe = ctx.parsed["wfe"]
    sec14_2 = slice_between(doc, "### 14.2 Requirements REQ-654–REQ-703", "### 14.3")
    reqs = [c for c in table_rows(sec14_2) if c and re.fullmatch(r"REQ-\d{3}", c[0])]
    ctx.need(cid, len(reqs) == 50, f"orphan total 2: {len(reqs)} requirements", errs)

    sec14_3 = slice_between(doc, "### 14.3 Every numbered WAR rule", "**14.3.1")
    numbered: list[int] = []
    for c in table_rows(sec14_3):
        if c and re.match(r"`WAR-\d{3}`", c[0]):
            numbered.extend(expand(c[0], "WAR"))
    ctx.need(cid, ranges_cover(numbered, 188) and len(b10_lettered(ctx.docs["b10"])) == 42,
             "orphan total 1: rule inventory is incomplete", errs)

    sec14_4 = slice_between(doc, "### 14.4 All 39 formulas", "### 14.5")
    frows = [c for c in table_rows(sec14_4) if c and re.fullmatch(r"`F-WR-\d{3}`", c[0])]
    ctx.need(cid, len(frows) == 39, f"orphan total 3: {len(frows)} formulas", errs)

    ctx.need(cid, len({int(m) for m in re.findall(r'^\| `B10-AD-(\d{2})` \|', doc, re.M)}) == 25,
             "orphan total 4: architecture decisions are not 25", errs)
    ctx.need(cid, len({int(m) for m in re.findall(r'^\| `B10-C(\d{2})` \|', doc, re.M)}) == 34,
             "orphan total 4: conflict entries are not 34", errs)
    open_uds = [u for u in range(40, 50)
                if unresolved_status(ctx.docs["unresolved"], f"UD-{u:03d}") == "Open"]
    ctx.need(cid, open_uds == list(range(40, 50)),
             f"orphan total 4: UD-040–UD-049 are not all Open ({open_uds})", errs)

    sec10_2 = slice_between(doc, "**10.2 Identifier span and defined codes.**", "**10.3")
    wrf = {int(m) for m in re.findall(r"^\| `WRF-(\d{2})` \|", sec10_2, re.M)}
    ctx.need(cid, wrf == DEFINED_WRF, f"orphan total 5: WRF set is {sorted(wrf)}", errs)

    sec14_5 = slice_between(doc, "### 14.5 The fourteen audit events", "### 14.6")
    wra = {int(m) for m in re.findall(r"^\| `WRA-(\d{2})`", sec14_5, re.M)}
    ctx.need(cid, wra == set(range(1, 15)), f"orphan total 6: WRA set is {sorted(wra)}", errs)

    sec14_9 = slice_between(doc, "### 14.9 Subsystem and prompt integration rows", "### 14.10")
    irows = [c for c in table_rows(sec14_9) if c and c[0].isdigit()]
    ctx.need(cid, len(irows) == 13, f"orphan total 7: {len(irows)} integration rows", errs)

    for n in range(1, WFW_TOTAL + 1):
        wfw = f"WFW-{n:03d}"
        tests = [wid for wid, v in ident.items()
                 if wfw in [f"WFW-{x:03d}" for x in expand(v["wfw"], "WFW")] and wid != "WFA-120"]
        ctx.need(cid, bool(tests), f"orphan total 8: {wfw} has no dedicated test", errs)

    for eid, v in wfe.items():
        ctx.need(cid, v["test"] in ident and eid in re.findall(r"WFE-\d{3}", ident[v["test"]]["wfe"]),
                 f"orphan total 9: {eid} is not cited back by {v['test']}", errs)

    for wid, v in ident.items():
        ctx.need(cid, bool(expand(v["req"], "REQ")), f"orphan total 10: {wid} names no requirement", errs)
        ctx.need(cid, bool(expand(v["wfw"], "WFW")), f"orphan total 10: {wid} names no workflow", errs)
        ctx.need(cid, bool(v["rules"]), f"orphan total 10: {wid} names no rule", errs)
    ctx.need(cid, set(ident) == set(beh), "orphan total 10: test tables do not join", errs)
    return errs


def check_34(doc, ctx, cid):
    errs = []
    autonomy = ctx.docs["autonomy"]
    for needle in ("D-014", "Category A", "Category B", "Category C", "Category D"):
        ctx.need(cid, needle in autonomy, f"D-014 policy missing {needle!r}", errs)
    for u in range(40, 50):
        status = unresolved_status(ctx.docs["unresolved"], f"UD-{u:03d}")
        ctx.need(cid, status == "Open", f"UD-{u:03d} status is {status!r}, expected Open", errs)
    ud32 = re.search(r"^\| `?UD-032`? \|.*$", ctx.docs["unresolved"], re.M)
    ctx.need(cid, bool(ud32) and "Resolved" in ud32.group(0),
             "UD-032 is not Resolved", errs)
    ctx.need(cid, "`UD-040`–`UD-049` remain **Open**" in doc,
             "the document does not restate that UD-040–UD-049 remain Open", errs)
    ctx.need(cid, "**Category C — provisional decisions.** **None created by 10C.**" in doc,
             "Category C 'none created' statement missing", errs)
    ctx.need(cid, "**Category D — external, costly or irreversible actions.** **None taken.**" in doc,
             "Category D 'none taken' statement missing", errs)
    ctx.need(cid, not re.search(r"UD-04\d[^\n|]*\|[^\n]*(Resolved|Approved)", doc),
             "the document presents a UD-040–UD-049 entry as resolved or approved", errs)
    ctx.need(cid, "DD-191" in ctx.docs["decisions"], "DD-191 is absent from the decision register", errs)
    ctx.need(cid, "D-143" in ctx.docs["decisions"], "D-143 is absent from the decision register", errs)
    ctx.need(cid, "D-143" in ctx.docs["decisions_md"], "D-143 is absent from DECISIONS.md", errs)
    ctx.need(cid, "D-143" in doc and "DD-191" in doc,
             "the document does not cite D-143 and DD-191", errs)
    return errs


def check_35(doc, ctx, cid):
    errs = []
    for needle in (
        "civilian Food",
        "soldier-equivalent",
        "`WRF-35` never applies to `OP-09`",
        "protected civilian",
        "no Alliance, office, ballot, treaty, AI or administrator",
        "National `DP-T01`",
        "The only B-05 attribute a strike may reduce is city infrastructure",
        "kills, evicts or transfers a person",
        "G-1",
        "G-6",
        "never infers consent from silence",
    ):
        ctx.need(cid, needle in doc, f"substantive invariant missing {needle!r}", errs)
    return errs


# --------------------------------------------------------------------------
# checks 36-43 — status, doc consistency, traceability statements, registry
# --------------------------------------------------------------------------


def check_36(doc, ctx, cid):
    errs = []
    ctx.need(cid, "No test below has been executed as a runtime test" in doc,
             "design-only status sentence missing", errs)
    ctx.need(cid, "every record is `Definition: COMPLETE` and `Execution: NOT RUN`" in doc,
             "Definition/Execution status statement missing", errs)
    for v in ctx.parsed["wfa_ident"].values():
        ctx.need(cid, v["execution"] == "NOT RUN", f"{v['name']}: execution is not NOT RUN", errs)
    for i, line in enumerate(doc.splitlines(), 1):
        low = line.lower()
        if "runtime-passed" in low and "no row is" not in low:
            ctx.need(cid, False, f"line {i}: positive runtime claim", errs)
        if "has been implemented" in low or "is deployed" in low:
            ctx.need(cid, False, f"line {i}: implementation claim", errs)
    return errs


def check_37(doc, ctx, cid):
    sec29 = slice_between(doc, "### 2.9 Forbidden vocabulary", "## 3. Actors")
    scanned = doc.replace(sec29, "") if sec29 else doc
    low = scanned.lower()
    errs = []
    for phrase in FORBIDDEN_PHRASES:
        ctx.need(cid, phrase not in low, f"forbidden construct present: {phrase!r}", errs)
    return errs


def check_38(doc, ctx, cid):
    errs = []
    ctx.need(cid, doc.lower().count("provisional") >= 10, "expected at least 10 provisional labels", errs)
    ctx.need(cid, "**PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**" in doc,
             "the fixed provisional label is missing", errs)
    for phrase in ("is calibrated", "values are final", "approved value", "final value"):
        ctx.need(cid, phrase not in doc.lower(), f"provisional promotion language present: {phrase!r}", errs)
    return errs


def check_39(doc, ctx, cid):
    b10, reg = ctx.docs["b10"], ctx.docs["register"]
    errs = []
    checks = (
        ("numbered WAR", len(b10_numbered(b10)), 188),
        ("lettered WAR", len(b10_lettered(b10)), 42),
        ("B10-AD", len({int(m) for m in re.findall(r"B10-AD-(\d{2})", b10)}), 25),
        ("B10-C", len({int(m) for m in re.findall(r"B10-C(\d{2})", b10)}), 34),
        ("WRA", len({m for m in re.findall(r"WRA-(\d{2})", b10)}), 14),
        ("defined WRF", len({m for m in re.findall(r"^\| `WRF-(\d{2})` \|", b10, re.M)}), 32),
        ("F-WR", len(register_formulas(reg)), 39),
    )
    for label, value, expected in checks:
        ctx.need(cid, value == expected, f"B-10/register {label} count is {value}, expected {expected}", errs)
    for phrase in (
        "230 `WAR-` identifiers (188 numbered plus 42 lettered sub-rules)",
        "39 formulas", "25 architecture decisions", "34 conflict entries",
        "14 audit events", "32 defined failure codes",
    ):
        ctx.need(cid, phrase in doc, f"the document does not state {phrase!r}", errs)
    ctx.need(cid, "v1.3" in b10[:4000], "B-10 is not v1.3", errs)
    ctx.need(cid, "v1.3" in reg[:2000], "the formula register is not v1.3", errs)
    return errs


def check_40(doc, ctx, cid):
    errs = []
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", doc):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (DOC_PATH.parent / target).resolve()
        ctx.need(cid, resolved.exists(), f"broken link target {target!r}", errs)
    return errs


def check_41(doc, ctx, cid):
    errs = []
    sec = slice_between(doc, "### 14.11 Orphan audit", "### 14.12")
    rows = [c for c in table_rows(sec) if c and c[0].isdigit()]
    ctx.need(cid, len(rows) == 10, f"orphan audit must have 10 numbered totals, found {len(rows)}", errs)
    for c in rows:
        if len(c) >= 5:
            ctx.need(cid, "**0**" in c[4], f"orphan total {c[0]} does not state zero unexplained orphans", errs)
        else:
            ctx.need(cid, False, f"orphan total {c[0]} row is incomplete", errs)
    nf_sec = slice_between(doc, "### 14.12", "## 15.")
    nf = set(re.findall(r"`(NF-\d{2})`", nf_sec))
    executable_nf = {f["id"] for f in NEGATIVE_FIXTURES}
    ctx.need(cid, len(nf) >= 15, f"§14.12 names only {len(nf)} representative fixtures", errs)
    ctx.need(cid, nf <= executable_nf,
             f"§14.12 names fixtures absent from the executable registry: {sorted(nf - executable_nf)}", errs)
    return errs


def check_42(doc, ctx, cid):
    errs = []
    reg = ctx.registry_override if ctx.registry_override is not None else ctx.registry
    ids = [c[0] for c in reg]
    ctx.need(cid, len(ids) == len(set(ids)), f"duplicate check IDs: {sorted({i for i in ids if ids.count(i) > 1})}", errs)
    ctx.need(cid, ids == [f"{i:02d}" for i in range(1, len(ids) + 1)],
             f"check IDs are not sequential 01..{len(ids)}", errs)
    for c in reg:
        ctx.need(cid, len(c) == 4, f"check {c[0]}: invalid definition (expected 4 parts)", errs)
        if len(c) == 4:
            ctx.need(cid, callable(c[2]), f"check {c[0]}: no callable function", errs)
            ctx.need(cid, callable(c[3]), f"check {c[0]}: no mutator", errs)
            ctx.need(cid, bool(c[1]), f"check {c[0]}: empty name", errs)
    return errs


def check_43(doc, ctx, cid):
    errs = []
    for phrase in (
        "124 acceptance tests in 16 classes",
        "60 edge cases",
        "40 workflows",
        "17 player journeys",
        "39 formulas",
        "14 audit events",
        "32 defined failure codes",
        "25 architecture decisions",
        "34 conflict entries",
        "13 subsystem/prompt integration rows",
        "50 warfare requirements",
    ):
        ctx.need(cid, phrase in doc, f"count statement missing {phrase!r}", errs)
    return errs


def check_44(doc, ctx, cid):
    """Every numbered and lettered WAR rule has a complete disposition."""
    errs = []
    defs, dups = b10_definitions(ctx.docs["b10"])
    numbered = b10_numbered(ctx.docs["b10"])
    lettered = b10_lettered(ctx.docs["b10"])
    ctx.need(cid, not dups, f"B-10 has duplicate definitions: {sorted(set(dups))}", errs)
    ctx.need(cid, len(numbered) == 188, f"B-10 numbered definitions are {len(numbered)}, expected 188", errs)
    ctx.need(cid, len(lettered) == 42, f"B-10 lettered definitions are {len(lettered)}, expected 42", errs)

    ident0 = ctx.parsed["wfa_ident"]
    lettered_sec = slice_between(doc, "**14.3.1 The 42 lettered sub-rules.**", "**14.3.2")
    listed_lettered = set()
    for c in table_rows(lettered_sec):
        if c and re.fullmatch(r"`WAR-\d{3}[a-z]`", c[0]):
            lid = c[0].strip("`")
            listed_lettered.add(lid)
            for t in re.findall(r"WFA-\d{3}", c[3]) if len(c) > 3 else []:
                ctx.need(cid, t in ident0, f"{lid}: nonexistent test {t}", errs)
    ctx.need(cid, listed_lettered == lettered,
             f"lettered table differs from B-10 "
             f"(doc-only={sorted(listed_lettered - lettered)}, b10-only={sorted(lettered - listed_lettered)})", errs)

    rows = parse_war_ranges(doc)
    covered = [n for row in rows for n in row["ids"]]
    ctx.need(cid, len(covered) == len(set(covered)),
             f"WAR ranges overlap: {sorted(n for n in set(covered) if covered.count(n) > 1)}", errs)
    ctx.need(cid, set(covered) == numbered,
             f"WAR ranges do not equal B-10 numbered definitions "
             f"(doc-only={sorted(set(covered) - numbered)}, b10-only={sorted(numbered - set(covered))})", errs)
    for row in rows:
        ctx.need(cid, bool(row["wfws"]) and all(1 <= w <= WFW_TOTAL for w in row["wfws"]),
                 f"range {row['ids'][0]:03d}–{row['ids'][-1]:03d}: invalid or empty workflow mapping", errs)
        ctx.need(cid, bool(row["tests"]) and all(1 <= t <= WFA_TOTAL for t in row["tests"]),
                 f"range {row['ids'][0]:03d}–{row['ids'][-1]:03d}: invalid or empty test mapping", errs)

    disp = war_dispositions(ctx, doc)
    counts_n = {"DIRECT": 0, "SUPPORTING": 0, "DEFERRED": 0, "NOT COVERED": 0}
    counts_l = {"DIRECT": 0, "SUPPORTING": 0, "DEFERRED": 0, "NOT COVERED": 0}
    for n in sorted(numbered):
        rid = f"WAR-{n:03d}"
        v = disp[rid]
        counts_n[v["kind"]] += 1
        _check_disposition(cid, ctx, doc, rid, v, errs, numbered=True)
    for rid in sorted(lettered):
        ctx.need(cid, rid in disp, f"{rid}: lettered sub-rule has no disposition", errs)
        if rid not in disp:
            continue
        v = disp[rid]
        counts_l[v["kind"]] += 1
        _check_disposition(cid, ctx, doc, rid, v, errs, numbered=False)
        ctx.need(cid, v["kind"] in ("DIRECT", "SUPPORTING"),
                 f"{rid}: lettered sub-rule is {v['kind']}", errs)

    sec = slice_between(doc, "**14.3.6 Per-rule disposition.**", "### 14.4")
    stated = {}
    for c in table_rows(sec):
        if c and c[0].startswith("Numbered"):
            stated["numbered"] = [int(x) for x in re.findall(r"\d+", " ".join(c[1:6]))]
        elif c and c[0].startswith("Lettered"):
            stated["lettered"] = [int(x) for x in re.findall(r"\d+", " ".join(c[1:6]))]
    expected_n = [len(numbered), counts_n["DIRECT"], counts_n["SUPPORTING"],
                  counts_n["DEFERRED"], counts_n["NOT COVERED"]]
    expected_l = [len(lettered), counts_l["DIRECT"], counts_l["SUPPORTING"],
                  counts_l["DEFERRED"], counts_l["NOT COVERED"]]
    ctx.need(cid, stated.get("numbered") == expected_n,
             f"§14.3.6 numbered totals {stated.get('numbered')} != derived {expected_n}", errs)
    ctx.need(cid, stated.get("lettered") == expected_l,
             f"§14.3.6 lettered totals {stated.get('lettered')} != derived {expected_l}", errs)
    return errs


def _check_disposition(cid, ctx, doc, rid, v, errs, numbered: bool):
    ident = ctx.parsed["wfa_ident"]
    ctx.need(cid, bool(v["workflows"]), f"{rid}: no workflow mapping", errs)
    ctx.need(cid, bool(v["tests"]), f"{rid}: no acceptance-test mapping", errs)
    for w in v["workflows"]:
        ctx.need(cid, re.fullmatch(r"WFW-\d{3}", w) and 1 <= int(w[4:]) <= WFW_TOTAL,
                 f"{rid}: invalid workflow {w}", errs)
    for t in v["tests"]:
        ctx.need(cid, t in ident, f"{rid}: nonexistent test {t}", errs)
    ctx.need(cid, bool(v["source"]), f"{rid}: no evidence source", errs)
    if v["kind"] == "DIRECT":
        t = v["tests"][0] if v["tests"] else ""
        if t in ident:
            rec = ident[t]
            ctx.need(cid, rec["definition"] == "COMPLETE", f"{rid}: test {t} is not COMPLETE", errs)
            beh = ctx.parsed["wfa_beh"].get(t, {})
            ctx.need(cid, bool(beh.get("output")) and bool(beh.get("mutation")),
                     f"{rid}: test {t} has no real expected result", errs)
            ctx.need(cid, bool(expand(rec["wfw"], "WFW")), f"{rid}: test {t} names no workflow", errs)
            ctx.need(cid, bool(beh.get("evidence")), f"{rid}: test {t} has no evidence", errs)
            cites = (rid in re.findall(r"WAR-\d{3}[a-z]", rec["rules"]) if not numbered
                     else int(rid[4:]) in expand(rec["rules"], "WAR"))
            ctx.need(cid, cites, f"{rid}: DIRECT test {t} does not cite the exact rule", errs)
            if rec["formula"].startswith("`F-WR-"):
                fid = int(re.search(r"F-WR-(\d{3})", rec["formula"]).group(1))
                ctx.need(cid, fid in register_formulas(ctx.docs["register"]),
                         f"{rid}: test {t} names unknown F-WR-{fid:03d}", errs)
    if v["kind"] == "NOT COVERED":
        ctx.need(cid, False, f"{rid}: NOT COVERED without an explicit scope justification", errs)
    if v["kind"] == "DEFERRED":
        ctx.need(cid, False, f"{rid}: DEFERRED without owner and future task", errs)


_JOINED_CACHE: dict[tuple[str, ...], str] = {}
_STAR_CACHE: dict[str, dict[str, bool]] = {}


def _joined_subsystems(docs: dict[str, str]) -> str:
    """All subsystem and decision sources joined once per distinct content set.

    `_resolve_ident` is called for every identifier in a mandatory field, so
    rebuilding this several-hundred-kilobyte string each time dominated the
    runtime of checks 45 and 47. String hashes are cached by CPython and the
    tuple equality check short-circuits on identity, so this lookup is cheap.
    """
    keys = ("b02", "b03", "b04", "b05", "b06", "b07", "b08", "b09",
            "decisions", "decisions_md")
    parts = tuple(docs.get(k, "") for k in keys)
    text = _JOINED_CACHE.get(parts)
    if text is None:
        text = "\n".join(parts)
        if len(_JOINED_CACHE) >= 8:
            _JOINED_CACHE.clear()
        _JOINED_CACHE[parts] = text
    return text


def _resolve_ident(tok, docs, subsystem_key):
    """True when an identifier exists in the named authoritative source."""
    if tok.startswith("WAR-"):
        if re.fullmatch(r"WAR-\d{3}", tok):
            return int(tok[4:]) in b10_numbered(docs["b10"])
        return tok in b10_lettered(docs["b10"])
    if tok.startswith("F-WR-"):
        return int(tok[5:]) in register_formulas(docs["register"])
    if tok.startswith("WRA-"):
        return 1 <= int(tok[4:]) <= 14
    if tok.startswith("WFW-"):
        return 1 <= int(tok[4:]) <= WFW_TOTAL
    if tok.startswith("WFE-"):
        return 1 <= int(tok[4:]) <= WFE_TOTAL
    if tok.startswith("WFA-"):
        return 1 <= int(tok[4:]) <= WFA_TOTAL
    if tok.startswith("REQ-"):
        return int(tok[4:]) in authoritative_requirements(docs["reqs"])
    if subsystem_key == "*":
        text = _joined_subsystems(docs)
        cache = _STAR_CACHE.get(text)
        if cache is None:
            if len(_STAR_CACHE) >= 8:
                _STAR_CACHE.clear()
            cache = _STAR_CACHE[text] = {}
        if tok not in cache:
            cache[tok] = bool(re.search(
                r"(?<![A-Za-z0-9-])" + re.escape(tok) + r"(?![0-9a-z])", text))
        return cache[tok]
    text = docs.get(subsystem_key, "")
    return bool(re.search(r"(?<![A-Za-z0-9-])" + re.escape(tok) + r"(?![0-9a-z])", text))


def check_45(doc, ctx, cid):
    """Thirteen integration contracts resolve to real subsystem rules."""
    sec = slice_between(doc, "### 14.9 Subsystem and prompt integration rows", "### 14.10")
    rows = [c for c in table_rows(sec) if c and c[0].isdigit()]
    errs = []
    ctx.need(cid, [c[0] for c in rows] == [str(i) for i in range(1, 14)],
             f"integration rows are not 1..13: {[c[0] for c in rows]}", errs)
    docs = ctx.docs
    subsystem_key = {1: "b02", 2: "b03", 3: "b04", 4: "b05", 5: "b06",
                     6: "b07", 7: "b08", 8: "b09", 9: "b10", 10: "b10",
                     11: "b10", 12: "b10", 13: "doc"}
    for c in rows:
        n = int(c[0])
        if len(c) != 14:
            ctx.need(cid, False, f"integration row {n}: expected 14 columns, found {len(c)}", errs)
            continue
        for idx, field in ((1, "subsystem"), (2, "source rule"), (3, "workflow"),
                           (4, "edge case"), (5, "test"), (6, "validation owner"),
                           (7, "mutation owner"), (8, "trigger/phase"), (9, "ordering"),
                           (10, "transaction/accounting"), (11, "failure/recovery"),
                           (12, "audit"), (13, "privacy")):
            ok, why = justified_value(c[idx], "audit" if idx == 12 else None, ctx)
            ctx.need(cid, ok, f"integration row {n}: {field} invalid ({why})", errs)
        # source document and exact rule identifiers
        keys = subsystem_key[n]
        if n == 1:
            keys = "b02"
        source = c[2]
        toks = IDENT_RE.findall(source)
        has_anchor = bool(re.search(r"§\d", source))
        ctx.need(cid, len(toks) >= 1 or (n >= 9 and has_anchor),
                 f"integration row {n}: source rule names no exact identifier or section anchor", errs)
        for tok in toks:
            ctx.need(cid, _resolve_ident(tok, docs, keys),
                     f"integration row {n}: source identifier {tok} does not exist in {keys}", errs)
        if n in (1, 2, 3, 4, 5, 6, 7, 8):
            src_doc = SUBSYSTEM_DOCS[n] if n in SUBSYSTEM_DOCS else B02_PATH
            ctx.need(cid, src_doc.exists(), f"integration row {n}: source document is missing", errs)
            if src_doc.exists():
                text = read(src_doc)
                for tok in toks:
                    ctx.need(cid, bool(re.search(r"(?<![A-Za-z0-9-])" + re.escape(tok) + r"(?![0-9a-z])", text)),
                             f"integration row {n}: {tok} absent from {src_doc.name}", errs)
        if n == 11:
            ctx.need(cid, "**12.3 Confirmation requirements.**" in doc,
                     "integration row 11: this document §12.3 is missing", errs)
        if n == 13:
            ctx.need(cid, "## 14. Bidirectional traceability" in doc,
                     "integration row 13: this document §14 is missing", errs)
        # workflows, edge cases, tests
        wfws = expand(c[3], "WFW")
        ctx.need(cid, bool(wfws), f"integration row {n}: no workflow", errs)
        for w in wfws:
            ctx.need(cid, 1 <= w <= WFW_TOTAL, f"integration row {n}: unknown WFW-{w:03d}", errs)
        edgerefs = re.findall(r"WFE-\d{3}", c[4])
        ctx.need(cid, bool(edgerefs) or c[4].startswith("—") or c[4].startswith("N/A"),
                 f"integration row {n}: edge case is neither an identifier nor a justified none", errs)
        for e in edgerefs:
            ctx.need(cid, int(e[4:]) <= WFE_TOTAL, f"integration row {n}: unknown {e}", errs)
        tests = re.findall(r"WFA-\d{3}", c[5])
        ctx.need(cid, bool(tests), f"integration row {n}: no test", errs)
        for t in tests:
            ctx.need(cid, 1 <= int(t[4:]) <= WFA_TOTAL, f"integration row {n}: unknown {t}", errs)
        # ownership and transaction semantics
        if n <= 8:
            ctx.need(cid, not re.match(r"(?i)^(none|n/a)\b", c[7]),
                     f"integration row {n}: mutation owner is none for a mutating subsystem", errs)
            ctx.need(cid, not re.match(r"(?i)^(none|n/a|no transaction)\b", c[10]),
                     f"integration row {n}: transaction/accounting is not defined", errs)
            ctx.need(cid, not re.match(r"(?i)^(none|n/a)\b", c[9]),
                     f"integration row {n}: ordering is not defined", errs)
        phases = set(re.findall(r"\b(OPEN|P2|P3\.7|P4\.1|P5|P7)\b", c[8]))
        ctx.need(cid, bool(phases) or any(k in c[8] for k in
                 ("Continuous", "Every", "Handoff", "Calibration", "P5/P6", "OPEN")),
                 f"integration row {n}: trigger names no phase", errs)
        for a in re.findall(r"WRA-(\d{2})", c[12]):
            ctx.need(cid, 1 <= int(a) <= 14, f"integration row {n}: unknown WRA-{a}", errs)
    return errs


def check_46(doc, ctx, cid):
    """Every mandatory N/A or none carries a meaningful, non-placeholder reason."""
    errs = []
    ident = ctx.parsed["wfa_ident"]
    beh = ctx.parsed["wfa_beh"]
    checked = 0
    for wid, v in sorted(ident.items()):
        for f in ("wfe", "formula"):
            checked += 1
            ok, why = justified_value(v[f], f, ctx)
            ctx.need(cid, ok, f"{wid}: {f} cell invalid ({why})", errs)
    for wid, v in sorted(beh.items()):
        for f in ("ledger", "audit", "failure", "privacy"):
            checked += 1
            ok, why = justified_value(v[f], f, ctx)
            ctx.need(cid, ok, f"{wid}: {f} cell invalid ({why})", errs)
    sec = slice_between(doc, "### 14.9 Subsystem and prompt integration rows", "### 14.10")
    for c in table_rows(sec):
        if c and c[0].isdigit() and len(c) == 14:
            for idx in range(6, 14):
                ok, why = justified_value(c[idx], "audit" if idx == 12 else None, ctx)
                ctx.need(cid, ok, f"integration row {c[0]}: column {idx} invalid ({why})", errs)
    ctx.need(cid, checked == WFA_TOTAL * 6,
             f"checked {checked} mandatory cells, expected {WFA_TOTAL * 6}", errs)
    return errs


def parse_catalogue(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if c and re.fullmatch(r"(PF|NF|NA)-\d{2}", c[0].strip("`")):
            rows.append({
                "id": c[0].strip("`"), "name": c[1], "mutation": c[2],
                "check": c[3].strip("`"), "reason": c[4],
                "executable": c[5].strip("`"), "result": c[6],
            })
    return rows


REQUIRED_BINDING_FIELDS = (
    "id", "kind", "name", "op", "source", "target", "expected_value",
    "expected_check", "expected_reason", "executor", "executor_sha1",
    "mutation", "result", "doc_ref",
)


def _fixture_source_text(ctx, source: str):
    if source == "doc":
        return None
    if source.startswith("current:"):
        return ctx.docs["current"].get(source.split(":", 1)[1], "")
    return ctx.docs.get(source, "")


def _source_hash(fn) -> str:
    return hashlib.sha1(inspect.getsource(fn).encode("utf-8")).hexdigest()


def _find_rows(lines, target: str, ncols):
    return [(i, line) for i, line in enumerate(lines)
            if line.startswith(target) and (ncols is None or len(cells(line)) == ncols)]


def _changed_blocks(before: str, after: str) -> list[tuple[str, list[str], list[str]]]:
    a, b = before.splitlines(), after.splitlines()
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            out.append((tag, a[i1:i2], b[j1:j2]))
    return out


def _verify_binding(entry: dict, doc: str, ctx) -> tuple[list[str], str, object]:
    """Run the declared executor and prove it makes exactly the declared change.

    Returns the findings, the mutated document and the mutated context so the
    caller can run the expected check without executing the fixture a second time.
    """
    errs: list[str] = []
    fid = entry["id"]
    source = entry["source"]
    before_text = doc if source == "doc" else _fixture_source_text(ctx, source)
    if before_text is None:
        return [f"{fid}: unknown mutation source {source!r}"], doc, ctx
    fn = globals().get(entry["executor"])
    if not callable(fn):
        return [f"{fid}: executor {entry['executor']!r} is not callable"], doc, ctx
    snapshot_doc = doc
    snapshot_docs = dict(ctx.docs)
    snapshot_registry = list(ctx.registry)
    snapshot_override = ctx.registry_override
    after, mut_ctx = fn(doc, ctx)
    if (doc != snapshot_doc or ctx.docs != snapshot_docs
            or ctx.registry != snapshot_registry
            or ctx.registry_override != snapshot_override):
        errs.append(f"{fid}: executor mutated shared validator state")
    after_ctx = mut_ctx if isinstance(mut_ctx, Ctx) else ctx
    after_text = after if source == "doc" else _fixture_source_text(after_ctx, source)
    if after_text is None:
        return errs + [f"{fid}: mutation source {source!r} disappeared"], after, after_ctx
    op = entry["op"]
    target = entry["target"]
    expected = entry["expected_value"]
    old = entry["old_value"]
    if op == "edit_row":
        before_rows = _find_rows(before_text.splitlines(), target, entry["ncols"])
        after_rows = _find_rows(after_text.splitlines(), target, entry["ncols"])
        if len(before_rows) != 1 or len(after_rows) != 1:
            errs.append(f"{fid}: target row {target!r} is not unique before and after")
        else:
            before_cells = cells(before_rows[0][1])
            after_cells = cells(after_rows[0][1])
            if before_cells[entry["field"]] != old:
                errs.append(f"{fid}: declared old value does not match the live row")
            if after_cells[entry["field"]] != expected:
                errs.append(f"{fid}: executor produced {after_cells[entry['field']]!r}, "
                            f"declared {expected!r}")
        blocks = _changed_blocks(before_text, after_text)
        replace_blocks = [b for b in blocks if b[0] == "replace"]
        if len(blocks) != 1 or len(replace_blocks) != 1:
            errs.append(f"{fid}: expected exactly one edited line, found {len(blocks)} change blocks")
        elif len(replace_blocks[0][1]) != 1 or len(replace_blocks[0][2]) != 1:
            errs.append(f"{fid}: edited row did not change exactly one line")
    elif op == "delete_row":
        before_rows = _find_rows(before_text.splitlines(), target, entry["ncols"])
        after_rows = _find_rows(after_text.splitlines(), target, entry["ncols"])
        if len(before_rows) != 1:
            errs.append(f"{fid}: target row {target!r} is not unique before deletion")
        if after_rows:
            errs.append(f"{fid}: target row {target!r} survives the deletion")
        blocks = _changed_blocks(before_text, after_text)
        if len(blocks) != 1 or blocks[0][0] != "delete" or len(blocks[0][1]) != 1:
            errs.append(f"{fid}: expected exactly one deleted line, found {len(blocks)} blocks")
    elif op == "insert_row":
        before_rows = _find_rows(before_text.splitlines(), target, entry["ncols"])
        after_rows = _find_rows(after_text.splitlines(), target, entry["ncols"])
        if before_rows:
            errs.append(f"{fid}: inserted row {target!r} already exists")
        if len(after_rows) != 1:
            errs.append(f"{fid}: inserted row {target!r} is not uniquely present")
        elif after_rows[0][1].strip() != expected:
            errs.append(f"{fid}: inserted line differs from the declared line")
        blocks = _changed_blocks(before_text, after_text)
        if len(blocks) != 1 or blocks[0][0] != "insert" or len(blocks[0][2]) != 1:
            errs.append(f"{fid}: expected exactly one inserted line, found {len(blocks)} blocks")
    elif op == "replace":
        blocks = _changed_blocks(before_text, after_text)
        if not blocks:
            errs.append(f"{fid}: executor changed nothing")
        for tag, old_lines, new_lines in blocks:
            if tag not in ("replace",):
                errs.append(f"{fid}: unexpected {tag} change block")
                continue
            for line in old_lines:
                if old not in line:
                    errs.append(f"{fid}: changed line does not contain the declared old value")
            for line in new_lines:
                if expected not in line:
                    errs.append(f"{fid}: changed line does not contain the declared new value")
        scope = entry.get("scope") or ""
        if scope:
            changed_old = [l for b in blocks for l in b[1]]
            changed_new = [l for b in blocks for l in b[2]]
            if not all(scope in l for l in changed_old + changed_new):
                errs.append(f"{fid}: changed lines fall outside the declared scope {scope!r}")
    elif op == "append":
        if not after_text.startswith(before_text):
            errs.append(f"{fid}: append rewrote existing content")
        elif after_text[len(before_text):].strip() != expected.strip():
            errs.append(f"{fid}: appended text differs from the declared value")
    else:
        errs.append(f"{fid}: unknown binding operation {op!r}")
    return errs, after, after_ctx


def _registry_errors(data: dict, doc: str, ctx, only=None) -> list[str]:
    errs: list[str] = []
    fixtures = data.get("fixtures", []) if isinstance(data, dict) else []
    if not isinstance(fixtures, list) or not fixtures:
        return ["registry has no fixtures"]
    only_set = set(only) if only else None
    ids = [f.get("id") for f in fixtures]
    if len(ids) != len(set(ids)):
        errs.append("registry contains duplicate fixture IDs")
    pos = {f[0]: f for f in POSITIVE_FIXTURES}
    neg = {f["id"]: f for f in NEGATIVE_FIXTURES}
    na = {f[0]: f for f in NA_FIXTURES}
    expected_ids = set(pos) | set(neg) | set(na)
    if set(ids) != expected_ids:
        errs.append(f"registry IDs differ from executable fixtures "
                    f"(registry-only={sorted(set(ids) - expected_ids)}, "
                    f"executable-only={sorted(expected_ids - set(ids))})")
    check_ids = {c[0] for c in CHECKS}
    catalogue = {r["id"]: r for r in parse_catalogue(ctx.docs.get("catalogue", ""))}
    for entry in fixtures:
        fid = entry.get("id")
        if only_set is not None and fid not in only_set:
            continue
        missing = [k for k in REQUIRED_BINDING_FIELDS if k not in entry]
        if missing:
            errs.append(f"{fid}: registry entry missing {missing}")
            continue
        if entry["kind"] == "negative" and fid in neg:
            fixture = neg[fid]
            if entry["name"] != fixture["name"]:
                errs.append(f"{fid}: registry description differs from the executable fixture")
            if entry["executor"] != fixture["mutator"]:
                errs.append(f"{fid}: declared executor {entry['executor']!r} differs "
                            f"from the registered executor {fixture['mutator']!r}")
            if entry["expected_check"] != fixture["check"]:
                errs.append(f"{fid}: declared check {entry['expected_check']!r} differs "
                            f"from the executable check {fixture['check']!r}")
            if entry["expected_reason"] != fixture["reason"]:
                errs.append(f"{fid}: declared reason differs from the executable reason")
            if entry["result"] != "Rejected":
                errs.append(f"{fid}: negative fixture is not marked Rejected")
        elif entry["kind"] == "positive" and fid in pos:
            fixture = pos[fid]
            if entry["name"] != fixture[1] or entry["expected_check"] != fixture[2]:
                errs.append(f"{fid}: positive fixture declaration differs from the executable fixture")
            if entry["executor"] != f"check_{fixture[2]}":
                errs.append(f"{fid}: positive executor is not check_{fixture[2]}")
            if entry["result"] != "Accepted":
                errs.append(f"{fid}: positive fixture is not marked Accepted")
        elif entry["kind"] == "na" and fid in na:
            fixture = na[fid]
            if entry["expected_value"] != fixture[2]:
                errs.append(f"{fid}: N/A value differs from the executable fixture")
            want = "Accepted" if fixture[3] else "Rejected"
            if entry["result"] != want:
                errs.append(f"{fid}: N/A verdict differs from the executable fixture")
            if entry["executor"] != "justified_value":
                errs.append(f"{fid}: N/A executor is not justified_value")
        else:
            errs.append(f"{fid}: unknown fixture kind {entry['kind']!r}")
            continue
        fn = globals().get(entry["executor"])
        if not callable(fn):
            errs.append(f"{fid}: executor {entry['executor']!r} is not callable")
            continue
        if _source_hash(fn) != entry["executor_sha1"]:
            errs.append(f"{fid}: executor source hash does not match the registry")
        described = entry["mutation"]
        if entry["kind"] == "positive":
            if described != "none — the unmutated document is run":
                errs.append(f"{fid}: positive mutation description is not canonical")
        elif entry["kind"] == "na":
            if described != f"set a mandatory cell to {entry['expected_value']!r}":
                errs.append(f"{fid}: N/A mutation description is not canonical")
        else:
            recomputed = _describe_binding(entry)
            if described != recomputed:
                errs.append(f"{fid}: documented mutation description differs from the binding")
        if entry["kind"] == "negative":
            binding_errs, mutated, mut_ctx = _verify_binding(entry, doc, ctx)
            errs.extend(binding_errs)
            fresh = rebuild_ctx(mutated, ctx, mut_ctx)
            expected_check = next((c for c in CHECKS if c[0] == entry["expected_check"]), None)
            if expected_check is None:
                errs.append(f"{fid}: expected check {entry['expected_check']!r} does not exist")
            else:
                observed = run_check(expected_check[2], mutated, fresh, expected_check[0])
                if not observed:
                    errs.append(f"{fid}: expected check {entry['expected_check']} accepted it")
                elif not any(entry["expected_reason"].lower() in e.lower() for e in observed):
                    errs.append(f"{fid}: rejection reason does not contain "
                                f"{entry['expected_reason']!r}")
        elif entry["kind"] == "positive":
            if entry["expected_check"] not in check_ids:
                errs.append(f"{fid}: expected check {entry['expected_check']!r} does not exist")
            else:
                result = run_check(fn, doc, ctx, entry["expected_check"])
                if result != []:
                    errs.append(f"{fid}: clean document did not satisfy the positive fixture")
                if ctx.counts.get(entry["expected_check"], 0) == 0:
                    errs.append(f"{fid}: positive fixture asserted nothing")
        else:
            field = NA_FIELDS.get(fid)
            ok, why = justified_value(entry["expected_value"], field, ctx)
            if ok != (entry["result"] == "Accepted"):
                errs.append(f"{fid}: N/A verdict mismatch ({why})")
        row = catalogue.get(fid)
        if row is None:
            errs.append(f"{fid}: documented catalogue row is missing")
        else:
            for key, cat_key in (("name", "name"), ("mutation", "mutation"),
                                 ("expected_check", "check"), ("expected_reason", "reason"),
                                 ("executor", "executable"), ("result", "result")):
                want = _catalogue_mutation(entry) if key == "mutation" else entry[key]
                if want != row[cat_key]:
                    errs.append(f"{fid}: catalogue {cat_key} differs from the registry")
    if only_set is None:
        cat_ids = set(catalogue)
        if cat_ids != set(ids):
            errs.append(f"catalogue IDs differ from the registry "
                        f"(catalogue-only={sorted(cat_ids - set(ids))}, "
                        f"registry-only={sorted(set(ids) - cat_ids)})")
    return errs


def check_47(doc, ctx, cid):
    """The canonical registry, the catalogue and the executable fixtures agree.

    Every negative fixture is executed and its actual change is compared with the
    declared target and value; the declared executor is identified by name and by
    a source hash; the expected check must reject it with the stated reason; and
    the clean context must survive untouched.
    """
    errs = []
    try:
        data = json.loads(ctx.docs.get("registry", ""))
    except json.JSONDecodeError as exc:
        ctx.need(cid, False, f"fixture registry is not valid JSON: {exc}", errs)
        return errs
    findings = _registry_errors(data, doc, ctx)
    for finding in findings:
        ctx.need(cid, False, finding, errs)
    ctx.need(cid, data.get("totals", {}).get("negative") == len(NEGATIVE_FIXTURES),
             "registry negative-fixture total differs from the executable count", errs)
    ctx.need(cid, data.get("totals", {}).get("positive") == len(POSITIVE_FIXTURES),
             "registry positive-fixture total differs from the executable count", errs)
    ctx.need(cid, data.get("totals", {}).get("na") == len(NA_FIXTURES),
             "registry N/A-fixture total differs from the executable count", errs)
    nf_sec = slice_between(doc, "### 14.12", "## 15.")
    named = set(re.findall(r"`(NF-\d{2})`", nf_sec))
    ctx.need(cid, named and named <= {f["id"] for f in NEGATIVE_FIXTURES},
             f"§14.12 names fixtures absent from the registry: "
             f"{sorted(named - {f['id'] for f in NEGATIVE_FIXTURES})}", errs)
    return errs


def _is_historical(line: str) -> bool:
    low = line.lower()
    return any(k in low for k in ("§63", "§64", "historical", "pre-10c",
                                  "before 10c", "at the time", "formerly", "original"))


def check_48(doc, ctx, cid):
    """Current-status summaries agree with the canonical 124/16 counts."""
    errs = []
    for path in CURRENT_STATUS_DOCS:
        text = ctx.docs["current"].get(path.name, read(path))
        for i, line in enumerate(text.splitlines(), 1):
            low = line.lower()
            if _is_historical(line):
                continue
            if re.search(r"\b120\b", line) and re.search(r"WFA|acceptance tests?", line):
                ctx.need(cid, False, f"{path.name}:{i}: current-status claim of 120 acceptance tests", errs)
            if re.search(r"\b(?:15|fifteen)\s+(?:test\s+)?classes\b", low):
                ctx.need(cid, False, f"{path.name}:{i}: current-status claim of 15 test classes", errs)
            if re.search(r"\b124\b", line) and re.search(r"WFA|acceptance tests?", line):
                ctx.need(cid, True, "", errs)
    handoff = ctx.docs["current"].get("00_stage_2_handoff.md", "")
    ctx.need(cid, "124" in handoff and "16" in handoff,
             "the current Stage 2 handoff does not state 124 acceptance tests in 16 classes", errs)
    ctx.need(cid, "124 acceptance tests in 16 classes" in doc,
             "the canonical document does not state 124 acceptance tests in 16 classes", errs)
    progress = ctx.docs["progress"]
    latest = progress.rsplit("## 65", 1)
    if len(latest) == 2:
        ctx.need(cid, "124" in latest[1] and "16" in latest[1],
                 "the latest progress section does not state 124/16", errs)
    section = ""
    current_124 = False
    for i, line in enumerate(progress.splitlines(), 1):
        heading = re.match(r"^## (\d+)\.", line)
        if heading:
            section = heading.group(1)
            continue
        if section in ("63", "64", "65"):
            continue
        low = line.lower()
        if any(k in low for k in ("historical", "pre-10c", "before 10c",
                                  "at the time", "formerly", "original")):
            continue
        if re.search(r"\b120\b", line) and re.search(r"WFA|acceptance tests?", line):
            ctx.need(cid, False,
                     f"progress log:{i}: active claim of 120 acceptance tests", errs)
        if re.search(r"\b(?:15|fifteen)\s+(?:test\s+)?classes\b", low):
            ctx.need(cid, False,
                     f"progress log:{i}: active claim of 15 test classes", errs)
        if re.search(r"\b124\b", line) and re.search(r"WFA|acceptance tests?", line):
            current_124 = True
    ctx.need(cid, current_124, "the active progress register never states 124 tests", errs)
    return errs


def check_49(doc, ctx, cid):
    """No broad exception handler, no silent pass, deterministic results."""
    errs = []
    src = ctx.docs.get("source", Path(__file__).read_text(encoding="utf-8"))
    ctx.need(cid, not re.search(
        r"(?m)^\s*except\s*(?:Exception|BaseException)?\s*(?:as\s+\w+\s*)?:", src),
        "a broad exception handler is present", errs)
    for c in CHECKS:
        if c[0] in (cid, "42"):
            continue
        first = run_check(c[2], doc, ctx, c[0])
        second = run_check(c[2], doc, ctx, c[0])
        ctx.need(cid, first == second, f"check {c[0]} is not deterministic", errs)
        ctx.need(cid, ctx.counts.get(c[0], 0) > 0, f"check {c[0]} asserts nothing", errs)
    return errs


# --------------------------------------------------------------------------
# registry
# --------------------------------------------------------------------------


def mutation_01(d, c):
    return re.sub(r"\*\*Version:\*\* 1\.0", "**Version:**", d, count=1), c


def mutation_02(d, c):
    return d.replace("**Protected decisions preserved.**", "**Protected decisions noted.**", 1), c


def mutation_03(d, c):
    return d.replace("`OP-09 RESUPPLY`", "`OP-09 RESUPPLY` `OP-10 ESPIONAGE`", 1), c


def mutation_04(d, c):
    return re.sub(r"^\| 25 \|.*\n", "", d, count=1, flags=re.M), c


def mutation_05(d, c):
    return d.replace("#### WFW-002 — Declaration rejected", "#### WFW-001 — Declaration rejected", 1), c


def mutation_06(d, c):
    return d.replace("| Consent | Unilateral", "| ConsentX | Unilateral", 1), c


def mutation_07(d, c):
    return d.replace("**J17 — Loss cap reached mid-campaign.**", "**J18 — Loss cap reached mid-campaign.**", 1), c


def mutation_08(d, c):
    return re.sub(r"^\| `WFE-060` \|", "| `WFE-061` |", d, count=1, flags=re.M), c


def mutation_09(d, c):
    return re.sub(r"^\| `WFA-124` \|.*\n", "", d, count=1, flags=re.M), c


def mutation_10(d, c):
    return re.sub(r"^(\| `WFA-001` \|.*\| )COMPLETE \| NOT RUN \|$", r"\1INCOMPLETE | NOT RUN |", d,
                  count=1, flags=re.M), c


def mutation_11(d, c):
    out = []
    done = False
    for line in d.splitlines(keepends=True):
        if not done and line.startswith("| `WFA-002` |") and line.count("|") == 14:
            parts = line.split("|")
            parts[4] = " P6 "
            line = "|".join(parts)
            done = True
        out.append(line)
    return "".join(out), c


def mutation_12(d, c):
    out = []
    done = False
    for line in d.splitlines(keepends=True):
        if not done and line.startswith("| `WFA-001` |") and line.count("|") == 14:
            line = line.replace("| OPEN |", "| P6 |", 1)
            done = True
        out.append(line)
    return "".join(out), c


def mutation_13(d, c):
    return re.sub(r"^(\| `WFA-121` \|[^\n]*?\| )P \|", r"\1A |", d, count=1, flags=re.M), c


def mutation_14(d, c):
    return re.sub(r"^(\| `WFA-001` \|[^\n]*?\| )WFE-001 \|", r"\1WFE-999 |", d, count=1, flags=re.M), c


def mutation_15(d, c):
    return re.sub(r"^(\| `WFA-001` \|[^\n]*?\| )WFW-001, WFW-002 \|", r"\1WFW-999 |", d, count=1, flags=re.M), c


def mutation_16(d, c):
    return re.sub(r"^(\| `WFA-001` \|[^\n]*?\| )REQ-654, REQ-678 \|", r"\1REQ-704 |", d, count=1, flags=re.M), c


def mutation_17(d, c):
    return re.sub(r"^(\| `WFA-001` \|[^\n]*?`WRF-01`)\s*\|", r"\1, `WRF-19` |", d, count=1, flags=re.M), c


def _edit_row_n(d, prefix, ncols, col, value):
    lines = d.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith(prefix) and len(cells(line)) == ncols:
            parts = [x.strip() for x in line.strip().strip("|").split("|")]
            parts[col] = value
            lines[i] = "| " + " | ".join(parts) + " |\n"
            break
    return "".join(lines)


def mutation_17(d, c):
    return _edit_row_n(d, "| `WFA-001` |", 10, 6, "`WAR-001`, `WRF-19`"), c


def mutation_18(d, c):
    return _edit_row_n(d, "| `WFA-001` |", 10, 6, "`WAR-001`, `WAR-189`"), c


def mutation_19(d, c):
    return _edit_row_n(d, "| `WFA-001` |", 10, 6, "`WAR-001`, `WRA-15`"), c


def mutation_20(d, c):
    return d.replace("WFW-009", "WFW-008"), c


def nf20(d, c):
    return _edit_row_n(d, "| `WFA-001` |", 10, 6, "`WAR-001`, `F-WR-040`"), c


def mutation_21(d, c):
    return _edit_row_n(d, "| `WFE-001` |", 6, 5, "`WFA-999`"), c


def mutation_22(d, c):
    return _edit_row_n(d, "| `WFE-001` |", 6, 5, "`WFA-002`"), c


def mutation_23(d, c):
    return re.sub(r"^\| REQ-703 \|.*\n", "", d, count=1, flags=re.M), c


def mutation_24(d, c):
    return _edit_row_n(d, "| REQ-654 |", 5, 3, "`WFW-999`"), c


def mutation_25(d, c):
    return _edit_row_n(d, "| REQ-655 |", 5, 4, "`WFA-999`"), c


def mutation_26(d, c):
    return re.sub(r"^\| `F-WR-039` \|.*\n", "", d, count=1, flags=re.M), c


def mutation_27(d, c):
    return _edit_row_n(d, "| `F-WR-001` |", 4, 2, "`WFW-999`"), c


def mutation_28(d, c):
    return _edit_row_n(d, "| `F-WR-001` |", 4, 3, "`WFA-999`"), c


def mutation_29(d, c):
    return re.sub(r"^\| `WRA-14` .*\n", "", d, count=1, flags=re.M), c


def mutation_30(d, c):
    return d.replace("| `WRF-14` |", "| `WRF-15` |", 1), c


def mutation_31(d, c):
    return re.sub(r"^\| `B10-AD-25` \|.*\n", "", d, count=1, flags=re.M), c


def mutation_32(d, c):
    return re.sub(r"^\| `B10-C34` \|.*\n", "", d, count=1, flags=re.M), c


def mutation_33(d, c):
    return re.sub(r"^\| 13 \| Prompt 15 \|.*\n", "", d, count=1, flags=re.M), c


def mutation_34(d, c):
    return _edit_row_n(d, "| 13 |", 14, 7, ""), c


def nf13(d, c):
    return _edit_row_n(d, "| `WFE-001` |", 6, 1, "B"), c


def nf35(d, c):
    return _edit_row_n(d, "| 1 |", 14, 5, "`WFA-999`"), c


def mutation_36(d, c):
    return d.replace("`WAR-183`–`WAR-188`", "`WAR-183`–`WAR-187`", 1), c


def mutation_37(d, c):
    return re.sub(r"^\| `WAR-163b` \|.*\n", "", d, count=1, flags=re.M), c


def mutation_38(d, c):
    ctx2 = Ctx.__new__(Ctx)
    ctx2.__dict__.update(c.__dict__)
    ctx2.docs = dict(c.docs)
    ctx2.docs["unresolved"] = c.docs["unresolved"].replace(
        "| `UD-040` | Open |", "| `UD-040` | Resolved |", 1)
    return d, ctx2


def mutation_36r(d, c):
    return d + "\nThis suite was runtime-passed.\n", c


def mutation_37f(d, c):
    return d + "\nA province_id is used for supply.\n", c


def mutation_38p(d, c):
    return d.replace("**PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**", "**CALIBRATED**", 1), c


def mutation_39(d, c):
    return d.replace("230 `WAR-` identifiers (188 numbered plus 42 lettered sub-rules)",
                     "230 `WAR-` identifiers (188 numbered plus 41 lettered sub-rules)", 1), c


def mutation_40(d, c):
    return d.replace("](17_warfare_and_settlements.md)", "](17_missing.md)", 1), c


def mutation_41(d, c):
    return d.replace("### 14.12 Fixture catalogue and named representative subset",
                     "### 14.12 Fixture catalogue (`NF-99`) and named representative subset", 1), c


def mutation_42(d, c):
    ctx2 = Ctx.__new__(Ctx)
    ctx2.__dict__.update(c.__dict__)
    ctx2.registry_override = list(c.registry) + [c.registry[0]]
    return d, ctx2


def mutation_22c(d, c):
    def repl(m):
        return m.group(0).replace("DIRECT VERIFICATION", "NOT COVERED", 1)
    return re.sub(r"^\| REQ-654 \|.*$", repl, d, count=1, flags=re.M), c


def mutation_35(d, c):
    return d.replace("civilian Food", "military Food"), c


def mutation_43(d, c):
    return d.replace("124 acceptance tests in 16 classes", "120 acceptance tests in 16 classes", 1), c


def _ctx_with_docs(c, updates):
    c2 = Ctx.__new__(Ctx)
    c2.__dict__.update(c.__dict__)
    c2.docs = dict(c.docs)
    c2.docs.update(updates)
    return c2


def mutation_44(d, c):
    return re.sub(r"(\| Numbered `WAR-001`–`WAR-188` \| 188 \| )95( \|)",
                  r"\g<1>96\g<2>", d, count=1), c


def mutation_45(d, c):
    out = []
    for line in d.splitlines(keepends=True):
        if line.startswith("| 1 | B-02 phases |"):
            line = line.replace("`TR-040`", "`FAKE-999`", 1)
        out.append(line)
    return "".join(out), c


def mutation_46(d, c):
    lines = d.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("| `WFA-003` |") and len(cells(line)) == 13:
            parts = [x.strip() for x in line.strip().strip("|").split("|")]
            parts[8] = "none"
            lines[i] = "| " + " | ".join(parts) + " |\n"
            break
    return "".join(lines), c


def mutation_47(d, c):
    text = c.docs["catalogue"].replace("| Rejected |", "| Unverified |", 1)
    return d, _ctx_with_docs(c, {"catalogue": text})


def mutation_48(d, c):
    current = dict(c.docs["current"])
    name = "AI_CONTEXT.md"
    current[name] = current[name].replace("124 WFA tests in 16 classes",
                                          "120 WFA tests in 15 classes", 1)
    return d, _ctx_with_docs(c, {"current": current})


def mutation_49(d, c):
    src = c.docs.get("source", "") + "\nexcept Exception:\n    pass\n"
    return d, _ctx_with_docs(c, {"source": src})


def _edit_row(d, prefix, col, value):
    lines = d.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            parts = [x.strip() for x in line.strip().strip("|").split("|")]
            parts[col] = value
            lines[i] = "| " + " | ".join(parts) + " |\n"
            break
    return "".join(lines)


def c41(d, c):
    return _edit_row(d, "| `WAR-001`–`WAR-014` |", 2, "`WFW-999`"), c


def c42(d, c):
    return _edit_row(d, "| `WAR-001`–`WAR-014` |", 3, "`WFA-999`"), c


def c43(d, c):
    return _edit_row(d, "| `WAR-005a` |", 2, "`WFW-999`"), c


def c44(d, c):
    return _edit_row_n(d, "| `WAR-005a` |", 4, 3, "`WFA-999`"), c


def c45(d, c):
    return d.replace("| `WAR-001`–`WAR-014` |", "| `WAR-001`–`WAR-014`, `WAR-999` |", 1), c


def c46(d, c):
    lines = d.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("**14.3.2 Numbered-rule completeness.**"):
            lines.insert(i, "| `WAR-005z` | Fabricated sub-rule | WFW-001 | WFA-001 |\n")
            break
    return "".join(lines), c


def c47(d, c):
    return d.replace("| `F-WR-006` | COMPLETE |", "| `F-WR-040` | COMPLETE |", 1), c


def c48(d, c):
    return d.replace("| `WAR-001`–`WAR-014` |", "| `WAR-001`–`WAR-014` |", 1).replace(
        "| Numbered `WAR-001`–`WAR-188` | 188 | 95 |", "| Numbered `WAR-001`–`WAR-188` | 188 | 96 |", 1), c


def c49(d, c):
    return _edit_row_n(d, "| `WFA-003` |", 10, 4, ""), c


def c50(d, c):
    out = []
    for line in d.splitlines(keepends=True):
        if line.startswith("| `WFA-") and len(cells(line)) == 10:
            line = line.replace("WFW-040", "WFW-039")
        out.append(line)
    return "".join(out), c


def c51(d, c):
    return _edit_row(d, "| `WFE-060` |", 5, "`WFA-001`"), c


def c52(d, c):
    return "".join(l for l in d.splitlines(keepends=True)
                   if not l.startswith("| `WFA-124` |") or len(cells(l)) != 10), c


def _source_append(d, rownum, extra):
    lines = d.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith(f"| {rownum} |") and len(cells(line)) == 14:
            parts = [x.strip() for x in line.strip().strip("|").split("|")]
            parts[2] = parts[2] + ", " + extra
            lines[i] = "| " + " | ".join(parts) + " |\n"
            break
    return "".join(lines)


def c53(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 2, "B-99 / `FAKE-999`"), c


def c54(d, c):
    return _source_append(d, 2, "`ONB-999`"), c


def c55(d, c):
    return _source_append(d, 3, "`ECN-999`"), c


def c56(d, c):
    return _source_append(d, 4, "`URB-999`"), c


def c57(d, c):
    return _source_append(d, 5, "`DMP-999`"), c


def c58(d, c):
    return _source_append(d, 6, "`MKT-999`"), c


def c59(d, c):
    return _source_append(d, 7, "`DIP-999`"), c


def c60(d, c):
    return _source_append(d, 8, "`ALL-999`"), c


def c61(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 3, "WFW-999"), c


def c62(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 5, "WFA-999"), c


def c63(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 6, ""), c


def c64(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 7, ""), c


def c65(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 9, ""), c


def c66(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 11, ""), c


def c67(d, c):
    return _edit_row(d, "| 1 | B-02 phases |", 13, ""), c


CHECKS = [
    ("01", "header, version and design-only status", check_01, mutation_01),
    ("02", "eight fixed constraints and their exact text", check_02, mutation_02),
    ("03", "nine-operation catalogue, no espionage", check_03, mutation_03),
    ("04", "25 lifecycle steps", check_04, mutation_04),
    ("05", "40 workflow headings in sequence", check_05, mutation_05),
    ("06", "23 fields in every workflow", check_06, mutation_06),
    ("07", "17 player journeys", check_07, mutation_07),
    ("08", "60 edge cases", check_08, mutation_08),
    ("09", "124 tests, two linked tables, same IDs", check_09, mutation_09),
    ("10", "identification fields and Definition/Execution values", check_10, mutation_10),
    ("11", "behaviour fields, phase vocabulary, failure/audit/ledger", check_11, mutation_11),
    ("12", "class sizes A-O eight each and P four", check_12, mutation_13),
    ("13", "edge-case primary test exists and class agrees", check_13, mutation_21),
    ("14", "test edge-case references resolve or declare none", check_14, mutation_14),
    ("15", "test workflow references resolve", check_15, mutation_15),
    ("16", "test requirement references resolve to the register", check_16, mutation_16),
    ("17", "rule, failure, audit and formula references resolve", check_17, mutation_17),
    ("18", "every workflow has a dedicated test", check_18, mutation_09),
    ("19", "every edge case is cited back by its test", check_19, mutation_22),
    ("20", "every operation has dedicated coverage", check_20, mutation_20),
    ("21", "REQ-654..703 present once each", check_21, mutation_23),
    ("22", "classification totals 44/1/5/0", check_22, mutation_22c),
    ("23", "requirement rows name live workflows and tests", check_23, mutation_24),
    ("24", "39 formula rows match the register", check_24, mutation_26),
    ("25", "formula rows name live workflows and tests", check_25, mutation_27),
    ("26", "14 audit events with actor, timing, test and replay", check_26, mutation_29),
    ("27", "32 WRF codes, gaps disclosed, every code tested", check_27, mutation_30),
    ("28", "25 architecture decisions match B-10", check_28, mutation_31),
    ("29", "34 conflict entries match B-10", check_29, mutation_32),
    ("30", "13 integration contracts with all fields", check_30, mutation_34),
    ("31", "numbered WAR ranges cover 001..188 exactly", check_31, mutation_36),
    ("32", "42 lettered sub-rules match B-10", check_32, mutation_37),
    ("33", "ten orphan totals, zero unexplained", check_33, mutation_09),
    ("34", "D-014, owner-reserved and register consistency", check_34, mutation_38),
    ("35", "substantive fixed invariants", check_35, mutation_35),
    ("36", "no runtime or implementation claim", check_36, mutation_36r),
    ("37", "no prohibited geographic or destructive construct", check_37, mutation_37f),
    ("38", "provisional labels, no promotion", check_38, mutation_38p),
    ("39", "cross-document counts match B-10 and register", check_39, mutation_39),
    ("40", "internal markdown links resolve", check_40, mutation_40),
    ("41", "ten orphan totals and a labelled representative fixture subset", check_41, mutation_41),
    ("42", "check-registry integrity", check_42, mutation_42),
    ("43", "prose count claims match computed totals", check_43, mutation_43),
    ("44", "per-rule WAR disposition for 188 numbered and 42 lettered", check_44, mutation_44),
    ("45", "13 integration contracts resolve to real subsystem rules", check_45, mutation_45),
    ("46", "justified N/A and none in every mandatory field", check_46, mutation_46),
    ("47", "documented fixture catalogue matches executable fixtures", check_47, mutation_47),
    ("48", "current-status 124/16 claims agree across documents", check_48, mutation_48),
    ("49", "validator integrity, no broad exception, determinism", check_49, mutation_49),
]


# --------------------------------------------------------------------------
# fixtures
# --------------------------------------------------------------------------

POSITIVE_FIXTURES = [
    ("PF-01", "header and design-only status", "01"),
    ("PF-02", "fixed constraints unchanged", "02"),
    ("PF-03", "nine-operation catalogue", "03"),
    ("PF-04", "workflow schema complete", "06"),
    ("PF-05", "two-table test schema joins", "09"),
    ("PF-06", "failure-code coverage and gaps", "27"),
    ("PF-07", "requirement rows complete", "21"),
    ("PF-08", "formula inventory from register", "24"),
    ("PF-09", "audit-event coverage", "26"),
    ("PF-10", "integration contracts complete", "30"),
    ("PF-11", "WAR rule inventory exact", "31"),
    ("PF-12", "D-014 and owner-reserved consistency", "34"),
    ("PF-13", "ten orphan totals at zero", "41"),
]

NEGATIVE_FIXTURES = [
    {"id": "NF-01", "name": "remove the document version", "check": "01",
     "mutator": "mutation_01", "reason": "header missing '**Version:** 1.0'"},
    {"id": "NF-02", "name": "weaken a fixed constraint", "check": "02",
     "mutator": "mutation_02", "reason": "constraint text missing '**Protected decisions preserved.**'"},
    {"id": "NF-03", "name": "add a tenth operation", "check": "03",
     "mutator": "mutation_03", "reason": "operation beyond OP-09"},
    {"id": "NF-04", "name": "delete lifecycle step 25", "check": "04",
     "mutator": "mutation_04", "reason": "lifecycle steps must be 1..25"},
    {"id": "NF-05", "name": "duplicate a workflow heading", "check": "05",
     "mutator": "mutation_05", "reason": "workflow headings must be WFW-001..040 in order"},
    {"id": "NF-06", "name": "rename a mandatory workflow field", "check": "06",
     "mutator": "mutation_06", "reason": "fields differ (found 22 of 23)"},
    {"id": "NF-07", "name": "add an eighteenth journey", "check": "07",
     "mutator": "mutation_07", "reason": "journeys must be J1..J17"},
    {"id": "NF-08", "name": "renumber an edge case to WFE-061", "check": "08",
     "mutator": "mutation_08", "reason": "edge-case IDs are not WFE-001..060"},
    {"id": "NF-09", "name": "delete a test identification row", "check": "09",
     "mutator": "mutation_09", "reason": "identification and behaviour sets differ"},
    {"id": "NF-10", "name": "mark a definition INCOMPLETE", "check": "10",
     "mutator": "mutation_10", "reason": "Definition is 'INCOMPLETE'"},
    {"id": "NF-11", "name": "use an invalid phase", "check": "11",
     "mutator": "mutation_11", "reason": "invalid phase 'P6'"},
    {"id": "NF-12", "name": "assign a class-P test to class A", "check": "12",
     "mutator": "mutation_13", "reason": "class distribution"},
    {"id": "NF-13", "name": "change an edge-case class so it disagrees with its test", "check": "13",
     "mutator": "nf13", "reason": "class B disagrees with WFA-001 class A"},
    {"id": "NF-14", "name": "point a test at WFE-999", "check": "14",
     "mutator": "mutation_14", "reason": "unknown WFE-999"},
    {"id": "NF-15", "name": "point a test at WFW-999", "check": "15",
     "mutator": "mutation_15", "reason": "unknown WFW-999"},
    {"id": "NF-16", "name": "point a test at REQ-704", "check": "16",
     "mutator": "mutation_16", "reason": "REQ-704 outside REQ-654–REQ-703"},
    {"id": "NF-17", "name": "cite unallocated WRF-19", "check": "17",
     "mutator": "mutation_17", "reason": "cites unallocated WRF-19"},
    {"id": "NF-18", "name": "cite WAR-189", "check": "17",
     "mutator": "mutation_18", "reason": "WAR-189 is not in the B-10 inventory"},
    {"id": "NF-19", "name": "cite WRA-15", "check": "17",
     "mutator": "mutation_19", "reason": "unknown WRA-15"},
    {"id": "NF-20", "name": "cite F-WR-040", "check": "17",
     "mutator": "nf20", "reason": "unknown F-WR-040"},
    {"id": "NF-21", "name": "point an edge case at WFA-999", "check": "13",
     "mutator": "mutation_21", "reason": "primary test WFA-999 does not exist"},
    {"id": "NF-22", "name": "make an edge case cite a test that does not cite it", "check": "19",
     "mutator": "mutation_22", "reason": "primary test WFA-002 does not cite it"},
    {"id": "NF-23", "name": "delete REQ-703", "check": "21",
     "mutator": "mutation_23", "reason": "requirement rows must be 654..703"},
    {"id": "NF-24", "name": "point a requirement at WFW-999", "check": "23",
     "mutator": "mutation_24", "reason": "REQ-654: unknown WFW-999"},
    {"id": "NF-25", "name": "point a requirement at WFA-999", "check": "23",
     "mutator": "mutation_25", "reason": "REQ-655: unknown WFA-999"},
    {"id": "NF-26", "name": "delete F-WR-039", "check": "24",
     "mutator": "mutation_26", "reason": "formula rows must be 001..039"},
    {"id": "NF-27", "name": "point a formula at WFW-999", "check": "25",
     "mutator": "mutation_27", "reason": "F-WR-001: unknown WFW-999"},
    {"id": "NF-28", "name": "point a formula at WFA-999", "check": "25",
     "mutator": "mutation_28", "reason": "F-WR-001: unknown WFA-999"},
    {"id": "NF-29", "name": "delete WRA-14", "check": "26",
     "mutator": "mutation_29", "reason": "expected 14 audit rows, found 13"},
    {"id": "NF-30", "name": "redefine WRF-14 as the gap WRF-15", "check": "27",
     "mutator": "mutation_30", "reason": "defined WRF codes differ from the 32-code set"},
    {"id": "NF-31", "name": "delete B10-AD-25", "check": "28",
     "mutator": "mutation_31", "reason": "B10-AD rows must be 01..25"},
    {"id": "NF-32", "name": "delete B10-C34", "check": "29",
     "mutator": "mutation_32", "reason": "B10-C rows must be 01..34"},
    {"id": "NF-33", "name": "delete an integration row", "check": "30",
     "mutator": "mutation_33", "reason": "expected 13 integration rows, found 12"},
    {"id": "NF-34", "name": "blank an integration contract field", "check": "30",
     "mutator": "mutation_34", "reason": "empty mutation owner"},
    {"id": "NF-35", "name": "point an integration test at WFA-999", "check": "30",
     "mutator": "nf35", "reason": "unknown WFA-999"},
    {"id": "NF-36", "name": "shorten a WAR range", "check": "31",
     "mutator": "mutation_36", "reason": "WAR ranges are incomplete or overlapping"},
    {"id": "NF-37", "name": "delete a lettered sub-rule", "check": "32",
     "mutator": "mutation_37", "reason": "lettered table has 41 rows, expected 42"},
    {"id": "NF-38", "name": "mark a UD-040 owner decision resolved", "check": "34",
     "mutator": "mutation_38", "reason": "UD-040 status is 'Resolved', expected Open"},
    {"id": "NF-39", "name": "claim a runtime pass", "check": "36",
     "mutator": "mutation_36r", "reason": "positive runtime claim"},
    {"id": "NF-40", "name": "introduce a mapless violation", "check": "37",
     "mutator": "mutation_37f", "reason": "forbidden construct present: 'province_id'"},
    {"id": "NF-41", "name": "point a numbered-WAR range workflow at WFW-999", "check": "44",
     "mutator": "c41", "reason": "range 001–014: invalid or empty workflow mapping"},
    {"id": "NF-42", "name": "point a numbered-WAR range acceptance test at WFA-999", "check": "44",
     "mutator": "c42", "reason": "range 001–014: invalid or empty test mapping"},
    {"id": "NF-43", "name": "point a lettered-WAR row workflow at WFW-999", "check": "44",
     "mutator": "c43", "reason": "invalid workflow WFW-999"},
    {"id": "NF-44", "name": "point a lettered-WAR row test at WFA-999", "check": "44",
     "mutator": "c44", "reason": "nonexistent test WFA-999"},
    {"id": "NF-45", "name": "insert WAR-999 into a numbered range", "check": "44",
     "mutator": "c45", "reason": "WAR ranges do not equal B-10 numbered definitions"},
    {"id": "NF-46", "name": "insert a fabricated lettered rule", "check": "44",
     "mutator": "c46", "reason": "lettered table differs from B-10"},
    {"id": "NF-47", "name": "cite an invalid formula from a test", "check": "44",
     "mutator": "c47", "reason": "test WFA-004 names unknown F-WR-040"},
    {"id": "NF-48", "name": "claim a DIRECT disposition without a citing test", "check": "44",
     "mutator": "c48", "reason": "!= derived [188, 95, 93, 0, 0]"},
    {"id": "NF-49", "name": "remove the workflow source mapping from a WFA record", "check": "15",
     "mutator": "c49", "reason": "no workflow reference"},
    {"id": "NF-50", "name": "orphan WFW-040", "check": "18",
     "mutator": "c50", "reason": "no dedicated test outside the end-to-end scenario"},
    {"id": "NF-51", "name": "orphan WFE-060", "check": "19",
     "mutator": "c51", "reason": "primary test WFA-001 does not cite it"},
    {"id": "NF-52", "name": "orphan WFA-124", "check": "09",
     "mutator": "c52", "reason": "expected 124 identification rows, found 123"},
    {"id": "NF-53", "name": "point a B-02 integration source at B-99 / FAKE-999", "check": "45",
     "mutator": "c53", "reason": "source identifier FAKE-999 does not exist in b02"},
    {"id": "NF-54", "name": "cite a nonexistent B-03 protection rule", "check": "45",
     "mutator": "c54", "reason": "source identifier ONB-999 does not exist in b03"},
    {"id": "NF-55", "name": "cite a nonexistent B-04 Food rule", "check": "45",
     "mutator": "c55", "reason": "source identifier ECN-999 does not exist in b04"},
    {"id": "NF-56", "name": "cite a nonexistent B-05 infrastructure rule", "check": "45",
     "mutator": "c56", "reason": "source identifier URB-999 does not exist in b05"},
    {"id": "NF-57", "name": "cite a nonexistent B-06 political rule", "check": "45",
     "mutator": "c57", "reason": "source identifier DMP-999 does not exist in b06"},
    {"id": "NF-58", "name": "cite a nonexistent B-07 trade rule", "check": "45",
     "mutator": "c58", "reason": "source identifier MKT-999 does not exist in b07"},
    {"id": "NF-59", "name": "cite a nonexistent B-08 diplomatic rule", "check": "45",
     "mutator": "c59", "reason": "source identifier DIP-999 does not exist in b08"},
    {"id": "NF-60", "name": "cite a nonexistent B-09 Alliance rule", "check": "45",
     "mutator": "c60", "reason": "source identifier ALL-999 does not exist in b09"},
    {"id": "NF-61", "name": "point an integration workflow at WFW-999", "check": "45",
     "mutator": "c61", "reason": "unknown WFW-999"},
    {"id": "NF-62", "name": "point an integration test at WFA-999", "check": "45",
     "mutator": "c62", "reason": "unknown WFA-999"},
    {"id": "NF-63", "name": "remove an integration validation owner", "check": "45",
     "mutator": "c63", "reason": "validation owner invalid (empty mandatory field)"},
    {"id": "NF-64", "name": "remove an integration mutation owner", "check": "45",
     "mutator": "c64", "reason": "mutation owner invalid (empty mandatory field)"},
    {"id": "NF-65", "name": "remove integration phase ordering", "check": "45",
     "mutator": "c65", "reason": "ordering invalid (empty mandatory field)"},
    {"id": "NF-66", "name": "remove integration failure handling", "check": "45",
     "mutator": "c66", "reason": "failure/recovery invalid (empty mandatory field)"},
    {"id": "NF-67", "name": "remove integration privacy", "check": "45",
     "mutator": "c67", "reason": "privacy invalid (empty mandatory field)"},
]

NA_FIXTURES = [
    ("NA-01", "bare N/A formula", "N/A", False),
    ("NA-02", "bare N/A ledger", "N/A", False),
    ("NA-03", "bare NONE audit", "NONE", False),
    ("NA-04", "bare none failure", "none", False),
    ("NA-05", "empty mandatory field", "", False),
    ("NA-06", "empty N/A reason", "N/A — ", False),
    ("NA-07", "punctuation-only justification", "N/A — ...", False),
    ("NA-08", "valid N/A with a meaningful explanation", "N/A — no failure code exists for a lawful outcome", True),
    ("NA-09", "valid NONE with a meaningful explanation", "none — a read-only query writes no ledger item", True),
    ("NA-10", "valid existing formula identifier", "`F-WR-031`", True),
]

NA_FIELDS = {
    "NA-01": "formula", "NA-02": "ledger", "NA-03": "audit", "NA-04": "failure",
    "NA-05": "ledger", "NA-06": "formula", "NA-07": "formula",
    "NA-08": "failure", "NA-09": "ledger", "NA-10": "formula",
}

C3_NA_TESTS = [
    ("C3-NA-01", "bare N/A is rejected in any case or padding",
     ("N/A", " n/a ", "NA"), "formula", False),
    ("C3-NA-02", "bare NONE is rejected in any case",
     ("NONE", "none", "None"), "audit", False),
    ("C3-NA-03", "empty and whitespace-only values are rejected",
     ("", "   ", "\t"), "ledger", False),
    ("C3-NA-04", "N/A citing an unresolved WAR identifier is rejected",
     ("N/A — no formula applies; see `WAR-999`", "NONE — `WAR-999`"), "formula", False),
    ("C3-NA-05", "N/A citing an unresolved WFW identifier is rejected",
     ("N/A — no audit event exists for `WFW-999`",), "audit", False),
    ("C3-NA-06", "N/A citing an unresolved WFA identifier is rejected",
     ("N/A — no ledger item exists for `WFA-999`",), "ledger", False),
    ("C3-NA-07", "placeholder word because is rejected",
     ("N/A — because", "N/A — no", "N/A — none"), "failure", False),
    ("C3-NA-08", "not-applicable and no-details placeholders are rejected",
     ("N/A — not applicable", "NONE — no details"), "formula", False),
    ("C3-NA-09", "empty reason after a reason label is rejected",
     ("N/A — reason:", "NONE — reason:"), "audit", False),
    ("C3-NA-10", "punctuation-only values and reasons are rejected",
     ("...", "—", "---", "N/A — ...", "N/A — reason: ."), "wfe", False),
    ("C3-NA-11", "a valid-looking explanation with an invalid identifier is rejected",
     ("N/A — no formula applies; the check is in `WFR-999`",), "formula", False),
    ("C3-NA-12", "a valid explanation with an applicable real identifier is accepted",
     ("N/A — no formula applies; the check is structural (`WAR-155`)",), "formula", True),
    ("C3-NA-13", "a valid field-specific explanation without an identifier is accepted",
     ("N/A — no arithmetic applies to this consent rule",), "formula", True),
    ("C3-NA-14", "a real formula identifier is accepted as an ordinary value",
     ("`F-WR-031`", "F-WR-031"), None, True),
    ("C3-NA-15", "an ordinary WFA identifier is accepted as an ordinary value",
     ("`WFA-001`", "WFA-124"), None, True),
]

# Exact mutation binding for every negative fixture.  `op` is one of replace,
# edit_row, delete_row, insert_row, append.  The registry is generated from these
# declarations and checked against the live executor on every run.
FIXTURE_BINDINGS = {
    "NF-01": {"op": "replace", "target": "**Version:**", "old": "**Version:** 1.0", "new": "**Version:**"},
    "NF-02": {"op": "replace", "target": "**Protected decisions preserved.**",
              "old": "**Protected decisions preserved.**", "new": "**Protected decisions noted.**"},
    "NF-03": {"op": "replace", "target": "`OP-09 RESUPPLY`",
              "old": "`OP-09 RESUPPLY`", "new": "`OP-09 RESUPPLY` `OP-10 ESPIONAGE`"},
    "NF-04": {"op": "delete_row", "target": "| 25 |"},
    "NF-05": {"op": "replace", "target": "#### WFW-002 — Declaration rejected",
              "old": "#### WFW-002 — Declaration rejected",
              "new": "#### WFW-001 — Declaration rejected"},
    "NF-06": {"op": "replace", "target": "| Consent | Unilateral",
              "old": "| Consent | Unilateral", "new": "| ConsentX | Unilateral"},
    "NF-07": {"op": "replace", "target": "**J17 — Loss cap reached mid-campaign.**",
              "old": "**J17 — Loss cap reached mid-campaign.**",
              "new": "**J18 — Loss cap reached mid-campaign.**"},
    "NF-08": {"op": "replace", "target": "| `WFE-060` |",
              "old": "| `WFE-060` |", "new": "| `WFE-061` |"},
    "NF-09": {"op": "delete_row", "target": "| `WFA-124` |", "ncols": 10},
    "NF-10": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 8},
    "NF-11": {"op": "edit_row", "target": "| `WFA-002` |", "ncols": 13, "field": 3},
    "NF-12": {"op": "edit_row", "target": "| `WFA-121` |", "ncols": 10, "field": 2},
    "NF-13": {"op": "edit_row", "target": "| `WFE-001` |", "ncols": 6, "field": 1},
    "NF-14": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 5},
    "NF-15": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 4},
    "NF-16": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 3},
    "NF-17": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 6},
    "NF-18": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 6},
    "NF-19": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 6},
    "NF-20": {"op": "edit_row", "target": "| `WFA-001` |", "ncols": 10, "field": 6},
    "NF-21": {"op": "edit_row", "target": "| `WFE-001` |", "ncols": 6, "field": 5},
    "NF-22": {"op": "edit_row", "target": "| `WFE-001` |", "ncols": 6, "field": 5},
    "NF-23": {"op": "delete_row", "target": "| REQ-703 |"},
    "NF-24": {"op": "edit_row", "target": "| REQ-654 |", "ncols": 5, "field": 3},
    "NF-25": {"op": "edit_row", "target": "| REQ-655 |", "ncols": 5, "field": 4},
    "NF-26": {"op": "delete_row", "target": "| `F-WR-039` |"},
    "NF-27": {"op": "edit_row", "target": "| `F-WR-001` |", "ncols": 4, "field": 2},
    "NF-28": {"op": "edit_row", "target": "| `F-WR-001` |", "ncols": 4, "field": 3},
    "NF-29": {"op": "delete_row", "target": "| `WRA-14` "},
    "NF-30": {"op": "replace", "target": "| `WRF-14` |",
              "old": "| `WRF-14` |", "new": "| `WRF-15` |"},
    "NF-31": {"op": "delete_row", "target": "| `B10-AD-25` |"},
    "NF-32": {"op": "delete_row", "target": "| `B10-C34` |"},
    "NF-33": {"op": "delete_row", "target": "| 13 | Prompt 15 |", "ncols": 14},
    "NF-34": {"op": "edit_row", "target": "| 13 |", "ncols": 14, "field": 7},
    "NF-35": {"op": "edit_row", "target": "| 1 |", "ncols": 14, "field": 5},
    "NF-36": {"op": "replace", "target": "`WAR-183`–`WAR-188`",
              "old": "`WAR-183`–`WAR-188`", "new": "`WAR-183`–`WAR-187`"},
    "NF-37": {"op": "delete_row", "target": "| `WAR-163b` |"},
    "NF-38": {"op": "replace", "source": "unresolved", "target": "| `UD-040` | Open |",
              "old": "| `UD-040` | Open |", "new": "| `UD-040` | Resolved |"},
    "NF-39": {"op": "append", "target": "end of document", "new": "This suite was runtime-passed."},
    "NF-40": {"op": "append", "target": "end of document", "new": "A province_id is used for supply."},
    "NF-41": {"op": "edit_row", "target": "| `WAR-001`–`WAR-014` |", "ncols": 4, "field": 2},
    "NF-42": {"op": "edit_row", "target": "| `WAR-001`–`WAR-014` |", "ncols": 4, "field": 3},
    "NF-43": {"op": "edit_row", "target": "| `WAR-005a` |", "ncols": 4, "field": 2},
    "NF-44": {"op": "edit_row", "target": "| `WAR-005a` |", "ncols": 4, "field": 3},
    "NF-45": {"op": "replace", "target": "| `WAR-001`–`WAR-014` |",
              "old": "| `WAR-001`–`WAR-014` |", "new": "| `WAR-001`–`WAR-014`, `WAR-999` |"},
    "NF-46": {"op": "insert_row", "target": "| `WAR-005z` |"},
    "NF-47": {"op": "replace", "target": "| `F-WR-006` |",
              "old": "| `F-WR-006` | COMPLETE |", "new": "| `F-WR-040` | COMPLETE |"},
    "NF-48": {"op": "replace", "target": "| Numbered `WAR-001`–`WAR-188` |",
              "old": "| Numbered `WAR-001`–`WAR-188` | 188 | 95 |",
              "new": "| Numbered `WAR-001`–`WAR-188` | 188 | 96 |"},
    "NF-49": {"op": "edit_row", "target": "| `WFA-003` |", "ncols": 10, "field": 4},
    "NF-50": {"op": "replace", "target": "WFW-040", "scope": "| `WFA-",
              "old": "WFW-040", "new": "WFW-039"},
    "NF-51": {"op": "edit_row", "target": "| `WFE-060` |", "ncols": 6, "field": 5},
    "NF-52": {"op": "delete_row", "target": "| `WFA-124` |", "ncols": 10},
    "NF-53": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 2},
    "NF-54": {"op": "edit_row", "target": "| 2 | B-03 protection", "ncols": 14, "field": 2},
    "NF-55": {"op": "edit_row", "target": "| 3 | B-04 economy", "ncols": 14, "field": 2},
    "NF-56": {"op": "edit_row", "target": "| 4 | B-05 cities", "ncols": 14, "field": 2},
    "NF-57": {"op": "edit_row", "target": "| 5 | B-06 population", "ncols": 14, "field": 2},
    "NF-58": {"op": "edit_row", "target": "| 6 | B-07 market", "ncols": 14, "field": 2},
    "NF-59": {"op": "edit_row", "target": "| 7 | B-08 diplomacy", "ncols": 14, "field": 2},
    "NF-60": {"op": "edit_row", "target": "| 8 | B-09 Alliance", "ncols": 14, "field": 2},
    "NF-61": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 3},
    "NF-62": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 5},
    "NF-63": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 6},
    "NF-64": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 7},
    "NF-65": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 9},
    "NF-66": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 11},
    "NF-67": {"op": "edit_row", "target": "| 1 | B-02 phases |", "ncols": 14, "field": 13},
}


def _describe_binding(entry: dict) -> str:
    op = entry["op"]
    target = entry["target"]
    if op == "edit_row":
        return (f"edit row {target!r}, field {entry['field']}: "
                f"{entry['old_value']!r} → {entry['expected_value']!r}")
    if op == "delete_row":
        return f"delete row {target!r}"
    if op == "insert_row":
        return f"insert line {entry['expected_value']!r}"
    if op == "replace":
        scope = f" within lines containing {entry['scope']!r}" if entry.get("scope") else ""
        return (f"replace {entry['old_value']!r} with {entry['expected_value']!r}"
                f" in {entry['source']}{scope}")
    if op == "append":
        return f"append {entry['expected_value']!r} to {entry['source']}"
    return f"{op} {target!r}"


def _derive_binding(spec: dict, doc: str, ctx, mutator: str):
    entry = {
        "op": spec["op"],
        "source": spec.get("source", "doc"),
        "target": spec.get("target", ""),
        "ncols": spec.get("ncols"),
        "field": spec.get("field"),
        "scope": spec.get("scope", ""),
        "old_value": "",
        "expected_value": "",
    }
    source = entry["source"]
    before_text = doc if source == "doc" else _fixture_source_text(ctx, source)
    after, mut_ctx = globals()[mutator](doc, ctx)
    after_ctx = mut_ctx if isinstance(mut_ctx, Ctx) else ctx
    after_text = after if source == "doc" else _fixture_source_text(after_ctx, source)
    if entry["op"] == "edit_row":
        before_rows = _find_rows(before_text.splitlines(), entry["target"], entry["ncols"])
        after_rows = _find_rows(after_text.splitlines(), entry["target"], entry["ncols"])
        if len(before_rows) != 1 or len(after_rows) != 1:
            raise ValueError(f"{entry['target']!r} is not a unique row for the declared binding")
        entry["old_value"] = cells(before_rows[0][1])[entry["field"]]
        entry["expected_value"] = cells(after_rows[0][1])[entry["field"]]
    elif entry["op"] == "delete_row":
        entry["old_value"] = "<row present>"
        entry["expected_value"] = "<absent>"
    elif entry["op"] == "insert_row":
        after_rows = _find_rows(after_text.splitlines(), entry["target"], None)
        if len(after_rows) != 1:
            raise ValueError(f"inserted row {entry['target']!r} is not unique")
        entry["old_value"] = "<absent>"
        entry["expected_value"] = after_rows[0][1].strip()
    elif entry["op"] == "replace":
        entry["old_value"] = spec["old"]
        entry["expected_value"] = spec["new"]
    elif entry["op"] == "append":
        entry["old_value"] = "<end of source>"
        entry["expected_value"] = spec["new"]
    else:
        raise ValueError(f"unknown binding operation {entry['op']!r}")
    entry["mutation"] = _describe_binding(entry)
    return entry


def build_registry(doc: str, ctx) -> dict:
    fixtures = []
    for fid, name, cid in POSITIVE_FIXTURES:
        fn = globals()[f"check_{cid}"]
        fixtures.append({
            "id": fid, "kind": "positive", "name": name,
            "op": "positive", "source": "doc", "target": "clean document",
            "ncols": None, "field": None, "scope": "",
            "old_value": "<unmutated>", "expected_value": "<pass>",
            "expected_check": cid,
            "expected_reason": "clean document satisfies this check",
            "executor": fn.__name__, "executor_sha1": _source_hash(fn),
            "mutation": "none — the unmutated document is run",
            "result": "Accepted", "doc_ref": "§14.12",
        })
    for f in NEGATIVE_FIXTURES:
        entry = _derive_binding(FIXTURE_BINDINGS[f["id"]], doc, ctx, f["mutator"])
        entry.update({
            "id": f["id"], "kind": "negative", "name": f["name"],
            "expected_check": f["check"], "expected_reason": f["reason"],
            "executor": f["mutator"],
            "executor_sha1": _source_hash(globals()[f["mutator"]]),
            "result": "Rejected", "doc_ref": "§14.12",
        })
        fixtures.append(entry)
    for fid, name, value, expected_ok in NA_FIXTURES:
        fixtures.append({
            "id": fid, "kind": "na", "name": name, "op": "value",
            "source": "cell", "target": "single mandatory cell",
            "ncols": None, "field": NA_FIELDS.get(fid), "scope": "",
            "old_value": "", "expected_value": value,
            "expected_check": "NA", "expected_reason": name,
            "executor": "justified_value", "executor_sha1": _source_hash(justified_value),
            "mutation": f"set a mandatory cell to {value!r}",
            "result": "Accepted" if expected_ok else "Rejected",
            "doc_ref": "§14.12",
        })
    return {
        "schema": 1,
        "generated_by": "verify_warfare_workflows.py --emit-catalogue",
        "totals": {
            "positive": len(POSITIVE_FIXTURES),
            "negative": len(NEGATIVE_FIXTURES),
            "na": len(NA_FIXTURES),
        },
        "fixtures": fixtures,
    }



def mutation_nf35(d, c):
    out = []
    for line in d.splitlines(keepends=True):
        if line.startswith("| 13 | Prompt 15 |"):
            line = line.replace("| WFA-120 |", "| WFA-999 |", 1)
        out.append(line)
    return "".join(out), c


NAMED_FIXTURES = {"NF35": mutation_nf35}


def apply_fixture(doc, ctx, fixture):
    fn = globals().get(fixture["mutator"])
    if not callable(fn):
        raise KeyError(fixture["mutator"])
    return fn(doc, ctx)


def run_check(func, doc, ctx, cid):
    ctx.counts[cid] = 0
    result = func(doc, ctx, cid)
    if result is None:
        return None
    return result


def rebuild_ctx(mutated, base, mut_ctx):
    """Re-parse a mutated document so cached structure reflects the mutation."""
    source = mut_ctx if isinstance(mut_ctx, Ctx) else base
    fresh = Ctx(mutated, source.docs)
    fresh.registry = source.registry or base.registry
    fresh.registry_override = source.registry_override
    return fresh


SELF_TEST_TIMEOUT = 120.0


def self_test(doc, ctx):
    failures = 0
    skipped: list[str] = []
    start = time.monotonic()
    deadline = start + SELF_TEST_TIMEOUT
    base = Ctx(doc, dict(ctx.docs))
    base.registry = list(CHECKS)
    base.registry_override = None

    print("SELF-TEST")
    print(f"  START {time.strftime('%Y-%m-%dT%H:%M:%S')}  "
          f"timeout {SELF_TEST_TIMEOUT:.0f}s  checks {len(CHECKS)}")

    def over_budget() -> bool:
        return time.monotonic() > deadline

    # 1. registry integrity
    reg_ids = [c[0] for c in CHECKS]
    if reg_ids != [f"{i:02d}" for i in range(1, len(CHECKS) + 1)]:
        print(f"  REGISTRY FAIL: IDs are {reg_ids}")
        failures += 1
    else:
        print(f"  REGISTRY PASS: {len(CHECKS)} unique sequential check IDs")

    # 2. clean run — every check passes and asserts, on an isolated context
    clean_fail = 0
    for cid, name, func, _mut in CHECKS:
        errs = run_check(func, doc, base, cid)
        if errs is None:
            print(f"  CLEAN FAIL [{cid}] returned None")
            clean_fail += 1
        elif errs:
            print(f"  CLEAN FAIL [{cid}] {name}: {errs}")
            clean_fail += 1
        elif base.counts.get(cid, 0) == 0:
            print(f"  CLEAN FAIL [{cid}] passed without asserting")
            clean_fail += 1
    if clean_fail:
        failures += 1
    else:
        print(f"  CLEAN PASS: {len(CHECKS)}/{len(CHECKS)} checks passed, each with assertions")

    # 3. positive fixtures
    pf_ok = 0
    for fid, name, cid in POSITIVE_FIXTURES:
        func = next(c[2] for c in CHECKS if c[0] == cid)
        errs = run_check(func, doc, base, cid)
        if not errs and base.counts.get(cid, 0) > 0:
            pf_ok += 1
        else:
            print(f"  POSITIVE FAIL [{fid}] {name}: {errs}")
    print(f"  POSITIVE: {pf_ok}/{len(POSITIVE_FIXTURES)} accepted")
    if pf_ok != len(POSITIVE_FIXTURES):
        failures += 1

    # 4. per-check mutations
    mut_ok = 0
    for cid, name, func, mut in CHECKS:
        mutated, mut_ctx = mut(doc, base)
        docs_changed = isinstance(mut_ctx, Ctx) and mut_ctx.docs != base.docs
        if mutated == doc and not docs_changed and cid != "42":
            print(f"  MUTATION FAIL [{cid}] {name}: mutation did not change the document")
            failures += 1
            continue
        errs = run_check(func, mutated, rebuild_ctx(mutated, base, mut_ctx), cid)
        if errs:
            mut_ok += 1
        else:
            print(f"  MUTATION FAIL [{cid}] {name}: mutation was not detected")
            failures += 1
    print(f"  MUTATIONS: {mut_ok}/{len(CHECKS)} detected")

    # 5. negative fixtures — targeted binding verification, not a rerun of every check
    registry_data = json.loads(base.docs["registry"])
    nf_errors = _registry_errors(registry_data, doc, base)
    nf_ok = 0
    for f in NEGATIVE_FIXTURES:
        mine = [e for e in nf_errors if e.startswith(f["id"] + ":")]
        if mine:
            print(f"  NEGATIVE FAIL [{f['id']}] {f['name']}: {mine[:2]}")
        else:
            nf_ok += 1
    print(f"  NEGATIVE: {nf_ok}/{len(NEGATIVE_FIXTURES)} bound, executed and rejected "
          f"at the expected check")
    if nf_ok != len(NEGATIVE_FIXTURES):
        failures += 1

    # 6. ten N/A unit fixtures
    na_ok = 0
    for fid, name, value, expected_ok in NA_FIXTURES:
        ok, _why = justified_value(value, NA_FIELDS.get(fid), base)
        if ok == expected_ok:
            na_ok += 1
        else:
            print(f"  NA FAIL [{fid}] {name}: got {ok}, expected {expected_ok}")
    print(f"  N/A FIXTURES: {na_ok}/{len(NA_FIXTURES)} matched the expected verdict")
    if na_ok != len(NA_FIXTURES):
        failures += 1

    # 7. C3-NF-01..05 — permanent meta-tests of the registry binding itself
    c3nf_ok = 0
    original = json.loads(base.docs["registry"])

    def tampered(mutate):
        data = json.loads(json.dumps(original))
        entry = next(x for x in data["fixtures"] if x["id"] == "NF-53")
        mutate(entry, data)
        return data

    c3nf_cases = [
        ("C3-NF-01", "a different valid executor is rejected",
         lambda e, d: e.update(executor="c54")),
        ("C3-NF-02", "a replaced description is rejected",
         lambda e, d: e.update(name="a different documented description")),
        ("C3-NF-03", "an incorrect mutation target is rejected",
         lambda e, d: e.update(target="| 2 | B-03 protection", field=4,
                               old_value="wrong", expected_value="wrong")),
        ("C3-NF-04", "an incorrect expected check is rejected",
         lambda e, d: e.update(expected_check="46")),
    ]
    for fid, name, mutate in c3nf_cases:
        errs = _registry_errors(tampered(mutate), doc, base, only=("NF-53",))
        if errs:
            c3nf_ok += 1
        else:
            print(f"  C3-NF FAIL [{fid}] {name}: corruption was accepted")
    # C3-NF-05: the original NF-53 definition is accepted and still rejected by 45
    nf53 = next(x for x in original["fixtures"] if x["id"] == "NF-53")
    errs = _registry_errors(original, doc, base, only=("NF-53",))
    if not errs:
        mutated, mut_ctx = apply_fixture(doc, base, next(f for f in NEGATIVE_FIXTURES
                                                         if f["id"] == "NF-53"))
        fresh = rebuild_ctx(mutated, base, mut_ctx)
        observed = run_check(check_45, mutated, fresh, "45")
        if observed and any(nf53["expected_reason"].lower() in e.lower() for e in observed):
            c3nf_ok += 1
        else:
            print("  C3-NF FAIL [C3-NF-05] original NF-53 was not rejected with the stated reason")
    else:
        print(f"  C3-NF FAIL [C3-NF-05] original NF-53 definition: {errs[:2]}")
    print(f"  C3-NF: {c3nf_ok}/5 registry-binding meta-tests passed")
    if c3nf_ok != 5:
        failures += 1

    # 8. C3-NA-01..15 — permanent N/A and identifier-enforcement tests
    c3na_ok = 0
    for fid, name, values, field, expected_ok in C3_NA_TESTS:
        verdicts = [justified_value(value, field, base)[0] for value in values]
        if all(v == expected_ok for v in verdicts):
            c3na_ok += 1
        else:
            print(f"  C3-NA FAIL [{fid}] {name}: got {verdicts}, expected {expected_ok}")
    print(f"  C3-NA: {c3na_ok}/{len(C3_NA_TESTS)} N/A enforcement tests passed")
    if c3na_ok != len(C3_NA_TESTS):
        failures += 1

    # 9. bounded-time and skip report
    elapsed = time.monotonic() - start
    timed_out = elapsed > SELF_TEST_TIMEOUT or over_budget()
    if timed_out:
        failures += 1
        print(f"  TIMEOUT: elapsed {elapsed:.2f}s exceeds the {SELF_TEST_TIMEOUT:.0f}s bound")
    finish = time.strftime('%Y-%m-%dT%H:%M:%S')
    print(f"  FINISH {finish}  ELAPSED {elapsed:.2f}s  LIMIT {SELF_TEST_TIMEOUT:.0f}s  "
          f"STATUS {'TIMEOUT' if timed_out else 'WITHIN BOUND'}")
    print(f"  TOTALS: checks {len(CHECKS)}  positive {len(POSITIVE_FIXTURES)}  "
          f"negative {len(NEGATIVE_FIXTURES)}  N/A {len(NA_FIXTURES)}  "
          f"C3-NF 5  C3-NA {len(C3_NA_TESTS)}  skipped {len(skipped)}")
    for item in skipped:
        print(f"  SKIPPED: {item}")
    print("SELF-TEST RESULT:", "PASS" if failures == 0 else "FAIL")
    return 0 if failures == 0 else 1


def _md_cell(value) -> str:
    return str(value).replace("|", "/").strip()


def _catalogue_mutation(entry: dict) -> str:
    return entry["mutation"].replace("|", "/")


def build_catalogue(registry: dict) -> str:
    """Render the catalogue as a projection of the canonical JSON registry."""
    lines = [
        "# Warfare acceptance fixture catalogue",
        "",
        "This file is **generated** by `verify_warfare_workflows.py --emit-catalogue`.",
        "It is a projection of `warfare_fixture_registry.json`, which is the single",
        "canonical machine-readable mapping between documented fixtures and the",
        "executable functions in the validator. A fixture that appears here but has",
        "no callable implementation, an executor whose source hash differs, a",
        "mutation that does not produce the declared target value, or an executable",
        "fixture absent here fails check 47.",
        "",
        "| Fixture | Name | Exact mutation | Expected check | Expected reason | Executable | Result |",
        "|---|---|---|---|---|---|---|",
    ]
    for entry in registry["fixtures"]:
        lines.append("| " + " | ".join(_md_cell(x) for x in (
            entry["id"], entry["name"], _catalogue_mutation(entry),
            entry["expected_check"], entry["expected_reason"],
            entry["executor"], entry["result"],
        )) + " |")
    totals = registry["totals"]
    lines.append("")
    lines.append(f"Totals: {totals['positive']} positive, "
                 f"{totals['negative']} negative, {totals['na']} N/A.")
    lines.append("")
    return "\n".join(lines)


def reference_scan_text(doc: str) -> str:
    """Document text excluding fixture and disposition prose that names deliberate
    negative-example placeholders (`WAR-999`, `WFA-999`, and so on). The §17.6
    correction-evidence table cites the same placeholders and is excluded for the
    same reason; it is evidence about the fixtures, not a normative reference."""
    out = doc
    for start, end in (("**14.3.6 Per-rule disposition.**", "### 14.4"),
                       ("### 14.12", "## 15."),
                       ("**17.6 C3 correction evidence", None)):
        i = out.find(start)
        if i < 0:
            continue
        if end is None:
            out = out[:i]
        else:
            j = out.find(end)
            if j > i:
                out = out[:i] + out[j:]
    return out


def report_metrics(doc, ctx) -> list[tuple[str, object]]:
    """Compute the twenty-seven reported totals independently of each other."""
    docs = ctx.docs
    scan = reference_scan_text(doc)
    numbered = b10_numbered(docs["b10"])
    lettered = b10_lettered(docs["b10"])
    ident = ctx.parsed["wfa_ident"]
    beh = ctx.parsed["wfa_beh"]
    disp = war_dispositions(ctx, doc)

    numbered_ok = sum(1 for rid in numbered
                      if f"WAR-{rid:03d}" in disp and disp[f"WAR-{rid:03d}"]["workflows"]
                      and disp[f"WAR-{rid:03d}"]["tests"])
    lettered_ok = sum(1 for rid in lettered
                      if rid in disp and disp[rid]["workflows"] and disp[rid]["tests"])

    war_refs = set(re.findall(r"WAR-\d{3}[a-z]?", scan))
    invalid_war = {t for t in war_refs
                   if (t[4:].isdigit() and int(t[4:]) not in numbered) or
                      (not t[4:].isdigit() and t not in lettered)}
    invalid_wfw = {t for t in re.findall(r"WFW-\d{3}", scan) if not 1 <= int(t[4:]) <= WFW_TOTAL}
    invalid_wfe = {t for t in re.findall(r"WFE-\d{3}", scan) if not 1 <= int(t[4:]) <= WFE_TOTAL}
    invalid_wfa = {t for t in re.findall(r"WFA-\d{3}", scan) if not 1 <= int(t[4:]) <= WFA_TOTAL}
    formulas = register_formulas(docs["register"])
    invalid_formula = {t for t in re.findall(r"F-WR-\d{3}", scan) if int(t[5:]) not in formulas}

    sec = slice_between(doc, "### 14.9 Subsystem and prompt integration rows", "### 14.10")
    rows = [c for c in table_rows(sec) if c and c[0].isdigit() and len(c) == 14]
    subsystem_key = {1: "b02", 2: "b03", 3: "b04", 4: "b05", 5: "b06",
                     6: "b07", 7: "b08", 8: "b09", 9: "b10", 10: "b10",
                     11: "b10", 12: "b10", 13: "doc"}
    invalid_source = 0
    for c in rows:
        n = int(c[0])
        for tok in IDENT_RE.findall(c[2]):
            if not _resolve_ident(tok, docs, subsystem_key[n]):
                invalid_source += 1

    bad_na = 0
    for wid, v in ident.items():
        for f in ("wfe", "formula"):
            if not justified_value(v[f], f, ctx)[0]:
                bad_na += 1
    for wid, v in beh.items():
        for f in ("ledger", "audit", "failure", "privacy"):
            if not justified_value(v[f], f, ctx)[0]:
                bad_na += 1

    cat_rows = parse_catalogue(docs["catalogue"])
    doc_nf = [r for r in cat_rows if r["id"].startswith("NF-")]
    exec_by_id = {f["id"]: f for f in NEGATIVE_FIXTURES}
    aligned = sum(1 for r in doc_nf
                  if r["id"] in exec_by_id
                  and r["executable"] == exec_by_id[r["id"]]["mutator"]
                  and r["check"] == exec_by_id[r["id"]]["check"])

    forward_orphans = sum(1 for rid, v in disp.items()
                          if not v["workflows"] or not v["tests"])
    workflows_cited = {w for w in ctx.parsed["wfa_ident"].values()
                       for w in expand(w["wfw"], "WFW")}
    reverse_orphans = sum(1 for n in range(1, WFW_TOTAL + 1) if n not in workflows_cited)
    reverse_orphans += sum(1 for e in range(1, WFE_TOTAL + 1)
                           if f"WFE-{e:03d}" not in ctx.parsed["wfe"])
    reverse_orphans += sum(1 for n in range(1, WFA_TOTAL + 1)
                           if f"WFA-{n:03d}" not in ident
                           or not expand(ident[f"WFA-{n:03d}"]["wfw"], "WFW")
                           or not re.search(r"REQ-\d{3}", ident[f"WFA-{n:03d}"]["req"]))

    passed = failed = 0
    for cid, _name, func, _mut in CHECKS:
        result = run_check(func, doc, ctx, cid)
        if result == []:
            passed += 1
        else:
            failed += 1
    check_src = {c[0]: inspect.getsource(c[2]) for c in CHECKS}
    d014_checks = sum(1 for s in check_src.values() if 'ctx.docs["autonomy"]' in s)
    owner_reserved = sum(1 for s in check_src.values()
                         if re.search(r"UD-04|range\(40, 50\)", s))

    return [
        ("total check definitions", len(CHECKS)),
        ("unique check IDs", len({c[0] for c in CHECKS})),
        ("executed", len(CHECKS)),
        ("passed", passed),
        ("failed", failed),
        ("skipped", 0),
        ("authoritative numbered WAR", len(numbered)),
        ("authoritative lettered WAR", len(lettered)),
        ("numbered WAR mappings verified", numbered_ok),
        ("lettered WAR mappings verified", lettered_ok),
        ("invalid WAR references", len(invalid_war)),
        ("invalid WFW references", len(invalid_wfw)),
        ("invalid WFE references", len(invalid_wfe)),
        ("invalid WFA references", len(invalid_wfa)),
        ("invalid formula references", len(invalid_formula)),
        ("integration contracts verified", len(rows)),
        ("invalid integration source references", invalid_source),
        ("WFA records checked", len(ident)),
        ("WFA records missing/invalid N/A reasons", bad_na),
        ("documented negative fixtures", len(doc_nf)),
        ("executable negative fixtures", len(NEGATIVE_FIXTURES)),
        ("aligned fixtures", aligned),
        ("misaligned fixtures", len(doc_nf) - aligned),
        ("forward orphans", forward_orphans),
        ("reverse orphans", reverse_orphans),
        ("D-014 checks", d014_checks),
        ("owner-reserved decision checks", owner_reserved),
    ]


def print_report(doc, ctx) -> int:
    print("REPORT — TWENTY-SEVEN SEPARATE TOTALS")
    for name, value in report_metrics(doc, ctx):
        print(f"  {name}: {value}")
    return 0


def main(argv):
    missing = [str(p) for p in INPUTS
               if not p.exists() and not (p in (CATALOGUE_PATH, REGISTRY_PATH)
                                          and "--emit-catalogue" in argv)]
    if missing:
        print("INPUT MISSING:", ", ".join(missing))
        return 2
    doc = read(DOC_PATH)
    docs = {
        "b10": read(B10_PATH),
        "register": read(FORMULA_PATH),
        "reqs": read(REQ_PATH),
        "decisions": read(DECISIONS_PATH),
        "unresolved": read(UNRESOLVED_PATH),
        "autonomy": read(AUTONOMY_PATH),
        "decisions_md": read(DECISIONS_MD_PATH),
        "progress": read(PROGRESS_PATH),
        "b02": read(B02_PATH),
        "b03": read(SUBSYSTEM_DOCS[2]),
        "b04": read(SUBSYSTEM_DOCS[3]),
        "b05": read(SUBSYSTEM_DOCS[4]),
        "b06": read(SUBSYSTEM_DOCS[5]),
        "b07": read(SUBSYSTEM_DOCS[6]),
        "b08": read(SUBSYSTEM_DOCS[7]),
        "b09": read(SUBSYSTEM_DOCS[8]),
        "catalogue": read(CATALOGUE_PATH) if CATALOGUE_PATH.exists() else "",
        "registry": read(REGISTRY_PATH) if REGISTRY_PATH.exists() else "",
        "current": {p.name: read(p) for p in CURRENT_STATUS_DOCS},
        "source": Path(__file__).read_text(encoding="utf-8"),
    }
    ctx = Ctx(doc, docs)
    ctx.registry = CHECKS

    if "--emit-catalogue" in argv:
        registry = build_registry(doc, ctx)
        REGISTRY_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8")
        CATALOGUE_PATH.write_text(build_catalogue(registry), encoding="utf-8")
        print(f"WROTE {REGISTRY_PATH}")
        print(f"WROTE {CATALOGUE_PATH}")
        return 0

    if "--self-test" in argv:
        return self_test(doc, ctx)

    if "--report" in argv:
        return print_report(doc, ctx)

    executed = []
    failures = 0
    for cid, name, func, _mut in CHECKS:
        executed.append(cid)
        errs = func(doc, ctx, cid)
        if errs is None:
            print(f"[{cid}] FAIL {name}: check returned None")
            failures += 1
            continue
        status = "PASS" if not errs else "FAIL"
        print(f"[{cid}] {status} {name} ({ctx.counts.get(cid, 0)} assertions)")
        for e in errs:
            print(f"      - {e}")
        if errs:
            failures += 1

    declared = [c[0] for c in CHECKS]
    if executed != declared:
        print("REGISTRY FAIL: declared checks were not all executed")
        failures += 1
    print()
    print(f"CHECKS: {len(CHECKS)}  EXECUTED: {len(executed)}  FAILED: {failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
