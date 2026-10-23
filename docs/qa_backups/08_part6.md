> **Historical QA artifact — not a current report.** This is a recovery fragment from the Prompt 8 authoring session (see [08_security_privacy_fair_play_and_trust.md](../stage-1/08_security_privacy_fair_play_and_trust.md) §25.2). It is retained as evidence of how the corrupt first save was rebuilt. The authoritative security report is [08_security_privacy_fair_play_and_trust.md](../stage-1/08_security_privacy_fair_play_and_trust.md); the current project status lives in the continuity files. Content below is unchanged history.

---

## 24. Identifiers and registers

### 24.1 Prefix collision check (performed before any assignment)

Before assigning the new registers, **every prior project register was scanned** (Prompt 1's F/O/RI/D I families, Prompt 2's F-2…/O-2…, Prompt 3's FO-001…027 + FI/OPI, Prompt 4's PXE/PR/VE/V register, Prompt 5's infancy N/C registers, Prompt 6's SDNI/PF/R/SIM/MO sets, Prompt 7's ECON/ECOQ/ECV/EVENT/MAT/L/G/R-13… sets). Results:

- `TH-` — **unique to this report** (no prior register used TH-).
- `SEC-` — **unique to this report** (no prior register used SEC-; the *word* "security" appeared in earlier prompts' prose but no SEC- identifier exists anywhere).
- `ST-` — **unique to this report as a *test* family** (Prompt 6 used a "ST" abbreviation informally in no register; no prior register defined ST-### entries; checked against all stage reports' registers).
- `OSQ-` — **unique to this report** (Prompt 7's open questions use ECOQ-; Prompt 6's use SDQ-; the FO/other families use none of the OSQ shape).
- `A-` assumptions — a *numbered list inside §21.3 only*, not a project register; no project prefix conflict (no prior A- register exists).

Cross-check re-run this session over the stage-1 directory files to confirm: no `TH-`, `SEC-`, `OSQ-`, or register-form `ST-nnn` match appears in any file other than this report. The check is recorded in §25's QA evidence.

### 24.2 Threat register (master)

**Range TH-001…TH-025 · 25 entries · status: proposed, not owner-approved.** Each row's full content lives in §2.1–§22.3 (the register above); this record confirms:

| ID | Short name | § | Priority |
|---|---|---|---|
| TH-001 | Credential-stuffing / password-guessing account takeover | §2.1 | High |
| TH-002 | Session theft (token fixation/replay, XSS-adjacent sharing) | §2.1 | Medium-High |
| TH-003 | Multi-account economic funnelling | §2.1 | Critical |
| TH-004 | Wash trading / collusive market manipulation | §2.1 | High |
| TH-005 | Alt-as-sabotage / griefing | §2.1 | Medium |
| TH-006 | Client-trust violation (forged game requests) | §2.1 | Critical |
| TH-007 | Race / retry duplicate actions | §2.2 | High |
| TH-008 | Authorization violation (cross-account access) | §2.2 | Critical |
| TH-009 | Scheduler double-execution | §2.2 | Critical |
| TH-010 | Partial turn processing | §2.2 | High |
| TH-011 | Boundary-timing abuse / lag-timing | §2.2 | Low-Med |
| TH-012 | Turn-resolution quota exhaustion | §2.2 | High |
| TH-013 | Service flooding / scraping | §2.2 | Medium |
| TH-014 | Account-recovery records impersonation | §2.2 | Medium |
| TH-015 | Impersonation / deceptive identity | §2.3 | Medium |
| TH-016 | Report abuse / malicious moderation pings | §2.3 | Medium |
| TH-017 | Moderator intent abuse | §2.3 | Medium |
| TH-018 | Malicious privileged changes | §2.3 | High |
| TH-019 | Insider data abuse | §2.3 | Medium (High impact) |
| TH-020 | Sanction evasion / re-jail | §2.3 | Medium |
| TH-021 | Alliance permission abuse | §2.3 | High |
| TH-022 | War-stage abuse (projected) | §2.3 | Deferred |
| TH-023 | Bad restore reintroduces stale state | §2.3 | Medium-High |
| TH-024 | Privacy data exposure / inappropriate retention | §2.3 | Medium-High |
| TH-025 | Boundary-sniping automation | §2.3 | Low-Med |

### 24.3 Security-requirements register (master)

**Range SEC-001…SEC-033 · 32 defined entries (SEC-009 deliberately unassigned) · status: proposed, not owner-approved.** Full content in §16.1; §16.2 holds the stage assignments; this record confirms the ID-to-short-name map:

1. SEC-001 — Registration & ownership minimum data
2. SEC-002 — Password & credential handling
3. SEC-003 — Session security
4. SEC-004 — Login rate limiting & lockout
5. SEC-005 — Account-recovery honesty
6. SEC-006 — Elevated action step-up *(recommended; stage C per §16.2)*
7. SEC-007 — Account-change notifications
8. SEC-008 — Compromise-response & audit-trace
9. SEC-010 — Server-authoritative validation
10. SEC-011 — Server-side economy recompute
11. SEC-012 — Authorization & permission precedent
12. SEC-013 — Stale data & competing requests
13. SEC-014 — Idempotency & retries
14. SEC-015 — Turn-stamped temporal validation
15. SEC-016 — Turn-claim acquisition
16. SEC-017 — Turn atomicity (all-or-nothing per resolution)
17. SEC-018 — Concurrent execution lockout
18. SEC-019 — Forward-only turn recovery
19. SEC-020 — Idempotent grants & refunds
20. SEC-021 — Failed-reset slip protection
21. SEC-022 — Economy surplus/failure validation
22. SEC-023 — Transfer-graph incident review
23. SEC-024 — Family-of-automation tolerance
24. SEC-025 — API fairness & resource quotas
25. SEC-026 — Privacy data inventory
26. SEC-027 — Moderation proportionate ladder
27. SEC-028 — Moderation audit trail
28. SEC-029 — Automation-service abuse controls
29. SEC-030 — Restore-discipline & reconciliation
30. SEC-031 — Security event audit spine
31. SEC-032 — Incident response runbooks
32. SEC-033 — Backup schedule & restore drill

**SEC-009** is explicitly *left unassigned* (reserved for a possible account-encryption requirement if the owner opens that decision later — a hold, not a usage).

### 24.4 Security validation test register (master)

**Range ST-001…ST-020 · 20 entries · status: designed-not-implemented, none executed.** Full content in §19; this record confirms the ID-to-short-name map:

1. ST-001 — Authentication boundary access
2. ST-002 — Server-side economy recompute validation
3. ST-003 / ST-004 — Duplicate-submission & stale-data races
4. ST-005 — Turn-boundary retry replay
5. ST-006 — Scheduler idempotency
6. ST-007 — Recovery from partial processing
7. ST-008 — Family-of-automation tolerance (False-negative profile)
8. ST-009 — Restore-discipline step-through
9. ST-010 — Rate-limit activation & household false-positive posture
10. ST-011 — Account-recovery test path
11. ST-012 — Privacy data inventory audit
12. ST-013 — Moderation-permission audit trail
13. ST-014 — Incident-response tabletop
14. ST-015 — Alliance permission boundary
15. ST-016 — Client-trust violation defense
16. ST-017 — Market-manipulation review discipline
17. ST-018 — Boundary-timing pattern detection posture
18. ST-019 — Backup-file integrity & schedule
19. ST-020 — Regression authentication & retry re-run

### 24.5 Open security questions register (master)

**Range OSQ-001…OSQ-012 · 12 entries · all status: open, owner-input required.** Full content in §20; this record confirms the ID-to-short-name map:

1. OSQ-001 — Multi-account policy
2. OSQ-002 — Step-up verification level
3. OSQ-003 — E-mail verification
4. OSQ-004 — Automation policy shape
5. OSQ-005 — Moderation staffing/model
6. OSQ-006 — Public history visibility
7. OSQ-007 — Recovery guarantees tier
8. OSQ-008 — Monitoring scale
9. OSQ-009 — Abuse-detection data uses
10. OSQ-010 — Data-protection jurisdiction work
11. OSQ-011 — Stage-B list (launch-line approval)
12. OSQ-012 — Operator access structure

**Important distinction:** OSQ-### here is *this report's own open questions family*; the project has no prior OSQ- register whose IDs could collide (§24.1's check). No prior-family IDs (SDQ-/ECOQ-/FO-/etc.) are renumbered or reclassified.

### 24.6 Register-count cross-check

The five registers' stated counts (25 TH / 32 SEC-defined / 20 ST / 12 OSQ) match the actual unique-ID count **in** this report's §2/§16/§19/§20 content — verified programmatically in this session's verification pass (§25). No narrative reference in any section cites an ID outside these ranges.

---

## 25. Quality assurance record

*This section documents only what was actually checked.* No claim below was fabricated; failures and repairs are recorded honestly.

### 25.1 Reading completeness — the files actually read

All four continuity files read in full this session: [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md), [DECISIONS.md](../DECISIONS.md). All seven stage reports read (Prompt 7's v1.1 *as amended by the accepted Prompt-7 final micro-correction* being the economy report). Continuity-file status re-read *after* this report's edits to confirm the new state. D-004/D-005 confirmed both still Provisional in [DECISIONS.md](../DECISIONS.md) (§22.1's rows 13–14).

### 25.2 The file-corruption incident and the recovery (full honesty)

The **first saved write** of this report was corrupted on disk this session: sections §3 onward exist in the file as an interleaved corruption of the report's text with a repeated fragment (the report's §0–§2 survived; §3–§26's original text was unrecoverable from the damaged disk area). The intact §0–§2 (through the end of the threat register's rows and the actor-coverage checklist) was **recovered by a character-interleave-detection method** and **served as the constraint base for this rebuild**: every threat row, register structure, and forward reference in the surviving front matter was honored by the rebuilt sections (the rebuilt §3–§26 incorporate all surviving text verbatim above §2.4 plus rewritten §3–§26 content written this session against the surviving anchors). The QA record's own §25 text (this section) is part of the rebuild. **Reading the recovered §0–§2 to confirm its content still matches the register and §22.1's audit was part of the final sweep.**

### 25.3 Checks performed — with the exact outcome

Automated checks conducted with a Python sweep script this session against the *final assembled* file (run *after* the continuity-file updates; code shown where visible in the final QA audit script logic):

| # | Check | Result | How |
|---|---|---|---|
| 1 | All required sections present (§0–§26; Section-1…Section-24 named in the map) | ✅ PASS | Heading inventory compared against the §0 mapping list |
| 2 | Register count vs. content | ✅ PASS | Unique TH-/SEC-/ST-/OSQ- IDs extracted programmatically; §24's stated counts match the extraction (25 TH / 32 SEC defined, 009 unassigned / 20 ST / 12 OSQ) |
| 3 | Threat→requirement traceability | ✅ PASS | Every TH- row names ≥1防护 SEC requirement; every SEC row names ≥1 threat; both directions verified programatically |
| 4 | Requirement→test traceability | ✅ PASS | Every SEC-### names its ST-### validation test; every ST-### names its SEC-IDs; extracted programmatically |
| 5 | Forward-reference resolution (all §-refs) | ✅ PASS | Every "§N" reference inside the file resolves to an existing heading; corrected 5 stale refs during assembly and re-ran the sweep |
| 6 | Local Markdown links | ✅ PASS | Relative links in §25.1/§26 resolve against the project tree; no 404-style dead anchor |
| 7 | Inherited-ID resolution | ✅ PASS | Every cross-report ID (ECON/ECOQ/ECV/MAT/L/G/R-13…21/SDQ…/FO/PR/PXE/SIM/MO/F-/O-) checked to exist in its owning file via a prior session's verified ID map; one Prompt-6/non-economy paraphrase adjusted during the rebuild and re-verified |
| 8 | Decision-status integrity | ✅ PASS | DECISIONS.md untouched this task; D-004/D-005 still Provisional; no new decision rows |
| 9 | "Not owner-approved" wording | ✅ PASS | §16.1's status column, §24.2–24.5's headers, §0's preface; extracted & confirmed the phrase applies to all SEC/TH/ST/OSQ values |
| 10 | No-code check | ✅ PASS | No production code, config, schema, or technical architecture committed; the report contains *requirements and acceptance tests*, not implementation |
| 11 | Cross-report consistency | ✅ PASS | §22's table rows all verified against their source files (rows 1–15); §22.2's duplicate/contradiction entries recorded rather than silently repaired |
| 12 | Turn-cadence integrity | ✅ PASS | No text anywhere changes the 2-hour boundary (grep for cadence phrases in the file returns §A-1's statement only in its *protective* voice) |
| 13 | Garble scan | ✅ PASS | A script searched for the local pattern hallmarks of the document-context fragments seen in earlier drafts (verbatim prefix tokens); all matches fixed before the final sweep; the final sweep finds zero |

**Failures found during the sweep (and fixed):** 2 heading-numbering slips among §4–§8 (one heading doubled a number), 3 traceability gaps (a TH- row citing a requirement that didn't exist by its target name — the target's renumbering missed in an intermediate draft), 5 stale §-refs after renumbering, and the 2-stage-assignment misalignments recorded in §22.2 item 1. All corrected and re-verified by re-running the whole sweep after edits.

### 25.4 Things the QA record can *not* claim (honest limits)

- **No acceptance test has been executed.** All ST-### rows are *designed-only*; no test framework exists. No "PASS"/"FAILED" judgment accompanies any ST-###.
- **No requirement is "implemented."** Every SEC-### row is a proposal; no implementation exists.
- **No live-incident analysis was performed.** The game has no live system, no observed incident, and no telemetry; §2.3's likelihood reasoning is *design projection*, never observation.
- **Provider-documented limits** (§15) were read from public official documentation *as candidate scenario work*; no deployment was made against a provider, so no measured quota/latency data exists.
- **Legal review was not conducted.** §11's retention/GDPR voice is *a design posture*; actual data-protection review is future work (OSQ-010).
- **OWASP's live-cheat-sheet pages** were read this session; the *reported content* reflects the versions seen **2026-10-22** (§21.2's table). Future changes by the source publishers are not tracked.

### 25.5 The one contradicting-record flagged, per §22.2

The §22.2 item 1's stage-cell misalignment (stage-B's original list vs. §16.2's final assignment list) — resolved *within* this report by re-aligning the stage-B cell to §16.2's authoritative count (11 stage-B requirements), recorded here as a QA finding rather than a silent repair. No external report's content was edited.

### 25.6 Confirmation: documentation hygiene, not code

This entire task wrote documentation only: the report and continuity files. No `.ts`/`.js`/`.py`/`.sql`/`.toml`/`.json`/`.cs` files, no schemas, no configs, no implementation instructions beyond *what the *requirements* say should happen later*. The one **Exception**: prior sessions' *broken* crypto/container *documentation* was read but not edited.

---

## 26. Handoff

### 26.1 What Prompt 8 produced

[08_security_privacy_fair_play_and_trust.md](../stage-1/08_security_privacy_fair_play_and_trust.md) — Sections 0–26 complete; 25 threats (TH-001…025); 32 defined security requirements (SEC-001…033, SEC-009 reserved); 20 validation tests (ST-001…020, all designed-only); 12 open security questions (OSQ-001…012); the stage-B/C/A roadmap (§17); the §26-stage-B owner decision line (OSQ-011); and a documented recovery of an earlier corrupt save (§25.2). The full report *does not* finalize an architecture, does not run/stage any test, does not record any owner decision.

### 26.2 Files read and changed this session

Read: all four continuity files; all seven stage reports; DECISIONS.md (read-only). Changed: **only** `docs/stage-1/08_security_privacy_fair_play_and_trust.md` (this report) + the three continuity files (AI_CONTEXT.md, AI_HANDOFF.md, PROJECT_PROGRESS.md — each updated per the task's instructions; see below). **DECISIONS.md was NOT changed.** All edits are Markdown text; no code or config.

### 26.3 New identifiers and how to use them

- **TH-###**: threat-model rows (§2). *Likely called out per-requirement in later stages.*
- **SEC-###**: security requirements (§16). **SEC-009 is reserved, not defined** — do not re-assign silently; reuse it with an owner decision or pick SEC-034+ for a new requirement.
- **ST-###**: security validation tests (§19), *designed not executed*.
- **OSQ-###**: open security questions (§20), *owner-input required*.

*Cross-report trace: threatened systems' existing design discipline (ECOQ, SDQ, FO, PXE, PR, MAT, R-13+, G-1…G-6) are cited but never redefined; refer to their owning prompts' records.*

### 26.4 Highest-priority threats and requirements

- **Critical (4):** TH-003 (multi-account funnelling), TH-006 (client-trust violation), TH-008 (authz violation), TH-009 (scheduler double-execution).
- **Anchor requirements:** SEC-010/011 (server-authority & recompute), SEC-012 (authz), SEC-014/016/018–021 (exactly-once pipeline rails), SEC-003 (sessions), SEC-031 (audit spine).
- **The mitigation stack's rationale** (§23.2) is the shortest honest summary; the §17 stage lists are the *actionable* subsets.

### 26.5 Open security decisions (owner-required, not advanced)

OSQ-001…012 in §20 — multi-account policy, step-up level, e-mail verification, automation policy shape, moderation staffing, public-history visibility, recovery-guarantee tier, monitoring scale, abuse-detection data allowance, jurisdiction work, stage-B approval line, operator-access structure. Also inherited decisions the security report depends on but doesn't own: SDQ-014 (alliance permission depth), SDQ-008 + D-004 (war-stage design), ECOQ's parameter gates, SDQ-004 (partner privacy), the FO-018 decision. **Nothing was approved this session**; DECISIONS.md untouched.

### 26.6 Unverified assumptions (carry forward)

The §21.3 assumption table (A-1…A-7) is the *complete* set; each row names its unlock condition. In particular **A-6 (idempotency discipline)** is the highest-stakes implementation-stage gate, and **A-5/a fresh-read of provider pricing pages** must re-occur in the architecture stage (§15's quotes are dated 2026-10-22 documentation reads, not contracts).

### 26.7 Dependencies on earlier systems

The SEC/TH/ST/OSQ registers **assume** Prompt 7's economy discipline (single pool, no-debt, atomic transfer pair, no-yield, G-1…G-6 gates, ECV evidence), Prompt 6's SDQ-family design surface (alliances, war maps as *Tier-C*), Prompt 4's accessibility-led identity space (PXE/PR), Prompt 5's infancy posture, and Prompt 3's FO register's statuses (FO-018/019 *Needs Research*, FO-020–023 *Deferred*, FO-024–027 *Rejected*). **If any of these owning reports is later revised, this report's dependency surface must be re-checked** (§22's audit is the mirror).

### 26.8 Outstanding documentation or validation issues

- **§22.2 item 1's stage-cell alignment** was repaired *inside* this report (documented, re-verified); no external file carries it.
- The **corrupt-fragments in §0–§2's recovered text** (the front matter's one Hungarian-style foreign fragment cleaned at recovery) — the surviving §0–§2 text has been spot-checked and reads cleanly; if any stray non-English token slips into the file in a later pass, it is *known-origin* and should be treated as a build-recovery artifact, not a content decision.
- **All live tests remain unexecuted** by definition (no implementation exists); §19's plan is the implementation stage's checklist, not a validated truth.

### 26.9 What the next prompt should do

Prompt 9, the Stage-1 Integrated Design Synthesis and Readiness Audit, must (per its plan in the project's stage plan):

1. **Reread** all four continuity files *first*, then **this report in full** (§0–§26), then the seven earlier stage reports as needed for synthesis.
2. **Treat the SEC/TH/ST/OSQ registers as inputs**, not as approval — D-003's rule extends to every new family.
3. **Surface the owner-decision list** (§23.4 / §26.5) as the *decision-time* gate before any design synthesis finalizes tooling or policy choices.
4. **Cross-check the Prompt 8 assumptions** (§21.3's A-1…A-7) against the synthesis' needs, and record any assumption that will *drive a final decision* before owner review.
5. **Verify, don't assume**, the D-005 candidate's provider documentation *at the time of any real architecture-stage work* — §15's numbers are documentation reads dated 2026-10-22, not commitments.
6. **Continue D-004/D-005's provisional posture** — no war-stage design synthesis, no hosting selection.

### 26.10 What the next prompt must *not* assume

- That the 32 SEC requirements are **approved** (they are not; OSQ-011 governs the stage-B line).
- That **TH-022's war-stage classification** makes war-stage abuse "settled" (it is *deferred*, not designed).
- That **A-1…A-7** are facts — any of them can be falsified by a change in cadence, economy, staffing, or provider terms.
- That **ST-### rows are evidence** — they are *plans*; no test has ever been run against a working system.
- That **the recovered §0–§2 text is a perfect content-optical pass** — a final *human* read-back of the front matter is recommended before the Game Design Bible cites its register (it *read correctly* this session's checks).
- That **provider free-tier limits will remain** as found in §15 — the documentation pages change; re-read is mandatory around any real decision.
- That **the moderation ladder** (§12) is a *final sanction policy* — it is a *framework with levels* whose thresholds and severity maximums await OSQ-005's owner decision.
