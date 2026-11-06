#!/usr/bin/env python3
"""Document checks for B-08 (diplomacy) and its formula register.

Prompt 08B-C exists because the B-08 pair contained seven confirmed defects:
a stale `15_alliances.md` reference, two competing same-turn orders, an
ordered/unordered pair muddle, freeze omissions in the timing formulas, a
wrong rolling-window example, an incomplete posture matrix and a wrong
cross-reference. Prompt 08B-D added a ninth group for three freeze-aware
cooldowns (F-DP-005/007/008): each must name its base duration, its exact
three-argument interval and its freeze extension, and the §3 limits table must
agree. The semantic validators could not see any of them, because they checked
registers and continuity, not diplomacy rules.

This script checks the *corrected semantics* against the saved files. It is a
documentation checker: no game code exists to run (D-012), so nothing here is a
runtime, load or security test.

Usage:
    python3 verify_diplomacy_numbers.py [--self-test]

Documentation QA only; standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
B08 = DOCS / "stage-2" / "15_diplomacy.md"
REG = DOCS / "stage-2" / "15_diplomacy_formula_register.md"
ROADMAP_REG = DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md"
OUTLINE = DOCS / "stage-2" / "02_master_game_design_bible_outline.md"
DECISIONS = DOCS / "DECISIONS.md"

POSTURES = ("FRIENDLY", "NEUTRAL", "TENSE", "HOSTILE")

checks: list[tuple[bool, str, str]] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append((bool(ok), label, detail))


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rule_defs(text: str) -> set[str]:
    return set(re.findall(r"^\*\*DIP-(\d{3}[a-z]?)", text, re.M)) | set(
        re.findall(r"^\| \*\*DIP-(\d{3}[a-z]?)\*\*", text, re.M)
    )


def entry_block(text: str, heading: str) -> str:
    """One register entry: its heading up to the next `### ` heading."""
    start = text.index(heading)
    nxt = text.find("\n### ", start + len(heading))
    return text[start:] if nxt < 0 else text[start:nxt]


def limit_row(reg: str, label: str) -> str:
    """The §3 consolidated-limits row for one label, or empty."""
    for line in reg.splitlines():
        if line.startswith(f"| {label} |"):
            return line
    return ""


def posture_pairs(text: str) -> set[tuple[str, str]]:
    """Ordered (from, to) pairs in the §4.2 table, ignoring the guard rows."""
    start = text.index("### 4.2 Posture transition table")
    end = text.index("**DIP-031", start)
    found: set[tuple[str, str]] = set()
    for line in text[start:end].splitlines():
        m = re.match(r"\|\s*T\d+\s*\|\s*`(\w+)`\s*\|\s*`(\w+)`\s*\|", line)
        if m:
            found.add((m.group(1), m.group(2)))
    return found


def format_problems(b08: str, reg: str) -> list[str]:
    problems: list[str] = []

    # 1. Structure and identifiers.
    sections = [int(n) for n in re.findall(r"^## (\d+)\. ", b08, re.M)]
    if sections != list(range(1, 23)):
        problems.append(f"B-08 sections are not 1..22: {sections}")
    defs = rule_defs(b08)
    numeric = sorted(int(d) for d in defs if d.isdigit())
    expected = list(range(1, 158))
    if numeric != expected:
        missing = [n for n in expected if n not in numeric]
        extra = [n for n in numeric if n > 157]
        problems.append(f"DIP numeric IDs incomplete: missing {missing[:5]}, extra {extra[:5]}")
    if "039a" not in defs:
        problems.append("DIP-039a is not defined")
    refs = set(re.findall(r"DIP-(\d{3}[a-z]?)", b08)) | set(re.findall(r"DIP-(\d{3}[a-z]?)", reg))
    undefined = sorted(refs - defs)
    if undefined:
        problems.append(f"undefined DIP references: {undefined[:5]}")
    dpf = sorted({int(n) for n in re.findall(r"DPF-(\d{2})", b08)})
    if dpf != list(range(1, 16)):
        problems.append(f"DPF codes are not 01..15: {dpf}")
    examples = [int(n) for n in re.findall(r"^### E(\d+) ", b08, re.M)]
    if examples != list(range(1, 13)):
        problems.append(f"worked examples are not E1..E12: {examples}")
    fdp = sorted({int(n) for n in re.findall(r"F-DP-(\d{3})", reg)})
    if fdp != list(range(1, 13)):
        problems.append(f"formula register is not F-DP-001..012: {fdp}")

    # 2. Prompt 09 filename.
    reg_roadmap = rd(ROADMAP_REG)
    if re.search(r"\|\s*`15_alliances\.md`\s*\|", reg_roadmap):
        problems.append("stage-2 register still lists 15_alliances.md as the Prompt 09 deliverable")
    if not re.search(r"\|\s*09\s*\|[^\n]*16_alliances\.md", reg_roadmap):
        problems.append("stage-2 register row 09 does not name 16_alliances.md")
    if "16_alliances.md" not in rd(ROADMAP_REG):
        problems.append("stage-2 register does not name 16_alliances.md")
    if "16_alliances.md" not in rd(OUTLINE):
        problems.append("outline does not name 16_alliances.md")
    if "16_alliances.md" not in rd(DECISIONS):
        problems.append("D-132 does not record 16_alliances.md")

    # 3. One authoritative same-turn order: expiry/termination, breach,
    #    activation, scheduled delivery, embargo.
    order = ["EXPIRY_AND_TERMINATION", "BREACH", "ACTIVATION", "SCHEDULED_OBLIGATION", "EMBARGO"]
    band = b08[b08.index("**DIP-103") : b08.index("**DIP-104")]
    positions = [band.find(f"`{step}`") for step in order]
    if any(p < 0 for p in positions) or positions != sorted(positions):
        problems.append(f"DIP-103 does not list the five steps in order: {positions}")
    p4 = b08[b08.index("| **P4 "): b08.index("| **P6 ")]
    if not all(step in p4 or step.lower().replace("_", " ") in p4.lower() for step in order):
        # P4 states the steps in prose; require the five names explicitly
        missing = [s for s in order if s not in p4]
        if missing:
            problems.append(f"DIP-101 P4 does not name the five steps: {missing}")
    if re.search(r"`?ACTIVATION`?\s+before\s+`?BREACH`?", b08):
        problems.append("B-08 still says activation precedes breach")
    if "Delivery is ordered before breach" in b08:
        problems.append("B-08 still contains the contradictory delivery/breach sentence")
    if "Step 2 (`BREACH`) precedes step 4" not in b08:
        problems.append("DIP-131 does not state the corrected break-before-delivery order")

    # 4. Directed proposals, unordered agreements.
    if "(from_nation, to_nation, type, PENDING)" not in b08:
        problems.append("DIP-124 does not key proposals by ordered from/to")
    if "({nation_a, nation_b}, type, ACCEPTED|ACTIVE)" not in b08:
        problems.append("DIP-124 does not key agreements by unordered pair")
    f2 = reg[reg.index("### F-DP-002") : reg.index("### F-DP-003")]
    if "p.from = from and p.to = to" not in f2:
        problems.append("F-DP-002 does not use an ordered proposal key")
    if "unordered" not in f2:
        problems.append("F-DP-002 does not distinguish the unordered agreement key")
    if "p.pair = pair" in f2:
        problems.append("F-DP-002 still uses an unordered proposal pair")
    if "**Reciprocal variant (same turns).**" not in b08:
        problems.append("E1 has no reciprocal-proposal worked example")

    # 5. Freeze arithmetic.
    for pid, token in (("F-DP-004", "frozen_pair"), ("F-DP-006", "frozen_pair"),
                       ("F-DP-009", "frozen_pair")):
        block = reg[reg.index(f"### {pid}") : reg.index("### F-DP-", reg.index(f"### {pid}") + 5)]
        if token not in block:
            problems.append(f"{pid} does not apply {token}")
    if "frozen_turns(actor" not in reg[reg.index("### F-DP-006") : reg.index("### F-DP-007")]:
        problems.append("F-DP-006b does not apply the actor freeze to the notice cooldown")
    if "frozen_turns(imposer" not in reg[reg.index("### F-DP-008") : reg.index("### F-DP-009")]:
        problems.append("F-DP-008 does not apply the imposer freeze to re-imposition")
    f8 = reg[reg.index("### F-DP-008") : reg.index("### F-DP-009")]
    if "freeze-aware" not in f8 or "**not**" not in f8:
        problems.append("F-DP-008 does not state that the embargo term is not freeze-aware")
    if "**Not extended, deliberately:**" not in b08:
        problems.append("DIP-105 has no explicit not-extended list")
    for word in ("embargo's 24-turn term", "12-turn minimum", "strictly before expiry", "Dormancy"):
        if word not in b08[b08.index("**DIP-105") : b08.index("**DIP-106")]:
            problems.append(f"DIP-105 exception missing: {word}")

    # 6. Rolling-window example.
    f10 = reg[reg.index("### F-DP-010") : reg.index("### F-DP-011")]
    if "4480" not in f10:
        problems.append("F-DP-010 example does not use current turn 4480")
    if "4480 \u2212 4380 = 100" not in f10 and "4480 - 4380 = 100" not in f10:
        problems.append("F-DP-010 example does not show the lower bound 100")
    if "at 100 is **excluded**" not in f10:
        problems.append("F-DP-010 example does not exclude the breach at 100")

    # 7. Complete posture matrix.
    pairs = posture_pairs(b08)
    wanted = {(a, b) for a in POSTURES for b in POSTURES if a != b}
    missing = sorted(wanted - pairs)
    if missing:
        problems.append(f"posture matrix is missing {missing}")
    extra = sorted(p for p in pairs if p[0] not in POSTURES or p[1] not in POSTURES)
    if extra:
        problems.append(f"posture matrix has unknown states {extra}")
    if "T3, T6 and T9" not in b08:
        problems.append("DIP-031 does not name every transition to HOSTILE")

    # 8. Cross-reference and player authority.
    d061 = next((ln for ln in b08.splitlines() if ln.startswith("**DIP-061")), "")
    if "DIP-127" not in d061 or "DIP-130" in d061:
        problems.append("DIP-061 does not point reroll cleanup at DIP-127")
    for phrase in ("**DIP-013 \u2014 Sole authority.**", "**DIP-015 \u2014 No delegation in B-08.**",
                   "**DIP-019 \u2014 The system never accepts",
                   "**DIP-020 \u2014 Automatic acts are a closed list.**",
                   "**DIP-062 \u2014 Consent is not silence.**"):
        if phrase not in b08:
            problems.append(f"player-authority rule missing: {phrase}")
    if ("auto-accepting an incoming proposal" not in b08
            or "declaring war or an embargo for a player" not in b08):
        problems.append("DIP-019's no-autonomous-decision list is missing")

    # 9. Freeze-aware cooldowns: the extension is named and its interval is explicit.
    # Prompt 08B-D: F-DP-005 and F-DP-007 read `frozen_turns(actor)` with no
    # interval while the function takes three arguments, and the §3 limits rows
    # still described the three cooldowns as fixed durations. Neither the
    # registers nor the continuity validators could see it.
    for pid, entry, base, who, interval, phrase in (
        ("F-DP-005", entry_block(reg, "### F-DP-005"), "12", "actor",
         "frozen_turns(actor, last_posture_change_turn, t)",
         "the actor's own freeze extension"),
        ("F-DP-007", entry_block(reg, "### F-DP-007"), "36", "actor",
         "frozen_turns(actor, breach_turn, t)",
         "the breaker's own freeze extension"),
        ("F-DP-008", entry_block(reg, "### F-DP-008"), "12", "imposer",
         "frozen_turns(imposer, end_turn, t)",
         "the imposer's freeze extension"),
    ):
        if f"{base}-turn base" not in entry:
            problems.append(f"{pid} does not state the {base}-turn base duration")
        if interval not in entry:
            problems.append(f"{pid} does not count freeze over the explicit interval {interval}")
        if re.search(rf"frozen_turns\({who}\)", entry):
            problems.append(f"{pid} still uses the one-argument frozen_turns({who})")
        if phrase not in entry:
            problems.append(f"{pid} description does not state {phrase}")
        if "unfrozen" not in entry:
            problems.append(f"{pid} does not say the cooldown counts unfrozen boundaries")

    for label, pid, expected in (
        ("Posture cooldown", "F-DP-005", "+ actor freeze"),
        ("Breach cooldown", "F-DP-007", "+ actor freeze"),
        ("Embargo re-imposition", "F-DP-008", "+ imposer freeze"),
        ("Proposal expiry", "F-DP-004", "+ pair freeze"),
        ("Notice window (validity)", "F-DP-006a", "+ pair freeze"),
        ("Notice cooldown", "F-DP-006b", "+ actor freeze"),
        ("Agreement term", "F-DP-009", "+ pair freeze"),
    ):
        row = limit_row(reg, label)
        if not row:
            problems.append(f"§3 limits has no '{label}' row")
            continue
        if pid not in row:
            problems.append(f"§3 limits row '{label}' does not cite {pid}")
        if expected not in row:
            problems.append(f"§3 limits row '{label}' does not say '{expected}'")
    embargo_term = limit_row(reg, "Embargo term")
    if "24 turns" not in embargo_term:
        problems.append("§3 limits Embargo term row lost its 24-turn value")
    elif "freeze" not in embargo_term and "frozen" not in embargo_term:
        problems.append("§3 limits Embargo term row does not say the term is not freeze-extended")

    for rid in ("DIP-027", "DIP-073"):
        line = next((ln for ln in b08.splitlines() if ln.startswith(f"**{rid}")), "")
        if "freeze" not in line and "frozen" not in line:
            problems.append(f"{rid} does not state its freeze extension")
    d039a = next((ln for ln in b08.splitlines() if ln.startswith("**DIP-039a")), "")
    if "pair freeze" not in d039a:
        problems.append("DIP-039a window does not include the pair freeze")
    if "unfrozen" not in d039a:
        problems.append("DIP-039a cooldown does not count unfrozen boundaries")
    d093 = next((ln for ln in b08.splitlines() if "last embargo on that target ended" in ln), "")
    if "freeze" not in d093 and "frozen" not in d093:
        problems.append("DIP-093 precondition 4 does not state the imposer freeze extension")

    return problems


def run_self_test() -> int:
    b08 = rd(B08)
    reg = rd(REG)
    cases = [
        ("posture gap", lambda t, r: (t.replace("| T12 | `HOSTILE` | `FRIENDLY` |", "| T12x | `HOSTILE` | `FRIENDLY` |"), r), "posture matrix is missing"),
        ("ordered key", lambda t, r: (t, r.replace("p.from = from and p.to = to", "p.pair = pair")), "F-DP-002"),
        ("freeze omission", lambda t, r: (t, r.replace("frozen_pair", "0")), "F-DP-004"),
        ("breach example", lambda t, r: (t, r.replace("4480", "4380")), "F-DP-010"),
        ("cross-reference", lambda t, r: (t.replace("every agreement terminates (DIP-127)", "every agreement terminates (DIP-130)"), r), "DIP-061"),
        ("reciprocal example", lambda t, r: (t.replace("**Reciprocal variant (same turns).**", "Reciprocal note."), r), "reciprocal-proposal worked example"),
        ("order", lambda t, r: (t.replace("| 2 | `BREACH` |", "| 2 | `ACTIVATION` |").replace("| 3 | `ACTIVATION` |", "| 3 | `BREACH` |"), r), "DIP-103"),
        ("filename", lambda t, r: (t, r), "15_alliances.md"),
        # Added 2026-10-30 (08B-D): the three cooldown formulas and their limits rows.
        ("F-DP-005 interval", lambda t, r: (t, r.replace(
            "frozen_turns(actor, last_posture_change_turn, t)", "frozen_turns(actor)")), "F-DP-005"),
        ("F-DP-005 summary", lambda t, r: (t, r.replace(
            "| Posture cooldown | F-DP-005 | 12 turns **+ actor freeze** |",
            "| Posture cooldown | F-DP-005 | 12 turns |")), "Posture cooldown"),
        ("F-DP-007 no freeze", lambda t, r: (t, r.replace(
            "frozen_turns(actor, breach_turn, t)", "")), "F-DP-007"),
        ("F-DP-007 partial interval", lambda t, r: (t, r.replace(
            "frozen_turns(actor, breach_turn, t)", "frozen_turns(actor, breach_turn)")), "F-DP-007"),
        ("F-DP-008 summary", lambda t, r: (t, r.replace(
            "| Embargo re-imposition | F-DP-008 | 12 turns **+ imposer freeze** |",
            "| Embargo re-imposition | F-DP-008 | 12 turns |")), "Embargo re-imposition"),
        ("limits disagree with formula", lambda t, r: (t, r.replace(
            "| Posture cooldown | F-DP-005 | 12 turns **+ actor freeze** |",
            "| Posture cooldown | F-DP-005 | 12 turns **+ imposer freeze** |")), "Posture cooldown"),
    ]
    failures = 0
    for name, mutate, expected in cases:
        if name == "filename":
            saved = rd(ROADMAP_REG)
            try:
                ROADMAP_REG.write_text(saved + "\n| 09 | Alliances | `15_alliances.md` | Pending |\n", encoding="utf-8")
                problems = format_problems(b08, reg)
            finally:
                ROADMAP_REG.write_text(saved, encoding="utf-8")
        else:
            t2, r2 = mutate(b08, reg)
            problems = format_problems(t2, r2)
        hit = any(expected in p for p in problems)
        print(f"SELFTEST {'PASS' if hit else 'FAIL'}  {name} -> {(problems or ['undetected'])[0][:100]}")
        failures += 0 if hit else 1
    clean = format_problems(b08, reg)
    print(f"SELFTEST {'PASS' if not clean else 'FAIL'}  corrected files -> {(clean or ['no problems'])[0][:100]}")
    failures += 0 if not clean else 1
    total = len(cases) + 1
    if failures:
        print(f"SELFTEST: {failures} of {total} checks failed")
        return 2
    print(f"SELFTEST: {total}/{total} checks pass ({len(cases)} defect guards + 1 clean fixture)")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return run_self_test()
    problems = format_problems(rd(B08), rd(REG))
    if problems:
        print("\nB-08 CONSISTENCY FAILURES:")
        for p in problems:
            print("  -", p)
        return 1
    print("\nB-08 CONSISTENCY: 9 groups checked (structure, filenames, same-turn order, "
          "proposal/agreement keys, freeze arithmetic, rolling window, posture matrix, "
          "cross-reference and authority, freeze-aware cooldowns and limits), 0 failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
