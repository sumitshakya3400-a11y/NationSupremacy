#!/usr/bin/env python3
"""Prompt 12B B-12 specification validator.

Validates the **documentary consistency, traceability and honesty** of the
Stage 2 Prompt 12B deliverable set:

* ``docs/stage-2/20_fair_play_and_player_protection.md``
* ``docs/stage-2/20_fair_play_and_player_protection_formula_register.md``
* ``docs/stage-2/20_fair_play_and_player_protection_requirements.md``
* ``docs/stage-2/20_fair_play_and_player_protection_acceptance.md``
* ``docs/DECISIONS.md`` and ``docs/stage-2/04_approved_and_provisional_decisions.md``
* ``docs/stage-2/03_requirements_traceability.md``
* ``docs/stage-2/05_unresolved_design_decisions.md``
* the three continuity status files and the Stage 2 progress log

**This is a document checker. It is not a security test, privacy audit, legal
opinion, fault-injection run or implementation review.** It proves nothing about
cheat detection, RLS, grants, authentication, moderation tooling, appeal
execution, audit tamper resistance, ledger conservation or legal compliance.
Every control it inspects is a *stated* control. It confirms only that the
specification record exists, is traceable, is internally consistent, preserves
owner-reserved decisions, and does not overstate its own status.

Run from anywhere: paths resolve relative to this file.

    python 12B_validate_b12.py
    python 12B_validate_b12.py --verbose
    python 12B_validate_b12.py --self-test
    python 12B_validate_b12.py --fixtures
    python 12B_validate_b12.py --mutation-audit

Exit code: 0 when every check and fixture passes, 1 when any check or fixture
fails, 2 when a canonical input file is missing. ``--fixtures`` runs the whole
check registry over each isolated mutation, and ``--mutation-audit`` copies
every input file, mutates the copy and runs this validator as a subprocess, so
a rejection is never proven only by a helper-level test.

Documentation QA only. No game code, no dependencies beyond the standard library.
"""

from __future__ import annotations

import argparse
import copy
import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

QA_DIR = Path(__file__).resolve().parent
DOCS = QA_DIR.parent
STAGE2 = DOCS / "stage-2"

RULEBOOK = STAGE2 / "20_fair_play_and_player_protection.md"
FORMULAS = STAGE2 / "20_fair_play_and_player_protection_formula_register.md"
REQUIREMENTS = STAGE2 / "20_fair_play_and_player_protection_requirements.md"
ACCEPTANCE = STAGE2 / "20_fair_play_and_player_protection_acceptance.md"
DECISIONS = DOCS / "DECISIONS.md"
DD_REGISTER = STAGE2 / "04_approved_and_provisional_decisions.md"
UD_REGISTER = STAGE2 / "05_unresolved_design_decisions.md"
REQ_LEDGER = STAGE2 / "03_requirements_traceability.md"
PROGRESS_LOG = STAGE2 / "06_stage_2_progress_log.md"
HANDOFF = STAGE2 / "00_stage_2_handoff.md"
CONTINUITY = [DOCS / "AI_CONTEXT.md", DOCS / "AI_HANDOFF.md",
              DOCS / "PROJECT_PROGRESS.md"]

FILES = {
    "rulebook": RULEBOOK,
    "formulas": FORMULAS,
    "requirements": REQUIREMENTS,
    "acceptance": ACCEPTANCE,
    "decisions": DECISIONS,
    "dd": DD_REGISTER,
    "ud": UD_REGISTER,
    "ledger": REQ_LEDGER,
    "log": PROGRESS_LOG,
    "handoff": HANDOFF,
    "ai_context": DOCS / "AI_CONTEXT.md",
    "ai_handoff": DOCS / "AI_HANDOFF.md",
    "project": DOCS / "PROJECT_PROGRESS.md",
}

PREFIXES = {
    "FP": 35, "EVD": 42, "MA": 12, "CO": 10, "EX": 12, "PRV": 25,
    "MOD": 60, "ADM": 30, "COR": 18, "SEC": 40, "INT": 20, "FR": 15,
    "GOV": 25,
}
RULE_TOTAL = sum(PREFIXES.values())
REQ_FIRST, REQ_LAST = 764, 869
OPEN_REQS = {782, 795, 808, 809, 812, 816, 817, 830, 831, 837,
             842, 843, 844, 846, 849, 855, 857, 867, 868, 869}
FORMULA_IDS = [f"F-FP-{n:03d}" for n in range(1, 17)]
PRIVACY_CLASSES = ["PUB", "PLAYER", "ALLIANCE", "OPS", "MOD",
                   "PERSONAL", "SEC", "AUDIT", "LEGAL"]
ACTORS = ["Player", "Alliance personnel", "Moderator", "Appeals reviewer",
          "Investigator", "Administrator", "Operator/emergency",
          "Audit reviewer"]
ROLES = ["R-MOD", "R-SMOD", "R-APL", "R-INV", "R-SEC", "R-OPS",
         "R-AUD", "R-EMG"]
TIERS = ["T0", "T1", "T2", "T3", "T4", "T5"]
STATUSES = ("PASS", "PARTIAL", "FAIL", "BLOCKED", "NOT RUN", "NOT APPLICABLE")
GATE_TALLY = {"PASS": 23, "PARTIAL": 3, "FAIL": 0, "BLOCKED": 0,
              "NOT RUN": 0, "NOT APPLICABLE": 0}

RULE_RE = re.compile(
    r"^\*\*((?:FP|EVD|MA|CO|EX|PRV|MOD|ADM|COR|SEC|INT|FR|GOV)-(\d{3}))"
    r"\s+—\s+([^*]+?)\.\*\*\s*(.+)$", re.M)

IMPLEMENTATION_CLAIMS = [
    r"\b(?:the|this|a|all|every)\s+[\w-]+(?:\s+[\w-]+){0,4}\s+(?:is|are)\s+"
    r"(?:now\s+)?(?:implemented|deployed|live|running)\b",
    r"\bhas been (?:implemented|deployed|enabled|released)\b",
    r"\bproduction[- ]ready\b",
    r"\bgoes?\s+live\b",
]

LEGAL_CLAIMS = [
    r"\b(?:we are|the project is)\s+(?:GDPR|DSA|COPPA)[- ]compliant\b",
    r"\bcompliant with (?:the )?GDPR\b",
    r"\blegally required (?:of|for) Nation Supremacy\b",
    r"\bbinding on the project\b",
]


# --- helpers ---------------------------------------------------------------

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def cells(line: str) -> list[str]:
    """Split a markdown table line into stripped cells without edge pipes."""
    parts = line.strip().strip("|").split("|")
    return [p.strip() for p in parts]


def section(text: str, start: str, end: str | None = None) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(end, i + len(start)) if end else len(text)
    return text[i:] if j < 0 else text[i:j]


def gaps(ids: list[int]) -> list[str]:
    out = []
    for a, b in zip(ids, ids[1:]):
        if b != a + 1:
            out.append(f"{a}->{b}")
    return out


def strip_ticks(s: str) -> str:
    return s.replace("`", "").strip()


def parse_rule_defs(text: str) -> dict[str, tuple[str, str]]:
    out = {}
    for m in RULE_RE.finditer(text):
        out[m.group(1)] = (m.group(3).strip(), m.group(4).strip())
    return out


def parse_formulas(text: str) -> dict[str, dict[int, str]]:
    out: dict[str, dict[int, str]] = {}
    for block in re.split(r"\n### ", text):
        m = re.match(r"(F-FP-\d{3})\s+—", block)
        if not m:
            continue
        fields = {}
        for fm in re.finditer(r"^(\d{1,2})\. \*\*([^*]+)\.\*\*\s*(.*)$",
                              block, re.M):
            fields[int(fm.group(1))] = fm.group(3).strip()
        out[m.group(1)] = fields
    return out


def parse_gates(text: str) -> dict[str, str]:
    out = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*`?(P12B-\d{2})`?\s*\|", line)
        if m:
            row = cells(line)
            result = row[5] if len(row) > 5 else ""
            toks = [t for t in STATUSES if t in result]
            out[m.group(1)] = toks[0] if toks else "MISSING"
    return out


# --- model -----------------------------------------------------------------

@dataclass
class Model:
    src: dict[str, str] = field(default_factory=dict)
    rules: dict[str, tuple[str, str]] = field(default_factory=dict)
    classes: dict[str, list[str]] = field(default_factory=dict)
    privacy: dict[str, list[str]] = field(default_factory=dict)
    actors: dict[str, list[str]] = field(default_factory=dict)
    roles: dict[str, list[str]] = field(default_factory=dict)
    posts: dict[str, list[str]] = field(default_factory=dict)
    formulas: dict[str, dict[int, str]] = field(default_factory=dict)
    params: dict[str, list[str]] = field(default_factory=dict)
    param_raw: list[str] = field(default_factory=list)
    canonical_defs: list[str] = field(default_factory=list)
    canonical_problems: list[str] = field(default_factory=list)
    def_records: list[dict] = field(default_factory=list)
    req1: dict[int, list[str]] = field(default_factory=dict)
    req2: dict[int, list[str]] = field(default_factory=dict)
    d_rows: dict[int, list[str]] = field(default_factory=dict)
    dd_rows: dict[int, list[str]] = field(default_factory=dict)
    ud_rows: dict[int, list[str]] = field(default_factory=dict)
    gates: dict[str, str] = field(default_factory=dict)
    int_fields: dict[str, list[str]] = field(default_factory=dict)
    dep_trace: dict[str, list[str]] = field(default_factory=dict)
    sys_map: dict[str, list[str]] = field(default_factory=dict)

    def rebuild(self) -> None:
        r = self.src.get("rulebook", "")
        f = self.src.get("formulas", "")
        q = self.src.get("requirements", "")
        a = self.src.get("acceptance", "")
        d = self.src.get("decisions", "")
        dd = self.src.get("dd", "")
        u = self.src.get("ud", "")

        self.rules = parse_rule_defs(r)
        self.classes = {}
        annex_a = section(r, "## Annex A", "## Annex B")
        for line in annex_a.splitlines():
            m = re.match(r"^\|\s*`(V-\d{2})`\s*\|", line)
            if m:
                self.classes[m.group(1)] = cells(line)
        self.privacy = {}
        annex_b = section(r, "## Annex B", "## Annex C")
        for line in annex_b.splitlines():
            m = re.match(r"^\|\s*`([A-Z]+)`\s*\|", line)
            if m and m.group(1) in PRIVACY_CLASSES:
                self.privacy[m.group(1)] = cells(line)
        self.actors = {}
        matrix = section(annex_b, "**Actor/action matrix", "No actor holds")
        actor_rows = []
        for line in matrix.splitlines():
            if not line.strip().startswith("|"):
                continue
            row = cells(line)
            if not row or row[0] in ("Actor", "") or set(row[0]) <= {"-", ":"}:
                continue
            actor_rows.append(row)
        for row in actor_rows:
            self.actors[row[0]] = row
        self.actor_row_count = len(actor_rows)
        self.roles = {}
        annex_c = section(r, "## Annex C", "## Annex D")
        for line in annex_c.splitlines():
            m = re.match(r"^\|\s*`(R-[A-Z]+)`\s*\|", line)
            if m:
                self.roles[m.group(1)] = cells(line)
        self.posts = {}
        annex_d = section(r, "## Annex D", "## Annex E")
        for line in annex_d.splitlines():
            m = re.match(r"^\|\s*`(FR-\d{2})`\s*\|", line)
            if m:
                self.posts[m.group(1)] = cells(line)

        self.formulas = parse_formulas(f)
        self.params = {}
        self.param_raw = []
        # Canonical definitions are discovered across every block kind inside
        # the parameter-register region — table rows, headings, list items,
        # definition lists and ordinary prose — by canonical_definitions(). A
        # heading line is never discarded before its content is inspected, and
        # an explanatory mention is not mistaken for a definition record.
        if f:
            ordered, def_problems, records = canonical_definitions(f)
        else:
            ordered, def_problems, records = [], [], []
        self.canonical_defs = ordered
        self.canonical_problems = def_problems
        self.def_records = records
        for rec in records:
            if rec["boundary"] != "canonical region":
                continue
            self.param_raw.append(rec["token"])
            tok = rec["token"]
            if CANONICAL_PARAM_ID_RE.fullmatch(tok):
                if rec["kind"] == "table-row":
                    self.params.setdefault(
                        tok, [c.strip() for c in
                              rec["text"].strip().strip("|").split("|")])
                else:
                    self.params.setdefault(tok, [rec["text"]])

        p1 = section(q, "## 2. Requirement records", "## 3. Requirement records")
        p2 = section(q, "## 3. Requirement records", "## 4. Totals")
        self.req1, self.req2 = {}, {}
        for region, target in ((p1, self.req1), (p2, self.req2)):
            for line in region.splitlines():
                m = re.match(r"^\|\s*(REQ-(\d{3}))\s*\|", line)
                if m:
                    target[int(m.group(2))] = cells(line)

        self.d_rows = {}
        for line in d.splitlines():
            m = re.match(r"^\|\s*(D-\d{3})\s*\|", line)
            if m:
                self.d_rows[int(m.group(1).split("-")[1])] = cells(line)
        self.dd_rows = {}
        for line in dd.splitlines():
            m = re.match(r"^\|\s*`?(DD-\d{3})`?\s*\|", line)
            if m:
                self.dd_rows[int(m.group(1).split("-")[1])] = cells(line)
        self.ud_rows = {}
        for line in u.splitlines():
            m = re.match(r"^\|\s*(UD-\d{3})\s*\|", line)
            if m:
                self.ud_rows[int(m.group(1).split("-")[1])] = cells(line)

        self.gates = parse_gates(section(a, "## 2. Gate register", "### 2.1"))

        self.int_fields = {}
        sec161 = section(r, "### 16.1 Integration dependency fields", "## 17.")
        for line in sec161.splitlines():
            mt = re.match(r"^\|\s*`(INT-\d{3})`\s*\|", line)
            if mt:
                self.int_fields[mt.group(1)] = cells(line)
        self.dep_trace = {}
        sec52 = section(a, "### 5.2 Consolidated dependency traceability", "## 6.")
        for line in sec52.splitlines():
            mt = re.match(r"^\|\s*`(INT-\d{3})`\s*\|", line)
            if mt:
                self.dep_trace[mt.group(1)] = cells(line)
        self.sys_map = {}
        sec51 = section(a, "### 5.1 Canonical system-to-contract mapping", "### 5.2")
        for line in sec51.splitlines():
            if not line.strip().startswith("|"):
                continue
            row = cells(line)
            if row and row[0] not in ("System", "") and not set(row[0]) <= {"-", ":"}:
                self.sys_map[row[0]] = row


def load() -> Model:
    m = Model()
    for key, path in FILES.items():
        m.src[key] = read(path) if path.exists() else ""
    m.rebuild()
    return m


# --- checks ----------------------------------------------------------------

def check_01(m: Model) -> tuple[bool, str]:
    """Every canonical B-12 document and register exists."""
    missing = [p.name for p in FILES.values() if not p.exists()]
    return (not missing,
            "all canonical inputs present" if not missing else f"missing: {missing}")


def check_02(m: Model) -> tuple[bool, str]:
    """Each B-12 document carries version, date, status and a non-claim."""
    problems = []
    for key in ("rulebook", "formulas", "requirements", "acceptance"):
        text = m.src.get(key, "")
        for token in ("**Version:** 1.0", "2026-11-07", "**Status:**"):
            if token not in text:
                problems.append(f"{key} missing {token}")
        low = text.lower()
        if not any(p in low for p in ("unimplemented", "not implemented",
                                      "none is implemented", "documentation level")):
            problems.append(f"{key} has no honest status phrase")
    return (not problems, "headers and non-claims present" if not problems
            else "; ".join(problems))


def check_03(m: Model) -> tuple[bool, str]:
    """The rule inventory parses to exactly 344 normative definitions."""
    n = len(m.rules)
    return n == RULE_TOTAL, f"{n} rule definitions parsed (expected {RULE_TOTAL})"


def check_04(m: Model) -> tuple[bool, str]:
    """Each rule prefix is contiguous, unique and equal to its declared count."""
    problems = []
    raw = [mt.group(1) for mt in RULE_RE.finditer(m.src.get("rulebook", ""))]
    dup = len(raw) - len(set(raw))
    if dup:
        problems.append(f"{dup} duplicate rule definitions")
    for prefix, expected in PREFIXES.items():
        nums = sorted(int(k.split("-")[1]) for k in m.rules if k.startswith(prefix + "-"))
        if len(nums) != expected:
            problems.append(f"{prefix}={len(nums)}/{expected}")
        if nums and nums[0] != 1:
            problems.append(f"{prefix} starts at {nums[0]}")
        bad = gaps(nums)
        if bad:
            problems.append(f"{prefix} gaps {bad[:3]}")
    return (not problems, f"{RULE_TOTAL} rules across 13 prefixes are contiguous"
            if not problems else "; ".join(problems))


def check_05(m: Model) -> tuple[bool, str]:
    """Every rule has a non-trivial title and a body."""
    bad = [k for k, (t, b) in m.rules.items() if len(t) < 3 or len(b) < 20]
    return not bad, ("every rule has a title and body" if not bad
                     else f"thin or empty rules: {bad[:8]}")


def check_06(m: Model) -> tuple[bool, str]:
    """Exactly sixteen violation classes exist."""
    ids = sorted(m.classes)
    ok = ids == [f"V-{n:02d}" for n in range(1, 17)]
    return ok, f"{len(ids)} violation classes {ids[0] if ids else '-'}…{ids[-1] if ids else '-'}"


def check_07(m: Model) -> tuple[bool, str]:
    """Each violation class carries the eleven normative elements."""
    bad = [k for k, c in m.classes.items()
           if len(c) != 13 or any(not x for x in c[1:])]
    return not bad, ("all 16 classes carry 11 populated elements" if not bad
                     else f"incomplete classes: {bad}")


def check_08(m: Model) -> tuple[bool, str]:
    """No seventeenth violation class is defined or referenced."""
    bad = sorted(set(re.findall(r"\bV-(\d{2})\b", m.src.get("rulebook", "")))
                 - {f"{n:02d}" for n in range(1, 17)})
    return not bad, ("no class beyond V-16" if not bad else f"stray classes: {bad}")


def check_09(m: Model) -> tuple[bool, str]:
    """A charge must name the class; a catch-all is prohibited."""
    body = m.rules.get("FP-021", ("", ""))[1]
    ok = "`V-` class" in body and "catch-all" in m.rules.get("FP-021", ("", ""))[0].lower()
    return ok, "FP-021 requires a named class and forbids a catch-all"


def check_10(m: Model) -> tuple[bool, str]:
    """Exactly five evidence states exist."""
    body = m.rules.get("EVD-001", ("", ""))[1]
    ok = all(tok in body for tok in ("E0", "E1", "E2", "E3", "EX")) \
        and "Exactly five states exist" in body
    extra = re.findall(r"\bE[4-9]\b", m.src.get("rulebook", ""))
    return ok and not extra, "five states only: E0, E1, E2, E3, EX"


def check_11(m: Model) -> tuple[bool, str]:
    """The consequence ceiling per evidence state is explicit."""
    body = m.rules.get("EVD-002", ("", ""))[1]
    ok = "E3" in body and "E2" in body and "EX" in body and "MUST NOT" not in body
    return ok, "EVD-002 states the maximum consequence per state"


def check_12(m: Model) -> tuple[bool, str]:
    """Automated rules may never create a finding or permanent measure."""
    body = m.rules.get("EVD-003", ("", ""))[1]
    ok = "MUST NOT create" in body and "E3" in body
    return ok, "automated ceiling present"


def check_13(m: Model) -> tuple[bool, str]:
    """Behavioural evidence alone is never a violation."""
    body = m.rules.get("EVD-004", ("", ""))[1]
    ok = "MUST NOT be treated as a violation" in body and "independent non-behavioural" in body
    return ok, "EVD-004 forbids behaviour-only findings"


def check_14(m: Model) -> tuple[bool, str]:
    """Network evidence cannot support a sanction above the lowest tier."""
    body = m.rules.get("EVD-005", ("", ""))[1]
    ok = "never support a sanction above the lowest" in body and "IP address" in body
    return ok, "EVD-005 demotes network evidence"


def check_15(m: Model) -> tuple[bool, str]:
    """No universal confidence score is permitted."""
    text = m.src.get("rulebook", "")
    ok = "No universal confidence formula" in text \
        and not re.search(r"\b(?:a|the) (?:composite|universal) (?:risk |confidence )?score (?:is|of)\b",
                          text, re.I)
    return ok, "no universal confidence score"


def check_16(m: Model) -> tuple[bool, str]:
    """Nine privacy classes are defined."""
    ok = sorted(m.privacy) == sorted(PRIVACY_CLASSES)
    return ok, f"{len(m.privacy)} privacy classes"


def check_17(m: Model) -> tuple[bool, str]:
    """Eight actor classes appear in the permission matrix."""
    ok = list(m.actors) == ACTORS and m.actor_row_count == 8
    return ok, f"{m.actor_row_count} actor classes"


def check_18(m: Model) -> tuple[bool, str]:
    """Six actions are declared for the actor matrix."""
    text = m.src.get("rulebook", "")
    ok = "`V` view, `S` search, `X` export, `M` modify, `D` delete, `Dc` disclose" in text
    return ok, "six actions declared"


def check_19(m: Model) -> tuple[bool, str]:
    """Exactly eight administrative roles exist."""
    ok = sorted(m.roles) == sorted(ROLES)
    return ok, f"{len(m.roles)} roles"


def check_20(m: Model) -> tuple[bool, str]:
    """Every role row carries all eleven role fields."""
    bad = [k for k, c in m.roles.items() if len(c) != 12 or any(not x for x in c)]
    return not bad, ("all eight roles carry 11 populated fields" if not bad
                     else f"incomplete roles: {bad}")


def check_21(m: Model) -> tuple[bool, str]:
    """The administrative prohibition list is substantive."""
    body = m.rules.get("ADM-001", ("", ""))[1]
    ok = "treasury" in body and body.count(";") >= 4 and "delete or edit an audit record" in body
    return ok, "ADM-001 prohibition list present"


def check_22(m: Model) -> tuple[bool, str]:
    """No superuser or inherited all-permission role exists."""
    text = m.src.get("rulebook", "")
    ok = 'There is no "see everything"' in text and "individually granted" in text
    return ok, "no superuser role"


def check_23(m: Model) -> tuple[bool, str]:
    """Exactly six sanction tiers exist."""
    body = m.rules.get("MOD-036", ("", ""))[1]
    ok = all(t in body for t in TIERS) and "T6" not in body
    return ok, "six tiers T0…T5 only"


def check_24(m: Model) -> tuple[bool, str]:
    """Every tier states its minimum evidence."""
    body = m.rules.get("MOD-038", ("", ""))[1]
    ok = all(t in body for t in ("T0", "T1", "T2", "T3", "T5")) and "E3" in body
    return ok, "MOD-038 states evidence per tier"


def check_25(m: Model) -> tuple[bool, str]:
    """Exactly four appeal outcomes exist."""
    body = m.rules.get("MOD-045", ("", ""))[1]
    ok = all(t in body for t in ("UPHELD", "REDUCED", "REVERSED", "REMANDED")) \
        and "EXPUNGED" not in body
    return ok, "four appeal outcomes"


def check_26(m: Model) -> tuple[bool, str]:
    """An unsegregated appeal is labelled, not claimed independent."""
    body = m.rules.get("MOD-049", ("", ""))[1]
    ok = "not independent" in body and "does not claim more" in body
    return ok, "MOD-049 labels the independence gap"


def check_27(m: Model) -> tuple[bool, str]:
    """Exactly six correction transaction types exist."""
    body = m.rules.get("COR-001", ("", ""))[1]
    ok = all(t in body for t in ("ORIGINAL", "CORRECTION", "REVERSAL",
                                 "COMPENSATION", "ILLICIT_REMOVAL",
                                 "ADMIN_ADJUSTMENT")) \
        and "No seventh type" in body
    return ok, ("six correction transaction types" if ok
                else "missing a type or a seventh correction type is permitted")


def check_28(m: Model) -> tuple[bool, str]:
    """The conservation identity is specified with a signed convention."""
    fields = m.formulas.get("F-FP-014", {})
    text = " ".join(fields.values())
    ok = "Z = O + L + C + R + P + X + A" in text and "signed" in text.lower()
    return ok, "F-FP-014 signed conservation identity present"


def check_29(m: Model) -> tuple[bool, str]:
    """Correction and sanction are separate classes."""
    body = m.rules.get("MOD-055", ("", ""))[1]
    ok = "does not imply a conduct finding" in body and "separately" in body
    return ok, "MOD-055 separates correction and sanction"


def check_30(m: Model) -> tuple[bool, str]:
    """Chain-of-custody events are specified."""
    custody = m.rules.get("EVD-022", ("", ""))[1]
    provenance = m.rules.get("EVD-036", ("", ""))[1]
    ok = "audit event" in custody and "producer" in provenance
    return ok, "custody and provenance rules present"


def check_31(m: Model) -> tuple[bool, str]:
    """Retention, redaction and minimisation are specified."""
    retention = m.rules.get("PRV-023", ("", ""))[1]
    redaction = m.rules.get("EVD-038", ("", ""))[1]
    minimisation = m.rules.get("EVD-024", ("", ""))[1]
    ok = "per class" in retention and "preserves a record" in redaction \
        and "minimised" in minimisation
    return ok, "retention, redaction and minimisation present"


def check_32(m: Model) -> tuple[bool, str]:
    """The digest-chain construction is specified."""
    fields = m.formulas.get("F-FP-012", {})
    text = " ".join(fields.values())
    ok = "SHA-256" in text and "h_{i" in text and "genesis" in text
    return ok, "F-FP-012 specifies the digest chain"


def check_33(m: Model) -> tuple[bool, str]:
    """The verification interval is specified and not claimed to run."""
    text = " ".join(m.formulas.get("F-FP-013", {}).values())
    ok = "I_v" in text and ("no job runs" in text or "not running" in text
                            or "must not exceed" in text)
    return ok, "F-FP-013 is an interval, not a running job"


def check_34(m: Model) -> tuple[bool, str]:
    """Server authority is stated."""
    body = m.rules.get("FP-011", ("", ""))[1]
    ok = "server-side" in body and "client-supplied" in body
    return ok, "FP-011 server authority"


def check_35(m: Model) -> tuple[bool, str]:
    """Single-writer ownership is stated."""
    body = m.rules.get("FP-012", ("", ""))[1]
    ok = "exactly one owning subsystem" in body and "in place" in body
    return ok, "FP-012 single writer"


def check_36(m: Model) -> tuple[bool, str]:
    """Idempotency and rate limits key to account and resource."""
    idem = m.rules.get("SEC-003", ("", ""))[1]
    rate = m.rules.get("SEC-007", ("", ""))[1]
    ok = "idempotency-keyed" in idem and "authenticated account" in rate
    return ok, "idempotency and rate rules present"


def check_37(m: Model) -> tuple[bool, str]:
    """Known prototype privilege and audit defects are disclosed."""
    text = m.src.get("rulebook", "")
    ok = all(k in text for k in ("table-wide", "treasury", "0005", "protective trigger"))
    return ok, "prototype defect disclosure present"


def check_38(m: Model) -> tuple[bool, str]:
    """No claim that tamper-evident protection exists."""
    text = m.src.get("rulebook", "")
    bad = re.search(r"\btamper-evident (?:protection|audit) (?:is|has been) "
                    r"(?:implemented|running|verified|operating)\b", text, re.I)
    ok = ("not implemented" in text or "Unimplemented" in text) \
        and "not running" in text and not bad
    return ok, "tamper-evidence is an obligation, not a claim"


def check_39(m: Model) -> tuple[bool, str]:
    """Twenty cross-system contracts exist."""
    n = len([k for k in m.rules if k.startswith("INT-")])
    return n == 20, f"{n} INT contracts"


def check_40(m: Model) -> tuple[bool, str]:
    """Each INT contract names an owner relationship and a non-claim."""
    bad = [k for k, (t, b) in m.rules.items()
           if k.startswith("INT-") and len(b) < 40]
    return not bad, ("20 contracts populated" if not bad else f"thin contracts: {bad}")


def check_41(m: Model) -> tuple[bool, str]:
    """B-12 owns no gameplay value or outcome."""
    body = m.rules.get("FP-004", ("", ""))[1]
    ok = "owns no gameplay value" in body and "never writes another subsystem" in body
    return ok, "FP-004 boundary present"


def check_42(m: Model) -> tuple[bool, str]:
    """Sixteen formulas are defined with the expected identifiers."""
    ok = sorted(m.formulas) == FORMULA_IDS
    return ok, f"{len(m.formulas)} formulas defined"


def check_43(m: Model) -> tuple[bool, str]:
    """Every formula carries all twenty mandatory fields."""
    bad = []
    for fid, fields in m.formulas.items():
        missing = [n for n in range(1, 21) if n not in fields]
        if missing:
            bad.append(f"{fid}:{missing}")
    return not bad, ("all 16 formulas carry fields 1–20" if not bad
                     else f"missing fields: {bad[:4]}")


def check_44(m: Model) -> tuple[bool, str]:
    """Six value classifications are declared."""
    text = m.src.get("formulas", "")
    needed = ("Structural", "Structural + provisional parameter", "Provisional",
              "Owner decision required", "Legal review required",
              "Capacity validation required")
    ok = all(x in text for x in needed)
    return ok, "six value classes declared"


def check_45(m: Model) -> tuple[bool, str]:
    """Parameter count is source-derived from the canonical register; none calibrated."""
    ordered, problems = canonical_params(m)
    if problems:
        return False, "; ".join(problems)
    expected_count = len(ordered)
    text = m.src.get("formulas", "")
    decl = re.search(r"\*\*Parameters:\s*(\d+)\*\*", text)
    if decl and int(decl.group(1)) != expected_count:
        return False, (f"register declares {decl.group(1)} parameters but defines "
                       f"{expected_count}")
    bad = re.search(r"\b(?:all|every) (?:parameter|value)s? (?:is|are) "
                    r"(?:approved|calibrated|validated)\b", text, re.I)
    if bad:
        return False, "a parameter is claimed calibrated/approved"
    return True, f"{expected_count} parameters (source-derived), none calibrated"


def check_46(m: Model) -> tuple[bool, str]:
    """Every formula declares its variables and leaves no term undefined."""
    problems = []
    for fid, fields in m.formulas.items():
        variables = fields.get(5, "")
        if not variables.strip():
            problems.append(f"{fid}:no variables")
        block = " ".join(fields.values())
        if re.search(r"\b(?:TBD|TODO|undefined variable|not defined)\b", block, re.I):
            problems.append(f"{fid}:undefined")
    return not problems, ("every formula declares its variables" if not problems
                          else f"problems: {problems[:5]}")


def check_47(m: Model) -> tuple[bool, str]:
    """Exactly 106 requirement rows exist, each once, in both halves."""
    q = m.src.get("requirements", "")
    p1 = section(q, "## 2. Requirement records", "## 3. Requirement records")
    p2 = section(q, "## 3. Requirement records", "## 4. Totals")
    raw1 = re.findall(r"^\| (REQ-\d{3}) \|", p1, re.M)
    raw2 = re.findall(r"^\| (REQ-\d{3}) \|", p2, re.M)
    ok = len(raw1) == 106 and len(raw2) == 106 \
        and len(set(raw1)) == 106 and len(set(raw2)) == 106 \
        and sorted(m.req1) == sorted(m.req2)
    return ok, f"part1={len(raw1)}, part2={len(raw2)}"


def check_48(m: Model) -> tuple[bool, str]:
    """Requirement identifiers are contiguous REQ-764…REQ-869."""
    ids = sorted(m.req1)
    ok = ids and ids[0] == REQ_FIRST and ids[-1] == REQ_LAST and not gaps(ids)
    return ok, f"{len(ids)} requirements {ids[0] if ids else '-'}…{ids[-1] if ids else '-'}"


def check_49(m: Model) -> tuple[bool, str]:
    """Each requirement is paired in order with its 12A candidate."""
    bad = []
    for i, rid in enumerate(sorted(m.req1)):
        row = m.req1[rid]
        authority = row[5] if len(row) > 5 else ""
        if f"12A-CR-{i + 1:03d}" not in authority:
            bad.append(f"REQ-{rid}")
    return not bad, ("106 candidates pair one-to-one" if not bad
                     else f"broken pairing: {bad[:5]}")


def check_50(m: Model) -> tuple[bool, str]:
    """Requirement statuses reconcile to 86 Provisional and 20 Open."""
    provisional = open_ = approved = 0
    for rid, row in m.req1.items():
        status = row[4].replace("*", "").strip() if len(row) > 4 else ""
        if status == "Provisional":
            provisional += 1
        elif status == "Open":
            open_ += 1
        elif status == "Approved":
            approved += 1
    ok = (provisional, open_, approved) == (86, 20, 0)
    return ok, f"Provisional={provisional}, Open={open_}, Approved={approved}"


def check_51(m: Model) -> tuple[bool, str]:
    """The Open set equals the twenty declared owner/legal rows."""
    actual = {rid for rid, row in m.req1.items()
              if len(row) > 4 and row[4].replace("*", "").strip() == "Open"}
    ok = actual == OPEN_REQS
    return ok, (f"Open rows match ({len(actual)})" if ok
                else f"missing={sorted(OPEN_REQS - actual)} extra={sorted(actual - OPEN_REQS)}")


def check_52(m: Model) -> tuple[bool, str]:
    """Every UD reference in the requirement register resolves."""
    text = m.src.get("requirements", "")
    refs = {int(x) for x in re.findall(r"UD-(\d{3})", text)}
    missing = sorted(refs - set(m.ud_rows))
    return not missing, (f"{len(refs)} UD references resolve" if not missing
                         else f"unresolved UD: {missing}")


def check_53(m: Model) -> tuple[bool, str]:
    """Ten B-12 decisions D-178…D-187 are recorded."""
    missing = [n for n in range(178, 188) if n not in m.d_rows]
    thin = [n for n in range(178, 188)
            if n in m.d_rows and len(m.d_rows[n]) < 8]
    return not missing and not thin, (f"10 decisions recorded" if not missing and not thin
                                      else f"missing={missing} thin={thin}")


def check_54(m: Model) -> tuple[bool, str]:
    """Ten mirrored DD rows DD-226…DD-235 cite their D counterparts."""
    bad = []
    for i, n in enumerate(range(226, 236)):
        if n not in m.dd_rows:
            bad.append(f"DD-{n} missing")
        elif f"D-{178 + i}" not in " ".join(m.dd_rows[n]):
            bad.append(f"DD-{n} does not cite D-{178 + i}")
    return not bad, ("10 mirrored rows present" if not bad else "; ".join(bad))


def check_55(m: Model) -> tuple[bool, str]:
    """The continuity files name 12B and the next prompt 12C."""
    problems = []
    for key in ("handoff", "ai_context", "ai_handoff", "project"):
        text = m.src.get(key, "")
        if "12C" not in text:
            problems.append(f"{key} does not name 12C")
        if "12B" not in text:
            problems.append(f"{key} does not name 12B")
    return not problems, ("continuity names 12B and 12C" if not problems
                          else "; ".join(problems))


def check_56(m: Model) -> tuple[bool, str]:
    """Progress-log §75 records the Prompt 12B pass."""
    text = m.src.get("log", "")
    ok = re.search(r"^## 75\. .*12B", text, re.M) is not None
    return ok, "progress log §75 present"


def check_57(m: Model) -> tuple[bool, str]:
    """No Prompt 12C journey or workflow-library section exists."""
    bad = []
    for key in ("rulebook", "formulas", "requirements", "acceptance"):
        for line in m.src.get(key, "").splitlines():
            if re.match(r"^#{1,3} .*(player journey|workflow library|operational sequence)", line, re.I):
                bad.append(f"{key}: {line.strip()[:50]}")
    return not bad, ("no 12C deliverable section" if not bad
                     else f"12C section present: {bad[:3]}")


def check_58(m: Model) -> tuple[bool, str]:
    """The 12C handoff states that 12C is not started and not authorized."""
    text = m.src.get("rulebook", "")
    ok = "not started and not authorized" in text or "not started and is not authorized" in text
    return ok, "12C boundary stated"


def affirmative(text: str, pattern: str) -> str | None:
    """Return the first positive claim, ignoring one preceded by a negation."""
    for mt in re.finditer(pattern, text, re.I):
        before = text[max(0, mt.start() - 60):mt.start()].lower()
        if re.search(r"\b(?:no|not|none|never|neither|without)\b", before):
            continue
        return mt.group(0)
    return None


def check_59(m: Model) -> tuple[bool, str]:
    """No B-12 document claims an implemented or deployed control."""
    problems = []
    for key in ("rulebook", "formulas", "requirements", "acceptance"):
        for pat in IMPLEMENTATION_CLAIMS:
            hit = affirmative(m.src.get(key, ""), pat)
            if hit:
                problems.append(f"{key}: {hit[:60]}")
                break
    return not problems, ("no implementation claim" if not problems
                          else "; ".join(problems))


def check_60(m: Model) -> tuple[bool, str]:
    """No legal-compliance or binding-obligation claim is made."""
    problems = []
    for key in ("rulebook", "formulas", "requirements", "acceptance"):
        for pat in LEGAL_CLAIMS:
            hit = affirmative(m.src.get(key, ""), pat)
            if hit:
                problems.append(f"{key}: {hit[:60]}")
                break
    return not problems, ("no legal-compliance claim" if not problems
                          else "; ".join(problems))


def check_61(m: Model) -> tuple[bool, str]:
    """Gate register: 26 well-formed, unique gates with legal statuses."""
    a = m.src.get("acceptance", "")
    gate_section = section(a, "## 2. Gate register", "### 2.1")
    malformed, raw_ids = [], []
    for ln in gate_section.splitlines():
        if not ln.strip().startswith("|"):
            continue
        row = cells(ln)
        if not row:
            continue
        first = row[0].strip().strip("`")
        if first.startswith("P12B-"):
            if re.fullmatch(r"P12B-\d{2}", first):
                raw_ids.append(first)
            else:
                malformed.append(first)
    ids = sorted(m.gates)
    expected = [f"P12B-{n:02d}" for n in range(1, 27)]
    bad = [g for g, s in m.gates.items() if s not in STATUSES]
    problems = []
    if ids != expected:
        problems.append(f"gates={len(ids)} expected 26")
    if bad:
        problems.append(f"bad-status={bad[:4]}")
    if malformed:
        problems.append("malformed gate identifier(s): " + ", ".join(malformed))
    if len(raw_ids) != len(set(raw_ids)):
        problems.append("duplicate gate identifier rows")
    return not problems, (f"{len(ids)} gates" if not problems
                          else "; ".join(problems))


def check_62(m: Model) -> tuple[bool, str]:
    """The declared gate tally equals the parsed result column."""
    counts = {s: 0 for s in STATUSES}
    for s in m.gates.values():
        if s in counts:
            counts[s] += 1
    ok = counts == GATE_TALLY
    text = m.src.get("acceptance", "")
    declared = ("23 `PASS` · 3 `PARTIAL` · 0 `FAIL` · 0 `BLOCKED` · "
                "0 `NOT RUN` · 0 `NOT APPLICABLE`") in text
    detail = (f"PASS={counts['PASS']} PARTIAL={counts['PARTIAL']} "
              f"FAIL={counts['FAIL']}")
    if not declared:
        detail += "; declared tally does not match"
    return ok and declared, detail


PROMPT_ARCHIVE = DOCS / "prompts" / "prompt_12B_complete_system_specifications.md"
PROMPT_INDEX = DOCS / "prompts" / "INDEX.md"
POLICY = DOCS / "AUTONOMOUS_DECISION_POLICY.md"
# The authoritative parameter collection is extracted dynamically from the
# canonical formula register (see canonical_params); no hard-coded production
# expectation is maintained here.

# Files Prompt 12B-C1-R1 actually changed; its §77.1 manifest must list them.
R1_MANIFEST_REQUIRED = [
    "docs/stage-2/20_fair_play_and_player_protection_acceptance.md",
    "docs/AI_CONTEXT.md",
    "docs/stage-2/06_stage_2_progress_log.md",
    "docs/qa_backups/12B_validate_b12.py",
    "docs/prompts/INDEX.md",
    "docs/prompts/prompt_12B-C1_formula_corrections_and_closeout.md",
    "docs/prompts/prompt_12B-C1-R1_final_documentation_synchronization.md",
    "docs/stage-2/01_stage_2_prompt_roadmap.md",
]

# Parameter identifiers may be formatted (`FP-P01`) or unformatted (FP-P01),
# bolded, or split across a wrapped line; ranges may use a hyphen, en dash, em
# dash, tilde, ellipsis or the word "to". Scanning is occurrence-based and never
# converts to a set before duplicate detection.
PARAM_RANGE_TOKEN_RE = re.compile(
    r"`?FP-P(\d{2})`?\s*(?:[-–—…~]|\s+to\s+)\s*`?FP-P(\d{2})`?")
# Maximal-munch candidate scan. Whitespace between "FP-" and "P" is tolerated so
# a token broken by a line wrap is still discovered, and the trailing class is
# greedy so a valid prefix can never be cut out of a larger malformed token.
PARAM_CANDIDATE_RE = re.compile(r"FP-[ \t]*P[A-Za-z0-9_.\-]*")
PARAM_NAMESPACE_RE = re.compile(r"FP-[ \t]*P")
CANONICAL_PARAM_ID_RE = re.compile(r"FP-P\d{2}")


# --- structural document model (R7) ----------------------------------------

@dataclass
class Block:
    """One logical document unit with its source location.

    Kinds: heading, table-row, list-item, key-entry, paragraph, blockquote,
    code. Continuation lines belong to the block they continue.
    """

    kind: str
    section: str
    text: str
    start_line: int
    end_line: int


@dataclass
class Occurrence:
    """One FP-P namespace token retained before any deduplication."""

    order: int = 0
    source: str = ""
    section: str = ""
    line: int = 0
    offset: int = 0
    end: int = 0
    raw: str = ""
    ident: str | None = None
    form: str = "standalone"
    statement: str = ""
    context: str = ""
    classification: str = "unclassified"
    outcome: str = "pending"


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LIST_ITEM_RE = re.compile(r"^(?:[-*+]\s+|\d{1,3}[.)]\s+)(.*)$")
KEY_ENTRY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*[ \t]*:[ \t]+\S")
HR_LINE_RE = re.compile(r"^(?:-{3,}|\*{3,}|_{3,})$")
HTML_LINE_RE = re.compile(r"^<!--.*-->$|^</?[a-zA-Z][^>]*>$")
TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|?$")
STRUCTURAL_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.;])\s+|\s*\|\s*|\n+")
# Characters that decorate a token without being part of it. A leading position
# is measured after these, so formatting can never hide a definition or an
# occurrence from the scanner.
LEADING_MARKERS = " \t`*_>#"


def leading_index(text: str) -> int:
    """Offset of the first content character of a block or statement."""
    return len(text) - len(text.lstrip(LEADING_MARKERS))


def after_token(text: str, offset: int, raw: str) -> str:
    """The text that follows a token, ignoring its closing markers."""
    return text[offset + len(raw):].lstrip(LEADING_MARKERS)


def iter_blocks(text: str) -> list[Block]:
    """Parse a markdown document into complete logical blocks.

    Every line is assigned to a block; no line kind is discarded. Headings are
    blocks in their own right (R7 defect 4: heading lines were skipped), table
    rows keep row identity, and indented or wrapped lines join the block they
    continue so an assertion split across physical lines stays one statement.
    """
    lines = text.splitlines()
    blocks: list[Block] = []
    headings: list[str] = []
    i, n = 0, len(lines)

    def emit(kind: str, parts: list[str], start: int, end: int) -> None:
        joined = " ".join(p.strip() for p in parts).strip()
        if joined:
            blocks.append(Block(kind, " > ".join(h for h in headings if h),
                                joined, start, end))

    def is_break(raw_line: str) -> bool:
        s = raw_line.strip()
        return (not s or bool(HEADING_RE.match(s)) or s.startswith(("|", ">", "```"))
                or bool(HR_LINE_RE.match(s)) or bool(HTML_LINE_RE.match(s))
                or bool(LIST_ITEM_RE.match(s)))

    while i < n:
        raw = lines[i]
        st = raw.strip()
        if not st or HR_LINE_RE.match(st) or HTML_LINE_RE.match(st):
            i += 1
            continue
        hm = HEADING_RE.match(st)
        if hm:
            level, title = len(hm.group(1)), hm.group(2)
            del headings[level:]
            while len(headings) < level:
                headings.append("")
            headings[level - 1] = title
            blocks.append(Block("heading", " > ".join(h for h in headings if h),
                                st, i + 1, i + 1))
            i += 1
            continue
        if st.startswith("```"):
            start, i = i, i + 1
            buf: list[str] = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            emit("code", buf, start + 1, i)
            continue
        if st.startswith("|"):
            if not TABLE_SEP_RE.match(st):
                blocks.append(Block("table-row",
                                    " > ".join(h for h in headings if h),
                                    st, i + 1, i + 1))
            i += 1
            continue
        if st.startswith(">"):
            start, buf = i, []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            emit("blockquote", buf, start + 1, i)
            continue
        if LIST_ITEM_RE.match(st):
            start, buf = i, [st]
            i += 1
            while i < n and lines[i].startswith((" ", "\t")) and lines[i].strip():
                buf.append(lines[i])
                i += 1
            emit("list-item", buf, start + 1, i)
            continue
        kind = "key-entry" if KEY_ENTRY_RE.match(raw) else "paragraph"
        start, buf = i, [st]
        i += 1
        while i < n:
            nxt = lines[i]
            if is_break(nxt):
                break
            # an unindented "key:" line starts a new record; an indented one is
            # a continuation of the current entry.
            if kind == "key-entry" and KEY_ENTRY_RE.match(nxt) \
                    and not nxt.startswith((" ", "\t")):
                break
            buf.append(nxt.strip())
            i += 1
        emit(kind, buf, start + 1, i)
    return blocks


def split_statements(text: str) -> list[str]:
    """Split a block into sentence/table-cell units for semantic reading."""
    parts = [p.strip() for p in STRUCTURAL_SENTENCE_SPLIT_RE.split(text)]
    return [p for p in parts if p]


def scan_occurrences(text: str, source: str = "", section: str = "",
                     line: int = 0, statement: str = "",
                     context: str = "") -> tuple[list[Occurrence], list[str]]:
    """Return every FP-P occurrence in document order with its location."""
    occs: list[Occurrence] = []
    problems: list[str] = []
    seq = [0]

    def push(offset: int, raw: str, ident: str | None, form: str,
             end: int = 0) -> None:
        seq[0] += 1
        occs.append(Occurrence(order=seq[0], source=source, section=section,
                               line=line, offset=offset, end=end, raw=raw,
                               ident=ident, form=form,
                               statement=statement or text, context=context))

    ranges = [(m.start(), m.end(), int(m.group(1)), int(m.group(2)))
              for m in PARAM_RANGE_TOKEN_RE.finditer(text)]
    range_spans = [(s, e) for s, e, _a, _b in ranges]
    for start, end, a, b in ranges:
        if a > b:
            problems.append(f"reversed range FP-P{a:02d}..FP-P{b:02d}")
            continue
        for num in range(a, b + 1):
            push(start, f"FP-P{num:02d}", f"FP-P{num:02d}", "range", end)

    malformed_spans: list[tuple[int, int]] = []
    matched: list[tuple[int, int, int, str, str, bool]] = []
    for m in PARAM_CANDIDATE_RE.finditer(text):
        raw = m.group(0)
        core = raw.rstrip(".,;:")
        norm = re.sub(r"[ \t]+", "", raw)
        ident = norm.rstrip(".,;:")
        # A token contaminated by a preceding alphanumeric character (XFP-P01)
        # is reported, never silently reduced to its valid prefix.
        prev = text[m.start() - 1] if m.start() else ""
        valid = bool(CANONICAL_PARAM_ID_RE.fullmatch(ident)) and not prev.isalnum()
        # Containment is measured on the identifier body, so trailing sentence
        # punctuation cannot push a range endpoint outside its own range span.
        matched.append((m.start(), m.start() + len(core), m.end(), raw, ident, valid))
        if not valid:
            malformed_spans.append((m.start(), m.end()))

    for start, core_end, end, raw, ident, valid in matched:
        if any(rs <= start and core_end <= re_ for rs, re_ in range_spans):
            continue
        if not valid and any(ms <= start and core_end <= me
                             for ms, me in malformed_spans
                             if (ms, me) != (start, end)):
            continue
        if valid:
            push(start, raw, ident, "standalone", end)
        else:
            push(start, raw, None, "malformed", end)
    # Document order is restored before any comparison: a range is expanded
    # first, so without this sort a reordered representation would look ordered.
    occs.sort(key=lambda o: o.offset)
    for n, o in enumerate(occs, start=1):
        o.order = n
    return occs, problems


def occurrence_stream(blocks: list[Block], source: str) -> tuple[list[Occurrence], list[str]]:
    """Every occurrence in every statement of every block, with provenance."""
    out: list[Occurrence] = []
    problems: list[str] = []
    counter = 0
    for blk in blocks:
        for stmt in split_statements(blk.text):
            occs, probs = scan_occurrences(
                stmt, source=source, section=blk.section, line=blk.start_line,
                statement=stmt, context=blk.kind)
            problems.extend(probs)
            for o in occs:
                counter += 1
                o.order = counter
                o.statement = stmt
                o.context = blk.kind
                o.section = blk.section
                o.line = blk.start_line
                out.append(o)
    return out, problems


def malformed_param_tokens(text: str) -> list[str]:
    """FP-P namespace candidates that violate the canonical identifier format."""
    return [o.raw for o in scan_occurrences(text)[0] if o.form == "malformed"]


def scan_param_occurrences(text: str) -> tuple[list[str], list[str]]:
    """Parameter occurrences in document order plus range parse diagnostics."""
    occs, problems = scan_occurrences(text)
    return [o.ident for o in occs if o.ident], problems


def compare_param_occurrences(label: str, occurrences: list[str],
                              expected_ordered: list[str],
                              parse_problems: list[str]) -> list[str]:
    """Duplicate/missing/unexpected/order diagnostics against the canonical set."""
    from collections import Counter
    out = list(parse_problems)
    expected_set = set(expected_ordered)
    counts = Counter(occurrences)
    dups = sorted(k for k, v in counts.items() if v > 1)
    if dups:
        out.append(f"{label} contains duplicate parameter "
                   + ", ".join(f"{k} (×{counts[k]})" for k in dups))
    actual = set(occurrences)
    missing = sorted(expected_set - actual)
    unexpected = sorted(actual - expected_set)
    if missing:
        out.append(f"{label} missing parameters: {', '.join(missing)}")
    if unexpected:
        out.append(f"{label} unexpected parameters: {', '.join(unexpected)}")
    first_order = list(dict.fromkeys(occurrences))
    if not missing and not unexpected and first_order != list(expected_ordered):
        out.append(f"{label} parameters out of canonical order")
    return out


# --- semantic classification (R7 defects 2 and 3) ---------------------------

# The digits of a count claim must stand alone: "B-12 parameters" names a
# system, it does not claim there are twelve parameters.
COUNT_CLAIM_RE = re.compile(
    r"(?<![\w-])(\d{1,3})\s+(?:uncalibrated\s+|provisional\s+)?(?:parameters?"
    r"|identifiers?|entries|parameter\s+values)\b", re.I)
COLLECTIVE_NOUN_RE = re.compile(
    r"\b(?:parameters?|parameter\s+(?:set|list|collection|register|inventory|series"
    r"|roster|range|chain|group|total|count|IDs)|identifiers?|entries|inventory"
    r"|collection|register|roster|chain|series|set|list)\b", re.I)
EQUATIVE_RE = re.compile(
    r"\b(?:is|are|were|was|consists?|comprise[sd]?|include[sd]?|contain[sed]?"
    r"|cover[sd]?|list[sed]?|enumerat(?:e|es|ed)|remain[sd]?|stands?|totals?"
    r"|equals?|has|have|had|spans?|runs?|gives?|reads?|amounts?)\b", re.I)
EQUATIVE_PUNCT_RE = re.compile(r"[:–—][`*_ \t]*$")
TOTALIZER_RE = re.compile(
    r"\b(?:the|these|those|all|every|both|each|current|currently|present|today"
    r"|complete|full|entire|whole|authoritative|canonical|total|remaining"
    r"|unchanged|revised|new|registered)\b", re.I)
PRESENT_STATE_RE = re.compile(
    r"\b(?:now|currently|current|present|today|still|remains?|stands?\s+at"
    r"|is|are|includes?|contains?|consists?|comprises?|covers?|lists?|equals?"
    r"|totals?|counts?|has|have|spans?|runs?\s+from|enumerates?)\b", re.I)
PAST_TENSE_RE = re.compile(
    r"\b(?:was|were|had|contained|included|listed|used|held|comprised|consisted"
    r"|became|added|registered|replaced|removed|introduced)\b", re.I)
HISTORICAL_ANCHOR_RE = re.compile(
    r"\b(?:previously|formerly|originally|historical\s+comparison|at\s+the\s+time"
    r"|earlier\s+(?:revision|version|draft|state|record|value)|previous"
    r"\s+(?:revision|version|draft|state|record)|before\s+the\s+correction"
    r"|in\s+the\s+earlier|compared\s+with\s+the\s+earlier|superseded"
    r"|replaced\s+by|obsolete|archived|no\s+longer)\b", re.I)
DATE_ANCHOR_RE = re.compile(
    r"\b(?:19|20)\d{2}-\d{2}-\d{2}\b|\b(?:in|as\s+of|dated)\s+(?:19|20)\d{2}\b"
    r"|\b(?:19|20)\d{2}\b", re.I)
SUPERSESSION_RE = re.compile(r"\b(?:superseded|replaced\s+by|obsolete|no\s+longer"
                             r"|former\s+definition)\b", re.I)
LOCUS_RE = re.compile(
    r"\b(?:this\s+entry|the\s+entry|b[\s-]*12\s+entry|the\s+register"
    r"|formula[\s-]+register|parameter[\s-]+list|parameter[\s-]+set"
    r"|parameter[\s-]+collection|parameter[\s-]+inventor\w*|the\s+inventor\w*"
    r"|inventor\w*|authoritative|canonical[\s-]+(?:set|list|collection)"
    r"|the\s+collection|handoff[\s-]+entry|status[\s-]+entry)\b", re.I)
DEFINITION_SHAPE_RE = re.compile(
    r"^\s*`?FP-[ \t]*P[A-Za-z0-9_.\-]*`?\s*"
    r"(?:[:=–—-]|\bas\b|\bmeans\b|\bis\s+(?:defined|the|a|an)\b"
    r"|\brefer(?:s)?\s+to\b)", re.I)
# An entry that adds an identifier to the enumeration it just gave is extending
# the authoritative representation, not explaining a formula.
EXTENSION_MARKER_RE = re.compile(
    r"\b(?:also|additionally|moreover|further|plus|again|both|and|as well|"
    r"in addition|included)\b", re.I)
AMBIGUOUS_MARKERS = ("historical", "previously", "formerly", "originally", "former",
                     "old", "legacy", "archived", "superseded", "earlier", "previous")
# An explicit partial qualifier settles what an enumeration covers, so a
# legitimate sub-collection statement stays explanatory instead of failing.
PARTIAL_QUALIFIER_RE = re.compile(
    r"\b(?:outside|outside\s+of|some|several|individual|part\s+of|among|such\s+as"
    r"|including|notably|two\s+of|three\s+of|the\s+following|each\s+of|whereas"
    r"|sub-?collection|subset|selected|certain)\b", re.I)


def is_historical_exempt(stmt: str) -> bool:
    """Context-based historical classification, not keyword exemption.

    A historical word carries no exemption on its own. Exemption needs an
    explicit anchor (a date, a past-tense predicate, or a documented
    supersession) AND no present-state collection predicate; a present-tense
    assertion always defeats the qualifier.
    """
    cls, _ = classify_statement(stmt)
    return cls in ("historical", "superseded")


CLASSIFICATIONS = ("current-assertion", "historical", "superseded", "explanatory",
                   "canonical-definition", "malformed-candidate", "ambiguous")


@lru_cache(maxsize=40000)
def classify_statement(stmt: str) -> tuple[str, str]:
    """Assign one of the seven R7 classifications to a logical statement."""
    low = stmt.lower()
    occs = scan_occurrences(stmt)[0]
    ids = [o.ident for o in occs if o.ident]
    mal = [o for o in occs if o.form == "malformed"]
    if mal and not ids:
        return "malformed-candidate", "malformed identifier with no valid token"
    if not ids and not COUNT_CLAIM_RE.search(stmt):
        return "explanatory", "no parameter-bearing content"

    has_range = bool(PARAM_RANGE_TOKEN_RE.search(stmt))
    has_count = bool(COUNT_CLAIM_RE.search(stmt))
    first = min((o.offset for o in occs if o.ident), default=len(stmt))
    head = stmt[:first]
    enumerated_claim = bool(COLLECTIVE_NOUN_RE.search(head)
                            and (EQUATIVE_RE.search(head)
                                 or EQUATIVE_PUNCT_RE.search(head))
                            and TOTALIZER_RE.search(head))
    locus_claim = bool(LOCUS_RE.search(stmt) and PRESENT_STATE_RE.search(stmt))
    claim = has_range or has_count or enumerated_claim or locus_claim
    if not claim:
        if DEFINITION_SHAPE_RE.match(stmt):
            return "canonical-definition", "definition-shaped record"
        # An enumeration introduced by a colon after a collective noun, with no
        # totalizer and no partial qualifier, cannot be read either way. In an
        # authoritative region it is reported, never silently exempted.
        if (ids and COLLECTIVE_NOUN_RE.search(head)
                and EQUATIVE_PUNCT_RE.search(head)
                and not PARTIAL_QUALIFIER_RE.search(stmt)):
            return "ambiguous", "colon enumeration without a completeness signal"
        return "explanatory", "reference to an individual parameter"

    # Tense is decided by the clause that governs the enumeration, never by a
    # trailing parenthetical and never by a historical word on its own.
    head_present = bool(PRESENT_STATE_RE.search(head))
    head_anchored = bool(HISTORICAL_ANCHOR_RE.search(head)
                         or DATE_ANCHOR_RE.search(head)
                         or PAST_TENSE_RE.search(head))
    if head_present or (locus_claim and not head_anchored):
        return "current-assertion", "present-state clause governs the enumeration"
    if head_anchored:
        if SUPERSESSION_RE.search(head):
            return "superseded", "explicitly superseded record"
        return "historical", "anchored past-tense record"
    if SUPERSESSION_RE.search(low) and not PRESENT_STATE_RE.search(low):
        return "superseded", "explicitly superseded record"
    if has_range or has_count or enumerated_claim:
        return "current-assertion", "unanchored collection enumeration is current"
    return "ambiguous", "collection reference with no tense or completeness signal"


def logical_statements(text: str) -> list[str]:
    """Every sentence-unit of every block, in document order."""
    out: list[str] = []
    for blk in iter_blocks(text):
        out.extend(split_statements(blk.text))
    return out


def representation_problems(label: str, blocks: list[Block],
                            ordered: list[str], source: str,
                            require_representation: bool = False,
                            ledger: bool = True,
                            strict: bool = False) -> tuple[list[str], list[Occurrence]]:
    """Validate every authoritative current-state representation in a block set.

    Strict mode is used for the AI_CONTEXT B-12 entry, where a sentence that
    adds an identifier to the entry's enumeration extends the authoritative
    representation instead of being an explanatory mention. Elsewhere a
    well-formed explanatory mention of a canonical identifier stays valid.
    """
    expected_set, expected_count = set(ordered), len(ordered)
    problems: list[str] = []
    ledger_ids: list[str] = []
    representations = 0
    stream, stream_problems = occurrence_stream(blocks, source)
    problems.extend(stream_problems)
    for blk in blocks:
        for stmt in split_statements(blk.text):
            cls, _ = classify_statement(stmt)
            stmt_occs = scan_occurrences(
                stmt, source=source, section=blk.section, line=blk.start_line,
                statement=stmt, context=blk.kind)[0]
            for o in stmt_occs:
                o.classification = cls
            mal = [o.raw for o in stmt_occs if o.form == "malformed"]
            ids = [o.ident for o in stmt_occs if o.ident]
            if is_historical_exempt(stmt):
                # An anchored historical or superseded record is exempt first; a
                # present-tense claim never becomes exempt because of a label.
                if mal:
                    problems.append(
                        f"{label} malformed parameter identifier(s) in historical "
                        "record: " + ", ".join(sorted(set(mal))))
                for o in stmt_occs:
                    o.outcome = "exempt-historical" if o.form != "malformed" \
                        else "rejected-malformed"
                continue
            if mal:
                problems.append(
                    f"{label} malformed parameter identifier(s): "
                    + ", ".join(sorted(set(mal))))
            for o in stmt_occs:
                o.outcome = "rejected-malformed" if o.form == "malformed" else "counted"
            if not ids and not COUNT_CLAIM_RE.search(stmt):
                continue
            if cls == "ambiguous":
                problems.append(
                    f"{label} ambiguous current-state parameter assertion at line "
                    f"{blk.start_line}: " + stmt[:80].strip())
                continue
            if (strict and cls == "explanatory" and ids
                    and (EXTENSION_MARKER_RE.search(stmt)
                         or len(set(ids)) > 1)
                    and not PARTIAL_QUALIFIER_RE.search(stmt)):
                # Inside the authoritative entry an identifier added to the
                # enumeration, or a bare multi-identifier listing, extends the
                # current representation rather than commenting on a formula,
                # so it joins the duplicate and completeness accounting.
                cls = "current-assertion"
            if cls == "explanatory":
                unexpected = sorted(set(ids) - expected_set)
                if unexpected:
                    problems.append(f"{label} unexpected parameters: "
                                    + ", ".join(unexpected))
                for o in stmt_occs:
                    if o.ident:
                        o.outcome = "counted-explanatory"
                continue
            if cls == "canonical-definition":
                continue
            # current-assertion: an authoritative representation
            representations += 1
            ledger_ids.extend(ids)
            for cm in COUNT_CLAIM_RE.finditer(stmt):
                if int(cm.group(1)) != expected_count:
                    problems.append(
                        f"{label} stale {cm.group(1)}-parameter current-state claim "
                        f"at line {blk.start_line} (canonical register declares "
                        f"{expected_count})")
            for rm in PARAM_RANGE_TOKEN_RE.finditer(stmt):
                span_ids = [o.ident for o in stmt_occs if o.form == "range"]
                if set(span_ids) != expected_set:
                    problems.append(
                        f"{label} stale current-state parameter range "
                        f"{rm.group(0)} at line {blk.start_line}")
            if ids and set(ids) != expected_set:
                problems.append(f"{label} stale current-state parameter "
                                "identifiers: " + ", ".join(sorted(set(ids))))
            if ids:
                problems.extend(compare_param_occurrences(label, ids, ordered, []))
    if ledger and ledger_ids:
        problems.extend(compare_param_occurrences(label, ledger_ids, ordered, []))
    if require_representation and representations == 0:
        problems.append(f"{label} carries no authoritative parameter representation")
    return problems, stream


def param_representation(blocks: list[Block], ordered: list[str]) -> dict[str, object]:
    """Summary of the authoritative representations found in a block set."""
    expected = set(ordered)
    reps = []
    for blk in blocks:
        for stmt in split_statements(blk.text):
            cls, _ = classify_statement(stmt)
            ids = [o.ident for o in scan_occurrences(stmt)[0] if o.ident]
            if cls == "current-assertion" and ids:
                reps.append({"line": blk.start_line, "kind": blk.kind,
                             "complete": set(ids) == expected,
                             "count": len(set(ids)), "ids": ids})
    return {"representations": reps, "canonical_set": sorted(expected)}


def canonical_region_blocks(text: str) -> tuple[list[Block], list[Block], list[str]]:
    """Split the canonical register into its parameter-definition region.

    Returns (region blocks, outside blocks, problems). The boundary runs from
    the parameter-register heading to the next heading that is not part of the
    definition region; an undeterminable boundary is reported, never guessed.
    """
    problems: list[str] = []
    blocks = iter_blocks(text)
    start = next((i for i, b in enumerate(blocks)
                  if b.kind == "heading" and re.match(r"^#+\s*3\.\s*Parameter register",
                                                      b.text, re.I)), None)
    if start is None:
        return [], blocks, ["canonical parameter-register section heading missing"]
    end = len(blocks)
    for j in range(start + 1, len(blocks)):
        b = blocks[j]
        if b.kind != "heading":
            continue
        level = len(b.text) - len(b.text.lstrip("#"))
        title = b.text.lstrip("#").strip()
        if level <= 2 or re.match(r"^3\.\d", title):
            end = j
            break
    if end == len(blocks):
        problems.append("canonical parameter-definition region has no closing "
                        "boundary heading")
    outside = blocks[:start + 1] + blocks[end:]
    return blocks[start + 1:end], outside, problems


def canonical_definitions(text: str) -> tuple[list[str], list[str], list[dict]]:
    """Discover every canonical parameter definition candidate in the register.

    Table rows, headings, list items, definition lists and ordinary prose are
    all inspected; no block kind is skipped. A candidate is a definition when
    the identifier sits in a leading definition position or is followed by a
    definition separator, so an explanatory mention is never counted as a
    second definition.
    """
    region, outside, problems = canonical_region_blocks(text)
    if not region and not problems:
        problems.append("canonical parameter-definition region is empty")
    records: list[dict] = []
    ordered: list[str] = []
    seen: set[str] = set()

    def consider(tok_raw: str, norm: str, blk: Block, position: str,
                 boundary: str) -> None:
        valid = bool(CANONICAL_PARAM_ID_RE.fullmatch(norm))
        records.append({"token": norm if valid else tok_raw, "valid": valid,
                        "line": blk.start_line, "kind": blk.kind,
                        "section": blk.section, "position": position,
                        "boundary": boundary, "text": blk.text})
        if not valid:
            problems.append(f"malformed canonical parameter ID: {tok_raw} "
                            f"(line {blk.start_line}, {position})")
            return
        if norm in seen:
            problems.append(f"duplicate canonical parameter definition: {norm} "
                            f"(line {blk.start_line}, {position})")
            return
        seen.add(norm)
        ordered.append(norm)

    for blk in region:
        cells_txt = None
        if blk.kind == "table-row":
            cells_txt = [c.strip() for c in blk.text.strip().strip("|").split("|")]
            head = cells_txt[0] if cells_txt else ""
            occ = scan_occurrences(head, context=blk.kind, statement=blk.text)[0]
            leading = [o for o in occ if o.offset == leading_index(head)]
            if leading:
                o = leading[0]
                consider(o.raw, (o.ident or re.sub(r"[ \t]+", "", o.raw).rstrip(".,;:")),
                         blk, "table-row first cell", "canonical region")
                continue
            body_occ = scan_occurrences(blk.text, context=blk.kind,
                                        statement=blk.text)[0]
            if body_occ:
                problems.append(
                    f"parameter-bearing table record without a leading identifier "
                    f"at line {blk.start_line}: {blk.text[:70]}")
            continue
        for stmt in split_statements(blk.text):
            occ = scan_occurrences(stmt, context=blk.kind, statement=stmt)[0]
            if not occ:
                continue
            first = occ[0]
            at_leading = first.offset == leading_index(stmt)
            tail = after_token(stmt, first.offset, first.raw)
            followed = re.match(
                r"(?:[:=–—-]|\bis\s+defined\s+as\b|\bmeans\b|\brefers?\s+to\b|\bis\b)",
                tail, re.I)
            if at_leading or followed:
                norm = first.ident or re.sub(r"[ \t]+", "", first.raw).rstrip(".,;:")
                consider(first.raw, norm, blk,
                         f"{blk.kind} leading" if at_leading else f"{blk.kind} defined-as",
                         "canonical region")
            else:
                for o in occ:
                    if o.form == "malformed":
                        problems.append(
                            f"malformed canonical parameter ID: {o.raw} "
                            f"(line {blk.start_line}, {blk.kind})")

    # Definition records outside the permitted canonical boundary. Only an
    # unambiguous definition record (leading identifier plus definition verb or
    # separator) counts, so ordinary explanatory prose in the register is not
    # mistaken for a second definition.
    for blk in outside:
        for stmt in split_statements(blk.text):
            occ = scan_occurrences(stmt, context=blk.kind, statement=stmt)[0]
            if not occ:
                continue
            first = occ[0]
            at_leading = first.offset == leading_index(stmt)
            explicit = re.match(
                r"(?:[:=–—-]|\bis\s+defined\s+as\b|\bmeans\b|\brefers?\s+to\b)",
                after_token(stmt, first.offset, first.raw), re.I)
            if at_leading and explicit:
                problems.append(
                    "canonical definition record outside the parameter-register "
                    f"boundary: line {blk.start_line} ({blk.kind}) "
                    f"{first.raw or first.ident}")
                if first.ident and first.ident not in seen:
                    problems.append(f"unexpected canonical parameter definition: "
                                    f"{first.ident}")
    return ordered, problems, records


def canonical_params(m: Model) -> tuple[list[str], list[str]]:
    """Extract the authoritative ordered parameter IDs from the canonical register.

    The formula register is the sole production source of truth. The ordered
    collection, its expected count and its identifier set are derived from the
    discovered definition records; no downstream check keeps a fixed list.
    Presence, format, uniqueness, contiguity and region boundary are validated
    and an empty or unreadable extraction is a failure, never a fallback.
    """
    if not m.src.get("formulas"):
        return [], ["canonical formula register missing or unreadable"]
    return list(m.canonical_defs), list(m.canonical_problems)


def check_63(m: Model) -> tuple[bool, str]:
    """F-FP-002 removes the observed excess and its example arithmetic holds."""
    fields = m.formulas.get("F-FP-002", {})
    expr = fields.get(4, "")
    example = fields.get(12, "")
    boundary = fields.get(7, "")
    mt = re.search(r"`V_law = (\d+)`, `V_obs = (\d+)`, `B_i = (\d+)` → "
                   r"`C = min\(max\(\d+, 0\), \d+\) = (\d+)`", example)
    if "V_obs − V_law" not in expr or not mt or "V_obs ≤ V_law" not in boundary:
        return False, "F-FP-002 direction, boundary or example missing"
    law, obs, bi, claimed = (int(x) for x in mt.groups())
    computed = min(max(obs - law, 0), bi)
    if computed != claimed:
        return False, f"F-FP-002 example computes {computed}, claims {claimed}"
    return True, f"F-FP-002 example computes {computed} = claimed {claimed}"


def check_64(m: Model) -> tuple[bool, str]:
    """F-FP-001 carries no repetition term and its example arithmetic holds."""
    fields = m.formulas.get("F-FP-001", {})
    expr = fields.get(4, "")
    example = fields.get(12, "")
    if "+ R" in expr or "− R" in expr:
        return False, "F-FP-001 still contains a repetition term"
    mt = re.search(r"`S_c = (\d+)`, `I_p = (\d+)`, `K = (\d+)`, `M = (\d+)` → "
                   r"`SEV = (\d+)`", example)
    if not mt:
        return False, "F-FP-001 example missing"
    sc, ip, k, mm, claimed = (int(x) for x in mt.groups())
    computed = max(sc + ip + k - mm, 0)
    if computed != claimed:
        return False, f"F-FP-001 example computes {computed}, claims {claimed}"
    return True, f"F-FP-001 example computes {computed} = claimed {claimed}"


def check_65(m: Model) -> tuple[bool, str]:
    """F-FP-011 is the sole repetition adjustment and its example holds."""
    fields = m.formulas.get("F-FP-011", {})
    purpose = fields.get(1, "")
    example = fields.get(12, "")
    if "only formula" not in purpose:
        return False, "F-FP-011 does not state it is the sole repetition adjustment"
    mt = re.search(r"`SEV = (\d+)`, `R = (\d+)`, `q = (\d+)` → `SEV_R = (\d+)`",
                   example)
    if not mt:
        return False, "F-FP-011 example missing"
    sev, r, q, claimed = (int(x) for x in mt.groups())
    computed = sev + min(r, 2) * q
    if computed != claimed:
        return False, f"F-FP-011 example computes {computed}, claims {claimed}"
    return True, f"F-FP-011 example computes {computed} = claimed {claimed}"


def check_66(m: Model) -> tuple[bool, str]:
    """F-FP-014 and COR-003 share the signed convention and all six types."""
    fields = m.formulas.get("F-FP-014", {})
    variables = fields.get(5, "")
    expr = fields.get(4, "")
    cor003 = m.rules.get("COR-003", ("", ""))[1]
    ok = ("signed" in variables.lower() and "+ A" in expr
          and "signed" in cor003.lower() and "ADMIN_ADJUSTMENT" in cor003)
    return ok, "signed conservation convention aligned" if ok else "sign convention or ADMIN_ADJUSTMENT missing"


def check_67(m: Model) -> tuple[bool, str]:
    """The configurable window and rate factor are registered and referenced."""
    f8 = " ".join(m.formulas.get("F-FP-008", {}).values())
    f9 = " ".join(m.formulas.get("F-FP-009", {}).values())
    ok = ("FP-P13" in m.params and "FP-P14" in m.params
          and "FP-P13" in f8 and "FP-P14" in f9 and "FP-P07" in f9)
    return ok, "FP-P13 and FP-P14 registered and referenced" if ok else "window/factor parameter missing"


def check_68(m: Model) -> tuple[bool, str]:
    """Parameter identifiers are unique."""
    raw = re.findall(r"^\|\s*`(FP-P\d{2})`", m.src.get("formulas", ""), re.M)
    dup = len(raw) - len(set(raw))
    return dup == 0, f"{len(raw)} parameter rows, {dup} duplicates"


def check_69(m: Model) -> tuple[bool, str]:
    """The acceptance system mapping matches the canonical INT contracts."""
    expected = {
        "B-02": ["INT-013", "INT-014"],
        "B-03": ["INT-001"],
        "B-04": ["INT-003"],
        "B-05": ["INT-004"],
        "B-06": ["INT-005"],
        "B-07": ["INT-006"],
        "B-08": ["INT-007"],
        "B-09": ["INT-008"],
        "B-10": ["INT-009"],
    }
    problems = []
    for prefix, contracts in expected.items():
        rows = [row for key, row in m.sys_map.items() if key.startswith(prefix)]
        if not rows:
            problems.append(f"{prefix} row missing")
            continue
        joined = " ".join(" ".join(row) for row in rows)
        for c in contracts:
            if c not in joined:
                problems.append(f"{prefix} lacks {c}")
    world = [row for key, row in m.sys_map.items() if key.startswith("B-11 world")]
    rank = [row for key, row in m.sys_map.items() if key.startswith("B-11 rankings")]
    if not world or "INT-010" not in " ".join(world[0]):
        problems.append("B-11 world events lacks INT-010")
    if not rank or "INT-011" not in " ".join(rank[0]):
        problems.append("B-11 rankings lacks INT-011")
    if any("economy" in key for key in m.sys_map if key.startswith("B-03")):
        problems.append("B-03 mislabelled as economy")
    return not problems, ("canonical system mapping verified" if not problems
                          else "; ".join(problems))


def check_70(m: Model) -> tuple[bool, str]:
    """Every INT contract states the seven dependency fields."""
    expected = [f"INT-{n:03d}" for n in range(1, 21)]
    if sorted(m.int_fields) != expected:
        return False, f"expected 20 INT field rows, found {len(m.int_fields)}"
    bad = [k for k, row in m.int_fields.items()
           if len(row) != 8 or any(not c for c in row)]
    return not bad, ("20 contracts carry seven populated fields" if not bad
                     else f"incomplete field rows: {bad[:5]}")


def check_71(m: Model) -> tuple[bool, str]:
    """The consolidated dependency traceability links resolve to requirements."""
    expected = [f"INT-{n:03d}" for n in range(1, 21)]
    if sorted(m.dep_trace) != expected:
        return False, f"expected 20 traceability rows, found {len(m.dep_trace)}"
    bad = []
    for k, row in m.dep_trace.items():
        if len(row) < 11:
            bad.append(f"{k}:thin")
            continue
        for rid in re.findall(r"REQ-(\d{3})", row[2]):
            if int(rid) not in m.req1:
                bad.append(f"{k}:REQ-{rid}")
    return not bad, ("20 traceability rows resolve" if not bad
                     else f"unresolved: {bad[:5]}")


def check_72(m: Model) -> tuple[bool, str]:
    """The original Prompt 12B instruction is archived, indexed and referenced."""
    import hashlib
    if not PROMPT_ARCHIVE.exists() or not PROMPT_INDEX.exists():
        return False, "prompt archive or index missing"
    data = PROMPT_ARCHIVE.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    index = PROMPT_INDEX.read_text(encoding="utf-8")
    roadmap = m.src.get("log", "") + read(STAGE2 / "01_stage_2_prompt_roadmap.md")
    ok = (PROMPT_ARCHIVE.name in index and digest in index
          and PROMPT_ARCHIVE.name in roadmap and len(data) > 30000)
    return ok, f"archive present, {len(data)} bytes, hash indexed" if ok else "archive/index/roadmap reference incomplete"


def check_73(m: Model) -> tuple[bool, str]:
    """A truthful policy-reading attestation is recorded."""
    log = m.src.get("log", "")
    seg = section(log, "## 76.", "## 77.") or log[log.find("## 76."):]
    ok = ("AUTONOMOUS_DECISION_POLICY.md" in seg and "2026-11-07" in seg
          and "complete" in seg.lower() and "D-014" in seg
          and "historical" in seg.lower())
    return ok, "policy attestation present with date and historical distinction" if ok else "attestation missing or incomplete"


def check_74(m: Model) -> tuple[bool, str]:
    """The 12B-C1 gate reassessment is recorded and preserves the PARTIAL gates."""
    a = m.src.get("acceptance", "")
    seg = section(a, "### 2.1 Prompt 12B-C1 reassessment", "## 3.")
    ok = bool(seg) and all(g in seg for g in ("P12B-14", "P12B-16", "P12B-23")) \
        and seg.count("PARTIAL") >= 3
    return ok, "reassessment recorded; three PARTIAL gates preserved" if ok else "reassessment missing"


def check_75(m: Model) -> tuple[bool, str]:
    """The formula-to-parameter mapping covers all sixteen formulas."""
    seg = section(m.src.get("formulas", ""), "### 3.1 Formula-to-parameter mapping", "## 4.")
    ids = set(re.findall(r"^\|\s*`(F-FP-\d{3})`", seg, re.M))
    ok = ids == set(FORMULA_IDS)
    return ok, f"{len(ids)} formulas mapped" if ok else f"mapping covers {len(ids)}/16"


def check_76(m: Model) -> tuple[bool, str]:
    """The canonical register defines a unique, well-formed, contiguous set.

    Every definition candidate inside the parameter-register region is
    discovered — table rows, headings, list items and prose — and every
    definition-shaped record outside the region boundary is reported.
    """
    ordered, problems = canonical_params(m)
    if problems:
        return False, "; ".join(problems)
    if not ordered:
        return False, "canonical formula register has no parameter definitions"
    nums = [int(x[4:]) for x in ordered]
    if sorted(nums) != list(range(1, len(nums) + 1)):
        missing = [f"FP-P{n:02d}" for n in range(1, max(nums) + 1)
                   if f"FP-P{n:02d}" not in set(ordered)]
        return False, ("canonical register missing parameters: "
                       + ", ".join(missing) + " (non-contiguous)")
    if nums != sorted(nums):
        return False, ("canonical register parameter order does not ascend: "
                       + ", ".join(ordered))
    kinds = {r["kind"] for r in m.def_records if r["boundary"] == "canonical region"}
    return True, (f"canonical register defines {len(ordered)} unique parameters "
                  f"{ordered[0]}…{ordered[-1]} across {len(kinds)} block kinds")


B12_RELEVANT_RE = re.compile(
    r"\b(?:B-12|b12_fair_play|12B|fair_play_and_player_protection|FP-P|F-FP-)")


def b12_entry_blocks(ctx: str) -> tuple[list[Block], list[Block], list[Block]]:
    """Locate the complete current B-12 entry inside AI_CONTEXT.

    Returns (status-entry blocks, inventory blocks, whole-entry blocks). The
    entry is the `b12_fair_play:` status record together with the B-12
    formula-register inventory row and every block attached to either of them:
    continuation lines, indented content, following paragraphs, extra table
    rows and additional sentences. Selection is structural and transitive, not
    first-match, so content that continues an entry line is never left behind.
    """
    blocks = iter_blocks(ctx)
    status = [b for b in blocks
              if b.kind == "key-entry" and b.text.startswith("b12_fair_play:")]
    register_rows = [b for b in blocks
                     if b.kind == "table-row" and CTX_REGISTER_PATH in b.text]
    seeds = status + register_rows
    included = {id(b) for b in seeds}
    entry: list[Block] = []
    for i, blk in enumerate(blocks):
        if id(blk) in included:
            entry.append(blk)
            continue
        if i == 0:
            continue
        prev = blocks[i - 1]
        if id(prev) not in included:
            continue
        if blk.start_line - prev.end_line - 1 > 1:
            continue
        if blk.kind == "heading":
            continue
        if B12_RELEVANT_RE.search(blk.text) or B12_RELEVANT_RE.search(prev.text):
            entry.append(blk)
            included.add(id(blk))
    return status, register_rows, entry


def acceptance_current_problems(a: str, ordered: list[str]) -> list[str]:
    """Semantic scan of every current-state parameter claim in the acceptance doc.

    The acceptance document legitimately restates the canonical collection in
    several sections (gate register, §2.1, §6, §9, §11), so duplicate
    accounting is applied within each representation rather than across the
    whole document. Every representation must still equal the extracted
    collection exactly.
    """
    blocks = iter_blocks(a)
    problems, _ = representation_problems("acceptance", blocks, ordered,
                                          "acceptance document", ledger=False)
    return problems


def check_77(m: Model) -> tuple[bool, str]:
    """Exactly one P12B-19 gate; full occurrence scan; no stale current claims."""
    a = m.src.get("acceptance", "")
    ordered, _ = canonical_params(m)
    expected_set, expected_count = set(ordered), len(ordered)
    problems = []
    gate_section = section(a, "## 2. Gate register", "### 2.1")
    gates = [ln for ln in gate_section.splitlines()
             if re.match(r"^\|\s*`?P12B-19`?\s*\|", ln)]
    if len(gates) != 1:
        problems.append(f"expected exactly one P12B-19 gate row, found {len(gates)}")
    for g in gates:
        occ, parse_problems = scan_param_occurrences(g)
        problems.extend(compare_param_occurrences("P12B-19", occ, ordered,
                                                  parse_problems))
        mal = malformed_param_tokens(g)
        if mal:
            problems.append("P12B-19 contains malformed parameter identifier(s): "
                            + ", ".join(sorted(set(mal))))
    sec9 = section(a, "## 9.", "## 10.")
    if f"{expected_count} parameters" not in sec9:
        problems.append(f"acceptance §9 does not report {expected_count} parameters")
    problems.extend(acceptance_current_problems(a, ordered))
    return not problems, (f"P12B-19 and acceptance current-state claims cover all "
                          f"{expected_count} canonical parameters"
                          if not problems else "; ".join(problems))


def check_78(m: Model) -> tuple[bool, str]:
    """The complete current B-12 AI_CONTEXT entry is structurally parsed."""
    ctx = m.src.get("ai_context", "")
    ordered, _ = canonical_params(m)
    expected_count = len(ordered)
    expected_set = set(ordered)
    status, register_rows, entry = b12_entry_blocks(ctx)
    if not register_rows:
        return False, "AI_CONTEXT B-12 formula-register entry missing"
    problems = []
    if len(register_rows) > 1:
        problems.append(f"AI_CONTEXT contains {len(register_rows)} conflicting "
                        "current-state B-12 formula-register entries "
                        "(expected exactly one)")
    if len(status) > 1:
        problems.append(f"AI_CONTEXT contains {len(status)} conflicting "
                        "b12_fair_play status entries (expected exactly one)")
    if status:
        rep_problems, _ = representation_problems(
            "AI_CONTEXT b12_fair_play status entry", status, ordered,
            "AI_CONTEXT status entry", require_representation=True)
        problems.extend(rep_problems)
    entry_problems, _stream = representation_problems(
        "AI_CONTEXT B-12 entry", entry, ordered, "AI_CONTEXT B-12 entry",
        strict=True)
    problems.extend(entry_problems)
    entry_text = "\n".join(b.text for b in entry)
    if f"{expected_count} parameters" not in entry_text:
        problems.append(f"AI_CONTEXT B-12 entry does not report {expected_count} "
                        "parameters")
    # Tier 2: no unrecognised identifier may hide in explanatory entry content.
    all_ids = [o.ident for o in _stream if o.ident]
    unexpected = sorted(set(all_ids) - expected_set)
    if unexpected:
        problems.append("AI_CONTEXT B-12 entry unexpected parameters: "
                        + ", ".join(unexpected))
    seen: set[str] = set()
    out = []
    for p in problems:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return not out, (f"AI_CONTEXT complete B-12 entry covers all "
                     f"{expected_count} canonical parameters"
                     if not out else "; ".join(out))


def check_83(m: Model) -> tuple[bool, str]:
    """Every FP-P namespace occurrence in the validated corpus is accounted for.

    Each occurrence keeps its source file, section, line, span, original token,
    normalised identifier, surrounding statement, structural context, semantic
    classification, order and outcome. A namespace marker that is not covered
    by a recorded occurrence span is an accounting failure, so punctuation,
    markdown or a line break cannot make an occurrence disappear.
    """
    ordered, _ = canonical_params(m)
    expected = set(ordered)
    problems: list[str] = []
    total = 0
    classes: dict[str, int] = {}
    for label, blocks in (("acceptance document",
                           iter_blocks(m.src.get("acceptance", ""))),
                          ("AI_CONTEXT B-12 entry",
                           b12_entry_blocks(m.src.get("ai_context", ""))[2])):
        for blk in blocks:
            for stmt in split_statements(blk.text):
                occs, probs = scan_occurrences(
                    stmt, source=label, section=blk.section, line=blk.start_line,
                    statement=stmt, context=blk.kind)
                problems.extend(p for p in probs if p not in problems)
                total += len(occs)
                cls, _ = classify_statement(stmt)
                for o in occs:
                    o.classification = cls
                if cls not in CLASSIFICATIONS:
                    problems.append(f"{label} line {blk.start_line}: unknown "
                                    f"classification {cls}")
                for o in occs:
                    classes[cls] = classes.get(cls, 0) + 1
                    if not o.source or not o.line or not o.statement:
                        problems.append(f"{label} occurrence {o.raw} has no "
                                        "provenance")
                    if o.form == "malformed":
                        o.outcome = "rejected-malformed"
                        problems.append(f"{label} malformed parameter identifier "
                                        f"{o.raw} at line {o.line}")
                    elif o.ident not in expected:
                        o.outcome = "rejected-unexpected"
                        problems.append(f"{label} unexpected parameter {o.ident} "
                                        f"at line {o.line}")
                    else:
                        o.outcome = "accounted"
                # namespace coverage
                covered = [(o.offset, o.end) for o in occs]
                for mt in PARAM_NAMESPACE_RE.finditer(stmt):
                    if any(s <= mt.start() < e for s, e in covered):
                        continue
                    problems.append(
                        f"{label} unaccounted FP-P namespace marker at line "
                        f"{blk.start_line}: {stmt[mt.start():mt.start() + 12]!r}")
    detail = (f"{total} occurrences accounted across "
              + ", ".join(f"{k}={v}" for k, v in sorted(classes.items())))
    return not problems, detail if not problems else "; ".join(problems[:6])


def check_84(m: Model) -> tuple[bool, str]:
    """Canonical definition discovery inspects every block kind, not tables only."""
    if not m.src.get("formulas"):
        return False, "canonical formula register missing or unreadable"
    ordered, problems, records = canonical_definitions(m.src.get("formulas", ""))
    if problems:
        return False, "; ".join(problems)
    if not records:
        return False, "no canonical definition candidates discovered"
    positions = {r["position"] for r in records}
    if not any("first cell" in p for p in positions):
        return False, "table-row definitions not discovered"
    region_blocks = iter_blocks(m.src.get("formulas", ""))
    kinds = {b.kind for b in region_blocks}
    return True, (f"{len(records)} definition candidates discovered; region holds "
                  f"{sorted(kinds)} blocks; {len(ordered)} canonical parameters "
                  f"({', '.join(sorted(positions))})")


def check_85(m: Model) -> tuple[bool, str]:
    """No authoritative parameter-bearing record is left ambiguous."""
    ordered, _ = canonical_params(m)
    ambiguous = []
    for label, blocks in (
            ("acceptance document", iter_blocks(m.src.get("acceptance", ""))),
            ("AI_CONTEXT B-12 entry",
             b12_entry_blocks(m.src.get("ai_context", ""))[2])):
        for blk in blocks:
            for stmt in split_statements(blk.text):
                cls, _ = classify_statement(stmt)
                if cls == "ambiguous":
                    ambiguous.append(
                        f"{label} line {blk.start_line} [ambiguous assertion] "
                        + stmt[:70])
    return not ambiguous, (f"no ambiguous authoritative parameter records"
                           if not ambiguous else "; ".join(ambiguous[:4]))


def check_86(m: Model) -> tuple[bool, str]:
    """A historical exemption is always anchor-backed, never keyword-only."""
    exempt = 0
    unanchored = []
    for text in (m.src.get("acceptance", ""), m.src.get("ai_context", "")):
        for stmt in logical_statements(text):
            ids = [o.ident for o in scan_occurrences(stmt)[0] if o.ident]
            if not ids and not COUNT_CLAIM_RE.search(stmt):
                continue
            low = stmt.lower()
            if not any(w in low for w in AMBIGUOUS_MARKERS):
                continue
            cls, _ = classify_statement(stmt)
            if cls in ("historical", "superseded"):
                exempt += 1
                anchored = bool(DATE_ANCHOR_RE.search(low)
                                or HISTORICAL_ANCHOR_RE.search(low)
                                or PAST_TENSE_RE.search(low))
                if not anchored:
                    unanchored.append(f"{cls} without a date, past-tense or "
                                      f"supersession anchor: {stmt[:70]}")
            elif cls == "current-assertion":
                if PRESENT_STATE_RE.search(low):
                    continue
                unanchored.append("keyword-only historical exemption: " + stmt[:70])
    return not unanchored, (f"{exempt} anchored historical exemptions; no "
                            f"keyword-only exemption" if not unanchored
                            else "; ".join(unanchored[:4]))


def check_87(m: Model) -> tuple[bool, str]:
    """Every authoritative representation equals the single extracted source."""
    ordered, problems = canonical_params(m)
    if problems or not ordered:
        return False, "; ".join(problems) or "no canonical definitions extracted"
    expected = list(ordered)
    checked = 0
    drift = []
    for label, blocks in (
            ("acceptance", iter_blocks(m.src.get("acceptance", ""))),
            ("AI_CONTEXT", b12_entry_blocks(m.src.get("ai_context", ""))[2])):
        summary = param_representation(blocks, expected)
        for rep in summary["representations"]:
            checked += 1
            if rep["ids"] != expected:
                drift.append(f"{label} line {rep['line']} enumerates "
                             f"{len(rep['ids'])} identifiers that differ from the "
                             f"{len(expected)} extracted canonical records")
    if drift:
        return False, "; ".join(drift[:4])
    if checked < 2:
        return False, (f"only {checked} authoritative representations found in "
                       "acceptance and AI_CONTEXT")
    return True, (f"{checked} authoritative representations equal the "
                  f"source-derived collection ({len(expected)} parameters)")


def check_79(m: Model) -> tuple[bool, str]:
    """The policy attestation line count matches the actual policy file."""
    log = m.src.get("log", "")
    seg = section(log, "## 76.", "## 77.") or log[log.find("## 76."):]
    if not POLICY.exists():
        return False, "policy file missing"
    actual = len(read(POLICY).splitlines())
    ok = ("AUTONOMOUS_DECISION_POLICY.md" in seg and f"{actual} lines" in seg
          and ("wc -l" in seg or "splitlines" in seg)
          and "version 1.0" in seg.lower() and "2026-11-07" in seg)
    return ok, (f"attestation line count {actual} matches policy (reproducible)"
                if ok else f"attestation metadata incorrect (policy has {actual} lines)")


def check_80(m: Model) -> tuple[bool, str]:
    """The R1-specific §77.1 manifest independently lists every R1-changed file."""
    seg = section(m.src.get("log", ""), "### 77.1", "### 77.2")
    if not seg:
        return False, "R1 §77.1 manifest section missing"
    rows = re.findall(r"^\|\s*`([^`]+)`\s*\|", seg, re.M)
    if not rows:
        return False, "R1 §77.1 manifest is empty or malformed (no file rows)"
    listed = set(rows)
    missing = [f for f in R1_MANIFEST_REQUIRED if f not in listed]
    if missing:
        return False, ("R1 §77.1 manifest missing: " + ", ".join(missing)
                       + " (a §76.1 entry cannot satisfy §77.1)")
    return True, f"R1 §77.1 manifest lists all {len(R1_MANIFEST_REQUIRED)} required files"


def check_81(m: Model) -> tuple[bool, str]:
    """The historical §75 record of the earlier 12-parameter state is preserved."""
    seg = section(m.src.get("log", ""), "## 75.", "## 76.")
    ok = bool(seg) and bool(re.search(r"\b12 (?:uncalibrated )?parameters\b", seg))
    return ok, ("historical 12-parameter record preserved" if ok
                else "historical §75 12-parameter record was rewritten or removed")


def check_82(m: Model) -> tuple[bool, str]:
    """The historical C1 §76.1 manifest-completeness note is preserved."""
    seg = section(m.src.get("log", ""), "### 76.1", "### 76.2")
    needed = ["Manifest completeness correction", "docs/AI_CONTEXT.md",
              "docs/AI_HANDOFF.md", "docs/PROJECT_PROGRESS.md", "docs/ROADMAP.md",
              "docs/stage-2/00_stage_2_handoff.md"]
    missing = [x for x in needed if x not in seg]
    return not missing, ("historical C1 manifest-completeness note preserved"
                         if not missing else f"C1 §76.1 note missing: {missing}")


CHECKS: list[tuple[str, str, object]] = []


def register() -> None:
    for n in range(1, 88):
        fn = globals().get(f"check_{n:02d}")
        if fn:
            CHECKS.append((f"12B-{n:02d}", fn.__doc__.strip().splitlines()[0], fn))


register()


# --- fixtures --------------------------------------------------------------

def _replace_first(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1)


def fx_delete_rule(src):
    src["rulebook"] = src["rulebook"].replace(
        "**FP-011 — Server authority.**", "**Server authority.**")


def fx_duplicate_rule(src):
    line = next(l for l in src["rulebook"].splitlines()
                if l.startswith("**MA-001 —"))
    src["rulebook"] = src["rulebook"].replace(line, line + "\n" + line, 1)


def fx_add_v17(src):
    line = next(l for l in src["rulebook"].splitlines()
                if l.startswith("| `V-16` |"))
    extra = "| `V-17` | Fabricated class | x | x | x | x | x | x | `T1` | x | x | x | x |"
    src["rulebook"] = src["rulebook"].replace(line, line + "\n" + extra, 1)


def fx_six_states(src):
    src["rulebook"] = _replace_first(
        src["rulebook"], "Exactly five states exist",
        "Exactly six states exist, including `E6`")


def fx_behaviour_only(src):
    src["rulebook"] = _replace_first(
        src["rulebook"], "MUST NOT be treated as a violation",
        "MAY be treated as a violation")


def fx_drop_privacy(src):
    src["rulebook"] = re.sub(r"^\| `PUB` \|.*\n", "", src["rulebook"], count=1, flags=re.M)


def fx_add_actor(src):
    line = next(l for l in src["rulebook"].splitlines()
                if l.startswith("| Audit reviewer |"))
    src["rulebook"] = src["rulebook"].replace(
        line, line + "\n| Intruder | V | V | V | V | V | V | V | V | V |", 1)


def fx_add_role(src):
    line = next(l for l in src["rulebook"].splitlines()
                if l.startswith("| `R-EMG` |"))
    extra = "| `R-ROOT` | All | All | None | All | All | None | None | Some | None | None | Never |"
    src["rulebook"] = src["rulebook"].replace(line, line + "\n" + extra, 1)


def fx_add_t6(src):
    src["rulebook"] = _replace_first(
        src["rulebook"], "`T5` permanent measure",
        "`T5` permanent measure, `T6` deletion")


def fx_add_appeal_outcome(src):
    src["rulebook"] = _replace_first(
        src["rulebook"], "`UPHELD`, `REDUCED`, `REVERSED` or `REMANDED`",
        "`UPHELD`, `REDUCED`, `REVERSED`, `REMANDED` or `EXPUNGED`")


def fx_add_cor_type(src):
    src["rulebook"] = _replace_first(
        src["rulebook"], "No seventh type without a decision.",
        "A seventh type `PURGE` is allowed without a decision.")


def fx_drop_formula_field(src):
    src["formulas"] = re.sub(r"^20\. \*\*Approval\.\*\*.*\n", "",
                             src["formulas"], count=1, flags=re.M)


def fx_undeclared_var(src):
    src["formulas"] = _replace_first(
        src["formulas"],
        "5. **Variables.** `S_c` ∈ {1,2,3,4,5};",
        "5. **Variables.** `Q_undef` is an undefined variable; `S_c` ∈ {1,2,3,4,5};")


def fx_approve_open(src):
    src["requirements"] = _replace_first(
        src["requirements"],
        "| REQ-782 | Value may be corrected against either or both sides of an established beneficial flow | Operations |",
        "| REQ-782 | Value may be corrected against either or both sides of an established beneficial flow | Operations |")
    # Replace the status cell only on the REQ-782 row.
    lines = src["requirements"].splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| REQ-782 |"):
            parts = line.split("|")
            # cells: '', id, statement, type, pri, status, ...
            if len(parts) > 6:
                parts[5] = " Approved "
                lines[i] = "|".join(parts)
            break
    src["requirements"] = "\n".join(lines)


def fx_duplicate_req(src):
    line = next(l for l in src["requirements"].splitlines()
                if l.startswith("| REQ-764 |"))
    src["requirements"] = src["requirements"].replace(line, line + "\n" + line, 1)


def fx_break_pairing(src):
    src["requirements"] = _replace_first(
        src["requirements"], "12A-CR-050", "12A-CR-999")


def fx_drop_d187(src):
    src["decisions"] = re.sub(r"^\| D-187 \|.*\n", "", src["decisions"],
                              count=1, flags=re.M)


def fx_bad_mirror(src):
    lines = src["dd"].splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| DD-226 |"):
            lines[i] = line.replace("D-178", "D-999", 1)
            break
    src["dd"] = "\n".join(lines)


def fx_impl_claim(src):
    src["rulebook"] += "\nThe control is implemented and deployed.\n"


def fx_12c_section(src):
    src["rulebook"] += "\n## 20. Player journey library\n\nDetails.\n"


def fx_illegal_gate(src):
    src["acceptance"] = _replace_first(
        src["acceptance"], "| **PASS** |", "| **OK** |")


def fx_tally_drift(src):
    src["acceptance"] = _replace_first(
        src["acceptance"], "23 `PASS` · 3 `PARTIAL`", "24 `PASS` · 2 `PARTIAL`")


@dataclass
class Fixture:
    fid: str
    check: str
    positive: bool
    mutate: object
    reason: str
    expect: str


def fx_revert_002(src):
    src["formulas"] = src["formulas"].replace(
        "`C = min(max(V_obs − V_law, 0), B_i)`",
        "`C = min(max(V_law − V_obs, 0), B_i)`", 1)


def fx_readd_R(src):
    src["formulas"] = src["formulas"].replace(
        "`SEV = S_c + I_p + K − M`", "`SEV = S_c + I_p + R + K − M`", 1)


def fx_drop_A(src):
    src["formulas"] = src["formulas"].replace(
        "`Z = O + L + C + R + P + X + A`", "`Z = O + L + C + R + P + X`", 1)


def fx_drop_p14(src):
    src["formulas"] = re.sub(r"^\| `FP-P14`.*\n", "", src["formulas"],
                             count=1, flags=re.M)


def fx_bad_mapping(src):
    src["acceptance"] = src["acceptance"].replace(
        "| B-03 accounts and lifecycle | B-03 | `INT-001`, `INT-016` |",
        "| B-03 accounts and lifecycle | B-03 | `INT-003`, `INT-016` |", 1)


def fx_thin_int_fields(src):
    src["rulebook"] = src["rulebook"].replace(
        "| `INT-001` | B-12 ↔ B-03 accounts |",
        "| `INT-001` | B-12 ↔ B-03 accounts |", 1)
    # remove the last cell of the INT-001 field row
    lines = src["rulebook"].splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| `INT-001` | B-12 ↔ B-03 accounts |"):
            parts = line.split("|")
            lines[i] = "|".join(parts[:-2]) + "|"
            break
    src["rulebook"] = "\n".join(lines)


def fx_drop_attestation(src):
    src["log"] = re.sub(r"## 76\.[\s\S]*?(?=\n## 77\.|\Z)", "", src["log"], count=1)


def fx_drop_mapping_row(src):
    src["formulas"] = re.sub(r"^\| `F-FP-016` \| `FP-P10`.*\n", "",
                             src["formulas"], count=1, flags=re.M)


def fx_drop_p13(src):
    src["formulas"] = re.sub(r"^\| `FP-P13`.*\n", "", src["formulas"],
                             count=1, flags=re.M)


def fx_dup_p14(src):
    line = next(l for l in src["formulas"].splitlines()
                if l.startswith("| `FP-P14`"))
    src["formulas"] = src["formulas"].replace(line, line + "\n" + line, 1)


def fx_accept_12(src):
    src["acceptance"] = src["acceptance"].replace(
        "14 parameters (`FP-P01`–`FP-P14`)",
        "12 parameters (`FP-P01`–`FP-P12`)", 1)


def fx_accept_range12(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P12`", 1)


def fx_ctx_12(src):
    lines = src["ai_context"].splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("|") and \
                "20_fair_play_and_player_protection_formula_register.md" in ln:
            lines[i] = ln.replace("14 parameters", "12 parameters") \
                         .replace("FP-P01`…`FP-P14", "FP-P01`…`FP-P12")
            break
    src["ai_context"] = "\n".join(lines)


def fx_attest_122(src):
    src["log"] = src["log"].replace("**121 lines**", "**122 lines**", 1)


def fx_manifest_drop(src):
    # Remove the AI_CONTEXT row from the R1 §77.1 manifest only; the §76.1
    # historical note still mentions it, reproducing the audited bypass.
    src["log"] = re.sub(
        r"^\| `docs/AI_CONTEXT\.md` \| B-12 formula-register entry synchronized.*\n",
        "", src["log"], count=1, flags=re.M)


def fx_history_rewrite(src):
    src["log"] = src["log"].replace(
        "12 parameters `FP-P01`…`FP-P12`, none calibrated",
        "14 parameters `FP-P01`…`FP-P14`, none calibrated")
    src["log"] = src["log"].replace(
        "16 formulas and 12 parameters", "16 formulas and 14 parameters")
    src["log"] = src["log"].replace(
        "12 uncalibrated parameters", "14 uncalibrated parameters")


def _ctx_row_replace(src, old, new):
    lines = src["ai_context"].splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("|") and \
                "20_fair_play_and_player_protection_formula_register.md" in ln:
            lines[i] = ln.replace(old, new, 1)
            break
    src["ai_context"] = "\n".join(lines)


def fx_gate_incomplete_list(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`, `FP-P02`, `FP-P14`", 1)


def fx_gate_missing_p13(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P12`, `FP-P14`", 1)


def fx_gate_missing_p14(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P13`", 1)


def fx_gate_missing_mid(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P06`, `FP-P08`–`FP-P14`", 1)


def fx_ctx_missing_p13(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`",
                     "`FP-P01`…`FP-P12`, `FP-P14`")


def fx_ctx_range12(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`",
                     "`FP-P01`…`FP-P12`")


def fx_ctx_missing_mid(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`",
                     "`FP-P01`…`FP-P06`, `FP-P08`…`FP-P14`")


def fx_manifest_elsewhere(src):
    # Drop the §77.1 row but mention AI_CONTEXT in §77.2 instead.
    src["log"] = re.sub(
        r"^\| `docs/AI_CONTEXT\.md` \| B-12 formula-register entry synchronized.*\n",
        "", src["log"], count=1, flags=re.M)
    src["log"] = src["log"].replace(
        "### 77.2 Validation actually run",
        "### 77.2 Validation actually run\n\nNote: docs/AI_CONTEXT.md was reviewed.",
        1)


def fx_manifest_empty(src):
    i = src["log"].find("### 77.1")
    j = src["log"].find("### 77.2")
    seg = src["log"][i:j]
    seg = re.sub(r"^\| `docs/.*\n", "", seg, flags=re.M)
    src["log"] = src["log"][:i] + seg + src["log"][j:]


def fx_c1_note_drop(src):
    src["log"] = src["log"].replace(
        "**Manifest completeness correction (12B-C1-R1).**", "", 1)


def fx_gate_dup_p01(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P14`, `FP-P01`", 1)


def fx_gate_dup_mid(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P14`, `FP-P07`", 1)


def fx_gate_unexpected(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P14`, `FP-P15`", 1)


def fx_ctx_dup_p01(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`**",
                     "`FP-P01`…`FP-P14`, `FP-P01`**")


def fx_ctx_dup_mid(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`**",
                     "`FP-P01`…`FP-P14`, `FP-P07`**")


def fx_ctx_unexpected(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`**",
                     "`FP-P01`…`FP-P14`, `FP-P15`**")


def _ctx_add_second_entry(src, param_text):
    lines = src["ai_context"].splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("|") and \
                "20_fair_play_and_player_protection_formula_register.md" in ln:
            extra = ("| [stage-2/20_fair_play_and_player_protection_formula_register.md]"
                     "(stage-2/20_fair_play_and_player_protection_formula_register.md) "
                     f"| **B-12 formula register** {param_text} |")
            lines.insert(i + 1, extra)
            break
    src["ai_context"] = "\n".join(lines)


def fx_ctx_second_entry_12(src):
    _ctx_add_second_entry(src, "12 parameters `FP-P01`…`FP-P12`")


def fx_ctx_second_entry_incomplete14(src):
    _ctx_add_second_entry(src, "14 parameters `FP-P01`…`FP-P12`, `FP-P14`")


def fx_accept_stale_range_elsewhere(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Current formula-register range: `FP-P01`–`FP-P12`.\n\n## 10. Limitations",
        1)


def fx_accept_stale_count_elsewhere(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The register currently has 12 parameters.\n\n## 10. Limitations", 1)


def fx_accept_stale_fake_historical(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Historical note: current formula-register range `FP-P01`–`FP-P12`.\n\n"
        "## 10. Limitations", 1)


def fx_gate_duplicate_row(src):
    lines = src["acceptance"].splitlines()
    for i, ln in enumerate(lines):
        if re.match(r"^\|\s*`?P12B-19`?\s*\|", ln) and "Formula and parameter" in ln:
            lines.insert(i + 1, ln)
            break
    src["acceptance"] = "\n".join(lines)


def fx_gate_semicolon_unexpected(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P14`; `FP-P15`", 1)


def fx_gate_semicolon_duplicate(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P14`; `FP-P01`", 1)


def fx_gate_reordered(src):
    src["acceptance"] = src["acceptance"].replace(
        "`FP-P01`–`FP-P14`", "`FP-P14`, `FP-P01`–`FP-P13`", 1)


def fx_accept_stale_in_21(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 3. Ten-area coverage matrix",
        "Current formula-register range: `FP-P01`–`FP-P12`.\n\n"
        "## 3. Ten-area coverage matrix", 1)


def fx_accept_stale_unformatted(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Current formula-register range: FP-P01-FP-P12.\n\n## 10. Limitations", 1)


def fx_accept_stale_emdash(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Current formula-register range: FP-P01—FP-P12.\n\n## 10. Limitations", 1)


def _ctx_row_append(src, extra):
    lines = src["ai_context"].splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("|") and \
                "20_fair_play_and_player_protection_formula_register.md" in ln:
            lines[i] = ln.rstrip()[:-1] + extra + " |"
            break
    src["ai_context"] = "\n".join(lines)


def fx_ctx_outside_unexpected(src):
    _ctx_row_append(src, " Also FP-P15.")


def fx_ctx_outside_duplicate(src):
    _ctx_row_append(src, " Also FP-P01.")


def fx_canonical_duplicate(src):
    line = next(l for l in src["formulas"].splitlines()
                if l.startswith("| `FP-P14`"))
    src["formulas"] = src["formulas"].replace(line, line + "\n" + line, 1)


def fx_canonical_malformed(src):
    src["formulas"] = src["formulas"].replace("| `FP-P14`", "| `FP-PXX`", 1)


def fx_canonical_extra(src):
    line = next(l for l in src["formulas"].splitlines()
                if l.startswith("| `FP-P14`"))
    extra = "| `FP-P15` extra parameter | `F-FP-001` | undefined | Provisional | Owner | Test |"
    src["formulas"] = src["formulas"].replace(line, line + "\n" + extra, 1)


def fx_canonical_empty(src):
    src["formulas"] = re.sub(r"^\| `FP-P\d{2}`.*\n", "", src["formulas"],
                             flags=re.M)


def fx_canonical_missing(src):
    src["formulas"] = ""


def _gate_append(tok):
    def f(src):
        src["acceptance"] = src["acceptance"].replace(
            "`FP-P01`–`FP-P14`", "`FP-P01`–`FP-P14` " + tok, 1)
    return f


def _accept_insert(text):
    def f(src):
        src["acceptance"] = src["acceptance"].replace(
            "## 10. Limitations", text + "\n\n## 10. Limitations", 1)
    return f


fx_gate_malformed_xx = _gate_append("FP-PXX")
fx_gate_malformed_short = _gate_append("FP-P1")
fx_gate_malformed_long = _gate_append("FP-P001")
fx_gate_malformed_idsuffix = _gate_append("FP-P01X")
fx_accept_stale_individual = _accept_insert(
    "Current formula-register identifiers: FP-P01, FP-P12.")
fx_accept_stale_individual_backtick = _accept_insert(
    "Current formula-register identifiers: `FP-P01`, `FP-P12`.")
fx_accept_historical_current = _accept_insert(
    "Historical note: the formula register now contains only FP-P01–FP-P12.")
fx_accept_partial_current = _accept_insert(
    "Current formula-register identifiers: FP-P01, FP-P02.")
fx_accept_current_elsewhere = _accept_insert(
    "The formula register currently lists FP-P01–FP-P12.")
fx_accept_mixed_hist_current = _accept_insert(
    "Historical background: the register formerly had twelve entries, but it "
    "now contains only FP-P01–FP-P12.")
fx_accept_historical_valid = _accept_insert(
    "Historical record (2026-11-06): the register previously contained "
    "FP-P01–FP-P12.")
fx_accept_explanatory_valid = _accept_insert(
    "See parameter FP-P13 for the report-cluster window dependency.")
fx_accept_superseded_valid = _accept_insert(
    "Superseded definition (formerly FP-P01–FP-P12), replaced by the revised "
    "register.")


def fx_canonical_duplicate_unformatted(src):
    line = next(l for l in src["formulas"].splitlines()
                if l.startswith("| `FP-P14`"))
    extra = "| FP-P14 | duplicate unformatted | x | x | x | x |"
    src["formulas"] = src["formulas"].replace(line, line + "\n" + extra, 1)


def fx_ctx_key_unexpected(src):
    lines = src["ai_context"].splitlines()
    for i, l in enumerate(lines):
        if l.startswith("b12_fair_play:"):
            lines[i] = l + " Additional current parameter FP-P15."
            break
    src["ai_context"] = "\n".join(lines)


def _gate_add_row(gate_id):
    def f(src):
        lines = src["acceptance"].splitlines()
        for i, l in enumerate(lines):
            if re.match(r"^\|\s*`?P12B-19`?\s*\|", l) and "Formula and parameter" in l:
                lines.insert(i + 1, f"| `{gate_id}` | malformed duplicate gate "
                             "| x | x | x | **PASS** | x | x |")
                break
        src["acceptance"] = "\n".join(lines)
    return f


fx_gate_malformed_id = _gate_add_row("P12B-19X")
fx_gate_malformed_suffix = _gate_add_row("P12B-19A")


def _ctx_continuation(text):
    def f(src):
        lines = src["ai_context"].splitlines()
        for i, ln in enumerate(lines):
            if ln.startswith("|") and \
                    "20_fair_play_and_player_protection_formula_register.md" in ln:
                lines.insert(i + 1, text)
                break
        src["ai_context"] = "\n".join(lines)
    return f


fx_ctx_continuation_unexpected = _ctx_continuation(
    "Continuation: current B-12 parameters also include FP-P15.")
fx_ctx_continuation_duplicate = _ctx_continuation(
    "Note: FP-P01 is mentioned again in this entry.")
fx_ctx_continuation_incomplete = _ctx_continuation(
    "Current B-12 parameters: FP-P01, FP-P12.")
fx_accept_stale_set = _accept_insert(
    "Current formula-register parameter set: FP-P01, FP-P12.")
fx_accept_includes = _accept_insert(
    "The parameter set includes FP-P01, FP-P12.")
fx_accept_split_lines = _accept_insert(
    "Current formula-register identifiers:\nFP-P01, FP-P12.")
fx_gate_malformed_extra = _gate_append("FP-P01_extra")
fx_gate_malformed_bare = _gate_append("FP-P.")
fx_gate_malformed_hyphen = _gate_append("FP-P-01")
fx_accept_explanatory_individual = _accept_insert(
    "The severity index uses parameter FP-P01 as its base class weight.")
fx_accept_historical_comparison = _accept_insert(
    "Historical comparison: the earlier revision used FP-P01–FP-P12.")
fx_accept_explanatory_sentence = _accept_insert(
    "The rate allowance depends on FP-P07 and FP-P14.")


def fx_canonical_prose_duplicate(src):
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "FP-P14 is also defined here as a duplicate parameter.\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_canonical_prose_malformed(src):
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "FP-P-01 = a malformed definition.\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_canonical_missing_one(src):
    src["formulas"] = re.sub(r"^\| `FP-P07`.*\n", "", src["formulas"],
                             count=1, flags=re.M)


def fx_ctx_duplicate_row(src):
    lines = src["ai_context"].splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("|") and \
                "20_fair_play_and_player_protection_formula_register.md" in ln:
            lines.insert(i + 1, ln)
            break
    src["ai_context"] = "\n".join(lines)


CTX_REGISTER_PATH = "20_fair_play_and_player_protection_formula_register.md"


def _ctx_status_index(lines: list[str]) -> int:
    for i, ln in enumerate(lines):
        if ln.startswith("b12_fair_play:"):
            return i
    raise AssertionError("b12_fair_play status entry missing")


def _ctx_register_index(lines: list[str]) -> int:
    for i, ln in enumerate(lines):
        if ln.startswith("|") and CTX_REGISTER_PATH in ln:
            return i
    raise AssertionError("AI_CONTEXT B-12 register row missing")


def _ctx_apply(fn):
    def mutate(src):
        lines = src["ai_context"].splitlines()
        src["ai_context"] = "\n".join(fn(lines))
    return mutate


def fx_r7_status_duplicate(src):
    """R7-01: FP-P01 occurs twice inside the current b12_fair_play entry."""
    _ctx_apply(lambda lines: [
        (ln.replace("16 formulas, 14 uncalibrated parameters",
                    "16 formulas, 14 uncalibrated parameters "
                    "(`FP-P01`…`FP-P14`, `FP-P01`")
         if ln.startswith("b12_fair_play:") else ln) for ln in lines])(src)


def fx_r7_status_no_representation(src):
    """R7-02: the current B-12 entry states no parameter representation at all."""
    _ctx_apply(lambda lines: [
        (ln.replace("16 formulas, 14 uncalibrated parameters, ", "16 formulas, ")
         if ln.startswith("b12_fair_play:") else ln) for ln in lines])(src)


def fx_r7_paragraph_incomplete(src):
    """R7-03: a separate paragraph asserts an incomplete current collection."""
    def mutate(src):
        lines = src["ai_context"].splitlines()
        i = _ctx_register_index(lines)
        lines.insert(i + 1, "")
        lines.insert(i + 2, "The current B-12 formula parameters are `FP-P01` "
                            "and `FP-P12`.")
        src["ai_context"] = "\n".join(lines)
    mutate(src)


def fx_r7_status_continuation(src):
    """R7-04: continuation text of the status entry states a conflicting set."""
    def mutate(src):
        lines = src["ai_context"].splitlines()
        i = _ctx_status_index(lines)
        lines.insert(i + 1, "  also: the current B-12 parameters are "
                            "`FP-P01`, `FP-P12`.")
        src["ai_context"] = "\n".join(lines)
    mutate(src)


def fx_r7_extra_inventory_row(src):
    """R7-05: an additional B-12 parameter inventory row contradicts the source."""
    def mutate(src):
        lines = src["ai_context"].splitlines()
        i = _ctx_register_index(lines)
        lines.insert(i + 1, "| B-12 parameter inventory | secondary row: 14 "
                            "parameters `FP-P01`…`FP-P12`, `FP-P14` |")
        src["ai_context"] = "\n".join(lines)
    mutate(src)


def fx_r7_accept_21_incomplete(src):
    """R7-06: acceptance §2.1 states an incomplete current collection."""
    src["acceptance"] = src["acceptance"].replace(
        "The tally remains **23 PASS",
        "The current parameter list is `FP-P01`, `FP-P02`.\n\n"
        "The tally remains **23 PASS", 1)


def fx_r7_accept_disguised_present(src):
    """R7-07: historical wording that cannot disguise a present-state claim."""
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Historical record: the B-12 formula parameters remain `FP-P01` and "
        "`FP-P12`.\n\n## 10. Limitations", 1)


def fx_r7_canonical_duplicate_heading(src):
    """R7-08: a duplicate canonical definition hidden in a heading."""
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "#### `FP-P14` action-class rate factor (duplicate definition)\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_r7_malformed_canonical_heading(src):
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "#### `FP-P0X` malformed heading parameter\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_r7_unexpected_canonical_heading(src):
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "#### `FP-P15` additional heading parameter\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_r7_canonical_prose_across_formats(src):
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "`FP-P07` is defined as the configurable rate base `A_0`.\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_r7_canonical_prose_unexpected(src):
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "`FP-P15` is defined as the escalation factor.\n\n"
        "### 3.1 Formula-to-parameter mapping", 1)


def fx_r7_canonical_definition_outside_boundary(src):
    src["formulas"] = src["formulas"].replace(
        "## 3. Parameter register",
        "`FP-P16` is defined as an out-of-boundary parameter.\n\n"
        "## 3. Parameter register", 1)


def fx_r7_canonical_region_unclosed(src):
    """The definition region loses every closing boundary heading."""
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "Formula-to-parameter mapping (heading removed)", 1)
    src["formulas"] = src["formulas"].replace(
        "## 4. Non-claims", "Non-claims (heading removed)", 1)


def fx_r7_canonical_record_without_identity(src):
    """A mapping table is pulled into the region without leading identities."""
    src["formulas"] = src["formulas"].replace(
        "### 3.1 Formula-to-parameter mapping",
        "Formula-to-parameter mapping (heading removed)", 1)


def fx_r7_canonical_missing_p09(src):
    src["formulas"] = re.sub(r"^\| `FP-P09`.*\n", "", src["formulas"],
                             count=1, flags=re.M)


def fx_r7_canonical_reordered(src):
    lines = src["formulas"].splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("| `FP-P14`"):
            row = lines.pop(i)
            for j, ln2 in enumerate(lines):
                if ln2.startswith("| `FP-P02`"):
                    lines.insert(j, row)
                    break
            break
    src["formulas"] = "\n".join(lines)


def fx_r7_status_second_full_chain(src):
    """A second, correct complete enumeration inside the same entry."""
    lines = src["ai_context"].splitlines()
    i = _ctx_status_index(lines)
    lines[i] = (lines[i] + " Restatement: 14 parameters `FP-P01`…`FP-P14`.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_status_malformed(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_status_index(lines)
    lines[i] = lines[i] + (" Malformed forms FP-P1, FP-P001, FP-P-01, FP-P01X "
                           "and FP-P01_extra appear here.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_split_token(src):
    """An identifier broken across a wrapped continuation line."""
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Note: FP-\nP01 is cited again by this entry.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_three_conflicting_entries(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    extra = ("| [stage-2/20_fair_play_and_player_protection_formula_register.md]"
             "(stage-2/20_fair_play_and_player_protection_formula_register.md) "
             "| **B-12 formula register** 14 parameters `FP-P01`…`FP-P14` |")
    lines.insert(i + 1, extra)
    lines.insert(i + 2, extra)
    src["ai_context"] = "\n".join(lines)


def fx_r7_row_punctuation_duplicate(src):
    _ctx_row_replace(src, "`FP-P01`…`FP-P14`**", "`FP-P01`…`FP-P14`—`FP-P07`**")


def fx_r7_ctx_ambiguous_colon(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Parameter inventory note: `FP-P01`.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_accept_ambiguous_colon(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Parameter collection: `FP-P01`, `FP-P14`.\n\n## 10. Limitations", 1)


def fx_r7_accept_hidden_contaminated(src):
    """A malformed token must not be reduced to its valid prefix."""
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "Reference XFP-P01 is contaminated by a leading letter.\n\n"
        "## 10. Limitations", 1)


def fx_r7_accept_emdash_incomplete(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The current B-12 parameter range is FP-P01—FP-P13.\n\n"
        "## 10. Limitations", 1)


def fx_r7_accept_two_conflicting_sentences(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The current formula-register identifiers are `FP-P01`–`FP-P14`. "
        "The B-12 parameter set includes `FP-P01`, `FP-P02`.\n\n"
        "## 10. Limitations", 1)


def fx_r7_accept_multiple_in_one_sentence(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The authoritative parameter collection consists of `FP-P01`, `FP-P02`, "
        "`FP-P01`.\n\n## 10. Limitations", 1)


def fx_r7_accept_hist_plus_present_entry(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Historical note: the B-12 parameters now are "
                        "`FP-P01`, `FP-P12`.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_two_continuations(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "The current parameter list is `FP-P01`, `FP-P02`.")
    lines.insert(i + 2, "The complete B-12 parameter collection consists of "
                        "`FP-P03`, `FP-P04`.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_duplicate_inventory_rows(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "| B-12 parameter inventory | 14 parameters `FP-P01`…"
                        "`FP-P14` |")
    lines.insert(i + 2, "| B-12 parameter inventory | parameter set: `FP-P01`, "
                        "`FP-P02` |")
    src["ai_context"] = "\n".join(lines)


def fx_r7_accept_explanatory_unexpected(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The rate allowance depends on FP-P15.\n\n## 10. Limitations", 1)


def fx_r7_entry_bare_multiid_listing(src):
    """A bare multi-identifier listing attached to the authoritative entry."""
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Parameter note: `FP-P01`, `FP-P12`.")
    src["ai_context"] = "\n".join(lines)


# --- R7 positive fixtures --------------------------------------------------

def fx_r7_entry_explanatory_mention(src):
    """A legitimate explanatory mention inside the B-12 entry stays valid."""
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Continuation: `FP-P13` governs the report-cluster "
                        "window dependency; its value stays undefined.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_entry_individual_formula(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "`FP-P07` sets the rate base used by `F-FP-009`.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_entry_two_sentences(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "The report-cluster window `FP-P13` remains provisional; "
                        "the action-class rate factor `FP-P14` likewise stays "
                        "undefined.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_entry_dated_historical(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Historical record (2026-11-06): this entry listed "
                        "`FP-P01`…`FP-P12`.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_entry_superseded(src):
    lines = src["ai_context"].splitlines()
    i = _ctx_register_index(lines)
    lines.insert(i + 1, "Superseded definition (formerly `FP-P01`…`FP-P12`), "
                        "replaced by the revised register.")
    src["ai_context"] = "\n".join(lines)


def fx_r7_canonical_bold_format_variation(src):
    src["formulas"] = src["formulas"].replace(
        "| `FP-P07` rate base `A_0` |", "| **`FP-P07`** rate base `A_0` |", 1)


def fx_r7_accept_full_current_range_sentence(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The current B-12 formula-register identifiers are `FP-P01`–`FP-P14`.\n\n"
        "## 10. Limitations", 1)


def fx_r7_accept_single_explanatory(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "FP-P01 is used by the severity index calculation.\n\n"
        "## 10. Limitations", 1)


def fx_r7_accept_endash_unicode_full(src):
    src["acceptance"] = src["acceptance"].replace(
        "## 10. Limitations",
        "The authoritative parameter collection consists of FP-P01–FP-P14.\n\n"
        "## 10. Limitations", 1)


FIXTURES: list[Fixture] = [
    Fixture("12B-P01", "12B-03", True, None, "", "rule definitions"),
    Fixture("12B-P02", "12B-06", True, None, "", "violation classes"),
    Fixture("12B-P03", "12B-16", True, None, "", "privacy classes"),
    Fixture("12B-P04", "12B-19", True, None, "", "roles"),
    Fixture("12B-P05", "12B-23", True, None, "", "six tiers"),
    Fixture("12B-P06", "12B-27", True, None, "", "correction"),
    Fixture("12B-P07", "12B-42", True, None, "", "formulas"),
    Fixture("12B-P08", "12B-47", True, None, "", "part1"),
    Fixture("12B-P09", "12B-51", True, None, "", "Open rows"),
    Fixture("12B-P10", "12B-53", True, None, "", "decisions"),
    Fixture("12B-P11", "12B-61", True, None, "", "gates"),
    Fixture("12B-P12", "12B-62", True, None, "", "PASS="),
    Fixture("12B-N01", "12B-03", False, fx_delete_rule, "rule definitions", "344"),
    Fixture("12B-N02", "12B-04", False, fx_duplicate_rule, "MA-001", "duplicate"),
    Fixture("12B-N03", "12B-06", False, fx_add_v17, "violation classes", "V-17"),
    Fixture("12B-N04", "12B-10", False, fx_six_states, "five states", "five states"),
    Fixture("12B-N05", "12B-13", False, fx_behaviour_only, "MUST NOT be treated", "behaviour"),
    Fixture("12B-N06", "12B-16", False, fx_drop_privacy, "privacy classes", "8"),
    Fixture("12B-N07", "12B-17", False, fx_add_actor, "actor classes", "9"),
    Fixture("12B-N08", "12B-19", False, fx_add_role, "roles", "roles"),
    Fixture("12B-N09", "12B-23", False, fx_add_t6, "six tiers", "six tiers"),
    Fixture("12B-N10", "12B-25", False, fx_add_appeal_outcome, "four appeal outcomes", "four appeal outcomes"),
    Fixture("12B-N11", "12B-27", False, fx_add_cor_type, "six correction", "seventh"),
    Fixture("12B-N12", "12B-43", False, fx_drop_formula_field, "fields 1–20", "missing fields"),
    Fixture("12B-N13", "12B-46", False, fx_undeclared_var, "undefined", "undefined"),
    Fixture("12B-N14", "12B-50", False, fx_approve_open, "Approved=1", "Approved"),
    Fixture("12B-N15", "12B-47", False, fx_duplicate_req, "part1=107", "107"),
    Fixture("12B-N16", "12B-49", False, fx_break_pairing, "broken pairing", "REQ-813"),
    Fixture("12B-N17", "12B-53", False, fx_drop_d187, "missing", "187"),
    Fixture("12B-N18", "12B-54", False, fx_bad_mirror, "does not cite", "DD-226"),
    Fixture("12B-N19", "12B-59", False, fx_impl_claim, "implementation claim", "implemented"),
    Fixture("12B-N20", "12B-57", False, fx_12c_section, "12C section", "journey"),
    Fixture("12B-N21", "12B-61", False, fx_illegal_gate, "bad-status", "bad-status"),
    Fixture("12B-N22", "12B-62", False, fx_tally_drift, "PASS=23", "declared tally"),
    Fixture("12B-P13", "12B-63", True, None, "", "computes 40"),
    Fixture("12B-P14", "12B-64", True, None, "", "computes 5"),
    Fixture("12B-P15", "12B-65", True, None, "", "computes 6"),
    Fixture("12B-P16", "12B-66", True, None, "", "aligned"),
    Fixture("12B-P17", "12B-67", True, None, "", "FP-P14"),
    Fixture("12B-P18", "12B-68", True, None, "", "0 duplicates"),
    Fixture("12B-P19", "12B-69", True, None, "", "verified"),
    Fixture("12B-P20", "12B-70", True, None, "", "seven"),
    Fixture("12B-P21", "12B-71", True, None, "", "resolve"),
    Fixture("12B-P22", "12B-72", True, None, "", "archive"),
    Fixture("12B-P23", "12B-73", True, None, "", "attestation"),
    Fixture("12B-P24", "12B-74", True, None, "", "reassessment"),
    Fixture("12B-P25", "12B-75", True, None, "", "16 formulas"),
    Fixture("12B-N23", "12B-63", False, fx_revert_002, "reversed direction", "direction"),
    Fixture("12B-N24", "12B-64", False, fx_readd_R, "repetition term restored", "repetition term"),
    Fixture("12B-N25", "12B-66", False, fx_drop_A, "ADMIN_ADJUSTMENT dropped", "ADMIN_ADJUSTMENT"),
    Fixture("12B-N26", "12B-67", False, fx_drop_p14, "FP-P14 removed", "missing"),
    Fixture("12B-N27", "12B-69", False, fx_bad_mapping, "B-03 remapped", "B-03 lacks INT-001"),
    Fixture("12B-N28", "12B-70", False, fx_thin_int_fields, "field cell removed", "incomplete field rows"),
    Fixture("12B-N29", "12B-73", False, fx_drop_attestation, "attestation removed", "attestation missing"),
    Fixture("12B-N30", "12B-75", False, fx_drop_mapping_row, "mapping row removed", "15/16"),
    Fixture("12B-P26", "12B-76", True, None, "", "FP-P14"),
    Fixture("12B-P27", "12B-77", True, None, "", "cover all 14"),
    Fixture("12B-P28", "12B-78", True, None, "", "covers all 14"),
    Fixture("12B-P29", "12B-79", True, None, "", "matches policy"),
    Fixture("12B-P30", "12B-80", True, None, "", "§77.1"),
    Fixture("12B-P31", "12B-81", True, None, "", "preserved"),
    Fixture("12B-N31", "12B-76", False, fx_drop_p13, "FP-P13 removed", "missing"),
    Fixture("12B-N32", "12B-76", False, fx_dup_p14, "FP-P14 duplicated", "duplicate"),
    Fixture("12B-N33", "12B-77", False, fx_accept_12, "acceptance reverted to 12", "stale 12-parameter"),
    Fixture("12B-N34", "12B-77", False, fx_accept_range12, "range ends at FP-P12", "missing parameters"),
    Fixture("12B-N35", "12B-78", False, fx_ctx_12, "AI_CONTEXT reverted to 12", "does not report 14"),
    Fixture("12B-N36", "12B-79", False, fx_attest_122, "attestation line count wrong", "incorrect"),
    Fixture("12B-N37", "12B-80", False, fx_manifest_drop, "AI_CONTEXT dropped from §77.1", "missing"),
    Fixture("12B-N38", "12B-81", False, fx_history_rewrite, "historical record rewritten", "rewritten"),
    Fixture("12B-P32", "12B-82", True, None, "", "preserved"),
    Fixture("12B-N39", "12B-77", False, fx_gate_incomplete_list, "gate lists only FP-P01/02/14", "missing parameters"),
    Fixture("12B-N40", "12B-77", False, fx_gate_missing_p13, "gate omits FP-P13 keeps FP-P14", "FP-P13"),
    Fixture("12B-N41", "12B-77", False, fx_gate_missing_p14, "gate omits FP-P14", "FP-P14"),
    Fixture("12B-N42", "12B-77", False, fx_gate_missing_mid, "gate omits intermediate FP-P07", "FP-P07"),
    Fixture("12B-N43", "12B-78", False, fx_ctx_missing_p13, "AI_CONTEXT omits FP-P13 keeps 14 claim", "FP-P13"),
    Fixture("12B-N44", "12B-78", False, fx_ctx_range12, "AI_CONTEXT range ends FP-P12", "missing parameters"),
    Fixture("12B-N45", "12B-78", False, fx_ctx_missing_mid, "AI_CONTEXT omits intermediate FP-P07", "FP-P07"),
    Fixture("12B-N46", "12B-80", False, fx_manifest_elsewhere, "AI_CONTEXT only outside §77.1", "missing"),
    Fixture("12B-N47", "12B-80", False, fx_manifest_empty, "§77.1 manifest emptied", "empty or malformed"),
    Fixture("12B-N48", "12B-82", False, fx_c1_note_drop, "C1 completeness note removed", "missing"),
    Fixture("12B-P33", "12B-77", True, None, "", "cover all 14"),
    Fixture("12B-N49", "12B-77", False, fx_gate_dup_p01, "gate duplicates FP-P01", "duplicate parameter FP-P01"),
    Fixture("12B-N50", "12B-77", False, fx_gate_dup_mid, "gate duplicates FP-P07", "duplicate parameter FP-P07"),
    Fixture("12B-N51", "12B-77", False, fx_gate_unexpected, "gate adds unexpected FP-P15", "unexpected parameters: FP-P15"),
    Fixture("12B-N52", "12B-78", False, fx_ctx_dup_p01, "AI_CONTEXT duplicates FP-P01", "duplicate parameter FP-P01"),
    Fixture("12B-N53", "12B-78", False, fx_ctx_dup_mid, "AI_CONTEXT duplicates FP-P07", "duplicate parameter FP-P07"),
    Fixture("12B-N54", "12B-78", False, fx_ctx_unexpected, "AI_CONTEXT adds unexpected FP-P15", "unexpected parameters: FP-P15"),
    Fixture("12B-N55", "12B-78", False, fx_ctx_second_entry_12, "second current-state entry reports 12", "conflicting"),
    Fixture("12B-N56", "12B-78", False, fx_ctx_second_entry_incomplete14, "second entry incomplete 14 claim", "conflicting"),
    Fixture("12B-N57", "12B-77", False, fx_accept_stale_range_elsewhere, "stale range elsewhere", "stale current-state parameter range"),
    Fixture("12B-N58", "12B-77", False, fx_accept_stale_count_elsewhere, "stale 12 count elsewhere", "stale 12-parameter"),
    Fixture("12B-N59", "12B-77", False, fx_accept_stale_fake_historical, "fake-historical current claim", "stale current-state parameter range"),
    Fixture("12B-R4-01", "12B-77", False, fx_gate_duplicate_row, "duplicate complete P12B-19 row", "exactly one"),
    Fixture("12B-R4-02", "12B-77", False, fx_gate_semicolon_unexpected, "unexpected FP-P15 after semicolon", "unexpected parameters: FP-P15"),
    Fixture("12B-R4-03", "12B-77", False, fx_gate_semicolon_duplicate, "duplicate FP-P01 after semicolon", "duplicate parameter FP-P01"),
    Fixture("12B-R4-04", "12B-77", False, fx_accept_stale_in_21, "stale current range inside §2.1", "stale current-state parameter range"),
    Fixture("12B-R4-05", "12B-77", False, fx_accept_stale_unformatted, "unformatted stale FP-P01-FP-P12", "stale current-state parameter range"),
    Fixture("12B-R4-06", "12B-78", False, fx_ctx_outside_unexpected, "unexpected FP-P15 outside AI_CONTEXT chain", "unexpected parameters: FP-P15"),
    Fixture("12B-R4-07", "12B-78", False, fx_ctx_outside_duplicate, "duplicate FP-P01 outside AI_CONTEXT chain", "duplicate parameter FP-P01"),
    Fixture("12B-N60", "12B-77", False, fx_gate_reordered, "reordered gate identifiers", "out of canonical order"),
    Fixture("12B-N61", "12B-76", False, fx_canonical_duplicate, "duplicate canonical definition", "duplicate canonical"),
    Fixture("12B-N62", "12B-76", False, fx_canonical_malformed, "malformed canonical ID", "malformed canonical"),
    Fixture("12B-N63", "12B-77", False, fx_canonical_extra, "extra canonical parameter desyncs documents", "missing parameters: FP-P15"),
    Fixture("12B-N64", "12B-76", False, fx_canonical_empty, "empty canonical collection", "no parameter definitions"),
    Fixture("12B-N65", "12B-76", False, fx_canonical_missing, "missing canonical register", "missing or unreadable"),
    Fixture("12B-N66", "12B-77", False, fx_accept_stale_emdash, "em-dash stale range", "stale current-state parameter range"),
    Fixture("12B-R5-01", "12B-77", False, fx_gate_malformed_xx, "malformed FP-PXX in gate", "malformed parameter identifier"),
    Fixture("12B-R5-02", "12B-77", False, fx_accept_stale_individual, "stale individual IDs", "stale current-state parameter identifiers"),
    Fixture("12B-R5-03", "12B-77", False, fx_accept_stale_individual_backtick, "stale backticked comma IDs", "stale current-state parameter identifiers"),
    Fixture("12B-R5-04", "12B-76", False, fx_canonical_duplicate_unformatted, "unformatted canonical duplicate", "duplicate canonical"),
    Fixture("12B-R5-05", "12B-77", False, fx_accept_historical_current, "historical wording around current claim", "stale current-state parameter range"),
    Fixture("12B-R5-06", "12B-78", False, fx_ctx_key_unexpected, "unexpected param in b12 registry key", "unexpected parameters: FP-P15"),
    Fixture("12B-R5-07", "12B-61", False, fx_gate_malformed_id, "malformed P12B-19X gate row", "malformed gate identifier"),
    Fixture("12B-R5-08", "12B-45", True, None, "", "source-derived"),
    Fixture("12B-R5-09", "12B-76", False, fx_canonical_malformed, "malformed canonical definition", "malformed canonical"),
    Fixture("12B-R5-10", "12B-76", False, fx_canonical_duplicate, "formatted canonical duplicate", "duplicate canonical"),
    Fixture("12B-R5-11", "12B-77", False, fx_accept_range12, "missing parameters in gate", "missing parameters"),
    Fixture("12B-R5-12", "12B-77", False, fx_accept_partial_current, "partial current representation", "stale current-state parameter identifiers"),
    Fixture("12B-R5-13", "12B-77", False, fx_gate_semicolon_unexpected, "unexpected valid-looking FP-P15", "unexpected parameters: FP-P15"),
    Fixture("12B-R5-14", "12B-77", False, fx_accept_current_elsewhere, "current assertion elsewhere", "stale current-state parameter range"),
    Fixture("12B-R5-15", "12B-61", False, fx_gate_malformed_suffix, "malformed gate suffix P12B-19A", "malformed gate identifier"),
    Fixture("12B-R5-16", "12B-78", False, fx_ctx_second_entry_12, "conflicting current B-12 entry", "conflicting"),
    Fixture("12B-R5-17", "12B-77", True, fx_accept_historical_valid, "genuine historical range accepted", "cover all 14"),
    Fixture("12B-R5-18", "12B-77", True, fx_accept_explanatory_valid, "legitimate explanatory reference accepted", "cover all 14"),
    Fixture("12B-R5-19", "12B-77", True, fx_accept_superseded_valid, "superseded historical definition accepted", "cover all 14"),
    Fixture("12B-R5-20", "12B-77", False, fx_accept_mixed_hist_current, "mixed historical and current assertion", "stale current-state parameter range"),
    Fixture("12B-N67", "12B-77", False, fx_gate_malformed_short, "malformed FP-P1", "malformed parameter identifier"),
    Fixture("12B-N68", "12B-77", False, fx_gate_malformed_long, "malformed FP-P001", "malformed parameter identifier"),
    Fixture("12B-N69", "12B-77", False, fx_gate_malformed_idsuffix, "malformed FP-P01X", "malformed parameter identifier"),
    Fixture("12B-R6-01", "12B-78", False, fx_ctx_continuation_unexpected, "AI_CONTEXT continuation FP-P15", "unexpected parameters: FP-P15"),
    Fixture("12B-R6-02", "12B-78", False, fx_ctx_continuation_duplicate, "AI_CONTEXT continuation duplicate FP-P01", "duplicate parameter FP-P01"),
    Fixture("12B-R6-03", "12B-78", False, fx_ctx_continuation_incomplete, "AI_CONTEXT continuation incomplete list", "stale current-state parameter identifiers"),
    Fixture("12B-R6-04", "12B-77", False, fx_accept_stale_set, "stale parameter set", "stale current-state parameter identifiers"),
    Fixture("12B-R6-05", "12B-77", False, fx_accept_includes, "stale claim using includes", "stale current-state parameter identifiers"),
    Fixture("12B-R6-06", "12B-77", False, fx_accept_historical_current, "historical wording around current claim", "stale current-state parameter range"),
    Fixture("12B-R6-07", "12B-77", False, fx_accept_split_lines, "assertion split across lines", "stale current-state parameter identifiers"),
    Fixture("12B-R6-08", "12B-77", False, fx_gate_malformed_extra, "malformed FP-P01_extra", "malformed parameter identifier"),
    Fixture("12B-R6-09", "12B-77", False, fx_gate_malformed_bare, "malformed bare FP-P", "malformed parameter identifier"),
    Fixture("12B-R6-10", "12B-76", False, fx_canonical_prose_duplicate, "prose duplicate canonical definition", "duplicate canonical"),
    Fixture("12B-R6-11", "12B-76", False, fx_canonical_prose_malformed, "prose malformed canonical definition", "malformed canonical"),
    Fixture("12B-R6-12", "12B-76", False, fx_canonical_duplicate_unformatted, "duplicate canonical without backticks", "duplicate canonical"),
    Fixture("12B-R6-13", "12B-77", False, fx_accept_current_elsewhere, "current assertion outside acceptance chain", "stale current-state parameter range"),
    Fixture("12B-R6-14", "12B-78", False, fx_ctx_key_unexpected, "assertion outside AI_CONTEXT formula row", "unexpected parameters: FP-P15"),
    Fixture("12B-R6-15", "12B-78", False, fx_ctx_second_entry_12, "multiple conflicting current representations", "conflicting"),
    Fixture("12B-R6-16", "12B-77", False, fx_gate_malformed_idsuffix, "malformed token appended to valid chain", "malformed parameter identifier"),
    Fixture("12B-R6-17", "12B-77", False, fx_gate_semicolon_duplicate, "duplicate ID separated by punctuation", "duplicate parameter FP-P01"),
    Fixture("12B-R6-18", "12B-77", False, fx_gate_reordered, "reordered canonical representation", "out of canonical order"),
    Fixture("12B-R6-19", "12B-76", False, fx_canonical_missing_one, "missing canonical definition", "missing parameters"),
    Fixture("12B-R6-20", "12B-77", False, fx_gate_duplicate_row, "duplicate exact gate identifier", "exactly one"),
    Fixture("12B-R6-21", "12B-61", False, fx_gate_malformed_id, "malformed duplicate gate identifier", "malformed gate identifier"),
    Fixture("12B-R6-22", "12B-78", False, fx_ctx_duplicate_row, "ambiguous authoritative block boundary", "conflicting"),
    Fixture("12B-R6-23", "12B-76", True, None, "", "unique parameters"),
    Fixture("12B-R6-24", "12B-77", True, fx_accept_historical_valid, "dated historical range accepted", "cover all 14"),
    Fixture("12B-R6-25", "12B-77", True, fx_accept_superseded_valid, "superseded historical representation accepted", "cover all 14"),
    Fixture("12B-R6-26", "12B-77", True, fx_accept_explanatory_valid, "legitimate explanatory FP-P01 accepted", "cover all 14"),
    Fixture("12B-R6-27", "12B-77", True, fx_accept_explanatory_individual, "individual formula parameter explanation accepted", "cover all 14"),
    Fixture("12B-R6-28", "12B-77", True, fx_accept_historical_comparison, "historical comparison with old IDs accepted", "cover all 14"),
    Fixture("12B-R6-29", "12B-76", True, None, "", "unique parameters"),
    Fixture("12B-R6-30", "12B-77", True, fx_accept_explanatory_sentence, "explanatory sentence with parameter IDs accepted", "cover all 14"),
    Fixture("12B-N70", "12B-77", False, fx_gate_malformed_hyphen, "malformed FP-P-01", "malformed parameter identifier"),
    # --- R7: the eight independently reproduced bypasses --------------------
    Fixture("12B-R7-01", "12B-78", False, fx_r7_status_duplicate,
            "duplicate FP-P01 in the current B-12 entry", "duplicate parameter FP-P01"),
    Fixture("12B-R7-02", "12B-78", False, fx_r7_status_no_representation,
            "no parameter representation in the current B-12 entry",
            "carries no authoritative parameter representation"),
    Fixture("12B-R7-03", "12B-78", False, fx_r7_paragraph_incomplete,
            "incomplete current parameter assertion in AI_CONTEXT",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-04", "12B-78", False, fx_r7_status_continuation,
            "continuation text with a conflicting parameter assertion",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-05", "12B-78", False, fx_r7_extra_inventory_row,
            "additional B-12 parameter inventory row", "missing parameters: FP-P13"),
    Fixture("12B-R7-06", "12B-77", False, fx_r7_accept_21_incomplete,
            "incomplete collection in acceptance §2.1",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-07", "12B-77", False, fx_r7_accept_disguised_present,
            "historical wording disguising a present-state assertion",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-08", "12B-76", False, fx_r7_canonical_duplicate_heading,
            "duplicate canonical definition in a heading",
            "duplicate canonical parameter definition"),
    # --- R7: additional negative fixtures -----------------------------------
    Fixture("12B-R7-N01", "12B-78", False, fx_r7_three_conflicting_entries,
            "multiple conflicting B-12 entries", "conflicting"),
    Fixture("12B-R7-N02", "12B-78", False, fx_r7_status_second_full_chain,
            "second correct complete enumeration in the same entry",
            "duplicate parameter FP-P01"),
    Fixture("12B-R7-N03", "12B-78", False, fx_r7_status_malformed,
            "multiple malformed identifier forms in the status entry",
            "malformed parameter identifier"),
    Fixture("12B-R7-N04", "12B-78", False, fx_r7_split_token,
            "identifier split across a continuation line", "duplicate parameter FP-P01"),
    Fixture("12B-R7-N05", "12B-78", False, fx_r7_row_punctuation_duplicate,
            "duplicate identifier separated by an em dash",
            "duplicate parameter FP-P07"),
    Fixture("12B-R7-N06", "12B-78", False, fx_r7_ctx_ambiguous_colon,
            "ambiguous colon enumeration in the entry",
            "ambiguous current-state parameter assertion"),
    Fixture("12B-R7-N07", "12B-77", False, fx_r7_accept_ambiguous_colon,
            "ambiguous colon enumeration in acceptance",
            "ambiguous current-state parameter assertion"),
    Fixture("12B-R7-N08", "12B-77", False, fx_r7_accept_hidden_contaminated,
            "token contaminated by a leading letter",
            "malformed parameter identifier"),
    Fixture("12B-R7-N09", "12B-77", False, fx_r7_accept_emdash_incomplete,
            "em-dash range with an incomplete collection",
            "stale current-state parameter range"),
    Fixture("12B-R7-N10", "12B-77", False, fx_r7_accept_two_conflicting_sentences,
            "two sentences with conflicting representations",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-N11", "12B-77", False, fx_r7_accept_multiple_in_one_sentence,
            "duplicate identifier inside one representation",
            "duplicate parameter FP-P01"),
    Fixture("12B-R7-N12", "12B-77", False, fx_r7_accept_explanatory_unexpected,
            "unexpected identifier in an explanatory sentence",
            "unexpected parameters: FP-P15"),
    Fixture("12B-R7-N13", "12B-78", False, fx_r7_accept_hist_plus_present_entry,
            "historical qualifier combined with a present-tense claim",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-N14", "12B-78", False, fx_r7_two_continuations,
            "multiple continuation lines with conflicting claims",
            "stale current-state parameter identifiers"),
    Fixture("12B-R7-N15", "12B-78", False, fx_r7_duplicate_inventory_rows,
            "duplicate parameter inventory rows", "duplicate parameter FP-P01"),
    Fixture("12B-R7-N16", "12B-76", False, fx_r7_malformed_canonical_heading,
            "malformed canonical definition in a heading",
            "malformed canonical parameter ID"),
    Fixture("12B-R7-N17", "12B-76", False, fx_r7_canonical_prose_across_formats,
            "duplicate canonical definition across table and prose",
            "duplicate canonical parameter definition"),
    Fixture("12B-R7-N18", "12B-76", False, fx_r7_canonical_definition_outside_boundary,
            "definition record outside the canonical boundary",
            "outside the parameter-register boundary"),
    Fixture("12B-R7-N19", "12B-76", False, fx_r7_canonical_region_unclosed,
            "canonical region boundary cannot be determined",
            "no closing boundary heading"),
    Fixture("12B-R7-N20", "12B-76", False, fx_r7_canonical_missing_p09,
            "missing canonical identifier", "missing parameters: FP-P09"),
    Fixture("12B-R7-N21", "12B-76", False, fx_r7_canonical_reordered,
            "reordered canonical definitions", "order does not ascend"),
    Fixture("12B-R7-N22", "12B-77", False, fx_r7_unexpected_canonical_heading,
            "unexpected canonical identifier changes the derived collection",
            "missing parameters: FP-P15"),
    Fixture("12B-R7-N23", "12B-77", False, fx_r7_canonical_prose_unexpected,
            "additional prose definition changes the count",
            "missing parameters: FP-P15"),
    Fixture("12B-R7-N24", "12B-76", False, fx_canonical_empty,
            "empty canonical extraction", "no parameter definitions"),
    Fixture("12B-R7-N25", "12B-84", False, fx_canonical_missing,
            "missing formula register", "missing or unreadable"),
    Fixture("12B-R7-N26", "12B-83", False, fx_gate_malformed_extra,
            "occurrence accounting rejects a malformed token",
            "malformed parameter identifier"),
    Fixture("12B-R7-N27", "12B-85", False, fx_r7_accept_ambiguous_colon,
            "ambiguity audit fails closed", "ambiguous"),
    Fixture("12B-R7-N28", "12B-87", False, fx_r7_accept_21_incomplete,
            "representation equality detects drift", "differ from the"),
    Fixture("12B-R7-N29", "12B-76", False, fx_r7_canonical_record_without_identity,
            "parameter-bearing record without a leading identity",
            "without a leading identifier"),
    Fixture("12B-R7-N30", "12B-78", False, fx_r7_entry_bare_multiid_listing,
            "bare multi-identifier listing attached to the entry",
            "ambiguous current-state parameter assertion"),
    # --- R7: additional positive fixtures ------------------------------------
    Fixture("12B-R7-P01", "12B-83", True, None, "", "occurrences accounted"),
    Fixture("12B-R7-P02", "12B-84", True, None, "", "definition candidates"),
    Fixture("12B-R7-P03", "12B-85", True, None, "", "no ambiguous"),
    Fixture("12B-R7-P04", "12B-86", True, None, "", "anchored historical"),
    Fixture("12B-R7-P05", "12B-87", True, None, "", "representations equal"),
    Fixture("12B-R7-P06", "12B-78", True, fx_r7_entry_explanatory_mention,
            "legitimate parameter mention in an AI_CONTEXT continuation",
            "covers all 14"),
    Fixture("12B-R7-P07", "12B-78", True, fx_r7_entry_individual_formula,
            "individual formula parameter explanation stays valid",
            "covers all 14"),
    Fixture("12B-R7-P08", "12B-78", True, fx_r7_entry_two_sentences,
            "valid explanatory paragraph inside the B-12 entry",
            "covers all 14"),
    Fixture("12B-R7-P09", "12B-78", True, fx_r7_entry_dated_historical,
            "genuinely dated historical range inside the entry",
            "covers all 14"),
    Fixture("12B-R7-P10", "12B-78", True, fx_r7_entry_superseded,
            "explicitly superseded collection inside the entry",
            "covers all 14"),
    Fixture("12B-R7-P11", "12B-76", True, fx_r7_canonical_bold_format_variation,
            "legitimate canonical formatting variation", "unique parameters"),
    Fixture("12B-R7-P12", "12B-77", True, fx_r7_accept_full_current_range_sentence,
            "semantically equivalent complete current claim", "cover all 14"),
    Fixture("12B-R7-P13", "12B-77", True, fx_r7_accept_single_explanatory,
            "single explanatory FP-P01 reference", "cover all 14"),
    Fixture("12B-R7-P14", "12B-77", True, fx_r7_accept_endash_unicode_full,
            "unicode range separator with a complete collection", "cover all 14"),
]


# --- end-to-end mutation audit (R7) ----------------------------------------
#
# The fixture harness mutates the parsed corpus. This audit is deliberately
# stronger: it copies every file the production validator reads into an
# isolated tree, applies one mutation to the file on disk, and runs this very
# validator as a subprocess. Acceptance therefore never rests on a helper-level
# test; it rests on the complete production validator's own exit code.

AUDIT_INPUTS = [p for p in FILES.values()] + [
    PROMPT_ARCHIVE, PROMPT_INDEX, POLICY,
    STAGE2 / "01_stage_2_prompt_roadmap.md",
]

# (label, mutation, check that must reject it, reason substring)
AUDIT_MUTATIONS: list[tuple[str, object, str, str]] = [
    ("R7-01", fx_r7_status_duplicate, "12B-78", "duplicate parameter FP-P01"),
    ("R7-02", fx_r7_status_no_representation, "12B-78",
     "carries no authoritative parameter representation"),
    ("R7-03", fx_r7_paragraph_incomplete, "12B-78",
     "stale current-state parameter identifiers"),
    ("R7-04", fx_r7_status_continuation, "12B-78", "12B-78"),
    ("R7-05", fx_r7_extra_inventory_row, "12B-78", "missing parameters: FP-P13"),
    ("R7-06", fx_r7_accept_21_incomplete, "12B-77",
     "stale current-state parameter identifiers"),
    ("R7-07", fx_r7_accept_disguised_present, "12B-77",
     "stale current-state parameter identifiers"),
    ("R7-08", fx_r7_canonical_duplicate_heading, "12B-76",
     "duplicate canonical parameter definition"),
    ("R7-N01", fx_r7_three_conflicting_entries, "12B-78", "conflicting"),
    ("R7-N03", fx_r7_status_malformed, "12B-78", "malformed parameter identifier"),
    ("R7-N04", fx_r7_split_token, "12B-78", "duplicate parameter FP-P01"),
    ("R7-N06", fx_r7_ctx_ambiguous_colon, "12B-78", "ambiguous"),
    ("R7-N08", fx_r7_accept_hidden_contaminated, "12B-83",
     "malformed parameter identifier"),
    ("R7-N16", fx_r7_malformed_canonical_heading, "12B-76",
     "malformed canonical parameter ID"),
    ("R7-N17", fx_r7_canonical_prose_across_formats, "12B-76",
     "duplicate canonical parameter definition"),
    ("R7-N18", fx_r7_canonical_definition_outside_boundary, "12B-76",
     "outside the parameter-register boundary"),
    ("R7-N19", fx_r7_canonical_region_unclosed, "12B-76",
     "no closing boundary heading"),
    ("R7-N21", fx_r7_canonical_reordered, "12B-76", "order does not ascend"),
    ("R7-N22", fx_r7_unexpected_canonical_heading, "12B-77",
     "missing parameters: FP-P15"),
    ("R7-P06", fx_r7_entry_explanatory_mention, "", "baseline remains accepted"),
    ("R7-P08", fx_r7_entry_two_sentences, "", "baseline remains accepted"),
    ("R7-P09", fx_r7_entry_dated_historical, "", "baseline remains accepted"),
    ("R7-P12", fx_r7_accept_full_current_range_sentence, "",
     "baseline remains accepted"),
]


def run_mutation_audit(model: Model, verbose: bool) -> int:
    import shutil
    import subprocess
    import tempfile

    base = copy.deepcopy(model.src)
    root = Path(tempfile.mkdtemp(prefix="12B-R7-audit-"))
    rejected = accepted = bad = 0
    try:
        for rel in AUDIT_INPUTS:
            dst = root / "docs" / rel.relative_to(DOCS)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if rel.exists():
                shutil.copyfile(rel, dst)
        self_copy = root / "docs" / Path(__file__).resolve().relative_to(DOCS)
        self_copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(Path(__file__).resolve(), self_copy)

        for label, mutate, expect_check, expect_reason in AUDIT_MUTATIONS:
            src = copy.deepcopy(base)
            mutate(src)
            for key, text in src.items():
                dst = root / "docs" / FILES[key].relative_to(DOCS)
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(text, encoding="utf-8")
            proc = subprocess.run([sys.executable, str(self_copy)],
                                  capture_output=True, text=True, timeout=600)
            out = proc.stdout + proc.stderr
            crashed = proc.returncode not in (0, 1)
            if crashed:
                bad += 1
                print(f"[FAIL] audit {label}: validator exited "
                      f"{proc.returncode}: {out.strip()[:200]}")
                continue
            if proc.returncode == 0:
                if expect_check:
                    bad += 1
                    print(f"[FAIL] audit {label}: the complete production "
                          "validator ACCEPTED the mutation (exit 0)")
                else:
                    accepted += 1
                    if verbose:
                        print(f"[PASS] audit {label}: legitimate content still "
                              "passes the complete validator")
                continue
            hit = next((ln for ln in out.splitlines()
                        if ln.startswith("[FAIL]") and expect_check
                        and ln.split()[1] == expect_check
                        and expect_reason.lower() in ln.lower()), None)
            if expect_check and not hit:
                bad += 1
                print(f"[FAIL] audit {label}: rejected, but not by "
                      f"{expect_check} for '{expect_reason}': "
                      + " | ".join(ln for ln in out.splitlines()
                                   if ln.startswith("[FAIL]"))[:260])
                continue
            rejected += 1
            if verbose:
                print(f"[PASS] audit {label}: complete validator rejected it"
                      + (f" via {expect_check}" if expect_check else ""))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    total = len(AUDIT_MUTATIONS)
    print(f"\nMUTATION AUDIT: {rejected + accepted}/{total} mutations handled by "
          f"the production validator as subprocess ({rejected} rejected for the "
          f"intended reason, {accepted} legitimate variants accepted); {bad} wrong")
    return 0 if bad == 0 else 1


def run_checks(model: Model, verbose: bool) -> int:
    failed = 0
    for cid, desc, fn in CHECKS:
        try:
            ok, detail = fn(model)
        except Exception as exc:  # a crashing check is a failure, not an excuse
            ok, detail = False, f"check raised {type(exc).__name__}: {exc}"
        if verbose or not ok:
            print(f"[{'PASS' if ok else 'FAIL'}] {cid} {desc} — {detail}")
        if not ok:
            failed += 1
    print(f"\nCHECKS: {len(CHECKS) - failed}/{len(CHECKS)} passed; {failed} failed")
    return 0 if failed == 0 else 1


def evaluate(model: Model, mutate) -> tuple[list[tuple[str, bool, str]], list[str]]:
    """Run the complete production check registry over an isolated corpus copy."""
    target = copy.deepcopy(model)
    target.src = copy.deepcopy(model.src)
    if mutate is not None:
        mutate(target.src)
        target.rebuild()
    results: list[tuple[str, bool, str]] = []
    raised: list[str] = []
    for cid, _desc, fn in CHECKS:
        try:
            ok, detail = fn(target)
        except Exception as exc:
            ok, detail = False, f"check raised {type(exc).__name__}: {exc}"
            raised.append(cid)
        results.append((cid, ok, detail))
    return results, raised


def run_fixtures(model: Model, verbose: bool) -> int:
    """Every fixture runs the complete validator, never a single helper.

    A negative fixture counts only when the named check rejects the mutation
    for the intended reason without raising; a positive fixture counts only
    when the whole corpus passes every check.
    """
    pos = neg = bad = 0
    for fx in FIXTURES:
        results, raised = evaluate(model, fx.mutate)
        detail_map = {cid: (ok, detail) for cid, ok, detail in results}
        failed = [cid for cid, ok, _ in results if not ok]
        ok_named, detail = detail_map.get(fx.check, (False, "check missing"))
        if fx.positive:
            if raised:
                bad += 1
                print(f"[FAIL] {fx.fid} the complete validator raised in "
                      f"{raised[:3]}")
                continue
            if failed or not ok_named or fx.expect not in detail:
                bad += 1
                print(f"[FAIL] {fx.fid} expected the complete validator to pass "
                      f"and {fx.check} to report '{fx.expect}', got "
                      f"failed={failed[:4]}: {detail[:160]}")
                continue
            pos += 1
            if verbose:
                print(f"[PASS] {fx.fid} {fx.check} — {detail} "
                      f"(complete validator: {len(CHECKS)} checks)")
            continue
        if raised:
            bad += 1
            print(f"[FAIL] {fx.fid} rejected only by an exception in "
                  f"{raised[:3]}, not by a validation decision")
            continue
        if ok_named or fx.expect.lower() not in detail.lower():
            bad += 1
            print(f"[FAIL] {fx.fid} expected {fx.check} to fail with "
                  f"'{fx.expect}', got ok={ok_named}: {detail[:200]}")
            continue
        neg += 1
        if verbose:
            print(f"[PASS] {fx.fid} rejected by the complete validator for the "
                  f"expected reason — {detail[:160]}")
    print(f"\nPOSITIVE FIXTURES: {pos}/{sum(1 for f in FIXTURES if f.positive)} accepted")
    print(f"NEGATIVE FIXTURES: {neg}/{sum(1 for f in FIXTURES if not f.positive)} "
          f"rejected for the expected reason")
    return 0 if bad == 0 else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Prompt 12B B-12 specification validator")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--fixtures", action="store_true")
    ap.add_argument("--mutation-audit", action="store_true",
                    help="run the validator as a subprocess against isolated "
                         "mutated copies of every input file")
    args = ap.parse_args(argv)

    for key, path in FILES.items():
        if not path.exists():
            print(f"MISSING CANONICAL INPUT: {key} -> {path}")
            return 2

    model = load()
    if args.mutation_audit:
        return run_mutation_audit(model, args.verbose)
    if args.self_test or args.fixtures:
        rc1 = run_fixtures(model, args.verbose)
        rc2 = run_checks(model, args.verbose) if args.self_test else 0
        return 0 if rc1 == 0 and rc2 == 0 else 1
    return run_checks(model, args.verbose)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))