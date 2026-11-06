#!/usr/bin/env python3
"""Prompt 11B B-11 specification validator.

Validates the **documentation and specification quality** of the B-11
deliverables:

* ``docs/stage-2/18_world_events_objectives_rankings_progression.md``
* ``docs/stage-2/18_world_events_objectives_rankings_progression_formula_register.md``
* the requirement, unresolved-decision and decision registers they update

It implements the specification checks required by the Prompt 11B brief §21.1,
identifier-integrity and count checks, and the Prompt 11B-C checks for the
original 52-gate acceptance crosswalk, reward-class consistency and formula
classification. Positive and negative fixtures prove each check accepts good
input and rejects the exact defect class it claims to detect.

The 61 `B11-` checks are **not** the 52 original `P11B-` acceptance gates.
The report prints gate coverage, validator checks, fixtures and documentation
link validation in separate sections; a gate is never marked PASS because a
validator check passed. ``B11-60`` verifies a preserved source hash and row
shape; ``B11-61`` verifies criterion equality. Neither proves authorship,
semantic sufficiency or runtime behaviour.

**This is a document checker. It is not a game test.** It validates none of:
event behaviour, ranking arithmetic, reward conservation, privacy
enforcement, exploitation resistance or playability. No rule it checks is
implemented, executed or balanced.

Run from anywhere; paths resolve relative to this file.

    python 11B_validate_b11.py
    python 11B_validate_b11.py --verbose
    python 11B_validate_b11.py --self-test
    python 11B_validate_b11.py --fixtures

Exit code is 0 only when every check and every fixture passes.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import re
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

MAIN = STAGE2 / "18_world_events_objectives_rankings_progression.md"
FORMULA = STAGE2 / "18_world_events_objectives_rankings_progression_formula_register.md"
CROSSWALK = STAGE2 / "18_world_events_objectives_rankings_progression_acceptance_crosswalk.md"
SOURCE = STAGE2 / "18_world_events_objectives_rankings_progression_acceptance_source.md"
REQ = STAGE2 / "03_requirements_traceability.md"
UD = STAGE2 / "05_unresolved_design_decisions.md"
DEC = DOCS / "DECISIONS.md"
APPROVED = STAGE2 / "04_approved_and_provisional_decisions.md"
HANDOFF = STAGE2 / "00_stage_2_handoff.md"
ROADMAP = STAGE2 / "01_stage_2_prompt_roadmap.md"
LOG = STAGE2 / "06_stage_2_progress_log.md"

SOURCE_START = "<!-- P11B-SOURCE-GATES-START -->"
SOURCE_END = "<!-- P11B-SOURCE-GATES-END -->"
SOURCE_GATES_SHA256 = "d2e6c35e1b85f772a5b8273e821a62bcf5b3af406c2c3d42e96fea379086f766"

RULE_START = re.compile(r"^\*\*(WEP-\d{3}) — ", re.MULTILINE)
FORMULA_HEAD = re.compile(r"^### (F-WEP-\d{3}) — ", re.MULTILINE)
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

MANDATORY_SECTIONS = [
    "## 1. Purpose",
    "## 2. Authority",
    "## 3. Terminology",
    "## 4. Architecture",
    "## 5. Fixed constraints",
    "## 6. Domain A",
    "## 7. Domain B",
    "## 8. Domain C",
    "## 9. Domain D",
    "## 10. Achievements",
    "## 11. Rewards",
    "## 12. Eligibility",
    "## 13. State machines",
    "## 14. Rules",
    "## 15. Data ownership",
    "## 16. Turn-processing",
    "## 17. Cross-system",
    "## 18. Security",
    "## 19. Privacy",
    "## 20. Error",
    "## 21. Audit",
    "## 22. Formula",
    "## 23. Requirements",
    "## 24. Decision",
    "## 25. Provisional",
    "## 26. Deferred",
    "## 27. Prompt 11C",
    "## 28. Prompt 12",
    "## 29. Final",
]

FORMULA_FIELD_LABELS = [
    "Identifier", "Name", "Domain", "Purpose", "Expression", "Variables",
    "Input source", "Units", "Valid range", "Output range", "Rounding",
    "Caps", "Floors", "Phase", "Snapshot", "Missing data", "Invalid input",
    "Example", "Boundary case", "Provisional status",
]


@dataclass
class Model:
    main: str
    formula: str
    req: str
    ud: str
    dec: str
    approved: str
    handoff: str
    roadmap: str
    log: str
    crosswalk: str = ""
    source: str = ""
    context: str = ""
    progress: str = ""
    rule_ids: list[str] = field(default_factory=list)
    rules: dict[str, str] = field(default_factory=dict)
    formula_texts: dict[str, str] = field(default_factory=dict)
    main_path: Path = MAIN
    formula_path: Path = FORMULA


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def load() -> Model:
    main = read(MAIN)
    formula = read(FORMULA)
    ids = RULE_START.findall(main)
    spans = []
    matches = list(RULE_START.finditer(main))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(main)
        spans.append((m.group(1), main[m.start():end]))
    rules = dict(spans)
    fheads = list(FORMULA_HEAD.finditer(formula))
    ftexts: dict[str, str] = {}
    for i, m in enumerate(fheads):
        end = fheads[i + 1].start() if i + 1 < len(fheads) else len(formula)
        ftexts[m.group(1)] = formula[m.start():end]
    return Model(
        main=main, formula=formula, req=read(REQ), ud=read(UD), dec=read(DEC),
        approved=read(APPROVED), handoff=read(HANDOFF), roadmap=read(ROADMAP),
        log=read(LOG), crosswalk=read(CROSSWALK),
        source=read(SOURCE),
        context=read(DOCS / "AI_CONTEXT.md"), progress=read(DOCS / "PROJECT_PROGRESS.md"),
        rule_ids=ids, rules=rules, formula_texts=ftexts,
    )


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def rule_number(rid: str) -> int:
    return int(rid.split("-")[1])


def section_text(main: str, heading: str) -> str:
    start = main.find(heading)
    if start < 0:
        return ""
    nxt = main.find("\n## ", start + 1)
    return main[start:] if nxt < 0 else main[start:nxt]


def formula_block_problems(block: str) -> list[str]:
    problems = []
    for n, label in enumerate(FORMULA_FIELD_LABELS, start=1):
        if not re.search(rf"\|\s*{n}\s*\|\s*{re.escape(label)}", block):
            problems.append(f"missing field {n} ({label})")
    return problems


def formula_expression(block: str) -> str:
    m = re.search(r"\|\s*5\s*\|\s*Expression\s*\|\s*(.*?)\s*\|", block, re.DOTALL)
    return m.group(1) if m else ""


def formula_field(block: str, n: int, label: str) -> str:
    m = re.search(rf"\|\s*{n}\s*\|\s*{re.escape(label)}\s*\|\s*(.*?)\s*\|", block, re.DOTALL)
    return m.group(1) if m else ""


def traceability_ranges(main: str) -> list[tuple[int, int, str]]:
    start = main.find("Rule-family traceability matrix")
    if start < 0:
        return []
    end = main.find("\n## ", start + 1)
    block = main[start:end if end > 0 else len(main)]
    rows = []
    for line in block.splitlines():
        m = re.match(r"\|\s*`WEP-(\d{3})`[–-]`?(?:WEP-)?(\d{3})`?\s*\|(.*)\|", line)
        if m:
            rows.append((int(m.group(1)), int(m.group(2)), m.group(3)))
    return rows


def source_gate_block(text: str) -> str | None:
    if SOURCE_START not in text or SOURCE_END not in text:
        return None
    start = text.index(SOURCE_START)
    end = text.index(SOURCE_END) + len(SOURCE_END)
    return text[start:end]


def gate_rows(text: str) -> list[tuple[str, str]]:
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(P11B-\d{2})\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows


def rule_sections(main: str) -> dict[str, str]:
    section = ""
    out: dict[str, str] = {}
    for line in main.splitlines():
        heading = re.match(r"^## (\d+)\.", line)
        if heading:
            section = heading.group(1)
        rule = re.match(r"^\*\*(WEP-\d{3}[a-z]?) — ", line)
        if rule:
            out[rule.group(1)] = section
    return out


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

@dataclass
class Check:
    cid: str
    name: str
    fn: Callable[[Model], tuple[bool, str]]


def c01(m: Model):
    return MAIN.exists() and MAIN.stat().st_size > 100_000, f"{MAIN.name} exists, {MAIN.stat().st_size if MAIN.exists() else 0} bytes"


def c02(m: Model):
    ok = FORMULA.exists() and FORMULA.stat().st_size > 40_000
    return ok, f"{FORMULA.name} exists, {FORMULA.stat().st_size if FORMULA.exists() else 0} bytes"


def c03(m: Model):
    missing = [s for s in MANDATORY_SECTIONS if s not in m.main]
    return not missing, f"{len(MANDATORY_SECTIONS)-len(missing)}/{len(MANDATORY_SECTIONS)} mandatory sections present" + (f"; missing {missing}" if missing else "")


def domain_count(m: Model, lo: int, hi: int) -> int:
    return sum(1 for rid in m.rule_ids if lo <= rule_number(rid) <= hi)


def c04(m: Model):
    n = domain_count(m, 71, 202)
    ok = n >= 120 and "EV-CAL" in m.main and "two-stage teardown" in m.main
    return ok, f"{n} world-event rules; taxonomy and teardown present"


def c05(m: Model):
    n = domain_count(m, 203, 316)
    ok = n >= 105 and "OBJ-DEV" in m.main and "COMPLETED_PENDING_VALIDATION" in m.main
    return ok, f"{n} objective rules; categories and lifecycle present"


def c06(m: Model):
    n = domain_count(m, 317, 422)
    ok = (n >= 95 and "ST-DEV" in m.main and "WSE" in m.main
          and "No overall composite" in m.main
          and "any undisclosed value are prohibited" in m.main)
    return ok, f"{n} standing rules; ten standings, WSE, no-composite and published tie-break present"


def c07(m: Model):
    n = domain_count(m, 423, 486)
    ok = n >= 55 and "no prestige currency" in m.main and "Season reset scope" in m.main
    return ok, f"{n} progression rules; permanent/seasonal separation present"


def c08(m: Model):
    n = domain_count(m, 487, 498)
    ok = n >= 10 and "Five recognition objects" in m.main and "NAT-052" in m.main
    return ok, f"{n} recognition-object rules; milestone-as-record present"


def c09(m: Model):
    n = domain_count(m, 499, 556)
    ok = (n >= 50 and "REWARD" in m.main and "achievement key" in m.main
          and "An uncapped repeatable material reward is invalid" in m.main
          and "Duplication protection" in m.main)
    return ok, f"{n} reward rules; ledger, key, stacking cap and dedupe present"


def c10(m: Model):
    nums = [rule_number(r) for r in m.rule_ids]
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    missing = [n for n in range(1, max(nums) + 1) if n not in nums] if nums else []
    ok = not dupes and not missing and nums == sorted(nums)
    return ok, f"{len(nums)} rules, max {max(nums) if nums else 0}; duplicate={dupes}; gaps={missing[:10]}"


def c11(m: Model):
    ids = list(m.formula_texts)
    nums = [int(i.split("-")[2]) for i in ids]
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    missing = [n for n in range(1, 51) if n not in nums]
    ok = len(ids) == 50 and not dupes and not missing
    return ok, f"{len(ids)} formula blocks; duplicate={dupes}; missing={missing[:10]}"


def c12(m: Model):
    refs = set(re.findall(r"F-WEP-\d{3}(?![\w-])", m.main))
    unknown = sorted(r for r in refs if r not in m.formula_texts)
    covered: set[str] = set()
    for lo, hi in re.findall(r"F-WEP-(\d{3})`[^F\n]{0,12}F-WEP-(\d{3})`", m.main):
        covered.update(f"F-WEP-{n:03d}" for n in range(int(lo), int(hi) + 1))
    for lo, hi in re.findall(r"F-WEP-(\d{3})[–-](?:`F-WEP-|`)?(\d{3})`?", m.main):
        covered.update(f"F-WEP-{n:03d}" for n in range(int(lo), int(hi) + 1))
    unreferenced = sorted(f for f in m.formula_texts if f not in refs and f not in covered)
    missing_covered = sorted(covered - set(m.formula_texts))
    ok = not unknown and not unreferenced and not missing_covered
    return ok, f"{len(refs)} references; unknown={unknown}; unreferenced={unreferenced}; promised-but-missing={missing_covered}"


def c13(m: Model):
    bad = []
    for fid, block in m.formula_texts.items():
        if not formula_field(block, 6, "Variables") or not formula_field(block, 7, "Input source"):
            bad.append(fid)
    return not bad, f"variables/input source declared for {50-len(bad)}/50; bad={bad}"


def c14(m: Model):
    bad = {fid: formula_block_problems(b) for fid, b in m.formula_texts.items()}
    bad = {k: v for k, v in bad.items() if v}
    return not bad, f"{50-len(bad)}/50 complete; defects={list(bad.items())[:3]}"


def c15(m: Model):
    missing = []
    for fid, block in m.formula_texts.items():
        status = formula_field(block, 20, "Provisional status")
        if not status:
            missing.append(fid)
    return not missing, f"provisional/structural status present for {50-len(missing)}/50"


def c16(m: Model):
    bad = []
    for fid, block in m.formula_texts.items():
        status = formula_field(block, 20, "Provisional status")
        if "Provisional" in status and "Prompt 14" not in status:
            bad.append(fid)
    return not bad, f"Prompt 14 named on every provisional formula; bad={bad}"


def c17(m: Model):
    miss_main = [f"D-{n}" for n in range(144, 152) if f"D-{n}" not in m.main]
    miss_dec = [f"D-{n}" for n in range(144, 152) if f"D-{n}" not in m.dec]
    ok = not miss_main and not miss_dec
    return ok, f"D-144..D-151 in main={8-len(miss_main)}/8, in DECISIONS={8-len(miss_dec)}/8"


def c18(m: Model):
    miss_main = [f"DD-{n}" for n in range(192, 200) if f"DD-{n}" not in m.main]
    miss_appr = [f"DD-{n}" for n in range(192, 200) if f"DD-{n}" not in m.approved]
    ok = not miss_main and not miss_appr
    return ok, f"DD-192..DD-199 in main={8-len(miss_main)}/8, in 04={8-len(miss_appr)}/8"


def c19(m: Model):
    rows = [ln for ln in m.ud.splitlines() if re.match(r"\|\s*UD-04[0-9]\s*\|", ln)]
    open_rows = [ln for ln in rows if "Open" in ln]
    main_ok = ("UD-040" in m.main and "remain Open" in m.main)
    ok = len(open_rows) >= 10 and main_ok
    return ok, f"{len(open_rows)}/10 owner-reserved UD rows marked Open; main preserves them={main_ok}"


def c20(m: Model):
    miss = [f"11A-CR-{n:03d}" for n in range(1, 31) if f"11A-CR-{n:03d}" not in m.main]
    dr_rows = re.findall(
        r"^\|\s*`?(11A-DR-\d{3})`?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$",
        m.main, re.MULTILINE,
    )
    dr = {rid: (disposition.strip(), where.strip()) for rid, disposition, where in dr_rows}
    expected = [f"11A-DR-{n:03d}" for n in range(1, 35)]
    missing_dr = [rid for rid in expected if rid not in dr]
    bad_dr = [
        rid for rid in expected
        if rid in dr and (
            not re.match(r"^(ADOPTED|REJECTED|NOT APPLICABLE|DEFERRED)\b", dr[rid][0])
            or not re.search(r"WEP-\d{3}|§\d|D-\d{3}", dr[rid][1])
        )
    ]
    ok = not miss and not missing_dr and not bad_dr
    return ok, (f"{30-len(miss)}/30 candidate requirements; "
                f"{34-len(missing_dr)}/34 recommendations with a disposition; "
                f"missing DR={missing_dr}; invalid DR={bad_dr}")


def c21(m: Model):
    miss = [f"11A-OPEN-{n:03d}" for n in range(1, 17) if f"11A-OPEN-{n:03d}" not in m.main]
    return not miss, f"{16-len(miss)}/16 open questions dispositioned; missing={miss}"


def c22(m: Model):
    miss_main = [f"REQ-{n}" for n in range(704, 764) if f"REQ-{n}" not in m.main]
    miss_req = [f"REQ-{n}" for n in range(704, 764) if f"REQ-{n}" not in m.req]
    ok = not miss_main and not miss_req
    return ok, f"REQ-704..763 in main={60-len(miss_main)}/60, in 03={60-len(miss_req)}/60"


def c23(m: Model):
    ids = re.findall(r"^\|\s*(REQ-\d{3})\s*\|", m.req, re.MULTILINE)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    return not dupes, f"{len(ids)} requirement rows, unique={not dupes}; duplicates={dupes[:10]}"


def c24(m: Model):
    miss = [f"WPC-{n:02d}" for n in range(1, 18) if f"WPC-{n:02d}" not in m.main]
    subsystems = [f"B-{n:02d}" for n in range(2, 11) if f"B-{n:02d}" not in m.main]
    ok = not miss and not subsystems
    return ok, f"{17-len(miss)}/17 contracts; missing={miss}; subsystems={subsystems}"


def c25(m: Model):
    bad = []
    for path in (MAIN, FORMULA):
        if not path.exists():
            continue
        text = read(path)
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                bad.append(f"{path.name} -> {target}")
    return not bad, f"{len(bad)} broken local links" + (f"; {bad[:5]}" if bad else "")


def c26(m: Model):
    text = section_text(m.main, "## 15. Data ownership")
    ok = "Authoritative owner" in text and "B-11" in text and all(f"B-{n:02d}" in text for n in range(2, 11))
    return ok, "ownership matrix names B-02..B-10 and B-11"


def c27(m: Model):
    ok = "conservation" in m.main.lower() and "ECN-111" in m.main and "F-WEP-049" in m.main and "REWARD" in m.main
    return ok, "reward conservation identity, ledger and F-WEP-049 referenced"


def c28(m: Model):
    ok = ("Snapshot immutability" in m.main and "WEP-383" in m.main and "WEP-390" in m.main
          and "correction snapshot" in m.main.lower()
          and "**WEP-197 — Corrections.**" in m.main and "appends a new record" in m.main)
    return ok, "snapshot immutability, correction and duplicate prevention present"


def c29(m: Model):
    sec = section_text(m.main, "## 18. Security")
    scenarios = len(re.findall(r"^\|\s*\d+\s*\|", sec, re.MULTILINE))
    ok = scenarios >= 20 and "Idempotency keys" in sec and "Atomicity" in sec
    return ok, f"{scenarios} manipulation scenarios; idempotency and atomicity present"


def c30(m: Model):
    ok = "D-027" in m.main and "k = 5" in m.main and "Visibility matrix" in m.main and "no new threshold" in m.main.lower()
    return ok, "D-027, k=5, visibility matrix and no-new-threshold rule present"


def c31(m: Model):
    ok = "D-014" in m.main and "No consent by silence" in m.main and "Category B" in m.main and "Category C" in m.main
    return ok, "D-014, consent-by-silence and Category B/C audit content present"


def c32(m: Model):
    ok = "## 27. Prompt 11C handoff" in m.main and "WEP-708" in m.main and "Prompt 11C" in m.main
    return ok, "Prompt 11C handoff section present"


def c33(m: Model):
    sec = section_text(m.main, "## 28. Prompt 12")
    ok = all(f"Prompt {n}" in sec for n in (12, 13, 14, 15))
    return ok, "Prompt 12, 13, 14 and 15 boundaries present"


def c34(m: Model):
    # A positive claim that B-11 amended another subsystem would fail.
    forbidden = [
        "B-11 amends B-10", "B-11 changes B-04", "B-11 overrides B-03",
        "replaces the B-02 phase order",
    ]
    found = [p for p in forbidden if p.lower() in m.main.lower()]
    preserves = "B-11 cites B-02…B-10 identifiers and never rewrites their text" in m.main
    return not found and preserves, f"no subsystem-amendment claim; preservation rule present={preserves}"


def c35(m: Model):
    ok = all(g in m.main for g in ("G-1", "G-2", "G-3", "G-4", "G-5", "G-6"))
    not_met = "not met" in m.main and "partial" in m.main
    return ok and not_met, f"all six gates named={ok}; unchanged state stated={not_met}"


def c36(m: Model):
    disclaimer = "No gameplay implementation is authorized" in m.main
    bad = re.findall(r"\b(is implemented|was implemented|has been deployed|is deployed|runtime[- ]tested and passed)\b", m.main, re.IGNORECASE)
    return disclaimer and not bad, f"disclaimer={disclaimer}; false-claim phrases={bad}"


def c37(m: Model):
    ranges = traceability_ranges(m.main)
    covered: set[int] = set()
    problems = []
    for lo, hi, rest in ranges:
        cells = [c.strip() for c in rest.split("|")]
        if len([c for c in cells if c]) < 6:
            problems.append(f"{lo}-{hi} has an empty traceability cell")
        covered.update(range(lo, hi + 1))
    missing = [n for n in range(1, 724) if n not in covered]
    ok = not problems and not missing
    return ok, f"{len(ranges)} families cover {723-len(missing)}/723 rules; problems={problems[:3]}; gaps={missing[:10]}"


def c38(m: Model):
    ranges = traceability_ranges(m.main)
    orphans = [rid for rid in m.rule_ids if not any(lo <= rule_number(rid) <= hi for lo, hi, _ in ranges)]
    return not orphans, f"{len(orphans)} unexplained rule orphans" + (f"; {orphans[:5]}" if orphans else "")


def c39(m: Model):
    sec = section_text(m.main, "## 13. State machines")
    machines = ["event definition", "event instance", "event participation", "objective definition",
                "objective instance", "objective progress", "achievement", "ranking snapshot",
                "seasonal progression", "reward claim", "historical record correction"]
    missing = [x for x in machines if x.lower() not in sec.lower()]
    ok = not missing and "invalid" in sec.lower()
    return ok, f"state-machine coverage; missing={missing}"


def c40(m: Model):
    defined = set(re.findall(r"`(WPF-\d{2})`\s*\|", m.main))
    expected = {f"WPF-{n:02d}" for n in range(1, 41)}
    missing = sorted(expected - defined)
    return not missing, f"{40-len(missing)}/40 failure codes defined; missing={missing[:10]}"


def c41(m: Model):
    defined = set(re.findall(r"`(WPA-\d{2})`", m.main))
    expected = {f"WPA-{n:02d}" for n in range(1, 51)}
    missing = sorted(expected - defined)
    return not missing, f"{50-len(missing)}/50 audit events defined; missing={missing[:10]}"


def c42(m: Model):
    sec = section_text(m.main, "## 25. Provisional")
    ok = "Prompt 14" in sec and "Structural" in m.main and "PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED" in m.main
    return ok, "provisional classification and Prompt 14 ownership present"


def c43(m: Model):
    inventory = re.findall(r"^\|\s*`(F-WEP-\d{3})`\s*\|", m.formula, re.MULTILINE)
    ok = len(inventory) == 50 and set(inventory) == set(m.formula_texts)
    return ok, f"inventory {len(inventory)}, blocks {len(m.formula_texts)}"


def c44(m: Model):
    return "No consent by silence" in m.main and "WEP-014" in m.main, "explicit player-consent restriction present"


def c45(m: Model):
    ok = "D-014" in m.main and "Development AI autonomy" in m.main or "player sovereignty" in m.main.lower()
    return ok, "D-014 development/gameplay autonomy distinction present"


def c46(m: Model):
    ok = "forfeit" in m.main and "D-028" in m.main and "never expires through absence" in m.main
    return ok, "absence never forfeits an entitlement"


def c47(m: Model):
    ok = (all(x in m.main for x in ("ST-MIL", "ST-DEF", "WAR-162", "WAR-147"))
          and "No exact readiness, force, inventory or OP value" in m.main
          and "**WEP-065 — No military value exposure.**" in m.main)
    return ok, "B-10 privacy and receipt rules integrated"


def c48(m: Model):
    ok = (all(x in m.main for x in ("ALL-224", "ALL-156", "AX-18"))
          and "Alliance military command" in m.main and "MUST NOT create" in m.main
          and "military command is granted" not in m.main.lower())
    return ok, "Alliance command/prize/member-data boundaries present"


def c49(m: Model):
    ok = "Prompt 11C" in m.handoff and "11C" in m.roadmap and "11B" in m.roadmap
    return ok, "handoff and roadmap name 11B/11C"


def c50(m: Model):
    # No fabricated IDs: every WPC/WPA/WPF referenced exists in its catalogue.
    referenced_wpc = set(re.findall(r"WPC-\d{2}", m.main))
    defined_wpc = {f"WPC-{n:02d}" for n in range(1, 18)}
    stray = sorted(referenced_wpc - defined_wpc)
    return not stray, f"stray contract IDs={stray}"


# --- acceptance crosswalk (Prompt 11B-C) -----------------------------------

ROOT = DOCS.parent
EXPECTED_GATES = [f"P11B-{n:02d}" for n in range(1, 53)]
CROSSWALK_STATUSES = ("PASS", "PARTIAL", "FAIL", "BLOCKED")
AUTHORITATIVE_REWARD_CLASSES = (
    "RECOGNITION", "RECORD", "AUTHORSHIP", "COSMETIC", "TITLE", "MATERIAL",
)
GATE_ID = re.compile(r"^P11B-\d{2}$")


def crosswalk_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if re.match(r"^\|\s*P11B-\d{2}\s*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 8:
                rows.append(cells)
    return rows


def crosswalk_summary(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", line)
        if m and m.group(1).strip() not in ("Summary item", "---"):
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def summary_int(summary: dict[str, str], prefix: str) -> int | None:
    for key, value in summary.items():
        if key.lower().startswith(prefix.lower()):
            digits = re.search(r"\d+", value)
            return int(digits.group(0)) if digits else None
    return None


def reward_class_lists(text: str) -> list[tuple[str, ...]]:
    """Return every literal six-name list that starts with `RECOGNITION`.

    A scattered mention of `ACCESS` elsewhere in the paragraph is not a class
    list; only six consecutive backticked names are compared.
    """
    found = []
    pattern = re.compile(
        r"`RECOGNITION`\s*,\s*`([A-Z]{3,})`\s*,\s*`([A-Z]{3,})`\s*,"
        r"\s*`([A-Z]{3,})`\s*,\s*`([A-Z]{3,})`\s*,\s*`([A-Z]{3,})`"
    )
    for match in pattern.finditer(text):
        found.append(("RECOGNITION",) + match.groups())
    return found


def formula_classification(m: Model) -> tuple[list[str], list[str], list[str], list[str]]:
    provisional, structural, structural_p14, retired = [], [], [], []
    for fid, block in m.formula_texts.items():
        status = formula_field(block, 20, "Provisional status")
        if status.startswith("**Provisional"):
            provisional.append(fid)
        elif status.startswith("**Structural"):
            structural.append(fid)
            if "Prompt 14" in status:
                structural_p14.append(fid)
        elif status.startswith("**Retired"):
            retired.append(fid)
    return (sorted(provisional), sorted(structural),
            sorted(structural_p14), sorted(retired))


def resolve_evidence(cell: str, texts: dict[str, str],
                     fallback_md: str | None = None) -> tuple[list[str], list[str]]:
    """Return (missing paths, invalid identifier/section references) for one cell.

    A supporting cell often carries section references without repeating the
    primary file. `fallback_md` is the row's primary Markdown file, so a
    section is resolved against the file the row actually cites.
    """
    missing: list[str] = []
    invalid: list[str] = []
    paths = re.findall(r"`(docs/[^`]+\.(?:md|py))`", cell)
    for path in paths:
        if not (ROOT / path).exists():
            missing.append(path)
    first_md = next((p for p in paths if p.endswith(".md") and (ROOT / p).exists()), fallback_md)

    for rid in re.findall(r"(?<![A-Za-z])WEP-\d{3}[a-z]?", cell):
        if rid not in texts.get("rules", ""):
            invalid.append(rid)
    for fid in re.findall(r"F-WEP-\d{3}", cell):
        if fid not in texts.get("formulas", ""):
            invalid.append(fid)
    for cid in re.findall(r"WPC-\d{2}", cell):
        if cid not in texts.get("contracts", ""):
            invalid.append(cid)
    for cid in re.findall(r"WPF-\d{2}", cell):
        if cid not in texts.get("failures", ""):
            invalid.append(cid)
    for cid in re.findall(r"WPA-\d{2}", cell):
        if cid not in texts.get("audits", ""):
            invalid.append(cid)
    for req in re.findall(r"REQ-\d{3}", cell):
        if req not in texts.get("requirements", ""):
            invalid.append(req)
    for did in re.findall(r"(?<![A-Z])D-\d{3}", cell):
        if did not in texts.get("decisions", ""):
            invalid.append(did)
    for did in re.findall(r"DD-\d{3}", cell):
        if did not in texts.get("approved", ""):
            invalid.append(did)
    for uid in re.findall(r"UD-\d{3}", cell):
        if uid not in texts.get("unresolved", ""):
            invalid.append(uid)
    for cid in re.findall(r"B11-\d{2}", cell):
        if cid not in texts.get("checks", ""):
            invalid.append(cid)

    for number in re.findall(r"§(\d+)", cell):
        if first_md is None:
            invalid.append(f"§{number} without a Markdown file")
            continue
        body = (ROOT / first_md).read_text(encoding="utf-8", errors="replace")
        if not re.search(rf"^##\s+{number}\.", body, re.MULTILINE):
            invalid.append(f"§{number} not in {first_md}")
    return missing, invalid


def acceptance_stats(m: Model) -> dict[str, object]:
    rows = crosswalk_rows(m.crosswalk)
    statuses = [r[5] for r in rows]
    counts = {status: statuses.count(status) for status in CROSSWALK_STATUSES}
    texts = {
        "rules": m.main,
        "formulas": " ".join(m.formula_texts),
        "contracts": " ".join(f"WPC-{n:02d}" for n in range(1, 18)),
        "failures": m.main,
        "audits": m.main,
        "requirements": m.req,
        "decisions": m.dec,
        "approved": m.approved,
        "unresolved": m.ud,
        "checks": " ".join(c.cid for c in CHECKS),
    }
    missing_evidence = 0
    invalid_refs: list[str] = []
    for row in rows:
        if row[5] != "PASS":
            continue
        primary, supporting = row[2], row[3]
        has_path = bool(re.search(r"`docs/[^`]+\.(?:md|py)`", primary))
        has_anchor = bool(re.search(r"WEP-|F-WEP-|WPC-|WPF-|WPA-|REQ-|DD-|UD-|B11-|§\d", primary + " " + supporting))
        if not has_path or not has_anchor:
            missing_evidence += 1
        primary_paths = re.findall(r"`(docs/[^`]+\.md)`", primary)
        fallback_md = next((p for p in primary_paths if (ROOT / p).exists()), None)
        for cell in (primary, supporting):
            missing, invalid = resolve_evidence(cell, texts, fallback_md)
            if missing:
                missing_evidence += 1
            invalid_refs.extend(invalid)
    return {
        "rows": rows,
        "ids": [r[0] for r in rows],
        "statuses": statuses,
        "counts": counts,
        "missing_evidence": missing_evidence,
        "invalid_refs": invalid_refs,
        "summary": crosswalk_summary(m.crosswalk),
    }


def c51(m: Model):
    block = m.rules.get("WEP-499", "")
    names = tuple(re.findall(r"`([A-Z]+)`", block)[:6])
    d159 = next((line for line in m.dec.splitlines() if line.startswith("| D-159 |")), "")
    ok = (names == AUTHORITATIVE_REWARD_CLASSES and "ACCESS" not in block
          and "cosmetic, title, material" in d159.lower())
    return ok, f"WEP-499 classes={names}; D-159 agrees={'cosmetic, title, material' in d159.lower()}"


def c52(m: Model):
    documents = {
        "AI_CONTEXT": read(DOCS / "AI_CONTEXT.md"),
        "AI_HANDOFF": read(DOCS / "AI_HANDOFF.md"),
        "PROJECT_PROGRESS": read(DOCS / "PROJECT_PROGRESS.md"),
        "ROADMAP": read(DOCS / "ROADMAP.md"),
        "00_handoff": m.handoff,
        "log": m.log,
    }
    bad = []
    for name, text in documents.items():
        for names in reward_class_lists(text):
            if set(names) != set(AUTHORITATIVE_REWARD_CLASSES):
                bad.append(f"{name}:{names}")
    exact = ("`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`")
    log_ok = exact in m.log
    return not bad and log_ok, f"bad lists={bad[:3]}; log exact list={log_ok}"


def c53(m: Model):
    provisional, structural, structural_p14, retired = formula_classification(m)
    expected_provisional = ["F-WEP-011", "F-WEP-021", "F-WEP-029",
                            "F-WEP-030", "F-WEP-033", "F-WEP-046"]
    expected_p14 = ["F-WEP-003", "F-WEP-004", "F-WEP-005", "F-WEP-007",
                    "F-WEP-009", "F-WEP-010", "F-WEP-012", "F-WEP-015",
                    "F-WEP-016", "F-WEP-019", "F-WEP-024", "F-WEP-025",
                    "F-WEP-031", "F-WEP-034", "F-WEP-035", "F-WEP-036",
                    "F-WEP-040", "F-WEP-042", "F-WEP-043", "F-WEP-050"]
    summary_ok = (re.search(r"Structural[^\n]{0,24}43", m.formula) is not None
                  and re.search(r"Provisional:?\**\s*6\b", m.formula) is not None
                  and re.search(r"(?:Retired[^\n]{0,24}1\b|1\s+retired)", m.formula, re.IGNORECASE) is not None
                  and "20 contain a Prompt 14 parameter" in m.formula
                  and "23 contain no calibration parameter" in m.formula)
    lists_ok = (all(fid in m.formula for fid in expected_provisional)
                and all(fid in m.formula for fid in expected_p14))
    ok = (provisional == expected_provisional and structural_p14 == expected_p14
          and len(structural) == 43 and retired == ["F-WEP-048"]
          and summary_ok and lists_ok)
    return ok, (f"provisional={len(provisional)}, structural={len(structural)}, "
                f"structural+Prompt14={len(structural_p14)}, retired={retired}, "
                f"summary={summary_ok}")


def c54(m: Model):
    baseline = ("Structural formulas containing provisional parameters are structurally "
                "specified but are not numerically finalized.")
    documents = {
        "AI_CONTEXT": m.context,
        "AI_HANDOFF": read(DOCS / "AI_HANDOFF.md"),
        "PROJECT_PROGRESS": m.progress,
        "ROADMAP": read(DOCS / "ROADMAP.md"),
        "00_handoff": m.handoff,
        "log": m.log,
    }
    missing = [name for name, text in documents.items() if baseline not in text]
    overbroad = "Every number remains **PROVISIONAL — PROMPT 14 CALIBRATION REQUIRED**"
    over = [name for name, text in documents.items() if overbroad in text]
    patterns = [
        r"\ball\s+(?:B-11\s+)?(?:numbers?|values?|formulas?|parameters?)\s+"
        r"(?:are\s+|remain\s+|remains\s+)?(?:all\s+)?provisional",
        r"\bevery\s+(?:B-11\s+)?number\s+(?:is\s+|remains\s+)?provisional",
        r"\bB-11\b[^\n]{0,100}\b(?:fully calibrated|balance-final|"
        r"calibration (?:is )?complete|calibration has been completed)\b",
    ]
    # Only active status surfaces are scanned semantically. The log is history
    # and may quote a defect while explaining its correction.
    status_surfaces = ["AI_CONTEXT", "AI_HANDOFF", "PROJECT_PROGRESS", "ROADMAP", "00_handoff"]
    semantic = []
    for name in status_surfaces:
        for line in documents[name].splitlines():
            low = line.lower()
            is_b11_status = (
                "b11_progression" in low
                or "11b status" in low
                or "b-11 v1.0 specification" in low
            )
            if not is_b11_status:
                continue
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    semantic.append(f"{name}:{line.strip()[:90]}")
                    break
    register_ok = ("A structural formula may contain a provisional constant" in m.formula
                   and "Prompt 14" in m.formula)
    ok = not missing and not over and not semantic and register_ok
    return ok, (f"precise wording missing={missing}; overbroad={over}; "
                f"semantic overbroad={semantic[:3]}; register={register_ok}")


def c55(m: Model):
    rows = crosswalk_rows(m.crosswalk)
    ids = [r[0] for r in rows]
    missing = [g for g in EXPECTED_GATES if g not in ids]
    duplicates = sorted({g for g in ids if ids.count(g) > 1})
    unknown = sorted(g for g in ids if not GATE_ID.match(g) or g not in EXPECTED_GATES)
    summary = crosswalk_summary(m.crosswalk)
    declared_expected = summary_int(summary, "Acceptance gates expected")
    declared_accounted = summary_int(summary, "Gates accounted for")
    ok = (not missing and not duplicates and not unknown and len(ids) == 52
          and declared_expected == 52 and declared_accounted == len(ids))
    return ok, (f"rows={len(ids)} missing={missing[:5]} duplicate={duplicates[:5]} "
                f"unknown={unknown[:5]} declared={declared_expected}/{declared_accounted}")


def c56(m: Model):
    stats = acceptance_stats(m)
    counts = stats["counts"]
    summary = stats["summary"]
    declared = {s: summary_int(summary, s) for s in CROSSWALK_STATUSES}
    statuses = stats["statuses"]
    invalid = sorted({s for s in statuses if s not in CROSSWALK_STATUSES})
    total = sum(counts.values())
    counts_ok = total == len(statuses) == 52 and all(counts[s] == declared[s] for s in CROSSWALK_STATUSES)
    ok = not invalid and counts_ok
    return ok, (f"computed={counts} declared={declared} invalid={invalid} total={total}")


def c57(m: Model):
    stats = acceptance_stats(m)
    section_map = rule_sections(m.main)
    misplaced: list[str] = []
    for row in stats["rows"]:
        if row[5] != "PASS":
            continue
        for cell in (row[2], row[3]):
            paths = re.findall(r"`(docs/[^`]+\.md)`", cell)
            sections = re.findall(r"§(\d+)", cell)
            ids = re.findall(r"WEP-\d{3}[a-z]?", cell)
            if not paths or not sections or not ids:
                continue
            if not any(path.endswith(MAIN.name) for path in paths):
                continue
            for rid in ids:
                actual = section_map.get(rid)
                if actual and actual not in sections:
                    misplaced.append(f"{row[0]}:{rid} cited under §{'/'.join(sections)} but is in §{actual}")
    ok = stats["missing_evidence"] == 0 and not stats["invalid_refs"] and not misplaced
    return ok, (f"PASS missing evidence={stats['missing_evidence']}; "
                f"invalid references={stats['invalid_refs'][:5]}; misplaced={misplaced[:5]}")


def c58(m: Model):
    canonical = set(m.rule_ids) | {"WEP-692a"}
    numeric = {rule_number(r) for r in m.rule_ids}
    rows = []
    for line in m.req.splitlines():
        match = re.match(r"\|\s*REQ-(\d{3})\s*\|", line)
        if match and 704 <= int(match.group(1)) <= 763:
            rows.append((int(match.group(1)), line))
    problems = []
    for number, line in rows:
        refs = re.findall(r"(?<!F-)WEP-[A-Za-z0-9]+", line)
        if not refs:
            problems.append(f"REQ-{number}: no WEP reference")
            continue
        for ref in refs:
            if not re.fullmatch(r"WEP-\d{3}[a-z]?", ref):
                problems.append(f"REQ-{number}: malformed {ref}")
            elif ref not in canonical:
                problems.append(f"REQ-{number}: missing {ref}")
        for lo, hi in re.findall(
            r"(?<!F-)WEP-(\d{3})\s*[–—…-]\s*(?:WEP-)?(\d{3})", line
        ):
            low, high = int(lo), int(hi)
            if low > high:
                problems.append(f"REQ-{number}: inverted WEP-{lo}..{hi}")
                continue
            missing = [n for n in range(low, high + 1) if n not in numeric]
            if missing:
                problems.append(f"REQ-{number}: range WEP-{lo}..{hi} misses {missing[:3]}")
    numbers = [n for n, _ in rows]
    ok = len(rows) == 60 and len(set(numbers)) == 60 and not problems
    return ok, (f"{len(rows)}/60 B-11 requirement rows; "
                f"reference problems={problems[:5]}")


def c59(m: Model):
    summary = crosswalk_summary(m.crosswalk)
    declared_checks = summary_int(summary, "Validator checks")
    declared_gates = summary_int(summary, "Acceptance gates expected")
    separation = ("never added, substituted or equated" in m.crosswalk
                  and "Documentation link validation is a separate command" in m.crosswalk)
    ok = (declared_checks == len(CHECKS) and declared_gates == 52
          and separation)
    return ok, (f"declared checks={declared_checks}, actual checks={len(CHECKS)}, "
                f"declared gates={declared_gates}, separation={separation}")


def c60(m: Model):
    block = source_gate_block(m.source)
    problems: list[str] = []
    if not block:
        problems.append("source artifact or gate markers missing")
        rows: list[tuple[str, str]] = []
    else:
        digest = hashlib.sha256(block.encode("utf-8")).hexdigest()
        if digest != SOURCE_GATES_SHA256:
            problems.append(f"source block hash {digest} != preserved {SOURCE_GATES_SHA256}")
        if SOURCE_GATES_SHA256 not in m.source:
            problems.append("artifact does not declare the preserved block hash")
        rows = gate_rows(block)
    ids = [g for g, _ in rows]
    if len(rows) != 52:
        problems.append(f"{len(rows)} source gate rows, expected 52")
    if ids != EXPECTED_GATES:
        problems.append("source gate IDs are not exactly P11B-01..P11B-52 in order")
    empty = [g for g, criterion in rows if not criterion.strip()]
    if empty:
        problems.append(f"empty source criteria: {empty[:5]}")
    for token in (
        "line 3 of the transcript",
        "0f46245a-8c76-4433-b4d6-cfa63d424147",
        "2026-11-05T09:33:08.190Z",
        "5b45dfe230862d3527aaa089a83807929c92dc0c20af6c78710532d494f307a8",
        "# 23. FINAL PROMPT 11B ACCEPTANCE GATES",
    ):
        if token not in m.source:
            problems.append(f"provenance field missing: {token}")
    return not problems, (f"source rows={len(rows)}; hash={SOURCE_GATES_SHA256[:12]}…; "
                          f"problems={problems[:4]}")


def c61(m: Model):
    source = gate_rows(source_gate_block(m.source) or "")
    crosswalk = crosswalk_rows(m.crosswalk)
    problems: list[str] = []
    if not source:
        problems.append("no source gate rows")
    if [g for g, _ in source] != EXPECTED_GATES:
        problems.append("source IDs are not contiguous P11B-01..P11B-52")
    if [r[0] for r in crosswalk] != [g for g, _ in source]:
        problems.append("crosswalk gate IDs/order differ from the preserved source")
    for (gate, criterion), row in zip(source, crosswalk):
        if len(row) < 8:
            problems.append(f"{gate}: crosswalk row is incomplete")
            continue
        if row[0] != gate:
            problems.append(f"{row[0]}: out of order relative to {gate}")
        if row[1] != criterion:
            problems.append(f"{gate}: criterion wording differs from the preserved source")
        if row[5] not in CROSSWALK_STATUSES:
            problems.append(f"{gate}: invalid status {row[5]!r}")
        if not row[6].strip() or not row[7].strip():
            problems.append(f"{gate}: missing explanation or remaining action")
    return not problems, (f"source gates={len(source)}; crosswalk rows={len(crosswalk)}; "
                          f"criterion/wording problems={problems[:5]}")


CHECKS = [
    Check("B11-01", "Main specification exists", c01),
    Check("B11-02", "Formula register exists", c02),
    Check("B11-03", "All mandatory sections exist", c03),
    Check("B11-04", "World-event rules present", c04),
    Check("B11-05", "Objective rules present", c05),
    Check("B11-06", "Ranking rules present", c06),
    Check("B11-07", "Progression rules present", c07),
    Check("B11-08", "Achievement and milestone rules present", c08),
    Check("B11-09", "Reward rules present", c09),
    Check("B11-10", "Rule IDs unique and contiguous", c10),
    Check("B11-11", "Formula IDs unique and complete", c11),
    Check("B11-12", "Formula references resolve", c12),
    Check("B11-13", "Formula variables declared", c13),
    Check("B11-14", "Every formula has mandatory fields", c14),
    Check("B11-15", "Provisional parameters labelled", c15),
    Check("B11-16", "Prompt 14 calibration ownership", c16),
    Check("B11-17", "D-144..D-151 handled", c17),
    Check("B11-18", "DD-192..DD-199 handled", c18),
    Check("B11-19", "Owner-reserved decisions remain open", c19),
    Check("B11-20", "All 11A recommendations/CRs dispositioned", c20),
    Check("B11-21", "All 11A open questions dispositioned", c21),
    Check("B11-22", "Requirements accounted for", c22),
    Check("B11-23", "No duplicate requirements", c23),
    Check("B11-24", "B-02..B-10 integration contracts exist", c24),
    Check("B11-25", "Local links resolve", c25),
    Check("B11-26", "Ownership fields populated", c26),
    Check("B11-27", "Reward conservation requirements exist", c27),
    Check("B11-28", "Ranking snapshot integrity exists", c28),
    Check("B11-29", "Security controls exist", c29),
    Check("B11-30", "Privacy rules exist", c30),
    Check("B11-31", "D-014 audit exists", c31),
    Check("B11-32", "Prompt 11C handoff exists", c32),
    Check("B11-33", "Prompt 12-15 boundaries exist", c33),
    Check("B11-34", "No B-02..B-10 mechanic silently changed", c34),
    Check("B11-35", "Global Trade gates unchanged", c35),
    Check("B11-36", "No false implementation claim", c36),
    Check("B11-37", "Traceability matrix covers every rule", c37),
    Check("B11-38", "No unexplained traceability orphans", c38),
    Check("B11-39", "State machines complete", c39),
    Check("B11-40", "Failure codes complete", c40),
    Check("B11-41", "Audit events complete", c41),
    Check("B11-42", "Provisional classification and calibration owner", c42),
    Check("B11-43", "Formula inventory matches blocks", c43),
    Check("B11-44", "Explicit player-consent restriction", c44),
    Check("B11-45", "D-014 autonomy distinction", c45),
    Check("B11-46", "No forfeiture through absence", c46),
    Check("B11-47", "B-10 privacy integration", c47),
    Check("B11-48", "B-09 alliance boundaries", c48),
    Check("B11-49", "Handoff/roadmap continuity", c49),
    Check("B11-50", "No fabricated contract IDs", c50),
    Check("B11-51", "Authoritative reward-class set", c51),
    Check("B11-52", "Reward-class summaries consistent", c52),
    Check("B11-53", "Formula classifications match field 20", c53),
    Check("B11-54", "Provisional-status wording precise", c54),
    Check("B11-55", "Crosswalk accounts for all 52 gates", c55),
    Check("B11-56", "Crosswalk status counts add up and are honest", c56),
    Check("B11-57", "Every PASS has resolving evidence", c57),
    Check("B11-58", "Every B-11 requirement names a rule", c58),
    Check("B11-59", "Gate count separated from check count", c59),
    Check("B11-60", "Original 52-gate source preserved and hashed", c60),
    Check("B11-61", "Crosswalk criteria match the preserved source", c61),
]


# ---------------------------------------------------------------------------
# fixtures
# ---------------------------------------------------------------------------

def run_all(m: Model) -> list[tuple[str, bool, str]]:
    return [(c.cid, *c.fn(m)) for c in CHECKS]


def check_by_id(m: Model, cid: str) -> tuple[bool, str]:
    for c in CHECKS:
        if c.cid == cid:
            return c.fn(m)
    raise KeyError(cid)


@dataclass
class Fixture:
    fid: str
    cid: str
    expect: bool
    mutate: Callable[[Model], None]
    reason: str


def strip_rule(m: Model, lo: int, hi: int):
    ids = [rid for rid in list(m.rule_ids) if lo <= rule_number(rid) <= hi]
    for rid in ids:
        m.rules.pop(rid, None)
        m.rule_ids.remove(rid)
        m.main = m.main.replace(f"**{rid} —", f"**REMOVED {rid} —")


def f_neg_01(m: Model):
    strip_rule(m, 71, 148)


def f_neg_02(m: Model):
    strip_rule(m, 203, 219)


def f_neg_03(m: Model):
    strip_rule(m, 281, 290)


def f_neg_04(m: Model):
    m.formula_texts.pop("F-WEP-029", None)


def f_neg_05(m: Model):
    m.rule_ids.append("WEP-326")
    m.rules["WEP-326-dup"] = m.rules["WEP-326"]


def f_neg_06(m: Model):
    block = m.formula_texts["F-WEP-001"]
    m.formula_texts["F-WEP-001"] = re.sub(r"\|\s*6\s*\|\s*Variables\s*\|.*?\n", "\n", block)


def f_neg_07(m: Model):
    block = m.formula_texts["F-WEP-021"]
    m.formula_texts["F-WEP-021"] = re.sub(r"\|\s*20\s*\|\s*Provisional status\s*\|.*?\n", "\n", block)


def f_neg_08(m: Model):
    block = m.formula_texts["F-WEP-001"]
    m.formula_texts["F-WEP-001"] = re.sub(r"\|\s*11\s*\|\s*Rounding\s*\|.*?\n", "\n", block)


def f_neg_09(m: Model):
    block = m.formula_texts["F-WEP-001"]
    m.formula_texts["F-WEP-001"] = re.sub(r"\|\s*15\s*\|\s*Snapshot\s*\|.*?\n", "\n", block)


def f_neg_10(m: Model):
    m.main = m.main.replace(
        "**WEP-396 — Prohibited tie-breaks.** *Approved.* Operator identity, account age, insertion order, database row order, hash order, client-supplied order, alliance membership, nation age as merit and any undisclosed value are prohibited.",
        "**WEP-396 — Prohibited tie-breaks.** *Approved.* Operator identity is the preferred tie-break."
    )


def f_neg_11(m: Model):
    m.main = m.main.replace("**WEP-553 — Unbounded accumulation.** *Approved.* A repeatable reward declares a cap. An uncapped repeatable material reward is invalid.",
                            "**WEP-553 — Unbounded accumulation.** *Approved.* A repeatable reward may stack without a cap.")


def f_neg_12(m: Model):
    m.main = m.main.replace("**WEP-510 — Duplication protection.**", "**WEP-510 — Duplication removed.**")


def f_neg_13(m: Model):
    m.main = m.main.replace("**WEP-197 — Corrections.**", "**WEP-197 — Correction removed.**")


def f_neg_14(m: Model):
    m.main += "\nSee F-WEP-999 for the missing calculation.\n"


def f_neg_15(m: Model):
    m.main = m.main.replace("**WEP-065 — No military value exposure.**", "**WEP-065 — Military values public.**")


def f_neg_16(m: Model):
    m.main += "\nAlliance military command is granted to the Alliance founder.\n"


def f_neg_17(m: Model):
    m.main = m.main.replace("G-1, G-2, G-3, G-5 and G-6 are not met and G-4 is partial", "all gates are met")


def f_neg_18(m: Model):
    lines = m.ud.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| UD-046 |"):
            lines[i] = line.replace("Open", "Resolved")
            break
    m.ud = "\n".join(lines)


def f_neg_19(m: Model):
    m.main = m.main.replace("**WEP-014 — No consent by silence.**", "**WEP-014 — Consent may be inferred.**")
    m.main = m.main.replace("No consent by silence.", "Silence is consent.")


def f_neg_20(m: Model):
    m.main = m.main.replace("**WEP-014 — No consent by silence.** *Approved (D-014 §5.6, REQ-523, `11A-CR-027`).* The game MUST NOT accept an objective, join an event, choose a reward, accept a treaty, spend treasury, or take any discretionary national action on a player's behalf because a notification was delivered or a timer elapsed. Silence is never consent. System bookkeeping that an accepted rule authorizes is not a discretionary choice.",
                            "**WEP-014 — Consent.** *Approved.* A notification may be treated as acceptance.")


def f_neg_21(m: Model):
    block = m.formula_texts["F-WEP-011"]
    m.formula_texts["F-WEP-011"] = block.replace("**Prompt 14**", "**approved**")


def f_neg_22(m: Model):
    m.formula = m.formula.replace("Prompt 14", "the balance team")
    m.main = m.main.replace("Prompt 14", "the balance team")
    m.formula_texts = {k: v.replace("Prompt 14", "the balance team") for k, v in m.formula_texts.items()}


def f_neg_23(m: Model):
    m.main = m.main.replace("## 27. Prompt 11C handoff", "## 27. Workflows")


def set_gate_row(m: Model, gate: str, changes: dict[int, str]) -> None:
    lines = m.crosswalk.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {gate} |"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            for index, value in changes.items():
                cells[index] = value
            lines[i] = "| " + " | ".join(cells) + " |"
            break
    m.crosswalk = "\n".join(lines)


def f_neg_24(m: Model):
    m.crosswalk = "\n".join(
        line for line in m.crosswalk.splitlines() if not line.startswith("| P11B-52 |")
    )


def f_neg_25(m: Model):
    first = next(line for line in m.crosswalk.splitlines() if line.startswith("| P11B-01 |"))
    m.crosswalk += "\n" + first + "\n"


def f_neg_26(m: Model):
    m.crosswalk += (
        "\n| P11B-53 | Invented gate | `docs/stage-2/18_world_events_objectives_rankings_progression.md` §1 `WEP-001` | "
        "None | None | PASS | Invented | None |\n"
    )


def f_neg_27(m: Model):
    set_gate_row(m, "P11B-01", {2: "", 3: ""})


def f_neg_28(m: Model):
    set_gate_row(m, "P11B-01", {
        2: "`docs/stage-2/nonexistent_spec.md` §1 `WEP-001`",
    })


def f_neg_29(m: Model):
    set_gate_row(m, "P11B-01", {
        2: "`docs/stage-2/18_world_events_objectives_rankings_progression.md` §1 `WEP-999`",
    })


def f_neg_30(m: Model):
    set_gate_row(m, "P11B-01", {5: "PARTIAL"})


def f_neg_31(m: Model):
    set_gate_row(m, "P11B-02", {5: "BLOCKED"})


def f_neg_32(m: Model):
    m.crosswalk = m.crosswalk.replace("| Gates accounted for | 52 |", "| Gates accounted for | 51 |")


def f_neg_33(m: Model):
    m.crosswalk = m.crosswalk.replace(
        "| Validator checks (B11-01…B11-61) | 61 |",
        "| Validator checks (B11-01…B11-61) | 52 |",
    )


def f_neg_34(m: Model):
    m.log = m.log.replace(
        "`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `COSMETIC`, `TITLE`, `MATERIAL`",
        "`RECOGNITION`, `RECORD`, `AUTHORSHIP`, `MATERIAL`, `COSMETIC`, `ACCESS`",
    )


def f_neg_35(m: Model):
    m.formula_texts["F-WEP-048"] = m.formula_texts["F-WEP-048"].replace(
        "**Retired**", "**Structural**"
    )


def f_neg_36(m: Model):
    baseline = ("Structural formulas containing provisional parameters are structurally "
                "specified but are not numerically finalized.")
    m.handoff = m.handoff.replace(
        baseline, "Every number remains **PROVISIONAL \u2014 PROMPT 14 CALIBRATION REQUIRED**."
    )


def f_neg_37(m: Model):
    m.context = m.context.replace(
        "unapproved calibration remains with Prompt 14",
        "all numbers provisional for Prompt 14",
    )


def f_neg_38(m: Model):
    m.progress = m.progress.replace(
        "unapproved calibration remains with Prompt 14",
        "all numbers provisional for Prompt 14",
    )


def f_neg_39(m: Model):
    lines = m.req.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| REQ-755 |"):
            lines[i] = line.replace("WEP-499…WEP-514", "WEP-499…WEP-999", 1)
            break
    m.req = chr(10).join(lines)


def f_neg_40(m: Model):
    set_gate_row(m, "P11B-01", {1: "Canonical B-11 specification may exist"})


def f_neg_41(m: Model):
    m.source = m.source.replace(
        "| P11B-01 | Canonical B-11 specification exists |",
        "| P11B-01 | Canonical B-11 specification may exist |",
    )


def f_neg_42(m: Model):
    m.source = chr(10).join(
        line for line in m.source.splitlines() if not line.startswith("| P11B-52 |")
    )


def f_neg_43(m: Model):
    set_gate_row(m, "P11B-08", {
        2: "`docs/stage-2/18_world_events_objectives_rankings_progression.md` §13 `WEP-099`",
    })


def f_neg_44(m: Model):
    m.main = chr(10).join(
        line for line in m.main.splitlines() if not line.startswith("| `11A-DR-034` |")
    )


FIXTURES = [
    Fixture("POS-01", "B11-04", True, lambda m: None, "valid event rules accepted"),
    Fixture("POS-02", "B11-05", True, lambda m: None, "valid objective rules accepted"),
    Fixture("POS-03", "B11-06", True, lambda m: None, "valid ranking definitions accepted"),
    Fixture("POS-04", "B11-14", True, lambda m: None, "valid formula with 20 fields accepted"),
    Fixture("POS-05", "B11-24", True, lambda m: None, "valid cross-system contracts accepted"),
    Fixture("POS-06", "B11-15", True, lambda m: None, "valid provisional parameter accepted"),
    Fixture("POS-07", "B11-07", True, lambda m: None, "valid permanent/seasonal split accepted"),
    Fixture("POS-08", "B11-27", True, lambda m: None, "valid reward accounting accepted"),
    Fixture("POS-09", "B11-55", True, lambda m: None, "complete 52-gate crosswalk accepted"),
    Fixture("POS-10", "B11-53", True, lambda m: None, "field-20 formula classification accepted"),
    Fixture("POS-11", "B11-51", True, lambda m: None, "authoritative reward classes accepted"),
    Fixture("POS-12", "B11-54", True, lambda m: None, "precise provisional wording accepted"),
    Fixture("POS-13", "B11-58", True, lambda m: None, "resolvable requirement references accepted"),
    Fixture("POS-14", "B11-60", True, lambda m: None, "preserved 52-gate source accepted"),
    Fixture("POS-15", "B11-61", True, lambda m: None, "crosswalk criteria matching the source accepted"),
    Fixture("POS-16", "B11-20", True, lambda m: None, "all 34 11A recommendations dispositioned accepted"),
    Fixture("NEG-01", "B11-04", False, f_neg_01, "missing event lifecycle rejected"),
    Fixture("NEG-02", "B11-05", False, f_neg_02, "missing objective eligibility rejected"),
    Fixture("NEG-03", "B11-05", False, f_neg_03, "missing objective completion validation rejected"),
    Fixture("NEG-04", "B11-12", False, f_neg_04, "missing ranking formula rejected"),
    Fixture("NEG-05", "B11-10", False, f_neg_05, "duplicate ranking/rule ID rejected"),
    Fixture("NEG-06", "B11-13", False, f_neg_06, "undefined formula variable rejected"),
    Fixture("NEG-07", "B11-14", False, f_neg_07, "undefined coefficient/status rejected"),
    Fixture("NEG-08", "B11-14", False, f_neg_08, "missing rounding rule rejected"),
    Fixture("NEG-09", "B11-14", False, f_neg_09, "missing snapshot timing rejected"),
    Fixture("NEG-10", "B11-06", False, f_neg_10, "invalid tie-break rule rejected"),
    Fixture("NEG-11", "B11-09", False, f_neg_11, "unbounded reward stacking rejected"),
    Fixture("NEG-12", "B11-09", False, f_neg_12, "duplicate reward claim protection removed"),
    Fixture("NEG-13", "B11-28", False, f_neg_13, "inconsistent historical correction rejected"),
    Fixture("NEG-14", "B11-12", False, f_neg_14, "invalid source-system/formula reference rejected"),
    Fixture("NEG-15", "B11-47", False, f_neg_15, "broken B-10 privacy rejected"),
    Fixture("NEG-16", "B11-48", False, f_neg_16, "Alliance command escalation rejected"),
    Fixture("NEG-17", "B11-35", False, f_neg_17, "Global Trade gate promotion rejected"),
    Fixture("NEG-18", "B11-19", False, f_neg_18, "owner-reserved decision marked resolved rejected"),
    Fixture("NEG-19", "B11-31", False, f_neg_19, "missing D-014 section rejected"),
    Fixture("NEG-20", "B11-44", False, f_neg_20, "missing explicit player-consent restriction rejected"),
    Fixture("NEG-21", "B11-16", False, f_neg_21, "unjustified provisional parameter rejected"),
    Fixture("NEG-22", "B11-16", False, f_neg_22, "missing Prompt 14 calibration ownership rejected"),
    Fixture("NEG-23", "B11-32", False, f_neg_23, "missing Prompt 11C handoff rejected"),
    Fixture("NEG-24", "B11-55", False, f_neg_24, "one missing acceptance gate rejected"),
    Fixture("NEG-25", "B11-55", False, f_neg_25, "duplicate gate ID rejected"),
    Fixture("NEG-26", "B11-55", False, f_neg_26, "unknown gate ID rejected"),
    Fixture("NEG-27", "B11-57", False, f_neg_27, "PASS without evidence rejected"),
    Fixture("NEG-28", "B11-57", False, f_neg_28, "PASS with a broken file reference rejected"),
    Fixture("NEG-29", "B11-57", False, f_neg_29, "PASS with a nonexistent rule ID rejected"),
    Fixture("NEG-30", "B11-56", False, f_neg_30, "PARTIAL counted in the PASS total rejected"),
    Fixture("NEG-31", "B11-56", False, f_neg_31, "BLOCKED counted in the PASS total rejected"),
    Fixture("NEG-32", "B11-55", False, f_neg_32, "mismatched gate count rejected"),
    Fixture("NEG-33", "B11-59", False, f_neg_33, "check count represented as gate count rejected"),
    Fixture("NEG-34", "B11-52", False, f_neg_34, "unsupported ACCESS reward class rejected"),
    Fixture("NEG-35", "B11-53", False, f_neg_35, "retired formula reclassified without a decision rejected"),
    Fixture("NEG-36", "B11-54", False, f_neg_36, "overbroad provisional wording rejected"),
    Fixture("NEG-37", "B11-54", False, f_neg_37, "AI_CONTEXT all-numbers-provisional row rejected"),
    Fixture("NEG-38", "B11-54", False, f_neg_38, "PROJECT_PROGRESS all-numbers-provisional row rejected"),
    Fixture("NEG-39", "B11-58", False, f_neg_39, "nonexistent WEP reference in a requirement rejected"),
    Fixture("NEG-40", "B11-61", False, f_neg_40, "crosswalk criterion wording drift cannot retain PASS rejected"),
    Fixture("NEG-41", "B11-60", False, f_neg_41, "altered source criterion rejected by the preserved hash"),
    Fixture("NEG-42", "B11-60", False, f_neg_42, "missing source gate row rejected"),
    Fixture("NEG-43", "B11-57", False, f_neg_43, "evidence ID cited under the wrong section rejected"),
    Fixture("NEG-44", "B11-20", False, f_neg_44, "missing 11A recommendation disposition rejected"),
]


def run_fixtures(base: Model) -> list[tuple[str, str, bool, str]]:
    out = []
    for fx in FIXTURES:
        m = copy.deepcopy(base)
        fx.mutate(m)
        passed, detail = check_by_id(m, fx.cid)
        ok = (passed == fx.expect)
        out.append((fx.fid, fx.cid, ok, f"{fx.reason}: check returned {passed} ({detail})"))
    return out


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def run_link_validation() -> tuple[int, int | None, str]:
    """Run the separate project link validator; never treat its result as a gate."""
    import subprocess

    script = QA_DIR / "validate_links.py"
    if not script.exists():
        return 2, None, "validate_links.py not found"
    proc = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    match = re.search(r"Unresolved:\s*(\d+)", out)
    tail = " | ".join(out.strip().splitlines()[-4:])
    return proc.returncode, int(match.group(1)) if match else None, tail


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Validate the Prompt 11B B-11 specification.")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-test", action="store_true", help="run checks and fixtures")
    ap.add_argument("--fixtures", action="store_true", help="run only the fixtures")
    args = ap.parse_args(argv)

    if not MAIN.exists() or not FORMULA.exists() or not CROSSWALK.exists():
        print("FAIL: canonical B-11 documents or the acceptance crosswalk are missing.")
        return 2

    model = load()
    results = run_all(model)
    failures = [r for r in results if not r[1]]
    stats = acceptance_stats(model)

    print("Prompt 11B B-11 specification validator")
    print(f"rules={len(model.rule_ids)} formulas={len(model.formula_texts)} checks={len(CHECKS)}")
    print("-" * 72)
    for cid, ok, detail in results:
        if args.verbose or not ok:
            print(f"{cid} {'PASS' if ok else 'FAIL'}  {detail}")
    print("-" * 72)

    print("ACCEPTANCE GATE COVERAGE (original Prompt 11B section 23):")
    counts = stats["counts"]
    print(f"  gates expected {len(EXPECTED_GATES)}; accounted {len(stats['rows'])}; "
          f"PASS {counts['PASS']}; PARTIAL {counts['PARTIAL']}; "
          f"FAIL {counts['FAIL']}; BLOCKED {counts['BLOCKED']}")
    print(f"  missing evidence {stats['missing_evidence']}; "
          f"invalid evidence references {len(stats['invalid_refs'])}")
    print("B-11 VALIDATOR CHECKS:")
    print(f"  checks passed {len(results)-len(failures)}/{len(results)}")
    print("NOT the acceptance-gate count: validator checks are quality checks, not Prompt 11B gates.")

    fixture_results = run_fixtures(model) if (args.self_test or args.fixtures) else []
    if fixture_results:
        pos = [f for f in fixture_results if f[0].startswith("POS")]
        neg = [f for f in fixture_results if f[0].startswith("NEG")]
        for fid, cid, ok, detail in fixture_results:
            if args.verbose or not ok:
                print(f"{fid} {'PASS' if ok else 'FAIL'}  [{cid}] {detail}")
        print("-" * 72)
        print(f"positive fixtures {sum(1 for f in pos if f[2])}/{len(pos)}")
        print(f"negative fixtures {sum(1 for f in neg if f[2])}/{len(neg)}")
        if any(not f[2] for f in fixture_results):
            failures.append(("FIXTURES", False, "one or more fixtures failed"))

    if not args.fixtures:
        print("-" * 72)
        print("DOCUMENTATION LINK VALIDATION (separate command, not a gate):")
        rc, unresolved, tail = run_link_validation()
        print(f"  exit={rc}; unresolved={unresolved}; {tail}")
        if rc != 0 or unresolved != 0:
            failures.append(("LINKS", False, "link validation failed"))

    all_pass = (counts["PASS"] == len(EXPECTED_GATES)
                and counts["PARTIAL"] == counts["FAIL"] == counts["BLOCKED"] == 0)
    print(f"CLOSEOUT ELIGIBILITY: {'all 52 gates PASS' if all_pass else 'not eligible — non-PASS gates exist'}")

    if failures:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS — specification and fixtures are internally consistent at the documentation level.")
    print("Gate PASS is documentary only; B11-60/B11-61 do not prove authorship, semantic sufficiency or runtime behaviour.")
    print("NOT PROVEN: runtime behaviour, balance, privacy enforcement, storage cost or player experience.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
