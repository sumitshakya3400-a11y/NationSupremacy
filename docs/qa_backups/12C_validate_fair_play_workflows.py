#!/usr/bin/env python3
"""Prompt 12C fair-play workflow, integration and acceptance validator.

Stdlib-only document checker. It grades the internal consistency of the three
Prompt 12C deliverables and the governance clauses Prompt 12C §5 and §12 require
to be preserved. It proves nothing about runtime behaviour: there is no
implementation for it to test.

Exit codes: 0 all checks pass, 1 a check failed, 2 the corpus could not be read.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "stage-2"

FILES = {
    "workflows": DOCS / "20_fair_play_and_player_protection_workflows.md",
    "integration": DOCS / "20_fair_play_and_player_protection_integration.md",
    "acceptance": DOCS / "20_fair_play_and_player_protection_edge_cases_acceptance.md",
    "rulebook": DOCS / "20_fair_play_and_player_protection.md",
    "requirements": DOCS / "20_fair_play_and_player_protection_requirements.md",
    "formulas": DOCS / "20_fair_play_and_player_protection_formula_register.md",
    "accept12b": DOCS / "20_fair_play_and_player_protection_acceptance.md",
    "handoff": DOCS / "00_stage_2_handoff.md",
    "log": DOCS / "06_stage_2_progress_log.md",
    "ai_context": ROOT / "AI_CONTEXT.md",
    "ai_handoff": ROOT / "AI_HANDOFF.md",
    "progress": ROOT / "PROJECT_PROGRESS.md",
    "roadmap": ROOT / "ROADMAP.md",
    "stage_roadmap": DOCS / "01_stage_2_prompt_roadmap.md",
}

EXPECT = {
    "FPJ": 10,
    "FPW": 52,
    "FPE": 100,
    "FPA": 378,
    "INT": 20,
    "GATE": 20,
    "REQ": 106,
    "FPG": 10,
}

FPE_CATEGORIES = {"C1": 6, "C2": 24, "C3": 7, "C4": 25, "C5": 19, "C6": 19}
FPA_CLASSES = {"POS": 48, "NEG": 48, "BND": 43, "SEC": 77, "INT": 47, "REC": 44, "PRV": 36, "OWN": 35}
FPA_EXEC = {"auto": 169, "integration": 114, "manual": 95}
FPA_STATUS = {"SPECIFIED": 368, "BLOCKED": 10}
GATE_TALLY = {"PASS": 16, "PARTIAL": 2, "BLOCKED": 2}

B12_PREFIXES = ("FP", "EVD", "MA", "CO", "EX", "PRV", "MOD", "ADM", "COR", "SEC", "INT", "FR", "GOV")
B12_MAXIMA = {"FP": 35, "EVD": 42, "MA": 12, "CO": 10, "EX": 12, "PRV": 25, "MOD": 60,
              "ADM": 30, "COR": 18, "SEC": 40, "INT": 20, "FR": 15, "GOV": 25}

IMPLEMENTATION_CLAIMS = [
    r"\bis implemented\b", r"\bare implemented\b", r"\bhas been implemented\b",
    r"\bis deployed\b", r"\bis enabled\b", r"\bis live\b", r"\bis running\b",
    r"\btests? (?:were|have been) (?:run|executed|passed)\b",
    r"\bwe (?:ran|executed) the (?:anti-cheat|moderation|privacy|security|audit)\b",
    r"\bproduction[- ]ready\b", r"\bthe audit (?:spine|trail) is (?:tamper[- ]proof|immutable|verified|monitored)\b",
    r"\b(?:tamper[- ]evidence|the digest chain) (?:exists|is operating|is active)\b",
    r"\b(?:gdpr|dsa|coppa) complian(?:ce|t)\b", r"\bis legally required of nation supremacy\b",
    r"\bthe prototype (?:profiles|grant) (?:defect )?is fixed\b",
]

NEGATION = r"(?:not|never|no |nothing|without|cannot|until|unless|before|unimplemented|nor|lacks|absence|refus|prohibit|blocked|forbid|remains|still|outstanding|must not|may not|pending|await)"

FIELD_ROW = re.compile(r"^\| (?!Field \|)([A-Z][^|]*)\|", re.M)

HISTORICAL_MARKERS = (r"\bsuperseded\b", r"\bhistorical\b", r"\bprevious\b", r"\bearlier\b",
                      r"\bsnapshot\b", r"\bwas\b", r"\badated\b", r"\b12b[- ]c1\b", r"\br[1-7]\b",
                      r"\bretained\b", r"\bpreserved\b", r"\bv\d+\.\d+\b", r"\b20\d\d-\d\d-\d\d\b")


class Checker:
    def __init__(self, texts: dict[str, str], verbose: bool = False):
        self.t = texts
        self.verbose = verbose
        self.results: list[tuple[str, str, bool, str]] = []

    def run(self, cid: str, title: str, fn):
        try:
            detail = fn()
        except Exception as exc:  # a crash is a failure, never a pass
            detail = f"unexpected error: {type(exc).__name__}: {exc}"
            self.results.append((cid, title, False, detail))
            return
        if detail is None:
            self.results.append((cid, title, True, "ok"))
        else:
            self.results.append((cid, title, False, detail))

    # ---------------------------------------------------------------- helpers
    def all_12c(self) -> str:
        return self.t["workflows"] + "\n" + self.t["integration"] + "\n" + self.t["acceptance"]

    def rows(self, text: str, pattern: str) -> list[list[str]]:
        out = []
        for line in text.splitlines():
            if re.match(pattern, line):
                out.append([c.strip() for c in line.split("|")[1:-1]])
        return out

    def claim_lines(self, name: str):
        for i, line in enumerate(self.t[name].splitlines(), 1):
            yield i, line

    # ------------------------------------------------------------------ checks
    def c01(self):
        problems = []
        for key in ("workflows", "integration", "acceptance"):
            text = self.t[key]
            head = text[:4000]
            for token in ("**Version:**", "**Created:**", "**Status:**", "**Authority.**", "**Companions.**"):
                if token not in head:
                    problems.append(f"{key}: missing {token}")
            if not re.search(r"design only|documentation level", head, re.I):
                problems.append(f"{key}: no design-only status clause")
            if "NOT RUN" not in text and "not executed" not in text.lower():
                problems.append(f"{key}: no not-executed clause")
        if problems:
            return "; ".join(problems[:6])
        return None

    def c02(self):
        hits = []
        for name in ("workflows", "integration", "acceptance"):
            for lineno, line in self.claim_lines(name):
                for pat in IMPLEMENTATION_CLAIMS:
                    if re.search(pat, line, re.I) and not re.search(NEGATION, line, re.I):
                        hits.append(f"{name}:{lineno} {pat}")
        if hits:
            return "; ".join(hits[:5])
        return None

    def _records(self, text: str, pfx: str):
        blocks = re.split(r"\n### " + pfx + r"-\d{3} ", text)[1:]
        heads = re.findall(r"### " + pfx + r"-(\d{3}) ", text)
        return heads, blocks

    def c03(self):
        heads, blocks = self._records(self.t["workflows"], "FPJ")
        nums = sorted(int(h) for h in heads)
        if nums != list(range(1, EXPECT["FPJ"] + 1)):
            return f"FPJ ids {nums[:12]} != 1..{EXPECT['FPJ']}"
        bad = [(h, len(FIELD_ROW.findall(b.split("\n---\n")[0])))
               for h, b in zip(heads, blocks)
               if len(FIELD_ROW.findall(b.split("\n---\n")[0])) != 12]
        if bad:
            return f"FPJ records without 12 field rows: {bad[:5]}"
        return None

    def c04(self):
        heads, blocks = self._records(self.t["workflows"], "FPW")
        nums = sorted(int(h) for h in heads)
        if nums != list(range(1, EXPECT["FPW"] + 1)):
            return f"FPW ids != 1..{EXPECT['FPW']} (got {len(nums)})"
        bad = []
        for head, body in zip(heads, blocks):
            body = body.split("\n---\n")[0]
            fields = FIELD_ROW.findall(body)
            if len(fields) != 12:
                bad.append((head, len(fields)))
        if bad:
            return f"FPW records with != 12 fields: {bad[:5]}"
        if "`FPW-053` onward is unallocated" not in self.t["workflows"]:
            return "FPW frontier statement missing"
        return None

    def c05(self):
        counts = {}
        for r in self.rows(self.t["acceptance"], r"^\| `FPE-\d{3}` \|"):
            counts[r[1]] = counts.get(r[1], 0) + 1
        if counts != FPE_CATEGORIES:
            return f"parsed categories {counts} != expected {FPE_CATEGORIES}"
        declared = {
            ("C" + m.group(1)).upper(): int(m.group(2))
            for m in re.finditer(r"\*\*C([1-6]) [a-z ]+ (\d+)\*\*", self.t["acceptance"])
        }
        if declared != FPE_CATEGORIES:
            return f"declared category counts {declared} != parsed {counts}"
        return None

    def c06(self):
        ids = [int(r[0].strip("`").split("-")[1]) for r in self.rows(self.t["acceptance"], r"^\| `FPE-\d{3}` \|")]
        if sorted(ids) != list(range(1, EXPECT["FPE"] + 1)):
            return f"FPE ids != 1..{EXPECT['FPE']} (n={len(ids)}, dupes={len(ids) - len(set(ids))})"
        weak = [i for i, r in zip(ids, self.rows(self.t["acceptance"], r"^\| `FPE-\d{3}` \|"))
                if "FPW-" not in r[5] or "FPA-" not in r[11]]
        if weak:
            return f"edge cases without a workflow or test link: {weak[:6]}"
        return None

    def c07(self):
        text = self.all_12c()
        defs = re.findall(r"^#+\s*`?WEE-\d+", text, re.M)
        if defs:
            return f"12C redefines 11C edge cases: {defs[:3]}"
        if "`WEE-`" not in text and "WEE-001" not in text:
            return "deduplication rule does not cite the 11C register"
        if "not restate" not in text and "not **not** restated" not in text and "are **not**" not in text:
            return "no explicit non-restatement clause"
        return None

    def c08(self):
        matrix = [r for r in self.rows(self.t["integration"], r"^\| `INT-\d{3}` \|")]
        ids = sorted({r[0].strip("`").split("-")[1] for r in matrix})
        if len(ids) != EXPECT["INT"]:
            return f"contract rows define {len(ids)} identifiers != {EXPECT['INT']}"
        if ids != [f"{i:03d}" for i in range(1, 21)]:
            return f"INT ids not 001..020: {ids[:5]}...{ids[-2:]}"
        for m in re.finditer(r"`INT-(0(?:2[1-9]|[3-9]\d))`", self.t["integration"]):
            window = self.t["integration"][max(0, m.start() - 200):m.end() + 200]
            if not re.search(NEGATION, window, re.I):
                return f"INT-0{m.group(1)} used outside a prohibition sentence"
        if len(matrix) != 40:
            return f"matrix rows: {len(matrix)} != 40 (two parts of 20)"
        return None

    def c09(self):
        p1 = self.rows(self.t["integration"], r"^\| `INT-\d{3}` \|")[:20]
        p2 = self.rows(self.t["integration"], r"^\| `INT-\d{3}` \|")[20:]
        for rowset, cols, label in ((p1, 7, "part 1"), (p2, 8, "part 2")):
            for r in rowset:
                if len(r) != cols:
                    return f"{label} row {r[0]} has {len(r)} cells, expected {cols}"
                if any(not c or c == "—" for c in r[1:]):
                    return f"{label} row {r[0]} has an empty field"
        bad = [r[0] for r in p2 if "FPW-" not in r[6] or "FPA-" not in r[7]]
        if bad:
            return f"part 2 rows missing a workflow or test link: {bad[:4]}"
        return None

    def c10(self):
        forbidden = [
            r"B-12 (?:writes|sets|types|edits) (?:a|the) (?:balance|treasury|election|snapshot|treaty|battle)",
            r"only B-12 applies", r"B-12 may re-?parent", r"B-12 owns (?:the|every) balance",
            r"B-12 recomputes (?:a|the) (?:battle|campaign|market)",
        ]
        hits = []
        # table cells are judged individually so that a correct refusal in a neighbouring
        # cell cannot mask an inverted authority claim in the same row
        for name in ("integration", "workflows"):
            for lineno, line in self.claim_lines(name):
                cells = [c for c in line.split("|")[1:-1]] if line.startswith("|") else [line]
                for cell in cells:
                    for pat in forbidden:
                        if re.search(pat, cell, re.I) and not re.search(NEGATION, cell, re.I):
                            hits.append(f"{name}:{lineno} {cell[:48]}")
        return "; ".join(hits[:4]) if hits else None

    def c11(self):
        rows = self.rows(self.t["integration"], r"^\| `(?:C-\d{2}|FPG-\d{2})` \|")
        if len(rows) != 12:
            return f"conflict and gap rows: {len(rows)} != 12 (2 conflicts + 10 gaps)"
        for r in rows:
            if len(r[-1]) < 12:
                return f"{r[0]} lacks an owner or a 12C treatment"
        counts = re.findall(r"`FPG-(\d{2})`", self.t["integration"])
        if len(set(counts)) != EXPECT["FPG"]:
            return f"gap identifiers: {len(set(counts))} != {EXPECT['FPG']}"
        return None

    def c12(self):
        ids = [int(r[0].strip("`").split("-")[1]) for r in self.rows(self.t["acceptance"], r"^\| `FPA-\d{3}` \|")]
        if len(ids) != EXPECT["FPA"]:
            return f"FPA row count {len(ids)} != {EXPECT['FPA']}"
        if sorted(ids) != list(range(1, EXPECT["FPA"] + 1)):
            missing = sorted(set(range(1, EXPECT["FPA"] + 1)) - set(ids))
            dupes = len(ids) - len(set(ids))
            return f"FPA not contiguous: missing {missing[:8]}, duplicates {dupes}"
        return None

    def c13(self):
        rows = self.rows(self.t["acceptance"], r"^\| `FPA-\d{3}` \|")
        cls, ex, st = {}, {}, {}
        blocked = []
        for r in rows:
            cls[r[4]] = cls.get(r[4], 0) + 1
            e = r[9].strip("`")
            ex[e] = ex.get(e, 0) + 1
            status = "BLOCKED" if "BLOCKED" in r[10] else r[10].replace("**", "").strip()
            st[status] = st.get(status, 0) + 1
            if status == "BLOCKED":
                blocked.append(int(r[0].strip("`").split("-")[1]))
        if cls != FPA_CLASSES:
            return f"class tally {cls} != declared {FPA_CLASSES}"
        if ex != FPA_EXEC:
            return f"execution tally {ex} != declared {FPA_EXEC}"
        if st != FPA_STATUS:
            return f"status tally {st} != declared {FPA_STATUS}"
        decl = self.t["acceptance"].split("**3.3 Counts")[1].split("**3.4")[0] if "**3.3 Counts" in self.t["acceptance"] else ""
        if not decl:
            return "no 3.3 declaration block"
        expect_blocked = [309, 310, 311, 312, 313, 314, 316, 318, 319, 320]
        if sorted(blocked) != expect_blocked:
            return f"BLOCKED rows {blocked} != {expect_blocked}"
        decl_cls = {m.group(1): int(m.group(2)) for m in re.finditer(r"`(POS|NEG|BND|SEC|INT|REC|PRV|OWN)` (\d+)", decl)}
        if decl_cls != FPA_CLASSES:
            return f"declared class tally {decl_cls} != parsed {cls}"
        decl_ex = {m.group(1): int(m.group(2)) for m in re.finditer(r"`(auto|integration|manual)` (\d+)", decl)}
        if decl_ex != FPA_EXEC:
            return f"declared execution tally {decl_ex} != parsed {ex}"
        decl_st = {m.group(1): int(m.group(2)) for m in re.finditer(r"`(SPECIFIED|BLOCKED)` (\d+)", decl)}
        if decl_st != FPA_STATUS:
            return f"declared status tally {decl_st} != parsed {st}"
        return None

    def c14(self):
        rows = self.rows(self.t["acceptance"], r"^\| `REQ-\d{3}` \|")
        ids = [r[0] for r in rows]
        if len(ids) != EXPECT["REQ"]:
            return f"ledger rows {len(ids)} != {EXPECT['REQ']}"
        if len(set(ids)) != EXPECT["REQ"]:
            return "duplicate REQ rows in the ledger"
        want = {f"`REQ-{n}`" for n in range(764, 870)}
        missing = sorted(want - set(ids))
        if missing:
            return f"requirements absent from the ledger: {missing[:6]}"
        for r in rows:
            if r[1] == "":
                return f"{r[0]} has no focus"
            if len(r[-1]) < 4 and "none" not in r[-1]:
                return f"{r[0]} has neither a mapping nor a reason"
        return None

    def c15(self):
        text = self.all_12c()
        rules = self.t["rulebook"]
        problems = []
        for pfx, mx in B12_MAXIMA.items():
            for m in re.finditer(rf"`{pfx}-(\d{{3}})`", text):
                n = m.group(1)
                i = int(n)
                if i > mx:
                    window = text[max(0, m.start() - 240):m.end() + 240]
                    if pfx == "INT" and re.search(NEGATION, window, re.I):
                        continue
                    problems.append(f"{pfx}-{n} exceeds the {pfx} frontier {mx}")
                elif pfx == "INT":
                    if f"**{pfx}-{n} —" not in rules:
                        problems.append(f"INT-{n} is not defined in the rulebook §16")
                elif f"**{pfx}-{n} —" not in rules and f"**{pfx}-{n} —" not in self.t["requirements"]:
                    problems.append(f"{pfx}-{n} is not defined in the rulebook")
        if problems:
            return "; ".join(sorted(set(problems))[:6])
        bad_req = sorted({n for n in re.findall(r"`REQ-(\d{3})`", text) if not 1 <= int(n) <= 869})
        if bad_req:
            return f"out-of-range REQ references: {bad_req[:4]}"
        return None

    def c16(self):
        text = self.all_12c()
        if re.search(r"REQ-\d{3}`? is (?:a |the )?new requirement", text):
            return "a requirement is presented as newly created"
        if re.search(r"^\|\s*`?REQ-\d{3}`?\s*\|[^|]{20,}\|\s*\n", text, re.M):
            return "requirement statement duplicated as a 12C register row"
        for m in re.finditer(r"(?:allocat\w+|assign\w+|creat\w+) (?:a |an |the |no |106 |new )*\bREQ-(\d{3})", text):
            window = text[max(0, m.start() - 160):m.end() + 160]
            if not re.search(NEGATION, window, re.I):
                return f"possible new requirement allocation: {m.group(0)[:60]}"
        return None

    def c17(self):
        text = self.all_12c()
        need = {
            "P12B-14": r"P12B-14",
            "P12B-16": r"P12B-16",
            "P12B-23": r"P12B-23",
            "R8 deferral": r"R8[^.\n]{0,40}(?:DEFERRED|remains \*\*DEFERRED)",
            "12B-C1 not closed": r"12B-C1 (?:remains |stays )?\*{0,2}NOT CLOSED",
            "R7 not independently accepted": r"not[- ]independently[- ]accepted|not independently accepted|R7 remains implemented-but-not-independently-accepted",
            "five residual weaknesses": r"five residual weaknesses",
            "seven 12A PARTIAL gates": r"seven (?:12A|Prompt 12A) ?`?PARTIAL`? gates?",
        }
        missing = [label for label, pat in need.items() if not re.search(pat, text, re.I)]
        for name in ("handoff", "log", "ai_context", "ai_handoff", "progress", "roadmap", "stage_roadmap"):
            body = self.t[name]
            for pat in (r"P12B-14", r"P12B-16|P12B-14/16", r"P12B-23|/23|14/16/23"):
                if not re.search(pat, body):
                    missing.append(f"{name} lost a 12B PARTIAL gate reference")
            if not re.search(r"DEFERRED BY OWNER|R8 remains DEFERRED|R8 is DEFERRED|12B-C1 remains NOT CLOSED", body):
                missing.append(f"{name} lost the R8/12B-C1 clause")
        if missing:
            return "; ".join(missing[:6])
        return None

    def c18(self):
        text = self.all_12c()
        pending = NEGATION + r"|would need|keep their exact status|keep their existing status|is written to the boundary"
        bad = []
        for ud in ("UD-017", "UD-044", "UD-046", "UD-050", "UD-052", "UD-053", "UD-054",
                   "UD-055", "UD-056", "UD-057", "UD-058", "UD-059", "UD-060"):
            for m in re.finditer(ud, text):
                seg = text[max(0, m.start() - 160):m.end() + 160]
                if re.search(r"\b(?:resolved|closed|settled|answered|decided|approved)\b", seg, re.I) \
                        and not re.search(pending, seg, re.I):
                    bad.append(ud)
                    break
        if bad:
            return f"owner-reserved rows described as settled: {sorted(set(bad))}"
        if "Open**" not in text and "**Open" not in text:
            return "no visible Open dependency wording"
        return None

    def c19(self):
        text = self.all_12c()
        if "PROVISIONAL_BLOCK" not in text:
            return "PROVISIONAL_BLOCK branch is absent"
        for name in ("workflows", "acceptance"):
            for lineno, line in self.claim_lines(name):
                if re.search(r"(?:parameter|weight|duration|window|cap|interval|rate|band) is approved", line, re.I) \
                        and not re.search(NEGATION, line, re.I):
                    return f"{name}:{lineno} promotes a parameter"
        return None

    def c20(self):
        text = self.all_12c()
        pat = r"(?:always|never|globally)\s+fail\s+(?:open|closed)(?:\s+(?:across|for)\s+(?:the\s+)?(?:whole|entire|system|game))?"
        hits = [m.group(0) for m in re.finditer(pat, text, re.I)
                if not re.search(r"no global|never a global|not a global|prohibit", text[max(0, m.start() - 220):m.start() + 220], re.I)]
        if hits:
            return f"universal posture statement: {hits[:2]}"
        return None

    def c21(self):
        problems = []
        for name in ("workflows", "integration", "acceptance"):
            for lineno, line in self.claim_lines(name):
                if re.match(r"^\*\*(?:FP|EVD|MA|CO|EX|PRV|MOD|ADM|COR|SEC|FR|GOV)-\d{3}", line):
                    problems.append(f"{name}:{lineno} defines a B-12 rule")
                if re.search(r"12C (?:adds|creates|introduces) (?:a |an )?(?:new )?(?:rule|violation class|tier|evidence state|transaction type|privacy class|role|posture)", line, re.I) \
                        and not re.search(NEGATION, line, re.I):
                    problems.append(f"{name}:{lineno} claims a new normative object")
        if re.search(r"\bT6\b|\bV-1[7-9]\b|\bE4\b|\bseventh (?:correction type|sanction tier|evidence state)\b", self.all_12c()):
            problems.append("an out-of-range normative identifier appears")
        return "; ".join(problems[:4]) if problems else None

    def c22(self):
        surfaces = ("ai_context", "ai_handoff", "progress", "roadmap", "handoff", "stage_roadmap", "log")
        missing = [s for s in surfaces if "12C" not in self.t[s]]
        if missing:
            return f"surfaces not naming 12C: {missing}"
        if "P12C-" not in self.t["log"]:
            return "the progress log does not cite the 12C gate register"
        return None

    def c23(self):
        gates = self.rows(self.t["acceptance"], r"^\| `P12C-\d{2}` \|")
        ids = [r[0] for r in gates]
        if len(ids) != EXPECT["GATE"] or sorted(int(i.strip("`").split("-")[1]) for i in ids) != list(range(1, 21)):
            return f"gate ids != P12C-01..{EXPECT['GATE']} (n={len(ids)})"
        tally = {}
        for r in gates:
            res = re.sub(r"\*", "", r[5]).strip()
            tally[res] = tally.get(res, 0) + 1
        if tally != GATE_TALLY:
            return f"parsed gate tally {tally} != declared {GATE_TALLY}"
        declared = re.search(r"Tally: (\d+) `PASS` . (\d+) `PARTIAL` . (\d+) `BLOCKED`", self.t["acceptance"])
        if not declared or (int(declared.group(1)), int(declared.group(2)), int(declared.group(3))) != (16, 2, 2):
            return "declared gate tally line does not match the P12C gate rows"
        return None

    def c24(self):
        text = self.all_12c()
        for pat, why in ((r"\brow count[s]? (?:is )?\d+ (?:tests?|workflows?) pass(?:ed)?\b", "test-count pass claim"),
                         (r"\bspecification complete and verified\b", "verification conflation"),
                         (r"\bacceptance (?:is |was )?(?:met|achieved|passed)\b", "acceptance passed claim")):
            for m in re.finditer(pat, text, re.I):
                if not re.search(NEGATION, text[max(0, m.start() - 160):m.end() + 160], re.I):
                    return f"{why}: {m.group(0)[:48]}"
        return None


CHECKS = [
    ("12C-01", "the three 12C deliverables exist with header, status, authority and non-claim blocks", "c01"),
    ("12C-02", "no implementation, migration, execution or legal-compliance claim appears", "c02"),
    ("12C-03", "FPJ-001..FPJ-010 are contiguous and complete", "c03"),
    ("12C-04", "FPW-001..FPW-052 are contiguous and every record carries twelve fields", "c04"),
    ("12C-05", "declared edge-case category counts equal the parsed register", "c05"),
    ("12C-06", "FPE-001..FPE-100 are contiguous, unique and linked", "c06"),
    ("12C-07", "11C edge cases are cited, never restated or renumbered", "c07"),
    ("12C-08", "the integration matrix uses exactly INT-001..INT-020", "c08"),
    ("12C-09", "both matrix parts fill every operational field", "c09"),
    ("12C-10", "no row gives a system an authority the rulebook does not grant", "c10"),
    ("12C-11", "every conflict and gap names its decider and its 12C treatment", "c11"),
    ("12C-12", "FPA-001..FPA-378 are contiguous and unique", "c12"),
    ("12C-13", "class, execution and status tallies reconcile with the declarations", "c13"),
    ("12C-14", "the traceability ledger covers REQ-764..REQ-869 without gap or duplicate", "c14"),
    ("12C-15", "every cited B-12 rule identifier exists and stays inside its frontier", "c15"),
    ("12C-16", "no requirement is restated as a new requirement or reallocated", "c16"),
    ("12C-17", "the three 12B PARTIAL gates, seven 12A gates and the R7/R8/12B-C1 clauses are preserved", "c17"),
    ("12C-18", "no owner-reserved or legal UD row is described as resolved", "c18"),
    ("12C-19", "PROVISIONAL_BLOCK remains the specified branch and no parameter is promoted", "c19"),
    ("12C-20", "no universal fail-open or fail-closed statement exists", "c20"),
    ("12C-21", "12C defines no B-12 rule, tier, class, state, role or posture", "c21"),
    ("12C-22", "the project status surfaces name Prompt 12C", "c22"),
    ("12C-23", "the P12C gate register is complete with a reconciling tally", "c23"),
    ("12C-24", "no acceptance-passed or verification-conflating wording exists", "c24"),
]


def load():
    texts = {}
    for key, path in FILES.items():
        if not path.exists():
            raise SystemExit(f"FATAL: required file missing: {path}")
        texts[key] = path.read_text(encoding="utf-8")
    return texts


def run_all(texts, verbose=False):
    ck = Checker(texts, verbose)
    for cid, title, meth in CHECKS:
        ck.run(cid, title, getattr(ck, meth))
    return ck.results


# --------------------------------------------------------------------- fixtures
NEGATIVE = [
    ("NEG-01 implementation claim", "workflows",
     lambda t: t.replace("## 2. Terminology used by every record",
                         "The moderation queue is implemented and running today.\n\n## 2. Terminology used by every record", 1), "12C-02"),
    ("NEG-02 workflow deleted", "workflows",
     lambda t: t.replace("### FPW-043 —", "### FPW-943 —", 1), "12C-04"),
    ("NEG-03 workflow field dropped", "workflows",
     lambda t: t.replace("| Notifications | Internal only; the reporter keeps", "|  | Internal only; the reporter keeps", 1), "12C-03"),
    ("NEG-04 edge case renumbered", "acceptance",
     lambda t: t.replace("| `FPE-077` |", "| `FPE-977` |", 1), "12C-06"),
    ("NEG-05 category count falsified", "acceptance",
     lambda t: t.replace("**C6 privacy and information handling 19**", "**C6 privacy and information handling 8**", 1),
     "12C-05"),
    ("NEG-06 new contract allocated", "integration",
     lambda t: t.replace("| `INT-020` |", "| `INT-021` |\n| `INT-020` |", 1), "12C-08"),
    ("NEG-07 balance written by B-12", "integration",
     lambda t: t.replace("B-12 instructs; **B-04 computes and appends**", "B-12 writes the balance directly", 1),
     "12C-10"),
    ("NEG-08 test tally falsified", "acceptance",
     lambda t: t.replace("`SEC` 77", "`SEC` 60", 1), "12C-13"),
    ("NEG-09 requirement dropped", "acceptance",
     lambda t: re.sub(r"^\| `REQ-819` \|\n?", "", t, flags=re.M) if re.search(r"^\| `REQ-819` \|", t, re.M)
     else t.replace("| `REQ-819` | owner's appended correction path", "| `REQ-899` | owner's appended correction path", 1),
     "12C-14"),
    ("NEG-10 invented rule identifier", "workflows",
     lambda t: t.replace("`MOD-036`", "`MOD-071`", 1), "12C-15"),
    ("NEG-11 owner decision described as closed", "acceptance",
     lambda t: t.replace("`UD-053` Open", "`UD-053` resolved and closed", 1), "12C-18"),
    ("NEG-12 universal fail-closed rule", "workflows",
     lambda t: t.replace("**1.4 Owner-reserved questions stay open.**",
                         "All controls always fail open across the whole system.\n\n**1.4 Owner-reserved questions stay open.**", 1),
     "12C-20"),
    ("NEG-13 new violation class", "workflows",
     lambda t: t.replace("**1.2 It is not an implementation claim.**",
                         "12C introduces a new violation class V-17 for automation clusters.\n\n"
                         "**1.2 It is not an implementation claim.**", 1), "12C-21"),
    ("NEG-14 gate result inflated", "acceptance",
     lambda t: t.replace("| **PARTIAL** | Two registered conflicts", "| **PASS** | Two registered conflicts", 1),
     "12C-23"),
    ("NEG-15 preservation clause deleted", "workflows",
     lambda t: t.replace("R8 remains **DEFERRED BY OWNER**", "R8 remains **ACCEPTED AND CLOSED**", 1), "12C-17"),
    ("NEG-16 acceptance passed wording", "acceptance",
     lambda t: t.replace("**4.3 Ledger totals.**", "Acceptance is met for every workflow.\n\n**4.3 Ledger totals.**", 1),
     "12C-24"),
]


def self_test(verbose=False):
    base = load()
    ok = 0
    results = run_all(base, verbose=False)
    failed = [r for r in results if not r[2]]
    if failed:
        print(f"POSITIVE BASELINE: {len(results) - len(failed)}/{len(results)} checks passed")
        for cid, title, _, detail in failed:
            print(f"  [FAIL] {cid} — {detail}")
        return 1
    print(f"POSITIVE BASELINE: {len(results)}/{len(results)} checks passed on the unmutated corpus")
    ok += 1
    for name, key, mutate, expect in NEGATIVE:
        texts = dict(base)
        texts[key] = mutate(base[key])
        if texts[key] == base[key]:
            print(f"  [SKIP] {name}: mutation did not apply")
            continue
        res = run_all(texts, verbose=False)
        failing = {c for c, _t, good, _d in res if not good}
        if expect in failing:
            print(f"  [OK]   {name} rejected by {expect}")
            ok += 1
        elif failing:
            print(f"  [FAIL] {name}: expected {expect}, got {sorted(failing)}")
        else:
            print(f"  [FAIL] {name}: mutation was accepted by every check (expected {expect})")
    print(f"NEGATIVE FIXTURES: {ok - 1}/{len(NEGATIVE)} rejected for the expected reason")
    return 0 if ok - 1 == len(NEGATIVE) else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Prompt 12C documentation validator")
    ap.add_argument("--self-test", action="store_true", help="run the fixture suite")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--root", default=None, help="override the docs root for fixture runs")
    args = ap.parse_args(argv)
    if args.root:
        global DOCS, ROOT
        ROOT = pathlib.Path(args.root)
        DOCS = ROOT / "stage-2"
        for k, v in list(FILES.items()):
            FILES[k] = (DOCS / v.name) if k not in ("ai_context", "ai_handoff", "progress", "roadmap") else (ROOT / v.name)
    if args.self_test:
        return self_test(args.verbose)
    texts = load()
    results = run_all(texts, args.verbose)
    failed = 0
    for cid, title, good, detail in results:
        if not good:
            failed += 1
            print(f"[FAIL] {cid} {title} — {detail}")
        elif args.verbose:
            print(f"[PASS] {cid} {title}")
    print(f"\nCHECKS: {len(results) - failed}/{len(results)} passed; {failed} failed")
    if failed:
        print("The validator grades documents only. It is not a security test, a runtime test, "
              "an executed acceptance test or an independent acceptance of Prompt 12C.")
        return 1
    print("RESULT: PASS at the documentation level. No workflow, contract, edge case or acceptance "
          "specification has been implemented or executed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
