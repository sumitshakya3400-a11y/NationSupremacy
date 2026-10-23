import re, os, io

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
check("section titles non-empty", all(nm.strip() for _, nm in h2))

# ---------- 1. register extraction ----------
th  = sorted(set(re.findall(r'\bTH-(\d{3})\b', t)))
sec_all = sorted(set(re.findall(r'\bSEC-(\d{3})\b', t)))
sec = [x for x in sec_all if 1 <= int(x) <= 33]
st  = sorted(set(re.findall(r'\bST-(\d{3})\b', t)))
osq = sorted(set(re.findall(r'\bOSQ-(\d{3})\b', t)))
check("TH register contiguous 001-025", th == [f"{i:03d}" for i in range(1, 26)], f"N={len(th)}")
check("SEC register: 33 ids in 001-033 incl. reserved 009", sec == [f"{i:03d}" for i in range(1, 34)], f"N={len(sec)}")
check("narrative SEC mentions beyond 033 are only SEC-034+", [x for x in sec_all if int(x) > 33] == ['034'], f"extra={[x for x in sec_all if int(x) > 33]}")
check("ST register contiguous 001-020", st == [f"{i:03d}" for i in range(1, 21)], f"N={len(st)}")
check("OSQ register within 001-012", all(1 <= int(x) <= 12 for x in osq), f"N={len(osq)}")

m9 = re.findall(r'SEC-009[^\\n]{0,120}'.replace('\\\\','\\'), t)
m9 = re.findall(r'SEC-009[^\n]{0,120}', t)
ok9 = all(('reserv' in s.lower() or 'unassign' in s.lower() or 'gap' in s.lower() or 'placeholder' in s.lower()) for s in m9)
check("SEC-009 only ever described as reserved/unassigned", ok9, [(s[:60] if not ok9 else '') for s in m9])

# ---------- 2. traceability ----------
def section(n):
    m = re.search(rf'^## {n}\. ', t, re.M)
    if not m: return ""
    nxt = re.search(rf'^## {n+1}\. ', t, re.M)
    return t[m.start(): nxt.start() if nxt else len(t)]

s2, s16, s19, s20 = section(2), section(16), section(19), section(20)

rows_no_sec_th, seen = [], set()
for line in s2.splitlines():
    mrow = re.match(r'\s*\|\s*(TH-\d{3})\s*\|', line)
    if mrow and mrow.group(1) not in seen:
        seen.add(mrow.group(1))
        if not re.search(r'\bSEC-\d{3}\b', line):
            rows_no_sec_th.append(mrow.group(1))
absent = sorted(set(re.findall(r'\b(TH-\d{3})\b', s2)) - seen)
check("every threat has a register row in section 2", not absent, f"absent: {absent}")
check("every section-2 threat row cites >=1 SEC requirement", not rows_no_sec_th, f"missing: {rows_no_sec_th}")

sec_ids = sorted(set(re.findall(r'\bSEC-(\d{3})\b', s16)))
no_th  = [s for s in sec_ids if not re.search(rf'\bSEC-{s}\b(?=(?:(?!\n## ).)*?\bTH-\d{{3}})', s16, re.S)]
no_st  = [s for s in sec_ids if not re.search(rf'\bSEC-{s}\b(?=(?:(?!\n## ).)*?\bST-\d{{3}})', s16, re.S)]
no_sec = [s for s in st   if not re.search(rf'\bST-{s}\b(?=(?:(?!\n## ).)*?\bSEC-\d{{3}})', s19, re.S)]
check("every SEC row cites >=1 TH threat", not no_th, f"missing: {no_th}")
check("every SEC row cites >=1 ST test", not no_st, f"missing: {no_st}")
check("every ST test cites >=1 SEC requirement", not no_sec, f"missing: {no_sec}")

osq_ids = sorted(set(re.findall(r'\bOSQ-(\d{3})\b', s20)))
check("section 20's OSQ rows are contiguous 001-012", osq_ids == [f"{i:03d}" for i in range(1, 13)], f"{osq_ids}")

# ---------- 3. section refs ----------
refs = re.findall(r'(?:§|Section\s+)(\d{1,2})(?!\.\d)', t)
refs = sorted(set(int(r) for r in refs if 0 <= int(r) <= 99))
bad_refs = [r for r in refs if r not in secs]
check("all top-level §-refs resolve to existing sections", not bad_refs, f"bad: {bad_refs}")

headings = {(int(a), int(b)) for a, b in re.findall(r'^\#{2,4} (\d{1,2})\.(\d{1,2}) ', t, re.M)}
bad_sub = []
prompt_spans = [(pm.start(), pm.end()) for pm in re.finditer(r'Prompt \d+ [^;|\n]{0,80}', t)]
for mt in re.finditer(r'§(\d{1,2})\.(\d{1,2})', t):
    is_prompt = any(ps <= mt.start() <= pe for ps, pe in prompt_spans)
    n, m_ = int(mt.group(1)), int(mt.group(2))
    if not is_prompt and (n, m_) not in headings:
        bad_sub.append(f"{n}.{m_}")
check("all §N.M refs resolve to existing headings", not bad_sub, f"bad: {sorted(bad_sub)}")

# ---------- 4. local markdown links ----------
badlinks = []
for l in re.findall(r'\]\((?!http)([^)]+)\)', t):
    target = l.split('#')[0]
    if not target: continue
    if not os.path.exists(os.path.normpath(os.path.join(BASE, 'stage-1', target))):
        badlinks.append(l)
check("all local markdown links resolve", not badlinks, f"bad: {badlinks}")

# ---------- 5. inherited IDs resolve in owning report(s) ----------
owners = {
    r'ECON-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'ECOQ-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'ECV-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'MAT-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
    r'EVENT-\d{3}': ['stage-1/07_economy_design_and_market_structure.md'],
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
    r'\bV-\d\b': ['stage-1/04_target_audience_and_player_experience.md'],
    r'\bAP-\d{3}\b': ['stage-1/05_core_game_concept_and_design_pillars.md'],
    r'FO-\d{3}': ['stage-1/03_feature_comparison_opportunity_analysis.md'],
    r'\bF-\d{1,3}\b': ['stage-1/02_strengths_weaknesses_player_frustrations.md', 'stage-1/05_core_game_concept_and_design_pillars.md'],
    r'\bO-\d{1,2}\b': ['stage-1/02_strengths_weaknesses_player_frustrations.md'],
}
files = {}
for own in set(sum(owners.values(), [])):
    try: files[own] = open(os.path.join(BASE, own), encoding='utf-8').read()
    except OSError: files[own] = ""
bad_ids = []
for pat, owns in owners.items():
    for m in sorted(set(re.findall(pat, t))):
        # skip narrative family-annotation mentions like "F-2…/O-2…"
        i0 = t.find(m)
        after = t[i0 + len(m): i0 + len(m) + 3] if i0 != -1 else ""
        if after.startswith('…') or after.startswith('...'):
            continue
        found = any(re.search(r'(?<![\w-])' + re.escape(m) + r'(?![\w])', files[o]) for o in owns if o in files)
        if not found:
            bad_ids.append(f"{m} -> {owns[0]}")
check("all inherited IDs resolve in their owning report(s)", not bad_ids, f"bad: {bad_ids}")

# ---------- 6. decision discipline ----------
d = open(os.path.join(BASE, 'DECISIONS.md'), encoding='utf-8').read()
check("D-004 still Provisional", 'Provisional' in d and 'D-004' in d)
check("D-005 still Provisional", 'Provisional' in d and 'D-005' in d)
check("no new D-007+ rows added", not re.search(r'\bD-00[7-9]\b|\bD-01\d\b', d))
check("report claims proposal-only status", t.count('not owner-approved') >= 3, f"count={t.count('not owner-approved')}")

# ---------- 7. turn cadence + walkthroughs + hygiene ----------
check("2-hour cadence present", '2-hour' in t or 'two-hour' in t)
wids = set(re.findall(r'W-18-([A-Z])\b', t))
check(">=12 W-18 walkthrough scenarios", len(wids) >= 12, f"n={len(wids)}")
bad = re.compile(r'[\u0400-\u04FF\u3040-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF\u0621-\u064A]')
check("no foreign-token artifacts", not bad.search(t))
check("no U+FFFD replacement chars", '\ufffd' not in t)
check("no stray question-mark ID refs (X-###?)", not re.search(r'\b[A-Z]{2,4}-\d{1,3}\?', t))

# ---------- output ----------
out = []
fails = 0
for ok, name, det in results:
    out.append(f"{'PASS' if ok else 'FAIL'} | {name}" + (f" | {det}" if det else ""))
    if not ok: fails += 1
io.open(os.path.join(BASE, 'qa_backups', '08_sweep_result.txt'), 'w', encoding='utf-8').write("\n".join(out))
print(f"total={len(results)} pass={len(results)-fails} fail={fails}")
for ok, name, det in results:
    if not ok:
        print("FAIL:", name, "|", (det or "")[:300].encode('ascii','replace').decode())
