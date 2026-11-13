#!/usr/bin/env python3
"""Current cross-file validator for the Project X Stage 1 document set.

History: this started as a point-in-time checker written at the end of the
Prompt 8 correction pass. Its original assertions expected Prompt 9 to be
"not started" and no 09 report to exist, so it reported four stale failures
once the owner authorized and executed Prompt 9. On 2026-10-23 it was
re-purposed: the stale expectations were replaced with the actual nine-prompt
executed-sequence state, and the valid checks were retained unchanged.

It validates documents only. It is not a game test, not a security test, and
not evidence that any proposed control works.

Scope note (2026-10-23, Prompt 10): the "no production code" assertion used to
mean "no code exists anywhere in the project". Prompt 10 authorises a bounded,
labelled feasibility spike, so the assertion now means what it was for: no code
in the research deliverables or at the project root. Only
`prototypes/` (with its dependencies and build output) is exempt, and the
prototype contains no gameplay code.

Run from anywhere: paths resolve relative to this file.
"""

from __future__ import annotations

import glob
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # keep the repo free of __pycache__
# Keep a failure message readable if it quotes a non-ASCII label ("₹", "…").
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_rules import (  # noqa: E402  (document-QA helper)
    COMPLETED_SUBPROMPTS,
    stale_next_actions,
    subprompt_status_problems,
)

DOCS = Path(__file__).resolve().parents[1]
ROOT = DOCS.parent

fail: list[str] = []


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


# --- Stage 2 reference guards (2026-10-28 cross-document reconciliation) ---

def version_reference_problems(lines, current):
    """Current-status rows that cite the B-06 register must cite its version."""
    problems = []
    for label, line in lines:
        if not line:
            problems.append(f"{label}: current B-06 register row not found")
            continue
        if "12_population_and_domestic_politics_formula_register.md" not in line:
            problems.append(f"{label}: does not link the B-06 formula register")
        versions = re.findall(r"\bv(\d+\.\d+)\b", line)
        if current not in versions:
            problems.append(
                f"{label}: register cited as {sorted(set(versions)) or 'no version'}, current v{current}")
    return problems


def roadmap_log_problems(row, log_text, all_rows=None):
    """Roadmap rows must cite real log sections; the latest section must be cited somewhere.

    The earlier form assumed the Prompt 06 row ended at the newest log section.
    That stopped being true when Prompt 07A added §20, so the check now verifies
    the row's own citations and requires the roadmap as a whole to reach the
    latest section. It is not weaker: every row passed in is still checked, and
    an uncited newest section still fails.
    """
    problems = []
    refs = [int(n) for n in re.findall(r"§(\d+)", row)]
    sections = [int(n) for n in re.findall(r"^## (\d+)\. ", log_text, re.M)]
    if not refs:
        return ["roadmap Prompt 06 row has no progress-log section reference"]
    for n in refs:
        if n not in sections:
            problems.append(f"roadmap cites log §{n}, which does not exist")
    if all_rows is not None and sections:
        cited = {int(n) for line in all_rows for n in re.findall(r"§(\d+)", line)}
        latest = max(sections)
        if latest not in cited:
            problems.append(f"no roadmap row cites the latest log §{latest}")
    elif sections and max(refs) != max(sections):
        problems.append(f"roadmap log range ends at §{max(refs)}, latest is §{max(sections)}")
    return problems


def election_wording_problems(decisions, trace):
    """No current decision or requirement may state the superseded timing."""
    problems = []
    d092 = next((ln for ln in decisions.splitlines() if ln.startswith("| D-092 |")), "")
    d096 = next((ln for ln in decisions.splitlines() if ln.startswith("| D-096 |")), "")
    if "first active `NORMAL`" in d092:
        problems.append("D-092 still postpones a due contest to the first active NORMAL turn")
    if "new administration takes office" in d092:
        problems.append("D-092 still implies a new administration takes office")
    if "campaign_open_turn" not in d092:
        problems.append("D-092 does not state the authoritative campaign opening")
    if "`ELECTORAL` or `SUCCESSION`" not in d092:
        problems.append("D-092 does not state all three resolving states")
    if "campaign_open_turn" not in d096:
        problems.append("D-096 does not qualify the 24-turn ELECTORAL period")
    rows = {}
    for ln in trace.splitlines():
        m = re.match(r"\| (REQ-\d{3}) \|", ln)
        if m:
            rows[m.group(1)] = ln
    checks = (
        ("REQ-328", "office from `T+1`", "campaign_open_turn"),
        ("REQ-332", "arriving as turn `T` opens", "resolution turn"),
        ("REQ-337", "after `T-12`", "registration_close_turn"),
        ("REQ-338", "after `T-12`", "registration_close_turn"),
        ("REQ-356", "at `T-24`", "campaign_open_turn"),
        ("REQ-419", "after `T-12`", "registration_close_turn"),
    )
    for req, bad, good in checks:
        row = rows.get(req, "")
        if not row:
            problems.append(f"{req} is missing from the traceability matrix")
            continue
        if bad in row:
            problems.append(f"{req} still states the superseded timing: {bad}")
        if good not in row:
            problems.append(f"{req} does not name {good}")
    return problems


def handoff_header_problems(header: str) -> list[str]:
    """The stage-2/00 header must not still call a completed sub-prompt "next".

    2026-10-30: the governing status line still said "08B — diplomacy
    foundations — is next" while §10 correctly named 08C.
    `subprompt_status_problems` missed it because the sentence says "is next",
    not "is the next task", which its claim patterns require.
    2026-11-03 (Prompt 10A): the same guard now covers the 09 and 10 families,
    so a header cannot name a completed 10A as the live next sub-prompt.
    """
    problems = []
    for match in re.finditer(r"\b((?:0[789]|10)[A-C])\b([^.;]*?)\bis next\b", header, re.I):
        if match.group(1) not in COMPLETED_SUBPROMPTS:
            continue  # the genuinely next sub-prompt may say so
        tail = match.group(2)
        if re.search(r"historical|superseded|at the time|was the next", tail, re.I):
            continue
        problems.append(f"stage-2/00 header still says {match.group(1)} is next")
    return problems


if "--self-test" in sys.argv:
    fixtures = (
        ("register version", version_reference_problems(
            [("fixture", "[register](12_population_and_domestic_politics_formula_register.md) **v2.3**")],
            "2.4"), "register cited as"),
        ("roadmap section", roadmap_log_problems(
            "| 06 | [log §10](x)–[§15](x) |", "## 10. A\n## 15. B\n## 16. C\n",
            ["| 06 | [log §10](x)–[§15](x) |"]), "no roadmap row cites the latest log §16"),
        ("decision wording", election_wording_problems(
            "| D-092 | postponed to the first active `NORMAL` turn |\n| D-096 | `ELECTORAL` runs 24 turns from `T-24` |",
            ""), "D-092"),
        # Added 2026-10-29: the prompt-number rule cannot see 07B vs 07C.
        ("sub-prompt status", subprompt_status_problems(
            "**Prompt 07B — market foundations is the next intended task** and has not started.\n"),
            "07B"),
        # Added 2026-10-29: the handoff used "next outstanding task is **Prompt
        # 07C", which the old prefix pattern missed because "Prompt" sat
        # between the claim and the number.
        ("next outstanding task prefix", subprompt_status_problems(
            "its next outstanding task is **Prompt 07C — market workflows and "
            "acceptance** (07A research and 07B market foundations are complete).\n"),
            "07C"),
        # Added 2026-10-29: Prompt 08 is split, so 08A joins the completed set
        # and must be caught when a status sentence names it as what is next.
        ("split Prompt 08", subprompt_status_problems(
            "**Prompt 08A — diplomacy research is the next intended task** and "
            "has not started.\n"),
            "08A"),
        # Added 2026-10-30: 08B is complete too, so the rule must catch it.
        ("split Prompt 08B", subprompt_status_problems(
            "**Prompt 08B — diplomacy foundations is the next intended task** "
            "and has not started.\n"),
            "08B"),
        # Added 2026-10-30 (08B-D): the handoff header said "08B ... is next"
        # while §10 named 08C; the "is the next task" patterns missed it.
        ("handoff header says next", handoff_header_problems(
            "**Status:** 08A is complete; 08B — diplomacy foundations — is "
            "next. 08C has not started.\n"),
            "08B is next"),
        # Added 2026-10-30 (08C): 08C is complete too, so the split-prompt
        # guard must catch a status sentence that still names it as next.
        ("split Prompt 08C", subprompt_status_problems(
            "**Prompt 08C — workflows and acceptance is the next intended "
            "task** and has not started.\n"),
            "08C"),
    )
    bad = 0
    for name, found, expected in fixtures:
        ok = any(expected in p for p in found)
        print(f"SELF-TEST {'PASS' if ok else 'FAIL'}  {name} -> {(found or ['undetected'])[0]}")
        bad += 0 if ok else 1
    clean_header = handoff_header_problems(
        "**Status:** 08C — workflows and acceptance — is complete; Prompt 09 "
        "— alliances — is next and has not started.\n")
    print(f"SELF-TEST {'PASS' if not clean_header else 'FAIL'}  handoff header clean "
          f"-> {(clean_header or ['no problems'])[0]}")
    bad += 0 if not clean_header else 1
    total = len(fixtures) + 1
    if bad:
        print(f"SELF-TEST: {bad} of {total} guards failed")
        raise SystemExit(2)
    print(f"SELF-TEST: {total}/{total} guards detect their defect")
    raise SystemExit(0)


ctx = rd(DOCS / "AI_CONTEXT.md")
hnd = rd(DOCS / "AI_HANDOFF.md")
prog = rd(DOCS / "PROJECT_PROGRESS.md")
r8 = rd(DOCS / "stage-1" / "08_security_privacy_fair_play_and_trust.md")
r9 = rd(DOCS / "stage-1" / "09_integrated_design_synthesis_and_readiness_audit.md")
dec = rd(DOCS / "DECISIONS.md")

# 1. Headers updated ---------------------------------------------------------
# 2026-11-04 (Prompt 10C): the header gate used to demand the literal 2026-11-03.
# It now accepts any November date from 2026-11-03 onward so a later work day can
# date its own header; the gate still proves the header was refreshed, and an
# undated or October header still fails.
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)]:
    head = "\n".join(text.splitlines()[:4])
    if not re.search(r"2026-11-0[3-9]|2026-1[12]-\d\d", head):
        fail.append(f"{name}: header not dated on or after 2026-11-03")

# 2. Current status language -------------------------------------------------
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)]:
    required = [
        (r"Prompt 9", "prompt-9 mention"),
        (r"Prompt 9[^.\n]{0,120}(complete|executed|delivered)", "prompt-9 completed"),
        # Disclosure history: the audit's "not complete" language is retained in
        # Report 9, while the continuity files now carry the closed state.
        (r"Stage 1 is[^.\n]{0,10}not complete|Stage 1 is incomplete|Stage 1 NOT complete|Stage 1 is CLOSED|STAGE 1 CLOSED", "stage-1 status"),
        (r"nine[- ]prompt|9 prompts|Prompt 9", "nine-prompt sequence"),
        (r"Prompt 8", "prompt-8 mention"),
        (r"correction|corrected|passed", "prompt-8 correction wording"),
        (r"Prompt 7[^.\n]{0,40}accepted|Prompt 7[^.\n]{0,220}micro-correction|final micro-correction", "prompt-7 micro-correction"),
        (r"conditionally ready", "readiness verdict"),
    ]
    for pattern, label in required:
        if not re.search(pattern, text, re.I):
            fail.append(f"{name}: missing {label}")
    if re.search(r"Prompt 9[^.\n]{0,80}(not started|awaits|awaiting authorization)", text, re.I):
        fail.append(f'{name}: stale "Prompt 9 not started" wording')
    if re.search(r"Prompt 8[^.\n]{0,60}(not started|not begun)", text, re.I):
        fail.append(f'{name}: stale "Prompt 8 not started" wording')

# 2b. QA-vs-production distinction ------------------------------------------
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd)]:
    if re.search(r"no code exists|consists entirely of research", text, re.I):
        fail.append(f"{name}: broad no-code wording remains")
    if not re.search(r"document-QA tooling|QA tooling|document QA", text, re.I):
        fail.append(f"{name}: QA-tooling wording missing")
    if not re.search(r"Production game implementation has not started|implementation has not started", text, re.I):
        fail.append(f"{name}: production-not-started wording missing")

# 3. Prompt 8 correction markers (DEF-004/005/010) ---------------------------
if not re.search(r"\*\*Version:\*\* v1\.1", r8):
    fail.append("08: version header is not v1.1")
r8_154 = r8[r8.index("### 15.4 Which protections"):r8.index("## 16. Security requirements")]
if "16 requirements on stage A" in r8_154:
    fail.append('08 §15.4: stale "16 requirements on stage A" still present as a live claim')
if not re.search(r"\*\*Twelve requirements\*\* are assigned to stage A", r8):
    fail.append("08 §15.4: twelve-requirement correction missing")
if not re.search(r"12 full requirements \(SEC-010/011", r8):
    fail.append("08 §17.1: exact stage-A count note missing")
if not re.search(r"subset of SEC-031", r8):
    fail.append("08 A8: SEC-031 subset wording missing")
if not re.search(r"PL \(money/pipeline spine rows required at A8", r8):
    fail.append("08 §16.2: SEC-031 stage cell not clarified")
if not re.search(r"\*\*Stage-A prevention:\*\*", r8):
    fail.append("08 TH-011: Stage-A prevention wording missing")
if not re.search(r"Residual \(accepted\)", r8):
    fail.append("08 TH-011: accepted residual wording missing")
if not re.search(r"superseded", r8):
    fail.append("08 §26.9: superseded Prompt 9 handoff wording missing")

# 3b. Prompt 8 §25/§26 markers retained from the first pass -------------------
r8sec = r8[r8.index("## 25. Quality assurance record"):r8.index("## 26. Handoff")]
for label in [
    "SEC-009",
    "Correction-pass addendum",
    "validate_final.py",
    "DECISIONS.md was NOT changed",
    "production game implementation has not started",
]:
    if not re.search(re.escape(label), r8sec, re.I):
        fail.append(f"08 §25: missing {label}")

row9 = re.search(r"SEC-009 \|", r8)
if row9:
    blk = r8[row9.start():row9.start() + 700]
    if not any(x in blk for x in ["reserve, not a usage", "deliberately unassigned", "placeholder row"]):
        fail.append("SEC-009 row not labelled as reserve")

# 4. Prompt 9 state ----------------------------------------------------------
if not re.search(r"## Section 20 — Stage 1 readiness gates", r9):
    fail.append("09: readiness-gate section missing")
for gate in ("GATE-13", "GATE-16", "GATE-18"):
    if gate not in r9:
        fail.append(f"09: {gate} missing")
if not re.search(r"\| \*\*Pass\*\* \| \*\*17\*\*", r9):
    fail.append("09: gate tally is not 17 pass")
if not re.search(r"\| \*\*Conditional\*\* \| \*\*3\*\*", r9):
    fail.append("09: gate tally is not 3 conditional")
if "**Fixed 2026-10-23**" not in r9:
    fail.append("09: corrected DEF rows not marked Fixed")
if not re.search(r"DEF-010[^\n]*\*\*Fixed 2026-10-23\*\*", r9):
    fail.append("09: DEF-010 not marked Fixed")
if not re.search(r"GATE-03[^\n]*\| \*\*Pass\*\*", r9):
    fail.append("09: GATE-03 is not marked Pass")
if not re.search(r"conditionally ready", r9, re.I):
    fail.append("09: readiness verdict missing")

# 5. ID registers ------------------------------------------------------------
def ids(text: str, prefix: str) -> set[str]:
    return {v for v in re.findall(prefix + r"-(.{3})", text) if v.isdigit()}


sec, th, st, osq = ids(r8, "SEC"), sorted(ids(r8, "TH")), sorted(ids(r8, "ST")), sorted(ids(r8, "OSQ"))
if not all(("%03d" % i) in sec for i in list(range(1, 9)) + list(range(10, 34))):
    fail.append("SEC register incomplete: " + ",".join(
        x for x in [("%03d" % i) for i in range(1, 34)] if x not in sec))
for label, (got, want) in {
    "TH-001..TH-025": (th, ["%03d" % i for i in range(1, 26)]),
    "ST-001..ST-020": (st, ["%03d" % i for i in range(1, 21)]),
    "OSQ-001..OSQ-012": (osq, ["%03d" % i for i in range(1, 13)]),
}.items():
    if got != want:
        fail.append(f"{label}: mismatch")

w = sorted(set(re.findall(r"W-18-([A-R])", r8)))
if w != [chr(c) for c in range(65, 83)]:
    fail.append('W-18-A..R register: got "' + "".join(w) + '"')

# 6. Relative links resolve --------------------------------------------------
def links(text: str) -> list[str]:
    out = []
    for m in re.finditer(r"\]\(([^)\s#]+)", text):
        link = m.group(1)
        if link.startswith(("http", "#", "mailto")):
            continue
        out.append(link)
    return out


missing = []
for text, base in [(ctx, DOCS), (hnd, DOCS), (prog, DOCS), (r8, DOCS / "stage-1"), (r9, DOCS / "stage-1")]:
    for link in set(links(text)):
        if not (base / link).resolve().exists():
            missing.append(f"{base.name}: {link}")
if missing:
    fail.append("dead relative links: " + "; ".join(missing[:10]))

# 7. DECISIONS.md integrity --------------------------------------------------
# Updated 2026-10-23 for Prompt 10.1. The original table asserted that D-005
# stayed Provisional and that no D-007 existed — a guard written while nothing
# was owner-approved. Two decisions now are (D-007, D-008) and D-005 is
# superseded, so the expectation had to follow the documents. After the
# 2026-10-23 decision pass, D-004 is itself superseded by D-015: the guard now
# asserts the supersession, so silently reverting D-004 to "Provisional" or
# deleting its original text still fails.
want_status = {
    "D-001": "Confirmed", "D-002": "Confirmed", "D-003": "Confirmed",
    "D-004": "Superseded by D-015", "D-005": "Superseded by D-008", "D-006": "Provisional",
    "D-007": "Confirmed", "D-008": "Confirmed",
    # Prompt 10.2: the Pages address and the dedicated project are owner instructions.
    "D-009": "Confirmed", "D-010": "Confirmed",
    # Final closure: the owner closed Stage 1 and authorized Stage 2.
    "D-011": "Confirmed",
    # Roadmap alignment (2026-10-23): official numbering restored, Stage 2 is
    # the Master Game Design Bible.
    "D-012": "Confirmed",
    # Legacy deletion: recorded as owner-confirmed, not as independent proof.
    "D-013": "Confirmed",
    # Decision pass (2026-10-23): the autonomous policy and nine design
    # decisions. Confirmed entries are asserted so none can vanish silently.
    "D-014": "Confirmed", "D-015": "Confirmed", "D-016": "Confirmed",
    "D-017": "Confirmed", "D-018": "Confirmed", "D-019": "Confirmed",
    "D-020": "Confirmed", "D-021": "Confirmed", "D-022": "Confirmed",
    "D-023": "Confirmed",
    # Decision-closure audit (2026-10-23): six more confirmed policies.
    "D-024": "Confirmed", "D-025": "Confirmed", "D-026": "Confirmed",
    "D-027": "Confirmed", "D-028": "Confirmed", "D-029": "Confirmed",
}
for did, expected in want_status.items():
    rows = [ln for ln in dec.splitlines() if re.match(r"\|\s*" + re.escape(did) + r"\s*\|", ln)]
    if not rows:
        fail.append(f"DECISIONS: no row for {did}")
        continue
    cells = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    status = cells[4] if len(cells) > 4 else "(missing)"
    if not status.replace("*", "").strip().startswith(expected):
        fail.append(f"DECISIONS: {did} status is {status!r}, expected {expected}")
if "Nation Supremacy" not in dec:
    fail.append("DECISIONS: D-007 does not name Nation Supremacy")
if "Supabase" not in dec:
    fail.append("DECISIONS: D-008 does not record the Supabase direction")
if "nation-supremacy.pages.dev" not in dec:
    fail.append("DECISIONS: D-009 does not record the Pages address")
if "lqdzchtfxrbtwsrpkrzo" not in dec:
    fail.append("DECISIONS: D-010 does not record the dedicated project reference")
if 'Keep "Operations Points" as a provisional' not in dec:
    fail.append("DECISIONS: D-004 decision text altered")
if "Treat Cloudflare Workers + D1 as initial candidates only" not in dec:
    fail.append("DECISIONS: D-005 decision text altered")

# 7b. Official roadmap and the Stage 2 register -------------------------------
# The owner's original stage numbering is authoritative (D-012): Stage 2 is the
# Master Game Design Bible, Stage 3 the hosting test, Stage 5 the architecture.
roadmap = DOCS / "ROADMAP.md"
register = DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md"
if not roadmap.exists():
    fail.append("ROADMAP.md missing")
else:
    rm = rd(roadmap)
    if not re.search(r"\| \*\*2\*\* \| \*\*Create the Master Game Design Bible\*\*", rm):
        fail.append("ROADMAP: stage 2 is not the Master Game Design Bible")
    if "Master Game Design Bible" not in rm or "Stage 5" not in rm:
        fail.append("ROADMAP: missing the Bible mission or the Stage 5 mapping")
if not register.exists():
    fail.append("stage-2/01_stage_2_prompt_roadmap.md missing")
else:
    rr = rd(register)
    got = re.findall(r"### Prompt (\d{2}[AB]?) —", rr)
    nums = sorted({g[:2] for g in got})
    if nums != [f"{i:02d}" for i in range(1, 16)] or "06A" not in got or "06B" not in got:
        fail.append(f"Stage 2 register prompts wrong (06 must be split into 06A/06B): {got}")
    if "Bounded completion rule" not in rr:
        fail.append("Stage 2 register: bounded completion rule missing")
handoff = DOCS / "stage-2" / "00_stage_2_handoff.md"
if not handoff.exists():
    fail.append("stage-2/00_stage_2_handoff.md missing")
else:
    ho = rd(handoff)
    if "Master Game Design Bible" not in ho or "Prompt 07" not in ho:
        fail.append("Stage 2 handoff does not name the Bible mission and Prompt 07")
for name, text in [("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)]:
    if "Master Game Design Bible" not in text:
        fail.append(f"{name}: Stage 2 mission not recorded")
    if "Prompt 07" not in text:
        fail.append(f"{name}: next Stage 2 prompt (Prompt 07) not recorded")
    if re.search(r"Stage 1 (is|remains) (still )?(incomplete|not complete)", text):
        fail.append(f"{name}: stale open Stage 1 status")

# 7b-2. No current next-action statement may point at an earlier prompt ------
# Presence checks above prove Prompt 03 is mentioned; this proves nothing still
# *instructs* the reader to run Prompt 01/02. Labelled history stays legal.
handoff_doc = DOCS / "stage-2" / "00_stage_2_handoff.md"
log_doc = DOCS / "stage-2" / "06_stage_2_progress_log.md"
next_action_docs = [
    ("AI_CONTEXT", ctx),
    ("AI_HANDOFF", hnd),
    ("PROJECT_PROGRESS", prog),
    ("stage-2/00", rd(handoff_doc) if handoff_doc.exists() else ""),
    ("stage-2/06", rd(log_doc) if log_doc.exists() else ""),
]
for name, text in next_action_docs:
    for snippet in stale_next_actions(text):
        fail.append(f"{name}: stale current next-action (earlier prompt) :: {snippet}")

# 7b-3. A *completed sub-prompt* may not be presented as the live next task --
# Prompt 07 is split into 07A/07B/07C, so 07B and 07C are both "Prompt 07" and
# the prompt-number rule above is blind to the difference. The 2026-10-29 audit
# found the progress summary still saying "07B is the next intended task and has
# not started" while its own header said 07B was complete.
subprompt_docs = [
    ("AI_CONTEXT", ctx),
    ("AI_HANDOFF", hnd),
    ("PROJECT_PROGRESS", prog),
    ("ROADMAP", rd(DOCS / "ROADMAP.md")),
    ("stage-2/00", rd(handoff_doc) if handoff_doc.exists() else ""),
    ("stage-2/01", rd(DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md")),
    ("stage-2/02", rd(DOCS / "stage-2" / "02_master_game_design_bible_outline.md")),
]
if log_doc.exists():
    _log = rd(log_doc)
    # Only the log's current-status header; its dated sections are history.
    subprompt_docs.append(("stage-2/06 header", _log[:_log.index("## 1.")] if "## 1." in _log else _log[:1200]))
for name, text in subprompt_docs:
    for snippet in subprompt_status_problems(text):
        fail.append(f"{name}: completed sub-prompt still described as live :: {snippet}")
if any("08C" not in text or "Prompt 09" not in text for text in (ctx, hnd, prog)):
    fail.append("continuity set: no current-status file names Prompt 08C complete and Prompt 09 next")

if handoff_doc.exists():
    ho = rd(handoff_doc)
    block = ho[ho.index("## 10. Next action"):ho.index("## 11. House rules")] if "## 10. Next action" in ho and "## 11. House rules" in ho else ""
    if "Prompt 10C" not in block or "Prompt 10B" not in block or "Prompt 11" not in block:
        fail.append("stage-2/00 §10: next action does not name Prompt 10B/10C complete and Prompt 11 next")
    ho_header = ho[:ho.index("## 1.")] if "## 1." in ho else ho[:1500]
    for problem in handoff_header_problems(ho_header):
        fail.append(problem)
if log_doc.exists():
    lg = rd(log_doc)
    head = lg[:lg.index("## 1.")] if "## 1." in lg else lg[:1200]
    if "Prompt 06" not in head:
        fail.append("stage-2/06: progress-log header does not name Prompt 06")

# 7c. Structured current status must agree across the continuity files -------
# Each file carries one STATUS block. Presence of phrases is not enough; the
# values have to match, and the log has to back the range they claim.
STATUS_KEYS = [
    "status_updated", "stage_1", "stage_2", "stage_2_next_prompt", "roadmap",
    "legacy_worker", "legacy_supabase_project", "operations_points", "decisions_range",
]


def status_block(text: str) -> dict[str, str]:
    blocks = re.findall(r"<!-- STATUS:BEGIN -->(.*?)<!-- STATUS:END -->", text, re.S)
    if len(blocks) != 1:
        fail.append(f"STATUS blocks found: {len(blocks)} (expected 1)")
        return {}
    out = {}
    for line in blocks[0].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    for k in STATUS_KEYS:
        if k not in out:
            fail.append(f"STATUS block missing '{k}'")
    return out


blocks = [status_block(t) for t in (ctx, hnd, prog)]
if all(blocks):
    for key in STATUS_KEYS:
        vals = {b.get(key) for b in blocks}
        if len(vals) != 1:
            fail.append(f"STATUS '{key}' disagrees across files: {sorted(x for x in vals if x)}")
    one = blocks[0]
    if one.get("stage_1") != "CLOSED":
        fail.append(f"STATUS: stage_1 is {one.get('stage_1')!r}, expected CLOSED")
    if one.get("stage_2") != "IN PROGRESS":
        fail.append(f"STATUS: stage_2 is {one.get('stage_2')!r}, expected IN PROGRESS")
    if one.get("stage_2_next_prompt") != "13D":
        fail.append(f"STATUS: next Stage 2 prompt is {one.get('stage_2_next_prompt')!r}, expected 13D")
    op_state = one.get("operations_points", "")
    if not (op_state.startswith("Approved") and "D-015" in op_state and "provisional" in op_state.lower()):
        fail.append(f"STATUS: Operations Points state is {op_state!r}, expected the D-015 model with provisional values")
    for key in ("legacy_worker", "legacy_supabase_project"):
        if "deleted" not in one.get(key, "") or "owner-confirmed" not in one.get(key, ""):
            fail.append(f"STATUS: {key} is not recorded as deleted (owner-confirmed)")
    dec_ids = re.findall(r"^\| (D-\d{3}) \|", dec, re.M)
    d_last = dec_ids[-1][2:] if dec_ids else ""
    m = re.search(r"D-(\d{3})\.\.D-(\d{3})", one.get("decisions_range", ""))
    if not m or m.group(2) != d_last or m.group(1) != "001":
        fail.append(f"STATUS: decisions_range is {one.get('decisions_range')!r}, log ends D-{d_last}")

# 7e. Stage 2 Prompt 01 deliverables ----------------------------------------
stage2_files = {
    "outline": "02_master_game_design_bible_outline.md",
    "trace": "03_requirements_traceability.md",
    "decisions": "04_approved_and_provisional_decisions.md",
    "unresolved": "05_unresolved_design_decisions.md",
    "log": "06_stage_2_progress_log.md",
}
for label, name in stage2_files.items():
    if not (DOCS / "stage-2" / name).exists():
        fail.append(f"Stage 2 Prompt 01 deliverable missing: {name}")
if (DOCS / "stage-2" / stage2_files["trace"]).exists():
    tr = rd(DOCS / "stage-2" / stage2_files["trace"])
    ids_ = re.findall(r"^\| (REQ-\d{3}) ", tr, re.M)
    if ids_ != [f"REQ-{i:03d}" for i in range(1, 870)]:
        fail.append(f"tracker requirement IDs: {len(ids_)} rows, expected REQ-001..869")
    rows_ = [ln for ln in tr.splitlines() if re.match(r"\| REQ-\d{3} \|", ln)]
    if any(not re.search(r"\| (?:0[2-9]|1[0-5])[ABC]? \||\| all \|", ln) for ln in rows_):
        fail.append("tracker contains a requirement with no assigned prompt")
if (DOCS / "stage-2" / stage2_files["outline"]).exists():
    ol = rd(DOCS / "stage-2" / stage2_files["outline"])
    if len(re.findall(r"^### B-\d{2} — ", ol, re.M)) != 19:
        fail.append("Bible outline does not carry 19 parts")
if (DOCS / "stage-2" / stage2_files["decisions"]).exists():
    dr = rd(DOCS / "stage-2" / stage2_files["decisions"])
    if len(re.findall(r"^\| DD-\d{3} \|", dr, re.M)) != 281:
        fail.append("design register does not carry DD-001..DD-281 contiguously")
    if "| DD-042 |" not in dr or "| DD-048 |" not in dr:
        fail.append("design register does not carry the decision-closure positions DD-042..DD-048")
    if "| DD-049 |" not in dr or "| DD-060 |" not in dr:
        fail.append("design register does not carry the Prompt 03 positions DD-049..DD-060")
    if "| DD-061 |" not in dr or "| DD-080 |" not in dr:
        fail.append("design register does not carry the Prompt 04 positions DD-061..DD-080")
    if "Superseded by DD-033" not in dr or "values Provisional" not in dr:
        fail.append("design register does not record DD-019 -> DD-033 with provisional OP values")
if (DOCS / "stage-2" / stage2_files["unresolved"]).exists():
    ur = rd(DOCS / "stage-2" / stage2_files["unresolved"])
    if len(re.findall(r"^\| UD-\d{3} \|", ur, re.M)) != 60:
        fail.append("unresolved register does not carry UD-001..UD-060")
if (DOCS / "stage-2" / stage2_files["log"]).exists():
    lg = rd(DOCS / "stage-2" / stage2_files["log"])
    if "Prompt 03 checkpoint" not in lg or "Prompt 04 checkpoint" not in lg or "Prompt 05 checkpoint" not in lg or "Prompt 06A" not in lg or "Prompt 06B" not in lg:
        fail.append("Stage 2 progress log does not record Prompts 03–05 and 06A/06B")

    def log_status(prompt):
        for line in lg.splitlines():
            if line.startswith(f"| {prompt} |"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                return cells[3] if len(cells) >= 4 else ""
        return ""

    # 06B completed on 2026-10-28. The previous assertion only required the
    # label to appear somewhere, so it accepted a table row that still said
    # "next — not started" while the header said complete.
    if ("**Complete**" not in log_status("06A")
            or "**Complete**" not in log_status("06B")
            or "Complete" not in log_status("07")):
        fail.append("Stage 2 progress log 06A/06B/07 status rows disagree with the summary")
    # 2026-11-03: Phase 09B is accepted, 09C and 10A are complete at the
    # specification/documentation level, and Prompt 10B is complete; 2026-11-04:
    # row 10 is complete at the specification/documentation level with 10C
    # closed and Prompt 11 next; Prompts 11–15 stay "Pending".
    if ("**08A complete**" not in log_status("08")
            or "**08B complete**" not in log_status("08")
            or "**08C complete**" not in log_status("08")):
        fail.append("Stage 2 progress log row 08 does not record 08A, 08B and 08C complete")
    if ("**ACCEPTED" not in log_status("09")
            or "Prompt 09C: complete at the specification/documentation level" not in log_status("09")
            or "Prompt 10A: complete" not in log_status("09")
            or "Prompt 10B: complete at the specification/documentation level" not in log_status("09")
            or "Prompt 10C: complete at the specification/documentation level" not in log_status("09")):
        fail.append("Stage 2 progress log row 09 does not record Phase 09B accepted, 09C, 10A, 10B and 10C complete")
    if ("10A research complete" not in log_status("10")
            or "10B specification complete" not in log_status("10")
            or "Prompt 10C complete" not in log_status("10")
            or "Prompt 13D next" not in log_status("10")):
        fail.append("Stage 2 progress log row 10 does not record 10A complete, 10B complete, 10C complete and Prompt 13D next")
    # 2026-11-07 (Prompt 12A review remediation): row 12 must say 12A is
    # complete at the research/design-foundations level and 12B is next.
    # 2026-11-11 (Prompt 13A): 12C closed on 2026-11-10 and was owner-accepted
    # on 2026-11-11, so row 12 must record the whole 12 family as complete and
    # must not still name 12C as the live next sub-prompt.
    if ("12a complete at the research/design-foundations level" not in log_status("12").lower()
            or "12b complete at the specification" not in log_status("12").lower()
            or "12c complete at the specification" not in log_status("12").lower()):
        fail.append("Stage 2 progress log row 12 does not record 12A, 12B and 12C complete")
    if lg.count("| Pending |") != 2:
        fail.append(f"Stage 2 progress log pending count is {lg.count('| Pending |')}, expected 2 (rows 14-15; rows 11-13 record their sub-prompts complete)")

# 7e-2. Phase 09B acceptance, Prompt 09C completion at the specification level
# and downstream alignment (2026-11-03). Acceptance and 09C completion are
# specification/documentation only; these checks keep the record from drifting
# into an implementation, owner-authorization or release claim.
ACCEPTANCE_SENTENCE = "Phase 09B Alliance specification and documentation: ACCEPTED."
acceptance_docs = [
    ("ROADMAP", rd(DOCS / "ROADMAP.md")),
    ("PROJECT_PROGRESS", prog),
    ("AI_CONTEXT", ctx),
    ("AI_HANDOFF", hnd),
    ("stage-2/00", rd(DOCS / "stage-2" / "00_stage_2_handoff.md")),
    ("stage-2/01", rd(DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md")),
    ("stage-2/02", rd(DOCS / "stage-2" / "02_master_game_design_bible_outline.md")),
    ("stage-2/06", lg),
    ("stage-2/16 audit", rd(DOCS / "stage-2" / "16_alliances_project_wide_consistency_audit.md")),
]
for name, text in acceptance_docs:
    if ACCEPTANCE_SENTENCE not in text:
        fail.append(f"{name}: does not state the exact Phase 09B acceptance sentence")
    if "production implementation" not in text.lower() or "pending" not in text.lower():
        fail.append(f"{name}: acceptance is not bounded by pending production implementation")

d142 = next((ln for ln in dec.splitlines() if ln.startswith("| D-142 |")), "")
if not d142:
    fail.append("DECISIONS.md does not record D-142")
elif not all(term in d142 for term in ("specification/documentation", "owner authorization")):
    fail.append("D-142 does not bound acceptance to specification/documentation and disclaim a new owner authorization")
if "| DD-165 |" not in dr or "D-142" not in dr:
    fail.append("04 register does not cross-reference DD-165 to D-142")
for did in ("D-140", "D-141"):
    if not any(ln.startswith(f"| {did} |") for ln in dec.splitlines()):
        fail.append(f"DECISIONS.md lost {did}")

for uid in [f"UD-{i:03d}" for i in range(40, 50)]:
    row = next((ln for ln in ur.splitlines() if ln.startswith(f"| {uid} |")), "")
    cells = [c.strip() for c in row.strip().strip("|").split("|")] if row else []
    status = cells[8] if len(cells) >= 9 else ""
    if not row or not status.startswith("Open"):
        fail.append(f"{uid} is not preserved as Open")
if "**28 Resolved**" not in ur or "**3 Deferred to a future prompt**" not in ur or "**29 Open**" not in ur:
    fail.append("UD register counts changed during the acceptance record")

roadmap01 = rd(DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md")
if "Prompt 09C" not in roadmap01 or "16_alliances_workflows_acceptance.md" not in roadmap01:
    fail.append("01 roadmap does not register Prompt 09C with its canonical deliverable")
if "complete at the specification/documentation level" not in roadmap01.lower() or "prompt 10" not in roadmap01.lower():
    fail.append("01 roadmap does not record Prompt 09C as complete and Prompt 10 as next")
# 2026-11-03 (Prompt 10A): the parent Prompt 10 is split into 10A/10B/10C;
# the register must name the completed research report and the live sub-prompt.
if "Prompt 10A" not in roadmap01 or "research/10A_politics_and_war_warfare_research.md" not in roadmap01:
    fail.append("01 roadmap does not register Prompt 10A research with its canonical report")
# 2026-11-04 (Prompt 10C): the workflow/acceptance companion is complete, so
# the register must name it, keep B-10 and its formula register, and hand the
# live prompt to Prompt 11.
if "Prompt 10C" not in roadmap01 or "17_warfare_workflows_acceptance.md" not in roadmap01:
    fail.append("01 roadmap does not register Prompt 10C complete with its canonical companion")
if "Prompt 11" not in roadmap01:
    fail.append("01 roadmap does not register Prompt 11 as next")
if ("17_warfare_and_settlements.md" not in roadmap01
        or "17_warfare_formula_register.md" not in roadmap01):
    fail.append("01 roadmap does not link the B-10 rulebook and formula register")
for phrase in (
    "Founding and membership", "Constitution and governance", "Taxation", "Donations",
    "ARL and operational funding", "Treaties", "NAP", "Same-Alliance attack prevention",
    "Audit, notification and security", "Failure and recovery",
    "bidirectional traceability", "REQ-534", "AX-01", "Acceptance standard",
):
    if phrase not in roadmap01:
        fail.append(f"01 roadmap Prompt 09C registration is missing {phrase!r}")
canonical_09c = DOCS / "stage-2" / "16_alliances_workflows_acceptance.md"
if not canonical_09c.exists():
    fail.append("Prompt 09C canonical deliverable is missing")
else:
    c09 = rd(canonical_09c)
    if "not a functioning Alliance system" not in c09 or "No gameplay code" not in c09:
        fail.append("Prompt 09C companion does not state the specification-only boundary")
for competing in (
    "16_alliances_workflows_and_acceptance.md",
    "16_alliances_acceptance_matrix.md",
    "16_alliances_qa_suite.md",
):
    if (DOCS / "stage-2" / competing).exists():
        fail.append(f"competing Prompt 09C deliverable exists: {competing}")

prompt_sections = re.split(r"(?=^### Prompt \d{2} )", roadmap01, flags=re.M)
by_number = {}
for section in prompt_sections:
    m = re.match(r"### Prompt (\d{2}) ", section)
    if m:
        by_number[int(m.group(1))] = section
for number, term in (
    (10, "same-Alliance attack ban"),
    (12, "DPE-049"),
    (13, "tax bracket"),
    (14, "0–100%"),
    (15, "09C workflow-and-acceptance companion"),
):
    section = by_number.get(number, "")
    if "B-09 Alliance dependency" not in section or term not in section:
        fail.append(f"Prompt {number} does not carry the required B-09 Alliance dependency ({term})")

outline_map = {
    "B-10": "17_warfare_and_settlements.md",
    "B-11": "18_world_events_and_progression.md",
    "B-12": "19_fair_play_and_player_protection.md",
    # 2026-11-11 (Prompt 13A, D-198): the `20_` serial is authored by the B-12
    # family, so the four remaining planned parts moved one serial forward. The
    # pre-D-198 names survive only inside the outline's dated 2026-11-03 mapping
    # note, which labels them superseded.
    "B-13": "21_interface_and_player_journeys.md",
    "B-14": "22_formulas_and_balance.md",
    "B-15": "23_master_game_design_bible.md",
    "B-18": "23_master_game_design_bible.md",
    "B-19": "24_stage_2_completion_report.md",
}
for part, filename in outline_map.items():
    if f"`{filename}`" not in ol:
        fail.append(f"outline mapping is missing {part} -> {filename}")
for stale_name in (
    "16_warfare_and_settlements.md", "17_world_events_and_progression.md",
    "18_fair_play_and_player_protection.md", "19_interface_and_player_journeys.md",
    "20_formulas_and_balance.md", "22_stage_2_completion_report.md",
):
    if f"`{stale_name}`" in ol:
        fail.append(f"outline still uses the stale filename {stale_name}")

for name, text in (("ROADMAP", rd(DOCS / "ROADMAP.md")), ("01 roadmap", roadmap01), ("stage-2/06", lg)):
    if "Prompts 10–15 are complete" in text or re.search(
            r"Prompt 09C is complete(?! at the specification)", text):
        fail.append(f"{name}: claims downstream prompt/09C completion beyond the specification level")

spec_doc = DOCS / "stage-2" / "07_core_gameplay_loop_symbolic_world_and_turn_system.md"
if not spec_doc.exists():
    fail.append("Stage 2 Prompt 02 specification missing")
else:
    sp = rd(spec_doc)
    got = [int(n) for n in re.findall(r"^## (\d+)\. ", sp, re.M)]
    if got != list(range(1, 32)):
        fail.append(f"B-02 sections wrong: {got}")
    trs = sorted({int(n) for n in re.findall(r"\bTR-(\d{3})\b", sp)})
    if trs != list(range(1, 98)):
        fail.append(f"B-02 TR IDs not contiguous: {len(trs)}")
    if "7200" not in sp or "mapless" not in sp.lower():
        fail.append("B-02 does not preserve the 2-hour lattice / mapless world")
    if "D-004 → D-015" not in sp:
        fail.append("B-02 does not record the D-004 -> D-015 supersession")

# 7d. History is preserved and stale current-state wording is gone ----------
stale = [
    "Stage 1 (research stage)",
    "paused pending manual deletion",
    "remain the outstanding Stage 1 work",
    "currently holds six entries",
    "paused rather than deleted",
    "Deleting the old project is still outstanding",
]
for phrase in stale:
    for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)):
        if phrase.lower() in text.lower():
            fail.append(f"{name}: stale wording present: {phrase!r}")

_WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}
_WORDS["twenty-one"] = 21
_WORDS["twenty-two"] = 22
_WORDS["twenty-three"] = 23
_WORDS["twenty-nine"] = 29
_WORDS["thirty"] = 30
_WORDS["forty-two"] = 42
_WORDS["fifty-one"] = 51
_WORDS["sixty-five"] = 65
_WORDS["eighty"] = 80
_WORDS["ninety"] = 90
_WORDS["ninety-one"] = 91
_WORDS["one hundred and eight"] = 108
_WORDS["one hundred and twenty-one"] = 121
_WORDS["one hundred and twenty-two"] = 122
_WORDS["one hundred and thirty-two"] = 132
_WORDS["one hundred and thirty-four"] = 134
_WORDS["one hundred and thirty-nine"] = 139
_WORDS["one hundred and forty"] = 140
_WORDS["one hundred and forty-one"] = 141
_WORDS["one hundred and forty-two"] = 142
_WORDS["one hundred and forty-three"] = 143
_WORDS["one hundred and fifty-one"] = 151
_WORDS["one hundred and five"] = 105
_WORDS["one hundred and eight"] = 108
_WORDS["one hundred and seventy-seven"] = 177
_WORDS["one hundred and eighty-seven"] = 187
_WORDS["one hundred and ninety-seven"] = 197
_WORDS["two hundred and five"] = 205
_WORDS["two hundred and nineteen"] = 219
_WORDS["two hundred and thirty-two"] = 232
_WORDS["two hundred and thirty-three"] = 233
_mc = re.search(r"holds \*\*([\w -]+?)\*\* entries", hnd)
_dec_rows = [ln for ln in dec.splitlines() if re.match(r"\|\s*D-\d{3}\s*\|", ln)]
if not _mc or _WORDS.get(_mc.group(1).lower()) != len(_dec_rows):
    fail.append(f"DECISIONS: handoff count {_mc.group(1) if _mc else None!r} vs {len(_dec_rows)} rows")

d010 = next((ln for ln in dec.splitlines() if ln.startswith("| D-010 |")), "")
if "paused now" not in d010 or "Superseded by D-013" not in d010:
    fail.append("DECISIONS: D-010 history not preserved/pointed to D-013")
d013 = next((ln for ln in dec.splitlines() if ln.startswith("| D-013 |")), "")
if "owner-confirmed" not in d013.lower():
    fail.append("DECISIONS: D-013 does not record the deletion as owner-confirmed")
if "Stage 1 is not complete" not in r9:
    fail.append("Report 9: historical pre-closure verdict was edited away")

# 7f. Decision-closure audit (2026-10-23) -------------------------------------
audit_doc = DOCS / "stage-2" / "08_final_decision_closure_audit.md"
if not audit_doc.exists():
    fail.append("stage-2/08_final_decision_closure_audit.md missing")
else:
    au = rd(audit_doc)
    for did in ("D-024", "D-025", "D-026", "D-027", "D-028", "D-029", "D-030"):
        if did not in au:
            fail.append(f"audit does not record {did}")
    for uid in ("UD-004", "UD-015", "UD-016", "UD-025", "UD-027", "UD-028", "UD-029"):
        if uid not in au:
            fail.append(f"audit inventory omits {uid}")
    if "No Prompt 03 deliverable exists yet" not in au:
        fail.append("audit does not state that Prompt 03 was not written")
    if "CF-02" not in au or "CF-04" not in au:
        fail.append("audit does not separate the unexecuted CF-02/CF-04 proofs")

# 7g. FO-018 may not read as a live owner question ---------------------------
for name, text in (("AI_CONTEXT", ctx), ("AI_HANDOFF", hnd), ("PROJECT_PROGRESS", prog)):
    if "FO-018 (catch-up) stays owner-held" in text or "FO-018 catch-up decision itself remains owner-held" in text:
        fail.append(f"{name}: FO-018 is still described as owner-held (D-021 decided it)")
if "D-021" not in dec or "No catch-up acceleration at launch" not in dec:
    fail.append("DECISIONS: D-021 launch posture missing")

# 7g-2. Cross-register decision status -------------------------------------
# Catches the recurring failure where a decision is resolved in one register
# but still reads Open elsewhere, and where an ID is duplicated or dropped.
ur_doc = DOCS / "stage-2" / "05_unresolved_design_decisions.md"
if ur_doc.exists():
    ur = rd(ur_doc)
    urows = {m.group(1): ln for ln in ur.splitlines()
             if (m := re.match(r"\| (UD-\d{3}) \|", ln))}
    expected_ids = [f"UD-{i:03d}" for i in range(1, 61)]
    if sorted(urows) != expected_ids:
        fail.append(f"unresolved register IDs are not UD-001..UD-060: {len(urows)} rows")
    resolved = {"UD-001", "UD-002", "UD-003", "UD-004", "UD-008", "UD-010",
                "UD-011", "UD-014", "UD-015", "UD-016", "UD-018", "UD-019",
                "UD-020", "UD-021", "UD-025", "UD-027", "UD-028", "UD-029",
                "UD-030", "UD-009", "UD-013", "UD-033", "UD-012", "UD-039",
                "UD-032", "UD-024", "UD-034", "UD-035"}
    deferred = {"UD-022": "13", "UD-023": "13",
                "UD-031": "12"
                }
    open_ud = ["UD-005", "UD-006", "UD-007", "UD-017", "UD-026", "UD-036",
               "UD-037", "UD-038", "UD-040", "UD-041", "UD-042", "UD-043", "UD-044", "UD-045", "UD-046", "UD-047", "UD-048", "UD-049",
               "UD-050", "UD-051", "UD-052", "UD-053", "UD-054", "UD-055", "UD-056", "UD-057", "UD-058", "UD-059", "UD-060"]
    def _ud_status(row: str) -> str:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        return cells[8] if len(cells) >= 9 else ""

    for uid in sorted(resolved):
        if not _ud_status(urows.get(uid, "")).startswith("**Resolved"):
            fail.append(f"{uid} is not resolved in its Status cell")
    for uid, prompt in deferred.items():
        if not _ud_status(urows.get(uid, "")).startswith(f"**Deferred to Prompt {prompt}**"):
            fail.append(f"{uid} is not deferred to Prompt {prompt} in its Status cell")
    for uid in open_ud:
        status = _ud_status(urows.get(uid, ""))
        if not status.startswith("Open") or "Resolved" in status:
            fail.append(f"{uid} should be a genuinely open row")
    non_resolved = sorted(list(deferred) + open_ud)
    if "## 6." in ur:
        u6 = re.findall(r"^\| `?(UD-\d{3})`? \|", ur[ur.index("## 6."):], re.M)
        if u6 != non_resolved:
            fail.append(f"§6 inventory disagrees with non-resolved rows: {u6}")
    if "**28 Resolved**" not in ur or "**3 Deferred to a future prompt**" not in ur or "**29 Open**" not in ur:
        fail.append("unresolved register does not state the reconciling 28/3/29 counts")

for did in [f"D-{i:03d}" for i in range(24, 31)]:
    drow = next((ln for ln in dec.splitlines() if ln.startswith(f"| {did} |")), "")
    drow_design = rd(DOCS / "stage-2" / "04_approved_and_provisional_decisions.md")
    if "Confirmed" not in drow or f"| {did} |" not in drow_design:
        fail.append(f"{did} is not confirmed/summarised consistently")
for did, successor in (("D-004", "D-015"), ("D-005", "D-008")):
    drow = next((ln for ln in dec.splitlines() if ln.startswith(f"| {did} |")), "")
    if f"Superseded by {successor}" not in drow:
        fail.append(f"{did} lost its {successor} supersession")

# 7g-3. Continuity totals and the fixed architecture ------------------------
    if "D-001" not in text or "D-151" not in text:
        fail.append(f"{name}: decision range is not D-001..D-151")
    if "Cloudflare" not in text or "Supabase" not in text:
        fail.append(f"{name}: fixed Cloudflare + Supabase architecture not named")
    if re.search(r"\b(Vercel|Netlify|Firebase)\b", text):
        fail.append(f"{name}: names a provider outside the fixed architecture")
    if "D-001…D-029" in text or "D-001..D-029" in text:
        fail.append(f"{name}: current decision range still ends at D-029")
ctx04 = next((ln for ln in ctx.splitlines() if "stage-2/04_approved" in ln), "")
ctx07 = next((ln for ln in ctx.splitlines() if "stage-2/07_core" in ln), "")
if ("DD-001" not in ctx04 or "DD-281" not in ctx04) or ("D-001" not in ctx04 or "D-233" not in ctx04):
    fail.append("AI_CONTEXT row 04 carries stale decision/position totals")
if "v1.5" not in ctx07:
    fail.append("AI_CONTEXT row 07 carries a stale B-02 version")

# 7g-4. Backup policy must match the verified three-part CLI workflow --------
d025 = next((ln for ln in dec.splitlines() if ln.startswith("| D-025 |")), "")
dd043 = next((ln for ln in rd(DOCS / "stage-2" / "04_approved_and_provisional_decisions.md").splitlines()
              if ln.startswith("| DD-043 |")), "")
for label, text in (("D-025", d025), ("DD-043", dd043)):
    if "--role-only" not in text or "--data-only" not in text:
        fail.append(f"{label}: backup policy does not name both export flags")
    if "no data" not in text.lower() and "no table data" not in text.lower():
        fail.append(f"{label}: does not record the default dump's missing data")
    if "custom roles" not in text.lower():
        fail.append(f"{label}: does not record the default dump's missing custom roles")
for label, text in (("DECISIONS", dec), ("audit", au)):
    if "`supabase db dump` — roles, schema, data" in text:
        fail.append(f"{label}: still describes one dump as roles+schema+data")

# 7h. The requirements status counts must match the table ---------------------
tr_doc = DOCS / "stage-2" / "03_requirements_traceability.md"
if tr_doc.exists():
    tr_rows = [ln for ln in rd(tr_doc).splitlines() if re.match(r"\| REQ-\d{3} \|", ln)]
    counts = {"Approved": 0, "Provisional": 0, "Open": 0, "Deferred": 0, "Proposed": 0}
    for ln in tr_rows:
        cells = ln.split("|")
        cell = cells[4] if len(cells) > 4 else ""
        for key in counts:
            if key in cell:
                counts[key] += 1
                break
    if counts != {"Approved": 55, "Provisional": 774, "Open": 39, "Deferred": 1, "Proposed": 0}:
        fail.append(f"requirements status counts are {counts}, expected 55/774/39/1/0")

# 7i. Stage 2 Prompt 03 specification (2026-10-24) ---------------------------
b03_doc = DOCS / "stage-2" / "09_account_onboarding_nation_creation_and_progression.md"
if not b03_doc.exists():
    fail.append("stage-2/09_account_onboarding_nation_creation_and_progression.md missing")
else:
    b03 = rd(b03_doc)
    secs = [int(n) for n in re.findall(r"^## (\d+)\. ", b03, re.M)]
    if secs != list(range(1, 23)):
        fail.append(f"B-03 sections wrong: {secs}")
    inv_rows = re.findall(r"^\| INV-\d{3} \|", b03, re.M)
    if len(inv_rows) != 32:
        fail.append(f"B-03 invariant table has {len(inv_rows)} rows, expected 32")
    for prefix, last in (("ACC", 49), ("NET", 61), ("NAT", 53), ("RRL", 34), ("ONB", 52), ("DAT", 12), ("INV", 32)):
        got = sorted({int(n) for n in re.findall(rf"\b{prefix}-(\d{{2,3}})\b", b03)})
        if got != list(range(1, last + 1)):
            fail.append(f"B-03 {prefix} IDs are not {prefix}-001..{prefix}-{last:03d}")
    t03 = set(re.findall(r"\bT03-[A-E]\d{2}\b", b03))
    cited = set(re.findall(r"\bT03-[A-E]\d{2}\b", b03[b03.index("| ID | Invariant"):b03.index("**INV-ENF")]))
    if cited - t03 or len(cited) < 25:
        fail.append(f"B-03 invariant table cites unknown or too few tests: {sorted(cited - t03)}")
    for phrase, label in (
        ("no gameplay cooldown", "reroll has no gameplay cooldown"),
        ("Permanently delete", "reroll confirmation names permanent deletion"),
        ("no raw IP", "raw IP is never stored"),
        ("never sufficient by itself", "IP alone cannot justify a permanent ban"),
        ("No standing co-resident exemption", "co-resident exemption is refused"),
        ("D-021", "the no-catch-up decision is applied"),
    ):
        if phrase.lower() not in b03.lower():
            fail.append(f"B-03 does not state that {label}")
    if "TAC-" in b03:
        fail.append("B-03 still uses the retired TAC- test IDs")
    if not re.search(r"\*\*None has been tested against running code", b03):
        fail.append("B-03 does not state that no invariant has been tested")
    for req in ("REQ-061", "REQ-077", "REQ-090", "REQ-097"):
        if req not in b03:
            fail.append(f"B-03 does not cite {req}")

# 7j. Stage 2 Prompt 04 specification (2026-10-24) ---------------------------
b04_doc = DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md"
b04_reg_doc = DOCS / "stage-2" / "10_economic_formula_and_balance_register.md"
b04_res_doc = DOCS / "stage-2" / "research" / "04_politics_and_war_economy_research.md"
for doc in (b04_doc, b04_reg_doc, b04_res_doc):
    if not doc.exists():
        fail.append(f"missing Stage 2 Prompt 04 document: {doc.name}")
if b04_doc.exists() and b04_reg_doc.exists():
    b04 = rd(b04_doc)
    b04_reg = rd(b04_reg_doc)
    secs = [int(n) for n in re.findall(r"^## (\d+)\. ", b04, re.M)]
    if secs != list(range(1, 26)):
        fail.append(f"B-04 sections wrong: {secs}")
    roster = ("food", "coal", "oil", "uranium", "lead", "bauxite", "iron",
              "gasoline", "ammunition", "steel", "aluminum")
    missing_res = [r for r in roster if r not in b04.lower()]
    if missing_res:
        fail.append(f"B-04 roster is missing: {missing_res}")
    for recipe, label in (("10 oil", "oil→gasoline"), ("10 iron", "iron→steel"),
                          ("12 bauxite", "bauxite→aluminum"), ("8 lead", "lead→ammunition")):
        if recipe not in b04.lower() or recipe not in b04_reg.lower():
            fail.append(f"B-04 recipe {label} is not stated in both the rulebook and the register")
    examples = len(re.findall(r"^### Example \d+", b04, re.M))
    if examples != 20:
        fail.append(f"B-04 has {examples} worked examples, expected 20")
    for prefix, last in (("A", 5), ("B", 8), ("C", 5), ("D", 8), ("E", 6),
                         ("F", 5), ("G", 6), ("H", 4), ("I", 3), ("J", 4)):
        got = sorted({int(n) for n in re.findall(rf"\bT04-{prefix}(\d{{2}})\b", b04)})
        if got != list(range(1, last + 1)):
            fail.append(f"B-04 T04-{prefix} IDs are not 01..{last:02d}")
    missing_req = sorted({f"REQ-{i:03d}" for i in range(98, 188)} - set(re.findall(r"REQ-\d{3}", b04)))
    if missing_req:
        fail.append(f"B-04 does not cite its own requirements: {missing_req[:8]}")
    missing_f = sorted(set(re.findall(r"F-EC-\d{3}", b04)) - set(re.findall(r"F-EC-\d{3}", b04_reg)))
    if missing_f:
        fail.append(f"B-04 cites formulas absent from the register: {missing_f}")
    for phrase, label in (
        ("append-only", "the ledger is append-only"),
        ("P3.1", "the P3 sub-phase order is published"),
        ("austerity", "the austerity order exists"),
        ("no debt", "debt is refused"),
        ("hunger", "the food shortage penalty is defined"),
        ("1,000 people", "one food unit feeds 1,000 people"),
        ("restricted", "a restricted pair's trade is blocked"),
    ):
        if phrase.lower() not in b04.lower():
            fail.append(f"B-04 does not state that {label}")
    if "0 of 54 tests executed" not in b04:
        fail.append("B-04 does not record that none of its 54 tests has run")

# 7j. Stage 2 Prompt 05 specification (2026-10-25) ---------------------------
b05_doc = DOCS / "stage-2" / "11_cities_infrastructure_production_and_research.md"
b05_reg_doc = DOCS / "stage-2" / "11_city_infrastructure_production_and_research_formula_register.md"
b05_res_doc = DOCS / "stage-2" / "research" / "05_politics_and_war_city_infrastructure_production_research.md"
for doc in (b05_doc, b05_reg_doc, b05_res_doc):
    if not doc.exists():
        fail.append(f"missing B-05 deliverable: {doc.name}")
if b05_doc.exists() and b05_reg_doc.exists():
    b05 = rd(b05_doc)
    b05_reg = rd(b05_reg_doc)
    # The version header and the revision history legitimately name IDs that were
    # retired during the audit (REQ-258). The citation check must read the rules,
    # not the changelog that explains why an ID is gone.
    b05_current = "\n".join(
        line for line in b05.splitlines() if not line.startswith("**Version:**")
    ).split("**URB-172 — Revision history.**")[0]
    secs5 = [int(n) for n in re.findall(r"^## (\d+)\. ", b05, re.M)]
    if secs5 != list(range(1, 27)):
        fail.append(f"B-05 section numbering is not 1..26: {secs5}")
    for token, label in (
        ("**no** coordinates", "cities carry no coordinates"),
        ("cannot be deleted", "cities cannot be deleted"),
        ("development capacity", "the capacity model is defined"),
        ("bld_farm", "the extraction catalogue exists"),
        ("bld_refinery", "the processing catalogue exists"),
        ("tech_nuclear_engineering", "the nuclear gate exists"),
        ("prg_granary", "the programme layer exists"),
        ("45,000 + 100", "the housing formula is stated"),
        ("25% of the crown", "the demolition refund is bounded"),
    ):
        if token.lower() not in b05.lower():
            fail.append(f"B-05 does not state that {label}")
    for res in ("food", "coal", "oil", "uranium", "lead", "bauxite", "iron",
                "gasoline", "ammunition", "steel", "aluminum"):
        if res not in b05.lower():
            fail.append(f"B-05 roster is missing: {res}")
    recipes = (("10 oil → 8 gasoline", "oil to gasoline", "gasoline"),
               ("10 iron + 6 coal → 8 steel", "iron to steel", "steel"),
               ("12 bauxite → 8 aluminum", "bauxite to aluminum", "aluminum"),
               ("8 lead + 4 coal → 10 ammunition", "lead to ammunition", "ammunition"))
    for recipe, label, good in recipes:
        if recipe not in b05 or good not in b05_reg.lower():
            fail.append(f"B-05 recipe {label} is not stated in the rulebook and its register")
    examples5 = len(re.findall(r"^### Example \d+", b05, re.M))
    if examples5 != 20:
        fail.append(f"B-05 has {examples5} worked examples, expected 20")
    for prefix in "ABCDEFGHIJ":
        if not re.search(rf"\bT05-{prefix}\d{{2}}\b", b05):
            fail.append(f"B-05 T05-{prefix} tests are missing")
    missing_req5 = sorted({f"REQ-{i:03d}" for i in range(188, 258)} - set(re.findall(r"REQ-\d{3}", b05)))
    if missing_req5:
        fail.append(f"B-05 does not cite its own requirements: {missing_req5[:8]}")
    missing_f5 = sorted(set(re.findall(r"F-CI-\d{3}", b05)) - set(re.findall(r"F-CI-\d{3}", b05_reg)))
    if missing_f5:
        fail.append(f"B-05 cites formulas absent from its register: {missing_f5}")
    # The catalogue is closed at 17 types, and every type needs a stable building_id.
    bld_ids = set(re.findall(r"`(bld_[a-z_]+)`", b05_current))
    if len(bld_ids) != 17:
        fail.append(f"B-05 names {len(bld_ids)} building IDs, expected 17: {sorted(bld_ids)}")
    if "nineteenth" in b05_current:
        fail.append("B-05 still implies an eighteenth existing catalogue type")
    for phrase, label in (
        ("**Version:** 1.7", "the v1.7 header is current"),
        ("unexecuted", "none of the 64 tests is claimed as executed"),
        ("no rule here is implemented", "nothing is claimed implemented"),
    ):
        if phrase.lower() not in b05.lower():
            fail.append(f"B-05 does not state that {label}")
    if not re.search(r"D-066", b05) or not re.search(r"DD-081", b05):
        fail.append("B-05 does not point at its decision records")
    known5 = set(re.findall(r"REQ-\d{3}", rd(DOCS / "stage-2" / "03_requirements_traceability.md")))
    dangling5 = sorted(set(re.findall(r"REQ-\d{3}", b05_current)) - known5)
    if dangling5:
        fail.append(f"B-05 cites requirements that do not exist: {dangling5[:8]}")
    if "seventeen types" not in b05 or "twelve technologies" not in b05:
        fail.append("B-05 catalogue/technology count no longer matches its own tables")

# 7k. B-06 version, roadmap section and election-wording consistency --------
b06_doc = DOCS / "stage-2" / "12_population_and_domestic_politics.md"
b06_reg_doc = DOCS / "stage-2" / "12_population_and_domestic_politics_formula_register.md"
roadmap_doc = DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md"
if not (b06_doc.exists() and b06_reg_doc.exists() and roadmap_doc.exists()):
    fail.append("missing a B-06 or roadmap deliverable")
else:
    b06 = rd(b06_doc)
    b06_reg = rd(b06_reg_doc)
    roadmap = rd(roadmap_doc)
    m_b06 = re.search(r"\*\*Version:\*\*\s*(\d+\.\d+)", b06)
    m_reg = re.search(r"\*\*Version:\*\*\s*(\d+\.\d+)", b06_reg)
    if not m_b06 or m_b06.group(1) != "2.6":
        fail.append(f"B-06 header version is {m_b06.group(1) if m_b06 else None!r}, expected 2.6")
    if not m_reg:
        fail.append("B-06 formula register has no version header")
    reg_version = m_reg.group(1) if m_reg else ""
    if reg_version != "2.5":
        fail.append(f"B-06 register version is {reg_version!r}, expected 2.5")
    ctx_header = next((ln for ln in ctx.splitlines() if ln.startswith("**Last updated:**")), "")
    hnd06 = next((ln for ln in hnd.splitlines() if ln.startswith("**Prompt 06 is complete")), "")
    prog06 = next((ln for ln in prog.splitlines() if ln.startswith("| 06 |")), "")
    ho06 = next((ln for ln in rd(handoff_doc).splitlines() if ln.startswith("Prompt 06 is **complete**")), "")
    road06 = next((ln for ln in roadmap.splitlines() if ln.startswith("| 06 |")), "")
    ol06 = next((ln for ln in ol.splitlines() if "B-06, 38 sections" in ln), "")
    for problem in version_reference_problems(
            (("AI_CONTEXT header", ctx_header),
             ("AI_HANDOFF Prompt 06 record", hnd06),
             ("PROJECT_PROGRESS row 06", prog06),
             ("stage-2/00 Prompt 06 record", ho06),
             ("roadmap row 06", road06),
             ("outline B-06 entry", ol06)), reg_version):
        fail.append(problem)
    roadmap_rows = [ln for ln in roadmap.splitlines() if re.match(r"\|\s*\d{2}\s*\|", ln)]
    for problem in roadmap_log_problems(road06, rd(log_doc), roadmap_rows):
        fail.append(problem)
    for problem in election_wording_problems(dec, tr):
        fail.append(problem)
    if "takes office" in b06:
        fail.append("B-06 still says a new administration takes office")
    if "remains the nation's controller" not in b06:
        fail.append("B-06 does not state that the account keeps the nation after a contest")
    roaddoc = DOCS / "ROADMAP.md"
    if not roaddoc.exists():
        fail.append("missing ROADMAP.md")
    else:
        rm = rd(roaddoc)
        # The stage row must name the *current* sub-stage, not merely "Prompt 07":
        # 07B is complete and 07C is next, so the earlier bare "Prompt 07 next"
        # wording is no longer true.
        if ("Prompts 01–09 are complete" not in rm
                or "Prompt 10" not in rm
                or "Prompt 10A" not in rm
                or "Prompt 10B" not in rm
                or "Prompt 10C" not in rm
                or "Prompt 11" not in rm):
            fail.append("ROADMAP stage-2 row does not record Prompts 01–09 complete, 10A–10C and Prompt 11 next")

# 8. No production code outside the authorised prototype --------------------
# Prompt 10 permits exactly one isolated spike directory. Code anywhere else
# (docs/, project root, future game directories) still fails this check.
EXEMPT_PARTS = {"prototypes", "node_modules", "dist", ".git", ".wrangler"}
files = [p for p in glob.glob(str(ROOT / "**" / "*"), recursive=True) if ".git" not in Path(p).parts and Path(p).is_file()]
prodlike = [
    f
    for f in files
    if f.lower().endswith((".ts", ".js", ".tsx", ".jsx", ".cs", ".go", ".rb", ".php", ".java", ".c", ".cpp"))
    and not (set(Path(f).parts) & EXEMPT_PARTS)
]
if prodlike:
    fail.append("production-code-like files present: " + "; ".join(prodlike[:10]))
py_out = [f for f in files if f.endswith(".py") and "qa_backups" not in Path(f).parts]
if py_out:
    fail.append(".py files outside qa_backups: " + "; ".join(py_out))

# 9. Required documents exist ------------------------------------------------
for required in [
    DOCS / "stage-1" / "01_competitor_research.md",
    DOCS / "stage-1" / "02_strengths_weaknesses_player_frustrations.md",
    DOCS / "stage-1" / "03_feature_comparison_opportunity_analysis.md",
    DOCS / "stage-1" / "04_target_audience_and_player_experience.md",
    DOCS / "stage-1" / "05_core_game_concept_and_design_pillars.md",
    DOCS / "stage-1" / "06_core_gameplay_systems_and_interactions.md",
    DOCS / "stage-1" / "07_economy_design_and_market_structure.md",
    DOCS / "stage-1" / "08_security_privacy_fair_play_and_trust.md",
    DOCS / "stage-1" / "09_integrated_design_synthesis_and_readiness_audit.md",
    DOCS / "stage-2" / "research" / "08A_diplomacy_research.md",
    DOCS / "stage-2" / "research" / "10A_politics_and_war_warfare_research.md",
    DOCS / "stage-2" / "17_warfare_and_settlements.md",
    DOCS / "stage-2" / "17_warfare_formula_register.md",
    DOCS / "stage-2" / "15_diplomacy.md",
    DOCS / "stage-2" / "15_diplomacy_formula_register.md",
]:
    if not required.exists():
        fail.append(f"missing required document: {required}")

print("VALIDATION:", "ALL CHECKS PASSED" if not fail else "FAILURES:")
for item in fail:
    print("  -", item)
sys.exit(1 if fail else 0)
