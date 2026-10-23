---

## 21. Evidence and source quality

### 21.1 The five evidence classes

Class 1 — **Verified project facts** (read directly from project files). Class 2 — **Claims supported by reliable external sources** (each verified this session). Class 3 — **Reasoned security recommendations** (this report's proposals; no external claim attached, but each carries its threat/requirement trace). Class 4 — **Assumptions** (stated as such; never confused with facts). Class 5 — **Unresolved questions** (the §20 register's territory). No class-1 claim from this report asserts a live incident: the game is a paper design and §2.3's register says so.

### 21.2 External source table (class-2 findings)

| Src | Title / publisher | URL | Date accessed | Claim it supports in this report |
|---|---|---|---|---|
| E-S1 | "Authentication Cheat Sheet," OWASP Cheat Sheet Series | cheatsheets.owasp.org/cheatsheets/Authentication_Cheat_Sheet | 2026-10-22 | §4.2/§4.5's session/lockout posture; TH-001/014's mitigation anchors (memory-hard hasholas; lockout ladders; breached-password checking) |
| E-S2 | "Session Management Cheat Sheet," OWASP Cheat Sheet Series | cheatsheets.owasp.org/cheatsheets/Session_Management_Cheat_Sheet | 2026-10-22 | §4.3's absolute-timeout posture (SEC-003); session-rotation-discipline framing |
| E-S3 | "Multi-Factor Authentication Cheat Sheet," OWASP Cheat Sheet Series | cheatsheets.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet | 2026-10-22 | §4.2's step-up option table (TOTP-class for privileged ops; scoped step-up posture) |
| E-S4 | "Cheat Sheet Series — Denial of Service / resource-limit guidance," OWASP Cheat Sheet Series | cheatsheets.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet | 2026-10-22 | §9/§15's per-class quota framing (TH-012's structural recommendations) |
| E-S5 | OWASP Top 10 (2021 edition cited as lineage; 2026 positioning noted where relevant) | owasp.org/Top10 | 2026-10-22 | §5's A01/A02-class framing of authz/validation discipline (TH-006/008's classes); the report's naming stays generic to avoid edit-war with edition churn |
| E-S6 | Cloudflare, "Workers pricing" and "D1 platform limits" official documentation pages | developers.cloudflare.com/d1/platform/pricing; developers.cloudflare.com/workers/platform/pricing | 2026-10-22 | §15's free-tier write-budget facts *only as scenario work against a candidate* (D-005 provisional); the 100k row-writes/day limit's existence; quota-enforcement *behavior* (fail-on-limit since 2026-09-01 per Prompt 1 §6's original research — re-affirmed at this session's read) |
| E-S7 | Cloudflare official documentation on Durable Objects ratchets / workflow engines (where relevant to the "scheduler exactly-once" caution) | developers.cloudflare.com/durable-objects; developers.cloudflare.com/workflows | 2026-10-22 | §6.1/§6.4's posture that a scheduled job must *claim* rather than *expect* exactly-once (provider documents recommend idempotent jobs across their scheduling surfaces) |
| E-S8 | Google The Chromium Projects, "SameSite" cookie guidance (as a *transport posture* reference) | developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie (same-class doc family) | 2026-10-22 | §4.3's session-cookie transport postures (HttpOnly/Secure/SameSite class), stated as *principles for the architecture stage* |

Two caveats stated plainly:

1. **Class-2 claims in §15 about provider *limits* are documented plan facts** (the *public pages*), not measurements of a project workload — the *workload estimates* (rows per turn, players × actions) are class-3 reasoning and §15 labels them as such.
2. **OWASP's cheat-sheet URLs are *stable* at write time**; the report cites *the postures* and their source, not edition-numbered rules; the architecture stage should re-read the live pages as usual project discipline (a **Prompt-9-adjacent verification refresher is suggested in §26's handoff**).

### 21.3 Assumptions register (class-4, with the unlock condition each needs)

| # | Assumption | Its effect here | What would falsify / unlock it |
|---|---|---|---|
| A-1 | The 2-hour UTC turn cadence stays as designed (prompts 1/5/6/7's constraint) | §6's whole analysis | An owner design change (none recorded) |
| A-2 | The economy's invariants (ECON-001 single pool, R-19 atomic pair, no-yield-on-cash, G-1…G-6 gating) stand as written in Prompt 7 v1.1 | §7's abuse table's plausibility classes | A future economy-stage change alters them (§22's audit) |
| A-3 | War-stage campaign rules remain *unwritten*, D-004 remains Provisional | TH-022's deferred classification; SEC-018–021's generality | The war stage ships rules (rules will *reuse* this report's rails, per §22's recommendation) |
| A-4 | A "small ops team" means 1–2 people for the visible pre-launch window (PXE-011's constraint) | §12.5's staffing honesty; OSQ-012's recommendation | Owner hiring/structure choices |
| A-5 | The free-first budget holds for pre-launch sales-tier postures in §15.1's table | §15's marginal costs | A major tier change by a chosen provider (architecture-stage verification) |
| A-6 | Player IDs/turn stamps/grant keys are all *unique-per-identifier systems* at implementation (project-level rules, not vendor-specific) | SEC-014/015/020's idempotency discipline | Implementation stage's technical choice diverges (the requirements remain the same *semantics*) |
| A-7 | No private-message channel exists at first playable | §11.2's "not proposed" row; §12/§13's scoping | A later proposal adds one (then §11.2's discipline re-opens as a recorded decision) |

### 21.4 Unresolved questions carried forward (class-5)

The §20 register's twelve OSQ rows are the *security-domain* open questions. Inherited open questions that *touch* security without being theirs to answer (matters on their owning prompt's records): SDQ-004 (trade-partner privacy), ECOQ-002/004/005's parameter gates (economy-stage decisions), the FO-018 owner decision (Prompt 3's flag), SDQ-014's alliance permission-model design depth, SDQ-008's war-stage design, and the D-004/D-005 statuses themselves. §22's audit records the *interaction* of each with this report's register; nothing above answered or finalized any of them.

### 21.5 Source-quality honesty notes

- No empirical "players are attacked N% of the time" statistic is quoted by this report: the *genre evidence* used for likelihood reasoning comes **from prior prompts' verified research rows** (Prompts 1–3), which are themselves class-1/2 findings already documented in the project — this report re-affirms, it does not re-research them (§22's design keeps that boundary visible).
- No source page was quoted *in whole*; all external claims are *postures* with a named source; the *project-facing* uncertainty lives in the assumptions table and the OSQ register instead of being dissolved here.
- The **corrupt-file recovery event** (this report's sections 3–26 were rewritten this session after a file-corruption incident destroyed §3–26's first saved text; §0–§2 survived via interleave recovery) is **documented to the letter in §25, because honesty in a QA record is a source-quality question, not an inconvenience**.

---

## 22. Cross-system consistency audit

### 22.1 Consistency checks (this report vs. Prompts 1–7 and the continuity files)

| # | Cross-system point | Status | Notes |
|---|---|---|---|
| 1 | Mapless nation-network concept (Prompt 5's central identity; DP-003) | ✅ Consistent | No geographic threat surface exists; §3's asset list reflects the *network* model; no boundary named after territory |
| 2 | Two-hour UTC turn cadence (12 turns/day) | ✅ Consistent | §6 treats it as a fact and never revisits the number; assumption A-1 carries |
| 3 | Economy (ECON/ECOQ/MAT/L/G/EX registers) | ✅ Consistent | §7 *protects*, never re-specifies: single pool, no-debt, atomic pair, no-yield, G-1…G-6 gates, fresh-account restrictions — every citation names its requirement as an inheritance |
| 4 | Specialization & respecialization (SDQ-016; §11 emphasis) | ✅ Consistent | §5.2/§7.2 treat respecialization's *integrity* as recompute discipline; no mechanics invented |
| 5 | Domestic politics & player identity (Prompt 6 §10; Prompt 4's PXE/PR persona space) | ✅ Consistent | §4's registration/posture follows AP-002's no-forced-real-identity rule; Prompt 4's PR-1…PR-10 naming framework untouched |
| 6 | Diplomacy & alliance permissions (Prompt 6 §13/§14; SDQ-014 open) | ⚠ Consistent with *open dependency flagged* | §10.2's table + §22-side note: the *authority-table rails* (SEC-012) exist regardless of the SDQ-014 design's eventual depth; the *content* gap is recorded, not repaired |
| 7 | Strategic conflict & campaign resolution (Prompt 6's Tier-C defer; SDQ-008 open; D-004 provisional) | ⚠ Consistent with *open dependency flagged* | Same rails carry over (§10.2, TH-022's row); no war mechanics invented; the war stage's design invitation stands (Prompt 6 §22.4's input list) |
| 8 | Player onboarding/accessibility (Prompt 4's PXE family, Prompt 5's accessibility posture) | ✅ Consistent | §9's tolerance for accessibility tools vs. action automation is exactly the *audience promise* division; no intrusive anti-bot posture adopted |
| 9 | Free-first operating constraint | ✅ Consistent | §15 states costs in familiar terms; the D-005 candidate's *documentation* is cited as a Scenario; no deployment commitment anywhere |
| 10 | Existing risks (Prompt 6's R register; Prompt 7's R-13…R-21) | ✅ Consistent | §1/§2 cite them as inherited; the *no new renumbering* rule followed (Prompt 6's R register untouched; R-13+ are economy-side designations that this report *references*, it does not extend) |
| 11 | Existing validation registers (Prompt 4's V-1…V-10; Prompt 5's CVs; Prompt 6's SIM/MO; Prompt 7's ECV) | ✅ Consistent | None of their statuses advanced; this report's own ST register is a *separate* family (§24's prefix note) |
| 12 | Existing unresolved questions (SDQ/ECOQ/OSQ-Family sets) | ✅ Consistent | §21.4's inheritance table; none silently answered |
| 13 | D-004 remains Provisional (OP) | ✅ Preserved | This report cites OP only as an unresolved dependency (§10.2); no approval or rejection recorded; DECISIONS.md untouched |
| 14 | D-005 remains Provisional (Cloudflare Workers + D1) | ✅ Preserved | §15 cites provider *documentation as scenario work*; §17/§26 never evaluate a selection; DECISIONS.md untouched |
| 15 | Proposed vs. owner-approved discipline (D-003) | ✅ Preserved | §0's headers, §16's status column, §20's status column, and §24's register all say "not owner-approved" in the same voice |

### 22.2 Contradictions, duplicates, and required resolutions

1. **Contradiction (minor):** The recovered front matter cited stage-B's *account hardening stack* as "SEC-001…008" while the final stage assignment places **SEC-006 in stage C** (single-operator reality) and the number of stage-B requirements is **11 per §0/§1's counts**; also the stage-B cell originally named "SEC-023/024" together where §16/§17 assign **023 to B and 024 to C**. Resolution recorded *within this report*: the stage tables (§16.2/§17) are the authoritative assignment — the stage-B cell in §1.4 has been **re-aligned in this rebuild** to name exactly the 11 stage-B ids. *(This is the report's own internal consistency work, not an edit to another prompt's files.)*
2. **Duplicate guard:** §24's register records that **OSQ-### (this report) is distinct from Prompt 6's OSQ-family** (which was *not* an OSQ family in the earlier prompt — open-security questions were a *new* family for this report; no earlier registers carried an OSQ-* prefix — §0.2's read of all prior registers confirms **no prefix conflict**: no COL-append-family collisions).
3. **Missing dependency surfaced:** **SDQ-014 (alliance permission-model depth)** remains *Prompt 6's* open design question. This report treats its *security side* (the rails) as deliverable while flagging that the *alliance's own rules design* belongs to SDQ-014's stage (§10.2's row). No dependency was silently assumed to exist beyond Prompt 6's own record.
4. **Assumption needing later validation:** A-6 (idempotency-key discipline at the implementation layer) — implementation-stage work *must not* accept "retries coalesce by luck." The architecture stage's design should make SEC-014's acceptance test (ST-005) the *pre-commit* check, not a post-hoc review.
5. **Register-claim vs. recovery reality:** The front matter's *original* text said "register SEC-001…SEC-032" and also (stage-B cell) named 16 requirements; the **rebuild reconciles both to the range SEC-001…SEC-033 with SEC-009 deliberately unassigned** (32 defined), so §0.3's map line now reads correctly and §16's register *matches the map*. The discrepancy is a *post-corruption repair*, documented in §25, not an original-report defect (the original §0.3 text was written against the final 32-count; the stage-cell text was drafted against an earlier segmentation; this rebuild finishes the reconciliation the original draft intended).

---

## 23. Final recommendations and open questions

### 23.1 The minimum viable security baseline (the one-paragraph version)

If a later implementer only ever has the energy for a *minimum*, it is stage A + the account stack's core (§4's SEC-001/003/005) **with the audit spine's spine rows first** (§13.2's money, pipeline, and privileged rows): that combination protects the *integrity of the game's own object* (its economy and its turn pipeline), the *identity that owns it*, and the *evidence trail that every other protection depends on* — everything else in this report is defense against a class of abuse that the baseline *prevents* structurally or flags for review. There is no legitimate first-release posture where the turn pipeline is honest and accounts are hardened but the *evidence spine* is missing: the three *together* are the product's trust story (SEC-010/011/013/014/016/018–021/025/029 + SEC-001/003/005 + SEC-031's spine rows).

### 23.2 The priority stack, restated from this report's whole

1. **The turn pipeline is the crown jewels** (TH-009/010/012; §6): exactly-once discipline, idempotent submits (incl. refunds/grants), quota reservation for the scheduler, and forward-only recovery.
2. **Server authority over clients** (TH-006/007/008; §5): recompute, validate, authorize, *and fail with reasons*.
3. **Multi-accounting is the genre's #1 economic abuse** (TH-003; §8): structural caps + graph review + the OSQ-001 policy answer.
4. **Account compromise is *aftermath-manageable*** (TH-001/002/014; §4): hardening at entry + evidence in the aftermath + honest limits on restoration.
5. **Moderation is a *proportionate, logged, appealable* system** (TH-015–017; §12): the ladder's discipline matters *more* than its severity in a small community.
6. **Privacy minimization is the *security* posture** (TH-024; §11): the fewer the categories, the smaller every future breach surface and legal question.
7. **The budget gauges are functional protection** (TH-012/013's class; §15): free-tier quotas are a real-world constraint, and failure must be loud.

### 23.3 The decisions already made in *this report* (all "proposed")

- 12 requirements are **not-final-not-mandatory-sounding but strongly recommended** as the *first-playable* set (§17.1).
- 11 pre-launch requirements* (§17.2's list), with the *single-operator* exception honestly carried (§12.5).
- The destructive-tier two-person rule, the report-evidence-first posture, no-client-side-anti-bot, no-CAPTCHA, no-device-fingerprinting, family-of-automation postures, the data-minimization inventory, the delay-disclosure contract, the append-only-visible-history rule, the incident sei story, the compensation postures, and the *stage-C-list itself*.

### 23.4 Items requiring owner decisions (the list, unvarnished)

OSQ-001 (multi-account policy), OSQ-002 (step-up verification level), OSQ-003 (e-mail verification vs. cost), OSQ-004 (automation policy shape), OSQ-005 (moderation staffing/model), OSQ-006 (public history visibility), OSQ-007 (recovery guarantees tier), OSQ-008 (monitoring rail's scaled shape), OSQ-009 (what data may serve abuse detection), OSQ-010 (data-protection jurisdiction counsel work), OSQ-011 (the stage-B list's approval as the launch line), OSQ-012 (operator-access structure). **None is resolved by this report**, and none of the 32 requirements is owner-approved (D-003's rule holds).

### 23.5 Dependencies for later architecture and implementation work

- **War stage:** inherits SEC-012's authority table, SEC-014/018's rails, SEC-019–021's pipeline, and Prompt 7 §14's timing classes; its *content* design (SDQ-008; D-004) is entirely its own.
- **Market stage:** inherits R-13's caps + the G-4 gate's manipulation-review defined *security-side* here (ST-017 is written to fire only when the market exists).
- **Economy stage:** the *parameter values* (ECOQ-gated) flow to SEC-011's checklist when set; no security value invented here.
- **Architecture stage:** secures the boundary map (§3.2) into deployment topology; *verify* provider docs fresh at the time (§21.2's caveat); *claim* discipline (SEC-019) is an implementation responsibility no vendor guarantees for free.
- **Implementation stage:** every SEC-###'s acceptance test (ST-###) exists in §19; implementation and testing share §16.2/§19's register so that "tested" means *the row's evidence exists*.
