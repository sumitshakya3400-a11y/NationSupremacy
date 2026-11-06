#!/usr/bin/env python3
"""Prompt 12A research- and design-foundations validator.

Validates the **research, evidence, requirements and design-foundation quality**
of the Stage 2 Prompt 12A deliverable set:

* ``docs/stage-2/research/12A_fair_play_privacy_moderation_administration_research.md``
* ``docs/stage-2/research/12A_sources_and_benchmarks_register.md``
* ``docs/stage-2/research/12A_requirements_integration_and_risk_registers.md``
* the three authoritative registers those deliverables update
  (``DECISIONS.md``, ``04_approved_and_provisional_decisions.md``,
  ``05_unresolved_design_decisions.md``)

It implements the six check families required by the Prompt 12A brief §22:
research integrity, requirement integrity, decision integrity, integration
integrity, documentation integrity, and negative fixtures.

**This is a document checker. It is not a security test.** It validates none
of: cheat detection, privacy enforcement, RLS behaviour, moderation tooling,
authentication, appeal workflow execution, audit-log tamper resistance or
playability. Every control it inspects is a *stated* control; none is
implemented, executed, calibrated or released. It confirms only that the
research record exists, is traceable, is internally consistent, does not
overstep the authority of an ``A``-phase pass, and does not overstate its own
status.

Run from anywhere: paths resolve relative to this file.

    python 12A_validate_foundations.py
    python 12A_validate_foundations.py --verbose
    python 12A_validate_foundations.py --self-test
    python 12A_validate_foundations.py --fixtures

Exit code: 0 when every check and fixture passes, 1 when any check or fixture
fails, 2 when a canonical input file is missing.

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

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

QA_DIR = Path(__file__).resolve().parent
DOCS = QA_DIR.parent
RESEARCH = DOCS / "stage-2" / "research"

MAIN = RESEARCH / "12A_fair_play_privacy_moderation_administration_research.md"
SOURCES = RESEARCH / "12A_sources_and_benchmarks_register.md"
REGISTERS = RESEARCH / "12A_requirements_integration_and_risk_registers.md"
DECISIONS = DOCS / "DECISIONS.md"
DD_REGISTER = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
UD_REGISTER = DOCS / "stage-2" / "05_unresolved_design_decisions.md"
REQ_REGISTER = DOCS / "stage-2" / "03_requirements_traceability.md"
PROGRESS_LOG = DOCS / "stage-2" / "06_stage_2_progress_log.md"
CONTINUITY = [DOCS / "AI_CONTEXT.md", DOCS / "AI_HANDOFF.md", DOCS / "PROJECT_PROGRESS.md"]

FILES = {"main": MAIN, "sources": SOURCES, "registers": REGISTERS,
         "decisions": DECISIONS, "dd": DD_REGISTER, "ud": UD_REGISTER,
         "req": REQ_REGISTER, "log": PROGRESS_LOG}

# --- expected cardinalities -------------------------------------------------
# These are the figures the deliverables themselves declare. A mismatch is a
# documentation defect, not a style preference: the project's rule is that a
# published count must equal the rows that exist.
EXPECTED = {
    "12A-RS": 152,
    "12A-BM": 40,
    "12A-CMP": 18,
    "12A-CR": 106,
    "12A-INT": 30,
    "12A-RK": 32,
    "12A-FR": 15,
    "12A-OPEN": 15,
    "12A-IC": 11,
    "12A-DR": 32,
}

# Owner-reserved or fixed identifiers that Prompt 12A must never present as
# changed, resolved or superseded.
PROTECTED_IDS = [
    "D-014", "D-015", "D-017", "D-018", "D-024", "D-025", "D-026", "D-027",
    "D-028", "D-032", "D-033", "D-035", "D-036", "D-037", "D-039", "D-042",
    "D-064", "D-122", "D-137", "D-140", "D-141", "D-142", "D-143",
]

OWNER_RESERVED_UD = ["UD-017"] + [f"UD-0{n}" for n in range(40, 52)]

# --- vocabularies -----------------------------------------------------------
SOURCE_TYPES = (
    "LEGISLATION", "REGULATOR", "STANDARDS", "OFFICIAL-OPERATOR",
    "OFFICIAL-VENDOR", "PEER-REVIEWED", "PREPRINT", "INDUSTRY", "TERTIARY",
    "COMMUNITY", "ACADEMIC", "RESEARCH FINDING",
)
CONFIDENCE_TOKENS = ("High", "Medium", "Low", "Unverified")
CR_STATUSES = (
    "Restates approved policy", "New proposal",
    "New proposal, closes a registered gap",
    "New proposal, extends a registered artefact",
    "New proposal, extends an approved design",
    "New proposal, consolidates registered obligations",
)
PRIORITIES = ("A", "B", "C")
RISK_CLASSES = ("CONFIRMED", "PLAUSIBLE", "RESEARCH", "HYPOTHETICAL", "IMPL")

# Phrases that would claim implementation, execution or release of a control.
IMPLEMENTATION_CLAIMS = [
    r"\b(?:is|are|has been|have been|was|were)\s+(?:now\s+)?(?:implemented|deployed|enabled|live|running)\b",
    r"\btests?\s+(?:were|was|have been|has been)\s+(?:run|executed|passed)\b",
    r"\bwe\s+(?:ran|executed|tested)\s+(?:the\s+)?(?:anti-?cheat|moderation|privacy|security)\b",
    r"\bproduction[- ]ready\b",
    r"\bgoes?\s+live\b",
]

# Sentences that would wrongly promote a 12A candidate or recommendation.
PROMOTION_CLAIMS = [
    r"\b12A[- ]CR-\d+[^\n]{0,40}\bis approved by\b",
    r"\b12A[- ]DR-\d+[^\n]{0,40}\bis approved by\b",
    r"\bPrompt 12A approved (?:a|the) (?:ladder|penalty|permission|retention|tier)\b",
    r"\bREQ-7[6-9]\d[^.\n]{0,30}allocated by 12A\b",
    r"\bUD-0(?:5[2-9]|60)[^.\n]{0,60}\b(?:resolved by 12A|closed by 12A)\b",
]

# Legal conclusions the corpus must not state while the jurisdiction is open.
LEGAL_OVERREACH = [
    r"\bGDPR (?:therefore |clearly )?applies to (?:us|Nation Supremacy|this project)\b",
    r"\bis legally required (?:of|for) Nation Supremacy\b",
    r"\bwe are (?:GDPR|DSA|COPPA) compliant\b",
    r"\bbinding on the project\b",
]

STATUS_TOKENS_RE = re.compile(
    r"\b(PASS|PARTIAL|FAIL|BLOCKED|NOT RUN|NOT APPLICABLE)\b")

CR_CATEGORIES_20 = [
    "Fair play principle", "Anti-cheat architecture", "Multi-account policy",
    "Collusion prevention", "Detection and investigation", "Privacy",
    "Data protection", "Moderation", "Disciplinary enforcement",
    "Player reporting", "Evidence integrity", "Appeals",
    "Administrative authority", "Separation of duties",
    "Emergency administration", "Auditability", "Security incidents",
    "Cross-system integration", "Failure handling", "Governance",
]


# --- parsing helpers --------------------------------------------------------

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def cells(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def id_numbers(text: str, prefix: str) -> list[int]:
    return sorted({int(n) for n in re.findall(rf"\b{re.escape(prefix)}-(\d+)\b", text)})


def rows_for(text: str, prefix: str, arity: int | None = None) -> list[list[str]]:
    pat = re.compile(rf"^\|\s*`{re.escape(prefix)}-(\d+)`\s*\|")
    out = []
    for ln in text.splitlines():
        m = pat.match(ln)
        if m and (arity is None or ln.count("|") == arity):
            out.append(cells(ln))
    return out


def rows_after(text: str, anchor: str, prefix: str) -> list[list[str]]:
    """Rows of one id namespace inside one section, located by its heading.

    Several 12A tables share an id namespace and the same column count, so a
    single arity filter cannot separate them; the section heading can. The
    section runs from the anchor to the next heading at any level.
    """
    i = text.find(anchor)
    if i < 0:
        return []
    level = len(anchor) - len(anchor.lstrip("#"))
    nxt = re.search(rf"^#{{1,{level}}} ", text[i + len(anchor):], flags=re.M)
    end = i + len(anchor) + (nxt.start() if nxt else len(text))
    pat = re.compile(rf"^\|\s*`{re.escape(prefix)}-(\d+)`\s*\|")
    return [cells(ln) for ln in text[i:end].splitlines() if pat.match(ln)]


def by_num(rows: list[list[str]]) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    for x in rows:
        m = re.search(r"12A-[A-Z]+-(\d+)", x[0])
        if m:
            out[int(m.group(1))] = x
    return out


def gaps(nums: list[int]) -> list[int]:
    if not nums:
        return []
    return [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]


def citations(text: str, prefix: str) -> set[int]:
    return {int(n) for n in re.findall(rf"`{re.escape(prefix)}-(\d+)`", text)}


def section(text: str, heading_re: str, stop_re: str) -> str:
    m = re.search(heading_re, text, flags=re.M)
    if not m:
        return ""
    rest = text[m.start():]
    s = re.search(stop_re, rest[len(m.group(0)):], flags=re.M)
    return rest[: len(m.group(0)) + s.start()] if s else rest


@dataclass
class Model:
    """All parsed state. Rebuilt from raw text so fixtures can mutate it."""
    src: dict[str, str] = field(default_factory=dict)
    rs: dict[int, list[str]] = field(default_factory=dict)
    bm: dict[int, list[str]] = field(default_factory=dict)
    cmp_: dict[int, list[str]] = field(default_factory=dict)
    cr_p1: dict[int, list[str]] = field(default_factory=dict)
    cr_p2: dict[int, list[str]] = field(default_factory=dict)
    int_p1: dict[int, list[str]] = field(default_factory=dict)
    int_p2: dict[int, list[str]] = field(default_factory=dict)
    rk_def: dict[int, list[str]] = field(default_factory=dict)
    rk_ctl: dict[int, list[str]] = field(default_factory=dict)
    rk_res: dict[int, list[str]] = field(default_factory=dict)
    fr: dict[int, list[str]] = field(default_factory=dict)
    op: dict[int, list[str]] = field(default_factory=dict)
    dr: dict[int, list[str]] = field(default_factory=dict)
    ic: dict[int, list[str]] = field(default_factory=dict)
    gates: dict[str, str] = field(default_factory=dict)
    d_rows: dict[int, list[str]] = field(default_factory=dict)
    dd_rows: dict[int, list[str]] = field(default_factory=dict)
    ud_rows: dict[int, list[str]] = field(default_factory=dict)
    req_max: int = 0

    def rebuild(self) -> None:
        s = self.src.get("sources", "")
        r = self.src.get("registers", "")
        g = self.src.get("main", "")
        d = self.src.get("decisions", "")
        dd = self.src.get("dd", "")
        u = self.src.get("ud", "")
        q = self.src.get("req", "")
        self.rs = by_num(rows_for(s, "12A-RS", 10))
        self.bm = by_num(rows_for(s, "12A-BM", 9))
        self.cmp_ = {int(re.search(r"12A-CMP-(\d+)", x[0]).group(1)): x
                     for x in rows_for(s, "12A-CMP", 6)}
        self.cr_p1 = by_num(rows_after(r, "## 2. Candidate requirement register, part 1", "12A-CR"))
        self.cr_p2 = by_num(rows_after(r, "## 3. Candidate requirement register, part 2", "12A-CR"))
        self.int_p1 = by_num(rows_after(r, "### 4.1 Rows 1–6", "12A-INT"))
        self.int_p2 = by_num(rows_after(r, "### 4.2 Rows 7–12", "12A-INT"))
        self.rk_def = by_num(rows_after(r, "### 5.2 Fields 1–7", "12A-RK"))
        self.rk_ctl = by_num(rows_after(r, "### 5.3 Fields 8–13", "12A-RK"))
        self.rk_res = by_num(rows_after(r, "### 5.4 Fields 14–18", "12A-RK"))
        self.fr = by_num(rows_after(r, "## 7. Failure and recovery posture register", "12A-FR"))
        self.op = by_num(rows_after(r, "## 8. Open research questions", "12A-OPEN"))
        self.dr = by_num(rows_after(g, "## 27. Recommendations for Prompt 12B", "12A-DR"))
        self.ic = by_num(rows_after(g, "## 11. Information classification", "12A-IC"))
        self.gates = _gates(g)
        self.d_rows = {}
        for ln in d.splitlines():
            m = re.match(r"^\|\s*(D-\d{3})\s*\|", ln)
            if m:
                self.d_rows[int(m.group(1).split("-")[1])] = cells(ln)
        self.dd_rows = {}
        for ln in dd.splitlines():
            m = re.match(r"^\|\s*`?(DD-\d{3})`?\s*\|", ln)
            if m:
                self.dd_rows[int(m.group(1).split("-")[1])] = cells(ln)
        self.ud_rows = {}
        for ln in u.splitlines():
            m = re.match(r"^\|\s*(UD-\d{3})\s*\|", ln)
            if m and ln.count("|") >= 9:
                self.ud_rows[int(m.group(1).split("-")[1])] = cells(ln)
        nums = [int(x.group(1)) for x in re.finditer(r"^\| REQ-(\d{3}) \|", q, re.M)]
        self.req_max = max(nums) if nums else 0


def _collect(rows: list[list[str]]) -> list[list[str]]:
    """Keep rows whose first cell parses as a bare id; drop header noise."""
    return [x for x in rows if re.match(r"^[A-Za-z0-9]+-\d+$", x[0].strip("`"))]


def _collect_all_dd(text: str) -> list[list[str]]:
    out = []
    for ln in text.splitlines():
        m = re.match(r"^\|\s*`?(DD-\d{3})`?\s*\|", ln)
        if m:
            out.append(cells(ln))
    return out


def _gates(main_text: str) -> dict[str, str]:
    """Parse the P12A gate table into {gate id: status token}."""
    out: dict[str, str] = {}
    for ln in main_text.splitlines():
        m = re.match(r"^\|\s*`?(P12A-\d{2})`?\s*\|", ln)
        if m:
            toks = STATUS_TOKENS_RE.findall(ln)
            out[m.group(1)] = toks[-1] if toks else "MISSING"
    return out


def load() -> Model:
    m = Model()
    for key, path in FILES.items():
        m.src[key] = read(path) if path.exists() else ""
    m.rebuild()
    return m


# --- checks ----------------------------------------------------------------

def check_01(m: Model) -> tuple[bool, str]:
    missing = [p.name for p in FILES.values() if not p.exists()]
    return (not missing,
            "all eight canonical inputs present" if not missing else f"missing: {missing}")


def check_02(m: Model) -> tuple[bool, str]:
    """Source ids unique, contiguous, and equal to the declared count."""
    ids = sorted(m.rs)
    bad = gaps(ids)
    dup = len(rows_for(m.src["sources"], "12A-RS", 10)) - len(ids)
    if bad or dup:
        return False, f"gaps {bad[:8]}, duplicate rows {dup}"
    return (len(ids) == EXPECTED["12A-RS"] and ids[0] == 1 and ids[-1] == EXPECTED["12A-RS"],
            f"{len(ids)} source rows, contiguous 001…{ids[-1] if ids else 0}, no duplicates")


def check_03(m: Model) -> tuple[bool, str]:
    """Every source row carries a valid type token, an access-dated URL and a confidence."""
    bad_type, bad_conf, bad_url = [], [], []
    for n, c in m.rs.items():
        body = " ".join(c).upper()
        if not any(t in body for t in SOURCE_TYPES):
            bad_type.append(n)
        if not any(c[-1].startswith(t) for t in CONFIDENCE_TOKENS):
            bad_conf.append(n)
        ref = c[1].lower()
        traceable = ("http", "same url as", "url not captured", "url not retrieved",
                     "no external url")
        if not any(k in ref for k in traceable):
            bad_url.append(n)
    if bad_type or bad_conf or bad_url:
        return False, (f"no type token {bad_type[:4]}; bad confidence {bad_conf[:4]}; "
                       f"untraced {bad_url[:4]}")
    return True, f"{len(m.rs)} rows: type token, confidence and a traceable reference all populated"


def check_04(m: Model) -> tuple[bool, str]:
    """Every source row states a limitation and a Nation Supremacy consequence."""
    thin = [n for n, c in m.rs.items()
            if len(c[4]) < 25 or len(c[5]) < 12 or len(c[6]) < 12 or len(c[7]) < 12]
    return (not thin,
            f"all {len(m.rs)} rows carry finding, limitation, relevance and implication"
            if not thin else f"thin or empty cells in rows {thin[:6]}")


def check_05(m: Model) -> tuple[bool, str]:
    """Every RS id cited anywhere must resolve to a real source row."""
    cited = (citations(m.src["registers"], "12A-RS") | citations(m.src["main"], "12A-RS")
             | citations(m.src["sources"], "12A-RS"))
    dangling = sorted(c for c in cited if c not in m.rs)
    uncited = sorted(n for n in m.rs if n not in cited)
    if dangling:
        return False, f"cited but absent: {dangling[:8]}"
    if uncited:
        return False, f"{len(uncited)} source rows never cited anywhere: {uncited[:8]}"
    return True, f"all {len(cited)} cited source references resolve and every row is used"


def check_06(m: Model) -> tuple[bool, str]:
    """Benchmark rows must cite sources and be genuinely comparative."""
    orphan, thin = [], []
    for n, c in m.bm.items():
        body = " ".join(c).replace(f"12A-BM-{n:03d}", "")
        if not (citations(body, "12A-RS") or citations(body, "12A-BM")):
            orphan.append(n)
        if len(c[3]) < 40 or len(c[5]) < 25 or len(c[6]) < 30:
            thin.append(n)
    if orphan or thin:
        return False, f"uncited {orphan[:5]}; not comparative {thin[:5]}"
    return True, (f"{len(m.bm)} benchmark rows, each citing sources and carrying "
                  "approach, strength, limitation and applicability")


def check_07(m: Model) -> tuple[bool, str]:
    """Comparator profiles must state a verification condition, not just a name."""
    bad = [n for n, c in m.cmp_.items() if len(c) < 5 or len(c[4]) < 25]
    return (not bad and len(m.cmp_) == EXPECTED["12A-CMP"],
            f"{len(m.cmp_)} comparator profiles with a verification statement"
            if not bad else f"profiles without verification state: {bad}")


def check_08(m: Model) -> tuple[bool, str]:
    """Retrieval honesty: failed or excerpt-only sources are labelled, not hidden."""
    text = m.src["sources"]
    flagged = len(re.findall(r"Fetch failed|not retrievable|could not be read|"
                             r"blocked|403|502|404|excerpt only|search index",
                             text, re.I))
    unverified = [n for n, c in m.rs.items() if c[-1].startswith("Unverified")]
    need = [n for n, c in m.rs.items()
            if re.search(r"Fetch failed|not read|unreadable|403|blocked", " ".join(c), re.I)]
    if flagged < 20:
        return False, f"only {flagged} retrieval-failure statements in the register"
    if not need:
        return False, "no row admits a retrieval failure; unverifiable claims may be present"
    return True, (f"{flagged} retrieval statements; {len(need)} rows admit they were not read; "
                  f"{len(unverified)} rated Unverified")


def check_09(m: Model) -> tuple[bool, str]:
    """Requirement ids unique, contiguous, and present in both halves."""
    raw1 = rows_after(m.src["registers"], "## 2. Candidate requirement register, part 1", "12A-CR")
    raw2 = rows_after(m.src["registers"], "## 3. Candidate requirement register, part 2", "12A-CR")
    dup = (len(raw1) - len(m.cr_p1)) + (len(raw2) - len(m.cr_p2))
    if dup:
        return False, f"{dup} duplicate candidate requirement rows"
    p1, p2 = sorted(m.cr_p1), sorted(m.cr_p2)
    bad = gaps(p1) or gaps(p2)
    if bad:
        return False, f"gaps in the candidate block: {bad[:8]}"
    only1 = sorted(set(p1) - set(p2))
    only2 = sorted(set(p2) - set(p1))
    if only1 or only2:
        return False, f"missing part-2 row for {only1[:5]}; missing part-1 row for {only2[:5]}"
    return (len(p1) == EXPECTED["12A-CR"],
            f"{len(p1)} candidates, contiguous, each with exactly one row in both halves")


def check_10(m: Model) -> tuple[bool, str]:
    """Every candidate carries a testable statement, rationale and verification approach."""
    weak_stmt, weak_rat, weak_ver = [], [], []
    for n, c in m.cr_p1.items():
        if len(c[1]) < 60 or len(c[1]) > 900:
            weak_stmt.append(n)
    for n, c in m.cr_p2.items():
        if len(c[1]) < 20:
            weak_rat.append(n)
        if len(c[-1]) < 12:
            weak_ver.append(n)
    if weak_stmt or weak_rat or weak_ver:
        return False, (f"statement length {weak_stmt[:4]}; rationale {weak_rat[:4]}; "
                       f"verification {weak_ver[:4]}")
    return True, "all candidates have a substantial statement, a rationale and a verification approach"


def check_11(m: Model) -> tuple[bool, str]:
    """Vague, untestable requirement language is banned by brief §15.2."""
    vague = [r"\bshould be secure\b", r"\bcheaters should be detected\b",
             r"\bprivacy should be respected\b", r"\badministrators should behave\b",
             r"\bsystem should be robust\b", r"\badequate(?:ly)? secure\b",
             r"\bas appropriate as possible\b", r"\beffort will be made\b"]
    hits = []
    for n, c in m.cr_p1.items():
        for pat in vague:
            if re.search(pat, c[1], re.I):
                hits.append((n, pat))
    return (not hits, "no untestable requirement wording" if not hits else f"vague wording: {hits[:4]}")


def check_12(m: Model) -> tuple[bool, str]:
    """Priority and status vocabularies are closed; status never says Approved."""
    bad_pri, bad_stat = [], []
    for n, c in m.cr_p1.items():
        if c[3] not in PRIORITIES:
            bad_pri.append(n)
        if not any(c[4].startswith(s) for s in CR_STATUSES):
            bad_stat.append(n)
        if re.match(r"^Approved\b", c[4]):
            bad_stat.append(n)
    if bad_pri or bad_stat:
        return False, f"bad priority {bad_pri[:4]}; bad status {bad_stat[:4]}"
    return True, f"{len(m.cr_p1)} rows use only the closed priority and status vocabularies"


def check_13(m: Model) -> tuple[bool, str]:
    """All twenty requirement categories of brief §15.1 are represented."""
    present = {c[2] for c in m.cr_p1.values()}
    missing = [k for k in CR_CATEGORIES_20 if not any(k in p for p in present)]
    if missing:
        return False, f"categories with no requirement: {missing}"
    return True, f"all 20 categories populated across {len(present)} distinct labels"


def check_14(m: Model) -> tuple[bool, str]:
    """No candidate may carry an owner dependency that no UD row actually holds."""
    refs = set()
    for n, c in m.cr_p1.items():
        refs |= {int(x) for x in re.findall(r"UD-(\d{3})", c[6])}
    dangling = sorted(r for r in refs if r not in m.ud_rows)
    unowned = sorted(n for n, c in m.cr_p1.items()
                     if c[6].startswith("Yes") and not re.search(r"UD-\d{3}", c[6]))
    if dangling:
        return False, f"owner-dependency references to nonexistent UD rows: {dangling[:6]}"
    if unowned:
        return False, f"'Yes — owner' rows with no registered UD row: {unowned[:6]}"
    return True, (f"every owner dependency names an existing UD row "
                  f"({sorted(refs)}); no ownerless 'Yes' rows")


def check_15(m: Model) -> tuple[bool, str]:
    """An A-phase pass allocates no global REQ identifier and moves no frontier."""
    if m.req_max != 763:
        return False, f"global requirement register frontier is REQ-{m.req_max}, expected 763"
    rows = re.findall(r"^\|\s*`?REQ-(\d{3})`?\s*\|", m.src["registers"], re.M)
    added = sorted({n for n in rows if int(n) >= 764})
    if added:
        return False, f"12A allocated global requirement rows: {added[:6]}"
    reserved = re.findall(r"REQ-7(?:6[4-9]|7\d|8\d)", m.src["registers"])
    if not reserved:
        return False, "the reserved 12B block is not declared"
    return True, ("REQ-763 remains the frontier; REQ-764 onward reserved for 12B; "
                  f"{len(reserved)} reservation mentions and no allocated row")


def check_16(m: Model) -> tuple[bool, str]:
    """Declared register totals equal the computed totals."""
    decl = m.src["registers"]
    want = {
        "12A-CR": (EXPECTED["12A-CR"], len(m.cr_p1)),
        "12A-INT": (EXPECTED["12A-INT"], len(m.int_p1)),
        "12A-RK": (EXPECTED["12A-RK"], len(m.rk_def)),
        "12A-FR": (EXPECTED["12A-FR"], len(m.fr)),
        "12A-OPEN": (EXPECTED["12A-OPEN"], len(m.op)),
    }
    bad = [f"{k}: declared {v[0]} found {v[1]}" for k, v in want.items() if v[0] != v[1]]
    totals_row = re.search(r"\| Candidate requirements \| `12A-CR-###` \|[^|]*\| \*\*(\d+)\*\*",
                           decl)
    if not totals_row or int(totals_row.group(1)) != len(m.cr_p1):
        bad.append("§9 totals table disagrees with the rows")
    return (not bad, "all declared counts reconcile with the rows" if not bad else "; ".join(bad))


def check_17(m: Model) -> tuple[bool, str]:
    """The sources register's own totals table matches the rows it owns."""
    s = m.src["sources"]
    want = {"12A-RS": EXPECTED["12A-RS"], "12A-BM": EXPECTED["12A-BM"],
            "12A-CMP": EXPECTED["12A-CMP"]}
    have = {"12A-RS": len(m.rs), "12A-BM": len(m.bm), "12A-CMP": len(m.cmp_)}
    bad = [f"{k}: declared {want[k]} found {have[k]}" for k in want if want[k] != have[k]]
    if not re.search(r"\| \*\*152\*\* \| contiguous, no gaps, no duplicates \|", s):
        bad.append("the 152-row total is not stated in §10")
    return (not bad, "sources register totals reconcile (152 / 40 / 18)" if not bad
            else "; ".join(bad))


def check_18(m: Model) -> tuple[bool, str]:
    """Decision register: contiguous, unique, and the fifteen new rows are complete."""
    ids = sorted(m.d_rows)
    if gaps(ids):
        return False, f"gaps in D- numbering: {gaps(ids)[:8]}"
    if len(ids) != 177 or ids[-1] != 177:
        return False, f"expected D-001…D-177, found {len(ids)} rows to max {ids[-1] if ids else 0}"
    incomplete = [n for n in range(163, 178)
                  if n not in m.d_rows or len(m.d_rows[n]) != 8
                  or any(len(c) < 8 for c in m.d_rows[n][3:8])]
    if incomplete:
        return False, f"new decision rows incomplete: {incomplete}"
    return True, "177 decisions, contiguous and unique; D-163…D-177 all carry eight fields"


def check_19(m: Model) -> tuple[bool, str]:
    """Design register: contiguous DD ids, the fifteen new rows, and a reconciling tally."""
    ids = sorted(m.dd_rows)
    bad = gaps(ids)
    if bad:
        return False, f"gaps in DD- numbering: {bad[:8]}"
    if ids[-1] != 225 or len(ids) != 225:
        return False, f"expected 225 DD rows, found {len(ids)} to max {ids[-1]}"
    missing_new = [n for n in range(211, 226) if n not in m.dd_rows]
    raw_dd = len(re.findall(r"^\| DD-(\d{3}) \|", m.src["dd"], re.M))
    if raw_dd != len(ids):
        return False, f"{raw_dd} DD rows parsed against {len(ids)} unique ids (duplicates)"
    tally = re.findall(r"^\| (?:Approved|Provisional|Confirmed|Binding inherited|"
                       r"Candidate / Open|Superseded|Deferred) \| (\d+) \|",
                       m.src["dd"], re.M)
    total = sum(int(x) for x in tally)
    declared = re.search(r"\| \*\*Total\*\* \| \*\*(\d+)\*\* \| DD-001…DD-(\d+) \|", m.src["dd"])
    if missing_new:
        return False, f"missing DD rows {missing_new}"
    if not declared or total != int(declared.group(1)):
        return False, f"tally rows sum to {total}, register declares {declared.groups if declared else 'nothing'}"
    return True, f"225 DD rows; §6 tally sums to {total} and matches the declared total"


def check_20(m: Model) -> tuple[bool, str]:
    """Protected and fixed decisions are still present and unmodified in status."""
    absent = [pid for pid in PROTECTED_IDS
              if int(pid.split("-")[1]) not in m.d_rows]
    changed = []
    for pid in ("D-014", "D-015", "D-018", "D-026", "D-032", "D-037", "D-042", "D-122"):
        row = m.d_rows.get(int(pid.split("-")[1]), [])
        body = " ".join(row)
        if "Superseded" in body or "Rejected" in body:
            changed.append(pid)
    if absent or changed:
        return False, f"absent {absent}; newly superseded or rejected {changed}"
    return True, f"{len(PROTECTED_IDS)} protected identifiers present; none superseded by 12A"


def check_21(m: Model) -> tuple[bool, str]:
    """Recommendations are visibly distinct from approved decisions."""
    if len(m.dr) != EXPECTED["12A-DR"]:
        return False, f"found {len(m.dr)} recommendations, declared {EXPECTED['12A-DR']}"
    noalt = [n for n, c in m.dr.items() if len(c[3]) < 8]
    hits = [p for p in PROMOTION_CLAIMS for t in m.src.values() if re.search(p, t, re.I)]
    if noalt:
        return False, f"recommendations with no rejected alternative recorded: {noalt[:5]}"
    if hits:
        return False, f"a candidate or recommendation is presented as approved: {hits[:2]}"
    if "not an approved rule" not in m.src["main"]:
        return False, "the recommendations section does not disclaim approval"
    return True, f"{len(m.dr)} recommendations, each naming a rejected alternative, none promoted"


def check_22(m: Model) -> tuple[bool, str]:
    """Owner-reserved decisions remain open, and 12A's nine new rows are open too."""
    closed = []
    for uid in OWNER_RESERVED_UD + [f"UD-0{n}" for n in range(52, 61)]:
        row = m.ud_rows.get(int(uid.split("-")[1]), [])
        status = row[-1] if row else "MISSING"
        if not row or not status.startswith(("**Open", "Open", "**Deferred", "Deferred")):
            closed.append(f"{uid}:{status[:18]}")
    if closed:
        return False, f"owner- or evidence-reserved rows not open: {closed}"
    return True, (f"all {len(OWNER_RESERVED_UD)} pre-existing reserved rows plus UD-052…UD-060 "
                  "remain Open or Deferred")



def check_23(m: Model) -> tuple[bool, str]:
    """Integration rows: both halves aligned and all twelve fields populated."""
    p1, p2 = sorted(m.int_p1), sorted(m.int_p2)
    if p1 != p2:
        return False, ("half-row mismatch: only-1 "
                       f"{sorted(set(p1) - set(p2))[:4]}, only-2 {sorted(set(p2) - set(p1))[:4]}")
    empty = [n for n in p1 if any(not c for c in m.int_p1[n][1:])
             or any(not c for c in m.int_p2[n][1:])]
    def open_cell(cell: str) -> bool:
        return bool(re.fullmatch(r"(?:None|Owner|Stage \d+|Prompt \d+|12[BC]|1[3-5])", cell)) \
            or bool(re.search(r"OPEN|UD-\d", cell)) or len(cell) >= 8

    thin = [n for n in p1 if len(m.int_p1[n][3]) < 20 or len(m.int_p2[n][3]) < 15
            or not open_cell(m.int_p2[n][6])]
    if empty or thin:
        return False, f"empty field {empty[:4]}; too thin {thin[:4]}"
    return True, f"{len(p1)} dependency rows, each with all twelve fields populated"




def _plain(cell: str) -> str:
    return re.sub(r"[*`]", "", cell).strip()


def check_24(m: Model) -> tuple[bool, str]:
    """Threat rows: three halves aligned, class and ordinal assessment present."""
    d, c, r = sorted(m.rk_def), sorted(m.rk_ctl), sorted(m.rk_res)
    if not (d == c == r):
        return False, f"half-set mismatch: def {len(d)}, ctl {len(c)}, res {len(r)}"
    bad_class = [n for n in d
                 if not any(_plain(m.rk_ctl[n][1]).upper().startswith(k) for k in RISK_CLASSES)]
    no_basis = [n for n in d if "L" not in m.rk_ctl[n][2] or "I" not in m.rk_ctl[n][3]]
    no_band = [n for n in d if not re.search(r"\d", m.rk_ctl[n][4])]
    no_res = [n for n in d if len(_plain(m.rk_res[n][-1])) < 3]
    if bad_class or no_basis or no_band or no_res:
        return False, (f"bad class {bad_class[:4]}; no basis {no_basis[:4]}; "
                       f"no band {no_band[:4]}; no residual {no_res[:4]}")
    return True, (f"{len(d)} threat rows with evidence class, likelihood and impact basis, "
                  "a risk band and a stated residual")




def check_25(m: Model) -> tuple[bool, str]:
    """Every threat names a preventive control, a detection control and a requirement."""
    no_prev = [n for n in m.rk_def if len(m.rk_ctl[n][5]) < 8]
    no_det = [n for n in m.rk_def if len(m.rk_ctl[n][6]) < 8]
    no_req = [n for n in m.rk_def if "12A-CR" not in " ".join(m.rk_res[n])]
    refs = {int(x) for x in re.findall(r"12A-CR-(\d+)",
                                      " ".join(" ".join(v) for v in m.rk_res.values()))}
    dangling = sorted(refs - set(m.cr_p1))
    cls = {k: [n for n in m.rk_def if _plain(m.rk_ctl[n][1]).upper().startswith(k)]
           for k in RISK_CLASSES}
    if no_prev or no_det or no_req or dangling:
        return False, (f"no preventive {no_prev[:3]}; no detection {no_det[:3]}; "
                       f"no requirement link {no_req[:3]}; dangling refs {dangling[:3]}")
    if len(cls["CONFIRMED"]) < 3:
        return False, f"only {len(cls['CONFIRMED'])} rows classified CONFIRMED"
    used = {k: len(v) for k, v in cls.items() if v}
    if len(used) < 4:
        return False, f"the five evidence classes are barely distinguished: {used}"
    return True, ("all 32 threats carry prevention, detection and a requirement; classes "
                  + ", ".join(f"{k} {v}" for k, v in sorted(used.items())))




def check_26(m: Model) -> tuple[bool, str]:
    """Source-of-truth ownership is stated for every protected category."""
    seg = section(m.src["main"], r"^### 6\.2 ", r"^### 6\.3 ")
    rows = [ln for ln in seg.splitlines() if re.match(r"^\| (?!--|Protected|Data|ID)", ln)]
    body = " ".join(rows).lower()
    needed = ["treasury balance", "resource balance", "population", "military readiness",
              "operations points", "warfare outcome", "diplomatic", "alliance",
              "market transaction", "objective progress", "event participation",
              "ranking", "progression grant", "reward entitlement", "moderation"]
    missing = [k for k in needed if k not in body]
    if len(rows) < 16:
        return False, f"source-of-truth table has {len(rows)} rows, expected 16"
    if missing:
        return False, f"categories absent: {missing}"
    return True, f"{len(rows)} protected categories, each assigned one owning subsystem"




def check_27(m: Model) -> tuple[bool, str]:
    """No unauthorised subsystem authority is introduced for B-12."""
    forbidden = [
        r"\bB-12 (?:may|can|will) (?:directly )?(?:set|edit|rewrite) (?:a |the )?"
        r"(?:treasury|balance|battle|election|standing|snapshot|objective result)\b",
        r"\bmoderation may (?:transfer|confiscate|mint)\b",
        r"\badministrator[s]? (?:may|can) set (?:a |the )?treasury\b",
        r"\bB-12 owns (?:the )?(economy|market|election|warfare|progression) (?:rules|mechanics)\b",
    ]
    hits = []
    for key in ("main", "registers", "sources"):
        for pat in forbidden:
            if re.search(pat, m.src[key], re.I):
                hits.append((key, pat[:28]))
    corpus = m.src["main"] + " " + m.src["registers"]
    if not re.search(r"owns no gameplay mechanic|owns no mechanic", corpus, re.I):
        hits.append(("corpus", "boundary denial absent"))
    if "perform another" not in corpus and "universal controller" not in corpus:
        hits.append(("corpus", "universal-controller refusal absent"))
    if hits:
        return False, f"authority-boundary problem: {hits[:3]}"
    return True, ("B-12 is denied gameplay authority in text and the universal-controller "
                  "refusal is stated; no contradictory boundary found")



def check_28(m: Model) -> tuple[bool, str]:
    """Failure postures: fifteen rows, each with a posture, a reason and a reference."""
    bad = [n for n, c in m.fr.items()
           if len(c) != 7 or len(c[2]) < 12 or len(c[3]) < 20 or len(c[5]) < 12]
    if bad:
        return False, f"incomplete posture rows: {bad[:5]}"
    global_policy = re.search(r"(?:always|never) fail (?:open|closed) across the (?:whole )?system",
                              m.src["registers"], re.I)
    if global_policy:
        return False, "a single global failure policy is asserted"
    return True, f"{len(m.fr)} postures declared per category; no universal failure policy"


def check_29(m: Model) -> tuple[bool, str]:
    """Open questions each name an owner and a blocked decision."""
    bad = [n for n, c in m.op.items() if len(c) != 5 or len(c[3]) < 8 or len(c[4]) < 8]
    if bad:
        return False, f"open questions without an owner or a blocked item: {bad}"
    refs = {int(x) for x in re.findall(r"UD-(\d{3})", " ".join(" ".join(v) for v in m.op.values()))}
    dangling = sorted(r for r in refs if r not in m.ud_rows)
    if dangling:
        return False, f"open questions cite nonexistent UD rows: {dangling}"
    return True, f"{len(m.op)} open questions, each owned; every UD reference resolves"


def check_30(m: Model) -> tuple[bool, str]:
    """The gate register exists with P12A-01…P12A-22 and legal status tokens only."""
    want = [f"P12A-{i:02d}" for i in range(1, 23)]
    missing = [g for g in want if g not in m.gates]
    illegal = {g: v for g, v in m.gates.items() if v not in
               ("PASS", "PARTIAL", "FAIL", "BLOCKED", "NOT RUN", "NOT APPLICABLE")}
    if missing or illegal:
        return False, f"missing {missing[:6]}; illegal status {list(illegal.items())[:3]}"
    tally = m.src["main"].count("PASS")
    counts = {k: sum(1 for v in m.gates.values() if v == k)
              for k in ("PASS", "PARTIAL", "FAIL", "BLOCKED", "NOT RUN", "NOT APPLICABLE")}
    declared = re.search(r"\*\*(\d+) PASS · (\d+) PARTIAL · (\d+) FAIL · (\d+) BLOCKED · "
                         r"(\d+) NOT RUN · (\d+) NOT APPLICABLE\*\*", m.src["main"])
    if declared:
        got = tuple(int(x) for x in declared.groups())
        want_t = (counts["PASS"], counts["PARTIAL"], counts["FAIL"], counts["BLOCKED"],
                  counts["NOT RUN"], counts["NOT APPLICABLE"])
        if got != want_t:
            return False, f"declared gate tally {got} != computed {want_t}"
    return True, f"22 gates with legal statuses: {counts}"



def check_31(m: Model) -> tuple[bool, str]:
    """The nine machine-checked continuity keys still agree across the three files."""
    required = {"status_updated", "stage_1", "stage_2", "stage_2_next_prompt", "roadmap",
                "legacy_worker", "legacy_supabase_project", "operations_points",
                "decisions_range"}
    blocks = {}
    for path in CONTINUITY:
        seg = section(read(path), r"<!-- STATUS:BEGIN -->", r"<!-- STATUS:END -->")
        vals = {}
        for line in seg.splitlines():
            if ":" in line and not line.startswith("<!--"):
                k, _, v = line.partition(":")
                vals[k.strip()] = v.strip()
        blocks[path.name] = vals
    disagree = []
    for key in sorted(required):
        seen = {name: vals.get(key) for name, vals in blocks.items()}
        if len(set(seen.values())) != 1:
            disagree.append(f"{key}={seen}")
    if disagree:
        return False, "required keys disagree: " + "; ".join(disagree[:3])
    first = blocks[CONTINUITY[0].name]
    missing_keys = sorted(required - set(first))
    if missing_keys:
        return False, f"required keys absent: {missing_keys}"
    if not first["stage_2_next_prompt"].startswith("12"):
        return False, f"stage_2_next_prompt is '{first['stage_2_next_prompt']}'"
    if first["decisions_range"] != "D-001..D-177":
        return False, f"decisions_range is '{first['decisions_range']}'"
    return True, (f"the {len(required)} required status keys agree; next prompt "
                  f"{first['stage_2_next_prompt']}, range {first['decisions_range']}")



def check_32(m: Model) -> tuple[bool, str]:
    """The new progress-log section exists and the historical ones are intact."""
    log = m.src["log"]
    if "## 73. Prompt 12A" not in log:
        return False, "no §73 Prompt 12A record"
    for keep in ("## 72. Prompt 11C", "## 71. Prompt 11B-C3", "## 70.", "## 67."):
        if keep not in log:
            return False, f"historical section {keep} is missing"
    if "12A_validate_foundations.py" not in section(log, r"^## 73\. ", r"^## 7[4-9]\. "):
        return False, "§73 does not record the validator it ran"
    return True, "§73 present and reporting execution; §§67, 70, 71 and 72 intact"


def check_33(m: Model) -> tuple[bool, str]:
    """No implementation, no executed test and no legal conclusion is claimed."""
    impl, legal, promo = [], [], []
    for key in ("main", "registers", "sources"):
        text = m.src[key]
        for pat in IMPLEMENTATION_CLAIMS:
            for mt in re.finditer(pat, text, re.I):
                ctx = text[max(0, mt.start() - 70):mt.end() + 40]
                if not re.search(r"\b(?:not|nothing|never|without|no |only)\b", ctx, re.I):
                    impl.append((key, mt.group(0)[:34]))
        for pat in LEGAL_OVERREACH:
            if re.search(pat, text, re.I):
                legal.append((key, pat[:30]))
        for pat in PROMOTION_CLAIMS:
            if re.search(pat, text, re.I):
                promo.append((key, pat[:30]))
    if impl or legal or promo:
        return False, f"implementation {impl[:2]}; legal {legal[:2]}; promotion {promo[:2]}"
    return True, "no implementation claim, no executed-test claim, no legal conclusion, no promotion"


def check_34(m: Model) -> tuple[bool, str]:
    """Every internal Markdown link in the three deliverables resolves."""
    out = subprocess.run([sys.executable, str(QA_DIR / "validate_links.py")],
                         capture_output=True, text=True, timeout=600)
    body = out.stdout + out.stderr
    unresolved = re.search(r"Unresolved:\s*(\d+)", body)
    if out.returncode == 2:
        return False, "the link validator could not run"
    if not unresolved:
        return False, "the link validator produced no count"
    if int(unresolved.group(1)) != 0:
        return False, f"{unresolved.group(1)} unresolved links"
    return True, "external link gate reports Unresolved: 0"


def check_35(m: Model) -> tuple[bool, str]:
    """The information-classification foundation is present and internally consistent."""
    if len(m.ic) != EXPECTED["12A-IC"]:
        return False, f"found {len(m.ic)} classification rows, declared {EXPECTED['12A-IC']}"
    bad = [n for n, c in m.ic.items() if len(c) != 7 or not c[2] or not c[3] or not c[4]
           or not c[5]]
    if bad:
        return False, f"category rows missing an axis value: {bad}"
    axes = re.search(r"three declared axes|three-axis", m.src["main"], re.I)
    if not axes:
        return False, "the three-axis model is not stated"
    if "WEP-647" not in m.src["main"] or "TR-021" not in m.src["main"]:
        return False, "the model does not reconcile the existing vocabularies"
    return True, (f"{len(m.ic)} candidate categories mapped onto three axes, reconciling "
                   "D-042, TR-021, TR-090 and WEP-647")


# --- registry ----------------------------------------------------------------

@dataclass
class _Check:
    cid: str
    name: str
    fn: object


CHECKS: list = []


def _register():
    specs = [
        ("12A-01", "all canonical deliverables and registers exist", check_01),
        ("12A-02", "source ids unique, contiguous, count as declared", check_02),
        ("12A-03", "every source row carries type, confidence and URL", check_03),
        ("12A-04", "every source row carries finding, limitation, relevance, implication",
         check_04),
        ("12A-05", "every cited source reference resolves and no row is orphaned", check_05),
        ("12A-06", "benchmark rows cite sources and are genuinely comparative", check_06),
        ("12A-07", "comparator profiles state how their evidence was verified", check_07),
        ("12A-08", "retrieval failures are recorded, not hidden", check_08),
        ("12A-09", "candidate requirement ids unique and paired", check_09),
        ("12A-10", "every requirement has statement, rationale and verification approach",
         check_10),
        ("12A-11", "no untestable requirement wording", check_11),
        ("12A-12", "requirement priority and status vocabularies are closed", check_12),
        ("12A-13", "all twenty requirement categories are represented", check_13),
        ("12A-14", "owner dependencies name an existing unresolved row", check_14),
        ("12A-15", "no global requirement id is allocated by an A-phase pass", check_15),
        ("12A-16", "declared requirement register totals reconcile with the rows", check_16),
        ("12A-17", "declared source register totals reconcile with the rows", check_17),
        ("12A-18", "decision register contiguous, unique, new rows complete", check_18),
        ("12A-19", "design register contiguous and its tally reconciles", check_19),
        ("12A-20", "protected and fixed decisions unchanged", check_20),
        ("12A-21", "recommendations distinguishable from approved decisions", check_21),
        ("12A-22", "owner-reserved decisions remain open", check_22),
        ("12A-23", "integration rows paired with all twelve fields", check_23),
        ("12A-24", "threat rows paired with class and ordinal assessment", check_24),
        ("12A-25", "every threat names prevention, detection and a requirement", check_25),
        ("12A-26", "source-of-truth ownership stated for every category", check_26),
        ("12A-27", "no unauthorised subsystem authority introduced", check_27),
        ("12A-28", "failure postures are per-category, never universal", check_28),
        ("12A-29", "open questions each name an owner and reference valid rows", check_29),
        ("12A-30", "gate register complete with legal statuses", check_30),
        ("12A-31", "continuity status blocks agree", check_31),
        ("12A-32", "new progress-log section present, history intact", check_32),
        ("12A-33", "no implementation, executed-test or legal overclaim", check_33),
        ("12A-34", "external link gate resolves every internal link", check_34),
        ("12A-35", "information-classification foundation complete and consistent", check_35),
    ]
    for cid, name, fn in specs:
        CHECKS.append(_Check(cid, name, fn))


_register()


# --- fixtures ---------------------------------------------------------------

@dataclass
class Fixture:
    fid: str
    cid: str
    expect: bool
    mutate: object
    desc: str


def _drop_line(text: str, needle: str) -> str:
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if needle in ln:
            return "".join(lines[:i] + lines[i + 1:])
    raise AssertionError("fixture needle absent: " + needle[:50])


def _dup_line(text: str, needle: str) -> str:
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if needle in ln:
            return "".join(lines[:i] + [ln] + lines[i:])
    raise AssertionError("fixture needle absent: " + needle[:50])


def _sub(text: str, old: str, new: str) -> str:
    if old not in text:
        raise AssertionError("fixture needle absent: " + old[:50])
    return text.replace(old, new, 1)


def fx_missing_source(model):
    model.src["sources"] = _drop_line(model.src["sources"], "`12A-RS-077`")
    model.rebuild()
    return model


def fx_dangling_source_ref(model):
    model.src["registers"] = _sub(model.src["registers"], "`12A-RS-001`, `12A-RS-002`",
                                  "`12A-RS-901`, `12A-RS-002`")
    model.rebuild()
    return model


def fx_duplicate_requirement(model):
    model.src["registers"] = _dup_line(model.src["registers"], "| `12A-CR-030` |")
    model.rebuild()
    return model


def fx_no_verification_intent(model):
    old = ("| `12A-CR-044` | Key custody is what separates a keyed MAC from a "
           "brute-forceable digest over a small identifier space |")
    new = ("| `12A-CR-044` | Key custody | `12A-RS-092` | D-036 | Strongly positive "
           "| Positive | The secret is separated, owned and rotated |  |")
    model.src["registers"] = _sub(model.src["registers"], old, new)
    model.rebuild()
    return model


def fx_unsupported_approval(model):
    model.src["registers"] = _sub(
        model.src["registers"],
        "its notice and its appeal route | Moderation | B | New proposal",
        "its notice and its appeal route | Moderation | B | Approved")
    model.rebuild()
    return model


def fx_owner_row_closed(model):
    model.src["ud"] = _sub(
        model.src["ud"],
        "| Open — awaiting explicit owner decision on what a member can "
        "appeal and who decides; 09B supplies candidate options only |",
        "| **Resolved** by Prompt 12A |")
    model.rebuild()
    return model


def fx_missing_dependency_half(model):
    model.src["registers"] = _drop_line(model.src["registers"], "| `12A-INT-25` | Aggregate only |")
    model.rebuild()
    return model


def fx_duplicate_decision(model):
    model.src["dd"] = _dup_line(model.src["dd"], "| DD-214 |")
    model.rebuild()
    return model


def fx_contradictory_classification(model):
    model.src["main"] = _sub(
        model.src["main"],
        "| `12A-IC-06` | Military-confidential information | Private | "
        "`NATION_OWNER` | S | B-10 |",
        "| `12A-IC-06` | Military-confidential information |  |  |  | B-10 |")
    model.rebuild()
    return model


def fx_legal_overreach(model):
    model.src["main"] = _sub(model.src["main"], "## 28. Conclusions",
                             "The GDPR is binding on the project and we are DSA compliant."
                             "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_untraceable_assertion(model):
    model.src["sources"] = _sub(
        model.src["sources"],
        "obligation for 12B | `12A-RS-121` |",
        "obligation for 12B | — |")
    model.rebuild()
    return model


def fx_illegal_gate_status(model):
    model.src["main"] = _sub(
        model.src["main"],
        "checks `12A-23`, `12A-09` | **PASS**",
        "checks `12A-23`, `12A-09` | **DONE**")
    model.rebuild()
    return model


def fx_implementation_claim(model):
    model.src["main"] = _sub(model.src["main"], "## 28. Conclusions",
                             "The moderation service is now implemented."
                             "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_totals_drift(model):
    model.src["registers"] = _sub(
        model.src["registers"],
        "| Candidate requirements | `12A-CR-###` | `12A-CR-001` … `12A-CR-106` | **106** |",
        "| Candidate requirements | `12A-CR-###` | `12A-CR-001` … `12A-CR-106` | **140** |")
    model.rebuild()
    return model


def fx_protected_decision_changed(model):
    model.src["decisions"] = _sub(model.src["decisions"],
                                  "| **Confirmed** (policy) | Resolves UD-014's policy half.",
                                  "| **Superseded** by Prompt 12A | Resolves UD-014's policy half.")
    model.rebuild()
    return model


FIXTURES: list = [
    Fixture("12A-P01", "12A-02", True, lambda m: m, "source ids resolve contiguously"),
    Fixture("12A-P02", "12A-05", True, lambda m: m, "every cited source resolves"),
    Fixture("12A-P03", "12A-09", True, lambda m: m, "candidates unique and paired"),
    Fixture("12A-P04", "12A-15", True, lambda m: m, "no global requirement allocated"),
    Fixture("12A-P05", "12A-18", True, lambda m: m, "decision register contiguous"),
    Fixture("12A-P06", "12A-19", True, lambda m: m, "design register tally reconciles"),
    Fixture("12A-P07", "12A-22", True, lambda m: m, "owner reservations intact"),
    Fixture("12A-P08", "12A-26", True, lambda m: m, "source-of-truth table complete"),
    Fixture("12A-P09", "12A-30", True, lambda m: m, "gate register well formed"),
    Fixture("12A-P10", "12A-35", True, lambda m: m, "classification model consistent"),
    Fixture("12A-N01", "12A-02", False, fx_missing_source, "a research source row is deleted"),
    Fixture("12A-N02", "12A-05", False, fx_dangling_source_ref, "a claim cites a nonexistent source"),
    Fixture("12A-N03", "12A-09", False, fx_duplicate_requirement, "a requirement id is duplicated"),
    Fixture("12A-N04", "12A-10", False, fx_no_verification_intent, "a requirement has no verification"),
    Fixture("12A-N05", "12A-12", False, fx_unsupported_approval, "a candidate is marked Approved"),
    Fixture("12A-N06", "12A-22", False, fx_owner_row_closed, "an owner-reserved row is closed"),
    Fixture("12A-N07", "12A-23", False, fx_missing_dependency_half, "a dependency half is removed"),
    Fixture("12A-N08", "12A-19", False, fx_duplicate_decision, "a design position id is duplicated"),
    Fixture("12A-N09", "12A-35", False, fx_contradictory_classification,
            "a category loses its axis assignment"),
    Fixture("12A-N10", "12A-33", False, fx_legal_overreach, "an unsupported legal conclusion"),
    Fixture("12A-N11", "12A-06", False, fx_untraceable_assertion, "a benchmark cites no source"),
    Fixture("12A-N12", "12A-30", False, fx_illegal_gate_status, "a gate uses an illegal status"),
    Fixture("12A-N13", "12A-33", False, fx_implementation_claim, "an implementation claim appears"),
    Fixture("12A-N14", "12A-16", False, fx_totals_drift, "a declared total drifts"),
    Fixture("12A-N15", "12A-20", False, fx_protected_decision_changed,
            "a protected decision is superseded"),
]


# --- runners ----------------------------------------------------------------

def run_checks(model, verbose):
    by_id = {c.cid: c for c in CHECKS}
    failed = []
    passed = 0
    for cid in sorted(by_id):
        ok, detail = by_id[cid].fn(model)
        if ok:
            passed += 1
        else:
            failed.append((cid, detail))
        if verbose or not ok:
            print(f"[{'PASS' if ok else 'FAIL'}] {cid} {by_id[cid].name} — {detail}")
    return passed, len(CHECKS), failed


def run_fixtures(model, verbose):
    by_id = {c.cid: c for c in CHECKS}
    pos_ok = pos_n = neg_ok = neg_n = 0
    problems = []
    for fx in FIXTURES:
        mutated = Model(src={k: v for k, v in model.src.items()})
        mutated.rebuild()
        try:
            mutated = fx.mutate(mutated)
        except AssertionError as exc:
            problems.append(f"{fx.fid}: fixture is stale — {exc}")
            if fx.expect:
                pos_n += 1
            else:
                neg_n += 1
            continue
        ok, detail = by_id[fx.cid].fn(mutated)
        good = (ok == fx.expect)
        if fx.expect:
            pos_n += 1
            pos_ok += 1 if good else 0
        else:
            neg_n += 1
            neg_ok += 1 if good else 0
        if verbose or not good:
            want = "accepted" if fx.expect else "rejected"
            print(f"[{'OK ' if good else 'BAD'}] {fx.fid} {fx.cid} expected to {want} "
                  f"({fx.desc}) -> {ok}: {str(detail)[:110]}")
    return pos_ok, pos_n, neg_ok, neg_n, problems


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(description="Prompt 12A foundations validator")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--fixtures", action="store_true")
    args = ap.parse_args(argv)

    missing = [p.name for p in FILES.values() if not p.exists()]
    if missing:
        print(f"RESULT: MISSING INPUT — {missing}")
        return 2

    model = load()
    print(f"12A foundations · sources={len(model.rs)} benchmark={len(model.bm)} "
          f"comparators={len(model.cmp_)} candidates={len(model.cr_p1)} "
          f"dependencies={len(model.int_p1)} threats={len(model.rk_def)} "
          f"postures={len(model.fr)} open-questions={len(model.op)} "
          f"recommendations={len(model.dr)} categories={len(model.ic)}")
    print(f"registers · D={len(model.d_rows)} DD={len(model.dd_rows)} "
          f"UD={len(model.ud_rows)} REQ max={model.req_max}")

    problems = []
    pos_ok = pos_n = neg_ok = neg_n = 0
    passed = total = 0

    if not args.fixtures:
        passed, total, failed = run_checks(model, args.verbose or args.self_test)
        problems += [f"{cid}: {d}" for cid, d in failed]

    if args.self_test or args.fixtures:
        pos_ok, pos_n, neg_ok, neg_n, fx_problems = run_fixtures(model,
                                                                 args.verbose or args.self_test)
        problems += fx_problems

    print()
    if not args.fixtures:
        print(f"CHECKS: {passed}/{total} passed; {total - passed} failed")
    if args.self_test or args.fixtures:
        print(f"POSITIVE FIXTURES: {pos_ok}/{pos_n} accepted")
        print(f"NEGATIVE FIXTURES: {neg_ok}/{neg_n} rejected for the expected reason")
    print(f"MISSING EVIDENCE / INVALID REFERENCES / TRACEABILITY GAPS: {len(problems)}")

    if problems:
        for p in problems[:14]:
            print(f"  - {p}")
        print("RESULT: FAIL — Prompt 12A documentation-quality checks not satisfied")
        return 1

    print("RESULT: PASS — documentation quality only. This is not the acceptance-gate count.")
    print("NOT PROVEN: any executed test, any implemented control, any enforced privacy rule, "
          "any working moderation or appeal workflow, any production security posture, any "
          "calibrated number, and no independent review of this pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
