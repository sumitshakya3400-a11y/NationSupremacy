#!/usr/bin/env python3
"""Bounded detectors for stale *current* next-action statements.

Why this exists (2026-10-23): phrase checks were not enough. `AI_CONTEXT.md`
carried sentences that still told a reader the next action was an earlier
Stage 2 prompt while the STATUS blocks, the handoff and the progress log all
named a later one. A whole-repository ban on the words "Prompt 01" would be
wrong: completed-work summaries, closure records and the roadmap may
legitimately mention earlier prompts.

The rule implemented here is deliberately narrow:

* Only text blocks/lines that *assert a next action* are examined (a unit
  containing "next action", "next task", "next activity", "next authorized
  task", "next prompt" or "next =").
* A unit is stale only if it names one or more prompt numbers, **none** of them
  is at least the current prompt, and it carries no historical marker
  ("historical", "superseded", "at the time", "re-pointed", "then completed",
  ...).

So "Next action: Prompt 04" passes while "Next action: Prompt 03" fails once 04
is current; "*Historical:* the next action was Prompt 01; Prompt 04 is next"
passes. The current prompt is read from a STATUS block when present, otherwise
the caller's default applies.

Documentation QA only — no game code, no dependencies beyond the stdlib.
"""

from __future__ import annotations

import re

# A unit that says what comes next.
CURRENT_MARKER = re.compile(
    r"next\s+(?:authorized\s+)?(?:action|task|activity)|next\s+prompt|next\s*=",
    re.IGNORECASE,
)

# A unit that explicitly frames itself as history or as a superseded state.
HISTORICAL_MARKER = re.compile(
    r"historical|superseded|has since|at the time|re-pointed|was the next|"
    r"then completed|then executed|no longer|previously|were each detected",
    re.IGNORECASE,
)

# "Prompt 01", "Prompt 1", "next prompt = 02" — never "Prompt 10" as "Prompt 1".
PROMPT_NUMBER = re.compile(r"(?:Prompt\s*0?|prompt\s*=\s*0?)(\d{1,2})(?!\d)", re.IGNORECASE)

STATUS_NEXT = re.compile(r"stage_2_next_prompt\s*:\s*(\d{1,2}[A-D]?)")


def text_blocks(text: str) -> list[str]:
    """Split on blank lines; Markdown headings stay attached to their body."""
    return [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]


def text_units(text: str) -> list[str]:
    """Blocks *and* single lines.

    A Markdown table row is its own instruction, but it shares a block with
    every other row of that table — so a row saying "next action = Prompt 02"
    would be hidden by a neighbouring row that names the current prompt. Lines
    are therefore inspected as well; the block pass still catches a bare heading
    whose body sits in the next paragraph.
    """
    units: list[str] = []
    for block in text_blocks(text):
        units.extend(line.strip() for line in block.splitlines() if line.strip())
        units.append(block)
    return units


def status_next_prompt(text: str) -> str | None:
    """Return the value of `stage_2_next_prompt` in the STATUS block, if any."""
    match = STATUS_NEXT.search(text)
    return match.group(1) if match else None


def stale_next_actions(text: str, current_prompt: int = 4) -> list[str]:
    """Return a short excerpt for every unit that still makes an old prompt current."""
    status = status_next_prompt(text)
    if status:
        # "09C" advances the prompt-number floor to 09; the letter suffix only
        # selects the sub-prompt and must not defeat the numeric comparison.
        digits = re.match(r"\d{1,2}", status)
        if digits:
            current_prompt = int(digits.group(0))
    stale: list[str] = []
    seen: set[str] = set()
    for unit in text_units(text):
        if not CURRENT_MARKER.search(unit):
            continue
        if HISTORICAL_MARKER.search(unit):
            continue
        numbers = {int(n) for n in PROMPT_NUMBER.findall(unit)}
        if numbers and not any(n >= current_prompt for n in numbers):
            flat = re.sub(r"\s+", " ", unit)
            if flat not in seen:
                seen.add(flat)
                stale.append(flat[:140])
    return stale


# --- Sub-prompt level (2026-10-29) -----------------------------------------
# Prompt 07 is split into 07A/07B/07C and Prompt 08 into 08A/08B/08C. The
# prompt-number rule above cannot see that distinction: 07B and 07C are both
# "Prompt 07", and 08A/08B/08C are all "Prompt 08", so a sentence saying "07B
# is the next intended task" (2026-10-29) or "08A is the next intended task"
# would pass every prompt-number check while the progress log, the handoff
# header and the roadmap said that sub-prompt was complete.
# This rule works at sub-prompt level and stays scoped to *current-status*
# claims: a labelled history ("was the next", "at the time") is ignored, and a
# claim is attributed to a sub-prompt only up to the next sub-prompt mention,
# so "07B is complete; 07C is next" is never read as a 07B claim.

CURRENT_SUBPROMPT = "13D"
# 2026-10-29: Prompt 08 is split too, so 08A joins the completed set.
# 2026-10-30: 08B is complete as well, so it is caught the same way, and
# 08C closes the set.
# 2026-11-03: Prompt 09 is split into 09A research, 09B specification and 09C
# workflow/acceptance; all three are complete, so Prompt 10 is next.
# 2026-11-03 (Prompt 10A): Prompt 10 is split the same way — 10A research is
# complete, so 10A joins the completed set and the live sub-prompt becomes 10B.
# 2026-11-03 (Prompt 10B): 10B specification is complete, so 10B joins the
# completed set and the live sub-prompt becomes 10C.
# 2026-11-04 (Prompt 10C): the 10C workflow/acceptance companion is complete,
# so 10C joins the completed set and the whole Prompt 10 parent is closed at the
# specification/documentation level; the live prompt is now Prompt 11.
# 2026-11-04 (Prompt 11A): Prompt 11 is split into 11A research, 11B foundations
# and 11C workflows, the same shape as the 10 family. 11A is complete at the
# research/design-foundations level.
# 2026-11-05 (Prompt 11B): the B-11 specification is complete at the
# system-specification level, so 11B joins the completed set and the live
# sub-prompt becomes 11C. 11C is not complete, so Prompt 11 stays open.
# 2026-11-06 (Prompt 11C): the B-11 workflow/acceptance companion closes the
# 11 family at the specification/documentation level; Prompt 12 opens.
# 2026-11-06 (Prompt 12A): Prompt 12 is split into 12A research and design
# foundations, 12B the B-12 specification and 12C workflows and acceptance, the
# same shape as the 10 and 11 families. 12A is complete at the research level,
# so the live sub-prompt is 12B and the regex gains the 12 family — without it
# "12A" was not a recognised sub-prompt token at all.
# 2026-11-06 (Prompt 12A closure): 12A joins the completed set, so the live
# sub-prompt is 12B and a sentence naming 12A as next is now stale.
# 2026-11-07 (Prompt 12B): the B-12 specification closed, so 12B joins the set.
# 2026-11-10 (Prompt 12C): the 12C workflows, integration and acceptance
# companions closed the 12 family at the specification/documentation level, so
# 12C joins the completed set and the live prompt is Prompt 13.
# 2026-11-11 (Prompt 13A): Prompt 13 is split into 13A research, architecture
# and design foundations and 13B screen and component specifications, the same
# shape as the 10, 11 and 12 families. 13A is complete at the research level, so
# it joins the completed set and the live sub-prompt becomes 13B — which is why
# the SUBPROMPT token range now reaches the 13 family.
COMPLETED_SUBPROMPTS = ("07A", "07B", "07C", "08A", "08B", "08C", "09A", "09B", "09C",
                        "10A", "10B", "10C", "11A", "11B", "11C", "12A", "12B", "12C",
                        "13A", "13B", "13C")

SUBPROMPT = re.compile(r"\b((?:0[789]|1[0-3])[A-D])\b")

NEXT_TASK_CLAIM = re.compile(
    r"\b(?:is|remains|stays)\s+(?:still\s+)?the\s+next(?:\s+(?:intended|outstanding|authorized))?"
    r"\s+(?:task|action|activity|prompt)\b",
    re.IGNORECASE,
)

NOT_STARTED_CLAIM = re.compile(
    r"\b(?:has|had|have)\s+not\s+(?:yet\s+)?(?:been\s+)?started\b|"
    r"\b(?:hasn't|haven't|hadn't)\s+(?:yet\s+)?started\b|"
    r"\bnot\s+yet\s+begun\b",
    re.IGNORECASE,
)

PENDING_CLAIM = re.compile(r"\b(?:is|remains)\s+(?:still\s+)?pending\b", re.IGNORECASE)

# "**Next action:** Prompt 07B ..." or "its next outstanding task is **Prompt
# 07C ..." — the claim precedes the identifier. The optional `Prompt` token is
# needed for the second form: without it the prefix ends at "**Prompt ", which
# is not the end of the clause and the 2026-10-29 handoff sentence escaped.
NEXT_TASK_PREFIX = re.compile(
    r"next(?:\s+(?:intended|outstanding|authorized))?\s+(?:task|action|prompt|activity)"
    r"\s*(?::|=|\bis\b|\u2014|-)?\s*\**\s*(?:Prompt\s*)?$",
    re.IGNORECASE,
)


def status_clauses(text: str) -> list[str]:
    """Split into sentence-ish clauses so one sub-prompt's claim cannot leak.

    Table rows and prose lines are split further on `;` and `.`; that is enough
    to keep "07B is complete; 07C is next" apart without a full parser.
    """
    clauses: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        clauses.extend(part.strip() for part in re.split(r"(?<=[.;])\s+", line) if part.strip())
    return clauses


def subprompt_status_problems(
    text: str,
    completed: tuple[str, ...] = COMPLETED_SUBPROMPTS,
) -> list[str]:
    """Return excerpts where a *completed* sub-prompt is still described as live.

    A problem is a current-status clause that says a completed sub-prompt is
    "the next ... task" (or is not started / still pending). Labelled history is
    skipped; the claim is truncated at the next sub-prompt mention.
    """
    problems: list[str] = []
    seen: set[str] = set()
    for clause in status_clauses(text):
        if HISTORICAL_MARKER.search(clause):
            continue
        for match in SUBPROMPT.finditer(clause):
            if match.group(1) not in completed:
                continue
            rest = clause[match.end():]
            following = SUBPROMPT.search(rest)
            tail = rest[: following.start()] if following else rest
            prefix = clause[: match.start()]
            flagged = bool(
                NEXT_TASK_CLAIM.search(tail)
                or NOT_STARTED_CLAIM.search(tail)
                or PENDING_CLAIM.search(tail)
                or NEXT_TASK_PREFIX.search(prefix)
            )
            if not flagged:
                continue
            flat = re.sub(r"\s+", " ", clause)
            if flat not in seen:
                seen.add(flat)
                problems.append(flat[:160])
    return problems
