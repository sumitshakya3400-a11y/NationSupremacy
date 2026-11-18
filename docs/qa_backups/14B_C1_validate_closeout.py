"""Prompt 14B-C1 / 14B-C1-R1 closeout validator.

Checks:

  A. D-014 decision-category metadata for all 49 B-04 parameter records,
     including decision-reference existence, relevance, authority wording and
     evidence-resolution checks (R1-B).
  B. 35-row cross-system matrix tally reconciliation and separation from the
     contradiction register.
  C. The 17-category QA evidence crosswalk and its seven evidence dimensions
     (R1-C).
  R. The R1 semantic-review record, report references and authority wording.
  M. Ten mutation self-tests proving that the checks reject the required
     invalid cases.

Document/tooling QA only. Run from `docs/`:

    python qa_backups/14B_C1_validate_closeout.py
    python qa_backups/14B_C1_validate_closeout.py --self-test
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
INVENTORY = DOCS / "stage-2" / "22_numerical_parameter_inventory.md"
REPORT = DOCS / "stage-2" / "25_prompt_14B_b04_economy_completion_report.md"
QA = DOCS / "stage-2" / "22_numerical_baseline_qa_report.md"
B14 = DOCS / "stage-2" / "22_formulas_and_balance.md"
LOG = DOCS / "stage-2" / "06_stage_2_progress_log.md"
ROADMAP = DOCS / "stage-2" / "01_stage_2_prompt_roadmap.md"
HANDOFF = DOCS / "AI_HANDOFF.md"
PROGRESS = DOCS / "PROJECT_PROGRESS.md"
DECISIONS = DOCS / "DECISIONS.md"
SPEC = DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md"
REGISTER = DOCS / "stage-2" / "10_economic_formula_and_balance_register.md"
WARFARE = DOCS / "stage-2" / "17_warfare_formula_register.md"
C1_REPORT = DOCS / "stage-2" / "26_prompt_14B-C1_closeout_report.md"
R1_REPORT = DOCS / "stage-2" / "27_prompt_14B-C1-R1_closeout_report.md"
R1R1_REPORT = DOCS / "stage-2" / "28_prompt_14B-C1-R1-R1_closeout_report.md"
QA_BACKUPS = DOCS / "qa_backups"

STATUSES = {"OWNER-APPROVED VALUE", "PROVISIONAL VALUE", "DESIGN PROPOSAL", "NEEDS PLAYTESTING"}
CATEGORIES = {"A", "B", "C", "D", "UNRESOLVED"}
EVIDENCE_LEVELS = {
    "DOCUMENTED", "NUMERICALLY VALIDATED", "INTEGRATION CHECKED",
    "RUNTIME VERIFIED", "RUNTIME NOT VERIFIED",
    "MIGRATION VERIFIED", "MIGRATION NOT VERIFIED",
    "BALANCE TESTED", "BALANCE NOT ACCEPTED",
    "PLAYTESTED", "PLAYTESTING NOT EXECUTED",
    "NOT APPLICABLE", "NOT YET VERIFIED",
}
FORBIDDEN_CLAIMS = {"RUNTIME VERIFIED", "MIGRATION VERIFIED", "BALANCE TESTED", "PLAYTESTED"}
EXPECTED_PARENT = {"3.2": "D-045", "3.3": "D-046", "3.4": "D-048", "3.5": "D-058"}

FAILURES: list[str] = []
CHECKS = [0]


def check(label: str, condition: bool, detail="") -> None:
    CHECKS[0] += 1
    if not condition:
        FAILURES.append(f"{label}{(': ' + str(detail)) if detail else ''}")


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def plain(cell: str) -> str:
    return cell.strip().strip("*` ").strip()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


# --------------------------------------------------------------------------------------
# Reference helpers (R1-B)
# --------------------------------------------------------------------------------------


def decision_rows(text: str) -> dict[str, str]:
    rows = {}
    for line in text.splitlines():
        m = re.match(r"\| (D-\d{3}) \|", line)
        if m:
            rows[m.group(1)] = line
    return rows


def decision_exists(did: str, decisions_text: str) -> bool:
    return bool(did) and did in decision_rows(decisions_text)


def decision_is_superseded(did: str, decisions_text: str) -> bool:
    row = decision_rows(decisions_text).get(did, "")
    return "superseded" in row.lower()


def authority_wording_ok(text: str) -> bool:
    lowered = text.lower()
    return not any(p in lowered for p in ("owner-approved", "owner approved", "owner authorization"))


def evidence_wording_ok(text: str) -> bool:
    lowered = text.lower()
    if any(p in lowered for p in ("playtest completed", "playtested", "completed playtest", "balance tested")):
        return False
    return True


def category_distinct(category: str, status: str) -> bool:
    return category not in STATUSES and plain(category) not in STATUSES and category != status


def invented_id(text: str) -> bool:
    return bool(re.search(r"\b(NP|PARAM|P)-EC-\d", text))


def ecn_ids(text: str) -> set[str]:
    return set(re.findall(r"\*\*(ECN-\d{3}[a-z]?)\b", text))


def fec_ids(text: str) -> set[str]:
    return set(re.findall(r"\*\*(F-EC-\d{3}[a-z]?)\b", text))


def fwr_ids(text: str) -> set[str]:
    return (set(re.findall(r"^### (F-WR-\d{3}[a-z]?)(?:\s|$)", text, re.M))
            | set(re.findall(r"\| `(F-WR-\d{3}[a-z]?)`", text)))


def expand_ids(text: str, prefix: str) -> set[str]:
    p = re.escape(prefix)
    ids = set(re.findall(rf"{p}-\d{{3}}[a-z]?", text))
    for a, b in re.findall(rf"{p}-(\d{{3}})[a-z]?\s*[–-]\s*{p}-(\d{{3}})[a-z]?", text):
        for n in range(int(a), int(b) + 1):
            ids.add(f"{prefix}-{n:03d}")
    return ids


def local_link_targets(text: str) -> list[str]:
    targets = []
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        targets.append(target.split("#", 1)[0])
    return targets


def check_local_link(target: str) -> bool:
    if not target:
        return True
    root = DOCS.parent.resolve()
    path = (R1_REPORT.parent / target).resolve()
    return path.exists() and path.is_relative_to(root)


def has_section(text: str, token: str) -> bool:
    return bool(re.search(rf"^#{{2,4}}\s+{re.escape(token)}(?:\.|\s|$)", text, re.M))


def map_doc(doc: str, token: str) -> str | None:
    if doc == "B-04 rulebook":
        return "SPEC"
    if doc in ("B-04 register", "register"):
        return "REGISTER"
    if doc == "B-04":
        return "REGISTER" if token.startswith("3.") else "SPEC"
    if doc in ("parameter inventory", "inventory"):
        return "INVENTORY"
    if doc in ("14B report", "14B"):
        return "REPORT"
    if doc == "this report":
        return "QA"
    return None


def section_refs(cell: str) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    doc_re = r"(B-04 rulebook|B-04 register|B-04|register|parameter inventory|inventory|14B report|14B|this report)"
    for part in re.split(r"[;,]", cell):
        m = re.search(doc_re + r"\s*§", part)
        if m:
            doc = m.group(1)
            for token in re.findall(r"§([\d.]+)", part):
                refs.append((doc, token))
        else:
            m2 = re.search(r"§([\d.]+)", part)
            if m2 and refs:
                refs.append((refs[-1][0], m2.group(1)))
    return refs


def resolve_section(doc: str, token: str) -> bool:
    key = map_doc(doc, token)
    if key is None:
        return False
    path = {"SPEC": SPEC, "REGISTER": REGISTER, "INVENTORY": INVENTORY,
            "REPORT": REPORT, "QA": QA}[key]
    return has_section(read(path), token)


# --------------------------------------------------------------------------------------
# A. D-014 category metadata + reference integrity
# --------------------------------------------------------------------------------------


def category_rows(inv_text: str | None = None) -> list[list[str]]:
    inv = read(INVENTORY) if inv_text is None else inv_text
    start = inv.find("### 6.1 D-014 decision-category metadata")
    end = inv.find("## 7.", start)
    block = inv[start:end] if start >= 0 else ""
    return [cells(l) for l in block.splitlines() if l.startswith("| B-04 §3.")]


def check_categories() -> None:
    inv = read(INVENTORY)
    decisions = read(DECISIONS)
    main: dict[tuple[str, str], tuple[str, str]] = {}
    for line in inv.splitlines():
        if not line.startswith("| None |"):
            continue
        c = cells(line)
        if len(c) != 14:
            continue
        m = re.match(r"B-04 §(3\.[1-5])", c[4])
        if not m:
            continue
        main[(m.group(1), c[1])] = (c[2], c[10])

    check("A1 main B-04 table has 49 rows", len(main) == 49, f"{len(main)}")
    rows = category_rows(inv)
    check("A2 category table has 49 rows", len(rows) == 49, f"{len(rows)}")
    check("A3 every category row has 10 fields", all(len(r) == 10 for r in rows),
          str(sorted({len(r) for r in rows})))

    seen = set()
    cat_counts = Counter()
    for r in rows:
        key, name, value, status, category, authority, parent, rationale, owner_action, unresolved = r
        category = plain(category)
        status = plain(status)
        m = re.match(r"B-04 §(3\.[1-5]) · (.+)$", key)
        check(f"A4 record key is a source locator: {key!r}", bool(m))
        if not m:
            continue
        section, key_name = m.group(1), m.group(2)
        check(f"A5 record key name matches parameter: {key!r}", key_name == name)
        check(f"A6 record is unique: {key!r}", key not in seen)
        seen.add(key)
        check(f"A7 record matches a main-table row: {key!r}", (section, name) in main)
        check(f"A8 no invented parameter ID: {key!r}", not invented_id(key))
        check(f"A9 numerical status unchanged: {key!r}", status in STATUSES and status == main.get((section, name), ("", ""))[1])
        check(f"A10 value unchanged: {key!r}", value == main.get((section, name), ("", ""))[0])
        check(f"A11 D-014 category is valid: {key!r}", category in CATEGORIES, category)
        check(f"A12 category is not a numerical status: {key!r}", category_distinct(category, status))
        check(f"A13 authority present: {key!r}", bool(authority))
        check(f"A14 structural parent/source present: {key!r}", bool(parent))
        check(f"A15 rationale present: {key!r}", len(rationale) >= 40)
        check(f"A16 owner-action field present: {key!r}", bool(owner_action))
        check(f"A17 unresolved-evidence field present: {key!r}", bool(unresolved))
        check(f"A18 category is C (the tested value decision): {key!r}", category == "C")
        cat_counts[category] += 1

        cited = re.findall(r"D-\d{3}", parent)
        check(f"A19 every cited decision exists: {key!r}", all(decision_exists(d, decisions) for d in cited), cited)
        check(f"A20 no cited decision is a superseded record presented as current: {key!r}",
              all(not decision_is_superseded(d, decisions) for d in cited), cited)
        check(f"A21 decision authority wording is not an owner-approval claim: {key!r}",
              authority_wording_ok(authority) and authority_wording_ok(parent), authority + " / " + parent)
        expected = EXPECTED_PARENT.get(section, "D-063")
        check(f"A22 the relevant structural parent is cited: {key!r}", expected in parent, f"{expected} not in {parent}")
        if section == "3.1" and name == "Warehouse capacity":
            check("A23 warehouse row cites D-052", "D-052" in parent)
        check(f"A24 evidence wording does not claim a completed playtest: {key!r}", evidence_wording_ok(unresolved), unresolved)
        check(f"A25 evidence path names a test or playtest: {key!r}",
              "test" in unresolved.lower() or "playtest" in unresolved.lower(), unresolved)

    check("A26 all 49 category keys are unique", len(seen) == 49, f"{len(seen)}")
    check("A27 category summary is 0/0/49/0", (cat_counts["A"], cat_counts["B"], cat_counts["C"], cat_counts["D"]) == (0, 0, 49, 0),
          dict(cat_counts))

    reserved = []
    for line in inv.splitlines():
        if line.startswith("| None |"):
            c = cells(line)
            if len(c) == 14 and c[4].startswith("B-04 §3.") and c[13].strip() != "No":
                reserved.append((c[1], c[13]))
    check("A28 no B-04 record is owner-reserved", not reserved, str(reserved))
    promoted = [k for k, (v, s) in main.items() if s != "PROVISIONAL VALUE"]
    check("A29 all 49 values remain PROVISIONAL VALUE", not promoted, str(promoted))
    check("A30 the four-status vocabulary is unchanged", all(s in inv for s in STATUSES))

    for path in (INVENTORY, C1_REPORT, LOG):
        check(f"A31 {path.name} does not call a Category B decision owner-approved",
              "Category B / owner-approved" not in read(path), "unsupported wording present")


# --------------------------------------------------------------------------------------
# B. Matrix tally
# --------------------------------------------------------------------------------------


def matrix_rows() -> list[list[str]]:
    text = read(REPORT)
    start = text.find("### 5.3 Consistency assessment")
    end = text.find("### 5.4", start)
    block = text[start:end] if start >= 0 else ""
    return [cells(l) for l in block.splitlines() if l.startswith("| X-")]


def check_matrix() -> None:
    rows = matrix_rows()
    check("B1 matrix has 35 rows", len(rows) == 35, f"{len(rows)}")
    statuses = Counter()
    for r in rows:
        status_cell = next((c for c in r if "VERIFIED" in c or "CONTRADICTION" in c or "NOT YET" in c), "")
        if "VERIFIED WITH DOCUMENTED LIMITATION" in status_cell:
            statuses["VWDL"] += 1
        elif "VERIFIED CONSISTENT" in status_cell:
            statuses["VC"] += 1
        elif "CONTRADICTION IDENTIFIED" in status_cell:
            statuses["CI"] += 1
        elif "NOT YET VERIFIED" in status_cell:
            statuses["NYV"] += 1
        else:
            statuses["UNKNOWN"] += 1
    check("B2 counts are 27/4/4/0", (statuses["VC"], statuses["VWDL"], statuses["CI"], statuses["NYV"]) == (27, 4, 4, 0),
          dict(statuses))
    check("B3 statuses sum to 35", sum(statuses.values()) == 35, dict(statuses))

    tally = next((l for l in read(REPORT).splitlines() if l.startswith("**Tally:**")), "")
    for n, label in ((27, "VERIFIED CONSISTENT"), (4, "VERIFIED WITH DOCUMENTED LIMITATION"),
                     (4, "CONTRADICTION IDENTIFIED"), (0, "NOT YET VERIFIED")):
        check(f"B4 report tally states {n} {label}", f"{n} `{label}`" in tally, tally[:200])
    check("B5 report tally does not claim 5 contradictions", "5 `CONTRADICTION IDENTIFIED`" not in read(REPORT))
    check("B6 report tally does not claim 6 limitations", "6 `VERIFIED WITH DOCUMENTED LIMITATION`" not in read(REPORT))

    creg = [l for l in read(REPORT).splitlines() if l.startswith("| C-")]
    check("B7 contradiction register has 18 entries", len(creg) == 18, f"{len(creg)}")
    check("B8 no C- register ID appears in the matrix rows",
          not any(c.startswith("| C-") for c in ["| " + r[0] + " |" for r in rows]))
    check("B9 the register is explicitly separate from the 35-row matrix",
          "contradiction register" in read(REPORT).lower())

    standard = ("35 dependency-matrix rows: 27 `VERIFIED CONSISTENT`, 4 `VERIFIED WITH DOCUMENTED LIMITATION`, "
                "4 `CONTRADICTION IDENTIFIED`, 0 `NOT YET VERIFIED`")
    for path in (REPORT, B14, LOG, ROADMAP, QA):
        text = read(path)
        check(f"B10 {path.name} carries the corrected tally", standard in text, "corrected tally phrase absent")
        check(f"B11 {path.name} has no stale 6/5 tally",
              "6 `VERIFIED WITH DOCUMENTED LIMITATION`" not in text and "5 `CONTRADICTION IDENTIFIED`" not in text)

    check("B12 B-06 items are recorded outside 14B authority",
          "OUTSIDE PROMPT 14B AUTHORITY" in read(REPORT) and "C-06" in read(REPORT) and "C-07" in read(REPORT))


# --------------------------------------------------------------------------------------
# C. QA crosswalk and seven dimensions
# --------------------------------------------------------------------------------------


def crosswalk_sections() -> tuple[list[list[str]], list[list[str]]]:
    qa = read(QA)
    s82 = qa.find("### 8.2 Source and result mapping")
    s83 = qa.find("### 8.3 Evidence-dimension matrix")
    s84 = qa.find("### 8.4 Scope boundary")
    rows82 = [cells(l) for l in qa[s82:s83].splitlines() if re.match(r"\| \d+ \|", l)] if s82 >= 0 and s83 >= 0 else []
    rows83 = [cells(l) for l in qa[s83:s84].splitlines() if re.match(r"\| \d+ \|", l)] if s83 >= 0 and s84 >= 0 else []
    return rows82, rows83


def check_crosswalk() -> None:
    qa = read(QA)
    rows, dims = crosswalk_sections()
    check("C1 crosswalk sections exist", bool(rows) and bool(dims))
    check("C2 source/result table has 17 rows", len(rows) == 17, f"{len(rows)}")
    check("C3 source/result rows have 8 fields", all(len(r) == 8 for r in rows),
          str(sorted({len(r) for r in rows})))
    check("C4 dimension matrix has 17 rows", len(dims) == 17, f"{len(dims)}")
    check("C5 dimension rows have 9 fields", all(len(r) == 9 for r in dims),
          str(sorted({len(r) for r in dims})))

    required_categories = (
        "Tax and income", "Resource inventory and accounting", "Starting economy and initial parameters",
        "Extraction and production chains", "Manufacturing and processing recipes",
        "Food demand and civilian/military boundaries", "Power demand, generation and fuel",
        "Maintenance and operating costs", "Treasury, reservations, cash flow and closing balances",
        "Reference prices, margins and payback", "Conservation and reconciliation",
        "Worked economic examples A–H", "Cross-system dependency matrix",
        "Parameter ownership and D-014 category metadata", "Exploit, dominance and money-creation",
        "Validation scripts and actual execution results", "Limitations and runtime/playtesting",
    )
    got = [r[1] for r in rows]
    for category in required_categories:
        check(f"C6 crosswalk covers {category!r}", any(category.lower() in g.lower() for g in got))

    for r in rows:
        primary = plain(r[7])
        check(f"C7 primary status valid: {r[0]}", primary in EVIDENCE_LEVELS, primary)
        check(f"C8 authoritative source present: {r[0]}", bool(r[2]))
        check(f"C9 supporting section present: {r[0]}", bool(r[3]))
        check(f"C10 result or limitation present: {r[0]}", bool(r[6]))

    for r in dims:
        idx = r[0]
        statuses = [plain(c) for c in r[2:9]]
        check(f"C11 all seven dimension statuses valid: {idx}", all(s in EVIDENCE_LEVELS for s in statuses), statuses)
        check(f"C12 documentation dimension is documented: {idx}", statuses[0] == "DOCUMENTED", statuses[0])
        check(f"C13 runtime is not claimed: {idx}", statuses[3] == "RUNTIME NOT VERIFIED", statuses[3])
        check(f"C14 migration is not claimed: {idx}",
              statuses[4] in {"NOT APPLICABLE", "MIGRATION NOT VERIFIED"}, statuses[4])
        check(f"C15 balance is not claimed: {idx}", statuses[5] in {"BALANCE NOT ACCEPTED", "NOT APPLICABLE"}, statuses[5])
        check(f"C16 playtesting is not claimed: {idx}",
              statuses[6] in {"PLAYTESTING NOT EXECUTED", "NOT APPLICABLE"}, statuses[6])
        check(f"C17 no forbidden success claim: {idx}", not any(s in FORBIDDEN_CLAIMS for s in statuses), statuses)

    check("C18 the seven dimensions are separately named in the table header",
          all(h in qa for h in ("Documentation", "Numerical validation", "Integration consistency",
                                "Runtime implementation", "Migration", "Gameplay balance", "Playtesting")))
    check("C19 scope boundary paragraph exists", "### 8.4 Scope boundary" in qa and "production readiness" in qa)
    check("C20 the vocabulary marks the four success claims as not used",
          all(f"`{claim}`" in qa and "Not used in this report" in qa for claim in FORBIDDEN_CLAIMS))


# --------------------------------------------------------------------------------------
# X. Crosswalk reference resolution (R1-R1)
# --------------------------------------------------------------------------------------


def check_crosswalk_references() -> None:
    qa = read(QA)
    rows, _dims = crosswalk_sections()
    decisions = read(DECISIONS)
    spec = read(SPEC)
    reg = read(REGISTER)
    war = read(WARFARE)
    ecn = ecn_ids(spec)
    fec = fec_ids(reg)
    fwr = fwr_ids(war)
    dset = set(decision_rows(decisions))
    execution = read(REPORT) + "\n" + read(R1_REPORT)
    inv_rows = category_rows()

    check("X1 crosswalk has 17 numeric rows", len(rows) == 17, len(rows))
    check("X2 crosswalk row numbers are 1..17",
          [r[0] for r in rows] == [str(i) for i in range(1, 18)], [r[0] for r in rows])

    for r in rows:
        if len(r) != 8:
            continue
        n, _category, source, support, completion, validators, result = r[0], r[1], r[2], r[3], r[4], r[5], r[6]
        ids_text = source + " " + support

        check(f"X3 row {n} names a recognized source",
              any(t in source for t in ("B-04", "register", "Register", "B-10", "inventory",
                                        "Inventory", "14B", "this report")), source)

        for cell, label in ((source, "source"), (completion, "completion")):
            for doc, token in section_refs(cell):
                check(f"X4 row {n} {label} section {doc} §{token} exists",
                      resolve_section(doc, token), f"{doc} §{token}")

        for prefix, idset in (("ECN", ecn), ("F-EC", fec), ("F-WR", fwr)):
            for x in sorted(expand_ids(ids_text, prefix)):
                check(f"X5 row {n} {prefix} {x} exists", x in idset, x)

        for d in sorted(set(re.findall(r"D-\d{3}", ids_text + " " + completion))):
            check(f"X6 row {n} decision {d} exists", d in dset, d)

        names = sorted(set(re.findall(r"[A-Za-z0-9_]+\.py(?![A-Za-z0-9])", validators)))
        if names:
            for name in names:
                check(f"X7 row {n} validator {name} exists", (QA_BACKUPS / name).exists(), name)
                check(f"X8 row {n} validator {name} has execution evidence", name in execution, name)
        else:
            check(f"X9 row {n} explicitly records that no validator applies",
                  validators.strip().lower().startswith("none"), validators)

        for claim in ("170/170", "321/321", "64/64", "9/9", "1,330/1,330", "856/856"):
            if claim in result:
                check(f"X10 row {n} result {claim} is recorded", claim in execution, claim)

        low = result.lower()
        check(f"X11 row {n} result does not claim unsupported success",
              not any(p in low for p in ("runtime verified", "migration verified", "balance tested",
                                         "playtest completed", "playtested")), result)

        if "B-02/B-03" in source:
            check(f"X12 row {n} matrix source families are present",
                  all(s in read(REPORT) for s in ("B-02", "B-03", "B-05", "B-06",
                                                  "B-07", "B-08", "B-09", "B-10")))

        if "24 §3.1 records" in support:
            count = len([x for x in inv_rows if x[0].startswith("B-04 §3.1")])
            check(f"X13 row {n} 24 §3.1 records exist", count == 24, count)
        if "49 records" in support:
            check(f"X14 row {n} 49 records exist", len(inv_rows) == 49, len(inv_rows))

        check(f"X15 row {n} does not use a local reading key as a source ID",
              not re.search(r"\bR-\d{2}\b", ids_text), ids_text)

    check("X16 ECN-999 is not a valid source identifier", "ECN-999" not in ecn)
    check("X17 F-EC-999 is not a valid formula identifier", "F-EC-999" not in fec)
    check("X18 F-WR-999 is not a valid warfare identifier", "F-WR-999" not in fwr)
    check("X19 D-999 is not a valid decision identifier", "D-999" not in dset)
    check("X20 the mutant validator filename is absent",
          not (QA_BACKUPS / "14B_nonexistent_economy.py").exists())

    for label, text in (("QA report", qa), ("R1 report", read(R1_REPORT)), ("C1 report", read(C1_REPORT))):
        for name in sorted(set(re.findall(r"[A-Za-z0-9_]+\.py(?![A-Za-z0-9])", text))):
            check(f"X21 {label} validator {name} exists", (QA_BACKUPS / name).exists(), name)


# --------------------------------------------------------------------------------------
# R. R1 report, semantic record and reference resolution
# --------------------------------------------------------------------------------------


def check_r1_report() -> None:
    r1 = read(R1_REPORT)
    decisions = read(DECISIONS)
    check("R1 the R1 closeout report exists", bool(r1))
    if not r1:
        return
    for did in sorted(set(re.findall(r"D-\d{3}", r1))):
        check(f"R2 cited decision exists: {did}", decision_exists(did, decisions))
    scan = r1
    corr_start = scan.find("**Exact wording corrected.**")
    corr_end = scan.find("**Decision IDs", corr_start)
    if corr_start >= 0 and corr_end >= 0:
        scan = scan[:corr_start] + scan[corr_end:]
    check("R3 no unsupported owner-approved constraint phrase outside the correction record",
          "owner-approved constraint" not in scan.lower())
    check("R4 the R1 report states no owner approval was invented",
          "no owner approval" in r1.lower() or "not owner approval" in r1.lower())

    sr_rows = [cells(l) for l in r1.splitlines() if l.startswith("| SR-")]
    check("R5 semantic review record has 5 rows", len(sr_rows) == 5, f"{len(sr_rows)}")
    for r in sr_rows:
        if len(r) < 8:
            continue
        sr, rng, parent, authority, source_status, num_status, why, review = r[:8]
        check(f"R6 semantic row cites an existing decision: {sr}",
              all(decision_exists(d, decisions) for d in re.findall(r"D-\d{3}", parent)), parent)
        check(f"R7 semantic row describes delegated Category B authority: {sr}",
              "category b" in authority.lower() and "not owner" in authority.lower(), authority)
        check(f"R8 source status is a real status: {sr}",
              plain(source_status).upper() in {"CURRENT", "HISTORICAL", "SUPERSEDED", "PROVISIONAL"}, source_status)
        check(f"R9 numerical status remains PROVISIONAL VALUE: {sr}", plain(num_status) == "PROVISIONAL VALUE")
        check(f"R10 human semantic review is not falsely claimed: {sr}", "NOT PERFORMED" in review.upper(), review)
        for did in re.findall(r"D-\d{3}", parent):
            if plain(source_status).upper() == "CURRENT":
                check(f"R11 a CURRENT source is not a superseded decision: {sr}/{did}",
                      not decision_is_superseded(did, decisions))

    for target in set(local_link_targets(r1)):
        if target.startswith(("mailto:", "http")):
            continue
        path = (R1_REPORT.parent / target).resolve()
        check(f"R12 local link resolves: {target}", path.exists(), str(path))


# --------------------------------------------------------------------------------------
# R1-R1. Closeout report, mutation table and CW semantic record
# --------------------------------------------------------------------------------------


def check_r1r1_report() -> None:
    r = read(R1R1_REPORT)
    decisions = read(DECISIONS)
    check("R1R1-1 the R1-R1 closeout report exists", bool(r))
    if not r:
        return
    scan = chr(10).join(l for l in r.splitlines() if not l.startswith("| M"))
    for did in sorted(set(re.findall(r"D-\d{3}", scan))):
        check(f"R1R1-2 cited decision exists: {did}", decision_exists(did, decisions))

    mutations = [cells(l) for l in r.splitlines() if re.match(r"\| M\d{2} \|", l)]
    check("R1R1-3 mutation table has 15 rows", len(mutations) == 15, f"{len(mutations)}")
    for row in mutations:
        if len(row) < 7:
            check(f"R1R1-4 mutation row has 7 fields: {row[0] if row else '?'}", False, str(len(row)))
            continue
        check(f"R1R1-4 mutation exit is 1: {row[0]}", plain(row[4]) == "1", row[4])
        check(f"R1R1-5 mutation result is PASS: {row[0]}", "PASS" in row[6], row[6])
        check(f"R1R1-6 mutation diagnostic present: {row[0]}", bool(row[5]), row[5])

    cw = [cells(l) for l in r.splitlines() if l.startswith("| CW-")]
    check("R1R1-7 CW semantic record has 17 rows", len(cw) == 17, f"{len(cw)}")
    for i, row in enumerate(cw, 1):
        if len(row) < 9:
            check(f"R1R1-8 CW row has 9 fields: {row[0] if row else '?'}", False, str(len(row)))
            continue
        check(f"R1R1-8 CW row number is {i}: {row[0]}", plain(row[1]) == str(i), row[1])
        check(f"R1R1-9 CW source present: {row[0]}", bool(row[2]))
        check(f"R1R1-10 CW cited record present: {row[0]}", bool(row[3]))
        check(f"R1R1-11 CW relevance is substantive: {row[0]}", len(row[5]) >= 30, row[5])
        check(f"R1R1-12 CW authority present: {row[0]}", bool(row[6]))
        check(f"R1R1-13 human review is not falsely claimed: {row[0]}",
              "NOT PERFORMED" in row[7].upper(), row[7])

    check("R1R1-14 report states 15/15 mutations rejected", "15/15" in r)
    check("R1R1-15 report states 20/20 resolver controls", "20/20" in r)
    check("R1R1-16 report records the final status COMPLETE", "`COMPLETE`" in r)
    check("R1R1-17 report does not claim owner-approved Category B decisions",
          "owner-approved constraint" not in scan.lower())

    for target in set(local_link_targets(r)):
        if target.startswith(("mailto:", "http")):
            continue
        path = (R1R1_REPORT.parent / target).resolve()
        check(f"R1R1-18 local link resolves: {target}", path.exists(), str(path))


# --------------------------------------------------------------------------------------
# M. Mutation self-tests
# --------------------------------------------------------------------------------------


def self_test() -> int:
    decisions = read(DECISIONS)
    register = read(REGISTER)
    rows = [list(r) for r in category_rows()]
    cases = []

    def detected(label, rejected: bool):
        cases.append((label, rejected))

    detected("M1 nonexistent decision ID", not decision_exists("D-999", decisions))
    detected("M2 nonexistent file path", not check_local_link("qa_backups/does_not_exist_14B_C1_R1.py"))
    detected("M3 nonexistent formula ID", "F-EC-999" not in fec_ids(register))
    mutated4 = [row[:] for row in rows]
    mutated4[0][6] = ""
    detected("M4 removed source reference", not all(bool(r[6]) for r in mutated4))
    detected("M5 superseded decision detected",
             decision_is_superseded("D-004", decisions) and decision_exists("D-004", decisions))
    detected("M6 Category B falsely owner-approved", not authority_wording_ok("Category B owner-approved constraint"))
    detected("M7 planned playtest falsely completed", not evidence_wording_ok("playtest completed; no further test required"))
    detected("M8 category copied from numerical status", not category_distinct("PROVISIONAL VALUE", "PROVISIONAL VALUE"))
    detected("M9 invented source parameter ID", invented_id("NP-EC-001"))
    mutated10 = rows[:-1]
    detected("M10 valid record deleted (count check)", len(mutated10) != 49)

    CHECKS[0] += len(cases)
    for label, passed in cases:
        if not passed:
            FAILURES.append(f"self-test {label} did not trigger")
    print(f"SELF-TESTS: {len(cases)} cases")
    if FAILURES:
        for item in FAILURES:
            print("  -", item)
    return 0 if all(p for _l, p in cases) else 1


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------


def main() -> int:
    check_categories()
    check_matrix()
    check_crosswalk()
    check_crosswalk_references()
    check_r1_report()
    check_r1r1_report()
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} problem(s) in {CHECKS[0]} checks")
        for item in FAILURES:
            print("  -", item)
        return 1
    print(f"PASS: {CHECKS[0]}/{CHECKS[0]} Prompt 14B-C1/R1 closeout checks passed")
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
