#!/usr/bin/env python3
"""Targeted documentation QA for the Prompt 09A Alliance research package.

This validator exists because the general validators passed while the Alliance
matrix cited requirements that existed but did not support the integration.
It checks the *structure of the evidence*, not the truth of the research:

  1. AX completeness and unique IDs.
  2. Every cited REQ/decision/UD/formula identifier exists.
  3. Every AX-to-REQ pair has a relationship classification.
  4. Every DIRECT DEPENDENCY has a substantive evidence sentence, and a
     supporting/related reference is not presented as a direct dependency.
  5. Subsystem ownership: Economy, City, Diplomacy, Military and Global Trade
     are never reassigned to Alliance.
  6. Discord and real-time communication exclusions survive in the documents.
  7. The 120 Alliance requirements (84 09A candidates plus 36 owner-authorized
     09B rows) and the unresolved-decision rows are intact, and
     their dependency cells do not cite the stale references.
  8. One consistent current status: 09A accepted, Phase 09B accepted at the
     specification/documentation level, 09C registered next and not started.
  9. The Politics & War permission inventory has 15 sourced rows and a
     comparison table.
 10. Forum sources use exact thread permalinks, not the forum root.
 11. Change logs exist for the matrix, source register and research report.

Run:  python docs/qa_backups/09A_validate_alliance.py [docs-root]
Exit 0 = all checks pass. Exit 1 = at least one failure.

Documentation QA only; stdlib only; no network access.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ALLOWED = {
    "DIRECT DEPENDENCY",
    "RELATED CONSTRAINT",
    "SUPPORTING CONTEXT",
    "NO VALID RELATIONSHIP",
    "NO EXISTING REQUIREMENT",
    "OWNER DECISION REQUIRED",
}

FORBIDDEN_PAIRS = {
    ("AX-01", "REQ-012"),
    ("AX-01", "REQ-176"),
    ("AX-02", "REQ-176"),
    ("AX-03", "REQ-012"),
    ("AX-04", "REQ-012"),
    ("AX-06", "REQ-530"),
    ("AX-08", "REQ-530"),
    ("AX-09", "REQ-012"),
    ("AX-11", "REQ-530"),
    ("AX-16", "REQ-532"),
    ("AX-17", "REQ-532"),
}

PERMISSIONS = [
    "View Bank",
    "Withdraw Bank",
    "Change Permissions",
    "See Spies",
    "See Reset Timers",
    "Tax Brackets",
    "Post Announcements",
    "Manage Announcements",
    "Manage Applicants",
    "Remove Members",
    "Edit Alliance Info",
    "Manage Treaties",
    "Manage Market Share",
    "Manage Embargoes",
    "Promote Self to Leader",
]

BANNED_OWNERSHIP = [
    r"alliance\s+(owns|controls|dictates)\s+(the\s+)?(resource value|ledger|national diplomacy|military|city development)",
    r"alliance\s+leader\s+(may|can|consents|signs|binds)",
    r"alliance\s+(may|can)\s+(impose|declare)\s+(an?\s+)?(b-08\s+)?embargo",
    r"alliance\s+owns\s+national\s+consent",
]

BANNED_COMMUNICATION = [
    r"(discord bot|oauth|role sync|role synchroni[sz]ation|message mirroring|real-time (alliance )?chat|websocket)[^.\n]{0,90}(approved|included|required|part of the (first )?release|will be built)",
    r"(approved|included|required|part of the (first )?release|will be built)[^.\n]{0,90}(discord bot|oauth|role sync|real-time (alliance )?chat|websocket)",
]

STALE_NEXT = [
    "Prompt 09 — the Alliance System — is the next task and has not started",
    "Prompt 09 has not started",
    "Prompt 09 is next",
    "Prompt 09A is next",
    "Prompt 09A has not started",
    "Prompt 09C is next",
    "Prompt 09C has not started",
    "Prompt 09C is registered next",
]

CURRENT_STATUS = (
    "phase 09b alliance specification and documentation: accepted."
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def section(text: str, start: str, end: str | None = None) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(end, i + len(start)) if end else -1
    return text[i : j if j >= 0 else len(text)]


def norm_class(value: str) -> str:
    return re.sub(r"[*`]", "", value).strip().upper()


def table_rows(block: str, prefix: str, width: int) -> list[list[str]]:
    out: list[list[str]] = []
    for line in block.splitlines():
        if line.startswith(prefix):
            row = cells(line)
            if len(row) == width:
                out.append(row)
    return out


def validate(docs: Path) -> tuple[list[str], int]:
    """Return (problems, checks_run). Each problem is 'group :: message'."""
    problems: list[str] = []
    checks = 0

    def check(ok: bool, group: str, message: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            problems.append(f"{group} :: {message}")

    matrix_p = docs / "stage-2" / "research" / "09A_alliance_integration_matrix.md"
    research_p = docs / "stage-2" / "research" / "09A_alliance_research.md"
    sources_p = docs / "stage-2" / "research" / "09A_alliance_sources_findings.md"
    review_p = docs / "stage-2" / "research" / "09A_alliance_reference_review.md"
    req_p = docs / "stage-2" / "03_requirements_traceability.md"
    dec_p = docs / "stage-2" / "04_approved_and_provisional_decisions.md"
    ud_p = docs / "stage-2" / "05_unresolved_design_decisions.md"
    handoff_p = docs / "stage-2" / "00_stage_2_handoff.md"
    roadmap_p = docs / "stage-2" / "01_stage_2_prompt_roadmap.md"
    log_p = docs / "stage-2" / "06_stage_2_progress_log.md"
    root_roadmap_p = docs / "ROADMAP.md"
    progress_p = docs / "PROJECT_PROGRESS.md"
    context_p = docs / "AI_CONTEXT.md"
    ai_handoff_p = docs / "AI_HANDOFF.md"
    decisions_p = docs / "DECISIONS.md"
    outline_p = docs / "stage-2" / "02_master_game_design_bible_outline.md"

    required = [
        matrix_p, research_p, sources_p, review_p, req_p, dec_p, ud_p,
        handoff_p, roadmap_p, log_p, root_roadmap_p, progress_p,
        context_p, ai_handoff_p, decisions_p, outline_p,
    ]
    missing = [p for p in required if not p.exists()]
    check(not missing, "1-structure", f"missing documents: {[str(p) for p in missing]}")
    if missing:
        return problems, checks

    matrix = read(matrix_p)
    research = read(research_p)
    sources = read(sources_p)
    review = read(review_p)
    req = read(req_p)
    dec = read(dec_p)
    ud = read(ud_p)
    handoff = read(handoff_p)
    roadmap = read(roadmap_p)
    log = read(log_p)
    root_roadmap = read(root_roadmap_p)
    progress = read(progress_p)
    context = read(context_p)
    ai_handoff = read(ai_handoff_p)
    decisions = read(decisions_p)
    outline = read(outline_p)

    # --- 1. AX structure -----------------------------------------------------
    summary = table_rows(section(matrix, "## 2.", "## 3."), "| AX-", 10)
    audit = table_rows(section(matrix, "## 3.", "## 4."), "| AX-", 7)
    fields = table_rows(section(matrix, "## 4.", "## 5."), "| AX-", 10)

    summary_ids = [r[0] for r in summary]
    expected_ids = [f"AX-{i:02d}" for i in range(1, 27)]
    check(summary_ids == expected_ids, "1-structure", f"summary AX IDs are not AX-01..AX-26 in order: {summary_ids}")
    check(len(set(summary_ids)) == len(summary_ids), "1-structure", "duplicate AX ID in summary")
    audit_ids = sorted({r[0] for r in audit})
    check(audit_ids == expected_ids, "1-structure", f"audit does not cover all AX IDs: {audit_ids}")
    check(len(fields) == 26, "1-structure", f"fields 12–20 table has {len(fields)} rows, expected 26")
    check(all(r[0] in expected_ids for r in fields), "1-structure", "fields table has an unknown AX ID")

    for row in summary:
        check(all(row[i] for i in (1, 2, 3, 4, 5, 6, 7, 8, 9)), "1-structure", f"{row[0]} summary row has an empty required field")
    for row in audit:
        check(all(row[i] for i in (0, 1, 2, 3, 4, 5)), "1-structure", f"{row[0]} audit row has an empty field: {row}")
    pairs = [(r[0], r[1]) for r in audit if r[1] != "—"]
    check(len(pairs) == len(set(pairs)), "1-structure", "duplicate AX/REQ audit pair")

    # --- 2. Identifier existence --------------------------------------------
    req_ids = {f"REQ-{n:03d}" for n in range(1, 618)}
    found_req_rows = {
        m.group(1)
        for m in re.finditer(r"^\| (REQ-\d{3}) \|", req, flags=re.MULTILINE)
    }
    check(len(found_req_rows) == 763, "2-references", f"requirement register has {len(found_req_rows)} unique rows, expected 763")
    for _, rid in pairs:
        check(rid in req_ids, "2-references", f"audit cites nonexistent requirement {rid}")
        check(rid in found_req_rows, "2-references", f"audit cites {rid}, which has no register row")

    dec_ids = set(re.findall(r"\bD-\d{3}\b", dec)) | set(re.findall(r"\bDD-\d{3}\b", dec))
    ud_ids = set(re.findall(r"\bUD-\d{3}\b", ud))
    for token in sorted(set(re.findall(r"\b(?:D|DD)-\d{3}\b", matrix))):
        check(token in dec_ids or token in set(re.findall(r"\bD-\d{3}\b", decisions)), "2-references", f"matrix cites missing decision {token}")
    for token in sorted(set(re.findall(r"\bUD-\d{3}\b", matrix))):
        check(token in ud_ids, "2-references", f"matrix cites missing unresolved decision {token}")
    for token in sorted(set(re.findall(r"\bDIP-\d{3}\b", matrix))):
        check(token in read(docs / "stage-2" / "15_diplomacy.md"), "2-references", f"matrix cites missing DIP rule {token}")
    for token in sorted(set(re.findall(r"\bECN-\d{3}\b", matrix))):
        check(token in read(docs / "stage-2" / "10_economy_resources_treasury_and_finances.md"), "2-references", f"matrix cites missing ECN rule {token}")
    for token in sorted(set(re.findall(r"\bF-[A-Z]{2}-\d{3}[a-z]?\b", matrix))):
        check(any(token in read(p) for p in docs.glob("stage-2/*formula_register.md")), "2-references", f"matrix cites missing formula {token}")

    # --- 3. Classifications --------------------------------------------------
    class_counts = {k: 0 for k in ALLOWED}
    for row in audit:
        cls = norm_class(row[3])
        check(cls in ALLOWED, "3-classification", f"{row[0]}/{row[1]} has invalid classification {row[3]!r}")
        if cls in class_counts:
            class_counts[cls] += 1
        if cls == "NO VALID RELATIONSHIP":
            check(False, "3-classification", f"{row[0]}/{row[1]} leaves NO VALID RELATIONSHIP in the canonical matrix")
        if cls == "NO EXISTING REQUIREMENT":
            check(row[1] == "—", "3-classification", f"{row[0]} marks no existing requirement but cites {row[1]}")

    # Counts recorded in the review record must match the matrix.
    review_counts = {}
    for label, key in [
        ("Requirement relationships reviewed", "relationships"),
        ("Direct dependencies retained", "DIRECT DEPENDENCY"),
        ("Related constraints retained", "RELATED CONSTRAINT"),
        ("Supporting-context references retained", "SUPPORTING CONTEXT"),
        ("Invalid references removed", "removed"),
        ("AX records with an explicit no-existing-requirement row", "no_existing_ax"),
        ("AX records with an owner decision or future-prompt gate", "gated"),
    ]:
        m = re.search(rf"\| {re.escape(label)} \| (\d+) \|", review)
        review_counts[key] = int(m.group(1)) if m else None
    check(review_counts["relationships"] == len(audit), "3-classification", f"review records {review_counts['relationships']} relationships, matrix has {len(audit)}")
    check(review_counts["DIRECT DEPENDENCY"] == class_counts["DIRECT DEPENDENCY"], "3-classification", f"review records {review_counts['DIRECT DEPENDENCY']} direct dependencies, matrix has {class_counts['DIRECT DEPENDENCY']}")
    check(review_counts["RELATED CONSTRAINT"] == class_counts["RELATED CONSTRAINT"], "3-classification", f"review records {review_counts['RELATED CONSTRAINT']} related constraints, matrix has {class_counts['RELATED CONSTRAINT']}")
    check(review_counts["SUPPORTING CONTEXT"] == class_counts["SUPPORTING CONTEXT"], "3-classification", f"review records {review_counts['SUPPORTING CONTEXT']} supporting references, matrix has {class_counts['SUPPORTING CONTEXT']}")
    no_existing_ax = len({r[0] for r in audit if norm_class(r[3]) == "NO EXISTING REQUIREMENT"})
    check(review_counts["no_existing_ax"] == no_existing_ax, "3-classification", f"review records {review_counts['no_existing_ax']} no-requirement AX records, matrix has {no_existing_ax}")

    # --- 4. Evidence and stale pairs ----------------------------------------
    for row in audit:
        cls = norm_class(row[3])
        evidence = row[4]
        if cls == "DIRECT DEPENDENCY":
            check(len(evidence) >= 60, "4-evidence", f"{row[0]}/{row[1]} direct dependency has a short evidence text")
            check(len(evidence.split()) >= 8, "4-evidence", f"{row[0]}/{row[1]} direct evidence is a placeholder, not an explanation")
        if cls in ("RELATED CONSTRAINT", "SUPPORTING CONTEXT"):
            check(len(evidence) >= 30, "4-evidence", f"{row[0]}/{row[1]} {cls} has no substantive evidence")
            check("direct dependency" not in evidence.lower() or "not a direct" in evidence.lower(), "4-evidence", f"{row[0]}/{row[1]} supporting/related row is described as a direct dependency")

    for ax, rid in FORBIDDEN_PAIRS:
        bad = [r for r in audit if r[0] == ax and r[1] == rid]
        check(not bad, "4-evidence", f"stale pair {ax}/{rid} is still in the canonical audit table")
        removed_block = section(matrix, "## 6.", "## 7.")
        check(ax in removed_block and rid in removed_block, "4-evidence", f"removed pair {ax}/{rid} is not recorded in the correction table")

    # --- 5. Ownership boundaries --------------------------------------------
    owner_expectations = {
        "AX-06": ("Economy",),
        "AX-07": ("Economy",),
        "AX-08": ("Economy",),
        "AX-11": ("Cities",),
        "AX-15": ("Diplomacy",),
        "AX-16": ("Diplomacy",),
        "AX-17": ("Diplomacy", "Economy"),
        "AX-18": ("Military",),
        "AX-26": ("Market",),
    }
    for ax, needles in owner_expectations.items():
        row = next((r for r in summary if r[0] == ax), None)
        check(row is not None and all(n.lower() in row[3].lower() for n in needles), "5-ownership", f"{ax} does not name the owning system correctly: {row[3] if row else 'missing'}")
        check(row is not None and row[3].strip().lower() != "alliance", "5-ownership", f"{ax} assigns ownership to Alliance")

    owner_section = section(matrix, "## 5.", "## 6.")
    for needle in [
        "B-04 owns", "B-08 owns", "B-05 owns", "B-10 owns", "B-12 owns",
        "Alliance may not do", "No existing canonical document was modified",
    ]:
        check(needle in owner_section, "5-ownership", f"ownership section is missing {needle!r}")
    for pattern in BANNED_OWNERSHIP:
        check(not re.search(pattern, matrix, flags=re.IGNORECASE), "5-ownership", f"matrix reassigns an owning rule to Alliance: /{pattern}/")
    for token in ("REQ-513", "D-122", "DD-136", "G-1", "G-6"):
        check(token in matrix, "5-ownership", f"Global Trade boundary token {token} is missing from the matrix")
    check("release-gated" in matrix.lower() or "release gated" in matrix.lower(), "5-ownership", "matrix does not preserve the Global Trade release gate")

    # --- 6. Discord / communication -----------------------------------------
    check("Excluded permanently unless the owner changes D-133" in research, "6-communication", "research lacks the permanent exclusion statement")
    for word in ("chat", "bots", "OAuth", "role sync", "mirroring"):
        check(word.lower() in research.lower(), "6-communication", f"research exclusion list is missing {word!r}")
    check("Member discussion | **Not provided**" in research, "6-communication", "research no longer marks in-game member discussion as not provided")
    check("Optional, unlinked" in research, "6-communication", "research no longer states that Discord identity is optional and unlinked")
    check("no real-time chat" in dec.lower(), "6-communication", "DD-147 no longer records the no-real-time-chat constraint")
    check("no discord bot" in dec.lower(), "6-communication", "DD-147 no longer records the no-Discord-bot constraint")
    check("chat" in decisions.lower(), "6-communication", "DECISIONS does not record D-133")
    for pattern in BANNED_COMMUNICATION:
        check(not re.search(pattern, research, flags=re.IGNORECASE), "6-communication", f"research reintroduces excluded communication: /{pattern}/")
    ax19 = next((r for r in summary if r[0] == "AX-19"), None)
    ax20 = next((r for r in summary if r[0] == "AX-20"), None)
    check(ax19 is not None and "static" in ax19[1].lower(), "6-communication", "AX-19 is no longer a static link integration")
    check(ax20 is not None and "asynchronous" in (ax20[1] + " " + ax20[2]).lower(), "6-communication", "AX-20 is no longer asynchronous")
    cand_rows = {r[0]: r for r in table_rows(req, "| REQ-", 9)}
    for rid, row in cand_rows.items():
        if 534 <= int(rid.split("-")[1]) <= 653:
            joined = " ".join(row)
            if re.search(r"discord bot|oauth|role sync|real-time chat|websocket", joined, flags=re.IGNORECASE):
                check(re.search(r"\bno\b|not part|excluded|never", joined, flags=re.IGNORECASE) is not None, "6-communication", f"candidate requirement {rid} appears to add an excluded communication feature")

    # --- 7. Requirements and decisions --------------------------------------
    check(len(cand_rows) == 763, "7-register", f"requirement table parsed {len(cand_rows)} rows, expected 763")
    alliance_rows = [r for rid, r in cand_rows.items() if 534 <= int(rid.split("-")[1]) <= 653]
    check(len(alliance_rows) == 120, "7-register", f"Alliance requirement count is {len(alliance_rows)}, expected 120")
    check(all(r[3].startswith("Approved") or r[3].startswith("Proposed") or r[3].startswith("Provisional") or "Open" in r[3] or "Deferred" in r[3] for r in alliance_rows), "7-register", "an Alliance requirement is not Approved, Proposed, Provisional, Open or Deferred")
    status_counts = {}
    for r in cand_rows.values():
        key = re.sub(r"[*]", "", r[3]).split("(")[0].strip()
        status_counts[key] = status_counts.get(key, 0) + 1
    check(status_counts.get("Approved") == 55, "7-register", f"Approved count is {status_counts.get('Approved')}, expected 55")
    check(status_counts.get("Open") == 19, "7-register", f"Open count is {status_counts.get('Open')}, expected 19")
    check(status_counts.get("Provisional") == 688, "7-register", f"Provisional count is {status_counts.get('Provisional')}, expected 688")
    check(status_counts.get("Deferred") == 1, "7-register", f"Deferred count is {status_counts.get('Deferred')}, expected 1")
    check(status_counts.get("Proposed", 0) == 0, "7-register", "Proposed count is 0")

    bad_deps = {
        "REQ-534": "REQ-012",
        "REQ-535": "REQ-530",
        "REQ-548": "REQ-038",
        "REQ-562": "REQ-009",
        "REQ-571": "REQ-085",
        "REQ-576": "REQ-517",
        "REQ-579": "REQ-532",
    }
    for rid, bad in bad_deps.items():
        row = cand_rows.get(rid)
        check(row is not None and bad not in row[7], "7-register", f"candidate {rid} still depends on the invalid {bad}")

    for needle in ("D-133", "DD-147", "DD-148", "DD-149", "DD-150"):
        check(needle in dec or needle in decisions, "7-register", f"missing decision {needle}")
    for needle in ("UD-039", "UD-040", "UD-049"):
        check(needle in ud, "7-register", f"missing unresolved decision {needle}")
    check(re.search(r"\| DD-148 \|[^\n]*\| \*\*Provisional\*\*", dec) is not None, "7-register", "DD-148 is not Provisional")
    check(re.search(r"\| DD-149 \|[^\n]*\| \*\*Approved\*\*", dec) is not None, "7-register", "DD-149 is not Approved")
    check(re.search(r"\| DD-150 \|[^\n]*\| \*\*Approved\*\*", dec) is not None, "7-register", "DD-150 is not Approved")
    ud039_row = next((l for l in ud.splitlines() if l.startswith("| UD-039 |")), "")
    check("Resolved by D-137" in ud039_row, "7-register", "UD-039 is not recorded as resolved by D-137")
    ud039_lower = ud039_row.lower()
    check(
        "no alliance-level treaty object" in ud039_lower
        or "does not reuse the b-08 object" in ud039_lower,
        "7-register",
        "UD-039 resolution does not state the no-object or separate-object outcome",
    )
    check("zero diplomatic delegation" in ud039_lower,
          "7-register", "UD-039 resolution does not state the zero-delegation outcome")
    ud039_research = section(research, "## 17.", "## 18.")
    check("not option (a)" in ud039_research, "7-register", "research §17 mislabels the no-object recommendation as option (a)")
    check("outside UD-039" in ud039_research, "7-register", "research §17 does not state that the no-object path is outside UD-039's recorded options")

    # --- 8. Handoff / next action -------------------------------------------
    handoff_next = section(handoff, "## 10. Next action", "## 11.")
    check("Prompt 10" in handoff_next, "8-handoff", "Stage 2 handoff §10 does not name Prompt 10 as next")
    check("10C" in handoff_next and "next" in handoff_next.lower(), "8-handoff", "Stage 2 handoff §10 does not record 10C next")
    check("10B" in handoff_next and "complete" in handoff_next.lower(), "8-handoff", "Stage 2 handoff §10 does not record 10B complete")
    check(not re.search(r"09B[^.\n]{0,40}has not started", handoff_next, re.I), "8-handoff", "Stage 2 handoff §10 still says Prompt 09B has not started")
    opening = handoff.split("## 1.", 1)[0]
    check("09A" in opening and "accepted" in opening.lower(), "8-handoff", "handoff opening does not record 09A accepted")
    check("09B" in opening, "8-handoff", "handoff opening does not name 09B next")

    roadmap_row = next((l for l in roadmap.splitlines() if l.startswith("| 09 |")), "")
    check("09A" in roadmap_row and ("accepted" in roadmap_row.lower() or "complete" in roadmap_row.lower()), "8-handoff", f"prompt roadmap row 09 does not record 09A accepted: {roadmap_row[:160]}")
    check("09B" in roadmap_row or "09C" in roadmap_row, "8-handoff", "prompt roadmap row 09 does not name 09B or 09C")
    check("09D" not in roadmap_row, "8-handoff", "prompt roadmap row 09 names 09D as the next action")

    log_header = "\n".join(log.splitlines()[:40])
    check("Prompt 10" in log_header, "8-handoff", "progress-log header does not name Prompt 10 next")
    check("09A" in log_header and "accepted" in log_header.lower(), "8-handoff", "progress-log header does not record 09A accepted")

    for name, text in (("ROADMAP", root_roadmap), ("PROJECT_PROGRESS", progress), ("AI_CONTEXT", context), ("AI_HANDOFF", ai_handoff)):
        check("09A" in text and "09B" in text, "8-handoff", f"{name} does not record 09A and 09B")
        check("09A" in text and "accepted" in text.lower(), "8-handoff", f"{name} does not record 09A accepted")
    for stale in STALE_NEXT:
        for name, text in (("handoff", handoff), ("roadmap", roadmap), ("progress", progress), ("AI_CONTEXT", context), ("AI_HANDOFF", ai_handoff)):
            check(stale not in text, "8-handoff", f"{name} contains stale next-action phrase: {stale!r}")
    status = re.search(r"stage_2_next_prompt:\s*(\d{1,2}[A-C]?)", context)
    # 2026-11-03 (Prompt 10A): the parent Prompt 10 is split into 10A/10B/10C;
    # the live sub-prompt is 10B, and the bare 10 remains valid history.
    # 2026-11-04 (Prompt 10C): 10C closed, so the live prompt is 11.
    # 2026-11-05 (Prompt 11A): Prompt 11 split into 11A/11B/11C and 11A closed,
    # so the live sub-prompt is 11B; the bare 11 and the whole 10 family remain
    # valid history elsewhere in the same block.
    # 2026-11-06 (Prompt 11C): the 11C companion closed the Prompt 11 family at
    # the design level, so the live prompt is 12; 10/11 remain valid history.
    # 2026-11-07 (Prompt 12A review remediation): 12A closed, so 12B is live.
    check(status is not None and re.fullmatch(r"(?:10[A-C]?|11[A-C]?|12B?)", status.group(1)) is not None,
          "8-handoff", "AI_CONTEXT status block does not set Prompt 10/10A/10B/10C, 11/11A/11B/11C or 12/12B as the active prompt")

    # --- 9. Permissions inventory -------------------------------------------
    perm_block = section(research, "### 7.2", "### 7.3")
    perm_rows = [cells(l) for l in perm_block.splitlines() if re.match(r"\| \d{1,2} \|", l)]
    perm_rows = [r for r in perm_rows if len(r) == 5]
    check(len(perm_rows) == 15, "9-permissions", f"permission inventory has {len(perm_rows)} rows, expected 15")
    check([r[1] for r in perm_rows] == PERMISSIONS, "9-permissions", f"permission names/order differ: {[r[1] for r in perm_rows]}")
    for row in perm_rows:
        check(len(row[2]) >= 40, "9-permissions", f"permission {row[1]} has no exact description")
        check(row[2].startswith("“") or '"' in row[2], "9-permissions", f"permission {row[1]} description is not quoted from the source")
        check(row[4] not in ("", "—"), "9-permissions", f"permission {row[1]} has no default-holder evidence")
    check("15 possible permissions" in perm_block, "9-permissions", "permission section does not state the 15-permission count")
    check("ALS-013" in perm_block or "ALS-013" in research, "9-permissions", "permission inventory does not cite ALS-013")

    risk_block = section(research, "### 7.3", "### 7.4")
    risk_rows = [cells(l) for l in risk_block.splitlines() if re.match(r"\| \d{1,2} \|", l)]
    risk_rows = [r for r in risk_rows if len(r) == 10]
    check(len(risk_rows) == 15, "9-permissions", f"risk table has {len(risk_rows)} rows, expected 15")
    for row in risk_rows:
        check(all(row[i] for i in range(1, 10)), "9-permissions", f"risk row for {row[1]} has an empty governance field")
    self_promo = next((r for r in risk_rows if r[1] == "Promote Self to Leader"), None)
    check(self_promo is not None and ("capture" in self_promo[2].lower() or "takeover" in self_promo[2].lower()), "9-permissions", "Promote Self to Leader risk is not described")
    check(self_promo is not None and ("do not ship" in self_promo[9].lower() or "never copy" in self_promo[7].lower()), "9-permissions", "Promote Self to Leader is not excluded from the Nation Supremacy model")

    comp_block = section(research, "### 7.6", "### 7.7")
    comp_rows = [cells(l) for l in comp_block.splitlines() if l.startswith("| ") and not l.startswith("|---") and "Politics & War permission" not in l]
    comp_rows = [r for r in comp_rows if len(r) == 5]
    check(len(comp_rows) == 15, "9-permissions", f"comparison table has {len(comp_rows)} rows, expected 15")
    for row in comp_rows:
        check(all(row[i] for i in range(0, 5)), "9-permissions", f"comparison row {row[0]} has an empty field")

    # --- 10. Sources ---------------------------------------------------------
    source_block = section(sources, "## 1. Source register", "## 2. Finding register")
    source_rows = table_rows(source_block, "| ALS-", 9)
    check(len(source_rows) == 27, "10-sources", f"source register has {len(source_rows)} rows, expected 27")
    by_id = {r[0]: r for r in source_rows}
    for sid in ("ALS-016", "ALS-017", "ALS-027"):
        row = by_id.get(sid)
        check(row is not None, "10-sources", f"missing forum source {sid}")
        if row:
            check("/topic/" in row[3], "10-sources", f"{sid} does not use an exact thread permalink")
            check("forum.politicsandwar.com/ (" not in row[3], "10-sources", f"{sid} still points at the forum root")
            check(row[4] == "ANECDOTAL", "10-sources", f"{sid} is not classified ANECDOTAL")
    check(by_id.get("ALS-013", ["", "", "", "", ""])[4] == "COMMUNITY DOCUMENTATION", "10-sources", "ALS-013 is not COMMUNITY DOCUMENTATION")
    check("2026-10-31" in by_id.get("ALS-013", ["", "", "", "", "", ""])[5], "10-sources", "ALS-013 has no 2026-10-31 access date")
    check("Not retrieved" in by_id.get("ALS-015", ["", "", "", "", "", ""])[5], "10-sources", "ALS-015 is not marked as not retrieved")
    check("has not started" not in by_id.get("ALS-011", ["", "", "", "", ""])[8].lower(), "10-sources", "ALS-011 reliability still calls the page a shell")
    check("placeholder" in by_id.get("ALS-011", ["", "", "", "", ""])[8].lower(), "10-sources", "ALS-011 limitation does not record the unpublished requirements panel")

    for sid, row in by_id.items():
        check(row[3].startswith("http") or row[3].startswith("`") or row[3].startswith("Prompt"), "10-sources", f"{sid} has no usable direct reference")
        check(row[5] != "", "10-sources", f"{sid} has no access/date field")

    # --- 11. Change control --------------------------------------------------
    check("## 6. Correction record" in matrix, "11-change", "matrix lacks the correction record")
    check("## 7. Change log" in matrix, "11-change", "matrix lacks a change log")
    check("## 5. Source-register corrections made by 09A-C" in sources, "11-change", "source register lacks its correction record")
    check("## 23. Prompt 09A-C correction record" in research, "11-change", "research lacks its 09A-C correction record")
    check("## 24. Prompt 09A-D correction record" in research, "11-change", "research lacks its 09A-D correction record")
    check("## 25. Prompt 09A-E correction record" in research, "11-change", "research lacks its 09A-E correction record")
    check("| AX-08 (09A-E) |" in matrix, "11-change", "matrix lacks AX-08 (09A-E) correction record")
    check("## 26. Prompt 09A-F correction record" in research, "11-change", "research lacks its 09A-F correction record")
    check("| AX-08 (09A-F) |" in matrix, "11-change", "matrix lacks AX-08 (09A-F) correction record")
    check("| 2026-10-31 | 1.4 |" in matrix and "Prompt 09A-F" in matrix, "11-change", "matrix lacks Prompt 09A-F entry in Section 7 change log")
    check("09A_alliance_reference_review.md" in research, "11-change", "research does not link the semantic review record")
    check("single-author" in review.lower() and "not an independent review" in review.lower(), "11-change", "review record does not disclose that it is not independent")
    check("does not prove" in review.lower() or "does not independently prove" in review.lower(), "11-change", "review record does not state the limit of automated validation")

    # --- 12. Treasury storage / AX-08 traceability --------------------------
    ax08_summary = [r for r in summary if r[0] == "AX-08"]
    check(len(ax08_summary) == 1, "12-treasury-storage", f"AX-08 summary row count is {len(ax08_summary)}, expected 1")
    if ax08_summary:
        s_row = ax08_summary[0]
        check(all(bool(c) for c in s_row), "12-treasury-storage", "AX-08 summary row has empty fields")
        check("REQ-176 **DIRECT**" in s_row[5], "12-treasury-storage", "AX-08 summary does not show REQ-176 as DIRECT")
        check("REQ-141 **RELATED**" in s_row[5], "12-treasury-storage", "AX-08 summary does not show REQ-141 as RELATED")
        check("REQ-142 **RELATED**" in s_row[5], "12-treasury-storage", "AX-08 summary does not show REQ-142 as RELATED")
        check("no existing" in s_row[5].lower(), "12-treasury-storage", "AX-08 summary does not record no existing capacity requirement")
        check("UD-046" in s_row[8], "12-treasury-storage", "AX-08 summary does not reference UD-046")
        check("hold pooled resources within economy capacity" not in s_row[2].lower(), "12-treasury-storage", "AX-08 summary implies national warehouse capacity governs alliance-pool capacity")
        check("national warehouse capacity does not establish" in s_row[2].lower(), "12-treasury-storage", "AX-08 summary does not state that national warehouse capacity does not establish alliance-pool capacity")

    ax08_audit = [r for r in audit if r[0] == "AX-08"]
    check(len(ax08_audit) == 4, "12-treasury-storage", f"AX-08 audit row count is {len(ax08_audit)}, expected 4")

    ax08_by_req = {r[1]: r for r in ax08_audit}

    # REQ-141 in AX-08: must be RELATED CONSTRAINT
    check("REQ-141" in ax08_by_req, "12-treasury-storage", "AX-08 audit lacks REQ-141 row")
    if "REQ-141" in ax08_by_req:
        r141 = ax08_by_req["REQ-141"]
        check(norm_class(r141[3]) == "RELATED CONSTRAINT", "12-treasury-storage", f"AX-08 REQ-141 classification is {r141[3]}, expected RELATED CONSTRAINT")
        check("national warehouse" in r141[4].lower() and "not establish" in r141[4].lower(), "12-treasury-storage", "AX-08 REQ-141 evidence does not explain that national warehouse does not establish alliance treasury capacity")

    # REQ-142 in AX-08: must be RELATED CONSTRAINT
    check("REQ-142" in ax08_by_req, "12-treasury-storage", "AX-08 audit lacks REQ-142 row")
    if "REQ-142" in ax08_by_req:
        r142 = ax08_by_req["REQ-142"]
        check(norm_class(r142[3]) == "RELATED CONSTRAINT", "12-treasury-storage", f"AX-08 REQ-142 classification is {r142[3]}, expected RELATED CONSTRAINT")
        check("national" in r142[4].lower() and ("not establish" in r142[4].lower() or "does not define" in r142[4].lower()), "12-treasury-storage", "AX-08 REQ-142 evidence does not explain that national overflow does not establish alliance deposit behaviour")

    # REQ-176 in AX-08: must be DIRECT DEPENDENCY
    check("REQ-176" in ax08_by_req, "12-treasury-storage", "AX-08 audit lacks REQ-176 row")
    if "REQ-176" in ax08_by_req:
        r176 = ax08_by_req["REQ-176"]
        check(norm_class(r176[3]) == "DIRECT DEPENDENCY", "12-treasury-storage", f"AX-08 REQ-176 classification is {r176[3]}, expected DIRECT DEPENDENCY")
        check("separate" in r176[4].lower() and ("pool" in r176[4].lower() or "audited" in r176[4].lower() or "integrity" in r176[4].lower()), "12-treasury-storage", "AX-08 REQ-176 evidence does not cite separate audited pools or integrity")
        check("numerical capacity limit" not in r176[4].lower() or "not define" in r176[4].lower(), "12-treasury-storage", "AX-08 REQ-176 claims to establish a numerical capacity limit")

    # Missing requirement row for AX-08
    check("—" in ax08_by_req, "12-treasury-storage", "AX-08 lacks explicit NO EXISTING REQUIREMENT row for pool capacity")
    if "—" in ax08_by_req:
        r_none = ax08_by_req["—"]
        check(norm_class(r_none[3]) == "NO EXISTING REQUIREMENT", "12-treasury-storage", "AX-08 missing requirement row is not classified NO EXISTING REQUIREMENT")
        check("UD-046" in r_none[6], "12-treasury-storage", f"AX-08 missing requirement row does not cite UD-046: {r_none[6]!r}")
        check("capacity" in r_none[4].lower() and "unresolved" in r_none[4].lower(), "12-treasury-storage", "AX-08 missing requirement evidence does not explain that pool capacity is unresolved")

    # UD-046 checks
    check("UD-046" in ud_ids, "12-treasury-storage", "missing UD-046 in ud_ids")
    ud046_reg_row = next((l for l in ud.splitlines() if l.startswith("| UD-046 |")), "")
    check(bool(ud046_reg_row), "12-treasury-storage", "UD-046 register row not found")
    if ud046_reg_row:
        ud046_cells = cells(ud046_reg_row)
        check(len(ud046_cells) >= 9, "12-treasury-storage", "UD-046 register row has unexpected column count")
        check(ud046_cells[8].startswith("Open"), "12-treasury-storage", f"UD-046 register row is not Open: {ud046_cells[8]!r}")
        check("resolved" not in ud046_cells[8].lower(), "12-treasury-storage", "UD-046 register row is marked resolved")

    ud046_summary_row = next((l for l in ud.splitlines() if l.startswith("| `UD-046` |")), "")
    check(bool(ud046_summary_row), "12-treasury-storage", "UD-046 summary row not found")
    if ud046_summary_row:
        ud046_s_cells = cells(ud046_summary_row)
        check(len(ud046_s_cells) >= 5, "12-treasury-storage", "UD-046 summary row has unexpected column count")
        check(ud046_s_cells[1] == "Open", "12-treasury-storage", f"UD-046 summary row status is {ud046_s_cells[1]!r}, expected 'Open'")
        check("resolved" not in ud046_s_cells[1].lower(), "12-treasury-storage", "UD-046 summary row is marked resolved")

    # Banned mappings: national warehouse capacity substituted for alliance pool, or deposit described as purchase
    banned_ax08 = [
        (r"national\s+warehouse\s+capacity\s+(automatically\s+)?(establishes|sets|governs|defines)\s+alliance\s+treasury", "national warehouse capacity substituted for alliance treasury capacity"),
        (r"alliance\s+deposit\s+(?:is\s+)?(?:treated\s+as\s+|acts\s+as\s+|is\s+)?(?:a\s+)?national\s+(?:purchase|production)", "alliance deposit described as national purchase or production"),
    ]
    for pattern, desc in banned_ax08:
        check(not re.search(pattern, matrix, flags=re.IGNORECASE), "12-treasury-storage", f"matrix contains prohibited statement: {desc}")

    # Total counts check
    check(len(audit) == 77, "12-treasury-storage", f"matrix has {len(audit)} audit rows, expected 77")
    check(class_counts["DIRECT DEPENDENCY"] == 39, "12-treasury-storage", f"matrix has {class_counts['DIRECT DEPENDENCY']} DIRECT DEPENDENCY, expected 39")
    check(class_counts["RELATED CONSTRAINT"] == 19, "12-treasury-storage", f"matrix has {class_counts['RELATED CONSTRAINT']} RELATED CONSTRAINT, expected 19")
    check(class_counts["SUPPORTING CONTEXT"] == 6, "12-treasury-storage", f"matrix has {class_counts['SUPPORTING CONTEXT']} SUPPORTING CONTEXT, expected 6")
    check(class_counts["NO EXISTING REQUIREMENT"] == 13, "12-treasury-storage", f"matrix has {class_counts['NO EXISTING REQUIREMENT']} NO EXISTING REQUIREMENT, expected 13")

    # Review record cross-check for AX-08
    review_ax08 = next((l for l in review.splitlines() if l.startswith("| AX-08 |")), "")
    check("REQ-176 DIRECT" in review_ax08 and "REQ-141/142 RELATED" in review_ax08, "12-treasury-storage", "review record does not reflect AX-08 classifications (REQ-176 DIRECT; REQ-141/142 RELATED)")

    # AX-08 Fields 12–20 checks
    ax08_fields = [r for r in fields if r[0] == "AX-08"]
    check(len(ax08_fields) == 1, "12-treasury-storage", f"AX-08 fields row count is {len(ax08_fields)}, expected 1")
    if ax08_fields:
        f_row = ax08_fields[0]
        check("reject over-capacity deposit cleanly" not in f_row[5].lower(), "12-treasury-storage", "AX-08 failure/recovery claims unapproved 'Reject over-capacity deposit cleanly'")
        check("unresolved" in f_row[5].lower() and "ud-046" in f_row[5].lower(), "12-treasury-storage", "AX-08 failure/recovery does not state over-capacity behaviour is unresolved under UD-046")
        check(f_row[4].strip().lower() != "capacity only", "12-treasury-storage", "AX-08 resource impact is unclarified 'Capacity only'")
        check("unestablished" in f_row[4].lower() and "ud-046" in f_row[4].lower(), "12-treasury-storage", "AX-08 resource impact does not state capacity is unestablished under UD-046")

    # Stale current-status and validator count checks
    check("accepted after 09a-c" not in handoff.lower(), "12-treasury-storage", "handoff contains stale 'accepted after 09A-C' current-status text")
    check("accepted (09a/09a-c)" not in handoff.lower(), "12-treasury-storage", "handoff contains stale 'Accepted (09A/09A-C)' current-status text")
    check("accepted after 09a-c" not in outline.lower(), "12-treasury-storage", "outline contains stale 'accepted after 09A-C' current-status text")
    check("following the 09a-c correction" not in outline.lower(), "12-treasury-storage", "outline contains stale 'following the 09A-C correction' current-status text")
    check("829 checks" not in handoff, "12-treasury-storage", "handoff cites stale 829 validator check count")

    # Requirements register: no unapproved capacity requirement marked Approved.
    # A requirement may mention capacity only to deny one while UD-046 is Open;
    # flag positive capacity assertions, not explicit denials.
    capacity_denial = re.compile(
        r"\b(?:no|not|never|none|without|unestablished|unresolved)\b"
        r"|\b(?:remains?|stays?)\s+open\b|\bassumes?\s+no\b",
        re.I,
    )
    positive_capacity = re.compile(
        r"\b(?:alliance|pool|treasury)\b[^.;]{0,40}\b(?:capacity|storage limit|pool size)\b"
        r"[^.;]{0,40}\b(?:is|are|equals|fixed at|limited to|capped at|set to)\b"
        r"|\b(?:capacity|storage limit|pool size)\b[^.;]{0,30}\b(?:of|at)\s+\d",
        re.I,
    )
    for line in req.splitlines():
        if line.startswith("| REQ-"):
            r_cells = cells(line)
            if len(r_cells) >= 4:
                r_title = r_cells[1].lower()
                r_status = r_cells[3].strip()
                if ("alliance" in r_title
                        and ("capacity" in r_title or "storage limit" in r_title or "pool size" in r_title)
                        and r_status == "Approved"
                        and positive_capacity.search(r_title)
                        and not capacity_denial.search(r_title)):
                    check(False, "12-treasury-storage", f"unapproved alliance capacity requirement marked Approved: {r_cells[0]}")

# --- 13. Current-status consistency checks -----------------------------
    # 1. AI_CONTEXT.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status
    check("09a accepted after 09a-f" in context.lower() or "accepted after the final 09a-f closure pass" in context.lower() or "accepted after prompt 09a-f" in context.lower(), "13-current-status", "AI_CONTEXT.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in context.lower(), "13-current-status", "AI_CONTEXT.md does not carry the current 09B/09C status")

    # 2. AI_HANDOFF.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status
    check("09a accepted after 09a-f" in ai_handoff.lower() or "accepted after the final 09a-f closure pass" in ai_handoff.lower() or "accepted after prompt 09a-f" in ai_handoff.lower(), "13-current-status", "AI_HANDOFF.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in ai_handoff.lower(), "13-current-status", "AI_HANDOFF.md does not carry the current 09B/09C status")

    # 3. 01_stage_2_prompt_roadmap.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status, and references §36
    check("09a accepted after 09a-f" in roadmap.lower() or "accepted after the final 09a-f closure pass" in roadmap.lower(), "13-current-status", "01_stage_2_prompt_roadmap.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in roadmap.lower(), "13-current-status", "01_stage_2_prompt_roadmap.md does not carry the current 09B/09C status")
    check("§36" in roadmap or "§32–§36" in roadmap or "§32-§36" in roadmap, "13-current-status", "01_stage_2_prompt_roadmap.md does not reference progress log section §36")
    check("§32](06_stage_2_progress_log.md)–[§35]" not in roadmap and "§32](06_stage_2_progress_log.md)–[§34]" not in roadmap, "13-current-status", "01_stage_2_prompt_roadmap.md contains stale progress log range")

    # 4. 06_stage_2_progress_log.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status in summary/table, and contains Section 36
    log_header = "\n".join(log.splitlines()[:15])
    check("accepted after prompt 09a-f" in log_header.lower() or "accepted after 09a-f" in log_header.lower(), "13-current-status", "06_stage_2_progress_log.md summary does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in log_header.lower(), "13-current-status", "06_stage_2_progress_log.md summary does not carry the current 09B/09C status")
    log_row09 = next((l for l in log.splitlines() if l.startswith("| 09 |")), "")
    check("09a accepted after 09a-f" in log_row09.lower(), "13-current-status", "06_stage_2_progress_log.md row 09 does not report Prompt 09A accepted after Prompt 09A-F")
    check("§36" in log_row09 or "§32–§36" in log_row09, "13-current-status", "06_stage_2_progress_log.md row 09 does not reference §36")
    check("## 36. Prompt 09A-F" in log, "13-current-status", "06_stage_2_progress_log.md lacks Section 36")

    # 5. 00_stage_2_handoff.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status
    check("accepted after the final 09a-f closure pass" in handoff.lower() or "accepted (09a/09a-f)" in handoff.lower(), "13-current-status", "00_stage_2_handoff.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in handoff.lower(), "13-current-status", "00_stage_2_handoff.md does not carry the current 09B/09C status")

    # 6. 02_master_game_design_bible_outline.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status
    check("accepted after prompt 09a-f" in outline.lower() or "accepted after 09a-f" in outline.lower(), "13-current-status", "02_master_game_design_bible_outline.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in outline.lower(), "13-current-status", "02_master_game_design_bible_outline.md does not carry the current 09B/09C status")

    # 7. ROADMAP.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status, and references §36
    check("09a accepted after the final 09a-f closure pass" in root_roadmap.lower() or "09a accepted after 09a-f" in root_roadmap.lower(), "13-current-status", "ROADMAP.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in root_roadmap.lower(), "13-current-status", "ROADMAP.md does not carry the current 09B/09C status")
    check("§36" in root_roadmap or "§32–§36" in root_roadmap, "13-current-status", "ROADMAP.md does not reference progress log section §36")
    check("§32](stage-2/06_stage_2_progress_log.md)–[§35]" not in root_roadmap and "§32](stage-2/06_stage_2_progress_log.md)–[§34]" not in root_roadmap, "13-current-status", "ROADMAP.md contains stale progress log range")

    # 8. PROJECT_PROGRESS.md reports Prompt 09A accepted after Prompt 09A-F and the current 09B/09C status
    check("09a accepted after 09a-f" in progress.lower() or "accepted after the final 09a-f closure pass" in progress.lower(), "13-current-status", "PROJECT_PROGRESS.md does not report Prompt 09A accepted after Prompt 09A-F")
    check(CURRENT_STATUS in progress.lower(), "13-current-status", "PROJECT_PROGRESS.md does not carry the current 09B/09C status")

    # 9. All continuity documents agree on the current 09B/09C status
    continuity_docs = [
        ("AI_CONTEXT.md", context),
        ("AI_HANDOFF.md", ai_handoff),
        ("01_stage_2_prompt_roadmap.md", roadmap),
        ("06_stage_2_progress_log.md", log_header),
        ("00_stage_2_handoff.md", handoff),
        ("02_master_game_design_bible_outline.md", outline),
        ("ROADMAP.md", root_roadmap),
        ("PROJECT_PROGRESS.md", progress),
    ]
    for dname, dtext in continuity_docs:
        check(CURRENT_STATUS in dtext.lower(), "13-current-status", f"{dname} does not carry the current 09B/09C status")
        check("prompt 10" in dtext.lower(), "13-current-status", f"{dname} does not name Prompt 10 as the next step")
        check("prompt 09c" in dtext.lower(), "13-current-status", f"{dname} does not record Prompt 09C as complete at the specification/documentation level")
        check(
            not re.search(
                r"prompt\s+09(?:b|d)\b[^.\n]{0,40}(?:is|remains)\s+(?:the\s+)?next",
                dtext,
                re.I,
            ),
            "13-current-status",
            f"{dname} claims a different prompt is next",
        )

    # 10. Absence of stale current-status statements claiming Prompt 09A accepted after 09A-D, 09A-E, or 09A-C
    check("accepted after 09a-d" not in context.lower(), "13-current-status", "AI_CONTEXT.md contains stale 'accepted after 09A-D'")
    check("accepted after 09a-e" not in context.lower(), "13-current-status", "AI_CONTEXT.md contains stale 'accepted after 09A-E'")
    check("accepted after 09a-c" not in context.lower(), "13-current-status", "AI_CONTEXT.md contains stale 'accepted after 09A-C'")

    status_block_ah = section(ai_handoff, "<!-- STATUS:BEGIN -->", "<!-- STATUS:END -->")
    check("accepted after 09a-d" not in status_block_ah.lower(), "13-current-status", "AI_HANDOFF.md STATUS block contains stale 'accepted after 09A-D'")
    check("accepted after 09a-e" not in status_block_ah.lower(), "13-current-status", "AI_HANDOFF.md STATUS block contains stale 'accepted after 09A-E'")
    check("accepted after 09a-c" not in status_block_ah.lower(), "13-current-status", "AI_HANDOFF.md STATUS block contains stale 'accepted after 09A-C'")

    status_block_pp = section(progress, "<!-- STATUS:BEGIN -->", "<!-- STATUS:END -->")
    check("accepted after 09a-d" not in status_block_pp.lower(), "13-current-status", "PROJECT_PROGRESS.md STATUS block contains stale 'accepted after 09A-D'")
    check("accepted after 09a-e" not in status_block_pp.lower(), "13-current-status", "PROJECT_PROGRESS.md STATUS block contains stale 'accepted after 09A-E'")
    check("accepted after 09a-c" not in status_block_pp.lower(), "13-current-status", "PROJECT_PROGRESS.md STATUS block contains stale 'accepted after 09A-C'")

    handoff_header = "\n".join(handoff.splitlines()[:50])
    check("accepted after the 09a-d" not in handoff_header.lower() and "accepted after 09a-d" not in handoff_header.lower(), "13-current-status", "00_stage_2_handoff.md header contains stale 'accepted after 09A-D'")
    check("accepted after the 09a-e" not in handoff_header.lower() and "accepted after 09a-e" not in handoff_header.lower(), "13-current-status", "00_stage_2_handoff.md header contains stale 'accepted after 09A-E'")
    check("accepted after the 09a-c" not in handoff_header.lower() and "accepted after 09a-c" not in handoff_header.lower(), "13-current-status", "00_stage_2_handoff.md header contains stale 'accepted after 09A-C'")

    check("accepted after the 09a-d" not in outline.lower() and "accepted after 09a-d" not in outline.lower(), "13-current-status", "02_master_game_design_bible_outline.md contains stale 'accepted after 09A-D'")
    check("accepted after the 09a-e" not in outline.lower() and "accepted after 09a-e" not in outline.lower(), "13-current-status", "02_master_game_design_bible_outline.md contains stale 'accepted after 09A-E'")

    check("accepted after the 09a-d" not in root_roadmap.lower() and "accepted after 09a-d" not in root_roadmap.lower(), "13-current-status", "ROADMAP.md contains stale 'accepted after 09A-D'")
    check("accepted after the 09a-e" not in root_roadmap.lower() and "accepted after 09a-e" not in root_roadmap.lower(), "13-current-status", "ROADMAP.md contains stale 'accepted after 09A-E'")

    roadmap_header = "\n".join(roadmap.splitlines()[:30])
    check("accepted after the 09a-d" not in roadmap_header.lower() and "accepted after 09a-d" not in roadmap_header.lower(), "13-current-status", "01_stage_2_prompt_roadmap.md header contains stale 'accepted after 09A-D'")
    check("accepted after the 09a-e" not in roadmap_header.lower() and "accepted after 09a-e" not in roadmap_header.lower(), "13-current-status", "01_stage_2_prompt_roadmap.md header contains stale 'accepted after 09A-E'")

    check("accepted after 09a-d" not in log_header.lower(), "13-current-status", "06_stage_2_progress_log.md header contains stale 'accepted after 09A-D'")
    check("accepted after 09a-e" not in log_header.lower(), "13-current-status", "06_stage_2_progress_log.md header contains stale 'accepted after 09A-E'")
    check("accepted after 09a-c" not in log_header.lower(), "13-current-status", "06_stage_2_progress_log.md header contains stale 'accepted after 09A-C'")


    return problems, checks


def main(argv: list[str]) -> int:
    docs = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parents[1]
    problems, checks = validate(docs)
    print(f"09A Alliance validator — {docs}")
    print(f"Checks run: {checks}")
    if problems:
        print(f"FAIL: {len(problems)} problem(s)")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("PASS: all Alliance integration, source, permission and handoff checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
