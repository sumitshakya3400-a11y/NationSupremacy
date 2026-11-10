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
<<<<<<< HEAD
    "12A-RS": 153,
=======
    "12A-RS": 152,
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
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
    """Read a document as UTF-8 text, replacing decoding errors."""
    return path.read_text(encoding="utf-8", errors="replace")


def cells(row: str) -> list[str]:
    """Split one Markdown table row into stripped cells."""
    return [c.strip() for c in row.strip().strip("|").split("|")]


def id_numbers(text: str, prefix: str) -> list[int]:
    """Return the sorted, de-duplicated numeric ids of one prefix in text."""
    return sorted({int(n) for n in re.findall(rf"\b{re.escape(prefix)}-(\d+)\b", text)})


def rows_for(text: str, prefix: str, arity: int | None = None) -> list[list[str]]:
    """Return table rows that begin with a backticked id of the given prefix."""
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
    """Index parsed rows by their numeric 12A id."""
    out: dict[int, list[str]] = {}
    for x in rows:
        m = re.search(r"12A-[A-Z]+-(\d+)", x[0])
        if m:
            out[int(m.group(1))] = x
    return out


def gaps(nums: list[int]) -> list[int]:
    """Return the missing integers between the smallest and largest id."""
    if not nums:
        return []
    return [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]


def citations(text: str, prefix: str) -> set[int]:
    """Return every numeric id of one prefix cited in backticks."""
    return {int(n) for n in re.findall(rf"`{re.escape(prefix)}-(\d+)`", text)}


def section(text: str, heading_re: str, stop_re: str) -> str:
    """Return the text from a heading to the next heading matched by stop_re."""
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
        """Re-derive every parsed view from the raw source texts."""
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
    """Return every DD table row in file order, duplicates included."""
    out = []
    for ln in text.splitlines():
        m = re.match(r"^\|\s*`?(DD-\d{3})`?\s*\|", ln)
        if m:
            out.append(cells(ln))
    return out


def _gates(main_text: str) -> dict[str, str]:
    """Parse the P12A gate table into {gate id: status token}.

    Only the Result cell (column 6) counts. Searching the whole row would let a
    status word in the evidence, limitation or action cell decide the gate.
    """
    out: dict[str, str] = {}
    for ln in main_text.splitlines():
        m = re.match(r"^\|\s*`?(P12A-\d{2})`?\s*\|", ln)
        if m:
            row = cells(ln)
            result = row[5] if len(row) > 5 else ""
            toks = STATUS_TOKENS_RE.findall(result)
            out[m.group(1)] = toks[0] if toks else "MISSING"
    return out


def load() -> Model:
    """Build a Model from the eight canonical input files."""
    m = Model()
    for key, path in FILES.items():
        m.src[key] = read(path) if path.exists() else ""
    m.rebuild()
    return m


# --- checks ----------------------------------------------------------------

def check_01(m: Model) -> tuple[bool, str]:
    """Every canonical deliverable and register exists."""
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
        # A token anywhere else in the row (title, finding, implication) must
        # not rescue an empty or invalid Type cell.
        type_cell = c[3].upper()
        if not any(t in type_cell for t in SOURCE_TYPES):
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
    """Every cited source resolves, and every source row is used by something."""
    cited = (citations(m.src["registers"], "12A-RS") | citations(m.src["main"], "12A-RS")
             | citations(m.src["sources"], "12A-RS"))
    # A row's own first cell names the row, so leaving it in the corpus makes
    # every row trivially "cited" and the orphan half of this check vacuous.
    # Strip each defining identifier before harvesting usage.
    stripped = re.sub(r"^\|\s*`12A-RS-\d+`", "", m.src["sources"], flags=re.M)
    usage = (citations(m.src["registers"], "12A-RS") | citations(m.src["main"], "12A-RS")
             | citations(stripped, "12A-RS"))
    dangling = sorted(c for c in cited if c not in m.rs)
    uncited = sorted(n for n in m.rs if n not in usage)
    if dangling:
        return False, f"cited but absent: {dangling[:8]}"
    if uncited:
        return False, f"{len(uncited)} source rows cited only by themselves: {uncited[:8]}"
    return True, (f"all {len(cited)} cited source references resolve and all {len(m.rs)} rows "
                  "are used outside their own defining cell")


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
<<<<<<< HEAD
    disclosure = re.compile(
        r"Fetch failed|could not be read|not read|unreadable|not retrievable|"
        r"corrupted stream|index record only|search-index snippet|excerpt|"
        r"metadata only|body not rendered|403|blocked", re.I)
    need = [n for n in RETRIEVAL_FAILURE_ROWS
            if n in m.rs and disclosure.search(" ".join(m.rs[n]))]
    if flagged < 20:
        return False, f"only {flagged} retrieval-failure statements in the register"
    missing = sorted(set(RETRIEVAL_FAILURE_ROWS) - set(need))
    if missing:
        return False, f"retrieval-failure rows without a disclosure: {missing}"
    unverified = [n for n, c in m.rs.items() if c[-1].startswith("Unverified")]
    return True, (f"{flagged} retrieval statements; all {len(RETRIEVAL_FAILURE_ROWS)} "
                  f"substantive retrieval failures carry a disclosure; "
=======
    unverified = [n for n, c in m.rs.items() if c[-1].startswith("Unverified")]
    need = [n for n, c in m.rs.items()
            if re.search(r"Fetch failed|not read|unreadable|403|blocked", " ".join(c), re.I)]
    if flagged < 20:
        return False, f"only {flagged} retrieval-failure statements in the register"
    if not need:
        return False, "no row admits a retrieval failure; unverifiable claims may be present"
    return True, (f"{flagged} retrieval statements; {len(need)} rows admit they were not read; "
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
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
<<<<<<< HEAD
    if m.req_max < 763 or m.req_max > 869:
        return False, f"global requirement register frontier is REQ-{m.req_max}, expected 763 or the later 12B frontier 869"
=======
    if m.req_max != 763:
        return False, f"global requirement register frontier is REQ-{m.req_max}, expected 763"
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
    rows = re.findall(r"^\|\s*`?REQ-(\d{3})`?\s*\|", m.src["registers"], re.M)
    added = sorted({n for n in rows if int(n) >= 764})
    if added:
        return False, f"12A allocated global requirement rows: {added[:6]}"
    reserved = re.findall(r"REQ-7(?:6[4-9]|7\d|8\d)", m.src["registers"])
    if not reserved:
        return False, "the reserved 12B block is not declared"
<<<<<<< HEAD
    return True, ("12A allocated no global requirement row; REQ-763 was its frontier "
                  f"and REQ-764…REQ-869 now belong to Prompt 12B; {len(reserved)} reservation mentions")
=======
    return True, ("REQ-763 remains the frontier; REQ-764 onward reserved for 12B; "
                  f"{len(reserved)} reservation mentions and no allocated row")
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3


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
<<<<<<< HEAD
    if not re.search(r"\| \*\*153\*\* \| contiguous, no gaps, no duplicates \|", s):
        bad.append("the 153-row total is not stated in §10")
    return (not bad, "sources register totals reconcile (153 / 40 / 18)" if not bad
=======
    if not re.search(r"\| \*\*152\*\* \| contiguous, no gaps, no duplicates \|", s):
        bad.append("the 152-row total is not stated in §10")
    return (not bad, "sources register totals reconcile (152 / 40 / 18)" if not bad
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
            else "; ".join(bad))


def check_18(m: Model) -> tuple[bool, str]:
    """Decision register: contiguous, unique, and the fifteen new rows are complete."""
    ids = sorted(m.d_rows)
    if gaps(ids):
        return False, f"gaps in D- numbering: {gaps(ids)[:8]}"
<<<<<<< HEAD
    if len(ids) < 177 or ids[-1] < 177:
        return False, f"expected at least D-001…D-177, found {len(ids)} rows to max {ids[-1] if ids else 0}"
=======
    if len(ids) != 177 or ids[-1] != 177:
        return False, f"expected D-001…D-177, found {len(ids)} rows to max {ids[-1] if ids else 0}"
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
    incomplete = [n for n in range(163, 178)
                  if n not in m.d_rows or len(m.d_rows[n]) != 8
                  or any(len(c) < 8 for c in m.d_rows[n][3:8])]
    if incomplete:
        return False, f"new decision rows incomplete: {incomplete}"
<<<<<<< HEAD
    return True, f"{len(ids)} decisions, contiguous and unique; D-163…D-177 all carry eight fields"
=======
    return True, "177 decisions, contiguous and unique; D-163…D-177 all carry eight fields"
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3


def check_19(m: Model) -> tuple[bool, str]:
    """Design register: contiguous DD ids, the fifteen new rows, and a reconciling tally."""
    ids = sorted(m.dd_rows)
    if not ids:
        return False, "the design register has no DD rows"
    bad = gaps(ids)
    if bad:
        return False, f"gaps in DD- numbering: {bad[:8]}"
<<<<<<< HEAD
    if ids[-1] < 225 or len(ids) < 225:
        return False, f"expected at least 225 DD rows, found {len(ids)} to max {ids[-1]}"
=======
    if ids[-1] != 225 or len(ids) != 225:
        return False, f"expected 225 DD rows, found {len(ids)} to max {ids[-1]}"
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
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
        declared_value = declared.group(1) if declared else "nothing"
        return False, f"tally rows sum to {total}, register declares {declared_value}"
<<<<<<< HEAD
    return True, f"{len(ids)} DD rows; §6 tally sums to {total} and matches the declared total"
=======
    return True, f"225 DD rows; §6 tally sums to {total} and matches the declared total"
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3


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
    short = [n for n in p1 if len(m.int_p1[n]) < 7 or len(m.int_p2[n]) < 7]
    if short:
        return False, f"short dependency rows: {short[:4]}"
    empty = [n for n in p1 if any(not c for c in m.int_p1[n][1:])
             or any(not c for c in m.int_p2[n][1:])]
    def open_cell(cell: str) -> bool:
        """Accept a populated field even when its wording is short or open-ended."""
        return bool(re.fullmatch(r"(?:None|Owner|Stage \d+|Prompt \d+|12[BC]|1[3-5])", cell)) \
            or bool(re.search(r"OPEN|UD-\d", cell)) or len(cell) >= 8

    thin = [n for n in p1 if len(m.int_p1[n][3]) < 20 or len(m.int_p2[n][3]) < 15
            or not open_cell(m.int_p2[n][6])]
    if empty or thin:
        return False, f"empty field {empty[:4]}; too thin {thin[:4]}"
    return True, f"{len(p1)} dependency rows, each with all twelve fields populated"




def _plain(cell: str) -> str:
    """Strip Markdown emphasis characters from a cell."""
    return re.sub(r"[*`]", "", cell).strip()


BAND_RE = re.compile(r"\b(Low|Medium|High|Critical)\s+(\d{1,2})\b")
LIKELIHOOD_RE = re.compile(r"\bL[1-5]\b")
IMPACT_RE = re.compile(r"\bI[1-5]\b")


def _band_value(cell: str) -> bool:
    """A band cell names a band word and a score on the 1–25 ordinal scale.

    Row-level overrides are legitimate: the register uses e.g. "High 16
    Critical band" and "Critical 10, elevated by breadth", where the word and
    the score deliberately diverge from §5.1's nominal ranges. The check
    therefore requires a band word with an in-range score, not range agreement.
    """
    for match in BAND_RE.finditer(_plain(cell)):
        if 1 <= int(match.group(2)) <= 25:
            return True
    return False


def check_24(m: Model) -> tuple[bool, str]:
    """Threat rows: three halves aligned, class and ordinal assessment present."""
    d, c, r = sorted(m.rk_def), sorted(m.rk_ctl), sorted(m.rk_res)
    if not (d == c == r):
        return False, f"half-set mismatch: def {len(d)}, ctl {len(c)}, res {len(r)}"
    # 5.4 puts the residual in column 8; a row truncated before it ends on the
    # outstanding decision and must not have that cell read as the residual.
    short = [n for n in d if len(m.rk_ctl[n]) < 5 or len(m.rk_res[n]) < 8]
    if short:
        return False, f"short threat rows: {short[:4]}"
    bad_class = [n for n in d
                 if not any(_plain(m.rk_ctl[n][1]).upper().startswith(k) for k in RISK_CLASSES)]
    no_lik = [n for n in d if not LIKELIHOOD_RE.search(_plain(m.rk_ctl[n][2]))]
    no_imp = [n for n in d if not IMPACT_RE.search(_plain(m.rk_ctl[n][3]))]
    bad_band = [n for n in d if not _band_value(m.rk_ctl[n][4])]
    no_res = [n for n in d if len(_plain(m.rk_res[n][7])) < 3]
    if bad_class or no_lik or no_imp or bad_band or no_res:
        return False, (f"bad class {bad_class[:4]}; no L token {no_lik[:4]}; "
                       f"no I token {no_imp[:4]}; bad band {bad_band[:4]}; "
                       f"no residual {no_res[:4]}")
    return True, (f"{len(d)} threat rows with evidence class, explicit L and I scores, "
                  "a risk band and a stated residual")




def check_25(m: Model) -> tuple[bool, str]:
    """Every threat names a preventive control, a detection control and a requirement."""
    d, c, r = sorted(m.rk_def), sorted(m.rk_ctl), sorted(m.rk_res)
    if not (d == c == r):
        return False, f"half-set mismatch: def {len(d)}, ctl {len(c)}, res {len(r)}"
    short = [n for n in d if len(m.rk_ctl[n]) < 7 or len(m.rk_res[n]) < 2]
    if short:
        return False, f"short threat rows: {short[:4]}"
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
<<<<<<< HEAD
    if not re.fullmatch(r"D-001\.\.D-1(?:77|87)", first["decisions_range"]):
=======
    if first["decisions_range"] != "D-001..D-177":
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
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


def _claim_sentence(text: str, start: int, end: int) -> str:
    """Return the single sentence that contains text[start:end].

    Negation only excuses a claim when it is part of the same statement: an
    unrelated "not" earlier in the paragraph must not neutralise a real claim.
    """
    left = 0
    for m in re.finditer(r"[.!?\n]", text[:start]):
        left = m.end()
    nxt = re.search(r"[.!?\n]", text[end:])
    right = end + nxt.start() + 1 if nxt else len(text)
    return text[left:right]


def _claim_context(text: str, start: int, end: int) -> str:
    """Return the sentence, or the table cell, that contains the claim.

    A Markdown table row is one line, so a whole-sentence search would let a
    "no" in one cell excuse a claim in another cell of the same row. When the
    claim sits in a table, only its own cell is the context.
    """
    row_start = text.rfind("\n", 0, start) + 1
    row_end = text.find("\n", end)
    if row_end == -1:
        row_end = len(text)
    row = text[row_start:row_end]
    if row.lstrip().startswith("|"):
        rel_start, rel_end = start - row_start, end - row_start
        left = row.rfind("|", 0, rel_start)
        right = row.find("|", rel_end)
        return row[left + 1:right if right != -1 else len(row)]
    return _claim_sentence(text, start, end)


def check_33(m: Model) -> tuple[bool, str]:
    """No implementation, no executed test and no legal conclusion is claimed."""
    impl, legal, promo = [], [], []
    for key in ("main", "registers", "sources"):
        text = m.src[key]
        for pat in IMPLEMENTATION_CLAIMS:
            for mt in re.finditer(pat, text, re.I):
                # "only" narrows scope; it does not disclaim a claim. A negation
                # in a neighbouring table cell does not disclaim it either.
                context = _claim_context(text, mt.start(), mt.end())
                if not re.search(r"\b(?:not|nothing|never|without|no)\b",
                                 context, re.I):
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


<<<<<<< HEAD
# --- 12A-C1 reconciliation constants (2026-11-07) ---------------------------
# These sets are the canonical access classification documented in register
# §10.1. They are deliberately explicit: a row moving between classes must be
# accompanied by a documentation change, not silently absorbed.
NOT_FULL_ROWS = {17, 21, 22, 30, 37, 38, 39, 77, 103, 127, 129, 132, 152}
PARTIAL_ROWS = {21, 22, 37, 38, 77, 103, 127, 129, 132}
INACCESSIBLE_ROWS = {17, 30, 39}
SNIPPET_ROWS = {21, 22, 37, 77}
RETRIEVAL_FAILURE_ROWS = {17, 21, 22, 30, 39, 77, 127, 129, 132}
INTERNAL_FINDING_ROWS = {152}
ABSENCE_FINDING_ROWS = {152}

AGCM_URL = ("https://en.agcm.it/en/media/press-releases/2026/10/"
            "EU-level-coordinated-actions-in-the-gaming-sector-"
            "The-Italian-Competition-Authority-is-leading-action-in-relation-to-"
            "Microsoft-group-video-games")


def confidence_totals(m: Model) -> dict[str, int]:
    """Count rows by the leading token of the confidence cell."""
    counts = {token: 0 for token in CONFIDENCE_TOKENS}
    for _, row in m.rs.items():
        for token in CONFIDENCE_TOKENS:
            if row[-1].startswith(token):
                counts[token] += 1
                break
    return counts


def _access_row_ids(text: str, label: str) -> set[int]:
    """Return the source ids listed on an access-class table row."""
    for line in text.splitlines():
        if line.startswith(f"| {label}"):
            return {int(n) for n in re.findall(r"12A-RS-(\d+)", line)}
    return set()


def _access_row_count(text: str, label: str) -> int | None:
    """Return the final count cell on an access-class table row."""
    for line in text.splitlines():
        if line.startswith(f"| {label}"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            nums = re.findall(r"\d+", cells[-1])
            return int(nums[-1]) if nums else None
    return None


def check_36(m: Model) -> tuple[bool, str]:
    """The report's §5 benchmark range agrees with the register's 40 rows."""
    seg = section(m.src["main"], r"^## 5\. ", r"^## 6\. ")
    ids = {int(n) for n in re.findall(r"12A-BM-(\d+)", seg)}
    declared = re.search(r"\| Benchmark mechanisms \| (\d+) \|", m.src["sources"])
    declared_n = int(declared.group(1)) if declared else None
    if len(m.bm) != EXPECTED["12A-BM"]:
        return False, f"benchmark rows {len(m.bm)}, expected {EXPECTED['12A-BM']}"
    if not ids:
        return False, "§5 cites no 12A-BM identifier"
    if max(ids) != len(m.bm):
        return False, f"§5 benchmark range ends at {max(ids)}, register has {len(m.bm)}"
    if declared_n != len(m.bm):
        return False, f"register declares {declared_n} benchmarks, rows are {len(m.bm)}"
    return True, f"§5 and the register agree on {len(m.bm)} benchmark mechanisms"


def check_37(m: Model) -> tuple[bool, str]:
    """The report's §5 comparator range agrees with the register's 18 profiles."""
    seg = section(m.src["main"], r"^## 5\. ", r"^## 6\. ")
    ids = {int(n) for n in re.findall(r"12A-CMP-(\d+)", seg)}
    declared = re.search(r"\| Comparator profiles \| (\d+) \|", m.src["sources"])
    declared_n = int(declared.group(1)) if declared else None
    if len(m.cmp_) != EXPECTED["12A-CMP"]:
        return False, f"comparator rows {len(m.cmp_)}, expected {EXPECTED['12A-CMP']}"
    if not ids:
        return False, "§5 cites no 12A-CMP identifier"
    if max(ids) != len(m.cmp_):
        return False, f"§5 comparator range ends at {max(ids)}, register has {len(m.cmp_)}"
    if declared_n != len(m.cmp_):
        return False, f"register declares {declared_n} comparators, rows are {len(m.cmp_)}"
    return True, f"§5 and the register agree on {len(m.cmp_)} comparator profiles"


def check_38(m: Model) -> tuple[bool, str]:
    """The confidence summary agrees with the rows in both documents."""
    counts = confidence_totals(m)
    reg = re.search(
        r"`High` \*\*(\d+)\*\* · `Medium` \*\*(\d+)\*\* · `Low` \*\*(\d+)\*\* · "
        r"`Unverified` \*\*(\d+)\*\*", m.src["sources"])
    main = re.search(
        r"`High` \*\*(\d+)\*\*, `Medium` \*\*(\d+)\*\*, `Low` \*\*(\d+)\*\* and "
        r"`Unverified` \*\*(\d+)\*\*", m.src["main"])
    if not reg or not main:
        return False, "confidence summary missing from the register or the report"
    reg_v = tuple(int(x) for x in reg.groups())
    main_v = tuple(int(x) for x in main.groups())
    want = tuple(counts[t] for t in CONFIDENCE_TOKENS)
    if reg_v != want:
        return False, f"register confidence {reg_v}, rows are {want}"
    if main_v != want:
        return False, f"report confidence {main_v}, rows are {want}"
    shown = " · ".join(f"{k} {v}" for k, v in counts.items())
    return True, f"confidence summary reconciles in both documents: {shown}"


def check_39(m: Model) -> tuple[bool, str]:
    """Access classification is complete, row-linked and totals 153."""
    s = m.src["sources"]
    partial = _access_row_ids(s, "Read partially or through extracts")
    inaccessible = _access_row_ids(s, "Inaccessible or unreadable")
    internal = _access_row_ids(s, "Internal research finding")
    snippet = _access_row_ids(s, "Search-index or snippet-only (flag)")
    failure = _access_row_ids(s, "Substantive retrieval failure (flag)")
    absence = _access_row_ids(s, "Absence-of-evidence finding (flag)")
    expected = {
        "partial": PARTIAL_ROWS, "inaccessible": INACCESSIBLE_ROWS,
        "internal": INTERNAL_FINDING_ROWS, "snippet": SNIPPET_ROWS,
        "failure": RETRIEVAL_FAILURE_ROWS, "absence": ABSENCE_FINDING_ROWS,
    }
    found = {"partial": partial, "inaccessible": inaccessible, "internal": internal,
             "snippet": snippet, "failure": failure, "absence": absence}
    wrong = [k for k in expected if found[k] != expected[k]]
    if wrong:
        return False, f"access-class rows disagree: {wrong}"
    counts = {
        "full": _access_row_count(s, "Read in full"),
        "partial": _access_row_count(s, "Read partially or through extracts"),
        "inaccessible": _access_row_count(s, "Inaccessible or unreadable"),
        "internal": _access_row_count(s, "Internal research finding"),
        "snippet": _access_row_count(s, "Search-index or snippet-only (flag)"),
        "failure": _access_row_count(s, "Substantive retrieval failure (flag)"),
        "absence": _access_row_count(s, "Absence-of-evidence finding (flag)"),
    }
    want = {"full": len(m.rs) - len(NOT_FULL_ROWS), "partial": len(PARTIAL_ROWS),
            "inaccessible": len(INACCESSIBLE_ROWS),
            "internal": len(INTERNAL_FINDING_ROWS), "snippet": len(SNIPPET_ROWS),
            "failure": len(RETRIEVAL_FAILURE_ROWS),
            "absence": len(ABSENCE_FINDING_ROWS)}
    bad = [f"{k} {counts[k]}!={want[k]}" for k in want if counts[k] != want[k]]
    if bad:
        return False, "access-class counts disagree: " + ", ".join(bad)
    total = _access_row_count(s, "**Access-class total**")
    if total != len(m.rs):
        return False, f"access classes total {total}, rows are {len(m.rs)}"
    report = m.src["main"]
    if "140 rows read in full" not in report or "13 rows not read in full" not in report:
        return False, "the report does not state the 140 full-read / 13 not-full split"
    if "Nine rows are substantive retrieval failures" not in report:
        return False, "the report does not state the nine substantive retrieval failures"
    return True, (f"{want['full']} full · {want['partial']} partial · "
                  f"{want['inaccessible']} inaccessible · {want['internal']} internal; "
                  f"flags: {want['snippet']} snippet, {want['failure']} failures, "
                  f"{want['absence']} absence")


def check_40(m: Model) -> tuple[bool, str]:
    """The register's type vocabulary and source classes match the validator."""
    seg = section(m.src["sources"], r"^### 1\.3 ", r"^### 1\.4 ")
    if not seg:
        return False, "the source-type vocabulary section is missing"
    classes = ("| `EXTERNAL` |", "| `INTERNAL RESEARCH FINDING` |",
               "| `ABSENCE-OF-EVIDENCE FINDING` |")
    missing_classes = [c for c in classes if c not in seg]
    if missing_classes:
        return False, f"source-class rows missing: {missing_classes}"
    type_part = seg.split("| Type | Meaning | Weight |", 1)
    if len(type_part) != 2:
        return False, "the source-type table header is missing"
    vocab = set(re.findall(r"^\| `([A-Z][A-Z -]+)` \|", type_part[1], re.M))
    if vocab != set(SOURCE_TYPES):
        return False, (f"register vocabulary {sorted(vocab)} != validator "
                       f"{sorted(SOURCE_TYPES)}")
    return True, (f"{len(vocab)} source types and 3 source classes agree between "
                  "the register and the validator")


def check_41(m: Model) -> tuple[bool, str]:
    """RS-152 is an internal absence finding, not an external source."""
    row = m.rs.get(152)
    if not row:
        return False, "RS-152 is missing"
    type_cell = row[3].upper()
    ref = row[1].lower()
    limit = row[5].lower()
    finding = row[4].lower()
    problems = []
    if not type_cell.startswith("RESEARCH FINDING"):
        problems.append("type is not RESEARCH FINDING")
    if "absence" not in type_cell.lower():
        problems.append("type does not name the absence class")
    if "no external url" not in ref or "http" in ref:
        problems.append("reference presents it as an external URL")
    if "not an external publication" not in limit:
        problems.append("limitation does not deny external publication")
    if "retrievable" not in finding:
        problems.append("finding does not record the absence")
    if not row[-1].startswith("High"):
        problems.append("confidence is not the recorded High absence rating")
    if "12A-RS-152" not in m.src["main"] or "absence finding" not in m.src["main"].lower():
        problems.append("the report does not cite it as an absence finding")
    if problems:
        return False, "RS-152 classification: " + "; ".join(problems)
    return True, "RS-152 is registered as an internal absence-of-evidence finding"


def check_42(m: Model) -> tuple[bool, str]:
    """RS-153 records the AGCM action accurately and is cited with its limits."""
    row = m.rs.get(153)
    if not row:
        return False, "RS-153 is missing"
    ref, date, type_cell = row[1], row[2], row[3].upper()
    finding, limit = row[4].lower(), row[5].lower()
    problems = []
    if AGCM_URL not in ref:
        problems.append("official AGCM URL absent")
    if "2026-10-08" not in date or "2026-11-07" not in date:
        problems.append("publication or retrieval date missing")
    if "REGULATOR" not in type_cell:
        problems.append("type is not REGULATOR")
    for token in ("widespread infringement", "activision blizzard uk", "norway",
                  "denmark", "virtual currenc", "dark pattern", "parental control",
                  "blocked"):
        if token not in finding:
            problems.append(f"finding omits {token!r}")
    for token in ("ongoing", "no infringement finding", "no automatic legal obligation",
                  "ud-017"):
        if token not in limit:
            problems.append(f"limitation omits {token!r}")
    report = m.src["main"]
    for token in ("12A-RS-153", "not a final finding", "monetisation model",
                  "jurisdictions", "UD-017"):
        if token not in report:
            problems.append(f"report omits {token!r}")
    if problems:
        return False, "RS-153 registration: " + "; ".join(problems)
    return True, "RS-153 records the ongoing 8 October 2026 AGCM action with its limits"


def check_43(m: Model) -> tuple[bool, str]:
    """P12A-05 and the narrative use D-176/DD-224 for the residual."""
    d176 = " ".join(m.d_rows.get(176, []))
    d177 = " ".join(m.d_rows.get(177, []))
    dd224 = " ".join(m.dd_rows.get(224, []))
    dd225 = " ".join(m.dd_rows.get(225, []))
    problems = []
    if "accepted critical residual" not in d176.lower():
        problems.append("D-176 is not the accepted critical residual")
    if "reliably detected" not in d176.lower():
        problems.append("D-176 does not state the reliable-detection limit")
    if "posture" not in d177.lower() or "prevention-heavy" not in d177.lower():
        problems.append("D-177 is not the prevention-heavy posture")
    if "accepted critical residual" not in dd224.lower():
        problems.append("DD-224 is not the accepted critical residual")
    if "prevention-heavy" not in dd225.lower():
        problems.append("DD-225 is not the prevention-heavy posture")
    p05 = next((ln for ln in m.src["main"].splitlines()
                if ln.startswith("| `P12A-05`")), "")
    if "D-176" not in p05 or "DD-224" not in p05:
        problems.append("P12A-05 does not cite D-176 / DD-224")
    if "D-177" in p05 or "D-164" in p05:
        problems.append("P12A-05 still cites the wrong decision")
    if re.search(r"D-177[^.\n]{0,60}(?:accepted critical residual|the residual)",
                 m.src["main"], re.I):
        problems.append("the narrative still pairs D-177 with the residual")
    if problems:
        return False, "decision cross-reference: " + "; ".join(problems)
    return True, "D-176/DD-224 hold the residual and P12A-05 cites them correctly"


def check_44(m: Model) -> tuple[bool, str]:
    """Multi-account wording is precise and distinguishes identity from conduct."""
    text = m.src["main"]
    forbidden = [r"\bundetectable\b", r"\bnot detectable\b", r"\bcannot be detected\b",
                 r"\bimpossible to detect\b"]
    hits = [p for p in forbidden if re.search(p, text, re.I)]
    if hits:
        return False, f"absolute multi-account wording remains: {hits}"
    canonical = ("Identity-layer multi-accounting cannot be reliably detected "
                 "under the current fixed constraints")
    if canonical.lower() not in text.lower():
        return False, "the canonical identity-layer detection sentence is absent"
    if "behavioural, transactional and outcome evidence" not in text.lower():
        return False, "the report does not distinguish identity proof from coordinated-abuse evidence"
    return True, ("no absolute detection wording; the canonical limit and the "
                  "behavioural/transactional/outcome distinction are present")


def check_45(m: Model) -> tuple[bool, str]:
    """The global access-date statement agrees with the per-row retrieval records."""
    seg = section(m.src["sources"], r"^### 1\.5 ", r"^### 1\.6 ")
    if not seg:
        return False, "the access-date section is missing"
    problems = []
    if re.search(r"All rows were accessed \*\*2026-11-06\*\*", seg):
        problems.append("the unqualified global access date remains")
    if "2026-11-06" not in seg or "2026-11-07" not in seg:
        problems.append("the two corpus dates are not both stated")
    if not re.search(r"`12A-RS-001` through `12A-RS-152`", seg):
        problems.append("the original corpus range is not stated")
    if "12A-RS-153" not in seg:
        problems.append("the RS-153 exception is not stated")
    row153 = m.rs.get(153)
    if not row153 or "2026-11-07" not in " ".join(row153):
        problems.append("RS-153 does not record its 2026-11-07 retrieval")
    others = [n for n, c in m.rs.items()
              if n != 153 and "retrieved 2026-11-07" in " ".join(c)]
    if others:
        problems.append(f"other rows claim the 2026-11-07 access date: {sorted(others)}")
    if problems:
        return False, "access-date statement: " + "; ".join(problems)
    return True, ("the 2026-11-06 original corpus and the 2026-11-07 "
                  "RS-153 addition are stated consistently")


=======
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
# --- registry ----------------------------------------------------------------

@dataclass
class _Check:
    cid: str
    name: str
    fn: object


CHECKS: list = []


def _register():
    """Populate CHECKS from the check specification table."""
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
<<<<<<< HEAD
        ("12A-36", "benchmark count agrees across report and register", check_36),
        ("12A-37", "comparator count agrees across report and register", check_37),
        ("12A-38", "source confidence summary agrees with the rows", check_38),
        ("12A-39", "source-access classification complete and reconciled", check_39),
        ("12A-40", "source taxonomy agrees between register and validator", check_40),
        ("12A-41", "RS-152 is an internal absence finding", check_41),
        ("12A-42", "RS-153 AGCM registration and citation are correct", check_42),
        ("12A-43", "D-176/DD-224 residual references are correct", check_43),
        ("12A-44", "multi-account wording is precise, not absolute", check_44),
        ("12A-45", "global access date agrees with per-row retrieval records", check_45),
=======
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
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
    reason: str = ""


def _drop_line(text: str, needle: str) -> str:
    """Remove the first line containing needle, or fail loudly."""
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if needle in ln:
            return "".join(lines[:i] + lines[i + 1:])
    raise AssertionError("fixture needle absent: " + needle[:50])


def _dup_line(text: str, needle: str) -> str:
    """Duplicate the first line containing needle, or fail loudly."""
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if needle in ln:
            return "".join(lines[:i] + [ln] + lines[i:])
    raise AssertionError("fixture needle absent: " + needle[:50])


def _sub(text: str, old: str, new: str) -> str:
    """Replace one occurrence of old with new, or fail loudly."""
    if old not in text:
        raise AssertionError("fixture needle absent: " + old[:50])
    return text.replace(old, new, 1)


def fx_missing_source(model):
    """Fixture: delete one research source row."""
    model.src["sources"] = _drop_line(model.src["sources"], "`12A-RS-077`")
    model.rebuild()
    return model


def fx_dangling_source_ref(model):
    """Fixture: cite a source id that does not exist."""
    model.src["registers"] = _sub(model.src["registers"], "`12A-RS-001`, `12A-RS-002`",
                                  "`12A-RS-901`, `12A-RS-002`")
    model.rebuild()
    return model


def fx_duplicate_requirement(model):
    """Fixture: duplicate one candidate requirement row."""
    model.src["registers"] = _dup_line(model.src["registers"], "| `12A-CR-030` |")
    model.rebuild()
    return model


def fx_no_verification_intent(model):
    """Fixture: remove a requirement's verification approach, keeping its rationale."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "| Custody review; rotation-plan existence check |",
        "|  |")
    model.rebuild()
    return model


def fx_unsupported_approval(model):
    """Fixture: mark a candidate requirement Approved."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "its notice and its appeal route | Moderation | B | New proposal",
        "its notice and its appeal route | Moderation | B | Approved")
    model.rebuild()
    return model


def fx_owner_row_closed(model):
    """Fixture: close an owner-reserved unresolved row."""
    model.src["ud"] = _sub(
        model.src["ud"],
        "| Open — awaiting explicit owner decision on what a member can "
        "appeal and who decides; 09B supplies candidate options only |",
        "| **Resolved** by Prompt 12A |")
    model.rebuild()
    return model


def fx_missing_dependency_half(model):
    """Fixture: remove one half of a dependency pair."""
    model.src["registers"] = _drop_line(model.src["registers"], "| `12A-INT-25` | Aggregate only |")
    model.rebuild()
    return model


def fx_duplicate_decision(model):
    """Fixture: duplicate one DD design row."""
    model.src["dd"] = _dup_line(model.src["dd"], "| DD-214 |")
    model.rebuild()
    return model


def fx_contradictory_classification(model):
    """Fixture: remove a category's three-axis assignment."""
    model.src["main"] = _sub(
        model.src["main"],
        "| `12A-IC-06` | Military-confidential information | Private | "
        "`NATION_OWNER` | S | B-10 |",
        "| `12A-IC-06` | Military-confidential information |  |  |  | B-10 |")
    model.rebuild()
    return model


def fx_legal_overreach(model):
    """Fixture: assert an unsupported legal conclusion."""
    model.src["main"] = _sub(model.src["main"], "## 28. Conclusions",
                             "The GDPR is binding on the project and we are DSA compliant."
                             "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_untraceable_assertion(model):
    """Fixture: remove the source citation from a benchmark row."""
    model.src["sources"] = _sub(
        model.src["sources"],
        "obligation for 12B | `12A-RS-121` |",
        "obligation for 12B | — |")
    model.rebuild()
    return model


def fx_illegal_gate_status(model):
    """Fixture: replace a gate status with an undefined token."""
    model.src["main"] = _sub(
        model.src["main"],
        "checks `12A-23`, `12A-09` | **PASS**",
        "checks `12A-23`, `12A-09` | **DONE**")
    model.rebuild()
    return model


def fx_implementation_claim(model):
    """Fixture: claim that a control is implemented."""
    model.src["main"] = _sub(model.src["main"], "## 28. Conclusions",
                             "The moderation service is now implemented."
                             "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_implementation_claim_after_negation(model):
    """A negation in an earlier sentence must not excuse a later real claim."""
    model.src["main"] = _sub(model.src["main"], "## 28. Conclusions",
                             "This pass adds no implementation and no test run."
                             "\n\nThe moderation service is now implemented."
                             "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_totals_drift(model):
    """Fixture: change a declared register total."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "| Candidate requirements | `12A-CR-###` | `12A-CR-001` … `12A-CR-106` | **106** |",
        "| Candidate requirements | `12A-CR-###` | `12A-CR-001` … `12A-CR-106` | **140** |")
    model.rebuild()
    return model


def fx_protected_decision_changed(model):
    """Fixture: supersede a protected decision."""
    model.src["decisions"] = _sub(model.src["decisions"],
                                  "| **Confirmed** (policy) | Resolves UD-014's policy half.",
                                  "| **Superseded** by Prompt 12A | Resolves UD-014's policy half.")
    model.rebuild()
    return model


def fx_staging_only_implementation_claim(model):
    """Fixture: "only" narrows scope; it must not excuse an implementation claim."""
    model.src["main"] = _sub(model.src["main"], "## 28. Conclusions",
                             "The moderation service is implemented only in staging."
                             "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_cross_cell_negation(model):
    """Fixture: a "no" in a neighbouring table cell must not excuse the claim."""
    model.src["main"] = _sub(
        model.src["main"], "## 28. Conclusions",
        "| No implementation is claimed here | The moderation service is now implemented. |"
        "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_illegal_gate_result(model):
    """Fixture: Result cell illegal while another cell carries a legal token."""
    model.src["main"] = _sub(
        model.src["main"],
        "**PASS** | Classification is of documentation state",
        "**DONE** | PASS is recorded in this cell for the fixture")
    model.rebuild()
    return model


def fx_missing_likelihood_token(model):
    """Fixture: a likelihood cell carries prose instead of an L1–L5 score."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "| L2 — needs deliberate scripting near a boundary | I4 |",
        "| Likely — needs deliberate scripting near a boundary | I4 |")
    model.rebuild()
    return model


def fx_band_without_score(model):
    """Fixture: a risk band names the band but carries no ordinal score."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "| I4 | High 8 | `CR-008` |",
        "| I4 | High | `CR-008` |")
    model.rebuild()
    return model


def fx_band_out_of_range(model):
    """Fixture: a risk band score falls outside the 1–25 ordinal scale."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "| I4 | High 8 | `CR-008` |",
        "| I4 | High 99 | `CR-008` |")
    model.rebuild()
    return model


def fx_missing_residual_column(model):
    """Fixture: truncate a 5.4 row before its residual-risk column."""
    model.src["registers"] = _sub(
        model.src["registers"],
        "| None | **Zero by design** — and unproven until a build exists |",
        "| None |")
    model.rebuild()
    return model


<<<<<<< HEAD
def fx_bm_range_short(model):
    """Fixture: the report's §5 benchmark range stops short of the register."""
    model.src["main"] = _sub(
        model.src["main"],
        "`12A-BM-001` … `12A-BM-040`",
        "`12A-BM-001` … `12A-BM-032`")
    model.rebuild()
    return model


def fx_cmp_range_short(model):
    """Fixture: the report's §5 comparator range stops short of the register."""
    model.src["main"] = _sub(
        model.src["main"],
        "`12A-CMP-01` … `12A-CMP-18`",
        "`12A-CMP-01` … `12A-CMP-12`")
    model.rebuild()
    return model


def fx_confidence_drift(model):
    """Fixture: the register's High count disagrees with the source rows."""
    model.src["sources"] = _sub(
        model.src["sources"],
        "`High` **65** ·",
        "`High` **64** ·")
    model.rebuild()
    return model


def fx_access_full_drift(model):
    """Fixture: the full-read count disagrees with the access classes."""
    model.src["sources"] = _sub(
        model.src["sources"],
        "| All rows except the 13 below | **140** |",
        "| All rows except the 13 below | **141** |")
    model.rebuild()
    return model


def fx_missing_research_type(model):
    """Fixture: the internal RESEARCH FINDING type is dropped from the vocabulary."""
    model.src["sources"] = _drop_line(
        model.src["sources"],
        "| `RESEARCH FINDING` | This pass's own internal finding")
    model.rebuild()
    return model


def fx_rs152_externalised(model):
    """Fixture: RS-152 is retyped as an external operator source."""
    model.src["sources"] = _sub(
        model.src["sources"],
        "| RESEARCH FINDING (absence of evidence) |",
        "| OFFICIAL-OPERATOR |")
    model.rebuild()
    return model


def fx_rs153_date_drift(model):
    """Fixture: RS-153 carries the wrong publication date."""
    model.src["sources"] = _sub(
        model.src["sources"],
        "2026-10-08 (retrieved 2026-11-07)",
        "2026-10-09 (retrieved 2026-11-07)")
    model.rebuild()
    return model


def fx_p12a05_wrong_decision(model):
    """Fixture: P12A-05 cites the posture decision instead of the residual."""
    model.src["main"] = _sub(
        model.src["main"],
        "this report §8; `D-176` / `DD-224`",
        "this report §8; `D-177` / `DD-224`")
    model.rebuild()
    return model


def fx_absolute_multi_account(model):
    """Fixture: an absolute undetectability claim reappears."""
    model.src["main"] = _sub(
        model.src["main"],
        "## 28. Conclusions",
        "Identity-layer multi-accounting is undetectable."
        "\n\n## 28. Conclusions")
    model.rebuild()
    return model


def fx_access_date_collapse(model):
    """Fixture: the global statement dates the RS-153 addition to 2026-11-06."""
    model.src["sources"] = _sub(
        model.src["sources"],
        "`12A-RS-153` was added and retrieved on **2026-11-07**",
        "`12A-RS-153` was also accessed on **2026-11-06**")
    model.rebuild()
    return model


=======
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
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
    Fixture("12A-N01", "12A-02", False, fx_missing_source,
            "a research source row is deleted", "gaps"),
    Fixture("12A-N02", "12A-05", False, fx_dangling_source_ref,
            "a claim cites a nonexistent source", "cited but absent"),
    Fixture("12A-N03", "12A-09", False, fx_duplicate_requirement,
            "a requirement id is duplicated", "duplicate"),
    Fixture("12A-N04", "12A-10", False, fx_no_verification_intent,
            "a requirement has no verification", "verification [44]"),
    Fixture("12A-N05", "12A-12", False, fx_unsupported_approval,
            "a candidate is marked Approved", "bad status"),
    Fixture("12A-N06", "12A-22", False, fx_owner_row_closed,
            "an owner-reserved row is closed", "not open"),
    Fixture("12A-N07", "12A-23", False, fx_missing_dependency_half,
            "a dependency half is removed", "half-row mismatch"),
    Fixture("12A-N08", "12A-19", False, fx_duplicate_decision,
            "a design position id is duplicated", "duplicates"),
    Fixture("12A-N09", "12A-35", False, fx_contradictory_classification,
            "a category loses its axis assignment", "axis value"),
    Fixture("12A-N10", "12A-33", False, fx_legal_overreach,
            "an unsupported legal conclusion", "we are (?:GDPR|DSA|COPPA) co"),
    Fixture("12A-N11", "12A-06", False, fx_untraceable_assertion,
            "a benchmark cites no source", "uncited"),
    Fixture("12A-N12", "12A-30", False, fx_illegal_gate_status,
            "a gate uses an illegal status", "illegal status"),
    Fixture("12A-N13", "12A-33", False, fx_implementation_claim,
            "an implementation claim appears", "implementation"),
    Fixture("12A-N14", "12A-16", False, fx_totals_drift,
            "a declared total drifts", "totals table disagrees"),
    Fixture("12A-N15", "12A-20", False, fx_protected_decision_changed,
            "a protected decision is superseded", "superseded"),
    Fixture("12A-N16", "12A-33", False, fx_implementation_claim_after_negation,
            "an unrelated negation must not suppress a real implementation claim",
            "implementation"),
    Fixture("12A-N17", "12A-33", False, fx_staging_only_implementation_claim,
            "an implementation claim qualified only by scope is still a claim",
            "implementation"),
    Fixture("12A-N18", "12A-33", False, fx_cross_cell_negation,
            "a negation in another table cell must not suppress the claim",
            "implementation"),
    Fixture("12A-N19", "12A-30", False, fx_illegal_gate_result,
            "an illegal Result cell is not rescued by a legal token elsewhere",
            "illegal status"),
    Fixture("12A-N20", "12A-24", False, fx_missing_likelihood_token,
            "a likelihood cell has no L1–L5 token", "no L token"),
    Fixture("12A-N21", "12A-24", False, fx_band_without_score,
            "a risk band has no ordinal score", "bad band"),
    Fixture("12A-N22", "12A-24", False, fx_band_out_of_range,
            "a risk band score is outside 1–25", "bad band"),
    Fixture("12A-N23", "12A-24", False, fx_missing_residual_column,
            "a threat row is truncated before the residual column",
            "short threat rows"),
<<<<<<< HEAD
    Fixture("12A-N24", "12A-36", False, fx_bm_range_short,
            "the report's benchmark range stops at 32", "§5 benchmark range"),
    Fixture("12A-N25", "12A-37", False, fx_cmp_range_short,
            "the report's comparator range stops at 12", "§5 comparator range"),
    Fixture("12A-N26", "12A-38", False, fx_confidence_drift,
            "the register's High count is one short", "register confidence"),
    Fixture("12A-N27", "12A-39", False, fx_access_full_drift,
            "the full-read count is one above its classes", "access-class counts"),
    Fixture("12A-N28", "12A-40", False, fx_missing_research_type,
            "the internal RESEARCH FINDING type is removed", "register vocabulary"),
    Fixture("12A-N29", "12A-41", False, fx_rs152_externalised,
            "RS-152 is retyped as an external source", "RS-152 classification"),
    Fixture("12A-N30", "12A-42", False, fx_rs153_date_drift,
            "RS-153 carries the wrong publication date", "RS-153 registration"),
    Fixture("12A-N31", "12A-43", False, fx_p12a05_wrong_decision,
            "P12A-05 cites the posture decision", "P12A-05"),
    Fixture("12A-N32", "12A-44", False, fx_absolute_multi_account,
            "an absolute undetectability claim reappears",
            "absolute multi-account"),
    Fixture("12A-N33", "12A-45", False, fx_access_date_collapse,
            "the RS-153 addition is dated to the original access day",
            "access-date statement"),
=======
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
]


# --- runners ----------------------------------------------------------------

def run_checks(model, verbose):
    """Run every check and return the pass count, total and failures."""
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
    """Run the fixture suite against deep-copied models."""
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
        wrong_reason = ""
        if good and not fx.expect and fx.reason:
            detail_l = str(detail).lower()
            # A bare bucket label ("legal", "verification") also occurs in an
            # empty failure bucket ("legal []") printed by a check that failed
            # for a different cause. Require the finding named by the fixture,
            # and reject a reason that only matches an empty bucket.
            empty_bucket = f"{fx.reason.lower()} []" in detail_l
            if fx.reason.lower() not in detail_l or empty_bucket:
                good = False
                why = ("the declared finding bucket is empty"
                       if empty_bucket else
                       f"expected {fx.reason!r} in {str(detail)[:90]!r}")
                wrong_reason = f"; rejected for the wrong reason — {why}"
        if fx.expect:
            pos_n += 1
            pos_ok += 1 if good else 0
        else:
            neg_n += 1
            neg_ok += 1 if good else 0
        if not good:
            want = "accepted" if fx.expect else "rejected"
            got = "accepted" if ok else "rejected"
            problems.append(f"{fx.fid} ({fx.cid}) expected {want}, got {got} "
                            f"({fx.desc}){wrong_reason}")
        if verbose or not good:
            want = "accepted" if fx.expect else "rejected"
            print(f"[{'OK ' if good else 'BAD'}] {fx.fid} {fx.cid} expected to {want} "
                  f"({fx.desc}) -> {ok}: {str(detail)[:110]}")
    return pos_ok, pos_n, neg_ok, neg_n, problems


def main(argv: list) -> int:
    """Parse arguments, run the selected suites and print the verdict."""
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
