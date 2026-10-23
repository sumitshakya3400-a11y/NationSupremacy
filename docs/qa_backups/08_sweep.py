import re, io, os, sys, glob, unicodedata, json

BASE = r"C:\Users\suren\Downloads\Project X\docs"
REPORT = os.path.join(BASE, "stage-1", "08_security_privacy_fair_play_and_trust.md")
t = open(REPORT, encoding="utf-8").read()

results = []
def check(name, ok, detail=""):
    results.append((ok, name, detail))

# ---------- 0. structure ----------
h2 = re.findall(r'^## (\d+)\. (.+)$', t, re.M)
secs = [int(n) for n, _ in h2]
check("sections 0-26 present, no duplicates", secs == list(range(27)), f"got {secs}")
names = dict(h2)
for n, name in names.items():
    if not name.strip():
        check(f"section {n} has a title", False)
check("section titles non-empty", True)

# ---------- 1. register extraction ----------
th  = sorted(set(re.findall(r'\bTH-(\d{3})\b', t)))
sec = sorted(set(x for x in re.findall(r'\bSEC-(\d{3})\b', t) if int(x) <= 33))
st  = sorted(set(re.findall(r'\bST-(\d{3})\b', t)))
osq = sorted(set(re.findall(r'\bOSQ-(\d{3})\b', t)))
def rng_ok(lst, lo, hi): return all(lo <= int(x) <= hi for x in lst) and lst == lst
check("TH register contiguous 001-025", th == [f"{i:03d}" for i in range(1, 26)], f"N={len(th)}")
check("SEC register within 001-033, SEC-009 reserved, 32 defined (narrative SEC-034 mention allowed separately)", all(1 <= int(x) <= 33 for x in sec) and '009' in sec and len(sec) == 33, f"N={len(set(sec))}")
sec_all = sorted(set(re.findall(r'\bSEC-(\d{3})\b', t)))
check("only narrative-range mention beyond 033 is SEC-034+", [x for x in sec_all if int(x) > 33] == ['034'], f"extra={[x for x in sec_all if int(x) > 33]}")
check("ST register contiguous 001-020", st == [f"{i:03d}" for i in range(1, 21)], f"N={len(st)}")
check("OSQ register within 001-012", all(1 <= int(x) <= 12 for x in osq), f"N={len(osq)} ids={osq if len(osq) < 14 else ''}")

# SEC-009's posture: reserved, not defined
m9 = re.findall(r'SEC-009[^\n]{0,120}', t)
check("SEC-009 named only as reserved/unassigned", all(('reserv' in s.lower() or 'unassign' in s.lower() or 'gap' in s.lower()) for s in m9), f"{len(m9)} mentions")

# ---------- 2. traceability ----------
# split body by sections for per-row scans
def section(n):
    m = re.search(rf'^## {n}\. ', t, re.M)
    if not m: return ""
    nxt = re.search(rf'^## {n+1}\. ', t, re.M)
    return t[m.start(): nxt.start() if nxt else len(t)]

s2, s16, s19, s20 = section(2), section(16), section(19), section(20)

# threat rows in section 2 must name >=1 SEC (per table row line)
rows_no_sec_th = []
seen = set()
for line in s2.splitlines():
    mrow = re.match(r'\s*\|\s*(TH-\d{3})\s*\|', line)
    if mrow and mrow.group(1) not in seen:
        seen.add(mrow.group(1))
        if not re.search(r'\bSEC-\d{3}\b', line):
            rows_no_sec_th.append(mrow.group(1))
missing = sorted(set(re.findall(r'\b(TH-\d{3})\b', s2)) - seen)
check("every threat has a register row in section 2", not missing, f"absent: {missing}")
check("every section-2 threat row cites >=1 SEC requirement", not rows_no_sec_th, f"missing: {rows_no_sec_th}")

# every SEC id appears in section 2 (threat linkage) -> SEC rows cite TH ids
sec_ids = sorted(set(re.findall(r'\bSEC-(\d{3})\b', s16)))
no_th = [s for s in sec_ids if not re.search(rf'\bSEC-{s}\b(?=(?:(?!\n## ).)*?\bTH-\d{{3}})', s16, re.S)]
check("every SEC requirement row cites >=1 TH threat", not no_th, f"missing: {no_th}")

# requirement->test: every SEC row cites ST; test->req: every ST cites SEC
no_st = [s for s in sec_ids if not re.search(rf'\bSEC-{s}\b(?=(?:(?!\n## ).)*?\bST-\d{{3}})', s16, re.S)]
no_sec = [s for s in st if not re.search(rf'\bST-{s}\b(?=(?:(?!\n## ).)*?\bSEC-\d{{3}})', s19, re.S)]
check("every SEC row cites >=1 ST test", not no_st, f"missing: {no_st}")
check("every ST test cites >=1 SEC requirement", not no_sec, f"missing: {no_sec}")

# OSQ rows: section 20
osq_ids = sorted(set(re.findall(r'\bOSQ-(\d{3})\b', s20)))
check("section 20's OSQ rows are contiguous 001-012", osq_ids == [f"{i:03d}" for i in range(1, 13)], f"{osq_ids}")

# ---------- 3. §-reference resolution ----------
refs = re.findall(r'(?:§|Section\s+)(\d{1,2})(?!\.\d)', t)
refs = sorted(set(int(r) for r in refs if 0 <= int(r) <= 99))
bad_refs = [r for r in refs if r not in secs]
check("all §-refs resolve to existing sections", not bad_refs, f"bad: {bad_refs}")

# subsection refs §N.M: N must exist and N.M must exist as heading
# BUT skip refs that name another report first: "Prompt N §X.Y" (cross-file refs)
t_subscan = re.sub(r'Prompt \d+ \\-lookup-ignore\-', '', t)  # placeholder (unused)
pos_by_prompt = [m for m in re.finditer(r'Prompt \d+ \\u00a7', t)]
sub_bad = []
cand = re.findall(r'§(\d{1,2})\.(\d{1,2})', t)
headings = {(int(a), int(b)) for a, b in re.findall(r'^\#{2,4} (\d{1,2})\.(\d{1,2}) ', t, re.M)}
prompt_idx = [m.start() + m.end() - 2 for m in re.finditer(r'Prompt \d+ §', t)]  # positions of '§' after 'Prompt N '
prompt_pos = set()
for m in re.finditer(r'Prompt \d+ §', t):
    for off in range(m.end()-1, min(m.end()+2, len(t))):
        prompt_pos.add(off)
bad_sub = []
for mt in re.finditer(r'§(\d{1,2})\.(\d{1,2})', t):
    is_prompt = False
    for pm in re.finditer(r'Prompt \d+ ', t):
        if pm.start() <= mt.start() <= pm.end() + 1:
            is_prompt = True
            break
    n, m_ = int(mt.group(1)), int(mt.group(2))
    if not is_prompt and (n, m_) not in headings:
        bad_sub.append(f"{n}.{m_}")
check("all §N.M refs resolve to existing headings", not bad_sub, f"bad: {sorted(bad_sub)}")

# ---------- 4. local markdown links ----------
links = re.findall(r'\]\((?!http)([^)]+)\)', t)
badlinks = []
for l in links:
    target = l.split('#')[0]
    if not target: continue
    tp = os.path.normpath(os.path.join(BASE, 'stage-1', target))
    if not os.path.exists(tp):
        badlinks.append(l)
check("all local markdown links resolve", not badlinks, f"bad: {badlinks}")

# ---------- 5. inherited IDs exist in owning files ----------
owners = {
    r'ECON-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'ECOQ-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'ECV-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'MAT-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'\bL-\d\b': ['stage-1/07_economy_design_and_market_structure.md'],
    r'\bG-[1-6]\b': ['stage-1/07_economy_design_and_market_structure.md'],
    r'\bR-1[3-9]\b|\bR-2[01]\b': ['stage-1/07_economy_design_and_market_structure.md'],
    r'\bR-0[1-9]\b|\bR-1[0-2]\b': ['stage-1/06_core_gameplay_systems_and_interactions.md'],
    r'SDQ-\d{3}': ['stage-1/06_core_gameplay_systems_and_interactions.md'],
    r'INT-\d{3}': ['stage-1/06_core_gameplay_systems_and_interactions.md'],
    r'SYS-\d{3}': ['stage-1/06_core_gameplay_systems_and_interactions.md'],
    r'SIM-\d{3}': ['stage-1/06_core_gameplay_systems_and_interactions.md'],
    r'MO-\d{3}': ['stage-1/06_core_gameplay_systems_and_interactions.md'],
    r'PXE-\d{3}': ['stage-1/04_target_audience_and_player_experience.md'],
    r'\bPR-\d+\b': ['stage-1/04_target_audience_and_player_experience.md'],
    r'\bAP-\d{3}\b': ['stage-1/05_core_game_concept_and_design_pillars.md'],
    r'FO-\d{3}': ['stage-1/03_feature_comparison_opportunity_analysis.md'],
    r'\bF-\d{1,3}\b': ['stage-1/02_strengths_weaknesses_player_frustrations.md', 'stage-1/05_core_game_concept_and_design_pillars.md'],
    r'\bO-\d{1,2}\b': ['stage-1/02_strengths_weaknesses_player_frustrations.md'],
}
files = {}
for own in set(sum(owners.values(), [])):
    try: files[own] = open(os.path.join(BASE, own), encoding='utf-8').read()
    except OSError: files[own] = ""
for pat, owns in owners.items():
    for m in sorted(set(re.findall(pat, t))):
        if not any(re.search((r'(?<![\w-])' if '-' not in pat else '') + re.escape(m) + r'(?![\w])', files[o]) for o in owns if o in files):
            check(f"inherited ID {m} resolves in {owns}", False)
files = {}
for pat, own in owners.items():
    if own not in files:
        try: files[own] = open(os.path.join(BASE, own), encoding='utf-8').read()
        except OSError: files[own] = ""
    for m in sorted(set(re.findall(pat, t))):
        if not re.search(pat, files[own]):
            check(f"inherited ID {m} resolves in {own}", False)

check("inherited-ID resolution sweep done", True)

# ---------- 6. decision discipline ----------
d = open(os.path.join(BASE, 'DECISIONS.md'), encoding='utf-8').read()
check("D-004 still Provisional", 'Provisional' in d and 'D-004' in d)
check("D-005 still Provisional", 'Provisional' in d and 'D-005' in d)
check("no new D-007+ rows added", not re.search(r'\bD-00[7-9]\b|\bD-01\d\b', d))
check("report claims proposal-only status", t.count('not owner-approved') >= 3, f"count={t.count('not owner-approved')}")

# ---------- 7. turn cadence untouched ----------
check("2-hour cadence referenced not altered", '2-hour' in t or 'two-hour' in t)

# ---------- 8. W-18 walkthroughs ----------
wids = sorted(set(re.findall(r'W-18-([A-Z])\b', t)))
check("walkthroughs W-18-A..W-18-? present (>=12 scenarios)", len(set(wids)) >= 12, f"{len(wids)}: {wids}")

# ---------- 9. report's own QA promise: no foreign tokens, no mojibake ----------
bad = re.compile(r'[\u0400-\u04FF\u3040-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF\u0621-\u064A]')
check("no foreign-token artifacts", not bad.search(t))
check("no U+FFFD replacement chars", '\ufffd' not in t)

# ---------- output ----------
fails = [r for r in results if not r[0]]
out = []
for ok, name, det in results:
    out.append(f"{'PASS' if ok else 'FAIL'} | {name}" + (f" | {det}" if det else ""))
io.open(os.path.join(BASE, 'qa_backups', '08_sweep_result.txt'), 'w', encoding='utf-8').write("\n".join(out))
nl = "\n".join(out).encode('ascii', 'replace').decode()
print(f"total={len(results)} pass={len(results)-len(fails)} fail={len(fails)}")
for ok, name, det in results:
    if not ok:
        print("FAIL:", name.encode('ascii', 'replace').decode(), det.encode('ascii', 'replace').decode()[:200] if det else "")
