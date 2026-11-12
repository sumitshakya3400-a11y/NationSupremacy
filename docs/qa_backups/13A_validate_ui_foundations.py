#!/usr/bin/env python3
"""Prompt 13A focused validator — UI research, architecture and design foundations.

Run:  python docs/qa_backups/13A_validate_ui_foundations.py
Self-test (seeded defects):  python docs/qa_backups/13A_validate_ui_foundations.py --self-test

Scope discipline. This validator grades *documentation quality only*: identifier
integrity, register arithmetic, citation resolution, governance synchronization and
hygiene across Prompt 13A's five canonical deliverables. It is not an acceptance
substitute — the `P13A-` gate register in
`docs/stage-2/research/13A_ui_requirements_open_questions_and_acceptance.md` is the
acceptance record, and every gate there is a documentation-level verdict. Nothing
here executes a UI, a test or a migration, and no check may be read as evidence that
any screen, component or framework exists.

Every expectation is *derived from the documents themselves* (row counts, tallies,
identifier sets, status blocks); no register number is hard-coded as truth without a
matching extraction from the file it describes.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
RESEARCH = DOCS / "stage-2" / "research"

DELIVERABLES = {
    "doc1": RESEARCH / "13A_politics_and_war_ui_research.md",
    "doc2": RESEARCH / "13A_ui_design_principles_and_architecture.md",
    "doc3": RESEARCH / "13A_master_screen_inventory.md",
    "doc4": RESEARCH / "13A_responsive_and_design_system_foundations.md",
    "doc5": RESEARCH / "13A_ui_requirements_open_questions_and_acceptance.md",
}
GOVERNANCE = {
    "ai_context": DOCS / "AI_CONTEXT.md",
    "ai_handoff": DOCS / "AI_HANDOFF.md",
    "progress": DOCS / "PROJECT_PROGRESS.md",
    "roadmap": DOCS / "ROADMAP.md",
    "decisions": DOCS / "DECISIONS.md",
    "register04": DOCS / "stage-2" / "04_approved_and_provisional_decisions.md",
    "unresolved": DOCS / "stage-2" / "05_unresolved_design_decisions.md",
    "tracker": DOCS / "stage-2" / "03_requirements_traceability.md",
    "outline": DOCS / "stage-2" / "02_master_game_design_bible_outline.md",
    "prompt_roadmap": DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md",
    "log": DOCS / "stage-2" / "06_stage_2_progress_log.md",
    "handoff_stage2": DOCS / "stage-2" / "00_stage_2_handoff.md",
    "prompt_index": DOCS / "prompts" / "INDEX.md",
}
ARCHIVE = DOCS / "prompts" / "prompt_13A_ui_research_architecture_and_design_foundations.md"

EXPECTED_SRC_TOTAL = 36
EXPECTED_SRC_PRIMARY = 28          # §3 rows 13A-SRC-001..028
EXPECTED_SRC_SUPPLEMENTARY = 2     # §4 rows 029 (Cyber Nations), 030 (eRepublik)
EXPECTED_SRC_NEGATIVE = 1          # §4 row 031 (NationStates, negative access check)
EXPECTED_SRC_BOUNDARY = 5          # §5 rows 032..036
EXPECTED_FND = 40
EXPECTED_BP = 28
EXPECTED_DR = 24
EXPECTED_PR = 16
EXPECTED_STATES = 13
EXPECTED_NAV_SECTIONS = 8
EXPECTED_SCREENS = 100
EXPECTED_OVERLAYS = 8
EXPECTED_DS = 15
EXPECTED_RD = 8
EXPECTED_UR = 48
EXPECTED_OQ = 16
EXPECTED_GATES = 24
TALLY_TEXT = "**Tally: 23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED.**"


def load() -> dict[str, str]:
    texts: dict[str, str] = {}
    for key, path in DELIVERABLES.items():
        texts[key] = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    for key, path in GOVERNANCE.items():
        texts[key] = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    texts["archive"] = ARCHIVE.read_text(encoding="utf-8", errors="replace") if ARCHIVE.exists() else ""
    return texts


# Dynamic canonical legacy/project register definitions (derived from files on disk).
# Tuple fields: (prefix, zero_pad_width, doc_rel_paths_or_T_keys, canonical_def_regex, scope_label)
LEGACY_REGISTER_SPECS: tuple[tuple[str, int, tuple[str, ...], str, str], ...] = (
    ("F-PD", 3, ("stage-2/12_population_and_domestic_politics_formula_register.md",),
     r"^\*\*F-PD-(\d{3}[a-z]?)\b", "B-06 formula register"),
    ("TR", 3, ("stage-2/07_core_gameplay_loop_symbolic_world_and_turn_system.md",),
     r"\*\*TR-(\d{3}[a-z]?)\b", "B-02 turn & clock rules"),
    ("ACC", 3, ("stage-2/09_account_onboarding_nation_creation_and_progression.md",),
     r"\*\*ACC-(\d{3}[a-z]?)\b", "B-03 account rules"),
    ("NAT", 3, ("stage-2/09_account_onboarding_nation_creation_and_progression.md",),
     r"\*\*NAT-(\d{3}[a-z]?)\b", "B-03 nation creation rules"),
    ("NET", 3, ("stage-2/09_account_onboarding_nation_creation_and_progression.md",),
     r"\*\*NET-(\d{3}[a-z]?)\b", "B-03 network/multi-account rules"),
    ("ONB", 3, ("stage-2/09_account_onboarding_nation_creation_and_progression.md",),
     r"\*\*ONB-(\d{3}[a-z]?)\b", "B-03 onboarding/protection rules"),
    ("RRL", 3, ("stage-2/09_account_onboarding_nation_creation_and_progression.md",),
     r"\*\*RRL-(\d{3}[a-z]?)\b", "B-03 reroll/closure rules"),
    ("ECN", 3, ("stage-2/10_economy_resources_treasury_and_finances.md",),
     r"(?:\*\*|^\|\s*`?)ECN-(\d{3}[a-z]?)\b", "B-04 economy rules"),
    ("URB", 3, ("stage-2/11_cities_infrastructure_production_and_research.md",),
     r"\*\*URB-(\d{3}[a-z]?)\b", "B-05 cities/production rules"),
    ("DMP", 3, ("stage-2/12_population_and_domestic_politics.md",),
     r"\*\*DMP-(\d{3}[a-z]?)\b", "B-06 population/domestic politics rules"),
    ("MKT", 3, ("stage-2/13_trade_and_markets.md",),
     r"\*\*MKT-(\d{3}[a-z]?)\b", "B-07 trade/market rules"),
    ("DIP", 3, ("stage-2/15_diplomacy.md",),
     r"\*\*DIP-(\d{3}[a-z]?)\b", "B-08 diplomacy rules"),
    ("DPE", 3, ("stage-2/15_diplomacy_workflows_acceptance.md",),
     r"\bDPE-(\d{3})\b", "B-08 diplomacy edge-case specs"),
    ("ALL", 3, ("stage-2/16_alliances.md",),
     r"(?:^\|\s*`?ALL-|\*\*ALL-|`ALL-)(\d{3}[a-z]?)\b", "B-09 alliance rules"),
    ("AX", 2, ("stage-2/16_alliances_integration_contracts.md",),
     r"(?:^#{2,4}\s*`?AX-|^\|\s*`?AX-)(\d{2})\b", "B-09 integration contracts"),
    ("AN", 2, ("stage-2/16_alliances_workflows_acceptance.md",),
     r"^\|\s*`?AN-(\d{2})`?\s*\|", "B-09 notification matrices"),
    ("WAR", 3, ("stage-2/17_warfare_and_settlements.md",),
     r"^`WAR-(\d{3}[a-z]?)`", "B-10 warfare rules"),
    ("WEP", 3, ("stage-2/18_world_events_objectives_rankings_progression.md",),
     r"\*\*WEP-(\d{3}[a-z]?)\b", "B-11 world events/rankings rules"),
    ("WPC", 2, ("stage-2/19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md",),
     r"\bWPC-(\d{2})\b", "B-11 integration contracts"),
    ("ADM", 3, ("stage-2/20_fair_play_and_player_protection.md",),
     r"\*\*ADM-(\d{3}[a-z]?)\b", "B-12 admin boundary rules"),
    ("EVD", 3, ("stage-2/20_fair_play_and_player_protection.md",),
     r"\*\*EVD-(\d{3}[a-z]?)\b", "B-12 evidence/claim vocabulary rules"),
    ("FP", 3, ("stage-2/20_fair_play_and_player_protection.md",),
     r"\*\*FP-(\d{3}[a-z]?)\b", "B-12 fair-play rules"),
    ("FR", 3, ("stage-2/20_fair_play_and_player_protection.md",),
     r"\*\*FR-(\d{3}[a-z]?)\b", "B-12 anti-abuse rate/degradation rules"),
    ("MOD", 3, ("stage-2/20_fair_play_and_player_protection.md",),
     r"\*\*MOD-(\d{3}[a-z]?)\b", "B-12 moderation/appeal rules"),
    ("PRV", 3, ("stage-2/20_fair_play_and_player_protection.md",),
     r"\*\*PRV-(\d{3}[a-z]?)\b", "B-12 privacy rules"),
    ("SEC", 3, ("stage-2/20_fair_play_and_player_protection.md", "stage-1/08_security_privacy_fair_play_and_trust.md"),
     r"(?:\*\*|^\|\s*)SEC-(\d{3}[a-z]?)\b", "Stage-1 & B-12 security rules"),
    ("V", 2, ("stage-2/20_fair_play_and_player_protection.md",),
     r"^\|\s*`?V-(\d{2})`?\s*\|", "B-12 violation taxonomy"),
    ("B", 2, ("T:outline",),
     r"^###\s*B-(\d{2})\b", "Master bible outline sections"),
    ("FO", 3, ("stage-1/03_feature_comparison_opportunity_analysis.md",),
     r"(?:\(FO-|^\|\s*FO-)(\d{3})\b", "Stage-1 opportunity register"),
    ("CX", 1, ("stage-1/05_core_game_concept_and_design_pillars.md",),
     r"^###\s*CX-(\d)\b", "Stage-1 core game concepts"),
    ("AP", 3, ("stage-1/05_core_game_concept_and_design_pillars.md",),
     r"(?:^\|\s*|\*\*)AP-(\d{3})\b", "Stage-1 atmosphere/anti-patterns"),
    ("UXD", 3, ("stage-1/05_core_game_concept_and_design_pillars.md",),
     r"(?:^\|\s*|\*\*)UXD-(\d{3})\b", "Stage-1 UX direction rules"),
    ("DP", 3, ("stage-1/09_integrated_design_synthesis_and_readiness_audit.md",),
     r"^\|\s*DP-(\d{3})\s*\|", "Stage-1 design pillars"),
    ("SYS", 3, ("stage-1/06_core_gameplay_systems_and_interactions.md",),
     r"\*\*SYS-(\d{3})\b", "Stage-1 system charter register"),
    ("SIM", 3, ("stage-1/06_core_gameplay_systems_and_interactions.md",),
     r"(?:^\*\*|^\|\s*|^\s*-\s*\*\*)SIM-(\d{3})\b", "Stage-1 simulation principles"),
    ("ECON", 3, ("stage-1/07_economy_design_and_market_structure.md",),
     r"^\|\s*ECON-(\d{3})\s*\|", "Stage-1 economy model decisions"),
    ("ECV", 3, ("stage-1/07_economy_design_and_market_structure.md",),
     r"\bECV-(\d{3})\b", "Stage-1 economy validation tests"),
    ("F", 3, ("stage-1/02_strengths_weaknesses_player_frustrations.md",),
     r"(?:\*\*|^\|\s*)F-(\d{3})\b", "Stage-1 competitor frustration register"),
    ("G", 1, ("stage-1/07_economy_design_and_market_structure.md",),
     r"\bG-(\d)\b", "Stage-1/B-07 market readiness gates"),
    ("R", 2, ("stage-1/06_core_gameplay_systems_and_interactions.md", "stage-1/07_economy_design_and_market_structure.md"),
     r"(?:^\*\*|^\|\s*)R-(\d{2})\b", "Stage-1 risk register"),
)

LEGACY_WIDTHS: dict[str, int] = {pref: width for pref, width, _, _, _ in LEGACY_REGISTER_SPECS}
# Longest/compound prefixes first (`F-PD` before `F`) so prefix alternation never shadows `F-PD`.
LEGACY_PREFS_RE: str = "|".join(re.escape(pref) for pref, _, _, _, _ in LEGACY_REGISTER_SPECS)

_LEGACY_FILE_CACHE: dict[str, tuple[tuple[int, int], str]] = {}


def _read_cached_doc(rel: str) -> str:
    path = DOCS / rel
    if not path.exists():
        return ""
    st = path.stat()
    sig = (st.st_mtime_ns, st.st_size)
    cached = _LEGACY_FILE_CACHE.get(rel)
    if cached and cached[0] == sig:
        return cached[1]
    text = path.read_text(encoding="utf-8", errors="replace")
    _LEGACY_FILE_CACHE[rel] = (sig, text)
    return text


_LEGACY_UNIV_CACHE: dict[int, set[str]] = {}


def _load_legacy_universe(T: dict[str, str]) -> set[str]:
    """Dynamically collect every canonical Stage-1/Stage-2 legacy identifier from disk."""
    outline_text = T.get("outline", "")
    # Key by outline hash + disk mtime/size signatures so self-test runs don't re-scan 3k+ tokens repeatedly.
    cache_key = hash(outline_text)
    if cache_key in _LEGACY_UNIV_CACHE and _LEGACY_FILE_CACHE:
        return _LEGACY_UNIV_CACHE[cache_key]
    univ: set[str] = set()
    for pref, width, sources, pat, _ in LEGACY_REGISTER_SPECS:
        pat_re = re.compile(pat, re.M)
        for src in sources:
            if src.startswith("T:"):
                text = T.get(src[2:], "")
            else:
                text = _read_cached_doc(src)
            if not text:
                continue
            for m in pat_re.finditer(text):
                raw = next((g for g in m.groups() if g is not None), "")
                sm = re.fullmatch(r"0*(\d+)([a-z]?)", raw)
                if sm:
                    univ.add(f"{pref}-{int(sm.group(1)):0{width}d}{sm.group(2)}")
    _LEGACY_UNIV_CACHE[cache_key] = univ
    return univ


_EXPAND_PAT_CACHE: dict[tuple[str, int], tuple[re.Pattern, re.Pattern, re.Pattern]] = {}


def _expand_prefixed_tokens(
    text: str, prefs_re: str, width_map: dict[str, int], max_digits: int = 3
) -> set[str]:
    """Extract & expand single, slash-compound, and range-compound prefixed tokens."""
    key = (prefs_re, max_digits)
    cached = _EXPAND_PAT_CACHE.get(key)
    if cached is None:
        unit = rf"0*\d{{1,{max_digits}}}[a-z]?(?!\d*[A-Za-z_])"
        seg = rf"(?:(?:{prefs_re})-{unit}|{unit})"
        pat = re.compile(
            rf"(?<![A-Za-z0-9-])({prefs_re})-0*(\d{{1,{max_digits}}})([a-z]?)(?!\d*[A-Za-z_])"
            rf"((?:(?:[/,]|\.\.|[\u2013\u2026]|-(?=\d{{2,{max_digits}}}\b)){seg})*)"
        )
        dm_pat = re.compile(r"^(/|,|\.\.|[\u2013\u2026]|-)")
        im_pat = re.compile(
            rf"^(?:({prefs_re})-)?0*(\d{{1,{max_digits}}})([a-z]?)(?!\d*[A-Za-z_])"
        )
        cached = (pat, dm_pat, im_pat)
        _EXPAND_PAT_CACHE[key] = cached
    pat, dm_pat, im_pat = cached
    out: set[str] = set()
    for m in pat.finditer(text):
        cp, n1, s1, tail = m.group(1), int(m.group(2)), m.group(3), m.group(4)
        w = width_map[cp]
        out.add(f"{cp}-{n1:0{w}d}{s1}")
        pos, prev_num, prev_pref = 0, n1, cp
        while pos < len(tail):
            dm = dm_pat.match(tail[pos:])
            if not dm:
                break
            delim = dm.group(1)
            pos += len(delim)
            im = im_pat.match(tail[pos:])
            if not im:
                break
            next_pref = im.group(1) or prev_pref
            n2, s2 = int(im.group(2)), im.group(3)
            nw = width_map[next_pref]
            if (
                delim in ("\u2026", "..", "\u2013", "-")
                and not s2
                and n2 >= prev_num
                and n2 - prev_num <= 30
            ):
                for k in range(prev_num, n2 + 1):
                    out.add(f"{next_pref}-{k:0{nw}d}")
            else:
                out.add(f"{next_pref}-{n2:0{nw}d}{s2}")
            prev_pref, prev_num = next_pref, n2
            pos += im.end()
    return out


def _extract_legacy_tokens(text: str) -> set[str]:
    return _expand_prefixed_tokens(text, LEGACY_PREFS_RE, LEGACY_WIDTHS, max_digits=3)


def section(text: str, marker: str) -> str:
    """From the heading that starts with `marker` to the next `## ` heading."""
    i = text.find(marker)
    if i < 0:
        return ""
    nxt = text.find("\n## ", i + len(marker))
    return text[i:] if nxt < 0 else text[i:nxt]


def row_ids(text: str, family: str) -> list[int]:
    """Row-leading identifiers of one family, in document order."""
    pat = rf"^\|\s*`?{re.escape(family)}-(\d{{2,3}})`?\s*\|"
    return [int(m.group(1)) for m in re.finditer(pat, text, re.M)]


def row_cells(text: str, family: str) -> list[tuple[int, list[str]]]:
    out = []
    for line in text.splitlines():
        m = re.match(rf"^\|\s*`?{re.escape(family)}-(\d{{2,3}})`?\s*\|", line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append((int(m.group(1)), cells[1:]))
    return out


def contiguous(nums: list[int], start: int, end: int) -> bool:
    return nums == list(range(start, end + 1))


def status_value(text: str, key: str) -> str:
    """The value of one STATUS-block key, read inside the fenced block only."""
    m = re.search(r"<!-- STATUS:BEGIN -->(.*?)<!-- STATUS:END -->", text, re.S)
    if not m:
        return ""
    hit = re.search(rf"^{re.escape(key)}:[ \t]*([^\n]*)$", m.group(1), re.M)
    return hit.group(1).strip() if hit else ""


# ---------------------------------------------------------------------------
# checks — each returns a list of problems (empty == pass)
# ---------------------------------------------------------------------------

def c01_files(T):
    p = []
    for key, path in DELIVERABLES.items():
        if not path.exists():
            p.append(f"missing deliverable: {path.name}")
        elif len(T[key]) < 4000:
            p.append(f"{path.name} is implausibly short ({len(T[key])} chars)")
    return p


def c02_headers(T):
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        head = T[key][:2600]
        if "Prompt 13A" not in head:
            p.append(f"{key}: header does not identify Prompt 13A")
        if "2026-11-11" not in head:
            p.append(f"{key}: header carries no 2026-11-11 creation date")
        if not re.search(r"(?i)(no|not).{0,60}(implement|built|approved as a product commitment)"
                         r"|(approves no rule, screen|no screen is specified in final detail)", head):
            p.append(f"{key}: header states no research-level / no-implementation boundary")
    return p


def c03_src_register(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-SRC")
    p = []
    if not contiguous(nums, 1, EXPECTED_SRC_TOTAL):
        dup = [n for n in set(nums) if nums.count(n) > 1]
        missing = sorted(set(range(1, EXPECTED_SRC_TOTAL + 1)) - set(nums))
        p.append(f"13A-SRC rows are not 001..{EXPECTED_SRC_TOTAL} exactly once "
                 f"(duplicates={dup}, missing={missing}, rows={len(nums)})")
    s3, s4, s5 = (row_ids(section(t, "## 3."), "13A-SRC"),
                  row_ids(section(t, "## 4."), "13A-SRC"),
                  row_ids(section(t, "## 5."), "13A-SRC"))
    if not contiguous(s3, 1, EXPECTED_SRC_PRIMARY):
        p.append(f"§3 source rows are not 001..{EXPECTED_SRC_PRIMARY}: {s3}")
    if not contiguous(s4, 29, 29 + EXPECTED_SRC_SUPPLEMENTARY + EXPECTED_SRC_NEGATIVE - 1):
        p.append(f"§4 supplementary rows are not 029..031: {s4}")
    if not contiguous(s5, 32, 32 + EXPECTED_SRC_BOUNDARY - 1):
        p.append(f"§5 boundary rows are not 032..036: {s5}")
    return p


def c04_src_tokens(T):
    """No malformed, wrong-width, wrong-family or bad-suffix identifier survives.

    Rejects: non-digit suffixes (`13A-DR-005x`, `SCR-088_old`), wrong-family
    combinations (`13A-SCR-001`, `13A-OVL-01`), corrupted tokens (`13A-SR26` while
    exempting valid pass labels like `13A-C1`), and wrong zero-padded widths.
    """
    p = []
    three = ("SRC", "FND", "BP", "DR", "UR", "OQ")
    two = ("PR", "RD", "DS")
    scope = ("doc1", "doc2", "doc3", "doc4", "doc5")
    legacy_univ = _load_legacy_universe(T)
    legacy_sfx_pat = re.compile(
        rf"(?<![A-Za-z0-9-])({LEGACY_PREFS_RE}|REQ|D|DD|UD)-0*(\d{{1,4}})"
        r"(_[A-Za-z0-9_]+|[A-Za-z][A-Za-z0-9_]*)\b"
    )
    for key in scope:
        text = T[key]
        # Corrupted token letters+digit (`13A-SR26`), exempting valid pass labels (`13A-C1`).
        for m in re.finditer(r"13A-[A-Z]{1,4}\d", text):
            tail = text[m.start():m.end() + 4]
            if re.match(r"^13A-C\d+\b", tail):
                continue
            p.append(f"{key}: corrupted identifier at {text[max(0, m.start()-8):m.end()+6]!r}")
        for m in re.finditer(r"\b13A-(SCR|OVL|P13A)-\d+", text):
            p.append(f"{key}: wrong-family identifier {m.group(0)!r}")
        for m in re.finditer(
                r"\b(?:13A-(?:SRC|FND|BP|DR|PR|RD|DS|UR|OQ)|SCR|OVL|P13A)-\d{2,3}(?:_[A-Za-z0-9_]+|[A-Za-z][A-Za-z0-9_]*)\b",
                text):
            p.append(f"{key}: unsupported identifier suffix {m.group(0)!r}")
        for m in legacy_sfx_pat.finditer(text):
            pref, num_s, sfx = m.group(1), m.group(2), m.group(3)
            if pref in LEGACY_WIDTHS:
                norm = f"{pref}-{int(num_s):0{LEGACY_WIDTHS[pref]}d}{sfx}"
                if norm in legacy_univ:
                    continue
            p.append(f"{key}: unsupported legacy identifier suffix {m.group(0)!r}")
        for m in re.finditer(r"13A-([A-Z]{2,4})-([\d/,#]{1,60})", text):
            fam, num = m.group(1), m.group(2)
            if num.replace("/", "").replace(",", "").replace("#", "") == "":
                continue  # `13A-SRC-###` notation table
            width = 3 if fam in three else (2 if fam in two else 0)
            if width == 0:
                p.append(f"{key}: unknown 13A family 13A-{fam}-")
                continue
            parts = [x for x in re.split(r"[/,]", num) if x]
            bad = [x for x in parts if not re.fullmatch(rf"#{{3}}|\d{{{width}}}", x)]
            if bad:
                p.append(f"{key}: bad-width 13A-{fam}-{num!r} ({bad[0]!r} is not {width} digits)")
        for m in re.finditer(r"P13A-([\d/,#]{1,30})", text):
            parts = [x for x in re.split(r"[/,]", m.group(1)) if x]
            bad = [x for x in parts if x != "###" and not re.fullmatch(r"\d{2}", x)]
            if bad:
                p.append(f"{key}: bad-width P13A-{m.group(1)!r}")
        for m in re.finditer(r"(?<![\w-])(SCR|OVL)-([\d/,#]{1,80})", text):
            fam, num = m.group(1), m.group(2)
            width = 3 if fam == "SCR" else 2
            parts = [x for x in re.split(r"[/,]", num) if x]
            bad = [x for x in parts if x != "###" and not re.fullmatch(rf"\d{{{width}}}", x)]
            if bad:
                p.append(f"{key}: bad-width {fam}-{num!r} ({bad[0]!r})")
    return p


def c05_evidence_classes(T):
    """The class column is the source of truth; §10.1 must report what it says."""
    t = T["doc1"]
    rows = row_cells(section(t, "## 3."), "13A-SRC")
    if not rows:
        return ["§3 source rows could not be parsed"]
    counts = {"OBSERVED": 0, "DOCUMENTED": 0, "NOT-RETRIEVABLE": 0, "OTHER": 0}
    for _, cells in rows:
        cls = cells[1] if len(cells) > 1 else ""
        if cls.startswith("OBSERVED"):
            counts["OBSERVED"] += 1
        elif cls.startswith("DOCUMENTED"):
            counts["DOCUMENTED"] += 1
        elif cls.startswith("NOT-RETRIEVABLE"):
            counts["NOT-RETRIEVABLE"] += 1
        else:
            counts["OTHER"] += 1
            p = [f"row has no recognised evidence class: {cls[:40]!r}"]
            return p
    if sum(counts.values()) != EXPECTED_SRC_PRIMARY:
        return [f"§3 class rows total {sum(counts.values())}, expected {EXPECTED_SRC_PRIMARY}"]
    dist = section(t, "### 10.1")
    p = []
    for label, n in (("OBSERVED", counts["OBSERVED"]), ("DOCUMENTED", counts["DOCUMENTED"]),
                     ("NOT-RETRIEVABLE", counts["NOT-RETRIEVABLE"])):
        if not re.search(rf"\b{counts and n}\b `?{label}", dist):
            p.append(f"§10.1 does not state {n} {label} rows (computed from the class column)")
    if f"**{EXPECTED_SRC_PRIMARY + EXPECTED_SRC_BOUNDARY} are Politics & War**" not in dist:
        p.append("§10.1 does not report 33 Politics & War rows (28 primary + 5 boundary)")
    for claim in ("Of the 36 numbered source rows", "the two supplementary evidence rows",
                  "the supplementary negative access row"):
        if claim not in dist:
            p.append(f"§10.1 missing distribution claim {claim!r}")
    for cls in ("OBSERVED", "DOCUMENTED", "SECONDARY", "INFERRED", "NOT-RETRIEVABLE"):
        if cls not in section(t, "## 1."):
            p.append(f"§1 does not define the {cls} evidence class")
    # The acceptance register restates the same distribution on gate P13A-02; the
    # two statements must agree with the class column rather than with each other.
    gate02 = next((rest for num, rest in re.findall(
        r"^\|\s*`?P13A-(\d{2})`?\s*\|(.*)\|\s*$", section(T["doc5"], "## 5."), re.M) if num == "02"), "")
    for cls in ("OBSERVED", "DOCUMENTED", "NOT-RETRIEVABLE"):
        n = counts[cls]
        if n and not re.search(rf"\b{n} `?{cls}", gate02):
            p.append(f"P13A-02 does not restate the computed {n} {cls} rows")
    if gate02 and "33 of the 36" not in gate02:
        p.append("P13A-02 does not restate the 33-of-36 P&W distribution")
    return p


def c06_findings(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-FND")
    p = []
    if not contiguous(nums, 1, EXPECTED_FND):
        p.append(f"13A-FND rows are not 001..{EXPECTED_FND} exactly once ({len(nums)} rows)")
    for rid, cells in row_cells(section(t, "## 7."), "13A-FND"):
        if len(cells) != 3:
            p.append(f"13A-FND-{rid:03d} has {len(cells)} cells, expected 3 (finding, evidence, class)")
        elif not re.search(r"13A-SRC-\d{3}|SECONDARY|fixed constraint|boundary|constraint", cells[1]):
            p.append(f"13A-FND-{rid:03d} cites no evidence row")
        elif not re.search(r"(?i)OBSERVED|DOCUMENTED|SECONDARY|INFERRED|NOT-RETRIEVABLE|constraint|boundary",
                           cells[2]):
            p.append(f"13A-FND-{rid:03d} states no evidence class")
    return p


def c07_patterns(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-BP")
    p = []
    if not contiguous(nums, 1, EXPECTED_BP):
        p.append(f"13A-BP rows are not 001..{EXPECTED_BP} exactly once ({len(nums)} rows)")
    dispositions = 0
    for rid, cells in row_cells(section(t, "## 8."), "13A-BP"):
        if len(cells) != 3:
            p.append(f"13A-BP-{rid:03d} has {len(cells)} cells, expected 3")
            continue
        if re.search(r"(?i)\*\*(retain|adapt|reject|defer|provisional)", cells[1]):
            dispositions += 1
        else:
            p.append(f"13A-BP-{rid:03d} states no retain/adapt/reject disposition")
    if dispositions != EXPECTED_BP:
        p.append(f"only {dispositions} of {EXPECTED_BP} patterns carry a disposition")
    return p


def c08_recommendations(T):
    t = T["doc1"]
    nums = row_ids(t, "13A-DR")
    p = []
    if not contiguous(nums, 1, EXPECTED_DR):
        p.append(f"13A-DR rows are not 001..{EXPECTED_DR} exactly once ({len(nums)} rows)")
    for rid, cells in row_cells(section(t, "## 9."), "13A-DR"):
        if len(cells) != 2:
            p.append(f"13A-DR-{rid:03d} has {len(cells)} cells, expected 2")
        elif not re.search(r"13A-SRC|13A-FND|13A-BP|REQ-|D-\d{3}|TR-\d|WEP-|WAR-|fixed", cells[1]):
            p.append(f"13A-DR-{rid:03d} states no basis")
    return p


def c09_benchmark(T):
    t = T["doc1"]
    p = []
    if "https://politicsandwar.com/" not in t:
        p.append("primary benchmark URL absent")
    if not re.search(r"(?i)primary (UI )?benchmark", t):
        p.append("the primary-benchmark role is not stated")
    if "Prohibited categories" not in t:
        p.append("the prohibited-comparator-category paragraph is missing")
    if "approves no rule, screen, component, number or implementation" not in t:
        p.append("the inputs-only boundary sentence is missing")
    if "2026-11-11" not in t:
        p.append("no retrieval date recorded")
    return p


def c10_principles(T):
    t = T["doc2"]
    p = []
    nums = row_ids(t, "13A-PR")
    if not contiguous(nums, 1, EXPECTED_PR):
        p.append(f"13A-PR rows are not 01..{EXPECTED_PR:02d} exactly once ({len(nums)} rows)")
    nav = [l for l in section(t, "## 5.").splitlines() if re.match(r"^\|\s*\d+\s*\|", l)]
    if len(nav) != EXPECTED_NAV_SECTIONS:
        p.append(f"navigation register has {len(nav)} sections, expected {EXPECTED_NAV_SECTIONS}")
    states = [l for l in section(t, "## 6.").splitlines() if re.match(r"^\|\s*\*\*", l)]
    if len(states) != EXPECTED_STATES:
        p.append(f"application-state register has {len(states)} states, expected {EXPECTED_STATES}")
    for term in ("PROVISIONAL_BLOCK", "suppressed"):
        if term not in section(t, "## 6."):
            p.append(f"state register does not name {term}")
    for term in ("mapless", "Network View", "War Operations Board"):
        if term not in t:
            p.append(f"architecture text does not use the fixed term {term!r}")
    if "remain reserved" not in t or "D-203" not in t:
        p.append("brand/visual-identity values are not recorded as owner-reserved (D-203)")
    if "no implementation, no visual asset, no component built" not in t:
        p.append("the no-implementation boundary sentence is missing")
    return p


def _scr_rows(T):
    t = T["doc3"]
    return row_cells(section(t, "## 2."), "SCR")


def c11_screen_ids(T):
    nums = row_ids(T["doc3"], "SCR")
    if not contiguous(nums, 1, EXPECTED_SCREENS):
        dup = [n for n in set(nums) if nums.count(n) > 1]
        missing = sorted(set(range(1, EXPECTED_SCREENS + 1)) - set(nums))
        return [f"SCR rows are not 001..{EXPECTED_SCREENS} exactly once "
                f"(rows={len(nums)}, duplicates={dup}, missing={missing})"]
    bad = [rid for rid, cells in _scr_rows(T) if len(cells) != 5]
    if bad:
        return [f"SCR rows with the wrong cell count (expected 6 columns): {bad[:8]}"]
    return []


def c12_screen_tally(T):
    rows = _scr_rows(T)
    if len(rows) != EXPECTED_SCREENS:
        return [f"screen register parsed {len(rows)} rows, expected {EXPECTED_SCREENS}"]
    tally = {"mandatory": 0, "admin": 0, "conditional": 0, "provisional": 0}
    conditional, provisional = [], []
    for rid, cells in rows:
        cls = cells[3].strip("*").strip()
        if cls == "Mandatory":
            tally["mandatory"] += 1
        elif cls == "Mandatory (admin)":
            tally["admin"] += 1
        elif cls.lower().startswith("conditional"):
            tally["conditional"] += 1
            conditional.append(rid)
        elif cls.lower().startswith("provisional"):
            tally["provisional"] += 1
            provisional.append(rid)
        else:
            return [f"unknown screen class {cls!r} on SCR-{rid:03d}"]
    p = []
    if tally != {"mandatory": 85, "admin": 10, "conditional": 4, "provisional": 1}:
        p.append(f"computed class tally {tally} != the registered 85/10/4/1")
    arith = section(T["doc3"], "## 7.")
    if conditional and "SCR-020/038/039/077" not in arith:
        p.append("§7 does not name the computed Conditional set")
    if sorted(conditional) != [20, 38, 39, 77]:
        p.append(f"Conditional screens are {conditional}, expected [20, 38, 39, 77]")
    if provisional != [68]:
        p.append(f"Provisional screens are {provisional}, expected [68]")
    for claim in ("Player-facing: 90", "Administrative: 10 (Mandatory)", "Total screens **100**",
                  "overlays 8", "sections 8"):
        if claim not in arith:
            p.append(f"§7 arithmetic line missing {claim!r}")
    return p


def c13_admin_family(T):
    rows = _scr_rows(T)
    admin = [rid for rid, cells in rows if cells[1] == "Admin"]
    p = []
    if admin != list(range(91, 101)):
        p.append(f"Parent=Admin rows are {admin[:12]}…, expected SCR-091..100")
    if not re.search(r"SCR-091\u2026SCR-100", T["doc3"]):
        p.append("the administrative family is not registered as SCR-091…SCR-100")
    return p


def c14_hierarchy(T):
    t = T["doc3"]
    p = []
    if "```mermaid" not in t:
        p.append("no Mermaid hierarchy diagram")
    else:
        start = t.index("```mermaid")
        graph = t[start:t.index("```", start + 10)]
        if "graph" not in graph[:120].lower() and "flowchart" not in graph[:120].lower():
            p.append("the Mermaid block declares no graph/flowchart")
        # The diagram addresses screens by their SCR numeric suffix, so the eight
        # section nodes plus the two roots are the checkable structure.
        for label in ("Public shell", "Authenticated shell", "Admin 091-100"):
            if label not in graph:
                p.append(f"hierarchy diagram omits {label!r}")
        for n in range(1, 9):
            if not re.search(rf"{n} (Home|Economy|Cities|Politics|Foreign|War|World|Account)", graph):
                p.append(f"hierarchy diagram omits navigation section {n}")
    nums = row_ids(t, "OVL")
    if not contiguous(nums, 1, EXPECTED_OVERLAYS):
        p.append(f"OVL rows are not 01..{EXPECTED_OVERLAYS} exactly once ({len(nums)} rows)")
    if not re.search(r"(?i)cross-system transition", t):
        p.append("no cross-system transition table")
    if not re.search(r"(?i)navigation-quality audit|seven-risk", t):
        p.append("the navigation-quality audit is missing")
    return p


def c15_responsive_ds(T):
    t = T["doc4"]
    p = []
    ds = row_ids(t, "13A-DS")
    if not contiguous(ds, 1, EXPECTED_DS):
        p.append(f"13A-DS rows are not 01..{EXPECTED_DS} exactly once ({len(ds)} rows)")
    rd_rows = row_ids(t, "13A-RD")
    if not contiguous(rd_rows, 2, EXPECTED_RD):
        p.append(f"13A-RD table rows are not 02..{EXPECTED_RD}: {rd_rows}")
    if "13A-RD-01" not in t:
        p.append("13A-RD-01 is not recorded anywhere in the responsive foundations")
    if "13A-RD-01" in [f"13A-RD-{n:02d}" for n in rd_rows]:
        p.append("13A-RD-01 must be a prose rule, not a duplicated table row")
    coverage = (("token discipline", r"(?i)token"),
                ("WCAG thresholds", r"(?i)WCAG"),
                ("the six-number-type register law", r"(?i)six-number|number-type"),
                ("the component state matrix", r"focus-visible"))
    for term, pat in coverage:
        if not re.search(pat, t):
            p.append(f"design-system foundations do not cover {term!r}")
    return p


def c16_responsive_boundaries(T):
    t = T["doc4"]
    p = []
    if "same game with the same rules" not in t:
        p.append("the same-rules-every-device guarantee is missing")
    if "Not owner-approved numbers" not in t or "Provisional breakpoints" not in t:
        p.append("breakpoints are not labelled provisional, not owner-approved")
    if "no CSS, no framework, no component implementation" not in t:
        p.append("the no-CSS/no-framework boundary is missing")
    if "no compliance claim is made" not in t:
        p.append("the no-accessibility-compliance-claim boundary is missing")
    for oq in ("13A-OQ-001", "13A-OQ-002"):
        if oq not in t:
            p.append(f"owner-reserved brand question {oq} is not referenced")
    return p


def c17_ur_register(T):
    t = T["doc5"]
    hits = re.findall(r"^\|\s*`?UR-(\d{3})`?\s*\|", t, re.M)
    nums = [int(h) for h in hits]
    p = []
    if not contiguous(sorted(set(nums)), 1, EXPECTED_UR):
        p.append(f"UR identifiers are not 001..{EXPECTED_UR} ({len(set(nums))} distinct)")
    for n in range(1, EXPECTED_UR + 1):
        if nums.count(n) != 2:
            p.append(f"UR-{n:03d} appears as a row {nums.count(n)} times, expected 2 "
                     "(candidate register + dependency ledger)")
            break
    return p


def c18_open_questions(T):
    nums = row_ids(section(T["doc5"], "## 4."), "OQ")
    if not contiguous(nums, 1, EXPECTED_OQ):
        return [f"OQ rows are not 001..{EXPECTED_OQ} exactly once ({len(nums)} rows)"]
    buckets = 0
    body = section(T["doc5"], "## 4.")
    for label in ("owner", "technical", "design", "legal", "research", "calibration", "scope"):
        if re.search(rf"(?i){label}", body):
            buckets += 1
    if buckets < 5:
        return [f"the open-question register exposes only {buckets} decision buckets"]
    return []


def _gate_rows(T):
    return re.findall(r"^\|\s*`?P13A-(\d{2})`?\s*\|(.*)\|\s*$", section(T["doc5"], "## 5."), re.M)


def c19_gate_rows(T):
    p = []
    nums = [int(m.group(1)) for m in re.finditer(r"^\|\s*`?P13A-(\d{2})`?\s*\|",
                                                 section(T["doc5"], "## 5."), re.M)]
    if not contiguous(nums, 1, EXPECTED_GATES):
        dup = [n for n in set(nums) if nums.count(n) > 1]
        missing = sorted(set(range(1, EXPECTED_GATES + 1)) - set(nums))
        p.append(f"P13A gates are not 01..{EXPECTED_GATES} exactly once "
                 f"(rows={len(nums)}, duplicates={dup}, missing={missing})")
    for num, rest in _gate_rows(T):
        cells = [c.strip() for c in rest.split("|")]
        results = [c for c in cells if re.fullmatch(
            r"\*\*(PASS|PARTIAL|FAIL|BLOCKED|NOT RUN|NOT APPLICABLE)\*\*", c)]
        if len(results) != 1:
            p.append(f"P13A-{num} has {len(results)} bolded result cells, expected exactly 1")
    return p


def c20_gate_tally(T):
    p = []
    counts = {"PASS": 0, "PARTIAL": 0, "FAIL": 0, "BLOCKED": 0}
    partial_ids = []
    for num, rest in _gate_rows(T):
        cells = [c.strip() for c in rest.split("|")]
        for c in cells:
            m = re.fullmatch(r"\*\*(PASS|PARTIAL|FAIL|BLOCKED)\*\*", c)
            if m:
                counts[m.group(1)] += 1
                if m.group(1) == "PARTIAL":
                    partial_ids.append(num)
    claimed = re.search(r"\*\*Tally: (\d+) PASS / (\d+) PARTIAL / (\d+) FAIL / (\d+) BLOCKED\.\*\*",
                        T["doc5"])
    if not claimed:
        return ["the gate register states no bolded PASS/PARTIAL/FAIL/BLOCKED tally"]
    got = tuple(int(x) for x in claimed.groups())
    want = (counts["PASS"], counts["PARTIAL"], counts["FAIL"], counts["BLOCKED"])
    if got != want:
        p.append(f"stated tally {got} disagrees with the computed gate results {want}")
    if claimed.group(0) != TALLY_TEXT:
        p.append(f"tally sentence is not the canonical {TALLY_TEXT!r}")
    if partial_ids != ["10"]:
        p.append(f"PARTIAL gates are {partial_ids}, expected exactly ['10'] (P13A-10)")
    return p


def c21_identifier_policy(T):
    t = T["doc5"]
    p = []
    if "REQ-870" not in t or "reserved" not in t:
        p.append("REQ-870 is not recorded as reserved for Prompt 13B")
    if not re.search(r"(?i)no global `?REQ-`?|allocated no global", t):
        p.append("the no-global-REQ-allocation policy is not stated")
    if not re.search(r"(?i)no global `?UD-`?|UD-0\d\d`? remain Open", t) \
            and "resolved none" not in t:
        p.append("the UD non-resolution duty is not stated")
    if "none is implemented" not in t:
        p.append("the acceptance register does not say none is implemented")
    return p


def c22_req_citations(T):
    defined = {int(m.group(1)) for m in re.finditer(r"^\|\s*REQ-(\d{3})\s*\|", T["tracker"], re.M)}
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        for line in T[key].splitlines():
            for m in re.finditer(r"REQ-(\d{3})\b", line):
                n = int(m.group(1))
                if n in defined:
                    continue
                if n == 870 and re.search(r"(?i)reserved|frontier", line):
                    continue
                p.append(f"{key}: unresolved REQ-{n:03d} in {line[:70]!r}")
    return p


def c23_decision_citations(T):
    d_ids = {int(m.group(1)) for m in re.finditer(r"^\| D-(\d{3}) \|", T["decisions"], re.M)}
    ud_ids = {int(m.group(1)) for m in re.finditer(r"^\|\s*`?UD-(\d{3})`?\s*\|", T["unresolved"], re.M)}
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        text = T[key]
        for m in re.finditer(r"\bD-(\d{3})\b", text):
            if int(m.group(1)) not in d_ids:
                p.append(f"{key}: cites D-{m.group(1)} which is not in DECISIONS.md")
        for m in re.finditer(r"\bUD-(\d{3})\b", text):
            if int(m.group(1)) not in ud_ids:
                p.append(f"{key}: cites UD-{m.group(1)} which is not in the unresolved register")
    seen = set()
    return [x for x in p if not (x in seen or seen.add(x))]


def c24_family_citations(T):
    """Every 13A-/SCR-/OVL-/P13A- (including compound & shorthand) resolves."""
    defined = {
        "13A-SRC": set(row_ids(T["doc1"], "13A-SRC")),
        "13A-FND": set(row_ids(T["doc1"], "13A-FND")),
        "13A-BP": set(row_ids(T["doc1"], "13A-BP")),
        "13A-DR": set(row_ids(T["doc1"], "13A-DR")),
        "13A-PR": set(row_ids(T["doc2"], "13A-PR")),
        "SCR": set(row_ids(T["doc3"], "SCR")),
        "OVL": set(row_ids(T["doc3"], "OVL")),
        "13A-RD": set(row_ids(T["doc4"], "13A-RD")) | {1},
        "13A-DS": set(row_ids(T["doc4"], "13A-DS")),
        "13A-OQ": set(row_ids(T["doc5"], "OQ")),
        "13A-UR": set(row_ids(T["doc5"], "UR")),
        "P13A": set(row_ids(T["doc5"], "P13A")),
    }
    short_map = {
        "SRC": "13A-SRC", "FND": "13A-FND", "BP": "13A-BP", "DR": "13A-DR",
        "PR": "13A-PR", "RD": "13A-RD", "DS": "13A-DS", "OQ": "13A-OQ", "UR": "13A-UR",
    }
    d_slice = "\n".join(l for l in T["decisions"].splitlines()
                        if re.match(r"^\|\s*D-(?:198|199|20[0-5])\s*\|", l))
    dd_slice = "\n".join(l for l in T["register04"].splitlines()
                         if re.match(r"^\|\s*DD-(?:24[6-9]|25[0-3])\s*\|", l))
    targets = [("doc1", T["doc1"]), ("doc2", T["doc2"]), ("doc3", T["doc3"]),
               ("doc4", T["doc4"]), ("doc5", T["doc5"]),
               ("decisions:D-198..205", d_slice), ("register04:DD-246..253", dd_slice)]
    pat = re.compile(
        r"(?<![A-Za-z0-9-])(13A-SRC|13A-FND|13A-BP|13A-DR|13A-PR|13A-RD|13A-DS|13A-OQ|13A-UR|"
        r"SCR|OVL|P13A|SRC|FND|BP|DR|PR|RD|DS|OQ|UR)-0*(\d{1,3})"
        r"(?:([/,…\-\u2013]+|\.\.)0*(\d{1,3}(?:[/,]\d{1,3})*))?\b"
    )
    p = []
    for label, text in targets:
        for m in pat.finditer(text):
            raw_fam, first, sep, rest = m.group(1), int(m.group(2)), m.group(3), m.group(4)
            fam = short_map.get(raw_fam, raw_fam)
            nums = [first]
            if rest is not None:
                if sep in ("…", "..", "-", "\u2013"):
                    end = int(re.split(r"[/,]", rest)[0])
                    if end >= first and end - first <= 100:
                        nums = list(range(first, end + 1))
                    else:
                        nums.extend(int(x) for x in re.split(r"[/,]", rest) if x.isdigit())
                else:
                    nums.extend(int(x) for x in re.split(r"[/,]", rest) if x.isdigit())
            for n in nums:
                if n not in defined[fam]:
                    p.append(f"{label}: dangling or compound-invalid citation {m.group(0)} -> {fam}-{n:03d}")
    return p


def c25_decision_records(T):
    p = []
    rows = re.findall(r"^\| D-(\d{3}) \| (2026-11-11) \|", T["decisions"], re.M)
    got = sorted(int(n) for n, _ in rows)
    if got != list(range(198, 206)):
        p.append(f"DECISIONS.md rows dated 2026-11-11 are {got}, expected D-198..D-205")
    dd = row_ids(T["register04"], "DD")
    if not contiguous(dd, 1, 253):
        p.append(f"stage-2/04 DD rows are not contiguous to DD-253 (max={max(dd) if dd else None})")
    for n in range(246, 254):
        if f"| DD-{n:03d} |" not in T["register04"]:
            p.append(f"DD-{n:03d} row missing from the mirrored position register")
    return p


def c26_status_blocks(T):
    p = []
    keys = ("ai_context", "ai_handoff", "progress")
    for k in keys:
        if status_value(T[k], "stage_2_next_prompt") != "13B":
            p.append(f"{k}: stage_2_next_prompt is "
                     f"{status_value(T[k], 'stage_2_next_prompt')!r}, expected 13B")
        if status_value(T[k], "decisions_range") != "D-001..D-205":
            p.append(f"{k}: decisions_range is {status_value(T[k], 'decisions_range')!r}")
        if status_value(T[k], "status_updated") != "2026-11-12":
            p.append(f"{k}: status_updated is {status_value(T[k], 'status_updated')!r}")
    dates = [status_value(T[k], "status_updated") for k in keys]
    if len(set(dates)) != 1:
        p.append(f"status_updated values disagree across continuity files: {dates!r}")
    ui = [status_value(T[k], "ui_foundations") for k in keys]
    if not all(ui):
        p.append("ui_foundations status key missing from at least one continuity file")
    elif len(set(ui)) != 1:
        p.append("ui_foundations status entries disagree across the three continuity files")
    if "Prompt 13A" not in T["ai_context"][:6000] or "Prompt 13A" not in T["progress"][:6000]:
        p.append("no Prompt 13A current-status block at the head of AI_CONTEXT/PROJECT_PROGRESS")
    return p


def c27_roadmap_registration(T):
    p = []
    if not re.search(r"^## 87\. Prompt 13A", T["log"], re.M):
        p.append("progress log has no §87 for Prompt 13A")
    if not re.search(r"^## 88\. Prompt 13A-C1", T["log"], re.M):
        p.append("progress log has no §88 for Prompt 13A-C1")
    if not re.search(r"^## 89\. Prompt 13A-C1-R1", T["log"], re.M):
        p.append("progress log has no §89 for Prompt 13A-C1-R1")
    if not re.search(r"^## 90\. Prompt 13A-C1-R2", T["log"], re.M):
        p.append("progress log has no §90 for Prompt 13A-C1-R2")
    if "Executed split (2026-11-11; D-198)" not in T["prompt_roadmap"]:
        p.append("the Stage 2 roadmap does not register the executed 13A/13B split")
    if "13A" not in T["prompt_roadmap"] or "13B" not in T["prompt_roadmap"]:
        p.append("the Stage 2 roadmap prompt table does not carry both 13A and 13B")
    b13 = section(T["outline"], "### B-13")
    if "`21_interface_and_player_journeys.md`" not in b13:
        p.append("outline B-13 does not use the D-198 path 21_interface_and_player_journeys.md")
    if "20_interface_and_player_journeys.md" in b13:
        p.append("outline B-13 still presents the superseded 20_ path as current")
    return p


def c28_prompt_archive(T):
    p = []
    if not ARCHIVE.exists():
        return ["the Prompt 13A instruction is not archived under docs/prompts/"]
    head = T["archive"][:2000]
    if "Archival provenance" not in head:
        p.append("the archive carries no provenance paragraph")
    if "# PROMPT 13A" not in T["archive"][:400]:
        p.append("the archive does not preserve the original title line")
    if "prompt_13A_ui_research_architecture_and_design_foundations.md" not in T["prompt_index"]:
        p.append("docs/prompts/INDEX.md has no Prompt 13A row")
    if re.search(r"SHA-256 `[0-9a-f]{64}`", T["prompt_index"]) is None:
        p.append("docs/prompts/INDEX.md records no stored-bytes digest")
    return p


def c29_protected_statuses(T):
    """Prompt 13A may not have quietly advanced any preserved 12A/12B/12C status."""
    joined = "\n".join(T[key] for key in ("ai_context", "ai_handoff", "progress", "roadmap",
                                         "handoff_stage2", "log", "doc5"))
    p = []
    required = (
        "D-014",
        "DEFERRED BY OWNER",
        "NOT CLOSED",
        "P12B-14",
        "P12B-16",
        "P12B-23",
        "16 PASS / 2 PARTIAL / 2 BLOCKED",
        "378",
        "owner acceptance GRANTED",
    )
    for token in required:
        if token not in joined:
            p.append(f"protected-status token absent from the synchronized record: {token!r}")
    if not re.search(r"(?i)(R7|independent acceptance).{0,160}(not accepted|not independently)",
                     joined):
        p.append("R7's outstanding independent acceptance is not preserved")
    if "five residual weaknesses" not in joined and "five further bypass classes" not in joined:
        p.append("the five known R7 residual weaknesses are not preserved")
    for obligation in ("0005", "audit trigger", "tests/sql"):
        if obligation not in joined:
            p.append(f"outstanding security obligation {obligation!r} is not preserved")
    return p


def c30_hygiene(T):
    """Line-anchored conflict markers only.

    Progress log §86 quotes the markers as evidence of the *repaired* baseline
    defect; a quoted token inside a sentence is documentation, while a marker at
    column zero is an unrepaired hunk.
    """
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5", "ai_context", "ai_handoff", "progress",
                "roadmap", "decisions", "register04", "tracker", "outline", "prompt_roadmap",
                "log", "handoff_stage2", "archive"):
        for line in T[key].splitlines():
            if re.match(r"^<<<<<<<[ \n]|^=======$|^>>>>>>>[ \n]", line):
                p.append(f"{key}: unrepaired conflict-marker line {line[:30]!r}")
    return p


def c31_links(T):
    p = []
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        base = RESEARCH
        for m in re.finditer(r"\]\(([^)\s#]+)(?:#[^)]*)?\)", T[key]):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (base / target).exists():
                p.append(f"{key}: unresolved relative link {target!r}")
    return p


def c32_no_overclaim(T):
    p = []
    banned = (r"(?i)\b(?:ui|frontend|screen|component|framework)\b[^.\n]{0,30}"
              r"\b(?:has been|was|is)\s+implemented",
              r"(?i)deployed the (?:ui|frontend)",
              r"(?i)accessibility conformance (?:verified|achieved|certified)",
              r"(?i)conformance verified",
              r"(?i)breakpoints? (?:are |is )?owner-approved",
              r"(?i)brand identity (?:is|was) decided")
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5", "log"):
        for pat in banned:
            for m in re.finditer(pat, T[key]):
                clause = T[key][max(0, m.start() - 120):m.start()]
                # "No appeal mechanic, migration or UI is implemented" is the boundary
                # sentence itself; only an unqualified assertion is an over-claim.
                if re.search(r"(?i)\b(?:no|not|nothing|never|non)\b[^.\n]{0,110}$", clause):
                    continue
                p.append(f"{key}: over-claim {m.group(0)[:60]!r}")
    if "## 87." not in T["log"]:
        p.append("progress log §87 missing")
    return p


# Machine-checkable semantic cross-reference table:
# (label, source_key, line_anchor_regex, required_ids_any, forbidden_ids_any)
def _claim(
    record_id: str,
    doc_key: str,
    anchor: str,
    *,
    subject: str,
    classification: str,
    self_ids: tuple[str, ...] = (),
    allow_src: tuple[str, ...] = (),
    allow_fnd: tuple[str, ...] = (),
    allow_bp: tuple[str, ...] = (),
    allow_dr: tuple[str, ...] = (),
    allow_deps: tuple[str, ...] = (),
    allow_reqs: tuple[str, ...] = (),
    allow_dec: tuple[str, ...] = (),
    allow_legacy: tuple[str, ...] = (),
    required_any: tuple[str, ...] = (),
    required_markers: tuple[str, ...] = (),
    rationale: str = "",
) -> dict:
    """Build a strict, machine-checkable claim-to-citation allowlist record.

    Supporting research evidence (`allow_src`, `allow_fnd`, `allow_bp`, `allow_dr`)
    is kept strictly separate from system dependencies and governance cross-references
    (`allow_deps`, `allow_reqs`, `allow_dec`, `allow_legacy`). Non-`REQ-` internal 13A
    tokens passed via `allow_reqs` are normalized into `allow_deps` for compatibility.
    """
    compat_deps = {t for t in allow_reqs if not t.startswith("REQ-")}
    only_reqs = {t for t in allow_reqs if t.startswith("REQ-")}
    tok_m = re.fullmatch(r"\^\\\|\\s\*(?:`\\\?)?([A-Za-z0-9-]+)(?:`\\\?)?\\s\*\\\|", anchor)
    return {
        "record_id": record_id,
        "doc_key": doc_key,
        "anchor": anchor,
        "anchor_re": re.compile(anchor),
        "row_tok": tok_m.group(1) if tok_m else None,
        "subject": subject,
        "classification": classification,
        "self_ids": frozenset(self_ids),
        "allow_src": frozenset(allow_src),
        "allow_fnd": frozenset(allow_fnd),
        "allow_bp": frozenset(allow_bp),
        "allow_dr": frozenset(allow_dr),
        "allow_deps": frozenset(allow_deps) | compat_deps,
        "allow_reqs": frozenset(only_reqs),
        "allow_dec": frozenset(allow_dec),
        "allow_legacy": frozenset(allow_legacy),
        "required_any": tuple(required_any),
        "required_markers": tuple(required_markers),
        "rationale": rationale,
    }


def _table_claims(specs: tuple[tuple, ...]) -> list[dict]:
    """Expand compact register row allowlist specs into `_claim` records."""
    out = []
    for rid, doc_key, row_tok, src, fnd, bp, dr, dep, req, dec, leg in specs:
        cls = "BENCHMARK_SUPPORTED" if (src or fnd or bp) and not (req or dec or leg or dr) else (
            "NS_RULE_SUPPORTED" if (req or dec or leg or dr) and not (src or fnd or bp)
            else "HYBRID_BENCHMARK_AND_NS_RULE"
        )
        anchor = rf"^\|\s*`?{re.escape(row_tok)}`?\s*\|"
        self_ids = (row_tok, f"13A-{row_tok}") if row_tok.startswith("UR-") else (row_tok,)
        out.append(_claim(
            rid, doc_key, anchor,
            subject=f"Register row {row_tok} strict allowlist",
            classification=cls,
            self_ids=self_ids,
            allow_src=src, allow_fnd=fnd, allow_bp=bp, allow_dr=dr,
            allow_deps=dep, allow_reqs=req, allow_dec=dec, allow_legacy=leg,
        ))
    return out


CLAIM_ALLOWLISTS = [
    # --- doc1: P&W UI research source->finding & recommendation traceability ---
    _claim("doc1:13A-FND-003", "doc1", r"^\|\s*`?13A-FND-003`?\s*\|",
           subject="12-section public nation profile density", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-003",), allow_src=("13A-SRC-004",), required_any=("13A-SRC-004",),
           rationale="Nation profile density is directly observed on the P&W nation profile page (SRC-004)."),
    _claim("doc1:13A-FND-013", "doc1", r"^\|\s*`?13A-FND-013`?\s*\|",
           subject="Public API / machine-readable world export", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-013",), allow_src=("13A-SRC-023", "13A-SRC-024"),
           required_any=("13A-SRC-023", "13A-SRC-024"),
           rationale="API/export support is grounded solely in API docs/key-gate evidence (SRC-023/024), not UI a11y."),
    _claim("doc1:13A-FND-017", "doc1", r"^\|\s*`?13A-FND-017`?\s*\|",
           subject="Alliance and Color columns in P&W tables", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-017",), allow_src=("13A-SRC-002", "13A-SRC-005", "13A-SRC-007"),
           required_any=("13A-SRC-002", "13A-SRC-005", "13A-SRC-007"),
           rationale="Alliance + Color HTML table columns observed across SRC-002/005/007."),
    _claim("doc1:13A-FND-026", "doc1", r"^\|\s*`?13A-FND-026`?\s*\|",
           subject="Logged-out world catalogue navigation vs NOT-RETRIEVABLE auth Home", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-026",), allow_src=("13A-SRC-003", "13A-SRC-032"),
           required_any=("13A-SRC-003", "13A-SRC-032"),
           rationale="Logged-out public nav observed on SRC-003; authenticated console bounded by SRC-032."),
    _claim("doc1:13A-FND-027", "doc1", r"^\|\s*`?13A-FND-027`?\s*\|",
           subject="Long-page scrolling without progressive disclosure", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-027",), allow_src=("13A-SRC-004", "13A-SRC-007"),
           required_any=("13A-SRC-004", "13A-SRC-007"),
           rationale="Long-page density observed on profile and Top-100 pages (SRC-004/007)."),
    _claim("doc1:13A-FND-028", "doc1", r"^\|\s*`?13A-FND-028`?\s*\|",
           subject="Single-metric leaderboards and API export", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-028",), allow_src=("13A-SRC-007", "13A-SRC-023"),
           required_any=("13A-SRC-007", "13A-SRC-023"),
           rationale="Leaderboard export limitation stems from SRC-007 and API docs SRC-023, not keyboard UX."),
    _claim("doc1:13A-FND-031", "doc1", r"^\|\s*`?13A-FND-031`?\s*\|",
           subject="Bounded Alliance + Color column observation (CSS unverified)", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-031",), allow_src=("13A-SRC-002", "13A-SRC-005", "13A-SRC-007"),
           required_any=("13A-SRC-002", "13A-SRC-005", "13A-SRC-007"),
           rationale="HTML column parity verified in SRC-002/005/007; client CSS swatch channel unverified."),
    _claim("doc1:13A-FND-032", "doc1", r"^\|\s*`?13A-FND-032`?\s*\|",
           subject="Bounded logged-out shell fallback on gated routes", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-FND-032",), allow_src=("13A-SRC-009", "13A-SRC-025", "13A-SRC-032"),
           required_any=("13A-SRC-009", "13A-SRC-025", "13A-SRC-032"),
           rationale="Logged-out HTTP shell fallback observed on SRC-009/025; auth states bounded by SRC-032."),
    _claim("doc1:13A-DR-001", "doc1", r"^\|\s*`?13A-DR-001`?\s*\|",
           subject="Command Digest + Inbox Home surface", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-DR-001",), allow_src=("13A-SRC-032",), allow_fnd=("13A-FND-026",),
           allow_reqs=("REQ-022",), allow_legacy=("DP-002", "TR-089"),
           required_any=("13A-FND-026", "13A-SRC-032"),
           rationale="Driven by NS digest/re-entry rules (TR-089/REQ-022/DP-002) and contrasted with bounded FND-026/SRC-032."),
    _claim("doc1:13A-DR-015", "doc1", r"^\|\s*`?13A-DR-015`?\s*\|",
           subject="Colour + glyph + text non-reliance on hue alone", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-DR-015",), allow_fnd=("13A-FND-017", "13A-FND-031"),
           allow_reqs=("REQ-321",), allow_legacy=("DMP-164",), required_any=("13A-FND-031",),
           rationale="Independent NS accessibility standard (DMP-164/REQ-321) paired with bounded FND-017/031."),
    _claim("doc1:13A-DR-018", "doc1", r"^\|\s*`?13A-DR-018`?\s*\|",
           subject="Named error/empty/denied first-class states", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-DR-018",), allow_src=("13A-SRC-032",), allow_fnd=("13A-FND-032",),
           allow_dec=("D-194",),
           allow_legacy=("B-02", "B-03", "B-04", "B-05", "B-06", "B-07", "B-08", "B-09", "B-10", "B-11", "B-12"),
           required_any=("13A-FND-032",),
           rationale="Grounded in NS failure catalogues (B-02..B-12)/D-194 and bounded shell fallback observation FND-032/SRC-032."),
    _claim("doc1:13A-DR-021", "doc1", r"^\|\s*`?13A-DR-021`?\s*\|",
           subject="Explicit blocked cases on Alliance surfaces", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-DR-021",), allow_fnd=("13A-FND-010", "13A-FND-012"),
           allow_legacy=("ALL-161", "ALL-167", "ALL-168", "B-09", "B-10", "WAR-149"),
           required_any=("13A-FND-010", "13A-FND-012"),
           rationale="Cites graduated disclosure & cooldown evidence (FND-010/012) plus B-09/B-10 rules, never Discord BP-017."),

    # --- doc2: UI design principles & architecture ---
    _claim("doc2:13A-PR-02", "doc2", r"^\|\s*`?13A-PR-02`?\s*\|",
           subject="Legibility before density, density before decoration", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-PR-02",), allow_fnd=("13A-FND-003", "13A-FND-027"), allow_legacy=("DP-004",),
           required_any=("13A-FND-003", "13A-FND-027"),
           rationale="Density observation comes strictly from P&W profile/long-page findings FND-003 and FND-027 with DP-004."),
    _claim("doc2:13A-PR-04", "doc2", r"^\|\s*`?13A-PR-04`?\s*\|",
           subject="Explain, don't teach-around (in-context help)", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-PR-04",), allow_fnd=("13A-FND-029",), allow_dr=("13A-DR-010",),
           allow_legacy=("F-010",), required_any=("13A-DR-010",),
           rationale="Cites off-platform wiki spill finding FND-029, Stage-1 F-010, and in-product help recommendation DR-010."),
    _claim("doc2:13A-PR-05", "doc2", r"^\|\s*`?13A-PR-05`?\s*\|",
           subject="Transparency by rule, opacity by design (k=5 suppression)", classification="NS_RULE_SUPPORTED",
           self_ids=("13A-PR-05",), allow_dr=("13A-DR-006",), allow_dec=("D-027", "D-030"),
           allow_legacy=("B-12", "DP-004", "TR-021", "WAR-148", "WAR-149", "WAR-150"),
           required_any=("13A-DR-006",),
           rationale="Cites aggregate suppression gate recommendation DR-006, D-027/D-030, and disclosure boundaries."),
    _claim("doc2:13A-PR-09", "doc2", r"^\|\s*`?13A-PR-09`?\s*\|",
           subject="Confirmation-first with cooldown & failure disclosure", classification="NS_RULE_SUPPORTED",
           self_ids=("13A-PR-09",), allow_dr=("13A-DR-009", "13A-DR-018"), allow_legacy=("RRL-006",),
           required_any=("13A-DR-009", "13A-DR-018"),
           rationale="Cites control cooldown recommendation DR-009, error/denied state DR-018, and RRL-006."),
    _claim("doc2:13A-PR-10", "doc2", r"^\|\s*`?13A-PR-10`?\s*\|",
           subject="Disabled control explains itself before click", classification="BENCHMARK_SUPPORTED",
           self_ids=("13A-PR-10",), allow_bp=("13A-BP-028",), required_any=("13A-BP-028",),
           rationale="Matches CN show-unaffordable-with-reason benchmark pattern BP-028."),
    _claim("doc2:13A-PR-12", "doc2", r"^\|\s*`?13A-PR-12`?\s*\|",
           subject="Colour + glyph + text status redundancy", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-PR-12",), allow_fnd=("13A-FND-017", "13A-FND-031"),
           allow_dr=("13A-DR-015",), allow_reqs=("REQ-321",), allow_legacy=("DMP-164",),
           required_any=("13A-DR-015",),
           rationale="Independent NS accessibility law DR-015 / DMP-164 / REQ-321 paired with bounded FND-017/031."),
    _claim("doc2:tone-suppressed", "doc2", r"^-\s*`suppressed`\s*[—-]",
           subject="Suppressed alert/status tone for k=5 non-disclosure", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-006",), required_any=("13A-DR-006",),
           rationale="Maps strictly to aggregate disclosure/suppression recommendation DR-006."),
    _claim("doc2:shell-d201", "doc2", r"^\*\*The shell \(D-201\)\.\*\*",
           subject="Persistent application frame across all states", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_src=("13A-SRC-017",), allow_bp=("13A-BP-001",), allow_dec=("D-201",),
           required_any=("13A-BP-001", "13A-SRC-017"),
           rationale="Cites persistent-frame benchmark BP-001 / SRC-017 under D-201."),
    _claim("doc2:shell-rule-anchor-E", "doc2", r"^\|\s*E\.\s*Breadcrumb",
           subject="Breadcrumb and governing rule anchor", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-009", "13A-DR-010"), required_any=("13A-DR-009", "13A-DR-010"),
           rationale="Binds governing rule anchor to cooldown/rule naming DR-009 and in-product help DR-010."),
    _claim("doc2:shell-alert-bar-C", "doc2", r"^-\s*\*\*C\*\*\s+is presentation-tier",
           subject="Alert bar notification presentation tier", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-011",), allow_reqs=("REQ-731",), required_any=("13A-DR-011",),
           rationale="Notification presentation tiers without new channel (DR-011, REQ-731)."),
    _claim("doc2:shell-help-anchor", "doc2", r"^-\s*\*\*Help and support access",
           subject="In-context explanation and support entry points", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-009", "13A-DR-010"), allow_deps=("13A-PR-04",),
           allow_legacy=("B-12", "MOD-002", "MOD-013"),
           required_any=("13A-DR-009", "13A-DR-010"),
           rationale="Explains rule anchors via PR-04, DR-009, DR-010, and B-12 intake/appeal entry."),
    _claim("doc2:shell-admin-sep", "doc2", r"^-\s*\*\*Administration surfaces",
           subject="Separate role-gated admin shell", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-013",), allow_dec=("D-042",), allow_legacy=("DIP-121",),
           required_any=("13A-DR-013",),
           rationale="Separate administrative shell recommendation DR-013, D-042, and DIP-121 isolation."),
    _claim("doc2:shell-long-sessions", "doc2", r"^\*\*Why this supports long sessions:\*\*",
           subject="Digest + context panel + stable frame ergonomics", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_fnd=("13A-FND-026", "13A-FND-027"),
           allow_dr=("13A-DR-001", "13A-DR-005", "13A-DR-018"),
           required_any=("13A-FND-026", "13A-FND-027"),
           rationale="Answers logged-out/long-page findings FND-026/027 via DR-001, DR-005, and DR-018."),
    _claim("doc2:nav-inbox", "doc2", r"^-\s*\*\*Inbox/queue\*\*",
           subject="Destination-based inbox/queue navigation", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-001",), required_any=("13A-DR-001",),
           rationale="Maps strictly to Command Digest and Inbox recommendation DR-001."),
    _claim("doc2:state-empty-new", "doc2", r"^\|\s*\*\*Empty \(new nation\)\*\*\s*\|",
           subject="Empty new-nation real frame with zeroes", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_src=("13A-SRC-017",), allow_bp=("13A-BP-001",), allow_dec=("D-063",),
           allow_legacy=("NAT-016",), required_any=("13A-BP-001", "13A-SRC-017"),
           rationale="Real-frame zero-state grounded in BP-001, SRC-017, NAT-016, and standard start D-063."),
    _claim("doc2:state-blocked-rule", "doc2", r"^\|\s*\*\*Blocked-by-rule\*\*\s*\|",
           subject="Disabled control with inline rule reason", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-028",), allow_deps=("13A-PR-10",), required_any=("13A-BP-028",),
           rationale="Grounded in CN unaffordable-reason pattern BP-028 and PR-10."),
    _claim("doc2:boundary-no-discord", "doc2", r"^-\s*\*\*No chat, no Discord",
           subject="Rejection of off-platform real-time chat", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-017",), allow_dec=("D-133", "UD-049"),
           allow_legacy=("ALL-162", "ALL-163", "ALL-164", "ALL-165", "ALL-166", "ALL-167", "ALL-168", "B-09"),
           required_any=("13A-BP-017",),
           rationale="Rejects off-platform Discord dependency BP-017 per D-133, ALL-162..168, and preserved UD-049."),
    _claim("doc2:boundary-a11y-resp", "doc2", r"^-\s*\*\*Accessibility and responsive\*\*",
           subject="Architectural-level responsive and a11y boundaries", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_src=("13A-SRC-029", "13A-SRC-036"), allow_fnd=("13A-FND-031",),
           allow_dr=("13A-DR-012", "13A-DR-015"), required_any=("13A-DR-012", "13A-DR-015"),
           rationale="Mobile/colour-independence DR-012/015 bounded against FND-031, SRC-029, SRC-036."),

    # --- doc3: Master screen inventory ---
    _claim("doc3:rule-object-pages", "doc3", r"^3\.\s*\*\*Object pages vs task screens\.\*\*",
           subject="Object pages vs confirmation-first task screens", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-003", "13A-BP-019"), allow_dr=("13A-DR-005",),
           allow_deps=("13A-PR-09",), required_any=("13A-BP-003", "13A-BP-019", "13A-DR-005"),
           rationale="Sectioned profiles BP-003/019 + DR-005 paired with confirmation principle PR-09."),
    _claim("doc3:rule-admin-sep", "doc3", r"^4\.\s*\*\*Admin separation\.\*\*",
           subject="Admin family SCR-091..100 separation", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-013",), allow_deps=("SCR-091", "SCR-100"),
           allow_dec=("D-042",), allow_legacy=("DIP-121",), required_any=("13A-DR-013",),
           rationale="Admin screen range behind DR-013 / D-042 separate shell and DIP-121 isolation."),
    _claim("doc3:SCR-002", "doc3", r"^\|\s*`?SCR-002`?\s*\|",
           subject="Registration with multi-account warning", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-002",), allow_bp=("13A-BP-014",), allow_dec=("D-029", "D-032"),
           allow_legacy=("B-03",), required_any=("13A-BP-014",),
           rationale="Registration warning cites multi-account disclosure BP-014 + D-029/032 (B-03)."),
    _claim("doc3:SCR-008", "doc3", r"^\|\s*`?SCR-008`?\s*\|",
           subject="Onboarding guide inside real shell", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-008",), allow_src=("13A-SRC-017",), allow_bp=("13A-BP-001",), allow_dec=("D-040",),
           allow_legacy=("B-03", "ONB-009", "ONB-010", "ONB-011", "ONB-012", "ONB-013", "ONB-014", "ONB-015", "ONB-016", "ONB-017", "ONB-036", "ONB-038"),
           required_any=("13A-BP-001", "13A-SRC-017"),
           rationale="Uses real persistent shell lesson BP-001 / SRC-017 under D-040 and ONB rules."),
    _claim("doc3:SCR-014", "doc3", r"^\|\s*`?SCR-014`?\s*\|",
           subject="Inbox / pending actions queue", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-014",), allow_bp=("13A-BP-018",), allow_dr=("13A-DR-001",),
           allow_dec=("D-016", "D-030"), allow_legacy=("B-02",),
           required_any=("13A-DR-001", "13A-BP-018"),
           rationale="Digest+Inbox DR-001 contrasting with logged-out world catalogue BP-018."),
    _claim("doc3:SCR-017", "doc3", r"^\|\s*`?SCR-017`?\s*\|",
           subject="National Chronicle history browser", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-017",), allow_bp=("13A-BP-024",), allow_dr=("13A-DR-020",),
           allow_dec=("D-026",), allow_legacy=("B-11",),
           required_any=("13A-BP-024", "13A-DR-020"),
           rationale="Bounded history depth BP-024 + retention labelling DR-020 + D-026."),
    _claim("doc3:SCR-018", "doc3", r"^\|\s*`?SCR-018`?\s*\|",
           subject="Network View (mapless world surface)", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-018",), allow_bp=("13A-BP-006", "13A-BP-016"), allow_dr=("13A-DR-003",),
           allow_reqs=("REQ-041",), allow_legacy=("B-02", "B-08", "B-09", "DP-003", "FO-013"),
           required_any=("13A-BP-006", "13A-BP-016"),
           rationale="Treaty web BP-006, map rejection BP-016, Network View DR-003, FO-013, DP-003, REQ-041."),
    _claim("doc3:SCR-024", "doc3", r"^\|\s*`?SCR-024`?\s*\|",
           subject="Policy axes management cooldown", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-024",), allow_bp=("13A-BP-010",), allow_dr=("13A-DR-009",),
           allow_dec=("D-087",), allow_legacy=("B-06",),
           required_any=("13A-BP-010", "13A-DR-009"),
           rationale="Policy screen cooldown disclosure BP-010 / DR-009 / D-087."),
    _claim("doc3:SCR-029", "doc3", r"^\|\s*`?SCR-029`?\s*\|",
           subject="Treasury dashboard six-number display", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-029",), allow_bp=("13A-BP-026",),
           allow_legacy=("B-04", "ECN-176", "ECN-177", "ECN-178"), required_any=("13A-BP-026",),
           rationale="Treasury inline bars reference strictly BP-026 and ECN-176..178 (not UGC ads BP-022)."),
    _claim("doc3:SCR-056", "doc3", r"^\|\s*`?SCR-056`?\s*\|",
           subject="Alliance tax brackets & member assignment", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-056",), allow_src=("13A-SRC-021",), allow_dr=("13A-DR-022",),
           allow_legacy=("B-09",), required_any=("13A-SRC-021", "13A-DR-022"),
           rationale="Cites P&W Alliance tax analogy SRC-021 and B-09 tax/funding boundary DR-022."),
    _claim("doc3:SCR-062", "doc3", r"^\|\s*`?SCR-062`?\s*\|",
           subject="Conflicts ledger public war list", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-062",), allow_bp=("13A-BP-008",), allow_dr=("13A-DR-008",),
           allow_legacy=("B-10",), required_any=("13A-BP-008", "13A-DR-008"),
           rationale="Conflict ledger vs gated timeline BP-008 and War surface separation DR-008."),
    _claim("doc3:SCR-072", "doc3", r"^\|\s*`?SCR-072`?\s*\|",
           subject="Named standings lists", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-072",), allow_bp=("13A-BP-005", "13A-BP-020"), allow_dr=("13A-DR-007",),
           allow_legacy=("B-11", "WEP-324", "WEP-325"),
           required_any=("13A-BP-005", "13A-BP-020", "13A-DR-007"),
           rationale="Rankings BP-005, comparison limits BP-020, WEP-324/325, and named standings DR-007."),
    _claim("doc3:SCR-078", "doc3", r"^\|\s*`?SCR-078`?\s*\|",
           subject="World Guide & glossary help index", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-078",), allow_bp=("13A-BP-009",), allow_dr=("13A-DR-010",),
           allow_legacy=("DP-004", "F-010"), required_any=("13A-BP-009", "13A-DR-010"),
           rationale="Menu-mirrored help BP-009, F-010/DP-004, and in-product help layer DR-010."),
    _claim("doc3:SCR-088", "doc3", r"^\|\s*`?SCR-088`?\s*\|",
           subject="Change disclosures (changelog)", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("SCR-088",), allow_bp=("13A-BP-012",), allow_dr=("13A-DR-014",),
           allow_legacy=("B-02", "B-12", "TR-049"), required_any=("13A-BP-012", "13A-DR-014"),
           rationale="Public changelog BP-012, TR-049, and DR-014."),
    _claim("doc3:detail-008-009", "doc3", r"^\|\s*008[–-]009\s*\|",
           subject="Onboarding detail zero-state frame", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_src=("13A-SRC-017",), allow_bp=("13A-BP-001",), allow_dec=("D-040",),
           required_any=("13A-BP-001", "13A-SRC-017"),
           rationale="Matches real shell zero-state lesson BP-001 / SRC-017 under D-040."),
    _claim("doc3:detail-014", "doc3", r"^\|\s*014\s*\|",
           subject="Inbox detail digest spine", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-001",), allow_dec=("D-016", "D-030"),
           required_any=("13A-DR-001",),
           rationale="Matches Digest+Inbox DR-001."),
    _claim("doc3:detail-017", "doc3", r"^\|\s*017\s*\|",
           subject="Chronicle detail retention & browsability", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_fnd=("13A-FND-019",), allow_bp=("13A-BP-024",), allow_dr=("13A-DR-020",),
           allow_dec=("D-026",), required_any=("13A-DR-020", "13A-FND-019", "13A-BP-024"),
           rationale="Matches history depth FND-019 / BP-024 / DR-020 / D-026."),
    _claim("doc3:detail-018", "doc3", r"^\|\s*018\s*\|",
           subject="Network View detail mapless relational edges", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-006", "13A-BP-016"), allow_dr=("13A-DR-003",),
           allow_reqs=("REQ-041",), allow_dec=("D-030",), allow_legacy=("FO-013",),
           required_any=("13A-BP-006", "13A-BP-016"),
           rationale="Matches treaty web BP-006, map rejection BP-016, FO-013, DR-003."),
    _claim("doc3:detail-019", "doc3", r"^\|\s*019\s*\|",
           subject="Alerts & notification history presentation tiers", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_src=("13A-SRC-029",), allow_bp=("13A-BP-027",), allow_dr=("13A-DR-011",),
           allow_legacy=tuple(f"AN-{n:02d}" for n in range(1, 17)),
           required_any=("13A-DR-011",),
           rationale="Notification presentation tiers DR-011 informed by CN alert log BP-027 / SRC-029 and AN-01..16."),
    _claim("doc3:detail-024", "doc3", r"^\|\s*024\s*\|",
           subject="Policy axes detail cooldown control", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-010",), allow_dr=("13A-DR-009",), allow_dec=("D-087",),
           required_any=("13A-BP-010", "13A-DR-009"),
           rationale="Cooldown control pattern BP-010 / DR-009 / D-087."),
    _claim("doc3:detail-031", "doc3", r"^\|\s*031\s*\|",
           subject="Economic reports retention boundaries", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-024",), allow_dr=("13A-DR-020",), allow_legacy=("SEC-031",),
           required_any=("13A-BP-024", "13A-DR-020"),
           rationale="History bounds BP-024, SEC-031, and retention boundary labelling DR-020."),
    _claim("doc3:detail-033", "doc3", r"^\|\s*033\s*\|",
           subject="Warehouse balances inline bars", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-026",), allow_legacy=("MKT-053",), required_any=("13A-BP-026",),
           rationale="Inline bar chart pattern BP-026 and MKT-053 reservation triple."),
    _claim("doc3:detail-054", "doc3", r"^\|\s*054\s*\|",
           subject="Alliance membership & applicants (no Discord deflection)", classification="BENCHMARK_SUPPORTED",
           self_ids=(), allow_bp=("13A-BP-017",), allow_dec=("UD-040",), required_any=("13A-BP-017",),
           rationale="Addresses rejected off-platform Discord dependency BP-017 under preserved UD-040."),
    _claim("doc3:detail-056", "doc3", r"^\|\s*056\s*\|",
           subject="Alliance tax brackets detail", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_src=("13A-SRC-021",), allow_dr=("13A-DR-022",), allow_dec=("UD-040",),
           required_any=("13A-SRC-021", "13A-DR-022"),
           rationale="P&W tax analogy SRC-021 and B-09 boundary DR-022 under preserved UD-040."),
    _claim("doc3:detail-062", "doc3", r"^\|\s*062\s*\|",
           subject="Conflicts ledger detail split", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-008",), allow_dr=("13A-DR-008",), required_any=("13A-BP-008",),
           rationale="Conflict ledger vs gated timeline BP-008 / DR-008."),
    _claim("doc3:detail-078", "doc3", r"^\|\s*078\s*\|",
           subject="World Guide detail in-context glossary", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_fnd=("13A-FND-029",), allow_bp=("13A-BP-009",), allow_dr=("13A-DR-010",),
           allow_legacy=("DP-004", "F-010", "UXD-001"), required_any=("13A-BP-009", "13A-DR-010"),
           rationale="Menu-mirrored help BP-009, off-platform spill FND-029, F-010/DP-004/UXD-001, DR-010."),
    _claim("doc3:audit-confusing-bounds", "doc3", r"^\|\s*Confusing system boundaries\s*\|",
           subject="Navigation audit: confusing system boundaries mitigation", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-009", "13A-DR-010"), allow_deps=("13A-UR-044",),
           required_any=("13A-DR-009", "13A-DR-010", "13A-UR-044"),
           rationale="Mitigates boundary confusion with rule-naming DR-009, help DR-010, and UR-044."),

    # --- doc4: Responsive & design-system foundations ---
    _claim("doc4:benchmark-reading", "doc4", r"^P&W is a \*\*desktop-oriented genre reference\*\*",
           subject="Desktop-oriented P&W genre + CN mobile override evidence", classification="BENCHMARK_SUPPORTED",
           self_ids=(), allow_src=("13A-SRC-029", "13A-SRC-036"), allow_fnd=("13A-FND-003", "13A-FND-027"),
           allow_deps=("13A-OQ-014",), required_any=("13A-FND-003", "13A-FND-027"),
           rationale="Desktop density FND-003/027, mobile toggle note SRC-036, CN mobile mode SRC-029, OQ-014."),
    _claim("doc4:comp-data", "doc4", r"^Data:\s*\*\*table grammar\*\*",
           subject="Data component families (table grammar & inline bars)", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-004", "13A-BP-026"), allow_deps=("13A-PR-01", "13A-RD-04"),
           allow_legacy=("WAR-085", "WAR-086", "WAR-087", "WAR-088"), required_any=("13A-BP-026",),
           rationale="Table grammar BP-004, CN inline bars BP-026, WAR band meters, mobile card fallback RD-04, PR-01."),
    _claim("doc4:comp-actions", "doc4", r"^Actions:\s*button ladder",
           subject="Action component families (confirmations & cooldowns)", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-010",), allow_dr=("13A-DR-009",),
           allow_deps=("13A-PR-10", "OVL-01", "OVL-02", "OVL-03"), required_any=("13A-BP-010", "13A-DR-009"),
           rationale="Cooldown control BP-010/DR-009, confirmation/reason overlays OVL-01..03, PR-10."),
    _claim("doc4:viz-historical", "doc4", r"^\|\s*Historical trends\s*\|",
           subject="Info-viz historical retention disclosure", classification="NS_RULE_SUPPORTED",
           self_ids=(), allow_dr=("13A-DR-020",), required_any=("13A-DR-020",),
           rationale="Historical trend disclosure binds strictly to retention recommendation DR-020."),
    _claim("doc4:viz-comparisons", "doc4", r"^\|\s*Strategic comparisons\s*\|",
           subject="Info-viz strategic comparison gating & history", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=(), allow_bp=("13A-BP-020",), allow_dr=("13A-DR-006", "13A-DR-020"),
           required_any=("13A-DR-006", "13A-DR-020"),
           rationale="Single-metric limits BP-020, k=5 gate DR-006, slot/retention boundary DR-020."),
    _claim("doc4:13A-DS-07", "doc4", r"^\|\s*`?13A-DS-07`?\s*\|",
           subject="Keyboard operability and focus management", classification="INDEPENDENT_ACCESSIBILITY_REQUIREMENT",
           self_ids=("13A-DS-07",), allow_deps=("13A-PR-14",), allow_reqs=("REQ-321",),
           allow_legacy=("DMP-164",),
           required_markers=("INDEPENDENT_ACCESSIBILITY_REQUIREMENT",),
           rationale="Independent NS accessibility requirement (PR-14, DMP-164/REQ-321, WCAG 2.2 AA design intent); P&W research findings excluded."),
    _claim("doc4:13A-DS-10", "doc4", r"^\|\s*`?13A-DS-10`?\s*\|",
           subject="Colour-independence (colour + glyph + text)", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-DS-10",), allow_fnd=("13A-FND-017", "13A-FND-031"), allow_dr=("13A-DR-015",),
           allow_deps=("13A-PR-12",), allow_reqs=("REQ-321",), allow_legacy=("DMP-164",),
           required_any=("13A-DR-015", "13A-FND-031"),
           rationale="NS rule DR-015 / PR-12 / DMP-164 / REQ-321 bounded against P&W table column observations FND-017/031."),

    # --- doc5: UI requirements register (both §2.1 & §2.2 enforced) ---
    _claim("doc5:UR-003", "doc5", r"^\|\s*UR-003\s*\|",
           subject="Post-absence Command Digest landing", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-003",), allow_fnd=("13A-FND-026",), allow_bp=("13A-BP-018",), allow_dr=("13A-DR-001",),
           allow_reqs=("REQ-022",), allow_dec=("D-016", "D-030"), required_any=("13A-DR-001", "13A-BP-018"),
           rationale="Digest+Inbox DR-001 contrasted with bounded logged-out world catalogue BP-018/FND-026."),
    _claim("doc5:UR-004", "doc5", r"^\|\s*UR-004\s*\|",
           subject="Inbox actionable pending queue", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-004",), allow_bp=("13A-BP-018",), allow_dr=("13A-DR-001",),
           allow_reqs=("REQ-022",), allow_legacy=("B-02", "SYS-017", "TR-089"),
           required_any=("13A-DR-001", "13A-BP-018"),
           rationale="Digest-first TR-089/SYS-017/DR-001 contrasting with BP-018 under REQ-022."),
    _claim("doc5:UR-005", "doc5", r"^\|\s*UR-005\s*\|",
           subject="Six number types distinguish state/forecast/history", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-005",), allow_bp=("13A-BP-026",), allow_deps=("13A-PR-03",),
           allow_reqs=("REQ-250",), allow_legacy=("B-04", "B-05", "ECN-177", "ECN-178", "URB-152"),
           required_any=("13A-PR-03", "13A-BP-026"),
           rationale="Six number types PR-03/ECN-177/178/URB-152 paired with CN inline bars BP-026."),
    _claim("doc5:UR-007", "doc5", r"^\|\s*UR-007\s*\|",
           subject="Disabled actions state governing reason & cooldown", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-007",), allow_bp=("13A-BP-028",), allow_dr=("13A-DR-009",),
           allow_reqs=("REQ-257",), allow_legacy=("ECN-181",), required_any=("13A-BP-028", "13A-DR-009"),
           rationale="Show-unaffordable BP-028, ECN-181, and control cooldown DR-009."),
    _claim("doc5:UR-008", "doc5", r"^\|\s*UR-008\s*\|",
           subject="Confirmation modals show cost, cooldown, consequence", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-008",), allow_bp=("13A-BP-010",), allow_dr=("13A-DR-009",),
           allow_deps=("13A-PR-09",), allow_legacy=("B-13", "RRL-006"),
           required_any=("13A-PR-09", "13A-BP-010"),
           rationale="Confirmation principle PR-09, RRL-006, and cooldown patterns BP-010/DR-009."),
    _claim("doc5:UR-009", "doc5", r"^\|\s*UR-009\s*\|",
           subject="Colour + glyph + text non-reliance on hue alone", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-009",), allow_fnd=("13A-FND-017", "13A-FND-031"), allow_dr=("13A-DR-015",),
           allow_deps=("13A-DS-10", "13A-PR-12"), allow_reqs=("REQ-321",), allow_dec=("D-203",),
           allow_legacy=("DMP-164",), required_any=("13A-DR-015", "13A-FND-031"),
           rationale="Colour-independence DR-015/PR-12/DS-10/D-203/DMP-164/REQ-321 with bounded FND-017/031."),
    _claim("doc5:UR-010", "doc5", r"^\|\s*UR-010\s*\|",
           subject="Keyboard-operable action paths with visible focus", classification="INDEPENDENT_ACCESSIBILITY_REQUIREMENT",
           self_ids=("13A-UR-010",), allow_deps=("13A-DS-07", "13A-PR-14"), allow_reqs=("REQ-321",),
           allow_legacy=("DMP-164",),
           required_markers=("INDEPENDENT_ACCESSIBILITY_REQUIREMENT",),
           rationale="Independent NS accessibility requirement anchored on DS-07/PR-14/DMP-164/REQ-321; P&W research excluded."),
    _claim("doc5:UR-012", "doc5", r"^\|\s*UR-012\s*\|",
           subject="k=5 aggregate suppression notice", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-012",), allow_bp=("13A-BP-007",), allow_dr=("13A-DR-006",), allow_dec=("D-027",),
           allow_legacy=("B-07", "B-08", "B-10", "B-11", "MKT-110", "TR-022", "WEP-663"),
           required_any=("13A-DR-006", "13A-BP-007"),
           rationale="Aggregate gate BP-007, suppression notice DR-006, D-027, TR-022, WEP-663, MKT-110."),
    _claim("doc5:UR-013", "doc5", r"^\|\s*UR-013\s*\|",
           subject="Graduated visibility & permission denial without leaks", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-013",), allow_fnd=("13A-FND-010", "13A-FND-025"), allow_dr=("13A-DR-016",),
           allow_reqs=("REQ-590", "REQ-670"), allow_legacy=("PRV-009", "PRV-014", "PRV-019", "TR-021"),
           required_any=("13A-FND-010", "13A-FND-025", "13A-DR-016"),
           rationale="Graduated disclosure FND-010/025, TR-021/PRV rules, and server-decided denial DR-016."),
    _claim("doc5:UR-014", "doc5", r"^\|\s*UR-014\s*\|",
           subject="Mapless relational Network View", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-014",), allow_bp=("13A-BP-006", "13A-BP-016"), allow_dr=("13A-DR-003",),
           allow_reqs=("REQ-041",), allow_legacy=("B-02", "B-08", "FO-013"),
           required_any=("13A-BP-006", "13A-BP-016", "13A-DR-003"),
           rationale="Treaty web BP-006, map rejection BP-016, Network View DR-003, FO-013, REQ-041."),
    _claim("doc5:UR-015", "doc5", r"^\|\s*UR-015\s*\|",
           subject="Alliance surface omits member military ops / readiness", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-015",), allow_fnd=("13A-FND-010",), allow_bp=("13A-BP-008",), allow_dr=("13A-DR-008",),
           allow_reqs=("REQ-589", "REQ-590", "REQ-591"), allow_dec=("UD-047", "UD-049"),
           allow_legacy=("AX-18", "B-09", "B-10", "WAR-148"),
           required_any=("13A-BP-008", "13A-DR-008"),
           rationale="Public/alliance/owner war separation AX-18/WAR-148/BP-008/DR-008 with FND-010 gating."),
    _claim("doc5:UR-016", "doc5", r"^\|\s*UR-016\s*\|",
           subject="Alliance tax & ARL surface bounded to B-09 rules", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-016",), allow_src=("13A-SRC-021",), allow_dr=("13A-DR-022",),
           allow_reqs=("REQ-614", "REQ-615", "REQ-616", "REQ-617"),
           allow_dec=("UD-040", "UD-045", "UD-046"), allow_legacy=("B-09",),
           required_any=("13A-SRC-021", "13A-DR-022"),
           rationale="Tax analogy SRC-021 and B-09 rule boundary DR-022 under preserved UDs."),
    _claim("doc5:UR-017", "doc5", r"^\|\s*UR-017\s*\|",
           subject="Explicit Alliance treaty NAP/attack-block disclosure", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-017",), allow_fnd=("13A-FND-029",), allow_bp=("13A-BP-017",), allow_dr=("13A-DR-021",),
           allow_dec=("D-133",),
           allow_legacy=("ALL-161", "ALL-162", "ALL-163", "ALL-164", "ALL-165", "ALL-166", "ALL-167", "ALL-168", "B-09", "WAR-149"),
           required_any=("13A-BP-017", "13A-DR-021"),
           rationale="Rejects Discord deflection BP-017/FND-029 and mandates explicit blocked-case UI DR-021."),
    _claim("doc5:UR-019", "doc5", r"^\|\s*UR-019\s*\|",
           subject="Owner-only War Operations Board separation", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-019",), allow_bp=("13A-BP-008",), allow_dr=("13A-DR-008",),
           allow_reqs=("REQ-687",), allow_legacy=("B-10", "WAR-085", "WAR-086", "WAR-087", "WAR-088"),
           required_any=("13A-BP-008", "13A-DR-008"),
           rationale="War surface split and WAR-085..088 bands via BP-008 and DR-008."),
    _claim("doc5:UR-020", "doc5", r"^\|\s*UR-020\s*\|",
           subject="Standings declare denominator, window, no live rank", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-020",), allow_bp=("13A-BP-005", "13A-BP-020"), allow_dr=("13A-DR-007",),
           allow_reqs=("REQ-728",), allow_legacy=("B-11", "WEP-324", "WEP-325"),
           required_any=("13A-BP-005", "13A-BP-020", "13A-DR-007"),
           rationale="Standings BP-005, single-metric limit BP-020, WEP-324/325, named standings DR-007."),
    _claim("doc5:UR-021", "doc5", r"^\|\s*UR-021\s*\|",
           subject="New nation lands in real persistent shell", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-021",), allow_src=("13A-SRC-017",), allow_fnd=("13A-FND-002",), allow_bp=("13A-BP-001",),
           allow_reqs=("REQ-089", "REQ-090"), allow_dec=("D-039", "D-040"),
           allow_legacy=("B-03", "NAT-016"), required_any=("13A-SRC-017", "13A-BP-001"),
           rationale="Real-frame zero-state SRC-017, FND-002, BP-001, NAT-016, D-039/040."),
    _claim("doc5:UR-024", "doc5", r"^\|\s*UR-024\s*\|",
           subject="Multi-account warning at registration", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-024",), allow_src=("13A-SRC-018",), allow_bp=("13A-BP-014",),
           allow_reqs=("REQ-070", "REQ-075", "REQ-865"), allow_dec=("D-034",),
           allow_legacy=("B-03", "B-12", "EVD-009", "NET-023", "NET-050"),
           required_any=("13A-BP-014", "13A-SRC-018"),
           rationale="Registration warning BP-014 / SRC-018 and NET-023/050/EVD-009 disclosures."),
    _claim("doc5:UR-028", "doc5", r"^\|\s*UR-028\s*\|",
           subject="Admin screens inhabit separate role-gated shell", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-028",), allow_fnd=("13A-FND-010",), allow_dr=("13A-DR-013",),
           allow_reqs=("REQ-865",), allow_dec=("D-042",),
           allow_legacy=("ADM-021", "ADM-022", "B-12"),
           required_any=("13A-DR-013", "13A-FND-010"),
           rationale="Admin separation DR-013, ADM-021/022, and role-graduated access FND-010 / D-042."),
    _claim("doc5:UR-029", "doc5", r"^\|\s*UR-029\s*\|",
           subject="Notification presentation tiers over existing events", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-029",), allow_bp=("13A-BP-027",), allow_dr=("13A-DR-011",),
           allow_reqs=("REQ-731",),
           allow_legacy=tuple(f"AN-{n:02d}" for n in range(1, 17)),
           required_any=("13A-DR-011", "13A-BP-027"),
           rationale="Notification presentation tiers DR-011 informed by CN alert log BP-027 and AN-01..16."),
    _claim("doc5:UR-033", "doc5", r"^\|\s*UR-033\s*\|",
           subject="Stable deep-link URLs for all game objects", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-033",), allow_fnd=("13A-FND-001",), allow_dr=("13A-DR-017",),
           allow_deps=("13A-PR-09", "13A-PR-13"), required_any=("13A-FND-001", "13A-DR-017"),
           rationale="Addressability FND-001 and deep-link recommendation DR-017."),
    _claim("doc5:UR-035", "doc5", r"^\|\s*UR-035\s*\|",
           subject="Named empty/error/denied/suppressed states", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-035",), allow_fnd=("13A-FND-032",), allow_bp=("13A-BP-021",),
           allow_dr=("13A-DR-006", "13A-DR-018"), required_any=("13A-BP-021", "13A-DR-018"),
           rationale="Shell-fallback replacement BP-021/FND-032, explicit states DR-018, suppression DR-006."),
    _claim("doc5:UR-036", "doc5", r"^\|\s*UR-036\s*\|",
           subject="Actionable recovery and failure codes", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-036",), allow_fnd=("13A-FND-032",), allow_dr=("13A-DR-018",),
           allow_dec=("D-143",), allow_legacy=("TR-075", "TR-080"), required_any=("13A-DR-018",),
           rationale="Explicit failure/denied states DR-018, D-143, TR-075/080 contrasting bounded FND-032."),
    _claim("doc5:UR-039", "doc5", r"^\|\s*UR-039\s*\|",
           subject="Archive/chronicle views state retention bounds", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-039",), allow_fnd=("13A-FND-019",), allow_bp=("13A-BP-024",), allow_dr=("13A-DR-020",),
           allow_dec=("D-026",), required_any=("13A-BP-024", "13A-DR-020"),
           rationale="Bounded history depth BP-024/FND-019 and retention labelling DR-020."),
    _claim("doc5:UR-040", "doc5", r"^\|\s*UR-040\s*\|",
           subject="Rule/event cause chains surfaced on Digest & help", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-040",), allow_fnd=("13A-FND-034",), allow_dr=("13A-DR-001", "13A-DR-010"),
           allow_deps=("13A-PR-04", "13A-PR-06"), allow_legacy=("B-02", "B-04", "B-06", "DMP-073", "ECV-001"),
           required_any=("13A-FND-034", "13A-DR-001", "13A-DR-010"),
           rationale="Cause-effect FND-034, ECV-001/DMP-073 lineage, Digest DR-001, help DR-010."),
    _claim("doc5:UR-042", "doc5", r"^\|\s*UR-042\s*\|",
           subject="Responsive core layout with optional mode toggle question", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-042",), allow_src=("13A-SRC-029", "13A-SRC-036"), allow_deps=("13A-RD-06",),
           required_any=("13A-SRC-029", "13A-SRC-036"),
           rationale="CN mobile mode SRC-029, P&W toggle note SRC-036, provisional breakpoints RD-06."),
    _claim("doc5:UR-044", "doc5", r"^\|\s*UR-044\s*\|",
           subject="Every screen links governing rule/help entry", classification="NS_RULE_SUPPORTED",
           self_ids=("13A-UR-044",), allow_bp=("13A-BP-009",), allow_dr=("13A-DR-009", "13A-DR-010"),
           allow_legacy=("B-02", "B-03", "B-04", "B-05", "B-06", "B-07", "B-08", "B-09", "B-10", "B-11", "B-12"),
           required_any=("13A-DR-009", "13A-DR-010"),
           rationale="Matches menu-mirrored help BP-009, rule naming DR-009, help DR-010 across B-02..B-12."),
    _claim("doc5:UR-046", "doc5", r"^\|\s*UR-046\s*\|",
           subject="No dark patterns, streaks, or FOMO timers", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("13A-UR-046",), allow_fnd=("13A-FND-027",), allow_bp=("13A-BP-019",),
           allow_dr=("13A-DR-005", "13A-DR-019"), allow_deps=("13A-PR-14",),
           allow_legacy=("AP-001", "DP-002"),
           required_any=("13A-FND-027", "13A-BP-019", "13A-DR-019"),
           rationale="Anti-FOMO/session-safety DR-019/AP-001/DP-002 paired with anti-overload BP-019/DR-005/FND-027."),

    # --- DECISIONS.md D-201..D-203 ---
    _claim("decisions:D-201", "decisions", r"^\|\s*D-201\s*\|",
           subject="Global shell, eight-section nav, admin separation", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("D-201",), allow_src=("13A-SRC-017", "13A-SRC-032"),
           allow_fnd=("13A-FND-023", "13A-FND-026", "13A-FND-027"),
           allow_bp=("13A-BP-001", "13A-BP-002", "13A-BP-003", "13A-BP-018"),
           allow_reqs=("REQ-022",), allow_dec=("D-042",), allow_legacy=("DP-002", "TR-089"),
           required_any=("13A-FND-026", "13A-FND-027", "13A-BP-018"),
           rationale="Shell & navigation architecture position supported by bounded FND-023/026/027, TR-089/DP-002/REQ-022, and BP-001..003/018."),
    _claim("decisions:D-202", "decisions", r"^\|\s*D-202\s*\|",
           subject="Responsive strategy & mobile-mode open question", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("D-202",), allow_src=("13A-SRC-029", "13A-SRC-036"), allow_deps=("13A-OQ-014",),
           allow_dec=(), required_any=("13A-SRC-029", "13A-SRC-036"),
           rationale="Mobile evidence rests on CN mode SRC-029 and bounded P&W toggle note SRC-036, not non-existent SRC-035."),
    _claim("decisions:D-203", "decisions", r"^\|\s*D-203\s*\|",
           subject="Design system tokens & colour-independence position", classification="HYBRID_BENCHMARK_AND_NS_RULE",
           self_ids=("D-203",), allow_fnd=("13A-FND-017", "13A-FND-031"), allow_dr=("13A-DR-015",),
           allow_deps=("13A-OQ-001", "13A-OQ-002", "13A-OQ-013"), allow_reqs=("REQ-321",),
           allow_legacy=("DMP-164",),
           required_any=("13A-FND-017", "13A-FND-031", "13A-DR-015"),
           rationale="Token system + independent colour-plus-glyph rule DR-015/DMP-164/REQ-321 bounded against FND-017/031."),
] + _table_claims((
    # --- Remaining doc1 FND/BP/DR register rows ---
    ("doc1:13A-FND-001", "doc1", "13A-FND-001", ("13A-SRC-003",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-002", "doc1", "13A-FND-002", ("13A-SRC-009", "13A-SRC-017"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-004", "doc1", "13A-FND-004", ("13A-SRC-002", "13A-SRC-005", "13A-SRC-008", "13A-SRC-011", "13A-SRC-012"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-005", "doc1", "13A-FND-005", ("13A-SRC-007",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-006", "doc1", "13A-FND-006", ("13A-SRC-008", "13A-SRC-009"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-007", "doc1", "13A-FND-007", ("13A-SRC-010",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-008", "doc1", "13A-FND-008", ("13A-SRC-013", "13A-SRC-016"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-009", "doc1", "13A-FND-009", ("13A-SRC-003", "13A-SRC-006"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-010", "doc1", "13A-FND-010", ("13A-SRC-006",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-011", "doc1", "13A-FND-011", ("13A-SRC-021",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-012", "doc1", "13A-FND-012", ("13A-SRC-022",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-014", "doc1", "13A-FND-014", ("13A-SRC-019",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-015", "doc1", "13A-FND-015", ("13A-SRC-003", "13A-SRC-028"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-016", "doc1", "13A-FND-016", ("13A-SRC-018", "13A-SRC-032"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-018", "doc1", "13A-FND-018", ("13A-SRC-007", "13A-SRC-016"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-019", "doc1", "13A-FND-019", ("13A-SRC-002", "13A-SRC-004", "13A-SRC-012"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-020", "doc1", "13A-FND-020", ("13A-SRC-015",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-021", "doc1", "13A-FND-021", ("13A-SRC-009", "13A-SRC-017"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-022", "doc1", "13A-FND-022", ("13A-SRC-014",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-023", "doc1", "13A-FND-023", ("13A-SRC-003", "13A-SRC-017"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-024", "doc1", "13A-FND-024", tuple(f"13A-SRC-{n:03d}" for n in range(2, 13)), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-025", "doc1", "13A-FND-025", ("13A-SRC-004", "13A-SRC-006", "13A-SRC-009"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-029", "doc1", "13A-FND-029", ("13A-SRC-006", "13A-SRC-027"), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-030", "doc1", "13A-FND-030", ("13A-SRC-016",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-033", "doc1", "13A-FND-033", ("13A-SRC-020",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-034", "doc1", "13A-FND-034", ("13A-SRC-013",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-035", "doc1", "13A-FND-035", ("13A-SRC-004",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-036", "doc1", "13A-FND-036", ("13A-SRC-010",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-037", "doc1", "13A-FND-037", ("13A-SRC-014",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-038", "doc1", "13A-FND-038", ("13A-SRC-023",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-039", "doc1", "13A-FND-039", ("13A-SRC-028",), (), (), (), (), (), (), ()),
    ("doc1:13A-FND-040", "doc1", "13A-FND-040", ("13A-SRC-001", "13A-SRC-017"), (), (), (), (), (), (), ()),
    ("doc1:13A-BP-001", "doc1", "13A-BP-001", ("13A-SRC-017",), (), (), (), (), (), ("D-027",), ()),
    ("doc1:13A-BP-002", "doc1", "13A-BP-002", (), ("13A-FND-001",), (), (), (), (), (), ()),
    ("doc1:13A-BP-003", "doc1", "13A-BP-003", ("13A-SRC-004",), (), (), (), (), (), (), ()),
    ("doc1:13A-BP-004", "doc1", "13A-BP-004", (), ("13A-FND-004",), (), (), (), (), (), ()),
    ("doc1:13A-BP-005", "doc1", "13A-BP-005", ("13A-SRC-007",), (), (), (), (), (), (), ("WEP-324", "WEP-325")),
    ("doc1:13A-BP-006", "doc1", "13A-BP-006", ("13A-SRC-010",), (), (), (), (), (), (), ("DP-003", "FO-013", "SIM-012")),
    ("doc1:13A-BP-007", "doc1", "13A-BP-007", ("13A-SRC-013", "13A-SRC-015"), (), (), (), (), (), ("D-027",), ("TR-022",)),
    ("doc1:13A-BP-008", "doc1", "13A-BP-008", (), ("13A-FND-006", "13A-FND-025"), (), (), (), (), (), ("B-10", "WAR-085", "WAR-086", "WAR-087", "WAR-088", "WAR-148")),
    ("doc1:13A-BP-009", "doc1", "13A-BP-009", (), ("13A-FND-011", "13A-FND-033"), (), (), (), (), (), ("B-13",)),
    ("doc1:13A-BP-010", "doc1", "13A-BP-010", ("13A-SRC-022",), (), (), (), (), ("REQ-257",), ("D-087",), ()),
    ("doc1:13A-BP-011", "doc1", "13A-BP-011", (), ("13A-FND-038",), (), (), (), (), (), ("B-12",)),
    ("doc1:13A-BP-012", "doc1", "13A-BP-012", ("13A-SRC-019",), (), (), (), (), (), (), ("B-12", "MOD-017", "TR-049")),
    ("doc1:13A-BP-013", "doc1", "13A-BP-013", ("13A-SRC-028",), (), (), (), (), (), (), ()),
    ("doc1:13A-BP-014", "doc1", "13A-BP-014", ("13A-SRC-018",), (), (), (), (), (), ("D-018",), ("B-03",)),
    ("doc1:13A-BP-015", "doc1", "13A-BP-015", (), ("13A-FND-017", "13A-FND-031"), (), ("13A-DR-015",), (), ("REQ-321",), (), ("DMP-164",)),
    ("doc1:13A-BP-016", "doc1", "13A-BP-016", ("13A-SRC-016",), (), (), (), (), (), (), ("AP-002",)),
    ("doc1:13A-BP-017", "doc1", "13A-BP-017", (), ("13A-FND-029",), (), (), (), (), ("D-133",), ("ALL-161", "B-09")),
    ("doc1:13A-BP-018", "doc1", "13A-BP-018", ("13A-SRC-032",), ("13A-FND-026",), (), ("13A-DR-001",), (), ("REQ-022",), (), ("DP-002", "TR-089")),
    ("doc1:13A-BP-019", "doc1", "13A-BP-019", (), ("13A-FND-027",), (), (), (), (), (), ()),
    ("doc1:13A-BP-020", "doc1", "13A-BP-020", (), ("13A-FND-028",), (), (), ("SCR-077",), (), (), ("B-11",)),
    ("doc1:13A-BP-021", "doc1", "13A-BP-021", ("13A-SRC-032",), ("13A-FND-032",), (), (), (), ("REQ-821",), ("D-194",), ()),
    ("doc1:13A-BP-022", "doc1", "13A-BP-022", ("13A-SRC-014",), (), (), (), (), (), (), ()),
    ("doc1:13A-BP-023", "doc1", "13A-BP-023", (), ("13A-FND-021",), (), (), (), (), (), ()),
    ("doc1:13A-BP-024", "doc1", "13A-BP-024", ("13A-SRC-004", "13A-SRC-019"), (), (), (), (), (), ("D-026",), ("B-11",)),
    ("doc1:13A-BP-025", "doc1", "13A-BP-025", ("13A-SRC-029",), (), (), (), (), (), (), ()),
    ("doc1:13A-BP-026", "doc1", "13A-BP-026", ("13A-SRC-029",), (), (), (), (), (), (), ()),
    ("doc1:13A-BP-027", "doc1", "13A-BP-027", ("13A-SRC-029",), (), (), (), (), ("REQ-731",), (), ()),
    ("doc1:13A-BP-028", "doc1", "13A-BP-028", ("13A-SRC-029",), (), (), (), (), (), (), ("ECN-181", "URB-152")),
    ("doc1:13A-DR-002", "doc1", "13A-DR-002", (), ("13A-FND-002",), (), (), (), (), ("D-027",), ("B-02",)),
    ("doc1:13A-DR-003", "doc1", "13A-DR-003", (), (), ("13A-BP-006", "13A-BP-016"), (), (), (), (), ("DP-003", "FO-013")),
    ("doc1:13A-DR-004", "doc1", "13A-DR-004", (), ("13A-FND-004",), (), (), ("13A-PR-07",), (), (), ()),
    ("doc1:13A-DR-005", "doc1", "13A-DR-005", ("13A-SRC-004",), ("13A-FND-027",), (), (), (), (), (), ()),
    ("doc1:13A-DR-006", "doc1", "13A-DR-006", (), ("13A-FND-034",), (), (), (), (), ("D-027",), ("TR-022", "WEP-663")),
    ("doc1:13A-DR-007", "doc1", "13A-DR-007", (), (), ("13A-BP-005",), (), (), (), (), ("B-11", "WEP-324", "WEP-325", "WEP-361", "WEP-362")),
    ("doc1:13A-DR-008", "doc1", "13A-DR-008", (), ("13A-FND-006",), (), (), (), (), (), ("B-10", "WAR-085", "WAR-086", "WAR-087", "WAR-088", "WAR-148", "WAR-149", "WAR-150")),
    ("doc1:13A-DR-009", "doc1", "13A-DR-009", ("13A-SRC-022",), (), (), (), (), ("REQ-257",), ("D-087",), ()),
    ("doc1:13A-DR-010", "doc1", "13A-DR-010", (), ("13A-FND-029", "13A-FND-033"), (), (), (), (), (), ("DP-004", "F-010", "SYS-018")),
    ("doc1:13A-DR-011", "doc1", "13A-DR-011", (), (), ("13A-BP-027",), (), (), ("REQ-731",), (), ()),
    ("doc1:13A-DR-012", "doc1", "13A-DR-012", ("13A-SRC-029",), (), (), (), (), (), (), ()),
    ("doc1:13A-DR-013", "doc1", "13A-DR-013", (), ("13A-FND-010",), (), (), (), (), ("D-042",), ()),
    ("doc1:13A-DR-014", "doc1", "13A-DR-014", (), ("13A-FND-014",), (), (), (), (), (), ("B-13", "MOD-017", "TR-049")),
    ("doc1:13A-DR-016", "doc1", "13A-DR-016", (), ("13A-FND-010",), (), (), (), ("REQ-553", "REQ-645"), (), ()),
    ("doc1:13A-DR-017", "doc1", "13A-DR-017", (), ("13A-FND-001",), (), (), (), (), (), ()),
    ("doc1:13A-DR-019", "doc1", "13A-DR-019", (), (), (), (), (), (), ("D-021",), ("AP-001", "DP-002")),
    ("doc1:13A-DR-020", "doc1", "13A-DR-020", (), ("13A-FND-019",), (), (), (), (), ("D-026",), ()),
    ("doc1:13A-DR-022", "doc1", "13A-DR-022", ("13A-SRC-021",), (), (), (), (), (), ("D-140", "D-141", "UD-045", "UD-046"), ("B-09",)),
    ("doc1:13A-DR-023", "doc1", "13A-DR-023", (), ("13A-FND-039",), (), (), (), (), (), ()),
    ("doc1:13A-DR-024", "doc1", "13A-DR-024", (), (), (), (), (), (), ("D-199",), ()),
    # --- Remaining doc2 PR rows ---
    ("doc2:13A-PR-01", "doc2", "13A-PR-01", (), (), (), (), (), (), (), ("AP-001", "DP-002")),
    ("doc2:13A-PR-03", "doc2", "13A-PR-03", (), (), (), (), (), (), ("D-056",), ("DIP-155", "ECN-177", "URB-152")),
    ("doc2:13A-PR-06", "doc2", "13A-PR-06", (), (), (), (), (), ("REQ-022",), (), ("F-015", "F-016", "TR-089")),
    ("doc2:13A-PR-07", "doc2", "13A-PR-07", (), ("13A-FND-024",), ("13A-BP-004",), (), (), (), (), ()),
    ("doc2:13A-PR-08", "doc2", "13A-PR-08", (), (), (), (), (), (), (), ("CX-5", "DP-001")),
    ("doc2:13A-PR-11", "doc2", "13A-PR-11", (), (), (), (), (), (), (), ("URB-135",)),
    ("doc2:13A-PR-13", "doc2", "13A-PR-13", (), ("13A-FND-001", "13A-FND-023"), (), (), (), (), (), ()),
    ("doc2:13A-PR-14", "doc2", "13A-PR-14", (), (), (), (), (), (), (), ()),
    ("doc2:13A-PR-15", "doc2", "13A-PR-15", (), (), (), (), (), (), (), ()),
    ("doc2:13A-PR-16", "doc2", "13A-PR-16", (), (), (), (), (), (), ("D-194",), ("MKT-110",)),
    # --- Remaining doc3 SCR and OVL rows ---
    ("doc3:SCR-001", "doc3", "SCR-001", ("13A-SRC-001",), (), (), (), (), (), ("D-007",), ("B-03",)),
    ("doc3:SCR-003", "doc3", "SCR-003", ("13A-SRC-017",), (), (), (), (), (), (), ("ACC-018", "B-03")),
    ("doc3:SCR-004", "doc3", "SCR-004", ("13A-SRC-017",), (), (), (), (), (), ("D-041",), ("B-03",)),
    ("doc3:SCR-005", "doc3", "SCR-005", (), (), (), (), (), (), ("D-041",), ("B-03",)),
    ("doc3:SCR-006", "doc3", "SCR-006", (), (), (), (), (), (), ("D-029",), ("B-03",)),
    ("doc3:SCR-007", "doc3", "SCR-007", (), (), (), (), (), (), ("D-038", "D-063"), ("B-03", "B-04", "NAT-015", "NAT-016")),
    ("doc3:SCR-009", "doc3", "SCR-009", (), (), (), (), (), (), (), ("B-03", "B-11")),
    ("doc3:SCR-010", "doc3", "SCR-010", (), ("13A-FND-003",), (), (), (), (), (), ("B-03", "B-06", "B-10", "B-11", "NAT-015", "RRL-020", "TR-021")),
    ("doc3:SCR-011", "doc3", "SCR-011", (), (), (), (), (), (), ("D-041",), ("B-03",)),
    ("doc3:SCR-012", "doc3", "SCR-012", (), (), (), (), (), (), ("D-026", "D-041"), ("B-03",)),
    ("doc3:SCR-013", "doc3", "SCR-013", (), (), (), (), (), ("REQ-022",), (), ("B-02", "SYS-017", "TR-089")),
    ("doc3:SCR-015", "doc3", "SCR-015", (), (), (), (), (), (), (), ("B-04", "B-05", "B-06", "B-10", "DMP-073", "ECN-176", "URB-052")),
    ("doc3:SCR-016", "doc3", "SCR-016", (), (), (), (), (), (), (), ("B-02", "TR-049", "TR-075", "TR-080")),
    ("doc3:SCR-019", "doc3", "SCR-019", (), (), (), (), (), ("REQ-731",), (), tuple(f"AN-{n:02d}" for n in range(1, 17)) + ("B-02", "B-11")),
    ("doc3:SCR-020", "doc3", "SCR-020", (), (), (), (), ("13A-OQ-012",), (), (), ()),
    ("doc3:SCR-021", "doc3", "SCR-021", (), (), (), (), (), (), (), ("B-06", "DMP-256", "DMP-268")),
    ("doc3:SCR-022", "doc3", "SCR-022", (), (), (), (), (), (), ("D-084", "D-085"), ("B-06", "DMP-079", "DMP-080", "DMP-081", "DMP-082", "DMP-083")),
    ("doc3:SCR-023", "doc3", "SCR-023", (), (), (), (), (), (), (), ("B-06", "DMP-073", "F-PD-004", "F-PD-005", "F-PD-006", "F-PD-007", "F-PD-008", "F-PD-009")),
    ("doc3:SCR-025", "doc3", "SCR-025", (), (), (), (), (), (), (), ("B-06", "DMP-256")),
    ("doc3:SCR-026", "doc3", "SCR-026", (), (), (), (), (), (), ("D-094",), ("B-06",)),
    ("doc3:SCR-027", "doc3", "SCR-027", (), (), (), (), (), (), ("D-097", "D-098"), ("B-06", "DMP-184")),
    ("doc3:SCR-028", "doc3", "SCR-028", (), (), (), (), (), (), (), ("B-06", "DMP-163")),
    ("doc3:SCR-030", "doc3", "SCR-030", (), (), (), (), (), (), ("D-051", "D-062"), ("B-04", "ECN-009")),
    ("doc3:SCR-031", "doc3", "SCR-031", (), (), (), (), (), (), (), ("B-04", "ECN-142")),
    ("doc3:SCR-032", "doc3", "SCR-032", (), (), (), (), (), (), ("D-053",), ("B-04",)),
    ("doc3:SCR-033", "doc3", "SCR-033", (), (), (), (), (), (), (), ("B-04", "B-05", "ECN-006", "MKT-053")),
    ("doc3:SCR-034", "doc3", "SCR-034", (), (), (), (), (), (), ("D-048",), ("B-04", "B-05")),
    ("doc3:SCR-035", "doc3", "SCR-035", (), (), (), (), (), ("REQ-465",), (), ("B-07",)),
    ("doc3:SCR-036", "doc3", "SCR-036", (), (), (), (), (), (), (), ("B-07", "MKT-038", "MKT-060")),
    ("doc3:SCR-037", "doc3", "SCR-037", (), (), (), (), (), (), ("D-017",), ("B-07", "ECON-013")),
    ("doc3:SCR-038", "doc3", "SCR-038", (), (), (), (), (), ("REQ-513",), ("D-122",), ("B-07", "G-1", "G-2", "G-3", "G-4", "G-5", "G-6")),
    ("doc3:SCR-039", "doc3", "SCR-039", (), (), (), (), (), (), ("D-111",), ("B-07",)),
    ("doc3:SCR-040", "doc3", "SCR-040", (), (), (), (), (), (), ("D-117",), ("B-07",)),
    ("doc3:SCR-041", "doc3", "SCR-041", (), (), (), (), (), (), ("D-067",), ("B-05", "URB-031")),
    ("doc3:SCR-042", "doc3", "SCR-042", (), (), (), (), (), (), (), ("B-05", "URB-052")),
    ("doc3:SCR-043", "doc3", "SCR-043", (), (), (), (), (), (), ("D-073", "D-074"), ("B-05", "URB-148")),
    ("doc3:SCR-044", "doc3", "SCR-044", (), (), (), (), (), (), (), ("B-05", "URB-149")),
    ("doc3:SCR-045", "doc3", "SCR-045", (), (), (), (), (), (), ("D-076",), ("B-05", "URB-150", "URB-152")),
    ("doc3:SCR-046", "doc3", "SCR-046", (), (), (), (), (), (), ("D-068",), ("B-05",)),
    ("doc3:SCR-047", "doc3", "SCR-047", (), (), (), (), (), (), (), ("B-08", "DIP-030")),
    ("doc3:SCR-048", "doc3", "SCR-048", (), (), (), (), (), (), (), ("B-08", "NET-023")),
    ("doc3:SCR-049", "doc3", "SCR-049", (), (), (), (), (), (), ("D-030",), ("B-08",)),
    ("doc3:SCR-050", "doc3", "SCR-050", (), (), (), (), (), (), (), ("B-08",)),
    ("doc3:SCR-051", "doc3", "SCR-051", (), (), (), (), (), (), (), ("B-08", "DIP-108", "DIP-109", "DIP-110", "DIP-111", "DIP-112", "DIP-113")),
    ("doc3:SCR-052", "doc3", "SCR-052", (), (), (), (), (), (), (), ("B-08",)),
    ("doc3:SCR-053", "doc3", "SCR-053", ("13A-SRC-006",), (), (), (), (), (), (), ("ALL-086", "B-09")),
    ("doc3:SCR-054", "doc3", "SCR-054", (), (), (), (), (), (), ("UD-040",), ("B-09",)),
    ("doc3:SCR-055", "doc3", "SCR-055", (), (), (), (), (), (), ("D-135",), ("B-09",)),
    ("doc3:SCR-057", "doc3", "SCR-057", (), (), (), (), (), (), ("UD-045", "UD-046"), ("B-09",)),
    ("doc3:SCR-058", "doc3", "SCR-058", (), (), (), (), (), (), (), ("B-09", "WAR-149")),
    ("doc3:SCR-059", "doc3", "SCR-059", (), (), (), (), (), (), ("D-015",), ("B-10", "SYS-011")),
    ("doc3:SCR-060", "doc3", "SCR-060", (), (), (), (), (), (), (), ("B-10",)),
    ("doc3:SCR-061", "doc3", "SCR-061", (), (), (), (), (), (), (), ("B-10", "WAR-148")),
    ("doc3:SCR-063", "doc3", "SCR-063", (), (), (), (), (), (), (), ("B-10", "WAR-085", "WAR-086", "WAR-087", "WAR-088")),
    ("doc3:SCR-064", "doc3", "SCR-064", ("13A-SRC-034",), (), (), (), (), (), (), ("B-10",)),
    ("doc3:SCR-065", "doc3", "SCR-065", (), (), (), (), (), (), (), ("B-10",)),
    ("doc3:SCR-066", "doc3", "SCR-066", (), (), (), (), (), (), ("D-026",), ("B-10", "B-11")),
    ("doc3:SCR-067", "doc3", "SCR-067", (), (), (), (), (), (), ("UD-032",), ("B-10",)),
    ("doc3:SCR-068", "doc3", "SCR-068", (), (), (), (), ("13A-OQ-010",), (), (), ("B-10",)),
    ("doc3:SCR-069", "doc3", "SCR-069", (), (), (), (), (), (), (), ("B-11", "WPC-14")),
    ("doc3:SCR-070", "doc3", "SCR-070", (), (), ("13A-BP-007",), (), (), (), (), ("B-11",)),
    ("doc3:SCR-071", "doc3", "SCR-071", (), (), (), (), (), (), (), ("B-11", "WEP-713")),
    ("doc3:SCR-073", "doc3", "SCR-073", (), (), (), (), (), (), (), ("B-11",)),
    ("doc3:SCR-074", "doc3", "SCR-074", (), (), (), (), (), (), (), ("B-11",)),
    ("doc3:SCR-075", "doc3", "SCR-075", (), (), (), (), (), (), (), ("B-11",)),
    ("doc3:SCR-076", "doc3", "SCR-076", (), (), (), (), (), (), (), ("B-11", "TR-049")),
    ("doc3:SCR-077", "doc3", "SCR-077", ("13A-SRC-015",), (), (), (), (), (), ("D-027",), ("B-11",)),
    ("doc3:SCR-079", "doc3", "SCR-079", (), (), (), (), (), (), ("D-042",), ("B-12", "PRV-009")),
    ("doc3:SCR-080", "doc3", "SCR-080", (), (), (), (), (), (), ("D-041",), ("B-03", "B-12")),
    ("doc3:SCR-081", "doc3", "SCR-081", (), (), (), (), (), (), (), ("B-12", "FR-001", "FR-006", "MOD-002")),
    ("doc3:SCR-082", "doc3", "SCR-082", (), (), (), (), (), (), (), ("B-12", "EVD-009", "MOD-017")),
    ("doc3:SCR-083", "doc3", "SCR-083", (), (), (), (), (), (), (), ("B-12", "MOD-013")),
    ("doc3:SCR-084", "doc3", "SCR-084", (), (), (), (), (), (), (), ("ACC-018", "B-03", "B-12", "NET-023", "NET-050")),
    ("doc3:SCR-085", "doc3", "SCR-085", (), (), (), (), (), (), ("D-026",), ("B-03", "B-12", "SEC-032")),
    ("doc3:SCR-086", "doc3", "SCR-086", (), (), (), (), (), (), ("D-033", "D-034"), ("B-03",)),
    ("doc3:SCR-087", "doc3", "SCR-087", (), (), (), (), ("SCR-078",), (), (), ("B-12",)),
    ("doc3:SCR-089", "doc3", "SCR-089", (), (), (), (), (), (), (), ("B-03", "ONB-020", "ONB-022", "WAR-115", "WAR-116", "WAR-117")),
    ("doc3:SCR-090", "doc3", "SCR-090", (), (), (), (), (), (), ("D-039",), ("B-03", "RRL-006")),
    ("doc3:SCR-091", "doc3", "SCR-091", (), (), (), (), (), (), (), ("B-12",)),
    ("doc3:SCR-092", "doc3", "SCR-092", (), (), (), (), (), (), (), ("ADM-021", "ADM-022", "B-12")),
    ("doc3:SCR-093", "doc3", "SCR-093", (), (), (), (), (), (), (), ("B-12",) + tuple(f"V-{n:02d}" for n in range(1, 17))),
    ("doc3:SCR-094", "doc3", "SCR-094", (), (), (), (), (), (), (), ("B-08", "B-12")),
    ("doc3:SCR-095", "doc3", "SCR-095", (), (), (), (), (), (), ("D-034",), ("B-03", "B-12")),
    ("doc3:SCR-096", "doc3", "SCR-096", (), (), (), (), (), (), (), ("B-12", "SEC-031")),
    ("doc3:SCR-097", "doc3", "SCR-097", (), (), (), (), (), (), (), ("B-02", "TR-080")),
    ("doc3:SCR-098", "doc3", "SCR-098", (), (), (), (), (), (), ("D-026",), ("B-12",)),
    ("doc3:SCR-099", "doc3", "SCR-099", (), (), (), (), (), (), (), ("ALL-164", "B-09", "B-12", "MOD-017")),
    ("doc3:SCR-100", "doc3", "SCR-100", (), (), (), (), (), (), (), ("ADM-021", "ADM-022", "B-12")),
    ("doc3:OVL-01", "doc3", "OVL-01", (), (), (), (), ("13A-PR-09",), (), (), ()),
    ("doc3:OVL-02", "doc3", "OVL-02", (), (), (), (), ("SCR-090",), (), (), ("RRL-006",)),
    ("doc3:OVL-03", "doc3", "OVL-03", (), (), (), (), ("13A-PR-10",), (), (), ()),
    ("doc3:OVL-04", "doc3", "OVL-04", (), (), (), (), ("13A-PR-04",), (), (), ()),
    ("doc3:OVL-05", "doc3", "OVL-05", (), (), (), (), (), (), (), ()),
    ("doc3:OVL-06", "doc3", "OVL-06", (), (), (), (), ("13A-PR-06",), (), (), ()),
    ("doc3:OVL-07", "doc3", "OVL-07", (), (), (), (), (), (), ("D-027",), ()),
    ("doc3:OVL-08", "doc3", "OVL-08", (), (), (), (), ("SCR-082", "SCR-084"), (), (), ("B-12", "EVD-009")),
    # --- Remaining doc4 RD & DS rows ---
    ("doc4:13A-RD-02", "doc4", "13A-RD-02", (), (), (), (), (), (), (), ()),
    ("doc4:13A-RD-03", "doc4", "13A-RD-03", (), (), (), (), (), (), (), ()),
    ("doc4:13A-RD-04", "doc4", "13A-RD-04", (), (), (), (), ("13A-PR-01",), (), (), ("MKT-053",)),
    ("doc4:13A-RD-05", "doc4", "13A-RD-05", (), (), (), (), (), (), (), ()),
    ("doc4:13A-RD-06", "doc4", "13A-RD-06", (), (), (), (), (), (), (), ()),
    ("doc4:13A-RD-07", "doc4", "13A-RD-07", (), (), (), (), (), (), (), ()),
    ("doc4:13A-RD-08", "doc4", "13A-RD-08", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-01", "doc4", "13A-DS-01", (), (), (), (), ("13A-OQ-002",), (), (), ()),
    ("doc4:13A-DS-02", "doc4", "13A-DS-02", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-03", "doc4", "13A-DS-03", (), (), (), (), ("13A-PR-16",), (), (), ("B-04",)),
    ("doc4:13A-DS-04", "doc4", "13A-DS-04", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-05", "doc4", "13A-DS-05", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-06", "doc4", "13A-DS-06", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-08", "doc4", "13A-DS-08", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-09", "doc4", "13A-DS-09", (), (), (), (), ("13A-OQ-001",), (), (), ()),
    ("doc4:13A-DS-11", "doc4", "13A-DS-11", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-12", "doc4", "13A-DS-12", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-13", "doc4", "13A-DS-13", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-14", "doc4", "13A-DS-14", (), (), (), (), (), (), (), ()),
    ("doc4:13A-DS-15", "doc4", "13A-DS-15", ("13A-SRC-017",), (), (), (), (), (), (), ()),
    # --- Remaining doc5 UR rows (all 48 UR-001..048 covered in §2.1 & §2.2!) ---
    ("doc5:UR-001", "doc5", "UR-001", ("13A-SRC-017",), (), ("13A-BP-001",), ("13A-DR-002", "13A-DR-017"), ("13A-OQ-015",), ("REQ-020", "REQ-022"), (), ("B-02",)),
    ("doc5:UR-002", "doc5", "UR-002", (), (), (), ("13A-DR-002",), ("13A-PR-01",), (), (), ("B-02",)),
    ("doc5:UR-006", "doc5", "UR-006", (), (), ("13A-BP-026",), (), ("13A-RD-04",), (), (), ("B-04", "B-07", "MKT-053")),
    ("doc5:UR-011", "doc5", "UR-011", (), (), ("13A-BP-004",), (), ("13A-DS-12",), (), (), ()),
    ("doc5:UR-018", "doc5", "UR-018", (), (), (), (), (), ("REQ-317", "REQ-318", "REQ-319", "REQ-320", "REQ-321"), (), ("B-06", "DMP-256", "DMP-268")),
    ("doc5:UR-022", "doc5", "UR-022", (), (), (), (), (), ("REQ-090", "REQ-687"), ("D-040",), ("B-03", "B-10", "B-12", "ONB-020", "ONB-022")),
    ("doc5:UR-023", "doc5", "UR-023", ("13A-SRC-017", "13A-SRC-018"), (), (), (), (), ("REQ-085", "REQ-092"), ("D-029", "D-041"), ("B-03",)),
    ("doc5:UR-025", "doc5", "UR-025", (), (), (), (), (), ("REQ-821", "REQ-822"), (), ("B-12", "FR-001", "FR-006", "MOD-002")),
    ("doc5:UR-026", "doc5", "UR-026", (), (), (), (), (), ("REQ-826", "REQ-833", "REQ-848"), (), ("B-12", "EVD-009", "MOD-013", "MOD-017")),
    ("doc5:UR-027", "doc5", "UR-027", (), (), (), (), (), ("REQ-801", "REQ-802", "REQ-803", "REQ-804"), (), ("B-12", "PRV-009", "PRV-014")),
    ("doc5:UR-030", "doc5", "UR-030", (), (), (), (), (), ("REQ-513",), ("D-117",), ("B-07", "G-1", "G-2", "G-3", "G-4", "G-5", "G-6")),
    ("doc5:UR-031", "doc5", "UR-031", (), ("13A-FND-004", "13A-FND-024"), ("13A-BP-004",), ("13A-DR-004",), (), (), (), ("MKT-065",)),
    ("doc5:UR-032", "doc5", "UR-032", (), ("13A-FND-001",), ("13A-BP-002",), ("13A-DR-017",), ("13A-PR-13",), (), (), ()),
    ("doc5:UR-034", "doc5", "UR-034", (), (), (), (), ("13A-OQ-005", "13A-OQ-009"), (), (), ()),
    ("doc5:UR-037", "doc5", "UR-037", (), (), (), (), (), (), ("D-194",), ("B-12",)),
    ("doc5:UR-038", "doc5", "UR-038", (), (), (), ("13A-DR-002",), ("13A-PR-01",), (), (), ("B-02",)),
    ("doc5:UR-041", "doc5", "UR-041", (), (), ("13A-BP-025",), ("13A-DR-012",), ("13A-RD-02", "13A-RD-07", "13A-RD-08", "13A-UR-002", "13A-UR-006", "13A-UR-012", "13A-UR-018", "13A-UR-022"), (), (), ()),
    ("doc5:UR-043", "doc5", "UR-043", (), (), (), (), ("13A-OQ-001", "13A-OQ-002"), (), (), ()),
    ("doc5:UR-045", "doc5", "UR-045", (), ("13A-FND-023",), (), (), (), (), (), ()),
    ("doc5:UR-047", "doc5", "UR-047", ("13A-SRC-017",), ("13A-FND-021",), ("13A-BP-023",), (), ("13A-DS-15",), (), (), ()),
    ("doc5:UR-048", "doc5", "UR-048", (), (), (), (), ("13A-OQ-016",), (), (), ()),
    # --- Remaining DECISIONS.md rows D-198..D-205 ---
    ("decisions:D-198", "decisions", "D-198", (), (), (), (), (), (), ("D-132", "D-163"), ("B-07", "B-08", "B-09", "B-11", "B-12", "B-13", "B-14", "B-15", "B-18", "B-19")),
    ("decisions:D-199", "decisions", "D-199", (), (), (), (), ("P13A-02", "P13A-03", "P13A-19"), (), ("D-003",), ()),
    ("decisions:D-200", "decisions", "D-200", (), (), (), (), ("OVL-01", "OVL-08", "SCR-001", "SCR-091", "SCR-100"), (), (), ()),
    ("decisions:D-204", "decisions", "D-204", (), (), (), (), ("13A-OQ-001", "13A-OQ-016", "13A-UR-001", "13A-UR-048"), ("REQ-764", "REQ-869", "REQ-870"), ("D-163",), ("B-13",)),
    ("decisions:D-205", "decisions", "D-205", (), (), (), (), (), (), ("D-195", "D-196"), ()),
))

# Backward-compatible name alias for callers inspecting the semantic table.
SEMANTIC_CROSS_REFS = CLAIM_ALLOWLISTS


def _extract_tokens(text: str) -> set[str]:
    """Expand compound citations inside a single row or paragraph for semantic checks."""
    out = set()
    short_map = {
        "SRC": "13A-SRC", "FND": "13A-FND", "BP": "13A-BP", "DR": "13A-DR",
        "PR": "13A-PR", "RD": "13A-RD", "DS": "13A-DS", "OQ": "13A-OQ", "UR": "13A-UR",
    }
    pat = re.compile(
        r"(?<![A-Za-z0-9-])(13A-SRC|13A-FND|13A-BP|13A-DR|13A-PR|13A-RD|13A-DS|13A-OQ|13A-UR|"
        r"SCR|OVL|P13A|SRC|FND|BP|DR|PR|RD|DS|OQ|UR)-0*(\d{1,3})"
        r"(?:([/,…\-\u2013]+|\.\.)0*(\d{1,3}(?:[/,]\d{1,3})*))?\b"
    )
    for m in pat.finditer(text):
        raw_fam, first, sep, rest = m.group(1), int(m.group(2)), m.group(3), m.group(4)
        fam = short_map.get(raw_fam, raw_fam)
        width = 2 if fam in ("13A-PR", "13A-RD", "13A-DS", "OVL", "P13A") else 3
        nums = [first]
        if rest is not None:
            if sep in ("…", "..", "-", "\u2013"):
                end = int(re.split(r"[/,]", rest)[0])
                if end >= first and end - first <= 30:
                    nums = list(range(first, end + 1))
                else:
                    nums.extend(int(x) for x in re.split(r"[/,]", rest) if x.isdigit())
            else:
                nums.extend(int(x) for x in re.split(r"[/,]", rest) if x.isdigit())
        for n in nums:
            out.add(f"{fam}-{n:0{width}d}")
    return out


def _extract_req_tokens(text: str) -> set[str]:
    return _expand_prefixed_tokens(text, "REQ", {"REQ": 3}, max_digits=4)


def _extract_dec_tokens(text: str) -> set[str]:
    return _expand_prefixed_tokens(text, r"D|UD", {"D": 3, "UD": 3}, max_digits=3)


_DUP_CIT_PAT = re.compile(
    rf"(?<![A-Za-z0-9-])(13A-SRC|13A-FND|13A-BP|13A-DR|13A-PR|13A-RD|13A-DS|13A-OQ|13A-UR|"
    rf"SCR|OVL|P13A|REQ|D|UD|{LEGACY_PREFS_RE})-0*(\d{{1,4}})([a-z]?)(?![0-9A-Za-z_])"
)
_DUP_SHORT_PAT = re.compile(
    rf"(?<![A-Za-z0-9-])(13A-SRC|13A-FND|13A-BP|13A-DR|13A-PR|13A-RD|13A-DS|13A-OQ|13A-UR|"
    rf"SCR|OVL|P13A|REQ|D|UD|{LEGACY_PREFS_RE})-0*(\d{{1,4}})([a-z]?)\s*[/,]\s*0*\2\3(?![0-9A-Za-z_])"
)
_DUP_GAP_RE = re.compile(r"[\s`*]*(?:,|;|/|&|\band\b)[\s`*]*", re.I)


def _norm_cit_token(fam: str, num_s: str, suf: str) -> str:
    n = int(num_s)
    if fam in LEGACY_WIDTHS:
        return f"{fam}-{n:0{LEGACY_WIDTHS[fam]}d}{suf}"
    if fam in ("REQ", "D", "UD"):
        return f"{fam}-{n:03d}{suf}"
    width = 2 if fam in ("13A-PR", "13A-RD", "13A-DS", "OVL", "P13A") else 3
    return f"{fam}-{n:0{width}d}{suf}"


def _find_list_duplicate_citations(block: str) -> list[str]:
    """Detect list-adjacent duplicate citations inside any single cell (e.g. `DMP-164, DMP-164` or `WAR-148/148`)."""
    dups: list[str] = []
    seen_dups: set[str] = set()
    for cell in block.split("|"):
        for sm in _DUP_SHORT_PAT.finditer(cell):
            tok = _norm_cit_token(sm.group(1), sm.group(2), sm.group(3))
            if tok not in seen_dups:
                seen_dups.add(tok)
                dups.append(tok)
        matches = list(_DUP_CIT_PAT.finditer(cell))
        for prev_m, cur_m in zip(matches, matches[1:]):
            gap = cell[prev_m.end():cur_m.start()]
            if not _DUP_GAP_RE.fullmatch(gap):
                continue
            t1 = _norm_cit_token(prev_m.group(1), prev_m.group(2), prev_m.group(3))
            t2 = _norm_cit_token(cur_m.group(1), cur_m.group(2), cur_m.group(3))
            if t1 == t2 and t1 not in seen_dups:
                seen_dups.add(t1)
                dups.append(t1)
    return dups


def c33_semantic_cross_refs(T):
    """Strict claim-level citation allowlist validation (13A + REQ + D/UD + all legacy namespaces) and UR checks."""
    p = []
    # Canonical live identifier universes derived dynamically from disk registers (never static copies).
    canon_13a = (
        {f"13A-SRC-{n:03d}" for n in row_ids(section(T["doc1"], "## 3."), "13A-SRC")}
        | {f"13A-SRC-{n:03d}" for n in row_ids(section(T["doc1"], "## 4."), "13A-SRC")}
        | {f"13A-SRC-{n:03d}" for n in row_ids(section(T["doc1"], "## 5."), "13A-SRC")}
        | {f"13A-FND-{n:03d}" for n in row_ids(section(T["doc1"], "## 7."), "13A-FND")}
        | {f"13A-BP-{n:03d}" for n in row_ids(section(T["doc1"], "## 8."), "13A-BP")}
        | {f"13A-DR-{n:03d}" for n in row_ids(section(T["doc1"], "## 9."), "13A-DR")}
        | {f"13A-PR-{n:02d}" for n in row_ids(T["doc2"], "13A-PR")}
        | {f"SCR-{n:03d}" for n in row_ids(T["doc3"], "SCR")}
        | {f"OVL-{n:02d}" for n in row_ids(T["doc3"], "OVL")}
        | {f"13A-RD-{n:02d}" for n in row_ids(section(T["doc4"], "### 1.3"), "13A-RD")}
        | {"13A-RD-01"}
        | {f"13A-DS-{n:02d}" for n in row_ids(T["doc4"], "13A-DS")}
        | {f"13A-UR-{n:03d}" for n in row_ids(section(T["doc5"], "### 2.1"), "UR")}
        | {f"13A-OQ-{n:03d}" for n in row_ids(section(T["doc5"], "## 4."), "OQ")}
        | {f"P13A-{n:02d}" for n in row_ids(section(T["doc5"], "## 5."), "P13A")}
    )
    legacy_univ = _load_legacy_universe(T)
    if not legacy_univ:
        return ["failed to load canonical legacy identifier universe from stage-1/stage-2 registers"]

    # Global existence check across all five 13A deliverables for every recognized legacy identifier.
    for key in ("doc1", "doc2", "doc3", "doc4", "doc5"):
        missing_legacy = sorted(_extract_legacy_tokens(T[key]) - legacy_univ)
        if missing_legacy:
            p.append(f"{key}: unknown/non-existent legacy identifier(s) {missing_legacy} not in canonical Stage-1/Stage-2 registers")

    s21_text = section(T["doc5"], "### 2.1").split("### 2.2")[0]
    s22_text = section(T["doc5"], "### 2.2")
    lines_by_scope = {
        k: T[k].splitlines() for k in ("doc1", "doc2", "doc3", "doc4", "decisions")
    }
    lines_by_scope["s21"] = s21_text.splitlines()
    lines_by_scope["s22"] = s22_text.splitlines()
    row_idx_by_scope: dict[str, dict[str, list[tuple[int, str]]]] = {}
    for scope, slines in lines_by_scope.items():
        rmap: dict[str, list[tuple[int, str]]] = {}
        for idx, line in enumerate(slines):
            if line.startswith("|"):
                parts = line.split("|", 2)
                if len(parts) >= 2:
                    c0 = parts[1].strip().strip("`")
                    rmap.setdefault(c0, []).append((idx, line))
        row_idx_by_scope[scope] = rmap

    def _validate_block(rule, block: str, scope_tag: str, check_requirements: bool) -> None:
        label = f"{rule['record_id']}{scope_tag}"
        raw_13a = _extract_tokens(block)
        unknown_13a = raw_13a - canon_13a
        if unknown_13a:
            p.append(f"{label}: non-existent/invalid 13A identifier(s) {sorted(unknown_13a)} in {block[:80]!r}")

        raw_legacy = _extract_legacy_tokens(block)
        unknown_legacy = raw_legacy - legacy_univ
        if unknown_legacy:
            p.append(f"{label}: non-existent legacy identifier(s) {sorted(unknown_legacy)} in {block[:80]!r}")

        dups = _find_list_duplicate_citations(block)
        if dups:
            p.append(f"{label}: duplicate citation(s) in list {dups}")

        cited_13a = raw_13a - rule["self_ids"]
        allowed_deps = rule["allow_deps"] | {t for t in rule["allow_reqs"] if not t.startswith("REQ-")}
        extra_by_fam = {
            "13A-SRC": {t for t in cited_13a if t.startswith("13A-SRC-")} - rule["allow_src"],
            "13A-FND": {t for t in cited_13a if t.startswith("13A-FND-")} - rule["allow_fnd"],
            "13A-BP": {t for t in cited_13a if t.startswith("13A-BP-")} - rule["allow_bp"],
            "13A-DR": {t for t in cited_13a if t.startswith("13A-DR-")} - rule["allow_dr"],
            "13A-foundation/SCR/OVL": (
                {t for t in cited_13a if not t.startswith(("13A-SRC-", "13A-FND-", "13A-BP-", "13A-DR-"))}
                - allowed_deps
            ),
        }
        for fam_name, extra in extra_by_fam.items():
            if extra:
                p.append(f"{label}: unpermitted {fam_name} citation(s) {sorted(extra)} not in allowlist ({rule['classification']})")

        allowed_req = {t for t in rule["allow_reqs"] if t.startswith("REQ-")}
        cited_req = _extract_req_tokens(block) - rule["self_ids"]
        extra_req = cited_req - allowed_req
        if extra_req:
            p.append(f"{label}: unpermitted REQ citation(s) {sorted(extra_req)} not in allowlist")

        cited_dec = _extract_dec_tokens(block) - rule["self_ids"]
        extra_dec = cited_dec - rule["allow_dec"]
        if extra_dec:
            p.append(f"{label}: unpermitted decision citation(s) {sorted(extra_dec)} not in allowlist")

        cited_legacy = raw_legacy - rule["self_ids"]
        extra_legacy = cited_legacy - rule["allow_legacy"]
        if extra_legacy:
            p.append(f"{label}: unpermitted legacy citation(s) {sorted(extra_legacy)} not in allowlist ({rule['classification']})")

        if check_requirements:
            all_cited = cited_13a | cited_req | cited_dec | cited_legacy
            if rule["required_any"] and not any(req in all_cited for req in rule["required_any"]):
                p.append(f"{label}: lacks any required support {rule['required_any']} (saw {sorted(all_cited)})")

            for marker in rule["required_markers"]:
                if marker not in block:
                    p.append(f"{label}: missing required classification marker {marker!r}")

        if rule["classification"] == "INDEPENDENT_ACCESSIBILITY_REQUIREMENT":
            research_toks = {t for t in cited_13a if t.startswith(("13A-SRC-", "13A-FND-", "13A-BP-"))}
            if research_toks:
                p.append(f"{label}: independent accessibility requirement must not cite P&W research/patterns {sorted(research_toks)}")

    for rule in CLAIM_ALLOWLISTS:
        label = rule["record_id"]
        key = rule["doc_key"]
        anchor_re = rule["anchor_re"]
        rtok = rule["row_tok"]

        if key == "doc5" and label.startswith("doc5:UR-"):
            if rtok is not None:
                s22_hits = [line for _, line in row_idx_by_scope["s22"].get(rtok, ())]
            else:
                s22_hits = [l for l in lines_by_scope["s22"] if anchor_re.search(l)]
            if not s22_hits:
                p.append(f"{label} (§2.2): traceability ledger row missing in §2.2")
            else:
                for line in s22_hits:
                    _validate_block(rule, line, " (§2.2)", check_requirements=False)
            scope = "s21"
        else:
            scope = key

        search_lines = lines_by_scope[scope]
        if rtok is not None:
            hits = row_idx_by_scope[scope].get(rtok, ())
            idxs = [idx for idx, _ in hits]
        else:
            idxs = [i for i, l in enumerate(search_lines) if anchor_re.search(l)]
        if not idxs:
            p.append(f"{label}: anchor pattern missing in {key}")
            continue
        for idx in idxs:
            block = search_lines[idx]
            if label == "doc2:shell-rule-anchor-E" and idx + 1 < len(search_lines):
                block = block + "\n" + search_lines[idx + 1]
            _validate_block(rule, block, "", check_requirements=True)

    # Also verify UR-001..048 System column values belong to known NS systems/scopes.
    valid_systems = {"all", "cross", "chronicle", "infra", "region"} | {f"B-{n:02d}" for n in range(2, 13)}
    for uid, cells in row_cells(s21_text, "UR"):
        if len(cells) >= 5:
            sys_cell = cells[4].strip()
            parts = [s.strip() for s in re.split(r"[/+,\s]+", sys_cell) if s.strip()]
            bad_sys = [s for s in parts if s not in valid_systems]
            if bad_sys:
                p.append(f"doc5:UR-{uid:03d}: unrecognized System token(s) {bad_sys} in {sys_cell!r}")
    return p


def c34_research_evidence_alignment(T):
    """Check bounded P&W claims (FND-026/031/032), independent a11y evidence (DS-07/UR-010), DR->BP/FND links, and gate honesty."""
    p = []
    doc1 = T["doc1"]

    def _row(text, pat):
        return next((l for l in text.splitlines() if re.search(pat, l)), "")

    f26 = _row(doc1, r"^\|\s*`?13A-FND-026`?\s*\|")
    f31 = _row(doc1, r"^\|\s*`?13A-FND-031`?\s*\|")
    f32 = _row(doc1, r"^\|\s*`?13A-FND-032`?\s*\|")
    dr21 = _row(doc1, r"^\|\s*`?13A-DR-021`?\s*\|")
    dr01 = _row(doc1, r"^\|\s*`?13A-DR-001`?\s*\|")
    dr15 = _row(doc1, r"^\|\s*`?13A-DR-015`?\s*\|")
    dr18 = _row(doc1, r"^\|\s*`?13A-DR-018`?\s*\|")
    ds07 = _row(T["doc4"], r"^\|\s*`?13A-DS-07`?\s*\|")
    ur010 = _row(section(T["doc5"], "### 2.1").split("### 2.2")[0], r"^\|\s*UR-010\s*\|")

    if "NOT-RETRIEVABLE" not in f26 or "13A-SRC-032" not in f26:
        p.append("doc1:13A-FND-026 must explicitly record the logged-out / NOT-RETRIEVABLE (13A-SRC-032) boundary")
    if "colour-only affiliation encoding with no observed non-colour" in f31.lower() or "Alliance" not in f31 or "Color" not in f31:
        p.append("doc1:13A-FND-031 must accurately report Alliance + Color text columns without colour-only overclaim")
    if "hides state failures" in f32.lower() or "13A-SRC-032" not in f32:
        p.append("doc1:13A-FND-032 must bound shell fallback to unauthenticated GET without claiming P&W hides authenticated errors")
    if "13A-BP-017" in _extract_tokens(dr21):
        p.append("doc1:13A-DR-021 improperly cites 13A-BP-017 (Discord rejection) instead of WAR-149/ALL-161/13A-FND-010/012")
    if "13A-SRC-032" not in _extract_tokens(dr01) or "p&w lacks it" in dr01.lower():
        p.append("doc1:13A-DR-001 must ground Digest+Inbox in NS rules + bounded 13A-FND-026/13A-SRC-032")
    if "13A-FND-031" not in _extract_tokens(dr15) or "DMP-164" not in dr15:
        p.append("doc1:13A-DR-015 must pair independent NS accessibility basis with bounded 13A-FND-031")
    if "13A-FND-032" not in _extract_tokens(dr18) or "defect" in dr18.lower():
        p.append("doc1:13A-DR-018 must frame NS error/empty/denied states independently with bounded 13A-FND-032")

    for rec_label, line in (("doc4:13A-DS-07", ds07), ("doc5:UR-010", ur010)):
        toks = _extract_tokens(line)
        if toks & {"13A-FND-013", "13A-FND-028"}:
            p.append(f"{rec_label}: improperly cites unrelated P&W API/export findings {sorted(toks & {'13A-FND-013', '13A-FND-028'})} for keyboard accessibility")
        if "INDEPENDENT_ACCESSIBILITY_REQUIREMENT" not in line or "REQ-321" not in line:
            p.append(f"{rec_label}: must classify keyboard/focus requirement as INDEPENDENT_ACCESSIBILITY_REQUIREMENT with NS REQ-321 basis")

    if "not** received owner acceptance" not in T["doc5"].lower() and "has not received owner acceptance" not in T["doc5"].lower():
        p.append("doc5:§5 must state explicitly that Prompt 13A has not received owner acceptance")
    return p


CHECKS = [
    ("13A-01", "the five 13A deliverables exist at canonical paths", c01_files),
    ("13A-02", "every deliverable header records Prompt 13A and its boundary", c02_headers),
    ("13A-03", "source register is 001–036 contiguous with correct section membership", c03_src_register),
    ("13A-04", "no malformed, wrong-family, bad-suffix or wrong-width 13A identifier token", c04_src_tokens),
    ("13A-05", "evidence-class distribution is computed and §10.1 reports it", c05_evidence_classes),
    ("13A-06", "findings register 001–040, every row cites evidence", c06_findings),
    ("13A-07", "benchmark-pattern register 001–028 with a disposition each", c07_patterns),
    ("13A-08", "recommendation register 001–024 with a basis each", c08_recommendations),
    ("13A-09", "P&W identity, prohibited categories and inputs-only boundary", c09_benchmark),
    ("13A-10", "16 principles, 8 navigation sections, 13 application states", c10_principles),
    ("13A-11", "screen identifiers are unique and contiguous SCR-001–100", c11_screen_ids),
    ("13A-12", "class tally and §7 arithmetic agree with the register", c12_screen_tally),
    ("13A-13", "administrative family is SCR-091–100 behind the Admin parent", c13_admin_family),
    ("13A-14", "hierarchy diagram, overlay register and navigation audit present", c14_hierarchy),
    ("13A-15", "design-system 01–15 and responsive 01–08 rules registered", c15_responsive_ds),
    ("13A-16", "same-rules guarantee, provisional breakpoints, no-CSS boundary", c16_responsive_boundaries),
    ("13A-17", "UR-001–048 appear in both the register and the ledger", c17_ur_register),
    ("13A-18", "open questions OQ-001–016 with bucket coverage", c18_open_questions),
    ("13A-19", "P13A-01–24 unique, one bolded result per gate", c19_gate_rows),
    ("13A-20", "stated gate tally equals the computed results (23/1/0/0)", c20_gate_tally),
    ("13A-21", "identifier policy: no global REQ/UD, REQ-870 reserved", c21_identifier_policy),
    ("13A-22", "every cited REQ- resolves in the requirements tracker", c22_req_citations),
    ("13A-23", "every cited D-/UD- resolves in the decision registers", c23_decision_citations),
    ("13A-24", "every cited 13A-/SCR-/OVL-/P13A- id (incl. compounds & D-198..205) resolves", c24_family_citations),
    ("13A-25", "D-198–205 and DD-246–253 are recorded and mirrored", c25_decision_records),
    ("13A-26", "STATUS blocks agree: 13B, D-001..D-205, ui_foundations identical", c26_status_blocks),
    ("13A-27", "log §§87–89, roadmap split registration and outline B-13 path", c27_roadmap_registration),
    ("13A-28", "Prompt 13A instruction archived and indexed with its digest", c28_prompt_archive),
    ("13A-29", "12A/12B/12C/R7/R8/security statuses preserved unchanged", c29_protected_statuses),
    ("13A-30", "no merge-conflict markers in the touched files", c30_hygiene),
    ("13A-31", "relative links inside the deliverables resolve", c31_links),
    ("13A-32", "no implementation, conformance or owner-approval over-claims", c32_no_overclaim),
    ("13A-33", "strict claim-level citation allowlist validation across 13A & D-201..203", c33_semantic_cross_refs),
    ("13A-34", "P&W evidence bounds, independent accessibility evidence & acceptance bounds", c34_research_evidence_alignment),
]


def run(T):
    results = []
    for cid, name, fn in CHECKS:
        try:
            problems = fn(T)
        except Exception as exc:  # a crashing check is a failure, never a pass
            problems = [f"check raised {type(exc).__name__}: {exc}"]
        results.append((cid, name, problems))
    return results


# ---------------------------------------------------------------------------
# self-test — seeded defects must be caught by the named check (plus valid controls)
# ---------------------------------------------------------------------------

def fx_dup_scr(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-050`"))
    T["doc3"] = t.replace(line, line.replace("SCR-050", "SCR-049", 1), 1)
    return "13A-11"


def fx_gate_swap(T):
    lines = T["doc5"].splitlines()
    idx = next(i for i, l in enumerate(lines) if re.match(r"^\|\s*`?P13A-05`?\s*\|", l))
    lines[idx] = lines[idx].replace("**PASS**", "**FAIL**", 1)
    T["doc5"] = "\n".join(lines) + "\n"
    return "13A-20"


def fx_class_flip(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-002`"))
    T["doc3"] = t.replace(line, line.replace("| B-03 | Mandatory |", "| B-03 | Conditional |"), 1)
    return "13A-12"


def fx_fake_req(T):
    T["doc2"] = T["doc2"] + "\nDepends on REQ-991 which the tracker does not carry.\n"
    return "13A-22"


def fx_src_removed(T):
    t = T["doc1"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-SRC-014`"))
    T["doc1"] = t.replace(line + "\n", "", 1)
    return "13A-03"


def fx_status_reverted(T):
    T["ai_context"] = T["ai_context"].replace("stage_2_next_prompt: 13B", "stage_2_next_prompt: 12C", 1)
    return "13A-26"


def fx_conflict_marker(T):
    T["doc4"] = T["doc4"] + "\n<<<<<<< HEAD\nlocal edit\n=======\nowner edit\n>>>>>>>> branch\n"
    return "13A-30"


def fx_pr_row_dropped(T):
    t = T["doc2"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-PR-16`") or l.startswith("| 13A-PR-16"))
    T["doc2"] = t.replace(line + "\n", "", 1)
    return "13A-10"


def fx_boundary_removed(T):
    T["doc4"] = T["doc4"].replace("no CSS, no framework, no component implementation",
                                  "CSS and framework are recorded as 13B inputs")
    return "13A-16"


def fx_overclaim(T):
    T["doc4"] = (T["doc4"] + "\nThe UI framework has been implemented and accessibility "
                               "conformance verified against WCAG.\n")
    return "13A-32"


def fx_ui_key_split(T):
    T["progress"] = T["progress"].replace(
        "ui_foundations: Prompt 13A complete", "ui_foundations: Prompt 13B pending", 1)
    return "13A-26"


def fx_broken_link(T):
    T["doc1"] = T["doc1"].replace("(13A_ui_design_principles_and_architecture.md)",
                                  "(13A_ui_design_principles_and_architectur.md)", 1)
    return "13A-31"


def fx_decision_missing(T):
    t = T["decisions"]
    line = next(l for l in t.splitlines() if l.startswith("| D-201 |"))
    T["decisions"] = t.replace(line + "\n", "", 1)
    return "13A-25"


def fx_dangling_family_ref(T):
    T["doc3"] = T["doc3"] + "\nSee `SCR-141` for the omitted surface.\n"
    return "13A-24"


# --- Prompt 13A-C1 15 semantic/structural regression fixtures ---

def fx_sem_wrong_dr_citation(T):
    T["doc2"] = T["doc2"].replace("(`13A-DR-006`)", "(`13A-DR-005`)", 1)
    return "13A-33"


def fx_sem_wrong_bp_citation(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-002`"))
    T["doc3"] = t.replace(line, line.replace("13A-BP-014", "13A-BP-016"), 1)
    return "13A-33"


def fx_sem_wrong_src_citation(T):
    t = T["decisions"]
    line = next(l for l in t.splitlines() if l.startswith("| D-202 |"))
    T["decisions"] = t.replace(line, line.replace("13A-SRC-036", "13A-SRC-035"), 1)
    return "13A-33"


def fx_sem_wrong_fnd_citation(T):
    t = T["doc4"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-DS-10`"))
    T["doc4"] = t.replace(line, line.replace("`13A-FND-017/031`", "`13A-FND-037`"), 1)
    return "13A-33"


def fx_sem_compound_second_invalid(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-088`"))
    T["doc3"] = t.replace(line, line.replace("`13A-BP-012`, `13A-DR-014`", "`13A-BP-012/035`"), 1)
    return "13A-24"


def fx_sem_unsupported_suffix(T):
    T["doc2"] = T["doc2"] + "\nCross-check `13A-DR-006x` for unsupported suffix rejection.\n"
    return "13A-04"


def fx_sem_wrong_identifier_family(T):
    T["doc3"] = T["doc3"] + "\nInvalid family token `13A-SCR-013` must be rejected.\n"
    return "13A-04"


def fx_sem_claim_to_source_overreach(T):
    t = T["doc1"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-FND-031`"))
    T["doc1"] = t.replace(line, "| `13A-FND-031` | Colour-only affiliation encoding with no observed non-colour channel | `13A-SRC-002/005/007` | OBSERVED |", 1)
    return "13A-34"


def fx_sem_valid_single_ref_accepted(T):
    T["doc2"] = T["doc2"] + "\nNote confirming valid single reference `13A-DR-006` passes cleanly.\n"
    return "PASS_CONTROL"


def fx_sem_valid_multi_ref_accepted(T):
    T["doc4"] = T["doc4"] + "\nNote confirming valid compound reference `13A-FND-017/031` passes cleanly.\n"
    return "PASS_CONTROL"


def fx_sem_scr_table_mismatch(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-056`"))
    T["doc3"] = t.replace(line, line.replace("`13A-SRC-021`, `13A-DR-022`", "`13A-BP-010`"), 1)
    return "13A-33"


def fx_sem_ur_table_mismatch(T):
    t = T["doc5"]
    line = next(l for l in t.splitlines() if l.startswith("| UR-028 |"))
    T["doc5"] = t.replace(line, line.replace("`13A-DR-013`, `13A-FND-010`", "`13A-DR-018`"), 1)
    return "13A-33"


def fx_sem_decision_row_mismatch(T):
    t = T["decisions"]
    line = next(l for l in t.splitlines() if l.startswith("| D-203 |"))
    T["decisions"] = t.replace(line, line.replace("`13A-FND-017`; `13A-FND-031`", "`13A-FND-037`"), 1)
    return "13A-33"


def fx_sem_dr_internal_linkage(T):
    t = T["doc1"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-DR-021`"))
    T["doc1"] = t.replace(line, line.replace("WAR-149", "`13A-BP-017`; WAR-149"), 1)
    return "13A-34"


def fx_sem_ur_system_mismatch(T):
    t = T["doc5"]
    line = next(l for l in t.splitlines() if l.startswith("| UR-016 |"))
    T["doc5"] = t.replace(line, line.replace("| B-09 |", "| B-99 |"), 1)
    return "13A-33"


# --- Prompt 13A-C1-R1 16 allowlist & independent-accessibility regression fixtures ---

def fx_c1r1_bp022_bypass_on_pr02(T):
    """Exact reproduced Prompt 13A-C1-R1 mutation: unrelated existing BP-022 added to 13A-PR-02."""
    t = T["doc2"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-PR-02`"))
    T["doc2"] = t.replace(line, line.replace("13A-FND-003/027", "13A-FND-003/027, 13A-BP-022"), 1)
    return "13A-33"


def fx_c1r1_ur010_citing_fnd013(T):
    t = T["doc5"]
    line = next(l for l in t.splitlines() if l.startswith("| UR-010 |"))
    T["doc5"] = t.replace(line, line.replace("`13A-DS-07`", "`13A-FND-013`, `13A-DS-07`"), 1)
    return "13A-33"


def fx_c1r1_ur010_citing_fnd028(T):
    t = T["doc5"]
    line = next(l for l in t.splitlines() if l.startswith("| UR-010 |"))
    T["doc5"] = t.replace(line, line.replace("`13A-DS-07`", "`13A-FND-028`, `13A-DS-07`"), 1)
    return "13A-33"


def fx_c1r1_ds07_citing_fnd013(T):
    t = T["doc4"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-DS-07`"))
    T["doc4"] = t.replace(line, line.replace("`13A-PR-14`", "`13A-FND-013`, `13A-PR-14`"), 1)
    return "13A-33"


def fx_c1r1_ds07_citing_fnd028(T):
    t = T["doc4"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-DS-07`"))
    T["doc4"] = t.replace(line, line.replace("`13A-PR-14`", "`13A-FND-028`, `13A-PR-14`"), 1)
    return "13A-33"


def fx_c1r1_extra_bp_citation(T):
    t = T["doc2"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-PR-04`"))
    T["doc2"] = t.replace(line, line.replace("`13A-DR-010`", "`13A-DR-010`, `13A-BP-016`"), 1)
    return "13A-33"


def fx_c1r1_extra_dr_citation(T):
    t = T["doc2"]
    line = next(l for l in t.splitlines() if l.startswith("- `suppressed`"))
    T["doc2"] = t.replace(line, line.replace("`13A-DR-006`", "`13A-DR-006`, `13A-DR-023`"), 1)
    return "13A-33"


def fx_c1r1_extra_src_citation(T):
    t = T["decisions"]
    line = next(l for l in t.splitlines() if l.startswith("| D-202 |"))
    T["decisions"] = t.replace(line, line.replace("`13A-SRC-036`", "`13A-SRC-036`; `13A-SRC-014`"), 1)
    return "13A-33"


def fx_c1r1_valid_indep_a11y_no_research(T):
    """Positive control: DS-07 and UR-010 carry INDEPENDENT_ACCESSIBILITY_REQUIREMENT with zero P&W citations."""
    return "PASS_CONTROL"


def fx_c1r1_valid_multi_allowed_citations(T):
    """Positive control: UR-009 / D-203 multiple explicitly allowlisted citations pass cleanly."""
    return "PASS_CONTROL"


def fx_c1r1_valid_src_to_fnd(T):
    """Positive control: explicit source-to-finding mappings in doc1 pass cleanly."""
    return "PASS_CONTROL"


def fx_c1r1_compound_missing_second(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-088`"))
    T["doc3"] = t.replace(line, line.replace("`13A-BP-012`", "`13A-BP-012/099`"), 1)
    return "13A-24"


def fx_c1r1_unsupported_suffix(T):
    T["doc3"] = T["doc3"] + "\nReject unsupported suffix token `SCR-088b`.\n"
    return "13A-04"


def fx_c1r1_wrong_citation_family(T):
    T["doc4"] = T["doc4"] + "\nReject wrong-family citation token `13A-OVL-01`.\n"
    return "13A-04"


def fx_c1r1_extra_citation_in_screen(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-029`"))
    T["doc3"] = t.replace(line, line.replace("`13A-BP-026`", "`13A-BP-026`, `13A-BP-022`"), 1)
    return "13A-33"


def fx_c1r1_extra_citation_in_requirement(T):
    t = T["doc5"]
    line = next(l for l in t.splitlines() if l.startswith("| UR-007 |"))
    T["doc5"] = t.replace(line, line.replace("`13A-DR-009`", "`13A-DR-009`, `13A-DR-023`"), 1)
    return "13A-33"


def _mutate_ur010_s21(T, old: str, new: str) -> None:
    parts = T["doc5"].split("### 2.2", 1)
    line = next(l for l in parts[0].splitlines() if l.startswith("| UR-010 |"))
    parts[0] = parts[0].replace(line, line.replace(old, new, 1), 1)
    T["doc5"] = "### 2.2".join(parts)


def _mutate_ur010_s22(T, old: str, new: str) -> None:
    parts = T["doc5"].split("### 2.2", 1)
    line = next(l for l in parts[1].splitlines() if l.startswith("| UR-010 |"))
    parts[1] = parts[1].replace(line, line.replace(old, new, 1), 1)
    T["doc5"] = "### 2.2".join(parts)


def fx_c1r2_ur010_citing_dmp268(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `DMP-268`")
    return "13A-33"


def fx_c1r2_ur010_citing_war148(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `WAR-148`")
    return "13A-33"


def fx_c1r2_ur010_citing_all161(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `ALL-161`")
    return "13A-33"


def fx_c1r2_ur010_citing_ax18(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `AX-18`")
    return "13A-33"


def fx_c1r2_ur010_s22_citing_dmp268(T):
    _mutate_ur010_s22(T, "DS-07", "DS-07, `DMP-268`")
    return "13A-33"


def fx_c1r2_ur010_citing_other_namespaces(T):
    _mutate_ur010_s21(
        T, "`DMP-164`",
        "`DMP-164`, `TR-089`, `ECN-177`, `URB-152`, `MKT-053`, `DIP-030`, `WEP-324`, `MOD-002`",
    )
    return "13A-33"


def fx_c1r2_pass_ur010_ds07_dmp164_req321(T):
    """Positive control: DMP-164 and REQ-321 remain valid independent accessibility dependencies."""
    return "PASS_CONTROL"


def fx_c1r2_pass_valid_legacy_deps(T):
    """Positive control: allowlisted WAR/ALL/AX/MKT/ECN/F-PD dependencies pass cleanly."""
    return "PASS_CONTROL"


def fx_c1r2_pass_valid_mixed_modern_legacy(T):
    """Positive control: valid mixed modern 13A-* + legacy citations pass cleanly."""
    return "PASS_CONTROL"


def fx_c1r2_nonexistent_legacy_id(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `DMP-999`, `AX-99`")
    return "13A-33"


def fx_c1r2_wrong_legacy_namespace(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `ACC-001`")
    return "13A-33"


def fx_c1r2_compound_invalid_second(T):
    t = T["doc5"]
    line = next(l for l in t.splitlines() if l.startswith("| UR-015 |") and "WAR-148" in l)
    T["doc5"] = t.replace(line, line.replace("WAR-148", "WAR-148/999"), 1)
    return "13A-33"


def fx_c1r2_compound_unrelated_all_war(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `WAR-148/ALL-161`")
    return "13A-33"


def fx_c1r2_bad_legacy_suffix(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164x`")
    return "13A-04"


def fx_c1r2_duplicate_legacy_citation(T):
    _mutate_ur010_s21(T, "`DMP-164`", "`DMP-164`, `DMP-164`")
    return "13A-33"


def fx_c1r2_valid_plus_unrelated_pair(T):
    _mutate_ur010_s22(T, "DS-07", "DS-07, `DMP-164`, `WAR-148`")
    return "13A-33"


def fx_c1r2_ds07_citing_dmp268(T):
    t = T["doc4"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-DS-07` |"))
    T["doc4"] = t.replace(line, line.replace("`DMP-164`", "`DMP-164`, `DMP-268`"), 1)
    return "13A-33"


def fx_c1r2_ds07_citing_ax18(T):
    t = T["doc4"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-DS-07` |"))
    T["doc4"] = t.replace(line, line.replace("`DMP-164`", "`DMP-164`, `AX-18`"), 1)
    return "13A-33"


def fx_c1r2_scr029_citing_war148(T):
    t = T["doc3"]
    line = next(l for l in t.splitlines() if l.startswith("| `SCR-029`"))
    T["doc3"] = t.replace(line, line.replace("ECN-176/177/178", "ECN-176/177/178, `WAR-148`"), 1)
    return "13A-33"


def fx_c1r2_pr02_citing_all161(T):
    t = T["doc2"]
    line = next(l for l in t.splitlines() if l.startswith("| `13A-PR-02` |"))
    T["doc2"] = t.replace(line, line.replace("DP-004", "DP-004, `ALL-161`"), 1)
    return "13A-33"


def fx_c1r2_req_range_overreach(T):
    _mutate_ur010_s21(T, "`REQ-321`", "`REQ-321\u2013322`")
    return "13A-33"


SELF_TEST_FIXTURES = (
    fx_dup_scr, fx_gate_swap, fx_class_flip, fx_fake_req, fx_src_removed, fx_status_reverted,
    fx_conflict_marker, fx_pr_row_dropped, fx_boundary_removed, fx_overclaim, fx_ui_key_split,
    fx_broken_link, fx_decision_missing, fx_dangling_family_ref,
    fx_sem_wrong_dr_citation, fx_sem_wrong_bp_citation, fx_sem_wrong_src_citation,
    fx_sem_wrong_fnd_citation, fx_sem_compound_second_invalid, fx_sem_unsupported_suffix,
    fx_sem_wrong_identifier_family, fx_sem_claim_to_source_overreach,
    fx_sem_valid_single_ref_accepted, fx_sem_valid_multi_ref_accepted,
    fx_sem_scr_table_mismatch, fx_sem_ur_table_mismatch, fx_sem_decision_row_mismatch,
    fx_sem_dr_internal_linkage, fx_sem_ur_system_mismatch,
    fx_c1r1_bp022_bypass_on_pr02,
    fx_c1r1_ur010_citing_fnd013, fx_c1r1_ur010_citing_fnd028,
    fx_c1r1_ds07_citing_fnd013, fx_c1r1_ds07_citing_fnd028,
    fx_c1r1_extra_bp_citation, fx_c1r1_extra_dr_citation, fx_c1r1_extra_src_citation,
    fx_c1r1_valid_indep_a11y_no_research, fx_c1r1_valid_multi_allowed_citations, fx_c1r1_valid_src_to_fnd,
    fx_c1r1_compound_missing_second, fx_c1r1_unsupported_suffix, fx_c1r1_wrong_citation_family,
    fx_c1r1_extra_citation_in_screen, fx_c1r1_extra_citation_in_requirement,
    fx_c1r2_ur010_citing_dmp268, fx_c1r2_ur010_citing_war148,
    fx_c1r2_ur010_citing_all161, fx_c1r2_ur010_citing_ax18,
    fx_c1r2_ur010_s22_citing_dmp268, fx_c1r2_ur010_citing_other_namespaces,
    fx_c1r2_pass_ur010_ds07_dmp164_req321, fx_c1r2_pass_valid_legacy_deps,
    fx_c1r2_pass_valid_mixed_modern_legacy,
    fx_c1r2_nonexistent_legacy_id, fx_c1r2_wrong_legacy_namespace,
    fx_c1r2_compound_invalid_second, fx_c1r2_compound_unrelated_all_war,
    fx_c1r2_bad_legacy_suffix, fx_c1r2_duplicate_legacy_citation,
    fx_c1r2_valid_plus_unrelated_pair,
    fx_c1r2_ds07_citing_dmp268, fx_c1r2_ds07_citing_ax18,
    fx_c1r2_scr029_citing_war148, fx_c1r2_pr02_citing_all161,
    fx_c1r2_req_range_overreach,
)


def main(argv: list[str]) -> int:
    # Windows consoles default to cp1252; the registers quote French/emoji-free but
    # typographic punctuation (— § ≤), so reporting must never crash on encoding.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    T = load()
    if "--self-test" in argv:
        bad = 0
        by_id = {cid: (name, fn) for cid, name, fn in CHECKS}
        for fx in SELF_TEST_FIXTURES:
            mutated = dict(T)
            expected = fx(mutated)
            results = run(mutated)
            caught = [cid for cid, _, probs in results if probs]
            if expected == "PASS_CONTROL":
                ok = len(caught) == 0
                detail = "valid reference accepted cleanly" if ok else f"unexpected failure: {caught}"
            else:
                ok = expected in caught
                detail = next((by_id[cid][1](mutated)[0][:110] for cid in caught if cid == expected), "undetected")
            print(f"SELF-TEST {'PASS' if ok else 'FAIL'}  {fx.__name__} -> "
                  f"expected {expected}: {detail}")
            bad += 0 if ok else 1
        print(f"SELF-TEST: {len(SELF_TEST_FIXTURES) - bad}/{len(SELF_TEST_FIXTURES)} regression cases passed")
        return 0 if bad == 0 else 1

    results = run(T)
    failed = [(cid, name, probs) for cid, name, probs in results if probs]
    print("13A UI-foundations validator — documentation quality only")
    print(f"CHECKS: {len(results) - len(failed)}/{len(results)} passed; {len(failed)} failed")
    for cid, name, probs in failed:
        print(f"\nFAILED {cid}: {name}")
        for pr in probs[:12]:
            print(f"  - {pr}")
        if len(probs) > 12:
            print(f"  - … {len(probs) - 12} more")
    if not failed:
        print("RESULT: PASS at the documentation level. No screen, component, framework, "
              "migration or implementation exists, and no Prompt 13A gate is evidence of one.")
        return 0
    print("\nRESULT: FAIL — Prompt 13A documentation-quality checks not satisfied")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
