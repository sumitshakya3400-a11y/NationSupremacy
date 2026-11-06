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

STATUS_NEXT = re.compile(r"stage_2_next_prompt\s*:\s*(\d{1,2}[A-C]?)")


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

CURRENT_SUBPROMPT = "12"
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
# 2026-11-06 (Prompt 11C): the workflow/acceptance companion closed the whole
# Prompt 11 family at the specification/documentation level, so 11C joins the
# completed set. Its ACCEPTANCE is PARTIAL, which is tracked separately below:
# "specification-complete" and "accepted" are different states and must never
# be collapsed into one.
COMPLETED_SUBPROMPTS = ("07A", "07B", "07C", "08A", "08B", "08C", "09A", "09B", "09C",
                        "10A", "10B", "10C", "11A", "11B", "11C")

# The scheduled next Stage 2 prompt. There is no 12A/12B/12C split, so the
# prompt-level and sub-prompt-level values coincide; both names are kept so a
# caller that asks either question gets the same answer.
CURRENT_PROMPT = CURRENT_SUBPROMPT
NEXT_PROMPT = CURRENT_PROMPT

# Acceptance is not completion. A prompt can be specification-complete and still
# be unaccepted; 11C is exactly that. Only a recorded owner verdict changes this.
PROMPT_ACCEPTANCE = {"11C": "PARTIAL"}

# Prompts the roadmap has not started. "12" is the next scheduled stage; 14 is
# the calibration prompt, which must not be reported as begun or complete.
UNSTARTED_PROMPTS = ("12", "13", "14", "15")

# Owner-reserved decisions that no documentation pass may close.
OWNER_RESERVED_OPEN = tuple(f"UD-{i:03d}" for i in list(range(40, 50)) + [50, 51])

SUBPROMPT = re.compile(r"\b((?:0[789]|1[01])[A-C])\b")

# A prompt-level mention ends the region a sub-prompt claim can own. Without
# this, "11C is complete … so Prompt 12 is next and has not started" was read
# as an 11C claim, because Prompt 12 is not itself a sub-prompt match.
PROMPT_MENTION = re.compile(r"\bPrompt\s*0?\d{1,2}[A-C]?\b", re.IGNORECASE)

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


def _mask_labelled_parentheticals(line: str) -> str:
    """Blank bracketed records whose opening clause labels them as history.

    A label at the start of a parenthetical scopes to that whole record, the
    same way a line-opening label scopes to its line. The handoff's
    "(Historical, superseded: … Prompt 11C is authorized but has not started.)"
    record is historical even though the label is not at the line start.
    """
    masked = line
    start = line.find("(")
    while start != -1:
        depth = 0
        end = -1
        for index in range(start, len(line)):
            if line[index] == "(":
                depth += 1
            elif line[index] == ")":
                depth -= 1
                if depth == 0:
                    end = index
                    break
        if end == -1:
            break
        first = re.split(r"(?<=[.;])\s+", line[start + 1:end], maxsplit=1)[0]
        if HISTORICAL_MARKER.search(first):
            masked = masked[:start] + " " * (end - start + 1) + masked[end + 1:]
        start = line.find("(", end + 1)
    return masked


def status_clauses(text: str) -> list[str]:
    """Split into sentence-ish clauses so one sub-prompt's claim cannot leak.

    Table rows and prose lines are split further on `;` and `.`; that is enough
    to keep "07B is complete; 07C is next" apart without a full parser.
    """
    clauses: list[str] = []
    for line in text.splitlines():
        line = _mask_labelled_parentheticals(line).strip()
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
    # A labelled history label applies to the whole record, not just the clause
    # that happens to contain it. Splitting first lost the label, so the 11A
    # status block ("superseded by the 11B status above: … 11C is next") was
    # reported even though the record is explicitly historical.
    for line in text.splitlines():
        # Mask a labelled bracket first: its label scopes to the bracket, not to
        # the rest of the line. Only then may a marker that opens the remaining
        # record label the whole record. A marker elsewhere on the line exempts
        # only its own clause, so a live claim in a later clause is reported.
        line = _mask_labelled_parentheticals(line)
        if HISTORICAL_LINE_MARKER.match(line):
            continue
        for clause in (part.strip() for part in re.split(r"(?<=[.;])\s+", line.strip())):
            if not clause or HISTORICAL_MARKER.search(clause):
                continue
            for match in SUBPROMPT.finditer(clause):
                if match.group(1) not in completed:
                    continue
                rest = clause[match.end():]
                bounds = [m.start() for m in (SUBPROMPT.search(rest), PROMPT_MENTION.search(rest)) if m]
                tail = rest[: min(bounds)] if bounds else rest
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


# --- Cross-document status agreement (2026-11-06, Prompt 11C-C1) ------------
# Completing a prompt is not the same as accepting it, and neither is the same
# as implementing it. The 11C audit found a document that still said "11C … not
# started" while the status blocks said the prompt was complete, and a status
# model whose `CURRENT_SUBPROMPT` still named the finished prompt. The checks
# below compare *declarations* across documents instead of trusting each file
# separately. They stay lexical on purpose: the project has no database of
# status records, only Markdown that has to agree with itself.

STATUS_BLOCK = re.compile(r"<!-- STATUS:BEGIN -->(.*?)<!-- STATUS:END -->", re.S)
DECLARED_NEXT = re.compile(r"^stage_2_next_prompt\s*:\s*([0-9]{1,2}[A-C]?)\s*$", re.M)
ROADMAP_NEXT_ROW = re.compile(
    r"^\|\s*Next prompt\s*\|\s*(.*?)\s*\|\s*$", re.M
)
PROMPT_14_DONE = re.compile(
    r"\bprompt\s*14\b[^.\n]{0,80}\b(?:is|are|was|has been|have been)\s+"
    r"(?:now\s+)?(?:complete|completed|done|approved|calibrated|started)\b",
    re.IGNORECASE,
)
IMPLEMENTED_CLAIM = re.compile(
    r"\b(?:is|are|was|were|has been|have been)\s+(?:now\s+)?(?:fully\s+)?"
    r"(?:implemented|released|deployed|runtime-verified|playtested)\b",
    re.IGNORECASE,
)
OWNER_RESERVED_APPROVED = re.compile(
    r"\bUD-(?:04[0-9]|05[01])\b[^.\n]{0,80}\b(?:is|are|was|were|has been|have been)\s+"
    r"(?:now\s+)?(?:approved|resolved|closed|signed off)\b",
    re.IGNORECASE,
)
NEGATION_WORDS = {
    "no", "not", "nothing", "never", "without", "neither", "nor", "none", "cannot",
    "prohibit", "prohibited", "forbid", "forbidden", "unapproved", "unresolved",
    "outstanding", "pending", "open",
}

# A marker that opens the line/record labels the whole record (the 11A
# "superseded by …" status block). Markdown emphasis, quote and bracket markers
# may precede it.
HISTORICAL_LINE_MARKER = re.compile(
    r"^[\s>*_`\[\]()]*(" + HISTORICAL_MARKER.pattern + r")", re.IGNORECASE
)

CONTRAST = re.compile(r"\b(?:but|however|yet|although|though|whereas)\b|[.;]", re.IGNORECASE)


def _negation_applies(clause: str, match: re.Match[str]) -> bool:
    """True when a negation governs this specific claim, not merely the clause.

    Only the segment between the last contrast/sentence boundary and the match
    can suppress it. This keeps a mixed clause honest: "Nothing is implemented,
    but the event system is implemented" still reports the positive half.
    """
    prefix = clause[max(0, match.start() - 120):match.start()]
    parts = CONTRAST.split(prefix)
    lead = parts[-1] if parts else prefix
    tokens = {t.strip(".,;:()*`").lower() for t in (lead + " " + match.group(0)).split()}
    return bool(tokens & NEGATION_WORDS)


def declared_next_prompt(text: str) -> str | None:
    """The prompt a document says comes next, from its STATUS block or its row.

    Both forms are admitted because the continuity files carry a STATUS block
    while the Stage 2 handoff carries a `| Next prompt |` row. A document that
    declares neither returns None and is not compared.
    """
    block = STATUS_BLOCK.search(text)
    if block:
        match = DECLARED_NEXT.search(block.group(1))
        if match:
            return match.group(1)
    row = ROADMAP_NEXT_ROW.search(text)
    if row:
        match = PROMPT_NUMBER.search(row.group(1))
        if match:
            return match.group(1)
    return None


def continuity_problems(
    documents: dict[str, str],
    expected_next: str | None = None,
) -> list[str]:
    """Return disagreements between active status documents.

    `documents` is a name→text map of the live status surfaces. The checks are:

    1. every declared next prompt equals `expected_next` (default `NEXT_PROMPT`);
    2. no document presents a completed sub-prompt as still next / not started;
    3. no document presents the B-11 or 11C work as runtime-implemented;
    4. no owner-reserved decision is presented as approved or resolved;
    5. Prompt 14 is not presented as started, complete or calibrated.

    Historical prose is exempt only where it labels itself (the `HISTORICAL_MARKER`
    rule), and negated claims are exempt because they assert the opposite.
    """
    expected = expected_next or NEXT_PROMPT
    problems: list[str] = []

    declarations: dict[str, str] = {}
    for name, text in documents.items():
        value = declared_next_prompt(text)
        if value is not None:
            declarations[name] = value
    for name, value in sorted(declarations.items()):
        if value != expected:
            problems.append(
                f"{name}: declares next prompt {value!r}, expected {expected!r}"
            )
    if len({v for v in declarations.values()}) > 1:
        problems.append(f"status documents disagree on the next prompt: {declarations}")

    for name, text in documents.items():
        for excerpt in subprompt_status_problems(text):
            problems.append(f"{name}: completed sub-prompt presented as live: {excerpt}")

        for clause in status_clauses(text):
            if HISTORICAL_MARKER.search(clause):
                continue
            low = clause.lower()
            if "11c" in low or "b-11" in low or "prompt 11" in low:
                for match in IMPLEMENTED_CLAIM.finditer(clause):
                    if _negation_applies(clause, match):
                        continue
                    problems.append(f"{name}: specification presented as implementation: {clause[:150]}")
                    break
            for match in OWNER_RESERVED_APPROVED.finditer(clause):
                if _negation_applies(clause, match):
                    continue
                problems.append(f"{name}: owner-reserved decision presented as settled: {clause[:150]}")
                break
            for match in PROMPT_14_DONE.finditer(clause):
                if _negation_applies(clause, match):
                    continue
                problems.append(f"{name}: Prompt 14 presented as begun or complete: {clause[:150]}")
                break

    seen: set[str] = set()
    unique: list[str] = []
    for problem in problems:
        if problem not in seen:
            seen.add(problem)
            unique.append(problem)
    return unique
