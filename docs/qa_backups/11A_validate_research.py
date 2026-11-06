#!/usr/bin/env python3
"""Prompt 11A research-quality validator.

Validates the **research and documentation quality** of the Stage 2 Prompt 11A
deliverable set:

* ``docs/stage-2/research/11A_world_events_objectives_rankings_progression_research.md``
* ``docs/stage-2/research/11A_comparator_sources_and_benchmarks.md``
* ``docs/stage-2/research/11A_integration_and_risk_registers.md``

It implements the twenty-six checks required by the Prompt 11A brief §24 plus
identifier-integrity and claim-versus-actual count checks.

**This is a document checker. It is not a game test.** It validates none of:
event behaviour, ranking arithmetic, reward conservation, privacy enforcement,
exploitation resistance or playability. No rule it checks is implemented,
executed or balanced; it confirms only that the research record exists, is
traceable, is internally consistent and does not overstate its own status.

Run from anywhere: paths resolve relative to this file.

    python 11A_validate_research.py
    python 11A_validate_research.py --verbose
    python 11A_validate_research.py --self-test

Exit code is 0 only when every check passes.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

QA_DIR = Path(__file__).resolve().parent
DOCS = QA_DIR.parent
RESEARCH = DOCS / "stage-2" / "research"

MAIN = RESEARCH / "11A_world_events_objectives_rankings_progression_research.md"
COMPARATOR = RESEARCH / "11A_comparator_sources_and_benchmarks.md"
REGISTERS = RESEARCH / "11A_integration_and_risk_registers.md"

# Project registers C29 reads. They are inputs to the historical-allocation
# check, not 11A deliverables, but they are listed here so the self-test can
# seed a defect into an in-memory copy instead of editing the live register.
REQUIREMENTS = DOCS / "stage-2" / "03_requirements_traceability.md"
DECISIONS = DOCS / "DECISIONS.md"

FILES = {"main": MAIN, "comparator": COMPARATOR, "registers": REGISTERS,
         "requirements": REQUIREMENTS, "decisions": DECISIONS}

# The documents 11A actually owns. C24 and C25 scan these only; the project
# registers are inputs to C29 and carry other prompts' legitimate history.
DELIVERABLE_KEYS = ("main", "comparator", "registers")

# The last global requirement that existed when Prompt 11A closed (2026-11-05).
# 11A allocated none of its own; 11B later allocated REQ-704..REQ-763 lawfully.
# A later prompt that allocates outside its sanctioned range is a failure, which
# is what makes this a boundary check rather than a maximum check.
HISTORICAL_REQ_MAX = 703
# The recorded 11B allocation and the highest ID it covers. Anything above this
# may be a future legitimate allocation and is judged on its owner token, not on
# its number, so later work cannot retroactively fail the 11A check.
KNOWN_LATER_MAX = 763
KNOWN_PROMPT_OWNER = re.compile(r"^(?:(?:0[2-9]|1[0-5])[ABC]?|all)$")
# REQ-704..REQ-763 are 11B's, except two conditional rows whose decision is
# explicitly downstream: REQ-748 belongs to Prompt 12 and REQ-752 to Prompt 14.
# Any other owner in the block, including 12/14 on the wrong row, is a
# misattribution.
LATER_BLOCK_DEFAULT_OWNER = "11B"
LATER_BLOCK_OWNER_BY_NUMBER = {748: "12", 752: "14"}

GAMES = [
    "Politics & War",
    "NationStates",
    "Supremacy 1914",
    "Travian",
    "eRepublik",
    "Call of War",
    "Tribal Wars",
]

# Registers that must exist with an exact cardinality, and the file that owns them.
ID_CARDINALITY = {
    "11A-RS": (COMPARATOR, 114),
    "11A-BM": (COMPARATOR, 73),
    "11A-INT": (REGISTERS, 40),
    "11A-RK": (REGISTERS, 28),
    "11A-CR": (REGISTERS, 30),
    "11A-OPEN": (REGISTERS, 16),
    "11A-DR": (MAIN, 34),
}

# Owner-reserved or fixed decisions that 11A must never present as changed.
PROTECTED_IDS = [
    "D-014", "D-015", "D-021", "D-027", "D-028", "D-032",
    "D-122", "D-137", "D-140", "D-141", "D-142", "D-143",
]

# Phrases that would claim implementation, execution or release of gameplay.
IMPLEMENTATION_CLAIMS = [
    r"\b(?:is|are|has been|have been)\s+(?:now\s+)?implemented\b",
    r"\b(?:is|are|has been|have been)\s+(?:now\s+)?deployed\b",
    r"\b(?:was|were)\s+released\s+(?:to\s+production|live)\b",
    r"\bruns?\s+in\s+production\b",
    r"\bgo(?:es)?\s+live\b",
    r"\bimplemented\s+and\s+tested\b",
]

# Words that turn an implementation phrase into an explicit denial. The record is
# full of sentences such as "Nothing is implemented", which must not be flagged.
NEGATION_MARKERS = re.compile(
    r"\b(?:not|nothing|neither|never|without|only|zero|no)\b", re.I)

# Phrases that would wrongly mark a deferred gate or owner decision as satisfied.
# The auxiliary verb must sit directly against the state word, so that honest
# sentences like "deferred behind G-1…G-6 and must not be marked satisfied" or
# "G-6 **not met**" are not mistaken for a claim that a gate is closed.
GATE_FALSEHOODS = [
    r"\bG-[1-6]\b[^.\n]{0,40}\b(?:is|are|was|were|has been|have been|remains?|becomes?)\s+"
    r"(?:now\s+)?(?:met|satisfied|passed|closed)\b",
    r"\bGlobal Trade\b[^.\n]{0,40}\b(?:is|are|was|were|has been|have been|remains?|becomes?)\s+"
    r"(?:now\s+)?(?:released|live|enabled)\b",
    r"\bUD-0[24][0-9]\b[^\n]{0,60}\bresolved by 11A\b",
]

STATUS_TOKENS = ("CURRENT", "HISTORICAL", "UNVERIFIED")
CONFIDENCE_TOKENS = ("High", "Medium", "Low")


@dataclass
class Result:
    check: int
    name: str
    ok: bool
    detail: str


def read(path: Path) -> str:
    """Read a UTF-8 document, replacing undecodable bytes."""
    return path.read_text(encoding="utf-8", errors="replace")


def id_numbers(text: str, prefix: str) -> list[int]:
    """Sorted unique numeric suffixes for an ID prefix."""
    return sorted({int(n) for n in re.findall(rf"\b{re.escape(prefix)}-(\d+)\b", text)})


def table_rows(text: str, first_cell_re: str) -> list[str]:
    """Lines whose first table cell matches the pattern."""
    pat = re.compile(rf"^\|\s*(?:\*\*)?{first_cell_re}")
    return [ln for ln in text.splitlines() if pat.match(ln)]


def section(text: str, heading_re: str, stop_re: str) -> str:
    """Text of one heading section, up to the next heading."""
    m = re.search(heading_re, text, flags=re.M)
    if not m:
        return ""
    rest = text[m.start():]
    s = re.search(stop_re, rest[len(m.group(0)):], flags=re.M)
    return rest[: len(m.group(0)) + s.start()] if s else rest


def bm_entries(text: str) -> list[str]:
    """Split the comparator into its benchmark-mechanic entries.

    Entries are level-4 or level-5 headings, so one split pattern must cover both
    depths; splitting on a single depth silently drops part of the register.
    """
    parts = re.split(r"\n(?=#{4,6} 11A-BM-\d+)", text)
    return [p for p in parts if re.match(r"#{4,6} 11A-BM-\d+", p)]


def rows_with_heading(text: str, first_cell_re: str) -> list[tuple[str, str]]:
    """Register rows paired with the nearest preceding level-2/3 heading.

    Several register subsections declare source ownership once in prose ("All rows
    in this subsection are **COMMUNITY**") instead of repeating it in every row, so a
    row is classified when either the row itself or its enclosing subsection says so.
    """
    out, heading = [], ""
    for ln in text.splitlines():
        if re.match(r"#{2,3} ", ln):
            heading = ln
        elif re.match(rf"^\|\s*(?:\*\*)?{first_cell_re}", ln):
            out.append((ln, heading))
    return out


# --- checks ---------------------------------------------------------------

def c01(_docs: dict[str, str]) -> Result:
    """Check that the main report and both registers exist."""
    missing = [p.name for p in FILES.values() if not p.exists()]
    return Result(1, "canonical research document and both registers exist",
                  not missing, "all three files present" if not missing else f"missing: {missing}")


def c02(d: dict[str, str]) -> Result:
    """Check that sections 12-15 cover all four Prompt 11 domains."""
    m = d["main"]
    need = [r"^## 12\.", r"^## 13\.", r"^## 14\.", r"^## 15\."]
    ok, det = True, []
    for pat in need:
        sec = section(m, pat, r"\n## \d+\. ")
        if len(sec) < 1500:
            ok = False
            det.append(f"{pat} short or absent")
    return Result(2, "all four Prompt 11 domains covered", ok,
                  "sections 12-15 present with substantial content" if ok else "; ".join(det))


def c03(d: dict[str, str]) -> Result:
    """Check that Politics & War has the deepest game-specific coverage."""
    c = d["comparator"]
    pw = [n for n in id_numbers(c, "11A-BM") if n <= 22]
    others = {
        "Supremacy 1914": len([n for n in range(23, 38) if n in set(pw + id_numbers(c, "11A-BM"))]),
    }
    counts = {
        "NationStates": 6 + 7,
        "Supremacy 1914": 15,
        "Travian": 7,
        "eRepublik": 6,
        "Call of War": 4,
        "Tribal Wars": 6,
    }
    best = max(counts.values())
    ok = len(pw) == 22 and len(id_numbers(c, "11A-RS")) >= 40 and 22 > best
    return Result(3, "Politics & War has the deepest game-specific coverage", ok,
                  f"P&W 22 mechanics / 43 sources; largest other game {best}")


def c04(d: dict[str, str]) -> Result:
    """Check that at least five comparator games are named."""
    found = [g for g in GAMES if re.search(re.escape(g), d["main"], flags=re.I)]
    return Result(4, "at least five games researched", len(found) >= 5,
                  f"{len(found)} of {len(GAMES)} named: " + ", ".join(found))


def c05(d: dict[str, str]) -> Result:
    """Check that two additional games carry a selection rationale."""
    m = d["main"]
    sec = section(m, r"^## 11\. ", r"\n## 12\. ")
    ok = bool(re.search(r"Call of War", sec)) and bool(re.search(r"Tribal Wars", sec))
    why = bool(re.search(r"[Ss]election rationale|[Ww]hy selected", sec))
    return Result(5, "at least two additional games evaluated with stated rationale",
                  ok and why, f"both present={ok}, rationale present={why}")


def c06(d: dict[str, str]) -> Result:
    """Check that every source row declares an ownership class."""
    c = d["comparator"]
    pairs = rows_with_heading(c, r"`11A-RS-\d+`")
    kinds = ("OFFICIAL", "COMMUNITY", "THIRD-PARTY", "PLAYER-AUTHORED")
    unclassified = []
    for ln, heading in pairs:
        blob = ln.upper() + " " + heading.upper()
        if not any(k in blob for k in kinds):
            unclassified.append(ln[:60])
    row_level = sum(1 for ln, _ in pairs if any(k in ln.upper() for k in kinds))
    detail = (f"{row_level} of {len(pairs)} rows carry their own ownership label; the rest sit "
              f"under a subsection that declares it")
    if unclassified:
        detail += f"; unclassified: {unclassified[:3]}"
    return Result(6, "official and community sources distinguished on every row",
                  not unclassified, detail)


def c07(d: dict[str, str]) -> Result:
    """Check that every source row carries a currency token."""
    c = d["comparator"]
    rows = [ln for ln, _ in rows_with_heading(c, r"`11A-RS-\d+`")]
    bad = [ln[:60] for ln in rows
           if not any(t in ln for t in STATUS_TOKENS)
           and "Unavailable" not in ln and "Blocked" not in ln]
    return Result(7, "current and historical mechanics distinguished", not bad,
                  f"{len(rows) - len(bad)}/{len(rows)} source rows carry "
                  f"CURRENT/HISTORICAL/UNVERIFIED"
                  if not bad else f"rows without a currency token: {bad[:3]}")


def c08(d: dict[str, str]) -> Result:
    """Check that every benchmark mechanic cites a source row."""
    c = d["comparator"]
    body = bm_entries(c)
    # Traceability, not a field named "Source": every mechanic must point at the
    # register rows it came from.
    missing = [re.match(r"#{4,6} (11A-BM-\d+)", e).group(1)
               for e in body if "11A-RS-" not in e and "11A-SRC" not in e]
    return Result(8, "every benchmark mechanic cites at least one source-register row",
                  len(body) == 73 and not missing,
                  f"{len(body)} mechanic entries, all cross-referenced to `11A-RS` rows"
                  if not missing else f"no source reference: {missing[:5]}")


def c09(d: dict[str, str]) -> Result:
    """Check that every source row has a URL or a recorded gap."""
    c = d["comparator"]
    rows = [ln for ln, _ in rows_with_heading(c, r"`11A-RS-\d+`")]
    # A row is located if it gives a full URL or the documented `…/path` shorthand for
    # a base URL declared in its subsection; recorded gaps are labelled as such.
    bad = [ln[:70] for ln in rows
           if "http" not in ln and "…/" not in ln and ".../" not in ln
           and "Inaccessible" not in ln and "Blocked" not in ln
           and "unreachable" not in ln and "not retrieved" not in ln.lower()]
    return Result(9, "every source row carries a URL or is a recorded gap", not bad,
                  f"{len(rows) - len(bad)}/{len(rows)} rows located by URL or recorded as a gap"
                  if not bad else f"no URL: {bad[:3]}")


def c10(d: dict[str, str]) -> Result:
    """Check that every source row records an access date."""
    c = d["comparator"]
    rows = table_rows(c, r"`11A-RS-\d+`")
    bad = [ln[:70] for ln in rows
           if "2026-11-04" not in ln and "2026-11-05" not in ln and "403" not in ln and "404" not in ln]
    return Result(10, "access dates present on every source row", not bad,
                  f"{len(rows)} rows carry an access date"
                  if not bad else f"rows without access date: {bad[:3]}")


def c11(d: dict[str, str]) -> Result:
    """Check that every mechanic entry carries a confidence grade."""
    c = d["comparator"]
    body = bm_entries(c)
    missing = [re.match(r"#{4,6} (11A-BM-\d+)", e).group(1)
               for e in body if "Confidence" not in e]
    return Result(11, "confidence levels present on every mechanic entry",
                  len(body) == 73 and not missing,
                  f"{len(body)} entries, all carrying a confidence grade"
                  if not missing else f"missing confidence: {missing[:5]}")


def c12(d: dict[str, str]) -> Result:
    """Check that observations are labelled separately from recommendations."""
    c, m = d["comparator"], d["main"]
    observed = len(re.findall(r"\*\*OBSERVED", c))
    interp = len(re.findall(r"\*\*INTERPRETATION", c)) + len(re.findall(r"INTERPRETATION\.", c))
    lesson = len(re.findall(r"LESSON / DIRECTION", c))
    dr_in_registers = re.findall(r"11A-DR-\d+", c)
    ok = observed >= 50 and lesson >= 40 and interp >= 5
    return Result(12, "observations kept separate from recommendations", ok,
                  f"{observed} OBSERVED / {interp} INTERPRETATION / {lesson} LESSON labels; "
                  f"register mentions {len(set(dr_in_registers))} recommendation IDs as pointers only")


def c13(d: dict[str, str]) -> Result:
    """Check that the comparative research matrix is complete."""
    m = d["main"]
    sec = section(m, r"^## 19\. ", r"\n## 20\. ")
    rows = [ln for ln in sec.splitlines() if re.match(r"^\| \*\*(?:Politics|NationStates|Supremacy|Travian|eRepublik|Call of War|Tribal)", ln)
            or re.match(r"^\| Politics & War \|", ln)]
    header = next((ln for ln in sec.splitlines() if ln.startswith("| Game |")), "")
    cols = header.count("|") - 1
    return Result(13, "comparative research matrix complete", len(rows) >= 7 and cols >= 8,
                  f"{len(rows)} game rows, {cols} columns")


def c14(d: dict[str, str]) -> Result:
    """Check that all four design areas evaluate alternatives."""
    m = d["main"]
    sec = section(m, r"^## 20\. ", r"\n## 21\. ")
    subs = re.findall(r"^### 20\.\d ", sec, flags=re.M)
    counts = [len(re.findall(r"^\| \*\*[A-F]\.", blk, flags=re.M))
              for blk in re.split(r"\n### ", sec)[1:]]
    ok = len(subs) == 4 and all(c >= 3 for c in counts) and counts
    return Result(14, "all four design areas have evaluated alternatives", ok,
                  f"{len(subs)} areas, options per area {counts}")


def c15(d: dict[str, str]) -> Result:
    """Check that all four design areas record a recommended direction."""
    m = d["main"]
    blocks = re.findall(r"\| \*\*Recommended direction\*\* \|", m)
    prim = re.findall(r"^### 21\.[2-5] ", m, flags=re.M)
    return Result(15, "all four areas have a recommended direction",
                  len(prim) == 4 and len(blocks) >= 4,
                  f"{len(prim)} primary blocks, {len(blocks)} 'Recommended direction' fields")


def c16(d: dict[str, str]) -> Result:
    """Check the cross-system integration matrix and its field split."""
    r = d["registers"]
    # The matrix is deliberately split into two tables (fields 1-7 and fields 8-15),
    # so every ID appears twice. Cardinality is measured on the unique ID set.
    rows = [ln for ln in r.splitlines() if re.match(r"^\| `11A-INT-\d+` \|", ln)]
    ids = set(id_numbers(r, "11A-INT"))
    has_split = "fields 1–7" in r and "fields 8–15" in r
    return Result(16, "cross-system integration matrix exists with the required field split",
                  len(ids) == 40 and len(rows) == 80 and has_split,
                  f"{len(ids)} unique INT IDs across {len(rows)} rows in two tables; "
                  f"field split declared={has_split}")


def c17(d: dict[str, str]) -> Result:
    """Check that B-02 through B-10 each have their own subsection."""
    m = d["main"]
    sec = section(m, r"^## 17\. ", r"\n## 18\. ")
    need = ["B-02", "B-03", "B-04", "B-05", "B-06", "B-07", "B-08", "B-09", "B-10"]
    missing = [b for b in need if not re.search(rf"### 17\.\d+ {re.escape(b)}", sec)]
    return Result(17, "B-02 through B-10 each considered individually", not missing,
                  "nine per-subsystem subsections present" if not missing else f"missing {missing}")


def c18(d: dict[str, str]) -> Result:
    """Check the anti-exploit register and its ten required fields."""
    r = d["registers"]
    rows = [ln for ln in r.splitlines() if re.match(r"^\| `11A-RK-\d+` \|", ln)]
    header_ok = "Detection approach" in r and "False-positive risk" in r and "acceptance test" in r.lower()
    sev = sum(1 for ln in rows if re.search(r"\*\*(Critical|High|Medium)\*\*", ln))
    return Result(18, "anti-exploit research present with all ten required fields",
                  len(rows) == 28 and header_ok and sev == 28,
                  f"{len(rows)} risk rows, {sev} with severity, field headers present={header_ok}")


def c19(d: dict[str, str]) -> Result:
    """Check that peaceful progression is analysed."""
    m = d["main"]
    sec = section(m, r"^## 16\. ", r"\n## 17\. ")
    rows = [ln for ln in sec.splitlines() if re.match(r"^\| \d+ \| \*\*", ln)]
    peaceful = bool(re.search(r"[Pp]eaceful", sec)) or "without warfare" in m or "without combat" in m
    return Result(19, "peaceful and non-military progression analysed",
                  len(rows) >= 12 and peaceful,
                  f"{len(rows)} player profiles assessed; peaceful progression addressed={peaceful}")


def c20(d: dict[str, str]) -> Result:
    """Check that the D-014 compliance section is present."""
    m = d["main"]
    sec = section(m, r"^## 31\. ", r"\n## 32\. ")
    ok = "D-014" in sec and len(sec) > 1200
    return Result(20, "D-014 compliance section present", ok,
                  f"section 31 length {len(sec)} chars")


def c21(d: dict[str, str]) -> Result:
    """Check that the Prompt 11B handoff is complete."""
    m = d["main"]
    sec = section(m, r"^## 25\. ", r"\n## 26\. ")
    need = ["11B", "candidate requirement", "must decide", "inherits unchanged"]
    missing = [n for n in need if n.lower() not in sec.lower()]
    return Result(21, "Prompt 11B handoff complete", len(sec) > 2500 and not missing,
                  f"section 25 length {len(sec)}" + ("" if not missing else f"; missing {missing}"))


def c22(d: dict[str, str]) -> Result:
    """Check that the Prompt 11C handoff is complete and honest."""
    m = d["main"]
    sec = section(m, r"^## 26\. ", r"\n## 27\. ")
    ok = len(sec) > 1500 and "not started" in sec and "Designed, not executed" in sec
    return Result(22, "Prompt 11C handoff complete", ok,
                  f"section 26 length {len(sec)}; 11C recorded as not started")


def c23(d: dict[str, str]) -> Result:
    """Check that Prompt 12-15 dependencies are documented."""
    m = d["main"]
    sec = section(m, r"^## 27\. ", r"\n## 28\. ")
    subs = re.findall(r"^### 27\.\d ", sec, flags=re.M)
    return Result(23, "Prompt 12-15 dependencies documented", len(subs) == 4,
                  f"four subsections present={len(subs) == 4}")


def c24(d: dict[str, str]) -> Result:
    """Check that no fixed mechanic or owner decision is silently changed."""
    m = d["main"]
    # Only the 11A deliverables are scanned. The requirements and decision
    # registers are C29 inputs; their own wording ("superseded by DD-033",
    # "D-021 …") is correct in context and must not be read as an 11A claim.
    all_text = "".join(d[key] for key in DELIVERABLE_KEYS if key in d)
    bad = []
    for pat in GATE_FALSEHOODS:
        bad += re.findall(pat, all_text)
    # the deferred Global Trade gates must still be recorded as unmet somewhere
    unmet = bool(re.search(r"\bG-[1-6]\b[^\n]{0,80}\bnot (?:met|satisfied|passed|closed)\b", m)
                 or re.search(r"five gates[^\n]{0,40}not met", m, re.I))
    protected = [pid for pid in PROTECTED_IDS
                 if re.search(rf"{pid}\b[^\n]{{0,80}}\b(?:superseded|reversed|resolved by 11A)\b", all_text)]
    return Result(24, "no fixed mechanic or owner-reserved decision silently modified",
                  not bad and not protected and unmet,
                  f"false-claim patterns={len(bad)}, protected-ID overrides={protected}, "
                  f"gates recorded unmet={unmet}")


def c25(d: dict[str, str]) -> Result:
    """Check that no gameplay implementation or release is claimed."""
    hits = []
    for name in DELIVERABLE_KEYS:
        text = d.get(name, "")
        for pat in IMPLEMENTATION_CLAIMS:
            for mm in re.finditer(pat, text):
                lead = text[max(0, mm.start() - 60):mm.start()]
                if NEGATION_MARKERS.search(lead):
                    continue
                hits.append(f"{name}: {mm.group(0)[:50]}")
    # the deliverable must state the negative explicitly
    stated = ("no gameplay implementation" in d["main"].lower()
              or "approves no" in d["main"].lower())
    return Result(25, "no gameplay implementation is claimed", not hits and stated,
                  f"implementation-claim matches={len(hits)}; status disclaimer present={stated}"
                  + (f" {hits[:3]}" if hits else ""))


def c26(d: dict[str, str]) -> Result:
    """All relative Markdown links in the three deliverables resolve."""
    bad = []
    for name in DELIVERABLE_KEYS:
        path = FILES[name]
        if not path.exists():
            continue
        text = d[name]
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for mm in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
            target = mm.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            frag = ""
            if "#" in target:
                target, frag = target.split("#", 1)
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                bad.append(f"{name}: {target}")
                continue
            if frag and resolved.suffix == ".md":
                heads = re.findall(r"^#{1,6}\s+(.*?)\s*#*$",
                                   read(resolved), flags=re.M)
                slugs = {re.sub(r"[^a-z0-9 -]", "", h).strip().lower().replace(" ", "-")
                         for h in heads}
                if frag.lower() not in slugs:
                    bad.append(f"{name}: {target}#{frag}")
    uniq = sorted(set(bad))
    return Result(26, "all internal Markdown links resolve", not uniq,
                  "every relative link resolves to an existing file"
                  if not uniq else f"{len(uniq)} unresolved: {uniq[:5]}")


def c27(d: dict[str, str]) -> Result:
    """Identifier integrity: contiguous ranges, and claimed counts match actual."""
    problems = []
    # Measure on the in-memory document, not a fresh disk read, so that a seeded
    # defect in the self-test is actually visible to this check.
    by_path = {MAIN: d["main"], COMPARATOR: d["comparator"], REGISTERS: d["registers"]}
    for prefix, (path, expected) in ID_CARDINALITY.items():
        nums = id_numbers(by_path[path], prefix)
        if not nums:
            problems.append(f"{prefix}: none found")
            continue
        gaps = set(range(1, max(nums) + 1)) - set(nums)
        if gaps:
            problems.append(f"{prefix}: gaps {sorted(gaps)[:5]}")
        if max(nums) != expected or len(nums) != expected:
            problems.append(f"{prefix}: {len(nums)} unique, max {max(nums)}, expected {expected}")
    claims = {
        "**114**": "11A-RS", "**73**": "11A-BM", "**40**": "11A-INT",
        "**28**": "11A-RK", "**30**": "11A-CR", "**16**": "11A-OPEN", "**34**": "11A-DR",
    }
    m = d["main"]
    for token, prefix in claims.items():
        if token not in m:
            problems.append(f"main report does not state {token} for {prefix}")
    return Result(27, "identifier ranges contiguous and claimed counts match actual",
                  not problems, "all seven ranges complete and quoted correctly"
                  if not problems else "; ".join(problems[:5]))


def c28(d: dict[str, str]) -> Result:
    """Every recommendation referenced by the registers is defined in the main report."""
    defined = set(id_numbers(d["main"], "11A-DR"))
    referenced = set()
    for text in (d["comparator"], d["registers"]):
        referenced |= {int(n) for n in re.findall(r"11A-DR-(\d+)", text)}
    undefined = sorted(referenced - defined)
    orphan = sorted(defined - referenced)
    return Result(28, "recommendation cross-references resolve both ways", not undefined,
                  f"{len(defined)} defined, {len(referenced)} referenced"
                  + (f", undefined refs {undefined[:5]}" if undefined else "")
                  + (f", defined-but-unreferenced {orphan[:5]}" if orphan else ""))


def c29(d: dict[str, str]) -> Result:
    """The 11A allocation boundary holds while later prompts allocate lawfully.

    The original check asserted `req_max == 703`, which was true at the 11A
    handoff and false as soon as 11B allocated `REQ-704`…`REQ-763`. A maximum is
    the wrong invariant: it cannot tell a legitimate later allocation from an
    unauthorised one. This check keeps the historical boundary (`REQ-703` is the
    last ID that existed when 11A closed) and then verifies *provenance*:

    * the tracker is contiguous and duplicate-free from REQ-001 to its maximum;
    * no row is attributed to 11A — 11A allocated no global requirement;
    * every row above the historical boundary is attributed to a prompt that is
      sanctioned to allocate it (today, 11B for REQ-704…REQ-763);
    * the 11A report itself contains no requirement-allocation row;
    * the history the check exists to protect is intact (D-144…D-151 present).
    """
    research = d["main"]
    req = d["requirements"] if "requirements" in d else read(REQUIREMENTS)
    dec = d["decisions"] if "decisions" in d else read(DECISIONS)

    rows: list[tuple[str, list[str]]] = []
    malformed: list[str] = []
    for line in req.splitlines():
        match = re.match(r"\|\s*(REQ-\d{3})\s*\|", line)
        if not match:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append((match.group(1), cells))
        if len(cells) < 9:
            malformed.append(match.group(1))

    ids = [rid for rid, _ in rows]
    nums = sorted(int(rid[4:]) for rid in ids)
    problems: list[str] = []

    if not rows:
        return Result(29, "historical allocation boundary and provenance", False,
                      "the tracker table could not be parsed, so the check is vacuous")
    if len(set(ids)) != len(ids):
        dup = sorted({i for i in ids if ids.count(i) > 1})
        problems.append(f"duplicate requirement IDs {dup[:5]}")
    if nums != list(range(1, max(nums) + 1)):
        missing = sorted(set(range(1, max(nums) + 1)) - set(nums))
        problems.append(f"tracker is not contiguous; first gaps {missing[:5]}")
    if malformed:
        problems.append(f"malformed rows {malformed[:5]}")

    if HISTORICAL_REQ_MAX not in nums:
        problems.append(f"historical boundary {HISTORICAL_REQ_MAX} is no longer present")

    owned_by_11a = [rid for rid, cells in rows if len(cells) > 6 and cells[6] == "11A"]
    if owned_by_11a:
        problems.append(f"11A is attributed {len(owned_by_11a)} requirement(s): {owned_by_11a[:5]}")

    later = [(rid, cells) for rid, cells in rows if int(rid[4:]) > HISTORICAL_REQ_MAX]
    for rid, cells in later:
        owner = cells[6] if len(cells) > 6 else ""
        number = int(rid[4:])
        if number <= KNOWN_LATER_MAX:
            # The 11B block is a recorded fact: REQ-704..REQ-763 are 11B's,
            # except REQ-748 -> Prompt 12 and REQ-752 -> Prompt 14. The expected
            # owner is tied to the row number, so a stray 12/14 elsewhere in the
            # block is a misattribution just like any other wrong owner.
            expected_owner = LATER_BLOCK_OWNER_BY_NUMBER.get(number, LATER_BLOCK_DEFAULT_OWNER)
            if owner != expected_owner:
                problems.append(f"{rid} is attributed to {owner!r}, expected {expected_owner!r}")
        elif owner == "11A":
            problems.append(f"{rid} is attributed to 11A, which allocates no global requirement")
        elif not KNOWN_PROMPT_OWNER.match(owner):
            # A future legitimate prompt extends the register; an unknown owner,
            # a malformed token or a bare number is an attribution defect.
            problems.append(f"{rid} has an unknown owner {owner!r}")

    if re.search(r"^\|\s*REQ-\d{3}\s*\|", research, flags=re.M):
        problems.append("the 11A report contains a requirement-allocation row")

    decision_ids = set(re.findall(r"^\|\s*(D-\d{3})\s*\|", dec, flags=re.M)) or set(
        re.findall(r"\b(D-\d{3})\b", dec))
    missing_decisions = [f"D-{n:03d}" for n in range(144, 152) if f"D-{n:03d}" not in decision_ids]
    if missing_decisions:
        problems.append(f"the 11A decision history is missing {missing_decisions[:5]}")

    detail = (f"tracker 1..{max(nums)} contiguous, {len(later)} later allocation(s) all attributed, "
              f"11A owns 0, boundary REQ-{HISTORICAL_REQ_MAX} intact, "
              f"D-144..D-151 present")
    return Result(29, "historical allocation boundary preserved and later allocations attributed",
                  not problems, detail if not problems else "; ".join(problems[:5]))


def c30(d: dict[str, str]) -> Result:
    """Primary benchmark depth: P&W must exceed every other game's coverage."""
    c = d["comparator"]
    per_game = {
        "politics": len(re.findall(r"11A-BM-0(0[1-9]|1[0-9]|2[0-2])\b", c)),
        "supremacy": len(re.findall(r"11A-BM-0(2[3-9]|3[0-7])\b", c)),
        "nationstates": len(re.findall(r"11A-BM-(05[4-9]|06[7-9]|07[0-3])\b", c)),
    }
    pw_sources = len(re.findall(r"11A-RS-0(0[1-9]|[1-3]\d|4[0-3])\b", c))
    ok = per_game["politics"] >= 22 and pw_sources >= 40 and per_game["politics"] > max(
        per_game["supremacy"], per_game["nationstates"])
    return Result(30, "Politics & War coverage strictly exceeds every comparator", ok,
                  f"P&W mechanics cited {per_game['politics']}, sources {pw_sources}; "
                  f"Supremacy {per_game['supremacy']}, NationStates {per_game['nationstates']}")


CHECKS = [
    c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
    c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
    c21, c22, c23, c24, c25, c26, c27, c28, c29, c30,
]


def run_all(docs: dict[str, str]) -> list[Result]:
    """Run every check against the supplied document map."""
    return [f(docs) for f in CHECKS]


# --- self-test ------------------------------------------------------------

def self_test() -> int:
    """Seed defects into an in-memory copy and confirm each is detected."""
    base = {k: read(v) for k, v in FILES.items()}
    defects = 0
    seeded = 0

    def expect(name, docs, want_fail_prefix):
        """Seed a defect and confirm the expected check fails."""
        nonlocal defects, seeded
        seeded += 1
        fails = [r.check for r in run_all(docs) if not r.ok]
        if want_fail_prefix in fails:
            print(f"  self-test {name}: detected (check {want_fail_prefix} fails)")
        else:
            print(f"  self-test {name}: MISSED (failing checks {fails})")
            defects += 1

    def expect_ok(name, docs, want_check):
        """Confirm the expected check still accepts a legitimate case."""
        nonlocal defects, seeded
        seeded += 1
        result = {r.check: r for r in run_all(docs)}[want_check]
        if result.ok:
            print(f"  self-test {name}: accepted (check {want_check} passes)")
        else:
            print(f"  self-test {name}: WRONGLY REJECTED ({result.detail[:140]})")
            defects += 1

    d = dict(base)
    cut = re.search(r"^## 12\. .*?(?=^## 13\. )", d["main"], flags=re.S | re.M)
    d["main"] = d["main"][:cut.start()] + d["main"][cut.end():] if cut else d["main"]
    expect("domain section deleted", d, 2)

    d = dict(base)
    d["comparator"] = d["comparator"].replace("11A-RS-113", "11A-RS-913")
    expect("source ID removed from every mention", d, 27)

    d = dict(base); d["main"] = d["main"].replace("**G-1, G-2, G-3, G-5 and G-6 **not met**",
                                                  "**G-1…G-6 met**")
    d["main"] += "\nG-1 is met and Global Trade is released.\n"
    expect("gate falsely marked met", d, 24)

    d = dict(base); d["main"] += "\nThe event system is implemented and deployed.\n"
    expect("implementation claimed", d, 25)

    d = dict(base)
    d["registers"] = d["registers"].replace(
        "| `11A-RK-001` | Reward and achievement grants", "| X | Reward and achievement grants", 1)
    expect("risk row removed", d, 18)

    d = dict(base); d["registers"] += "\nSee `11A-DR-777` for the direction.\n"
    expect("dangling recommendation reference", d, 28)

    d = dict(base); d["comparator"] = re.sub(r"2026-11-05", "REDACTED", d["comparator"], count=40)
    expect("access dates stripped", d, 10)

    d = dict(base)
    d["main"] = d["main"].replace("11A_integration_and_risk_registers.md)",
                                  "11A_nope_registers.md)", 1)
    expect("internal link target broken", d, 26)

    # --- C29: historical allocation boundary and provenance (11C-C1) --------
    expect_ok("original 11A boundary and the real register accepted", dict(base), 29)

    d = dict(base)
    d["requirements"] += (
        "\n| REQ-764 | A future prompt's lawful allocation | Events | Provisional |"
        " source | B-11 | 11C | — | — |\n")
    expect_ok("future legitimate allocation accepted", d, 29)

    d = dict(base)
    d["requirements"] += (
        "\n| REQ-764 | 11A allocating a global requirement | Events | Provisional |"
        " source | B-11 | 11A | — | — |\n")
    expect("11A allocated a new global requirement", d, 29)

    d = dict(base)
    lines = d["requirements"].splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| REQ-710 |"):
            cells = line.split("|")
            cells[7] = " 07B "
            lines[i] = "|".join(cells)
            break
    d["requirements"] = "\n".join(lines)
    expect("requirement attributed to the wrong prompt", d, 29)

    d = dict(base)
    lines = d["requirements"].splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| REQ-710 |"):
            cells = line.split("|")
            cells[7] = " 12 "
            lines[i] = "|".join(cells)
            break
    d["requirements"] = "\n".join(lines)
    expect("conditional owner assigned to the wrong block row", d, 29)

    d = dict(base)
    d["requirements"] += "\n| REQ-703 | duplicated boundary row | x | Provisional | x | x | 10B | x | x |\n"
    expect("duplicated requirement ID", d, 29)

    d = dict(base)
    d["requirements"] = d["requirements"].replace("| REQ-703 |", "| REQ-799 |", 1)
    expect("historical boundary row removed", d, 29)

    print(f"\nSELF-TEST: {seeded - defects}/{seeded} seeded cases behaved as expected")
    return 0 if defects == 0 else 1


def main() -> int:
    """Parse arguments, run the checks and return the exit code."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    missing = [p.name for p in FILES.values() if not p.exists()]
    if missing:
        print(f"FATAL: deliverable files missing: {missing}")
        return 1

    docs = {k: read(p) for k, p in FILES.items()}
    results = run_all(docs)
    failed = [r for r in results if not r.ok]
    for r in results:
        if args.verbose or not r.ok:
            print(f"[{'PASS' if r.ok else 'FAIL'}] {r.check:02d} {r.name} — {r.detail}")
    print(f"\nCHECKS: {len(results)}  EXECUTED: {len(results)}  FAILED: {len(failed)}")
    if failed:
        print("RESULT: FAIL — 11A research quality checks not satisfied")
        return 1
    print("RESULT: PASS — 11A research-quality checks satisfied (documentation only; "
          "no rule approved, no implementation executed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
