"""One-shot Prompt 12A documentation synchroniser (mirrors 11C_sync_docs.py).

Rewrites the recurring "Prompt 12 is next / not started" current-status claims to
the accurate post-12A wording, inserts the 12A status blockquote into the live
status surfaces, and advances the recurring tally sentences. Run once from the
repository root. It changes status wording only; no specification, register row
or historical log entry is rewritten.
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(".")
SURFACES = [ROOT / "docs" / n for n in
            ("AI_CONTEXT.md", "AI_HANDOFF.md", "PROJECT_PROGRESS.md", "ROADMAP.md")]
ALL = SURFACES + [ROOT / "docs" / "stage-2" / n for n in
                  ("00_stage_2_handoff.md", "01_stage_2_prompt_roadmap.md",
                   "02_master_game_design_bible_outline.md")]

COMPLETE = ("**Prompt 12A — fair play, privacy, moderation and administration: research, "
            "evidence, requirements and design foundations — is complete at the research and "
            "design-foundations level (2026-11-06; log §73)**")

# Longest first: each rule rewrites one live-status claim shape.
RULES = [
    ("Prompt 12 is next in the roadmap, has not started, and is not authorized to start by this prompt",
     COMPLETE.replace("**", "") + "; Prompt 12B is next in the roadmap, has not started, and "
     "is not authorized to start by this prompt"),
    ("Prompt 12 is next in the roadmap, has not started, and needs explicit owner authorization (D-002)",
     "Prompt 12A is complete at the research/design-foundations level (log §73); Prompt 12B is "
     "next in the roadmap, has not started, and needs explicit owner authorization (D-002)"),
    ("Prompt 12 is next, requires separate owner authorization and has not started",
     "Prompt 12A is complete (log §73); Prompt 12B is next, requires separate owner "
     "authorization and has not started"),
    ("Prompt 12 is next, has not started and needs explicit owner authorization",
     "Prompt 12A is complete (log §73); Prompt 12B is next, has not started and needs "
     "explicit owner authorization"),
    ("Prompt 12 is the next roadmap prompt and needs its own authorization",
     "Prompt 12A is complete at the research/design-foundations level (log §73) and Prompt 12B "
     "is the next roadmap prompt, needing its own authorization"),
    ("Prompt 12 is next and needs owner authorization",
     "Prompt 12A is complete (log §73); Prompt 12B is next and needs owner authorization"),
    ("Prompt 12 is next and is not authorized to start",
     "Prompt 12A is complete (log §73); Prompt 12B is next and is not authorized to start"),
    ("Prompt 12 is next and has not started",
     "Prompt 12A is complete (log §73); Prompt 12B is next and has not started"),
    ("Prompt 12 is next and not started",
     "Prompt 12A is complete (log §73); Prompt 12B is next and not started"),
    ("Prompt 12 is next; no new 09B redesign or research authorized",
     "Prompt 12A is complete (log §73); Prompt 12B is next; no new 09B redesign or research authorized"),
    ("Prompt 12 — fair play, player protection, privacy and administration — is next in the "
     "roadmap, not started, and needs explicit owner authorization.",
     "Prompt 12A — the B-12 research and design foundations — is **complete** (log §73) and "
     "**Prompt 12B — the B-12 rulebook and formula register — is next in the roadmap, not "
     "started, and needs explicit owner authorization.**"),
]

BLOCKQUOTE = (
    "> **12A status (2026-11-06; current — the dated entries in progress-log §§56–§73 hold the "
    "history):** **Prompt 12A — Fair play, privacy, moderation and administration: research, "
    "evidence, requirements and design foundations — is COMPLETE at the research and "
    "design-foundations level (documentation only).** Its three deliverables are "
    "[the B-12 research report]({P}research/12A_fair_play_privacy_moderation_administration_"
    "research.md) (33 sections), [the source and benchmark register]({P}research/"
    "12A_sources_and_benchmarks_register.md) (152 source rows, 40 benchmark mechanics, 18 "
    "comparator profiles) and [the requirements, integration and risk registers]({P}research/"
    "12A_requirements_integration_and_risk_registers.md) (106 candidate requirements, 30 "
    "twelve-field dependency rows, 32 threat rows, 15 failure postures, 15 open questions). "
    "Fifteen design positions **D-163…D-177 / DD-211…DD-225** are recorded and nine unresolved "
    "rows **UD-052…UD-060** are opened; **`UD-040`–`UD-049`, `UD-050` and `UD-051` are untouched "
    "and remain Open**, and no owner-reserved decision was resolved. No global `REQ-` was "
    "allocated: **`REQ-763` remains the frontier and `REQ-764` is reserved for Prompt 12B**. The "
    "independent validator [`docs/qa_backups/12A_validate_foundations.py`]"
    "({QA}12A_validate_foundations.py) passes **35/35** checks with **10/10** positive and "
    "**15/15** negative fixtures, and the 22 acceptance gates close at **15 PASS / 7 PARTIAL / "
    "0 FAIL / 0 BLOCKED / 0 NOT RUN / 0 NOT APPLICABLE**. B-12's canonical rulebook path "
    "**`stage-2/20_fair_play_and_player_protection.md` is reserved, not created** (D-163/DD-211). "
    "**No fair-play rule, penalty, duration, permission, moderation workflow, schema or "
    "implementation exists; the Supabase prototype's client-writable `profiles.treasury` column "
    "and its unprotected `audit` table remain open defects, and the prototype is not "
    "security-verified.** **Prompt 12B — B-12 rulebook and formula register — is next in the "
    "roadmap, has not started, and is not authorized to start by this prompt.**\n")


def build_blockquote(prefix: str, qa: str) -> str:
    return BLOCKQUOTE.replace("{P}", prefix).replace("{QA}", qa)


def demote_and_insert(text: str, bq: str) -> str:
    """Put the 12A blockquote first and mark the previous current header superseded."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("> **1") and " status (2026-1" in ln and "; current —" in ln:
            lines[i] = ln.replace("; current —", "; superseded by the 12A status above —", 1)
            lines.insert(i, bq.rstrip("\n"))
            return "\n".join(lines)
    raise AssertionError("no current status header")


counts = {}
for path in ALL:
    t = path.read_text(encoding="utf-8")
    before = t
    for old, new in RULES:
        n = t.count(old)
        if n:
            counts[old[:40]] = counts.get(old[:40], 0) + n
            t = t.replace(old, new)
    if path in SURFACES:
        t = demote_and_insert(t, build_blockquote("stage-2/", "qa_backups/"))
    elif path.name == "00_stage_2_handoff.md":
        t = demote_and_insert(t, build_blockquote("", "../qa_backups/"))
    if t != before:
        path.write_text(t, encoding="utf-8")
        print("synced", path)

for k, v in counts.items():
    print(f"{v:3d}  {k}")
