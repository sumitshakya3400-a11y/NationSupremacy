"""One-shot Prompt 11C documentation synchroniser.

Rewrites the recurring "Prompt 11C is next / not started" claims to the accurate
post-completion wording, keeps the three STATUS blocks identical, and records the
Prompt 11C result in the Stage 2 surfaces. Run once from docs/.
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOC_LINK = "stage-2/19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md"
QA_LINK = "../qa_backups/11C_validate_b11_workflows.py"

REPLACEMENTS = [
    # --- recurring next-action claims ------------------------------------- #
    ("**Prompt 11C — workflows, cross-system integration and acceptance — is next, authorized and has not started.**",
     "**Prompt 11C — workflows, cross-system integration and acceptance — is COMPLETE at the specification, integration and acceptance-design level (2026-11-05; log §72); Prompt 12 is next, requires separate owner authorization and has not started.**"),
    ("Prompt 11C is authorized to begin after the C3 acceptance but has not started; Prompt 14 calibration has not started.",
     "Prompt 11C has since been executed and is complete at the specification/documentation level (log §72); Prompt 12 is the next roadmap prompt and needs its own authorization; Prompt 14 calibration has not started."),
    ("and Prompt 11C is next and has not started**",
     "and Prompt 11C is complete at the specification/documentation level (log §72), so Prompt 12 is next and has not started**"),
    ("and Prompt 11C is next and has not started;",
     "and Prompt 11C is complete at the specification/documentation level (log §72), so Prompt 12 is next;"),
    ("and Prompt 11C is next and has not started",
     "and Prompt 11C is complete at the specification/documentation level (log §72), so Prompt 12 is next and has not started"),
    ("Prompt 11C is next, authorized but not started",
     "Prompt 11C is complete at the specification/documentation level (log §72); Prompt 12 is next and has not started"),
    ("Prompt 11C is next, authorized and not started",
     "Prompt 11C is complete at the specification/documentation level (log §72); Prompt 12 is next and has not started"),
    ("Prompt 11C is authorized but not started",
     "Prompt 11C is complete at the specification/documentation level (log §72)"),
    ("Prompt 11C is next, not started",
     "Prompt 11C is complete (log §72); Prompt 12 is next and not started"),
    ("**11C next, not started; authorized by C3**",
     "**11C complete at the specification/documentation level (log §72); Prompt 12 next and not started**"),
    ("**11C next and not started**",
     "**11C complete at the specification/documentation level (log §72); Prompt 12 is next and not started**"),
    ("Prompt 11C next and not started",
     "Prompt 11C complete (log §72); Prompt 12 next and not started"),
    ("Prompt 11C: next, not started",
     "Prompt 11C: complete at the specification/documentation level (log §72)"),
    ("Prompt 11C is next and not started",
     "Prompt 11C is complete (log §72) and Prompt 12 is next and not started"),
    ("Prompt 11C is next, not started",
     "Prompt 11C is complete (log §72); Prompt 12 is next, not started"),
    ("**Prompt 11C is authorized to begin but has not started**",
     "**Prompt 11C is complete at the specification/documentation level**"),
    ("**Prompt 11C has not started and must not start before independent acceptance",
     "**Prompt 11C has been executed after the C3 acceptance"),
    ("**Prompt 11C has not started**", "**Prompt 11C is complete at the specification/documentation level**"),
    ("the next task is Prompt 11C", "the next task was Prompt 11C, now complete (log §72)"),
    ("and 11C is not started", "and 11C is complete at the specification/documentation level"),
    ("Prompt 11C is the next task, authorized by the C3 acceptance (§71), and not started**",
     "Prompt 11C was the next task, authorized by the C3 acceptance (§71), and has since completed (§72)**"),
    ("Prompt 11C — B-11 workflows, edge cases and acceptance — next and not started",
     "Prompt 11C — B-11 workflows, edge cases and acceptance — complete at the specification/documentation level (log §72)"),
    ("Prompt 11C is next and has not started; Prompt 11's parent stays open",
     "Prompt 11C is complete at the specification/documentation level (log §72); Prompt 11's parent stays open pending owner acceptance of the PARTIAL verdict"),
    ("11C next and not started", "11C complete (log §72); Prompt 12 next and not started"),
    # --- STATUS block values ---------------------------------------------- #
    ("stage_2_next_prompt: 11C", "stage_2_next_prompt: 12"),
]

B11_NEW = (
    "b11_progression: B-11 v1.0 specification complete at the documentation level (18_world_events_objectives_rankings_progression.md "
    "+ 50-ID formula register (49 active + 1 retired)); 723 WEP rules, 17 WPC contracts, 40 WPF codes, 50 WPA events; "
    "D-152..D-161 / DD-200..DD-209; UD-024 resolved, UD-050/UD-051 open; formula register 50 IDs (49 active + `F-WEP-048` retired), "
    "43 active structural (20 with Prompt 14 parameters, 23 without) and 6 Provisional; 11B-C2 integrity correction independently "
    "accepted by C3; **Prompt 11C complete at the specification/documentation level (log §72): canonical companion "
    "19_world_events_objectives_rankings_progression_workflows_integration_acceptance.md with 25 WJ journeys, 50 WWF workflows, "
    "84 WEE edge cases, 272 WTA tests (all Designed, not executed), 30 WTS threats, 11 WEG gaps, the 17 WPC contracts reused, "
    "and 20 gates at 11 PASS / 9 PARTIAL / 0 FAIL / 0 BLOCKED; validator 11C_validate_b11_workflows.py 34/34 with 9/9 positive and "
    "19/19 negative fixtures; Prompt 11 design closure now awaits owner acceptance of the PARTIAL verdict; the Supabase profile "
    "treasury UPDATE defect stays open and the prototype is not security-verified; Prompt 12 is next and is not authorized to start**"
)


def sync(path: pathlib.Path, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    before = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    text = re.sub(r"b11_progression: [^\n]*", B11_NEW, text, count=1)
    if label == "continuity":
        text = text.replace(
            "> **11B status (2026-11-05; current —",
            "> **11B status (2026-11-05; superseded by the 11C status above —", 1)
    if text != before:
        path.write_text(text, encoding="utf-8")
    print(f"{'CHANGED' if text != before else 'no-op  '} {path.name}")


ROOT = pathlib.Path(".")
TARGETS = ["AI_CONTEXT.md", "AI_HANDOFF.md", "PROJECT_PROGRESS.md", "ROADMAP.md",
           "stage-2/00_stage_2_handoff.md", "stage-2/01_stage_2_prompt_roadmap.md",
           "stage-2/06_stage_2_progress_log.md"]
for t in TARGETS:
    sync(ROOT / t, "continuity" if t.count("/") == 0 else "stage2")
