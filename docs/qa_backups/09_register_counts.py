#!/usr/bin/env python3
"""Prompt 9 QA: count identifier-register entries from the saved Stage 1 reports.

Read-only. Does not modify project documents. Counts *distinct* IDs matched by
each family's pattern, reports ranges, gaps for numbered families, and checks
that proposed new Prompt 9 prefixes are unused.
"""
import re
import os
import sys
from collections import OrderedDict

DOCS = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(DOCS)                      # docs/
STAGE1 = os.path.join(BASE, "stage-1")


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main():
    files = OrderedDict()
    for name in ("AI_CONTEXT.md", "AI_HANDOFF.md", "PROJECT_PROGRESS.md", "DECISIONS.md"):
        files[name] = read(os.path.join(BASE, name))
    for name in sorted(os.listdir(STAGE1)):
        if name.endswith(".md"):
            files["stage-1/" + name] = read(os.path.join(STAGE1, name))

    blob = "\n".join(files.values())

    families = OrderedDict([
        ("F", r"\bF-\d{3}[a-z]?\b"),
        ("O", r"\bO-\d{1,2}\b"),
        ("FO", r"\bFO-\d{3}\b"),
        ("PXE", r"\bPXE-\d{3}\b"),
        ("PR", r"\bPR-\d{1,2}\b"),
        ("PXO", r"\bPXO-\d{3}\b"),
        ("V", r"\bV-\d{1,2}\b"),
        ("CV", r"\bCV-\d{3}\b"),
        ("CX", r"\bCX-\d\b"),
        ("DP", r"\bDP-\d{3}\b"),
        ("UXD", r"\bUXD-\d{3}\b"),
        ("AP", r"\bAP-\d{3}\b"),
        ("CCR", r"\bCCR-\d{3}\b"),
        ("DIR", r"\bDIR-\d\b"),
        ("RC", r"\bRC-\d\b"),
        ("H", r"\bH-\d\b"),
        ("SYS", r"\bSYS-\d{3}\b"),
        ("INT", r"\bINT-\d{3}\b"),
        ("SDQ", r"\bSDQ-\d{3}\b"),
        ("SIM", r"\bSIM-\d{3}\b"),
        ("MO", r"\bMO-\d{3}\b"),
        ("R", r"\bR-\d{2}\b"),
        ("ECON", r"\bECON-\d{3}\b"),
        ("ECOQ", r"\bECOQ-\d{3}\b"),
        ("ECV", r"\bECV-\d{3}\b"),
        ("MAT", r"\bMAT-\d{2}\b"),
        ("TH", r"\bTH-\d{3}\b"),
        ("SEC", r"\bSEC-\d{3}\b"),
        ("ST", r"\bST-\d{3}\b"),
        ("OSQ", r"\bOSQ-\d{3}\b"),
        ("D", r"\bD-\d{3}\b"),
        ("G", r"\bG-[1-6]\b"),
    ])

    print("=" * 78)
    print("IDENTIFIER FAMILY COUNTS (distinct IDs seen anywhere in docs/)")
    print("=" * 78)
    for fam, pat in families.items():
        ids = sorted(set(re.findall(pat, blob)))
        nums = []
        for i in ids:
            m = re.search(r"(\d+)[a-z]?$", i)
            if m:
                nums.append(int(m.group(1)))
        span = ""
        if nums:
            lo, hi = min(nums), max(nums)
            missing = [n for n in range(lo, hi + 1) if n not in nums]
            span = f" range {lo:03d}-{hi:03d}"
            if missing and fam not in ("O", "V", "R", "H", "RC", "DIR", "CX", "PR", "G"):
                span += f" gaps={missing}"
        print(f"{fam:6s} count={len(ids):3d}{span}")

    print()
    print("=" * 78)
    print("PROPOSED PROMPT-9 PREFIX COLLISION CHECK")
    print("=" * 78)
    for prefix in ("REQ-", "ZD-", "GATE-", "DEF-", "TQ-", "IV-", "PV-"):
        hits = re.findall(re.escape(prefix) + r"\d", blob)
        print(f"{prefix:7s} existing uses: {len(hits)}")

    print()
    print("=" * 78)
    print("FILES SCANNED")
    print("=" * 78)
    for name in files:
        print(" ", name, len(files[name].splitlines()), "lines")


if __name__ == "__main__":
    sys.exit(main())
